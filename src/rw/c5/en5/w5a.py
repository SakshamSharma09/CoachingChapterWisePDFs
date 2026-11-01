"""Class 5 Writing & Grammar sets 1-5 (original). W = [message/notice(3) OR, letter/invitation(5) OR, paragraph(4) OR]; G = 8 items."""
from eng9_lib import Q, OR
def N(q, a): return Q(q, a, "3")
def L(q, a): return Q(q, a, "5")
def A(q, a): return Q(q, a, "4")
def g(q, a): return Q(q, a, "1")
SETS = {}

SETS[1] = dict(W=[
 OR(N("You are Ria/Rohan. You are going to your uncle's house for two days. Write a message in about 30 words to your friend Sameer to tell him that you will not attend the cricket practice.",
      "<b>MESSAGE</b><br>5 March, 4:00 p.m.<br>Dear Sameer,<br>I am going to my uncle's house for two days, so I cannot come to cricket practice. Please tell the coach. I will join you on Friday.<br>Ria"),
    N("Your school is going to hold a Drawing Competition. Write a notice in about 40 words. You are the Head Boy/Head Girl.",
      "<b>NOTICE</b><br>Mastermind Public School<br>5 March 2026<br><b>DRAWING COMPETITION</b><br>A drawing competition will be held on 12 March in the school hall at 10 a.m. Topic: 'My Village'. Students should bring their own colours. Give your names to the art teacher by 9 March.<br>Head Boy")),
 OR(L("Write a letter to your friend inviting him/her to your birthday party. Give the date, time and place. (About 60 words)",
      "12, Green Park<br>Jaipur<br>5 March 2026<br>Dear Nisha,<br>I am having my birthday party on Sunday, 15 March, at 5 p.m. at my house. We will cut the cake, play games and eat tasty food. Please come with your parents. I will be waiting for you.<br>Your friend,<br>Ria"),
    L("Write a letter to your grandmother telling her about your school annual day. (About 60 words)",
      "7, Shanti Nagar<br>Jaipur<br>5 March 2026<br>Dear Dadi,<br>I hope you are well. Our school annual day was held last Saturday. I danced in a group dance and everybody clapped. I also got a prize for good attendance. Please come to see us in the holidays.<br>With love,<br>Rohan")),
 OR(A("Write 5–6 sentences about 'My Pet' (or an animal you like).",
      "I have a pet dog named Tommy. He is brown and has soft fur. He plays with me every evening. He guards our house at night. I give him milk and bread. He loves me very much."),
    A("Write 5–6 sentences about 'My School'.",
      "My school is Mastermind Public School. It has a big playground and a library. My teachers are kind. We have many friends here. I go to school at 8 o'clock. I love my school.")),
], G=[
 g("Write the plural of 'baby'.", "babies."),
 g("Fill in the blank with a, an or the: ______ elephant is a big animal.", "An."),
 g("Choose the correct word: She (go / goes) to school daily.", "goes."),
 g("Write the opposite of 'hot'.", "cold."),
 g("Fill in the blank with the correct preposition (in / on / at): The book is ______ the table.", "on."),
 g("Choose the correct pronoun: (He / Him) is my brother.", "He."),
 g("Add a full stop or a question mark: Where do you live", "Where do you live?"),
 g("Fill in the blank with the correct form: Tara ______ (is / are) playing in the garden.", "is."),
])

