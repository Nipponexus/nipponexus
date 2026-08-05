# -*- coding: utf-8 -*-
"""pro_verify_loop: 機械検出の赤字を入力にProが一次照合を複数回まわし
修正案(old/new+根拠URL)を構造化JSONで出力する(2026-07-29・分担逸脱の是正)。
★C-3b堅持: Proの修正案も正解データとして採用しない。決定論ゲート(evidence照合)で
   newの核心固有名が出典本文に実在するかを検証し、実在しなければunresolvedへ降格。"""
import re, json
import authority_check as ac
import ephemeral_src as es

def _fetch(url, timeout=12):
    """2026-08-02・133諏訪湖: 生HTMLを返していたためマークアップ上の近接で誤判定していた。
       『諏訪市観光協会』と『協力』がナビ/フッタのタグ内で±80字に同居し役割共起が○になり、
       ac.checkも script や メニュー内の文字列を『出典に出現』と数えうる(生HTML473,925字 vs
       本文20,040字)。段階③の年号照合で実績のある deepseek_draft._fetch_text と同方式に揃える。"""
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read(600000)
            enc = r.headers.get_content_charset() or "utf-8"
            html = raw.decode(enc, errors="replace")
    except Exception:
        return ""
    html = re.sub(r"(?is)<(script|style).*?</\1>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html)

# --- 還元(2026-08-01・131PMF): Pro照合ループの型崩壊対策 ---
# 候補集合が1つしかなく検出器の種別を問わず全defectへ渡っていたため、年号targetに
# 団体名の候補が渡り、Proが4/4で『1940年→組織委員会』という修正案を返した。
# evidence_gateが型を見ないため団体名は出典に実在し全件『検証通過』になった(130霧島と同型)。
_YEAR_DETECTORS = ('audit_years_against_citations', 'audit_dates_against_citations')
_ORG_DETECTORS = ('authority_check',)
# 2026-08-03・140おぢや: 単年系の赤字を渡しながらプロンプトに『その年限定の情報は対象外』と
# 書いていたため、Proは『公式に第50回が明記されている』と実在確認で答え論点がずれた。
# 単年系は事実性でなくC-1の陳腐化回避ルール違反を問う=実在しても削除/相対化が正解。
_EPHEMERAL_DETECTORS = ('detect_future_ephemeral', 'ephemeral_src')
_EPH_RULE = ("★これは『特定年限定の情報を書いていないか』を見る検出器の赤字です。事実として実在するかは問いません。"
             "特定年の回数(第N回)・日程・来場者数・出演者・単年企画・N年ぶり等が書かれていれば、公式に実在しても"
             "陳腐化回避のため削除または相対表現化が正解=verdict=confirmed_wrong とし、noteに『削除』か『相対表現化』の"
             "どちらが適切かを書いてください。恒常的事実(初回開催年・毎年の会期の目安等)なら detector_false_positive とします。\n")
# 2026-08-04: JA漢字固有名とENローマ字表記の対応確認。★判定済みの赤字ではなく『確認依頼』。
# 音写の正誤は音写距離/DF/読み/提示型の4方式すべてで機械判定が不成立(02)。対応の列挙のみ
# 決定論で行い、正誤の確定はProの検索接地に委ねる=142三国花火でClaudeが手でやった工程の移管。
_TRANSLIT_DETECTORS = ('translit_check',)
_TRL_RULE = ("★これは判定済みの誤りではなく『確認依頼』です。JA本文の固有名とEN本文のローマ字表記が同一の対象を指し、"
             "かつENの表記が公式表記(鉄道事業者/自治体/施設の公式サイトの英字表記)と一致しているかを検索で確認してください。\n"
             "★一致していれば verdict=detector_false_positive (確認の結果、問題なし)とします。\n"
             "★食い違っていれば verdict=confirmed_wrong とし、note に『記事の誤表記→公式の正表記』を明記してください"
             "(候補リストは無いので公式表記を自分で書く)。\n"
             "★さらに JSON へ \"new\":\"公式の正表記(EN)\" を必ず含めてください。"
             "この new は出典本文に literal で存在するかを機械検証し、不在なら不採用にします"
             "(2026-08-05: 従来は正表記を note にだけ書かせていたため new検証を必ず落ちていた)。\n"
             "★神社→Shrine・寺→Temple・公園→Park のような意味翻訳は一致とみなします(誤りではありません)。\n"
             "★JA側とEN側で件数が違っても、それ自体は誤りではありません(片方だけ言及される場合があります)。\n"
             "★英語検索は表記の確認にのみ用い、記事内容の補充には使わないでください"
             "(情報の薄い対象では別の祭りを拾い接ぎ木の元になるため)。\n")
_STD_RULE = "★その年限定の情報(単年企画/出演者/特定年日程)は対象外。恒常的事実のみ。\n"
_YEAR_FORM = re.compile(r'^(1[5-9]\d{2}|20[0-4]\d)年?(\d{1,2}月(\d{1,2}日)?)?$')
_FIRST_CTX = re.compile(r'第1回|第一回|初開催|初めて開催')
_FOUND_CTX = re.compile(r'創設|創始|創立|始まった|スタートした|発足')
_OTHER_ENT = re.compile(r'[^\s、。]{2,}?(音楽祭|オーケストラ|交響楽団|ホール|美術館|博物館|大学|協会|財団|神社|寺)')

def _is_subject_year(ja, y, label=''):
    """その西暦が本祭自身の初回・創設を述べているか。他団体の創立年やホール開館年などの
       背景年をProループへ渡さないための絞り込み(review.mdには従来どおり×人的確認で残る)。
       節の単位は129で確立した読点・句点区切り(距離では分離できないため)。
       第1回・初開催は主語が本祭で確定するため無条件に対象、創設語は同じ節に別主体
       (◯◯音楽祭/◯◯交響楽団/◯◯ホール等)があれば背景年とみなして除外する。"""
    for seg in re.split(r'[。、\n]', ja or ''):
        if y not in seg:
            continue
        if _FIRST_CTX.search(seg):
            return True
        if _FOUND_CTX.search(seg):
            ent = _OTHER_ENT.search(seg)
            if not ent or ent.group(0) in (label or ''):
                return True
    return False

def extract_year_candidates(docs, limit=12):
    """年号defect用の型一致した候補集合=出典本文に実在する西暦のみを候補にする。"""
    cnt = {}
    for u, t in (docs or {}).items():
        for y in set(re.findall(r'(?<!\d)(1[5-9]\d{2}|20[0-4]\d)(?!\d)', t or '')):
            cnt[y] = cnt.get(y, 0) + 1
    top = sorted(cnt.items(), key=lambda kv: -kv[1])[:limit]
    return [(y + '年', n) for y, n in top]

def _pick_candidates(detector, org_cands, year_cands):
    if detector in _YEAR_DETECTORS:
        return year_cands or None
    if detector in _ORG_DETECTORS:
        return org_cands or None
    return None

def collect_defects(qid, ja, en, cites, run_all_lines, fetch_sources=False):
    defects = []
    cur = ""
    # 還元(2026-08-01・129フジロック): 旧実装は(a)NG見出しの後にcurをリセットせず
    # 後続のOK節の詳細行まで巻き込み、(b)詳細行を「L」始まりに限定していたため
    # 訳語照合のdict形式の赤字を取りこぼしていた。見出し行(先頭が数字+空白)で
    # 状態を切り替え、NG節の配下にある詳細行だけを拾う方式へ変更する。
    for ln in (run_all_lines or []):
        s = ln.strip()
        if not s:
            continue
        if re.match(r"^\d+\s", s) or s.startswith("=="):
            cur = s if ": NG" in s else ""
            continue
        if cur:
            defects.append({"detector": "run_all_checks", "field": cur,
                            "excerpt": s, "detail": cur + " / " + s})
    # 還元(2026-07-30・127本目しばれフェス): audit_years_against_citations/
    # detect_future_ephemeralはreview.md出力のみでcollect_defectsに未接続だった。
    # Pro照合ループの監査対象は run_all_checks5項目+authority_check+ephemeral_srcの
    # 7項目に限定され、年号照合と将来陳腐化はClaude一次照合に依存していた
    # (Proループがdefect_count:0を返したのは正しい判定だが、対象範囲が狭すぎた)。
    try:
        from deepseek_draft import audit_years_against_citations, detect_future_ephemeral
        for y, verdict, doms in audit_years_against_citations(ja, cites or []):
            if "×人的確認" in verdict and _is_subject_year(ja, y):
                defects.append({"detector": "audit_years_against_citations",
                                "field": "年号(要人的確認)",
                                "excerpt": f"{y}年", "detail": f"{y}: {verdict}"})
        fe, fe_hits = detect_future_ephemeral(ja, en)
        if fe:
            for h in fe_hits:
                defects.append({"detector": "detect_future_ephemeral",
                                "field": "将来陳腐化候補",
                                "excerpt": h[:120], "detail": h})
    except Exception as e:
        defects.append({"detector": "collect_defects_ext", "field": "接続エラー",
                        "excerpt": f"{type(e).__name__}: {e}",
                        "detail": "audit_years_against_citations/detect_future_ephemeral接続失敗"})
    # 2026-08-04: translit_check(JA固有名とEN音写の対応確認)を接続。出典本文に依存しないため
    # fetch_sourcesの外に置く(139湯涌=出典キャッシュ欠落でSKIPし赤字0件になった事故を踏まえ、
    # 外部依存の少ない位置で必ず走らせる)。
    try:
        import translit_check as _tc
        for d in _tc.as_defects(ja, en):
            defects.append({"detector": "translit_check",
                            "field": "訳語の対応確認(%s)" % d["kind"],
                            "excerpt": d["target"], "detail": d["target"]})
    except Exception as e:
        defects.append({"detector": "collect_defects_ext", "field": "接続エラー",
                        "excerpt": "%s: %s" % (type(e).__name__, e),
                        "detail": "translit_check接続失敗"})
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
        # 2026-08-02・133諏訪湖: 実在する団体への誤った役割の割り当ては
        # ac.check(名称の共起のみ)を素通りする。役割共起はWARN専用で赤字に載せる
        # (条件B回帰6/6・既存23本のWARN率0%を確認してから接続)。
        try:
            import graft_check as _gc
            _lb = _gc.load_meta(qid)[2] or ""
        except Exception:
            _lb = ""
        _rw, _rlines = ac.check_roles(ja, sources_text, label=_lb)
        for ln in _rlines:
            if "▲" in ln:
                defects.append({"detector": "authority_role", "field": "権威属性の役割",
                                "excerpt": ln.strip()[:140], "detail": ln.strip()})
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
            "★検出器は誤検出(偽陽性)を出すことがあります。まず赤字が真の誤りか検出器の偽陽性かを判定し、真の誤りである場合にのみ候補から正しい団体名を選んでください。候補に正解が無い場合も選ばないでください。\n"
            "偽陽性の典型=(1)助詞や動詞を跨いだ抽出断片(例『して市』)(2)出典本文キャッシュに無いだけで公式には実在する表記(3)候補が実在しても記事の役割(主催/共催/後援)とは別の役割の団体である場合。\n"
            "★出力は必ず次のJSONのみ(前置き・説明・コードフェンス禁止):\n"
            '{"verdict":"confirmed_wrong(赤字が誤りで候補が正解) か confirmed_correct(赤字は正しい) か detector_false_positive(赤字自体が検出器の偽陽性)",'
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
            '{"verdict":"confirmed_wrong か unverifiable か confirmed_correct か detector_false_positive",'
            '"evidence_urls":["根拠URL(公式優先)"],'
            '"confidence":"high か medium か low",'
            '"note":"判定理由を1文で"}\n'
            "★その年限定の情報(単年企画/出演者/特定年日程)は対象外。恒常的事実のみ。\n"
            "★確認できなければ verdict=unverifiable とする(推測でnewを埋めない)。\n"
            "★長い思考は不要。JSONを直ちに出力。\n\n"
            f"【対象】{pref}の「{label}」/ 検出器: {det}\n【赤字の箇所】\n{exc}"
        )
        if det in _EPHEMERAL_DETECTORS:
            prompt += _EPH_RULE
        elif det in _TRANSLIT_DETECTORS:
            prompt += _TRL_RULE
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

