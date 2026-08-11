# -*- coding: utf-8 -*-
"""自律駆動の外枠(2026-08-06)。既存ファイルを文字列手術しない(00-17)。
★停止は終了でなく保留: run_one は status=stopped を『返す』ので、外側で hold して次へ進める。
★公開: poll_word で probe を決め nx.deploy へ渡す(run_one L141-144の空ループの代替)。
★判定はしない。正誤の決定は evidence_gate と人に委ねる。
"""
import os, sys, sqlite3, datetime, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DB = os.path.expanduser('~/nipponexus/data/sqlite/nipponexus.db')
SITE = 'https://nipponexus.com'

def _cx():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; return c

def pick(n=1, exclude_qids=()):
    c=_cx(); out=[]
    open_q={r['qid'] for r in c.execute("SELECT DISTINCT qid FROM hold_queue WHERE resolved_at IS NULL")}
    for r in c.execute("SELECT qid,label_ja,prefecture,priority_score FROM festivals "
        "WHERE status='pending' ORDER BY CAST(IFNULL(priority_score,0) AS REAL) DESC LIMIT 400"):
        if len(out)>=n: break
        if r['qid'] in exclude_qids or r['qid'] in open_q: continue
        out.append(dict(r))
    return out

def hold(qid, reason, detail=''):
    c=_cx()
    d=c.execute("SELECT id FROM hold_queue WHERE qid=? AND reason=? AND resolved_at IS NULL",(qid,reason)).fetchone()
    if d: return {'skipped':True,'id':d['id']}
    r=c.execute("SELECT label_ja FROM festivals WHERE qid=?",(qid,)).fetchone()
    cur=c.execute("INSERT INTO hold_queue(qid,label_ja,reason,detail,created_at) VALUES(?,?,?,?,?)",
        (qid, r['label_ja'] if r else None, reason, detail[:2000],
         datetime.datetime.now().isoformat(timespec='seconds')))
    c.commit(); return {'inserted':cur.lastrowid}

def holds(open_only=True):
    c=_cx(); q="SELECT * FROM hold_queue"+(" WHERE resolved_at IS NULL" if open_only else "")+" ORDER BY id"
    return [dict(r) for r in c.execute(q)]

def resolve(hid, resolution='ok'):
    c=_cx(); c.execute("UPDATE hold_queue SET resolved_at=?,resolution=? WHERE id=? AND resolved_at IS NULL",
        (datetime.datetime.now().isoformat(timespec='seconds'),resolution,hid)); c.commit()
    return {'resolved':c.total_changes}

def probes_for(qid):
    """新規記事は本番に頁が無い(404)ので live='' として扱う。"""
    import poll_word as pw
    slug_ja, slug_en, ja, en = pw.load(qid)
    ju, eu = '%s/%s/'%(SITE,slug_ja), '%s/en/%s/'%(SITE,slug_en)
    def live(u):
        try: return pw.fetch(u)
        except Exception: return ''
    wj, we = pw.pick(ja, live(ju), 14), pw.pick(en, live(eu), 40)
    if not wj or not we: raise RuntimeError('probe語なし(既に反映済かDB未更新): ja=%r en=%r'%(wj,we))
    return {ju: wj, eu: we}

def run_batch(n=1, deploy=False, qids=None):
    """選題→run_one→停止なら保留して次へ→完走分をまとめて1回だ�push。"""
    import run_one, nx
    targets = [{'qid':q,'label_ja':None} for q in qids] if qids else pick(n)
    done=[]; held=[]
    for t in targets:
        q=t['qid']; print('\n########## %s %s ##########'%(q, t.get('label_ja') or ''))
        try:
            res = run_one.run(q, deploy=False)
        except Exception:
            hold(q,'例外',traceback.format_exc()); held.append((q,'例外')); continue
        st = res.get('status')
        if st == 'stopped':
            hold(q,'停止条件','; '.join(res.get('reasons') or [])); held.append((q,res.get('reasons'))); continue
        set_month(q)
        if st != 'written':
            hold(q,'想定外status',str(res)); held.append((q,st)); continue
        done.append(q)
    out={'done':done,'held':held,'open_holds':len(holds())}
    if deploy and done:
        pr={}
        for q in done:
            try: pr.update(probes_for(q))
            except Exception as e: hold(q,'probe不成立',str(e)); out['held'].append((q,'probe'))
        if pr:
            out['deploy']=nx.deploy('auto: %d articles (%s)'%(len(done), ','.join(done)), probes=pr)
    return out


