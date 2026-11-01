"""Class 6 Writing & Grammar sets 1-5 (original). W=[notice/message (3) OR, letter/email (5) OR, paragraph/diary (4) OR]; G=8 grammar items."""
from en6.whelp import *
SCH = "Mastermind Public School, Jaipur"
SETS = {}

SETS[1] = dict(
W=[
 OR(N("Your school is organising a Drawing Competition. Write a notice in about 40 words giving the date, time and venue. You are the Art Teacher, Mrs Sharma.",
      NOT("2 November 2026", "DRAWING COMPETITION", "A Drawing Competition will be held on 14 November 2026 at 10 a.m. in the school hall. The topic is ‘My Dream House’. Students of Classes 6–8 may take part. Bring your own colours.", "Mrs Sharma, Art Teacher")),
    N("You are going to your grandmother's house and your mother is out. Write a message in about 30 words for her telling where you have gone, when you will return and what to heat for dinner. You are Rahul/Rhea.",
      MSG("2 November 2026", "Mummy", "I have gone to Nani's house with Papa. We will come back by 8 p.m. The dal is in the fridge; please heat it for dinner. Do not worry.", "Rahul/Rhea"))),
 OR(L("Write a letter to your friend Karan in about 80 words inviting him to spend the Diwali holidays at your house in Jaipur.",
      LET("14, Gandhi Nagar, Jaipur", "2 November 2026", "Karan", "How are you? I hope you are fine. Diwali is coming and I am very excited. I want you to spend the holidays with us in Jaipur. We shall make rangoli, light diyas and eat lots of sweets. My cousins will also be there. We can visit the Amber Fort too. Please ask your parents and come soon. I am sure we shall have great fun together.", "Ravi")),
    L("Write an email to your cousin Neha in about 80 words telling her about your school's Annual Day.",
      EML("neha@example.com", "Our Annual Day", "I hope you are well. Last Friday our school held its Annual Day. I danced in a group song and our class won the first prize in the skit. The Chief Guest gave medals to all the winners. My parents were very proud. We ate samosas and ice cream afterwards. I wish you had been there. Do write to me soon.", "Meena"))),
 OR(A("Write a paragraph in about 80 words on 'My Pet' (or an animal you would like to keep).",
      PAR("My Pet", "I have a pet dog named Tommy. He is brown and white, and he has long, soft ears. Every morning he wakes me up by licking my face. I take him for a walk in the park and play fetch with him. He is very clever and loyal. He guards our house at night. I feed him milk and biscuits. Tommy is my best friend and I love him dearly.")),
    A("Write a diary entry in about 80 words about the happiest day of your week.",
      DIA("Friday, 6 November 2026", "Today was the happiest day of my week. Our class went to the zoo. We saw lions, elephants and colourful parrots. I fed a baby deer with grass. We had lunch under a big tree and sang songs on the bus. My teacher clicked our photos. I was tired but very happy. I hope we go on another trip soon.")),
 ),
],
G=[
 g("Fill in the blank with ‘a’, ‘an’ or ‘the’: She ate ______ apple and drank ______ milk.", "an; the."),
 g("Choose the correct verb: The boys (is / are) playing in the garden.", "are."),
 g("Write the plural of: child, box, leaf.", "children, boxes, leaves."),
 g("Fill in the blank with a suitable preposition: The cat is hiding ______ the table.", "under (or ‘beneath’/‘behind’)."),
 g("Write the opposite of ‘brave’ and of ‘ancient’.", "cowardly (timid); modern."),
 g("Rewrite in the past tense: Mother cooks food every day.", "Mother cooked food every day."),
 g("Join with ‘because’: She was happy. She won the prize.", "She was happy because she won the prize."),
 g("Rearrange to form a meaningful sentence: is / a / the / sun / star", "The sun is a star."),
])

