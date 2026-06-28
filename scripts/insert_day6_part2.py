#!/usr/bin/env python3
"""Insert festivals #66-70 (Phase 1c day 6 part 2)"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q1033843",
        "slug_ja": "pacific-music-festival",
        "slug_en": "pacific-music-festival",
        "manual_content_ja": """パシフィック・ミュージック・フェスティバル（PMF）は、北海道札幌市で毎年7月から8月にかけて約1ヶ月間にわたって開催される国際教育音楽祭であり、世界三大教育音楽祭の一つに数えられる。20世紀を代表する指揮者・作曲家のレナード・バーンスタインが、若手音楽家育成を理念として1990年に創設し、今もその精神を継承する若き才能育成の場として国際的に高く評価されている。

PMFの創設は1990年（平成2年）にさかのぼる。米国のタングルウッド音楽祭（ボストン交響楽団主催）、ドイツのシュレスヴィヒ・ホルシュタイン音楽祭と並ぶ「世界三大教育音楽祭」を構想したバーンスタインが、晩年に手がけた最後の大プロジェクトとして札幌で開催することを選んだ。創設の前年に来日して札幌芸術の森を訪れたバーンスタインは、自然と都市が共存する札幌の環境と、北海道民の音楽への熱意に深く感銘を受け、ここを教育音楽祭の地として選定した。バーンスタインは創設の年に72歳で逝去したが、その精神は札幌市と国際的な音楽家コミュニティによって今日まで継承されている。

PMFの中核はPMFオーケストラと呼ばれる若手音楽家のためのオーケストラである。世界中から書類審査とオーディションを経て選ばれた20歳代から30歳代前半の若手演奏家約100名が、約1ヶ月間札幌に滞在し、世界トップクラスの指揮者・ソリスト・室内楽奏者の指導を受けながら集中的に研鑽を積む。PMFアカデミーと呼ばれるこの教育プログラムでは、ボストン交響楽団、ベルリン・フィルハーモニー、ウィーン・フィルハーモニーなどの首席奏者がプロフェッサーとして招かれ、若手と直接共演しながら指導を行う密度の高い学びの場が提供される。

主会場である札幌芸術の森野外ステージは、自然林に囲まれた約7,500人収容の野外コンサート会場で、夏の札幌の心地よい気候のなか開放的な雰囲気で本格的なオーケストラ演奏が楽しめる。札幌コンサートホールKitara、札幌市民交流プラザのhitaru、北海道立札幌芸術の森美術館エリアなど市内各所でも演奏会が開催され、約1ヶ月間にわたって市民・観光客が日常的にクラシック音楽に触れられる稀有な機会となる。チケット価格も比較的手頃で、芸術の森のピクニックコンサートは家族連れにも人気がある。

期間中はPMFオーケストラのコンサートに加えて、室内楽演奏会、PMFアンサンブル、招聘アーティストによるソロリサイタル、子ども向けの公開リハーサルなど多様なプログラムが組まれる。札幌交響楽団との合同演奏会、世界的な指揮者による特別演奏会など、年によって魅力的な企画が並ぶ。

アクセスは札幌市営地下鉄南北線真駒内駅からバスで約15分、JR札幌駅からは観光バスツアーや直行バスも運行される。札幌観光の定番である大通公園、すすきの、円山動物園、北海道大学植物園、藻岩山ロープウェイなどと組み合わせれば、夏の北海道を音楽と自然の両面から堪能する充実した旅程が構成できる。""",
        "manual_content_en": """The Pacific Music Festival, known internationally as PMF, is one of the world's three great educational music festivals, held annually for approximately one month from July through August in Sapporo, Hokkaido. Founded in 1990 by the legendary American conductor and composer Leonard Bernstein as his final major project, PMF continues to serve as a leading platform for the development of young classical musicians from around the world. Alongside the Tanglewood Music Festival in the United States and the Schleswig-Holstein Music Festival in Germany, it forms the global triumvirate of festivals specifically dedicated to advanced music education.

The festival's origins trace to Bernstein's vision of creating an Asian counterpart to the educational programs he had championed throughout his career, particularly his association with Tanglewood. Bernstein visited Japan in 1989, and during a stay at Sapporo's Geijutsu no Mori, or Sapporo Art Park, he experienced firsthand the harmony of urban culture and surrounding nature that characterizes Hokkaido's capital. Equally compelling was his sense of the genuine enthusiasm for classical music among Hokkaido residents and Japanese audiences more broadly. These impressions led him to select Sapporo as the site for what he envisioned as a transformational long-term institution. Tragically, Bernstein died at age seventy-two later in 1990, the same year the festival was inaugurated, but the City of Sapporo and the international classical music community have continued and expanded the project through subsequent decades.

