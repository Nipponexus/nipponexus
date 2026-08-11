#!/usr/bin/env python3
import os,sys,time,traceback
HOME=os.path.expanduser("~"); SCR=HOME+"/nipponexus/scripts"; LOG=HOME+"/nipponexus/logs"
os.makedirs(LOG,exist_ok=True)
LF=LOG+"/daily.log"
try:
    if os.path.exists(LF) and os.path.getsize(LF)>1048576:
        os.replace(LF,LF+"."+time.strftime("%Y%m%d"))
except Exception: pass
def log(m):
    line=time.strftime("%F %T")+" "+m
    try: open(LF,"a").write(line+"\n")
    except Exception: pass
    print(line,flush=True)
log("start pid=%d py=%s" % (os.getpid(), sys.executable))
rc=0
try:
    sys.path.insert(0,SCR)
    import json,sqlite3,subprocess
    import oracles
    DB=HOME+"/nipponexus/data/sqlite/nipponexus.db"
    N=int(os.environ.get("NX_DAILY_N","5"))
    # canary は必ず force=True。キャッシュを引くと壊れても永久にOKになる。
    CANARY={"Sensoji":"Sens\u014d-ji","Yamadera":"Yama-dera","Eiheiji":"Eihei-ji","Hachiman Shrine":None}
    bad=[]
    for k,v in CANARY.items():
        try: g=oracles.canon_title(k,force=True)
        except Exception as e: g="ERR:"+str(e)[:40]
        if g!=v: bad.append((k,g,v))
    if bad:
        log("FREEZE canary不一致 %s" % bad); sys.exit(3)
    log("canary OK (force)")
    r=subprocess.run([sys.executable,SCR+"/nxcheck.py"],capture_output=True,text=True)
    if "NG" in r.stdout or r.returncode!=0:
        log("FREEZE gate NG rc=%s" % r.returncode); sys.exit(4)
    log("gate OK")
    con=sqlite3.connect(DB)
    q=con.execute("select qid,term from publish_queue where state='pending' order by rowid limit ?",(N,)).fetchall()
    if not q:
        log("queue empty"); con.close(); sys.exit(0)
    snap={}; done=0
    for qid,term in q:
        try:
            new=oracles.canon_title(term)
            if not new or new==term:
                con.execute("update publish_queue set state='nochange' where qid=? and term=?",(qid,term)); continue
            row=con.execute("select manual_content_en from festivals where qid=?",(qid,)).fetchone()
            if not row:
                con.execute("update publish_queue set state='error',note='no row' where qid=? and term=?",(qid,term)); continue
            txt=row[0]; nt=txt.replace(term,new)
            if abs(len(nt)-len(txt))>60 or nt.count("\n")!=txt.count("\n"): raise ValueError("guard len/line")
            snap[qid]=txt
            con.execute("update festivals set manual_content_en=? where qid=?",(nt,qid))
            con.execute("update publish_queue set state='done' where qid=? and term=?",(qid,term))
            done+=1; log("  applied %s %s -> %s" % (qid,term,new))
        except Exception as e:
            con.execute("update publish_queue set state='error',note=? where qid=? and term=?",(str(e)[:80],qid,term))
            log("  error %s %s: %s" % (qid,term,str(e)[:80]))
    con.commit()
    if snap:
        p=LOG+"/prewrite_daily_%s.json" % time.strftime("%Y%m%d_%H%M%S")
        json.dump(snap,open(p,"w",encoding="utf-8"),ensure_ascii=False); log("snapshot=%s" % p)
    con.close(); log("applied=%d/%d" % (done,len(q)))
except SystemExit as e:
    rc=e.code if isinstance(e.code,int) else 0
except Exception:
    log("FATAL\n"+traceback.format_exc()); rc=1
sys.exit(rc)
