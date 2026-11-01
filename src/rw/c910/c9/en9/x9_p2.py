"""Class 9 reading: NEW case-based passages (200-250 words, 8 marks: 4 MCQ + 4 short answer)."""
from eng9_lib import P, S
def m(q, o): return S(q, "a", 1, o)
T = "Read the following case and answer the questions that follow."
P2 = {}
P2[1] = P("""<p>The Eco Club of Mastermind Public School decided to reduce the paper used in the school office. In September it counted the sheets of paper used by each section and then began a campaign called 'Print Less, Save More'. Teachers were asked to send circulars through the school app and to use both sides of a sheet for rough work. Notices on the board were kept short and shared with several classes at once.</p>
<table><tr><th>Section</th><th>Sheets used in September</th><th>Sheets used in October</th></tr><tr><td>Office</td><td>2400</td><td>1500</td></tr><tr><td>Examination branch</td><td>3000</td><td>2700</td></tr><tr><td>Library</td><td>600</td><td>400</td></tr><tr><td>Classrooms</td><td>1800</td><td>1500</td></tr></table>
<p>At the end of October, the Principal congratulated the club. She noted that the Office had made the largest saving, while the Examination branch, which must print question papers, had saved the least in number. She also announced that the money saved would be used to buy saplings for the school garden, and that the campaign would continue for the whole session. Students were invited to suggest further ideas to the club's suggestion box near the main gate.</p>""",
 [m("The campaign launched by the Eco Club was called:", ["Print Less, Save More", "Paper Free School", "Green Office", "Save a Tree"]),
  m("Which section made the largest saving in sheets?", ["Office", "Library", "Classrooms", "Examination branch"]),
  m("The money saved will be used to buy:", ["saplings for the garden", "new computers", "notebooks", "printers"]),
  m("Teachers were asked to send circulars through the:", ["school app", "post", "notice board only", "students"]),
  S("How many sheets did the Library save?", "600 − 400 = 200 sheets.", 1),
  S("Why did the Examination branch save the least?", "It must print question papers.", 1),
  S("Name one way, mentioned in the text, of using less paper.", "Using both sides of a sheet for rough work (or sending circulars on the app).", 1),
  S("Where can students put suggestions for the club?", "In the suggestion box near the main gate.", 1)], title=T)
P2[2] = P("""<p>Anand lives in a small town and cycles to school every day. Last month the town administration introduced a bicycle-sharing scheme. Forty cycles were placed at four stands near the railway station, the market, the hospital and the school. Any resident can unlock a cycle with a mobile application, ride it and leave it at any stand. The first thirty minutes cost five rupees, and every additional fifteen minutes cost three rupees.</p>
<p>Anand's friend Zoya, who lives near the market, uses the scheme to reach school in fifteen minutes instead of waiting half an hour for a crowded bus. On Sunday she rode to the hospital to visit her uncle and returned in forty-five minutes of total riding time. For this she paid five rupees for the first thirty minutes and three rupees for the extra fifteen minutes. The administration says that in the first month more than nine hundred rides were recorded, and that most of them were on weekdays between seven and nine in the morning.</p>
<p>Some residents, however, complained that stands near the hospital are often empty by noon. The administration has promised to move cycles from crowded stands to empty ones every evening and to add twenty more cycles next month.</p>""",
 [m("How many cycle stands were set up?", ["Four", "Two", "Six", "Forty"]),
  m("The first thirty minutes of a ride cost:", ["five rupees", "three rupees", "eight rupees", "ten rupees"]),
  m("Most rides in the first month were taken:", ["on weekdays between seven and nine in the morning", "on Sunday evenings", "after midnight", "during school hours"]),
  m("Which complaint did residents make?", ["Stands near the hospital are often empty by noon", "Cycles are too costly", "Cycles have no brakes", "There are too many stands"]),
  S("How is a cycle unlocked?", "With a mobile application.", 1),
  S("Calculate the total amount Zoya paid for her Sunday ride.", "5 + 3 = 8 rupees.", 1),
  S("How will the administration solve the problem of empty stands?", "By moving cycles from crowded stands to empty ones every evening and adding twenty more cycles.", 1),
  S("Why does Zoya prefer the scheme to the bus?", "She reaches school in fifteen minutes instead of waiting half an hour for a crowded bus.", 1)], title=T)
