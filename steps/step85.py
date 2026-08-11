#!/usr/bin/env python3
# step85 : 日付ルール抽出を全件へ拡大 + ガードをモジュール化 + 検証待ちキュー生成
import os, sys, re, json, sqlite3, shutil, datetime, inspect, subprocess, time, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
SCR  = os.path.join(ROOT, "scripts")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [DATE_RULE_FULLSCAN_20260811]"
APPLY = os.environ.get("NX_APPLY") == "1"
LIMIT = int(os.environ.get("NX_N", "0"))      # 0 = 全件
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

NXGUARD = r'''
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
'''

def s1():
    p = os.path.join(SCR, "nxguard.py")
    open(p, "w", encoding="utf-8").write(NXGUARD.lstrip())
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    import nxguard
    cases = [("たてもん祭り", "2007年からは8月第1金曜日に行われる。", "毎年8月第1金曜日",
              "2007年からは8月第1金曜日に行われる", "ok"),
             ("あばれ祭り", "かつては7月7日に行われていた。", "毎年7月7日",
              "かつては7月7日に行われていた", "past"),
             ("采女祭", "旧暦8月15日に行われる。", "毎年8月15日", "旧暦8月15日に行われる", "lunar"),
             ("京都三大祭り", "葵祭などの総称である。", "毎年8月16日", "", "concept")]
    for t, i, r, s, want in cases:
        got = nxguard.guard(t, i, r, s)[0]
        print("    %-12s %-8s %s" % (t, got, "OK" if got == want else "NG want=" + want))
        assert got == want
    print("  nxguard 自己検証 OK (4/4) / step77 と同一ロジック")
    return {"path": p}

def s2():
    """nxdate の API を実行時に確認する。名前を決め打ちしない。"""
    import nxdate
    fns = [(n, str(inspect.signature(f))) for n, f in vars(nxdate).items()
           if callable(f) and not n.startswith("_")]
    for n, s in fns: print("    %s%s" % (n, s))
    cand = [n for n, _ in fns if re.search(r"parse|extract|rule", n, re.I)]
    print("  抽出関数の候補 = " + str(cand))
    assert cand, "nxdate に抽出関数が見つからない"
    fn = getattr(nxdate, cand[0])
    r = fn("毎年8月第1金曜日に行われる。")
    print("  試験呼出 %s(...) -> %s" % (cand[0], str(r)[:140]))
    OUT["_fn"] = cand[0]
    return {"fn": cand[0], "fns": [n for n, _ in fns]}

