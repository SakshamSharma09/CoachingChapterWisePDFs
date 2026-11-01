from yhelp import items, gap, passage, reorder
B = []
O = lambda *a: tuple(a)
RI = "Rearrange the words and phrases to form meaningful sentences."
B += reorder('B','B4.1','Reordering — Set 1',RI,[
"One of the best / thirst quenchers / in summer / is the watermelon.",
"It is cultivated / in many countries / around the world.",
"It was first grown / in Africa / about five thousand years ago.",
"Some researchers say / that it was grown / in India / at the same time.",
"Travellers used it / as a source of water / when they crossed / a desert.",
"The fruit contains / a lot of water / and many vitamins.",
])
B += reorder('B','B4.2','Reordering — Set 2',RI,[
"Discipline / has no parallel / in any walk of life.",
"Duties and rights / should go together / in a good society.",
"They should be treated / as equally important / for a satisfying life.",
"If one is ignored, / it will prove very bad / for the other.",
"A disciplined student / makes the best use / of his time.",
"Self-discipline / is the key / to lasting success.",
])
B += reorder('B','B4.3','Reordering — Set 3',RI,[
"Koalas get / all their water / from the leaves they eat.",
"So, in areas inhabited by koalas, / the demand for tree leaves / is high.",
"It takes several acres of trees / to support / one group of koalas.",
"Each adult koala / can eat up to one and a half kilograms / of leaves every day.",
"Koalas spend / most of the day / sleeping in trees.",
"Bushfires / are a serious threat / to their homes.",
])
B += reorder('B','B4.4','Reordering — Set 4',RI,[
"The Veena / has been depicted / in temple architecture / since about 500 A.D.",
"Sadly, / the instrument / today has few takers.",
"There are / few exponents / to whom students can turn.",
"It is not offered / even as a subsidiary subject / in university curricula.",
"Classical instruments / need support / from schools and society.",
"Our heritage / will survive / only if we preserve it.",
])
B += reorder('B','B4.5','Reordering — Set 5',RI,[
"High blood pressure / is the main cause / of a paralytic attack.",
"People affected / by a stroke / may not be able to speak.",
"Some can communicate / only / with their eyes.",
"Damage to the nervous system / makes even a small gesture / impossible.",
"Regular check-ups / can detect / high blood pressure early.",
"A balanced diet / and exercise / help keep it under control.",
])
B += reorder('B','B4.6','Reordering — Set 6',RI,[
"When my parents went to the city, / they left me / with my grandmother.",
"She used to wake me up / early / in the morning.",
"She sang / prayers in a monotonous voice / every morning.",
"I loved her voice / because / it was so soothing.",
"She told me stories / until / I fell asleep.",
"I still remember / those happy days / spent with her.",
])
B += reorder('B','B4.7','Reordering — Set 7',RI,[
"The library / remains open / from nine to five.",
"Students are allowed / to borrow / two books at a time.",
"A fine is charged / if the books / are returned late.",
"The librarian helps / readers / choose suitable books.",
"Newspapers and magazines / are kept / in the reading room.",
"Silence must be maintained / so that / no one is disturbed.",
])
B += reorder('B','B4.8','Reordering — Set 8',RI,[
"Plastic bags / are choking / our drains and rivers.",
"We should switch / to cloth bags / and reusable bottles.",
"The government / has banned / single-use plastic in many cities.",
"Everyone must do / his or her part / to keep the environment clean.",
"A cleaner city / begins / with cleaner habits.",
"Small steps / taken together / can bring big change.",
])

