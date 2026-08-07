"""JA漢字固有名とEN音写の対応を『列挙するだけ』の抽出器(2026-08-04)。
★判定しない。正誤の判断はProの検索接地に委ねる。
★理由=音写の正誤は音写距離/頻度/読み/提示型の4方式すべてで機械判定が不成立と実測で確定(02参照)。
  しかし『対応づけて並べる』工程は決定論で書ける。142三国花火でClaudeが手でやったのはこれだけ。
★種別語(駅/川/神社/寺/公園/橋/城/IC)を持つ固有名に限る=JA/EN双方に対応語があるため対応が構造的に決まる。
  任意の固有名を拾うと1本あたり中央値65件で面積が減らない(提示型の失敗)。本方式は中央値6件。
★2026-08-06: EN側で『From Hiroshima Station』→"From Hiroshima"、『Hibiya Line Hibiya Station』
  →"Line Hibiya" のように、直前の前置詞・路線語まで固有名として切り出していた。146広島で
  この断片をProへ投げ、Proが誤って修正案を出し、停止条件になった(自律駆動の律速)。
  先頭の機能語・交通事業者語を剥がす _clean_en を追加。判定はせず、列挙の質だけを直す。
"""
import re

JA_RE = {
 '駅':   re.compile(r'([一-龥ァ-ヴ]{2,8})駅'),
 '川':   re.compile(r'([一-龥ァ-ヴ]{2,6})川'),
 '神社': re.compile(r'([一-龥ァ-ヴ]{2,8})神社'),
 '寺':   re.compile(r'([一-龥ァ-ヴ]{2,8})寺'),
 '公園': re.compile(r'([一-龥ァ-ヴ]{2,8})公園'),
 '橋':   re.compile(r'([一-龥ァ-ヴ]{2,6})橋'),
 '城':   re.compile(r'([一-龥ァ-ヴ]{2,6})城'),
 'IC':   re.compile(r'([一-龥ァ-ヴ]{2,8})(?:IC|インターチェンジ)'),
}
EN_RE = {
 '駅':   re.compile(r'\b([A-Z][A-Za-z\-\u2019]{1,24}(?:\s+[A-Z][A-Za-z\-]{1,20})?)\s+Station\b'),
 '川':   re.compile(r'\b([A-Z][A-Za-z\-]{1,20})\s+River\b'),
 '神社': re.compile(r'\b([A-Z][A-Za-z\-\u2019]{1,24})\s+(?:Shrine|Jinja)\b'),
 '寺':   re.compile(r'\b([A-Z][A-Za-z\-\u2019]{1,24})\s+Temple\b'),
 '公園': re.compile(r'\b([A-Z][A-Za-z\-]{1,20}(?:\s+[A-Z][A-Za-z\-]{1,20})?)\s+Park\b'),
 '橋':   re.compile(r'\b([A-Z][A-Za-z\-]{1,20})\s+Bridge\b'),
 '城':   re.compile(r'\b([A-Z][A-Za-z\-]{1,20})\s+Castle\b'),
 'IC':   re.compile(r'\b([A-Z][A-Za-z\-]{1,24})\s+(?:Interchange|IC)\b'),
}

# JA側の抽出崩れ(種別語の直前が普通名詞)。正誤判定ではなく列挙ノイズの除去のみ。
_JA_NG = ('最寄', '各', '同', '当', '本', '複数', '臨時', '有料', '無料', '会場', '周辺', '河')
# 2026-08-05: 県名(神奈川/石川/香川/旭川市等)と広域道路の断片(圏央道相模原愛+川)を誤って
# 『川』として拾っていた。存在しない地名の確認をProへ投げるため過剰捕捉は害になる。
_PREF_KAWA = ('神奈', '石', '香')          # 神奈川県/石川県/香川県
_ROAD_FRAG = re.compile(r'(道|自動車|高速|国道)')  # 『央道相模原愛』型の断片