_PAT=[r'毎年\s*(\d{1,2})\s*月', r'(\d{1,2})\s*月\s*[上中下]旬', r'(\d{1,2})\s*月\s*\d{1,2}\s*日', r'(\d{1,2})\s*月に']
_KAN={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'十一':11,'十二':12}
_KP=[r'毎年\s*(十[一二]?|[一二三四五六七八九])月', r'(十[一二]?|[一二三四五六七八九])月\s*[上中下]旬',
     r'(十[一二]?|[一二三四五六七八九])月\s*[一二三四五六七八九十]{1,3}日']
_NEG=None; _S2M={'spring':{3,4,5},'summer':{6,7,8},'autumn':{9,10,11},'winter':{12,1,2}}
_M2S={m:s for s,ms in _S2M.items() for m in ms}

def set_month(qid):
    """投入後の start_month 確定。本文から一意に決まる時だけ書く(決まらなければ保留)。"""
    import re, nx
    global _NEG
    if _NEG is None: _NEG=re.compile(r'(旧暦|指定|制定|創建|創設|記念|登録|認定|\d{2,4}年|元年|世紀)')
    c=_cx(); r=c.execute("SELECT label_ja,season,start_month,manual_content_ja FROM festivals WHERE qid=?",(qid,)).fetchone()
    if r is None: return {'error':'not found'}
    if r['start_month']: return {'skipped':True,'start_month':r['start_month']}
    t=r['manual_content_ja'] or ''; res=set()
    for p in _PAT+_KP:
        for m in re.finditer(p,t):
            pre=t[max(0,m.start()-14):m.start()]
            if _NEG.search(pre): continue
            g=m.group(1); v=_KAN.get(g) if g in _KAN else (int(g) if g.isdigit() else None)
            if v and 1<=v<=12: res.add(v)
    allow=_S2M.get((r['season'] or '').strip().lower())
    hit=(res&allow) if allow else res
    if len(hit)!=1:
        hold(qid,'start_month未確定','候補=%s season=%s'%(sorted(res),r['season']))
        return {'held':True,'cands':sorted(res)}
    mo=list(hit)[0]; kv={'start_month':mo}
    if not r['season'] and _M2S.get(mo): kv['season']=_M2S[mo]
    nx.setmeta(qid,**kv); return {'set':kv}


# FINALIZE_v1  確定処理: slug必須・検査通過・字数検算のうえ status=drafted
import sqlite3 as _s3, re as _re2
def finalize(qid, apply=False):
    import deepseek_draft as dd
    c=_s3.connect(DB); c.row_factory=_s3.Row
    r=c.execute("""SELECT qid,label_ja,slug_ja,slug_en,status,manual_content_ja ja,
                   manual_content_en en FROM festivals WHERE qid=?""",(qid,)).fetchone()
    if not r: return {"qid":qid,"ok":False,"why":"DBに無い"}
    if not (r["slug_ja"] and r["slug_en"]): return {"qid":qid,"ok":False,"why":"slug未設定"}
    ja,en=r["ja"] or "", r["en"] or ""
    lj,le=len(ja),len(en)
    if lj<2400: return {"qid":qid,"ok":False,"why":f"ja={lj}<2400"}
    # 2026-08-07: nx.write と同一基準へ統一(従来1.7倍のみで二重基準だった)。
    #   既存draftedは再finalizeされないため遡及影響なし(呼び出し元=pending限定を確認済)。
    if not (le >= lj*2 or (le >= 8000 and le >= lj*1.7)):
        return {"qid":qid,"ok":False,"why":f"en不足 {le}/{lj} (要 2.0倍 or 8000字かつ1.7倍)"}
    # 2026-08-07: 区切り残留。字数・比率は満たすため既存ゲートを素通りしていた
    #   (朝の4本=斎王/石取/田辺/貴船が==EN==・===EN===を含んだまま公開された経路)
    _sep=_re2.search(r"={2,}\s*EN\s*={2,}", ja+"\n"+en)
    if _sep: return {"qid":qid,"ok":False,"why":f"EN区切り残留: {_sep.group(0)!r}"}
    # NXPREF_v1 (2026-08-07): 公開直前の県名整合ガード。desc矛盾/座標bbox外で停止。
    import nxpref as _nxp
    _pok,_pwhy=_nxp.check(c.execute('SELECT prefecture,description_ja,latitude,longitude FROM festivals WHERE qid=?',(qid,)).fetchone())
    if not _pok: return {"qid":qid,"ok":False,"why":"県名NG: "+_pwhy}
    ng,lines=dd.run_all_checks(qid,ja,en)
    if ng: return {"qid":qid,"ok":False,"why":"検出器NG","lines":[l for l in lines if "NG" in l]}
    if not apply: return {"qid":qid,"ok":True,"why":"dry(未書込)","ja":lj,"en":le,"slug":r["slug_ja"]}
    c.execute("UPDATE festivals SET status='drafted', published_at=NULL WHERE qid=?",(qid,))
    c.commit(); c.close()
    return {"qid":qid,"ok":True,"why":"drafted確定","ja":lj,"en":le,"slug":r["slug_ja"]}


