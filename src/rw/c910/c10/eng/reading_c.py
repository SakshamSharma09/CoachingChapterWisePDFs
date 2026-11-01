"""Reading sets 6–10 (original passages)."""
from eng_lib import P, S

def m(q, o): return S(q, "a", 1, o)
def tbl(head, rows):
    return "<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
T1 = "Read the following passage carefully and answer the questions that follow."
T2 = "Read the following case and answer the questions that follow."
SETS = {}

# ───────────── SET 6 : volunteering ─────────────
SETS[6] = dict(
P1=P("""<p>A boy of fifteen, Imran, once spent his Sunday mornings teaching the children of a nearby construction site to read. He had no certificate to give them, no classroom to teach them in, only a few old picture books and a patch of shade under a neem tree. At the end of a year, eleven of those children could read a newspaper headline. 'I didn't do anything great,' he said. 'I only turned up.'</p>
<p>Those three words, 'only turned up', contain the whole secret of voluntary work. Most of us imagine that service to others needs money, time and special training. It needs something simpler: the habit of noticing that someone nearby needs help, and the decision to give a little of what we have. A student can give a hour of explaining a lesson. A retired teacher can give an evening of stories. A shopkeeper can give a corner of his shop for a book-box.</p>
<p>Volunteering also helps the giver. Studies in several countries have found that people who volunteer regularly are happier, more confident and less lonely. In helping, they discover skills they did not know they had. Imran, for example, found that he could explain a difficult idea in the simplest words, a gift that later served him well in his own examinations.</p>
<p>It is true that good intentions are not enough. A volunteer must be reliable. A child who has been promised a lesson and finds no teacher waiting learns a sad lesson in place of the planned one. The true volunteer is therefore not the one who starts with a great show, but the one who keeps coming back, quietly, until the work is done.</p>""",
[m("Imran's Sunday classes were held:", ["under a neem tree", "in a school hall", "in a library", "in his home"]),
 m("By the end of a year, eleven children could:", ["read a newspaper headline", "write essays", "speak English fluently", "pass the Class 10 examination"]),
 m("'Only turned up' is called the secret of voluntary work because service needs:", ["the habit of being present and helpful", "a great deal of money", "special degrees", "public praise"]),
 m("Studies have found that regular volunteers are:", ["happier and more confident", "richer", "more tired", "more famous"]),
 m("Why must a volunteer be reliable?", ["A child may be disappointed if no teacher comes", "Reliability earns money", "Schools demand it", "It gives fame"]),
 S("Name two things Imran had for his classes.", "A few old picture books and a patch of shade under a neem tree.", 1),
 S("Give one example of what a retired teacher can offer.", "An evening of stories.", 1),
 S("What skill did Imran discover in himself?", "The ability to explain a difficult idea in the simplest words.", 1),
 S("Find a word in the passage which means 'done by choice, without being paid'.", "Voluntary.", 1),
 S("Find a word in the passage which is the opposite of 'disappointing' or 'unreliable'.", "Reliable.", 1)], title=T1),
P2=P("""<p>The notice below was put up by the Social Service League of a school.</p>
<p style="text-align:center"><b>SOCIAL SERVICE LEAGUE — VOLUNTEERS WANTED</b><br>
A weekend 'Teach and Share' camp for children of the Shanti Nagar basti.<br>
Dates: Saturday and Sunday, 5–6 December 2026 &nbsp;|&nbsp; Time: 9:00 a.m. to 12:00 noon<br>
Who can join: Students of Classes 9–12 &nbsp;|&nbsp; Number of places: 30<br>
Tasks: Reading help, drawing, simple science experiments, games<br>
Please bring: Water bottle, a notebook and one good story to tell.<br>
Name to the Secretary, Aarti Verma (Class 11-B), by 28 November.</p>""",
[m("How long will the camp run each day?", ["3 hours", "2 hours", "4 hours", "6 hours"]),
 m("Who is the secretary of the League?", ["Aarti Verma", "Imran", "The principal", "A teacher"]),
 m("Which of these is NOT one of the tasks?", ["Teaching computer coding", "Reading help", "Drawing", "Games"]),
 S("For whom is the camp organised?", "For the children of the Shanti Nagar basti.", 1),
 S("What is the last date to give one's name?", "28 November.", 1),
 S("How many volunteers will be selected?", "30.", 1),
 S("What are volunteers asked to bring?", "A water bottle, a notebook and one good story.", 1),
 S("On which days of the week will the camp be held?", "Saturday and Sunday.", 1),
 S("Why do you think volunteers must tell a story?", "Stories interest children and help in teaching reading and speaking.", 1),
 S("Find a word in the notice which means 'a request for people to apply or help'.", "Wanted / (volunteers) wanted.", 1)], title="Read the following notice and answer the questions that follow."),
)

