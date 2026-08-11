"""nxcal : DB だけを見てカレンダーを生成する。外部照会ゼロ。日次実行の本体。"""
import os, re, json, sqlite3, datetime

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
OUTD = os.path.join(ROOT, "out")
DOW  = {"月":0,"火":1,"水":2,"木":3,"金":4,"土":5,"日":6}
PUBLISHABLE = ("ok",)

def calc(rule, year):
    r = rule or ""
    m = re.match(r"毎年(\d{1,2})月(\d{1,2})日〜(\d{1,2})月(\d{1,2})日", r)
    if m:
        return (datetime.date(year, int(m.group(1)), int(m.group(2))),
                datetime.date(year, int(m.group(3)), int(m.group(4))))
    m = re.match(r"毎年(\d{1,2})月(\d{1,2})日$", r)
    if m:
        a = datetime.date(year, int(m.group(1)), int(m.group(2))); return (a, a)
    m = re.match(r"毎年(\d{1,2})月第(\d)([月火水木金土日])曜日", r)
    if m:
        mo, n, d = int(m.group(1)), int(m.group(2)), DOW[m.group(3)]
        f = datetime.date(year, mo, 1)
        a = f + datetime.timedelta(days=((d - f.weekday()) % 7) + 7 * (n - 1))
        return (a, a) if a.month == mo else None
    m = re.match(r"毎年(\d{1,2})月最終([月火水木金土日])曜日", r)
    if m:
        mo, d = int(m.group(1)), DOW[m.group(2)]
        nm = datetime.date(year + (1 if mo == 12 else 0), 1 if mo == 12 else mo + 1, 1)
        last = nm - datetime.timedelta(days=1)
        a = last - datetime.timedelta(days=(last.weekday() - d) % 7)
        return (a, a)
    return None

def load():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    cols = set(r[1] for r in c.execute("PRAGMA table_info(festivals)"))
    if "date_guard" not in cols:
        c.close(); raise RuntimeError("date_guard 列がない。step77 を NX_APPLY=1 で実行のこと")
    want = [x for x in ("qid","label_ja","prefecture","date_rule","date_guard","date_verified") if x in cols]
    rows = [dict(r) for r in c.execute(
        "SELECT " + ",".join(want) + " FROM festivals "
        "WHERE date_rule IS NOT NULL AND date_rule<>'' AND date_guard IS NOT NULL")]
    c.close(); return rows

def upcoming(rows, days, today=None):
    today = today or datetime.date.today()
    end = today + datetime.timedelta(days=days)
    hits = []
    for r in rows:
        if r.get("date_guard") not in PUBLISHABLE: continue
        for y in (today.year, today.year + 1):
            d = calc(r.get("date_rule"), y)
            if not d: continue
            a, b = d
            if a <= end and b >= today:
                hits.append((a, b, r)); break
    hits.sort(key=lambda x: x[0]); return hits

def _tbl(hits):
    L = ["| 開催日 | 祭り | 都道府県 | 根拠となる規則 | 出典 |", "|---|---|---|---|---|"]
    for a, b, r in hits:
        d = a.strftime("%m月%d日") + ("〜" + b.strftime("%m月%d日") if b != a else "")
        t = r.get("label_ja") or ""
        L.append("| " + d + " | " + t + " | " + (r.get("prefecture") or "-") + " | "
                 + (r.get("date_rule") or "") + " | [jawiki](https://ja.wikipedia.org/wiki/" + t + ") |")
    return L

NEXT_N = 12

def upcoming_n(rows, n, today=None):
    """日数窓ではなく件数固定。年をまたいで必ず n 件返す。冬の空白対策。"""
    today = today or datetime.date.today()
    hits = []
    for r in rows:
        if r.get("date_guard") not in PUBLISHABLE: continue
        for y in (today.year, today.year + 1):
            d = calc(r.get("date_rule"), y)
            if not d: continue
            a, b = d
            if b >= today:
                hits.append((a, b, r)); break
    hits.sort(key=lambda x: x[0])
    return hits[:n]

def annual(rows, year=None):
    year = year or datetime.date.today().year
    out = []
    for r in rows:
        if r.get("date_guard") not in PUBLISHABLE: continue
        d = calc(r.get("date_rule"), year)
        if d: out.append((d[0], d[1], r))
    out.sort(key=lambda x: x[0]); return out

NEXT_N = 12

def upcoming_n(rows, n, today=None):
    """日数窓ではなく件数固定。年をまたいで必ず n 件返す。冬の空白対策。"""
    today = today or datetime.date.today()
    hits = []
    for r in rows:
        if r.get("date_guard") not in PUBLISHABLE: continue
        for y in (today.year, today.year + 1):
            d = calc(r.get("date_rule"), y)
            if not d: continue
            a, b = d
            if b >= today:
                hits.append((a, b, r)); break
    hits.sort(key=lambda x: x[0])
    return hits[:n]

def annual(rows, year=None):
    year = year or datetime.date.today().year
    out = []
    for r in rows:
        if r.get("date_guard") not in PUBLISHABLE: continue
        d = calc(r.get("date_rule"), year)
        if d: out.append((d[0], d[1], r))
    out.sort(key=lambda x: x[0]); return out

def render(today=None):
    today = today or datetime.date.today()
    rows = load()
    nx = upcoming_n(rows, NEXT_N, today)
    an = annual(rows, today.year)
    L = ["# 日本の祭り カレンダー（自動生成）", "",
         "最終更新: " + today.isoformat() + " / 収録 " + str(len(an)) + " 件", "",
         "日付は各記事に記載された開催規則（例「7月第3土曜日」）から計算した値です。",
         "実際の開催日は主催者の発表を必ずご確認ください。旧暦基準・過去の規則・",
         "記事内の日付と矛盾する行は自動判定で除外しています。", "",
         "## 次に来る祭り " + str(len(nx)) + " 件", ""]
    L += _tbl(nx) if nx else ["該当なし"]
    L += ["", "## 年間一覧（" + str(today.year) + "年 / 月別）", ""]
    for m in range(1, 13):
        mm = [x for x in an if x[0].month == m]
        if not mm: continue
        L += ["### " + str(m) + "月（" + str(len(mm)) + "件）", ""] + _tbl(mm) + [""]
    os.makedirs(OUTD, exist_ok=True)
    md = os.path.join(OUTD, "calendar.md")
    open(md, "w", encoding="utf-8").write("\n".join(L) + "\n")
    js = os.path.join(OUTD, "calendar.json")
    json.dump({"generated": today.isoformat(), "next_n": len(nx), "annual": len(an),
               "items": [{"date_start": a.isoformat(), "date_end": b.isoformat(),
                          "qid": r.get("qid"), "label_ja": r.get("label_ja"),
                          "prefecture": r.get("prefecture"), "rule": r.get("date_rule"),
                          "confidence": r.get("date_verified")} for a, b, r in an]},
              open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return {"next_n": len(nx), "annual": len(an), "md": md, "json": js}

if __name__ == "__main__":
    print(json.dumps(render(), ensure_ascii=False))
