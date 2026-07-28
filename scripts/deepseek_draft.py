#!/usr/bin/env python3
"""Nipponexus 薄記事底上げ自動下書き (DeepSeek V4 Flash + OpenRouter webプラグイン)
工程1 DB薄記事取得 -> 工程2 検索接地下書き -> 工程3 検算 -> 工程4 照合レポート出力(ここで停止)
工程5(本番投入)は既存の投入ブロックへ手動接続。本スクリプトは本番非反映(llm_sim出力のみ)。
使い方:
  python3 scripts/deepseek_draft.py --auto        # 最優先の薄記事1件
  python3 scripts/deepseek_draft.py --qid Q123456 # qid指定
"""
import sys, os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import os, re, json, time, sqlite3, argparse, pathlib, urllib.request, urllib.error, socket, http.client
try:
    from term_check import detect_en_term_mismatch
except Exception:
    detect_en_term_mismatch = None


DB   = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")
ENV  = os.path.expanduser("~/.openclaw/.env")
OUT  = pathlib.Path(os.path.expanduser("~/nexus_data/llm_sim"))
MODEL = "deepseek/deepseek-v4-flash"
MODEL_PRO = "deepseek/deepseek-v4-pro"

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

【将来陳腐化の回避(必須)】記事は長期間掲載されるため、その年限りで古くなる情報を本文に書かない。具体的には(1)特定年の開催日程(「2026年2月6日〜11日」等)や回数(「第67回」等)、(2)その年のテーマキャラクター名・コラボ企業名・出演者やアーティスト名・楽曲名、(3)単年限りの特別企画は書かない。開催時期は「例年2月上旬」「例年○月○旬の△曜」等の相対表現にし、「最新の日程・実施可否は公式サイトで確認」と注記する。ただし毎年同じ固定日(例:5月15日)や、過去の歴史的事実(創始年・文化財指定年・記録樹立年等)は正確な年で書いてよい(これらは相対化しない)。
・その年限定の企画名/出演者/タレント名/スポーツ大会連動事業/コラボ名は書かない(例: 『アジア大会フレンドシップ事業』『○○トークショー』)。恒常的な行事のみ記述する。単年の協賛企業も同様。

【出力形式】まず日本語本文(2,400字以上・目安3,500〜4,500字。事実が濃い題材でも冗長な一般論や美辞麗句で水増しせず、固有事実の3段展開で厚みを出す)、次に区切り線 ===EN=== 、続けて英語本文(日本語の2倍以上かつ2,400字以上)。英語本文に半角ダブルクォートを使わない。日本の祭事固有の行事名を英訳する際は意味を取り違えないこと(特に打毬=mounted ball game/polo系 と 流鏑馬=horseback archery、神楽/田楽/田植神事、神幸祭 と 還幸祭 など混同しやすい語)。原語の意味を確認してから訳す。前置き・後書き・メタ発言は書かず本文のみ出力。"""

def _post(prompt, key, model=None, search_prompts=None, max_tokens=16000):
    body = {"model": model or MODEL,
            "plugins": [{"id": "web", "max_results": 6,
                         "search_prompts": search_prompts or [],
                         "exclude_domains": ["nipponexus.com"]}],
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "HTTP-Referer": "https://nipponexus.com", "X-Title": "Nipponexus"},
        method="POST")
    with urllib.request.urlopen(req, timeout=420) as r:
        return json.loads(r.read())

def call(prompt, key, use_brave=False, model=None, search_prompts=None, max_tokens=16000):
    """content Noneガード付き。最大3回試行。本文が取れなければ例外で安全停止。"""
    last=None
    _NETERR=(urllib.error.URLError, http.client.IncompleteRead, http.client.HTTPException,
             socket.timeout, ConnectionError, TimeoutError, OSError)
    for i in range(3):
        try:
            data=_post(prompt, key, model=model, search_prompts=search_prompts, max_tokens=max_tokens)
        except _NETERR as e:
            # 通信例外(IncompleteRead/接続断/タイムアウト等)も再試行対象(2026-07-25・八戸で判明)
            print(f"  [警告] 試行{i+1}: 通信例外({type(e).__name__}: {e})・再試行")
            last=None; time.sleep(5); continue
        msg=data.get("choices",[{}])[0].get("message",{})
        content=msg.get("content")
        fr=data.get("choices",[{}])[0].get("finish_reason")
        print(f"  [生成] 試行{i+1}: finish_reason={fr} content_len={len(content or '')}")
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
    """EN見出しレベルずれ検出(True=ずれあり)。責務分離: H1混入はdetect_h1に委ね判定回避。
       正しい構造=先頭## Overview + 6大セクションが##(Overview/History/Highlights/Event/
       Surrounding/Related)。見どころ内の###小見出しは正常(103博多松囃子の誤検知修正)。
       真のNG=先頭が## Overviewでない(タイトル混入/1段下げ)、または##大セクションが6未満
       (セクションがH3に落ちている=26本目型の1段下げ)。###の有無単独ではNGにしない。"""
    if detect_h1(en): return False
    lines = en.strip().splitlines()
    first = next((l for l in lines if l.strip()), "")
    head_ng = first.strip() != "## Overview"
    big_sections = sum(1 for l in lines if l.strip().startswith("## "))
    return head_ng or big_sections < 6

def detect_meta_preamble(text, expected):
    """先頭見出しチェック(True=メタ前置き等の混入あり)。先頭の非空行がexpected見出し
       (JA='## 概要'/EN='## Overview')でなければTrue。detect_h1(H1混入)とは責務分離し
       前置き文・---水平線・その他の混入を捕捉(31本目でメタ前置き文混入を検出)。"""
    lines = text.strip().splitlines()
    first = next((l for l in lines if l.strip()), "")
    return first.strip() != expected

