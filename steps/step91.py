#!/usr/bin/env python3
"""step91: 公開接続 - サイト向けJSON生成とAstroページ雛形"""
import os,sys,json,sqlite3,datetime,shutil,re
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SITE=os.path.join(ROOT,'site'); OUT=os.path.join(ROOT,'out')
APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
sys.path.insert(0,os.path.join(ROOT,'scripts'))

print('===== s1 calendar.json の構造 =====')
raw=json.load(open(os.path.join(OUT,'calendar.json'),encoding='utf-8'))
def shape(o,d=0):
    if isinstance(o,dict): return '{'+', '.join(k+':'+shape(v,d+1) for k,v in list(o.items())[:8])+'}' if d<2 else 'dict'
    if isinstance(o,list): return '['+str(len(o))+'x '+(shape(o[0],d+1) if o else '')+']'
    return type(o).__name__
print('  ',shape(raw)[:600])

print('===== s2 サイト向けJSON =====')
def pick(o):
    if isinstance(o,list): return o
    for k in ('next','next_n','upcoming','items','rows','list'):
        if isinstance(o,dict) and isinstance(o.get(k),list): return o[k]
    return []
nxt=pick(raw); ann=[]
if isinstance(raw,dict):
    for k in ('annual','year','all'):
        if isinstance(raw.get(k),list): ann=raw[k]; break
print('  next',len(nxt),'件 / annual',len(ann),'件')
if nxt: print('  1件目のキー:',list(nxt[0].keys()) if isinstance(nxt[0],dict) else type(nxt[0]).__name__)
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
meta={r['qid']:dict(r) for r in con.execute("select qid,label_ja,prefecture,slug_ja,wikipedia_ja,image_url,status from festivals")}
def conv(it):
    if not isinstance(it,dict): return None
    q=it.get('qid') or it.get('id') or ''
    m=meta.get(q,{})
    return {'qid':q,'name':it.get('name') or it.get('label_ja') or m.get('label_ja') or '',
            'pref':m.get('prefecture') or it.get('pref') or '',
            'date':it.get('date') or it.get('date_disp') or it.get('day') or '',
            'start':it.get('start') or '', 'end':it.get('end') or '',
            'rule':it.get('rule') or it.get('date_rule') or '',
            'slug':m.get('slug_ja') or '', 'wiki':m.get('wikipedia_ja') or '','status':m.get('status') or ''}
site={'generated':datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
      'next':[c for c in map(conv,nxt) if c],'annual':[c for c in map(conv,ann) if c]}
ok=sum(1 for c in site['next'] if c['qid'] and c['name'])
print('  変換 next',len(site['next']),'/ qid+名あり',ok,'/ 記事あり',sum(1 for c in site['next'] if c['slug']))
if site['next'][:2]: print('  例:',json.dumps(site['next'][0],ensure_ascii=False)[:180])
if ok==0: print('  [NG] qid が取れない → ページ生成を中止'); sys.exit(1)
json.dump(site,open(os.path.join(OUT,'site_calendar.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('[OK] out/site_calendar.json')

print('===== s3 訂正履歴JSON =====')
rows=[dict(r) for r in con.execute("""select tkey,verdict,note,url,qid,ja,old,new,decided_at from verdict_ledger
 where tkey like 'PREF%' or tkey like 'DATEGUARD%' or tkey like 'DATEFIX%' or tkey like 'canon|%' or tkey like 'pref|%'
 order by decided_at desc""")]
json.dump({'generated':site['generated'],'rows':rows},open(os.path.join(OUT,'site_corrections.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('  台帳',len(rows),'件 → out/site_corrections.json')
con.close()

print('===== s4 BaseLayout の作法 =====')
c=open(os.path.join(SITE,'src/pages/contact.astro'),encoding='utf-8').read()
m=re.search(r'<BaseLayout([^>]*)>',c)
imp=[l for l in c.split('---')[1].splitlines() if 'import' in l]
print('  import:',imp); print('  tag:',(m.group(0) if m else '(不明)')[:160])
