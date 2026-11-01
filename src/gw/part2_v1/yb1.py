from yhelp import gap, edit, omit
B = []
GI = "Fill in each blank with the most appropriate option."
O = lambda *a: tuple(a)
B += gap('B','B1.1','Gap Filling — Solar Energy',GI,
"The sun is [1] richest source of energy on Earth. Every day it sends [2] the earth far more energy than all human beings [3] in a year. Scientists [4] developed panels which convert sunlight into electricity. These panels, [5] are fitted on rooftops, work silently and cause no pollution. [6] they are costly at first, they save money [7] the long run. If more families [8] solar power, our cities would breathe cleaner air.",
[(O("a","an","the","some"),2),(O("at","to","for","on"),1),(O("uses","using","use","used"),2),(O("has","have","are","had"),1),(O("who","whose","which","where"),2),(O("Because","Although","Unless","Until"),1),(O("on","at","in","by"),2),(O("adopt","adopted","will adopt","would adopt"),1)])
B += gap('B','B1.2','Gap Filling — Mobile Phones',GI,
"Mobile phones have [1] a necessary part of our lives. Students use them [2] searching for information, but many of them waste hours [3] games and videos. A recent survey says that the number of teenagers [4] sleep late [5] steadily. Doctors warn that [6] much screen time [7] harm the eyes. It is high time we [8] to use phones wisely.",
[(O("became","become","becomes","becoming"),1),(O("for","with","to","at"),0),(O("on","in","at","of"),0),(O("who","whose","whom","which"),0),(O("increase","are increasing","is increasing","were increased"),2),(O("too","enough","very","quite"),0),(O("can","could have","may be","is"),0),(O("learn","learnt","learning","will learn"),1)])
B += gap('B','B1.3','Gap Filling — Saving Water',GI,
"Water is [1] precious that we cannot afford to waste even a drop. In many villages of Rajasthan, women walk [2] kilometres to fetch water. Rainwater harvesting, [3] was practised by our ancestors, is being revived [4] the government. If we [5] now, future generations [6] face a severe shortage. Each of us [7] a duty to save water [8] we can.",
[(O("so","such","very","too"),0),(O("several","much","little","a little"),0),(O("who","what","which","whom"),2),(O("from","by","with","through"),1),(O("did not act","do not act","would not act","had not acted"),1),(O("would have","will have","would","will"),3),(O("have","has","are having","having"),1),(O("whichever","whatever","however","whomever"),2)])
B += gap('B','B1.4','Gap Filling — Yoga',GI,
"Yoga, [1] originated in India thousands of years ago, is now practised [2] the world. It consists of postures, breathing exercises and meditation. People [3] practise yoga regularly [4] fewer health problems than those who do not. Instructors advise beginners [5] start with simple postures. One [6] not expect results overnight; patience and regularity [7] needed. Since 2015, the International Day of Yoga [8] celebrated on 21 June.",
[(O("which","who","whose","where"),0),(O("all over","over all","all across of","around of"),0),(O("who","whom","which","whose"),0),(O("has","have","having","to have"),1),(O("to","for","by","on"),0),(O("should","would","might","used"),0),(O("is","are","was","has"),1),(O("is","has been","was","have been"),1)])
B += gap('B','B1.5','Gap Filling — A Museum Visit',GI,
"Last Sunday our class [1] a visit to the museum. We [2] there by 9 a.m., but the guide [3] not yet arrived. While we [4] for him, we looked at a huge stone statue. When he finally came, he apologised [5] being late. He told us that the museum [6] three floors. We [7] never seen so many ancient coins [8] one place. Everyone returned home tired but happy.",
[(O("did","made","took","gave"),1),(O("reached","arrive","are reaching","had reach"),0),(O("has","had","have","was"),1),(O("wait","waited","were waiting","had waited"),2),(O("for","of","at","to"),0),(O("have","would have","had","is having"),2),(O("had","have","has","were"),0),(O("in","at","on","to"),0)])
B += gap('B','B1.6','Gap Filling — Plastic Pollution',GI,
"Plastic is cheap, light and durable; that is [1] it has become so popular. However, it does not rot like paper or wood. Every year millions of tonnes of plastic [2] thrown into the oceans, [3] harms sea creatures. A turtle may [4] a plastic bag for a jellyfish and die. We should [5] carrying cloth bags and avoid [6] single-use items. [7] we act together, the damage [8] be reversed.",
[(O("because","why","how","what"),1),(O("is","are","was","has"),1),(O("which","what","who","where"),0),(O("mistake","mistakes","mistaking","mistook"),0),(O("start","started","to start","starting"),0),(O("to use","using","use","used"),1),(O("If","Unless","Although","Until"),0),(O("can","did","has","is"),0)])
B += gap('B','B1.7','Gap Filling — The School Library',GI,
"A library is a treasure house of knowledge. Our school library [1] over ten thousand books, [2] range from fiction to science. Students are allowed to borrow two books [3] a time for a fortnight. A student [4] fails to return a book in time has to pay a fine. The librarian, Mr Verma, has been [5] here for twenty years. He is always [6] to help every reader. Silence [7] be maintained in the reading room, so that no one [8] disturbed.",
[(O("have","has","are having","were"),1),(O("who","which","what","whose"),1),(O("in","on","at","by"),2),(O("who","whom","whose","which"),0),(O("work","working","worked","works"),1),(O("ready","readily","readiness","readies"),0),(O("must","used to","dare","need"),0),(O("is","was","are","were"),0)])
B += gap('B','B1.8','Gap Filling — Road Safety',GI,
"Road accidents [1] a major cause of death in India. Most accidents are caused [2] over-speeding and carelessness. Pedestrians should [3] zebra crossings, and drivers must [4] for them. Two-wheeler riders [5] always wear helmets. A helmet protects the head [6] injury. Traffic rules [7] strictly followed if we [8] to reduce accidents.",
[(O("is","are","was being","has"),1),(O("by","with","from","of"),0),(O("use","to use","using","used"),0),(O("wait","waits","to wait","waiting"),0),(O("must","ought","used","dare"),0),(O("from","of","to","for"),0),(O("must be","must","must been","must being"),0),(O("want","wanted","will want","are wanting"),0)])

