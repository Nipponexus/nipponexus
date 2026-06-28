#!/usr/bin/env python3
"""Insert festivals #61-65 (Phase 1c day 6 part 1)"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q20045025",
        "slug_ja": "jindai-ji-hozuki-matsuri",
        "slug_en": "jindai-ji-hozuki-matsuri",
        "manual_content_ja": """深大寺鬼燈まつりは、東京都調布市の深大寺で毎年7月の3連休に開催される夏の風物詩であり、東京西部で最も親しまれている真夏の縁日の一つである。深大寺の参道や境内に並ぶ約120軒のほおずき店が、朱色に染まった実をたわわに付けたほおずき鉢を売り、来場者は涼やかな鈴の音と緑陰に包まれて夏の入りを楽しむ。

深大寺は奈良時代の733年（天平5年）に開かれたとされる関東屈指の古刹で、本尊の白鳳期釈迦如来倚像は国宝に指定されている。浅草寺に次ぐ東京で2番目に古い寺としても知られ、武蔵野の面影を残す広大な境内には参道沿いに名物のそば店が並ぶ。鬼燈まつり期間中はこの参道に加えて、境内・元三大師堂・釈迦堂周辺まで露店が広がり、寺院ならではの厳かさと縁日の賑わいが共存する独特の雰囲気が生まれる。

ほおずきは古くから「鬼灯」と書かれ、お盆に祖先の霊を迎える際の提灯に見立てられる縁起物として、また実から取れる成分が薬用に用いられたことから、夏の魔除けと無病息災の象徴として親しまれてきた。深大寺の鬼燈まつりは、東京都内では浅草寺のほおずき市と並ぶ規模を誇り、より落ち着いた寺町の雰囲気の中でほおずきを選べることから、毎年家族連れや写真愛好家、地元の常連客で賑わう。

期間中は寺院による特別な法要や、お練り行列が行われる日もあり、深大寺そばの食べ歩き、地ビール「深大寺ビール」、団子や和菓子など武蔵野の味覚も楽しめる。隣接する神代植物公園のバラ園や芝生広場と組み合わせれば、半日から一日かけて緑豊かな調布の自然と寺院文化を堪能できる。

アクセスは京王線調布駅から京王バスで約15分、JR三鷹駅・吉祥寺駅からも小田急バスで深大寺前まで直行できる。新宿から京王線特急で約20分という都心からの近さも魅力で、東京観光の合間に立ち寄れる隠れた夏の名所として、近年は海外からの旅行者にも知られるようになってきている。""",
        "manual_content_en": """The Jindai-ji Hozuki Festival is one of the most beloved midsummer events in western Tokyo, held annually over a three-day weekend in July at Jindai-ji Temple in the city of Chofu. The temple's approach, main precincts, and surrounding lanes fill with approximately one hundred twenty hozuki vendors selling potted Chinese lantern plants laden with bright orange-red fruits, accompanied by the soft chiming of wind chimes that signals the arrival of high summer.

Jindai-ji Temple is among the most historically significant Buddhist sites in the Tokyo area. Founded in 733 during the Nara period, it is the second-oldest temple in Tokyo after the more famous Senso-ji in Asakusa. The temple is renowned for its principal image, a bronze seated Shaka Nyorai dating from the Hakuho period of the late seventh century and designated a National Treasure of Japan as the oldest Buddhist statue in eastern Japan. The grounds preserve much of the wooded character of the original Musashino landscape that once covered the Kanto plain, with venerable trees, mossy stone steps, and a network of small streams creating an atmosphere quite distinct from the urban density of central Tokyo only thirty minutes away.

The festival centers on the hozuki, known in English as Chinese lantern plant or winter cherry, whose Japanese name combines characters meaning demon and lantern. The bright orange husks enclosing the small red fruits resemble paper lanterns and have been associated since ancient times with the lanterns used during the Obon festival to guide ancestral spirits home. The plant also has a long history of medicinal use, with extracts traditionally employed as a mild sedative and for various ailments. Together these associations have established hozuki as a powerful summer talisman, symbolizing protection from heat-related illness and welcoming favorable spirits into the household for the season.

