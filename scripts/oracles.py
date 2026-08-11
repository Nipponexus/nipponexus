
import os,re,json,time,unicodedata,urllib.parse,urllib.request
CD=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data","oracache")
os.makedirs(CD,exist_ok=True)
UA={"User-Agent":"nipponexus/1.0 (translit verification; contact: local)"}
def _get(url):
    k=os.path.join(CD,re.sub(r'[^A-Za-z0-9]','_',url)[-120:]+".json")
    if os.path.exists(k) and time.time()-os.path.getmtime(k)<30*86400:
        try: return json.load(open(k,encoding="utf-8"))
        except Exception: pass
    for i in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=20)
            d=json.loads(r.read().decode("utf-8"))
            json.dump(d,open(k,"w",encoding="utf-8")); time.sleep(0.6); return d
        except Exception:
            time.sleep(1.5*(i+1))
    return None
_Y={"きゃ":"kya","きゅ":"kyu","きょ":"kyo","しゃ":"sha","しゅ":"shu","しょ":"sho",
"ちゃ":"cha","ちゅ":"chu","ちょ":"cho","にゃ":"nya","にゅ":"nyu","にょ":"nyo",
"ひゃ":"hya","ひゅ":"hyu","ひょ":"hyo","みゃ":"mya","みゅ":"myu","みょ":"myo",
"りゃ":"rya","りゅ":"ryu","りょ":"ryo","ぎゃ":"gya","ぎゅ":"gyu","ぎょ":"gyo",
"じゃ":"ja","じゅ":"ju","じょ":"jo","びゃ":"bya","びゅ":"byu","びょ":"byo",
"ぴゃ":"pya","ぴゅ":"pyu","ぴょ":"pyo"}
_S={"あ":"a","い":"i","う":"u","え":"e","お":"o","か":"ka","き":"ki","く":"ku","け":"ke","こ":"ko",
"さ":"sa","し":"shi","す":"su","せ":"se","そ":"so","た":"ta","ち":"chi","つ":"tsu","て":"te","と":"to",
"な":"na","に":"ni","ぬ":"nu","ね":"ne","の":"no","は":"ha","ひ":"hi","ふ":"fu","へ":"he","ほ":"ho",
"ま":"ma","み":"mi","む":"mu","め":"me","も":"mo","や":"ya","ゆ":"yu","よ":"yo",
"ら":"ra","り":"ri","る":"ru","れ":"re","ろ":"ro","わ":"wa","を":"o","ん":"n",
"が":"ga","ぎ":"gi","ぐ":"gu","げ":"ge","ご":"go","ざ":"za","じ":"ji","ず":"zu","ぜ":"ze","ぞ":"zo",
"だ":"da","ぢ":"ji","づ":"zu","で":"de","ど":"do","ば":"ba","び":"bi","ぶ":"bu","べ":"be","ぼ":"bo",
"ぱ":"pa","ぴ":"pi","ぷ":"pu","ぺ":"pe","ぽ":"po","ー":""}
def hepburn(k):
    k="".join(chr(ord(c)-0x60) if "ァ"<=c<="ヶ" else c for c in (k or ""))
    o=[];i=0
    while i<len(k):
        if k[i:i+2] in _Y: o.append(_Y[k[i:i+2]]); i+=2; continue
        if k[i]=="っ": 
            n=k[i+1:i+3]; r=_Y.get(n) or _S.get(k[i+1:i+2]) or ""
            o.append(r[0] if r else ""); i+=1; continue
        o.append(_S.get(k[i],"")); i+=1
    r="".join(o)
    for a,b in [("ou","o"),("uu","u"),("oo","o"),("aa","a"),("ee","e")]: r=r.replace(a,b)
    return r
def norm(s):
    s=unicodedata.normalize("NFKD",s or "")
    s="".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]","",s.lower())