# ───────────── SET 7 : plastic ─────────────
SETS[7] = dict(
P1=P("""<p>If you were to look closely at the contents of an ordinary household dustbin, you would find that more than half of what is thrown away is wrapped, packed or carried in plastic. A biscuit packet, a carry bag, a straw, a toothbrush: each one is used for a few minutes and thrown away, yet will take hundreds of years to break down. It is a strange arrangement in which the useful life of a thing is a morning and its harmful life is a century.</p>
<p>Plastic is not the villain of the story. It is light, cheap and strong, and it has made medicines safer and food fresher. The harm arises from our habit of using it once and forgetting it. Rivers carry it to the sea; fish and birds mistake it for food; and in many cities, drains choked by plastic turn a heavy shower into a flood.</p>
<p>Some governments have tried banning carry bags, with mixed results. A ban works when there is a cheap alternative ready. In a town in Kerala, for example, women's groups began stitching cloth bags from old sarees and selling them at the vegetable market for a few rupees. The ban succeeded there because shoppers were given something better than a lecture.</p>
<p>What can an ordinary person do? Carry a cloth bag. Refuse a straw. Choose a steel bottle over a disposable one. Separate wet and dry waste so that recyclers can use what is useful. None of these acts will save the planet by itself. But a habit is a vote cast every day, and a million habits can change what the market decides to sell.</p>""",
[m("More than half of the contents of a dustbin is:", ["wrapped or packed in plastic", "paper", "food", "metal"]),
 m("The 'strange arrangement' mentioned means that plastic:", ["is used for minutes but harms for centuries", "is expensive but useful", "is hard to make", "is cheap and weak"]),
 m("According to the writer, plastic is:", ["useful but harmful when used once and forgotten", "totally harmful", "useless", "a natural material"]),
 m("The ban on carry bags worked in the Kerala town because:", ["cloth bags were available as a cheap alternative", "heavy fines were charged", "shops were closed", "plastic was costly"]),
 m("A habit is compared to:", ["a vote cast every day", "a gift", "a rule", "a tax"]),
 S("How does plastic cause floods in cities?", "It chokes the drains, so heavy rain cannot flow away.", 1),
 S("Who stitched the cloth bags in the Kerala town?", "Women's groups.", 1),
 S("Mention two things that an ordinary person can do to reduce plastic.", "Carry a cloth bag and refuse a straw (or use a steel bottle).", 1),
 S("Find a word in the passage which means 'to divide into parts or sort out'.", "Separate.", 1),
 S("Find a word in the passage which means 'blocked'.", "Choked.", 1)], title=T1),
P2=P("""<p>A town survey recorded the plastic waste collected from four localities in a week and the share that was recycled.</p>""" +
tbl(["Locality", "Waste collected (kg)", "Recycled (kg)"], [["Gandhi Nagar", "400", "100"], ["Lake View", "300", "150"], ["Market Road", "500", "100"], ["Green Park", "200", "160"]]),
[m("Which locality collected the most plastic waste?", ["Market Road", "Gandhi Nagar", "Lake View", "Green Park"]),
 m("Which locality recycled the highest share of its waste?", ["Green Park", "Lake View", "Gandhi Nagar", "Market Road"]),
 m("The total waste collected in the four localities was:", ["1,400 kg", "1,000 kg", "1,200 kg", "1,500 kg"]),
 S("How much waste was recycled in all?", "100 + 150 + 100 + 160 = 510 kg.", 1),
 S("What percentage of Lake View's waste was recycled?", "50%.", 1),
 S("How much waste from Market Road was not recycled?", "400 kg.", 1),
 S("What percentage of Green Park's waste was recycled?", "80%.", 1),
 S("Suggest one step to improve recycling in Market Road.", "Provide separate bins for wet and dry waste and run an awareness drive.", 1),
 S("Which locality probably has the best waste-sorting habit? Why?", "Green Park, because it recycles 80% of its waste.", 1),
 S("Find a word in the passage which means 'places in a town'.", "Localities.", 1)], title=T2),
)

