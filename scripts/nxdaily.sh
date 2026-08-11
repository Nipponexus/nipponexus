#!/bin/bash
# Nipponexus daily: 選題 -> 生成 -> 昇格 -> カレンダー反映 -> ログ/通知
# 2026-08-12 新規。push/デプロイは23:00のnightly_rebuild.shに委ねる(競合回避)
cd ~/nipponexus || exit 1
LOGDIR="$HOME/nexus_data/logs"; mkdir -p "$LOGDIR"
LOG="$LOGDIR/$(date +%Y%m%d).log"
PY3=/usr/bin/python3
say(){ echo "[$(date '+%F %T')] $*" >> "$LOG"; }
notify(){
  source ~/.openclaw/.env 2>/dev/null
  [ -z "$DISCORD_WEBHOOK" ] && return 0
  curl -s -H 'Content-Type: application/json' \
    -d "$($PY3 -c 'import json,sys;print(json.dumps({"content":sys.argv[1][:1800]}))' "$1")" \
    "$DISCORD_WEBHOOK" > /dev/null
}
say "===== daily start ====="

QID=$($PY3 scripts/nxpick.py -n 1 2>>"$LOG" | head -1 | awk '{print $1}')
if [ -z "$QID" ]; then
  say "[STOP] 選題ゼロ(在庫切れ)"; notify "Nipponexus daily [STOP] 選題ゼロ。在庫切れ"; exit 1
fi
say "[pick] $QID"

$PY3 scripts/run_one.py --qid "$QID" --write >> "$LOG" 2>&1
RC=$?
if [ $RC -ne 0 ]; then
  say "[STOP] run_one 異常終了 rc=$RC"; notify "Nipponexus daily [STOP] $QID run_one rc=$RC"; exit 1
fi

RES=$($PY3 - "$QID" <<'PYEOF' 2>>"$LOG"
import sys; sys.path.insert(0,'scripts')
import nxauto
q = sys.argv[1]
m = nxauto.set_month(q)
s = nxauto.ensure_slug(q, apply=True)
if not s:
    print('STOP\tslug未発行(label_en不整合の可能性)\t%s' % m); raise SystemExit(0)
f = nxauto.finalize(q, apply=True)
print(('OK' if f.get('ok') else 'STOP') + '\t' + str(f) + '\t' + str(s))
PYEOF
)
say "[promote] $RES"
case "$RES" in
  OK*) ;;
  *) notify "Nipponexus daily [STOP] $QID
$RES"; say "[STOP] 昇格せず"; exit 1 ;;
esac

NX_APPLY=1 $PY3 steps/step92.py >> "$LOG" 2>&1
say "[cal] site_calendar 更新"

# バックアップ30世代ローテ(nx.writeが毎回.bakを作る)
ls -1t data/sqlite/nipponexus.db.bak_* 2>/dev/null | tail -n +31 | while read f; do rm -f "$f"; say "[rot] rm $f"; done
# 役割完了の一時ファイル掃除(00-G)
rm -f "$HOME/nexus_data/llm_sim/${QID}_"* 2>/dev/null && say "[clean] llm_sim/$QID"

say "[DONE] $QID 投入完了。push/公開は23:00のnightlyに委任"
notify "Nipponexus daily [OK] $QID 投入完了"