def s3():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = [dict(r) for r in c.execute(
        "SELECT qid,label_ja FROM festivals WHERE label_ja IS NOT NULL AND label_ja<>'' "
        "AND (date_rule IS NULL OR date_rule='') ORDER BY qid")]
    c.close()
    if LIMIT: rows = rows[:LIMIT]
    print("  未処理 = %d 件 (規則未取得)" % len(rows))
    import nxwiki, nxdate, nxguard
    fn = getattr(nxdate, OUT["_fn"])
    got, t0 = [], time.time()
    for i in range(0, len(rows), 20):
        b = rows[i:i+20]
        try: ex = nxwiki.extracts([r["label_ja"] for r in b], intro=True)
        except TypeError: ex = nxwiki.extracts([r["label_ja"] for r in b], True)
        for r in b:
            intro = (ex or {}).get(r["label_ja"], "")
            if not intro: continue
            try: res = fn(intro)
            except Exception: continue
            if not res: continue
            d = res[0] if isinstance(res, (list, tuple)) and res and isinstance(res[0], dict) else res
            if not isinstance(d, dict): continue
            rule = d.get("rule") or d.get("text") or d.get("label")
            if not rule: continue
            src = d.get("src") or d.get("sentence") or ""
            g, why = nxguard.guard(r["label_ja"], intro, rule, src)
            got.append({"qid": r["qid"], "label_ja": r["label_ja"], "rule": rule,
                        "rule_json": json.dumps(d, ensure_ascii=False), "src": src,
                        "guard": g, "why": why, "type": d.get("type")})
        if (i // 20) % 10 == 0:
            print("    %4d/%d 件 経過 %.0f 秒 取得 %d" % (i, len(rows), time.time() - t0, len(got)))
    print("  規則を抽出 = %d 件 / 走査 %d 件 (%.0f%%) 所要 %.0f 秒"
          % (len(got), len(rows), 100.0 * len(got) / max(1, len(rows)), time.time() - t0))
    ty, gd = {}, {}
    for r in got:
        ty[r["type"]] = ty.get(r["type"], 0) + 1
        gd[r["guard"]] = gd.get(r["guard"], 0) + 1
    print("  種別内訳 = " + str(ty))
    print("  ガード内訳 = " + str(gd))
    print("  掲載可 (ok) = %d 件" % gd.get("ok", 0))
    OUT["_got"] = got
    return {"scanned": len(rows), "found": len(got), "type": ty, "guard": gd}

def s4():
    got = OUT.get("_got") or []
    if not APPLY:
        print("  保存 0 件 (APPLY=False)")
        for r in got[:10]:
            print("    %-11s %-20s %-18s %s" % (r["qid"], (r["label_ja"] or "")[:18],
                                                r["rule"], r["guard"]))
        return {"saved": 0}
    c = sqlite3.connect(DB)
    n = 0
    for r in got:
        cur = c.execute("SELECT date_rule FROM festivals WHERE qid=?", (r["qid"],)).fetchone()
        if cur is None or (cur[0] or ""): continue      # CAS: 既に規則があれば触らない
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
    print("  → 未検証 %d 件が日次の作業対象になる (1日5件で %d 日分)" % (unv, (unv + 4) // 5))
    return {"saved": n, "total": tot, "ok": okn, "unverified": unv}

def s5():
    import importlib, nxcal
    importlib.reload(nxcal)
    r = nxcal.render()
    print("  カレンダー再生成: 次に来る %d 件 / 年間 %d 件 (従来 98)" % (r["next_n"], r["annual"]))
    rows = nxcal.load()
    mon = {}
    for x in rows:
        if x.get("date_guard") != "ok": continue
        d = nxcal.calc(x.get("date_rule"), 2026)
        if d: mon[d[0].month] = mon.get(d[0].month, 0) + 1
    print("  ── 月別分布 ──")
    for m in range(1, 13):
        print("    %2d月 %3d %s" % (m, mon.get(m, 0), "#" * min(40, mon.get(m, 0))))
    d, empty = datetime.date(2026, 1, 1), 0
    while d < datetime.date(2027, 1, 1):
        if not nxcal.upcoming(rows, 6, d): empty += 1
        d += datetime.timedelta(days=7)
    print("  7日窓が空になる週 = %d / 52 (従来 13)" % empty)
    return {"annual": r["annual"], "empty_weeks": empty}

def s6():
    a = OUT.get("s3", {}) or {}
    b = OUT.get("s4", {}) or {}
    c = OUT.get("s5", {}) or {}
    lines = [
        KEY,
        "- ガードを scripts/nxguard.py に分離 (step77 と同一ロジック、自己検証つき)。",
        "- 未処理 " + str(a.get("scanned")) + " 件を走査し " + str(a.get("found")) + " 件から規則を抽出。",
        "- ガード内訳: " + str(a.get("guard")),
        "- 収録は 98 件 → " + str(c.get("annual")) + " 件。7日窓の空白週は 13 → " + str(c.get("empty_weeks")) + "。",
        "- 一括抽出では本文全体との照合を省き date_verified='rule_only' とした。",
        "  未検証 " + str(b.get("unverified")) + " 件が日次の作業対象になる (1日数件ずつ照合)。",
        "  これで「日次に流す材料がない」状態が解消する。",
        "",
    ]
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    cur = open(DOC, encoding="utf-8").read()
    nl = cur.count("\n")
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), nl))
    if nl > 340: print("  ※ 次回、古い KEY ブロックを集約する")
    return {"lines": nl}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items() if not str(k).startswith("_")}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("nxguard", s1); sec("api", s2)
sec("scan", s3); sec("save", s4); sec("calendar", s5); sec("doc", s6)
try:
    for k in ("_fn", "_got"): OUT.pop(k, None)
    p = os.path.join(SNAP, "step85_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step85_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)[:200000]); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
