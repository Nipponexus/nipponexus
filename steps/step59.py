#!/usr/bin/env python3
# step59: step55の再生成(=/tmp消失対応)。canonはoracles一本化。成果物は永続ディレクトリへ。
import os,sys,re,json,time,sqlite3,unicodedata,traceback,subprocess
HOME=os.path.expanduser("~"); SCR=f"{HOME}/nipponexus/scripts"; SNAP=f"{HOME}/nipponexus/snapshots"
DOC=f"{HOME}/nexus_data"; ADD=f"{DOC}/04_addenda.md"; DB=f"{HOME}/nipponexus/data/sqlite/nipponexus.db"
sys.path.insert(0,SCR); os.makedirs(SNAP,exist_ok=True)
APPLY=os.environ.get("NX_APPLY")=="1"; FACT=os.environ.get("NX_FACT")=="1"
TS=time.strftime("%Y%m%d_%H%M%S"); R={}
def sec(n,t,fn):
    print(f"\n=== {n}) {t} ===")
    try: R[n]=fn(); print(f"  -- section {n} ok")
    except Exception:
        R[n]="ERR"; print(f"  !! section {n} 失敗（後続継続）")
        for l in traceback.format_exc().splitlines()[-6:]: print("   | "+l)
PREF={"北海道":"Hokkaido","青森":"Aomori","岩手":"Iwate","宮城":"Miyagi","秋田":"Akita","山形":"Yamagata",
"福島":"Fukushima","茨城":"Ibaraki","栃木":"Tochigi","群馬":"Gunma","埼玉":"Saitama","千葉":"Chiba",
"東京":"Tokyo","神奈川":"Kanagawa","新潟":"Niigata","富山":"Toyama","石川":"Ishikawa","福井":"Fukui",
"山梨":"Yamanashi","長野":"Nagano","岐阜":"Gifu","静岡":"Shizuoka","愛知":"Aichi","三重":"Mie",
"滋賀":"Shiga","京都":"Kyoto","大阪":"Osaka","兵庫":"Hyogo","奈良":"Nara","和歌山":"Wakayama",
"鳥取":"Tottori","島根":"Shimane","岡山":"Okayama","広島":"Hiroshima","山口":"Yamaguchi",
"徳島":"Tokushima","香川":"Kagawa","愛媛":"Ehime","高知":"Kochi","福岡":"Fukuoka","佐賀":"Saga",
"長崎":"Nagasaki","熊本":"Kumamoto","大分":"Oita","宮崎":"Miyazaki","鹿児島":"Kagoshima","沖縄":"Okinawa"}
ALLP=set(PREF.values())
TERMS=["Kasuga Taisha","Sumiyoshi Taisha","Sensoji","Todaiji","Eiheiji","Kofukuji",
       "Suwa Taisha","Yamadera","Hachiman Shrine","Shinji","Kanpei Taisha","Gion Shrine"]
STOP={"shinji","gyoji","naorai","matsuri","mikoshi"}
def pref_en(j): return PREF.get(re.sub(r"(都|道|府|県)$","",j or "")) if j else None
def dups(s): return set(x.lower() for x in re.findall(r"\b(\w+)\s+\1\b",s))
import oracles
con=sqlite3.connect(DB); cur=con.cursor()
STATE={"plan":[],"rej":[],"rows":[],"hold":[]}

def s0():
    print(f"  steps={HOME}/nipponexus/steps  snapshots={SNAP}")
    print(f"  NX_APPLY={APPLY}  NX_FACT={FACT}")
    return True
sec(0,"環境",s0)

def s1():
    for t in TERMS:
        if t.lower() in STOP:
            STATE["rej"].append((t,"-","一般名詞(語尾誤爆)")); print(f"  [reject  ] {t:16s} 一般名詞"); continue
        d=oracles.canon_probe(t)
        new=oracles.canon_title(t)
        if new and new!=t:
            STATE["plan"].append((t,new,d)); print(f"  [apply   ] {t:16s} -> {new:16s} qid={d.get('qid')} lat={d.get('lat')} P625={d.get('P625')}")
        elif new==t: print(f"  [nochange] {t:16s}")
        else:
            why=f"非実体/欠落 state={d.get('state')} qid={d.get('qid')} lat={d.get('lat')} P625={d.get('P625')}"
            STATE["rej"].append((t,d.get("title","-"),why)); print(f"  [reject  ] {t:16s} -> {d.get('title','-'):16s} {why}")
    return len(STATE["plan"])
sec(1,"canon判定（oracles.canon_title 一本化）",s1)

def s2():
    for old,new,d in STATE["plan"]:
        ex=d.get("extract","") or ""
        home={p for p in ALLP if re.search(rf"\b{p}\b",ex)}
        for qid,pj,txt in cur.execute(
            "select qid,prefecture,manual_content_en from festivals where manual_content_en like ?",(f"%{old}%",)).fetchall():
            pe=pref_en(pj)
            if pe and pe in home: STATE["rows"].append((qid,old,new,"県一致")); continue
            subject = old in txt[:200]
            near=""; 
            for m in re.finditer(re.escape(old),txt):
                w=txt[max(0,m.start()-120):m.end()+120]
                if any(re.search(rf"\b{h}\b",w) for h in home):
                    near=" ".join(w.split())[:120]; break
            if near and not subject: STATE["rows"].append((qid,old,new,f"参照:{near[:50]}…")); continue
            m=re.search(rf".{{0,60}}{re.escape(old)}.{{0,60}}",txt,re.S)
            STATE["hold"].append((qid,pj,old,new," ".join(m.group(0).split()) if m else ""))
    print(f"  適用={len(STATE['rows'])}レコード / hold={len(STATE['hold'])}レコード")
    for qid,pj,old,new,ctx in STATE["hold"]: print(f"  [hold] {qid} {pj} {old}: …{ctx[:100]}…")
    return len(STATE["rows"])
