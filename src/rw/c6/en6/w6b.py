"""Class 6 Writing & Grammar sets 6-10 (original)."""
from en6.whelp import *
SETS = {}

SETS[6] = dict(
W=[
 OR(N("Your school will hold a Science Exhibition. Write a notice in about 40 words inviting students to take part. You are the Science Teacher, Mr Joshi.",
      NOT("8 November 2026", "SCIENCE EXHIBITION", "A Science Exhibition will be held on 20 November 2026 in the school hall from 10 a.m. to 1 p.m. Students of Classes 6–8 may display working models or charts. Names should be given to Mr Joshi by 15 November.", "Mr Joshi, Science Teacher")),
    N("Your mother has gone to the temple and your aunt has come to meet her. Write a message in about 30 words for her. You are Pooja.",
      MSG("8 November 2026", "Mummy", "Mausi came to meet you at four o'clock. She waited for half an hour and has gone home. She will call you tonight. I gave her tea and biscuits.", "Pooja"))),
 OR(L("Write a letter to your friend in about 80 words describing the Republic Day function in your school.",
      LET("3, Tilak Nagar, Jaipur", "8 November 2026", "Kunal", "How are you? Our school celebrated Republic Day with great joy. The Principal hoisted the national flag and we sang the national anthem. Many students gave patriotic songs and speeches. I took part in a march-past. We were given laddoos at the end. I felt very proud of our country. Do tell me how you celebrated the day.", "Sameer")),
    L("Write an email to your friend in about 80 words inviting her to your birthday party.",
      EML("anita@example.com", "Birthday Party", "I am going to turn twelve on 20 November. We are having a small party at my house at 5 p.m. There will be games, music and cake. Many of our school friends will come. Please do come and bring your sister along. My mother has made your favourite pasta. I will be waiting for you.", "Nidhi"))),
 OR(A("Write a paragraph in about 80 words on 'Importance of Games'.",
      PAR("Importance of Games", "Games are as important as studies. They keep us fit and healthy. Playing outdoors in fresh air makes us strong and cheerful. Games teach us teamwork, discipline and how to accept defeat. A child who plays regularly sleeps well and studies better. Cricket, football and hockey are popular games. Hence, we should give some time to play every day.")),
    A("Write a diary entry in about 80 words about your first day on the school sports team.",
      DIA("Monday, 9 November 2026", "Today was my first day in the school football team. Our coach, Mr Singh, made us run three rounds and then taught us how to pass the ball. I was nervous but my teammates were friendly. I scored one goal in the practice match. My legs are aching, but I feel proud. I will practise every day.")),
 ),
],
G=[
 g("Fill in the blank with the correct tense: She ______ (write) a letter now.", "is writing."),
 g("Choose the correct article: There is ______ umbrella in the corner. (a / an / the)", "an."),
 g("Write the plural of: wife, baby, potato.", "wives, babies, potatoes."),
 g("Fill in the blank with a preposition: He has been ill ______ Monday.", "since."),
 g("Give the opposite of: ‘always’, ‘north’.", "never; south."),
 g("Change into the passive voice: Ravi wrote a poem.", "A poem was written by Ravi."),
 g("Choose the correct word: (Their / There) house is near the park.", "Their."),
 g("Add punctuation: where are you going asked mother", "“Where are you going?” asked Mother."),
])

