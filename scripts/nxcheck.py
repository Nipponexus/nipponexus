import os,sys,re,json,sqlite3,importlib
SCR=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,SCR)
DB=os.path.join(os.path.dirname(SCR),"data","sqlite","nipponexus.db")
FIX=os.path.join(SCR,"nxcheck_fixtures.json")
def build_u(tkey,old,new):
    return {"tkey":tkey,"excerpt":tkey,"qid":tkey.split("|")[0],"old":old,"new":new,
            "verdict":"confirmed_wrong","evidence_verified":True,"detector":"translit_check"}
def main():
    import nxapply; importlib.reload(nxapply)
    fx=json.load(open(FIX,encoding="utf-8")); ng=0
    for f in fx:
        u=build_u(f["tkey"],f["old"],f["new"])
        try: ok,why=nxapply._entity_ok(u,f["old"],f["new"])
        except Exception as e: ok,why=None,"ERR %s"%e
        mark="OK " if ok==f["expect"] else "NG "
        if ok!=f["expect"]: ng+=1
        print("%s %-22s %-24r -> %-26r exp=%-5s got=%-5s %s"%(
            mark,f["tkey"].split("|")[0],f["old"],f["new"],f["expect"],ok,(why or "")[:46]))
    print("--- %d/%d PASS ---"%(len(fx)-ng,len(fx)))
    return 1 if ng else 0
if __name__=="__main__": sys.exit(main())
