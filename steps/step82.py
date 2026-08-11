#!/usr/bin/env python3
# step82 : tkey 形式(小文字|区切り)への対応 + 旧値→新値の表示 + 外向け文面化
import os, sys, re, json, sqlite3, shutil, datetime, subprocess, traceback

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
SNAP = os.path.join(ROOT, "snapshots")
SCR  = os.path.join(ROOT, "scripts")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
KEY  = "## [FIXLOG_V2_20260811]"
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
sys.path.insert(0, SCR)
OUT = {"ts": TS}

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
    """40 行の中身を全部見る。公開前に何を出すか目で確認する。"""
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    rows = [dict(r) for r in c.execute(
        "SELECT tkey,qid,ja,old,new,verdict,wd_label,wd_url,note,url,src FROM verdict_ledger "
        "WHERE tkey NOT LIKE 'DATEGUARD%' ORDER BY tkey")]
    print("  非DATEGUARD = %d 行" % len(rows))
    print("  %-26s %-16s %-6s->%-6s %s" % ("tkey", "verdict", "old", "new", "note有"))
    for r in rows:
        print("    %-26s %-16s %-6s->%-6s %s" % ((r["tkey"] or "")[:24], r["verdict"] or "",
              (r["old"] or "-")[:6], (r["new"] or "-")[:6], "有" if (r["note"] or "").strip() else "―"))
    n_on = sum(1 for r in rows if (r["old"] or "").strip() and (r["new"] or "").strip())
    n_nt = sum(1 for r in rows if (r["note"] or "").strip())
    print("  old/new 両方あり = %d / note あり = %d" % (n_on, n_nt))
    c.close()
    return {"rows": len(rows), "oldnew": n_on, "note": n_nt}

