# -*- coding: utf-8 -*-
# step60 : LEDGER_v3(upsert+列補完) / MIX_v1(文内表記混在検出) / hold3件の機械決着
import os, sys, re, json, shutil, sqlite3, subprocess, datetime, tempfile, importlib

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
SCR  = os.path.join(ROOT, "scripts")
SNAP = os.path.join(ROOT, "snapshots")
BK   = os.path.join(ROOT, "_backup")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
APPLY = os.environ.get("NX_APPLY") == "1"
for d in (SNAP, BK, os.path.join(ROOT, "steps")):
    os.makedirs(d, exist_ok=True)
sys.path.insert(0, SCR)
R = {}

def sec(n, f):
    try:
        R[n] = f()
        print("[OK] " + n)
    except Exception as e:
        R[n] = "ERR: %r" % (e,)
        print("[NG] %s : %r" % (n, e))

# ---------- §1 退避 ----------
def s1():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    src = sqlite3.connect(DB); dst = sqlite3.connect(b)
    src.backup(dst); dst.close(); src.close()
    out = {"db_snapshot": b, "bytes": os.path.getsize(b)}
    p = os.path.join(SCR, "nxledger.py")
    if os.path.exists(p):
        q = os.path.join(BK, "nxledger.py.bak_" + TS)
        shutil.copy2(p, q); out["nxledger_bak"] = q
    print(json.dumps(out, ensure_ascii=False))
    return out

# ---------- §2 verdict_ledger 欠落列 ----------
def s2():
    con = sqlite3.connect(DB)
    have = [r[1] for r in con.execute("pragma table_info('verdict_ledger')")]
    added = []
    for c in ("en", "note", "url"):
        if c not in have:
            con.execute("alter table verdict_ledger add column %s TEXT" % c)
            added.append(c)
    con.commit()
    now = [r[1] for r in con.execute("pragma table_info('verdict_ledger')")]
    con.close()
    print("  added=%s cols=%s" % (added, now))
    return {"added": added, "cols": now}

# ---------- §3 LEDGER_v3 ----------
LEDGER_V3 = r'''# -*- coding: utf-8 -*-
# LEDGER_v3 : verdict_ledger への書き込みは必ずこの関数経由。
# v2 からの変更 = (1) tkey 衝突は例外でなく upsert (2) 未知キーを黙って捨てない
import os, re as _re
_IDENT = _re.compile(r"^[a-z][a-z0-9_]{0,30}$")
ALLOW_EXT = {"tkey","qid","ja","en","old","new","verdict","wd_label","wd_url",
             "decided_at","src","note","url","evidence","excerpt","target_excerpt","status"}

def cols(con):
    return [r[1] for r in con.execute("pragma table_info('verdict_ledger')")]

def exists(con, tkey, new):
    c = cols(con)
    if "tkey" in c and "new" in c:
        return con.execute("select 1 from verdict_ledger where tkey=? and new=?",
                           (tkey, new)).fetchone() is not None
    return False

def ensure_cols(con, keys):
    """ALLOW_EXT の未知キーは列を足す。範囲外は例外。黙って捨てるのを禁止する。"""
    have = set(cols(con)); added = []
    for k in keys:
        if k in have:
            continue
        if k in ALLOW_EXT and _IDENT.match(k):
            con.execute("alter table verdict_ledger add column %s TEXT" % k)
            added.append(k); have.add(k)
        elif os.environ.get("NX_LEDGER_LAX") == "1":
            print("[LEDGER][WARN] dropped key: %s" % k)
        else:
            raise ValueError("unknown ledger key: %s (ALLOW_EXT に追加するか綴りを確認)" % k)
    return added

def put(con, **kv):
    """tkey 必須。既存 tkey は upsert。戻り値 = (使った列, 追加した列)"""
    if not kv.get("tkey"):
        raise ValueError("put() requires tkey")
    added = ensure_cols(con, list(kv))
    have = set(cols(con))
    keys = [k for k in kv if k in have]
    ph = ",".join("?" * len(keys))
    upd = [k for k in keys if k != "tkey"]
    tail = ("do update set " + ",".join("%s=excluded.%s" % (k, k) for k in upd)) if upd else "do nothing"
    con.execute("insert into verdict_ledger(%s) values(%s) on conflict(tkey) %s"
                % (",".join(keys), ph, tail), [kv[k] for k in keys])
    return keys, added
'''