def _subject_alts(subject):
    """還元(2026-08-02・135): evidence_gateは候補が出典本文に在るかだけを見ており、
       その出典が本題材を扱っているかを見ていなかった。別イベントの公式が出典に混ざると
       候補は当然実在するため接ぎ木の修正案が検証通過する(133の生HTML是正で消えたのは
       タグ内文字列を数える緩さで、『どの出典か』を見ない緩さは残っていた)。"""
    if not subject:
        return []
    s = str(subject).strip()
    alts = {s, s.replace('\u30fb', ''), s.replace(' ', '')}
    for m in re.findall(r'[\u4e00-\u9fff]{2,}', s):
        alts.add(m)
    return [a for a in alts if len(a) >= 2]


def _subject_near(text, core, alts, win=400):
    for m in re.finditer(re.escape(core), text):
        seg = text[max(0, m.start() - win): m.end() + win]
        if any(a in seg for a in alts):
            return True
    return False


_ROLE_NEAR = re.compile(r'主催|共催|主管|後援|運営|事務局|問い合わせ|お問い合わせ')


def _role_near(text, core, win=80):
    """138姫路: 候補が出典本文のどこかに在れば通る緩さを狭める。
       ★限界の明記=本件の『ゆかたまつり奉賛会』は別行事(地域ふれあいステージ)の主催として
       同じ公式頁に主催語つきで実在するため本ゲートでは分離できない。分離の主役は
       Proへ与えた detector_false_positive の分岐であり、本ゲートは役割語と無縁な
       文脈だけに現れる候補を落とす補助である。"""
    for m in re.finditer(re.escape(core), text):
        seg = text[max(0, m.start() - win): m.end() + win]
        if _ROLE_NEAR.search(seg):
            return True
    return False



