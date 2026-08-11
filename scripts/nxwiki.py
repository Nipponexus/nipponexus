# -*- coding: utf-8 -*-
# WIKI_v2 : jawiki 取得。v1 の欠陥 = exlimit 未指定。
# MediaWiki の prop=extracts は exintro 無し(全文)だと exlimit が 1 に制限され、
# 20件バッチで投げると先頭1件しか返らない。全文取得は必ず1件ずつ。
import json, time, sys, urllib.request, urllib.parse
UA_DEFAULT = "nipponexus/1.0 (contact: yuki.shiori@nexus-ds.jp)"

PREFS = ["\u5317\u6d77\u9053","\u9752\u68ee\u770c","\u5ca9\u624b\u770c","\u5bae\u57ce\u770c","\u79cb\u7530\u770c",
"\u5c71\u5f62\u770c","\u798f\u5cf6\u770c","\u8328\u57ce\u770c","\u6803\u6728\u770c","\u7fa4\u99ac\u770c",
"\u57fc\u7389\u770c","\u5343\u8449\u770c","\u6771\u4eac\u90fd","\u795e\u5948\u5ddd\u770c","\u65b0\u6f5f\u770c",
"\u5bcc\u5c71\u770c","\u77f3\u5ddd\u770c","\u798f\u4e95\u770c","\u5c71\u68a8\u770c","\u9577\u91ce\u770c",
"\u5c90\u961c\u770c","\u9759\u5ca1\u770c","\u611b\u77e5\u770c","\u4e09\u91cd\u770c","\u6ecb\u8cc0\u770c",
"\u4eac\u90fd\u5e9c","\u5927\u962a\u5e9c","\u5175\u5eab\u770c","\u5948\u826f\u770c","\u548c\u6b4c\u5c71\u770c",
"\u9ce5\u53d6\u770c","\u5cf6\u6839\u770c","\u5ca1\u5c71\u770c","\u5e83\u5cf6\u770c","\u5c71\u53e3\u770c",
"\u5fb3\u5cf6\u770c","\u9999\u5ddd\u770c","\u611b\u5a9b\u770c","\u9ad8\u77e5\u770c","\u798f\u5ca1\u770c",
"\u4f50\u8cc0\u770c","\u9577\u5d0e\u770c","\u718a\u672c\u770c","\u5927\u5206\u770c","\u5bae\u5d0e\u770c",
"\u9e7f\u5150\u5cf6\u770c","\u6c96\u7e04\u770c"]
_PREF_RX = None
def pref_findall(text):
    """正規表現の総称パターンは『年千葉県』のような誤検出を生む。47固定リストで走査する。"""
    global _PREF_RX
    import re
    if _PREF_RX is None:
        _PREF_RX = re.compile("|".join(sorted(PREFS, key=len, reverse=True)))
    return list(dict.fromkeys(_PREF_RX.findall(text or "")))

def api(host, params, ua=None, timeout=45):
    url = "https://%s/w/api.php?%s" % (host, urllib.parse.urlencode(params))
    rq = urllib.request.Request(url, headers={"User-Agent": ua or UA_DEFAULT})
    with urllib.request.urlopen(rq, timeout=timeout) as f:
        return json.loads(f.read().decode("utf-8"))

def extracts(titles, intro=True, ua=None, sleep=1.0, verbose=True):
    out = {t: "" for t in titles}
    batch = 20 if intro else 1
    for i in range(0, len(titles), batch):
        chunk = titles[i:i + batch]
        p = {"action": "query", "format": "json", "prop": "extracts", "explaintext": 1,
             "redirects": 1, "exlimit": (20 if intro else 1), "titles": "|".join(chunk)}
        if intro:
            p["exintro"] = 1
        try:
            d = api("ja.wikipedia.org", p, ua)
        except Exception as e:
            if verbose: print("  [warn] %r" % e)
            time.sleep(2); continue
        q = d.get("query", {})
        by = {pg.get("title"): (pg.get("extract") or "") for pg in q.get("pages", {}).values()}
        alias = {}
        for r in (q.get("redirects") or []): alias[r["from"]] = r["to"]
        for nz in (q.get("normalized") or []): alias[nz["from"]] = nz["to"]
        for t in chunk:
            cur, k = t, 0
            while cur in alias and k < 5:
                cur = alias[cur]; k += 1
            out[t] = by.get(cur, by.get(t, ""))
        if verbose:
            sys.stdout.write("\r  取得 %d/%d" % (min(i + batch, len(titles)), len(titles))); sys.stdout.flush()
        time.sleep(sleep)
    if verbose: print()
    return out

def title_of(url, label):
    if url and "/" in url:
        return urllib.parse.unquote(url.rstrip("/").split("/")[-1]).replace("_", " ")
    return url or label

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
