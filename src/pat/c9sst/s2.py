from h import *
META = meta(2, "Set 02")
A = [
 m("Which tectonic boundary is formed when two plates move towards each other?", "Convergent boundary", ["Divergent boundary", "Transform boundary", "Passive boundary"], "Collision/subduction e.g. Himalayas."),
 ar("The Himalayas are young fold mountains and are still rising slowly.", "The Indian plate continues to push against the Eurasian plate.", 'a', "Continuing convergence keeps uplifting the Himalayas and causes frequent earthquakes."),
 m("The point on the Earth's surface directly above the focus of an earthquake is the:", "epicentre", ["seismograph", "hypocentre line", "fault"], "Epicentre lies vertically above the focus."),
 m("Which of the following is a landform created by glacial deposition?", "Moraine", ["Delta", "Sea stack", "Barchan"], "Moraines are heaps of rock debris dropped by glaciers."),
 m("Crescent-shaped sand dunes formed by wind in deserts are called:", "barchans", ["levees", "cirques", "sea arches"], "Wind deposition."),
 st("The troposphere is the layer of the atmosphere in which weather phenomena occur.", "Temperature increases with height in the troposphere.", True, False, "In the troposphere temperature decreases with height."),
 m("The most abundant gas in the Earth's atmosphere is:", "nitrogen", ["oxygen", "carbon dioxide", "argon"], "About 78% nitrogen, 21% oxygen."),
 ar("Greenhouse gases keep the Earth warm enough for life.", "They trap part of the outgoing infrared radiation.", 'a', "Natural greenhouse effect; excess gases cause global warming."),
 m("Scarcity arises in an economy because:", "resources are limited while human wants are unlimited", ["people do not work", "prices are high", "the government taxes goods"], "Basic economic problem."),
 m("A point inside the PPC indicates:", "under-utilisation of resources", ["full use of resources", "unattainable production", "foreign trade"], "Resources unemployed/under-used."),
 m("Printers and ink cartridges are examples of:", "complementary goods", ["substitute goods", "public goods", "inferior goods"], "Demand for one rises with the other."),
 m("If the price of coffee rises, the demand for tea (its substitute) will most likely:", "increase", ["decrease", "remain unchanged", "become zero"], "People shift from coffee to tea."),
 m("The price at which quantity demanded equals quantity supplied is the:", "equilibrium price", ["ceiling price", "floor price", "retail price"], "Market clears."),
 match(["Price ceiling", "Price floor", "Monopoly"], ["Single seller in the market", "Maximum price fixed by government", "Minimum price fixed by government"], ["a-2, b-3, c-1", "a-3, b-2, c-1", "a-1, b-2, c-3", "a-2, b-1, c-3"], 'a', "Ceiling = maximum; floor (e.g., MSP) = minimum; monopoly = one seller."),
 m("The earliest cities of the Indus (Harappan) civilisation were known for their:", "grid-pattern streets and covered drains", ["huge pyramids", "iron weapons", "temples of stone"], "Planned towns with drainage."),
 m("The Great Bath is found at:", "Mohenjodaro", ["Lothal", "Kalibangan", "Rakhigarhi"], "Mohenjodaro (Sindh, Pakistan)."),
 m("The civilisation that developed in the valley between the Tigris and the Euphrates is the:", "Mesopotamian civilisation", ["Egyptian civilisation", "Chinese civilisation", "Harappan civilisation"], "Greek ‘Mesopotamia’ = land between rivers."),
 m("Ashoka's Rock Edict XIII describes his remorse after the war with:", "Kalinga", ["Gandhara", "Magadha", "Avanti"], "Led him to follow dhamma."),
 m("The Allahabad Pillar inscription, composed by Harishena, praises the conquests of:", "Samudragupta", ["Chandragupta Maurya", "Harshavardhana", "Kanishka"], "Gupta ruler."),
 m("The Model Code of Conduct comes into effect from the date:", "elections are announced by the Election Commission", ["results are declared", "the government is formed", "nominations close"], "Ensures free and fair polls."),
]
B = [
 sa("Distinguish between weathering and erosion in two points.", 2, "Weathering: breaking down of rocks in place (1). Erosion: removal and transport of material by water, wind, ice (1)."),
 sa("Name any two materials carried by a river and state where they are mostly deposited.", 2, "Silt, sand, gravel, pebbles (any two) (1); deposited on flood plains and at the river mouth/delta where speed falls (1)."),
 OR(sa("What is a fundamental right? Name any two fundamental rights.", 2, "Basic human rights guaranteed by the Constitution, enforceable in court (1). Any two: equality, freedom, against exploitation, religion, cultural & educational rights, constitutional remedies (1)."),
    sa("What is the Right to Constitutional Remedies? Why did Dr Ambedkar call it the ‘heart and soul’ of the Constitution?", 2, "Right to move the Supreme Court/High Courts to enforce FR (Art. 32) (1); without it other rights would be only on paper (1).")),
 sa("Give two reasons why the Harappan cities are called ‘planned’ cities.", 2, "Grid-pattern streets, well-planned drainage, citadel and lower town, standard bricks (any two)."),
]
C = [
 sa("Explain how plate tectonics causes earthquakes and volcanoes.", 3, "Crust divided into plates moving slowly (1); stress at convergent/transform boundaries released as earthquakes (1); magma rises at boundaries/subduction zones forming volcanoes — Ring of Fire (1)."),
 sa("Explain the greenhouse effect and name two greenhouse gases.", 3, "Atmosphere traps outgoing heat (1.5), keeping Earth warm; gases: carbon dioxide, methane, water vapour, nitrous oxide (any two) (1); excess leads to global warming (0.5)."),
 OR(sa("What is the law of supply? Why does the supply curve slope upwards?", 3, "Law (1): as price rises quantity supplied rises, other things equal. Reason (2): higher price means higher profit, so producers supply more; costs of extra units are covered."),
    sa("Why is a price floor such as MSP fixed by the government? Give one effect.", 3, "To protect farmers from very low prices (1.5); fixed above equilibrium (0.5); effect—surplus stock/procurement by government or assured income (1).")),
 sa("Describe any three features of the Mauryan administration.", 3, "Strong centralised rule with the king; capital Pataliputra; provinces under princes; spies (gudhapurusha); officials like amatyas; Arthashastra; dhamma mahamattas. Any three."),
 sa("State three duties of the Election Commission of India.", 3, "Prepares and updates electoral rolls; announces schedule and conducts elections; enforces Model Code; allots symbols and recognises parties; monitors expenditure. Any three."),
]
D = [
 OR(sa("Describe the landforms made by glaciers and by wind with examples.", 5, "Glacier: cirques, U-shaped valleys, aretes, moraines (2.5). Wind: mushroom rocks, sand dunes (barchans), loess (2.5)."),
    sa("Explain how rivers shape the land in their upper, middle and lower courses.", 5, "Upper: V-shaped valley, waterfalls, gorge (erosion) (1.5); middle: meanders, ox-bow lakes (1.5); lower: flood plains, levees, delta (deposition) (1.5); conclusion (0.5).")),
 OR(sa("Discuss the major river-valley civilisations of the ancient world.", 5, "Mesopotamia (Tigris–Euphrates), Egypt (Nile), Indus, China (Huang He/Yangtze) — location, features such as writing (cuneiform, hieroglyphs), cities, agriculture. Any five points with examples."),
    sa("Describe the town planning, trade and craft of the Harappan civilisation.", 5, "Grid streets, drains, citadel, Great Bath (2); trade with Mesopotamia, seals, standard weights (1.5); bead-making, pottery, copper & bronze work (1.5).")),
 OR(sa("Explain the importance of the Right to Equality and the Right to Freedom.", 5, "Equality (Art 14–18): equality before law, no discrimination, abolition of untouchability, titles (2.5). Freedom (Art 19–22): speech, assembly, movement, profession; protection in arrest (2.5)."),
    sa("Explain the role of the Supreme Court as the guardian of the Constitution.", 5, "Judicial review (1.5); protects FR through writs (1.5); resolves disputes between Centre and States (1); PIL (1).")),
 OR(sa("What is opportunity cost? How does it help a government and a household make better choices? Give examples.", 5, "Definition (1); household example (1.5); government example e.g., hospital vs. school (1.5); conclusion on trade-offs (1)."),
    sa("What is a public good? Why can the market not provide it efficiently? Give examples.", 5, "Non-excludable, non-rivalrous (2); free-rider problem, no profit (1.5); examples: street lights, roads, defence (1); government provides through taxes (0.5).")),
]
E = [
 src("The Junagadh rock at Girnar in Gujarat holds three important inscriptions. The earliest is a set of edicts of the Mauryan emperor Ashoka. In about 150 CE, the Shaka ruler Rudradaman I added a long Sanskrit inscription describing the repair of the Sudarshana lake, which had been built in the time of Chandragupta Maurya. Later, in the 5th century CE, the Gupta ruler Skandagupta recorded the repair of the same lake on the same rock.",
     [sub("Where is the Junagadh rock inscription located?", 1, "Girnar, Gujarat."), sub("Name the ruler who added the long Sanskrit inscription.", 1, "Rudradaman I."), sub("What does this single rock tell us about the history of the region?", 2, "Several dynasties — Mauryas, Shakas, Guptas — ruled/cared for the region (1); importance of irrigation/lake and continuity of records (1).")]),
 src("In a market, buyers and sellers interact to decide the price of goods. When the price of a good is higher than the equilibrium price, sellers want to sell more than buyers want to buy and an excess supply appears. Sellers then lower the price. When the price is lower than the equilibrium price, buyers want more than is available, causing excess demand, and the price rises. In this way the market moves towards equilibrium.",
     [sub("What is excess supply?", 1, "Quantity supplied greater than quantity demanded."), sub("What happens to price when there is excess demand?", 1, "It rises."), sub("Explain how a market reaches equilibrium.", 2, "Price adjusts upward/downward (1) until quantity demanded = quantity supplied (1).")]),
 src("The Constitution of India was adopted on 26 November 1949 and came into force on 26 January 1950. The Drafting Committee was chaired by Dr B. R. Ambedkar. The Preamble declares India a sovereign, socialist, secular, democratic republic and promises justice, liberty, equality and fraternity to all citizens. Fundamental Rights protect individuals against arbitrary State action and can be enforced in courts.",
     [sub("When did the Constitution of India come into force?", 1, "26 January 1950."), sub("Who chaired the Drafting Committee?", 1, "Dr B. R. Ambedkar."), sub("Why are Fundamental Rights important in a democracy?", 2, "Protect individual freedom and equality (1); enforceable by courts against State (1).")]),
]
F = mapq([("Dholavira (Harappan site)", 70.2, 23.9), ("Rakhigarhi (Harappan site)", 76.1, 29.3), ("Burzahom (Neolithic site)", 74.9, 34.1), ("Varanasi (Kashi Mahajanapada)", 83.0, 25.3), ("Ujjain (Avanti Mahajanapada)", 75.8, 23.2), ("Chennai", 80.27, 13.08)], [])
SECTIONS = assemble(A, B, C, D, E, F)