DI = "Complete the conversation by choosing the correct option for each blank."
B += gap('B','B5.1','Dialogue Completion — Planning a Trip',DI,
"Sister: When do you leave for Mumbai?\nBrother: I am leaving the day after tomorrow.\nSister: Where have you decided to stay?\nBrother: [1]\nSister: Why are you not staying with Aunt and Uncle?\nBrother: [2] I won't be able to enjoy my holidays.\nSister: Don't tell me you'll stay in a hotel!\nBrother: Definitely not. [3]\nSister: How are you both spending your vacation?\nBrother: [4]",
[(O("I won't decide as yet.","I haven't decided as yet.","I hadn't decided as yet.","I don't decide as yet."),1),(O("They were too strict.","They are too strict.","They will be too strict.","They are too funny."),1),(O("I plan to stay with Rahul.","I plan to stay in a hotel.","I won't stay with anyone.","I plan to stay with Aunt."),0),(O("We'll go nowhere.","We'll go sightseeing.","We'll stay inside.","We'll go somewhere else not."),1)])
B += gap('B','B5.2','Dialogue Completion — At the Doctor',DI,
"Doctor: How long have you been sick?\nPatient: I have been having this headache [1] one month.\nDoctor: Have you taken any medicine?\nPatient: No. But I [2] by an eye specialist.\nDoctor: What did he say?\nPatient: He said my eyes are fine.\nDoctor: [3] sleeping late at night?\nPatient: No, I sleep regularly at 10 p.m.\nDoctor: Have you [4] in the past or lately?\nPatient: No, but I had injured my head when I was ten.",
[(O("for the past","since the past","during the past","for a past"),0),(O("got my eye test","will get my eyes","got my eyes tested","would get my eye"),2),(O("Has you been","Had you been","Have you been","Had you be"),2),(O("met with an accident","meets with an accident","meet with an accident","meeting with an accident"),0)])
B += gap('B','B5.3','Dialogue Completion — A Phone Call',DI,
"David: Hello. Is this 26857903?\nMeenu: Yes, [1]?\nDavid: Could I speak to Meenu? I am her friend, David.\nMeenu: David? It's Meenu. [2]?\nDavid: I am calling from the Indira Gandhi International Airport. I am here for a visit.\nMeenu: That's great. [3] about your visit?\nDavid: I wanted to give you a surprise.\nMeenu: When did you arrive? [4]?\nDavid: I just got here and I am alone.",
[(O("shall I know to whom do you want to talk","will I know which do you want to talk","may I know who is speaking","may I know who do you want to speak to"),2),(O("From where you are calling","Where you are calling from","Where are you calling from","You are calling from where"),2),(O("Why you did not inform me","Why didn't you inform me earlier","Why you didn't informed me","Why didn't you informed me"),1),(O("Are you being accompanied by someone","You are being accompanied by someone","Are someone accompanying you","Is anyone accompanied you"),0)])
B += gap('B','B5.4','Dialogue Completion — At the Bookshop',DI,
"Customer: Do you have a good dictionary for Class 10?\nShopkeeper: [1] Here are two editions.\nCustomer: [2] is the difference between them?\nShopkeeper: The newer one has more words and pictures.\nCustomer: [3] is the price of the newer one?\nShopkeeper: It costs three hundred rupees.\nCustomer: That is a bit costly. [4] you give me a discount?\nShopkeeper: I can give you ten per cent off.",
[(O("Yes, we have.","Yes, we are having.","Yes, certainly we do.","Yes, we has."),2),(O("Who","What","Which","Whom"),1),(O("How much","How many","What","Who"),0),(O("Should","Must","Could","Need"),2)])
B += gap('B','B5.5','Dialogue Completion — School Picnic',DI,
"Teacher: Where would you like to go for the picnic?\nStudent: [1]\nTeacher: That place is quite far. How will we reach there?\nStudent: [2]\nTeacher: Have you asked for permission from the Principal?\nStudent: Not yet, madam. [3]\nTeacher: Do that today. And [4]",
[(O("I suggests the zoo.","I suggest the zoo.","I am suggest the zoo.","I suggested the zoo tomorrow."),1),(O("We can hire a bus.","We can hires a bus.","We hire can a bus.","We can to hire a bus."),0),(O("I will go to meet her now.","I will went to meet her now.","I am go to meet her now.","I had meet her now."),0),(O("collect the money from every students.","collect the money from every student.","collecting the money from each students.","to collect money from every students."),1)])
B += gap('B','B5.6','Dialogue Completion — Lost and Found',DI,
"Boy: Excuse me, sir. I have lost my bag.\nOfficer: [1] Where did you lose it?\nBoy: I think I [2] it in the bus.\nOfficer: What does it look like?\nBoy: It is a blue bag [3] a school logo on it.\nOfficer: Please fill in this form. We [4] you as soon as we find it.",
[(O("I am sorry to hear that.","I am sorry hearing that.","I sorry to hear that.","I was sorry hear that."),0),(O("leave","leaving","have left","am leaving"),2),(O("with","by","for","of"),0),(O("will inform","inform","informed","have informed"),0)])

