# -*- coding: utf-8 -*-
# MIX_v1 : 同一文内で「正式形の兄弟語」と「旧表記」が混在する箇所を検出する読み取り専用モジュール
import re
CANON = {
    "Todaiji": "T\u014ddai-ji", "Kofukuji": "K\u014dfuku-ji", "Sensoji": "Sens\u014d-ji",
    "Kasuga Taisha": "Kasuga-taisha", "Sumiyoshi Taisha": "Sumiyoshi-taisha",
    "Suwa Taisha": "Suwa-taisha", "Eiheiji": "Eihei-ji", "Yamadera": "Yama-dera",
}
_SPLIT = re.compile(r"(?<=[.!?])\s+")

def _pat(w):
    return re.compile(r"(?<![0-9A-Za-z-])" + re.escape(w) + r"(?![0-9A-Za-z])")

def sentences(t):
    return [s for s in _SPLIT.split(t or "") if s.strip()]

def scan_text(t):
    out = []
    for s in sentences(t):
        olds = [k for k in CANON if _pat(k).search(s)]
        news = [v for v in CANON.values() if _pat(v).search(s)]
        if olds and news:
            out.append({"sentence": s.strip()[:300], "old": olds, "new": news})
    return out

def scan_db(con, cols=("manual_content_en", "manual_content_ja")):
    rows = []
    q = "select qid,%s from festivals" % ",".join(cols)
    for r in con.execute(q):
        for i, c in enumerate(cols):
            for hit in scan_text(r[1 + i]):
                hit["qid"] = r[0]; hit["col"] = c; rows.append(hit)
    return rows
