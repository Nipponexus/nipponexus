#!/usr/bin/env python3
"""
Nipponexus: Wikidata から日本の祭り・年中行事を取得
v3: 全UNION枝に日本国内フィルタを必須化・サブクラス暴走源を除去
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = "Nipponexus/0.3 (https://nipponexus.com; info@nexus-ds.jp) python-requests/2.32"

QUERY = """
SELECT DISTINCT ?item ?itemLabel ?itemLabelEn ?descJa ?descEn 
                ?location ?locationLabel ?locationLabelEn
                ?coord ?inception ?startTime ?endTime ?pointInTime ?month ?image
                ?wikipediaJa ?wikipediaEn
WHERE {
  {
    ?item wdt:P31/wdt:P279* wd:Q132241 .
    ?item wdt:P17 wd:Q17 .
  } UNION {
    ?item wdt:P31 wd:Q19833351 .
  } UNION {
    ?item wdt:P31/wdt:P279* wd:Q132241 .
    ?item wdt:P276 ?loc .
    ?loc wdt:P17 wd:Q17 .
  } UNION {
    ?item wdt:P31 wd:Q5891044 .
  }

  OPTIONAL { ?item rdfs:label ?itemLabel    FILTER(LANG(?itemLabel) = "ja") }
  OPTIONAL { ?item rdfs:label ?itemLabelEn  FILTER(LANG(?itemLabelEn) = "en") }
  OPTIONAL { ?item schema:description ?descJa FILTER(LANG(?descJa) = "ja") }
  OPTIONAL { ?item schema:description ?descEn FILTER(LANG(?descEn) = "en") }
  OPTIONAL {
    ?item wdt:P276 ?location .
    OPTIONAL { ?location rdfs:label ?locationLabel   FILTER(LANG(?locationLabel) = "ja") }
    OPTIONAL { ?location rdfs:label ?locationLabelEn FILTER(LANG(?locationLabelEn) = "en") }
  }
  OPTIONAL { ?item wdt:P625 ?coord }
  OPTIONAL { ?item wdt:P571 ?inception }
  OPTIONAL { ?item wdt:P580 ?startTime }
  OPTIONAL { ?item wdt:P582 ?endTime }
  OPTIONAL { ?item wdt:P585 ?pointInTime }
  OPTIONAL { ?item wdt:P837 ?month }
  OPTIONAL { ?item wdt:P18 ?image }
  OPTIONAL { ?wikipediaJa schema:about ?item ;
                          schema:inLanguage "ja" ;
                          schema:isPartOf <https://ja.wikipedia.org/> }
  OPTIONAL { ?wikipediaEn schema:about ?item ;
                          schema:inLanguage "en" ;
                          schema:isPartOf <https://en.wikipedia.org/> }
}
"""


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=4, max=30))
def fetch_sparql(query):
    headers = {"User-Agent": USER_AGENT, "Accept": "application/sparql-results+json"}
    response = requests.get(SPARQL_ENDPOINT, params={"query": query, "format": "json"},
                            headers=headers, timeout=90)
    response.raise_for_status()
    return response.json()


def main():
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    print(f"[INFO] 開始: {ts} (v3)")

    try:
        result = fetch_sparql(QUERY)
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTPError: {e}", file=sys.stderr)
        if e.response is not None:
            print(f"  body: {e.response.text[:500]}", file=sys.stderr)
        sys.exit(1)

    bindings = result["results"]["bindings"]
    qids = {b["item"]["value"].rsplit("/", 1)[-1] for b in bindings if "item" in b}
    print(f"[INFO] 取得行数: {len(bindings)}")
    print(f"[INFO] ユニーク QID: {len(qids)}")

    out_path = RAW_DIR / f"festivals_wikidata_{ts}.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[INFO] 保存: {out_path.name} ({out_path.stat().st_size:,} bytes)")

    print("\n=== サンプル15件 ===")
    seen = set()
    n = 0
    for b in bindings:
        qid = b.get("item", {}).get("value", "").rsplit("/", 1)[-1]
        if qid in seen:
            continue
        seen.add(qid)
        ja = b.get("itemLabel", {}).get("value", "")
        en = b.get("itemLabelEn", {}).get("value", "")
        loc = b.get("locationLabel", {}).get("value", "")
        print(f"  {qid}: {ja} / {en} ({loc})")
        n += 1
        if n >= 15:
            break


if __name__ == "__main__":
    main()
