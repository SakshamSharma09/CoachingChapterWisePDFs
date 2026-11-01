"""Reading sets 2–5 (original passages)."""
from eng_lib import P, S

def m(q, o): return S(q, "a", 1, o)
def tbl(head, rows):
    return "<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
T1 = "Read the following passage carefully and answer the questions that follow."
T2 = "Read the following case and answer the questions that follow."
SETS = {}

# ───────────── SET 2 : sleep ─────────────
SETS[2] = dict(
P1=P("""<p>Ask a group of students what they would like to have more of and a large number will say, without a moment's hesitation, 'sleep'. It is odd, then, that the thing we all crave is the first thing we sacrifice when examinations come near. We stay awake with books and tea, believing that every extra hour of study is a gift to our future. Doctors and teachers who have watched this habit for years tell a different story.</p>
<p>During sleep the brain is not idle. It sorts the day's experiences, throws out what is useless and stores what is useful. A lesson revised at ten at night and then slept upon is often remembered better than a lesson read at three in the morning. A tired brain also makes careless mistakes: a student who has not slept may know the formula perfectly and still copy a number wrongly. In this way, the hours saved by staying awake are quietly taken back in the examination hall.</p>
<p>Sleep also guards our mood. A child who sleeps less than seven or eight hours is more likely to be irritable, to quarrel with friends and to lose interest in things that were once enjoyable. Parents often scold such children for 'attitude' when what they need is a longer night.</p>
<p>Good sleep needs a little discipline. The room should be dark and cool, and bright screens should be put away at least half an hour before bedtime. Heavy meals and strong tea late in the evening make rest difficult. Above all, there should be a fixed hour for going to bed, even on holidays. A body that knows when to expect sleep is generous in giving it.</p>""",
[m("Why does the writer find it odd that students lose sleep before examinations?", ["They give up what they most want to have", "They never feel sleepy", "They dislike study", "They fall ill"]),
 m("During sleep the brain:", ["sorts and stores the day's experiences", "stops working", "forgets everything", "repeats lessons aloud"]),
 m("A student who has not slept may:", ["copy a number wrongly though he knows the formula", "score full marks", "finish early", "remember better"]),
 m("Children who sleep less than seven or eight hours are likely to be:", ["irritable", "cheerful", "athletic", "silent"]),
 m("Which of the following is NOT advised for good sleep?", ["Drinking strong tea in the evening", "A dark, cool room", "A fixed bedtime", "Putting screens away early"]),
 S("What do students sacrifice first as examinations come near?", "Their sleep.", 1),
 S("How is a lesson revised at ten at night better than one at three in the morning?", "It is slept upon, so the brain stores it and it is remembered better.", 1),
 S("Why do parents wrongly scold sleepy children?", "They think it is bad 'attitude' when the child really needs more sleep.", 1),
 S("Find a word in the passage which means 'to want very strongly'.", "Crave.", 1),
 S("Find a word in the passage which is the opposite of 'careful'.", "Careless.", 1)], title=T1),
P2=P("""<p>A health club surveyed 100 students of Class 10 about the number of hours they slept on a school night, and noted the average marks of each group in the pre-board test.</p>""" +
tbl(["Hours of sleep", "Number of students", "Average marks (out of 80)"], [["Less than 5", "12", "46"], ["5 to 6", "28", "52"], ["7 to 8", "45", "63"], ["More than 8", "15", "60"]]),
[m("How many students slept for 7 to 8 hours?", ["45", "28", "15", "12"]),
 m("Which group scored the highest average marks?", ["7 to 8 hours", "Less than 5 hours", "5 to 6 hours", "More than 8 hours"]),
 m("How many students slept for 6 hours or less (including the 5–6 group and below)?", ["40", "28", "12", "55"]),
 S("What was the average score of students who slept less than 5 hours?", "46 marks.", 1),
 S("How much higher is the best average than the lowest average?", "63 − 46 = 17 marks.", 1),
 S("What percentage of the students slept for 7 to 8 hours?", "45%.", 1),
 S("Do the figures prove that more sleep always gives higher marks? Give a reason.", "No; the group sleeping more than 8 hours scored slightly less (60) than the 7–8 hour group (63).", 1),
 S("Suggest one conclusion from the table.", "Moderate sleep of 7 to 8 hours is linked with better performance.", 1),
 S("Name the group that scored lower than 50.", "Students who slept less than 5 hours.", 1),
 S("Find a word in the passage which means 'a study of a group'.", "Survey.", 1)], title=T2),
)

