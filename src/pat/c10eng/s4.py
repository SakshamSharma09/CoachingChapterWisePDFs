from lib_eng import *
S = dict(set_no=4)
p1 = [
 "When India's first satellite, Aryabhata, was carried into orbit in 1975 aboard a foreign rocket, few people imagined that the country would one day launch dozens of satellites in a single mission. Yet India's space programme has travelled a remarkable distance since those modest beginnings. Today the Indian Space Research Organisation, ISRO, builds its own rockets, sends probes to the Moon and Mars, and earns respect for doing so at a fraction of the cost spent by other nations.",
 "The programme was never meant merely to win prestige. From its early days, its leaders insisted that space science must serve ordinary people. Satellites now provide weather warnings that help fishermen return safely before a cyclone, maps that guide farmers on soil and water, and communication links to remote villages and hill stations. During floods and earthquakes, images from space help rescue teams to decide where to reach first. Even a small village school can now take lessons through a satellite link, which would have seemed impossible a generation ago. The benefits therefore reach people who may never see a rocket or know the name of a single scientist.",
 "Costs have been kept low through careful planning and the reuse of designs. Engineers often modify existing technology rather than start afresh, and many parts are manufactured within the country. The Mars Orbiter Mission of 2014, for example, cost less than the budget of several Hollywood films, and it made India the first Asian nation to reach Martian orbit at the first attempt. Another mission, Chandrayaan-3, landed near the Moon's south pole in 2023, a region that no other country had reached, and brought lasting pride to a whole generation of young Indians.",
 "A new chapter has begun with the opening of the sector to private companies. Young start-ups now design small satellites, rocket engines and tools for analysing satellite data. Students in colleges and even schools build tiny satellites that are launched alongside larger ones, giving thousands of young people a chance to take part in real space missions. Many of these young designers say that the best part of the work is learning to solve problems with limited money, a skill that serves them in any career.",
 "The road ahead is not free of challenges. Space debris is growing, competition is intense, and every launch demands years of patient work. Nevertheless, a country that once borrowed a rocket now plans missions with astronauts of its own. The story of the programme shows how careful planning and a clear purpose can turn limited resources into great achievements.",
]
p1parts = [
 P("Why was it surprising that India later launched dozens of satellites in one mission? (Paragraph 1)", 1, "Because in 1975 it needed a foreign rocket to launch its first satellite."),
 P("According to Paragraph 2, satellites help people in all of the following ways EXCEPT", 1, "Nothing is said about satellites producing electricity for villages.", ["warning fishermen about cyclones", "guiding farmers about soil and water", "connecting remote villages", "supplying electricity to villages"], 'd'),
 P("Complete the following by selecting the correct option from those in the brackets: The programme was meant to serve __________ rather than only win prestige. (ordinary people / foreign nations) (Paragraph 2)", 1, "ordinary people"),
 P("Select the option that is TRUE about the Mars Orbiter Mission, according to Paragraph 3.", 1, "It made India the first Asian nation to reach Mars orbit at the first attempt.", ["It cost more than several films.", "It made India the first Asian nation to reach Mars orbit at the first attempt.", "It used only foreign parts.", "It failed to reach Mars."], 'b'),
 P("Complete the analogy by selecting the correct option.<br>Start-up : Small satellite :: Student team : ______", 1, "Tiny satellite.", ["Tiny satellite", "Mars mission"], 'a'),
 P("How has ISRO managed to keep the cost of its missions low? (Paragraph 3)", 2, "It modifies existing technology instead of starting afresh (1); many parts are made within the country (1)."),
 P("What are the main ideas of Paragraph 4 and Paragraph 5?<br>i. The sector is open to private companies and students.<br>ii. The programme faces challenges but has shown the power of planning.<br>iii. Space research should be stopped.<br>iv. Satellites are of no use.<br>v. Rockets must be imported.", 1, "Paragraph 4 — i; Paragraph 5 — ii.", None, 'b', table(["Option", "Main idea of Paragraph 4", "Main idea of Paragraph 5"], [["A", "iii", "iv"], ["B", "i", "ii"], ["C", "ii", "v"], ["D", "iv", "iii"]])),
 P("What can you infer about the future of India's space programme from the last paragraph? (Paragraph 5)", 2, "It will continue to grow, with human missions planned (1); success depends on patient work and a clear purpose despite debris and competition (1)."),
]
p2 = [
 "A survey of 500 shoppers in a city market studied the use of plastic bags. The results were mixed. About 60% of the shoppers (300) said that they carried their own cloth or jute bags, while the other 40% (200) depended on bags given by shopkeepers, often for a few rupees or even free of cost. Among the latter, 70% (140) said that plastic was more convenient, and 30% (60) said they simply forgot to bring a bag.",
 "The survey also tested awareness of the local ban on thin plastic bags. In all, 55% of the shoppers (275) knew about the ban. Among those who carried their own bags, 225 (75%) were aware of it, compared with only 50 of the 200 others (25%). Officials concluded that awareness encourages better habits, although some of the shoppers who knew the rule still used plastic by choice, saying that cloth bags were heavy to carry and inconvenient to wash.",
 "Shopkeepers suggested that cloth bags should be sold at low cost near the market gate and that customers be offered a small discount for bringing their own. With these steps, they believe, the market could become almost plastic-free within a year. A few customers, however, argued that unless the ban is also enforced at the wholesale level, thin plastic will keep returning to the market in some form or another.",
]
p2parts = [
 P("Why does the author describe the results as 'mixed'? (Paragraph 1)", 1, "Because while many shoppers carry their own bags, a large group still relies on plastic."),
 P("Complete the following by selecting the correct option from the brackets. Of the 200 plastic users, most said plastic is __________. (convenient / harmful) (Paragraph 1)", 1, "convenient"),
 P("Select the option that best explains the word 'aware' in Paragraph 2.", 1, "Having knowledge of something.", ["Afraid of something", "Having knowledge of something", "Angry about something", "Tired of something"], 'b'),
 P("Complete the following. The figures in Paragraph 2 suggest that", 1, "shoppers who know about the ban tend to carry their own bags.", ["the ban is useless.", "shoppers who know about the ban tend to carry their own bags.", "cloth bags are costly.", "shopkeepers dislike the ban."], 'b'),
 P("Complete the analogy by selecting the correct option.<br>Discount : Encouragement :: Fine : ______", 1, "Discouragement / deterrent.", ["Deterrent", "Reward"], 'a'),
 P("Complete the following appropriately. The 60 shoppers who 'forgot to bring a bag' represent ____ % of those who use plastic. (Paragraph 1)", 1, "30"),
 P("How many shoppers in all knew about the ban, and what percentage is this? (Paragraph 2)", 1, "275 shoppers, i.e. 55%."),
 P("Why did officials say that some shoppers still used plastic 'by choice'? (Paragraph 2)", 1, "Because even some who knew the rule used plastic for convenience."),
 P("Suggest two ways in which shopkeepers believe the market can become plastic-free. Why might these steps work? (Paragraph 3)", 2, "Selling cheap cloth bags near the gate and giving a discount to those who bring their own (1); they make the eco-friendly choice easy and rewarding (1)."),
]
S['passages'] = [dict(paras=p1, parts=p1parts), dict(paras=p2, parts=p2parts)]
S['grammar'] = [
 P("Fill in the blank using the correct form of the word in brackets for a school notice:<br>The school takes great ______ (proud) in announcing the success of its team.", 1, "pride"),
 P("Identify the error and write the correction.<br>He gave me an advice about my career.", 1, "Error: an advice — Correction: some/a piece of advice.", extra=errtab()),
 P("Fill in the blank with the correct form of the verb.<br>If I ______ (know) her address, I would have sent the invitation.", 1, "had known"),
 P("Read the given statement.<br>The principal said, “The results will be declared next week.”<br>Report: The principal said that ______________________.", 1, "the results would be declared the following week."),
 P("Fill in the blank by choosing the correct option.<br>The villagers were suffering ______ a severe drought.", 1, "suffer from", ["from", "of", "with", "by"], 'a'),
 P("Report the following.<br>“Don't be late for the rehearsal,” the director told the actors.<br>The director told ______________________.", 1, "the actors not to be late for the rehearsal."),
 P("Complete the sentence by choosing the correct option.<br>_____ the match, the team celebrated all night.", 1, "Having won.", ["Having won", "To win", "Win", "Winning to"], 'a'),
 P("The sentence has an error. Select the option that correctly identifies the error and the correction.<br>One of my cousins live in Canada.", 1, "‘One’ takes a singular verb: live → lives.", None, 'b', table(["No.", "Error", "Correction"], [["A.", "One", "Ones"], ["B.", "live", "lives"], ["C.", "cousins", "cousin"], ["D.", "Canada", "a Canada"]])),
 P("Report the following question.<br>“What are you reading these days?” the librarian asked Rohit.", 1, "The librarian asked Rohit what he was reading those days."),
 P("Choose the correct option from the brackets.<br>It is raining heavily; he ______ (can / may) not have reached home yet.", 1, "may"),
 P("Fill in the blank with the correct option.<br>I have ______ time to waste; please be quick.", 1, "‘no’ is the correct determiner.", ["any", "no", "many", "few"], 'b'),
 P("Identify the error and write the correction.<br>She is the taller of all the girls in the class.", 1, "Error: taller — Correction: tallest.", extra=errtab()),
]
S['q4'] = (
 dict(q="You are Nisha/Nikhil of Class X. A recent examination was marred by loud construction work next to your school. Write a letter to the Municipal Commissioner, in about 120 words, requesting that such work be regulated during examination days.",
      sol="<b>Format (1), Content (2), Fluency (2).</b> Points: nature of noise, effect on concentration, request to stop work during exams, timing restrictions.<br><i>Sample:</i> The Municipal Commissioner, Jaipur / Subject: Request to regulate construction noise. Sir, I am a student of Class X, and I write to bring to your notice that the construction work next to our school causes continuous drilling noise during examinations. Students cannot concentrate, and several papers were disturbed last week. Since the board examinations are approaching, I request you to restrict heavy construction work near schools between 8 a.m. and 3 p.m. on examination days. Kindly instruct the builder to follow noise rules. I am confident that you will take prompt action. Yours faithfully, Nisha Verma."),
 dict(q="You are Samar/Simran, the Secretary of the Eco Club. Write a letter to the Principal, in about 120 words, seeking permission to hold a tree plantation drive in the school campus, with details of the plan.",
      sol="<b>Format (1), Content (2), Fluency (2).</b> Points: date, number of saplings, species, volunteers, care plan, benefits.<br><i>Sample:</i> The Principal, Delhi Public School, Jaipur / Subject: Permission for tree plantation drive. Respected Madam, The Eco Club proposes to hold a plantation drive on 5 November from 9 a.m. to 12 noon. We plan to plant 100 saplings of neem, peepal and gulmohar along the boundary wall. Fifty volunteers from Classes IX to XII will take part, and each class will adopt a few saplings to water and protect. The saplings will be provided by the forest department. I request your kind permission and presence at the function. Yours obediently, Samar Gupta, Secretary, Eco Club."),
)
S['q5'] = (
 dict(q="The school Cultural Committee must choose between two compères for the annual function. <b>Isha:</b> fluent and confident, with a witty sense of humour, but often unprepared and forgets names. <b>Rehan:</b> well prepared and respectful, but speaks softly and becomes nervous before an audience. Analyse the profiles and decide who would be the better compère. (100–120 words)",
      sol="<b>Content (2), Organisation (1), Fluency (2).</b><br><i>Sample:</i> Isha would be the better compère. The job demands confidence and the ability to hold the audience's attention, qualities that she possesses in plenty. Her wit will keep the programme lively. Her weakness of forgetting names is a lesser problem, since it can be solved with a written script and rehearsals. Rehan's preparation and courtesy are admirable, but nervousness and a soft voice would make it difficult for the audience to follow him. With help from Rehan in preparing the script and cue cards, Isha can deliver a smooth and entertaining show."),
 dict(q="The table compares two mobile data plans.<br>" + table(["Features", "Plan X", "Plan Y"], [["Monthly cost", "₹299", "₹499"], ["Data per day", "1.5 GB", "3 GB"], ["Validity", "28 days", "56 days"], ["Calls", "Unlimited", "Unlimited"], ["Extra benefits", "None", "Streaming subscription"]]) + "Study the data and write an analytical paragraph in 100–120 words comparing the plans and recommending the better one for a student who uses data mainly for online classes.",
      sol="<b>Content (2), Analysis/recommendation (1), Fluency (2).</b><br><i>Sample:</i> Plan X costs ₹299 for 28 days, which works out at about ₹10.7 per day, while Plan Y costs ₹499 for 56 days, or about ₹8.9 per day. Plan Y therefore offers better value, gives double the daily data and includes a streaming subscription. However, its upfront cost is higher. For a student who uses data mainly for online classes, 1.5 GB a day may be adequate, so Plan X is cheaper to begin with. Yet over two months Plan Y is more economical and gives enough data for long video lessons. If the student can afford the upfront cost, Plan Y is the wiser choice."),
)
S['q6'] = [
 dict(extract="The Buddha listened to the grieving mother and told her that he could cure her only if she brought him a handful of mustard seeds. But the seeds must come from a house where no one had ever died. She went from door to door, and everywhere she heard the same story of loss.", src="The Sermon at Benares — extract adapted",
      parts=[P("What did the Buddha ask Kisa Gotami to bring?", 1, "Mustard seeds.", ["Medicine", "Mustard seeds", "Water", "Flowers"], 'b'),
             P("What condition did he put on the seeds?", 1, "They must come from a house where no one had died."),
             P("Complete suitably. Kisa Gotami's search taught her that death is __________.", 1, "universal.", ["rare", "universal", "a punishment", "avoidable"], 'b'),
             P("How does the Buddha's method help Kisa Gotami accept her loss? Answer in about 40 words.", 2, "He lets her discover for herself that everyone suffers loss (1); the realisation brings acceptance and peace (1).")]),
 dict(extract="Lomov arrived in his best clothes to ask for Natalya's hand. Before long, the talk turned to who owned the Oxen Meadows, and voices were raised. Chubukov, her father, took her side, and the suitor's nervous heart began to hurt so much that he almost fainted.", src="The Proposal — extract adapted",
      parts=[P("What was the cause of the quarrel?", 1, "Ownership of the Oxen Meadows.", ["A dog", "Oxen Meadows", "A wedding date", "A loan"], 'b'),
             P("Why did Lomov come to Chubukov's house?", 1, "To propose to Natalya."),
             P("Complete suitably. The scene is mainly __________.", 1, "comic.", ["tragic", "comic", "serious", "solemn"], 'b'),
             P("How does the extract show that the characters are quarrelsome by nature? Answer in about 40 words.", 2, "They argue over trivial matters (1); each becomes angry quickly and Lomov's health suffers from excitement (1).")]),
]
S['q7'] = [
 dict(extract="The poet describes a girl who is told by her mother to put away her toys, to tidy her hair, to sit straight and to stop dreaming. Amanda wishes only to be a mermaid in a lonely sea, or to be alone like Robin Redbreast in a tree, where nobody would give her orders.", src="Amanda! — paraphrased",
      parts=[P("What does Amanda want to become?", 1, "A mermaid.", ["A bird", "A mermaid", "A queen", "A teacher"], 'b'),
             P("Who gives Amanda the commands?", 1, "Her mother / elders.", ["Her friends", "Her mother", "Her teacher", "The poet"], 'b'),
             P("The poem shows Amanda's __________.", 1, "longing for freedom.", ["fear of water", "longing for freedom", "disobedience", "ill health"], 'b'),
             P("How does the poem show a child's need for freedom? Answer in about 40 words.", 2, "Amanda is constantly given orders (1); her daydream of a mermaid and a bird shows her wish to escape control (1).")]),
 dict(extract="The brave Custard the dragon lay down quietly and cried while everyone else boasted. When the pirate came, however, it was he who leapt up and fought, gobbled the pirate, and then returned to his place, hungry for praise but quite content to be called a coward again.", src="The Tale of Custard the Dragon — paraphrased",
      parts=[P("How did the others treat Custard?", 1, "They called him a coward.", ["As a hero", "They called him a coward", "As a king", "As a guest"], 'b'),
             P("What did Custard do when the pirate came?", 1, "He fought and defeated him."),
             P("The poem is mainly __________.", 1, "humorous.", ["tragic", "humorous", "serious", "mournful"], 'b'),
             P("What does the poem suggest about real courage? Answer in about 40 words.", 2, "True courage is shown in action, not words (1); Custard was brave when needed, while the boasters were not (1).")]),
]
S['q8'] = [
 ("What was the mistake made by the doctor in 'A Triumph of Surgery'? Why did Tricki improve? (A Triumph of Surgery)", "Mr Herriot did not operate (1); he treated Tricki with a plain diet and exercise (1); Mrs Pumphrey believed it was a surgical triumph (1)."),
 ("How does the pilot's meeting with the black aeroplane show courage? (Two Stories about Flying)", "He kept flying through the storm (1); he followed the unknown plane (1); he landed safely and felt grateful (1)."),
 ("Describe Anne Frank's feelings about Mr Dussel. (From the Diary of Anne Frank)", "She finds him dull and fussy (1); he keeps correcting her (1); she is irritated by his views on manners (1)."),
 ("How does the conductor treat Valli when she boards the bus? (Madam Rides the Bus)", "Valli is a small girl (1); she acted like a lady, and he treated her seriously (1); she paid the full fare and sat like a grown-up (1)."),
 ("How does the Tiger in the Zoo contrast with his wild life? (A Tiger in the Zoo)", "In the zoo he paces his cage (1); in the wild he stalks near the village (1); the poet contrasts confinement and freedom (1)."),
]
S['q9'] = [
 ("How does Bholi's father show his love for her in the end? (Bholi)", "He is helpless and ashamed (1); he welcomes her choice (1); the daughter's confidence changes his view (1)."),
 ("What does the story 'A Question of Trust' teach about misplaced trust? (A Question of Trust)", "Horace trusted a stranger who tricked him (1); she took advantage of his honesty (1); we should be careful before trusting strangers (1)."),
 ("Why was the Book That Saved the Earth a comic tale? Mention two humorous ideas. (The Book That Saved the Earth)", "The Martians mistake a nursery rhyme for a serious book (1); they decide to attack Earth (1); the 'Humpty Dumpty' misunderstanding saves Earth (1)."),
]
S['q10'] = (
 ("Compare how Natalya and Lomov in 'The Proposal' and Mrs Pumphrey and Tricki in 'A Triumph of Surgery' bring out the humour of human behaviour. (The Proposal / A Triumph of Surgery)", "<b>Points:</b> Lomov's hypochondria; Natalya's stubbornness; Mrs Pumphrey's pampering; Tricki's overeating; both satirise human folly; humour through exaggeration. (2+2+2)"),
 ("Discuss how 'Amanda!' and 'The Ball Poem' present childhood experiences and what lessons each offers. (Amanda! / The Ball Poem)", "<b>Points:</b> Amanda's need for freedom; the boy's loss; the poet's comment on responsibility; contrast in tone; lessons about growing up. (2+2+2)"),
)
S['q11'] = (
 ("'The Sermon at Benares' teaches that grief can be overcome through understanding. Discuss. (The Sermon at Benares)", "<b>Points:</b> Kisa Gotami's grief; the mustard seed; the search; realisation; Buddha's teaching of universality of death; her acceptance. (2+2+2)"),
 ("'Humour and irony make 'The Proposal' a lively play.' Discuss with examples. (The Proposal)", "<b>Points:</b> Lomov's ailments; quarrel over meadows and dogs; Chubukov's intervention; sudden reconciliation; satire on greed. (2+2+2)"),
)
if __name__ == '__main__':
    for i, ps in enumerate(S['passages']): print(i, wc(ps['paras']))
    build(S, '/home/claude/pat/out/Class10_English/'); print('built')
