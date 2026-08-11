# -*- coding: utf-8 -*-
# step72 : 確定7件の反映 / WD不在を第二軸(市区町村→県)で解決 / loc_qid 空 463件の汚染率測定
import os, sys, re, json, time, sqlite3, datetime, collections, urllib.parse
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = os.environ.get("NX_UA", "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)")
APPLY = os.environ.get("NX_APPLY") == "1"
sys.path.insert(0, SCR)
import nxwiki, nxledger
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

def s0():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    a = sqlite3.connect(DB); c = sqlite3.connect(b); a.backup(c); c.close(); a.close()
    print("  " + b); return {"db_snapshot": b}

CITY = re.compile("(" + "|".join(sorted(nxwiki.PREFS, key=len, reverse=True)) + ")"
                  r"([\u4e00-\u9fa5\u3040-\u30ff]{1,6}?[市区町村])")
def wd_ents(ids, props="claims|labels", langs="ja"):
    out = {}
    for i in range(0, len(ids), 50):
        p = {"action": "wbgetentities", "format": "json", "props": props, "ids": "|".join(ids[i:i+50])}
        if langs: p["languages"] = langs
        try: out.update(nxwiki.api("www.wikidata.org", p, UA).get("entities", {}))
        except Exception as e: print("  [warn] wd %r" % e)
        time.sleep(1.0)
    return out
def qid_of_titles(titles):
    out = {}
    for i in range(0, len(titles), 40):
        p = {"action": "query", "format": "json", "prop": "pageprops", "redirects": 1,
             "titles": "|".join(titles[i:i+40])}
        try:
            d = nxwiki.api("ja.wikipedia.org", p, UA).get("query", {})
            by = {pg.get("title"): (pg.get("pageprops", {}) or {}).get("wikibase_item")
                  for pg in d.get("pages", {}).values()}
            alias = {}
            for r in (d.get("redirects") or []): alias[r["from"]] = r["to"]
            for nz in (d.get("normalized") or []): alias[nz["from"]] = nz["to"]
            for t in titles[i:i+40]:
                cur = alias.get(t, t)
                out[t] = by.get(cur)
        except Exception as e: print("  [warn] pageprops %r" % e)
        time.sleep(1.0)
    return out
def city_to_pref(cities):
    """市区町村名 -> 県名。jawiki記事 -> wikibase_item -> P131 を上位に辿る。祭名を一切使わない独立経路。"""
    q = qid_of_titles(cities)
    ids = [v for v in q.values() if v]
    ents = wd_ents(ids)
    res = {}
    for c in cities:
        qid = q.get(c)
        if not qid: continue
        cur, seen = qid, 0
        while cur and seen < 4:
            e = ents.get(cur)
            if e is None:
                e = wd_ents([cur]).get(cur, {}); ents[cur] = e
            lab = (e.get("labels", {}).get("ja", {}) or {}).get("value", "")
            if lab in nxwiki.PREFS: res[c] = lab; break
            nxt = None
            for cl in e.get("claims", {}).get("P131", []):
                v = (cl.get("mainsnak", {}).get("datavalue", {}) or {}).get("value", {})
                if isinstance(v, dict) and v.get("id"): nxt = v["id"]; break
            cur = nxt; seen += 1
    return res

# ---------- §1 確定7件 ----------
CONFIRMED = [("Q11267368","さいすくい","三重県","大分県"),("Q11455990","富士山御神火まつり","山梨県","静岡県"),
             ("Q11556000","津屋崎祇園山笠","三重県","福岡県"),("Q28691756","滝山寺鬼まつり","山形県","愛知県"),
             ("Q38277378","日本幻野祭","福岡県","千葉県"),("Q56010148","猪名川花火大会","京都府","兵庫県"),
             ("Q64539503","鳥羽の火祭り","三重県","愛知県")]
def s1():
    con = sqlite3.connect(DB); n = 0
    for qid, lab, old, new in CONFIRMED:
        cur_v = con.execute("select prefecture from festivals where qid=?", (qid,)).fetchone()
        if not cur_v or cur_v[0] != old:
            print("  [skip] %s 現在値=%s (期待 %s)" % (qid, cur_v and cur_v[0], old)); continue
        if APPLY:
            c = con.execute("update festivals set prefecture=?, updated_at=? where qid=? and prefecture=?",
                            (new, TS, qid, old))
            if c.rowcount != 1: raise RuntimeError("CAS %s" % qid)
            nxledger.put(con, tkey="pref|%s" % qid, qid=qid, ja=lab, old=old, new=new, verdict="apply",
                         decided_at=TS, src="step72/PREFCHECK_v2_WD",
                         note="jawiki導入部とWikidata P131/P276 の二系統一致による訂正。旧値は名称由来の推測とみられる。",
                         url="https://www.wikidata.org/wiki/" + qid)
        n += 1
        print("  %-11s %-18s %s -> %s" % (qid, lab[:18], old, new))
    if APPLY: con.commit()
    con.close(); print("  反映 %d 件 (APPLY=%s)" % (n, APPLY)); return n

# ---------- §2 WD不在16件を第二軸で解決 ----------
HOLDS = ["Q11361495","Q11381253","Q11408464","Q11425142","Q11437490","Q11463659","Q11464484",
         "Q11465151","Q11466745","Q11467395","Q11538304","Q11549648","Q11558195","Q21652662",
         "Q30928431","Q1636567"]
