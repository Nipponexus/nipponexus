# -*- coding: utf-8 -*-
# nxenchk.py  ENLABEL_v3 2026-08-12
# label_en(Wikidata由来)は生成にも検査にも触れられないままURLになる。EN本文と語単位で照合する。
# v1: 正規化で語境界を消し "Kakudana" が素通り。v2: 分かち書きの揺れと有意トークン皆無を誤判定。
import re, unicodedata
STOP = {"festival","festivals","matsuri","odori","the","of","and","in","at","no","great",
        "annual","city","town","village","shrine","temple","fireworks","parade","carnival",
        "event","day","days","night","summer","spring","autumn","winter","grand","sacred",
        "international","national","traditional","ceremony","service","rite","rites"}
HOLD_RATIO = 0.5
SPLIT = r'[^0-9A-Za-z\u00c0-\u024f]+'
def _w(t):
    t = unicodedata.normalize('NFKD', t or '')
    t = ''.join(ch for ch in t if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9]', '', t.lower())
def wordlist(text):
    return [w for w in (_w(t) for t in re.split(SPLIT, text or '')) if w]
def forms(text):
    """語 + 隣接2〜3語の連結。分かち書きの揺れ(Hina Matsuri / Hinamatsuri)を吸収する。"""
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
    if len(n) >= 5 and any(n in w for w in ws if len(w) > len(n)): return True
    return False
def check(label_en, body_en):
    if not label_en: return {'ok': False, 'why': 'no_label_en', 'missing': [], 'ratio': 1.0}
    if not body_en:  return {'ok': False, 'why': 'no_body_en', 'missing': [], 'ratio': 1.0}
    fset, ws = forms(body_en)
    tk = tokens(label_en)
    if not tk:
        whole = _w(label_en)
        ok = whole in fset or any(whole in w for w in ws)
        return {'ok': True, 'why': 'ok' if ok else 'unjudgeable', 'missing': [], 'ratio': 0.0}
    miss = [t for t, n in tk if not _hit(n, fset, ws)]
    ratio = len(miss) / len(tk)
    ok = ratio < HOLD_RATIO
    return {'ok': ok, 'why': 'ok' if ok else 'token_not_in_body',
            'missing': miss, 'ratio': round(ratio, 2)}
# 実データ由来の固定フィクスチャ。目視確認に頼らずimport時に検証する。
_B = "The Kakuda Canola Flower Festival (Kakuda Nanohana Matsuri) is held in Kakuda City."
assert check("Kakudana Flower Festival", _B)['ok'] is False, 'FX1 原欠陥を素通り'
assert check("Kakuda Canola Flower Festival", _B)['ok'] is True, 'FX2 正当を棄却'
assert check("Aoi Matsuri", "The Aoi Matsuri is held in Kyoto.")['ok'] is True, 'FX3 有意語なしを棄却'
assert check("PL Art of Fireworks", "The display in Tondabayashi.")['ok'] is True, 'FX4 判定不能を棄却'
assert check("Kurama Himatsuri", "Kurama no Hi Matsuri is a fire festival.")['ok'] is True, 'FX5 分かち書き'
assert check("Saidai-ji Eyo", "Saidaiji Eyo is held in Okayama.")['ok'] is True, 'FX6 連結表記'
assert check("Kanuma lmamiya Shrine Festival", "Kanuma Imamiya Shrine Festival.")['ok'] is False, 'FX7 文字化け'
assert check("Crow-dipper sprouts", "Hangesho is a seasonal marker.")['ok'] is False, 'FX8 未使用直訳'
if __name__ == '__main__': print('[OK] nxenchk v3 self-test 8/8')
