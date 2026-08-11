# -*- coding: utf-8 -*-
# DECIDE_v1 : 旧表記1件の処遇を決める唯一の入口。判定順序をここに固定する。
# 順序 = SIBLING_COHERENCE -> REFERENCE_APPOSITIVE -> PLACENAME_v2 -> hold
# 各段は (verdict, why) を返し、最初に確定した段で打ち切る。順序を変える時はここだけ直す。
import re
import nxmix, nxrules

ORDER = ["SIBLING_COHERENCE_v1", "REFERENCE_APPOSITIVE_v1", "PLACENAME_v2"]

def _sentences_with(term, en):
    return [s.strip() for s in nxmix.sentences(en or "") if nxrules._pat(term).search(s)]

def sibling(term, en, ja):
    for s in _sentences_with(term, en):
        sib = [v for k, v in nxmix.CANON.items() if k != term and nxrules._pat(v).search(s)]
        if sib:
            return "apply", "SIBLING_COHERENCE_v1: 同一文に正式形 " + ",".join(sib)
    return None, None

def appositive(term, en, ja):
    m = re.search(r"([A-Z][\w\-]+)\s+of\s+" + re.escape(term) + r"(?![0-9A-Za-z])", en or "")
    if m:
        return "apply", "REFERENCE_APPOSITIVE_v1: 『%s of %s』=人物・物の所属先" % (m.group(1), term)
    return None, None

def placename(term, en, ja):
    v, why, sig = nxrules.judge(term, en or "", ja or "")
    return (("reject", why) if v == "reject" else (None, None))

STAGES = {"SIBLING_COHERENCE_v1": sibling,
          "REFERENCE_APPOSITIVE_v1": appositive,
          "PLACENAME_v2": placename}

def decide(term, en, ja):
    for name in ORDER:
        v, why = STAGES[name](term, en, ja)
        if v:
            return v, why, name
    return "hold", "全規則が不発(要人手または規則追加)", None
