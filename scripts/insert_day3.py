#!/usr/bin/env python3
"""Insert festivals #31-40 (Phase 1c day 3):
Q125959947 荒処の沼入り梵天 / Q127789312 小金井桜まつり /
Q1636567 神戸ルミナリエ / Q17226795 佐那神社 / Q1749262 博多祇園山笠 /
Q21653325 水郷佐原あやめ祭り / Q22120521 三宅神社 /
Q24887619 入谷朝顔まつり / Q30924149 豊年祭(田縣神社) / Q30925534 伊甘神社"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q125959947",
        "slug_ja": "arasho-no-numairi-bonden",
        "slug_en": "arasho-no-numairi-bonden",
        "manual_content_ja": """## 概要

荒処の沼入り梵天（あらどころのぬまいりぼんでん）は、秋田県横手市平鹿町下鞭（しもむち）の荒処地区で毎年2月に行われる小正月の伝統行事である。氏子たちが「梵天（ぼんでん）」と呼ばれる五穀豊穣・無病息災の祈りを込めた依り代を担ぎ、極寒の沼に飛び込んで奉納する勇壮な雪国の祭礼として知られる。

## 歴史

梵天奉納行事は秋田県内陸部に古くから伝わる小正月の風習で、五穀豊穣・家内安全・地域繁栄を祈念する依り代を山の神・水神に捧げる神事である。荒処の沼入り梵天はその中でも特に過酷な形態を持ち、厳冬期に氷の張った沼へ褌姿の若者が梵天を担いだまま入水する点に特徴がある。起源は江戸期にまで遡るとされ、農耕と狩猟の境界地域で水神信仰と山神信仰が融合して成立した民俗行事として、地域住民に脈々と継承されてきた。横手市域の数ある梵天行事の中でも稀少な水神奉納型として民俗学的価値が高い。

## 見どころ

氷点下の沼に褌姿の男衆が梵天を担いで飛び込む光景は圧巻で、白い息と雪原の中に映える鮮やかな梵天の彩りが幻想的な対比を生む。氏子の若衆たちは事前に酒や火で身体を温め、勢いをつけて沼に飛び込む。沼入りの後は岸辺の祭壇で神事が執り行われ、参拝者には甘酒や餅が振る舞われる。横手地方の冬の風物詩として地元の温かな雰囲気が漂う。

## 開催情報・アクセス

会場は秋田県横手市平鹿町下鞭の荒処地区。JR奥羽本線横手駅から車で約20分。例年2月中旬の小正月時期に開催される。観覧は無料だが、防寒対策と長靴が必須。

## 周辺観光

横手市内には日本三大雪まつりの一つ「横手の雪まつり（かまくら）」、増田町の伝統的建造物群保存地区、後三年合戦金沢資料館、横手城址などの観光資源が集中する。冬季は稲庭うどんの里、横手やきそば、地酒の蔵元巡りなど、秋田南部の食と文化を堪能できる。""",
        "manual_content_en": """## Overview

Arasho no Numairi Bonden (Arasho Swamp-Entering Bonden Ritual) is a traditional Koshōgatsu (Little New Year) ceremony held each February in the Arasho district of Shimomuchi, Hiraka-machi, Yokote City, Akita Prefecture. Parishioners shoulder sacred "bonden" effigies—divine vessels embodying prayers for bountiful harvests and protection from illness—and plunge into the freezing winter swamp to make their offering, creating one of the most striking ceremonies of snow-country Japan.

## History

Bonden offering rites are ancient Little New Year customs widely preserved across the inland regions of Akita Prefecture, in which sacred effigies symbolizing prayers for bountiful harvests, family safety, and community prosperity are dedicated to mountain deities and water deities. Among the many bonden traditions, the Arasho Swamp-Entering Bonden stands out for its especially severe form, requiring young men in loincloths to enter a frozen swamp while still carrying their bonden in the depths of winter. The ritual's origins are believed to reach back to the Edo period, having developed in a borderland between agriculture and hunting cultures where worship of water deities and mountain deities fused into a single folk ceremony. It has been continuously transmitted by local residents ever since. Within the many bonden ceremonies of the Yokote region, it holds significant value as a rare swamp-offering variant from the perspective of folklore studies.

## Highlights

The sight of bare-skinned men in white loincloths leaping into a sub-zero swamp while shouldering bonden creates a breathtaking spectacle, where the white breath of participants and the snow-covered landscape form a striking contrast with the vivid colors of the bonden themselves. Young parishioners warm their bodies in advance with sake and fire before charging into the icy water with momentum. Following the swamp entry, sacred rituals are conducted at an altar by the water's edge, with sweet amazake rice drink and rice cakes offered to spectators. The whole event radiates the warm intimacy of a winter folk festival of the Yokote region.

## Event Details and Access

The venue is the Arasho district of Shimomuchi, Hiraka-machi, Yokote City, Akita Prefecture. Access is approximately 20 minutes by car from Yokote Station on the JR Ōu Main Line. The festival is held annually in mid-February during the Koshōgatsu (Little New Year) period. Viewing is free of charge, but warm clothing and boots are essential due to deep snow conditions.

## Surrounding Attractions