P2[3] = P("""<p>A group of Class 9 students conducted a small survey on what they eat during the long break. Seventy students were asked to name the item they bought most often from the canteen. The results are shown below.</p>
<table><tr><th>Item</th><th>Number of students</th></tr><tr><td>Samosa</td><td>24</td></tr><tr><td>Sandwich</td><td>14</td></tr><tr><td>Fruit</td><td>8</td></tr><tr><td>Biscuits</td><td>16</td></tr><tr><td>Sprouts chaat</td><td>8</td></tr></table>
<p>The students presented the findings to the school nurse, who observed that nearly one-third of the children chose a fried snack. She explained that fried food is high in oil and salt, and that eating it daily may lead to tiredness and weight gain in the long run. She suggested that the canteen contractor should offer at least two healthy items, such as fruit and sprouts, at lower prices than the fried ones.</p>
<p>The Principal agreed and asked the survey team to repeat the exercise after two months. If the sale of healthy items has increased, the school will invite a nutritionist to talk to the students and parents. A poster competition on 'Eat Right, Stay Bright' will also be organised in the third week of the month.</p>""",
 [m("How many students took part in the survey?", ["70", "60", "80", "24"]),
  m("Which item was bought by the most students?", ["Samosa", "Sandwich", "Biscuits", "Fruit"]),
  m("The nurse said fried food is high in:", ["oil and salt", "vitamins", "fibre", "water"]),
  m("The poster competition will be on:", ["'Eat Right, Stay Bright'", "'Save Water'", "'Healthy Week'", "'Fit India'"]),
  S("How many students chose fruit or sprouts chaat altogether?", "8 + 8 = 16 students.", 1),
  S("What may daily fried food lead to, according to the nurse?", "Tiredness and weight gain in the long run.", 1),
  S("What did the nurse suggest to the canteen contractor?", "Offer at least two healthy items such as fruit and sprouts at lower prices than the fried ones.", 1),
  S("When will the survey be repeated?", "After two months.", 1)], title=T)
P2[4] = P("""<p>The Rajasthan Tourism Department has released a notice for the Pushkar Fair visitors. The fair will be held for eight days, beginning on 1 November. Visitors are advised to book accommodation at least a month in advance, as hotels and tented camps fill quickly. The department has set up a help desk near the bus stand, open from 7 a.m. to 9 p.m., where maps, schedules and emergency numbers are available free of charge.</p>
<p>To keep the town clean, visitors must not throw rubbish in the open. Dustbins in green and blue colours have been placed at every hundred metres: green for wet waste and blue for dry waste. Plastic bags below fifty microns are banned, and a fine of five hundred rupees will be charged to anyone found littering. Camel and horse rides near the sacred lake are allowed only in the marked area, and children must be accompanied by an adult.</p>
<p>Free medical camps will operate near the main ground in the mornings. Cultural programmes, including folk music and puppet shows, will be held every evening at the open-air stage. Entry to the programmes is free, but visitors are requested to be seated before 6:30 p.m.</p>""",
 [m("The fair will be held for:", ["eight days", "five days", "ten days", "two weeks"]),
  m("The help desk is located near the:", ["bus stand", "sacred lake", "main ground", "open-air stage"]),
  m("Dustbins for wet waste are:", ["green", "blue", "red", "yellow"]),
  m("What is the fine for littering?", ["Five hundred rupees", "One hundred rupees", "Fifty rupees", "One thousand rupees"]),
  S("Why should visitors book accommodation a month ahead?", "Hotels and tented camps fill quickly.", 1),
  S("What is available at the help desk?", "Maps, schedules and emergency numbers, free of charge.", 1),
  S("Where are camel and horse rides allowed?", "Only in the marked area near the sacred lake.", 1),
  S("Name one cultural programme mentioned.", "Folk music or puppet shows.", 1)], title=T)
