#!/usr/bin/env python3
"""Insert festivals #56-60 (Phase 1c day 5 part 2)"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q11487216",
        "slug_ja": "hirosaki-castle-chrysanthemum-autumn-foliage",
        "slug_en": "hirosaki-castle-chrysanthemum-autumn-foliage",
        "manual_content_ja": """弘前城菊と紅葉まつりは、青森県弘前市の弘前公園で毎年10月中旬から11月上旬にかけて開催される秋の祭典である。日本三大桜名所として知られる弘前公園が、春の桜まつりに続いて秋にも見せる華やかな顔として、菊人形や菊花壇と、城跡を彩る紅葉の競演が楽しめる。1962年（昭和37年）の第1回開催以来、約60年の歴史を持つ津軽地方を代表する秋祭りである。

最大の見どころは、植物園内に展示される大規模な菊花展示である。1,000鉢を超える菊花が、大菊・小菊・盆栽菊などの形式別に整然と並べられ、それぞれの花の美しさを競う。特に注目されるのが、その年の話題やストーリーを題材にした巨大な菊人形展示で、職人が一鉢一鉢丁寧に育てた菊の花を組み合わせて人物像を作り上げる。NHK大河ドラマの登場人物や歴史上の偉人がテーマとなることが多く、伝統的な菊細工の技と現代的なストーリー性が融合した独自の表現が来場者を魅了する。

園内の紅葉も同時期に最盛期を迎える。約1,000本のモミジ、カエデ、イチョウ、ナナカマドが赤や黄に色づき、春には桜のトンネルとなる外濠の小径が今度は紅葉のトンネルへと変貌する。下乗橋から望む天守と紅葉、岩木山を背景にした構図は秋の弘前を代表する景観で、写真愛好家にとっては年に一度の絶好の機会となる。

夜間には「もみじライトアップ」が実施され、ライトに照らされた紅葉が漆黒の堀の水面に映る幻想的な光景が見られる。期間中は園内に屋台や物産展も並び、青森りんごの新品種試食、嶽きみ、けの汁、せんべい汁など秋の味覚が楽しめる。津軽塗や下川原焼など地元の伝統工芸品の販売も行われる。

JR弘前駅から100円循環バスで約15分とアクセスは桜まつりと同じ。同じ弘前公園を舞台にしながら、春の桜と秋の紅葉・菊の対比を楽しめるのが弘前観光の魅力である。十和田湖・奥入瀬渓流の紅葉、八甲田山ロープウェイなど青森県内の秋の名所と組み合わせれば、東北の秋を堪能する旅程が構成できる。""",
        "manual_content_en": """The Hirosaki Castle Chrysanthemum and Autumn Foliage Festival is the autumn counterpart to the famous Hirosaki Cherry Blossom Festival, held each year from mid-October through early November in Hirosaki Park, Aomori Prefecture. While the spring festival draws international fame, the autumn event reveals a quieter but equally compelling side of the park, where elaborate chrysanthemum displays meet the vivid colors of changing leaves against the backdrop of historic castle architecture. Since its inception in 1962, the festival has grown into one of the most beloved autumn events in the Tohoku region.

The festival's centerpiece is its monumental chrysanthemum display, staged within the park's botanical garden area. More than a thousand pots of chrysanthemums are arranged in carefully organized sections according to flower type, including large-headed ogiku varieties, small-headed kogiku, and trained bonsai-style chrysanthemums. Each plant has been cultivated for nearly a year by dedicated growers, who shape, prune, and pinch the plants to produce the precise forms and densities of bloom that competitive chrysanthemum culture demands. Visitors can examine plants displayed singly, in three-flower formal arrangements, and in massed plantings that create entire walls of color.

The most distinctive element of the chrysanthemum exhibit is the kiku-ningyo, or chrysanthemum dolls. These are life-sized human figures composed primarily of living chrysanthemum flowers, with the blooms forming the entire body of robes, sleeves, sashes, and accessories worn by the figures. Each year a theme is chosen, often drawing from the current NHK Taiga historical drama or from notable Japanese historical figures, and craftspeople assemble tableaux of multiple dolls in dramatic scenes. The creation of a single chrysanthemum doll requires the coordinated growth of dozens of carefully timed plants, with blooms reaching peak fullness at precisely the moment of the festival. The technique itself is a traditional art form with roots in the Edo period and is preserved by only a small number of specialist gardeners across Japan.

