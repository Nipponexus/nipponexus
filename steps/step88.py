#!/usr/bin/env python3
"""step88: date guard v4 - 過去判定を近接方式へ。創始年記述の誤検出を解消"""
import os,re,sys,json,shutil,sqlite3,datetime
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SNAP=os.path.join(ROOT,'snapshots'); SCR=os.path.join(ROOT,'scripts')
DOC=os.path.expanduser('~/nexus_data/04_addenda.md')
K3='## [DATE_GUARD_V3_20260811]'; KEY='## [DATE_GUARD_V4_20260811]'
APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
TS=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'); sys.path.insert(0,SCR)
os.makedirs(SNAP,exist_ok=True)

GUARD=r'''# nxguard4: 日付規則の信頼性判定 v4（過去判定は近接方式）
import re
_Z=str.maketrans('０１２３４５６７８９','0123456789')
def norm(s): return (s or '').translate(_Z)
WIN=16
CONCEPT_EXACT={'七夕','日本の七夕','端午の節句','雛祭り','桃の節句','地蔵盆','元始祭','節分',
 '二百十日','二百二十日','入梅','半夏生','中秋の名月','土用の丑の日','大晦日','小正月'}
RE_CONCEPT=re.compile(r'三大|一覧|総称')
RE_CYCLE=re.compile(r'隔年|一年おき|[0-9二三四五六七八九十]年に[一1]度|下一桁')
RE_PAST_NEAR=re.compile(r'古くは|かつては|以前は|旧来は|往時は|時代には|時代は|年までは|までは')
RE_LUNAR=re.compile(r'旧暦|太陰暦|中秋の名月|十五夜|八朔')
RE_PERIOD=re.compile(r'試験的|\d{4}年の開催から\d{4}年まで')
RE_CHANGED=re.compile(r'(\d{4}年|平成\d{1,2}年|令和\d{1,2}年|平成元年|令和元年)[^。]{0,8}(より|から|以降)[^。]{0,30}(変更|移動|開催されるように|行われるように|変わ)')
RE_RECENT=re.compile(r'(20[1-3][0-9])年')
RE_SIG=re.compile(r'毎年|例年|恒例')
def _past_near(rule,src):
    m=re.search(r'(\d{1,2})月',rule)
    if not m: return False
    mon=m.group(1).lstrip('0')
    poss=[x.start() for x in re.finditer(r'(?<!\d)'+mon+'月',src)]
    if not poss: return False
    return all(RE_PAST_NEAR.search(src[max(0,p-WIN):p]) for p in poss)
def classify(title,rule,src):
    t=norm(title).strip(); s=norm(src); r=norm(rule)
    if t in CONCEPT_EXACT or RE_CONCEPT.search(t): return 'concept','暦の行事・まとめ記事で個別の開催日を持たない'
    if RE_CYCLE.search(s): return 'cycle','毎年開催ではない（隔年・数年に一度）'
    if _past_near(r,s):
        n='抽出元が過去の開催日を述べている'
        if RE_LUNAR.search(s): n=n+'（旧暦記述あり）'
        return 'past',n
    if RE_LUNAR.search(s): return 'lunar','旧暦基準のため新暦換算が必要'
    if RE_PERIOD.search(s): return 'review','期間限定・試験的な日程'
    if RE_CHANGED.search(s): return 'review','途中で開催日が変更された記述あり'
    if RE_RECENT.search(s) and not RE_SIG.search(s): return 'review','特定年の告知のみで毎年性の根拠なし'
    return 'ok',''
'''
open(os.path.join(SCR,'nxguard4.py'),'w').write(GUARD)
import py_compile; py_compile.compile(os.path.join(SCR,'nxguard4.py'),doraise=True)
import nxguard4 as G
print('[OK] nxguard4 生成')
bk=os.path.join(SNAP,'db_'+TS+'.db'); shutil.copy2(DB,bk); print('[OK] backup',bk)