MIX_V1 = r'''# -*- coding: utf-8 -*-
# MIX_v1 : 同一文内で「正式形の兄弟語」と「旧表記」が混在する箇所を検出する読み取り専用モジュール
import re
CANON = {
    "Todaiji": "T\u014ddai-ji", "Kofukuji": "K\u014dfuku-ji", "Sensoji": "Sens\u014d-ji",
    "Kasuga Taisha": "Kasuga-taisha", "Sumiyoshi Taisha": "Sumiyoshi-taisha",
    "Suwa Taisha": "Suwa-taisha", "Eiheiji": "Eihei-ji", "Yamadera": "Yama-dera",
}
_SPLIT = re.compile(r"(?<=[.!?])\s+")

def _pat(w):
    return re.compile(r"(?<![0-9A-Za-z-])" + re.escape(w) + r"(?![0-9A-Za-z])")

def sentences(t):
    return [s for s in _SPLIT.split(t or "") if s.strip()]

def scan_text(t):
    out = []
    for s in sentences(t):
        olds = [k for k in CANON if _pat(k).search(s)]
        news = [v for v in CANON.values() if _pat(v).search(s)]
        if olds and news:
            out.append({"sentence": s.strip()[:300], "old": olds, "new": news})
    return out

def scan_db(con, cols=("manual_content_en", "manual_content_ja")):
    rows = []
    q = "select qid,%s from festivals" % ",".join(cols)
    for r in con.execute(q):
        for i, c in enumerate(cols):
            for hit in scan_text(r[1 + i]):
                hit["qid"] = r[0]; hit["col"] = c; rows.append(hit)
    return rows
'''

def _write(path, body):
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    subprocess.run([sys.executable, "-m", "py_compile", path], check=True)
    nn = os.path.join(SCR, "nxname.py")
    if os.path.exists(nn):
        p = subprocess.run([sys.executable, nn, path], capture_output=True, text=True)
        print("  NAMECHECK %s : rc=%s %s" % (os.path.basename(path), p.returncode, p.stdout.strip()[:200]))
    return path

def s3():
    _write(os.path.join(SCR, "nxledger.py"), LEDGER_V3)
    _write(os.path.join(SCR, "nxmix.py"), MIX_V1)
    import nxledger, nxmix
    importlib.reload(nxledger); importlib.reload(nxmix)
    t = os.path.join(tempfile.mkdtemp(), "t.db")
    shutil.copy2(R["backup"]["db_snapshot"], t)
    c = sqlite3.connect(t)
    nxledger.put(c, tkey="canon|__selftest__", verdict="apply", note="n1", url="u1", en="E1")
    nxledger.put(c, tkey="canon|__selftest__", verdict="reject", note="n2", url="u2", en="E2")
    row = c.execute("select verdict,note,url,en from verdict_ledger where tkey='canon|__selftest__'").fetchall()
    c.close()
    assert len(row) == 1 and row[0] == ("reject", "n2", "u2", "E2"), row
    print("  upsert selftest OK -> %s" % (row[0],))
    return {"upsert": "OK", "row": row[0]}

# ---------- §4 混在スキャン ----------
def s4():
    import nxmix
    con = sqlite3.connect(DB)
    hits = nxmix.scan_db(con)
    con.close()
    for h in hits:
        print("  %s %s old=%s new=%s" % (h["qid"], h["col"], h["old"], h["new"]))
        print("    " + h["sentence"][:180])
    print("  文内混在 = %d 箇所" % len(hits))
    return hits

# ---------- §5 hold の判定 ----------
PREF_EN = {"北海":"Hokkaido","青森":"Aomori","岩手":"Iwate","宮城":"Miyagi","秋田":"Akita",
"山形":"Yamagata","福島":"Fukushima","茨城":"Ibaraki","栃木":"Tochigi","群馬":"Gunma",
"埼玉":"Saitama","千葉":"Chiba","東京":"Tokyo","神奈川":"Kanagawa","新潟":"Niigata",
"富山":"Toyama","石川":"Ishikawa","福井":"Fukui","山梨":"Yamanashi","長野":"Nagano",
"岐阜":"Gifu","静岡":"Shizuoka","愛知":"Aichi","三重":"Mie","滋賀":"Shiga","京都":"Kyoto",
"大阪":"Osaka","兵庫":"Hyogo","奈良":"Nara","和歌山":"Wakayama","鳥取":"Tottori",
"島根":"Shimane","岡山":"Okayama","広島":"Hiroshima","山口":"Yamaguchi","徳島":"Tokushima",
"香川":"Kagawa","愛媛":"Ehime","高知":"Kochi","福岡":"Fukuoka","佐賀":"Saga",
"長崎":"Nagasaki","熊本":"Kumamoto","大分":"Oita","宮崎":"Miyazaki","鹿児島":"Kagoshima","沖縄":"Okinawa"}
JA_TERM = {"Todaiji": "東大寺", "Kofukuji": "興福寺", "Yamadera": "山寺"}

