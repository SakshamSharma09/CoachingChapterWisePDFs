from xlib import G,T,L
C=[]
# Test 1 (Classes 5-6) 20 marks
C.append(L("C1-A","Test 1, Section A — Fill in the blanks (5 marks)","Fill in the blank with the correct form of the verb in brackets.",[
("My sister ______ (play) the piano every evening.","plays"),
("The children ______ (watch) a film now.","are watching"),
("We ______ (visit) Jaipur last year.","visited"),
("She has ______ (write) a long letter.","written"),
("It ______ (rain) when we left home.","was raining")]))
C.append(G("C1-B","Test 1, Section B — Choose the correct option (5 marks)","Read each sentence and choose the correct option for the blank.",
[("on|in|at|by",1),("an|a|the|X",1),("is|are|were|be",2),("him|he|his|himself",1),("taller|tallest|more tall|tall",1)],ins="Choose the correct option.") )
C[-1]['body']="1. The book is ______ the table.<br>2. She is ______ honest girl.<br>3. The boys ______ playing in the park.<br>4. Give ______ the pen.<br>5. Ravi is ______ than Mohan."
C.append(L("C1-C","Test 1, Section C — Spot the error (5 marks)","Each sentence has one error. Write the correct form of the wrong word.",[
("He don't like tea.","don't → doesn't"),("There is five pens on the desk.","is → are"),("She sings very sweet.","sweet → sweetly"),("My mother cook food daily.","cook → cooks"),("They did not went home.","went → go")]))
C.append(L("C1-D","Test 1, Section D — Rewrite as directed (5 marks)","Rewrite as directed.",[
("Ravi writes a letter. (Passive)","A letter is written by Ravi."),
("He said, \"I am tired.\" (Reported speech)","He said that he was tired."),
("She is a good singer. (Make interrogative)","Is she a good singer?"),
("Gold is costlier than silver. (Positive)","Silver is not as costly as gold."),
("Join using 'who': I know a girl. She plays chess.","I know a girl who plays chess.")]))
# Test 2 (Classes 7-8)
C.append(L("C2-A","Test 2, Section A — Tenses (5 marks)","Fill in the blank with the correct tense form of the verb in brackets.",[
("By the time we arrived, the match ______ (begin).","had begun"),
("She ______ (live) in Kota since 2015.","has lived (also: has been living)"),
("This time tomorrow, I ______ (travel) to Delhi.","shall/will be travelling"),
("If he ______ (work) hard, he will succeed.","works"),
("He ______ (not/see) the film yet.","has not seen")]))
C.append(G("C2-B","Test 2, Section B — Choose the correct option (5 marks)","Choose the correct option for the numbered blank.",
[("is|are|were|have",1),("whom|who|whose|which",3),("to meet|meeting|meet|met",2),("have to|used to|ought|need",2),("for|since|from|by",2)],ins="Choose the correct option for the numbered blank.") )
C[-1]['body']="1. Neither of the boys ______ present.<br>2. The girl ______ bag was lost cried.<br>3. I look forward to ______ you.<br>4. My grandfather ______ walk every morning (past habit).<br>5. He has been ill ______ Monday."
C.append(L("C2-C","Test 2, Section C — Editing (5 marks)","Each line has one error. Write the incorrect word and the correction.",[
("The news are very surprising.","are → is"),
("He is more taller than his brother.","more taller → taller"),
("She suggested me to rest.","suggested me to rest → advised/told me to rest (or suggested that I rest)"),
("Unless you do not hurry, you will be late.","do not hurry → hurry"),
("He asked me where was the station.","where was the station → where the station was")]))
C.append(L("C2-D","Test 2, Section D — Transformation (5 marks)","Rewrite as directed.",[
("The thief was caught by the police. (Active)","The police caught the thief."),
("She said, \"I will help you.\" (Reported speech)","She said that she would help me/him/her."),
("He is too weak to walk. (so … that)","He is so weak that he cannot walk."),
("Because it rained, we stayed in. (Compound, using 'so')","It rained, so we stayed in."),
("The man is my uncle. You met him. (Join with a relative pronoun)","The man whom you met is my uncle.")]))