# ───────────── SET 8 : sport ─────────────
SETS[8] = dict(
P1=P("""<p>In many schools the period for games is the first to be cancelled when the syllabus runs behind. Teachers exchange a worried look, a notice is read out, and the playground is left to the dust. The assumption is that sport is a luxury and mathematics is a necessity. It is worth asking whether this is really true.</p>
<p>Consider what happens on a hockey field. A player must watch the ball, the opponents and her own teammates at the same time. She must decide in a second whether to pass or to run. If her team loses she must, within minutes, shake hands and go back to the game. A hundred such small decisions teach patience, judgement and good temper in a way no lecture can.</p>
<p>Sport also teaches a kind of honesty. On the field, a player's skill cannot be hidden behind a long answer. Either the ball goes in or it does not. Players learn to accept the result, to find out why they lost and to practise until they improve. This habit of honest practice is exactly what a student needs for studies.</p>
<p>The body, too, has its claim. Children who play for an hour a day sleep better, concentrate longer and fall ill less often. Several studies have found that students who exercise regularly perform as well as their classmates in examinations, though they spend fewer hours at their desks. A cancelled games period saves time on paper but takes it back in tiredness. The sensible school keeps the playground open, for it is also a classroom with a larger roof.</p>""",
[m("The writer begins by pointing out that in many schools:", ["games periods are cancelled first", "games are compulsory", "teachers play with students", "the playground is crowded"]),
 m("The hockey example shows that sport teaches:", ["quick judgement and good temper", "only physical strength", "only discipline", "how to defeat others"]),
 m("'Sport teaches a kind of honesty' because:", ["on the field skill cannot be hidden", "players never lie", "rules are strict", "umpires are strict"]),
 m("Children who play for an hour daily:", ["sleep better and fall ill less often", "score less", "become lazy", "forget lessons"]),
 m("'A classroom with a larger roof' means:", ["the playground", "a hall", "a library", "the sky"]),
 S("Why is sport treated as a luxury in some schools?", "People assume mathematics and other subjects are necessary and sport is not.", 1),
 S("What must a hockey player do at the same time?", "Watch the ball, the opponents and her teammates.", 1),
 S("What habit learned from sport is useful for studies?", "The habit of honest practice and improving after a loss.", 1),
 S("Find a word in the passage which means 'something not necessary but pleasant'.", "Luxury.", 1),
 S("Find a word in the passage which means 'the ability to decide wisely'.", "Judgement.", 1)], title=T1),
P2=P("""<p>The Sports Committee of a school recorded the number of students participating in four games and the number of medals won by the school in the last inter-school meet.</p>""" +
tbl(["Game", "Students participating", "Medals won"], [["Kabaddi", "24", "5"], ["Athletics", "30", "8"], ["Volleyball", "18", "2"], ["Badminton", "12", "4"]]),
[m("Which game had the most participants?", ["Athletics", "Kabaddi", "Volleyball", "Badminton"]),
 m("In which game were the fewest medals won?", ["Volleyball", "Badminton", "Kabaddi", "Athletics"]),
 m("How many medals did the school win in all?", ["19", "15", "21", "17"]),
 S("How many students took part in all the games?", "24 + 30 + 18 + 12 = 84.", 1),
 S("Which game gave the highest number of medals?", "Athletics (8).", 1),
 S("Which game had the best ratio of medals to participants?", "Badminton (4 medals from 12 students).", 1),
 S("How many more students took part in Athletics than in Badminton?", "30 − 12 = 18.", 1),
 S("Suggest one way to improve results in volleyball.", "Arrange extra coaching and more practice matches.", 1),
 S("What does the data suggest about the school's performance?", "The school did well in individual games like athletics and badminton, and needs improvement in volleyball.", 1),
 S("Find a word in the passage which means 'a gathering for competitions'.", "Meet.", 1)], title=T2),
)