# ───────────── SET 3 : water ─────────────
SETS[3] = dict(
P1=P("""<p>In many Indian villages, the arrival of the monsoon is still greeted like the arrival of a guest of honour. The first drops are welcomed, the soil is smelt, and everyone watches the sky. Yet when the guest departs, very little is kept for later. Most of the rain flows away through drains and rivers to the sea, and by April the same people are standing in queues with empty pots.</p>
<p>Rainwater harvesting is an old answer to this problem. In the deserts of Rajasthan, families built tanks known as tankas under their courtyards and carefully directed the water from their roofs into them. A well-kept tanka could keep a family supplied for months, and no one called it a 'scheme'; it was simply what sensible people did. Over the years, as pipes and pumps arrived, these tanks were forgotten. Taps gave water without effort, and effort was soon forgotten too.</p>
<p>Today the taps are failing. The level of groundwater has fallen in many places because we draw more than the earth can give back. Wells have gone dry and deeper borewells have to be dug at greater cost. Experts say that the solution is not a single grand project but thousands of small ones: a pit near a house, a pond in a village, a cleaned-up lake in a town.</p>
<p>Young people can lead the change. A school roof that is connected to a storage tank can supply the garden for the whole year. A family can mend leaking taps, which waste several litres a day, and water plants with the water used for washing vegetables. These are small acts, but when a whole neighbourhood repeats them, a river of saving begins to flow.</p>""",
[m("The writer compares the monsoon to:", ["a guest of honour", "an enemy", "a teacher", "a festival"]),
 m("What is a tanka?", ["A tank built under a courtyard to store rainwater", "A kind of pump", "A river", "A borewell"]),
 m("Why were the old storage tanks forgotten?", ["Taps gave water without effort", "They were unsafe", "They were costly", "They were banned"]),
 m("The fall in groundwater level is caused because we:", ["draw more than the earth can give back", "get too much rain", "build tanks", "plant trees"]),
 m("Experts say that the solution is:", ["thousands of small projects", "one grand project", "importing water", "closing wells"]),
 S("What happens to most rainwater in India according to the passage?", "It flows away through drains and rivers into the sea.", 1),
 S("Why was a tanka important to a Rajasthan family?", "It kept the family supplied with water for months.", 1),
 S("Mention one way a family can save water.", "By mending leaking taps or reusing water used for washing vegetables.", 1),
 S("Find a word in the passage which means 'to send in a particular direction'.", "Directed.", 1),
 S("Find a word in the passage which means 'the opposite of arrive'.", "Depart(s)/departs.", 1)], title=T1),
P2=P("""<p>The Green Committee of a town measured the monthly rainfall and the quantity of rainwater stored by a school with a harvesting tank in the monsoon months.</p>""" +
tbl(["Month", "Rainfall (mm)", "Water stored (thousand litres)"], [["June", "120", "30"], ["July", "320", "80"], ["August", "280", "70"], ["September", "180", "45"]]),
[m("In which month was the rainfall highest?", ["July", "June", "August", "September"]),
 m("How much water was stored in August?", ["70 thousand litres", "80 thousand litres", "45 thousand litres", "30 thousand litres"]),
 m("The total water stored in the four months was:", ["225 thousand litres", "180 thousand litres", "250 thousand litres", "200 thousand litres"]),
 S("How much more rain fell in July than in June?", "320 − 120 = 200 mm.", 1),
 S("How much water is stored for every 4 mm of rain?", "1 thousand litres (1,000 litres) per 4 mm.", 1),
 S("Which month gave the least stored water?", "June (30 thousand litres).", 1),
 S("Why would the tank be useful in the dry months?", "It can supply water for the garden and cleaning when there is no rain.", 1),
 S("What is the total rainfall in the four months?", "120 + 320 + 280 + 180 = 900 mm.", 1),
 S("Suggest one use of the stored water in school.", "Watering plants, cleaning toilets or washing floors.", 1),
 S("Find a word in the passage which means 'collecting and keeping'.", "Harvesting / stored.", 1)], title=T2),
)