The heart of PMF is the PMF Orchestra, an ensemble assembled each year from young professional musicians selected through international application and audition. Approximately one hundred players in their twenties and early thirties travel to Sapporo from around the world to participate in an intensive program of rehearsals, master classes, and public performances over the festival period. The educational component, known as the PMF Academy, brings in principal players and section leaders from the world's leading orchestras—the Boston Symphony Orchestra, Berlin Philharmonic, Vienna Philharmonic, New York Philharmonic, and Chicago Symphony Orchestra have all been regular contributors—who serve as faculty members teaching individual lessons, sectional rehearsals, and chamber music coachings. Many of the festival's faculty members maintain decades-long associations with PMF, returning year after year and creating a sense of community across generations of participants.

The festival's principal venue is the Sapporo Art Park Outdoor Stage, an open-air concert facility surrounded by natural forest with seating for approximately seventy-five hundred attendees. The Hokkaido summer climate—mild compared to the rest of Japan and notably free of the rainy season that disrupts outdoor events further south—creates ideal conditions for outdoor orchestral performance. Audiences spread blankets on the lawn or take seats in the covered grandstand, often arriving early to picnic and enjoy the surrounding forest. Major concerts at this venue have included full performances of works by Mahler, Shostakovich, Stravinsky, and Bernstein himself, with the resonance of the forest providing acoustic character unique among major orchestral venues.

Additional performances take place at Sapporo Concert Hall Kitara, a smaller indoor venue purpose-built for classical performances with acoustic design widely admired internationally, as well as at Hitaru in the Sapporo Citizens Exchange Plaza and various other venues throughout the city. The geographic distribution of performances throughout central and suburban Sapporo means that the festival pervades the city for its month-long duration, with concerts available nearly every day for both committed enthusiasts and casual visitors interested in sampling classical performance.

The annual program extends well beyond traditional orchestral concerts. Chamber music recitals featuring small groupings of academy participants and faculty showcase the intimate side of the classical repertoire. The PMF Ensemble, composed of selected academy members, presents focused programs of contemporary and standard works. Visiting artists provide solo recitals that often serve as Japanese-market debuts for emerging international careers. Open rehearsals for children invite young audiences to observe the actual process by which an orchestra prepares a major work, demystifying the world of classical performance and building the next generation of audience members. Joint concerts with the Sapporo Symphony Orchestra create opportunities for the visiting academy members to perform alongside the professional ensemble that anchors Hokkaido's classical music scene year-round.

Access to the main outdoor venue requires some planning but is straightforward. From Makomanai Station on the Sapporo Subway Namboku Line, a public bus reaches Sapporo Art Park in approximately fifteen minutes. From JR Sapporo Station, both organized tour buses and direct shuttle services operate during the festival period. The festival pairs naturally with broader exploration of summer Sapporo, including the famous Odori Park where the city's beer garden operates simultaneously, the entertainment district of Susukino, the Maruyama Zoo, the Hokkaido University Botanical Garden, and the cable car ascending Mount Moiwa for panoramic views of the city. For visitors seeking to combine classical music enthusiasm with Hokkaido's exceptional summer climate and culinary offerings, PMF provides an experience that no other festival on the Asian classical music calendar can match.""",
    },
    {
        "qid": "Q105338690",
        "slug_ja": "kibune-matsuri-manazuru",
        "slug_en": "kibune-matsuri-manazuru",
        "manual_content_ja": """貴船まつりは、神奈川県足柄下郡真鶴町の貴船神社で毎年7月27日と28日に執り行われる例大祭であり、日本三大船祭りの一つに数えられる海上神事である。相模湾に面した小さな漁師町を舞台に、豪華絢爛な装飾を施した小早船と櫂伝馬船が湾内を渡御する壮大な海上絵巻が展開され、約400年の歴史を持つ真鶴の伝統文化の精華として国の重要無形民俗文化財に指定されている。

貴船神社は平安時代初期の889年（寛平元年）の創建と伝わる古社で、京都の貴船神社と並ぶ水の神・航海安全の神として、相模湾の漁業者や海運業者から篤い信仰を集めてきた。真鶴半島の漁業集落に住む人々にとって、貴船神社は文字通り生活の中心であり、年に一度の例大祭は漁師たちの一年の総決算とも言える最も重要な行事として位置づけられてきた。

祭りの最大の見どころは、7月28日に行われる海上渡御である。小早船と呼ばれる装飾船2隻と、櫂伝馬船3隻が、真鶴港から岩漁港までの約3キロメートルの海上を、約4時間かけて優雅に進む。小早船は江戸時代の軍船を模した装飾船で、船体全体に色鮮やかな幟・提灯・水引・装飾品が施され、船上では神楽舞や囃子が奉納される。櫂伝馬船は櫂を使う伝統的な漕ぎ船で、若衆が揃いの法被姿で激しく櫂を漕ぎ進む様は勇壮そのものである。