RS = "Complete the paragraph by reporting the conversation. Use the correct tense and pronouns."
B += passage('B','B6.1','Reported Speech — Rama and Sita',RS,
["Rama: I am going to the jungle.","Sita: Why?","Rama: I have been banished for fourteen years by my father.","Sita: Oh! It is very sad. Can I go with you?","Rama: No. Stay at home and take care of my old parents."],
"Rama told Sita {a}. She asked him {b}. Rama replied {c}. Sita exclaimed that it was very sad and asked {d}. Rama refused and told her to stay at home and take care of his old parents.",
["that he was going to the jungle","why he was going to the jungle","that he had been banished for fourteen years by his father","if / whether she could go with him"])
B += passage('B','B6.2','Reported Speech — Anita and Prakash',RS,
["Anita: What do you want to do this morning?","Prakash: I feel like taking a walk. It's so nice outside.","Anita: Great, let's walk around the lake in the park.","Prakash: It's really rocky here.","Anita: Yes, watch your step so you don't trip."],
"Anita asked Prakash {a}. Prakash answered that he {b}. He added that it was so nice outside. Anita agreed and suggested {c}. Then Prakash observed that {d}. Anita cautioned him to watch his step.",
["what he wanted to do that morning","felt like taking a walk","that they should walk around the lake in the park","it was really rocky there"])
B += passage('B','B6.3','Reported Speech — Teacher and Student',RS,
["Teacher: Why are you late today?","Student: My bus broke down on the way, sir.","Teacher: Did you inform your parents?","Student: Yes, sir. I called them from a shop.","Teacher: Go to your seat and do not be late again."],
"The teacher asked the student {a}. The student replied respectfully that {b}. The teacher asked him {c}. The student said that he had, and added that {d}. The teacher told him to go to his seat and not to be late again.",
["why he was late that day","his bus had broken down on the way","if / whether he had informed his parents","he had called them from a shop"])
B += passage('B','B6.4','Reported Speech — Shopkeeper and Customer',RS,
["Customer: How much does this jacket cost?","Shopkeeper: It costs two thousand rupees, madam.","Customer: That is too expensive. Can you reduce the price?","Shopkeeper: I will give you a ten per cent discount.","Customer: Thank you. I shall take it."],
"The customer asked the shopkeeper {a}. The shopkeeper replied that {b}. The customer remarked that it was too expensive and asked {c}. The shopkeeper promised {d}. The customer thanked him and said that she would take it.",
["how much that jacket cost","it cost two thousand rupees","if / whether he could reduce the price","that he would give her a ten per cent discount"])
B += passage('B','B6.5','Reported Speech — Mother and Son',RS,
["Mother: Where are you going, Rohan?","Rohan: I am going to play cricket, Mother.","Mother: Have you finished your homework?","Rohan: I shall do it after I return.","Mother: Don't stay out after dark."],
"His mother asked Rohan {a}. Rohan replied that {b}. His mother wanted to know {c}. Rohan said {d}. His mother told him not to stay out after dark.",
["where he was going","he was going to play cricket","if / whether he had finished his homework","that he would do it after he returned"])
B += passage('B','B6.6','Reported Speech — Comic Strip: Charlie and Patty',RS,
["Charlie: I am making a list of what I want from Santa Claus. Do you think he can afford all this?","Patty: Everything these days is promotion. If the truth were known, he is financed by some big chain."],
"While making the list of what he wanted from Santa Claus, Charlie asked Patty {a}. Patty replied that {b}. She added that {c}.",
["if / whether she thought Santa could afford all that","everything these days was promotion","if the truth were known, he was financed by some big chain"])
B += passage('B','B6.7','Reported Speech — Interview',RS,
["Reporter: What made you take up cricket?","Player: I watched my father play when I was a child.","Reporter: Do you practise every day?","Player: Yes, I practise for six hours daily.","Reporter: What is your message to young players?","Player: Work hard and never give up."],
"The reporter asked the player {a}. The player replied that {b}. The reporter then asked if {c}. The player said that {d}. When asked about his message to young players, he advised them to work hard and never give up.",
["what had made him take up cricket","he had watched his father play when he was a child","he practised every day","he practised for six hours daily"])
B += passage('B','B6.8','Reported Speech — Station Enquiry',RS,
["Passenger: When does the Jaipur Express leave?","Clerk: It leaves at 6.30 p.m. from platform number four.","Passenger: Is it running on time?","Clerk: No, it is running one hour late.","Passenger: Thank you. I shall wait in the waiting room."],
"The passenger asked the clerk {a}. The clerk replied that {b}. The passenger enquired {c}. The clerk said that {d}. The passenger thanked him and said that he would wait in the waiting room.",
["when the Jaipur Express left","it left at 6.30 p.m. from platform number four","if / whether it was running on time","it was running one hour late"])

