#!/usr/bin/env python3
"""step92: サイト向けJSONの修正とAstroページ生成"""
import os,sys,json,sqlite3,datetime,shutil
ROOT=os.path.expanduser('~/nipponexus'); DB=os.path.join(ROOT,'data/sqlite/nipponexus.db')
SITE=os.path.join(ROOT,'site'); OUT=os.path.join(ROOT,'out'); PG=os.path.join(SITE,'src/pages')
APPLY=str(os.environ.get('NX_APPLY','')).lower() in ('1','true','yes')
TODAY=datetime.date.today().isoformat()

raw=json.load(open(os.path.join(OUT,'calendar.json'),encoding='utf-8'))
items=raw.get('items') or []
con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
meta={r['qid']:dict(r) for r in con.execute("select qid,prefecture,slug_ja,wikipedia_ja,status from festivals")}
def conv(it):
    m=meta.get(it.get('qid',''),{})
    s=it.get('date_start') or ''; e=it.get('date_end') or ''
    return {'qid':it.get('qid',''),'name':it.get('label_ja') or '',
            'pref':(it.get('prefecture') or m.get('prefecture') or ''),
            'start':s,'end':e if e and e!=s else '','rule':it.get('rule') or '',
            'conf':it.get('confidence') or '','slug':m.get('slug_ja') or '','wiki':m.get('wikipedia_ja') or ''}
