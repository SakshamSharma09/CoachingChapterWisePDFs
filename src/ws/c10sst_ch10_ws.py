"""Class 10 Social Science Ch 10 - Minerals and Energy Resources (Geography Ch 5): worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c10sst_ch10"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)
AR = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"]
def ar(a, r, i, why, lvl="E"):
    return W(f"Assertion (A): {a}  Reason (R): {r}  Choose the correct option.", 1, f"({'abcd'[i]}) {AR[i]}. {why}", lvl, opts=AR)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("The finest iron ore, with up to 70 per cent iron and excellent magnetic qualities, is:", ["haematite", "magnetite", "limonite", "siderite"], 1, "Haematite is the most important in quantity but has 50-60 per cent iron."),
mc("Minerals such as gold, silver, tin and platinum that occur in sands of valley floors are called:", ["placer deposits", "lodes", "veins", "residual deposits"], 0, "They are not corroded by water."),
mc("Which one of these is a non-ferrous mineral?", ["Iron ore", "Manganese", "Copper", "Nickel steel"], 2, "Ferrous minerals contain iron; copper and bauxite do not."),
mc("The ore from which aluminium is obtained is:", ["mica", "bauxite", "limestone", "manganese"], 1, "It is a clay-like substance formed by decomposition of rocks."),
mc("The Gondwana coal fields of India are mostly situated in the:", ["Himalayas", "Damodar valley", "Thar desert", "Western coast"], 1, "Jharia, Raniganj and Bokaro are important fields."),
mc("Which of these is the lowest-grade coal, found at Neyveli in Tamil Nadu?", ["Anthracite", "Bituminous", "Lignite", "Peat"], 2, "It is soft brown coal with high moisture content."),
mc("Thorium is found in the monazite sands of:", ["Kerala", "Punjab", "Gujarat", "Assam"], 0),
mc("Which source of energy uses sunlight directly through photovoltaic technology?", ["Biogas", "Solar energy", "Geothermal energy", "Tidal energy"], 1),
W("Define a mineral and an ore.", 2,
  "A mineral is a homogeneous, naturally occurring substance with a definable internal structure (1). An ore is the accumulation of a mineral mixed with other elements (1).", "E"),
W("Name the four ranks of coal in order of increasing carbon content.", 2,
  "Peat, lignite, bituminous, anthracite. (2; one mark if only one is out of order)", "E"),
W("Fill in the blanks: Assam's oldest oil field is ______ and the most important oil field of Gujarat is ______.", 1, "Digboi; Ankleshwar. (1)", "E"),
W("True or false (with a reason): 'Minerals are renewable resources.'", 2,
  "False (1). They take millions of years to form while the rate of consumption is very high; the rate of replenishment is infinitely small (1).", "E"),
W("Match the mineral with its use: (i) Manganese (ii) Copper (iii) Mica (iv) Limestone.  A. Insulator in electrical industry  B. Cement  C. Steel-making  D. Electrical cables.", 2,
  "(i)-C, (ii)-D, (iii)-A, (iv)-B. (all four = 2; two or three correct = 1)", "E"),
W("Name any two non-conventional sources of energy.", 1, "Any two of solar, wind, tidal, geothermal, biogas, atomic energy. (1)", "E"),
W("Name two hydroelectric projects and two states in which uranium and thorium are available.", 2,
  "Hydroelectric: any two of Bhakra Nangal, Damodar Valley Corporation, Kopili Hydel Project (1). Uranium and thorium: Jharkhand and the Aravalli ranges of Rajasthan (thorium also in monazite sands of Kerala) (1).", "E"),
W("Expand HVJ and say what the pipeline links.", 2,
  "Hazira-Vijaipur-Jagdishpur (1). It is a 1,700 km pipeline linking the Mumbai High and Bassein gas fields with fertiliser, power and industrial complexes in western and northern India (1).", "E"),
W("Which two states have the largest wind farm cluster? Name its extent.", 2,
  "The largest cluster is in Tamil Nadu, from Nagercoil to Madurai (1). Nagercoil and Jaisalmer are well known for wind energy; Andhra Pradesh, Karnataka, Gujarat, Kerala, Maharashtra and Lakshadweep also have wind farms (1).", "E"),
# ------------------------------------------------------------------ MEDIUM (20)
ar("Minerals in igneous and metamorphic rocks occur as veins and lodes.", "Minerals in liquid or gaseous form are forced upward through cracks and crevices, where they cool and solidify.", 0, "Metallic minerals such as tin, copper, zinc and lead are obtained from veins and lodes.", "M"),
ar("Magnetite is regarded as the finest iron ore.", "It contains up to 70 per cent iron and has excellent magnetic qualities.", 0, "Haematite is more important in quantity but has only 50-60 per cent iron.", "M"),
W("Describe the three modes of occurrence of minerals in rocks and give one example of each.", 3,
  "In igneous and metamorphic rocks they occur in cracks, crevices, faults and joints as veins and lodes, e.g. tin, copper, zinc, lead (1). In sedimentary rocks they occur in beds or layers, e.g. coal, iron ore, gypsum, potash salt (1). By decomposition of surface rocks, leaving a residual mass of weathered material, e.g. bauxite; or as placer deposits, e.g. gold, silver (1).", "M"),
W("Differentiate between ferrous and non-ferrous minerals with two examples each.", 3,
  "Ferrous minerals contain iron; they account for about three-fourths of the total value of metallic mineral production; e.g. iron ore, manganese, nickel, cobalt (1.5). Non-ferrous minerals contain metals other than iron, e.g. copper, lead, zinc, bauxite (1.5).", "M"),
W("Name the four major iron ore belts of India with one mine or hill range of each.", 3,
  "Odisha-Jharkhand belt (Badampahar in Mayurbhanj and Kendujhar; Gua and Noamundi in Singhbhum); Durg-Bastar-Chandrapur belt (Bailadila hills); Ballari-Chitradurga-Chikkamagaluru-Tumakuru belt in Karnataka (Kudremukh); Maharashtra-Goa belt (Ratnagiri and Goa) (3, 0.75 for each belt with example).", "M"),
W("Why is the Kudremukh mine called a '100 per cent export unit'? How is its ore carried?", 2,
  "The mines in the Western Ghats of Karnataka export all their ore (1). The ore is transported as slurry through a pipeline to a port near Mangaluru (1).", "M"),
W("Manganese is called a key input for steel. If nearly 10 kg of manganese is needed to make one tonne of steel, how much manganese is needed for a plant making 600 tonnes of steel in a day? Name two other uses of manganese.", 3,
  "600 x 10 kg = 6,000 kg = 6 tonnes per day (2). Bleaching powder, insecticides and paints (any two) (1).", "M", wp=True),
W("Locate and name (on a map) the bauxite regions of India. Which state is the largest producer, and which deposit is the most important there?", 3,
  "Amarkantak plateau, Maikal hills and the Bilaspur-Katni plateau region (1). Odisha was the largest producer (2018-19) (1). Panchpatmali deposits in Koraput district (1).", "M"),
W("Give any three uses of mica and name three mica-producing areas.", 3,
  "Mica is an excellent insulator with resistance to high voltage and is used in electrical and electronic industries (1.5, any three uses or properties). Koderma-Gaya-Hazaribagh belt of Jharkhand (leading), Ajmer in Rajasthan, Nellore in Andhra Pradesh (1.5).", "M"),
W("Explain why limestone is called a key raw material of the cement industry and where else it is used.", 2,
  "It is found with calcium carbonate rocks in sedimentary formations and is the basic raw material for cement (1). It is also essential for smelting iron ore in the blast furnace (1).", "M"),
W("Locate the Damodar valley coalfields on a map and name three coal fields. Why is Damodar valley called the main source of metallurgical coal?", 3,
  "Damodar valley in Jharkhand and West Bengal: Jharia, Raniganj and Bokaro (2). It has the major resources of Gondwana coal, which is metallurgical coal needed for the blast furnaces of the iron and steel industry (1).", "M"),
W("Differentiate between Gondwana coal and tertiary coal on age and location.", 2,
  "Gondwana coal is a little over 200 million years old and found in the Damodar, Godavari, Mahanadi, Son and Wardha valleys (1). Tertiary coal is about 55 million years old and found in the north-eastern states of Meghalaya, Assam, Arunachal Pradesh and Nagaland (1).", "M"),
W("How is petroleum found in rock formations? Name the three major petroleum-producing regions of India.", 3,
  "Mostly in anticlines and fault traps in tertiary rock formations; in folded regions, oil collects in the crest of upfolds, and gas, being lighter, usually occurs above the oil (2). Mumbai High, Gujarat and Assam (1).", "M"),
W("'Petroleum refineries act as a nodal industry.' Explain with two examples.", 2,
  "Refineries supply raw material to a number of industries (1), such as synthetic textiles, fertilisers and numerous chemicals; petroleum also gives fuel for heat, lighting and lubricants (1).", "M"),
W("Why are CNG and PNG called cleaner fuels and why is natural gas called 'the fuel of the future'? Name two areas of large reserves.", 3,
  "Natural gas is used as a domestic and industrial fuel and is fast becoming a preferred transport fuel (CNG) and cooking fuel (PNG); it releases less pollution than coal or oil (2). Large reserves: Mumbai High and the west coast, Cambay basin, Krishna-Godavari basin on the east coast (1).", "M"),
W("Describe how the working of a tidal power plant uses floodgate dams.", 3,
  "Floodgate dams are built across inlets (1). During high tide, water flows into the inlet and gets trapped when the gate is closed (1). After the tide falls outside, the retained water flows back to the sea through a pipe that carries it past a power-generating turbine (1).", "M"),
W("A family in rural Jaisalmer uses dung cake and firewood for cooking. Suggest two non-conventional alternatives with a benefit of each.", 3,
  "Biogas (gobar gas plant): gives twin benefits of energy and improved-quality manure and has higher thermal efficiency than dung cake or kerosene (1.5). Solar energy: ample sunshine in a tropical country; photovoltaic cells or solar cooker reduce dependence on firewood and dung cake and also save forests (1.5).", "M", wp=True),
W("Where in India are geothermal and tidal energy possibilities being tapped? Name two sites each.", 3,
  "Geothermal: Parvati valley near Manikaran in Himachal Pradesh and Puga Valley in Ladakh (1.5). Tidal: Gulf of Khambhat, Gulf of Kuchchh (Gujarat) and Sunderban in West Bengal (1.5).", "M"),
W("Error analysis. A student writes: 'India is rich in copper and exports it all over the world. Odisha produces the most copper.' Identify the errors.", 2,
  "India is critically deficient in the reserve and production of copper (1). The leading producers are the Balaghat mines in Madhya Pradesh, Khetri in Rajasthan and Singhbhum district of Jharkhand, not Odisha (1).", "M"),
W("Study the table. Fuel / Share: Wood and dung cake - more than 70% of rural household energy.  (i) What do these two sources show about rural India? (ii) Give two problems with using dung cake and firewood.", 3,
  "(i) Rural households depend largely on firewood and cattle dung cake as everyday energy (1). (ii) Forests are decreasing, so firewood is difficult to get; dung cake consumes valuable manure that could improve the soil (2).", "M"),
# ------------------------------------------------------------------ HARD (13)
W("Explain how uneven distribution of minerals affects the economy of India. Support with the example of the peninsular plateau and the northern plains.", 4,
  "Peninsular rocks contain most of the reserves of coal, metallic minerals, mica and many non-metallic minerals; the sedimentary rocks of the western and eastern flanks have limestone and petroleum in Gujarat and Assam (1.5). The vast alluvial plains of north India are almost devoid of economic minerals (1). So industries cluster around Chota Nagpur and similar regions, while other regions must import raw material, transport costs rise and regional development becomes uneven (1.5).", "H"),
W("Assertion (A): Odisha, Chhattisgarh, Karnataka and Jharkhand together produce almost all of India's iron ore.  Reason (R): Iron ore belts lie in the old peninsular rocks. State whether A and R are true and whether R explains A. Quote the share given in the text.", 3,
  "Both are true (1). About 97 per cent of iron ore production in 2018-19 came from these four states, the rest (3 per cent) from other states (1). The main belts (Odisha-Jharkhand, Durg-Bastar-Chandrapur, Ballari-Chitradurga belt) lie in the peninsular rocks, so R explains A (1).", "H"),
W("Read the extract. 'The dust and noxious fumes inhaled by miners make them vulnerable to pulmonary diseases. The risk of collapsing mine roofs, inundation and fires in coalmines are a major threat to the miners.'  (i) Whom does this affect? (ii) Name two other effects of mining on the environment. (iii) Suggest two remedies.", 4,
  "(i) The miners (1). (ii) Pollution of water sources and rivers by waste and slurry, dumping of waste, land degradation and soil erosion (1.5, any two). (iii) Safety measures, wet drilling and masks, proper disposal of waste, reclamation of land and planned and sustainable use of minerals (1.5, any two).", "H"),
W("Compare conventional and non-conventional sources of energy on four points: examples, availability, effect on environment and cost or use.", 4,
  "Conventional: firewood, dung cake, coal, petroleum, natural gas, electricity (hydel and thermal); limited, exhaustible fossil fuels; coal and oil burning pollutes the air; widely used but rising prices (2). Non-conventional: solar, wind, tidal, geothermal, biogas, atomic; mostly renewable and abundant in a tropical country with sun, wind and biomass; eco-friendly and cleaner; need technology and investment but reduce dependence on fossil fuels (2).", "H"),
W("Case study. In 2022, four families in a Barmer village each installed a 'gobar gas plant' and two solar panels. Cooking fuel cost earlier was Rs 900 a month per family in LPG and wood. Now each saves 60 per cent of this cost. (i) Compute the yearly saving of one family. (ii) Which two sources are used? (iii) Give two benefits besides money.", 4,
  "(i) Saving per month = 60% of 900 = Rs 540; per year = 540 x 12 = Rs 6,480 (1.5). (ii) Biogas and solar energy (1). (iii) Fewer trees cut and less smoke; the slurry gives improved manure for the farm (1.5, any two).", "H", wp=True),
W("Evaluate the claim: 'Energy saved is energy produced.' Give four measures that individuals and the nation can adopt, with a reason for each.", 4,
  "Using public transport instead of private vehicles cuts fuel use and pollution (1). Switching off electrical devices when not needed saves electricity (1). Using power-saving devices such as LED bulbs lowers consumption (1). Shifting to non-conventional sources reduces dependence on exhaustible fossil fuels (1).", "H"),
W("Electricity saving problem. A school in Jaipur replaces 40 tube-lights of 60 watts with LED panels of 20 watts. The lights burn 6 hours a day for 25 school days a month. Find the energy saved in kilowatt-hours a month and the money saved if one unit costs Rs 8.", 4,
  "Saving per light = 60 - 20 = 40 W; for 40 lights = 1,600 W = 1.6 kW (1). Energy saved per day = 1.6 x 6 = 9.6 kWh (1). Per month = 9.6 x 25 = 240 kWh (1). Money = 240 x 8 = Rs 1,920 (1).", "H", wp=True),
W("Why should conservation of mineral resources be given priority in India? Explain the three measures suggested in the text.", 4,
  "Mineral resources are finite and non-renewable; they take millions of years to form and are being used up quickly (1). Planned and sustainable use of minerals is essential (1). Improved technologies should allow the use of low-grade ores at low cost (1). Recycling of metals and use of scrap metals and substitutes help to reduce waste (1).", "H"),
W("Study the statement: 'Hematite ore is the most important industrial iron ore in terms of quantity, but magnetite is the finest.' (i) Give the iron content of each. (ii) Why is magnetite valuable in the electrical industry? (iii) Name one state where each is mined.", 4,
  "(i) Magnetite up to 70 per cent; hematite 50 to 60 per cent (1.5). (ii) It has excellent magnetic qualities (1). (iii) Hematite: Odisha (Badampahar) or Chhattisgarh (Bailadila); magnetite: Karnataka (Kudremukh) (1.5).", "H"),
W("Describe how electricity is generated in thermal and hydel power stations and say why a hydel project like Bhakra Nangal is called multipurpose.", 5,
  "Hydel: running water turns turbines (renewable); Bhakra Nangal, Damodar Valley Corporation and Kopili are examples (1.5). Thermal: coal, petroleum and natural gas are burnt to produce steam to turn turbines; these are non-renewable fossil fuels (1.5). Multi-purpose projects serve irrigation, flood control and electricity generation at the same dam, so a single project meets several needs (2).", "H"),
W("Mark and explain on an outline map of India the nuclear power stations. Name six stations with their states and the minerals used.", 5,
  "Tarapur (Maharashtra), Rawatbhata (Rajasthan), Kalpakkam (Tamil Nadu), Narora (Uttar Pradesh), Kakrapar (Gujarat), Kaiga (Karnataka) (3). They use uranium and thorium: uranium and thorium are available in Jharkhand and the Aravalli ranges of Rajasthan and thorium in the monazite sands of Kerala; energy is produced by altering the structure of atoms, releasing heat to generate electricity (2).", "H"),
W("Why is the spread of coal important for the industrial map of India? Give three reasons using Damodar valley and the iron and steel industry.", 4,
  "Coal is the most abundant fossil fuel and a main source for power generation and industry (1). Metallurgical Gondwana coal of the Damodar valley and iron ore of Odisha-Jharkhand lie close together, which led to steel centres in the region (1.5). Because coal is bulky, industries locate near coalfields to cut transport cost (1.5).", "H"),
W("'Solar and wind energy suit Rajasthan better than coal.' Examine with three arguments and one limitation.", 4,
  "Rajasthan is a tropical, sunny state with large desert areas available for solar plants and wind potential at places like Jaisalmer (1.5). Both are renewable and do not pollute, reducing the pressure on fossil fuels (1). They can supply remote rural households where power lines do not reach, reducing the use of firewood and dung cake (1). Limitation: high initial cost and dependence on weather and sunshine hours (0.5).", "H"),
]

def _sub(x, pairs):
    if isinstance(x, str):
        for a, b in pairs: x = x.replace(a, b)
        return x
    if isinstance(x, (list, tuple)): return type(x)(_sub(i, pairs) for i in x)
    return x
_old = runpy.run_path(str(REPO / "src/rn_work/c10_sst/c10.py"))["CH"]
_i = max(k for k, b in enumerate(_old["blocks"]) if b[0] == "h2")
_PAIRS = [("about 60% iron", "50-60% iron"), ("(most important in quantity, about 60% iron)", "(most important in quantity, 50-60% iron)"),
          ("About 63 per cent of India's production is from **Mumbai High**, 18 per cent from Gujarat and 16 per cent from Assam.", "Major producing areas are **Mumbai High**, Gujarat and Assam."),
          ("The **Bhuj** (Gujarat) plant is an important solar plant. ", ""), ("**HBJ pipeline** links Hazira (Gujarat), Bijaipur (Madhya Pradesh) and Jagdishpur (Uttar Pradesh)", "**HVJ pipeline** (1,700 km) links Hazira (Gujarat), Vijaipur (Madhya Pradesh) and Jagdishpur (Uttar Pradesh) with Mumbai High and Bassein"),
          ("Odisha is the leading producer", "Mainly an input for steel-making"), ("**Odisha** leads in manganese and bauxite", "**Odisha** leads in bauxite"), ("�", "'")]
_core = _sub(_old["blocks"][:_i], _PAIRS)
_extra = [
 ("h2", "Fuel Minerals and Energy: Grouping"),
 ("table", ["Type", "Examples", "Key facts"], [
  ["Conventional", "Firewood, cattle dung cake, coal, petroleum, natural gas, electricity (hydel and thermal)", "Firewood and dung cake meet more than 70 per cent of rural household energy needs; fossil fuels are exhaustible"],
  ["Non-conventional", "Solar, wind, tidal, geothermal, biogas, atomic", "Renewable and clean; India has abundant sunlight, water, wind and biomass"],
  ["Hydro / Thermal / Nuclear electricity", "Bhakra Nangal, Damodar Valley Corporation, Kopili / coal, oil and gas based / uranium and thorium", "Hydel uses a renewable resource; thermal uses non-renewable fossil fuels"]]),
 ("h2", "Where to Find What: Distribution Summary"),
 ("table", ["Mineral", "Leading areas", "Remember"], [
  ["Iron ore", "Odisha-Jharkhand, Durg-Bastar-Chandrapur, Ballari-Chitradurga belt, Maharashtra-Goa belt", "97 per cent of output (2018-19) from Odisha, Chhattisgarh, Karnataka, Jharkhand; Bailadila hills look like the hump of an ox"],
  ["Manganese", "Used for steel and ferro-manganese", "About 10 kg per tonne of steel"],
  ["Copper", "Balaghat (Madhya Pradesh), Khetri (Rajasthan), Singhbhum (Jharkhand)", "India is critically deficient in copper"],
  ["Bauxite", "Amarkantak plateau, Maikal hills, Bilaspur-Katni; Odisha largest; Panchpatmali (Koraput)", "Clay-like; ore of aluminium"],
  ["Mica", "Koderma-Gaya-Hazaribagh (Jharkhand), Ajmer (Rajasthan), Nellore (Andhra Pradesh)", "Insulator"],
  ["Coal", "Damodar valley (Jharia, Raniganj, Bokaro), Godavari, Mahanadi, Son and Wardha valleys; tertiary coal in the north-east", "Gondwana: a little over 200 million years; tertiary: about 55 million years"],
  ["Petroleum", "Mumbai High, Gujarat (Ankleshwar), Assam (Digboi, Naharkatiya, Moran-Hugrijan)", "Assam is the oldest oil-producing state"],
  ["Wind farms", "Nagercoil to Madurai in Tamil Nadu; Jaisalmer", "Largest cluster is in Tamil Nadu"]]),
 ("h2", "Hazards of Mining"),
 ("ul", ["Dust and noxious fumes inhaled by miners cause **pulmonary (lung) diseases**.",
  "There are risks of collapsing mine roofs, flooding (inundation) and fires in coal mines.",
  "Mining pollutes rivers and water sources, and wastes and slurry damage land and soil; so planned, sustainable extraction and safe disposal are needed."]),
 ("h2", "Map Pointers"),
 ("ul", ["Mark **Badampahar (Mayurbhanj, Odisha), Gua and Noamundi (Singhbhum), Bailadila (Bastar), Kudremukh (Karnataka)** and the ports **Marmagao** and **Mangaluru** linked to iron ore exports.",
  "Locate coalfields **Jharia, Raniganj, Bokaro** (Damodar valley) and lignite at **Neyveli** (Tamil Nadu).",
  "Mark oil fields **Digboi** (Assam), **Ankleshwar** (Gujarat) and the offshore **Mumbai High**; trace the **HVJ pipeline**.",
  "Nuclear power stations: **Tarapur, Rawatbhata, Kalpakkam, Narora, Kakrapar, Kaiga**."]),
 ("h2", "Cause and Effect Chains"),
 ("table", ["Cause", "Effect"], [
  ["Different geological structure and time of formation", "Uneven distribution of minerals; the northern alluvial plains have almost none"],
  ["Rapid consumption and negligible replenishment", "Minerals and fossil fuels are finite, so conservation is vital"],
  ["Rising oil and gas prices and decreasing forests", "Need for solar, wind, biogas and other non-conventional sources"],
  ["Use of dung cake as fuel", "Valuable manure is lost; biogas gives both energy and manure"]]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "**Magnetite** is the *finest* ore (up to 70 per cent iron) but **haematite** is the *most important in quantity* (50-60 per cent iron). Do not interchange them."),
 ("note", "REMEMBER", "Coal order by quality: **peat, lignite, bituminous, anthracite**. Neyveli is lignite, not anthracite. The Damodar valley belongs to **Gondwana** coal, while the north-eastern coal is **tertiary** and younger."),
 ("h2", "Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Why is it necessary to conserve mineral resources? How can it be done? (5)", "Minerals are finite, non-renewable and take millions of years to form; consumption is rapid. Conservation: planned and sustainable use, improved technology for low-grade ores, recycling, and substitutes. In energy: public transport, switching off devices, power-saving devices and non-conventional sources."),
  ("How are minerals formed or found in rocks? (3)", "Veins and lodes in igneous and metamorphic rocks; beds or layers in sedimentary rocks; residual mass by decomposition (bauxite); placer deposits in valley floor sands; ocean waters (common salt, magnesium, bromine)."),
  ("Describe the importance of iron ore and name its belts. (3)", "It is the basic mineral and backbone of industrial development; belts: Odisha-Jharkhand, Durg-Bastar-Chandrapur, Ballari-Chitradurga-Chikkamagaluru-Tumakuru, Maharashtra-Goa."),
  ("Describe solar energy potential in India. (3)", "India is tropical with enormous solar potential; photovoltaic technology converts sunlight directly into electricity; solar energy is becoming popular in rural and remote areas, reducing dependence on firewood and dung cakes."),
  ("What is meant by biogas and gobar gas plants? (3)", "Organic waste (shrubs, farm waste, animal and human waste) decomposes to yield gas with higher thermal efficiency than kerosene, dung cake and charcoal; plants using cattle dung are 'gobar gas plants' and give energy and improved manure."),
 ]),
]
CH = dict(num=10, title=_old["title"], tag=_old["tag"], intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_core + _extra, takeaways=_sub(_old["takeaways"], _PAIRS) + ["Mineral distribution is uneven: the peninsular rocks hold most metals and coal, the northern plains hold almost none.", "Mining brings hazards to miners and to the environment, so extraction must be planned and sustainable."])

if __name__ == "__main__": run(__file__, BANK, 10, "Social_Science", WS, CH)
