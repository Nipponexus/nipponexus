import { getDraftedFestivals, type Festival } from './festivals';
import { calendarForecastRows } from './calendar_event_status';
// 注目枠の選定。現状の客観指標は priority_score のみ（DB にユネスコ・重文の列なし）。
// 画像ありに限り既定3件。将来 heritage 列を追加したらこの関数だけ差し替える。
export function getFeaturedFestivals(locale: 'ja' | 'en', limit = 3): Festival[] {
  return calendarForecastRows(getDraftedFestivals(locale))
    .filter((f) => f.image_url && f.image_url.trim() !== '')
    .slice(0, limit);
}