def kana_of(term):
    d=_get("https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=ja&limit=1&search="+urllib.parse.quote(term))
    qid=(d or {}).get("search") and d["search"][0]["id"]
    if qid:
        e=_get("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=claims&ids="+qid)
        try:
            for c in e["entities"][qid]["claims"].get("P1814",[]):
                return c["mainsnak"]["datavalue"]["value"]["text"]
        except Exception: pass
    d=_get("https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&explaintext=1&exintro=1&titles="+urllib.parse.quote(term))
    try:
        pg=list(d["query"]["pages"].values())[0].get("extract","")
        m=re.search(r"[（(]\s*([ぁ-んァ-ヶー・\s]{2,30}?)\s*[）)]",pg[:300])
        return m.group(1).replace(" ","").replace("・","") if m else None
    except Exception: return None
def enwiki_title(term):
    d=_get("https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=langlinks&lllang=en&titles="+urllib.parse.quote(term))
    try:
        pg=list(d["query"]["pages"].values())[0]
        return pg["langlinks"][0]["*"]
    except Exception: return None
def adjudicate(ja, old, new):
    """読み→ヘボン式 と ja→en言語間リンク の2オラクルで自動裁定"""
    k=kana_of(ja); hep=hepburn(k) if k else None
    ev={"kana":k,"hepburn":hep}
    if hep:
        ho=norm(old.split()[0] if old.split() else ""); hn=norm(new.split()[0] if new.split() else "")
        so=hep.startswith(ho) and bool(ho); sn=hep.startswith(hn) and bool(hn)
        if sn and not so: return "accept","読み一致 %s→%s"%(k,hep), ev
        if so and not sn: return "reject","現行が読みと一致 %s→%s (Pro誤り)"%(k,hep), ev
    t=enwiki_title(ja); ev["enwiki"]=t
    if t:
        if norm(t)==norm(new): return "accept","enwiki=%s"%t, ev
        if norm(t)==norm(old): return "reject","enwiki=%s (現行が正)"%t, ev
        return "hold","enwiki=%s がold/newどちらとも異なる"%t, ev
    return "hold","読み・langlinkとも取得できず", ev


# ---- KANA_v2 / VOTE_v1 (2026-08-10) ----
GENERIC_JA = ("菩提寺","本堂","山門","参道","境内","本殿","公民館","市役所","駅前","商店街","神社","寺")
def _kana_paren(txt, term=""):
    for m in re.finditer(r"[（(]\s*([ぁ-んァ-ヶー・\s]{2,32}?)\s*[）)]", txt or ""):
        k=m.group(1).replace(" ","").replace("・","")
        if len(k)>=2: return k
    return None
def kana_v2(term, ja_body=""):
    if ja_body:
        i=ja_body.find(term)
        if i>=0:
            k=_kana_paren(ja_body[i:i+80]); 
            if k: return k,"本文"
    d=_get("https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=ja&limit=1&search="+urllib.parse.quote(term))
    qid=(d or {}).get("search") and d["search"][0]["id"]
    if qid:
        e=_get("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=claims|labels|aliases&languages=ja|ja-hira&ids="+qid)
        try:
            ent=e["entities"][qid]
            for c in ent.get("claims",{}).get("P1814",[]):
                return c["mainsnak"]["datavalue"]["value"]["text"],"WD:P1814"
            for a in ent.get("aliases",{}).get("ja-hira",[]): return a["value"],"WD:ja-hira"
            lb=ent.get("labels",{}).get("ja-hira",{}).get("value")
            if lb: return lb,"WD:label-hira"
        except Exception: pass
    for url in ["https://ja.wikipedia.org/w/api.php?action=query&format=json&redirects=1&prop=extracts&explaintext=1&exintro=1&titles=",
                None]:
        if url:
            d=_get(url+urllib.parse.quote(term))
            try:
                ex=list(d["query"]["pages"].values())[0].get("extract","")
                k=_kana_paren(ex[:300])
                if k: return k,"jawiki"
            except Exception: pass
        else:
            s=_get("https://ja.wikipedia.org/w/api.php?action=query&format=json&list=search&srlimit=1&srsearch="+urllib.parse.quote(term))
            hits=[h["title"] for h in (s or {}).get("query",{}).get("search",[])]
            if hits and norm(hits[0])!=norm(term):
                d=_get("https://ja.wikipedia.org/w/api.php?action=query&format=json&redirects=1&prop=extracts&explaintext=1&exintro=1&titles="+urllib.parse.quote(hits[0]))
                try:
                    ex=list(d["query"]["pages"].values())[0].get("extract","")
                    if term in ex[:200]:
                        k=_kana_paren(ex[:300])
                        if k: return k,"jawiki:search"
                except Exception: pass
    return None,None
