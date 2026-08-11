# -*- coding: utf-8 -*-
# step63 : 判定連鎖の常設化(nxdecide) / 全件再スキャンと publish_queue 投入 / 台帳 LEGACY 印付け
import os, sys, re, json, sqlite3, subprocess, datetime, collections
HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
SCR  = os.path.join(ROOT, "scripts")
SNAP = os.path.join(ROOT, "snapshots")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC  = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
APPLY = os.environ.get("NX_APPLY") == "1"
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try:
        R[n] = f(); print("[OK] " + n)
    except Exception as e:
        R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

def s1():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    a = sqlite3.connect(DB); c = sqlite3.connect(b); a.backup(c); c.close(); a.close()
    print("  " + b); return {"db_snapshot": b}

DECIDE = r'''# -*- coding: utf-8 -*-
# DECIDE_v1 : 旧表記1件の処遇を決める唯一の入口。判定順序をここに固定する。
# 順序 = SIBLING_COHERENCE -> REFERENCE_APPOSITIVE -> PLACENAME_v2 -> hold
# 各段は (verdict, why) を返し、最初に確定した段で打ち切る。順序を変える時はここだけ直す。
import re
import nxmix, nxrules

ORDER = ["SIBLING_COHERENCE_v1", "REFERENCE_APPOSITIVE_v1", "PLACENAME_v2"]

def _sentences_with(term, en):
    return [s.strip() for s in nxmix.sentences(en or "") if nxrules._pat(term).search(s)]

def sibling(term, en, ja):
    for s in _sentences_with(term, en):
        sib = [v for k, v in nxmix.CANON.items() if k != term and nxrules._pat(v).search(s)]
        if sib:
            return "apply", "SIBLING_COHERENCE_v1: 同一文に正式形 " + ",".join(sib)
    return None, None

def appositive(term, en, ja):
    m = re.search(r"([A-Z][\w\-]+)\s+of\s+" + re.escape(term) + r"(?![0-9A-Za-z])", en or "")
    if m:
        return "apply", "REFERENCE_APPOSITIVE_v1: 『%s of %s』=人物・物の所属先" % (m.group(1), term)
    return None, None

def placename(term, en, ja):
    v, why, sig = nxrules.judge(term, en or "", ja or "")
    return (("reject", why) if v == "reject" else (None, None))

STAGES = {"SIBLING_COHERENCE_v1": sibling,
          "REFERENCE_APPOSITIVE_v1": appositive,
          "PLACENAME_v2": placename}

def decide(term, en, ja):
    for name in ORDER:
        v, why = STAGES[name](term, en, ja)
        if v:
            return v, why, name
    return "hold", "全規則が不発(要人手または規則追加)", None
'''

def s2():
    p = os.path.join(SCR, "nxdecide.py")
    open(p, "w", encoding="utf-8").write(DECIDE)
    subprocess.run([sys.executable, "-m", "py_compile", p], check=True)
    q = subprocess.run([sys.executable, os.path.join(SCR, "nxname.py"), p], capture_output=True, text=True)
    print("  NAMECHECK rc=%s %s" % (q.returncode, q.stdout.strip()[:120]))
    import nxdecide
    cases = [
      ("Kofukuji", "such as Tōdai-ji Temple, Kofukuji Temple, and Kasuga-taisha Shrine.", "", "apply"),
      ("Todaiji", "a high disciple of the priest Roben of Todaiji.", "", "apply"),
      ("Yamadera", "Ichinomiya Shrine (guardian deity of the Yamadera and Kumanishi areas). "
                   "Yamadera Yamagasa and Kumanishi Yamagasa. Kumade Ichiban Yamagasa, Fujita Nishi Yamagasa.",
       "\u5c71\u5bfa\u30fb\u718a\u897f\u5730\u533a\u306e\u6c0f\u795e", "reject"),
      ("Yamadera", "Yamadera in Yamagata, also called Risshaku-ji.", "", "hold"),
    ]
    for term, en, ja, exp in cases:
        v, why, st = nxdecide.decide(term, en, ja)
        print("  selftest %-9s exp=%-6s got=%-6s %s [%s] %s" % (term, exp, v, "OK" if v == exp else "NG", st, why[:70]))
        assert v == exp, (term, exp, v, why)
    return {"cases": len(cases)}

