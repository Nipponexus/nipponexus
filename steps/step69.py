# -*- coding: utf-8 -*-
# step69 : (1) プール構成の実態 (2) 県名の全件突合(機械検証可能な誤り) (3) 抽出は全文で再試験
import os, sys, re, json, time, sqlite3, datetime, collections, urllib.request, urllib.parse
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = os.environ.get("NX_UA", "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)")
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

def api(host, params):
    url = "https://%s/w/api.php?%s" % (host, urllib.parse.urlencode(params))
    rq = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(rq, timeout=45) as f:
        return json.loads(f.read().decode("utf-8"))

def title_of(wj, lj):
    if wj and "/" in wj:
        return urllib.parse.unquote(wj.rstrip("/").split("/")[-1]).replace("_", " ")
    return wj or lj

def pages(titles, intro):
    out = {}
    for i in range(0, len(titles), 20):
        p = {"action": "query", "format": "json", "prop": "extracts", "explaintext": 1,
             "redirects": 1, "titles": "|".join(titles[i:i+20])}
        if intro: p["exintro"] = 1
        try:
            d = api("ja.wikipedia.org", p)
            for pg in d.get("query", {}).get("pages", {}).values():
                out[pg.get("title")] = pg.get("extract") or ""
            for r in d.get("query", {}).get("redirects", []) or []:
                out[r["from"]] = out.get(r["to"], "")
            for nz in d.get("query", {}).get("normalized", []) or []:
                out[nz["from"]] = out.get(nz["to"], "")
        except Exception as e:
            print("  [warn] extracts %r" % e)
        sys.stdout.write("\r  取得 %d/%d" % (min(i+20, len(titles)), len(titles))); sys.stdout.flush()
        time.sleep(1.0)
    print()
    return out

# ---------- §1 プール構成 ----------
def s1():
    con = sqlite3.connect(DB)
    EMPTY = ("(manual_content_ja is null or manual_content_ja='') and "
             "(manual_content_en is null or manual_content_en='')")
    ids = [r[0] for r in con.execute("select qid from festivals where %s and status='pending' "
                                     "and wikipedia_ja is not null and wikipedia_ja<>''" % EMPTY)]
    con.close()
    n = int(os.environ.get("NX_N1", "0")) or len(ids)
    ids = ids[:n]
    p31 = collections.Counter(); of = {}
    for i in range(0, len(ids), 50):
        try:
            d = api("www.wikidata.org", {"action": "wbgetentities", "format": "json",
                                         "props": "claims", "ids": "|".join(ids[i:i+50])})
            for qid, e in d.get("entities", {}).items():
                vs = []
                for c in e.get("claims", {}).get("P31", []):
                    v = (c.get("mainsnak", {}).get("datavalue", {}) or {}).get("value", {})
                    if isinstance(v, dict) and v.get("id"):
                        vs.append(v["id"]); p31[v["id"]] += 1
                of[qid] = vs
        except Exception as e:
            print("  [warn] wd %r" % e)
        sys.stdout.write("\r  分類照会 %d/%d" % (min(i+50, len(ids)), len(ids))); sys.stdout.flush()
        time.sleep(1.0)
    print()
    top = [q for q, _ in p31.most_common(30)]
    lab = {}
    for i in range(0, len(top), 50):
        d = api("www.wikidata.org", {"action": "wbgetentities", "format": "json",
                                     "props": "labels", "languages": "ja|en", "ids": "|".join(top[i:i+50])})
        for q, e in d.get("entities", {}).items():
            L = e.get("labels", {})
            lab[q] = (L.get("ja", {}).get("value") or L.get("en", {}).get("value") or q)
        time.sleep(1.0)
    print("  プール %d 件の分類(P31)上位:" % len(of))
    for q, c in p31.most_common(20):
        print("    %-10s %-28s %d" % (q, lab.get(q, "?")[:28], c))
    KW = ("映画祭", "film festival", "音楽祭", "music festival", "見本市", "コンベンション",
          "アニメ", "同人", "コンテスト", "展覧会", "芸術祭", "スポーツ")
    off = sum(c for q, c in p31.items() if any(k in lab.get(q, "") for k in KW))
    print("  現代イベント系(映画祭・音楽祭等)と判定される分類の延べ数 = %d" % off)
    return {"n": len(of), "p31": dict(p31.most_common(20)), "labels": lab}

