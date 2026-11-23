"""Class 7 Social Science Ch 5 - Cities and States: The Second Urbanisation: worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c7sst_ch05"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("The 'Second Urbanisation' of India began in the:", ["early 2nd millennium BCE", "1st millennium BCE", "1st century CE", "5th century CE"], 1, "In the Ganga plains."),
mc("The word 'janapada' means:", ["a royal court", "where the people have set foot (settled)", "a trading guild", "a fort"], 1),
mc("The capital of Magadha was:", ["Shravasti", "Rajagriha", "Ujjayini", "Kaushambi"], 1),
mc("Which of these was an early republic (gana-sangha)?", ["Magadha", "Kosala", "Vrijji", "Avanti"], 2),
mc("The first Indian coins were made of:", ["gold", "copper", "silver", "iron"], 2, "Punch-marked silver coins."),
mc("The word 'caste' comes from the Portuguese word:", ["casta", "varna", "jati", "kasta"], 0),
mc("Which of these was NOT one of the three early southern kingdoms named in ancient Tamil literature?", ["Chola", "Chera", "Pandya", "Maurya"], 3),
W("Name any four of the sixteen mahajanapadas.", 2,
  "Any four of Magadha, Kosala, Vatsa, Avanti, Gandhara, Vrijji, Malla, Anga, Kuru, Panchala, Shurasena, Matsya, Chedi, Kamboja, Ashmaka. (4 = 2, 2-3 = 1)", "E"),
W("Match the mahajanapada and its capital: (i) Kosala (ii) Avanti (iii) Vatsa (iv) Gandhara.  A. Ujjayini  B. Takshashila  C. Shravasti  D. Kaushambi.", 2,
  "(i)-C, (ii)-A, (iii)-D, (iv)-B. (4 right = 2, 2-3 = 1)", "E"),
W("What were sabha and samiti?", 2,
  "Assemblies of elders in a janapada, mentioned in the Vedas (1), who advised the raja (1).", "E"),
W("True or false, with reason: 'After the Harappan cities declined, Indian cities continued without a break.'", 2,
  "False (1). Urban life almost disappeared for about a thousand years and people returned to village life, until the Second Urbanisation (1).", "E"),
W("Name two sources from which historians know about the Second Urbanisation.", 2,
  "Archaeological excavations of ancient urban centres (1) and literature such as late Vedic, Buddhist and Jain texts (1).", "E"),
W("State two advantages of iron over copper and bronze for farmers and armies.", 2,
  "Iron tools helped farm on a bigger scale (1); iron weapons were lighter and sharper, strengthening armies (1).", "E"),
W("What were punch-marked coins and why were they needed?", 2,
  "Silver coins punched with symbols (1), needed because growing trade required a common medium of exchange (1).", "E"),
W("Name the four varnas and the traditional role of any one.", 2,
  "Brahmins, Kshatriyas, Vaishyas, Shudras (1). e.g. Kshatriyas defended society and land (1).", "E"),
W("Rohan's father says 'Mahajanapadas such as Magadha rose in the Ganga plains because of fertile land.' Give two more reasons.", 2,
  "Iron ore in nearby hills (1) and new trade networks (1).", "E", wp=True),
W("Fill in the blanks: A moat is a deep ______-filled ditch outside the ______ of a fort.", 2,
  "water; ramparts/walls (1+1).", "E"),
# ------------------------------------------------------------------ MEDIUM (19)
W("What happened to Harappan urban life, and what was lost?", 3,
  "The Harappan civilisation declined in the early 2nd millennium BCE (1). Planned cities, markets, specialised crafts, writing, sanitation and administration vanished (1); people reverted to village life (1).", "M"),
W("Describe the defence of a mahajanapada capital.", 3,
  "The city was fortified with rampart walls (1), a water-filled moat outside the walls (1) and narrow gateways so guards could control the movement of people and goods (1).", "M"),
W("Differentiate between a monarchy and a gana-sangha in two ways (decision-making and ruler).", 3,
  "Monarchy: the raja was the ultimate authority, hereditary (1.5). Gana-sangha: the assembly held more power, took decisions by discussion and vote, and the ruler was selected (1.5).", "M"),
W("Why are Vrijji and Malla called early republics?", 2,
  "They were ruled by assemblies, not hereditary kings (1), where decisions were by discussion or vote; they were among the earliest republics in the world (1).", "M"),
W("Source-based. 'Janapada: where the people (jana) have set foot (pada). By the 8th-7th centuries BCE some janapadas merged into larger states called mahajanapadas, usually listed as sixteen from Gandhara to Anga and Ashmaka.'  (i) What does 'pada' mean here? (ii) Which was the north-west mahajanapada? (iii) Which was in central India near the Godavari?", 3,
  "(i) Foot (1). (ii) Gandhara (1). (iii) Ashmaka (1).", "M"),
W("Map description: Using a map of ancient India, say where you would place (i) Gandhara (ii) Magadha (iii) Avanti (iv) Anga.", 3,
  "(i) North-west (ii) South Bihar, east of Kosala (iii) Central India (Malwa, Ujjain region) (iv) East, beyond Magadha. (4 right = 3, 3 right = 2, 2 right = 1)", "M"),
W("Why were so many mahajanapadas located in the Ganga plains?", 3,
  "Fertile land supported farming (1); iron ore in nearby hills (1); river trade networks (1).", "M"),
W("Cause and effect: How did iron lead to the rise of larger states and warfare?", 3,
  "Iron tools increased farm output and surplus (1); a food surplus supported cities, rulers and armies (1); iron weapons made armies stronger, leading to wars and alliances that built kingdoms and empires (1).", "M"),
W("List three duties of a king in a mahajanapada.", 3,
  "Collect taxes or revenue; keep law and order; build fortifications; maintain an army to defend or fight (any three, 1 each).", "M"),
W("Explain jati and varna in two lines each.", 3,
  "Varna: a Vedic-text concept of four classes - Brahmins, Kshatriyas, Vaishyas, Shudras (1.5). Jati: community defined by a specific occupation with skills passed down generations, with sub-jatis having their own customs (1.5).", "M"),
W("How did the varna-jati system provide stability, and how did it later cause problems?", 3,
  "Early on people could change occupations and groups complemented one another, giving stability (1.5). Later it became rigid and led to inequality and discrimination against lower jatis and those outside the system (1.5).", "M"),
W("Describe Shishupalgarh as a city.", 3,
  "Capital of Kalinga near Bhubaneswar, Odisha (1); strict square plan with fortifications (1); moat, narrow gateways and broad streets (1).", "M"),
W("Why were Uttarapatha and Dakshinapatha important?", 2,
  "They were major routes of trade, pilgrimage and armies (1) linking the north-west and Ganga plains with the south through the Vindhyas via Kaushambi, helping regions to connect (1).", "M"),
W("Give two features of cities in south India from about 400 BCE, with one example.", 3,
  "Cities arose with kingdoms of the Cholas, Cheras and Pandyas (1); rich in gems, gold and spices and traded overseas (1). Example: Kodumanal near Erode with shell and gemstone industries (1).", "M"),
W("Match the item with the period: (i) iron tools widespread (ii) punch-marked coins (iii) Harappan cities (iv) mahajanapadas.  A. 1st millennium BCE  B. early 2nd millennium BCE  C. late 2nd millennium BCE  D. about 8th-7th centuries BCE.", 3,
  "(i)-C (ii)-A (iii)-B (iv)-D. (4 right = 3, 3 right = 2, 2 right = 1)", "M"),
W("Error analysis: 'The Vrijjis were a hereditary monarchy ruled by a king chosen by his son.' Correct the statement.", 2,
  "Vrijji was a gana-sangha, an early republic (1); decisions were by assembly discussion and vote, and rulers were selected, not hereditary (1).", "M"),
W("Magadha was among the most powerful mahajanapadas. Name two features of its Ganga-plains setting that helped states grow.", 2,
  "Fertile land that supported farming and iron ore in the nearby hills (1); new trade networks (1).", "M"),
W("Why do Kautilya's Arthashastra descriptions of the ideal kingdom matter for understanding cities and states?", 2,
  "They describe a fortified capital, fertile land, mines, forests, pastures, rivers and good roads (1), the same features seen in the early states (1).", "M"),
W("What changes did the Second Urbanisation bring about in everyday life? Give three.", 3,
  "Markets and trade expanded with coins (1); new crafts and tools of iron (1); new ideas spread by Buddhist, Jain and late Vedic scholars and monastic centres (1).", "M"),
# ------------------------------------------------------------------ HARD (14)
W("Compare the First and Second Urbanisations on region, metal and money.", 4,
  "Region: Indus-Sarasvati valleys vs Ganga plains spreading widely (1.5). Metal: copper and bronze vs iron (1). Money: no coins vs punch-marked silver coins (1.5).", "H"),
W("Case study: A village on a river near a hill with iron ore is growing into a town with a market, a fort and a mint. (i) Name the period. (ii) List three factors helping its growth. (iii) What would its ruler need to ensure?", 5,
  "(i) Second Urbanisation (mahajanapada period) (1). (ii) Fertile land, iron ore, trade routes/river (any three, 3). (iii) Taxes, law and order, defence with fort and army (1).", "H", wp=True),
W("'Wars and alliances between mahajanapadas finally led to empires.' Explain with reference to Magadha and the end of the period.", 4,
  "With iron weapons and larger armies mahajanapadas fought one another (1.5). Stronger states like Magadha absorbed others (1.5). By about 300-200 BCE the mahajanapadas ended and gave way to empires (1).", "H"),
W("Evaluate: 'The varna-jati system was flexible at first and rigid later.' Give two examples of each and one effect today.", 5,
  "Flexible: people changed occupation in a drought; some Brahmins took to trade or military work (2). Rigid: hardened over time and under British rule; discrimination against lower jatis and groups outside (2). Effect: inequality remains a challenge, so equal respect is needed (1).", "H"),
W("A trader's journey runs Kaushambi - Ujjayini - Pratishthana. (i) Which route is it? (ii) Name two goods he may carry. (iii) Why would he want to join pilgrims?", 4,
  "(i) Dakshinapatha (1). (ii) Any two: shells, pearls, gold, diamonds, cotton, spices, sandalwood (1). (iii) Pilgrim routes and trade routes overlap; he gets customers and company for the journey (2).", "H", wp=True),
W("How did the use of punch-marked coins change trade? Explain the advantages over barter in three points.", 3,
  "Coins are a common measure of value (1); they are easy to carry and store (1); they allowed trade across regions and abroad, since coins circulated widely (1).", "H"),
W("Describe how decisions might have been made in a gana-sangha like Vrijji. Is this like a modern democracy? Give one similarity and one difference.", 4,
  "Assembly members discussed and voted if needed (1.5). Similarity: decisions by discussion and vote (1). Difference: a modern democracy gives every adult citizen a vote, while the gana assemblies were mainly of elders and leading members (the evidence is limited) (1.5).", "H"),
W("Why is the evidence for the removal of an incompetent king in the mahajanapadas described as incomplete?", 3,
  "Texts suggest a poor king might be removed (1), but the evidence is incomplete and not settled law, so we cannot be sure it was normal practice (2).", "H"),
W("Draw a timeline in words for Harappan civilisation, janapadas, mahajanapadas, iron use, Second Urbanisation and end of mahajanapadas, with approximate dates.", 4,
  "Harappan about 1900 BCE; early 2nd millennium BCE decline; about 1200 BCE janapadas; late 2nd millennium BCE iron tools; 8th-7th centuries BCE mahajanapadas; 1st millennium BCE Second Urbanisation; about 300-200 BCE end of mahajanapadas, empires begin (4 points correct in order = 4).", "H"),
W("'Modern cities are also the result of the Second Urbanisation.' Explain what this means and what is similar between ancient and modern cities.", 3,
  "The Second Urbanisation began in the 1st millennium BCE and, in a way, continues today (1). Similar: trade, markets, administration, mixed communities, sacred and learning centres (2).", "H"),
W("Why did the capital cities need narrow gateways and moats? Give two security and one economic reason.", 3,
  "Security: slows attackers; guards control entry and exit (2). Economic: guards can check and tax goods (1).", "H"),
W("Compare the four most powerful mahajanapadas on location and capital in a table-like answer.", 4,
  "Magadha - Bihar - Rajagriha; Kosala - Uttar Pradesh - Shravasti; Vatsa - near Prayagraj, Uttar Pradesh - Kaushambi; Avanti - Madhya Pradesh - Ujjayini (4 x 1).", "H"),
W("Puzzle: Identify. (i) 'My ruins at modern Rajgir in Bihar mark a capital of Magadha.' (ii) 'My name is Portuguese for lineage.' (iii) 'I was the capital of Kalinga, excavated from 1948.' (iv) 'I am the Vedic assembly of elders.'", 3,
  "(i) Rajagriha (ii) Caste (casta) (iii) Shishupalgarh (iv) Sabha / samiti. (4 right = 3, 3 right = 2, 2 right = 1)", "H"),
]

_old = runpy.run_path(str(REPO / "src/rn_work/c7_sst/c05.py"))["CH"]
_i = max(k for k, b in enumerate(_old["blocks"]) if b[0] == "h2")
_core = _old["blocks"][:_i]
def _fix(blocks):
    out = []
    for b in blocks:
        if b[0] == "table":
            rows = []
            for row in b[2]:
                if row[0] == "Money":
                    row = [row[0], "No coins (seals used in trade)", row[2]]
                if row[0] == "Monasteries and warfare":
                    row = [row[0], "Not part of the NCERT comparison", row[2]]
                rows.append(row)
            b = (b[0], b[1], rows)
        out.append(b)
    return out
_core = _fix(_core)
_extra = [
 ("h2", "5.8 Timeline"),
 ("table", ["Period", "Event"], [
  ["About 1900 BCE", "Harappan (First Urbanisation) at its height; decline in the early 2nd millennium BCE"],
  ["About 1000 years", "Almost no urban life in India after the Harappan decline"],
  ["About 1200 BCE", "Janapadas: clans linked to territories"],
  ["Late 2nd millennium BCE", "Iron tools become widespread"],
  ["8th-7th centuries BCE", "Mahajanapadas (16) emerge"],
  ["1st millennium BCE", "Second Urbanisation in the Ganga plains; punch-marked silver coins"],
  ["About 400 BCE", "Cities appear in South India; Cholas, Cheras, Pandyas"],
  ["About 300-200 BCE", "Whole Subcontinent interlinked; mahajanapadas end and empires begin"]]),
 ("h2", "5.9 Key Terms and People"),
 ("table", ["Term", "Meaning"], [
  ["Urbanisation", "Growth of cities and city life"],
  ["Janapada / mahajanapada", "Territory settled by a clan / large state formed by merger"],
  ["Raja", "The ruler of a janapada"],
  ["Sabha / samiti", "Assemblies of elders advising the raja"],
  ["Gana / sangha", "Assembly-based republic such as Vrijji and Malla"],
  ["Rampart / moat", "Fort wall / water-filled ditch around it"],
  ["Punch-marked coin", "India's earliest silver coins with punched symbols"],
  ["Varna / jati", "Four Vedic classes / occupation-based communities"],
  ["Caste", "From Portuguese casta; used for varna, jati or the whole system"],
  ["Uttarapatha / Dakshinapatha", "Northern and southern trade-pilgrim routes"],
  ["Kautilya", "Author of the Arthashastra, describes an ideal kingdom"]]),
 ("h2", "5.10 Map Pointers"),
 ("ul", ["Mark the 16 mahajanapadas, especially **Magadha, Kosala, Vatsa, Avanti, Gandhara, Vrijji, Malla, Anga, Ashmaka**.",
  "Mark capitals: **Rajagriha, Shravasti, Kaushambi, Ujjayini, Takshashila, Vaishali, Champa**.",
  "Trace **Uttarapatha** and **Dakshinapatha**, the **Vindhyas**, and mark **Shishupalgarh** (near Bhubaneswar) and **Kodumanal** (near Erode).",
  "Shade the **Ganga plains**, where iron ore, fertile soil and trade combined."]),
 ("h2", "5.11 Cause and Effect Chains"),
 ("table", ["Cause", "Effect"], [
  ["Iron tools", "Bigger farm surplus and stronger weapons"],
  ["Surplus and trade", "Cities, markets, coins"],
  ["Rivalry among mahajanapadas", "Wars, alliances, later empires"],
  ["Growing trade", "Need for punch-marked coins"],
  ["Complex societies", "Occupation groups; varna-jati; later inequality"]]),
 ("h2", "5.12 Case and Source Notes"),
 ("ul", ["**Case: Shishupalgarh.** Square plan, fortification, moat and broad streets show planning in a Kalinga capital.",
  "**Case: Vrijji.** Assembly decisions and selected leaders show early republican ideas.",
  "**Case: Kodumanal.** Shell and gemstone industries show crafts and trade in south India.",
  "**Source skills:** identify what the source is (excavation or text), what it tells (city, trade, society) and what it cannot tell."]),
 ("h2", "5.13 Common Mistakes"),
 ("note", "REMEMBER", "**Janapada** is smaller; **mahajanapada** is the large state. **Magadha, Kosala, Vatsa, Avanti** were the most powerful. **Vrijji and Malla** were ganas, not monarchies."),
 ("note", "REMEMBER", "The **first coins** were silver punch-marked. Iron was perfected from the early 2nd millennium BCE but widespread by the late 2nd millennium BCE."),
 ("h2", "5.14 Likely 3 and 5 Mark Answers"),
 ("qa", [("Explain the Second Urbanisation and the factors that caused it. (5)", "A new phase of city growth in the 1st millennium BCE in the Ganga plains after a thousand years of almost no cities. Factors: fertile land, iron tools and ore, trade routes, coins, rulers who built fortified capitals, and new ideas."),
  ("How did gana-sangha differ from monarchy? (3)", "Monarchy: hereditary raja, final authority, advised by elders and ministers. Gana-sangha: assembly decisions by discussion or vote, selected leaders; Vrijji and Malla."),
  ("Why were iron and coins important? (3)", "Iron expanded agriculture and strengthened armies; coins made trade easier and spread across regions."),
  ("Explain varna and jati. (3)", "Varna: four classes from Vedic texts. Jati: occupation-based communities with inherited skills and sub-jatis. Early flexibility, later rigidity.")]),
]
CH = dict(num=5, title="Cities and States: The Second Urbanisation", tag=_old["tag"], intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_core + _extra, takeaways=_old["takeaways"])

if __name__ == "__main__": run(__file__, BANK, 7, "Social_Science", WS, CH)
