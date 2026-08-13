// seo_title2.ts (2026-08-13 新規・独立モジュール)
// 旧版は固定尾部が長くJA91%/EN97%が表示上限超過。尾部を短縮し、超過時は 月→ブランド→県 の順に落とす。
import { prefEn } from "./i18n_geo";

const MON_EN = ["January","February","March","April","May","June",
  "July","August","September","October","November","December"];
const MAX_JA = 32, MAX_EN = 60;

export type TitleF = {
  label_ja: string;
  label_en?: string | null;
  prefecture?: string | null;
  start_month?: number | null;
};

const STEPS: [boolean, boolean, boolean][] =
  [[true,true,true],[true,false,true],[false,true,true],[false,false,true],[false,false,false]];

export function title2(f: TitleF, locale: string): string {
  if (locale === "ja") {
    for (const [brand, month, pref] of STEPS) {
      const parts: string[] = [];
      if (pref && f.prefecture) parts.push(f.prefecture);
      if (month && f.start_month) parts.push(`例年${f.start_month}月`);
      const head = parts.join("・");
      const core = head ? `${f.label_ja}（${head}）` : f.label_ja;
      const s = `${core}の見どころ` + (brand ? "｜Nipponexus" : "");
      if (s.length <= MAX_JA) return s;
    }
    return f.label_ja.length <= MAX_JA ? f.label_ja : f.label_ja.slice(0, MAX_JA);
  }
  const name = f.label_en || f.label_ja;
  const pref = f.prefecture ? prefEn(f.prefecture) : "";
  for (const [brand, month, usePref] of STEPS) {
    const parts: string[] = [];
    if (usePref && pref) parts.push(pref);
    if (month && f.start_month) parts.push(MON_EN[f.start_month - 1]);
    const head = parts.join(", ");
    const core = head ? `${name} (${head})` : name;
    const s = `${core} Dates & Access` + (brand ? " | Nipponexus" : "");
    if (s.length <= MAX_EN) return s;
  }
  return name.length <= MAX_EN ? name : name.slice(0, MAX_EN);
}