def detect_future_ephemeral(ja, en, now_year=None):
    """将来陳腐化する単年情報の混入検出(True=候補あり)。戻り:(bool, 候補リスト)。
       過去(生成時点以前)の西暦・日付・回数は史実/既往事実として警告から除外し、
       将来・現在寄りの単年情報(未来日程/未来の回/相対語/単年コラボ)のみ警告する。
       最終判断は人/Claudeが行う警告用だが、過去日付の自動除外で人的仕分けを削減。"""
    import datetime
    if now_year is None: now_year = datetime.date.today().year
    text = (ja or "") + "\n" + (en or "")
    hits = []
    def near_year(pos, span=30):
        # 近傍テキストから4桁西暦を拾い、最大値を文脈年とみなす(なければNone)
        seg = text[max(0,pos-span):pos+span]
        ys = [int(y) for y in re.findall(r'(?:19|20)\d{2}', seg)]
        return max(ys) if ys else None
    # (1) 特定年の具体日程: その西暦が未来/当年なら警告(過去は史実として除外)
    for m in re.finditer(r'((?:19|20)\d{2})\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日', text):
        if int(m.group(1)) >= now_year:
            s=max(0,m.start()-15); hits.append(f"[特定年の具体日程] ...{text[s:m.end()+15]}...".replace(chr(10)," "))
    # (2) 「○年は」単年言及: 未来/当年のみ
    for m in re.finditer(r'((?:19|20)\d{2})\s*年は', text):
        if int(m.group(1)) >= now_year:
            s=max(0,m.start()-15); hits.append(f"[「○年は」単年言及] ...{text[s:m.end()+15]}...".replace(chr(10)," "))
    # (3) 回数(第N回): 近傍西暦が未来/当年、または近傍に西暦が無く「予定」等を伴う場合のみ警告
    for m in re.finditer(r'第\s*\d+\s*回', text):
        ny = near_year(m.start())
        seg = text[max(0,m.start()-20):m.end()+20]
        future_ctx = bool(re.search(r'予定|開催され(る|ます)|今年|来年', seg))
        if (ny is not None and ny >= now_year) or (ny is None and future_ctx):
            s=max(0,m.start()-15); hits.append(f"[回数(第N回・将来/予定)] ...{text[s:m.end()+15]}...".replace(chr(10)," "))
    # (4) 相対的単年語: 常に警告(絶対年に依存せず陳腐化する)
    for m in re.finditer(r'今年|来年|本年度', text):
        s=max(0,m.start()-15); hits.append(f"[相対的単年語] ...{text[s:m.end()+15]}...".replace(chr(10)," "))
    # (5) 単年コラボ表現: 常に警告
    for m in re.finditer(r'テーマキャラクター|コラボレーション企画として登場', text):
        s=max(0,m.start()-15); hits.append(f"[単年コラボ表現] ...{text[s:m.end()+15]}...".replace(chr(10)," "))
    return (len(hits)>0, hits[:12])

def detect_en_cjk(en):
    """還元(2026-07-24・86灘): EN本文へのCJK漢字混入を機械検出(DeepSeekが相关人员/临时等の
       中国語簡体字をEN側に紛れ込ませる新種形式エラー)。CJK統合漢字(\u4e00-\u9fff)+拡張A
       (\u3400-\u4dbf)を全数検出。ひらがな/カタカナは対象外(別問題)。戻り:(bool, 該当行リスト)。
       原理的に見逃し0・無料・確実。Proの再現率に依存させず機械で弾く。"""
    hits=[]
    pat=re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')
    # 還元I(2026-07-26・104カセ鳥): ローマ字表記の直後の括弧内原語併記は英語記事として
    # 正当な用法(例 "Kasedori" (加勢鳥) / Kendai (蓑))。これを除いた残余のみをNGとする。
    paren = re.compile(r'[\(（]\s*[\u3000-\u9fff\u3400-\u4dbf]{1,12}\s*[\)）]')
    for i, ln in enumerate(en.splitlines()):
        residual = paren.sub('', ln)
        ms=pat.findall(residual)
        if ms:
            chars="".join(sorted(set(ms)))
            hits.append(f"L{i}[{chars}] ...{ln.strip()[:70]}...")
    return (len(hits)>0, hits[:20])

# ---- インライン出典装飾除去(2026-07-22追加/DeepSeekが地の文に[ラベル](URL)を乱発する問題) ----
_CITE = re.compile(r'\[[^\]]*\]\(https?://[^\)]*\)')
_BARE_CITE = re.compile(r'\s*\[[\w.\-]+\.(?:com|jp|org|net|info|co|go|lg|or|ne|ac)(?:\.[a-z]{2,3})?\]')

def strip_bare_citations(s):
    """還元(2026-07-28・113相模川): DeepSeekは回によって出典を[ラベル](URL)でなく
       [incloop.com]のような裸ブラケットで書く。_CITEはリンク形式のみ対象のため
       この形式が素通りし本番本文にドメイン名が露出した(66箇所)。装飾形式差に非依存化。"""
    return re.sub(r'[ \t]{2,}', ' ', _BARE_CITE.sub('', s or ''))


def _strip_citations_base(s):
    """地の文の[ラベル](URL)装飾を除去。ただし'公式情報'/'Official Information'行の
       公式サイトリンク1個は有用要素として保持する(手作りモデル記事の標準構成に準拠)。"""
    out=[]
    for ln in (s or '').split('\n'):
        if ('公式情報' in ln) or ('Official Information' in ln):
            out.append(ln); continue      # 公式リンク行はそのまま保持
        out.append(_CITE.sub('', ln))
    r='\n'.join(out)
    r=re.sub(r'[ \t]+\n','\n',r)
    r=re.sub(r'[ \t]{2,}',' ',r)
    r=re.sub(r'\n{3,}','\n\n',r)
    return r.strip()

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