SETS[2] = dict(
W=[
 OR(N("Your school is holding a Health Week. Write a notice in about 40 words. You are the School Captain.",
      NOT("3 November 2026", "HEALTH WEEK", "A Health Week will be observed in school from 9 to 13 November 2026. Doctors will give talks on healthy habits every morning in the assembly. Students of Classes 6–8 are requested to attend. Wear clean uniform.", "School Captain")),
    N("You have to go for tuition and your sister Priya is at home. Write a message in about 30 words telling her where the keys are and what to do before you come back.",
      MSG("3 November 2026", "Priya", "I have gone for tuition and will return at six. The keys are under the green flower pot. Please water the plants and keep the milk inside the fridge. Thank you.", "Rohit"))),
 OR(L("Write a letter to your grandmother in about 80 words thanking her for the birthday gift she sent you.",
      LETF("22, Lal Kothi, Jaipur", "3 November 2026", "Nani", "Thank you very much for the lovely birthday gift. The story books are just what I wanted. I started reading the first one last night and enjoyed it very much. My friends also liked the party. I miss you a lot and wish you could have been here. Please come to Jaipur during the holidays. Mummy and Papa send their regards.", "Aarav", "Your loving grandson")),
    L("Write an email to your friend in about 80 words telling him about a book you have recently read.",
      EML("sameer@example.com", "A book I loved", "I hope you are well. I recently read ‘The Jungle Book’. It is the story of a boy called Mowgli who lives with wolves. Baloo the bear and Bagheera the panther teach him about the jungle. I liked the brave Mowgli best. The book teaches us about friendship and courage. You should read it too. Tell me which book you are reading.", "Vikram"))),
 OR(A("Write a paragraph in about 80 words on 'My School Library'.",
      PAR("My School Library", "Our school library is a quiet, bright room on the first floor. It has hundreds of books, magazines and newspapers. The librarian, Mr Verma, helps us to find the books we like. We visit the library twice a week and can borrow one book for seven days. I love reading adventure stories and science books there. The library teaches us to read, to think and to keep silence.")),
    A("Write a diary entry in about 80 words about a rainy day at your home.",
      DIA("Sunday, 8 November 2026", "It rained heavily today. The sky was grey from morning and I could not go out to play. I made a paper boat and floated it in the water at the gate. Mummy made hot pakoras and tea. We sat near the window and watched the raindrops. In the evening the sky cleared and there was a lovely rainbow. It was a cosy day.")),
 ),
],
G=[
 g("Fill in the blank with ‘is’, ‘am’ or ‘are’: I ______ a student and my friends ______ also students.", "am; are."),
 g("Write the past tense of: go, eat, write.", "went, ate, wrote."),
 g("Choose the correct word: He is (taller / tallest) than his brother.", "taller."),
 g("Fill in the blank with a suitable pronoun: Ravi and I are friends. ______ play together every day.", "We."),
 g("Add the correct punctuation: what a beautiful garden it is", "What a beautiful garden it is!"),
 g("Write the feminine of: prince, host, uncle.", "princess, hostess, aunt."),
 g("Join with ‘but’: He tried hard. He did not win.", "He tried hard but he did not win."),
 g("Choose the correct option: There (is / are) many books on the shelf.", "are."),
])

