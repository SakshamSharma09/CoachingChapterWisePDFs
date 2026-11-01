from yhelp import items, gap, edit, omit, reorder, passage
C = []
O = lambda *a: tuple(a)
GI = "Q1. Fill in each blank with the most appropriate option. (½ × 8 = 4)"
DI = "Q2. Complete the conversation by choosing the correct option for each blank. (1 × 4 = 4)"
RI = "Q2. Complete the paragraph by reporting the conversation. (1 × 4 = 4)"
HI = "Q2. Use the information in the headlines to complete the news items. (1 × 4 = 4)"
PI = "Q2. Read the instructions and complete the passage. (1 × 4 = 4)"
EI = "Q3. The following passage has not been edited. There is one error in each line. Write the incorrect word and its correction. (1 × 4 = 4)"
OI = "Q4. In the passage below, one word has been omitted in each line. Put a slash where it is missing and write the missing word. (1 × 4 = 4)"
SI = "Q5. Rearrange the words and phrases to form meaningful sentences. (1 × 4 = 4)"
def hd(n, cls, extra=""):
    return [("h2", f"Practice Test {n} · Class {cls} · Section C: Grammar (20 marks)"),
            ("p", "Time: 25 minutes. Attempt all questions." + extra)]

# ---------- TEST 1 (Class 9) ----------
C += hd(1, 9)
C += gap('C','C1.Q1','Gap Filling',GI,
"Festivals bring joy [1] our lives. Diwali, [2] is celebrated in autumn, is the festival of lights. Families clean their houses and [3] them with lamps. Children burst crackers, [4] causes noise and air pollution. This year, our colony [5] decided to celebrate a green Diwali. Residents [6] to use only earthen lamps. They will also [7] sweets among the poor. Nobody [8] a happier festival.",
[(O("to","at","by","with"),0),(O("who","which","whose","where"),1),(O("decorate","decorated","decorating","decorates"),0),(O("who","which","what","where"),1),(O("have","has","is","was"),1),(O("have agreed","has agreed","is agreed","agreeing"),0),(O("distribute","distributes","distributing","distributed"),0),(O("can imagine","can imagines","imagining","do imagine"),0)])
C += gap('C','C1.Q2','Dialogue Completion',DI,
"Rita: Where are you off to so early?\nMohan: [1]\nRita: Which train are you taking?\nMohan: The Shatabdi. [2]\nRita: How long does the journey take?\nMohan: [3]\nRita: Will you return the same day?\nMohan: No. [4]",
[(O("I go to the station to receive my uncle.","I am going to the station to receive my uncle.","I went to the station to receive my uncle.","I have going to the station."),1),(O("It leaves at six thirty.","It leave at six thirty.","It is leave at six thirty.","It leaving at six thirty."),0),(O("It takes about four hours.","It take about four hours.","It is taking about four hour.","It taken about four hours."),0),(O("I will stay overnight with my aunt.","I stay overnight to my aunt.","I will staying overnight with my aunt.","I shall stayed overnight."),0)])
C += edit('C','C1.Q3','Editing',EI,[
"Last Sunday we {visit|visited} the zoo with our teacher.",
"There {was|were} many animals that we had never seen.",
"The elephants were {biggest|bigger} than I had imagined.",
"We returned {on|in} the evening feeling tired.",
])
C += omit('C','C1.Q4','Omission',OI,[
"The village school was built [in] 1950.",
"Today it has [over] two hundred students.",
"Most of [them] walk to school every day.",
"Some travel [by] bus from nearby hamlets.",
])
C += reorder('C','C1.Q5','Reordering',SI,[
"Our teacher / asked us / to submit / the project on Monday.",
"The match / was postponed / because of / heavy rain.",
"Regular exercise / keeps / the body / fit and healthy.",
"She has been / learning the piano / for / five years.",
])

