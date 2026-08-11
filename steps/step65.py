# -*- coding: utf-8 -*-
# step65 : (1) 監査バグ修正=必須列チェック (2) tkey からの証拠展開 (3) 空欄962件の実態把握
import os, sys, re, json, sqlite3, collections, datetime, subprocess
HOME = os.path.expanduser("~"); ROOT = os.path.join(HOME, "nipponexus")
SCR = os.path.join(ROOT, "scripts"); SNAP = os.path.join(ROOT, "snapshots")
DB = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
DOC = os.path.join(HOME, "nexus_data", "04_addenda.md")
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
APPLY = os.environ.get("NX_APPLY") == "1"
sys.path.insert(0, SCR)
R = {}
def sec(n, f):
    try: R[n] = f(); print("[OK] " + n)
    except Exception as e: R[n] = "ERR: %r" % (e,); print("[NG] %s : %r" % (n, e))

def need(con, tbl, names):
    """列名を推定する箇所は必ずこれを通す。1つも当たらなければ即例外(黙って素通りさせない)。"""
    have = [r[1] for r in con.execute("pragma table_info('%s')" % tbl)]
    got = [c for c in names if c in have]
    if not got:
        raise KeyError("%s に候補列なし: 候補=%s 実在=%s" % (tbl, names, have))
    return got

def s0():
    b = os.path.join(SNAP, "db_" + TS + ".db")
    a = sqlite3.connect(DB); c = sqlite3.connect(b); a.backup(c); c.close(); a.close()
    print("  " + b); return {"db_snapshot": b}

def parse_tkey(tkey):
    ja = en = None
    for m in re.finditer(r"JA\[([^\]]*)\]|EN\[([^\]]*)\]", tkey):
        if m.group(1) is not None: ja = m.group(1)
        if m.group(2) is not None: en = m.group(2)
    parts = tkey.split("|")
    qid = parts[0] if parts and re.match(r"^Q", parts[0]) else None
    return qid, ja, en

# ---------- §1 名称突合(今度は実列で) ----------
def s1():
    con = sqlite3.connect(DB)
    nc = need(con, "festivals", ["label_ja", "label_en"])
    print("  使用列 = %s" % nc)
    out = []
    for (tkey, qid_c) in con.execute("select tkey,qid from verdict_ledger"):
        qid, ja, en = parse_tkey(tkey)
        qid = qid_c or qid
        if not qid or not re.match(r"^Q[0-9]+$", qid) or not ja:
            continue
        row = con.execute("select label_ja,label_en,manual_content_ja from festivals where qid=?", (qid,)).fetchone()
        if not row:
            out.append((qid, ja, "festivals に不在", "")); continue
        lj, le, body = row[0] or "", row[1] or "", row[2] or ""
        if ja in lj:
            continue
        out.append((qid, ja, "台帳JAが label_ja と不一致" + ("(本文にはあり)" if ja in body else "(本文にも無し)"),
                    "label_ja=%s / label_en=%s" % (lj[:24], le[:30])))
    for o in out:
        print("  [!] %-11s JA=%-8s %-34s %s" % o)
    print("  名称不整合 = %d 件" % len(out))
    con.close(); return out

# ---------- §2 証拠展開 ----------
def s2():
    con = sqlite3.connect(DB)
    plan = []
    for (tkey, ja, en, note, src, old, new, verdict) in con.execute(
            "select tkey,ja,en,note,src,old,new,verdict from verdict_ledger"):
        if (note or "").strip():
            continue
        _, tja, ten = parse_tkey(tkey)
        kv = {}
        if tja and not (ja or "").strip(): kv["ja"] = tja
        if ten and not (en or "").strip(): kv["en"] = ten
        ev = "根拠は tkey に埋め込まれていた形式を展開: " + tkey
        if not tja and not ten:
            ev = "判定 %s / 出典 %s。対象は概念記事のため実体紐付けなし。" % (verdict, src)
        kv["note"] = ("%s || %s -> %s (%s)" % (ev, old, new, src))[:600]
        plan.append((tkey, kv))
    for t, kv in plan[:20]:
        print("  %-52s <- %s" % (t[:52], {k: (v[:40] if isinstance(v, str) else v) for k, v in kv.items()}))
    if APPLY:
        for t, kv in plan:
            sets = ",".join("%s=?" % k for k in kv)
            con.execute("update verdict_ledger set %s where tkey=?" % sets, list(kv.values()) + [t])
        con.commit()
    n = con.execute("select count(*) from verdict_ledger where note is null or note=''").fetchone()[0]
    print("  展開 %d 行 / 適用後の note 空 = %d (APPLY=%s)" % (len(plan), n, APPLY))
    con.close(); return {"planned": len(plan), "empty_after": n}

