#!/usr/bin/env python3
import sqlite3, os, re, sys, shutil, datetime

DB    = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")
TS    = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
STAGE = os.path.expanduser("~/nipponexus/_staging/push_" + TS)

def die(m):
    print("\n!! ABORT: " + m); sys.exit(1)
def head(t):
    print("\n" + "="*8 + " " + t + " " + "="*8)

head("0. backup")
bk = os.path.expanduser("~/nipponexus/data/sqlite/_backup/nipponexus.db." + TS)
os.makedirs(os.path.dirname(bk), exist_ok=True); shutil.copy2(DB, bk)
print("backup:", bk)
con = sqlite3.connect(DB); con.row_factory = sqlite3.Row

head("0c. deploy_article.py / nightly_rebuild.sh")
for p in ["~/nipponexus/scripts/deploy_article.py", "~/nipponexus/scripts/nightly_rebuild.sh"]:
    fp = os.path.expanduser(p)
    if not os.path.exists(fp):
        print("\n--- " + p + " : NOT FOUND"); continue
    t = open(fp, encoding="utf-8", errors="replace").read()
    print("\n--- " + p + "  (" + str(len(t)) + "B) ---")
    print(t[:3500])
    if len(t) > 3500: print("...[truncated]")

head("0d. site tree")
site = os.path.expanduser("~/nipponexus/site")
n = 0
for dp, dn, fn in os.walk(site):
    dn[:] = [d for d in dn if d not in (".git","node_modules",".next","dist",".astro")]
    rel = os.path.relpath(dp, site)
    md = [f for f in fn if f.endswith((".md",".mdx",".json"))]
    if md:
        print("  " + rel + "/  (" + str(len(md)) + " files) e.g. " + ", ".join(sorted(md)[:4]))
        n += 1
    if n > 25: print("  ..."); break

head("1. candidates")
hold_open, unresolved = set(), set()
tabs = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
if "hold_queue" in tabs:
    hq = [r["name"] for r in con.execute("PRAGMA table_info(hold_queue)")]
    st = "status" if "status" in hq else None
    q = "SELECT * FROM hold_queue"
    if st: q += " WHERE " + st + " NOT IN ('closed','resolved','done')"
    for r in con.execute(q):
        for k in ("qid","target_qid","item"):
            if k in r.keys() and r[k]: hold_open.add(r[k])
if "pref_audit" in tabs:
    for r in con.execute("SELECT qid FROM pref_audit WHERE COALESCE(applied,0)=0 AND status NOT IN ('rejected','false_positive')"):
        unresolved.add(r["qid"])
print("open holds=%d  unresolved pref_audit=%d" % (len(hold_open), len(unresolved)))

rows = [dict(r) for r in con.execute(
    "SELECT qid,label_ja,label_en,slug_ja,slug_en,prefecture,published_at,"
    "manual_content_ja AS ja, manual_content_en AS en "
    "FROM festivals WHERE status='drafted'")]
if not rows: die("no drafted rows")
print("drafted: %d" % len(rows))
print("published_at already set: %d" % sum(1 for r in rows if r["published_at"]))
print("manual_content_en 欠落: %d" % sum(1 for r in rows if not (r["en"] or "").strip()))

END_KW = re.compile(r"(終了しました|最後の開催|をもって終了|廃止)")
FUT_KW = re.compile(r"(開催予定|2027年|2028年)")
ok, why = [], {}
for r in rows:
    b = (r["ja"] or ""); e = (r["en"] or "")
    rs = []
    if len(b) < 3000: rs.append("short")
    if not r["slug_ja"]: rs.append("no-slug_ja")
    if not r["slug_en"]: rs.append("no-slug_en")
    if not e.strip(): rs.append("no-en-body")
    if not r["label_en"]: rs.append("no-label_en")
    if not r["prefecture"]: rs.append("no-pref")
    if r["published_at"]: rs.append("already-published")
    if r["qid"] in hold_open: rs.append("hold")
    if r["qid"] in unresolved: rs.append("pref_audit")
    if END_KW.search(b): rs.append("ended?")
    if FUT_KW.search(b): rs.append("future?")
    if rs: why[r["qid"]] = rs
    else: ok.append(r)
from collections import Counter
c = Counter(x for v in why.values() for x in v)
print("除外理由 内訳:", dict(c.most_common()))
if len(ok) < 5: die("only %d clean candidates" % len(ok))
ok.sort(key=lambda r: -len(r["ja"]))
print("clean candidates: %d\n" % len(ok))

FORCE = "Q21654380"   # 深谷まつり(県名修正済)を必ず1本入れる
seen, pick = set(), []
for r in ok:
    if r["qid"] == FORCE:
        pick.append(r); seen.add(r["prefecture"]); break
for r in ok:
    if len(pick) >= 5: break
    if r in pick or r["prefecture"] in seen: continue
    seen.add(r["prefecture"]); pick.append(r)
for i, r in enumerate(pick, 1):
    print("%d. %s / %s / %s / ja%d字 en%d字 / %s | %s" % (
        i, r["label_ja"], r["qid"], r["prefecture"], len(r["ja"]), len(r["en"]), r["slug_ja"], r["slug_en"]))

head("2. lint")
LINT = [("回次表記", r"第\s*\d+\s*回"),
        ("相対年",   r"(来年|今年|昨年|一昨年|今年度|来年度|現在まで|直近)"),
        ("電話番号", r"\d{2,4}-\d{2,4}-\d{3,4}"),
        ("主催不明", r"主催[：: ]*(不明|未確認|なし|N/A)"),
        ("検出器残渣", r"(▲出典|\bL\d{1,3}\b|｜要出典)")]
bad = 0
for r in pick:
    hits = []
    for name, pat in LINT:
        m = re.findall(pat, r["ja"]) + re.findall(pat, r["en"])
        if m: hits.append("%s×%d: %s" % (name, len(m), str(m[:3])[:80]))
    pc = r["ja"].count(r["prefecture"])
    print("\n[%s] 県名『%s』本文出現 %d回" % (r["label_ja"], r["prefecture"], pc))
    if pc == 0: hits.append("本文に県名なし(要目視)")
    for h in hits: print("   -", h)
    if hits: bad += 1
    else: print("   clean")
print("\n要目視: %d/5" % bad)

head("3. staging (書き出しのみ / push無し)")
os.makedirs(STAGE, exist_ok=True)
for r in pick:
    for lang, slug, body, title in (("ja", r["slug_ja"], r["ja"], r["label_ja"]),
                                    ("en", r["slug_en"], r["en"], r["label_en"])):
        fp = os.path.join(STAGE, lang + "__" + slug + ".md")
        with open(fp, "w", encoding="utf-8") as f:
            f.write("---\ntitle: " + str(title) + "\nslug: " + slug +
                    "\nprefecture: " + r["prefecture"] + "\nqid: " + r["qid"] + "\n---\n\n")
            f.write(body.strip() + "\n")
    mid = r["ja"][len(r["ja"])//2:][:24].replace("\n", "")
    print("  %-28s 検証句: 「%s」" % (r["slug_ja"], mid))
print("\nstaged -> " + STAGE)

head("4. status")
for r in con.execute("SELECT status, COUNT(*) n FROM festivals GROUP BY status ORDER BY n DESC"):
    print("  %-24s %d" % (r["status"], r["n"]))
con.close()
print("\n>> push未実行。0c/0d を見てから公開コマンドを確定します。")
