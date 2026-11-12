from english_common import *

lex = [
    ("Meena found her pencil box, but Sohan could not find ______.", ["her", "his", "hers", "them"], 1),
    ("My father ______ a newspaper every morning.", ["read", "reads", "reading", "are reading"], 1),
    ("Choose the word closest in meaning to <b>quick</b>.", ["slow", "fast", "late", "lazy"], 1),
    ("Choose the word opposite in meaning to <b>empty</b>.", ["full", "clean", "light", "wide"], 0),
    ("Which word is an adjective in this sentence? <i>The tired farmer drank water.</i>", ["tired", "farmer", "drank", "water"], 0),
    ("When the suffix <b>-less</b> is added to <b>hope</b>, the new word means:", ["full of hope", "without hope", "hoping again", "not hoping yet"], 1),
    ("Which is the plural form of <b>sheep</b>?", ["sheeps", "sheep", "sheepes", "sheepies"], 1),
]
jumble = [("RAEWT", "we drink it and use it for bathing", "WATER"), ("KSOOB", "we read them; there are many in a library", "BOOKS")]
choose2 = [("The Ganga is longer (than / then) the Yamuna.", "than"), ("Divya is very good (at / on) drawing.", "at")]
fill3 = (["carefully", "mango", "shouted"],
         ["The ripe ______ fell from the tree with a thud.",
          "Raju carried the glass jar ______ so that it would not break.",
          "The coach ______ &ldquo;Run faster!&rdquo; to the players yesterday."],
         ["mango", "carefully", "shouted"])
choose5 = [("I (am / is / are) eating a banana.", "am"),
           ("They (play / plays / played) cricket yesterday.", "played"),
           ("The bag is (in / on / at) the table.", "on"),
           ("She (sometimes / yesterday / tomorrow) visits her grandmother on Sundays.", "sometimes"),
           ("Each of the girls (has / have) a notebook.", "has")]
cloze = ("In July, heavy (1)______ filled the pond near our house. At night the frogs began to (2)______ loudly. In the morning, the children floated paper (3)______ on the water. "
         "My mother said we must keep the pond (4)______ so that nobody falls sick.",
         ["boats", "dirty", "rain", "swim", "clean", "croak"], ["rain", "croak", "boats", "clean"])
match = (["A dustbin", "A comb", "A mosquito net", "A nail cutter", "A handkerchief"],
         ["protects us from bites while we sleep", "keeps nails short and clean", "keeps our hair neat", "is used for throwing waste", "is used to cover the nose while sneezing"],
         ["(d)", "(c)", "(a)", "(b)", "(e)"])
arts = [("Aarti has ______ uncle in Pune.", "an"), ("______ Ganga is a holy river.", "The")]

A = ("The Chambal is one of the cleanest rivers of India. It begins in Madhya Pradesh, flows through Rajasthan and finally joins the Yamuna. The city of Kota stands on its bank. "
     "Farmers use its water to grow wheat and mustard, and its dams give us electricity. Very few factories stand along the river, and the villagers do not dump waste into it. "
     "That is why rare animals such as the gharial, a crocodile with a long, thin snout, and the river dolphin live in its water. Every year, the children of Kota gather on the river bank "
     "to clear plastic bags and bottles. They say that a clean river is a gift we must protect.")
readA = (A, "A Clean River", [
    [("Where does the Chambal begin and which river does it join?", "It begins in Madhya Pradesh and joins the Yamuna.", 2),
     ("Name any two uses of the Chambal&rsquo;s water mentioned in the passage.", "Farmers use it to grow wheat and mustard; its dams give electricity.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>common</i>.", "rare", 1)],
    [("Which two animals live in the water of the Chambal?", "The gharial and the river dolphin.", 2),
     ("Why is the Chambal one of the cleanest rivers?", "Very few factories stand along it and the villagers do not dump waste into it.", 2),
     ("Write the plural form of <b>city</b>.", "cities", 1)],
    [("What do the children of Kota do every year?", "They gather on the river bank to clear plastic bags and bottles.", 2),
     ("What do the children say a clean river is?", "They say a clean river is a gift we must protect.", 2),
     ("Find a word in the passage that means <i>to throw away carelessly</i>.", "dump", 1)]])