# ───────────── SET 4 : failure ─────────────
SETS[4] = dict(
P1=P("""<p>When a little child learns to walk, nobody scolds her for falling. We clap when she stands, laugh when she sits down hard and lift her again. Somewhere between the age of three and the age of thirteen, we change the rules. A fall becomes a disgrace, and the child learns that the safest way never to fail is never to try anything new.</p>
<p>This is a pity, because almost every important discovery has a pile of failures behind it. A scientist who tries a hundred experiments and finds ninety-nine of them wrong has not wasted ninety-nine days; she has found ninety-nine ways that do not work, and is now much closer to the one that does. A cricketer who is out for a duck in the first over learns something about the pitch that a hundred runs would never have taught him.</p>
<p>The fear of failure is also catching. Pupils who are frightened of making mistakes stop asking questions, and a class that does not ask questions slowly stops thinking. Teachers sometimes make this worse by praising only the highest marks. A better habit is to ask the child, after every test, 'What did you learn from the questions you got wrong?'</p>
<p>None of this means that failure is pleasant. It hurts, and it is right that it should. But the hurt is useful, like the pain that tells us to take our hand away from a flame. A person who has failed and tried again has something that no examination can award: the knowledge that she can get up.</p>""",
[m("Why does the writer begin with the example of a child learning to walk?", ["To show that we accept falling then but not later", "To praise parents", "To criticise children", "To describe a game"]),
 m("As children grow older, a fall becomes:", ["a disgrace", "a game", "a reward", "a duty"]),
 m("According to the writer, the scientist with ninety-nine failed experiments has:", ["found ninety-nine ways that do not work", "wasted her time", "proved herself wrong", "given up"]),
 m("Pupils who fear mistakes:", ["stop asking questions", "ask more questions", "score higher", "teach others"]),
 m("The hurt of failure is compared to:", ["pain that makes us pull our hand from a flame", "a gift", "a holiday", "a loud noise"]),
 S("What question does the writer suggest teachers should ask after a test?", "'What did you learn from the questions you got wrong?'", 1),
 S("What does a cricketer learn from being out for a duck?", "Something about the pitch.", 1),
 S("What does a person who has failed and tried again gain?", "The knowledge that she can get up again.", 1),
 S("Find a word in the passage which means 'something to be ashamed of'.", "Disgrace.", 1),
 S("Find a word in the passage which means 'spreading from one person to another'.", "Catching.", 1)], title=T1),
P2=P("""<p>The school notice board carried the following poster.</p>
<p style="text-align:center"><b>ST. MARY'S PUBLIC SCHOOL — 'TRY AGAIN' WEEK</b><br>
Venue: Auditorium &nbsp;|&nbsp; Date: 14–18 November 2026 &nbsp;|&nbsp; Time: 11:00 a.m. – 1:00 p.m.<br>
Day 1: Talk by an Olympic athlete &nbsp;|&nbsp; Day 2: Science of mistakes (workshop) &nbsp;|&nbsp; Day 3: 'My biggest failure' – student stories<br>
Day 4: Fun quiz – wrong answers also win marks! &nbsp;|&nbsp; Day 5: Certificates and refreshments<br>
Entry free for students of Classes 8–12. Register with your class teacher by 10 November.</p>""",
[m("What is the venue of the programme?", ["Auditorium", "Playground", "Library", "Classroom"]),
 m("On which day will students tell their own stories?", ["Day 3", "Day 1", "Day 4", "Day 5"]),
 m("Who can attend the programme?", ["Students of Classes 8–12", "Only Class 10", "Teachers only", "Parents only"]),
 S("What is the last date for registration?", "10 November.", 1),
 S("For how many hours does the programme run each day?", "Two hours (11:00 a.m. to 1:00 p.m.).", 1),
 S("Who will speak on the first day?", "An Olympic athlete.", 1),
 S("What is special about the quiz on Day 4?", "Wrong answers also win marks.", 1),
 S("Why do you think the school chose this theme?", "To teach students that failure is part of learning and not a disgrace.", 1),
 S("Is there any fee for attending?", "No; entry is free.", 1),
 S("Find a word in the poster which means 'a place where an event is held'.", "Venue.", 1)], title="Read the following poster and answer the questions that follow."),
)

