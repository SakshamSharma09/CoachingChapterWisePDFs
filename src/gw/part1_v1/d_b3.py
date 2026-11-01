from xlib import G,T,L
B=[]
def TF(sid,title,ins,items): return L(sid,title,ins,items)
B.append(TF("B9.1","Sentence Transformation — Kinds of Sentences (Classes 5–6)","Rewrite as directed.",[
("She is a good singer. (Make interrogative)","Is she a good singer?"),
("They play cricket on Sundays. (Make interrogative)","Do they play cricket on Sundays?"),
("He did his work. (Make negative)","He did not do his work."),
("She has seen the Taj Mahal. (Make interrogative)","Has she seen the Taj Mahal?"),
("It is a very hot day. (Make exclamatory)","What a hot day it is!"),
("The soup is very tasty. (Make exclamatory with 'How')","How tasty the soup is!"),
("You must open the box. (Make negative)","You must not open the box."),
("Open the window. (Make negative imperative)","Do not open the window.")]))
B.append(TF("B9.2","Sentence Transformation — Degrees of Comparison (Classes 6–7)","Change the degree of comparison without changing the meaning.",[
("Mount Everest is the highest peak. (Comparative)","Mount Everest is higher than any other peak."),
("No other student is as clever as Anita. (Superlative)","Anita is the cleverest student."),
("Few cities are as clean as Indore. (Superlative)","Indore is one of the cleanest cities."),
("Gold is more costly than silver. (Positive)","Silver is not as costly as gold."),
("Iron is the most useful of all metals. (Comparative)","Iron is more useful than all other metals."),
("This question is easier than that one. (Positive)","That question is not as easy as this one."),
("My bag is heavier than yours. (Positive)","Your bag is not as heavy as mine."),
("Neha is the best singer in the school. (Comparative)","Neha is a better singer than any other in the school.")]))
B.append(TF("B9.3","Sentence Transformation — too … to / so … that (Class 7)","Rewrite as directed.",[
("He is too tired to walk. (Use 'so … that')","He is so tired that he cannot walk."),
("The tea was too hot to drink. (Use 'so … that')","The tea was so hot that I/we could not drink it."),
("She is so weak that she cannot lift the bag. (Use 'too … to')","She is too weak to lift the bag."),
("The boy is intelligent enough to solve this. (Use 'so … that')","The boy is so intelligent that he can solve this."),
("She spoke so softly that nobody could hear. (Use 'too … to')","She spoke too softly to be heard."),
("The news is too good to be true. (Use 'so … that')","The news is so good that it cannot be true."),
("The bag is not light enough for the child to carry. (Use 'too … to')","The bag is too heavy for the child to carry."),
("He ran so fast that no one could catch him. (Use 'too … to')","He ran too fast to be caught.")]))
B.append(TF("B9.4","Sentence Transformation — Simple, Compound, Complex (Class 8)","Rewrite as directed.",[
("He is poor but honest. (Change to a complex sentence using 'although')","Although he is poor, he is honest."),
("Because he was ill, he stayed at home. (Change to a compound sentence using 'so')","He was ill, so he stayed at home."),
("On seeing the lion, the children ran away. (Change to a complex sentence)","When the children saw the lion, they ran away."),
("Work hard, or you will fail. (Change to a complex sentence using 'if')","If you do not work hard, you will fail."),
("He worked hard to pass the exam. (Change to a complex sentence using 'so that')","He worked hard so that he might/could pass the exam."),
("I know his address. (Change to a complex sentence using 'where')","I know where he lives."),
("Having finished his work, he went home. (Change to a compound sentence)","He finished his work and went home."),
("She is clever and she is hardworking. (Change to a simple sentence using 'both … and')","She is both clever and hardworking.")]))
B.append(TF("B9.5","Sentence Transformation — Joining and Rewriting (Class 8)","Rewrite as directed.",[
("I know a boy. He can speak five languages. (Join using 'who')","I know a boy who can speak five languages."),
("He saw the snake. He ran away. (Join using a participle)","Seeing the snake, he ran away."),
("Hurry up, or you will miss the bus. (Use 'unless')","Unless you hurry up, you will miss the bus."),
("As soon as the bell rang, the students left. (Use 'No sooner')","No sooner did the bell ring than the students left."),
("As soon as he reached, it began to rain. (Use 'Hardly')","Hardly had he reached when it began to rain."),
("He likes to swim. (Use a gerund)","He likes swimming."),
("To tell a lie is wrong. (Begin with 'It')","It is wrong to tell a lie."),
("In spite of his illness, he came. (Use 'although')","Although he was ill, he came.")]))
# sentence completion
B.append(G("B10.1","Sentence Completion — Choose the Best Ending (Classes 6–8)",
"1. If I had a million rupees, ______<br>2. She was late because ______<br>3. Although he was tired, ______<br>4. Unless you work hard, ______<br>5. No sooner had the teacher entered than ______<br>6. The boy who ______ is my cousin.",
[("I would build a school.|I will build a school.|I built a school.|I have built a school.",1),("the bus had broken down.|the bus breaking down.|the bus will break down.|of the bus down.",1),("he finished the work.|so he finished the work.|because he finished the work.|and but he finished.",1),("you will fail.|you won't fail.|you would not fail.|you not fail.",1),("the students stood up.|did the students stand up.|the students standing up.|stood the students.",1),("won the race|winning the race|win the race|has win the race",1)],
ins="Complete each sentence by choosing the correct option for the numbered blank in the order given.") )
B.append(L("B10.2","Sentence Completion — Complete Meaningfully (Classes 7–8)","Complete each sentence in your own words. (Any grammatically correct and meaningful completion earns credit; a sample answer is given.)",[
("If it rains tomorrow, ______","we shall cancel the picnic. (sample)"),
("She was so happy that ______","she danced with joy. (sample)"),
("I will wait here until ______","you return. (sample)"),
("The boy who sits next to me ______","is my best friend. (sample)"),
("He is too young to ______","drive a car. (sample)"),
("Hardly had we left home when ______","it started raining. (sample)")]))
B.append(G("B10.3","Sentence Completion — Choose the Best Ending (Classes 5–6)",
"1. I like mangoes, but ______<br>2. We went to the park and ______<br>3. She asked me ______<br>4. The tiger is a ______ animal.<br>5. He sat down because ______<br>6. I have a friend whose ______",
[("my sister does not like them.|my sister doesn't likes them.|my sister not like them.|my sisters didn't likes them.",1),("played football.|playing football.|play football yesterday.|plays football.",1),("where I was going.|where was I going.|where am I going.|where I am go.",1),("danger|dangerous|dangerously|dangering",2),("he was tired.|he is tire.|tiring.|tired of.",1),("father is a pilot.|father are a pilot.|a father pilot.|pilot father is.",1)],
ins="Complete each sentence by choosing the correct option for the numbered blank in the order given."))
# verb forms in passage
def V(sid,title,body,ans,ins="Fill in each blank with the correct form of the verb given in brackets."):
    return T(sid,title,ins,[(f"Blank ({chr(97+i)})",a) for i,a in enumerate(ans)],body=body,head="Blank")