SETS[2] = dict(W=[
 OR(N("You are Aman/Anita. Your mother is not at home. Write a message in about 30 words to her telling that your friend came to meet her.",
      "<b>MESSAGE</b><br>6 March, 5:00 p.m.<br>Dear Mummy,<br>Your friend Mrs Gupta came to meet you at 4 p.m. She will come again tomorrow morning. Please wait for her.<br>Aman"),
    N("Write a notice in about 40 words for the school notice board about a lost water bottle. You are the class monitor.",
      "<b>NOTICE</b><br>Mastermind Public School<br>6 March 2026<br><b>LOST</b><br>A blue water bottle was lost near the playground on Monday. If anyone finds it, please give it to the class teacher of Class 5-A.<br>Class Monitor")),
 OR(L("Write a letter to your friend telling him/her about your summer holidays plan. (About 60 words)",
      "14, Model Town<br>Jaipur<br>6 March 2026<br>Dear Karan,<br>I am very happy as holidays are coming. I will go to my aunt's house in Udaipur. We will visit the lake and the palace. I will also read story books. Tell me what you will do.<br>Your friend,<br>Anita"),
    L("Write a letter to your father who is away on a tour, telling him about your studies. (About 60 words)",
      "9, Vaishali Nagar<br>Jaipur<br>6 March 2026<br>Dear Papa,<br>We are all fine and miss you. I am studying every day for my exams. I finished my Maths and English books. Mummy helps me in Science. Please come back soon.<br>Your loving son,<br>Aman")),
 OR(A("Write 5–6 sentences about 'My Best Friend'.",
      "My best friend is Rahul. He sits next to me in class. He is honest and helpful. We play cricket together. He shares his tiffin with me. I like him very much."),
    A("Write 5–6 sentences about 'A Visit to a Park'.",
      "Last Sunday I went to a park with my family. There were flowers, trees and swings. I played on the slide. We ate ice cream. Many birds were singing. We came home happily.")),
], G=[
 g("Write the plural of 'child'.", "children."),
 g("Fill in the blank with a, an or the: She has ______ umbrella.", "an."),
 g("Choose the correct verb: They (is / are) in the garden.", "are."),
 g("Write the opposite of 'up'.", "down."),
 g("Choose the correct preposition (in / at / on): I get up ______ six o'clock.", "at."),
 g("Choose the correct pronoun: Give the book to (she / her).", "her."),
 g("Put a capital letter where needed: my friend lives in delhi.", "My friend lives in Delhi."),
 g("Change into past tense: I play cricket.", "I played cricket."),
])

SETS[3] = dict(W=[
 OR(N("You are Neha/Nitin. Write a message in about 30 words to your teacher saying that you will be late to school tomorrow because of a doctor's visit.",
      "<b>MESSAGE</b><br>7 March<br>Respected Madam,<br>I have to go to the doctor tomorrow morning, so I will reach school late. Kindly excuse me.<br>Yours obediently,<br>Neha"),
    N("Write a notice in about 40 words about a Picnic to the Zoo. You are the class teacher.",
      "<b>NOTICE</b><br>Mastermind Public School<br>7 March 2026<br><b>PICNIC TO THE ZOO</b><br>Class 5 will go to the zoo on 20 March. The bus will leave at 8 a.m. Students should bring lunch and water. Give Rs 100 and the permission slip by 15 March.<br>Class Teacher")),
 OR(L("Write a letter to your cousin thanking him/her for a birthday gift. (About 60 words)",
      "21, Sector 4<br>Jaipur<br>7 March 2026<br>Dear Mohit,<br>Thank you very much for the lovely storybook you sent for my birthday. I read it in one day. The pictures are very nice. I will keep it safely. Please come to our house soon.<br>Your cousin,<br>Neha"),
    L("Write a letter to your friend inviting him/her to your house for Diwali. (About 60 words)",
      "21, Sector 4<br>Jaipur<br>7 March 2026<br>Dear Rishi,<br>Diwali is coming and we are very happy. Please come to my house on Diwali day. We will light diyas, burst crackers and eat sweets. Please bring your parents too.<br>Your friend,<br>Nitin")),
 OR(A("Write 5–6 sentences about 'My Mother'.",
      "My mother is the best person in the world. She wakes up early and cooks food. She helps me with my homework. She tells me stories at night. She takes care of all of us. I love my mother."),
    A("Write 5–6 sentences about 'The Cow'.",
      "The cow is a useful animal. She has four legs, two horns and a tail. She eats grass and hay. She gives us milk. Milk is used to make curd, butter and sweets. We should be kind to cows.")),
], G=[
 g("Write the plural of 'bus'.", "buses."),
 g("Fill in the blank with a, an or the: ______ sun rises in the east.", "The."),
 g("Choose the correct verb: Ravi (play / plays) football.", "plays."),
 g("Write the opposite of 'happy'.", "sad."),
 g("Choose the correct preposition (in / on / under): The cat is ______ the bed. (below)", "under."),
 g("Fill in the blank with 'and', 'but' or 'or': I like tea ______ she likes coffee.", "but."),
 g("Choose the correct word: He is (taller / tallest) than me.", "taller."),
 g("Write the plural of 'leaf'.", "leaves."),
])