# ───────────── SET 9 : kindness / honesty ─────────────
SETS[9] = dict(
P1=P("""<p>On a crowded morning, a flower seller named Kamla found a leather purse near her stall. It contained four thousand rupees, a ration card and a photograph of a smiling woman. For a few minutes she looked at it as one looks at a gift. Then she thought of the owner, who must have been looking for it with a sinking heart, and she carried it to the nearby police post. The owner turned out to be a nurse who had withdrawn her month's salary. She offered Kamla a reward. Kamla refused, saying, 'Take your money, but give me a smile; it is worth more.'</p>
<p>It is easy to praise honesty and just as easy to forget it when we are tempted. The difficulty is that honesty seldom brings an immediate prize. The dishonest man often seems to prosper, while the honest one waits. Yet if we look more closely at people whom we trust, we find that their honesty has made them rich in the only way that matters: when they speak, others listen.</p>
<p>Honesty is also a kind of freedom. A person who tells the truth does not have to remember what he said to whom. He sleeps lightly and wakes without worry. His friends know where they stand with him. A liar, on the other hand, must keep a notebook of his lies in his head and forever fear that the notebook will be found.</p>
<p>Parents can teach this lesson best by example. A child who sees his father return an extra change to the shopkeeper learns more than from a month of sermons. In every home, in every classroom, honesty is taught by the quiet things done when no one is watching.</p>""",
[m("What did Kamla find near her stall?", ["A purse with money", "A gold chain", "A mobile phone", "A bag of flowers"]),
 m("Where did she take the purse?", ["To the police post", "To her home", "To a temple", "To the market office"]),
 m("The owner of the purse was a:", ["nurse", "teacher", "shopkeeper", "policewoman"]),
 m("Kamla refused the reward because she:", ["valued the owner's smile more", "was rich", "was afraid", "was told to"]),
 m("According to the writer, honesty makes a person:", ["trusted when he speaks", "wealthy", "famous", "lonely"]),
 S("What did the purse contain?", "Four thousand rupees, a ration card and a photograph.", 1),
 S("Why is a liar compared to a person with a notebook?", "He has to remember all his lies and fear that they will be discovered.", 1),
 S("How can parents teach honesty best?", "By example, such as returning extra change to a shopkeeper.", 1),
 S("Find a word in the passage which means 'to become successful'.", "Prosper.", 1),
 S("Find a word in the passage which means 'rarely'.", "Seldom.", 1)], title=T1),
P2=P("""<p>The following advertisement appeared in a local newspaper.</p>
<p style="text-align:center"><b>LOST — A BROWN LEATHER SCHOOL BAG</b><br>
Lost on 12 October on the 7:45 a.m. city bus (Route 14, Station Road to Model School).<br>
Contains: Class 10 notebooks, a geometry box and a blue water bottle with the name 'Rohan' on it.<br>
Reward of ₹ 500 for the finder. Please contact: Rohan Mehta, 24 Park Lane. Phone: 98xx-xxx-210 (after 4 p.m.).<br>
The bag has no money; only the notes are precious.</p>""",
[m("When was the bag lost?", ["12 October", "14 October", "7 November", "12 November"]),
 m("Where was it lost?", ["On a city bus", "In a shop", "At school", "On a train"]),
 m("What is the reward offered?", ["₹ 500", "₹ 50", "₹ 5,000", "₹ 100"]),
 S("Whose name is written on the water bottle?", "Rohan.", 1),
 S("At what time can the owner be called?", "After 4 p.m.", 1),
 S("What does the bag contain?", "Class 10 notebooks, a geometry box and a water bottle.", 1),
 S("Why does the owner say 'only the notes are precious'?", "The bag has no money; the notebooks matter for his studies.", 1),
 S("Which bus route was the student travelling on?", "Route 14.", 1),
 S("What would be the right action of a person who finds the bag?", "Contact Rohan at the given address or number and return it.", 1),
 S("Find a word in the advertisement which means 'valuable'.", "Precious.", 1)], title="Read the following advertisement and answer the questions that follow."),
)

