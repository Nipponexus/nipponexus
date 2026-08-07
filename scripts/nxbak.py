# -*- coding: utf-8 -*-
"""DBスナップショット。投入直後に呼ぶ(2026-08-07事故=投入3秒前の世代しか無く復元不能)。"""
import os, shutil, glob, datetime
DB  = os.path.expanduser("~/nipponexus/data/sqlite/nipponexus.db")
DST = os.path.expanduser("~/nexus_data/_backup")
def snapshot(tag="post_deploy", keep=None):
    os.makedirs(DST, exist_ok=True)
    dst = os.path.join(DST, "nipponexus.db.bak_%s_%s"
                       % (datetime.datetime.now().strftime("%Y%m%d_%H%M%S"), tag))
    shutil.copy2(DB, dst)
    # 既定は削除しない。8/7の復旧は8/3世代まで総当たりして初めて状況が判明した。
    if keep:
        old = sorted(glob.glob(os.path.join(DST, "nipponexus.db.bak_*")))[:-keep]
        for f in old:
            os.remove(f)
        print("[BAK] %s (削除%d件)" % (os.path.basename(dst), len(old)))
    else:
        print("[BAK] %s" % os.path.basename(dst))
    return dst
