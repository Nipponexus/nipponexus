#!/usr/bin/env python3
"""Insert festivals #51-55 (Phase 1c day 5 part 1)"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q912124",
        "slug_ja": "jidai-matsuri",
        "slug_en": "jidai-matsuri",
        "manual_content_ja": """時代祭は、京都市左京区の平安神宮で毎年10月22日に執り行われる例大祭であり、葵祭・祇園祭と並ぶ京都三大祭の一つに数えられる。平安遷都1100年を記念して1895年（明治28年）に創建された平安神宮の創建と同時に始まった比較的新しい祭礼でありながら、京都の千年を超える歴史絵巻を再現する壮大な時代行列で知られている。

祭の中心となる時代行列は、京都御所の建礼門前を午前中に出発し、平安神宮までの約4.5キロメートルを約3時間かけて練り歩く。行列は明治維新時代から始まり平安遷都の延暦時代まで時代を遡る構成で、約2,000名の市民が当時の装束を身にまとって参加する。徳川城使上洛列、織田公上洛列、楠公上洛列、藤原公卿参朝列、延暦武官行進列など、各時代を代表する人物や軍勢が登場し、和宮、徳川和子、淀君、静御前、小野小町、紫式部、清少納言、巴御前、横笛など歴史上の女性たちも色とりどりの衣装で参列する。

行列で用いられる衣裳・祭具・調度品はいずれも厳密な時代考証に基づいて再現されたもので、京都の伝統工芸技術の粋を集めて製作されている。京都市の各学区から選ばれた市民が出演者となるため、地域共同体の祭として現在まで継承されてきた。雨天の場合は翌23日に順延される。

平安神宮は岡崎公園に隣接し、国の名勝に指定されている広大な神苑も併せて拝観できる。周辺には京都国立近代美術館や京都市美術館、京都市動物園が集まる文化ゾーンが広がり、地下鉄東山駅や京阪神宮丸太町駅から徒歩圏内とアクセスも良好である。10月の京都は気候も穏やかで、嵐山や東山の紅葉が色づき始める時期と重なるため、時代祭観覧と合わせて京都観光を計画する旅行者も多い。""",
        "manual_content_en": """Jidai Matsuri, the Festival of the Ages, is one of Kyoto's three great festivals alongside the Aoi Matsuri and Gion Matsuri, held annually on October 22 at Heian Jingu Shrine in the city's Sakyo Ward. Although it is the youngest of the three—established in 1895 to commemorate the 1,100th anniversary of the founding of Heian-kyo, as Kyoto was originally called—it has become one of the most visually spectacular pageants in Japan, presenting more than a thousand years of Japanese history in a single afternoon procession.

The festival was conceived as a way for Kyoto's citizens to reaffirm their pride in their city after the imperial capital was relocated to Tokyo in 1869, an event that had left Kyoto economically and culturally diminished. By recreating the city's storied past in elaborate detail, the people of Kyoto reasserted their identity as the cultural heart of Japan. The procession travels from the Kyoto Imperial Palace to Heian Jingu Shrine, a distance of roughly 4.5 kilometers covered over three hours, and is watched by tens of thousands of spectators lining the streets.

What makes Jidai Matsuri remarkable is its meticulous historical accuracy. The procession moves backward through time, beginning with the Meiji Restoration of the late nineteenth century and progressing through the Edo, Azuchi-Momoyama, Muromachi, Yoshino, Kamakura, Fujiwara, and finally Enryaku periods, ending with the era when Heian-kyo was founded in 794. Approximately 2,000 participants drawn from Kyoto's various neighborhood associations dress in costumes that have been researched and reproduced according to strict scholarly standards. Every garment, weapon, accessory, and piece of equipment is crafted using traditional Kyoto techniques, drawing on the city's deep heritage of textile dyeing, weaving, metalwork, and lacquerware.