Concurrent with the chrysanthemum displays, Hirosaki Park's approximately one thousand maple, Japanese maple, ginkgo, and rowan trees reach their peak color. The same outer moat that becomes a tunnel of cherry blossoms in spring transforms in autumn into an arcade of reds, oranges, and yellows. The view from Gejo Bridge, which connects the outer and inner sections of the park, frames the castle keep against a wash of autumn color, with Mount Iwaki rising in the background. This composition has become one of the iconic autumn images of Tohoku and is heavily photographed throughout the festival period.

Evening illumination, known as the momiji light-up, transforms the park into a different experience. Floodlights cast warm glow on the colored leaves while the dark water of the moats reflects the illuminated foliage above, creating mirror images of brilliant color against the night sky. The castle keep, illuminated in white light against this autumn backdrop, takes on a presence quite different from its daytime appearance and quite different again from its illumination during cherry blossom season.

Food stalls and craft markets operate within the park throughout the festival, offering seasonal Aomori specialties. Visitors can sample new apple varieties at tasting booths, try grilled corn known locally as dake-kimi, warm themselves with the regional kenoshiru vegetable soup, or enjoy senbei-jiru, a hot pot dish featuring local rice crackers simmered in chicken broth. Traditional crafts from the Tsugaru region are also available, including the lustrous Tsugaru lacquerware known for its distinctive multi-layered finish and the rustic Shimokawara pottery with its dark glazes.

Access to the festival is identical to that of the spring cherry blossom event. JR Hirosaki Station can be reached from Shin-Aomori Station, the regional Shinkansen terminus, in approximately thirty-five minutes via the Ou Main Line, and from there the park is fifteen minutes by the one-hundred-yen circulator bus. The festival pairs naturally with broader autumn travel in Aomori Prefecture, where Lake Towada and the Oirase Stream offer some of Japan's most dramatic mountain foliage, and the Hakkoda Mountains feature autumn vistas accessible via cableway. The contrast between Hirosaki's cultivated garden aesthetics and the wild autumn landscapes of the surrounding mountains gives visitors a comprehensive view of how the Japanese tradition celebrates the season.""",
    },
    {
        "qid": "Q11502083",
        "slug_ja": "shinkawa-ichi-matsuri",
        "slug_en": "shinkawa-ichi-matsuri",
        "manual_content_ja": """新川市まつりは、山口県防府市の中心市街地で毎年7月下旬に開催される夏祭りであり、防府市民にとって最大の年中行事の一つである。新川と呼ばれる市街地を流れる川沿いと、駅前の中心商店街を会場として、神輿渡御、花火大会、踊りパレードなどが繰り広げられる。江戸時代から続く市場の名残を伝える祭りで、地域コミュニティの結束を象徴する伝統行事として大切に継承されている。

防府市は奈良時代に周防国の国府が置かれた古い歴史を持つ街で、菅原道真を祀る防府天満宮（日本三大天神の一つ）の門前町として栄えた。新川市まつりは、この防府天満宮の御神幸祭などの神事行事の流れを汲みつつ、明治以降に商店街や市民組織が中心となって整備された比較的新しい形の市民祭である。「市（いち）」の名が示す通り、もともとは新川沿いに開かれた定期市が祭りの原型で、商業の繁栄を祝う性格が強い。

祭りのハイライトは複数あり、初日の夕方には子ども神輿や女神輿の渡御が市街地を練り歩く。地元の町内会や事業所が独自の連を組んで参加し、それぞれの個性的な衣装や囃子で街を盛り上げる。2日目には花火大会が開催され、新川河畔から打ち上げられる約3,000発の花火が夏の夜空を彩る。花火は河川敷からも見られるほか、駅前商店街の各所からも観賞でき、市街地全体が祭りの空気に包まれる。

最終日にはパレード形式の総踊りが行われ、市民が浴衣姿で参加する盆踊りが街路を埋め尽くす。地元の小中学生によるよさこい風の創作踊りや、伝統的な防府音頭の踊り手が混在し、世代を超えた賑わいが生まれる。屋台村も商店街沿いに並び、関門地区特産のふくの天ぷら、瀬戸内の海産物を使った焼き物、地元の銘菓などが楽しめる。

