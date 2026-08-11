# -*- coding: utf-8 -*-
# CITYCHAIN_v2 : 市区町村名 -> 帰属県。祭の名称を一切経由しない独立経路。
# v1 の欠陥 = 「多気郡明和町」のように郡名込みで jawiki を引き、記事に当たらず解決不能だった。
# v2 = 郡を剥がした候補、曖昧回避の「県名+市名」候補を順に試す。
import re, time
import nxwiki
GUN = re.compile(r"^[\u4e00-\u9fa5\u3040-\u30ff]{1,5}郡")
CITY_RX = None

def city_candidates(pref, city):
    """照会に使うタイトル候補を優先順に返す。"""
    out = []
    bare = GUN.sub("", city)          # 多気郡明和町 -> 明和町
    for c in ([city] if city != bare else []) + [bare]:
        out.append(c)
        out.append("%s (%s)" % (c, pref))   # 明和町 (三重県)
        out.append(pref + c)                 # 三重県明和町
    seen, r = set(), []
    for x in out:
        if x not in seen:
            seen.add(x); r.append(x)
    return r

def resolve(pairs, ua=None, verbose=True):
    """[(pref, city)] -> {(pref,city): 県名}。pref は候補生成の絞り込みにのみ使う。"""
    titles = []
    idx = {}
    for pref, city in pairs:
        cs = city_candidates(pref, city)
        idx[(pref, city)] = cs
        titles += cs
    titles = list(dict.fromkeys(titles))
    qmap = nxwiki.pageprops_qid(titles, ua=ua)
    ids = [v for v in qmap.values() if v]
    ents = nxwiki.wd_entities(ids, ua=ua)
    res, why = {}, {}
    for key, cands in idx.items():
        for t in cands:
            qid = qmap.get(t)
            if not qid:
                continue
            p = nxwiki.wd_climb_pref(qid, ents, ua=ua)
            if p:
                res[key] = p; why[key] = "%s -> %s -> P131" % (t, qid); break
    return res, why
