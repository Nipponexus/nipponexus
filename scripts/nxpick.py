#!/usr/bin/env python3
"""nxpick: 日次自走の選題(2026-08-11)。判定はせず『次の1本のqid』だけを決定論で返す。
対象= status='pending' かつ wikipedia_ja あり かつ 本文未満2400字。
除外= deepseek_draft.EXCLUDE_QIDS / skipped_* / excluded_shrine(status条件で自動除外)。
順序= priority_score desc, qid asc(同点でも毎日同じ順=再現可能)。
使い方: python3 scripts/nxpick.py        -> qid を1行出力(無ければ終了コード3)
        python3 scripts/nxpick.py -n 5   -> 上位5件を確認用に出力
"""
import os,sys,sqlite3,argparse
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
DB=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data/sqlite/nipponexus.db')
def excludes():
    try:
        import deepseek_draft as dd
        return list(getattr(dd,'EXCLUDE_QIDS',[]) or [])
    except Exception:
        return []
def pick(n=1):
    ex=excludes(); ph=','.join('?'*len(ex)) if ex else "''"
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
    rows=con.execute(
        "SELECT qid,label_ja,prefecture,COALESCE(priority_score,0) p FROM festivals "
        "WHERE status='pending' AND COALESCE(wikipedia_ja,'')<>'' "
        "AND COALESCE(label_en,'')<>'' "   # slug生成に必須(2026-08-11)
        "AND (label_ja LIKE '%祭%' OR label_ja LIKE '%まつり%' OR label_ja LIKE '%神事%') "
        "AND label_ja NOT LIKE '%映画祭%' AND label_ja NOT LIKE '%音楽祭%' "
        "AND label_ja NOT LIKE '%フェスティバル%' AND label_ja NOT LIKE '%フェス%' "
        "AND label_ja NOT LIKE '%映画%' AND label_ja NOT LIKE '%アニメ%' "
        "AND label_ja NOT LIKE '%ジャズ%' AND label_ja NOT LIKE '%コンサート%' "
        "AND LENGTH(COALESCE(manual_content_ja,''))<2400 "
        f"AND qid NOT IN ({ph}) ORDER BY p DESC, qid ASC LIMIT ?",
        (*ex,n)).fetchall()
    con.close(); return [dict(r) for r in rows]
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('-n',type=int,default=1); ap.add_argument('--verbose',action='store_true')
    a=ap.parse_args(); rs=pick(a.n)
    if not rs: sys.exit(3)
    for r in rs:
        print(f"{r['qid']}\t{r['p']}\t{r['prefecture'] or '-'}\t{r['label_ja']}" if (a.verbose or a.n>1) else r['qid'])