The Jindai-ji festival rivals the more famous Senso-ji hozuki-ichi held in Tokyo's Asakusa district in early July, but offers a distinctly different atmosphere. While Senso-ji's market unfolds in the dense urban temple precinct with overwhelming crowds, Jindai-ji's festival takes place in a temple village setting where soba noodle shops, traditional sweet shops, and small craft stores line winding paths beneath ancient trees. The pace is more relaxed, allowing visitors to examine plants carefully, speak with the growers, and select pots that will mature into beautiful displays over the coming weeks. Each pot typically costs between two and three thousand yen and is sold with a small bell-shaped wind chime attached, the soft sound of which is considered part of the gift.

The temple holds special Buddhist services during the festival period, and on certain days a formal procession known as an oneri makes its way through the grounds with priests in ceremonial robes carrying offerings to the main hall. These religious observances run alongside the commercial festivities, reminding visitors of the festival's roots in the cycle of Buddhist devotional life.

Culinary attractions abound throughout the festival area. Jindai-ji is famous for its handmade soba noodles, and visitors can sample the fresh buckwheat noodles at any of the dozen or so soba shops along the approach road, many of which have been operating for generations. The locally brewed Jindai-ji Beer offers a craft alternative to mass-market beverages, and traditional sweets such as warabi-mochi and dango are widely available from stalls and small confectioneries. The temple area is also adjacent to Jindai Botanical Gardens, where visitors can extend their visit with a walk through the rose garden, which reaches peak bloom in late spring and early autumn, or the spacious lawn areas popular with families.

Access to the festival is straightforward despite its location away from the main Tokyo rail lines. Keio Bus from Chofu Station on the Keio Line reaches the temple area in approximately fifteen minutes, and Odakyu buses serve the temple directly from JR Mitaka and Kichijoji stations on the Chuo Line. From central Tokyo, Chofu can be reached from Shinjuku in about twenty minutes on the Keio Line limited express service, making Jindai-ji an accessible half-day or full-day excursion that combines Buddhist heritage, traditional commerce, and the natural beauty of preserved Musashino woodland.""",
    },
    {
        "qid": "Q21652456",
        "slug_ja": "ichinomiya-tanabata",
        "slug_en": "ichinomiya-tanabata",
        "manual_content_ja": """一宮七夕まつりは、愛知県一宮市の中心市街地で毎年7月最終週の木曜日から日曜日にかけて開催される七夕祭りであり、仙台七夕・平塚七夕と並ぶ日本三大七夕の一つに数えられる。期間中は約120万人の来場者が訪れ、一宮駅前のアーケード街と商店街が華やかな七夕飾りで埋め尽くされる、東海地方を代表する夏の風物詩である。

一宮市は古くから繊維産業、特に毛織物の集積地として知られ、戦前から「ガチャ万景気」と呼ばれる繊維業の黄金期を経験した街である。一宮七夕まつりは、この繊維業の繁栄を背景に1956年（昭和31年）に始まった。地元の織物業者や商店主が、織女・棚機津女（たなばたつめ）の伝説にちなんで自社の織物製品を七夕飾りとして街に展示したのが起源で、繊維のまちならではの華麗な布製吹き流しが他の七夕祭りと異なる独自の魅力を形作っている。

最大の見どころは、本町商店街・銀座通り・栄通りを中心に飾られる豪華絢爛な吹き流しと七夕飾りである。仙台七夕の和紙製吹き流しと異なり、一宮では繊維のまちを象徴する色とりどりの布製吹き流しが主流で、長さ10メートルを超える大型作品が頭上を埋め尽くす。商店主や事業所が前年から準備した個性豊かな飾りが競演し、地元住民の投票による「コンクール」も実施されて優秀作品が表彰される。

期間中は本町通りを中心にパレードが繰り広げられ、コスチュームパレードや一宮おどりパレード、ミスコンテスト、ステージイベントなどが連続して開催される。地元の市民団体・学校・企業・町内会が参加し、世代を超えた賑わいを生み出す。屋台村も商店街沿いに数百軒並び、味噌煮込みうどん、ひつまぶし、味噌カツ、きしめん、串カツなど名古屋圏の郷土料理が幅広く味わえる。

