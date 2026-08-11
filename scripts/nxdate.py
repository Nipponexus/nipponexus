# -*- coding: utf-8 -*-
# DATE_v1 : 日本語の開催日表現 -> 機械可読ルール -> 任意年の実日付。
# 設計方針: 毎年変わる情報は照合相手がいない。だが「規則」は不変なので、
# 規則を保存して毎年計算すれば、外部照会なしに永久に更新できる。
# 規則化できないもの(旬・月のみ・不定)は rule=None とし、自動更新の対象外にする。
import re, calendar, datetime

DOW = {"月": 0, "火": 1, "水": 2, "木": 3, "金": 4, "土": 5, "日": 6}
NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
# 特定年の記述を除外する。「2023年（令和5年）10月29日」は毎年の開催日ではない。
YEARISH = re.compile(r"(\d{4}年|令和\d+年|平成\d+年|昭和\d+年|第\d+回)")
RECUR = re.compile(r"(毎年|例年|恒例)")

PATS = [
 ("nth_dow",   re.compile(r"(\d{1,2})月(?:の)?第([一二三四五1-5])[週]?(?:の)?([日月火水木金土])曜日")),
 ("last_dow",  re.compile(r"(\d{1,2})月(?:の)?最終(?:の)?([日月火水木金土])曜日")),
 ("range_fix", re.compile(r"(\d{1,2})月(\d{1,2})日\s*(?:から|〜|～|-|‐|・)\s*(?:(\d{1,2})月)?(\d{1,2})日")),
 ("fixed",     re.compile(r"(\d{1,2})月(\d{1,2})日")),
]

def _tainted(text, pos, back=16):
    """直前に特定年・回数の記述があれば、それは毎年の開催日ではない。"""
    pre = text[max(0, pos - back):pos]
    if RECUR.search(pre):
        return False
    return bool(YEARISH.search(pre))