def wd_label(term):
    try:
        import pro_verify_loop as _p
        lab,_u=_p.wikidata_en_label(term); return lab
    except Exception: return None
def adjudicate2(ja, old, new, ja_body=""):
    """WD / enwiki / 読み の3票で裁定。accept=newが正 reject=oldが正 hold=票割れor無票"""
    if ja in GENERIC_JA: return "drop","JAが一般名詞(検出器で落とすべき)",{}
    ev={}; vo=vn=0; src=[]
    lab=wd_label(ja); ev["wd"]=lab
    if lab:
        if norm(lab)==norm(new): vn+=1; src.append("WD=new")
        elif norm(lab)==norm(old): vo+=1; src.append("WD=old")
        else: src.append("WD=%s(別)"%lab)
    t=enwiki_title(ja); ev["enwiki"]=t
    if t:
        if norm(t)==norm(new): vn+=1; src.append("enwiki=new")
        elif norm(t)==norm(old): vo+=1; src.append("enwiki=old")
        else: src.append("enwiki=%s(別)"%t)
    k,ks=kana_v2(ja,ja_body); hep=hepburn(k) if k else None
    ev["kana"]=k; ev["kana_src"]=ks; ev["hepburn"]=hep
    if hep:
        ho=norm("".join(old.split()[:-1]) or old); hn=norm("".join(new.split()[:-1]) or new)
        mo=bool(ho) and (hep.startswith(ho) or ho.startswith(hep[:max(4,len(hep)-3)]))
        mn=bool(hn) and (hep.startswith(hn) or hn.startswith(hep[:max(4,len(hep)-3)]))
        if mn and not mo: vn+=1; src.append("読み=new(%s)"%hep)
        elif mo and not mn: vo+=1; src.append("読み=old(%s)"%hep)
    ev["votes"]="new%d/old%d"%(vn,vo)
    if vn and not vo: return "accept"," ".join(src),ev
    if vo and not vn: return "reject"," ".join(src),ev
    if vn and vo: return "hold","票割れ "+" ".join(src),ev
    return "hold","無票 "+" ".join(src),ev


# ---- ENTVERIFY_v1 / THIRD_v1 / WDFIRST_v1 (2026-08-10) ----
_KYU2={"國":"国","驛":"駅","縣":"県","廣":"広","濱":"浜","邊":"辺","澤":"沢","櫻":"桜",
"藝":"芸","學":"学","體":"体","龍":"竜","舊":"旧","靖國":"靖国","齋":"斎","澁":"渋"}
def shinji(s):
    for a,b in _KYU2.items(): s=(s or "").replace(a,b)
    return s
def _wd_entity(term):
    """ENTVERIFY_v1: 検索1位を無検証で使うと別項目を掴む(大和西大寺→伏見)。ラベル一致を必須にする。"""
    for t in {term, shinji(term)}:
        d=_get("https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=ja&limit=5&search="+urllib.parse.quote(t))
        for h in (d or {}).get("search",[]):
            if norm(h.get("label",""))==norm(t): return h["id"]
    return None
