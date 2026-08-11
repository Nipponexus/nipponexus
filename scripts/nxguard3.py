# nxguard3: 日付規則の信頼性判定 v3
import re
_Z=str.maketrans('０１２３４５６７８９','0123456789')
def norm(s): return (s or '').translate(_Z)
CONCEPT_EXACT={'七夕','日本の七夕','端午の節句','雛祭り','桃の節句','地蔵盆','元始祭',
 '二百十日','二百二十日','入梅','節分','中秋の名月','半夏生','土用の丑の日'}
RE_CONCEPT=re.compile(r'三大|一覧|総称')
RE_CYCLE=re.compile(r'隔年|一年おき|[0-9二三四五六七八九十]年に[一1１]度|下一桁')
RE_PAST=re.compile(r'古くは|かつては|以前は|旧来|明治初年|江戸時代|明治時代|大正時代|昭和初期|当時は|旧暦.{0,8}時代|までは.{0,12}(行わ|執行|開催)')
RE_LUNAR=re.compile(r'旧暦|太陰暦|中秋の名月|十五夜|八朔')
RE_PERIOD=re.compile(r'試験的|\d{4}年の開催から\d{4}年まで')
RE_CHANGED=re.compile(r'(\d{4}年|平成\d{1,2}年|令和\d{1,2}年)(より|から)[^。]{0,24}(変更|移動|開催されるように|行われるように|変わ)')
RE_SIG=re.compile(r'毎年|例年|恒例')
RE_YEAR=re.compile(r'\d{4}年')
def classify(title,rule,src):
    t=norm(title).strip(); s=norm(src)
    if t in CONCEPT_EXACT or RE_CONCEPT.search(t): return 'concept','暦の行事・まとめ記事で個別の開催日を持たない'
    if RE_CYCLE.search(s): return 'cycle','毎年開催ではない（隔年・数年に一度）'
    if RE_PAST.search(s):  return 'past','抽出元が過去の開催日を述べている'
    if RE_LUNAR.search(s): return 'lunar','旧暦基準のため新暦換算が必要'
    if RE_PERIOD.search(s):return 'review','期間限定・試験的な日程'
    if RE_CHANGED.search(s):return 'review','途中で開催日が変更された記述あり'
    if RE_YEAR.search(s) and not RE_SIG.search(s): return 'review','特定年の告知のみで毎年性の根拠なし'
    return 'ok',''
