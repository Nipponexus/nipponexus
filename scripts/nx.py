# -*- coding: utf-8 -*-
'''nx = Nipponexus運用の単一ファサード(2026-08-03新設)。
   Blockスクリプトは nx.* だけを呼ぶ。素の関数を直接呼ばない。
   目的は今日3型で再発した事故をコードで不可能にすること。
   (1)署名の推測 -> import時に配下関数の署名を検査し不一致なら即停止(_bind)
   (2)一括編集の副作用 -> invariants()を通らないと write() できない(行数/字下げ/二重空白)
   (3)範囲削除の巻き添え -> patch_file()がトップレベル定義の欠落を検出して拒否'''
import os, re, sys, time, shutil, sqlite3, subprocess, datetime, urllib.request, inspect, py_compile

ROOT = os.path.expanduser('~/nipponexus')
SCRIPTS = os.path.join(ROOT, 'scripts')
DB = os.path.join(ROOT, 'data', 'sqlite', 'nipponexus.db')
BK = os.path.expanduser('~/nexus_data/_backup')
SENT = '\ue000%d\ue000'
sys.path.insert(0, SCRIPTS)
import deepseek_draft as _dd
import bracket_check as _bc


def _bind(fn, *required):
    sig = inspect.signature(fn)
    missing = [p for p in required if p not in sig.parameters]
    if missing:
        raise RuntimeError('署名不一致: %s%s に %s が無い(nxの前提が変わった)' % (fn.__name__, sig, missing))
    return fn


_run_all = _bind(_dd.run_all_checks, 'qid', 'ja', 'en', 'strict')
_verify = _bind(_dd.verify, 'ja', 'en')
_strip_cite = _dd.strip_citations


def help():
    '''使えるものを一覧する。迷ったらまずこれ。'''
    for n, f in sorted(globals().items()):
        if callable(f) and not n.startswith('_') and getattr(f, '__module__', None) == __name__:
            d = (f.__doc__ or '').strip().split('\n')[0]
            print('  nx.%-18s %-42s %s' % (n + str(inspect.signature(f)), '', d))


def ts():
    '''バックアップ用のタイムスタンプ。'''
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')


def row(qid):
    '''festivals の1行を dict で返す。'''
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    r = c.execute('SELECT * FROM festivals WHERE qid=?', (qid,)).fetchone()
    c.close()
    if not r:
        raise KeyError(qid)
    return dict(r)


def clean(text):
    '''出典装飾(リンク/裸ブラケット/括弧付きURL)を除去する。空白と字下げには触れない。'''
    return _bc.strip_citation_urls(_strip_cite(text or ''))


def checks(qid, ja, en):
    '''検出器の単一入口。(ng, lines)を返す。'''
    return _run_all(qid=qid, ja=ja, en=en, strict=False)


def audit(ja, en):
    '''字数検算+出典残骸+URL残骸をまとめて見る。'''
    ng_b, hb = _bc.check(ja, en)
    urls = _bc.residual_urls(ja, en)
    return {'verify': _verify(ja, en), 'bracket': (ng_b, hb[:3]),
            'url_labeled': sum(1 for u in urls if u[2]), 'url_unlabeled': [u for u in urls if not u[2]][:3],
            'ja': len(ja), 'en': len(en), 'ratio': round(len(en) / max(1, len(ja)), 2)}


def invariants(old, new, allow_line_delta=0, allow_deleted=None):
    '''編集の副作用を禁じる不変条件。違反の一覧を返す(空なら健全)。'''
    v = []
    ol, nl = old.split('\n'), new.split('\n')
    d = len(ol) - len(nl)
    if allow_deleted is None and abs(d) > allow_line_delta:
        v.append('行数 %d -> %d (許容差%d)' % (len(ol), len(nl), allow_line_delta))
        return v
    import difflib
    ok = tuple(allow_deleted or ())
    okline = lambda s: (not s.strip()) or any(w in s for w in ok)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ol, nl).get_opcodes():
        if op == 'delete':
            for s in ol[i1:i2]:
                if not okline(s):
                    v.append('意図しない行削除 %r' % s[:60])
        elif op == 'insert':
            for s in nl[j1:j2]:
                if not okline(s):
                    v.append('意図しない行挿入 %r' % s[:60])
        elif op == 'replace':
            if (i2 - i1) != (j2 - j1):
                v.append('置換で行数変化 %d -> %d' % (i2 - i1, j2 - j1))
            for a, b in zip(ol[i1:i2], nl[j1:j2]):
                ia = a[:len(a) - len(a.lstrip())]
                ib = b[:len(b) - len(b.lstrip())]
                if ia != ib:
                    v.append('字下げ変化 %r -> %r' % (ia, ib)); break
    if re.search(r'\S  +\S', new) and not re.search(r'\S  +\S', old):
        v.append('二重空白が新規発生')
    return v


