"""Class 6 Social Science Ch 11 - Grassroots Democracy Part 2: Local Government in Rural Areas: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6sst_ch11"

def _base():
    s = importlib.util.spec_from_file_location("c6sst_c11", str(REPO / "src/rn_work/c6_sst/c11.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The local government of a village in India is called the:", 1, "(b) Panchayat", "E", opts=["Municipality", "Panchayat", "High Court", "Cabinet"]),
W("The head of a Gram Panchayat is called the:", 1, "(a) Sarpanch", "E", opts=["Sarpanch", "Patwari", "Governor", "Collector"]),
W("The lowest tier of the Panchayati Raj system is the:", 1, "(c) Gram Panchayat", "E", opts=["Zila Parishad", "Panchayat Samiti", "Gram Panchayat", "Lok Sabha"]),
W("The Panchayat Samiti works at which level?", 1, "(d) block", "E", opts=["village", "district", "State", "block"]),
W("The Zila Parishad works at the ______ level.", 1, "(b) district", "E", opts=["village", "district", "block", "national"]),
W("The officer who keeps the village land records is the:", 1, "(a) Patwari", "E", opts=["Patwari", "Panchayat Secretary", "Sarpanch", "Judge"]),
W("What fraction of seats in the Panchayati Raj institutions is reserved for women?", 1, "(c) one-third", "E", opts=["one-tenth", "one-fourth", "one-third", "one-half"]),
W("Who wrote the Arthaśhāstra?", 1, "(d) Kauṭilya (Chāṇakya)", "E", opts=["Vincent Smith", "Tagore", "Tiruvalluvar", "Kauṭilya (Chāṇakya)"]),
W("Fill in the blank: The Gram Sabha is a group of adult ______ of a village.", 1, "voters (enrolled as voters). (1)", "E"),
W("Write True or False: The Panchayati Raj is a system of self-government.", 1, "True. It lets villagers manage local matters themselves. (1)", "E"),
W("Write True or False: A Gram Panchayat is elected by the people of the district.", 1, "False. Its members are elected directly by the Gram Sabha, that is, people of the village. (1)", "E"),
W("Name the three tiers of the Panchayati Raj system, from bottom to top.", 2, "Gram Panchayat (village), Panchayat Samiti (block), Zila Parishad (district). (2)", "E"),
W("About how many villages does India have, according to the chapter?", 1, "About 600,000 villages. (1)", "E"),
W("Whose saying is 'The real India lives in its villages'?", 1, "M.K. Gandhi. (1)", "E"),
W("What do Bal Sabhas and Bal Panchayats give to children?", 2, "They give children an opportunity to express their ideas and opinions on matters affecting their wellbeing. (2)", "E"),
W("Name two matters on which the people of Lakshmanpur village need decisions.", 2, "Any two: water for the fields, repair of the main road, upkeep of the primary school, land disputes, theft of crops. (1+1)", "E"),
W("Which scheme is named in the chapter for building all-weather roads in rural areas?", 1, "Pradhan Mantri Gram Sadak Yojana. (1)", "E"),
W("Who helps the Gram Panchayat with administration such as calling meetings and maintaining records?", 1, "The Panchayat Secretary. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Why can't the people of a village run to the State or the national capital for every problem? How does the Panchayat solve this?", 3, "India is huge with about 600,000 villages, and each has small daily problems like water, roads, school or disputes (1). It is not practical to go to the capital (1). The Panchayat brings governance close to the people so they can solve local matters themselves (1).", "M", wp=True),
W("Lakshmanpur has 200 houses and about 700 people. Which of the following can its Gram Panchayat decide: (i) repair of the village road (ii) the country's currency (iii) maintenance of the primary school? Give a reason.", 3, "(i) and (iii) (1 each). They are local matters. The currency is a national matter decided by the Central government (1).", "M", wp=True),
W("Explain what the Gram Sabha is and what it does.", 3, "It is a group of adults of a village (or neighbouring villages) enrolled as voters (1). Women and men discuss all matters of their area and take decisions (1). It elects the members of the Gram Panchayat (1).", "M"),
W("Write the duties of the Panchayat Secretary and the Patwari.", 2, "The Panchayat Secretary does administrative work like calling meetings and keeping records (1). The Patwari maintains the villagers' land records (1).", "M"),
W("Why can the old maps kept by a Patwari be useful to us?", 2, "They show how land was used and divided in the past, so they help to compare with the present and settle land disputes. (2)", "M"),
W("Which Sarpanch is described as the first female Sarpanch of her village? Which community does she belong to, and what did she do?", 3, "Vandana Bahadur Maida of Khankhandvi, Madhya Pradesh (1). She belongs to the Bhil community (1). She convinced women to attend Sabha meetings and worked on education and sanitation (1).", "M"),
W("What was the motto of Dnyaneshwar Kamble and what does it mean?", 2, "Lok seva, gram seva: service to the village is service to the public. (2)", "M"),
W("How did Popatrao Pawar change Hiware Bazar? Give three steps.", 3, "He used Anna Hazare's model of rainwater harvesting (1), watershed conservation (1) and planting lakhs of trees, which recharged groundwater and made the village green and prosperous (1).", "M"),
W("In what year was Popatrao Pawar awarded the Padma Shri, and for which village's change?", 2, "In 2020, for the transformation of Hiware Bazar in Ahmednagar district, Maharashtra. (2)", "M"),
W("What did the Bal Panchayats of Maharashtra do?", 2, "They worked to eliminate child labour and child marriage, and brought many children back to school by convincing parents and elders. (2)", "M"),
W("What was done by the Sangkhu Radhu Khandu Gram Panchayat in Sikkim for children?", 3, "It built compound walls for schools to make them safer (1) and built kitchens in the schools so that midday meals are cooked hygienically (1). Therefore it was declared child-friendly (1).", "M"),
W("Describe the Children's Parliament of Rajasthan in three points.", 3, "It grew out of Bunker Roy's Barefoot College (1). Children aged 8 to 14 learned democracy through night schools and parliament-like elections with voter ID cards and campaigning (1). The elected representatives formed a 'Cabinet' that oversaw school management and community needs (1).", "M"),
W("What is the role of a Panchayat Samiti?", 2, "It is the link between the Gram Panchayat and the Zila Parishad. It coordinates matters across Gram Panchayats, for example by collecting their development plans and presenting them at higher levels. (2)", "M"),
W("Find the mistake: \"The Zila Parishad is the lowest tier and the Gram Panchayat is the highest.\"", 2, "It is the other way round. The Gram Panchayat is the lowest tier at the village level; the Zila Parishad is the highest at the district level. (2)", "M"),
W("Why are one-third of seats reserved for women and special rules made for disadvantaged sections?", 2, "So that women and disadvantaged groups can make their needs and problems heard and take part in decisions. (2)", "M"),
W("Why do the names and the structure of Panchayati Raj institutions differ a little in different States?", 2, "States have the authority over these institutions, so names and structure differ a little, but the objective is the same: to let villagers take an active part in managing their villages. (2)", "M"),
W("Match: (a) Sarpanch (b) Patwari (c) Panchayat Secretary with (1) keeps land records (2) calls meetings (3) head of Gram Panchayat.", 3, "(a) with (3), (b) with (1), (c) with (2). (1 each)", "M"),
W("What was the work of Vandana Maida in encouraging women, and why was it important in a village with patriarchal norms?", 3, "She convinced women of the village to attend the Sabha meetings (1). She raised issues like education and sanitation (1). Her work shows that women can lead and bring change in rural India even when old norms stop them (1).", "M"),
# ---------------- HARD ----------------
W("Case study: A village school sits next to a highway and the children find it unsafe to cross. Which institutions of Panchayati Raj can help? Suggest what the students can do.", 4, "The students can write to or meet the Sarpanch and ask the Gram Sabha to discuss the problem (1). The Gram Panchayat can ask the Panchayat Samiti, which collects plans and requests funds (1). The Zila Parishad can help present it to the district and State authorities for a speed breaker, zebra crossing or footbridge (1). Students can also get a Bal Sabha to raise it and a letter or petition signed by many children (1).", "H", wp=True),
W("Write a short letter (4 to 5 lines) to the Sarpanch about plastic bags lying on the roadside.", 4, "Format: place and date (1), address 'Respected Sarpanch ji' (1), body: tells the problem, its harm to cows, drains and the village, and requests collection, bins and awareness (1), closing and name (1).", "H", wp=True),
W("Case study: Kavita, an elected member of her village Panchayat, hears from women that the village has no clean toilets for girls in school. What steps can she take through the Panchayati Raj system?", 4, "Raise the matter in the Gram Sabha and the Gram Panchayat (1). Ask the Panchayat Secretary to prepare a proposal and list it in the village development plan (1). The Panchayat Samiti can put it together with other villages' plans and ask for funds (1). She can involve women and children, as Vandana Maida did for sanitation (1).", "H", wp=True),
W("Compare the working of the government at the Central level and at the Panchayat level. Give two similarities and one difference.", 3, "Similarity: both have elected people who take decisions for others (1), and both work at several levels / tiers (1). Difference: the Central government is for the whole country (big matters like defence), while the Panchayat is for local matters like village roads and water (1). (Any sensible points are accepted.)", "H"),
W("Explain how democracy in the Panchayati Raj works both through direct participation and through elected representatives.", 3, "Direct: all adult voters of a village take part in the Gram Sabha and discuss and decide matters (1.5). Representative: they elect members of the Gram Panchayat, and the higher tiers have elected members as well (1.5).", "H"),
W("Why is the Panchayati Raj called 'self-government'? Give two reasons.", 3, "Villagers manage their own local affairs through people they elect (1.5). It reduces dependence on the distant government, and the people can take an active part in decisions and development (1.5).", "H"),
W("Kauṭilya wrote that the king should set up a sangrahaṇa for every 10 villages, a kārvaṭika for 100, a droṇamukha for 400 and a sthānīya for 800 villages. What does this passage show about administration in ancient India, and why does the chapter call it amazing?", 4, "It shows a layered structure of administration from the village upwards: sub-district headquarters for 10 villages, district headquarters for 100 villages, and provincial headquarters for 800 villages. (2) The chapter finds it amazing that a structure with several levels, similar in idea to our local, district and State levels today, was thought of some 2,300 years ago. (2)", "H"),W("Read the quote: 'The real India lives in its villages.' Using the chapter, give three facts that support this idea.", 3, "India has about 600,000 villages against 8,000 towns and over 4,000 cities (1). Almost two-thirds of the 1.4 billion people live in rural areas (1). Villages are where farming, water and local governance take place, so strong Panchayats matter (1).", "H"),
W("Explain how the Child-Friendly Panchayat Initiative is a good idea. Give two benefits and two examples.", 4, "Benefits: children's voices and rights are heard (1) and children learn leadership and democracy early (1). Examples: Bal Panchayats in Maharashtra stopped child labour and child marriage (1); the Sikkim Gram Panchayat built safer school walls and clean kitchens (1).", "H"),
W("Do you think the Children's Parliament is a good model for schools in your area? Give your view with two reasons based on the chapter.", 3, "Yes (or reasoned no). Children aged 8 to 14 learned democracy by practising it with elections and voter IDs (1.5). It built leadership, social awareness and let them tackle education, sanitation and equality, and won the World's Children's Honorary Award in 2001 (1.5).", "H"),
W("Which problems of Lakshmanpur village will be dealt with at (i) the village level (ii) the block level? Explain with one example each.", 3, "(i) Local needs such as repairing a damaged village road or school maintenance, discussed in the Gram Sabha (1.5). (ii) Matters involving several villages, like putting together development plans for a road scheme such as Pradhan Mantri Gram Sadak Yojana (1.5).", "H", wp=True),
W("What type of person should be a Gram Panchayat member? List four qualities with a reason for each.", 4, "(1 each) Honest (to use funds properly), helpful and caring (to serve people), good listener (to hear all voices including women and children), hard working and knowledgeable (to solve problems). Any four sensible qualities with reasons.", "H"),
W("Why is it important to give more attention to the disadvantaged sections of society in the panchayats?", 3, "Disadvantaged people have fewer resources and are often not heard (1). Special rules and reserved seats give them a voice in decisions (1). This makes development fair and benefits reach everyone (1).", "H"),
]

CH = _base()
def _fix(x):
    if isinstance(x, str):
        return x.replace(" — comparable to our block, district and province structure.", ". The chapter asks what names we would give these four categories today.")
    if isinstance(x, (list, tuple)):
        return type(x)(_fix(i) for i in x)
    return x
CH["blocks"] = _fix(CH["blocks"])
CH["blocks"] += [
 ("h2", "11.7 Time and Number Pointers"),
 ("table", ["Number / date", "Fact"], [
  ["About 2,300 years ago", "Kauṭilya wrote the Arthaśhāstra describing administration from village to provincial capital"],
  ["About 600,000 / 8,000 / over 4,000", "Villages / towns / cities in India"],
  ["More than 1.4 billion; almost two-thirds rural", "Population of India"],
  ["200 houses, about 700 people", "The village of Lakshmanpur"],
  ["2001", "Children's Parliament received the World's Children's Honorary Award"],
  ["2017", "Dnyaneshwar Kamble elected Sarpanch of Tarangfal"],
  ["2020", "Popatrao Pawar awarded the Padma Shri"],
  ["One-third", "Seats reserved for women at all three tiers"],
  ["Ages 8 to 14", "Children in the Children's Parliament"]]),
 ("h2", "11.8 Key Terms and People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Panchayat**", "Village council; local government in villages"],
  ["**Panchayati Raj**", "System of rural self-government in three tiers"],
  ["**Gram Sabha**", "Group of adult voters of a village that discusses matters and elects the Gram Panchayat"],
  ["**Sarpanch / Pradhan**", "Head of the Gram Panchayat"],
  ["**Panchayat Secretary**", "Does administrative work: meetings and records"],
  ["**Patwari**", "Keeps land records and old maps"],
  ["**Bal Sabha / Bal Panchayat**", "Platforms for children to speak on matters concerning them"],
  ["**Barefoot College (Bunker Roy)**", "Initiative from which the Children's Parliament grew"],
  ["**Kauṭilya (Chāṇakya)**", "Author of the Arthaśhāstra"],
  ["**Anna Hazare**", "Source of the model of rainwater harvesting and watershed conservation used at Hiware Bazar"]]),
 ("h2", "11.9 Map Pointers"),
 ("ul", ["**Lakshmanpur** — imagined village in the foothills of the Himalayas.",
  "**Tarangfal (Solapur) and Hiware Bazar (Ahmednagar)** — Maharashtra; **Khankhandvi** — Madhya Pradesh; **Sangkhu Radhu Khandu** — west Sikkim; **Children's Parliament** — Rajasthan.",
  "Locate these States on the political map of India and write the Sarpanch or initiative at each."]),
 ("h2", "11.10 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Too many villages and issues for capital-level governance", "Panchayati Raj system: local self-government"],
  ["Frequent droughts in Hiware Bazar", "Sarpanch Pawar's rainwater harvesting and tree planting made it green"],
  ["Child labour and child marriage", "Bal Panchayats brought children back to school"],
  ["Different States' authority over panchayats", "Names and structure vary slightly, objectives the same"],
  ["Need for voice of disadvantaged groups", "Special rules and one-third reservation for women"]]),
 ("note", "IMPORTANT", "The three tiers go **from bottom up: village (Gram Panchayat), block (Panchayat Samiti), district (Zila Parishad)**. Answer 'who elects whom' with the Gram Sabha at the base."),
 ("h2", "11.11 Rural and Central Government: Think and Compare"),
 ("ul", ["**Similarities:** both have elected representatives; both work at more than one level; both aim to serve people; both make decisions through discussion.",
  "**Differences:** the Central government looks after the whole country (defence, currency and so on), while the Panchayat looks after local needs such as village roads, water and school upkeep. In the Gram Sabha, villagers can take part directly, because they all know each other.",
  "A good Gram Panchayat member should be honest, helpful, a good listener and ready to work for all, including women, children and the disadvantaged."]),
 ("note", "REMEMBER", "For letter-writing questions (for example about plastic bags on the roadside) write: place and date, address to the Sarpanch, subject, the problem, your request, and your name."),
 ("h2", "11.12 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Describe the three-tier Panchayati Raj system. (5 marks)", "The system works at the village, block and district levels. At the village is the Gram Panchayat, elected by the Gram Sabha and headed by the Sarpanch. At the block level the Panchayat Samiti is the link between Gram Panchayat and Zila Parishad and coordinates development plans. At the district level the Zila Parishad coordinates and presents the plans. They cover agriculture, roads, water, education, health and welfare, and keep one-third seats for women."),
  ("Write a short note on any two exemplary Sarpanchs. (3 marks)", "Vandana Bahadur Maida of Khankhandvi, Madhya Pradesh, was the first female Sarpanch of her village. She brought women to the Sabha and worked on education and sanitation. Popatrao Pawar of Hiware Bazar used rainwater harvesting and tree planting to make the village green; he got the Padma Shri in 2020."),
  ("Why are Panchayats important in governance and democracy? (3 marks)", "They bring governance close to the people, help them take part in decisions, address local issues, promote development and ensure that government schemes reach the grassroots."),
 ]),
]
CH["takeaways"] += ["Three tiers: **Gram Panchayat - Panchayat Samiti - Zila Parishad**; the **Gram Sabha** elects the Gram Panchayat.",
  "Learn the example Sarpanchs: **Kamble, Maida, Pawar**, and child-friendly examples from Maharashtra, Sikkim and Rajasthan."]

if __name__ == "__main__": run(__file__, BANK, 6, "Social_Science", WS, CH)