def s3():
    import nxmix, nxdecide
    con = sqlite3.connect(DB)
    fc = [r[1] for r in con.execute("pragma table_info('festivals')")]
    pf = "prefecture" if "prefecture" in fc else None
    seen = {(q, t) for q, t in con.execute("select qid,term from publish_queue")}
    sel = "select qid, manual_content_en, manual_content_ja" + (", " + pf if pf else "") + " from festivals"
    hits, cnt = [], collections.Counter()
    for row in con.execute(sel):
        qid, en, ja = row[0], row[1] or "", row[2] or ""
        for term in nxmix.CANON:
            n = len(nxmix._pat(term).findall(en))
            if not n:
                continue
            v, why, st = nxdecide.decide(term, en, ja)
            cnt[v] += 1
            hits.append({"qid": qid, "term": term, "n": n, "verdict": v, "stage": st, "why": why,
                         "pref": (row[3] if pf else None), "known": (qid, term) in seen})
    con.close()
    print("  検出 %d 件 / 内訳 %s / 既知 %d"
          % (len(hits), dict(cnt), sum(1 for h in hits if h["known"])))
    by = collections.Counter((h["term"], h["verdict"]) for h in hits)
    for (t, v), c in sorted(by.items()):
        print("    %-18s %-6s %d" % (t, v, c))
    print("  -- hold の先頭10件(規則追加の材料) --")
    for h in [x for x in hits if x["verdict"] == "hold"][:10]:
        print("    %s %-18s [%s] %s" % (h["qid"], h["term"], h["pref"], h["why"][:60]))
    return hits

def s4():
    con = sqlite3.connect(DB)
    ins = collections.Counter()
    for h in R["scan"]:
        if h["known"]:
            ins["skip_known"] += 1; continue
        state = "pending" if h["verdict"] == "apply" else h["verdict"]
        if APPLY:
            con.execute("insert into publish_queue(qid,term,state,note) values(?,?,?,?)",
                        (h["qid"], h["term"], state, (h["why"] or "")[:200]))
        ins[state] += 1
    if APPLY:
        con.commit()
    q = con.execute("select state,count(*) from publish_queue group by state").fetchall()
    con.close()
    print("  APPLY=%s 投入内訳=%s / queue現況=%s" % (APPLY, dict(ins), q))
    return dict(ins)

def s5():
    con = sqlite3.connect(DB)
    rows = con.execute("select tkey,old,new,verdict,src from verdict_ledger "
                       "where note is null or note=''").fetchall()
    for r in rows[:20]:
        print("    " + " | ".join(str(x) for x in r))
    if APPLY:
        con.execute("update verdict_ledger set note='LEGACY: 根拠未記録(LEDGER_v3以前の書き込み)。"
                    "再検証対象。' where note is null or note=''")
        con.commit()
    n = con.execute("select count(*) from verdict_ledger where note like 'LEGACY%'").fetchone()[0]
    con.close()
    print("  未記載 %d 行 -> LEGACY 印 %d 行 (APPLY=%s)" % (len(rows), n, APPLY))
    return {"legacy": len(rows)}

def s6():
    p = subprocess.run([sys.executable, os.path.join(SCR, "nxcheck.py")], cwd=ROOT,
                       capture_output=True, text=True)
    print("  nxcheck rc=%d %s" % (p.returncode, (p.stdout or "").strip()[-120:]))
    return {"rc": p.returncode}

KEY = "## [DECIDE_V1_QUEUE_20260810]"
BLOCK = KEY + """
判定順序を nxdecide.ORDER に一本化。SIBLING_COHERENCE_v1 -> REFERENCE_APPOSITIVE_v1
-> PLACENAME_v2 -> hold。規則が step スクリプト内に散っていると順序が暗黙になり、
step60 と step62 で違う順序が動く事故が起きる。順序の変更は ORDER のみを編集すること。
全件再スキャンの結果を publish_queue へ投入。apply 判定は即時反映せず state='pending'
として日次ドリップに渡す。reject/hold はそのまま記録し、日次は触らない。
既に queue にある (qid,term) は再投入しない(known スキップ)。
verdict_ledger の note 空欄行は LEGACY 印を付与。証拠の遡及生成はしない。
空欄放置は「検証済みなのに根拠がない」行を検証済みと誤読させるため、明示的に再検証対象と記す。
"""
def s7():
    import nxdoc
    try:
        nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError:
        nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    n = open(DOC, encoding="utf-8").read().count(KEY)
    print("  key count = %d" % n); return {"key_count": n}

sec("backup", s1); sec("decide", s2); sec("scan", s3)
sec("queue", s4); sec("legacy", s5); sec("regress", s6); sec("doc", s7)
j = os.path.join(SNAP, "step63_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