# ---------- §3 プレースホルダ QID の実体探索 ----------
def s3():
    con = sqlite3.connect(DB)
    res = []
    for tkey, in con.execute("select tkey from verdict_ledger where tkey like 'Q\\_%' escape '\\'"):
        _, ja, en = parse_tkey(tkey)
        cand = con.execute("select qid,label_ja,label_en from festivals where label_ja like ? or "
                           "manual_content_ja like ? limit 5", ("%" + (ja or "@@") + "%", "%" + (ja or "@@") + "%")).fetchall()
        print("  %-46s JA=%s -> 候補 %s" % (tkey[:46], ja, cand or "なし"))
        res.append({"tkey": tkey, "ja": ja, "cand": cand})
    con.close(); return res

# ---------- §4 空欄962件の実態 ----------
def s4():
    con = sqlite3.connect(DB)
    q = lambda s: con.execute(s).fetchone()[0]
    tot = q("select count(*) from festivals")
    en_ok = q("select count(*) from festivals where manual_content_en is not null and manual_content_en<>''")
    ja_ok = q("select count(*) from festivals where manual_content_ja is not null and manual_content_ja<>''")
    both = q("select count(*) from festivals where manual_content_ja<>'' and manual_content_en<>''")
    ja_only = q("select count(*) from festivals where manual_content_ja is not null and manual_content_ja<>'' "
                "and (manual_content_en is null or manual_content_en='')")
    none = q("select count(*) from festivals where (manual_content_ja is null or manual_content_ja='') "
             "and (manual_content_en is null or manual_content_en='')")
    print("  総数 %d / JA本文 %d / EN本文 %d / 両方 %d" % (tot, ja_ok, en_ok, both))
    print("  JAのみ(=EN生成の候補) %d / どちらも空(=一次情報から要収集) %d" % (ja_only, none))
    print("  status 内訳 = %s" % con.execute("select status,count(*) from festivals group by 1 order by 2 desc").fetchall())
    print("  published_at あり = %d" % q("select count(*) from festivals where published_at is not null and published_at<>''"))
    print("  素材の充足(どちらも空 %d 件のうち):" % none)
    for c in ("wikipedia_ja", "wikipedia_en", "image_url", "image_license", "latitude", "description_ja"):
        n = q("select count(*) from festivals where (manual_content_ja is null or manual_content_ja='') "
              "and (manual_content_en is null or manual_content_en='') and %s is not null and %s<>''" % (c, c))
        print("    %-16s %d" % (c, n))
    print("  priority_score 上位で未着手のもの:")
    for r in con.execute("select qid,label_ja,prefecture,priority_score from festivals "
                         "where (manual_content_ja is null or manual_content_ja='') "
                         "order by priority_score desc limit 8"):
        print("    %-11s %-22s %-6s %s" % r)
    con.close()
    return {"total": tot, "en": en_ok, "ja": ja_ok, "ja_only": ja_only, "none": none}

KEY = "## [AUDIT_COLGUARD_GAP_20260810]"
BLOCK = KEY + """
step64 の監査は列名候補を name_ja/title_ja で探し、実列 label_ja に当たらず候補0のまま
名称突合を素通りした。put() の未知キー黙殺と同型の「静かに何もしない」失敗。
対策 need(con,tbl,names): 候補が1つも実在しなければ KeyError。列名推定は必ずこれを通す。
verdict_ledger の note 空15行は根拠喪失ではなく、tkey に JA[..]/EN[..] 形式で埋め込まれていた。
LEGACY と塗り潰す案は誤り。tkey を解析して ja/en/note へ展開する(step65 §2)。
現況の要点: CANON 語の是正対象は残存2件(いずれも reject 済 Yamadera)で実質完了。
festivals 1256 件中 EN 本文は 294 件のみ。日次に流すべき玉は綴り是正ではなく本文の空欄。
綴り是正を前提にした日次設計は、玉が尽きた時点で空回りする。供給源の設計が次の課題。
"""
def s5():
    import nxdoc
    try: nxdoc.insert_once(DOC, KEY, BLOCK)
    except TypeError: nxdoc.insert_once(path=DOC, key=KEY, block=BLOCK)
    print("  key count = %d" % open(DOC, encoding="utf-8").read().count(KEY))
    return {"ok": True}

sec("backup", s0); sec("names", s1); sec("evidence", s2)
sec("placeholder", s3); sec("gap", s4); sec("doc", s5)
j = os.path.join(SNAP, "step65_" + TS + ".json")
open(j, "w", encoding="utf-8").write(json.dumps(R, ensure_ascii=False, indent=1, default=str))
print("=" * 60); print("APPLY=%s snapshot=%s" % (APPLY, j))