B.append(V("B11.1","Verb Forms in a Passage — The Picnic (Classes 5–6)",
"Last Sunday, my family (a) ______ (go) for a picnic. My father (b) ______ (drive) the car, and my mother (c) ______ (sit) beside him. We (d) ______ (reach) the river at ten. The children (e) ______ (play) in the sand when it suddenly (f) ______ (begin) to rain. We (g) ______ (run) to the car. By the time we (h) ______ (reach) the car, our clothes (i) ______ (become) wet. It (j) ______ (be) a fun day all the same.",
["went","drove","sat","reached","were playing","began","ran","reached","had become","was"]))
B[-1]['items'][7]=("Blank (h)","reached")
B.append(V("B11.2","Verb Forms in a Passage — Rohit (Class 7)",
"Rohit (a) ______ (live) in Jodhpur since 2018. He (b) ______ (study) in Class 7 at a local school. Every morning he (c) ______ (get) up at six and (d) ______ (go) for a walk. At present he (e) ______ (prepare) for the annual exams. He (f) ______ (already, finish) most of his syllabus. His teacher says that if he (g) ______ (work) hard, he (h) ______ (score) well. By next March, he (i) ______ (complete) all his revision. He (j) ______ (hope) to become a scientist.",
["has lived (also: has been living)","studies","gets","goes","is preparing","has already finished","works","will score","will have completed","hopes"]))
B.append(V("B11.3","Verb Forms in a Passage — The Earthquake (Class 8)",
"When the earthquake (a) ______ (strike), most people (b) ______ (sleep). Many houses (c) ______ (collapse) within seconds. Rescue teams (d) ______ (reach) the area at noon and (e) ______ (begin) work immediately. By evening they (f) ______ (rescue) over two hundred people. Relief camps (g) ______ (set up) and food (h) ______ (distribute). The government says that it (i) ______ (rebuild) the damaged houses next year. Scientists warn that earthquakes (j) ______ (be) unpredictable.",
["struck","were sleeping","collapsed","reached","began","had rescued","were set up","was distributed","will rebuild","are"],
ins="Fill in each blank with the correct tense (and voice, where the verb needs it) of the verb in brackets."))
# preposition / determiner cloze
def C(sid,title,body,ans,ins):
    return T(sid,title,ins,[(f"Blank ({chr(97+i)})",a) for i,a in enumerate(ans)],body=body,head="Blank")
