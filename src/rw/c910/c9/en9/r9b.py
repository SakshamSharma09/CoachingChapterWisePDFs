"""Class 9 reading skill sets 5-8 (original)."""
from eng9_lib import P, S

def m(q, o):
    return S(q, "a", 1, o)

SETS = {}

SETS[5] = dict(
P1=P("""<p>The humble bicycle is making a quiet comeback. In many cities, people who once travelled by car have begun to ride to work, to the market and to school. The reasons are simple. A bicycle needs no fuel, takes little space and produces no smoke. It also keeps the rider fit, which no car can promise.</p>
<p>City planners are noticing the trend. Some have marked special lanes where cycles can move safely, away from fast traffic. Others have set up stands where a person can hire a cycle for an hour and leave it at another stand. Such schemes have already cut the number of short car trips in a few cities.</p>
<p>Yet cycling is not free of troubles. In crowded roads without lanes, riders fear accidents. Rain and heat make long rides tiring, and thieves target unlocked cycles. If cycling is to grow, authorities must make roads safer and citizens must show consideration to riders. A cycle may be small, but the change it promises is large.</p>""",
[m("The writer's main point is that:", ["cycling is returning and needs support", "cars are cheaper", "cycles are old-fashioned", "cities are shrinking"]),
 m("A bicycle is better than a car because it:", ["needs no fuel and causes no smoke", "goes faster", "carries more people", "is more costly"]),
 m("City planners have:", ["marked cycle lanes and hire stands", "banned cars", "closed roads", "raised taxes"]),
 m("Which problem of cyclists is NOT mentioned?", ["Lack of air in tyres", "Fear of accidents", "Theft", "Tiring weather"]),
 m("'Quiet comeback' suggests that the change is:", ["gradual and unnoticed", "loud and sudden", "violent", "forced"]),
 S("Give two reasons why people are turning to bicycles.", "No fuel, little space, no smoke, keeps them fit (any two).", 1),
 S("What do hire stands allow?", "A person can hire a cycle for an hour and leave it at another stand.", 1),
 S("What effect have such schemes had?", "They have cut short car trips in a few cities.", 1),
 S("What must authorities do to promote cycling?", "Make roads safer.", 1),
 S("Find a word in the passage that means 'plain and ordinary'.", "Humble.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>School Library Timetable and Rules</b></p><p>The library is open from <b>8:30 a.m. to 3:30 p.m.</b> on all working days, and till <b>1:00 p.m.</b> on Saturdays. Students of Classes 6–8 may borrow <b>two books</b> for <b>10 days</b>; students of Classes 9–12 may borrow <b>three books</b> for <b>14 days</b>. A fine of <b>₹2 per day</b> will be charged for each book returned late. Reference books, encyclopaedias and newspapers cannot be issued. Silence must be maintained. Lost books must be replaced by the borrower. A 'Book of the Month' will be displayed near the entrance.</p>""",
[m("On Saturdays the library is open till:", ["1:00 p.m.", "3:30 p.m.", "12:00 noon", "5:00 p.m."]),
 m("A Class 9 student may borrow:", ["three books for 14 days", "two books for 10 days", "one book for 7 days", "five books for a month"]),
 m("The fine per day per book is:", ["₹2", "₹5", "₹10", "₹1"]),
 m("Which items cannot be issued?", ["Reference books and newspapers", "Novels", "Poetry books", "Magazines"]),
 m("If a book is lost, the borrower should:", ["replace it", "pay nothing", "report to the police", "ignore it"]),
 S("What time does the library open on working days?", "8:30 a.m.", 1),
 S("For how many days can a Class 7 student keep a book?", "10 days.", 1),
 S("Where is the 'Book of the Month' displayed?", "Near the entrance.", 1),
 S("What must students maintain in the library?", "Silence.", 1),
 S("How much fine will a student pay for two books returned 3 days late?", "₹2 × 2 × 3 = ₹12.", 1)],
 title="Read the following rules and answer the questions that follow."),
)

SETS[6] = dict(
P1=P("""<p>Every village in India has a story hidden in its skyline. A temple spire, a well, a banyan tree and a school building form a small family of places where people meet. These places teach us something that no textbook can: that a community survives because its members look after shared things.</p>
<p>Consider the village pond. In many places it was dug by the people themselves and cleaned each year before the rains. It gave water to cattle, a place for children to swim and a cool spot for elders to talk in the evening. Today, in many places, ponds are filled with garbage or built over. When this happens, the village loses not only water but also a meeting place.</p>
<p>Some villages have shown another path. In one village, youth groups have cleaned the pond, planted trees around it and put up a signboard asking visitors to keep it clean. Within two years, birds returned, and a weekly market began on its bank. The lesson is that public places stay alive only when ordinary people take responsibility for them.</p>""",
[m("The writer says that village places teach us that:", ["a community survives by caring for shared things", "textbooks are useless", "temples are the oldest", "wells are needed"]),
 m("A village pond was used for all EXCEPT:", ["running a factory", "watering cattle", "children swimming", "elders talking"]),
 m("When ponds are filled with garbage, a village loses:", ["water and a meeting place", "only a path", "only birds", "only trees"]),
 m("The youth groups did all of these EXCEPT:", ["sold the pond", "cleaned the pond", "planted trees", "put up a signboard"]),
 m("What returned to the village after two years?", ["birds", "floods", "factories", "snakes"]),
 S("Name two places that form the village's skyline.", "A temple spire, a well, a banyan tree or a school.", 1),
 S("How did the villagers earlier keep the pond clean?", "They cleaned it each year before the rains.", 1),
 S("What began on the pond's bank?", "A weekly market.", 1),
 S("Find a word that means 'something shared by all people'.", "Public (public places).", 1),
 S("What is the lesson of the passage?", "Public places stay alive when ordinary people take responsibility.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p>A school conducted a survey on the favourite subjects of 120 students of Class 9.</p><table><tr><th>Subject</th><th>Number of students</th></tr><tr><td>Mathematics</td><td>30</td></tr><tr><td>Science</td><td>36</td></tr><tr><td>English</td><td>24</td></tr><tr><td>Social Science</td><td>18</td></tr><tr><td>Hindi</td><td>12</td></tr></table>""",
[m("Which subject is the most popular?", ["Science", "Mathematics", "English", "Hindi"]),
 m("How many students prefer Hindi?", ["12", "18", "24", "30"]),
 m("How many students chose English or Social Science?", ["42", "36", "54", "30"]),
 m("Science is preferred by how many more students than English?", ["12", "6", "24", "18"]),
 m("The total of all students is:", ["120", "100", "110", "130"]),
 S("Which subject is least popular?", "Hindi.", 1),
 S("What fraction of the students like Mathematics?", "30/120 = 1/4.", 1),
 S("How many students like Mathematics and Science together?", "30 + 36 = 66.", 1),
 S("Is English more popular than Social Science?", "Yes, 24 against 18.", 1),
 S("Suggest one way the school can make the least popular subject interesting.", "Use activities, stories, drama or projects.", 1)],
 title="Read the following data and answer the questions that follow."),
)

SETS[7] = dict(
P1=P("""<p>Honesty is often described as the best policy, but it is not always the easiest one. A student who has not studied may feel tempted to copy. A shopkeeper who has been given extra change may be tempted to keep quiet. Such moments are small and pass quickly, yet it is in these moments that character is built.</p>
<p>A story is told of a young boy who found a purse on the road. It held more money than his family earned in a month. He walked to the address written inside and returned it to its owner. The owner offered him a reward, but the boy refused. 'I only did what was right,' he said. The old man later helped him with his schooling.</p>
<p>Honesty does not always bring a reward, and it should not be practised for one. Its real gift is peace of mind. A person who is honest has nothing to hide, nothing to remember and nothing to fear. Trust grows around such a person like a quiet shade tree.</p>""",
[m("According to the writer, character is built in:", ["small moments of choice", "large public events", "holidays", "exams only"]),
 m("The boy in the story found:", ["a purse full of money", "a mobile phone", "a bag of books", "a watch"]),
 m("The boy refused the reward because he:", ["believed he had only done what was right", "disliked money", "was afraid", "was rich"]),
 m("What did the old man later do?", ["Helped him with schooling", "Hired him", "Sent him away", "Gave him a shop"]),
 m("'Trust grows around such a person like a quiet shade tree' is an example of a:", ["simile", "metaphor", "alliteration", "pun"]),
 S("Give one example of temptation mentioned in the passage.", "Copying in an exam or keeping extra change.", 1),
 S("How did the boy find the owner of the purse?", "He used the address written inside.", 1),
 S("What is the real gift of honesty?", "Peace of mind.", 1),
 S("Find a word in the passage that means 'attracted to do something wrong'.", "Tempted.", 1),
 S("Why does an honest person have nothing to fear?", "He has nothing to hide or remember.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>Bus Pass Scheme — Notice</b></p><p>The State Transport Department has launched a <b>Student Bus Pass</b> for school and college students. The monthly pass costs <b>₹150</b> and permits unlimited travel within the city limits on all ordinary buses between <b>6 a.m. and 8 p.m.</b> Students must apply online or at any bus depot with a <b>bonafide certificate</b> from their institution, a <b>passport-size photograph</b> and an <b>ID proof</b>. The pass is valid for <b>30 days</b> from the date of issue. Duplicate passes will be issued for a fee of ₹30. Applications will be processed within <b>three working days</b>.</p>""",
[m("The monthly bus pass costs:", ["₹150", "₹30", "₹300", "₹50"]),
 m("The pass is valid for:", ["30 days", "7 days", "1 year", "60 days"]),
 m("Travel is allowed between:", ["6 a.m. and 8 p.m.", "all day and night", "8 a.m. and 5 p.m.", "10 a.m. and 6 p.m."]),
 m("Which document is required with the application?", ["bonafide certificate", "bank passbook", "driving licence", "voter ID"]),
 m("A duplicate pass costs:", ["₹30", "₹150", "₹15", "₹100"]),
 S("Who can get the pass?", "School and college students.", 1),
 S("Where can one apply?", "Online or at any bus depot.", 1),
 S("How soon will the application be processed?", "Within three working days.", 1),
 S("Name two things that must be submitted along with the form.", "Photograph and ID proof (also bonafide certificate).", 1),
 S("On which buses is the pass valid?", "Ordinary buses within city limits.", 1)],
 title="Read the following notice and answer the questions that follow."),
)

SETS[8] = dict(
P1=P("""<p>The great banyan tree in many Indian villages is more than a tree. Its roots drop from the branches and become new trunks, so that one tree can cover the area of a small field. Birds nest in it, cattle rest beneath it and the village elders often hold their meetings in its shade.</p>
<p>Trees give more than shade. They absorb carbon dioxide, release oxygen and cool the air around them. A single tree can hold the soil with its roots so that heavy rain does not wash it away. Forests act like sponges, soaking up rainwater and releasing it slowly into streams.</p>
<p>Yet each year we lose large stretches of forest for roads, mines and buildings. Planting a sapling is easy; making it survive is harder. A sapling needs water in summer, a guard against cattle and love for several years. The best way to celebrate a birthday or an anniversary is to plant a tree and promise to look after it. Such a promise, kept for ten years, may be the most useful gift one ever gives.</p>""",
[m("The banyan tree spreads because its:", ["roots drop from branches and become trunks", "seeds fly", "leaves are large", "bark is thick"]),
 m("Elders hold meetings:", ["in the shade of the banyan", "at the temple", "in the school", "at the pond"]),
 m("Trees help the soil by:", ["holding it with their roots", "making it wet", "making it rocky", "burning it"]),
 m("Forests are compared to:", ["sponges", "mountains", "walls", "rivers"]),
 m("A sapling needs all of these EXCEPT:", ["fertiliser from a factory", "water in summer", "protection from cattle", "care for years"]),
 S("Name two things trees do for the air.", "Absorb carbon dioxide and release oxygen (also cool the air).", 1),
 S("Why are forests being lost?", "For roads, mines and buildings.", 1),
 S("What does the writer suggest for birthdays?", "Plant a tree and promise to look after it.", 1),
 S("Find a word in the passage meaning 'a young tree'.", "Sapling.", 1),
 S("What makes planting a tree harder than it seems?", "Making the sapling survive needs years of care.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p>The bar chart below was described in a school magazine. During a week-long Eco Drive, the students of a school collected waste paper. The totals (in kg) for the five days were: Monday 18, Tuesday 25, Wednesday 22, Thursday 30, Friday 35.</p><table><tr><th>Day</th><th>Paper collected (kg)</th></tr><tr><td>Monday</td><td>18</td></tr><tr><td>Tuesday</td><td>25</td></tr><tr><td>Wednesday</td><td>22</td></tr><tr><td>Thursday</td><td>30</td></tr><tr><td>Friday</td><td>35</td></tr></table>""",
[m("On which day was the most paper collected?", ["Friday", "Monday", "Thursday", "Tuesday"]),
 m("The least paper was collected on:", ["Monday", "Wednesday", "Tuesday", "Friday"]),
 m("The total paper collected in the five days is:", ["130 kg", "120 kg", "110 kg", "140 kg"]),
 m("How many kg more were collected on Friday than on Monday?", ["17 kg", "15 kg", "10 kg", "20 kg"]),
 m("On which day did collection fall compared with the previous day?", ["Wednesday", "Tuesday", "Thursday", "Friday"]),
 S("How many kilograms were collected on Thursday?", "30 kg.", 1),
 S("What was the average collection per day?", "130 ÷ 5 = 26 kg.", 1),
 S("Which two consecutive days had the largest increase?", "Wednesday to Thursday and Thursday to Friday (increase of 8 and 5; Wednesday to Thursday is largest at 8 kg).", 1),
 S("What was the drive meant to promote?", "Recycling and care for the environment.", 1),
 S("Suggest one way to use the collected paper.", "Send it for recycling.", 1)],
 title="Read the following data and answer the questions that follow."),
)