SETS[3] = dict(
W=[
 OR(N("Your school will be closed for Holi. Write a notice in about 40 words informing students about the holiday and the date school reopens. You are the Principal.",
      NOT("3 March 2027", "HOLI HOLIDAY", "The school will remain closed on 6 March 2027 on account of Holi. It will reopen on Monday, 8 March 2027. Students are advised to play with safe, herbal colours and take care of their eyes.", "Principal")),
    N("You are going to the market with your father. Write a message for your elder brother in about 30 words telling him to take the washing from the terrace.",
      MSG("5 March 2027", "Bhaiya", "Papa and I have gone to the market and will return by 7 p.m. Please bring the washing from the terrace before it gets dark. Also, switch off the fan in my room. Thanks.", "Sonu"))),
 OR(L("Write a letter to your friend in about 80 words telling him/her about your new school.",
      LET("7, Vidhyadhar Nagar, Jaipur", "3 March 2027", "Anju", "I hope you are well. I have joined a new school this year. It has a big playground, a library and a computer lab. My class teacher, Mrs Gupta, is very kind. I have made two good friends already, Ritu and Sonal. We play together at recess. I like the school but I miss you all. Please write back soon and tell me about your school.", "Divya")),
    L("Write an email to your uncle in about 80 words wishing him on his birthday.",
      EML("uncle@example.com", "Happy Birthday!", "Many happy returns of the day! I wish you good health and happiness in the coming year. I still remember the lovely time we spent together at your house last summer. I have made a card for you and will give it when we meet. Mummy and Papa also send you their love. Please cut a big cake for me!", "Anshul"))),
 OR(A("Write a paragraph in about 80 words on 'My Favourite Festival'.",
      PAR("My Favourite Festival", "My favourite festival is Diwali. It is the festival of lights. We clean our house, make rangoli and light diyas. In the evening we worship Goddess Lakshmi and eat sweets. Children burst crackers but I prefer sparklers. Relatives and friends visit each other and exchange gifts. Everyone wears new clothes and the whole city glows. Diwali teaches us that good always wins over evil.")),
    A("Complete the story in about 80 words. ‘A thirsty crow found a pot with a little water at the bottom. The beak could not reach…’",
      "<b>A Clever Crow</b><br>A thirsty crow found a pot with a little water at the bottom. The beak could not reach the water. The crow thought hard. It saw some pebbles nearby. It picked them one by one and dropped them in the pot. Slowly the water rose to the top. The crow drank to its heart's content and flew away happily.<br><b>Moral:</b> Where there is a will, there is a way.<br>" + FA),
 ),
],
G=[
 g("Fill in the blank with the correct form of the verb: She ______ (sing) a song at the moment.", "is singing."),
 g("Choose the correct article: He is ______ honest boy. (a / an / the)", "an."),
 g("Write the plural of: mouse, man, tooth.", "mice, men, teeth."),
 g("Fill in the blank with ‘in’, ‘on’ or ‘at’: The meeting starts ______ 10 o'clock ______ Monday.", "at; on."),
 g("Write a word that means the same as ‘big’ and a word that means the opposite of ‘late’.", "large/huge; early."),
 g("Rewrite as a question: You are coming to my party.", "Are you coming to my party?"),
 g("Choose the correct word: Neither of the boys (was / were) present.", "was."),
 g("Rearrange to form a sentence: reads / a / every / newspaper / my / day / father", "My father reads a newspaper every day."),
])

SETS[4] = dict(
W=[
 OR(N("Your school is going on an excursion to the Albert Hall Museum. Write a notice in about 40 words. You are the Class Teacher.",
      NOT("4 November 2026", "SCHOOL EXCURSION", "Class VI will visit the Albert Hall Museum, Jaipur, on 16 November 2026. The bus will leave at 8 a.m. Students should bring lunch, water and ₹100. Parents' consent slips must be submitted by 12 November.", "Class Teacher")),
    N("Your friend Aman came to your house to meet you but you were out. Write a message in about 30 words for him telling him why you were out and when you will call.",
      MSG("4 November 2026", "Aman", "I am sorry I was not at home when you came. I had gone to the dentist with my mother. I will be back by five and will call you in the evening. Please wait for my call.", "Sachin"))),
 OR(L("Write a letter to your father who is staying in another city, in about 80 words, telling him about your exam preparation.",
      LETF("15, Malviya Nagar, Jaipur", "4 November 2026", "Papa", "I hope you are well. My half-yearly exams begin from next week. I am studying two hours daily and have finished revising Maths and Science. Mummy helps me with English. I am a little worried about Social Science but I will do my best. Please take care of your health and come home soon. I miss you a lot.", "Deepak", "Your loving son")),
    L("Write an email to your teacher in about 80 words asking for leave for two days because you are ill.",
      "<b>To:</b> teacher@example.com<br><b>Subject:</b> Leave of absence<br>Respected Madam,<br>I am Aman of Class VI-B. I have a fever and the doctor has advised me to rest for two days. I shall therefore not be able to come to school on 5 and 6 November 2026. Kindly grant me leave for these days. I shall complete my classwork after I return.<br>Yours obediently,<br>Aman, Class VI-B, Roll No. 14<br>" + FL)),
 OR(A("Write a paragraph in about 80 words on 'A Visit to a Zoo'.",
      PAR("A Visit to a Zoo", "Last Sunday I visited the zoo with my family. We saw tigers, lions and monkeys in cages. The elephant was the biggest animal there. I enjoyed watching the colourful birds. We took a ride on the toy train and had lunch in the garden. The zoo keeper told us not to feed the animals. We returned home in the evening, tired but happy.")),
    A("Write a diary entry in about 80 words about the day you helped someone.",
      DIA("Thursday, 5 November 2026", "Today I helped an old lady to cross the road. She was carrying a heavy bag and could not walk fast. I held her hand and carried her bag across. She blessed me and gave me a toffee. I felt very happy. Mummy said that small acts of kindness are the best. I will try to help others every day.")),
 ),
],
G=[
 g("Fill in the blank with the correct form: Yesterday I ______ (see) a rainbow.", "saw."),
 g("Choose the correct pronoun: This book is (my / mine).", "mine."),
 g("Write the opposites: hot, strong, empty.", "cold, weak, full."),
 g("Fill in the blank with a suitable word: The sun ______ in the east.", "rises."),
 g("Choose the right option: She has (much / many) friends.", "many."),
 g("Change into the negative: He plays hockey.", "He does not play hockey."),
 g("Write one word for: ‘a person who writes books’.", "author (writer)."),
 g("Correct the sentence: She go to school by bus.", "She goes to school by bus."),
])