T=[('神田祭','毎年9月15日','祭礼の時期は現在は5月の中旬だが、以前は旧暦の9月15日に行っていた。','past'),
 ('扇祭','毎年6月14日〜6月18日','今日では例年7月14日に執行されるが、古くは6月14日・18日に執行された。','past'),
 ('三条まつり','毎年3月15日','旧暦（太陰暦）時代には3月15日に行われていたが、明治改暦によって新暦','past'),
 ('富山まつり','毎年8月第1土曜日','夏祭りである。かつては毎年8月第1土曜日・日曜日開催だったが、2022年以降は9月下旬の開催が続いている。','past'),
 ('石動曳山祭','毎年4月23日〜4月25日','曳山供奉が行われる。以前は4月23日〜25日に行われていた。','past'),
 ('伏木曳山祭','毎年5月第3土曜日','富山県高岡市伏木地区にて毎年5月の第3土曜日に行われる、江戸時代後期より続く伏木神社の春季例大祭','ok'),
 ('越中八尾曳山祭','毎年5月3日','富山市八尾地域で毎年5月3日に行われる江戸時代中期より続く八尾八幡社の春季祭礼である。','ok'),
 ('福野夜高祭','毎年5月1日〜5月3日','市街地で毎年5月1日から3日に行われる江戸時代中期より続く福野神明社の春季祭礼である。','ok'),
 ('城下町新発田ふるさとまつり','毎年8月27日〜8月29日','新発田市内にて毎年8月27日から29日に行われる祭りである。江戸時代からつづく新発田諏訪神社の祭礼','ok'),
 ('大門曳山まつり','毎年10月第2日曜日','射水市大門地区にて、毎年10月第2日曜日に行われる明治時代初めより続く大門神社の秋季祭礼','ok'),
 ('時代祭','毎年10月22日','平安神宮の例大祭（10月22日）に附属する年中行事である。明治時代より始められた京都','ok'),
 ('中条祭り','毎年9月3日〜9月6日','毎年9月3日から9月6日にかけて行われる。古くは「熊野若宮神社大祭」と呼ばれており','ok'),
 ('酒田祭','毎年5月19日〜5月21日','毎年5月19日から21日までの3日間行われる。江戸時代から続く祭りで、古くは山','ok'),
 ('下呂の田の神祭','毎年2月7日〜2月14日','明治初年までは1月14日に行われていたが、現在は2月7日から14日までの8日間に亘って','ok'),
 ('郷ノ浦祇園山笠','毎年7月第4土曜日','1750年（寛延3年）に再び疫病が流行したときからとされている。祭は7月の第4土曜日・日曜日に開催され','ok'),
 ('大正天皇祭','毎年1月7日','平成元年（1989年）以降、先帝祭は昭和天皇祭（1月7日）に変更されている。','review'),
 ('大文字まつり','毎年8月16日','例年8月16日に行われていたが、2018年より山の日に合わせて8月11日に開催されるようになった','review'),
 ('横手の雪まつり','毎年2月第2金曜日','2026年の開催から2029年まで、試験的にかまくらの開催日が2月第2金曜日に変更される。','review'),
 ('小津安二郎記念蓼科高原映画祭','毎年9月26日','年開催される映画祭である。 2026年「第29回」が9月26日、27日に開催することが発表された。','review'),
 ('山王祭','毎年6月15日','現在隔年の6月中旬を中心に本祭が行われるが、明治以前は旧暦の6月15日に行われていた。','cycle'),
 ('はんだ山車まつり','毎年10月第4日曜日','五年に一度（西暦の下一桁が2、もしくは7の年）、10月第4週の日曜日','cycle'),
 ('池ノ上みそぎ祭','毎年12月第2土曜日','葛懸神社で毎年12月第2土曜日に開催される神事であり、かつては旧暦10月（神無月','lunar'),
 ('起きよ祭り','毎年8月1日','宮崎県日向市の美々津町で旧暦「八朔」（8月1日）の夜に子どもたちが','lunar'),
 ('二百十日','毎年9月1日','立春を起算日として210日目である','concept'),
 ('四国三大祭り','毎年8月9日〜8月12日','で開催される知名度の高い以下の3つの祭をいう','concept'),
 ('長崎くんち','毎年10月7日〜10月9日','長崎県長崎市の諏訪神社の祭礼である。10月7日から9日','ok')]
