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
                # 置換区間の先頭 (i2-i1) 行は既存行の置換後とみなし、
                # それを超えて増えた行だけを「追記」として宣言の有無を見る。
                extra = nl[j1 + (i2 - i1):j2] if (j2 - j1) > (i2 - i1) else []
                gone = ol[i1 + (j2 - j1):i2] if (i2 - i1) > (j2 - j1) else []
                bad = [s for s in extra + gone if not okline(s)]
                if bad:
                    v.append('置換で行数変化 %d -> %d (未宣言 %r)' % (i2 - i1, j2 - j1, bad[0][:40]))
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


def write(qid, ja, en, old_ja=None, old_en=None, allow_line_delta=0, min_ja=2400, allow_deleted=None, mode='replace'):
    '''DBへ書く。バックアップ->不変条件->検出器->字数->書込み->読み直し照合まで一括。'''
    assert mode in ('replace', 'augment'), "mode は 'replace' か 'augment'"
    if mode == 'augment':
        # 増補モード: 既存の全行が順序を保ち一字も変わらず残ることを要求する。
        # DBの現本文を正として突合し、引数のold_ja任せにしない(省略による検査回避を防ぐ)。
        ca = sqlite3.connect(DB)
        ra = ca.execute('SELECT manual_content_ja,manual_content_en FROM festivals WHERE qid=?', (qid,)).fetchone()
        ca.close()
        assert ra, 'qid不明 %s' % qid
        v = augment(ra[0] or '', ja) + augment(ra[1] or '', en)
        assert not v, '増補条件違反: %s' % v
    elif old_ja is None:
        c0 = sqlite3.connect(DB)
        r0 = c0.execute('SELECT manual_content_ja,manual_content_en FROM festivals WHERE qid=?', (qid,)).fetchone()
        c0.close()
        assert r0, 'qid不明 %s' % qid
        if r0[0] and len(r0[0]) >= min_ja:
            raise AssertionError(
                'old_ja省略は不可: DB現本文が既に%d字(是正済みの疑い)。'
                'old_ja/old_enを明示するか、意図的な全面差替なら old_ja=DB現本文 を渡すこと' % len(r0[0]))
    if old_ja is not None:
        v = invariants(old_ja, ja, allow_line_delta, allow_deleted) + \
            invariants(old_en or '', en, allow_line_delta, allow_deleted)
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
    # 2026-08-06: 自律駆動では同一パッチが再実行されうる(field_check接続時に二重適用の
    # 構造だった)。newが既に在りoldが無い=適用済みとみなしskip。両方在る場合は判断できない
    # ので従来どおりassertで止める。
    # ★初版は n==0 のみを見ており、oldがnewに含まれる追記型パッチ(『def shapes():』の前へ
    #   関数を挿入する型)では適用後もoldが1件残り n==1==expect が成立して再挿入されていた
    #   =冪等化のコード自体が二重適用を通す穴を持っていた(回帰で検出・2026-08-06)。
    if new and src.count(new) >= 1 and (n == 0 or old in new):
        return {'replaced': 0, 'skipped': 'already applied', 'lost': []}
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


_REGION = {'北海道':'hokkaido',
 '青森県':'tohoku','岩手県':'tohoku','宮城県':'tohoku','秋田県':'tohoku','山形県':'tohoku','福島県':'tohoku',
 '茨城県':'kanto','栃木県':'kanto','群馬県':'kanto','埼玉県':'kanto','千葉県':'kanto','東京都':'kanto','神奈川県':'kanto',
 '新潟県':'chubu','富山県':'chubu','石川県':'chubu','福井県':'chubu','山梨県':'chubu','長野県':'chubu',
 '岐阜県':'chubu','静岡県':'chubu','愛知県':'chubu',
 '三重県':'kinki','滋賀県':'kinki','京都府':'kinki','大阪府':'kinki','兵庫県':'kinki','奈良県':'kinki','和歌山県':'kinki',
 '鳥取県':'chugoku','島根県':'chugoku','岡山県':'chugoku','広島県':'chugoku','山口県':'chugoku',
 '徳島県':'shikoku','香川県':'shikoku','愛媛県':'shikoku','高知県':'shikoku',
 '福岡県':'kyushu','佐賀県':'kyushu','長崎県':'kyushu','熊本県':'kyushu','大分県':'kyushu','宮崎県':'kyushu','鹿児島県':'kyushu',
 '沖縄県':'okinawa'}


def _region_of(pref):
    return _REGION.get((pref or '').strip())


def _season_of(m):
    try:
        m = int(m)
    except (TypeError, ValueError):
        return None
    return {3:'spring',4:'spring',5:'spring',6:'summer',7:'summer',8:'summer',
            9:'autumn',10:'autumn',11:'autumn',12:'winter',1:'winter',2:'winter'}.get(m)