SETS[5] = dict(
W=[
 OR(N("Your school is organising a Cleanliness Drive. Write a notice in about 40 words inviting students to join. You are the Head Boy/Head Girl.",
      NOT("6 November 2026", "CLEANLINESS DRIVE", "A Cleanliness Drive will be conducted on 15 November 2026 at 8 a.m. in the school campus and nearby park. Interested students should give their names to the Class Teacher by 12 November. Bring gloves and a cap.", "Head Boy/Head Girl")),
    N("Your parents are out and you have to go to the library. Write a message in about 30 words for your grandfather telling him where you have gone and when you will return.",
      MSG("6 November 2026", "Dadaji", "I have gone to the school library to return some books. I will be back by 5 p.m. The tea is on the table, and your medicine is next to the clock. Please rest.", "Mohit"))),
 OR(L("Write a letter to your friend in about 80 words describing how you spent your summer vacation.",
      LET("9, Pratap Nagar, Jaipur", "6 November 2026", "Sanjay", "I hope you are in the best of health. My summer vacation was wonderful. I went to my grandparents' village for two weeks. I played in the fields, swam in the pond and ate fresh mangoes. We also visited a fair. I read three story books as well. I wish you had come along. Tell me how you spent your holidays.", "Naman")),
    L("Write an email to your friend in about 80 words telling him about your favourite sport.",
      EML("rahul@example.com", "My favourite sport", "I hope you are well. My favourite sport is cricket. I play it every evening with my friends in the park. I bat well and sometimes bowl spin. Last week our team won a match by ten runs. Cricket teaches us teamwork and discipline. My hero is Virat Kohli. Which sport do you like? Write to me soon.", "Aryan"))),
 OR(A("Write a paragraph in about 80 words on 'My Best Friend'.",
      PAR("My Best Friend", "My best friend is Rohan. He sits next to me in class. He is honest, friendly and helpful. When I forget my pencil, he lends me his. We play cricket together and share our lunch. He helps me in Maths and I help him in English. He never tells a lie. A true friend is a rare treasure, and I am lucky to have him.")),
    A("Write a short story in about 80 words with the title ‘The Honest Boy’. Use these points: a boy finds a purse — takes it to the teacher — owner gets it back — boy is praised.",
      "<b>The Honest Boy</b><br>Sohan was walking to school when he found a purse on the road. It had a lot of money in it. He did not keep it. He took it to his teacher, who announced it in the assembly. Soon an old man came and claimed the purse. He thanked Sohan and the Principal praised him before everyone.<br><b>Moral:</b> Honesty is the best policy.<br>" + FA),
 ),
],
G=[
 g("Fill in the blank with ‘some’ or ‘any’: I do not have ______ money, but I have ______ coins.", "any; some."),
 g("Choose the correct preposition: He jumped (in / into) the river.", "into."),
 g("Change into plural: This is a ripe mango.", "These are ripe mangoes."),
 g("Fill in the blank: They ______ (play) football when it started raining.", "were playing."),
 g("Choose the correct word: I want to (buy / by) a pen.", "buy."),
 g("Write the opposite of: increase, accept.", "decrease; refuse (reject)."),
 g("Join using ‘and’: Ria sings. Ria dances.", "Ria sings and dances."),
 g("Rearrange: a / bird / sings / sweet / song / the", "The bird sings a sweet song."),
])