The procession features columns representing famous figures from each era. The Tokugawa shogunate's envoy column recreates the formal entry of the shogun's representatives into Kyoto, while the Oda Nobunaga column depicts the warlord's ascent to the capital in the sixteenth century. Earlier periods bring forward figures from Japan's classical age, including aristocratic courtiers in Heian robes, Buddhist priests, and warrior bands. Particularly beloved are the columns of historical women, which include such legendary and historical figures as Princess Kazunomiya, Tokugawa Kazuko, Yodo-gimi, Shizuka Gozen, Ono no Komachi, Murasaki Shikibu, Sei Shonagon, Tomoe Gozen, and Yokobue. Their twelve-layered junihitoe robes and ornate hair ornaments offer a vivid display of classical Japanese aesthetics.

Heian Jingu Shrine itself is worth visiting in its own right. Built as a partial replica of the original Heian-period imperial palace, its vermilion buildings and vast white gravel courtyard evoke the architectural style of the ninth century. Behind the main hall lies a celebrated stroll garden designated a national Place of Scenic Beauty, where weeping cherry trees, water lilies, and irises bloom in succession through the seasons. In late October, when Jidai Matsuri takes place, the surrounding Higashiyama and Arashiyama districts begin to show their first hints of autumn color, making the period especially attractive for visitors planning a broader Kyoto itinerary.

Access to the festival route is convenient. The Kyoto Imperial Palace can be reached via the Karasuma subway line at Marutamachi or Imadegawa stations, while Heian Jingu Shrine is a short walk from Higashiyama Station on the Tozai subway line or Jingu-Marutamachi Station on the Keihan line. The procession passes through Marutamachi and Karasuma streets before turning eastward toward the shrine, and viewing stands with reserved seating are set up along the route for those who wish to watch in comfort. In the event of rain, the festival is postponed to the following day, October 23.