P2[5] = P("""<p>The table below shows the number of books borrowed from the school library by students of different classes during one month.</p>
<table><tr><th>Class</th><th>Fiction</th><th>Science</th><th>Biography</th></tr><tr><td>VI</td><td>120</td><td>40</td><td>20</td></tr><tr><td>VII</td><td>110</td><td>55</td><td>25</td></tr><tr><td>VIII</td><td>90</td><td>70</td><td>30</td></tr><tr><td>IX</td><td>60</td><td>85</td><td>45</td></tr></table>
<p>The librarian, Mrs Chauhan, studied the figures and noticed that fiction is the favourite of younger students, while older students prefer science and biographies. She believes that this is natural, because as students move to higher classes they start to look for knowledge that helps them with their studies and with decisions about their future. At the same time she has noticed that the total number of books borrowed in Class IX is lower than that of Class VI, and she would like to change this.</p>
<p>To encourage reading, she plans a 'Book of the Month' display, in which a short review by a student will be pinned next to the chosen book. She will also invite local authors and scientists to talk to students once a term.</p>""",
 [m("Which class borrowed the most fiction books?", ["VI", "VII", "VIII", "IX"]),
  m("How many science books did Class VIII borrow?", ["70", "90", "30", "85"]),
  m("According to Mrs Chauhan, older students prefer:", ["science and biographies", "only fiction", "comics", "newspapers"]),
  m("The 'Book of the Month' display will carry:", ["a short review by a student", "the author's photograph", "a quiz", "a price list"]),
  S("What is the total number of books borrowed by Class IX?", "60 + 85 + 45 = 190.", 1),
  S("Why does the librarian think older students prefer such books?", "They look for knowledge that helps their studies and decisions about their future.", 1),
  S("Which class borrowed the fewest biographies?", "Class VI (20).", 1),
  S("Whom will she invite once a term?", "Local authors and scientists.", 1)], title=T)
P2[6] = P("""<p>The advertisement below appeared in a local newspaper.</p>
<p style="text-align:center"><b>SUNRISE COMPUTER INSTITUTE, KOTA</b><br>Summer Course for School Students — Learn to Code in 30 Days!</p>
<p>The course is meant for students of Classes 8 to 12 and will begin on 2 June. Classes will be held for two hours a day, from 10 a.m. to 12 noon, from Monday to Friday. Students will learn the basics of computers, simple programming in Python and how to create a website. Each batch will have only twenty students so that every learner receives personal attention. All study material and laboratory use are included in the fee of ₹3,500.</p>
<p>A discount of 20 per cent is offered to students who register before 15 May, and an extra 10 per cent concession is given to girl students. A certificate will be awarded to every student who completes the course with at least 80 per cent attendance, and the three best projects will win prizes. For admission, contact the institute at 22, Station Road, Kota, between 9 a.m. and 5 p.m., or visit its website. Seats are limited and are allotted on a first-come, first-served basis.</p>""",
 [m("The course is meant for students of:", ["Classes 8 to 12", "Classes 5 to 8", "Classes 1 to 5", "Class 12 only"]),
  m("How many students will be there in each batch?", ["Twenty", "Thirty", "Fifty", "Ten"]),
  m("The fee for the course is:", ["₹3,500", "₹2,000", "₹5,000", "₹350"]),
  m("A certificate is given to students who have at least:", ["80 per cent attendance", "50 per cent attendance", "full attendance", "90 per cent marks"]),
  S("For how many hours a day will classes be held?", "Two hours.", 1),
  S("Who gets the extra concession?", "Girl students (an extra 10 per cent).", 1),
  S("Name two things students will learn.", "Basics of computers, Python programming, website creation (any two).", 1),
  S("How are seats allotted?", "On a first-come, first-served basis.", 1)], title=T)
