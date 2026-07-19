#!/usr/bin/env python3
"""Nipponexus 薄記事底上げ自動下書き (DeepSeek V4 Flash + OpenRouter webプラグイン)
工程1 DB薄記事取得 -> 工程2 検索接地下書き -> 工程3 検算 -> 工程4 照合レポート出力(ここで停止)
工程5(本番投入)は既存の投入ブロックへ手動接続。本スクリプトは本番非反映(llm_sim出力のみ)。
使い方:
  python3 scripts/deepseek_draft.py --auto        # 最優先の薄記事1件
  python3 scripts/deepseek_draft.py --qid Q123456 # qid指定
"""
import os, re, json, time, sqlite3, argparse, pathlib, urllib.request, urllib.error

DB   = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")
ENV  = os.path.expanduser("~/.openclaw/.env")
OUT  = pathlib.Path(os.path.expanduser("~/nexus_data/llm_sim"))
MODEL = "deepseek/deepseek-v4-flash"

def get_key():
    m = re.search(r'^OPENROUTER_API_KEY=(.+)$', pathlib.Path(ENV).read_text(), re.M)
    if not m: raise SystemExit("NG: OPENROUTER_API_KEY 未設定")
    return m.group(1).strip()

# ---- 工程1: 薄記事取得 ----
def pick(qid=None, auto=False):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    if qid:
        row = con.execute("SELECT * FROM festivals WHERE qid=?", (qid,)).fetchone()
    else:
        row = con.execute(
            "SELECT * FROM festivals WHERE status='drafted' "
            "AND LENGTH(COALESCE(manual_content_ja,''))<2400 "
            "ORDER BY COALESCE(priority_score,0) DESC LIMIT 1").fetchone()
    con.close()
    if not row: raise SystemExit("NG: 対象記事なし")
    return dict(row)

# ---- 工程2: 検索接地下書き ----
RULES_TMPL = """あなたは日本の祭り・年中行事の多言語データベース「Nipponexus」の記事執筆者です。
以下の品質基準を厳守し、Web検索で一次情報を確認しながら書いてください。学習知識で補完してはいけません。

【対象】{pref}の「{label}」

【必須構造・6セクション(markdown ## 見出し必須)】
## 概要 (2段落以上)
## 歴史・由来 (4段落以上)
## 見どころ (太字**小見出し**を6個以上・各小見出しは最低3文=事実1文+背景/理由1文+意味/情景1文)
## 開催情報・アクセス (6項目以上)
## 周辺情報 (3段落以上)
## 関連情報 (6項目以上)

【文章の質】各段落3文以上。各事実を3段展開(事実→背景/理由→意味/情景)。抽象語の水増し禁止。固有事実(年号・地名・人名・数値)で肉付け。

【ハルシネーション厳禁(最重要)】Webで確認できない事実は書かない。起源等が不確かなら「言い伝えによれば」「一説では」等の留保を付ける。創作で字数を埋めない。裏取り不能な電話番号・不確かな数値は書かない。中止・休止のあった祭りは開催情報に「最新の開催日程・実施可否は公式サイトで確認」と明記。終了した祭りは過去形で歴史的事実として記述。

【出力形式】まず日本語本文(2,400字以上・目安3,500〜4,500字。事実が濃い題材でも冗長な一般論や美辞麗句で水増しせず、固有事実の3段展開で厚みを出す)、次に区切り線 ===EN=== 、続けて英語本文(日本語の2倍以上かつ2,400字以上)。英語本文に半角ダブルクォートを使わない。前置き・後書き・メタ発言は書かず本文のみ出力。"""

def _post(prompt, key):
    body = {"model": MODEL,
            "plugins": [{"id": "web", "max_results": 6}],
            "max_tokens": 16000,
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "HTTP-Referer": "https://nipponexus.com", "X-Title": "Nipponexus"},
        method="POST")
    with urllib.request.urlopen(req, timeout=420) as r:
        return json.loads(r.read())

def call(prompt, key, use_brave=False):
    """content Noneガード付き。最大3回試行。本文が取れなければ例外で安全停止。"""
    last=None
    for i in range(3):
        data=_post(prompt, key)
        msg=data.get("choices",[{}])[0].get("message",{})
        content=msg.get("content")
        fr=data.get("choices",[{}])[0].get("finish_reason")
        if content and content.strip():
            return data
        # 本文が空: finish_reason=length等の可能性。ログ出して再試行
        print(f"  [警告] 試行{i+1}: content空(finish_reason={fr})・再試行")
        last=data
        time.sleep(3)
    raise SystemExit(f"NG: 3回試行しても本文が空。finish_reason={last.get('choices',[{}])[0].get('finish_reason') if last else '?'} "
                     f"(reasoningで打ち切り/長文切れの可能性・max_tokens増やすか題材変更)")