_WALL = re.compile(r"(?i)(password|\u30d1\u30b9\u30ef\u30fc\u30c9|\u8a8d\u8a3c\u304c\u5fc5\u8981|"
                   r"\u30ed\u30b0\u30a4\u30f3\u3057\u3066|sign in to continue|access denied|"
                   r"\u95b2\u89a7\u3059\u308b\u306b\u306f)")
_NEW_STOP = {"Festival","Japan","Japanese","City","Town","Station","River","Shrine","Temple",
             "Prefecture","Important","Intangible","Cultural","Property","The","This",
             "Port","Bay","Bridge","Park","Beach","Coast","Hall","Museum",
             "Line","Road","Avenue","Street","Mountain","Lake","Valley","Island",
             "Castle","Gate","Hill","Pond","Village","Hot","Spring","Park"}

def _is_walled(t):
    """還元(2026-08-04): パスワード壁/認証要求は200で本文も返るため到達性だけでは弾けない。
       三国でProがこの型のページを根拠に挙げ存在しない表記を作った。"""
    return bool(_WALL.search(t[:4000]))

def _new_tokens(new):
    """newから検証対象のラテン語トークンを取る(音写の是正が主対象)。判定はせず抽出のみ。"""
    toks = [w for w in re.findall(r"\b[A-Z][A-Za-z]{3,}(?:-[A-Za-z]{2,})*\b", new or "")
            if w not in _NEW_STOP]
    return sorted(set(toks))