B = ("One morning, the children of Class V noticed a sparrow carrying small twigs to a corner of the school verandah, just above the old fan. She was building a nest. "
     "Their teacher, Mrs Joshi, asked them not to switch on that fan, because its blades could hurt the little birds. For many days the children kept a bowl of water and some grains of rice on a stool nearby, "
     "and they watched from a distance without making any noise. After two weeks, three tiny eggs hatched into chicks. The mother sparrow flew in and out all day to feed them. "
     "In a few more weeks, the chicks learnt to fly and left the nest. The children were a little sad, but they were glad that they had helped. Mrs Joshi smiled and said, &ldquo;Kindness is never wasted.&rdquo;")
readB = (B, "The Sparrow in the Verandah", [
    [("What did the children notice one morning?", "They noticed a sparrow carrying twigs to build a nest in a corner of the verandah above the fan.", 2),
     ("Why did Mrs Joshi ask the children not to switch on the fan?", "The blades of the fan could hurt the little birds in the nest.", 2),
     ("Find a word from the passage that means <i>small pieces of a dry branch</i>.", "twigs", 1)],
    [("How did the children help the sparrow?", "They kept a bowl of water and some grains of rice nearby and watched quietly from a distance.", 2),
     ("What happened after two weeks?", "Three tiny eggs hatched into chicks.", 2),
     ("Write the singular form of <b>chicks</b>.", "chick", 1)],
    [("What did the chicks do in a few more weeks?", "They learnt to fly and left the nest.", 2),
     ("How did the children feel when the chicks left? Why?", "They were a little sad but glad, because they had helped the birds.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>huge</i>.", "tiny", 1)]])

letter = Q("You are Sneha/Sumit of Class V, Government Upper Primary School, Ajmer. Write a <b>letter</b> to your friend Mahi describing the village fair you visited last Sunday with your family.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Points:</i> sender&rsquo;s address and date; Dear Mahi; opening line; what you saw (swings, camel rides, sweets, puppet show); with whom you went; what you liked best; invitation to come next year; closing (Your loving friend, name).",
    alt=Q("You are Sumit/Sneha of Class V. Write an <b>application</b> to the Principal for one day&rsquo;s leave because you have to attend your cousin&rsquo;s wedding.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Sample:</i> To, The Principal, Government Upper Primary School, Ajmer. Date: 5 Dec 2026. Subject: Application for one day&rsquo;s leave. Respected Sir/Madam, "
    "I beg to state that my cousin&rsquo;s wedding is on 7 December and my family has to travel to Beawar. Kindly grant me leave for one day. Thanking you. Yours obediently, Sumit, Class V."))

scene = "<div style='font-size:26px;line-height:1.35'>🏪 &nbsp;🍎🍌🥭 &nbsp;👨‍🍳 &nbsp;🛒 &nbsp;👩 &nbsp;🧒<br>🐄 &nbsp;🚲 &nbsp;🧺 &nbsp;☂️ &nbsp;🐈</div>"
pic = Q("Look at the picture of a market. Write <b>four</b> sentences about it. (2 marks each)", 8,
    "<b>Any four correct sentences, 2 marks each (1 for content, 1 for grammar).</b><br><i>Sample:</i> There is a fruit shop in the market. Apples, bananas and mangoes are kept on the stall. A woman is pushing a shopping trolley. A cow and a cat are standing near the road. (Also: A child is with his mother; a man is riding a bicycle.)",
    fig=scene,
    alt=Q("Complete the story using the words given: <i>rain, umbrella, puddle, mother, laughed</i>.<br>It was raining heavily when Pinky came out of school &hellip;", 8,
    "<b>Marking: sense 3 + use of the five words 3 + language 2.</b><br><i>Sample:</i> It was raining heavily when Pinky came out of school. She had forgotten her umbrella. Just then her mother arrived with a big umbrella. On the way home Pinky jumped into a puddle and splashed her mother. They both laughed and walked home happily."))

make(2, lex, jumble, choose2, fill3, choose5, cloze, match, arts, readA, readB, letter, pic)