# AUTOSLUG_v1  slug自動生成(label_en基準)と一括確定
import unicodedata as _ud
_STOP=set()  # 実測: 除外なしが最良(59%)
def slugify(en):
    if not en: return ''
    s=_ud.normalize('NFKD',en).encode('ascii','ignore').decode().lower()
    w=[x for x in _re2.split(r'[^a-z0-9]+',s) if x and x not in _STOP]
    return '-'.join(w)
def ensure_slug(qid, apply=False):
    c=_s3.connect(DB); c.row_factory=_s3.Row
    r=c.execute("SELECT qid,label_ja,label_en,slug_ja FROM festivals WHERE qid=?",(qid,)).fetchone()
    if not r: return None
    if r['slug_ja']: c.close(); return r['slug_ja']
    base=slugify(r['label_en'])
    if not base: c.close(); return None
    s=base; i=2
    while c.execute("SELECT 1 FROM festivals WHERE (slug_ja=? OR slug_en=?) AND qid!=?",(s,s,qid)).fetchone():
        s=f"{base}-{i}"; i+=1
    if apply:
        c.execute("UPDATE festivals SET slug_ja=?,slug_en=? WHERE qid=?",(s,s,qid)); c.commit()
    c.close(); return s
def finalize_all(apply=False):
    c=_s3.connect(DB); c.row_factory=_s3.Row
    rows=c.execute("""SELECT qid FROM festivals WHERE status='pending'
      AND manual_content_ja IS NOT NULL AND manual_content_ja!=''""").fetchall()
    c.close(); out=[]
    for r in rows:
        s=ensure_slug(r['qid'], apply=apply)
        res=finalize(r['qid'], apply=apply)
        res['slug_auto']=s; out.append(res)
        if not res['ok']: hold(r['qid'],'finalize不可',res.get('why',''))
    return out


def run_full(n=1, deploy=False):
    """選題→生成→検出→Pro→start_month→slug→drafted確定 を一本で通す。
    【2026-08-07訂正】「pushは別」ではない。drafted確定=公開確定。
    site側が status IN ('drafted','published') で引くため、deploy=False でも
    当夜23時のcronがdump差分をpushして公開される。finalize(apply=True) が公開ボタン。"""
    import run_one
    # 2026-08-07: 重複定義の静かな後勝ちを生成前に止める(pick_safeが811B完全一致で潜在)
    import nxcheck as _nc
    _dup=_nc.scan_dups()
    if _dup: raise AssertionError('重複定義を検出=生成前に停止: %s' % _dup)
    res={'done':[],'held':[],'failed':[]}
    for t in pick_safe(n):
        qid=t['qid']
        print('\n########## %s %s (score=%s) ##########'%(qid, t.get('label_ja') or '', t.get('priority_score')))
        try:
            out=run_one.run(qid, deploy=False)
        except Exception as e:
            import traceback as _tb   # TRACE_v1
            _t=_tb.format_exc()
            print(_t)
            hold(qid,'実行例外',(str(e)+' || '+_t[-400:])[:800])
            res['failed'].append((qid,str(e)[:80])); continue
        st=out.get('status') if isinstance(out,dict) else str(out)
        if st=='stopped':   # RETRY_ONCE_v1 生成は確率的。再生成を1回だけ試す
            print('  [retry] 停止 → 1回だけ再生成して再判定')
            try: out=run_one.run(qid, deploy=False)
            except Exception as e:
                hold(qid,'実行例外(再試行時)',str(e)[:300]); res['failed'].append((qid,'retry例外')); continue
            st=out.get('status') if isinstance(out,dict) else str(out)
            if st=='stopped':
                hold(qid,'停止条件(2回)','; '.join(map(str,out.get('reasons') or []))[:400])
                res['held'].append((qid,'stopped x2')); continue
        if st!='written':
            hold(qid,'想定外status',str(out)[:300]); res['held'].append((qid,st)); continue
        try: set_month(qid)
        except Exception as e: print("  [warn] set_month:",e)
        ensure_label_en(qid, apply=True)  # LABEL_EN_FROM_BODY_20260810
        s=ensure_slug(qid, apply=True)
        f=finalize(qid, apply=True)
        if f['ok']: res['done'].append({'qid':qid,'slug':s,'ja':f.get('ja'),'en':f.get('en')})
        else: hold(qid,'確定不可',f.get('why','')); res['held'].append((qid,f.get('why')))
    res['open_holds']=len([h for h in holds() if not h['resolved_at']])
    return res
