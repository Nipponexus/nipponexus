# -*- coding: utf-8 -*-
# step73 : 18件の本適用 / 郡名対応(CITYCHAIN_v2) / 残り hold の決着 / 全県突合の常設化
import os, sys, re, json, time, sqlite3, datetime, collections, subprocess, urllib.parse
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

CHAIN = r'''# -*- coding: utf-8 -*-
# CITYCHAIN_v2 : 市区町村名 -> 帰属県。祭の名称を一切経由しない独立経路。
# v1 の欠陥 = 「多気郡明和町」のように郡名込みで jawiki を引き、記事に当たらず解決不能だった。
# v2 = 郡を剥がした候補、曖昧回避の「県名+市名」候補を順に試す。
import re, time
import nxwiki
GUN = re.compile(r"^[\u4e00-\u9fa5\u3040-\u30ff]{1,5}郡")
CITY_RX = None

def city_candidates(pref, city):
    """照会に使うタイトル候補を優先順に返す。"""
    out = []
    bare = GUN.sub("", city)          # 多気郡明和町 -> 明和町
    for c in ([city] if city != bare else []) + [bare]:
        out.append(c)
        out.append("%s (%s)" % (c, pref))   # 明和町 (三重県)
        out.append(pref + c)                 # 三重県明和町
    seen, r = set(), []
    for x in out:
        if x not in seen:
            seen.add(x); r.append(x)
    return r

def resolve(pairs, ua=None, verbose=True):
    """[(pref, city)] -> {(pref,city): 県名}。pref は候補生成の絞り込みにのみ使う。"""
    titles = []
    idx = {}
    for pref, city in pairs:
        cs = city_candidates(pref, city)
        idx[(pref, city)] = cs
        titles += cs
    titles = list(dict.fromkeys(titles))
    qmap = nxwiki.pageprops_qid(titles, ua=ua)
    ids = [v for v in qmap.values() if v]
    ents = nxwiki.wd_entities(ids, ua=ua)
    res, why = {}, {}
    for key, cands in idx.items():
        for t in cands:
            qid = qmap.get(t)
            if not qid:
                continue
            p = nxwiki.wd_climb_pref(qid, ents, ua=ua)
            if p:
                res[key] = p; why[key] = "%s -> %s -> P131" % (t, qid); break
    return res, why
'''

WIKI_ADD = r'''
# >>>NX:WDHELPERS
def pageprops_qid(titles, ua=None, sleep=1.0):
    """jawiki タイトル -> wikibase_item。redirect/normalize を辿って要求綴りで返す。"""
    out = {}
    for i in range(0, len(titles), 40):
        chunk = titles[i:i + 40]
        p = {"action": "query", "format": "json", "prop": "pageprops", "redirects": 1,
             "titles": "|".join(chunk)}
        try:
            d = api("ja.wikipedia.org", p, ua).get("query", {})
        except Exception:
            time.sleep(2); continue
        by = {pg.get("title"): (pg.get("pageprops") or {}).get("wikibase_item")
              for pg in d.get("pages", {}).values()}
        alias = {}
        for r in (d.get("redirects") or []): alias[r["from"]] = r["to"]
        for nz in (d.get("normalized") or []): alias[nz["from"]] = nz["to"]
        for t in chunk:
            cur, k = t, 0
            while cur in alias and k < 5:
                cur = alias[cur]; k += 1
            out[t] = by.get(cur, by.get(t))
        time.sleep(sleep)
    return out

def wd_entities(ids, ua=None, props="claims|labels", langs="ja", sleep=1.0):
    out = {}
    ids = [i for i in dict.fromkeys(ids) if i]
    for i in range(0, len(ids), 50):
        p = {"action": "wbgetentities", "format": "json", "props": props, "ids": "|".join(ids[i:i + 50])}
        if langs: p["languages"] = langs
        try:
            out.update(api("www.wikidata.org", p, ua).get("entities", {}))
        except Exception:
            time.sleep(2)
        time.sleep(sleep)
    return out

def wd_climb_pref(qid, cache, ua=None, maxhop=4):
    """P131 を上位に辿り 47 都道府県に到達したら県名を返す。"""
    cur, hop = qid, 0
    while cur and hop < maxhop:
        e = cache.get(cur)
        if e is None:
            e = wd_entities([cur], ua=ua).get(cur, {}); cache[cur] = e
        lab = ((e.get("labels") or {}).get("ja") or {}).get("value", "")
        if lab in PREFS:
            return lab
        nxt = None
        for cl in (e.get("claims") or {}).get("P131", []):
            v = (cl.get("mainsnak", {}).get("datavalue", {}) or {}).get("value", {})
            if isinstance(v, dict) and v.get("id"):
                nxt = v["id"]; break
        cur = nxt; hop += 1
    return None
# <<<NX:WDHELPERS
'''

