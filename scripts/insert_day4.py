#!/usr/bin/env python3
"""Insert festivals #41-50 (Phase 1c day 4):
Q4701224 竿燈 / Q48743940 国府宮はだか祭り / Q48758315 羽浦神社 /
Q493695 唐津くんち / Q6663968 足立の花火 / Q6663970 高岡御車山祭 /
Q72727981 長幡部神社 / Q862407 青森ねぶた /
Q888184 日前神宮・國懸神宮 / Q903645 国際花と緑の博覧会"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q4701224",
        "slug_ja": "kanto-matsuri-akita",
        "slug_en": "kanto-matsuri-akita",
        "manual_content_ja": """## 概要

竿燈まつり（かんとうまつり）は、秋田県秋田市で毎年8月3日から6日までの4日間にわたって行われる、五穀豊穣・無病息災・厄除けを祈念する伝統行事である。重さ50キログラム、長さ12メートルにも及ぶ「竿燈（かんとう）」と呼ばれる竹竿に46個もの提灯を吊るし、それを腰や額、肩、手のひらで支える妙技を披露する。青森ねぶた・仙台七夕と並んで「東北三大祭り」に数えられ、1980年（昭和55年）に国の重要無形民俗文化財に指定されている。

## 歴史

竿燈の起源は宝暦年間（1751-1764年）以前に遡るとされ、当時の秋田藩で行われていた「ねぶり流し」という眠気払いの行事と、五穀豊穣を祈願する七夕の風習が融合して成立したと伝わる。藩政期には町人文化として発展し、寛政元年（1789年）の津村淙庵『雪の降る道』に竿燈らしき行事の記述が残されている。明治・大正期には一時衰退したものの、昭和初期に地元有志により復興、戦後は秋田市の観光行事として大規模化し、現在では国内外から多数の観光客を迎える夏祭りに発展した。

## 見どころ

最大の見どころは毎晩18:50頃から始まる「夜本番」で、約280本もの竿燈が約2万個の提灯の灯りを揺らしながら大通りを埋め尽くす光景は圧巻。差し手（さして）と呼ばれる演者が「ドッコイショ、ドッコイショ」の掛け声と共に、流し・平手・額・肩・腰の5つの技を披露する。提灯の灯りが稲穂のように揺れる姿は、五穀豊穣を象徴する原初の祈りの形を伝える。日中には「妙技会」が開催され、技の優劣を競う競技形式の演技も楽しめる。

## 開催情報・アクセス

会場は秋田県秋田市の竿燈大通り（山王十字路から二丁目橋まで約800メートル）。JR秋田駅から徒歩約15分。観覧席は有料（前売り2,700-3,500円）、自由観覧は無料。4日間で約130万人の観光客が訪れる。

## 周辺観光

秋田市内には千秋公園（久保田城跡）、赤れんが郷土館、秋田県立美術館、ねぶり流し館（竿燈の常設展示）など歴史・文化観光資源が集中する。郊外には男鹿半島・なまはげ館、田沢湖、角館武家屋敷、乳頭温泉郷などの観光地が広がり、夏季は秋田名物・きりたんぽ、稲庭うどん、比内地鶏、地酒の蔵元巡りなど食文化も堪能できる。""",
        "manual_content_en": """## Overview

The Kantō Festival (Kantō Matsuri) is a traditional Japanese festival held annually from August 3 to 6 in Akita City, Akita Prefecture, dedicated to prayers for bountiful harvests, protection from illness, and the warding off of evil. Performers display extraordinary feats of balance using "kantō"—long bamboo poles up to 12 meters in length and 50 kilograms in weight, hung with as many as 46 paper lanterns—supporting them on their hips, foreheads, shoulders, and palms. Together with the Aomori Nebuta and Sendai Tanabata, it is counted among the "Three Great Festivals of the Tōhoku Region" and was designated as a National Important Intangible Folk Cultural Property in 1980 (Shōwa 55).

## History

The origins of the Kantō Festival are traced back to before the Hōreki era (1751-1764), when a drowsiness-dispelling ritual called "Neburi-nagashi" performed in the Akita Domain merged with the Tanabata custom of praying for bountiful harvests. During the domain administration period, the festival developed as a townspeople's culture, with descriptions of what appears to be the kantō ritual recorded in Tsumura Sōan's 1789 (Kansei 1) work "Yuki no Furu Michi" (The Snow-Falling Road). Although the festival declined temporarily during the Meiji and Taishō periods, it was revived in the early Shōwa era through the efforts of local volunteers. After World War II, it grew into a large-scale tourism event sponsored by Akita City, developing into the major summer festival it is today, welcoming visitors from around the world.

## Highlights

The greatest attraction is the "Yoru Honban" (Evening Performance) beginning around 18:50 each night, when approximately 280 kantō poles fill the main avenue, their roughly 20,000 lanterns swaying with light in an overwhelming spectacle. Performers called "sashite" demonstrate five techniques—Nagashi (flow), Hirate (palm), Hitai (forehead), Kata (shoulder), and Koshi (hip)—accompanied by chants of "Dokkoisho, Dokkoisho." The sight of the lantern lights swaying like ripe rice ears conveys the primitive form of prayer for bountiful harvests. During the day, "Myōgi-kai" (skill competitions) are held, allowing visitors to enjoy competitive performances where techniques are judged for excellence.

## Event Details and Access

The venue is Kantō Ōdōri Avenue in Akita City, Akita Prefecture, extending approximately 800 meters from Sannō Crossing to Nichōme Bridge. Access is approximately 15 minutes on foot from Akita Station on the JR lines. Reserved seating is available for purchase (advance tickets 2,700-3,500 yen), while general viewing along the street is free. The four-day festival attracts approximately 1.3 million visitors.

## Surrounding Attractions

