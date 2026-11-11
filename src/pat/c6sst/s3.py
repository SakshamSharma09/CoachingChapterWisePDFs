from h8 import *
META = meta(3, "Set 03")
# Set 3: emphasis Economics, Cultural roots, Family & Community, Earth's features
A = [
 m("Indian Standard Time is based on the longitude of —", "82.5° E", ["0°", "23.5° N", "90° W"], "The 82.5° E meridian passes near Mirzapur (Uttar Pradesh) and is used for IST."),
 m("Which continent has no permanent human population?", "Antarctica", ["Australia", "Europe", "South America"], "Only scientists stay there temporarily."),
 ar("Very few people live in the high Himalayan regions.", "The cold climate, steep slopes and thin soil make farming and travel difficult there.", 'exp', "R explains A."),
 m("Scientists who dig up and study the remains of the past are called —", "archaeologists", ["economists", "geologists", "astronomers"], "Archaeologists excavate sites."),
 st("The Constitution of India names the country as 'India, that is Bharat'.", "The name Hindustan has no connection with the Sindhu (Indus) river.", True, False, "Names like Hindu/India come from Sindhu."),
 fill("The famous Great Bath was found at the Harappan city of ...........", "Mohenjo-daro", ["Lothal", "Dholavira", "Kalibangan"], "It is a large public water tank."),
 m("The famous words 'Satyameva Jayate' (truth alone triumphs) come from the —", "Mundaka Upanishad", ["Panchatantra", "Arthashastra", "Ramayana"], "It is also the motto of India."),
 m("The number of languages included in the Eighth Schedule of the Constitution is —", "22", ["8", "12", "50"], "India recognises 22 scheduled languages."),
 m("Festivals celebrated together by a community mainly help to —", "build togetherness and pass on traditions", ["spread quarrels", "waste time and money only", "keep neighbours apart"], "Festivals strengthen bonds."),
 m("Rules made by the government that everyone must follow are called —", "laws", ["customs only", "games", "stories"], "Laws are backed by the authority of the state."),
 m("The three tiers of Panchayati Raj from lowest to highest are —", "Gram Panchayat, Panchayat Samiti, Zila Parishad", ["Zila Parishad, Panchayat Samiti, Gram Panchayat", "Panchayat Samiti, Gram Panchayat, Zila Parishad", "Gram Panchayat, Zila Parishad, Panchayat Samiti"], "Village, block and district levels."),
 m("A town with a population of about 1 lakh to 10 lakh generally has a —", "Municipal Council", ["Gram Panchayat", "Zila Parishad", "Panchayat Samiti"], "Smaller cities have Municipal Councils."),
 st("Taking care of children at home without being paid is a non-economic activity.", "A doctor treating patients for a fee is doing a non-economic activity.", True, False, "The doctor's work earns money, so it is economic."),
 m("Farming, fishing and mining are examples of the —", "primary sector", ["secondary sector", "tertiary sector", "non-economic activities"], "These activities use natural resources directly."),
 m("A farmer swaps 10 kg of wheat for 4 kg of lentils with a neighbour. This kind of exchange is called —", "barter", ["salary", "wage", "tax"], "Goods are exchanged directly without money."),
]
B = [
 vsa("What is a plateau? Give one example from India.", "A plateau is a raised flat-topped landform with steep sides — 1 mark", "Example: Deccan plateau (or Chota Nagpur plateau) — 1 mark", head="Marking points:"),
 OR(vsa("State any two teachings of Mahavira.", "Ahimsa (non-violence)", "Truthfulness / non-possession / respect for all life (any two, 1 mark each)"),
    vsa("What are the Upanishads? Name one idea from them.", "Ancient texts that discuss the nature of the self and the universe — 1 mark", "Idea: truth alone triumphs / the oneness of all life — 1 mark", head="Marking points:")),
 vsa("What is the Gram Sabha? Who can take part in it?", "It is the meeting of all the adult voters of a village — 1 mark", "Every adult on the village voter list can take part and speak — 1 mark", head="Marking points:"),
 vsa("Classify as primary, secondary or tertiary: (i) growing wheat (ii) baking bread (iii) selling bread in a shop.", "(i) primary (ii) secondary (iii) tertiary (any two correct = 1 mark; all three = 2 marks)", head="Marking points:"),
]
C = [
 sa("Write any three facts about the continents and oceans of the Earth.", 3, sol("Marking points (any three, 1 mark each):", "There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe and Australia", "There are five oceans: Pacific, Atlantic, Indian, Southern and Arctic", "Asia is the largest continent and Australia the smallest", "The Pacific Ocean is the largest and deepest ocean", "Water covers about 70 per cent of the Earth's surface")),
 OR(sa("Explain any three ways in which family members and neighbours support one another in a community.", 3, sol("Marking points (any three, 1 mark each):", "Share food, tools and help during festivals/weddings", "Care for the old, sick and the young", "Help in times of trouble such as floods or illness", "Look out for each other's safety", "Pass on skills, values and traditions")),
    sa("State any three benefits of living in a community.", 3, sol("Marking points (any three, 1 mark each):", "Mutual help and a sense of security", "Sharing of resources and responsibilities", "Celebrating festivals together", "Learning from each other's skills", "Working together to solve common problems"))),
]
D = [
 OR(sa("Explain how pilgrimage, geography and shared stories made Bharat feel like one land.", 5, sol("Marking points (any five, 1 mark each):", "Sacred places lie in all directions — Badrinath, Dwarka, Puri, Rameswaram", "People from all parts travelled to the sacred rivers, mountains and temples", "Rivers such as the Ganga and the Kaveri and the Himalayas are held sacred", "Epics like the Ramayana and the Mahabharata spread across the land", "Old texts describe the land between the Himalayas and the southern ocean as Bharatavarsha", "Trade routes and the exchange of ideas joined different regions")),
    sa("Describe the various names by which the Indian subcontinent has been known and what each means.", 5, sol("Marking points (any five, 1 mark each):", "Sapta Sindhava — 'land of seven rivers' (Rig Veda)", "Jambudvipa — 'island of the jamun tree'", "Bharatavarsha — 'country of the Bharatas' (epics and Puranas)", "India — derived from the Sindhu (Indus) river", "Hindustan — also from Sindhu/Hindu", "Bharat — the name used in the Constitution"))),
 OR(sa("Explain the primary, secondary and tertiary sectors of the economy with two examples of each.", 5, sol("Marking points:", "Primary sector — activities that use natural resources directly: farming, fishing, mining, forestry (1 + 1 for any two examples)", "Secondary sector — turn raw materials into goods: making furniture, baking bread, making cloth (1 + 1)", "Tertiary sector — services: teaching, banking, transport, medical care (1 + 1) — maximum 5 marks")),
    sa("Explain how the use of money solved the problems of the barter system (five points).", 5, sol("Marking points (any five, 1 mark each):", "Barter needs a 'double coincidence of wants'; money removes this need", "Money is accepted by everybody for payment", "Money gives a common unit for pricing different goods", "Money can be saved and used later", "Money makes trade over long distances easy", "It makes payment of wages and salaries convenient"))),
]
E = [
 src("About 9000 years ago, people at Mehrgarh, in the north-west of the subcontinent, began growing wheat and barley and keeping sheep, goats and cattle. They built houses of mud bricks and made grain stores. Over time, villages grew into the first cities of the Harappan civilisation.",
     [s("What did the people of Mehrgarh grow?", 1, "Wheat and barley."),
      s("Name any one thing that they built.", 1, "Mud-brick houses / grain stores."),
      s("How did settled farming help in the growth of cities? Give two points.", 2, "(1) Farming gave a regular food surplus, so some people could do other jobs (crafts, trade); (1) people could stay in one place, build houses and storage, and settlements grew.")]),
 src("The Panchayat of village Shantipur made a rule that the village pond must not be used for washing clothes. The Sarpanch and the secretary make sure that the rule is followed. When two neighbours quarrelled over a boundary wall, they went to the court, where a judge heard both sides and gave a decision.",
     [s("Who made the rule about the village pond?", 1, "The Panchayat (village council)."),
      s("Who decided the quarrel between the neighbours?", 1, "The judge in the court (judiciary)."),
      s("Name the organ of government to which each of these belongs: (a) making the rule (b) making sure the rule is followed.", 2, "(a) Legislature (1) (b) Executive (1)")]),
 src("In Anita's house, her mother cooks, cleans and looks after the elders and children. Anita's father works as a bus driver and receives a monthly salary. Her aunt weaves baskets and sells them in the weekly market. Anita says, \"Everybody works, but only some of the work is paid for.\"",
     [s("Which member of the family earns a monthly salary?", 1, "Anita's father (bus driver)."),
      s("Name one non-economic (unpaid) activity from the passage.", 1, "The mother's cooking, cleaning and caring for elders and children."),
      s("Why should unpaid household work be valued? Give any two reasons.", 2, "(1) It is essential for the care and well-being of the family; (1) if it had to be paid for, it would cost a lot — it is a contribution of love and time that enables others to earn.")]),
 src("The Pacific Ocean, the largest of the oceans, covers about one-third of the Earth's surface and contains the deepest known point, the Mariana Trench. The Indian Ocean is the only ocean named after a country. The Atlantic Ocean separates the Americas from Europe and Africa. The smallest ocean, the Arctic, is around the North Pole.",
     [s("Which is the largest ocean?", 1, "The Pacific Ocean."),
      s("Which ocean is named after a country?", 1, "The Indian Ocean (named after India)."),
      s("Name the two continents that lie to the east of the Atlantic Ocean.", 2, "Europe (1) and Africa (1).")]),
]
F = mapq([("Amritsar", 74.87, 31.63, "Punjab"), ("Haridwar", 78.16, 29.95, "Uttarakhand"), ("Varanasi", 82.99, 25.32, "Uttar Pradesh"), ("Guwahati", 91.74, 26.14, "Assam"), ("Rameswaram", 79.31, 9.29, "Tamil Nadu"), ("Dwarka", 69.1, 22.3, "Gujarat")])
SECTIONS = assemble(A, B, C, D, E, F)
