// Public index policy only. Never mutate festival records or the calendar source.
import {
  getDraftedFestivals,
  groupByRegion as legacyGroupByRegion,
  groupByPrefecture as legacyGroupByPrefecture,
  groupBySeason as legacyGroupBySeason,
  type Festival,
} from './festivals';

type Locale = 'ja' | 'en';
const PREFECTURES_BY_REGION: Record<string, readonly string[]> = {
  hokkaido: ['北海道'],
  tohoku: ['青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県'],
  kanto: ['茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県'],
  chubu: ['新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県'],
  kinki: ['三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県'],
  chugoku: ['鳥取県', '島根県', '岡山県', '広島県', '山口県'],
  shikoku: ['徳島県', '香川県', '愛媛県', '高知県'],
  kyushu: ['福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県'],
  okinawa: ['沖縄県'],
};
const REGION_BY_PREFECTURE = new Map(
  Object.entries(PREFECTURES_BY_REGION).flatMap(([region, prefs]) =>
    prefs.map(pref => [pref, region] as const)),
);

function isPublic(f: Festival, locale: Locale): boolean {
  const slug = locale === 'ja' ? f.slug_ja : f.slug_en;
  const body = locale === 'ja' ? f.manual_content_ja : f.manual_content_en;
  return (f.status === 'drafted' || f.status === 'published')
    && typeof slug === 'string' && slug.trim().length > 0
    && typeof body === 'string' && body.trim().length > 0;
}

export function getAllFestivalsForIndex(locale: Locale): Festival[] {
  return getDraftedFestivals(locale).filter(f => isPublic(f, locale));
}

export function getPublicFestivalSlugs(locale: Locale): Set<string> {
  return new Set(getAllFestivalsForIndex(locale).map(f =>
    (locale === 'ja' ? f.slug_ja : f.slug_en)!));
}

export function groupByRegion(festivals: Festival[], locale: Locale) {
  return legacyGroupByRegion(festivals.filter(f => isPublic(f, locale)).flatMap(f => {
    const region = REGION_BY_PREFECTURE.get(f.prefecture ?? '');
    return region ? [{ ...f, region }] : [];
  }), locale);
}

export function groupByPrefecture(festivals: Festival[], locale: Locale) {
  return legacyGroupByPrefecture(festivals.filter(f =>
    isPublic(f, locale) && REGION_BY_PREFECTURE.has(f.prefecture ?? '')), locale);
}

export function groupBySeason(festivals: Festival[], locale: Locale) {
  return legacyGroupBySeason(festivals.filter(f => isPublic(f, locale)), locale);
}