会場はJR防府駅から徒歩約5分の中心市街地で、新山口駅からは山陽本線で約15分とアクセスも良好。秋吉台や錦帯橋など山口県内の観光地と組み合わせれば、防府天満宮参拝も含めた山口の文化と祭りを満喫する旅程が構成できる。""",
        "manual_content_en": """Shinkawa-ichi Matsuri is a vibrant summer festival held each year in late July in the central district of Hofu City, Yamaguchi Prefecture. Centered on the Shinkawa River that flows through downtown Hofu and the main shopping arcades near the station, the festival fills several days with portable shrine processions, fireworks displays, and large-scale dance parades. It represents one of the most important annual gatherings for the city's residents and serves as a focal point for community identity in this historically significant region of western Japan.

Hofu has been a place of importance since ancient times. During the Nara period, it served as the provincial capital, or kokufu, of Suo Province, and many of the area's place names still preserve administrative terms from that era. The city is also home to Hofu Tenmangu Shrine, dedicated to the deified scholar and statesman Sugawara no Michizane and considered one of the three great Tenjin shrines of Japan alongside Dazaifu and Kitano. The medieval and early modern town developed as a temple-gate community around this shrine, with merchant districts spreading along the river systems that connected the inland temple to the Seto Inland Sea ports.

The Shinkawa-ichi Matsuri grew out of this commercial and religious heritage. The word ichi in the festival's name means market, indicating that the festival's origins lie in the regular markets that were once held along the Shinkawa River. Over the Meiji and Taisho periods, as the riverside markets gradually transformed and modern shopping arcades developed, local merchants and civic associations organized a unified summer festival to celebrate commercial prosperity and community welfare. The festival in its present form draws on this market heritage while incorporating elements of the older religious processions associated with Hofu Tenmangu Shrine.

The festival unfolds across several days, each with distinct highlights. On the opening evening, portable shrine processions wind through the streets of central Hofu. These include children's mikoshi carried by elementary school groups and women's mikoshi distinguished by their elegant decorations and the spirited cries of the all-female teams that shoulder them. Neighborhood associations and local businesses form their own teams, called ren, each with distinctive costumes and musical accompaniment. The processions move through the shopping arcades and along the riverbank, drawing residents from their homes to watch and join in.

The second evening is dedicated to the fireworks display, the festival's most spectacular component. Approximately three thousand fireworks are launched from the banks of the Shinkawa River, illuminating the sky over central Hofu for nearly an hour. The fireworks can be enjoyed from designated viewing areas along the river or from various vantage points throughout the shopping district, where the lights of the explosions reflect off shop windows and create a doubled spectacle visible throughout the city center.

The final day features a grand parade and communal dance, with citizens in yukata cotton summer kimono filling the streets to perform traditional Hofu folk dances. Younger generations contribute energetic yosakoi-style modern dance routines, while older participants preserve the traditional Hofu Ondo, a regional folk song and dance that has been part of the festival for generations. The mixing of generations and styles creates a uniquely inclusive atmosphere that distinguishes Hofu's festival from more formally choreographed events in larger cities.

Food stalls line the shopping arcades throughout the festival period, offering specialties of the western Yamaguchi region. Tempura made from fugu, the famous pufferfish of nearby Shimonoseki, can be sampled in a more accessible form than the regulated restaurant servings. Seafood from the Seto Inland Sea features prominently, prepared as grilled skewers or in soups, and local sweets made with regional ingredients such as natsumikan citrus provide refreshment in the summer heat.