P2[7] = P("""<p>The bar chart in a school magazine showed the number of trees planted by four houses during a tree plantation week. Ashoka House planted 60 saplings, Beas House planted 45, Chambal House planted 75 and Dwarka House planted 30. The magazine editor, Rohit, noted that the plantation week was organised jointly by the Eco Club and the local Municipal Corporation, which supplied the saplings free of cost.</p>
<p>The saplings included neem, peepal, gulmohar and amla. The students dug the pits in the morning and planted the saplings in the afternoon after the soil had been softened by a shower. Each house was asked to adopt the trees it planted and to water them for the next six months. The house whose plants survive in the largest number will receive a rolling trophy at the Annual Day.</p>
<p>Rohit also wrote that the exercise taught the students responsibility. 'It is easy to plant a tree,' he wrote, 'but it takes patience to nurture it. A forest is built not in a day but through the daily work of many hands.' The Principal appreciated the effort and announced that a plaque would be placed near the garden, carrying the names of all the houses.</p>""",
 [m("Which house planted the most saplings?", ["Chambal", "Ashoka", "Beas", "Dwarka"]),
  m("Who supplied the saplings?", ["The Municipal Corporation", "The Principal", "The parents", "The Eco Club"]),
  m("The houses must water the trees for the next:", ["six months", "one week", "two years", "one month"]),
  m("The winning house will receive:", ["a rolling trophy", "a cash prize", "a certificate only", "a holiday"]),
  S("How many saplings were planted by the four houses in all?", "60 + 45 + 75 + 30 = 210.", 1),
  S("Name two types of saplings planted.", "Any two of neem, peepal, gulmohar and amla.", 1),
  S("Why were the saplings planted in the afternoon?", "The soil had been softened by a shower.", 1),
  S("What does the editor mean by 'a forest is built through the daily work of many hands'?", "A forest needs the continuous, shared effort of many people over time.", 1)], title=T)
P2[8] = P("""<p>Dr Meera Joshi, a local doctor, gave a talk to Class 9 students on 'Good Habits for a Healthy Life'. She began by asking how many students had eaten breakfast that morning. Almost a third of the hands stayed down. She explained that skipping breakfast reduces concentration in class and makes children tired by mid-morning. A simple meal of milk, fruit, and a paratha or porridge, she said, gives the brain the energy it needs.</p>
<p>The doctor advised the students to drink at least eight glasses of water a day, to sleep for nine hours and to play outdoors for an hour. She spoke about the dangers of too much screen time, such as eye strain, headaches and poor posture. 'Follow the 20-20-20 rule,' she said. 'After every twenty minutes on a screen, look at an object twenty feet away for twenty seconds.'</p>
<p>At the end, students asked questions. One asked if fast food is bad for health. Dr Joshi smiled and said that it is not a crime to eat it once in a while, but a habit of eating it daily could harm the body. The session ended with a pledge to eat breakfast, drink water and move more.</p>""",
 [m("What did nearly a third of the students not do that morning?", ["Eat breakfast", "Drink water", "Play", "Sleep"]),
  m("How many glasses of water did the doctor advise a day?", ["At least eight", "Two", "Four", "Twelve"]),
  m("The 20-20-20 rule says look at an object twenty feet away for:", ["twenty seconds", "twenty minutes", "two seconds", "one minute"]),
  m("The doctor's view on fast food was that it:", ["should not be a daily habit", "is forbidden", "is a healthy meal", "is good for the eyes"]),
  S("What happens when children skip breakfast?", "They lose concentration and feel tired by mid-morning.", 1),
  S("Name two problems caused by too much screen time.", "Eye strain, headaches and poor posture (any two).", 1),
  S("How many hours of sleep did she recommend?", "Nine hours.", 1),
  S("What pledge ended the session?", "To eat breakfast, drink water and move more.", 1)], title=T)
