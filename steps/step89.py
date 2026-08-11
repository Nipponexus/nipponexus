#!/usr/bin/env python3
"""step89: 台帳の整合と都道府県欠損の監査（公開接続の前段）"""
import os,sys,json,shutil,sqlite3,datetime,subprocess,re
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SNAP=os.path.join(ROOT,'snapshots')
APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
TS=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'); os.makedirs(SNAP,exist_ok=True)
def sh(c):
    try: return subprocess.run(c,shell=True,cwd=ROOT,capture_output=True,text=True,timeout=30).stdout.strip()
    except Exception as e: return 'ERR '+str(e)

print('===== s1 リポジトリ全容 =====')
fs=[l for l in sh('git ls-files').splitlines() if not l.startswith(('steps/','snapshots/','logs/','scripts/'))]
print('  非scripts追跡ファイル',len(fs),'件 / scripts',len(sh('git ls-files scripts/').splitlines()),'件')
for f in fs[:40]: print('   ',f)
print('  --- .gitignore ---'); print('   '+sh('cat .gitignore').replace('\n','\n   '))
print('  --- サイト設定の有無 ---')
for f in ['package.json','astro.config.mjs','next.config.js','hugo.toml','config.yaml','wrangler.toml','_config.yml','index.html','public','src','web','site']:
    print('   ',f,'=',('あり' if os.path.exists(os.path.join(ROOT,f)) else '-'))
print('  --- 直近コミット ---'); print('   '+sh('git log --oneline -5').replace('\n','\n   '))
print('  --- 作業ツリーの差分 ---'); print('   '+(sh('git status --porcelain')[:600] or '(なし)').replace('\n','\n   '))

bk=os.path.join(SNAP,'db_'+TS+'.db'); shutil.copy2(DB,bk); print('[OK] backup',bk)
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
cols={c['name'] for c in con.execute('pragma table_info(verdict_ledger)')}

print('===== s2 台帳の整合 =====')
miss=con.execute("""select qid,label_ja,date_rule,date_guard,date_guard_note,wikipedia_ja from festivals
 where ifnull(date_rule,'')<>'' and ifnull(date_guard,'')<>'ok'
 and not exists(select 1 from verdict_ledger v where v.tkey='DATEGUARD['||qid||']')""").fetchall()
stale=con.execute("""select v.tkey from verdict_ledger v where v.tkey like 'DATEGUARD[%'
 and exists(select 1 from festivals f where 'DATEGUARD['||f.qid||']'=v.tkey and ifnull(f.date_guard,'')='ok')""").fetchall()
print('  台帳なしの非ok',len(miss),'件 / okなのに台帳あり',len(stale),'件')
for m in miss: print('   +',m['qid'],m['label_ja'][:18],m['date_guard'],'|',(m['date_guard_note'] or '')[:34])
NOTE={'lunar':'旧暦基準のため新暦換算が必要','concept':'暦の行事・まとめ記事で個別の開催日を持たない',
      'past':'抽出元が過去の開催日を述べている','cycle':'毎年開催ではない（隔年・数年に一度）',
      'review':'根拠が不十分なため保留','conflict':'日付抽出の競合（別枠で対応）'}
if APPLY:
    for m in miss:
        d={'tkey':'DATEGUARD['+m['qid']+']','verdict':m['date_guard'],'note':m['date_guard_note'] or NOTE.get(m['date_guard'],''),
           'url':m['wikipedia_ja'] or '','qid':m['qid'],'ja':m['label_ja'],'old':m['date_rule'],'new':'',
           'decided_at':datetime.datetime.now().isoformat(timespec='seconds'),'src':'step89'}
        d={k:v for k,v in d.items() if k in cols}
        con.execute('insert into verdict_ledger('+','.join(d)+') values('+','.join(['?']*len(d))+')',list(d.values()))
    for s in stale: con.execute('delete from verdict_ledger where tkey=?',(s['tkey'],))
    con.commit(); print('[OK] apply 台帳を整合')
else: print('[--] dry-run')

print('===== s3 都道府県の欠損 =====')
P=['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県','新潟県','富山県','石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県','鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県']
ok=con.execute("select qid,label_ja,prefecture,location_label_ja,description_ja,date_rule_src from festivals where ifnull(date_guard,'')='ok' and ifnull(date_rule,'')<>''").fetchall()
blank=[r for r in ok if not (r['prefecture'] or '').strip()]
rec=[]
for r in blank:
    hay=' '.join([r['location_label_ja'] or '',r['description_ja'] or '',(r['date_rule_src'] or '')[:200]])
    hits={p for p in P if p in hay}
    if len(hits)==1: rec.append((r['qid'],r['label_ja'],hits.pop()))
print('  掲載可',len(ok),'件中 都道府県が空',len(blank),'件 ('+str(round(len(blank)*100/max(1,len(ok))))+'%)')
print('  本文から一意に復元できる',len(rec),'件')
for x in rec[:15]: print('   ',x[0],x[1][:20],'->',x[2])
con.close()
snap=os.path.join(SNAP,'step89_'+TS+'.json')
json.dump({'apply':APPLY,'ledger_add':len(miss),'ledger_del':len(stale),'pref_blank':len(blank),'pref_recover':len(rec)},open(snap,'w'),ensure_ascii=False,indent=1)
print('APPLY='+str(APPLY),'snapshot='+snap)
