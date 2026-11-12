from english_common import *

lex = [
    ("Ravi and I forgot ______ umbrellas at school.", ["my", "our", "their", "your"], 1),
    ("The children ______ playing in the park when it started to rain.", ["is", "was", "were", "are"], 2),
    ("Choose the word closest in meaning to <b>tiny</b>.", ["huge", "small", "heavy", "loud"], 1),
    ("Choose the word opposite in meaning to <b>ancient</b>.", ["old", "modern", "broken", "dusty"], 1),
    ("In which word does the underlined letter sound different from the others?", ["<u>c</u>ity", "<u>c</u>at", "<u>c</u>ow", "<u>c</u>up"], 0),
    ("Which prefix makes the opposite of the word <b>happy</b>?", ["dis-", "un-", "im-", "in-"], 1),
    ("Choose the word that sounds like <b>sea</b> but has a different spelling and meaning.", ["say", "see", "sew", "sit"], 1),
]
jumble = [("MNOTH", "a part of a year, like January", "MONTH"), ("HCEATER", "a person who teaches in a school", "TEACHER")]
choose2 = [("Ramesh is (taller / tallest) than his younger brother.", "taller"),
           ("Please sit (between / among) the two girls on the bench.", "between")]
fill3 = (["slowly", "library", "sings"],
         ["Our school has a big ______ with thousands of books.",
          "The tortoise walked ______ across the road.",
          "My sister ______ a sweet song every morning."],
         ["library", "slowly", "sings"])
choose5 = [("She (go / goes / going) to school by bus.", "goes"),
           ("We (will / did / are) visit Amer Fort tomorrow.", "will"),
           ("The bird sat (on / in / at) the branch of the tree.", "on"),
           ("My grandfather (always / never / rarely) wakes up before sunrise; he is an early riser.", "always"),
           ("There (is / are) many peacocks in the garden.", "are")]
cloze = ("<br>Last Sunday, our family went to the cattle (1)______ at Pushkar, where people buy and sell camels. We reached the railway (2)______ early "
         "and stood in a long queue to buy (3)______. My little brother was so (4)______ that he kept clapping all the way.",
         ["station", "tickets", "excited", "fair", "sleepy", "lantern"], ["fair", "station", "tickets", "excited"])
match = (["A zebra crossing", "The red signal of a traffic light", "A helmet", "Soap", "A toothbrush"],
         ["helps us keep our hands clean", "protects the head of a scooter rider", "tells vehicles to stop", "cleans our teeth", "helps people cross the road safely"],
         ["(e)", "(c)", "(b)", "(a)", "(d)"])
arts = [("Ravi is ______ honest boy.", "an"), ("______ Sun rises in the east.", "The")]

A = ("Aman lives in Jaisalmer, where the night sky is wide and clear. On his tenth birthday, his uncle gave him a small telescope. That evening, Aman climbed to the roof "
     "with his sister Neha and pointed it at the Moon. He was amazed to see round holes on its surface. &ldquo;Those are craters,&rdquo; said his uncle. &ldquo;Rocks from space hit the Moon long ago and made them.&rdquo; "
     "Neha asked why the Moon shines. Her uncle explained that the Moon has no light of its own; it only reflects the light of the Sun. He also told them that India&rsquo;s Chandrayaan-3 landed near the "
     "Moon&rsquo;s south pole in 2023. Aman felt proud and decided to become a scientist. Since then, he looks at the sky every clear night and notes down what he sees in a small diary.")
readA = (A, "Aman and the Moon", [
    [("Who gave Aman a telescope, and on which occasion?", "His uncle gave it to him on his tenth birthday.", 2),
     ("What did Aman see on the surface of the Moon through the telescope?", "He saw round holes (craters) on the Moon&rsquo;s surface.", 2),
     ("Find a word from the passage that means <i>very surprised</i>.", "amazed", 1)],
    [("What are craters, according to Aman&rsquo;s uncle?", "Craters are holes made by rocks from space that hit the Moon long ago.", 2),
     ("Why does the Moon shine?", "The Moon has no light of its own; it shines because it reflects the light of the Sun.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>narrow</i>.", "wide", 1)],
    [("What did Aman decide after that evening?", "He decided to become a scientist.", 2),
     ("What does Aman do on every clear night?", "He looks at the sky and notes down what he sees in a small diary.", 2),
     ("Write the plural form of <b>diary</b>.", "diaries", 1)]])

