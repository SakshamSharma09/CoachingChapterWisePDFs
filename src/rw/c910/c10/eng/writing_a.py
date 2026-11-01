"""Writing & Grammar sets 1–5 (original). Each set: W = [notice(3), letter(5) OR, paragraph(4) OR], G = 8 grammar items (1 mark each)."""
from eng_lib import Q, OR, mcq

def N(q, ans): return Q(q, ans, "3")
def L(q, ans): return Q(q, ans, "5")
def A(q, ans): return Q(q, ans, "4")
def g(q, ans): return Q(q, ans, "1")

SETS = {}

SETS[1] = dict(
W=[
 OR(N("Your school is organising a Science Exhibition. Write a notice in not more than 50 words, informing students of Classes 8–10 about the exhibition. Give all necessary details. You are Ravi/Ravina, the Secretary of the Science Club.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>SCIENCE EXHIBITION</b><br>The Science Club is organising a Science Exhibition on Saturday, 21 November 2026, from 10 a.m. to 1 p.m. in the school auditorium. Students of Classes 8 to 10 may display working models and charts. Interested students should give their names to the undersigned by 16 November.<br>Ravi/Ravina, Secretary, Science Club<br><i>(Format 1 · Content 1 · Language 1)</i>"),
    N("Your school is going to hold a Blood Donation Camp. Draft a notice in not more than 50 words, inviting students of Class 12 and staff to volunteer. You are the Head Boy/Head Girl.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>BLOOD DONATION CAMP</b><br>A Blood Donation Camp will be held in the school hall on 25 November 2026, from 9 a.m. to 2 p.m. Students of Class 12 (above 18 years) and staff willing to donate may register with the school nurse by 20 November.<br>Head Boy/Head Girl<br><i>(Format 1 · Content 1 · Language 1)</i>")),
 OR(L("You are Mohan/Mohini of 14, Gandhi Nagar, Jaipur. Write a letter to the Editor of a local daily, in about 120 words, complaining about the lack of street lighting in your locality and requesting the authorities to take action.",
      "14, Gandhi Nagar<br>Jaipur<br>10 November 2026<br>The Editor<br>The Daily Herald<br>Jaipur<br>Subject: Poor street lighting in Gandhi Nagar<br>Sir/Madam,<br>Through the columns of your newspaper, I wish to draw the attention of the municipal authorities to the poor street lighting in Gandhi Nagar. Most lamps on our main road have not worked for three weeks. After dark, women and children find it difficult to walk, and there have been cases of chain-snatching and accidents. Residents have complained several times, but no repair has been done. I request the authorities to repair or replace the lamps urgently and to arrange regular inspection. I hope this letter will bring a quick response.<br>Yours faithfully,<br>Mohan/Mohini<br><i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>"),
    L("You are Rohit/Rashmi. Write a letter to your friend, in about 120 words, describing how you spent your winter holidays in a hill station.",
      "22, Civil Lines<br>Jaipur<br>10 January 2027<br>Dear Arun,<br>I hope you are well. I am writing to tell you about my winter holidays, which I spent in Manali. We travelled by bus and reached there at sunrise. The mountains were covered with snow, and the air was crisp. I enjoyed walking in the pine forest, building a snowman, and sipping hot soup. We also went to the Hadimba temple and watched local people dancing. The best part was the toboggan ride. I returned with happy memories and a few photographs, which I shall show you when we meet. Do write to me about your holidays.<br>Yours affectionately,<br>Rohit/Rashmi<br><i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>")),
 OR(A("Write a paragraph in about 100 words on 'The Importance of Reading Newspapers'.",
      "Newspapers are windows to the world. Reading them daily keeps us informed about local, national and international events, and helps us develop an informed opinion. They improve vocabulary and language skills, especially when we read editorials. For students, newspapers are a source of general knowledge and current affairs, which are valuable for examinations. They also teach us to see an issue from different points of view. Moreover, they offer entertainment through sports pages, cartoons and puzzles. In this age of fast digital news, the printed newspaper still gives a reliable and balanced account. A habit of reading it every morning is therefore a good investment for the mind.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'Why Exercise Is Important for Students'.",
      "A healthy mind needs a healthy body, and regular exercise provides both. Students who exercise stay fit, sleep better and fall ill less often. Exercise releases chemicals in the brain which improve mood and reduce stress, so a student can concentrate longer. Team games teach discipline, cooperation and the spirit of sportsmanship. A short walk or yoga session each day can also improve posture, which suffers from long hours at the desk. Schools should therefore give games a regular place in the timetable, and parents should encourage children to play outdoors rather than spend all their free time before a screen.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form of the verb: She ______ (live) in Jaipur since 2015.", "has lived."),
 g("Choose the correct modal: You ______ wear a helmet while riding a motorcycle. (can / must / may)", "must."),
 g("Fill in the blank with a suitable determiner: There is ______ milk in the pot. (few / a little / many)", "a little."),
 g("Rewrite in reported speech: The teacher said to the students, \"Submit your notebooks tomorrow.\"", "The teacher told the students to submit their notebooks the next day."),
 g("Change into passive voice: The committee will announce the results tomorrow.", "The results will be announced by the committee tomorrow."),
 g("Join using 'who': I met a girl. She had won a gold medal.", "I met a girl who had won a gold medal."),
 g("Edit the sentence: He go to school by bus every day.", "He goes to school by bus every day."),
 g("Rearrange to form a meaningful sentence: the / is / library / on / the / floor / first", "The library is on the first floor."),
])

SETS[2] = dict(
W=[
 OR(N("Your school is going to hold an Inter-House Debate Competition. Write a notice in not more than 50 words giving all details. You are Neha/Nitin, the Cultural Secretary.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>12 November 2026<br><b>INTER-HOUSE DEBATE COMPETITION</b><br>An Inter-House Debate on 'Social Media: Boon or Bane?' will be held in the school auditorium on 28 November 2026 at 10 a.m. Each House may send two speakers from Classes 9–12. Names should be given to the undersigned by 20 November.<br>Neha/Nitin, Cultural Secretary<br><i>(Format 1 · Content 1 · Language 1)</i>"),
    N("Your school library has received a set of new books. Write a notice in not more than 50 words informing students about it. You are the Librarian.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>12 November 2026<br><b>NEW ARRIVALS IN THE LIBRARY</b><br>The library has received 200 new books, including novels, biographies and science magazines. Students may issue them from 16 November between 9 a.m. and 3 p.m. on school days. Each student may borrow two books for one week.<br>Librarian<br><i>(Format 1 · Content 1 · Language 1)</i>")),
 OR(L("You are Sachin/Sarika of 8, Subhash Marg, Kota. Write a letter to the Principal of your school, in about 120 words, requesting permission to attend a state-level badminton tournament for three days.",
      "8, Subhash Marg<br>Kota<br>12 November 2026<br>The Principal<br>Mastermind Public School<br>Kota<br>Subject: Request for leave for three days<br>Respected Sir/Madam,<br>I beg to state that I have been selected to represent our district in the State-Level Badminton Tournament to be held at Jaipur from 20 to 22 November 2026. I therefore request you to grant me leave for three days. I assure you that I shall complete the missed lessons and assignments with the help of my classmates and teachers. I shall be grateful for your kind permission.<br>Yours obediently,<br>Sachin/Sarika<br>Class 10-A, Roll No. 12<br><i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>"),
    L("You are Kiran/Karan. Write a letter to your younger brother/sister, in about 120 words, advising him/her to take studies seriously and to develop good habits.",
      "5, Lal Kothi<br>Jaipur<br>12 November 2026<br>My dear Anu,<br>I hope you are doing well. I was glad to read your last letter, but I was a little worried to learn that your marks have fallen. I know you can do better. Please make a timetable and follow it every day. Revise your lessons the same day and ask your teachers if you have doubts. Sleep early, avoid too much television and spend some time in the playground. Remember that regular effort is the key to success. I am sure you will improve soon.<br>Your loving brother/sister,<br>Kiran/Karan<br><i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>")),
 OR(A("Write a paragraph in about 100 words on 'Save Water, Save Life'.",
      "Water is the source of life, yet we often waste it carelessly. India faces serious scarcity as groundwater levels fall and rivers get polluted. We must therefore use water wisely. Leaking taps should be mended, and water used for washing vegetables can be used for plants. Rainwater harvesting can store water for dry months. Farmers should adopt drip irrigation. Industries must treat waste water before releasing it into rivers. Every drop saved today is a drop available for tomorrow. If each citizen does his part, we shall secure enough water for our children.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'The Advantages of Early Rising'.",
      "Early rising is a golden habit. The morning air is fresh and free from noise and dust, and a walk or yoga then makes the body strong. The mind is calm, so studies done in the morning are remembered better. A person who rises early has more time for work, breakfast and preparation, and does not have to hurry to school or office. Early risers are generally cheerful and punctual. Great men and women of the world have followed this habit. Therefore, every student should go to bed early and rise at dawn.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct tense: When I reached the station, the train ______ (leave).", "had left."),
 g("Choose the correct modal: ______ I borrow your pen? (Shall / May / Must)", "May."),
 g("Fill in the blank with the right article: She is ______ honest girl.", "an."),
 g("Rewrite in reported speech: He said, \"I am writing a letter.\"", "He said that he was writing a letter."),
 g("Change into active voice: The window was broken by the boys.", "The boys broke the window."),
 g("Join using 'although': He was tired. He went on working.", "Although he was tired, he went on working."),
 g("Find and correct the error: Each of the boys have finished the work.", "Each of the boys has finished the work."),
 g("Rearrange to form a meaningful sentence: has / the / begun / examination / week / this", "The examination has begun this week."),
])

SETS[3] = dict(
W=[
 OR(N("You have lost your school identity card. Write a notice in not more than 50 words for the school notice board. You are Preeti/Pratap of Class 10-B.",
      "<b>LOST</b><br>10 November 2026<br>I have lost my school identity card on 9 November 2026 between the school gate and the library. Whoever finds it is requested to hand it over to the Principal's office or contact the undersigned.<br>Preeti/Pratap, Class 10-B"),
    N("Your school is going to organise a tree plantation drive. Write a notice in not more than 50 words. You are the Secretary of the Eco Club.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>TREE PLANTATION DRIVE</b><br>The Eco Club will hold a tree plantation drive on 22 November 2026 at 8 a.m. in the school campus. Interested students are requested to assemble at the main gate and bring a spade or a water can. Saplings will be provided.<br>Secretary, Eco Club")),
 OR(L("You are Deepak/Divya, a resident of 7, Shastri Nagar, Ajmer. Write a letter to the Municipal Commissioner, in about 120 words, complaining about irregular garbage collection in your area.",
      "7, Shastri Nagar<br>Ajmer<br>10 November 2026<br>The Municipal Commissioner<br>Ajmer Municipal Corporation<br>Ajmer<br>Subject: Irregular garbage collection<br>Sir,<br>I wish to bring to your notice that garbage is not collected regularly from Shastri Nagar. For over two weeks heaps of waste have been lying on the roadside, giving off a foul smell and attracting stray animals and flies. This is a serious health risk, especially for children. Several complaints have been made to the local office, but there has been no action. I request you to arrange daily collection and to place more bins in the locality at the earliest.<br>Yours faithfully,<br>Deepak/Divya"),
    L("You are Sonal/Sandeep. Write a letter to a friend, in about 120 words, congratulating him/her on winning a prize in an essay competition.",
      "12, Civil Lines<br>Ajmer<br>10 November 2026<br>Dear Tanvi,<br>I was delighted to learn that you won the first prize in the inter-school essay competition. Hearty congratulations! I know how hard you worked and how many evenings you spent in the library. Your essay on 'Our Rivers' was so thoughtful that it deserved the first prize. Your parents and teachers must be very proud. I am sure this success will encourage you to write even more. Please accept my best wishes and give my regards to your family. Let us celebrate when we meet.<br>Yours affectionately,<br>Sonal/Sandeep")),
 OR(A("Write a paragraph in about 100 words on 'The Role of Teachers in Society'.",
      "Teachers are the builders of the nation. They shape the minds and character of young people and prepare them to face life. A good teacher not only gives knowledge but also teaches values such as honesty, discipline and respect. In difficult times, a teacher is a guide and a friend. Teachers also encourage curiosity and creativity. Society should honour and support teachers by giving them respect and good facilities. It is no exaggeration to say that the quality of a nation depends on the quality of its teachers.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'Road Safety'.",
      "Road accidents claim thousands of lives every year in India. Most of them are caused by carelessness. Drivers should obey speed limits and traffic signals. Two-wheeler riders should always wear helmets and car passengers should use seat belts. Pedestrians must use zebra crossings and footpaths. Using a mobile phone while driving is dangerous. The government should improve roads and enforce rules strictly. Schools must teach road safety to children. With discipline and awareness, we can reduce accidents and make our roads safe.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form: By next June, I ______ (complete) my course.", "will have completed."),
 g("Choose the correct modal: You ______ obey your elders. (ought to / may / could)", "ought to."),
 g("Fill in the blank with the correct preposition: He has been living here ______ 2018.", "since."),
 g("Rewrite in reported speech: She said to me, \"Where do you live?\"", "She asked me where I lived."),
 g("Change into passive voice: Who wrote this novel?", "By whom was this novel written?"),
 g("Join using 'so that': He worked hard. He wanted to pass.", "He worked hard so that he might pass."),
 g("Find and correct the error: She does not know nothing about it.", "She does not know anything about it."),
 g("Rearrange to form a meaningful sentence: is / in / honesty / best / the / policy", "Honesty is the best policy."),
])

SETS[4] = dict(
W=[
 OR(N("The school is organising an annual sports day. Write a notice in not more than 50 words informing students about it. You are the Sports Captain.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>ANNUAL SPORTS DAY</b><br>The Annual Sports Day will be held on 5 December 2026 from 8 a.m. in the school ground. Students interested in participating in athletics, relay or team games should give their names to their class teachers by 25 November.<br>Sports Captain"),
    N("Your school wants to start a Reading Club. Write a notice in not more than 50 words inviting students to join. You are the Head of the English Department.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>READING CLUB</b><br>A Reading Club is being started for students of Classes 8–12. It will meet every Friday at 2 p.m. in the library. Students who love reading should give their names to Mrs Sharma by 20 November.<br>Head, English Department")),
 OR(L("You are Hemant/Harsha of 15, Vidya Nagar, Bikaner. Write a letter to the Principal of a college, in about 120 words, enquiring about the courses, fees and hostel facilities.",
      "15, Vidya Nagar<br>Bikaner<br>10 November 2026<br>The Principal<br>Government College<br>Jaipur<br>Subject: Enquiry about courses, fees and hostel<br>Sir/Madam,<br>I am a student of Class 12 and wish to take admission in your college. Kindly inform me about the courses offered in the Science stream, the eligibility criteria and the last date for application. I would also like to know the fee structure and whether hostel accommodation is available for outstation students. I shall be grateful if you could also send me a prospectus and the admission form.<br>Yours faithfully,<br>Hemant/Harsha"),
    L("You are Reena/Ravi. Write a letter to your friend, in about 120 words, inviting him/her to your sister's wedding.",
      "20, Model Town<br>Jaipur<br>10 November 2026<br>Dear Sneha,<br>I am happy to inform you that my sister Aarti's wedding will be held on 5 December 2026 at the Royal Garden, Jaipur. The ceremonies will begin at 6 p.m. My parents and I would be delighted if you could come with your family and stay with us for two days. Your presence will make the occasion more joyful. Please let me know your date of arrival so that I can receive you at the station.<br>Yours affectionately,<br>Reena/Ravi")),
 OR(A("Write a paragraph in about 100 words on 'The Uses of the Internet'.",
      "The Internet has changed our lives. It brings information from every corner of the world within seconds. Students use it to find notes and to join online classes. People send messages, make video calls and pay bills without leaving home. It offers entertainment through music, films and games. Businesses use it to reach customers. But it must be used with care, as it also spreads false news and can lead to addiction. If used wisely, the Internet is a powerful tool for learning and progress.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'My Favourite Festival'.",
      "My favourite festival is Diwali. It is celebrated with great joy in our home. We clean the house, decorate it with rangoli and light diyas. On the day, we worship Goddess Lakshmi and share sweets with neighbours. The sky glows with fireworks, but we try to use fewer crackers to avoid pollution. The festival brings the family together and spreads the message that light always conquers darkness. It also teaches us to be generous and to forgive.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct tense: The sun ______ (rise) in the east.", "rises."),
 g("Choose the correct modal: He ______ be at home; his light is on. (must / ought / dare)", "must."),
 g("Fill in the blank with a suitable determiner: ______ student of the class has passed. (Every / All / Many)", "Every."),
 g("Rewrite in reported speech: He said, \"I shall go tomorrow.\"", "He said that he would go the next day."),
 g("Change into passive voice: They are repairing the road.", "The road is being repaired by them."),
 g("Join using 'which': I bought a book. It was very interesting.", "I bought a book which was very interesting."),
 g("Find and correct the error: Neither of the answers were correct.", "Neither of the answers was correct."),
 g("Rearrange to form a meaningful sentence: reading / of / improves / vocabulary / habit / the", "The habit of reading improves vocabulary."),
])

SETS[5] = dict(
W=[
 OR(N("Your school is going to conduct a Career Counselling Session. Write a notice in not more than 50 words. You are the school Counsellor.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>CAREER COUNSELLING SESSION</b><br>A career counselling session for Classes 10 and 12 will be held on 24 November 2026 at 11 a.m. in the seminar hall. A career expert will speak on courses and opportunities. Students should bring questions.<br>School Counsellor"),
    N("The school canteen will remain closed for repairs. Write a notice in not more than 50 words. You are the Vice Principal.",
      "<b>NOTICE</b><br>Mastermind Public School, Jaipur<br>10 November 2026<br><b>CANTEEN CLOSED</b><br>The school canteen will remain closed from 16 to 20 November 2026 for repairs. Students are requested to bring their own tiffin and water. Regular services will resume on 21 November.<br>Vice Principal")),
 OR(L("You are Vimal/Vimla of 3, Station Road, Kota. Write a letter to the Editor of a newspaper, in about 120 words, on the increasing noise pollution in your city.",
      "3, Station Road<br>Kota<br>10 November 2026<br>The Editor<br>The Rajasthan Times<br>Kota<br>Subject: Noise pollution<br>Sir,<br>Through your newspaper I wish to draw the attention of the authorities to the rising noise pollution in our city. Loud horns, DJ systems and loudspeakers disturb students, patients and the elderly. Public examinations make it worse. I request the authorities to enforce the laws on noise limits, to ban pressure horns and to fix silent zones near schools and hospitals. Citizens too should cooperate. I hope action will be taken soon.<br>Yours faithfully,<br>Vimal/Vimla"),
    L("You are Gaurav/Gauri. Write a letter to your cousin, in about 120 words, thanking him/her for a gift sent on your birthday.",
      "9, Ashok Vihar<br>Jaipur<br>10 November 2026<br>Dear Mohit,<br>Thank you very much for the beautiful wristwatch you sent me on my birthday. It was a wonderful surprise, and I loved the design. I have been wearing it every day, and my friends admire it. It will also help me to be punctual! My birthday was a happy one, and your gift made it even better. I hope you will visit us in the winter holidays. Give my regards to uncle and aunt.<br>Yours affectionately,<br>Gaurav/Gauri")),
 OR(A("Write a paragraph in about 100 words on 'The Value of Punctuality'.",
      "Punctuality means doing things at the right time. A punctual person is respected and trusted. Time lost is never regained, and a student who finishes tasks on time has leisure for sports and hobbies. Punctuality also reduces stress, as one need not hurry at the last minute. In business and public life, being late can cause loss and annoyance to others. Great persons such as Mahatma Gandhi were extremely punctual. We should therefore make a habit of keeping time from childhood.<br><i>(Content 2 · Organisation 1 · Language 1)</i>"),
    A("Write a paragraph in about 100 words on 'The Importance of a Balanced Diet'.",
      "A balanced diet contains the right amounts of carbohydrates, proteins, fats, vitamins and minerals. It gives energy, builds the body and fights disease. Fruits, vegetables, pulses, milk and cereals should form a part of the daily meal. Junk food, which has too much oil and sugar, causes obesity and tiredness. Drinking enough water is equally important. Students, who need energy to study and play, should avoid skipping breakfast. A healthy diet today is the foundation of a healthy life tomorrow.<br><i>(Content 2 · Organisation 1 · Language 1)</i>")),
],
G=[
 g("Fill in the blank with the correct form: He ______ (not/come) yesterday.", "did not come."),
 g("Choose the correct modal: Children ______ not play with fire. (should / can / may be)", "should."),
 g("Fill in the blank with the right article: He is ______ European.", "a."),
 g("Rewrite in reported speech: She said, \"I have finished my work.\"", "She said that she had finished her work."),
 g("Change into passive voice: Someone has stolen my bag.", "My bag has been stolen (by someone)."),
 g("Join using 'who': The man is my uncle. He is standing at the gate.", "The man who is standing at the gate is my uncle."),
 g("Find and correct the error: He is one of the best player in the team.", "He is one of the best players in the team."),
 g("Rearrange to form a meaningful sentence: taught / English / Mr Mehta / us / last year", "Mr Mehta taught us English last year."),
])
