# -*- coding: utf-8 -*-
"""pro_verify_loop: 機械検出の赤字を入力にProが一次照合を複数回まわし
修正案(old/new+根拠URL)を構造化JSONで出力する(2026-07-29・分担逸脱の是正)。
★C-3b堅持: Proの修正案も正解データとして採用しない。決定論ゲート(evidence照合)で
   newの核心固有名が出典本文に実在するかを検証し、実在しなければunresolvedへ降格。"""
import re, json
import authority_check as ac
import ephemeral_src as es

def _fetch(url, timeout=12):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            enc = r.headers.get_content_charset() or "utf-8"
            return raw.decode(enc, errors="replace")
    except Exception:
        return ""

def collect_defects(qid, ja, en, cites, run_all_lines, fetch_sources=False):
    defects = []
    cur = ""
    for ln in (run_all_lines or []):
        if "NG" in ln and "OK" not in ln:
            cur = ln.strip()
        elif ln.strip().startswith("L") and cur:
            defects.append({"detector": "run_all_checks", "field": cur,
                            "excerpt": ln.strip(), "detail": cur + " / " + ln.strip()})
    sources_text = ""
    if fetch_sources:
        docs = []
        for u in cites or []:
            t = _fetch(u)
            if t: docs.append(t)
        sources_text = "\n".join(docs)
        ng, lines = ac.check(ja, sources_text)
        for ln in lines:
            if "×出典に不在" in ln:
                m = re.search(r"L\d+\s+(\S+)\s+:", ln)
                name = m.group(1) if m else ln.strip()
                defects.append({"detector": "authority_check", "field": "権威属性",
                                "excerpt": name, "detail": ln.strip()})
        names = [d["excerpt"] for d in defects if d["detector"] == "authority_check"]
        if names:
            ng2, lines2 = es.check(names, docs)
            for ln in lines2:
                if "×単年候補" in ln:
                    m = re.search(r"^\s*(\S+)\s+:", ln)
                    n = m.group(1) if m else ln.strip()
                    defects.append({"detector": "ephemeral_src", "field": "単年候補",
                                    "excerpt": n, "detail": ln.strip()})
    return defects, sources_text

def pro_verify(qid, label, pref, defect, key, call_fn, model_pro, candidates=None):
    """赤字1件に対しProを呼び判定する。還元T(2026-07-29): 候補がある場合は
       Proは正解を生成せず候補から選択するのみ(幻覚の余地なし)。
       candidates=Noneの場合は従来通り生成モード(候補抽出が空の場合のフォールバック)。
       出力: verdict(confirmed_wrong/confirmed_correct/unverifiable)
             + selected_candidate(候補選択時のみ) + evidence_urls + note。
       newは生成しない(正解値の生成はProの役割でない=120で実証)。"""
    exc = defect["excerpt"][:400]
    det = defect["detector"]
    if candidates:
        cand_list = "\n".join(f"- {name}" for name, _ in candidates[:5])
        prompt = (
            "日本の祭り記事のファクトチェッカーです。検出器が以下の箇所に『出典に不在/定型流し込みの疑い』の赤字を出しました。"
            "以下の候補団体名の中から、正しい主催/団体名を選択してください。候補は出典本文から決定論で抽出したもので、いずれかが正解です。\n"
            "★出力は必ず次のJSONのみ(前置き・説明・コードフェンス禁止):\n"
            '{"verdict":"confirmed_wrong(赤字箇所が誤りで候補が正解) か confirmed_correct(赤字箇所が正しく候補は別団体)",'
            '"selected_candidate":"選択した候補団体名(該当なしなら空)",'
            '"evidence_urls":["根拠URL(公式優先)"],'
            '"note":"判定理由を1文で"}\n'
            "★候補の中に正解がない場合は selected_candidate を空にする(推測で新しい団体名を作らない)。\n"
            "★長い思考は不要。JSONを直ちに出力。\n\n"
            f"【対象】{pref}の「{label}」/ 検出器: {det}\n【赤字の箇所】\n{exc}\n\n【候補団体名】\n{cand_list}"
        )
        sp = [f"{label} 主催 公式", f"{label} {pref} 問い合わせ"][:5]
    else:
        prompt = (
            "日本の祭り記事のファクトチェッカーです。検出器が以下の箇所に『出典に不在/定型流し込みの疑い』の赤字を出しました。"
            "Web検索で公式情報(自治体/主催団体/文化庁DB等の一次ソース優先)を確認し、この箇所が正しいか誤りかを判定してください。\n"
            "★出力は必ず次のJSONのみ(前置き・説明・コードフェンス禁止):\n"
            '{"verdict":"confirmed_wrong か unverifiable か confirmed_correct",'
            '"evidence_urls":["根拠URL(公式優先)"],'
            '"confidence":"high か medium か low",'
            '"note":"判定理由を1文で"}\n'
            "★その年限定の情報(単年企画/出演者/特定年日程)は対象外。恒常的事実のみ。\n"
            "★確認できなければ verdict=unverifiable とする(推測でnewを埋めない)。\n"
            "★長い思考は不要。JSONを直ちに出力。\n\n"
            f"【対象】{pref}の「{label}」/ 検出器: {det}\n【赤字の箇所】\n{exc}"
        )
        sp = [f"{label} {exc[:20]} 公式", f"{label} {pref} 主催 問い合わせ"][:5]
    data = call_fn(prompt, key, model=model_pro, search_prompts=sp, max_tokens=4000)
    msg = data["choices"][0]["message"]
    txt = (msg.get("content") or "").strip()
    urls = [x.get("url_citation", {}).get("url") for x in (msg.get("annotations") or [])
            if x.get("url_citation", {}).get("url")]
    m = re.search(r"\{.*\}", txt, re.S)
    try:
        obj = json.loads(m.group(0)) if m else {}
    except Exception:
        obj = {}
    for k in ("verdict", "confidence", "note", "selected_candidate"):
        obj.setdefault(k, "")
    obj.setdefault("evidence_urls", [])
    if not obj["evidence_urls"]:
        obj["evidence_urls"] = urls[:3]
    obj["detector"] = det
    obj["target_excerpt"] = exc
    obj["candidates"] = [name for name, _ in (candidates or [])]
    return obj, txt