Yokote City offers a concentration of major tourist attractions including the Yokote Snow Festival (Kamakura), counted among Japan's three great snow festivals, the Masuda traditional architecture preservation district, the Gosannen Battle Kanazawa Museum, and the ruins of Yokote Castle. The winter season also brings opportunities to enjoy the home of Inaniwa udon noodles, the famed Yokote yakisoba, and visits to local sake breweries, allowing visitors to experience the food and culture of southern Akita in depth."""
    },
    {
        "qid": "Q127789312",
        "slug_ja": "koganei-sakura-matsuri",
        "slug_en": "koganei-sakura-matsuri",
        "manual_content_ja": """## 概要

小金井桜まつり（こがねいさくらまつり）は、東京都小金井市の都立小金井公園および玉川上水沿いの「名勝小金井（サクラ）」一帯で、毎年4月上旬の桜の見頃に合わせて開催される花見の祭典である。江戸期から続く桜の名所として知られ、市民・観光客で賑わう東京西郊の春の風物詩である。

## 歴史

小金井の桜並木は江戸時代中期、元文2年（1737年）に川崎平右衛門が玉川上水沿いの土手を補強する目的でヤマザクラ約2,000本を植樹したことに始まる。武蔵野の地味豊かな土壌と玉川上水の清流に育まれた桜並木は、江戸の名所として浮世絵にも描かれるほど親しまれ、明治末期に「名勝小金井（サクラ）」として国の名勝に指定された。第二次世界大戦中の伐採や戦後の都市開発で大幅に減少したものの、都立小金井公園の整備とともに新たに植樹が行われ、現代の桜まつりとして再生・継承されている。

## 見どころ

都立小金井公園内には約1,700本の桜が植えられ、ソメイヨシノ・ヤマザクラ・サトザクラなど多様な品種が次々と見頃を迎える。期間中は屋台の出店、地元和太鼓・伝統芸能の奉納演奏、フリーマーケットなどが行われ、家族連れで賑わう。江戸東京たてもの園を併設しているため、復元された明治大正期の建物群と桜のコラボレーションも楽しめる。

## 開催情報・アクセス

会場は東京都立小金井公園（東京都小金井市関野町1-13-1）。JR中央線武蔵小金井駅から関東バスで約5分。入園無料。例年4月上旬の桜の見頃に合わせて開催。

## 周辺観光

小金井公園内の江戸東京たてもの園は、東京の歴史的建造物を移築・復元した野外博物館として人気が高い。隣接する小平市の小平ふるさと村、武蔵野市の井の頭恩賜公園、府中市の大國魂神社など、武蔵野エリアの自然・歴史観光と組み合わせた周遊が可能。""",
        "manual_content_en": """## Overview

The Koganei Cherry Blossom Festival (Koganei Sakura Matsuri) is a flower-viewing celebration held annually in early April during the cherry blossom peak at Tokyo Metropolitan Koganei Park and along the Tamagawa Aqueduct in the "Scenic Beauty Koganei (Cherry Trees)" area in Koganei City, Tokyo. Famous as a cherry blossom destination since the Edo period, it has become a beloved springtime tradition of Tokyo's western suburbs, drawing crowds of residents and tourists alike.

## History

The Koganei cherry tree avenue traces its origins to the mid-Edo period in 1737 (Genbun 2), when Kawasaki Heiemon planted approximately 2,000 mountain cherry trees along the embankment of the Tamagawa Aqueduct as a reinforcement project. Nurtured by the fertile Musashino soil and the clear waters of the Tamagawa Aqueduct, the cherry tree avenue became a famous Edo landmark depicted in ukiyo-e prints and was officially designated as a National Place of Scenic Beauty as "Scenic Beauty Koganei (Cherry Trees)" in the late Meiji era. Although the number of trees declined significantly due to wartime felling during World War II and postwar urban development, new plantings have been carried out alongside the development of Koganei Park, and the festival has been revived and transmitted to the present day.

## Highlights

Tokyo Metropolitan Koganei Park hosts approximately 1,700 cherry trees, with diverse varieties including Somei Yoshino, mountain cherry, and Satozakura coming into peak bloom in succession. The festival period features food stalls, dedicatory performances of local taiko drumming and traditional folk arts, flea markets, and family-friendly entertainment. The adjacent Edo-Tokyo Open Air Architectural Museum offers the rare experience of viewing restored Meiji- and Taishō-period buildings amid the cherry blossoms.

## Event Details and Access

The venue is Tokyo Metropolitan Koganei Park (1-13-1 Sekino-chō, Koganei City, Tokyo). Access is approximately 5 minutes by Kantō Bus from Musashi-Koganei Station on the JR Chūō Line. Park admission is free. The festival is held annually in early April to coincide with the cherry blossom peak.

## Surrounding Attractions

The Edo-Tokyo Open Air Architectural Museum within Koganei Park is a popular outdoor museum displaying relocated and restored historical buildings of Tokyo. Together with nearby attractions such as Kodaira Furusato Village in Kodaira City, Inokashira Park in Musashino City, and Ōkunitama Shrine in Fuchū City, the Musashino area offers a rich combination of natural beauty, historical sites, and traditional culture for combined sightseeing tours."""
    },
    {
        "qid": "Q1636567",
        "slug_ja": "kobe-luminarie",
        "slug_en": "kobe-luminarie",
        "manual_content_ja": """## 概要

神戸ルミナリエ（こうべるみなりえ）は、兵庫県神戸市中央区の旧外国人居留地および東遊園地で毎年12月（近年は1月に変更）に開催される、阪神・淡路大震災の犠牲者への鎮魂と都市復興を祈念する大規模光の祭典である。1995年12月の初開催以来、神戸の冬の風物詩として定着し、世界的にも著名な光の芸術祭の一つに数えられる。

## 歴史

神戸ルミナリエは1995年1月17日の阪神・淡路大震災で犠牲となった6,434人の方々への鎮魂と被災者への希望の光を灯す目的で、同年12月にイタリアの光の芸術家ヴァルテル・パーレ・コモッリの企画により始まった。「ルミナリエ」とはイタリア語で「光の彫刻」を意味する伝統的な祭典に由来し、神戸市と神戸ルミナリエ組織委員会が主催する。第1回開催では約254万人が来場し、以降毎年12月初旬から中旬にかけて開催されてきた。2020-2022年はコロナ禍で中止・縮小開催となり、2024年からは開催時期を1月17日（震災記念日）に合わせて移動した。

## 見どころ

中心となる「フロントーネ」（正面装飾）と「ガレリア」（光の回廊）は、毎年異なるデザインで制作される手作業のイタリア式光のアーチで、約20万個のLED電球が点灯する。色彩豊かな光のトンネルを歩く体験は厳かで幻想的であり、震災の記憶と復興への祈りが込められた荘厳な雰囲気が漂う。東遊園地のメイン会場には「光の壁掛け（スパッリエーラ）」が設置され、フィナーレでは一斉点灯のセレモニーが行われる。

## 開催情報・アクセス

会場は兵庫県神戸市中央区の旧外国人居留地（仲町通り）および東遊園地。JR神戸線元町駅から徒歩約10分、阪神電鉄元町駅から徒歩約8分。観覧は無料だが、震災復興支援のための募金協力が呼びかけられる。近年は混雑緩和のため整理券・予約制を導入。

## 周辺観光

神戸市中心部には北野異人館街、南京町（神戸中華街）、メリケンパーク、ハーバーランド、神戸ポートタワーなどの観光名所が集中する。冬季は神戸牛・神戸ベーカリー文化、有馬温泉、六甲山夜景なども楽しめ、ルミナリエと組み合わせた1泊2日の都市観光が人気。""",
        "manual_content_en": """## Overview

Kobe Luminarie is a large-scale illumination festival held annually in December (recently shifted to January) at the former Foreign Settlement district and Higashi Yūenchi Park in Chūō Ward, Kobe City, Hyōgo Prefecture. Dedicated to the repose of victims of the Great Hanshin-Awaji Earthquake and to the prayer for urban recovery, the festival has become a defining winter tradition of Kobe since its first edition in December 1995 and is counted among the world's most renowned light art festivals.

## History

Kobe Luminarie was established to honor the 6,434 victims of the Great Hanshin-Awaji Earthquake of January 17, 1995, and to light a beacon of hope for survivors. The festival began in December of that same year under the artistic direction of Italian light artist Valerio Festi. The name "Luminarie" derives from a traditional Italian festival meaning "light sculptures," and the event is organized by Kobe City and the Kobe Luminarie Organizing Committee. The inaugural edition drew approximately 2.54 million visitors, and the festival has continued annually from early to mid-December ever since. From 2020 to 2022, the festival was cancelled or scaled down due to the COVID-19 pandemic, and from 2024 onward, the timing was shifted to align with January 17, the anniversary of the earthquake.

## Highlights

The centerpiece "Frontone" (front facade decoration) and "Galleria" (light corridor) are handmade Italian-style light arches designed differently each year, illuminated by approximately 200,000 LED bulbs. Walking through the colorful light tunnels offers a solemn and otherworldly experience, imbued with the memory of the earthquake and the prayer for recovery. The main venue at Higashi Yūenchi Park features a "Spalliera" (light wall decoration), and the finale includes a simultaneous lighting ceremony that captures the heart of the festival.

## Event Details and Access

The venues are the former Foreign Settlement district (Nakamachi-dōri) and Higashi Yūenchi Park in Chūō Ward, Kobe City, Hyōgo Prefecture. Access is approximately 10 minutes on foot from Motomachi Station on the JR Kōbe Line, or 8 minutes from Motomachi Station on the Hanshin Electric Railway. Admission is free, though donations are requested to support earthquake recovery efforts. In recent years, reservation and numbered-ticket systems have been introduced to manage crowds.

## Surrounding Attractions

Central Kobe offers a wealth of tourist attractions including the Kitano Ijinkan foreign residences district, Nankin-machi (Kobe Chinatown), Meriken Park, Harbor Land, and the Kobe Port Tower. The winter season also offers opportunities to enjoy Kobe beef cuisine, the city's bakery culture, Arima hot spring resort, and the night views from Mount Rokko, making a one- or two-night urban tourism stay combined with the Luminarie experience particularly popular among visitors."""
    },
    {
        "qid": "Q17226795",
        "slug_ja": "sana-jinja",
        "slug_en": "sana-jinja",
        "manual_content_ja": """## 概要

佐那神社（さなじんじゃ）は、三重県多気郡多気町仁田（にた）に鎮座する式内社で、天手力男命（あめのたぢからおのみこと）と曙立王命（あけたつおうのみこと）を祀る古社である。『延喜式神名帳』に記載される伊勢国多気郡の式内社の一座で、天岩戸神話の力の神を祀る格式高い神社として知られる。

## 歴史

佐那神社は『延喜式神名帳』（927年）に式内社として記載されており、創建年代は不詳ながら少なくとも平安時代以前に遡る古社である。主祭神の天手力男命は『古事記』『日本書紀』の天岩戸神話において、岩戸に隠れた天照大神を引き出す際にその巨石を投げ飛ばした剛力の神として知られ、武運・力・農耕守護の神として崇敬されてきた。配神の曙立王命は神武天皇の御代に活躍した皇族で、当地と関わりが深いと伝わる。伊勢神宮の祭祀圏に近接する立地から、古代より朝廷・神宮の崇敬を受け、中世以降は地域の鎮守として継承されてきた。

## 見どころ

社殿は神明造系の落ち着いた建築で、深い杜に囲まれた境内は伊勢神宮の社叢を彷彿とさせる清浄な雰囲気をたたえる。天手力男命を祀ることから、勝負事・武道・スポーツ・力仕事の守護神として崇敬を集め、力石が境内に奉納されている。例祭は10月で、地元氏子による神事・神楽奉納が行われる。

## 開催情報・アクセス

JR紀勢本線多気駅から車・タクシーで約15分。境内参拝は終日自由。例祭は毎年10月に執り行われる。

## 周辺観光

多気町・松阪市・伊勢市一帯は伊勢神宮の祭祀圏として古代史の聖地が集中する。伊勢神宮内宮・外宮、おかげ横丁、松阪城跡、本居宣長記念館、瀧原宮など、神道文化と国学の核心に触れられる観光地が点在する。多気町内のVISON（ヴィソン）は和食・伝統工芸の体験型大型施設として近年人気が高い。""",
        "manual_content_en": """## Overview

Sana Shrine (Sana Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Nita, Taki Town, Taki District, Mie Prefecture. The shrine enshrines Ame no Tajikarao no Mikoto and Aketatsuō no Mikoto as its principal deities. As one of the Engishiki-registered shrines of Taki District in Ise Province, it is renowned as a prestigious shrine dedicated to the deity of strength from the Heavenly Rock Cave mythology.

## History

Sana Shrine is recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. Although the founding date is unknown, its existence as an ancient shrine reaches back at least to before the Heian period. The principal deity Ame no Tajikarao no Mikoto is famous in the Kojiki and Nihon Shoki for being the powerful god who hurled away the great boulder when drawing forth the Sun Goddess Amaterasu from the Heavenly Rock Cave, and has been long venerated as a deity governing martial fortune, physical strength, and agricultural protection. The co-enshrined deity Aketatsuō no Mikoto was an imperial figure active during the reign of Emperor Jinmu, said to have deep connections with this region. Located in close proximity to the sacred precincts of the Ise Grand Shrine, Sana Shrine received veneration from the imperial court and the Grand Shrine from ancient times and has continued as a regional guardian shrine from the medieval period onward.

## Highlights

The main shrine hall is built in the restrained Shinmei-zukuri tradition, and the precincts enclosed by deep forest evoke the pure atmosphere of the sacred groves of the Ise Grand Shrine. Because the shrine enshrines Ame no Tajikarao no Mikoto, it has attracted worshippers seeking divine protection for competitions, martial arts, sports, and physically demanding work, with stone weights (chikara-ishi) traditionally dedicated within the precincts. The annual main festival is held in October and features sacred rituals and dedicatory kagura sacred dance performances by local parishioners.

## Event Details and Access

The shrine is accessible by car or taxi in approximately 15 minutes from Taki Station on the JR Kisei Main Line. The precincts are open for worship throughout the day. The annual main festival is held in October each year.

## Surrounding Attractions

The Taki Town, Matsusaka City, and Ise City area is densely packed with sacred sites of ancient Japanese history within the ritual precincts of the Ise Grand Shrine. Attractions include the Inner and Outer Shrines of Ise Jingū, the Okage Yokochō traditional street, the ruins of Matsusaka Castle, the Motoori Norinaga Memorial Museum, and Takihara no Miya. The expansive VISON facility in Taki Town has gained popularity in recent years as an experiential complex offering Japanese cuisine and traditional crafts, making it an excellent complement to the area's rich religious heritage."""
    },
    {
        "qid": "Q1749262",
        "slug_ja": "hakata-gion-yamakasa",
        "slug_en": "hakata-gion-yamakasa",
        "manual_content_ja": """## 概要

博多祇園山笠（はかたぎおんやまかさ）は、福岡県福岡市博多区の櫛田神社で毎年7月1日から15日にかけて行われる、約780年の歴史を持つ国指定重要無形民俗文化財の伝統祭礼である。総重量1トンを超える「舁き山笠（かきやまかさ）」を男衆が舁いて博多の街を疾走する勇壮な姿で全国的に知られ、ユネスコ無形文化遺産「山・鉾・屋台行事」を構成する日本三大祇園祭の一つに数えられる。

## 歴史

博多祇園山笠の起源は鎌倉時代の仁治2年（1241年）、博多に疫病が流行した際、承天寺の開祖・聖一国師が施餓鬼棚に乗って祈祷水を撒き疫病退散を祈願したことに始まると伝わる。室町期には博多商人が町の繁栄と疫病退散を祈願して山笠を担ぐ風習が定着し、戦国時代の博多焼失と豊臣秀吉による太閤町割（1587年）を経て、町ごとに「流（ながれ）」と呼ばれる組織が形成された。江戸期には豪華絢爛な「飾り山笠」が発達したが、明治31年（1898年）に電線架設で高さ制限が生じ、現在の「舁き山笠（疾走用・低い）」と「飾り山笠（観賞用・高い）」の二本立てに分化した。1979年に国の重要無形民俗文化財に指定、2016年にユネスコ無形文化遺産に登録された。

## 見どころ

最大の見せ場はクライマックスの「追い山笠」で、7月15日午前4時59分の太鼓を合図に櫛田神社を一斉スタートし、約5キロのコースを各流が全力疾走で駆け抜ける。総重量1トンの舁き山笠を約30人の舁き手が肩に担ぎ、地下足袋に長法被姿で「オイサ、オイサ」の掛け声と共に博多の街を疾走する姿は圧巻。期間中は市内14基の「飾り山笠」も街中に展示され、歴史絵巻や時事ネタを織り込んだ豪華な人形装飾を間近で観賞できる。

## 開催情報・アクセス

会場は櫛田神社（福岡市博多区上川端町1-41）を中心とする博多旧市街地一帯。JR博多駅から徒歩約15分、地下鉄祇園駅から徒歩約3分。観覧は無料。期間中（7/1-7/15）の最大の盛り上がりは15日早朝の追い山笠で、観客動員は約100万人。

## 周辺観光

博多区一帯は櫛田神社・東長寺・承天寺など歴史的寺社や、博多町家ふるさと館、博多伝統工芸館などが集中する。中洲屋台街、博多ラーメン、もつ鍋、明太子など博多グルメの聖地でもあり、福岡空港・博多駅の交通至便性と相まって、夏のインバウンド観光地として国際的人気が高い。""",
        "manual_content_en": """## Overview

Hakata Gion Yamakasa is a traditional festival with approximately 780 years of history, held annually from July 1 to 15 at Kushida Shrine in Hakata Ward, Fukuoka City, Fukuoka Prefecture, and designated as a National Important Intangible Folk Cultural Property. Renowned nationwide for the spectacular sight of men carrying "kakiyama" floats weighing over one ton while sprinting through the streets of Hakata, the festival is counted among Japan's three great Gion festivals and is a constituent element of the UNESCO Intangible Cultural Heritage "Yama, Hoko, Yatai Float Festivals."

## History

The origins of Hakata Gion Yamakasa trace back to 1241 (Ninji 2) during the Kamakura period, when an epidemic broke out in Hakata and Shōichi Kokushi, the founder of Jōten-ji Temple, mounted a segaki memorial platform and scattered blessed water to pray for the epidemic's end. During the Muromachi period, the custom of Hakata merchants shouldering yamakasa floats to pray for town prosperity and epidemic protection became firmly established. Following the destruction of Hakata during the Warring States period and Toyotomi Hideyoshi's Taikō Town Division (1587), neighborhood organizations called "Nagare" were formed. During the Edo period, magnificent "Kazariyama" decorative floats developed, but the introduction of overhead electrical wires in 1898 (Meiji 31) created height restrictions, leading to the current dual format of low "Kakiyama" (running floats) and tall "Kazariyama" (display floats). The festival was designated a National Important Intangible Folk Cultural Property in 1979 and registered as a UNESCO Intangible Cultural Heritage in 2016.

## Highlights

The climactic highlight is the "Oiyama" finale, when at the signal of drums at 4:59 a.m. on July 15, all teams simultaneously depart from Kushida Shrine and race through an approximately 5-kilometer course at full sprint. Approximately 30 carriers shoulder a one-ton kakiyama float, dressed in jika-tabi traditional footwear and long happi coats, charging through the streets of Hakata with shouts of "Oisa, Oisa." During the festival period, 14 ornate "Kazariyama" floats are displayed throughout the city, allowing close viewing of magnificent doll decorations incorporating historical scrolls and contemporary themes.

## Event Details and Access

The festival is centered around Kushida Shrine (1-41 Kamikawabata-chō, Hakata Ward, Fukuoka City) and extends throughout the old Hakata district. Access is approximately 15 minutes on foot from Hakata Station or 3 minutes from Gion Station on the subway. Viewing is free of charge. The peak excitement during the festival period (July 1-15) occurs during the Oiyama finale on the early morning of July 15, drawing approximately one million spectators in total.

## Surrounding Attractions

The Hakata Ward area features a concentration of historic temples and shrines including Kushida Shrine, Tōchō-ji Temple, and Jōten-ji Temple, as well as the Hakata Machiya Folk Museum and the Hakata Traditional Craft Museum. The district is also a sacred ground of Hakata cuisine, famed for its Nakasu yatai food stalls, Hakata ramen, motsunabe hot pot, and mentaiko spicy cod roe. Combined with the convenient access of Fukuoka Airport and Hakata Station, the area has gained tremendous international popularity as a summer inbound tourism destination."""
    },
    {
        "qid": "Q21653325",
        "slug_ja": "suigo-sawara-ayame-matsuri",
        "slug_en": "suigo-sawara-ayame-matsuri",
        "manual_content_ja": """## 概要

水郷佐原あやめ祭り（すいごうさわらあやめまつり）は、千葉県香取市の水郷佐原あやめパークで毎年5月下旬から6月下旬にかけて開催される、約400品種150万本のハナショウブが咲き誇る関東屈指のあやめ・花菖蒲の祭典である。利根川下流域の水郷地帯の風景と共に楽しむ花の祭りとして、対岸の茨城県潮来市の「水郷潮来あやめまつり」と並び称される。

## 歴史

佐原は江戸時代から利根川水運の要衝として栄えた水郷都市で、湿地帯に自生するあやめ・ハナショウブが古くから親しまれてきた。水郷佐原あやめパーク（旧・水郷佐原水生植物園）は1969年（昭和44年）に開園し、地域観光資源として整備された。香取市の市町村合併（2006年）後、施設改修を経て現在の「水郷佐原あやめパーク」として再オープンし、毎年のあやめ祭りも規模を拡大してきた。江戸期の利根川水運を支えた佐原の伝統と、ハナショウブを中心とする花文化の融合を体現する祭典として定着している。

## 見どころ

園内には約400品種・150万本のハナショウブが植えられ、紫・白・黄・絞り模様など色彩豊かな品種が一斉に見頃を迎える。期間中の土日には「嫁入り舟」が運行され、白無垢の花嫁が小舟で園内の水路を渡る往時の水郷婚礼風景を再現する。ろ舟遊覧、夜間ライトアップ、地元産品の販売、伝統芸能の奉納など、水郷文化を堪能できる多彩なプログラムが用意される。

## 開催情報・アクセス

会場は水郷佐原あやめパーク（千葉県香取市扇島1837-2）。JR成田線佐原駅から車・タクシーで約20分。期間中は臨時シャトルバスが運行される。入園は有料（あやめ祭り期間中の特別料金）。期間中の来場者は約30万人。

## 周辺観光

佐原市街は重要伝統的建造物群保存地区に指定され、江戸期の商家・蔵・水路が残る「小江戸佐原」として観光人気が高い。伊能忠敬旧宅・記念館、香取神宮、利根川河川敷、対岸の潮来あやめ園など、水郷文化と歴史を堪能できる観光資源が集中する。鹿島神宮との「鹿島・香取・息栖」東国三社巡りも近年人気。""",
        "manual_content_en": """## Overview

The Suigō Sawara Iris Festival (Suigō Sawara Ayame Matsuri) is a major iris and Japanese iris festival held annually from late May to late June at the Suigō Sawara Ayame Park in Katori City, Chiba Prefecture, showcasing approximately 1.5 million hanashōbu Japanese iris blooms across some 400 varieties. As one of the Kantō region's premier iris-viewing events, the festival is celebrated alongside the surrounding water-country landscape of the lower Tone River basin and is widely paired with the Suigō Itako Iris Festival on the opposite bank in Ibaraki Prefecture.

## History

Sawara flourished from the Edo period as a key water-transport hub along the Tone River, and the iris and hanashōbu plants native to the surrounding wetlands have long been cherished by local residents. The Suigō Sawara Ayame Park (formerly the Suigō Sawara Aquatic Botanical Garden) was opened in 1969 (Shōwa 44) and developed as a regional tourism resource. Following the municipal merger of Katori City in 2006, the facility underwent renovation and reopened as the current "Suigō Sawara Ayame Park," with the annual iris festival continuing to expand in scale. The festival has become firmly established as a celebration embodying the fusion of Sawara's tradition supporting the Edo-era Tone River water transport and its flower culture centered on hanashōbu.

## Highlights

The park hosts approximately 1.5 million hanashōbu plants across some 400 varieties, displaying a spectacular palette of purple, white, yellow, and variegated blooms at peak bloom. On weekends during the festival period, the famous "Bridal Boat" (Yomeiri-bune) procession reenacts traditional water-borne wedding ceremonies, with brides in pristine white wedding kimono ferried across the canals of the park in small wooden boats. Diverse programs allow visitors to fully experience the water culture, including ro-bune rowboat tours, evening illuminations, sales of local specialty products, and dedicatory performances of traditional folk arts.

## Event Details and Access

The venue is the Suigō Sawara Ayame Park (1837-2 Ōgishima, Katori City, Chiba Prefecture). Access is approximately 20 minutes by car or taxi from Sawara Station on the JR Narita Line, with special shuttle bus service operating during the festival period. Park admission requires a special festival-period entry fee. The event draws approximately 300,000 visitors over its month-long run.

## Surrounding Attractions

The Sawara city center is designated as a National Important Preservation District for Groups of Traditional Buildings, retaining Edo-period merchant houses, traditional storehouses, and historic canals that have earned it the nickname "Little Edo Sawara" and made it a highly popular tourist destination. Concentrated attractions include the former residence and memorial museum of Inō Tadataka (the renowned Edo-period cartographer), Katori Shrine, the Tone River embankment, and the Itako Iris Garden on the opposite shore. The "Kashima-Katori-Ikisu" tour of the Three Eastern Shrines, including Kashima Shrine, has also gained considerable popularity in recent years."""
    },
    {
        "qid": "Q22120521",
        "slug_ja": "miyake-jinja-suzuka",
        "slug_en": "miyake-jinja-suzuka",
        "manual_content_ja": """## 概要

三宅神社（みやけじんじゃ）は、三重県鈴鹿市国府町（こうちょう）に鎮座する式内社で、大彦命（おおひこのみこと）を主祭神として祀る古社である。『延喜式神名帳』に記載される伊勢国鈴鹿郡の式内社の一座で、古代豪族・三宅連（みやけのむらじ）との結びつきと、伊勢国府推定地に隣接する立地で知られる。

## 歴史

三宅神社は『延喜式神名帳』（927年）に式内社として記載されており、創建年代は不詳ながら少なくとも平安時代以前に遡る古社である。主祭神の大彦命は『古事記』『日本書紀』において第8代孝元天皇の皇子で、四道将軍の一人として北陸道を平定した皇族として記される。その子孫が三宅連を名乗り、ヤマト政権の屯倉（みやけ・直轄領）管理を司ったとされる。鎮座地の鈴鹿市国府町一帯は伊勢国府の所在地と推定される古代地名で、国府の鎮守として機能した可能性が高く、律令期から朝廷の崇敬を受けた古社として継承されてきた。

## 見どころ

社殿は近世以降の建築様式を残し、深い杜に囲まれた境内には古代の聖域の名残が感じられる。伊勢国府推定地に隣接する立地から、考古学・古代史研究の観点でも注目される。境内には三宅連ゆかりの祭神を象徴する文物や、地域の郷土史を語る石碑が残されている。例祭は秋季10月で、地元氏子による神事と神楽奉納が行われる。

## 開催情報・アクセス

近鉄鈴鹿線平田町駅から車・タクシーで約10分。境内参拝は終日自由。秋季例祭は毎年10月に執り行われる。

## 周辺観光

鈴鹿市は鈴鹿サーキットで有名なモータースポーツの聖地として国際的に知られる。椿大神社（猿田彦大本宮）、伊勢国分寺跡、加佐登神社など、伊勢国西部の古代史を語る古社・史跡が集中する。亀山市・関宿の伝統的町並み、菰野町の湯の山温泉、四日市港など、北勢地域の観光資源と組み合わせた周遊が可能。""",
        "manual_content_en": """## Overview

Miyake Shrine (Miyake Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Kō-chō, Suzuka City, Mie Prefecture. The shrine enshrines Ōhiko no Mikoto as its principal deity. As one of the Engishiki-registered shrines of Suzuka District in Ise Province, it is known for its connection to the ancient Miyake no Muraji clan and its location adjacent to the presumed site of the Ise Provincial Government Office.

## History

Miyake Shrine is recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. Although the founding date is unknown, its existence as an ancient shrine reaches back at least to before the Heian period. The principal deity Ōhiko no Mikoto is recorded in the Kojiki and Nihon Shoki as a son of the eighth emperor Kōgen and as one of the Shidō Shōgun (Four-Road Generals) who pacified the Hokurikudō region. His descendants took the name Miyake no Muraji and are said to have served the Yamato court by managing the miyake (directly controlled territories of the imperial government). The shrine's location in the Kō-chō district of Suzuka City corresponds to the presumed site of the Ise Provincial Government Office, suggesting the shrine likely functioned as a guardian shrine of the provincial government and has been transmitted as an ancient shrine receiving imperial court veneration since the Ritsuryō period.

## Highlights

The main shrine hall preserves the architectural style from the early-modern period onward, and the precincts enclosed by deep forest convey the lingering presence of an ancient sacred site. The location adjacent to the presumed Ise Provincial Government Office site attracts attention from the perspectives of archaeology and ancient historical research. Within the precincts remain artifacts symbolizing the deities associated with the Miyake no Muraji clan and stone monuments narrating local regional history. The annual main festival is held in October and features sacred rituals and dedicatory kagura sacred dance performances by local parishioners.

## Event Details and Access

The shrine is accessible by car or taxi in approximately 10 minutes from Hirata-chō Station on the Kintetsu Suzuka Line. The precincts are open for worship throughout the day. The autumn main festival is held in October each year.

## Surrounding Attractions

Suzuka City is internationally renowned as a motor sports mecca, home to the famous Suzuka Circuit racetrack. The area features a concentration of ancient shrines and historical sites narrating the ancient history of western Ise Province, including Tsubaki Grand Shrine (Sarutahiko Daihongū), the ruins of the Ise Provincial Temple, and Kasado Shrine. Combined sightseeing tours are possible incorporating the traditional townscape of Kameyama City and Seki-juku, the Yunoyama Hot Spring resort in Komono Town, and Yokkaichi Port, allowing visitors to explore the diverse tourism resources of the Hokusei region."""
    },
    {
        "qid": "Q24887619",
        "slug_ja": "iriya-asagao-matsuri",
        "slug_en": "iriya-asagao-matsuri",
        "manual_content_ja": """## 概要

入谷朝顔まつり（いりやあさがおまつり）は、東京都台東区下谷の入谷鬼子母神（真源寺）境内およびその周辺の言問通り沿いで、毎年7月6日から8日にかけて開催される朝顔の市である。江戸の風物詩として明治期に始まり、東京都内最大の朝顔市として広く親しまれ、約60万人の来場者を集める下町の夏の風物詩である。

## 歴史

入谷の朝顔は江戸末期から明治期にかけて、入谷一帯の植木屋が栽培した変化朝顔（へんかあさがお）で全国的に名を馳せた。当時の入谷は江戸郊外の田園地帯で、ヘチマ・ヒョウタン・朝顔などの園芸植物の生産地として栄えていた。明治13年（1880年）頃から入谷鬼子母神を中心に朝顔市が立つようになり、変化朝顔の珍品奇種を求める愛好家で賑わった。第二次世界大戦中の一時中断を経て、1948年（昭和23年）に地元商店街・植木組合の尽力で復活、以降毎年7月6-8日の3日間に定着し、台東区の指定無形文化財に登録されている。

## 見どころ

期間中は約120軒の朝顔業者と100軒の露店が言問通り沿いに軒を連ね、朝早朝5時頃から夜23時頃まで賑わう。並ぶ朝顔は伝統的な大輪朝顔、団十郎（赤茶色）、団十郎黒、変化朝顔の貴重種など多彩で、1鉢2,000円前後から購入可能。入谷鬼子母神では参拝者で行列ができ、朝顔をモチーフにした団扇・絵馬・お守りも頒布される。地元商店街の屋台料理、伝統工芸品の露店も人気。

## 開催情報・アクセス

会場は入谷鬼子母神（真源寺・東京都台東区下谷1-12-16）および周辺言問通り沿い。地下鉄日比谷線入谷駅から徒歩約1分、JR山手線鶯谷駅から徒歩約7分。観覧・入場は無料。開催時間は7月6-8日の3日間、早朝5時頃から夜23時頃まで。

## 周辺観光

下町情緒の濃い台東区一帯は浅草寺・浅草神社・仲見世通り・浅草演芸ホール、上野公園・東京国立博物館・上野動物園、谷中銀座商店街・谷中霊園など、東京の伝統と歴史を堪能できる観光資源が集中する。7月初旬の朝顔まつりに続き、7月9-10日には浅草寺の「ほおずき市」も開催されるため、下町の夏祭りを連続で楽しむ周遊コースが人気。""",
        "manual_content_en": """## Overview

The Iriya Asagao Festival (Iriya Morning Glory Market) is a traditional morning glory market held annually from July 6 to 8 at Iriya Kishimojin (Shingen-ji Temple) and along the surrounding Kototoi-dōri Avenue in Shitaya, Taitō Ward, Tokyo. Originating as an Edo-era tradition that flourished during the Meiji period, it is widely cherished as Tokyo's largest morning glory market, drawing approximately 600,000 visitors and standing as a defining summer tradition of Tokyo's old downtown district.

## History

The morning glories of Iriya gained nationwide fame during the late Edo and Meiji periods through "henka asagao" (variant morning glories) cultivated by gardeners throughout the Iriya area. At that time, Iriya was a rural area on the outskirts of Edo that flourished as a production center for garden plants including loofah, gourd, and morning glory. From around 1880 (Meiji 13), morning glory markets began to be held around Iriya Kishimojin, attracting enthusiasts seeking rare and unusual variant morning glories. Following a temporary suspension during World War II, the festival was revived in 1948 (Shōwa 23) through the efforts of the local merchant association and gardening union, and has continued annually on the three days of July 6-8 ever since. The festival is registered as a Designated Intangible Cultural Property of Taitō Ward.

## Highlights

During the festival period, approximately 120 morning glory vendors and 100 food and craft stalls line the Kototoi-dōri Avenue, bustling from early morning around 5 a.m. until late at night around 11 p.m. The morning glories on display include traditional large-blossom varieties, the distinctive reddish-brown "Danjūrō," the prized "Danjūrō Black," and rare specimens of variant morning glories, with potted plants available from around 2,000 yen each. Iriya Kishimojin attracts queues of worshippers, and morning glory-motif uchiwa fans, prayer plaques, and amulets are distributed. The local merchant association's food stalls and traditional craft vendors also enjoy great popularity.

## Event Details and Access

The venue is Iriya Kishimojin (Shingen-ji Temple, 1-12-16 Shitaya, Taitō Ward, Tokyo) and the surrounding Kototoi-dōri Avenue. Access is approximately 1 minute on foot from Iriya Station on the Tokyo Metro Hibiya Line, or 7 minutes from Uguisudani Station on the JR Yamanote Line. Admission is free. The festival runs from July 6 to 8, from early morning around 5 a.m. until late at night around 11 p.m.

## Surrounding Attractions

The Taitō Ward area, rich in the atmosphere of old Tokyo, offers a concentration of tourism resources for experiencing the city's traditions and history, including Sensōji Temple, Asakusa Shrine, Nakamise-dōri shopping street, the Asakusa Engei Hall, Ueno Park, the Tokyo National Museum, Ueno Zoo, the Yanaka Ginza shopping street, and Yanaka Cemetery. Following the Asagao Festival in early July, the "Hōzuki-ichi" (Chinese Lantern Plant Market) is held at Sensōji Temple on July 9-10, making a consecutive tour of the downtown summer festivals particularly popular among visitors."""
    },
    {
        "qid": "Q30924149",
        "slug_ja": "honensai-tagata-jinja",
        "slug_en": "honensai-tagata-jinja",
        "manual_content_ja": """## 概要

豊年祭（ほうねんさい）は、愛知県小牧市田縣町（たがたちょう）の田縣神社（たがたじんじゃ）で毎年3月15日に行われる、五穀豊穣・子孫繁栄・万物育成を祈願する古代農耕祭礼である。男性のシンボルを御神体とする神事として国際的に広く知られ、日本古来の生命崇拝・農耕信仰の素朴な原型を伝える希少な民俗祭として、毎年多くの国内外の参拝客が訪れる。

## 歴史

田縣神社は『延喜式神名帳』（927年）に式内社として記載される尾張国丹羽郡の古社で、御歳神（みとしのかみ）と玉姫命（たまひめのみこと）を祀る。御歳神は五穀豊穣の神、玉姫命は子孫繁栄・夫婦和合・万物育成の女神とされる。豊年祭の起源は弥生時代の農耕儀礼に遡るとされ、男性器を象徴する御神体「大男茎形（おおおわせがた）」を奉納することで稲作の豊穣と人々の生命力の更新を祈念してきた。中世以降は神仏習合を経て民俗祭として継承され、明治期の神仏分離後も古い形態を維持し、現在に至る。日本の生殖崇拝・農耕信仰の最も古層を伝える祭として民俗学的価値が極めて高い。

## 見どころ

祭礼のクライマックスは午後2時頃からの行列で、新調された木製の御神体（長さ約2.5メートル、重さ約280キロ）を厄年の男性が担ぎ、田縣神社から熊野社まで約1キロを練り歩く。地元の女性が小型の御神体を抱える「巫女行列」、餅まきも行われる。境内には多数の同様の御神体が奉納されており、夫婦和合・子授け・縁結びを祈願する参拝者で賑わう。国際的にも「Penis Festival」として広く報道され、海外からの観光客も多く訪れる。

## 開催情報・アクセス

会場は田縣神社（愛知県小牧市田県町152）。名鉄小牧線田県神社前駅から徒歩約5分。開催日は毎年3月15日（曜日固定）、午前10時頃から午後4時頃まで。参拝・観覧は無料、餅まきへの参加も自由。

## 周辺観光

小牧市内には小牧城・小牧山史跡公園、犬山市の犬山城（国宝）、明治村、リトルワールド、犬山温泉郷など、尾張地方の歴史と文化を堪能できる観光資源が集中する。豊年祭の対となる祭として、小牧市の北隣の犬山市・大縣神社（おおあがたじんじゃ）の「豊年祭（梵天祭）」（女性器を象徴・3月15日に近い日曜日開催）も合わせて訪問する周遊が定番。""",
        "manual_content_en": """## Overview

Hōnensai (Bountiful Harvest Festival) is an ancient agricultural festival held annually on March 15 at Tagata Shrine in Tagata-chō, Komaki City, Aichi Prefecture, dedicated to prayers for bountiful harvests, prosperity of descendants, and the flourishing of all living things. Internationally known as a Shinto ritual featuring a male symbol as its sacred object, the festival is recognized as a rare folk celebration preserving the primitive form of Japan's ancient veneration of life and agricultural beliefs, drawing numerous domestic and international visitors each year.

## History

Tagata Shrine is an ancient shrine of Niwa District in Owari Province, recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927, enshrining Mitoshi no Kami and Tamahime no Mikoto. Mitoshi no Kami is the deity of bountiful harvests, while Tamahime no Mikoto is venerated as a goddess of prosperity of descendants, marital harmony, and the flourishing of all living things. The origins of Hōnensai are traced back to agricultural rituals of the Yayoi period, when offerings of the male-symbol sacred object "Ōowasegata" were made to pray for bountiful rice harvests and the renewal of the people's vital force. From the medieval period onward, the festival continued as a folk celebration through the syncretism of Shinto and Buddhism, and maintained its ancient form even after the Meiji-era separation of Shinto and Buddhism. It holds exceptionally high folkloric value as a festival transmitting the oldest stratum of Japan's reproductive veneration and agricultural beliefs.

## Highlights

The festival's climax is the procession beginning around 2 p.m., in which men of the unlucky age (yakudoshi) shoulder a newly carved wooden sacred object (approximately 2.5 meters long and 280 kilograms in weight) and parade approximately 1 kilometer from Tagata Shrine to Kumano Shrine. A "miko procession" of local women carrying smaller sacred objects also takes place, along with a mochi-throwing ceremony. The precincts contain numerous similar sacred objects dedicated by worshippers, attracting visitors praying for marital harmony, fertility, and matchmaking. Widely reported internationally as the "Penis Festival," the event also draws many overseas tourists.

## Event Details and Access

The venue is Tagata Shrine (152 Tagata-chō, Komaki City, Aichi Prefecture). Access is approximately 5 minutes on foot from Tagata-Jinja-mae Station on the Meitetsu Komaki Line. The festival is held annually on March 15 (fixed date, regardless of day of the week), from around 10 a.m. to 4 p.m. Worship and viewing are free of charge, and participation in the mochi-throwing ceremony is open to all.

## Surrounding Attractions

Komaki City features tourism resources for experiencing the history and culture of the Owari region, including Komaki Castle, the Komaki-yama Historic Park, and nearby Inuyama City's Inuyama Castle (a National Treasure), Meiji-mura open-air museum, Little World, and the Inuyama Hot Spring resort. As a counterpart festival to Hōnensai, the "Hōnensai (Bonten Festival)" held at Ōagata Shrine in neighboring Inuyama City—featuring a female-symbol sacred object and held on the Sunday closest to March 15—is traditionally visited as part of a paired sightseeing tour."""
    },
    {
        "qid": "Q30925534",
        "slug_ja": "iyu-jinja",
        "slug_en": "iyu-jinja",
        "manual_content_ja": """## 概要

伊甘神社（いゆうじんじゃ）は、島根県浜田市下府町（しもこうちょう）に鎮座する式内社で、伊甘大神（いゆうのおおかみ）を主祭神として祀る古社である。『延喜式神名帳』に記載される石見国那賀郡の式内社の一座で、石見国府の所在地に隣接する立地と、古代石見国の総鎮守として崇敬されてきた格式の高さで知られる。

## 歴史

伊甘神社は『延喜式神名帳』（927年）に式内社として記載されており、創建年代は不詳ながら少なくとも平安時代以前に遡る古社である。主祭神の伊甘大神は地域の祖神・国津神とされ、古代石見国の開拓と農耕守護の神として崇敬されてきた。鎮座地の浜田市下府町一帯は石見国府の所在地と推定される古代地名で、伊甘神社は国府の鎮守として機能した可能性が高い。律令期から朝廷の崇敬を受け、中世以降は石見地方の地域信仰の中核として機能、明治期の社格制度では郷社に列せられた。

## 見どころ

社殿は出雲地方特有の大社造系の意匠を残す近世建築で、簡素ながら格調高い佇まいが特徴。境内には古代国府時代を偲ばせる石組みや、樹齢数百年とされる神木が残されている。石見国府推定地に隣接する立地から、考古学・古代史研究の観点でも注目される。例祭は秋季10月で、地元氏子による神事と神楽奉納が行われ、石見地方独特の「石見神楽」が奉納されることもある。

## 開催情報・アクセス

JR山陰本線下府駅から徒歩約15分または車で約5分。境内参拝は終日自由。秋季例祭は毎年10月に執り行われる。

## 周辺観光

浜田市は日本海に面した山陰地方の港町で、石見畳ヶ浦（国指定天然記念物・名勝）、しまね海洋館アクアス、浜田城跡、世界遺産・石見銀山遺跡（隣接する大田市）など、石見地方の自然・歴史・文化を堪能できる観光資源が集中する。石見神楽の上演施設、温泉津温泉、有福温泉など温泉文化も楽しめ、出雲大社・松江城との周遊観光が可能。""",
        "manual_content_en": """## Overview

Iyu Shrine (Iyu Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Shimokō-chō, Hamada City, Shimane Prefecture. The shrine enshrines Iyu no Ōkami as its principal deity. As one of the Engishiki-registered shrines of Naka District in Iwami Province, it is renowned for its location adjacent to the site of the Iwami Provincial Government Office and its prestigious status as a chief tutelary shrine of ancient Iwami Province.

## History

Iyu Shrine is recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. Although the founding date is unknown, its existence as an ancient shrine reaches back at least to before the Heian period. The principal deity Iyu no Ōkami is considered an ancestral deity and earth-born deity (kunitsukami) of the region, venerated as the god of pioneering settlement and agricultural protection in ancient Iwami Province. The shrine's location in the Shimokō-chō district of Hamada City corresponds to the presumed site of the Iwami Provincial Government Office, suggesting Iyu Shrine likely functioned as a guardian shrine of the provincial government. The shrine received veneration from the imperial court since the Ritsuryō period, served as a central institution of regional faith in the Iwami area from the medieval period onward, and was ranked as a Gōsha (district shrine) under the Meiji-era shrine ranking system.

## Highlights

The main shrine hall is an early-modern construction preserving design elements of the Taisha-zukuri tradition characteristic of the Izumo region, featuring a simple yet refined and dignified appearance. The precincts contain stone arrangements evoking the era of the ancient provincial government and sacred trees estimated to be several centuries old. The location adjacent to the presumed Iwami Provincial Government Office site attracts attention from the perspectives of archaeology and ancient historical research. The annual main festival is held in October and features sacred rituals and dedicatory kagura sacred dance performances by local parishioners, sometimes including offerings of the distinctive "Iwami Kagura" unique to the Iwami region.

## Event Details and Access

The shrine is accessible approximately 15 minutes on foot or 5 minutes by car from Shimokō Station on the JR San'in Main Line. The precincts are open for worship throughout the day. The autumn main festival is held in October each year.

## Surrounding Attractions

Hamada City is a port town facing the Sea of Japan in the San'in region, offering a concentration of tourism resources for experiencing the nature, history, and culture of the Iwami area, including Iwami Tatamigaura (a nationally designated Natural Monument and Place of Scenic Beauty), the Shimane Aquarium Aquas, the ruins of Hamada Castle, and the nearby UNESCO World Heritage Site of the Iwami Ginzan Silver Mine in adjacent Ōda City. Visitors can also enjoy Iwami Kagura performance venues and the hot spring culture of Yunotsu Onsen and Arifuku Onsen, making it possible to combine sightseeing with Izumo Taisha Grand Shrine and Matsue Castle for a comprehensive tour of the San'in region."""
    },
]

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    for item in ITEMS:
        cur.execute("""
            UPDATE festivals
            SET slug_ja=?, slug_en=?, manual_content_ja=?, manual_content_en=?, status='drafted'
            WHERE qid=?
        """, (item["slug_ja"], item["slug_en"], item["manual_content_ja"], item["manual_content_en"], item["qid"]))
        print(f"[OK] {item['qid']} updated to drafted (rows={cur.rowcount})")
    conn.commit()
    print("\n=== Verification ===")
    for item in ITEMS:
        cur.execute("SELECT qid, label_ja, status, LENGTH(manual_content_ja), LENGTH(manual_content_en) FROM festivals WHERE qid=?", (item["qid"],))
        row = cur.fetchone()
        print(f"[VERIFY] {row[0]} {row[1]} status={row[2]} len_ja={row[3]} len_en={row[4]}")
    conn.close()

if __name__ == "__main__":
    main()