def kana_v3(term, ja_body=""):
    if ja_body:
        i=ja_body.find(term)
        if i>=0:
            seg=ja_body[i+len(term):i+len(term)+3]
            m=re.match(r"\s*[（(]\s*([ぁ-んァ-ヶー・\s]{2,32}?)\s*[）)]", ja_body[i+len(term):i+len(term)+40])
            if m: return m.group(1).replace(" ","").replace("・",""),"本文(直後)"
    q=_wd_entity(term)
    if q:
        e=_get("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=claims|labels|aliases&languages=ja|ja-hira&ids="+q)
        try:
            ent=e["entities"][q]
            for c in ent.get("claims",{}).get("P1814",[]):
                return c["mainsnak"]["datavalue"]["value"]["text"],"WD:P1814"
            for a in ent.get("aliases",{}).get("ja-hira",[]): return a["value"],"WD:hira"
        except Exception: pass
    for t in {term, shinji(term)}:
        d=_get("https://ja.wikipedia.org/w/api.php?action=query&format=json&redirects=1&prop=extracts&explaintext=1&exintro=1&titles="+urllib.parse.quote(t))
        try:
            ex=list(d["query"]["pages"].values())[0].get("extract","")
            if ex.startswith(t) or norm(t) in norm(ex[:40]):
                m=re.search(r"[（(]\s*([ぁ-んァ-ヶー・\s]{2,32}?)\s*[）)]",ex[:200])
                if m: return m.group(1).replace(" ","").replace("・",""),"jawiki"
        except Exception: pass
    return None,None
def official_en(term):
    for t in {term, shinji(term)}:
        l=wd_label(t)
        if l: return l,"WD"
        l=enwiki_title(t)
        if l: return l,"enwiki"
    return None,None
def adjudicate3(ja, old, new, ja_body=""):
    """THIRD_v1: 権威が第三の答えを出したら「newは誤り」の積極的証拠として扱う"""
    if ja in GENERIC_JA: return "drop","JAが一般名詞",{}
    ev={}; vn=vo=0; third=None; src=[]
    for f,nm in ((wd_label,"WD"),(enwiki_title,"enwiki")):
        try: l=f(ja) or f(shinji(ja))
        except Exception: l=None
        ev[nm]=l
        if not l: continue
        if norm(l)==norm(new): vn+=1; src.append(nm+"=new")
        elif norm(l)==norm(old): vo+=1; src.append(nm+"=old")
        else: third=l; src.append("%s=%s"%(nm,l))
    k,ks=kana_v3(ja,ja_body); ev["kana"]=k; ev["kana_src"]=ks
    hep=hepburn(k) if k else None; ev["hepburn"]=hep
    if hep:
        core=re.sub(r"(eki|jinja|jinjya|gawa|kawa|bashi|hashi|dera|tera|ji|koen|jo)$","",hep)
        ho=norm("".join(old.split()[:-1]) or old); hn=norm("".join(new.split()[:-1]) or new)
        mo=bool(ho) and (core.startswith(ho) or ho.startswith(core)) and abs(len(core)-len(ho))<=3
        mn=bool(hn) and (core.startswith(hn) or hn.startswith(core)) and abs(len(core)-len(hn))<=3
        if mn and not mo: vn+=1; src.append("読み=new")
        elif mo and not mn: vo+=1; src.append("読み=old")
    ev["votes"]="new%d/old%d"%(vn,vo); ev["third"]=third
    if vn and not vo: return "accept"," ".join(src),ev
    if vo and not vn: return "reject"," ".join(src),ev
    if vn and vo: return "hold","票割れ "+" ".join(src),ev
    if third: return "reject","権威は第三の答え %r → newは誤り"%third,ev
    return "hold","全オラクル沈黙",ev
def self_fix(ja, en_body, ja_body=""):
    """WDFIRST_v1: Proを介さず、公式英名と本文中の異表記の差から是正案を自力生成"""
    if ja in GENERIC_JA or (ja_body and ja not in ja_body): return None
    lab,srcn=official_en(ja)
    if not lab: return None
    ln=norm(lab); nw=len(lab.split())
    toks=re.findall(r"[A-Za-z0-9\u00c0-\u024f'\u2019\-]+", en_body or "")
    for w in (nw,nw+1,nw-1):
        if w<1: continue
        for i in range(len(toks)-w+1):
            frag=" ".join(toks[i:i+w])
            if norm(frag)==ln and frag!=lab and frag in en_body:
                return {"ja":ja,"old":frag,"new":lab,"src":srcn}
    return None


