import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q1046742",
        "slug_ja": "comiket",
        "slug_en": "comiket",
        "manual_content_ja": """## 概要

コミックマーケット(通称コミケ、Comiket)は、毎年夏(8月中旬)と冬(12月末)の年2回、東京都江東区有明の東京国際展示場(東京ビッグサイト)で開催される、世界最大規模の同人誌即売会です。1日あたり数十万人、3日間で延べ50〜60万人もの参加者が集う、日本のサブカルチャーを象徴するイベントとして国際的にも広く認知されています。

漫画・アニメ・ゲーム・小説・音楽など、ジャンルを問わない約3万のサークルが自主制作の作品を頒布し、企業ブースでも最新コンテンツのプロモーションが展開されます。参加者の多くがコスプレで会場を彩り、表現の自由と文化的多様性を体現する祝祭空間が形成されています。

## 歴史と由来

コミックマーケットの歴史は、1975年(昭和50年)12月21日に東京・虎ノ門の日本消防会館会議室で開催された第1回大会に遡ります。32サークル・推定700人という小規模なスタートでしたが、当時の漫画批評グループが「描き手と読み手が直接交流できる場」を目指して立ち上げました。

その後、1980年代の同人誌文化の急速な拡大とともに参加者が増加し、開催地は東京・晴海、千葉・幕張と移転を重ねながら規模を拡大。1996年(平成8年)の第50回大会以降、東京ビッグサイトを恒久会場として開催されるようになりました。

2019年(令和元年)の夏のコミケ(C96)では延べ73万人を動員し、2020年(令和2年)以降の新型コロナウイルス感染症の影響による中止・縮小開催を経て、現在も日本の文化イベントとして最大規模を維持し続けています。

主催はボランティアベースの非営利組織「コミックマーケット準備会」であり、表現の自由を守る場としての理念を50年以上にわたって貫いている点が、他のポップカルチャーイベントとの大きな違いです。

## 見どころ

**サークルスペース**
東京ビッグサイトの東ホール・西ホールを中心に、約3万の同人サークルが自主制作の同人誌・同人グッズを頒布します。プロ作家の自由制作から学生作家のデビュー作まで、商業流通には乗らない多様な作品に出会える唯一無二の場です。

**企業ブース**
ゲーム会社・出版社・アニメ制作会社など大手企業が出展し、限定グッズの先行販売や新作タイトルのプロモーションを展開。コミケ限定アイテムを求めて開場前から長蛇の列ができる定番の光景です。

**コスプレ広場**
東京ビッグサイト屋外スペースでは、参加者が自作衣装でキャラクターに扮するコスプレ広場が展開されます。写真撮影マナーや更衣室運用など、コミュニティで培われたルールに基づき秩序ある文化として運営されています。

**始発組と入場待機列**
開場前の早朝5時頃から「始発組」と呼ばれる参加者が長蛇の列を形成し、独自の文化を生み出しています。スタッフによる誘導と参加者の自律的協力により、数十万人規模でも安全に運営される点は世界的にも評価されています。

## 開催情報

- **開催地**: 東京都江東区有明 東京国際展示場(東京ビッグサイト)
- **開催時期**: 夏コミは毎年8月中旬の3日間、冬コミは毎年12月末の3日間(大晦日まで含む)
- **アクセス**: りんかい線「国際展示場駅」または「ゆりかもめ「東京ビッグサイト駅」から徒歩約3〜7分。JR新橋駅・大崎駅・東京駅から30分圏内
- **参加方法**: 一般参加は当日入場券(リストバンド)または事前購入チケット制。サークル参加は事前申込・抽選制
- **公式情報**: [コミックマーケット公式サイト](https://www.comiket.co.jp/)

## 周辺の見どころ

東京ビッグサイトのある臨海副都心エリア(お台場)は、現代東京を代表する観光地です。日本科学未来館、お台場海浜公園、ダイバーシティ東京プラザ、フジテレビ本社、レインボーブリッジといった観光スポットが徒歩・ゆりかもめ圏内に集積し、コミケ参加と組み合わせた東京観光が容易です。

東京駅・銀座エリアまでも20〜30分でアクセス可能で、コミケ後に秋葉原電気街・池袋サンシャインシティ・中野ブロードウェイといったポップカルチャー聖地を巡る周遊ルートも人気です。8月・12月いずれも東京の繁忙期にあたるため、宿泊予約は早めの確保が必須です。

## 関連情報

- 開催月: 8月中旬(夏)・12月末(冬)
- 都道府県: 東京都(関東)
- 起源: 1975年12月21日(第1回開催)
- 規模: 1回あたり延べ50〜60万人・サークル数約3万
- 主催: コミックマーケット準備会(非営利組織)
""",
        "manual_content_en": """## Overview

Comic Market (Comiket) is the world's largest doujinshi (self-published works) fair, held twice annually—in mid-August (Summer Comiket) and at the end of December (Winter Comiket)—at the Tokyo International Exhibition Center (Tokyo Big Sight) in Ariake, Koto Ward, Tokyo. Drawing several hundred thousand attendees per day and a cumulative 500,000 to 600,000 over three days, it stands as an iconic event symbolizing Japanese subculture and is internationally recognized.

Approximately 30,000 circles distribute self-published works spanning all genres—manga, anime, games, novels, and music—while corporate booths showcase the latest content promotions. Many participants don cosplay, embodying a festive space that celebrates freedom of expression and cultural diversity.

## History and Origins

Comic Market traces its origins to December 21, 1975, when the first edition was held in a meeting room at the Japan Fire Defense Hall in Toranomon, Tokyo. Starting modestly with 32 circles and an estimated 700 participants, the event was launched by a manga critique group with the aim of creating a venue where creators and readers could interact directly.

As doujinshi culture expanded rapidly through the 1980s, the number of participants grew accordingly. The venue relocated through Harumi in Tokyo and Makuhari in Chiba while scaling up. Since the 50th edition in 1996, Tokyo Big Sight has served as the permanent venue.

The Summer Comiket of 2019 (C96) attracted a cumulative attendance of 730,000. After cancellations and downsized editions due to the COVID-19 pandemic from 2020 onward, Comiket continues to maintain its position as the largest cultural event in Japan.

The organizer is the volunteer-based, non-profit "Comic Market Preparatory Committee." Its commitment to protecting freedom of expression as a guiding principle for over fifty years sets it apart from other pop culture events.

## Highlights

**Circle Spaces**
Approximately 30,000 doujin circles distribute self-published doujinshi and merchandise primarily across the East and West Halls of Tokyo Big Sight. From freely created works by professional authors to debut pieces by student creators, the venue offers a unique opportunity to encounter diverse works that never enter commercial distribution.

**Corporate Booths**
Major game companies, publishers, and anime production studios exhibit limited-edition merchandise and promote upcoming titles. Long queues forming before the doors open in search of Comiket-exclusive items have become a familiar scene.

**Cosplay Plaza**
In the outdoor spaces of Tokyo Big Sight, participants in self-made costumes embodying their favorite characters gather in the Cosplay Plaza. Photography etiquette and changing room protocols, refined through years of community practice, sustain this culture as an orderly tradition.

**Pre-Dawn Queues**
From around 5 AM before opening, dedicated participants known as the "first train group" form extensive queues, creating their own subculture. The combination of staff guidance and participant cooperation enables safe operations at scales of hundreds of thousands, an achievement recognized globally.

## Event Information

- **Location**: Tokyo International Exhibition Center (Tokyo Big Sight), Ariake, Koto Ward, Tokyo
- **Period**: Summer Comiket: three days in mid-August; Winter Comiket: three days at the end of December (including New Year's Eve)
- **Access**: Approximately 3–7 minutes on foot from Kokusai-tenjijo Station (Rinkai Line) or Tokyo Big Sight Station (Yurikamome Line). Within 30 minutes from JR Shimbashi, Osaki, and Tokyo Stations
- **Participation**: General attendance requires same-day entry wristbands or advance purchase tickets. Circle participation is by advance application and lottery
- **Official Information**: [Comic Market Official Website](https://www.comiket.co.jp/)

## Nearby Attractions

The Tokyo Bay Area (Odaiba), where Tokyo Big Sight is located, is one of contemporary Tokyo's representative tourist districts. Attractions including the National Museum of Emerging Science and Innovation, Odaiba Seaside Park, DiverCity Tokyo Plaza, Fuji TV Headquarters, and Rainbow Bridge are clustered within walking distance or a short ride on the Yurikamome, making it easy to combine Comiket attendance with Tokyo sightseeing.

Tokyo Station and Ginza are accessible within 20–30 minutes, and many visitors enjoy circuits combining Comiket with pop culture pilgrimages to Akihabara Electric Town, Ikebukuro Sunshine City, or Nakano Broadway. Since both August and December are peak tourism seasons in Tokyo, early accommodation booking is essential.

## Related Information

- Season: Mid-August (Summer) / Late December (Winter)
- Prefecture: Tokyo (Kanto Region)
- Origin: December 21, 1975 (First edition)
- Scale: 500,000–600,000 cumulative attendance per event; approximately 30,000 circles
- Organizer: Comic Market Preparatory Committee (non-profit organization)
""",
    },
    {
        "qid": "Q11265785",
        "slug_ja": "guzuyaki-festival",
        "slug_en": "guzuyaki-festival",
        "manual_content_ja": """## 概要

ぐず焼き祭りは、富山県魚津市で毎年8月に開催される、夏の終わりを告げる伝統的な民俗行事です。「ぐず」と呼ばれる魚(ハゼ科の魚の地方名)を模した竹と藁の巨大な張り子を市内で曳き回し、最後に焼き払うという、北陸地方独自の火の祭りです。

魚津漁港と諏訪神社を中心に展開される祭りは、漁業の安全と豊漁を祈願する地域信仰と、夏の災厄を火によって祓い清める日本古来の精霊送り信仰が結びついた独特の形式を持っています。地元住民と漁業従事者にとっては、ふるさとの夏の終わりを彩る欠かせない行事として親しまれています。

## 歴史と由来

ぐず焼き祭りの起源は、魚津の漁業文化と密接に結びついた地域信仰に遡ります。富山湾は古くから豊かな漁場として知られ、特に夏のハゼ漁・キス漁は地域経済を支える重要な営みでした。漁業従事者たちは、海への感謝と航海安全を願う一方で、夏の盛りに発生する疫病や災厄を「ぐず」に託して焼き払うという信仰行為を続けてきました。

「ぐず」という呼称は、富山湾沿岸でハゼ科の魚を指す方言です。この魚を模した張り子を作り、町内を練り歩いた後に火にかけて焼き払う行為は、稲作地帯の「虫送り」や「精霊送り」と類似する原理を持ち、共同体の災厄を象徴的な対象物に転移させて浄化する民俗的儀礼として位置づけられます。

現在では、地元の自治会・商店街・漁業関係者が連携して実行委員会を組織し、伝統行事を守りつつ観光客にも開かれた地域の夏祭りとして毎年継承されています。

## 見どころ

**「ぐず」の張り子作りと町内巡行**
祭りの数日前から、地元の有志が竹と藁で「ぐず」の張り子を制作します。全長数メートルにも及ぶ巨大な魚の張り子が、太鼓と笛の囃子に合わせて市内を巡行する光景は、北陸の港町ならではの素朴で力強い情景です。

**諏訪神社での神事**
祭りの中心となる諏訪神社では、神職による厳かな神事が執り行われ、漁業安全と豊漁が祈願されます。地域信仰の核として、世代を超えて受け継がれる神聖な場面です。

**「ぐず」焚き上げ**
祭りのクライマックスは、町内を巡行した「ぐず」の張り子を広場で焼き払う儀式です。炎の中に消えていく魚の姿は、夏の災厄や穢れを共同体から送り出す象徴であり、参加者は手を合わせて祭りの終わりを見届けます。

**地元グルメと夜店**
祭り会場周辺では、富山湾の海の幸を活かした地元グルメや夜店が出店し、地域住民と観光客が交流する賑やかな祝祭空間が形成されます。

## 開催情報

- **開催地**: 富山県魚津市内および諏訪神社周辺
- **開催時期**: 毎年8月(具体的な日程は年により異なる)
- **アクセス**: あいの風とやま鉄道「魚津駅」から徒歩約10分。北陸自動車道「魚津IC」から車で約10分
- **観覧料**: 無料
- **公式情報**: [魚津市観光案内サイト](https://uozu-kanko.jp/)

## 周辺の見どころ

魚津市は富山湾の中央に位置し、「蜃気楼」「ホタルイカ」「埋没林」の3つの神秘として知られる観光資源を持ちます。魚津埋没林博物館では、約2,000年前の杉の原生林が海中から発掘された世界的にも珍しい遺構を見学でき、魚津水族館では富山湾の多様な海洋生物を観察できます。

近隣の黒部市・宇奈月温泉までは車で30分圏内で、立山黒部アルペンルートの観光と組み合わせた周遊旅行が人気です。8月の魚津は富山湾の海風が心地よく、海産物と温泉、伝統行事を一度に楽しめる北陸観光の好シーズンです。

## 関連情報

- 開催月: 8月(夏)
- 都道府県: 富山県(北陸)
- 起源: 漁業文化と精霊送り信仰の融合(具体的な始期は不詳)
- 性格: 民俗行事・火祭り・漁業安全祈願
- 関連: 諏訪神社の神事
""",
        "manual_content_en": """## Overview

The Guzuyaki Festival (Guzu-yaki Matsuri) is a traditional folk event marking the end of summer, held annually in August in Uozu City, Toyama Prefecture. A giant effigy of a fish called "guzu" (a regional name for goby-family fish) made of bamboo and straw is paraded through the city before being ceremonially burned at the festival's climax, making it a distinctive fire festival unique to the Hokuriku region.

Centered on Uozu Fishing Port and Suwa Shrine, the festival uniquely combines local beliefs praying for fishing safety and bountiful catches with the ancient Japanese tradition of spirit-sending, which purifies summer misfortunes through fire. For local residents and fishermen, it remains an indispensable event coloring the end of summer in their hometown.

## History and Origins

The origins of the Guzuyaki Festival trace back to local beliefs intimately tied to Uozu's fishing culture. Toyama Bay has long been renowned as a rich fishing ground, with summer goby and sillago fisheries supporting the regional economy. Fishermen expressed gratitude to the sea and prayed for navigational safety while also continuing the ritual practice of burning a "guzu" effigy to ward off plagues and misfortunes that arise during the height of summer.

The term "guzu" is a dialect word along the Toyama Bay coast referring to goby-family fish. Crafting an effigy of this fish, parading it through neighborhoods, and then burning it follows the same logic as the "insect-sending" and "spirit-sending" rituals of rice-cultivating regions. It functions as a folk ritual transferring communal misfortunes onto a symbolic object for purification.

Today, local neighborhood associations, merchants' associations, and fishing industry stakeholders cooperate to organize an executive committee that preserves the traditional event while opening it to tourists as an annual summer festival of the region.

## Highlights

**Crafting and Procession of the "Guzu" Effigy**
For several days before the festival, local volunteers craft the "guzu" effigy from bamboo and straw. The sight of a giant fish effigy several meters long parading through the city to the rhythm of drums and flutes is a rustic and powerful scene unique to a Hokuriku port town.

**Suwa Shrine Ritual**
At Suwa Shrine, the festival's spiritual core, Shinto priests conduct solemn rituals praying for fishing safety and bountiful catches. As the heart of local belief, it represents a sacred moment passed down across generations.

**Burning of the "Guzu"**
The climax is the ceremony of burning the "guzu" effigy in an open square after its procession through town. The fish disappearing into the flames symbolizes the communal sending-off of summer misfortunes and impurities. Participants press their palms together to witness the festival's conclusion.

**Local Cuisine and Night Stalls**
Around the festival grounds, food stalls offering local cuisine made with seafood from Toyama Bay create a lively festive space where residents and tourists interact.

## Event Information

- **Location**: Within Uozu City and around Suwa Shrine, Toyama Prefecture
- **Period**: Annually in August (specific dates vary by year)
- **Access**: Approximately 10 minutes on foot from Uozu Station (Ainokaze Toyama Railway). Approximately 10 minutes by car from the Uozu IC on the Hokuriku Expressway
- **Admission**: Free
- **Official Information**: [Uozu City Tourism Guide](https://uozu-kanko.jp/)

## Nearby Attractions

Uozu City lies at the center of Toyama Bay and is known for its three mysteries: mirages (shinkiro), firefly squid (hotaruika), and submerged forest (maibotsurin). The Uozu Buried Forest Museum exhibits a world-rare archaeological site where a 2,000-year-old cedar forest was excavated from the sea, while the Uozu Aquarium offers observation of the diverse marine life of Toyama Bay.

Kurobe City and Unazuki Onsen lie within 30 minutes by car, making circuits combining the Tateyama Kurobe Alpine Route popular. August in Uozu brings pleasant sea breezes from Toyama Bay, offering an ideal Hokuriku tourism season to enjoy seafood, hot springs, and traditional events together.

## Related Information

- Season: August (Summer)
- Prefecture: Toyama (Hokuriku Region)
- Origin: Fusion of fishing culture and spirit-sending beliefs (specific origin date unknown)
- Character: Folk event, fire festival, prayer for fishing safety
- Related: Suwa Shrine rituals
""",
    },
    {
        "qid": "Q11285021",
        "slug_ja": "odate-amekko-ichi",
        "slug_en": "odate-amekko-ichi",
        "manual_content_ja": """## 概要

大館アメッコ市(おおだてアメッコいち)は、毎年2月の第2土曜日とその翌日の日曜日の2日間、秋田県大館市の中心市街地「おおまちハチ公通り」で開催される、400年以上の歴史を持つ冬の伝統民俗行事です。「この日にアメを食べると風邪をひかない」という言い伝えとともに、地元住民から観光客まで幅広く愛されてきました。

色とりどりの飴を販売する屋台が通りに数十軒並び、ミズキの枝にカラフルな飴を結わえつけた縁起物が会場を彩る光景は、雪深い東北の冬を華やかに演出する風物詩です。秋田犬パレードや白ひげ大神巡行など、大館ならではの催しも見どころとなっています。

## 歴史と由来

大館アメッコ市の起源は、天正16年(1588年)頃と伝えられ、約400年の歴史を誇る東北地方屈指の民俗行事です。古来、赤みのあるミズキの枝に飴を付け、稲穂代わりに神前に供えたことから始まったとされ、五穀豊穣と無病息災を祈る農耕文化と結びついた信仰行事が原型となっています。

「2月の第2土曜日に近隣の山々から神様がアメを買いに降りてくる」という伝承が地域に根づき、白い髭を蓄えた山の神「白ひげ大神」が市中を巡行する儀式が祭りの中核として継承されてきました。当初は地元の民俗行事として小規模に行われていましたが、昭和47年(1972年)から現在の「おおまちハチ公通り」を会場として大規模化し、観光客にも開かれた現代的な祭りへと発展しています。

大館は秋田犬の原産地として国際的にも知られており、平成年間以降は秋田犬パレードが組み込まれ、伝統行事と地域ブランディングを融合した独自の祭りとして全国的な知名度を獲得しました。

## 見どころ

**飴屋台の連なり**
おおまちハチ公通りには、地元菓子店や和菓子職人による飴屋台が数十軒並びます。色とりどりの伝統飴、現代的なアレンジを加えた創作飴、ミズキの枝に飴を結わえた縁起物など、見て楽しく食べて美味しい多彩な飴文化を体験できます。

**白ひげ大神の巡行**
山から飴を買いに降りてきた神様を再現する「白ひげ大神」の巡行は、祭りの神秘的なハイライトです。白い髭を蓄え、伝統衣装をまとった神が市中を練り歩く姿は、400年続く信仰の生きた姿を感じさせます。

**秋田犬パレード**
大館が原産地である秋田犬たちが、飼い主と共に通りを練り歩くパレードは祭りのもう一つの目玉です。海外からの観光客にも人気が高く、秋田犬と触れ合える貴重な機会として注目されています。

**ミズキ飾りと縁起物**
祭りのフィナーレでは、大きなミズキの枝に色とりどりの飴をたっぷりと飾った巨大な縁起物が登場します。家庭に持ち帰って一年の無病息災を祈る習慣も残っており、地域の祈りの形が可視化される瞬間です。

## 開催情報

- **開催地**: 秋田県大館市 おおまちハチ公通り
- **開催時期**: 毎年2月の第2土曜日とその翌日の日曜日の2日間
- **アクセス**: JR奥羽本線「大館駅」からバスで約10分、「大町」バス停下車すぐ。秋田自動車道「大館北IC」から車で約10分
- **観覧料**: 無料
- **公式情報**: [大館市公式観光サイト](https://www.city.odate.lg.jp/city/kankou/festibal/festa/winter/amekko)

## 周辺の見どころ

大館市は秋田犬発祥の地として、秋田犬の里(秋田犬展示・観光案内施設)が市内中心部に位置します。忠犬ハチ公の故郷でもあり、ハチ公にまつわる史跡や記念施設も点在しています。

近隣の鹿角市・小坂町までは車で30〜40分圏内で、世界遺産・大湯環状列石(ストーンサークル)、小坂鉱山史跡群、十和田湖といった東北北部の代表的観光地と組み合わせた周遊旅行が可能です。2月の大館は深い雪に覆われ、温泉郷の田代岱・大滝温泉などで雪見露天風呂を楽しめる時期でもあります。

## 関連情報

- 開催月: 2月(冬)
- 都道府県: 秋田県(東北)
- 起源: 天正16年(1588年)頃・約400年の歴史
- 性格: 民俗行事・農耕信仰・無病息災祈願
- 関連: 秋田犬発祥の地・忠犬ハチ公の故郷
""",
        "manual_content_en": """## Overview

The Odate Amekko-ichi (Odate Candy Fair) is a winter folk event with over 400 years of history, held annually on the second Saturday of February and the following Sunday along Omachi Hachiko Street in central Odate City, Akita Prefecture. Accompanied by the saying "those who eat candy on this day will not catch a cold," the festival has been beloved by local residents and tourists alike.

Dozens of stalls selling colorful candies line the street, while charms made by tying vibrant candies onto branches of Japanese dogwood (mizuki) decorate the venue, painting a vivid winter scene in the snow-covered Tohoku region. Unique features such as the Akita dog parade and the procession of Shirohige Okami (the White-Bearded Mountain God) further enhance the festival's appeal.

## History and Origins

The Odate Amekko-ichi is said to have originated around 1588 (Tensho 16) and boasts approximately 400 years of history, making it one of the most prominent folk events in the Tohoku region. It is believed to have begun with the practice of attaching candies to reddish dogwood branches and offering them to deities in place of rice ears, rooted in agricultural beliefs praying for bountiful harvests and good health.

The local legend that "mountain gods descend from the surrounding peaks on the second Saturday of February to buy candies" has taken root in the community, and the procession of Shirohige Okami—a deity with a long white beard representing the mountain god—has been preserved as the festival's core ritual. Originally held on a small scale as a local folk event, the festival expanded significantly from 1972 (Showa 47) when Omachi Hachiko Street became the venue, evolving into a modern festival open to tourists.

Odate is internationally known as the birthplace of the Akita dog breed, and since the Heisei era, the Akita dog parade has been incorporated into the festival, achieving nationwide recognition as a unique event blending traditional ritual with regional branding.

## Highlights

**Rows of Candy Stalls**
Dozens of candy stalls operated by local confectioners and traditional Japanese sweet artisans line Omachi Hachiko Street. Visitors can experience a rich candy culture featuring colorful traditional candies, creative modern variations, and dogwood-branch charms decorated with sweets—a feast for both eyes and palate.

**Procession of Shirohige Okami**
The procession of Shirohige Okami, reenacting the mountain god descending to buy candy, is the festival's mystical highlight. The figure with a long white beard in traditional attire parading through the streets evokes the living presence of 400 years of belief.

**Akita Dog Parade**
A parade of Akita dogs—the breed originating from this region—walking the streets with their owners is another centerpiece of the festival. Highly popular among international visitors, it draws attention as a rare opportunity to interact with Akita dogs.

**Dogwood Decorations and Charms**
At the festival's finale, large dogwood branches lavishly decorated with multicolored candies appear as oversized lucky charms. Visitors take these home as part of a tradition praying for a year of good health, making the festival's communal prayers visible.

## Event Information

- **Location**: Omachi Hachiko Street, Odate City, Akita Prefecture
- **Period**: The second Saturday of February and the following Sunday, annually
- **Access**: Approximately 10 minutes by bus from Odate Station (JR Ou Main Line), alighting at Omachi bus stop. Approximately 10 minutes by car from Odate Kita IC on the Akita Expressway
- **Admission**: Free
- **Official Information**: [Odate City Official Tourism Site](https://www.city.odate.lg.jp/city/kankou/festibal/festa/winter/amekko)

## Nearby Attractions

As the birthplace of the Akita dog, Odate City hosts the Akita Inu no Sato (an exhibition and tourist information facility dedicated to the breed) in its central district. It is also the hometown of the loyal dog Hachiko, with related historical sites and memorial facilities scattered throughout the city.

Neighboring Kazuno City and Kosaka Town lie within 30–40 minutes by car, allowing tourists to combine visits with northern Tohoku attractions such as the UNESCO World Heritage Oyu Stone Circles, the Kosaka Mine historical sites, and Lake Towada. February in Odate is deeply covered in snow, offering opportunities to enjoy outdoor hot springs amid snowy scenery at Tashirodai and Otaki Onsen.

## Related Information

- Season: February (Winter)
- Prefecture: Akita (Tohoku Region)
- Origin: Around 1588 (Tensho 16), approximately 400 years of history
- Character: Folk event, agricultural belief, prayer for good health
- Related: Birthplace of the Akita dog breed, hometown of the loyal dog Hachiko
""",
    },
    {
        "qid": "Q11301756",
        "slug_ja": "game-market",
        "slug_en": "game-market",
        "manual_content_ja": """## 概要

ゲームマーケットは、ボードゲーム・カードゲーム・テーブルトークRPGなど「電源不要ゲーム」のみを対象とした、日本最大規模のアナログゲーム展示即売会です。東京では毎年春(5月頃)と秋(11月頃)の年2回、近年は幕張メッセを会場として開催され、2万人を超える参加者が訪れます。大阪でも年1回開催され、西日本のアナログゲームファンの拠点となっています。

国内外のボードゲームメーカー・同人サークル・個人クリエイターが新作タイトルを発表・販売する場であり、購入したゲームをその場で試遊できるエリアも併設されています。アナログゲーム文化の成長を象徴するイベントとして、業界関係者・ヘビーユーザー・初心者まで幅広い層が集う祭典です。

## 歴史と由来

ゲームマーケットの第1回開催は、2000年(平成12年)4月2日に東京都内の小規模会場でスタートしました。創設者は当時の日本アナログゲーム愛好家コミュニティで、海外発のドイツボードゲーム(ユーロゲーム)が日本で本格普及し始めた時期と重なり、「ボードゲーム専用の即売会」というニッチな着想が時代の波に乗りました。

当初は60ブース程度・参加者数百名の小規模イベントでしたが、2000年代後半からの世界的なボードゲームブームに乗り、出展サークルと来場者数が年々増加。2010年代には東京ビッグサイト、その後さらに大規模化して幕張メッセへと会場を拡大し、2020年代には来場者2万人を超える日本最大級のアナログゲームイベントへと成長しました。

2013年(平成25年)からは大阪開催も始まり、ゲームマーケット初の地方開催として85ブース・予想を超える反響を呼びました。現在は東京春・東京秋・大阪の年3回開催体制が定着し、アナログゲーム文化の全国的な普及拠点として機能しています。

主催はアークライト株式会社で、商業出版社・同人クリエイター・海外メーカーの三者が対等に参加できる場として運営されている点が、他のホビーイベントとの大きな違いです。

## 見どころ

**新作ボードゲームの発表と頒布**
国内のアナログゲームメーカー・同人サークル数百団体が、新作タイトルを発表・販売します。商業流通に乗る前の同人作品から、海外で評価を受けたタイトルの日本語版まで、ボードゲームファンにとっては年に数回しかない貴重な購入機会です。

**試遊コーナー**
購入を検討しているゲームをその場で実際にプレイできる試遊エリアが充実しています。ルールの分かりやすさ、プレイ時間、戦略性などを体感した上で購入できるため、初心者にも優しい設計です。

**海外メーカーブースとパブリッシャー商談**
近年は海外のボードゲームパブリッシャーやデザイナーも出展し、国際的なライセンス商談の場としても機能しています。日本市場への参入を狙う海外メーカーにとって重要な拠点となっています。

**TRPG・パーティゲーム体験会**
テーブルトークRPGのセッション体験会、パーティゲームの大会、ゲームデザイナーによるトークイベントなど、購入以外の体験プログラムも充実しており、コミュニティの交流が深まります。

## 開催情報

- **開催地**: 東京開催=幕張メッセ展示ホール(千葉県千葉市美浜区)、大阪開催=大阪ATCホール(大阪府大阪市住之江区)
- **開催時期**: 東京春は毎年5月頃の土日2日間、東京秋は毎年11月頃の土日2日間、大阪は年1回
- **アクセス**: 幕張メッセはJR京葉線「海浜幕張駅」から徒歩約5分。大阪ATCホールはニュートラム「トレードセンター前駅」から徒歩約2分
- **入場料**: 当日券1,500円程度、前売券1,000円程度(年により変動)
- **公式情報**: [ゲームマーケット公式サイト](https://gamemarket.jp/)

## 周辺の見どころ

幕張メッセのある千葉市美浜区(幕張新都心)は、東京湾岸の現代的な都市開発エリアです。幕張海浜公園、三井アウトレットパーク幕張、イオンモール幕張新都心など、ショッピングとレジャーが楽しめる施設が徒歩圏内に集まっています。東京ディズニーリゾートまでも電車で30分圏内のため、家族連れでの周遊旅行も人気です。

大阪ATCホール周辺は大阪南港の臨海エリアで、海遊館、天保山、ユニバーサル・スタジオ・ジャパンといった大阪を代表する観光地と組み合わせた旅程が組みやすいロケーションです。5月・11月いずれも気候が穏やかで、屋内イベントと観光を組み合わせた快適な旅程が可能なシーズンです。

## 関連情報

- 開催月: 5月(春)・11月(秋)・大阪開催は年1回
- 都道府県: 千葉県(関東)・大阪府(近畿)
- 起源: 2000年4月2日(第1回開催)
- 規模: 来場者2万人超・出展数百ブース
- 主催: アークライト株式会社
""",
        "manual_content_en": """## Overview

Game Market is Japan's largest analog game exhibition and sales event, dedicated exclusively to "power-free games" such as board games, card games, and tabletop role-playing games. The Tokyo editions are held twice a year, in spring (around May) and autumn (around November), with Makuhari Messe serving as the venue in recent years, drawing over 20,000 visitors. An additional Osaka edition is held annually, serving as a hub for analog game fans in western Japan.

Domestic and international board game publishers, doujin circles, and individual creators announce and sell new titles, with adjacent play-test areas where purchased games can be tried on the spot. As an event symbolizing the growth of analog gaming culture in Japan, it attracts a broad audience ranging from industry professionals and dedicated enthusiasts to newcomers.

## History and Origins

The first Game Market was held on April 2, 2000, at a small venue in Tokyo. Founded by the Japanese analog game enthusiast community of the time, it coincided with the period when German-style board games (Eurogames) began to gain serious popularity in Japan. The niche concept of a "board game-exclusive sales event" perfectly rode the wave of the times.

Initially a small-scale event with around 60 booths and several hundred participants, Game Market grew steadily through the late 2000s global board game boom, with the number of exhibiting circles and attendees increasing each year. In the 2010s, the venue moved to Tokyo Big Sight and later expanded further to Makuhari Messe, growing in the 2020s into Japan's largest analog game event with over 20,000 attendees.

The Osaka edition launched in 2013 as the festival's first regional expansion, with 85 booths and a stronger-than-expected response. The current three-edition annual cycle (Tokyo Spring, Tokyo Autumn, Osaka) has become well-established, functioning as a nationwide hub for analog game culture.

Organized by Arclight Inc., the event distinguishes itself from other hobby events by providing a venue where commercial publishers, doujin creators, and overseas manufacturers participate on equal footing.

## Highlights

**Announcement and Distribution of New Board Games**
Hundreds of domestic analog game publishers and doujin circles announce and sell new titles. From doujin works yet to enter commercial distribution to Japanese-language editions of titles acclaimed overseas, the event offers board game fans rare purchasing opportunities available only a few times a year.

**Play-Test Corners**
Extensive play-test areas allow visitors to actually try games they are considering buying. The ability to experience rule clarity, playtime, and strategic depth before purchase makes the event newcomer-friendly.

**Overseas Publisher Booths and Licensing Negotiations**
In recent years, overseas board game publishers and designers have also exhibited, with the event functioning as a venue for international licensing negotiations. It has become an important hub for overseas manufacturers seeking entry into the Japanese market.

**TRPG and Party Game Experience Sessions**
Beyond purchasing, the event offers tabletop RPG session experiences, party game tournaments, and talk events by game designers, deepening community engagement.

## Event Information

- **Location**: Tokyo editions: Makuhari Messe Exhibition Hall, Mihama-ku, Chiba City, Chiba Prefecture. Osaka edition: Osaka ATC Hall, Suminoe-ku, Osaka City
- **Period**: Tokyo Spring: two days in May; Tokyo Autumn: two days in November; Osaka: once a year
- **Access**: Makuhari Messe is approximately 5 minutes on foot from Kaihin-Makuhari Station (JR Keiyo Line). Osaka ATC Hall is approximately 2 minutes on foot from Trade Center-mae Station (New Tram)
- **Admission**: Approximately JPY 1,500 same-day tickets, JPY 1,000 advance tickets (varies by year)
- **Official Information**: [Game Market Official Website](https://gamemarket.jp/)

## Nearby Attractions

Makuhari Shintoshin in Mihama-ku, Chiba City, where Makuhari Messe is located, is a modern urban development area along Tokyo Bay. Facilities such as Makuhari Seaside Park, Mitsui Outlet Park Makuhari, and AEON Mall Makuhari Shintoshin offering shopping and leisure are clustered within walking distance. Tokyo Disney Resort is also within 30 minutes by train, making it popular for family circuits.

The area around Osaka ATC Hall lies in the Osaka South Port waterfront district, with easy access to representative Osaka attractions such as the Osaka Aquarium Kaiyukan, Tempozan, and Universal Studios Japan. Both May and November feature mild climates, making it a comfortable season to combine indoor events with sightseeing.

## Related Information

- Season: May (Spring) / November (Autumn) / Osaka annually
- Prefecture: Chiba (Kanto Region) / Osaka (Kinki Region)
- Origin: April 2, 2000 (First edition)
- Scale: Over 20,000 attendees, hundreds of exhibitor booths
- Organizer: Arclight Inc.
""",
    },
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

for item in ITEMS:
    cur.execute("""
        UPDATE festivals
        SET manual_content_ja = ?,
            manual_content_en = ?,
            slug_ja = ?,
            slug_en = ?,
            status = 'drafted'
        WHERE qid = ?
    """, (
        item["manual_content_ja"],
        item["manual_content_en"],
        item["slug_ja"],
        item["slug_en"],
        item["qid"],
    ))
    print(f"[OK] {item['qid']}: {item['slug_ja']} updated to drafted")

conn.commit()

for item in ITEMS:
    cur.execute("SELECT qid, label_ja, slug_ja, status, LENGTH(manual_content_ja), LENGTH(manual_content_en) FROM festivals WHERE qid = ?", (item["qid"],))
    row = cur.fetchone()
    print(f"[VERIFY] {row}")

conn.close()
