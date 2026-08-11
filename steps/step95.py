# -*- coding: utf-8 -*-
# step95: 全文抽出パイロット（30件・DB書込なし）
import sys, os, json, sqlite3, urllib.parse, re, collections
sys.path.insert(0, os.path.expanduser('~/nipponexus/scripts'))
import nxwiki, nxdate, nxguard4
H = os.path.expanduser('~/nipponexus')
CD = H + '/data/wikitext'
db = sqlite3.connect(H + '/data/sqlite/nipponexus.db')
db.row_factory = sqlite3.Row
N = int(os.environ.get('NX_N', '30'))
rows = db.execute("""select qid,label_ja,wikipedia_ja from festivals
 where (date_rule is null or date_rule='') and wikipedia_ja<>''
 order by random() limit ?""", (N,)).fetchall()
print('対象 %d 件' % len(rows))
need, title_of = [], {}
for r in rows:
    t = urllib.parse.unquote(r['wikipedia_ja'].rsplit('/wiki/', 1)[-1]).replace('_', ' ')
    title_of[r['qid']] = t
    if not os.path.exists('%s/%s.txt' % (CD, r['qid'])): need.append(t)
print('取得必要 %d 件（キャッシュ済 %d）' % (len(need), len(rows) - len(need)))
if need:
    got = nxwiki.extracts(need, intro=False, sleep=1.0, verbose=False)
    n2q = {v: k for k, v in title_of.items()}
    for t, txt in got.items():
        q = n2q.get(t)
        if q and txt:
            open('%s/%s.txt' % (CD, q), 'w', encoding='utf-8').write(txt)
print('--- 本文長 ---')
ln = []
for r in rows:
    p = '%s/%s.txt' % (CD, r['qid'])
    ln.append(len(open(p, encoding='utf-8').read()) if os.path.exists(p) else 0)
print('  取得成功 %d / 空 %d / 中央値 %d字 / 最大 %d字'
      % (sum(1 for x in ln if x), sum(1 for x in ln if not x), sorted(ln)[len(ln)//2], max(ln)))
# 抽出
first = True
hit, tally, samples = 0, collections.Counter(), []
for r in rows:
    p = '%s/%s.txt' % (CD, r['qid'])
    if not os.path.exists(p): continue
    txt = open(p, encoding='utf-8').read()
    res = nxdate.parse(txt)
    if first and res:
        print('--- parse 戻り値の形 ---'); print(' ', type(res).__name__, json.dumps(res, ensure_ascii=False)[:300]); first = False
    if not res: continue
    raw = res.get('raw') if isinstance(res, dict) else None
    ctx = res.get('ctx') if isinstance(res, dict) else None
    if not raw: continue
    hit += 1
    g = nxguard4.classify(r['label_ja'], raw, ctx or '')
    gk = g[0] if isinstance(g, (tuple, list)) else g
    tally[gk] += 1
    if len(samples) < 14:
        samples.append((gk, r['label_ja'], str(raw)[:26], re.sub(r'\s+', ' ', str(ctx))[:52]))
print('--- 結果 ---')
print('  抽出 %d / %d 件 (%.0f%%)' % (hit, len(rows), 100.0*hit/max(1, len(rows))))
print('  ガード内訳:', dict(tally))
print('--- 標本 ---')
for s in samples: print('  [%s] %s | %s | %s' % s)
