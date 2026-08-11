#!/usr/bin/env python3
# step81 : 台帳の棚卸し + 訂正履歴ページ生成 (nxfix.py) + 日次ランナー統合
import os, sys, re, json, sqlite3, shutil, datetime, subprocess, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
SCR  = os.path.join(ROOT, "scripts")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [FIXLOG_V1_20260811]"
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

def s1():
    """台帳に何が入っているかを先に棚卸しする。公開前に中身を把握する。"""
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    cols = [r[1] for r in c.execute("PRAGMA table_info(verdict_ledger)")]
    print("  列: " + ",".join(cols))
    tot = c.execute("SELECT COUNT(*) FROM verdict_ledger").fetchone()[0]
    print("  総行数 = %d" % tot)
    print("  ── tkey 接頭辞別 ──")
    pref = {}
    for r in c.execute("SELECT tkey,verdict,note,url FROM verdict_ledger"):
        m = re.match(r"^([A-Z_]+)\[", r["tkey"] or "")
        k = m.group(1) if m else "(その他)"
        d = pref.setdefault(k, {"n": 0, "note": 0, "url": 0, "v": {}})
        d["n"] += 1
        if (r["note"] or "").strip(): d["note"] += 1
        if (r["url"] or "").strip(): d["url"] += 1
        d["v"][r["verdict"]] = d["v"].get(r["verdict"], 0) + 1
    for k, d in sorted(pref.items(), key=lambda x: -x[1]["n"]):
        print("    %-14s %3d件  note %3d  url %3d  %s" % (k, d["n"], d["note"], d["url"], d["v"]))
    print("  ── 公開候補になりうる行の例 (note あり先頭8) ──")
    for r in c.execute("SELECT tkey,verdict,note FROM verdict_ledger "
                       "WHERE note IS NOT NULL AND note<>'' LIMIT 8"):
        print("    %-26s %-8s %s" % ((r["tkey"] or "")[:24], r["verdict"], (r["note"] or "")[:50]))
    c.close()
    return {"total": tot, "prefix": {k: v["n"] for k, v in pref.items()}}

NXFIX = r'''
"""nxfix : 台帳から訂正履歴ページを生成する。DB のみ参照、外部照会ゼロ。"""
import os, re, json, sqlite3, datetime

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
OUTD = os.path.join(ROOT, "out")

# 公開してよい種別のみ。LEGACY や自作プレースホルダは出さない。
PUBLIC_PREFIX = ("PREF", "PLACENAME", "DATEGUARD", "CITYCHAIN")

def _q(tkey):
    m = re.search(r"(Q\d+)", tkey or "")
    return m.group(1) if m else None

def load():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    lab = {}
    for r in c.execute("SELECT qid,label_ja,prefecture FROM festivals WHERE qid IS NOT NULL"):
        lab[r["qid"]] = (r["label_ja"], r["prefecture"])
    rows = []
    for r in c.execute("SELECT tkey,verdict,note,url FROM verdict_ledger "
                       "WHERE note IS NOT NULL AND note<>'' ORDER BY rowid"):
        tk = r["tkey"] or ""
        m = re.match(r"^([A-Z_]+)\[", tk)
        pre = m.group(1) if m else ""
        if not any(pre.startswith(p) for p in PUBLIC_PREFIX): continue
        if (r["note"] or "").startswith("LEGACY"): continue
        q = _q(tk)
        name, pref = lab.get(q, (None, None))
        rows.append({"prefix": pre, "qid": q, "label_ja": name, "prefecture": pref,
                     "verdict": r["verdict"], "note": r["note"], "url": r["url"]})
    c.close(); return rows

def render(today=None):
    today = today or datetime.date.today()
    rows = load()
    kinds = {}
    for r in rows: kinds.setdefault(r["prefix"], []).append(r)
    TITLE = {"PREF": "所在地（都道府県）の訂正",
             "CITYCHAIN": "所在地（都道府県）の訂正",
             "PLACENAME": "地名の同名誤りの訂正",
             "DATEGUARD": "開催日の掲載保留（誤りを載せないための判断）"}
    L = ["# 訂正・検証の記録", "",
         "最終更新: " + today.isoformat() + " / 記録 " + str(len(rows)) + " 件", "",
         "当サイトは掲載前に、記事本文と Wikidata の二系統で内容を照合しています。",
         "その過程で見つかった誤りと、確証が得られず掲載を見送った項目を公開します。",
         "以下はいずれも自動照合で検出し、根拠を確認したうえで記録したものです。", ""]
    for pre in ("PREF", "CITYCHAIN", "PLACENAME", "DATEGUARD"):
        rs = kinds.get(pre)
        if not rs: continue
        L += ["## " + TITLE.get(pre, pre) + "（" + str(len(rs)) + "件）", "",
              "| 対象 | 判定 | 根拠 | 出典 |", "|---|---|---|---|"]
        for r in rs:
            nm = r["label_ja"] or (r["qid"] or "-")
            u = r["url"] or ""
            src = "[出典](" + u + ")" if u.startswith("http") else "-"
            note = (r["note"] or "").replace("|", "／").replace("\n", " ")
            L.append("| " + nm + " | " + (r["verdict"] or "") + " | " + note[:90] + " | " + src + " |")
        L.append("")
    os.makedirs(OUTD, exist_ok=True)
    md = os.path.join(OUTD, "corrections.md")
    open(md, "w", encoding="utf-8").write("\n".join(L) + "\n")
    js = os.path.join(OUTD, "corrections.json")
    json.dump({"generated": today.isoformat(), "count": len(rows), "items": rows},
              open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return {"count": len(rows), "kinds": {k: len(v) for k, v in kinds.items()}, "md": md}

if __name__ == "__main__":
    print(json.dumps(render(), ensure_ascii=False))
'''

