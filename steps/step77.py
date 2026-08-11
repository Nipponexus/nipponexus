#!/usr/bin/env python3
# step77 : 掲載ガード v2 (判定軸を date_rule_src に固定) + 60日カレンダー生成
import os, re, sys, json, sqlite3, shutil, datetime, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
OUTD = os.path.join(ROOT, "out")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [DATE_GUARD_V2_PAGE_20260811]"
APPLY = os.environ.get("NX_APPLY") == "1"
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
OUT = {"ts": TS, "apply": APPLY}

def sec(name, fn):
    try:
        r = fn(); OUT[name] = r; print("[OK] " + name); return r
    except Exception as e:
        OUT[name] = {"error": repr(e)}
        print("[NG] " + name + ": " + str(e)); traceback.print_exc(); return None

def cx():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; return c

def ensure_cols(c, table, cols):
    have = set(r[1] for r in c.execute("PRAGMA table_info(" + table + ")"))
    add = []
    for name, typ in cols:
        if name not in have:
            c.execute("ALTER TABLE %s ADD COLUMN %s %s" % (table, name, typ)); add.append(name)
    c.commit(); return add

# ---------- guard v2 ----------
RE_LUNAR = re.compile(r"旧暦|太陰暦|中秋の名月|十五夜")
RE_PAST  = re.compile(r"かつて|以前は|までは|廃止|行われていた|開催されていた|催されていた|行なわれていた")
RE_NOW   = re.compile(r"毎年|例年|現在|近年|以降は|現行|からは")
RE_CONCEPT_T = re.compile(r"三大|一覧|総称")
RE_CONCEPT_B = re.compile(r"の総称であ|を総称して|の一覧であ")

def is_concept(title, intro):
    if RE_CONCEPT_T.search(title or ""): return "title"
    m = RE_CONCEPT_B.search(intro or "")
    if m: return "body:" + m.group(0)
    return None

def month_of(rule):
    m = re.search(r"(\d{1,2})月", rule or "")
    return int(m.group(1)) if m else None

def date_sents(intro, month):
    if not intro or not month: return []
    return [s for s in re.split(r"[。\n]", intro) if ("%d月" % month) in s]

def guard(title, intro, rule, src):
    """判定軸: 規則の抽出元文(src)。無ければ同月文にフォールバック。"""
    c = is_concept(title, intro)
    if c: return ("concept", "概念/一覧記事 (" + c + ")", src or "")
    base = (src or "").strip()
    axis = "src"
    if not base:
        base = " ".join(date_sents(intro, month_of(rule))); axis = "month_sent"
    if not base:
        return ("nosrc", "根拠文が特定できない", "")
    m = RE_LUNAR.search(base)
    if m: return ("lunar", "旧暦基準 (" + m.group(0) + "/" + axis + ")", base)
    m = RE_PAST.search(base)
    if m and not RE_NOW.search(base):
        return ("past", "過去の開催日記述 (" + m.group(0) + "): " + base[:34], base)
    return ("ok", "", base)

def guard_v1(title, intro, rule):
    if is_concept(title, intro): return "concept"
    base = " ".join(date_sents(intro, month_of(rule))) or (intro or "")
    if RE_LUNAR.search(base): return "lunar"
    for s in date_sents(intro, month_of(rule)):
        if re.search(r"江戸時代|明治時代|かつて|以前は|までは|廃止", s) and not re.search(r"現在|近年|以降は|現行", s):
            return "past"
    return "ok"

def s1():
    cases = [
        ("たてもん祭り", "2007年からは8月第1金曜日・土曜日に行われる。2006年までは8月7日・8日に行なわれていた。",
         "毎年8月第1金曜日", "2007年からは8月第1金曜日・土曜日に行われる", "ok"),
        ("伏木曳山祭", "富山県高岡市伏木地区にて毎年5月第3土曜日に行われる、江戸時代から続く祭礼である。",
         "毎年5月第3土曜日", "毎年5月第3土曜日に行われる", "ok"),
        ("あばれ祭り", "かつては7月7日・8日に行われていた。",
         "毎年7月7日", "かつては7月7日・8日に行われていた", "past"),
        ("采女祭", "中秋の名月にあたる旧暦8月15日に猿沢池で行われる。",
         "毎年8月15日", "旧暦8月15日に猿沢池で行われる", "lunar"),
        ("京都三大祭り", "葵祭・祇園祭・時代祭の総称である。", "毎年8月16日", "", "concept"),
    ]
    ok = True
    for t, i, r, src, want in cases:
        got, why, _ = guard(t, i, r, src)
        good = (got == want); ok = ok and good
        print("    %-12s want=%-8s got=%-8s %s" % (t, want, got, "OK" if good else "NG"))
    assert ok, "guard v2 self-test failed"
    print("  自己検証 OK (5/5) 判定軸=date_rule_src")
    return {"ok": True}

