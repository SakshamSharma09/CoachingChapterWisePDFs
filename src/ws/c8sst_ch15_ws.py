"""Class 8 Social Science Ch 15 - Cultural Currents: 13th to 17th Centuries (NCERT Part 2 Ch 8): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c8sst_ch15"

def _base():
    s = importlib.util.spec_from_file_location("c8sst_c15", str(REPO / "src/rn_work/c8_sst2/c15.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The 'path of devotion', one of the paths to moksha that did not require rituals or priests, is called:", 1, "(b) bhakti marga", "E", opts=["jnana marga", "bhakti marga", "karma yoga", "ashrama dharma"]),
W("Kabir, presumably raised by a weaver couple, lived in the 15th century in present-day:", 1, "(c) Uttar Pradesh", "E", opts=["Tamil Nadu", "Maharashtra", "Uttar Pradesh", "Assam"]),
W("The 'father of Carnatic music' mentioned in the chapter is:", 1, "(a) Purandaradasa", "E", opts=["Purandaradasa", "Tansen", "Amir Khusro", "Kanakadasa"]),
W("The Sufi devotional song form fusing Indian, Persian and Arabic traditions, credited to Amir Khusro, is the:", 1, "(d) qawwali", "E", opts=["dhrupad", "abhang", "pattachitra", "qawwali"]),
W("Dara Shikoh is remembered for translating into Persian:", 1, "(b) 52 Upanishads", "E", opts=["the Mahabharata", "52 Upanishads", "the Lilavati", "the Guru Granth Sahib"]),
W("The first and only female ruler of the Delhi Sultanate was:", 1, "(c) Razia Sultan", "E", opts=["Nur Jahan", "Tirumalamba", "Razia Sultan", "Mirabai"]),
W("Tansen went to the court of which emperor, at his insistence?", 1, "(a) Akbar", "E", opts=["Akbar", "Jahangir", "Shah Jahan", "Krishnadevaraya"]),
W("Madhava, whose followers formed the 'Kerala School', made pioneering contributions to:", 1, "(d) calculus and infinite series", "E", opts=["Persian poetry", "temple architecture", "textile dyeing", "calculus and infinite series"]),
W("Fill in the blank: The Persian garden design with four parts and waterways, adopted by the Mughals, is the ______.", 1, "charbagh. (1)", "E"),
W("True or False: Carnatic music developed largely unaffected by Persian and Arabic influences.", 1, "True. (1)", "E"),
W("What is 'culture'? Name two things it includes.", 2, "Culture is the shared way of life of a group of people, passed down generations, shaping how they see the world and live (1). It includes values, morals, customs, traditions, art, music, literature, philosophy and science (any two, 1).", "E"),
W("State the three common patterns noticed in this turbulent period.", 2, "Continuation of traditional practices in communities (0.67); patronage from rulers of various backgrounds in arts, languages, literature and philosophy (0.67); active participation by people from all sections of society (0.66).", "E"),
W("Name two bhakti saints with their regions or languages.", 2, "Any two: Kabir (north, Uttar Pradesh); Ravidas (north); Guru Nanak (Punjab); Mirabai (Rajasthan); Chaitanya Mahaprabhu (east); Tukaram, Dnyaneshwar, Namdev (west); Purandaradasa, Kanakadasa (south). (1+1)", "E"),
W("What are 'zikr' and 'qawwali'?", 2, "Zikr is remembrance of God through repeated chanting or silent recitation of divine names (1). Qawwali is Sufi devotional singing fusing local classical styles with Persian and Arabic traditions, with powerful lyrics on love, faith and unity (1).", "E"),
W("Match: (a) Nur Jahan (b) Razia Sultan (c) Tirumalamba (d) Amir Khusro with (1) wrote Varadambika Parinaya (2) coins minted in her name (3) father of Urdu literature (4) first woman ruler of the Delhi Sultanate.", 2, "(a)-(2), (b)-(4), (c)-(1), (d)-(3). (Any four correct = 2; two or three correct = 1)", "E"),
W("Name two foods that came to India with Persian influence and the Indian dishes they became.", 2, "Sambuseh became the samosa (stuffed with potatoes and peas instead of meat and nuts) (1); zalabiyeh became the jalebi (circular coils and simple sugar syrup) (1). (Naan in a clay oven is also a Persian influence.)", "E"),
W("What is a GI tag? Which sari of the chapter has it?", 2, "A Geographical Indication tag gives weavers of an area rights over their knowledge and restricts who may use the name (1). Banarasi saris (from certain districts) have it (1).", "E"),
# ---------------- MEDIUM ----------------
W("Why has Indian culture been described as 'resilient'? Give three reasons from the chapter.", 3, "Deep roots and timeless values (1); scientific temper (1); rich philosophical and artistic traditions, and openness to adopting or adapting the best of external influences (1). Unlike Mesopotamia, Egypt, Greece and Rome, it stayed alive.", "M"),
W("Explain the role of the bhakti tradition in this period. Why did it become popular in times of political upheaval?", 3, "It was a path to moksha without rituals or priests, crystallised by the 6th century and renewed in this period (1). Verses and songs in local languages expressed love, compassion and equality, connecting people through music and dance (1). It showed cultural continuity and society's search for spiritual resilience amid political and religious upheaval (1).", "M"),
W("Source-based. 'kaba phir kasi bhaya, Ram bhaya re Rahim; mot chun maida bhaya baithi Kabira jim.' (i) Who composed it? (ii) What is the example of wheat and flour? (iii) What message does it give?", 3, "(i) Kabir (0.5). (ii) When wheat is ground into flour all differences between individual grains disappear (1). (iii) When one realises the divine, all differences between Ram and Rahim, names of god in Hinduism and Islam, dissolve; there is one god (1.5).", "M"),
W("State the messages of Ravidas and Guru Nanak. Where are Guru Nanak's teachings preserved?", 3, "Ravidas (early 16th century, family of leather-workers): equality and oneness of all, breaking the rigid walls of varna and jati (1). Guru Nanak: travelled across regions spreading the message of one God and equality of all people (1). His teachings, with hymns of several Hindu saints, are in the Guru Granth Sahib (1).", "M"),
W("What is Sufism? Name two Sufi saints and two features of Sufi practice.", 3, "A path of Islam focusing on devotion and an inner, personal search for god (1). Saints: Khwaja Moinuddin Chishti, Nizamuddin Auliya (1). Features: qawwali music, meditation like zikr, asceticism, inner silence, whirling dervishes (any two, 1).", "M"),
W("How did bhakti and Sufi traditions overlap? What did Dara Shikoh do and what happened to him?", 3, "Sufis adopted yogic and Vedantic techniques (inner silence, asceticism, meditation); poets brought together ideas from different religions (1). Dara Shikoh saw Vedanta and Sufism as converging on universal truth and had 52 Upanishads translated into Persian with scholars in Varanasi (1). Aurangzeb captured him, accused him of heresy and executed him (1).", "M", wp=True),
W("A stamp was released in 1964 on Purandaradasa's 400th death anniversary. (i) In which year did he die? (ii) Nilakantha Somayaji's planetary model dates from 1500 and Copernicus's heliocentric model from 1543; how many years apart? (iii) How many kirtanas is Purandaradasa said to have composed?", 3, "(i) 1964 - 400 = 1564 (1). (ii) 1543 - 1500 = 43 years; Nilakantha's model came earlier (1). (iii) As many as 4,75,000 (1).", "M", wp=True),
W("Who was Tansen? What is dhrupad and who patronised its development?", 3, "Tansen (Ramtanu Pandey) was a renowned musician who joined Akbar's court at his insistence and became one of its nine ratnas (1). Dhrupad (dhruva = fixed, pada = verse) is a genre of great antiquity (1), developed to new heights in the late 15th century under Raja Mansingh Tomar of Gwalior (1).", "M"),
W("Compare Rajput painting and Mughal miniature painting on themes and influences.", 3, "Rajput: from the 15th to late 19th century; traditional Hindu themes and expressions of beauty such as lotus, banyan trees, elephants, peacocks and women with large eyes (1.5). Mughal: distinct genre shaped by Persian influences, secular themes (landscapes, court scenes, portraits), height in Akbar's atelier where artists collaborated (1.5).", "M"),
W("What is a charbagh? Give two examples of Mughal-style gardens in the chapter.", 3, "A Persian design in four parts with gardens and waterways representing the rivers of Paradise, with water channels, fountains and terraces (1.5). Examples: Nishat Bagh, Srinagar (early 17th century); gardens at Amer Fort, Jaipur; Mughal Gardens at Rashtrapati Bhawan (any two, 1.5).", "M"),
W("Why did purdah become more widespread in parts of north India? Was it the same in the south?", 3, "Invasions and military campaigns from the 12th century affected women's status: women and children were captured and sold as slaves, and attempts were made to protect them (1.5). Purdah and ghunghat spread mainly in north India, and some scholars see the veil as a symbol of nobility (0.5). In the south the situation did not change much: elite women continued in administration, and Hampi engravings show them in public life (1).", "M"),
W("Describe Razia Sultan's rule in three points. Why did it end?", 3, "She was the first and only woman ruler of the Delhi Sultanate in the early 13th century (1). She led military campaigns, set up educational institutions across Delhi and prioritised merit-based administration (1). She appeared unveiled at court and addressed the public; these 'rebellious' acts fuelled a conspiracy that ended her brief reign (1).", "M"),
W("Write three facts about Nur Jahan's role in the Mughal Empire.", 3, "Married to Emperor Jahangir, she was among the most influential women of the Mughal Empire in the early 17th century (1). She issued royal orders, attended court meetings and had coins minted in her name (1). She supported art, architecture and trade and was known for intelligence, leadership and style (1).", "M"),
W("How did Banarasi silk saris and Pashmina shawls show cultural exchange?", 3, "Weavers from Gujarat moved to Banaras with Akbar's encouragement, bringing their expertise; Mughals introduced zari or zardozi and brocades, with nature-inspired and geometric designs (1.5). Pashmina is woven from cashmere of Ladakh and Kashmir goats, patronised by the Mughals as a symbol of nobility, with Persian floral embroidery and the buta (paisley) motif (1.5).", "M"),
W("How did Persian influence enter Indian literature and administration? Give two examples of translation.", 3, "Persian became the language of administration and courtly culture, producing histories and poetry and preserving earlier Indian knowledge (1). Loan words from Persian entered regional languages (1). Translations: Bhaskaracharya's Lilavati into Persian (by Faizi, three translations) and Kalhana's Rajatarangini (1).", "M"),
W("How did Urdu develop? Who is called the 'father of Urdu literature'?", 3, "Urdu developed in the Ganga-Yamuna plains from the Hindi/Hindavi spoken there, integrating Arabic and Persian words (1); south of the Deccan it became Dakhini with loan words from Telugu and Marathi (1). Amir Khusrau, who wrote in Hindavi, Punjabi and Braj Bhasha, is called its father (1).", "M"),
W("Find the mistakes and correct them: 'Tansen was at the court of Krishnadevaraya, and Carnatic music was strongly shaped by Persian influences.'", 2, "Tansen was at Akbar's court (1); Carnatic music developed independently, largely unaffected by Persian and Arabic influences, while Hindustani music in the north interacted with them (1).", "M"),
W("Timeline. Arrange from earliest to latest: Nilakantha Somayaji's planetary model; Razia Sultan's reign; Kabir; Nishat Bagh in Srinagar; Dara Shikoh.", 3, "Razia Sultan (first half of the 13th century); Kabir (15th century); Nilakantha (1500); Nishat Bagh (early 17th century); Dara Shikoh (17th century). (3 for the correct order; 2 if one pair is swapped)", "M"),
# ---------------- HARD ----------------
W("Source-based. The Portuguese traveller Fernao Nunes wrote of the Vijayanagara king: 'He has also women who wrestle, and others who are astrologers and soothsayers; ... women who write all the accounts of expenses ... and women for music.' (i) List four vocations. (ii) What does it show about women in the south? (iii) What other evidence supports it?", 4, "(i) Wrestlers, astrologers and soothsayers, accountants or writers of the kingdom's affairs, musicians and singers (any four, 2). (ii) Women had public roles and responsibilities in the king's staff (1). (iii) The wall engravings at Hampi depict women in public life; inscriptions record temple donations, community halls and wells built by women (1).", "H"),
W("Source-based. A 10th-century Arab chronicler wrote that Indian princes 'allow their women to be seen by the men who attend' court and 'no veil conceals them'. (i) Who wrote it? (ii) What does it say about the earlier period? (iii) How did the picture change later and why?", 4, "(i) Abu Zaidu-l Hasan (1). (ii) Women in royal courts appeared without veils in public (1). (iii) After the invasions from the 12th century, women's public appearance and engagement declined and purdah and ghunghat spread in parts of north India, partly to protect them and partly as a symbol of nobility (2).", "H"),
W("Source-based. Abul Fazl wrote of Hindu painters: 'Their pictures surpass our conception of things.' (i) Who was Abul Fazl? (ii) What does his praise show? (iii) How did Rajput and Mughal painting influence each other?", 4, "(i) The author of the Ain-i-Akbari, Akbar's court historian (1). (ii) Mughal courts admired the skill of Hindu painters, so there was respect across traditions (1). (iii) Exchanges in style, technique and colours; plants, gardens, animals and hunting scenes entered Rajput paintings; Mughal court painters who migrated to Bikaner blended styles, while Hindu themes continued (2).", "H"),
W("Case study. Dara Shikoh is called an advocate of Hindu-Muslim harmony. List three things he did or believed, one lasting effect of his work, and what his fate suggests.", 4, "Seen with yogis, pandits and Muslim scholars; saw Vedanta and Sufism converging on universal truth; translated 52 Upanishads into Persian with scholars in Varanasi (any three, 2). The translations later reached Europe and influenced leading 19th-century philosophers (1). He was persecuted, accused of heresy and executed by Aurangzeb, showing the cost of such ideas in political struggle (1).", "H"),
W("Compare the bhakti and Sufi traditions on beliefs, practice, music and bridging cultures. Give one example each.", 5, "Beliefs: bhakti: devotion to god, equality, one god (Kabir, Guru Nanak); Sufism: inner personal search for god in Islam (1.5). Practice: bhakti did not need rituals or priests; Sufis used meditation, zikr and asceticism (1). Music: bhajans, kirtans, abhangs with instruments and dance; qawwalis fusing local, Persian and Arabic styles (1.5). Bridging: both overlapped, e.g. Kabir's 'Ram and Rahim' and Dara Shikoh; Sufi poet Rumi on unity (1).", "H"),
W("Describe the achievements of the Kerala School of Astronomy and Mathematics and of two other scientific contributions mentioned for this period.", 4, "Madhava: pioneering calculus, series expansion for trigonometric functions and an exact value of pi as an infinite series, both world firsts (1.5). Nilakantha Somayaji (1500): planetary model with Mercury and Venus going round the Sun, decades before Copernicus (1543) (1). Others: production of pure zinc by a special distillation process; Narayana Pandita's Ganitakaumudi (14th century); saltpetre for gunpowder and refrigeration; Itr Jahangir perfume (any two, 1.5 combined).", "H"),
W("Explain how the same events affected women differently in north and south India, and name two factors from the chapter that may explain the difference.", 4, "North: invasions, slavery of women and children, jauhar, so protective measures led to purdah and ghunghat and a decline in public appearance (1.5). South: norms did not change much; elite women continued in administration, issued grants and made donations (1.5). Factors: where invasions and military campaigns reached, local customs, and the status of ruling classes (practised by the Muslim aristocracy in the north) (1).", "H"),
W("Show how temples and educational centres showed resilience. Use Srirangam, Vijayanagara's purvamaryade and the loss of Nalanda and Vikramashila.", 4, "The Sri Ranganathaswamy Temple at Srirangam was ravaged in the early 14th century but rebuilt by the end of the century, with new temples added later (1.5). Vijayanagara rulers followed purvamaryade, supporting temples and mathas so education continued (1). Nalanda and Vikramashila were destroyed in the late 12th century, a huge cultural loss, but gurukulas, mathas, temple schools, pathashalas and apprenticeships, being decentralised, survived (1.5).", "H"),
W("Table of cultural exchange. Write one example each of an exchange in (i) food, (ii) clothing, (iii) music instruments, (iv) gardens, explaining what was adopted and how it was adapted.", 4, "(i) Samosa from Persian sambuseh, stuffing changed to potato and peas; jalebi from zalabiyeh with circular coils and sugar syrup (1). (ii) Jama, pyjama and angrakha adopted from Persian court fashion and adapted to Indian fabrics, with muslin dupattas and the sari continuing (1). (iii) Sitar and tabla evolved with older Indian instruments such as the pakhawaj (1). (iv) Persian charbagh with fountains and terraces used around forts, tombs and mosques, and copied at Amer Fort (1).", "H"),
W("HOTS. The chapter says Indian culture 'adopted or adapted' external influences. Why might adaptation help a culture survive better than copying or rejecting? Support with two examples.", 3, "Adapting keeps the core while allowing new ideas to enrich it; copying loses identity and rejecting blocks growth (1). Examples: Tansen kept composing for Krishna and Shiva while influenced by a Sufi saint; samosa and jalebi were adapted; Urdu mixed Hindavi with Persian; Banarasi brocade combined Gujarati skill with Mughal zari (any two, 2).", "H"),
W("Application. You are asked to give a 3-minute talk on Kabir or Mirabai. Write the outline: (a) the song or doha chosen, (b) its message, (c) why it appealed to ordinary people, (d) its relevance today.", 4, "(1 mark each for a clear point) Sample on Kabir: (a) the doha 'kaba phir kasi bhaya, Ram bhaya re Rahim'; (b) all differences between Ram and Rahim vanish in the oneness of god; (c) simple everyday example of flour, local language, criticism of rituals of both religions, so people from all communities could relate; (d) it promotes harmony and equality in a diverse society today.", "H", wp=True),
W("'Music and dance played a significant role in spreading the message of bhakti.' Do you agree? Give three reasons.", 3, "Yes. Songs and bhajans in local languages could reach everyone, including the unlettered (1). Singing and dancing together to instruments brought people from all sections of society to join in, breaking barriers (1). Music is easy to remember and pass on; bhajans of that time are still sung today (1).", "H"),
W("Cause and effect. How did invasions and political instability affect education and what kept learning alive? Give four points.", 4, "Invasions and campaigns disrupted education; the destruction of Nalanda and Vikramashila in the late 12th century dispersed scholars (1.5). Yet learning continued in villages and temples through gurukulas, mathas, pathashalas, vihara and Jain palli, with madrasas for Arabic, Persian, Hindavi and Islamic studies (1.5). Jati and shreni systems with apprenticeships carried crafts and trades, protected by kings, saints and poets (1).", "H"),
W("Describe how literature in regional languages and translation enriched culture in this period. Give four examples.", 4, "Chaitanya Mahaprabhu influenced 16th-century Bengali literature, including biographies and Dhamali folk songs on Krishna (1). Kavindra Paramesvara translated the Mahabharata into Bengali; Persian poetry was translated into Bengali (1). Tirumalamba wrote the Sanskrit kavya Varadambika Parinaya at Achyutadevaraya's court; Krishnadevaraya and the Gajapati kings of Odisha patronised poets (1). Lilavati and Rajatarangini were translated into Persian and the Mahabharata into Persian as the Razmnama (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "Timeline of Cultural Currents (13th–17th Centuries)"),
 ("table", ["Period", "Development"], [
  ["6th–9th century", "Alvars and Nayanars compose the Divya Prabandham and Tiruvachakam"],
  ["10th–11th century", "Paper reaches India; painting moves from walls to paper"],
  ["Late 12th century", "Nalanda and Vikramashila destroyed in invasions"],
  ["13th century", "Razia Sultan rules in Delhi; Konark Sun Temple; Eastern Ganga dynasty"],
  ["Mid-13th to early 14th", "Amir Khusro, Indo-Persian poet and singer; qawwali"],
  ["Early 14th century", "Srirangam temple ravaged; rebuilt by the end of the century"],
  ["14th century", "Narayana Pandita's Ganitakaumudi; Madhava of the Kerala School"],
  ["15th century", "Kabir; Ranakpur temple; Raja Mansingh Tomar's dhrupad; Purandaradasa (15th–16th c.)"],
  ["Early 16th century", "Ravidas; Kavindra Paramesvara; Chaitanya Mahaprabhu (16th c.)"],
  ["1500", "Nilakantha Somayaji's planetary model"],
  ["1543", "Copernicus's heliocentric model (compare)"],
  ["1598", "Razmnama folio painting"],
  ["Early 17th century", "Nur Jahan; Nishat Bagh, Srinagar"],
  ["Mid-17th century", "Dara Shikoh translates 52 Upanishads; Bikaner Holi painting"],
  ["1623", "Pietro Della Valle writes about schools in coastal Karnataka"]]),
 ("h2", "Key Terms"),
 ("table", ["Term", "Meaning"], [
  ["**Culture**", "Shared way of life of a group, passed on through generations"],
  ["**Bhakti marga**", "Path of devotion, a path to moksha without rituals or priests"],
  ["**Moksha**", "Realisation of Truth or release from the cycle of death and rebirth"],
  ["**Sufism / zikr**", "Inner, devotional path of Islam / chanting of divine names"],
  ["**Qawwali**", "Sufi devotional song fusing Indian, Persian, Arabic styles"],
  ["**Dhrupad**", "Ancient genre: fixed verse; flourished in Gwalior"],
  ["**Pattachitra**", "Cloth painting telling epic stories (Odisha, West Bengal, Andhra Pradesh)"],
  ["**Atelier**", "An artist's studio"],
  ["**Charbagh**", "Persian four-part garden"],
  ["**Purdah / ghunghat**", "Curtain or veil / head covering"],
  ["**Jauhar**", "Self-immolation by women to avoid capture"],
  ["**Pathashala, matha, madrasa**", "Village school, monastic centre of learning, Muslim school"],
  ["**Hindavi**", "Early Hindi-Urdu with Indian grammar and Persian and Arabic words"],
  ["**Brocade, zari**", "Rich raised-pattern fabric; gold or silver thread work"],
  ["**GI tag**", "Geographical Indication protecting a region's product name"],
  ["**Purvamaryade**", "Following previously established practices of dharma and social norms (Vijayanagara)"]]),
 ("h2", "Comparing the Currents"),
 ("table", ["Feature", "Bhakti", "Sufi"], [
  ["Religion", "Hindu and Sikh tradition (and others)", "Islam"],
  ["Core idea", "Devotion and oneness of god; equality", "Inner search for god; love and unity"],
  ["Practice", "Bhajans, kirtans, abhangs; no rituals or priests needed", "Qawwali, zikr, meditation, asceticism"],
  ["Language", "Local languages", "Persian, Hindavi and local languages"],
  ["Examples", "Kabir, Ravidas, Nanak, Mirabai, Tukaram", "Moinuddin Chishti, Nizamuddin Auliya, Amir Khusro, Rumi"]]),
 ("table", ["Hindustani music", "Carnatic music"], [
  ["North India", "South India"],
  ["Interacted with Persian and Arabic influences; dhrupad, Tansen", "Developed independently, largely unaffected"],
  ["Patrons: Raja Mansingh Tomar, Akbar", "Purandaradasa at Krishnadevaraya's Vijayanagara court"]]),
 ("h2", "Map and Picture Pointers"),
 ("ul", ["Locate **Delhi, Gwalior, Agra, Amer (Jaipur), Bikaner, Udaipur, Kota, Ranakpur, Banaras, Srinagar, Hampi (Vijayanagara), Srirangam, Kanchipuram, Sringeri, Konark, Shravanabelagola, Kerala** on a map.",
  "Mark bhakti regions: Kabir and Ravidas (north), Mirabai (Rajasthan), Chaitanya (east), Tukaram, Dnyaneshwar, Namdev (Maharashtra), Purandaradasa and Kanakadasa (south).",
  "Pictures: Kabir with attendants, Ravidas, Chaitanya dancing, whirling dervishes, Tansen, Amir Khusro stamp, Rajput and Mughal paintings, Nishat Bagh, Sheesh Mahal, Banarasi brocade, pashmina buta motif."]),
 ("h2", "Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Political and religious upheaval", "Renewed popularity of bhakti; saints' message of equality"],
  ["Mughal patronage with Persian influence", "Mughal miniature, charbagh gardens, Persian translations"],
  ["Persian as administrative language", "Loan words in regional languages; Urdu"],
  ["Invasions and campaigns", "Greater seclusion of women in north India; loss of Nalanda"],
  ["Decentralised learning and guilds", "Education and crafts survived turmoil"],
  ["Royal and community patronage", "Temples rebuilt (Srirangam); Hampi's golden age"]]),
 ("h2", "Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Describe the contribution of bhakti saints. (5 marks)", "Kabir spoke of one god and criticised rituals of both Hinduism and Islam; Ravidas preached equality and broke barriers of varna and jati; Guru Nanak taught one God and equality, preserved in the Guru Granth Sahib; Mirabai, Chaitanya, Tukaram, Dnyaneshwar, Namdev, Purandaradasa and Kanakadasa spread devotion in local languages through songs and dance. People of all sections participated, and these bhajans are sung even today."),
  ("How did Rajput and Mughal painting influence each other? (3 marks)", "Rajput painting depicted Hindu themes; Mughal miniatures, shaped by Persian influence, showed courts and portraits. They exchanged style, technique and colours; Rajput works included gardens, animals and hunting scenes; Mughal painters moved to Bikaner and blended styles."),
  ("What was the status of women in this period? (5 marks)", "In the north, invasions led to seclusion, purdah and ghunghat, though a few women such as Razia Sultan and Nur Jahan ruled or governed. In the south the status largely continued: elite women held administration roles, made donations and built halls and wells; Hampi engravings and Fernao Nunes show women in public life. Economic prosperity involved women's active participation."),
  ("Why were music, art and learning not destroyed during this period? (3 marks)", "Continuation of tradition, patronage by rulers of different backgrounds and participation by all sections of society kept them alive; local, decentralised institutions such as temple schools and guilds survived political turmoil."),
 ]),
]
CH["takeaways"] += ["Know the three patterns: continuation, patronage and participation.",
  "Match saints and artists to region and message: bhakti (equality, one god), Sufism (love and unity), and know examples of exchange: samosa, jalebi, Urdu, charbagh.",
  "Women's status differed by region: purdah in the north, continued public roles in the south."]

if __name__ == "__main__": run(__file__, BANK, 8, "Social_Science", WS, CH)
