# nxguard4: 日付規則の信頼性判定 v4（過去判定は近接方式）
import re
_Z=str.maketrans('０１２３４５６７８９','0123456789')
def norm(s): return (s or '').translate(_Z)
WIN=16
CONCEPT_EXACT={'七夕','日本の七夕','端午の節句','雛祭り','桃の節句','地蔵盆','元始祭','節分',
 '二百十日','二百二十日','入梅','半夏生','中秋の名月','土用の丑の日','大晦日','小正月'}
RE_CONCEPT=re.compile(r'三大|一覧|総称')
RE_CYCLE=re.compile(r'隔年|一年おき|[0-9二三四五六七八九十]年に[一1]度|下一桁')
RE_PAST_NEAR=re.compile(r'古くは|かつては|以前は|旧来は|往時は|時代には|時代は|年までは|までは')
RE_LUNAR=re.compile(r'旧暦|太陰暦|中秋の名月|十五夜|八朔')
RE_PERIOD=re.compile(r'試験的|\d{4}年の開催から\d{4}年まで')
RE_CHANGED=re.compile(r'(\d{4}年|平成\d{1,2}年|令和\d{1,2}年|平成元年|令和元年)[^。]{0,8}(より|から|以降)[^。]{0,30}(変更|移動|開催されるように|行われるように|変わ)')
RE_RECENT=re.compile(r'(20[1-3][0-9])年')
RE_SIG=re.compile(r'毎年|例年|恒例')
def _past_near(rule,src):
    m=re.search(r'(\d{1,2})月',rule)
    if not m: return False
    mon=m.group(1).lstrip('0')
    poss=[x.start() for x in re.finditer(r'(?<!\d)'+mon+'月',src)]
    if not poss: return False
    return all(RE_PAST_NEAR.search(src[max(0,p-WIN):p]) for p in poss)
def classify(title,rule,src):
    t=norm(title).strip(); s=norm(src); r=norm(rule)
    if t in CONCEPT_EXACT or RE_CONCEPT.search(t): return 'concept','暦の行事・まとめ記事で個別の開催日を持たない'
    if RE_CYCLE.search(s): return 'cycle','毎年開催ではない（隔年・数年に一度）'
    if _past_near(r,s):
        n='抽出元が過去の開催日を述べている'
        if RE_LUNAR.search(s): n=n+'（旧暦記述あり）'
        return 'past',n
    if RE_LUNAR.search(s): return 'lunar','旧暦基準のため新暦換算が必要'
    if RE_PERIOD.search(s): return 'review','期間限定・試験的な日程'
    if RE_CHANGED.search(s): return 'review','途中で開催日が変更された記述あり'
    if RE_RECENT.search(s) and not RE_SIG.search(s): return 'review','特定年の告知のみで毎年性の根拠なし'
    return 'ok',''