アクセスはJR尾張一宮駅および名鉄一宮駅から徒歩約3分。名古屋駅から名鉄またはJR東海道本線で約12分とアクセス抜群で、名古屋観光の一環として組み入れやすい立地である。犬山城・国宝犬山祭の山車展示、岐阜の長良川鵜飼など東海地方の夏の名所と組み合わせれば、繊維のまちの歴史と七夕文化を堪能する旅程が構成できる。""",
        "manual_content_en": """The Ichinomiya Tanabata Festival is one of Japan's three great Tanabata celebrations, held annually from Thursday through Sunday during the final week of July in the central districts of Ichinomiya City, Aichi Prefecture. Alongside the Sendai Tanabata Festival and the Shonan Hiratsuka Tanabata Festival, it forms the trio of major Tanabata events that draw the largest crowds in Japan, with approximately 1.2 million visitors over its four-day run. The festival transforms the shopping arcades and main streets around Ichinomiya Station into a canopy of brilliant fabric streamers, celebrating both the ancient star festival and the city's heritage as one of Japan's most important textile manufacturing centers.

Ichinomiya rose to prominence during the late nineteenth and early twentieth centuries as the heart of Japan's wool textile industry, producing high-quality woolen fabrics that supplied the rapidly modernizing nation. The local industry experienced its golden age in the postwar period, when the so-called gacha-man boom—a term coined to describe the speed at which money flowed in—made the city one of Japan's wealthiest small cities per capita. The Ichinomiya Tanabata Festival was established in 1956, at the height of this textile boom, when local manufacturers and shopkeepers began displaying their finest textile products as Tanabata decorations along the city's main streets. The festival drew explicit inspiration from the Tanabata legend itself, in which the deified weaver maiden Orihime is separated from her lover Hikoboshi by the Milky Way and permitted to meet him only once a year.

The festival's most distinctive feature is its fukinagashi, the long decorative streamers that have become synonymous with major Tanabata celebrations. While the streamers at Sendai's famous festival are made from washi paper, Ichinomiya's are predominantly fabric, reflecting the city's textile heritage. These cloth streamers reach lengths of more than ten meters and incorporate elaborate three-dimensional ornaments at the top, suspended high above the shopping arcades in dense canopies of color. Each major shop or business contributes its own streamer, designed and assembled over the preceding year. A formal competition runs throughout the festival, with local residents voting on their favorites and prizes awarded to the most outstanding displays. This competitive element has driven the artistry of the streamers to extraordinary heights, with leading shops investing significant resources in creating works that combine traditional Tanabata themes with contemporary design innovations.

Beyond the decorations, the festival features an extensive program of parades and performances along Honmachi Street, the main commercial thoroughfare. The schedule includes costume parades featuring participants in elaborate handmade outfits, the Ichinomiya Odori dance parade that brings together hundreds of participants in matching yukata, beauty pageants selecting Tanabata princesses who serve as festival ambassadors, and continuous stage events featuring local performers and visiting artists. Schools, civic associations, businesses, and neighborhood groups all participate, creating an inclusive atmosphere that engages residents of all ages.

The culinary offerings at Ichinomiya Tanabata showcase the rich food culture of the Nagoya metropolitan area, of which Ichinomiya forms part. Hundreds of food stalls line the festival routes, offering signature regional dishes including miso nikomi udon, the hearty wheat noodle soup simmered in red bean miso broth, hitsumabushi grilled eel served over rice with multiple eating styles, miso katsu pork cutlet topped with the region's distinctive sweet bean paste, kishimen flat wheat noodles, and kushikatsu skewered fried foods.

Access to the festival is exceptionally convenient. JR Owari-Ichinomiya Station and the adjacent Meitetsu Ichinomiya Station both lie within a three-minute walk of the central festival area. From Nagoya Station, Ichinomiya can be reached in approximately twelve minutes by either the Meitetsu line or the JR Tokaido Main Line, making the festival an easy addition to any Nagoya-area itinerary. The festival also serves as a springboard for broader exploration of Aichi and Gifu attractions, including the original wooden tenshu of Inuyama Castle, the National Treasure festival floats of the nearby Inuyama Festival, and the cormorant fishing demonstrations along the Nagara River in Gifu City.""",
    },
    {
        "qid": "Q3698846",
        "slug_ja": "onbashira-matsuri",
        "slug_en": "onbashira-matsuri",
        "manual_content_ja": """御柱祭は、長野県諏訪地域の諏訪大社で寅年と申年の7年に一度（数え年の7年・実際は満6年間隔）開催される神事であり、日本三大奇祭の一つに数えられる天下の大祭である。山中から切り出した樅の大木16本を、氏子たちの手と組織された曳行隊によって諏訪大社の上社本宮・上社前宮・下社春宮・下社秋宮の四社の社殿四隅に建て替える壮大な行事で、約1,200年以上の歴史を持つ諏訪信仰の中核をなす。次回開催は2028年（令和10年・申年）の春から夏にかけて予定されている。