Akita City offers a concentration of historical and cultural attractions including Senshū Park (the ruins of Kubota Castle), the Akarenga Museum of Local History, the Akita Museum of Art, and the Neburi-nagashi Hall (a permanent exhibition of kantō poles). The surrounding area features the Oga Peninsula and Namahage Museum, Lake Tazawa, the Kakunodate samurai district, and the Nyūtō Hot Spring village. Summer travelers can also enjoy Akita's culinary specialties including kiritanpo, Inaniwa udon noodles, Hinai-jidori chicken, and tours of local sake breweries, making it a richly rewarding destination for both cultural and gastronomic exploration."""
    },
    {
        "qid": "Q48743940",
        "slug_ja": "konomiya-hadaka-matsuri",
        "slug_en": "konomiya-hadaka-matsuri",
        "manual_content_ja": """## 概要

国府宮はだか祭り（こうのみやはだかまつり）は、愛知県稲沢市の尾張大国霊神社（おわりおおくにたまじんじゃ・通称「国府宮」）で毎年旧暦1月13日（現行暦の2月上旬から中旬）に開催される、約1,250年の歴史を持つ厄除け神事である。正式名称は「儺追神事（なおいしんじ）」で、神男（しんおとこ）と呼ばれる選ばれた男性に厄を移して払い清めるため、数千人の裸の男たちが「儺追笹」を奉納する勇壮な伝統祭礼である。

## 歴史

国府宮はだか祭りの起源は奈良時代の神護景雲元年（767年）に遡るとされ、称徳天皇の勅命により全国の国分寺で厄除けの儺追神事が行われたことに始まる。尾張国では国府宮が国府の鎮守として神事を引き継ぎ、平安期以降は地域の伝統行事として継承された。江戸期には尾張藩の支援のもと現在のような大規模な「裸祭り」の形態が確立し、数千人の男衆が褌姿で集結する独特の様式が定着した。明治期以降も地域住民の信仰と熱意により継承され、1991年に愛知県の無形民俗文化財に指定された。

## 見どころ

祭りの中心は午後3時頃から始まる「儺追神事」で、約9,000人もの裸の男たち（褌のみの姿）が尾張大国霊神社の参道や境内を埋め尽くす。神男に触れることで厄を移すことができるとされ、男衆は神男のもとへと殺到し、激しい揉み合いを繰り広げる。前日には「直会祭」、当日朝には「儺追笹奉納」、夜には「夜儺追神事」と神男の追放儀礼が行われ、3日間にわたって厳粛な神事と熱狂的な裸祭りが交錯する。冬の寒さの中、男たちの白い息と熱気が立ち上る光景は圧巻である。

## 開催情報・アクセス

会場は尾張大国霊神社（愛知県稲沢市国府宮1-1-1）。名鉄名古屋本線国府宮駅から徒歩約3分。観覧は無料。日程は旧暦1月13日（毎年2月上旬から中旬の特定日）。参加には事前申込みと褌・地下足袋着用が必要。

## 周辺観光

稲沢市内には国府宮神社のほか、性海寺（あじさい寺として有名）、矢合観音、稲沢サボテンの里など地域観光資源が点在する。名古屋市中心部からも電車で約15分の好アクセスで、名古屋城・熱田神宮・徳川美術館・有松絞り、犬山城（国宝）など尾張地方の歴史観光と組み合わせた周遊が可能。""",
        "manual_content_en": """## Overview

The Kōnomiya Naked Festival (Kōnomiya Hadaka Matsuri) is a 1,250-year-old purification ritual held annually on the 13th day of the first lunar month (early to mid-February in the modern calendar) at Owari Ōkunitama Shrine (commonly known as Kōnomiya) in Inazawa City, Aichi Prefecture. Officially named the "Naoi Shinji" (Evil-Chasing Ritual), the festival features thousands of nearly-naked men offering "Naoi-zasa" bamboo branches to transfer their misfortunes onto a specially chosen "Shin-otoko" (Sacred Man), creating one of Japan's most dynamic and ancient traditional festivals.

## History

The origins of the Kōnomiya Naked Festival trace back to 767 (Jingo-keiun 1) during the Nara period, when Empress Shōtoku issued an imperial edict ordering Naoi purification rituals at all provincial temples across the country. In Owari Province, Kōnomiya inherited these rituals as the guardian shrine of the provincial government, and from the Heian period onward, the festival was preserved as a traditional regional event. During the Edo period, with the support of the Owari Domain, the festival took on its current large-scale "naked festival" form, in which thousands of men gather wearing only loincloths. The festival continued through the Meiji era thanks to the faith and dedication of local residents, and was designated as an Intangible Folk Cultural Property of Aichi Prefecture in 1991.

## Highlights

The festival's central event is the "Naoi Shinji" beginning around 3 p.m., when approximately 9,000 nearly-naked men (wearing only loincloths) fill the approach and precincts of Owari Ōkunitama Shrine. By touching the Shin-otoko (Sacred Man), participants believe they can transfer their misfortunes onto him, and the men surge toward the Shin-otoko in fierce jostling. The day before features a "Naorai-sai" (Communion Festival), the festival morning includes the "Naoi-zasa Hōnō" (Bamboo Offering), and the night brings the "Yoru-Naoi Shinji" expulsion ritual for the Shin-otoko, with three days of solemn rites and fervent naked festival intertwined. The sight of white breath and heat rising from the men amid winter cold creates a truly overwhelming spectacle.

## Event Details and Access

The venue is Owari Ōkunitama Shrine (1-1-1 Kōnomiya, Inazawa City, Aichi Prefecture). Access is approximately 3 minutes on foot from Kōnomiya Station on the Meitetsu Nagoya Main Line. Viewing is free of charge. The date corresponds to the 13th day of the first lunar month (a specific date from early to mid-February each year). Participation requires advance application and the wearing of a loincloth and jika-tabi traditional footwear.

## Surrounding Attractions

Inazawa City features Kōnomiya Shrine alongside other local attractions including Shōkai-ji Temple (famous as the "Hydrangea Temple"), Yagose Kannon, and the Inazawa Cactus Village. Conveniently located approximately 15 minutes by train from central Nagoya City, the area allows for combined tours with major Owari region historical attractions including Nagoya Castle, Atsuta Shrine, the Tokugawa Art Museum, the Arimatsu Shibori dyeing district, and Inuyama Castle (a National Treasure), making it an ideal destination for exploring the rich heritage of the Owari region."""
    },
    {
        "qid": "Q48758315",
        "slug_ja": "hanoura-jinja",
        "slug_en": "hanoura-jinja",
        "manual_content_ja": """## 概要

羽浦神社（はのうらじんじゃ）は、徳島県阿南市羽ノ浦町中庄（はのうらちょうなかしょう）に鎮座する神社で、誉田別命（ほんだわけのみこと・応神天皇）を主祭神として祀る古社である。羽ノ浦町の総鎮守として地域住民に篤く崇敬され、阿波国南部の歴史と農耕文化を伝える郷社として継承されてきた。

## 歴史

羽浦神社の創建年代は不詳ながら、江戸時代以前から羽ノ浦地域の鎮守として機能していたことが地誌類から確認される。主祭神の誉田別命は第15代応神天皇であり、八幡神として全国で広く崇敬される神格である。武運・国家鎮護・農耕守護の神として、武家のみならず農民・町人にも親しまれた。阿波国（現徳島県）は古代から麻・藍・稲作で栄えた地域であり、羽浦神社も農耕儀礼の中心として地域の信仰生活を支えてきた。明治期の社格制度下では郷社に列せられ、近代以降も地域の核となる神社として継承されている。

## 見どころ

社殿は近世以降の建築様式を残し、地域の風土に調和した素朴で品格ある佇まいが特徴。境内には樹齢数百年とされる神木や、地域の郷土史を語る石碑、奉納された絵馬・狛犬などが点在し、阿波の農村信仰の素朴な雰囲気を伝える。例祭は秋季10月に執り行われ、地元氏子による神事・神輿渡御・奉納神楽が行われる。羽ノ浦町の伝統行事として地域住民に親しまれている。

## 開催情報・アクセス

JR牟岐線羽ノ浦駅から徒歩約15分または車で約5分。境内参拝は終日自由。秋季例祭は毎年10月の指定日に執り行われる。

## 周辺観光

阿南市は徳島県南部の中心都市で、四国八十八ヶ所霊場の22番札所・平等寺、23番札所・薬王寺（牟岐町）が近接し、お遍路の重要中継地点として知られる。橘湾の絶景、蒲生田岬（四国最東端）、太龍寺ロープウェイなど自然景観も豊か。徳島県内では阿波踊り（徳島市・8月開催）、大塚国際美術館（鳴門市）、祖谷渓・かずら橋（三好市）など、阿波文化を堪能できる観光地と組み合わせた周遊が可能。""",
        "manual_content_en": """## Overview

Hanoura Shrine (Hanoura Jinja) is a Shinto shrine located in Nakashō, Hanoura-chō, Anan City, Tokushima Prefecture, enshrining Hondawake no Mikoto (Emperor Ōjin) as its principal deity. As the chief tutelary shrine of Hanoura-chō, it has been deeply venerated by local residents and preserved as a regional shrine transmitting the history and agricultural culture of southern Awa Province.

## History

Although the founding date of Hanoura Shrine is unknown, regional historical records confirm that it functioned as the guardian shrine of the Hanoura area from before the Edo period. The principal deity Hondawake no Mikoto is the 15th Emperor Ōjin, widely venerated throughout Japan as the Hachiman deity. Beloved by warriors, farmers, and townspeople alike, this deity was revered as a god of martial fortune, national protection, and agricultural guardianship. Awa Province (present-day Tokushima Prefecture) has been known since ancient times as a region prospering through hemp, indigo, and rice cultivation, and Hanoura Shrine served as a center of agricultural rituals supporting the religious life of the local community. Under the Meiji-era shrine ranking system, it was designated as a Gōsha (district shrine), and from the modern era onward, it has continued as the central shrine of the region.

## Highlights

The shrine buildings preserve architectural styles from the early-modern period onward, featuring a humble yet dignified appearance harmonizing with the local landscape. Within the precincts stand sacred trees estimated to be several centuries old, stone monuments narrating local regional history, and dedicated wooden votive plaques (ema) and stone guardian dog statues (komainu), conveying the simple atmosphere of rural folk faith in Awa Province. The annual main festival is held in October, featuring sacred rituals, portable shrine (mikoshi) processions, and dedicatory kagura sacred dance performances by local parishioners. The festival has been cherished as a traditional event of Hanoura-chō by local residents.

## Event Details and Access

The shrine is accessible approximately 15 minutes on foot or 5 minutes by car from Hanoura Station on the JR Mugi Line. The precincts are open for worship throughout the day. The autumn main festival is held on a designated date in October each year.

## Surrounding Attractions

Anan City is the central urban hub of southern Tokushima Prefecture, with Byōdō-ji Temple (the 22nd temple on the Shikoku Pilgrimage) and the nearby Yakuō-ji Temple (the 23rd temple, in Mugi Town) making it a major waypoint along the famous Shikoku Henro pilgrimage route. The area also features rich natural scenery including the spectacular views of Tachibana Bay, Kamoda Misaki (the easternmost point of Shikoku), and the Tairyū-ji Ropeway. Within Tokushima Prefecture, combined sightseeing tours are possible with attractions allowing visitors to experience Awa culture, including the Awa Odori dance festival in Tokushima City (August), the Otsuka Museum of Art in Naruto City, and the Iya Valley with its famous Kazura-bashi vine bridges in Miyoshi City."""
    },
    {
        "qid": "Q493695",
        "slug_ja": "karatsu-kunchi",
        "slug_en": "karatsu-kunchi",
        "manual_content_ja": """## 概要

唐津くんち（からつくんち）は、佐賀県唐津市の唐津神社の秋季例大祭で、毎年11月2日から4日にかけて開催される、約400年の歴史を持つ伝統祭礼である。14台の豪華絢爛な「曳山（ひきやま）」が城下町を巡行する勇壮な姿で全国的に知られ、1980年（昭和55年）に国の重要無形民俗文化財に指定、2016年にはユネスコ無形文化遺産「山・鉾・屋台行事」の構成要素として登録された。

## 歴史

唐津くんちの起源は、寛文年間（1661-1673年）に唐津神社の秋季例大祭として始まったと伝わるが、本格的な曳山の登場は文政2年（1819年）の「赤獅子」が最古とされる。江戸後期から明治初期にかけて、唐津の町人たちが各町ごとに豪華な曳山を新調し、現在の14台体制が明治9年（1876年）の「七宝丸」をもって完成した。曳山は「武者・獅子・鯛・龍・兜・鳳凰・宝船」など多彩な題材で、漆と金箔を多用した重さ2-3トンの大型山車である。第二次世界大戦中も中断せず継承され、戦後は唐津市を代表する観光行事として規模を拡大した。

## 見どころ

最大の見どころは11月3日の「お旅所神幸」で、14台の曳山が囃子の音色に乗って唐津神社から西の浜お旅所まで約2キロを巡行する。曳山は「ヤァサーヤァサー」「エンヤーエンヤー」の掛け声と共に、500人以上の曳き子により西の浜の砂浜に勢いよく曳き込まれ、車輪が砂にめり込む中を力強く進む光景は圧巻。夜には提灯に灯りが入り、漆塗りの曳山が幻想的に浮かび上がる。11月2日の宵山、4日の町廻りも華やか。

## 開催情報・アクセス

会場は唐津神社（佐賀県唐津市南城内3-13）および唐津市中心部の旧城下町一帯。JR唐津駅から徒歩約10分。観覧は無料。3日間で約50万人の観光客が訪れる。曳山展示場では年間を通して全14台の曳山を観覧可能。

## 周辺観光

唐津市内には唐津城、旧唐津銀行（辰野金吾設計）、虹の松原（日本三大松原）、鏡山展望台などの歴史・自然観光地が集中する。郊外には呼子の朝市（イカ料理で全国的に有名）、名護屋城跡（豊臣秀吉の朝鮮出兵拠点）、玄海国定公園など、肥前国北部の歴史と海の幸を堪能できる観光資源が広がる。佐賀県内では吉野ヶ里遺跡、有田焼の里・有田町と組み合わせた周遊も人気。""",
        "manual_content_en": """## Overview

Karatsu Kunchi is a traditional festival with approximately 400 years of history, held annually from November 2 to 4 as the autumn grand festival of Karatsu Shrine in Karatsu City, Saga Prefecture. Renowned nationwide for the spectacular sight of 14 magnificent "hikiyama" (pulled floats) parading through the castle town, the festival was designated as a National Important Intangible Folk Cultural Property in 1980 (Shōwa 55) and registered as a constituent element of the UNESCO Intangible Cultural Heritage "Yama, Hoko, Yatai Float Festivals" in 2016.

## History

The origins of Karatsu Kunchi are believed to date back to the Kanbun era (1661-1673) as the autumn grand festival of Karatsu Shrine, though the full-scale appearance of hikiyama floats began with the "Akajishi" (Red Lion) of 1819 (Bunsei 2), the oldest extant float. From the late Edo to early Meiji periods, the townspeople of Karatsu each commissioned magnificent hikiyama for their respective districts, completing the current 14-float lineup with the "Shippōmaru" in 1876 (Meiji 9). The floats feature diverse motifs including warriors, lions, sea bream, dragons, helmets, phoenixes, and treasure ships, and are large, ornate constructions weighing 2-3 tons, generously decorated with lacquer and gold leaf. The festival continued uninterrupted even during World War II, and after the war it expanded in scale to become the signature tourism event representing Karatsu City.

## Highlights

The festival's greatest highlight is the "Otabisho Shinkō" (Sacred Journey to the Shrine Outpost) on November 3, when all 14 hikiyama parade approximately 2 kilometers from Karatsu Shrine to the Nishi-no-Hama Otabisho. To the rhythms of festival music and accompanied by shouts of "Yāsā-Yāsā" and "Enya-Enya," more than 500 puller-children draw the floats vigorously onto the sandy beach of Nishi-no-Hama, where the wheels sink deep into the sand but are forced forward by sheer human strength—an overwhelming spectacle of communal effort. At night, lanterns are lit on the floats, causing the lacquered hikiyama to glow with magical beauty. The "Yoiyama" (Eve Festival) on November 2 and the "Machi-mawari" (Town Procession) on November 4 are also resplendent occasions.

## Event Details and Access

The venue is Karatsu Shrine (3-13 Minami-Jōnai, Karatsu City, Saga Prefecture) and the surrounding old castle town center. Access is approximately 10 minutes on foot from Karatsu Station on the JR lines. Viewing is free of charge. The three-day festival attracts approximately 500,000 visitors. The Hikiyama Exhibition Hall allows year-round viewing of all 14 hikiyama floats.

## Surrounding Attractions

Karatsu City features a concentration of historical and natural attractions including Karatsu Castle, the former Karatsu Bank building (designed by famed architect Tatsuno Kingo), Niji-no-Matsubara (the Rainbow Pine Grove, one of Japan's three great pine groves), and the Kagamiyama Observation Deck. The surrounding area offers Yobuko's famous morning market (renowned nationwide for squid cuisine), the Nagoya Castle ruins (Toyotomi Hideyoshi's base for the Korean campaigns), and the Genkai Quasi-National Park, providing rich resources for experiencing the history and seafood bounty of northern Hizen Province. Within Saga Prefecture, combined tours with the Yoshinogari archaeological site and the Arita porcelain village in Arita Town are also highly popular among visitors."""
    },
    {
        "qid": "Q6663968",
        "slug_ja": "adachi-no-hanabi",
        "slug_en": "adachi-no-hanabi",
        "manual_content_ja": """## 概要

足立の花火（あだちのはなび）は、東京都足立区の荒川河川敷で毎年7月下旬に開催される、東京都内で最も早い時期に行われる大規模花火大会のひとつである。約1万3,500発の花火が打ち上げられ、約60万人の観客を集める下町の夏の風物詩として親しまれている。

## 歴史

足立の花火は1924年（大正13年）、足立区西新井大師の千部会奉納花火として始まったとされ、約100年の歴史を持つ。第二次世界大戦中の中断と戦後復興を経て、1979年（昭和54年）に「足立の花火」として現在の形に再編され、足立区観光交流協会と足立区が主催する都内有数の花火大会として発展した。荒川河川敷という広大な打上げ会場を活かし、東京都心では他に類を見ないスケールと観覧の自由度で人気を集める。7月下旬という早い開催時期から、東京の夏祭りシーズンの幕開けを告げる花火大会としても知られる。

## 見どころ

約1時間で1万3,500発を打ち上げる凝縮されたプログラム構成が特徴で、スターマイン、特大スターマイン、メッセージ花火、フィナーレの大スターマインなど多彩な演出が次々と展開される。荒川河川敷の広い空に大輪の花火が低く大きく開く光景は迫力満点で、河川敷の芝生から無料で観覧できる解放感も魅力。夜空に花火が映える中、千住の町並みのシルエットが浮かび上がる景観は下町情緒たっぷり。

## 開催情報・アクセス

会場は東京都足立区千住・西新井・梅島周辺の荒川河川敷（千住側および小台側の両岸）。東武スカイツリーライン梅島駅・五反野駅、京成本線関屋駅、JR常磐線・東京メトロ千代田線北千住駅などから徒歩15-25分。観覧は無料（一部有料席あり）。例年7月下旬の特定の土曜日に開催。

## 周辺観光

足立区一帯は北千住の昭和レトロな商店街、西新井大師（厄除けで全国的に有名）、舎人公園、東京武道館などの観光資源が点在する。北千住駅周辺は近年若者にも人気の街となり、新旧の文化が交差する魅力的なエリア。荒川を挟んで葛飾区側には柴又帝釈天・寅さん記念館、墨田区側には東京スカイツリー・浅草寺など、東京下町観光の名所が近接する。""",
        "manual_content_en": """## Overview

Adachi no Hanabi (Adachi Fireworks Festival) is a large-scale fireworks display held annually in late July along the Arakawa Riverbed in Adachi Ward, Tokyo, ranking among the earliest major fireworks events of the Tokyo summer season. With approximately 13,500 fireworks launched and 600,000 spectators attending, it has become a cherished summer tradition of Tokyo's old downtown district.

## History

Adachi no Hanabi traces its origins to 1924 (Taishō 13) as a dedicatory fireworks display for the Senbu-e ceremony at Nishiarai Daishi Temple in Adachi Ward, giving it approximately 100 years of history. After interruption during World War II and postwar recovery, the festival was reorganized into its current form as "Adachi no Hanabi" in 1979 (Shōwa 54), developing as one of Tokyo's leading fireworks displays under the joint hosting of the Adachi City Tourism Exchange Association and the ward government. Taking advantage of the expansive launching venue along the Arakawa Riverbed, the festival attracts large crowds with a scale and freedom of viewing unmatched elsewhere in central Tokyo. Its early late-July timing has also earned it recognition as the fireworks display heralding the opening of Tokyo's summer festival season.

## Highlights

The festival's distinctive feature is its condensed program structure, launching 13,500 fireworks in approximately one hour through diverse productions including star mines, oversized star mines, message fireworks, and the grand finale star mine in rapid succession. The sight of large fireworks blooming low and broad across the wide skies above the Arakawa Riverbed delivers tremendous visual impact, and the open atmosphere of free viewing from the riverbed grass adds to its appeal. As the fireworks paint the night sky, the silhouette of the Senju townscape emerges below, creating a scene rich with downtown Tokyo's nostalgic atmosphere.

## Event Details and Access

The venue is the Arakawa Riverbed in the Senju, Nishiarai, and Umejima areas of Adachi Ward, Tokyo (both the Senju side and the Odai side). Access is 15-25 minutes on foot from Umejima Station and Gotanno Station on the Tobu Skytree Line, Sekiya Station on the Keisei Main Line, or Kita-Senju Station on the JR Jōban Line and Tokyo Metro Chiyoda Line. Viewing is free (with some reserved paid seating available). The festival is typically held on a specific Saturday in late July.

## Surrounding Attractions

The Adachi Ward area features tourist attractions including the Showa-retro shopping streets of Kita-Senju, Nishiarai Daishi Temple (nationally famous for its protection against evil), Toneri Park, and the Tokyo Budōkan martial arts hall. The Kita-Senju Station area has become a popular district among young people in recent years, offering a charming blend of old and new cultural elements. Across the Arakawa River, Katsushika Ward features Shibamata Taishakuten Temple and the Tora-san Museum, while Sumida Ward offers Tokyo Skytree and Sensōji Temple, making the area highly accessible to Tokyo's renowned downtown sightseeing destinations."""
    },
    {
        "qid": "Q6663970",
        "slug_ja": "takaoka-mikurumayama-matsuri",
        "slug_en": "takaoka-mikurumayama-matsuri",
        "manual_content_ja": """## 概要

高岡御車山祭（たかおかみくるまやままつり）は、富山県高岡市の高岡関野神社の春季例祭として毎年5月1日に開催される、約430年の歴史を持つ伝統祭礼である。7基の豪華絢爛な「御車山（みくるまやま）」が高岡市旧市街地を巡行する勇壮華麗な姿で知られ、1979年（昭和54年）に国の重要有形民俗文化財、1981年（昭和56年）に国の重要無形民俗文化財に指定、2016年にはユネスコ無形文化遺産「山・鉾・屋台行事」の構成要素として登録された日本屈指の山車祭である。

## 歴史

御車山祭の起源は天正16年（1588年）、豊臣秀吉が後陽成天皇を聚楽第に迎えた際に使用された御所車を、慶長14年（1609年）に加賀藩2代藩主・前田利長が高岡城築城の祝いとして高岡の町に下賜したことに始まる。利長は7つの町に分配し、各町が独自の意匠を凝らした御車山として発展させ、現在の7基の体制が確立した。江戸時代を通じて加賀藩の篤い庇護を受け、漆塗り・金工・木彫・染織など加賀文化の粋を集めた豪華な装飾が施された。明治期以降も町衆の手で維持・継承され、戦後は高岡市の代表的な観光行事として国内外に知られるようになった。

## 見どころ

最大の見どころは5月1日の御車山巡行で、7基の御車山が高岡関野神社を出発し、片原町・坂下町・小馬出町・通町・木舟町・御馬出町・二番町の各町を一日かけて巡行する。御車山は高さ約7.5メートル、重さ1-2トンの大型山車で、車輪は金具で飾られ、御所車形式の優雅な姿に「鉾留め（ほこどめ）」と呼ばれる立物が天高くそびえる。前夜の宵山では提灯に灯りが入り、漆と金箔の装飾が幻想的に浮かび上がる。御車山会館では7基の本物の御車山が常設展示されており、年間を通して間近で観賞できる。

## 開催情報・アクセス

会場は高岡関野神社（富山県高岡市末広町9-56）を中心とする高岡市旧市街地一帯。あいの風とやま鉄道高岡駅から徒歩約10分。観覧は無料。御車山会館（高岡市守山町42）は通年営業で大人450円。

## 周辺観光

高岡市は加賀藩2代藩主・前田利長によって築かれた城下町として、銅器・漆器（高岡漆器）・絹織物などの伝統工芸が今も息づく工芸の町である。瑞龍寺（国宝）、高岡大仏（日本三大仏）、高岡古城公園、金屋町（鋳物発祥の地・重伝建）など歴史観光地が集中する。富山県内では立山黒部アルペンルート、五箇山合掌造り集落（世界遺産）、富山湾・氷見の海の幸など、自然・文化観光と組み合わせた周遊が可能。""",
        "manual_content_en": """## Overview

The Takaoka Mikurumayama Festival is a traditional festival with approximately 430 years of history, held annually on May 1 as the spring grand festival of Takaoka Sekino Shrine in Takaoka City, Toyama Prefecture. Renowned for the spectacular procession of seven magnificent "Mikurumayama" (Imperial Carriage Floats) through the old city center, the festival was designated as a National Important Tangible Folk Cultural Property in 1979 (Shōwa 54), as a National Important Intangible Folk Cultural Property in 1981 (Shōwa 56), and registered as a constituent element of the UNESCO Intangible Cultural Heritage "Yama, Hoko, Yatai Float Festivals" in 2016, making it one of Japan's most prestigious float festivals.

## History

The origins of the Mikurumayama Festival trace back to 1588 (Tenshō 16), when Toyotomi Hideyoshi used imperial carriages to welcome Emperor Go-Yōzei to his Jurakudai residence in Kyoto. These carriages were later bestowed upon the town of Takaoka in 1609 (Keichō 14) by Maeda Toshinaga, the second lord of the Kaga Domain, to celebrate the completion of Takaoka Castle. Toshinaga distributed them among seven districts of the town, and each district developed them into uniquely designed Mikurumayama floats, establishing the current seven-float system. Throughout the Edo period, the festival received generous patronage from the Kaga Domain, and the floats were adorned with the finest examples of Kaga cultural artistry including lacquer work, metalwork, woodcarving, and textile dyeing. The festival continued to be maintained and transmitted by the townspeople through the Meiji era and beyond, and after World War II became known both domestically and internationally as a signature tourism event of Takaoka City.

## Highlights

The festival's greatest highlight is the Mikurumayama procession on May 1, when all seven floats depart from Takaoka Sekino Shrine and parade through the districts of Katahara-machi, Sakashita-machi, Komandashi-machi, Tōri-machi, Kibune-machi, Ouma-dashi-machi, and Nibanmachi over the course of a full day. The Mikurumayama are large floats approximately 7.5 meters tall and weighing 1-2 tons, with wheels decorated in metalwork in the elegant imperial carriage style, surmounted by towering "Hoko-dome" (Halberd Caps) reaching high into the sky. During the previous night's "Yoiyama" (Eve Festival), lanterns are lit on the floats, causing the lacquer and gold leaf decorations to glow with magical beauty. The Mikurumayama Kaikan exhibition hall displays all seven authentic floats year-round, allowing visitors to view them up close throughout the year.

## Event Details and Access

The venue is Takaoka Sekino Shrine (9-56 Suehiro-machi, Takaoka City, Toyama Prefecture) and the surrounding old city center. Access is approximately 10 minutes on foot from Takaoka Station on the Ainokaze Toyama Railway. Viewing is free of charge. The Mikurumayama Kaikan (42 Moriyama-machi, Takaoka City) operates year-round with adult admission of 450 yen.

## Surrounding Attractions

Takaoka City, built as a castle town by Maeda Toshinaga, the second lord of the Kaga Domain, remains a town of living craft tradition where copperware, lacquerware (Takaoka Lacquerware), and silk textiles continue to thrive. Major historical attractions concentrated in the area include Zuiryū-ji Temple (a National Treasure), the Takaoka Daibutsu (one of Japan's three great Buddha statues), Takaoka Kojō Park, and Kanaya-machi (the birthplace of metal casting, designated as an Important Preservation District). Within Toyama Prefecture, combined sightseeing tours are possible with attractions including the Tateyama Kurobe Alpine Route, the Gokayama Gasshō-zukuri village (a UNESCO World Heritage Site), and the seafood bounty of Toyama Bay and Himi."""
    },
    {
        "qid": "Q72727981",
        "slug_ja": "nagahatabe-jinja-kamisato",
        "slug_en": "nagahatabe-jinja-kamisato",
        "manual_content_ja": """## 概要

長幡部神社（ながはたべじんじゃ）は、埼玉県児玉郡上里町（かみさとまち）に鎮座する古社で、長幡部連の祖神を祀る式内社級の格式を持つ神社である。律令期に朝廷の機織りを司った渡来系豪族・長幡部連と深い関わりを持ち、上里町の総鎮守として地域住民に篤く崇敬されてきた。

## 歴史

長幡部神社の創建年代は不詳ながら、『延喜式神名帳』（927年）に式内社として記載される武蔵国賀美郡（現・児玉郡）の古社である。長幡部連は古代の機織り技術を伝えた渡来系氏族で、朝廷に絹織物を貢納する役割を担っていた。神社の鎮座地である上里町一帯は、古代武蔵国北部の織物文化の中心地として栄え、長幡部連の祖神を祀ることで地域の繁栄と織物産業の隆盛を祈願してきた。中世以降は地域の鎮守として継承され、明治期の社格制度では郷社に列せられた。武蔵国の式内社の一座として、関東地方の古代史を語る重要な神社の一つである。

## 見どころ

社殿は近世以降の建築様式を残し、深い杜に囲まれた境内は古代の聖域の名残を感じさせる清浄な雰囲気をたたえる。境内には樹齢数百年の神木、地域の郷土史を語る石碑、長幡部連ゆかりの織物文化を象徴する文物が点在する。例祭は秋季10月で、地元氏子による神事と神楽奉納が行われ、武蔵国北部の古代信仰の名残を今に伝える。境内には織物産業の発展を祈願した絵馬・お守りなどが奉納されている。

## 開催情報・アクセス

JR高崎線神保原（じんぼはら）駅または上里町コミュニティバスで約10分。境内参拝は終日自由。秋季例祭は毎年10月に執り行われる。

## 周辺観光

上里町は埼玉県北西部に位置し、群馬県との県境に近い農業と歴史の町である。近隣には日本三大稲荷の一つ・桶川稲荷神社、本庄市の旧本庄商業銀行煉瓦倉庫、深谷市の渋沢栄一記念館、群馬県側の高崎観音山、富岡製糸場（世界遺産・近代の絹織物産業遺産）など、関東北部の歴史・文化遺産が集中する。長幡部連の織物伝統と、明治近代の富岡製糸場という時代を超えた絹文化のつながりを巡る旅も可能。""",
        "manual_content_en": """## Overview

Nagahatabe Shrine (Nagahatabe Jinja) is an ancient shrine located in Kamisato Town, Kodama District, Saitama Prefecture, possessing the dignity of a Shikinaisha (shrine listed in the 10th-century Engishiki register) and enshrining the ancestral deity of the Nagahatabe no Muraji clan. Maintaining deep connections with the immigrant clan responsible for imperial weaving during the Ritsuryō period, it has been deeply venerated by local residents as the chief tutelary shrine of Kamisato Town.

## History

Although the founding date of Nagahatabe Shrine is unknown, it is an ancient shrine of the former Kami District of Musashi Province (present-day Kodama District), recorded as a Shikinaisha in the Engishiki Jinmyōchō (Register of Deities) compiled in 927. The Nagahatabe no Muraji were an immigrant clan that transmitted ancient weaving technology and served the imperial court by providing silk textile tribute. The Kamisato Town area where the shrine is located flourished as a center of textile culture in northern Musashi Province during ancient times, and prayers were offered at the shrine through veneration of the Nagahatabe ancestral deity for the prosperity of the region and the flourishing of the textile industry. The shrine continued as a regional guardian shrine from the medieval period onward and was ranked as a Gōsha (district shrine) under the Meiji-era shrine ranking system. As one of the Shikinaisha shrines of Musashi Province, it stands as an important shrine narrating the ancient history of the Kantō region.

## Highlights

The main shrine hall preserves architectural styles from the early-modern period onward, and the precincts enclosed by deep forest convey a pure atmosphere evoking the lingering presence of an ancient sacred site. Within the precincts stand sacred trees estimated to be several centuries old, stone monuments narrating local regional history, and cultural artifacts symbolizing the textile heritage connected to the Nagahatabe no Muraji clan. The annual main festival is held in October, featuring sacred rituals and dedicatory kagura sacred dance performances by local parishioners, transmitting to the present day the lingering traces of ancient faith from northern Musashi Province. Within the precincts are dedicated wooden votive plaques and amulets praying for the development of the textile industry.

## Event Details and Access

The shrine is accessible approximately 10 minutes from Jinbohara Station on the JR Takasaki Line or via the Kamisato Town Community Bus. The precincts are open for worship throughout the day. The autumn main festival is held in October each year.

## Surrounding Attractions

Kamisato Town is located in the northwestern part of Saitama Prefecture near the border with Gunma Prefecture, serving as a town of agriculture and history. Nearby attractions include Okegawa Inari Shrine (one of Japan's three great Inari shrines), the former Honjō Commercial Bank Brick Warehouse in Honjō City, the Shibusawa Eiichi Memorial Museum in Fukaya City, and on the Gunma Prefecture side, the Takasaki Kannon and the Tomioka Silk Mill (a UNESCO World Heritage Site preserving the modern silk industry heritage). A journey can be designed to explore the trans-temporal connections of silk culture, linking the textile tradition of the Nagahatabe no Muraji clan with the modern Meiji-era Tomioka Silk Mill."""
    },
    {
        "qid": "Q862407",
        "slug_ja": "aomori-nebuta",
        "slug_en": "aomori-nebuta",
        "manual_content_ja": """## 概要

青森ねぶた祭（あおもりねぶたまつり）は、青森県青森市で毎年8月2日から7日までの6日間にわたって開催される、日本を代表する夏の伝統祭礼である。「ねぶた」と呼ばれる高さ約5メートル、幅約9メートルの巨大な人形灯籠（運行台車含め重さ4トン）が市内を練り歩く勇壮華麗な姿で世界的に有名で、1980年（昭和55年）に国の重要無形民俗文化財に指定され、毎年約280万人の観光客が訪れる東北最大級の夏祭りである。

## 歴史

青森ねぶたの起源は奈良時代に遡るとされ、坂上田村麻呂が蝦夷征討の際に巨大な人形灯籠で敵を欺いたという伝承が有名だが、史実としては七夕の「眠り流し」と呼ばれる眠気払いの行事と灯籠流しの風習が融合して成立した民俗行事と考えられている。江戸時代後期から青森城下町の町人文化として発展し、明治・大正期を経て次第に大型化、人形の意匠も歌舞伎・神話・歴史上の英雄をモチーフとした豪華絢爛なものへと進化した。戦後は青森市の観光行事として大規模化し、ねぶた師（人形製作の職人）の名匠たちが代々技術を継承する一大伝統工芸祭礼となった。

## 見どころ

最大の見どころは8月2-6日の夜間運行で、20数台の大型ねぶたが「ラッセラー、ラッセラー」の掛け声と笛・太鼓の囃子に乗って市内中心部を巡行する。跳人（はねと）と呼ばれる踊り手が浴衣姿で飛び跳ねながら囃子に合わせて踊る姿は、観客との一体感を生む祭りの真髄。8月7日には昼間の「市内合同運行」と夜の「青森花火大会・ねぶた海上運行」が行われ、ねぶたを台船に乗せて青森湾に浮かべる幻想的な光景でフィナーレを迎える。ねぶた師の技と伝統工芸の粋を集めた巨大灯籠の造形美は、海外メディアからも高く評価されている。

## 開催情報・アクセス

会場は青森県青森市中心部の青森駅東口周辺から国道4号沿いの大通り。JR青森駅・新青森駅から徒歩圏内。観覧は無料（一部有料席あり）。期間中は青森ねぶた祭協賛会と青森市が主催。観覧時間は18:00-21:00頃が中心。

## 周辺観光

青森市内には「ねぶたの家ワ・ラッセ」（ねぶた常設展示館）、青森県立美術館（奈良美智作品で世界的に有名）、八甲田丸（青函連絡船メモリアルシップ）、三内丸山遺跡（縄文時代・世界遺産候補）など歴史・文化観光地が集中する。郊外には十和田湖・奥入瀬渓流、青函トンネル記念館、酸ヶ湯温泉、弘前城（東北唯一の現存天守）など、青森県の自然と歴史を堪能できる観光資源が豊富。夏はインバウンド観光の人気目的地でもある。""",
        "manual_content_en": """## Overview

The Aomori Nebuta Festival (Aomori Nebuta Matsuri) is one of Japan's most iconic summer traditional festivals, held annually from August 2 to 7 in Aomori City, Aomori Prefecture. World-famous for its spectacular procession of enormous illuminated paper lantern figures called "Nebuta"—approximately 5 meters tall, 9 meters wide, and weighing up to 4 tons including the carrying platform—parading through the city streets, the festival was designated as a National Important Intangible Folk Cultural Property in 1980 (Shōwa 55) and attracts approximately 2.8 million visitors annually, ranking among the largest summer festivals of the Tōhoku region.

## History

The origins of Aomori Nebuta are believed to trace back to the Nara period, with the famous legend that Sakanoue no Tamuramaro deceived enemies with giant illuminated figures during his campaigns against the Emishi people. As a matter of historical record, however, the festival is believed to have developed as a folk event combining the "Nemuri-nagashi" drowsiness-dispelling ritual of the Tanabata festival with the custom of floating lanterns. From the late Edo period onward, it developed as a townspeople's culture in the Aomori castle town, gradually growing in scale through the Meiji and Taishō eras, with figure designs evolving into magnificent and ornate representations of kabuki characters, mythological figures, and historical heroes. After World War II, it expanded into a major tourism event sponsored by Aomori City, becoming a great traditional craft festival where master "nebuta-shi" (figure-making artisans) transmit their techniques across generations.

## Highlights

The festival's greatest highlight is the evening procession from August 2-6, when more than 20 large nebuta floats parade through the city center accompanied by chants of "Rassera, Rassera" and the rhythms of flutes and drums. Dancers called "Haneto" (Jumpers) wearing yukata leap and dance in time with the music, embodying the festival's essence of unity between performers and spectators. On August 7, the festival features the daytime "Citywide Joint Procession" and the nighttime "Aomori Fireworks and Nebuta Maritime Procession," when nebuta floats are loaded onto barges and float across Aomori Bay in a magical finale. The artistic excellence of these enormous illuminated figures, embodying the height of the nebuta-shi craft and traditional artistry, has received high acclaim from international media.

## Event Details and Access

The venue is the central area of Aomori City, ranging from the area around the east exit of Aomori Station to the main avenue along National Route 4. Access is within walking distance of Aomori Station and Shin-Aomori Station on the JR lines. Viewing is free of charge (with some reserved paid seating available). The festival is hosted by the Aomori Nebuta Festival Sponsorship Association and Aomori City. Viewing hours center on 6:00 p.m. to 9:00 p.m.

## Surrounding Attractions

Aomori City features a concentration of historical and cultural attractions including the Nebuta no Ie Wa-Rasse (a permanent nebuta exhibition hall), the Aomori Museum of Art (world-famous for works by artist Yoshitomo Nara), the Hakkōda Maru (a memorial ship of the former Seikan Ferry), and the Sannai Maruyama Archaeological Site (a Jōmon-period UNESCO World Heritage candidate). The surrounding area offers Lake Towada and the Oirase Mountain Stream, the Seikan Tunnel Memorial Museum, Sukayu Hot Spring, and Hirosaki Castle (the only original castle keep in the Tōhoku region), providing rich tourism resources for experiencing the nature and history of Aomori Prefecture. Summer makes the area a particularly popular destination for international inbound tourism."""
    },
    {
        "qid": "Q888184",
        "slug_ja": "hinokuma-kunikakasu-jingu",
        "slug_en": "hinokuma-kunikakasu-jingu",
        "manual_content_ja": """## 概要

日前神宮・國懸神宮（ひのくまじんぐう・くにかかすじんぐう）は、和歌山県和歌山市秋月（あきづき）に鎮座する紀伊国一宮であり、皇室の祖神に縁深い格式の高い古社である。日前神宮には日前大神（ひのくまのおおかみ・天照大神の御神体である日像鏡を祀る）、國懸神宮には國懸大神（くにかかすのおおかみ・天照大神の御神体である日矛鏡を祀る）を主祭神として祀り、同一境内に二つの神宮が並び立つ独特の形態を持つ。『延喜式神名帳』では名神大社に列せられ、伊勢神宮に次ぐ「準勅祭社」の格式を持つ。

## 歴史

日前神宮・國懸神宮の創建は神武天皇東征の時代に遡るとされ、『日本書紀』の伝承によれば、天照大神の御神体として石凝姥命（いしこりどめのみこと）が作った鏡のうち、日像鏡が日前神宮に、日矛鏡が國懸神宮に祀られたとされる。両神宮は紀伊国造（きいのくにのみやつこ）家である紀氏が代々祭祀を司り、古代から朝廷の篤い崇敬を受けてきた。『延喜式神名帳』（927年）では名神大社、特に重要な「准伊勢神宮」格として位置付けられ、明治期の近代社格制度では官幣大社に列せられた。皇室祭祀との深い関わりを持つ紀伊国一宮として、関西地方有数の格式高い神社である。

## 見どころ

両神宮は同一の広大な境内に並んで鎮座し、伊勢神宮を彷彿とさせる神明造系の社殿建築が深い杜に映える。境内は約8万坪と広大で、楠の巨木が林立する社叢は和歌山県の天然記念物に指定されている。日前神宮と國懸神宮の二つの本殿が並んで建つ独特の景観は他に類を見ず、皇祖神信仰と日本古代の鏡信仰の中核を体感できる。境内には水盤舎、随神門、宝物殿などの建造物があり、紀伊国造家ゆかりの文物・古文書が伝えられている。例祭は4月26日（春季）と10月26日（秋季）で、雅楽奉納・神事が厳粛に執り行われる。

## 開催情報・アクセス

会場は日前神宮・國懸神宮（和歌山県和歌山市秋月365）。JR和歌山駅から徒歩約20分または車で約10分、和歌山電鐵貴志川線日前宮駅から徒歩約2分。境内参拝は早朝から夕方まで自由（拝観時間あり）。

## 周辺観光

和歌山市内には和歌山城（御三家・紀州徳川家の居城）、紀三井寺（西国三十三所第2番）、和歌浦・玉津島神社、雑賀崎、紀州東照宮など歴史観光地が集中する。和歌山県内では高野山（世界遺産・真言密教の聖地）、熊野古道（世界遺産）、那智の滝・熊野那智大社、白浜温泉、串本海岸など、紀伊半島の信仰・自然・温泉文化を堪能できる観光資源が豊富。日前神宮・國懸神宮は熊野詣の前後参拝としても古来重視されてきた。""",
        "manual_content_en": """## Overview

Hinokuma Jingū and Kunikakasu Jingū (Hinokuma Shrine and Kunikakasu Shrine) constitute the Ichinomiya (first-ranked shrine) of Kii Province, located in Akizuki, Wakayama City, Wakayama Prefecture, and stand as ancient shrines of the highest dignity with deep connections to the imperial ancestral deities. Hinokuma Jingū enshrines Hinokuma no Ōkami (worshipping the Hi-no-kata-no-Kagami, one of the sacred mirror objects of Amaterasu), while Kunikakasu Jingū enshrines Kunikakasu no Ōkami (worshipping the Hihoko-no-Kagami, another sacred mirror object of Amaterasu). The two shrines stand together in a single precinct in a unique configuration. In the Engishiki Jinmyōchō, both were ranked as Myōjin Taisha (Major Shrines of Famous Deities) and held the prestigious "Quasi-Imperial Festival Shrine" status second only to the Ise Grand Shrine.

## History

The founding of Hinokuma Jingū and Kunikakasu Jingū traces back to the era of Emperor Jinmu's eastern campaign. According to the traditions of the Nihon Shoki, among the mirrors created by Ishikoridome no Mikoto as sacred objects of Amaterasu, the Hi-no-kata-no-Kagami was enshrined at Hinokuma Jingū and the Hihoko-no-Kagami at Kunikakasu Jingū. The Ki clan, the Kuni no Miyatsuko (provincial governors) of Kii Province, conducted the rituals at both shrines across generations, and the shrines received deep veneration from the imperial court since ancient times. In the Engishiki Jinmyōchō (927), both were ranked as Myōjin Taisha and especially positioned as "Quasi-Ise Grand Shrine" status, and under the modern shrine ranking system of the Meiji era, both were designated as Kanpei Taisha (Major Imperial Shrines). As the Ichinomiya of Kii Province with deep connections to imperial rituals, they stand among the most prestigious shrines of the Kansai region.

## Highlights

The two shrines stand side by side in an expansive precinct, with Shinmei-zukuri style shrine architecture evoking the Ise Grand Shrine standing beautifully amid deep forest. The precincts span approximately 80,000 tsubo (about 26 hectares), and the sacred grove with its towering camphor trees has been designated as a Natural Monument of Wakayama Prefecture. The unique landscape of two main shrine halls standing parallel is unmatched elsewhere, allowing visitors to experience the core of imperial ancestral faith and ancient Japanese mirror worship. The precincts feature a water purification hall (mizubasha), divine gate (zuishin-mon), and treasure hall, preserving artifacts and ancient documents connected to the Ki clan provincial governors. The annual main festivals are held on April 26 (spring) and October 26 (autumn), featuring solemn gagaku court music dedications and sacred rituals.

## Event Details and Access

The venue is Hinokuma Jingū and Kunikakasu Jingū (365 Akizuki, Wakayama City, Wakayama Prefecture). Access is approximately 20 minutes on foot or 10 minutes by car from Wakayama Station on the JR lines, or approximately 2 minutes on foot from Hinokuma-gū Station on the Wakayama Dentetsu Kishigawa Line. The precincts are open for worship from early morning to evening (with specific viewing hours).

## Surrounding Attractions

Wakayama City features a concentration of historical attractions including Wakayama Castle (the residence of the Kii Tokugawa family, one of the three Tokugawa branch families), Kimiidera Temple (the 2nd temple on the Saigoku Pilgrimage), Wakanoura and Tamatsushima Shrine, Saikazaki, and Kishū Tōshō-gū. Within Wakayama Prefecture, abundant tourism resources allow visitors to experience the faith, nature, and hot spring culture of the Kii Peninsula, including Mount Kōya (a UNESCO World Heritage Site and sacred place of Shingon Buddhism), the Kumano Kodō pilgrimage routes (a World Heritage Site), Nachi Falls and Kumano Nachi Taisha, Shirahama Hot Spring, and Kushimoto Coast. Hinokuma Jingū and Kunikakasu Jingū have historically been important pilgrimage stops both before and after the Kumano pilgrimage."""
    },
    {
        "qid": "Q903645",
        "slug_ja": "expo-90-osaka-flower",
        "slug_en": "expo-90-osaka-flower",
        "manual_content_ja": """## 概要

国際花と緑の博覧会（こくさいはなとみどりのはくらんかい・通称「花博」「EXPO'90」）は、1990年（平成2年）4月1日から9月30日までの183日間、大阪府大阪市鶴見区の花博記念公園鶴見緑地で開催された国際園芸博覧会である。国際園芸家協会（AIPH）認定A1クラス（最高位）・国際博覧会条約（BIE）特別博として開催され、日本で初めての本格的な国際園芸博覧会として2,312万人を動員した歴史的なイベントである。

## 歴史

国際花と緑の博覧会は、1990年に開催された大阪市制施行100周年記念事業として企画され、国際園芸家協会（AIPH）と国際博覧会事務局（BIE）の認定を受けた本格的な国際博覧会として開催された。テーマは「花と緑と人間生活のかかわりをとらえ、21世紀へ向けて潤いのある豊かな社会の創造を目指す」というもので、自然と人間の共生・都市環境の緑化推進・園芸文化の国際交流を目的とした。会場となった鶴見緑地は元々大阪市の都市公園で、博覧会終了後は「花博記念公園鶴見緑地」として再整備され、現在も大阪市民の憩いの場として親しまれている。本博覧会の成功は、その後の日本における園芸文化の普及と緑化運動の推進に大きく貢献し、2027年に横浜で開催予定の「GREEN×EXPO 2027」へと続く系譜の起点となった。

## 見どころ

博覧会は83の国・国際機関・212の国内外企業・55の都道府県市等の出展により構成され、世界各地の伝統園芸文化と最先端の緑化技術が一堂に集った。「いのちの塔」（高さ85メートルの記念建造物・後にダウンタウンズ命名）や「咲くやこの花館」（現在も植物園として運営中）など、博覧会のために建設された施設のいくつかは現在も鶴見緑地で見学可能。会期中は世界各国の園芸ショー、フラワーパレード、コンサート、文化交流イベントなどが連日開催され、約2,300万人の来場者を迎えた歴史的盛況となった。

## 開催情報・アクセス

会場は花博記念公園鶴見緑地（大阪府大阪市鶴見区緑地公園2-163）。大阪メトロ長堀鶴見緑地線鶴見緑地駅から徒歩約1分。現在は公園として常時開放され、「咲くやこの花館」（大人500円）など博覧会跡施設の見学が可能。博覧会自体は1990年に終了。

## 周辺観光

鶴見緑地公園のほか、大阪市内には大阪城・大阪城公園、難波・心斎橋・道頓堀の繁華街、新世界・通天閣、海遊館、ユニバーサル・スタジオ・ジャパンなど多彩な観光資源が集中する。郊外には万博記念公園（1970年大阪万博跡・太陽の塔）、京都・奈良の古都との周遊も可能。2025年には大阪・関西万博が夢洲で開催され、大阪は2027年横浜のGREEN×EXPOへとつながる「博覧会の都市」としての系譜を継承している。""",
        "manual_content_en": """## Overview

The International Garden and Greenery Exposition (Kokusai Hana to Midori no Hakurankai, commonly known as "Hanahaku" or "EXPO'90") was an international horticultural exposition held over 183 days from April 1 to September 30, 1990 (Heisei 2) at the Hanahaku Memorial Park Tsurumi-ryokuchi in Tsurumi Ward, Osaka City, Osaka Prefecture. Held as an AIPH-certified A1-class event (the highest rank) and as a Special Exposition under the BIE (Bureau International des Expositions) Treaty, it stands as a historic event drawing 23.12 million visitors as Japan's first full-scale international horticultural exposition.

## History

The International Garden and Greenery Exposition was planned as a commemorative project for the 100th anniversary of Osaka City's municipal incorporation in 1990, and was held as a full-scale international exposition certified by both the International Association of Horticultural Producers (AIPH) and the Bureau International des Expositions (BIE). Its theme was "Capturing the Relationships among Flowers, Greenery, and Human Life: Toward the Creation of a Rich and Fulfilling Society for the 21st Century," aimed at promoting harmony between nature and humanity, urban greening initiatives, and international exchange of horticultural cultures. The venue at Tsurumi-ryokuchi had originally been a municipal park of Osaka City, and after the exposition's conclusion was redeveloped as Hanahaku Memorial Park Tsurumi-ryokuchi, which continues today as a beloved recreational area for Osaka residents. The success of this exposition greatly contributed to the subsequent spread of horticultural culture and the promotion of greening movements in Japan, becoming the starting point of a lineage continuing to the GREEN×EXPO 2027 scheduled to be held in Yokohama.

## Highlights

The exposition was composed of exhibits by 83 countries and international organizations, 212 domestic and foreign corporations, and 55 prefectural and municipal governments, bringing together traditional horticultural cultures from around the world alongside cutting-edge greening technologies. Among the facilities built for the exposition, some remain accessible for viewing at Tsurumi-ryokuchi today, including the "Tower of Life" (an 85-meter-tall memorial structure later mentioned in popular culture) and "Sakuya Konohana-kan" (which continues to operate as a botanical garden). During the run, horticultural shows from countries around the world, flower parades, concerts, and cultural exchange events were held daily, welcoming approximately 23 million visitors in a historic success.

## Event Details and Access

The venue is Hanahaku Memorial Park Tsurumi-ryokuchi (2-163 Ryokuchi Kōen, Tsurumi Ward, Osaka City, Osaka Prefecture). Access is approximately 1 minute on foot from Tsurumi-ryokuchi Station on the Osaka Metro Nagahori Tsurumi-ryokuchi Line. The park is currently open year-round, and facilities remaining from the exposition such as Sakuya Konohana-kan (adult admission 500 yen) can be visited. The exposition itself concluded in 1990.

## Surrounding Attractions

In addition to Tsurumi-ryokuchi Park, central Osaka offers diverse tourism resources including Osaka Castle and Osaka Castle Park, the Namba, Shinsaibashi, and Dōtonbori commercial districts, Shinsekai and Tsutenkaku, Kaiyūkan Aquarium, and Universal Studios Japan. The suburbs feature Expo '70 Commemorative Park (the site of the 1970 Osaka World Expo with the iconic Tower of the Sun), and combined tours with the ancient capitals of Kyoto and Nara are possible. The 2025 Osaka-Kansai Expo will be held on Yumeshima, continuing Osaka's lineage as a "city of expositions" leading to the GREEN×EXPO 2027 in Yokohama."""
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
