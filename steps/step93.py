#!/usr/bin/env python3
"""step93: 公開前の最終品質監査（日付逆転・非祭り項目・git追跡）"""
import os,sys,json,re,shutil,sqlite3,datetime,subprocess
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SNAP=os.path.join(ROOT,'snapshots'); OUT=os.path.join(ROOT,'out')
APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
TS=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'); os.makedirs(SNAP,exist_ok=True)
shutil.copy2(DB,os.path.join(SNAP,'db_'+TS+'.db')); print('[OK] backup')
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
cols={c['name'] for c in con.execute('pragma table_info(verdict_ledger)')}
def led(tk,vd,note,url,qid,ja,old):
    d={'tkey':tk,'verdict':vd,'note':note,'url':url or '','qid':qid,'ja':ja,'old':old,'new':'',
       'decided_at':datetime.datetime.now().isoformat(timespec='seconds'),'src':'step93'}
    d={k:v for k,v in d.items() if k in cols}
    con.execute('delete from verdict_ledger where tkey=?',(tk,))
    con.execute('insert into verdict_ledger('+','.join(d)+') values('+','.join(['?']*len(d))+')',list(d.values()))

print('===== s1 日付の逆転・異常 =====')
d=json.load(open(os.path.join(OUT,'site_calendar.json'),encoding='utf-8'))
rev=[r for r in d['annual'] if r['end'] and r['end']<r['start']]
print('  終了日<開始日 =',len(rev),'件')
for r in rev:
    s=con.execute("select date_rule_src from festivals where qid=?",(r['qid'],)).fetchone()
    print('   ',r['qid'],r['name'],'|',r['start'],'->',r['end'],'| 規則:',r['rule'])
    print('      src:',(s['date_rule_src'] or '')[:110].replace('\n',' ') if s else '')

print('===== s2 祭りでない項目 =====')
NOT_FEST={'アマチュア無線の日','漢字の日','迎え火','東流','送り火'}
RE_DAY=re.compile(r'(の日|記念日)$')
cand=[]
for r in con.execute("select qid,label_ja,date_rule,wikipedia_ja,date_rule_src from festivals where ifnull(date_guard,'')='ok' and ifnull(date_rule,'')<>''"):
    t=(r['label_ja'] or '').strip()
    if t in NOT_FEST or RE_DAY.search(t):
        cand.append((r['qid'],t,r['date_rule'],r['wikipedia_ja'],(r['date_rule_src'] or '')[:70].replace('\n',' ')))
print('  該当',len(cand),'件')
for c in cand: print('   ',c[0],c[1],'|',c[2],'|',c[4])

print('===== s3 季節が疑わしい行 =====')
for q in ('十日えびす','甲山廿日えびす','胡子講','松上げ','宮津祭'):
    r=con.execute("select qid,label_ja,date_rule,substr(replace(ifnull(date_rule_src,''),char(10),' '),1,90) s from festivals where label_ja=?",(q,)).fetchone()
    if r: print('   ',r['qid'],r['label_ja'],'|',r['date_rule'],'|',r['s'])

if APPLY:
    n=0
    for qid,ja,rule,wp,_ in cand:
        con.execute("update festivals set date_guard='concept',date_guard_note=? where qid=?",('記念日・行事の総称であり個別の祭りではない',qid)); n+=1
        led('DATEGUARD['+qid+']','concept','記念日・行事の総称であり個別の祭りではない',wp,qid,ja,rule)
    for r in rev:
        w=con.execute("select wikipedia_ja from festivals where qid=?",(r['qid'],)).fetchone()
        con.execute("update festivals set date_guard='conflict',date_guard_note=? where qid=?",('開催期間の解析に失敗（終了日が開始日より前）',r['qid'])); n+=1
        led('DATEGUARD['+r['qid']+']','conflict','開催期間の解析に失敗（終了日が開始日より前）',w['wikipedia_ja'] if w else '',r['qid'],r['name'],r['rule'])
    con.commit(); print('[OK] apply',n,'件を除外')
else: print('[--] dry-run')
print('  掲載可',con.execute("select count(*) from festivals where ifnull(date_guard,'')='ok' and ifnull(date_rule,'')<>''").fetchone()[0],'件')
con.close()

print('===== s4 git 追跡（公開の前提）=====')
def sh(c): return subprocess.run(c,shell=True,cwd=ROOT,capture_output=True,text=True).stdout.strip()
print('  out/ 追跡数:',len(sh('git ls-files out/').splitlines()))
print('  ignore判定:',sh('git check-ignore -v out/site_calendar.json') or '(対象外＝追跡可能)')
print('  site/追跡の新規:',sh('git status --porcelain site/src/pages/ site/src/components/') or '(なし)')
print('  ※ out/*.json を追跡しないと Cloudflare では 0 件表示になる')
