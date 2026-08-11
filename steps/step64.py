# -*- coding: utf-8 -*-
# step64 : READ ONLY 監査。(1) QID 整合 (2) tkey からの証拠展開の可否 (3) 日次の実仕事の在処
import os, sys, re, json, sqlite3, collections
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
sys.path.insert(0, SCR)
import nxmix

con = sqlite3.connect(DB)
def cols(t): return [r[1] for r in con.execute("pragma table_info('%s')" % t)]
print("=" * 72); print("§1 テーブル一覧と規模")
tabs = [r[0] for r in con.execute("select name from sqlite_master where type='table' order by 1")]
for t in tabs:
    try: n = con.execute("select count(*) from '%s'" % t).fetchone()[0]
    except Exception as e: n = "ERR %r" % e
    print("  %-24s %s" % (t, n))
print("  festivals cols = %s" % cols("festivals"))

print("=" * 72); print("§2 verdict_ledger の tkey 構造と証拠展開の可否")
rows = con.execute("select tkey,qid,ja,en,old,new,verdict,src,note from verdict_ledger").fetchall()
pat = re.compile(r"JA\[([^\]]*)\]|EN\[([^\]]*)\]")
parsed = []
for r in rows:
    tkey = r[0]; parts = tkey.split("|")
    ja = en = None
    for m in pat.finditer(tkey):
        if m.group(1) is not None: ja = m.group(1)
        if m.group(2) is not None: en = m.group(2)
    qid = r[1] or (parts[0] if parts and re.match(r"^Q", parts[0]) else None)
    parsed.append({"tkey": tkey, "kind": (parts[1] if len(parts) > 1 else "canon"),
                   "qid": qid, "ja_from_tkey": ja, "en_from_tkey": en,
                   "old": r[4], "new": r[5], "verdict": r[6], "src": r[7],
                   "note_empty": not (r[8] or "").strip()})
k = collections.Counter(p["kind"] for p in parsed)
print("  種別内訳 = %s" % dict(k))
print("  note 空 = %d / %d、うち tkey から JA か EN を復元可 = %d"
      % (sum(p["note_empty"] for p in parsed), len(parsed),
         sum(1 for p in parsed if p["note_empty"] and (p["ja_from_tkey"] or p["en_from_tkey"]))))

print("=" * 72); print("§3 QID 整合検査")
fq = {r[0] for r in con.execute("select qid from festivals")}
nc = [c for c in ("name_ja", "title_ja", "name", "name_en", "title_en") if c in cols("festivals")]
bad = []
for p in parsed:
    q = p["qid"]
    if not q: continue
    if not re.match(r"^Q[0-9]+$", q):
        bad.append((q, p["tkey"][:60], "QID書式でない(自作プレースホルダ)")); continue
    if q not in fq:
        bad.append((q, p["tkey"][:60], "festivals に存在しない")); continue
    if p["ja_from_tkey"] and nc:
        row = con.execute("select %s from festivals where qid=?" % ",".join(nc), (q,)).fetchone()
        blob = " / ".join(str(x) for x in row if x)
        if p["ja_from_tkey"] not in blob:
            body = (con.execute("select manual_content_ja from festivals where qid=?", (q,)).fetchone() or [""])[0] or ""
            where = "本文にはあり" if p["ja_from_tkey"] in body else "本文にも無し"
            bad.append((q, p["tkey"][:60], "台帳JA『%s』が festivals 名称と不一致(%s) 名称=%s"
                        % (p["ja_from_tkey"], where, blob[:40])))
for b in bad:
    print("  [!] %-12s %-62s %s" % b)
print("  不整合 = %d / 検査対象 %d" % (len(bad), sum(1 for p in parsed if p["qid"])))

print("=" * 72); print("§4 日次の実仕事はどこにあるか")
print("  CANON 8語 の本文残存:")
tot = 0
for term in nxmix.CANON:
    n = sum(len(nxmix._pat(term).findall((r[0] or "") + " " + (r[1] or "")))
            for r in con.execute("select manual_content_en, manual_content_ja from festivals"))
    tot += n
    if n: print("    %-18s %d" % (term, n))
print("    合計残存 = %d" % tot)
have_en = con.execute("select count(*) from festivals where manual_content_en is not null and manual_content_en<>''").fetchone()[0]
print("  festivals 総数 %d / EN本文あり %d" % (len(fq), have_en))
for t in tabs:
    if t == "verdict_ledger" or "queue" in t or "scan" in t or "cand" in t or "pend" in t:
        try:
            c = cols(t); st = next((x for x in ("state", "status", "verdict") if x in c), None)
            if st:
                print("  %s の状態内訳 = %s" % (t, con.execute("select %s,count(*) from '%s' group by 1" % (st, t)).fetchall()))
        except Exception as e:
            print("  %s 読取失敗 %r" % (t, e))
print("=" * 72); print("§5 結論材料")
print("  ・CANON 語の未処理 = %d 件 -> 日次に流す玉が %s" % (tot, "無い" if tot == 0 else "ある"))
print("  ・台帳 QID 不整合 = %d 件" % len(bad))
print("  ・tkey から復元可能な証拠行 = %d 件"
      % sum(1 for p in parsed if p["note_empty"] and (p["ja_from_tkey"] or p["en_from_tkey"])))
con.close()