def parse(text):
    """最初に見つかった規則を返す。見つからなければ None。"""
    if not text:
        return None
    for kind, rx in PATS:
        for m in rx.finditer(text):
            if _tainted(text, m.start()):
                continue
            g = m.groups()
            if kind == "nth_dow":
                r = {"type": "nth_dow", "month": int(g[0]), "nth": NUM.get(g[1], 0), "dow": DOW[g[2]]}
                if not r["nth"]:
                    continue
            elif kind == "last_dow":
                r = {"type": "last_dow", "month": int(g[0]), "dow": DOW[g[1]]}
            elif kind == "range_fix":
                r = {"type": "range_fixed", "month": int(g[0]), "day": int(g[1]),
                     "end_month": int(g[2]) if g[2] else int(g[0]), "end_day": int(g[3])}
            else:
                r = {"type": "fixed", "month": int(g[0]), "day": int(g[1])}
            r["raw"] = m.group(0)
            r["ctx"] = text[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
            r["pos"] = m.start()
            return r
    return None

def evaluate(rule, year):
    """規則 + 年 -> (開始日, 終了日)。計算不能なら None。"""
    if not rule:
        return None
    t = rule["type"]
    try:
        if t == "fixed":
            d = datetime.date(year, rule["month"], rule["day"]); return (d, d)
        if t == "range_fixed":
            a = datetime.date(year, rule["month"], rule["day"])
            b = datetime.date(year, rule["end_month"], rule["end_day"])
            return (a, b)
        if t == "nth_dow":
            first = datetime.date(year, rule["month"], 1)
            off = (rule["dow"] - first.weekday()) % 7
            day = 1 + off + (rule["nth"] - 1) * 7
            last = calendar.monthrange(year, rule["month"])[1]
            if day > last:
                return None
            d = datetime.date(year, rule["month"], day); return (d, d)
        if t == "last_dow":
            last = calendar.monthrange(year, rule["month"])[1]
            d = datetime.date(year, rule["month"], last)
            d -= datetime.timedelta(days=(d.weekday() - rule["dow"]) % 7)
            return (d, d)
    except ValueError:
        return None
    return None

def describe(rule):
    if not rule: return ""
    t = rule["type"]
    if t == "fixed": return "毎年%d月%d日" % (rule["month"], rule["day"])
    if t == "range_fixed": return "毎年%d月%d日〜%d月%d日" % (rule["month"], rule["day"], rule["end_month"], rule["end_day"])
    if t == "nth_dow": return "毎年%d月第%d%s曜日" % (rule["month"], rule["nth"], "月火水木金土日"[rule["dow"]])
    if t == "last_dow": return "毎年%d月最終%s曜日" % (rule["month"], "月火水木金土日"[rule["dow"]])
    return ""

CALC = ("nth_dow", "last_dow")

def verify_against_text(rule, fulltext):
    """独立検証: 規則から過去年の日付を計算し、本文中の『YYYY年…M月D日』と突き合わせる。
    導入部の規則文とは別の箇所(沿革・日程表)に一致があれば、二つ目の根拠になる。"""
    if not rule or rule["type"] not in CALC or not fulltext:
        return None
    hits, miss = [], []
    for m in re.finditer(r"(\d{4})年[^。]{0,24}?(\d{1,2})月(\d{1,2})日", fulltext):
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if not (1990 <= y <= 2030) or mo != rule["month"]:
            continue
        got = evaluate(rule, y)
        if not got:
            continue
        (hits if got[0].day == d else miss).append("%d年%d月%d日(計算=%d日)" % (y, mo, d, got[0].day))
    if not hits and not miss:
        return None
    return {"match": hits[:4], "mismatch": miss[:4], "ok": len(hits) > 0 and len(hits) >= len(miss)}


# >>>NX:VERIFY2
# verify_v2 : v1 の欠陥を修正した独立検証。
#  欠陥1 = 多日開催を考慮せず開始日のみ比較。川越氷川祭(第3土曜と日曜)で偽の不一致。
#  欠陥2 = 同月の無関係な日付(文化財指定日・別行事)を拾う。文脈語で絞る。
HELD = re.compile(r"(開催|行われ|行なわれ|実施|挙行|斎行|催さ|開かれ)")
NOTHELD = re.compile(r"(指定|創建|設立|認定|登録|選択|竣工|落成|廃止|中止|生まれ|死去)")

def verify_v2(rule, fulltext, tol=3):
    """規則から計算した日付と、本文中の実績日を突き合わせる。
    tol 日以内は多日開催の別日とみなし一致扱い。判定材料は文脈語で絞る。"""
    if not rule or not fulltext:
        return None
    match, mism = [], []
    for m in re.finditer(r"(\d{4})年[^。]{0,30}?(\d{1,2})月(\d{1,2})日", fulltext):
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if not (1990 <= y <= 2035) or mo != rule.get("month"):
            continue
        ctx = fulltext[max(0, m.start() - 30): m.end() + 30]
        if NOTHELD.search(ctx) and not HELD.search(ctx):
            continue
        if not HELD.search(ctx):
            continue
        got = evaluate(rule, y)
        if not got:
            continue
        diff = abs((datetime.date(y, mo, d) - got[0]).days)
        rec = "%d年%d月%d日(計算%d日 差%d)" % (y, mo, d, got[0].day, diff)
        (match if diff <= tol else mism).append(rec)
    if not match and not mism:
        return None
    return {"match": match[:4], "mismatch": mism[:4],
            "ok": len(match) > 0 and len(match) > len(mism)}

# カレンダーに置ける型。固定日・期間も毎年同じ日付なので配置可能。
PLACEABLE = ("nth_dow", "last_dow", "fixed", "range_fixed")
# 年ごとに計算が要る型(それ以外は毎年同一日)
NEEDS_CALC = ("nth_dow", "last_dow")
# <<<NX:VERIFY2