ng=0
for t,r,s,exp in T:
    got=G.classify(t,r,s)[0]
    if got!=exp: ng+=1; print('  NG',t,'期待',exp,'実際',got)
print('  self-test',str(len(T)-ng)+'/'+str(len(T)),'OK' if ng==0 else 'NG'); assert ng==0,'self-test 失敗'

con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
rows=con.execute("select qid,label_ja,date_rule,date_rule_src,date_guard,wikipedia_ja from festivals where ifnull(date_rule,'')<>''").fetchall()
chg=[]; tally={}
for r in rows:
    v,note=G.classify(r['label_ja'],r['date_rule'],r['date_rule_src'])
    cur=r['date_guard'] or ''
    if v=='ok' and cur=='conflict': v,note='conflict','日付抽出の競合（別枠で対応）'
    tally[v]=tally.get(v,0)+1
    if v!=cur: chg.append((r['qid'],r['label_ja'],cur,v,note,r['date_rule'],r['wikipedia_ja']))
print('[OK] scan 総数',len(rows),'v4判定',dict(sorted(tally.items(),key=lambda x:-x[1])))
print('  変化',len(chg),'件 / ok',tally.get('ok',0),'(v2 243 / v3 220)')
print('  ── 非ok の全件 ──')
for r in rows:
    v,note=G.classify(r['label_ja'],r['date_rule'],r['date_rule_src'])
    if v not in ('ok','conflict','lunar','concept'):
        print('   ',v,r['qid'],r['label_ja'][:20],'|',r['date_rule'])

FIX=[('Q3334755','今日では例年7月14日','毎年7月14日','根拠文が現行日を7月14日と明記。古い6月の日付を採用していた'),
     ('Q11435600','2018年より','毎年8月11日','根拠文が2018年より8月11日へ変更と明記')]
try: import nxdate
except Exception as e: nxdate=None; print('  nxdate 未取得',e)
fixed=[]
for qid,ev,newrule,why in FIX:
    r=con.execute("select label_ja,date_rule,date_rule_src,wikipedia_ja from festivals where qid=?",(qid,)).fetchone()
    if not r or ev not in (r['date_rule_src'] or ''): print('  skip',qid); continue
    j=None
    if nxdate:
        try:
            d=nxdate.parse(newrule)
            if not d: print('  skip',qid,'parse不可'); continue
            if hasattr(nxdate,'describe') and nxdate.describe(d)!=newrule:
                print('  skip',qid,'describe不一致',nxdate.describe(d)); continue
            j=json.dumps(d,ensure_ascii=False,default=str)
        except Exception as e: print('  skip',qid,'例外',e); continue
    fixed.append((qid,r['label_ja'],r['date_rule'],newrule,j,why,r['wikipedia_ja']))
    print('  訂正候補',qid,r['label_ja'],r['date_rule'],'->',newrule)
print('[OK] fix',len(fixed),'件')

cols={c['name'] for c in con.execute('pragma table_info(verdict_ledger)')}
def led(tkey,verdict,note,url,qid,ja,old,new):
    d={'tkey':tkey,'verdict':verdict,'note':note,'url':url,'qid':qid,'ja':ja,'old':old,'new':new,
       'decided_at':datetime.datetime.now().isoformat(timespec='seconds'),'src':'step88'}
    d={k:v for k,v in d.items() if k in cols}
    con.execute('delete from verdict_ledger where tkey=?',(tkey,))
    con.execute('insert into verdict_ledger('+','.join(d)+') values('+','.join(['?']*len(d))+')',list(d.values()))
