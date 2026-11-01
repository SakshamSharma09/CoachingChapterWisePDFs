from h import *
META = meta(5, "Set 05")
A = [
 m("Which of the following is an example of an igneous rock?", "Granite", ["Limestone", "Slate", "Sandstone"], "Formed by cooling of magma."),
 m("A funnel-shaped opening through which lava and gases erupt is a:", "volcano", ["glacier", "meander", "dune"], "Volcanic eruption at plate boundaries."),
 m("The instrument used to record the intensity of earthquake waves is the:", "seismograph", ["barometer", "anemometer", "hygrometer"], "Seismic waves recorded as seismograms."),
 ar("The summers in Rajasthan are hotter than in Kerala.", "Rajasthan lies far from the moderating influence of the sea.", 'a', "Continentality makes climate extreme."),
 st("Wind is moving air that flows from a region of high pressure to low pressure.", "The monsoon winds blow from the land to the sea in summer.", True, False, "In summer the SW monsoon blows from the sea to the land."),
 m("Humidity refers to the amount of ______ in the air.", "water vapour", ["nitrogen", "dust", "carbon dioxide"], "Relative humidity compares it to the maximum possible."),
 m("The word ‘economics’ is derived from the Greek word oikonomia, which means:", "household management", ["wealth of nations", "market place", "trade"], "Oikos = house, nomos = rule."),
 m("Which of the following is a need rather than a want?", "Drinking water", ["A video game", "A branded watch", "A holiday abroad"], "Needs are essential for survival."),
 ar("India is called a mixed economy.", "Both the government and private enterprises take economic decisions in India.", 'a', "Public and private sectors coexist."),
 m("In a perfectly planned economy, the biggest drawback is:", "little incentive for efficiency and innovation", ["too much competition", "high consumer choice", "excess supply always"], "Central control limits initiative."),
 m("Which of the following leads to a rightward shift of the demand curve of a normal good?", "A rise in the consumers' income", ["A rise in its price", "A fall in income", "A fall in the number of consumers"], "More demand at every price."),
 m("A good whose use by one person does not reduce its availability to others is:", "non-rivalrous", ["rivalrous", "inferior", "luxury"], "Characteristic of public goods."),
 m("Which one of the following is a feature of the Indus script?", "It is still undeciphered", ["It is written like Brahmi", "It is alphabetic like English", "It uses cuneiform wedges"], "Symbols on seals."),
 m("The Rigveda is divided into:", "mandalas", ["cantos", "volumes", "pitakas"], "Ten mandalas."),
 m("Which Harappan site has a unique system of water conservation and is a UNESCO World Heritage Site?", "Dholavira", ["Rakhigarhi", "Banawali", "Ropar"], "Dholavira, Kachchh, Gujarat (inscribed 2021)."),
 m("The sixteen large states of north India around 600 BCE were called:", "Mahajanapadas", ["Mandalas", "Subas", "Janapadas only"], "Anguttara Nikaya lists them."),
 m("Which dynasty founded by Pulakeshin I ruled from Badami?", "Chalukya", ["Pallava", "Pala", "Rashtrakuta"], "Badami (Vatapi), Karnataka."),
 m("Universal adult franchise in India is guaranteed to citizens aged:", "18 years and above", ["21 years and above", "25 years and above", "16 years and above"], "61st Amendment lowered age from 21 to 18."),
 m("Reserved constituencies in India are meant for:", "Scheduled Castes and Scheduled Tribes", ["women only", "minorities only", "senior citizens"], "Ensure representation."),
 m("‘NOTA’ in electronic voting machines stands for:", "None of the Above", ["No Option To Act", "Not On The Agenda", "Nominated Officials To Assembly"], "Option introduced in 2013."),
]
B = [
 sa("Distinguish between igneous and sedimentary rocks.", 2, "Igneous: from cooling of molten magma/lava e.g., basalt (1). Sedimentary: from layers of deposited sediments e.g., sandstone (1)."),
 OR(sa("What is a ‘public good’? Give two examples.", 2, "A good that benefits everyone and cannot be denied to anyone (1); street lights, roads, national defence (1)."),
    sa("What is meant by ‘equilibrium price’?", 2, "Price at which quantity demanded equals quantity supplied (1); there is neither excess supply nor excess demand (1).")),
 sa("Name any two Neolithic inventions that changed human life.", 2, "Farming/agriculture, domestication of animals, pottery, wheel, settled villages (any two)."),
 sa("Why are free and fair elections essential for a democracy?", 2, "Give people a real choice and the power to change rulers (1); make governments accountable (1)."),
]
C = [
 sa("Explain the process of weathering and its types.", 3, "Weathering = breaking of rocks in place (1); physical (temperature, frost) (1); chemical (water, acids) and biological (roots, animals) (1)."),
 sa("What are the different types of rainfall? Explain any one.", 3, "Convectional, orographic, cyclonic (1); explanation of one e.g. orographic: moist wind forced up a mountain cools, condenses and gives rain on windward side (2)."),
 sa("Explain opportunity cost with the help of an example of a farmer deciding between two crops.", 3, "Scarce land/water (1); choosing wheat means giving up pulses (1); value of pulses forgone = opportunity cost (1)."),
 OR(sa("Describe any three contributions of the Pallavas to art and architecture.", 3, "Rock-cut rathas and Shore temple at Mahabalipuram; Kailasanatha temple, Kanchipuram; sculpture and patronage of music/literature (any three, 1 each)."),
    sa("Describe any three contributions of the Chalukyas to art and architecture.", 3, "Cave temples at Badami; temples at Aihole and Pattadakal (UNESCO site); mix of northern and southern styles; patronage of literature (any three, 1 each).")),
 sa("List any three functions of the Election Commission of India.", 3, "Prepares electoral rolls; conducts elections; enforces Model Code of Conduct; recognises parties and allots symbols (any three)."),
]
D = [
 OR(sa("Explain the origin and effects of earthquakes. How are they measured?", 5, "Origin: plate movements, faults, volcanic activity (1.5); effects: damage to buildings, tsunamis, landslides (1.5); measured by seismograph on the Richter scale (1); focus and epicentre (1)."),
    sa("Describe the formation of the three types of rocks and the rock cycle.", 5, "Igneous (1.2), sedimentary (1.2), metamorphic (1.2); rock cycle — one rock changes into another (1.4).")),
 OR(sa("Explain the problem of scarcity and how the three central economic questions arise from it.", 5, "Scarcity (1.5); what to produce (1); how to produce (1); for whom to produce (1); examples (0.5)."),
    sa("How do changes in price and in other factors affect supply? Explain with examples.", 5, "Law of supply (1.5); factors: cost of inputs, technology, number of sellers, taxes/subsidies (2.5); example (1).")),
 OR(sa("Describe the main features of the Mauryan empire under Chandragupta and Ashoka.", 5, "Founding with Kautilya's help, defeat of Nandas (1); extent, capital Pataliputra, administration (2); Ashoka — Kalinga and dhamma (2)."),
    sa("Describe the achievements of the Gupta rulers in science, art and literature.", 5, "Aryabhata, Varahamihira (1.5); Kalidasa (1); Ajanta paintings, iron pillar at Mehrauli (1.5); coins, trade (1).")),
 OR(sa("What are the merits and limitations of the First-Past-the-Post system? Compare it with proportional representation.", 5, "FPTP: simple, stable, local link (1.5); limitations — wasted votes, winner with less than 50% (1.5); PR: seats in proportion to votes (1.5); comparison (0.5)."),
    sa("Describe the role of the Election Commission in conducting free and fair elections.", 5, "Independent constitutional body (1); roll, schedule, polling (1.5); Model Code (1); EVM/VVPAT, observers, counting (1.5).")),
]
E = [
 src("Monsoon winds reverse their direction with the seasons. In summer the land becomes much hotter than the sea, creating a low-pressure area over northern India. Moist south-west winds blow from the Indian Ocean towards the land and bring heavy rainfall between June and September. In winter, the land cools quickly and the winds blow from the land to the sea, which is why most of India remains dry in these months, except the Coromandel coast.",
     [sub("In which months does the south-west monsoon bring heavy rain to India?", 1, "June to September."), sub("Why does a low-pressure area form over northern India in summer?", 1, "Land heats up faster than the sea."), sub("Explain why winter winds in India are mostly dry.", 2, "They blow from land to sea (1) and carry little moisture (1).")]),
 src("In the market for vegetables, the price of tomatoes rose sharply after heavy rains damaged the crop. As the supply fell, many families reduced the amount of tomatoes they bought, while some switched to other vegetables. A few weeks later, when fresh produce arrived, the price came down and the demand recovered. This shows how prices act as signals in a market.",
     [sub("What caused the price of tomatoes to rise?", 1, "A fall in supply due to crop damage."), sub("Name the law that explains why families bought less at a higher price.", 1, "Law of demand."), sub("How do prices act as signals for buyers and sellers?", 2, "High price signals scarcity — buyers cut down, sellers produce more (1); low price signals abundance — buyers buy more, sellers reduce supply (1).")]),
 src("The Right to Information Act, 2005 empowers citizens to seek information from public authorities. Any citizen can file an application, paying a small fee, and the authority must give the information within 30 days. The Act promotes transparency and accountability in government, and has been used by ordinary citizens to expose corruption and improve public services such as ration distribution.",
     [sub("When was the RTI Act passed?", 1, "2005."), sub("Within how many days must the public authority usually reply?", 1, "30 days."), sub("How does the RTI Act strengthen democracy?", 2, "Promotes transparency/accountability (1); lets citizens question government and participate (1).")]),
]
F = mapq([("Dholavira (Harappan site)", 70.2, 23.9), ("Delhi", 77.2, 28.6), ("Hallur (Neolithic site)", 75.4, 14.9), ("Madurai (Pandya kingdom)", 78.1, 9.9), ("Kaushambi (Vatsa Mahajanapada)", 81.4, 25.4), ("Girnar / Junagadh (Ashokan rock edict)", 70.5, 21.5)], [])
SECTIONS = assemble(A, B, C, D, E, F)
