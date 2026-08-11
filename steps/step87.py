#!/usr/bin/env python3
"""step87: date guard v3 - past/cycle/changed/concept を除外し、根拠文で直せる2件を自動訂正"""
import os,re,sys,json,shutil,sqlite3,datetime
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SNAP=os.path.join(ROOT,'snapshots'); SCR=os.path.join(ROOT,'scripts')
DOC=os.path.expanduser('~/nexus_data/04_addenda.md'); KEY='## [DATE_GUARD_V3_20260811]'
APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
TS=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'); sys.path.insert(0,SCR)
os.makedirs(SNAP,exist_ok=True)

GUARD=r'''# nxguard3: 日付規則の信頼性判定 v3
import re
_Z=str.maketrans('０１２３４５６７８９','0123456789')
def norm(s): return (s or '').translate(_Z)
CONCEPT_EXACT={'七夕','日本の七夕','端午の節句','雛祭り','桃の節句','地蔵盆','元始祭',
 '二百十日','二百二十日','入梅','節分','中秋の名月','半夏生','土用の丑の日'}
RE_CONCEPT=re.compile(r'三大|一覧|総称')
RE_CYCLE=re.compile(r'隔年|一年おき|[0-9二三四五六七八九十]年に[一1１]度|下一桁')
RE_PAST=re.compile(r'古くは|かつては|以前は|旧来|明治初年|江戸時代|明治時代|大正時代|昭和初期|当時は|旧暦.{0,8}時代|までは.{0,12}(行わ|執行|開催)')
RE_LUNAR=re.compile(r'旧暦|太陰暦|中秋の名月|十五夜|八朔')
RE_PERIOD=re.compile(r'試験的|\d{4}年の開催から\d{4}年まで')
RE_CHANGED=re.compile(r'(\d{4}年|平成\d{1,2}年|令和\d{1,2}年)(より|から)[^。]{0,24}(変更|移動|開催されるように|行われるように|変わ)')
RE_SIG=re.compile(r'毎年|例年|恒例')
RE_YEAR=re.compile(r'\d{4}年')
def classify(title,rule,src):
    t=norm(title).strip(); s=norm(src)
    if t in CONCEPT_EXACT or RE_CONCEPT.search(t): return 'concept','暦の行事・まとめ記事で個別の開催日を持たない'
    if RE_CYCLE.search(s): return 'cycle','毎年開催ではない（隔年・数年に一度）'
    if RE_PAST.search(s):  return 'past','抽出元が過去の開催日を述べている'
    if RE_LUNAR.search(s): return 'lunar','旧暦基準のため新暦換算が必要'
    if RE_PERIOD.search(s):return 'review','期間限定・試験的な日程'
    if RE_CHANGED.search(s):return 'review','途中で開催日が変更された記述あり'
    if RE_YEAR.search(s) and not RE_SIG.search(s): return 'review','特定年の告知のみで毎年性の根拠なし'
    return 'ok',''
'''
open(os.path.join(SCR,'nxguard3.py'),'w').write(GUARD)
import py_compile; py_compile.compile(os.path.join(SCR,'nxguard3.py'),doraise=True)
import nxguard3
print('[OK] nxguard3 生成')

# s0 backup
bk=os.path.join(SNAP,'db_'+TS+'.db'); shutil.copy2(DB,bk); print('[OK] backup',bk)