# ---------- TEST 2 (Class 9) ----------
C += hd(2, 9)
C += gap('C','C2.Q1','Gap Filling',GI,
"The internet has changed [1] way we learn. A student [2] once spent hours in a library can now find the same information [3] seconds. Online classes [4] become common since the pandemic. [5], not all information on the web is reliable. We must therefore [6] the sources before we believe anything. Parents should also [7] a watch on what their children [8] online.",
[(O("a","an","the","that"),2),(O("who","which","whom","whose"),0),(O("in","on","at","for"),0),(O("has","have","had","are"),1),(O("However","Because","Unless","So that"),0),(O("check","checks","checked","checking"),0),(O("keep","hold","make","take"),0),(O("do","does","did","doing"),0)])
C += passage('C','C2.Q2','Reported Speech',RI,
["Father: Why have you not started your homework?","Son: I was helping Mother in the kitchen.","Father: Finish it before dinner.","Son: I shall do it right now."],
"Father asked his son {a}. The son replied that {b}. Father told him {c}. The son promised that {d}.",
["why he had not started his homework","he had been helping his mother in the kitchen","to finish it before dinner","he would do it right then / immediately"])
C += edit('C','C2.Q3','Editing',EI,[
"My sister {are|is} learning to drive a car.",
"She goes to a driving school {at|in} the morning.",
"Her instructor is {kindest|kinder} than the one before.",
"She hopes to {gets|get} her licence next month.",
])
C += omit('C','C2.Q4','Omission',OI,[
"I always carry [a] bottle of water with me.",
"Water is [important] for the body.",
"Many people forget [to] drink water.",
"This can lead [to] headaches and tiredness.",
])
C += reorder('C','C2.Q5','Reordering',SI,[
"The monsoon / reaches Rajasthan / in / early July.",
"Farmers / have already / sown / their seeds.",
"Several schools / were closed / due to / heavy snowfall.",
"The new library / will be / inaugurated / by the Mayor.",
])

# ---------- TEST 3 (Class 9) ----------
C += hd(3, 9)
C += gap('C','C3.Q1','Gap Filling',GI,
"When I was ten, I [1] a summer in my grandfather's village. Every morning he [2] me to the fields. We would walk [3] the narrow path between the wheat fields. He showed me how crops [4] grown. I [5] never seen a tractor at work before. One day, while we [6] the tractor, it suddenly stopped. The driver, [7] looked worried, called a mechanic. [8] he arrived, it was already dark.",
[(O("spend","spent","have spent","spending"),1),(O("took","takes","taken","had taken"),0),(O("along","among","within","onto"),0),(O("are grown","grows","is grown","were growing"),0),(O("have","had","was","has"),1),(O("watch","watched","were watching","had watched"),2),(O("who","which","whom","whose"),0),(O("By the time","Until","Unless","During"),0)])
C += items('C','C3.Q2','Newspaper Headlines',HI,[
("STUDENTS WIN QUIZ — Students of our school ______ the district quiz contest.","won / have won"),
("PM TO ADDRESS NATION TONIGHT — The Prime Minister ______ the nation tonight.","will address / will be addressing"),
("FIRE DESTROYS GODOWN — A fire ______ a godown near the market last night.","destroyed"),
("THIEF HELD AT STATION — A thief ______ by the police at the railway station.","was held / was arrested"),
])
C += edit('C','C3.Q3','Editing',EI,[
"Our school {have|has} a large playground.",
"Every evening many students {plays|play} on it.",
"The ground is cleaned by the sweeper {ever|every} day.",
"We feel proud {on|of} our school.",
])
C += omit('C','C3.Q4','Omission',OI,[
"Birds build nests [with] twigs and leaves.",
"They lay eggs and [sit] on them for days.",
"After some time the chicks [come] out.",
"The parents feed them [until] they can fly.",
])
C += reorder('C','C3.Q5','Reordering',SI,[
"The old man / was walking slowly / towards / the temple.",
"Neither / the teacher / nor the students / were present.",
"I have / not seen him / since / last year.",
"If you / work hard, / you will / succeed.",
])

# ---------- TEST 4 (Class 9) ----------
C += hd(4, 9)
C += gap('C','C4.Q1','Gap Filling',GI,
"Sports Day is the most awaited event [1] our school year. Students [2] part in races, jumps and team games. This year the chief guest, [3] is an Olympic medallist, [4] the prizes. She told us that hard work [5] always rewarded. Our class [6] the relay race for the third year in a row. We practised [7] two months before the event. It is not [8] winning but taking part that matters.",
[(O("of","at","by","with"),0),(O("takes","take","took","taking"),1),(O("who","whom","which","whose"),0),(O("distributed","distributes","distributing","distribute"),0),(O("is","are","has","have"),0),(O("win","won","wins","winning"),1),(O("for","since","from","during"),0),(O("about","to","at","by"),0)])
C += passage('C','C4.Q2','Procedure Writing',PI,
["Take a clean glass jar.","Fill it with water.","Add three spoons of salt and stir.","Place an egg in the water.","Observe how it floats."],
"First, a clean glass jar {a}. It {b} with water. Three spoons of salt {c} and the water is stirred. Then an egg is placed in the water and its floating {d}.",
["is taken","is filled","are added","is observed"])
C += edit('C','C4.Q3','Editing',EI,[
"The Taj Mahal {were|was} built by Shah Jahan.",
"It attracts {million|millions} of tourists every year.",
"Tourists come {at|to} see its beauty in the moonlight.",
"It is one of the {wonder|wonders} of the world.",
])
C += omit('C','C4.Q4','Omission',OI,[
"Rani wants [to] become a doctor.",
"She studies [for] four hours every day.",
"Her parents are proud [of] her.",
"She [has] never missed a class.",
])
C += reorder('C','C4.Q5','Reordering',SI,[
"Honesty / is / the best / policy.",
"My brother / is taller / than / my father.",
"The thief / was caught / by / the police.",
"They / have been / living here / since 2010.",
])

