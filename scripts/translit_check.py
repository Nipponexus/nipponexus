"""JA漢字固有名とEN音写の対応を『列挙するだけ』の抽出器(2026-08-04)。
★判定しない。正誤の判断はProの検索接地に委ねる。
★理由=音写の正誤は音写距離/頻度/読み/提示型の4方式すべてで機械判定が不成立と実測で確定(02参照)。
  しかし『対応づけて並べる』工程は決定論で書ける。142三国花火でClaudeが手でやったのはこれだけ。
★種別語(駅/川/神社/寺/公園/橋/城/IC)を持つ固有名に限る=JA/EN双方に対応語があるため対応が構造的に決まる。
  任意の固有名を拾うと1本あたり中央値65件で面積が減らない(提示型の失敗)。本方式は中央値6件。
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


def collect(ja, en):
    """種別ごとに {kind, ja[], en[]} を返す。判定は行わない。"""
    out = []
    for k in JA_RE:
        js = sorted({m for m in JA_RE[k].findall(ja or '') if m not in _JA_NG})
        es = sorted(set(EN_RE[k].findall(en or '')))
        if js or es:
            out.append({'kind': k, 'ja': js, 'en': es})
    return out


def size(rows):
    return sum(max(len(r['ja']), len(r['en'])) for r in rows)


def as_defects(ja, en):
    """Pro照合ループへ渡す形。judge=Falseで『判定済みの赤字ではない』ことを明示する。"""
    ds = []
    for r in collect(ja, en):
        if not r['ja'] and not r['en']:
            continue
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