# ---- SELFFIX_v2 (2026-08-10): NBSP汚染/様式差/誤取得/429 の是正 ----
def _sp(s): return re.sub(r"[\s\u00a0\u3000]+"," ",s or "").strip()
def _dia(s):
    s=unicodedata.normalize("NFKD",s or "")
    return "".join(c for c in s if not unicodedata.combining(c))
def _hy(s): return re.sub(r"[-\u2010\u2011\u2013\u2014]","",s or "")
def sclass(old,new):
    o,n=_sp(old),_sp(new)
    if o==n: return "whitespace"
    if _dia(o)==_dia(n): return "diacritic"
    if _hy(o).lower()==_hy(n).lower(): return "hyphen"
    if o.lower()==n.lower(): return "case"
    if _hy(_dia(o)).lower()==_hy(_dia(n)).lower(): return "hyphen+diacritic"
    return "substance"
def wd_label_v2(term):
    """pvlを介さずキャッシュ+スロットル付きで公式英名。完全一致ラベルが複数idなら曖昧棄却。"""
    ids=[]
    for t in [term, shinji(term)]:
        d=_get("https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=ja&limit=7&search="+urllib.parse.quote(t))
        for h in (d or {}).get("search",[]):
            if norm(h.get("label",""))==norm(t) and h["id"] not in ids: ids.append(h["id"])
        if ids: break
    if len(ids)!=1: return None
    e=_get("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=labels&languages=en&ids="+ids[0])
    try: return e["entities"][ids[0]]["labels"]["en"]["value"]
    except Exception: return None
def jawiki_title(term):
    """リダイレクト後の実タイトルを検証して返す(別ページ掴みを防ぐ)"""
    for t in [term, shinji(term)]:
        d=_get("https://ja.wikipedia.org/w/api.php?action=query&format=json&redirects=1&titles="+urllib.parse.quote(t))
        try:
            pg=list(d["query"]["pages"].values())[0]
            if "missing" in pg: continue
            ttl=pg["title"]
            if norm(ttl)==norm(t) or t in ttl or ttl in t: return ttl
        except Exception: pass
    return None
def kana_v4(term, ja_body=""):
    if ja_body:
        m=re.match(r"\s*[（(]\s*([ぁ-んァ-ヶー・\s]{2,32}?)\s*[）)]", ja_body[ja_body.find(term)+len(term):ja_body.find(term)+len(term)+40]) if term in ja_body else None
        if m: return m.group(1).replace(" ","").replace("・",""),"本文"
    q=_wd_entity(term)
    if q:
        e=_get("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=claims|aliases&languages=ja-hira&ids="+q)
        try:
            ent=e["entities"][q]
            for c in ent.get("claims",{}).get("P1814",[]): return c["mainsnak"]["datavalue"]["value"]["text"],"WD:P1814"
            for a in ent.get("aliases",{}).get("ja-hira",[]): return a["value"],"WD:hira"
        except Exception: pass
    ttl=jawiki_title(term)
    if ttl:
        d=_get("https://ja.wikipedia.org/w/api.php?action=query&format=json&redirects=1&prop=extracts&explaintext=1&exintro=1&titles="+urllib.parse.quote(ttl))
        try:
            ex=list(d["query"]["pages"].values())[0].get("extract","")
            if ex[:30].startswith(ttl[:4]):
                m=re.search(r"[（(]\s*([ぁ-んァ-ヶー・\s]{2,32}?)\s*[）)]",ex[:200])
                if m: return m.group(1).replace(" ","").replace("・",""),"jawiki(%s)"%ttl
        except Exception: pass
    return None,None
def official_en_v2(term):
    l=wd_label_v2(term)
    if l: return l,"WD"
    t=enwiki_title(term)
    if t: return t,"enwiki"
    return None,None
