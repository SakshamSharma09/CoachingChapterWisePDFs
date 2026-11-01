from h import *
META = meta(3, "Set 03")
A = [
 m("The three main types of rocks are:", "igneous, sedimentary and metamorphic", ["granite, basalt and marble", "crust, mantle and core", "alluvial, black and red"], "Classification by origin."),
 m("Which of the following is an example of a metamorphic rock?", "Marble", ["Granite", "Sandstone", "Basalt"], "Marble forms from limestone under heat and pressure."),
 m("The layer of the Earth between the crust and the core is the:", "mantle", ["atmosphere", "hydrosphere", "biosphere"], "Thick, hot, semi-molten in parts."),
 ar("The temperature of the Earth's surface decreases from the equator towards the poles.", "The Sun's rays fall more obliquely at higher latitudes.", 'a', "Oblique rays spread over a larger area, giving less heat."),
 m("Land breeze blows:", "from land to sea at night", ["from sea to land at night", "from land to sea in the daytime", "only in winter"], "Land cools faster than the sea at night."),
 m("The air pressure on a mountaintop is lower than at sea level because:", "the air above is thinner", ["the air is hotter", "the winds are stronger", "the sun is nearer"], "Pressure decreases with altitude."),
 st("The Indian monsoon is the seasonal reversal of winds.", "The south-west monsoon brings most of India's annual rainfall.", True, True, "Winds reverse seasonally; SW monsoon (June–Sept) gives bulk of the rain."),
 m("In economics, a ‘want’ differs from a ‘need’ because wants:", "are unlimited and not essential for survival", ["are essential for survival", "can always be fulfilled", "are fixed by the government"], "Needs: food, clothing, shelter."),
 m("Which of the following questions does a central problem of an economy NOT include?", "Who will rule?", ["What to produce?", "How to produce?", "For whom to produce?"], "Three central questions."),
 m("In a planned economy, the main economic decisions are taken by:", "the government/central authority", ["consumers", "private firms", "foreign companies"], "Command economy."),
 m("When the price of a good falls, the quantity demanded generally:", "rises", ["falls", "stays constant", "becomes zero"], "Law of demand."),
 ar("The demand curve generally slopes downwards.", "Consumers buy more of a good when its price falls, other things remaining the same.", 'a', "Inverse relation between price and quantity demanded."),
 m("An outward shift of the demand curve can be caused by:", "an increase in the income of consumers", ["a fall in the price of the good", "a fall in the cost of production", "a rise in the supply of the good"], "Price change = movement along curve; income change = shift."),
 m("Which Harappan site in Rajasthan shows evidence of ploughed fields and fire altars?", "Kalibangan", ["Lothal", "Dholavira", "Harappa"], "Kalibangan (Hanumangarh)."),
 m("The script of the Harappan civilisation:", "has not yet been deciphered", ["is Brahmi", "is cuneiform", "is Devanagari"], "Seals carry symbols."),
 match(["Chola", "Pandya", "Chera"], ["Madurai", "Vanji / Muziris region (Kerala)", "Uraiyur / Kaveri delta"], ["a-3, b-1, c-2", "a-1, b-2, c-3", "a-2, b-3, c-1", "a-3, b-2, c-1"], 'a', "Cholas — Uraiyur, Kaveri delta; Pandyas — Madurai; Cheras — Kerala coast."),
 m("Which Mahajanapada was a republic (gana-sangha)?", "Vajji", ["Magadha", "Kosala", "Avanti"], "Vajji confederacy had its capital at Vaishali."),
 m("A state with an elected president and a fixed term and no monarch is a:", "republic", ["monarchy", "dictatorship", "theocracy"], "India is a democratic republic."),
 m("Which Article of the Constitution provides for the Election Commission?", "Article 324", ["Article 14", "Article 21", "Article 370"], "ECI supervises elections."),
 m("In the First-Past-the-Post system the winner is the candidate who:", "gets the highest number of votes in the constituency", ["gets more than 50% votes", "is nominated by the Governor", "has the most property"], "Plurality system used in Lok Sabha polls."),
]
B = [
 sa("What is meant by weather and climate? Write one difference.", 2, "Weather: day-to-day atmospheric conditions (1). Climate: average weather over a long period (30+ years) (1)."),
 sa("What is a ‘want’? How is it different from a ‘need’? Give an example.", 2, "Want: desire for goods beyond survival (1); needs are essential e.g. food; wants e.g. a smartphone (1)."),
 OR(sa("Name any two sources from which we learn about the Harappan civilisation.", 2, "Excavated remains of cities, seals, pottery, tools, ornaments, burials (any two)."),
    sa("Mention any two causes of the decline of the Harappan civilisation.", 2, "Climate change/drying rivers, floods, shifting rivers, decline of trade (any two).")),
 sa("Write any two functions of political parties.", 2, "Contest elections; form government/opposition; shape public opinion; make policies (any two)."),
]
C = [
 sa("Explain the heat budget of the Earth in brief.", 3, "Insolation received by Earth (1); about one-third reflected, rest absorbed by atmosphere and surface (1); Earth radiates equal heat back so temperature stays constant (1)."),
 sa("Describe the formation of a delta.", 3, "River slows near the mouth (1); deposits silt in many branches/distributaries (1); fan-shaped fertile land e.g. Ganga–Brahmaputra (Sundarbans) delta (1)."),
 sa("Why is the market demand curve flatter than the individual demand curve?", 3, "Market demand = sum of individual demands (1); every price change induces a larger total change in quantity (1); example (1)."),
 OR(sa("Describe the rule of Ashoka and the idea of dhamma.", 3, "Ashoka's remorse after the Kalinga war (1); dhamma = tolerance, non-violence, respect for elders/animals (1); edicts and dhamma mahamattas (1)."),
    sa("Describe the achievements of Samudragupta.", 3, "Conquests in north & south as per the Allahabad Pillar inscription (1.5); title ‘Napoleon of India’ (0.5); patron of arts and music (1).")),
 sa("Explain the importance of the voter list (electoral roll) and the voter ID card (EPIC).", 3, "Roll lists eligible voters (1); prevents impersonation/duplicate voting (1); EPIC serves as proof of identity for voting (1)."),
]
D = [
 OR(sa("Describe the structure of the atmosphere with a labelled diagram.", 5, "Labelled diagram (2); troposphere (weather), stratosphere (ozone), mesosphere, thermosphere (ionosphere), exosphere — one line each (3)."),
    sa("Explain the factors that affect the climate of a place.", 5, "Latitude, altitude, distance from the sea, winds, ocean currents, relief — one explained point per mark.")),
 OR(sa("Explain the working of the market economy and the planned economy, and the merits and demerits of each.", 5, "Market: price mechanism — efficiency, but inequality (2.5). Planned: central planning — equity, but low incentive (2.5)."),
    sa("Describe the economic reforms of 1991 in India and their significance.", 5, "Liberalisation, privatisation, globalisation (3); reduced controls, foreign investment (1); growth and challenges (1).")),
 OR(sa("Describe the political, social and religious life of the Vedic people.", 5, "Tribal polity with rajan, sabha, samiti (1.5); pastoral life, cattle wealth (1); joint family (1); worship of Indra, Agni, Varuna; yajnas (1.5)."),
    sa("What were the Mahajanapadas? Why did Magadha become the most powerful?", 5, "Sixteen large states c.600 BCE (1.5); Magadha: fertile land, iron, elephants, rivers, able rulers Bimbisara and Ajatashatru (3.5).")),
 OR(sa("Explain the features of a representative democracy. How is it different from direct democracy?", 5, "People elect representatives (1.5); regular free and fair elections (1); rule of law (1); difference with direct democracy (1.5)."),
    sa("Describe the Right against Exploitation and Right to Freedom of Religion.", 5, "Art 23–24: ban on human trafficking, forced labour, child labour in hazardous jobs (2.5); Art 25–28: freedom to profess, practise and propagate religion (2.5).")),
]
E = [
 src("A river begins as a small stream high in the mountains. In its upper course the steep slope gives it great speed, and it cuts deep V-shaped valleys and forms waterfalls. In the middle course it flows more slowly and begins to swing from side to side in large bends known as meanders. Sometimes a meander gets cut off from the main channel and forms a lake. Near its mouth the river deposits its load and builds a delta.",
     [sub("In which course of a river are V-shaped valleys formed?", 1, "Upper course."), sub("What is a meander?", 1, "A large bend/loop in a river's middle course."), sub("How is an ox-bow lake formed?", 2, "Erosion on outer bank/deposition on inner bank narrows the neck (1); river cuts through it, leaving a cut-off lake (1).")]),
 src("The law of demand states that, other things remaining the same, when the price of a good rises, the quantity demanded falls, and when the price falls, the quantity demanded rises. Srivalli buys 1 kg of mangoes at ₹150 per kg, but when the price drops to ₹50 per kg she buys 3 kg. If we plot such pairs of price and quantity on a graph and join them, we get the individual demand curve, which slopes downwards.",
     [sub("State the law of demand.", 1, "Price and quantity demanded are inversely related, other things equal."), sub("How much does Srivalli buy at ₹50 per kg?", 1, "3 kg."), sub("Why does the demand curve slope downward? Give two reasons.", 2, "Lower price makes the good cheaper than substitutes/raises real income (1); diminishing marginal utility makes people buy more only at lower prices (1).")]),
 src("India is the world's largest democracy. Every citizen aged 18 years and above has the right to vote, irrespective of caste, religion, gender, education or income. This principle is called universal adult franchise. Elections are conducted by the Election Commission of India, an independent constitutional body. To ensure free and fair elections, the Commission enforces the Model Code of Conduct once elections are announced.",
     [sub("What is the minimum voting age in India?", 1, "18 years."), sub("Which body conducts elections in India?", 1, "Election Commission of India."), sub("Why is the Model Code of Conduct important?", 2, "Ensures a level playing field (1); prevents misuse of government resources and unfair practices (1).")]),
]
F = mapq([("Sanganakallu (Neolithic site)", 76.9, 15.1), ("Bhimbetka (rock paintings)", 77.6, 22.9), ("Pataliputra (Patna)", 85.1, 25.6), ("Madurai (Pandya kingdom)", 78.1, 9.9), ("Dhauli (Ashokan rock edict)", 85.8, 20.2), ("Kolkata", 88.35, 22.57)], [])
SECTIONS = assemble(A, B, C, D, E, F)
