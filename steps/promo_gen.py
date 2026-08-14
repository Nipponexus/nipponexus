"""promo_gen : 発信スケジュールと下書きを生成する。
date_guard='ok' の祭りだけ具体日を書き、それ以外は月の相対表現に落とす。
既存ファイルへの手術はせず、このファイル単体で完結する。"""
import os, re, sqlite3, datetime, json

ROOT = os.path.join(os.path.expanduser("~"), "nipponexus")
DB   = os.path.join(ROOT, "data", "sqlite", "nipponexus.db")
OUT  = os.path.join(ROOT, "out")
LEAD = 21  # 開催の何日前に投稿するか

def rows(months):
    """開催月は start_month を最優先。date_rule の文字列は補助にとどめる。
    date_guard が past / concept のものは発信対象から外す（旧日程・総称記事）。"""
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row
    r = [dict(x) for x in c.execute(
        "SELECT qid,label_ja,prefecture,slug_ja,date_rule,date_guard,start_month,image_url,"
        "length(ifnull(manual_content_ja,'')) blen FROM festivals "
        "WHERE slug_ja IS NOT NULL AND status IN ('drafted','published')")]
    c.close()
    out = []
    for x in r:
        if (x.get("date_guard") or "") in ("past", "concept"):
            continue
        m = x.get("start_month")
        if not m:
            mm = re.search(r"毎年(\d{1,2})月", x.get("date_rule") or "")
            m = int(mm.group(1)) if mm else None
        if m not in months:
            continue
        x["month"] = m
        out.append(x)
    return out

def when(x):
    """guard が ok のときだけ規則をそのまま出す。それ以外は月のみ。"""
    if (x.get("date_guard") or "") == "ok" and x.get("date_rule"):
        return x["date_rule"], True
    return "%d月ごろ（日程未確定）" % x["month"], False

def build(months=(9, 10, 11), today=None):
    today = today or datetime.date.today()
    items = sorted(rows(months), key=lambda x: (x["month"], x["label_ja"]))
    sch = ["# 発信スケジュール（%s 生成 %s）" % ("-".join(map(str, months)) + "月", today.isoformat()), "",
           "日程を確定できた祭りのみ具体日を記載します。未確定は月のみとし、投稿時は日付に触れません。", "",
           "| 開催 | 記事 | 県 | 日程 | 確定 | 本文 | 画像 |", "|---|---|---|---|---|---|---|"]
    dr = ["# 発信下書き（生成 %s）" % today.isoformat(), ""]
    n_ok = 0
    for x in items:
        w, fixed = when(x)
        if fixed: n_ok += 1
        sch.append("| %d月 | %s | %s | %s | %s | %d | %s |" % (
            x["month"], x["label_ja"], x["prefecture"] or "-", w,
            "確定" if fixed else "未確定", x["blen"], "有" if x["image_url"] else "無"))
        dr += ["## %s / %s" % (x["slug_ja"], w), "",
               "```", "%s（%s）" % (x["label_ja"], x["prefecture"] or ""), "",
               ("例年の開催時期は%sです。最新の日程は主催者の公式発表でご確認ください。" % w) if not fixed
               else ("開催は%s。最新の日程は主催者の公式発表でご確認ください。" % x["date_rule"]),
               "", "https://nipponexus.com/%s/" % x["slug_ja"], "```", ""]
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "promo_schedule.md"), "w", encoding="utf-8").write("\n".join(sch) + "\n")
    open(os.path.join(OUT, "promo_drafts.md"), "w", encoding="utf-8").write("\n".join(dr) + "\n")
    return {"total": len(items), "fixed": n_ok, "unfixed": len(items) - n_ok}

if __name__ == "__main__":
    print(json.dumps(build(), ensure_ascii=False))