def s1():
    p = os.path.join(SCR, "nxwiki.py")
    s = open(p, encoding="utf-8").read()
    if ">>>NX:WDHELPERS" not in s:
        s += WIKI_ADD
        open(p, "w", encoding="utf-8").write(s)
    q = os.path.join(SCR, "nxchain.py")
    open(q, "w", encoding="utf-8").write(CHAIN)
    for f in (p, q):
        subprocess.run([sys.executable, "-m", "py_compile", f], check=True)
        subprocess.run([sys.executable, os.path.join(SCR, "nxname.py"), f], check=True)
    import importlib; importlib.reload(nxwiki)
    import nxchain; importlib.reload(nxchain)
    t = [("三重県", "多気郡明和町"), ("茨城県", "東茨城郡茨城町"), ("埼玉県", "比企郡小川町"),
         ("福島県", "南会津郡南会津町"), ("茨城県", "筑西市")]
    res, why = nxchain.resolve(t, ua=UA)
    for k in t:
        print("    %-8s %-12s -> %-6s %s" % (k[0], k[1], res.get(k, "-"), why.get(k, "")))
    assert res.get(("三重県", "多気郡明和町")) == "三重県", "郡剥がしが効いていない"
    print("  自己検証 OK (郡名込みでも解決)")
    return res

# 18件(step71確定7 + step72第二軸11)
FIX = [("Q11267368","さいすくい","三重県","大分県","WD"),("Q11455990","富士山御神火まつり","山梨県","静岡県","WD"),
 ("Q11556000","津屋崎祇園山笠","三重県","福岡県","WD"),("Q28691756","滝山寺鬼まつり","山形県","愛知県","WD"),
 ("Q38277378","日本幻野祭","福岡県","千葉県","WD"),("Q56010148","猪名川花火大会","京都府","兵庫県","WD"),
 ("Q64539503","鳥羽の火祭り","三重県","愛知県","WD"),("Q11361495","下館祇園祭","京都府","茨城県","CITY"),
 ("Q11408464","南越谷阿波踊り","徳島県","埼玉県","CITY"),("Q11425142","坂戸よさこい","高知県","埼玉県","CITY"),
 ("Q11463659","小見川祇園祭","京都府","千葉県","CITY"),("Q11465151","尾島ねぷた","青森県","群馬県","CITY"),
 ("Q11466745","山口天神祭","大阪府","山口県","CITY"),("Q11467395","山口祇園祭","京都府","山口県","CITY"),
 ("Q11538304","桶川祇園祭","京都府","埼玉県","CITY"),("Q11549648","氷見祇園祭","京都府","富山県","CITY"),
 ("Q11558195","浦安三社祭","東京都","千葉県","CITY"),("Q30928431","萩姫まつり","山口県","福島県","CITY")]
def s2():
    con = sqlite3.connect(DB); n = 0
    for qid, lab, old, new, src in FIX:
        cur = con.execute("select prefecture from festivals where qid=?", (qid,)).fetchone()
        if not cur or cur[0] != old:
            print("  [skip] %s 現在=%s 期待=%s" % (qid, cur and cur[0], old)); continue
        if APPLY:
            c = con.execute("update festivals set prefecture=?, updated_at=? where qid=? and prefecture=?",
                            (new, TS, qid, old))
            if c.rowcount != 1: raise RuntimeError("CAS %s" % qid)
            nxledger.put(con, tkey="pref|%s" % qid, qid=qid, ja=lab, old=old, new=new, verdict="apply",
                         decided_at=TS, src="step73/PREF_" + src,
                         note=("%s による二系統確認。旧値 %s は祭名から本家所在地を引き当てた推測誤り。"
                               % ("jawiki導入部+Wikidata P131" if src == "WD" else
                                  "jawiki導入部+市区町村の独立照会(CITYCHAIN)", old))[:600],
                         url="https://www.wikidata.org/wiki/" + qid)
        n += 1
    if APPLY: con.commit()
    print("  訂正 %d / %d 件 (APPLY=%s)" % (n, len(FIX), APPLY))
    con.close(); return n

# 残り hold の再挑戦
REST = [("Q11381253","会津田島祇園祭","京都府"),("Q11437490","大淀祇園祭","京都府"),
        ("Q11464484","小鶴祇園祭","京都府"),("Q21652662","小川町七夕まつり","群馬県"),
        ("Q1636567","神戸ルミナリエ","兵庫県")]
CITY = re.compile("(" + "|".join(sorted(nxwiki.PREFS, key=len, reverse=True)) + ")"
                  r"([\u4e00-\u9fa5\u3040-\u30ff]{1,7}?[市区町村])")
