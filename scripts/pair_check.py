"""還元R(2026-07-28・118じゃんとこい魚津/日英ペア漏れ通算7回目): JA側を是正したとき
EN側の対応表現を人が英語で思いつけないと漏れる穴を塞ぐ。既存のcount_targetsは
『渡したキーを数える』までで、キーの発想自体は人依存だった(25/80/118で再発)。
→JA/ENの段落対応(##見出しで区切られたブロックの同位置)から、JA是正箇所に対応する
EN段落を機械的に引き当てて提示する。語彙辞書は不要=対応関係だけを使う。"""
import re

def _blocks(text):
    """見出し行を境界にブロック分割。戻り: [(見出し, 本文行list, 開始行番号)]"""
    lines = (text or "").split("\n")
    out, cur, head, start = [], [], None, 1
    for i, l in enumerate(lines, 1):
        if l.startswith("## "):
            if head is not None or cur:
                out.append((head, cur, start))
            head, cur, start = l.strip(), [], i
        else:
            cur.append((i, l))
    if head is not None or cur:
        out.append((head, cur, start))
    return [b for b in out if b[0] is not None]

def en_counterpart(ja, en, ja_snippet, ctx=200):
    """ja_snippetを含むJA段落を特定し、同位置のEN段落を返す(是正ペア作成の材料)。
       戻り: dict(見つかったか, JA見出し, EN見出し, EN段落テキスト)"""
    jb, eb = _blocks(ja), _blocks(en)
    if len(jb) != len(eb):
        print(f"  [WARN] 段落数不一致 JA={len(jb)} EN={len(eb)} =対応が崩れている可能性")
    for idx, (head, body, _s) in enumerate(jb):
        joined = "\n".join(l for _i, l in body)
        if ja_snippet in joined:
            if idx < len(eb):
                ehead, ebody, _es = eb[idx]
                etext = "\n".join(l for _i, l in ebody).strip()
                print(f"  [対応] JA{head} -> EN{ehead}")
                print(f"  [EN段落] {etext[:ctx*3]}")
                return {"found": True, "ja_head": head, "en_head": ehead, "en_text": etext}
            print(f"  [NG] JA第{idx+1}段落に対応するEN段落が存在しない")
            return {"found": False, "ja_head": head, "en_head": None, "en_text": ""}
    print(f"  [NG] '{ja_snippet}' を含むJA段落が見つからない(表記を確認)")
    return {"found": False, "ja_head": None, "en_head": None, "en_text": ""}

def _match_blocks(ja, snippet):
    """snippetを含むJAブロックの索引を全部返す(曖昧検出のため複数返す)。"""
    out = []
    for idx, (head, body, _s) in enumerate(_blocks(ja)):
        if snippet in "\n".join(l for _i, l in body):
            out.append((idx, head))
    return out


def require_pairs(ja_fixes, ja, en):
    """JA是正ペア(old,new)を受け、各是正のEN対応段落を列挙する。
       ★oldは切り詰めず全文で照合する(30字丸めは別ブロックへの誤対応を生む)。
       ★複数ブロックに一致したら曖昧として警告し、対応を確定させない。"""
    print("=== JA是正に対応するEN段落(ここからENペアを作る) ===")
    jb, eb = _blocks(ja), _blocks(en)
    if len(jb) != len(eb):
        print(f"  [WARN] 段落数不一致 JA={len(jb)} EN={len(eb)} =対応が崩れている可能性")
    res = []
    for item in ja_fixes:
        old = item[0] if isinstance(item, (tuple, list)) else item
        hits = _match_blocks(ja, old)
        print(f"\n--- JA是正: {old[:46]}...")
        if not hits:
            print(f"  [NG] 本文に該当なし(表記を確認・カウント0を不在と読まない)")
            res.append({"found": False, "ambiguous": False, "ja_head": None,
                        "en_head": None, "en_text": ""}); continue
        if len(hits) > 1:
            print(f"  [曖昧] {len(hits)}ブロックに一致 {[h for _i,h in hits]} =oldを一意になるまで伸ばすこと")
            res.append({"found": False, "ambiguous": True, "ja_head": None,
                        "en_head": None, "en_text": ""}); continue
        idx, head = hits[0]
        if idx >= len(eb):
            print(f"  [NG] JA第{idx+1}ブロックに対応するEN段落が存在しない")
            res.append({"found": False, "ambiguous": False, "ja_head": head,
                        "en_head": None, "en_text": ""}); continue
        ehead, ebody, _es = eb[idx]
        etext = "\n".join(l for _i, l in ebody).strip()
        print(f"  [対応] JA{head} -> EN{ehead}")
        print(f"  [EN段落] {etext[:600]}")
        res.append({"found": True, "ambiguous": False, "ja_head": head,
                    "en_head": ehead, "en_text": etext})
    return res