B.append(C("B12.1","Cloze — Prepositions (Classes 5–6)",
"Tara lives (a) ______ a flat (b) ______ the third floor. Every day she goes (c) ______ school (d) ______ bus. She leaves home (e) ______ 7:30 and stays at school (f) ______ two o'clock. She is fond (g) ______ drawing and is good (h) ______ painting.",
["in","on","to","by","at","till/until","of","at"],"Fill in each blank with one suitable word (preposition)."))
B.append(C("B12.2","Cloze — Determiners (Class 7)",
"In the zoo, I saw (a) ______ elephant. (b) ______ elephant is the largest land animal. It has (c) ______ long trunk. (d) ______ trunk is used for drinking, eating and lifting. An elephant eats (e) ______ lot of food every day. There are very (f) ______ elephants left in some forests. (g) ______ the villagers say that elephants never forget. (h) ______ elephant in this park is looked after by the forest department.",
["an","The","a","The","a","few","All","Each/Every"],"Fill in each blank with a suitable determiner (article, quantifier or other)."))
B.append(C("B12.3","Cloze — Prepositions and Connectors (Class 8)",
"He was angry (a) ______ me (b) ______ I had lost his pen. (c) ______ I apologised, he did not speak (d) ______ me. I decided to buy another pen (e) ______ him, but the shop was closed (f) ______ Sunday. I therefore waited (g) ______ Monday morning. He thanked me (h) ______ my kindness.",
["with","because/as/since","Although/Though","to","for","on","until/till","for"],"Fill in each blank with one suitable word."))
# error spotting
def S(sid,title,rows): return T(sid,title,"Each sentence has ONE error. Identify the error and write the correct form.",rows,head="Sentence")
B.append(S("B13.1","Spot the Error — Set 1 (Classes 5–6)",[
("She don't like apples.","don't → doesn't"),("There is many birds on the tree.","is → are"),("I has a new bicycle.","has → have"),("He go to school by bus.","go → goes"),("My mother cooked a delicious foods.","foods → food"),("Ramesh is more taller than Suresh.","more taller → taller"),("She sings very good.","good → well"),("Both the boys is absent.","is → are"),("We are going at the market.","at → to"),("I am agree with you.","am agree → agree")]))
B.append(S("B13.2","Spot the Error — Set 2 (Class 7)",[
("Neither of the girls have finished the work.","have → has"),("He is senior than me.","than → to"),("She said me to take rest.","said → told"),("I have been knowing him for years.","have been knowing → have known"),("He bought a lot of furnitures.","furnitures → furniture"),("If I will see him, I will tell him.","will see → see"),("He can to swim well.","to swim → swim"),("The teacher, along with the students, are coming.","are → is"),("I prefer tea than coffee.","than → to"),("Hardly he had reached when it rained.","he had → had he")]))
B.append(S("B13.3","Spot the Error — Set 3 (Class 8)",[
("The news are shocking.","are → is"),("He insisted to go there.","to go → on going"),("I look forward to meet you.","meet → meeting"),("Unless you do not work hard, you will fail.","do not work → work"),("She is one of the best teacher in the school.","teacher → teachers"),("The man whom I thought was honest cheated me.","whom → who"),("My brother is elder than me.","elder → older"),("He as well as his sons are guilty.","are → is"),("It is high time we start.","start → started"),("He asked me what was my name.","what was my name → what my name was")]))