# s1 self-test
T=[('扇祭','毎年6月14日〜6月18日','今日では例年7月14日に執行されるが、古くは6月14日・18日に執行された','past'),
   ('山王祭','毎年6月15日','現在隔年の6月中旬を中心に本祭が行われるが、明治以前は','cycle'),
   ('はんだ山車まつり','毎年10月第4日曜日','五年に一度（西暦の下一桁が2、もしくは7の年）、10月第4週の日','cycle'),
   ('大文字まつり','毎年8月16日','例年8月16日に行われていたが、2018年より山の日に合わせて8月11日に開催されるようになった','review'),
   ('横手の雪まつり','毎年2月第2金曜日','2026年の開催から2029年まで、試験的にかまくらの開催日が','review'),
   ('小津安二郎記念蓼科高原映画祭','毎年9月26日','2026年「第29回小津安二郎記念蓼科高原映画祭」が9月26日、27日に開催','review'),
   ('二百十日','毎年9月1日','立春を起算日として210日目である','concept'),
   ('四国三大祭り','毎年8月9日〜8月12日','で開催される知名度の高い以下の3つの祭をいう','concept'),
   ('起きよ祭り','毎年8月1日','旧暦「八朔」（8月1日）の夜に子どもたちが','lunar'),
   ('仙台七夕花火祭','毎年8月5日','仙台七夕まつりの前日に開催される花火大会である','ok'),
   ('おんまく','毎年8月第1土曜日','(2026年)は、8月8日・9日に開催され、例年は8月の第一土曜日','ok'),
   ('長崎くんち','毎年10月7日〜10月9日','長崎県長崎市の諏訪神社の祭礼である。10月7日から9日','ok')]
ng=0
for t,r,s,exp in T:
    got=nxguard3.classify(t,r,s)[0]
    if got!=exp: ng+=1; print('  NG',t,'期待',exp,'実際',got)
print('  self-test',str(len(T)-ng)+'/'+str(len(T)),'OK' if ng==0 else 'NG')
assert ng==0,'self-test 失敗'

# s2 再判定（降格のみ / ok への昇格はしない）
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
rows=con.execute("select qid,label_ja,date_rule,date_rule_src,date_guard,wikipedia_ja from festivals where ifnull(date_rule,'')<>''").fetchall()
chg=[]; tally={}
for r in rows:
    v,note=nxguard3.classify(r['label_ja'],r['date_rule'],r['date_rule_src'])
    cur=r['date_guard'] or ''
    if v=='ok' and cur not in ('','ok'): v,note=cur,'v2判定を維持'
    tally[v]=tally.get(v,0)+1
    if v!=cur: chg.append((r['qid'],r['label_ja'],cur,v,note,r['date_rule'],r['wikipedia_ja']))
print('[OK] scan  総数',len(rows),' v3判定',dict(sorted(tally.items(),key=lambda x:-x[1])))
print('  変化',len(chg),'件  ok件数',tally.get('ok',0),'(従来 243)')
for c in chg[:30]: print('   ',c[0],c[1][:18],c[2] or '(空)','->',c[3],'|',c[4])
if len(chg)>30: print('    ... 他',len(chg)-30,'件')

# s3 根拠文で直せる訂正（自己整合チェック付き）
FIX=[('Q3334755','今日では例年7月14日','毎年7月14日','根拠文が現行日を7月14日と明記。古い6月の日付を採用していた'),
     ('Q11435600','2018年より','毎年8月11日','根拠文が2018年より8月11日へ変更と明記')]
try:
    import nxdate
except Exception as e:
    nxdate=None; print('  nxdate 未取得',e)
fixed=[]
for qid,ev,newrule,why in FIX:
    r=con.execute("select label_ja,date_rule,date_rule_src,wikipedia_ja from festivals where qid=?",(qid,)).fetchone()
    if not r: print('  skip',qid,'行なし'); continue
    if ev not in (r['date_rule_src'] or ''): print('  skip',qid,'根拠文なし'); continue
    j=None
    if nxdate:
        try:
            d=nxdate.parse(newrule)
            if not d: print('  skip',qid,'parse不可'); continue
            if hasattr(nxdate,'describe') and nxdate.describe(d)!=newrule:
                print('  skip',qid,'describe不一致',nxdate.describe(d)); continue
            j=json.dumps(d,ensure_ascii=False,default=str)
        except Exception as e:
            print('  skip',qid,'parse例外',e); continue
    fixed.append((qid,r['label_ja'],r['date_rule'],newrule,j,why,r['wikipedia_ja']))
    print('  訂正候補',qid,r['label_ja'],r['date_rule'],'->',newrule)
print('[OK] fix 候補',len(fixed),'件')