御柱祭の起源は古く、平安時代初期の804年（延暦23年）の桓武天皇の時代には既に行われていたとの記録が残る。樹齢150年を超える樅の大木を山から切り出し、これを神の依り代として社殿の四隅に建てることで、社殿の御神威を更新するという信仰に基づく。柱は長さ約17メートル、直径約1メートル、重さ約12トンに達する巨木で、これを人力のみで山から里へ、そして社殿まで運搬する過程そのものが祭礼の中心となる。

最大の見どころは「木落とし」と「川越し」である。上社の木落としは茅野市の木落とし坂で、下社は下諏訪町の木落とし坂で行われ、約30度の急斜面を巨木に氏子たちが乗ったまま一気に滑り落とす。命がけの神事として知られ、過去には死傷者も出ているが、それでも地元の若者にとって御柱に乗ることは生涯の名誉とされる。上社の川越しは宮川を渡って柱を運ぶ神事で、冷たい川水に浸かりながら大勢で柱を曳き渡す光景は壮観である。

里曳きの段階では、各地区の氏子が法被姿で「ヨイサー、ヨイサー」の掛け声とともに柱を曳き、ラッパ隊の音色や木遣り歌が街道に響く。沿道では家々が屋台を出し、地元の郷土料理や酒を振る舞う。一般観光客も限定的に曳行に参加できる区間があり、地元の氏子と一体となって日本最大級の神事を体験できる貴重な機会となる。

会場は諏訪市・茅野市・岡谷市・下諏訪町・諏訪郡富士見町の5市町にまたがる広範囲で、上社木落とし会場へは中央自動車道諏訪南インターから、下社木落とし会場へはJR下諏訪駅から徒歩約25分。御柱祭年以外でも諏訪大社四社めぐり、諏訪湖、霧ヶ峰高原、八ヶ岳など信州中央部の観光地が充実しており、2028年の次回開催を待つ間も訪れる価値が高い地域である。""",
        "manual_content_en": """The Onbashira Festival, held in the Suwa region of Nagano Prefecture, is one of the most spectacular and dangerous traditional festivals in Japan and is widely counted among the country's three great unconventional festivals. Conducted once every seven years by the traditional Japanese counting system—meaning an actual interval of six years—it takes place during the Year of the Tiger and the Year of the Monkey of the East Asian zodiac. The festival centers on the cutting, transportation, and ceremonial erection of sixteen massive fir trees at the four shrines of the Suwa Taisha complex, an act believed to renew the spiritual power of the shrines. The next iteration is scheduled for spring through summer of 2028, the upcoming Year of the Monkey.

The festival's origins reach back more than 1,200 years. Documents indicate that the practice was already established by 804 CE during the reign of Emperor Kanmu in the early Heian period, and many scholars believe its roots extend further into prehistoric mountain worship traditions that long predated the formalization of Shinto. The four shrines of Suwa Taisha—Kamisha Honmiya, Kamisha Maemiya, Shimosha Harumiya, and Shimosha Akimiya—are among the oldest in Japan, with Suwa Taisha itself considered the head shrine of the more than ten thousand Suwa shrines scattered across the nation. The Suwa deity is associated with martial valor, agriculture, and the protection of travelers, and the Onbashira ritual serves to refresh the deity's presence at each shrine.

Each onbashira pillar is a single fir tree, selected from sacred mountain forests, measuring approximately seventeen meters in length, one meter in diameter, and weighing around twelve tons. Following ceremonial felling using traditional axes, the logs are transported entirely by human effort across distances of more than ten kilometers from the mountains to the shrine grounds. The transport is carried out by thousands of community members organized into parishes corresponding to specific neighborhoods, each responsible for designated pillars and segments of the journey.

