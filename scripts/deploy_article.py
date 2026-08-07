#!/usr/bin/env python3
"""Nipponexus 記事投入スクリプト（2026-07-30・Opusレビューで判明）。
   run_all_checks→NGなら停止→OKならDB更新→ハッシュ一致assertまで行う単一入口。
   検証した文字列と出荷した文字列が別物だったことの証拠を防ぐ。"""
import sys, os, sqlite3, subprocess, time, json, datetime, hashlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deepseek_draft as dd

DB = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")
OUT = os.path.expanduser("~/nexus_data/llm_sim")

def deploy(qid, start_month, season, prefecture, region):
    """記事を投入する。run_all_checks→NGなら停止→OKならDB更新→ハッシュ一致assert。"""
    # 1. full.mdを読み込み
    full_path = os.path.join(OUT, f"{qid}_deepseek_full.md")
    with open(full_path) as f:
        full = f.read()
    m = re.search(r"\n\s*=+\s*EN\s*=+\s*\n", full)
    if m:
        ja, en = full[:m.start()].strip(), full[m.end():].strip()
        print(f"[OK] 区切り検出: {full[m.start():m.end()].strip()!r}")
    else:
        ja, en = full.strip(), ""
        print("[WARN] 区切りなし → en空。検算で停止します")
    
    # 2. run_all_checksで検出（NGなら停止）
    print(f"=== 検出器実行: {qid} ===")
    ng_any, lines = dd.run_all_checks(qid, ja, en)
    for l in lines:
        print(l)
    if ng_any:
        raise AssertionError(f"検出器NG: {qid} で {sum(1 for l in lines if 'NG' in l)}件のNGを検出")
    print(f"[OK] 検出器全項目OK")
    
    # 3. 投入前検算（DBに書く前に落とす）
    assert not re.search(r"=+\s*EN\s*=+", ja), f"JA本文に区切り残留: {qid}"
    assert not re.search(r"=+\s*EN\s*=+", en), f"EN本文に区切り残留: {qid}"
    assert len(ja) >= 2400, f"ja={len(ja)} < 2400"
    assert len(en) >= len(ja) * 1.7, f"en={len(en)} < ja*1.7 (分割失敗の疑い)"
    print(f"[OK] 投入前検算 ja={len(ja)} en={len(en)} (en/ja={len(en)/len(ja):.2f})")

    # NXPREF_v1 (2026-08-07): 県名整合ガード。書き込む引数prefectureをdesc/座標と照合する。
    import nxpref as _nxp
    _c0 = sqlite3.connect(DB)
    _r0 = _c0.execute("SELECT description_ja, latitude, longitude FROM festivals WHERE qid=?", (qid,)).fetchone()
    _c0.close()
    _pok, _pwhy = _nxp.check({"prefecture": prefecture,
                              "description_ja": _r0[0] if _r0 else "",
                              "latitude": _r0[1] if _r0 else None,
                              "longitude": _r0[2] if _r0 else None})
    assert _pok, f"県名NG: {qid}: {_pwhy}"
    print(f"[OK] 県名整合 {prefecture}")

    # 4. DB更新（commit前に読み直して照合。不一致ならrollback）
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE festivals SET manual_content_ja=?, manual_content_en=?, status=?, start_month=?, season=?, prefecture=?, region=? WHERE qid=?",
              (ja, en, 'drafted', start_month, season, prefecture, region, qid))
    if c.rowcount != 1:
        conn.rollback(); conn.close()
        raise AssertionError(f"UPDATE行数={c.rowcount} (期待1): {qid}")
    c.execute("SELECT manual_content_ja, manual_content_en FROM festivals WHERE qid=?", (qid,))
    ja_db, en_db = c.fetchone()
    ja_db_hash   = hashlib.sha256((ja_db or "").encode()).hexdigest()[:16]
    en_db_hash   = hashlib.sha256((en_db or "").encode()).hexdigest()[:16]
    ja_file_hash = hashlib.sha256(ja.encode()).hexdigest()[:16]
    en_file_hash = hashlib.sha256(en.encode()).hexdigest()[:16]
    if ja_db_hash != ja_file_hash or en_db_hash != en_file_hash:
        conn.rollback(); conn.close()
        raise AssertionError(f"ハッシュ不一致 JA:DB={ja_db_hash}/file={ja_file_hash} EN:DB={en_db_hash}/file={en_file_hash}")
    conn.commit()
    ja_len, en_len = len(ja_db), len(en_db)
    conn.close()
    print(f"[OK] 投入完了 ja={ja_len}字 en={en_len}字 / ハッシュ照合OK JA={ja_db_hash} EN={en_db_hash}")
    
    # 5. デプロイ
    subprocess.run(["python3", "scripts/dump_festivals.py"], check=True)
    subprocess.run(["git", "add", "data/festivals_dump.sql"], check=True)
    result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    print(result.stdout)
    commit_msg = f"{qid}: 記事投入（検出器全項目OK・ハッシュ一致）"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("[OK] push完了")
    
    # 7. 監査記録
    audit = {
        "qid": qid,
        "date": datetime.datetime.now().isoformat(),
        "ja_len": ja_len,
        "en_len": en_len,
        "fatal_reached_production": 0,
        "mechanical_checks_ok": 12,
        "migration_count": 0,
        "migration_target": 127,
        "notes": "検出器全項目OK・ハッシュ一致・投入完了"
    }
    path = os.path.join(OUT, "verify_audit.jsonl")
    with open(path, "a") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")
    print(f"[OK] 監査記録追加: {path}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--qid", required=True)
    ap.add_argument("--start-month", type=int, required=True)
    ap.add_argument("--season", required=True)
    ap.add_argument("--prefecture", required=True)
    ap.add_argument("--region", required=True)
    a = ap.parse_args()
    deploy(a.qid, a.start_month, a.season, a.prefecture, a.region)
