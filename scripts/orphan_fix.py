
# 還元K(2026-07-27): strip_citations後に残る空主語(出典リンクが主語だった箇所)を吸収する
import re

_JA_MARK = re.compile(r'(?m)(?:(?<=[。、])|^)[ \u3000]+(?:は、|も、|では、|によれば、|によると、|が)')
_JA_PRED = [
    ('という説を紹介している。', 'という説がある。'),
    ('点を特徴として挙げている。', '点が特徴である。'),
    ('ことを示唆している。', 'とみられる。'),
    ('ことを紹介している。', '。'),
    ('ことを説明している。', '。'),
    ('ことを指摘している。', '。'),
    ('ことを強調している。', '。'),
    ('ことを評価している。', '。'),
    ('と評価している。', '。'),
    ('と説明している。', '。'),
    ('と指摘している。', '。'),
    ('と紹介している。', '。'),
]
_VERBS = (r'notes|states|explains|emphasizes|points out|evaluates|reports|confirms|'
          r'highlights|mentions|shows|indicates|suggests|describes|introduces|lists')
# 句読点(+閉じ引用符)を消費して書き戻す方式。後読みの継ぎ足しをやめ穴を塞ぐ
_P = r'([.!?,](?:["\u201d\u2019])?)'
_EN_REC  = re.compile(_P + r'\s+introduces\s+records\s+from\s+')
_EN_LIST = re.compile(_P + r'\s+lists\s+various\s+theories,\s+including\s+')
_EN_SUGG = re.compile(r'([.!?](?:["\u201d\u2019])?)\s+suggests\s+that\s+')
_EN_THAT = re.compile(_P + r'\s+(?:' + _VERBS + r')\s+that\s+([A-Za-z])')
_EN_HOW  = re.compile(_P + r'\s+describes\s+how\s+([A-Za-z])')
_EN_ACC  = re.compile(r'[Aa]ccording to\s*,\s*([A-Za-z])')
_EN_RESID = re.compile(_P + r'\s+(?:' + _VERBS + r')\b')

def _case(punct, ch):
    # 文末句読点の後は大文字始まり、カンマの後は小文字のまま
    return ch.upper() if not punct.startswith(',') else ch.lower()

def _fix_en_line(l):
    n = l
    if _EN_REC.search(n):
        n = _EN_REC.sub(lambda m: m.group(1) + ' Records from ', n)
        n = n.replace(', which indicate that', ' indicate that')
    n = _EN_LIST.sub(lambda m: m.group(1) + ' Various theories exist, including ', n)
    n = _EN_SUGG.sub(lambda m: m.group(1) + ' It appears that ', n)
    n = _EN_THAT.sub(lambda m: m.group(1) + ' ' + _case(m.group(1), m.group(2)), n)
    n = _EN_HOW.sub(lambda m: m.group(1) + ' ' + _case(m.group(1), m.group(2)), n)
    n = _EN_ACC.sub(lambda m: m.group(1).upper(), n)
    return n

def _fix_ja_line(l):
    if not _JA_MARK.search(l):
        return l
    n = _JA_MARK.sub('', l)
    for a, b in _JA_PRED:
        n = n.replace(a, b)
    return n


def _is_ja(t):
    return bool(re.search(r'[\u3040-\u30ff]', t))

def absorb_orphan_attribution(text, lang=None):
    ja = _is_ja(text) if lang is None else (lang == 'ja')
    f = _fix_ja_line if ja else _fix_en_line
    return '\n'.join(f(l) for l in text.split('\n'))

def detect_orphan_attribution(ja, en):
    bad = []
    for tag, t, rx in (('JA', ja, _JA_MARK), ('EN', en, _EN_RESID)):
        for i, l in enumerate((t or '').split('\n'), 1):
            if rx.search(l):
                bad.append((tag, i, l[:120]))
    return (len(bad) > 0, bad)
