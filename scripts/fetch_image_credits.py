#!/usr/bin/env python3
"""Commons から撮影者・ライセンスを取得し3列に格納。image_url を https 化。"""
import html, json, re, sqlite3, time, urllib.parse, urllib.request

DB  = "data/sqlite/nipponexus.db"
API = "https://commons.wikimedia.org/w/api.php"
UA  = "Nipponexus/1.0 (https://nipponexus.com) python-urllib"

conn = sqlite3.connect(DB)
cur  = conn.cursor()

cols = {r[1] for r in cur.execute("PRAGMA table_info(festivals)")}
for c in ("image_author", "image_license", "image_credit_url"):
    if c not in cols:
        cur.execute("ALTER TABLE festivals ADD COLUMN " + c + " TEXT")
        print("[ADD] " + c)
conn.commit()

urls = [r[0] for r in cur.execute(
    "SELECT DISTINCT image_url FROM festivals "
    "WHERE image_url IS NOT NULL AND image_url<>''")]
print("[INFO] unique image_url = %d" % len(urls))

TAG = re.compile(r"<[^>]+>")
def clean(v):
    if not v:
        return ""
    return re.sub(r"\s+", " ", html.unescape(TAG.sub("", v))).strip()

titles = {}
for u in urls:
    m = re.search(r"Special:FilePath/(.+)$", u)
    if not m:
        print("[SKIP] 想定外URL: " + u)
        continue
    t = "File:" + urllib.parse.unquote(m.group(1)).replace("_", " ")
    titles.setdefault(t, []).append(u)

meta, missing = {}, []
keys = list(titles)
for i in range(0, len(keys), 50):
    chunk  = keys[i:i + 50]
    params = {
        "action": "query", "format": "json", "formatversion": "2",
        "titles": "|".join(chunk), "prop": "imageinfo",
        "iiprop": "extmetadata", "redirects": "1",
        "iiextmetadatafilter":
            "Artist|Credit|LicenseShortName|UsageTerms|LicenseUrl|AttributionRequired",
    }
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params),
                                 headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        q = json.load(r).get("query", {})

    fwd = {t: t for t in chunk}
    for n_ in q.get("normalized", []):
        for k, v in list(fwd.items()):
            if v == n_["from"]:
                fwd[k] = n_["to"]
    for d in q.get("redirects", []):
        for k, v in list(fwd.items()):
            if v == d["from"]:
                fwd[k] = d["to"]
    back = {v: k for k, v in fwd.items()}

    for p in q.get("pages", []):
        orig = back.get(p.get("title"), p.get("title"))
        ii   = p.get("imageinfo")
        if not ii:
            missing.append(orig)
            continue
        em     = ii[0].get("extmetadata", {})
        author = clean(em.get("Artist", {}).get("value")) \
                 or clean(em.get("Credit", {}).get("value")) or "不明"
        lic    = clean(em.get("LicenseShortName", {}).get("value")) \
                 or clean(em.get("UsageTerms", {}).get("value")) or "不明"
        page   = "https://commons.wikimedia.org/wiki/" + \
                 urllib.parse.quote(p["title"].replace(" ", "_"), safe=":/")
        meta[orig] = (author[:200], lic, page)
    print("[API] %d/%d" % (min(i + 50, len(keys)), len(keys)))
    time.sleep(0.3)

n = 0
for t, us in titles.items():
    if t not in meta:
        continue
    a, l, c = meta[t]
    for u in us:
        cur.execute(
            "UPDATE festivals SET image_author=?, image_license=?, "
            "image_credit_url=?, image_url=? WHERE image_url=?",
            (a, l, c, u.replace("http://", "https://", 1), u))
        n += cur.rowcount
conn.commit()

print("\n[DONE] 更新 %d 行 / 成功 %d 件 / 失敗 %d 件" % (n, len(meta), len(missing)))
for t in missing[:10]:
    print("  [MISS] " + t)
print("\n--- ライセンス内訳 ---")
for lic, c in cur.execute(
        "SELECT COALESCE(image_license,'(null)'), count(*) FROM festivals "
        "WHERE image_url<>'' GROUP BY 1 ORDER BY 2 DESC"):
    print("  %4d  %s" % (c, lic))
conn.close()
