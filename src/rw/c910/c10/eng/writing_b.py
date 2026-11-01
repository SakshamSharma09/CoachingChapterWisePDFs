"""Writing & Grammar sets 6–10 (original)."""
from eng_lib import Q, OR

def N(q, ans): return Q(q, ans, "3")
def L(q, ans): return Q(q, ans, "5")
def A(q, ans): return Q(q, ans, "4")
def g(q, ans): return Q(q, ans, "1")

SETS = {}

SETS[6] = dict(
W=[
 OR(N("Your school is organising a Fancy Dress Competition for the primary section. Write a notice in not more than 50 words. You are the Cultural Secretary.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>FANCY DRESS COMPETITION</b><br>A Fancy Dress Competition for Classes 1–5 will be held on 27 November 2026 at 10 a.m. in the school auditorium. The theme is 'Heroes of India'. Parents are requested to send names to class teachers by 20 November.<br>Cultural Secretary"),
    N("Your school wants to sell old textbooks at a book exchange. Write a notice in not more than 50 words inviting students to participate. You are the Secretary of the Student Council.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>BOOK EXCHANGE</b><br>The Student Council will hold a Book Exchange on 30 November 2026, from 11 a.m. to 1 p.m., in the library hall. Students may bring old textbooks in good condition and exchange them with others. No money will be charged.<br>Secretary, Student Council")),
 OR(L("You are Tarun/Tanya of 18, Moti Doongri Road, Jaipur. Write a letter to the Station Master, in about 120 words, complaining about the dirty condition of the platforms and waiting room.",
      "18, Moti Doongri Road<br>Jaipur<br>10 November 2026<br>The Station Master<br>Jaipur Railway Station<br>Jaipur<br>Subject: Unclean platforms and waiting room<br>Sir,<br>I travel from your station almost every week and am sorry to report that the platforms and waiting room are very dirty. Dustbins overflow, the floor is stained and the toilets are not cleaned regularly. Passengers, especially women and the elderly, face great inconvenience. I request you to arrange for daily cleaning, to provide more dustbins and to appoint a supervisor for the work.<br>Yours faithfully,<br>Tarun/Tanya"),
    L("You are Pooja/Pankaj. Write a letter to your friend, in about 120 words, advising him/her to give up the habit of watching too much television.",
      "11, Gandhi Path<br>Jaipur<br>10 November 2026<br>Dear Kunal,<br>I was sorry to learn that you spend most of your evenings before the television. This is affecting your studies and your health. Your eyes will weaken, and you will soon become lazy. Instead, take a walk after school, play with your friends and read a good book. Watch only one hour of informative programmes. I am sure you will feel more active and cheerful. Do think about my advice, and write to me soon.<br>Yours affectionately,<br>Pooja/Pankaj")),
 OR(A("Write a paragraph in about 100 words on 'The Importance of Trees'.",
      "Trees are the lungs of the earth. They give us oxygen and absorb carbon dioxide. Their roots hold the soil and prevent floods and erosion. Trees provide food, fuel, timber and medicine. They give shade, attract rain and keep the temperature low. Birds and animals make their homes in them. Yet we cut trees thoughtlessly for roads and buildings. We must plant more trees and protect existing ones. A single tree planted today will serve many generations.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'Discipline in Student Life'.",
      "Discipline is the key to success in student life. A disciplined student gets up early, plans his day and does his work on time. He obeys his teachers and respects elders. Discipline teaches self-control and responsibility. It helps in games, studies and later in careers. Students who lack it waste time and suffer failures. Schools should therefore make discipline a daily habit through assemblies, games and group activities.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form: We ______ (watch) a film when the guests arrived.", "were watching."),
 g("Choose the correct modal: You ______ not tell a lie. (should / can / might)", "should."),
 g("Fill in the blank with the correct determiner: I have ______ friends in this city. (a few / a little / much)", "a few."),
 g("Rewrite in reported speech: He said to her, \"Will you help me?\"", "He asked her if she would help him."),
 g("Change into passive voice: The teacher is explaining the lesson.", "The lesson is being explained by the teacher."),
 g("Join using 'because': He was late. The bus broke down.", "He was late because the bus broke down."),
 g("Find and correct the error: The news are good.", "The news is good."),
 g("Rearrange to form a meaningful sentence: great / is / a / virtue / patience", "Patience is a great virtue."),
])

SETS[7] = dict(
W=[
 OR(N("The school is organising an Educational Trip to Delhi. Write a notice in not more than 50 words. You are the Class Teacher of Class 10.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>EDUCATIONAL TRIP</b><br>An educational trip to Delhi is being organised for Class 10 on 5 December 2026. Students will visit the National Museum and the Science Centre. Fee: ₹ 500. Students interested should submit the fee and parent's consent to the Class Teacher by 28 November.<br>Class Teacher"),
    N("A school vehicle bus will change its route next week. Write a notice in not more than 50 words informing students and parents. You are the Transport In-charge.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>CHANGE IN BUS ROUTE</b><br>Bus No. 4 will not go via Station Road from 16 November 2026 because of road work. It will take the Ring Road instead and pick students from Gandhi Chowk at the usual time. Parents are requested to note this change.<br>Transport In-charge")),
 OR(L("You are Amit/Amita of 6, Ratanada, Jodhpur. Write a letter to the Principal, in about 120 words, requesting the school to arrange extra classes in Mathematics for weak students.",
      "6, Ratanada<br>Jodhpur<br>10 November 2026<br>The Principal<br>Mastermind Public School<br>Jodhpur<br>Subject: Request for extra Mathematics classes<br>Respected Sir/Madam,<br>I am a student of Class 10-B. Many of us find Mathematics difficult because the syllabus is long and class time is short. With the board examination approaching, we need more practice and individual attention. I request you to arrange extra classes in the afternoon for weaker students. We shall be thankful to you for this kind help.<br>Yours obediently,<br>Amit/Amita<br>Class 10-B"),
    L("You are Seema/Sameer. Write a letter to a friend, in about 120 words, describing a fair that you visited recently.",
      "15, Sardarpura<br>Jodhpur<br>10 November 2026<br>Dear Neeraj,<br>Last Sunday I went with my family to the Pushkar Fair, and I want to tell you about it. The fair was crowded and colourful. There were camels, horses and cattle in hundreds. I rode a giant wheel and tasted local sweets. Folk dancers entertained the crowd with songs and music. The best part was the sunset over the sand dunes. I bought a few souvenirs. I wish you had been with me. Do come next year.<br>Yours affectionately,<br>Seema/Sameer")),
 OR(A("Write a paragraph in about 100 words on 'My Aim in Life'.",
      "My aim in life is to become a doctor. I have seen how a doctor can save lives and help the poor. I want to serve people living in villages where medical help is hard to get. To achieve this, I study hard, especially science subjects, and I read about the human body. I also help my family when anyone is ill. I know the way is long, but with hard work and honest effort, I hope to realise my dream.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'The Evils of Plastic'.",
      "Plastic has become a threat to the environment. It does not decay and remains in the soil for hundreds of years. Plastic bags choke drains and cause floods. Animals, including cows and fish, swallow plastic and die. Burning it releases poisonous gases. We should avoid single-use plastic, carry cloth bags, recycle bottles and encourage the use of alternatives. Government and citizens must work together to protect the earth.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form: The train ______ (already/leave) before we reached.", "had already left."),
 g("Choose the correct modal: You ______ speak softly in the library. (must / can / will)", "must."),
 g("Fill in the blank with the correct preposition: She is good ______ music.", "at."),
 g("Rewrite in reported speech: The boy said, \"I have lost my pen.\"", "The boy said that he had lost his pen."),
 g("Change into passive voice: The police arrested the thief.", "The thief was arrested by the police."),
 g("Join using 'if': Work hard. You will succeed.", "If you work hard, you will succeed."),
 g("Find and correct the error: She said me that she was ill.", "She told me that she was ill."),
 g("Rearrange to form a meaningful sentence: early / the / bird / worm / catches / the", "The early bird catches the worm."),
])

SETS[8] = dict(
W=[
 OR(N("Your school wants to start a Yoga class for students. Write a notice in not more than 50 words. You are the Physical Education Teacher.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>YOGA CLASSES</b><br>Yoga classes for students of Classes 6–12 will begin from 16 November 2026. They will be held every morning from 7 to 8 a.m. in the school ground. Interested students should give their names to the undersigned by 14 November.<br>PE Teacher"),
    N("You have found a wristwatch in the school corridor. Write a notice in not more than 50 words. You are Yash/Yamini of Class 10.",
      "<b>FOUND</b><br>10 November 2026<br>A wristwatch has been found in the first-floor corridor of the school on 9 November. The owner may collect it from the undersigned after giving its description.<br>Yash/Yamini, Class 10")),
 OR(L("You are Raman/Ramya of 21, Shiv Colony, Udaipur. Write a letter to the Manager of a bookshop, in about 120 words, placing an order for some books.",
      "21, Shiv Colony<br>Udaipur<br>10 November 2026<br>The Manager<br>Gyan Book Depot<br>Udaipur<br>Subject: Order for books<br>Sir,<br>Kindly send me by VPP the following books: (1) Oxford English Dictionary — 1 copy; (2) Class 10 Mathematics Guide — 2 copies; (3) Science Practice Papers — 1 copy. Please send them within a week. Discount as admissible may be allowed. I shall pay the amount on delivery.<br>Yours faithfully,<br>Raman/Ramya"),
    L("You are Lata/Lalit. Write a letter to your friend, in about 120 words, inviting him/her to spend the summer vacation with you.",
      "10, Jawahar Nagar<br>Udaipur<br>10 April 2027<br>Dear Sunita,<br>I hope you are doing well. The examinations will be over next week, and I am planning to spend the vacation at home. I request you to come and stay with me for a fortnight. We shall go boating on the lake and visit the old fort. Mother is also eager to meet you. I am sure we shall have a wonderful time. Please inform me of your arrival date.<br>Yours affectionately,<br>Lata/Lalit")),
 OR(A("Write a paragraph in about 100 words on 'The Benefits of Learning a Second Language'.",
      "Learning a second language opens new doors. It improves memory and thinking skills, and helps us understand other cultures. A person who knows more than one language has better job opportunities and can travel easily. Language also gives access to literature and films from other lands. In a country like India, knowing a regional language and English helps one to communicate widely. So students should enjoy learning languages.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'The Use of Mobile Phones in Schools'.",
      "Mobile phones have both uses and dangers in schools. They help students to access information and reach parents in an emergency. But they distract students in class and can be used for cheating or bullying. Many schools therefore ban them in classrooms. A balanced approach is best: phones may be used for learning under the teacher's supervision, and kept away at other times. Students must learn to use them responsibly.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form: She ______ (sing) since morning.", "has been singing."),
 g("Choose the correct modal: The doctor said that I ______ rest for a week. (should / can / might)", "should."),
 g("Fill in the blank with the right article: He is ______ best player of the team.", "the."),
 g("Rewrite in reported speech: The teacher said, \"The earth moves round the sun.\"", "The teacher said that the earth moves round the sun."),
 g("Change into passive voice: He will write a letter.", "A letter will be written by him."),
 g("Join using 'when': I reached home. It started raining.", "When I reached home, it started raining."),
 g("Find and correct the error: He is senior than me.", "He is senior to me."),
 g("Rearrange to form a meaningful sentence: the / sun / sets / west / in / the", "The sun sets in the west."),
])

SETS[9] = dict(
W=[
 OR(N("Your school is organising an Inter-School Quiz. Write a notice in not more than 50 words. You are the Convenor of the Quiz Club.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>INTER-SCHOOL QUIZ</b><br>The Quiz Club is organising an Inter-School General Knowledge Quiz on 29 November 2026 at 10 a.m. in the auditorium. Teams of three from Classes 9–12 may take part. Names to be given to the Convenor by 22 November.<br>Convenor, Quiz Club"),
    N("Your school is closing for winter vacation. Write a notice in not more than 50 words informing students. You are the Principal's Secretary.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>WINTER VACATION</b><br>The school will remain closed for winter vacation from 25 December 2026 to 5 January 2027. Classes will reopen on 6 January 2027. Students are advised to complete the holiday homework.<br>Principal's Secretary")),
 OR(L("You are Naveen/Navita of 9, Adarsh Nagar, Alwar. Write a letter to the Principal, in about 120 words, requesting a transfer certificate.",
      "9, Adarsh Nagar<br>Alwar<br>10 November 2026<br>The Principal<br>Mastermind Public School<br>Alwar<br>Subject: Request for Transfer Certificate<br>Respected Sir/Madam,<br>I am a student of Class 10-A. My father has been transferred to Jaipur and our family is moving there next week. I request you to issue my Transfer Certificate and the report card so that I can take admission in a new school. I shall be thankful.<br>Yours obediently,<br>Naveen/Navita<br>Class 10-A, Roll No. 15"),
    L("You are Madhu/Manoj. Write a letter to your uncle, in about 120 words, thanking him for his hospitality during your stay.",
      "4, Subhash Nagar<br>Alwar<br>10 November 2026<br>Dear Uncle,<br>I reached home safely yesterday. I thank you and aunt for the love and care I received during my stay. The days passed like a dream. I enjoyed the trip to the fort and the dinner at the garden restaurant. Your guidance about my studies will help me a lot. Please give my love to Ritu and Rahul. I hope you will visit us soon.<br>Yours affectionately,<br>Madhu/Manoj")),
 OR(A("Write a paragraph in about 100 words on 'A Visit to a Historical Place'.",
      "Last month I visited the Amer Fort near Jaipur. The fort stands on a hill and its red sandstone walls look magnificent. We rode an elephant up to the entrance and saw the Sheesh Mahal, where tiny mirrors sparkled on the walls. The guide told us stories of the Rajput kings. I admired the carvings and the huge gardens. It was a thrilling and educational visit.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'Cleanliness Drive in the City'.",
      "Cleanliness is a sign of civilised society. In our city, garbage heaps and plastic waste are common sights. The municipal corporation should arrange daily collection, place bins at all corners and fine those who litter. Citizens should keep their surroundings clean and avoid throwing waste on roads. Schools can start cleanliness campaigns. If everyone cooperates, our city can become clean and healthy.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form: I ______ (meet) him tomorrow.", "shall meet / will meet."),
 g("Choose the correct modal: ______ you help me with this bag, please? (Could / Must / Ought)", "Could."),
 g("Fill in the blank with the correct determiner: ______ of the two boys is guilty. (Either / Any / All)", "Either."),
 g("Rewrite in reported speech: She said, \"I was reading a book.\"", "She said that she had been reading a book."),
 g("Change into passive voice: Have you finished the work?", "Has the work been finished by you?"),
 g("Join using 'unless': Work hard. You will fail.", "Unless you work hard, you will fail."),
 g("Find and correct the error: I have seen him yesterday.", "I saw him yesterday."),
 g("Rearrange to form a meaningful sentence: a / is / wealth / health / real", "Health is real wealth."),
])

SETS[10] = dict(
W=[
 OR(N("Your school is organising a Cleanliness Awareness Rally. Write a notice in not more than 50 words. You are the Head of the Scouts and Guides Unit.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>CLEANLINESS AWARENESS RALLY</b><br>A rally to spread awareness of cleanliness will be taken out on 2 December 2026 at 7 a.m. from the school gate through nearby colonies. Scouts, Guides and interested students of Classes 7–10 should reach school by 6.45 a.m. in uniform.<br>Head, Scouts and Guides"),
    N("The annual day rehearsals will be held after school. Write a notice in not more than 50 words informing participants. You are the Cultural In-charge.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>ANNUAL DAY REHEARSALS</b><br>Rehearsals for the Annual Day will be held from 2 to 4 p.m. every day from 16 to 27 November 2026 in the auditorium. All participants must attend regularly and bring their costumes and props on 26 November.<br>Cultural In-charge")),
 OR(L("You are Jatin/Juhi of 3, Bapu Nagar, Jaipur. Write a letter to the Editor, in about 120 words, on the problem of stray animals on city roads.",
      "3, Bapu Nagar<br>Jaipur<br>10 November 2026<br>The Editor<br>The Pink City Times<br>Jaipur<br>Subject: Stray animals on city roads<br>Sir,<br>Through your newspaper I wish to raise the problem of stray cattle and dogs on the roads of our city. They roam in large numbers, block traffic and cause accidents. Children and the elderly are in danger from dogs. I request the municipal authorities to set up shelters, vaccinate the animals and fine those who leave cattle on the road. I hope action will be taken soon.<br>Yours faithfully,<br>Jatin/Juhi"),
    L("You are Meenu/Mohan. Write a letter to your friend, in about 120 words, telling him/her about your plans after Class 10.",
      "12, Shastri Nagar<br>Jaipur<br>10 November 2026<br>Dear Kavita,<br>How are you? Our board examinations are near, and everyone is asking what we shall do after Class 10. I have decided to take the science stream, as I wish to become an engineer. I have talked to my teachers and parents, and they have encouraged me. I shall also join a coaching class. What about you? Do write soon and tell me your plan.<br>Yours affectionately,<br>Meenu/Mohan")),
 OR(A("Write a paragraph in about 100 words on 'A Rainy Day'.",
      "It was a rainy day last Sunday. Dark clouds covered the sky, and a cool breeze blew. Soon heavy rain started. Water filled the streets, and children played in puddles. I sat by my window with a cup of tea and watched the trees swaying. The air smelled of wet earth. After some time the rain stopped, and a rainbow appeared. It was a refreshing and joyful day.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'Honesty Is the Best Policy'.",
      "Honesty means speaking the truth and being fair in all dealings. An honest person is trusted by all and sleeps in peace. Dishonesty may bring some quick gain but it leads to shame and loss. Many great persons became great because of their honesty. Children should be taught to value it from the beginning. Truly, honesty is the best policy.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form: Look! The baby ______ (sleep).", "is sleeping."),
 g("Choose the correct modal: It ______ rain today; take an umbrella. (might / must / shall)", "might."),
 g("Fill in the blank with the correct preposition: He was angry ______ me.", "with."),
 g("Rewrite in reported speech: She said to him, \"Please help me.\"", "She requested him to help her."),
 g("Change into passive voice: The cat killed the rat.", "The rat was killed by the cat."),
 g("Join using 'that': He is so weak. He cannot walk.", "He is so weak that he cannot walk."),
 g("Find and correct the error: Mathematics are my favourite subject.", "Mathematics is my favourite subject."),
 g("Rearrange to form a meaningful sentence: country / love / our / we / dearly", "We love our country dearly."),
])
