# -*- coding: utf-8 -*-
# step96: 全文からの候補選別（DB書込なし・キャッシュ再利用）
import os,sys,re,sqlite3,collections
sys.path.insert(0,os.path.expanduser('~/nipponexus/scripts'))
import nxdate,nxguard4
H=os.path.expanduser('~/nipponexus'); CD=H+'/data/wikitext'
db=sqlite3.connect(H+'/data/sqlite/nipponexus.db'); db.row_factory=sqlite3.Row
ANN=re.compile(r'(毎年|例年|恒例)')
NOW=re.compile(r'(行われる|開催される|催される|実施される|開かれる)')
YEAR=re.compile(r'(1[89]\d\d年|20\d\d年|平成\d+年|令和\d+年|昭和\d+年|大正\d+年|明治\d+年|同年|の場合|予備日|順延|台風|中止|初回|第\d+回|であった|していた|かつて|までは)')
FUZZY=re.compile(r'(過ぎ|頃|ころ|ごろ|前後|付近|中旬|初旬|下旬|以降|前後の|近い|あたり)')
def select(text):
    """全候補から恒常規則らしいものを1つ選ぶ。無ければ None。理由も返す。"""
    cand=[]
    for kind,rx in nxdate.PATS:
        for m in rx.finditer(text):
            cand.append((m.start(),m.end(),kind,m.group(0)))
    cand.sort()
    for st,en,kind,raw in cand:
        back=text[max(0,st-45):st]; fwd=text[en:en+30]; w=back+raw+fwd
        if YEAR.search(w): continue                      # 年号・過去形は拒否
        if FUZZY.search(back[-12:]) or FUZZY.search(fwd[:8]): continue  # 曖昧表現は拒否
        ann=bool(ANN.search(back))
        dow=kind in ('nth_dow','last_dow') and bool(NOW.search(fwd))
        if not (ann or dow): continue
        g={'nth_dow':lambda:{'type':'nth_dow','month':int(re.match(r'(\d+)月',raw).group(1))}}
        r=nxdate.parse(text[st:en+2]) or nxdate.parse(raw)
        if not r: continue
        r['pos']=st; r['ctx']=w.replace('\n',' ')
        r['why']='毎年表現' if ann else '第N曜日+現在形'
        return r
    return None
rows=[]
for f in sorted(os.listdir(CD)):
    q=f[:-4]; r=db.execute("select label_ja from festivals where qid=?",(q,)).fetchone()
    if not r: continue
    t=open(CD+'/'+f,encoding='utf-8').read()
    rows.append((q,r['label_ja'],t,select(t)))
ok=[x for x in rows if x[3]]
print('走査 %d 件 / 採用 %d 件 (%.0f%%)'%(len(rows),len(ok),100.0*len(ok)/max(1,len(rows))))
print('--- 採用 ---')
tally=collections.Counter()
for q,lab,t,r in ok:
    d=nxdate.describe(r); g=nxguard4.classify(lab,d,r['ctx'])
    gk=g[0] if isinstance(g,(tuple,list)) else g; tally[gk]+=1
    print('  [%-7s] %-20s %-18s (%s) %s'%(gk,lab[:20],d,r['why'],r['ctx'][-42:]))
print('  ガード内訳:',dict(tally))
print('--- 見送り（%d件・先頭候補のみ表示）---'%(len(rows)-len(ok)))
for q,lab,t,r in rows:
    if r: continue
    c=nxdate.parse(t)
    print('  %-22s %s'%(lab[:22],(c['raw']+' | '+c['ctx'][-38:]) if c else '(日付なし)'))