annual=sorted([conv(i) for i in items],key=lambda x:x['start'])
nxt=[c for c in annual if c['start']>=TODAY][:12]
if len(nxt)<12: nxt+=annual[:12-len(nxt)]
print('  annual',len(annual),'/ next',len(nxt),'/ 県名あり',sum(1 for c in annual if c['pref']),'/ 記事あり',sum(1 for c in annual if c['slug']))
assert len(annual)>200 and len(nxt)==12,'件数異常'
assert all(nxt[i]['start']<=nxt[i+1]['start'] for i in range(len(nxt)-1)),'昇順でない'
assert all(c['start'] and c['name'] for c in nxt),'日付か名称が空'
print('  self-test OK'); print('  先頭3件:')
for c in nxt[:3]: print('   ',c['start'],c['name'],c['pref'],c['rule'])
site={'generated':datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),'today':TODAY,'next':nxt,'annual':annual}
json.dump(site,open(os.path.join(OUT,'site_calendar.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)

L={'PREFFILL':'所在地の補完','DATEFIX':'開催日の訂正','DATEGUARD':'掲載見送り','pref':'所在地の訂正','canon':'名称の照合'}
def kind(t): 
    for k,v in L.items():
        if t.startswith(k): return v
    return 'その他'
rows=[{'kind':kind(r['tkey']),'name':r['ja'] or '','old':r['old'] or '','new':r['new'] or '',
       'note':r['note'] or '','url':r['url'] or '','at':(r['decided_at'] or '')[:10]}
      for r in con.execute("select tkey,ja,old,new,note,url,decided_at from verdict_ledger order by decided_at desc")]
rows=[r for r in rows if r['kind']!='その他' and r['name']]
json.dump({'generated':site['generated'],'rows':rows},open(os.path.join(OUT,'site_corrections.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
from collections import Counter
print('  訂正履歴',len(rows),'件',dict(Counter(r['kind'] for r in rows)))
con.close()

CAL='''---
import fs from "node:fs";
import path from "node:path";
import BaseLayout from "../layouts/BaseLayout.astro";
let d = { generated: "", next: [], annual: [] };
try { d = JSON.parse(fs.readFileSync(path.resolve(process.cwd(), "../out/site_calendar.json"), "utf-8")); } catch (e) {}
const months = Array.from({ length: 12 }, (_, i) => {
  const m = String(i + 1).padStart(2, "0");
  return { m: i + 1, rows: d.annual.filter((r) => (r.start || "").slice(5, 7) === m) };
});
const fmt = (s, e) => { const f = (x) => x.slice(5, 7) + "/" + x.slice(8, 10); return e ? f(s) + "〜" + f(e) : f(s); };
const link = (r) => (r.slug ? "/" + r.slug + "/" : r.wiki);
---
<BaseLayout title="祭りカレンダー | Nipponexus" description="日本各地の祭りの開催日を、各記事に記載された開催規則から算出した一覧です。" locale="ja" altLang="https://nipponexus.com/en/calendar/">
  <h1>祭りカレンダー</h1>
  <p>収録 {d.annual.length} 件 / 更新 {d.generated}</p>
  <p>開催日は記事に記載された規則（例「7月第3土曜日」）から算出した推定値です。旧暦基準・隔年開催・過去の規則にあたるものは除外しています。実際の日程は主催者の発表をご確認ください。</p>
  <h2>次に来る祭り</h2>
  <ul>
    {d.next.map((r) => (<li><b>{fmt(r.start, r.end)}</b> <a href={link(r)}>{r.name}</a> {r.pref && <span>（{r.pref}）</span>} <small>{r.rule}</small></li>))}
  </ul>
  {months.map((mo) => mo.rows.length > 0 && (
    <section><h2>{mo.m}月（{mo.rows.length}件）</h2>
      <ul>{mo.rows.map((r) => (<li>{fmt(r.start, r.end)} <a href={link(r)}>{r.name}</a> {r.pref && <span>（{r.pref}）</span>}</li>))}</ul>
    </section>))}
</BaseLayout>
'''
FIX='''---
import fs from "node:fs";
import path from "node:path";
import BaseLayout from "../layouts/BaseLayout.astro";
let d = { generated: "", rows: [] };
try { d = JSON.parse(fs.readFileSync(path.resolve(process.cwd(), "../out/site_corrections.json"), "utf-8")); } catch (e) {}
const kinds = [...new Set(d.rows.map((r) => r.kind))];
---
<BaseLayout title="訂正と検証の記録 | Nipponexus" description="掲載前の照合で見つかった誤りと、確証が得られず掲載を見送った項目の記録です。" locale="ja" altLang="https://nipponexus.com/en/corrections/">
  <h1>訂正と検証の記録</h1>
  <p>{d.rows.length} 件 / 更新 {d.generated}</p>
  <p>掲載前に記事本文とウィキデータの二経路で照合し、一方でしか裏が取れない場合は採用せず記録しています。</p>
  {kinds.map((k) => (
    <section><h2>{k}（{d.rows.filter((r) => r.kind === k).length}件）</h2>
      <table><thead><tr><th>対象</th><th>修正前</th><th>修正後</th><th>理由</th></tr></thead>
        <tbody>{d.rows.filter((r) => r.kind === k).map((r) => (
          <tr><td>{r.url ? <a href={r.url}>{r.name}</a> : r.name}</td><td>{r.old || "—"}</td><td>{r.new || "—"}</td><td>{r.note}</td></tr>))}
        </tbody></table>
    </section>))}
</BaseLayout>
'''
if APPLY:
    for n,c in (('calendar.astro',CAL),('corrections.astro',FIX)):
        p=os.path.join(PG,n)
        if os.path.exists(p): shutil.copy2(p,p+'.bak')
        open(p,'w',encoding='utf-8').write(c); print('[OK] site/src/pages/'+n)
    h=os.path.join(SITE,'src/components/Header.astro'); src=open(h,encoding='utf-8').read()
    if 'calendar' not in src:
        shutil.copy2(h,h+'.bak')
        old="<a href={indexPath}>{isJa ? '索引' : 'Index'}</a>"
        if old in src:
            src=src.replace(old,old+"\n      <a href=\"/calendar/\">{isJa ? 'カレンダー' : 'Calendar'}</a>\n      <a href=\"/corrections/\">{isJa ? '訂正記録' : 'Corrections'}</a>")
            open(h,'w',encoding='utf-8').write(src); print('[OK] Header にリンク追加')
        else: print('[NG] Header のリンク行が一致せず・手動対応')
else: print('[--] dry-run（JSONのみ生成・ページ未作成）')
print('APPLY='+str(APPLY))