B = ("Lakshmi, a girl of Class V, was walking home from school in Bikaner when she saw a small green purse lying near the bus stop. She picked it up and opened it. It had a few notes, a bus pass and a photograph. "
     "Many children would have kept the money, but Lakshmi did not. She read the name on the bus pass: Mr Gopal Verma. She asked a shopkeeper nearby if he knew him. &ldquo;He works at the post office,&rdquo; said the shopkeeper. "
     "Lakshmi went there at once and handed the purse to Mr Verma. He was very happy because he had been searching for it for an hour. He offered her some money as a reward, but she politely refused. "
     "&ldquo;My mother says honesty is its own reward,&rdquo; she said. The next day, Mr Verma came to her school and told the whole assembly about her. The principal gave Lakshmi a certificate and everyone clapped loudly.")
readB = (B, "Lakshmi and the Green Purse", [
    [("Where did Lakshmi find the purse?", "She found it lying near the bus stop.", 2),
     ("What was inside the purse?", "It had a few notes, a bus pass and a photograph.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>accepted</i>.", "refused", 1)],
    [("How did Lakshmi find out who the owner of the purse was?", "She read the name on the bus pass and asked a shopkeeper, who told her Mr Verma worked at the post office.", 2),
     ("Why was Mr Verma very happy?", "He had been searching for his purse for an hour and Lakshmi returned it to him.", 2),
     ("Find a word from the passage that means <i>a gift given for a good deed</i>.", "reward", 1)],
    [("What did Lakshmi say when Mr Verma offered her money?", "She said, &ldquo;My mother says honesty is its own reward.&rdquo;", 2),
     ("What did the principal give Lakshmi?", "The principal gave her a certificate.", 2),
     ("Write the singular form of <b>children</b>.", "child", 1)]])

letter = Q("You are Rohan/Riya of Class V, Sunrise Public School, Kota. You have a high fever. Write an <b>application</b> to your class teacher asking for two days&rsquo; leave.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Sample:</i> To, The Class Teacher, Class V, Sunrise Public School, Kota. Date: 12 July 2026. "
    "Subject: Application for two days&rsquo; leave. Respected Madam, I beg to say that I am suffering from high fever since last night and the doctor has advised me to take complete rest. "
    "So I cannot attend school on 13 and 14 July. Kindly grant me leave for these two days. Thanking you. Yours obediently, Rohan, Class V, Roll No. 14.",
    alt=Q("Write a <b>letter</b> to your friend Karan, inviting him to your birthday party on Sunday at your house.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Points:</i> address and date; greeting (Dear Karan); invitation with day, time, place; what will be done (cake, games, lunch); request to come; closing (Your friend, name)."))

scene = "<div style='font-size:26px;line-height:1.3'>🌳 &nbsp;🌳 &nbsp;☀️ &nbsp;🐦 &nbsp;🌸<br>🧒⚽ &nbsp;👧🚲 &nbsp;🐕 &nbsp;🧓🪑 &nbsp;🍦</div>"
pic = Q("Look at the picture of a park. Write <b>four</b> sentences about it. (2 marks each)", 8,
    "<b>Any four correct sentences, 2 marks each (1 for content, 1 for correct grammar).</b><br><i>Sample:</i> A boy is playing football. A girl is riding a bicycle. A dog is running near the trees. An old man is sitting on a chair. (Also: Birds are flying; the sun is shining.)",
    fig=scene,
    alt=Q("Complete the story using the words given: <i>kite, tree, string, helped, thanked</i>.<br>One windy day, Gopal was flying his kite &hellip;", 8,
    "<b>Marking: sense 3 + use of the five words 3 + language 2.</b><br><i>Sample:</i> One windy day, Gopal was flying his kite on the roof. Suddenly the string broke and the kite got stuck in a tall tree. Gopal was sad. His neighbour Imran saw him and helped him to get it down with a long stick. Gopal thanked him and gave him a sweet."))

make(1, lex, jumble, choose2, fill3, choose5, cloze, match, arts, readA, readB, letter, pic)
