import { prefEn } from "./i18n_geo";
import { desc2 } from "./seo_desc2";

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
  if (locale === "ja") {
    const head = [f.prefecture || "", f.start_month ? `例年${f.start_month}月` : ""]
      .filter(Boolean).join("・");
    const core = head ? `${f.label_ja}（${head}）` : f.label_ja;
    const full = `${core}の見どころとアクセス｜Nipponexus`;
    return full.length <= 42 ? full : `${core}｜Nipponexus`;
  }
  const name = f.label_en || f.label_ja;
  const head = [f.prefecture ? prefEn(f.prefecture) : "",
    f.start_month ? MON_EN[f.start_month - 1] : ""].filter(Boolean).join(", ");
  const core = head ? `${name} (${head})` : name;
  return `${core}: Dates, Access and Highlights | Nipponexus`;
}

export function seoDesc(f: F, locale: string): string {
  return desc2(f, locale);
}
