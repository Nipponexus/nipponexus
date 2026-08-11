# -*- coding: utf-8 -*-
# step61 : (1) Yamadera hold の文脈全ダンプ (2) step60 本適用 (3) 事後検証
import os, sys, re, json, sqlite3, subprocess
HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "nipponexus")
SCR  = os.path.join(ROOT, "scripts")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
sys.path.insert(0, SCR)
import nxmix

def cols(con, t):
    return [r[1] for r in con.execute("pragma table_info('%s')" % t)]

def win(t, m, n=300):
    return t[max(0, m.start() - n): m.end() + n].replace("\n", " ")

# ---------- §1 Yamadera 文脈ダンプ (read only) ----------
print("=" * 70); print("§1 Q11678183 / Yamadera 文脈")
con = sqlite3.connect(DB)
fc = cols(con, "festivals")
want = [c for c in ("qid","name_en","name_ja","prefecture","city","municipality",
                    "manual_content_en","manual_content_ja") if c in fc]
r = con.execute("select %s from festivals where qid=?" % ",".join(want), ("Q11678183",)).fetchone()
rec = dict(zip(want, r)) if r else {}
for k in want:
    if k.startswith("manual_"):
        continue
    print("  %-18s %s" % (k, rec.get(k)))
en = rec.get("manual_content_en") or ""
ja = rec.get("manual_content_ja") or ""
print("  len(en)=%d len(ja)=%d" % (len(en), len(ja)))
pat = nxmix._pat("Yamadera")
ms = list(pat.finditer(en))
print("  EN 出現 = %d" % len(ms))
for i, m in enumerate(ms):
    print("  --- 出現#%d (pos=%d) ±300字 ---" % (i + 1, m.start()))
    print("  " + win(en, m))
for i, s in enumerate(nxmix.sentences(en)):
    if pat.search(s):
        print("  --- 該当文#%d (全文) ---" % (i + 1)); print("  " + s.strip())
for m in re.finditer("山寺", ja):
    print("  --- JA 山寺 ±60字 ---"); print("  " + ja[max(0, m.start()-60): m.end()+60].replace("\n", " "))
print("  JA 山寺 出現 = %d" % len(re.findall("山寺", ja)))
oth = [w for w in ("Yamagata","Risshaku","立石寺","山形") if w in en or w in ja]
print("  正典側の手掛かり(Yamagata/Risshaku/立石寺/山形) = %s" % (oth or "なし"))
q = con.execute("select * from publish_queue").fetchall()
print("  publish_queue = %s" % (q,))
con.close()

# ---------- §2 step60 本適用 ----------
print("=" * 70); print("§2 step60 NX_APPLY=1")
env = dict(os.environ); env["NX_APPLY"] = "1"
p = subprocess.run([sys.executable, os.path.join(ROOT, "steps", "step60.py")],
                   cwd=ROOT, env=env, capture_output=True, text=True)
print(p.stdout[-4000:])
if p.stderr.strip():
    print("[stderr]" + p.stderr[-1000:])
print("  step60 rc=%d" % p.returncode)

# ---------- §3 事後検証 ----------
print("=" * 70); print("§3 事後検証")
con = sqlite3.connect(DB)
left = nxmix.scan_db(con)
print("  文内混在 残 = %d %s" % (len(left), [x["qid"] for x in left]))
for qid, term in (("Q3461576", "Todaiji"), ("Q844110", "Kofukuji")):
    t = con.execute("select manual_content_en from festivals where qid=?", (qid,)).fetchone()[0] or ""
    print("  %s : 旧'%s'残=%d 新'%s'=%d" % (qid, term, len(nxmix._pat(term).findall(t)),
          nxmix.CANON[term], len(nxmix._pat(nxmix.CANON[term]).findall(t))))
print("  -- verdict_ledger (今回分) --")
for row in con.execute("select tkey,verdict,new,url,substr(note,1,90) from verdict_ledger "
                       "where tkey like 'canon|%' and decided_at like '2026%' "
                       "order by decided_at desc limit 8"):
    print("   " + " | ".join(str(x) for x in row))
n_null = con.execute("select count(*) from verdict_ledger where note is null or note=''").fetchone()[0]
print("  note 未記載の台帳行 = %d / %d (LEDGER_v3 以前の分)"
      % (n_null, con.execute("select count(*) from verdict_ledger").fetchone()[0]))
print("  publish_queue = %s" % (con.execute("select * from publish_queue").fetchall(),))
con.close()
