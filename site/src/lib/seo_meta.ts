import { prefEn } from "./i18n_geo";

const MON_EN = ["January","February","March","April","May","June",
  "July","August","September","October","November","December"];

type F = {
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
  if (locale === "ja") {
    const place = f.location_label_ja || f.prefecture || "日本";
    const when = f.start_month ? `例年${f.start_month}月に` : "";
    return `${place}で${when}行われる${f.label_ja}のガイド。歴史と由来、見どころ、会場へのアクセスをまとめています。最新の日程は公式の発表でご確認ください。`;
  }
  const name = f.label_en || f.label_ja;
  const place = f.prefecture ? prefEn(f.prefecture) : "Japan";
  const when = f.start_month ? ` each ${MON_EN[f.start_month - 1]}` : "";
  return `A guide to ${name}, held${when} in ${place}, Japan. History and origins, highlights, venue and access. Check the official announcement for the current schedule.`;
}
