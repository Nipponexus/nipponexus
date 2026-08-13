// seo_desc2.ts (2026-08-13 新規・独立モジュール)
// 素材は「創始年」と「駅名＋徒歩分」のみ。本文由来の称号は誤帰属が出たため不採用（00-A10）。
// 長さ超過時は 月 → 素材 の順に落とす（素材の方がCTR寄与が大きいため）。
import { prefEn } from "./i18n_geo";
import { SEO_FACTS } from "../data/seo_facts";

const MON_EN = ["January","February","March","April","May","June",
  "July","August","September","October","November","December"];
const TAIL_JA = "歴史・見どころ・アクセスを掲載。";
const TAIL_EN = "History, highlights and access.";
const MAX_JA = 118, MAX_EN = 155;

const KIND: Record<string, [string, string]> = {
  Q82113:["イベント","event"], Q1046742:["イベント","event"],
  Q1043431:["映画祭","film festival"], Q1033843:["音楽祭","music festival"],
  Q21652601:["映画祭","film festival"], Q3610588:["イベント","event"],
  Q11301756:["イベント","event"], Q2276034:["映画祭","film festival"],
  Q1151186:["音楽祭","music festival"], Q7398902:["イベント","event"],
  Q6920834:["音楽祭","music festival"], Q21653791:["イベント","event"],
  Q86740734:["イベント","event"], Q11618171:["音楽祭","music festival"],
  Q11660875:["音楽祭","music festival"],
};

export type DescF = {
  qid?: string | null;
  label_ja: string;
  label_en?: string | null;
  prefecture?: string | null;
  start_month?: number | null;
};

export function desc2(f: DescF, locale: string): string {
  const qid = f.qid || "";
  const kind = KIND[qid] || ["祭り", "festival"];
  if (locale === "ja") {
    const pref = f.prefecture || "日本";
    const fact = SEO_FACTS[qid]?.ja || "";
    const build = (withMonth: boolean, withFact: boolean) => {
      const when = withMonth && f.start_month ? `例年${f.start_month}月に` : "";
      let h = `${f.label_ja}は${pref}で${when}開催される${kind[0]}。`;
      if (withFact && fact) h += `${fact}。`;
      return h + TAIL_JA;
    };
    for (const [m, x] of [[true, true], [false, true], [true, false]] as [boolean, boolean][]) {
      const s = build(m, x);
      if (s.length <= MAX_JA) return s;
    }
    return build(false, false).slice(0, MAX_JA);
  }
  const name = f.label_en || f.label_ja;
  const pref = f.prefecture ? prefEn(f.prefecture) : "";
  const art = "aeiou".includes(kind[1][0]) ? "an" : "a";
  const fact = SEO_FACTS[qid]?.en || "";
  const build = (withMonth: boolean, withFact: boolean) => {
    const when = withMonth && f.start_month ? ` held each ${MON_EN[f.start_month - 1]}` : "";
    const base = pref
      ? `${name} is ${art} ${kind[1]}${when} in ${pref}, Japan`
      : `${name} is ${art} ${kind[1]}${when} in Japan`;
    return (withFact && fact ? `${base}, ${fact}` : base) + ". " + TAIL_EN;
  };
  for (const [m, x] of [[true, true], [false, true], [true, false]] as [boolean, boolean][]) {
    const s = build(m, x);
    if (s.length <= MAX_EN) return s;
  }
  return build(false, false).slice(0, MAX_EN);
}
