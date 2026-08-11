# -*- coding: utf-8 -*-
"""run_one: 1本を生成->機械検出->Pro照合ループ->自動是正->DB投入->(任意で)デプロイまで
1コマンドで通す単一入口(2026-08-03)。自律運転の本体。

★停止条件(fail-closed): 以下のいずれかで停止し人へ回す。
  (1) Proループの未解決赤字が残る(verdict != detector_false_positive)
  (2) 検出器NG(nx.checks)が残る
  (3) 字数/構造の検算NG・見出し0件
  (4) 不変条件違反(nx.write内)
★verdict=detector_false_positive はProが偽陽性と判定した赤字=停止理由にしない
  (138姫路: 赤字を誤りと決めつける契約だったためProが偽陽性を弾けなかったことの是正)。
★【2026-08-07訂正】draftedにした時点で公開される。site/src/lib/festivals.ts:41 が
  status IN ('drafted','published') で引くため、--deploy を付けなくても当夜23時のcron
  (nightly_rebuild.sh)がdump差分をpushし公開される。投入=公開として扱うこと。
  --deploy は「即座にpushするか」の違いに過ぎず、公開の可否ゲートではない。
"""
import os, sys, json, argparse, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deepseek_draft as dd
import pro_verify_loop as pv
import nx
import re

FP = "detector_false_positive"


def _gen(qid):
    """生成工程は既存mainを再利用せず必要部分のみ呼ぶ(mainは人向けの出力で終わるため)。"""
    key = dd.get_key()
    row = dd.pick(qid, False)
    label = row.get("label_ja") or ""
    pref = row.get("prefecture") or ""
    data = dd.call(dd.RULES_TMPL.format(pref=pref, label=label), key)
    msg = data["choices"][0]["message"]
    ja, en, fb = dd.split_ja_en(msg.get("content") or "")
    ja, en = dd.strip_citations(ja), dd.strip_citations(en)
    cites = [x.get("url_citation", {}).get("url") for x in (msg.get("annotations") or [])
             if x.get("type") == "url_citation"]
    dd.OUT.mkdir(parents=True, exist_ok=True)
    (dd.OUT / f"{qid}_deepseek_full.md").write_text(ja + "\n\n===EN===\n\n" + en)
    (dd.OUT / f"{qid}_cites.txt").write_text("\n".join(cites))
    # ★2026-08-03・139湯涌: 既存mainにある出典本文キャッシュの生成を_genへ写していなかった。
    #   結果『権威属性の出典共起/役割共起』がSKIPし、Proループの赤字が0件になった。
    #   赤字0件は品質が良いのではなく検査が走っていない状態=最も危険な偽の合格。
    bodies = [t for t in (dd._fetch_text(u) for u in cites) if t]
    (dd.OUT / f"{qid}_cites_body.txt").write_text("\n".join(bodies))
    print(f"  出典本文キャッシュ {sum(len(t) for t in bodies)}字 / {len(bodies)}件")
    return dict(key=key, label=label, pref=pref, ja=ja, en=en, cites=cites, fb=fb)


def _read_cites(qid):  # NXAPPLY_v3: cites欠落でも止めない
    p = dd.OUT / f"{qid}_cites.txt"
    if not p.exists():
        print(f"[reuse] cites無し(出典照合は縮退): {p.name}")
        return []
    return [l for l in p.read_text().split("\n") if l.strip()]


