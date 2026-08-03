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
★pushは不可逆(00-A12)のため既定で行わない。--deploy 指定時のみ。
"""
import os, sys, json, argparse, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deepseek_draft as dd
import pro_verify_loop as pv
import nx

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
    return dict(key=key, label=label, pref=pref, ja=ja, en=en, cites=cites, fb=fb)


def run(qid, deploy=False, reuse=False, write=True):
    if reuse:
        p = dd.OUT / f"{qid}_deepseek_full.md"
        ja, en = p.read_text().split("\n\n===EN===\n\n")
        row = dd.pick(qid, False)
        g = dict(key=dd.get_key(), label=row.get("label_ja") or "", pref=row.get("prefecture") or "",
                 ja=ja, en=en, fb=False,
                 cites=[l for l in (dd.OUT / f"{qid}_cites.txt").read_text().split("\n") if l.strip()])
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

    _, run_lines = dd.run_all_checks(qid, ja, en, strict=False)
    payload, report = pv.run(qid, g["label"], g["pref"], ja, en, g["cites"], run_lines,
                             g["key"], dd.call, dd.MODEL_PRO, fetch_sources=True)
    (dd.OUT / f"{qid}_pro_verify.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(report)

    fixes = payload.get("verified_fixes") or []
    unresolved = [u for u in (payload.get("unresolved") or []) if u.get("verdict") != FP]
    fpn = len(payload.get("unresolved") or []) - len(unresolved)
    print(f"[Proループ] 検証通過{len(fixes)}件 / 未解決{len(unresolved)}件 / 偽陽性判定{fpn}件")

    pairs = [(f["target_excerpt"], f["selected_candidate"]) for f in fixes
             if f.get("target_excerpt") and f.get("selected_candidate")
             and f["target_excerpt"] in ja]
    if pairs:
        ja2, log = nx.fix(ja, pairs, min_hits=1)
        print(f"[自動是正] {log}")
        import pair_check as pc
        for o, _ in pairs:
            r = pc.en_counterpart(ja, en, o[:40])
            print(f"  [EN対応要確認] {o[:24]} -> {str(r)[:110]}")
            stop.append(f"EN側の対応是正が未確定(還元R): {o[:24]}")
        ja = ja2

    if unresolved:
        stop += [f"未解決赤字: {u.get('detector')} {u.get('target_excerpt','')[:40]} / {u.get('note','')[:60]}"
                 for u in unresolved]
    if ng:
        stop.append("検出器NGが残存")

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

    if reuse and not write:
        print("[reuse] --write未指定のためDB書込みを行わない(経路確認モード)")
        return {"qid": qid, "status": "dry"}
    print(nx.write(qid, ja, en))
    row = dd.pick(qid, False)
    if not row.get("start_month"):
        print("[WARN] start_month未設定=setmetaで要指定")
    if not deploy:
        print("[投入完了・push未実施] --deploy 指定時のみpush(不可逆・00-A12)")
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