SETS[7] = dict(
W=[
 OR(N("Your school is going to organise a Yoga Camp. Write a notice in about 40 words. You are the Sports Teacher.",
      NOT("9 November 2026", "YOGA CAMP", "A Yoga Camp will be held from 16 to 20 November 2026, 7 to 8 a.m., on the school ground. Students of Classes 6–8 may join. Wear comfortable clothes and bring a yoga mat.", "Sports Teacher")),
    N("You have found a pair of spectacles in the classroom. Write a message in about 30 words to your classmates. You are Gaurav.",
      MSG("9 November 2026", "friends", "I found a pair of spectacles near the last bench in our class today. The owner may collect them from me tomorrow in recess. Please give the proof of ownership.", "Gaurav"))),
 OR(L("Write a letter to your younger brother in about 80 words advising him to take care of his health.",
      LETF("11, Bani Park, Jaipur", "9 November 2026", "Aman", "I have heard that you are not eating healthy food. Junk food may taste good but it is not good for your health. You should eat fruits, vegetables and pulses. Drink plenty of water and sleep early. Play outdoors every day. If you eat well and exercise, you will feel strong and happy. Please follow my advice. Take care.", "Neha", "Your loving sister")),
    L("Write an email to your friend in about 80 words describing your visit to a fair.",
      EML("kiran@example.com", "A day at the fair", "Last Sunday I went to the Diwali Fair with my parents. There were many shops selling toys, lamps and sweets. We rode on a giant wheel and a merry-go-round. I ate hot jalebis and bought a small clay lamp. A magician performed tricks that amazed all the children. We came home late. I wish you had been with me.", "Rahul"))),
 OR(A("Write a paragraph in about 80 words on 'Trees are our friends'.",
      PAR("Trees Are Our Friends", "Trees are our true friends. They give us fruits, wood, shade and fresh air. Their roots hold the soil and prevent floods. Birds make their nests on them. Trees also bring rain. Yet, people cut them for roads and houses. We must plant more trees and take care of them. If we protect trees, trees will protect us.")),
    A("Write a story in about 80 words using these points: a lion sleeps — a mouse runs over him — lion catches the mouse — mouse promises to help — lion caught in a net — mouse cuts it.",
      "<b>The Lion and the Mouse</b><br>A lion was sleeping in the forest. A little mouse ran over him and woke him up. The lion caught the mouse and was about to eat it. The mouse begged, ‘Spare me and I shall help you one day.’ The lion laughed and let it go. Later the lion was caught in a hunter's net. The mouse cut the net with its teeth and freed him.<br><b>Moral:</b> Small friends can be a great help.<br>" + FA),
 ),
],
G=[
 g("Choose the correct form: He (don't / doesn't) like tea.", "doesn't."),
 g("Fill in the blank with the past form: Last week we ______ (visit) the museum.", "visited."),
 g("Write the plural of: knife, deer, foot.", "knives, deer, feet."),
 g("Fill in the blank with a suitable conjunction: I stayed at home ______ it was raining.", "because."),
 g("Choose the correct preposition: The cat jumped (off / of) the wall.", "off."),
 g("Write the degree: good — ______ — best.", "better."),
 g("Change into the plural: The girl has a doll.", "The girls have dolls."),
 g("Rearrange to form a sentence: very / the / beautiful / is / moon / tonight", "The moon is very beautiful tonight."),
])