# ───────────── SET 5 : space ─────────────
SETS[5] = dict(
P1=P("""<p>When a rocket leaves the ground, thousands of people stand on rooftops to watch it, and thousands more complain about what it costs. 'Why spend crores on the sky,' they ask, 'when so much is needed on the earth?' It is a fair question and deserves a fair answer.</p>
<p>The first answer is that space research has already come down to earth. Weather satellites warn fishermen of cyclones and give farmers an idea of when the rains will arrive. Communication satellites carry our telephone calls and television programmes, and navigation systems help ambulances find the shortest road. Many of the materials used in modern kitchens, hospitals and sports shoes were first developed because a space mission needed something light and strong.</p>
<p>The second answer is less visible but more important. A country that builds rockets must train engineers, chemists and mathematicians of the highest quality. These people do not remain in space centres for ever; they move to industries, universities and start-ups, and carry their skill with them. A single successful mission can inspire a whole generation of children to look up and ask, 'How?'</p>
<p>Still, the critics are partly right. A nation must also build schools, hospitals and roads, and no scientist would deny it. The wise path is not to choose between earth and sky, but to see that the one supports the other. The wealth of knowledge that comes from space should return, again and again, to the people who paid for it.</p>""",
[m("People complain about rocket launches because of:", ["their cost", "their noise", "their danger", "their delay"]),
 m("Weather satellites help farmers by:", ["giving an idea of when the rains will arrive", "irrigating the fields", "supplying seeds", "storing grain"]),
 m("Materials developed for space missions are now used in:", ["kitchens, hospitals and sports shoes", "only rockets", "only schools", "only roads"]),
 m("The 'second answer' stresses the value of:", ["trained people and inspiration", "profits", "tourism", "weapons"]),
 m("The writer's final view is that:", ["earth and sky should support each other", "space research should stop", "schools are unimportant", "only rockets matter"]),
 S("Name two services provided by satellites.", "Weather warning and communication (or navigation).", 1),
 S("How do ambulances benefit from space technology?", "Navigation systems help them find the shortest road.", 1),
 S("What does a successful mission do to children?", "It inspires them to ask 'How?'", 1),
 S("Find a word in the passage which means 'people who disagree or find fault'.", "Critics.", 1),
 S("Find a word in the passage which means 'not easily seen'.", "Invisible / less visible.", 1)], title=T1),
P2=P("""<p>The Space Club of a school displayed the following data about launches by four countries in a year.</p>""" +
tbl(["Country", "Launches", "Successful"], [["A", "20", "18"], ["B", "10", "9"], ["C", "8", "8"], ["D", "12", "9"]]),
[m("Which country had the highest number of launches?", ["A", "B", "C", "D"]),
 m("Which country had a 100% success record?", ["C", "A", "B", "D"]),
 m("How many launches failed in country D?", ["3", "2", "1", "0"]),
 S("What is the total number of launches by the four countries?", "20 + 10 + 8 + 12 = 50.", 1),
 S("What is the total number of successful launches?", "18 + 9 + 8 + 9 = 44.", 1),
 S("What percentage of launches by country A were successful?", "90%.", 1),
 S("Which country had the lowest success rate?", "D (9 out of 12, i.e. 75%).", 1),
 S("How many launches in all did not succeed?", "50 − 44 = 6.", 1),
 S("What conclusion can the club draw about space missions?", "Most missions succeed, but some risk of failure always remains.", 1),
 S("Find a word in the passage which means 'a flight into space'.", "Launch(es).", 1)], title=T2),
)