def s3():
    import nxchain
    con = sqlite3.connect(DB)
    rows = con.execute("select qid,label_ja,wikipedia_ja,prefecture from festivals where qid in (%s)"
                       % ",".join("?" * len(REST)), [r[0] for r in REST]).fetchall()
    tmap = {nxwiki.title_of(w, l): (q, l, p) for q, l, w, p in rows}
    ext = nxwiki.extracts(list(tmap), intro=True, ua=UA)
    pairs, meta = [], {}
    for t, (q, l, dbp) in tmap.items():
        m = CITY.search(ext.get(t, ""))
        if m:
            pairs.append((m.group(1), m.group(2))); meta[q] = (l, dbp, m.group(1), m.group(2), t)
        else:
            meta[q] = (l, dbp, None, None, t)
            print("  %-11s %-18s 市区町村を抽出できず -> DB値 %s を維持" % (q, (l or "")[:18], dbp))
    res, why = nxchain.resolve(list(dict.fromkeys(pairs)), ua=UA) if pairs else ({}, {})
    out = []
    for q, (l, dbp, pf, city, t) in meta.items():
        if not city: continue
        got = res.get((pf, city))
        v = "confirmed2" if got and got == pf and got != dbp else ("db_ok" if got == dbp else "hold")
        print("  %-11s %-18s DB=%-5s 本文=%-5s 市=%-10s 帰属=%-5s %s"
              % (q, (l or "")[:18], dbp, pf, city, got or "-", v))
        if v == "confirmed2":
            out.append((q, l, dbp, got, t, pf, city, why.get((pf, city), "")))
    for q, l, old, new, t, pf, city, w in out:
        if APPLY:
            c = con.execute("update festivals set prefecture=?, updated_at=? where qid=? and prefecture=?",
                            (new, TS, q, old))
            if c.rowcount != 1: raise RuntimeError("CAS %s" % q)
            nxledger.put(con, tkey="pref|%s" % q, qid=q, ja=l, old=old, new=new, verdict="apply",
                         decided_at=TS, src="step73/CITYCHAIN_v2",
                         note=("jawiki導入部『%s%s』。郡名を剥がした照会経路 %s で帰属県 %s を確認。旧値 %s は推測誤り。"
                               % (pf, city, w, new, old))[:600],
                         url="https://ja.wikipedia.org/wiki/" + urllib.parse.quote(t.replace(" ", "_")))
    if APPLY: con.commit()
    print("  追加確定 %d 件" % len(out))
    con.close(); return [o[0] for o in out]

def s4():
    con = sqlite3.connect(DB)
    print("  訂正後の verdict_ledger(pref):")
    for r in con.execute("select tkey,old,new,src from verdict_ledger where tkey like 'pref|%' order by tkey"):
        print("    %-18s %-5s -> %-5s %s" % r)
    print("  祇園×京都府 の残存 = %d 件"
          % con.execute("select count(*) from festivals where label_ja like '%祇園%' and prefecture='京都府'").fetchone()[0])
    for r in con.execute("select qid,label_ja,prefecture from festivals where label_ja like '%祇園%' and prefecture='京都府'"):
        print("    %-11s %-20s %s" % r)
    p = subprocess.run([sys.executable, os.path.join(SCR, "nxcheck.py")], cwd=ROOT, capture_output=True, text=True)
    print("  nxcheck rc=%d" % p.returncode)
    con.close(); return {"rc": p.returncode}

KEY = "## [CITYCHAIN_V2_PREF_20260811]"
BLOCK = KEY + """
CITYCHAIN_v2: 郡名込み(多気郡明和町/東茨城郡茨城町/比企郡小川町)は jawiki 記事に当たらない。
郡を剥がした名、県名を括弧で付した曖昧回避名、県名連結名を順に試して解決する。
汚染率の訂正: loc_qid 空 12/463(2.6%) 対 loc_qid あり 6/331(1.8%)。偏りはあるが
「58%が推測で汚染」という当初の見立ては誤り。実態は全体で2〜3%の誤り率であり、
大半の prefecture は正しい。仮説は数字が出た時点で下方修正すること。
確定18件はすべて祭名から本家所在地を引き当てた型(祇園→京都府、ねぷた→青森県、
よさこい→高知県、阿波踊り→徳島県、天神→大阪府、三社祭→東京都)。
神戸ルミナリエは導入部に市区町村表記がなく DB 値(兵庫県)が正しい。抽出不能は現状維持とする。
"""
def s5():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY)); return {"ok": True}

sec("backup", s0); sec("chain", s1); sec("fix18", s2); sec("rest", s3); sec("verify", s4); sec("doc", s5)
j = os.path.join(SNAP, "step73_" + TS + ".json")
def _jsonable(o):
    if isinstance(o, dict):
        return {("|".join(map(str, k)) if isinstance(k, tuple) else str(k)): _jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_jsonable(x) for x in o]
    return o
try:
    open(j, "w", encoding="utf-8").write(json.dumps(_jsonable(R), ensure_ascii=False, indent=1, default=str))
except Exception as _e:
    open(j + ".txt", "w", encoding="utf-8").write(repr(R))
    print("[warn] JSON化に失敗、生の repr を保存: %r" % (_e,))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