SETS[8] = dict(
W=[
 OR(N("Your school is giving a farewell to the retiring Principal. Write a notice in about 40 words. You are the Cultural Secretary.",
      NOT("10 November 2026", "FAREWELL FUNCTION", "A farewell function for our Principal, Mr Mehta, will be held on 25 November 2026 at 11 a.m. in the school auditorium. Students who wish to present songs or speeches should meet the Cultural Secretary by 20 November.", "Cultural Secretary")),
    N("You are going to a friend's house to study. Write a message in about 30 words for your mother. You are Kabir.",
      MSG("10 November 2026", "Mummy", "I have gone to Rohan's house to study for the Science test. I will be home before dinner. I have taken my bottle and notebooks. Please do not worry.", "Kabir"))),
 OR(L("Write a letter to your friend in about 80 words about a trip you made to a historical place.",
      LET("5, Shyam Nagar, Jaipur", "10 November 2026", "Pankaj", "Last Sunday we visited the Amber Fort. We rode up on an elephant and saw the Sheesh Mahal, whose walls shine like stars. The guide told us stories of the brave kings of Rajasthan. We ate kachori outside and bought small wooden toys. I felt proud of our history. I hope we can visit the fort together some day.", "Dhruv")),
    L("Write an email to your teacher in about 80 words thanking her for helping you in the school quiz.",
      "<b>To:</b> teacher@example.com<br><b>Subject:</b> Thank you<br>Dear Madam,<br>Thank you very much for helping me to prepare for the school quiz. Your notes and encouragement gave me confidence. Our team won the first prize and the Principal appreciated us. We could not have done it without you. I will keep working hard.<br>Yours respectfully,<br>Meera, Class VI-A<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'My Mother'.",
      PAR("My Mother", "My mother is the most loving person in the world. She wakes up early, cooks tasty food and helps us with our homework. She is always smiling and never scolds without reason. She tells us stories at night. When I am ill, she stays awake the whole night. I love my mother very much and promise to make her proud.")),
    A("Write a diary entry in about 80 words about the school Annual Sports Day.",
      DIA("Saturday, 14 November 2026", "Today was our Annual Sports Day. I ran in the 100-metre race and came second. The relay team of my house won the cup. The Chief Guest gave us medals. We cheered each other and enjoyed cold drinks. Although I did not win the first prize, I learnt that taking part is more important.")),
 ),
],
G=[
 g("Fill in the blank with ‘has’ or ‘have’: She ______ a red kite and they ______ blue ones.", "has; have."),
 g("Choose the correct word: The baby is (sleeping / slept) now.", "sleeping."),
 g("Write the opposites: sweet, lend.", "sour (bitter); borrow."),
 g("Fill in the blank with ‘a’, ‘an’ or ‘the’: ______ sun rises in ______ east.", "The; the."),
 g("Change to a negative sentence: They went to the market.", "They did not go to the market."),
 g("Choose the correct pronoun: The teacher praised (we / us).", "us."),
 g("Join using ‘although’: He was tired. He kept working.", "Although he was tired, he kept working."),
 g("Write one word for: ‘a place where books are kept’.", "library."),
])

SETS[9] = dict(
W=[
 OR(N("Your school is holding a Quiz Competition. Write a notice in about 40 words giving details. You are the Quiz Club Secretary.",
      NOT("11 November 2026", "INTER-HOUSE QUIZ", "An inter-house quiz competition will be held on 21 November 2026 at 11 a.m. in the school hall. Each house will send a team of three students. Names should be given to the Quiz Club Secretary by 17 November.", "Quiz Club Secretary")),
    N("You have been called to the Principal's office. Write a message in about 30 words to your friend telling her to take your bag. You are Tina.",
      MSG("11 November 2026", "Sneha", "The Principal has called me to her office. Please take my bag to the next class and tell the teacher that I will join soon. Thank you for your help.", "Tina"))),
 OR(L("Write a letter to your friend in about 80 words congratulating him on winning a prize.",
      LET("14, Sodala, Jaipur", "11 November 2026", "Rishi", "I was very happy to hear that you have won the first prize in the elocution contest. Congratulations! You practised so hard and you truly deserve it. All of us are proud of you. Please treat us to ice cream when we meet. Keep winning many more prizes. Give my regards to your parents.", "Harsh")),
    L("Write an email to your friend in about 80 words telling her about the new pet you have got.",
      EML("pooja@example.com", "My new pet", "I have got a lovely white rabbit. Papa gave it to me for my good result. I have named it Snowy. It eats carrots and lettuce and hops around the garden. Everyone in the family loves it. Do come and meet Snowy this Sunday.", "Garima"))),
 OR(A("Write a paragraph in about 80 words on 'A Rainy Day'.",
      PAR("A Rainy Day", "A rainy day is a delight. The sky is covered with dark clouds and cool winds blow. Raindrops fall on trees and houses. Children float paper boats in puddles. Farmers are happy because their crops get water. But sometimes heavy rain floods the roads. On such a day we enjoy hot pakoras and tea at home.")),
    A("Write a story in about 80 words using these points: a boy loses a ball — a dog finds it — returns it — friendship.",
      "<b>The Dog and the Ball</b><br>Ravi was playing in the park when his ball rolled into the bushes. He searched everywhere but could not find it. Soon a friendly dog came wagging its tail. It had the ball in its mouth. The dog dropped it at Ravi's feet. Ravi patted the dog, and they became good friends.<br><b>Moral:</b> Kindness is returned with love.<br>" + FA),
 ),
],
G=[
 g("Fill in the blank with the correct form: Mother ______ (cook) food when I reached home.", "was cooking."),
 g("Choose the correct word: This is the (best / better) film I have seen.", "best."),
 g("Write the plural of: city, tomato, sheep.", "cities, tomatoes, sheep."),
 g("Fill in the blank with a preposition: We went to school ______ foot.", "on."),
 g("Choose the right option: He gave (me / I) a pencil.", "me."),
 g("Write the past forms: begin, buy.", "began, bought."),
 g("Rewrite as a question: She can swim.", "Can she swim?"),
 g("Rearrange to form a sentence: bought / mother / a / yesterday / new / dress / me / for", "Mother bought a new dress for me yesterday."),
])