H = "Use the information in the headline to complete the news item. Write the missing words."
B += items('B','B7.1','Headlines — Set 1',H,[
("CAPARO ENTERS US MARKET — The Caparo group ______ the North American vehicle market.","has entered"),
("PM TO VISIT JAPAN ON APRIL 11 — The Foreign Minister announced that the Prime Minister ______ in the second week of April.","will visit Japan / will be visiting Japan"),
("TWO KILLED IN BUS ACCIDENT — ______ in a bus accident here on Monday.","Two persons were killed"),
("SIX FLIGHTS DELAYED — There was anger among passengers of six flights ______ for hours at the airport.","that were delayed"),
("CITY GETS NEW PARK — The municipal corporation ______ a new park in the city.","has opened / opened"),
])
B += items('B','B7.2','Headlines — Set 2',H,[
("CHINA DEVELOPS MEDICAL ROBOT — A university in China ______ that can conduct surgeries.","has developed a medical robot"),
("KIDS FALL ILL AFTER MID-DAY MEAL — Five children of a primary school ______ after having the mid-day meal.","fell ill"),
("SPORTS WEEK ENDS — A week-long sports celebration in the schools ______ on 22 April with a prize distribution.","ended"),
("BUS CRUSHES GIRL TO DEATH — A four-year-old girl ______ to death when a speeding bus ran over her.","was crushed"),
("5 LAKH JOBS TO BE CREATED BY 2030 — A member of the Planning Commission said that ______ by the year 2030.","five lakh jobs would be created"),
])
B += items('B','B7.3','Headlines — Set 3',H,[
("STUDENTS SWEEP STATE QUIZ — Students of our school ______ the state-level quiz competition.","swept / have swept"),
("RIVER CLEANING DRIVE LAUNCHED — The district administration ______ a drive to clean the river.","has launched / launched"),
("FIRE DESTROYS MARKET — A fire ______ the main market last night.","destroyed"),
("TEACHERS TO GET TRAINING — The department said that all teachers ______ training next month.","will get / would get"),
("RECORD RAIN LASHES CITY — The city ______ record rainfall on Sunday.","received / recorded"),
])
B += items('B','B7.4','Headlines — Set 4',H,[
("FARMERS PROTEST OVER PRICES — Farmers ______ outside the collectorate demanding better prices.","protested / are protesting"),
("INDIA WINS SERIES — India ______ the series by two matches to one.","won / have won"),
("NEW BRIDGE OPENED FOR TRAFFIC — The new bridge ______ for traffic yesterday.","was opened"),
("SCHOOLS TO REMAIN CLOSED — The Education Minister announced that schools ______ closed till Monday.","would remain / will remain"),
("THIEF CAUGHT RED-HANDED — A thief ______ red-handed by villagers while breaking into a house.","was caught"),
])
B += items('B','B7.5','Headlines — Set 5',H,[
("LIBRARY GETS 1,000 NEW BOOKS — The school library ______ one thousand new books.","has received / received"),
("BOY SAVES DROWNING CHILD — A teenaged boy ______ a drowning child in the lake.","saved / has saved"),
("PRICES OF VEGETABLES FALL — The prices of vegetables ______ sharply this week.","have fallen / fell"),
("CYCLONE TO HIT COAST TOMORROW — The weather office said that a cyclone ______ the coast tomorrow.","will hit"),
("OLDEST TEMPLE RESTORED — The oldest temple in the town ______ by the archaeology department.","has been restored / was restored"),
])
B += items('B','B7.6','Headlines — Set 6',H,[
("YOUNG SCIENTIST WINS AWARD — A young scientist ______ the national award for her invention.","won / has won"),
("METRO TO RUN EVERY FIVE MINUTES — The Metro authority said that trains ______ every five minutes from next month.","will run"),
("POWER CUT HITS EXAM — A power cut ______ the examination in several centres.","disrupted / affected"),
("TREES PLANTED ON ENVIRONMENT DAY — Hundreds of trees ______ in the city on Environment Day.","were planted"),
("MAN ARRESTED FOR FRAUD — A man ______ by the police for cheating many people.","was arrested"),
])

