from english_common import *

lex = [
    ("The monkeys ate all the bananas, and then ______ ran away.", ["he", "it", "they", "we"], 2),
    ("My cousins ______ just reached Jaipur.", ["has", "have", "is", "was"], 1),
    ("Choose the word closest in meaning to <b>silent</b>.", ["loud", "quiet", "rough", "sharp"], 1),
    ("Choose the word opposite in meaning to <b>victory</b>.", ["win", "defeat", "prize", "match"], 1),
    ("Which word is an adjective in this sentence? <i>Seema wore a beautiful dress.</i>", ["Seema", "wore", "beautiful", "dress"], 2),
    ("What is formed by adding the prefix <b>re-</b> (meaning &lsquo;again&rsquo;) to the word <b>write</b>?", ["rewrite", "unwrite", "inwrite", "forwrite"], 0),
    ("Which is the plural form of <b>mouse</b>?", ["mouses", "mice", "mices", "mouse"], 1),
]
jumble = [("USEHO", "we live in it", "HOUSE"), ("HELTENAP", "the biggest land animal; it has a trunk", "ELEPHANT")]
choose2 = [("The baby (sleep / sleeps) in a cradle.", "sleeps"), ("Neha is happy (because / but) she won the race.", "because")]
fill3 = (["neatly", "tiger", "climbed"],
         ["The ______ roared loudly inside the cage.",
          "Meera writes ______ in her notebook.",
          "The monkey ______ up the tree in a second."],
         ["tiger", "neatly", "climbed"])
choose5 = [("He (is / are / were) my best friend.", "is"),
           ("The sun (rises / rose / rising) in the east every day.", "rises"),
           ("She walked (across / between / under) the road to reach the shop.", "across"),
           ("I (rarely / always / often) eat sweets because the doctor has told me to avoid sugar.", "rarely"),
           ("Two of my friends (is / are) coming to tea.", "are")]
cloze = ("Our class went to Amer Fort by (1)______. The fort stands on a (2)______, so we (3)______ many steps to reach the top. Everybody took (4)______ of the beautiful palace.",
         ["hungry", "hill", "photos", "bus", "stairs", "climbed"], ["bus", "hill", "climbed", "photos"])
match = (["A carrot", "Milk", "Soap", "Sleeping early at night", "Water"],
         ["removes germs from our hands", "quenches our thirst", "helps us wake up fresh and active", "is good for our eyesight", "gives calcium for strong bones and teeth"],
         ["(d)", "(e)", "(a)", "(c)", "(b)"])
arts = [("We saw ______ eagle sitting on the cliff.", "an"), ("______ moon is shining brightly tonight.", "The")]

A = ("India is like a big garden with flowers of many colours. In Rajasthan, men wear bright turbans and women wear lehengas with mirror work. In Kerala, people enjoy a feast on banana leaves during Onam. "
     "In Punjab, farmers dance the bhangra to welcome the new crop at Baisakhi, and in Assam, the Bihu dance fills the villages with joy. We speak many languages, eat different foods and follow different customs. "
     "Yet, when the tricolour is raised on Independence Day, we all stand together with pride. A teacher once told her class that a rainbow looks beautiful because it has many colours. "
     "In the same way, India looks beautiful because of its many cultures. We should respect every language and festival, and never laugh at anyone&rsquo;s dress or food.")
readA = (A, "The Colours of Our Country", [
    [("What do the men and women of Rajasthan wear, according to the passage?", "Men wear bright turbans and women wear lehengas with mirror work.", 2),
     ("What do people of Kerala enjoy during Onam?", "They enjoy a feast served on banana leaves.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>sadness</i>.", "joy", 1)],
    [("Why do farmers of Punjab dance the bhangra at Baisakhi?", "They dance to welcome the new crop.", 2),
     ("In what ways are the people of India different from one another?", "They speak many languages, eat different foods and follow different customs.", 2),
     ("Find a word from the passage that means <i>happy and satisfied with oneself or one&rsquo;s country</i>.", "pride", 1)],
    [("Why does a rainbow look beautiful, according to the teacher?", "It looks beautiful because it has many colours.", 2),
     ("What should we never do, and what should we do?", "We should never laugh at anyone&rsquo;s dress or food; we should respect every language and festival.", 2),
     ("Write the plural form of <b>language</b>.", "languages", 1)]])

