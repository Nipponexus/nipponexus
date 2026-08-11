#!/usr/bin/env python3
# step84 : qid を tkey から復元 + 重複判定キーの修正 + 台帳 qid 列の補完
import os, sys, re, json, sqlite3, shutil, datetime, subprocess, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
SCR  = os.path.join(ROOT, "scripts")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [FIXLOG_V4_QID_20260811]"
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
    """qid 列の欠損状況を確認する。tkey から復元できる件数を数える。"""
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = [dict(r) for r in c.execute("SELECT rowid,tkey,qid FROM verdict_ledger")]
    null = [r for r in rows if not (r["qid"] or "").strip()]
    rec = [r for r in null if re.search(r"Q\d+", r["tkey"] or "")]
    print("  台帳 %d 行 / qid 空 %d 行 / うち tkey から復元可 %d 行" % (len(rows), len(null), len(rec)))
    for r in rec[:6]:
        print("    %-26s -> %s" % ((r["tkey"] or "")[:24], re.search(r"Q\d+", r["tkey"]).group(0)))
    if len(rec) < len(null):
        print("  復元不可 (プレースホルダ等):")
        for r in null:
            if not re.search(r"Q\d+", r["tkey"] or ""):
                print("    %s" % (r["tkey"] or "")[:40])
    if APPLY and rec:
        n = 0
        for r in rec:
            q = re.search(r"Q\d+", r["tkey"]).group(0)
            c.execute("UPDATE verdict_ledger SET qid=? WHERE rowid=? AND (qid IS NULL OR qid='')",
                      (q, r["rowid"])); n += 1
        c.commit()
        left = c.execute("SELECT COUNT(*) FROM verdict_ledger WHERE qid IS NULL OR qid=''").fetchone()[0]
        print("  qid 補完 %d 行 / 残り空 %d 行" % (n, left))
    else:
        print("  qid 補完 0 行 (APPLY=False)")
    c.close()
    return {"total": len(rows), "null": len(null), "recoverable": len(rec)}

PATCH_LOAD = '''
def _qid(tkey, col):
    """qid 列が空でも tkey から復元する。DATEGUARD 系は列が空のまま記録された。"""
    if (col or "").strip(): return col.strip()
    m = re.search(r"Q\\d+", tkey or "")
    return m.group(0) if m else None

def load():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    lab = {}
    for r in c.execute("SELECT qid,label_ja FROM festivals WHERE qid IS NOT NULL"):
        lab[r["qid"]] = r["label_ja"]
    out, seen = [], set()
    for r in c.execute("SELECT tkey,qid,ja,old,new,verdict,wd_label,wd_url,note,url "
                       "FROM verdict_ledger ORDER BY rowid"):
        k = kind_of(r["tkey"])
        if k not in PUBLIC: continue
        note = (r["note"] or "").strip()
        if note.startswith("LEGACY"): continue
        old, new = (r["old"] or "").strip(), (r["new"] or "").strip()
        if not note and not (old and new): continue
        # 重複判定は tkey を含める。qid が空でも別行が潰れない。
        key = (r["tkey"], old, new, note)
        if key in seen: continue
        seen.add(key)
        q = _qid(r["tkey"], r["qid"])
        name = lab.get(q) or r["ja"] or r["wd_label"] or q or "-"
        out.append({"kind": k, "qid": q, "name": name, "old": old, "new": new,
                    "verdict": r["verdict"], "note": note, "human": humanize(note),
                    "url": (r["url"] or r["wd_url"] or "").strip()})
    c.close(); return out
'''

def s2():
    p = os.path.join(SCR, "nxfix.py")
    src = open(p, encoding="utf-8").read()
    i = src.index("def load():")
    j = src.index("def _src(")
    new = src[:i] + PATCH_LOAD.strip() + "\n\n" + src[j:]
    assert new.count("def load():") == 1 and "def _qid(" in new
    open(p, "w", encoding="utf-8").write(new)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    import importlib, nxfix
    importlib.reload(nxfix)
    for tk, col, want in [("DATEGUARD[Q218646]", None, "Q218646"),
                          ("pref|Q11267368", "Q11267368", "Q11267368"),
                          ("canon|Gion Shrine", None, None)]:
        got = nxfix._qid(tk, col)
        print("    %-26s col=%-10s -> %s %s" % (tk, str(col), got, "OK" if got == want else "NG"))
        assert got == want, "qid 復元に失敗: " + tk
    rows = nxfix.load()
    kinds = {}
    for r in rows: kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    print("  公開対象 = %d 件 / 種別 = %s" % (len(rows), kinds))
    assert kinds.get("DATEGUARD", 0) == 14, "DATEGUARD が %d 件 (14 のはず)" % kinds.get("DATEGUARD", 0)
    dash = [r for r in rows if r["name"] == "-"]
    print("  対象名が '-' の行 = %d" % len(dash))
    assert not dash, "名称を解決できない行がある"
    print("  自己検証 OK (qid 復元 3件 / DATEGUARD 14件 / 名称欠落なし)")
    return {"n": len(rows), "kinds": kinds}

def s3():
    import nxfix
    r = nxfix.render()
    assert not r["jargon"], "内部語彙の残留: " + str(r["jargon"])
    print("  訂正 %d 件 (所在地 %d / 名称 %d) / 保留 %d 件" % (r["fixed"], r["loc"], r["name"], r["held"]))
    assert r["held"] == 15, "保留が %d 件 (14+1=15 のはず)" % r["held"]
    body = open(r["md"], encoding="utf-8").read()
    print("  out/corrections.md = %d 行 / %d 文字" % (body.count("\n"), len(body)))
    i = body.find("## 掲載を見送った")
    print("  ── 保留セクション全文 ──")
    for l in body[i:].split("\n")[:22]:
        print("    " + l[:150])
    return r

def s4():
    sysp = "/usr/bin/python3" if os.path.exists("/usr/bin/python3") else sys.executable
    r = subprocess.run([sysp, os.path.join(ROOT, "steps", "daily_cal.py")],
                       capture_output=True, text=True)
    print("  rc=%d %s" % (r.returncode, (r.stdout or r.stderr).strip()[:200]))
    assert r.returncode == 0, "daily runner failed"
    return {"rc": r.returncode}

def s5():
    r = OUT.get("s3", {}) or {}
    q = OUT.get("s1", {}) or {}
    lines = [
        KEY,
        "- step80 の台帳記録が tkey/verdict/note/url のみで qid 列を埋めておらず、DATEGUARD 14 行の qid が空だった。",
        "- そのため重複判定キー (種別,qid,old,new,note) で lunar 8 件などが同一視され 14→4 に潰れていた。",
        "  判定キーに tkey を含める形へ修正。併せて _qid() で tkey から Q番号を復元し名称も解決。",
        "- 台帳 qid 列を tkey から補完 (復元可 " + str(q.get("recoverable")) + " 行)。既存値は上書きしない。",
        "- 結果: 訂正 " + str(r.get("fixed")) + " 件 / 保留 " + str(r.get("held")) + " 件。",
        "- 教訓: 導出可能な値でも列に入れておかないと、後段の集合演算が静かに壊れる。",
        "",
    ]
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    cur = open(DOC, encoding="utf-8").read()
    nl = cur.count("\n")
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), nl))
    if nl > 350: print("  ※ 次回、古い KEY ブロックの集約を実施する")
    return {"lines": nl}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("qid", s1); sec("patch", s2)
sec("render", s3); sec("runner", s4); sec("doc", s5)
try:
    p = os.path.join(SNAP, "step84_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step84_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("APPLY=" + str(APPLY) + " snapshot=" + p)
