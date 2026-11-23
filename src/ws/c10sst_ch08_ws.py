"""Class 10 Social Science Ch 8 - Water Resources (Geography): worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c10sst_ch08"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("About what fraction of the earth's surface is covered with water?", ["one-fourth", "one-half", "three-fourths", "nine-tenths"], 2, "But only a small proportion of it is freshwater that can be put to use."),
mc("Who called dams the 'temples of modern India'?", ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "B. R. Ambedkar"], 1),
mc("The Hirakud Dam is built on the river:", ["Satluj", "Mahanadi", "Krishna", "Narmada"], 1),
mc("Underground tanks for storing rooftop rainwater in Bikaner, Phalodi and Barmer are called:", ["johads", "tankas", "kuls", "ahars"], 1),
mc("The 'guls' or 'kuls' of the Western Himalayas are:", ["diversion channels for irrigation", "bamboo pipes", "underground tanks", "flood embankments"], 0),
mc("The first state in India to make rooftop rainwater harvesting compulsory for all houses was:", ["Rajasthan", "Tamil Nadu", "Gujarat", "Punjab"], 1),
mc("The Bhakra-Nangal project water is used for:", ["only flood control", "hydel power and irrigation", "only navigation", "only fish breeding"], 1, "It lies in the Sutluj-Beas river basin."),
W("Fill in the blank: The Sardar Sarovar Dam is built across the river ______ in Gujarat.", 1, "Narmada. (1)", "E"),
W("True or false, with a reason: 'Water scarcity in India is only because of low rainfall.'", 2,
  "False (1). It is also caused by over-exploitation, excessive use, unequal access, growing population and pollution (1).", "E"),
W("Define (i) multipurpose river project (ii) rainwater harvesting.", 2,
  "(i) A dam that serves many purposes at once: irrigation, power, water supply, flood control, navigation, recreation, fish breeding (1). (ii) Collection and storage of rainwater, so that it can be used later or can recharge groundwater (1).", "E"),
W("Name two uses of water in a modern multipurpose project besides irrigation.", 2,
  "Any two: electricity generation, water supply for domestic and industrial use, flood control, inland navigation, recreation, fish breeding. (1 + 1)", "E"),
W("Match: (i) Khadins (ii) Inundation channels (iii) Bamboo drip irrigation (iv) Kuls.  A. Meghalaya  B. Bengal flood plains  C. Jaisalmer  D. Western Himalayas.", 2,
  "(i)-C, (ii)-B, (iii)-A, (iv)-D. (all four = 2; two or three = 1)", "E"),
W("Name two multipurpose projects with their rivers.", 2,
  "Any two: Bhakra-Nangal (Sutluj-Beas basin), Hirakud (Mahanadi), Sardar Sarovar (Narmada). (1 + 1)", "E"),
W("Name two ways in which pollution affects water availability.", 2,
  "Domestic and industrial wastes, chemicals, pesticides and fertilisers dissolve in water (1). This makes water unfit for use, reducing the quantity of usable water (1).", "E"),
W("What is 'palar pani' in Rajasthan?", 2,
  "Rainwater (1). It is considered the purest form of natural water, and is stored in tankas for drinking (1).", "E"),
W("Why is it surprising that countries and regions suffer water scarcity when three-fourths of the earth is covered with water? Give one reason from the chapter.", 2,
  "Only a small proportion of the water is freshwater that can be put to use (1). It comes from surface run-off and groundwater renewed through the hydrological cycle, but scarcity arises from over-exploitation, excessive use and unequal access (1).", "E"),
W("Which Indian state's village Gendathur is known for rooftop rainwater harvesting?", 1,
  "Karnataka (Mysuru district). (1)", "E"),
W("Name two traditional rainwater harvesting methods and the regions where they are used.", 2,
  "Any two: tankas (Bikaner, Phalodi, Barmer), kuls (Western Himalayas), khadins (Jaisalmer), johads (Rajasthan), inundation channels (Bengal), bamboo drip irrigation (Meghalaya). (1 + 1)", "E"),
# ------------------------------------------------------------------ MEDIUM (19)
W("Why is the 'hydrological cycle' important for water resources? Explain in three steps.", 3,
  "Water evaporates from oceans and land, forms clouds and falls as rain or snow (1). Part runs off into rivers and recharges groundwater (1). Because the cycle continually renews freshwater, water is a renewable resource, but only if it is used sustainably and kept unpolluted (1).", "M"),
W("Why was water harvesting seen as a viable alternative to multipurpose projects? Give three points.", 3,
  "Multipurpose projects face rising resistance because of their disadvantages (1). Water harvesting is viable both socio-economically and environmentally (1). It uses local knowledge of rainfall regimes, soil types and water needs, e.g. tankas, kuls and johads (1).", "M"),
W("Explain why India faces water scarcity though it has a large share of world rainfall. Give three reasons.", 3,
  "Availability is uneven in space and time; some regions get heavy rain, others very little (1). Population growth increased demand for domestic use, food and industry (1). Over-extraction of groundwater by tube wells, pollution and unequal access reduce usable water (1).", "M"),
W("How has irrigation for higher food production worsened water scarcity? Give two points.", 2,
  "To produce more food, water resources are over-exploited to expand irrigated area for dry-season agriculture; irrigated agriculture is the largest consumer of water (1). Farmers dig own wells and tube-wells, which lowers groundwater levels and affects water availability and food security (1).", "M"),
W("Read the source and answer. 'Jawaharlal Nehru proclaimed dams as the temples of modern India. He believed that the dams would integrate agriculture and the village economy with industry and urban economy.'  (i) Why did Nehru consider dams so important? (ii) Name two benefits. (iii) What criticisms later emerged?", 3,
  "(i) They would bring together agriculture and industry, rural and urban economies (1). (ii) Irrigation, hydroelectricity, flood control (any two) (1). (iii) Dams affect the natural flow of rivers, cause sedimentation and fragment rivers; they submerge vegetation and soil, cause large-scale displacement and loss of livelihood, and irrigation has shifted farmers to water-intensive commercial crops (1).", "M"),
W("List three advantages of multipurpose projects, with one example each.", 3,
  "Hydel power and irrigation - Bhakra-Nangal in the Sutluj-Beas basin (1). Flood control with conservation of water - Hirakud in the Mahanadi basin (1). Water for drought-prone and desert areas - Sardar Sarovar on the Narmada (1).", "M"),
W("Why have dams been opposed? Explain three problems.", 3,
  "Regulating and damming affects the natural flow, causing excessive sedimentation in reservoirs and poorer habitats for aquatic life; dams fragment rivers (1). Reservoirs submerge vegetation and soil; dams meant to control floods have triggered floods through sedimentation, and the flood plains lose natural silt (1). Multipurpose projects have induced earthquakes, caused water-borne diseases and pests, and changed cropping patterns towards water-intensive crops (1).", "M"),
W("What is the inter-state water dispute? Give an example from the chapter and explain why such disputes arise.", 3,
  "A disagreement between states over sharing of river water (1). Example: the Krishna-Godavari dispute, where Karnataka and Andhra Pradesh object to Maharashtra diverting more water at Koyna for a multipurpose project (1). It would reduce the downstream flow in their states, harming agriculture and industry (1).", "M"),
W("Why have big dams been unsuccessful in controlling floods at times? Give two points.", 2,
  "Dams constructed to control floods have triggered floods because of sedimentation in the reservoir (1). Big dams have mostly been unsuccessful in controlling floods at the time of excessive rainfall, causing damage to life and property and soil erosion (1).", "M"),
W("Describe the Sardar Sarovar project in three points.", 3,
  "Built over the Narmada in Gujarat, it is one of the largest water resource projects of India, covering four states: Maharashtra, Madhya Pradesh, Gujarat and Rajasthan (1). It provides irrigation to 18.45 lakh hectares covering 3,112 villages in 15 districts of Gujarat (1). It also irrigates 2,46,000 hectares in the desert districts of Barmer and Jalore in Rajasthan and 37,500 hectares in tribal Maharashtra (1).", "M"),
W("Explain traditional rainwater harvesting in Rajasthan: tankas, khadins and johads.", 3,
  "Tankas: underground tanks, as large as a big room, built in houses to store rooftop rainwater in Bikaner, Phalodi and Barmer; the first spell of rain is not collected (1). Khadins: fields in Jaisalmer converted into rain-fed storage so water can stand and moisten the soil (1). Johads: similar rain-fed storage structures in other parts of Rajasthan (1).", "M"),
W("A student writes: 'Bamboo drip irrigation is used in Rajasthan.' Correct the statement and describe the method.", 3,
  "It is used in Meghalaya (1). Bamboo pipes tap natural springs on hilltops and carry water to plants by gravity, even over hundreds of metres (1). About 18-20 litres entering the system is reduced to 20-80 drops a minute at the plant; the system is about 200 years old (1).", "M"),
W("Why was rooftop rainwater harvesting declining in western Rajasthan? Why are tankas still valued?", 3,
  "The perennial Indira Gandhi Canal made plenty of water available, so rooftop harvesting declined (1). Some houses still keep tankas because they do not like the taste of tap water (1). Tankas store 'palar pani', the purest natural water, and keep drinking water available when other sources dry up in summer (1).", "M"),
W("How did Tamil Nadu and Gendathur (Karnataka) show the success of rainwater harvesting?", 3,
  "Tamil Nadu is the first state to make rooftop rainwater harvesting structures compulsory for all houses, with legal provisions to punish defaulters (1). In Gendathur, a remote village in Mysuru, nearly 200 households installed rooftop systems and the village is rich in rainwater (1). Shillong, though near Cherapunjee and Mawsynram, uses rooftop harvesting for 15-25 per cent of household water needs (1).", "M"),
W("Arrange in chronological order: (a) Sringaverapura near Allahabad (first century B.C.) harvests Ganga flood water (b) dams and lakes built in the time of Chandragupta Maurya (c) Bhopal Lake built (11th century) (d) Hauz Khas tank built (13th-14th century). Give the letters.", 2,
  "b, a, c, d. (all in order = 2; one slip = 1)", "M"),
W("Map description: On a map of India, locate the basins of (i) Bhakra-Nangal (ii) Hirakud (iii) Sardar Sarovar.", 3,
  "(i) Bhakra-Nangal: Sutluj-Beas basin in the north-west (1). (ii) Hirakud: Mahanadi basin in Odisha (1). (iii) Sardar Sarovar: Narmada river in Gujarat (1).", "M"),
W("Why is the quality of water as important as quantity? Give three points.", 3,
  "Polluted water cannot be used for drinking, irrigation or industry, so the usable quantity falls (1). Untreated domestic and industrial wastes, pesticides and fertilisers contaminate rivers and groundwater (1). Poor quality leads to diseases, loss of aquatic life and added cost for treatment (1).", "M"),
W("Why do many cities face water stress even if the region has ample water? Give two reasons.", 2,
  "Large dense populations and urban lifestyles need more water and energy, and many housing societies have their own groundwater pumping devices (1). Industries are heavy users of water and also need power; fragile water resources are over-exploited and depleted in several cities (1).", "M", wp=True),
W("Name four uses of modern dams other than irrigation and explain why they are called multipurpose projects.", 2,
  "Dams impound water, so besides irrigation they now serve electricity generation, domestic and industrial water supply, flood control, recreation, inland navigation and fish breeding (1). Their many uses are integrated with one another (1).", "M"),
W("Differentiate between traditional rainwater harvesting and large multipurpose dams using two examples each.", 3,
  "Traditional: tankas, johads, khadins, kuls, bamboo drip - made with knowledge of local rainfall and soil (1.5). Modern: big dams such as Bhakra-Nangal and Hirakud, canals and tube wells - large scale, power and irrigation, but displacement, sedimentation and disputes (1.5).", "M"),
# ------------------------------------------------------------------ HARD (13)
W("'Dams have been called temples of modern India, but they have also become sources of conflict.' Discuss with two arguments on each side.", 5,
  "For: multipurpose use - irrigation, power, flood control; integrates agriculture and the village economy with industry and the urban economy; Bhakra-Nangal and Hirakud (2). Against: sedimentation, fragmented rivers, submerged land, large-scale displacement and loss of livelihood, disputes such as Krishna-Godavari, water-intensive commercial crops (2). Balanced view: modern thinking prefers smaller decentralised projects combined with watershed management (1).", "H"),
W("Case study. Meena, a farmer's daughter in Barmer, wants to store rooftop water but her family relies on the canal supply. (i) Name the structure that she could build. (ii) Explain how it works. (iii) Give two reasons why it is good for the region. (iv) Give one limitation.", 4,
  "(i) A tanka, underground tank (1). (ii) Rainwater from the roof is collected through a pipe into the tank and stored; some houses have the tank connected to the roof; it is used for drinking in the dry months (1). (iii) Water is pure (palar pani), cheap, available near the house, and recharges groundwater (1). (iv) Needs rain and space and is limited in quantity; hence it supports rather than replaces canal supplies (1).", "H", wp=True),
W("Examine how the relation between population, industrialisation, urbanisation and water scarcity develops. Use five points.", 5,
  "Population growth raises demand for domestic water and food (1). Irrigation expansion with tube wells lowers groundwater levels (1). Industries use huge volumes and discharge waste, polluting rivers (1). Urbanisation creates large water-demanding populations and builds over recharge areas (1). Unequal access and poor management make it worse; policy must conserve, recycle and harvest (1).", "H"),
W("Compare multipurpose projects with rainwater harvesting on (i) cost (ii) environmental impact (iii) beneficiaries (iv) maintenance.", 4,
  "(i) Dams are very costly; harvesting structures are cheap (1). (ii) Dams submerge land and disrupt rivers; harvesting is eco-friendly (1). (iii) Dams serve large regions and cities; harvesting serves households and villages (1). (iv) Dams need state agencies and technical management; harvesting can be maintained by local people (1).", "H"),
W("Study the data (Sardar Sarovar project, from the chapter): irrigation in Gujarat 18.45 lakh ha; Barmer and Jalore (Rajasthan) 2,46,000 ha; tribal Maharashtra 37,500 ha.  (i) Convert the Rajasthan and Maharashtra areas to lakh hectares. (ii) Find the total irrigated area in lakh hectares. (iii) Why is the project important for drought-prone areas?", 4,
  "(i) 2,46,000 ha = 2.46 lakh ha; 37,500 ha = 0.375 lakh ha (1). (ii) 18.45 + 2.46 + 0.375 = 21.285 lakh ha (about 21.3 lakh ha) (2). (iii) About 75 per cent of the command area in Gujarat and all of the command in Rajasthan is drought-prone; assured water will make the area drought-proof (1).", "H", wp=True),
W("How have traditional water-harvesting systems adapted to different regions of India? Give five regional examples and say why they suited the place.", 5,
  "Western Himalayas: kuls (guls) are diversion channels for agriculture in hill and mountain regions (1). Rajasthan: tankas for rooftop water in Bikaner, Phalodi and Barmer in the arid region (1). Jaisalmer and other parts of Rajasthan: khadins and johads, fields converted to rain-fed storage in arid and semi-arid land (1). Bengal: inundation channels to irrigate fields on flood plains (1). Meghalaya: bamboo drip irrigation tapping hilltop springs by gravity (1).", "H"),
W("Read the source and answer. 'In Gendathur, a remote backward village in Mysuru, Karnataka, villagers have installed rooftop rainwater harvesting in their households; nearly 200 households have installed the system.'  (i) What does this show about community action? (ii) How can rooftop harvesting reduce pressure on groundwater? (iii) Write two steps a school in your city can take.", 3,
  "(i) Villagers can solve water problems by their own initiative, even in remote places (1). (ii) Stored rainwater reduces the need for pumps and also recharges groundwater (1). (iii) Any two: collect roof water with a pipe, filter it through sand and bricks and send it to a sump or well; recharge groundwater through a hand pump or abandoned dug well (1).", "H"),
W("Compare the water situations of a region with high rainfall but large population and a region with high rainfall but polluted water. Which of them suffers water scarcity and why?", 4,
  "Both can suffer water scarcity (1). A large and growing population needs more water for domestic use and to produce food, so demand can exceed supply even where rainfall is high (1.5). Where water is sufficient but polluted by domestic and industrial wastes, chemicals, pesticides and fertilisers, it becomes hazardous for human use, so scarcity arises from bad quality (1.5).", "H"),
W("Evaluate the statement: 'Conserving water means more than building dams.' Give four measures from the chapter.", 4,
  "Rainwater harvesting at household level and revival of tankas, johads and kuls (1). Controlling pollution of water by domestic and industrial wastes, chemicals and fertilisers (1). Developing drought-resistant crops and dry-farming techniques, since irrigated agriculture is the largest consumer (1). Government schemes such as Jal Jeevan Mission (piped potable water), Atal Bhujal Yojana and PM Krishi Sinchayee Yojana ('per drop more crop') (1).", "H"),
W("A district officer in Rajasthan must decide whether to promote tankas or a big canal. Prepare a two-sided note with one recommendation.", 4,
  "Canal (like the perennial Indira Gandhi Canal): brings plentiful water, but rooftop harvesting declined where it came (1.5). Tanka: stores palar pani, the purest water, a reliable drinking source in summer when others dry up; also keeps rooms cool (1). Recommendation: combine both, using the canal for farming and tankas for drinking water, with reasoning (1.5).", "H", wp=True),
W("Why does the unequal access to water by different social groups matter? Link it to scarcity, irrigation and drinking water in villages and cities.", 4,
  "Water scarcity in most cases is caused by over-exploitation, excessive use and unequal access among different social groups, not only by low rainfall (1). Farmers with their own wells and tube-wells and housing societies with their own pumps draw groundwater, lowering the water table (1). Irrigation has shifted many farmers to water-intensive commercial crops (1). Hence sharing and conservation matter as much as supply (1).", "H"),
W("Examine the role of dams in flood control and in causing floods, using the chapter's points. Suggest one improvement.", 4,
  "Dams like Hirakud integrate conservation of water with flood control (1). But dams built to control floods have triggered floods because of sedimentation in the reservoir (1). Big dams have mostly failed to control floods at the time of excessive rainfall, causing devastation and soil erosion, and flood plains are deprived of silt (1). Improvement: any reasoned suggestion, e.g. rainwater harvesting and watershed measures to reduce reliance on huge dams (1).", "H"),
]

# ------------------------------------------------------------------ NOTES
_old = runpy.run_path(str(REPO / "src/rn_work/c10_sst/c08.py"))["CH"]
_i = max(k for k, b in enumerate(_old["blocks"]) if b[0] == "h2")
_core = _old["blocks"][:_i]
def _fix(x, a, b):
    if isinstance(x, str): return x.replace(a, b)
    if isinstance(x, (list, tuple)): return type(x)(_fix(y, a, b) for y in x)
    return x
def _drop(blocks):
    out = []
    for b in blocks:
        if b[0] == "table":
            rows = [r for r in b[2] if not any(k in " ".join(r) for k in ("Nagarjuna", "Tungabhadra", "Tehri", "Ahars"))]
            b = (b[0], b[1], rows)
        out.append(b)
    return out
_core = _drop(_core)
for _a, _b2 in [
    ("About **96.5 per cent** of the world's water is in the oceans and only about **2.5 per cent** is freshwater; of this, nearly 70 per cent is in the form of ice sheets and glaciers. India receives about **4 per cent** of the global precipitation yet it ranks only about 133rd in the world in water availability per person per year, and the availability is uneven in space and time.", "About three-fourths of the earth's surface is covered with water, but only a small proportion is freshwater that can be put to use; it comes from surface run-off and groundwater renewed by the hydrological cycle, so water is a renewable resource. Its availability varies over space and time because of variations in seasonal and annual precipitation."),
    ("Irrigation: to increase food production, India has used large amounts of water for the **green revolution**; farmers have used tube wells and pumps, which has led to a fall in groundwater levels.", "Irrigation: to produce more food, water resources are over-exploited to expand irrigated area; irrigated agriculture is the largest consumer of water, and tube wells and wells in farms lower groundwater levels."),
    ("Dams caused **inter-state water disputes** (such as over the Krishna-Godavari and Cauvery) and in some cases flooding rather than flood control (for example the Maharashtra-Gujarat floods of 2006, linked to water released from dams).", "Dams cause **inter-state water disputes** (for example Krishna-Godavari: Karnataka and Andhra Pradesh object to Maharashtra diverting more water at Koyna) and sometimes trigger floods through sedimentation instead of controlling them; they can also induce earthquakes and water-borne diseases and push farmers to water-intensive commercial crops."),
    ("**Social movements:** the **Narmada Bachao Andolan** and the **Tehri Dam Andolan** opposed dams, mainly for displacement and the cost to the environment. Many such dams did not give the benefits promised: irrigation was used for commercial crops, and water was not equitably shared.", "**Opposition:** large dams and multipurpose projects have come under great scrutiny for displacement, loss of livelihood and ecological costs. The **Sardar Sarovar** project on the Narmada (Gujarat, four states) will irrigate 18.45 lakh hectares in Gujarat and 2,46,000 hectares in Barmer and Jalore."),
    ("Hence emphasis shifted to **small, decentralised** projects, using watershed management and rainwater harvesting.", "Rainwater harvesting was seen as a viable alternative, both socio-economically and environmentally."),
    ("; the states of Karnataka also encouraged it", ""),
    ("**Tankas / kunds**: underground tanks", "**Tankas**: underground tanks"),
    ("sometimes connected with the roof; ", "connected to sloping roofs by a pipe; "),
    ("Dams were traditionally", "Dams were traditionally"),
]:
    _core = _fix(_core, _a, _b2)
_extra = [
 ("h2", "Timeline and Landmarks"),
 ("table", ["Period", "Development"], [
  ["Ancient and medieval India", "Guls/kuls, tankas, khadins, johads and inundation channels"],
  ["After Independence", "Multipurpose projects such as Bhakra-Nangal, Hirakud and Sardar Sarovar; Nehru calls dams temples of modern India"],
  ["Recent decades", "Tube wells, industry and cities raise demand; groundwater falls"],
  ["Recent years", "Revival of rainwater harvesting; Tamil Nadu makes rooftop harvesting compulsory"]]),
 ("h2", "Key Terms"),
 ("table", ["Term", "Meaning"], [
  ["Hydrological cycle", "Circulation of water between ocean, air and land"],
  ["Multipurpose project", "Dam used for many purposes"],
  ["Watershed management", "Conserving and efficiently using water and soil in a drainage basin"],
  ["Tanka", "Underground tank in Rajasthan homes"],
  ["Johad / khadin", "Rain-storing earthen check dam / agricultural field storage"],
  ["Guls / kuls", "Western Himalayan irrigation channels"],
  ["Palar pani", "Rainwater, purest natural water"],
  ["Sedimentation", "Silt deposition reducing reservoir capacity"]]),
 ("h2", "Map Pointers"),
 ("ul", ["Mark rivers and dams: **Sutluj-Beas (Bhakra-Nangal), Mahanadi (Hirakud), Narmada (Sardar Sarovar)** and **Koyna** (Krishna-Godavari dispute).",
  "Mark **Bikaner, Phalodi, Barmer (tankas), Jaisalmer (khadins)**, **Meghalaya** (bamboo drip), **Himachal** (kuls) and **Gendathur (Karnataka)**."]),
 ("h2", "Case Notes"),
 ("ul", ["**Case: Tankas in Bikaner.** Underground tank, rooftop water, 'palar pani', mostly neglected after canal water arrived.",
  "**Case: Sardar Sarovar.** Narmada project covering four states; irrigates 18.45 lakh ha in Gujarat and desert districts Barmer and Jalore; criticised for displacement and costs.",
  "**Case: Gendathur.** Villagers installed rooftop harvesting and became water-rich.",
  "**Source tip:** In a source about water, identify (i) source, (ii) user, (iii) problem, (iv) solution."]),
 ("h2", "Cause and Effect Chains"),
 ("table", ["Cause", "Effect"], [
  ["Population growth and irrigation", "Rising demand; groundwater falls"],
  ["Industrial and domestic waste", "Water pollution, less usable water"],
  ["Big dams", "Power and irrigation, but displacement and disputes"],
  ["Canal water supply", "Traditional tankas neglected"],
  ["Rainwater harvesting", "Groundwater recharge and local self-reliance"]]),
 ("h2", "Writing Better Answers on Water Resources"),
 ("ul", ["**Start with the paradox.** India receives a large share of global precipitation, yet scarcity is common. Explain it with three linked ideas: uneven distribution in space and time, rising demand (population, irrigation, industry, cities) and pollution or unequal access.",
  "**Balance every dam answer.** Benefits: irrigation, hydroelectricity, flood control, water supply, navigation, fish breeding. Costs: displacement, loss of fertile land and forests, sedimentation, fragmented rivers, inter-state disputes and benefits going to commercial crops and richer regions.",
  "**Name the place with the method.** Tankas - Bikaner, Phalodi, Barmer; khadins - Jaisalmer; kuls - Western Himalayas; inundation channels - Bengal; bamboo drip - Meghalaya. One method per region earns full marks in a list answer.",
  "**Argue for revival.** Traditional methods are cheap, local, eco-friendly and recharge groundwater, but were neglected after canals, piped supply and tube wells arrived; a good answer says what has changed (Tamil Nadu's rule, Gendathur's success).",
  "**Include a lesson.** Water security needs conservation, recycling, pollution control and community management, not dams alone. Government schemes named in the chapter: Jal Jeevan Mission (assured piped potable water, 55 litres per person per day), Atal Bhujal Yojana (water-stressed gram panchayats of seven states) and PM Krishi Sinchayee Yojana (har khet ko pani, per drop more crop).",
  "**Use numbers carefully.** Three-fourths of the earth's surface is water, but only a small proportion is usable freshwater; Gendathur's 200 houses harvest about 1,00,000 litres a year (as given in the text) and Sardar Sarovar irrigates 18.45 lakh hectares in Gujarat; quote text figures only."]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "Do not claim that water scarcity is due only to low rainfall. **Tankas** are in **Rajasthan**; **bamboo drip** is in **Meghalaya**; **kuls** in **Western Himalayas**. **Nehru** called dams temples of modern India."),
 ("h2", "Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Why is water scarce in India? (3)", "Uneven availability, over-use, population growth, pollution and unequal access."),
  ("Give arguments for and against multipurpose projects. (5)", "Benefits: irrigation, power, flood control. Problems: displacement, sedimentation, disputes, floods and unequal benefits."),
  ("Describe rainwater harvesting methods of India. (5)", "Kuls in the Himalayas, tankas, khadins and johads in Rajasthan, inundation channels in Bengal, bamboo drip in Meghalaya."),
  ("How can rooftop harvesting help cities? (3)", "Stores rainwater, recharges groundwater and cuts demand on piped water."),
  ("What is the role of communities in water conservation? (3)", "They build, maintain and manage local systems and can launch movements like NBA."),
 ]),
]
CH = dict(num=8, title=_old["title"], tag=_old["tag"], intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_core + _extra, takeaways=_old["takeaways"] + ["Remember: **Nehru - dams as temples; Rajasthan - tankas; Meghalaya - bamboo drip; Tamil Nadu - compulsory harvesting**."])

if __name__ == "__main__": run(__file__, BANK, 10, "Social_Science", WS, CH)
