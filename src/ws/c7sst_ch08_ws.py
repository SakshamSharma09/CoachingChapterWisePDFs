"""Class 7 Social Science Ch 8 - The Gupta Era (NCERT Ch 7): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c7sst_ch08"

def _base():
    s = importlib.util.spec_from_file_location("c7sst_c08", str(REPO / "src/rn_work/c7_sst/c08.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The capital of the Gupta Empire was:", 1, "(b) Pataliputra (present-day Patna)", "E", opts=["Ujjayini", "Pataliputra (present-day Patna)", "Kanchipuram", "Nandivardhana"]),
W("The Iron Pillar at Mehrauli in Delhi was erected during the reign of:", 1, "(d) Chandragupta II", "E", opts=["Chandragupta Maurya", "Chandragupta I", "Samudragupta", "Chandragupta II"]),
W("The Prayaga Prashasti was composed by the court poet:", 1, "(a) Harisena", "E", opts=["Harisena", "Kalidasa", "Varahamihira", "Faxian"]),
W("Aryabhata wrote a short treatise on mathematics and astronomy called the:", 1, "(c) Aryabhatiya", "E", opts=["Brihat Samhita", "Meghadutam", "Aryabhatiya", "Charaka Samhita"]),
W("The Chinese pilgrim who visited India in the early 5th century CE was:", 1, "(b) Faxian", "E", opts=["Megasthenes", "Faxian", "Heliodorus", "Harisena"]),
W("The Pallava capital, known as the 'city of a thousand temples', was:", 1, "(d) Kanchipuram", "E", opts=["Madurai", "Ujjayini", "Nalanda", "Kanchipuram"]),
W("The Vakataka capital was Nandivardhana, near present-day:", 1, "(a) Nagpur", "E", opts=["Nagpur", "Patna", "Karur", "Guwahati"]),
W("Fill in the blank: The Iron Pillar has not rusted for about ______ years.", 1, "1,600 (1)", "E"),
W("Write True or False: Chandragupta II was also known as Vikramaditya.", 1, "True. (1)", "E"),
W("Who wrote Meghadutam, and what does the title mean in English?", 2, "Kalidasa wrote it; the title means 'The Cloud Messenger'. (1+1)", "E"),
W("Name the tribe from Central Asia whose repeated attacks weakened the Gupta Empire.", 1, "The Hunas. (1)", "E"),
W("What are copper plates, as used in the Gupta administration?", 2, "They were metal plates on which land grants to local rulers, priests and chieftains were inscribed to keep accurate records. (2)", "E"),
W("Name two great scientists of the Gupta period and one field each worked in.", 2, "Aryabhata (mathematics and astronomy) and Varahamihira (astronomy, mathematics, astrology; encyclopedic work). (1+1)", "E"),
W("In which present-day state are (i) the Udayagiri caves and (ii) the Ajanta caves located?", 2, "Udayagiri is in Madhya Pradesh and Ajanta is in Maharashtra. (1+1)", "E"),
W("Which Gupta king is shown playing the veena on a coin?", 1, "Samudragupta. (1)", "E"),
W("Give the modern place name of the Gupta capital Pataliputra and of the ancient Saketa.", 2, "Pataliputra is present-day Patna; Saketa is Ayodhya. (1+1)", "E"),
W("What does 'regent' mean?", 2, "A regent is a person who temporarily governs a kingdom for a monarch who is unable to do so, until they can. (2)", "E"),
# ---------------- MEDIUM ----------------
W("Why is the Iron Pillar of Delhi called a 'testament to advanced metallurgical skills'? Give the explanation scientists offer for its not rusting.", 3, "It is a 6-tonne iron pillar that has stood in the open for about 1,600 years without rusting (1). Scientists believe a thin protective layer forms on its surface from the special iron used and oxygen in the air (1), which shields the metal from corrosion; this shows the advanced metal-working skills of ancient India (1).", "M"),
W("Why is the Gupta period called the 'classical age' of India?", 3, "A long period of peace and stability supported achievements in many fields (1). Sanskrit literature, mathematics, astronomy, medicine, metallurgy and art all flourished, and knowledge from earlier eras was compiled in texts (1). A strong economy allowed the state to support scholars, artists and scientists (1).", "M"),
W("Name three titles adopted by Gupta rulers. How were they different from earlier titles and what did they claim?", 3, "Maharajadhiraja, samrat and chakravartin (1). Earlier kings used simpler titles like rajan and maharaja (1). The new titles claimed supreme authority and superiority over earlier rulers (1).", "M"),
W("Source-based. 'The people are numerous and happy... Those who farm royal land pay a portion of their grain... Heads of Vaishya families establish houses for charity and medicines.' (Faxian). (i) Who was Faxian? (ii) Write two features of Gupta society from the passage.", 3, "(i) A Chinese Buddhist pilgrim who came to India in the early 5th century CE to visit sacred sites and collect manuscripts (1). (ii) Any two: people prosperous and happy; farmers on royal land paid a share of grain; royal attendants had salaries; merchants set up charitable houses and medical care for the poor, orphans and sick (1+1).", "M"),
W("Faxian's account is valuable but 'reflects only the writer's perspective'. What other fact does he record, and what should historians do about such accounts?", 3, "He also describes the harsh treatment of the chandalas, regarded as outcastes living outside the city (1). A traveller's account shows only one writer's view at one point in time (1), so historians should compare many sources and perspectives before drawing conclusions (1).", "M"),
W("How did Prabhavati Gupta show the importance of matrimonial alliances? Answer in three or four lines.", 3, "She was Chandragupta II's daughter, married to a prince of the Vakataka kingdom, the southern neighbours of the Guptas (1). The prince died early and she became regent ruler (1). She kept Vakataka-Gupta ties strong; her inscription calls her 'mother of two kings' (1). (She is also linked to seven Vishnu temples, some at Ramagiri (Ramtek), Maharashtra.)", "M"),
W("Describe how the Gupta administration worked and how it helped the kings.", 3, "The empire was divided into provinces rather than being controlled entirely from one centre (1). Land was granted to local rulers, priests and chieftains and recorded on copper plates (1). This ensured proper tax collection and efficient governance while leaving some control with local leaders (1).", "M"),
W("List four sources of Gupta revenue and two ways in which the money was used.", 3, "Sources (any four): land tax (the main one), fines, taxes on mines, irrigation, trade, crafts (2). Uses (any two): administration, maintaining the army, building temples and infrastructure, supporting scholars and artists (1).", "M"),
W("Why is Socotra Island important in the study of Gupta-age trade?", 3, "It lies in the Arabian Sea, a strategic stop on the way to the Mediterranean markets (1). Pottery, Brahmi inscriptions and a stupa design found there show that Indian traders stayed there for centuries (1), along with traders from Egypt, Arabia, Rome and Greece, so it shows trade led to cultural exchange (1).", "M"),
W("Give any three contributions of Aryabhata mentioned in the chapter.", 3, "Any three: wrote the Aryabhatiya; gave formulas for the motion of the Sun, Moon and planets; said the Earth spins on its axis causing day and night; calculated the length of a year; gave a fair estimate of Earth's size; explained solar and lunar eclipses correctly; described calculation and equation-solving techniques. (1 each)", "M"),
W("Aryabhata gave the year as 365 days 6 h 12 min 30 s. The modern value in the chapter is 365 days 5 h 48 min 45 s. By how much was Aryabhata's value more than the modern one?", 3, "6 h 12 min 30 s minus 5 h 48 min 45 s (1). 6 h 12 min 30 s = 5 h 72 min 30 s = 5 h 71 min 90 s; so 5 h 71 min 90 s minus 5 h 48 min 45 s (1) = 23 min 45 s (1). So he was only a little under 24 minutes off.", "M", wp=True),
W("Match: (a) Kusumapura (b) Ujjayini (c) Sarnath with (1) Buddha sculptures (2) Varahamihira (3) Aryabhata.", 3, "(a) with (3), (b) with (2), (c) with (1). (1 each)", "M"),
W("What does the Ayurveda passage say about the Charaka Samhita and Sushruta Samhita?", 3, "Ayurveda has roots several centuries BCE (1), but these two texts were compiled and given their final shape in the Gupta period (1). They deal with diseases and diagnosis, treatment, diet, medicines and surgical techniques, and stress healing of mind, body and nature together (1).", "M"),
W("Mark the mistake and correct it: 'Ajanta caves are in Madhya Pradesh and show Buddhist wall paintings; they were made by the Pallavas.'", 2, "Ajanta is in present-day Maharashtra (1); the caves were carved with the support of the Guptas and the Vakatakas, not the Pallavas (1).", "M"),
W("Why did the Gupta rulers, who were devotees of Vishnu, also patronise Buddhist institutions? Give two examples of the Buddhist support.", 3, "Their approach was inclusive and open to many traditions (1). They patronised the renowned Nalanda university (1) and other Buddhist viharas (monasteries) (1).", "M"),
W("Who were the Pallavas? Where did they rule and what were their contributions?", 3, "A southern dynasty that gradually consolidated power in parts of present-day Tamil Nadu, Karnataka, Telangana and Andhra Pradesh, possibly first tributaries of the Satavahanas (1). Capital Kanchipuram, 'city of a thousand temples' (1). Most were Shiva devotees and built temples and rock-cut caves, and promoted learning through ghatikas (1).", "M"),
W("Where was the Kamarupa kingdom? Who ruled it and what was an ancient name of this region?", 3, "In the Brahmaputra valley, roughly present-day Assam, and the northern parts of present-day Bengal and Bangladesh (1). It was ruled by the Varman dynasty (1). The ancient name was Pragjyotisha (1).", "M"),
W("Match: (a) Chandragupta I (b) Samudragupta (c) Prabhavati Gupta with (1) regent of the Vakataka kingdom (2) coin with queen Kumaradevi (3) 'dharani-bandha'.", 3, "(a) with (2), (b) with (3), (c) with (1). (1 each)", "M"),
# ---------------- HARD ----------------
W("Explain why Chandragupta II is written with 'II'. Who is the other Chandragupta of the same dynasty, and why should students not confuse him with Chandragupta Maurya?", 3, "Historians added the number because there was an earlier Chandragupta in the dynasty: Chandragupta I, his grandfather (1). Chandragupta I helped the early expansion of the Gupta Empire and is remembered for his coins and strategic alliances (1). Chandragupta Maurya belonged to the earlier Maurya dynasty, which ruled centuries before (1).", "H"),
W("Source-based. 'Neither force nor mere diplomacy can eliminate evil; nor is righteousness upheld by flattery alone. It is wisdom and knowledge that truly strengthen a kingdom.' (Kalidasa, Raghuvamsham). Explain the message and link it with the Gupta age.", 4, "The poet says that a kingdom is made strong by wisdom and knowledge, not just by force, diplomacy, flattery or luxury (2). The Guptas supported scholars, scientists and artists, and in peace and stability the arts, literature, medicine and science flourished (2).", "H"),
W("Case study. Riya's class visits Delhi and sees the Iron Pillar. The guide says it was probably first set up near the Udayagiri caves. (i) Who built it, and for whom was it dedicated? (ii) Why would the king add an inscription? (iii) What does it teach about science?", 4, "(i) It was erected in the reign of Chandragupta II (the 'Chandra' of the inscription) and dedicated to Vishnu (1). (ii) Inscriptions celebrate the king's achievements and proclaim them to future generations (1). (iii) It shows advanced metallurgy: the thin protective layer formed by the special iron and oxygen keeps it from corroding (2).", "H", wp=True),
W("Read the Prayaga Prashasti passage. How does it describe Samudragupta's aim and treatment of defeated kings, and how does the chapter say the south and north-east were treated?", 4, "The aim was 'dharani-bandha', to unify the Earth (1). He defeated many kings and took over their kingdoms; some were reinstated and offered tribute, others submitted out of fear (1). In the south he defeated a Pallava ruler and in the north-east the ruler of Kamarupa, but did not take over their lands (1); they could keep their thrones if they accepted his rule and paid tribute, which kept relations peaceful (1).", "H"),
W("Compare the Pallavas and the Guptas on location, capital, the god most rulers followed, and one contribution.", 4, "Guptas: north India, capital Pataliputra, mostly Vishnu devotees; contributions such as the Iron Pillar, Ajanta and Aryabhata (2). Pallavas: south (Tamil Nadu and nearby), capital Kanchipuram, mostly Shiva devotees; contributions such as magnificent temples and rock-cut caves and ghatikas (2).", "H"),
W("'Periods of peace support the development of sociocultural life, literature, and science.' Examine this statement with four examples from the Gupta Empire.", 5, "Peace and stability meant the state could support scholars, artists and scientists (1). Literature: Kalidasa and the Puranas (1). Science: Aryabhata and Varahamihira in mathematics and astronomy, and medical texts such as Charaka and Sushruta (1). Metallurgy: the Iron Pillar (1). Art: Sarnath, Ajanta, Udayagiri and Deogarh (1).", "H"),
W("Timeline. In order from earliest to latest, arrange: the Hunas attack (6th century CE), Faxian's visit (about AD 399-414), the weakening of the Kushanas (3rd century CE), Aryabhata at Kusumapura (about 500 CE). Write the century for each.", 4, "Kushana weakening (3rd century CE) (1); Faxian's visit (early 5th century CE, AD 399-414) (1); Aryabhata (about 500 CE; 5th to 6th century) (1); Hunas attack (6th century CE) (1).", "H"),
W("Why does the chapter call Varahamihira a 'pioneer in science'? Describe his Brihat Samhita.", 4, "Because he could observe the world, use logical reasoning and combine it with traditional knowledge (2). The Brihat Samhita is an encyclopedic work covering astronomy and astrology, weather forecasting, architecture, town planning and even farming (2).", "H"),
W("Case study. Arjun reads Faxian's description of Gupta cities in his textbook. Using only the passage, describe two ways in which the cities cared for people, and state one limit of using this source.", 4, "From the text: heads of Vaishya families set up houses for charity and medicines, caring for the poor, orphans and the sick (1); doctors give treatment and the needy receive food and medicines (1). Limit: it reflects only the writer's perspective at one point in time and for a limited part of society; elsewhere he describes the harsh treatment of chandalas (2).", "H", wp=True),
W("Explain why Gupta art 'set high standards of aesthetics and beauty'. Give three examples with place and state.", 4, "Rulers created a supportive environment for creativity and craftsmanship (1). Examples: Sarnath (near Varanasi, Uttar Pradesh), exquisite Buddha sculptures; Ajanta caves (Maharashtra), rock-cut caves and paintings such as Padmapani; Udayagiri (Madhya Pradesh), rock-cut caves with carvings of deities; Deogarh Dashavatara temple (Uttar Pradesh), Vishnu on Sheshnag; terracotta Ganga and Yamuna from Ahichchhatra (any three, 1 each).", "H"),
W("Why did the Gupta Empire decline? Give one external and one internal reason and say what the chapter suggests came next.", 3, "External: repeated attacks by the Huna tribe from Central Asia, which weakened control over north India (1). Internal: the rise of powerful regional rulers led to conflicts (1). The chapter hints this was not just an end but the beginning of a new period and a turning point in Indian history, to be studied in the next part (1).", "H"),
W("The Vakatakas were 'allies of the Guptas'. Give two pieces of evidence from the chapter and explain why alliances mattered to an empire.", 4, "Evidence: Prabhavati Gupta, Chandragupta II's daughter, married a Vakataka prince and ruled as regent (1); she kept ties strong, and the Ajanta caves were carved with the support of the Guptas and the Vakatakas (1). Alliances, including matrimonial ones, helped the Guptas expand and consolidate their empire peacefully and keep neighbours friendly (2).", "H"),
W("Imagine you are a young student at Nalanda during the Gupta era writing a letter home. Mention four things from the chapter that you saw or heard about in the empire.", 4, "(1 each for any four relevant, accurate points) Example: scholars like Aryabhata and Varahamihira; Kalidasa's poetry such as Meghadutam; the Iron Pillar; charitable houses and medicines run by merchants; trade with Southeast Asia and China; the king's titles; land grants on copper plates; Ajanta paintings.", "H", wp=True),
]

CH = _base()
def _sub(o, a, b):
    if isinstance(o, str): return o.replace(a, b)
    if isinstance(o, list): return [_sub(x, a, b) for x in o]
    if isinstance(o, tuple): return tuple(_sub(x, a, b) for x in o)
    return o
CH["blocks"] = _sub(CH["blocks"], "; ashvamedha coins mark the horse sacrifice", "")
CH["blocks"] += [
 ("h2", "8.11 Timeline of the Gupta Era"),
 ("table", ["Period", "Event"], [
  ["By the 3rd century CE", "Kushana empire weakens; Guptas rise as regional rulers near present Uttar Pradesh"],
  ["3rd to 6th century CE", "The Gupta Empire flourishes; capital Pataliputra"],
  ["Chandragupta I", "Early expansion, strategic alliances; coin with Queen Kumaradevi and Lakshmi"],
  ["Samudragupta", "Warrior king; Prayaga Prashasti by Harisena; veena coin"],
  ["Chandragupta II (Vikramaditya)", "Peak of art, science and literature; Iron Pillar; his daughter Prabhavati Gupta rules the Vakatakas as regent"],
  ["Early 5th century CE (AD 399-414)", "Chinese pilgrim Faxian visits India"],
  ["About 500 CE", "Aryabhata at Kusumapura; Aryabhatiya"],
  ["6th century CE", "Huna attacks and rise of regional rulers; decline of the Guptas"],
  ["Up to the later 9th century CE", "Pallavas of Kanchipuram rule in the south"]]),
 ("note", "REMEMBER", "The Guptas, the Vakatakas, the Pallavas and Kamarupa were all contemporaries. When a question asks 'what was happening in the rest of the subcontinent', give these three, with capitals and regions."),
 ("h2", "8.12 Key Terms and Key People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Dharani-bandha**", "'Unifier of the Earth': Samudragupta's ambition in the Prayaga Prashasti"],
  ["**Prashasti**", "A praise-inscription describing a ruler's achievements"],
  ["**Regent**", "Someone who temporarily governs for a ruler unable to rule"],
  ["**Tributary**", "A ruler who keeps his throne by accepting a stronger king's rule and paying tribute"],
  ["**Copper plate**", "Metal plate on which land grants were inscribed"],
  ["**Outcastes (chandalas)**", "People considered too low to be part of the varna system"],
  ["**Codified**", "Arranged or written in an organised and systematic way, e.g. Ayurveda texts"],
  ["**Vihara**", "A Buddhist monastery"],
  ["**Ghatika**", "A centre of learning that emerged in Satavahana times"],
  ["**Harisena**", "Court poet who wrote the Prayaga Prashasti"],
  ["**Faxian**", "Chinese pilgrim; wrote A Record of Buddhistic Kingdoms"],
  ["**Kalidasa**", "Poet of Meghadutam and Raghuvamsham"],
  ["**Aryabhata / Varahamihira**", "Mathematician-astronomers; Aryabhatiya / Brihat Samhita"],
  ["**Vikramaditya**", "Another name of Chandragupta II"]]),
 ("h2", "8.13 Map and Picture Pointers"),
 ("ul", ["On the map of the Gupta Empire (Fig. 7.8) locate **Pataliputra, Prayaga, Saketa, Kashi, Vaishali, Tamralipti, Ujjayini, Indraprastha**, the Ganga, Yamuna and Narmada rivers, and the allied **Vakataka** kingdom; the east coast down to **Kanchipura (Pallava)** and **Kamarupa** in the north-east.",
  "Mark the present-day states where the Guptas ruled and count them, as the chapter's activity suggests (most of north and west India, parts of central and east India).",
  "Sites: **Mehrauli (Delhi)**: Iron Pillar; **Sarnath (near Varanasi)**: Buddha sculptures; **Ajanta (Maharashtra)**; **Udayagiri (Madhya Pradesh)**; **Deogarh (Uttar Pradesh)**: Dashavatara temple; **Ahichchhatra (western Uttar Pradesh)**: terracotta Ganga and Yamuna; **Ramagiri/Ramtek (Maharashtra)**: Prabhavati's temples; **Nalanda**; **Socotra Island (Arabian Sea)**."]),
 ("h2", "8.14 Reading the Sources"),
 ("table", ["Source", "What we learn"], [
  ["Prayaga Prashasti (Harisena)", "Samudragupta's conquests, aim to unify the Earth, patronage of art, learning and trade"],
  ["Iron Pillar inscription", "King 'Chandra' (Chandragupta II); a Vishnu dedication; metallurgy"],
  ["Gupta coins", "Chandragupta I and Kumaradevi; veena player; ashvamedha horse; goddess Lakshmi"],
  ["Vishnu Purana", "Core regions: Anuganga, Prayaga, Saketa, Magadha"],
  ["Faxian's Record of Buddhistic Kingdoms", "Prosperous cities, charity, light taxation; also harsh treatment of chandalas"],
  ["Copper plates", "Land grants and tax records"],
  ["Socotra finds", "Pottery, Brahmi inscriptions and a stupa design of Indian traders"],
  ["Aryabhatiya, Brihat Samhita, Meghadutam", "Science, encyclopedic knowledge and poetry of the age"]]),
 ("h2", "8.15 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Kushana weakness in the 3rd century CE", "New kingdoms; rise of the Guptas"],
  ["Military conquests, alliances and tributary kings", "A large empire from limited direct control"],
  ["Long peace and a strong economy", "Support to scholars, artists and scientists; the 'classical age'"],
  ["Trade with the Mediterranean, Southeast Asia and China", "Revenue; cultural exchange (e.g. Socotra)"],
  ["Repeated Huna invasions and regional rulers", "Decline of the Guptas by the 6th century CE"]]),
 ("h2", "8.16 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Describe the achievements of Samudragupta. (3 marks)", "The Prayaga Prashasti by Harisena calls him a king who wanted to unify the Earth. He defeated many kings; some were reinstated as tributaries. He supported art, learning and trade and is shown on a coin playing the veena. He defeated a Pallava ruler and the Kamarupa ruler but let them rule as tributaries."),
  ("Describe the scientific and literary achievements of the Gupta Age. (5 marks)", "Aryabhata wrote the Aryabhatiya, said the Earth spins on its axis, gave an almost correct year length and correctly explained eclipses. Varahamihira's Brihat Samhita covered astronomy, weather, architecture, town planning and farming. Kalidasa wrote Meghadutam and Raghuvamsham. The Charaka and Sushruta Samhitas were given their final form. Metallurgy is shown by the Iron Pillar. Many Puranas were also written. Peace and royal patronage made this possible, hence the 'classical age'."),
  ("How did the Guptas rule such a large empire? (5 marks)", "They used military conquest, diplomacy and matrimonial alliances, as with Prabhavati Gupta. They took new titles like maharajadhiraja. They divided the empire into provinces and made land grants to local rulers, priests and chieftains, recorded on copper plates, so that taxes were collected and local control was kept. Defeated kings often stayed as tributaries. Land tax and trade gave revenue for the army, temples and scholars."),
  ("Why should we be careful while using Faxian's account? (3 marks)", "It reflects only the writer's viewpoint, at one point in time, about part of society. He praises the prosperity and charity of the cities but also describes harsh treatment of the chandalas. Historians need to compare many sources before they draw conclusions."),
 ]),
]
CH["takeaways"] += ["Use the right chronology: Kushana decline (3rd c.), Faxian (early 5th c., AD 399-414), Aryabhata (about 500 CE), Hunas (6th c.).",
  "Always name capitals: **Pataliputra** (Guptas), **Nandivardhana** (Vakatakas), **Kanchipuram** (Pallavas)."]

if __name__ == "__main__": run(__file__, BANK, 7, "Social_Science", WS, CH)