def load_rows():
    c = cx()
    cols = set(r[1] for r in c.execute("PRAGMA table_info(festivals)"))
    want = ["qid","label_ja","prefecture","date_rule","date_rule_src","date_verified","status"]
    need = [x for x in want if x in cols]
    rows = [dict(r) for r in c.execute(
        "SELECT " + ",".join(need) + " FROM festivals WHERE date_rule IS NOT NULL AND date_rule<>''")]
    c.close()
    print("  列: " + ",".join(need))
    return rows

def get_intros(titles):
    import nxwiki
    out = {}
    for i in range(0, len(titles), 20):
        b = titles[i:i+20]
        try: d = nxwiki.extracts(b, intro=True)
        except TypeError: d = nxwiki.extracts(b, True)
        out.update(d or {})
    return out

def s2():
    rows = load_rows()
    nsrc = sum(1 for r in rows if (r.get("date_rule_src") or "").strip())
    print("  規則行 = %d / うち date_rule_src あり = %d" % (len(rows), nsrc))
    intros = get_intros([r["label_ja"] for r in rows if r.get("label_ja")])
    tally, flips, flagged = {}, [], []
    for r in rows:
        t = r.get("label_ja"); intro = intros.get(t, "")
        st, why, base = guard(t, intro, r.get("date_rule"), r.get("date_rule_src"))
        if (r.get("date_verified") or "") == "conflict" and st == "ok":
            st, why = "conflict", "本文の実日付と規則が不一致"
        v1 = guard_v1(t, intro, r.get("date_rule"))
        r["_g"], r["_why"] = st, why
        tally[st] = tally.get(st, 0) + 1
        if v1 != st: flips.append((r.get("qid"), t, v1, st, why))
        if st != "ok": flagged.append(r)
    print("  ガード内訳 v2 = " + str(tally))
    print("  ── v1 から判定が変わった行 ──")
    for q, t, a, b, why in flips:
        print("    %-11s %-20s %-8s -> %-8s %s" % (q, (t or "")[:18], a, b, why[:38]))
    print("  ── 除外候補 (v2) ──")
    for r in flagged[:40]:
        print("    %-11s %-20s %-8s %s" % (r.get("qid",""), (r.get("label_ja") or "")[:18],
                                           r["_g"], r["_why"][:46]))
    OUT["_rows"] = rows
    return {"tally": tally, "flips": len(flips), "src_rate": nsrc}

DOW = {"月":0,"火":1,"水":2,"木":3,"金":4,"土":5,"日":6}
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

def upcoming(rows, days):
    today = datetime.date.today(); end = today + datetime.timedelta(days=days)
    hits = []
    for r in rows:
        if r.get("_g") != "ok": continue
        for y in (today.year, today.year + 1):
            d = calc(r.get("date_rule"), y)
            if not d: continue
            a, b = d
            if a <= end and b >= today:
                hits.append((a, b, r)); break
    hits.sort(key=lambda x: x[0]); return hits

