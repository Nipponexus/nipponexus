"""nxfix_en : 訂正記録の日本語平文を英訳する対訳表。
nxfix.humanize が出す定型文と1対1で対応させる。未知の文は None を返し、
呼び出し側で英語行を出さない（誤訳を出すより落とすほうが安全）。"""

KIND_EN = {
    "所在地の訂正": "Location corrections",
    "所在地の補完": "Location added",
    "名称の照合": "Name verification",
    "開催日の訂正": "Date corrections",
    "掲載見送り": "Withheld from publication",
}

NOTE_EN = {
    '根拠文の「11月17日〜11月4日」を「N日間」の記述から訂正':
        'The source gave the range "17 November to 4 November", which is inconsistent; the end date was corrected using the number of days stated in the article.',
    '根拠文が現行日を7月14日と明記。古い6月の日付を採用していた':
        'The article states that the festival is now held on July 14; the earlier value used an outdated June date.',
    '根拠文が2018年より8月11日へ変更と明記':
        'The article states that the date was changed to August 11 in 2018.',
    "記事の本文から一意に特定":
        "Identified unambiguously from the article text.",
    "記事冒頭の記述とウィキデータの二経路で所在地を確認。旧来の値は祭りの名称から推測された誤り":
        "Location confirmed via two independent routes: the opening passage of the article and Wikidata. "
        "The earlier value was an error inferred from the festival's name.",
    "記事冒頭に郡を含む住所が記されているため、郡名を除いた自治体名で照合し、その自治体が属する県を確認":
        "The article's opening gives an address including the district (gun); we matched on the municipality "
        "name with the district removed and confirmed the prefecture that municipality belongs to.",
    "暦の行事・まとめ記事で個別の開催日を持たない":
        "A calendrical observance or overview article with no single date of its own.",
    "毎年開催ではない（隔年・数年に一度）":
        "Not held every year (biennial or once every few years).",
    "記念日であり祭りではない":
        "A commemorative day, not a festival.",
    "抽出元が過去の開催日を述べている（旧暦記述あり）":
        "The source passage describes a past date (stated on the lunar calendar).",
    "抽出元が過去の開催日を述べている":
        "The source passage describes a past date.",
    "人物の所属先を示す表記のため、正式表記に統一":
        "The wording indicates a person's affiliation, so the official romanisation is used.",
    "同一文中の他の寺社が正式表記のため、表記を統一":
        "Other temples and shrines in the same sentence use the official romanisation, so it was made consistent.",
    "盆の風習の総称であり個別の祭りではない":
        "A general term for Bon customs rather than a specific festival.",
    "祭りの参加団体（流）であり祭りではない":
        "A participating group (nagare) within a festival, not a festival itself.",
    "記事内容がえびす講（年中行事の総称）でラベルと不一致":
        "The article covers Ebisu-ko, a general annual observance, which does not match the label.",
    "地域一帯の火祭りの総称で開催日が一定でない":
        "A collective term for fire festivals across a region, with no fixed date.",
    "期間限定・試験的な日程":
        "A limited-run or trial schedule.",
    "特定年の告知のみで毎年性の根拠なし":
        "Only an announcement for a specific year; no evidence that it recurs annually.",
    "途中で開催日が変更された記述あり":
        "The article notes that the date was changed at some point.",
}

_PREFIX = [
    ("根拠文の「", "Corrected from the source passage: "),
    ("根拠文が", "The source passage states: "),
]

def note_en(ja):
    """既知の定型文のみ英訳する。未知の文は None を返し、呼び出し側で英語行を出さない。
    前置きだけを付けて日本語本文を残す旧フォールバックは日本語混入を生んだため撤去した。"""
    return NOTE_EN.get((ja or "").strip())

def kind_en(ja):
    return KIND_EN.get(ja, ja)
