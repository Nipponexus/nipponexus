# -*- coding: utf-8 -*-
# step97: 全文抽出 本走査（643件）
import os,sys,re,sqlite3,json,time,shutil,collections,urllib.parse,datetime
sys.path.insert(0,os.path.expanduser('~/nipponexus/scripts'))
import nxwiki,nxdate,nxguard4
H=os.path.expanduser('~/nipponexus'); CD=H+'/data/wikitext'; os.makedirs(CD,exist_ok=True)
APPLY=os.environ.get('NX_APPLY')=='1'
DBP=H+'/data/sqlite/nipponexus.db'
if APPLY:
    b=H+'/snapshots/db_step97_%s.db'%datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    shutil.copy(DBP,b); print('backup',os.path.basename(b))
db=sqlite3.connect(DBP); db.row_factory=sqlite3.Row
ANN=re.compile(r'(毎年|例年|恒例)')
NOW=re.compile(r'(行われる|開催される|催される|実施される|開かれる)')
YEAR=re.compile(r'(1[89]\d\d年|20\d\d年|平成\d+年|令和\d+年|昭和\d+年|大正\d+年|明治\d+年|同年|の場合|予備日|順延|台風|中止|初回|第\d+回|であった|していた|かつて|までは|異なり|例外)')
FUZZY=re.compile(r'(過ぎ|頃|ころ|ごろ|前後|付近|中旬|初旬|下旬|以降|近い|あたり)')
def select(text):
    c=[]
    for kind,rx in nxdate.PATS:
        for m in rx.finditer(text): c.append((m.start(),m.end(),kind,m.group(0)))
    c.sort()
    for st,en,kind,raw in c:
        back=text[max(0,st-45):st]; fwd=text[en:en+30]; w=back+raw+fwd
        if YEAR.search(w): continue
        if FUZZY.search(back[-12:]) or FUZZY.search(fwd[:8]): continue
        ann=bool(ANN.search(back)); dow=kind in('nth_dow','last_dow') and bool(NOW.search(fwd))
        if not(ann or dow): continue
        r=nxdate.parse(text[st:en+2]) or nxdate.parse(raw)
        if not r: continue
        r['pos']=st; r['ctx']=w.replace('\n',' ').strip(); return r
    return None
rows=db.execute("""select qid,label_ja,wikipedia_ja from festivals
 where (date_rule is null or date_rule='') and wikipedia_ja<>'' order by qid""").fetchall()
print('対象 %d 件'%len(rows)); t0=time.time(); fetched=0
for i,r in enumerate(rows):
    p='%s/%s.txt'%(CD,r['qid'])
    if os.path.exists(p): continue
    t=urllib.parse.unquote(r['wikipedia_ja'].rsplit('/wiki/',1)[-1]).replace('_',' ')
    try:
        g=nxwiki.extracts([t],intro=False,sleep=0.0,verbose=False)
        open(p,'w',encoding='utf-8').write(g.get(t,'') or ''); fetched+=1
    except Exception as e:
        open(p,'w',encoding='utf-8').write(''); print(' [warn]',t[:20],repr(e)[:40])
    time.sleep(0.8)
    if fetched and fetched%100==0: print('  取得 %d 件 / %.0f秒'%(fetched,time.time()-t0))
print('取得 %d 件 / 所要 %.0f 秒'%(fetched,time.time()-t0))
tally=collections.Counter(); hits=[]
for r in rows:
    p='%s/%s.txt'%(CD,r['qid'])
    if not os.path.exists(p): continue
    t=open(p,encoding='utf-8').read()
    if not t: continue
    s=select(t)
    if not s: continue
    d=nxdate.describe(s)
    if not d: continue
    g=nxguard4.classify(r['label_ja'],d,s['ctx']); gk=g[0] if isinstance(g,(tuple,list)) else g
    tally[gk]+=1; hits.append((r['qid'],r['label_ja'],d,s,gk))
print('抽出 %d 件 (%.0f%%) 内訳 %s'%(len(hits),100.0*len(hits)/len(rows),dict(tally)))
print('--- 標本20 ---')
for q,l,d,s,gk in hits[:20]: print('  [%-7s] %-22s %s'%(gk,l[:22],d))
if APPLY:
    for q,l,d,s,gk in hits:
        db.execute("""update festivals set date_rule=?,date_rule_json=?,date_rule_src=?,
          date_verified='rule_only',date_guard=?,date_guard_note='全文抽出(step97)'
          where qid=? and (date_rule is null or date_rule='')""",
          (d,json.dumps(s,ensure_ascii=False),s['ctx'],gk,q))
        db.execute("insert into verdict_ledger(tkey,verdict,note,qid) values(?,?,?,?)",
          ('DATERULE[%s]'%q,gk,'全文から抽出: '+d,q))
    db.commit(); print('保存 %d 件'%len(hits))
print('APPLY=%s'%APPLY)
