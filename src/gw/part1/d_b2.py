from xlib import G,T,L
B=[]
def R(sid,title,rows,ins="Rearrange the words/phrases to form a meaningful sentence."):
    return T(sid,title,ins,rows,head="Words and phrases")
B.append(R("B4.1","Sentence Reordering — Set 1 (Classes 5–6)",[
("to school / every day / walks / Meena","Meena walks to school every day."),
("is / my favourite / mathematics / subject","Mathematics is my favourite subject."),
("in the sky / are flying / the birds / high","The birds are flying high in the sky."),
("were playing / when it started / the children / to rain","The children were playing when it started to rain.")]))
B.append(R("B4.2","Sentence Reordering — Set 2 (Classes 5–6)",[
("is the / in the world / tallest mountain / Mount Everest","Mount Everest is the tallest mountain in the world."),
("grows / on the banks / of rivers / rice / well","Rice grows well on the banks of rivers."),
("by farmers / is harvested / in October / the crop","The crop is harvested by farmers in October."),
("wheat / a lot of / India / produces","India produces a lot of wheat.")]))
B.append(R("B4.3","Sentence Reordering — Honey Bees (Class 7)",[
("live / in colonies / honey bees / thousands of","Thousands of honey bees live in colonies."),
("collects / nectar / from flowers / every worker bee","Every worker bee collects nectar from flowers."),
("is stored / in the hive / the nectar / as honey","The nectar is stored as honey in the hive."),
("lays / all the eggs / the queen / in the colony","The queen lays all the eggs in the colony.")]))
B.append(R("B4.4","Sentence Reordering — Food Waste (Class 8)",[
("large amounts of food / every year / are wasted","Large amounts of food are wasted every year."),
("this food / could feed / millions of hungry people","This food could feed millions of hungry people."),
("should not / we / take more food / than we can eat","We should not take more food than we can eat."),
("the leftovers / can be given / to the needy / at the end of the party","The leftovers can be given to the needy at the end of the party.")]))
B.append(R("B4.5","Sentence Reordering — Questions (Classes 6–8)",[
("you / do / what / want to be","What do you want to be?"),
("have / you / finished / your homework / yet","Have you finished your homework yet?"),
("was / the film / how","How was the film?"),
("is / where / the nearest / post office","Where is the nearest post office?")]))
# ---- dialogue completion (G helper builds options)
B.append(G("B5.1","Dialogue Completion — At a Shop (Classes 6–8)",
"Customer: Good morning. (a) ______<br>Shopkeeper: Yes, madam. We have all sizes.<br>Customer: (b) ______<br>Shopkeeper: It costs five hundred rupees.<br>Customer: That is too costly. (c) ______<br>Shopkeeper: I can give you a ten per cent discount.<br>Customer: (d) ______, I will take it.",
[("Do you have school bags?|You have school bags?|Are you having school bag?|Have you school bag be?",1),("How much it costs?|How much does it cost?|How it costs much?|What much it costs?",2),("Can you reduce the price a little?|Can you reducing the price?|Could you reduced price?|You reduce the price?",1),("In that case|In that cases|On that case|At that case",1)],
ins="Complete the conversation by choosing the correct option."))
B.append(G("B5.2","Dialogue Completion — At the Doctor's (Classes 7–8)",
"Doctor: What is the problem?<br>Patient: (a) ______ since morning.<br>Doctor: (b) ______ any medicine?<br>Patient: No, I haven't.<br>Doctor: You (c) ______ more water and rest well.<br>Patient: (d) ______ come again, doctor?<br>Doctor: Yes, come after three days.",
[("I am having a headache|I have had a headache|I had a headache|I will have a headache",2),("Do you take|Have you taken|Are you taken|Did you took",2),("should drink|should drinks|should drank|should to drink",1),("Shall I|Do I shall|Am I shall|Will I shall",1)],
ins="Complete the conversation by choosing the correct option."))
B.append(G("B5.3","Dialogue Completion — A Phone Call (Class 8)",
"Ravi: Hello! May I speak to Mr Sharma?<br>Voice: (a) ______<br>Ravi: This is Ravi from Mastermind Classes. (b) ______<br>Voice: Mr Sharma (c) ______ at the moment. Can I take a message?<br>Ravi: (d) ______ Please tell him that the test has been postponed.",
[("Who is speaking, please?|Who are you speaking?|Whom are you?|Who you are speaking?",1),("I am calling to inform about the test.|I am calling to inform you about the test.|I call for inform you about test.|I called to inform you the test about.",2),("is not available|not available|does not available|has not available",1),("Yes, please.|Yes, I please.|Yes, pleased.|Please, yes I.",1)],
ins="Complete the conversation by choosing the correct option."))
B.append(G("B5.4","Dialogue Completion — A Picnic Plan (Classes 5–6)",
"Rita: Are you free (a) ______ Sunday?<br>Gita: Yes, I am. (b) ______<br>Rita: Let us (c) ______ a picnic.<br>Gita: That is a (d) ______ idea!",
[("in|on|at|by",2),("What we shall do?|What shall we do?|What we do shall?|Shall what we do?",2),("plan|plans|planned|to plan",1),("well|good|goodly|best",2)],
ins="Complete the conversation by choosing the correct option."))
# ---- reported speech paragraph completion
def RS(sid,title,conv,para,ans):
    return T(sid,title,"Read the conversation. Then complete the report by filling in each blank.",[(f"Blank ({chr(97+i)})",a) for i,a in enumerate(ans)],body=conv+"<br><br><b>Report:</b> "+para,head="Blank")