Access to the festival is straightforward. Hofu Station on the JR Sanyo Main Line lies within a five-minute walk of the central festival area. From Shin-Yamaguchi Station, the nearest Shinkansen stop, Hofu can be reached in approximately fifteen minutes. For travelers planning broader exploration of Yamaguchi Prefecture, the festival pairs naturally with visits to the Akiyoshidai limestone plateau, the historic Kintaikyo Bridge in Iwakuni, and of course Hofu Tenmangu Shrine itself, which sits just a short distance from the festival grounds and offers a quieter contrast to the lively summer celebration.""",
    },
    {
        "qid": "Q11511700",
        "slug_ja": "asahikawa-winter-festival",
        "slug_en": "asahikawa-winter-festival",
        "manual_content_ja": """旭川冬まつりは、北海道旭川市で毎年2月上旬から中旬にかけて開催される雪と氷の祭典であり、さっぽろ雪まつりと並ぶ北海道を代表する冬祭りの一つである。世界最大級の雪像を擁する祭りとしてギネス世界記録に認定されたこともあり、道北の厳冬期を彩る一大イベントとして約100万人の来場者を集める。

旭川冬まつりは1960年（昭和35年）に始まった。当時、旭川では石狩川河川敷で大規模な雪像が造られ、市民の冬の楽しみとして親しまれていたものを正式な祭りとして組織化したのが起源である。1994年には高さ27メートル、長さ150メートルの世界最大の雪像を制作してギネス世界記録に登録され、その後も大規模な雪像制作の伝統が引き継がれている。

会場は平和通買物公園と石狩川旭橋河畔の2か所に分かれている。中心市街地の平和通買物公園では、約1キロメートルの歩行者天国に氷像が並び、北海道内外の彫刻家や学生チームが氷の芸術作品を展示する。光に透ける氷像は夜間ライトアップによって幻想的な美しさを増し、ショッピングと観賞を兼ねた市民の散策路となる。

石狩川旭橋河畔の特設会場では、大規模な雪のステージと巨大な滑り台が設けられ、家族向けのスノーアトラクションが充実する。陸上自衛隊の協力による大雪像も毎年制作され、その年の話題やテーマに沿った彫刻が圧倒的なスケールで来場者を圧倒する。雪のすべり台は子どもから大人まで楽しめる人気アトラクションで、長さ100メートルを超える長大な滑走路を専用のソリで下る爽快な体験ができる。

夜間には花火大会も開催され、冬の澄んだ空に上がる花火と雪像のライトアップが幻想的な雰囲気を作り出す。会場周辺には旭川名物の屋台が並び、旭川ラーメン、ジンギスカン、海鮮丼、ザンギ（北海道風唐揚げ）など道北の冬グルメが堪能できる。

JR旭川駅から平和通買物公園は徒歩約3分、石狩川河畔会場へは無料シャトルバスで約10分。新千歳空港からは特急で約3時間半、旭川空港からは車で約30分とアクセスも整っている。旭山動物園、層雲峡氷瀑まつり、富良野・美瑛など道北の人気観光地と組み合わせれば、北海道の冬を満喫する旅程が構成できる。気温は氷点下20度を下回ることもあるため、最強の防寒装備が必須となる。""",
        "manual_content_en": """The Asahikawa Winter Festival is one of Hokkaido's three great winter festivals, held each year in early to mid-February in the city of Asahikawa in central Hokkaido. Together with the Sapporo Snow Festival and the Sounkyo Ice Waterfall Festival, it forms a trio of major winter events that draw visitors from across Japan and abroad to experience Hokkaido's harshest and most beautiful season. Approximately one million visitors attend each year, despite—and perhaps because of—the extreme cold that defines Asahikawa winters, with temperatures regularly dropping below minus twenty degrees Celsius.

The festival began in 1960, growing out of an informal tradition of large-scale snow sculpture building on the Ishikari River floodplain. Local residents had been creating monumental snow figures for community enjoyment, and civic leaders organized these activities into a formal annual event with growing scale and ambition. The festival achieved international recognition in 1994 when its main sculpture, measuring twenty-seven meters in height and one hundred fifty meters in length, was certified by Guinness World Records as the largest snow sculpture ever constructed. Although that specific record has since been surpassed, the tradition of monumental sculpture remains central to the festival's identity, and each year's main sculpture is constructed at an awe-inspiring scale.

The festival uses two main venues. The first is the Heiwa-dori Buyo Park, a pedestrian shopping street running through the heart of central Asahikawa for approximately one kilometer. During the festival, this pedestrian zone becomes an open-air ice sculpture gallery, with works displayed by ice carvers and competition teams from across Hokkaido and beyond. The ice sculptures range from intricate small pieces examining detailed subjects to ambitious larger works incorporating colored lighting and water elements. Evening illumination transforms these works into glowing forms set against the darkness of winter, creating a magical promenade for residents and visitors strolling between shops.