def fix(text, pairs, min_hits=1):
    '''置換。期待件数は書かない(実測して全件置換し残存0を保証)。newがoldを含む追記型も安全。'''
    out = text
    log = []
    for i, (old, new) in enumerate(pairs):
        n = out.count(old)
        if n < min_hits:
            raise AssertionError('未マッチ old=%r 実測%d件 (近傍=%r)' % (old[:40], n, _near(out, old)))
        s = SENT % i
        out = out.replace(old, s)
        assert old not in out or old in new, '残存 old=%r' % old[:40]
        out = out.replace(s, new)
        log.append((old[:24], n))
    # 2026-08-03・140おぢや: Global Balloon Festivalを4件置換したのに、指定しなかった
    # 同族表記(Hirasa Venue/Hirasa Shinden)が残った。nx.fixは渡された文字列しか置換しない
    # ため『全カウントを人が思いつく』穴が残る(114一宮の再演)。置換したoldの先頭語が
    # 別の形で本文に残っていれば警告する(判定はせず提示のみ)。
    resid = []
    for old, _n in [(o, 0) for o, _ in pairs]:
        head = re.split(r'[\s（(]', old.strip())[0]
        if len(head) >= 4 and head in out:
            ctx = out[max(0, out.find(head) - 30): out.find(head) + len(head) + 30]
            resid.append((head, out.count(head), ctx.replace('\n', ' ')))
    if resid:
        print('  [残存警告] 置換語の先頭語が別表記で残存: %s' % resid[:5])
    return out, log


def _near(text, old):
    key = old[:12]
    for line in text.split('\n'):
        if key and key[:6] in line:
            return line[:80]
    return ''


def write(qid, ja, en, old_ja=None, old_en=None, allow_line_delta=0, min_ja=2400):
    '''DBへ書く。バックアップ->不変条件->検出器->字数->書込み->読み直し照合まで一括。'''
    if old_ja is not None:
        v = invariants(old_ja, ja, allow_line_delta) + invariants(old_en or '', en, allow_line_delta)
        assert not v, '不変条件違反: %s' % v
    assert len(ja) >= min_ja, '字数不足 ja=%d' % len(ja)
    assert len(en) >= len(ja) * 2 or (len(en) >= 8000 and len(en) / len(ja) >= 1.7), 'en不足 %d/%d' % (len(en), len(ja))
    ngb, hb = _bc.check(ja, en)
    assert not ngb, '出典装飾の残存 %s' % hb[:3]
    ng, lines = checks(qid, ja, en)
    shutil.copy(DB, os.path.join(BK, 'nipponexus.db.bak_' + ts()))
    c = sqlite3.connect(DB)
    c.execute('UPDATE festivals SET manual_content_ja=?, manual_content_en=? WHERE qid=?', (ja, en, qid))
    c.commit()
    rja, ren = c.execute('SELECT manual_content_ja,manual_content_en FROM festivals WHERE qid=?', (qid,)).fetchone()
    c.close()
    assert (rja, ren) == (ja, en), '書込み後の照合失敗'
    return {'ng': ng, 'lines': lines, 'ja': len(ja), 'en': len(en)}


def setmeta(qid, **kv):
    '''start_month等のメタ更新。列名を検査してから更新する。'''
    c = sqlite3.connect(DB)
    cols = {r[1] for r in c.execute('PRAGMA table_info(festivals)')}
    bad = [k for k in kv if k not in cols]
    assert not bad, '存在しない列 %s' % bad
    for k, v in kv.items():
        c.execute('UPDATE festivals SET %s=? WHERE qid=?' % k, (v, qid))
    c.commit(); c.close()
    return {k: row(qid)[k] for k in kv}


def _sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def deploy(message, probes=None, mode='present', tries=12, wait=15):
    '''dump->add(dumpのみ)->commit->push->SHA一致->ポーリング。probes={url: 語句}。'''
    now = datetime.datetime.now()
    assert not (2245 <= int(now.strftime('%H%M')) <= 2315), 'nightly競合帯(22:45-23:15)'
    rc, o, e = _sh('python3 scripts/dump_festivals.py')
    assert rc == 0, e
    _sh('git add data/festivals_dump.sql')
    staged = _sh('git diff --cached --name-only')[1].split()
    assert staged in ([], ['data/festivals_dump.sql']), 'add混入 %s' % staged
    _sh('git commit -m "%s"' % message.replace('"', "'"))
    tok = ''
    for line in open(os.path.expanduser('~/.openclaw/.env')):
        if line.strip().startswith('GITHUB_TOKEN_NIPPONEXUS='):
            tok = line.strip().split('=', 1)[1].strip().strip('"').strip(chr(39))
    assert tok, 'token未取得'
    origin = _sh('git remote get-url origin')[1]
    pu = re.sub(r'https://[^@/]*@', 'https://', origin).replace('https://', 'https://x-access-token:%s@' % tok)
    rc, o, e = _sh('git -c credential.helper= push "%s" main' % pu)
    local = _sh('git rev-parse main')[1]
    remote = (_sh('git -c credential.helper= ls-remote "%s" refs/heads/main' % pu)[1] or ' ').split()[0]
    assert local == remote, 'SHA不一致 %s/%s' % (local[:8], remote[:8])
    st = 'ポーリングなし'
    if probes:
        for i in range(1, tries + 1):
            got = {u: fetch(u).count(w) for u, w in probes.items()}
            ok = all(v > 0 for v in got.values()) if mode == 'present' else all(v == 0 for v in got.values())
            print('  [poll %02d] %s' % (i, got))
            if ok:
                st = '反映確認済(try%d)' % i; break
            time.sleep(wait)
        else:
            st = '未反映(ビルド待ち)'
    return {'commit': local[:7], 'status': st}


