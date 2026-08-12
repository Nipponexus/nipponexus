# -*- coding: utf-8 -*-
# nxenchk.py  ENLABEL_v4 2026-08-12
# label_en(Wikidata由来)は生成にも検査にも触れられないままURLになる。EN本文と語単位で照合し、
# 本文に存在しない造語がslug化されるのを止める。停止は「全滅」と「近似語あり=誤字/文字化け」の2条件のみ。
# v1:語境界消失で素通り / v2:分かち書きと有意語皆無を誤判定 / v3:長音ouと4字語で偽陽性6件
import re, unicodedata, difflib
STOP = {"festival","festivals","matsuri","odori","the","of","and","in","at","no","great",
        "annual","city","town","village","shrine","temple","fireworks","parade","carnival",
        "event","day","days","night","summer","spring","autumn","winter","grand","sacred",
        "international","national","traditional","ceremony","service","rite","rites"}
SUFFIX = ("matsuri","festival","odori","jinja","taisai","sai","shrine")
SPLIT = r'[^0-9A-Za-z\u00c0-\u024f]+'
NEAR = 0.8
def _w(t):
    t = unicodedata.normalize('NFKD', t or '')
    t = ''.join(ch for ch in t if not unicodedata.combining(ch))
    t = re.sub(r'[^a-z0-9]', '', t.lower())
    t = t.replace('ou', 'o').replace('uu', 'u').replace('oo', 'o')
    return t
def wordlist(text):
    return [w for w in (_w(t) for t in re.split(SPLIT, text or '')) if w]
def forms(text):
    ws = wordlist(text); s = set(ws)
    for i in range(len(ws)-1):
        s.add(ws[i]+ws[i+1])
        if i+2 < len(ws): s.add(ws[i]+ws[i+1]+ws[i+2])
    return s, ws
def tokens(label):
    out = []
    for t in re.split(SPLIT, label or ''):
        n = _w(t)
        if len(n) >= 4 and n not in STOP: out.append((t, n))
    return out
def _hit(n, fset, ws):
    if n in fset: return True
    if len(n) >= 4 and any(n in w for w in ws if len(w) > len(n)): return True
    for sfx in SUFFIX:                      # taikomatsuri -> taiko
        if n.endswith(sfx) and len(n) > len(sfx) + 2:
            if _hit(n[:-len(sfx)], fset, ws): return True
    return False
def _near(n, ws):
    m = difflib.get_close_matches(n, [w for w in set(ws) if w != n], n=1, cutoff=NEAR)
    return m[0] if m else None
def check(label_en, body_en):
    if not label_en: return {'ok': False, 'why': 'no_label_en', 'missing': [], 'near': {}}
    if not body_en:  return {'ok': False, 'why': 'no_body_en', 'missing': [], 'near': {}}
    fset, ws = forms(body_en)
    tk = tokens(label_en)
    if not tk:
        return {'ok': True, 'why': 'unjudgeable', 'missing': [], 'near': {}}
    miss = [(t, n) for t, n in tk if not _hit(n, fset, ws)]
    near = {t: _near(n, ws) for t, n in miss if _near(n, ws)}
    if len(miss) == len(tk):
        return {'ok': False, 'why': 'all_tokens_absent', 'missing': [t for t,_ in miss], 'near': near}
    if near:
        return {'ok': False, 'why': 'near_miss_typo', 'missing': [t for t,_ in miss], 'near': near}
    return {'ok': True, 'why': 'ok' if not miss else 'partial',
            'missing': [t for t,_ in miss], 'near': {}}
# 実データ由来の固定フィクスチャ。目視回帰に頼らずimport時に検証する(v1はこれが無く素通りを見逃した)。
FX = [
 ("Kakudana Flower Festival", "The Kakuda Canola Flower Festival (Kakuda Nanohana Matsuri).", False, 'FX1 原欠陥'),
 ("Kakuda Canola Flower Festival", "The Kakuda Canola Flower Festival (Kakuda Nanohana Matsuri).", True, 'FX2 正当'),
 ("Aoi Matsuri", "The Aoi Matsuri is held in Kyoto.", True, 'FX3 有意語なし'),
 ("PL Art of Fireworks", "The display in Tondabayashi.", True, 'FX4 判定不能'),
 ("Kurama Himatsuri", "Kurama no Hi Matsuri is a fire festival.", True, 'FX5 分かち書き'),
 ("Saidai-ji Eyo", "Saidaiji Eyo is held in Okayama.", True, 'FX6 連結'),
 ("Hōnen Matsuri", "The Hounen Matsuri at Tagata Jinja.", True, 'FX7 長音ou'),
 ("Hōjōya", "Hojouya is held at Hakozaki.", True, 'FX8 長音ou単独'),
 ("Uwajima Ushi-oni Festival", "The Uwajima Ushioni parade.", True, 'FX9 4字部分一致'),
 ("Doi taikomatsuri", "The Doi Taiko Festival in Shikokuchuo.", True, 'FX10 接尾辞'),
 ("Gero Ta-no-Kami Festival", "The Gero rice field deity rite.", True, 'FX11 別訳は通す'),
 ("Kanuma lmamiya Shrine Festival", "Kanuma Imamiya Shrine Festival.", False, 'FX12 文字化け'),
 ("Crow-dipper sprouts", "Hangesho is a seasonal marker.", False, 'FX13 未使用直訳'),
]
for lab, bod, exp, tag in FX:
    got = check(lab, bod)['ok']
    assert got is exp, '%s: expected %s got %s (%s)' % (tag, exp, got, check(lab, bod))
if __name__ == '__main__': print('[OK] nxenchk v4 self-test %d/%d' % (len(FX), len(FX)))