The second venue, set up on the floodplain along the Asahibashi Bridge over the Ishikari River, hosts the larger sculptural works and family-oriented attractions. The main snow sculpture, constructed with the cooperation of the Japan Ground Self-Defense Force, is the festival's most iconic feature. The theme varies from year to year and has included reproductions of famous architectural monuments, large-scale scenes from popular media, and original compositions celebrating Japanese cultural heritage. Whatever the subject, the sheer scale of the work, often the size of an apartment building, creates an indelible impression on visitors approaching across the snow-covered floodplain.

The Asahibashi venue also features one of the festival's most popular attractions: an enormous snow slide measuring more than a hundred meters in length, accessed by climbing the back of the snow sculpture and descended using specialized sleds. The slide is open to participants of all ages, from young children to elderly visitors, and provides a memorable physical experience of the snow that contrasts with the more contemplative viewing of the static sculptures.

Evenings during the festival feature fireworks displays that take advantage of the clarity and crispness of Hokkaido winter air. Fireworks against the deep black night sky, viewed across the illuminated snow sculptures, create a uniquely Hokkaido winter scene that combines pyrotechnic spectacle with the silent majesty of the surrounding cold.

Food stalls operate throughout both venues, offering specialties of Asahikawa and the broader Hokkaido region. The city is the birthplace of Asahikawa ramen, a distinctive style featuring soy-flavored broth and curly noodles topped with chashu pork and bamboo shoots, and bowls served at festival stalls offer welcome warmth between sculpture viewings. Other regional specialties include Genghis Khan grilled lamb, fresh seafood from the nearby Sea of Okhotsk, zangi which is the Hokkaido-style version of fried chicken, and warming sweet drinks such as amazake.

Access to the festival is straightforward. The Heiwa-dori venue lies just three minutes on foot from JR Asahikawa Station, while the Asahibashi venue is reached by free shuttle bus in about ten minutes. From New Chitose Airport, the main air gateway to Hokkaido, Asahikawa can be reached in approximately three and a half hours by limited express train. Asahikawa Airport provides direct access for travelers with shorter timelines, with the city center about thirty minutes by car. The festival pairs well with visits to the famous Asahiyama Zoo, the Sounkyo Ice Waterfall Festival in the nearby gorge, and the celebrated landscapes of Furano and Biei, allowing visitors to construct a comprehensive winter itinerary across central and northern Hokkaido. Visitors must come prepared for severe cold with high-quality insulated outerwear, waterproof boots with good traction on packed snow and ice, gloves, hats, and face coverings.""",
    },
    {
        "qid": "Q11513690",
        "slug_ja": "kasuga-wakamiya-on-matsuri",
        "slug_en": "kasuga-wakamiya-on-matsuri",
        "manual_content_ja": """春日若宮おん祭は、奈良県奈良市の春日大社の摂社である若宮神社で毎年12月15日から18日にかけて執り行われる祭礼であり、国の重要無形民俗文化財に指定されている。880年以上の歴史を持つ大和地方最古の祭礼の一つで、平安時代から現在まで一度も中断することなく続けられてきた稀有な伝統行事である。

おん祭の起源は1136年（保延2年）に遡る。当時、大和国が長雨と疫病に苦しんでいた折、関白藤原忠通が若宮神に祈願して五穀豊穣と疫病退散を願ったことが始まりとされる。以来、興福寺と春日大社の僧侶・神官、そして奈良の民衆が一体となって受け継ぎ、戦国時代の戦乱期や明治の神仏分離令、第二次世界大戦の混乱期も含めて、880年以上にわたり毎年欠かさず執行されてきた。

祭礼の中心は12月17日に行われる「お渡り式」である。正午、若宮神社の御神霊を一の鳥居前の御旅所にお遷しする神事に続き、興福寺南大門跡から県庁前を経て、御旅所までの約1キロメートルの道のりを、平安時代から江戸時代までの各時代の装束をまとった行列が練り歩く。日使、神子、巫女、細男、田楽、猿楽、競馬、流鏑馬、大名行列など、約1,000人が参加する壮麗な時代絵巻となる。これらの芸能は中世以来の古い形を伝えるもので、能楽の源流とされる猿楽、田植え踊りの原型である田楽など、日本芸能史の生きた資料として学術的にも極めて重要である。

