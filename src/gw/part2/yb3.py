from yhelp import items
B=[]
SC="Complete each sentence using the cue in brackets. The answer shows one correct completion; any grammatically correct and meaningful one is accepted."
S=[
("Tenses",[("She ______ (read) when the phone rang.","was reading"),("By the time we arrived, the match ______ (start).","had started"),("My uncle ______ (live) in Pune since 2012.","has been living / has lived"),("The sun ______ (set) in the west.","sets"),("This time next week, we ______ (travel) to Goa.","will be travelling")]),
("Modals",[("You ______ (should / must) always speak the truth.","should"),("______ I borrow your pen, please?","May / Can"),("He ______ (ability) swim across the river when he was young.","could"),("Children ______ not play with fire.","must / should"),("They ______ be at home; the lights are on.","must")]),
("Conditionals",[("If you heat ice, ______.","it melts"),("If I had known the answer, ______.","I would have told you"),("Had she studied harder, ______.","she would have passed"),("Unless you leave now, ______.","you will miss the train"),("I wish I ______ (be) a pilot.","were")]),
("Relatives and Connectors",[("The book ______ I borrowed is excellent. (relative)","which / that"),("He is the doctor ______ son is a cricketer.","whose"),("She was tired, ______ she kept working. (contrast)","yet / but"),("Do not move ______ I return.","until"),("______ it was raining, we went out. (concession)","Although / Though")]),
("Non-finites and Gerunds",[("______ (swim) is a good exercise.","Swimming"),("He wants ______ (become) a pilot.","to become"),("I am tired of ______ (wait).","waiting"),("She was seen ______ (enter) the room.","entering"),("The ______ (injure) player was carried out.","injured")]),
("Passive and Reported",[("The window ______ (break) by the boys yesterday.","was broken"),("The letters ______ (post) tomorrow.","will be posted"),("He told me that he ______ (be) busy.","was"),("She asked me where I ______ (live).","lived"),("The teacher said that the sun ______ (rise) in the east.","rises")]),
("Comparison and Articles",[("He is ______ (tall) boy in the class.","the tallest"),("This book is ______ (interesting) than that one.","more interesting"),("She is ______ honest girl. (a / an)","an"),("Delhi is ______ capital of India.","the"),("Of the two shirts, this is the ______ (cheap).","cheaper")]),
("Prepositions",[("She is afraid ______ spiders.","of"),("He was born ______ 12 March.","on"),("The cat jumped ______ the wall.","over / onto"),("We have been waiting ______ two hours.","for"),("He is good ______ drawing.","at")]),
("Subject-Verb Agreement",[("Each of the players ______ (get) a medal.","gets"),("The children ______ (be) playing in the garden.","are"),("Neither Raj nor his friends ______ (be) ready.","were / are"),("Slow and steady ______ (win) the race.","wins"),("Ten kilometres ______ (be) a long distance.","is")]),
("Nominalisation and Avoiding Repetition",[("He was angry. His ______ (angry) frightened us. Use the noun form.","anger"),("She is honest; we admire her ______.","honesty"),("My pen is better than ______ of my brother. (avoid repetition)","that"),("Ravi works hard and so ______ his sister. (avoid repetition)","does"),("I like this shirt but not that ______. (avoid repetition)","one")]),
("Mixed Revision",[("Despite ______ (be) ill, he attended school.","being"),("It is high time we ______ (leave).","left"),("She would rather ______ (stay) at home.","stay"),("No sooner ______ he reached than it rained.","had"),("Not only ______ he sing, but he also dances.","does")]),
]
S=[x for x in S if x[0] not in ('Tenses','Comparison and Articles','Subject-Verb Agreement')]
for i,(t,p) in enumerate(S,1):
    B += items('B',f'B10.{i}',f'Sentence Completion — {t}',SC,p)