def s3():
    rows = OUT.get("_rows") or []
    h60 = upcoming(rows, 60); h7 = upcoming(rows, 7)
    print("  今週(7日) = %d 件 / 60日 = %d 件" % (len(h7), len(h60)))
    os.makedirs(OUTD, exist_ok=True)
    today = datetime.date.today()
    L = []
    L.append("# 日本の祭り カレンダー（自動生成）")
    L.append("")
    L.append("最終更新: " + today.isoformat() + " / 掲載 " + str(len(h60)) + " 件")
    L.append("")
    L.append("日付は各記事に記載された開催規則（例「7月第3土曜日」）から計算した推定日です。")
    L.append("実際の開催日は主催者の発表を必ずご確認ください。旧暦基準・過去の規則・")
    L.append("記事内の日付と矛盾する行は自動判定で除外しています。")
    L.append("")
    L.append("## 今週（" + today.isoformat() + " から7日以内）")
    L.append("")
    if not h7:
        L.append("該当なし")
    else:
        L.append("| 開催日 | 祭り | 都道府県 | 根拠となる規則 | 出典 |")
        L.append("|---|---|---|---|---|")
    for a, b, r in h7:
        d = a.strftime("%m月%d日") + ("〜" + b.strftime("%m月%d日") if b != a else "")
        t = r.get("label_ja") or ""
        L.append("| " + d + " | " + t + " | " + (r.get("prefecture") or "-") + " | "
                 + (r.get("date_rule") or "") + " | [jawiki](https://ja.wikipedia.org/wiki/" + t + ") |")
    L.append("")
    L.append("## 今後60日")
    L.append("")
    L.append("| 開催日 | 祭り | 都道府県 | 根拠となる規則 | 出典 |")
    L.append("|---|---|---|---|---|")
    for a, b, r in h60:
        d = a.strftime("%m月%d日") + ("〜" + b.strftime("%m月%d日") if b != a else "")
        t = r.get("label_ja") or ""
        L.append("| " + d + " | " + t + " | " + (r.get("prefecture") or "-") + " | "
                 + (r.get("date_rule") or "") + " | [jawiki](https://ja.wikipedia.org/wiki/" + t + ") |")
    md = os.path.join(OUTD, "calendar.md")
    open(md, "w", encoding="utf-8").write("\n".join(L) + "\n")
    js = os.path.join(OUTD, "calendar.json")
    json.dump({"generated": today.isoformat(),
               "items": [{"date_start": a.isoformat(), "date_end": b.isoformat(),
                          "qid": r.get("qid"), "label_ja": r.get("label_ja"),
                          "prefecture": r.get("prefecture"), "rule": r.get("date_rule"),
                          "confidence": r.get("date_verified")} for a, b, r in h60]},
              open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("  生成: " + md)
    print("  生成: " + js)
    print("  ── 今週分 ──")
    for a, b, r in h7:
        print("    %s  %-20s %s" % (a.isoformat(), (r.get("label_ja") or "")[:18], r.get("prefecture") or "-"))
    return {"w7": len(h7), "d60": len(h60), "md": md}

def s4():
    rows = OUT.get("_rows") or []
    if not APPLY:
        print("  保存 0 件 (APPLY=False)"); return {"saved": 0}
    c = cx()
    add = ensure_cols(c, "festivals", [("date_guard", "TEXT"), ("date_guard_note", "TEXT")])
    if add: print("  列追加: " + str(add))
    n = 0
    for r in rows:
        cur = c.execute("SELECT date_rule FROM festivals WHERE qid=?", (r.get("qid"),)).fetchone()
        if not cur or cur[0] != r.get("date_rule"): continue   # CAS
        c.execute("UPDATE festivals SET date_guard=?, date_guard_note=? WHERE qid=?",
                  (r["_g"], r["_why"], r.get("qid"))); n += 1
    c.commit(); c.close()
    print("  保存 %d 件" % n)
    try:
        import nxledger
        k = 0
        for r in rows:
            if r["_g"] in ("lunar", "past", "concept"):
                nxledger.put(tkey="DATEGUARD[" + str(r.get("qid")) + "]", verdict="reject",
                             note=r["_g"] + ": " + r["_why"],
                             url="https://ja.wikipedia.org/wiki/" + (r.get("label_ja") or ""))
                k += 1
        print("  台帳記録 %d 件" % k)
    except Exception as e:
        print("  台帳 skip (" + str(e) + ")")
    return {"saved": n}

def s5():
    t = str(OUT.get("s2", {}).get("tally", {}))
    c = OUT.get("s3", {}) or {}
    lines = [
        KEY,
        "- ガード v2: 判定軸を「同月を含む全文」から date_rule_src (規則の抽出元文) に固定。",
        "- v1 の誤検出: たてもん祭り/伏木曳山祭/城端曳山祭/越中八尾曳山祭 を past と誤判定。",
        "  原因は旧規則の記述や江戸時代の背景説明が同月文に同居したため。毎年・からは を現行signalに追加。",
        "- v2 判定内訳: " + t,
        "- 生成物: out/calendar.md, out/calendar.json (今週 " + str(c.get("w7")) + " 件 / 60日 " + str(c.get("d60")) + " 件)。",
        "- 掲載文面に「規則からの計算値・主催者発表を要確認」を明記し、各行に jawiki 出典を付与。",
        "- 旧暦基準 9 件は誤りではなく未対応。新暦換算は外部照会不要の決定論的計算のため次段候補。",
        "",
    ]
    os.makedirs(os.path.dirname(DOC), exist_ok=True)
    body = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in body:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    print("  key count = " + str(open(DOC, encoding="utf-8").read().count(KEY)))
    return {"doc": DOC}

def s0():
    os.makedirs(SNAP, exist_ok=True)
    p = os.path.join(SNAP, "db_" + TS + ".db"); shutil.copy2(DB, p); print("  " + p)
    return {"backup": p}

def _jsonable(o):
    if isinstance(o, dict): return {str(k): _jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_jsonable(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("selftest", s1); sec("scan", s2)
sec("page", s3); sec("save", s4); sec("doc", s5)
try:
    OUT.pop("_rows", None)
    p = os.path.join(SNAP, "step77_" + TS + ".json")
    json.dump(_jsonable(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step77_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
