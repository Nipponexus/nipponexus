import { verifiedIndexStatuses } from "./index_event_status";

/** Display-only, source-verified cessation of this exact named event.
 * Never infer cessation from all index badges, raw event_end, or old names.
 * Source re-read 2026-11-06: 相模原市FAQ1028587 (updated 2023-05-19).
 * 「泳げ鯉のぼり相模川」は実行委員会の決定により、令和元年度の開催をもって終了しております。
 * 実行委員会も解散しており、現時点での再開の予定はないとのことです。
 * No article/checker exemption; raw recurrence data and articles stay intact.
 */
export const verifiedCalendarCessations = {
  Q65272329: {
    ...verifiedIndexStatuses.Q65272329,
    eventName: "泳げ鯉のぼり相模川",
    finalFiscalYear: 2019,
    disposition: "named-event-ended-no-restart-announced",
    reverifiedAt: "2026-11-06T10:10:34+09:00",
  },
};

export function calendarForecastRows<T extends { qid?: string }>(rows: T[]): T[] {
  return rows.filter((row) => !Object.hasOwn(verifiedCalendarCessations, row.qid || ""));
}

export function calendarForecastView<T extends { annual: { qid?: string }[]; next?: { qid?: string }[] }>(data: T): T {
  return { ...data, annual: calendarForecastRows(data.annual),
    ...(data.next ? { next: calendarForecastRows(data.next) } : {}) };
}