# ---- 工程3: 検算 ----
# ---- 段階②形式検出器(2026-07-16・過去5本で回帰テスト済 H1=8/8 日英年号=4/4) ----
def detect_h1(text):
    """先頭の非空行が # で始まる(H1混入)なら True。既存記事は ## 概要 始まり。"""
    for line in text.splitlines():
        if line.strip()=='': continue
        return bool(re.match(r'^#\s+', line))
    return False

def detect_ja_en_year_mismatch(ja, en):
    """JAに在りENに無い4桁西暦(only_ja)が1件以上ならTrue(=日英不整合)。
       方向をJA基準に限定しEN側の片方向補足年号による誤検出を排除。戻り: (bool, only_ja集合)"""
    if not en: return False, set()
    pat = r'(?<!\d)(1[5-9]\d{2}|20\d{2})(?!\d)'
    only_ja = set(re.findall(pat, ja)) - set(re.findall(pat, en))
    return (len(only_ja)>0, only_ja)

def detect_en_heading_level(en):
    """EN見出しレベルずれ検出(True=ずれあり)。責務分離: H1混入はdetect_h1に委ね
       ここでは判定回避。ずれ条件=先頭非空行が## Overviewでない、または本文中に### あり。
       既存記事はEN先頭## Overview・全セクション##で統一(26本目でタイトルH2+H3ずれを検出)。"""
    if detect_h1(en): return False
    lines = en.strip().splitlines()
    first = next((l for l in lines if l.strip()), "")
    head_ng = first.strip() != "## Overview"
    has_h3 = any(l.strip().startswith("### ") for l in lines)
    return head_ng or has_h3

def detect_meta_preamble(text, expected):
    """先頭見出しチェック(True=メタ前置き等の混入あり)。先頭の非空行がexpected見出し
       (JA='## 概要'/EN='## Overview')でなければTrue。detect_h1(H1混入)とは責務分離し
       前置き文・---水平線・その他の混入を捕捉(31本目でメタ前置き文混入を検出)。"""
    lines = text.strip().splitlines()
    first = next((l for l in lines if l.strip()), "")
    return first.strip() != expected

def clen(t): return len(re.sub(r'\s','',t))
def headings(t): return len(re.findall(r'^##\s', t, re.M))
def bolds(t): return len(re.findall(r'\*\*[^*]+\*\*', t))

def verify(ja, en):
    r = {"ja_len": clen(ja), "en_len": clen(en), "h": headings(ja), "b": bolds(ja)}
    std = (r["ja_len"]>=2400 and r["en_len"]>=max(2400, r["ja_len"]*2))
    exc = (r["en_len"]>=8000 and r["ja_len"]>=4800 and r["en_len"]>=r["ja_len"]*1.7)
    r["mode"] = "標準" if std else ("例外" if exc else "NG")
    r["ok"] = ((std or exc) and r["h"]>=6 and r["b"]>=6)
    return r

# ---- 分割(===EN===欠落時フォールバック・2026-07-19追加/35・37本目でセパレータ欠落2回) ----
def _normalize_h1(block):
    """先頭が単一#のH1見出しを##へ格上げ(既存##小見出しは不変)。全見出しH1化事故の是正。"""
    out=[]
    for l in block.splitlines():
        out.append('## '+l[2:] if re.match(r'^# (?!#)', l) else l)
    return '\n'.join(out).strip()

def split_ja_en(content):
    """(ja, en, fallback) を返す。===EN===があれば通常2分割(正規化なし=既存挙動維持)。
       無ければ # Overview / ## Overview 行でフォールバック分割しH1→H2正規化。
       境界が無ければ en='' で返し検算NGで安全停止。"""
    if "===EN===" in content:
        ja, en = (content.split("===EN===",1)+[""])[:2]
        return ja.strip(), en.strip(), False
    # フォールバック: EN先頭見出し(# Overview or ## Overview)を探す
    lines = content.splitlines()
    sep = next((i for i,l in enumerate(lines)
                if l.strip() in ("# Overview","## Overview")), None)
    if sep is None:
        return content.strip(), "", False
    ja = _normalize_h1("\n".join(lines[:sep]))
    en = _normalize_h1("\n".join(lines[sep:]))
    return ja, en, True

