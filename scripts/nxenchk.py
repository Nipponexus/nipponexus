# -*- coding: utf-8 -*-
# nxenchk.py  ENLABEL_v2 2026-08-12
# label_en(Wikidata由来)は生成にも検査にも触れられないままURLになる。EN本文の語集合と照合する。
# v1は正規化で語境界を消し "Kakudana" が "Kakuda Nanohana" に部分一致して素通りした。語単位で判定する。
import re, unicodedata
STOP = {"festival","festivals","matsuri","odori","the","of","and","in","at","no","great",
        "annual","city","town","village","shrine","temple","fireworks","parade","carnival",
        "event","day","days","night","summer","spring","autumn","winter","grand","sacred",
        "international","national","traditional","ceremony","service","rite","rites"}
HOLD_RATIO = 0.5
def _w(t):
    t = unicodedata.normalize('NFKD', t or '')
    t = ''.join(ch for ch in t if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9]', '', t.lower())
def words(text):
    return {w for w in (_w(t) for t in re.split(r'[^0-9A-Za-z\u00c0-\u024f]+', text or '')) if w}
def tokens(label):
    out = []
    for t in re.split(r'[^0-9A-Za-z\u00c0-\u024f]+', label or ''):
        n = _w(t)
        if len(n) >= 4 and n not in STOP: out.append((t, n))
    return out
def check(label_en, body_en):
    if not label_en: return {'ok': False, 'why': 'no_label_en', 'missing': [], 'ratio': 1.0}
    if not body_en:  return {'ok': False, 'why': 'no_body_en', 'missing': [], 'ratio': 1.0}
    tk = tokens(label_en)
    if not tk: return {'ok': False, 'why': 'no_significant_token', 'missing': [], 'ratio': 1.0}
    bw = words(body_en)
    miss = [t for t, n in tk if n not in bw]
    ratio = len(miss) / len(tk)
    ok = ratio < HOLD_RATIO
    return {'ok': ok, 'why': 'ok' if ok else 'token_not_in_body',
            'missing': miss, 'ratio': round(ratio, 2)}
# 原欠陥を固定フィクスチャとして埋め込む。素通りしたらimportで落とす。
_BODY = "The Kakuda Canola Flower Festival (Kakuda Nanohana Matsuri) is held in Kakuda City."
assert check("Kakudana Flower Festival", _BODY)['ok'] is False, 'FIXTURE: 原欠陥を検出できていない'
assert check("Kakuda Canola Flower Festival", _BODY)['ok'] is True, 'FIXTURE: 正当な label_en を弾いた'
assert check("Yasaka Jinja Gion Matsuri", "Yasaka Shrine Gion Matsuri in Kakegawa")['ok'] is True
assert check("Crow-dipper sprouts", "Hangesho is a seasonal marker.")['ok'] is False
if __name__ == '__main__':
    print('[OK] nxenchk self-test 4/4')