def evidence_gate(fixes, fetch=True):
    """決定論ゲート: verdict=confirmed_wrong かつ selected_candidate非空の修正案について、
       evidence_urlsの本文にselected_candidateが実在するかを共起照合する。
       実在すれば evidence_verified=True、しなければ False で unresolved へ降格。
       還元T(2026-07-29): newの生成でなく候補選択の検証に変更(Proの正解値生成は
       120で実証したとおり不可能のため、出典由来の候補選択のみを検証)。"""
    out = []
    for f in fixes:
        f2 = dict(f)
        core = f2.get("selected_candidate", "").strip()
        if f2.get("verdict") != "confirmed_wrong" or not core:
            f2["evidence_verified"] = False
            out.append(f2); continue
        verified = False
        if fetch:
            for u in (f2.get("evidence_urls") or [])[:2]:
                t = _fetch(u)
                if t and core in t:
                    verified = True; break
        f2["evidence_verified"] = verified
        out.append(f2)
    return out

def build_report(qid, label, defects, fixes, sources_text=""):
    verified = [f for f in fixes if f.get("evidence_verified")]
    unresolved = [f for f in fixes if not f.get("evidence_verified")]
    payload = {"qid": qid, "label": label, "defect_count": len(defects),
               "verified_fixes": verified, "unresolved": unresolved}
    lines = [f"# Pro照合ループ結果 {qid} {label}",
             f"赤字 {len(defects)}件 / 修正案 {len(fixes)}件 / evidence検証通過 {len(verified)}件"]
    for i, f in enumerate(verified, 1):
        lines.append(f"\n[検証通過 {i}] {f.get('detector')}")
        lines.append(f"  target: {f.get('target_excerpt','')[:80]}")
        lines.append(f"  selected: {f.get('selected_candidate','')[:80]}")
        lines.append(f"  根拠: {', '.join((f.get('evidence_urls') or [])[:2])}")
        lines.append(f"  理由: {f.get('note','')[:100]}")
    for i, f in enumerate(unresolved, 1):
        lines.append(f"\n[未解決 {i}] {f.get('detector')} : {f.get('note','')[:80]} (evidence照合未通過)")
    return payload, "\n".join(lines)

def run(qid, label, pref, ja, en, cites, run_all_lines, key, call_fn, model_pro, fetch_sources=True):
    """単一入口。赤字収集→候補抽出→Pro選択→決定論ゲート→JSON。Claudeは結果の監査のみ。
       還元T(2026-07-29): Proは正解を生成せず候補から選択するのみ。"""
    defects, sources_text = collect_defects(qid, ja, en, cites, run_all_lines,
                                          fetch_sources=fetch_sources)
    docs = {}
    if fetch_sources:
        for u in cites or []:
            t = _fetch(u)
            if t: docs[u] = t
    candidates = extract_source_candidates(docs) if docs else []
    fixes = []
    for i, d in enumerate(defects, 1):
        print(f"  Pro照合[{i}/{len(defects)}] {d['detector']}: {d['excerpt'][:40]}")
        try:
            obj, raw = pro_verify(qid, label, pref, d, key, call_fn, model_pro,
                                  candidates=candidates if candidates else None)
            fixes.append(obj)
        except Exception as e:
            fixes.append({"detector": d["detector"], "target_excerpt": d["excerpt"][:80],
                          "verdict": "unverifiable", "selected_candidate": "",
                          "evidence_urls": [], "confidence": "low",
                          "note": f"Pro照合失敗({type(e).__name__})", "evidence_verified": False})
    fixes = evidence_gate(fixes, fetch=fetch_sources)
    return build_report(qid, label, defects, fixes, sources_text)

_SRC_MARKERS = ("主催", "共催", "後援", "主管", "お問い合わせ", "問い合わせ",
                "運営", "事務局", "Copyright", "copyright", "©", "ⓒ")

def extract_source_candidates(docs, min_len=4):
    """還元T(2026-07-29・120神戸): 正解をProに生成させるのでなく出典本文から
       決定論で抽出する。docs={url: 本文}。主催/問い合わせ/copyright等の
       マーカー近傍(+140字)に出る団体名を候補として集計。
       出典に実在する名前しか候補にならない=幻覚の余地がゼロ。
       Proの生成タスク(正解値を書く=外しうる)を選択タスク(候補から選ぶ)に変える。"""
    import authority_check as ac
    cands = {}
    for u, t in (docs or {}).items():
        if not t:
            continue
        for mk in _SRC_MARKERS:
            for m in re.finditer(re.escape(mk), t):
                w = t[m.start():m.start()+140]
                for om in ac._ORG.finditer(w):
                    name = om.group(0).strip("・-* 　:：")
                    # ノイズ除去: 『市』で終わる短い誤切り(例『神戸市市』)を除外
                    if name.endswith("市") and len(name) <= 3:
                        continue
                    # 『神戸市市』のような重複市名を除外
                    if re.search(r"(市|町|村)\1", name):
                        continue
                    if len(name) >= min_len:
                        c = cands.setdefault(name, {"count": 0, "urls": set()})
                        c["count"] += 1
                        c["urls"].add(u)
    return sorted(cands.items(), key=lambda x: -x[1]["count"])