御旅所では夜を徹して神楽、東遊、田楽、細男、能、狂言、舞楽などの伝統芸能が奉納される。これらの芸能奉納は深夜から翌18日未明まで続き、薪能と並ぶ古典芸能の聖地としての奈良の格式を示す貴重な機会となる。観覧は自由で、寒さの厳しい12月の夜の屋外で繰り広げられる芸能を間近で見ることができる。

春日大社は世界遺産「古都奈良の文化財」の構成資産で、参道の燈籠と原始林に包まれた境内は祭礼期間以外も訪れる価値が高い。会場へはJR・近鉄奈良駅から春日大社方面のバスで約10分または徒歩約25分。東大寺、興福寺、奈良公園など徒歩圏内に世界的な文化遺産が集中しており、おん祭の見学と合わせて奈良の古都文化を深く体験できる。12月の奈良は冷え込みが厳しいため、十分な防寒対策が必要となる。""",
        "manual_content_en": """The Kasuga Wakamiya On-Matsuri is one of Japan's oldest continuously held religious festivals, taking place each year from December 15 to 18 at the Wakamiya Shrine, a subordinate shrine within the broader complex of Kasuga Taisha in Nara. The festival is designated an Important Intangible Folk Cultural Property of Japan and stands as an exceptionally rare example of a major religious observance that has continued without interruption for more than 880 years, preserving classical Japanese performing arts and processional traditions in forms that have all but disappeared elsewhere.

The festival's origin can be precisely dated to the year 1136, during the late Heian period. The Yamato region had been suffering from prolonged rains and outbreaks of epidemic disease, and the regent Fujiwara no Tadamichi commissioned the establishment of a major annual observance at the Wakamiya Shrine, dedicated to the deity Ame no Oshikumone no Mikoto, to pray for agricultural prosperity and protection from pestilence. From that initiation, the festival has been continuously observed every year for nearly nine centuries, surviving the upheavals of the medieval warring states period, the religious reforms of the Meiji Restoration that separated Buddhism from Shinto, and the disruption of the Second World War. This unbroken continuity makes the On-Matsuri a unique repository of medieval ritual practice and performing arts.

The central event of the festival is the Owatari Shiki, or Procession of the Sacred Passage, held on December 17. At midday, the spirit of the Wakamiya deity is ceremonially transferred from the shrine to a temporary sanctuary, the otabisho, set up before the first torii gate of the Kasuga Taisha approach. A grand procession then forms at the site of the former Nandai-mon gate of Kofuku-ji Temple and proceeds along approximately one kilometer of city streets to the otabisho, where it presents the sacred presence to a gathered audience.

The procession itself is the festival's most visually striking element, with approximately one thousand participants dressed in costumes representing every era from the Heian period through the Edo period. Each column within the procession represents a particular role or social class from earlier times. Imperial messengers known as hizukai lead the line in formal court dress. Mediums and shrine maidens follow, accompanied by special performers. Among the most historically significant participants are the practitioners of medieval performing arts: the sarugaku who would later evolve into the noh tradition, the dengaku rice-planting dancers whose movements preserve agricultural ritual older than recorded history, and the seinoo and komainu performers whose roles are recorded in medieval texts but who appear in their traditional forms almost nowhere else in modern Japan. Mounted warriors representing different periods, archers performing yabusame mounted archery, and processions representing the lavish retinues of feudal lords complete the assembly.

After the procession's arrival at the otabisho, the festival enters its most extraordinary phase. From the late afternoon of December 17 through the early hours of December 18, dedicated performances of traditional arts are continuously offered before the sacred space. These include kagura sacred dance, azuma asobi ritual dance from eastern Japan, dengaku, the medieval seinoo performance, classical noh and kyogen, and bugaku, the ancient courtly dance form preserved primarily within shrine and palace traditions. The performances extend through the cold December night, with audiences wrapping themselves in blankets as they watch performances by torchlight and lantern. The atmosphere is one of meditative reverence rather than festive celebration, fundamentally different from most Japanese festivals encountered by foreign visitors and offering a glimpse of the religious dimensions that originally underlay all such observances.