EI = "The following passage has not been edited. There is one error in each line. Write the incorrect word and its correction."
B += edit('B','B2.1','Editing — Sleep',EI,[
"Doctors {says|say} that an adult needs seven to eight hours of sleep.",
"However, many students {sleeps|sleep} for only five hours every night.",
"They stay awake {since|until} midnight to watch videos.",
"As a result, they feel tired {at|during} the day.",
"Lack of sleep {make|makes} it difficult to concentrate.",
"A child {which|who} sleeps well performs better in class.",
"Teachers should {advises|advise} students to go to bed early.",
"Good sleep is the {cheaper|cheapest} medicine of all.",
])
B += edit('B','B2.2','Editing — A Fair in the Village',EI,[
"Last week a fair {is|was} held in our village.",
"People {come|came} from nearby towns to enjoy it.",
"There {was|were} many shops selling toys and sweets.",
"I bought {a|an} umbrella for my mother.",
"My brother was fond {for|of} riding the giant wheel.",
"The children laughed {loud|loudly} and clapped with joy.",
"We returned home late {in|at} night.",
"I had never enjoyed {me|myself} so much before.",
])
B += edit('B','B2.3','Editing — Newspaper Report: Flood Relief',EI,[
"Heavy rains {has|have} flooded several villages in the district.",
"More than two thousand people {is|are} living in relief camps.",
"The Collector visited {a|the} affected areas yesterday.",
"He said that food packets {will be|would be} supplied to everyone.",
"Volunteers are working day {or|and} night to help the victims.",
"A boat carrying medicines {were|was} sent to the island.",
"The rain has {stopping|stopped} but the water level is still high.",
"Officials hope that normal life {resumes|will resume} soon.",
])
B += edit('B','B2.4','Editing — Importance of Reading',EI,[
"Reading is one of the {good|best} habits a student can develop.",
"A good book {take|takes} us to a different world.",
"It also improves our vocabulary and {write|writing} skills.",
"Students who {reads|read} regularly are often more confident speakers.",
"I {had|have} been reading a novel every month since last year.",
"Neither my brother nor my sister {are|is} fond of reading.",
"Parents should {to buy|buy} books for their children.",
"Reading is {an|a} habit that stays for life.",
])
B += edit('B','B2.5','Editing — The Marathon',EI,[
"The annual marathon will {held|be held} in our city next Sunday.",
"Thousands of runners {is|are} expected to take part.",
"The race will start at six {at|in} the morning.",
"Roads will be {close|closed} to traffic till noon.",
"Participants {should to|should} reach the venue by five.",
"Those {whom|who} have registered will get a free T-shirt.",
"The route is longer {from|than} last year's.",
"Everyone is looking forward {for|to} the event.",
])
B += edit('B','B2.6','Editing — Environment Day',EI,[
"Our school celebrated Environment Day {at|on} 5 June.",
"The Principal planted a sapling and {saying|said} a few words.",
"She asked us to {stopped|stop} using plastic bags.",
"Students took {a|an} oath to save energy.",
"A rally {were|was} also taken out in the colony.",
"We carried posters which {reads|read} 'Plant a tree'.",
"The people living there {appreciates|appreciated} our efforts.",
"It was the most {memorably|memorable} day for all of us.",
])
B += edit('B','B2.7','Editing — A Lost Wallet',EI,[
"Yesterday I {finds|found} a wallet on the road.",
"It contained some money and {a|an} identity card.",
"I {give|gave} it to the police immediately.",
"The owner, {whom|who} was a retired teacher, thanked me warmly.",
"He {say|said} that honesty still exists in the world.",
"I felt {happily|happy} that I had done my duty.",
"My mother was proud {on|of} me.",
"The police also praised {me|my} honesty in the newspaper.",
])
B += edit('B','B2.8','Editing — Newspaper Report: A Rescue',EI,[
"A young boy {were|was} rescued from a well yesterday.",
"He had fallen {on|into} it while playing with his friends.",
"Villagers {informing|informed} the fire brigade at once.",
"The rescue team {reach|reached} the spot within fifteen minutes.",
"They lowered a rope and {pull|pulled} the boy out safely.",
"The boy, who was {frightening|frightened}, was given first aid.",
"Doctors said that he {is|was} out of danger.",
"His parents thanked the team {from|with} tears in their eyes.",
])