# ───────────── SET 10 : crafts / heritage ─────────────
SETS[10] = dict(
P1=P("""<p>In a narrow lane of a Rajasthan town, an old potter named Hari Ram still turns his wheel at dawn. His hands, thick with clay, know how much pressure a pot needs before it begins to bend. His grandfather made pots, so did his father, and he has always thought that his son would one day do the same. But the son has gone to the city to work in a factory. 'The pot is cheaper than the plastic jug,' says Hari Ram, 'but nobody counts the hours.'</p>
<p>India has thousands of such crafts: weaving, block printing, pottery, metal work, wood carving and embroidery. For centuries they have fed families and given beauty to daily life. Today many of them are fading. Machines produce goods faster and cheaper; young people see little respect and little money in the old trades; and customers rarely stop to ask who made the cloth or the cup that they use.</p>
<p>Yet there are signs of change. Some designers now work with village artisans and bring their patterns to a wider market. Online shops allow a weaver in a small town to sell directly to buyers in distant cities. Schools in some places invite craftspeople to teach children for a day, and the children return with clay under their nails and a new respect in their eyes.</p>
<p>What can a buyer do? Choose handmade goods when possible and pay a fair price. Ask where an item was made. Visit craft fairs. A craft survives only as long as someone is willing to buy its work and someone is willing to learn it. Both of these depend, in the end, on all of us.</p>""",
[m("Hari Ram's son has gone to the city to:", ["work in a factory", "study", "sell pots", "learn weaving"]),
 m("'Nobody counts the hours' means:", ["people do not value the time and skill that goes into the work", "the potter works little", "pots are made quickly", "customers are punctual"]),
 m("One reason why crafts are fading is that:", ["machines make goods faster and cheaper", "raw material is expensive", "crafts are banned", "there are no customers abroad"]),
 m("How do online shops help artisans?", ["They let artisans sell directly to distant buyers", "They provide clay", "They provide training", "They set prices"]),
 m("A craft survives only as long as:", ["there are buyers and learners", "the government exists", "machines are costly", "fairs are held"]),
 S("What kinds of crafts are named in the passage? Name two.", "Weaving and pottery (or block printing, metal work, wood carving, embroidery).", 1),
 S("What do children gain when craftspeople visit their school?", "A new respect for crafts and a chance to try the work.", 1),
 S("What can a buyer do to help a craft survive? Mention one.", "Choose handmade goods and pay a fair price.", 1),
 S("Find a word in the passage which means 'skilled workers who make things by hand'.", "Artisans / craftspeople.", 1),
 S("Find a word in the passage which means 'becoming weaker or disappearing slowly'.", "Fading.", 1)], title=T1),
P2=P("""<p>A craft fair recorded the stalls and sales of five types of handicrafts on its first day.</p>""" +
tbl(["Craft", "Number of stalls", "Sales (₹)"], [["Pottery", "6", "18,000"], ["Block-printed cloth", "8", "40,000"], ["Wood carving", "4", "24,000"], ["Embroidery", "5", "25,000"]]),
[m("Which craft recorded the highest sales?", ["Block-printed cloth", "Pottery", "Wood carving", "Embroidery"]),
 m("How many stalls were there in all?", ["23", "21", "25", "19"]),
 m("What were the total sales on the first day?", ["₹ 1,07,000", "₹ 1,00,000", "₹ 90,000", "₹ 1,17,000"]),
 S("What was the average sale per stall for wood carving?", "₹ 24,000 ÷ 4 = ₹ 6,000.", 1),
 S("Which craft had the lowest sales?", "Pottery (₹ 18,000).", 1),
 S("How much more did block-printed cloth sell than pottery?", "₹ 40,000 − ₹ 18,000 = ₹ 22,000.", 1),
 S("Which craft earned the same sales per stall as ₹ 5,000?", "Embroidery (₹ 25,000 ÷ 5).", 1),
 S("Suggest one way to attract more visitors to pottery stalls.", "Hold live demonstrations or let visitors try the wheel.", 1),
 S("Why do fairs help craftspeople?", "They let artisans meet buyers directly and earn a fair price.", 1),
 S("Find a word in the passage which means 'objects made by hand'.", "Handicrafts.", 1)], title=T2),
)
