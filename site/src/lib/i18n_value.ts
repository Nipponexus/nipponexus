// 訂正記録の Before/After 値を英語表示に変換する。DB と JSON は日本語のまま。
// 対象は3系統のみ: 記録なし / 県名 / 「毎年…」の日付表記。未知値は原文を返す。
import { prefEn } from './i18n_geo';
const MONTH = ['January','February','March','April','May','June','July','August','September','October','November','December'];
const NTH = ['', 'first','second','third','fourth','fifth'];
const DOW: Record<string,string> = { '日':'Sunday','月':'Monday','火':'Tuesday','水':'Wednesday','木':'Thursday','金':'Friday','土':'Saturday' };
const md = (m: string, d: string): string => MONTH[Number(m) - 1] + ' ' + Number(d);
export function valueEn(v: string | null | undefined): string {
  const s = (v ?? '').trim();
  if (!s) return '';
  if (s === '（記録なし）' || s === '(記録なし)') return 'Not recorded';
  if (/^(北海道|東京都|(京都|大阪)府|.+県)$/.test(s)) return prefEn(s);
  let m = s.match(/^毎年(\d{1,2})月(\d{1,2})日[〜~-](\d{1,2})月(\d{1,2})日$/);
  if (m) {
    const sameMonth = m[1] === m[3];
    const forward = Number(m[3]) > Number(m[1]) || (sameMonth && Number(m[4]) >= Number(m[2]));
    // 終了が開始より前の異常値（訂正前の値）は月名を省略せずそのまま示す
    const tail = (sameMonth && forward) ? String(Number(m[4])) : md(m[3], m[4]);
    return 'Annually, ' + md(m[1], m[2]) + ' to ' + tail;
  }
  m = s.match(/^毎年(\d{1,2})月(\d{1,2})日$/);
  if (m) return 'Annually, ' + md(m[1], m[2]);
  m = s.match(/^毎年(\d{1,2})月第(\d)([日月火水木金土])曜日$/);
  if (m) return 'Annually, the ' + NTH[Number(m[2])] + ' ' + DOW[m[3]] + ' of ' + MONTH[Number(m[1]) - 1];
  return s;
}