def run(qid, deploy=False, reuse=False, write=True):
    if reuse:
        p = dd.OUT / f"{qid}_deepseek_full.md"
        if not p.exists():  # NXAPPLY_v3: バッチ中1記事の欠落で全体を落とさない
            print(f"[reuse] 生成物なし=スキップ: {p.name}")
            return {"qid": qid, "status": "skipped", "reason": "生成物なし(--reuse)"}
        _t = p.read_text()
        _m = re.search(r"\n\s*={2,}\s*EN\s*={2,}\s*\n", _t)
        if not _m:
            print(f"[reuse] 区切りなし=スキップ: {p.name}")
            return {"qid": qid, "status": "skipped", "reason": "===EN===区切りなし"}
        ja, en = _t[:_m.start()].strip(), _t[_m.end():].strip()
        row = dd.pick(qid, False)
        g = dict(key=dd.get_key(), label=row.get("label_ja") or "", pref=row.get("prefecture") or "",
                 ja=ja, en=en, fb=False,
                 cites=_read_cites(qid))
        print(f"[reuse] 既存生成物を使用 ja={len(ja)} en={len(en)}")
    else:
        g = _gen(qid)
        print(f"[生成] {g['label']} ja={len(g['ja'])} en={len(g['en'])} cites={len(g['cites'])}")
    ja, en = g["ja"], g["en"]

    vr = dd.verify(ja, en)
    print(f"[検算] {vr}")
    stop = []
    if not vr.get("ok"):
        stop.append(f"検算NG {vr}")
    if vr.get("h", 0) == 0:
        stop.append("見出し0件(6セクション欠落=136嵐山型の生成事故)")

    ng, lines = nx.checks(qid, ja, en)
    print("\n".join(lines))
    # ★検査未実行(SKIP)を合格として扱わない(139湯涌)
    skipped = [l.strip() for l in lines if "SKIP" in l]

    # ★2026-08-04: 戻り値の第一要素(ng_any)を捨てていたため、run_all_checksへ
    #   8番として接続したfield_check(必須フィールドの欠落)が停止に寄与していなかった。
    #   nx.checksのngとは対象項目が異なるので両方を停止条件に使う(139のSKIP同型の穴)。
    checks_ng, run_lines = dd.run_all_checks(qid, ja, en, strict=False)
    payload, report = pv.run(qid, g["label"], g["pref"], ja, en, g["cites"], run_lines,
                             g["key"], dd.call, dd.MODEL_PRO, fetch_sources=True)
    (dd.OUT / f"{qid}_pro_verify.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(report)

    fixes = payload.get("verified_fixes") or []
    # LEDGER_v1 2026-08-10: Proは非決定的で、同じ案件がverified_fixesに来たり来なかったりする
    # (Q5288609は前回confirmed_wrong / 今回unresolved)。WD完全一致で確定済みの判定は
    # 台帳から注入し、自動反映をProの揺れから切り離す。反映可否は従来どおり五重ガードが決める。
    try:
        import sqlite3 as _s3, os as _os
        _db = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                            "data", "sqlite", "nipponexus.db")
        _cx = _s3.connect(_db)
        _rows = _cx.execute("SELECT tkey,old,new FROM verdict_ledger "
                            "WHERE qid=? AND src='WD_EXACT'", (qid,)).fetchall()
        _cx.close()
        _have = {((f.get("old") or ""), (f.get("new") or "")) for f in fixes}
        for _tk, _o, _n in _rows:
            if (_o, _n) in _have: continue
            fixes.append({"detector": "translit_check", "verdict": "confirmed_wrong",
                          "old": _o, "new": _n, "target_excerpt": _tk,
                          "evidence_verified": True, "src": "LEDGER"})
            print("[ledger] 台帳から注入: %r -> %r" % (_o, _n))
    except Exception as _le:
        print("[ledger] 注入スキップ: %s" % _le)
    unresolved = [u for u in (payload.get("unresolved") or []) if u.get("verdict") != FP]
    fpn = len(payload.get("unresolved") or []) - len(unresolved)
    print(f"[Proループ] 検証通過{len(fixes)}件 / 未解決{len(unresolved)}件 / 偽陽性判定{fpn}件")

    # NXAPPLY_v3(2026-08-10): 検証通過(verified_fixes)のうちold/new型(音写是正)は
    # selected_candidateを持たないためnx.fixのpairsに乗らず、unresolvedにも来ないので
    # nxgate側のフックも通らず素通りしていた。反映はここで行う(入口の取り違えの是正)。
    try:
        import nxapply
        _pl = []
        for f in fixes:
            p, why = nxapply.plan(qid, dict(f, evidence_verified=True), ja, en)
            if p: _pl.append(p)
        if _pl:
            ja, en, _done = nxapply.apply_plans(qid, _pl, ja, en)
            print(f"[nxapply] 検証通過から{len(_done)}件を本文へ反映")
    except Exception as _e:
        print('[nxapply] skip: %r' % (_e,))

    pairs = [(f["target_excerpt"], f["selected_candidate"]) for f in fixes
             if f.get("target_excerpt") and f.get("selected_candidate")
             and f["target_excerpt"] in ja]
    if pairs:
        ja2, log = nx.fix(ja, pairs, min_hits=1)
        print(f"[自動是正] {log}")
        # 2026-08-06: nx.pairs(全文照合+複数一致を曖昧として確定させない)へ昇格済みなのに
        # run_oneは旧経路 pc.en_counterpart(o[:40]) を呼び続けていた=昇格の未配線。
        # ★2026-08-10(NXAPPLY_v3)撤回: 上の「EN側は機械適用が成立しない」は当時の判断で、
        #   以後のnx.pairs昇格とtranslit_norm整形を経ても見直されず272件を人手に積み続けた。
        #   実測: 272件全てoldが本文に実在し全置換で反映可。Proにja/enを見せてold/newを
        #   書かせ、evidence通過分のみnxapplyが反映する(反映不可は従来どおり人へ)。
        rs, bad = nx.pairs(pairs, ja, en)
        for (o, _), r in zip(pairs, rs):
            tag = "確定" if r.get("found") else ("曖昧" if r.get("ambiguous") else "不在")
            print(f"  [EN対応/{tag}] {o[:24]} -> {r.get('en_head')}")
        if bad:  # NXAPPLY_v3: EN側が全件確定なら停止理由にしない(未確定のみ止める)
            stop.append("EN側の対応是正が未適用(JA是正%d件 / EN未確定あり=表記要確認)" % len(pairs))
        else:
            print("[自動是正] EN対応 全件確定=停止理由にしない")
        ja = ja2

    import nxgate  # 2026-08-06: 誰も誤りと言っていない項目で停止しない(決定論トリアージ)
    unresolved = nxgate.triage(qid, unresolved, ja, en)
    if unresolved:
        stop += [f"未解決赤字: {u.get('detector')} {u.get('target_excerpt','')[:40]} / {u.get('note','')[:60]}"
                 for u in unresolved]
    if ng:
        stop.append("検出器NGが残存")
    if checks_ng:
        stop.append("run_all_checks NGが残存(必須フィールドの欠落等)")
    if skipped:
        stop += ["検査未実行(SKIP)=合格ではない: " + s for s in skipped]

    # ★2026-08-03: --reuseで是正前の生成物を読み、是正済みの本番本文(ja4693)を
    #   生成時点の版(ja4591)へ上書きする事故を起こした。生成物は常に是正前なので、
    #   DB側が長い/是正済み語を持つ場合は上書きを禁じる(不可逆に近い破壊のため)。
    _row = dd.pick(qid, False)
    _dbja = _row.get("manual_content_ja") or ""
    if len(_dbja) > len(ja):
        stop.append("DB現本文(ja%d)が生成物(ja%d)より長い=是正済みの上書きの疑い"
                    % (len(_dbja), len(ja)))

    if stop:
        print("\n===== 停止(人へ回す) =====")
        for s in stop:
            print(" -", s)
        return {"qid": qid, "status": "stopped", "reasons": stop}

    if not write:
        print("[reuse] --write未指定のためDB書込みを行わない(経路確認モード)")
        return {"qid": qid, "status": "dry"}
    # CAS_v1 2026-08-10: old_ja/old_en省略でnx.writeのCASガードに弾かれ書込み不能だった。
    # 直前のDB現本文を照合トークンとして渡す。是正済み上書き事故はL163の長さ検査が担当。
    import sqlite3 as _s3
    _c = _s3.connect(os.path.expanduser('~/nipponexus/data/sqlite/nipponexus.db'))
    _r0 = _c.execute("SELECT manual_content_ja, manual_content_en FROM festivals WHERE qid=?", (qid,)).fetchone()
    _oja, _oen = (_r0[0] or ''), (_r0[1] or '')
    if (ja, en) == (_oja, _oen):
        print('[write] 差分なし=書込み省略')
    elif not _oja:   # NEWROW_v1 2026-08-11: 新規投入はold_ja=Noneが正規入口(行数検査は対象外)
        print('[write] 新規投入(DB現本文なし)')
        print(nx.write(qid, ja, en))
    else:
        print(nx.write(qid, ja, en, old_ja=_oja, old_en=_oen, allow_line_delta=0))
    row = dd.pick(qid, False)
    if not row.get("start_month"):
        print("[WARN] start_month未設定=setmetaで要指定")
    if not deploy:
        print("[書込完了] DBへ本文を投入。status遷移は未実施(nxauto.ensure_slug+finalizeが必要)")
        return {"qid": qid, "status": "written"}
    probes = {}
    for w in ("特典", "会場"):
        pass
    return {"qid": qid, "status": "written", "note": "deployは投入語句選定後に別途"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--qid", required=True)
    ap.add_argument("--deploy", action="store_true")
    ap.add_argument("--reuse", action="store_true")
    ap.add_argument("--write", action="store_true", help="--reuse時にDBへ書く")
    a = ap.parse_args()
    print(json.dumps(run(a.qid, a.deploy, a.reuse, a.write or not a.reuse), ensure_ascii=False, indent=2))