陸上では、各町内会の山車「鹿島踊」が町中を練り歩く。鹿島踊は東関東から伝わった伝統舞踊で、約30名の踊り手が円形になって踊る独特の様式が特徴で、神奈川県無形民俗文化財に指定されている。鹿島踊と海上渡御が真鶴の小さな漁師町で同時に繰り広げられる光景は、日本の港町の祭礼文化の集大成といえる。

真鶴町は古くからの漁師町であり、祭礼期間中は地元の海の幸が屋台や民家で振る舞われる。地魚の刺身、新鮮なサザエやアワビ、ところてんなど、相模湾の海の恵みが豊富に味わえる。アクセスはJR東海道本線真鶴駅から徒歩約20分、または無料シャトルバスで約5分。東京から東海道線快速で約100分とアクセスもよく、箱根温泉郷や小田原城、湯河原温泉など神奈川県西部の観光地と組み合わせれば、東京近郊で本格的な海上祭礼を体験できる貴重な旅程が構成できる。""",
        "manual_content_en": """The Kibune Matsuri, held annually on July 27 and 28 in the fishing town of Manazuru in Kanagawa Prefecture, is one of Japan's three great boat festivals and a Nationally Designated Important Intangible Folk Cultural Property. The festival centers on a spectacular maritime procession in which elaborately decorated boats traverse the calm waters of Sagami Bay, accompanied by traditional dances and music performed both at sea and on land. With approximately four hundred years of continuous history, the festival represents the pinnacle of maritime festival culture in the broader Kanto region and provides one of the most visually striking experiences available to visitors interested in Japanese folk traditions.

Kibune Shrine, the focal point of the festival, traces its founding to 889 CE during the early Heian period. The shrine is associated with the deity of water and maritime safety, paralleling the more famous Kibune Shrine in northern Kyoto from which it derives part of its name and divine connection. For the fishing communities of the Manazuru Peninsula, which juts into Sagami Bay along the western edge of the broader Sagami Plain, Kibune Shrine has historically served as the spiritual center of community life. Manazuru's economy depended for centuries on fishing in the rich waters of the bay, and the annual festival represented both a formal expression of gratitude for the year's catch and a request for safe and abundant seas in the year to come.

The festival's most distinctive component is the maritime procession conducted on July 28, the second and main day. Two kobaya-bune, or small ship-style decorated vessels, and three kaidenma-bune, or oared transport boats, depart from Manazuru Harbor and proceed approximately three kilometers along the coast to Iwa Harbor over the course of about four hours. The kobaya-bune are modeled on Edo-period military vessels and are adorned across their entire surfaces with brilliantly colored banners, paper lanterns, ceremonial cords, and ornamental fittings, creating mobile temples that progress slowly across the bay surface. On board these vessels, sacred kagura dances are performed and traditional festival music plays continuously, the sounds carrying across the water to spectators gathered along the coastline.

The kaidenma-bune, by contrast, demonstrate the practical maritime skills that defined the lives of Manazuru's fishermen for centuries. Crewed by young men in matching happi coats, these vessels are propelled by team of rowers operating the long oars in precise coordination. The physical intensity of the rowing, the rhythmic shouts of the crew, and the powerful synchronized movements create an entirely different mood from the contemplative procession of the decorated vessels, capturing the strength and discipline that historically characterized fishing communities along Japan's coasts.

On land, simultaneous celebrations unfold throughout the town. Each neighborhood association produces a portable shrine and decorative float, with the most distinctive being the dashi associated with the Kashima Odori, a traditional dance form designated a Cultural Property of Kanagawa Prefecture. The Kashima Odori originated in the Kashima region of eastern Japan and was transmitted to Manazuru centuries ago, where it has been preserved with remarkable fidelity. Approximately thirty dancers form a circle, executing precise movements while wearing distinctive costumes that have changed little since the Edo period. The simultaneous performance of land-based and sea-based ritual elements creates an immersive experience in which visitors can move between vantage points to appreciate different dimensions of the festival.

Manazuru's identity as a fishing town shapes the culinary experience available during the festival. Food stalls and private homes alike serve fresh local catches throughout the festival period. Sashimi prepared from fish landed that very morning, fresh sea snails and abalone, seaweed dishes characteristic of the Sagami coast, and tokoroten gelatin made from local seaweeds offer visitors direct access to the maritime food culture that the festival itself celebrates. Local sake breweries and small confectioners also typically operate stalls during the festival.

