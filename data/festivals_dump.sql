BEGIN TRANSACTION;
CREATE TABLE festivals (
            qid TEXT PRIMARY KEY,
            label_ja TEXT,
            label_en TEXT,
            description_ja TEXT,
            description_en TEXT,
            location_qid TEXT,
            location_label_ja TEXT,
            location_label_en TEXT,
            prefecture TEXT,
            region TEXT,
            latitude REAL,
            longitude REAL,
            inception_year INTEGER,
            start_month INTEGER,
            season TEXT,
            image_url TEXT,
            wikipedia_ja TEXT,
            wikipedia_en TEXT,
            priority_score INTEGER DEFAULT 0,
            status TEXT DEFAULT 'pending',
            manual_content_ja TEXT,
            manual_content_en TEXT,
            slug_ja TEXT,
            slug_en TEXT,
            published_at TEXT,
            fetched_at TEXT NOT NULL,
            source TEXT NOT NULL DEFAULT 'wikidata'
        );
INSERT INTO "festivals" VALUES('Q218663','山王祭','Sannō Matsuri','東京都千代田区にある日枝神社の祭礼','major Shinto festival in Tokyo held biennially in June','Q702042','日枝神社','Hie Shrine','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hie%20jinjya-7.jpg','https://ja.wikipedia.org/wiki/%E5%B1%B1%E7%8E%8B%E7%A5%AD_(%E5%8D%83%E4%BB%A3%E7%94%B0%E5%8C%BA)','https://en.wikipedia.org/wiki/Sann%C5%8D_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q82113','広島国際アニメーションフェスティバル','Hiroshima International Animation Festival',NULL,'biennial Japanese festival','Q34664','広島市','Hiroshima','広島県','chugoku',34.38525,132.45531,1985,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BA%83%E5%B3%B6%E5%9B%BD%E9%9A%9B%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Hiroshima_International_Animation_Festival',70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q218646','神田祭','Kanda Matsuri','東京都千代田区の神田明神で行われる祭礼','Japanese festival that takes place in Kanda, Tokyo','Q717682','神田明神','Kanda-myōjin','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kanda%20Matsuri%202009-1%20in%20Akihabara.jpg','https://ja.wikipedia.org/wiki/%E7%A5%9E%E7%94%B0%E7%A5%AD','https://en.wikipedia.org/wiki/Kanda_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q114712','長崎くんち','Nagasaki Kunchi','長崎市のお祭り','festival in Nagasaki, Japan','Q84028','鎮西大社諏訪神社','Suwa Shrine','長野県','chubu',32.754125,129.88211111,1634,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Jaodori%20of%20Nagasaki%20Kunchi.jpg','https://ja.wikipedia.org/wiki/%E9%95%B7%E5%B4%8E%E3%81%8F%E3%82%93%E3%81%A1','https://en.wikipedia.org/wiki/Nagasaki_Kunchi',95,'drafted','## 概要

長崎くんち（ながさきくんち）は、長崎県長崎市の鎮西大社諏訪神社で毎年10月7日から9日にかけて執り行われる、諏訪神社の例大祭である。「長崎くんちの奉納踊」として国の重要無形民俗文化財に指定されており、博多おくんち（福岡県）、唐津くんち（佐賀県）と並ぶ「日本三大くんち」のひとつに数えられる。異国情緒あふれる「龍踊（じゃおどり）」「コッコデショ」「川船」など、長崎の国際性を象徴する奉納踊が最大の見どころである。

## 歴史

起源は1634年（寛永11年）、長崎奉行が諏訪神社の遷宮を機に町衆に奉納踊を命じたことに始まる。当時の長崎は鎖国下にあってオランダ・中国との貿易の窓口であり、外国文化が町人文化に深く浸透していた。その結果、龍踊や蛇踊といった中国由来の演目、オランダ船を模した「オランダ船」などの異国情緒豊かな出し物が生まれ、約400年の歴史を通じて受け継がれてきた。1979年（昭和54年）、奉納踊が国の重要無形民俗文化財に指定された。

## 見どころ

最大の見どころは、町ごとに7年に1度の輪番制で奉納される独特の演目群である。中国の影響を受けた「龍踊」（じゃおどり）は、長さ約20メートルの龍が大太鼓と銅鑼の轟音とともに乱舞する壮観な演目。「コッコデショ」（樺島町）は、約1トンの太鼓山を36人の男衆が空高く投げ上げる迫力ある奉納で、観衆から「モッテコーイ」（アンコール）の声がかかる。「川船」「鯨の潮吹き」「阿蘭陀万歳」など長崎ならではの演目が次々と披露される。会場は諏訪神社境内、八坂神社、お旅所、公会堂前広場など複数。

## 開催情報

開催地は長崎県長崎市上西山町の鎮西大社諏訪神社ほか市内複数会場。最寄駅は長崎電気軌道「諏訪神社駅」徒歩約3分。開催期間は毎年10月7日（前日）・8日（中日）・9日（後日）の3日間。諏訪神社境内の桟敷席は事前抽選制で有料、お旅所・八坂神社の観覧スペースは一部無料。海外からの観光客も多く、3日間で延べ約60万人が来訪する。

## 周辺の見どころ

長崎市は世界遺産「長崎と天草地方の潜伏キリシタン関連遺産」の中核地として知られ、大浦天主堂・グラバー園・出島など歴史観光地が市内に集積している。原爆資料館・平和公園では戦争と平和について学べる。長崎中華街では本場の中国料理、稲佐山展望台からは世界新三大夜景に選ばれた市街地夜景が一望できる。祭礼期間中はホテルが早期満室になるため数ヶ月前からの予約が推奨される。','## Overview

Nagasaki Kunchi (長崎くんち) is the grand annual festival of Chinzei Taisha Suwa Shrine, held every year from October 7 to 9 in Nagasaki City, Nagasaki Prefecture. Designated as an Important Intangible Folk Cultural Property of Japan, it ranks alongside Hakata Okunchi (Fukuoka) and Karatsu Kunchi (Saga) as one of Japan''s three great Kunchi festivals. The festival is celebrated for its strikingly cosmopolitan dedicatory performances — including the Dragon Dance (Ja-odori), Kokkodesho, and Kawafune (river boat) — that reflect Nagasaki''s unique heritage as Japan''s historical gateway to the world.

## History

The festival''s origins trace back to 1634 (Kan''ei 11), when the Nagasaki magistrate commanded the city''s townspeople to perform dedicatory dances at the relocation ceremony of Suwa Shrine. At that time, Nagasaki was Japan''s sole window onto the outside world during the period of national seclusion, with trade conducted only with the Dutch and Chinese, and foreign culture permeated the city''s townspeople culture deeply. This produced uniquely international performances — the Dragon Dance derived from Chinese traditions, the "Dutch Ship" floats modeled after Dutch trading vessels, and many others — which have been passed down through approximately 400 years of history. In 1979, the dedicatory performances were designated as an Important Intangible Folk Cultural Property of Japan.

## Highlights

The festival''s central attraction is the rotating roster of distinctive performances dedicated by each neighborhood on a seven-year cycle. The Chinese-influenced Dragon Dance (Ja-odori) features a 20-meter-long dragon swirling in dynamic patterns to the thunderous beat of large drums and gongs. Kokkodesho, performed by the Kabashima district, involves 36 men hurling a one-ton drum platform high into the air to thrilling effect — drawing shouts of "Mottekoi!" ("Bring it back!") from the crowd, the local equivalent of an encore call. Other distinctively Nagasaki performances include Kawafune (River Boat), Kujira no Shiofuki (Whale''s Water Spout), and Oranda Manzai (Dutch Comic Dialogue), unfolding one after another. Venues include the precincts of Suwa Shrine, Yasaka Shrine, the Otabisho, and the plaza in front of the Public Hall.

## Event Information

The main venue is Chinzei Taisha Suwa Shrine in Kami-Nishiyama, Nagasaki City, along with several other locations throughout the city. The nearest stop is Suwa Jinja Station on the Nagasaki Electric Tramway, about a 3-minute walk away. The festival is held annually on October 7 (eve), 8 (middle day), and 9 (final day). Reserved seating within the shrine grounds is by advance lottery and ticketed, while some viewing areas at the Otabisho and Yasaka Shrine are free. The festival attracts approximately 600,000 visitors over its three days, including many from overseas.

## Nearby Attractions

Nagasaki City lies at the heart of the UNESCO World Heritage Site "Hidden Christian Sites in the Nagasaki Region," and the city is dense with historical attractions including Ōura Cathedral, Glover Garden, and Dejima (the former Dutch trading post). The Atomic Bomb Museum and Peace Park offer profound reflections on war and peace. Nagasaki Chinatown serves authentic Chinese cuisine, while Mount Inasa Observatory offers a sweeping view of the city — one of the world''s three new top night views. Hotel rooms book up months in advance for the festival period, so early reservations are strongly recommended.','nagasaki-kunchi','nagasaki-kunchi',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q210150','花見','hanami','主に桜の花を鑑賞し、春の訪れを寿ぐ風習','Japanese traditional custom of enjoying the transient beauty of flowers',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/Castle%20Himeji%20sakura02.jpg','https://ja.wikipedia.org/wiki/%E8%8A%B1%E8%A6%8B','https://en.wikipedia.org/wiki/Hanami',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q116021','多度祭','Tado Festival','三重県桑名市多度町で毎年5月4日、5日に行われる祭り','Japanese festival','Q116140','多度大社','Tado Taisha','三重県','kinki',NULL,NULL,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/Tado%20Festival%202.jpg','https://ja.wikipedia.org/wiki/%E5%A4%9A%E5%BA%A6%E7%A5%AD','https://en.wikipedia.org/wiki/Tado_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q866977','彼岸','Higan','日本の雑節の一つ','Buddhist holiday exclusively during both the Spring and Autumnal Equinox',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BD%BC%E5%B2%B8','https://en.wikipedia.org/wiki/Higan',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q834387','山形国際ドキュメンタリー映画祭','Yamagata International Documentary Film Festival',NULL,'film festival in Japan','Q205526','山形市','Yamagata','山形県','tohoku',NULL,NULL,1989,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B1%B1%E5%BD%A2%E5%9B%BD%E9%9A%9B%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%82%BF%E3%83%AA%E3%83%BC%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Yamagata_International_Documentary_Film_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q844110','雛祭り','Hinamatsuri','毎年3月3日に行われる、日本の年中行事のひとつ','Japanese holiday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/Ist%20di%20Cultura%20giapponese%20-%20altare%20della%20festa%20delle%20bambole%20P1100919.JPG','https://ja.wikipedia.org/wiki/%E9%9B%9B%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Hinamatsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q773085','葵祭','Aoi Matsuri','京都市の賀茂御祖神社と賀茂別雷神社で行われる例祭','traditional Japanese Festival in Kyoto','Q11401356','北大路通','Kitaōji Street','京都府','kinki',NULL,NULL,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/Aoi%20Matsuri.jpg','https://ja.wikipedia.org/wiki/%E8%91%B5%E7%A5%AD','https://en.wikipedia.org/wiki/Aoi_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q862407','青森ねぶた','Aomori Nebuta Matsuri','日本の青森県青森市で毎年8月に開催される祭','Japanese summer festival','Q146790','青森市','Aomori','青森県','tohoku',40.822342,140.74739,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Aomori%20Nebuta%20Festival%20Float%20August%202006.jpg','https://ja.wikipedia.org/wiki/%E9%9D%92%E6%A3%AE%E3%81%AD%E3%81%B6%E3%81%9F','https://en.wikipedia.org/wiki/Aomori_Nebuta_Matsuri',95,'drafted','## 概要

青森ねぶた祭（あおもりねぶたまつり）は、青森県青森市で毎年8月2日から7日までの6日間にわたって開催される、日本を代表する夏の伝統祭礼である。「ねぶた」と呼ばれる高さ約5メートル、幅約9メートルの巨大な人形灯籠（運行台車含め重さ4トン）が市内を練り歩く勇壮華麗な姿で世界的に有名で、1980年（昭和55年）に国の重要無形民俗文化財に指定され、毎年約280万人の観光客が訪れる東北最大級の夏祭りである。

## 歴史

青森ねぶたの起源は奈良時代に遡るとされ、坂上田村麻呂が蝦夷征討の際に巨大な人形灯籠で敵を欺いたという伝承が有名だが、史実としては七夕の「眠り流し」と呼ばれる眠気払いの行事と灯籠流しの風習が融合して成立した民俗行事と考えられている。江戸時代後期から青森城下町の町人文化として発展し、明治・大正期を経て次第に大型化、人形の意匠も歌舞伎・神話・歴史上の英雄をモチーフとした豪華絢爛なものへと進化した。戦後は青森市の観光行事として大規模化し、ねぶた師（人形製作の職人）の名匠たちが代々技術を継承する一大伝統工芸祭礼となった。

## 見どころ

最大の見どころは8月2-6日の夜間運行で、20数台の大型ねぶたが「ラッセラー、ラッセラー」の掛け声と笛・太鼓の囃子に乗って市内中心部を巡行する。跳人（はねと）と呼ばれる踊り手が浴衣姿で飛び跳ねながら囃子に合わせて踊る姿は、観客との一体感を生む祭りの真髄。8月7日には昼間の「市内合同運行」と夜の「青森花火大会・ねぶた海上運行」が行われ、ねぶたを台船に乗せて青森湾に浮かべる幻想的な光景でフィナーレを迎える。ねぶた師の技と伝統工芸の粋を集めた巨大灯籠の造形美は、海外メディアからも高く評価されている。

## 開催情報・アクセス

会場は青森県青森市中心部の青森駅東口周辺から国道4号沿いの大通り。JR青森駅・新青森駅から徒歩圏内。観覧は無料（一部有料席あり）。期間中は青森ねぶた祭協賛会と青森市が主催。観覧時間は18:00-21:00頃が中心。

## 周辺観光

青森市内には「ねぶたの家ワ・ラッセ」（ねぶた常設展示館）、青森県立美術館（奈良美智作品で世界的に有名）、八甲田丸（青函連絡船メモリアルシップ）、三内丸山遺跡（縄文時代・世界遺産候補）など歴史・文化観光地が集中する。郊外には十和田湖・奥入瀬渓流、青函トンネル記念館、酸ヶ湯温泉、弘前城（東北唯一の現存天守）など、青森県の自然と歴史を堪能できる観光資源が豊富。夏はインバウンド観光の人気目的地でもある。','## Overview

The Aomori Nebuta Festival (Aomori Nebuta Matsuri) is one of Japan''s most iconic summer traditional festivals, held annually from August 2 to 7 in Aomori City, Aomori Prefecture. World-famous for its spectacular procession of enormous illuminated paper lantern figures called "Nebuta"—approximately 5 meters tall, 9 meters wide, and weighing up to 4 tons including the carrying platform—parading through the city streets, the festival was designated as a National Important Intangible Folk Cultural Property in 1980 (Shōwa 55) and attracts approximately 2.8 million visitors annually, ranking among the largest summer festivals of the Tōhoku region.

## History

The origins of Aomori Nebuta are believed to trace back to the Nara period, with the famous legend that Sakanoue no Tamuramaro deceived enemies with giant illuminated figures during his campaigns against the Emishi people. As a matter of historical record, however, the festival is believed to have developed as a folk event combining the "Nemuri-nagashi" drowsiness-dispelling ritual of the Tanabata festival with the custom of floating lanterns. From the late Edo period onward, it developed as a townspeople''s culture in the Aomori castle town, gradually growing in scale through the Meiji and Taishō eras, with figure designs evolving into magnificent and ornate representations of kabuki characters, mythological figures, and historical heroes. After World War II, it expanded into a major tourism event sponsored by Aomori City, becoming a great traditional craft festival where master "nebuta-shi" (figure-making artisans) transmit their techniques across generations.

## Highlights

The festival''s greatest highlight is the evening procession from August 2-6, when more than 20 large nebuta floats parade through the city center accompanied by chants of "Rassera, Rassera" and the rhythms of flutes and drums. Dancers called "Haneto" (Jumpers) wearing yukata leap and dance in time with the music, embodying the festival''s essence of unity between performers and spectators. On August 7, the festival features the daytime "Citywide Joint Procession" and the nighttime "Aomori Fireworks and Nebuta Maritime Procession," when nebuta floats are loaded onto barges and float across Aomori Bay in a magical finale. The artistic excellence of these enormous illuminated figures, embodying the height of the nebuta-shi craft and traditional artistry, has received high acclaim from international media.

## Event Details and Access

The venue is the central area of Aomori City, ranging from the area around the east exit of Aomori Station to the main avenue along National Route 4. Access is within walking distance of Aomori Station and Shin-Aomori Station on the JR lines. Viewing is free of charge (with some reserved paid seating available). The festival is hosted by the Aomori Nebuta Festival Sponsorship Association and Aomori City. Viewing hours center on 6:00 p.m. to 9:00 p.m.

## Surrounding Attractions

Aomori City features a concentration of historical and cultural attractions including the Nebuta no Ie Wa-Rasse (a permanent nebuta exhibition hall), the Aomori Museum of Art (world-famous for works by artist Yoshitomo Nara), the Hakkōda Maru (a memorial ship of the former Seikan Ferry), and the Sannai Maruyama Archaeological Site (a Jōmon-period UNESCO World Heritage candidate). The surrounding area offers Lake Towada and the Oirase Mountain Stream, the Seikan Tunnel Memorial Museum, Sukayu Hot Spring, and Hirosaki Castle (the only original castle keep in the Tōhoku region), providing rich tourism resources for experiencing the nature and history of Aomori Prefecture. Summer makes the area a particularly popular destination for international inbound tourism.','aomori-nebuta','aomori-nebuta',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q929531','さっぽろ雪まつり','Sapporo Snow Festival','北海道札幌市で毎年2月に開催される雪と氷の祭典','festival held annually in Sapporo, Japan','Q37951','札幌市','Sapporo','北海道','hokkaido',43.061047,141.35638,1950,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/SapporoFestival8.JPG','https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%A3%E3%81%BD%E3%82%8D%E9%9B%AA%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Sapporo_Snow_Festival',95,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q888184','日前神宮・國懸神宮','Hinokuma Jingū','和歌山市にある神社','building in Wakayama Prefecture, Japan',NULL,NULL,NULL,'和歌山県','kinki',34.228398,135.201993,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hinokuma%20Shrine.JPG','https://ja.wikipedia.org/wiki/%E6%97%A5%E5%89%8D%E7%A5%9E%E5%AE%AE%E3%83%BB%E5%9C%8B%E6%87%B8%E7%A5%9E%E5%AE%AE','https://en.wikipedia.org/wiki/Hinokuma_Shrine',95,'drafted','## 概要

日前神宮・國懸神宮（ひのくまじんぐう・くにかかすじんぐう）は、和歌山県和歌山市秋月（あきづき）に鎮座する紀伊国一宮であり、皇室の祖神に縁深い格式の高い古社である。日前神宮には日前大神（ひのくまのおおかみ・天照大神の御神体である日像鏡を祀る）、國懸神宮には國懸大神（くにかかすのおおかみ・天照大神の御神体である日矛鏡を祀る）を主祭神として祀り、同一境内に二つの神宮が並び立つ独特の形態を持つ。『延喜式神名帳』では名神大社に列せられ、伊勢神宮に次ぐ「準勅祭社」の格式を持つ。

## 歴史

日前神宮・國懸神宮の創建は神武天皇東征の時代に遡るとされ、『日本書紀』の伝承によれば、天照大神の御神体として石凝姥命（いしこりどめのみこと）が作った鏡のうち、日像鏡が日前神宮に、日矛鏡が國懸神宮に祀られたとされる。両神宮は紀伊国造（きいのくにのみやつこ）家である紀氏が代々祭祀を司り、古代から朝廷の篤い崇敬を受けてきた。『延喜式神名帳』（927年）では名神大社、特に重要な「准伊勢神宮」格として位置付けられ、明治期の近代社格制度では官幣大社に列せられた。皇室祭祀との深い関わりを持つ紀伊国一宮として、関西地方有数の格式高い神社である。

## 見どころ

両神宮は同一の広大な境内に並んで鎮座し、伊勢神宮を彷彿とさせる神明造系の社殿建築が深い杜に映える。境内は約8万坪と広大で、楠の巨木が林立する社叢は和歌山県の天然記念物に指定されている。日前神宮と國懸神宮の二つの本殿が並んで建つ独特の景観は他に類を見ず、皇祖神信仰と日本古代の鏡信仰の中核を体感できる。境内には水盤舎、随神門、宝物殿などの建造物があり、紀伊国造家ゆかりの文物・古文書が伝えられている。例祭は4月26日（春季）と10月26日（秋季）で、雅楽奉納・神事が厳粛に執り行われる。

## 開催情報・アクセス

会場は日前神宮・國懸神宮（和歌山県和歌山市秋月365）。JR和歌山駅から徒歩約20分または車で約10分、和歌山電鐵貴志川線日前宮駅から徒歩約2分。境内参拝は早朝から夕方まで自由（拝観時間あり）。

## 周辺観光

和歌山市内には和歌山城（御三家・紀州徳川家の居城）、紀三井寺（西国三十三所第2番）、和歌浦・玉津島神社、雑賀崎、紀州東照宮など歴史観光地が集中する。和歌山県内では高野山（世界遺産・真言密教の聖地）、熊野古道（世界遺産）、那智の滝・熊野那智大社、白浜温泉、串本海岸など、紀伊半島の信仰・自然・温泉文化を堪能できる観光資源が豊富。日前神宮・國懸神宮は熊野詣の前後参拝としても古来重視されてきた。','## Overview

Hinokuma Jingū and Kunikakasu Jingū (Hinokuma Shrine and Kunikakasu Shrine) constitute the Ichinomiya (first-ranked shrine) of Kii Province, located in Akizuki, Wakayama City, Wakayama Prefecture, and stand as ancient shrines of the highest dignity with deep connections to the imperial ancestral deities. Hinokuma Jingū enshrines Hinokuma no Ōkami (worshipping the Hi-no-kata-no-Kagami, one of the sacred mirror objects of Amaterasu), while Kunikakasu Jingū enshrines Kunikakasu no Ōkami (worshipping the Hihoko-no-Kagami, another sacred mirror object of Amaterasu). The two shrines stand together in a single precinct in a unique configuration. In the Engishiki Jinmyōchō, both were ranked as Myōjin Taisha (Major Shrines of Famous Deities) and held the prestigious "Quasi-Imperial Festival Shrine" status second only to the Ise Grand Shrine.

## History

The founding of Hinokuma Jingū and Kunikakasu Jingū traces back to the era of Emperor Jinmu''s eastern campaign. According to the traditions of the Nihon Shoki, among the mirrors created by Ishikoridome no Mikoto as sacred objects of Amaterasu, the Hi-no-kata-no-Kagami was enshrined at Hinokuma Jingū and the Hihoko-no-Kagami at Kunikakasu Jingū. The Ki clan, the Kuni no Miyatsuko (provincial governors) of Kii Province, conducted the rituals at both shrines across generations, and the shrines received deep veneration from the imperial court since ancient times. In the Engishiki Jinmyōchō (927), both were ranked as Myōjin Taisha and especially positioned as "Quasi-Ise Grand Shrine" status, and under the modern shrine ranking system of the Meiji era, both were designated as Kanpei Taisha (Major Imperial Shrines). As the Ichinomiya of Kii Province with deep connections to imperial rituals, they stand among the most prestigious shrines of the Kansai region.

## Highlights

The two shrines stand side by side in an expansive precinct, with Shinmei-zukuri style shrine architecture evoking the Ise Grand Shrine standing beautifully amid deep forest. The precincts span approximately 80,000 tsubo (about 26 hectares), and the sacred grove with its towering camphor trees has been designated as a Natural Monument of Wakayama Prefecture. The unique landscape of two main shrine halls standing parallel is unmatched elsewhere, allowing visitors to experience the core of imperial ancestral faith and ancient Japanese mirror worship. The precincts feature a water purification hall (mizubasha), divine gate (zuishin-mon), and treasure hall, preserving artifacts and ancient documents connected to the Ki clan provincial governors. The annual main festivals are held on April 26 (spring) and October 26 (autumn), featuring solemn gagaku court music dedications and sacred rituals.

## Event Details and Access

The venue is Hinokuma Jingū and Kunikakasu Jingū (365 Akizuki, Wakayama City, Wakayama Prefecture). Access is approximately 20 minutes on foot or 10 minutes by car from Wakayama Station on the JR lines, or approximately 2 minutes on foot from Hinokuma-gū Station on the Wakayama Dentetsu Kishigawa Line. The precincts are open for worship from early morning to evening (with specific viewing hours).

## Surrounding Attractions

Wakayama City features a concentration of historical attractions including Wakayama Castle (the residence of the Kii Tokugawa family, one of the three Tokugawa branch families), Kimiidera Temple (the 2nd temple on the Saigoku Pilgrimage), Wakanoura and Tamatsushima Shrine, Saikazaki, and Kishū Tōshō-gū. Within Wakayama Prefecture, abundant tourism resources allow visitors to experience the faith, nature, and hot spring culture of the Kii Peninsula, including Mount Kōya (a UNESCO World Heritage Site and sacred place of Shingon Buddhism), the Kumano Kodō pilgrimage routes (a World Heritage Site), Nachi Falls and Kumano Nachi Taisha, Shirahama Hot Spring, and Kushimoto Coast. Hinokuma Jingū and Kunikakasu Jingū have historically been important pilgrimage stops both before and after the Kumano pilgrimage.','hinokuma-kunikakasu-jingu','hinokuma-kunikakasu-jingu',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q979873','祇園祭','Gion Matsuri','京都市の祭り','festival in Kyoto city, Japan','Q692714','八坂神社','Yasaka Shrine','京都府','kinki',NULL,NULL,869,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Gion%20Matsuri%202017-5.jpg','https://ja.wikipedia.org/wiki/%E7%A5%87%E5%9C%92%E7%A5%AD','https://en.wikipedia.org/wiki/Gion_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q911345','CON-CANムービーフェスティバル','CON-CAN Movie Festival',NULL,'film festival',NULL,NULL,NULL,'千葉県','kanto',35.67659,139.70793,2005,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/CON-CAN%E3%83%A0%E3%83%BC%E3%83%93%E3%83%BC%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/CON-CAN_Movie_Festival',70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q901495','ゆうばり国際ファンタスティック映画祭','Yubari International Fantastic Film Festival','日本の北海道夕張市で開かれている映画祭','film festival','Q637145','夕張市','Yūbari-shi','北海道','hokkaido',NULL,NULL,1990,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%86%E3%81%86%E3%81%B0%E3%82%8A%E5%9B%BD%E9%9A%9B%E3%83%95%E3%82%A1%E3%83%B3%E3%82%BF%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Yubari_International_Fantastic_Film_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q903645','国際花と緑の博覧会','Expo ''90','1990年に大阪府の鶴見緑地で行われた国際博覧会','international gardening exposition held in Tsurumi Ryokuchi, Osaka','Q11615139','花博記念公園鶴見緑地','Tsurumiryokuchi Expo ''90 Commemorative Park','大阪府','kinki',34.71216667,135.57416667,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/EXPO%201990.JPG','https://ja.wikipedia.org/wiki/%E5%9B%BD%E9%9A%9B%E8%8A%B1%E3%81%A8%E7%B7%91%E3%81%AE%E5%8D%9A%E8%A6%A7%E4%BC%9A','https://en.wikipedia.org/wiki/Expo_%2790',95,'drafted','## 概要

国際花と緑の博覧会（こくさいはなとみどりのはくらんかい・通称「花博」「EXPO''90」）は、1990年（平成2年）4月1日から9月30日までの183日間、大阪府大阪市鶴見区の花博記念公園鶴見緑地で開催された国際園芸博覧会である。国際園芸家協会（AIPH）認定A1クラス（最高位）・国際博覧会条約（BIE）特別博として開催され、日本で初めての本格的な国際園芸博覧会として2,312万人を動員した歴史的なイベントである。

## 歴史

国際花と緑の博覧会は、1990年に開催された大阪市制施行100周年記念事業として企画され、国際園芸家協会（AIPH）と国際博覧会事務局（BIE）の認定を受けた本格的な国際博覧会として開催された。テーマは「花と緑と人間生活のかかわりをとらえ、21世紀へ向けて潤いのある豊かな社会の創造を目指す」というもので、自然と人間の共生・都市環境の緑化推進・園芸文化の国際交流を目的とした。会場となった鶴見緑地は元々大阪市の都市公園で、博覧会終了後は「花博記念公園鶴見緑地」として再整備され、現在も大阪市民の憩いの場として親しまれている。本博覧会の成功は、その後の日本における園芸文化の普及と緑化運動の推進に大きく貢献し、2027年に横浜で開催予定の「GREEN×EXPO 2027」へと続く系譜の起点となった。

## 見どころ

博覧会は83の国・国際機関・212の国内外企業・55の都道府県市等の出展により構成され、世界各地の伝統園芸文化と最先端の緑化技術が一堂に集った。「いのちの塔」（高さ85メートルの記念建造物・後にダウンタウンズ命名）や「咲くやこの花館」（現在も植物園として運営中）など、博覧会のために建設された施設のいくつかは現在も鶴見緑地で見学可能。会期中は世界各国の園芸ショー、フラワーパレード、コンサート、文化交流イベントなどが連日開催され、約2,300万人の来場者を迎えた歴史的盛況となった。

## 開催情報・アクセス

会場は花博記念公園鶴見緑地（大阪府大阪市鶴見区緑地公園2-163）。大阪メトロ長堀鶴見緑地線鶴見緑地駅から徒歩約1分。現在は公園として常時開放され、「咲くやこの花館」（大人500円）など博覧会跡施設の見学が可能。博覧会自体は1990年に終了。

## 周辺観光

鶴見緑地公園のほか、大阪市内には大阪城・大阪城公園、難波・心斎橋・道頓堀の繁華街、新世界・通天閣、海遊館、ユニバーサル・スタジオ・ジャパンなど多彩な観光資源が集中する。郊外には万博記念公園（1970年大阪万博跡・太陽の塔）、京都・奈良の古都との周遊も可能。2025年には大阪・関西万博が夢洲で開催され、大阪は2027年横浜のGREEN×EXPOへとつながる「博覧会の都市」としての系譜を継承している。','## Overview

The International Garden and Greenery Exposition (Kokusai Hana to Midori no Hakurankai, commonly known as "Hanahaku" or "EXPO''90") was an international horticultural exposition held over 183 days from April 1 to September 30, 1990 (Heisei 2) at the Hanahaku Memorial Park Tsurumi-ryokuchi in Tsurumi Ward, Osaka City, Osaka Prefecture. Held as an AIPH-certified A1-class event (the highest rank) and as a Special Exposition under the BIE (Bureau International des Expositions) Treaty, it stands as a historic event drawing 23.12 million visitors as Japan''s first full-scale international horticultural exposition.

## History

The International Garden and Greenery Exposition was planned as a commemorative project for the 100th anniversary of Osaka City''s municipal incorporation in 1990, and was held as a full-scale international exposition certified by both the International Association of Horticultural Producers (AIPH) and the Bureau International des Expositions (BIE). Its theme was "Capturing the Relationships among Flowers, Greenery, and Human Life: Toward the Creation of a Rich and Fulfilling Society for the 21st Century," aimed at promoting harmony between nature and humanity, urban greening initiatives, and international exchange of horticultural cultures. The venue at Tsurumi-ryokuchi had originally been a municipal park of Osaka City, and after the exposition''s conclusion was redeveloped as Hanahaku Memorial Park Tsurumi-ryokuchi, which continues today as a beloved recreational area for Osaka residents. The success of this exposition greatly contributed to the subsequent spread of horticultural culture and the promotion of greening movements in Japan, becoming the starting point of a lineage continuing to the GREEN×EXPO 2027 scheduled to be held in Yokohama.

## Highlights

The exposition was composed of exhibits by 83 countries and international organizations, 212 domestic and foreign corporations, and 55 prefectural and municipal governments, bringing together traditional horticultural cultures from around the world alongside cutting-edge greening technologies. Among the facilities built for the exposition, some remain accessible for viewing at Tsurumi-ryokuchi today, including the "Tower of Life" (an 85-meter-tall memorial structure later mentioned in popular culture) and "Sakuya Konohana-kan" (which continues to operate as a botanical garden). During the run, horticultural shows from countries around the world, flower parades, concerts, and cultural exchange events were held daily, welcoming approximately 23 million visitors in a historic success.

## Event Details and Access

The venue is Hanahaku Memorial Park Tsurumi-ryokuchi (2-163 Ryokuchi Kōen, Tsurumi Ward, Osaka City, Osaka Prefecture). Access is approximately 1 minute on foot from Tsurumi-ryokuchi Station on the Osaka Metro Nagahori Tsurumi-ryokuchi Line. The park is currently open year-round, and facilities remaining from the exposition such as Sakuya Konohana-kan (adult admission 500 yen) can be visited. The exposition itself concluded in 1990.

## Surrounding Attractions

In addition to Tsurumi-ryokuchi Park, central Osaka offers diverse tourism resources including Osaka Castle and Osaka Castle Park, the Namba, Shinsaibashi, and Dōtonbori commercial districts, Shinsekai and Tsutenkaku, Kaiyūkan Aquarium, and Universal Studios Japan. The suburbs feature Expo ''70 Commemorative Park (the site of the 1970 Osaka World Expo with the iconic Tower of the Sun), and combined tours with the ancient capitals of Kyoto and Nara are possible. The 2025 Osaka-Kansai Expo will be held on Yumeshima, continuing Osaka''s lineage as a "city of expositions" leading to the GREEN×EXPO 2027 in Yokohama.','expo-90-osaka-flower','expo-90-osaka-flower',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q912124','時代祭','Jidai Matsuri','平安神宮の例大祭に附属する年中行事','traditional Japanese festival in Kyoto','Q34600','京都市','Kyoto','京都府','kinki',35.011635,135.76804,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/JidaiMatsuri%20Gohouren.jpg','https://ja.wikipedia.org/wiki/%E6%99%82%E4%BB%A3%E7%A5%AD','https://en.wikipedia.org/wiki/Jidai_Matsuri',95,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11566547','瀬戸内国際芸術祭','Setouchi Triennale',NULL,'art festival in Seto Inland Sea','Q11520216','本島','Honjima',NULL,NULL,NULL,NULL,2010,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%80%AC%E6%88%B8%E5%86%85%E5%9B%BD%E9%9A%9B%E8%8A%B8%E8%A1%93%E7%A5%AD','https://en.wikipedia.org/wiki/Setouchi_Triennale',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11465151','尾島ねぷた','Ojima Neputa Festival',NULL,'festival in Japan',NULL,NULL,NULL,'青森県','tohoku',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B0%BE%E5%B3%B6%E3%81%AD%E3%81%B7%E3%81%9F','https://en.wikipedia.org/wiki/Ojima_Neputa_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11510099','日立風流物','Hitachi Fūryūmono','茨城県日立市に伝わる民俗文化財','Japanese festival with puppets','Q28683513','神峰神社','Kamine Shrine','茨城県','kanto',NULL,NULL,1695,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Furyumonoomoteyama.jpg','https://ja.wikipedia.org/wiki/%E6%97%A5%E7%AB%8B%E9%A2%A8%E6%B5%81%E7%89%A9','https://en.wikipedia.org/wiki/Hitachi_Furyumono',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11487216','弘前城菊と紅葉まつり','Hirosaki Castle Chrysanthemum and Autumn Foliage Festival',NULL,'annual autumn festival in Hirosaki, Japan','Q11288816','弘前公園','Hirosaki Park','青森県','tohoku',40.6039,140.4649,1962,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Hirosaki%20Castle%20chrysanthemum%20and%20autumn%20leaves%20festival%2003.jpg','https://ja.wikipedia.org/wiki/%E5%BC%98%E5%89%8D%E5%9F%8E%E8%8F%8A%E3%81%A8%E7%B4%85%E8%91%89%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Hirosaki_Castle_Chrysanthemum_and_Autumn_Leaves_Festival',90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11501518','新嘗祭','Niiname-no-Matsuri','日本の宮中祭祀のひとつ','Japanese harvest ritual',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Omike%28Yamatohime-no-miya%29%2001.JPG','https://ja.wikipedia.org/wiki/%E6%96%B0%E5%98%97%E7%A5%AD','https://en.wikipedia.org/wiki/Niiname-no-Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11487199','弘前さくらまつり','Hirosaki Cherry Blossom Festival',NULL,'cherry blossom festival in Hirosaki, Japan','Q11288816','弘前公園','Hirosaki Park','青森県','tohoku',40.6039,140.4649,1918,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hirosaki%20castle.jpg','https://ja.wikipedia.org/wiki/%E5%BC%98%E5%89%8D%E3%81%95%E3%81%8F%E3%82%89%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Hirosaki_Cherry_Blossom_Festival',90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11487218','弘前城雪燈籠まつり','Hirosaki Castle Snow Lantern Festival',NULL,'annual winter festival in Hirosaki, Japan','Q11288816','弘前公園','Hirosaki Park','青森県','tohoku',40.6039,140.4649,1977,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BC%98%E5%89%8D%E5%9F%8E%E9%9B%AA%E7%87%88%E7%B1%A0%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Hirosaki_Castle_Snow_Lantern_Festival',70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11487200','弘前ねぷた','Hirosaki Neputa','青森県弘前市で開催される夏祭り','summer festival in Hirosaki, Japan',NULL,NULL,NULL,'青森県','tohoku',40.6039,140.4649,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%C5%8Cgi%20Neputa.jpg','https://ja.wikipedia.org/wiki/%E5%BC%98%E5%89%8D%E3%81%AD%E3%81%B7%E3%81%9F','https://en.wikipedia.org/wiki/Hirosaki_Neputa_Festival',95,'drafted','## 概要

弘前ねぷた（ひろさきねぷた）は、青森県弘前市で毎年8月1日から7日にかけて執り行われる、津軽地方を代表する夏祭りである。「弘前ねぷたまつり」として国の重要無形民俗文化財に指定されており、青森ねぶた（青森市・ねぶたは「立体」）、五所川原立佞武多（五所川原市・「巨大」）と並ぶ津軽三大ねぷた・ねぶたのひとつに数えられる。扇形の山車「扇ねぷた」が特徴で、戦国時代の合戦絵巻を題材とした勇壮な絵が描かれる。

## 歴史

起源は江戸時代中期にまで遡るとされ、坂上田村麻呂が蝦夷征伐の際に大灯籠で敵をおびき寄せたという伝説や、津軽藩主による七夕の灯籠流しが起源とされる説など諸説ある。「ねぷた」の語源は「眠流し（ねむりながし）」で、夏の暑さによる眠気・農作業の妨げとなる眠りを灯籠とともに川に流す禊（みそぎ）の意味を持つとされる。1980年（昭和55年）に国の重要無形民俗文化財に指定された。

## 見どころ

最大の特徴は、扇形の「扇ねぷた」と呼ばれる山車である。直径約9メートルに達する大型の扇に、表（鏡絵）には三国志・水滸伝・歌舞伎演目などを題材とした勇壮な合戦絵、裏（見送り絵）には妖艶な美人画が描かれる。これは青森市の立体ねぶたとは対照的なスタイルで、津軽武士の質実剛健な気風を反映する。山車の運行に合わせて「ヤーヤドー」の掛け声と勇壮な太鼓・笛・鉦の囃子が街に響き、約80台の山車が市内を巡行する。期間中の観客動員は約160万人。

## 開催情報

開催地は青森県弘前市中心市街地（土手町・駅前大通りなどの巡行ルート）。最寄駅はJR奥羽本線「弘前駅」徒歩約15分（巡行ルートまで）。開催期間は毎年8月1日から7日まで（7日は「なぬか日ねぷた」と呼ばれ昼間運行）。運行時間は1〜6日が19:00頃から21:00頃まで、7日は10:00頃から13:00頃まで。観覧は無料で、有料桟敷席も土手町通りに設置される。8月初旬の弘前は涼しい夕方も冷え込むことがあるため、薄手の上着を持参するとよい。

## 周辺の見どころ

弘前公園（弘前城）は日本さくら名所100選の代表的存在で、現存12天守のひとつ「弘前城天守」を見学できる。津軽藩ねぷた村では、ねぷた制作の様子や津軽三味線の生演奏を年中観覧可能。岩木山神社・嶽温泉郷も近く、津軽富士「岩木山」を望む観光と組み合わせやすい。津軽の郷土料理「いがめんち」「貝焼き味噌」「けの汁」も祭礼の屋台で味わえる。','## Overview

Hirosaki Neputa (弘前ねぷた) is one of the Tsugaru region''s signature summer festivals, held annually from August 1 to 7 in Hirosaki City, Aomori Prefecture. Officially known as the Hirosaki Neputa Festival, it is designated as an Important Intangible Folk Cultural Property of Japan and counted among the "Three Great Neputa/Nebuta Festivals of Tsugaru" alongside the Aomori Nebuta (Aomori City, featuring three-dimensional floats) and Goshogawara Tachi Neputa (Goshogawara City, featuring giant standing floats). Hirosaki''s distinctive feature is its fan-shaped Ōgi Neputa floats, which display dramatic battle scenes drawn from Japanese and Chinese historical epics.

## History

The festival''s origins are said to date back to the mid-Edo period, with several theories — including a legend that Sakanoue no Tamuramaro used giant lanterns to lure enemy forces during his northern campaigns, and another tracing the festival to Tanabata lantern-floating rituals practiced by lords of the Tsugaru domain. The word "Neputa" is believed to derive from "nemuri-nagashi" (sleep-washing), referring to a purification ritual in which the drowsiness of summer — which hampered farm work — was floated away on rivers together with lanterns. In 1980 (Shōwa 55), the festival was designated as an Important Intangible Folk Cultural Property of Japan.

## Highlights

The festival''s defining feature is the Ōgi Neputa, fan-shaped floats reaching diameters of approximately 9 meters. The front face (kagamie, or "mirror picture") depicts heroic battle scenes drawn from the Romance of the Three Kingdoms, the Water Margin, and famous kabuki plays, while the rear face (miokurie, or "send-off picture") portrays graceful beauties. This stylistic restraint contrasts with the three-dimensional Nebuta of Aomori City and reflects the austere, disciplined character of the Tsugaru samurai tradition. As the floats are paraded, shouts of "Yāyadō!" ring through the streets, accompanied by the powerful rhythms of taiko drums, flutes, and gongs. Approximately 80 floats parade through the city during the festival, drawing about 1.6 million spectators over the seven days.

## Event Information

The festival is held in the central district of Hirosaki City, Aomori Prefecture, along parade routes including Dotemachi and the main street in front of the station. The nearest station is Hirosaki Station on the JR Ōu Main Line, about a 15-minute walk to the parade route. The festival runs annually from August 1 to 7, with the seventh day known as the Nanuka-bi Neputa, featuring daytime processions. Parades run from approximately 7:00 PM to 9:00 PM on days 1 through 6, and from about 10:00 AM to 1:00 PM on day 7. Admission is free, with paid reserved seating available along Dotemachi-dōri. Early-August evenings in Hirosaki can be cool, so a light jacket is recommended.

## Nearby Attractions

Hirosaki Park (Hirosaki Castle) is one of Japan''s Top 100 Cherry Blossom Spots and home to the original Hirosaki Castle Keep — one of only twelve original castle keeps still standing in Japan. At Tsugaru-han Neputa Village, visitors can observe Neputa float construction and enjoy live performances of Tsugaru shamisen year-round. Iwakiyama Shrine and the Dake Onsen hot-spring district are within easy reach, and the conical peak of Mount Iwaki (the "Tsugaru Fuji") provides a stunning backdrop. Local specialties such as igamenchi (squid fritters), kaiyaki miso (scallop and miso grilled in shell), and ke no shiru soup can be enjoyed at festival food stalls.','hirosaki-neputa','hirosaki-neputa',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11465312','尾張津島天王祭','Owari Tsushima Tennō Festival','津島神社の祭事','annual festival in Tsushima, Aichi, Japan','Q705136','津島神社','Tsushima Shrine','三重県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tushimatennousai1.JPG','https://ja.wikipedia.org/wiki/%E5%B0%BE%E5%BC%B5%E6%B4%A5%E5%B3%B6%E5%A4%A9%E7%8E%8B%E7%A5%AD','https://en.wikipedia.org/wiki/Tenno_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q219122','三社祭','Sanja Matsuri','ヤクザによる東京都台東区浅草の浅草神社の例大祭','Shinto festival in Japan','Q670049','浅草神社','Asakusa Shrine','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/View%20of%20mikoshi%20from%20sensoji%20Sanja%20Matsuri%202006-3.jpg','https://ja.wikipedia.org/wiki/%E4%B8%89%E7%A4%BE%E7%A5%AD','https://en.wikipedia.org/wiki/Sanja_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1046742','コミックマーケット','Comiket','世界最大規模の同人誌即売会','world''s largest dōjinshi fair, held twice a year in Tokyo, Japan','Q1359125','東京国際展示場','Tokyo Big Sight','東京都','kanto',35.630833333,139.796666666,1975,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/The%20Cosplayers%20of%20Comiket%2069.jpg','https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%9F%E3%83%83%E3%82%AF%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%83%E3%83%88','https://en.wikipedia.org/wiki/Comiket',95,'drafted','## 概要

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
','## Overview

Comic Market (Comiket) is the world''s largest doujinshi (self-published works) fair, held twice annually—in mid-August (Summer Comiket) and at the end of December (Winter Comiket)—at the Tokyo International Exhibition Center (Tokyo Big Sight) in Ariake, Koto Ward, Tokyo. Drawing several hundred thousand attendees per day and a cumulative 500,000 to 600,000 over three days, it stands as an iconic event symbolizing Japanese subculture and is internationally recognized.

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
- **Period**: Summer Comiket: three days in mid-August; Winter Comiket: three days at the end of December (including New Year''s Eve)
- **Access**: Approximately 3–7 minutes on foot from Kokusai-tenjijo Station (Rinkai Line) or Tokyo Big Sight Station (Yurikamome Line). Within 30 minutes from JR Shimbashi, Osaki, and Tokyo Stations
- **Participation**: General attendance requires same-day entry wristbands or advance purchase tickets. Circle participation is by advance application and lottery
- **Official Information**: [Comic Market Official Website](https://www.comiket.co.jp/)

## Nearby Attractions

The Tokyo Bay Area (Odaiba), where Tokyo Big Sight is located, is one of contemporary Tokyo''s representative tourist districts. Attractions including the National Museum of Emerging Science and Innovation, Odaiba Seaside Park, DiverCity Tokyo Plaza, Fuji TV Headquarters, and Rainbow Bridge are clustered within walking distance or a short ride on the Yurikamome, making it easy to combine Comiket attendance with Tokyo sightseeing.

Tokyo Station and Ginza are accessible within 20–30 minutes, and many visitors enjoy circuits combining Comiket with pop culture pilgrimages to Akihabara Electric Town, Ikebukuro Sunshine City, or Nakano Broadway. Since both August and December are peak tourism seasons in Tokyo, early accommodation booking is essential.

## Related Information

- Season: Mid-August (Summer) / Late December (Winter)
- Prefecture: Tokyo (Kanto Region)
- Origin: December 21, 1975 (First edition)
- Scale: 500,000–600,000 cumulative attendance per event; approximately 30,000 circles
- Organizer: Comic Market Preparatory Committee (non-profit organization)
','comiket','comiket',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q10869430','東京高円寺阿波おどり','Kōenji Awa Odori',NULL,'Summer street festival in Tokyo, Japan','Q3180833','高円寺','Kōenji','東京都','kanto',35.7038,139.65,1957,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Koenj%20awaodori3.jpg','https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E9%AB%98%E5%86%86%E5%AF%BA%E9%98%BF%E6%B3%A2%E3%81%8A%E3%81%A9%E3%82%8A','https://en.wikipedia.org/wiki/K%C5%8Denji_Awa_Odori',90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11255045','神嘗祭','Kanname-no-Matsuri','宮中および伊勢神宮で行われる祭祀','Japanese festival','Q687168','伊勢神宮','Ise Jingū','三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A5%9E%E5%98%97%E7%A5%AD','https://en.wikipedia.org/wiki/Kannamesai_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q289513','チャグチャグ馬コ','Chagu Chagu Umakko','岩手県滝沢市から盛岡市で実施される、農耕馬への感謝の祭り','horse festival in Morioka, Japon',NULL,NULL,NULL,'岩手県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Chagu-chagu%20Umakko%20parade%20near%20the%20Nakanohashi%20Bridge%202023b.jpg','https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%A3%E3%82%B0%E3%83%81%E3%83%A3%E3%82%B0%E9%A6%AC%E3%82%B3','https://en.wikipedia.org/wiki/Chagu_Chagu_Umakko',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1043431','東京国際映画祭','Tokyo International Film Festival','東京で毎年開催される映画祭','international film festival held annually in Tokyo, Japan','Q1490','東京都','Tokyo','東京都','kanto',35.6894,139.6917,1985,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Day%20bfefore%20Tokyo%20International%20Film%20festival%2C%20at%20EX%20Theater%20Roppongi.jpg','https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E5%9B%BD%E9%9A%9B%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Tokyo_International_Film_Festival',95,'drafted','## 概要

東京国際映画祭(Tokyo International Film Festival、略称TIFF)は、毎年10月下旬から11月上旬にかけて東京都心部で開催される、日本最大級の国際映画祭です。国際映画製作者連盟(FIAPF)公認のコンペティション部門を有する世界15の競争型映画祭の一つに位置づけられ、アジアを代表する映画文化の祭典として国際的に高い知名度を誇ります。

日比谷・有楽町・銀座エリアを中心とした複数の映画館で、世界各国から選ばれた長編作品・短編作品・アニメーション作品が10日間にわたって上映され、例年約25万人の映画ファンが訪れます。レッドカーペットには国内外の著名な俳優・監督が登壇し、秋の東京を華やかな映画文化で彩ります。

## 歴史と由来

東京国際映画祭は1985年(昭和60年)、日本映画産業界と東京都の主導により創設されました。日本初の本格的な国際映画祭として、世界の映画文化の交流拠点を東京に築くことを目的とし、第1回大会から国際映画製作者連盟(FIAPF)の公認を受けてスタートしています。

創設当初は2年に1度の隔年開催でしたが、1991年(平成3年)からは毎年開催へと移行し、アジア映画の発信地としての役割を強化してきました。2004年(平成16年)以降は六本木ヒルズを中心会場として展開し、2021年(令和3年)からは会場を日比谷・有楽町・銀座エリアへ移転。歴史ある宝塚劇場、TOHOシネマズ日比谷、角川シネマ有楽町など、東京の映画文化の象徴的な施設群を活用する形に再編されました。

コンペティション部門の最高賞である「東京グランプリ」は、アジアの新進気鋭の作家から世界的巨匠まで、多様な才能を発掘・顕彰する場として機能してきました。黒澤明監督の特集上映やジブリ作品の海外プロモーションなど、日本映画を世界に発信する役割も担っており、映画産業の国際的なハブとしての性格を強めています。

## 見どころ

**コンペティション部門**
世界各国から選ばれた長編作品が「東京グランプリ」をはじめとする各賞を競う、映画祭の核となる部門です。国際的に著名な映画人で構成される審査委員会による厳正な審査が行われ、受賞作はその後の国際映画祭巡回への登竜門となります。

**アジアの未来部門**
アジア圏の新進気鋭の監督による作品を上映する部門で、近年は韓国・中国・タイ・インドネシアなど多様な国の若手作家の発掘の場として注目を集めています。アジア映画の最前線に触れることができる貴重な機会です。

**Japan Now部門 / ニッポン・シネマ・ナウ**
最新の日本映画を世界に向けて発信する特集部門。話題の新作から実験的な作品まで幅広くラインナップされ、海外バイヤーやプレス向けの上映会も併設されます。

**オープニング・クロージングセレモニーとレッドカーペット**
開幕日の日比谷ステップ広場で行われるレッドカーペットイベントは、国内外の著名俳優・監督・プロデューサーが登壇する華やかな祭典。テレビ中継もされ、映画祭の象徴的な光景として親しまれています。

**ガラ・セレクション部門**
世界の主要映画祭で話題を呼んだ作品をいち早く日本で上映する部門。カンヌ・ヴェネチア・ベルリンといった他の国際映画祭の受賞作・話題作を、東京で先行体験できる貴重な機会です。

## 開催情報

- **開催地**: 東京都心部(日比谷・有楽町・銀座エリアを中心とした複数会場)
- **主な会場**: TOHOシネマズ日比谷、角川シネマ有楽町、東京宝塚劇場、東京国際フォーラム、EX THEATER ROPPONGIなど
- **開催時期**: 毎年10月下旬から11月上旬の約10日間
- **アクセス**: 日比谷駅(東京メトロ日比谷線・千代田線・都営三田線)、有楽町駅(JR山手線・京葉線、東京メトロ有楽町線)、銀座駅(東京メトロ銀座線・丸ノ内線・日比谷線)から徒歩圏内
- **観覧料**: 一般上映1作品1,500円〜2,000円程度。オープニング・クロージング作品やガラ・セレクションは別料金
- **公式情報**: [東京国際映画祭公式サイト](https://2025.tiff-jp.net/)

## 周辺の見どころ

映画祭のメイン会場である日比谷・有楽町・銀座エリアは、東京を代表する文化・商業の中心地です。日比谷公園や皇居外苑といった都心の緑地、銀座の高級ブランド街、丸の内の歴史的建造物群が徒歩圏内に集まり、映画鑑賞の合間に東京の多層的な魅力を体感できます。

東京駅周辺には三菱一号館美術館、国立映画アーカイブといった文化施設が点在し、映画ファンには国立映画アーカイブで開催される常設・企画上映との組み合わせ観覧もおすすめです。また六本木ヒルズや国立新美術館、サントリー美術館までも地下鉄で15分圏内にあり、現代アートと映画を併せて楽しむ文化周遊が可能です。

10月下旬から11月上旬の東京は、紅葉が始まる前の穏やかな気候で、屋外イベントと屋内鑑賞を組み合わせた旅程に最適なシーズンです。

## 関連情報

- 開催月: 10月下旬〜11月上旬(秋)
- 都道府県: 東京都(関東)
- 起源: 1985年(第1回開催)
- 規模: 約25万人(観客動員数)
- 国際認定: 国際映画製作者連盟(FIAPF)公認コンペティション部門あり
','## Overview

The Tokyo International Film Festival (TIFF) is one of Japan''s largest international film festivals, held annually in central Tokyo from late October to early November. As one of only fifteen competitive feature film festivals officially accredited by the International Federation of Film Producers Associations (FIAPF), it stands as a representative cinematic celebration of Asia, enjoying high international recognition.

Centered in the Hibiya, Yurakucho, and Ginza districts, the festival screens feature films, short films, and animated works from around the world across multiple theaters over ten days, drawing approximately 250,000 film enthusiasts each year. Renowned actors and directors from Japan and abroad walk the red carpet, bringing a glamorous touch of cinematic culture to autumn Tokyo.

## History and Origins

The Tokyo International Film Festival was established in 1985 through the joint initiative of the Japanese film industry and the Tokyo Metropolitan Government. Founded as Japan''s first full-scale international film festival, it received FIAPF accreditation from its inaugural edition, with the aim of building a hub for global cinematic cultural exchange in Tokyo.

Originally held biennially, the festival transitioned to annual editions in 1991, strengthening its role as a platform for disseminating Asian cinema. From 2004 onward, Roppongi Hills served as the main venue, but in 2021 the festival relocated to the Hibiya, Yurakucho, and Ginza districts, restructuring around iconic Tokyo cinema venues such as the historic Takarazuka Theatre, TOHO Cinemas Hibiya, and Kadokawa Cinema Yurakucho.

The Tokyo Grand Prix, the highest award in the Competition section, has served as a venue for discovering and honoring diverse talent, from emerging Asian filmmakers to globally renowned masters. The festival has also played a key role in promoting Japanese cinema worldwide, hosting retrospectives of directors such as Akira Kurosawa and international promotion screenings for Studio Ghibli works, increasingly functioning as an international hub for the film industry.

## Highlights

**Competition Section**
The core of the festival, in which feature films selected from around the world compete for the Tokyo Grand Prix and other awards. A jury composed of internationally renowned film professionals conducts rigorous evaluations, with winning works often gaining entry into the international festival circuit.

**Asian Future Section**
A section featuring works by emerging directors from across Asia, attracting attention in recent years as a discovery ground for young auteurs from countries including South Korea, China, Thailand, and Indonesia. It offers a valuable opportunity to encounter the cutting edge of Asian cinema.

**Japan Now Section / Nippon Cinema Now**
A special program dedicated to introducing the latest Japanese films to the world. Featuring a wide range of works from buzzed-about new releases to experimental productions, it also includes screenings tailored for overseas buyers and press.

**Opening and Closing Ceremonies with Red Carpet**
The opening day red carpet event held at Hibiya Step Square is a glamorous celebration attended by renowned actors, directors, and producers from Japan and abroad. Broadcast on television, it has become a symbolic scene of the festival.

**Gala Selection Section**
A section presenting works that have generated buzz at major international film festivals worldwide, offering early Japanese screenings. It provides a precious opportunity to experience award-winning and acclaimed works from Cannes, Venice, and Berlin in Tokyo.

## Event Information

- **Location**: Central Tokyo (multiple venues centered in the Hibiya, Yurakucho, and Ginza districts)
- **Main Venues**: TOHO Cinemas Hibiya, Kadokawa Cinema Yurakucho, Tokyo Takarazuka Theatre, Tokyo International Forum, EX THEATER ROPPONGI, and others
- **Period**: Approximately ten days from late October to early November annually
- **Access**: Within walking distance from Hibiya Station (Tokyo Metro Hibiya, Chiyoda, and Toei Mita lines), Yurakucho Station (JR Yamanote and Keiyo lines, Tokyo Metro Yurakucho line), and Ginza Station (Tokyo Metro Ginza, Marunouchi, and Hibiya lines)
- **Admission**: General screenings range from approximately JPY 1,500 to 2,000 per film. Opening, closing, and Gala Selection screenings are priced separately
- **Official Information**: [Tokyo International Film Festival Official Website](https://2025.tiff-jp.net/)

## Nearby Attractions

The Hibiya, Yurakucho, and Ginza districts that host the festival are among Tokyo''s leading cultural and commercial hubs. Hibiya Park, the Imperial Palace Outer Gardens, the luxury brand streets of Ginza, and the historic architecture of Marunouchi all lie within walking distance, allowing visitors to experience Tokyo''s multilayered charm between screenings.

The Tokyo Station area houses cultural facilities such as the Mitsubishi Ichigokan Museum and the National Film Archive of Japan, the latter offering permanent and special screenings highly recommended for cinema enthusiasts. Roppongi Hills, the National Art Center, and the Suntory Museum of Art are all within a 15-minute subway ride, enabling a cultural tour combining contemporary art with cinema.

Tokyo from late October to early November enjoys mild weather just before the autumn foliage peak, making it an ideal season for itineraries combining outdoor events and indoor screenings.

## Related Information

- Season: Late October to early November (Autumn)
- Prefecture: Tokyo (Kanto Region)
- Origin: 1985 (First edition)
- Scale: Approximately 250,000 attendees
- International Accreditation: FIAPF-accredited competitive film festival
','tokyo-international-film-festival','tokyo-international-film-festival',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11249715','TOKYO IDOL FESTIVAL','Tokyo Idol Festival','2010年より開催されている日本の音楽イベント','annual music event in Japan','Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,2010,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/TOKYO_IDOL_FESTIVAL','https://en.wikipedia.org/wiki/Tokyo_Idol_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q446474','酒まつり','Sake Matsuri','毎年10月第2土・日曜の2日間にわたって広島県東広島市西条町の西条中央公園と西条酒蔵通りを中心にして行われる祭り',NULL,NULL,NULL,NULL,'広島県','chugoku',NULL,NULL,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Saij%C5%8D%20Sake%20Matsuri%202017.jpg','https://ja.wikipedia.org/wiki/%E9%85%92%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Saij%C5%8D_Sake_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q493695','唐津くんち','Karatsu Kunchi','佐賀県唐津市にある唐津神社の秋季例大祭','festival in Japan','Q11418639','唐津神社','Karatsu Shrine','佐賀県','kyushu',33.445171292,129.967403864,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Hikiyama.jpg','https://ja.wikipedia.org/wiki/%E5%94%90%E6%B4%A5%E3%81%8F%E3%82%93%E3%81%A1','https://en.wikipedia.org/wiki/Karatsu_Kunchi',95,'drafted','## 概要

唐津くんち（からつくんち）は、佐賀県唐津市の唐津神社の秋季例大祭で、毎年11月2日から4日にかけて開催される、約400年の歴史を持つ伝統祭礼である。14台の豪華絢爛な「曳山（ひきやま）」が城下町を巡行する勇壮な姿で全国的に知られ、1980年（昭和55年）に国の重要無形民俗文化財に指定、2016年にはユネスコ無形文化遺産「山・鉾・屋台行事」の構成要素として登録された。

## 歴史

唐津くんちの起源は、寛文年間（1661-1673年）に唐津神社の秋季例大祭として始まったと伝わるが、本格的な曳山の登場は文政2年（1819年）の「赤獅子」が最古とされる。江戸後期から明治初期にかけて、唐津の町人たちが各町ごとに豪華な曳山を新調し、現在の14台体制が明治9年（1876年）の「七宝丸」をもって完成した。曳山は「武者・獅子・鯛・龍・兜・鳳凰・宝船」など多彩な題材で、漆と金箔を多用した重さ2-3トンの大型山車である。第二次世界大戦中も中断せず継承され、戦後は唐津市を代表する観光行事として規模を拡大した。

## 見どころ

最大の見どころは11月3日の「お旅所神幸」で、14台の曳山が囃子の音色に乗って唐津神社から西の浜お旅所まで約2キロを巡行する。曳山は「ヤァサーヤァサー」「エンヤーエンヤー」の掛け声と共に、500人以上の曳き子により西の浜の砂浜に勢いよく曳き込まれ、車輪が砂にめり込む中を力強く進む光景は圧巻。夜には提灯に灯りが入り、漆塗りの曳山が幻想的に浮かび上がる。11月2日の宵山、4日の町廻りも華やか。

## 開催情報・アクセス

会場は唐津神社（佐賀県唐津市南城内3-13）および唐津市中心部の旧城下町一帯。JR唐津駅から徒歩約10分。観覧は無料。3日間で約50万人の観光客が訪れる。曳山展示場では年間を通して全14台の曳山を観覧可能。

## 周辺観光

唐津市内には唐津城、旧唐津銀行（辰野金吾設計）、虹の松原（日本三大松原）、鏡山展望台などの歴史・自然観光地が集中する。郊外には呼子の朝市（イカ料理で全国的に有名）、名護屋城跡（豊臣秀吉の朝鮮出兵拠点）、玄海国定公園など、肥前国北部の歴史と海の幸を堪能できる観光資源が広がる。佐賀県内では吉野ヶ里遺跡、有田焼の里・有田町と組み合わせた周遊も人気。','## Overview

Karatsu Kunchi is a traditional festival with approximately 400 years of history, held annually from November 2 to 4 as the autumn grand festival of Karatsu Shrine in Karatsu City, Saga Prefecture. Renowned nationwide for the spectacular sight of 14 magnificent "hikiyama" (pulled floats) parading through the castle town, the festival was designated as a National Important Intangible Folk Cultural Property in 1980 (Shōwa 55) and registered as a constituent element of the UNESCO Intangible Cultural Heritage "Yama, Hoko, Yatai Float Festivals" in 2016.

## History

The origins of Karatsu Kunchi are believed to date back to the Kanbun era (1661-1673) as the autumn grand festival of Karatsu Shrine, though the full-scale appearance of hikiyama floats began with the "Akajishi" (Red Lion) of 1819 (Bunsei 2), the oldest extant float. From the late Edo to early Meiji periods, the townspeople of Karatsu each commissioned magnificent hikiyama for their respective districts, completing the current 14-float lineup with the "Shippōmaru" in 1876 (Meiji 9). The floats feature diverse motifs including warriors, lions, sea bream, dragons, helmets, phoenixes, and treasure ships, and are large, ornate constructions weighing 2-3 tons, generously decorated with lacquer and gold leaf. The festival continued uninterrupted even during World War II, and after the war it expanded in scale to become the signature tourism event representing Karatsu City.

## Highlights

The festival''s greatest highlight is the "Otabisho Shinkō" (Sacred Journey to the Shrine Outpost) on November 3, when all 14 hikiyama parade approximately 2 kilometers from Karatsu Shrine to the Nishi-no-Hama Otabisho. To the rhythms of festival music and accompanied by shouts of "Yāsā-Yāsā" and "Enya-Enya," more than 500 puller-children draw the floats vigorously onto the sandy beach of Nishi-no-Hama, where the wheels sink deep into the sand but are forced forward by sheer human strength—an overwhelming spectacle of communal effort. At night, lanterns are lit on the floats, causing the lacquered hikiyama to glow with magical beauty. The "Yoiyama" (Eve Festival) on November 2 and the "Machi-mawari" (Town Procession) on November 4 are also resplendent occasions.

## Event Details and Access

The venue is Karatsu Shrine (3-13 Minami-Jōnai, Karatsu City, Saga Prefecture) and the surrounding old castle town center. Access is approximately 10 minutes on foot from Karatsu Station on the JR lines. Viewing is free of charge. The three-day festival attracts approximately 500,000 visitors. The Hikiyama Exhibition Hall allows year-round viewing of all 14 hikiyama floats.

## Surrounding Attractions

Karatsu City features a concentration of historical and natural attractions including Karatsu Castle, the former Karatsu Bank building (designed by famed architect Tatsuno Kingo), Niji-no-Matsubara (the Rainbow Pine Grove, one of Japan''s three great pine groves), and the Kagamiyama Observation Deck. The surrounding area offers Yobuko''s famous morning market (renowned nationwide for squid cuisine), the Nagoya Castle ruins (Toyotomi Hideyoshi''s base for the Korean campaigns), and the Genkai Quasi-National Park, providing rich resources for experiencing the history and seafood bounty of northern Hizen Province. Within Saga Prefecture, combined tours with the Yoshinogari archaeological site and the Arita porcelain village in Arita Town are also highly popular among visitors.','karatsu-kunchi','karatsu-kunchi',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11193613','COMITIA','COMITIA','自主制作漫画誌展示即売会','doujinshi convention in Japan','Q1359125','東京国際展示場','Tokyo Big Sight','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/COMITIA','https://en.wikipedia.org/wiki/COMITIA',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1033843','パシフィック・ミュージック・フェスティバル','Pacific Music Festival','作曲家のレナード・バーンスタインが北海道札幌市で創設した国際教育音楽祭','an international classical music festival held annually in Sapporo, Japan',NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,1990,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Sapporo%20Art%20Park%20Outdoor%20Stage%20%282017%29.jpg','https://ja.wikipedia.org/wiki/%E3%83%91%E3%82%B7%E3%83%95%E3%82%A3%E3%83%83%E3%82%AF%E3%83%BB%E3%83%9F%E3%83%A5%E3%83%BC%E3%82%B8%E3%83%83%E3%82%AF%E3%83%BB%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Pacific_Music_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q746798','節分','Setsubun','雑節の一つ、各季節の始まりの日の前日、及びその日に行われる行事','Japanese holiday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Setsubun.jpg','https://ja.wikipedia.org/wiki/%E7%AF%80%E5%88%86','https://en.wikipedia.org/wiki/Setsubun',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q9359311','ASIAN KUNG-FU GENERATION presents NANO-MUGEN FES.','Nano-Mugen Festival',NULL,'annual music festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2003,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/ASIAN_KUNG-FU_GENERATION_presents_NANO-MUGEN_FES.','https://en.wikipedia.org/wiki/Nano-Mugen_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1032381','初詣','Hatsumōde','年が明けてから初めて神社や寺院などに参拝する行事',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'winter',NULL,'https://ja.wikipedia.org/wiki/%E5%88%9D%E8%A9%A3','https://en.wikipedia.org/wiki/Hatsum%C5%8Dde',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1045869','ヨコハマ映画祭','Yokohama Film Festival','日本の映画賞','Japanese film awards ceremony','Q38283','横浜市','Yokohama','神奈川県','kanto',NULL,NULL,1980,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%A8%E3%82%B3%E3%83%8F%E3%83%9E%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Yokohama_Film_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q722072','オズフェスト','Ozzfest',NULL,'former music festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1996,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Phil%20Anselmo.jpg','https://ja.wikipedia.org/wiki/%E3%82%AA%E3%82%BA%E3%83%95%E3%82%A7%E3%82%B9%E3%83%88','https://en.wikipedia.org/wiki/Ozzfest',80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11019445','川越氷川祭','Kawagoe Hikawa Festival','埼玉県川越市の川越氷川神社の祭礼','Japanese traditional dance','Q11549607','氷川神社','Hikawa Shrine','埼玉県','kanto',NULL,NULL,1648,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kawagoe%20Festival4.jpg','https://ja.wikipedia.org/wiki/%E5%B7%9D%E8%B6%8A%E6%B0%B7%E5%B7%9D%E7%A5%AD','https://en.wikipedia.org/wiki/Kawagoe_Hikawa_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q9302453','お水取り','Omizutori','毎年3月に日本の東大寺で行われる行事のひとつ','festival in Japan','Q3341341','東大寺二月堂','Nigatsu-dō','奈良県','kinki',NULL,NULL,760,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/Omizutori.jpg','https://ja.wikipedia.org/wiki/%E3%81%8A%E6%B0%B4%E5%8F%96%E3%82%8A','https://en.wikipedia.org/wiki/Omizutori',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11236230','デザインフェスタ','Design Festa',NULL,'biannual fashion and music festival in Tokyo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF','https://en.wikipedia.org/wiki/Design_Festa',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11596116','秩父夜祭','Chichibu Night Festival','埼玉県秩父市にある秩父神社の例祭','Chichibu Shrine''s annual festival celebrated on the nights of December 1-6','Q2963366','秩父神社','Chichibu Shrine','埼玉県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/ChichibuFes1.jpg','https://ja.wikipedia.org/wiki/%E7%A7%A9%E7%88%B6%E5%A4%9C%E7%A5%AD','https://en.wikipedia.org/wiki/Chichibu_Night_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28153869','ウルトラ・ジャパン','Ultra Japan','毎年9月にお台場で開催されているエレクトロニック・ダンス・ミュージックのイベント','electronic music festival in Tokyo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%BB%E3%82%B8%E3%83%A3%E3%83%91%E3%83%B3','https://en.wikipedia.org/wiki/Ultra_Japan',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653307','しろんご祭り','Shirongo Matsuri','三重県鳥羽市の菅島で受け継がれている海女の伝統行事','Japanese festival',NULL,NULL,NULL,'愛知県','chubu',34.5025,136.906388888,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%97%E3%82%8D%E3%82%93%E3%81%94%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Shirongo_Matsuri',75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11568692','熊谷うちわ祭','Kumagaya Uchiwa Festival',NULL,NULL,'Q41106','熊谷市','Kumagaya','埼玉県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%86%8A%E8%B0%B7%E3%81%86%E3%81%A1%E3%82%8F%E7%A5%AD','https://en.wikipedia.org/wiki/Kumagaya_Uchiwa_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30924149','豊年祭','Hōnen Matsuri','愛知県小牧市にある田縣神社の祭礼','Japanese festival','Q60581','田縣神社','Tagata Shrine','愛知県','chubu',35.315833333,136.941111111,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/H%C5%8Dnen%20Matsuri%202.JPG','https://ja.wikipedia.org/wiki/%E8%B1%8A%E5%B9%B4%E7%A5%AD_(%E7%94%B0%E7%B8%A3%E7%A5%9E%E7%A4%BE)','https://en.wikipedia.org/wiki/H%C5%8Dnensai',95,'drafted','## 概要

豊年祭（ほうねんさい）は、愛知県小牧市田縣町（たがたちょう）の田縣神社（たがたじんじゃ）で毎年3月15日に行われる、五穀豊穣・子孫繁栄・万物育成を祈願する古代農耕祭礼である。男性のシンボルを御神体とする神事として国際的に広く知られ、日本古来の生命崇拝・農耕信仰の素朴な原型を伝える希少な民俗祭として、毎年多くの国内外の参拝客が訪れる。

## 歴史

田縣神社は『延喜式神名帳』（927年）に式内社として記載される尾張国丹羽郡の古社で、御歳神（みとしのかみ）と玉姫命（たまひめのみこと）を祀る。御歳神は五穀豊穣の神、玉姫命は子孫繁栄・夫婦和合・万物育成の女神とされる。豊年祭の起源は弥生時代の農耕儀礼に遡るとされ、男性器を象徴する御神体「大男茎形（おおおわせがた）」を奉納することで稲作の豊穣と人々の生命力の更新を祈念してきた。中世以降は神仏習合を経て民俗祭として継承され、明治期の神仏分離後も古い形態を維持し、現在に至る。日本の生殖崇拝・農耕信仰の最も古層を伝える祭として民俗学的価値が極めて高い。

## 見どころ

祭礼のクライマックスは午後2時頃からの行列で、新調された木製の御神体（長さ約2.5メートル、重さ約280キロ）を厄年の男性が担ぎ、田縣神社から熊野社まで約1キロを練り歩く。地元の女性が小型の御神体を抱える「巫女行列」、餅まきも行われる。境内には多数の同様の御神体が奉納されており、夫婦和合・子授け・縁結びを祈願する参拝者で賑わう。国際的にも「Penis Festival」として広く報道され、海外からの観光客も多く訪れる。

## 開催情報・アクセス

会場は田縣神社（愛知県小牧市田県町152）。名鉄小牧線田県神社前駅から徒歩約5分。開催日は毎年3月15日（曜日固定）、午前10時頃から午後4時頃まで。参拝・観覧は無料、餅まきへの参加も自由。

## 周辺観光

小牧市内には小牧城・小牧山史跡公園、犬山市の犬山城（国宝）、明治村、リトルワールド、犬山温泉郷など、尾張地方の歴史と文化を堪能できる観光資源が集中する。豊年祭の対となる祭として、小牧市の北隣の犬山市・大縣神社（おおあがたじんじゃ）の「豊年祭（梵天祭）」（女性器を象徴・3月15日に近い日曜日開催）も合わせて訪問する周遊が定番。','## Overview

Hōnensai (Bountiful Harvest Festival) is an ancient agricultural festival held annually on March 15 at Tagata Shrine in Tagata-chō, Komaki City, Aichi Prefecture, dedicated to prayers for bountiful harvests, prosperity of descendants, and the flourishing of all living things. Internationally known as a Shinto ritual featuring a male symbol as its sacred object, the festival is recognized as a rare folk celebration preserving the primitive form of Japan''s ancient veneration of life and agricultural beliefs, drawing numerous domestic and international visitors each year.

## History

Tagata Shrine is an ancient shrine of Niwa District in Owari Province, recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927, enshrining Mitoshi no Kami and Tamahime no Mikoto. Mitoshi no Kami is the deity of bountiful harvests, while Tamahime no Mikoto is venerated as a goddess of prosperity of descendants, marital harmony, and the flourishing of all living things. The origins of Hōnensai are traced back to agricultural rituals of the Yayoi period, when offerings of the male-symbol sacred object "Ōowasegata" were made to pray for bountiful rice harvests and the renewal of the people''s vital force. From the medieval period onward, the festival continued as a folk celebration through the syncretism of Shinto and Buddhism, and maintained its ancient form even after the Meiji-era separation of Shinto and Buddhism. It holds exceptionally high folkloric value as a festival transmitting the oldest stratum of Japan''s reproductive veneration and agricultural beliefs.

## Highlights

The festival''s climax is the procession beginning around 2 p.m., in which men of the unlucky age (yakudoshi) shoulder a newly carved wooden sacred object (approximately 2.5 meters long and 280 kilograms in weight) and parade approximately 1 kilometer from Tagata Shrine to Kumano Shrine. A "miko procession" of local women carrying smaller sacred objects also takes place, along with a mochi-throwing ceremony. The precincts contain numerous similar sacred objects dedicated by worshippers, attracting visitors praying for marital harmony, fertility, and matchmaking. Widely reported internationally as the "Penis Festival," the event also draws many overseas tourists.

## Event Details and Access

The venue is Tagata Shrine (152 Tagata-chō, Komaki City, Aichi Prefecture). Access is approximately 5 minutes on foot from Tagata-Jinja-mae Station on the Meitetsu Komaki Line. The festival is held annually on March 15 (fixed date, regardless of day of the week), from around 10 a.m. to 4 p.m. Worship and viewing are free of charge, and participation in the mochi-throwing ceremony is open to all.

## Surrounding Attractions

Komaki City features tourism resources for experiencing the history and culture of the Owari region, including Komaki Castle, the Komaki-yama Historic Park, and nearby Inuyama City''s Inuyama Castle (a National Treasure), Meiji-mura open-air museum, Little World, and the Inuyama Hot Spring resort. As a counterpart festival to Hōnensai, the "Hōnensai (Bonten Festival)" held at Ōagata Shrine in neighboring Inuyama City—featuring a female-symbol sacred object and held on the Sunday closest to March 15—is traditionally visited as part of a paired sightseeing tour.','honensai-tagata-jinja','honensai-tagata-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q23044788','イメージフォーラム・フェスティバル','Image Forum Festival',NULL,NULL,'Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,1987,NULL,NULL,NULL,NULL,'https://en.wikipedia.org/wiki/Image_Forum_Festival',45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652601','大阪アジアン映画祭','Osaka Asian Film Festival',NULL,'film festival','Q35765','大阪市','Osaka','大阪府','kinki',NULL,NULL,2005,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Asahi%20Broadcasting%20Corporation%20headquarter.JPG','https://ja.wikipedia.org/wiki/%E5%A4%A7%E9%98%AA%E3%82%A2%E3%82%B8%E3%82%A2%E3%83%B3%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Osaka_Asian_Film_Festival',80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21075984','なら国際映画祭','Nara International Film Festival',NULL,'film festival','Q169134','奈良市','Nara','奈良県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%AA%E3%82%89%E5%9B%BD%E9%9A%9B%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Nara_International_Film_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q16941387',NULL,'Matsuyama Shiroyama Koen Cherry Blossom Festival',NULL,'festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://en.wikipedia.org/wiki/Matsuyama_Shiroyama_Koen_Cherry_Blossom_Festival',25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q13423122','七夕','Qixi Festival','アジア圏における節句・節日のひとつ','Chinese valentine festival, on the seventh day of the seventh month of the lunar calendar',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Niulang%20and%20Zhinv%20%28Long%20Corridor%29.JPG','https://ja.wikipedia.org/wiki/%E4%B8%83%E5%A4%95','https://en.wikipedia.org/wiki/Qixi_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q18578715','端午の節句','Tango no sekku','日本の祭り','Japanese festival on 5th May',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Flying%20Koi%20by%20tiseb%20in%20Nagasaki.jpg',NULL,'https://en.wikipedia.org/wiki/Tango_no_sekku',70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17222071','鳥取しゃんしゃん祭','Tottori Shan-Shan Festival','毎年8月中旬に鳥取市で開催されるイベント','a festival in Tottori, Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Shanshan2013-2.jpg','https://ja.wikipedia.org/wiki/%E9%B3%A5%E5%8F%96%E3%81%97%E3%82%83%E3%82%93%E3%81%97%E3%82%83%E3%82%93%E7%A5%AD','https://en.wikipedia.org/wiki/Shan-shan_festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q16642915','土用の丑の日','Midsummer Day of the Ox','土用の時期中で、十二支が丑に当たる日','Day of the Japanese calendar',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9C%9F%E7%94%A8%E3%81%AE%E4%B8%91%E3%81%AE%E6%97%A5','https://en.wikipedia.org/wiki/Midsummer_Ox_Day',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q16909481','SUPER ROCK ''85 IN JAPAN','Super Rock ''85 in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/SUPER_ROCK_%2785_IN_JAPAN','https://en.wikipedia.org/wiki/Super_Rock_%2785_in_Japan',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3610588','ひろしまフラワーフェスティバル','Hiroshima Flower Festival','広島県広島市で開催される祭り','annual Flower Festival in Japan',NULL,NULL,NULL,'広島県','chugoku',NULL,NULL,1977,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hana-no-to2.jpg','https://ja.wikipedia.org/wiki/%E3%81%B2%E3%82%8D%E3%81%97%E3%81%BE%E3%83%95%E3%83%A9%E3%83%AF%E3%83%BC%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Hiroshima_Flower_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q4947265','藤崎八旛宮秋季例大祭','Boshita Festival',NULL,'festival in Japan','Q167146','藤崎八旛宮','Fujisaki Hachimangū',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Boshita-kazarioroshi2009.9.19Higo-chiyukai.jpg','https://ja.wikipedia.org/wiki/%E8%97%A4%E5%B4%8E%E5%85%AB%E6%97%9B%E5%AE%AE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD','https://en.wikipedia.org/wiki/The_Great_Festival_of_Fujisaki_Hachimangu_Shrine',80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3837559','LOUD PARK','Loud Park Festival','日本で行われるヘヴィメタルのフェス','heavy metal festival held annually at Saitama Super Arena in Saitama City or Makuhari Messe in Chiba City, Japan','Q862452','幕張メッセ','Makuhari Messe',NULL,NULL,NULL,NULL,2006,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/LOUD_PARK','https://en.wikipedia.org/wiki/Loud_Park_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5288609','土居太鼓祭り','Doi taikomatsuri',NULL,NULL,NULL,NULL,NULL,'愛媛県','shikoku',33.965,133.43,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9C%9F%E5%B1%85%E5%A4%AA%E9%BC%93%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Doi_taikomatsuri',70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11276889','ぴあフィルムフェスティバル','Pia Film Festival',NULL,'film festival in Japan','Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,1977,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%B4%E3%81%82%E3%83%95%E3%82%A3%E3%83%AB%E3%83%A0%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Pia_Film_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5371810','天神祭','Tenjin Matsuri','大阪天満宮を中心として大阪市で行われる祭り','Annual festival in Japan','Q385793','大阪天満宮','Ōsaka Tenmangū','大阪府','kinki',NULL,NULL,951,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/120725%20Osaka%20Tenjinmatsuri%20Japan08bs.jpg','https://ja.wikipedia.org/wiki/%E5%A4%A9%E7%A5%9E%E7%A5%AD','https://en.wikipedia.org/wiki/Tenjin_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5332426','大地の芸術祭 越後妻有アートトリエンナーレ','Echigo-Tsumari Art Triennial','新潟県十日町市、津南町で開催される国際芸術祭','international modern art festival held once every three years in the Niigata prefecture, Japan',NULL,NULL,NULL,'新潟県','chubu',37.016666666,138.6,2000,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%9C%B0%E3%81%AE%E8%8A%B8%E8%A1%93%E7%A5%AD_%E8%B6%8A%E5%BE%8C%E5%A6%BB%E6%9C%89%E3%82%A2%E3%83%BC%E3%83%88%E3%83%88%E3%83%AA%E3%82%A8%E3%83%B3%E3%83%8A%E3%83%BC%E3%83%AC','https://en.wikipedia.org/wiki/Echigo-Tsumari_Art_Triennial',75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3698846','御柱祭','Onbashira',NULL,'festival held every six years in the Lake Suwa area of Nagano, Japan','Q11631849','諏訪地域','Suwa area','長野県','chubu',36.075277777,138.091388888,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/ONBASHIRA%20festival%20%28tree%20drop%29%20Nagano%2CJAPAN.jpg','https://ja.wikipedia.org/wiki/%E5%BE%A1%E6%9F%B1%E7%A5%AD','https://en.wikipedia.org/wiki/Onbashira',90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3307937','壬生の花田植','Mibu no Hana Taue','広島県北広島町で行われる伝統行事','Rice transplanting ritual in Hiroshima, Japan',NULL,NULL,NULL,'広島県','chugoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Mibu-hanadaue01.JPG','https://ja.wikipedia.org/wiki/%E5%A3%AC%E7%94%9F%E3%81%AE%E8%8A%B1%E7%94%B0%E6%A4%8D','https://en.wikipedia.org/wiki/Mibu_no_Hana_Taue',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5174676','コスキン・エン・ハポン','Cosquín en Japón','福島県伊達郡川俣町で毎年開催されているフォルクローレの音楽祭','a South American folk festival held annually in Kawamata, Fukushima, Japan',NULL,NULL,NULL,'福島県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B3%E3%82%B9%E3%82%AD%E3%83%B3%E3%83%BB%E3%82%A8%E3%83%B3%E3%83%BB%E3%83%8F%E3%83%9D%E3%83%B3','https://en.wikipedia.org/wiki/Cosqu%C3%ADn_en_Jap%C3%B3n',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11301756','ゲームマーケット','Game Market','日本最大級の電源不要ゲーム(アナログゲーム)のイベント','Japanese gaming convention',NULL,NULL,NULL,'千葉県','kanto',35.6308,139.797,2000,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Gamemarket2014autumn08.jpg','https://ja.wikipedia.org/wiki/%E3%82%B2%E3%83%BC%E3%83%A0%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%83%E3%83%88','https://en.wikipedia.org/wiki/Game_Market',95,'drafted','## 概要

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
','## Overview

Game Market is Japan''s largest analog game exhibition and sales event, dedicated exclusively to "power-free games" such as board games, card games, and tabletop role-playing games. The Tokyo editions are held twice a year, in spring (around May) and autumn (around November), with Makuhari Messe serving as the venue in recent years, drawing over 20,000 visitors. An additional Osaka edition is held annually, serving as a hub for analog game fans in western Japan.

Domestic and international board game publishers, doujin circles, and individual creators announce and sell new titles, with adjacent play-test areas where purchased games can be tried on the spot. As an event symbolizing the growth of analog gaming culture in Japan, it attracts a broad audience ranging from industry professionals and dedicated enthusiasts to newcomers.

## History and Origins

The first Game Market was held on April 2, 2000, at a small venue in Tokyo. Founded by the Japanese analog game enthusiast community of the time, it coincided with the period when German-style board games (Eurogames) began to gain serious popularity in Japan. The niche concept of a "board game-exclusive sales event" perfectly rode the wave of the times.

Initially a small-scale event with around 60 booths and several hundred participants, Game Market grew steadily through the late 2000s global board game boom, with the number of exhibiting circles and attendees increasing each year. In the 2010s, the venue moved to Tokyo Big Sight and later expanded further to Makuhari Messe, growing in the 2020s into Japan''s largest analog game event with over 20,000 attendees.

The Osaka edition launched in 2013 as the festival''s first regional expansion, with 85 booths and a stronger-than-expected response. The current three-edition annual cycle (Tokyo Spring, Tokyo Autumn, Osaka) has become well-established, functioning as a nationwide hub for analog game culture.

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
','game-market','game-market',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3562464','信玄公祭り','Shingen-ko Festival','山梨県甲府市において行われているイベント','Annual traditional Japanese festival',NULL,NULL,NULL,'山梨県','chubu',NULL,NULL,1947,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Paradeimregen3.JPG','https://ja.wikipedia.org/wiki/%E4%BF%A1%E7%8E%84%E5%85%AC%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Shingen-ko_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q4663470','あばれ祭り','Abare Festival','石川県能登町で行われるキリコ祭り',NULL,NULL,NULL,NULL,'石川県','chubu',NULL,NULL,1700,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%82%E3%81%B0%E3%82%8C%E7%A5%AD','https://en.wikipedia.org/wiki/Abare_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q4926801',NULL,'Blip Festival',NULL,'music festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2006,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Dubmood%20blipfestival%202008%202.jpg',NULL,'https://en.wikipedia.org/wiki/Blip_Festival',45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q4806729','アジアンクィア映画祭','Asian Queer Film Festival',NULL,'Japanese LGBT film festival','Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,2007,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%B8%E3%82%A2%E3%83%B3%E3%82%AF%E3%82%A3%E3%82%A2%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Asian_Queer_Film_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q4829650','阿波の狸まつり','Awa no Tanuki Festival','徳島県徳島市で毎年11月上旬に催される祭り','Japanese festival',NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E9%98%BF%E6%B3%A2%E3%81%AE%E7%8B%B8%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Awa_no_Tanuki_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5327561','イースト・イースト','East-East',NULL,'Japanese-Lithuanian architecture festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%BC%E3%82%B9%E3%83%88%E3%83%BB%E3%82%A4%E3%83%BC%E3%82%B9%E3%83%88','https://en.wikipedia.org/wiki/East-East',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5347024','ええじゃないか','ee ja nai ka','日本の慶応3年8月から12月にかけて発生した騒動','carnivalesque celebrations, communal activities, and protests in Japan in 1867–68',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/EeJaNaiKaScene.jpg','https://ja.wikipedia.org/wiki/%E3%81%88%E3%81%88%E3%81%98%E3%82%83%E3%81%AA%E3%81%84%E3%81%8B','https://en.wikipedia.org/wiki/Ee_ja_nai_ka',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q4701224','竿燈','Akita Kantō','秋田県秋田市で行われる祭り','Japanese festival celebrated from 3–7 August in Akita, Japan','Q17139','秋田市','Akita','秋田県','tohoku',39.71847222,140.11319444,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Akita%20Kanto%20Festival%202017.jpg','https://ja.wikipedia.org/wiki/%E7%AB%BF%E7%87%88','https://en.wikipedia.org/wiki/Akita_Kant%C5%8D',95,'drafted','## 概要

竿燈まつり（かんとうまつり）は、秋田県秋田市で毎年8月3日から6日までの4日間にわたって行われる、五穀豊穣・無病息災・厄除けを祈念する伝統行事である。重さ50キログラム、長さ12メートルにも及ぶ「竿燈（かんとう）」と呼ばれる竹竿に46個もの提灯を吊るし、それを腰や額、肩、手のひらで支える妙技を披露する。青森ねぶた・仙台七夕と並んで「東北三大祭り」に数えられ、1980年（昭和55年）に国の重要無形民俗文化財に指定されている。

## 歴史

竿燈の起源は宝暦年間（1751-1764年）以前に遡るとされ、当時の秋田藩で行われていた「ねぶり流し」という眠気払いの行事と、五穀豊穣を祈願する七夕の風習が融合して成立したと伝わる。藩政期には町人文化として発展し、寛政元年（1789年）の津村淙庵『雪の降る道』に竿燈らしき行事の記述が残されている。明治・大正期には一時衰退したものの、昭和初期に地元有志により復興、戦後は秋田市の観光行事として大規模化し、現在では国内外から多数の観光客を迎える夏祭りに発展した。

## 見どころ

最大の見どころは毎晩18:50頃から始まる「夜本番」で、約280本もの竿燈が約2万個の提灯の灯りを揺らしながら大通りを埋め尽くす光景は圧巻。差し手（さして）と呼ばれる演者が「ドッコイショ、ドッコイショ」の掛け声と共に、流し・平手・額・肩・腰の5つの技を披露する。提灯の灯りが稲穂のように揺れる姿は、五穀豊穣を象徴する原初の祈りの形を伝える。日中には「妙技会」が開催され、技の優劣を競う競技形式の演技も楽しめる。

## 開催情報・アクセス

会場は秋田県秋田市の竿燈大通り（山王十字路から二丁目橋まで約800メートル）。JR秋田駅から徒歩約15分。観覧席は有料（前売り2,700-3,500円）、自由観覧は無料。4日間で約130万人の観光客が訪れる。

## 周辺観光

秋田市内には千秋公園（久保田城跡）、赤れんが郷土館、秋田県立美術館、ねぶり流し館（竿燈の常設展示）など歴史・文化観光資源が集中する。郊外には男鹿半島・なまはげ館、田沢湖、角館武家屋敷、乳頭温泉郷などの観光地が広がり、夏季は秋田名物・きりたんぽ、稲庭うどん、比内地鶏、地酒の蔵元巡りなど食文化も堪能できる。','## Overview

The Kantō Festival (Kantō Matsuri) is a traditional Japanese festival held annually from August 3 to 6 in Akita City, Akita Prefecture, dedicated to prayers for bountiful harvests, protection from illness, and the warding off of evil. Performers display extraordinary feats of balance using "kantō"—long bamboo poles up to 12 meters in length and 50 kilograms in weight, hung with as many as 46 paper lanterns—supporting them on their hips, foreheads, shoulders, and palms. Together with the Aomori Nebuta and Sendai Tanabata, it is counted among the "Three Great Festivals of the Tōhoku Region" and was designated as a National Important Intangible Folk Cultural Property in 1980 (Shōwa 55).

## History

The origins of the Kantō Festival are traced back to before the Hōreki era (1751-1764), when a drowsiness-dispelling ritual called "Neburi-nagashi" performed in the Akita Domain merged with the Tanabata custom of praying for bountiful harvests. During the domain administration period, the festival developed as a townspeople''s culture, with descriptions of what appears to be the kantō ritual recorded in Tsumura Sōan''s 1789 (Kansei 1) work "Yuki no Furu Michi" (The Snow-Falling Road). Although the festival declined temporarily during the Meiji and Taishō periods, it was revived in the early Shōwa era through the efforts of local volunteers. After World War II, it grew into a large-scale tourism event sponsored by Akita City, developing into the major summer festival it is today, welcoming visitors from around the world.

## Highlights

The greatest attraction is the "Yoru Honban" (Evening Performance) beginning around 18:50 each night, when approximately 280 kantō poles fill the main avenue, their roughly 20,000 lanterns swaying with light in an overwhelming spectacle. Performers called "sashite" demonstrate five techniques—Nagashi (flow), Hirate (palm), Hitai (forehead), Kata (shoulder), and Koshi (hip)—accompanied by chants of "Dokkoisho, Dokkoisho." The sight of the lantern lights swaying like ripe rice ears conveys the primitive form of prayer for bountiful harvests. During the day, "Myōgi-kai" (skill competitions) are held, allowing visitors to enjoy competitive performances where techniques are judged for excellence.

## Event Details and Access

The venue is Kantō Ōdōri Avenue in Akita City, Akita Prefecture, extending approximately 800 meters from Sannō Crossing to Nichōme Bridge. Access is approximately 15 minutes on foot from Akita Station on the JR lines. Reserved seating is available for purchase (advance tickets 2,700-3,500 yen), while general viewing along the street is free. The four-day festival attracts approximately 1.3 million visitors.

## Surrounding Attractions

Akita City offers a concentration of historical and cultural attractions including Senshū Park (the ruins of Kubota Castle), the Akarenga Museum of Local History, the Akita Museum of Art, and the Neburi-nagashi Hall (a permanent exhibition of kantō poles). The surrounding area features the Oga Peninsula and Namahage Museum, Lake Tazawa, the Kakunodate samurai district, and the Nyūtō Hot Spring village. Summer travelers can also enjoy Akita''s culinary specialties including kiritanpo, Inaniwa udon noodles, Hinai-jidori chicken, and tours of local sake breweries, making it a richly rewarding destination for both cultural and gastronomic exploration.','kanto-matsuri-akita','kanto-matsuri-akita',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3343765','サイトウ・キネン・フェスティバル松本','Seiji Ozawa Matsumoto Festival',NULL,'annual classical music festival held in the Japanese Alps near Matsumoto',NULL,NULL,NULL,'長野県','chubu',NULL,NULL,1992,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%BB%E3%82%A4%E3%82%B8%E3%83%BB%E3%82%AA%E3%82%B6%E3%83%AF_%E6%9D%BE%E6%9C%AC%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Seiji_Ozawa_Matsumoto_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11372403','五所川原立佞武多','Goshogawara Tachineputa Festival','青森県五所川原市で開催される祭り','summer festival in Goshogawara, Japan',NULL,NULL,NULL,'青森県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tachineputa%EF%BD%9E2007%20%22Mebukiurasaburu%22.JPG','https://ja.wikipedia.org/wiki/%E4%BA%94%E6%89%80%E5%B7%9D%E5%8E%9F%E7%AB%8B%E4%BD%9E%E6%AD%A6%E5%A4%9A','https://en.wikipedia.org/wiki/Goshogawara_Tachineputa_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1749262','博多祇園山笠','Hakata Gion Yamakasa Festival','博多の櫛田神社における神事','festival in Hakata, Fukuoka, Japan','Q11433106','大博通り','Taihaku Dōri','福岡県','kyushu',33.59297,130.41045,1241,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Hakata%20gion%20yamakasa%202005%2001.jpg','https://ja.wikipedia.org/wiki/%E5%8D%9A%E5%A4%9A%E7%A5%87%E5%9C%92%E5%B1%B1%E7%AC%A0','https://en.wikipedia.org/wiki/Hakata_Gion_Yamakasa',95,'drafted','## 概要

博多祇園山笠（はかたぎおんやまかさ）は、福岡県福岡市博多区の櫛田神社で毎年7月1日から15日にかけて行われる、約780年の歴史を持つ国指定重要無形民俗文化財の伝統祭礼である。総重量1トンを超える「舁き山笠（かきやまかさ）」を男衆が舁いて博多の街を疾走する勇壮な姿で全国的に知られ、ユネスコ無形文化遺産「山・鉾・屋台行事」を構成する日本三大祇園祭の一つに数えられる。

## 歴史

博多祇園山笠の起源は鎌倉時代の仁治2年（1241年）、博多に疫病が流行した際、承天寺の開祖・聖一国師が施餓鬼棚に乗って祈祷水を撒き疫病退散を祈願したことに始まると伝わる。室町期には博多商人が町の繁栄と疫病退散を祈願して山笠を担ぐ風習が定着し、戦国時代の博多焼失と豊臣秀吉による太閤町割（1587年）を経て、町ごとに「流（ながれ）」と呼ばれる組織が形成された。江戸期には豪華絢爛な「飾り山笠」が発達したが、明治31年（1898年）に電線架設で高さ制限が生じ、現在の「舁き山笠（疾走用・低い）」と「飾り山笠（観賞用・高い）」の二本立てに分化した。1979年に国の重要無形民俗文化財に指定、2016年にユネスコ無形文化遺産に登録された。

## 見どころ

最大の見せ場はクライマックスの「追い山笠」で、7月15日午前4時59分の太鼓を合図に櫛田神社を一斉スタートし、約5キロのコースを各流が全力疾走で駆け抜ける。総重量1トンの舁き山笠を約30人の舁き手が肩に担ぎ、地下足袋に長法被姿で「オイサ、オイサ」の掛け声と共に博多の街を疾走する姿は圧巻。期間中は市内14基の「飾り山笠」も街中に展示され、歴史絵巻や時事ネタを織り込んだ豪華な人形装飾を間近で観賞できる。

## 開催情報・アクセス

会場は櫛田神社（福岡市博多区上川端町1-41）を中心とする博多旧市街地一帯。JR博多駅から徒歩約15分、地下鉄祇園駅から徒歩約3分。観覧は無料。期間中（7/1-7/15）の最大の盛り上がりは15日早朝の追い山笠で、観客動員は約100万人。

## 周辺観光

博多区一帯は櫛田神社・東長寺・承天寺など歴史的寺社や、博多町家ふるさと館、博多伝統工芸館などが集中する。中洲屋台街、博多ラーメン、もつ鍋、明太子など博多グルメの聖地でもあり、福岡空港・博多駅の交通至便性と相まって、夏のインバウンド観光地として国際的人気が高い。','## Overview

Hakata Gion Yamakasa is a traditional festival with approximately 780 years of history, held annually from July 1 to 15 at Kushida Shrine in Hakata Ward, Fukuoka City, Fukuoka Prefecture, and designated as a National Important Intangible Folk Cultural Property. Renowned nationwide for the spectacular sight of men carrying "kakiyama" floats weighing over one ton while sprinting through the streets of Hakata, the festival is counted among Japan''s three great Gion festivals and is a constituent element of the UNESCO Intangible Cultural Heritage "Yama, Hoko, Yatai Float Festivals."

## History

The origins of Hakata Gion Yamakasa trace back to 1241 (Ninji 2) during the Kamakura period, when an epidemic broke out in Hakata and Shōichi Kokushi, the founder of Jōten-ji Temple, mounted a segaki memorial platform and scattered blessed water to pray for the epidemic''s end. During the Muromachi period, the custom of Hakata merchants shouldering yamakasa floats to pray for town prosperity and epidemic protection became firmly established. Following the destruction of Hakata during the Warring States period and Toyotomi Hideyoshi''s Taikō Town Division (1587), neighborhood organizations called "Nagare" were formed. During the Edo period, magnificent "Kazariyama" decorative floats developed, but the introduction of overhead electrical wires in 1898 (Meiji 31) created height restrictions, leading to the current dual format of low "Kakiyama" (running floats) and tall "Kazariyama" (display floats). The festival was designated a National Important Intangible Folk Cultural Property in 1979 and registered as a UNESCO Intangible Cultural Heritage in 2016.

## Highlights

The climactic highlight is the "Oiyama" finale, when at the signal of drums at 4:59 a.m. on July 15, all teams simultaneously depart from Kushida Shrine and race through an approximately 5-kilometer course at full sprint. Approximately 30 carriers shoulder a one-ton kakiyama float, dressed in jika-tabi traditional footwear and long happi coats, charging through the streets of Hakata with shouts of "Oisa, Oisa." During the festival period, 14 ornate "Kazariyama" floats are displayed throughout the city, allowing close viewing of magnificent doll decorations incorporating historical scrolls and contemporary themes.

## Event Details and Access

The festival is centered around Kushida Shrine (1-41 Kamikawabata-chō, Hakata Ward, Fukuoka City) and extends throughout the old Hakata district. Access is approximately 15 minutes on foot from Hakata Station or 3 minutes from Gion Station on the subway. Viewing is free of charge. The peak excitement during the festival period (July 1-15) occurs during the Oiyama finale on the early morning of July 15, drawing approximately one million spectators in total.

## Surrounding Attractions

The Hakata Ward area features a concentration of historic temples and shrines including Kushida Shrine, Tōchō-ji Temple, and Jōten-ji Temple, as well as the Hakata Machiya Folk Museum and the Hakata Traditional Craft Museum. The district is also a sacred ground of Hakata cuisine, famed for its Nakasu yatai food stalls, Hakata ramen, motsunabe hot pot, and mentaiko spicy cod roe. Combined with the convenient access of Fukuoka Airport and Hakata Station, the area has gained tremendous international popularity as a summer inbound tourism destination.','hakata-gion-yamakasa','hakata-gion-yamakasa',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q2276034','沖縄国際映画祭','Okinawa International Movie Festival','日本の沖縄県で開催される映画祭','annual film festival in Japan','Q600614','沖縄本島','Okinawa','沖縄県','okinawa',NULL,NULL,2009,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/3rd%20Okinawa%20International%20Movie%20Festival%20001.jpg','https://ja.wikipedia.org/wiki/%E6%B2%96%E7%B8%84%E5%9B%BD%E9%9A%9B%E6%98%A0%E7%94%BB%E7%A5%AD','https://en.wikipedia.org/wiki/Okinawa_International_Movie_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q2616539','裸祭り','Hadaka Matsuri','男性参加者が褌姿など裸体に近い姿、または全裸で参加する祭り','type of Japanese festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Hadaka%20Matsuri%20small.JPG','https://ja.wikipedia.org/wiki/%E8%A3%B8%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Hadaka_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1636567','神戸ルミナリエ','Kobe Luminarie','神戸市で行われる祭典','light festival in Kobe (Japan)','Q59520','元町駅','Motomachi Station','兵庫県','kinki',34.68808333,135.18994444,1995,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/%E7%AC%AC30%E5%9B%9E%E7%A5%9E%E6%88%B8%E3%83%AB%E3%83%9F%E3%83%8A%E3%83%AA%E3%82%A8%281%29.jpg','https://ja.wikipedia.org/wiki/%E7%A5%9E%E6%88%B8%E3%83%AB%E3%83%9F%E3%83%8A%E3%83%AA%E3%82%A8','https://en.wikipedia.org/wiki/Kobe_Luminarie',95,'drafted','## 概要

神戸ルミナリエ（こうべるみなりえ）は、兵庫県神戸市中央区の旧外国人居留地および東遊園地で毎年12月（近年は1月に変更）に開催される、阪神・淡路大震災の犠牲者への鎮魂と都市復興を祈念する大規模光の祭典である。1995年12月の初開催以来、神戸の冬の風物詩として定着し、世界的にも著名な光の芸術祭の一つに数えられる。

## 歴史

神戸ルミナリエは1995年1月17日の阪神・淡路大震災で犠牲となった6,434人の方々への鎮魂と被災者への希望の光を灯す目的で、同年12月にイタリアの光の芸術家ヴァルテル・パーレ・コモッリの企画により始まった。「ルミナリエ」とはイタリア語で「光の彫刻」を意味する伝統的な祭典に由来し、神戸市と神戸ルミナリエ組織委員会が主催する。第1回開催では約254万人が来場し、以降毎年12月初旬から中旬にかけて開催されてきた。2020-2022年はコロナ禍で中止・縮小開催となり、2024年からは開催時期を1月17日（震災記念日）に合わせて移動した。

## 見どころ

中心となる「フロントーネ」（正面装飾）と「ガレリア」（光の回廊）は、毎年異なるデザインで制作される手作業のイタリア式光のアーチで、約20万個のLED電球が点灯する。色彩豊かな光のトンネルを歩く体験は厳かで幻想的であり、震災の記憶と復興への祈りが込められた荘厳な雰囲気が漂う。東遊園地のメイン会場には「光の壁掛け（スパッリエーラ）」が設置され、フィナーレでは一斉点灯のセレモニーが行われる。

## 開催情報・アクセス

会場は兵庫県神戸市中央区の旧外国人居留地（仲町通り）および東遊園地。JR神戸線元町駅から徒歩約10分、阪神電鉄元町駅から徒歩約8分。観覧は無料だが、震災復興支援のための募金協力が呼びかけられる。近年は混雑緩和のため整理券・予約制を導入。

## 周辺観光

神戸市中心部には北野異人館街、南京町（神戸中華街）、メリケンパーク、ハーバーランド、神戸ポートタワーなどの観光名所が集中する。冬季は神戸牛・神戸ベーカリー文化、有馬温泉、六甲山夜景なども楽しめ、ルミナリエと組み合わせた1泊2日の都市観光が人気。','## Overview

Kobe Luminarie is a large-scale illumination festival held annually in December (recently shifted to January) at the former Foreign Settlement district and Higashi Yūenchi Park in Chūō Ward, Kobe City, Hyōgo Prefecture. Dedicated to the repose of victims of the Great Hanshin-Awaji Earthquake and to the prayer for urban recovery, the festival has become a defining winter tradition of Kobe since its first edition in December 1995 and is counted among the world''s most renowned light art festivals.

## History

Kobe Luminarie was established to honor the 6,434 victims of the Great Hanshin-Awaji Earthquake of January 17, 1995, and to light a beacon of hope for survivors. The festival began in December of that same year under the artistic direction of Italian light artist Valerio Festi. The name "Luminarie" derives from a traditional Italian festival meaning "light sculptures," and the event is organized by Kobe City and the Kobe Luminarie Organizing Committee. The inaugural edition drew approximately 2.54 million visitors, and the festival has continued annually from early to mid-December ever since. From 2020 to 2022, the festival was cancelled or scaled down due to the COVID-19 pandemic, and from 2024 onward, the timing was shifted to align with January 17, the anniversary of the earthquake.

## Highlights

The centerpiece "Frontone" (front facade decoration) and "Galleria" (light corridor) are handmade Italian-style light arches designed differently each year, illuminated by approximately 200,000 LED bulbs. Walking through the colorful light tunnels offers a solemn and otherworldly experience, imbued with the memory of the earthquake and the prayer for recovery. The main venue at Higashi Yūenchi Park features a "Spalliera" (light wall decoration), and the finale includes a simultaneous lighting ceremony that captures the heart of the festival.

## Event Details and Access

The venues are the former Foreign Settlement district (Nakamachi-dōri) and Higashi Yūenchi Park in Chūō Ward, Kobe City, Hyōgo Prefecture. Access is approximately 10 minutes on foot from Motomachi Station on the JR Kōbe Line, or 8 minutes from Motomachi Station on the Hanshin Electric Railway. Admission is free, though donations are requested to support earthquake recovery efforts. In recent years, reservation and numbered-ticket systems have been introduced to manage crowds.

## Surrounding Attractions

Central Kobe offers a wealth of tourist attractions including the Kitano Ijinkan foreign residences district, Nankin-machi (Kobe Chinatown), Meriken Park, Harbor Land, and the Kobe Port Tower. The winter season also offers opportunities to enjoy Kobe beef cuisine, the city''s bakery culture, Arima hot spring resort, and the night views from Mount Rokko, making a one- or two-night urban tourism stay combined with the Luminarie experience particularly popular among visitors.','kobe-luminarie','kobe-luminarie',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q2915444','ファンタズミック!','Fantasmic!',NULL,'night-time pyrotechnic and light performance at multiple Disney Parks','Q1345090','ディズニー・ハリウッド・スタジオ','Disney''s Hollywood Studios',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Fantasmic%21%20Evil%20Queen%20spell.jpg','https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%83%B3%E3%82%BF%E3%82%BA%E3%83%9F%E3%83%83%E3%82%AF!','https://en.wikipedia.org/wiki/Fantasmic!',80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3092868','二本松の提灯祭り','Nihonmatsu Lantern Festival',NULL,'festival held in Nihonmatsu, Fukushima, Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E4%BA%8C%E6%9C%AC%E6%9D%BE%E3%81%AE%E6%8F%90%E7%81%AF%E7%A5%AD%E3%82%8A.jpg','https://ja.wikipedia.org/wiki/%E4%BA%8C%E6%9C%AC%E6%9D%BE%E6%8F%90%E7%81%AF%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Nihonmatsu_Lantern_Festival',80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3119229','隅田川花火大会','Sumidagawa Fireworks Festival','東京都の花火大会','Fireworks show in Japan','Q222149','隅田川','Sumida River','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Hanabi%20in%20Adachi-ku1.jpg','https://ja.wikipedia.org/wiki/%E9%9A%85%E7%94%B0%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A','https://en.wikipedia.org/wiki/Sumidagawa_Fireworks_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q2071242','おわら風の盆','Kaze no bon','富山県富山市八尾地区で、毎年9月1日から3日にかけて行われている盆踊り','annual Japanese festival','Q204266','富山市','Toyama','富山県','chubu',NULL,NULL,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Kazenobon01.jpg','https://ja.wikipedia.org/wiki/%E3%81%8A%E3%82%8F%E3%82%89%E9%A2%A8%E3%81%AE%E7%9B%86','https://en.wikipedia.org/wiki/Kaze_no_bon',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q2069076','ガタケット','Niigata Comic Market','新潟県新潟市で開催される同人誌即売会','comic convention in Niigata, Japan',NULL,NULL,NULL,'新潟県','chubu',NULL,NULL,1983,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%AC%E3%82%BF%E3%82%B1%E3%83%83%E3%83%88','https://en.wikipedia.org/wiki/Niigata_Comic_Market',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1151186','フジロックフェスティバル','Fuji Rock Festival','毎年夏季に日本で行われるロックフェスティバル','music festival','Q3268287','苗場スキー場','Naeba Ski Resort','新潟県','chubu',36.799,138.78359167,1997,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/FujiGreenStage.jpg','https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%B8%E3%83%AD%E3%83%83%E3%82%AF%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Fuji_Rock_Festival',95,'drafted','## 概要

フジロックフェスティバル（Fuji Rock Festival）は、新潟県南魚沼郡湯沢町の苗場スキー場で毎年7月最終週末の金・土・日3日間にわたって開催される、日本最大級の野外ロック・フェスティバルである。1997年に第1回が開催されて以来、約30年の歴史を持ち、3日間の来場者数は約12万人、海外からの来場者も多数を占める日本を代表する音楽イベントである。「世界一クリーンなフェス」としても国際的に知られている。

## 歴史

1997年（平成9年）、第1回が静岡県の富士天神山スキー場で開催されたが、台風直撃により2日目以降が中止となり「伝説のフェス」として語り継がれることになった。1999年から現在の新潟県苗場スキー場へ会場を移し、以降一度も中止することなく継続開催されている（2020年はコロナ禍でオンライン、2021年は規模縮小開催）。主催は株式会社スマッシュ。「自然との共生」「環境配慮」をコンセプトとし、ゴミの分別徹底・マイ食器推奨・森林保護プロジェクトなどサステナビリティへの取り組みが高く評価され、海外メディアからも「世界で最もクリーンなロックフェス」と評されている。

## 見どころ

会場は苗場スキー場の広大な森と渓流に囲まれた約9つのステージで構成され、メインの「グリーンステージ」「ホワイトステージ」では世界的ロックバンド・アーティストが連日ヘッドラインを飾る。出演アーティストは年により異なるが、過去にはレッド・ホット・チリ・ペッパーズ、レディオヘッド、コールドプレイ、オアシス、ボブ・ディラン、フー・ファイターズなど超大物が出演している。日本人アーティストも多数出演し、ロック・電子音楽・ヒップホップ・ジャズなどジャンルは多岐にわたる。会場内には飲食店約200店、温泉、キャンプサイトもあり、3日間滞在型のフェスとして定着している。

## 開催情報

開催地は新潟県南魚沼郡湯沢町三国苗場の苗場スキー場。最寄駅はJR上越新幹線「越後湯沢駅」からシャトルバスで約50分。開催期間は毎年7月最終週末の金・土・日3日間。チケットは1日券￥22,000前後、3日通し券￥58,000前後（年により変動）。前夜祭（木曜）も別途有料で開催。山岳地のため天候が急変しやすく、レインウェア・防寒着・歩きやすい靴は必須装備。場内はキャッシュレス決済対応。

## 周辺の見どころ

苗場・湯沢エリアは新潟県最大の温泉・スキーリゾート地で、フェス前後の宿泊先・観光地として人気が高い。越後湯沢駅周辺には「ぽんしゅ館」（新潟の地酒利き酒コーナー）、雪国まいたけ館などの観光施設が集積。少し足を伸ばせば、川端康成の小説『雪国』の舞台となった越後湯沢温泉、苗場ドラゴンドラ（日本最長5,481m）からの山岳パノラマも楽しめる。','## Overview

Fuji Rock Festival (フジロックフェスティバル) is Japan''s largest outdoor rock festival, held annually over the three days of the final weekend of July (Friday to Sunday) at the Naeba Ski Resort in Yuzawa Town, Minamiuonuma District, Niigata Prefecture. Since its inaugural edition in 1997, the festival has accumulated nearly three decades of history, drawing approximately 120,000 attendees over its three days, including a substantial number of international visitors. It is also recognized internationally as "the world''s cleanest music festival."

## History

The first Fuji Rock was held in 1997 (Heisei 9) at the Fujiten Snow Resort in Shizuoka Prefecture, but a direct hit by a typhoon forced the cancellation of the second and third days, immediately turning it into a legendary event in Japanese music history. Since 1999, the festival has been held at its current home, the Naeba Ski Resort in Niigata Prefecture, continuing without interruption (with the 2020 edition held online due to the pandemic, and a reduced-scale edition in 2021). The festival is organized by Smash Corporation. Built on the principles of "coexistence with nature" and "environmental responsibility," its commitment to thorough waste sorting, reusable tableware, and forest-protection projects has earned high praise from international media, which have described it as "the cleanest rock festival in the world."

## Highlights

The venue is set against the vast forest and mountain streams of the Naeba Ski Resort, encompassing approximately nine stages. The Green Stage and White Stage — the two main stages — host world-class rock bands and artists as nightly headliners. Past lineups have included the Red Hot Chili Peppers, Radiohead, Coldplay, Oasis, Bob Dylan, and the Foo Fighters. Japanese artists also feature prominently, with a lineup spanning rock, electronic, hip-hop, jazz, and many other genres. The festival grounds host approximately 200 food and drink stalls, on-site hot-spring baths, and campgrounds — establishing it as a true multi-day stay-and-experience festival.

## Event Information

The venue is the Naeba Ski Resort in Mikuni-Naeba, Yuzawa Town, Minamiuonuma District, Niigata Prefecture. The nearest station is Echigo-Yuzawa Station on the JR Jōetsu Shinkansen, followed by a shuttle bus ride of about 50 minutes. The festival runs annually over the three days of the final weekend of July. Tickets are approximately ¥22,000 for a single-day pass and ¥58,000 for a three-day pass (prices vary by year). A separately ticketed pre-festival event is held on Thursday evening. Mountain weather changes rapidly, making rain gear, warm layers, and sturdy walking shoes absolutely essential. The festival grounds operate on cashless payment.

## Nearby Attractions

The Naeba-Yuzawa area is one of Niigata Prefecture''s premier hot-spring and ski resort regions, making it an ideal destination before or after the festival. Around Echigo-Yuzawa Station, visitors will find Ponshu-kan (a tasting bar featuring all of Niigata''s sake breweries) and the Yukiguni Maitake Hall. A short trip further afield reveals Echigo-Yuzawa Onsen — the setting of Kawabata Yasunari''s Nobel Prize-winning novel "Snow Country" — and the Naeba Dragondola, Japan''s longest gondola at 5,481 meters, offering sweeping mountain panoramas.','fuji-rock-festival','fuji-rock-festival',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q2914758','五山送り火','Gozan no Okuribi','日本の京都府京都市で毎年8月16日の夜に行われるかがり火','Japanese festival',NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Gozanokuribi%20Daimonji2.jpg','https://ja.wikipedia.org/wiki/%E4%BA%94%E5%B1%B1%E9%80%81%E3%82%8A%E7%81%AB','https://en.wikipedia.org/wiki/Gozan_no_Okuribi',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1139891','東京フィルメックス','Tokyo Filmex','東京で毎年開催される国際映画祭','international film festival held annually in Tokyo, Japan','Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,2000,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E3%83%95%E3%82%A3%E3%83%AB%E3%83%A1%E3%83%83%E3%82%AF%E3%82%B9','https://en.wikipedia.org/wiki/Tokyo_Filmex',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q2238334','あえのこと','Oku-noto no Aenokoto','石川県奥能登地方で行われる農耕儀礼','agricultural ritual held in Oku-Noto area, Ishikawa, Japan','Q11446096','奥能登','Okunoto','石川県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Oku-noto%20no%20Aenokoto%2C%20offering%20meals%20to%20the%20deities.jpg','https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%A8%E3%83%8E%E3%82%B3%E3%83%88','https://en.wikipedia.org/wiki/Oku-noto_no_Aenokoto',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1072387','七五三','Shichi-Go-San','日本の年中行事','rite of passage and festival day in Japan for 3-, 5- or 7-year-old children in mid-November',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Shichigosan%20at%20Ikuta%20Jinja%20Shrine.JPG','https://ja.wikipedia.org/wiki/%E4%B8%83%E4%BA%94%E4%B8%89','https://en.wikipedia.org/wiki/Shichi-Go-San',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3090688','深川祭','Fukagawa Matsuri','東京都江東区の富岡八幡宮の祭礼','festival in Tokyo','Q654417','富岡八幡宮','Tomioka Hachiman Shrine','東京都','kanto',NULL,NULL,1642,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tomioka%20hachimangu4.jpg','https://ja.wikipedia.org/wiki/%E6%B7%B1%E5%B7%9D%E7%A5%AD','https://en.wikipedia.org/wiki/Fukagawa_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q1193996','日本の七夕','Tanabata','日本における七夕','Japanese festival (Japanese version of Double Seventh Festival)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E4%B8%83%E5%A4%95%20%2819545533256%29.jpg','https://ja.wikipedia.org/wiki/%E4%B8%83%E5%A4%95_(%E6%97%A5%E6%9C%AC)','https://en.wikipedia.org/wiki/Tanabata',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6518561','東京湾大華火祭','Tokyo Bay Grand Fireworks Festival',NULL,NULL,'Q11090204','晴海','Harumi','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tokyo%20bay%20fireworks%202015.jpg','https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E6%B9%BE%E5%A4%A7%E8%8F%AF%E7%81%AB%E7%A5%AD',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11235573','NHK音楽祭','NHK Music Festival','日本放送協会（NHK）とNHKプロモーションが企画制作する音楽祭','music festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/NHK%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q510847','初午','Hatsuuma','2月の最初の午の日',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Hatsuuma-festival%2CHrooka-inari%2CTajyuku%2CKatori-city%2CJapan.JPG','https://ja.wikipedia.org/wiki/%E5%88%9D%E5%8D%88',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11246063','Shintoku空想の森映画祭','Shintoku Fantasy Forest Film Festival','北海道上川郡新得町で主に9月に行われている映画祭',NULL,NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/Shintoku%E7%A9%BA%E6%83%B3%E3%81%AE%E6%A3%AE%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5860973','福岡国際映画祭','Fukuoka International Film Festival',NULL,'film festival','Q26600','福岡市','Fukuoka','福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q10855476','京都三大祭り','Three Great Festivals of Kyoto','京都府京都市内で行われる3つの祭り',NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E4%B8%89%E5%A4%A7%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6663968','足立の花火','Adachi Fireworks','毎年7月に日本の東京都足立区で開催される花火大会',NULL,NULL,NULL,NULL,'東京都','kanto',35.75869444,139.79783333,1924,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E8%B6%B3%E7%AB%8B%E3%81%AE%E8%8A%B1%E7%81%AB2016%E5%B9%B4.jpg','https://ja.wikipedia.org/wiki/%E8%B6%B3%E7%AB%8B%E3%81%AE%E8%8A%B1%E7%81%AB',NULL,95,'drafted','## 概要

足立の花火（あだちのはなび）は、東京都足立区の荒川河川敷で毎年7月下旬に開催される、東京都内で最も早い時期に行われる大規模花火大会のひとつである。約1万3,500発の花火が打ち上げられ、約60万人の観客を集める下町の夏の風物詩として親しまれている。

## 歴史

足立の花火は1924年（大正13年）、足立区西新井大師の千部会奉納花火として始まったとされ、約100年の歴史を持つ。第二次世界大戦中の中断と戦後復興を経て、1979年（昭和54年）に「足立の花火」として現在の形に再編され、足立区観光交流協会と足立区が主催する都内有数の花火大会として発展した。荒川河川敷という広大な打上げ会場を活かし、東京都心では他に類を見ないスケールと観覧の自由度で人気を集める。7月下旬という早い開催時期から、東京の夏祭りシーズンの幕開けを告げる花火大会としても知られる。

## 見どころ

約1時間で1万3,500発を打ち上げる凝縮されたプログラム構成が特徴で、スターマイン、特大スターマイン、メッセージ花火、フィナーレの大スターマインなど多彩な演出が次々と展開される。荒川河川敷の広い空に大輪の花火が低く大きく開く光景は迫力満点で、河川敷の芝生から無料で観覧できる解放感も魅力。夜空に花火が映える中、千住の町並みのシルエットが浮かび上がる景観は下町情緒たっぷり。

## 開催情報・アクセス

会場は東京都足立区千住・西新井・梅島周辺の荒川河川敷（千住側および小台側の両岸）。東武スカイツリーライン梅島駅・五反野駅、京成本線関屋駅、JR常磐線・東京メトロ千代田線北千住駅などから徒歩15-25分。観覧は無料（一部有料席あり）。例年7月下旬の特定の土曜日に開催。

## 周辺観光

足立区一帯は北千住の昭和レトロな商店街、西新井大師（厄除けで全国的に有名）、舎人公園、東京武道館などの観光資源が点在する。北千住駅周辺は近年若者にも人気の街となり、新旧の文化が交差する魅力的なエリア。荒川を挟んで葛飾区側には柴又帝釈天・寅さん記念館、墨田区側には東京スカイツリー・浅草寺など、東京下町観光の名所が近接する。','## Overview

Adachi no Hanabi (Adachi Fireworks Festival) is a large-scale fireworks display held annually in late July along the Arakawa Riverbed in Adachi Ward, Tokyo, ranking among the earliest major fireworks events of the Tokyo summer season. With approximately 13,500 fireworks launched and 600,000 spectators attending, it has become a cherished summer tradition of Tokyo''s old downtown district.

## History

Adachi no Hanabi traces its origins to 1924 (Taishō 13) as a dedicatory fireworks display for the Senbu-e ceremony at Nishiarai Daishi Temple in Adachi Ward, giving it approximately 100 years of history. After interruption during World War II and postwar recovery, the festival was reorganized into its current form as "Adachi no Hanabi" in 1979 (Shōwa 54), developing as one of Tokyo''s leading fireworks displays under the joint hosting of the Adachi City Tourism Exchange Association and the ward government. Taking advantage of the expansive launching venue along the Arakawa Riverbed, the festival attracts large crowds with a scale and freedom of viewing unmatched elsewhere in central Tokyo. Its early late-July timing has also earned it recognition as the fireworks display heralding the opening of Tokyo''s summer festival season.

## Highlights

The festival''s distinctive feature is its condensed program structure, launching 13,500 fireworks in approximately one hour through diverse productions including star mines, oversized star mines, message fireworks, and the grand finale star mine in rapid succession. The sight of large fireworks blooming low and broad across the wide skies above the Arakawa Riverbed delivers tremendous visual impact, and the open atmosphere of free viewing from the riverbed grass adds to its appeal. As the fireworks paint the night sky, the silhouette of the Senju townscape emerges below, creating a scene rich with downtown Tokyo''s nostalgic atmosphere.

## Event Details and Access

The venue is the Arakawa Riverbed in the Senju, Nishiarai, and Umejima areas of Adachi Ward, Tokyo (both the Senju side and the Odai side). Access is 15-25 minutes on foot from Umejima Station and Gotanno Station on the Tobu Skytree Line, Sekiya Station on the Keisei Main Line, or Kita-Senju Station on the JR Jōban Line and Tokyo Metro Chiyoda Line. Viewing is free (with some reserved paid seating available). The festival is typically held on a specific Saturday in late July.

## Surrounding Attractions

The Adachi Ward area features tourist attractions including the Showa-retro shopping streets of Kita-Senju, Nishiarai Daishi Temple (nationally famous for its protection against evil), Toneri Park, and the Tokyo Budōkan martial arts hall. The Kita-Senju Station area has become a popular district among young people in recent years, offering a charming blend of old and new cultural elements. Across the Arakawa River, Katsushika Ward features Shibamata Taishakuten Temple and the Tora-san Museum, while Sumida Ward offers Tokyo Skytree and Sensōji Temple, making the area highly accessible to Tokyo''s renowned downtown sightseeing destinations.','adachi-no-hanabi','adachi-no-hanabi',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11248128','TAMA CINEMA FORUM','Tama Cinema Forum','多摩市で開催される日本の映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/TAMA_CINEMA_FORUM',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6518542','神宮外苑花火大会','Jingu Fireworks Festival','東京都の花火大会',NULL,'Q11512386','明治神宮外苑軟式グラウンド','Meiji Shrine Gaien Softball Ground','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Jingu%20Fireworks%2008-1.jpg','https://ja.wikipedia.org/wiki/%E7%A5%9E%E5%AE%AE%E5%A4%96%E8%8B%91%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11225372','JAPAN国際コンテンツフェスティバル','Japan International Contents Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/JAPAN%E5%9B%BD%E9%9A%9B%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11252016','UNHCR難民映画祭','UNHCR Refugee Film Festival','移民、難民に関する映像作品を扱う映画祭',NULL,'Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,2008,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/UNHCR%E9%9B%A3%E6%B0%91%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q10860740','八王子まつり','Hachioji Matsuri','東京都八王子市にて毎年8月に開催される祭',NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,1961,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Hachioji-matsuri%202019a11.jpg','https://ja.wikipedia.org/wiki/%E5%85%AB%E7%8E%8B%E5%AD%90%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11249957','TOYAMA地域映画フェスティバル','TOYAMA Regional Film Festival','富山で開催されている映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/TOYAMA%E5%9C%B0%E5%9F%9F%E6%98%A0%E7%94%BB%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3461576','西大寺会陽','Saidai-ji Eyō','岡山市の西大寺で行われる裸祭り',NULL,'Q11627549','西大寺','Saidai-ji Temple',NULL,NULL,NULL,NULL,1510,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hadaka%20Matsuri%20%28-Naked%20Festival-%29%20in%20Saidaiji%2C%20Japan.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q720663','浅草サンバカーニバル','Samba Carnival of Asakusa','東京都台東区浅草で行われるサンバのパレード',NULL,'Q720644','浅草','Asakusa','東京都','kanto',NULL,NULL,1981,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Asakusa-Samba-Carnival-parade.jpg','https://ja.wikipedia.org/wiki/%E6%B5%85%E8%8D%89%E3%82%B5%E3%83%B3%E3%83%90%E3%82%AB%E3%83%BC%E3%83%8B%E3%83%90%E3%83%AB',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11250180','TSSショートムービーフェスティバル','TSS Short Movie Festival','短編映画を対象とした日本の映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/TSS%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%83%A0%E3%83%BC%E3%83%93%E3%83%BC%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11222654','HIROSHIMA MUSIC FESTIVAL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/HIROSHIMA_MUSIC_FESTIVAL',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11249129','THE VOC@LOiD M@STER','THE VOC@LOiD M@STER',NULL,'Vocaloid convention','Q17','日本','Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/THE_VOC@LOiD_M@STER',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11231913','MONSTER baSH',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/MONSTER_baSH',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11234423','NARITA花火大会in印旛沼',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/NARITA%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9Ain%E5%8D%B0%E6%97%9B%E6%B2%BC',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11248231','TBC夏まつり','TBC Summer Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/TBC%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11255135','YOSAKOIさせぼ祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/YOSAKOI%E3%81%95%E3%81%9B%E3%81%BC%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11241119','ROCKS TOKYO',NULL,'日本のロック・フェスティバル (2010-2012)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/ROCKS_TOKYO',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q199831','舞鶴つつじまつり',NULL,'京都府舞鶴市で行われているお祭りのひとつ',NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%88%9E%E9%B6%B4%E3%81%A4%E3%81%A4%E3%81%98%E3%81%BE%E3%81%A4%E3%82%8A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q9385159','仙台七夕','Sendai Tanabata','東北三大祭りの一つである宮城県仙台市で開かれる祭り',NULL,'Q46747','仙台市','Sendai','宮城県','tohoku',38.26049722,140.87196944,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Sendai%20Tanabata%202023.jpg','https://ja.wikipedia.org/wiki/%E4%BB%99%E5%8F%B0%E4%B8%83%E5%A4%95',NULL,95,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11192451','Black indie!','Black indie!','日本で開催されている自主映画の映画祭',NULL,'Q17','日本','Japan',NULL,NULL,NULL,NULL,2008,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/Black_indie!',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11251770','UBE現代日本彫刻展','Ube Sculpture Triennale','山口県宇部市で開催される野外彫刻の国際コンクール・展覧会','International Sculpture　Competition in Ube,Yamaguchi','Q11607744','緑と花と彫刻の博物館','Ube Tokiwa Museum','山口県','chugoku',NULL,NULL,1961,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/UBE%E7%8F%BE%E4%BB%A3%E6%97%A5%E6%9C%AC%E5%BD%AB%E5%88%BB%E5%B1%95',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11199280','FM.W','FM.W',NULL,'Rock Festival in Japan','Q37951','札幌市','Sapporo','北海道','hokkaido',NULL,NULL,2005,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/FM.W',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3350050','起きよ祭り','Okiyo Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%B5%B7%E3%81%8D%E3%82%88%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11242935','SETSTOCK','Setstock',NULL,'Japanese music festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/SETSTOCK',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11251519','仙台・青葉まつり','Sendai Aoba Matsuri',NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BB%99%E5%8F%B0%E3%83%BB%E9%9D%92%E8%91%89%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6663970','高岡御車山祭','Takaoka Mikurumayama Festival','富山県高岡市の関野神社の春季例祭',NULL,'Q11669562','高岡関野神社','Takaoka Sekino Shrine','富山県','chubu',36.747556,137.012056,1588,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/%E9%AB%98%E5%B2%A1%E5%B8%82%E8%A1%97%E3%81%AE%E9%A2%A8%E6%99%AF%20-%20panoramio.jpg','https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B2%A1%E5%BE%A1%E8%BB%8A%E5%B1%B1%E7%A5%AD',NULL,95,'drafted','## 概要

高岡御車山祭（たかおかみくるまやままつり）は、富山県高岡市の高岡関野神社の春季例祭として毎年5月1日に開催される、約430年の歴史を持つ伝統祭礼である。7基の豪華絢爛な「御車山（みくるまやま）」が高岡市旧市街地を巡行する勇壮華麗な姿で知られ、1979年（昭和54年）に国の重要有形民俗文化財、1981年（昭和56年）に国の重要無形民俗文化財に指定、2016年にはユネスコ無形文化遺産「山・鉾・屋台行事」の構成要素として登録された日本屈指の山車祭である。

## 歴史

御車山祭の起源は天正16年（1588年）、豊臣秀吉が後陽成天皇を聚楽第に迎えた際に使用された御所車を、慶長14年（1609年）に加賀藩2代藩主・前田利長が高岡城築城の祝いとして高岡の町に下賜したことに始まる。利長は7つの町に分配し、各町が独自の意匠を凝らした御車山として発展させ、現在の7基の体制が確立した。江戸時代を通じて加賀藩の篤い庇護を受け、漆塗り・金工・木彫・染織など加賀文化の粋を集めた豪華な装飾が施された。明治期以降も町衆の手で維持・継承され、戦後は高岡市の代表的な観光行事として国内外に知られるようになった。

## 見どころ

最大の見どころは5月1日の御車山巡行で、7基の御車山が高岡関野神社を出発し、片原町・坂下町・小馬出町・通町・木舟町・御馬出町・二番町の各町を一日かけて巡行する。御車山は高さ約7.5メートル、重さ1-2トンの大型山車で、車輪は金具で飾られ、御所車形式の優雅な姿に「鉾留め（ほこどめ）」と呼ばれる立物が天高くそびえる。前夜の宵山では提灯に灯りが入り、漆と金箔の装飾が幻想的に浮かび上がる。御車山会館では7基の本物の御車山が常設展示されており、年間を通して間近で観賞できる。

## 開催情報・アクセス

会場は高岡関野神社（富山県高岡市末広町9-56）を中心とする高岡市旧市街地一帯。あいの風とやま鉄道高岡駅から徒歩約10分。観覧は無料。御車山会館（高岡市守山町42）は通年営業で大人450円。

## 周辺観光

高岡市は加賀藩2代藩主・前田利長によって築かれた城下町として、銅器・漆器（高岡漆器）・絹織物などの伝統工芸が今も息づく工芸の町である。瑞龍寺（国宝）、高岡大仏（日本三大仏）、高岡古城公園、金屋町（鋳物発祥の地・重伝建）など歴史観光地が集中する。富山県内では立山黒部アルペンルート、五箇山合掌造り集落（世界遺産）、富山湾・氷見の海の幸など、自然・文化観光と組み合わせた周遊が可能。','## Overview

The Takaoka Mikurumayama Festival is a traditional festival with approximately 430 years of history, held annually on May 1 as the spring grand festival of Takaoka Sekino Shrine in Takaoka City, Toyama Prefecture. Renowned for the spectacular procession of seven magnificent "Mikurumayama" (Imperial Carriage Floats) through the old city center, the festival was designated as a National Important Tangible Folk Cultural Property in 1979 (Shōwa 54), as a National Important Intangible Folk Cultural Property in 1981 (Shōwa 56), and registered as a constituent element of the UNESCO Intangible Cultural Heritage "Yama, Hoko, Yatai Float Festivals" in 2016, making it one of Japan''s most prestigious float festivals.

## History

The origins of the Mikurumayama Festival trace back to 1588 (Tenshō 16), when Toyotomi Hideyoshi used imperial carriages to welcome Emperor Go-Yōzei to his Jurakudai residence in Kyoto. These carriages were later bestowed upon the town of Takaoka in 1609 (Keichō 14) by Maeda Toshinaga, the second lord of the Kaga Domain, to celebrate the completion of Takaoka Castle. Toshinaga distributed them among seven districts of the town, and each district developed them into uniquely designed Mikurumayama floats, establishing the current seven-float system. Throughout the Edo period, the festival received generous patronage from the Kaga Domain, and the floats were adorned with the finest examples of Kaga cultural artistry including lacquer work, metalwork, woodcarving, and textile dyeing. The festival continued to be maintained and transmitted by the townspeople through the Meiji era and beyond, and after World War II became known both domestically and internationally as a signature tourism event of Takaoka City.

## Highlights

The festival''s greatest highlight is the Mikurumayama procession on May 1, when all seven floats depart from Takaoka Sekino Shrine and parade through the districts of Katahara-machi, Sakashita-machi, Komandashi-machi, Tōri-machi, Kibune-machi, Ouma-dashi-machi, and Nibanmachi over the course of a full day. The Mikurumayama are large floats approximately 7.5 meters tall and weighing 1-2 tons, with wheels decorated in metalwork in the elegant imperial carriage style, surmounted by towering "Hoko-dome" (Halberd Caps) reaching high into the sky. During the previous night''s "Yoiyama" (Eve Festival), lanterns are lit on the floats, causing the lacquer and gold leaf decorations to glow with magical beauty. The Mikurumayama Kaikan exhibition hall displays all seven authentic floats year-round, allowing visitors to view them up close throughout the year.

## Event Details and Access

The venue is Takaoka Sekino Shrine (9-56 Suehiro-machi, Takaoka City, Toyama Prefecture) and the surrounding old city center. Access is approximately 10 minutes on foot from Takaoka Station on the Ainokaze Toyama Railway. Viewing is free of charge. The Mikurumayama Kaikan (42 Moriyama-machi, Takaoka City) operates year-round with adult admission of 450 yen.

## Surrounding Attractions

Takaoka City, built as a castle town by Maeda Toshinaga, the second lord of the Kaga Domain, remains a town of living craft tradition where copperware, lacquerware (Takaoka Lacquerware), and silk textiles continue to thrive. Major historical attractions concentrated in the area include Zuiryū-ji Temple (a National Treasure), the Takaoka Daibutsu (one of Japan''s three great Buddha statues), Takaoka Kojō Park, and Kanaya-machi (the birthplace of metal casting, designated as an Important Preservation District). Within Toyama Prefecture, combined sightseeing tours are possible with attractions including the Tateyama Kurobe Alpine Route, the Gokayama Gasshō-zukuri village (a UNESCO World Heritage Site), and the seafood bounty of Toyama Bay and Himi.','takaoka-mikurumayama-matsuri','takaoka-mikurumayama-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q10860730','原宿表参道元氣祭り・スーパーよさこい','Super Yosakoi',NULL,NULL,'Q746573','原宿','Harajuku','高知県','shikoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E3%82%B9%E3%83%BC%E3%83%91%E3%83%BC%E3%82%88%E3%81%95%E3%81%93%E3%81%842022%202.jpg','https://ja.wikipedia.org/wiki/%E5%8E%9F%E5%AE%BF%E8%A1%A8%E5%8F%82%E9%81%93%E5%85%83%E6%B0%A3%E7%A5%AD%E3%82%8A%E3%83%BB%E3%82%B9%E3%83%BC%E3%83%91%E3%83%BC%E3%82%88%E3%81%95%E3%81%93%E3%81%84',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11243525','SKIPシティ国際Dシネマ映画祭','SKIP City International D-Cinema Film Festival','川口市のSKIPシティで行われる映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/SKIP%E3%82%B7%E3%83%86%E3%82%A3%E5%9B%BD%E9%9A%9BD%E3%82%B7%E3%83%8D%E3%83%9E%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6404141','吉祥寺音楽祭','Kichijōji Music Festival','東京都武蔵野市吉祥寺で毎年ゴールデンウィークに開催される音楽イベント (1986-)',NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,1986,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%90%89%E7%A5%A5%E5%AF%BA%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11197438','EARTH VISION 地球環境映像祭','EARTH VISION Global Environment Video Festival','地球環境をテーマとする国際映像祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/EARTH_VISION_%E5%9C%B0%E7%90%83%E7%92%B0%E5%A2%83%E6%98%A0%E5%83%8F%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3959472','神宮式年遷宮','Jingū Shikinen Sengū','伊勢神宮において行われる式年遷宮',NULL,'Q687168','伊勢神宮','Ise Jingū','三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A5%9E%E5%AE%AE%E5%BC%8F%E5%B9%B4%E9%81%B7%E5%AE%AE',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11193741','COUNTDOWN JAPAN','Countdown Japan','日本のロック・フェスティバル (2003-)','music festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2003,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/COUNTDOWN_JAPAN',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11255132','よさこい祭り','Yosakoi Matsuri','高知県高知市の祭り','festival in Kōchi, Japan',NULL,NULL,NULL,'高知県','shikoku',NULL,NULL,1954,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Yosakoi%20Performers%20at%20Kochi%20Yosakoi%20Matsuri%202005%2065.jpg','https://ja.wikipedia.org/wiki/%E3%82%88%E3%81%95%E3%81%93%E3%81%84%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q774193','久喜の提灯祭り・天王様','Lantern Festival of Kuki',NULL,NULL,'Q47535','久喜市','Kuki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kuki%20Ch%C5%8Dchin%20Matsuri%2004.jpg','https://ja.wikipedia.org/wiki/%E4%B9%85%E5%96%9C%E3%81%AE%E6%8F%90%E7%81%AF%E7%A5%AD%E3%82%8A%E3%83%BB%E5%A4%A9%E7%8E%8B%E6%A7%98',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11193584','COMIC NETWORK','Comic Network',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/COMIC_NETWORK',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11200930','GEISAI','GEISAI',NULL,'Contemporary art festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2001,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/GEISAI',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3536029','豊川手筒まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%B1%8A%E5%B7%9D%E6%89%8B%E7%AD%92%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q3334755','扇祭','Ōgi Matsuri','和歌山県那智勝浦町にある熊野那智大社の例大祭',NULL,'Q710359','熊野那智大社','Kumano Nachi Taisha','和歌山県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%89%87%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11227575','KAWASAKIしんゆり映画祭','KAWASAKI Shinyuri Film Festival','神奈川県川崎市麻生区で毎年秋に行われている映画祭',NULL,NULL,NULL,NULL,'神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/KAWASAKI%E3%81%97%E3%82%93%E3%82%86%E3%82%8A%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11256649','あいち国際女性映画祭','Aichi International Women''s Film Festival','愛知県で毎年9月上旬に開催される映画祭',NULL,'Q80434','愛知県','Aichi Prefecture','愛知県','chubu',NULL,NULL,1996,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E3%81%82%E3%81%84%E3%81%A1%E5%9B%BD%E9%9A%9B%E5%A5%B3%E6%80%A7%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11259476','いたばし花火大会','Itabashi Fireworks Festival','東京都板橋区で行われる花火大会','annually-held firework event in Itabashi, Tokyo','Q232635','板橋区','Itabashi','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Itabashi%20Hanabi%20Taikai%20Zenkei%201.jpg','https://ja.wikipedia.org/wiki/%E3%81%84%E3%81%9F%E3%81%B0%E3%81%97%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11274533','なら燈花会','Nara Tōkae','毎年8月に奈良市内で開催されるイベント',NULL,'Q1186358','奈良公園','Nara Park','奈良県','kinki',NULL,NULL,1999,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Kasugano-Field%202007%20Nara-Tokae-Festival.jpg','https://ja.wikipedia.org/wiki/%E3%81%AA%E3%82%89%E7%87%88%E8%8A%B1%E4%BC%9A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11261784','おぢやまつり','Ojiya festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%A2%E3%82%84%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11256803','愛染まつり','Aizen Festival','大阪府大阪市天王寺区の愛染堂勝鬘院で催される祭り',NULL,'Q11400541','勝鬘院','Shōman-in Temple','大阪府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%84%9B%E6%9F%93%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11269668','すすきのアイスワールド','Susukino Ice World','札幌市中央区で開催しているイベント',NULL,'Q11521497','札幌駅前通','Sapporo Ekimae-dori','北海道','hokkaido',NULL,NULL,1981,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%99%E3%81%99%E3%81%8D%E3%81%AE%E3%82%A2%E3%82%A4%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%AB%E3%83%89',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11256639','あいちトリエンナーレ','Aichi Triennale','国際芸術祭','international arts festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2010,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%82%E3%81%84%E3%81%A1%E3%83%88%E3%83%AA%E3%82%A8%E3%83%B3%E3%83%8A%E3%83%BC%E3%83%AC',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11263357','お船祭り (須々岐水神社)','Ship Festival (Susukigisui Shrine)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E8%88%B9%E7%A5%AD%E3%82%8A_(%E9%A0%88%E3%80%85%E5%B2%90%E6%B0%B4%E7%A5%9E%E7%A4%BE)',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11261730','おたる潮まつり','Otaru Ushio Matsuri','小樽市の祭り',NULL,NULL,NULL,NULL,'北海道','hokkaido',43.202940261,141.007523346,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%9F%E3%82%8B%E6%BD%AE%E3%81%BE%E3%81%A4%E3%82%8A',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11263690','かごしま錦江湾サマーナイト大花火大会',NULL,'桜島に面した鹿児島港本港区で毎年8月に開催される花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%8B%E3%81%94%E3%81%97%E3%81%BE%E9%8C%A6%E6%B1%9F%E6%B9%BE%E3%82%B5%E3%83%9E%E3%83%BC%E3%83%8A%E3%82%A4%E3%83%88%E5%A4%A7%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11267368','さいすくい','Saisukui',NULL,NULL,'Q861221','中津市','Nakatsu','三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%84%E3%81%99%E3%81%8F%E3%81%84',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11262273','おはら祭','Ohara Festival','鹿児島県鹿児島市で行われる祭り','Festival in Kagoshima, Japan','Q11442666','天文館','Tenmonkan','鹿児島県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Ohara%20festival%20in%20Kagoshima.jpg','https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%AF%E3%82%89%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11257721','あつぎ鮎まつり',NULL,NULL,NULL,'Q389711','厚木市','Atsugi',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%82%E3%81%A4%E3%81%8E%E9%AE%8E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11265601','くらやみ祭','Kurayami Matsuri','東京都府中市の大國魂神社で行われる例大祭',NULL,'Q611678','大國魂神社','Ōkunitama Shrine','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Okunitama-jinja-24.jpg','https://ja.wikipedia.org/wiki/%E3%81%8F%E3%82%89%E3%82%84%E3%81%BF%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11273205','とっておきの音楽祭',NULL,NULL,NULL,'Q46747','仙台市','Sendai','宮城県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%A8%E3%81%A3%E3%81%A6%E3%81%8A%E3%81%8D%E3%81%AE%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11274443','なにわ淀川花火大会','Naniwa Yodogawa Fireworks Festival','大阪府大阪市で行われる花火大会','fireworks show in Japan','Q35765','大阪市','Osaka','大阪府','kinki',34.709939,135.478978,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%AA%E3%81%AB%E3%82%8F%E6%B7%80%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11260406','うすき竹宵',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%86%E3%81%99%E3%81%8D%E7%AB%B9%E5%AE%B5',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11260579','うつくしまyosakoi祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%86%E3%81%A4%E3%81%8F%E3%81%97%E3%81%BEyosakoi%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11261622','おしろい祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%97%E3%82%8D%E3%81%84%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11262740','おんまく',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%82%93%E3%81%BE%E3%81%8F',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11263474','お走りさん',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E8%B5%B0%E3%82%8A%E3%81%95%E3%82%93',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11265104','きらきらフェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8D%E3%82%89%E3%81%8D%E3%82%89%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11265607','くらわんか花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%8F%E3%82%89%E3%82%8F%E3%82%93%E3%81%8B%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11265746','くろほね夏まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8F%E3%82%8D%E3%81%BB%E3%81%AD%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11267412','さいたま市民まつり',NULL,NULL,NULL,NULL,NULL,NULL,'埼玉県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%84%E3%81%9F%E3%81%BE%E5%B8%82%E5%9B%BD%E9%9A%9B%E3%81%B5%E3%82%8C%E3%81%82%E3%81%84%E3%83%95%E3%82%A7%E3%82%A2',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11267583','さかいで大橋まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%8B%E3%81%84%E3%81%A7%E5%A4%A7%E6%A9%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11267580','さかいで塩まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%8B%E3%81%84%E3%81%A7%E5%A1%A9%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11267963','させぼシーサイドフェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%9B%E3%81%BC%E3%82%B7%E3%83%BC%E3%82%B5%E3%82%A4%E3%83%89%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11270948','たけの海上花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%9F%E3%81%91%E3%81%AE%E6%B5%B7%E4%B8%8A%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11271017','たたら祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%9F%E3%81%9F%E3%82%89%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11273189','とちぎ夏まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%A8%E3%81%A1%E3%81%8E%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11275931','はんだ山車まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%AF%E3%82%93%E3%81%A0%E5%B1%B1%E8%BB%8A%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11278128','まいづる細川幽斎田辺城まつり',NULL,NULL,NULL,NULL,NULL,NULL,'和歌山県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BE%E3%81%84%E3%81%A5%E3%82%8B%E7%B4%B0%E5%B7%9D%E5%B9%BD%E6%96%8E%E7%94%B0%E8%BE%BA%E5%9F%8E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11278129','まいづる魚まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BE%E3%81%84%E3%81%A5%E3%82%8B%E9%AD%9A%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11278373','まち遊びフェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BE%E3%81%A1%E9%81%8A%E3%81%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11265785','ぐず焼き祭り','Guzuyaki Festival','石川県加賀市動橋町で毎年8月27日、28日、29日に行われる祭り。','festival in Iburihashi, Kaga city, Ishikawa prefecture, Japan in 27th, 28th, and 29th August each year',NULL,NULL,NULL,'岐阜県','chubu',36.325416666,136.388638888,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Guzu%20going%20round%20the%20fire%204.jpg','https://ja.wikipedia.org/wiki/%E3%81%90%E3%81%9A%E7%84%BC%E3%81%8D%E7%A5%AD%E3%82%8A',NULL,95,'drafted','## 概要

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
','## Overview

The Guzuyaki Festival (Guzu-yaki Matsuri) is a traditional folk event marking the end of summer, held annually in August in Uozu City, Toyama Prefecture. A giant effigy of a fish called "guzu" (a regional name for goby-family fish) made of bamboo and straw is paraded through the city before being ceremonially burned at the festival''s climax, making it a distinctive fire festival unique to the Hokuriku region.

Centered on Uozu Fishing Port and Suwa Shrine, the festival uniquely combines local beliefs praying for fishing safety and bountiful catches with the ancient Japanese tradition of spirit-sending, which purifies summer misfortunes through fire. For local residents and fishermen, it remains an indispensable event coloring the end of summer in their hometown.

## History and Origins

The origins of the Guzuyaki Festival trace back to local beliefs intimately tied to Uozu''s fishing culture. Toyama Bay has long been renowned as a rich fishing ground, with summer goby and sillago fisheries supporting the regional economy. Fishermen expressed gratitude to the sea and prayed for navigational safety while also continuing the ritual practice of burning a "guzu" effigy to ward off plagues and misfortunes that arise during the height of summer.

The term "guzu" is a dialect word along the Toyama Bay coast referring to goby-family fish. Crafting an effigy of this fish, parading it through neighborhoods, and then burning it follows the same logic as the "insect-sending" and "spirit-sending" rituals of rice-cultivating regions. It functions as a folk ritual transferring communal misfortunes onto a symbolic object for purification.

Today, local neighborhood associations, merchants'' associations, and fishing industry stakeholders cooperate to organize an executive committee that preserves the traditional event while opening it to tourists as an annual summer festival of the region.

## Highlights

**Crafting and Procession of the "Guzu" Effigy**
For several days before the festival, local volunteers craft the "guzu" effigy from bamboo and straw. The sight of a giant fish effigy several meters long parading through the city to the rhythm of drums and flutes is a rustic and powerful scene unique to a Hokuriku port town.

**Suwa Shrine Ritual**
At Suwa Shrine, the festival''s spiritual core, Shinto priests conduct solemn rituals praying for fishing safety and bountiful catches. As the heart of local belief, it represents a sacred moment passed down across generations.

**Burning of the "Guzu"**
The climax is the ceremony of burning the "guzu" effigy in an open square after its procession through town. The fish disappearing into the flames symbolizes the communal sending-off of summer misfortunes and impurities. Participants press their palms together to witness the festival''s conclusion.

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
','guzuyaki-festival','guzuyaki-festival',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11271139','たてもん祭り','Uozu Tatemon Festival','富山県魚津市の諏訪神社の夏季祭礼',NULL,'Q11631937','諏訪神社','Suwa Shrine','長野県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Uozu-tatemon.jpg','https://ja.wikipedia.org/wiki/%E3%81%9F%E3%81%A6%E3%82%82%E3%82%93%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11268196','さぬき映画祭','Sanuki Film Festival','香川県内で毎年度開催されている映画祭',NULL,NULL,NULL,NULL,'香川県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%AC%E3%81%8D%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11261786','おぢや風船一揆','Ojiya balloon festival','新潟県小千谷市で行われる熱気球と花火によるイベント',NULL,'Q819174','小千谷市','Ojiya','新潟県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/2006%20Ojiya%20balloon%20festival%20006.jpg','https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%A2%E3%82%84%E9%A2%A8%E8%88%B9%E4%B8%80%E6%8F%86',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11278738','みあれ祭','Miare Festival','宗像大社秋季大祭の最初に行われる祭礼',NULL,'Q498047','玄界灘','Genkai Sea','福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%AE%97%E5%83%8F%E5%A4%A7%E7%A4%BE%E3%81%BF%E3%81%82%E3%82%8C%E7%A5%AD.jpg','https://ja.wikipedia.org/wiki/%E3%81%BF%E3%81%82%E3%82%8C%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11274711','にいはま納涼花火大会',NULL,'日本の花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%AB%E3%81%84%E3%81%AF%E3%81%BE%E7%B4%8D%E6%B6%BC%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11273191','とちぎ秋まつり','Tochigi Autumn Festival','栃木県栃木市の祭り',NULL,NULL,NULL,NULL,'栃木県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tochigi%20autumn%20festival%2Cfestival%20car%20of%20Yorozucho1-2-3chome%2Ctochigi%20city%2Cjapan.jpg','https://ja.wikipedia.org/wiki/%E3%81%A8%E3%81%A1%E3%81%8E%E7%A7%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11263112','お旅まつり','Otabi Festival',NULL,'an annual three-day festival held in Komatsu, Japan in May',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/OTABI%20MATSURI%20FESTIVAL%20KOMATSU%20002.JPG','https://ja.wikipedia.org/wiki/%E3%81%8A%E6%97%85%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11272648','てだこまつり','Urasoe Tedako Festival',NULL,NULL,'Q695895','浦添市','Urasoe',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tedako%20Matsuri%20festival%20brings%20communities%20together%20140720-M-LN208-489.jpg','https://ja.wikipedia.org/wiki/%E3%81%A6%E3%81%A0%E3%81%93%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11271457','定禅寺ストリートジャズフェスティバル','Jozenji Street Jazz Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AE%9A%E7%A6%85%E5%AF%BA%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%88%E3%82%B8%E3%83%A3%E3%82%BA%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11278423','まつりつくば','Matsuri Tsukuba',NULL,NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BE%E3%81%A4%E3%82%8A%E3%81%A4%E3%81%8F%E3%81%B0',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11270952','たけふ菊人形','Takefu Chrysanthemum Doll Festival','毎年10月上旬から11月上旬にかけて福井県越前市の武生中央公園で行われる菊人形',NULL,'Q18337240','武生中央公園','Takefu Central Park','福井県','chubu',NULL,NULL,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Takefu%20Chrysanthemum%20Doll%20Festival%202014-01.jpg','https://ja.wikipedia.org/wiki/%E3%81%9F%E3%81%91%E3%81%B5%E8%8F%8A%E4%BA%BA%E5%BD%A2',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11265326','くきのうみ花火の祭典',NULL,'北九州市の花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%8F%E3%81%8D%E3%81%AE%E3%81%86%E3%81%BF%E8%8A%B1%E7%81%AB%E3%81%AE%E7%A5%AD%E5%85%B8',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11262075','おのみち住吉花火まつり',NULL,'広島県尾道市で行われる花火大会',NULL,'Q696694','尾道市','Onomichi','大阪府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%AE%E3%81%BF%E3%81%A1%E4%BD%8F%E5%90%89%E8%8A%B1%E7%81%AB%E3%81%BE%E3%81%A4%E3%82%8A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11268205','さぬき高松まつり','Sanuki Takamatsu Festival',NULL,'festival in Takamatsu, Japan',NULL,NULL,NULL,'香川県','shikoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Japan%20-%20Takamatsu%20Awa%20Odori%20Bon%20Festival%2003.jpg','https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%AC%E3%81%8D%E9%AB%98%E6%9D%BE%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11272296','つくりもんまつり','Tsukurimon Festival','富山県高岡市福岡町で行なわれる奇祭',NULL,'Q17','日本','Japan','富山県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/National%20Museum%20of%20Ethnology%2C%20Osaka%20-%20Ranry%C3%B4-%C3%B4%20statue%20made%20of%20vegetables%20-%20Festival%20%22Tsukurimon-matsuri%22%20-%20Takaoka%2C%20Toyama%20pref.%20-%20Collected%20in%202012.jpg','https://ja.wikipedia.org/wiki/%E3%81%A4%E3%81%8F%E3%82%8A%E3%82%82%E3%82%93%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11272927','とうろう流しと大花火大会',NULL,'福井県敦賀市の花火大会',NULL,NULL,NULL,NULL,'福井県','chubu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%A8%E3%81%86%E3%82%8D%E3%81%86%E6%B5%81%E3%81%97%E3%81%A8%E5%A4%A7%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11261149','えんま市',NULL,'新潟県柏崎市で行われる夏祭り',NULL,'Q633983','柏崎市','Kashiwazaki','新潟県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%88%E3%82%93%E3%81%BE%E5%B8%82',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11269431','じゃんとこい魚津まつり','Jantokoi Uozu Festival','富山県魚津市で開催される夏祭り',NULL,NULL,NULL,NULL,'富山県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Uozu-tatemon.jpg','https://ja.wikipedia.org/wiki/%E3%81%98%E3%82%83%E3%82%93%E3%81%A8%E3%81%93%E3%81%84%E9%AD%9A%E6%B4%A5%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11261257','おおさか映画祭','Osaka Cinema Festival','大阪府で行われる映画祭',NULL,NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%8A%E3%81%95%E3%81%8B%E3%82%B7%E3%83%8D%E3%83%9E%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11275775','はままつ映画祭','Hamamatsu Film Festival','静岡県浜松市で開催される映画祭',NULL,NULL,NULL,NULL,'静岡県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%AF%E3%81%BE%E3%81%BE%E3%81%A4%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11277692','ほうらい祭り','Hōrai Matsuri','石川県白山市で開催される祭り',NULL,'Q11646557','金剱宮','Kinken-gū','石川県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tukurimon%20of%20Hourai%20Festival.JPG','https://ja.wikipedia.org/wiki/%E3%81%BB%E3%81%86%E3%82%89%E3%81%84%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11255141','YOSAKOIソーラン祭り','Yosakoi Soran Festival','6月上旬に北海道札幌市で行われるイベント',NULL,NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,1992,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/YOSAKOI%20Soran%20Festival.jpg','https://ja.wikipedia.org/wiki/YOSAKOI%E3%82%BD%E3%83%BC%E3%83%A9%E3%83%B3%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11268616','さんピンCAMP',NULL,'日本語ラップのイベント',NULL,'Q11509589','日比谷野外音楽堂','Hibiya Open-Air Concert Hall',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%82%93%E3%83%94%E3%83%B3CAMP',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11268878','したまちコメディ映画祭in台東','Shitamachi Comedy Film Festival in Taitung','東京都台東区で開催されていた映画祭',NULL,'Q232641','台東区','Taitō-ku','東京都','kanto',NULL,NULL,2008,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%97%E3%81%9F%E3%81%BE%E3%81%A1%E3%82%B3%E3%83%A1%E3%83%87%E3%82%A3%E6%98%A0%E7%94%BB%E7%A5%ADin%E5%8F%B0%E6%9D%B1',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11276657','ひらかた大菊人形','Hirakata Dai Kiku-Ningyō','大阪府枚方市のひらかたパークで行われていた展覧会',NULL,'Q302897','ひらかたパーク','Hirakata Park','大阪府','kinki',NULL,NULL,1910,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hirakata-kikuningyo3213.JPG','https://ja.wikipedia.org/wiki/%E3%81%B2%E3%82%89%E3%81%8B%E3%81%9F%E5%A4%A7%E8%8F%8A%E4%BA%BA%E5%BD%A2',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11258475','あやべ水無月まつり','Ayabe Minazuki Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%82%E3%82%84%E3%81%B9%E6%B0%B4%E7%84%A1%E6%9C%88%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11263450','お蔵出し映画祭','Okuradashi Film Festival',NULL,'film festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E8%94%B5%E5%87%BA%E3%81%97%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11263106','お手火祭り','Otebi Matsuri','広島県福山市の沼名前神社で行われる火祭り',NULL,'Q11554446','沼名前神社','Nunakuma Shrine','広島県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E6%89%8B%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7677467','高山祭','Takayama Festival','岐阜県高山市で開催される春の山王祭と秋の八幡祭の総称','Japanese festival','Q11537980','桜山八幡宮','Sakurayama Hachimangū','岐阜県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%A4%A7%E5%9B%BD%E5%8F%B0%20%28%E5%B2%90%E9%98%9C%E7%9C%8C%E9%AB%98%E5%B1%B1%E5%B8%82%29%20-%20panoramio%20%282%29.jpg','https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B1%B1%E7%A5%AD','https://en.wikipedia.org/wiki/Takayama_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6406163',NULL,'Kijimuna Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://en.wikipedia.org/wiki/Kijimuna_Festival',25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5952410','金沢百万石まつり','Hyakumangoku Matsuri','毎年6月に石川県金沢市で行われる祭り',NULL,NULL,NULL,NULL,'石川県','chubu',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Hyakumangoku%20Matsuri%20in%20front%20of%20Kanazawa%20station.jpg','https://ja.wikipedia.org/wiki/%E9%87%91%E6%B2%A2%E7%99%BE%E4%B8%87%E7%9F%B3%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Hyakumangoku_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6416609','岸和田だんじり祭','Kishiwada Danjiri Matsuri','大阪府岸和田市旧市地区で行われる祭','Danjiri Matsuri festival in Japan',NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,1745,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Kishiwada-Danjiri-Matsuri%20Osaka%20Japan.jpg','https://ja.wikipedia.org/wiki/%E5%B2%B8%E5%92%8C%E7%94%B0%E3%81%A0%E3%82%93%E3%81%98%E3%82%8A%E7%A5%AD','https://en.wikipedia.org/wiki/Kishiwada_Danjiri_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7813900','東京国際レズビアン&ゲイ映画祭','Rainbow Reel Tokyo',NULL,'International film festival for LGBT audiences','Q1490','東京都','Tokyo','東京都','kanto',35.683333333,139.766666666,1992,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%AC%E3%82%A4%E3%83%B3%E3%83%9C%E3%83%BC%E3%83%BB%E3%83%AA%E3%83%BC%E3%83%AB%E6%9D%B1%E4%BA%AC','https://en.wikipedia.org/wiki/Rainbow_Reel_Tokyo',70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7811554','戸畑祇園大山笠','Tobata Gion Festival','北九州市戸畑区にて行われる祭り','Annual festival in Kyushu, Japan',NULL,NULL,NULL,'鳥取県','chugoku',NULL,NULL,1803,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Tobata%20yamagasa%20at%20night.JPG','https://ja.wikipedia.org/wiki/%E6%88%B8%E7%95%91%E7%A5%87%E5%9C%92%E5%A4%A7%E5%B1%B1%E7%AC%A0','https://en.wikipedia.org/wiki/Tobata_Gion_Yamagasa_festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7814002','〈東京の夏〉音楽祭','Tokyo Summer Festival','アリオン音楽財団が開催する音楽祭',NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%80%88%E6%9D%B1%E4%BA%AC%E3%81%AE%E5%A4%8F%E3%80%89%E9%9F%B3%E6%A5%BD%E7%A5%AD','https://en.wikipedia.org/wiki/Tokyo_Summer_Festival',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7903785','和霊大祭','Uwajima Ushi-oni Festival','愛媛県宇和島市で行われる夏祭り',NULL,NULL,NULL,NULL,'愛媛県','shikoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Ushioni%20mask.jpg','https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9C%8A%E5%A4%A7%E7%A5%AD','https://en.wikipedia.org/wiki/Uwajima_Ushi-oni_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7849923','土崎神明社祭の曳山行事','Tsuchizaki Shinmei Shrine Festival','秋田県秋田市にある土崎神明社の例祭',NULL,'Q11423430','土崎神明社','Tsuchizaki Shinmeisha','秋田県','tohoku',NULL,NULL,1705,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/Tsuchi-yama-tsunafuru.jpg','https://ja.wikipedia.org/wiki/%E5%9C%9F%E5%B4%8E%E7%A5%9E%E6%98%8E%E7%A4%BE%E7%A5%AD%E3%81%AE%E6%9B%B3%E5%B1%B1%E8%A1%8C%E4%BA%8B','https://en.wikipedia.org/wiki/Tsuchizaki_Shinmeisha_Shrine_Annual_Celebration_And_The_Float_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11642807','那覇まつり','Naha Great Tug-of-War Festival',NULL,'cultural event in Okinawa Prefecture, Japan',NULL,NULL,NULL,'沖縄県','okinawa',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Naha%20Rope%20001.jpg','https://ja.wikipedia.org/wiki/%E9%82%A3%E8%A6%87%E5%A4%A7%E7%B6%B1%E6%8C%BD%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Naha_Great_Tug-of-War_Festival',80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7398902','佐賀インターナショナルバルーンフェスタ','Saga International Balloon Fiesta','日本の佐賀県で行われる熱気球の競技会・イベント','Hot air balloon festival in Saga, Japan',NULL,NULL,NULL,'佐賀県','kyushu',33.255555555,130.244444444,NULL,10,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Saga%20balloon%202007%201.jpg','https://ja.wikipedia.org/wiki/%E4%BD%90%E8%B3%80%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%8A%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB%E3%83%90%E3%83%AB%E3%83%BC%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF','https://en.wikipedia.org/wiki/Saga_International_Balloon_Fiesta',100,'drafted','## 概要

佐賀インターナショナルバルーンフェスタは、毎年10月下旬から11月初旬にかけて佐賀県佐賀市で開催される、アジア最大級の熱気球競技大会です。佐賀平野を流れる嘉瀬川河川敷を会場に、世界各国から100機を超える色とりどりの熱気球が集結し、5日間の開催期間中に約80万人もの観客が訪れる、佐賀を代表する秋の風物詩となっています。

朝霧に包まれた佐賀平野を背景に、夜明けとともに次々と空へ舞い上がる熱気球の光景は、視覚的なインパクトと静謐さを兼ね備えた、世界でも有数の熱気球イベントとして国際的に高い評価を得ています。

## 歴史と由来

佐賀インターナショナルバルーンフェスタの歴史は、1978年(昭和53年)に福岡県甘木市(現・朝倉市)で開催された第1回大会に遡ります。その後、1980年(昭和55年)に佐賀県佐賀市へと開催地が移され、嘉瀬川河川敷という熱気球競技に理想的な広大な平野と安定した気象条件を活かして発展してきました。

1989年(平成元年)には熱気球世界選手権大会の開催地としても選ばれ、世界各国のトップパイロットが集結する国際大会へと成長。1997年(平成9年)と2017年(平成29年)にも熱気球世界選手権を開催し、佐賀を「アジアの熱気球の聖地」として世界に位置付けました。

開催地となる嘉瀬川河川敷は、東西に開けた広大な平野と、有明海から吹く穏やかで安定した季節風という、熱気球競技に必要な気象条件を完璧に満たす立地です。この地理的優位性が、フェスタの長期的な発展を支えてきました。

## 見どころ

**早朝の一斉離陸 (Morning Mass Ascension)**
午前7時頃、夜明けの空に約100機の熱気球が一斉に離陸する光景は、フェスタ最大のハイライトです。バーナーの炎の音と朝霧に映える気球の色彩が織りなす情景は、写真愛好家にも絶大な人気を誇ります。

**バルーン・ファンタジア**
通常の球形だけでなく、動物やキャラクター、建物を模した変形気球が登場する企画。子ども連れの家族に特に人気のプログラムです。

**ラ・モンゴルフィエ・ノクチューン (La Montgolfier Nocturne)**
夜間に地上に係留された気球が音楽に合わせて一斉にバーナーを点火し、巨大な発光体として夜空を彩る幻想的なイベント。フェスタ期間中の特定の夜にのみ開催されます。

**熱気球ホンダグランプリ**
プロパイロットによる本格的な競技。決められた目標地点に近い場所へマーカーを投下する精度を競う「マーカー競技」など、観客にも分かりやすいルールで楽しめます。

## 開催情報

- **開催地**: 佐賀県佐賀市嘉瀬川河川敷
- **開催時期**: 毎年10月下旬から11月初旬の5日間
- **アクセス**: 期間中はJR長崎本線に臨時駅「バルーンさが駅」が開設されます。JR佐賀駅からは車で約15分、福岡空港からは高速バスとJRを乗り継いで約1時間30分
- **観覧料**: 無料(一部有料席あり)
- **公式情報**: [佐賀インターナショナルバルーンフェスタ公式サイト](https://www.sibf.jp/)

## 周辺の見どころ

佐賀市内には、鍋島藩の城下町の面影を残す佐賀城本丸歴史館や、有明海の干満差を活かした漁業文化を伝える施設が点在します。フェスタ会場から車で30分圏内には、有田焼の里として知られる有田町、伊万里焼の伊万里市、温泉地として人気の嬉野温泉・武雄温泉といった九州西部を代表する観光地が広がります。

10月下旬の佐賀は気候も穏やかで、フェスタ観覧と九州西部の文化観光・温泉巡りを組み合わせた周遊旅行に最適なシーズンです。

## 関連情報

- 開催月: 10月(秋)
- 都道府県: 佐賀県(九州)
- 起源: 1978年(佐賀開催は1980年から)
- 規模: 約100機・観客約80万人
','## Overview

The Saga International Balloon Fiesta is the largest hot air balloon competition in Asia, held annually in late October to early November in Saga City, Saga Prefecture. Set against the vast Kase River floodplain, the event attracts over 100 balloons from around the world and draws approximately 800,000 visitors over its five-day run, making it one of Saga''s most iconic autumn attractions.

The sight of dozens of colorful balloons ascending into the misty dawn sky above the Saga Plain has earned international acclaim as one of the most visually stunning hot air balloon events in the world.

## History and Origins

The festival traces its origins to 1978, when the first competition was held in Amagi City (now Asakura City) in neighboring Fukuoka Prefecture. In 1980, the event relocated to Saga City, taking advantage of the Kase River floodplain''s ideal terrain and stable atmospheric conditions for ballooning.

In 1989, the festival hosted its first Hot Air Balloon World Championship, cementing its international status. Saga returned as the World Championship venue in 1997 and 2017, establishing the city as Asia''s premier destination for competitive ballooning.

The Kase River venue offers the perfect combination of an open east-west-running plain and the gentle, predictable seasonal winds from the Ariake Sea — conditions that make it one of the most reliable balloon competition sites in the world.

## Highlights

**Morning Mass Ascension**
Around 7:00 AM, approximately 100 balloons launch simultaneously into the dawn sky. The sound of burners and the contrast of vivid balloon colors against the morning mist create an unforgettable spectacle, especially popular with photographers.

**Balloon Fantasia**
A special program featuring novelty-shaped balloons resembling animals, characters, and buildings. A highlight for families with children.

**La Montgolfière Nocturne**
On select evenings, tethered balloons ignite their burners in synchronized patterns set to music, transforming the night sky into a glowing, choreographed display.

**Honda Grand Prix Balloon Competition**
The serious side of the event — professional pilots compete in target-based contests where balloons must drop markers as close as possible to designated points, offering spectators a clear sense of skill and precision.

## Visitor Information

- **Location**: Kase River floodplain, Saga City, Saga Prefecture
- **Dates**: Five days, late October to early November (annually)
- **Access**: A temporary "Balloon Saga" station opens on the JR Nagasaki Main Line during the event. From JR Saga Station: ~15 minutes by car. From Fukuoka Airport: ~1 hour 30 minutes via highway bus and JR train.
- **Admission**: Free (some reserved seating available for purchase)
- **Official Site**: [Saga International Balloon Fiesta](https://www.sibf.jp/en/)

## Where to Stay

Saga City offers a range of accommodations from business hotels near JR Saga Station to traditional ryokan in nearby hot spring towns. For visitors planning to combine the festival with regional sightseeing, the hot spring resorts of **Ureshino Onsen** and **Takeo Onsen** (both within an hour''s drive) provide a uniquely Japanese lodging experience after a day at the balloons.

## Nearby Attractions

Within 30 minutes of the festival grounds, visitors can explore:
- **Saga Castle History Museum**: The reconstructed honmaru palace of the former Nabeshima Domain
- **Arita**: The historic porcelain town where Japan''s first porcelain was produced
- **Imari**: Famous for the Imari ware export ceramics
- **Yoshinogari Historical Park**: A reconstructed Yayoi-period (300 BCE - 300 CE) settlement

Late October offers mild weather ideal for combining the festival with a wider tour of western Kyushu''s cultural sites and hot springs.

## Quick Facts

- Month: October (Autumn)
- Prefecture: Saga (Kyushu region)
- Founded: 1978 (Saga venue since 1980)
- Scale: ~100 balloons, ~800,000 visitors
','saga-international-balloon-fiesta','saga-international-balloon-fiesta',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11662018','青森インターナショナルLGBTフィルムフェスティバル','Aomori International LGBT Film Festival',NULL,'LGBTQ film festival in Japan','Q146790','青森市','Aomori','青森県','tohoku',NULL,NULL,2006,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%9D%92%E6%A3%AE%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%8A%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%ABLGBT%E3%83%95%E3%82%A3%E3%83%AB%E3%83%A0%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Aomori_International_LGBT_Film_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7402591','斎王まつり','Saiō Matsuri','三重県明和町で開催される祭り','festival in Meiwa, Mie prefecture, Japan','Q3135853','斎宮跡','Ruins of Saikū','三重県','kinki',NULL,NULL,1983,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/SaioMatsuri.jpg','https://ja.wikipedia.org/wiki/%E6%96%8E%E7%8E%8B%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Sai%C5%8D_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11629710','西都古墳まつり','Saito Kofun Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%A5%BF%E9%83%BD%E5%8F%A4%E5%A2%B3%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Saito_Kofun_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7497628','新庄まつり','Shinjō Matsuri','山形県新庄市で開催される祭','Japanese festival',NULL,NULL,NULL,'山形県','tohoku',NULL,NULL,1755,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/ShinjoMatsuriNight.jpg','https://ja.wikipedia.org/wiki/%E6%96%B0%E5%BA%84%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Shinj%C5%8D_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6417750','北上・みちのく芸能まつり','Kitakami Michinoku Traditional Dance Festival','岩手県北上市の祭り','Summer festival in Iwate, Japan',NULL,NULL,NULL,'岩手県','tohoku',NULL,NULL,1962,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Oni%20Kenbai%201%2C%20Kitakami%2C%20Iwate.jpg','https://ja.wikipedia.org/wiki/%E5%8C%97%E4%B8%8A%E3%83%BB%E3%81%BF%E3%81%A1%E3%81%AE%E3%81%8F%E8%8A%B8%E8%83%BD%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Kitakami_Michinoku_Traditional_Dance_Festival',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6455253','皇霊祭','Kōreisai','宮中祭祀のひとつ','Japanese holiday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1878,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%9A%87%E9%9C%8A%E7%A5%AD','https://en.wikipedia.org/wiki/K%C5%8Dreisai',65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q120776905','LuckyFes','LuckyFes','日本の音楽フェスティバル','Japanese music festival',NULL,NULL,NULL,'茨城県','kanto',36.400555555,140.591388888,2022,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/LuckyFes','https://en.wikipedia.org/wiki/LuckyFes',75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7119701','教祖祭PL花火芸術','PL Art of Fireworks','パーフェクト リバティー教団（PL）の祭礼','Fireworks show in Japan','Q490928','富田林市','Tondabayashi',NULL,NULL,NULL,NULL,1953,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/PL%20Fireworks2010-5.jpg','https://ja.wikipedia.org/wiki/%E6%95%99%E7%A5%96%E7%A5%ADPL%E8%8A%B1%E7%81%AB%E8%8A%B8%E8%A1%93','https://en.wikipedia.org/wiki/PL_Art_of_Fireworks',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6080166','石取祭','Ishidori Matsuri','日本の三重県桑名市で開催される祭','festival in Kuwana, Mie, Japan','Q11537501','桑名宗社','Kuwana Sōsha','三重県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/IshidoriMatsuri.JPG','https://ja.wikipedia.org/wiki/%E7%9F%B3%E5%8F%96%E7%A5%AD','https://en.wikipedia.org/wiki/Ishidori_Matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6920834','マウント・フジ・ジャズ・フェスティバル','Mount Fuji Jazz Festival',NULL,'Music festival in Japan',NULL,NULL,NULL,'神奈川県','kanto',35.4192899,138.9014125,1986,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Mount%20Fuji%20Jazz%20fess%201994%208%2028%2002.jpg','https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%A6%E3%83%B3%E3%83%88%E3%83%BB%E3%83%95%E3%82%B8%E3%83%BB%E3%82%B8%E3%83%A3%E3%82%BA%E3%83%BB%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB','https://en.wikipedia.org/wiki/Mount_Fuji_Jazz_Festival',90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q5637073','八戸三社大祭','Hachinohe Sansha Taisai','青森県八戸市で行われる祭礼','festival of Hachinohe, Aomori, Japan',NULL,NULL,NULL,'青森県','tohoku',NULL,NULL,1721,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hachinohe%20Sansha%20Taisai%20Festival%2C%202%20August%202014-001.JPG','https://ja.wikipedia.org/wiki/%E5%85%AB%E6%88%B8%E4%B8%89%E7%A4%BE%E5%A4%A7%E7%A5%AD','https://en.wikipedia.org/wiki/Hachinohe_Sansha_Taisai',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11408926','博多どんたく','Hakata Dontaku','祭り','annual festival in Fukuoka, Japan',NULL,NULL,NULL,'福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hakata%20Dontaku%2078338697%20org.jpg','https://ja.wikipedia.org/wiki/%E5%8D%9A%E5%A4%9A%E3%81%A9%E3%82%93%E3%81%9F%E3%81%8F','https://en.wikipedia.org/wiki/Hakata_Dontaku',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q7972772','わっしょい百万夏祭り','Wasshoi Hyakuman Natsumatsuri',NULL,'matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%82%8F%E3%81%A3%E3%81%97%E3%82%87%E3%81%84%E7%99%BE%E4%B8%87%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A','https://en.wikipedia.org/wiki/Wasshoi_Hyakuman_Natsumatsuri',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6349714','角館のお祭り','Kakunodate Festival','秋田県仙北市の神明社と成就院薬師堂の祭','Japanese festival','Q11630890','角館','Kakunodate','秋田県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kakunodate%20maturi%202008a.jpg','https://ja.wikipedia.org/wiki/%E8%A7%92%E9%A4%A8%E3%81%AE%E3%81%8A%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Kakunodate-matsuri',85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q8054630',NULL,'Yokohama Jazz Festival',NULL,'jazz festival',NULL,NULL,NULL,'神奈川県','kanto',35.3794,139.647,NULL,NULL,NULL,NULL,NULL,'https://en.wikipedia.org/wiki/Yokohama_Jazz_Festival',35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q6003417','伊万里トンテントン祭り','Imari Ton-Ten-Ton Festival',NULL,'annual fighting festival held in Japan','Q857266','伊万里市','Imari','佐賀県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BC%8A%E4%B8%87%E9%87%8C%E3%83%88%E3%83%B3%E3%83%86%E3%83%B3%E3%83%88%E3%83%B3%E7%A5%AD%E3%82%8A','https://en.wikipedia.org/wiki/Imari_Ton-Ten-Ton_Festival',60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11615626','山形花笠まつり','Yamagata Hanagasa Festival','山形県山形市で開催される祭','tōhoku Japanese festival',NULL,NULL,NULL,'山形県','tohoku',NULL,NULL,1963,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hanagasa%20Festa%202002.jpg',NULL,'https://en.wikipedia.org/wiki/Yamagata_Hanagasa_Festival',70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11383026','佐原の大祭','Sawara Float Festival','千葉県香取市佐原で行われる本宿祇園祭と新宿秋祭りの総称',NULL,'Q17221438','八坂神社','Yasaka Shrine','千葉県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BD%90%E5%8E%9F%E3%81%AE%E5%A4%A7%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11400381','勝浦大漁まつり','Katsuura Autumn Festival','千葉県勝浦市の祭礼',NULL,NULL,NULL,NULL,'千葉県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8B%9D%E6%B5%A6%E5%A4%A7%E6%BC%81%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11408485','南部の火祭り','Nanbu Fire Festival',NULL,NULL,'Q1204802','南部町','Nanbu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8D%97%E9%83%A8%E3%81%AE%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11374881','京都国際学生映画祭','Kyoto International Student Film and Video Festival',NULL,NULL,'Q120730','京都府','Kyoto Prefecture','京都府','kinki',NULL,NULL,1997,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E5%9B%BD%E9%9A%9B%E5%AD%A6%E7%94%9F%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11400226','勝山まつり','Katsuyama Festival',NULL,NULL,'Q861230','真庭市','Maniwa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8B%9D%E5%B1%B1%E5%96%A7%E5%98%A9%E3%81%A0%E3%82%93%E3%81%98%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11400243','勝山左義長','Katsuyama Sagichō','福井県勝山市で2月に行われる祭り','festival in Katsuyama, Fukui Prefecture, Japan','Q847543','勝山市','Katsuyama','福井県','chubu',NULL,NULL,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Kaminaga.jpg','https://ja.wikipedia.org/wiki/%E5%8B%9D%E5%B1%B1%E5%B7%A6%E7%BE%A9%E9%95%B7',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11404276','北野天神社','Kitano Tenjinsha','埼玉県所沢市の神社','Shinto shrine in Saitama Prefecture, Japan',NULL,NULL,NULL,'埼玉県','kanto',35.790695,139.428834,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kitanotenjinsha-saitama-2012.jpg','https://ja.wikipedia.org/wiki/%E5%8C%97%E9%87%8E%E5%A4%A9%E7%A5%9E%E7%A4%BE_(%E6%89%80%E6%B2%A2%E5%B8%82)',NULL,95,'skipped',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11387821','元始祭','Genshisai','宮中祭祀のひとつ',NULL,'Q7797685','宮中三殿','Three Palace Sanctuaries',NULL,NULL,NULL,NULL,1870,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%85%83%E5%A7%8B%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11377772','仙台七夕花火祭','Sendai Tanabata Fireworks Festival','8月5日に仙台市で開催される花火大会',NULL,'Q11627260','西公園','Nishi Park','宮城県','tohoku',NULL,NULL,1970,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Sendai%20Tanabata%20Fireworks%20Festival%202009.jpg','https://ja.wikipedia.org/wiki/%E4%BB%99%E5%8F%B0%E4%B8%83%E5%A4%95%E8%8A%B1%E7%81%AB%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11402390','北海へそ祭り','Hokkaido Belly Button Festival','日本の北海道の祭り','festival in Furano, Japan',NULL,NULL,NULL,'北海道','hokkaido',43.347434358,142.388015401,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%8C%97%E6%B5%B7%E3%81%B8%E3%81%9D%E7%A5%AD%E3%82%8A',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11395759','出石初午大祭','Izushi Hatsuuma Taisai','兵庫県豊岡市で行われる祭',NULL,'Q11516349','有子山稲荷神社','Arikoyama Inari Shrine','兵庫県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%87%BA%E7%9F%B3%E5%88%9D%E5%8D%88%E5%A4%A7%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11386340','修正鬼会',NULL,NULL,NULL,NULL,NULL,NULL,'大分県','kyushu',33.578744,131.541622,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BF%AE%E6%AD%A3%E9%AC%BC%E4%BC%9A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11389952','全日本チンドンコンクール',NULL,'日本のイベント',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%85%A8%E6%97%A5%E6%9C%AC%E3%83%81%E3%83%B3%E3%83%89%E3%83%B3%E3%82%B3%E3%83%B3%E3%82%AF%E3%83%BC%E3%83%AB',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11400363','勝毎花火大会','Kachimai Fireworks',NULL,'Fireworks show in Japan','Q177149','帯広市','Obihiro','北海道','hokkaido',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%8B%9D%E6%AF%8E%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11381635','但馬牛まつり','Tajima Beef Festival','兵庫県立但馬牧場公園（新温泉町）で開催される祭典',NULL,'Q11392939','兵庫県立但馬牧場公園','Hyōgo Prefectural Tajima Pasture Park','兵庫県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BD%86%E9%A6%AC%E7%89%9B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11371735','二百二十日','Nihyakuhatsuka','雑節のひとつ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%8C%E7%99%BE%E4%BA%8C%E5%8D%81%E6%97%A5',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11388927','入梅',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%85%A5%E6%A2%85',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11381046','伏木曳山祭','Fushiki Hikiyama Festival','富山県高岡市にて行われる伏木神社の春季例大祭',NULL,'Q11381052','伏木神社','Fushiki Shrine','富山県','chubu',NULL,NULL,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/%E4%BC%8F%E6%9C%A8%E6%9B%B3%E5%B1%B1%E7%A5%AD.jpg','https://ja.wikipedia.org/wiki/%E4%BC%8F%E6%9C%A8%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11371737','二百十日','Nihyakutōka','雑節のひとつ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%8C%E7%99%BE%E5%8D%81%E6%97%A5',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11396267','刈谷わんさか祭り','Kariya Wansaka Festival','愛知県刈谷市で開催されるイベント','event held in Kariya, Aichi, Japan','Q11396287','刈谷市総合運動公園',NULL,'愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%88%88%E8%B0%B7%E3%82%8F%E3%82%93%E3%81%95%E3%81%8B%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11402392','北海ソーラン祭り','Hokkai Soran Matsuri','日本の北海道の祭り',NULL,NULL,NULL,NULL,'北海道','hokkaido',43.188471862,140.794824782,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%8C%97%E6%B5%B7%E3%82%BD%E3%83%BC%E3%83%A9%E3%83%B3%E7%A5%AD%E3%82%8A',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11391547','八王子いちょう祭り','Hachioji Ginkgo Festival','東京都八王子市にて毎年秋に実施される祭',NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,1979,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%85%AB%E7%8E%8B%E5%AD%90%E3%81%84%E3%81%A1%E3%82%87%E3%81%86%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11378042','仙台短篇映画祭','Sendai Short Film Festival',NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',NULL,NULL,2001,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BB%99%E5%8F%B0%E7%9F%AD%E7%AF%87%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11381210','会津まつり','Aizu Clan Parade',NULL,NULL,'Q237699','会津若松市','Aizuwakamatsu','福島県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Shinmei-dori%20during%202006%20Aizu%20Autumn%20Festival.JPG','https://ja.wikipedia.org/wiki/%E4%BC%9A%E6%B4%A5%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11406993','半夏生','Crow-dipper sprouts','雑節のひとつ','The 30th of the 72 pentads, lasting from July 2–6.',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Saururus%20chinensis%20kz01.jpg','https://ja.wikipedia.org/wiki/%E5%8D%8A%E5%A4%8F%E7%94%9F',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11405696','千灯籠まつり',NULL,'長崎県佐世保市江迎町で行われる祭り',NULL,'Q328000','佐世保市','Sasebo','長崎県','kyushu',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Emukae%20sentoro.jpg','https://ja.wikipedia.org/wiki/%E5%8D%83%E7%81%AF%E7%B1%A0%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11395741','出町子供歌舞伎曳山祭','Tonami Children''s Kabuki Float Hall',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E5%87%BA%E7%94%BA%E5%AD%90%E4%BE%9B%E6%AD%8C%E8%88%9E%E4%BC%8E%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11396697','別府八湯温泉まつり','Beppu Hatto Onsen Festival',NULL,NULL,NULL,NULL,NULL,'大分県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%88%A5%E5%BA%9C%E5%85%AB%E6%B9%AF%E6%B8%A9%E6%B3%89%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11397240','前橋まつり','Maebashi Matsuri',NULL,NULL,NULL,NULL,NULL,'群馬県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%89%8D%E6%A9%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11397692','前田祇園山笠','Maeda Gion Yamakasa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%89%8D%E7%94%B0%E7%A5%87%E5%9C%92%E5%B1%B1%E7%AC%A0',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11374838','京都・嵐山花灯路','Arashiyama Hanatōro',NULL,'event in Japan','Q2859566','嵐山','Arashiyama','京都府','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Arashiyama%20Hanat%C5%8Dro%2C%20Nison-in%20%E5%B5%90%E5%B1%B1%E8%8A%B1%E7%81%AF%E8%B7%AF%E3%83%BB%E4%BA%8C%E5%B0%8A%E9%99%A2%20%E7%B4%85%E8%91%89%E3%81%A8%E6%9C%88%20DSCF5361.JPG','https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E3%83%BB%E5%B5%90%E5%B1%B1%E8%8A%B1%E7%81%AF%E8%B7%AF',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11371526','二島祇園',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%B3%B6%E7%A5%87%E5%9C%92',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11381874','住吉祭','Sumiyoshi Matsuri','大阪市の住吉大社で行われる祭礼','Shinto shrine in Osaka Prefecture, Japan','Q705949','住吉大社','Sumiyoshi Taisha','大阪府','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Sumiyoshi%20Matsuri%20%2804%29%20IMG%203224-2%2020140801.JPG','https://ja.wikipedia.org/wiki/%E4%BD%8F%E5%90%89%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11379632','伊根祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BC%8A%E6%A0%B9%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11381258','会津絵ろうそくまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BC%9A%E6%B4%A5%E7%B5%B5%E3%82%8D%E3%81%86%E3%81%9D%E3%81%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11382961','佐倉市民花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'千葉県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E4%BD%90%E5%80%89%E5%B8%82%E6%B0%91%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11390862','八屋祇園',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%85%AB%E5%B1%8B%E7%A5%87%E5%9C%92',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11381803','住吉の御田植','Otaue Shinto Service','大阪市住吉区の住吉大社に伝わる田楽','Shinto shrine in Sumiyoshi, Japan','Q127774932','住吉大社御田','Onda, Sumiyoshi Taisha','大阪府','kinki',34.61135,135.492453,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Sumiyoshi%20jinja%20Otaue.jpg','https://ja.wikipedia.org/wiki/%E4%BD%8F%E5%90%89%E3%81%AE%E5%BE%A1%E7%94%B0%E6%A4%8D',NULL,95,'drafted','## 概要

住吉の御田植神事（すみよしのおたうえしんじ）は、大阪市住吉区の住吉大社で毎年6月14日に執り行われる、五穀豊穣を祈願する伝統神事である。「住吉の御田植」として1979年に国の重要無形民俗文化財に指定されており、日本三大御田植神事のひとつに数えられる。

## 歴史

神功皇后が住吉大社を創建した際、長門国（現在の山口県）より植女（うえめ）を召して御田を植えさせたことが起源と伝えられ、約1800年の歴史を持つとされる。中世以降、住吉大社の重要な年中行事として継承され、室町時代の文献にもその様子が記されている。戦時中の中断を経て戦後復活し、現在まで途切れることなく執行されている。

## 見どころ

御田と呼ばれる神田で、稚児・植女・替植女（かえうえめ）・八乙女（やおとめ）など華やかな衣装を身につけた女性たちが、実際に早苗を植える所作を奉納する。田の中央では棚を組み、その上で住吉踊・田植踊・住吉武者行列・風流武者行事などが次々と披露され、田植えと芸能が一体となった荘厳かつ華麗な空間が現出する。植女の鮮やかな衣装と笠、武者行列の勇壮さの対比が見どころである。

## 開催情報

開催地は大阪市住吉区住吉2丁目の住吉大社御田。最寄駅は南海本線「住吉大社駅」徒歩約3分、または阪堺電車「住吉鳥居前駅」目の前。開催日は毎年6月14日、13時頃から約2時間。観覧は無料で、御田周囲の観覧スペースから自由に見学できるが、混雑するため早めの場所取りが望ましい。梅雨期のため雨具を携行すべきである。

## 周辺の見どころ

住吉大社は全国約2300社ある住吉神社の総本社で、海上交通・和歌・農耕の神として信仰を集める。境内の反橋（太鼓橋）は大社の象徴的存在で、神事の前後に参拝するとよい。周辺には大阪の下町情緒が残る商店街や、近隣に堺市の仁徳天皇陵古墳など世界遺産級の見どころも点在する。','## Overview

Sumiyoshi no Otaue Shinji (住吉の御田植神事) is a traditional Shinto ritual held annually on June 14 at Sumiyoshi Taisha Shrine in Sumiyoshi Ward, Osaka City. It prays for a bountiful rice harvest and was designated an Important Intangible Folk Cultural Property of Japan in 1979. It is counted among the three greatest rice-planting rituals in Japan.

## History

According to legend, the ritual originated when Empress Jingu, who founded Sumiyoshi Taisha, summoned planting maidens (uеme) from Nagato Province (present-day Yamaguchi Prefecture) to plant rice in the shrine''s sacred fields. With a history of approximately 1,800 years, it has been continued as one of Sumiyoshi Taisha''s most important annual events since the medieval period and is mentioned in Muromachi-era documents. After a wartime interruption, the ritual was revived and has been performed without interruption ever since.

## Highlights

In a sacred field called Onda, young girls (chigo), planting maidens (uеme), substitute maidens (kaeueme), and the eight virgin dancers (yaotome) — all dressed in elaborate costumes — perform the act of planting rice seedlings as an offering. A stage is constructed in the center of the field, where Sumiyoshi Odori dance, rice-planting dances, samurai processions, and furyu (elegant pageantry) performances unfold one after another, creating a solemn yet vibrant space where agriculture and performing arts converge. The contrast between the colorful costumes and broad hats of the planting maidens and the bold samurai processions is particularly striking.

## Event Information

The venue is the Onda sacred field at Sumiyoshi Taisha, 2-chome Sumiyoshi, Sumiyoshi Ward, Osaka City. The nearest stations are Sumiyoshi Taisha Station on the Nankai Main Line (about a 3-minute walk) or Sumiyoshi Toriimae Station on the Hankai Tramway (right in front of the shrine). The ritual is held annually on June 14, beginning around 1:00 PM and lasting about two hours. Admission is free, with viewing spaces around the field, but as it gets crowded, early arrival is recommended. Visitors should bring rain gear, as the ritual coincides with the rainy season.

## Nearby Attractions

Sumiyoshi Taisha is the head shrine of approximately 2,300 Sumiyoshi shrines across Japan and is revered as the deity of maritime safety, waka poetry, and agriculture. The Sorihashi (arched drum bridge) within the precincts is a symbol of the shrine and worth visiting before or after the ritual. The surrounding area retains the atmosphere of traditional Osaka downtown, and the nearby Mozu Tombs in Sakai City, including the Emperor Nintoku Tomb, are designated as UNESCO World Heritage sites.','sumiyoshi-no-otaue-shinji','sumiyoshi-no-otaue-shinji',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11401311','北國大花火川北大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%8C%97%E5%9C%8B%E5%A4%A7%E8%8A%B1%E7%81%AB%E5%B7%9D%E5%8C%97%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11408464','南越谷阿波踊り',NULL,NULL,NULL,NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8D%97%E8%B6%8A%E8%B0%B7%E9%98%BF%E6%B3%A2%E8%B8%8A%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11374839','京都・東山花灯路','Higashiyama Hanatouro',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Illuminated%20Yasakanoto%20Tower%20%28Hokanji%20Temple%29%202.jpg','https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E3%83%BB%E6%9D%B1%E5%B1%B1%E8%8A%B1%E7%81%AF%E8%B7%AF',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11405274','千代流','Chiyo-nagare','博多祇園山笠の運営における構成単位である流の一つ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8D%83%E4%BB%A3%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11377742','仙台クラシックフェスティバル','Sendai Classical Music Festival',NULL,'music festival in Japan','Q46747','仙台市','Sendai','宮城県','tohoku',NULL,NULL,2006,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BB%99%E5%8F%B0%E3%82%AF%E3%83%A9%E3%82%B7%E3%83%83%E3%82%AF%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11378915','伊勢えび祭','Ise Lobster Festival','三重県志摩市で開催される祭り',NULL,NULL,NULL,NULL,'三重県','kinki',NULL,NULL,1961,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Iseebi%20Festival%202011.jpg','https://ja.wikipedia.org/wiki/%E4%BC%8A%E5%8B%A2%E3%81%88%E3%81%B3%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11404742','十万石まつり','Jumangoku festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8D%81%E4%B8%87%E7%9F%B3%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11400927','北九州国際音楽祭','Kitakyushu International Music Festival','北九州市八幡東区の北九州市立響ホールを主会場として開催される音楽祭','music festival in Japan',NULL,NULL,NULL,'福岡県','kyushu',NULL,NULL,1988,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11375013','京都市民映画祭','Kyoto Citizen Film Festival','日本映画の映画祭',NULL,'Q34600','京都市','Kyoto','京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E5%B8%82%E6%B0%91%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11378916','伊勢まつり','Ise Matsuri','三重県伊勢市で開催される市民の祭',NULL,NULL,NULL,NULL,'三重県','kinki',NULL,NULL,1895,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BC%8A%E5%8B%A2%E3%81%8A%E3%81%8A%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11396691','別府アルゲリッチ音楽祭','MUSIC FESTIVAL Argerich''s Meeting Point in Beppu','日本の大分県別府市で開催される音楽祭',NULL,NULL,NULL,NULL,'大分県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%88%A5%E5%BA%9C%E3%82%A2%E3%83%AB%E3%82%B2%E3%83%AA%E3%83%83%E3%83%81%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11389545','全国花火競技大会 (秋田県大仙市)','All-Japan National Fireworks Competition','秋田県大仙市で開催される花火大会',NULL,'Q695920','大仙市','Daisen','秋田県','tohoku',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%85%A8%E5%9B%BD%E8%8A%B1%E7%81%AB%E7%AB%B6%E6%8A%80%E5%A4%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11396442','初午祭','Hatsuuma Festival','鹿児島県霧島市の鹿児島神宮で開催される祭り',NULL,'Q704695','鹿児島神宮','Kagoshima Jingū','鹿児島県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hatsu%20uma%20sai%2002.jpg','https://ja.wikipedia.org/wiki/%E5%88%9D%E5%8D%88%E7%A5%AD_(%E9%B9%BF%E5%85%90%E5%B3%B6%E7%A5%9E%E5%AE%AE)',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11381253','会津田島祇園祭','Aizu Tajima Gion Matsuri',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E4%BC%9A%E6%B4%A5%E7%94%B0%E5%B3%B6%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11408922','博多おくんち','Hakata Okunchi','福岡市博多区の櫛田神社で行われる秋の例祭','autumn festival held at Kushida Shrine in Hakata-ku, Fukuoka City','Q11284628','博多','Hakata','長崎県','kyushu',NULL,NULL,1953,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E5%8D%9A%E5%A4%9A%E3%81%8A%E3%81%8F%E3%82%93%E3%81%A1',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11356768','三田祭','Mita festival','慶應義塾大学の学園祭',NULL,'Q3317048','三田','Mita',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Mita%20Festival%2C%20Keio%20University%20-%20Nov%2025%2C%202007%20%281%29.jpg','https://ja.wikipedia.org/wiki/%E4%B8%89%E7%94%B0%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11366503','中津祇園','Nakatsu Gion',NULL,'festival in Nakatsu, Oita prefecture, Japan',NULL,NULL,NULL,'大分県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%AD%E6%B4%A5%E7%A5%87%E5%9C%92',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11366524','中洲流','Nakasu-nagare','博多祇園山笠の運営における構成単位である流の一つ',NULL,NULL,NULL,NULL,'福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%AD%E6%B4%B2%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11347707','ラ・フォル・ジュルネ TOKYO','La Folle Journée TOKYO','毎年ゴールデンウィーク頃に東京で行われているクラシック音楽を中心とした催し','classical music festival in Tokyo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%BB%E3%83%95%E3%82%A9%E3%83%AB%E3%83%BB%E3%82%B8%E3%83%A5%E3%83%AB%E3%83%8D_TOKYO',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280396','やつしろ全国花火競技大会',NULL,NULL,NULL,'Q1358183','球磨川','Kuma River','熊本県','kyushu',32.4876083,130.6267719,1988,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%82%84%E3%81%A4%E3%81%97%E3%82%8D%E5%85%A8%E5%9B%BD%E8%8A%B1%E7%81%AB%E7%AB%B6%E6%8A%80%E5%A4%A7%E4%BC%9A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11301198','ケベス祭','Kebesu Sai',NULL,NULL,'Q873572','国東市','Kunisaki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B1%E3%83%99%E3%82%B9%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11353501','七尾祇園祭','Nanao Gion Matsuri','石川県七尾市で開催される夏祭り',NULL,'Q11433686','大地主神社','Ōtokonushi Shrine','京都府','kinki',37.04312,136.96747,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E4%B8%83%E5%B0%BE%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11307448','シネリンピック!','Cinelympics!','日米同時刻開催型の映画祭',NULL,'Q11279143','みなとみらい','Minatomirai',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%8D%E3%83%AA%E3%83%B3%E3%83%94%E3%83%83%E3%82%AF!',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11360142','上越まつり','Jōetsu Matsuri',NULL,NULL,NULL,NULL,NULL,'新潟県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%8A%E8%B6%8A%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11338450','ホーランエンヤ','Hōran-en''ya','大分県豊後高田市で行われる祭事',NULL,'Q11536671','桂川','Katsura River','大分県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Horan-enya%20boat.jpg','https://ja.wikipedia.org/wiki/%E3%83%9B%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%A8%E3%83%B3%E3%83%A4_(%E5%A4%A7%E5%88%86%E7%9C%8C)',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11361495','下館祇園祭','Shimodate Gion Matsuri',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E4%B8%8B%E9%A4%A8%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11294189','カセ鳥','Kasedori','山形県上山市で毎年2月11日に行われる小正月の民俗行事','Little New Year folk festival held annually on 11 February in Kaminoyama, Yamagata, Japan',NULL,NULL,NULL,'山形県','tohoku',NULL,NULL,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Kasedori%202026%20Kaminoyama%2001.jpg','https://ja.wikipedia.org/wiki/%E3%82%AB%E3%82%BB%E9%B3%A5',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11333690','フランス映画祭 (横浜)','French International Film Festival',NULL,NULL,'Q38283','横浜市','Yokohama','神奈川県','kanto',NULL,NULL,1993,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%A9%E3%83%B3%E3%82%B9%E6%98%A0%E7%94%BB%E7%A5%AD_(%E6%97%A5%E6%9C%AC)',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11308232','ショートショートフィルムフェスティバル','Short Shorts Film Festival','短編映画を対象とした日本の映画祭','Japan film festival','Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%83%95%E3%82%A3%E3%83%AB%E3%83%A0%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11292979','オロチョンの火祭り','Orochon no Hi Matsuri',NULL,NULL,'Q305640','網走市','Abashiri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%AD%E3%83%81%E3%83%A7%E3%83%B3%E3%81%AE%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11281926','わらじ曳き','Waraji-biki','三重県志摩市の波切神社で行なわれる祭',NULL,'Q11555441','波切神社','Nakiri Shrine','三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%8F%E3%82%89%E3%81%98%E6%9B%B3%E3%81%8D',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11278988','みちのく国際ミステリー映画祭','Michinoku International Mystery Film Festival','かつて岩手県盛岡市で開催された映画祭',NULL,'Q200077','盛岡市','Morioka','岩手県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BF%E3%81%A1%E3%81%AE%E3%81%8F%E5%9B%BD%E9%9A%9B%E3%83%9F%E3%82%B9%E3%83%86%E3%83%AA%E3%83%BC%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280851','ゆふいんこども映画祭','Yufuin Children''s Film Festival','大分県由布市湯布院町で開催される映画祭',NULL,'Q990455','由布市','Yufu','大分県','kyushu',NULL,NULL,1998,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%86%E3%81%B5%E3%81%84%E3%82%93%E3%81%93%E3%81%A9%E3%82%82%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11338823','ボロ市','Boro-ichi',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%9C%E3%83%AD%E5%B8%82',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280856','ゆふいん文化・記録映画祭','Yufuin Culture and Record Film Festival','大分県由布市湯布院町で開催される映画祭',NULL,'Q990455','由布市','Yufu','大分県','kyushu',NULL,NULL,1998,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%86%E3%81%B5%E3%81%84%E3%82%93%E6%96%87%E5%8C%96%E3%83%BB%E8%A8%98%E9%8C%B2%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11370941','亀崎潮干祭','Kamezaki Shiohi Festival','愛知県半田市にある神前神社の祭礼',NULL,'Q17226214','神前神社','Kamisaki Shrine','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kamezakishiohi%20Festival2.jpg','https://ja.wikipedia.org/wiki/%E4%BA%80%E5%B4%8E%E6%BD%AE%E5%B9%B2%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11304313','サウンドコニファー229','Sound Conifer 229',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B5%E3%82%A6%E3%83%B3%E3%83%89%E3%82%B3%E3%83%8B%E3%83%95%E3%82%A1%E3%83%BC229',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280366','やっさ祭り','Yassa Festival','広島県三原市で開催される祭り',NULL,NULL,NULL,NULL,'広島県','chugoku',NULL,NULL,1976,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E3%82%84%E3%81%A3%E3%81%95%E7%A5%AD%E3%82%8A2.jpg','https://ja.wikipedia.org/wiki/%E3%82%84%E3%81%A3%E3%81%95%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11343535','メガロポリス歌謡祭',NULL,'かつての日本の音楽祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%AC%E3%83%AD%E3%83%9D%E3%83%AA%E3%82%B9%E6%AD%8C%E8%AC%A1%E7%A5%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11278969','みちのくYOSAKOIまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BF%E3%81%A1%E3%81%AE%E3%81%8FYOSAKOI%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11279155','みなと舞鶴ちゃったまつり',NULL,NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BF%E3%81%AA%E3%81%A8%E8%88%9E%E9%B6%B4%E3%81%A1%E3%82%83%E3%81%A3%E3%81%9F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280261','やぎの花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%82%84%E3%81%8E%E3%81%AE%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11284866','アマチュア無線の日',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%9E%E3%83%81%E3%83%A5%E3%82%A2%E7%84%A1%E7%B7%9A%E3%81%AE%E6%97%A5',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11305117','サマーフェスタ イン ひさい',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B9%85%E5%B1%85%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11370288','九州現代音楽祭',NULL,'九州・沖縄作曲家協会が主催する現代音楽祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B9%9D%E5%B7%9E%E7%8F%BE%E4%BB%A3%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11340066','マグマ (音楽イベント)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%9E%E3%82%B0%E3%83%9E_(%E9%9F%B3%E6%A5%BD%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88)',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11352731','一日市の盆踊','Hitoichi no Bon-odori','秋田県八郎潟町で行われる盆踊り',NULL,NULL,NULL,NULL,'秋田県','tohoku',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Hitoichi%20Bon-odori%20Festival%202017b.jpg','https://ja.wikipedia.org/wiki/%E4%B8%80%E6%97%A5%E5%B8%82%E3%81%AE%E7%9B%86%E8%B8%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280858','ゆふいん音楽祭','Yufuin Music Festival',NULL,'music festival in Japan','Q990455','由布市','Yufu','大分県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%86%E3%81%B5%E3%81%84%E3%82%93%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11355803','三条まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%89%E6%9D%A1%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11285021','アメッコ市','Odate Amekko-ichi','日本の秋田県大館市の小正月行事',NULL,NULL,NULL,NULL,'青森県','tohoku',40.270611111,140.558722222,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/AmekkoIchi.jpg','https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%A1%E3%83%83%E3%82%B3%E5%B8%82',NULL,95,'drafted','## 概要

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
','## Overview

The Odate Amekko-ichi (Odate Candy Fair) is a winter folk event with over 400 years of history, held annually on the second Saturday of February and the following Sunday along Omachi Hachiko Street in central Odate City, Akita Prefecture. Accompanied by the saying "those who eat candy on this day will not catch a cold," the festival has been beloved by local residents and tourists alike.

Dozens of stalls selling colorful candies line the street, while charms made by tying vibrant candies onto branches of Japanese dogwood (mizuki) decorate the venue, painting a vivid winter scene in the snow-covered Tohoku region. Unique features such as the Akita dog parade and the procession of Shirohige Okami (the White-Bearded Mountain God) further enhance the festival''s appeal.

## History and Origins

The Odate Amekko-ichi is said to have originated around 1588 (Tensho 16) and boasts approximately 400 years of history, making it one of the most prominent folk events in the Tohoku region. It is believed to have begun with the practice of attaching candies to reddish dogwood branches and offering them to deities in place of rice ears, rooted in agricultural beliefs praying for bountiful harvests and good health.

The local legend that "mountain gods descend from the surrounding peaks on the second Saturday of February to buy candies" has taken root in the community, and the procession of Shirohige Okami—a deity with a long white beard representing the mountain god—has been preserved as the festival''s core ritual. Originally held on a small scale as a local folk event, the festival expanded significantly from 1972 (Showa 47) when Omachi Hachiko Street became the venue, evolving into a modern festival open to tourists.

Odate is internationally known as the birthplace of the Akita dog breed, and since the Heisei era, the Akita dog parade has been incorporated into the festival, achieving nationwide recognition as a unique event blending traditional ritual with regional branding.

## Highlights

**Rows of Candy Stalls**
Dozens of candy stalls operated by local confectioners and traditional Japanese sweet artisans line Omachi Hachiko Street. Visitors can experience a rich candy culture featuring colorful traditional candies, creative modern variations, and dogwood-branch charms decorated with sweets—a feast for both eyes and palate.

**Procession of Shirohige Okami**
The procession of Shirohige Okami, reenacting the mountain god descending to buy candy, is the festival''s mystical highlight. The figure with a long white beard in traditional attire parading through the streets evokes the living presence of 400 years of belief.

**Akita Dog Parade**
A parade of Akita dogs—the breed originating from this region—walking the streets with their owners is another centerpiece of the festival. Highly popular among international visitors, it draws attention as a rare opportunity to interact with Akita dogs.

**Dogwood Decorations and Charms**
At the festival''s finale, large dogwood branches lavishly decorated with multicolored candies appear as oversized lucky charms. Visitors take these home as part of a tradition praying for a year of good health, making the festival''s communal prayers visible.

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
','odate-amekko-ichi','odate-amekko-ichi',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11368913','久世祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B9%85%E4%B8%96%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11344772','モントレー・ジャズフェスティバル・イン・能登','Monterey Jazz Festival in Noto','石川県七尾市で開催されるジャズ・フェスティバル',NULL,'Q11353471','七尾マリンパーク','Nanao Marine Park','石川県','chubu',NULL,NULL,1989,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%B3%E3%83%88%E3%83%AC%E3%83%BC%E3%83%BB%E3%82%B8%E3%83%A3%E3%82%BA%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB%E3%83%BB%E3%82%A4%E3%83%B3%E3%83%BB%E8%83%BD%E7%99%BB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11370928','亀岡祭',NULL,NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%80%E5%B2%A1%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11302490','コミックシティ','Comic City','赤ブーブー通信社が主催するオールジャンル・マンガ同人誌即売会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1988,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%9F%E3%83%83%E3%82%AF%E3%82%B7%E3%83%86%E3%82%A3',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11287660','インディーズムービー・フェスティバル','Indie Movie Festival','かつて日本で開催された自主映画の映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%BC%E3%82%BA%E3%83%A0%E3%83%BC%E3%83%93%E3%83%BC%E3%83%BB%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11293020','オンチ映画祭','Onchi Film Festival','東京都町田市で毎年開催される映画祭',NULL,'Q210628','町田市','Machida','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%B3%E3%83%81%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11362874','中之条ビエンナーレ','Nakanojo Biennnale',NULL,NULL,NULL,NULL,NULL,'群馬県','kanto',36.589893,138.84099,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%AD%E4%B9%8B%E6%9D%A1%E3%83%93%E3%82%A8%E3%83%B3%E3%83%8A%E3%83%BC%E3%83%AC',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11296436','ガンダーラ映画祭','Gandara Film Festival','短編ドキュメンタリーの自主上映イベント',NULL,'Q735384','下北沢','Shimokitazawa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%AC%E3%83%B3%E3%83%80%E3%83%BC%E3%83%A9%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280572','やや祭り','Yaya Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%84%E3%82%84%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11297936','キネコ国際映画祭','KINEKO International Children''s Film Festival','東京都で毎年11月上旬に開催される映画祭',NULL,'Q11371454','二子玉川','Futako-Tamagawa','東京都','kanto',NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E3%82%AD%E3%83%8D%E3%82%B3%E5%9B%BD%E9%9A%9B%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11360475','上野間の裸まいり','Kaminoma Hadaka Mairi','愛知県知多郡美浜町上野間地区で行われる裸祭り',NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%8A%E9%87%8E%E9%96%93%E3%81%AE%E8%A3%B8%E3%81%BE%E3%81%84%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11327037','ハワリンバヤル','Havriin Bayar','1998年より東京で毎年開催されるモンゴルのフェスティバル','Annual Mongolian Festival in Tokyo since 1998','Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,1998,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%AF%E3%83%AA%E3%83%B3%E3%83%90%E3%83%A4%E3%83%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11360688','下呂の田の神祭','Gero Ta-no-Kami Festival','岐阜県下呂市森の、森水無八幡神社に伝わる祭り',NULL,'Q11539924','森水無八幡神社','Mori Minashi Hachiman Shrine','岐阜県','chubu',35.807214,137.243953,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Gero%20no%20Ta%20no%20Kami%20Festival%2C%20Marching%20people.jpg','https://ja.wikipedia.org/wiki/%E4%B8%8B%E5%91%82%E3%81%AE%E7%94%B0%E3%81%AE%E7%A5%9E%E7%A5%AD',NULL,95,'drafted','## 概要

下呂の田の神祭（げろのたのかみまつり）は、岐阜県下呂市森地区の森水無八幡神社（もりみなしはちまんじんじゃ）で2月7日から14日にかけて執り行われる、五穀豊穣を祈願する古式神事である。「下呂の田の神祭」として1976年に国の重要無形民俗文化財に指定された、飛騨地方を代表する予祝（よしゅく）神事である。

## 歴史

起源は鎌倉時代から室町時代にさかのぼると伝えられ、約700年の歴史を持つ。古くは森水無八幡神社の祭礼として地域に根付き、田植えの所作を演じることで翌年の豊作を予祝してきた。江戸時代を通じて飛騨地方の代表的な神事として継承され、戦後の急速な近代化のなかでも地元の保存会が中心となって伝統を守り続けてきた。

## 見どころ

祭りの中心は、白塗りの化粧と独特の装束を身につけた「翁（おきな）」「巫女（みこ）」「鍬持ち（くわもち）」など、田植え作業を象徴する役柄の人々による所作である。彼らが拝殿で田起こしから田植え、収穫までの一連の農作業を厳かに演じ、神に翌年の豊作を願う。2月14日の本祭では夜を徹して神楽と田楽が奉納され、地域住民が篝火を囲んで参列する幻想的な光景が広がる。

## 開催情報

開催地は岐阜県下呂市森。最寄駅はJR高山本線「下呂駅」で、駅から徒歩約20分。開催期間は毎年2月7日から14日で、本祭は2月14日。冬季の山間部開催のため、防寒対策と積雪に備えた靴が必須である。観覧は無料で、神事中の撮影には一部制限があるため現地の指示に従う必要がある。

## 周辺の見どころ

下呂温泉は日本三名泉のひとつに数えられ、祭り観覧と合わせた湯治旅として人気が高い。下呂温泉合掌村では飛騨地方の合掌造り家屋を移築展示しており、農村文化を体感できる。冬季は周辺の濁河温泉や御嶽山麓のスキー場も楽しめる。','## Overview

Gero no Ta no Kami Matsuri (下呂の田の神祭) is an ancient Shinto ritual held from February 7 to 14 at Morimina shi Hachiman Shrine in the Mori district of Gero City, Gifu Prefecture. It prays for a bountiful harvest in the coming year and was designated an Important Intangible Folk Cultural Property of Japan in 1976. It is one of the most representative yoshuku (pre-celebratory) rituals in the Hida region.

## History

The festival is said to have originated in the Kamakura to Muromachi period, giving it a history of approximately 700 years. As a ritual of Morimina shi Hachiman Shrine, it has long been rooted in the local community, with participants performing the motions of rice planting to predict and pray for an abundant harvest. Despite the rapid modernization of postwar Japan, local preservation societies have continued to safeguard this tradition.

## Highlights

The central feature is a series of performances by villagers dressed as symbolic agricultural figures — the elder (okina), the shrine maiden (miko), and the hoe-bearer (kuwa-mochi) — wearing white facial makeup and distinctive costumes. On the hall of the shrine, they solemnly enact the full cycle of rice cultivation, from tilling the soil to planting and harvesting. The main festival on February 14 features overnight performances of kagura (sacred music) and dengaku (rice-field dance), with local residents gathered around bonfires in a fantastical scene.

## Event Information

The venue is Morimina shi Hachiman Shrine in Mori, Gero City, Gifu Prefecture. The nearest station is Gero Station on the JR Takayama Main Line, about a 20-minute walk away. The festival runs annually from February 7 to 14, with the main ritual on February 14. As it takes place in a mountainous region in winter, warm clothing and snow-ready footwear are essential. Admission is free, though photography may be restricted during certain rituals — visitors should follow on-site instructions.

## Nearby Attractions

Gero Onsen, ranked as one of Japan''s three most famous hot springs, makes the festival ideal for combining with a hot-spring retreat. The Gero Onsen Gassho Village preserves relocated thatched-roof farmhouses from the Hida region, offering a glimpse of rural culture. Nearby Nigorigo Onsen and ski resorts at the foot of Mount Ontake are also accessible in winter.','gero-no-ta-no-kami-matsuri','gero-no-ta-no-kami-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280345','やすらい祭','Yasurai Matsuri',NULL,NULL,'Q500955','今宮神社','Imamiya Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%84%E3%81%99%E3%82%89%E3%81%84%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11353495','七尾港まつり','Nanao Port Festival','石川県七尾市で開催される市民祭',NULL,'Q11353471','七尾マリンパーク','Nanao Marine Park','石川県','chubu',NULL,NULL,1940,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%83%E5%B0%BE%E6%B8%AF%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11367985','丸亀お城まつり','Marugame Castle Festival',NULL,NULL,'Q250658','丸亀城','Marugame Castle','香川県','shikoku',NULL,NULL,1950,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%B8%E4%BA%80%E3%81%8A%E5%9F%8E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11360316','上野天神祭','Ueno Tenjin Festival','三重県伊賀市の菅原神社で行なわれる秋祭り',NULL,'Q17218755','菅原神社','Sugawara Shrine','大阪府','kinki',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Iga%20City%20Danjiri%20Kaikan%20ac.jpg','https://ja.wikipedia.org/wiki/%E4%B8%8A%E9%87%8E%E5%A4%A9%E7%A5%9E%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11361280','下総三山の七年祭り','Shimōsa Miyama Seven-Year Festival','千葉県船橋市三山にある二宮神社を中心として開催される大祭',NULL,'Q11371511','二宮神社','Ninomiya Shrine','千葉県','kanto',NULL,NULL,1445,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Shimousamiyamanoshichinennmatsuri.jpg','https://ja.wikipedia.org/wiki/%E4%B8%8B%E7%B7%8F%E4%B8%89%E5%B1%B1%E3%81%AE%E4%B8%83%E5%B9%B4%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11353544','七日堂裸まいり','Nanokado Hadaka Mairi',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%83%E6%97%A5%E5%A0%82%E8%A3%B8%E3%81%BE%E3%81%84%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11302749','コリアン・シネマ・ウィーク','Korean Cinema Week','駐日韓国文化院主催の映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%AA%E3%82%A2%E3%83%B3%E3%83%BB%E3%82%B7%E3%83%8D%E3%83%9E%E3%83%BB%E3%82%A6%E3%82%A3%E3%83%BC%E3%82%AF',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11338451','ホーランエンヤ','Hōran-en''ya','島根県松江市で行われる船渡御祭',NULL,NULL,NULL,NULL,'島根県','chugoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Horanenya%20higashimatsue.jpg','https://ja.wikipedia.org/wiki/%E3%83%9B%E3%83%BC%E3%83%A9%E3%83%B3%E3%82%A8%E3%83%B3%E3%83%A4_(%E5%B3%B6%E6%A0%B9%E7%9C%8C)',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11280528','やまなし映画祭','Yamanashi Film Festival','山梨県で行われていた映画祭',NULL,NULL,NULL,NULL,'山梨県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%84%E3%81%BE%E3%81%AA%E3%81%97%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11432381','大依羅神社','Ōyosami Shrine','大阪市にある神社','Shinto shrine in Osaka Prefecture, Japan',NULL,NULL,NULL,'大阪府','kinki',34.594833,135.518163,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Oyosami-jinja%2C%20haiden.jpg','https://ja.wikipedia.org/wiki/%E5%A4%A7%E4%BE%9D%E7%BE%85%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

大依羅神社（おおよさみじんじゃ）は、大阪市住吉区庭井に鎮座する古社で、延喜式神名帳に「摂津国住吉郡 大依羅神社 名神大 月次新嘗」と記される名神大社である。摂津国の有力古社のひとつとして、古来より地域の信仰を集めてきた。例祭は毎年10月17日に執り行われる。

## 歴史

創建は崇神天皇の御代と伝えられ、約2,000年の歴史を持つとされる。古代この一帯は「依網池（よさみのいけ）」と呼ばれる広大な灌漑池が広がり、依網氏（よさみうじ）と呼ばれる豪族が祭祀を司った。延喜式神名帳（927年成立）では摂津国住吉郡に列せられる名神大社として記載され、住吉大社と並ぶ格式を誇った。中世以降、依網池の干拓と都市化に伴い社地は縮小したが、地元住民の崇敬は途絶えることなく明治期の郷社、戦後の府社へと格式を保ってきた。

## 見どころ

主祭神は建豊波豆羅和気命（たけとよはずらわけのみこと）ほか五柱で、農耕と水利の神として古来より厚く崇敬されてきた。境内には依網池の名残を伝える池や、古代祭祀遺跡を示す石碑が点在し、住吉信仰圏における歴史的位置づけを実感できる。10月の例祭では神輿渡御と地車（だんじり）の曳行が行われ、住吉区南部の秋祭りとして地域を盛り上げる。

## 開催情報

所在地は大阪府大阪市住吉区庭井2丁目18-16。最寄駅はOsaka Metro御堂筋線「あびこ駅」徒歩約12分、またはJR阪和線「我孫子町駅」徒歩約15分。例祭は毎年10月17日。境内参拝は終日無料。だんじり曳行のある祭礼当日は周辺道路が一部交通規制されるため、公共交通機関の利用が推奨される。

## 周辺の見どころ

住吉大社（全国住吉神社の総本社）まで約3km圏内で、住吉信仰の地域史を巡る歴史散策に最適である。隣接する大依羅神社御旅所、住吉区の長居公園や大阪市立自然史博物館も徒歩・自転車圏内。あびこ駅周辺には大阪らしい商店街と下町の食文化が残っており、参拝後の街歩きも楽しめる。','## Overview

Ōyosami Shrine (大依羅神社) is an ancient shrine located in Niwai, Sumiyoshi Ward, Osaka City. Listed in the Engishiki Jinmyōchō (a 10th-century register of shrines) as a Myōjin Taisha — one of the highest-ranking shrine designations in ancient Japan — it has long been a major center of worship in Settsu Province. Its annual main festival is held every October 17.

## History

The shrine is said to have been founded during the reign of Emperor Sujin, giving it a history of approximately 2,000 years. The surrounding area was once home to Yosami Pond, a vast irrigation reservoir, and was governed by the Yosami clan, who served as the shrine''s hereditary priests. The Engishiki Jinmyōchō (compiled in 927) records the shrine as a Myōjin Taisha of Sumiyoshi District in Settsu Province, ranking alongside the famous Sumiyoshi Taisha. Although the shrine grounds were reduced over the medieval period as Yosami Pond was reclaimed and the area urbanized, local devotion remained strong, and the shrine was designated as a gōsha (district shrine) in the Meiji era and later as a fusha (prefectural shrine) after World War II.

## Highlights

The principal deity is Take-Toyohazu-rawake-no-Mikoto, along with five other kami, all venerated as deities of agriculture and water management. Stone monuments within the precincts mark the location of ancient ritual sites and remnants of the former Yosami Pond, offering visitors a tangible sense of the shrine''s place in the broader Sumiyoshi belief system. At the October main festival, mikoshi (portable shrines) and danjiri (wooden festival floats) are paraded through the streets, enlivening the autumn festivities of southern Sumiyoshi Ward.

## Event Information

The shrine is located at 2-18-16 Niwai, Sumiyoshi Ward, Osaka City. The nearest stations are Abiko Station on the Osaka Metro Midōsuji Line (about a 12-minute walk) and Abikochō Station on the JR Hanwa Line (about a 15-minute walk). The main annual festival is held on October 17. Admission to the shrine grounds is free year-round. On festival days, surrounding streets may be partially closed for the danjiri procession, so visitors are encouraged to use public transportation.

## Nearby Attractions

Sumiyoshi Taisha, the head shrine of all Sumiyoshi shrines in Japan, is located within approximately 3 km, making it ideal for a historical walking route exploring the heritage of Sumiyoshi worship. Nagai Park and the Osaka Museum of Natural History are also within walking or cycling distance. The area around Abiko Station preserves the atmosphere of traditional Osaka downtown shopping streets and culinary culture, perfect for exploring after a shrine visit.','oyosami-jinja','oyosami-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11431754','大つけ麺博','Grand Tsukemen Festival',NULL,NULL,'Q1378533','日比谷公園','Hibiya Park',NULL,NULL,NULL,NULL,2009,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E3%81%A4%E3%81%91%E9%BA%BA%E5%8D%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11414700','名のり・注連縄切り・火祭り','Nanori, Shimenawa-kiri, and Fire Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%90%8D%E3%81%AE%E3%82%8A%E3%83%BB%E6%B3%A8%E9%80%A3%E7%B8%84%E5%88%87%E3%82%8A%E3%83%BB%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11434756','大岡越前祭','Ōoka Echizen Festival','神奈川県茅ヶ崎市で行われる祭り',NULL,'Q11556886','浄見寺','Jōken-ji Temple','福井県','chubu',NULL,NULL,1912,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%B2%A1%E8%B6%8A%E5%89%8D%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11424684','地蔵盆','Jizobon','地蔵菩薩の縁日',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9C%B0%E8%94%B5%E7%9B%86',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11413521','吉田の火祭','Yoshida Fire Festival','山梨県富士吉田市で行われる祭り',NULL,'Q11401286','北口本宮冨士浅間神社','Kitaguchi Hongū Fuji Sengen Shrine','山梨県','chubu',35.478194,138.794139,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Torches%20burning%20Yoshida%20Fire%20Festival%20A.JPG','https://ja.wikipedia.org/wiki/%E5%90%89%E7%94%B0%E3%81%AE%E7%81%AB%E7%A5%AD',NULL,95,'drafted','## 概要

吉田の火祭（よしだのひまつり）は、山梨県富士吉田市の北口本宮冨士浅間神社および諏訪神社で毎年8月26日・27日に執り行われる、富士山の夏山閉山を告げる神事である。「吉田の火祭」として2012年に国の重要無形民俗文化財に指定され、日本三奇祭のひとつとされている。

## 歴史

起源は明確ではないが、富士山信仰と深く結びついた神事として平安時代末期から鎌倉時代にかけて成立したと考えられている。富士山は古来より霊峰として崇められ、夏季の限られた期間のみ登拝が許される神聖な山であった。閉山時期である8月末に大松明を焚き、夏山の終わりと安全な下山を感謝するとともに、火によって罪穢れを浄める意味が込められている。

## 見どころ

26日の「鎮火祭」では、夕刻に高さ約3メートル、直径約90センチの大松明70本以上が市内本町通りに立て並べられ、一斉に点火される。炎の柱が立ち上り、街全体が赤く染まる光景は圧巻である。各家の前にも井桁状の松明が組まれ、街路全体が火の道となる。27日の「すすき祭り」では、薄の玉串を持った氏子たちが諏訪神社の神輿を担いで還御する。富士山を背景にした火と山岳信仰の融合は、他にない神秘性を放つ。

## 開催情報

開催地は山梨県富士吉田市上吉田の北口本宮冨士浅間神社および諏訪神社、本町通り。最寄駅は富士急行線「富士山駅」徒歩約5分。開催日は毎年8月26日（鎮火祭）と27日（すすき祭り）。大松明の点火は26日18時30分頃から。観覧は無料だが、本町通りは夕刻から大変混雑するため早めの到着を推奨する。火を扱う祭りのため、燃えやすい服装は避け、安全な距離を保つこと。

## 周辺の見どころ

富士吉田市は富士山北麓に位置し、世界文化遺産「富士山」の構成資産である北口本宮冨士浅間神社は祭りの中心舞台である。富士急ハイランドや富士五湖（山中湖・河口湖など）も至近で、夏季の富士山観光と合わせて訪れる旅程が組みやすい。市内の吉田うどんは地元名物として知られ、祭り前後の食事におすすめである。','## Overview

Yoshida no Himatsuri (吉田の火祭) is a sacred fire festival held annually on August 26 and 27 at Kitaguchi Hongu Fuji Sengen Shrine and Suwa Shrine in Fujiyoshida City, Yamanashi Prefecture. It marks the closing of the summer climbing season on Mount Fuji and was designated an Important Intangible Folk Cultural Property of Japan in 2012. It is considered one of Japan''s three most unusual festivals (Nihon san-kisai).

## History

While its precise origins are unclear, the festival is believed to have taken shape between the late Heian and Kamakura periods as a ritual deeply tied to Mount Fuji worship. Mount Fuji has been revered as a sacred mountain since ancient times, with pilgrim ascents permitted only during a brief summer window. Held at the end of August to mark the close of the climbing season, the festival lights enormous torches to express gratitude for safe descents and to purify impurities through the cleansing power of fire.

## Highlights

On August 26, during the Chinka-sai (fire-pacifying festival), over 70 massive torches — each about 3 meters tall and 90 cm in diameter — are erected along Honcho-dori in central Fujiyoshida and lit simultaneously in the evening. Pillars of flame rise into the sky, bathing the entire town in red — a spectacle of remarkable scale. Each household also constructs lattice-shaped torches in front of their homes, transforming the streets into a corridor of fire. On August 27, during the Susuki Matsuri (pampas grass festival), parishioners bearing pampas-grass tamagushi offerings carry the Suwa Shrine portable shrine back to its resting place. The fusion of fire and mountain worship, with Mount Fuji as a backdrop, projects a mystique found nowhere else.

## Event Information

The venues are Kitaguchi Hongu Fuji Sengen Shrine, Suwa Shrine, and Honcho-dori in Kamiyoshida, Fujiyoshida City, Yamanashi Prefecture. The nearest station is Fujisan Station on the Fujikyu Railway, about a 5-minute walk away. The festival is held annually on August 26 (Chinka-sai) and August 27 (Susuki Matsuri), with the lighting of the great torches beginning around 6:30 PM on August 26. Admission is free, but Honcho-dori becomes extremely crowded from early evening, so arriving early is recommended. As this is a fire festival, avoid flammable clothing and maintain a safe distance from the flames.

## Nearby Attractions

Fujiyoshida City sits at the northern foot of Mount Fuji, and Kitaguchi Hongu Fuji Sengen Shrine — the central stage of the festival — is a component asset of the UNESCO World Heritage Site "Fujisan." Fuji-Q Highland amusement park and the Fuji Five Lakes (including Lake Yamanaka and Lake Kawaguchi) are also nearby, making it easy to combine the festival with summer sightseeing around Mount Fuji. The local specialty Yoshida udon is a recommended meal before or after the festival.','yoshida-no-himatsuri','yoshida-no-himatsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11425954','城下町新発田ふるさとまつり',NULL,NULL,NULL,NULL,NULL,NULL,'新潟県','chubu',38.002293,139.37245,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9F%8E%E4%B8%8B%E7%94%BA%E6%96%B0%E7%99%BA%E7%94%B0%E3%81%B5%E3%82%8B%E3%81%95%E3%81%A8%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11416021','向田の火祭り','Kōda no Himatsuri','石川県七尾市の伊夜比咩神社の火祭り',NULL,'Q11612025','能登島','Notojima','石川県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%90%91%E7%94%B0%E3%81%AE%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11412652','吉備津彦神社の御田植祭',NULL,NULL,NULL,'Q500763','吉備津彦神社','Kibitsuhiko Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%90%89%E5%82%99%E6%B4%A5%E5%BD%A6%E7%A5%9E%E7%A4%BE%E3%81%AE%E5%BE%A1%E7%94%B0%E6%A4%8D%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11433804','大垣祭','Ōgaki Festival','岐阜県大垣市で行われる大垣八幡神社の例祭',NULL,'Q11433764','大垣八幡神社','Ōgaki Hachiman Shrine','岐阜県','chubu',NULL,NULL,1648,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%A4%A7%E5%9E%A3%E5%B8%82%28%E5%A4%A7%E5%9E%A3%E3%81%BE%E3%81%A4%E3%82%8A%29%20-%20panoramio.jpg','https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%9E%A3%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11426255','城端曳山祭','Johana Hikiyama Festival','富山県南砺市にて行われる城端神明宮の春季祭礼',NULL,NULL,NULL,NULL,'富山県','chubu',NULL,NULL,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/%E5%9F%8E%E7%AB%AF%E7%94%BA%20%E6%9B%B3%E5%B1%B1%E7%A5%AD%E3%82%8A%20SLKY20180505%200000057.jpg','https://ja.wikipedia.org/wiki/%E5%9F%8E%E7%AB%AF%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11423732','土浦全国花火競技大会','Tsuchiura All Japan Fireworks Competition','茨城県土浦市で開催される花火大会',NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%9C%9F%E6%B5%A6%E5%85%A8%E5%9B%BD%E8%8A%B1%E7%81%AB%E7%AB%B6%E6%8A%80%E5%A4%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11411179','古川祭','Furukawa Festival','岐阜県飛騨市で開催される気多若宮神社の例祭',NULL,'Q3195586','気多若宮神社','Keta Wakamiya Shrine','岐阜県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Furukawa-yatai.jpg','https://ja.wikipedia.org/wiki/%E5%8F%A4%E5%B7%9D%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11412682','吉原の万灯籠',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%90%89%E5%8E%9F%E3%81%AE%E4%B8%87%E7%81%AF%E7%B1%A0',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11419969','四日市祭',NULL,NULL,NULL,NULL,NULL,NULL,'三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9B%9B%E6%97%A5%E5%B8%82%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11425142','坂戸よさこい',NULL,NULL,NULL,NULL,NULL,NULL,'高知県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9D%82%E6%88%B8%E3%82%88%E3%81%95%E3%81%93%E3%81%84',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11426080','城屋の揚松明',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9F%8E%E5%B1%8B%E3%81%AE%E6%8F%9A%E6%9D%BE%E6%98%8E',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11428318','堺祭',NULL,NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A0%BA%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11428944','塩野毘沙門堂祭礼',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A1%A9%E9%87%8E%E6%AF%98%E6%B2%99%E9%96%80%E5%A0%82%E7%A5%AD%E7%A4%BC',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11432637','大分七夕まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%88%86%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11412729','吉原祇園祭','Yoshiwara Gion-sai','静岡県富士市の吉原地区で毎年6月第二土曜日・日曜日に開催される祭り。','festival in Fuji city, Japan',NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Dashi.jpg','https://ja.wikipedia.org/wiki/%E5%90%89%E5%8E%9F%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11408956','博多松囃子','Hakata Matsubayashi',NULL,NULL,NULL,NULL,NULL,'福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Matsubayashi05.jpg','https://ja.wikipedia.org/wiki/%E5%8D%9A%E5%A4%9A%E6%9D%BE%E5%9B%83%E5%AD%90',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11433065','大前神社','Ōsaki Shrine','栃木県真岡市の神社','Shinto shrine in Tochigi Prefecture, Japan',NULL,NULL,NULL,'栃木県','kanto',36.449393,140.026004,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E8%B6%B3%E5%B0%BE%E5%B1%B1%E7%A5%9E%E7%A4%BE.jpg','https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%89%8D%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

大前神社（おおさきじんじゃ）は、栃木県真岡市東郷に鎮座する古社で、関東地方屈指の古社のひとつである。下野国延喜式内社で、主祭神は大物主大神（おおものぬしのおおかみ）と事代主大神（ことしろぬしのおおかみ）。「恵比寿様の総本宮」「日本一の大前恵比寿神社」を擁することで知られ、商売繁盛・縁結びの神として広く信仰を集めている。

## 歴史

創建は約1,500年前、第27代安閑天皇の御代と伝えられる。延喜式神名帳（927年成立）には下野国芳賀郡11座のひとつ「大前神社」として記載される式内社で、古代より下野国の有力神社として崇敬されてきた。中世以降、武家からも厚く信仰され、戦国時代には宇都宮氏、江戸時代には徳川幕府の祈願所として保護を受けた。社殿は1707年に再建されたもので、栃木県有形文化財に指定されている。

## 見どころ

最大の見どころは、境内に隣接する「大前恵比寿神社」の高さ約20メートルの黄金の恵比寿像である。日本一の大きさを誇り、商売繁盛・金運の象徴として全国から参拝者が訪れる。本殿（県指定文化財）は江戸時代中期の壮麗な彫刻が施され、龍・獅子・鳳凰など極彩色の意匠が見事である。例大祭は毎年4月の第3日曜日に執り行われ、神輿渡御と稚児行列が華やかに繰り広げられる。

## 開催情報

所在地は栃木県真岡市東郷937。最寄駅は真岡鐵道「北真岡駅」徒歩約20分、または車利用が一般的（北関東自動車道「真岡IC」より約10分）。参拝は終日可能で授与所は9:00〜16:00。例大祭は毎年4月第3日曜日。恵比寿祭は毎月20日に開催され、商売繁盛祈願の参拝者で賑わう。駐車場は約100台分完備。

## 周辺の見どころ

真岡市は「真岡木綿」の産地として知られ、市内には真岡木綿会館がある。SLが走る真岡鐵道は撮影名所として人気。芳賀地方の里山風景や、真岡井頭温泉、芳賀ロマンの湯など温泉施設も近隣に点在する。栃木県の郷土料理「しもつかれ」やいちごの産地でもあり、季節の味覚も楽しめる。','## Overview

Ōsaki Shrine (大前神社) is an ancient shrine located in Tōgō, Mōka City, Tochigi Prefecture. One of the most venerable shrines in the Kantō region, it is listed in the Engishiki Jinmyōchō as a shikinaisha (officially registered shrine of the early 10th century) of Shimotsuke Province. Its principal deities are Ōmononushi-no-Ōkami and Kotoshironushi-no-Ōkami. The shrine is famous for hosting Japan''s largest Ebisu statue, attracting worshippers seeking blessings for business prosperity and good fortune.

## History

The shrine is said to have been founded approximately 1,500 years ago during the reign of Emperor Ankan, the 27th emperor of Japan. It appears in the Engishiki Jinmyōchō (compiled in 927) as one of the eleven officially recognized shrines of Haga District in Shimotsuke Province, indicating its prominence in ancient times. From the medieval period onward, the shrine received the devotion of warrior families, including the Utsunomiya clan during the Sengoku period and the Tokugawa shogunate during the Edo period. The present main hall, rebuilt in 1707, is designated as a Tangible Cultural Property of Tochigi Prefecture.

## Highlights

The shrine''s most striking feature is the towering 20-meter golden Ebisu statue at the adjacent Ōsaki Ebisu Shrine — the largest of its kind in Japan and a powerful symbol of business success and prosperity. The main hall (a prefectural cultural property) showcases elaborate Edo-period carvings featuring dragons, lions, and phoenixes in vivid polychrome. The main annual festival, held on the third Sunday of April, features a mikoshi procession and a parade of children in traditional attire. The Ebisu Festival on the 20th of each month also draws large crowds praying for commercial success.

## Event Information

The shrine is located at 937 Tōgō, Mōka City, Tochigi Prefecture. The nearest station is Kitamōka Station on the Mōka Railway (about a 20-minute walk), though many visitors arrive by car (approximately 10 minutes from Mōka IC on the Kita-Kantō Expressway). The shrine grounds are open at all hours; the prayer office is open from 9:00 AM to 4:00 PM. The main festival is held on the third Sunday of April, and the monthly Ebisu Festival takes place on the 20th of each month. Free parking for approximately 100 vehicles is available.

## Nearby Attractions

Mōka City is known as a center for Mōka cotton production, and visitors can learn about this tradition at the Mōka Cotton Hall. The Mōka Railway, which still operates steam locomotives, is a popular destination for railway enthusiasts and photographers. The surrounding countryside features traditional rural landscapes, and nearby hot-spring facilities include Mōka Igashira Onsen and Haga Roman no Yu. The region is also famous for shimotsukare (a traditional Tochigi dish) and for being one of Japan''s top strawberry-producing areas, offering seasonal culinary delights.','osaki-jinja','osaki-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11431301','夜梅祭','Night Plum Festival','茨城県水戸市の偕楽園・常磐神社で行われるイベント',NULL,'Q71952','偕楽園','Kairaku-en','茨城県','kanto',NULL,NULL,2006,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/The%20finale%20of%20the%20night%20ume%20flowers%20festival%20%28Kairaku-en%20Garden%20.2019%29%20in%20Mito%2C%20Ibaraki.jpg','https://ja.wikipedia.org/wiki/%E5%A4%9C%E6%A2%85%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11420919','国府祭','Kokufu-sai','神奈川県大磯町で行われる相模国の国府祭',NULL,NULL,NULL,NULL,'神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9B%BD%E5%BA%9C%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11423189','土居流','Doi-nagare','博多祇園山笠の運営における構成単位である流の一つ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9C%9F%E5%B1%85%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11433116','大原はだか祭り','Ohara Hadaka Matsuri','千葉県いすみ市（旧大原町）で、毎年9月23日、24日に行われる祭礼',NULL,NULL,NULL,NULL,'千葉県','kanto',NULL,NULL,NULL,NULL,'winter',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%8E%9F%E3%81%AF%E3%81%A0%E3%81%8B%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11419692','四国三大祭り','Three Great Festivals of Shikoku','阿波踊り、よさこい祭り、新居浜太鼓祭りの総称',NULL,'Q60213044','四国地方','Shikoku Region',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9B%9B%E5%9B%BD%E4%B8%89%E5%A4%A7%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11414198','吉祥寺秋まつり','Kichijoji Autumn Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%90%89%E7%A5%A5%E5%AF%BA%E7%A7%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11414802','名古屋まつり','Nagoya Festival',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%90%8D%E5%8F%A4%E5%B1%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11417760','和泉だんじり祭',NULL,NULL,NULL,'Q696412','和泉市','Izumi',NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E5%92%8C%E6%B3%89%E3%81%A0%E3%82%93%E3%81%98%E3%82%8A%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q121294996','狛江・多摩川花火大会','Komae Tamagawa Fireworks Festival','狛江市で開催される花火大会','Fireworks show in Japan','Q121295034','多摩川緑地公園',NULL,'神奈川県','kanto',35.623,139.572,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%8B%9B%E6%B1%9F%E3%83%BB%E5%A4%9A%E6%91%A9%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q124570404','旭岡山神社の梵天奉納祭',NULL,'秋田県横手市の祭事',NULL,NULL,NULL,NULL,'秋田県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Yokote%27s%20Bonden%20at%20Kajimachi%20202402.jpg',NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q119478096','近代麻雀水着祭','Kindai Mahjong Swimsuit Festival',NULL,'swimsuit festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kindai%20Mahjong%20Swimsuit%20Festival%20%28April%2029%2C%202024%29051961.jpg','https://ja.wikipedia.org/wiki/%E8%BF%91%E4%BB%A3%E9%BA%BB%E9%9B%80%E6%B0%B4%E7%9D%80%E7%A5%AD',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q120885738','岩瀬駅前夏祭り',NULL,'茨城県桜川市の岩瀬市街地で行われる祭り','summer festival in Iwase, Sakuragawa, Ibaraki','Q116950442','岩瀬','Iwase','茨城県','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/DSC%20%E5%B2%A9%E7%80%AC%E9%A7%85%E5%89%8D%E5%A4%8F%E7%A5%AD%E3%82%8A%E8%8F%AF%E5%90%88%E3%82%8F%E3%81%9B2.jpg','https://ja.wikipedia.org/wiki/%E5%B2%A9%E7%80%AC%E9%A7%85%E5%89%8D%E5%A4%8F%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q115909474',NULL,'Green Image Film Festival',NULL,'environmental film festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q124363255','山留め','Yamadome','博多祇園山笠における山笠の出発地点','starting point for floats at Hakata Gion Yamakasa','Q123499905','福岡市道店屋町318号線','Tenyamachi 318th Street','福岡県','kyushu',33.593427777,130.4109,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kushida%20Shrine%20the%20stone%20singn%20marking%20the%20starting%20poit%20for%20floats%20at%20Hakata%20Gion%20Yamakasa%201-41%20Kami-kawabatamachi%20Hakata-ku%20Fukuoka%2020231204.jpg',NULL,NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q121646023','JAMAICA FESTIVAL レゲエ＆キュイジーヌ','Jamaica Festival Reggae & Cuisine in Tokyo',NULL,NULL,'Q1204253','代々木公園','Yoyogi Park',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q122353106','大湯祭','Daitōsai',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%B9%AF%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q117006841','POP YOURS','POP YOURS','日本のヒップホップフェスティバル','Japanese hip hop festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2022,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/POP_YOURS',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q116056816','2027年国際園芸博覧会','International Horticultural Expo 2027','2027年に神奈川県横浜市で開催予定の国際園芸博覧会','International Horticultural Expo in Yokohama, Japan','Q4420137','上瀬谷通信施設','Naval Support Facility Kamiseya','神奈川県','kanto',35.486388888,139.490277777,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Expo%202027.svg','https://ja.wikipedia.org/wiki/2027%E5%B9%B4%E5%9B%BD%E9%9A%9B%E5%9C%92%E8%8A%B8%E5%8D%9A%E8%A6%A7%E4%BC%9A',NULL,95,'drafted','## 概要

2027年国際園芸博覧会（GREEN×EXPO 2027）は、神奈川県横浜市旭区・瀬谷区の上瀬谷通信施設跡地で2027年3月19日から9月26日まで開催予定の国際園芸博覧会である。国際園芸家協会（AIPH）認定のA1クラス（最高位）に位置付けられ、テーマは「幸せを創る明日の風景」。日本では1990年の大阪「花の万博」以来37年ぶりの国際園芸博覧会となる。

## 歴史

会場となる上瀬谷地区は戦後長らく米軍通信施設として使用され、2015年に返還された242ヘクタールの広大な土地である。返還跡地の活用策として横浜市が国際園芸博覧会の招致を進め、2017年にAIPH承認、2020年にBIE（博覧会国際事務局）承認を取得した。コロナ禍を経て、2024年に正式名称「GREEN×EXPO 2027」が決定し、準備が本格化している。

## 見どころ

園芸・農業・環境技術を融合した最先端の屋外展示が中心で、世界各国のガーデンデザイン、日本古来の園芸文化、SDGsやカーボンニュートラルに対応する次世代農業技術が一堂に集まる。会期中は約1,500万人の来場が見込まれ、夜間ライトアップやドローンショーなど演出も計画されている。

## 開催情報・アクセス

会場は神奈川県横浜市旭区・瀬谷区の上瀬谷通信施設跡地（約80ヘクタール使用）。最寄駅は相鉄線瀬谷駅で、シャトルバスや臨時鉄道アクセスが整備される予定。会期は2027年3月19日〜9月26日の192日間。

## 周辺観光

横浜市内には横浜赤レンガ倉庫、みなとみらい21、横浜中華街など定番観光地が揃い、博覧会と組み合わせた周遊観光が想定される。近隣の瀬谷区・旭区は里山風景が残り、農業体験施設や四季の森公園など自然観光も楽しめる。','## Overview

The International Horticultural Expo 2027 (GREEN×EXPO 2027) is an international horticultural exposition scheduled to be held from March 19 to September 26, 2027, on the former Kamiseya Communications Facility site spanning Asahi Ward and Seya Ward in Yokohama City, Kanagawa Prefecture. Recognized by the International Association of Horticultural Producers (AIPH) as an A1-class event (the highest rank), the expo carries the theme "Scenery of the Future for Happiness." It marks Japan''s first international horticultural exposition in 37 years since the 1990 "Flower Expo" in Osaka.

## History

The Kamiseya district that will serve as the venue was used as a United States military communications facility for many decades after World War II, with the 242-hectare expanse returned to Japan in 2015. Yokohama City pursued the hosting of an international horticultural exposition as a strategy for utilizing the returned land. The city secured AIPH approval in 2017 and recognition from the Bureau International des Expositions (BIE) in 2020. After delays related to the COVID-19 pandemic, the official name "GREEN×EXPO 2027" was finalized in 2024, and preparations entered their main phase.

## Highlights

The expo will feature cutting-edge outdoor displays integrating horticulture, agriculture, and environmental technologies, bringing together garden designs from countries worldwide, traditional Japanese horticultural culture, and next-generation agricultural technologies responding to the SDGs and carbon neutrality goals. Approximately 15 million visitors are expected during the run, and elaborate evening illuminations and drone shows are being planned to provide spectacular nighttime entertainment.

## Event Details and Access

The venue occupies approximately 80 hectares of the former Kamiseya Communications Facility site straddling Asahi Ward and Seya Ward in Yokohama City, Kanagawa Prefecture. The nearest station is Seya Station on the Sōtetsu Line, with shuttle bus services and temporary rail access infrastructure being developed for the event. The exposition runs for 192 days from March 19 to September 26, 2027.

## Surrounding Attractions

Yokohama City offers a wealth of established tourist attractions including the Yokohama Red Brick Warehouse, Minato Mirai 21 district, and Yokohama Chinatown, allowing visitors to combine the expo with broader sightseeing tours. The neighboring Seya and Asahi wards preserve traditional satoyama countryside landscapes, with agricultural experience facilities and Shiki no Mori Park offering additional nature-focused attractions to complement the horticultural theme of the expo itself.','international-horticultural-expo-2027','international-horticultural-expo-2027',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q117084954','パンムジーク・フェスティバル東京',NULL,'日本で開催された現代音楽の音楽祭',NULL,'Q3892342','東京文化会館','Tokyo Bunka Kaikan','東京都','kanto',NULL,NULL,1976,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%B3%E3%83%A0%E3%82%B8%E3%83%BC%E3%82%AF%E3%83%BB%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB%E6%9D%B1%E4%BA%AC',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q123698819','紅葉八幡宮獅子まつり','Momiji Hachiman-gū Shishi Matsuri','福岡市文化財保護条例に基づき無形民俗文化財に登録された祭り',NULL,'Q110915527','高取','Takatori',NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q124751043','土祭','Hijisai','日本の栃木県益子町で行われている町おこしアートフェスティバル','Japanese Tochigi, Mashiko, community building art festival','Q122146730','陶芸メッセ・益子','Ceramic Art Messe Mashiko','栃木県','kanto',NULL,NULL,2009,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9C%9F%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q115680256','横手の雪まつり','Yokote’s Winter Festival','秋田県横手市で行われる行事',NULL,'Q496479','横手市','Yokote','秋田県','tohoku',39.31395,140.565816666,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Kamakura%20at%20Yokote%20Castle%20202402.jpg','https://ja.wikipedia.org/wiki/%E6%A8%AA%E6%89%8B%E3%81%AE%E9%9B%AA%E3%81%BE%E3%81%A4%E3%82%8A',NULL,95,'drafted','## 概要

横手の雪まつり（よこてのゆきまつり）は、秋田県横手市で毎年2月15日・16日に開催される、約450年の歴史を持つ小正月の伝統行事である。市内各所に大小100基以上の「かまくら」が築かれ、内部に祀られた水神様に家内安全・五穀豊穣を祈願する、日本を代表する雪の祭典のひとつである。

## 歴史

横手のかまくらは室町時代後期から続く伝統行事とされ、武家の左義長（小正月の火祭り）と商人の鎌倉大明神信仰、農民の井戸の神信仰などが融合して成立した。江戸期には町内ごとに大規模なかまくらが築かれ、子どもたちが籠もって甘酒・餅を振る舞う風習が定着した。1936年（昭和11年）にドイツの建築家ブルーノ・タウトが訪れて絶賛したことでも知られ、戦後は観光行事として再興され、現在の規模に発展した。

## 見どころ

メイン会場の横手公園・羽黒町通りなどに高さ約3メートルの大型かまくらが並び、内部では子どもたちが「はいってたんせ（入ってください）」「おがんでたんせ（お参りしてください）」と訪問客を招き入れ、甘酒や餅をふるまう。蛇の崎川原には数千の小型「ミニかまくら」にろうそくが灯され、雪原に幻想的な光の海が広がる。

## 開催情報・アクセス

会場は秋田県横手市中心部の複数エリア（横手公園・羽黒町通り・蛇の崎川原ほか）。JR奥羽本線横手駅から徒歩圏内で、観覧は無料。2日間で約30万人の来場者を迎える。

## 周辺観光

横手市内には増田町の伝統的建造物群保存地区、後三年合戦金沢資料館、横手城址など、平安〜近世の歴史を感じる観光地が多い。冬季はかまくら以外にもボンデン祭り、横手やきそばも名物として人気。','## Overview

The Yokote Snow Festival (Yokote no Yuki Matsuri), also known as the Kamakura Festival, is a traditional Koshōgatsu (Little New Year) celebration with approximately 450 years of history, held annually on February 15 and 16 in Yokote City, Akita Prefecture. More than 100 large and small "kamakura" snow huts are constructed throughout the city, each enshrining the water deity (Suijin) within, before whom visitors pray for family safety and bountiful harvests. It stands as one of Japan''s most iconic snow festivals.

## History

The Yokote kamakura tradition is believed to date back to the late Muromachi period, evolving from a fusion of the warrior class Sagichō fire festival of Koshōgatsu, merchant veneration of the Kamakura Daimyōjin deity, and rural worship of well-water gods. During the Edo period, each neighborhood constructed large kamakura where children would gather to serve sweet amazake rice drink and rice cakes to visitors, establishing customs still practiced today. The festival gained international recognition when German architect Bruno Taut visited in 1936 (Shōwa 11) and praised it enthusiastically in his writings. After World War II, the festival was revived as a major tourist event and developed into its current grand scale.

## Highlights

At main venues such as Yokote Park and Haguro-machi Street, large kamakura snow huts approximately three meters tall stand in long rows. Inside each hut, children warmly invite passersby with the dialect calls "Haitte tanse" (Please come in) and "Ogande tanse" (Please pray), offering visitors amazake and grilled mochi. At the Janosaki riverside, thousands of palm-sized "mini-kamakura" are lined up in the snow with candles flickering inside, creating an enchanting sea of warm light across the snowscape that has become an iconic image of Japanese winter.

## Event Details and Access

The festival takes place across multiple areas of central Yokote City, including Yokote Park, Haguro-machi Street, and the Janosaki riverside. All venues are within walking distance of Yokote Station on the JR Ōu Main Line, and admission is free. The two-day event attracts approximately 300,000 visitors annually.

## Surrounding Attractions

Yokote City offers numerous historical attractions, including the Masuda traditional architecture preservation district featuring magnificent Edo and Meiji-period merchant houses, the Gosannen Battle Kanazawa Museum commemorating the late Heian-period conflict, and the ruins of Yokote Castle. The winter season also features the Bonden Festival and the famous Yokote Yakisoba noodles, making the area a rich destination for both cultural and culinary tourism.','yokote-no-yuki-matsuri','yokote-no-yuki-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q116838033','八代妙見祭','Yatsushiro Myōken Festival','熊本県八代市にある八代神社の秋の例大祭',NULL,'Q11428677','塩屋八幡宮','Shioya Hachimangū','熊本県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q116045081','未体験ゾーンの映画たち','Movies in the Unexperienced Zone','東京テアトル株式会社主催の劇場発信型映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9C%AA%E4%BD%93%E9%A8%93%E3%82%BE%E3%83%BC%E3%83%B3%E3%81%AE%E6%98%A0%E7%94%BB%E3%81%9F%E3%81%A1',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q123294949','日本セルビア映画祭','Japanese Serbian Film Festival',NULL,NULL,'Q3711','ベオグラード','Belgrade',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%82%BB%E3%83%AB%E3%83%93%E3%82%A2%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q121160208','アイ・ラブ・アイルランド・フェスティバル','I Love Ireland Festival',NULL,NULL,'Q1204253','代々木公園','Yoyogi Park',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q124342230','Mixひとびとtango','mix hitobito tango','京都府の祭り',NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/Mix%E3%81%B2%E3%81%A8%E3%81%B3%E3%81%A8tango',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q122231583','つきがた夏まつり',NULL,NULL,NULL,'Q1357069','月形町','Tsukigata','北海道','hokkaido',43.339333333,141.684472222,NULL,NULL,NULL,NULL,NULL,NULL,30,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q116788691','福島ビエンナーレ','Fukushima Biennale',NULL,NULL,'Q71707','福島県','Fukushima Prefecture','福島県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E5%B3%B6%E3%83%93%E3%82%A8%E3%83%B3%E3%83%8A%E3%83%BC%E3%83%AC',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q124423382','サッポロ・ミュージック・エクスペリエンス','SAPPORO MUSIC EXPERIENCE','札幌ドームで開催される音楽フェス','music festival in Sapporo, Hokkaido',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%83%E3%83%9D%E3%83%AD%E3%83%BB%E3%83%9F%E3%83%A5%E3%83%BC%E3%82%B8%E3%83%83%E3%82%AF%E3%83%BB%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%9A%E3%83%AA%E3%82%A8%E3%83%B3%E3%82%B9',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q123185718','DESIGNART TOKYO','Designart Tokyo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/DESIGNART_TOKYO',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q121645849','JAMAICA FESTIVAL レゲエ＆キュイジーヌ','Jamaica Festival Reggae & Cuisine in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q123235651','洪鐘弁天大祭','Ōgane Benten Taisai','鎌倉市の祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B4%AA%E9%90%98%E5%BC%81%E5%A4%A9%E5%A4%A7%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q116838032','山鉾','Kyoto Gion Festival Yamahoko Parade','京都祇園祭で巡行される山車',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Gion%20Matsuri%202017-5.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q122272702','神田カレーグランプリ','Kanda Curry Grand Prix','東京都千代田区神田で毎年秋に開催されるカレーのイベント',NULL,'Q338861','神田','Kanda','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kanda%20Curry%20Grand%20Prix%202013%20Winner%27s%20Trophy%20%40%20Hinoya%20%40%20Kanda%20%2812326141433%29.jpg','https://ja.wikipedia.org/wiki/%E7%A5%9E%E7%94%B0%E3%82%AB%E3%83%AC%E3%83%BC%E3%82%B0%E3%83%A9%E3%83%B3%E3%83%97%E3%83%AA',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q115353522','Fill RECO FES',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,20,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q115979645','アイドル甲子園',NULL,NULL,NULL,NULL,NULL,NULL,'兵庫県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,20,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612607',NULL,'Sapporo International Short Film Festival & Market',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125611763',NULL,'Hokkaido International Film Festival (Japan)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125611835',NULL,'Asia International Independent Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125611874',NULL,'BonDance International Film Festival（ボンダンス国際映画祭）',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125611875',NULL,'Borderless Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125611941',NULL,'Cinema at Sea - Okinawa Pan-Pacific International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125611953',NULL,'CineSakura',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612000',NULL,'Damah International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612017',NULL,'DOCUMEMENTO Shinagawa/Tokyo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612096',NULL,'Fetifest in Hamburg: Japans Underground Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612139',NULL,'Future Vision Festival - A celebration of unusual animation 異色アニメ映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612159',NULL,'Golden Harvest Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612167',NULL,'HIGHLAND SUPER8 FILM FESTIVAL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612170',NULL,'Hiroshima Animation Season',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612202',NULL,'International Auto Film Festa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612218',NULL,'International Students Creative Award',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612219',NULL,'INTERNATIONAL STUDENTS CREATIVE AWARD',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612230',NULL,'ISCA - INTERNATIONAL STUDENTS CREATIVE AWARD',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612232',NULL,'Ishigaki Island International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612233',NULL,'Ishinomaki International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612246',NULL,'JAPAN WORLD FILM FESTIVAL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612247',NULL,'Japan World''s Tourism Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612244',NULL,'Japan Indies Music Awards',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612245',NULL,'Japan Web Fest',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612250',NULL,'JIFF Japan Indies Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612258',NULL,'Kaminari Japanese Film Festival.',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612259',NULL,'Kanazawa Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612257',NULL,'Kadoma International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612266',NULL,'KINEKO International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612280',NULL,'Kyoto Kawaramachi International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612396',NULL,'Mobile MovieeFans Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612411',NULL,'Morc Comadori Animation Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612443',NULL,'Nara International Film Festival (Japan)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612453',NULL,'non-syntax Experimental Image',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612576',NULL,'Rising Sun International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612622',NULL,'Scream Queen FilmFest Tokyo / 東京スクリーム・クイーン映画祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612640',NULL,'Shibuya Sasebo TANPEN Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612646',NULL,'Short Shorts Film Festival & Asia',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612672',NULL,'Smartphone Short Film Competition / FUKUOKA Co-Creative International FILM FES',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612750',NULL,'Tokyo Documentary Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612751',NULL,'Tokyo Horror Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612748',NULL,'Tokyo CINEMASTERS International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612749',NULL,'Tokyo Cowboys Quarterly Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612754',NULL,'Tokyo Lift-Off Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612755',NULL,'Tokyo Sukiyaki Theaters',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612752',NULL,'Tokyo International Cannabis Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612762',NULL,'Toyama International Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612763',NULL,'TOYO UNIVERSITY TOURISM SHORT FILM FESTIVAL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125611869',NULL,'Bloodstained Indie Film Festival: Sci-Fi Horror Action',NULL,'Japanese film festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125601325',NULL,'Genre Celebration Festival',NULL,NULL,'Q232631','杉並区','Suginami','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125573341',NULL,'Fukuoka Asian Film Festival',NULL,NULL,'Q26600','福岡市','Fukuoka','福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125601675',NULL,'Beyond The Frame Festival',NULL,NULL,'Q232631','杉並区','Suginami','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125018927','大浜流灌頂','Ōhama-nagare-kanjō','福岡市博多区大博町で毎年行われる伝統的な祭り',NULL,'Q124983851','流灌頂通り','Nagare-kanjō Dōri',NULL,NULL,NULL,NULL,1756,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125543524',NULL,'Skip City International D-Cinema Festival',NULL,NULL,'Q387136','川口市','Kawaguchi','埼玉県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125601524',NULL,'Artpolis Osaka',NULL,NULL,'Q17','日本','Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125601437',NULL,'Japan Wildlife Film Festival',NULL,NULL,'Q17','日本','Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125601472',NULL,'New Chitose Airport International Animation Festival',NULL,NULL,'Q17','日本','Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125601553',NULL,'Miyakojima International Film Festival',NULL,NULL,'Q17','日本','Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125601627',NULL,'Meihodo International Youth Visual Media Festival',NULL,NULL,'Q17','日本','Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q131012396','2024年11月3日の神田カレーグランプリ決定戦2024','Kanda curry grand prix 2024 (November 3, 2024)','2024年11月3日に旧今川中学校跡で開催された「神田カレーグランプリ2024」の決定戦',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q127513830','rockin''on sonic','rockin''on sonic','日本のロックフェスティバル',NULL,'Q862452','幕張メッセ','Makuhari Messe',NULL,NULL,NULL,NULL,2025,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q130753581','松戸まつり','Matsudo Festival','千葉県松戸市で開催される祭り','festival in Matsudo, Chiba','Q108392912','松戸','Matsudo','茨城県','kanto',35.784442,139.899967,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Matsudo%20Festival%202024%2005.jpg',NULL,NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612796',NULL,'UNITED FOR PEACE FILM FESTIVAL (UFPFF)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612829',NULL,'Visual Documentary Project (VDP)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612864',NULL,'Obuse Keidai Art Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612865',NULL,'Obuse Short Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125612854',NULL,'Yokohama Football Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q131826721',NULL,'International Ceramics Festival Mino',NULL,'ceramics triennale in Tajimi city, Mizunami city, Toki City, and Kani city of Gifu prefecture','Q819689','多治見市','Tajimi','岐阜県','chubu',NULL,NULL,1986,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q131701907','横濱漢祭 2025','Yokohama Otoko Matsuri 2025','2025年8月26日から8月28日まで横浜スタジアムで開催されたイベント',NULL,'Q1148681','横浜スタジアム','Yokohama Stadium','神奈川県','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E6%A8%AA%E6%BF%B1%E6%BC%A2%E7%A5%AD2025%E3%80%90JERA%20%E3%82%BB%E3%83%BB%E3%83%AA%E3%83%BC%E3%82%B0%E5%85%AC%E5%BC%8F%E6%88%A6%E3%80%91%E6%A8%AA%E6%B5%9CDeNA%E3%83%99%E3%82%A4%E3%82%B9%E3%82%BF%E3%83%BC%E3%82%BA%20vs%20%E9%98%AA%E7%A5%9E%E3%82%BF%E3%82%A4%E3%82%AC%E3%83%BC%E3%82%B9%2017%E5%9B%9E%E6%88%A6%20%E6%A8%AA%E6%B5%9C%E3%82%B9%E3%82%BF%E3%82%B8%E3%82%A2%E3%83%A0%202025%E5%B9%B48%E6%9C%8826%E6%97%A5%E3%81%AE%E6%A8%AA%E6%B5%9C%20202508261426%20IMG%204937.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125894291','梵天まつり','Bonden','秋田県内各地で行われる祭事',NULL,'Q81863','秋田県','Akita Prefecture','秋田県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Bonden%20Dedication%20at%20Asahiokayama%20Shrine%20202402b.jpg','https://ja.wikipedia.org/wiki/%E6%A2%B5%E5%A4%A9%E3%81%BE%E3%81%A4%E3%82%8A_(%E7%A7%8B%E7%94%B0%E7%9C%8C)',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q132348219','神宮からあげ祭','Jingu Karaage Festival','2025年4月2日から4月4日に明治神宮野球場(神宮球場)で開催されたイベント',NULL,'Q944559','明治神宮野球場','Meiji Jingu Stadium','東京都','kanto',NULL,NULL,NULL,NULL,'spring',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q129630207','ラヴィット！ロック2024','LOVE IT! ROCK 2024','2024年8月24日に国立代々木競技場第一体育館で開催された『ラヴィット！』のイベント',NULL,'Q1069457','国立代々木競技場','Yoyogi National Gymnasium',NULL,NULL,NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/202408241502%20IMG%202701.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q130530824','永平寺門前花祭り','Eiheiji Temple Flower Festival',NULL,'festival in Japan','Q1303631','永平寺町','Eiheiji','福井県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Japan%202024-05-06%20%2853893039588%29.jpg',NULL,NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q132172823','関西コミティア',NULL,NULL,NULL,'Q11589745','神戸サンボーホール','Kobe Sanbō Hall','兵庫県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%96%A2%E8%A5%BF%E3%82%B3%E3%83%9F%E3%83%86%E3%82%A3%E3%82%A2',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q132154379','富士山・河口湖映画祭',NULL,NULL,NULL,'Q1004231','富士河口湖町','Fujikawaguchiko','山梨県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AF%8C%E5%A3%AB%E5%B1%B1%E3%83%BB%E6%B2%B3%E5%8F%A3%E6%B9%96%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q127789312','小金井桜まつり','KOGANEI SAKURA FESTIVAL','東京都小金井市で開催される祭り',NULL,'Q2856049','小金井公園','Koganei Park','東京都','kanto',35.71491473,139.51247871,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/%E7%AC%AC59%E5%9B%9E%E5%B0%8F%E9%87%91%E4%BA%95%E6%A1%9C%E3%81%BE%E3%81%A4%E3%82%8A%202013.04.07%2011-01%20-%20panoramio.jpg','https://ja.wikipedia.org/wiki/%E5%B0%8F%E9%87%91%E4%BA%95%E6%A1%9C%E3%81%BE%E3%81%A4%E3%82%8A',NULL,95,'drafted','## 概要

小金井桜まつり（こがねいさくらまつり）は、東京都小金井市の都立小金井公園および玉川上水沿いの「名勝小金井（サクラ）」一帯で、毎年4月上旬の桜の見頃に合わせて開催される花見の祭典である。江戸期から続く桜の名所として知られ、市民・観光客で賑わう東京西郊の春の風物詩である。

## 歴史

小金井の桜並木は江戸時代中期、元文2年（1737年）に川崎平右衛門が玉川上水沿いの土手を補強する目的でヤマザクラ約2,000本を植樹したことに始まる。武蔵野の地味豊かな土壌と玉川上水の清流に育まれた桜並木は、江戸の名所として浮世絵にも描かれるほど親しまれ、明治末期に「名勝小金井（サクラ）」として国の名勝に指定された。第二次世界大戦中の伐採や戦後の都市開発で大幅に減少したものの、都立小金井公園の整備とともに新たに植樹が行われ、現代の桜まつりとして再生・継承されている。

## 見どころ

都立小金井公園内には約1,700本の桜が植えられ、ソメイヨシノ・ヤマザクラ・サトザクラなど多様な品種が次々と見頃を迎える。期間中は屋台の出店、地元和太鼓・伝統芸能の奉納演奏、フリーマーケットなどが行われ、家族連れで賑わう。江戸東京たてもの園を併設しているため、復元された明治大正期の建物群と桜のコラボレーションも楽しめる。

## 開催情報・アクセス

会場は東京都立小金井公園（東京都小金井市関野町1-13-1）。JR中央線武蔵小金井駅から関東バスで約5分。入園無料。例年4月上旬の桜の見頃に合わせて開催。

## 周辺観光

小金井公園内の江戸東京たてもの園は、東京の歴史的建造物を移築・復元した野外博物館として人気が高い。隣接する小平市の小平ふるさと村、武蔵野市の井の頭恩賜公園、府中市の大國魂神社など、武蔵野エリアの自然・歴史観光と組み合わせた周遊が可能。','## Overview

The Koganei Cherry Blossom Festival (Koganei Sakura Matsuri) is a flower-viewing celebration held annually in early April during the cherry blossom peak at Tokyo Metropolitan Koganei Park and along the Tamagawa Aqueduct in the "Scenic Beauty Koganei (Cherry Trees)" area in Koganei City, Tokyo. Famous as a cherry blossom destination since the Edo period, it has become a beloved springtime tradition of Tokyo''s western suburbs, drawing crowds of residents and tourists alike.

## History

The Koganei cherry tree avenue traces its origins to the mid-Edo period in 1737 (Genbun 2), when Kawasaki Heiemon planted approximately 2,000 mountain cherry trees along the embankment of the Tamagawa Aqueduct as a reinforcement project. Nurtured by the fertile Musashino soil and the clear waters of the Tamagawa Aqueduct, the cherry tree avenue became a famous Edo landmark depicted in ukiyo-e prints and was officially designated as a National Place of Scenic Beauty as "Scenic Beauty Koganei (Cherry Trees)" in the late Meiji era. Although the number of trees declined significantly due to wartime felling during World War II and postwar urban development, new plantings have been carried out alongside the development of Koganei Park, and the festival has been revived and transmitted to the present day.

## Highlights

Tokyo Metropolitan Koganei Park hosts approximately 1,700 cherry trees, with diverse varieties including Somei Yoshino, mountain cherry, and Satozakura coming into peak bloom in succession. The festival period features food stalls, dedicatory performances of local taiko drumming and traditional folk arts, flea markets, and family-friendly entertainment. The adjacent Edo-Tokyo Open Air Architectural Museum offers the rare experience of viewing restored Meiji- and Taishō-period buildings amid the cherry blossoms.

## Event Details and Access

The venue is Tokyo Metropolitan Koganei Park (1-13-1 Sekino-chō, Koganei City, Tokyo). Access is approximately 5 minutes by Kantō Bus from Musashi-Koganei Station on the JR Chūō Line. Park admission is free. The festival is held annually in early April to coincide with the cherry blossom peak.

## Surrounding Attractions

The Edo-Tokyo Open Air Architectural Museum within Koganei Park is a popular outdoor museum displaying relocated and restored historical buildings of Tokyo. Together with nearby attractions such as Kodaira Furusato Village in Kodaira City, Inokashira Park in Musashino City, and Ōkunitama Shrine in Fuchū City, the Musashino area offers a rich combination of natural beauty, historical sites, and traditional culture for combined sightseeing tours.','koganei-sakura-matsuri','koganei-sakura-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q131681151','わらアートフェスティバル','Wara Art Festival',NULL,'festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q127950177','鉱山祭','Gold Mine Festival','新潟県佐渡市相川地区で7月に行われる祭り',NULL,'Q124496789','大山祇神社','Oyamazumi Shrine','新潟県','chubu',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E3%82%84%E3%82%8F%E3%82%89%E3%81%8E.jpg','https://ja.wikipedia.org/wiki/%E9%89%B1%E5%B1%B1%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q131752982','函館港イルミナシオン映画祭',NULL,'函館市で開催されている映画祭',NULL,'Q26418','函館市','Hakodate','北海道','hokkaido',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q130354477','ITAMI GREENJAM','ITAMI GREENJAM','兵庫県伊丹市で行われる音楽フェス','performing arts festival in Itami, Hyogo, Japan','Q11511904','昆陽池公園','Koyaike Park','兵庫県','kinki',NULL,NULL,2014,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q131932035','高浜七年祭','Takahama 7 Years Festival','福井県大飯郡高浜町で開催される祭礼','festival in Takahama, Fukui, Japan','Q1349071','高浜町','Takahama','福井県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E6%B5%9C%E4%B8%83%E5%B9%B4%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q128480280','ものづくり・匠の技の祭典2024','Monozukuri - A Celebration of Japanese Artisanal Techniques 2024','2024年8月3日に東京国際フォーラムで開催された「ものづくり・匠の技の祭典2024」',NULL,'Q1359892','東京国際フォーラム','Tokyo International Forum','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/202408031300%20DSCN1999.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q130219846',NULL,'2014 Hanazono Shrine Grand Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q126866507','因幡の傘踊り','Inaba Umbrella Dance','鳥取県東部を中心に伝わる民俗芸能','traditional performing art of the eastern region of Tottori prefecture',NULL,NULL,NULL,'鳥取県','chugoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tottori%2020210102135601%20%2851346034297%29.jpg','https://ja.wikipedia.org/wiki/%E5%9B%A0%E5%B9%A1%E3%81%AE%E5%82%98%E8%B8%8A%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q129695018','横濱漢祭 2024','Yokohama Otoko Matsuri 2024','2024年8月20日から8月22日まで横浜スタジアムで開催されたイベント',NULL,'Q1148681','横浜スタジアム','Yokohama Stadium','神奈川県','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/202408221509%20IMG%202358.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q132449320','よこすか開国花火大会','Yokosuka Kaikoku Fireworks Festival','神奈川県横須賀市で開催される花火大会','fireworks festival held in Yokosuka, Kanagawa Prefecture, Japan','Q11260718','うみかぜ公園','Umikaze Park','神奈川県','kanto',NULL,NULL,2003,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Yokosuka%20Kaikoku%20Fireworks%20Festival%2002.jpg','https://ja.wikipedia.org/wiki/%E3%82%88%E3%81%93%E3%81%99%E3%81%8B%E9%96%8B%E5%9B%BD%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q126413848','第66回築地本願寺納涼盆踊り大会','Tsukiji Honganji Bon Dance Festival 2013','2013年に行われた祭り',NULL,'Q943255','築地本願寺','Tsukiji Hongan-ji Temple','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Tsukiji%20Honganji%20Bon%20Dance%20Festival%20%289434417100%29.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q125959947','荒処の沼入り梵天','Numa-iri Bonden','秋田県横手市で行われる伝統行事',NULL,'Q496479','横手市','Yokote','秋田県','tohoku',39.282638888,140.528027777,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Numa-iri%20Bonden%20at%20Yokote%2C%20Daigo%2C%20Aratokoro%20202405a.jpg','https://ja.wikipedia.org/wiki/%E8%8D%92%E5%87%A6%E3%81%AE%E6%B2%BC%E5%85%A5%E3%82%8A%E6%A2%B5%E5%A4%A9',NULL,95,'drafted','## 概要

荒処の沼入り梵天（あらどころのぬまいりぼんでん）は、秋田県横手市平鹿町下鞭（しもむち）の荒処地区で毎年2月に行われる小正月の伝統行事である。氏子たちが「梵天（ぼんでん）」と呼ばれる五穀豊穣・無病息災の祈りを込めた依り代を担ぎ、極寒の沼に飛び込んで奉納する勇壮な雪国の祭礼として知られる。

## 歴史

梵天奉納行事は秋田県内陸部に古くから伝わる小正月の風習で、五穀豊穣・家内安全・地域繁栄を祈念する依り代を山の神・水神に捧げる神事である。荒処の沼入り梵天はその中でも特に過酷な形態を持ち、厳冬期に氷の張った沼へ褌姿の若者が梵天を担いだまま入水する点に特徴がある。起源は江戸期にまで遡るとされ、農耕と狩猟の境界地域で水神信仰と山神信仰が融合して成立した民俗行事として、地域住民に脈々と継承されてきた。横手市域の数ある梵天行事の中でも稀少な水神奉納型として民俗学的価値が高い。

## 見どころ

氷点下の沼に褌姿の男衆が梵天を担いで飛び込む光景は圧巻で、白い息と雪原の中に映える鮮やかな梵天の彩りが幻想的な対比を生む。氏子の若衆たちは事前に酒や火で身体を温め、勢いをつけて沼に飛び込む。沼入りの後は岸辺の祭壇で神事が執り行われ、参拝者には甘酒や餅が振る舞われる。横手地方の冬の風物詩として地元の温かな雰囲気が漂う。

## 開催情報・アクセス

会場は秋田県横手市平鹿町下鞭の荒処地区。JR奥羽本線横手駅から車で約20分。例年2月中旬の小正月時期に開催される。観覧は無料だが、防寒対策と長靴が必須。

## 周辺観光

横手市内には日本三大雪まつりの一つ「横手の雪まつり（かまくら）」、増田町の伝統的建造物群保存地区、後三年合戦金沢資料館、横手城址などの観光資源が集中する。冬季は稲庭うどんの里、横手やきそば、地酒の蔵元巡りなど、秋田南部の食と文化を堪能できる。','## Overview

Arasho no Numairi Bonden (Arasho Swamp-Entering Bonden Ritual) is a traditional Koshōgatsu (Little New Year) ceremony held each February in the Arasho district of Shimomuchi, Hiraka-machi, Yokote City, Akita Prefecture. Parishioners shoulder sacred "bonden" effigies—divine vessels embodying prayers for bountiful harvests and protection from illness—and plunge into the freezing winter swamp to make their offering, creating one of the most striking ceremonies of snow-country Japan.

## History

Bonden offering rites are ancient Little New Year customs widely preserved across the inland regions of Akita Prefecture, in which sacred effigies symbolizing prayers for bountiful harvests, family safety, and community prosperity are dedicated to mountain deities and water deities. Among the many bonden traditions, the Arasho Swamp-Entering Bonden stands out for its especially severe form, requiring young men in loincloths to enter a frozen swamp while still carrying their bonden in the depths of winter. The ritual''s origins are believed to reach back to the Edo period, having developed in a borderland between agriculture and hunting cultures where worship of water deities and mountain deities fused into a single folk ceremony. It has been continuously transmitted by local residents ever since. Within the many bonden ceremonies of the Yokote region, it holds significant value as a rare swamp-offering variant from the perspective of folklore studies.

## Highlights

The sight of bare-skinned men in white loincloths leaping into a sub-zero swamp while shouldering bonden creates a breathtaking spectacle, where the white breath of participants and the snow-covered landscape form a striking contrast with the vivid colors of the bonden themselves. Young parishioners warm their bodies in advance with sake and fire before charging into the icy water with momentum. Following the swamp entry, sacred rituals are conducted at an altar by the water''s edge, with sweet amazake rice drink and rice cakes offered to spectators. The whole event radiates the warm intimacy of a winter folk festival of the Yokote region.

## Event Details and Access

The venue is the Arasho district of Shimomuchi, Hiraka-machi, Yokote City, Akita Prefecture. Access is approximately 20 minutes by car from Yokote Station on the JR Ōu Main Line. The festival is held annually in mid-February during the Koshōgatsu (Little New Year) period. Viewing is free of charge, but warm clothing and boots are essential due to deep snow conditions.

## Surrounding Attractions

Yokote City offers a concentration of major tourist attractions including the Yokote Snow Festival (Kamakura), counted among Japan''s three great snow festivals, the Masuda traditional architecture preservation district, the Gosannen Battle Kanazawa Museum, and the ruins of Yokote Castle. The winter season also brings opportunities to enjoy the home of Inaniwa udon noodles, the famed Yokote yakisoba, and visits to local sake breweries, allowing visitors to experience the food and culture of southern Akita in depth.','arasho-no-numairi-bonden','arasho-no-numairi-bonden',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q129694314','横濱漢祭','Yokohama Otoko Matsuri','横浜DeNAベイスターズが毎年夏に行う行うイベント','Event of Yokohama DeNA BayStars','Q1148681','横浜スタジアム','Yokohama Stadium','神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/202408221509%20IMG%202358.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q128214137',NULL,'S2O Japan',NULL,'music festival in Japan; part of S2O Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2018,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q127503128','ものづくり・匠の技の祭典2024','Monozukuri - A Celebration of Japanese Artisanal Techniques 2024','2024年8月2日から8月4日に開催された祭典',NULL,'Q1359892','東京国際フォーラム','Tokyo International Forum','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/202408031300%20DSCN1999.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q130901892','2024年11月2日の神田カレーグランプリ決定戦2024','Kanda curry grand prix 2024 (November 2, 2024)','2024年11月2日に旧今川中学校跡で開催された「神田カレーグランプリ2024」の決定戦',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q127415167','常盤平さくらまつり','Tokiwadaira Sakura Festival','千葉県松戸市で開催される祭り','festival in Matsudo, Chiba','Q11481505','常盤平さくら通り',NULL,'茨城県','kanto',35.80251,139.95079,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tokiwadaira%20Sakura%20Festival%2003.jpg',NULL,NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654329','平筒沼ふれあい公園桜まつり',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.61635556,141.23637778,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E5%B9%B3%E7%AD%92%E6%B2%BC%E3%81%B5%E3%82%8C%E3%81%82%E3%81%84%E5%85%AC%E5%9C%92%E6%A1%9C%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653297','湘南台七夕まつり',NULL,NULL,NULL,NULL,NULL,NULL,'神奈川県','kanto',35.39623889,139.46644722,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%B9%98%E5%8D%97%E5%8F%B0%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17219247','江戸川区花火大会','Edogawa Fireworks Festival',NULL,'Fireworks show in Japan','Q1194505','江戸川','Edo River','東京都','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%B1%9F%E6%88%B8%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A_(%E6%B1%9F%E6%88%B8%E5%B7%9D%E5%8C%BA%E3%83%BB%E5%B8%82%E5%B7%9D%E5%B8%82)',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652715','おもしぇがらきてけさin富谷',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.40008333,140.89122222,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%82%82%E3%81%97%E3%81%87%E3%81%8C%E3%82%89%E3%81%8D%E3%81%A6%E3%81%91%E3%81%95in%E5%AF%8C%E8%B0%B7',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17210412','竹鼻祭り','Takehana Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%AB%B9%E9%BC%BB%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17226082','日吉山王祭','Hiyoshi Sannō-sai','滋賀県大津市の日吉大社の祭礼',NULL,'Q656451','日吉大社','Hiyoshi Taisha','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E5%90%89%E5%B1%B1%E7%8E%8B%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17211667','三国祭','Mikuni Matsuri','福井県坂井市三国町で行われる三國神社の春祭り',NULL,'Q11354793','三國神社','Mikuni Shrine','福井県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Mikuni%20festival%202022.jpg','https://ja.wikipedia.org/wiki/%E4%B8%89%E5%9B%BD%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652985','くりこま山車まつり',NULL,NULL,NULL,NULL,NULL,NULL,'秋田県','tohoku',38.831125,140.99074722,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8F%E3%82%8A%E3%81%93%E3%81%BE%E5%B1%B1%E8%BB%8A%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21015433','多賀城跡あやめまつり',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.3037,140.99158611,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%9A%E8%B3%80%E5%9F%8E%E8%B7%A1%E3%81%82%E3%82%84%E3%82%81%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20045025','深大寺鬼燈まつり','Jindai-ji Hōzuki Festival',NULL,NULL,'Q500736','深大寺','Jindai-ji Temple','神奈川県','kanto',35.66752778,139.55047222,2009,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/JindaijiMonzen.JPG','https://ja.wikipedia.org/wiki/%E6%B7%B1%E5%A4%A7%E5%AF%BA%E9%AC%BC%E7%87%88%E3%81%BE%E3%81%A4%E3%82%8A',NULL,90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17211675','三國湊帯のまち流し',NULL,'福井県坂井市三国町で行われている祭り',NULL,NULL,NULL,NULL,'福井県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%89%E5%9C%8B%E6%B9%8A%E5%B8%AF%E3%81%AE%E3%81%BE%E3%81%A1%E6%B5%81%E3%81%97',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17214735','調布国際音楽祭','Chofu International Music Festival',NULL,NULL,'Q210667','調布市','Chōfu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%AA%BF%E5%B8%83%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17228250','きたむら田舎フェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,'北海道','hokkaido',43.2598015,141.695370278,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8D%E3%81%9F%E3%82%80%E3%82%89%E7%94%B0%E8%88%8E%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653176','サザンビーチちがさき花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'神奈川県','kanto',35.313225,139.399525,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%82%B5%E3%82%B6%E3%83%B3%E3%83%93%E3%83%BC%E3%83%81%E3%81%A1%E3%81%8C%E3%81%95%E3%81%8D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20825860','日本の灌仏会','Kambutsue',NULL,'Japanese festival celebrating the birth of Buddha',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652352','浅舞公園あやめまつり',NULL,'日本の秋田県横手市にある浅舞公園で開催される祭り',NULL,NULL,NULL,NULL,'秋田県','tohoku',39.25941111,140.49343611,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B5%85%E8%88%9E%E5%85%AC%E5%9C%92%E3%81%82%E3%82%84%E3%82%81%E3%81%BE%E3%81%A4%E3%82%8A',NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652482','いばらきまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%84%E3%81%B0%E3%82%89%E3%81%8D%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652579','大洗あんこう祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%B4%97%E3%81%82%E3%82%93%E3%81%93%E3%81%86%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654307','ひぬまあじさいまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%B2%E3%81%AC%E3%81%BE%E3%81%82%E3%81%98%E3%81%95%E3%81%84%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20044069','くりはら万葉祭',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.78097222,140.95719444,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8F%E3%82%8A%E3%81%AF%E3%82%89%E4%B8%87%E8%91%89%E7%A5%AD',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654380','深谷まつり','Fukaya Festival',NULL,NULL,NULL,NULL,NULL,'群馬県','kanto',36.19263333,139.28098056,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B7%B1%E8%B0%B7%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17222740','AIR JAM',NULL,'日本のロックフェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1997,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/AIR_JAM',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17226213','高田城址公園観桜会','Takada Castle Site Park Cherry Blossom Festival',NULL,NULL,'Q11672057','高田城址公園','Takada Castle Site Park',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Takada%20Castle%20Gokuraku-bashi.JPG','https://ja.wikipedia.org/wiki/%E9%AB%98%E7%94%B0%E5%9F%8E%E5%9D%80%E5%85%AC%E5%9C%92%E8%A6%B3%E6%A1%9C%E4%BC%9A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653223','山王史跡公園あやめ祭り',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.74200278,140.94965556,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B1%B1%E7%8E%8B%E5%8F%B2%E8%B7%A1%E5%85%AC%E5%9C%92%E3%81%82%E3%82%84%E3%82%81%E7%A5%AD%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17221872','牧山の松明',NULL,NULL,NULL,'Q127366766','中世木','nakaseki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%89%A7%E5%B1%B1%E3%81%AE%E6%9D%BE%E6%98%8E',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21019044','下町七夕まつり','Shitamachi Tanabata Festival',NULL,'Tanabata Festival',NULL,NULL,NULL,'茨城県','kanto',35.71480278,139.78726944,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E4%B8%8B%E7%94%BA%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653791','とみやマーチングフェスティバル','Tomiya Marching Festival',NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.40329722,140.88143611,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%A8%E3%81%BF%E3%82%84%E3%83%9E%E3%83%BC%E3%83%81%E3%83%B3%E3%82%B0%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17212518','Sky Jamboree',NULL,NULL,NULL,'Q38234','長崎市','Nagasaki','長崎県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/Sky_Jamboree',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q18339240','弁慶まつり','Benkei festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BC%81%E6%85%B6%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17214479','美濃まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%BE%8E%E6%BF%83%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17216293','黒河夜高祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%BB%92%E6%B2%B3%E5%A4%9C%E9%AB%98%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17222037','ドッコイセ福知山花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%83%89%E3%83%83%E3%82%B3%E3%82%A4%E3%82%BB%E7%A6%8F%E7%9F%A5%E5%B1%B1%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17225609','おべっさん',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E3%81%B9%E3%81%A3%E3%81%95%E3%82%93',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17225884','オーモンデー',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%87%E3%83%BC',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17228411','こいこい祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%93%E3%81%84%E3%81%93%E3%81%84%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17228789','庄川観光祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BA%84%E5%B7%9D%E8%A6%B3%E5%85%89%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17226795','佐那神社','Sana Shrine','三重県多気郡多気町仁田にある神社','Shinto shrine in Mie Prefecture, Japan',NULL,NULL,NULL,'三重県','kinki',34.480942,136.546151,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Sana%20Shrine.jpg','https://ja.wikipedia.org/wiki/%E4%BD%90%E9%82%A3%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

佐那神社（さなじんじゃ）は、三重県多気郡多気町仁田（にた）に鎮座する式内社で、天手力男命（あめのたぢからおのみこと）と曙立王命（あけたつおうのみこと）を祀る古社である。『延喜式神名帳』に記載される伊勢国多気郡の式内社の一座で、天岩戸神話の力の神を祀る格式高い神社として知られる。

## 歴史

佐那神社は『延喜式神名帳』（927年）に式内社として記載されており、創建年代は不詳ながら少なくとも平安時代以前に遡る古社である。主祭神の天手力男命は『古事記』『日本書紀』の天岩戸神話において、岩戸に隠れた天照大神を引き出す際にその巨石を投げ飛ばした剛力の神として知られ、武運・力・農耕守護の神として崇敬されてきた。配神の曙立王命は神武天皇の御代に活躍した皇族で、当地と関わりが深いと伝わる。伊勢神宮の祭祀圏に近接する立地から、古代より朝廷・神宮の崇敬を受け、中世以降は地域の鎮守として継承されてきた。

## 見どころ

社殿は神明造系の落ち着いた建築で、深い杜に囲まれた境内は伊勢神宮の社叢を彷彿とさせる清浄な雰囲気をたたえる。天手力男命を祀ることから、勝負事・武道・スポーツ・力仕事の守護神として崇敬を集め、力石が境内に奉納されている。例祭は10月で、地元氏子による神事・神楽奉納が行われる。

## 開催情報・アクセス

JR紀勢本線多気駅から車・タクシーで約15分。境内参拝は終日自由。例祭は毎年10月に執り行われる。

## 周辺観光

多気町・松阪市・伊勢市一帯は伊勢神宮の祭祀圏として古代史の聖地が集中する。伊勢神宮内宮・外宮、おかげ横丁、松阪城跡、本居宣長記念館、瀧原宮など、神道文化と国学の核心に触れられる観光地が点在する。多気町内のVISON（ヴィソン）は和食・伝統工芸の体験型大型施設として近年人気が高い。','## Overview

Sana Shrine (Sana Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Nita, Taki Town, Taki District, Mie Prefecture. The shrine enshrines Ame no Tajikarao no Mikoto and Aketatsuō no Mikoto as its principal deities. As one of the Engishiki-registered shrines of Taki District in Ise Province, it is renowned as a prestigious shrine dedicated to the deity of strength from the Heavenly Rock Cave mythology.

## History

Sana Shrine is recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. Although the founding date is unknown, its existence as an ancient shrine reaches back at least to before the Heian period. The principal deity Ame no Tajikarao no Mikoto is famous in the Kojiki and Nihon Shoki for being the powerful god who hurled away the great boulder when drawing forth the Sun Goddess Amaterasu from the Heavenly Rock Cave, and has been long venerated as a deity governing martial fortune, physical strength, and agricultural protection. The co-enshrined deity Aketatsuō no Mikoto was an imperial figure active during the reign of Emperor Jinmu, said to have deep connections with this region. Located in close proximity to the sacred precincts of the Ise Grand Shrine, Sana Shrine received veneration from the imperial court and the Grand Shrine from ancient times and has continued as a regional guardian shrine from the medieval period onward.

## Highlights

The main shrine hall is built in the restrained Shinmei-zukuri tradition, and the precincts enclosed by deep forest evoke the pure atmosphere of the sacred groves of the Ise Grand Shrine. Because the shrine enshrines Ame no Tajikarao no Mikoto, it has attracted worshippers seeking divine protection for competitions, martial arts, sports, and physically demanding work, with stone weights (chikara-ishi) traditionally dedicated within the precincts. The annual main festival is held in October and features sacred rituals and dedicatory kagura sacred dance performances by local parishioners.

## Event Details and Access

The shrine is accessible by car or taxi in approximately 15 minutes from Taki Station on the JR Kisei Main Line. The precincts are open for worship throughout the day. The annual main festival is held in October each year.

## Surrounding Attractions

The Taki Town, Matsusaka City, and Ise City area is densely packed with sacred sites of ancient Japanese history within the ritual precincts of the Ise Grand Shrine. Attractions include the Inner and Outer Shrines of Ise Jingū, the Okage Yokochō traditional street, the ruins of Matsusaka Castle, the Motoori Norinaga Memorial Museum, and Takihara no Miya. The expansive VISON facility in Taki Town has gained popularity in recent years as an experiential complex offering Japanese cuisine and traditional crafts, making it an excellent complement to the area''s rich religious heritage.','sana-jinja','sana-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652311','辻堂諏訪神社例大祭',NULL,'神奈川県藤沢市辻堂元町の辻堂諏訪神社で開催される祭り',NULL,NULL,NULL,NULL,'長野県','chubu',35.33148056,139.45256667,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%BE%BB%E5%A0%82%E8%AB%8F%E8%A8%AA%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD',NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652951','京都ヒストリカ国際映画祭','Kyoto HISTORICA International Film Festival',NULL,'film festival','Q11375592','京都文化博物館','Museum of Kyoto','京都府','kinki',35.009388888,135.762333333,2009,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E3%83%92%E3%82%B9%E3%83%88%E3%83%AA%E3%82%AB%E5%9B%BD%E9%9A%9B%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652662','小川町七夕まつり',NULL,NULL,NULL,NULL,NULL,NULL,'群馬県','kanto',36.056025,139.26064167,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B0%8F%E5%B7%9D%E7%94%BA%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17216025','WILD BUNCH FEST.',NULL,'日本の野外ロックフェスティバル',NULL,'Q11466573','山口きらら博記念公園',NULL,NULL,NULL,NULL,NULL,2013,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/WILD_BUNCH_FEST.',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20043629','加護坊桜まつり','Kagobo Cherry Blossom Festival',NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.590175,141.10646111,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E5%8A%A0%E8%AD%B7%E5%9D%8A%E6%A1%9C%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17214138','METROPOLITAN ROCK FESTIVAL','METROPOLITAN ROCK FESTIVAL','日本のロック・フェスティバル (2013-)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/METROPOLITAN_ROCK_FESTIVAL',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20044802','信夫三山暁まいり','Shinobu Sanzan Akatsuki Mairi',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BF%A1%E5%A4%AB%E4%B8%89%E5%B1%B1%E6%9A%81%E3%81%BE%E3%81%84%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653201','佐沼夏まつり',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.69113889,141.18870833,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BD%90%E6%B2%BC%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21019186','テレビ朝日・六本木ヒルズ 夏祭り SUMMER STATION',NULL,'東京都港区の六本木ヒルズで開催されるイベント',NULL,'Q1071084','六本木ヒルズ','Roppongi Hills','東京都','kanto',NULL,NULL,2014,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%83%86%E3%83%AC%E3%83%93%E6%9C%9D%E6%97%A5%E3%83%BB%E5%85%AD%E6%9C%AC%E6%9C%A8%E3%83%92%E3%83%AB%E3%82%BA_%E5%A4%8F%E7%A5%AD%E3%82%8A_SUMMER_STATION',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654455','ふじさわ江の島花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'神奈川県','kanto',35.31055278,139.47810833,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%B5%E3%81%98%E3%81%95%E3%82%8F%E6%B1%9F%E3%81%AE%E5%B3%B6%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20043282','浦和うなぎまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B5%A6%E5%92%8C%E3%81%86%E3%81%AA%E3%81%8E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20044135','KHBまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/KHB%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20044447','さいたま市花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'埼玉県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%84%E3%81%9F%E3%81%BE%E5%B8%82%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20044460','塞の神まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A1%9E%E3%81%AE%E7%A5%9E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654102','沼田町夜高あんどん祭り','Numata Yotaka Andon Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B2%BC%E7%94%B0%E7%94%BA%E5%A4%9C%E9%AB%98%E3%81%82%E3%82%93%E3%81%A9%E3%82%93%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17212378','にっぽんど真ん中祭り','Nippon Domannaka Festival','愛知県名古屋市を中心に行われるイベント',NULL,NULL,NULL,NULL,'愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%AB%E3%81%A3%E3%81%BD%E3%82%93%E3%81%A9%E7%9C%9F%E3%82%93%E4%B8%AD%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653623','つきだて七夕まつり','Tsukidate Tanabata Matsuri',NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.73322222,141.02709167,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%A4%E3%81%8D%E3%81%A0%E3%81%A6%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17219363','炎と森のカーニバル',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%82%8E%E3%81%A8%E6%A3%AE%E3%81%AE%E3%82%AB%E3%83%BC%E3%83%8B%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654085','日本一はっとフェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.69114167,141.18868333,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E4%B8%80%E3%81%AF%E3%81%A3%E3%81%A8%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17214268','りんくう花火','Rinku Fireworks',NULL,NULL,'Q11281491','りんくう公園','Rinku Park',NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%82%8A%E3%82%93%E3%81%8F%E3%81%86%E8%8A%B1%E7%81%AB',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20043614','かくだ菜の花まつり','Kakudana Flower Festival',NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',37.97621389,140.80483611,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8B%E3%81%8F%E3%81%A0%E8%8F%9C%E3%81%AE%E8%8A%B1%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17213195','''響の都''オペラの祭典','Kyoto Opera Festival',NULL,'music festival in Japan','Q34600','京都市','Kyoto','京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%9F%BF%E3%81%AE%E9%83%BD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653987','なとり夏まつり',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.15824444,140.91026389,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%AA%E3%81%A8%E3%82%8A%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17217972','MONGOL800 ga FESTIVAL What a Wonderful World!!',NULL,NULL,'Japanese rock festival','Q11337942','ホテル日航アリビラ/ヨミタンリゾート沖縄',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/MONGOL800_ga_FESTIVAL_What_a_Wonderful_World!!',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653325','水郷佐原あやめ祭り','Suigō Sawara Ayame Festival','千葉県香取市の水郷佐原あやめパークで行われる祭り',NULL,'Q4385625','水郷佐原あやめパーク','Suigō Sawara Ayame Park','千葉県','kanto',35.92801944,140.52430833,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Suigo-Sawara-aquatic-botanical-garden3%2Ciris%2CKatori-city%2CJapan.JPG','https://ja.wikipedia.org/wiki/%E6%B0%B4%E9%83%B7%E4%BD%90%E5%8E%9F%E3%81%82%E3%82%84%E3%82%81%E7%A5%AD%E3%82%8A',NULL,95,'drafted','## 概要

水郷佐原あやめ祭り（すいごうさわらあやめまつり）は、千葉県香取市の水郷佐原あやめパークで毎年5月下旬から6月下旬にかけて開催される、約400品種150万本のハナショウブが咲き誇る関東屈指のあやめ・花菖蒲の祭典である。利根川下流域の水郷地帯の風景と共に楽しむ花の祭りとして、対岸の茨城県潮来市の「水郷潮来あやめまつり」と並び称される。

## 歴史

佐原は江戸時代から利根川水運の要衝として栄えた水郷都市で、湿地帯に自生するあやめ・ハナショウブが古くから親しまれてきた。水郷佐原あやめパーク（旧・水郷佐原水生植物園）は1969年（昭和44年）に開園し、地域観光資源として整備された。香取市の市町村合併（2006年）後、施設改修を経て現在の「水郷佐原あやめパーク」として再オープンし、毎年のあやめ祭りも規模を拡大してきた。江戸期の利根川水運を支えた佐原の伝統と、ハナショウブを中心とする花文化の融合を体現する祭典として定着している。

## 見どころ

園内には約400品種・150万本のハナショウブが植えられ、紫・白・黄・絞り模様など色彩豊かな品種が一斉に見頃を迎える。期間中の土日には「嫁入り舟」が運行され、白無垢の花嫁が小舟で園内の水路を渡る往時の水郷婚礼風景を再現する。ろ舟遊覧、夜間ライトアップ、地元産品の販売、伝統芸能の奉納など、水郷文化を堪能できる多彩なプログラムが用意される。

## 開催情報・アクセス

会場は水郷佐原あやめパーク（千葉県香取市扇島1837-2）。JR成田線佐原駅から車・タクシーで約20分。期間中は臨時シャトルバスが運行される。入園は有料（あやめ祭り期間中の特別料金）。期間中の来場者は約30万人。

## 周辺観光

佐原市街は重要伝統的建造物群保存地区に指定され、江戸期の商家・蔵・水路が残る「小江戸佐原」として観光人気が高い。伊能忠敬旧宅・記念館、香取神宮、利根川河川敷、対岸の潮来あやめ園など、水郷文化と歴史を堪能できる観光資源が集中する。鹿島神宮との「鹿島・香取・息栖」東国三社巡りも近年人気。','## Overview

The Suigō Sawara Iris Festival (Suigō Sawara Ayame Matsuri) is a major iris and Japanese iris festival held annually from late May to late June at the Suigō Sawara Ayame Park in Katori City, Chiba Prefecture, showcasing approximately 1.5 million hanashōbu Japanese iris blooms across some 400 varieties. As one of the Kantō region''s premier iris-viewing events, the festival is celebrated alongside the surrounding water-country landscape of the lower Tone River basin and is widely paired with the Suigō Itako Iris Festival on the opposite bank in Ibaraki Prefecture.

## History

Sawara flourished from the Edo period as a key water-transport hub along the Tone River, and the iris and hanashōbu plants native to the surrounding wetlands have long been cherished by local residents. The Suigō Sawara Ayame Park (formerly the Suigō Sawara Aquatic Botanical Garden) was opened in 1969 (Shōwa 44) and developed as a regional tourism resource. Following the municipal merger of Katori City in 2006, the facility underwent renovation and reopened as the current "Suigō Sawara Ayame Park," with the annual iris festival continuing to expand in scale. The festival has become firmly established as a celebration embodying the fusion of Sawara''s tradition supporting the Edo-era Tone River water transport and its flower culture centered on hanashōbu.

## Highlights

The park hosts approximately 1.5 million hanashōbu plants across some 400 varieties, displaying a spectacular palette of purple, white, yellow, and variegated blooms at peak bloom. On weekends during the festival period, the famous "Bridal Boat" (Yomeiri-bune) procession reenacts traditional water-borne wedding ceremonies, with brides in pristine white wedding kimono ferried across the canals of the park in small wooden boats. Diverse programs allow visitors to fully experience the water culture, including ro-bune rowboat tours, evening illuminations, sales of local specialty products, and dedicatory performances of traditional folk arts.

## Event Details and Access

The venue is the Suigō Sawara Ayame Park (1837-2 Ōgishima, Katori City, Chiba Prefecture). Access is approximately 20 minutes by car or taxi from Sawara Station on the JR Narita Line, with special shuttle bus service operating during the festival period. Park admission requires a special festival-period entry fee. The event draws approximately 300,000 visitors over its month-long run.

## Surrounding Attractions

The Sawara city center is designated as a National Important Preservation District for Groups of Traditional Buildings, retaining Edo-period merchant houses, traditional storehouses, and historic canals that have earned it the nickname "Little Edo Sawara" and made it a highly popular tourist destination. Concentrated attractions include the former residence and memorial museum of Inō Tadataka (the renowned Edo-period cartographer), Katori Shrine, the Tone River embankment, and the Itako Iris Garden on the opposite shore. The "Kashima-Katori-Ikisu" tour of the Three Eastern Shrines, including Kashima Shrine, has also gained considerable popularity in recent years.','suigo-sawara-ayame-matsuri','suigo-sawara-ayame-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20044199','国府夏まつり','Kō Natsu Matsuri','愛知県豊川市の祭','festival','Q11420889','国府町','Kō','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9B%BD%E5%BA%9C%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21653682','天空のゆりガーデン',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.41873056,140.72306111,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A9%E7%A9%BA%E3%81%AE%E3%82%86%E3%82%8A%E3%82%AC%E3%83%BC%E3%83%87%E3%83%B3',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20045311','仙台放送まつり','Sendai Hōsō Matsuri',NULL,'festival',NULL,NULL,NULL,'宮城県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BB%99%E5%8F%B0%E6%94%BE%E9%80%81%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20042868','ICU祭',NULL,NULL,NULL,'Q1141728','国際基督教大学','International Christian University',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/ICU%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q18458829','渋川へそ祭り',NULL,'群馬県渋川市の夏祭り',NULL,NULL,NULL,NULL,'群馬県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B8%8B%E5%B7%9D%E3%81%B8%E3%81%9D%E7%A5%AD%E3%82%8A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q18337572','中条祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%AD%E6%9D%A1%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21652456','一宮七夕まつり','Ichinomiya Tanabata Festival',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',35.30346111,136.80104444,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E4%B8%80%E5%AE%AE%E4%B8%83%E5%A4%95%E7%A5%AD%E3%82%8A%20%2819834299148%29.jpg','https://ja.wikipedia.org/wiki/%E4%B8%80%E5%AE%AE%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q18235534','三国花火大会','Mikuni Fireworks Festival','福井県坂井市で開かれる花火大会',NULL,'Q11354762','三国海水浴場','Mikuni Sunset Beach','福井県','chubu',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Mikuni%20fireworks%202013.JPG','https://ja.wikipedia.org/wiki/%E4%B8%89%E5%9B%BD%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q20043960','KYOTOGRAPHIE','Kyotographie',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2013,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/KYOTOGRAPHIE',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109602917','OP PICTURES+フェス','OP PICTURES+FES',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/OP_PICTURES%2B%E3%83%95%E3%82%A7%E3%82%B9',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q112632326','安倍川花火大会','Abe River Fireworks Festival','静岡市の花火大会','Fireworks display in Japan','Q1131483','葵区','Aoi-ku',NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%AE%89%E5%80%8D%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q110375622','大多喜お城まつり','Ōtaki Castle Festival','千葉県夷隅郡大多喜町で開催される祭り',NULL,'Q2968402','大多喜城','Ōtaki Castle','千葉県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q72727981','長幡部神社','Nagahatabe Shrine','上里町にある神社',NULL,NULL,NULL,NULL,'埼玉県','kanto',36.243305555,139.110777777,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Nagahatabe-jinja%28Kamisato-machi%2CNagahama%29.jpg','https://ja.wikipedia.org/wiki/%E9%95%B7%E5%B9%A1%E9%83%A8%E7%A5%9E%E7%A4%BE_(%E4%B8%8A%E9%87%8C%E7%94%BA)',NULL,95,'drafted','## 概要

長幡部神社（ながはたべじんじゃ）は、埼玉県児玉郡上里町（かみさとまち）に鎮座する古社で、長幡部連の祖神を祀る式内社級の格式を持つ神社である。律令期に朝廷の機織りを司った渡来系豪族・長幡部連と深い関わりを持ち、上里町の総鎮守として地域住民に篤く崇敬されてきた。

## 歴史

長幡部神社の創建年代は不詳ながら、『延喜式神名帳』（927年）に式内社として記載される武蔵国賀美郡（現・児玉郡）の古社である。長幡部連は古代の機織り技術を伝えた渡来系氏族で、朝廷に絹織物を貢納する役割を担っていた。神社の鎮座地である上里町一帯は、古代武蔵国北部の織物文化の中心地として栄え、長幡部連の祖神を祀ることで地域の繁栄と織物産業の隆盛を祈願してきた。中世以降は地域の鎮守として継承され、明治期の社格制度では郷社に列せられた。武蔵国の式内社の一座として、関東地方の古代史を語る重要な神社の一つである。

## 見どころ

社殿は近世以降の建築様式を残し、深い杜に囲まれた境内は古代の聖域の名残を感じさせる清浄な雰囲気をたたえる。境内には樹齢数百年の神木、地域の郷土史を語る石碑、長幡部連ゆかりの織物文化を象徴する文物が点在する。例祭は秋季10月で、地元氏子による神事と神楽奉納が行われ、武蔵国北部の古代信仰の名残を今に伝える。境内には織物産業の発展を祈願した絵馬・お守りなどが奉納されている。

## 開催情報・アクセス

JR高崎線神保原（じんぼはら）駅または上里町コミュニティバスで約10分。境内参拝は終日自由。秋季例祭は毎年10月に執り行われる。

## 周辺観光

上里町は埼玉県北西部に位置し、群馬県との県境に近い農業と歴史の町である。近隣には日本三大稲荷の一つ・桶川稲荷神社、本庄市の旧本庄商業銀行煉瓦倉庫、深谷市の渋沢栄一記念館、群馬県側の高崎観音山、富岡製糸場（世界遺産・近代の絹織物産業遺産）など、関東北部の歴史・文化遺産が集中する。長幡部連の織物伝統と、明治近代の富岡製糸場という時代を超えた絹文化のつながりを巡る旅も可能。','## Overview

Nagahatabe Shrine (Nagahatabe Jinja) is an ancient shrine located in Kamisato Town, Kodama District, Saitama Prefecture, possessing the dignity of a Shikinaisha (shrine listed in the 10th-century Engishiki register) and enshrining the ancestral deity of the Nagahatabe no Muraji clan. Maintaining deep connections with the immigrant clan responsible for imperial weaving during the Ritsuryō period, it has been deeply venerated by local residents as the chief tutelary shrine of Kamisato Town.

## History

Although the founding date of Nagahatabe Shrine is unknown, it is an ancient shrine of the former Kami District of Musashi Province (present-day Kodama District), recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. The Nagahatabe no Muraji were an immigrant clan that transmitted ancient weaving technology and served the imperial court by providing silk textile tribute. The Kamisato Town area where the shrine is located flourished as a center of textile culture in northern Musashi Province during ancient times, and prayers were offered at the shrine through veneration of the Nagahatabe ancestral deity for the prosperity of the region and the flourishing of the textile industry. The shrine continued as a regional guardian shrine from the medieval period onward and was ranked as a Gōsha (district shrine) under the Meiji-era shrine ranking system. As one of the Shikinaisha shrines of Musashi Province, it stands as an important shrine narrating the ancient history of the Kantō region.

## Highlights

The main shrine hall preserves architectural styles from the early-modern period onward, and the precincts enclosed by deep forest convey a pure atmosphere evoking the lingering presence of an ancient sacred site. Within the precincts stand sacred trees estimated to be several centuries old, stone monuments narrating local regional history, and cultural artifacts symbolizing the textile heritage connected to the Nagahatabe no Muraji clan. The annual main festival is held in October, featuring sacred rituals and dedicatory kagura sacred dance performances by local parishioners, transmitting to the present day the lingering traces of ancient faith from northern Musashi Province. Within the precincts are dedicated wooden votive plaques and amulets praying for the development of the textile industry.

## Event Details and Access

The shrine is accessible approximately 10 minutes from Jinbohara Station on the JR Takasaki Line or via the Kamisato Town Community Bus. The precincts are open for worship throughout the day. The autumn main festival is held in October each year.

## Surrounding Attractions

Kamisato Town is located in the northwestern part of Saitama Prefecture near the border with Gunma Prefecture, serving as a town of agriculture and history. Nearby attractions include Okegawa Inari Shrine (one of Japan''s three great Inari shrines), the former Honjō Commercial Bank Brick Warehouse in Honjō City, the Shibusawa Eiichi Memorial Museum in Fukaya City, and on the Gunma Prefecture side, the Takasaki Kannon and the Tomioka Silk Mill (a UNESCO World Heritage Site preserving the modern silk industry heritage). A journey can be designed to explore the trans-temporal connections of silk culture, linking the textile tradition of the Nagahatabe no Muraji clan with the modern Meiji-era Tomioka Silk Mill.','nagahatabe-jinja-kamisato','nagahatabe-jinja-kamisato',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q107340850','蛇も蚊も',NULL,'横浜市鶴見区の祭り',NULL,'Q127513','神奈川県','Kanagawa Prefecture','神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%9B%87%E3%82%82%E8%9A%8A%E3%82%82',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86734962','日向ひょっとこ夏祭り','Hyuga Hyottoko Summer Festival',NULL,NULL,'Q850388','日向市','Hyūga-shi',NULL,NULL,NULL,NULL,1984,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E6%97%A5%E5%90%91%E3%81%B2%E3%82%87%E3%81%A3%E3%81%A8%E3%81%93%E5%A4%8F%E7%A5%AD%E3%82%8A%E3%83%91%E3%83%AC%E3%83%BC%E3%83%89.jpg','https://ja.wikipedia.org/wiki/%E6%97%A5%E5%90%91%E3%81%B2%E3%82%87%E3%81%A3%E3%81%A8%E3%81%93%E5%A4%8F%E7%A5%AD%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q113636826','市島川裾まつり','Ichijima Kawasuso Matsuri','兵庫県丹波市市島町市島で行われる川裾祭',NULL,NULL,NULL,NULL,'兵庫県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/20140729%20Ichijima-Kawasuso%20Matsuri%20%E5%B8%82%E5%B3%B6%E5%B7%9D%E8%A3%BE%E7%A5%AD%EF%BC%88%E4%B8%B9%E6%B3%A2%E5%B8%82%E5%B8%82%E5%B3%B6%E7%94%BA%EF%BC%89%E7%AB%B9%E7%94%B0%E5%B7%9DDSCF0507.JPG','https://ja.wikipedia.org/wiki/%E5%B8%82%E5%B3%B6%E5%B7%9D%E8%A3%BE%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q112222177','世田谷パン祭り','Setagaya Panmatsuri','日本の食文化の祭典','Japanese food and drink festival','Q231645','世田谷区','Setagaya','東京都','kanto',NULL,NULL,2011,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%96%E7%94%B0%E8%B0%B7%E3%83%91%E3%83%B3%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86727428','田辺祭','Tanabe Matsuri','和歌山県田辺市で行われる鬪雞神社の例大祭',NULL,'Q11656593','鬪雞神社','Tōkei Shrine','和歌山県','kinki',NULL,NULL,1600,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E7%94%B0%E8%BE%BA%E7%A5%AD%28%E9%AC%AA%E9%9B%9E%E7%A5%9E%E7%A4%BE%29.jpg','https://ja.wikipedia.org/wiki/%E7%94%B0%E8%BE%BA%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q97280756','目白バ・ロック音楽祭','Mejiro Ba-Rock Music Festival',NULL,'former music festival (Japan)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2005,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%9B%AE%E7%99%BD%E3%83%90%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q75021413','新野の雪まつり',NULL,NULL,NULL,'Q1203314','阿南町','Anan',NULL,NULL,NULL,NULL,NULL,NULL,'winter',NULL,'https://ja.wikipedia.org/wiki/%E6%96%B0%E9%87%8E%E3%81%AE%E9%9B%AA%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q110191727','佐倉の秋祭り',NULL,'毎年10月に千葉県佐倉市で行われる祭礼',NULL,'Q498011','佐倉市','Sakura','千葉県','kanto',35.7193,140.226794,NULL,10,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E4%BD%90%E5%80%89%E3%81%AE%E7%A7%8B%E7%A5%AD%E3%82%8A',NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q115298088','三ツ山大祭','Mitsuyama-taisai',NULL,NULL,'Q11458547','射楯兵主神社','Itatehyōzu Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q100532330','ムジークフェストなら',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%A0%E3%82%B8%E3%83%BC%E3%82%AF%E3%83%95%E3%82%A7%E3%82%B9%E3%83%88%E3%81%AA%E3%82%89',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86737662','濃姫まつり','Nōhime Matsuri',NULL,'festival','Q45798','岐阜市','Gifu','岐阜県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%BF%83%E5%A7%AB%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86727691','THE GREAT SATSUMANIAN HESTIVAL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/THE_GREAT_SATSUMANIAN_HESTIVAL',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86729367','発光路の強飯式',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%99%BA%E5%85%89%E8%B7%AF%E3%81%AE%E5%BC%B7%E9%A3%AF%E5%BC%8F',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q111242683','ONE PARK FESTIVAL','ONE PARK FESTIVAL','音楽フェス',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q80708100','豊橋鬼祭','Toyohashi Oni Festival','愛知県豊橋市の祭礼行事',NULL,'Q336431','豊橋市','Toyohashi','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Onimaturi.JPG','https://ja.wikipedia.org/wiki/%E8%B1%8A%E6%A9%8B%E9%AC%BC%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109358737','焼來肉ロックフェス',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%84%BC%E4%BE%86%E8%82%89%E3%83%AD%E3%83%83%E3%82%AF%E3%83%95%E3%82%A7%E3%82%B9',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109369110','秋コレ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A7%8B%E3%82%B3%E3%83%AC',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86737956','額田のダシ行事',NULL,NULL,NULL,'Q4819566','夜久野町','Yakuno',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%A1%8D%E7%94%B0%E3%81%AE%E3%83%80%E3%82%B7%E8%A1%8C%E4%BA%8B',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109362097','日本国際美術展',NULL,NULL,NULL,'Q1490','東京都','Tokyo','東京都','kanto',NULL,NULL,1952,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E5%9B%BD%E9%9A%9B%E7%BE%8E%E8%A1%93%E5%B1%95',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q85868916','さっぽろ雪まつりK-POP FESTIVAL','Sapporo Snow Festival K-POP Fest','さっぽろ雪まつりのK-POPイベント','K-POP festival held annually in Sapporo, Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2009,NULL,'winter',NULL,'https://ja.wikipedia.org/wiki/%E3%81%95%E3%81%A3%E3%81%BD%E3%82%8D%E9%9B%AA%E3%81%BE%E3%81%A4%E3%82%8AK-POP_FESTIVAL',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q110915859','御笏神社','Oshaku Shrine','東京都三宅村の神社','Shinto shrine in Shizuoka Prefecture, Japan',NULL,NULL,NULL,'東京都','kanto',34.119994,139.522254,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BE%A1%E7%AC%8F%E7%A5%9E%E7%A4%BE',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109596038','活性の火',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B4%BB%E6%80%A7%E3%81%AE%E7%81%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109599618','MORNING RIVER SUMMIT',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/MORNING_RIVER_SUMMIT',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q105837985','でやんな祭',NULL,NULL,NULL,'Q543193','西ノ島町','Nishinoshima',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%A7%E3%82%84%E3%82%93%E3%81%AA%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q99520825','両国花火','Ryōgoku hanabi','江戸時代に両国川開きの際に開催されていた花火大会',NULL,'Q3083463','両国','Ryōgoku','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/100%20views%20edo%20098.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q113470456','大須夏まつり','Osu Summer Festival','名古屋市中区大須商店街で毎年8月に行われる催し',NULL,'Q8081716','大須','Ōsu',NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q112571725','熱田まつり','Atsuta Matsuri','名古屋市熱田区で毎年6月に開催される祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Styai2154.JPG',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q114685042','挙母祭り',NULL,NULL,NULL,'Q65269150','挙母神社','koromo Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E6%8C%99%E6%AF%8D%E3%81%BE%E3%81%A4%E3%82%8A%20%28%E6%84%9B%E7%9F%A5%E7%9C%8C%E8%B1%8A%E7%94%B0%E5%B8%82%E5%85%83%E5%9F%8E%E7%94%BA%29%20-%20panoramio%20%286%29.jpg',NULL,NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109364451','アジア国際青少年映画祭','Asia International Youth Film Festival',NULL,NULL,'Q17','日本','Japan',NULL,NULL,NULL,NULL,2004,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%B8%E3%82%A2%E5%9B%BD%E9%9A%9B%E9%9D%92%E5%B0%91%E5%B9%B4%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q114884345','大鳥美波比神社','Danjiri Matsuri at Ōtori-taisha','大鳥大社の摂社で、だんじり祭で宮入りが行われる神社',NULL,NULL,NULL,NULL,'大阪府','kinki',34.536222222,135.461583333,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/2019%20Danjiri%20festival%20at%20Otori%20Shrine009.jpg',NULL,NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q111283049','火渡り祭','Hiwatari-sai',NULL,'Japanese festival','Q8194732','高尾山薬王院','Takao-san Yakuō-in Temple',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Takaosan%20Yakuouin-1.jpg',NULL,NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q106943951','浅虫温泉ねぶた祭り','Asamushi Onsen Nebuta Festival','青森県青森市にある浅虫温泉で行われる夏祭り',NULL,'Q4803496','浅虫温泉','Asamushi Onsen','青森県','tohoku',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Asamushi%20Onsen%20Nebuta%20Matsuri%20Aomori%20Japan11n.jpg','https://ja.wikipedia.org/wiki/%E6%B5%85%E8%99%AB%E6%B8%A9%E6%B3%89%E3%81%AD%E3%81%B6%E3%81%9F%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q108373656','ベトナムフェスティバル','Vietnam Festival in Japan',NULL,NULL,'Q1204253','代々木公園','Yoyogi Park',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q108376146','NAMIMONOGATARI','NAMIMONOGATARI','毎年8月に日本の愛知県で開催される野外音楽イベント','Outdoor music festival held in Aichi prefecture, Japan',NULL,NULL,NULL,'愛知県','chubu',NULL,NULL,2005,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/NAMIMONOGATARI',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q114045450','送り盆まつり','Okuribon Festival','秋田県横手市で行われる行事',NULL,'Q496479','横手市','Yokote','秋田県','tohoku',39.317611111,140.565221944,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Butsuke-ai%20at%20Okuribon-Festival%20B.jpg','https://ja.wikipedia.org/wiki/%E9%80%81%E3%82%8A%E7%9B%86%E3%81%BE%E3%81%A4%E3%82%8A',NULL,95,'drafted','## 概要

送り盆まつり（おくりぼんまつり）は、秋田県湯沢市で毎年8月16日から18日にかけて開催される、お盆の精霊送りを起源とする伝統的な夏祭りである。市内中心部の前郷二番丁通りを舞台に、巨大な「屋形舟」と呼ばれる山車が練り歩き、最終夜には舟同士が激しくぶつかり合う勇壮な「ぶつけ合い」が見どころとなる。

## 歴史

江戸時代中期、湯沢藩政下で町人文化が栄えるなかで、亡き祖先の霊を彼岸へ送り出す精霊送りの行事として始まったとされる。当初は小規模な灯籠流しの形態であったが、徐々に屋形舟が大型化し、町内ごとに独自の意匠を凝らした山車が制作されるようになった。明治以降は地域の若衆を中心に運営され、戦後の中断を経て1957年に本格復活、現在の形となった。

## 見どころ

祭りの主役は、長さ約5メートル、高さ約4メートルの「屋形舟」と呼ばれる豪華な山車である。極彩色の彫刻と提灯で飾られた舟が、太鼓と笛の囃子に合わせて町内を巡行する。最終日の18日夜、市役所前広場で行われる「ぶつけ合い」では、町内ごとの舟が正面から激しく衝突し、火花を散らすかのような迫力で観客を熱狂させる。屋形舟は祭り終了後に湯沢川で焼かれ、精霊送りの儀式が完結する。

## 開催情報

開催地は秋田県湯沢市前郷二番丁通り、ぶつけ合いは市役所前広場。最寄駅はJR奥羽本線「湯沢駅」徒歩約10分。開催期間は毎年8月16日から18日の3日間で、ぶつけ合いは18日夜19時頃から。観覧は無料で、ぶつけ合い会場は安全のため一定の距離を保った観覧エリアが設けられる。8月中旬の東北は夕方以降冷え込むこともあるため羽織りものを推奨する。

## 周辺の見どころ

湯沢市は秋田県南部に位置し、稲庭うどん発祥の地として知られる。市内には院内銀山跡や小安峡温泉など歴史・自然観光地が点在する。隣接する横手市の横手の雪まつり（かまくら）、大仙市の大曲花火大会と並んで、秋田県南部の三大祭りのひとつに数えられることもある。','## Overview

Okuribon Matsuri (送り盆まつり) is a traditional summer festival held annually from August 16 to 18 in Yuzawa City, Akita Prefecture. Originating as a ritual to send off ancestral spirits at the close of the Obon season, the festival features massive floats called yakata-bune (palace boats) parading through downtown Yuzawa, culminating on the final night in a fierce yakata-bune collision event called butsuke-ai.

## History

The festival is said to have begun in the mid-Edo period, when townspeople culture flourished under the rule of the Yuzawa domain, as a spirit-sending ritual to escort the souls of ancestors to the other shore. Originally a modest lantern-floating event, the floats gradually grew larger, with each neighborhood designing its own distinctive yakata-bune. From the Meiji era onward, the festival was managed by young men''s associations of each district. After a wartime interruption, it was fully revived in 1957 and has continued in its present form ever since.

## Highlights

The main attraction is the yakata-bune, ornate floats approximately 5 meters long and 4 meters high. Decorated with vivid carvings and paper lanterns, the boats parade through the town to the rhythm of taiko drums and flutes. On the final night of August 18, at the plaza in front of City Hall, the yakata-bune from each district crash head-on into one another in a dramatic display called butsuke-ai, thrilling spectators with a fiery, sparks-flying intensity. After the festival, the boats are burned at the Yuzawa River, completing the spirit-sending ritual.

## Event Information

The venue is Maesato Nibancho-dori in Yuzawa City, Akita Prefecture, with the butsuke-ai held at the plaza in front of City Hall. The nearest station is Yuzawa Station on the JR Ou Main Line, about a 10-minute walk away. The festival runs annually from August 16 to 18, with the butsuke-ai beginning around 7:00 PM on August 18. Admission is free, and a safe viewing area is set up at a distance from the collision zone. Evenings in mid-August in the Tohoku region can be cool, so a light jacket is recommended.

## Nearby Attractions

Yuzawa City is located in southern Akita Prefecture and is known as the birthplace of Inaniwa udon, one of Japan''s three great udon varieties. Local attractions include the Innai Silver Mine ruins and Oyasukyo Onsen, where hot-spring towns and historical sites are scattered through the area. Alongside the Yokote Snow Festival (Kamakura) in neighboring Yokote City and the Omagari Fireworks in Daisen City, it is sometimes counted as one of southern Akita''s three great festivals.','okuribon-matsuri','okuribon-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q105338690','貴船まつり','Kibune Matsuri','神奈川県真鶴町の貴船神社の例大祭',NULL,'Q1202786','真鶴町','Manazuru','神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E8%A5%BF%E5%B0%8F%E6%97%A9%E8%88%B9%E3%83%BB%E8%B2%B4%E5%AE%AE%E4%B8%B8%20%E6%B5%B7%E4%B8%8A%E6%B8%A1%E5%BE%A1.jpg','https://ja.wikipedia.org/wiki/%E8%B2%B4%E8%88%B9%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86735439','甲子秋まつり','Kinoene Aki Matsuri',NULL,'festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%94%B2%E5%AD%90%E7%A7%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q114874856','津久野だんじり祭','Tsukuno Danjiri Matsuri','堺市西区津久野町周辺で行われるだんじり祭','It held in Tsukuno, Nishi-ku, Sakai, Osaka, is one of the Danjiri festivals in Japan.',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/2022%20K%C5%8Dno-ch%C5%8D%27%EF%BD%93%20Danjiri%20at%20Tsukuno%20Danjiri%20Festival%20in%20Tsukuno%20Area%20001.jpg','https://ja.wikipedia.org/wiki/%E6%B4%A5%E4%B9%85%E9%87%8E%E3%81%A0%E3%82%93%E3%81%98%E3%82%8A%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86740734','しばれフェスティバル','Shibare Festival','北海道足寄郡陸別町で毎年2月に開催される催事','festival held annually in Rikubetsu, Hokkaido, Japan',NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,NULL,2,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Shibare%20Festival%202019.jpg','https://ja.wikipedia.org/wiki/%E3%81%97%E3%81%B0%E3%82%8C%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109598617','お熊甲祭','Okuma Kabuto Festival','石川県七尾市にある久麻加夫都阿良加志比古神社の例祭',NULL,NULL,NULL,NULL,'石川県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8A%E7%86%8A%E7%94%B2%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109603119','熱海海上花火大会','Atami Fireworks Festival',NULL,NULL,NULL,NULL,NULL,'静岡県','chubu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%86%B1%E6%B5%B7%E6%B5%B7%E4%B8%8A%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109359912','福知山音頭',NULL,'福知山市の盆踊り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E7%9F%A5%E5%B1%B1%E9%9F%B3%E9%A0%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q86728616','ボンクリ・フェス','Born Creative Festival','東京都で開催されている現代音楽の音楽祭','Contemporary classical music festival in Tokyo, Japan','Q1956181','東京芸術劇場','Tokyo Metropolitan Theatre','東京都','kanto',NULL,NULL,2017,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%83%9C%E3%83%B3%E3%82%AF%E3%83%AA%E3%83%BB%E3%83%95%E3%82%A7%E3%82%B9',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109364478','岩槻映画祭','Iwatsuki Film Festiva',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B2%A9%E6%A7%BB%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q97171491','亀岡平和祭保津川市民花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E3%83%BB%E4%BF%9D%E6%B4%A5%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109363890','小津安二郎記念蓼科高原映画祭','Yasujiro Otsu Memorial Tateshina Kogen Film Festival',NULL,NULL,'Q838660','茅野市','Chino',NULL,NULL,NULL,NULL,1998,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B0%8F%E6%B4%A5%E5%AE%89%E4%BA%8C%E9%83%8E%E8%A8%98%E5%BF%B5%E8%93%BC%E7%A7%91%E9%AB%98%E5%8E%9F%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q97310832','大窪八幡宮秋祭り',NULL,'兵庫県明石市大久保町の大窪八幡宮で行われる秋祭り',NULL,NULL,NULL,NULL,'兵庫県','kinki',34.691205,134.943901,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E7%AA%AA%E5%85%AB%E5%B9%A1%E5%AE%AE%E7%A7%8B%E7%A5%AD%E3%82%8A',NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q109357776','''86さっぽろ花と緑の博覧会',NULL,'1986年に北海道札幌市で開催の地方博覧会',NULL,'Q37951','札幌市','Sapporo','北海道','hokkaido',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%2786%E3%81%95%E3%81%A3%E3%81%BD%E3%82%8D%E8%8A%B1%E3%81%A8%E7%B7%91%E3%81%AE%E5%8D%9A%E8%A6%A7%E4%BC%9A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041067','同社大穴持神社','Oanamochi Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.283976,132.634246,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q133287908','八坂神社祇園祭','Yasaka Jinja Gion Matsuri','静岡県掛川市の八坂神社の祭礼','festival by Yasaka Jinja in Kakegawa City, Shizuoka Prefecture, Japan',NULL,NULL,NULL,'京都府','kinki',NULL,NULL,1086,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Naka%20Yasaka%20Jinja%20Gionsai%202016%2020161002%205.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069202','畠田神社','Hatada Shrine','三重県松阪市高木町 にある神社','Candidate shrine for Ihatano shrine',NULL,NULL,NULL,'三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040069','合祀：新鞍神社','Kohakino Shrine',NULL,NULL,NULL,NULL,NULL,'福井県','chubu',35.399151,135.481622,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039309','合祀：畠田神社','Ironouheno Shrine',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',34.586721,136.619543,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039147','合祀：辛国神社','Nakanono Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.569419,135.59366,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039297','合祀：畠田神社','Sakikurusuno Shrine co-EnShrinement',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',34.586722,136.619545,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041089','合祀：塩冶神社','Yamuya- Shrine (Co-Enshrinement)',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.352363,132.764298,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041278','麻為比売神社','Tsuwada Tenman-gu Shrine','和歌山県和歌山市秋月 にある神社',NULL,NULL,NULL,NULL,'大阪府','kinki',34.222123,135.203507,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134883698','グルメバーガー日本一決定戦','JAPAN BURGER CHAMPIONSHIP 2025','2025年6月13日から6月15日まで横浜赤レンガ倉庫で開催されるグルメバーガー日本一決定戦',NULL,'Q5363823','横浜赤レンガ倉庫','Yokohama Red Brick Warehouse','神奈川県','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/JAPAN%20BURGER%20CHAMPIONSHIP%202025%20%E6%A8%AA%E6%B5%9C%E8%B5%A4%E3%83%AC%E3%83%B3%E3%82%AC%E5%80%89%E5%BA%AB%202025%E5%B9%B46%E6%9C%8813%E6%97%A5%E3%81%AE%E6%A8%AA%E6%B5%9C%20202506131801%20IMG%206929.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040253','高向神社','Takamukuno Shrine',NULL,NULL,NULL,NULL,NULL,'石川県','chubu',36.121221,136.283128,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039159','合祀：大鳥美波比神社','Woshihakeno Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.536216,135.461493,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039294','畠田神社','Hatada Shrine','三重県多気郡多気町仁田 にある神社',NULL,NULL,NULL,NULL,'愛知県','chubu',34.586694444,136.6195,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q132860355','松戸花火大会','Matsudo Fireworks Festival','千葉県松戸市で開催される花火大会','fireworks show in Matsudo, Chiba',NULL,NULL,NULL,'茨城県','kanto',35.80247,139.89385,NULL,NULL,'summer',NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134434444',NULL,'World DJ Festival Japan',NULL,'electronic music festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2025,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039171','合祀：等乃伎神社','Ohotoshino Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.521167,135.456489,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040625','合祀：浅間神社','Kutsuno Shrine',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',35.440748,134.804007,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134927474','八幡神社 (下田市吉佐美)','Hachiman Shrine','東京都新島村本村 にある神社','Shinto shrine in Shizuoka Prefecture, Japan',NULL,NULL,NULL,'静岡県','chubu',34.659076,138.915183,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%85%AB%E5%B9%A1%E7%A5%9E%E7%A4%BE_(%E4%B8%8B%E7%94%B0%E5%B8%82%E5%90%89%E4%BD%90%E7%BE%8E)',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039284','合祀：鳥墓神社','Unino Shrine',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',34.519035,136.630193,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039310','豊原神社','Ohokushino Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.525194444,136.569611111,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040900','坐波夜都武自和気神社','Hayatsumushiwakeno Shrine',NULL,NULL,NULL,NULL,NULL,'鳥取県','chugoku',35.436823,133.16584,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039250','（参）神戸神社','Hichino Shrine',NULL,NULL,NULL,NULL,NULL,'兵庫県','kinki',34.691263,136.150832,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039254','猪田神社','Ida Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.712064,136.145751,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039258','猪田神社','Sakatono Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.712064,136.145751,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069203','天香山神社','Amanokaguyama Shrine','三重県松阪市柿木原 にある神社','Candidate shrine for Hichino shrine',NULL,NULL,NULL,'三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040120','合祀：利椋八幡神社','Asomurano- Shrine',NULL,NULL,NULL,NULL,NULL,'福井県','chubu',35.722973,136.098252,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039316','物部神社','Mononoheno Shrine Co-Enshrinement',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.568929,136.473318,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q132658851','関神社','Seki Shrine','三重県亀山市にある神社','shrine in Kameyama, Mie, Japan',NULL,NULL,NULL,'三重県','kinki',34.853525,136.396002777,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039303','合祀：明星神社','Unino Shrine',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',34.525866,136.636639,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039877','日枝神社','Hie Shrine',NULL,NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040911','坐御訳神社','Miwosano Shrine',NULL,NULL,NULL,NULL,NULL,'鳥取県','chugoku',35.394325,133.222797,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039306','合祀：相生神社','Ohowakeno Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.515842,136.562179,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039452','合祀：北桑名神社','Nakatomino Shrine',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',35.065484,136.694441,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039361','合祀：亀山神社','Makiwono Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.856641,136.449781,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041087','合祀：塩冶神社','Kanmusuhitamano- Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.352363,132.764298,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041082','合祀：塩冶神社','Yamuyahikono Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.352363,132.764298,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041083','合祀：塩冶神社','Yamuyahikomayumino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.352363,132.764298,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039000','素盞雄神社 (桜井市)','Nabekurano Shrine',NULL,NULL,NULL,NULL,NULL,'奈良県','kinki',34.534591,135.909438,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039320','堀坂神社','Horisakano Shrine Co-Enshrinement',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.568929,136.473318,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069198','清水神社','Shimizu Shrine','三重県松阪市柿木原 にある神社','Candidate shrine for Nakaretano shrine',NULL,NULL,NULL,'三重県','kinki',34.559409,136.58936,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134930277','二宮神社 (三宅村)','Ninomiya Shrine','東京都三宅村坪田 にある神社','Shinto shrine in Japan',NULL,NULL,NULL,'東京都','kanto',34.086327,139.560738,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%AE%AE%E7%A5%9E%E7%A4%BE_(%E4%B8%89%E5%AE%85%E6%9D%91)',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q133909049','箱館五稜郭祭','Hakodate Goryokaku Sai','北海道函館市で開催される歴史イベント',NULL,NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,1970,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040968','伊佐我神社','Isakano Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040961','天若日子神社','Amewakahikono Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040970','天若日子神社','Amewakahikono Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040967','神阿麻能比奈等理神社','Amanohinatorino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040960','神韓国伊太弖神社','Karakuniitateno Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040966','神伊佐那伎神社','Kanisanakino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040964','神魂意保刀自神社','Kantamaihotoshino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040965','神阿須伎神社','Kanasukino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040969','阿遅須伎神社','Achisukino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040962','須佐袁神社','Susanowono Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.3991905,132.7156544,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039173','合祀：大津神社','Ahano Shrine',NULL,NULL,NULL,NULL,NULL,'滋賀県','kinki',34.505104,135.405036,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134445206','大塚バラまつり',NULL,NULL,NULL,'Q236680','豊島区','Toshima','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Otsuka%20Rose%20Festival%202025%20%281%29.jpg',NULL,NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134883693','グルメバーガー日本一決定戦','JAPAN BURGER CHAMPIONSHIP',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039315','大神社','Ohomuwano Shrine Co-Enshrinement',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.568929,136.473318,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039177','合祀：春日神社','Hokurano Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.450608,135.482758,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040712','合祀：黒野神社','Shitsumino Shrine',NULL,NULL,NULL,NULL,NULL,'兵庫県','kinki',35.544659,134.565775,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041272','武智石打命神','Takechi-Ishiuchi-no-Mikoto Shrine',NULL,'Shinto shrine in Nagato Province, Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040761','合祀：稲田神社','Sakino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.373641,133.070207,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039307','櫃倉神社','Hitsukurano Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039363','天一鍬田神社','Amenohitokuhatano Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040152','合祀：丹津神社','Ohoyamamitano Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040144','雨夜神社','Amayono Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040922','坐波夜都武自神社','Hayatsumushino Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040925','合祀：布自伎美神社','Kadoeno Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040974','大穴持海代日女神社','Amashirohimeno Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040983','合祀：伊努神社','Ifukino Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040992','合祀：都我利神社','Isahano Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040979','比古佐和気神社','Hikosawakeno Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040976','神魂伊豆乃売神社','Kantamaitsunohimeno Shrine',NULL,NULL,NULL,NULL,NULL,'静岡県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040977','神魂神社','Kantamano Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041002','比売遅神社','Himechino Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041044','韓国伊太弖神社','Karakuniitateno Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135041137','合祀：小野神社','Sukanonoamenotakarawakakono- Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039190','合祀：高靇神社','Kamusakino Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.442953,135.344483,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040766','合祀：伊邪那美神社','Hayatamano Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.373246,133.069981,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040763','合祀：伊邪那美神社','Tanakano Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.373246,133.069981,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040764','合祀：伊邪那美神社','Tatewino Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',35.373246,133.069981,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039161','陶荒田神社','Kaden Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.510422,135.52253,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039157','合祀：櫻井神社','Yamanowino Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.485457,135.506207,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q133848927',NULL,'Central Music & Entertainment Festival',NULL,'J-pop music festival based in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2025,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q133874862','函館港まつり','Hakodate Port Festival','北海道函館市で幕末の開港を記念して毎年8月に行われる夏祭り',NULL,NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%87%BD%E9%A4%A8%E6%B8%AF%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q132858753','松戸宿坂川献灯まつり',NULL,'千葉県松戸市で開かれる祭り',NULL,NULL,NULL,NULL,'茨城県','kanto',35.782116,139.897877,NULL,NULL,NULL,NULL,NULL,NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039308','合祀：相鹿上神社','Isonokamino Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.504313,136.541722,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135038739','石作神社','Ishitsukurino Shrine',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',34.950857,135.666323,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134928742','二十五柱神社','Nijugohashira Shrine','三重県松阪市柿木原 にある神社','Shinto shrine in Mie Prefecture, Japan',NULL,NULL,NULL,'三重県','kinki',34.589722222,136.599722222,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%8D%81%E4%BA%94%E6%9F%B1%E7%A5%9E%E7%A4%BE',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135039443','合祀：北桑名神社','Sanofuno Shrine',NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',35.067824,136.688545,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q134926963','姫宮神社 (南伊豆町)','Himemiya Shrine','静岡県下田市高馬 にある神社','Shinto shrine in Shizuoka Prefecture, Japan',NULL,NULL,NULL,'静岡県','chubu',34.656703,138.818973,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A7%AB%E5%AE%AE%E7%A5%9E%E7%A4%BE_(%E5%8D%97%E4%BC%8A%E8%B1%86%E7%94%BA)',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040906','同社坐大穴持御子神社','Ohonamochimiko Shrine',NULL,NULL,NULL,NULL,NULL,'鳥取県','chugoku',35.399483,133.218419,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135040905','坐大穴持神社','Ohonamochi Shrine',NULL,NULL,NULL,NULL,NULL,'鳥取県','chugoku',35.399483,133.218419,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193370','長幡部神社 旧社地','Nagahatabe Shrine former site',NULL,'Shinto shrine in Kamisato, Japan',NULL,NULL,NULL,'群馬県','kanto',36.240195,139.102104,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186410','櫛田神社','Kushida Shrine',NULL,'Kushitatsukimotono Shrine (Ronsha 2)',NULL,NULL,NULL,'三重県','kinki',34.549851,136.588784,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186732','須伎神社に合祀','Co-Enshrinement of Ohokino Shrine Ronsha 2',NULL,'Ronsha 2 for Ohokino shrine',NULL,NULL,NULL,'愛知県','chubu',34.891227,136.625274,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186411','牛庭神社','Ushiniwa Shrine',NULL,'Ushinihano Shrine (Ronsha 1)',NULL,NULL,NULL,'三重県','kinki',34.522678,136.541961,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193681','（合祀）八幡神社','Co-Enshrinement of Tsuhakino Shrine',NULL,'A candidate shrine for Tsuhakino shrine',NULL,NULL,NULL,'福井県','chubu',35.613771,136.174032,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186398','根倉神社跡','Nekura Shrine Site',NULL,'Ronsha 1 of Hitsukurano Shrine',NULL,NULL,NULL,'愛知県','chubu',34.574763,136.635438,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098896','努能太比売命神社','Nunotahimeno- Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.596304,135.506565,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186776','（論社Bを合祀する）福王神社','Co-Enshrinement of Hotsumino Shrine',NULL,'A candidate shrine for Hotsumino shrine',NULL,NULL,NULL,'三重県','kinki',35.084257,136.476883,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186783','志氐神社に合祀','Co-Enshrinement of Haseno Shrine',NULL,'A candidate shrine for Haseno shrine',NULL,NULL,NULL,'愛知県','chubu',34.990927,136.632934,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194564','八幡神社','Hachiman Shrine',NULL,'Ronsha 3 of Ohoyamamitano Shrine',NULL,NULL,NULL,'福井県','chubu',36.047072,136.168088,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194562','舟津神社（合祀）','Co-Enshrinement of Ohoyamamitano Shrine',NULL,'A candidate shrine for Ohoyamamitano shrine',NULL,NULL,NULL,'福井県','chubu',35.938846,136.186046,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186401','津田神社','Tsuda Shrine',NULL,'Hitsukurano Shrine (Ronsha 3)',NULL,NULL,NULL,'三重県','kinki',34.502271,136.514111,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194566','神明神社（合祀）','Co-Enshrinement of Ohoyamamitano Shrine Ronsha 5',NULL,'Ronsha 5 for Ohoyamamitano shrine',NULL,NULL,NULL,'福井県','chubu',35.892729,136.166683,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186645','能褒野神社に合祀','Nobono Shrine Co-Enshrinement',NULL,'A candidate shrine for Nakushirino Shrine',NULL,NULL,NULL,'三重県','kinki',34.885622,136.483248,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070121','国司神社','Kuniji Shrine','島根県松江市鹿島町佐陀宮内73 にある神社','Candidate shrine for Tarumino shrine',NULL,NULL,NULL,'島根県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135185682','粟神社跡地','Awa Shrine Site',NULL,'Shinto shrine in Izumi district, Japan',NULL,NULL,NULL,'大阪府','kinki',34.497144,135.401041,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098886','長柄神社','Nakarano Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.618659,135.607567,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186400','（論社Aを合祀する）畠田神社','Co-Enshrinement of Hitsukurano Shrine',NULL,'A candidate shrine for Hitsukurano shrine',NULL,NULL,NULL,'愛知県','chubu',34.586721,136.619543,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135185436','（合祀）玉祖神社','Co-Enshrinement in Tamanoya Shrine',NULL,'A candidate shrine for Kamono Shrine',NULL,NULL,NULL,'大阪府','kinki',34.634823,135.65267,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070084','伊邪那美神社','Izanami Shrine','同上 にある神社','Candidate shrine for Noritono shrine',NULL,NULL,NULL,'島根県','chugoku',35.373246,133.069981,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186212','佐那神社（合祀）','Moruyamano Shrine Co-EnShrinement',NULL,'A candidate shrine for Moruyamano shrine',NULL,NULL,NULL,'三重県','kinki',34.480942,136.546151,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186709','関神社に合祀','Co-Enshrinement of Katayama Shrine',NULL,'A candidate shrine for Katayama-Jinja',NULL,NULL,NULL,'三重県','kinki',34.853898,136.395964,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186687','三宅神社に合祀','Eno Shrine (Co-Enshrinement)',NULL,'A candidate shrine for Eno shrine',NULL,NULL,NULL,'三重県','kinki',34.854431,136.507187,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194563','春日神社','Kasuga Shrine',NULL,'Ronsha 2 of Ohoyamamitano Shrine',NULL,NULL,NULL,'福井県','chubu',35.944325,136.167443,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070135','宇能遅神社','Unochi Shrine','同上 にある神社','Candidate shrine for -sumineno shrine',NULL,NULL,NULL,'島根県','chugoku',35.343832,132.903573,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186693','石神社','Ishigami Shrine',NULL,'Ronsha 2 of Ihano Shrine',NULL,NULL,NULL,'三重県','kinki',34.827874,136.461192,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186720','津萩神社（飯野神社に合祀）','Tsubaki Shrine (Iino Shrine goshi)',NULL,'A candidate shrine for Tsuhakino Shrine',NULL,NULL,NULL,'山口県','chugoku',34.896835,136.623672,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186780','長倉神社に合祀','Co-Enshrinement of Sakurano Shrine',NULL,'A candidate shrine for Sakurano shrine',NULL,NULL,NULL,'愛知県','chubu',35.017257,136.632293,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070276','鴨神社 (東みよし町)','Kamogami Shrine','徳島県三好郡東みよし町加茂 にある神社','Candidate shrine for Yokotano shrine',NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070263','八幡神社','Hachiman Shrine','徳島県阿波市市場町香美 にある神社','Candidate shrine for Takefutsuno shrine',NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070197','大和神社','Yamato Shrine','岡山県総社市総社 にある神社','Candidate shrine for Nomatano shrine',NULL,NULL,NULL,'岡山県','chugoku',34.797305555,133.702111111,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070305','猿田比古神社','Sarutahiko Shrine','徳島県徳島市眉山町 にある神社','Candidate shrine for -toyotamahimeno shrine',NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070151','五十猛神社','Itakeru Shrine','島根県大田市仁摩町仁万 にある神社','Candidate shrine for Kokubunjihiyakurakuno shrine',NULL,NULL,NULL,'島根県','chugoku',35.192998,132.444542,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135099002','阿知江神社','Achieno Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186692','石大神（椿大神社に合祀）','Ihano Shrine (Co-Enshrinement)',NULL,'A candidate shrine for Ihano Shrine',NULL,NULL,NULL,'三重県','kinki',34.953649,136.433806,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070150','神楽岡八幡宮','Kaguraokahachimanguu','島根県大田市仁摩町仁万 にある神社','Candidate shrine for Kokubunjihiyakurakuno shrine',NULL,NULL,NULL,'島根県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070148','神楽岡八幡宮','Kaguraokahachimanguu','島根県大田市温泉津町湯里 にある神社','Candidate shrine for Hiyakurakuno kamutoke shrine',NULL,NULL,NULL,'島根県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098868','感古佐備神社','Kankosahino Shrine',NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',34.462749,135.59777,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186331','合祀：畠田神社 旧社地','Sakikurusuno Shrine former site',NULL,'The former shrine site of Sakikurusuno shrine',NULL,NULL,NULL,'愛知県','chubu',34.575436,136.614326,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193369','長幡部神社 旧社地','Nagahatabe Shrine former site',NULL,'Shinto shrine in Kami district, Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186326','佐那神社（合祀）','Hichino shrine Co-Enshrinement',NULL,'A candidate shrine for Hichino shrine (Ronsha 8)',NULL,NULL,NULL,'三重県','kinki',34.480942,136.546151,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193122','物部天神社・國渭地祇神社・天満天神(北野天神社)の合祀','Co-Enshrinement of Kuniwichino Shrine',NULL,'A candidate shrine for Kitano Tenjinsha',NULL,NULL,NULL,'埼玉県','kanto',35.790695,139.428834,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186194','相鹿上神社（合祀）','Co-Enshrinement of Afukamuyamano Shrine',NULL,'A candidate shrine for Afukamuyamano shrine',NULL,NULL,NULL,'三重県','kinki',34.504265,136.541816,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186414','二十五柱神社','Nijugohashira Shrine',NULL,'Ushinihano Shrine (Ronsha 3)',NULL,NULL,NULL,'三重県','kinki',34.589976,136.599752,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186660','庄内神社','Shonai Shrine',NULL,'Ronsha 1 of Amenohitokuhatano Shrine',NULL,NULL,NULL,'三重県','kinki',34.922742,136.461487,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098954','石神社','Ihano Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186407','合祀：畠田神社 旧社地','Ironouheno Shrine former site',NULL,'The former shrine site of Ironouheno shrine',NULL,NULL,NULL,'愛知県','chubu',34.582222,136.639055,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070164','稲荷神社','Inari Shrine',NULL,'Candidate shrine for Yamaheno shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135099013','出雲岡神社','Izumowokano Shrine',NULL,NULL,NULL,NULL,NULL,'島根県','chugoku',33.851268,132.786913,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186409','神山神社','Kamiyama Shrine',NULL,'Kushitatsukimotono Shrine (Ronsha 1)',NULL,NULL,NULL,'三重県','kinki',34.525215,136.569648,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186324','二十五柱神社（合祀）','Co-Enshrinement of Hichino Shrine Ronsha 6',NULL,'A candidate shrine for Hichino shrine Ronsha 6',NULL,NULL,NULL,'三重県','kinki',34.589994,136.599754,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186646','那久志里神社古社地','Nakushirino Shrine Site',NULL,'Ronsha 2 of Nakushirino Shrine',NULL,NULL,NULL,'三重県','kinki',34.883499,136.487255,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186137','（合祀）大口神社（論社を合祀）','Co-Enshrinement of Kawara Shrine',NULL,'A candidate shrine for Kawara Shrine',NULL,NULL,NULL,'愛知県','chubu',34.508107,136.732284,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186284','幸神社（合祀）','Co-Enshrinement of Afukakotano Shrine',NULL,'A candidate shrine for Afukakotano- shrine',NULL,NULL,NULL,'三重県','kinki',34.471545,136.596947,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135185391','（相殿合祀）白鳥神社','Takayano Shrine (Co-enShrinement)',NULL,'A candidate shrine for Takayano shrine',NULL,NULL,NULL,'大阪府','kinki',34.553835,135.609401,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186320','竹神社（合祀）','Co-Enshrinement of Hichino Shrine',NULL,'A candidate shrine for Hichino shrine',NULL,NULL,NULL,'愛知県','chubu',34.537286,136.61869,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194345','（合祀先）若宮八幡神社境内摂社敷玉早御玉神社','Co-Enshrinement of Shikitamahayamitamano Shrine',NULL,'A candidate shrine for Shikitamahayamitamano shrine',NULL,NULL,NULL,'宮城県','tohoku',38.527956,140.920428,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069866','月山神社に','Co-Enshrinement at Gassan Shrine','宮城県亘理郡亘理町吉田 にある神社','Candidate shrine for Kashimaitsunohikeno shrine',NULL,NULL,NULL,'山形県','tohoku',38.548694444,140.027,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186661','天一鍬田神社古社地','Amanohitokuhatano Shrine Site',NULL,'Ronsha 2 of Amenohitokuhatano Shrine',NULL,NULL,NULL,'三重県','kinki',34.910859,136.461631,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186762','石部神社に合祀','Co-Enshrinement of Ohowano Shrine (Ronsha 1)',NULL,'Ohowano Shrine (Ronsha 1)',NULL,NULL,NULL,'三重県','kinki',35.040746,136.584961,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135185428','（合祀）玉祖神社','Co-Enshrinement at Tamanooya Shrine',NULL,'Mioyano Shrine (Ronsha 1)',NULL,NULL,NULL,'大阪府','kinki',34.634823,135.65267,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135099507','久須須美神社','Kusumi Shrine',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',34.841804,135.667679,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135099001','小虫神社','Womushino Shrine',NULL,NULL,NULL,NULL,NULL,'福井県','chubu',35.901023,136.126535,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069908','雨夜神社','Amayo Shrine','福井県越前市大虫町 にある神社','Candidate shrine for Amayono shrine',NULL,NULL,NULL,'福井県','chubu',35.983175,136.123191,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186668','（論社Aを合祀する）関神社','Co-Enshrinement in Seki Shrine',NULL,'A candidate shrine for Ohowino shrine',NULL,NULL,NULL,'三重県','kinki',34.853898,136.395964,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069910','岡太神社','Okata Shrine','福井県越前市大虫町 にある神社','Candidate shrine for Amayono shrine',NULL,NULL,NULL,'福井県','chubu',35.897779,136.148348,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194539','雨夜神社 旧社地','Amayono Shrine former site',NULL,'The former shrine site of Amayono shrine',NULL,NULL,NULL,'福井県','chubu',35.978615,136.120326,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186413','牛庭神社 旧社地','Ushinihano Shrine former site',NULL,'The former shrine site of Ushinihano Shrine',NULL,NULL,NULL,'三重県','kinki',34.583141,136.597376,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070203','天神社','Tenjin-sha','岡山県笠岡市神島外浦 にある神社','Candidate shrine for Kamishimano shrine',NULL,NULL,NULL,'岡山県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193751','五社神社','Gosha Shrine',NULL,'Machino Shrine (Ronsha 2)',NULL,NULL,NULL,'福井県','chubu',35.418178,136.028627,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186415','伊勢庭神社','Isetaniwa Shrine',NULL,'Ushinihano Shrine (Ronsha 4)',NULL,NULL,NULL,'三重県','kinki',34.530475,136.592915,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070283','正八幡宮','Shō Hachimangū','徳島県美馬郡つるぎ町貞光 にある神社','Candidate shrine for Yasokono shrine',NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193750','日枝神社（合祀）','Co-Enshrinement of Machino Shrine',NULL,'A candidate shrine for Machino shrine',NULL,NULL,NULL,'福井県','chubu',35.466922,136.043191,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098806','御諸神社','Mimorono Shrine',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',34.967202,135.773386,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070307','天神社','Tenjin-sha','徳島県徳島市明神町 にある神社','Candidate shrine for Mano- shrine',NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098926','流田上神社 （流田上社神社）','Nakaretanouheno Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.589994,136.599754,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135185533','久須須美神社 旧社地','Kusumi Shrine former site',NULL,'The former shrine site of Kusumi Shrine',NULL,NULL,NULL,'京都府','kinki',34.83844,135.673216,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098974','須波若御子神社','Sunami Wakamiko Shrine',NULL,NULL,NULL,NULL,NULL,'静岡県','chubu',34.727717,137.857118,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098903','幣久良神社','Mitekurano Shrine',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',34.854146,135.563052,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069907','大虫神社','Omushi Shrine','福井県越前市大虫町 にある神社','Shinto shrine – best candidate for Amayono shrine',NULL,NULL,NULL,'福井県','chubu',35.901079,136.126531,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098936','櫛田槻本神社','Kushitatsukimotono Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098940','牛庭神社','Ushinihano Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098950','那久志里神社','Nakushirino Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186167','佐那神社（合祀）','Sumaromeno Shrine Co-Enshrinement',NULL,'A candidate shrine for Sumaromeno Shrine',NULL,NULL,NULL,'三重県','kinki',34.480942,136.546151,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194424','（合祀先）鹿島神社','Katoshimikokamino Shrine (Co-Enshrinement)',NULL,'A candidate shrine for Katoshimikokamino shrine',NULL,NULL,NULL,'宮城県','tohoku',38.775404,141.022079,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186214','畠田神社（合祀）','Hatada Shrine co-EnShrinement',NULL,'A candidate shrine for Moruyamano shrine',NULL,NULL,NULL,'愛知県','chubu',34.586722,136.619545,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186317','畠田神社（合祀）','Hatada Shrine Co-enshrinement (Ihatano)',NULL,'A candidate shrine for Ihatano shrine',NULL,NULL,NULL,'愛知県','chubu',34.586722,136.619545,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193378','(論社・合祀)榛名宮神社','Co-Enshrinement of Imakiawosakanoinamiaramitamano Shrine',NULL,'A candidate shrine for Imakiawosakanoinamiaramitamano shrine',NULL,NULL,NULL,'群馬県','kanto',36.236202,139.139954,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194567','神明神社','Shinmei Shrine',NULL,'Ronsha 6 of Ohoyamamitano Shrine',NULL,NULL,NULL,'福井県','chubu',35.888249,136.157017,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135193385','(論社・合祀)榛名宮神社','Co-Enshrinement of Imakiawosakainaminoikekamino Shrine',NULL,'A candidate shrine for Imakiawosakainaminoikekamino shrine',NULL,NULL,NULL,'群馬県','kanto',36.236202,139.139954,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070196','池田神社','Ikeda Shrine','岡山県総社市総社 にある神社','Candidate shrine for Furukohorino shrine',NULL,NULL,NULL,'岡山県','chugoku',34.749694444,133.714805555,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135186734','津萩大木神社（飯野神社に合祀）','Co-Enshrinement of Ohokino Shrine',NULL,'A candidate shrine for Ohokino shrine',NULL,NULL,NULL,'山口県','chugoku',34.896835,136.623672,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070272','鴨神社','Kamogami Shrine','徳島県三好郡東みよし町加茂 にある神社','Candidate shrine for Tawano shrine',NULL,NULL,NULL,'徳島県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069232','亀山神社','Kameyama Shrine','三重県津市芸濃町楠原 にある神社','Candidate shrine for Shihakakino shrine',NULL,NULL,NULL,'三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070295','敷島神社','Shikishima Shrine','徳島県吉野川市鴨島町敷地 にある神社','Candidate shrine for Amatsunumahikono-amanomitsusekihimeno shrine',NULL,NULL,NULL,'徳島県','shikoku',34.057927,134.338716,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194508','合祀：利椋八幡神社 旧社地','Asomurano- Shrine former site',NULL,'The former shrine site of Asomurano- shrine',NULL,NULL,NULL,'福井県','chubu',35.726018,136.116181,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135098951','県主神社','Akatanushino Shrine',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',34.885593,136.483298,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135069242','神館飯野高市神社','Kandate Iino Takaichi Shrine  Co-Enshrinement','三重県鈴鹿市神戸石橋町 にある神社','Candidate shrine for Ohokano- shrine',NULL,NULL,NULL,'三重県','kinki',34.881929,136.579081,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135070273','八幡神社','Hachiman Shrine','徳島県三好郡東みよし町加茂 にある神社','Candidate shrine for Tawano shrine',NULL,NULL,NULL,'徳島県','shikoku',34.036271,133.948991,NULL,NULL,NULL,NULL,NULL,NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135185681','合祀：大津神社','Co-Enshrinement of Hyōzu Shrine',NULL,'A candidate shrine for Hyōzu-jinja',NULL,NULL,NULL,'滋賀県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q64539503','鳥羽の火祭り','Toba Fire Festival',NULL,NULL,NULL,NULL,NULL,'三重県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%B3%A5%E7%BE%BD%E3%81%AE%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65966757','中川金魚まつり','Nakagawa Kingyo Matsuri','名古屋市中川区尾頭橋で毎年7月に開催される祭',NULL,'Q1155226','中川区','Nakagawa-ku',NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48763611','ええじゃないかとよはし映画祭',NULL,NULL,NULL,'Q336431','豊橋市','Toyohashi','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%88%E3%81%88%E3%81%98%E3%82%83%E3%81%AA%E3%81%84%E3%81%8B%E3%81%A8%E3%82%88%E3%81%AF%E3%81%97%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q31899504',NULL,'Tokyo Lift-Off Film Festival',NULL,'film festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30930004','悪態祭り','Akutai Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%82%AA%E6%85%8B%E7%A5%AD%E3%82%8A_(%E7%AC%A0%E9%96%93%E5%B8%82)',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q55524579','古河桃まつり','Koga Peach Festival',NULL,NULL,NULL,NULL,NULL,'茨城県','kanto',36.17777778,139.70047222,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8F%A4%E6%B2%B3%E6%A1%83%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q38277378','日本幻野祭','Nihon Gen''yasai','1971年に成田空港反対派が開催した野外音楽イベント',NULL,'Q47392905','天神峰','Tenjinmine','福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E5%B9%BB%E9%87%8E%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30925534','伊甘神社','Ikan Shrine','浜田市にある神社','Shinto shrine in Shimane Prefecture, Japan',NULL,NULL,NULL,'島根県','chugoku',34.929829,132.110461,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E4%BC%8A%E7%94%98%E7%A5%9E%E7%A4%BE.jpg','https://ja.wikipedia.org/wiki/%E4%BC%8A%E7%94%98%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

伊甘神社（いゆうじんじゃ）は、島根県浜田市下府町（しもこうちょう）に鎮座する式内社で、伊甘大神（いゆうのおおかみ）を主祭神として祀る古社である。『延喜式神名帳』に記載される石見国那賀郡の式内社の一座で、石見国府の所在地に隣接する立地と、古代石見国の総鎮守として崇敬されてきた格式の高さで知られる。

## 歴史

伊甘神社は『延喜式神名帳』（927年）に式内社として記載されており、創建年代は不詳ながら少なくとも平安時代以前に遡る古社である。主祭神の伊甘大神は地域の祖神・国津神とされ、古代石見国の開拓と農耕守護の神として崇敬されてきた。鎮座地の浜田市下府町一帯は石見国府の所在地と推定される古代地名で、伊甘神社は国府の鎮守として機能した可能性が高い。律令期から朝廷の崇敬を受け、中世以降は石見地方の地域信仰の中核として機能、明治期の社格制度では郷社に列せられた。

## 見どころ

社殿は出雲地方特有の大社造系の意匠を残す近世建築で、簡素ながら格調高い佇まいが特徴。境内には古代国府時代を偲ばせる石組みや、樹齢数百年とされる神木が残されている。石見国府推定地に隣接する立地から、考古学・古代史研究の観点でも注目される。例祭は秋季10月で、地元氏子による神事と神楽奉納が行われ、石見地方独特の「石見神楽」が奉納されることもある。

## 開催情報・アクセス

JR山陰本線下府駅から徒歩約15分または車で約5分。境内参拝は終日自由。秋季例祭は毎年10月に執り行われる。

## 周辺観光

浜田市は日本海に面した山陰地方の港町で、石見畳ヶ浦（国指定天然記念物・名勝）、しまね海洋館アクアス、浜田城跡、世界遺産・石見銀山遺跡（隣接する大田市）など、石見地方の自然・歴史・文化を堪能できる観光資源が集中する。石見神楽の上演施設、温泉津温泉、有福温泉など温泉文化も楽しめ、出雲大社・松江城との周遊観光が可能。','## Overview

Iyu Shrine (Iyu Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Shimokō-chō, Hamada City, Shimane Prefecture. The shrine enshrines Iyu no Ōkami as its principal deity. As one of the Engishiki-registered shrines of Naka District in Iwami Province, it is renowned for its location adjacent to the site of the Iwami Provincial Government Office and its prestigious status as a chief tutelary shrine of ancient Iwami Province.

## History

Iyu Shrine is recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. Although the founding date is unknown, its existence as an ancient shrine reaches back at least to before the Heian period. The principal deity Iyu no Ōkami is considered an ancestral deity and earth-born deity (kunitsukami) of the region, venerated as the god of pioneering settlement and agricultural protection in ancient Iwami Province. The shrine''s location in the Shimokō-chō district of Hamada City corresponds to the presumed site of the Iwami Provincial Government Office, suggesting Iyu Shrine likely functioned as a guardian shrine of the provincial government. The shrine received veneration from the imperial court since the Ritsuryō period, served as a central institution of regional faith in the Iwami area from the medieval period onward, and was ranked as a Gōsha (district shrine) under the Meiji-era shrine ranking system.

## Highlights

The main shrine hall is an early-modern construction preserving design elements of the Taisha-zukuri tradition characteristic of the Izumo region, featuring a simple yet refined and dignified appearance. The precincts contain stone arrangements evoking the era of the ancient provincial government and sacred trees estimated to be several centuries old. The location adjacent to the presumed Iwami Provincial Government Office site attracts attention from the perspectives of archaeology and ancient historical research. The annual main festival is held in October and features sacred rituals and dedicatory kagura sacred dance performances by local parishioners, sometimes including offerings of the distinctive "Iwami Kagura" unique to the Iwami region.

## Event Details and Access

The shrine is accessible approximately 15 minutes on foot or 5 minutes by car from Shimokō Station on the JR San''in Main Line. The precincts are open for worship throughout the day. The autumn main festival is held in October each year.

## Surrounding Attractions

Hamada City is a port town facing the Sea of Japan in the San''in region, offering a concentration of tourism resources for experiencing the nature, history, and culture of the Iwami area, including Iwami Tatamigaura (a nationally designated Natural Monument and Place of Scenic Beauty), the Shimane Aquarium Aquas, the ruins of Hamada Castle, and the nearby UNESCO World Heritage Site of the Iwami Ginzan Silver Mine in adjacent Ōda City. Visitors can also enjoy Iwami Kagura performance venues and the hot spring culture of Yunotsu Onsen and Arifuku Onsen, making it possible to combine sightseeing with Izumo Taisha Grand Shrine and Matsue Castle for a comprehensive tour of the San''in region.','iyu-jinja','iyu-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30925655','矢作神社秋の大祭','Yahagi Shrine Autumn Grand Festival','愛知県岡崎市で開催される祭り',NULL,'Q11583921','矢作神社','Yahagi Shrine','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Yahagi-Jinja-1.jpg','https://ja.wikipedia.org/wiki/%E7%9F%A2%E4%BD%9C%E7%A5%9E%E7%A4%BE%E7%A7%8B%E3%81%AE%E5%A4%A7%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48762792','かみのやま温泉全国かかし祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8B%E3%81%BF%E3%81%AE%E3%82%84%E3%81%BE%E6%B8%A9%E6%B3%89%E5%85%A8%E5%9B%BD%E3%81%8B%E3%81%8B%E3%81%97%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q60996972','アーラ映画祭',NULL,NULL,NULL,'Q11411815','可児市文化創造センター',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%BC%E3%83%A9%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q56348130','東京イラン映画祭','Iranian Film Festival in Tokyo',NULL,NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,2018,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E3%82%A4%E3%83%A9%E3%83%B3%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65272329','泳げ鯉のぼり相模川','Sagami River Koinobori Matsuri','神奈川県相模原市の相模川高田橋上流で開催されていた行事','former koinobori event in Sagamihara, Kanagawa, Japan','Q209779','相模原市','Sagamihara','神奈川県','kanto',NULL,NULL,1988,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E6%B3%B3%E3%81%92%E9%AF%89%E3%81%AE%E3%81%BC%E3%82%8A%E7%9B%B8%E6%A8%A1%E5%B7%9D.jpg','https://ja.wikipedia.org/wiki/%E6%B3%B3%E3%81%92%E9%AF%89%E3%81%AE%E3%81%BC%E3%82%8A%E7%9B%B8%E6%A8%A1%E5%B7%9D',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q38277461','高塔山ジャム',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E5%A1%94%E5%B1%B1%E3%82%B8%E3%83%A3%E3%83%A0',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q56863439','こまねこまつり','Komaneko Festival','京丹後市峰山で民間主導で2016年にはじまったまちおこしイベント','festival in Kyoto, Japan','Q56523409','金刀比羅神社','Kotohira Shrine',NULL,NULL,NULL,NULL,2016,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E3%81%93%E3%81%BE%E3%81%AD%E3%81%93%E3%81%BE%E3%81%A4%E3%82%8A%E7%B4%A0%E7%84%BC%E3%81%8D%E3%81%93%E3%81%BE%E3%81%AD%E3%81%93.jpg','https://ja.wikipedia.org/wiki/%E3%81%93%E3%81%BE%E3%81%AD%E3%81%93%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48745443','尾張横須賀まつり','Owari Yokosuka Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B0%BE%E5%BC%B5%E6%A8%AA%E9%A0%88%E8%B3%80%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65247980','上杉雪灯篭まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%8A%E6%9D%89%E9%9B%AA%E7%81%AF%E7%AF%AD%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65258543','大石田まつり最上川花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E7%9F%B3%E7%94%B0%E3%81%BE%E3%81%A4%E3%82%8A%E6%9C%80%E4%B8%8A%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65272115','江包・大西の御綱',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B1%9F%E5%8C%85%E3%83%BB%E5%A4%A7%E8%A5%BF%E3%81%AE%E5%BE%A1%E7%B6%B1',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65280366','茅ヶ崎サザン芸術花火2018',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E8%8C%85%E3%83%B6%E5%B4%8E%E3%82%B5%E3%82%B6%E3%83%B3%E8%8A%B8%E8%A1%93%E8%8A%B1%E7%81%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q63795744','加悦谷祭','A feast day of Kayadani',NULL,NULL,'Q11398630','加悦谷',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8A%A0%E6%82%A6%E8%B0%B7%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30927123','みやこ祭',NULL,'東京都立大学の大学祭',NULL,'Q1148334','東京都立大学','Tokyo metropolitan university','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BF%E3%82%84%E3%81%93%E7%A5%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30928431','萩姫まつり','Hagi Hime Matsuri',NULL,'festival',NULL,NULL,NULL,'山口県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%90%A9%E5%A7%AB%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q56010148','猪名川花火大会',NULL,'大阪府池田市及び兵庫県川西市の猪名川流域で開催される花火大会',NULL,'Q11571867','猪名川','Ina River','京都府','kinki',34.820722222,135.417361111,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Inagawa%20Hanabi.jpeg','https://ja.wikipedia.org/wiki/%E7%8C%AA%E5%90%8D%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q38277088','騎馬武者ロックフェス',NULL,NULL,NULL,'Q642094','南相馬市','Minamisōma-shi','福島県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%A8%8E%E9%A6%AC%E6%AD%A6%E8%80%85%E3%83%AD%E3%83%83%E3%82%AF%E3%83%95%E3%82%A7%E3%82%B9',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48748728','江差かもめ島祭り','Esashi Kamomejima Festival',NULL,NULL,NULL,NULL,NULL,'北海道','hokkaido',41.866013833,140.118369833,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B1%9F%E5%B7%AE%E3%81%8B%E3%82%82%E3%82%81%E5%B3%B6%E7%A5%AD%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q56347969','鳴門市納涼花火大会','Naruto Fireworks Festival','徳島県鳴門市で開催される花火大会',NULL,'Q17217384','撫養川親水公園','Muya River Park','徳島県','shikoku',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E9%B3%B4%E9%96%80%E5%B8%82%E7%B4%8D%E6%B6%BC%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65236261','むらやま徳内まつり','Murayama Tokunai Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%80%E3%82%89%E3%82%84%E3%81%BE%E5%BE%B3%E5%86%85%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q60848673','十日えびす','Tōka Ebisu','1月10日前後に関西地方で行われる年中行事',NULL,'Q705297','西宮神社','Nishinomiya Shrine','兵庫県','kinki',NULL,NULL,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Horikawaebisu-jinja%20Osaka%20Japan04-r.jpg','https://ja.wikipedia.org/wiki/%E5%8D%81%E6%97%A5%E3%81%88%E3%81%B3%E3%81%99',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48758315','羽浦神社','Hanoura Shrine','徳島県阿南市羽ノ浦町中庄にある神社','Shinto shrine in Tokushima Prefecture, Japan',NULL,NULL,NULL,'徳島県','shikoku',33.964836,134.629643,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Haura-jinja%20%28anan%29.jpg','https://ja.wikipedia.org/wiki/%E7%BE%BD%E6%B5%A6%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

羽浦神社（はのうらじんじゃ）は、徳島県阿南市羽ノ浦町中庄（はのうらちょうなかしょう）に鎮座する神社で、誉田別命（ほんだわけのみこと・応神天皇）を主祭神として祀る古社である。羽ノ浦町の総鎮守として地域住民に篤く崇敬され、阿波国南部の歴史と農耕文化を伝える郷社として継承されてきた。

## 歴史

羽浦神社の創建年代は不詳ながら、江戸時代以前から羽ノ浦地域の鎮守として機能していたことが地誌類から確認される。主祭神の誉田別命は第15代応神天皇であり、八幡神として全国で広く崇敬される神格である。武運・国家鎮護・農耕守護の神として、武家のみならず農民・町人にも親しまれた。阿波国（現徳島県）は古代から麻・藍・稲作で栄えた地域であり、羽浦神社も農耕儀礼の中心として地域の信仰生活を支えてきた。明治期の社格制度下では郷社に列せられ、近代以降も地域の核となる神社として継承されている。

## 見どころ

社殿は近世以降の建築様式を残し、地域の風土に調和した素朴で品格ある佇まいが特徴。境内には樹齢数百年とされる神木や、地域の郷土史を語る石碑、奉納された絵馬・狛犬などが点在し、阿波の農村信仰の素朴な雰囲気を伝える。例祭は秋季10月に執り行われ、地元氏子による神事・神輿渡御・奉納神楽が行われる。羽ノ浦町の伝統行事として地域住民に親しまれている。

## 開催情報・アクセス

JR牟岐線羽ノ浦駅から徒歩約15分または車で約5分。境内参拝は終日自由。秋季例祭は毎年10月の指定日に執り行われる。

## 周辺観光

阿南市は徳島県南部の中心都市で、四国八十八ヶ所霊場の22番札所・平等寺、23番札所・薬王寺（牟岐町）が近接し、お遍路の重要中継地点として知られる。橘湾の絶景、蒲生田岬（四国最東端）、太龍寺ロープウェイなど自然景観も豊か。徳島県内では阿波踊り（徳島市・8月開催）、大塚国際美術館（鳴門市）、祖谷渓・かずら橋（三好市）など、阿波文化を堪能できる観光地と組み合わせた周遊が可能。','## Overview

Hanoura Shrine (Hanoura Jinja) is a Shinto shrine located in Nakashō, Hanoura-chō, Anan City, Tokushima Prefecture, enshrining Hondawake no Mikoto (Emperor Ōjin) as its principal deity. As the chief tutelary shrine of Hanoura-chō, it has been deeply venerated by local residents and preserved as a regional shrine transmitting the history and agricultural culture of southern Awa Province.

## History

Although the founding date of Hanoura Shrine is unknown, regional historical records confirm that it functioned as the guardian shrine of the Hanoura area from before the Edo period. The principal deity Hondawake no Mikoto is the 15th Emperor Ōjin, widely venerated throughout Japan as the Hachiman deity. Beloved by warriors, farmers, and townspeople alike, this deity was revered as a god of martial fortune, national protection, and agricultural guardianship. Awa Province (present-day Tokushima Prefecture) has been known since ancient times as a region prospering through hemp, indigo, and rice cultivation, and Hanoura Shrine served as a center of agricultural rituals supporting the religious life of the local community. Under the Meiji-era shrine ranking system, it was designated as a Gōsha (district shrine), and from the modern era onward, it has continued as the central shrine of the region.

## Highlights

The shrine buildings preserve architectural styles from the early-modern period onward, featuring a humble yet dignified appearance harmonizing with the local landscape. Within the precincts stand sacred trees estimated to be several centuries old, stone monuments narrating local regional history, and dedicated wooden votive plaques (ema) and stone guardian dog statues (komainu), conveying the simple atmosphere of rural folk faith in Awa Province. The annual main festival is held in October, featuring sacred rituals, portable shrine (mikoshi) processions, and dedicatory kagura sacred dance performances by local parishioners. The festival has been cherished as a traditional event of Hanoura-chō by local residents.

## Event Details and Access

The shrine is accessible approximately 15 minutes on foot or 5 minutes by car from Hanoura Station on the JR Mugi Line. The precincts are open for worship throughout the day. The autumn main festival is held on a designated date in October each year.

## Surrounding Attractions

Anan City is the central urban hub of southern Tokushima Prefecture, with Byōdō-ji Temple (the 22nd temple on the Shikoku Pilgrimage) and the nearby Yakuō-ji Temple (the 23rd temple, in Mugi Town) making it a major waypoint along the famous Shikoku Henro pilgrimage route. The area also features rich natural scenery including the spectacular views of Tachibana Bay, Kamoda Misaki (the easternmost point of Shikoku), and the Tairyū-ji Ropeway. Within Tokushima Prefecture, combined sightseeing tours are possible with attractions allowing visitors to experience Awa culture, including the Awa Odori dance festival in Tokushima City (August), the Otsuka Museum of Art in Naruto City, and the Iya Valley with its famous Kazura-bashi vine bridges in Miyoshi City.','hanoura-jinja','hanoura-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48748975','水都まつり','Suito Matsuri',NULL,'festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E9%83%BD%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q60996676','松原神社秋季大祭',NULL,'兵庫県尼崎市の浜田町にある神社で行われる秋祭り',NULL,NULL,NULL,NULL,'兵庫県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E5%8E%9F%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E5%A4%A7%E7%A5%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q55526350','本町の八月踊り','August dance in Honmachi','鹿児島県肝付町で江戸時代から続く豊作を祈る踊り','pray for good Harvest danced had been 300 year ago',NULL,NULL,NULL,'鹿児島県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/8gatu2%20b%20%28Kimotsuki%29.jpg','https://ja.wikipedia.org/wiki/%E6%9C%AC%E7%94%BA%E3%81%AE%E5%85%AB%E6%9C%88%E8%B8%8A%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q60985206','神奈川新聞花火大会','Kanagawa Shimbun Fireworks Festival',NULL,'fireworks festival held in Yokohama, Japan from 1986 to 2016','Q38283','横浜市','Yokohama','神奈川県','kanto',NULL,NULL,1986,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%A5%9E%E5%A5%88%E5%B7%9D%E6%96%B0%E8%81%9E%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q56026191','吉野川市納涼花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'奈良県','kinki',34.084833333,134.349916666,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%90%89%E9%87%8E%E5%B7%9D%E5%B8%82%E7%B4%8D%E6%B6%BC%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48748967','大垣十万石まつり','Ōgaki Jūmangoku Matsuri','岐阜県大垣市で行われる祭',NULL,NULL,NULL,NULL,'岐阜県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%B2%90%E9%98%9C%E7%9C%8C%E5%A4%A7%E5%9E%A3%E5%B8%82%E6%9D%B1%E5%A4%96%E5%81%B4%E7%94%BA%20-%20panoramio.jpg','https://ja.wikipedia.org/wiki/%E5%A4%A7%E5%9E%A3%E5%8D%81%E4%B8%87%E7%9F%B3%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q57388689','いいやま雪まつり','Iiyama Snow Festival',NULL,NULL,'Q851097','飯山市','Iiyama',NULL,NULL,NULL,NULL,1980,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/%E7%A6%8F%E5%AF%BF%E7%94%BA%E9%9B%AA%E5%83%8F.jpg','https://ja.wikipedia.org/wiki/%E3%81%84%E3%81%84%E3%82%84%E3%81%BE%E9%9B%AA%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q61057617','大阪世界帆船まつり','Osaka Sekai Hansen Matsuri',NULL,'festival',NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E9%98%AA%E4%B8%96%E7%95%8C%E5%B8%86%E8%88%B9%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48744152','湯涌ぼんぼり祭り','Yuwaku Bonbori Matsuri','石川県金沢市湯涌温泉の祭り',NULL,'Q11563731','湯涌温泉','Yuwaku Onsen','石川県','chubu',NULL,NULL,2011,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Yuwaku%20Bonbori%20sending-off%20ceremony%20for%20the%20god%202012-10-06.JPG','https://ja.wikipedia.org/wiki/%E6%B9%AF%E6%B6%8C%E3%81%BC%E3%82%93%E3%81%BC%E3%82%8A%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30925738','須賀神社大祭','Suga Shrine Taisai','愛知県岡崎市で行われる祭り',NULL,'Q11664821','須賀神社','Suga Shrine','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kashiyamacho-Suga-Jinja-2.jpg','https://ja.wikipedia.org/wiki/%E9%A0%88%E8%B3%80%E7%A5%9E%E7%A4%BE%E5%A4%A7%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q55528785','EDC Japan','EDC Japan',NULL,'music festival in Japan','Q170616','千葉市','Chiba','千葉県','kanto',NULL,NULL,2017,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/EDC_Japan',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30928413','城端むぎや祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9F%8E%E7%AB%AF%E3%82%80%E3%81%8E%E3%82%84%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30934365','排禍ばやし',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%8E%92%E7%A6%8D%E3%81%B0%E3%82%84%E3%81%97',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30935919','土浦カレーフェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9C%9F%E6%B5%A6%E3%82%AB%E3%83%AC%E3%83%BC%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65235263','とまこまいスケートまつり','Tomakomai Skate Matsuri',NULL,'festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%A8%E3%81%BE%E3%81%93%E3%81%BE%E3%81%84%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%88%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65272061','水郷大江夏まつり灯ろう流し花火大会',NULL,'山形県西村山郡大江町で開催される花火大会',NULL,NULL,NULL,NULL,'山形県','tohoku',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E9%83%B7%E5%A4%A7%E6%B1%9F%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A%E7%81%AF%E3%82%8D%E3%81%86%E6%B5%81%E3%81%97%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q55540286','秋葉原映画祭','Akiba Film Festival',NULL,NULL,'Q418096','秋葉原','Akihabara','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A7%8B%E8%91%89%E5%8E%9F%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q55526656','ほくそう春まつり','Hokusō Haru Matsuri',NULL,'festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BB%E3%81%8F%E3%81%9D%E3%81%86%E6%98%A5%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q60213133','強飯式','Gohan ritual','志願者が大盃の酒や山盛りのご飯を食べることを強要される儀式','in Buddhism, a ceremony called ceremony of forced rice eating',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q60997299','水戸のラーメンまつり',NULL,NULL,NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E6%88%B8%E3%81%AE%E3%83%A9%E3%83%BC%E3%83%A1%E3%83%B3%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q38276665','寺フェス in 山形県朝日町若宮寺',NULL,NULL,NULL,'Q1347249','朝日町','Asahi','山形県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AF%BA%E3%83%95%E3%82%A7%E3%82%B9_in_%E5%B1%B1%E5%BD%A2%E7%9C%8C%E6%9C%9D%E6%97%A5%E7%94%BA%E8%8B%A5%E5%AE%AE%E5%AF%BA',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q67704099','放生会','Hōjōya','福岡県福岡市の筥崎宮で開催される祭り',NULL,'Q714742','筥崎宮','Hakozaki Shrine','福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hojoya%20Festival%20of%20Hakozaki%20Shrine%2020190916-1.jpg','https://ja.wikipedia.org/wiki/%E6%94%BE%E7%94%9F%E4%BC%9A_(%E7%AD%A5%E5%B4%8E%E5%AE%AE)',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65262484','富津市民花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'三重県','kinki',35.306111111,139.813611111,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%AF%8C%E6%B4%A5%E5%B8%82%E6%B0%91%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q65279849','芝山はにわ祭','Shibayama Haniwa Festival','千葉県芝山町で開催される祭',NULL,NULL,NULL,NULL,'千葉県','kanto',NULL,NULL,1982,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%8A%9D%E5%B1%B1%E3%81%AF%E3%81%AB%E3%82%8F%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q60988115','くつっ子まつり','Kutsukko Matsuri',NULL,'festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8F%E3%81%A4%E3%81%A3%E5%AD%90%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q66633854','佐陀神能','Sada Shin Noh','島根県の祭り',NULL,'Q3461072','佐太神社','Sada Shrine','島根県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BD%90%E9%99%80%E7%A5%9E%E8%83%BD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q48743940','国府宮はだか祭り','Konomiya Hadaka Matsuri','稲沢市の伝統行事',NULL,'Q11465296','尾張大国霊神社','Owari Ōkunitama Shrine','愛知県','chubu',35.256111,136.805139,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Kounomiya-hadakamaturi.jpg','https://ja.wikipedia.org/wiki/%E5%9B%BD%E5%BA%9C%E5%AE%AE%E3%81%AF%E3%81%A0%E3%81%8B%E7%A5%AD',NULL,95,'drafted','## 概要

国府宮はだか祭り（こうのみやはだかまつり）は、愛知県稲沢市の尾張大国霊神社（おわりおおくにたまじんじゃ・通称「国府宮」）で毎年旧暦1月13日（現行暦の2月上旬から中旬）に開催される、約1,250年の歴史を持つ厄除け神事である。正式名称は「儺追神事（なおいしんじ）」で、神男（しんおとこ）と呼ばれる選ばれた男性に厄を移して払い清めるため、数千人の裸の男たちが「儺追笹」を奉納する勇壮な伝統祭礼である。

## 歴史

国府宮はだか祭りの起源は奈良時代の神護景雲元年（767年）に遡るとされ、称徳天皇の勅命により全国の国分寺で厄除けの儺追神事が行われたことに始まる。尾張国では国府宮が国府の鎮守として神事を引き継ぎ、平安期以降は地域の伝統行事として継承された。江戸期には尾張藩の支援のもと現在のような大規模な「裸祭り」の形態が確立し、数千人の男衆が褌姿で集結する独特の様式が定着した。明治期以降も地域住民の信仰と熱意により継承され、1991年に愛知県の無形民俗文化財に指定された。

## 見どころ

祭りの中心は午後3時頃から始まる「儺追神事」で、約9,000人もの裸の男たち（褌のみの姿）が尾張大国霊神社の参道や境内を埋め尽くす。神男に触れることで厄を移すことができるとされ、男衆は神男のもとへと殺到し、激しい揉み合いを繰り広げる。前日には「直会祭」、当日朝には「儺追笹奉納」、夜には「夜儺追神事」と神男の追放儀礼が行われ、3日間にわたって厳粛な神事と熱狂的な裸祭りが交錯する。冬の寒さの中、男たちの白い息と熱気が立ち上る光景は圧巻である。

## 開催情報・アクセス

会場は尾張大国霊神社（愛知県稲沢市国府宮1-1-1）。名鉄名古屋本線国府宮駅から徒歩約3分。観覧は無料。日程は旧暦1月13日（毎年2月上旬から中旬の特定日）。参加には事前申込みと褌・地下足袋着用が必要。

## 周辺観光

稲沢市内には国府宮神社のほか、性海寺（あじさい寺として有名）、矢合観音、稲沢サボテンの里など地域観光資源が点在する。名古屋市中心部からも電車で約15分の好アクセスで、名古屋城・熱田神宮・徳川美術館・有松絞り、犬山城（国宝）など尾張地方の歴史観光と組み合わせた周遊が可能。','## Overview

The Kōnomiya Naked Festival (Kōnomiya Hadaka Matsuri) is a 1,250-year-old purification ritual held annually on the 13th day of the first lunar month (early to mid-February in the modern calendar) at Owari Ōkunitama Shrine (commonly known as Kōnomiya) in Inazawa City, Aichi Prefecture. Officially named the "Naoi Shinji" (Evil-Chasing Ritual), the festival features thousands of nearly-naked men offering "Naoi-zasa" bamboo branches to transfer their misfortunes onto a specially chosen "Shin-otoko" (Sacred Man), creating one of Japan''s most dynamic and ancient traditional festivals.

## History

The origins of the Kōnomiya Naked Festival trace back to 767 (Jingo-keiun 1) during the Nara period, when Empress Shōtoku issued an imperial edict ordering Naoi purification rituals at all provincial temples across the country. In Owari Province, Kōnomiya inherited these rituals as the guardian shrine of the provincial government, and from the Heian period onward, the festival was preserved as a traditional regional event. During the Edo period, with the support of the Owari Domain, the festival took on its current large-scale "naked festival" form, in which thousands of men gather wearing only loincloths. The festival continued through the Meiji era thanks to the faith and dedication of local residents, and was designated as an Intangible Folk Cultural Property of Aichi Prefecture in 1991.

## Highlights

The festival''s central event is the "Naoi Shinji" beginning around 3 p.m., when approximately 9,000 nearly-naked men (wearing only loincloths) fill the approach and precincts of Owari Ōkunitama Shrine. By touching the Shin-otoko (Sacred Man), participants believe they can transfer their misfortunes onto him, and the men surge toward the Shin-otoko in fierce jostling. The day before features a "Naorai-sai" (Communion Festival), the festival morning includes the "Naoi-zasa Hōnō" (Bamboo Offering), and the night brings the "Yoru-Naoi Shinji" expulsion ritual for the Shin-otoko, with three days of solemn rites and fervent naked festival intertwined. The sight of white breath and heat rising from the men amid winter cold creates a truly overwhelming spectacle.

## Event Details and Access

The venue is Owari Ōkunitama Shrine (1-1-1 Kōnomiya, Inazawa City, Aichi Prefecture). Access is approximately 3 minutes on foot from Kōnomiya Station on the Meitetsu Nagoya Main Line. Viewing is free of charge. The date corresponds to the 13th day of the first lunar month (a specific date from early to mid-February each year). Participation requires advance application and the wearing of a loincloth and jika-tabi traditional footwear.

## Surrounding Attractions

Inazawa City features Kōnomiya Shrine alongside other local attractions including Shōkai-ji Temple (famous as the "Hydrangea Temple"), Yagose Kannon, and the Inazawa Cactus Village. Conveniently located approximately 15 minutes by train from central Nagoya City, the area allows for combined tours with major Owari region historical attractions including Nagoya Castle, Atsuta Shrine, the Tokugawa Art Museum, the Arimatsu Shibori dyeing district, and Inuyama Castle (a National Treasure), making it an ideal destination for exploring the rich heritage of the Owari region.','konomiya-hadaka-matsuri','konomiya-hadaka-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135500952','石清水八幡宮例祭','Iwashimizu Hachimangu Annual Festival',NULL,NULL,'Q710098','石清水八幡宮','Iwashimizu Hachimangū',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136779585','棚野の千両祭',NULL,'諏訪神社（南丹市）の祭礼',NULL,'Q6417767','北桑田郡','Kitakuwada district',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%A3%9A%E9%87%8E%E3%81%AE%E5%8D%83%E4%B8%A1%E7%A5%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136679543','アルバルク肉祭り',NULL,'2025年11月1日と11月2日にTOYORA ARENA TOKYOで開催予定のイベント',NULL,'Q131801357','TOYOTA ARENA TOKYO','TOYOTA ARENA TOKYO',NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q137803901','小正月','koshōgatsu','日本の正月15日の行事','former Japanese festival traditionally celebrating the first full moon of the new year',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'winter',NULL,'https://ja.wikipedia.org/wiki/%E5%B0%8F%E6%AD%A3%E6%9C%88',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135195174','多岐神社（合祀）','Co-Enshrinement of Takino Shrine',NULL,'A candidate shrine for Takino shrine',NULL,NULL,NULL,'新潟県','chubu',38.184118,139.499643,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136129904',NULL,'Rainbow Festa',NULL,'Pride festival in Osaka, Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q138854437','遠州横須賀凧揚げまつり','Enshu Yokosuka Kite Festival','静岡県掛川市の祭典','festival in Kakegawa City, Shizuoka Prefecture, Japan','Q823988','掛川市','Kakegawa','静岡県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Takoage%202018%2020180204%202.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q137910804','横濱漢祭 2026','Yokohama Otoko Matsuri 2026','2026年8月18日から8月20日まで横浜スタジアムで開催予定のイベント',NULL,'Q1148681','横浜スタジアム','Yokohama Stadium','神奈川県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135195110','中山神社（合祀）','Co-Enshrinement of Utsurahashino Shrine',NULL,'A candidate shrine for Utsurahashino shrine',NULL,NULL,NULL,'新潟県','chubu',37.730386,139.133407,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136657289','岩村町秋祭行事',NULL,'岐阜県恵那市で行われる祭礼',NULL,'Q819653','恵那市','Ena','岐阜県','chubu',NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E5%B2%A9%E6%9D%91%E7%94%BA%E7%A7%8B%E7%A5%AD%E8%A1%8C%E4%BA%8B',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135197944','（合祀）御崎神社','Co-Enshrinement of Kamishimano Shrine',NULL,'A candidate shrine for Kamishimano shrine',NULL,NULL,NULL,'岡山県','chugoku',34.471092,133.526716,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194565','大洗磯崎神社','Oarai Isozaki Shrine',NULL,'Ronsha 4 of Ohoyamamitano Shrine',NULL,NULL,NULL,'福井県','chubu',35.989453,136.137926,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136294506','グランドオペラフェスティバル in Japan','Grand Opera Festival in Japan',NULL,'Japanese opera festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135746980','若宮神社例大祭','Wakamiya Jinja Reitaisai','静岡県掛川市の若宮神社の祭礼','festival by Wakamiya Jinja in Kakegawa City, Shizuoka Prefecture, Japan',NULL,NULL,NULL,'静岡県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Matsuri%20no%20Wa%20Wakamiya%20Jinja%20Reitaisai%201.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135197934','（合祀）大和神社','Nomatano Shrine Co-EnShrinement',NULL,'A candidate shrine for Nomatano shrine',NULL,NULL,NULL,'岡山県','chugoku',34.797334,133.702072,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136343885','木曽音楽祭','Kiso Music Festival',NULL,'music festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,1975,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9C%A8%E6%9B%BD%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136917504','みなとみらいスマートフェスティバル',NULL,'日本の神奈川県横浜市で開催される花火の打ち上げを中心としたイベント',NULL,NULL,NULL,NULL,'神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BF%E3%81%AA%E3%81%A8%E3%81%BF%E3%82%89%E3%81%84%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136512405','ル・ポン国際音楽祭','Le Pont International Music Festival',NULL,'music festival in Japan','Q424813','赤穂市','Ako',NULL,NULL,NULL,NULL,2007,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E8%B5%A4%E7%A9%82%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E7%A5%AD%20%E3%83%97%E3%83%AA%E3%82%B3%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%88%EF%BC%88%E8%B5%A4%E7%A9%82%E6%96%87%E5%8C%96%E4%BC%9A%E9%A4%A8%EF%BC%89%20-%20panoramio.jpg',NULL,NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136375503',NULL,'Midsummer Swimsuit Festival',NULL,'swimsuit festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Midsummer%20Swimsuit%20Festival%20%28July%203%2C%202025%29DSC%208424.jpg',NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135503328','春日若宮神社例祭','Kasuga Wakamiya Shrine Annual Festival',NULL,NULL,'Q135460037','春日若宮神社','Kasuga Wakamiya Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136544536','毎朝御拝','Maichō Gohai','近代以前の天皇が毎朝行っていた宮中祭祀',NULL,'Q134962448','石灰壇','Ishibai no Dan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%AF%8E%E6%9C%9D%E5%BE%A1%E6%8B%9D',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135500954','鶴岡八幡宮例祭','Tsurugaoka Hachimangu Annual Festival',NULL,NULL,'Q701403','鶴岡八幡宮','Tsurugaoka Hachimangū','山形県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136544543','毎朝御代拝','Maichō Godaihai','侍従が天皇の代わりに毎朝、宮中三殿に参拝する祭祀',NULL,'Q7797685','宮中三殿','Three Palace Sanctuaries',NULL,NULL,NULL,NULL,1871,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%AF%8E%E6%9C%9D%E5%BE%A1%E4%BB%A3%E6%8B%9D',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194683','（参考）足羽神社（合祀）','Co-Enshrinement of Tsuchinowano Shrine',NULL,'A candidate shrine for Tsuchinowano shrine',NULL,NULL,NULL,'石川県','chubu',36.058409,136.209573,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194742','（合祀）牧岡神社（足羽神社境内）','Co-Enshrinement of Hirawoka Shrine',NULL,'A candidate shrine for Hirawoka shrine',NULL,NULL,NULL,'石川県','chubu',36.058409,136.209573,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135206688','旧鎮座地','Kaden Shrine Former Site',NULL,'A candidate shrine for Kaden Shrine',NULL,NULL,NULL,'大阪府','kinki',34.521771,135.526366,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135500947','北野天満宮例祭','Kitano Shrine Annual Festival',NULL,NULL,'Q662176','北野天満宮','Kitano Tenmangū','京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135195742','氷川神社合祀三崎神社','Co-Enshrinement of Shishichino Shrine',NULL,'A candidate shrine for Shishichino shrine',NULL,NULL,NULL,'埼玉県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135989693','渋谷アオハル2.0祭 2025','SHIBUYA AOHARU 2.0 2025','2025年8月16日と17日に渋谷区立宮下公園で開催された「渋谷アオハル2.0祭」',NULL,'Q6884419','宮下公園','Miyashita Park','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E6%B8%8B%E8%B0%B7%E3%82%A2%E3%82%AA%E3%83%8F%E3%83%AB2.0%E7%A5%AD%202025%20%E6%B8%8B%E8%B0%B7%E5%8C%BA%E7%AB%8B%E5%AE%AE%E4%B8%8B%E5%85%AC%E5%9C%92%202025%E5%B9%B48%E6%9C%8816%E6%97%A5%E3%81%AE%E6%B8%8B%E8%B0%B7%20202508161737%20DSCN4907.jpg',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194703','清瀧神社（合祀）','Co-Enshrinement of Kuninariohonono Shrine',NULL,'A candidate shrine for Kuninariohonono shrine',NULL,NULL,NULL,'岐阜県','chubu',35.981848,136.480389,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194598','大虫神社相殿（合祀）','Co-Enshrinement of Ikatsuchi Shrine',NULL,'A candidate shrine for Ikatsuchi shrine',NULL,NULL,NULL,'福井県','chubu',35.901049,136.126531,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q138330871','KOBE MELLOW CRUISE','KOBE MELLOW CRUISE','神戸で開催される都市型野外音楽フェス','An urban outdoor music festival held in Kobe','Q109360212','GLION ARENA KOBE',NULL,NULL,NULL,NULL,NULL,2022,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/KOBE_MELLOW_CRUISE',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194736','春日神社（合祀）','Co-Enshrinement of Katakishino Shrine',NULL,'A candidate shrine for Katakishino shrine',NULL,NULL,NULL,'福井県','chubu',36.206842,136.143334,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135891628','マリーンズ夏祭','Marines Natsu Matsuri','2025年8月19日から8月31日までZOZOマリンスタジアムで開催予定のお祭り',NULL,'Q486192','千葉マリンスタジアム','ZOZO Marine Stadium',NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135500943','厳島神社例祭','Itsukushima Shrine Annual Festival',NULL,NULL,'Q191763','厳島神社','Itsukushima Shrine','広島県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135462387','白山媛神社・神明宮・琴平神社・合殿','Hakusan-hime Shinmei-gu Kotohira combined shrine','新潟県新潟市北区太郎代にある神社',NULL,NULL,NULL,NULL,'石川県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135195246','木積神社','Kitsumi Shrine',NULL,'Achieno Shrine (Ronsha 2)',NULL,NULL,NULL,'京都府','kinki',35.555344,135.134879,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135504616','文京あじさいまつり','Bunkyō Hydrangea Festival',NULL,NULL,'Q212713','文京区','Bunkyō-ku','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135195111','五泉八幡宮（合祀）','Co-Enshrinement of Utsurahashino Shrine Ronsha 2',NULL,'Ronsha 2 for Utsurahashino shrine',NULL,NULL,NULL,'新潟県','chubu',37.741771,139.173709,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135206826','幣久良神社 旧社地','Mitekurano Shrine former site',NULL,'The former shrine site of Mitekurano Shrine',NULL,NULL,NULL,'京都府','kinki',34.841295,135.55893,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135194764','（参考）神明宮（市ノ瀬神社に合祀）','Co-Enshrinement of Ketamikono Shrine',NULL,'A candidate shrine for Ketamikono shrine',NULL,NULL,NULL,'岐阜県','chubu',36.294888,136.363491,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135195244','（合祀）大虫神社','Omushi Shrine',NULL,'A candidate shrine for Achieno Shrine',NULL,NULL,NULL,'京都府','kinki',35.493501,135.117324,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q136847459','塩屋湾のウンガミ','Ungami of Shioya Bay','重要無形民俗文化財',NULL,'Q49391902','塩屋湾','Shioya Bay',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Dragon%20boat%20race%20held%20during%20Ungami%20of%20Shioya%20Bay%20202509%2005.jpg','https://ja.wikipedia.org/wiki/%E5%A1%A9%E5%B1%8B%E6%B9%BE%E3%81%AE%E3%82%A6%E3%83%B3%E3%82%AC%E3%83%9F',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q135195293','（合祀）溝谷神社','Co-Enshrinement of Nakuno Shrine',NULL,'A candidate shrine for Nakuno shrine',NULL,NULL,NULL,'京都府','kinki',35.655239,135.111312,NULL,NULL,NULL,NULL,NULL,NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q139800634','MARINES FOOD FESTIVAL 2026','MARINES FOOD FESTIVAL 2026','千葉ロッテマリーンズが2026年4月28日から5月17日まで千葉マリンスタジアム(ZOZOマリンスタジアム)で開催するフードフェス',NULL,'Q486192','千葉マリンスタジアム','ZOZO Marine Stadium',NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,NULL,NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q139695547','鶴見の田祭り','Tsurumi no Tamatsuri','神奈川県横浜市鶴見区の鶴見神社で行われる民俗芸能','folk performing art held at Tsurumi Shrine in Yokohama, Japan','Q11676163','鶴見神社','Tsurumi Shrine','神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tsurumi%20no%20Tamatsuri%20Kamezo%20Otsuru%202026.jpg','https://ja.wikipedia.org/wiki/%E9%B6%B4%E8%A6%8B%E3%81%AE%E7%94%B0%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11436695','大正天皇祭','Emperor Taishō Festival','昭和年間における先帝祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1927,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%AD%A3%E5%A4%A9%E7%9A%87%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11440004','大阪ヨーロッパ映画祭','Osaka European Film Festival',NULL,'film festival',NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E9%98%AA%E3%83%A8%E3%83%BC%E3%83%AD%E3%83%83%E3%83%91%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11481688','常陸國總社宮大祭','Hitachinokuni Soshagu Reitaisai',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B8%B8%E9%99%B8%E5%9C%8B%E7%B8%BD%E7%A4%BE%E5%AE%AE%E5%A4%A7%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11477022','島立裸まつり','Shimadachi Hadaka Matsuri',NULL,NULL,NULL,NULL,NULL,'長野県','chubu',36.2310354,137.9440724,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B3%B6%E7%AB%8B%E8%A3%B8%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11455993','富士山河口湖音楽祭','Mt. Fuji Kawaguchiko Music Festival','富士河口湖町を中心とした地域で毎年7・8月に開かれる音楽祭',NULL,NULL,NULL,NULL,'山梨県','chubu',NULL,NULL,2002,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%AF%8C%E5%A3%AB%E5%B1%B1%E6%B2%B3%E5%8F%A3%E6%B9%96%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11457147','富田の鯨船行事','Kujirabune Festival','三重県四日市市の行事',NULL,'Q85884751','鳥出神社','Toride Shrine','三重県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kujirabune01.jpg','https://ja.wikipedia.org/wiki/%E5%AF%8C%E7%94%B0%E3%81%AE%E9%AF%A8%E8%88%B9%E8%A1%8C%E4%BA%8B',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11476051','峠の国盗り綱引き合戦','Tōge no Kunitori Tsunahiki Gassen',NULL,NULL,'Q11393703','兵越峠','Hyogoshi Pass',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B3%A0%E3%81%AE%E5%9B%BD%E7%9B%97%E3%82%8A%E7%B6%B1%E5%BC%95%E3%81%8D%E5%90%88%E6%88%A6',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11447453','姫路ゆかたまつり','Himeji Yukata Matsuri',NULL,NULL,'Q11651657','長壁神社','Osakabe Shrine','兵庫県','kinki',NULL,NULL,1742,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Himeji%20Yukata%20Matsuri%202009p1%20003.jpg','https://ja.wikipedia.org/wiki/%E5%A7%AB%E8%B7%AF%E3%82%86%E3%81%8B%E3%81%9F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11437490','大淀祇園祭','Ōyodo Gion Matsuri',NULL,'festival in Meiwa, Mie prefecture, Japan',NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%B7%80%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11437523','大湊ネブタ','Ōminato Nebuta','青森県むつ市で行われるねぶた',NULL,'Q11437522','大湊','Ōminato','青森県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Ominatonebuta.jpg','https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%B9%8A%E3%83%8D%E3%83%96%E3%82%BF',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11442078','大黒流','Daikoku-nagare','博多祇園山笠や博多松囃子（博多どんたく）の運営における構成単位である流の一つ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E9%BB%92%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11462179','小樽雪あかりの路','Otaru Snow Light Path','北海道小樽市で開催される祭典',NULL,NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,1999,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Otaru%20Yuki%20Akari%20no%20Michi.jpg','https://ja.wikipedia.org/wiki/%E5%B0%8F%E6%A8%BD%E9%9B%AA%E3%81%82%E3%81%8B%E3%82%8A%E3%81%AE%E8%B7%AF',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11465777','山あげ祭','Yamaage Matsuri','栃木県那須烏山市の八雲神社例大祭の奉納行事',NULL,'Q137321824',NULL,'Yakumo Shrine','栃木県','kanto',NULL,NULL,1560,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/2014%20Yamaage%20Matsuri%2004.JPG','https://ja.wikipedia.org/wiki/%E5%B1%B1%E3%81%82%E3%81%92%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11454224','宮崎国際音楽祭','Miyazaki International Music Festival',NULL,NULL,'Q11454461','宮崎県立芸術劇場','Miyazaki Prefectural Arts Center','宮崎県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AE%AE%E5%B4%8E%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11440018','大阪三大夏祭り','Three Great Summer Festivals of Osaka','大阪府大阪市で開催される代表的な3つの夏祭り',NULL,NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E9%98%AA%E4%B8%89%E5%A4%A7%E5%A4%8F%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11450469','安城七夕まつり','Anjo Tanabata Festival','愛知県安城市の祭',NULL,NULL,NULL,NULL,'愛知県','chubu',34.959986,137.08716,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Anjo-Tanabata-Matsuri-2023-6.jpg','https://ja.wikipedia.org/wiki/%E5%AE%89%E5%9F%8E%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,95,'drafted','## 概要

安城七夕まつり（あんじょうたなばたまつり）は、愛知県安城市の中心市街地で毎年8月第1金曜日から3日間にわたって開催される、日本三大七夕まつりのひとつに数えられる夏祭りである。仙台七夕まつり（宮城県）、湘南ひらつか七夕まつり（神奈川県）と並ぶ規模を誇り、3日間で約100万人の来場者を集める。「願いごと、日本一。」を合言葉に、市民参加型の七夕飾りと願いごと短冊の数が日本一を目指す。

## 歴史

1954年（昭和29年）、安城商工会議所と地元商店街が中心となり、戦後復興と地域振興を目的に始められた。当初は商店街の販促イベントとしての色彩が強かったが、1980年代以降、市民参加型の七夕飾りコンテストや短冊奉納が定着し、現在の規模へと発展した。安城市は江戸時代から「日本デンマーク」と呼ばれる先進農業地帯として知られ、農産物の販売促進の場としても機能してきた。2018年からは「願いごと、日本一。」をスローガンに掲げ、短冊数日本一記録更新を目指す市民運動として定着している。

## 見どころ

メイン会場のJR安城駅から南へ伸びる「あんぞう本通り」「えきまえ通り」を中心に、約1,000本の竹笹に色とりどりの七夕飾りが施され、街全体が七夕装飾で埋め尽くされる。市民・企業・学校が手作りで競い合う飾りはクリエイティビティに満ち、毎年テーマを変えた巨大装飾が話題を呼ぶ。短冊奉納コーナーでは誰でも願いごとを書いて飾ることができ、累計奉納数は1日5万枚以上に達する。夜は灯籠とライトアップで幻想的な雰囲気となり、地元グルメの屋台も多数並ぶ。

## 開催情報

開催地は愛知県安城市のJR安城駅前から本通り商店街一帯。最寄駅はJR東海道本線「安城駅」徒歩すぐ。開催期間は毎年8月第1金曜日から日曜日までの3日間。観覧は無料。会場一帯は祭礼期間中歩行者天国となるため、公共交通機関の利用が推奨される。8月初旬の愛知は猛暑となるため、こまめな水分補給と日除け対策が必須。

## 周辺の見どころ

安城市は明治用水による先進農業の歴史を持ち、デンパーク（安城産業文化公園）では農と食をテーマにした体験ができる。隣接する刈谷市・岡崎市の歴史観光（岡崎城、八丁味噌の郷など）と組み合わせれば、三河地方の魅力を一日で堪能できる。名古屋市までもJR快速で約25分とアクセス良好。','## Overview

Anjo Tanabata Festival (安城七夕まつり) is a summer festival held annually over three days starting from the first Friday of August in the central district of Anjo City, Aichi Prefecture. Ranked as one of Japan''s three great Tanabata festivals — alongside Sendai Tanabata in Miyagi Prefecture and Shōnan Hiratsuka Tanabata in Kanagawa Prefecture — it attracts approximately one million visitors over its three days. Under the slogan "The Most Wishes in Japan" (願いごと、日本一), the festival aims to display the largest number of community-made Tanabata decorations and wish tanzaku (wish strips) in the country.

## History

The festival began in 1954 (Shōwa 29) as a postwar economic revitalization initiative led by the Anjo Chamber of Commerce and local shopping district associations. Initially serving primarily as a commercial promotion event, it gradually evolved into a community-driven festival from the 1980s, with the introduction of citizen-participatory decoration contests and wish-strip offerings. Anjo City has been known since the Edo period as "Japan''s Denmark" for its advanced agricultural development, and the festival also serves as a platform for promoting local agricultural products. Since 2018, the festival has adopted "The Most Wishes in Japan" as its slogan, becoming a community-wide effort to set and break records for the number of wish strips offered.

## Highlights

The main festival area runs along Anzō Honmichi-dōri and Ekimae-dōri, extending south from JR Anjo Station, where approximately 1,000 bamboo poles are adorned with colorful Tanabata decorations, transforming the entire downtown into a vast Tanabata installation. The decorations — handcrafted by citizens, businesses, and schools in friendly competition — are renowned for their creativity, with large themed installations drawing fresh attention each year. At wish-tanzaku booths, anyone can write and hang a wish strip, with daily offerings exceeding 50,000 strips. At night, lanterns and illuminations create a magical atmosphere, complemented by numerous local food stalls.

## Event Information

The venue is the area around JR Anjo Station and the Honmichi shopping street in central Anjo City, Aichi Prefecture. The nearest station is JR Anjo Station on the JR Tōkaidō Main Line, directly accessible on foot. The festival is held annually from the first Friday to Sunday of August. Admission is free. The festival area becomes a pedestrian zone during the event, so public transportation is strongly recommended. Early August in Aichi Prefecture is extremely hot, so frequent hydration and sun protection are essential.

## Nearby Attractions

Anjo City has a rich agricultural history rooted in the Meiji Canal irrigation system. Denpark (Anjo Industrial and Cultural Park) offers hands-on experiences themed around agriculture and food. Combined with the historic attractions of nearby Kariya City and Okazaki City — such as Okazaki Castle and the Hatchō Miso Village — visitors can experience the full appeal of the Mikawa region in a single day. Nagoya City is also easily accessible by JR rapid train in approximately 25 minutes.','anjo-tanabata-matsuri','anjo-tanabata-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11475377','岩漫','Ganman','1980年から2010年まで岩手県で開催されていた同人誌即売会',NULL,'Q11526702','東山堂','Tosando Corporation','岩手県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B2%A9%E6%BC%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11455969','富士宮まつり','Fujinomiya Festival',NULL,NULL,NULL,NULL,NULL,'静岡県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AF%8C%E5%A3%AB%E5%AE%AE%E7%A7%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11463659','小見川祇園祭','Omigawa Gion-sai',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B0%8F%E8%A6%8B%E5%B7%9D%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11464484','小鶴祇園祭','Kozuru Gion-sai',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B0%8F%E9%B6%B4%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11455990','富士山御神火まつり','Fujisan Gojinka Matsuri',NULL,NULL,'Q653180','富士山本宮浅間大社','Fujisan Hongū Sengen Taisha','山梨県','chubu',NULL,NULL,1984,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AF%8C%E5%A3%AB%E5%B1%B1%E5%BE%A1%E7%A5%9E%E7%81%AB%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11435600','大文字まつり','Odate Daimonji Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%96%87%E5%AD%97%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11466617','山口七夕ちょうちんまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B1%B1%E5%8F%A3%E4%B8%83%E5%A4%95%E3%81%A1%E3%82%87%E3%81%86%E3%81%A1%E3%82%93%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11467395','山口祇園祭','Yamaguchi Gion-sai',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B1%B1%E5%8F%A3%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11436847','大江戸花火まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%B1%9F%E6%88%B8%E8%8A%B1%E7%81%AB%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11436902','大池まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%B1%A0%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11438152','大石りくまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E7%9F%B3%E3%82%8A%E3%81%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11438548','大胡祇園まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E8%83%A1%E7%A5%87%E5%9C%92%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11457148','富田の石取祭','Tomida Ishidori Matsuri','三重県四日市市で開催される祭り',NULL,'Q11457136','富田地区','Tomida','三重県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tomida%20ishidori.JPG','https://ja.wikipedia.org/wiki/%E5%AF%8C%E7%94%B0%E3%81%AE%E7%9F%B3%E5%8F%96%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11438786','大蛇山 (祭り)',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E8%9B%87%E5%B1%B1_(%E7%A5%AD%E3%82%8A)',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11439837','大門曳山まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E9%96%80%E6%9B%B3%E5%B1%B1%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11442147','天ヶ須賀の石取祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A9%E3%83%B6%E9%A0%88%E8%B3%80%E3%81%AE%E7%9F%B3%E5%8F%96%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11449469','宇治川花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%AE%87%E6%B2%BB%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11452522','宝塚観光花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'兵庫県','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%AE%9D%E5%A1%9A%E8%A6%B3%E5%85%89%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11459287','小友祇園山笠',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B0%8F%E5%8F%8B%E7%A5%87%E5%9C%92%E5%B1%B1%E7%AC%A0',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11461220','小松祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B0%8F%E6%9D%BE%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11466745','山口天神祭',NULL,NULL,NULL,NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B1%B1%E5%8F%A3%E5%A4%A9%E7%A5%9E%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11442189','天下祭','Tenka Matsuri','日本の江戸時代以来続いている、江戸・東京の代表的な祭の総称',NULL,'Q717682','神田明神','Kanda-myōjin','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A9%E4%B8%8B%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11472992','岡崎観光夏まつり花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B2%A1%E5%B4%8E%E5%9F%8E%E4%B8%8B%E5%AE%B6%E5%BA%B7%E5%85%AC%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11477729','川内大綱引',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B7%9D%E5%86%85%E5%A4%A7%E7%B6%B1%E5%BC%95',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11477732','川内川花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B7%9D%E5%86%85%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11478929','川渡り神幸祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B7%9D%E6%B8%A1%E3%82%8A%E7%A5%9E%E5%B9%B8%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11479257','川越百万灯夏祭り',NULL,NULL,NULL,NULL,NULL,NULL,'埼玉県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B7%9D%E8%B6%8A%E7%99%BE%E4%B8%87%E7%81%AF%E5%A4%8F%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11458640','将門まつり','Masakado Matsuri','茨城県坂東市で行われる祭',NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,1972,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B0%86%E9%96%80%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11481774','幌武者行列',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B9%8C%E6%AD%A6%E8%80%85%E8%A1%8C%E5%88%97',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11439317','大送神社の綱引き','Ōsō Shrine Tug-of-War',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E9%80%81%E7%A5%9E%E7%A4%BE%E3%81%AE%E7%B6%B1%E5%BC%95%E3%81%8D',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11454559','宮崎神宮大祭','Miyazaki Shrine Grand Festival','宮崎県宮崎市で行われる宮崎神宮の例祭',NULL,'Q704686','宮﨑神宮','Miyazaki Jingū','宮崎県','kyushu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Miyazaki%20Shrine%20Grand%20Festival%20in%202008%20Gohouren%2001.jpg','https://ja.wikipedia.org/wiki/%E5%AE%AE%E5%B4%8E%E7%A5%9E%E5%AE%AE%E5%A4%A7%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11471288','岐阜まつり','Gifu Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B2%90%E9%98%9C%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11465749','層雲峡氷瀑まつり','Sōunkyō Icefall Festival','日本の北海道の祭り',NULL,NULL,NULL,NULL,'北海道','hokkaido',43.727138888,142.948777777,1976,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Souunkyouhyoubakumatsuri.jpg','https://ja.wikipedia.org/wiki/%E5%B1%A4%E9%9B%B2%E5%B3%A1%E6%B0%B7%E7%80%91%E3%81%BE%E3%81%A4%E3%82%8A',NULL,95,'drafted','## 概要

層雲峡氷瀑まつり（そううんきょうひょうばくまつり）は、北海道上川郡上川町の層雲峡温泉で毎年1月下旬から3月中旬にかけて開催される、大雪山系の冬を代表する氷の祭典である。石狩川河川敷を会場に、巨大な氷のオブジェ・氷のトンネル・氷の神社などが造営され、夜間はライトアップによって幻想的な氷の世界が出現する。期間中の来場者は約20万人に達する、北海道の冬の風物詩のひとつである。

## 歴史

1976年（昭和51年）に層雲峡温泉観光協会が主催する冬季イベントとして始まった。当時、冬の温泉地集客を目的に小規模な氷のオブジェを設置したのが起源で、1980年代以降、地元住民と職人が手作りで巨大化を進め、現在の大規模氷瀑会場へと発展した。2007年からは「氷瀑神社」や「氷のトンネル」など参加型展示が増え、SNS映え時代の到来とともに国内外からの観光客が急増。2010年代には台湾・中国・東南アジアからのインバウンド層にも認知が広がった。

## 見どころ

会場最大の見どころは、高さ約15メートルの「氷瀑タワー」群と、内部を歩ける「氷のトンネル」である。氷柱と雪のブロックを組み上げた巨大構造物が、夜になると赤・青・緑のカラフルなライトに照らされ、まるで異世界の城のような景観を生み出す。氷の神社では絵馬を奉納でき、氷のバーでは限定の氷のグラスでカクテルを楽しめる（要予約）。毎週土曜日には花火大会も開催され、氷瀑と冬の夜空が彩られる。

## 開催情報

開催地は北海道上川郡上川町層雲峡温泉・石狩川河川敷特設会場。最寄駅はJR石北本線「上川駅」からバスで約30分（層雲峡温泉行き）。開催期間は毎年1月下旬から3月中旬まで（約7週間）。点灯時間は17:00〜21:30。入場料は協力金として中学生以上500円程度。氷点下20度以下になる極寒地のため、ダウンジャケット・厚手帽子・手袋・スノーブーツの完全装備が必須。

## 周辺の見どころ

層雲峡温泉は大雪山国立公園の玄関口に位置し、火山活動による壮大な柱状節理の渓谷美で知られる。氷瀑まつりに合わせて、徒歩圏内の「銀河の滝」「流星の滝」（日本の滝百選）も冬期は氷瀑となり訪問者を魅了する。黒岳ロープウェイで標高1,300メートルまで上がれば、雪山と樹氷の絶景が広がる。旭川市内まで車で約90分、旭山動物園との組み合わせも人気である。','## Overview

Sōunkyō Icefall Festival (層雲峡氷瀑まつり) is a winter ice festival held annually from late January to mid-March at Sōunkyō Onsen in Kamikawa Town, Kamikawa District, Hokkaido. Staged along the banks of the Ishikari River, the festival features massive ice sculptures, ice tunnels, and an ice shrine, illuminated at night to create a magical frozen world. Drawing approximately 200,000 visitors during its seven-week run, it is one of Hokkaido''s iconic winter attractions in the Daisetsuzan mountain range.

## History

The festival began in 1976 (Shōwa 51) as a winter event organized by the Sōunkyō Onsen Tourism Association. Originally consisting of small ice sculptures aimed at attracting winter visitors to the hot-spring town, it was gradually expanded from the 1980s by local craftsmen and residents who built ever-larger handmade structures, eventually developing into today''s grand ice-spectacle venue. Since 2007, interactive installations such as the Icefall Shrine and Ice Tunnel have been added, and with the rise of social media in the 2010s, the festival has seen explosive growth in inbound visitors from Taiwan, China, and Southeast Asia.

## Highlights

The festival''s centerpiece is a cluster of approximately 15-meter-tall ice towers and walk-through ice tunnels — massive structures built from ice pillars and snow blocks that, when illuminated at night with red, blue, and green lighting, evoke a fantastical otherworldly castle. Visitors can offer ema (wooden prayer plaques) at the Icefall Shrine and enjoy cocktails in special ice glasses at the Ice Bar (reservations required). Fireworks are launched every Saturday night, painting the winter sky above the ice formations.

## Event Information

The venue is the special site along the Ishikari River at Sōunkyō Onsen in Kamikawa Town, Kamikawa District, Hokkaido. The nearest station is Kamikawa Station on the JR Sekihoku Main Line, followed by an approximately 30-minute bus ride bound for Sōunkyō Onsen. The festival runs annually from late January to mid-March (about seven weeks). Illumination hours are from 5:00 PM to 9:30 PM. A cooperation fee of approximately 500 yen is requested for junior high school students and older. As temperatures regularly drop below −20°C, full winter gear — heavy down jacket, thick hat, gloves, and snow boots — is absolutely essential.

## Nearby Attractions

Sōunkyō Onsen sits at the gateway to Daisetsuzan National Park, renowned for its dramatic columnar jointed cliffs formed by volcanic activity. Two of Japan''s Top 100 Waterfalls — Ginga-no-Taki (Milky Way Falls) and Ryūsei-no-Taki (Shooting Star Falls) — are within walking distance and transform into frozen icefalls during the festival period. The Kurodake Ropeway carries visitors up to 1,300 meters, where breathtaking views of snow-covered peaks and rime-frosted trees await. Asahikawa City is approximately 90 minutes away by car, and combining the visit with Asahiyama Zoo is a popular itinerary.','sounkyo-hyobaku-matsuri','sounkyo-hyobaku-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11481932','平七夕まつり','Taira Tanabata Matsuri','福島県いわき市平で、毎年8月6日から8日にかけて行われる七夕祭',NULL,NULL,NULL,NULL,'福島県','tohoku',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%84%E3%82%8F%E3%81%8D%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11447740','婿投げ・墨塗り','Mukonage and Suminuri','新潟県十日町市松之山温泉で毎年1月15日に行われる小正月の伝統行事','Little New Year event in Matsunoyama Onsen, Tokamachi, Niigata, Japan','Q11529038','松之山温泉','Matsunoyama Onsen','新潟県','chubu',37.0642688,138.5967298,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Mukonage%20Matsunoyama%202026.jpg','https://ja.wikipedia.org/wiki/%E5%A9%BF%E6%8A%95%E3%81%92%E3%83%BB%E5%A2%A8%E5%A1%97%E3%82%8A',NULL,95,'drafted','## 概要

婿投げ・墨塗り（むこなげ・すみぬり）は、新潟県十日町市松之山温泉で毎年1月15日（小正月）に執り行われる、日本三大奇祭のひとつに数えられる伝統行事である。前年に松之山地区の女性と結婚した婿を、温泉街の薬師堂前の崖から雪の斜面に投げ落とす「婿投げ」と、参加者全員が顔に墨を塗り合う「墨塗り」が連続して行われ、夫婦円満と地域の幸せを祈願する。

## 歴史

起源は約300年前の江戸時代中期に遡るとされ、地域外から嫁を奪っていった婿への報復・通過儀礼として始まったと伝えられる。豪雪地帯である松之山では、冬の厳しい暮らしの中で地域の結束を強める年中行事として定着し、明治以降も住民の手で大切に守り継がれてきた。墨塗りは、墨を塗り合うことで前年の厄を落とし、新年の無病息災を祈る意味があるとされる。新潟県の無形民俗文化財に指定されている。

## 見どころ

午後2時頃から薬師堂前で「婿投げ」が始まる。前年に松之山に嫁いだ女性の夫が、地元の若衆によって雪の積もった崖（高さ約5メートル）から豪快に投げ落とされる。投げられた婿は雪まみれになりながらも笑顔で立ち上がり、観客から拍手喝采を浴びる。続く「墨塗り」では、賽の神（さいのかみ）と呼ばれる雪上の祭壇で燃やされた門松や注連縄の灰と雪を混ぜた墨を、参加者同士が顔に塗り合う。観光客も自由に参加でき、地元住民との一体感を体験できる。

## 開催情報

開催地は新潟県十日町市松之山湯本（松之山温泉街・薬師堂前）。最寄駅はほくほく線「まつだい駅」からバスで約25分。開催日は毎年1月15日（固定）。婿投げは14:00頃から、墨塗りは引き続き15:00頃まで。観覧は無料。雪上での開催のため防寒具・防水靴・スキーウェア等の完全装備が必須。墨塗りに参加する場合は汚れてもよい服装で。

## 周辺の見どころ

松之山温泉は日本三大薬湯のひとつに数えられ、塩分濃度の高い高張性温泉として知られる。湯治と祭り観覧を組み合わせた冬の旅程が人気である。周辺には越後妻有アート・トリエンナーレの作品群が点在し、「最後の真冬の田園美術館」とも呼ばれる豪雪地の景観美が広がる。十日町雪まつり（2月）と日程を合わせれば、雪国文化を深く体感できる。','## Overview

Mukonage and Suminuri (婿投げ・墨塗り) is one of Japan''s three most unusual festivals (Nihon san-kisai), held annually on January 15 (Koshōgatsu, or "Little New Year") at Matsunoyama Onsen in Tōkamachi City, Niigata Prefecture. The event consists of two consecutive rituals: Mukonage ("groom-throwing"), in which men who married into the Matsunoyama community during the previous year are hurled from a cliff onto a snowy slope, and Suminuri ("ink-smearing"), in which all participants smear black soot on each other''s faces — both performed to pray for marital harmony and the prosperity of the community.

## History

The festival is said to have originated approximately 300 years ago in the mid-Edo period as a form of rite of passage — and good-natured retribution — for grooms who had taken brides away from the community. In the heavy-snow region of Matsunoyama, it became established as an annual event reinforcing communal bonds during the harsh winters, and has been carefully preserved by local residents since the Meiji era. The ink-smearing portion is said to ward off the misfortunes of the previous year and pray for good health in the new year. The festival is designated as an Intangible Folk Cultural Property of Niigata Prefecture.

## Highlights

Around 2:00 PM, Mukonage begins in front of Yakushidō Hall. Husbands who married into Matsunoyama in the previous year are vigorously thrown by local young men from a snow-covered cliff approximately 5 meters high. The grooms emerge from the snow grinning, to cheers and applause from the crowd. Suminuri follows immediately afterward: ink made by mixing snow with the ashes of burned New Year decorations (kadomatsu and shimenawa) from the sai-no-kami snow altar is smeared on the faces of all participants. Tourists are welcome to join, creating a remarkable sense of unity with local residents.

## Event Information

The venue is in front of Yakushidō Hall on the main street of Matsunoyama Onsen, Yumoto, Tōkamachi City, Niigata Prefecture. The nearest station is Matsudai Station on the Hokuhoku Line, followed by a 25-minute bus ride. The festival is held annually on January 15. Mukonage begins around 2:00 PM, and Suminuri continues until about 3:00 PM. Admission is free. As the event takes place on snow in midwinter, full winter gear — warm clothing, waterproof footwear, and ski wear — is essential. Those joining the ink-smearing should wear clothes that can get stained.

## Nearby Attractions

Matsunoyama Onsen is ranked as one of Japan''s three great medicinal hot springs, known for its highly saline, hypertonic waters. Combining the festival with a hot-spring retreat is a popular winter itinerary. The surrounding area is home to numerous installations from the Echigo-Tsumari Art Triennale, often called "the world''s final deep-winter open-air art museum" thanks to its stunning snow-covered landscapes. Visitors who time their trip with the Tōkamachi Snow Festival in February can experience the depth of Japan''s snow country culture.','mukonage-suminuri','mukonage-suminuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11475588','岩船大祭',NULL,'新潟県村上市の祭事',NULL,NULL,NULL,NULL,'新潟県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B2%A9%E8%88%B9%E5%A4%A7%E7%A5%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11475809','岸和田十月祭礼',NULL,'大阪府岸和田市の6地区で行われるだんじり祭の総称',NULL,NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B2%B8%E5%92%8C%E7%94%B0%E5%8D%81%E6%9C%88%E7%A5%AD%E7%A4%BC',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11462952','小田原北條五代祭り','Odawara Hōjō Godai Festival','神奈川県小田原市の伝統的な祭り',NULL,'Q267258','小田原市','Odawara','神奈川県','kanto',NULL,NULL,1965,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/HJ5SH1.JPG','https://ja.wikipedia.org/wiki/%E5%B0%8F%E7%94%B0%E5%8E%9F%E5%8C%97%E6%A2%9D%E4%BA%94%E4%BB%A3%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11471245','山鹿灯籠まつり','Yamaga Lantern Festival',NULL,NULL,NULL,NULL,NULL,'熊本県','kyushu',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E5%8D%83%E4%BA%BA%E7%87%88%E7%B1%A0%E8%88%9E.jpg','https://ja.wikipedia.org/wiki/%E5%B1%B1%E9%B9%BF%E7%81%AF%E7%B1%A0%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11459006','小倉祇園太鼓','Kokura Gion Daiko','北九州市小倉北区で行なわれる祭',NULL,'Q11390696','八坂神社','Yasaka Shrine','京都府','kinki',NULL,NULL,1618,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kokura%20Gion%20Suedaiko.JPG','https://ja.wikipedia.org/wiki/%E5%B0%8F%E5%80%89%E7%A5%87%E5%9C%92%E5%A4%AA%E9%BC%93',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11447411','姫島盆踊り','Himeshima Bon odori',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%A7%AB%E5%B3%B6%E7%9B%86%E8%B8%8A%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11455045','宮津祭','Miyazu Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AE%AE%E6%B4%A5%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11454119','宮島水中花火大会','Miyajima Water Fireworks Festival',NULL,NULL,NULL,NULL,NULL,'広島県','chugoku',NULL,NULL,1971,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%AE%AE%E5%B3%B6%E6%B0%B4%E4%B8%AD%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24877085','梅宮神社の甘酒祭り',NULL,NULL,NULL,NULL,NULL,NULL,'埼玉県','kanto',35.87416667,139.41944444,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%A2%85%E5%AE%AE%E7%A5%9E%E7%A4%BE%E3%81%AE%E7%94%98%E9%85%92%E7%A5%AD%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22125537','能見神明宮大祭','Nomi Shinmeigū Festival',NULL,NULL,'Q242783','岡崎市','Okazaki','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%83%BD%E8%A6%8B%E7%A5%9E%E6%98%8E%E5%AE%AE%E5%A4%A7%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24861794','百万石音楽祭〜ミリオンロックフェスティバル〜',NULL,NULL,NULL,'Q191130','金沢市','Kanazawa','石川県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%99%BE%E4%B8%87%E7%9F%B3%E9%9F%B3%E6%A5%BD%E7%A5%AD%E3%80%9C%E3%83%9F%E3%83%AA%E3%82%AA%E3%83%B3%E3%83%AD%E3%83%83%E3%82%AF%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB%E3%80%9C',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q27926875','KYOTO EXPERIMENT','KYOTO EXPERIMENT','舞台芸術祭','festival','Q34600','京都市','Kyoto','京都府','kinki',NULL,NULL,2010,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/KYOTO_EXPERIMENT',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22120521','三宅神社','Miyake Shrine','三重県鈴鹿市国府町にある神社','shrine in Suzuka, Mie',NULL,NULL,NULL,'三重県','kinki',34.854431,136.507187,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Miyake-jinja%20%28Kou-cho%2C%20Suzuka%29%20haiden.JPG','https://ja.wikipedia.org/wiki/%E4%B8%89%E5%AE%85%E7%A5%9E%E7%A4%BE_(%E9%88%B4%E9%B9%BF%E5%B8%82%E5%9B%BD%E5%BA%9C%E7%94%BA)',NULL,95,'drafted','## 概要

三宅神社（みやけじんじゃ）は、三重県鈴鹿市国府町（こうちょう）に鎮座する式内社で、大彦命（おおひこのみこと）を主祭神として祀る古社である。『延喜式神名帳』に記載される伊勢国鈴鹿郡の式内社の一座で、古代豪族・三宅連（みやけのむらじ）との結びつきと、伊勢国府推定地に隣接する立地で知られる。

## 歴史

三宅神社は『延喜式神名帳』（927年）に式内社として記載されており、創建年代は不詳ながら少なくとも平安時代以前に遡る古社である。主祭神の大彦命は『古事記』『日本書紀』において第8代孝元天皇の皇子で、四道将軍の一人として北陸道を平定した皇族として記される。その子孫が三宅連を名乗り、ヤマト政権の屯倉（みやけ・直轄領）管理を司ったとされる。鎮座地の鈴鹿市国府町一帯は伊勢国府の所在地と推定される古代地名で、国府の鎮守として機能した可能性が高く、律令期から朝廷の崇敬を受けた古社として継承されてきた。

## 見どころ

社殿は近世以降の建築様式を残し、深い杜に囲まれた境内には古代の聖域の名残が感じられる。伊勢国府推定地に隣接する立地から、考古学・古代史研究の観点でも注目される。境内には三宅連ゆかりの祭神を象徴する文物や、地域の郷土史を語る石碑が残されている。例祭は秋季10月で、地元氏子による神事と神楽奉納が行われる。

## 開催情報・アクセス

近鉄鈴鹿線平田町駅から車・タクシーで約10分。境内参拝は終日自由。秋季例祭は毎年10月に執り行われる。

## 周辺観光

鈴鹿市は鈴鹿サーキットで有名なモータースポーツの聖地として国際的に知られる。椿大神社（猿田彦大本宮）、伊勢国分寺跡、加佐登神社など、伊勢国西部の古代史を語る古社・史跡が集中する。亀山市・関宿の伝統的町並み、菰野町の湯の山温泉、四日市港など、北勢地域の観光資源と組み合わせた周遊が可能。','## Overview

Miyake Shrine (Miyake Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Kō-chō, Suzuka City, Mie Prefecture. The shrine enshrines Ōhiko no Mikoto as its principal deity. As one of the Engishiki-registered shrines of Suzuka District in Ise Province, it is known for its connection to the ancient Miyake no Muraji clan and its location adjacent to the presumed site of the Ise Provincial Government Office.

## History

Miyake Shrine is recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. Although the founding date is unknown, its existence as an ancient shrine reaches back at least to before the Heian period. The principal deity Ōhiko no Mikoto is recorded in the Kojiki and Nihon Shoki as a son of the eighth emperor Kōgen and as one of the Shidō Shōgun (Four-Road Generals) who pacified the Hokurikudō region. His descendants took the name Miyake no Muraji and are said to have served the Yamato court by managing the miyake (directly controlled territories of the imperial government). The shrine''s location in the Kō-chō district of Suzuka City corresponds to the presumed site of the Ise Provincial Government Office, suggesting the shrine likely functioned as a guardian shrine of the provincial government and has been transmitted as an ancient shrine receiving imperial court veneration since the Ritsuryō period.

## Highlights

The main shrine hall preserves the architectural style from the early-modern period onward, and the precincts enclosed by deep forest convey the lingering presence of an ancient sacred site. The location adjacent to the presumed Ise Provincial Government Office site attracts attention from the perspectives of archaeology and ancient historical research. Within the precincts remain artifacts symbolizing the deities associated with the Miyake no Muraji clan and stone monuments narrating local regional history. The annual main festival is held in October and features sacred rituals and dedicatory kagura sacred dance performances by local parishioners.

## Event Details and Access

The shrine is accessible by car or taxi in approximately 10 minutes from Hirata-chō Station on the Kintetsu Suzuka Line. The precincts are open for worship throughout the day. The autumn main festival is held in October each year.

## Surrounding Attractions

Suzuka City is internationally renowned as a motor sports mecca, home to the famous Suzuka Circuit racetrack. The area features a concentration of ancient shrines and historical sites narrating the ancient history of western Ise Province, including Tsubaki Grand Shrine (Sarutahiko Daihongū), the ruins of the Ise Provincial Temple, and Kasado Shrine. Combined sightseeing tours are possible incorporating the traditional townscape of Kameyama City and Seki-juku, the Yunoyama Hot Spring resort in Komono Town, and Yokkaichi Port, allowing visitors to explore the diverse tourism resources of the Hokusei region.','miyake-jinja-suzuka','miyake-jinja-suzuka',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22124175','文京つつじまつり','Bunkyō Azalea Festival',NULL,NULL,'Q335612','根津神社','Nezu Shrine',NULL,NULL,NULL,NULL,1969,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Nezu-jinja-3.jpg','https://ja.wikipedia.org/wiki/%E6%96%87%E4%BA%AC%E3%81%A4%E3%81%A4%E3%81%98%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30922504','きさわ樹氷まつり','Kisawa Juhyō Matsuri',NULL,'festival','Q11519197','木沢村','Kisawa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8D%E3%81%95%E3%82%8F%E6%A8%B9%E6%B0%B7%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24896695','姥神大神宮渡御祭','Ubagami Daijingū Togyosai','北海道江差町にある姥神大神宮の例大祭',NULL,NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E7%A5%9E%E8%BC%BF%E6%B8%A1%E5%BE%A11.jpg','https://ja.wikipedia.org/wiki/%E5%A7%A5%E7%A5%9E%E5%A4%A7%E7%A5%9E%E5%AE%AE%E6%B8%A1%E5%BE%A1%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24875391','鹿沼今宮神社祭の屋台行事','Kanuma lmamiya Shrine Festival','栃木県鹿沼市で行われる祭り',NULL,'Q110734894','今宮神社','Imamiya Shrine','栃木県','kanto',NULL,NULL,1608,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kanumaimamiyayatai.jpg','https://ja.wikipedia.org/wiki/%E9%B9%BF%E6%B2%BC%E4%BB%8A%E5%AE%AE%E7%A5%9E%E7%A4%BE%E7%A5%AD%E3%81%AE%E5%B1%8B%E5%8F%B0%E8%A1%8C%E4%BA%8B',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654535','古川まつり','Furukawa Matsuri','宮城県大崎市で開催される夏祭り',NULL,NULL,NULL,NULL,'宮城県','tohoku',38.57514167,140.95970556,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8F%A4%E5%B7%9D%E3%81%BE%E3%81%A4%E3%82%8A',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24885401','京都国際映画祭','Kyoto international film and art festival','日本の京都市で開催される映画祭',NULL,'Q34600','京都市','Kyoto','京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E5%9B%BD%E9%9A%9B%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22130293','浦和まつり','Urawa Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B5%A6%E5%92%8C%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24876853','松上げ','Matsuage',NULL,NULL,'Q384981','おおい町','Oi',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E4%B8%8A%E3%81%92',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28685070','松山秋祭り','Matsuyama Aki Matsuri',NULL,NULL,NULL,NULL,NULL,'愛媛県','shikoku',NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E5%B1%B1%E7%A7%8B%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28689385','男鹿ナマハゲロックフェスティバル',NULL,NULL,NULL,'Q633935','男鹿市','Oga','秋田県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%94%B7%E9%B9%BF%E3%83%8A%E3%83%9E%E3%83%8F%E3%82%B2%E3%83%AD%E3%83%83%E3%82%AF%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22127131','ひょうげ祭り','Hyōge Matsuri','香川県高松市（旧香川町）に伝わる民俗芸能','festival in Takamatsu, Japan',NULL,NULL,NULL,'香川県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%B2%E3%82%87%E3%81%86%E3%81%92%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28691802','丸岡古城まつり','Maruoka Kojō Matsuri','福井県坂井市で開催される祭り',NULL,'Q1143892','丸岡城','Maruoka Castle','福井県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%B8%E5%B2%A1%E5%8F%A4%E5%9F%8E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24887619','入谷朝顔まつり','Iriya Asagao festival','入谷鬼子母神とその界隈で開催される朝顔祭り',NULL,'Q11583299','真源寺','Shingen-ji Temple','東京都','kanto',35.71988889,139.78268889,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Iriyaasagaomatsuri-tag-july8-2016.jpg','https://ja.wikipedia.org/wiki/%E5%85%A5%E8%B0%B7%E6%9C%9D%E9%A1%94%E3%81%BE%E3%81%A4%E3%82%8A',NULL,95,'drafted','## 概要

入谷朝顔まつり（いりやあさがおまつり）は、東京都台東区下谷の入谷鬼子母神（真源寺）境内およびその周辺の言問通り沿いで、毎年7月6日から8日にかけて開催される朝顔の市である。江戸の風物詩として明治期に始まり、東京都内最大の朝顔市として広く親しまれ、約60万人の来場者を集める下町の夏の風物詩である。

## 歴史

入谷の朝顔は江戸末期から明治期にかけて、入谷一帯の植木屋が栽培した変化朝顔（へんかあさがお）で全国的に名を馳せた。当時の入谷は江戸郊外の田園地帯で、ヘチマ・ヒョウタン・朝顔などの園芸植物の生産地として栄えていた。明治13年（1880年）頃から入谷鬼子母神を中心に朝顔市が立つようになり、変化朝顔の珍品奇種を求める愛好家で賑わった。第二次世界大戦中の一時中断を経て、1948年（昭和23年）に地元商店街・植木組合の尽力で復活、以降毎年7月6-8日の3日間に定着し、台東区の指定無形文化財に登録されている。

## 見どころ

期間中は約120軒の朝顔業者と100軒の露店が言問通り沿いに軒を連ね、朝早朝5時頃から夜23時頃まで賑わう。並ぶ朝顔は伝統的な大輪朝顔、団十郎（赤茶色）、団十郎黒、変化朝顔の貴重種など多彩で、1鉢2,000円前後から購入可能。入谷鬼子母神では参拝者で行列ができ、朝顔をモチーフにした団扇・絵馬・お守りも頒布される。地元商店街の屋台料理、伝統工芸品の露店も人気。

## 開催情報・アクセス

会場は入谷鬼子母神（真源寺・東京都台東区下谷1-12-16）および周辺言問通り沿い。地下鉄日比谷線入谷駅から徒歩約1分、JR山手線鶯谷駅から徒歩約7分。観覧・入場は無料。開催時間は7月6-8日の3日間、早朝5時頃から夜23時頃まで。

## 周辺観光

下町情緒の濃い台東区一帯は浅草寺・浅草神社・仲見世通り・浅草演芸ホール、上野公園・東京国立博物館・上野動物園、谷中銀座商店街・谷中霊園など、東京の伝統と歴史を堪能できる観光資源が集中する。7月初旬の朝顔まつりに続き、7月9-10日には浅草寺の「ほおずき市」も開催されるため、下町の夏祭りを連続で楽しむ周遊コースが人気。','## Overview

The Iriya Asagao Festival (Iriya Morning Glory Market) is a traditional morning glory market held annually from July 6 to 8 at Iriya Kishimojin (Shingen-ji Temple) and along the surrounding Kototoi-dōri Avenue in Shitaya, Taitō Ward, Tokyo. Originating as an Edo-era tradition that flourished during the Meiji period, it is widely cherished as Tokyo''s largest morning glory market, drawing approximately 600,000 visitors and standing as a defining summer tradition of Tokyo''s old downtown district.

## History

The morning glories of Iriya gained nationwide fame during the late Edo and Meiji periods through "henka asagao" (variant morning glories) cultivated by gardeners throughout the Iriya area. At that time, Iriya was a rural area on the outskirts of Edo that flourished as a production center for garden plants including loofah, gourd, and morning glory. From around 1880 (Meiji 13), morning glory markets began to be held around Iriya Kishimojin, attracting enthusiasts seeking rare and unusual variant morning glories. Following a temporary suspension during World War II, the festival was revived in 1948 (Shōwa 23) through the efforts of the local merchant association and gardening union, and has continued annually on the three days of July 6-8 ever since. The festival is registered as a Designated Intangible Cultural Property of Taitō Ward.

## Highlights

During the festival period, approximately 120 morning glory vendors and 100 food and craft stalls line the Kototoi-dōri Avenue, bustling from early morning around 5 a.m. until late at night around 11 p.m. The morning glories on display include traditional large-blossom varieties, the distinctive reddish-brown "Danjūrō," the prized "Danjūrō Black," and rare specimens of variant morning glories, with potted plants available from around 2,000 yen each. Iriya Kishimojin attracts queues of worshippers, and morning glory-motif uchiwa fans, prayer plaques, and amulets are distributed. The local merchant association''s food stalls and traditional craft vendors also enjoy great popularity.

## Event Details and Access

The venue is Iriya Kishimojin (Shingen-ji Temple, 1-12-16 Shitaya, Taitō Ward, Tokyo) and the surrounding Kototoi-dōri Avenue. Access is approximately 1 minute on foot from Iriya Station on the Tokyo Metro Hibiya Line, or 7 minutes from Uguisudani Station on the JR Yamanote Line. Admission is free. The festival runs from July 6 to 8, from early morning around 5 a.m. until late at night around 11 p.m.

## Surrounding Attractions

The Taitō Ward area, rich in the atmosphere of old Tokyo, offers a concentration of tourism resources for experiencing the city''s traditions and history, including Sensōji Temple, Asakusa Shrine, Nakamise-dōri shopping street, the Asakusa Engei Hall, Ueno Park, the Tokyo National Museum, Ueno Zoo, the Yanaka Ginza shopping street, and Yanaka Cemetery. Following the Asagao Festival in early July, the "Hōzuki-ichi" (Chinese Lantern Plant Market) is held at Sensōji Temple on July 9-10, making a consecutive tour of the downtown summer festivals particularly popular among visitors.','iriya-asagao-matsuri','iriya-asagao-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28691419','六ツ美悠紀斎田お田植えまつり','Mutsumi Yukisaiden Otaue Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%85%AD%E3%83%84%E7%BE%8E%E6%82%A0%E7%B4%80%E6%96%8E%E7%94%B0%E3%81%8A%E7%94%B0%E6%A4%8D%E3%81%88%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22130088','水戸まちなかフェスティバル',NULL,NULL,NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E6%88%B8%E3%81%BE%E3%81%A1%E3%81%AA%E3%81%8B%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22130298','本庄まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9C%AC%E5%BA%84%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22130964','こうのす花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%93%E3%81%86%E3%81%AE%E3%81%99%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22131441','世界キャラクターさみっとin羽生',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E4%B8%96%E7%95%8C%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC%E3%81%95%E3%81%BF%E3%81%A3%E3%81%A8in%E7%BE%BD%E7%94%9F',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22131442','富山まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AF%8C%E5%B1%B1%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24866077','因島水軍まつり','Innoshima Suigun Matsuri','広島県尾道市で行われる歳事','festival','Q11420237','因島','Innoshima','広島県','chugoku',NULL,NULL,1991,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9B%A0%E5%B3%B6%E6%B0%B4%E8%BB%8D%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28688423','義士祭','Gishi-sai','東京都港区にある泉岳寺で執り行われる供養行事',NULL,'Q3176144','泉岳寺','Sengaku-ji Temple','東京都','kanto',NULL,NULL,1950,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Sengakuji%20Gishisai%20191214e.jpg','https://ja.wikipedia.org/wiki/%E7%BE%A9%E5%A3%AB%E7%A5%AD_(%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%B8%AF%E5%8C%BA)',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24866217','山形大花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B1%B1%E5%BD%A2%E5%A4%A7%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24874240','土浦キララまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%9C%9F%E6%B5%A6%E3%82%AD%E3%83%A9%E3%83%A9%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24875250','大洗春祭り 海楽フェスタ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E6%B4%97%E6%98%A5%E7%A5%AD%E3%82%8A_%E6%B5%B7%E6%A5%BD%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24902075','四方子供曳山祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E5%9B%9B%E6%96%B9%E5%AD%90%E4%BE%9B%E6%9B%B3%E5%B1%B1%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22127846','沖縄全島エイサーまつり','Okinawa Zento Eisa Matsuri','沖縄県沖縄市で旧盆の翌週末に開催されるイベント',NULL,NULL,NULL,NULL,'沖縄県','okinawa',NULL,NULL,1956,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B2%96%E7%B8%84%E5%85%A8%E5%B3%B6%E3%82%A8%E3%82%A4%E3%82%B5%E3%83%BC%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28691636','まめからさん祭り',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.58311111,141.25416667,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BE%E3%82%81%E3%81%8B%E3%82%89%E3%81%95%E3%82%93%E7%A5%AD%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654826','みなみかた花菖蒲まつり',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.668375,141.14053611,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BF%E3%81%AA%E3%81%BF%E3%81%8B%E3%81%9F%E8%8A%B1%E8%8F%96%E8%92%B2%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654797','道饗祭','Michiae no matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%81%93%E9%A5%97%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q30925230','夏山八幡宮火祭り','Natsuyama Fire Festival',NULL,NULL,'Q11429969','夏山八幡宮','Natsuyama Hachimangu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%8F%E5%B1%B1%E5%85%AB%E5%B9%A1%E5%AE%AE%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28682646','ぎおん柏崎まつり','Gion Kashiwazaki Matsuri',NULL,'festival','Q633983','柏崎市','Kashiwazaki',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%8E%E3%81%8A%E3%82%93%E6%9F%8F%E5%B4%8E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24867306','寄居玉淀水天宮祭','Yoriitamayodosuitennguu Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AF%84%E5%B1%85%E7%8E%89%E6%B7%80%E6%B0%B4%E5%A4%A9%E5%AE%AE%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28686206','尾張津島秋まつり','Owari Tsushima Autumn Festival','愛知県津島市にて行われる祭',NULL,NULL,NULL,NULL,'愛知県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Owari%20Tsushima%20autumn%20festival1.jpg','https://ja.wikipedia.org/wiki/%E5%B0%BE%E5%BC%B5%E6%B4%A5%E5%B3%B6%E7%A7%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21654718','まほろば夏まつり',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',38.44202778,140.88121389,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%BE%E3%81%BB%E3%82%8D%E3%81%B0%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24872241','笠間の陶炎祭',NULL,'茨城県笠間市で行われる陶器市',NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%AC%A0%E9%96%93%E3%81%AE%E9%99%B6%E7%82%8E%E7%A5%AD',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q22123263','十二日まち','Jūninichi-machi','さいたま市浦和区で開かれる大歳の市','festival in Urawa-ku, Saitama',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%8D%81%E4%BA%8C%E6%97%A5%E3%81%BE%E3%81%A15.JPG','https://ja.wikipedia.org/wiki/%E5%8D%81%E4%BA%8C%E6%97%A5%E3%81%BE%E3%81%A1',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q21655120','YOSAKOI&ねぷたinとよさと',NULL,NULL,NULL,NULL,NULL,NULL,'青森県','tohoku',38.58228333,141.24588889,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/YOSAKOI%26%E3%81%AD%E3%81%B7%E3%81%9Fin%E3%81%A8%E3%82%88%E3%81%95%E3%81%A8',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28686932','べっぷ火の海まつり','Beppu Hinoumi Matsuri',NULL,'festival','Q273880','別府市','Beppu','大分県','kyushu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%B9%E3%81%A3%E3%81%B7%E7%81%AB%E3%81%AE%E6%B5%B7%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28686621','とよはしまちなかスロータウン映画祭',NULL,NULL,NULL,'Q336431','豊橋市','Toyohashi','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%A8%E3%82%88%E3%81%AF%E3%81%97%E3%81%BE%E3%81%A1%E3%81%AA%E3%81%8B%E3%82%B9%E3%83%AD%E3%83%BC%E3%82%BF%E3%82%A6%E3%83%B3%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24887792','やんさんま祭り','Yansanma Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%84%E3%82%93%E3%81%95%E3%82%93%E3%81%BE%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28732575',NULL,'Tokyo Gohan Film Festival',NULL,'film festival','Q7473516','東京','Tokyo','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,25,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24875082','須成祭','Sunari Festival','愛知県海部郡蟹江町で開催される祭礼','festival in Kanie town, Aichi prefecture, Japan','Q60990906','冨吉建速神社・八剱社','Sunari Shrine','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E9%A0%88%E6%88%90%E7%A5%AD%E3%82%8A%E6%9C%9D.jpg','https://ja.wikipedia.org/wiki/%E9%A0%88%E6%88%90%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28683601','宇佐八幡宮春季祭礼',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AE%87%E4%BD%90%E5%85%AB%E5%B9%A1%E5%AE%AE%E6%98%A5%E5%AD%A3%E7%A5%AD%E7%A4%BC',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28684805','よいやさ祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%82%88%E3%81%84%E3%82%84%E3%81%95%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28684776','安積国造神社秋季例大祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%AE%89%E7%A9%8D%E5%9B%BD%E9%80%A0%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28685120','べっぷクリスマスHanabiファンタジア',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E3%81%B9%E3%81%A3%E3%81%B7%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%9E%E3%82%B9Hanabi%E3%83%95%E3%82%A1%E3%83%B3%E3%82%BF%E3%82%B8%E3%82%A2',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28686179','大田まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%A4%A7%E7%94%B0%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28687310','琉球海炎祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%90%89%E7%90%83%E6%B5%B7%E7%82%8E%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28692103','Jin Rock Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/Jin_Rock_Festival',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28692170','北見厳寒の焼き肉まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%8C%97%E8%A6%8B%E5%8E%B3%E5%AF%92%E3%81%AE%E7%84%BC%E3%81%8D%E8%82%89%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q24897580','LUNATIC FEST.','Lunatic Fest',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/LUNATIC_FEST.',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28691756','滝山寺鬼まつり','Takisanji Oni Matsuri',NULL,NULL,'Q11565115','滝山寺','Takisan Temple','山形県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%BB%9D%E5%B1%B1%E5%AF%BA%E9%AC%BC%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q28685833','早稲田映画まつり','Waseda Movie Festival','学生主体の映画祭',NULL,'Q274486','早稲田大学','Waseda University',NULL,NULL,NULL,NULL,1987,11,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E6%97%A9%E7%A8%B2%E7%94%B0%E6%98%A0%E7%94%BB%E3%81%BE%E3%81%A4%E3%82%8A',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11496104','戦極 MCBATTLE','SENGOKU MC BATTLE',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2012,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%88%A6%E6%A5%B5_MCBATTLE',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11518609','木本まつり','Kinomoto Matsuri','三重県熊野市で行われる木本神社の例祭',NULL,'Q11518622','木本神社','Kinomoto Shrine','三重県','kinki',NULL,NULL,1608,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9C%A8%E6%9C%AC%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11493854','愛宕社の火祭り','Atagosya no Hi Matsuri',NULL,NULL,'Q819613','魚津市','Uozu','富山県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%84%9B%E5%AE%95%E7%A4%BE%E3%81%AE%E7%81%AB%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11492412','恵比須流','Ebisu-nagare','博多祇園山笠や博多松囃子（博多どんたく）の運営における構成単位である流の一つ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%81%B5%E6%AF%94%E9%A0%88%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11501940','新居浜太鼓祭り','Niihama Taiko Festival','愛媛県新居浜市の秋祭り',NULL,NULL,NULL,NULL,'愛媛県','shikoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%B1%B1%E6%A0%B9%E3%82%B0%E3%83%A9%E3%82%A6%E3%83%B3%E3%83%89%EF%BC%882009%E5%B9%B4%E6%96%B0%E5%B1%85%E6%B5%9C%E5%A4%AA%E9%BC%93%E7%A5%AD%E3%82%8A%EF%BC%89%20-%20Panoramio%2028123946.jpg','https://ja.wikipedia.org/wiki/%E6%96%B0%E5%B1%85%E6%B5%9C%E5%A4%AA%E9%BC%93%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11486153','真穴の座敷雛',NULL,'愛媛県八幡浜市の祭り',NULL,NULL,NULL,NULL,'愛媛県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%9C%9F%E7%A9%B4%E3%81%AE%E5%BA%A7%E6%95%B7%E9%9B%9B',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11526894','東広島映画祭','Higashi-Hiroshima Film Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E5%BA%83%E5%B3%B6%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11495708','成田祇園祭','Narita Gion Festival','千葉県成田市の祭礼行事',NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Narita-gion-festival-1%2CNarita-city%2CJapan.jpg','https://ja.wikipedia.org/wiki/%E6%88%90%E7%94%B0%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11513690','春日若宮おん祭','Kasuga Wakamiya On-Matsuri Festival',NULL,NULL,'Q714559','春日大社','Kasuga-taisha','三重県','kinki',34.680203,135.849128,1136,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Motonobu%20Nakagawa%2C%20Mayor%20of%20Nara.jpg','https://ja.wikipedia.org/wiki/%E6%98%A5%E6%97%A5%E8%8B%A5%E5%AE%AE%E3%81%8A%E3%82%93%E7%A5%AD',NULL,90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11513681','春日祭','Kasuga-sai',NULL,NULL,'Q714559','春日大社','Kasuga-taisha','奈良県','kinki',NULL,NULL,850,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%98%A5%E6%97%A5%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11496921','手力の火祭','Tejikara Fire Festival',NULL,NULL,'Q3517214','手力雄神社','Tejikarao Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%89%8B%E5%8A%9B%E3%81%AE%E7%81%AB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11496245','戸出七夕まつり','Toide Tanabata Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%88%B8%E5%87%BA%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11498705','播州の秋祭り','Banshū Aki Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E6%92%AD%E5%B7%9E%E3%81%AE%E7%A7%8B%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11498963','放生津曳山祭','Hōjōzu Hikiyama Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E6%94%BE%E7%94%9F%E6%B4%A5%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11524427','東京ミレナリオ','Tokyo Millenario','東京都千代田区丸の内で行われていた祭典',NULL,'Q11367944','丸の内仲通り','Marunouchi Nakadōri Street','東京都','kanto',NULL,NULL,1999,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E6%9D%B1%E4%BA%AC%E3%83%9F%E3%83%AC%E3%83%8A%E3%83%AA%E3%82%AA2005.JPG','https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E3%83%9F%E3%83%AC%E3%83%8A%E3%83%AA%E3%82%AA',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11521179','札幌国際短編映画祭','Sapporo International Short Film Festival & Market',NULL,'film festival','Q37951','札幌市','Sapporo','北海道','hokkaido',NULL,NULL,2006,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9C%AD%E5%B9%8C%E5%9B%BD%E9%9A%9B%E7%9F%AD%E7%B7%A8%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11499527','敦賀まつり','Tsuruga Matsuri','福井県敦賀市で開催される祭事',NULL,'Q28691812','敦賀駅前商店街',NULL,'福井県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%95%A6%E8%B3%80%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11522760','村上大祭',NULL,NULL,NULL,'Q284503','村上市','Murakami',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%91%E4%B8%8A%E5%A4%A7%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11527721','東流','Higashi-nagare','博多祇園山笠や博多松囃子（博多どんたく）の運営における構成単位である流の一つ',NULL,'Q11284628','博多','Hakata','福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11498044','按針祭海の花火大会','Anjin Festival Sea Fireworks','静岡県伊東市で行われる花火大会',NULL,'Q721163','伊東市','Ito','静岡県','chubu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%8C%89%E9%87%9D%E7%A5%AD%E6%B5%B7%E3%81%AE%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11524656','東京多摩国際園芸博覧会','Tokyo Tama International Horticultural Exposition','東京都で2013年に予定されていた国際園芸博覧会',NULL,'Q3915473','国営昭和記念公園','Shōwa Memorial Park','東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E5%A4%9A%E6%91%A9%E5%9B%BD%E9%9A%9B%E5%9C%92%E8%8A%B8%E5%8D%9A%E8%A6%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11511700','旭川冬まつり','Asahikawa Winter Festival',NULL,NULL,'Q11482272','平和通買物公園','Heiwa-dōri Kaimono Kōen','北海道','hokkaido',43.778333333,142.36,1960,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Asahikawa%20Winter%20Festival%20Snow%20Statue%201.jpg','https://ja.wikipedia.org/wiki/%E6%97%AD%E5%B7%9D%E5%86%AC%E3%81%BE%E3%81%A4%E3%82%8A',NULL,90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11499924','文学フリマ',NULL,'日本の文学作品展示即売会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2002,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%96%87%E5%AD%A6%E3%83%95%E3%83%AA%E3%83%9E',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11498235','掛川祭','Kakegawa Matsuri','龍尾神社、神明宮、利神社、池邊神社、白山神社、津島神社、および、貴船神社の祭礼','festival by Tatsuo Jinja, Shimmei Gū, Toshi Jinja, Ikebe Jinja, Hakusan Jinja, Tsushima Jinja and Kifune Jinja','Q823988','掛川市','Kakegawa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/2rin-yatai-kakegawa.jpg','https://ja.wikipedia.org/wiki/%E6%8E%9B%E5%B7%9D%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11526135','東北三大祭り','Three Great Festivals of Tōhoku','仙台七夕まつり、青森ねぶた祭、秋田竿燈まつりの総称',NULL,'Q129465','東北地方','Tōhoku region',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E5%8C%97%E4%B8%89%E5%A4%A7%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11502083','新川市まつり','Shinkawa-ichi Festival',NULL,NULL,NULL,NULL,NULL,'山口県','chugoku',33.95153,131.24677,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E6%96%B0%E5%B7%9D%E5%B8%82%E3%81%BE%E3%81%A4%E3%82%8A%20-%20panoramio.jpg','https://ja.wikipedia.org/wiki/%E6%96%B0%E5%B7%9D%E5%B8%82%E3%81%BE%E3%81%A4%E3%82%8A',NULL,90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11485910','庄川水まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BA%84%E5%B7%9D%E6%B0%B4%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11486080','府内戦紙',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%BA%9C%E5%86%85%E6%88%A6%E7%B4%99',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11524619','東京国際ファンタスティック映画祭','Tokyo International Fantastic Film Festival',NULL,'film festival',NULL,NULL,NULL,'東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E5%9B%BD%E9%9A%9B%E3%83%95%E3%82%A1%E3%83%B3%E3%82%BF%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11495996','戦国のろし祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%88%A6%E5%9B%BD%E3%81%AE%E3%82%8D%E3%81%97%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11496532','戸田橋花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%88%B8%E7%94%B0%E6%A9%8B%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11498207','掛塚貴船神社祭礼',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%81%A0%E5%B7%9E%E6%8E%9B%E5%A1%9A%E8%B2%B4%E8%88%B9%E7%A5%9E%E7%A4%BE%E4%BE%8B%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11504858','日光そばまつり',NULL,NULL,NULL,NULL,NULL,NULL,'栃木県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E5%85%89%E3%81%9D%E3%81%B0%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11519215','木津川やまなみ国際音楽祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9C%A8%E6%B4%A5%E5%B7%9D%E3%82%84%E3%81%BE%E3%81%AA%E3%81%BF%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11523928','東予祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%88%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11510844','日高火防祭','Hitaka Hibuse Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E9%AB%98%E7%81%AB%E9%98%B2%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11524909','東京時代まつり','Tokyo Jidai Festival',NULL,NULL,'Q232641','台東区','Taitō-ku','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/TokyoJidaiMatsuri%201%40Asakusa%2C%202006-11-03.jpg','https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E6%99%82%E4%BB%A3%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11482696','平川ねぷた','Hirakawa Neputa','青森県平川市の祭り',NULL,NULL,NULL,NULL,'青森県','tohoku',NULL,NULL,2006,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E5%B9%B3%E5%B7%9D%E3%81%AD%E3%81%B7%E3%81%9F',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11509924','日田祇園祭','Hita Gion Festival','大分県日田市で行われる神事',NULL,'Q11391826','八阪神社','Mameda Yasaka Shrine','京都府','kinki',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Gion%20fesutebaru%20Hita%20Oita%20Japan%202.jpg','https://ja.wikipedia.org/wiki/%E6%97%A5%E7%94%B0%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11489206','御燈祭','Otō Matsuri','和歌山県新宮市の神倉神社の例祭',NULL,'Q11588748','神倉神社','Kamikura Shrine','和歌山県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/518wakayama-Kumano%20Oto%20Festival-xl.jpg','https://ja.wikipedia.org/wiki/%E5%BE%A1%E7%87%88%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11513731','春木だんじり祭','Haruki Danjiri Matsuri','大阪府岸和田市春木地区で行われる祭',NULL,NULL,NULL,NULL,'大阪府','kinki',NULL,NULL,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/Haruki%20danjiri%202011.jpg','https://ja.wikipedia.org/wiki/%E6%98%A5%E6%9C%A8%E3%81%A0%E3%82%93%E3%81%98%E3%82%8A%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11518232','木古内町寒中みそぎ祭り','Kanchu Misogi Matsuri','毎年1月に日本の北海道木古内町で行われる祭り',NULL,NULL,NULL,NULL,'北海道','hokkaido',NULL,NULL,NULL,NULL,'winter',NULL,'https://ja.wikipedia.org/wiki/%E6%9C%A8%E5%8F%A4%E5%86%85%E7%94%BA%E5%AF%92%E4%B8%AD%E3%81%BF%E3%81%9D%E3%81%8E%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11502788','新潟まつり','niigata matsuri','新潟市の祭',NULL,'Q711787','中央区','Chūō-ku','新潟県','chubu',NULL,NULL,1955,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%96%B0%E6%BD%9F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11490726','忌部神社 (松江市)','Inbe Shrine (Matsue City)','松江市にある神社','Shinto shrine in Shimane Prefecture, Japan',NULL,NULL,NULL,'島根県','chugoku',35.399028,133.03111,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%BF%8C%E9%83%A8%E7%A5%9E%E7%A4%BE.jpg','https://ja.wikipedia.org/wiki/%E5%BF%8C%E9%83%A8%E7%A5%9E%E7%A4%BE_(%E6%9D%BE%E6%B1%9F%E5%B8%82)',NULL,95,'drafted','## 概要

忌部神社（いんべじんじゃ）は、島根県松江市東忌部町に鎮座する古社で、出雲国意宇郡（おうぐん）の延喜式内社である。古代より朝廷の祭祀を司った忌部氏（いんべうじ）の祖神を祀り、出雲国造家との深い関わりを持つ歴史ある神社として知られる。例祭は毎年10月19日に執り行われる。

## 歴史

創建年代は不詳だが、延喜式神名帳（927年成立）に出雲国意宇郡の小社「忌部神社」として記載されており、少なくとも平安時代初期には朝廷から正式な式内社として認定されていた。主祭神は天太玉命（あめのふとだまのみこと）で、忌部氏の祖神とされる。忌部氏は中臣氏（後の藤原氏）と並ぶ古代の祭祀氏族で、宮中の祭祀・神具製作を担った一族である。中世以降、出雲国造家（千家・北島両家）との関係を深め、出雲信仰圏の重要拠点のひとつとして続いてきた。

## 見どころ

社殿は大社造の流れを汲む簡素ながら格式高い造りで、出雲地方独特の建築美を伝える。境内は鎮守の森に囲まれ、樹齢数百年とされる古木が点在し、古社らしい荘厳な雰囲気が漂う。例祭の10月19日には、地元氏子による神楽奉納が行われる。出雲神楽の流れを汲む荘重な舞は、出雲地方の祭祀文化を今に伝える貴重な民俗芸能である。普段は静かな里宮であり、参拝者も少なく、出雲の古社の素朴な信仰風景を体感できる。

## 開催情報

所在地は島根県松江市東忌部町953。最寄駅はJR山陰本線「松江駅」からバスで約25分（東忌部行き）、または車で約20分。例祭は毎年10月19日。境内参拝は終日無料。公共交通機関のアクセスはやや限定的で、レンタカー利用が便利。10月の松江は朝夕冷え込むため、薄手のコートを持参するとよい。

## 周辺の見どころ

松江市は宍道湖を中心とした水の都として知られ、松江城（国宝・現存12天守のひとつ）、塩見縄手の武家屋敷通り、小泉八雲記念館などの歴史観光地が市内に集積する。出雲信仰の総本山「出雲大社」までは車で約45分。同じ意宇郡内には熊野大社（火の神を祀る出雲国一宮）、神魂神社（最古の大社造社殿・国宝）も点在し、出雲神話の聖地巡りに最適。宍道湖の夕日は日本夕陽百選にも選ばれている。','## Overview

Inbe Shrine (忌部神社) is an ancient shrine located in Higashi-Inbe-chō, Matsue City, Shimane Prefecture. Listed in the Engishiki Jinmyōchō as a shikinaisha of Ou District in Izumo Province, the shrine enshrines the ancestral deity of the Inbe clan — one of ancient Japan''s most important priestly families — and maintains deep ties with the Izumo Kokusō (the hereditary high priest lineage of Izumo Taisha). Its annual main festival is held every October 19.

## History

The exact founding date is unknown, but the shrine is recorded in the Engishiki Jinmyōchō (compiled in 927) as a minor shikinaisha of Ou District, Izumo Province, indicating that it had been officially recognized by the imperial court at least by the early Heian period. Its principal deity is Ame-no-Futodama-no-Mikoto, regarded as the ancestral kami of the Inbe clan. The Inbe were an ancient priestly family that, alongside the Nakatomi clan (later the Fujiwara), conducted rituals at the imperial court and produced sacred ritual implements. From the medieval period onward, the shrine deepened its ties with the Izumo Kokusō lineage (the Senge and Kitajima families) and remained an important node in the broader Izumo religious sphere.

## Highlights

The shrine building follows the lineage of the Taisha-zukuri architectural style — austere yet dignified — and conveys the architectural beauty distinctive to the Izumo region. The precincts are enveloped by a sacred forest dotted with ancient trees believed to be several hundred years old, creating the solemn atmosphere characteristic of ancient shrines. At the main festival on October 19, local parishioners dedicate kagura performances. These dignified dances, which descend from the Izumo Kagura tradition, are a precious folk-performing art that preserves the ritual culture of the Izumo region. As a quiet country shrine, Inbe Shrine sees few visitors most of the year, allowing pilgrims to experience the unpretentious devotional atmosphere of an ancient Izumo shrine.

## Event Information

The shrine is located at 953 Higashi-Inbe-chō, Matsue City, Shimane Prefecture. The nearest station is Matsue Station on the JR San''in Main Line, followed by an approximately 25-minute bus ride bound for Higashi-Inbe, or about 20 minutes by car. The main festival is held annually on October 19. Admission to the shrine grounds is free at all times. Public transportation access is somewhat limited, so a rental car is recommended. October mornings and evenings in Matsue can be chilly, so bringing a light coat is advisable.

## Nearby Attractions

Matsue City is known as the "City of Water" centered on Lake Shinji, with a wealth of historical attractions including Matsue Castle (a National Treasure and one of only twelve original castle keeps), the Shiomi Nawate samurai residences district, and the Lafcadio Hearn Memorial Museum. Izumo Taisha — the head shrine of all Izumo worship — is approximately 45 minutes away by car. Within the same former Ou District, visitors can also visit Kumano Taisha (the principal shrine of Izumo Province, dedicated to the deity of fire) and Kamosu Shrine (which preserves the oldest existing Taisha-zukuri structure, designated as a National Treasure), making the area ideal for a pilgrimage tour of Izumo mythology. The sunset over Lake Shinji is ranked among Japan''s Top 100 Sunset Views.','inbe-jinja-matsue','inbe-jinja-matsue',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11531687','松江水郷祭湖上花火大会',NULL,'島根県松江市で開催される花火大会',NULL,'Q207321','松江市','Matsue','島根県','chugoku',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E6%9D%BE%E6%B1%9F%E6%B0%B4%E9%83%B7%E7%A5%AD%E6%B9%96%E4%B8%8A%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A%E3%83%89%E3%83%AD%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%BC%E3%81%AE%E6%A7%98%E5%AD%90.jpg','https://ja.wikipedia.org/wiki/%E6%9D%BE%E6%B1%9F%E6%B0%B4%E9%83%B7%E7%A5%AD%E6%B9%96%E4%B8%8A%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11548666','水戸黄門まつり','Mito Kōmon Festival','茨城県水戸市で開かれる祭',NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E6%88%B8%E9%BB%84%E9%96%80%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11569952','片貝まつり','Katakai Festival','新潟県小千谷市片貝町で開催される秋祭り',NULL,NULL,NULL,NULL,'新潟県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%89%87%E8%B2%9D%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11563278','湘南ひらつか七夕まつり','Shōnan Hiratsuka Tanabata Festival','神奈川県平塚市で行われる七夕の祭り',NULL,'Q502199','平塚市','Hiratsuka','神奈川県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%B9%98%E5%8D%97%E3%81%B2%E3%82%89%E3%81%A4%E3%81%8B%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11579109','登別地獄まつり','Noboribetsu Jigoku Matsuri',NULL,NULL,'Q3888689','登別温泉','Noboribetsu Onsen',NULL,NULL,NULL,NULL,1964,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%99%BB%E5%88%A5%E5%9C%B0%E7%8D%84%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11536932','桃まつり','Peach Festival',NULL,'Japanese spring festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%A1%83%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11574728','生國魂祭','Ikutama Matsuri','大阪市天王寺区にある生國魂神社の祭礼',NULL,'Q11574477','生國魂神社','Ikukunitama Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%94%9F%E5%9C%8B%E9%AD%82%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11558084','浜降祭','Hamaori-sai','神奈川県茅ヶ崎市で行われる祭り',NULL,NULL,NULL,NULL,'神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hamaori-sai%202010%20b%2C%20Naka-kaigan%20Hachidai-ry%C5%AB%C5%8Djin.jpg','https://ja.wikipedia.org/wiki/%E6%B5%9C%E9%99%8D%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11565005','ネブタ流し','Namerikawa Nebuta Nagashi','滑川市の祭事',NULL,'Q823513','滑川市','Namerikawa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%BB%91%E5%B7%9D%E3%81%AE%E3%83%8D%E3%83%96%E3%82%BF%E6%B5%81%E3%81%97',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11563560','湯布院映画祭','Yufuin Film Festival',NULL,NULL,'Q990455','由布市','Yufu','大分県','kyushu',NULL,NULL,1976,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B9%AF%E5%B8%83%E9%99%A2%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11550984','江戸三大祭り','Three Great Festivals of Edo','東京都で行われる3つの大きなお祭り。神田祭、山王祭、深川祭。',NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B1%9F%E6%88%B8%E4%B8%89%E5%A4%A7%E7%A5%AD%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11566877','火振りかまくら','Hiburi Kamakura','秋田県仙北市角館地域に伝わる伝統行事',NULL,'Q11630890','角館','Kakunodate','秋田県','tohoku',NULL,NULL,NULL,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Hiburi%20Kamakura%20in%20Kakunodate%202019b.jpg','https://ja.wikipedia.org/wiki/%E7%81%AB%E6%8C%AF%E3%82%8A%E3%81%8B%E3%81%BE%E3%81%8F%E3%82%89',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11528841','杵築盆踊り','Kitsuki Bon-odori',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B5%E7%AF%89%E7%9B%86%E8%B8%8A%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11529737','松山まつり',NULL,NULL,NULL,NULL,NULL,NULL,'愛媛県','shikoku',33.83676,132.77014,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E5%B1%B1%E9%87%8E%E7%90%83%E6%8B%B3%E3%81%8A%E3%81%A9%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11565710','潮来祇園祭禮','Itako Gion Matsuri','茨城県潮来市で行われる祭礼',NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Itako%20Gion%20Festival%2C%20Ibaraki%2014.jpg','https://ja.wikipedia.org/wiki/%E6%BD%AE%E6%9D%A5%E7%A5%87%E5%9C%92%E7%A5%AD%E7%A6%AE',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11530803','松本ぼんぼん','Matsumoto-Bonbon Festival','毎年8月の第1土曜日に長野県松本市の中心街で行われる夏祭り','Summer festival held every year on the first Saturday in August in the center of Matsumoto City, Nagano Prefecture',NULL,NULL,NULL,'長野県','chubu',36.234425,137.96922,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E6%9C%AC%E3%81%BC%E3%82%93%E3%81%BC%E3%82%93',NULL,75,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11566707','瀬波大祭','Senami Festival','新潟県村上市の祭事',NULL,'Q284503','村上市','Murakami','新潟県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%80%AC%E6%B3%A2%E5%A4%A7%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11568981','熊野速玉祭','Kumano Hayatama Matsuri','和歌山県新宮市にある熊野速玉大社の例大祭',NULL,'Q335618','熊野速玉大社','Kumano Hayatama Taisha','和歌山県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E5%BE%A1%E8%88%B9%E7%A5%AD%20%E6%97%A9%E8%88%B9.JPG','https://ja.wikipedia.org/wiki/%E7%86%8A%E9%87%8E%E9%80%9F%E7%8E%89%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11566794','灘のけんか祭り','Nada no kenka matsuri',NULL,'festival in Himeji, Japan',NULL,NULL,NULL,'兵庫県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Nada%20no%20Kenka%20matsuri%2004.jpg','https://ja.wikipedia.org/wiki/%E7%81%98%E3%81%AE%E3%81%91%E3%82%93%E3%81%8B%E7%A5%AD%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11568918','熊野本宮大社例大祭','Kumano Hongū Taisha Reitaisha','和歌山県田辺市にある熊野本宮大社の例大祭',NULL,'Q705035','熊野本宮大社','Kumano Hongū Taisha','和歌山県','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%86%8A%E9%87%8E%E6%9C%AC%E5%AE%AE%E5%A4%A7%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11538304','桶川祇園祭','Okegawa Gion Matsuri',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%A1%B6%E5%B7%9D%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11547768','毛馬内の盆踊','Kemanai no Bon-odori','秋田県鹿角市十和田毛馬内行われる盆踊り','Bon dance held in Towada Kemauchi, Kazuno City, Akita Prefecture',NULL,NULL,NULL,'青森県','tohoku',40.2715,140.766667,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/%E6%AF%9B%E9%A6%AC%E5%86%85%E7%9B%86%E8%B8%8A%E3%82%8A%E3%81%AE%E9%A2%A8%E6%99%AF.jpg','https://ja.wikipedia.org/wiki/%E6%AF%9B%E9%A6%AC%E5%86%85%E3%81%AE%E7%9B%86%E8%B8%8A',NULL,95,'drafted','## 概要

毛馬内の盆踊（けまないのぼんおどり）は、秋田県鹿角市十和田毛馬内地区で毎年8月21日から23日の3日間にわたって執り行われる、お盆の精霊送りを起源とする伝統的な盆踊りである。「毛馬内の盆踊」として1998年に国の重要無形民俗文化財に指定され、西馬音内の盆踊（羽後町）、一日市の盆踊（八郎潟町）と並ぶ「秋田三大盆踊」のひとつに数えられる。

## 歴史

起源は南北朝時代にまで遡るとされ、約700年の歴史を持つと伝えられる。鹿角地方は中世から南部氏の統治下にあり、戦死者や祖先の霊を慰めるための盆踊りとして地域に根付いた。江戸時代を通じて南部藩の保護を受け、明治以降も地元の保存会を中心に伝統が守り継がれてきた。「大の坂（だいのさか）」と「甚句（じんく）」の2種類の踊りで構成され、それぞれ異なる起源と性格を持つ。

## 見どころ

最大の特徴は、踊り手が顔を白い手ぬぐいで覆い隠す独特の装束である。これは盆踊りが精霊送りの神事である神聖さを表すと同時に、男女の差別なく死者を悼む平等の精神を象徴するとされる。踊りは「大の坂」（大の坂峠の合戦で散った武士を悼む荘厳な踊り）と「甚句」（甚句節に合わせた軽快な踊り）の2部構成で、いずれも篝火を囲んで輪になって踊られる。会場は毛馬内本町通りで、両側に篝火が並ぶ通りが踊り手で埋め尽くされる光景は幽玄美にあふれる。

## 開催情報

開催地は秋田県鹿角市十和田毛馬内本町通り。最寄駅はJR花輪線「十和田南駅」徒歩約15分。開催期間は毎年8月21日から23日の3日間。踊りは各日19:30頃から22:00頃まで。観覧は無料で、観光客も装束を着用して踊りに参加することができる（保存会で装束貸出あり・要事前申込）。8月下旬の鹿角は夜間冷え込むことがあるため、薄手の羽織りものを持参するとよい。

## 周辺の見どころ

鹿角市は十和田八幡平国立公園の南玄関に位置し、十和田湖・八幡平・後生掛温泉などの観光地が至近にある。世界遺産「北海道・北東北の縄文遺跡群」の構成資産「大湯環状列石」は車で約20分。康楽館（明治・大正期の現役芝居小屋・国指定重要文化財）、史跡尾去沢鉱山も鹿角市内にあり、文化遺産と自然を組み合わせた旅程が組みやすい。きりたんぽ発祥の地として、本場のきりたんぽ鍋も味わえる。','## Overview

Kemanai no Bon-odori (毛馬内の盆踊) is a traditional Bon dance with roots in the spirit-sending rituals of the Obon festival, held annually over three days from August 21 to 23 in the Kemanai district of Towada, Kazuno City, Akita Prefecture. Designated as an Important Intangible Folk Cultural Property of Japan in 1998, it is counted among the "Three Great Bon Dances of Akita" alongside the Nishimonai no Bon-odori (Ugo Town) and the Hitoichi no Bon-odori (Hachirōgata Town).

## History

The dance''s origins are said to date back to the Nanboku-chō period, giving it a history of approximately 700 years. The Kazuno region had been under the rule of the Nanbu clan since medieval times, and the dance took root in the community as a means of consoling the spirits of fallen warriors and ancestors. Throughout the Edo period it received the patronage of the Nanbu domain, and from the Meiji era onward local preservation societies have safeguarded the tradition. The festival consists of two distinct dances — Dainosaka and Jinku — each with its own origin and character.

## Highlights

The most striking feature is the unique attire of the dancers, who cover their faces with white hand-towels (tenugui). This is said to express the sacred nature of the dance as a spirit-sending ritual, while also symbolizing the egalitarian spirit of mourning the dead without distinction of gender. The dance proceeds in two parts: Dainosaka, a solemn dance mourning the warriors who fell at the Battle of Dainosaka Pass, and Jinku, a brisk dance set to the lively Jinku-bushi melody. Both are performed in circles around bonfires. The venue is the Honmachi-dōri street of Kemanai, where the road lined with flaming braziers on both sides fills with dancers, creating a scene of profound ethereal beauty.

## Event Information

The venue is Honmachi-dōri street in Towada Kemanai, Kazuno City, Akita Prefecture. The nearest station is Towada-Minami Station on the JR Hanawa Line, about a 15-minute walk away. The festival runs annually from August 21 to 23. Dances are performed each evening from approximately 7:30 PM to 10:00 PM. Admission is free, and visitors are welcome to don the traditional attire and join the dance (the preservation society offers costume rentals; advance reservation required). Late-August evenings in Kazuno can be chilly, so a light jacket is recommended.

## Nearby Attractions

Kazuno City lies at the southern gateway to Towada-Hachimantai National Park, with major attractions including Lake Towada, Hachimantai, and Goshogake Onsen close at hand. The Ōyu Stone Circles — a component asset of the UNESCO World Heritage Site "Jōmon Prehistoric Sites in Northern Japan" — are about 20 minutes away by car. Within Kazuno City itself, visitors can also explore Kōrakukan (a working Meiji- and Taishō-era theater designated as an Important Cultural Property) and the Osarizawa Mine Historic Site. As the birthplace of kiritanpo, the area is also the ideal place to enjoy authentic kiritanpo-nabe hotpot.','kemanai-no-bon-odori','kemanai-no-bon-odori',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11548439','水天宮春大祭','Suitengū Spring Festival','福岡県久留米市の水天宮で行われる祭り','Shinto shrine in Yanagawa, Japan','Q3200625','水天宮','Kurume Suitengū','福岡県','kyushu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E5%A4%A9%E5%AE%AE%E6%98%A5%E5%A4%A7%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11572451','玉名納涼花火大会',NULL,NULL,NULL,'Q861610','玉名市','Tamana','熊本県','kyushu',32.926456,130.56609,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%8E%89%E5%90%8D%E7%B4%8D%E6%B6%BC%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11539090','森の祭り','Mori no Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%A3%AE%E3%81%AE%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11552606','沖縄サンバカーニバル','Okinawa International Carnival',NULL,NULL,'Q328615','沖縄市','Okinawa','沖縄県','okinawa',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Spectators%20watch%20a%20parade%20as%20part%20of%20the%20Okinawa%20City%20International%20Carnival%20Nov.%2030%2C%202013%2C%20outside%20Kadena%20Air%20Base%27s%20Gate%202%20in%20Okinawa%2C%20Japan%20131130-F-LI951-118.jpg','https://ja.wikipedia.org/wiki/%E6%B2%96%E7%B8%84%E3%82%B5%E3%83%B3%E3%83%90%E3%82%AB%E3%83%BC%E3%83%8B%E3%83%90%E3%83%AB',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11568888','熊野大花火大会','Kumano Great Fireworks Festival','三重県熊野市で開催される花火大会',NULL,'Q3482030','七里御浜','Shichirimi Beach','三重県','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%86%8A%E9%87%8E%E5%A4%A7%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11559869','深井だんじり祭り','Fukai Danjiri Festival',NULL,'danjiri float festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'autumn',NULL,'https://ja.wikipedia.org/wiki/%E6%B7%B1%E4%BA%95%E3%81%A0%E3%82%93%E3%81%98%E3%82%8A%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11551423','池ノ上みそぎ祭','Ikenoue Misogi Matsuri',NULL,NULL,'Q11620951','葛懸神社','Katsuragake Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B1%A0%E3%83%8E%E4%B8%8A%E3%81%BF%E3%81%9D%E3%81%8E%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11542169','樋山路盆踊り','Hiyamaji Bon-odori',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%A8%8B%E5%B1%B1%E8%B7%AF%E7%9B%86%E8%B8%8A%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11557680','浜崎祇園山笠','Hamasaki Gion Yamakasa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Hamasaki%20gion%20yamakasa%202008.jpg','https://ja.wikipedia.org/wiki/%E6%B5%9C%E5%B4%8E%E7%A5%87%E5%9C%92%E5%B1%B1%E7%AC%A0',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11543279','横浜開港祭','Yokohama Port Festival',NULL,NULL,NULL,NULL,NULL,'神奈川県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%A8%AA%E6%B5%9C%E9%96%8B%E6%B8%AF%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11571216','犬山祭','Inuyama Festival','愛知県犬山市で行われる針綱神社の祭礼',NULL,'Q11648178','針綱神社','Haritsuna Shrine','愛知県','chubu',NULL,NULL,1635,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Inuyamajo2.JPG','https://ja.wikipedia.org/wiki/%E7%8A%AC%E5%B1%B1%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11571727','狭山入間川七夕まつり',NULL,NULL,NULL,NULL,NULL,NULL,'埼玉県','kanto',35.85810833,139.40801111,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%8B%AD%E5%B1%B1%E5%B8%82%E5%85%A5%E9%96%93%E5%B7%9D%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11548378','水口曳山祭','Minakuchi Hikiyama Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E5%8F%A3%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11549310','水郷おみがわ花火大会',NULL,'千葉県香取市で開かれる花火大会',NULL,NULL,NULL,NULL,'千葉県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B4%E9%83%B7%E3%81%8A%E3%81%BF%E3%81%8C%E3%82%8F%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11528627','東金桜まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E6%9D%B1%E9%87%91%E6%A1%9C%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11529336','松原の石取祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E5%8E%9F%E3%81%AE%E7%9F%B3%E5%8F%96%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11529891','松山港まつり',NULL,NULL,NULL,NULL,NULL,NULL,'愛媛県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E5%B1%B1%E6%B8%AF%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11530797','松本のぼんぼん・青山様',NULL,NULL,NULL,NULL,NULL,NULL,'長野県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E6%9C%AC%E3%81%AE%E3%81%BC%E3%82%93%E3%81%BC%E3%82%93%E3%83%BB%E9%9D%92%E5%B1%B1%E6%A7%98',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11534049','柳まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9F%B3%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11530743','松明あかし','Taimatsu Akashi',NULL,NULL,'Q819664','須賀川市','Sukagawa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9D%BE%E6%98%8E%E3%81%82%E3%81%8B%E3%81%97',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11549648','氷見祇園祭','Himi Gion Matsuri',NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%B0%B7%E8%A6%8B%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11552667','沖縄国際カーニバル',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B2%96%E7%B8%84%E5%9B%BD%E9%9A%9B%E3%82%AB%E3%83%BC%E3%83%8B%E3%83%90%E3%83%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11556007','津山まつり',NULL,NULL,NULL,NULL,NULL,NULL,'岡山県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B4%A5%E5%B1%B1%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11556211','津沢夜高祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B4%A5%E6%B2%A2%E5%A4%9C%E9%AB%98%E3%81%82%E3%82%93%E3%81%A9%E3%82%93%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11556000','津屋崎祇園山笠','Tsuyazaki Gion Yamakasa',NULL,NULL,'Q825700','福津市','Fukutsu','三重県','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E6%B4%A5%E5%B1%8B%E5%B4%8E%E7%A5%87%E5%9C%92%E5%B1%B1%E7%AC%A0',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11558195','浦安三社祭',NULL,NULL,NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B5%A6%E5%AE%89%E4%B8%89%E7%A4%BE%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11559180','海老江曳山祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E6%B5%B7%E8%80%81%E6%B1%9F%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11564076','源平火牛まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%BA%90%E5%B9%B3%E7%81%AB%E7%89%9B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11564136','源氏まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%BA%90%E6%B0%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11566788','瀬高町納涼花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E3%81%BF%E3%82%84%E3%81%BE%E7%B4%8D%E6%B6%BC%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11566826','火の国まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%81%AB%E3%81%AE%E5%9B%BD%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11568835','熊谷花火大会',NULL,NULL,NULL,NULL,NULL,NULL,'埼玉県','kanto',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%86%8A%E8%B0%B7%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11573331','珠洲デカ曳山',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E7%8F%A0%E6%B4%B2%E3%83%87%E3%82%AB%E6%9B%B3%E5%B1%B1',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11577736','甲山廿日えびす',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%94%B2%E5%B1%B1%E5%BB%BF%E6%97%A5%E3%81%88%E3%81%B3%E3%81%99',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11541041','椿祭り','Camellia Festival','東京都大島町で行う祭り',NULL,NULL,NULL,NULL,'東京都','kanto',NULL,NULL,1956,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%A4%BF%E7%A5%AD%E3%82%8A_(%E6%9D%B1%E4%BA%AC%E9%83%BD)',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11546062','武生国際音楽祭','Takefu International Music Festival','福井県越前市（旧・武生市）で行われる音楽祭',NULL,NULL,NULL,NULL,'福井県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%AD%A6%E7%94%9F%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11557606','浜名湖花博','Pacific Flora 2004',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%B5%9C%E5%90%8D%E6%B9%96%E8%8A%B1%E5%8D%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11533908','染織祭',NULL,NULL,NULL,'Q34600','京都市','Kyoto','京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%9F%93%E7%B9%94%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11573781','琴弾八幡宮大祭','Kotohiki Hachimangū Taisai','香川県観音寺市の琴弾八幡宮の秋季大祭',NULL,'Q3199184','琴弾八幡宮','Kotohiki Hachimangū','香川県','shikoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Nanagouchi.jpg','https://ja.wikipedia.org/wiki/%E7%90%B4%E5%BC%BE%E5%85%AB%E5%B9%A1%E5%AE%AE%E5%A4%A7%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11549314','水郷潮来あやめまつり','Suigō Itako Iris Festival','茨城県潮来市の水郷潮来あやめ園で行われる祭り',NULL,'Q11397147','水郷潮来あやめ園','Suigō Itako Iris Garden','茨城県','kanto',35.9366,140.5461,1952,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Suigo%20Itako%20Ayame%20Garden%2015.jpg','https://ja.wikipedia.org/wiki/%E6%B0%B4%E9%83%B7%E6%BD%AE%E6%9D%A5%E3%81%82%E3%82%84%E3%82%81%E3%81%BE%E3%81%A4%E3%82%8A',NULL,95,'drafted','## 概要

水郷潮来あやめまつり（すいごういたこあやめまつり）は、茨城県潮来市の水郷潮来あやめ園で毎年5月下旬から6月下旬にかけて開催される、約100万本のあやめ・花菖蒲が咲き誇る大規模な花の祭典である。1952年（昭和27年）に始まり、関東屈指のあやめ名所として知られる。

## 歴史

潮来は江戸時代から水運で栄えた水郷の町として、利根川と霞ヶ浦・北浦を結ぶ要衝に位置し、湿地帯に自生していたあやめが古くから親しまれてきた。1932年（昭和7年）、地元有志が観光資源としてあやめ園の整備を始め、1952年に正式に「あやめまつり」として開催が始まった。1955年に発表された花村菊江の歌謡曲「潮来花嫁さん」のヒットにより全国的に知名度が高まり、嫁入り舟をはじめとする観光イベントが定着していった。

## 見どころ

園内には約500種100万本のあやめ・花菖蒲が植えられ、紫・白・黄・絞り模様など多彩な品種が見頃を迎える。期間中の土日には「嫁入り舟」が運行され、白無垢の花嫁が舟で水路を渡る往時の婚礼風景が再現される。夜間ライトアップやろ舟遊覧、地元産品の販売も行われる。

## 開催情報・アクセス

会場は水郷潮来あやめ園（茨城県潮来市あやめ1-5）。JR鹿島線潮来駅から徒歩約3分とアクセス良好で、入園は無料。期間中は約80万人の観光客が訪れる。

## 周辺観光

近隣には霞ヶ浦・北浦の水辺景観、鹿島神宮、香取神宮など歴史的な観光地が点在し、舟運の名残を伝える前川を巡るろ舟遊覧も人気。','## Overview

The Suigō Itako Iris Festival (Suigō Itako Ayame Matsuri) is a major flower festival held annually from late May to late June at the Suigō Itako Ayame Garden in Itako City, Ibaraki Prefecture, showcasing approximately one million iris and Japanese iris (hanashōbu) blooms. Begun in 1952, it is recognized as one of the most renowned iris-viewing destinations in the Kantō region and a signature event of Japan''s "water country" cultural tradition.

## History

Itako thrived as a water-transport hub during the Edo period, strategically located where the Tone River meets Lake Kasumigaura and Lake Kitaura. Native irises growing in the surrounding wetlands have long been cherished by local residents. In 1932 (Shōwa 7), local volunteers began developing the iris garden as a tourism resource, and in 1952 the official "Iris Festival" was launched. The release of Kikue Hanamura''s popular song "Itako Hanayome-san" (Bride of Itako) in 1955 propelled the festival to nationwide fame, and tourist events such as the bridal boat procession became firmly established traditions.

## Highlights

The garden hosts approximately 500 varieties and one million iris plants, displaying a spectacular palette of purple, white, yellow, and variegated blooms at peak bloom. On weekends during the festival period, the famous "Bridal Boat" (Yomeiri-bune) procession reenacts traditional water-borne wedding ceremonies, with brides in pristine white wedding kimono ferried across the canal in wooden boats. Evening illuminations, traditional rowboat (ro-bune) tours of the surrounding waterways, and stalls selling local specialty products complement the floral display.

## Event Details and Access

The venue is the Suigō Itako Ayame Garden (1-5 Ayame, Itako City, Ibaraki Prefecture), conveniently located about a three-minute walk from Itako Station on the JR Kashima Line, with free admission throughout the festival. The event draws approximately 800,000 visitors during its month-long run.

## Surrounding Attractions

Nearby attractions include the scenic waterscapes of Lake Kasumigaura and Lake Kitaura, the historic Kashima Shrine and Katori Shrine, and ro-bune rowboat tours along the Maekawa River that preserve the atmosphere of the old water-transport era. The combination of traditional canals, flowers, and shrines offers visitors an immersive experience of Japan''s water culture heritage.','suigo-itako-ayame-matsuri','suigo-itako-ayame-matsuri',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11537271','桐生八木節まつり','Kiryū Yagibushi festival',NULL,NULL,NULL,NULL,NULL,'群馬県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%A1%90%E7%94%9F%E5%85%AB%E6%9C%A8%E7%AF%80%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11614771','芦別健夏山笠','Ashibetsu Kenka Yamakasa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E8%8A%A6%E5%88%A5%E5%81%A5%E5%A4%8F%E5%B1%B1%E7%AC%A0',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11594394','福神流','Fukujin-nagare','博多松囃子（博多どんたく）の運営における構成単位である流の一つ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E7%A5%9E%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11580598','白鳥神社','Shiratori Shrine','大阪府羽曳野市にある神社','Shinto shrine in Habikino, Japan',NULL,NULL,NULL,'大阪府','kinki',34.553777777,135.609416666,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Shiratori-jinja%20haiden.jpg','https://ja.wikipedia.org/wiki/%E7%99%BD%E9%B3%A5%E7%A5%9E%E7%A4%BE_(%E7%BE%BD%E6%9B%B3%E9%87%8E%E5%B8%82)',NULL,95,'drafted','## 概要

白鳥神社（しらとりじんじゃ）は、大阪府羽曳野市古市にある神社で、ヤマトタケル（日本武尊）を祀る式内社級の古社である。例祭は毎年10月に行われ、地元では「白鳥さん」と呼ばれ親しまれる。古市古墳群の中心部に位置し、ヤマトタケル伝説と深く結びついた由緒を持つ。

## 歴史

『古事記』『日本書紀』が伝えるところによれば、ヤマトタケルは東征から大和への帰途に伊勢国能煩野で病没し、その魂が白鳥となって大和琴弾原を経て河内古市に降り立ったとされる。白鳥神社はこの白鳥伝説の終焉地として古市古墳群（応神天皇陵の南方）に鎮座し、ヤマトタケルの霊を祀ったのが起源と伝わる。律令期には朝廷の崇敬を受け、中世を通じて地域の守護神として崇められてきた。

## 見どころ

社殿は江戸期の建築様式を残し、境内には白鳥伝説を象徴する白鳥のレリーフや、古墳群と一体化した深い杜の景観が広がる。古市古墳群（2019年世界遺産登録）の構成資産に隣接し、近接する白鳥陵古墳（軽里大塚古墳）はヤマトタケルの陵墓に治定されている。

## 開催情報・アクセス

近鉄南大阪線古市駅から徒歩約10分。境内は終日参拝自由。例祭は10月に執り行われ、地元自治会による神輿渡御や奉納行事が行われる。

## 周辺観光

百舌鳥・古市古墳群（世界遺産）の応神天皇陵古墳、白鳥陵古墳、誉田八幡宮など、古代史の核心に触れられる史跡が密集する。羽曳野市・藤井寺市一帯は古墳ウォーキングルートが整備されており、徒歩で多くの古墳を巡ることができる。','## Overview

Shiratori Shrine (Shiratori Jinja) is an ancient shrine located in Furuichi, Habikino City, Osaka Prefecture, enshrining Yamato Takeru no Mikoto, the legendary prince of the Yamato royal family. Recognized at the rank of a Shikinaisha (shrine listed in the 10th-century Engishiki register), the shrine holds its annual main festival each October and is affectionately known to locals as "Shiratori-san." Situated within the heart of the Furuichi Kofun Cluster, it preserves deep connections to the legend of Yamato Takeru.

## History

According to the Kojiki and Nihon Shoki, Japan''s earliest chronicles, Prince Yamato Takeru fell ill and died at Nobono in Ise Province on his return journey from his eastern military campaign. His soul is said to have transformed into a white swan that flew via the Kotohiki Plain in Yamato before alighting at Furuichi in Kawachi Province. Shiratori Shrine was established at this final landing site of the swan, within what would later become the Furuichi Kofun Cluster south of Emperor Ōjin''s mausoleum, and is believed to have originated as a place of worship for the spirit of Yamato Takeru. During the Ritsuryō period, the shrine received imperial patronage, and throughout the medieval era it was venerated as a guardian deity of the surrounding region.

## Highlights

The main shrine hall preserves architectural elements from the Edo period, while the precincts feature reliefs depicting the swan symbolizing the Yamato Takeru legend and a deep forest landscape integrated with the surrounding ancient burial mounds. The shrine is adjacent to constituent sites of the Mozu-Furuichi Kofun Cluster, which was inscribed on the UNESCO World Heritage List in 2019. The nearby Shiratori-ryō Kofun (also known as Karusato Ōtsuka Kofun) is officially designated by the Imperial Household Agency as the tomb of Yamato Takeru himself.

## Event Details and Access

The shrine is approximately a ten-minute walk from Furuichi Station on the Kintetsu Minami-Osaka Line. The grounds are open for worship throughout the day. The annual main festival is held in October, featuring a portable shrine (mikoshi) procession organized by local neighborhood associations and various dedicatory rituals.

## Surrounding Attractions

The area is densely packed with historic sites at the heart of ancient Japanese history, including the Mozu-Furuichi Kofun Cluster (a UNESCO World Heritage Site) with the Emperor Ōjin Mausoleum Tumulus, the Shiratori-ryō Kofun, and Konda Hachimangū Shrine. The Habikino and Fujiidera area has developed an extensive kofun walking route system, enabling visitors to explore numerous ancient burial mounds on foot in a single immersive cultural pilgrimage.','shiratori-jinja-habikino','shiratori-jinja-habikino',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11629036','西流','Nishi-nagare','博多祇園山笠や博多松囃子（博多どんたく）の運営における構成単位である流の一つ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%A5%BF%E6%B5%81',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11613747','舟っこ流し','Funekko Nagashi','盆の送り火・精霊舟の一種','annual event in Morioka, Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%88%9F%E3%81%A3%E3%81%93%E6%B5%81%E3%81%97',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11596078','秦野たばこ祭','Hadano Tobacco Festival',NULL,NULL,'Q460806','秦野市','Hadano',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A7%A6%E9%87%8E%E3%81%9F%E3%81%B0%E3%81%93%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11586814','石清水祭','Iwashimizu-sai','京都府八幡市の石清水八幡宮の例祭',NULL,'Q710098','石清水八幡宮','Iwashimizu Hachimangū','京都府','kinki',NULL,NULL,863,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%9F%B3%E6%B8%85%E6%B0%B4%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11582543','相馬野馬追','Sōma Nomaoi','毎年7月に福島県相馬市および南相馬市で開催される祭り・神事',NULL,NULL,NULL,NULL,'福島県','tohoku',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/The%20Soma%20Nomaoi%202005-5.jpg','https://ja.wikipedia.org/wiki/%E7%9B%B8%E9%A6%AC%E9%87%8E%E9%A6%AC%E8%BF%BD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11612066','能褒野神社','Nobono Shrine','三重県亀山市田村町にある神社','Shinto shrine in Mie Prefecture, Japan',NULL,NULL,NULL,'三重県','kinki',34.886111,136.482778,1895,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Nobono-jinja%20torii.JPG','https://ja.wikipedia.org/wiki/%E8%83%BD%E8%A4%92%E9%87%8E%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

能褒野神社(のぼのじんじゃ)は、三重県亀山市田村町にある神社で、ヤマトタケル(日本武尊)を主祭神として祀る古社である。背後に控える能褒野墓は、宮内庁によりヤマトタケルの陵墓に治定されており、白鳥伝説発祥の地として歴史的価値が極めて高い。

## 歴史

『古事記』『日本書紀』によれば、ヤマトタケルは東国遠征の帰途、伊吹山の神との戦いで深手を負い、伊勢国能褒野の地でこの世を去ったとされる。これがいわゆる「能褒野の物語」であり、その魂は白鳥となって大和、河内へと飛び立ち、各地に白鳥伝説の聖地を残した。能褒野神社は明治12年(1879年)に宮内省がヤマトタケルの陵墓を能褒野王塚古墳に治定したことを受け、明治28年(1895年)に正式に創建された比較的新しい社だが、伝承の歴史は古代まで遡る。

## 見どころ

社殿は明治期の神社建築様式で整えられ、深い杜に囲まれた静謐な境内が広がる。背後の能褒野王塚古墳(全長約90メートルの前方後円墳)はヤマトタケル陵として宮内庁管理下にあり、神社の聖性を一層高めている。秋季例大祭(10月)には地元による神輿渡御や雅楽の奉納が行われる。

## 開催情報・アクセス

JR関西本線井田川駅から徒歩約25分またはバス利用が便利。境内参拝は終日自由で、能褒野王塚古墳も外周より見学可能。例大祭は毎年10月。

## 周辺観光

亀山市は東海道五十三次の宿場町「亀山宿」「関宿」の歴史的町並みが残り、特に関宿は重要伝統的建造物群保存地区として人気が高い。鈴鹿サーキット、椿大神社など、伊勢国の古代史と近世東海道文化を一度に楽しめる。','## Overview

Nobono Shrine (Nobono Jinja) is a Shinto shrine located in Tamura-chō, Kameyama City, Mie Prefecture, dedicated to the legendary Prince Yamato Takeru no Mikoto as its principal deity. The Nobono Mausoleum situated behind the shrine has been officially designated by the Imperial Household Agency as the tomb of Yamato Takeru, making the site of exceptional historical significance as the origin point of the famous white swan legend.

## History

According to the Kojiki and Nihon Shoki, Japan''s earliest chronicles, Prince Yamato Takeru sustained grave wounds in a battle with the deity of Mount Ibuki on his return journey from his eastern military campaigns, and ultimately passed away at Nobono in Ise Province. This forms the so-called "Nobono Story," after which his soul is said to have transformed into a white swan that flew toward Yamato and Kawachi provinces, leaving sacred sites associated with the white swan legend across various locations. While the shrine itself is relatively recent—formally established in 1895 (Meiji 28) following the Imperial Household Ministry''s 1879 designation of the Nobono Ōzuka Kofun as Yamato Takeru''s tomb—the legendary history reaches back to ancient times.

## Highlights

The main hall is built in the Meiji-era shrine architectural style, set within a serene precinct enclosed by deep forest. The Nobono Ōzuka Kofun directly behind the shrine—a keyhole-shaped burial mound approximately 90 meters in total length—is administered as Yamato Takeru''s mausoleum by the Imperial Household Agency, lending an additional layer of sacredness to the shrine itself. The autumn grand festival held in October features portable shrine (mikoshi) processions organized by local communities and dedicatory performances of gagaku court music.

## Event Details and Access

The shrine is accessible by an approximately 25-minute walk from Idagawa Station on the JR Kansai Main Line, with bus service also available. The precincts are open for worship throughout the day, and the Nobono Ōzuka Kofun can be viewed from its outer perimeter. The annual grand festival is held each October.

## Surrounding Attractions

Kameyama City preserves the historic post-station town atmospheres of Kameyama-juku and Seki-juku, which formed part of the famous Tōkaidō Fifty-three Stations route during the Edo period. Seki-juku in particular is renowned as a nationally designated Important Preservation District for Groups of Traditional Buildings. Other regional attractions include the Suzuka Circuit racetrack and Tsubaki Grand Shrine, allowing visitors to experience the ancient history of Ise Province alongside the early-modern Tōkaidō culture in a single trip.','nobono-jinja','nobono-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11581191','益子祇園祭','Mashiko Gion Matsuri','栃木県益子町で行われる祇園祭','Gion Matsuri of Mashiko',NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%9B%8A%E5%AD%90%E7%A5%87%E5%9C%92%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11592992','福島わらじまつり','Fukushima Waraji Matsuri',NULL,NULL,NULL,NULL,NULL,'福島県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E5%B3%B6%E3%82%8F%E3%82%89%E3%81%98%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11580520','白鳥おどり','Shirotori Odori','岐阜県郡上市で開催される盆踊り',NULL,NULL,NULL,NULL,'岐阜県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%99%BD%E9%B3%A5%E3%81%8A%E3%81%A9%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11625215','蘇民祭','Somin-sai','岩手県奥州市をはじめとする日本各地で行われる裸祭り',NULL,NULL,NULL,NULL,'岩手県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%98%87%E6%B0%91%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11621139','葦稲葉神社','Ashiinaba Shrine','徳島県板野郡上板町にある神社','Shinto shrine in Tokushima Prefecture, Japan',NULL,NULL,NULL,'徳島県','shikoku',34.130276,134.412463,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Ashiinaba%20shrine%2C%20Tokushima.jpg','https://ja.wikipedia.org/wiki/%E8%91%A6%E7%A8%B2%E8%91%89%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

葦稲葉神社(あしいなばじんじゃ)は、徳島県板野郡上板町神宅(かんやけ)に鎮座する式内社で、葦稲羽神(あしいなばのかみ)を主祭神として祀る古社である。『延喜式神名帳』に記載される阿波国板野郡の式内社の一座であり、稲作・五穀豊穣信仰の中心として地域住民に崇敬されてきた。

## 歴史

創建年代は不詳だが、『延喜式神名帳』(927年)に式内社として記載され、少なくとも平安時代以前に遡る古社であることが確認される。祭神の葦稲羽神は『古事記』神話に登場する大国主神と関わる神格と推定され、葦原と稲作を象徴する地母神的存在として崇敬された。阿波国(現徳島県)は古代から麻・藍・稲作で知られ、葦稲羽神への信仰は阿波の農耕文化の根幹に位置する。中世以降は地域の鎮守として存続し、明治期の社格制度では郷社に列せられた。

## 見どころ

社殿は近世以降の建築で、地元産の自然石を用いた素朴な石垣と簡素な拝殿が田園風景と調和する。境内には樹齢数百年とされる神木があり、農村信仰の素朴な雰囲気が残されている。例祭は秋季10月で、地元の氏子による神事と新穀奉納が行われ、現代でも農耕儀礼の伝統が継承されている。

## 開催情報・アクセス

JR徳島線板野駅から車・タクシーで約15分。境内参拝は終日自由。秋季例祭は毎年10月。

## 周辺観光

上板町・板野町一帯は阿波藍の本場として知られ、藍染体験施設や歴史的な藍商の屋敷が点在する。徳島県内では大塚国際美術館(鳴門市)、霊山寺をはじめとする四国八十八ヶ所霊場巡礼の起点が近く、信仰と工芸文化を一度に体験できる。','## Overview

Ashiinaba Shrine (Ashiinaba Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Kanyake, Kamiita Town, Itano District, Tokushima Prefecture. The shrine enshrines Ashiinaba no Kami as its principal deity and is one of the Engishiki-registered shrines of Itano District in Awa Province, having been revered by local residents for centuries as a central place of worship for rice cultivation and agricultural prosperity.

## History

Though the founding date is unknown, the shrine is recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927, confirming its existence as an ancient shrine reaching at least as far back as the Heian period. The enshrined deity Ashiinaba no Kami is considered to be related to Ōkuninushi no Kami appearing in the Kojiki mythology and was venerated as a mother-earth-like deity symbolizing reed plains and rice cultivation. Awa Province (present-day Tokushima Prefecture) has been known since ancient times for hemp, indigo, and rice cultivation, and worship of Ashiinaba no Kami occupies a fundamental position in the agricultural culture of Awa. The shrine continued as a regional guardian deity throughout the medieval period and was ranked as a Gōsha (district shrine) under the Meiji-era shrine ranking system.

## Highlights

The shrine buildings date from the early modern period onward, featuring rustic stone walls constructed from locally quarried natural stones and a simple worship hall (haiden) that harmonizes beautifully with the surrounding rural landscape. The precincts contain sacred trees estimated to be several centuries old, preserving the unpretentious atmosphere of rural folk faith. The annual main festival is held in October, when local parishioners conduct sacred rituals and offer freshly harvested grain, continuing agricultural ceremonial traditions that survive to this day.

## Event Details and Access

The shrine is accessible by car or taxi in approximately 15 minutes from Itano Station on the JR Tokushima Line. The precincts are open for worship throughout the day, and the autumn main festival is held in October each year.

## Surrounding Attractions

The Kamiita and Itano area is renowned as the heartland of Awa indigo dyeing, with numerous indigo-dyeing experience facilities and historic indigo merchant residences scattered throughout the region. Within Tokushima Prefecture, the Otsuka Museum of Art in Naruto City and the starting points of the Shikoku Eighty-Eight Temple Pilgrimage at Ryōzenji Temple are nearby, allowing visitors to experience both traditional faith culture and craft heritage in a single visit.','ashiinaba-jinja','ashiinaba-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11594455','福野夜高祭','Fukuno Yotaka Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E9%87%8E%E5%A4%9C%E9%AB%98%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11611950','能地春祭り','Nochi Spring Festival',NULL,'festival in Hiroshima Prefecture, Japan','Q820760','三原市','Mihara',NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E8%83%BD%E5%9C%B0%E6%98%A5%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11618171','草津国際音楽アカデミー&フェスティバル','Kusatsu International Summer Music Academy & Festival','日本の群馬県草津温泉で毎年夏に開催される音楽祭',NULL,NULL,NULL,NULL,'群馬県','kanto',NULL,NULL,1980,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E8%8D%89%E6%B4%A5%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E3%82%A2%E3%82%AB%E3%83%87%E3%83%9F%E3%83%BC%26%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB%E5%A4%A9%E7%8B%97%E5%B1%B1%E3%83%AC%E3%82%B9%E3%83%88%E3%83%8F%E3%82%A6%E3%82%B9.jpg','https://ja.wikipedia.org/wiki/%E8%8D%89%E6%B4%A5%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E3%82%A2%E3%82%AB%E3%83%87%E3%83%9F%E3%83%BC%26%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11602813','筑後川花火大会','Chikugo River Fireworks Festival','福岡県久留米市で開催される花火大会','Shinto shrine in Kurume, Japan','Q954320','筑後川','Chikugo River','福岡県','kyushu',NULL,NULL,1650,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/ColorfulFireworks.png','https://ja.wikipedia.org/wiki/%E7%AD%91%E5%BE%8C%E5%B7%9D%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11594894','秋吉台国際20世紀音楽セミナー&フェスティバル','Akiyoshidai International Contemporary Music Seminar and Festival',NULL,NULL,NULL,NULL,NULL,'山口県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A7%8B%E5%90%89%E5%8F%B0%E5%9B%BD%E9%9A%9B20%E4%B8%96%E7%B4%80%E9%9F%B3%E6%A5%BD%E3%82%BB%E3%83%9F%E3%83%8A%E3%83%BC%26%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11590440','神武天皇祭','Emperor Jinmu Festival','神武天皇を祭る皇室の祭祀',NULL,'Q62756148','畝傍山東北陵','Unebiyama-no-Ushitora-no-Sumi-no-Misasagi',NULL,NULL,NULL,NULL,1860,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Jinmusai-fes1.jpg','https://ja.wikipedia.org/wiki/%E7%A5%9E%E6%AD%A6%E5%A4%A9%E7%9A%87%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11622981','藤原まつり','Fujiwara Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%97%A4%E5%8E%9F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11585601','石崎奉燈祭','Issaki Hōtō Festival','石川県七尾市で開催されるキリコ祭り',NULL,NULL,NULL,NULL,'石川県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%9F%B3%E5%B4%8E%E5%A5%89%E7%87%88%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11603286','管絃祭','Kangensai','厳島神社の祭礼',NULL,'Q114575','広島湾','Hiroshima Bay',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Kangen%20jigozen2.jpg','https://ja.wikipedia.org/wiki/%E7%AE%A1%E7%B5%83%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11599004','竹割り祭り','Takewari Festival',NULL,NULL,'Q11619342','菅生石部神社','Sugō Isobe Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%AB%B9%E5%89%B2%E3%82%8A%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11582690','県祭り','Agata Matsuri','京都府宇治市の祭',NULL,'Q11608139','縣神社','Agata Shrine','京都府','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Bonten%20togyo.jpg','https://ja.wikipedia.org/wiki/%E7%9C%8C%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11603039','筒井町出来町天王祭','Tsutsui-chō Deki-machi Tennō-sai',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%AD%92%E4%BA%95%E7%94%BA%E5%87%BA%E6%9D%A5%E7%94%BA%E5%A4%A9%E7%8E%8B%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11628729','西条祭り','Saijo Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%A5%BF%E6%9D%A1%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11589725','神戸まつり','Kobe Matsuri',NULL,NULL,NULL,NULL,NULL,'兵庫県','kinki',NULL,NULL,1971,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/2010%20Kobe%20Matsuri00s3s4050.jpg','https://ja.wikipedia.org/wiki/%E7%A5%9E%E6%88%B8%E3%81%BE%E3%81%A4%E3%82%8A',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11604835','糸満ハーレー','Itoman Hārē',NULL,NULL,'Q860662','糸満市','Itoman',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E7%B3%B8%E6%BA%80%E3%83%8F%E3%83%BC%E3%83%AC%E3%83%BC.jpg','https://ja.wikipedia.org/wiki/%E7%B3%B8%E6%BA%80%E3%83%8F%E3%83%BC%E3%83%AC%E3%83%BC',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11603435','節分会はだか祭り','Setsubunkai Hadaka Matsuri',NULL,NULL,'Q11452340','宝光院 (大垣市)',NULL,'岐阜県','chubu',NULL,NULL,NULL,NULL,'winter',NULL,'https://ja.wikipedia.org/wiki/%E7%AF%80%E5%88%86%E4%BC%9A%E3%81%AF%E3%81%A0%E3%81%8B%E7%A5%AD%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11590283','神明の花火大会','Shinmei Fireworks Festival','山梨県西八代郡市川三郷町で行われる花火大会',NULL,'Q1204453','市川三郷町','Ichikawamisato','山梨県','chubu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%A5%9E%E6%98%8E%E3%81%AE%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11581773','直方山笠',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%9B%B4%E6%96%B9%E5%B1%B1%E7%AC%A0',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11582129','相模原納涼花火大会',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%9B%B8%E6%A8%A1%E5%8E%9F%E7%B4%8D%E6%B6%BC%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11585201','石動曳山祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E7%9F%B3%E5%8B%95%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11586462','石巻川開き祭り',NULL,NULL,NULL,NULL,NULL,NULL,'宮城県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%9F%B3%E5%B7%BB%E5%B7%9D%E9%96%8B%E3%81%8D%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11587641','砺波夜高祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A0%BA%E6%B3%A2%E5%A4%9C%E9%AB%98%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11591238','福井フェニックスまつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E4%BA%95%E3%83%95%E3%82%A7%E3%83%8B%E3%83%83%E3%82%AF%E3%82%B9%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11591996','福山ばら祭',NULL,NULL,NULL,NULL,NULL,NULL,'広島県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E5%B1%B1%E3%81%B0%E3%82%89%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11594028','福生七夕まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%A6%8F%E7%94%9F%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11584632','知立まつり','Chiryū Festival','愛知県知立市で開催される祭礼','festival in Chiryu city, Aichi prefecture, Japan','Q11584639','知立神社','Chiryū Shrine','愛知県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tiryuumatsuri7.JPG','https://ja.wikipedia.org/wiki/%E7%9F%A5%E7%AB%8B%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11602875','筑波山梅まつり',NULL,NULL,NULL,NULL,NULL,NULL,'茨城県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%AD%91%E6%B3%A2%E5%B1%B1%E6%A2%85%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11603787','篠田の花火',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%AF%A0%E7%94%B0%E3%81%AE%E8%8A%B1%E7%81%AB',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11604063','米子がいな祭',NULL,NULL,NULL,NULL,NULL,NULL,'鳥取県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%B1%B3%E5%AD%90%E3%81%8C%E3%81%84%E3%81%AA%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11581335','盛岡さんさ踊り','Morioka Sansa Odori','岩手県盛岡市にて行われる祭り','festival in Morioka, Japan','Q11363800','中央通り','Central Avenue','岩手県','tohoku',NULL,NULL,1978,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Sansa%20Odori%202.JPG','https://ja.wikipedia.org/wiki/%E7%9B%9B%E5%B2%A1%E3%81%95%E3%82%93%E3%81%95%E8%B8%8A%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11611763','胡子講','Ebisukō','広島市中区の胡子神社で開かれる祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Ebisu%20street.jpg','https://ja.wikipedia.org/wiki/%E8%83%A1%E5%AD%90%E8%AC%9B',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11617035','茂原七夕まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E8%8C%82%E5%8E%9F%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11622475','薬師祭植木市',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%96%AC%E5%B8%AB%E7%A5%AD%E6%A4%8D%E6%9C%A8%E5%B8%82',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11580506','白鬚神社の田楽',NULL,'佐賀県佐賀市に伝わる民俗芸能',NULL,'Q11580503','白鬚神社','Shirahige Shrine','福岡県','kyushu',33.332142,130.325536,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%99%BD%E9%AC%9A%E7%A5%9E%E7%A4%BE%E3%81%AE%E7%94%B0%E6%A5%BD',NULL,50,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11582264','相生ペーロン祭','Aioi Peron Matsuri',NULL,NULL,NULL,NULL,NULL,'兵庫県','kinki',34.7822598,134.4710824,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Aioi%20Peron%20Matsuri%20July09%20325.jpg','https://ja.wikipedia.org/wiki/%E7%9B%B8%E7%94%9F%E3%83%9A%E3%83%BC%E3%83%AD%E3%83%B3%E7%A5%AD',NULL,90,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11621265','蒲原まつり','Kanbara Matsuri','新潟市の祭事',NULL,'Q63148107','蒲原神社','Kanbara Shrine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%92%B2%E5%8E%9F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11596149','秩父神社御田植祭','Chichibu Shrine Otauesai','埼玉県秩父市の秩父神社で催される御田植祭',NULL,'Q2963366','秩父神社','Chichibu Shrine','埼玉県','kanto',NULL,NULL,1659,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A7%A9%E7%88%B6%E7%A5%9E%E7%A4%BE%E5%BE%A1%E7%94%B0%E6%A4%8D%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11620393','萩夏まつり','Hagi Summer Festival',NULL,NULL,NULL,NULL,NULL,'山口県','chugoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%90%A9%E5%A4%8F%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11628376','西日本大濠花火大会','Nishinippon Ohori Fireworks Festival','福岡市で1949年から2018年まで開催されていた花火大会',NULL,'Q846710','大濠公園','Ōhori Park',NULL,NULL,NULL,NULL,1949,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Nishi-Nippon%20Ohori%20Fireworks%20Festival%202009.jpg','https://ja.wikipedia.org/wiki/%E8%A5%BF%E6%97%A5%E6%9C%AC%E5%A4%A7%E6%BF%A0%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11611892','能代役七夕','Noshiro Yakutanabata',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E8%83%BD%E4%BB%A3%E5%BD%B9%E4%B8%83%E5%A4%95',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11613284','臼杵祇園まつり','Usuki Gion Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%87%BC%E6%9D%B5%E7%A5%87%E5%9C%92%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11620954','葛木坐火雷神社','Katsuraki ni Imasu Honoikaduchi Shrine','奈良県葛城市笛吹にある神社','Shinto shrine in Nara Prefecture, Japan',NULL,NULL,NULL,'奈良県','kinki',34.47164,135.710049,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Katsuragi-imasuhonoikaduchi-jinja%20haiden1.jpg','https://ja.wikipedia.org/wiki/%E8%91%9B%E6%9C%A8%E5%9D%90%E7%81%AB%E9%9B%B7%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

葛木坐火雷神社(かつらきにいますほのいかづちじんじゃ)は、奈良県葛城市笛吹に鎮座する式内大社で、火雷大神(ほのいかづちのおおかみ)と天香山命(あめのかぐやまのみこと)を祀る古社である。通称「笛吹神社」とも呼ばれ、雷神信仰と古代豪族・笛吹連(ふえふきのむらじ)との結びつきで知られる。

## 歴史

『延喜式神名帳』(927年)に大社として記載される式内大社で、創建年代は不詳ながら少なくとも奈良時代以前に遡る。祭神の天香山命は神武天皇東征に従った神とされ、その子孫が笛吹連を名乗り、宮中の音楽・祭祀を司った。火雷大神は雷・火・雨を司る神であり、農耕と密接に結びつく信仰として大和盆地南西部一帯で篤く崇敬された。中世以降は神仏習合のもと天台宗系の管理下にあったが、明治の神仏分離で純粋な神社として再整備された。

## 見どころ

本殿は江戸時代の建立で、檜皮葺の落ち着いた佇まいが特徴。境内には日露戦争で使用された大砲が奉納されており、地域の近代史とのつながりも垣間見える。雅楽・古代楽器に関わる祭神を祀ることから、笛・楽器奉納の風習が今も残る。例祭は10月10日前後で、神事と地元住民による奉納行事が行われる。

## 開催情報・アクセス

近鉄御所線忍海駅または葛城駅から車・タクシーで約10分。境内参拝は終日自由。例祭は毎年10月の指定日に執り行われる。

## 周辺観光

葛城地域は古代豪族・葛城氏の本拠地として知られ、一言主神社、高鴨神社、九品寺など格式高い古社・古刹が点在する。近隣には葛城山ロープウェイがあり、四季折々の登山・自然観光も楽しめる。','## Overview

Katsuraki ni Imasu Honoikaduchi Shrine (Katsuraki ni Imasu Honoikaduchi Jinja) is an ancient Shikinai Taisha (major shrine listed in the 10th-century Engishiki register) located in Fuefuki, Katsuragi City, Nara Prefecture. It enshrines Honoikaduchi no Ōkami—the great thunder, fire, and rain deity—together with Ame no Kaguyama no Mikoto. Commonly known as Fuefuki Shrine, it is renowned for its association with thunder god worship and its deep connection to the ancient Fuefuki no Muraji clan.

## History

The shrine is recorded as a major shrine in the Engishiki Jinmyōchō (Register of Deities) compiled in 927, with its founding date unknown but reaching at least as far back as before the Nara period. Ame no Kaguyama no Mikoto, one of the enshrined deities, is said to have accompanied Emperor Jinmu on his eastern campaign, and his descendants took the name Fuefuki no Muraji and served as masters of music and ritual at the imperial court. Honoikaduchi no Ōkami governs thunder, fire, and rain, and was deeply venerated throughout the southwestern Yamato Basin as a deity intimately connected to agriculture. From the medieval period onward, the shrine fell under the management of Tendai Buddhism through Shinto-Buddhist syncretism, but it was reorganized as a purely Shinto shrine following the Meiji-era separation of Shinto and Buddhism.

## Highlights

The main hall was built during the Edo period and features a refined cypress bark-shingled (hiwadabuki) construction. Within the precincts, a cannon used in the Russo-Japanese War has been dedicated, offering a glimpse into the shrine''s connection with modern regional history. Because the enshrined deity is associated with ancient music and instruments, the custom of dedicating flutes and other musical instruments persists to this day. The annual main festival is held around October 10, featuring sacred rituals and dedicatory ceremonies performed by local residents.

## Event Details and Access

The shrine is accessible by car or taxi in approximately 10 minutes from either Oshimi Station or Katsuragi Station on the Kintetsu Gose Line. The precincts are open for worship throughout the day, and the annual main festival is conducted on a designated date in October each year.

## Surrounding Attractions

The Katsuragi region was the stronghold of the ancient Katsuragi clan, and the area is dotted with prestigious ancient shrines and temples including Hitokotonushi Shrine, Takakamo Shrine, and Kuhonji Temple. Nearby, the Katsuragi-yama Ropeway provides access to hiking and seasonal nature tourism opportunities, making the area an excellent destination for combining ancient history with natural scenery.','katsuraki-ni-imasu-honoikaduchi-jinja','katsuraki-ni-imasu-honoikaduchi-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11615686','花輪ばやし','Hanawa Bayashi','秋田県鹿角市花輪の祭り',NULL,NULL,NULL,NULL,'秋田県','tohoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Hanawabayashi%202012.JPG','https://ja.wikipedia.org/wiki/%E8%8A%B1%E8%BC%AA%E3%81%B0%E3%82%84%E3%81%97',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11597870','立川まつり国営昭和記念公園花火大会','Showa Kinen Park Fireworks',NULL,NULL,'Q3915473','国営昭和記念公園','Shōwa Memorial Park',NULL,NULL,NULL,NULL,1954,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E7%AB%8B%E5%B7%9D%E3%81%BE%E3%81%A4%E3%82%8A%E5%9B%BD%E5%96%B6%E6%98%AD%E5%92%8C%E8%A8%98%E5%BF%B5%E5%85%AC%E5%9C%92%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11596130','秩父川瀬祭','Chichibu Kawase Matsuri','毎年7月に開催される埼玉県秩父市の祭り',NULL,'Q2963366','秩父神社','Chichibu Shrine','埼玉県','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Chichibu%20Kawase%20Matsuri.jpg','https://ja.wikipedia.org/wiki/%E7%A7%A9%E7%88%B6%E5%B7%9D%E7%80%AC%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17209977','漢字の日','Kanji Day',NULL,'annual event celebrating kanji','Q221716','清水寺','Kiyomizu-dera Temple','京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%BC%A2%E5%AD%97%E3%81%AE%E6%97%A5',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11662545','青森花火大会','Aomori Fireworks Display',NULL,'Fireworks show in Japan','Q11662157','青森港','Port of Aomori',NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E9%9D%92%E6%A3%AE%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11642088','三熊野神社大祭','Mikumano Jinja Taisai','静岡県掛川市の三熊野神社の祭礼','festival by Mikumano Jinja in Kakegawa City, Shizuoka Prefecture, Japan','Q823988','掛川市','Kakegawa','静岡県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Mikumano%20Jinja%20Taisai%202009%2020090404.jpg','https://ja.wikipedia.org/wiki/%E9%81%A0%E5%B7%9E%E6%A8%AA%E9%A0%88%E8%B3%80%E4%B8%89%E7%86%8A%E9%87%8E%E7%A5%9E%E7%A4%BE%E5%A4%A7%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q12624253','日韓交流おまつり',NULL,NULL,NULL,'Q8684','ソウル特別市','Seoul',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E6%97%A5%E9%9F%93%E4%BA%A4%E6%B5%81%E3%81%8A%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11630000','西馬音内の盆踊','Nishimonai no Bon-odori','秋田県羽後町に伝わる盆踊り',NULL,NULL,NULL,NULL,'秋田県','tohoku',39.199556,140.403222,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Nishimonai%20Bon%20Odori.jpg','https://ja.wikipedia.org/wiki/%E8%A5%BF%E9%A6%AC%E9%9F%B3%E5%86%85%E3%81%AE%E7%9B%86%E8%B8%8A',NULL,95,'drafted','## 概要

西馬音内の盆踊(にしもないのぼんおどり)は、秋田県雄勝郡羽後町西馬音内で毎年8月16日から18日にかけて行われる伝統盆踊りで、岐阜県の郡上踊り、徳島県の阿波踊りと並んで「日本三大盆踊り」の一つに数えられる。約700年の歴史を持つとされ、1981年(昭和56年)に国の重要無形民俗文化財に指定された。

## 歴史

西馬音内の盆踊の起源は鎌倉時代末期の正応年間(1288〜1293年)に修行僧・源親(げんしん)が蔵王権現の堂前で豊年祈願として行ったのが始まりとされる。その後、慶長6年(1601年)に西馬音内城主・小野寺氏が滅亡し、亡霊を弔う踊りと習合して現在の盆踊りの形になったと伝わる。「彦三頭巾(ひこさずきん)」と呼ばれる黒い覆面、「端縫い(はぬい)」と呼ばれる継ぎ接ぎ衣装と編み笠で踊り手が顔を隠す独特の様式が特徴で、亡霊の踊りとも称される神秘的な雰囲気を醸し出す。

## 見どころ

囃子(はやし)の音色と「がんけ」「音頭」の2種類の踊りが繰り返され、3日間延べ約10万人の観客が訪れる。編み笠と彦三頭巾で顔を覆った踊り手たちが、ゆるやかなのに艶めかしく、しなやかでありながら張りのある所作で篝火の周りを静かに巡る姿は、観る者に時代を超えた感動を与える。

## 開催情報・アクセス

会場は秋田県雄勝郡羽後町西馬音内本町通り。JR奥羽本線湯沢駅から羽後交通バスで約30分。観覧は無料。

## 周辺観光

羽後町は美しい里山風景に囲まれ、近隣には湯沢市の小安峡温泉、稲庭うどんの里、横手のかまくらなど秋田県南部の観光資源が集中する。8月は雄勝の伝統行事と温泉を組み合わせた旅行が定番。','## Overview

Nishimonai no Bon-odori (Nishimonai Bon Dance) is a traditional Bon dance held annually from August 16 to 18 in Nishimonai, Ugo Town, Ogachi District, Akita Prefecture. It ranks alongside Gujō Odori in Gifu Prefecture and Awa Odori in Tokushima Prefecture as one of the "Three Great Bon Dances of Japan." With a history reportedly spanning approximately 700 years, it was designated as a National Important Intangible Folk Cultural Property in 1981 (Shōwa 56).

## History

The origins of the Nishimonai Bon-odori are traced to the Shōō era (1288–1293) at the end of the Kamakura period, when the ascetic monk Genshin is said to have performed dances in front of the Zaō Gongen hall as prayers for bountiful harvests. Subsequently, following the destruction of the Onodera clan, lords of Nishimonai Castle, in 1601 (Keichō 6), the dance is believed to have merged with mourning rituals for the spirits of the deceased, taking on its present form as a Bon dance. The distinctive style features dancers concealing their faces with black hoods called "Hikosa-zukin" and patchwork garments called "Hanui" combined with woven straw hats. This face-concealing tradition has earned the dance the nickname "the dance of spirits," lending it a mysterious atmosphere unmatched in Japanese folk performing arts.

## Highlights

To the accompaniment of traditional festival music (hayashi), two types of dance—"Ganke" and "Ondo"—are performed in alternation, drawing approximately 100,000 spectators over the three-day event. Dancers concealing their faces behind woven hats and Hikosa-zukin hoods move slowly yet sensually, gracefully yet firmly around the central bonfires, creating a hauntingly beautiful spectacle that conveys to viewers a deep emotional resonance transcending the centuries.

## Event Details and Access

The venue is Honchō Street in Nishimonai, Ugo Town, Ogachi District, Akita Prefecture. Access is approximately 30 minutes by Ugo Kōtsū bus from Yuzawa Station on the JR Ōu Main Line. Viewing the dance is free of charge.

## Surrounding Attractions

Ugo Town is nestled within picturesque satoyama countryside landscapes, with nearby attractions concentrating the tourism resources of southern Akita Prefecture, including Oyasukyō Hot Spring in Yuzawa City, the home village of Inaniwa udon noodles, and the kamakura snow huts of Yokote. August in particular offers an ideal opportunity to combine traditional festivals of the Ogachi region with hot spring tourism in a memorable cultural journey.','nishimonai-no-bon-odori','nishimonai-no-bon-odori',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11670289','高松冬のまつり','Takamatsu Fuyu no Matsuri',NULL,'festival in Takamatsu, Japan',NULL,NULL,NULL,'香川県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E6%9D%BE%E5%86%AC%E3%81%AE%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11642072','遠州はまきた飛竜まつり','Hamakita Hiryū festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%81%A0%E5%B7%9E%E3%81%AF%E3%81%BE%E3%81%8D%E3%81%9F%E9%A3%9B%E7%AB%9C%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11633921','豊浜ちょうさ祭','Toyohama Chōsa Festival','香川県観音寺市豊浜町で行われる祭礼',NULL,NULL,NULL,NULL,'香川県','shikoku',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Toyohama%20Chosa%20example%20Apr%2001%202021%2004-45PM.jpeg','https://ja.wikipedia.org/wiki/%E8%B1%8A%E6%B5%9C%E3%81%A1%E3%82%87%E3%81%86%E3%81%95%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11662899','静岡まつり','Shizuoka Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%9D%99%E5%B2%A1%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q16638525','長岡京ガラシャ祭','Garasha Matsuri',NULL,NULL,NULL,NULL,NULL,'新潟県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11657228','阿佐谷七夕まつり','Asagaya Tanabata Festival','日本の東京都杉並区阿佐ヶ谷駅前で毎年8月に開かれる七夕祭り',NULL,'Q11657226','阿佐谷パールセンター','Asagaya Pearl Center','東京都','kanto',NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Asagaya%20Tanabata%202015%2011.JPG','https://ja.wikipedia.org/wiki/%E9%98%BF%E4%BD%90%E8%B0%B7%E4%B8%83%E5%A4%95%E3%81%BE%E3%81%A4%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11634237','豊見城ハーリー','Tomigusuku Hārī',NULL,NULL,'Q371446','豊見城市','Tomigusuku',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Tomishiro%20ha-ri.jpg','https://ja.wikipedia.org/wiki/%E8%B1%8A%E8%A6%8B%E5%9F%8E%E3%83%8F%E3%83%BC%E3%83%AA%E3%83%BC',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11636486','越後三大花火',NULL,'新潟県内で行われる3つの花火大会 (ぎおん柏崎まつり、長岡まつり、片貝まつり) の総称',NULL,NULL,NULL,NULL,'新潟県','chubu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E8%B6%8A%E5%BE%8C%E4%B8%89%E5%A4%A7%E8%8A%B1%E7%81%AB',NULL,40,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11644507','采女祭','Uneme Matsuri','奈良県奈良市の采女神社の例祭',NULL,'Q22118013','采女神社','Uneme Shrine','奈良県','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Uneme%20Matsuri%20Festival%202015092702.jpg','https://ja.wikipedia.org/wiki/%E9%87%87%E5%A5%B3%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q16272167','花祭り','Hana matsuri','釈迦の誕生日を祝う祭り（灌仏会）に対する日本語の名称。名称の発生は明治期','Buddha''s birthday festival in Japan',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/A%20birthday%20of%20Buddha%2Chanamatsuri%2Ckanpukuji-temple%2Ckatori-city%2Cjapan.JPG',NULL,NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11655139','閃光ライオット','Senko Riot','10代アーティストのみによる日本のロック・フェスティバル','Japanese music festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,2008,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%96%83%E5%85%89%E3%83%A9%E3%82%A4%E3%82%AA%E3%83%83%E3%83%88',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11678799','黒船祭','Shimoda Black Ship Festival','静岡県下田市で開催される祭',NULL,'Q653402','下田市','Shimoda','静岡県','chubu',NULL,NULL,NULL,5,'spring',NULL,'https://ja.wikipedia.org/wiki/%E9%BB%92%E8%88%B9%E7%A5%AD',NULL,70,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11678183','黒崎祇園山笠','Kurosaki Gion Yamagasa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Kurosakigionn3.JPG','https://ja.wikipedia.org/wiki/%E9%BB%92%E5%B4%8E%E7%A5%87%E5%9C%92%E5%B1%B1%E7%AC%A0',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11667185','香取神宮御田植祭','Otaue Festival at Katori Jingū',NULL,NULL,'Q372380','香取神宮','Katori Jingū','千葉県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Rice-transplanting%20Festival%20in%20Katori-jingu%201%2Ckatori-city%2Cjapan.jpg','https://ja.wikipedia.org/wiki/%E9%A6%99%E5%8F%96%E7%A5%9E%E5%AE%AE%E5%BE%A1%E7%94%B0%E6%A4%8D%E7%A5%AD',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17193576','今宮祭','Imamiya Matsuri',NULL,NULL,'Q500955','今宮神社','Imamiya Shrine',NULL,NULL,NULL,NULL,994,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Imamiya%20shrine%20Kanko-sai%202013-05B.JPG','https://ja.wikipedia.org/wiki/%E4%BB%8A%E5%AE%AE%E7%A5%AD',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11642725','那売佐神社','Namesa Shrine','島根県出雲市東神西町にある神社','Shinto shrine in Shimane Prefecture, Japan',NULL,NULL,NULL,'島根県','chugoku',35.314364,132.699845,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Namesajinjahonden.JPG','https://ja.wikipedia.org/wiki/%E9%82%A3%E5%A3%B2%E4%BD%90%E7%A5%9E%E7%A4%BE',NULL,95,'drafted','## 概要

那売佐神社(なめさじんじゃ)は、島根県出雲市東神西町(ひがしじんざいちょう)に鎮座する式内社で、葦原醜男命(あしはらしこおのみこと、大国主神の別名)を主祭神として祀る古社である。『延喜式神名帳』に記載される出雲国神門郡の式内社の一座で、出雲神話の中核をなす大国主信仰の一翼を担う。

## 歴史

『延喜式神名帳』(927年)に式内社として記載される那売佐神社は、創建年代は不詳ながら、出雲国風土記(733年成立)にも関連記述があり、奈良時代以前まで遡る古社である。祭神の葦原醜男命は大国主神の異名で、国土経営と医薬・縁結びの神として知られる。出雲地方は古代より大国主神を中心とした神話体系の本拠地であり、那売佐神社もそうした出雲信仰の枠組みの中で地域の中核的存在として機能してきた。中世以降は地元の鎮守として存続し、明治期に郷社に列せられた。

## 見どころ

社殿は出雲大社造を簡素化した近世建築で、出雲地方特有の大社造系の意匠を残す。境内には古代神西湖の名残を伝える地形が見られ、出雲国風土記の世界観を体感できる場所として研究者にも注目されている。例祭は秋季10月で、地元氏子による神事と神楽の奉納が行われる。

## 開催情報・アクセス

JR山陰本線出雲市駅から車・タクシーで約20分。一畑バスの神西経由路線も利用可能。境内参拝は終日自由。秋季例祭は毎年10月。

## 周辺観光

出雲市内には出雲大社(縁結びの神様)、稲佐の浜、日御碕神社・日御碕灯台、出雲文化伝承館など、出雲神話の聖地が集中する。神西湖周辺は静かな田園地帯で、神話の里らしい風情が今も残る。','## Overview

Namesa Shrine (Namesa Jinja) is an ancient Shikinaisha (shrine listed in the 10th-century Engishiki register) located in Higashi-Jinzai-chō, Izumo City, Shimane Prefecture. The shrine enshrines Ashihara Shikoo no Mikoto—another name for Ōkuninushi no Kami—as its principal deity, and is one of the Shikinaisha shrines of Kando District in Izumo Province. It plays an integral role in the worship of Ōkuninushi, which forms the core of Izumo mythology.

## History

Recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927, Namesa Shrine has an unknown founding date but appears in related descriptions within the Izumo no Kuni Fudoki (Records of Izumo Province) compiled in 733, confirming its existence as an ancient shrine reaching back at least to before the Nara period. The enshrined deity Ashihara Shikoo no Mikoto is an alternative name for Ōkuninushi no Kami, known as the deity of nation-building, medicine, and matchmaking. The Izumo region has served as the heartland of the mythological system centered on Ōkuninushi no Kami since ancient times, and Namesa Shrine has functioned as a regional anchor within this framework of Izumo belief. The shrine continued as a local guardian deity throughout the medieval period and was ranked as a Gōsha (district shrine) under the Meiji-era shrine ranking system.

## Highlights

The main shrine hall is a simplified early-modern construction in the Izumo Taisha-zukuri style, preserving design elements distinctive to the Taisha-zukuri tradition characteristic of the Izumo region. Within the precincts, topographical features preserving traces of the ancient Lake Jinzai can be observed, attracting attention from researchers as a location where visitors can experience the worldview of the Izumo no Kuni Fudoki firsthand. The annual main festival is held in October, featuring sacred rituals and dedicatory kagura sacred dance performances offered by local parishioners.

## Event Details and Access

The shrine is accessible by car or taxi in approximately 20 minutes from Izumo City Station on the JR San''in Main Line, with Ichibata Bus service via Jinzai also available. The precincts are open for worship throughout the day, and the autumn main festival is held in October each year.

## Surrounding Attractions

Izumo City is dense with sacred sites of Izumo mythology, including the famous Izumo Taisha Grand Shrine (deity of matchmaking), Inasa Beach where deities are said to convene, Hinomisaki Shrine and the historic Hinomisaki Lighthouse, and the Izumo Cultural Heritage Museum. The area around Lake Jinzai remains a quiet rural landscape that still preserves the atmosphere of the legendary "Land of the Gods," offering visitors a serene complement to the more famous sites of central Izumo.','namesa-jinja','namesa-jinja',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11636377','越中八尾曳山祭','Etchuyatsuo parade float festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring','http://commons.wikimedia.org/wiki/Special:FilePath/Yatsuo%20Hikiyama%20Museum.jpg','https://ja.wikipedia.org/wiki/%E8%B6%8A%E4%B8%AD%E5%85%AB%E5%B0%BE%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,80,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11661913','青柏祭','Seihaku Festival','石川県七尾市の大地主神社の例大祭（国の重要無形民俗文化財、ユネスコの無形文化遺産）',NULL,'Q11433686','大地主神社','Ōtokonushi Shrine','石川県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Dekayama%20sanno.jpg','https://ja.wikipedia.org/wiki/%E9%9D%92%E6%9F%8F%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11631901','諏訪湖祭湖上花火大会','Lake Suwa Fireworks Festival','長野県の諏訪湖で行われる花火大会',NULL,'Q1206692','諏訪湖','Lake Suwa','長野県','chubu',36.049167,138.085278,1949,NULL,'summer','http://commons.wikimedia.org/wiki/Special:FilePath/Suwa-ko%20firework%2020080815%2002.jpg','https://ja.wikipedia.org/wiki/%E8%AB%8F%E8%A8%AA%E6%B9%96%E7%A5%AD%E6%B9%96%E4%B8%8A%E8%8A%B1%E7%81%AB%E5%A4%A7%E4%BC%9A',NULL,95,'drafted','## 概要

諏訪湖祭湖上花火大会(すわこまつりこじょうはなびたいかい)は、長野県諏訪市の諏訪湖で毎年8月15日に開催される、約40,000発の花火が打ち上げられる国内最大級の花火大会である。諏訪湖の地形を活かした水中スターマインや、湖面に映る花火の二重映像で知られ、毎年約50万人の観客を集める。

## 歴史

諏訪湖祭湖上花火大会は1949年(昭和24年)、戦後復興の一環として地元有志により始められた。諏訪湖を取り囲む山々に音が反響する独特の音響効果と、湖面に映る花火の幻想的な美しさで早くから評判を呼び、毎年規模が拡大していった。1980年代には全国屈指の花火大会としての地位を確立し、現在では国内最大級の打上数を誇る夏の風物詩となっている。長野県の夏祭りを代表するイベントとして定着している。

## 見どころ

最大の見どころは諏訪湖の水面を活かした「水上スターマイン」と、湖中央から扇状に広がる「Kiss of Fire(大ナイアガラ瀑布)」と呼ばれる仕掛け花火である。山々に囲まれた地形ゆえに花火の音が反響して全身に振動が伝わり、視覚と聴覚の両方で圧倒される。湖面に映り込む花火と相まって、上下対称の光景が広がる。

## 開催情報・アクセス

会場は長野県諏訪市湖畔(諏訪湖畔公園周辺)。JR中央本線上諏訪駅から徒歩約8〜15分。一部有料観覧席あり、その他は湖畔から無料で観覧可能だが場所取りが極めて競争的。

## 周辺観光

諏訪地域は諏訪大社(上社本宮・下社秋宮など四宮)で知られ、御柱祭(7年に一度)でも有名。上諏訪温泉・下諏訪温泉などの温泉地、霧ヶ峰高原、ビーナスライン、北八ヶ岳ロープウェイなど自然観光資源も豊富で、花火大会と組み合わせた旅行が人気。','## Overview

The Lake Suwa Fireworks Festival (Suwako Matsuri Kojō Hanabi Taikai) is one of Japan''s largest fireworks displays, held annually on August 15 at Lake Suwa in Suwa City, Nagano Prefecture, launching approximately 40,000 fireworks. Renowned for its underwater star mine displays leveraging the lake''s distinctive topography and the spectacular double-image effects created by fireworks reflecting on the lake surface, the festival draws approximately 500,000 spectators each year.

## History

The Lake Suwa Fireworks Festival was initiated in 1949 (Shōwa 24) by local volunteers as part of postwar reconstruction efforts. The unique acoustic effects caused by sound reverberating off the mountains surrounding Lake Suwa, combined with the magical beauty of fireworks reflected on the lake''s surface, quickly earned the festival widespread acclaim, and its scale expanded year by year. By the 1980s, it had established itself as one of the nation''s premier fireworks events, and today it has become a defining summer tradition boasting one of the largest launch counts of any fireworks festival in Japan. It is widely regarded as the signature summer event of Nagano Prefecture.

## Highlights

The festival''s main attractions are the "Aquatic Star Mine" displays utilizing the lake''s water surface and the famous "Kiss of Fire" (Dai Niagara Falls)—a spectacular set piece in which fireworks cascade in a fan-shaped pattern from the center of the lake. The mountainous terrain surrounding the venue causes fireworks sounds to reverberate, creating physical vibrations that overwhelm spectators through both visual and auditory channels simultaneously. Combined with the reflections on the lake surface, the result is an awe-inspiring vertically symmetrical light spectacle unique to this location.

## Event Details and Access

The venue is the lakefront in Suwa City, Nagano Prefecture (centered on Lake Suwa Lakefront Park). Access is approximately 8 to 15 minutes on foot from Kami-Suwa Station on the JR Chūō Main Line. Reserved paid seating is available, while general lakefront viewing is free, though securing a viewing spot is highly competitive due to the festival''s enormous popularity.

## Surrounding Attractions

The Suwa region is renowned for the four shrines of Suwa Taisha (including the Kamisha Honmiya and Shimosha Akimiya), and is also famous for the Onbashira Festival held once every seven years. The area boasts abundant natural tourism resources including Kami-Suwa and Shimo-Suwa hot springs, the Kirigamine Highlands, the Venus Line scenic route, and the Kita-Yatsugatake Ropeway, making it a popular destination for combining the fireworks festival with broader sightseeing tours.','lake-suwa-fireworks-festival','lake-suwa-fireworks-festival',NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17193693','岩瀬曳山車祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E5%B2%A9%E7%80%AC%E6%9B%B3%E5%B1%B1%E8%BB%8A%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11669708','高崎まつり','Takasaki Matsuri',NULL,NULL,NULL,NULL,NULL,'群馬県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B4%8E%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11669772','高崎映画祭','Takasaki Film Festival',NULL,NULL,NULL,NULL,NULL,'群馬県','kanto',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B4%8E%E6%98%A0%E7%94%BB%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11644361','酒田祭','Sakata Matsuri',NULL,NULL,NULL,NULL,NULL,'山形県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%85%92%E7%94%B0%E7%A5%AD',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11678732','黒石ねぷた','Kuroishi Neputa','青森県黒石市の祭り',NULL,NULL,NULL,NULL,'青森県','tohoku',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E9%BB%92%E7%9F%B3%E3%81%AD%E3%81%B7%E3%81%9F',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11639333','送り火','okuribi','お盆に帰ってきた死者の魂を現世からふたたびあの世へと送り出す行事','part of the Bon Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Gozanokuribi%20Daimonji2.jpg','https://ja.wikipedia.org/wiki/%E9%80%81%E3%82%8A%E7%81%AB',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11651982','長岡まつり','Nagaoka Festival','毎年8月に日本の新潟県長岡市で開催される祭',NULL,NULL,NULL,NULL,'新潟県','chubu',NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E9%95%B7%E5%B2%A1%E3%81%BE%E3%81%A4%E3%82%8A',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11642810','那覇ハーリー','Naha Hari','沖縄県那覇市で行われるハーリー',NULL,'Q181966','那覇市','Naha','沖縄県','okinawa',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Naha%20Hari.jpg','https://ja.wikipedia.org/wiki/%E9%82%A3%E8%A6%87%E3%83%8F%E3%83%BC%E3%83%AA%E3%83%BC',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11673429','鬼夜','Oniyo',NULL,NULL,'Q11433630','大善寺','Daizenji',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AC%BC%E5%A4%9C',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q16676664','四宮祭り','Shinomiya Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,45,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11653306','長浜曳山祭','Nagahama Hikiyama Festival','滋賀県長浜市で開催される祭',NULL,'Q11653283','長浜八幡宮','Nagahama Hachimangū','滋賀県','kinki',NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E9%95%B7%E6%B5%9C%E6%9B%B3%E5%B1%B1%E7%A5%AD',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11654106','長野びんずる',NULL,NULL,NULL,'Q128849','長野市','Nagano','長野県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%95%B7%E9%87%8E%E3%81%B3%E3%82%93%E3%81%9A%E3%82%8B',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11646842','金子神社祭礼',NULL,'埼玉県入間市にある金子神社の例祭',NULL,'Q11646841','金子神社','Kaneko Shrine','埼玉県','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E4%BE%8B%E5%A4%A7%E7%A5%AD%E3%81%AE%E6%A8%A1%E6%A7%98.JPG','https://ja.wikipedia.org/wiki/%E9%87%91%E5%AD%90%E7%A5%9E%E7%A4%BE%E7%A5%AD%E7%A4%BC',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11652390','長崎ランタンフェスティバル','Nagasaki Lantern Festival','長崎市で行われるイベント',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1987,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%95%B7%E5%B4%8E%E3%83%A9%E3%83%B3%E3%82%BF%E3%83%B3%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11679207','龍勢祭り','Ryusei Matsuri',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E7%A7%A9%E7%88%B6%E5%90%89%E7%94%B0%E3%81%AE%E9%BE%8D%E5%8B%A2',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11675240','鳳だんじり祭り',NULL,NULL,NULL,'Q1042499','西区','Nishi-ku',NULL,NULL,NULL,NULL,NULL,NULL,'autumn','http://commons.wikimedia.org/wiki/Special:FilePath/2022%20Danjiri%20Festival%20at%20Otori%20Shrine%20007.jpg','https://ja.wikipedia.org/wiki/%E9%B3%B3%E3%81%A0%E3%82%93%E3%81%98%E3%82%8A%E7%A5%AD%E3%82%8A',NULL,55,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11669460','高岡といで菜の花フェスティバル','Takaoka Tode Nanohana Festival',NULL,'flower festival in Japan',NULL,NULL,NULL,'富山県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E5%B2%A1%E3%81%A8%E3%81%84%E3%81%A7%E8%8F%9C%E3%81%AE%E8%8A%B1%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%AB',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11663900','鞍馬の火祭','Kurama Himatsuri','京都府京都市左京区鞍馬にある由岐神社例祭の一つ','Festival in Japan','Q11577577','由岐神社','Yuki Shrine','京都府','kinki',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E9%9E%8D%E9%A6%AC%E3%81%AE%E7%81%AB%E7%A5%AD4.jpg','https://ja.wikipedia.org/wiki/%E9%9E%8D%E9%A6%AC%E3%81%AE%E7%81%AB%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q17210171','山王まつり','Sannō Matsuri','富山県富山市にある日枝神社の例大祭','festival in Toyama, Japan','Q11509530','日枝神社','Hie Shrine','富山県','chubu',NULL,NULL,1690,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E5%B1%B1%E7%8E%8B%E3%81%BE%E3%81%A4%E3%82%8A_(%E5%AF%8C%E5%B1%B1%E5%B8%82)',NULL,65,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11643131','郡山うねめまつり','Kōriyama Uneme Festival',NULL,'festival in Kōriyama, Japan',NULL,NULL,NULL,'福島県','tohoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%83%A1%E5%B1%B1%E3%81%86%E3%81%AD%E3%82%81%E3%81%BE%E3%81%A4%E3%82%8A',NULL,60,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11632182','謙信公祭',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%AC%99%E4%BF%A1%E5%85%AC%E7%A5%AD',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11633968','豊田おいでんまつり',NULL,NULL,NULL,NULL,NULL,NULL,'愛知県','chubu',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%B1%8A%E7%94%B0%E3%81%8A%E3%81%84%E3%81%A7%E3%82%93%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11635284','赤れんがフェスタ (舞鶴)',NULL,NULL,NULL,NULL,NULL,NULL,'京都府','kinki',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E8%B5%A4%E3%82%8C%E3%82%93%E3%81%8C%E3%83%95%E3%82%A7%E3%82%B9%E3%82%BF_(%E8%88%9E%E9%B6%B4)',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11643379','郷ノ浦祇園山笠',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'summer',NULL,'https://ja.wikipedia.org/wiki/%E9%83%B7%E3%83%8E%E6%B5%A6%E7%A5%87%E5%9C%92%E5%B1%B1%E7%AC%A0',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11647764','金砂神社磯出大祭礼',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%87%91%E7%A0%82%E7%A5%9E%E7%A4%BE%E7%A3%AF%E5%87%BA%E5%A4%A7%E7%A5%AD%E7%A4%BC',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11652555','長崎帆船まつり',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%95%B7%E5%B4%8E%E5%B8%86%E8%88%B9%E3%81%BE%E3%81%A4%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11665956','飛鳥光の回廊',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%A3%9B%E9%B3%A5%E5%85%89%E3%81%AE%E5%9B%9E%E5%BB%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11670487','高松秋のまつり・仏生山大名行列',NULL,NULL,NULL,NULL,NULL,NULL,'香川県','shikoku',NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E6%9D%BE%E7%A7%8B%E3%81%AE%E3%81%BE%E3%81%A4%E3%82%8A%E3%83%BB%E4%BB%8F%E7%94%9F%E5%B1%B1%E5%A4%A7%E5%90%8D%E8%A1%8C%E5%88%97',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11666571','飯田町燈籠山祭り','Iida-machi Toroyama Festival','石川県珠洲市で行われる山車祭り',NULL,'Q112874501','春日神社','Kasuga Shrine','長野県','chubu',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/%E9%A3%AF%E7%94%B0%E7%94%BA%E7%87%88%E7%B1%A0%E5%B1%B1%E7%A5%AD%E3%82%8A%EF%BC%88%E3%81%84%E3%81%84%E3%81%A0%E3%81%BE%E3%81%A1%E3%81%A8%E3%82%8D%E3%82%84%E3%81%BE%E3%81%BE%E3%81%A4%E3%82%8A%EF%BC%89.jpg','https://ja.wikipedia.org/wiki/%E9%A3%AF%E7%94%B0%E7%94%BA%E7%87%88%E7%B1%A0%E5%B1%B1%E7%A5%AD%E3%82%8A',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11672606','高砂山願念坊祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'https://ja.wikipedia.org/wiki/%E9%AB%98%E7%A0%82%E5%B1%B1%E9%A1%98%E5%BF%B5%E5%9D%8A%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11675706','鵜島の曳山祭り',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'spring',NULL,'https://ja.wikipedia.org/wiki/%E9%B5%9C%E5%B3%B6%E3%81%AE%E6%9B%B3%E5%B1%B1%E7%A5%AD%E3%82%8A',NULL,35,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11660875','霧島国際音楽祭','Kirishima International Music Festival','日本の鹿児島県の霧島高原で開催されているクラシック音楽祭','music festival in Kagoshima, Japan','Q858352','霧島市','Kirishima','鹿児島県','kyushu',NULL,NULL,1980,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Miyama%20Conseru.jpg','https://ja.wikipedia.org/wiki/%E9%9C%A7%E5%B3%B6%E5%9B%BD%E9%9A%9B%E9%9F%B3%E6%A5%BD%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11661985','青梅大祭','Ōme Grand Festival','東京都青梅市で行われる祭り',NULL,'Q237683','青梅市','Ome','東京都','kanto',NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Ibayashi.jpg','https://ja.wikipedia.org/wiki/%E9%9D%92%E6%A2%85%E5%A4%A7%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11638353','迎え火','mukaebi','客人や神霊をむかえるためにたく火','part of the Bon Festival',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'http://commons.wikimedia.org/wiki/Special:FilePath/Mukaebi%2020120731.jpg','https://ja.wikipedia.org/wiki/%E8%BF%8E%E3%81%88%E7%81%AB',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
INSERT INTO "festivals" VALUES('Q11635899','赤穂義士祭','Akō Gishi Festival','兵庫県赤穂市で毎年赤穂義士たちが討ち入りを果たした12月14日に行われる祭り',NULL,NULL,NULL,NULL,'兵庫県','kinki',NULL,NULL,1903,NULL,'winter','http://commons.wikimedia.org/wiki/Special:FilePath/Ako%20Gishisai%20De09%2013.jpg','https://ja.wikipedia.org/wiki/%E8%B5%A4%E7%A9%82%E7%BE%A9%E5%A3%AB%E7%A5%AD',NULL,85,'pending',NULL,NULL,NULL,NULL,NULL,'2026-05-20T15:07:52.470287+00:00','wikidata');
CREATE TABLE fetch_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fetched_at TEXT NOT NULL,
            raw_file TEXT NOT NULL,
            unique_qids INTEGER NOT NULL,
            inserted INTEGER NOT NULL,
            updated INTEGER NOT NULL
        );
INSERT INTO "fetch_history" VALUES(1,'2026-05-20T15:04:46.091425+00:00','festivals_wikidata_20260520_093931.json',1256,1256,0);
INSERT INTO "fetch_history" VALUES(2,'2026-05-20T15:07:52.470287+00:00','festivals_wikidata_20260520_093931.json',1256,0,1256);
CREATE INDEX idx_prefecture ON festivals(prefecture);
CREATE INDEX idx_region ON festivals(region);
CREATE INDEX idx_season ON festivals(season);
CREATE INDEX idx_status ON festivals(status);
CREATE INDEX idx_priority ON festivals(priority_score DESC);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('fetch_history',2);
COMMIT;