# ---------- TEST 5 (Class 10) ----------
C += hd(5, 10)
C += gap('C','C5.Q1','Gap Filling',GI,
"Climate change is [1] most serious challenge [2] humanity today. Global temperatures [3] steadily for the past century, and glaciers [4] at an alarming rate. Scientists believe that unless carbon emissions [5] drastically, sea levels [6] rise further. Not only [7] coastal cities face flooding, but farmers also [8] from erratic rains.",
[(O("a","an","the","no article"),2),(O("facing","faced","faces","to face"),0),(O("rise","are rising","have been rising","were rising"),2),(O("melted","are melting","has melted","is melting"),1),(O("are reduced","reduce","will be reduced","were reduced"),0),(O("will","ought","dare","used"),0),(O("do","are","does","will"),0),(O("suffer","suffers","suffered","suffering"),0)])
C += gap('C','C5.Q2','Dialogue Completion',DI,
"Customer: Good morning. I would like to return this mixer grinder.\nShopkeeper: [1]\nCustomer: It stopped working within a week.\nShopkeeper: [2]\nCustomer: Yes, here it is. I bought it on the fifth of this month.\nShopkeeper: [3]\nCustomer: I would prefer a replacement.\nShopkeeper: [4]",
[(O("What seems to be the problem?","What do seem the problem?","Which problem seems to you?","What the problem seems?"),0),(O("Have you brought the bill with you?","Did you brought the bill?","Are you bringing the bill with?","You have brought bill?"),0),(O("Would you like a refund or a replacement?","Do you liked a refund or replacement?","Will you like refund or replace?","Would you likes a refund?"),0),(O("Certainly. We will replace it by tomorrow.","Certainly. We replaced it by tomorrow.","Certain. We are replace it tomorrow.","Certainly. We have replace it by tomorrow."),0)])
C += edit('C','C5.Q3','Editing',EI,[
"Neither of the answers {are|is} correct.",
"The committee has submitted {their|its} report to the minister.",
"The man {whom|who} lives next door is a retired colonel.",
"He suggested me {to|that I should} join the club.",
])
C += omit('C','C5.Q4','Omission',OI,[
"Had I known the truth, I [would] have acted differently.",
"She insisted [on] paying the bill herself.",
"The news was so shocking [that] nobody spoke.",
"He is too proud [to] ask for help.",
])
C += reorder('C','C5.Q5','Reordering',SI,[
"Hardly had / the speaker / begun / when the lights went out.",
"Not only / was he / late, but / he was also rude.",
"It was / the first time / that / I had seen the sea.",
"Were I / in your place, / I would / accept the offer.",
])

# ---------- TEST 6 (Class 10) ----------
C += hd(6, 10)
C += gap('C','C6.Q1','Gap Filling',GI,
"India is fast becoming a hub of start-ups. Young entrepreneurs, [1] ideas once seemed risky, now attract investors. A start-up needs more [2] a good idea; it needs patience, funds and a strong team. Many ventures [3] within a year of their launch, yet some [4] to become global giants. Mr Kapoor, [5] founded a delivery company in 2016, today [6] over a thousand people. He [7] that failure is a stepping stone. Had he given up early, he [8] never have succeeded.",
[(O("who","whom","which","whose"),3),(O("then","than","that","as"),1),(O("fails","fail","failing","to fail"),1),(O("manages","manage","managing","has managed"),1),(O("who","whom","which","whose"),0),(O("employ","employs","employed","employing"),1),(O("believe","believes","believing","has believed"),1),(O("would","will","can","shall"),0)])
C += passage('C','C6.Q2','Reported Speech',RI,
["Interviewer: What inspired you to become a writer?","Writer: My grandmother's stories inspired me.","Interviewer: Do you write every day?","Writer: Yes. I write for three hours every morning."],
"The interviewer asked the writer {a}. The writer replied that {b}. The interviewer then asked {c}. The writer said that {d}.",
["what had inspired him / her to become a writer","his / her grandmother's stories had inspired him / her","if / whether he / she wrote every day","he / she wrote for three hours every morning"])
C += edit('C','C6.Q3','Editing',EI,[
"The doctor advised me {rest|to rest} for a week.",
"I {look|am looking} forward to meeting you.",
"She is {more taller|taller} than her sister.",
"Each of the players {were|was} given a medal.",
])
C += omit('C','C6.Q4','Omission',OI,[
"He is the person [whose] car was stolen.",
"Please wait [until] I return.",
"I congratulate you [on] your success.",
"Unless you hurry, you [will] miss the bus.",
])
C += reorder('C','C6.Q5','Reordering',SI,[
"The more / you practise, / the better / you will play.",
"It is high time / we took / steps / to save water.",
"She asked me / whether / I had / finished my work.",
"Having finished / his homework, / he went / out to play.",
])