NXFIX = r'''
"""nxfix : 台帳から訂正履歴ページを生成する。DB のみ参照、外部照会ゼロ。"""
import os, re, json, sqlite3, datetime

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
OUTD = os.path.join(ROOT, "out")

PUBLIC = ("PREF", "CITYCHAIN", "PLACENAME", "CANON", "DATEGUARD")

def kind_of(tkey):
    """tkey は PREFIX[...] と prefix|... の両形式がある。両方に対応する。"""
    head = re.split(r"[\[|]", tkey or "", 1)[0]
    return head.strip().upper()

VERDICT_JA = {"apply": "訂正済み", "confirmed_wrong": "誤りを確認",
              "reject": "掲載見送り", "hold": "保留", "hold_geo": "保留（所在地）"}

HUMAN = [
    (r"^concept:",  "一覧・総称を扱う記事のため、個別の祭りの開催日としては掲載しない"),
    (r"^conflict:", "記事本文にある実際の日付と、記載の開催規則が一致しないため掲載しない"),
    (r"^lunar:",    "旧暦を基準とする日付のため新暦への換算が必要。未対応のため掲載しない"),
    (r"^review:",   "自動判定では確証が得られず、人による確認待ち"),
    (r"^PLACENAME_v2:", "同名の地名との取り違え。本文に本家所在地を示す語が一切なく、別地点と判断"),
    (r"^REFERENCE_APPOSITIVE_v1:", "人物の所属先を示す表記のため、正式表記に統一"),
    (r"^SIBLING_COHERENCE_v1:", "同一文中の他の寺社が正式表記のため、表記を統一"),
    (r"jawiki導入部\+Wikidata", "記事本文と Wikidata の двух系統で所在地を確認。旧値は祭りの名称から推測された誤り"),
    (r"CITYCHAIN", "記事本文から市区町村を特定し、Wikidata でその所属県を確認（祭りの名称は使用せず）"),
]

def humanize(note):
    t = (note or "").strip()
    for pat, msg in HUMAN:
        if re.search(pat, t): return msg
    return t

def load():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    lab = {}
    for r in c.execute("SELECT qid,label_ja FROM festivals WHERE qid IS NOT NULL"):
        lab[r["qid"]] = r["label_ja"]
    out = []
    for r in c.execute("SELECT tkey,qid,ja,old,new,verdict,wd_label,wd_url,note,url "
                       "FROM verdict_ledger ORDER BY rowid"):
        k = kind_of(r["tkey"])
        if k not in PUBLIC: continue
        note = (r["note"] or "").strip()
        if note.startswith("LEGACY"): continue
        has_on = bool((r["old"] or "").strip() and (r["new"] or "").strip())
        if not note and not has_on: continue      # 根拠が無い行は出さない
        q = r["qid"]
        name = lab.get(q) or r["ja"] or r["wd_label"] or q or "-"
        out.append({"kind": k, "qid": q, "name": name,
                    "old": (r["old"] or "").strip(), "new": (r["new"] or "").strip(),
                    "verdict": r["verdict"], "note": note, "human": humanize(note),
                    "url": (r["url"] or r["wd_url"] or "").strip()})
    c.close(); return out

def _src(u):
    return "[出典](" + u + ")" if (u or "").startswith("http") else "-"

def _tbl_fix(rs):
    L = ["| 対象 | 修正前 | 修正後 | 確認方法 | 出典 |", "|---|---|---|---|---|"]
    for r in rs:
        L.append("| " + r["name"] + " | " + (r["old"] or "-") + " | " + (r["new"] or "-")
                 + " | " + r["human"].replace("|", "／")[:80] + " | " + _src(r["url"]) + " |")
    return L

def _tbl_hold(rs):
    L = ["| 対象 | 判定 | 理由 | 出典 |", "|---|---|---|---|"]
    for r in rs:
        L.append("| " + r["name"] + " | " + VERDICT_JA.get(r["verdict"], r["verdict"] or "")
                 + " | " + r["human"].replace("|", "／")[:80] + " | " + _src(r["url"]) + " |")
    return L

def render(today=None):
    today = today or datetime.date.today()
    rows = load()
    fixed = [r for r in rows if r["verdict"] in ("apply", "confirmed_wrong")]
    held  = [r for r in rows if r["verdict"] not in ("apply", "confirmed_wrong")]
    loc   = [r for r in fixed if r["kind"] in ("PREF", "CITYCHAIN")]
    nam   = [r for r in fixed if r["kind"] in ("CANON", "PLACENAME")]
    etc   = [r for r in fixed if r not in loc and r not in nam]
    L = ["# 訂正・検証の記録", "",
         "最終更新: " + today.isoformat() + " / 訂正 " + str(len(fixed)) + " 件・保留 " + str(len(held)) + " 件", "",
         "当サイトは掲載前に、記事本文と Wikidata という二つの経路で内容を照合しています。",
         "一方だけで裏が取れた場合は採用せず、保留として記録します。",
         "以下は、その照合で見つかった誤りと、確証が得られず掲載を見送った項目です。", ""]
    if loc:
        L += ["## 所在地（都道府県）の訂正（" + str(len(loc)) + "件）", "",
              "祭りの名称から所在地が推測され、実際とは別の県が記録されていたものです。", ""] + _tbl_fix(loc) + [""]
    if nam:
        L += ["## 名称・表記の訂正（" + str(len(nam)) + "件）", ""] + _tbl_fix(nam) + [""]
    if etc:
        L += ["## その他の訂正（" + str(len(etc)) + "件）", ""] + _tbl_fix(etc) + [""]
    if held:
        L += ["## 掲載を見送った項目（" + str(len(held)) + "件）", "",
              "誤った情報を載せないため、確証が得られないものは公開していません。", ""] + _tbl_hold(held) + [""]
    os.makedirs(OUTD, exist_ok=True)
    md = os.path.join(OUTD, "corrections.md")
    open(md, "w", encoding="utf-8").write("\n".join(L) + "\n")
    js = os.path.join(OUTD, "corrections.json")
    json.dump({"generated": today.isoformat(), "fixed": len(fixed), "held": len(held),
               "items": rows}, open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return {"fixed": len(fixed), "held": len(held), "loc": len(loc), "name": len(nam), "md": md}

if __name__ == "__main__":
    print(json.dumps(render(), ensure_ascii=False))
'''

