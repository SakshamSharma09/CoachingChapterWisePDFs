"""Class 7 Writing & Grammar sets 6-10 (original)."""
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

SETS[6] = dict(
W=[
 OR(N("Your school is organising a cleanliness drive. Write a notice in not more than 50 words. You are the Head Boy/Head Girl.",
      f"<b>NOTICE</b><br>{SCH}<br>15 November 2026<br><b>CLEANLINESS DRIVE</b><br>A Cleanliness Drive will be held in the school campus and the road outside on 22 November 2026 at 8 a.m. Students of Classes 6–8 are requested to join in. Gloves and bags will be provided. Please wear your house T-shirt.<br>Head Boy/Head Girl<br>" + FN),
    N("Your friend has been absent for three days. Write a message in about 30 words telling him/her about the homework given in school.",
      "<b>MESSAGE</b><br>15 November 2026, 5 p.m.<br>Dear Mohit,<br>You missed English, Maths and Science classes. Homework: English exercise 4, Maths questions 1–10 of Chapter 6, and the Science diagram. Please call me if you need help.<br>Sanjay<br>" + FN)),
 OR(L("Write a letter to your friend in about 100 words telling him/her how you spent your last Sunday.",
      "7, Malviya Nagar<br>Jaipur<br>15 November 2026<br>Dear Akash,<br>I hope you are fine. I want to tell you how I spent last Sunday. I woke up late and had a big breakfast. Then I helped Father to wash the car and played cricket with my friends in the park. In the afternoon we went to see a film. In the evening I finished my homework and watched television. It was a restful and happy day. Write to me about your Sunday.<br>Yours sincerely,<br>Rohit<br>" + FL),
    L("Write a letter to the Principal in about 100 words asking for permission to take a science exhibition team to another school. You are the Science Club Secretary.",
      "Science Club<br>Mastermind Public School<br>Jaipur<br>15 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Permission to visit the Science Exhibition<br>Respected Sir/Madam,<br>We have been invited to the Inter-School Science Exhibition at Sunrise Public School on 24 November 2026. Our club has made a working model of a water purifier. We request you to permit ten students and one teacher to go there. We shall be grateful.<br>Yours obediently,<br>Secretary, Science Club<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'The Cow'.",
      "The cow is a useful domestic animal. It has four legs, a long tail and two horns. It eats grass, hay and grain. The cow gives us milk, from which we make curd, butter and ghee. Its dung is used as manure and fuel. In India the cow is regarded as sacred and many people worship it. Cows should be treated kindly and not allowed to eat plastic. " + FA),
    A("Write a diary entry in about 80 words about a visit to a book fair.",
      "<b>Saturday, 15 November 2026</b><br>8 p.m.<br>Dear Diary,<br>Today I went to the Book Fair with Father. There were hundreds of colourful books, and I bought a book of fairy tales and a book on space. I also met an author who signed my copy. Father bought me a bookmark. We had ice cream on the way back. I could not stop smiling. I will start reading the space book tonight.<br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: The children ______ (be) happy yesterday.", "were."),
 g("Choose the correct word: This is the ______ book I have ever read. (good / better / best)", "best."),
 g("Fill in the blank with 'some' or 'any': I do not have ______ money.", "any."),
 g("Change into the plural: The baby is sleeping.", "The babies are sleeping."),
 g("Join with 'who': I met a girl. She plays the violin.", "I met a girl who plays the violin."),
 g("Write the opposite of 'ancient'.", "Modern."),
 g("Change into the passive voice: They are painting the wall.", "The wall is being painted by them."),
 g("Fill in the blank with a preposition: He divided the sweets ______ his friends.", "among."),
])

SETS[7] = dict(
W=[
 OR(N("The school is going on a one-day picnic. Write a notice in not more than 50 words giving the necessary details. You are the Cultural Secretary.",
      f"<b>NOTICE</b><br>{SCH}<br>18 November 2026<br><b>SCHOOL PICNIC</b><br>A one-day picnic to Jal Mahal will be held on 28 November 2026. Buses will leave at 8 a.m. from school. Students should carry lunch, a water bottle and a cap. Parents' consent slips must be submitted by 24 November.<br>Cultural Secretary<br>" + FN),
    N("You lost your pen in the school bus. Write a message in about 30 words for the bus conductor.",
      "<b>MESSAGE</b><br>18 November 2026<br>Dear Sir,<br>I lost a blue fountain pen in your bus (route no. 5) today. It has my initials. If found, please hand it over to the school office.<br>Thank you.<br>Karan, Class 7-B<br>" + FN)),
 OR(L("You are Mohit/Mohini. Write a letter to your grandmother in about 100 words telling her about your school's Annual Day.",
      "5, Bani Park<br>Jaipur<br>18 November 2026<br>Dear Dadi,<br>Pranam. I hope you are well. I want to tell you about our Annual Day, which was held last Saturday. I took part in a play and played the role of a king. Everyone clapped at the end. My class also won the prize for the best dance. I wish you had been there. Please come to us soon; we all miss you.<br>Your loving grandchild,<br>Mohit/Mohini<br>" + FL),
    L("Write a letter to the Principal in about 100 words requesting that a cricket coach be appointed. You are the Sports Captain.",
      "Mastermind Public School<br>Jaipur<br>18 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Request to appoint a cricket coach<br>Respected Sir/Madam,<br>Many students of our school wish to play cricket but do not have a trained coach. We request you to appoint a coach who can teach us the game properly. It will improve our fitness and help us win in inter-school matches. We shall be thankful.<br>Yours obediently,<br>Sports Captain<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'Discipline'.",
      "Discipline means following rules and obeying the right orders. It is important in every field of life. A disciplined student reaches school in time, completes homework and respects teachers. In armies and sports teams discipline wins battles and matches. Without it, there would be confusion everywhere. Discipline is learnt in childhood and is a habit that grows with practice. Every person should be disciplined. " + FA),
    A("Write a short story in about 80 words with the hints: A boy – always lies – shouts 'Tiger!' – villagers come – no tiger – real tiger – no one comes. Give a title.",
      "<b>The Boy Who Cried Tiger</b><br>A shepherd boy loved to play tricks. One day he cried, \"Tiger! Tiger!\" The villagers ran to help, but there was no tiger. They went back angry. He played the same trick again. One evening a real tiger came, and the boy screamed for help. This time nobody came, for they thought he was lying. He lost all his sheep.<br><i>Moral: Liars are not believed even when they speak the truth.</i><br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: By the time we arrived, the film ______ (start).", "had started."),
 g("Choose the correct pronoun: The girl lost ______ bag. (she / her / hers)", "her."),
 g("Fill in the blank with 'few' or 'little': There is ______ milk left in the pot.", "little."),
 g("Change into reported speech: He said, \"I am tired.\"", "He said that he was tired."),
 g("Form a noun from 'happy'.", "Happiness."),
 g("Fill in the blank with a preposition: The book is ______ the table.", "on."),
 g("Choose the correct option: Each of the players ______ a medal. (got / get)", "got."),
 g("Rewrite correctly: she dont know the answer", "She doesn't (does not) know the answer."),
])

SETS[8] = dict(
W=[
 OR(N("Your school has lost a school bag. Write a notice in not more than 50 words asking the finder to return it. You are the Head Boy/Head Girl.",
      f"<b>NOTICE</b><br>{SCH}<br>20 November 2026<br><b>LOST AND FOUND</b><br>A blue school bag with the name 'Aman Gupta, 7-C' was lost near the playground on 19 November. Whoever finds it is requested to return it to the school office.<br>Head Boy/Head Girl<br>" + FN),
    N("You are going to the dentist with your father and will miss tuition. Write a message in about 30 words for your tutor.",
      "<b>MESSAGE</b><br>20 November 2026, 3 p.m.<br>Dear Sir,<br>I have a dental appointment at 5 p.m. today and cannot attend tuition. Kindly excuse me. I will complete today's work by tomorrow.<br>Yours sincerely,<br>Pranav<br>" + FN)),
 OR(L("Write a letter to your friend in about 100 words congratulating him/her on winning the first prize in a painting competition.",
      "30, Mansarovar<br>Jaipur<br>20 November 2026<br>Dear Neeta,<br>I was very happy to hear that you won the first prize in the painting competition. Congratulations! Your painting of a village fair was beautiful, and you deserved it. You worked hard and now you have got the reward. I am proud to have a friend like you. Please send me a picture of your prize.<br>Yours sincerely,<br>Divya<br>" + FL),
    L("Write a letter to the Principal in about 100 words asking for a copy of your lost report card. You are Vijay/Vijaya of Class 7-A.",
      "Class 7-A<br>Mastermind Public School<br>Jaipur<br>20 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Request for a duplicate report card<br>Respected Sir/Madam,<br>I beg to state that I have lost my report card of the half-yearly examination. I need it for a scholarship form. Kindly issue me a duplicate copy and let me know the fee if any.<br>Yours obediently,<br>Vijay/Vijaya<br>Class 7-A, Roll No. 18<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'Trees'.",
      "Trees are our best friends. They give us fresh air, shade, fruits, flowers and wood. They absorb carbon dioxide and give out oxygen. Their roots hold the soil and prevent floods. Birds and animals live in them. Yet people cut trees recklessly for roads and buildings. We should plant more trees and protect those that stand. As the saying goes, a tree planted today is a gift to tomorrow. " + FA),
    A("Write a diary entry in about 80 words about your first day in Class 7.",
      "<b>Monday, 20 November 2026</b><br>9 p.m.<br>Dear Diary,<br>Today was my first day in Class 7. I felt a little nervous at first, but my class teacher Mrs. Rao welcomed us warmly. I found my seat next to my best friend. We got new books and a new time table. I like the Science lab very much. I think this year is going to be exciting.<br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: She has ______ (live) here for five years.", "lived."),
 g("Choose the correct article: ______ Ganga is a holy river. (A / An / The)", "The."),
 g("Choose the correct word: He is ______ than his brother. (clever / cleverer / cleverest)", "cleverer."),
 g("Change into reported speech: She said, \"I like mangoes.\"", "She said that she liked mangoes."),
 g("Form an adjective from 'danger'.", "Dangerous."),
 g("Fill in the blank with a preposition: He is interested ______ music.", "in."),
 g("Rearrange to form a sentence: to / she / school / walks / every day", "She walks to school every day."),
 g("Change into the passive voice: Mother cooked dinner.", "Dinner was cooked by Mother."),
])

SETS[9] = dict(
W=[
 OR(N("Your school is going to organise a Health Check-up Camp. Write a notice in not more than 50 words. You are the school captain.",
      f"<b>NOTICE</b><br>{SCH}<br>22 November 2026<br><b>HEALTH CHECK-UP CAMP</b><br>A free health check-up camp will be held in the school on 30 November 2026 from 9 a.m. to 1 p.m. Doctors from the City Hospital will check eyes, teeth and height and weight. All students must attend with their health cards.<br>School Captain<br>" + FN),
    N("Write an e-mail in about 40 words to your teacher, informing him/her that you will be absent on Monday due to a family function. Your e-mail ID is sana@mail.com; the teacher's ID is mrsmehta@school.com.",
      "<b>To:</b> mrsmehta@school.com<br><b>From:</b> sana@mail.com<br><b>Subject:</b> Leave for Monday<br>Respected Madam,<br>I shall not be able to attend school on Monday, 23 November, as I have to attend my cousin's wedding. Kindly grant me leave for the day.<br>Yours obediently,<br>Sana, Class 7-A<br>" + FN)),
 OR(L("Write a letter to your cousin in about 100 words describing a cricket match you watched.",
      "40, Tonk Road<br>Jaipur<br>22 November 2026<br>Dear Vivek,<br>Last Sunday I saw a thrilling cricket match between our school and Sunrise Public School. Our team batted first and scored 120 runs. Their batsmen played well, and the match reached the last over. Finally our bowler took the last wicket, and we won by two runs. Everyone cheered loudly. Wish you had been there to see it.<br>Yours lovingly,<br>Kunal<br>" + FL),
    L("Write a letter to the Principal in about 100 words requesting permission to start a school magazine. You are the Editor of the Class 7 wall magazine.",
      "Class 7-B<br>Mastermind Public School<br>Jaipur<br>22 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Request to start a school magazine<br>Respected Sir/Madam,<br>Our class has a wall magazine, which has been liked by everyone. Many students are interested in writing stories, poems and articles. We therefore request you to permit us to bring out a printed school magazine twice a year. Our English teacher has agreed to guide us.<br>Yours obediently,<br>Editor, Class 7 Wall Magazine<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'A Visit to a Railway Station'.",
      "Last Sunday I went to the railway station with my father to receive my uncle. The station was crowded with passengers and porters. Vendors sold tea, snacks and newspapers. A loud announcement said that the train was running late. At last the train arrived with a long whistle. Passengers rushed in and out. I saw my uncle and ran to greet him. It was an exciting experience. " + FA),
    A("Write a short story in about 80 words with the hints: A farmer – golden egg goose – greed – kills goose – nothing inside. Give a title.",
      "<b>The Goose and the Golden Eggs</b><br>A farmer had a goose that laid one golden egg every day. He became rich but wished for more. \"If I cut it open, I shall get all the eggs at once,\" he thought. He killed the goose, but found nothing inside. He lost both the goose and the daily egg.<br><i>Moral: Greed is a curse.</i><br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: Birds ______ (fly) in the sky.", "fly."),
 g("Choose the correct word: He drives very ______. (careful / carefully)", "carefully."),
 g("Fill in the blank with the correct form: I have just ______ (finish) my homework.", "finished."),
 g("Change into reported speech: Raj said, \"I will come tomorrow.\"", "Raj said that he would come the next day."),
 g("Write the plural of 'child'.", "Children."),
 g("Fill in the blank with a preposition: The teacher is angry ______ the students.", "with."),
 g("Combine using 'although': He was tired. He kept working.", "Although he was tired, he kept working."),
 g("Change into the interrogative: She is reading a novel.", "Is she reading a novel?"),
])

SETS[10] = dict(
W=[
 OR(N("Your school is going to start a Computer Club. Write a notice in not more than 50 words inviting students. You are the Head Boy/Head Girl.",
      f"<b>NOTICE</b><br>{SCH}<br>25 November 2026<br><b>COMPUTER CLUB</b><br>A Computer Club is starting in the school. Students of Classes 6–8 interested in learning coding and typing may join. Classes will be held on Wednesdays from 2 to 3 p.m. in the computer lab. Names should be given to Mr. Singh by 30 November.<br>Head Boy/Head Girl<br>" + FN),
    N("You are going out to play cricket and your mother is not at home. Write a message in about 30 words for her.",
      "<b>MESSAGE</b><br>25 November 2026, 5 p.m.<br>Dear Mummy,<br>I have gone to the park to play cricket with my friends. I shall return by 7 p.m. Milk is kept in the fridge. Please do not worry.<br>Aman<br>" + FN)),
 OR(L("Write a letter to your friend in about 100 words inviting him/her to your sister's wedding.",
      "12, Raja Park<br>Jaipur<br>25 November 2026<br>Dear Pankaj,<br>I am happy to inform you that my sister Reena's wedding will take place on 5 December 2026 at Hotel Orchid, Jaipur. We would like you and your parents to be with us on this happy occasion. Please come two days earlier so that we can enjoy together. All the family is eagerly waiting for you.<br>Yours sincerely,<br>Rahul<br>" + FL),
    L("Write a letter to the Principal in about 100 words complaining about the noise from a construction site near school. You are Pooja of Class 7.",
      "Class 7-C<br>Mastermind Public School<br>Jaipur<br>25 November 2026<br>The Principal<br>Mastermind Public School<br>Jaipur<br>Subject: Noise from the construction site<br>Respected Sir/Madam,<br>I wish to draw your attention to the constant noise from the construction work next to our school. It is difficult to hear the teacher in the classroom. I request you to contact the authorities so that heavy work may be done after school hours.<br>Yours obediently,<br>Pooja<br>Class 7-C<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'My Mother'.",
      "My mother is the most important person in my life. She wakes up early and works the whole day to look after the family. She cooks tasty food, helps me with my studies and tells me stories at night. She is strict when I am wrong and loving when I am sad. She taught me to be honest and to respect elders. I love her very much and I try never to hurt her. " + FA),
    A("Write a diary entry in about 80 words about a power cut that happened yesterday evening.",
      "<b>Wednesday, 25 November 2026</b><br>9 p.m.<br>Dear Diary,<br>Yesterday there was a power cut from six to nine in the evening. At first I felt bored and annoyed, but then Mother lit candles and we all sat together. Grandfather told us stories of his childhood. We played antakshari and ate dinner by candlelight. It was great fun. I realised that we spend too much time on screens and too little with family.<br>" + FA)),
],
G=[
 g("Fill in the blank with the correct form: Look! The baby ______ (cry).", "is crying."),
 g("Choose the correct word: There ______ many books on the shelf. (is / are)", "are."),
 g("Fill in the blank with 'a' or 'an': She wants to become ______ engineer.", "an."),
 g("Change into reported speech: Sita said, \"I can swim.\"", "Sita said that she could swim."),
 g("Write the opposite of 'increase'.", "Decrease."),
 g("Fill in the blank with a preposition: We should be kind ______ animals.", "to."),
 g("Change into the passive voice: The gardener waters the plants.", "The plants are watered by the gardener."),
 g("Join using 'so': It was raining. We stayed at home.", "It was raining, so we stayed at home."),
])