# RUN_FULL_v2  pick(n, exclude_qids) の実シグネチャに準拠
def pick_safe(n, exclude_qids=()):
    """label_ja(生成に必要)/label_en(slugに必要)が欠けた行は選題から外す。
       保留キューには入れない(データ欠落でありPro判断не要・後で一括補完する)。"""
    got=[]; skipped={'label_ja':0,'label_en':0}
    for q in pick(n*8, exclude_qids=exclude_qids):
        qid=q['qid']
        c=_s3.connect(DB); c.row_factory=_s3.Row
        r=c.execute("SELECT label_ja,label_en FROM festivals WHERE qid=?",(qid,)).fetchone(); c.close()
        if not r: continue
        if not (r['label_ja'] or '').strip(): skipped['label_ja']+=1; continue
        # LABEL_EN_FROM_BODY_20260810: label_en は生成後に本文から確定するため選題条件から除外
        # (旧: ここで271本を落としていた。label_ja のみ必須)
        got.append(q)
        if len(got)>=n: break
    if skipped['label_ja']:
        print("  [pick_safe] label_ja 欠落でスキップ: %d 件"%skipped['label_ja'])
    return got



# ===== LABEL_EN_FROM_BODY_20260810 =====
# label_en は slug 生成にしか使われず(227行の注記どおり)、記事内容には影響しない。
# Wikidata に無い271本(prefecture有109本)が選題から外れていたため、生成済み英語本文の
# Overview 直後1文目から英題を確定する。実測: 抽出成功96.6% / 既存slug一致50% /
# 類似0.8以上を含め約74%。差異の多くは既存slugが人手短縮されたもので抽出側が正式名称。
# 既存 label_en は上書きしない(Expo '90 のような良質な短縮を壊さないため)。
def extract_en_title(en):
    if not en: return None
    body = _re2.sub(r'^\s*#+\s*\w[\w \'-]*\s*$', '', en, flags=_re2.M)
    body = _re2.sub(r'^[\s\n]+', '', body)
    first = _re2.split(r'(?<=[.!?])\s', body.strip())[0] if body.strip() else ''
    m = _re2.match(r'^(?:The\s+)?([A-Z][A-Za-z0-9\u00C0-\u024F\'\u2019 .&-]{2,60}?)'
                   r'\s*(?:\(|,|\s(?:is|was|are|were|takes|has|refers))', first)
    if m:
        t = m.group(1).strip(' .,&')
        if len(t.split()) <= 8 and _re2.search(r'[A-Za-z]', t): return t
    return None

def ensure_label_en(qid, apply=False):
    """英語本文から label_en を確定する。既存値がある場合は触らない。"""
    c = _s3.connect(DB); c.row_factory = _s3.Row
    r = c.execute("SELECT label_en, manual_content_en FROM festivals WHERE qid=?", (qid,)).fetchone()
    if not r: c.close(); return None
    if (r['label_en'] or '').strip(): c.close(); return r['label_en']
    t = extract_en_title(r['manual_content_en'])
    if t and apply:
        c.execute("UPDATE festivals SET label_en=? WHERE qid=?", (t, qid)); c.commit()
    c.close(); return t