The Okazaki cultural district surrounding Heian Jingu offers further attractions, including the National Museum of Modern Art Kyoto, the Kyoto City KYOCERA Museum of Art, and the Kyoto Municipal Zoo, allowing visitors to combine festival viewing with a full day of cultural exploration. For travelers wishing to experience all three of Kyoto's great festivals in a single year, Jidai Matsuri completes the cycle that begins with Aoi Matsuri in May and Gion Matsuri throughout July.""",
    },
    {
        "qid": "Q929531",
        "slug_ja": "sapporo-snow-festival",
        "slug_en": "sapporo-snow-festival",
        "manual_content_ja": """さっぽろ雪まつりは、北海道札幌市で毎年2月上旬に開催される雪と氷の祭典であり、国内外から200万人を超える来場者を集める日本最大級の冬の祭事である。1950年（昭和25年）に地元の中学生・高校生が大通公園に6基の雪像を制作したことをきっかけに始まり、現在では大通会場・すすきの会場・つどーむ会場の3会場で展開される国際的な観光イベントへと発展した。

中心となる大通会場では、大通公園1丁目から12丁目までの約1.5キロメートルにわたって、大小200基を超える雪像・氷像が並ぶ。陸上自衛隊や市民ボランティアが大型雪像を制作し、世界の有名建築物、人気アニメキャラクター、その年の話題を象徴するモチーフなどが圧倒的なスケールで再現される。高さ15メートルに及ぶ大雪像は、トラック数千台分の雪を使用し、約1ヶ月をかけて削り出される。

すすきの会場では氷彫刻コンクールが開催され、透明感のある氷の芸術作品が華やかな歓楽街の夜景と調和する。つどーむ会場は家族向けエリアとして、滑り台やスノーラフト、雪上ゲームなど体験型アトラクションが充実している。期間中は夜間ライトアップやプロジェクションマッピングも実施され、昼と夜で異なる魅力を楽しめる。

国際雪像コンクールも併催され、世界各国のチームが招かれて技を競う。会場周辺には屋台村が設けられ、ジンギスカン、スープカレー、ラーメン、海鮮丼など北海道の冬の味覚が味わえる。

大通公園は札幌市中心部に位置し、地下鉄南北線・東西線の大通駅から直結、JR札幌駅からも徒歩約15分とアクセス抜群。札幌時計台や赤れんが庁舎、二条市場など市内の主要観光地もすべて徒歩圏内である。2月の札幌は氷点下が続く厳しい寒さとなるため、防寒具と滑りにくい靴の準備が必須となる。新千歳空港からは札幌駅まで快速エアポートで約40分でアクセスでき、小樽・登別温泉・ニセコなど道内各地への観光拠点としても最適である。""",
        "manual_content_en": """The Sapporo Snow Festival, known in Japanese as Sapporo Yuki Matsuri, is one of Japan's most internationally recognized winter events and the largest snow and ice festival in the country. Held each year in early February in Sapporo, the capital of Hokkaido, it draws more than two million visitors from across Japan and around the world, transforming the city's central park into an open-air gallery of monumental ice and snow sculptures.

The festival traces its origins to 1950, when local middle and high school students built six snow sculptures in Odori Park as part of a school project. The initial event proved so popular that it was repeated the following year, gradually expanding in scale and ambition. The turning point came in 1972, when Sapporo hosted the Winter Olympics, bringing global attention to the city's winter festival traditions. Since then, the Sapporo Snow Festival has grown into an international phenomenon featuring three distinct venues: the main Odori site, the lively Susukino entertainment district, and the family-oriented Tsudome dome.

The Odori site is the festival's centerpiece, stretching approximately 1.5 kilometers along Odori Park from the first to the twelfth city blocks. More than 200 large and small snow and ice sculptures line the park, ranging from massive works towering fifteen meters high to intricate smaller pieces. The most ambitious sculptures are constructed by units of the Japan Ground Self-Defense Force, working alongside teams of civilian volunteers. These crews use snow equivalent to thousands of truckloads, hauled in from the surrounding mountains, and spend roughly a month carving each piece. Themes vary from year to year and typically include famous buildings from around the world, beloved characters from anime and games, and symbols of current global events. Past sculptures have reproduced the Taj Mahal, Stockholm Cathedral, the Forbidden City, and life-size Hollywood film characters with breathtaking detail.

The Susukino site, located in the city's main entertainment quarter, hosts the International Ice Sculpture Competition. Here, transparent ice sculptures created by professional carvers and competitive teams glow against the neon backdrop of one of Japan's most famous nightlife districts. Walking through the illuminated street at night, visitors can examine each sculpture up close, with some featuring frozen flowers, fish, or other elements suspended in the ice. The juxtaposition of delicate ice artistry and the vibrant Susukino district creates an atmosphere unique to this venue.

The Tsudome site, set in a large indoor and outdoor sports complex on the city's outskirts, caters to families and visitors who wish to experience snow rather than simply observe it. Activities include long snow slides, snow rafting pulled by snowmobiles, miniature snow mazes, and various snow-based games. The indoor area provides a warm refuge with food stalls, performance stages, and seating areas, making it an ideal destination when temperatures drop below freezing as they regularly do during the festival period.

Each evening, the major sculptures at the Odori site are illuminated, and several feature elaborate projection mapping shows that bring the snow sculptures to life through coordinated light, color, and music. These nighttime presentations have become signature attractions, drawing crowds that fill the park even when temperatures dip well below zero degrees Celsius.

The festival is also a culinary destination. Pop-up food markets along Odori Park serve regional Hokkaido specialties suited to winter weather, including Genghis Khan grilled lamb, Hokkaido-style miso ramen, soup curry brimming with vegetables, fresh seafood bowls featuring sea urchin and salmon roe, and warming hot drinks such as amazake. Many local restaurants and izakaya in the surrounding blocks also offer special winter menus during the festival period.

Access to the festival is exceptionally convenient. Odori Park is directly connected to Odori Station on the Sapporo subway system and is approximately a fifteen-minute walk from JR Sapporo Station. Visitors traveling from outside Hokkaido can fly into New Chitose Airport and take the rapid Airport train to Sapporo Station in about forty minutes. The festival also serves as an excellent base for exploring other winter destinations in Hokkaido, including the canal city of Otaru, the hot spring resort of Noboribetsu, and the world-class ski areas of Niseko and Furano.

Given the severe cold of Sapporo in February, with daytime temperatures often well below freezing and frequent snowfall, visitors should come prepared with heavy winter clothing, waterproof boots with good traction, gloves, and head coverings. Sidewalks can become icy, and walking pace is necessarily slower than in milder seasons. Despite these challenges, the experience of standing among monumental snow sculptures in a city transformed by winter is unmatched, and the Sapporo Snow Festival remains a defining bucket-list destination for travelers seeking the singular beauty of Japan's northern winter.""",
    },
    {
        "qid": "Q9385159",
        "slug_ja": "sendai-tanabata",
        "slug_en": "sendai-tanabata",
        "manual_content_ja": """仙台七夕は、宮城県仙台市で毎年8月6日から8日までの3日間にわたって開催される七夕祭りであり、青森ねぶた祭・秋田竿燈まつりと並ぶ東北三大祭りの一つに数えられる。期間中は約200万人の観光客が訪れ、仙台中心部のアーケード街や駅前通りが色とりどりの巨大な吹き流しで埋め尽くされる、日本を代表する夏の風物詩である。

仙台七夕の起源は、仙台藩祖・伊達政宗が婦女子の文化向上のために奨励したとされ、江戸時代から長く続く伝統行事である。一時は明治維新後の混乱や第二次世界大戦の戦災で衰退したが、戦後の1946年に商店街を中心に復活し、現在では市民総出で取り組む大規模な祭典へと発展した。

最大の見どころは「七つ飾り」と呼ばれる伝統的な飾り付けである。短冊（学問の上達）、紙衣（裁縫の上達と無病息災）、折鶴（長寿）、巾着（金運上昇）、投網（豊漁・豊作）、屑籠（清潔と倹約）、吹き流し（織姫の織り糸）の7種類の飾りには、それぞれ意味が込められており、商店街の各店舗が一年がかりで手作りで製作する。仙台駅前から一番町、中央通りに至るアーケード街は、長さ10メートルを超える豪華絢爛な吹き流しで埋め尽くされ、頭上を歩くたびに和紙の華やかな色彩に包まれる体験ができる。

七夕の前夜である8月5日には、広瀬川河畔で「仙台七夕花火祭」が開催され、約16,000発の花火が夜空を彩る。期間中は勾当台公園に「おまつり広場」が設けられ、ステージイベント、伝統芸能の披露、屋台村などが楽しめる。仙台名物の牛タン、笹かまぼこ、ずんだ餅、せり鍋など、東北の夏グルメも豊富である。

会場はすべてJR仙台駅から徒歩圏内にあり、新幹線でのアクセスも良好。日帰りでも十分楽しめるが、松島・蔵王・鳴子温泉など仙台周辺の観光地と組み合わせた東北旅行の起点としても理想的な祭りである。""",
        "manual_content_en": """Sendai Tanabata is one of the three great summer festivals of the Tohoku region, held annually from August 6 to 8 in the city of Sendai in Miyagi Prefecture. Alongside the Aomori Nebuta Festival and the Akita Kanto Festival, it stands as a defining seasonal event in northern Japan, drawing approximately two million visitors over its three-day run. The festival fills the central arcades and main shopping streets of Sendai with thousands of enormous decorative streamers, creating an immersive landscape of color that has made the event one of Japan's most beloved summer spectacles.

The festival is rooted in the ancient Tanabata tradition, which itself originated in Chinese mythology and was brought to Japan during the Nara period. The legend tells of two celestial lovers, the weaver star Orihime and the cowherd star Hikoboshi, separated by the Milky Way and permitted to meet only once a year on the seventh night of the seventh month. In Japan, this story merged with native customs of writing wishes on strips of paper and hanging them from bamboo branches. While Tanabata is celebrated throughout the country, Sendai's version distinguishes itself through its monumental scale, the artistry of its decorations, and the depth of its civic engagement.

The Sendai Tanabata tradition was promoted by Date Masamune, the founding lord of the Sendai domain in the early seventeenth century, who encouraged its observance to elevate the cultural lives of women in his domain. The festival flourished throughout the Edo period but declined during the upheavals of the Meiji Restoration and was further diminished during World War II when much of the city was destroyed in aerial bombings. In 1946, immediately after the war, local merchants revived the festival as a symbol of recovery and civic pride. From these modest postwar beginnings, the festival has grown into the massive celebration seen today.

The most distinctive feature of Sendai Tanabata is the nanatsu-kazari, or seven traditional decorations, which carry specific symbolic meanings. The tanzaku are paper strips inscribed with wishes for academic and artistic improvement. The kamigoromo, paper kimono, represent prayers for sewing skill and protection from illness. Orizuru paper cranes symbolize longevity. Kinchaku, drawstring pouches, invite financial prosperity. Toami, casting nets, pray for abundant harvests of fish and crops. Kuzukago, waste baskets, represent cleanliness and thrift. The seventh and most spectacular decoration is the fukinagashi, long streamers that represent the threads woven by Orihime herself.

Each fukinagashi is handmade by the staff of a participating shop, often taking the better part of a year to design and assemble. Made from washi paper and bamboo, the streamers can reach more than ten meters in length and feature elaborate three-dimensional ornaments at the top. The shopping arcades from Sendai Station through Ichibancho and Chuo-dori are entirely transformed during the festival, with dense canopies of streamers hanging just overhead. Walking through these passages is a deeply sensory experience as breezes set the paper in motion and sunlight filters through countless shades of pink, gold, indigo, and red.

The evening of August 5, the night before the festival officially opens, features the Sendai Tanabata Fireworks Festival along the banks of the Hirose River. Approximately 16,000 fireworks are launched in a coordinated display lasting more than ninety minutes, providing a brilliant prelude to the days of decoration that follow. Throughout the main festival period, the Kotodai Park area hosts a designated festival plaza where stages present traditional performing arts including kagura dance, taiko drumming, and folk music. Food stalls offer regional Tohoku specialties such as gyutan grilled beef tongue, sasakamaboko fish cake, zunda mochi made with sweetened mashed edamame, and seri-nabe hot pot.

Sendai Tanabata is exceptionally accessible for visitors. All the major festival areas are within walking distance of JR Sendai Station, served by the Tohoku Shinkansen line which connects directly to Tokyo in approximately ninety minutes. The festival's central location also makes it an ideal starting point for broader exploration of Tohoku. The nearby coastal area of Matsushima, considered one of the three most scenic views in Japan, can be reached in about forty minutes by local train. The Zao mountain range, famous for its volcanic crater lake and hiking trails, lies to the west, and the hot spring resort of Naruko, known for traditional kokeshi dolls and therapeutic waters, is accessible by rail and bus.

Visitors planning their first experience of Sendai Tanabata should arrive early in the day to view the decorations under bright sunlight, when the colors of the streamers appear at their most vibrant, and return in the evening when the arcades are illuminated and the atmosphere shifts toward the festive energy of summer evening gatherings.""",
    },
    {
        "qid": "Q10869430",
        "slug_ja": "koenji-awa-odori",
        "slug_en": "koenji-awa-odori",
        "manual_content_ja": """東京高円寺阿波おどりは、東京都杉並区の高円寺地区で毎年8月最終土日に開催される阿波おどりの祭典であり、本場徳島県の阿波おどりに並ぶ規模を誇る関東最大級の踊りの祭りである。約1万人の踊り手が参加し、2日間で約100万人の観客が高円寺の街に押し寄せる、東京の夏を代表するイベントの一つである。

高円寺の阿波おどりは1957年（昭和32年）に始まった。当時、商店街の活性化策として徳島の阿波おどりを模した盆踊りが企画されたのが起源で、徳島から指導者を招いて本格的な踊りを学んだ。最初は小規模だったが、年々規模を拡大し、現在では国内最大級の阿波おどりイベントへと成長した。徳島本場の阿波おどりが400年以上の歴史を持つ伝統行事であるのに対し、高円寺は都市型の新しい伝統として独自の文化を築いてきた。

阿波おどりは「連（れん）」と呼ばれる踊り手の集団単位で踊られる。高円寺大会には地元高円寺の連に加えて、徳島本場の連、東京都内・関東各地の連が参加し、それぞれの個性的な踊りを披露する。男踊りは法被に股引き、提灯を持って力強く跳躍するように踊り、女踊りは編笠を深くかぶり、浴衣姿で手を高く上げてしなやかに舞う。鳴り物（三味線・笛・太鼓・鉦）の軽快なお囃子に乗って「ヤットサーヤットサー」の掛け声が街中に響く。

会場はJR中央線・総武線の高円寺駅と東京メトロ丸ノ内線の新高円寺駅を中心に、商店街と一般道路に設置された8つの演舞場で構成される。それぞれの演舞場で同時並行に踊りが繰り広げられ、観客は街を歩き回りながら好きな場所で観覧できる。

高円寺は古着屋やレコード店、ライブハウス、個性的な居酒屋が集まるサブカルチャーの街としても知られ、祭り期間外でも一日散策が楽しめる。新宿から中央線快速で約7分という都心からのアクセスの良さも魅力で、東京観光の一環として組み込みやすい祭りである。""",
        "manual_content_en": """The Koenji Awa Odori is one of the largest and most spirited Awa Odori dance festivals held outside the dance's birthplace in Tokushima Prefecture, taking place each year on the last weekend of August in the Koenji neighborhood of Tokyo's Suginami Ward. Approximately ten thousand dancers perform over two days, drawing crowds estimated at one million spectators, making it one of the defining summer events of the Tokyo calendar and a centerpiece of the city's traditional festival season.

Awa Odori itself is a dance tradition more than four hundred years old, originating in Tokushima on the island of Shikoku as part of Obon festivities honoring the spirits of ancestors. The Koenji version is considerably younger, established in 1957 when local merchants searching for a way to revitalize their shopping district invited instructors from Tokushima to teach the dance to neighborhood residents. From these humble beginnings, the festival grew steadily through subsequent decades to become a metropolitan tradition in its own right, blending the energy of the original folk dance with the dynamism of urban Tokyo culture.

The dance is performed by groups known as ren, each typically composed of dozens of dancers along with their own musicians. A ren has a distinctive style of costume, choreography, and musical interpretation, allowing each group to express its individual character within the broader Awa Odori tradition. At the Koenji festival, ren from across Tokyo and the wider Kanto region perform alongside guest ren from Tokushima itself, giving spectators an opportunity to see both the regional Tokyo style and the original Shikoku form within the same event.

The dance has two principal forms. The men's dance, known as otoko odori, is performed in a low crouching posture with arms raised and exaggerated, almost acrobatic movements. Male dancers wear short happi coats, momohiki leggings, and tabi socks, and often carry paper lanterns held high overhead. The dance projects vigor and physical exuberance, with leaping movements set to a fast tempo. The women's dance, onna odori, presents a striking contrast in mood. Women dancers wear yukata cotton kimono, geta clogs with elevated wooden bases, and amigasa woven straw hats tilted to obscure the face. Their movements are elegant and refined, with arms extended upward and hands tracing graceful lines in the air, fingers held in precise positions that have been passed down through generations of practitioners.

The music driving the dance is provided by a small ensemble using shamisen three-stringed lutes, fue bamboo flutes, taiko drums, and kane bells. The basic rhythm is a syncopated two-beat pattern that creates an irresistible propulsive feel, punctuated by the famous call-and-response shout of "Yattosa! Yattosa!" that echoes through the streets. The musicians themselves are part of the ren and perform in matching costumes, walking alongside or just behind the dancers.

The festival is staged across eight performance areas distributed throughout the Koenji shopping district and surrounding streets, centered on JR Koenji Station on the Chuo and Sobu lines and Shin-Koenji Station on the Tokyo Metro Marunouchi line. Each performance area runs its own continuous flow of ren throughout the afternoon and evening hours, allowing spectators to wander between locations and experience different vantage points. Some areas are along straight stretches of street ideal for watching long lines of dancers pass, while others occupy small plazas where ren can perform stationary set pieces.

Beyond the festival itself, Koenji is one of Tokyo's most distinctive neighborhoods and richly rewards exploration on its own merits. The area is renowned as a hub of alternative culture, with concentrations of secondhand clothing stores, used record shops, independent bookstores, and small live music venues. Eclectic izakaya and standing bars line the narrow streets running off the main shopping arcades, attracting an artistic and bohemian clientele. The neighborhood's relaxed character contrasts with the polished commercialism of more famous Tokyo districts and offers visitors a glimpse of a different side of the city.

Access to the festival from central Tokyo is straightforward. Koenji is approximately seven minutes from Shinjuku Station on the Chuo Line rapid service, making it possible to attend the festival as a side excursion during a broader Tokyo itinerary. Visitors should expect dense crowds, particularly during the peak evening hours, and may find it helpful to arrive in the late afternoon to secure a comfortable viewing position. Light summer clothing, a fan, and a water bottle are advisable, as late August in Tokyo brings high temperatures and humidity that persist well into the night.""",
    },
    {
        "qid": "Q11487199",
        "slug_ja": "hirosaki-cherry-blossom",
        "slug_en": "hirosaki-cherry-blossom",
        "manual_content_ja": """弘前さくらまつりは、青森県弘前市の弘前公園で毎年4月下旬から5月上旬にかけて開催される桜の祭典であり、日本三大桜名所の一つに数えられる。約2,600本もの桜が城跡の堀や石垣を彩る景観は、東北を代表する春の風物詩として国内外から200万人を超える観光客を集める。

弘前公園は、津軽氏代々の居城であった弘前城を中心とする広大な城跡公園で、現存12天守の一つである弘前城天守をはじめ、五つの城門と三つの櫓が国の重要文化財に指定されている。園内の桜は1715年に津軽信寿が25本のカスミザクラを植えたのが始まりとされ、明治時代に旧藩士が1,000本のソメイヨシノを寄贈したことで現在の規模となった。日本古来の樹齢100年を超える老木と、丁寧に手入れされた若木が共存する弘前の桜は、林檎の栽培技術を応用した独自の剪定法によって一本一本が大きな花房をつけることで知られている。

最大の見どころは「西濠の花筏」と「桜のトンネル」である。西濠の水面には散った花弁が一面に敷き詰められ、まるで桃色の絨毯のように流れていく光景は、満開を過ぎた数日間にしか見られない奇跡的な景観である。また外濠の桜のトンネルは、両岸の桜が頭上で交差し、約400メートルにわたって続く花のアーケードとなる。本丸からは岩木山を背景にした桜と天守の絶景が望め、津軽富士と呼ばれる秀峰と桜・城・石垣が織りなす構図は弘前を象徴する風景である。

期間中は夜桜のライトアップが実施され、堀の水面に映る幻想的な姿が楽しめる。園内には約200軒の屋台が並び、津軽そば、けの汁、ホタテ焼き、いがめんちなど青森の郷土料理が味わえる。アクセスはJR弘前駅から100円循環バスで約15分、新青森駅からは奥羽本線で弘前駅まで約35分。津軽鉄道や黒石こみせ通り、白神山地など周辺観光と組み合わせれば、津軽地方の春を満喫する旅程が構成できる。""",
        "manual_content_en": """The Hirosaki Cherry Blossom Festival is one of Japan's three most celebrated cherry blossom viewing destinations, held annually from late April through early May in the city of Hirosaki, Aomori Prefecture. Approximately 2,600 cherry trees fill the grounds of Hirosaki Park, the former castle of the Tsugaru clan, drawing more than two million visitors during its roughly two-week run. The festival's combination of historic castle architecture, abundant cherry varieties, and the dramatic backdrop of Mount Iwaki has made it one of the most photographed and beloved springtime events in northern Japan.

Hirosaki Park is built around the remains of Hirosaki Castle, which served as the seat of the Tsugaru clan throughout the Edo period. The castle complex preserves one of only twelve original castle keeps remaining in Japan, along with five castle gates and three turrets, all designated as Important Cultural Properties of the nation. The combination of original castle architecture from the seventeenth century, the moats and stone walls that surround the keep, and the dense plantings of cherry trees creates a setting unmatched anywhere in the country.

The history of cherry trees in Hirosaki Park dates to 1715, when Tsugaru Nobuhisa planted twenty-five kasumi-zakura trees within the castle grounds. The current scale of the planting, however, owes its existence to a Meiji-era donation by former samurai retainers of the Tsugaru clan, who contributed one thousand Yoshino cherry saplings to the park in 1882. Subsequent generations of gardeners have continued to expand and maintain the collection, and today the park contains more than fifty cherry varieties alongside the dominant Yoshino. What truly distinguishes Hirosaki's cherry trees, however, is the cultivation technique that has been developed over more than a century of careful study. Local horticulturalists, drawing on knowledge gained from Aomori's famous apple-growing industry, have applied pruning methods originally developed for fruit trees to the care of cherry trees. The result is that each Hirosaki cherry tree produces unusually large and dense flower clusters, with each branch bearing several blossoms in a single tight bouquet rather than the more scattered pattern typical of cherry trees elsewhere. Many of the trees in the park are over a century old, and a few exceed two hundred years, making them among the oldest living Yoshino cherries in Japan.

The festival's most iconic sights include the hana-ikada, or floating flower raft, on the western moat. After the peak bloom has passed and petals begin to fall, the still surface of the moat becomes blanketed with pink petals, creating the impression of a solid pink carpet floating on water. This phenomenon lasts only a few days each year and is one of the most photographed spring scenes in all of Japan. Equally celebrated is the cherry blossom tunnel along the outer moat, where trees planted along both banks have grown together overhead, forming an arch of blossoms approximately four hundred meters in length. Walking beneath this canopy, with light filtered through countless pink and white flowers, offers an immersive experience of spring at its most poetic.

From the inner bailey of the castle, visitors can take in a view that has become emblematic of Hirosaki: the castle keep set against a foreground of blooming cherry trees with Mount Iwaki, the so-called Tsugaru Fuji, rising in the distance. The 1,625-meter volcano is the spiritual mountain of the Tsugaru region and is often still snow-capped during cherry blossom season, providing a striking contrast of white peak, pink blossoms, and dark castle stone.

Evening illumination during the festival transforms the park into an entirely different experience. Floodlights cast the trees in soft glow while the still waters of the moats reflect the illuminated blossoms above, creating doubled images of fantastic beauty. The castle keep, when illuminated against the night sky, takes on an almost otherworldly appearance amid the surrounding flowers.

Approximately two hundred food stalls operate within the park during the festival, offering regional Aomori specialties such as Tsugaru soba noodles, kenoshiru vegetable soup, grilled scallops from Mutsu Bay, and igamenchi fried squid patties. Local sake breweries and apple orchards often have stands as well, allowing visitors to sample regional drinks alongside the food.

Access to the festival is convenient. JR Hirosaki Station is connected to Shin-Aomori, the Shinkansen terminus, by the Ou Main Line, with a travel time of approximately thirty-five minutes. From Hirosaki Station, the park is reached in about fifteen minutes by the one-hundred-yen circulating bus that loops through the city. The wider Tsugaru region offers additional attractions worth combining with a cherry blossom visit, including the historic Konagai Komise district of Kuroishi, the Tsugaru Railway with its retro stove-heated train cars, and the Shirakami Mountains, a UNESCO World Heritage Site featuring one of the largest virgin beech forests in East Asia.""",
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