def strip_meta_preamble(block, expected):
    """還元(2026-07-25・93本目角館): 先頭のメタ前置き文(『以下は/以下の記事は…』等)と
       それに続く水平線(---)を、最初の期待見出し(expected='## 概要'/'## Overview')まで
       削除する。detect_meta_preamble(検出専用)に対する自動修正版。H1除去(strip_leading_h1)と
       同じく無損失で安全なため自動修正へ格上げ。期待見出しが無ければ無変更で返す(安全側)。"""
    lines=block.splitlines()
    idx=next((i for i,l in enumerate(lines) if l.strip()==expected), None)
    if idx is None:
        return block.strip()
    # 期待見出しより前の行はメタ前置き/区切り線とみなし全削除
    if idx==0:
        return block.strip()
    return "\n".join(lines[idx:]).strip()

def strip_leading_h1(block):
    """還元B(2026-07-23・82本目まで毎回手書き除去していたH1混入を自動化):
       先頭付近の H1タイトル行(# xxx / ## Xxx でない単一# 見出し)を削除し
       ## 概要 / ## Overview から始まるよう整える。本文中の ## 小見出しは不変。
       H1除去は無損失で安全なため『警告のみ』から『自動修正』へ格上げ。"""
    lines=block.splitlines()
    out=[]
    for l in lines:
        if re.match(r'^# (?!#)', l):   # 単一# のH1行 = タイトル → 削除
            continue
        out.append(l)
    return '\n'.join(out).strip()

def split_ja_en(content):
    """(ja, en, fallback) を返す。===EN===があれば通常2分割(正規化なし=既存挙動維持)。
       無ければ # Overview / ## Overview 行でフォールバック分割しH1→H2正規化。
       境界が無ければ en='' で返し検算NGで安全停止。"""
    if "===EN===" in content:
        ja, en = (content.split("===EN===",1)+[""])[:2]
        return strip_meta_preamble(strip_leading_h1(ja),"## 概要"), strip_meta_preamble(strip_leading_h1(en),"## Overview"), False
    # フォールバック: EN先頭見出し(# Overview or ## Overview)を探す
    lines = content.splitlines()
    sep = next((i for i,l in enumerate(lines)
                if l.strip() in ("# Overview","## Overview")), None)
    if sep is None:
        return content.strip(), "", False
    ja_lines = lines[:sep]
    # 還元F(2026-07-23・お旅まつり85本目): フォールバック時JA末尾の'==='区切り行
    # 以降(ENタイトル巻き込み)を切り落とす。35/37/41/85で手動クリーンしていた両端汚れを自動化。
    cut = next((i for i,l in enumerate(ja_lines) if l.strip()=="==="), len(ja_lines))
    ja_lines = ja_lines[:cut]
    ja = strip_meta_preamble(strip_leading_h1(_normalize_h1("\n".join(ja_lines))),"## 概要")
    en = strip_meta_preamble(strip_leading_h1(_normalize_h1("\n".join(lines[sep:]))),"## Overview")
    return ja, en, True

# ---- 段階③アシスト(2026-07-23・85本目お旅で頭脳がやった年号一次照合の機械化) ----
def _fetch_text(url, timeout=12):
    """citation本文を単発GETしプレーンテキスト化(タグ簡易除去)。失敗はNone(防波堤=生成本体に影響させない)。"""
    import urllib.request, re as _re
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 (NipponexusReview)"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw=r.read(600000).decode(r.headers.get_content_charset() or "utf-8","ignore")
    except Exception:
        return None
    raw=_re.sub(r"(?is)<(script|style).*?</\1>"," ",raw)
    raw=_re.sub(r"(?s)<[^>]+>"," ",raw)
    return _re.sub(r"\s+"," ",raw)

# 元号開始西暦(和暦照合用・江戸中期以降を網羅)
_GENGO={"令和":2019,"平成":1989,"昭和":1926,"大正":1912,"明治":1868,
        "慶応":1865,"元治":1864,"文久":1861,"万延":1860,"安政":1854,"嘉永":1848,
        "弘化":1844,"天保":1830,"文政":1818,"文化":1804,"享和":1801,"寛政":1789,
        "天明":1781,"安永":1772,"明和":1764,"宝暦":1751,"寛延":1748,"延享":1744,
        "寛保":1741,"元文":1736,"享保":1716}