def _verify_new_literal(f2, fetch=True, docs=None):
    """還元(2026-08-04): evidence_gateは候補選択型しか検証できず、newに文字列を書く型
       (音写の是正等)は構造上いつまでもunresolvedのまま人手に残っていた。
       newの中核トークンが到達可能かつ非パスワード壁の出典にliteralで在るかを見る。"""
    toks = _new_tokens(f2.get("new", ""))
    if not toks:
        f2["evidence_verified"] = False
        f2["note"] = (f2.get("note", "") + " ／[new検証]検証対象トークンなし=要人手").strip()
        return f2
    for u in (f2.get("evidence_urls") or []):
        t = (docs or {}).get(u) or (_fetch(u) if fetch else "")
        if not t:
            f2["note"] = (f2.get("note", "") + " ／[new検証]根拠URLが到達不能").strip()
            continue
        if _is_walled(t):
            f2["note"] = (f2.get("note", "") + " ／[new検証]パスワード壁/認証要求ページは根拠に採らない").strip()
            continue
        tn = re.sub(r"\s+", " ", t)
        if all(re.sub(r"\s+", " ", w) in tn for w in toks):
            f2["evidence_verified"] = True
            return f2
    f2["evidence_verified"] = False
    f2["note"] = (f2.get("note", "") + " ／[new検証]newの中核が出典にliteralで不在=捏造の疑い").strip()
    return f2