B = ("In a green forest lived a crow named Kaalu. He was clever, but he was also very selfish. Every day he collected seeds and hid them in a hole in an old tree. "
     "When the sparrows asked him for a few seeds, Kaalu shouted, &ldquo;Go away! These are all mine!&rdquo; One summer, a heavy storm broke the tree and the rain washed all the seeds away. "
     "Kaalu was left with nothing. He sat on a branch, feeling hungry and sad. The sparrows saw him and felt sorry. They flew to him with a few seeds each and put them before him. "
     "Kaalu was ashamed. &ldquo;I did not share with you, yet you are sharing with me,&rdquo; he said. From that day, he never hid food again. He shared everything with his friends, and he was never lonely.")
readB = (B, "Kaalu the Crow", [
    [("Where did Kaalu keep the seeds he collected?", "He hid them in a hole in an old tree.", 2),
     ("What did Kaalu say when the sparrows asked for some seeds?", "He shouted, &ldquo;Go away! These are all mine!&rdquo;", 2),
     ("Find a word from the passage that means <i>thinking only about oneself</i>.", "selfish", 1)],
    [("What happened to the seeds during the storm?", "The storm broke the tree and the rain washed all the seeds away.", 2),
     ("How did the sparrows help Kaalu?", "They felt sorry for him and brought a few seeds each and put them before him.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>proud</i> (feeling that one has done wrong).", "ashamed", 1)],
    [("Why was Kaalu ashamed?", "He had not shared with the sparrows, but they shared with him.", 2),
     ("What lesson does the story teach us?", "We should share what we have with others.", 2),
     ("Write the past tense of <b>hide</b>.", "hid", 1)]])

letter = Q("You are Tanvi/Tarun of Class V, Vidya Bharti School, Bhilwara. Write a <b>letter</b> to your cousin telling him/her about the Annual Day celebrated in your school last Friday.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Points:</i> address and date; Dear cousin; opening enquiry; when and where the Annual Day was held; programmes (songs, dance, play), chief guest, prizes; what you liked best; invitation next year; closing (Your loving cousin, name).",
    alt=Q("Write an <b>application</b> to your class teacher requesting permission to leave school early at 12 noon because you have to visit a dentist.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Sample:</i> To, The Class Teacher, Class V, Vidya Bharti School, Bhilwara. Date: 3 Sept 2026. Subject: Application for early leave. Respected Madam, I beg to say that I have an appointment with the dentist at 1 p.m. today. "
    "Kindly allow me to leave school at 12 noon. Thanking you. Yours obediently, Tarun, Class V."))

scene = "<div style='font-size:26px;line-height:1.35'>🌾 &nbsp;🌻 &nbsp;🚜 &nbsp;👨‍🌾 &nbsp;🐄 &nbsp;🐓<br>🏡 &nbsp;🌳 &nbsp;🐐 &nbsp;🪣 &nbsp;☀️ &nbsp;🐑</div>"
pic = Q("Look at the picture of a farm. Write <b>four</b> sentences about it. (2 marks each)", 8,
    "<b>Any four correct sentences, 2 marks each (1 for content, 1 for grammar).</b><br><i>Sample:</i> A farmer is standing in the field. A tractor is parked near the crops. A cow, a goat and a sheep are eating grass. A hen is walking near the house. (Also: Sunflowers are blooming; the sun is shining.)",
    fig=scene,
    alt=Q("Complete the story using the words given: <i>lion, mouse, net, teeth, friends</i>.<br>A little mouse once lived near a lion&rsquo;s cave &hellip;", 8,
    "<b>Marking: sense 3 + use of the five words 3 + language 2.</b><br><i>Sample:</i> A little mouse once lived near a lion&rsquo;s cave. One day, the lion was caught in a hunter&rsquo;s net and roared in fear. The mouse heard him and ran there. With her sharp teeth she cut the ropes of the net. The lion was free and thanked her. From that day, they became good friends."))

make(4, lex, jumble, choose2, fill3, choose5, cloze, match, arts, readA, readB, letter, pic)