def s2():
    p = os.path.join(SCR, "nxfix.py")
    open(p, "w", encoding="utf-8").write(NXFIX.lstrip())
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    import nxfix
    rows = nxfix.load()
    assert not any((r["note"] or "").startswith("LEGACY") for r in rows), "LEGACY が混入"
    assert all(r["note"] for r in rows), "note 空の行が混入"
    print("  公開対象 = %d 件 / LEGACY 混入なし / note 空なし" % len(rows))
    r = nxfix.render()
    print("  種別内訳 = " + str(r["kinds"]))
    print("  生成: " + r["md"])
    return r

def s3():
    md = os.path.join(ROOT, "out", "corrections.md")
    body = open(md, encoding="utf-8").read()
    print("  out/corrections.md = %d 行 / %d 文字" % (body.count("\n"), len(body)))
    print("  ── 冒頭 22 行 ──")
    for l in body.split("\n")[:22]:
        print("    " + l[:150])
    return {"chars": len(body)}

RUNNER = r'''#!/usr/bin/env python3
"""日次: カレンダーと訂正履歴を再生成。DB は書き換えない。片方失敗でも他方は生成する。"""
import os, sys, json, datetime, traceback
ROOT = os.path.join(os.path.expanduser("~"), "nipponexus")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
LOG = os.path.join(ROOT, "logs", "daily_cal.log")
os.makedirs(os.path.dirname(LOG), exist_ok=True)
res = {}
for name in ("nxcal", "nxfix"):
    try:
        m = __import__(name)
        res[name] = m.render()
    except Exception as e:
        res[name] = {"error": repr(e), "tb": traceback.format_exc()[-400:]}
ok = all("error" not in v for v in res.values())
line = (datetime.datetime.now().isoformat(timespec="seconds") + " "
        + ("OK " if ok else "NG ") + json.dumps(res, ensure_ascii=False))
open(LOG, "a", encoding="utf-8").write(line + "\n")
print(line)
sys.exit(0 if ok else 1)
'''

def s4():
    p = os.path.join(ROOT, "steps", "daily_cal.py")
    open(p, "w", encoding="utf-8").write(RUNNER)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    sysp = "/usr/bin/python3" if os.path.exists("/usr/bin/python3") else sys.executable
    r = subprocess.run([sysp, p], capture_output=True, text=True)
    print("  rc=%d  %s" % (r.returncode, (r.stdout or r.stderr).strip()[:240]))
    assert r.returncode == 0, "daily runner failed"
    print("  cron 行 (手で crontab -e に入れる):")
    print("    35 4 * * * cd " + ROOT + " && " + sysp + " steps/daily_cal.py >> logs/cron.log 2>&1")
    return {"rc": r.returncode}

def s5():
    n = OUT.get("s2", {}) or {}
    lines = [
        KEY,
        "- 第三段: 台帳から訂正履歴ページを生成する scripts/nxfix.py を追加 (DB のみ、外部照会ゼロ)。",
        "- 公開対象は PREF/CITYCHAIN/PLACENAME/DATEGUARD の " + str(n.get("count")) + " 件。LEGACY と note 空は除外。",
        "- 内訳: " + str(n.get("kinds")),
        "- daily_cal.py を nxcal+nxfix の両生成に統合。片方が落ちても他方は生成し、rc で判別する。",
        "- cron は system python3 (/usr/bin/python3) を使用し nexus_b2b/venv 依存を解消。",
        "",
    ]
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    cur = open(DOC, encoding="utf-8").read()
    nl = cur.count("\n")
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), nl))
    if nl > 380:
        print("  ※ 400行が近い。次回、古い KEY ブロックの集約を実施する")
    return {"lines": nl}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("audit", s1); sec("nxfix", s2)
sec("preview", s3); sec("runner", s4); sec("doc", s5)
try:
    p = os.path.join(SNAP, "step81_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step81_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