B.append(RS("B6.1","Reported Speech Paragraph — Going to the Market (Classes 5–6)",
"Rama: I am going to the market.<br>Sita: Why are you going there?<br>Rama: I need to buy vegetables.<br>Sita: Can I come with you?",
"Rama told Sita (a) ______. She asked him (b) ______. He replied that (c) ______. Sita asked (d) ______.",
["that he was going to the market","why he was going there","he needed to buy vegetables","if/whether she could go with him"]))
B.append(RS("B6.2","Reported Speech Paragraph — The Homework (Classes 6–7)",
"Teacher: Where is your homework?<br>Student: I forgot it at home, sir.<br>Teacher: Bring it tomorrow.<br>Student: I will, sir.",
"The teacher asked the student (a) ______. The student replied respectfully that (b) ______. The teacher told him (c) ______. The student promised that (d) ______.",
["where his homework was","he had forgotten it at home","to bring it the next day","he would"]))
B.append(RS("B6.3","Reported Speech Paragraph — After Dinner (Class 7)",
"Mother: Have you finished your homework?<br>Son: Not yet. I'll finish it after dinner.<br>Mother: Don't watch TV until you finish.<br>Son: I won't, Mother.",
"Mother asked her son (a) ______. He answered that he had not finished it yet and that (b) ______. Mother told him (c) ______ until he finished. The son replied that (d) ______.",
["if/whether he had finished his homework","he would finish it after dinner","not to watch TV","he would not"]))
B.append(RS("B6.4","Reported Speech Paragraph — The Shirt (Class 8)",
"Customer: How much does this shirt cost?<br>Shopkeeper: It costs four hundred rupees.<br>Customer: That is too expensive. Will you give a discount?<br>Shopkeeper: I can give you ten per cent off.",
"The customer asked the shopkeeper (a) ______. The shopkeeper replied that (b) ______. The customer said that (c) ______ and asked (d) ______. The shopkeeper said that he could give ten per cent off.",
["how much that shirt cost","it cost four hundred rupees","that was too expensive","if/whether he would give a discount"]))
B.append(RS("B6.5","Reported Speech Paragraph — The Coach (Class 8)",
"Coach: Run faster.<br>Player: I am very tired, sir.<br>Coach: Don't give up. You are almost there.",
"The coach (a) ______. The player said that (b) ______. The coach (c) ______ and said that (d) ______.",
["told/ordered the player to run faster","he was very tired","advised him not to give up","he was almost there"]))
# ---- headlines
def H(sid,title,rows):
    return T(sid,title,"Use the information in the headline to complete the news item with the correct form of the verb.",rows,head="Headline and news item")
