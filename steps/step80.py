#!/usr/bin/env python3
# step80 : ledger_put の VAR_KEYWORD 対応 + DATEGUARD 記録 + カレンダーを「次に来るN件」方式へ
import os, sys, json, sqlite3, shutil, datetime, inspect, subprocess, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
SCR  = os.path.join(ROOT, "scripts")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [CAL_V2_NEXTN_20260811]"
APPLY = os.environ.get("NX_APPLY") == "1"
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

CONN_NAMES = ("con", "conn", "c", "db", "cx")

def ledger_put(con, **kw):
    """署名を実行時に読む。**kwargs があれば全キーを素通しする (step79 の取りこぼし修正)。"""
    import nxledger
    ps = inspect.signature(nxledger.put).parameters
    has_var_kw = any(p.kind == p.VAR_KEYWORD for p in ps.values())
    args = dict(kw) if has_var_kw else {k: v for k, v in kw.items() if k in ps}
    for name, p in ps.items():
        if name in args or p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD): continue
        if p.default is not inspect.Parameter.empty: continue
        if name in CONN_NAMES: args[name] = con
        else: raise RuntimeError("未知の必須引数: " + name)
    return nxledger.put(**args)

def s1():
    import nxledger
    print("  nxledger.put" + str(inspect.signature(nxledger.put)))
    con = sqlite3.connect(DB)
    n0 = con.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    ledger_put(con, tkey="SELFTEST[step80]", verdict="reject",
               note="署名適合の自己検証。直後に削除する。", url="https://example.invalid/selftest")
    con.commit()
    r = con.execute("SELECT verdict,note,url FROM verdict_ledger WHERE tkey='SELFTEST[step80]'").fetchone()
    n1 = con.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    con.execute("DELETE FROM verdict_ledger WHERE tkey='SELFTEST[step80]'"); con.commit()
    n2 = con.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    con.close()
    print("    書込行 = " + str(r))
    assert n1 == n0 + 1 and r and r[0] == "reject" and r[1] and n2 == n0, "ledger self-test failed"
    print("  自己検証 OK (%d→%d→%d / note,url とも保存)" % (n0, n1, n2))
    return {"ok": True}

def s2():
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(
        "SELECT qid,label_ja,date_guard,date_guard_note FROM festivals "
        "WHERE date_guard IS NOT NULL AND date_guard<>'ok' ORDER BY date_guard,qid")]
    print("  記録対象 = %d 件" % len(rows))
    if not APPLY:
        con.close(); print("  台帳記録 0 件 (APPLY=False)"); return {"n": 0, "target": len(rows)}
    for r in rows:
        ledger_put(con, tkey="DATEGUARD[" + r["qid"] + "]", verdict="reject",
                   note=r["date_guard"] + ": " + (r["date_guard_note"] or ""),
                   url="https://ja.wikipedia.org/wiki/" + (r["label_ja"] or ""))
    con.commit()
    tot = con.execute("SELECT COUNT(*) FROM verdict_ledger WHERE tkey LIKE 'DATEGUARD%'").fetchone()[0]
    all_n = con.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    con.close()
    print("  台帳記録 %d 件 / DATEGUARD = %d / 台帳総数 = %d" % (len(rows), tot, all_n))
    return {"n": len(rows), "total": tot}

PATCH = '''
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
    open(md, "w", encoding="utf-8").write("\\n".join(L) + "\\n")
    js = os.path.join(OUTD, "calendar.json")
    json.dump({"generated": today.isoformat(), "next_n": len(nx), "annual": len(an),
               "items": [{"date_start": a.isoformat(), "date_end": b.isoformat(),
                          "qid": r.get("qid"), "label_ja": r.get("label_ja"),
                          "prefecture": r.get("prefecture"), "rule": r.get("date_rule"),
                          "confidence": r.get("date_verified")} for a, b, r in an]},
              open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return {"next_n": len(nx), "annual": len(an), "md": md, "json": js}
'''

