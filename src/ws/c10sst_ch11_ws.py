"""Class 10 Social Science Ch 11 - Manufacturing Industries (Geography Ch 6): worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c10sst_ch11"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)
AR = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"]
def ar(a, r, i, why, lvl="E"):
    return W(f"Assertion (A): {a}  Reason (R): {r}  Choose the correct option.", 1, f"({'abcd'[i]}) {AR[i]}. {why}", lvl, opts=AR)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("Manufacturing is the process of:", ["extracting minerals from the earth", "producing more valuable goods in large quantities from raw materials", "growing crops", "selling goods in markets"], 1, "Paper from wood and sugar from sugarcane are examples."),
mc("Which one of these is an agro-based industry?", ["Cement", "Iron and steel", "Cotton textile", "Aluminium smelting"], 2, "Cotton, jute, silk, woollen, sugar and edible oil industries use farm raw materials."),
mc("Which one of the following is a basic or key industry?", ["Iron and steel", "Toothpaste", "Sugar", "Biscuits"], 0, "Its products are raw materials for other industries."),
mc("BHEL and SAIL belong to the:", ["private sector", "public sector", "joint sector", "cooperative sector"], 1),
mc("Oil India Limited (OIL) is an example of the:", ["joint sector", "cooperative sector", "private sector", "public sector only"], 0, "It is jointly owned by the public and the private sector."),
mc("The first successful cotton textile mill in India was set up in:", ["Ahmedabad in 1900", "Mumbai in 1854", "Kolkata in 1818", "Chennai in 1904"], 1),
mc("India's electronic capital is:", ["Hyderabad", "Bengaluru", "Pune", "Chennai"], 1),
mc("Thermal pollution of water occurs when:", ["oil spills on the sea", "hot water from factories and thermal plants is drained into rivers before cooling", "plastic is dumped on land", "acid rain falls"], 1, "It harms aquatic life."),
W("Fill in the blanks: The jute industry is concentrated mainly along the banks of the river ______ in West Bengal, and the first cement plant was set up in ______ in 1904.", 2, "Hugli; Chennai. (1 + 1)", "E"),
W("Name any two industries based on mineral raw materials.", 1, "Any two of iron and steel, cement, aluminium, machine tools, petrochemicals. (1)", "E"),
W("Name the four types of pollution caused by industries.", 2, "Air, water, land (soil) and noise pollution. (2; half a mark each)", "E"),
W("Define consumer industries with two examples.", 2, "Industries that produce goods for direct use by consumers (1), such as sugar, toothpaste, paper, sewing machines, fans (any two) (1).", "E"),
W("Match: (i) Jamshedpur (ii) Bhilai (iii) Mumbai (iv) Salem.  A. SAIL steel plant in Chhattisgarh  B. First cotton mill  C. Steel plant in Tamil Nadu  D. TISCO.", 2, "(i)-D, (ii)-A, (iii)-B, (iv)-C. (all four = 2; two or three correct = 1)", "E"),
W("True or false (with reason): 'Agriculture and industry are completely independent of each other.'", 2,
  "False (1). Agro-industries give a boost to agriculture by raising productivity (machines, fertilisers, pesticides) and agriculture supplies raw material to industries, so they move hand in hand (1).", "E"),
W("What is meant by a small-scale industry? What is the present investment limit mentioned in the text?", 2,
  "A small-scale industry is defined with reference to the maximum investment allowed on the assets of a unit (1). At present the limit is Rupees one crore (1).", "E"),
W("List any two ways in which the manufacturing sector helps in reducing regional disparities.", 2,
  "Industries are established in tribal and backward areas, creating jobs there (1). This reduces unemployment and poverty and brings down regional disparities (1).", "E"),
W("Name any two sources of noise pollution in industrial areas.", 1, "Machinery, factory equipment, generators, saw mills, pneumatic and electric drills (any two). (1)", "E"),
# ------------------------------------------------------------------ MEDIUM (20)
ar("The cotton textile industry was first concentrated in Maharashtra and Gujarat.", "These states have cotton-growing black soil, a moist climate, ports and a ready market.", 0, "Availability of raw cotton, market, transport including ports, labour and moist climate contributed to localisation.", "M"),
ar("Sugar mills have been shifting to the southern and western states, especially Maharashtra.", "The cane grown there has a higher sucrose content, cooler climate gives a longer crushing season and cooperatives are more successful.", 0, "All three factors named in R explain the shift.", "M"),
W("'Manufacturing is the backbone of development.' Explain with three points.", 3,
  "It modernises agriculture by supplying machines, fertilisers and pesticides, and reduces dependence on farming by creating jobs in the secondary and tertiary sectors (1). It reduces unemployment and poverty and brings down regional disparities by establishing industries in tribal and backward areas (1). Export of manufactured goods expands trade and brings in foreign exchange (1).", "M"),
W("Classify industries on the basis of ownership with one example of each.", 3,
  "Public sector: BHEL, SAIL (0.75). Private sector: TISCO, Bajaj Auto, Dabur (0.75). Joint sector: Oil India Limited (0.75). Cooperative sector: sugar industry in Maharashtra, coir industry in Kerala (0.75).", "M"),
W("Why is the sugar industry ideally suited to the cooperative sector?", 2,
  "Sugarcane is bulky and loses sucrose content in haulage, and the industry is seasonal in nature (1). Cooperatives are owned and run by the cane producers who pool their resources, share profits and losses and supply cane regularly to the mill (1).", "M"),
W("Why are jute mills mostly located in the Hugli basin? Give three reasons.", 3,
  "Proximity of the jute-producing areas and inexpensive water transport, supported by a good network of railways, roadways and waterways (1). Abundant water for processing raw jute and cheap labour from West Bengal and adjoining Bihar, Odisha and Uttar Pradesh (1). Kolkata provides banking, insurance and port facilities for the export of jute goods (1).", "M"),
W("State two facts about the jute industry from the chapter: its position in the world, the year and place of the first jute mill, and the effect of Partition in 1947.", 3,
  "India is the largest producer of raw jute and jute goods and second to Bangladesh as an exporter (1). The first jute mill was set up near Kolkata at Rishra in 1855 (1). After Partition in 1947 the mills remained in India but three-fourths of the jute-producing area went to Bangladesh (1).", "M"),
W("In an iron and steel plant, 28 tonnes of material are used in the ratio of 4 : 2 : 1 for iron ore, coking coal and limestone. Find the amount of each. Why is manganese also needed?", 3,
  "Total ratio 4 + 2 + 1 = 7 parts, so 1 part = 28 / 7 = 4 tonnes (1). Iron ore = 16 tonnes, coking coal = 8 tonnes, limestone = 4 tonnes (1). Manganese is needed in some quantity to harden the steel (1).", "M", wp=True),
W("Why is iron and steel called a basic or key industry? Why are its plants set up near raw materials?", 3,
  "All other industries (heavy, medium and light) depend on it for their machinery, and it supplies engineering goods, construction material, defence, medical and scientific equipment (1.5). The raw materials are heavy and bulky and costly to transport, so plants are located close to iron ore and coal (1.5).", "M"),
W("Name any four iron and steel plants and the states in which they are located.", 3,
  "Any four, e.g. Jamshedpur (Jharkhand, private TISCO), Bhilai (Chhattisgarh), Durgapur (West Bengal), Rourkela (Odisha), Bokaro (Jharkhand), Visakhapatnam (Andhra Pradesh), Salem (Tamil Nadu), Bhadravati (Karnataka) (3, 0.75 each).", "M"),
W("Why is the Chotanagpur plateau region ideal for iron and steel plants?", 3,
  "Low cost of iron ore and high-grade raw materials in the region (1). Cheap labour and a good market for steel (1). Closeness to coal and an efficient transport network (1).", "M"),
W("Give any three characteristics of aluminium. Why does an aluminium smelter need regular power supply?", 3,
  "Light, resistant to corrosion, a good conductor of heat and malleable, and it becomes strong when mixed with other metals (1.5, any three characteristics). Electricity is a prime location factor; smelting uses large amounts of power and bauxite is bulky, so the plant needs an assured raw material source at minimum cost (1.5).", "M"),
W("Differentiate between inorganic and organic chemical industries with examples.", 2,
  "Inorganic: sulphuric acid, nitric acid, alkalies, soda ash, caustic soda (1). Organic: petrochemicals, used to make synthetic fibres, synthetic rubber, plastics, dye-stuffs, drugs and pharmaceuticals (1).", "M"),
W("Why is the cement industry located near limestone sources and why are Gujarat's plants well placed for export?", 3,
  "Cement needs bulky and heavy raw materials such as limestone, silica, alumina and gypsum (1), and coal and electric power; transport of these is costly (1). Gujarat plants are near the ports, which help in exports (1).", "M"),
W("Locate on a map: (i) Rishra near Kolkata (ii) Chennai (iii) Bengaluru. What is each known for in this chapter?", 3,
  "(i) Rishra, near Kolkata in West Bengal: first jute mill (1855) (1). (ii) Chennai in Tamil Nadu: first cement plant (1904) (1). (iii) Bengaluru in Karnataka: electronic capital of India (1).", "M"),
W("What does the electronics industry cover, and what has been the major impact of the IT and electronics industry? Name three centres of major industry concentration.", 2,
  "It covers a wide range of products from transistor sets to television, telephones, cellular telecom, radars and computers (1). Major impact: employment generation; centres of major concentration: any three of Bengaluru, Noida, Mumbai, Chennai, Hyderabad, Pune (1).", "M"),
W("Error analysis. A student writes: 'Jute mills are mostly located in Maharashtra because it produces most jute.' Correct the statement.", 2,
  "Most jute mills are located in West Bengal along the Hugli river (1), because jute is produced in nearby areas and water transport, labour and water are available; Maharashtra is known for cotton textiles (1).", "M"),
W("A cooperative sugar mill near Kolhapur receives cane carried for 3 days by bullock cart. The mill manager says that the sugar recovered from this cane has fallen. (i) State the reason. (ii) Suggest one solution.", 2,
  "(i) The cane is bulky and its sucrose content reduces in haulage over long periods (1). (ii) Set up mills near the fields, ensure quick transport and crush the cane within hours of harvest (1).", "M", wp=True),
W("Why does a fertiliser industry expand after the Green Revolution? Name three states with fertiliser plants.", 3,
  "HYV seeds needed heavy fertiliser doses, so demand for nitrogenous, phosphatic and complex fertilisers increased (1.5). Gujarat, Tamil Nadu, Uttar Pradesh, Punjab, Kerala (any three) (1.5).", "M"),
# ------------------------------------------------------------------ HARD (13)
W("Classify industries on four bases: raw material, role, capital investment and ownership. Give two examples for each type in raw material and role.", 4,
  "Raw material: agro-based (cotton, jute, sugar) and mineral-based (iron and steel, cement) (1.5). Role: basic or key (iron and steel, copper smelting) and consumer industries (sugar, toothpaste, paper) (1). Capital investment: small scale (investment up to the limit of Rs one crore) and large scale (0.75). Ownership: public, private, joint and cooperative (0.75).", "H"),
W("Read the extract and answer. 'Thermal pollution of water occurs when hot water from factories and thermal plants is drained into rivers and ponds before cooling. Wastes from nuclear power plants and weapon production facilities cause cancers, birth defects and miscarriages.'  (i) What is thermal pollution? (ii) Which industries are main culprits of water pollution? (iii) Give two measures to control it.", 4,
  "(i) Rise in the temperature of river or pond water due to hot water discharged before cooling; it harms aquatic life (1). (ii) Paper, pulp, chemical, textile and dyeing, petroleum refineries, tanneries, electroplating and others which discharge dyes, detergents, acids, pesticides and fertilisers (1). (iii) Use water in two or more successive stages by reuse and recycling, rainwater harvesting, treatment of hot water and effluents before release into rivers (2).", "H"),
W("Describe in five points why iron and steel is called the basic industry and why the Chhotanagpur plateau has the maximum concentration of steel plants.", 5,
  "All other industries - heavy, medium and light - depend on it for their machinery (1). Steel is needed for engineering goods, construction material, defence, medical, telephonic and scientific equipment and consumer goods (1). It is a heavy industry; raw materials and finished goods are heavy and bulky and entail heavy transportation costs (1). Iron ore, coking coal and limestone are needed in the ratio of about 4 : 2 : 1, with some manganese to harden the steel (1). Chhotanagpur has low cost of iron ore, high-grade raw materials in proximity, cheap labour and vast growth potential in the home market (1).", "H"),
W("Explain how agriculture and industry are interdependent. Give four points with examples.", 4,
  "Agriculture and industry are not exclusive of each other; they move hand in hand (1). Agro-industries have given a major boost to agriculture by raising its productivity (1). Industries depend on agriculture for raw materials (cotton, jute, sugarcane, tea, edible oil) (1). They sell farmers irrigation pumps, fertilisers, insecticides, pesticides, plastic and PVC pipes, machines and tools (1).", "H"),
W("Case study. A factory in a Rajasthan town releases untreated dye-water into a drain that flows into a pond. Fish die, nearby wells become salty and the villagers complain of skin problems. (i) Name the type of pollution. (ii) List two substances that cause it. (iii) Suggest three control measures. (iv) Who should take action?", 5,
  "(i) Water pollution (1). (ii) Dyes, detergents, acids, salts, pesticides or fertilisers (1). (iii) Treatment of effluents before discharge, recycling and reuse of water, rainwater harvesting, and use of cleaner technology (2, any three). (iv) The factory owner, the State Pollution Control Board and the government, with the villagers' demand for compliance (1).", "H", wp=True),
W("Compare the cotton textile and the iron and steel industries on (i) raw material (ii) why they located where they did (iii) agro-based or mineral-based (iv) where they are concentrated.", 4,
  "Cotton: raw cotton; located in the cotton-growing belt of Maharashtra and Gujarat because of raw cotton, market, transport with ports, labour and moist climate; agro-based; spinning is centralised in Maharashtra, Gujarat and Tamil Nadu while weaving is decentralised (2). Iron and steel: iron ore, coking coal, limestone, manganese in about 4 : 2 : 1; located near raw materials because of heavy, bulky inputs; mineral-based; maximum concentration in the Chhotanagpur plateau region (2).", "H"),
W("Explain how industries pollute the air. Describe four measures to minimise air pollution given in the text.", 5,
  "Gases such as sulphur dioxide and carbon monoxide and particulate matter (dust, mist, smoke) are emitted by chemical and paper factories, brick kilns, refineries and smelting plants and by burning fossil fuels; toxic gas leaks (as in the Bhopal gas tragedy) can be hazardous; they harm health, animals, plants and buildings (2). Measures: install smoke stacks; fit particulate-capturing devices like electrostatic precipitators, scrubbers and fabric filters; use oil or gas instead of coal; change to cleaner fuels and technologies (3, any four).", "H"),
W("Explain with three examples why the textile industry occupies a unique position in the Indian economy.", 4,
  "It contributes significantly to industrial production, employment generation and foreign exchange earnings (1). It has close links with agriculture and gives work to farmers, cotton boll pluckers and workers engaged in ginning, spinning, weaving, dyeing, designing, packaging, tailoring and sewing (1.5). It supports other industries such as chemicals and dyes, packaging and engineering works, and it is the only industry in the country that is self-reliant and complete in the value chain (1.5).", "H"),
W("Passage-based. 'Our traditional industries suffered a setback during the colonial period because they could not compete with the mill-made cloth from England.'  (i) Which industry is this? (ii) Why could traditional producers not compete? (iii) How did the world wars help the Indian mills? (iv) Why must modern industries be efficient and competitive today?", 4,
  "(i) Cotton textile industry (hand spinning and handloom weaving) (1). (ii) Cheap mill-made cloth from England was produced in large quantity on machines (1). (iii) India was a British colony and, during the two world wars fought in Europe, there was demand for cloth in the UK, which boosted Indian mills (1). (iv) In a world of globalisation self-sufficiency alone is not enough; goods must be at par in quality with international goods to compete in global markets (1).", "H"),
W("Production problem. A cooperative mill crushes 1,500 tonnes of cane a day for 120 days and recovers 10 per cent as sugar. (i) How much sugar does it make in a season? (ii) If sugar sells at Rs 40 per kg, what is the total sale in crores of rupees? (iii) Why does a longer crushing season help?", 4,
  "(i) Cane = 1,500 x 120 = 1,80,000 tonnes; sugar = 10% = 18,000 tonnes (1.5). (ii) 18,000 tonnes = 1,80,00,000 kg; x Rs 40 = Rs 72,00,00,000 = Rs 72 crore (1.5). (iii) A longer crushing season keeps the mill working for more days, uses capital fully and gives farmers more time to sell cane (1).", "H", wp=True),
W("Describe the role of the automobile industry and explain how liberalisation affected it. Name four centres.", 4,
  "Automobile industry supplies trucks, buses, cars, motorcycles, scooters, mopeds and three-wheelers and creates demand for steel, aluminium, rubber, glass and electronics (1.5). After liberalisation the coming in of new and contemporary models stimulated the demand for vehicles, leading to healthy growth including passenger cars, two and three-wheelers (1). Centres: Delhi-Gurugram, Mumbai-Pune, Chennai, Kolkata, Lucknow, Indore, Hyderabad, Jamshedpur and Bengaluru (1.5, any four).", "H"),
W("'The industrial sector must not only grow but grow sustainably.' Explain with the example of NTPC and three measures needed.", 4,
  "Industries cause air, water, land and noise pollution, so growth without safeguards harms health and the environment (1). NTPC has ISO certification for its Environment Management System and a proactive approach: afforestation, ash utilisation, reuse of waste and compliance with environmental standards (1.5). Other measures: recycling of water, treatment of effluents, filters and precipitators, noise-reducing silencers and soundproofing (1.5).", "H"),
]

def _sub(x, pairs):
    if isinstance(x, str):
        for a, b in pairs: x = x.replace(a, b)
        return x
    if isinstance(x, (list, tuple)): return type(x)(_sub(i, pairs) for i in x)
    return x
_old = runpy.run_path(str(REPO / "src/rn_work/c10_sst/c11.py"))["CH"]
_i = max(k for k, b in enumerate(_old["blocks"]) if b[0] == "h2")
_PAIRS = [(". India's weaving sector, decentralised, is a major employer; India is a leading exporter of cotton yarn. Problems: erratic power supply, outdated machinery, low output of labour and stiff competition from synthetic fibres", ". Spinning is centralised in Maharashtra, Gujarat and Tamil Nadu while weaving is decentralised; the industry supports farmers, cotton boll pluckers and many other workers and is the only industry self-reliant and complete in the value chain"),
          ("; most mills are in the **Hugli basin** (West Bengal)", "; first jute mill at Rishra near Kolkata in 1855; most mills are in the **Hugli basin** (West Bengal)"),
          (". Challenges: stiff competition from synthetic substitutes and from Bangladesh, Brazil, Philippines, Egypt and Thailand; demand for jute bags in packaging has been promoted by the government", ". After Partition (1947) the mills remained in India but three-fourths of the jute-producing area went to Bangladesh"),
          (" Steel is produced in the **mini steel plants** as well.", ""),
          ("Steel is produced in the **mini steel plants** as well. ", ""),
          ("Second largest producer in the world after Brazil;", "Second largest producer of sugar in the world and first in gur and khandsari;"),
(" India is among the largest producers of crude steel and the largest producer of sponge iron; per capita consumption is low", ""),
          ("; India is the third largest producer of nitrogenous fertilisers", ""), ("; rapidly growing and diversified; contributes about 3 per cent of GDP", "; fast growing and diversifying, in both large and small units"),
          ("Second largest producer in the world after Brazil;", "Second largest producer of sugar in the world and first in gur and khandsari;"),
          ("Small scale (investment up to a limit) and large scale", "Small scale (maximum investment on assets, at present Rs one crore) and large scale"),
          (" **Taj Mahal** is threatened by the **Mathura refinery** and other industries, as acid rain (sulphur dioxide) damages the marble.", " Wastes from nuclear power plants and weapon production facilities cause cancers, birth defects and miscarriages."),
          ("**NTPC** has adopted environment-friendly measures: afforestation, ash utilisation, reuse of waste and compliance with environmental standards.", "**NTPC** has ISO 14001 certification for its Environment Management System and follows environment-friendly measures such as afforestation and ash utilisation."),
          ("; the target is to raise the share to 25 per cent", ""), ("the National Manufacturing Competitiveness Council (NMCC) was set up to improve the growth of manufacturing", "")]
_blocks = [b for b in _old["blocks"][:_i] if not (b[0] == "p" and "17 per cent" in b[1])]
_core = _sub(_blocks, _PAIRS)
_tk = [t for t in _old["takeaways"] if "NMCC" not in t]
_extra = [
 ("h2", "Chart: Industries by Classification"),
 ("table", ["Basis", "Group", "Examples"], [
  ["Raw material", "Agro-based", "Cotton, jute, silk, woollen textiles, sugar, edible oil, tea, coffee, rubber"],
  ["Raw material", "Mineral-based", "Iron and steel, cement, aluminium, machine tools, petrochemicals"],
  ["Role", "Basic / key", "Iron and steel, copper smelting"],
  ["Role", "Consumer", "Sugar, toothpaste, paper, sewing machines, fans"],
  ["Ownership", "Public / private / joint / cooperative", "BHEL, SAIL / TISCO, Bajaj Auto, Dabur / Oil India Ltd / sugar in Maharashtra, coir in Kerala"],
  ["Bulk and weight", "Heavy / light", "Iron and steel / electrical goods"]]),
 ("h2", "Location Factors of Major Industries"),
 ("table", ["Industry", "Why located there", "Main centres"], [
  ["Cotton textiles", "Cotton, market, ports, labour, moist climate", "Maharashtra, Gujarat; Mumbai (first successful mill, 1854)"],
  ["Jute", "Raw jute nearby, cheap water transport, water, labour, Kolkata port", "Hugli basin in West Bengal"],
  ["Sugar", "Bulky cane loses sucrose in transport; seasonal, so cooperatives suit", "Uttar Pradesh, Bihar, Maharashtra, Karnataka, Tamil Nadu"],
  ["Iron and steel", "Near iron ore, coal, limestone; cheap labour; market", "Jamshedpur, Bhilai, Durgapur, Rourkela, Bokaro, Visakhapatnam, Salem"],
  ["Aluminium", "Bauxite and assured power", "Odisha, West Bengal, Kerala, Uttar Pradesh, Chhattisgarh, Maharashtra, Tamil Nadu"],
  ["Cement", "Limestone, silica, alumina, gypsum, coal and power; ports for export", "First plant in Chennai (1904); Gujarat"],
  ["IT and electronics", "Skilled people, infrastructure, policy support", "Bengaluru (electronic capital), Hyderabad, Pune, Chennai, Delhi"]]),
 ("h2", "Timeline and Facts to Remember"),
 ("table", ["Year / ratio", "Fact"], [
  ["1854", "First successful textile mill in Mumbai"],
  ["1904", "First cement plant in Chennai"],
  ["1991", "Liberalisation and FDI boost the automobile and other industries"],
  ["4 : 2 : 1", "Approximate ratio of iron ore, coking coal and limestone for steel"],
  ["Rs one crore", "Maximum investment on assets for a small-scale unit (present limit)"],
  ["Sugar", "India second in the world in sugar, first in gur and khandsari"]]),
 ("h2", "Map Pointers"),
 ("ul", ["Mark the steel plants **Jamshedpur, Bhilai, Durgapur, Rourkela, Bokaro, Salem, Visakhapatnam, Bhadravati**.",
  "Mark the cotton centres **Mumbai, Ahmedabad, Surat**, the jute belt of the **Hugli basin** and the electronics hub **Bengaluru**.",
  "Mark **Rishra** (near Kolkata, first jute mill) and **Chennai** (first cement plant); locate the steel plants shown on the textbook map."]),
 ("h2", "Sources and Case Notes"),
 ("ul", ["**Source: Industrial pollution.** Industries cause four types of pollution: air, water, land and noise. Thermal power plants are also polluting industries.",
  "**Case: NTPC.** A major power corporation with ISO 14001 Environment Management System certification; takes up afforestation, ash utilisation and reuse of waste.",
  "**Case: Cooperative sugar mills of Maharashtra** show how producers own the industry and share profits and losses."]),
 ("h2", "Cause and Effect Chains"),
 ("table", ["Cause", "Effect"], [
  ["Colonial import of mill-made cloth from England", "Setback to traditional handloom industries"],
  ["Two world wars and demand from the UK", "Boost to the Indian cotton textile industry"],
  ["Green Revolution", "More demand for fertilisers; fertiliser industry expanded"],
  ["Hot water discharged from plants", "Thermal pollution; aquatic life harmed"],
  ["Bulky cane that loses sucrose", "Sugar mills near fields, in cooperatives, shifting to Maharashtra and the south"]]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "TISCO (Jamshedpur) is in the **private sector**, while SAIL plants (Bhilai, Durgapur, Rourkela, Bokaro) are in the **public sector**. The Hugli basin means the **jute** belt, not cotton."),
 ("note", "REMEMBER", "Do not mix **agro-based** (cotton, jute, sugar) and **mineral-based** (steel, cement, aluminium) industries. The ratio 4 : 2 : 1 is for **iron ore : coking coal : limestone**."),
 ("h2", "Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Why is manufacturing considered the backbone of economic development? (3)", "It modernises agriculture, creates secondary and tertiary jobs, cuts unemployment and poverty and regional disparities, and exports earn foreign exchange; prosperous countries convert raw materials into a wide range of finished goods."),
  ("Describe the measures to control industrial pollution of water. (3)", "Minimise water use by reuse and recycling in successive stages; harvest rainwater; treat hot water and effluents (physical, chemical and biological) before releasing them into rivers and ponds."),
  ("Why is the iron and steel industry called a basic industry? Where are its plants? (5)", "All industries depend on steel for machines; plants near raw materials at Jamshedpur, Bhilai, Durgapur, Rourkela, Bokaro, Visakhapatnam, Salem and Bhadravati; ratio 4 : 2 : 1 of ore, coking coal and limestone plus manganese."),
  ("How does the jute industry face competition? Suggest steps. (3)", "Competition from synthetic substitutes and from Bangladesh, Brazil, the Philippines, Egypt and Thailand; steps include better quality and government promotion of jute packaging."),
  ("State the importance of the IT industry. (3)", "Creates jobs, especially for women; earns foreign exchange through software and BPO; Bengaluru is the electronic capital; spread over several cities."),
 ]),
]
CH = dict(num=11, title=_old["title"], tag=_old["tag"], intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_core + _extra, takeaways=_tk + ["The first successful cotton mill was set up in **Mumbai in 1854**; the first cement plant in **Chennai in 1904**.", "Iron ore, coking coal and limestone are used in the ratio **4 : 2 : 1** in steel making."])

if __name__ == "__main__": run(__file__, BANK, 10, "Social_Science", WS, CH)