OI = "In the passage below, one word has been omitted in each line. The omitted word is shown in the key. Put a slash (/) where the word is missing and write the missing word in the space provided."
B += omit('B','B3.1','Omission — Police and Public',OI,[
"One thing we all must do [is] to cooperate with the police.",
"We should pay heed [to] their advice at all times.",
"They warn us not to touch unidentified [and] unclaimed objects.",
"We need to watch [out] for abandoned cars and scooters.",
"Anything suspicious must [be] reported at once.",
"The police control room can be reached [by] dialling 100.",
"Always report suspicious objects [to] the nearest police station.",
"Public cooperation [makes] the work of the police easier.",
])
B += omit('B','B3.2','Omission — My Grandmother',OI,[
"My grandmother lives [in] a small village near Ajmer.",
"She wakes up [at] five every morning.",
"After a bath, she prays [for] half an hour.",
"Then she milks [the] cow and prepares tea for everyone.",
"She tells us stories [about] her childhood.",
"Her stories are full of lessons [and] humour.",
"She [has] never been to a city.",
"Yet she is [the] wisest person I know.",
])
B += omit('B','B3.3','Omission — Healthy Habits',OI,[
"A healthy body [is] the foundation of a happy life.",
"We should [eat] fresh food and avoid junk food.",
"Drinking enough water [helps] the body stay fit.",
"Regular exercise keeps us active [and] cheerful.",
"Many people complain [of] lack of time.",
"But even a short walk is better [than] no exercise.",
"Sleeping on time is [also] important.",
"If we follow these habits, we [will] stay healthy.",
])
B += omit('B','B3.4','Omission — The Railway Station',OI,[
"The railway station was crowded [with] passengers.",
"Porters were running [here] and there with luggage.",
"A voice from the loudspeaker [announced] that the train was late.",
"Many people were sitting [on] benches and reading newspapers.",
"A small boy was selling tea [to] the waiting passengers.",
"At last the train [arrived] with a loud whistle.",
"Passengers rushed [towards] their coaches.",
"Within minutes the platform [became] quiet again.",
])
B += omit('B','B3.5','Omission — Digital India',OI,[
"Digital India is a campaign [to] make government services available online.",
"Today people can pay bills [from] home.",
"Farmers can check the prices [of] crops on their phones.",
"Students can attend classes [through] the internet.",
"This has saved a lot [of] time and money.",
"However, many villages still [lack] good internet connections.",
"Efforts are [being] made to solve this problem.",
"A digitally literate India [will] be a stronger nation.",
])
B += omit('B','B3.6','Omission — A Rainy Day',OI,[
"It had been raining [since] early morning.",
"The streets were [full] of water.",
"Children were sailing paper boats [in] the puddles.",
"I stood at the window and [watched] them.",
"My mother brought [me] a cup of hot tea.",
"The smell of wet earth made [me] very happy.",
"By evening the rain [had] stopped.",
"A rainbow appeared [in] the sky.",
])
B += omit('B','B3.7','Omission — The Tiger',OI,[
"The tiger is [the] national animal of India.",
"It is found [in] forests and grasslands.",
"Tigers are good swimmers [and] love to rest in water.",
"A tiger can eat [up] to thirty kilograms of meat at a time.",
"Their numbers fell [because] of hunting and loss of habitat.",
"Several reserves [have] been set up to protect them.",
"It is our duty [to] save this great animal.",
"Without tigers, the forest ecosystem [is] in danger.",
])
B += omit('B','B3.8','Omission — School Assembly',OI,[
"Our school assembly begins [at] 7.45 a.m.",
"Students stand [in] neat lines according to their classes.",
"We sing the prayer [and] the national anthem.",
"Then a student reads [out] the news headlines.",
"The Principal sometimes gives [a] short speech.",
"Announcements [are] made before we go to classes.",
"The assembly teaches us discipline [and] unity.",
"I look forward [to] it every day.",
])