# EN側の先頭に紛れる機能語・交通事業者語。固有名の一部ではないので剥がす。
_EN_LEAD = ('From', 'To', 'At', 'In', 'On', 'Near', 'The', 'A', 'An', 'Via', 'By', 'And', 'Or',
            'Of', 'For', 'With', 'Around', 'Between', 'Through', 'After', 'Before', 'During',
            'Take', 'Walk', 'Board', 'Alight', 'Exit', 'Nearest',
            'JR', 'Line', 'Metro', 'Subway', 'Railway', 'Railways', 'Toei', 'Shinkansen',
            'Bus', 'Tram', 'Streetcar', 'Local', 'Express', 'Rapid', 'Limited')


def _drop_ja(kind, w):
    if w in _JA_NG or len(w) < 2: return True
    if kind == '川' and (w in _PREF_KAWA or _ROAD_FRAG.search(w)): return True
    return False


def _clean_en(w):
    """先頭の機能語・路線語を剥がす。剥がした結果が空/1字なら列挙しない(空文字を返す)。"""
    parts = w.split()
    while parts and parts[0] in _EN_LEAD:
        parts.pop(0)
    out = ' '.join(parts)
    return out if len(out) >= 2 else ''


def collect(ja, en):
    """種別ごとに {kind, ja[], en[]} を返す。判定は行わない。"""
    out = []
    for k in JA_RE:
        js = sorted({m for m in JA_RE[k].findall(ja or '') if not _drop_ja(k, m)})
        es = sorted({c for c in (_clean_en(m) for m in EN_RE[k].findall(en or '')) if c})
        if js or es:
            out.append({'kind': k, 'ja': js, 'en': es})
    return out


def size(rows):
    return sum(max(len(r['ja']), len(r['en'])) for r in rows)


def as_defects(ja, en):
    """Pro照合ループへ渡す形。judge=Falseで『判定済みの赤字ではない』ことを明示する。"""
    ds = []
    seen = set()
    for r in collect(ja, en):
        if not r['ja'] and not r['en']:
            continue
        # 2026-08-06(146広島): 駅と城など別種別から同一の JA/EN 組が出て同じ問いを二度Proへ投げ、
        # 『偽陽性』と『検証不能』の相反する答えが返った。非決定性の除去とPro呼数の削減。
        _k = ('、'.join(r['ja']), ', '.join(r['en']))
        if _k in seen:
            continue
        seen.add(_k)
        ds.append({
            'detector': 'translit_check',
            'judge': False,
            'kind': r['kind'],
            'target': 'JA[%s] / EN[%s]' % ('、'.join(r['ja']), ', '.join(r['en'])),
            'ask': ('JA本文の固有名とEN本文のローマ字表記が同一の対象を指し、'
                    'かつENの表記が公式表記と一致しているかを検索で確認せよ。'
                    '意味翻訳が正当な語(神社→Shrine等)は一致とみなす。'),
        })
    return ds


### NOISE_GUARD_v1 — EN空・3件以上の列挙はProで検証不能なので送らない
import re as _re
_JA_RE=_re.compile(r"JA\[(.*?)\]"); _EN_RE=_re.compile(r"EN\[(.*?)\]")
def _noise_reason(d):
    s=str(d)
    mj=_JA_RE.search(s); me=_EN_RE.search(s)
    if not mj or not me: return None
    ja=[x for x in _re.split(r"[、,\uff0f/\s]+", mj.group(1)) if x]
    en=[x for x in _re.split(r"[,\uff0f/]+", me.group(1)) if x.strip()]
    if not en: return "EN側が空(照合対象なし)"
    if len(ja)>2 or len(en)>2: return f"列挙JA{len(ja)}/EN{len(en)}件(一括では検証不能)"
    return None
_raw_as_defects = as_defects
def as_defects(*a, **k):
    out = _raw_as_defects(*a, **k)
    keep=[]
    for d in out:
        r=_noise_reason(d)
        if r: print(f"  [prefilter] Pro送信除外: {str(d)[:60]} | {r}")
        else: keep.append(d)
    return keep