def self_fix_v2(ja, en_body, ja_body="", allow=("substance","hyphen","case")):
    if ja in GENERIC_JA or (ja_body and ja not in ja_body): return None
    lab,srcn=official_en_v2(ja)
    if not lab: return None
    ln=norm(lab); nw=len(lab.split())
    toks=re.findall(r"[A-Za-z0-9\u00c0-\u024f'\u2019\-]+", en_body or "")
    for w in (nw,nw+1,nw-1):
        if w<1: continue
        for i in range(len(toks)-w+1):
            frag=" ".join(toks[i:i+w])
            if norm(frag)!=ln or frag==lab or frag not in en_body: continue
            c=sclass(frag,lab)
            return {"ja":ja,"old":frag,"new":lab,"src":srcn,"class":c,"ok":c in allow}
    return None


# --- SUFFIX_v1 / AXIS_v1 ---
_SUF = ["駅","寺","神社","公園","川","城"]

def kana_v5(term):
    k, s = kana_v4(term)
    if k:
        return k, s
    for suf in _SUF:
        if term.endswith(suf):
            continue
        k, s = kana_v4(term + suf)
        if k:
            return k, (s or "") + "+suffix(" + suf + ")"
    return None, None

def official_en_v5(term):
    e, s = official_en_v2(term)
    if e:
        return e, s
    for suf in _SUF:
        if term.endswith(suf):
            continue
        e, s = official_en_v2(term + suf)
        if e:
            return e, (s or "") + "+suffix(" + suf + ")"
    return None, None

def strip_dia(s):
    import unicodedata as ud
    return "".join(c for c in ud.normalize("NFD", s) if ud.category(c) != "Mn")

def axis_split(old, new):
    ax = set()
    if strip_dia(old) != old or strip_dia(new) != new:
        if strip_dia(old) != strip_dia(new) or old != new:
            if strip_dia(new) != new:
                ax.add("diacritic")
    a, b = strip_dia(old), strip_dia(new)
    if _hy(a) != _hy(b) or _sp(a) != _sp(b):
        ax.add("hyphen")
    if _hy(_sp(a)).lower() != _hy(_sp(b)).lower():
        ax.add("substance")
    return ax


# --- SEARCH_v1 / CASE_v1 ---
import urllib.request as _ur, urllib.parse as _up, json as _js, time as _tm
_UA={"User-Agent":"nipponexus/1.0 (research; contact via repo)"}

def _get(url, tries=2):
    for i in range(tries):
        try:
            rq=_ur.Request(url, headers=_UA)
            with _ur.urlopen(rq, timeout=20) as r:
                return _js.loads(r.read().decode("utf-8"))
        except Exception:
            _tm.sleep(2.0*(i+1))
    return None

def kana_by_search(term):
    """記事が無い地名を、本文中の『term（よみ）』から拾う"""
    u=("https://ja.wikipedia.org/w/api.php?action=query&list=search"
       "&srsearch=%s&srlimit=3&format=json&utf8=1")%_up.quote(term)
    d=_get(u)
    if not d: return None,None
    for hit in (d.get("query",{}).get("search") or []):
        t=hit.get("title")
        _tm.sleep(1.5)
        e=("https://ja.wikipedia.org/w/api.php?action=query&prop=extracts"
           "&explaintext=1&titles=%s&format=json&utf8=1")%_up.quote(t)
        d2=_get(e)
        if not d2: continue
        for pg in (d2.get("query",{}).get("pages") or {}).values():
            body=pg.get("extract") or ""
            m=re.search(re.escape(term)+r"[（(]([ぁ-ゖー・]{2,20})[）)]", body)
            if m: return m.group(1), "jawiki-search(%s)"%t
    return None,None

_CASE={"shrine":"Shrine","station":"Station","temple":"Temple","park":"Park",
       "river":"River","castle":"Castle","museum":"Museum"}