The festival's most dramatic events are the kiotoshi, or log drop, and the kawagoshi, or river crossing. The kiotoshi takes place at designated steep slopes—one for the upper shrines in Chino City and one for the lower shrines in Shimosuwa Town. Each slope descends at approximately thirty degrees, and the logs are sent careening down these gradients with parishioners riding atop the massive trees. The participants cling to ropes attached to the logs, attempting to maintain their positions as the tons of wood plunge downward at increasing speed. The ride is genuinely life-threatening; fatalities and serious injuries have occurred in past festivals, and the choice to ride an onbashira pillar is considered a defining honor in the life of a Suwa region man. The kawagoshi, conducted for the upper shrine pillars, requires the parishioners to drag their logs across the cold waters of the Miyagawa River, an arduous group effort that creates one of the festival's most photographed scenes.

After the dramatic transportation phase comes the satobiki, or town pulling, during which the logs are drawn through populated areas to the shrines themselves. Parishioners in matching happi coats pull the logs with cries of "Yoisa, yoisa!" while specialized brass bands play marching tunes and traditional kiyari folk songs ring out along the route. Households along the path set up small stalls offering local foods, sake, and refreshments to the workers and spectators, transforming the towns into spontaneous festival spaces. Tourists may participate in certain designated segments of the pulling, providing visitors with the rare opportunity to take part directly in one of Japan's largest religious observances.

The festival is staged across a wide area encompassing the cities of Suwa, Chino, Okaya, and the towns of Shimosuwa and Fujimi in the Suwa region. The upper shrine log drop site can be reached from the Suwaminami interchange of the Chuo Expressway, while the lower shrine site is approximately twenty-five minutes on foot from JR Shimosuwa Station. Visitors during non-festival years can still appreciate the four shrines through a traditional pilgrimage circuit, and the broader Suwa region offers extensive attractions including Lake Suwa, the alpine plateaus of Kirigamine, and the dramatic peaks of the Yatsugatake mountains, making the area a worthwhile destination throughout the seven-year cycle between festivals.""",
    },
    {
        "qid": "Q6920834",
        "slug_ja": "mount-fuji-jazz-festival",
        "slug_en": "mount-fuji-jazz-festival",
        "manual_content_ja": """マウント・フジ・ジャズ・フェスティバルは、山梨県の富士急ハイランド特設会場で1986年から1998年まで毎年8月に開催された国際的ジャズフェスティバルであり、日本のジャズ史において最も重要な野外音楽イベントの一つとして記憶されている。富士山の壮大な景観を背景に、世界トップクラスのジャズミュージシャンが一堂に会したこの祭典は、最盛期には3日間で約8万人を動員し、ニューポート・ジャズ・フェスティバルやモントルー・ジャズ・フェスティバルと並ぶアジア最大級のジャズイベントとして国際的な評価を得た。

フェスティバルは、米国のブルーノート・レコードの創設に関わったプロデューサー、ジョージ・ウェインが手がけた「ニューポート・ジャズ・フェスティバル」のフォーマットを富士山麓に移植する形で始まった。日本企業の協賛を得て、富士急ハイランドという既存の大規模娯楽施設を会場として活用することで、宿泊・交通・観光のインフラを一体化した稀有なフェスティバルが実現した。1986年の第1回には、マイルス・デイビス、ハービー・ハンコック、ウィントン・マルサリス、ソニー・ロリンズなど、ジャズ界の頂点に立つアーティストが集結し、その後12年間にわたってジャズ史を彩る伝説的な公演が次々と繰り広げられた。

特に象徴的とされるのが、1986年の第1回フェスティバルにおけるマイルス・デイビスの公演である。当時60歳を迎えていたデイビスは、本フェスティバルで「TUTU」期の革新的な電子ジャズを披露し、富士山を背景にしたステージで演奏する姿は写真集や記録映像として今も語り継がれる。スタン・ゲッツ、デイヴ・ブルーベック、ディジー・ガレスピー、エラ・フィッツジェラルド、サラ・ヴォーン、カウント・ベイシー楽団など、20世紀後半のジャズの巨匠たちが軒並み出演し、若手・中堅ミュージシャンにとっても登竜門となる重要な舞台となった。

