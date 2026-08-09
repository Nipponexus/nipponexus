"""DeepSeek Pro 生成本文の投入前検証。使い方: python3 tools/validate_article.py <qid> <ja.md> <en.md> [--commit]"""
import sys,re,os,sqlite3,shutil,datetime
TPL=['とは','歴史と由来','見どころ','開催情報','アクセス','周辺観光']
NOTE=[r'年によって',r'(公式|主催|自治体|市)[^。]{0,30}(発表|サイト|情報|告知)[^。]{0,30}(確認|ご確認)',r'最新[^。]{0,20}(確認|ご確認)']
A=re.compile(r'(令和\d+年度?|平成\d+年度?|20\d{2}年度?)\s*(?:から|より)[^。]{0,40}(?:となり|なりまし|変更|移行|実施|開催され|変わ)')
def check(ja,en):
    ng=[]
    hs=[h.strip() for h in re.findall(r'^\s{0,3}##\s*(.+?)\s*$',ja,re.M)]
    he=[h.strip() for h in re.findall(r'^\s{0,3}##\s*(.+?)\s*$',en,re.M)]
    if len(ja)<3000: ng.append(f"JA {len(ja)}字 < 3000 (enriched未達)")
    if len(en)<2000: ng.append(f"EN {len(en)}字 < 2000")
    if len(hs)!=len(set(hs)): ng.append(f"JA 見出し重複 {[h for h in set(hs) if hs.count(h)>1]}")
    if len(he)!=len(set(he)): ng.append(f"EN 見出し重複 {[h for h in set(he) if he.count(h)>1]}")
    if len(hs)!=len(he): ng.append(f"日英 見出し数不一致 ja={len(hs)} en={len(he)}")
    extra=[h for h in hs if not any(t in h for t in TPL)]
    if len(extra)<2: ng.append(f"独自見出し {len(extra)} < 2")
    if not any(re.search(p,ja) for p in NOTE): ng.append("A-2.5相当の確認喚起注記なし")
    if A.search(ja) and not any(re.search(p,ja) for p in NOTE): ng.append("検出器10-A 赤")
    if re.search(r'[ぁ-んァ-ヶ一-龥]',en): ng.append("EN に日本語混入")
    return ng,hs,extra
if __name__=='__main__':
    qid,pja,pen=sys.argv[1],sys.argv[2],sys.argv[3]
    ja=open(pja,encoding='utf-8').read().strip(); en=open(pen,encoding='utf-8').read().strip()
    ng,hs,extra=check(ja,en)
    print(f"JA {len(ja)}字 / EN {len(en)}字 / 見出し{len(hs)} (独自{len(extra)}): {hs}")
    if ng: print("[NG]"); [print("  -",x) for x in ng]; sys.exit(1)
    print("[OK] 検証通過")
    if '--commit' in sys.argv:
        DB=os.path.expanduser('~/nipponexus/data/sqlite/nipponexus.db')
        ts=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        BK=os.path.expanduser('~/nexus_data/_backup'); os.makedirs(BK,exist_ok=True)
        shutil.copy2(DB,f"{BK}/nipponexus.db.bak_{ts}")
        con=sqlite3.connect(DB)
        old=con.execute("SELECT length(manual_content_ja) FROM festivals WHERE qid=?",(qid,)).fetchone()
        con.execute("UPDATE festivals SET manual_content_ja=?,manual_content_en=?,updated_at=? WHERE qid=?",(ja,en,ts,qid))
        con.commit(); con.close()
        print(f"[COMMIT] {qid}: {old[0] if old else '?'}字 -> {len(ja)}字  backup=nipponexus.db.bak_{ts}")
