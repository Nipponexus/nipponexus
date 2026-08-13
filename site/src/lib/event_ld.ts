// event_ld.ts  2026-08-13
// Event JSON-LD。Google必須の name/startDate/location が揃う場合のみ生成し、
// 揃わなければ null を返す（無効なEventを出さない）。日付は固定日・第n週規則から
// 次回開催日を算出する（特定年を本文に断定しないA-2.5とは独立、機械可読の構造化データのみ）。
type Rule = { type?: string; month?: number; day?: number; end_month?: number; end_day?: number; dow?: number; nth?: number };
export type EF = {
  qid?: string | null; label_ja?: string | null; label_en?: string | null;
  date_rule_json?: string | null; date_guard?: string | null;
  location_label_ja?: string | null; location_label_en?: string | null;
  prefecture?: string | null; latitude?: number | null; longitude?: number | null;
  image_url?: string | null;
};
const iso = (d: Date) => d.toISOString().slice(0, 10);
function nthDate(r: Rule, y: number): Date | null {
  if (r.month == null || r.dow == null) return null;
  const wd = (r.dow + 1) % 7; // DBは月曜=0、JSは日曜=0
  if (r.type === 'last_dow') {
    const d = new Date(Date.UTC(y, r.month, 0));
    while (d.getUTCDay() !== wd) d.setUTCDate(d.getUTCDate() - 1);
    return d;
  }
  if (r.nth == null) return null;
  const d = new Date(Date.UTC(y, r.month - 1, 1));
  while (d.getUTCDay() !== wd) d.setUTCDate(d.getUTCDate() + 1);
  d.setUTCDate(d.getUTCDate() + 7 * (r.nth - 1));
  return d.getUTCMonth() === r.month - 1 ? d : null;
}
function fixedDate(r: Rule, y: number): Date | null {
  if (r.month == null || r.day == null) return null;
  const d = new Date(Date.UTC(y, r.month - 1, r.day));
  return d.getUTCMonth() === r.month - 1 ? d : null;
}
export function nextDates(f: EF): { start: string; end?: string } | null {
  if (!f.date_rule_json || f.date_guard !== 'ok') return null;
  let r: Rule;
  try { r = JSON.parse(f.date_rule_json); } catch { return null; }
  const fx = r.type === 'fixed' || r.type === 'range_fixed';
  if (!fx && r.type !== 'nth_dow' && r.type !== 'last_dow') return null;
  const now = new Date(); const t0 = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate());
  for (const y of [now.getUTCFullYear(), now.getUTCFullYear() + 1]) {
    const s = fx ? fixedDate(r, y) : nthDate(r, y);
    if (s && s.getTime() >= t0) {
      let end: string | undefined;
      if (r.type === 'range_fixed' && r.end_month != null && r.end_day != null) {
        const e = new Date(Date.UTC(s.getUTCFullYear() + (r.end_month < r.month! ? 1 : 0), r.end_month - 1, r.end_day));
        if (e.getTime() >= s.getTime()) end = iso(e);
      }
      return { start: iso(s), end };
    }
  }
  return null;
}
export function eventLd(f: EF, isJa: boolean, url: string, desc: string) {
  const d = nextDates(f);
  if (!d) return null;
  const nm = (isJa ? f.location_label_ja : f.location_label_en || f.location_label_ja) || '';
  const pref = (f.prefecture || '').trim();
  if (!nm && !pref) return null;
  const loc: Record<string, unknown> = { '@type': 'Place', name: nm || pref };
  if (pref) loc.address = { '@type': 'PostalAddress', addressRegion: pref, addressCountry: 'JP' };
  if (f.latitude != null && f.longitude != null) loc.geo = { '@type': 'GeoCoordinates', latitude: f.latitude, longitude: f.longitude };
  const ld: Record<string, unknown> = {
    '@context': 'https://schema.org', '@type': 'Event',
    name: (isJa ? f.label_ja : f.label_en || f.label_ja) || '',
    startDate: d.start, eventStatus: 'https://schema.org/EventScheduled',
    eventAttendanceMode: 'https://schema.org/OfflineEventAttendanceMode',
    location: loc, url, description: desc,
  };
  if (d.end) ld.endDate = d.end;
  if (f.image_url) ld.image = f.image_url;
  return ld;
}
