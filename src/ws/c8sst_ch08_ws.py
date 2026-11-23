"""Class 8 Social Science Part 2 Ch 1 (bank ch08) - Understanding the World through Maps and Landforms: worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c8sst_ch08"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("On a physical map, plains are usually shown in:", ["blue", "green", "dark brown", "light yellow"], 1, "Blue is water, yellow/brown plateaus, dark brown high mountains, light yellow deserts."),
mc("The projection that keeps shape and direction and is useful for navigation is the:", ["Robinson projection", "Mercator projection", "Polar projection", "Globe projection"], 1),
mc("The deepest part of the ocean, the Challenger Deep, lies in the:", ["Puerto Rico Trench", "Mariana Trench", "Java Trench", "Atlantic Ridge"], 1, "More than 11,000 m below sea level."),
mc("The Gulf Stream makes the United Kingdom warmer because it:", ["is a cold current", "brings warm water from near the Equator", "blocks the winds", "melts glaciers"], 1),
mc("The highest and largest plateau on Earth is the:", ["Deccan Plateau", "Colorado Plateau", "Tibetan Plateau", "Mongolian Plateau"], 2),
mc("The longest river in the world, according to the chapter, is the:", ["Amazon", "Nile", "Yangtze", "Rhine"], 1, "About 6,650 km."),
mc("Which desert is the largest hot desert in the world?", ["Gobi", "Atacama", "Sahara", "Great Victoria"], 2),
W("Fill in the blank: The Earth is an ______ spheroid, so every flat map has some distortion.", 1, "oblate. (1)", "E"),
W("What is a map projection? Name two projections in the chapter.", 2, "The process of showing the Earth on a flat surface (1). Mercator and Robinson (1).", "E"),
W("Name the five oceans.", 2, "Pacific, Atlantic, Indian, Arctic and Southern (5 correct = 2; 3-4 = 1).", "E"),
W("True or false, with a reason: 'The Great Barrier Reef is in the Atlantic Ocean.'", 2, "False (1). It lies off Australia's north-eastern coast, in the Pacific side (Coral Sea), and is a UNESCO World Heritage Site (1).", "E"),
W("Define (i) a gulf (ii) a strait (iii) a canal with one example each.", 3 if False else 2, "Gulf: large inlet of the sea cutting deeply into land, e.g. Persian Gulf. Strait: narrow channel joining two seas or oceans. Canal: man-made channel, e.g. Suez Canal. (Any two correct with examples = 2; three correct definitions = 2)", "E"),
W("Match: (i) Aconcagua (ii) Uyuni (iii) Mont Blanc (iv) Old Faithful. Options: A. largest salt flat  B. highest peak in the Western Hemisphere  C. geyser at Yellowstone  D. famous peak of the Alps.", 2, "(i)-B, (ii)-A, (iii)-D, (iv)-C. (4 correct = 2; 2-3 = 1)", "E"),
W("Oceans cover about 71 per cent of the Earth's surface. What percentage is land?", 2, "100 - 71 = 29 per cent (2).", "E", wp=True),
W("The Tibetan Plateau is about 2,500 km from east to west and 1,000 km from north to south. Using length x breadth, estimate its area, and say how it compares with the Colorado Plateau (over 330,000 sq km).", 2, "2,500 x 1,000 = 25,00,000 sq km (about 2.5 million) (1). It is more than seven times the Colorado Plateau (about 7.6 times) (1).", "E", wp=True),
W("Why are mountains called 'water towers'?", 2, "Snow and glaciers on them melt to supply fresh water to rivers (2).", "E"),
W("Name two animals adapted to the Sahara and one adaptation each.", 2, "Fennec fox: large ears dissipate heat and hear underground prey (1). Camel / cactus (plant): camels in desert nomadic life; cacti store water in leaves (1).", "E"),
W("Antarctica covers over 14 million sq km, 'more than four times the area of India'. If India is about 3.3 million sq km, check this claim.", 2, "4 x 3.3 = 13.2 million, which is less than 14 million (1). So the claim is correct (1).", "E", wp=True),
# ------------------------------------------------------------------ MEDIUM (19)
W("Why do all map projections have some amount of distortion (NCERT Q.1)? Use the orange peel example.", 3, "The Earth is a nearly spherical oblate spheroid (1). Just as an orange peel cannot be laid flat without tearing, the curved surface cannot be flattened without stretching shape, size or direction (1). So every map is a compromise and we should look at multiple projections (1).", "M"),
W("Compare the Mercator and Robinson projections in three points.", 3, "Mercator preserves shape and direction, helps navigation (1); distorts size near the poles, Greenland looks as big as Africa (1). Robinson balances size and shape distortion and looks realistic (1).", "M"),
W("Read the extract and answer. 'Oceans give us almost half the oxygen we breathe. Tiny marine organisms, such as plankton, make this possible.'  (i) What are plankton? (ii) How do they make oxygen? (iii) What would pollution of plankton cause?", 3, "(i) Very small organisms that float on water (1). (ii) By making food through photosynthesis (1). (iii) Less oxygen for living beings and harm to marine food chains (1).", "M"),
W("How do the oceans help regulate the Earth's climate (NCERT Q.4)?", 3, "They absorb heat and release it slowly (1). They add moisture to the air, forming clouds and rainfall (1). Ocean currents carry warm or cold water to coasts, e.g. the Gulf Stream warming the UK (1).", "M"),
W("Describe the Mariana Trench and the life found there.", 3, "A V-shaped deep area, the deepest trench; Challenger Deep over 11,000 m below sea level, deeper than the height of Mount Everest (1.5). No light, near-freezing temperature and high pressure; organisms get energy from chemicals in water instead of photosynthesis (1.5).", "M"),
W("Why are coral reefs called the 'rainforests of the sea' (NCERT Q.3)?", 3, "They are among the most diverse ecosystems on Earth (1). They provide food and shelter for about one-quarter of all ocean species such as fish, crabs, turtles and sponges (1). Like rainforests on land they are rich in life and under threat (1).", "M"),
W("What is the main reason for the Great Barrier Reef facing threats today (NCERT Q.5)? Give details.", 3, "Human activities: climate change, pollution and overfishing (1). Bleaching occurs because of changes in the chemical composition of ocean water, largely human-caused (1). The death of coral destroys habitat for many species (1).", "M"),
W("Give three facts about the Great Barrier Reef.", 3, "Off Australia's north-east coast (1); about 2,000 km long, covering about 350,000 sq km (1); hundreds of coral species, thousands of fish species, UNESCO World Heritage Site (1).", "M"),
W("Why is the Bay of Bengal important? Give three points.", 3, "World's largest bay (1). Important for trade (1). Influences climate and is home to varied flora and fauna; bays give safe havens to ports (1).", "M"),
W("Why is the Suez Canal significant for India? When did it open?", 2, "It opened in 1869 and links the Red Sea with the Mediterranean (1). It is the shortest sea route from India to Europe (1).", "M"),
W("Why is the Tibetan Plateau called the 'Third Pole' and 'Roof of the World' (NCERT Q.2)?", 3, "Average height over 4,500 m, highest plateau (1). It has the largest freshwater reserves outside the polar regions (1). It is source of the Indus, Brahmaputra and Yangtze; formed by collision of Indo-Australian and Eurasian plates (1).", "M"),
W("Describe the Gobi Desert and explain why Mongolia is called the 'Land of the Eternal Blue Sky'.", 3, "A desert in Mongolia (part in north China) with sparse vegetation and herds moving seasonally (1). About 8 to 9 months of sunny weather (1). Winter temperatures can drop to minus 30 degrees C (1).", "M"),
W("Explain why the steppes are called a 'global carbon sink'.", 2, "Steppe grassland absorbs carbon from the air and stores it underground (1), which helps reduce greenhouse effects over time; it is also a resting spot for migratory birds like the Siberian crane (1).", "M"),
W("Describe the Ural Mountains in four facts.", 3, "About 2,500 km, ancient range from the Arctic Ocean to Kazakhstan (1); natural boundary between Europe and Asia (1); rich in iron ore, copper, zinc, platinum, gold, coal, oil and gas; taiga, tundra and deciduous forests (1).", "M"),
W("Why is the European Plain productive and populous?", 3, "Fertile soil from sediment grows wheat, barley, rye and potatoes (1). Rivers help trade and transport; coal, oil and gas support the economy (1). Flat land and favourable climate support cities like Moscow, Berlin, Paris and Amsterdam (1).", "M"),
W("List three uses of the Alps to people in Europe.", 3, "Tourism: skiing and hiking (1). Water for rivers like the Rhine and for drinking, irrigation and hydroelectric power (1). Minerals such as iron, copper, lead and rock salt; forests and farmland (1).", "M"),
W("How have people and animals adapted to the Sahara? Give three examples.", 3, "Underground dwellings stay cool in summer and warm in winter; nomads' clothing and headgear keep the body cool (1); date palms in oases give food (1); cacti store water and the fennec fox's large ears release heat (1).", "M"),
W("Why was the Nile the 'cradle' of Egyptian civilisation? Give three points.", 3, "Irrigation turned dry land into fertile farmland for wheat, barley, flax, fruits and vegetables (1.5). It gave drinking water and fish and hydroelectric power (1). It served as a transport route for centuries (0.5).", "M"),
W("Why is the Andes a 'conservation hotspot'? What resources lie there?", 3, "Only about one-fourth of the original flora and fauna remains (1.5). It holds copper, zinc, silver and lithium; feeds the Amazon and gives freshwater to millions (1.5).", "M"),
# ------------------------------------------------------------------ HARD (14)
W("Why is the Amazon called the 'Lungs of the Earth' (NCERT Q.6)? Explain two threats it faces and one global effect.", 4, "Its vast forest produces oxygen and absorbs carbon dioxide (1). Supports about 400 indigenous communities who conserve it (0.5). Threats: deforestation and climate change (1). Global effect: loss of oxygen and carbon storage raises climate change; even Sahara dust brings phosphorus to the Amazon (1.5).", "H"),
W("Choose one environmental issue (deforestation, coral bleaching or desertification) and explain causes, impacts and solutions (NCERT Q.9).", 5, "Model (coral bleaching): causes: warming oceans, pollution, overfishing (1.5). Impacts: loss of habitat for about one-quarter of ocean species, fall in fish, tourism and coastal protection (1.5). Solutions: cut emissions, reduce pollution, limit fishing, protect reefs and restore corals (2).", "H"),
W("The Atacama Desert is one of the driest places on Earth, yet it is in the news. Explain two reasons.", 3, "Clear night skies make it famous for stargazing; its Mars-like landscape is used by NASA to test rovers (1.5). It has become one of the fastest-growing dumps for discarded fast-fashion clothes, called an environmental and social emergency by the UN (1.5).", "H"),
W("Explain with the Yellowstone example how restoration of ecosystems can work.", 3, "Elk overgrazed and upset the balance (1). In 1995 wolves, a predator, were introduced and hunted elk, reducing their numbers (1). Flora returned and ecological balance was restored (1).", "H"),
W("Case study: Maria's family live near the Great Lakes. Her town draws drinking water from the lake but farms nearby use fertilisers. Using the chapter, explain two benefits of the lakes and two problems she should worry about.", 4, "Benefits: shipping routes for commerce and industry; drinking water for many cities; habitat for wildlife (2). Problems: chemical contamination of sediments and agricultural run-off and industrial processes contaminating water (2).", "H", wp=True),
W("Compare a hot desert (Sahara) and a cold desert (Gobi/Antarctica) on four points.", 4, "Sahara: largest hot desert, temperatures 30-46 degrees C, rainfall below 25 cm, nomads with camels (2). Gobi: sunny 8-9 months, winters down to minus 30 degrees C, seasonal herding; Antarctica: largest desert (over 14 million sq km), coldest, more than four times India's area (2).", "H"),
W("Trace the journey from the Ural Mountains westward: describe the landforms met in Europe and why each matters. Give four details.", 4, "Urals: boundary between Europe and Asia, minerals (1). European Plain: fertile, farming and cities (1). Alps: crescent-shaped barrier, source of rivers, tourism and hydro power (1). Rivers like the Rhine and Danube link trade and transport (1).", "H"),
W("How do landforms influence human settlement, farming and trade? Give an example for each from the chapter.", 4, "Settlement: European Plain cities, Nile valley (1.3). Farming: fertile plains of Europe, Nile irrigation (1.3). Trade: Alpine rivers, Great Lakes shipping, Suez Canal, Persian Gulf (1.4).", "H"),
W("Imagine you are advising a government to protect one major landscape in your country (NCERT Q.10). Name one (e.g. Western Ghats, Himalayas, Thar), state why it matters and two protection steps.", 4, "Choice with reasons: biodiversity, water, culture (2). Steps: protect forests and prevent over-extraction of resources; sustainable tourism and community involvement (2).", "H", wp=True),
W("Using the chapter, explain how human actions can trigger desertification, biodiversity loss and climate change.", 4, "Deforestation removes plant cover and soil protection, leading to desertification (1.5). Overuse of resources and pollution harm species and ecosystems, such as reefs and the Andes, causing biodiversity loss (1.5). Burning fuels and clearing forests raise greenhouse gases and temperatures, causing climate change (1).", "H"),
W("Pitch a road trip across two continents (NCERT Q.11). Name them, two stops in each and what the group will learn at each stop.", 5, "Any well-reasoned plan, e.g. Africa (Sahara, Nile) and South America (Andes, Amazon), with correct features and learning at each stop (1 for each stop, 1 for pitch and reasons).", "H", wp=True),
W("Puzzle: Identify. (i) 'I am a man-made channel opened in 1869.' (ii) 'I am the bird that rests on the steppes.' (iii) 'I am an artist's hand in a Chilean desert.' (iv) 'I was introduced to Yellowstone in 1995.'", 3, "(i) Suez Canal (ii) Siberian crane (iii) The sculpted hand in the Atacama Desert (iv) Wolves. (4 right = 3; 3 = 2; 2 = 1)", "H"),
W("Evaluate: 'Every map is a compromise.' Explain what this means and how we should use maps (NCERT).", 3, "No projection can show shape, size, direction and distance all correctly (1). Different maps suit different purposes: Mercator for navigation, Robinson for a realistic view (1). We should consult multiple projections and use latitude and longitude for precise location (1).", "H"),
]

_old = runpy.run_path(str(REPO / "src/rn_work/c8_sst2/c08.py"))["CH"]
_blocks = list(_old["blocks"])
_i = max(k for k, b in enumerate(_blocks) if b[0] == "h2")      # keep through 'Humans and the Environment'
_extra = [
 ("h2", "Key Facts and Figures at a Glance"),
 ("table", ["Feature", "Key figures"], [
  ["Oceans", "71% of the Earth's surface; 97% of Earth's water; about half the oxygen from plankton"],
  ["Mariana Trench", "Challenger Deep over 11,000 m below sea level"],
  ["Great Barrier Reef", "About 2,000 km long; about 350,000 sq km; UNESCO World Heritage Site"],
  ["Suez Canal", "Opened 1869; Red Sea to Mediterranean"],
  ["Tibetan Plateau", "About 2,500 km by 1,000 km; average height over 4,500 m"],
  ["Steppes", "Over 8,000 km west to east"],
  ["Ural Mountains", "About 2,500 km"],
  ["Alps", "About 1,200 km, crescent-shaped"],
  ["Nile", "About 6,650 km"],
  ["Atacama Desert", "About 1,000 km; 40 degrees C by day, 5 degrees C at night"],
  ["Colorado Plateau", "Over 330,000 sq km; about 5 million visitors a year to the Grand Canyon"],
  ["Rockies", "About 4,800 km"],
  ["Antarctica", "Over 14 million sq km, more than four times India"],
  ["Deserts overall", "About one-fifth of the land area; about one billion people live there"]]),
 ("h2", "Cause and Effect, and Case Notes"),
 ("table", ["Cause", "Effect"], [
  ["Collision of Indo-Australian and Eurasian plates", "Himalayas and the Tibetan Plateau formed"],
  ["Snow-melt on Tibetan Plateau and mountains", "Rivers such as Indus, Brahmaputra, Yangtze"],
  ["Warm Gulf Stream", "United Kingdom warmer than other places at the same latitude"],
  ["Ocean chemistry change from human actions", "Coral bleaching and loss of habitat"],
  ["Deforestation and climate change", "Threat to the Amazon and its indigenous communities"],
  ["Fast fashion", "Atacama becomes a dump for discarded clothes"],
  ["Overgrazing by elk, then wolves reintroduced", "Yellowstone's ecological balance restored"]]),
 ("ul", ["**Case: Yellowstone (1995).** Introducing a predator restored the balance: a lesson in ecosystem restoration.",
  "**Case: Sahara dust and the Amazon.** Dust travels from the Sahara to the Amazon carrying phosphorus the plants need, showing how distant places are linked.",
  "**Case: Southern Indian Ocean and the monsoon.** It influences the monsoon in the Gangetic Plains, showing our link to distant oceans.",
  "**Case: Tibetan Plateau satellite pictures (1987 and 2021).** Snow-melt has expanded existing lakes and created new ones.",
  "**Map reading:** physical maps use blue for water, green for plains, yellow-brown for plateaus, dark brown for high mountains and light yellow for deserts; read colours before reading labels."]),
 ("h2", "Map Pointers and Common Mistakes"),
 ("ul", ["Mark the five oceans, the Mariana Trench, the Great Barrier Reef, the Gulf Stream, the Persian Gulf, the Bay of Bengal and the Suez Canal.", "Mark the Tibetan Plateau, Gobi, Steppes, Urals, European Plain, Alps, Sahara, Savannah, Nile, Andes, Amazon, Atacama, Colorado Plateau, Rockies, Appalachians, Great Lakes and the Great Australian Desert on a world map.", "Locate Aconcagua (Andes), Uyuni salt flat (Bolivia) and Mont Blanc (Alps)."]),
 ("note", "REMEMBER", "A desert is defined by low precipitation (under 25 cm a year), not by heat: the Gobi and Antarctica are cold deserts. The Mercator map exaggerates size near the poles, so Greenland looks as large as Africa; in fact Greenland is smaller than India. Taiga lies in the north, steppes are grasslands, savannahs are tropical grasslands."),
]
CH = dict(num=8, title="Understanding the World through Maps and Landforms", tag="Geography (Part 2, Ch 1)",
          intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_blocks + _extra, takeaways=_old["takeaways"] + [
              "Mountains act as water towers and climate shapers; plains and river valleys support farming and cities.",
              "Ecosystems such as the Amazon, coral reefs and the Andes are fragile; restoration, as at Yellowstone, shows recovery is possible."])

if __name__ == "__main__": run(__file__, BANK, 8, "Social_Science", WS, CH)