SETS[4] = dict(W=[
 OR(N("You have found a pen in the classroom. Write a notice in about 40 words. You are the monitor.",
      "<b>NOTICE</b><br>Mastermind Public School<br>8 March 2026<br><b>FOUND</b><br>A black pen has been found in Class 5-B. The owner may collect it from the class teacher after proving ownership.<br>Monitor, Class 5-B"),
    N("Write a message in about 30 words to your friend asking him/her to bring a Maths book tomorrow. You are Tanu/Tarun.",
      "<b>MESSAGE</b><br>8 March, 6 p.m.<br>Dear Vikas,<br>I have forgotten my Maths book at home. Please bring your Maths book to school tomorrow. I will return it after the class.<br>Tarun")),
 OR(L("Write a letter to your friend who is ill, wishing him/her well. (About 60 words)",
      "6, Ashok Nagar<br>Jaipur<br>8 March 2026<br>Dear Sunil,<br>I was sorry to know that you are ill. Take rest and eat fruits. Do not worry about studies; I will share my notes with you. Get well soon.<br>Your friend,<br>Tanu"),
    L("Write a letter to your teacher requesting leave for two days because of fever. (About 60 words)",
      "6, Ashok Nagar<br>Jaipur<br>8 March 2026<br>The Class Teacher<br>Mastermind Public School<br>Respected Madam,<br>I have fever and cannot come to school on 9 and 10 March. Kindly grant me leave for two days.<br>Yours obediently,<br>Tarun")),
 OR(A("Write 5–6 sentences about 'My Favourite Festival'.",
      "My favourite festival is Diwali. We clean our houses and light diyas. We wear new clothes and eat sweets. We worship Goddess Lakshmi. Children burst crackers carefully. Diwali brings joy to everyone."),
    A("Write 5–6 sentences about 'A Rainy Day'.",
      "It was raining heavily. The sky was dark with clouds. I wore my raincoat and went out. I sailed a paper boat in the puddle. My mother made hot pakoras. I enjoyed the rainy day.")),
], G=[
 g("Write the plural of 'man'.", "men."),
 g("Fill in the blank with a, an or the: Delhi is ______ capital of India.", "the."),
 g("Choose the correct verb: She (sing / sings) a song.", "sings."),
 g("Write the opposite of 'early'.", "late."),
 g("Choose the correct preposition (in / on / of): He is the captain ______ our team.", "of."),
 g("Choose the correct pronoun: This book is (mine / me).", "mine."),
 g("Change into past tense: She eats an apple.", "She ate an apple."),
 g("Add the correct punctuation: how beautiful the rose is", "How beautiful the rose is!"),
])

SETS[5] = dict(W=[
 OR(N("You are Sana/Sameer. Write a message in about 30 words to your neighbour telling him/her that you are going out of town for a week and ask to collect the newspaper.",
      "<b>MESSAGE</b><br>9 March<br>Dear Uncle,<br>We are going out of town for a week. Please keep our newspaper with you. We will take it when we return. Thank you.<br>Sameer"),
    N("Write a notice in about 40 words about an Annual Sports Day. You are the sports captain.",
      "<b>NOTICE</b><br>Mastermind Public School<br>9 March 2026<br><b>ANNUAL SPORTS DAY</b><br>The Annual Sports Day will be held on 25 March at 8 a.m. in the school ground. Races, relay and tug of war will take place. All students should wear sports dress.<br>Sports Captain")),
 OR(L("Write a letter to your friend describing a trip to the zoo. (About 60 words)",
      "3, Gandhi Path<br>Jaipur<br>9 March 2026<br>Dear Hari,<br>Last Sunday I visited the zoo with my family. I saw lions, tigers, elephants and monkeys. The peacocks were dancing. We took many photos. I want to go again with you.<br>Your friend,<br>Sana"),
    L("Write a letter to your uncle inviting him to your school Annual Day. (About 60 words)",
      "3, Gandhi Path<br>Jaipur<br>9 March 2026<br>Dear Uncle,<br>Our school Annual Day will be held on 28 March at 5 p.m. I will take part in a play. Please come with aunty and my cousins. We will be very happy to see you.<br>Your nephew,<br>Sameer")),
 OR(A("Write 5–6 sentences about 'My Country, India'.",
      "India is my country. It is a big and beautiful land. It has rivers, mountains and deserts. People of many religions live here like brothers. Our national flag is the Tricolour. I love my country."),
    A("Write 5–6 sentences about 'Summer Season'.",
      "Summer is very hot. The days are long and the nights are short. We drink cold water and lassi. We eat mangoes and watermelons. We wear light cotton clothes. Schools are closed for holidays.")),
], G=[
 g("Write the plural of 'tooth'.", "teeth."),
 g("Fill in the blank with a, an or the: He is ______ honest boy.", "an."),
 g("Choose the correct verb: The birds (is / are) singing.", "are."),
 g("Write the opposite of 'strong'.", "weak."),
 g("Choose the correct preposition (in / at / on): She was born ______ Jaipur.", "in."),
 g("Choose the correct word: He (go / goes) to school by bus.", "goes."),
 g("Join with 'because': I was late. The bus was late.", "I was late because the bus was late."),
 g("Choose the correct spelling: (freind / friend).", "friend."),
])
