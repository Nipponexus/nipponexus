#!/usr/bin/env python3
# step78 : カレンダー生成を nxcal.py に分離 + 日次ランナー + concept 誤検出の review 降格
import os, sys, re, json, sqlite3, shutil, datetime, subprocess, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
SCR  = os.path.join(ROOT, "scripts")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [CAL_V1_DAILY_20260811]"
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

NXCAL = r'''
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

def render(today=None):
    today = today or datetime.date.today()
    rows = load()
    h7, h60 = upcoming(rows, 7, today), upcoming(rows, 60, today)
    L = ["# 日本の祭り カレンダー（自動生成）", "",
         "最終更新: " + today.isoformat() + " / 掲載 " + str(len(h60)) + " 件", "",
         "日付は各記事に記載された開催規則（例「7月第3土曜日」）から計算した推定日です。",
         "実際の開催日は主催者の発表を必ずご確認ください。旧暦基準・過去の規則・",
         "記事内の日付と矛盾する行は自動判定で除外しています。", "",
         "## 今週（" + today.isoformat() + " から7日以内）", ""]
    L += _tbl(h7) if h7 else ["該当なし"]
    L += ["", "## 今後60日", ""] + _tbl(h60)
    os.makedirs(OUTD, exist_ok=True)
    md = os.path.join(OUTD, "calendar.md")
    open(md, "w", encoding="utf-8").write("\n".join(L) + "\n")
    js = os.path.join(OUTD, "calendar.json")
    json.dump({"generated": today.isoformat(), "w7": len(h7), "d60": len(h60),
               "items": [{"date_start": a.isoformat(), "date_end": b.isoformat(),
                          "qid": r.get("qid"), "label_ja": r.get("label_ja"),
                          "prefecture": r.get("prefecture"), "rule": r.get("date_rule"),
                          "confidence": r.get("date_verified")} for a, b, r in h60]},
              open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return {"w7": len(h7), "d60": len(h60), "md": md, "json": js}

if __name__ == "__main__":
    print(json.dumps(render(), ensure_ascii=False))
'''

def s1():
    p = os.path.join(SCR, "nxcal.py")
    open(p, "w", encoding="utf-8").write(NXCAL.lstrip())
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    print("  " + p + " 書き出し + compile OK")
    return {"path": p}

def s2():
    import importlib, nxcal
    importlib.reload(nxcal)
    cases = [
        ("毎年8月16日", 2026, "2026-08-16", "2026-08-16"),
        ("毎年8月15日〜8月17日", 2026, "2026-08-15", "2026-08-17"),
        ("毎年9月第3月曜日", 2026, "2026-09-21", "2026-09-21"),
        ("毎年7月最終土曜日", 2026, "2026-07-25", "2026-07-25"),
        ("毎年2月第5日曜日", 2026, None, None),
    ]
    ok = True
    for rule, y, wa, wb in cases:
        d = nxcal.calc(rule, y)
        got = (d[0].isoformat(), d[1].isoformat()) if d else (None, None)
        good = got == (wa, wb); ok = ok and good
        print("    %-22s %s %s" % (rule, str(got), "OK" if good else "NG want=" + str((wa, wb))))
    assert ok, "nxcal calc self-test failed"
    rows = nxcal.load()
    for probe in ("2026-01-01", "2026-12-28", "2026-02-28"):
        d = datetime.date.fromisoformat(probe)
        print("    %s 起点 60日 = %d 件" % (probe, len(nxcal.upcoming(rows, 60, d))))
    print("  自己検証 OK (計算5件 / 年跨ぎ3点)")
    return {"ok": True}

def s3():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    tgt = [dict(r) for r in c.execute(
        "SELECT qid,label_ja,date_guard,date_guard_note FROM festivals "
        "WHERE date_guard='concept' AND date_guard_note LIKE '%body:%'")]
    for r in tgt:
        print("    降格候補: %-11s %s" % (r["qid"], r["label_ja"]))
    if APPLY and tgt:
        for r in tgt:
            c.execute("UPDATE festivals SET date_guard='review', date_guard_note=? "
                      "WHERE qid=? AND date_guard='concept'",
                      ("要人手確認(本文の総称表現による自動判定): " + (r["date_guard_note"] or ""), r["qid"]))
        c.commit()
        print("  %d 件を review に降格" % len(tgt))
    else:
        print("  降格 0 件 (APPLY=False)")
    c.close()
    return {"n": len(tgt)}

RUNNER = r'''#!/usr/bin/env python3
"""日次: カレンダー再生成のみ。DB を書き換えない。失敗しても既存 out/ は残る。"""
import os, sys, json, datetime, traceback
sys.path.insert(0, os.path.join(os.path.expanduser("~"), "nipponexus", "scripts"))
LOG = os.path.join(os.path.expanduser("~"), "nipponexus", "logs", "daily_cal.log")
os.makedirs(os.path.dirname(LOG), exist_ok=True)
try:
    import nxcal
    r = nxcal.render()
    msg = "OK " + json.dumps(r, ensure_ascii=False)
except Exception as e:
    msg = "NG " + repr(e) + "\n" + traceback.format_exc()
line = datetime.datetime.now().isoformat(timespec="seconds") + " " + msg
open(LOG, "a", encoding="utf-8").write(line + "\n")
print(line)
'''

def s4():
    p = os.path.join(ROOT, "steps", "daily_cal.py")
    open(p, "w", encoding="utf-8").write(RUNNER)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    r = subprocess.run([sys.executable, p], capture_output=True, text=True)
    print("  " + (r.stdout or r.stderr).strip()[:220])
    print("  cron 追加行 (未インストール / 内容を確認して手で入れること):")
    print("    35 4 * * * cd " + ROOT + " && " + sys.executable + " steps/daily_cal.py >> logs/cron.log 2>&1")
    return {"path": p, "rc": r.returncode}

def s5():
    md = os.path.join(ROOT, "out", "calendar.md")
    body = open(md, encoding="utf-8").read() if os.path.exists(md) else ""
    print("  out/calendar.md = %d 行 / %d 文字" % (body.count("\n"), len(body)))
    print("  ── 冒頭 14 行 ──")
    for l in body.split("\n")[:14]:
        print("    " + l)
    return {"chars": len(body)}

def s6():
    c = OUT.get("s4", {}) or {}
    lines = [
        KEY,
        "- カレンダー生成を scripts/nxcal.py に分離。DB のみ参照、外部照会ゼロ、日次実行の本体。",
        "- 掲載条件は date_guard='ok' のみ。lunar/past/conflict/concept/review は出さない。",
        "- steps/daily_cal.py は再生成のみで DB を書かない。失敗時も既存 out/ を保持。cron は 04:35 想定 (手動設定)。",
        "- 本文の総称表現による concept 判定 (豊橋鬼祭) は誤検出しやすいため review へ降格。",
        "- past は v2 で 0 件。規則の抽出元文に過去表現が入る例は実質なく、v1 の5件は全て誤検出だった。",
        "",
    ]
    os.makedirs(os.path.dirname(DOC), exist_ok=True)
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    cur = open(DOC, encoding="utf-8").read()
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), cur.count("\n")))
    if cur.count("\n") > 400:
        print("  ※ 04_addenda.md が 400 行超。古い KEY ブロックの集約を検討")
    return {"doc": DOC}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("nxcal", s1); sec("selftest", s2)
sec("demote", s3); sec("runner", s4); sec("preview", s5); sec("doc", s6)
try:
    p = os.path.join(SNAP, "step78_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step78_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