SETS[10] = dict(
W=[
 OR(N("Your school is organising a Fancy Dress Competition. Write a notice in about 40 words. You are the Cultural Head.",
      NOT("12 November 2026", "FANCY DRESS COMPETITION", "A Fancy Dress Competition will be held on 27 November 2026 at 10 a.m. in the school hall for Classes 6–8. The theme is ‘Heroes of India’. Participants should give their names to the Cultural Head by 23 November.", "Cultural Head")),
    N("You have to leave early for cricket practice and cannot wait for your younger sister. Write a message in about 30 words for her.",
      MSG("12 November 2026", "Gudiya", "I had to leave early for the cricket practice. Please do not walk alone; wait for Mummy near the gate. Your lunch box is in your bag. See you at home.", "Bhaiya"))),
 OR(L("Write a letter to your friend in about 80 words about how you celebrated your birthday.",
      LET("20, C-Scheme, Jaipur", "12 November 2026", "Aman", "I celebrated my birthday last Saturday. In the morning I wore new clothes and took my parents' blessings. In the evening my friends came for the party. We played games and cut a chocolate cake. I got a cricket bat and many story books as gifts. I missed you at the party. Please come over next time.", "Tushar")),
    L("Write an email to your cousin in about 80 words about your plans for the winter holidays.",
      EML("cousin@example.com", "Winter holidays", "Our winter holidays begin next week. I plan to visit my grandparents in Kota. I want to fly kites, read story books and play cricket in the fields. We will also have a picnic at the river. You should come too. I am sure we will have a wonderful time together.", "Sana"))),
 OR(A("Write a paragraph in about 80 words on 'My Hobby'.",
      PAR("My Hobby", "My hobby is gardening. I spend half an hour every evening in our small garden. I water the plants, remove the weeds and pick the flowers. I have grown roses, marigolds and tomatoes. When I see a flower open, I feel very happy. Gardening keeps me fit and teaches me patience. It is a hobby that I will never give up.")),
    A("Write a diary entry in about 80 words about a visit to your grandparents' house.",
      DIA("Sunday, 15 November 2026", "Today we visited my grandparents. Dadi made laddoos and Dada told me stories of his childhood. I played with my cousins on the terrace and flew kites. In the evening we sat together and had dinner. It was lovely to see them smiling. I wish I could stay longer. We will go again soon.")),
 ),
],
G=[
 g("Fill in the blank with ‘is’ or ‘are’: Neither of my friends ______ here.", "is."),
 g("Choose the correct verb form: She (has / have) finished her work.", "has."),
 g("Write the plural of: leaf, goose, bus.", "leaves, geese, buses."),
 g("Fill in the blank with a suitable adverb: He ran ______ to catch the bus. (quick / quickly)", "quickly."),
 g("Choose the correct preposition: The book is ______ the table. (on / in)", "on."),
 g("Write the opposite: ‘arrive’, ‘generous’.", "depart (leave); selfish (mean, stingy)."),
 g("Add the question tag: You are a student, ______?", "aren't you?"),
 g("Rewrite in the future tense: I play cricket every day.", "I shall play cricket every day."),
])
