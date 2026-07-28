# -*- coding: utf-8 -*-
"""出典ゼロ段落の検出(2026-07-28・113相模川の姉妹都市捏造を受けた還元)
設計: DeepSeekは検索接地した内容には安定して出典マーカーを付ける。
      よって『マーカーゼロの散文段落』は学習知識からの補完=幻覚の高確度シグナル。
      辞書・ウォッチリスト不要の内部シグナル検査(111接ぎ木と同思想)。
用途: NG断定でなくWARN(人的確認/Proへ狙い撃ち送付する対象の選別)。
"""
import re

CITE = re.compile(r'\[[^\]\n]{3,60}\.(com|jp|org|net|go\.jp|lg\.jp|or\.jp|ne\.jp)[^\]\n]*\]')
# 断定的な固有名詞・数値のシグナル(これが無い一般論の段落は対象外)
SIGNAL = re.compile(
    r'[一-龥ぁ-んァ-ヶ]{2,}(?:市|町|村|県|府|区|寺|神社|大社|宮|城|駅|大学|協会|クラブ|会社|財団|組合)'
    r'|\d{3,4}年|\d+世紀|第\d+回|約?\d+(?:人|匹|基|台|万人)'
)
MIN_LEN = 100

def detect_uncited(ja):
    """出典マーカーが1つも無い散文段落を返す [(para_no, 冒頭, 長さ)]"""
    hits = []
    for i, para in enumerate(ja.split("\n"), 1):
        s = para.strip()
        if not s or s.startswith("#") or s.startswith("- ") or s.startswith("**"):
            continue
        if re.match(r'^\d+\.\s', s):      # 関連情報の番号付きリストは除外
            continue
        if len(s) < MIN_LEN:
            continue
        if CITE.search(s):
            continue
        if not SIGNAL.search(s):
            continue
        hits.append((i, s[:60], len(s)))
    return hits

def report(ja):
    h = detect_uncited(ja)
    if not h:
        return "出典ゼロ段落: OK"
    out = [f"出典ゼロ段落: WARN {len(h)}件(幻覚の疑い=要一次照合/Proへ狙い撃ち送付)"]
    for n, head, ln in h:
        out.append(f"  L{n} ({ln}字): {head}...")
    return "\n".join(out)