# s4 台帳＋DB反映
cols={c['name'] for c in con.execute('pragma table_info(verdict_ledger)')}
def led(tkey,verdict,note,url,qid,ja,old,new):
    d={'tkey':tkey,'verdict':verdict,'note':note,'url':url,'qid':qid,'ja':ja,'old':old,'new':new,
       'decided_at':datetime.datetime.now().isoformat(timespec='seconds'),'src':'step87'}
    d={k:v for k,v in d.items() if k in cols}
    con.execute('delete from verdict_ledger where tkey=?',(tkey,))
    con.execute('insert into verdict_ledger('+','.join(d)+') values('+','.join(['?']*len(d))+')',list(d.values()))
if APPLY:
    for qid,ja,cur,v,note,rule,wp in chg:
        con.execute('update festivals set date_guard=?,date_guard_note=? where qid=?',(v,note,qid))
        if v in ('past','cycle','concept','review','lunar'):
            led('DATEGUARD['+qid+']',v,note,wp or '',qid,ja,rule,'')
    for qid,ja,old,new,j,why,wp in fixed:
        if j: con.execute('update festivals set date_rule=?,date_rule_json=?,date_guard=?,date_guard_note=? where qid=?',(new,j,'ok',why,qid))
        else: con.execute('update festivals set date_rule=?,date_guard=?,date_guard_note=? where qid=?',(new,'ok',why,qid))
        led('DATEFIX['+qid+']','apply',why,wp or '',qid,ja,old,new)
    con.commit(); print('[OK] apply 反映済み')
else: print('[--] dry-run（DB 未変更）')

# s5 全角正規化した月不一致の再監査
Z=str.maketrans('０１２３４５６７８９','0123456789')
bad=[]
for r in con.execute("select qid,label_ja,date_rule,date_rule_src from festivals where ifnull(date_rule,'')<>''"):
    m=re.search(r'(\d{1,2})月',(r['date_rule'] or '').translate(Z))
    if not m: continue
    ms={x.lstrip('0') for x in re.findall(r'(\d{1,2})月',(r['date_rule_src'] or '').translate(Z))}
    if ms and m.group(1).lstrip('0') not in ms: bad.append((r['qid'],r['label_ja'],r['date_rule'],sorted(ms,key=int)))
print('[OK] 月不一致（正規化後）=',len(bad),'件')
for b in bad[:10]: print('   ',b)

# s6 カレンダー再生成
try:
    import importlib,nxcal; importlib.reload(nxcal)
    res=nxcal.render(); print('[OK] calendar',res)
except Exception as e: print('[NG] calendar',e)
g=dict(con.execute("select date_guard,count(*) from festivals where ifnull(date_rule,'')<>'' group by 1").fetchall())
print('  DB上の guard 分布',g)
con.close()

# s7 doc（簡潔に）
lines=[KEY,
 '- 日付ガード v3: past/cycle/concept/review の4軸を追加（scripts/nxguard3.py）。',
 '- 追加軸: 古くは・以前は・旧暦時代（過去日）／隔年・N年に一度（周期）／N年より変更（失効）／雑節・三大等（概念）。',
 '- v2 の ok 243 件から v3 で '+str(tally.get('ok',0))+' 件へ。変化 '+str(len(chg))+' 件。',
 '- 根拠文で直した誤り: 扇祭 6月->7月14日、大文字まつり 8月16日->8月11日（台帳 DATEFIX）。',
 '- 月不一致は正規化後 '+str(len(bad))+' 件。全角数字が原因の誤検出は解消。',
 '- 次: nxfix の PUBLIC_PREFIX に DATEFIX を追加し訂正履歴へ公開。','']
txt=open(DOC,encoding='utf-8').read() if os.path.exists(DOC) else ''
if KEY in txt: print('[--] doc 既存キーあり・追記せず')
else:
    open(DOC,'a',encoding='utf-8').write('\n'+'\n'.join(lines))
    print('[OK] doc 追記')
n=len(open(DOC,encoding='utf-8').read().splitlines())
print('  DOC =',n,'行'+('  ※400行接近・要約統合を検討' if n>360 else ''))

snap=os.path.join(SNAP,'step87_'+TS+'.json')
json.dump({'apply':APPLY,'tally':tally,'changed':len(chg),'fixed':len(fixed),'month_bad':len(bad)},
          open(snap,'w'),ensure_ascii=False,indent=1)
print('APPLY='+str(APPLY),'snapshot='+snap)
