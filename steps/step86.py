#!/usr/bin/env python3
# step86 : nxdate の戻り値キー修正 (raw/ctx) + 既存112件での再現検証 + 全件抽出
import os, sys, re, json, sqlite3, shutil, datetime, subprocess, time, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
SCR  = os.path.join(ROOT, "scripts")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [DATE_RULE_FULLSCAN_V2_20260811]"
APPLY = os.environ.get("NX_APPLY") == "1"
LIMIT = int(os.environ.get("NX_N", "0"))
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
sys.path.insert(0, SCR)
OUT = {"ts": TS, "apply": APPLY}

def sec(name, fn):
    try:
        r = fn(); OUT[name] = r; print("[OK] " + name); return r
    except Exception as e:
        OUT[name] = {"error": repr(e)}
        print("[NG] " + name + ": " + str(e)); traceback.print_exc(); return None

def s0():
    os.makedirs(SNAP, exist_ok=True)
    p = os.path.join(SNAP, "db_" + TS + ".db"); shutil.copy2(DB, p); print("  " + p)
    return {"backup": p}

def fmt_raw(d):
    return "毎年" + (d.get("raw") or "")

def fmt_desc(d):
    import nxdate
    try:
        s = nxdate.describe(d)
        return s if isinstance(s, str) and s else None
    except Exception:
        return None

def s1():
    """既存112件で答え合わせ。date_rule_src を再パースして date_rule を再現できるか。"""
    import nxdate
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = [dict(r) for r in c.execute(
        "SELECT qid,label_ja,date_rule,date_rule_src FROM festivals "
        "WHERE date_rule IS NOT NULL AND date_rule<>'' AND date_rule_src IS NOT NULL AND date_rule_src<>''")]
    c.close()
    print("  照合対象 = %d 件" % len(rows))
    score, miss = {"describe": 0, "raw": 0}, {"describe": [], "raw": []}
    nofind = 0
    for r in rows:
        d = nxdate.parse(r["date_rule_src"])
        if isinstance(d, (list, tuple)): d = d[0] if d else None
        if not isinstance(d, dict):
            nofind += 1; continue
        for k, f in (("describe", fmt_desc), ("raw", fmt_raw)):
            v = f(d)
            if v == r["date_rule"]: score[k] += 1
            elif len(miss[k]) < 3: miss[k].append((r["label_ja"], r["date_rule"], v))
    print("  再パース不可 = %d 件" % nofind)
    for k in ("describe", "raw"):
        print("    %-9s 一致 %3d/%d (%.0f%%)" % (k, score[k], len(rows), 100.0 * score[k] / max(1, len(rows))))
        for nm, want, got in miss[k]:
            print("      例 %-16s 期待 %-18s 実際 %s" % ((nm or "")[:14], want, got))
    best = max(score, key=lambda k: score[k])
    print("  採用 = %s (一致率 %.0f%%)" % (best, 100.0 * score[best] / max(1, len(rows))))
    assert score[best] >= len(rows) * 0.9, "再現率が低い。整形関数が特定できていない"
    print("  自己検証 OK (既存結果を再現できる整形関数を実データで特定)")
    OUT["_fmt"] = best
    return {"n": len(rows), "score": score, "best": best}