def pref_en(p):
    if not p:
        return None
    return PREF_EN.get(re.sub(r"[都道府県]$", "", p))

def decide(nxmix, qid, term, ja_body, en_body, pref):
    ev = {"qid": qid, "term": term, "pref": pref, "new": nxmix.CANON.get(term)}
    text = en_body or ""
    m = nxmix._pat(term).search(text)
    if not m:
        ev.update(decision="skip", why="EN本文に出現なし"); return ev
    a, b = m.start(), m.end()
    win = text[max(0, a - 120): b + 120]
    ss = [s for s in nxmix.sentences(text) if nxmix._pat(term).search(s)]
    sent = ss[0].strip() if ss else win
    ev["sentence"] = sent[:300]
    ctx = text[max(0, a - 80): b + 80]
    if re.search(r"(district|area|neighbou?rhood|village|hamlet|quarter|town)", ctx, re.I) \
       and not re.search(r"(temple|shrine|Risshaku)", ctx, re.I):
        ev.update(decision="reject", why="PLACENAME_v1: 周辺80字が地名語のみで寺社語なし"); return ev
    sib = [v for k, v in nxmix.CANON.items() if k != term and nxmix._pat(v).search(sent)]
    if sib:
        ev.update(decision="apply", why="SIBLING_COHERENCE_v1: 同一文に正式形 " + ",".join(sib)); return ev
    m2 = re.search(r"([A-Z][\w\-]+)\s+of\s+" + re.escape(term) + r"\b", text)
    if m2:
        ev.update(decision="apply", why="REFERENCE_APPOSITIVE_v1: 『%s of %s』=人物の所属先" % (m2.group(1), term)); return ev
    pe = pref_en(pref)
    if re.search(r"\bof\s+" + re.escape(term) + r"\b", text) or re.search(re.escape(term) + r"['\u2019]s\b", text):
        if not (pe and re.search(re.escape(pe), win, re.I)):
            ev.update(decision="apply", why="REFERENCE_POSSESSIVE_v1: 参照構文かつ±120字に県名ENなし"); return ev
        ev.update(decision="hold", why="参照構文だが±120字に県名EN(%s)あり" % pe); return ev
    ev.update(decision="hold", why="規則未該当"); return ev

def qcols(con, tbl):
    return [r[1] for r in con.execute("pragma table_info('%s')" % tbl)]

def s5():
    import nxmix
    con = sqlite3.connect(DB)
    fc = qcols(con, "festivals")
    pc = qcols(con, "publish_queue")
    kq = "qid" if "qid" in pc else pc[0]
    kt = next((c for c in ("term", "word", "target", "old") if c in pc), pc[1])
    ks = next((c for c in ("status", "state") if c in pc), None)
    pf = "prefecture" if "prefecture" in fc else None
    rows = con.execute("select %s,%s from publish_queue where %s='hold'" % (kq, kt, ks)).fetchall() if ks \
        else con.execute("select %s,%s from publish_queue" % (kq, kt)).fetchall()
    out = []
    for qid, term in rows:
        sel = "select manual_content_ja, manual_content_en" + (", " + pf if pf else "") + " from festivals where qid=?"
        r = con.execute(sel, (qid,)).fetchone()
        if not r:
            out.append({"qid": qid, "term": term, "decision": "skip", "why": "festivals に該当なし"}); continue
        ev = decide(nxmix, qid, term, r[0], r[1], r[2] if pf else None)
        out.append(ev)
    con.close()
    for e in out:
        print("  %s %-10s -> %-6s %s" % (e["qid"], e["term"], e["decision"], e["why"]))
        if e.get("sentence"):
            print("     " + e["sentence"][:180])
    print("  queue cols=%s (key=%s term=%s status=%s)" % (pc, kq, kt, ks))
    return {"decisions": out, "qcols": [kq, kt, ks]}

# ---------- §6 反映 ----------
def dupw(t):
    return len(re.findall(r"\b(\w+)\s+\1\b", t or ""))

