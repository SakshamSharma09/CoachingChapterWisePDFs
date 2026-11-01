from h import *
META = meta(4, "Set 04")
A = [
 m("The famous Hindu Kush–Himalayan fold mountains were formed by the collision of the:", "Indian plate and the Eurasian plate", ["African and Pacific plates", "Arabian and Antarctic plates", "Pacific and Nazca plates"], "Convergent boundary."),
 m("A U-shaped valley is the work of:", "glaciers", ["rivers", "wind", "sea waves"], "River valleys are V-shaped."),
 m("Sea arches and sea stacks are landforms created by:", "sea waves", ["rivers", "glaciers", "winds in deserts"], "Coastal erosion."),
 st("Rocks in the lithosphere are broken down by weathering.", "Weathering needs the movement of the broken material by water or wind.", True, False, "Weathering is in situ; transport is erosion."),
 ar("Places near the equator receive more insolation than the poles.", "The Sun's rays fall nearly vertically at the equator.", 'a', "Vertical rays are concentrated on a smaller area."),
 m("Which gas in the atmosphere is essential for respiration of living beings?", "Oxygen", ["Nitrogen", "Argon", "Neon"], "About 21% of the atmosphere."),
 m("The rotation of the Earth deflects winds to the right in the Northern Hemisphere. This is known as the:", "Coriolis effect", ["Doppler effect", "Greenhouse effect", "Tyndall effect"], "Caused by rotation of Earth."),
 m("Who among the following studies the choices people make in using limited resources?", "An economist", ["A geologist", "An astronomer", "A botanist"], "Economics is the study of choices."),
 m("The PPC is bowed outward (concave to the origin) because:", "resources are not equally good at producing both goods", ["prices are constant", "demand is falling", "the government taxes goods"], "Increasing opportunity cost."),
 m("In a market economy, what to produce is decided mainly by:", "consumer demand and profit", ["a five-year plan", "the Supreme Court", "foreign banks"], "Price signals."),
 m("An example of a market where a single seller controls the supply is a:", "monopoly", ["perfect competition", "barter system", "cooperative"], "One seller."),
 m("The government's decision to fix the maximum retail price of an essential medicine is an example of a price:", "ceiling", ["floor", "equilibrium", "subsidy"], "Prevents prices from rising above a limit."),
 ar("An increase in the number of sellers shifts the market supply curve to the right.", "More sellers mean a larger quantity supplied at each price.", 'a', "Market supply is the sum of individual supplies."),
 m("The earliest known Neolithic site in the Indian subcontinent, on the Bolan river, is:", "Mehrgarh", ["Burzahom", "Chirand", "Sanganakallu"], "Mehrgarh in Balochistan, c. 7000 BCE."),
 m("Which of the following was a Mahajanapada with its capital at Kaushambi?", "Vatsa", ["Kosala", "Avanti", "Anga"], "Vatsa — Kaushambi."),
 m("The Chola kingdom was centred on the delta of the river:", "Kaveri", ["Godavari", "Krishna", "Narmada"], "Tamil Nadu."),
 m("Xuanzang, the Chinese pilgrim, visited India during the reign of:", "Harshavardhana", ["Ashoka", "Samudragupta", "Kanishka"], "Visited India c. 629–645 CE."),
 match(["Pulakeshin II", "Harshavardhana", "Chandragupta Maurya"], ["Kannauj", "Pataliputra", "Aihole inscription"], ["a-3, b-1, c-2", "a-1, b-2, c-3", "a-2, b-3, c-1", "a-3, b-2, c-1"], 'a', "Aihole record of Pulakeshin II; Harsha — Kannauj; Chandragupta — Pataliputra."),
 m("Which one of the following is NOT a feature of a democratic government?", "Rulers cannot be changed by the people", ["Free and fair elections", "Rule of law", "Freedom of expression"], "In democracy people can change rulers."),
 m("The voting machine used in Indian elections is called:", "EVM", ["ATM", "RTI", "NOTA"], "Electronic Voting Machine with VVPAT."),
]
B = [
 sa("Define ‘plate tectonics’. Name any two major plates.", 2, "Theory that the lithosphere is divided into moving plates (1). Pacific, Eurasian, African, Indo-Australian, North American… (1)."),
 sa("State the difference between ‘demand’ and ‘quantity demanded’.", 2, "Demand: the whole schedule/curve of quantities at different prices (1). Quantity demanded: quantity at a particular price (1)."),
 sa("What is the Right to Education? Which Article ensures it?", 2, "Free and compulsory education for children aged 6–14 years (1); Article 21A (added by the 86th Amendment, 2002) (1)."),
 OR(sa("Why are the Vedas important sources of information on the early Vedic period?", 2, "They are the oldest texts — Rigveda — describing religion, society, polity and economy (1); passed on orally for centuries (1)."),
    sa("What is the importance of Sangam literature?", 2, "Early Tamil poems/texts (1); give information about Chera, Chola, Pandya kingdoms, trade and society (1).")),
]
C = [
 sa("How are mountains important to humans? Give any three points.", 3, "Source of rivers; forests and minerals; tourism; influence on climate; biodiversity (any three)."),
 OR(sa("Describe any three effects of global warming.", 3, "Melting glaciers and rising sea level; extreme weather; changes in monsoon/agriculture; loss of species (any three)."),
    sa("Suggest three ways to reduce climate change.", 3, "Use renewable energy; plant trees; reduce use of fossil fuels; public transport; energy-efficient appliances (any three).")),
 sa("How do changes in income and price of related goods affect demand? Explain with examples.", 3, "Income rise → higher demand for normal goods (1); substitute price up → demand up (1); complement price up → demand down (1)."),
 sa("Describe the features of the Gupta age that earned it the name ‘golden age’.", 3, "Art, literature (Kalidasa), science (Aryabhata), coins, prosperity, strong rulers (any three)."),
 sa("Explain how First-Past-the-Post works with an example.", 3, "Country divided into constituencies (1); each voter votes for one candidate (1); candidate with the highest votes wins even without a majority — e.g., A 40%, B 35%, C 25% → A wins (1)."),
]
D = [
 OR(sa("Describe how wind and sea waves shape landforms with examples.", 5, "Wind: mushroom rocks, dunes, loess (2.5). Waves: cliffs, caves, arches, stacks, beaches (2.5)."),
    sa("Explain the layers of the Earth's interior with their features.", 5, "Crust (continental ~30–40 km, oceanic 5–7 km), mantle, outer core (liquid), inner core (solid) — properties of each.")),
 OR(sa("Why does scarcity force people to make choices? Explain with the help of examples of a household, a firm and a government.", 5, "Scarcity concept (1); household (1.3); firm (1.3); government (1.4); link to opportunity cost."),
    sa("Describe the role of a market economy and the government's role in it, citing the ‘referee’ analogy.", 5, "Market works on demand–supply (2); government sets rules, prevents monopoly, provides public goods like a referee (3).")),
 OR(sa("Describe the life of early humans from the Palaeolithic to the Neolithic age.", 5, "Palaeolithic: hunting–gathering, stone tools, fire (1.5); Mesolithic: microliths, rock paintings (1.5); Neolithic: farming, pottery, settled life (2)."),
    sa("Why is the Neolithic called a ‘revolution’? Mention its major sites in India.", 5, "Shift to farming and domestication (2); settled villages, pottery, surplus (1.5); sites: Mehrgarh, Burzahom, Chirand, Sanganakallu (1.5).")),
 OR(sa("Explain the objectives of the Constitution as stated in the Preamble.", 5, "Sovereign, socialist, secular, democratic, republic (2); Justice, liberty, equality, fraternity (3)."),
    sa("What are the three organs of government? Explain their functions.", 5, "Legislature — makes laws (1.7); Executive — implements (1.7); Judiciary — interprets and protects rights (1.6).")),
]
E = [
 src("The atmosphere is a thick envelope of gases around the Earth held by gravity. About 78 per cent of it is nitrogen and about 21 per cent is oxygen; the remaining 1 per cent includes argon, carbon dioxide, neon and water vapour. Most clouds, rain and storms occur in the lowest layer, the troposphere. Above it lies the stratosphere, which contains the ozone layer that protects living beings from harmful ultraviolet rays.",
     [sub("Which is the most abundant gas in the atmosphere?", 1, "Nitrogen."), sub("In which layer do clouds and rain occur?", 1, "Troposphere."), sub("Why is the ozone layer important for life on Earth?", 2, "Absorbs harmful UV radiation (1); prevents skin cancer, cataract and damage to plants/marine life (1).")]),
 src("The government of a country buys wheat from farmers at a minimum price called the Minimum Support Price (MSP) so that farmers do not have to sell at very low prices when the harvest is large. This wheat is stored in warehouses and later sold at low rates to poor families through ration shops. Both MSP and the ration system are examples of government intervention in the market.",
     [sub("What is MSP?", 1, "A minimum price fixed by the government at which it buys farm produce."), sub("Name one place where the government sells foodgrains at low rates.", 1, "Ration (Public Distribution System) shops."), sub("Explain why the government intervenes in the market for foodgrains.", 2, "To protect farmers' income (1); to ensure food security/affordability for the poor (1).")]),
 src("The Mauryan emperor Ashoka, after the war in Kalinga around 261 BCE, felt deep remorse at the loss of lives. He gave up conquest and adopted dhamma — a code of conduct based on tolerance, non-violence, respect for elders and kindness to all living beings. He had his messages engraved on rocks and pillars across the empire in Prakrit using the Brahmi script, and he appointed special officials called dhamma mahamattas.",
     [sub("In which war did Ashoka feel remorse?", 1, "Kalinga war."), sub("Name the script of Ashoka's edicts.", 1, "Brahmi."), sub("Explain any two principles of Ashoka's dhamma.", 2, "Tolerance among religions (1); non-violence and kindness to animals, respect for elders (1).")]),
]
F = mapq([("Bhimbetka (rock shelters)", 77.6, 22.9), ("Burzahom (Neolithic site)", 74.9, 34.1), ("Ujjain (Avanti Mahajanapada)", 75.8, 23.2), ("Kalibangan (Harappan site)", 74.1, 29.5), ("Pataliputra (Patna)", 85.1, 25.6), ("Kaveri delta (Chola kingdom)", 79.3, 10.9)], [])
SECTIONS = assemble(A, B, C, D, E, F)