# ---- 工程4: 照合レポート(要照合箇所=実務系を重点抽出) ----
def review(qid, label, ja, en, cites, vr, usage):
    years=[]
    for mm in re.finditer(r'(?:明暦|文化|文政|明治|大正|昭和|平成|令和|西暦)?\s*\d{3,4}\s*年', ja):
        s=max(0,mm.start()-25); years.append(ja[s:mm.end()+15].replace("\n"," "))
    tels = re.findall(r'0\d{1,4}[-\uff0d]\d{1,4}[-\uff0d]\d{3,4}', ja)
    access = [m.group(0).strip()[:90] for m in
              re.finditer(r'[^\n\u3002]*(?:駅|バス停|徒歩|IC|インター|料金|\d+\u5186)[^\n\u3002]*', ja)]
    L=[]
    L.append(f"# 照合レポート {qid} {label}\n")
    L.append(f"検算: ja{vr['ja_len']} en{vr['en_len']} 見出し{vr['h']} 太字{vr['b']} => {'OK' if vr['ok'] else 'NG'}")
    h1 = detect_h1(ja); h1e = detect_h1(en)
    mm, only_ja = detect_ja_en_year_mismatch(ja, en)
    enlv = detect_en_heading_level(en)
    metaja = detect_meta_preamble(ja, "## 概要"); metaen = detect_meta_preamble(en, "## Overview")
    L.append(f"形式チェック: H1混入(JA)={'NG除去要' if h1 else 'OK'} H1混入(EN)={'NG除去要' if h1e else 'OK'} "
             f"日英年号整合={'NG['+','.join(sorted(only_ja))+']がENに欠落' if mm else 'OK'} "
             f"EN見出しレベル={'NG(タイトルH2/H3ずれ→##統一要)' if enlv else 'OK'} "
             f"先頭見出し(JA)={'NG(## 概要前に混入→除去要)' if metaja else 'OK'} "
             f"先頭見出し(EN)={'NG(## Overview前に混入→除去要)' if metaen else 'OK'}")
    L.append("  ※start_monthは投入ブロックで必須セット(本スクリプト対象外)")
    L.append(f"コスト: ${usage.get('cost')}  tokens {usage.get('total_tokens')}\n")
    L.append("## 出典 url_citation (実在確認対象)")
    L += [f"- {u}" for u in cites] or ["- (0件=Braveフォールバック検討)"]
    L.append("\n## 要照合: 年号 (出典に実在するか現物確認)")
    L += [f"- {y}" for y in years]
    L.append("\n## 要照合: 電話番号 (裏取り不能なら削除)")
    L += [f"- {t}" for t in tels] or ["- なし"]
    L.append("\n## 要照合: アクセス実務系 (最寄り/料金/開催日程=重点)")
    L += [f"- {a}" for a in access]
    return "\n".join(L)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qid"); ap.add_argument("--auto", action="store_true")
    a = ap.parse_args()
    if not (a.qid or a.auto): raise SystemExit("--qid か --auto を指定")
    OUT.mkdir(parents=True, exist_ok=True)
    key = get_key()
    row = pick(a.qid, a.auto)
    qid, label, pref = row["qid"], row.get("label_ja") or "", row.get("prefecture") or ""
    print(f"対象: {qid} {label} ({pref}) 既存ja={len(row.get('manual_content_ja') or '')}字")
    prompt = RULES_TMPL.format(pref=pref, label=label)
    print("生成中...")
    t0=time.time(); data=call(prompt, key); el=time.time()-t0
    msg=data["choices"][0]["message"]; content=msg.get("content","")
    content=content or ""
    ja,en,fb=split_ja_en(content)
    if fb: print("  [警告] ===EN===欠落→Overview見出しでフォールバック分割+H1正規化を適用")
    cites=[x.get("url_citation",{}).get("url") for x in (msg.get("annotations") or [])
           if x.get("type")=="url_citation"]
    (OUT/f"{qid}_deepseek_full.md").write_text(content)
    vr=verify(ja,en); usage=data.get("usage",{})
    rep=review(qid,label,ja,en,cites,vr,usage)
    (OUT/f"{qid}_review.md").write_text(rep)
    print(f"完了 {el:.0f}秒 cost=${usage.get('cost')}")
    print(f"検算 ja{vr['ja_len']} en{vr['en_len']} 見出し{vr['h']} 太字{vr['b']} => {'OK' if vr['ok'] else 'NG'}")
    print(f"出力: llm_sim/{qid}_deepseek_full.md / {qid}_review.md")
    print("\n>>> 次: review.md を人/Claudeが照合 -> OKなら既存投入ブロックへ手動接続(本番投入は不可逆・別途確認)")

if __name__=="__main__":
    main()