_KANSU={1:"元",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十"}
def _wareki_variants(y):
    """西暦yを含みうる和暦表記の候補集合(元号N年/元号元年/漢数字)を返す。"""
    out=set()
    for g,s in _GENGO.items():
        n=y-s+1
        if 1<=n<64:
            out.add(f"{g}{n}年"); out.add(f"{g}{n}")
            if n==1: out.add(f"{g}元年"); out.add(f"{g}元")
            # 漢数字(1〜30程度を簡易対応)
            if n<=10: out.add(f"{g}{_KANSU[n]}年")
            elif n<20: out.add(f"{g}十{_KANSU.get(n-10,'')}年".replace('十元','十一'))
    return out

def audit_years_against_citations(ja, cites):
    """記事中の西暦4桁を抽出し、citation本文群に西暦または和暦(元号/元年/漢数字)で
       実在するか照合。返り値=[(西暦, 判定, 出典ドメイン列)]。
       ★判定の定義(2026-07-24・条件B再設計): 
         実在=西暦or和暦がcitation本文にある。
         ×人的確認=どの表記でもcitationに無い。★これは『削除指示』ではない=
           幻覚の可能性と『出典に明示ないが正しい背景/派生年号』(例:起源の前年凶作・
           電線敷設時期)の両方を含むため、頭脳が幻覚か正当補足かを最終判断する対象。
         取得不可=全citation取得失敗。
       真偽の材料提示のみ・修正LLMへ×人的確認をそのまま削除指示として渡さない。"""
    import re as _re
    from urllib.parse import urlparse
    yrs=sorted(set(_re.findall(r'(?<!\d)(1[5-9]\d{2}|20[0-4]\d)(?!\d)', ja)))
    if not yrs or not cites: return []
    texts={}
    for u in cites:
        if not u: continue
        t=_fetch_text(u)
        if t: texts[u]=t
    out=[]
    for y in yrs:
        yi=int(y); variants={y}|_wareki_variants(yi)
        hits=[urlparse(u).netloc for u,t in texts.items()
              if any(v in t for v in variants)]
        if hits: out.append((y,"実在",sorted(set(hits))))
        elif texts: out.append((y,"×人的確認(幻覚 or 出典外の正当補足)",[]))
        else: out.append((y,"取得不可(全citation取得失敗)",[]))
    return out

def audit_dates_against_citations(ja, cites):
    """還元(2026-07-25・93本目角館・指定日の月誤り3月→2月が年単体照合をすり抜けた):
       本文の『YYYY年…M月D日』(元号併記可)を抽出し、月日までcitation本文に在るか照合。
       年は実在でも月日がcitation不在なら×人的確認(月日の誤り疑い)を出す。削除指示でなく材料提示。"""
    import re as _re
    from urllib.parse import urlparse
    # 例: 1991年（平成3年）2月21日 / 1991年2月21日 / 2016年12月1日
    dates=_re.findall(r'(1[5-9]\d{2}|20[0-4]\d)年[^。\n]{0,12}?(\d{1,2})月(\d{1,2})日', ja)
    dates=sorted(set(dates))
    if not dates or not cites: return []
    texts={}
    for u in cites:
        if not u: continue
        t=_fetch_text(u)
        if t: texts[u]=t
    out=[]
    for (y,m,d) in dates:
        mi,di=int(m),int(d)
        # 月日の表記ゆれ(M月D日 / M/D / M-D / ゼロ埋め)
        pats={f"{mi}月{di}日", f"{mi}/{di}", f"{mi}-{di}", f"{int(m):02d}.{int(d):02d}", f"{mi}.{di}"}
        hits=[urlparse(u).netloc for u,t in texts.items() if any(pp in t for pp in pats)]
        tag="実在" if hits else ("×人的確認(月日がcitation不在=月日誤りの疑い)" if texts else "取得不可")
        out.append((f"{y}年{mi}月{di}日", tag, sorted(set(hits))))
    return out

# ---- 工程4: 照合レポート(要照合箇所=実務系を重点抽出) ----
import datetime as _dt

_STATUS_RX = re.compile(r"再開|中止|休止|見送ら|現在も|年現在|継続して開催")
_HOST_NG = ("staging", "proxy", "mirror", "translate.", "webcache", "todaiinews")
_DENIAL_RX = re.compile(r"確認(?:でき|が取れ)ない|確認不可|裏付け(?:が)?(?:取れ|得られ)ない|"
                        r"情報源(?:なし|が見当たら)|検索結果に(?:一切)?含まれ|該当する情報源なし")

def build_dynamic_queries(label, ja):
    """記事本文から検証すべき論点を決定論的に抽出しクエリ化。
       固定4本(日本語の由緒/文化財)に時間軸・主催の軸が無いのが過剰否定の構造的原因
       (2026-07-28・112夜梅祭でPro過剰否定8例目/111深大寺の現況誤りと同根)。"""
    qs, now = [], _dt.date.today().year
    if _STATUS_RX.search(ja):
        qs.append(f"{label} 中止 休止 {now}")
    yrs = [int(y) for y in re.findall(r"(20[0-4]\d)年", ja)]
    if yrs and max(yrs) >= now:
        qs.append(f"{label} {max(yrs)} 開催")
    if re.search(r"主催|主管|実行委員会", ja):
        qs.append(f"{label} 主催 実行委員会")
    return qs

def classify_pro_findings(txt):
    """Pro出力を(具体的な誤り指摘/確認不可)に分類。確認不可は是正候補に混ぜない。
       Proの否定は『Proの検索に一次公式が入らなかった』だけのことが多い(過剰否定8例)。"""
    blocks, cur = [], []
    for line in (txt or "").split("\n"):
        if line.startswith("- **") and cur:
            blocks.append("\n".join(cur)); cur = [line]
        else:
            cur.append(line)
    if cur: blocks.append("\n".join(cur))
    concrete, denial = [], []
    for b in blocks:
        if not b.strip(): continue
        (denial if _DENIAL_RX.search(b) else concrete).append(b.strip())
    return concrete, denial

def audit_pro_sources(urls):
    """Pro参照URLの一次ソース判定(ステージング/プロキシ/転載を警告)。"""
    bad = []
    for u in urls or []:
        host = re.sub(r"^https?://", "", u).split("/")[0].lower()
        if any(k in host for k in _HOST_NG):
            bad.append((host, u))
    return bad

_SEC_JA = ["## 概要", "## 歴史", "## 見どころ", "## 開催情報", "## 周辺情報", "## 関連情報"]

def split_sections(ja):
    """C-1の必須6セクションで本文を分割(見出しが欠ける場合も落とさない)"""
    pos = []
    for h in _SEC_JA:
        i = ja.find(h)
        if i >= 0:
            pos.append((i, h))
    pos.sort()
    out = {}
    for k, (i, h) in enumerate(pos):
        j = pos[k+1][0] if k+1 < len(pos) else len(ja)
        out[h] = ja[i:j].strip()
    return out

def build_pro_blocks(ja, en):
    """還元(2026-07-28・113相模川): 抜粋900字=本文の21.9%しかProに渡らず
       周辺情報(3208字目)が構造的死角だった。1回を長くするとExa暴走(88今宮)するため
       『長さ』でなく『回数』で解決する=同じ長さを複数回に分割送付。"""
    s = split_sections(ja)
    g = lambda *hs: "\n\n".join(s.get(h, "") for h in hs if s.get(h)).strip()
    blocks = [
        ("概要・歴史", g("## 概要", "## 歴史")[:1100]),
        ("見どころ",   g("## 見どころ")[:1100]),
        ("開催情報",   g("## 開催情報")[:1100]),
        ("周辺・関連", g("## 周辺情報", "## 関連情報")[:1100]),
    ]
    return [(n, t) for n, t in blocks if len(t) >= 80]

_ORG = re.compile(r'[一-龥ァ-ヶA-Za-z][一-龥ァ-ヶA-Za-zー・]{1,11}(?:市|町|村|寺|神社|大社|宮|城|大学|協会|クラブ|会館|博物館|科学館|公園|駅)(?![一-龥])')

def build_block_queries(label, pref, name, text):
    """ブロック内の固有名詞から検証クエリを作る。周辺情報の回では
       施設名・自治体名そのものを投げる(113の『相模原市 姉妹都市』型を捕捉)。"""
    if name == "概要・歴史":
        return [f"{label} {pref} 公式", f"{label} 由来 起源", f"{label} 主催"]
    if name == "見どころ":
        return [f"{label} 見どころ 内容", f"{label} {pref}"]
    if name == "開催情報":
        return [f"{label} 開催 日程 会場", f"{label} アクセス 最寄り"]
    names = []
    for m in _ORG.findall(text):
        if m not in names and m not in label:
            names.append(m)
    qs = [f"{n} {pref}" for n in names[:2]]
    if "姉妹都市" in text or "友好都市" in text:
        qs.append(f"{pref} 姉妹都市 友好都市")
    return qs or [f"{label} {pref} 周辺"]


_EPHEMERAL_PAT = re.compile(
    r'第\d+回|20[2-9]\d年|フレンドシップ|コラボ|トークショー|ゲスト|出演|タレント|'
    r'アーティスト|ライブ|コンテスト20|今年の|本年度の|competition|guest|talk show')

def classify_ephemeral(txt):
    """還元(2026-07-28・114一宮): Proは『公式発表との差分』で欠落を判定するため、
       公式発表=その年の情報である以上、指摘は構造的に単年ネタへ偏る。
       分割送付でカバレッジが上がるほどこの要求は増える→機械で不採用へ仕分ける。"""
    keep, drop = [], []
    for ln in (txt or "").split("\n"):
        (drop if (ln.strip().startswith("-") and _EPHEMERAL_PAT.search(ln)) else keep).append(ln)
    return "\n".join(keep), drop


def pro_proofread(qid, label, pref, ja, en, key):
    """Pro校正(2026-07-28改修: セクション分割送付)。
       ★1回あたりの長さは従来どおり短く保ちExa暴走(88今宮)を回避しつつ、
         回数を分けて本文全体をカバーする(113で周辺情報が死角=捏造を見逃した還元)。
       ★C-3b堅持: Proの回答は正解データとして採用せず人が一次照合する前提。"""
    blocks = build_pro_blocks(ja, en)
    if not blocks:
        blocks = [("冒頭", ja[:1100])]
    _m = re.search(r'##[^\n]*(?:見どころ|Highlights|Attractions)', en)
    en_ex = (en[_m.start():_m.start()+600] if _m else en[:600])

    facts, texts, allc, tot = [], [], [], {}
    for idx, (name, body) in enumerate(blocks, 1):
        pre = ("\n【前ブロックまでの確定事項(整合を確認)】\n" + "\n".join(facts[-4:])) if facts else ""
        extra = f"\n\n【英語(見どころ抜粋・訳語照合用)】\n{en_ex}" if name == "見どころ" else ""
        prompt = (
            "日本の祭り記事のファクトチェッカーです。以下は記事の一部です。"
            "Web検索で公式情報を確認し、(a)事実と食い違う箇所 (b)裏取りできない箇所 (c)欠落した核心情報 を箇条書きで指摘してください。"
            "特に、記事内の固有名詞(自治体名/施設名/団体名)と、その主体に関する断定(提携/指定/主催など)が実在するかを確認してください。"
            "★回答は自動採用されず人が一次照合します。断定せず根拠URL(公式優先)を添え、確認できない項目は「確認不可」と明記。"
            "★【重要】その年限定の情報(単年の企画名/出演者/タレント名/コラボ/大会連動事業/特定年の日程)は""記事の陳腐化を招くため意図的に除外している。これらを『欠落』として指摘しないこと。""毎年恒常的に成立する事実(正式名称/由緒/神格/中核行事/会場/主催)のみを対象とせよ。\n""★長い思考は不要。箇条書きを直ちに出力(前置き禁止)。\n\n"
            f"【対象】{pref}の「{label}」 / 検査対象セクション: {name}{pre}\n\n【本文】\n{body}{extra}"
        )
        sp = build_block_queries(label, pref, name, body)
        if name == "概要・歴史":
            sp += build_dynamic_queries(label, ja)
        sp = sp[:5]
        print(f"  Pro[{idx}/{len(blocks)}] {name} ({len(body)}字) queries={sp}")
        try:
            data = call(prompt, key, model=MODEL_PRO, search_prompts=sp, max_tokens=8000)
        except (SystemExit, Exception) as e:
            texts.append(f"### {name}\n(校正失敗: {type(e).__name__}: {e})")
            continue
        msg = data["choices"][0]["message"]
        t = (msg.get("content") or "").strip()
        texts.append(f"### {name}\n{t}")
        for x in (msg.get("annotations") or []):
            u = x.get("url_citation", {}).get("url")
            if u and u not in allc:
                allc.append(u)
        u_ = data.get("usage", {}) or {}
        for k_ in ("prompt_tokens", "completion_tokens", "total_tokens", "cost"):
            if k_ in u_:
                tot[k_] = tot.get(k_, 0) + u_[k_]
        if name == "概要・歴史" and t:
            facts.append(t[:300])
    return ("\n\n".join(texts), allc, tot)

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
    L.append(f"形式チェック: H1自動除去済(JA)={'NG除去要' if h1 else 'OK'} H1自動除去済(EN)={'NG除去要' if h1e else 'OK'} "
             f"日英年号整合={'NG['+','.join(sorted(only_ja))+']がENに欠落' if mm else 'OK'} "
             f"EN見出しレベル={'NG(タイトルH2/H3ずれ→##統一要)' if enlv else 'OK'} "
             f"先頭見出し(JA)={'NG(## 概要前に混入→除去要)' if metaja else 'OK'} "
             f"先頭見出し(EN)={'NG(## Overview前に混入→除去要)' if metaen else 'OK'}")
    fe, fe_hits = detect_future_ephemeral(ja, en)
    L.append(f"将来陳腐化: {'NG候補あり→相対化要('+str(len(fe_hits))+'件)' if fe else 'OK'}")
    if fe:
        L += [f"  - {h}" for h in fe_hits]
    encjk, encjk_hits = detect_en_cjk(en)
    L.append(f"EN他言語混入(CJK漢字): {'NG('+str(len(encjk_hits))+'行に混入→英語是正要)' if encjk else 'OK'}")
    if encjk:
        L += [f"  - {h}" for h in encjk_hits]
    if detect_en_term_mismatch is not None:
        _thit, _titems = detect_en_term_mismatch(ja, en)
        L.append("固有名詞の訳語照合: " + ("NG(誤訳語がENに出現→是正要)" if _thit else "OK"))
        for _it in _titems:
            L.append("  - [%s] %s : %s / 期待=%s"
                     % (_it["level"], _it["term"],
                        _it["found"] or _it["reason"], _it["expected"]))
    L.append("  ※start_monthは投入ブロックで必須セット(本スクリプト対象外)")
    L.append(f"コスト: ${usage.get('cost')}  tokens {usage.get('total_tokens')}\n")
    L.append("## 出典 url_citation (実在確認対象)")
    L += [f"- {u}" for u in cites] or ["- (0件=Braveフォールバック検討)"]
    # 偽/自ドメイン警告(2026-07-22追加: 44/67/70の循環参照・wikid偽ドメイン再発対策)
    bad = []
    for u in cites:
        lu = (u or "").lower()
        if "nipponexus.com" in lu: bad.append(("自サイト循環参照", u))
        elif "wikid.org" in lu: bad.append(("偽ドメインwikid.org", u))
        elif "wikipedia" in lu and "wikipedia.org" not in lu: bad.append(("偽wikipedia類似", u))
    # 本文中の出典装飾はstrip済みだが素のURL文字列が残る可能性も走査
    for tag, pat in [("自サイト循環参照(本文)","nipponexus.com"), ("偽ドメインwikid(本文)","wikid.org")]:
        if pat in ja or pat in en: bad.append((tag, pat))
    if bad:
        L.append("\n## ★要是正: 偽/自ドメイン検出 (投入前に必ず除去・正規化)")
        L += [f"- [{t}] {u}" for t, u in bad]
    L.append("\n## 要照合: 年号 (出典に実在するか現物確認)")
    L += [f"- {y}" for y in years]
    # 段階③アシスト: citation本文と西暦の自動照合(真偽の材料提示・GOは頭脳)
    try:
        audit=audit_years_against_citations(ja, cites)
    except Exception as e:
        audit=[]; L.append(f"\n## 段階③citation年号照合: スキップ({e})")
    if audit:
        L.append("\n## 段階③citation年号照合 (自動・×不在は頭脳が最終確認)")
        for y,verdict,doms in audit:
            L.append(f"- {y}: {verdict}" + (f"  出典={','.join(sorted(set(doms))[:3])}" if doms else ""))
    # 段階③月日照合(2026-07-25・93本目角館: 指定日の月誤り3月→2月が年単体照合をすり抜けた)
    try:
        audit_d=audit_dates_against_citations(ja, cites)
    except Exception as e:
        audit_d=[]; L.append(f"\n## 段階③citation月日照合: スキップ({e})")
    if audit_d:
        L.append("\n## 段階③citation月日照合 (自動・×は月日誤りの疑い=頭脳が最終確認)")
        for d,verdict,doms in audit_d:
            L.append(f"- {d}: {verdict}" + (f"  出典={','.join(sorted(set(doms))[:3])}" if doms else ""))
    L.append("\n## 要照合: 電話番号 (裏取り不能なら削除)")
    L += [f"- {t}" for t in tels] or ["- なし"]
    L.append("\n## 要照合: アクセス実務系 (最寄り/料金/開催日程=重点)")
    L += [f"- {a}" for a in access]
    # 接ぎ木/現況/メタ矛盾の決定論検出(2026-07-27・111深大寺の実データで条件B成立)
    try:
        import graft_check as _gc
        inc, sm, _lb = _gc.load_meta(qid)
        L.append("\n## 機械検出(接ぎ木・現況・メタ) 4項目")
        hit, subj, ev = _gc.detect_origin_conflict(ja)
        L.append(f"- 起源主体の自己矛盾: {'NG' if hit else 'OK'} {subj}")
        for i, sj in (ev if hit else []):
            L.append(f"    - L{i} {sj}")
        hit, ng = _gc.detect_meta_year_conflict(ja, inc, sm)
        L.append(f"- DBメタ突合(開始年/周年/開催月): {'NG' if hit else 'OK'}"
                 + ("  [WARN] start_month=None (投入時に必須セット)" if not sm else ""))
        for i, k, v in ng:
            L.append(f"    - L{i} [{k}] {v}")
        hit, ng = _gc.detect_status_assertion(ja, en)
        L.append(f"- 現況断定ガード(公式確認注記の有無): {'NG' if hit else 'OK'}")
        for t, i, v in ng:
            L.append(f"    - {t} L{i} {v}")
        hit, ng, warn = _gc.detect_reading_mismatch(ja, en)
        L.append(f"- 訳語の読み照合: {'NG' if hit else 'OK'}")
        for a, b, c in ng:
            L.append(f"    - NG {a} {b}: {c}")
        for a, b, c in warn:
            L.append(f"    - WARN {a} {b}: {c}")
    except (AttributeError, TypeError, NameError, ImportError) as e:
        # 還元O(2026-07-28・114/115でgraft_checkが2本連続で空回りしていた事故):
        # 検出器の『呼び出し側の誤り』(関数名・引数・import)はWARNで素通りさせない。
        # try/exceptで続行してよいのは検出器が正常動作した上で結果を出せない場合のみ。
        raise AssertionError('[FATAL] 接ぎ木検出器の呼び出しに失敗(検査未実施のまま進行禁止): %r' % (e,))
    except Exception as e:
        L.append(f"\n## 機械検出(接ぎ木・現況・メタ): スキップ({e})")
    return "\n".join(L)

def _unescape_literal(s):
    """還元M(2026-07-28・115鉱山祭): DeepSeek出力にリテラルの \' \" が混入すると
       固定文字列も正規表現も当たらず置換が空振りし、本番に children\'s と露出する。
       是正適用の前段で必ず正規化する(『カウント0を不在と読まない』の構造対処)。"""
    if not s:
        return s
    return s.replace("\\'", "'").replace('\\"', '"')


def apply_fixes(text, pairs, strict=False):
    """還元D(2026-07-23・82八尾)+還元L(2026-07-28・116本町の八月踊り)。
       pairs=[(old,new,expect,label),...]
       ★expectは『人が数えた正解』ではなく『最低これだけは当たるはずの下限』。
       116で count_targets が every other year:2 と出力済みだったのに expect へ 1 と
       手書きして停止した=数え漏れではなく『実測値を使わず目視を優先した』事故。
       →実測ヒット数を出力し、当たった全件を置換し、残存0をassertする方式へ変更。
       人が書くのは下限だけなので、数え間違いが原理的に起きない。
       strict=Trueの時だけ従来の完全一致判定(件数を意図的に固定したい場合のみ)。"""
    BAD = ("...", "\u2026", "TODO", "(仮)", "（仮）", "xxx", "XXX")
    text = _unescape_literal(text)
    for old, new, expect, label in pairs:
        for b in BAD:
            if b in new:
                raise AssertionError(f"[{label}] new に未確定痕跡'{b}'混入→停止(是正の幻覚防止)")
        old = _unescape_literal(old)
        cnt = text.count(old)
        floor = 1 if expect in (None, 0) else int(expect)
        if strict and expect is not None and cnt != expect:
            raise AssertionError(f"[{label}] strict: 期待{expect}件/実{cnt}件不一致→停止")
        if cnt < floor:
            key = old.strip()[:12]
            near = [l for l in text.splitlines() if key and key in l][:3]
            hint = ("  近傍: " + " / ".join(repr(l[:60]) for l in near)) if near else \
                   "  近傍なし=oldの語句自体が本文に無い。repr()で表記違いを確認せよ(115鉱山祭)"
            raise AssertionError(f"[{label}] 下限{floor}件/実{cnt}件→停止(空振り)\n{hint}")
        print(f"  [fix] {label}: 実測{cnt}件を置換(下限{floor})")
        # 還元N(2026-07-28): oldがnewの部分文字列である追記型是正(仮宮→仮宮(御旅所))で
        # 単純replace後の残存検査は必ず誤爆する。term_check._mask_expected(2026-07-27)と
        # 同一の『部分文字列包含』パターン。センチネル経由にして包含に非依存化する。
        sent = "\x00FIXSLOT\x00"
        if sent in text:
            raise AssertionError(f"[{label}] センチネル衝突→停止")
        text = text.replace(old, sent)
        if old in text:
            raise AssertionError(f"[{label}] 置換後に残存{text.count(old)}件→停止")
        text = text.replace(sent, new)
    return text

def count_targets(ja, en, keys, ctx=90):
    """還元J(2026-07-26・104カセ鳥/全カウント義務違反5回目の構造対処):
       是正ペアを組む【前】に、対象語の日英全出現を行番号+前後文脈つきで列挙する。
       目についた1箇所だけをペア化して数え漏れる事故(金沢/旭川/潮来/81豊橋/104カセ鳥)を
       構造的に防ぐ。既存assert_total_absentが『消し残り』を守るのに対し、本関数は
       『数え始める前の網羅』を守る。戻り:{tag:{key:件数}}。"""
    res={}
    for tag, text in (('JA', ja), ('EN', en)):
        res[tag]={}
        lines=(text or '').split('\n')
        print(f"\n########## {tag} ##########")
        for k in keys:
            n=(text or '').count(k)
            res[tag][k]=n
            print(f"\n--- [{tag}] '{k}' 総出現 {n} 件 ---")
            for i, l in enumerate(lines, 1):
                if k in l:
                    for m in re.finditer(re.escape(k), l):
                        a=max(0, m.start()-ctx); b=min(len(l), m.end()+ctx)
                        print(f"  L{i}: ...{l[a:b]}...")
    return res


def assert_total_absent(text, words):
    """還元H(2026-07-23・85本目お旅=マルシェお旅を小見出し+本文で数え漏れ):
       置換後に『消したはずの旧語』の総出現をゼロ検証する。全カウント義務のコード化。
       words=[旧語,...] を渡し、1件でも残れば停止(目についた箇所だけ置換して残る同型ミスを封じる)。"""
    for w in words:
        c=text.count(w)
        assert c==0, f"[全カウント義務] 旧語'{w}'が{c}件残存→数え漏れ(小見出し/別表記を確認)"



def run_all_checks(qid, ja, en, strict=True):
    """還元Q(2026-07-28・117伊勢えび祭): 検出器の呼び出しをBlock1で手書きしない。
       同一ターンで3回(run_all誤名/run引数順/detect_en_term_mismatchの戻り値数)、
       いずれも『シグネチャを確認せず推測で呼んだ』事故を起こした。原因が同じである以上
       注意では止まらない→呼び出しを一度テストした単一入口に固定し、推測の余地を消す。
       戻り: (ng_flag, lines)。strict=Trueなら呼び出し誤り(AttributeError/TypeError)は
       握りつぶさず送出する(還元O)。"""
    import graft_check as gc, term_check as tc
    L = []
    ng_any = False
    inc, sm, label = gc.load_meta(qid)
    L.append(f"== {qid} {label} (inception={inc} start_month={sm}) ==")
    hit, subj, ev = gc.detect_origin_conflict(ja)
    ng_any |= hit
    L.append(f"1 起源主体の自己矛盾 : {'NG' if hit else 'OK'}  {subj}")
    L += [f"     L{i} {s}" for i, s in ev]
    hit, ng = gc.detect_meta_year_conflict(ja, inc, sm)
    ng_any |= hit
    L.append(f"2 DBメタ突合         : {'NG' if hit else 'OK'}"
             + ("  [WARN] start_month=None (投入時に必須セット)" if not sm else ""))
    L += [f"     L{i} [{k}] {v}" for i, k, v in ng]
    hit, ng = gc.detect_status_assertion(ja, en)
    ng_any |= hit
    L.append(f"3 現況断定ガード     : {'NG' if hit else 'OK'}")
    L += [f"     {t} L{i} {v}" for t, i, v in ng]
    hit, ng, warn = gc.detect_reading_mismatch(ja, en)
    ng_any |= hit
    L.append(f"4 訳語の読み照合     : {'NG' if hit else 'OK'}")
    L += [f"     NG   {a} {b}: {c}" for a, b, c in ng]
    L += [f"     WARN {a} {b}: {c}" for a, b, c in warn]
    hit, items = tc.detect_en_term_mismatch(ja, en)
    ng_any |= hit
    L.append(f"5 固有名詞の訳語照合 : {'NG' if hit else 'OK'}")
    L += [f"     {it}" for it in items]
    return ng_any, L

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
    ja,en=strip_citations(ja),strip_citations(en)  # 出典装飾除去
    if fb: print("  [警告] ===EN===欠落→Overview見出しでフォールバック分割+H1正規化を適用")
    cites=[x.get("url_citation",{}).get("url") for x in (msg.get("annotations") or [])
           if x.get("type")=="url_citation"]
    # 還元(2026-07-25・89山鹿): full.mdはstrip_leading_h1+strip_citations適用後の
    # ja/enから再構成して書き出す(照合用生出力にH1/出典装飾を残さずBlock1のH1除去手当てを廃止)
    (OUT/f"{qid}_deepseek_full.md").write_text(ja + "\n\n===EN===\n\n" + en)
    (OUT/f"{qid}_cites.txt").write_text("\n".join(cites))
    print(f"  cites保存 {len(cites)}件 -> {qid}_cites.txt")
    vr=verify(ja,en); usage=data.get("usage",{})
    rep=review(qid,label,ja,en,cites,vr,usage)
    # ★防波堤(2026-07-25・八戸): Pro校正の前に機械検出までのreview.mdを必ず書き出す。
    #   Pro校正が通信例外等で落ちても本体(生成+機械検出)は失われない。
    (OUT/f"{qid}_review.md").write_text(rep)
    # ---- Pro校正工程(2026-07-24・86灘で確立: 短クエリ検索接地・C-3bで要一次照合) ----
    print("Pro校正中(deepseek-v4-pro・短クエリ検索接地)...")
    pro_txt, pro_cites, pro_usage = pro_proofread(qid, label, pref, ja, en, key)
    rep += "\n\n## 【Pro校正・要一次照合(C-3b: Proの正解データは信用せず必ず人が一次照合)】\n"
    rep += f"(model=deepseek-v4-pro / cost=${pro_usage.get('cost')} / tokens {pro_usage.get('total_tokens')})\n\n"
    rep += pro_txt + "\n\n### Pro参照URL(要実在確認)\n"
    rep += ("\n".join(f"- {u}" for u in pro_cites) if pro_cites else "- (0件=検索接地失敗の可能性・要確認)")
    _bad = audit_pro_sources(pro_cites)
    if _bad:
        rep += "\n\n### ★Pro参照URLの一次ソース警告(ステージング/プロキシ/転載)\n"
        rep += "\n".join(f"- {h}  {u}" for h, u in _bad)
    _con, _den = classify_pro_findings(pro_txt)
    rep += f"\n\n### Pro指摘の分類: 具体指摘{len(_con)}件 / 確認不可{len(_den)}件"
    if _den:
        rep += ("\n※確認不可はProの検索に一次公式が入らなかっただけの可能性が高い"
                "(過剰否定8例)。是正候補に入れず『要再検索の論点』として扱う。\n")
        rep += "\n".join(f"- (確認不可) {b.splitlines()[0][:70]}" for b in _den)
    (OUT/f"{qid}_review.md").write_text(rep)
    print(f"  Pro校正完了 cost=${pro_usage.get('cost')} 参照URL{len(pro_cites)}件")
    print(f"完了 {el:.0f}秒 cost=${usage.get('cost')}")
    print(f"検算 ja{vr['ja_len']} en{vr['en_len']} 見出し{vr['h']} 太字{vr['b']} => {'OK' if vr['ok'] else 'NG'}")
    print(f"出力: llm_sim/{qid}_deepseek_full.md / {qid}_review.md")
    print("\n>>> 次: review.md を人/Claudeが照合 -> OKなら既存投入ブロックへ手動接続(本番投入は不可逆・別途確認)")

from orphan_fix import absorb_orphan_attribution, detect_orphan_attribution, absorb_attribution_frames  # 還元K
def strip_citations(s, *a, **k):
    return strip_bare_citations(absorb_orphan_attribution(_strip_citations_base(absorb_attribution_frames(s), *a, **k)))


if __name__=="__main__":
    main()

