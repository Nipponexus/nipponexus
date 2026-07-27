# 還元K-2(2026-07-27): 出典リンクを錨に助詞句ごと巻き取る+文法規則ベースの残骸検出
import re
_C = r'\[[^\]]*\]\([^)]*\)'
_SKIP = ('公式情報', 'Official Information')
_JA_P = r'(?:によれば|によると|では|には|でも|および|で|に|は|も|が)'
_V = (r'notes|states|explains|emphasizes|points out|evaluates|reports|confirms|highlights|'
      r'mentions|shows|indicates|suggests|describes|introduces|lists|specifies|records')
# --- A) リンク健在時に枠ごと除去(本命) ---
_FA_JA = re.compile(_C + r'\s*' + _JA_P + r'?\s*[、]?')
_FA_EN = [
 (re.compile(r'According to a ([^,]*?) from (?:the )?' + _C + r'\s*,\s*'), r'According to a \1, '),
 (re.compile(r'According to (?:the )?' + _C + r'\s*,\s*'), ''),
 (re.compile(r'(?:The )?' + _C + r'\s+(?:' + _V + r')\s+that\s+'), ''),
 (re.compile(r'(?:The )?' + _C + r'\s+(?:' + _V + r')\s+'), ''),
 (re.compile(r'\s+(?:in|on|from)\s+(?:the )?' + _C + r'(?=[.,])'), ''),
]
def absorb_attribution_frames(s):
    out = []
    for ln in (s or '').split('\n'):
        if any(k in ln for k in _SKIP):
            out.append(ln); continue
        if re.search(r'[\u3040-\u30ff]', ln):
            ln = _FA_JA.sub('', ln)
        else:
            for rx, rep in _FA_EN:
                ln = rx.sub(rep, ln)
        out.append(ln)
    return '\n'.join(out)
# --- B) 除去後の残骸掃除(保険・文単位) ---
_JA_LEAD = re.compile(r'^\s*(?:によれば、|によると、|では、|では(?=「)|には、|でも(?=[^、])|'
                      r'および(?=[にでは])|の(?=\d)|で(?!き)|に(?!お|よ)|は(?!じ|や)|も(?!ち|う)|が(?![っん]))')
_JA_META = re.compile(r'^(?:.{0,25})?(?:掲載されています|確認できます|記載があります|詳細があります|'
                      r'引用されています|明記されています|記載されています)$')
_JA_PRED = [('という説を紹介している。', 'という説がある。'), ('点を特徴として挙げている。', '点が特徴である。'),
            ('ことを示唆している。', 'とみられる。'), ('ことを紹介している。', '。'), ('ことを説明している。', '。'),
            ('ことを指摘している。', '。'), ('ことを強調している。', '。'), ('ことを評価している。', '。'),
            ('と評価している。', '。'), ('と説明している。', '。'), ('と指摘している。', '。'), ('と紹介している。', '。')]
def _ja_line(l):
    head = re.match(r'^\s*(?:[-*]\s+|\d+\.\s+)?', l).group(0)
    body = l[len(head):]
    if not body: return l
    parts = re.split(r'(?<=。)', body)
    keep = []
    for p in parts:
        if not p.strip(): continue
        q = _JA_LEAD.sub('', p)
        if _JA_META.match(q.rstrip('。')): continue
        keep.append(q)
    n = head + ''.join(keep)
    for a, b in _JA_PRED: n = n.replace(a, b)
    return n
_EN_LEAD = re.compile(r'^\s*(?:The\s+)?(?:' + _V + r')\s+(?:that\s+|how\s+)?')
_EN_DROP = re.compile(r'(?:on|in|from)\s+the\s*\.\s*$|^\s*The\s+(?:' + _V + r')\s+this\b')
_EN_INL = [(re.compile(r'According to (?:the )?,\s*'), ''),
           (re.compile(r'from the ,\s*'), ', '),
           (re.compile(r'\bin the (?=(?:' + _V + r')\b)'), ''),
           (re.compile(r'\s+(?:on|in)\s+the\s*(?=[.,])'), '')]
def _en_line(l):
    head = re.match(r'^\s*(?:[-*]\s+|\d+\.\s+)?', l).group(0)
    body = l[len(head):]
    if not body: return l
    for rx, rep in _EN_INL: body = rx.sub(rep, body)
    parts = re.split(r'(?<=[.!?])\s+', body)
    keep = []
    for p in parts:
        if not p.strip(): continue
        if _EN_DROP.search(p): continue
        q = _EN_LEAD.sub('', p)
        if q and q[0].islower(): q = q[0].upper() + q[1:]
        keep.append(q)
    return head + ' '.join(keep)
def absorb_orphan_attribution(text, lang=None):
    ja = bool(re.search(r'[\u3040-\u30ff]', text)) if lang is None else (lang == 'ja')
    f = _ja_line if ja else _en_line
    return '\n'.join(f(l) for l in text.split('\n'))
def detect_orphan_attribution(ja, en):
    bad = []
    for tag, t in (('JA', ja), ('EN', en)):
        for i, l in enumerate((t or '').split('\n'), 1):
            b = re.sub(r'^\s*(?:[-*]\s+|\d+\.\s+)?', '', l)
            if tag == 'JA':
                for p in re.split(r'(?<=。)', b):
                    if p.strip() and _JA_LEAD.match(p): bad.append((tag, i, p[:100]))
            else:
                for p in re.split(r'(?<=[.!?])\s+', b):
                    if p.strip() and (_EN_LEAD.match(p) or _EN_DROP.search(p)): bad.append((tag, i, p[:100]))
    return (len(bad) > 0, bad)