# ---------- §2 県名突合 ----------
PREF = re.compile(r"(北海道|(?:京都|大阪)府|東京都|[\u4e00-\u9fa5]{2,3}県)")
def s2():
    con = sqlite3.connect(DB)
    rows = con.execute("select qid,label_ja,wikipedia_ja,prefecture from festivals "
                       "where prefecture is not null and prefecture<>'' "
                       "and wikipedia_ja is not null and wikipedia_ja<>'' "
                       "order by qid").fetchall()
    n = int(os.environ.get("NX_N2", "120"))
    rows = rows[:n]
    print("  突合対象 %d 件" % len(rows))
    tmap = {}
    for qid, lj, wj, pf in rows:
        tmap.setdefault(title_of(wj, lj), []).append((qid, lj, pf))
    ext = pages(list(tmap), intro=True)
    ok = miss = nodata = 0; bad = []
    for t, lst in tmap.items():
        txt = ext.get(t, "")
        found = PREF.findall(txt or "")
        for qid, lj, pf in lst:
            if not txt:
                nodata += 1; continue
            if not found:
                nodata += 1; continue
            if pf in found:
                ok += 1
            else:
                miss += 1
                bad.append({"qid": qid, "label": lj, "db": pf, "text": list(dict.fromkeys(found))[:3],
                            "ctx": (txt[:110].replace("\n", " "))})
    print("  一致 %d / 不一致 %d / 判定不能 %d" % (ok, miss, nodata))
    for b in bad[:25]:
        print("  [!] %-11s %-24s DB=%-5s 本文=%s" % (b["qid"], (b["label"] or "")[:24], b["db"], b["text"]))
        print("        …%s…" % b["ctx"][:100])
    return {"ok": ok, "miss": miss, "nodata": nodata, "bad": bad}

# ---------- §3 全文での抽出再試験 ----------
RXD = {
 "序数曜日": re.compile(r"(\d{1,2})月(?:の)?第([一二三四五1-5])[週]?(?:の)?([日月火水木金土])曜日"),
 "確定日": re.compile(r"(\d{1,2})月(\d{1,2})日"),
 "旬": re.compile(r"(\d{1,2})月(上旬|中旬|下旬)"),
}
NEG = re.compile(r"(創建|創始|開始|第1回|第一回|初開催|設立|建立|年に|より|以来|生まれ|没|落成)")
def s3():
    con = sqlite3.connect(DB)
    EMPTY = ("(manual_content_ja is null or manual_content_ja='') and "
             "(manual_content_en is null or manual_content_en='')")
    rows = con.execute("select qid,label_ja,wikipedia_ja from festivals where %s and status='pending' "
                       "and wikipedia_ja is not null and wikipedia_ja<>'' "
                       "and (label_ja like '%%祭%%' or label_ja like '%%まつり%%' or label_ja like '%%マツリ%%') "
                       "and label_ja not like '%%映画%%' and label_ja not like '%%音楽%%' "
                       "order by priority_score desc limit ?" % EMPTY,
                       (int(os.environ.get("NX_N3", "25")),)).fetchall()
    con.close()
    print("  伝統祭らしき対象 %d 件を全文で再試験" % len(rows))
    tmap = {title_of(w, l): (q, l) for q, l, w in rows}
    ext = pages(list(tmap), intro=False)
    hit = 0
    for t, (q, l) in tmap.items():
        txt = ext.get(t, "")
        if not txt:
            print("  %-11s %-20s 本文なし" % (q, (l or "")[:20])); continue
        head = txt[:400]
        got = []
        for k, rx in RXD.items():
            for m in rx.finditer(txt):
                s = txt[max(0, m.start()-50):m.end()+50].replace("\n", " ")
                if NEG.search(txt[max(0, m.start()-25):m.start()]):
                    continue
                got.append((k, m.group(0), s, m.start() < 400))
                break
        lead = [g for g in got if g[3]]
        if lead: hit += 1
        print("  %-11s %-20s 全文%d字 導入部一致=%s" % (q, (l or "")[:20], len(txt), bool(lead)))
        for k, v, s, inlead in got[:3]:
            print("      %-6s %-10s %s …%s…" % (k, v, "[導入部]" if inlead else "[本文中]", s[:80]))
    print("  導入部で日付を取れた = %d / %d" % (hit, len(tmap)))
    return {"hit": hit, "n": len(tmap)}

sec("pool", s1); sec("pref", s2); sec("extract", s3)
j = os.path.join(SNAP, "step69_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("READ ONLY / snapshot=%s" % j)