def s2():
    con = sqlite3.connect(DB)
    rows = con.execute("select qid,label_ja,wikipedia_ja,prefecture from festivals where qid in (%s)"
                       % ",".join("?" * len(HOLDS)), HOLDS).fetchall()
    tmap = {nxwiki.title_of(w, l): (q, l, p) for q, l, w, p in rows}
    ext = nxwiki.extracts(list(tmap), intro=True, ua=UA)
    pend = []
    for t, (q, l, dbp) in tmap.items():
        m = CITY.search(ext.get(t, ""))
        pend.append({"qid": q, "label": l, "db": dbp, "title": t,
                     "pref_in_text": m.group(1) if m else None, "city": m.group(2) if m else None,
                     "intro": ext.get(t, "")[:160].replace("\n", " ")})
    cities = sorted({p["city"] for p in pend if p["city"]})
    print("  市区町村を独立照会 (%d 件): %s" % (len(cities), cities))
    cmap = city_to_pref(cities)
    res = []
    for p in pend:
        p["city_pref"] = cmap.get(p["city"] or "", "")
        if not p["city"]:
            p["verdict"] = "hold(市区町村を抽出できず)"
        elif not p["city_pref"]:
            p["verdict"] = "hold(市の県を解決できず)"
        elif p["city_pref"] != p["pref_in_text"]:
            p["verdict"] = "hold(導入部の県と市の帰属が不一致)"
        elif p["city_pref"] == p["db"]:
            p["verdict"] = "db_ok"
        else:
            p["verdict"] = "confirmed2"
        res.append(p)
        print("  %-11s %-18s DB=%-5s 本文=%-5s 市=%-8s 市の帰属=%-5s %s"
              % (p["qid"], (p["label"] or "")[:18], p["db"], p["pref_in_text"] or "-",
                 p["city"] or "-", p["city_pref"] or "-", p["verdict"]))
    ok = [p for p in res if p["verdict"] == "confirmed2"]
    print("  第二軸で確定 = %d / %d" % (len(ok), len(res)))
    for p in ok:
        if APPLY:
            c = con.execute("update festivals set prefecture=?, updated_at=? where qid=? and prefecture=?",
                            (p["city_pref"], TS, p["qid"], p["db"]))
            if c.rowcount != 1: raise RuntimeError("CAS %s" % p["qid"])
            nxledger.put(con, tkey="pref|%s" % p["qid"], qid=p["qid"], ja=p["label"],
                         old=p["db"], new=p["city_pref"], verdict="apply", decided_at=TS,
                         src="step72/CITYCHAIN_v1",
                         note=("jawiki導入部に『%s%s』。市区町村 %s を祭名と無関係の経路(jawiki記事→wikibase_item→P131)"
                               "で照会し帰属県=%s を確認。旧値 %s は祭名からの推測誤り。導入部: %s"
                               % (p["pref_in_text"], p["city"], p["city"], p["city_pref"], p["db"], p["intro"]))[:600],
                         url="https://ja.wikipedia.org/wiki/" + urllib.parse.quote(p["title"].replace(" ", "_")))
    if APPLY: con.commit()
    con.close(); return res

# ---------- §3 汚染率 ----------
def s3():
    con = sqlite3.connect(DB)
    err = {c[0] for c in CONFIRMED} | {p["qid"] for p in R["second"] if p["verdict"] == "confirmed2"}
    tot = collections.Counter(); bad = collections.Counter()
    for qid, loc in con.execute("select qid, location_qid from festivals where prefecture is not null and prefecture<>''"):
        k = "loc_qid あり" if loc else "loc_qid 空"
        tot[k] += 1
        if qid in err: bad[k] += 1
    print("  誤り %d 件の分布:" % len(err))
    for k in tot:
        print("    %-12s 誤り %2d / 検査母数 %3d" % (k, bad[k], tot[k]))
    print("  ※ 母数は突合できた572件ベース。loc_qid 空の群に誤りが偏るなら推測由来が裏付けられる。")
    print("  loc_qid 空かつ prefecture ありの全件 = %d" % tot["loc_qid 空"])
    print("  名称推測が疑われる組み合わせ(loc_qid 空):")
    for kw, p in (("祇園","京都府"),("ねぷた","青森県"),("よさこい","高知県"),("阿波踊","徳島県"),
                  ("天神","大阪府"),("七夕","宮城県"),("だんじり","大阪府"),("エイサー","沖縄県")):
        n = con.execute("select count(*) from festivals where label_ja like ? and prefecture=? "
                        "and (location_qid is null or location_qid='')", ("%"+kw+"%", p)).fetchone()[0]
        if n: print("    %-8s -> %-5s %d 件" % (kw, p, n))
    con.close(); return dict(tot)

KEY = "## [WD_SILENCE_CITYCHAIN_20260811]"
BLOCK = KEY + """
不在と矛盾を区別する。step71 の hold 16件は二系統の食い違いではなく Wikidata が
P131/P276 を持たないだけだった。両者を同じ hold に潰すと、Wikidata が薄い領域で
永久に前へ進めなくなる。WD_SILENT と WD_CONFLICT を分けること。
CITYCHAIN_v1(第二軸): jawiki 導入部から「県名+市区町村名」を取り、市区町村名のみを
jawiki記事 -> wikibase_item -> P131 で照会して帰属県を得る。祭の名称を一切経由しないため
名称推測バイアスから独立。導入部の県と市の帰属が一致した時のみ訂正を確定する。
原因の裏付け: 祇園を含み京都府とされた9件中8件、ねぷた4件全件、よさこい2件全件で
location_qid が空。location_qid を持たない行の prefecture は祭名からの推測とみられる。
prefecture あり794件中463件(58%)が location_qid 空。prefecture 以外の列にも同じ疑いが及ぶ。
神戸ルミナリエは db_ok。導入部に震災の記述で東京都が出たための誤検出であり DB 値が正しい。
"""
def s4():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("backup", s0); sec("confirmed", s1); sec("second", s2); sec("pollution", s3); sec("doc", s4)
j = os.path.join(SNAP, "step72_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
