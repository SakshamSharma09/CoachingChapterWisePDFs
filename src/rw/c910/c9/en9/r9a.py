"""Class 9 reading skill sets 1-4 (original). Each set: P1 discursive (10 marks), P2 case-based/data (10 marks)."""
from eng9_lib import P, S

def m(q, o):
    return S(q, "a", 1, o)

SETS = {}

SETS[1] = dict(
P1=P("""<p>A good night's sleep is often treated as a luxury, yet it is closer to a basic need. During sleep the body repairs its tissues, the brain sorts what it has learned during the day, and the mind prepares itself for fresh thoughts. A student who sleeps for six hours or less may feel that she has gained extra time, but the truth is that she has borrowed it from tomorrow. Memory weakens, tempers shorten and small tasks begin to feel heavy.</p>
<p>Doctors suggest that teenagers need between eight and ten hours of sleep. The difficulty is that bright screens in the evening trick the brain into believing that it is still daytime. A phone held close to the face at eleven at night can delay sleep by an hour or more. Many young people therefore lie awake with tired eyes and a restless mind.</p>
<p>The remedy is a gentle routine. Going to bed at the same hour each night, switching off screens half an hour before sleeping, and reading a few pages of a printed book are small habits that train the body to relax. Light dinners and a short walk in the evening help as well. None of these steps costs money, yet together they can change how a person feels in the morning.</p>""",
[m("According to the passage, sleep is closer to:", ["a basic need", "a luxury", "a punishment", "a reward"]),
 m("A student who sleeps for six hours or less has actually:", ["borrowed time from tomorrow", "gained extra time", "improved memory", "saved energy"]),
 m("The recommended sleep for teenagers is:", ["eight to ten hours", "four to six hours", "ten to twelve hours", "five hours"]),
 m("Evening screens affect sleep because they:", ["trick the brain into thinking it is daytime", "make the room warm", "produce loud noise", "make people hungry"]),
 m("Which habit is NOT suggested in the passage?", ["Drinking coffee before bed", "Fixed bedtime", "Switching off screens early", "Reading a printed book"]),
 S("Name two things that happen in the body during sleep.", "The body repairs its tissues and the brain sorts what it has learned.", 1),
 S("What can a phone at eleven at night do?", "It can delay sleep by an hour or more.", 1),
 S("What is the 'gentle routine' the writer recommends? Mention one part.", "Going to bed at the same hour or switching off screens half an hour before sleeping.", 1),
 S("Find a word in the passage which means 'unable to rest'.", "Restless.", 1),
 S("Why does the writer say these steps are easy to follow?", "They cost no money.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>NOTICE — Mastermind Public School, Jaipur</b></p><p>The school will hold its <b>Annual Sports Day</b> on <b>Saturday, 5 December 2026</b>. Events will begin at <b>8:00 a.m.</b> at the school ground with a march-past, followed by races, relay events and the tug of war. The chief guest will be the District Sports Officer. Students must wear their house T-shirts and sports shoes. Parents are welcome to watch from the east stand. Names for events should be given to the House captains by <b>25 November</b>. Water and first-aid facilities will be available at the ground. The prize distribution will be at 12:30 p.m.</p>""",
[m("The Annual Sports Day will be held on:", ["5 December 2026", "25 November 2026", "12 December 2026", "8 December 2026"]),
 m("Events begin at:", ["8:00 a.m.", "12:30 p.m.", "10:00 a.m.", "6:00 a.m."]),
 m("The chief guest is the:", ["District Sports Officer", "Principal", "Mayor", "Collector"]),
 m("Students must wear:", ["house T-shirts and sports shoes", "school uniform", "casual clothes", "any colour"]),
 m("Parents may watch from the:", ["east stand", "west stand", "pavilion", "main hall"]),
 S("By which date should names be given?", "25 November.", 1),
 S("To whom are names given?", "House captains.", 1),
 S("Name two events that will be held.", "Race, relay and tug of war (any two).", 1),
 S("What facilities will be available at the ground?", "Water and first aid.", 1),
 S("At what time will the prizes be given?", "12:30 p.m.", 1)],
 title="Read the following notice and answer the questions that follow."),
)

SETS[2] = dict(
P1=P("""<p>Water seems to be everywhere, yet the amount that humans can actually drink is small. About ninety-seven per cent of the Earth's water is in the oceans and is too salty for use. Most of the remainder is frozen at the poles or lies deep underground. A very small portion in rivers, lakes and shallow wells serves the needs of billions of people.</p>
<p>In many Indian cities, taps run for an hour or two each day, and families store water in tanks and buckets. In villages, women and children often walk long distances to fetch a pot or two. When rain fails, wells dry up and farmers lose their crops. These are not distant problems; they touch every home.</p>
<p>Fortunately, ordinary people can help. Fixing a leaking tap can save thousands of litres in a year. Collecting rainwater from rooftops refills wells and keeps groundwater alive. Reusing the water used for washing vegetables to water plants costs nothing. Schools can teach children to switch off a running tap while brushing their teeth. A country that saves its water saves its future.</p>""",
[m("What percentage of the Earth's water is in the oceans?", ["about 97 per cent", "about 50 per cent", "about 10 per cent", "about 30 per cent"]),
 m("Water in the oceans is not useful because it is:", ["too salty", "too cold", "too far", "too deep"]),
 m("In many Indian cities taps run for:", ["an hour or two each day", "all day", "only at night", "once a week"]),
 m("Who often walk long distances to fetch water in villages?", ["Women and children", "Only men", "Old people", "Soldiers"]),
 m("Which of these helps recharge groundwater?", ["Collecting rainwater from rooftops", "Cutting trees", "Building more roads", "Using more tankers"]),
 S("Where is most of the remaining fresh water found?", "Frozen at the poles or deep underground.", 1),
 S("What happens when rain fails?", "Wells dry up and farmers lose crops.", 1),
 S("Give one way to reuse household water.", "Use the water from washing vegetables to water plants.", 1),
 S("Find a word in the passage that means 'a long way off'.", "Distant.", 1),
 S("What is the writer's final message?", "A country that saves water saves its future.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p>A class of 40 students was asked how they reach school each day. The results are given below.</p><table><tr><th>Mode of travel</th><th>Number of students</th></tr><tr><td>Walk</td><td>8</td></tr><tr><td>Bicycle</td><td>10</td></tr><tr><td>School bus</td><td>14</td></tr><tr><td>Car or scooter</td><td>8</td></tr></table>""",
[m("Which mode is used by the most students?", ["School bus", "Walk", "Bicycle", "Car or scooter"]),
 m("How many students walk to school?", ["8", "10", "14", "40"]),
 m("How many students come by bicycle or on foot together?", ["18", "10", "14", "22"]),
 m("How many more students travel by bus than by walking?", ["6", "4", "8", "14"]),
 m("The total number of students surveyed is:", ["40", "32", "42", "50"]),
 S("Which two modes have the same number of students?", "Walk and car or scooter (8 each).", 1),
 S("How many students use a vehicle with an engine (bus, car or scooter)?", "14 + 8 = 22.", 1),
 S("What fraction of the class uses a bicycle?", "10/40 = 1/4.", 1),
 S("Which mode of travel is healthiest and costs nothing?", "Walking.", 1),
 S("Suggest one way to reduce pollution caused by travel to school.", "Use cycles or carpool.", 1)],
 title="Read the following data and answer the questions that follow."),
)

SETS[3] = dict(
P1=P("""<p>Failure is a word that most students dread, yet nearly every successful person has a story that begins with one. A scientist repeats an experiment many times before it works. A cricketer is dropped from a team before returning as a captain. A writer receives rejection letters before one book is published. What separates these people from others is not an absence of failure but the choice to continue.</p>
<p>The trouble is that schools and families often measure a child by marks alone. A low score becomes a label, and a child who is labelled soon begins to believe it. Fear of failure then makes her avoid new subjects, new games and even new questions. She does only what is safe, and safe things rarely lead to growth.</p>
<p>A better approach is to treat a mistake as information. When a student studies a wrong answer, she discovers a gap that can be filled. Teachers can help by praising effort and improvement, not just results. Parents can help by asking, 'What did you learn?' rather than 'Why did you fail?' When the fear of failure shrinks, curiosity grows.</p>""",
[m("According to the passage, what separates successful people from others?", ["The choice to continue after failure", "Absence of failure", "Luck", "Wealth"]),
 m("The word 'dread' in the first line means:", ["fear", "enjoy", "ignore", "praise"]),
 m("A child who is labelled by marks:", ["begins to believe the label", "ignores it", "becomes proud", "forgets it"]),
 m("Which example is given of a failure before success?", ["A cricketer dropped from a team", "A farmer losing land", "A doctor leaving work", "A singer losing a voice"]),
 m("The writer suggests that parents should ask:", ["'What did you learn?'", "'Why did you fail?'", "'Who is first?'", "'How many marks?'"]),
 S("Why do children avoid new things when they fear failure?", "They want to stay safe and avoid mistakes.", 1),
 S("How can a student use a wrong answer?", "She can study it to find a gap in her learning.", 1),
 S("What should teachers praise according to the writer?", "Effort and improvement.", 1),
 S("Find a word in the passage that means 'to reject or turn away from'.", "Avoid.", 1),
 S("What grows when the fear of failure shrinks?", "Curiosity.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>Advertisement — City Craft Fair</b></p><p>The <b>Jaipur Craft Fair</b> invites you to experience the art of India! Dates: <b>10–15 January</b>. Venue: <b>Central Park Exhibition Ground</b>. Timings: <b>11 a.m. to 8 p.m.</b> Entry: ₹20 for adults, free for school students in uniform. Special attractions: live demonstrations of blue pottery, block printing and Rajasthani puppet shows. Handmade products by more than 100 artisans from 12 states. Food court with local cuisines. Parking available near Gate 2.</p>""",
[m("The fair will be held from:", ["10 to 15 January", "1 to 5 January", "10 to 15 December", "20 to 25 January"]),
 m("The venue is:", ["Central Park Exhibition Ground", "City Palace", "Town Hall", "Railway Station"]),
 m("Entry is free for:", ["school students in uniform", "all adults", "senior citizens", "foreigners"]),
 m("The fair is open until:", ["8 p.m.", "5 p.m.", "10 p.m.", "6 p.m."]),
 m("Which of these is a special attraction?", ["Block printing demonstrations", "Cricket match", "Film show", "Car race"]),
 S("What is the entry fee for adults?", "₹20.", 1),
 S("How many artisans take part?", "More than 100.", 1),
 S("From how many states do the artisans come?", "12.", 1),
 S("Where is parking available?", "Near Gate 2.", 1),
 S("Name two crafts mentioned in the advertisement.", "Blue pottery and block printing.", 1)],
 title="Read the following advertisement and answer the questions that follow."),
)

SETS[4] = dict(
P1=P("""<p>A hundred years ago, news travelled slowly. A letter might take a week to cross the country, and a telegram was sent only in an emergency. Today a photograph clicked in a village can reach another continent in a few seconds. Speed has become the pride of our age, but it has also changed how we listen.</p>
<p>When people received a single letter, they read it several times and replied with care. Today a hundred messages arrive in an hour, and most are answered with a quick emoji or not at all. The result is that we know a great deal about many people and very little about any one of them.</p>
<p>Conversation suffers the most. At a family meal, one can often see each member looking at a small screen instead of at one another. Grandparents wait to tell a story, and no one hears. This does not mean that technology is to blame. It means that we have to choose when to put it aside. A fixed 'no-phone' hour at dinner or on Sundays can bring back the lost habit of listening, which is the beginning of friendship.</p>""",
[m("A hundred years ago, a letter might take:", ["a week to cross the country", "a minute", "an hour", "a year"]),
 m("The writer says that today we know:", ["a lot about many people and little about any one", "everything about everybody", "nothing about anybody", "much about one person"]),
 m("According to the passage, conversation suffers because:", ["people look at screens instead of each other", "people speak too loudly", "there are no meals", "families are small"]),
 m("'Pride of our age' refers to:", ["speed", "silence", "letters", "telegrams"]),
 m("The writer's suggestion is to:", ["fix a no-phone hour", "ban phones", "stop sending messages", "use only letters"]),
 S("What was a telegram used for?", "Only in emergencies.", 1),
 S("How did people treat a single letter earlier?", "They read it several times and replied with care.", 1),
 S("Who waits to tell a story but is not heard?", "Grandparents.", 1),
 S("Find a word which means 'put away'.", "Aside (put aside).", 1),
 S("What does the writer call 'the beginning of friendship'?", "Listening.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p>The table shows the daily temperature (in °C) recorded in a town for five days in January.</p><table><tr><th>Day</th><th>Minimum</th><th>Maximum</th></tr><tr><td>Mon</td><td>6</td><td>18</td></tr><tr><td>Tue</td><td>5</td><td>17</td></tr><tr><td>Wed</td><td>4</td><td>15</td></tr><tr><td>Thu</td><td>7</td><td>19</td></tr><tr><td>Fri</td><td>8</td><td>21</td></tr></table>""",
[m("Which day had the lowest minimum temperature?", ["Wednesday", "Monday", "Friday", "Thursday"]),
 m("The highest maximum temperature was on:", ["Friday", "Monday", "Tuesday", "Wednesday"]),
 m("The difference between maximum and minimum on Monday is:", ["12 °C", "10 °C", "24 °C", "6 °C"]),
 m("On which day was the maximum temperature 15 °C?", ["Wednesday", "Tuesday", "Monday", "Friday"]),
 m("On which days was the minimum below 6 °C?", ["Tuesday and Wednesday", "Monday and Friday", "Thursday and Friday", "Monday and Thursday"]),
 S("What was the maximum temperature on Thursday?", "19 °C.", 1),
 S("On which day was the day warmest overall?", "Friday.", 1),
 S("What is the difference between Friday's maximum and Wednesday's maximum?", "21 − 15 = 6 °C.", 1),
 S("Is the weather getting warmer or colder after Wednesday?", "Warmer.", 1),
 S("Suggest what a person should wear on Wednesday morning.", "Warm clothes such as a sweater or jacket.", 1)],
 title="Read the following data and answer the questions that follow."),
)
