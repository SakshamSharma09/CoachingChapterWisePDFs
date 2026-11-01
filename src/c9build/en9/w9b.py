"""Class 9 Writing & Grammar sets 6-10 (original)."""
from eng9_lib import Q, OR, mcq

def N(q, ans): return Q(q, ans, "3")
def L(q, ans): return Q(q, ans, "5")
def A(q, ans): return Q(q, ans, "4")
def g(q, ans): return Q(q, ans, "1")
FN = "<i>(Format 1 · Content 1 · Language 1)</i>"
FL = "<i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>"
FA = "<i>(Content 2 · Organisation 1 · Language 1)</i>"
HDR = "Mastermind Public School, Jaipur<br>"
SETS = {}

def notice(date, title, body, by): return f"<b>NOTICE</b><br>{HDR}{date}<br><b>{title}</b><br>{body}<br>{by}<br>{FN}"

SETS[6] = dict(
W=[
 OR(N("Your school is organising a Fancy Dress Competition for junior classes. Write a notice in not more than 50 words. You are the Cultural Secretary.",
      notice("15 November 2026", "FANCY DRESS COMPETITION", "A Fancy Dress Competition for Classes 1–5 will be held on 27 November 2026 at 10 a.m. in the school hall. Theme: 'Freedom Fighters of India'. Names must be given to class teachers by 22 November.", "Cultural Secretary")),
    N("Your school is shifting the morning assembly to a new place for a week. Write a notice in not more than 50 words. You are the Vice-Principal.",
      notice("15 November 2026", "CHANGE IN ASSEMBLY VENUE", "From 18 to 24 November 2026 the morning assembly will be held in the auditorium instead of the ground because of repair work. Students should assemble class-wise by 8:00 a.m.", "Vice-Principal"))),
 OR(L("You are Hemant/Hema. Write a letter to the Municipal Commissioner, in about 120 words, complaining about irregular garbage collection in your area.",
      "33, Pratap Nagar<br>Jaipur<br>15 November 2026<br>The Municipal Commissioner<br>Jaipur Municipal Corporation<br>Jaipur<br>Subject: Irregular garbage collection<br>Sir/Madam,<br>I wish to bring to your notice that garbage in Pratap Nagar has not been collected for ten days. Heaps are lying on the roadside, causing foul smell and attracting flies and stray animals. There is a risk of diseases. I request you to direct the staff to collect garbage daily and to place dustbins at proper places. I hope for prompt action.<br>Yours faithfully,<br>Hemant/Hema<br>" + FL),
    L("You are Gaurav/Gauri. Write a letter to your friend in about 120 words, thanking him/her for a gift received on your birthday.",
      "6, Bani Park<br>Jaipur<br>15 November 2026<br>Dear Tanvi,<br>Thank you for the lovely book of stories you sent on my birthday. It was the best gift I received. I read it in two days and loved the tale of the clever crow. It was so thoughtful of you to remember my taste. I wish you had been here to cut the cake. Please visit us during the holidays.<br>Yours affectionately,<br>Gaurav/Gauri<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'Importance of Discipline'.",
      "Discipline means following rules in life. It teaches us to be punctual, honest and responsible. A disciplined student completes work on time and respects teachers. Soldiers, sportspersons and scientists succeed because of discipline. Without it there would be chaos in society. We should learn discipline at home and in school to become good citizens.<br>" + FA),
    A("Write a paragraph in about 100 words on 'A Memorable Journey'.",
      "My most memorable journey was a train trip to Udaipur. We left at night and woke up to see green hills outside the window. We visited the lake palaces and enjoyed a boat ride. The people were friendly and the food was tasty. I returned with many photographs and happy memories.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect: He realised that he ______ (forget) his wallet.", "had forgotten."),
 g("Make the opposite by adding a prefix: 'popular'.", "unpopular."),
 g("Complete the binomial: part and ______.", "parcel."),
 g("Choose the correct meaning: 'to learn by heart' means (to memorise / to feel love / to read slowly).", "to memorise."),
 g("Fill in the blank: Neither Ravi nor his friends ______ (is/are) present.", "are."),
 g("Rewrite in reported speech: The mother said to him, \"Eat your food.\"", "The mother told him to eat his food."),
 g("Change into passive voice: The principal will give the prizes.", "The prizes will be given by the principal."),
 g("Rearrange to form a meaningful sentence: early / rise / should / we / morning / in / the", "We should rise early in the morning."),
])

SETS[7] = dict(
W=[
 OR(N("Your school wants volunteers for a Plastic-Free Campus campaign. Write a notice in not more than 50 words. You are the Eco Club Secretary.",
      notice("17 November 2026", "PLASTIC-FREE CAMPUS", "The Eco Club invites volunteers for a plastic-free campus campaign. Students of Classes 8–10 should meet Mr Verma in Room 5 at 2 p.m. on 24 November. Volunteers will make posters and collect plastic from classrooms.", "Secretary, Eco Club")),
    N("The school is going to organise a Parent–Teacher Meeting. Write a notice in not more than 50 words. You are the Principal's secretary.",
      notice("17 November 2026", "PARENT–TEACHER MEETING", "A Parent–Teacher Meeting for Classes 9 and 10 will be held on 28 November 2026 from 10 a.m. to 1 p.m. Parents are requested to attend and meet subject teachers. Please bring the child's report card.", "Principal's Secretary"))),
 OR(L("You are Jai/Jaya. Write a letter to the Editor, in about 120 words, about the growing use of mobile phones among children and its effects.",
      "11, Raja Park<br>Jaipur<br>17 November 2026<br>The Editor<br>The Daily Herald<br>Jaipur<br>Subject: Children and mobile phones<br>Sir/Madam,<br>Today many children spend hours on mobile phones. This harms their eyes, sleep and studies and reduces outdoor play. Parents should fix time limits and encourage reading and games. Schools should organise screen-free hours. Mobile phones are useful but must be used with care. I hope you will publish my letter.<br>Yours truly,<br>Jai/Jaya<br>" + FL),
    L("You are Meera/Mohan. Write a letter to your friend in about 120 words about the new school you have joined.",
      "15, Sodala<br>Jaipur<br>17 November 2026<br>Dear Sonal,<br>I am writing to tell you about my new school. It is a large building with a playground and a library. The teachers are friendly and the students welcomed me warmly. I have already joined the debating club. I miss you and our old school but I am settling well. Do write to me and visit me soon.<br>Yours lovingly,<br>Meera/Mohan<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'The Role of Teachers in Our Life'.",
      "Teachers shape our lives. They give knowledge, teach manners and show the right path. A good teacher inspires students to dream big and work hard. They are our guides during difficult times. We should respect them and follow their advice. A society without teachers would lack wisdom.<br>" + FA),
    A("Write a paragraph in about 100 words on 'My Neighbourhood'.",
      "I live in a friendly neighbourhood. There is a small park where children play, and a temple at the corner. Shops sell fruits, vegetables and sweets. Neighbours greet one another and help in need. During festivals we celebrate together. I am proud of my locality.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect: The teacher said that the bell ______ (ring) already.", "had rung."),
 g("Make the opposite by adding a prefix: 'respect'.", "disrespect."),
 g("Complete the binomial: leaps and ______.", "bounds."),
 g("Choose the correct meaning: 'to burn the midnight oil' means (to study late at night / to light a lamp / to waste fuel).", "to study late at night."),
 g("Fill in the blank with the correct form: The children ______ (play) in the garden now.", "are playing."),
 g("Rewrite in reported speech: He said, \"We are leaving tomorrow.\"", "He said that they were leaving the next day."),
 g("Change into passive voice: The workers built the bridge.", "The bridge was built by the workers."),
 g("Rearrange to form a meaningful sentence: tradition / grandparents / a / stories / is / telling", "Telling stories is a tradition of grandparents."),
])

SETS[8] = dict(
W=[
 OR(N("Your school is organising a Career Guidance Workshop. Write a notice in not more than 50 words. You are the Head Boy/Head Girl.",
      notice("19 November 2026", "CAREER GUIDANCE WORKSHOP", "A Career Guidance Workshop for Classes 9 and 10 will be held on 3 December 2026 at 11 a.m. in the auditorium. A career counsellor, Ms Nidhi Rao, will address the students. Attendance is compulsory.", "Head Boy/Head Girl")),
    N("Your school plans a Science Model Exhibition. Write a notice in not more than 50 words. You are the Science Club Secretary.",
      notice("19 November 2026", "SCIENCE MODEL EXHIBITION", "A Science Model Exhibition will be held on 5 December 2026 from 10 a.m. to 1 p.m. in the Science Block. Students may submit their model titles to Mrs Joshi by 28 November.", "Secretary, Science Club"))),
 OR(L("You are Pooja/Pankaj. Write a letter to the Principal requesting him/her to start a computer club, in about 120 words.",
      "17, C-Scheme<br>Jaipur<br>19 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Request to start a computer club<br>Respected Sir/Madam,<br>Many students of our school are interested in coding and computers. A computer club would help them learn programming, design and safe use of the internet. It could meet once a week after school under a teacher's guidance. I request you to consider this proposal. We assure you of our full cooperation.<br>Yours obediently,<br>Pooja/Pankaj<br>Class IX<br>" + FL),
    L("You are Vishal/Vandita. Write a letter to your friend in about 120 words advising him/her to choose a hobby.",
      "9, Tilak Nagar<br>Jaipur<br>19 November 2026<br>Dear Rahul,<br>You told me that you feel bored in the evenings. I suggest that you take up a hobby such as drawing, music or gardening. A hobby uses free time well, reduces stress and develops creativity. You may begin with something simple and join a club. I am sure you will enjoy it. Do tell me which hobby you choose.<br>Yours sincerely,<br>Vishal/Vandita<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'Environment Protection'.",
      "Protecting the environment is the duty of every citizen. We should plant trees, save water, avoid plastic and use public transport. Pollution harms air, water and soil, and endangers life. Schools should teach children to care for nature. If everyone contributes a little, the Earth will remain green and healthy.<br>" + FA),
    A("Write a paragraph in about 100 words on 'A Festival I Love'.",
      "My favourite festival is Holi. On this day people play with colours, sing and dance and eat sweets like gujiya. It marks the victory of good over evil. Friends and neighbours forget quarrels and hug one another. I love the joy and unity it brings.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect: When I called him, he ______ (go) out.", "had gone."),
 g("Make the opposite by adding a prefix: 'continue'.", "discontinue."),
 g("Complete the binomial: mix and ______.", "match."),
 g("Choose the correct meaning: 'to pass with flying colours' means (to succeed brilliantly / to fly a flag / to paint a kite).", "to succeed brilliantly."),
 g("Fill in the blank with a suitable word: She is fond ______ music.", "of."),
 g("Rewrite in reported speech: Rita said, \"I have lost my pen.\"", "Rita said that she had lost her pen."),
 g("Change into passive voice: Who wrote this poem?", "By whom was this poem written?"),
 g("Rearrange to form a meaningful sentence: the / sun / the / east / rises / in", "The sun rises in the east."),
])

SETS[9] = dict(
W=[
 OR(N("Your school is going to hold a Charity Sale for flood victims. Write a notice in not more than 50 words. You are the Student Council Secretary.",
      notice("22 November 2026", "CHARITY SALE", "A Charity Sale in aid of flood victims will be held on 4 December 2026 from 10 a.m. to 2 p.m. in the school ground. Students may contribute handmade items, books and toys by 1 December to Mrs Kapoor.", "Secretary, Student Council")),
    N("Your school is changing its summer timings. Write a notice in not more than 50 words. You are the Principal.",
      notice("22 November 2026", "REVISED SCHOOL TIMINGS", "From 1 April 2027 the school will work from 7:30 a.m. to 1:30 p.m. Students are requested to reach school by 7:20 a.m. Transport timings will be changed accordingly.", "Principal"))),
 OR(L("You are Tarun/Tanya. Write a letter to the Editor, in about 120 words, on the need for more public libraries in your city.",
      "4, Murlipura<br>Jaipur<br>22 November 2026<br>The Editor<br>The Daily Chronicle<br>Jaipur<br>Subject: Need for public libraries<br>Sir/Madam,<br>Our city has very few public libraries, and many students cannot afford books. Libraries give free access to knowledge, develop reading habit and provide a quiet place for study. I request the authorities to open libraries in every ward, equip them with books and the internet and keep them open till late evening. I hope my letter will be published.<br>Yours truly,<br>Tarun/Tanya<br>" + FL),
    L("You are Rishi/Rishika. Write a letter to your uncle in about 120 words, thanking him for hosting you during the summer vacation.",
      "5, Gopalpura<br>Jaipur<br>22 November 2026<br>Dear Uncle,<br>I reached home safely. I would like to thank you and Aunty for your kindness during my stay. The trip to the fort and the evenings of storytelling were unforgettable. I learnt a lot from you. Please visit us soon, as my parents and I will be happy to host you.<br>Yours affectionately,<br>Rishi/Rishika<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'Our National Flag'.",
      "Our national flag, the Tiranga, has three colours: saffron, white and green, with the Ashoka Chakra in the centre. Saffron stands for courage, white for peace and green for prosperity. The chakra shows progress. We hoist it on Republic Day and Independence Day. We must respect it and never let it touch the ground.<br>" + FA),
    A("Write a paragraph in about 100 words on 'My Best Friend'.",
      "My best friend is Aman. He is honest, helpful and cheerful. We study together and play cricket every evening. When I am sad, he cheers me up. He shares his notes and gives good advice. A true friend like him is a blessing.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect: She told me she ______ (visit) Agra twice.", "had visited."),
 g("Make the opposite by adding a prefix: 'correct'.", "incorrect."),
 g("Complete the binomial: sink or ______.", "swim."),
 g("Choose the correct meaning: 'on and off' means (sometimes / always / never).", "sometimes."),
 g("Fill in the blank with the correct form: If it rains, we ______ (stay) at home.", "will stay."),
 g("Rewrite in reported speech: He said, \"I am going to Delhi.\"", "He said that he was going to Delhi."),
 g("Change into passive voice: Rohan solved the problem.", "The problem was solved by Rohan."),
 g("Rearrange to form a meaningful sentence: is / good / health / wealth / than / better", "Good health is better than wealth."),
])

SETS[10] = dict(
W=[
 OR(N("Your school is organising a Winter Clothes Donation Drive. Write a notice in not more than 50 words. You are the Social Service Club Secretary.",
      notice("25 November 2026", "WINTER CLOTHES DONATION DRIVE", "The Social Service Club is collecting warm clothes and blankets for the needy till 10 December 2026. Students may deposit them in the box kept outside the office. All items should be clean and in good condition.", "Secretary, Social Service Club")),
    N("The school canteen will introduce a healthy menu. Write a notice in not more than 50 words. You are the Canteen In-charge.",
      notice("25 November 2026", "HEALTHY CANTEEN MENU", "From 1 December 2026 the canteen will serve only healthy items such as fruit chaat, sprouts and sandwiches. Fried and sugary items will no longer be sold. Suggestions are welcome at the canteen counter.", "Canteen In-charge"))),
 OR(L("You are Aditya/Aditi. Write a letter to the Editor, in about 120 words, about the need to promote cycling among students.",
      "13, Sanganer<br>Jaipur<br>25 November 2026<br>The Editor<br>The Morning Post<br>Jaipur<br>Subject: Promote cycling among students<br>Sir/Madam,<br>Cycling keeps students fit and reduces pollution and traffic. Yet few students cycle because roads are unsafe. I suggest the authorities build cycle lanes, provide parking near schools and run safety awareness campaigns. Schools may reward students who cycle. I hope this letter will be published.<br>Yours truly,<br>Aditya/Aditi<br>" + FL),
    L("You are Sana/Sahil. Write a letter to your friend in about 120 words, inviting him/her to your school's Annual Day.",
      "8, Vaishali Nagar<br>Jaipur<br>25 November 2026<br>Dear Kabir,<br>Our school's Annual Day will be celebrated on 10 December at 5 p.m. There will be songs, dances and a play in which I act as a king. The chief guest will be a famous cricketer. I would be delighted if you came with your parents. Please let me know in advance so I can reserve seats for you.<br>Yours sincerely,<br>Sana/Sahil<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'Advantages of Team Work'.",
      "Team work means working together for a common goal. It divides the work, saves time and brings new ideas. Team members learn from one another and develop trust. In sports and science, big achievements are possible only through teamwork. Together, we can do what we cannot do alone.<br>" + FA),
    A("Write a paragraph in about 100 words on 'Winter Season'.",
      "Winter is a pleasant season. Mornings are foggy and the air is chilly. People wear sweaters, drink hot tea and sit around bonfires. Fruits and vegetables like oranges and carrots are plentiful. Children enjoy kite flying and outdoor games. Though the nights are long, winter brings cheer.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect: Before she left, she ______ (lock) the door.", "had locked."),
 g("Make the opposite by adding a prefix: 'interesting'.", "uninteresting."),
 g("Complete the binomial: high and ______.", "dry."),
 g("Choose the correct meaning: 'to draw a blank' means (to be unable to recall / to draw lines / to paint white).", "to be unable to recall."),
 g("Fill in the blank with a suitable word: I have lived here ______ ten years.", "for."),
 g("Rewrite in reported speech: Meena said, \"I can swim.\"", "Meena said that she could swim."),
 g("Change into passive voice: The boy broke the window.", "The window was broken by the boy."),
 g("Rearrange to form a meaningful sentence: care / environment / must / we / the / for", "We must care for the environment."),
])
