from eng9_lib import mcq, Q, X

NAME = "Carrier of Words; Words"
MCQ = [
 mcq("Khetaram is a:", ["Gramin Dak Sewak", "bank clerk", "forest guard", "railway porter"], "a", "Rural postman"),
 mcq("He serves the Somarad Branch Post Office in:", ["Rajasthan", "Punjab", "Kerala", "Assam"], "a", "Thar desert"),
 mcq("The village he serves lies close to the:", ["Indo-Pakistan border", "Bay of Bengal", "Himalayas", "Western Ghats"], "a", "2.5 km short of the border"),
 mcq("The maximum weight of his mailbag as per rules is:", ["28 kilos", "10 kilos", "50 kilos", "5 kilos"], "a", "Regulation"),
 mcq("Khetaram has served for about:", ["15 years", "2 years", "40 years", "5 years"], "a", "Sole postman"),
 mcq("A temperature of 50 °C is recorded as 49.9 °C because:", ["50 °C would mean a state holiday", "the thermometer is faulty", "it is a rule of postmen", "it is cooler at night"], "a", "Official practice"),
 mcq("Gramin Dak Sewaks form what share of India Post's workforce?", ["more than half", "one-tenth", "a quarter", "a few"], "a", "Over 50 per cent"),
 mcq("The selection of GDS requires that candidates have:", ["another means of livelihood", "a degree", "a car", "a government flat"], "a", "Essential criterion"),
 mcq("GDS may serve until the age of:", ["65", "58", "60", "70"], "a", "Allowed beyond 60"),
 mcq("The families of the desert depend partly on:", ["money orders from relatives", "taxes", "tourism", "mining"], "a", "Survival"),
 mcq("Khetaram can read and write letters, so villagers:", ["ask him to read and reply to letters", "avoid him", "pay him", "fear him"], "a", "Trust"),
 mcq("A letter with its right corner torn signifies:", ["news of a death", "a birth", "a wedding", "a job"], "a", "Ashubh samachar"),
 mcq("Khetaram deals with such a letter by:", ["reading it twice outside and tearing it", "delivering it at once", "keeping it", "returning it"], "a", "'Bad news must be destroyed'"),
 mcq("After independence the purpose of India Post was to:", ["bring the entire population within the mailing range", "carry company letters", "collect taxes", "serve only cities"], "a", "Compared to the British system"),
 mcq("The poem 'Words' compares words to:", ["summer birds and weeds", "diamonds", "rivers", "mountains"], "a", "Worthless without feeling"),
 mcq("The poet believes that:", ["a few sincere words can bring deep joy", "many words are better", "silence is useless", "words never matter"], "a", "Message"),
]
EXT = [
 X("Beyond the last railhead, where the road crumbles into sand, the Gramin Dak Sewak is the only link between remote hamlets and their relatives. Khetaram walks across dunes with a heavy mailbag so that the post reaches the border within a day of leaving the city.",
   [("What does the road do beyond the railhead?", "It crumbles into sand."),
    ("What is Khetaram's role?", "He is the only link between remote hamlets and families."),
    ("How quickly does the mail reach the border?", "Within 24 hours of dispatch."),
    ("What quality of Khetaram does this show?", "Dedication and hard work.")]),
 X("Khetaram says that famine is a way of life in his land. One crop of bajra cannot feed his family of five, so the job saved them from hunger. Most families also depend on money orders from relatives, and so on the trust people place in the post office.",
   [("How does Khetaram describe famine?", "As a way of life."),
    ("Why is one crop of bajra not enough?", "It cannot feed his family of five."),
    ("What else do families depend on?", "Money orders sent by relatives."),
    ("What does this show about the post office?", "People trust it greatly.")]),
 X("The poet says that if words could satisfy the heart it would have fewer cares. Words fly away like summer birds. A few true words can give more joy than many that only reach the head. Without sincerity, words are like showy plants that bear no fruit.",
   [("To what are words compared in the first stanza?", "Summer birds."),
    ("What can a few truthful words do?", "Give deeper joy."),
    ("What is the poet's complaint about many words?", "They reach the head but do not touch the heart."),
    ("What is the central message?", "Sincere speech is more valuable than a flood of words.")]),
]
SA = [
 Q("Why is Khetaram's job difficult?", "He walks long distances in the desert in extreme heat with a heavy bag and covers 20 km for a single delivery.", "2"),
 Q("Why do villagers trust Khetaram?", "He is honest, reads and writes letters for them and brings news and money safely.", "2"),
 Q("What is the significance of the money order in the desert?", "It sustains families through money sent by relatives and shows people's confidence in the post office.", "2"),
 Q("How is the Gramin Dak Sewak different from a regular postman?", "GDS work five hours a day, need another livelihood and can serve till 65.", "2"),
 Q("Why does Khetaram tear letters bearing bad news?", "He believes that bad news must not enter a home and should be destroyed.", "2"),
 Q("What does 'a little said and truly said' mean in the poem?", "A few sincere words can be more valuable than many empty ones.", "2"),
]
LA = [
 Q("Describe a day in Khetaram's life.", "He carries mail from the railhead and bus, walks across sand dunes and desert to far hamlets, delivers letters and money orders, reads and replies for villagers, and faces heat and sandstorms.", "3"),
 Q("Why is the role of the GDS called 'invaluable'?", "They reach inaccessible areas on foot, link families, deliver money and mail, and help India Post reach everyone.", "3"),
 Q("How does the writer show the trust people place in the postal system?", "A proposal to replace GDS was rejected; villagers deposit savings; Khetaram is welcomed everywhere.", "3"),
 Q("Why is Khetaram grateful for his job?", "It gives him a steady income to feed his family; he can serve beyond 60; people respect him.", "3"),
 Q("What challenges does the desert pose to Khetaram?", "Temperatures above 50 °C, sandstorms, water scarcity, walking long distances and heavy mailbags.", "3"),
 Q("How does the author pay tribute to postmen like Khetaram?", "By describing their toil with sympathy, calling them part of the social fabric and saluting them.", "3"),
 Q("What does the poem 'Words' say about the value of words?", "Words alone do not satisfy the heart; many words may be empty; few sincere words are precious.", "3"),
 Q("Explain the images used in the poem.", "Words as summer birds that fly away; words as weeds; plants with show but no fruit; they suggest emptiness without feeling.", "3"),
]
