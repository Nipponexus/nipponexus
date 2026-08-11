#!/usr/bin/env python3
"""step90: 都道府県の空欄を本文から復元（一意一致のみ）"""
import os,json,shutil,sqlite3,datetime
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SNAP=os.path.join(ROOT,'snapshots'); APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
TS=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'); os.makedirs(SNAP,exist_ok=True)
P=['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県','新潟県','富山県','石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県','鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県']
shutil.copy2(DB,os.path.join(SNAP,'db_'+TS+'.db')); print('[OK] backup')
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
cols={c['name'] for c in con.execute('pragma table_info(verdict_ledger)')}
rows=con.execute("select qid,label_ja,prefecture,location_label_ja,description_ja,date_rule_src,wikipedia_ja from festivals where ifnull(date_rule,'')<>'' and ifnull(prefecture,'')=''").fetchall()
rec=[];amb=[];non=[]
for r in rows:
    ev=[('所在地',r['location_label_ja'] or ''),('説明',r['description_ja'] or ''),('本文',(r['date_rule_src'] or '')[:200])]
    hits=None;via=''
    for tag,txt in ev:
        h={p for p in P if p in txt}
        if len(h)==1 and hits is None: hits=h.copy(); via=tag
        elif len(h)>1 and hits is None: hits=h.copy(); via=tag+'(複数)'
    allh={p for _,t in ev for p in P if p in t}
    if len(allh)==1: rec.append((r['qid'],r['label_ja'],allh.pop(),via or '本文',r['wikipedia_ja']))
    elif len(allh)>1: amb.append((r['qid'],r['label_ja'],sorted(allh)))
    else: non.append((r['qid'],r['label_ja']))
print('  空欄',len(rows),'/ 一意復元',len(rec),'/ 複数候補',len(amb),'/ 手掛かりなし',len(non))
print('  ── 復元一覧 ──')
for q,ja,p,via,_ in rec: print('   ',q,ja[:22],'->',p,'('+via+')')
print('  ── 複数候補（人手）──')
for q,ja,h in amb[:12]: print('   ',q,ja[:22],h)
print('  ── 手掛かりなし ──')
for q,ja in non[:12]: print('   ',q,ja[:22])
if APPLY:
    n=0
    for q,ja,p,via,wp in rec:
        c=con.execute("update festivals set prefecture=? where qid=? and ifnull(prefecture,'')=''",(p,q)).rowcount
        if c:
            n+=1
            d={'tkey':'PREFFILL['+q+']','verdict':'apply','note':'記事の'+via+'から一意に特定','url':wp or '','qid':q,'ja':ja,
               'old':'（記録なし）','new':p,'decided_at':datetime.datetime.now().isoformat(timespec='seconds'),'src':'step90'}
            d={k:v for k,v in d.items() if k in cols}
            con.execute('delete from verdict_ledger where tkey=?',('PREFFILL['+q+']',))
            con.execute('insert into verdict_ledger('+','.join(d)+') values('+','.join(['?']*len(d))+')',list(d.values()))
    con.commit(); print('[OK] apply',n,'件を補完')
else: print('[--] dry-run')
b=con.execute("select count(*) from festivals where ifnull(date_guard,'')='ok' and ifnull(date_rule,'')<>'' and ifnull(prefecture,'')=''").fetchone()[0]
print('  掲載可のうち県名空欄 =',b,'件')
con.close()
json.dump({'apply':APPLY,'rec':len(rec),'amb':len(amb),'non':len(non)},open(os.path.join(SNAP,'step90_'+TS+'.json'),'w'),ensure_ascii=False)
print('APPLY='+str(APPLY))