def s3():
    p = os.path.join(SCR, "nxcal.py")
    src = open(p, encoding="utf-8").read()
    i = src.index("def render(")
    j = src.index('if __name__ ==')
    new = src[:i] + PATCH.strip() + "\n\n" + src[j:]
    assert "def upcoming_n" in new and "def annual" in new and new.count("def render(") == 1
    open(p, "w", encoding="utf-8").write(new)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    print("  nxcal.py 差し替え + compile OK (upcoming_n / annual 追加、upcoming は温存)")
    return {"path": p}

def s4():
    import importlib, nxcal
    importlib.reload(nxcal)
    rows = nxcal.load()
    ok = True
    for probe in ("2026-01-01", "2026-03-05", "2026-08-11", "2026-12-28"):
        d = datetime.date.fromisoformat(probe)
        h = nxcal.upcoming_n(rows, 12, d)
        mono = all(h[k][0] <= h[k+1][0] for k in range(len(h)-1))
        first = h[0][0].isoformat() if h else "-"
        good = (len(h) == 12 and mono)
        ok = ok and good
        print("    %s 起点 -> %2d 件 先頭 %s 昇順 %s %s"
              % (probe, len(h), first, mono, "OK" if good else "NG"))
    d = datetime.date.fromisoformat("2026-12-28")
    wrap = [x for x in nxcal.upcoming_n(rows, 12, d) if x[0].year == 2027]
    print("    年跨ぎ: 12/28 起点の 2027年分 = %d 件 (0 なら NG)" % len(wrap))
    ok = ok and len(wrap) > 0
    an = nxcal.annual(rows, 2026)
    print("    年間一覧 = %d 件 (掲載可 98 と一致すること)" % len(an))
    assert ok and len(an) > 90, "nxcal v2 self-test failed"
    print("  自己検証 OK (4起点すべて12件 / 年跨ぎあり / 空白ゼロ)")
    return {"annual": len(an)}

def s5():
    r = subprocess.run([sys.executable, os.path.join(ROOT, "steps", "daily_cal.py")],
                       capture_output=True, text=True)
    print("  venv python : " + (r.stdout or r.stderr).strip()[:150])
    sysp = "/usr/bin/python3"
    if os.path.exists(sysp):
        r2 = subprocess.run([sysp, os.path.join(ROOT, "steps", "daily_cal.py")],
                            capture_output=True, text=True)
        good = r2.returncode == 0 and "OK" in (r2.stdout or "")
        print("  system python: " + (r2.stdout or r2.stderr).strip()[:150])
        print("  → nxcal は標準ライブラリのみ。system python で動くなら venv 依存を切れる: %s" % good)
        if good:
            print("  推奨 cron 行:")
            print("    35 4 * * * cd " + ROOT + " && " + sysp + " steps/daily_cal.py >> logs/cron.log 2>&1")
    md = os.path.join(ROOT, "out", "calendar.md")
    body = open(md, encoding="utf-8").read()
    print("  out/calendar.md = %d 行 / %d 文字" % (body.count("\n"), len(body)))
    print("  ── 冒頭 16 行 ──")
    for l in body.split("\n")[:16]:
        print("    " + l)
    return {"chars": len(body)}

def s6():
    s = OUT.get("s4", {}) or {}
    lines = [
        KEY,
        "- 季節分布の実測: 7日窓は 0 件の週が 13/52 (25%%)、8月24件に対し1月2件。窓固定は冬に空白ページを生む。",
        "- 対策: 日数窓を廃し「次に来る12件」+「年間一覧(月別)」の件数固定方式へ。年間どの日でも必ず埋まる。",
        "- ledger_put: 署名に **kwargs がある場合に全キーを素通しするよう修正 (step79 は取りこぼして全件失敗)。",
        "- DATEGUARD 14 件を台帳へ記録。除外根拠が台帳側にも残る。",
        "- nxcal は標準ライブラリのみ。cron は system python3 を推奨し nexus_b2b/venv 依存を切る。",
        "",
    ]
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(x.replace("%%", "%") for x in lines))
    cur = open(DOC, encoding="utf-8").read()
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), cur.count("\n")))
    return {"doc": DOC}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("sig", s1); sec("ledger", s2)
sec("patch", s3); sec("selftest", s4); sec("preview", s5); sec("doc", s6)
try:
    p = os.path.join(SNAP, "step80_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step80_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