P2[9] = P("""<p>A town's municipal board published the following information about its water supply. The town's population is about 1,20,000, and the daily demand is 18 million litres. The board, however, is able to supply only 15 million litres a day, drawn from a river 12 kilometres away and from twelve tube-wells. As a result, many colonies receive water for only two hours in the morning.</p>
<table><tr><th>Source</th><th>Supply (million litres/day)</th></tr><tr><td>River</td><td>9</td></tr><tr><td>Tube-wells</td><td>6</td></tr></table>
<p>To cut the gap, the board has decided to repair old pipelines, which at present lose almost one-fifth of the water through leaks. It has also asked residents to install meters and to avoid washing vehicles with running hoses. Housing societies have been encouraged to collect rainwater from rooftops, and a fine of ₹2,000 will be imposed on those who waste water.</p>
<p>The board's chairman said that the supply was expected to improve by December, when a new pumping station would start working. Citizens were asked to report leakage by calling the helpline number 1916, which functions twenty-four hours a day.</p>""",
 [m("The town's daily demand for water is:", ["18 million litres", "15 million litres", "12 million litres", "6 million litres"]),
  m("Water is drawn from a river that is:", ["12 kilometres away", "2 kilometres away", "20 kilometres away", "in the town"]),
  m("Old pipelines lose almost:", ["one-fifth of the water", "half of the water", "one-tenth of the water", "all the water"]),
  m("The helpline functions:", ["twenty-four hours a day", "only in the morning", "on Sundays only", "from 9 to 5"]),
  S("How much water is the board short of every day?", "18 − 15 = 3 million litres.", 1),
  S("Name two steps the board has taken to reduce the gap.", "Repairing pipelines, asking residents to install meters, rooftop rainwater harvesting, fine for waste (any two).", 1),
  S("What will happen in December?", "A new pumping station will start working and supply is expected to improve.", 1),
  S("How much is the fine for wasting water?", "₹2,000.", 1)], title=T)
P2[10] = P("""<p>Class 9 students of a school in Udaipur took part in a heritage walk organised by the local tourism club. They started at the City Palace at 8 a.m., walked down to the lake shore and ended at an old step-well in the market. A guide named Mr Salim led the walk and explained the history of each place. He pointed out that the palace had been built over nearly 400 years by successive rulers, each adding a new wing in the style of his own time.</p>
<p>At the lake, the students learnt about the system of canals and tanks through which medieval engineers brought water to the city. Mr Salim explained that the step-well was designed to remain cool in summer and to store water for long periods. Students noted that its steps seemed to go down endlessly, with carved pillars on both sides.</p>
<p>The walk ended at 11:30 a.m. with a quiz. Each student was asked to write a short paragraph on the monument he or she liked best. Mr Salim announced that the three best paragraphs would be printed in the club's newsletter, and he reminded everyone that monuments are fragile. 'Do not write on walls or throw litter,' he said. 'They belong to all of us, today and tomorrow.'</p>""",
 [m("The heritage walk began at the:", ["City Palace", "step-well", "lake shore", "market"]),
  m("The palace was built over nearly:", ["400 years", "40 years", "100 years", "4 years"]),
  m("The step-well was designed to remain:", ["cool in summer", "warm in winter", "dry in rain", "open at night"]),
  m("The best paragraphs would be printed in the:", ["club's newsletter", "school diary", "newspaper", "magazine of the palace"]),
  S("Who led the walk?", "Mr Salim, a guide.", 1),
  S("How did the palace get its present form?", "Each ruler added a new wing in the style of his own time.", 1),
  S("How long did the walk last?", "From 8 a.m. to 11:30 a.m., i.e. three and a half hours.", 1),
  S("What did the guide ask the students to do to protect monuments?", "Not to write on walls or throw litter.", 1)], title=T)

_ADD = {
1: "<p>The club has also decided to publish a monthly 'paper meter' on the notice board, showing how many sheets each section used, so that everyone can see the progress and feel responsible for it.</p>",
3: "<p>The survey team also noted that very few students had said they brought food from home, and they plan to ask the class teachers to encourage students to carry a fruit or a homemade snack at least twice a week.</p>",
4: "<p>For further information, visitors may call the department's toll-free helpline or visit its website, where the full programme of the fair, including the timings of the camel race and the cattle show, has been uploaded.</p>",
5: "<p>Class teachers have also been asked to give students one library period every week, and to inform the librarian about the topics being taught, so that suitable books can be kept ready on the shelves.</p>",
6: "<p>Students who wish to try before enrolling may attend a free demonstration class on 25 May at 4 p.m., where the faculty will answer questions from parents and show some projects completed by earlier batches.</p>",
9: "<p>Environmental groups have welcomed the plan but have asked the board to publish a monthly report on the quantity of water saved, so that citizens can judge whether the promised improvements are really taking place.</p>",
}
for _k, _t in _ADD.items():
    P2[_k]["text"] += _t