会場となった富士急ハイランドは、富士五湖の一つである河口湖と山中湖の中間に位置し、晴天時には会場のメインステージから雄大な富士山を直接望むことができた。3日間にわたり3つのステージで終日演奏が繰り広げられ、夜には湖畔の宿泊施設で出演者と聴衆が交流する場も生まれた。日本のジャズシーンが世界基準と直接接続する機会として、また当時の日本のバブル期の文化的豊かさを象徴する出来事として、本フェスティバルは今も多くのジャズファンの記憶に深く刻まれている。

1998年の終了から長い時を経た現在、富士急ハイランドは遊園地として営業を続け、富士山周辺は富士山世界遺産登録（2013年）を経て国際的観光地としての地位を確立した。フェスティバル自体は復活していないが、当時の記録映像や写真は富士急行の資料館やジャズ専門誌・書籍を通じて参照可能で、日本のジャズ文化を学ぶ上で欠かすことのできない歴史的事象として位置づけられている。富士山観光と合わせて当時のフェスティバル史跡を巡る愛好家も少なくない。""",
        "manual_content_en": """The Mount Fuji Jazz Festival was an internationally renowned outdoor jazz festival held annually each August from 1986 to 1998 at the Fuji-Q Highland amusement park in Yamanashi Prefecture, with the majestic peak of Mount Fuji serving as backdrop to one of Asia's most ambitious jazz events. During its peak years, the festival drew approximately eighty thousand attendees across its three-day run, earning international recognition alongside such storied festivals as the Newport Jazz Festival in the United States and the Montreux Jazz Festival in Switzerland. Although the festival ceased operations in 1998, it remains one of the defining cultural events of postwar Japanese music history and a touchstone for jazz enthusiasts worldwide.

The festival was conceived as a Japanese adaptation of the Newport Jazz Festival format pioneered by American producer George Wein, who served as artistic director and brought his extensive network of leading jazz musicians to the project. Corporate sponsorship from major Japanese companies, combined with the use of Fuji-Q Highland as venue, made it possible to integrate accommodation, transportation, and tourism infrastructure in ways that few other festivals could match. The result was a uniquely Japanese experience: world-class jazz performances staged with one of the world's most iconic natural landscapes as their visual backdrop.

The inaugural 1986 festival assembled a roster that read like a who's who of contemporary jazz, including Miles Davis, Herbie Hancock, Wynton Marsalis, and Sonny Rollins. Over the subsequent twelve years, the festival continued to attract the most significant figures in jazz, with appearances from such legends as Stan Getz, Dave Brubeck, Dizzy Gillespie, Ella Fitzgerald, Sarah Vaughan, the Count Basie Orchestra, Oscar Peterson, Chick Corea, and Pat Metheny. The festival also served as an important showcase for emerging Japanese jazz artists, providing them international exposure alongside the established stars from the United States and Europe.

Among the most legendary performances was Miles Davis's appearance at the inaugural 1986 festival. At sixty years old and in the midst of his late-career exploration of electronic jazz fusion documented on the album Tutu, Davis delivered a performance that crystallized the moment when jazz's most influential living figure intersected with one of the most visually striking concert settings in the world. Photographs and video recordings of Davis playing with Mount Fuji visible behind him have become iconic images of late-twentieth century jazz history, reproduced in countless retrospectives and exhibitions.

Fuji-Q Highland is situated between Lake Kawaguchi and Lake Yamanaka, two of the celebrated Fuji Five Lakes, providing a location where the snow-capped or sometimes cloud-wrapped silhouette of Mount Fuji could be appreciated directly from the festival grounds on clear days. Three stages operated concurrently during the festival period, with continuous programming from afternoon into late evening. Following performances, musicians and audiences would mix at the lakeside accommodations that surrounded the venue, creating opportunities for the kind of informal artist-audience interaction that has long been considered part of jazz culture but is rarely possible at festivals of this scale.

The festival's cultural significance extended beyond its immediate musical impact. For Japanese jazz musicians and fans, it provided direct access to the international jazz scene at a level previously available only through expensive overseas travel. For visiting international musicians, it offered exposure to Japanese audiences known for their deep appreciation and meticulous attention to musical detail. The festival was also emblematic of the cultural ambitions of Japan during its economic peak in the late 1980s and early 1990s, when major corporate sponsors could underwrite cultural events at scales that proved difficult to sustain after the economic transitions of subsequent decades.

