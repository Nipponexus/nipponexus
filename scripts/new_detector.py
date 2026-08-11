#!/usr/bin/env python3
"""検出器登録プロトコル。
登録条件（すべて満たさないと registry に載らない）:
  A 実データ由来の赤ケースが1件以上（DB実本文から抽出したもの）
  B 修正前FAIL→修正後PASS の遷移を機械確認
  C 判定は決定論的な文字列/構造検査のみ（真偽判断・外部照会を含まない）
  D 登録と同時に全記事へ遡及適用し、NG本数を記録
  E 遡及NG率が25%以下（2026-08-09追加: 294本中290本を叩く検出器が登録を通った事故）
使い方: register(spec) -> dict
"""
import os, json, datetime, sqlite3, inspect
H=os.path.expanduser("~")
REG=os.path.join(H,"nexus_data","llm_sim","detector_registry.json")

def _load():
    return json.load(open(REG,encoding="utf-8")) if os.path.exists(REG) else {"detectors":[]}

def _save(d):
    os.makedirs(os.path.dirname(REG),exist_ok=True)
    json.dump(d,open(REG,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

def register(spec, db_rows):
    """spec: {no,name,origin_defect,fn,cases:[(label,text,qid,expect_ng,from_real_data)]}"""
    errs=[]
    fn=spec["fn"]
    src=inspect.getsource(fn)
    for bad in ("requests","urllib","http","openai","input(","random"):
        if bad in src: errs.append(f"C違反: 非決定論的要素 {bad}")
    real=[c for c in spec["cases"] if c[4]]
    if not real: errs.append("A違反: 実データ由来ケースが0件")
    if not any(c[3] for c in real): errs.append("A違反: 実データ由来の赤ケース(expect_ng=True)が0件")
    fails=[]
    for label,text,qid,expect,_ in spec["cases"]:
        got=bool(fn(text,qid))
        if got!=expect: fails.append(label)
    if fails: errs.append("B違反: 期待と不一致 "+", ".join(fails))
    if errs:
        return {"registered":False,"errors":errs}
    ng=[]
    for qid,label,ja,en in db_rows:
        if fn((ja or "")+"\n"+(en or ""),qid): ng.append(qid)
    rate=len(ng)/len(db_rows) if db_rows else 0.0
    if rate>0.25:
        return {"registered":False,"retro_ng":len(ng),"retro_rate":round(rate,3),
                "errors":[f"E違反: 遡及NG率{rate:.1%}が上限25%超。検出器でなく仕様誤読の疑い"]}
    d=_load()
    d["detectors"]=[x for x in d["detectors"] if x.get("no")!=spec["no"]]
    d["detectors"].append({
        "no":spec["no"],"name":spec["name"],"origin_defect":spec["origin_defect"],
        "registered_at":datetime.datetime.now().isoformat(timespec="seconds"),
        "cases":len(spec["cases"]),"real_cases":len(real),
        "retro_scanned":len(db_rows),"retro_ng":len(ng),"retro_rate":round(rate,3),"retro_ng_qids":ng[:50]})
    d["detectors"].sort(key=lambda x:str(x.get("no") or x.get("id") or ""))
    _save(d)
    return {"registered":True,"retro_scanned":len(db_rows),"retro_ng":len(ng),"retro_rate":round(rate,3),"ng_qids":ng}
