# -*- coding: utf-8 -*-
# nxenchk.py  ENLABEL_v1 2026-08-11
# label_en は Wikidata 由来で生成にも検査にも触れられないままURLになる。
# EN本文に存在しない固有トークンを含む label_en を不整合として弾く。
import re, unicodedata
STOP = {"festival","festivals","matsuri","odori","the","of","and","in","at","no","great",
        "annual","city","town","village","shrine","temple","fireworks","parade","carnival",
        "event","day","days","night","summer","spring","autumn","winter","grand","sacred"}
def norm(s):
    s = unicodedata.normalize('NFKD', s or '')
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9]', '', s.lower())
def tokens(label):
    out = []
    for t in re.split(r'[^A-Za-z0-9\u00c0-\u024f]+', label or ''):
        n = norm(t)
        if len(n) >= 4 and n not in STOP: out.append((t, n))
    return out
def check(label_en, body_en):
    if not label_en: return {'ok': False, 'why': 'no_label_en', 'missing': []}
    if not body_en:  return {'ok': False, 'why': 'no_body_en', 'missing': []}
    tk = tokens(label_en)
    if not tk: return {'ok': False, 'why': 'no_significant_token', 'missing': []}
    nb = norm(body_en)
    miss = [t for t, n in tk if n not in nb]
    return {'ok': not miss, 'why': 'ok' if not miss else 'token_not_in_body', 'missing': miss}