After the festival's conclusion in 1998, Fuji-Q Highland continued operations as an amusement park, while the broader Mount Fuji area achieved UNESCO World Heritage status in 2013 and consolidated its position as an international tourist destination. The festival itself has not been revived, but recordings, photographs, and printed materials documenting its thirteen-year run remain available through the Fuji Express corporate archives, jazz specialty magazines, and academic studies of Japanese music history. For visitors interested in the cultural geography of Japanese jazz, the area around Mount Fuji retains layers of meaning that connect the natural sublime with one of the twentieth century's most important international musical convergences, making a visit a worthwhile pilgrimage even decades after the music has stopped.""",
    },
    {
        "qid": "Q86740734",
        "slug_ja": "shibare-festival",
        "slug_en": "shibare-festival",
        "manual_content_ja": """しばれフェスティバルは、北海道足寄郡陸別町で毎年2月の第1週目の土日に開催される極寒体験イベントであり、「日本一寒い町」を自称する陸別町の独自性を最大限に活かしたユニークな冬の祭典である。「しばれる」とは北海道弁で「凍えるほど寒い」を意味し、その名の通り氷点下20度を下回ることも珍しくない極寒の屋外で繰り広げられる耐寒イベントが、全国の冬好きや寒冷地マニアを惹きつけている。

陸別町は北海道東部の十勝管内に位置する人口約2,300人の小さな町で、その地理的条件から北海道内で最も低い気温を記録することが多い。観測史上の最低気温は1978年に記録された氷点下31.5度に達し、町は「日本一寒い町」をブランド化することで町興しを進めてきた。しばれフェスティバルは1985年（昭和60年）に始まったこの町興し戦略の中核イベントで、町民総出で運営する手作りの祭りとして40年近い歴史を持つ。

最大の見どころは「人間耐寒テスト」である。参加者は屋外特設会場で氷で囲まれた個別ブースに入り、寝袋一つで一晩を過ごす耐寒チャレンジに挑戦する。氷点下20度を下回る環境下で深夜から早朝までを過ごし、無事生還した参加者には認定証が授与される。完走率は天候により変動するが、近年では参加者の安全管理が大幅に強化され、医療スタッフが常駐するなど安全な極限体験として運営されている。

会場では他にも様々な氷の催しが繰り広げられる。氷でできた巨大なジャンボすべり台、氷柱でできたディナーレストラン「氷点下の食堂」、ダイヤモンドダストの観察会、巨大ジャンプ台付きスノーモービル体験など、極寒地ならではの体験が用意されている。夜には大規模な花火大会も開催され、冷気で空気が澄んだ漆黒の夜空に上がる花火は息を呑むほどに美しい。

陸別町は鉄道がなく公共交通機関のアクセスは限られるため、訪問は車（レンタカー）または札幌・帯広からの臨時バスツアー利用が一般的である。十勝平野の農村風景、阿寒摩周国立公園、屈斜路湖、然別湖など道東の自然と組み合わせた旅程が組みやすい。極寒地への訪問となるため、最強の防寒装備（雪山登山レベル）と万全の健康管理が必須となるが、その分得られる体験は他のどの祭りでも代替できない希少なものである。""",
        "manual_content_en": """The Shibare Festival is a distinctive winter event held annually on the first weekend of February in the town of Rikubetsu in Hokkaido's Tokachi region, celebrating the community's self-proclaimed status as Japan's coldest town. The word shibare derives from Hokkaido dialect and means freezing cold to the point of paralyzing the body, an apt description of the conditions visitors can expect during a festival held in temperatures that routinely drop below minus twenty degrees Celsius. What began as a small community initiative has grown into one of Japan's most unusual festivals, drawing winter enthusiasts and extreme weather aficionados from across the country and increasingly from abroad.