def fetch(url):
    '''HTML取得(キャッシュ回避ヘッダ付き)。'''
    try:
        r = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(r, timeout=30) as f:
            return f.read().decode('utf-8', 'ignore')
    except Exception:
        return ''


def _symbols(src):
    return set(re.findall(r'^(?:def |class )?([A-Za-z_][A-Za-z0-9_]*)\s*(?:\(|=)', src, re.M))


def patch_file(path, old, new, expect=1):
    '''コード改変。バックアップ->件数一致->トップレベル定義の欠落検査->py_compile。'''
    p = os.path.expanduser(path)
    src = open(p, encoding='utf-8').read()
    n = src.count(old)
    assert n == expect, '出現%d件(期待%d) old=%r' % (n, expect, old[:60])
    out = src.replace(old, new, expect)
    lost = _symbols(src) - _symbols(out)
    assert not lost, '巻き添えで消えた定義: %s' % sorted(lost)
    # 2026-08-03: 旧実装は『書いてからpy_compile』の順序だったため、構文エラーの変更でも
    # 壊れたファイルが残った(pro_verify_loop.pyを実際に壊した)。一時ファイルで構文を検証し、
    # 通ってから本体へ書く。失敗時は本体を一切触らない。
    tmp = p + '.patchtmp'
    open(tmp, 'w', encoding='utf-8').write(out)
    try:
        py_compile.compile(tmp, doraise=True)
    except Exception:
        os.remove(tmp)
        raise
    os.remove(tmp)
    shutil.copy(p, os.path.join(BK, os.path.basename(p) + '.bak_' + ts()))
    open(p, 'w', encoding='utf-8').write(out)
    py_compile.compile(p, doraise=True)
    return {'replaced': expect, 'lost': sorted(lost)}


def shapes():
    """戻り値の形を実測して固定する。_bindは引数のみを検査し戻り値の形を見ていなかった
       (2026-08-03: nx.fixを単数と推測し、nx.invariantsを例外送出と推測して落ちた)。"""
    t = '## a\n- x\n'
    r = fix(t, [('- x', '- y')])
    assert isinstance(r, tuple) and len(r) == 2 and isinstance(r[0], str), 'nx.fix は(text, log)を返す'
    assert isinstance(invariants(t, t), list), 'nx.invariants は違反リストを返す(例外でない)'
    assert isinstance(clean(t), str), 'nx.clean は str'
    return {'fix': '(text, log)', 'invariants': 'list(違反)', 'clean': 'str',
            'write': 'dict', 'checks': '(ng, lines)', 'audit': 'dict', 'deploy': 'dict'}


def selftest():
    '''nx自身の回帰。'''
    r = []
    t = 'A\n    - x\n  B。\n'
    r.append(('不変条件:字下げ破壊を検出', invariants(t, t.replace('    - x', ' - x')) != []))
    r.append(('不変条件:無変更は健全', invariants(t, t) == []))
    r.append(('不変条件:行削除を検出', invariants(t, 'A\n  B。\n') != []))
    o, lg = fix('仮宮を出て仮宮へ', [('仮宮', '仮宮(御旅所)')])
    r.append(('置換:追記型(newがoldを含む)', o == '仮宮(御旅所)を出て仮宮(御旅所)へ' and lg[0][1] == 2))
    try:
        fix('本文', [('存在しない', 'x')]); r.append(('置換:未マッチで停止', False))
    except AssertionError:
        r.append(('置換:未マッチで停止', True))
    try:
        _bind(_dd.run_all_checks, 'nonexistent_param'); r.append(('署名検査:不一致で停止', False))
    except RuntimeError:
        r.append(('署名検査:不一致で停止', True))
    doc = '## 開催情報\n\n1. **アクセス**:\n    - 南海本線から徒歩3分\n    - 阪堺線から徒歩すぐ\n\n2. **料金**: 無料\n'
    r.append(('出典除去:入れ子字下げ不変', clean(doc).split('\n')[3] == '    - 南海本線から徒歩3分'))
    for name, ok in r:
        print('  %-34s %s' % (name, 'PASS' if ok else 'FAIL'))
    assert all(ok for _, ok in r), 'selftest失敗'
    return True
