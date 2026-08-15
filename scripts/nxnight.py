#!/usr/bin/env python3
# NXNIGHT_v1 (2026-08-15) pending から N 件を自動投入する夜間入口。
# 流れ: 選題 -> run_one(生成/検査/Pro照合) -> ensure_slug -> 月確定(nxmonth) -> finalize(drafted)
# 失敗は hold_queue に落として次へ進む。既存モジュールは import のみで改変しない。
import os, re, sys, json, time, sqlite3, argparse, datetime, subprocess, traceback

NP  = os.path.expanduser('~/nipponexus')
DB  = os.path.join(NP, 'data', 'sqlite', 'nipponexus.db')
sys.path.insert(0, os.path.join(NP, 'scripts'))
import nxauto, nxmonth

# 概念・まとめ・オフトピック(映画祭/芸術祭等)は対象外(00ルール18 / 02 C-1)
SKIP_LABEL = re.compile(r'三大|一覧|とは|の日|IDOL|COUNTDOWN|ROCK|FES|フェス|映画祭|芸術祭|博覧会|見本市|音楽祭|アニメ|コミック')
NEG_CTX    = re.compile(r'(旧暦|指定|制定|創建|創設|記念|登録|認定|\d{2,4}年|元年|世紀)')
# 23:00 の nightly_rebuild と競合させない(02 C-3 / 00ルール7)
CUTOFF_HHMM = (22, 30)

def _cx():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; return c

def log(msg):
    line = '%s %s' % (datetime.datetime.now().strftime('%H:%M:%S'), msg)
    print(line, flush=True)

def body_cands(text, season):
    """nxauto.set_month と同一の本文推定。DBは触らない。"""
    res = set()
    for p in list(nxauto._PAT) + list(nxauto._KP):
        for m in re.finditer(p, text or ''):
            if NEG_CTX.search((text or '')[max(0, m.start()-14):m.start()]): continue
            g = m.group(1)
            v = nxauto._KAN.get(g) if g in nxauto._KAN else (int(g) if g.isdigit() else None)
            if v and 1 <= v <= 12: res.add(v)
    allow = nxauto._S2M.get((season or '').strip().lower())
    return (res & allow) if allow else res

def candidates(n):
    c = _cx()
    open_q = {r['qid'] for r in c.execute("SELECT DISTINCT qid FROM hold_queue WHERE resolved_at IS NULL")}
    out = []
    q = ("SELECT qid,label_ja,label_en,prefecture,date_rule,date_rule_json,"
         "COALESCE(priority_score,0) p FROM festivals WHERE status='pending' "
         "AND label_ja IS NOT NULL AND TRIM(label_ja)<>'' "
         "AND prefecture IS NOT NULL AND TRIM(prefecture)<>'' "
         "AND date_rule IS NOT NULL AND TRIM(date_rule)<>'' ORDER BY p DESC")
    for r in c.execute(q):
        if len(out) >= n: break
        if r['qid'] in open_q: continue
        if SKIP_LABEL.search(r['label_ja'] or ''): continue
        mo, why = nxmonth.month_from_rule(r['date_rule'], r['date_rule_json'])
        if not mo: continue
        d = dict(r); d['rule_month'] = mo; out.append(d)
    return out

def past_cutoff():
    now = datetime.datetime.now()
    return (now.hour, now.minute) >= CUTOFF_HHMM

def process(qid, label, apply=True, timeout=900):
    """1件を drafted まで運ぶ。戻り値 (ok, note)。"""
    t0 = time.time()
    logp = os.path.expanduser('~/nexus_data/nxnight.log')
    buf = []
    with open(logp, 'a', encoding='utf-8') as lf:
        lf.write('\n===== %s %s =====\n' % (datetime.datetime.now().isoformat(timespec='seconds'), qid))
        p = subprocess.Popen([sys.executable, os.path.join(NP,'scripts','run_one.py'), '--qid', qid],
                             cwd=NP, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        for line in p.stdout:
            buf.append(line.rstrip()); lf.write(line); lf.flush()
            print('     | ' + line.rstrip()[:150], flush=True)
        p.wait(timeout=timeout)
    out = '\n'.join(buf)
    if p.returncode != 0:
        return False, 'run_one rc=%s | %s' % (p.returncode, ' / '.join(buf[-3:]))
    # run_one は最終行に JSON を吐く。status=stopped は品質ゲートによる正当な停止。
    m = re.search(r'\{[\s\S]*\}\s*$', out)
    if m:
        try:
            res = json.loads(m.group())
            if res.get('status') == 'stopped':
                return False, 'run_one stopped: ' + ' / '.join(res.get('reasons') or [])[:400]
        except Exception:
            pass

    c = _cx()
    row = c.execute("SELECT season,start_month,slug_ja,manual_content_ja FROM festivals WHERE qid=?", (qid,)).fetchone()
    if not row or not (row['manual_content_ja'] or '').strip():
        return False, '本文が生成されていない'

    if apply: nxauto.ensure_slug(qid, apply=True)

    if not row['start_month']:
        rr = c.execute("SELECT date_rule,date_rule_json FROM festivals WHERE qid=?", (qid,)).fetchone()
        rm, _w = nxmonth.month_from_rule(rr['date_rule'], rr['date_rule_json'])
        mo, why = nxmonth.arbitrate(body_cands(row['manual_content_ja'], row['season']), rm)
        if mo is None:
            return False, 'start_month未確定 (%s)' % why
        if apply:
            kv = {'start_month': mo}
            if not row['season'] and nxauto._M2S.get(mo): kv['season'] = nxauto._M2S[mo]
            import nx; nx.setmeta(qid, **kv)
        log('    month=%s (%s)' % (mo, why))

    if apply:
        fin = nxauto.finalize(qid, apply=True)
        st = _cx().execute("SELECT status FROM festivals WHERE qid=?", (qid,)).fetchone()['status']
        if st != 'drafted':
            return False, 'finalize後 status=%s | %s' % (st, str(fin)[:160])
    return True, '%.0f秒' % (time.time() - t0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-n', type=int, default=3, help='投入本数')
    ap.add_argument('--dry', action='store_true', help='選題のみ。API を呼ばない')
    a = ap.parse_args()

    log('=== nxnight start n=%d dry=%s ===' % (a.n, a.dry))
    cands = candidates(a.n)
    log('候補 %d 件' % len(cands))
    for c in cands:
        log('  %s %s (%s) 規則%s月 p=%s' % (c['qid'], c['label_ja'], c['prefecture'], c['rule_month'], c['p']))
    if a.dry:
        log('=== dry-run 終了(DB未変更) ==='); return 0

    ok = ng = 0
    for c in cands:
        if past_cutoff():
            log('!! %02d:%02d を過ぎたため打ち切り(23:00の公開ジョブと競合回避)' % CUTOFF_HHMM); break
        log('-- %s %s 開始' % (c['qid'], c['label_ja']))
        try:
            good, note = process(c['qid'], c['label_ja'])
        except Exception as e:
            good, note = False, '例外 %s: %s' % (type(e).__name__, e)
            traceback.print_exc()
        if good:
            ok += 1; log('   OK drafted (%s)' % note)
        else:
            ng += 1; log('   HOLD %s' % note)
            try: nxauto.hold(c['qid'], 'nxnight失敗', note[:300])
            except Exception as e: log('   hold記録に失敗: %s' % e)
    log('=== 完了 drafted=%d hold=%d ===' % (ok, ng))
    return 0

if __name__ == '__main__':
    sys.exit(main())
