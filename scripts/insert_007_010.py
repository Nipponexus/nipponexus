#!/usr/bin/env python3
"""Insert festivals #7-10: 下呂の田の神祭, 住吉の御田植, 送り盆まつり, 吉田の火祭"""
import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "nipponexus/data/sqlite/nipponexus.db"

ITEMS = [
    {
        "qid": "Q11360688",
        "slug_ja": "gero-no-ta-no-kami-matsuri",
        "slug_en": "gero-no-ta-no-kami-matsuri",
        "manual_content_ja": """## 概要

下呂の田の神祭（げろのたのかみまつり）は、岐阜県下呂市森地区の森水無八幡神社（もりみなしはちまんじんじゃ）で2月7日から14日にかけて執り行われる、五穀豊穣を祈願する古式神事である。「下呂の田の神祭」として1976年に国の重要無形民俗文化財に指定された、飛騨地方を代表する予祝（よしゅく）神事である。

## 歴史

起源は鎌倉時代から室町時代にさかのぼると伝えられ、約700年の歴史を持つ。古くは森水無八幡神社の祭礼として地域に根付き、田植えの所作を演じることで翌年の豊作を予祝してきた。江戸時代を通じて飛騨地方の代表的な神事として継承され、戦後の急速な近代化のなかでも地元の保存会が中心となって伝統を守り続けてきた。

## 見どころ

祭りの中心は、白塗りの化粧と独特の装束を身につけた「翁（おきな）」「巫女（みこ）」「鍬持ち（くわもち）」など、田植え作業を象徴する役柄の人々による所作である。彼らが拝殿で田起こしから田植え、収穫までの一連の農作業を厳かに演じ、神に翌年の豊作を願う。2月14日の本祭では夜を徹して神楽と田楽が奉納され、地域住民が篝火を囲んで参列する幻想的な光景が広がる。

## 開催情報

開催地は岐阜県下呂市森。最寄駅はJR高山本線「下呂駅」で、駅から徒歩約20分。開催期間は毎年2月7日から14日で、本祭は2月14日。冬季の山間部開催のため、防寒対策と積雪に備えた靴が必須である。観覧は無料で、神事中の撮影には一部制限があるため現地の指示に従う必要がある。

## 周辺の見どころ

下呂温泉は日本三名泉のひとつに数えられ、祭り観覧と合わせた湯治旅として人気が高い。下呂温泉合掌村では飛騨地方の合掌造り家屋を移築展示しており、農村文化を体感できる。冬季は周辺の濁河温泉や御嶽山麓のスキー場も楽しめる。""",
        "manual_content_en": """## Overview

Gero no Ta no Kami Matsuri (下呂の田の神祭) is an ancient Shinto ritual held from February 7 to 14 at Morimina shi Hachiman Shrine in the Mori district of Gero City, Gifu Prefecture. It prays for a bountiful harvest in the coming year and was designated an Important Intangible Folk Cultural Property of Japan in 1976. It is one of the most representative yoshuku (pre-celebratory) rituals in the Hida region.

## History

The festival is said to have originated in the Kamakura to Muromachi period, giving it a history of approximately 700 years. As a ritual of Morimina shi Hachiman Shrine, it has long been rooted in the local community, with participants performing the motions of rice planting to predict and pray for an abundant harvest. Despite the rapid modernization of postwar Japan, local preservation societies have continued to safeguard this tradition.

## Highlights

The central feature is a series of performances by villagers dressed as symbolic agricultural figures — the elder (okina), the shrine maiden (miko), and the hoe-bearer (kuwa-mochi) — wearing white facial makeup and distinctive costumes. On the hall of the shrine, they solemnly enact the full cycle of rice cultivation, from tilling the soil to planting and harvesting. The main festival on February 14 features overnight performances of kagura (sacred music) and dengaku (rice-field dance), with local residents gathered around bonfires in a fantastical scene.

## Event Information

The venue is Morimina shi Hachiman Shrine in Mori, Gero City, Gifu Prefecture. The nearest station is Gero Station on the JR Takayama Main Line, about a 20-minute walk away. The festival runs annually from February 7 to 14, with the main ritual on February 14. As it takes place in a mountainous region in winter, warm clothing and snow-ready footwear are essential. Admission is free, though photography may be restricted during certain rituals — visitors should follow on-site instructions.

## Nearby Attractions

Gero Onsen, ranked as one of Japan's three most famous hot springs, makes the festival ideal for combining with a hot-spring retreat. The Gero Onsen Gassho Village preserves relocated thatched-roof farmhouses from the Hida region, offering a glimpse of rural culture. Nearby Nigorigo Onsen and ski resorts at the foot of Mount Ontake are also accessible in winter."""
    },
    {
        "qid": "Q11381803",
        "slug_ja": "sumiyoshi-no-otaue-shinji",
        "slug_en": "sumiyoshi-no-otaue-shinji",
        "manual_content_ja": """## 概要

住吉の御田植神事（すみよしのおたうえしんじ）は、大阪市住吉区の住吉大社で毎年6月14日に執り行われる、五穀豊穣を祈願する伝統神事である。「住吉の御田植」として1979年に国の重要無形民俗文化財に指定されており、日本三大御田植神事のひとつに数えられる。

## 歴史

神功皇后が住吉大社を創建した際、長門国（現在の山口県）より植女（うえめ）を召して御田を植えさせたことが起源と伝えられ、約1800年の歴史を持つとされる。中世以降、住吉大社の重要な年中行事として継承され、室町時代の文献にもその様子が記されている。戦時中の中断を経て戦後復活し、現在まで途切れることなく執行されている。

## 見どころ

御田と呼ばれる神田で、稚児・植女・替植女（かえうえめ）・八乙女（やおとめ）など華やかな衣装を身につけた女性たちが、実際に早苗を植える所作を奉納する。田の中央では棚を組み、その上で住吉踊・田植踊・住吉武者行列・風流武者行事などが次々と披露され、田植えと芸能が一体となった荘厳かつ華麗な空間が現出する。植女の鮮やかな衣装と笠、武者行列の勇壮さの対比が見どころである。

## 開催情報

開催地は大阪市住吉区住吉2丁目の住吉大社御田。最寄駅は南海本線「住吉大社駅」徒歩約3分、または阪堺電車「住吉鳥居前駅」目の前。開催日は毎年6月14日、13時頃から約2時間。観覧は無料で、御田周囲の観覧スペースから自由に見学できるが、混雑するため早めの場所取りが望ましい。梅雨期のため雨具を携行すべきである。

## 周辺の見どころ

住吉大社は全国約2300社ある住吉神社の総本社で、海上交通・和歌・農耕の神として信仰を集める。境内の反橋（太鼓橋）は大社の象徴的存在で、神事の前後に参拝するとよい。周辺には大阪の下町情緒が残る商店街や、近隣に堺市の仁徳天皇陵古墳など世界遺産級の見どころも点在する。""",
        "manual_content_en": """## Overview

Sumiyoshi no Otaue Shinji (住吉の御田植神事) is a traditional Shinto ritual held annually on June 14 at Sumiyoshi Taisha Shrine in Sumiyoshi Ward, Osaka City. It prays for a bountiful rice harvest and was designated an Important Intangible Folk Cultural Property of Japan in 1979. It is counted among the three greatest rice-planting rituals in Japan.

## History

According to legend, the ritual originated when Empress Jingu, who founded Sumiyoshi Taisha, summoned planting maidens (uеme) from Nagato Province (present-day Yamaguchi Prefecture) to plant rice in the shrine's sacred fields. With a history of approximately 1,800 years, it has been continued as one of Sumiyoshi Taisha's most important annual events since the medieval period and is mentioned in Muromachi-era documents. After a wartime interruption, the ritual was revived and has been performed without interruption ever since.

## Highlights

In a sacred field called Onda, young girls (chigo), planting maidens (uеme), substitute maidens (kaeueme), and the eight virgin dancers (yaotome) — all dressed in elaborate costumes — perform the act of planting rice seedlings as an offering. A stage is constructed in the center of the field, where Sumiyoshi Odori dance, rice-planting dances, samurai processions, and furyu (elegant pageantry) performances unfold one after another, creating a solemn yet vibrant space where agriculture and performing arts converge. The contrast between the colorful costumes and broad hats of the planting maidens and the bold samurai processions is particularly striking.

## Event Information

The venue is the Onda sacred field at Sumiyoshi Taisha, 2-chome Sumiyoshi, Sumiyoshi Ward, Osaka City. The nearest stations are Sumiyoshi Taisha Station on the Nankai Main Line (about a 3-minute walk) or Sumiyoshi Toriimae Station on the Hankai Tramway (right in front of the shrine). The ritual is held annually on June 14, beginning around 1:00 PM and lasting about two hours. Admission is free, with viewing spaces around the field, but as it gets crowded, early arrival is recommended. Visitors should bring rain gear, as the ritual coincides with the rainy season.

## Nearby Attractions

Sumiyoshi Taisha is the head shrine of approximately 2,300 Sumiyoshi shrines across Japan and is revered as the deity of maritime safety, waka poetry, and agriculture. The Sorihashi (arched drum bridge) within the precincts is a symbol of the shrine and worth visiting before or after the ritual. The surrounding area retains the atmosphere of traditional Osaka downtown, and the nearby Mozu Tombs in Sakai City, including the Emperor Nintoku Tomb, are designated as UNESCO World Heritage sites."""
    },
    {
        "qid": "Q114045450",
        "slug_ja": "okuribon-matsuri",
        "slug_en": "okuribon-matsuri",
        "manual_content_ja": """## 概要

送り盆まつり（おくりぼんまつり）は、秋田県湯沢市で毎年8月16日から18日にかけて開催される、お盆の精霊送りを起源とする伝統的な夏祭りである。市内中心部の前郷二番丁通りを舞台に、巨大な「屋形舟」と呼ばれる山車が練り歩き、最終夜には舟同士が激しくぶつかり合う勇壮な「ぶつけ合い」が見どころとなる。

## 歴史

江戸時代中期、湯沢藩政下で町人文化が栄えるなかで、亡き祖先の霊を彼岸へ送り出す精霊送りの行事として始まったとされる。当初は小規模な灯籠流しの形態であったが、徐々に屋形舟が大型化し、町内ごとに独自の意匠を凝らした山車が制作されるようになった。明治以降は地域の若衆を中心に運営され、戦後の中断を経て1957年に本格復活、現在の形となった。

## 見どころ

祭りの主役は、長さ約5メートル、高さ約4メートルの「屋形舟」と呼ばれる豪華な山車である。極彩色の彫刻と提灯で飾られた舟が、太鼓と笛の囃子に合わせて町内を巡行する。最終日の18日夜、市役所前広場で行われる「ぶつけ合い」では、町内ごとの舟が正面から激しく衝突し、火花を散らすかのような迫力で観客を熱狂させる。屋形舟は祭り終了後に湯沢川で焼かれ、精霊送りの儀式が完結する。

## 開催情報

開催地は秋田県湯沢市前郷二番丁通り、ぶつけ合いは市役所前広場。最寄駅はJR奥羽本線「湯沢駅」徒歩約10分。開催期間は毎年8月16日から18日の3日間で、ぶつけ合いは18日夜19時頃から。観覧は無料で、ぶつけ合い会場は安全のため一定の距離を保った観覧エリアが設けられる。8月中旬の東北は夕方以降冷え込むこともあるため羽織りものを推奨する。

## 周辺の見どころ

湯沢市は秋田県南部に位置し、稲庭うどん発祥の地として知られる。市内には院内銀山跡や小安峡温泉など歴史・自然観光地が点在する。隣接する横手市の横手の雪まつり（かまくら）、大仙市の大曲花火大会と並んで、秋田県南部の三大祭りのひとつに数えられることもある。""",
        "manual_content_en": """## Overview

Okuribon Matsuri (送り盆まつり) is a traditional summer festival held annually from August 16 to 18 in Yuzawa City, Akita Prefecture. Originating as a ritual to send off ancestral spirits at the close of the Obon season, the festival features massive floats called yakata-bune (palace boats) parading through downtown Yuzawa, culminating on the final night in a fierce yakata-bune collision event called butsuke-ai.

## History

The festival is said to have begun in the mid-Edo period, when townspeople culture flourished under the rule of the Yuzawa domain, as a spirit-sending ritual to escort the souls of ancestors to the other shore. Originally a modest lantern-floating event, the floats gradually grew larger, with each neighborhood designing its own distinctive yakata-bune. From the Meiji era onward, the festival was managed by young men's associations of each district. After a wartime interruption, it was fully revived in 1957 and has continued in its present form ever since.

## Highlights

The main attraction is the yakata-bune, ornate floats approximately 5 meters long and 4 meters high. Decorated with vivid carvings and paper lanterns, the boats parade through the town to the rhythm of taiko drums and flutes. On the final night of August 18, at the plaza in front of City Hall, the yakata-bune from each district crash head-on into one another in a dramatic display called butsuke-ai, thrilling spectators with a fiery, sparks-flying intensity. After the festival, the boats are burned at the Yuzawa River, completing the spirit-sending ritual.

## Event Information

The venue is Maesato Nibancho-dori in Yuzawa City, Akita Prefecture, with the butsuke-ai held at the plaza in front of City Hall. The nearest station is Yuzawa Station on the JR Ou Main Line, about a 10-minute walk away. The festival runs annually from August 16 to 18, with the butsuke-ai beginning around 7:00 PM on August 18. Admission is free, and a safe viewing area is set up at a distance from the collision zone. Evenings in mid-August in the Tohoku region can be cool, so a light jacket is recommended.

## Nearby Attractions

Yuzawa City is located in southern Akita Prefecture and is known as the birthplace of Inaniwa udon, one of Japan's three great udon varieties. Local attractions include the Innai Silver Mine ruins and Oyasukyo Onsen, where hot-spring towns and historical sites are scattered through the area. Alongside the Yokote Snow Festival (Kamakura) in neighboring Yokote City and the Omagari Fireworks in Daisen City, it is sometimes counted as one of southern Akita's three great festivals."""
    },
    {
        "qid": "Q11413521",
        "slug_ja": "yoshida-no-himatsuri",
        "slug_en": "yoshida-no-himatsuri",
        "manual_content_ja": """## 概要

吉田の火祭（よしだのひまつり）は、山梨県富士吉田市の北口本宮冨士浅間神社および諏訪神社で毎年8月26日・27日に執り行われる、富士山の夏山閉山を告げる神事である。「吉田の火祭」として2012年に国の重要無形民俗文化財に指定され、日本三奇祭のひとつとされている。

## 歴史

起源は明確ではないが、富士山信仰と深く結びついた神事として平安時代末期から鎌倉時代にかけて成立したと考えられている。富士山は古来より霊峰として崇められ、夏季の限られた期間のみ登拝が許される神聖な山であった。閉山時期である8月末に大松明を焚き、夏山の終わりと安全な下山を感謝するとともに、火によって罪穢れを浄める意味が込められている。

## 見どころ

26日の「鎮火祭」では、夕刻に高さ約3メートル、直径約90センチの大松明70本以上が市内本町通りに立て並べられ、一斉に点火される。炎の柱が立ち上り、街全体が赤く染まる光景は圧巻である。各家の前にも井桁状の松明が組まれ、街路全体が火の道となる。27日の「すすき祭り」では、薄の玉串を持った氏子たちが諏訪神社の神輿を担いで還御する。富士山を背景にした火と山岳信仰の融合は、他にない神秘性を放つ。

## 開催情報

開催地は山梨県富士吉田市上吉田の北口本宮冨士浅間神社および諏訪神社、本町通り。最寄駅は富士急行線「富士山駅」徒歩約5分。開催日は毎年8月26日（鎮火祭）と27日（すすき祭り）。大松明の点火は26日18時30分頃から。観覧は無料だが、本町通りは夕刻から大変混雑するため早めの到着を推奨する。火を扱う祭りのため、燃えやすい服装は避け、安全な距離を保つこと。

## 周辺の見どころ

富士吉田市は富士山北麓に位置し、世界文化遺産「富士山」の構成資産である北口本宮冨士浅間神社は祭りの中心舞台である。富士急ハイランドや富士五湖（山中湖・河口湖など）も至近で、夏季の富士山観光と合わせて訪れる旅程が組みやすい。市内の吉田うどんは地元名物として知られ、祭り前後の食事におすすめである。""",
        "manual_content_en": """## Overview

Yoshida no Himatsuri (吉田の火祭) is a sacred fire festival held annually on August 26 and 27 at Kitaguchi Hongu Fuji Sengen Shrine and Suwa Shrine in Fujiyoshida City, Yamanashi Prefecture. It marks the closing of the summer climbing season on Mount Fuji and was designated an Important Intangible Folk Cultural Property of Japan in 2012. It is considered one of Japan's three most unusual festivals (Nihon san-kisai).

## History

While its precise origins are unclear, the festival is believed to have taken shape between the late Heian and Kamakura periods as a ritual deeply tied to Mount Fuji worship. Mount Fuji has been revered as a sacred mountain since ancient times, with pilgrim ascents permitted only during a brief summer window. Held at the end of August to mark the close of the climbing season, the festival lights enormous torches to express gratitude for safe descents and to purify impurities through the cleansing power of fire.

## Highlights

On August 26, during the Chinka-sai (fire-pacifying festival), over 70 massive torches — each about 3 meters tall and 90 cm in diameter — are erected along Honcho-dori in central Fujiyoshida and lit simultaneously in the evening. Pillars of flame rise into the sky, bathing the entire town in red — a spectacle of remarkable scale. Each household also constructs lattice-shaped torches in front of their homes, transforming the streets into a corridor of fire. On August 27, during the Susuki Matsuri (pampas grass festival), parishioners bearing pampas-grass tamagushi offerings carry the Suwa Shrine portable shrine back to its resting place. The fusion of fire and mountain worship, with Mount Fuji as a backdrop, projects a mystique found nowhere else.

## Event Information

The venues are Kitaguchi Hongu Fuji Sengen Shrine, Suwa Shrine, and Honcho-dori in Kamiyoshida, Fujiyoshida City, Yamanashi Prefecture. The nearest station is Fujisan Station on the Fujikyu Railway, about a 5-minute walk away. The festival is held annually on August 26 (Chinka-sai) and August 27 (Susuki Matsuri), with the lighting of the great torches beginning around 6:30 PM on August 26. Admission is free, but Honcho-dori becomes extremely crowded from early evening, so arriving early is recommended. As this is a fire festival, avoid flammable clothing and maintain a safe distance from the flames.

## Nearby Attractions

Fujiyoshida City sits at the northern foot of Mount Fuji, and Kitaguchi Hongu Fuji Sengen Shrine — the central stage of the festival — is a component asset of the UNESCO World Heritage Site "Fujisan." Fuji-Q Highland amusement park and the Fuji Five Lakes (including Lake Yamanaka and Lake Kawaguchi) are also nearby, making it easy to combine the festival with summer sightseeing around Mount Fuji. The local specialty Yoshida udon is a recommended meal before or after the festival."""
    },
]

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for item in ITEMS:
        cur.execute("""
            UPDATE festivals
            SET slug_ja = ?,
                slug_en = ?,
                manual_content_ja = ?,
                manual_content_en = ?,
                status = 'drafted'
            WHERE qid = ?
        """, (
            item["slug_ja"],
            item["slug_en"],
            item["manual_content_ja"],
            item["manual_content_en"],
            item["qid"],
        ))
        print(f"[OK] {item['qid']} ({item['slug_ja']}) updated to drafted")

    conn.commit()

    # Verify
    for item in ITEMS:
        cur.execute("""
            SELECT qid, label_ja, slug_ja, status,
                   LENGTH(manual_content_ja) AS len_ja,
                   LENGTH(manual_content_en) AS len_en
            FROM festivals WHERE qid = ?
        """, (item["qid"],))
        row = cur.fetchone()
        print(f"[VERIFY] qid={row[0]} label={row[1]} slug={row[2]} status={row[3]} len_ja={row[4]} len_en={row[5]}")

    conn.close()

if __name__ == "__main__":
    main()
