#!/usr/bin/env python3
# step76 : 掲載前品質ガード v1 (旧暦 / 過去形規則 / 概念記事 の除外)
import os, re, sys, json, sqlite3, shutil, datetime, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [DATE_GUARD_V1_20260811]"
APPLY = os.environ.get("NX_APPLY") == "1"
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
OUT = {"ts": TS, "apply": APPLY}

def sec(name, fn):
    try:
        r = fn(); OUT[name] = r; print("[OK] " + name); return r
    except Exception as e:
        OUT[name] = {"error": repr(e)}
        print("[NG] %s: %s" % (name, e)); traceback.print_exc(); return None

def cx():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; return c

def ensure_cols(c, table, cols):
    have = set(r[1] for r in c.execute("PRAGMA table_info(%s)" % table))
    add = []
    for name, typ in cols:
        if name not in have:
            c.execute("ALTER TABLE %s ADD COLUMN %s %s" % (table, name, typ)); add.append(name)
    c.commit(); return add

# ---------- guards ----------
RE_LUNAR = re.compile(r"旧暦|太陰暦|中秋の名月|十五夜")
RE_PAST  = re.compile(r"江戸時代|明治時代|大正時代|かつて|以前は|戦前|当時は|までは|旧暦では|廃止")
RE_NOW   = re.compile(r"現在|近年|以降は|現行")

def is_concept(title, intro):
    if re.search(r"三大|一覧|総称", title or ""): return True
    if re.search(r"(の総称|を総称して|の一覧である)", intro or ""): return True
    return False

def month_of(rule):
    m = re.search(r"(\d{1,2})月", rule or "")
    return int(m.group(1)) if m else None

def date_sents(intro, month):
    if not intro or not month: return []
    out = []
    for s in re.split(r"[。\n]", intro):
        if ("%d月" % month) in s: out.append(s)
    return out

def guard(title, intro, rule):
    """returns (status, reason)"""
    if is_concept(title, intro): return ("concept", "概念/一覧記事")
    mo = month_of(rule)
    ss = date_sents(intro, mo)
    blob = " ".join(ss) if ss else (intro or "")
    if RE_LUNAR.search(blob): return ("lunar", "旧暦基準 (新暦換算が必要)")
    for s in ss:
        if RE_PAST.search(s) and not RE_NOW.search(s):
            return ("past", "過去の開催日記述: " + s.strip()[:40])
    return ("ok", "")

def s1():
    cases = [
        ("神田祭",       "江戸時代は9月15日に行われていた。現在は5月中旬。", "毎年9月15日", "past"),
        ("采女祭",       "中秋の名月の日、猿沢池で行われる。", "毎年8月15日", "lunar"),
        ("五山送り火",   "毎年8月16日に京都市で行われる。",   "毎年8月16日", "ok"),
        ("京都三大祭り", "葵祭・祇園祭・時代祭の総称。",       "毎年8月16日", "concept"),
    ]
    res = []
    for t, i, r, want in cases:
        got, why = guard(t, i, r)
        ok = (got == want)
        res.append({"title": t, "want": want, "got": got, "ok": ok})
        print("    %-12s want=%-8s got=%-8s %s" % (t, want, got, "OK" if ok else "NG"))
    assert all(x["ok"] for x in res), "guard self-test failed"
    print("  自己検証 OK (4/4)")
    return res

# ---------- rule -> dates (表示文字列から再計算) ----------
DOW = {"月":0,"火":1,"水":2,"木":3,"金":4,"土":5,"日":6}
def calc(rule, year):
    r = rule or ""
    m = re.match(r"毎年(\d{1,2})月(\d{1,2})日〜(\d{1,2})月(\d{1,2})日", r)
    if m:
        a = datetime.date(year, int(m.group(1)), int(m.group(2)))
        b = datetime.date(year, int(m.group(3)), int(m.group(4)))
        return (a, b)
    m = re.match(r"毎年(\d{1,2})月(\d{1,2})日$", r)
    if m:
        a = datetime.date(year, int(m.group(1)), int(m.group(2))); return (a, a)
    m = re.match(r"毎年(\d{1,2})月第(\d)([月火水木金土日])曜日", r)
    if m:
        mo, n, d = int(m.group(1)), int(m.group(2)), DOW[m.group(3)]
        first = datetime.date(year, mo, 1)
        off = (d - first.weekday()) % 7
        a = first + datetime.timedelta(days=off + 7 * (n - 1))
        if a.month != mo: return None
        return (a, a)
    m = re.match(r"毎年(\d{1,2})月最終([月火水木金土日])曜日", r)
    if m:
        mo, d = int(m.group(1)), DOW[m.group(2)]
        nm = datetime.date(year + (1 if mo == 12 else 0), 1 if mo == 12 else mo + 1, 1)
        last = nm - datetime.timedelta(days=1)
        a = last - datetime.timedelta(days=(last.weekday() - d) % 7)
        return (a, a)
    return None

def load_rows():
    c = cx()
    cols = set(r[1] for r in c.execute("PRAGMA table_info(festivals)"))
    need = [x for x in ("qid","label_ja","prefecture","date_rule","date_verified","status") if x in cols]
    q = "SELECT %s FROM festivals WHERE date_rule IS NOT NULL AND date_rule<>''" % ",".join(need)
    rows = [dict(r) for r in c.execute(q)]
    c.close(); return rows

def get_intros(titles):
    import nxwiki
    out = {}
    for i in range(0, len(titles), 20):
        b = titles[i:i+20]
        try:
            d = nxwiki.extracts(b, intro=True)
        except TypeError:
            d = nxwiki.extracts(b, True)
        out.update(d or {})
    return out