def title_norm(s):
    """enwiki題名の 'Itakiso shrine' 型を 'Itakiso Shrine' に正規化"""
    if not s: return s
    out=[]
    for w in s.split(" "):
        out.append(_CASE.get(w.lower(), w))
    return " ".join(out)


# >>>NX:ORACLE_V3

# ORACLE_v3: canon_title 一本化。ppprop は付けない(wikibase_item が落ちる)。
# CACHE_TTL: キャッシュは30日で失効。canary は force=True で必ず実引きすること。
import os as _o3os, json as _o3json, time as _o3time
import urllib.parse as _o3up, urllib.request as _o3ur
_C3_UA = "NipponExus/1.0 (contact: yuki.shiori@nexus-ds.jp)"
_C3_CACHE = _o3os.path.expanduser("~/nipponexus/data/canon_cache.json")
_C3_TTL = 30 * 86400

def _c3_load():
    try:
        return _o3json.load(open(_C3_CACHE, encoding="utf-8"))
    except Exception:
        return {}

def _c3_save(c):
    d = _o3os.path.dirname(_C3_CACHE)
    if d:
        _o3os.makedirs(d, exist_ok=True)
    _o3json.dump(c, open(_C3_CACHE, "w", encoding="utf-8"), ensure_ascii=False)

def _c3_get(base, params):
    req = _o3ur.Request(base + "?" + _o3up.urlencode(params), headers={"User-Agent": _C3_UA})
    with _o3ur.urlopen(req, timeout=25) as h:
        return _o3json.loads(h.read().decode())

def canon_probe(title, force=False):
    cache = _c3_load()
    hit = cache.get(title)
    if (not force) and hit and (_o3time.time() - hit.get("_ts", 0) < _C3_TTL):
        return hit
    try:
        d = _c3_get("https://en.wikipedia.org/w/api.php",
                    {"action": "query", "format": "json", "formatversion": "2",
                     "redirects": "1", "prop": "coordinates|pageprops|extracts",
                     "exintro": "1", "explaintext": "1", "titles": title})
    except Exception as e:
        return {"state": "ERR", "why": str(e)[:80]}
    q = d.get("query", {})
    redir = {}
    for k in ("normalized", "redirects"):
        for r in q.get(k, []):
            redir[r["from"]] = r["to"]
    t = title
    seen = set()
    while t in redir and t not in seen:
        seen.add(t)
        t = redir[t]
    pages = {p.get("title"): p for p in q.get("pages", [])}
    p = pages.get(t)
    if p is None:
        out = {"state": "ERR", "why": "nopage"}
    elif p.get("missing"):
        out = {"state": "missing", "title": t}
    else:
        pp = p.get("pageprops") or {}
        co = (p.get("coordinates") or [{}])[0]
        out = {"state": "ok", "title": t, "lat": co.get("lat"),
               "qid": pp.get("wikibase_item"), "disambig": "disambiguation" in pp,
               "P625": None, "extract": (p.get("extract") or "")[:800]}
        if out["lat"] is None and out["qid"]:
            try:
                w = _c3_get("https://www.wikidata.org/w/api.php",
                            {"action": "wbgetentities", "format": "json",
                             "props": "claims", "ids": out["qid"]})
                ent = (w.get("entities") or {}).get(out["qid"], {})
                out["P625"] = "P625" in (ent.get("claims") or {})
            except Exception:
                pass
    if out.get("state") in ("ok", "missing"):
        out["_ts"] = _o3time.time()
        cache[title] = out
        _c3_save(cache)
    _o3time.sleep(2.5)
    return out

def canon_title(title, force=False):
    """個別実体と確認できた場合のみ正式タイトルを返す。概念記事/欠落/曖昧さ回避は None。"""
    d = canon_probe(title, force=force)
    if d.get("state") != "ok" or d.get("disambig"):
        return None
    if d.get("lat") is None and d.get("P625") is not True:
        return None
    if d["title"] != title and d["title"].lower() == title.lower():
        return None
    return d["title"]

# <<<NX:ORACLE_V3