def evidence_gate(fixes, fetch=True, subject=None, docs=None):
    """決定論ゲート: verdict=confirmed_wrong かつ selected_candidate非空の修正案について、
       evidence_urlsの本文にselected_candidateが実在するかを共起照合する。
       実在すれば evidence_verified=True、しなければ False で unresolved へ降格。
       還元T(2026-07-29): newの生成でなく候補選択の検証に変更(Proの正解値生成は
       120で実証したとおり不可能のため、出典由来の候補選択のみを検証)。"""
    out = []
    for f in fixes:
        f2 = dict(f)
        core = f2.get("selected_candidate", "").strip()
        det = f2.get('detector', '')
        if det in _YEAR_DETECTORS and core and not _YEAR_FORM.match(core):
            f2['evidence_verified'] = False
            f2['note'] = (f2.get('note', '') + ' ／[型ガード]年号targetに非年号candidate=棄却').strip()
            out.append(f2); continue
        if f2.get("verdict") != "confirmed_wrong":
            f2["evidence_verified"] = False
            out.append(f2); continue
        if not core:
            out.append(_verify_new_literal(f2, fetch=fetch, docs=docs)); continue
        verified = False
        note_extra = ""
        subj_alts = _subject_alts(subject)
        for u in (f2.get("evidence_urls") or []):
            t = (docs or {}).get(u) or (_fetch(u) if fetch else "")
            if not t or core not in t:
                continue
            if subj_alts and not _subject_near(t, core, subj_alts):
                note_extra = " ／[主題束縛]候補は出典に在るが本題材への言及と結び付かない=別主体の出典混入の疑い"
                continue
            if det in _ORG_DETECTORS and not _role_near(t, core):
                note_extra = " ／[役割束縛]候補は出典に在るが役割語と共起しない=別役割団体の疑い(138姫路)"
                continue
            verified = True; break
        if note_extra and not verified:
            f2["note"] = (f2.get("note", "") + note_extra).strip()
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
    org_cands = extract_source_candidates(docs) if docs else []
    year_cands = extract_year_candidates(docs) if docs else []
    fixes = []
    for i, d in enumerate(defects, 1):
        print(f"  Pro照合[{i}/{len(defects)}] {d['detector']}: {d['excerpt'][:40]}")
        try:
            obj, raw = pro_verify(qid, label, pref, d, key, call_fn, model_pro,
                                  candidates=_pick_candidates(d.get('detector', ''), org_cands, year_cands))
            fixes.append(obj)
        except Exception as e:
            fixes.append({"detector": d["detector"], "target_excerpt": d["excerpt"][:80],
                          "verdict": "unverifiable", "selected_candidate": "",
                          "evidence_urls": [], "confidence": "low",
                          "note": f"Pro照合失敗({type(e).__name__})", "evidence_verified": False})
    fixes = evidence_gate(fixes, fetch=fetch_sources, subject=label, docs=docs)
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