# ---------- TEST 7 (Class 10) ----------
C += hd(7, 10)
C += gap('C','C7.Q1','Gap Filling',GI,
"Time and tide wait for [1]. Those [2] waste time later regret it. A student who plans his day well [3] to achieve more than one who does not. Mahatma Gandhi [4] very particular about punctuality. It is said that he never [5] late for any meeting. If we [6] each moment wisely, we [7] our goals easily. As the proverb goes, a stitch in time [8] nine.",
[(O("none","neither","no","anyone"),0),(O("who","which","whom","whose"),0),(O("is likely","likely","are likely","was likely"),0),(O("was","is","were","has been"),0),(O("is","was","were","being"),1),(O("use","using","to use","uses"),0),(O("will achieve","would achieve","achieved","achieving"),0),(O("save","saves","saved","saving"),1)])
C += items('C','C7.Q2','Newspaper Headlines',HI,[
("METRO TO REACH AIRPORT BY 2028 — The Chief Minister said that the Metro ______ the airport by 2028.","would reach / will reach"),
("TWO INJURED IN BUS-TRUCK COLLISION — Two persons ______ when a bus and a truck collided.","were injured"),
("NEW SCHOOL BUILDING INAUGURATED — The new school building ______ by the Governor yesterday.","was inaugurated"),
("RAINS LASH THE CITY — Heavy rain ______ the city for the third day running.","has lashed / has been lashing"),
])
C += edit('C','C7.Q3','Editing',EI,[
"Many a student {have|has} failed in this subject.",
"She is the {tallest|taller} of the two sisters.",
"I have been waiting here {since|for} two hours.",
"He is interested {to learn|in learning} music.",
])
C += omit('C','C7.Q4','Omission',OI,[
"No sooner did he enter [than] the lights went out.",
"I would rather [stay] at home than go out.",
"She is the girl [to] whom I gave the book.",
"Many books were [lying] on the table.",
])
C += reorder('C','C7.Q5','Reordering',SI,[
"No sooner / had he reached / than / the train left.",
"She speaks / as if / she were / the owner.",
"If it / had not rained, / we would have / played the match.",
"The boy / who won / the race / is my cousin.",
])

# ---------- TEST 8 (Class 10) ----------
C += hd(8, 10)
C += gap('C','C8.Q1','Gap Filling',GI,
"Social media has made it easy for people to stay connected, [1] it has also created new problems. Teenagers, in [2], spend hours scrolling through posts. Not only [3] their eyes get tired, but their attention also suffers. Some experts feel that children [4] be allowed accounts before the age of thirteen. Others argue that a total ban [5] not solve the problem. What is needed [6] responsible use. If parents [7] time with their children, they [8] understand their online lives better.",
[(O("but","so","because","or"),0),(O("particular","special","general","detail"),0),(O("do","are","does","will"),0),(O("should","would","used to","need"),0),(O("will","ought","dare","used"),0),(O("is","are","were","have"),0),(O("spend","spending","to spend","will spend"),0),(O("will","would","shall","did"),0)])
C += items('C','C8.Q2','Sentence Transformation',"Q2. Rewrite each sentence as directed. (1 × 4 = 4)",[
("The audience applauded the singer. (Passive)","The singer was applauded by the audience."),
("He is so weak that he cannot lift the box. (Use 'too ... to')","He is too weak to lift the box."),
("Unless you apologise, I will not forgive you. (Use 'if')","If you do not apologise, I will not forgive you."),
("She said to him, “Where are you going?” (Indirect)","She asked him where he was going."),
])
C += edit('C','C8.Q3','Editing',EI,[
"She asked me {that|whether} I had seen her bag.",
"The scissors {is|are} on the table.",
"He has {a|an} MBA degree from Pune.",
"My father is fond {for|of} gardening.",
])
C += omit('C','C8.Q4','Omission',OI,[
"As soon as the bell rang, the students [left] the class.",
"The earth [moves] round the sun.",
"He prevented me [from] going out.",
"If you work hard, you [will] pass.",
])
C += reorder('C','C8.Q5','Reordering',SI,[
"Not only / did he / win, but / he also broke the record.",
"The book / that I / borrowed / is very interesting.",
"They / are being / taken / to the museum.",
"By next month / I shall / have completed / the course.",
])