if APPLY:
    for qid,ja,cur,v,note,rule,wp in chg:
        con.execute('update festivals set date_guard=?,date_guard_note=? where qid=?',(v,note,qid))
        if v=='ok': con.execute('delete from verdict_ledger where tkey=?',('DATEGUARD['+qid+']',))
        else: led('DATEGUARD['+qid+']',v,note,wp or '',qid,ja,rule,'')
    for qid,ja,old,new,j,why,wp in fixed:
        if j: con.execute('update festivals set date_rule=?,date_rule_json=?,date_guard=?,date_guard_note=? where qid=?',(new,j,'ok',why,qid))
        else: con.execute('update festivals set date_rule=?,date_guard=?,date_guard_note=? where qid=?',(new,'ok',why,qid))
        led('DATEFIX['+qid+']','apply',why,wp or '',qid,ja,old,new)
    con.commit(); print('[OK] apply 反映済み')
else: print('[--] dry-run（DB 未変更）')

try:
    import importlib,nxcal; importlib.reload(nxcal); print('[OK] calendar',nxcal.render())
except Exception as e: print('[NG] calendar',e)
print('  DB guard 分布',dict(con.execute("select date_guard,count(*) from festivals where ifnull(date_rule,'')<>'' group by 1").fetchall()))
print('  台帳 DATEGUARD',con.execute("select count(*) from verdict_ledger where tkey like 'DATEGUARD%'").fetchone()[0],
      '/ DATEFIX',con.execute("select count(*) from verdict_ledger where tkey like 'DATEFIX%'").fetchone()[0])
con.close()

if APPLY:
    body='\n'.join([KEY,
     '- 日付ガード v4 (scripts/nxguard4.py): 過去判定を近接方式へ変更。規則の月が本文に出る位置の直前16字に過去語がある場合のみ past。',
     '- v3 の全体スキャン方式は「江戸時代より続く」等の創始年記述を誤検出（15件中10件が誤り）。v4 で past は '+str(tally.get('past',0))+' 件に。',
     '- 追加軸: 隔年・N年に一度は cycle、暦の雑節・節句は concept（完全一致集合）、近年(2015-2035)の年号のみで毎年性なしは review。',
     '- 訂正: 扇祭 6月->7月14日、大文字まつり 8月16日->8月11日（台帳 DATEFIX）。',
     '- 判定: ok '+str(tally.get('ok',0))+' / past '+str(tally.get('past',0))+' / cycle '+str(tally.get('cycle',0))+' / concept '+str(tally.get('concept',0))+' / lunar '+str(tally.get('lunar',0))+' / review '+str(tally.get('review',0))+'。',''])
    txt=open(DOC,encoding='utf-8').read() if os.path.exists(DOC) else ''
    if K3 in txt:
        i=txt.index(K3); j=txt.find('\n## ',i+1); txt=txt[:i]+body+('\n'+txt[j+1:] if j>0 else '\n')
        open(DOC,'w',encoding='utf-8').write(txt); print('[OK] doc v3ブロックをv4で置換')
    elif KEY not in txt:
        open(DOC,'a',encoding='utf-8').write('\n'+body); print('[OK] doc 追記')
    else: print('[--] doc 既存')
else: print('[--] doc 未更新（dry-run）')
n=len(open(DOC,encoding='utf-8').read().splitlines()) if os.path.exists(DOC) else 0
print('  DOC =',n,'行'+('  ※要約統合を検討' if n>360 else ''))
snap=os.path.join(SNAP,'step88_'+TS+'.json')
json.dump({'apply':APPLY,'tally':tally,'changed':len(chg),'fixed':len(fixed)},open(snap,'w'),ensure_ascii=False,indent=1)
print('APPLY='+str(APPLY),'snapshot='+snap)