B.append(H("B7.1","Newspaper Headlines — Set 1 (Classes 6–7)",[
("<b>PM TO INAUGURATE NEW AIRPORT TOMORROW</b> — The Prime Minister ______ a new airport tomorrow.","will inaugurate"),
("<b>FLOODS DESTROY CROPS IN BIHAR</b> — Heavy floods ______ crops over thousands of acres, officials said on Monday.","have destroyed (also: destroyed)"),
("<b>THREE ARRESTED FOR THEFT</b> — Three men ______ for stealing mobile phones from a shop.","have been arrested (also: were arrested)"),
("<b>SCHOOLS TO REMAIN CLOSED TILL MONDAY</b> — All schools in the city ______ closed till Monday due to heavy rain.","will remain")]))
B.append(H("B7.2","Newspaper Headlines — Set 2 (Classes 6–7)",[
("<b>INDIA WINS SERIES 3–1</b> — India ______ the five-match series by 3–1 on Sunday.","won (also: have won)"),
("<b>STUDENT FOUND SAFE AFTER TWO DAYS</b> — A missing student ______ safe after two days.","was found (also: has been found)"),
("<b>NEW LIBRARY TO OPEN IN JAIPUR</b> — A new library ______ in Jaipur next month.","will open (also: will be opened)"),
("<b>TEACHERS PRAISED FOR BRAVERY</b> — Two teachers ______ for their bravery in saving children from a fire.","were praised (also: have been praised)")]))
B.append(H("B7.3","Newspaper Headlines — Set 3 (Class 8)",[
("<b>FIRE DESTROYS GODOWN</b> — A fire ______ a godown in the old market last night.","destroyed"),
("<b>TRAFFIC HIT BY RAIN</b> — Traffic ______ badly by heavy rain on Tuesday.","was hit (also: was affected)"),
("<b>GOVT TO PROVIDE FREE BOOKS</b> — The government ______ free books to all students next year.","will provide"),
("<b>FARMERS DEMAND HIGHER PRICES</b> — Farmers ______ higher prices for their crops.","demand (also: are demanding / have demanded)")]))
B.append(H("B7.4","Newspaper Headlines — Set 4 (Classes 5–6)",[
("<b>BOY SAVES DOG FROM WELL</b> — A brave boy ______ a dog from a well.","saved"),
("<b>SCHOOL ANNUAL DAY ON 5 MARCH</b> — The school's annual day ______ on 5 March.","will be held"),
("<b>CHILDREN PLANT 100 TREES</b> — Children of Class 6 ______ 100 trees on Sunday.","planted"),
("<b>CAT RESCUED FROM TREE</b> — A cat ______ from a tall tree by firemen.","was rescued")]))
# ---- procedure
def P(sid,title,steps,para,ans):
    body="<b>Instructions:</b><br>"+"<br>".join(f"{i+1}. {s}" for i,s in enumerate(steps))+"<br><br><b>Report:</b> "+para
    return T(sid,title,"Read the instructions and complete the passage using the passive voice.",[(f"Blank ({chr(97+i)})",a) for i,a in enumerate(ans)],body=body,head="Blank")
B.append(P("B8.1","Procedure — Making Tea (Classes 5–6)",["Boil water in a pan.","Add tea leaves.","Add milk and sugar.","Strain and serve hot."],
"First, water (a) ______ in a pan. Then tea leaves (b) ______. Milk and sugar (c) ______ next. Finally, the tea (d) ______ and served hot.",
["is boiled","are added","are added","is strained"]))
B.append(P("B8.2","Procedure — Planting a Sapling (Classes 6–7)",["Dig a pit.","Put the sapling in it.","Fill the pit with soil.","Water the sapling daily."],
"First, a pit (a) ______. The sapling (b) ______ in it. The pit (c) ______ with soil. The sapling (d) ______ daily.",
["is dug","is put (also: is placed)","is filled","is watered"]))
B.append(P("B8.3","Procedure — An Experiment (Class 7; past tense)",["Rohan took a glass of water.","He added salt.","He stirred the water.","He noted the change."],
"A glass of water (a) ______ by Rohan. Salt (b) ______ to it. The water (c) ______. The change (d) ______.",
["was taken","was added","was stirred","was noted"]))
B.append(P("B8.4","Procedure — Making Lemonade (Class 8)",["Squeeze a lemon into a glass.","Add sugar.","Pour cold water.","Stir well.","Serve with ice."],
"The lemon juice (a) ______ into a glass. Sugar (b) ______. Cold water (c) ______. The drink (d) ______ well and (e) ______ with ice.",
["is squeezed","is added","is poured","is stirred","is served"]))