Rikubetsu is a small town of approximately 2,300 residents located in inland eastern Hokkaido, surrounded by the Tokachi agricultural plains. Its specific geographic situation—an inland basin with cold air drainage from surrounding hills, far from the moderating influence of any ocean, and at relatively high elevation—creates conditions ideal for the extreme cold that defines its identity. The town holds the modern observational record for the lowest temperature ever recorded in Hokkaido, minus thirty-one point five degrees Celsius, set in 1978. While Asahikawa and a few other Hokkaido locations contest various coldness titles, Rikubetsu has successfully branded itself as "the coldest town in Japan" through consistent marketing and tourism development efforts spanning four decades.

The Shibare Festival began in 1985 as the centerpiece of this branding strategy and has continued essentially uninterrupted since then. The festival is organized almost entirely by community volunteers, with the small town's population mobilizing collectively to construct, staff, and host an event that requires extensive preparation in some of the harshest conditions any festival anywhere faces.

The festival's most famous event is the Human Cold Endurance Test, an overnight challenge in which participants spend the night in individual ice-walled enclosures equipped only with a sleeping bag. Beginning in the early evening, participants settle into their ice booths and must survive through the night until early morning. Temperatures inside the enclosures typically range between minus fifteen and minus twenty-five degrees Celsius, depending on weather conditions during a given year's festival. Participants who complete the challenge receive an official certificate of endurance, while those who must withdraw early can leave at any point through professional support staff stationed throughout the test area. In recent years, safety protocols have been substantially strengthened, with medical personnel maintaining continuous presence and detailed health screening required before participation, transforming what might sound like a reckless stunt into a carefully managed extreme experience.

Beyond the endurance test, the festival features an array of activities designed to showcase the unique characteristics of extreme cold environments. A massive ice slide constructed from blocks of frozen water provides an exhilarating descent that lasts only seconds at the speeds achievable on the frictionless ice surface. The Below-Zero Cafeteria operates within structures built entirely from ice pillars and blocks, serving warm meals to diners seated at ice tables, with the contrast between hot food and frigid surroundings creating an unforgettable sensory experience. Diamond dust viewing sessions take advantage of one of the rarest atmospheric phenomena, in which ice crystals suspended in extremely cold air refract light into glittering patterns that have to be witnessed in person to be appreciated. Snowmobile experiences featuring purpose-built ramps allow visitors to attempt small jumps under expert supervision, and various other cold-weather activities operate throughout the day.

Evening activities culminate in a substantial fireworks display, with explosions illuminating the crystalline night air. The clarity of the atmosphere at such low temperatures, combined with the absence of light pollution that characterizes the surrounding rural areas, creates fireworks viewing conditions that connoisseurs consider among the finest in Japan, with each burst rendered in sharp detail against the absolute darkness.

Access to Rikubetsu requires careful planning. The town has no rail service, and the nearest major transit hubs are Obihiro to the south and Kitami to the north, both more than an hour away by car. Most visitors arrive either by rental car from these cities or via organized bus tours that run from Sapporo and Obihiro specifically during festival weekend. The remote location places the festival amid the wider attractions of eastern Hokkaido, allowing combinations with visits to Akan-Mashu National Park, Lake Kussharo, Lake Shikaribetsu where unique winter activities also operate, and the broad agricultural landscapes of the Tokachi plain. Visitors must come prepared for cold beyond what most travelers ever encounter, with mountain-climbing-grade insulated clothing, multiple layers, hand and foot warmers, face protection, and careful attention to their own physical condition essential prerequisites for participation in this most singular of Japanese winter festivals.""",
    },
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
for item in ITEMS:
    cur.execute("""
        UPDATE festivals
        SET slug_ja=?, slug_en=?, manual_content_ja=?, manual_content_en=?, status='drafted'
        WHERE qid=?
    """, (item["slug_ja"], item["slug_en"], item["manual_content_ja"], item["manual_content_en"], item["qid"]))
    print(f"[OK] {item['qid']} updated to drafted (rows: {cur.rowcount})")
conn.commit()

print("\n=== Part 1 検証 ===")
cur.execute(f"""
    SELECT qid, label_ja, status, LENGTH(manual_content_ja), LENGTH(manual_content_en)
    FROM festivals
    WHERE qid IN ({",".join(f"'{i['qid']}'" for i in ITEMS)})
""")
for row in cur.fetchall():
    print(f"[VERIFY] {row[0]} {row[1]} status={row[2]} len_ja={row[3]} len_en={row[4]}")
conn.close()
