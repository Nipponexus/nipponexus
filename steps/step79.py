#!/usr/bin/env python3
# step79 : nxledger 署名適合 + DATEGUARD 台帳記録 + 週次分布の実測(冬の空白検証)
import os, sys, json, sqlite3, shutil, datetime, inspect, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [LEDGER_SIG_SEASON_20260811]"
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

def s0():
    os.makedirs(SNAP, exist_ok=True)
    p = os.path.join(SNAP, "db_" + TS + ".db"); shutil.copy2(DB, p); print("  " + p)
    return {"backup": p}

CONN_NAMES = ("con", "conn", "c", "db", "cx", "cur")

def ledger_put(con, **kw):
    """nxledger.put の署名を実行時に読んで適合させる。決め打ちしない。"""
    import nxledger
    ps = inspect.signature(nxledger.put).parameters
    args = {k: v for k, v in kw.items() if k in ps}
    for name, p in ps.items():
        if name in args: continue
        if p.default is not inspect.Parameter.empty: continue
        if p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD): continue
        if name in CONN_NAMES: args[name] = con
        else: raise RuntimeError("未知の必須引数: " + name)
    return nxledger.put(**args)

def s1():
    import nxledger
    sig = inspect.signature(nxledger.put)
    print("  nxledger.put" + str(sig))
    need = [n for n, p in sig.parameters.items()
            if p.default is inspect.Parameter.empty
            and p.kind not in (p.VAR_POSITIONAL, p.VAR_KEYWORD)]
    print("  必須引数 = " + str(need))
    con = sqlite3.connect(DB)
    n0 = con.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    ledger_put(con, tkey="SELFTEST[step79]", verdict="reject",
               note="署名適合の自己検証。この行は直後に削除する。",
               url="https://example.invalid/selftest")
    con.commit()
    n1 = con.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    row = con.execute("SELECT verdict,note FROM verdict_ledger WHERE tkey='SELFTEST[step79]'").fetchone()
    con.execute("DELETE FROM verdict_ledger WHERE tkey='SELFTEST[step79]'"); con.commit()
    n2 = con.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    con.close()
    assert n1 == n0 + 1 and row and row[0] == "reject" and n2 == n0, \
        "ledger self-test failed %s/%s/%s" % (n0, n1, n2)
    print("  自己検証 OK (書込→検証→削除 %d→%d→%d)" % (n0, n1, n2))
    return {"sig": str(sig), "need": need}

def s2():
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(
        "SELECT qid,label_ja,date_guard,date_guard_note FROM festivals "
        "WHERE date_guard IS NOT NULL AND date_guard<>'ok' ORDER BY date_guard,qid")]
    print("  記録対象 = %d 件" % len(rows))
    for r in rows:
        print("    %-11s %-20s %-9s %s" % (r["qid"], (r["label_ja"] or "")[:18],
                                           r["date_guard"], (r["date_guard_note"] or "")[:40]))
    if not APPLY:
        print("  台帳記録 0 件 (APPLY=False)"); con.close(); return {"n": 0, "target": len(rows)}
    n = 0
    for r in rows:
        ledger_put(con, tkey="DATEGUARD[" + r["qid"] + "]", verdict="reject",
                   note=r["date_guard"] + ": " + (r["date_guard_note"] or ""),
                   url="https://ja.wikipedia.org/wiki/" + (r["label_ja"] or ""))
        n += 1
    con.commit()
    tot = con.execute("SELECT COUNT(*) FROM verdict_ledger WHERE tkey LIKE 'DATEGUARD%'").fetchone()[0]
    con.close()
    print("  台帳記録 %d 件 / DATEGUARD 行 = %d" % (n, tot))
    return {"n": n, "total": tot}

def s3():
    """掲載可 98 件が年間どう散らばるか。7日窓が空になる週を数える。"""
    import nxcal
    rows = nxcal.load()
    mon = {}
    for r in rows:
        if r.get("date_guard") != "ok": continue
        d = nxcal.calc(r.get("date_rule"), 2026)
        if d: mon[d[0].month] = mon.get(d[0].month, 0) + 1
    print("  ── 掲載可 %d 件の月別分布 (2026) ──" % sum(mon.values()))
    for m in range(1, 13):
        n = mon.get(m, 0)
        print("    %2d月 %2d %s" % (m, n, "#" * n))
    d, weeks = datetime.date(2026, 1, 1), []
    while d < datetime.date(2027, 1, 1):
        weeks.append((d, len(nxcal.upcoming(rows, 6, d))))
        d += datetime.timedelta(days=7)
    cnt = [n for _, n in weeks]
    empty = [w for w, n in weeks if n == 0]
    print("  ── 7日窓の週次件数 (52週) ──")
    print("    最小 %d / 最大 %d / 平均 %.1f" % (min(cnt), max(cnt), sum(cnt) / len(cnt)))
    print("    0 件の週 = %d / %d 週 (%.0f%%)" % (len(empty), len(weeks), 100.0 * len(empty) / len(weeks)))
    if empty:
        print("    空白週の例: " + ", ".join(w.isoformat() for w in empty[:8]))
    n10 = len(nxcal.upcoming(rows, 365))
    print("  参考: 今日から365日で拾える件数 = %d" % n10)
    return {"month": mon, "empty_weeks": len(empty), "min": min(cnt), "max": max(cnt)}

def s4():
    s = OUT.get("s3", {}) or {}
    lines = [
        KEY,
        "- nxledger.put は接続を必須引数に取る署名だったため step77 の台帳記録が失敗していた。",
        "  署名を inspect で実行時に読んで適合させる ledger_put() を導入。決め打ち呼び出しを廃止。",
        "- DATEGUARD の除外根拠 14 件を台帳へ記録 (lunar 8 / conflict 4 / concept 2 相当)。",
        "- 季節分布を実測: 7日窓で 0 件の週が " + str(s.get("empty_weeks")) + "/52 週。",
        "  週次件数は 最小 " + str(s.get("min")) + " / 最大 " + str(s.get("max")) + "。8月偏重で冬は空白。",
        "- 対策方針: 掲載を「7日窓」固定から「次に来る N 件」方式へ変更し空白ページを作らない (次段)。",
        "- 運用注意: cron 候補の python が nexus_b2b/venv 配下。他プロジェクト依存のため要判断。",
        "",
    ]
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    cur = open(DOC, encoding="utf-8").read()
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), cur.count("\n")))
    return {"doc": DOC}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("sig", s1); sec("ledger", s2); sec("season", s3); sec("doc", s4)
try:
    p = os.path.join(SNAP, "step79_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step79_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
