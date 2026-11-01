"""Class 7 Writing & Grammar sets 1-5 (original). W = [notice/message/email (3) OR, letter (5) OR, paragraph/diary/story (4) OR]; G = 8 grammar items."""
from eng9_lib import Q, OR

def N(q, ans): return Q(q, ans, "3")
def L(q, ans): return Q(q, ans, "5")
def A(q, ans): return Q(q, ans, "4")
def g(q, ans): return Q(q, ans, "1")
FN = "<i>(Format 1 · Content 1 · Language 1)</i>"
FL = "<i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>"
FA = "<i>(Content 2 · Organisation 1 · Language 1)</i>"
SCH = "Mastermind Public School, Jaipur"

SETS = {}

SETS[1] = dict(
W=[
 OR(N("Your school is organising a Book Fair. Write a notice in not more than 50 words. You are the Head Boy/Head Girl.",
      f"<b>NOTICE</b><br>{SCH}<br>2 November 2026<br><b>BOOK FAIR</b><br>A Book Fair will be held in the school hall from 9 to 11 November 2026, 9 a.m. to 3 p.m. Story books, science books and dictionaries will be available at a discount. Students may visit during recess.<br>Head Boy/Head Girl<br>" + FN),
    N("You are going to your grandparents' home and cannot attend the school drawing competition. Write a message to your friend in about 30 words, asking him/her to inform the teacher.",
      "<b>MESSAGE</b><br>2 November 2026, 6 p.m.<br>Dear Karan,<br>I am going to my grandparents' village tonight and will miss the drawing competition tomorrow. Please inform Ms. Sharma. I will be back on Monday.<br>Rohan<br>" + FN)),
 OR(L("You are Ravi/Ravina. Write a letter to your friend in about 100 words telling him/her about your birthday celebration.",
      "14, Lal Kothi<br>Jaipur<br>2 November 2026<br>Dear Karan,<br>I hope you are fine. I want to tell you about my birthday last Sunday. I woke up to find a surprise gift from my parents, a new cricket bat. In the evening my friends came home, and we cut a chocolate cake and played games. Grandmother cooked my favourite kheer. I wish you had been there with us. Do come to Jaipur in the holidays.<br>Yours lovingly,<br>Ravi/Ravina<br>" + FL),
    L("Write a letter to the Principal in about 100 words requesting two days' leave as you are suffering from fever. You are Anil/Anita of Class 7.",
      "Class 7-B<br>Mastermind Public School<br>Jaipur<br>2 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Application for two days' leave<br>Respected Sir/Madam,<br>I beg to state that I am suffering from fever since last night, and the doctor has advised me to take rest for two days. Kindly grant me leave on 3 and 4 November 2026. I shall be grateful to you.<br>Yours obediently,<br>Anil/Anita<br>Class 7-B, Roll No. 12<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'My School Library'.",
      "Our school library is my favourite place. It is a big, airy room on the first floor with rows of shelves full of books. There are story books, encyclopedias, comics and magazines. We visit the library once a week and the librarian lets us borrow two books for a week. The library is very quiet, and the tables are neat. I enjoy reading adventure stories there. A library helps us to learn new words and to love reading. " + FA),
    A("Write a diary entry in about 80 words about the school Annual Day that you attended today.",
      "<b>Monday, 2 November 2026</b><br>9:30 p.m.<br>Dear Diary,<br>Today was the Annual Day of our school. I woke up early with excitement. We reached school by eight in new uniforms. The chief guest gave away prizes, and I received a medal for the best recitation. My class presented a lovely dance. I forgot my steps for a moment but recovered quickly. Parents clapped loudly. I am very happy and tired. What a wonderful day!<br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form of the verb: Rohan ______ (play) cricket every evening.", "plays."),
 g("Fill in the blank with a, an or the: ______ moon goes round the earth.", "The."),
 g("Choose the correct preposition: The cat jumped ______ the wall. (in / over / at)", "over."),
 g("Change into the plural: This child is playing in the garden.", "These children are playing in the garden."),
 g("Join with 'because': He was late. He missed the bus.", "He was late because he missed the bus."),
 g("Write the opposite of 'brave'.", "Cowardly (or timid)."),
 g("Rewrite in the past tense: She writes a letter.", "She wrote a letter."),
 g("Put a full stop, comma or question mark where needed: where are you going", "Where are you going?"),
])

SETS[2] = dict(
W=[
 OR(N("Your school is planning a tree plantation drive. Write a notice in not more than 50 words inviting students to volunteer. You are the Secretary of the Eco Club.",
      f"<b>NOTICE</b><br>{SCH}<br>5 November 2026<br><b>TREE PLANTATION DRIVE</b><br>The Eco Club will hold a tree plantation drive on 14 November 2026 at 8 a.m. in the school ground. Interested students of Classes 6–8 should give their names to the undersigned by 10 November.<br>Secretary, Eco Club<br>" + FN),
    N("Your elder sister has gone out. A friend of hers, Neha, phoned. Write a message in about 30 words for your sister.",
      "<b>MESSAGE</b><br>5 November 2026, 4 p.m.<br>Dear Didi,<br>Neha phoned at 3:45 p.m. She wants you to bring your Maths notebook tomorrow. Please call her back after 6 p.m.<br>Ankit<br>" + FN)),
 OR(L("Write a letter to your uncle in about 100 words thanking him for the gift he sent you on your birthday. You are Sameer/Sameera.",
      "22, Vaishali Nagar<br>Jaipur<br>5 November 2026<br>Dear Uncle,<br>Thank you very much for the lovely storybook set you sent me for my birthday. I read the first story the same evening and loved it. It was very thoughtful of you to remember my interest in adventure. All of us missed you at the party. Mother says you must come to Jaipur during Diwali. I shall show you my school prizes then.<br>Yours affectionately,<br>Sameer/Sameera<br>" + FL),
    L("Write a letter to the Principal in about 100 words requesting that the school library be kept open after school hours for Class 7 students. You are the Class Monitor.",
      "Class 7-A<br>Mastermind Public School<br>Jaipur<br>5 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Request to keep the library open after school<br>Respected Sir/Madam,<br>With due respect I wish to state that many students of Class 7 wish to read books after classes, but the library closes at the end of the last period. We therefore request you to keep it open for one hour after school. It will help us to improve our reading and complete our projects. We shall be thankful.<br>Yours obediently,<br>Class Monitor, Class 7-A<br>" + FL)),
 OR(A("Write a short paragraph in about 80 words on 'A Rainy Day'.",
      "It was a rainy day. Dark clouds covered the sky from the morning, and soon big drops began to fall. The road became wet, and children splashed in the puddles. I sailed paper boats in the lane. My mother made hot pakoras, and we had them with tea on the balcony. The air was cool and smelt of wet earth. Farmers were happy because the fields needed water. I love rainy days. " + FA),
    A("Write a diary entry in about 80 words on a visit to the zoo.",
      "<b>Sunday, 5 November 2026</b><br>8:30 p.m.<br>Dear Diary,<br>Today my family went to the zoo. We saw tigers, elephants and colourful parrots. The white tiger was my favourite. A monkey snatched a banana from a boy and ran away, and everyone laughed. We had lunch under a big tree. I learnt that animals must be protected. I returned home tired but very happy.<br>" + FA)),
],
G=[
 g("Fill in the blank with 'is' or 'are': The books on the table ______ mine.", "are."),
 g("Fill in the blank with the correct tense: They ______ (watch) a film when I reached.", "were watching."),
 g("Choose the correct article: He is ______ honest man. (a / an / the)", "an."),
 g("Write the comparative form: This bag is ______ than that one. (heavy)", "heavier."),
 g("Join using 'but': He is poor. He is happy.", "He is poor but happy."),
 g("Write the synonym of 'big'.", "Large (or huge)."),
 g("Fill in the blank with a preposition: The train arrives ______ 6 o'clock.", "at."),
 g("Change into negative: She likes tea.", "She does not like tea."),
])

SETS[3] = dict(
W=[
 OR(N("Your school is organising a quiz competition. Write a notice in not more than 50 words. You are the School Captain.",
      f"<b>NOTICE</b><br>{SCH}<br>8 November 2026<br><b>INTER-HOUSE QUIZ</b><br>An Inter-House Quiz Competition will be held on 20 November 2026 at 11 a.m. in the school auditorium. Each house will send a team of three students of Classes 7–8. Names should be given to Mr. Verma by 15 November.<br>School Captain<br>" + FN),
    N("You were to go with your mother to the market but have to stay back for a class test. Write a message in about 30 words for your mother.",
      "<b>MESSAGE</b><br>8 November 2026, 7 a.m.<br>Dear Mummy,<br>I cannot come to the market today as I have a Science test in the last period. I will be home by 4 p.m. Please go with Aunty.<br>Riya<br>" + FN)),
 OR(L("You are Rohan/Rohini. Write a letter to your friend in about 100 words inviting him/her to spend the Diwali holidays with you.",
      "9, Ashok Vihar<br>Jaipur<br>8 November 2026<br>Dear Manish,<br>How are you? I am writing to invite you to spend the Diwali holidays with us. We will decorate the house, light diyas and make sweets. My father has promised to take us to the Diwali mela and burst safe crackers. My cousins will also come. Please ask your parents' permission and reach by 6 November. I am eagerly waiting.<br>Yours lovingly,<br>Rohan/Rohini<br>" + FL),
    L("Write a letter to the Principal in about 100 words requesting a fee concession as your father has lost his job. You are Deepak/Deepa of Class 7.",
      "Class 7-C<br>Mastermind Public School<br>Jaipur<br>8 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Request for fee concession<br>Respected Sir/Madam,<br>I beg to state that my father recently lost his job, and our family is finding it hard to pay the fees. I am regular and my last result was 85%. Kindly grant me a fee concession for this year. I shall be thankful to you and work hard.<br>Yours obediently,<br>Deepak/Deepa<br>Class 7-C<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'My Favourite Festival'.",
      "My favourite festival is Diwali. It is celebrated in October or November. A week before it, we clean the house and decorate it with lamps and rangoli. On the day we wear new clothes, worship Goddess Lakshmi and light diyas. We exchange sweets with neighbours and burst a few crackers carefully. The festival teaches us that good always wins over evil. It also brings the family together. I wait for it all year. " + FA),
    A("Write a short story in about 80 words with the hints: A thirsty crow – pot with little water – pebbles – water rises – crow drinks. Give a title.",
      "<b>The Clever Crow</b><br>On a hot day a thirsty crow flew everywhere looking for water. At last he saw a pot, but it had only a little water at the bottom. His beak could not reach it. He thought for a while and then dropped pebbles into the pot one by one. The water slowly rose to the top. The crow drank happily and flew away.<br><i>Moral: Where there is a will, there is a way.</i><br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: He ______ (go) to school yesterday.", "went."),
 g("Choose the correct pronoun: Give the book to ______. (I / me / my)", "me."),
 g("Fill in the blank: She is fond ______ music.", "of."),
 g("Change into the passive voice: Ram eats a mango.", "A mango is eaten by Ram."),
 g("Write the plural of 'leaf'.", "Leaves."),
 g("Fill in with 'much' or 'many': How ______ students are there in your class?", "many."),
 g("Add a suitable prefix to make the opposite of 'happy'.", "Unhappy."),
 g("Use the correct punctuation: what a lovely day it is", "What a lovely day it is!"),
])

SETS[4] = dict(
W=[
 OR(N("Your school wants to sell its old textbooks to junior students. Write a notice in not more than 50 words. You are the Librarian.",
      f"<b>NOTICE</b><br>{SCH}<br>10 November 2026<br><b>BOOK EXCHANGE</b><br>A Book Exchange will be held in the library on 19 November 2026 from 2 to 4 p.m. Students may bring old textbooks in good condition and exchange them with those of other classes. No money will be charged.<br>Librarian<br>" + FN),
    N("Write an e-mail in about 40 words to your cousin wishing him/her success in the coming exams. Your e-mail ID is rohan@mail.com; your cousin's is suman@mail.com.",
      "<b>To:</b> suman@mail.com<br><b>From:</b> rohan@mail.com<br><b>Subject:</b> Best wishes for exams<br>Dear Suman,<br>I hope you are well. I wish you all the best for your exams. Study regularly, revise well and stay calm. I am sure you will do very well.<br>Warm regards,<br>Rohan<br>" + FN)),
 OR(L("Write a letter to your friend in about 100 words describing a trip to a fort that you recently made.",
      "11, Civil Lines<br>Jaipur<br>10 November 2026<br>Dear Sunil,<br>I want to tell you about a trip to Amer Fort. Last Sunday we went there with our class teacher. We climbed to the fort on elephants and enjoyed the view. We saw the Sheesh Mahal, whose walls shine with tiny mirrors. The guide told us stories of the Rajput kings. We had a picnic lunch in the garden. I learnt a lot about our history. I hope you will join us next time.<br>Yours sincerely,<br>Arjun<br>" + FL),
    L("Write a letter to the Principal in about 100 words complaining that the drinking water in the school is not clean. You are the Head Boy/Head Girl.",
      "Mastermind Public School<br>Jaipur<br>10 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Complaint about unclean drinking water<br>Respected Sir/Madam,<br>I wish to bring to your notice that the water in the school coolers is not clean and smells bad. Many students have complained of stomach aches. I request you to get the tanks cleaned and the filters changed. Kindly look into the matter at the earliest.<br>Yours obediently,<br>Head Boy/Head Girl<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'My Best Friend'.",
      "My best friend is Sameer. He sits next to me in class, and we have been friends since Class 3. He is honest, helpful and cheerful. When I am sad he tells funny jokes. We study together and play cricket in the evening. He shares his lunch with me, and I share my books with him. A true friend stands by you in difficult times, and Sameer is one. I am lucky to have him. " + FA),
    A("Write a diary entry in about 80 words on the day you won a prize in the school quiz.",
      "<b>Friday, 10 November 2026</b><br>9 p.m.<br>Dear Diary,<br>Today was a golden day. Our house team won the school quiz, and I answered the last question about rivers correctly. The Principal gave me a trophy in the assembly. My friends cheered, and my teacher patted my back. When I told Mummy at home, she hugged me and made halwa. I will keep reading and learning new things. Good night.<br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: The sun ______ (rise) in the east.", "rises."),
 g("Fill in the blank with a suitable conjunction: Work hard ______ you will fail. (or / and / but)", "or."),
 g("Choose the correct word: He is the ______ boy in the class. (tall / taller / tallest)", "tallest."),
 g("Change into the plural: The man has a watch.", "The men have watches."),
 g("Complete with the correct modal: You ______ obey your elders. (should / can / may)", "should."),
 g("Write the synonym of 'happy'.", "Glad (or cheerful)."),
 g("Change into the past tense: They are playing football.", "They were playing football."),
 g("Fill in the blank with a preposition: He has been ill ______ Monday.", "since."),
])

SETS[5] = dict(
W=[
 OR(N("Your school is going to hold a Yoga Camp. Write a notice in not more than 50 words. You are the Sports Captain.",
      f"<b>NOTICE</b><br>{SCH}<br>12 November 2026<br><b>YOGA CAMP</b><br>A Yoga Camp will be held from 16 to 18 November 2026 on the school ground from 7 to 8 a.m. Students of Classes 6–8 may join. Wear comfortable clothes and carry a mat. Names should be given to the PT teacher.<br>Sports Captain<br>" + FN),
    N("You are late in reaching home from school because of a puncture in the bus. Write a message in about 30 words for your parents.",
      "<b>MESSAGE</b><br>12 November 2026, 2:30 p.m.<br>Dear Mummy and Papa,<br>Our school bus has a puncture, and we are waiting on the road. I am safe with my teacher. I shall be late by about an hour. Please do not worry.<br>Neha<br>" + FN)),
 OR(L("Write a letter to your younger brother in about 100 words advising him to take care of his health.",
      "18, Shyam Nagar<br>Jaipur<br>12 November 2026<br>Dear Vikas,<br>I was sorry to hear that you have been falling ill often. You must take care of your health. Eat fresh and home-cooked food, avoid junk food and drink plenty of water. Sleep early and play outdoors for an hour daily. A healthy body keeps the mind fresh. Please follow this advice and write to me soon.<br>Your loving brother,<br>Amit<br>" + FL),
    L("Write a letter to the Editor of a newspaper in about 100 words complaining about the stray dogs in your locality.",
      "12, Gandhi Nagar<br>Jaipur<br>12 November 2026<br>The Editor<br>The Daily Chronicle<br>Jaipur<br>Subject: Menace of stray dogs<br>Sir/Madam,<br>Through your newspaper I wish to draw the attention of the authorities to the problem of stray dogs in our colony. They bark at night and chase children and cyclists. Last week a child was bitten. I request the municipal corporation to remove them to a shelter and vaccinate them. I hope this letter will be published.<br>Yours truly,<br>Rakesh Sharma<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'Importance of Games'.",
      "Games are as important as studies. They keep our body fit and our mind fresh. By playing games, we learn teamwork, discipline and the spirit of sportsmanship. They teach us to take both victory and defeat in the right spirit. Playing outdoors also gives us fresh air and good sleep. A student who plays regularly studies better. All schools should therefore give enough time to games. " + FA),
    A("Write a short story in about 80 words with the hints: A lion sleeping – a mouse runs over him – lion catches the mouse – mouse promises help – lion caught in net – mouse cuts it. Give a title.",
      "<b>The Lion and the Mouse</b><br>A lion was sleeping in a forest. A mouse ran over his body and woke him. The angry lion caught her, but she begged, \"Spare me, and I shall help you someday.\" The lion laughed and let her go. Some days later the lion was trapped in a hunter's net. The mouse heard his roar, came running and cut the ropes with her teeth. The lion was free.<br><i>Moral: A small friend can be a great help.</i><br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: She ______ (not/like) cold coffee.", "does not like (doesn't like)."),
 g("Fill in the blank with 'a' or 'an': He bought ______ umbrella.", "an."),
 g("Choose the correct option: Neither of the boys ______ present. (was / were)", "was."),
 g("Change into the interrogative: You can swim.", "Can you swim?"),
 g("Write the past tense of 'bring'.", "Brought."),
 g("Write one word for: a person who treats sick people.", "Doctor."),
 g("Fill in the blank with a preposition: She is afraid ______ spiders.", "of."),
 g("Rewrite in the passive voice: The teacher praised the students.", "The students were praised by the teacher."),
])
