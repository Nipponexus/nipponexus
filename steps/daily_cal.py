#!/usr/bin/env python3
"""日次: カレンダーと訂正履歴を再生成。DB は書き換えない。片方失敗でも他方は生成する。"""
import os, sys, json, datetime, traceback
ROOT = os.path.join(os.path.expanduser("~"), "nipponexus")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
LOG = os.path.join(ROOT, "logs", "daily_cal.log")
os.makedirs(os.path.dirname(LOG), exist_ok=True)
res = {}
for name in ("nxcal", "nxfix"):
    try:
        m = __import__(name)
        res[name] = m.render()
    except Exception as e:
        res[name] = {"error": repr(e), "tb": traceback.format_exc()[-400:]}
ok = all("error" not in v for v in res.values())
line = (datetime.datetime.now().isoformat(timespec="seconds") + " "
        + ("OK " if ok else "NG ") + json.dumps(res, ensure_ascii=False))
open(LOG, "a", encoding="utf-8").write(line + "\n")
print(line)
sys.exit(0 if ok else 1)
