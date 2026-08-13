import { prefEn } from "./i18n_geo";
import { desc2 } from "./seo_desc2";
import { title2 } from "./seo_title2";

const MON_EN = ["January","February","March","April","May","June",
  "July","August","September","October","November","December"];

type F = {
  qid?: string | null;
  label_ja: string;
  label_en?: string | null;
  prefecture?: string | null;
  location_label_ja?: string | null;
  start_month?: number | null;
};

export function seoTitle(f: F, locale: string): string {
  return title2(f, locale);
}

export function seoDesc(f: F, locale: string): string {
  return desc2(f, locale);
}