PI = "Read the instructions and complete the passage using the passive voice. A hint is given with each set."
B += passage('B','B8.1','Procedure — Washing White Clothes (hint: are)',PI,
["Collect all the dirty white cotton clothes.","Soak them in a mixture of boiling water and soap.","Take them out and beat them with fists or a stick.","Rinse them in running water until the soap is washed off.","Squeeze them and hang them out to dry."],
"All the dirty white cotton clothes are collected and {a} of boiling water and soap. They {b} with fists or a stick. Then they {c} until the soap is washed off. Finally, they {d} to dry.",
["are soaked in a mixture","are taken out and beaten","are rinsed in running water","are squeezed and hung out"])
B += passage('B','B8.2','Procedure — Making Noodles (hint: is/are)',PI,
["Boil 500 ml of water in a pan.","Add the noodles and the spice mix.","Add finely chopped vegetables after steaming them.","Cook for only two minutes.","Serve hot."],
"Firstly, 500 ml of water {a} in a pan. After that, the noodles and the spice mix {b}. Then finely chopped vegetables {c} after they have been steamed. The mixture {d} for only two minutes. It is then served hot.",
["is boiled","are added","are added","is cooked"])
B += passage('B','B8.3','Procedure — Planting a Sapling (hint: is/are)',PI,
["Dig a pit about one foot deep.","Fill it with manure and soil.","Place the sapling in the centre of the pit.","Press the soil around it.","Water it every day."],
"A pit about one foot deep {a}. It {b} with manure and soil. The sapling {c} in the centre of the pit. The soil {d} around it. Then the sapling is watered every day.",
["is dug","is filled","is placed","is pressed"])
B += passage('B','B8.4','Procedure — How a Letter Travels (hint: is/are)',PI,
["Write the address clearly on the envelope.","Put a stamp on it.","Drop it in the letter box.","The postman collects the letters from the box.","The sorting office sorts them by town."],
"The address {a} clearly on the envelope. A stamp {b} on it, and it is dropped in the letter box. The letters {c} from the box by the postman. At the sorting office they {d} by town.",
["is written","is put / is fixed","are collected","are sorted"])
B += passage('B','B8.5','Procedure — Preparing Tea (hint: is)',PI,
["Boil a cup of water in a pan.","Add tea leaves and sugar to it.","Pour in half a cup of milk.","Let it boil for two minutes.","Strain it into cups."],
"First, a cup of water {a} in a pan. Tea leaves and sugar {b} to it. Then half a cup of milk {c}. It {d} to boil for two minutes. At last the tea is strained into cups.",
["is boiled","are added","is poured in","is allowed / is left"])
B += passage('B','B8.6','Procedure — Recycling Paper (past hint: was/were)',PI,
["Collect the waste paper.","Soak it in water.","Grind it into pulp.","Spread the pulp on a screen.","Dry it in the sun."],
"At the recycling unit, the waste paper {a} first. It {b} in water and then {c} into pulp. The pulp {d} on a screen and dried in the sun.",
["was collected","was soaked","ground","was spread"])

