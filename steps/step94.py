#!/usr/bin/env python3
"""step94: 非祭り項目の除外・範囲解析の訂正・公開経路の接続"""
import os,sys,re,json,shutil,sqlite3,datetime,subprocess
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SNAP=os.path.join(ROOT,'snapshots'); OUT=os.path.join(ROOT,'out'); SCR=os.path.join(ROOT,'scripts')
APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
TS=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'); sys.path.insert(0,SCR)
shutil.copy2(DB,os.path.join(SNAP,'db_'+TS+'.db')); print('[OK] backup')
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
cols={c['name'] for c in con.execute('pragma table_info(verdict_ledger)')}
def led(tk,vd,note,url,qid,ja,old,new=''):
    d={'tkey':tk,'verdict':vd,'note':note,'url':url or '','qid':qid,'ja':ja,'old':old,'new':new,
       'decided_at':datetime.datetime.now().isoformat(timespec='seconds'),'src':'step94'}
    d={k:v for k,v in d.items() if k in cols}
    con.execute('delete from verdict_ledger where tkey=?',(tk,))
    con.execute('insert into verdict_ledger('+','.join(d)+') values('+','.join(['?']*len(d))+')',list(d.values()))

print('===== s1 除外対象 =====')
EX=[('Q11284866','記念日であり祭りではない'),('Q17209977','記念日であり祭りではない'),
    ('Q11638353','盆の風習の総称であり個別の祭りではない'),('Q11527721','祭りの参加団体（流）であり祭りではない'),
    ('Q60848673','記事内容がえびす講（年中行事の総称）でラベルと不一致'),
    ('Q24876853','地域一帯の火祭りの総称で開催日が一定でない')]
tgt=[]
for q,why in EX:
    r=con.execute("select qid,label_ja,date_rule,date_guard,wikipedia_ja from festivals where qid=?",(q,)).fetchone()
    if r: tgt.append((r,why)); print('   ',q,r['label_ja'],'|',r['date_rule'],'|',why)
    else: print('   skip',q)

print('===== s2 「N日間」の解析監査 =====')
try: import nxdate
except Exception as e: nxdate=None; print('  nxdate 未取得',e)
RE_D=re.compile(r'(\d{1,2})月(\d{1,2})日(?:から|〜|～)(\d+)日間')
fix=[]
for r in con.execute("select qid,label_ja,date_rule,date_rule_src,wikipedia_ja from festivals where ifnull(date_rule,'')<>'' and ifnull(date_rule_src,'') like '%日間%'"):
    m=RE_D.search((r['date_rule_src'] or '').translate(str.maketrans('０１２３４５６７８９','0123456789')))
    if not m: continue
    mo,dy,n=int(m.group(1)),int(m.group(2)),int(m.group(3))
    try: e=datetime.date(2026,mo,dy)+datetime.timedelta(days=n-1)
    except Exception: continue
    new='毎年%d月%d日〜%d月%d日'%(mo,dy,e.month,e.day)
    if new==r['date_rule']: print('   ok ',r['label_ja'],r['date_rule']); continue
    j=None
    if nxdate:
        try:
            d=nxdate.parse(new)
            if not d or (hasattr(nxdate,'describe') and nxdate.describe(d)!=new):
                print('   skip',r['label_ja'],'describe不一致'); continue
            j=json.dumps(d,ensure_ascii=False,default=str)
        except Exception as ex: print('   skip',r['label_ja'],ex); continue
    fix.append((r['qid'],r['label_ja'],r['date_rule'],new,j,r['wikipedia_ja']))
    print('   訂正',r['qid'],r['label_ja'],r['date_rule'],'->',new)
print('  訂正候補',len(fix),'件')

if APPLY:
    for r,why in tgt:
        con.execute("update festivals set date_guard='concept',date_guard_note=? where qid=?",(why,r['qid']))
        led('DATEGUARD['+r['qid']+']','concept',why,r['wikipedia_ja'],r['qid'],r['label_ja'],r['date_rule'])
    for q,ja,old,new,j,wp in fix:
        if j: con.execute("update festivals set date_rule=?,date_rule_json=?,date_guard='ok',date_guard_note=? where qid=?",(new,j,'「N日間」の記述から終了日を算出',q))
        else: con.execute("update festivals set date_rule=?,date_guard='ok',date_guard_note=? where qid=?",(new,'「N日間」の記述から終了日を算出',q))
        led('DATEFIX['+q+']','apply','根拠文の「'+old.replace('毎年','')+'」を「N日間」の記述から訂正',wp,q,ja,old,new)
    con.commit(); print('[OK] apply 除外',len(tgt),'訂正',len(fix))
else: print('[--] dry-run')
print('  掲載可',con.execute("select count(*) from festivals where ifnull(date_guard,'')='ok' and ifnull(date_rule,'')<>''").fetchone()[0],'件')
con.close()

print('===== s3 nightly_rebuild.sh の組み替え =====')
NB='''#!/bin/bash
# Nipponexus nightly: 生成 -> ダンプ -> 差分があれば commit -> push
set -e
cd ~/nipponexus
LOG="$HOME/.openclaw/logs/nipponexus_nightly.log"
mkdir -p "$(dirname "$LOG")"
echo "===== $(date '+%F %T') nightly start =====" >> "$LOG"

/usr/bin/python3 steps/daily_cal.py >> "$LOG" 2>&1
/usr/bin/python3 steps/step92.py   >> "$LOG" 2>&1
/usr/bin/python3 scripts/dump_festivals.py >> "$LOG" 2>&1

T="data/festivals_dump.sql out/site_calendar.json out/site_corrections.json"
CH=0
git diff --quiet -- $T || CH=1
UP=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
if [ "$CH" = "0" ] && [ "$UP" = "0" ]; then
  echo "[INFO] no changes, skip push" >> "$LOG"; exit 0
fi
if [ "$CH" = "1" ]; then
  git add $T
  git commit -m "chore: nightly update ($(date '+%F'))" >> "$LOG" 2>&1
fi
source ~/.openclaw/.env
git push "https://${GITHUB_TOKEN_NIPPONEXUS}@github.com/Nipponexus/nipponexus.git" main >> "$LOG" 2>&1
echo "[OK] pushed" >> "$LOG"
'''
p=os.path.join(SCR,'nightly_rebuild.sh')
if APPLY:
    shutil.copy2(p,p+'.bak'); open(p,'w').write(NB); os.chmod(p,0o755); print('[OK] 書き換え（.bak 退避）')
    cur=subprocess.run('crontab -l',shell=True,capture_output=True,text=True).stdout
    new='\n'.join([l for l in cur.splitlines() if 'daily_cal.py' not in l])
    subprocess.run('crontab -',shell=True,input=new+'\n',text=True); print('[OK] 4:35 の cron 行を撤去')
else: print('[--] dry-run（未変更）')
print(subprocess.run('crontab -l',shell=True,capture_output=True,text=True).stdout.strip())
