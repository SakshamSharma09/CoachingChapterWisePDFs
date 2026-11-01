"""Class 9 Writing & Grammar sets 1-5 (original). W = [notice(3) OR, letter(5) OR, paragraph(4) OR]; G = 8 grammar items."""
from eng9_lib import Q, OR, mcq

def N(q, ans): return Q(q, ans, "3")
def L(q, ans): return Q(q, ans, "5")
def A(q, ans): return Q(q, ans, "4")
def g(q, ans): return Q(q, ans, "1")
FN = "<i>(Format 1 · Content 1 · Language 1)</i>"
FL = "<i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>"
FA = "<i>(Content 2 · Organisation 1 · Language 1)</i>"

SETS = {}

SETS[1] = dict(
W=[
 OR(N("Your school is organising a Book Fair. Write a notice in not more than 50 words giving details. You are the Head Boy/Head Girl.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>2 November 2026<br><b>BOOK FAIR</b><br>A Book Fair will be held in the school hall from 9 to 11 November 2026, 9 a.m. to 3 p.m. Books on fiction, science and general knowledge will be available at 10% discount. Students may visit during recess and after school.<br>Head Boy/Head Girl<br>" + FN),
    N("The school is organising a Tree Plantation Drive. Write a notice in not more than 50 words inviting students to volunteer. You are the Secretary of the Eco Club.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>2 November 2026<br><b>TREE PLANTATION DRIVE</b><br>The Eco Club will hold a tree plantation drive on 14 November 2026 at 8 a.m. in the school campus. Interested students of Classes 8–10 should give names to the undersigned by 10 November. Bring a cap and a water bottle.<br>Secretary, Eco Club<br>" + FN)),
 OR(L("You are Ravi/Ravina. Write a letter to the Editor of a newspaper, in about 120 words, expressing concern about the increasing use of plastic bags in your city and suggesting remedies.",
      "12, Lal Kothi<br>Jaipur<br>2 November 2026<br>The Editor<br>The Daily Chronicle<br>Jaipur<br>Subject: Menace of plastic bags<br>Sir/Madam,<br>Through your newspaper I wish to draw attention to the growing use of plastic bags in our city. They choke drains, harm stray animals and spoil our parks. Though the use of thin bags is banned, shops still give them freely. I suggest that the municipal authorities should fine shopkeepers who break the law, provide cloth bags at low cost and run awareness campaigns in schools. Citizens too must carry their own bags. I hope this letter will be published.<br>Yours truly,<br>Ravi/Ravina<br>" + FL),
    L("You are Anil/Anita. Write a letter to your friend in about 120 words telling him/her about a school picnic you recently enjoyed.",
      "18, Civil Lines<br>Jaipur<br>2 November 2026<br>Dear Karan,<br>I hope you are well. Last Saturday our school organised a picnic to Sisodia Rani Garden. We left at 8 a.m. in two buses singing songs. In the garden we played cricket, had a delicious lunch and later enjoyed antakshari. Our teachers joined in the fun. We returned at five in the evening, tired but happy. I wish you had been with us. Do write to me about your plans for the winter break.<br>Yours affectionately,<br>Anil/Anita<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'The Importance of Sleep for Students'.",
      "Sleep is as important to students as food. During sleep the body repairs itself and the brain stores what it has learned. A student who sleeps for eight hours feels fresh, remembers lessons well and stays cheerful. Lack of sleep causes tiredness, poor concentration and bad temper. To sleep well one must keep a fixed bedtime, avoid screens late at night and have a light dinner. Thus, good sleep is the key to good health and good marks.<br>" + FA),
    A("Write a paragraph in about 100 words on 'My Favourite Teacher'.",
      "My favourite teacher is Mrs Sharma, who teaches us English. She is kind, patient and always smiling. She explains difficult lessons with simple examples and encourages every student to speak. She tells stories and teaches us values like honesty and hard work. When someone makes a mistake she corrects gently. Because of her I have started loving reading. I hope to become as helpful to others as she is.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect form of the verb: When we reached the station, the train ______ (leave).", "had left."),
 g("Add a suitable prefix to form the opposite of 'polite'.", "impolite."),
 g("Complete the binomial: sooner or ______.", "later."),
 g("Choose the correct option: The idiom 'to burn the midnight oil' means to (study late into the night / light a lamp / waste oil).", "study late into the night."),
 g("Fill in the blank with a suitable preposition: She is good ______ painting.", "at."),
 g("Rewrite in reported speech: Ravi said, \"I am reading a book.\"", "Ravi said that he was reading a book."),
 g("Change into passive voice: The students planted ten trees.", "Ten trees were planted by the students."),
 g("Rearrange to form a meaningful sentence: the / of / elders / respect / we / should", "We should respect the elders."),
])

SETS[2] = dict(
W=[
 OR(N("Your school is arranging a blood donation awareness talk. Write a notice in not more than 50 words. You are the school captain.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>5 November 2026<br><b>AWARENESS TALK ON BLOOD DONATION</b><br>A talk by Dr. Meena Gupta of the Red Cross Society will be held on 12 November 2026 at 11 a.m. in the school auditorium. Students of Classes 9–12 are requested to attend.<br>School Captain<br>" + FN),
    N("Your school wants to sell old textbooks at a Book Exchange. Write a notice in not more than 50 words. You are the Librarian.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>5 November 2026<br><b>BOOK EXCHANGE</b><br>A Book Exchange will be held in the library on 19 November 2026 from 2 to 4 p.m. Students may bring old textbooks in good condition and exchange them with those of other classes.<br>Librarian<br>" + FN)),
 OR(L("You are Mohit/Mohini. Write a letter to the Principal requesting a day's leave for your sister's wedding, in about 120 words.",
      "22, Gandhi Nagar<br>Jaipur<br>5 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Leave for one day<br>Respected Sir/Madam,<br>I request you to grant me leave on 12 November 2026 since my sister's wedding will take place on that day. I have to attend the ceremonies and help my family. I shall complete my class work after returning. Kindly grant me leave for one day.<br>Yours obediently,<br>Mohit/Mohini<br>Class IX<br>" + FL),
    L("You are Rita/Rohan. Write a letter to your grandmother in about 120 words describing how you spent Diwali.",
      "5, Vidhyadhar Nagar<br>Jaipur<br>5 November 2026<br>Dear Dadi,<br>Namaste. I hope you are well. This Diwali we cleaned the house, lit diyas and made rangoli at the entrance. In the evening we worshipped Lakshmi and exchanged sweets with neighbours. I burst a few crackers carefully, but we kept the noise low. I missed you very much and wish you had been with us. Please come soon.<br>Your loving grandchild,<br>Rita/Rohan<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'Benefits of Reading Newspapers'.",
      "Reading newspapers keeps us in touch with the world. We learn about local events, politics, sports and science. Editorials help us understand different views. Reading also improves vocabulary and writing. Students who read daily become aware citizens. Newspapers also give advertisements and job notices. However, one should read reliable newspapers. Therefore, a daily habit of reading a newspaper is useful for everyone.<br>" + FA),
    A("Write a paragraph in about 100 words on 'A Visit to a Fair'.",
      "Last Sunday I visited a fair near our town. There were swings, stalls of toys and sweets and a giant wheel. Artisans were selling handicrafts, and a puppet show attracted many children. I bought a clay toy and ate hot jalebis. We returned in the evening with happy memories.<br>" + FA)),
],
G=[
 g("Fill in the blank with simple past or past perfect: By the time she ______ (arrive), the guests had left.", "arrived."),
 g("Add a prefix to form the opposite of 'possible'.", "impossible."),
 g("Complete the binomial: pick and ______.", "choose."),
 g("Match the idiom: 'to learn the ropes' means to (understand how to do an activity / climb a rope / make ropes).", "understand how to do an activity."),
 g("Fill in the blank with a suitable conjunction: He worked hard ______ he could win a medal.", "so that."),
 g("Rewrite in reported speech: The teacher said, \"Open your books.\"", "The teacher told them to open their books."),
 g("Change into passive voice: The cook prepares lunch daily.", "Lunch is prepared daily by the cook."),
 g("Rearrange to form a meaningful sentence: is / a / of / treasure / books / source", "Books are a source of treasure."),
])

SETS[3] = dict(
W=[
 OR(N("Your school wants to start a Reading Club. Write a notice in not more than 50 words inviting members. You are the English Teacher's assistant, Rahul/Radha.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>8 November 2026<br><b>READING CLUB</b><br>A Reading Club is being formed. Interested students of Classes 8–10 may meet Mrs Rao in the library on 15 November at 2 p.m. Members will read, discuss and review books every week.<br>Rahul/Radha<br>" + FN),
    N("Your school plans a Cleanliness Week. Write a notice in not more than 50 words. You are the Student Council Secretary.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>8 November 2026<br><b>CLEANLINESS WEEK</b><br>A Cleanliness Week will be observed from 16 to 21 November 2026. Each class will clean its room and nearby areas daily. Students should help and use dustbins. The cleanest class will get a trophy.<br>Secretary, Student Council<br>" + FN)),
 OR(L("You are Vikram/Vandana of Sector 4, Jaipur. Write a letter to the Editor, in about 120 words, about the problem of stray dogs in your locality.",
      "4/12, Sector 4<br>Jaipur<br>8 November 2026<br>The Editor<br>The Morning Post<br>Jaipur<br>Subject: Stray dog menace<br>Sir/Madam,<br>I wish to draw the attention of the authorities to the growing number of stray dogs in our locality. They chase children and cyclists and several people have been bitten. I request the municipality to catch and vaccinate the dogs, build shelters and fine people who feed them near public roads. Residents must keep the streets clean to avoid attracting them. I hope for early action.<br>Yours faithfully,<br>Vikram/Vandana<br>" + FL),
    L("You are Sneha/Sameer. Write a letter to your cousin in about 120 words inviting him/her to your birthday party.",
      "9, Shastri Nagar<br>Jaipur<br>8 November 2026<br>Dear Nisha,<br>I am happy to tell you that my birthday falls on 20 November. We are having a small party at home from 5 p.m. There will be games, a cake and a magic show. I would love you to come and stay for the weekend. Please bring your guitar so that we can sing together. Ask Uncle and Aunty also to join.<br>Yours lovingly,<br>Sneha/Sameer<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'The Importance of Physical Exercise'.",
      "Physical exercise is necessary for a healthy body and mind. A daily walk or game keeps the heart strong and the muscles active. It improves sleep and reduces stress. Students who exercise concentrate better in class. Exercise also builds team spirit when done in groups. We should therefore give at least thirty minutes a day to physical activity.<br>" + FA),
    A("Write a paragraph in about 100 words on 'My Hobby'.",
      "My hobby is gardening. Every morning I water the plants, remove weeds and pick flowers. I have grown roses, marigolds and tomatoes in our small garden. Gardening gives me fresh air, exercise and calm. It also teaches patience, since plants grow slowly. I enjoy sharing the vegetables with neighbours.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect: Before the film began, we ______ (buy) the tickets.", "had bought."),
 g("Make the opposite by adding a prefix: 'understand'.", "misunderstand."),
 g("Complete the binomial: hit and ______.", "run (or miss)."),
 g("Choose the correct meaning: 'To rack one's brain' means (to think very hard / to hurt the head / to break something).", "to think very hard."),
 g("Fill in the blank: He is the ______ (tall) boy in the class.", "tallest."),
 g("Rewrite in reported speech: She said, \"I will come tomorrow.\"", "She said that she would come the next day."),
 g("Change into passive voice: Someone has stolen my pen.", "My pen has been stolen."),
 g("Rearrange to form a meaningful sentence: reading / good / is / habit / a", "Reading is a good habit."),
])

SETS[4] = dict(
W=[
 OR(N("Your school is going on an educational trip to a museum. Write a notice in not more than 50 words. You are the Class Teacher.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>MUSEUM VISIT</b><br>Class IX will visit the Albert Hall Museum on 18 November 2026. The bus will leave at 8 a.m. Students should bring lunch, water and a notebook and submit the consent slip by 14 November.<br>Class Teacher<br>" + FN),
    N("Your school will conduct a Quiz Contest. Write a notice in not more than 50 words inviting teams. You are the Quiz Club Secretary.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>INTER-CLASS QUIZ CONTEST</b><br>An Inter-Class Quiz will be held on 22 November 2026 at 11 a.m. in the auditorium. Each class may send a team of three students. Names should reach the undersigned by 17 November.<br>Secretary, Quiz Club<br>" + FN)),
 OR(L("You are Deepak/Deepika. Write a letter to the Principal requesting a transfer certificate, in about 120 words.",
      "7, Mansarovar<br>Jaipur<br>10 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Request for Transfer Certificate<br>Respected Sir/Madam,<br>My father has been transferred to Bhopal and our family will shift next month. I request you to issue my Transfer Certificate and report card at the earliest. I have paid all dues. I shall be grateful for your help.<br>Yours obediently,<br>Deepak/Deepika<br>Class IX<br>" + FL),
    L("You are Aman/Anjali. Write a letter to your friend in about 120 words congratulating him/her on winning a prize in a drawing competition.",
      "21, Malviya Nagar<br>Jaipur<br>10 November 2026<br>Dear Priya,<br>I was delighted to hear that you won the first prize in the state drawing competition. Your painting of the village fair truly deserved it. I know how hard you worked for months. Your parents and teachers must be very proud. Please send me a photograph of the painting. Keep up the good work and aim higher.<br>Yours sincerely,<br>Aman/Anjali<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'Road Safety'.",
      "Road accidents take many lives every year. Most can be prevented by following simple rules. Drivers should obey signals, avoid speeding and wear seat belts or helmets. Pedestrians should cross at zebra crossings. Children should not play on roads. Schools should teach road safety. If everyone follows rules, roads will be safe.<br>" + FA),
    A("Write a paragraph in about 100 words on 'A Rainy Day'.",
      "It was a rainy day. Dark clouds covered the sky and cool winds blew. Soon heavy rain began. Children sailed paper boats in puddles and farmers rejoiced. The roads were wet, and traffic moved slowly. In the evening we drank hot tea and ate pakoras. The rain made everything fresh.<br>" + FA)),
],
G=[
 g("Fill in the blank with the past perfect: She told me that she ______ (see) the film already.", "had seen."),
 g("Make the opposite by adding a prefix: 'honest'.", "dishonest."),
 g("Complete the binomial: ups and ______.", "downs."),
 g("Choose the correct meaning: 'To draw a blank' means (to be unable to remember / to draw a picture / to leave a page empty).", "to be unable to remember."),
 g("Fill in the blank with a suitable article: He is ______ honest man.", "an."),
 g("Rewrite in reported speech: He said, \"I have finished my work.\"", "He said that he had finished his work."),
 g("Change into passive voice: The teacher is checking the notebooks.", "The notebooks are being checked by the teacher."),
 g("Rearrange to form a meaningful sentence: we / water / must / save", "We must save water."),
])

SETS[5] = dict(
W=[
 OR(N("Your school is organising a Yoga Camp. Write a notice in not more than 50 words. You are the Sports Captain.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>12 November 2026<br><b>YOGA CAMP</b><br>A free Yoga Camp will be held from 20 to 22 November 2026, 7 to 8 a.m., on the school ground. All students of Classes 6–10 may attend. Wear comfortable clothes and carry a mat.<br>Sports Captain<br>" + FN),
    N("Your school has found a lost water bottle. Write a notice in not more than 50 words. You are the School Secretary.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>12 November 2026<br><b>FOUND</b><br>A blue steel water bottle has been found in the playground. The owner may collect it from the school office with a proper description before 3 p.m. on 14 November.<br>School Secretary<br>" + FN)),
 OR(L("You are Kavita/Kunal. Write a letter to the Editor, in about 120 words, about the noise pollution caused by loud music at night.",
      "10, Jhotwara<br>Jaipur<br>12 November 2026<br>The Editor<br>The Times Daily<br>Jaipur<br>Subject: Noise pollution at night<br>Sir/Madam,<br>Loud music played late at night during functions disturbs the sleep of children, the old and the sick. Students find it hard to study. I request the authorities to enforce time limits strictly and fine offenders. Organisers should use low volume and stop by ten p.m. I hope this letter will be published.<br>Yours faithfully,<br>Kavita/Kunal<br>" + FL),
    L("You are Naman/Nisha. Write a letter to your younger brother in about 120 words advising him to take care of his health.",
      "Hostel Room 15<br>Jaipur<br>12 November 2026<br>Dear Rohan,<br>I was sad to learn that you have been ill often. You should eat home-cooked food, avoid street snacks and sleep on time. Play outdoors for an hour every day and drink plenty of water. Do not skip breakfast. A healthy body helps a sharp mind. Please follow my advice and write to me soon.<br>Your loving brother/sister,<br>Naman/Nisha<br>" + FL)),
 OR(A("Write a paragraph in about 100 words on 'The Value of Time'.",
      "Time is the most valuable thing we have. Once lost, it never returns. A student who makes a timetable and follows it succeeds easily. Wasting time on idle talk or games spoils our future. We should do each work at the right time and never delay it for tomorrow. Time well used brings success.<br>" + FA),
    A("Write a paragraph in about 100 words on 'Digital India'.",
      "Digital India aims to bring technology to every citizen. Services like online payments, e-governance and digital classes have made life easier. Even villages now use the internet to sell products and learn skills. However, people must be careful about frauds and protect their data. With awareness, Digital India can make the country stronger.<br>" + FA)),
],
G=[
 g("Fill in the blank with simple past or past perfect: After he ______ (finish) his homework, he went out to play.", "had finished."),
 g("Make the opposite by adding a prefix: 'important'.", "unimportant."),
 g("Complete the binomial: all or ______.", "nothing."),
 g("Match the meaning: 'to hit the books' means (to study seriously / to throw books / to buy books).", "to study seriously."),
 g("Fill in the blank with a suitable preposition: He has been waiting ______ morning.", "since."),
 g("Rewrite in reported speech: She said, \"I like this poem.\"", "She said that she liked that poem."),
 g("Change into passive voice: They are repairing the road.", "The road is being repaired by them."),
 g("Rearrange to form a meaningful sentence: students / the / library / in / read / books", "The students read books in the library."),
])