Kasuga Taisha itself, of which the Wakamiya Shrine is a subordinate component, is part of the UNESCO World Heritage Site Historic Monuments of Ancient Nara and is one of the most important shrines in Japan. The approach to the shrine winds through a primeval forest preserved continuously since medieval times, with thousands of stone and bronze lanterns donated by worshippers over the centuries lining the paths. Even outside the festival period, the shrine and its surroundings reward extended exploration.

Access to the festival is convenient. Both JR Nara Station and Kintetsu Nara Station are connected to the shrine area by frequent buses with a travel time of approximately ten minutes, or by a pleasant walk through Nara Park taking roughly twenty-five minutes. The wider Nara Park area concentrates several of Japan's most important cultural treasures within walking distance, including Todai-ji Temple with its monumental bronze Buddha, Kofuku-ji Temple with its iconic five-story pagoda, and the open lawns frequented by the famous deer of Nara. Visitors attending the December festival should prepare carefully for cold weather, as Nara temperatures in mid-December often approach freezing during the long nighttime performances at the otabisho.""",
    },
    {
        "qid": "Q11582264",
        "slug_ja": "aioi-peron-matsuri",
        "slug_en": "aioi-peron-matsuri",
        "manual_content_ja": """相生ペーロン祭は、兵庫県相生市の相生湾で毎年5月最終日曜日とその前日に開催される海上競漕の祭典である。中国・福建省発祥のドラゴンボートに似たペーロン船による競漕レースを中心に、花火大会や前夜祭が盛大に繰り広げられ、瀬戸内海沿岸を代表する初夏の風物詩として親しまれている。約10万人の観客が訪れる相生市最大の年間行事である。

ペーロンの起源は中国・長崎・相生という独特の伝播経路をたどる。1922年（大正11年）、相生の播磨造船所（後のIHI相生工場）で働いていた長崎県出身の労働者たちが、故郷で親しんでいたペーロン競漕を職場の親睦行事として持ち込んだのが始まりとされる。長崎のペーロンは中国・福建省から伝わった伝統行事であり、その流れを汲む相生のペーロンは、造船の街として発展した相生の労働者文化と融合し、独自の市民祭として発展した。戦後、造船所の労働組合活動や町内会対抗の形でレースが続けられ、現在では「相生市制施行記念」と「相生湾の海上安全祈願」を兼ねた市民総出の祭りとして定着している。

ペーロン船は全長約13メートル、幅約1.6メートルの木造和船で、漕ぎ手28名、舵取り1名、太鼓打ち1名、銅鑼打ち1名の計31名で構成される。船首には龍頭の装飾が施され、色鮮やかな旗をなびかせて海上を疾走する。レースは町内会、企業、官公庁、学生などの所属チームに分かれて行われ、太鼓と銅鑼のリズムに合わせて漕ぎ手が一斉にオールを引く姿は圧巻である。優勝チームの栄誉は地域内で大きな名誉とされ、各チームは数か月前から練習を重ねて本番に臨む。

前夜祭にあたる土曜日の夜には、相生湾上空で花火大会が開催される。約5,000発の花火が湾を囲む山々に響きわたり、海面に反射する光が幻想的な情景を作り出す。湾の地形がスタジアム状の天然観覧席を形成しているため、どの角度から見ても迫力のある花火が楽しめる。

会場周辺には屋台村が並び、相生かきや播磨灘の海産物、明石焼き、加古川名物のかつめしなど、播磨地方の郷土料理が味わえる。アクセスはJR山陽本線・赤穂線の相生駅から徒歩約20分、または無料シャトルバスで約5分。山陽新幹線相生駅からも接続良好で、姫路や赤穂城跡など兵庫県西部の観光地と組み合わせやすい立地である。瀬戸内海沿岸の初夏の風と海上競漕の熱気を体感できる、地方都市ならではの密度の高い祭りである。""",
        "manual_content_en": """The Aioi Peron Matsuri is a maritime racing festival held annually on the last Sunday of May and the preceding Saturday in Aioi Bay, Aioi City, Hyogo Prefecture. Featuring traditional rowing races between long boats known as peron, the festival has evolved into one of the most beloved early summer events along the Seto Inland Sea coast. Approximately one hundred thousand spectators attend across the two days, making it the largest annual gathering in Aioi and one of the more distinctive festivals in western Honshu.

The festival's origins follow an unusual cultural transmission route from China through Nagasaki to Aioi. Peron racing itself traces its roots to Fujian Province in southern China, where dragon boat racing has been practiced for more than two thousand years as part of the Duanwu Festival. The tradition reached Nagasaki during the Edo period through the city's role as Japan's primary port of international trade, where Chinese residents introduced and adapted the practice for the conditions of Nagasaki Harbor. The transmission to Aioi came in 1922 during the Taisho period, when workers from Nagasaki Prefecture employed at the Harima Shipyard, a forerunner of the modern IHI Aioi Works, organized peron races as a way to maintain their hometown traditions and build camaraderie among the rapidly growing workforce of the shipbuilding city.

The integration of peron racing into Aioi's civic identity reflects the broader history of the city as a planned industrial community built around the shipyard. Through the Showa period, labor unions and neighborhood associations gradually organized the races into a structured annual competition, and after the Second World War the festival was formally established as an event commemorating the founding of Aioi as a municipality and praying for safety on the waters of the bay. Today, the festival is a city-wide event that involves participation from neighborhood associations, businesses, government offices, and schools, with teams training for months in preparation for the competition.

A peron boat measures approximately thirteen meters in length and 1.6 meters in width, constructed from wood in a traditional Japanese style adapted from the original Chinese design. Each boat is crewed by thirty-one people: twenty-eight rowers seated in pairs along the length of the hull, a steersman at the stern controlling the rudder, a drummer who sets the pace with a small drum, and a gong player who provides additional rhythmic cues. The boats are decorated with carved dragon heads at the prow and brightly colored team flags fluttering from poles. When racing at full speed, with rowers pulling in unison to the rapid beats of drum and gong, the boats cut through the bay water in a display of physical coordination and group athletic intensity that is genuinely thrilling to watch.

Races run throughout the main day of the festival, with teams competing in tournament brackets that produce eventual divisional champions. The course typically runs along a straight stretch of bay water of approximately three hundred meters, with viewing positions available along the curving shoreline and from designated piers extending into the harbor. The compact natural amphitheater formed by the bay's surrounding hills provides excellent acoustics, allowing spectators to hear the drumming and the calls of team captains echoing across the water.

The evening before the racing competition features a major fireworks display, with approximately five thousand fireworks launched over Aioi Bay. The hills surrounding the bay form a natural amphitheater that amplifies and reflects the sounds of the fireworks while the calm waters of the harbor mirror the colored explosions above. This combination creates a uniquely immersive viewing experience, with fireworks visible above, reflected below, and audible echoing from the surrounding slopes. Many spectators bring blankets or chairs to set up along the waterfront for an unhurried evening of viewing.

Food stalls operate along the festival route on both days, offering specialties of the Harima region. Aioi oysters, raised in the rich waters of the Seto Inland Sea, feature prominently in grilled and fried preparations. Other regional dishes include akashi-yaki egg-rich dumplings from nearby Akashi, katsumeshi pork cutlet rice from Kakogawa, and various seafood preparations utilizing the abundance of the surrounding seas. Local sake breweries also typically maintain stalls during the festival, providing refreshment in keeping with the warm late spring weather.

Access to the festival is convenient. JR Aioi Station, served by both the Sanyo Main Line and the Akoa Line, lies about twenty minutes on foot from the main festival area, with free shuttle buses available reducing the journey to roughly five minutes during festival hours. The Sanyo Shinkansen also stops at Aioi Station, allowing easy connections from major cities including Kobe, Osaka, and points along the Sanyo line. The festival pairs naturally with visits to other attractions of western Hyogo Prefecture, including Himeji Castle, the well-preserved Ako castle ruins associated with the famous tale of the forty-seven loyal retainers, and the seaside scenery of the Inland Sea coast.""",
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

print("\n=== Day 5 全体集計 ===")
cur.execute("SELECT status, COUNT(*) FROM festivals GROUP BY status")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")
conn.close()