def s2():
    import nxwiki, nxdate, nxguard
    fmt = fmt_desc if OUT["_fmt"] == "describe" else fmt_raw
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = [dict(r) for r in c.execute(
        "SELECT qid,label_ja FROM festivals WHERE label_ja IS NOT NULL AND label_ja<>'' "
        "AND (date_rule IS NULL OR date_rule='') ORDER BY qid")]
    c.close()
    if LIMIT: rows = rows[:LIMIT]
    print("  未処理 = %d 件" % len(rows))
    got, noart, t0 = [], 0, time.time()
    for i in range(0, len(rows), 20):
        b = rows[i:i+20]
        try: ex = nxwiki.extracts([r["label_ja"] for r in b], intro=True)
        except TypeError: ex = nxwiki.extracts([r["label_ja"] for r in b], True)
        for r in b:
            intro = (ex or {}).get(r["label_ja"], "")
            if not intro: noart += 1; continue
            try: d = nxdate.parse(intro)
            except Exception: continue
            if isinstance(d, (list, tuple)): d = d[0] if d else None
            if not isinstance(d, dict): continue
            rule = fmt(d)
            if not rule: continue
            src = d.get("ctx") or ""
            g, why = nxguard.guard(r["label_ja"], intro, rule, src)
            got.append({"qid": r["qid"], "label_ja": r["label_ja"], "rule": rule,
                        "rule_json": json.dumps(d, ensure_ascii=False), "src": src,
                        "guard": g, "why": why, "type": d.get("type")})
        if (i // 20) % 10 == 0:
            print("    %4d/%d 経過 %.0f秒 抽出 %d" % (i, len(rows), time.time() - t0, len(got)))
    print("  抽出 = %d 件 / 走査 %d 件 (%.0f%%) 記事なし %d / 所要 %.0f 秒"
          % (len(got), len(rows), 100.0 * len(got) / max(1, len(rows)), noart, time.time() - t0))
    ty, gd = {}, {}
    for r in got:
        ty[r["type"]] = ty.get(r["type"], 0) + 1
        gd[r["guard"]] = gd.get(r["guard"], 0) + 1
    print("  種別 = " + str(ty))
    print("  ガード = " + str(gd) + "  掲載可 %d 件" % gd.get("ok", 0))
    print("  ── 抽出例 (先頭10) ──")
    for r in got[:10]:
        print("    %-11s %-20s %-18s %-8s %s" % (r["qid"], (r["label_ja"] or "")[:18],
              r["rule"], r["guard"], (r["src"] or "")[:26]))
    OUT["_got"] = got
    return {"scanned": len(rows), "found": len(got), "type": ty, "guard": gd, "noart": noart}

def s3():
    got = OUT.get("_got") or []
    if not APPLY:
        print("  保存 0 件 (APPLY=False)"); return {"saved": 0}
    c = sqlite3.connect(DB)
    n = 0
    for r in got:
        cur = c.execute("SELECT date_rule FROM festivals WHERE qid=?", (r["qid"],)).fetchone()
        if cur is None or (cur[0] or ""): continue     # CAS
        c.execute("UPDATE festivals SET date_rule=?,date_rule_json=?,date_rule_src=?,"
                  "date_verified=?,date_guard=?,date_guard_note=? WHERE qid=?",
                  (r["rule"], r["rule_json"], r["src"], "rule_only", r["guard"], r["why"], r["qid"]))
        n += 1
    c.commit()
    tot = c.execute("SELECT COUNT(*) FROM festivals WHERE date_rule IS NOT NULL AND date_rule<>''").fetchone()[0]
    okn = c.execute("SELECT COUNT(*) FROM festivals WHERE date_guard='ok'").fetchone()[0]
    unv = c.execute("SELECT COUNT(*) FROM festivals WHERE date_guard='ok' AND date_verified='rule_only'").fetchone()[0]
    c.close()
    print("  保存 %d 件 / 規則総数 %d / 掲載可 %d / 未検証 %d" % (n, tot, okn, unv))
    print("  → 未検証 %d 件が日次の作業対象 (1日5件で %d 日分)" % (unv, (unv + 4) // 5))
    return {"saved": n, "total": tot, "ok": okn, "unverified": unv}

def s4():
    import importlib, nxcal
    importlib.reload(nxcal)
    r = nxcal.render()
    print("  収録 %d 件 (従来 98) / 次に来る %d 件" % (r["annual"], r["next_n"]))
    rows = nxcal.load()
    mon = {}
    for x in rows:
        if x.get("date_guard") != "ok": continue
        d = nxcal.calc(x.get("date_rule"), 2026)
        if d: mon[d[0].month] = mon.get(d[0].month, 0) + 1
    for m in range(1, 13):
        print("    %2d月 %3d %s" % (m, mon.get(m, 0), "#" * min(46, mon.get(m, 0))))
    d, empty = datetime.date(2026, 1, 1), 0
    while d < datetime.date(2027, 1, 1):
        if not nxcal.upcoming(rows, 6, d): empty += 1
        d += datetime.timedelta(days=7)
    print("  7日窓が空になる週 = %d / 52 (従来 13)" % empty)
    return {"annual": r["annual"], "empty_weeks": empty}

def s5():
    a = OUT.get("s1", {}) or {}
    b = OUT.get("s2", {}) or {}
    d = OUT.get("s3", {}) or {}
    e = OUT.get("s4", {}) or {}
    lines = [
        KEY,
        "- step85 の抽出 0 件は nxdate.parse の戻り値キーの取り違え。規則は raw、抽出元文は ctx。",
        "  rule/text/label を探していたため全件スキップされていた。",
        "- 整形関数は決め打ちせず、既存 " + str(a.get("n")) + " 件の date_rule_src を再パースして",
        "  date_rule を再現できるかで実データから特定 (採用: " + str(a.get("best")) + ")。回帰試験を兼ねる。",
        "- 走査 " + str(b.get("scanned")) + " 件 → 抽出 " + str(b.get("found")) + " 件。ガード内訳: " + str(b.get("guard")),
        "- 収録 98 → " + str(e.get("annual")) + " 件 / 空白週 13 → " + str(e.get("empty_weeks")) + "。",
        "- 未検証 " + str(d.get("unverified")) + " 件 (date_verified='rule_only') が日次の作業対象。",
        "",
    ]
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    cur = open(DOC, encoding="utf-8").read()
    nl = cur.count("\n")
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), nl))
    if nl > 330: print("  ※ 次回、古い KEY ブロックを集約する")
    return {"lines": nl}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items() if not str(k).startswith("_")}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("reproduce", s1); sec("scan", s2)
sec("save", s3); sec("calendar", s4); sec("doc", s5)
try:
    for k in ("_fmt", "_got"): OUT.pop(k, None)
    p = os.path.join(SNAP, "step86_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step86_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)[:200000]); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