def s2():
    p = os.path.join(SCR, "nxfix.py")
    open(p, "w", encoding="utf-8").write(NXFIX.lstrip().replace("двух", "二"))
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    import importlib, nxfix
    importlib.reload(nxfix)
    cases = [("pref|Q11267368", "PREF"), ("DATEGUARD[Q218646]", "DATEGUARD"),
             ("canon|Todaiji|Q3461576", "CANON"), ("citychain|Q1", "CITYCHAIN")]
    for tk, want in cases:
        got = nxfix.kind_of(tk)
        print("    %-26s -> %-10s %s" % (tk, got, "OK" if got == want else "NG want=" + want))
    assert all(nxfix.kind_of(tk) == w for tk, w in cases), "kind_of self-test failed"
    rows = nxfix.load()
    kinds = {}
    for r in rows: kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    print("  公開対象 = %d 件 / 種別 = %s" % (len(rows), kinds))
    assert kinds.get("PREF", 0) > 0, "PREF が 0。tkey 解析がまだ合っていない"
    assert len(rows) >= 30, "公開対象が少なすぎる: %d" % len(rows)
    print("  自己検証 OK (両形式の tkey を解析 / PREF を取得)")
    return {"n": len(rows), "kinds": kinds}

def s3():
    import nxfix
    r = nxfix.render()
    md = r["md"]; body = open(md, encoding="utf-8").read()
    jargon = ["PLACENAME_v2", "SIBLING_COHERENCE", "REFERENCE_APPOSITIVE",
              "concept:", "conflict:", "lunar:", "P131", "jawiki導入部"]
    left = [j for j in jargon if j in body]
    print("  内部語彙の残留 = " + (str(left) if left else "なし"))
    assert not left, "外向け文面に内部語彙が残っている: " + str(left)
    print("  訂正 %d 件 (所在地 %d / 名称 %d) / 保留 %d 件" % (r["fixed"], r["loc"], r["name"], r["held"]))
    print("  out/corrections.md = %d 行 / %d 文字" % (body.count("\n"), len(body)))
    print("  ── 冒頭 24 行 ──")
    for l in body.split("\n")[:24]:
        print("    " + l[:150])
    return r

def s4():
    sysp = "/usr/bin/python3" if os.path.exists("/usr/bin/python3") else sys.executable
    r = subprocess.run([sysp, os.path.join(ROOT, "steps", "daily_cal.py")],
                       capture_output=True, text=True)
    print("  rc=%d %s" % (r.returncode, (r.stdout or r.stderr).strip()[:220]))
    assert r.returncode == 0, "daily runner failed"
    return {"rc": r.returncode}

def s5():
    r = OUT.get("s3", {}) or {}
    lines = [
        KEY,
        "- tkey は PREFIX[...] と prefix|... の二形式が混在。前者しか解析できず 40 行を取りこぼしていた。",
        "  kind_of() で [ と | の両方を区切りとして扱い解決。両形式を自己検証で固定。",
        "- 台帳は old/new/qid/wd_url 列を持つことが判明。旧値→新値を直接表示できる。",
        "- 訂正 " + str(r.get("fixed")) + " 件 (所在地 " + str(r.get("loc")) + " / 名称 " + str(r.get("name"))
          + ") と保留 " + str(r.get("held")) + " 件を分けて掲載。",
        "- 内部語彙 (規則名・conflict 等) を外向け日本語に変換。残留を自己検証で禁止。",
        "- 根拠のない行 (note も old/new も無い) は公開しない。",
        "",
    ]
    cur = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else ""
    if KEY not in cur:
        open(DOC, "a", encoding="utf-8").write("\n" + "\n".join(lines))
    cur = open(DOC, encoding="utf-8").read()
    print("  key count = %d / DOC = %d 行" % (cur.count(KEY), cur.count("\n")))
    return {"lines": cur.count("\n")}

def _j(o):
    if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [_j(v) for v in o]
    if isinstance(o, (str, int, float, bool)) or o is None: return o
    return repr(o)

sec("backup", s0); sec("audit", s1); sec("nxfix", s2)
sec("render", s3); sec("runner", s4); sec("doc", s5)
try:
    p = os.path.join(SNAP, "step82_" + TS + ".json")
    json.dump(_j(OUT), open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
except Exception as e:
    p = os.path.join(SNAP, "step82_" + TS + ".txt")
    open(p, "w", encoding="utf-8").write(repr(OUT)); print("  snapshot fallback (" + str(e) + ")")
print("=" * 60)
print("snapshot=" + p)