def s6():
    import nxledger, nxmix
    dec = R["decide"]["decisions"]
    kq, kt, ks = R["decide"]["qcols"]
    con = sqlite3.connect(DB)
    log = []
    for e in dec:
        term, new = e["term"], e.get("new")
        if e["decision"] == "apply" and new:
            changed = {}
            for col in ("manual_content_en", "manual_content_ja"):
                row = con.execute("select %s from festivals where qid=?" % col, (e["qid"],)).fetchone()
                t = row[0] if row else None
                if not t:
                    continue
                pat = nxmix._pat(term)
                n = len(pat.findall(t))
                if n == 0:
                    continue
                t2 = pat.sub(new, t)
                if dupw(t2) > dupw(t):
                    raise RuntimeError("DUPWORD guard: %s %s" % (e["qid"], col))
                if len(nxmix._pat(new).findall(t2)) < n:
                    raise RuntimeError("COUNT guard: %s %s" % (e["qid"], col))
                if APPLY:
                    cur = con.execute("update festivals set %s=? where qid=? and %s=?" % (col, col),
                                      (t2, e["qid"], t))
                    if cur.rowcount != 1:
                        raise RuntimeError("CAS failed: %s %s" % (e["qid"], col))
                changed[col] = n
            e["changed"] = changed
        if e["decision"] in ("apply", "reject") and APPLY:
            nxledger.put(con,
                tkey="canon|%s|%s" % (term, e["qid"]), qid=e["qid"],
                ja=JA_TERM.get(term, ""), old=term, new=(new or ""), en=(new or ""),
                verdict=e["decision"], decided_at=TS, src="step60/" + e["why"].split(":")[0],
                note=(e["why"] + " || " + e.get("sentence", ""))[:600],
                url=("https://en.wikipedia.org/wiki/" + (new or term).replace(" ", "_")))
            if ks:
                con.execute("update publish_queue set %s=? where %s=? and %s=?" % (ks, kq, kt),
                            (e["decision"], e["qid"], term))
        log.append({k: e[k] for k in ("qid", "term", "decision", "why") if k in e} | {"changed": e.get("changed")})
    if APPLY:
        con.commit()
    con.close()
    print("  APPLY=%s / %s" % (APPLY, json.dumps(log, ensure_ascii=False)))
    return log

# ---------- §7 回帰 ----------
def s7():
    p = subprocess.run([sys.executable, os.path.join(SCR, "nxcheck.py")],
                       cwd=ROOT, capture_output=True, text=True)
    print((p.stdout or "")[-1200:]); print((p.stderr or "")[-400:])
    if p.returncode != 0:
        print("  [!] 回帰NG。復旧は  cp %s %s" % (R["backup"]["db_snapshot"], DB))
    return {"rc": p.returncode}

# ---------- §8 追記 ----------
KEY = "## [LEDGER_V3_MIX_20260810]"
BLOCK = KEY + """
put() は未知キーを黙って捨てる仕様で、verdict_ledger に en/note/url 列自体が無かった。
根拠テキストと出典URLはこれまで一度も保存されていない。LEDGER_v3 で是正。
 * upsert: tkey 衝突は UNIQUE 制約エラーでなく on conflict do update。再実行が安全になる。
 * ensure_cols: ALLOW_EXT のキーは列を自動追加、範囲外は例外。NX_LEDGER_LAX=1 で警告に降格。
 * 黙って捨てる実装は「検証済みなのに証拠が無い」状態を作る。fail-loud を既定にする。
MIX_v1(scripts/nxmix.py): レコード単位の判定だけでは同一文内の表記混在を止められない。
 Q844110 は Tōdai-ji と Kofukuji が同じ文に並んだ。文単位の兄弟語照合を検出器として常設する。
hold の機械決着 3規則。PLACENAME_v1(周辺80字が地名語のみで寺社語なし=reject)、
 SIBLING_COHERENCE_v1(同一文に正式形の兄弟語=同一地域=apply)、
 REFERENCE_APPOSITIVE_v1(『人物名 of 対象』=所属先への参照=apply、県名近接は不問)。
 prefecture が NULL の記録は同名別実体テストが原理的に走らない。文脈規則へ落とすこと。
"""

def s8():
    import nxdoc
    try:
        nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError:
        nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    n = open(DOC, encoding="utf-8").read().count(KEY)
    print("  key count = %d" % n)
    return {"key_count": n}

sec("backup", s1)
sec("columns", s2)
sec("ledger_v3", s3)
sec("mixscan", s4)
sec("decide", s5)
sec("apply", s6)
sec("regress", s7)
sec("doc", s8)

j = os.path.join(SNAP, "step60_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60)
print("APPLY=%s  snapshot=%s" % (APPLY, j))
for k, v in R.items():
    print("  %-10s %s" % (k, (v if isinstance(v, str) else "ok")))