Access to Manazuru is convenient despite the town's small size. JR Manazuru Station on the Tokaido Main Line lies approximately twenty minutes on foot from the festival area, with free shuttle buses available reducing the journey to about five minutes during peak festival hours. From Tokyo, Manazuru can be reached in roughly one hundred minutes by Tokaido Line rapid service, making the festival accessible as a day trip from the capital. The wider area offers exceptional opportunities to combine festival viewing with broader explorations of western Kanagawa, including the renowned hot springs of Hakone and Yugawara, the historic Odawara Castle, and the dramatic coastal scenery of the Manazuru Peninsula itself, where preserved coastal forests, fishing villages, and dramatic rocky outcroppings provide one of the most photogenic landscapes within day-trip reach of Tokyo.""",
    },
    {
        "qid": "Q106943951",
        "slug_ja": "asamushi-onsen-nebuta",
        "slug_en": "asamushi-onsen-nebuta",
        "manual_content_ja": """浅虫温泉ねぶた祭りは、青森県青森市の浅虫温泉地区で毎年8月初旬に開催される夏祭りであり、青森ねぶた祭の前夜祭的な位置づけで温泉街全体が幻想的なねぶたの灯りに包まれる、青森を代表する温泉地ならではの個性的な祭礼である。青森市中心部のねぶた祭りと比較すると規模は小さいが、海と温泉と山に囲まれた立地ならではの親密な雰囲気と、温泉客と地元住民が一体となって楽しむ手作り感が魅力となっている。

浅虫温泉は青森市東部の陸奥湾に面した古い温泉地で、平安時代の886年（仁和2年）に円融天皇の勅命で開発されたとの伝承を持つ。江戸時代には弘前藩主の湯治場として整備され、明治期には津軽鉄道や東北本線の開通によって東北を代表する温泉地の一つとなった。浅虫温泉ねぶた祭りは、本祭である青森ねぶた祭（8月2日-7日）の前後に開催される地域版として発展し、温泉街の各旅館・商店・町内会が手作りのねぶたを出すアットホームな祭りとして親しまれている。

最大の見どころは、温泉街のメインストリートを練り歩くねぶた行列である。青森ねぶた祭の巨大なねぶたほどではないが、各町内会や旅館組合が制作した中型・小型のねぶた約10基が、笛・太鼓・鉦の囃子と「ラッセラー、ラッセラー」の掛け声に乗って温泉街を進む。地元の子どもたちや浴衣姿の温泉客も気軽に列に加わってハネト（跳ね手）として参加でき、観光客と地元住民の境界が消える独特の一体感が生まれる。

会場周辺では地元の海の幸を中心とした屋台が並び、ホタテのバター焼き、イカ焼き、ウニの塩辛、津軽そばなど青森の郷土料理が楽しめる。浅虫温泉の旅館では祭り期間中、夕食後に旅館の浴衣のまま祭りに参加できる特別プログラムを組むところも多く、温泉と祭りを同時に堪能できる稀有な体験となる。

陸奥湾の眺望は浅虫温泉の最大の魅力で、温泉宿の客室や露天風呂から夕陽が湾を染める光景や、対岸の下北半島・夏泊半島を望める景色は他に代えがたい。アクセスは青森駅から青い森鉄道で浅虫温泉駅まで約25分、青森空港からは車で約40分。本祭の青森ねぶた祭との連泊で組み合わせるのが定番で、青森市中心部の壮大な大型ねぶたと浅虫温泉の親密な中小型ねぶたの両方を体験する旅程は、ねぶた文化の多層性を理解する上で理想的である。""",
        "manual_content_en": """The Asamushi Onsen Nebuta Festival is a summer celebration held in early August in the Asamushi Onsen district of Aomori City, providing an intimate counterpart to the world-famous Aomori Nebuta Festival held in the central city during the same week. While the main Aomori festival features enormous illuminated floats and crowds of more than two million visitors, the Asamushi version unfolds at human scale through the streets of a historic hot spring town, allowing visitors a more personal experience of nebuta culture combined with the relaxation of traditional Japanese hot spring lodging.

Asamushi Onsen lies on the eastern coastline of Aomori City, facing Mutsu Bay across a setting where mountains descend nearly to the sea and the hot springs emerge naturally from the foothills. The springs have been in use for over a thousand years, with traditions dating their development to 886 CE during the reign of Emperor Enyu in the Heian period. The town's modern incarnation began in the early Edo period when the Hirosaki domain established it as a recuperative bathing site for samurai, and the connection of the Tohoku Main Line in the Meiji period transformed Asamushi into one of the most accessible major hot spring destinations in northern Japan.

The Asamushi Onsen Nebuta Festival emerged as a localized expression of the broader nebuta culture that dominates Aomori summer. The main Aomori Nebuta Festival runs from August 2 through August 7, drawing international attention and crowds that overwhelm the city. Asamushi's version operates on a more accessible scale, staged before or alongside the main event, allowing residents and visitors to experience nebuta traditions without the logistical challenges of the main festival. Local inns, shops, and neighborhood associations each contribute small to medium-sized nebuta floats, building them through community efforts in the months leading up to the festival.

The festival's centerpiece is the procession of these floats through the main street of the hot spring town. Approximately ten illuminated floats progress along the route, each accompanied by musicians playing flutes, taiko drums, and small gongs, with participants calling out the famous "Rasse-ra, rasse-ra!" cheer that defines nebuta festivals throughout Aomori. The floats themselves depict scenes from Japanese mythology, historical battles, kabuki theatre, and contemporary popular culture, with internal lighting bringing the painted figures to life against the evening sky.

A distinctive feature of the Asamushi festival is the participation of visitors as haneto, or jumping dancers who follow the floats while performing energetic leaping movements. While the main Aomori festival requires haneto to register and wear specific costumes, the Asamushi version welcomes spontaneous participation. Hot spring guests can join the procession wearing the yukata cotton robes provided by their inns, creating a uniquely informal atmosphere in which the boundary between tourists and locals dissolves. The combination of a relaxed bath, evening meal, and immediate participation in a traditional festival is virtually impossible to find at the larger Aomori event.

Food stalls along the festival route showcase the maritime cuisine for which Aomori is renowned. Grilled scallops in butter, taking advantage of the abundant shellfish harvested from Mutsu Bay, are a particular specialty, along with grilled squid, salt-cured sea urchin, and the regional Tsugaru soba noodles. Local sake breweries and small craft vendors also operate during the festival, providing opportunities to sample regional alcoholic beverages and purchase traditional crafts that range from Tsugaru lacquerware to small wooden kokeshi dolls.

Many of the inns at Asamushi Onsen offer special festival programs in which guests can step directly from their evening bath into the procession, returning afterward to enjoy late evening soaks under the stars. This combination of hot spring relaxation and active festival participation creates an experience available nowhere else in Japan, blending two of the country's most cherished cultural traditions into a seamless summer evening.

The setting itself contributes significantly to Asamushi's appeal. Guest rooms and outdoor baths offer views across Mutsu Bay toward the distant Shimokita Peninsula and Natsudomari Peninsula, with sunsets coloring the bay in shifting tones of pink and gold. Inland from the town, the slopes of Mount Asamushi provide hiking opportunities and panoramic viewpoints, while the small fishing harbors along the coast offer glimpses of traditional maritime life largely unchanged for generations.

Access to Asamushi Onsen is convenient. From Aomori Station, the Aoimori Railway connects to Asamushi Onsen Station in approximately twenty-five minutes, with the festival area lying within easy walking distance. From Aomori Airport, the town can be reached by car in about forty minutes. The standard recommended itinerary combines the Asamushi festival with attendance at the main Aomori Nebuta Festival in central Aomori, allowing visitors to experience both the monumental scale of the urban event and the intimate community character of the hot spring town version. Together they provide a complete view of nebuta culture in its native Aomori context, demonstrating how a single festival tradition expresses itself at radically different scales according to community and location.""",
    },
    {
        "qid": "Q1072387",
        "slug_ja": "shichi-go-san",
        "slug_en": "shichi-go-san",
        "manual_content_ja": """七五三は、日本全国の神社で毎年11月15日（およびその前後の週末）に行われる、子どもの成長を祝う通過儀礼であり、地域祭礼ではなく全国的に共有される年中行事として千年以上の歴史を持つ。3歳・5歳・7歳の子どもが晴れ着を身にまとい、両親に伴われて氏神を祀る神社を参拝し、これまでの無事を感謝するとともに、これからの健やかな成長を祈願する。日本の家族文化と神道信仰が融合した最も身近な伝統行事の一つである。

七五三の起源は平安時代に遡る。当時の貴族社会では、子どもの成長過程における節目を儀式によって祝う習慣があり、3歳の「髪置きの儀」（剃り上げていた髪を伸ばし始める儀式）、5歳の「袴着の儀」（男児が初めて袴を着ける儀式）、7歳の「帯解きの儀」（女児がそれまでの紐付き着物から大人と同じ帯を結ぶ着物に変える儀式）が、それぞれ独立した儀式として行われていた。これらが江戸時代に庶民の間にも広がり、明治以降に「七五三」として統合された形で全国に定着した。

11月15日が選ばれた由来には諸説あるが、最も有力なのは江戸時代5代将軍徳川綱吉が病弱だった長男・徳松の健康祈願をこの日に行ったことに始まるとする説である。陰陽道で「鬼が出歩かない日（鬼宿日）」とされ、何事を行うにも吉日とされてきた背景もある。現代では11月15日にこだわらず、10月後半から11月にかけての都合のよい週末に分散して参拝するのが一般的になっている。

七五三参りの中心は神社での参拝である。子どもは女児なら華やかな着物（3歳は「被布」と呼ばれる短い羽織を着る装い、7歳は本格的な振袖と帯）を、男児なら袴姿で正装する。神社では祈祷を受けることが多く、神主が祝詞を奏上して子どもの健康と成長を神に願う。祈祷の後、神社から記念品として絵馬や御守りが授与され、家族写真の撮影、両親の実家への報告、外食での祝賀会など、家族全体で祝う一日となる。

七五三の名物として知られるのが「千歳飴」である。紅白の細長い棒状の飴で、千年生きるほどの長寿を願う縁起物として、神社や和菓子店で販売される。千歳飴の袋は鶴亀や松竹梅などの縁起のよい絵柄で装飾され、子どもがこれを大切に抱えて神社を歩く姿は、七五三の季節の風物詩として写真にも頻繁に登場する。

地域による違いも興味深い。北海道や東北地方では11月の寒さから10月中に参拝を済ませる家庭が多く、関西地方では男児を3歳と5歳、女児を3歳と7歳で祝う伝統が比較的厳格に守られている。一方、関東地方では男児は5歳のみ祝う家庭も増えており、現代の七五三は地域伝統と各家庭の事情に応じて柔軟に営まれている。

参拝に訪れる代表的な神社としては、東京の明治神宮、神田明神、湯島天満宮、京都の伏見稲荷大社、北野天満宮、大阪の住吉大社、太宰府天満宮など、各地の有名神社が知られる。地元の氏神（住んでいる地域を守る神社）に参拝するのが本来の姿であり、観光地として有名な神社よりも、地元の小さな神社で家族が静かに祈願する光景こそが、この通過儀礼の本質を表している。""",
        "manual_content_en": """Shichi-Go-San, literally meaning seven-five-three, is one of the most universally observed rites of passage in Japan, celebrated each November 15 and the surrounding weekends at Shinto shrines throughout the country. Unlike most entries in Japanese festival traditions, Shichi-Go-San is not a localized matsuri tied to a specific shrine or community but rather a nationally shared annual observance marking key developmental milestones in a child's life. Children of ages three, five, and seven dress in formal traditional clothing and visit Shinto shrines with their families to express gratitude for their growth thus far and to pray for continued health and well-being. The tradition combines Shinto religious observance with family celebration to produce one of the most cherished events in the Japanese year.

The historical origins of Shichi-Go-San reach back to the Heian period, when Japanese aristocratic society marked specific points in childhood with formal ceremonies. The three-year ceremony, called kamioki, marked the moment when a child who had been having their head shaved according to early childhood custom could begin to grow out their hair. The five-year ceremony, called hakamagi, celebrated a boy's first wearing of formal hakama trousers, signifying a step toward adult male identity. The seven-year ceremony, called obitoki, marked a girl's transition from wearing children's kimono with strings to formal kimono secured with the obi sash worn by adult women. These three originally independent ceremonies served different practical and symbolic purposes within aristocratic society.

During the Edo period, these aristocratic customs gradually spread to merchant and farming families, transforming from elite practices into broadly observed traditions. The unified term Shichi-Go-San emerged in the Meiji era, consolidating the three separate ceremonies into a single recognizable seasonal observance. November 15 became established as the standard date, although traditions vary regarding the precise origins of this particular calendar choice. The most common account attributes it to the fifth Tokugawa shogun Tsunayoshi, who held a prayer ceremony on that date in 1681 for his frail eldest son Tokumatsu, an event that subsequently influenced widespread adoption. The date also held favorable associations in traditional onmyodo cosmology as a day when demons remained in their celestial abode and earthly activities therefore enjoyed special protection.

In contemporary practice, families rarely confine themselves strictly to November 15. The crowded weekends throughout late October and November have become standard, allowing parents to schedule visits around work obligations and weather. Photography studios often book up months in advance for the formal portrait sessions that have become an integral part of modern observance.

The clothing worn for Shichi-Go-San constitutes one of the most visually striking elements of the tradition. Three-year-old girls typically wear a kimono paired with a hifu, a short padded overgarment that adds warmth and provides a distinctive silhouette appropriate to the youngest age. Seven-year-old girls wear full kimono with formal obi sashes tied in elaborate decorative knots, often with the assistance of professional dressers given the complexity of the garments. Boys wear formal hakama trousers paired with haori jackets, sometimes including a small ceremonial sword and other accessories appropriate to traditional male formal dress. The clothing has typically been rented or borrowed within families across generations, although purchase of new garments remains common for families wishing to mark the milestone with permanent keepsakes.

At the shrine, families typically receive a formal blessing from a Shinto priest, who recites a prayer specifically calling upon the kami to watch over the child's continued growth. These blessings are usually offered for a modest fee and may include receipt of an ema votive plaque, an omamori protective amulet, and other religious mementos. Following the formal blessing, families typically conduct extensive photography both within the shrine grounds and at studio settings, and the day often concludes with festive meals at restaurants or family gatherings honoring the grandparents who frequently travel to attend the celebration.

One of the most beloved customs associated with Shichi-Go-San is the chitose-ame, or thousand-year candy. These long thin red and white candy sticks symbolize wishes for long life, with the name explicitly invoking a thousand years of healthy existence. The candy is sold at shrines and traditional confectioners during the season, packaged in colorful paper bags decorated with auspicious symbols including cranes, turtles, pine trees, bamboo, and plum blossoms. Children carrying their oversized bags of chitose-ame through shrine grounds form one of the most recognizable images of the season, frequently appearing in photographs that capture the tradition's blend of solemnity and childlike delight.

Regional variations add complexity to the tradition. Northern regions, particularly Hokkaido and Tohoku where November weather can be harsh, often see families completing visits in October to avoid the worst cold. The Kansai region tends to observe more traditional gender-specific timing, with boys celebrated at three and five while girls are celebrated at three and seven. In the Kanto region around Tokyo, contemporary practice has shifted somewhat, with many families celebrating boys only at age five rather than at both three and five. These variations reflect the way Japanese tradition adapts to local conditions and family preferences while maintaining core symbolic continuity.

While famous shrines such as Meiji Jingu, Kanda Myojin, and Yushima Tenmangu in Tokyo, Fushimi Inari Taisha and Kitano Tenmangu in Kyoto, Sumiyoshi Taisha in Osaka, and Dazaifu Tenmangu in Fukuoka all receive significant Shichi-Go-San visitor traffic, the tradition emphasizes visits to the local ujigami, the tutelary deity of the family's home district. The quiet visit to a small neighborhood shrine, where a family alone may receive their blessing from a local priest, represents the tradition more authentically than the more visually spectacular gatherings at famous shrines. This intimate connection between family, locality, and the spiritual landscape forms the heart of Shichi-Go-San as a continuing element of Japanese religious life.""",
    },
    {
        "qid": "Q10860740",
        "slug_ja": "hachioji-matsuri",
        "slug_en": "hachioji-matsuri",
        "manual_content_ja": """八王子まつりは、東京都八王子市で毎年8月第1週の金・土・日に開催される夏祭りであり、東京西部最大級の祭礼として約75万人の観客を集める多摩地域を代表する夏の風物詩である。約400年の歴史を持つ八王子の山車文化と、神輿渡御・千人踊り・関東太鼓大合戦など多彩な催しが融合し、市民の活力と地域への誇りが結集する3日間となる。

八王子市は江戸時代に絹織物の集散地として発展した宿場町で、八王子千人同心と呼ばれる徳川幕府の警備組織が置かれた要衝でもあった。八王子まつりの原型は、江戸時代後期から続く各町内会の山車祭りで、当時は氷川神社・八幡八雲神社・多賀神社の例大祭として個別に行われていた。これらが現代の市民祭として統合されたのは1968年（昭和43年）で、3神社の例祭日が8月の同じ週末に重なる伝統を活かして、市全体で楽しむ夏の総合祭礼として再編された。

最大の見どころは、19台もの山車が一斉に巡行する「山車年番制」である。八王子の山車は彫刻と漆塗りで装飾された江戸型山車・八王子型山車を中心に、各町内会が保有する貴重な文化財で、台車の上に二層・三層の屋根を構え、最上部には人形や彫刻が飾られる豪華な造りとなっている。各町内会の若衆が法被姿で山車を曳き、囃子方が太鼓と笛で囃しながら市街地を進む光景は、東京とは思えない祭礼絵巻となる。

土曜日の夜の「上の祭典」では、複数の山車が出会いの場所で一斉に向き合い、囃子の競演を繰り広げる「ぶっつけ」が行われる。各町の囃子方が互いの腕を競い、見物客もどちらの囃子がより力強いかを見守る伝統行事で、八王子まつりの最も熱気あふれる瞬間として知られる。日曜日の「下の祭典」でも別の組み合わせで同様の競演が繰り広げられ、3日間で複数の地区が独自の祭りを展開する。

並行して開催される「八王子千人踊り」は、市民約3,000名が参加する大規模盆踊りで、甲州街道（国道20号）を歩行者天国にして繰り広げられる。浴衣姿の参加者が車道を埋め尽くして踊る光景は壮観で、観光客もその場で気軽に列に加わって踊れる開放感がある。「関東太鼓大合戦」では関東各地から太鼓集団が集結し、市庁前広場で大規模な太鼓演奏が披露される。

会場はJR八王子駅と京王八王子駅の中心市街地一帯で、両駅から徒歩約3分とアクセスは抜群。新宿から中央線特快で約40分、京王線特急で約45分と、東京観光の一環として容易に組み込める立地である。高尾山、東京サマーランド、よみうりランドなど多摩地域の観光地と組み合わせれば、東京西部の自然と祭礼文化を一日で堪能する旅程が構成できる。""",
        "manual_content_en": """The Hachioji Matsuri is one of the largest festivals in western Tokyo, held annually on the Friday, Saturday, and Sunday of the first week of August in Hachioji City. With approximately seven hundred fifty thousand attendees over three days, it stands as the defining summer festival of the broader Tama region and offers one of Tokyo's most spectacular displays of traditional float-based festival culture. The festival combines the elegance of nineteenth-century Edo-style decorated floats with the energy of contemporary community celebration, providing visitors a vivid experience of how traditional Japanese matsuri practices have evolved within the urban context of modern Tokyo.

Hachioji developed during the Edo period as a post town and silk weaving center along the Koshu Kaido, the major highway connecting Edo to the silk-producing regions of central Japan. The town also served as the base for the Hachioji Sennin Doshin, an elite Tokugawa shogunate security force whose thousand members were tasked with protecting the western approaches to the capital. This dual identity as commercial center and military outpost gave Hachioji a distinct economic and cultural character that supported the development of elaborate local festival traditions.

The origins of the contemporary Hachioji Matsuri lie in the separate annual festivals of three local shrines: Hikawa Shrine, Hachiman Yagumo Shrine, and Taga Shrine. Each of these shrines maintained its own festival traditions including processions of decorated floats and portable shrines, with the festivals scheduled around the same period in early August. The modern integrated form of the Hachioji Matsuri was established in 1968, consolidating the three traditional shrine festivals into a unified civic celebration that takes advantage of the calendar overlap while preserving the distinct traditions of each shrine community.

The festival's most distinctive feature is its dashi, the elaborate decorated floats that participating neighborhood associations bring out from their storage facilities for the festival. Hachioji preserves nineteen of these magnificent vehicles, representing a combination of Edo-type and Hachioji-type designs that constitute a major cultural heritage of the region. The floats feature multiple tiered roofs, often two or three levels, with the uppermost tier crowned by carved figures, dolls, or other ornamental elements. Lower sections are lavishly decorated with carved wooden panels depicting scenes from Japanese mythology and classical literature, finished in multiple layers of lacquer and gilded with gold leaf. The combination of carving, lacquerwork, and metalwork on these floats represents the accumulated artistry of generations of specialist craftspeople, and many of the existing floats are recognized as designated cultural properties.

Each float is pulled by members of its associated neighborhood association, with the young men known as wakashu performing the physical labor of moving the massive vehicles through the streets. Hayashi musicians, typically positioned on the floats themselves or in close attendance, provide continuous music using taiko drums, flutes, and small bells, creating distinctive musical signatures that identify each neighborhood's float to listeners familiar with the local tradition. Participants wear matching happi coats in colors and patterns specific to their associations, with the various groups creating visual contrast as they encounter each other on the festival routes.

The festival's most exciting moments occur during the buttsuke, or float encounters, that take place when multiple floats meet at intersections. Several floats face each other in coordinated formation, and their respective hayashi musicians launch into competitive performances, each attempting to play more powerfully and skillfully than the others. The competition is unspoken but unmistakable, with crowds gathering around the encounters to witness the musical confrontations. The Saturday evening encounter known as the Upper Festival features one combination of floats, while the Sunday Lower Festival brings together a different grouping, providing distinct experiences across the festival period.

A parallel feature of the festival is the Hachioji Sennin Odori, a massive group dance involving approximately three thousand participants performing on the Koshu Kaido, which becomes a pedestrian-only zone for the duration of the festival. Participants in yukata cotton kimono fill the wide thoroughfare, executing the choreographed movements of traditional Bon dance under festive lighting. Visitors are welcomed to join the dancing without registration or experience, and the inclusive atmosphere transforms what could be an observed performance into a participatory event in which boundaries between performer and audience dissolve.

The Kanto Taiko Daigassen brings together drum ensembles from across the wider Kanto region for large-scale performances in the City Hall plaza. Drums of varying sizes are played in coordinated patterns by groups that have often trained together for years specifically for festival appearances, creating thunderous performances that demonstrate the deep contemporary vitality of taiko drumming as an art form derived from but distinct from traditional festival accompaniment music.

Access to the festival is exceptionally convenient, with JR Hachioji Station and Keio Hachioji Station both located in the central festival area, just minutes on foot from the main parade routes. From Shinjuku, Hachioji can be reached in approximately forty minutes by Chuo Line rapid service or forty-five minutes by Keio Line limited express, making the festival an easy addition to any Tokyo itinerary. The wider Tama region offers extensive additional attractions including the celebrated Mount Takao with its temples and hiking trails, the family-oriented Tokyo Summer Land water park, and the rolling hills of Yomiuriland amusement park, allowing visitors to combine traditional festival experience with broader exploration of the natural and recreational landscapes of western Tokyo.""",
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

print("\n=== Part 2 検証 ===")
cur.execute(f"""
    SELECT qid, label_ja, status, LENGTH(manual_content_ja), LENGTH(manual_content_en)
    FROM festivals
    WHERE qid IN ({",".join(f"'{i['qid']}'" for i in ITEMS)})
""")
for row in cur.fetchall():
    print(f"[VERIFY] {row[0]} {row[1]} status={row[2]} len_ja={row[3]} len_en={row[4]}")

print("\n=== Day 6 全体集計 ===")
cur.execute("SELECT status, COUNT(*) FROM festivals GROUP BY status")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")
conn.close()
