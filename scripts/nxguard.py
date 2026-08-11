"""nxguard : 掲載前ガード v2。判定軸は規則の抽出元文 (date_rule_src)。"""
import re

RE_LUNAR = re.compile(r"旧暦|太陰暦|中秋の名月|十五夜")
RE_PAST  = re.compile(r"かつて|以前は|までは|廃止|行われていた|開催されていた|催されていた|行なわれていた")
RE_NOW   = re.compile(r"毎年|例年|現在|近年|以降は|現行|からは")
RE_CONCEPT_T = re.compile(r"三大|一覧|総称")
RE_CONCEPT_B = re.compile(r"の総称であ|を総称して|の一覧であ")

def is_concept(title, intro):
    if RE_CONCEPT_T.search(title or ""): return "title"
    m = RE_CONCEPT_B.search(intro or "")
    return "body:" + m.group(0) if m else None

def month_of(rule):
    m = re.search(r"(\d{1,2})月", rule or "")
    return int(m.group(1)) if m else None

def date_sents(intro, month):
    if not intro or not month: return []
    return [s for s in re.split(r"[。\n]", intro) if ("%d月" % month) in s]

def guard(title, intro, rule, src):
    c = is_concept(title, intro)
    if c: return ("concept", "概念/一覧記事 (" + c + ")")
    base, axis = (src or "").strip(), "src"
    if not base:
        base, axis = " ".join(date_sents(intro, month_of(rule))), "month_sent"
    if not base:
        return ("nosrc", "根拠文が特定できない")
    m = RE_LUNAR.search(base)
    if m: return ("lunar", "旧暦基準 (" + m.group(0) + "/" + axis + ")")
    m = RE_PAST.search(base)
    if m and not RE_NOW.search(base):
        return ("past", "過去の開催日記述 (" + m.group(0) + "): " + base[:34])
    return ("ok", "")