T = "Rewrite each sentence as directed, without changing its meaning."
B += items('B','B9.1','Transformation — Set 1',T,[
("She is too weak to walk. (Use 'so ... that')","She is so weak that she cannot walk."),
("He is the tallest boy in the class. (Use comparative)","He is taller than any other boy in the class."),
("Because it rained, the match was cancelled. (Use 'due to')","The match was cancelled due to the rain."),
("Walking fast, he reached the station. (Use 'as')","As he walked fast, he reached the station."),
("Unless you work hard, you will fail. (Use 'if')","If you do not work hard, you will fail."),
("He said, “I shall help you.” (Indirect)","He said that he would help me."),
("She sings well. (Begin: She is ...)","She is a good singer."),
("Please open the window. (Passive)","You are requested to open the window. / Let the window be opened."),
("No sooner did he arrive than it began to rain. (Use 'as soon as')","As soon as he arrived, it began to rain."),
("The boy was so tired. He fell asleep at once. (Join)","The boy was so tired that he fell asleep at once."),
])
B += items('B','B9.2','Transformation — Set 2',T,[
("Though he is rich, he is unhappy. (Use 'but')","He is rich but he is unhappy."),
("I am sure that he will win. (Use 'sure of')","I am sure of his winning. / I am sure of his victory."),
("It is raining. We cannot play. (Join with 'so')","It is raining, so we cannot play."),
("The thief ran away. The policeman came. (Use 'before')","The thief ran away before the policeman came."),
("He is a man of honour. (Use adjective)","He is an honourable man."),
("As soon as the teacher entered, the students stood up. (Use 'no sooner')","No sooner did the teacher enter than the students stood up."),
("This book is mine. (Use 'belongs')","This book belongs to me."),
("He worked hard. He wanted to win. (Use 'to')","He worked hard to win."),
("She was punished for her laziness. (Use 'because she')","She was punished because she was lazy."),
("Mohan is better than all the other boys. (Superlative)","Mohan is the best boy."),
])
B += items('B','B9.3','Transformation — Set 3',T,[
("“Where does he live?” she asked. (Indirect)","She asked where he lived."),
("She said, “Don't make a noise.” (Indirect)","She told them not to make a noise."),
("Everyone loves a kind person. (Passive)","A kind person is loved by everyone."),
("I have not seen him since last Monday. (Use 'for'; today is Friday)","I have not seen him for five days."),
("If I were rich, I would travel the world. (Use 'wish')","I wish I were rich so that I could travel the world."),
("He is the man. I saw him yesterday. (Join with 'whom')","He is the man whom I saw yesterday."),
("It is a pity that he failed. (Use 'unfortunately')","Unfortunately, he failed."),
("The girl is beautiful. She won the contest. (Join with 'who')","The girl who won the contest is beautiful."),
("He ran fast but could not catch the bus. (Use 'although')","Although he ran fast, he could not catch the bus."),
("We must obey the law. (Passive)","The law must be obeyed."),
])
B += items('B','B9.4','Transformation — Set 4',T,[
("The Principal praised the winners. (Passive)","The winners were praised by the Principal."),
("He is too proud to apologise. (Use 'so ... that')","He is so proud that he cannot apologise."),
("Having completed the work, he went out. (Use 'after')","After he had completed the work, he went out."),
("Rita is not as clever as Seema. (Comparative)","Seema is cleverer than Rita."),
("I don't know what to do. (Use 'idea')","I have no idea what to do."),
("He is not only rich but also generous. (Use 'both ... and')","He is both rich and generous."),
("Do you know the answer? (Reported: He asked me)","He asked me if I knew the answer."),
("The sun having set, we returned home. (Use 'as')","As the sun had set, we returned home."),
("She is so poor that she cannot buy books. (Use 'too ... to')","She is too poor to buy books."),
("His arrival surprised us. (Verb form)","We were surprised when he arrived."),
])
B += items('B','B9.5','Transformation — Set 5',T,[
("It is necessary to save water. (Use 'must')","We must save water."),
("Although he was ill, he came to school. (Use 'in spite of')","In spite of his illness, he came to school."),
("You must run, otherwise you will miss the train. (Use 'unless')","Unless you run, you will miss the train."),
("The earthquake destroyed the town. (Passive)","The town was destroyed by the earthquake."),
("Whoever works hard succeeds. (Use 'If')","If anyone works hard, he succeeds."),
("He was foolish to trust them. (Use 'foolishness')","It was foolishness on his part to trust them."),
("He asked, “Are you ready?” (Indirect)","He asked if I was ready."),
("The teacher is kind. He taught us last year. (Join with 'who')","The teacher who taught us last year is kind."),
("It was a difficult exam. Everyone passed. (Use 'although')","Although it was a difficult exam, everyone passed."),
("She cannot but laugh. (Use 'help')","She cannot help laughing."),
])
B += items('B','B9.6','Transformation — Set 6',T,[
("The bus was late. We missed the film. (Join with 'because')","We missed the film because the bus was late."),
("Nobody can solve this problem. (Passive)","This problem cannot be solved by anybody."),
("This is the best film I have seen. (Use 'never')","I have never seen a better film than this."),
("My brother is taller than I. (Positive)","I am not as tall as my brother."),
("He is rich. He is not happy. (Use 'though')","Though he is rich, he is not happy."),
("The patient died before the doctor arrived. (Use 'had')","The patient had died before the doctor arrived."),
("Avoid sweets if you want to stay healthy. (Use 'unless')","Unless you avoid sweets, you will not stay healthy."),
("Her singing delighted everybody. (Begin: Everybody ...)","Everybody was delighted by her singing."),
("As he was ill, he did not go to school. (Use 'because of')","Because of his illness, he did not go to school."),
("I will call you when I reach home. (Use 'on')","On reaching home, I will call you."),
])
B += items('B','B9.7','Transformation — Set 7',T,[
("The shopkeeper gave me a discount. (Passive)","I was given a discount by the shopkeeper."),
("You should respect your elders. (Use 'ought')","You ought to respect your elders."),
("She is the youngest in the family. (Comparative)","She is younger than any other member of the family."),
("He insisted that he would go. (Direct)","He said, “I will go.”"),
("It does not matter whether you win or lose. (Use 'whether')","Whether you win or lose does not matter."),
("Swimming is good exercise. (Use 'To swim')","To swim is good exercise."),
("They were playing when it began to rain. (Use 'while' at the beginning)","While they were playing, it began to rain."),
("The man was so weak that he could not stand. (Use 'too')","The man was too weak to stand."),
("Take medicine, or you will not recover. (Use 'if')","If you do not take medicine, you will not recover."),
("He is a good player. (Adverb)","He plays well."),
])
B += items('B','B9.8','Transformation — Set 8',T,[
("I live in this house. My father built it. (Join with 'which')","I live in this house which my father built."),
("The news was shocking. We heard it yesterday. (Join with 'that')","The news that we heard yesterday was shocking."),
("Nobody was present. (Use 'everybody')","Everybody was absent."),
("It is the duty of every citizen to pay taxes. (Use 'should')","Every citizen should pay taxes."),
("If he had not helped me, I would have failed. (Use 'but for')","But for his help, I would have failed."),
("What a lovely garden! (Assertive)","It is a very lovely garden."),
("Is it not a pleasant evening? (Assertive)","It is a very pleasant evening."),
("They elected him captain. (Passive)","He was elected captain by them."),
("She was crying because she had lost her pen. (Use 'cause')","The cause of her crying was the loss of her pen."),
("The more you read, the more you learn. (Use 'if')","If you read more, you will learn more."),
])