sec(2,"レコード単位判定（±120字の距離条件・主体除外）",s2)

def s3():
    r=subprocess.run([sys.executable,f"{SCR}/nxcheck.py"],capture_output=True,text=True)
    print("  "+"\n  ".join([l for l in r.stdout.splitlines() if "PASS" in l or "NG" in l]))
    return ("NG" not in r.stdout) and r.returncode==0
sec(3,"回帰ゲート",s3)

def s4():
    if R.get(3) is not True: print("  gate NG のため反映しない"); return 0
    snap={}; done=0
    for qid,old,new,why in STATE["rows"]:
        row=cur.execute("select manual_content_en from festivals where qid=?",(qid,)).fetchone()
        if not row: continue
        txt=row[0]; c=txt.count(old)
        if not c: continue
        nt=txt.replace(old,new)
        if abs(len(nt)-len(txt))>60 or nt.count("\n")!=txt.count("\n"):
            print(f"  [NG] {qid} 長さ/行数"); continue
        nd=dups(nt)-dups(txt)
        if nd: print(f"  [NG] {qid} 置換で重複語発生 {nd}"); continue
        if dups(txt): print(f"  [note] {qid} 元から重複語 {dups(txt)}（別案件）")
        snap.setdefault(qid,txt)
        if APPLY:
            cur.execute("update festivals set manual_content_en=? where qid=?",(nt,qid)); done+=c
            print(f"  [ok] {qid} x{c} {old} -> {new} ({why})")
        else: print(f"  [dry] {qid} x{c} {old} -> {new} ({why})")
    if APPLY and snap:
        con.commit()
        p=f"{SNAP}/prewrite_step59_{TS}.json"; json.dump(snap,open(p,"w",encoding="utf-8"),ensure_ascii=False)
        print(f"  確定={done}箇所 snapshot={p}")
    return done
sec(4,"反映",s4)

def s5():
    rows=cur.execute("select qid,manual_content_en from festivals where manual_content_en like '%JR Konomiya%' or manual_content_en like '%JR Kōnomiya%'").fetchall()
    for qid,txt in rows:
        nt=re.sub(r"JR\s*K[oō]nomiya Station","JR Inazawa Station",txt)
        print(f"  {'[fact]' if FACT else '[dry-fact]'} {qid} JR Konomiya Station -> JR Inazawa Station")
        if FACT:
            p=f"{SNAP}/prewrite_fact_konomiya_{TS}.json"
            json.dump({qid:txt},open(p,"w",encoding="utf-8"),ensure_ascii=False)
            cur.execute("update festivals set manual_content_en=? where qid=?",(nt,qid)); print(f"    snapshot={p}")
    if FACT: con.commit()
    return len(rows)
sec(5,"国府宮 駅名訂正（証拠: konomiya.or.jp/access）",s5)

def s6():
    import nxledger
    for old,new,why in STATE["rej"]:
        url=f"https://en.wikipedia.org/wiki/{new.replace(' ','_')}" if new!="-" else ""
        r=nxledger.put(con,tkey=f"canon|{old}",ja="",en=old,verdict="reject",note=why[:180],url=url,src="enwiki+wikidata")
        print(f"  ledger {old}: {r}")
    con.commit(); return len(STATE["rej"])
sec(6,"棄却を台帳へ（証拠付きで再記録）",s6)

def s7():
    cur.execute("""create table if not exists publish_queue(
      qid text, term text, state text default 'pending', note text, primary key(qid,term))""")
    n=0
    for qid,pj,old,new,ctx in STATE["hold"]:
        cur.execute("insert or ignore into publish_queue(qid,term,state,note) values(?,?,'hold',?)",
                    (qid,old,f"同名別実体の疑い/{pj}")); n+=cur.rowcount
    con.commit()
    for st,c in cur.execute("select state,count(*) from publish_queue group by state"): print(f"  {st:10s} {c}")
    return n
sec(7,"hold を publish_queue へ",s7)

def s8():
    import nxdoc
    body=("## [TMPLOSS_20260810]\n"
          "TMPLOSS: /tmp は掃除される。step スクリプトは ~/nipponexus/steps/、\n"
          "巻き戻し用スナップショットは ~/nipponexus/snapshots/ に置く。/tmp へのsnapshot書き出しは禁止。\n"
          "canon の実装は oracles.py の ORACLE_V3 ブロックのみ。step 内に再実装しない(三重定義事故)。\n")
    return nxdoc.insert_once(ADD,"TMPLOSS_20260810",body)
sec(8,"04_addenda.md 追記",s8)
con.close()
print("\n=== summary ===")
for k in sorted(R): print(f"  section {k}: {R[k]}")