def autometa(qid, start_month=None, inception_year=None, apply=True):
    '''prefecture->region / start_month->season を決定論で埋める(2026-08-06)。
       既存の非NULL値は上書きせず不一致のみ conflict として報告する(不可逆な取り違えの防止)。
       底上げ済み248本のうち119本でメタが欠落し、検出器2(DBメタ突合)が機能していなかった。'''
    r = dict(row(qid))
    sm = start_month if start_month is not None else r.get('start_month')
    want = {'start_month': start_month, 'inception_year': inception_year,
            'region': _region_of(r.get('prefecture')), 'season': _season_of(sm)}
    out, conflict = {}, []
    for k, v in want.items():
        if v is None:
            continue
        cur = r.get(k)
        if cur in (None, ''):
            out[k] = v
        elif str(cur) != str(v):
            conflict.append((k, cur, v))
    if apply and out:
        setmeta(qid, **out)
    return {'set': out, 'conflict': conflict, 'derived_region': want['region'],
            'derived_season': want['season'], 'start_month': sm}


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


def cols(qid, *names):
    '''festivals の列を名前で取り出す。位置で受け取る事故(2026-08-04: enをNoneと誤報告)を防ぐ。
       戻りは dict なので添字の取り違えが起きない。'''
    c = sqlite3.connect(DB)
    cur = c.execute('SELECT * FROM festivals WHERE qid=?', (qid,))
    head = [d[0] for d in cur.description]
    row = cur.fetchone()
    c.close()
    assert row, 'qid不明 %s' % qid
    d = dict(zip(head, row))
    bad = [n for n in names if n not in d]
    assert not bad, '存在しない列 %s (実在=%s)' % (bad, head)
    return {n: d[n] for n in names} if names else d


def lens(qid):
    '''本文の実測長。字数を語るときは必ずこれを通す(推測で述べない)。'''
    d = cols(qid, 'manual_content_ja', 'manual_content_en', 'label_ja', 'slug_ja', 'slug_en')
    return {'ja': len(d['manual_content_ja'] or ''), 'en': len(d['manual_content_en'] or ''),
            'label_ja': d['label_ja'], 'slug_ja': d['slug_ja'], 'slug_en': d['slug_en']}


def pairs(ja_fixes, ja, en):
    '''JA是正ペアのEN対応段落を提示。曖昧/不在があればTrueを返す(要対処)。'''
    import pair_check as _pc
    rs = _pc.require_pairs(ja_fixes, ja, en)
    bad = [r for r in rs if not r['found']]
    if bad:
        print('  [要対処] 対応を確定できないJA是正が %d 件' % len(bad))
    return rs, bool(bad)


def augment(old, new):
    '''増補モードの不変条件。既存の全行が順序を保ち一字も変えずに残り、
       追加のみが起きていることを検証する。違反の一覧を返す(空なら健全)。
       全面差替(invariants)と違い replace/delete は常に違反=宣言で通す道がない。'''
    import difflib
    v, ol, nl = [], old.split('\n'), new.split('\n')
    add = 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ol, nl).get_opcodes():
        if op == 'equal':
            continue
        if op == 'insert':
            add += (j2 - j1)
            continue
        if op == 'delete':
            for s in ol[i1:i2]:
                if s.strip():
                    v.append('既存行の削除 %r' % s[:50])
        elif op == 'replace':
            for a, b in zip(ol[i1:i2], nl[j1:j2]):
                if a.strip() and a != b:
                    v.append('既存行の改変 %r -> %r' % (a[:34], b[:34]))
            if (i2 - i1) > (j2 - j1):
                for s in ol[i1 + (j2 - j1):i2]:
                    if s.strip():
                        v.append('既存行の削除 %r' % s[:50])
            else:
                add += (j2 - j1) - (i2 - i1)
    if add == 0 and not v:
        v.append('増補なし(追加行が0)')
    return v


def docfix(path, old, new, backup_dir='~/nexus_data/_backup'):
    """運営三書など文書の置換。2026-08-05: 同日に冪等チェックを3回間違えた
       (部分一致 NEW[:20] が別文に当たり『既に反映済み』と誤報告 / copy(p,p) /
       エスケープ済み文字列の検索失敗)。判定を人の書く式に委ねず実測カウントで行う。
       戻り値 dict(status, old_before, new_before, old_after, new_after)。"""
    import os, shutil, datetime
    p = os.path.expanduser(path)
    s = open(p, encoding='utf-8').read()
    ob, nb = s.count(old), s.count(new)
    if ob == 0 and nb > 0:
        return {'status': 'already', 'old_before': ob, 'new_before': nb,
                'old_after': ob, 'new_after': nb}
    if ob == 0 and nb == 0:
        raise AssertionError('置換対象も置換後も不在=対象文を確認せよ: %r' % old[:60])
    d = os.path.expanduser(backup_dir)
    os.makedirs(d, exist_ok=True)
    bk = os.path.join(d, os.path.basename(p) + '.bak_' +
                      datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    shutil.copy(p, bk)
    open(p, 'w', encoding='utf-8').write(s.replace(old, new))
    t = open(p, encoding='utf-8').read()
    oa, na = t.count(old), t.count(new)
    if oa != 0:
        raise AssertionError('置換後も旧文が残存 %d件' % oa)
    return {'status': 'done', 'old_before': ob, 'new_before': nb,
            'old_after': oa, 'new_after': na, 'backup': os.path.basename(bk)}


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