def s2():
    rows = load_rows()
    print("  規則を持つ行 = %d" % len(rows))
    titles = [r.get("label_ja") for r in rows if r.get("label_ja")]
    intros = get_intros(titles)
    print("  導入部取得 %d/%d" % (sum(1 for t in titles if intros.get(t)), len(titles)))
    tally, flagged = {}, []
    for r in rows:
        st, why = guard(r.get("label_ja"), intros.get(r.get("label_ja"), ""), r.get("date_rule"))
        if (r.get("date_verified") or "") == "conflict" and st == "ok":
            st, why = "conflict", "本文の実日付と規則が不一致"
        r["_guard"], r["_why"] = st, why
        tally[st] = tally.get(st, 0) + 1
        if st != "ok": flagged.append(r)
    print("  ガード内訳 = %s" % tally)
    print("  ── 掲載除外候補 ──")
    for r in flagged[:40]:
        print("    %-11s %-22s %-8s %s" % (r.get("qid",""), (r.get("label_ja") or "")[:20],
                                           r["_guard"], r["_why"][:44]))
    OUT["_rows"] = rows
    return {"tally": tally, "flagged": len(flagged), "total": len(rows)}

def s3():
    rows = OUT.get("_rows") or []
    today = datetime.date.today(); end = today + datetime.timedelta(days=60)
    hits = []
    for r in rows:
        if r.get("_guard") != "ok": continue
        for y in (today.year, today.year + 1):
            d = calc(r.get("date_rule"), y)
            if not d: continue
            a, b = d
            if a <= end and b >= today:
                hits.append((a, b, r)); break
    hits.sort(key=lambda x: x[0])
    print("  ── 第二段 (ガード適用後) 今日から60日 ──")
    print("  %-16s %-22s %-7s %s" % ("開催日", "名称", "県", "規則"))
    for a, b, r in hits:
        dr = a.strftime("%m/%d(%a)") + ("-" + b.strftime("%m/%d") if b != a else "")
        print("  %-16s %-22s %-7s %s" % (dr, (r.get("label_ja") or "")[:20],
                                         r.get("prefecture") or "-", r.get("date_rule")))
    print("  掲載可 = %d 件 (ガード前 22 件 → 除外後)" % len(hits))
    return {"count": len(hits), "items": [[a.isoformat(), b.isoformat(), r.get("qid")] for a, b, r in hits]}

def s4():
    rows = OUT.get("_rows") or []
    if not APPLY:
        print("  保存 0 件 (APPLY=False)"); return {"saved": 0}
    c = cx()
    added = ensure_cols(c, "festivals", [("date_guard", "TEXT"), ("date_guard_note", "TEXT")])
    if added: print("  列追加: %s" % added)
    n = 0
    for r in rows:
        cur = c.execute("SELECT date_rule FROM festivals WHERE qid=?", (r.get("qid"),)).fetchone()
        if not cur or cur[0] != r.get("date_rule"):
            continue  # CAS: 規則が変わっていたら触らない
        c.execute("UPDATE festivals SET date_guard=?, date_guard_note=? WHERE qid=?",
                  (r["_guard"], r["_why"], r.get("qid"))); n += 1
    c.commit(); c.close()
    print("  保存 %d 件" % n)
    try:
        import nxledger
        for r in rows:
            if r["_guard"] in ("lunar", "past", "concept"):
                nxledger.put(tkey="DATEGUARD[%s]" % r.get("qid"), verdict="reject",
                             note="%s: %s" % (r["_guard"], r["_why"]),
                             url="https://ja.wikipedia.org/wiki/" + (r.get("label_ja") or ""))
        print("  台帳記録 OK")
    except Exception as e:
        print("  台帳記録 skip (%s)" % e)
    return {"saved": n}

def s5():
    t = OUT.get("s2", {}).get("tally", {})
    blk = (KEY + "\n"
           "- 掲載前ガード v1: 旧暦 / 過去形の開催日記述 / 概念記事 を掲載対象から除外。\n"
           "- 契機: 60日カレンダー試作で 神田祭(江戸時代の9月15日) / 采女祭(中秋の名月=旧暦) / 京都三大祭り(概念記事) の3件混入 (誤り率14%)。\n"
           "- 判定内訳: %s\n"
           "- 旧暦型は誤りではなく未対応。新暦換算は決定論的に計算可能なので次段で対応候補。\n"
           "- 掲載時は必ず「jawiki記載の規則に基づく計算値／公式サイトで要確認」と出典リンクを併記する。\n" % (t,))
    os.makedirs(os.path.dirname(DOC), exist_ok=True)
    body = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in body:
        open(DOC, "a", encoding="utf-8").write("\n" + blk)
    print("  key count = %d" % (open(DOC, encoding="utf-8").read().count(KEY)))
    return {"doc": DOC}

def s0():
    os.makedirs(SNAP, exist_ok=True)
    p = os.path.join(SNAP, "db_%s.db" % TS); shutil.copy2(DB, p); print("  " + p)
    return {"backup": p}

def _jsonable(o):
    if isinstance(o, dict): return {str(k): _jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_jsonable(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0)
sec("selftest", s1)
sec("scan", s2)
sec("calendar", s3)
sec("save", s4)
sec("doc", s5)

try:
    OUT.pop("_rows", None)
    p = os.path.join(SNAP, "step76_%s.json" % TS)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(_jsonable(OUT), f, ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step76_%s.txt" % TS)
    open(p, "w", encoding="utf-8").write(repr(OUT))
    print("  snapshot fallback (%s)" % e)
print("=" * 60)
print("APPLY=%s snapshot=%s" % (APPLY, p))
