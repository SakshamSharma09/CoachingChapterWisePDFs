from english_common import *

lex = [
    ("The sun sets ______ the evening.", ["on", "at", "in", "with"], 2),
    ("Yesterday, Seema ______ her homework before dinner.", ["finish", "finishes", "finished", "finishing"], 2),
    ("Choose the word closest in meaning to <b>huge</b>.", ["tiny", "enormous", "narrow", "soft"], 1),
    ("Choose the word opposite in meaning to <b>brave</b>.", ["strong", "cowardly", "clever", "kind"], 1),
    ("In which word does the underlined <b>ch</b> sound different from the others?", ["<u>ch</u>air", "<u>ch</u>eese", "s<u>ch</u>ool", "<u>ch</u>alk"], 2),
    ("Which prefix gives the opposite of the word <b>possible</b>?", ["un-", "im-", "dis-", "mis-"], 1),
    ("Choose the word that sounds like <b>night</b> but has a different spelling and meaning.", ["knight", "light", "nice", "name"], 0),
]
jumble = [("NECPIL", "you write with it", "PENCIL"), ("RGBEID", "it is built over a river so that people can cross", "BRIDGE")]
choose2 = [("She is the (tallest / taller) girl in the class.", "tallest"), ("Riya (and / but) Anil are cousins.", "and")]
fill3 = (["gardener", "beautifully", "plucked"],
         ["The ______ watered all the plants in the evening.",
          "Kavya sings ______ at every school function.",
          "Grandma ______ fresh flowers for the puja yesterday."],
         ["gardener", "beautifully", "plucked"])
choose5 = [("There (is / are) a book on the desk.", "is"),
           ("My brother (was / were) ill last week.", "was"),
           ("The farmer is going (to / at / on) the field.", "to"),
           ("We drink milk (every day / yesterday / tomorrow) because it keeps our bones strong.", "every day"),
           ("Both the boys (have / has) won prizes.", "have")]
cloze = ("On 5 September, our class celebrated (1)______ Day. We decorated the board with (2)______ and wrote &lsquo;Thank You&rsquo; in big letters. "
         "Rohit made a (3)______ for our teacher, and the girls sang a (4)______ in chorus.",
         ["card", "bench", "Teachers&rsquo;", "song", "flowers", "holiday"], ["Teachers&rsquo;", "flowers", "card", "song"])
match = (["The red light", "The green light", "The yellow light", "A footpath", "A seat belt"],
         ["tells us to get ready", "is meant for people who walk", "tells vehicles to stop", "is worn inside a car", "tells vehicles to go"],
         ["(c)", "(e)", "(a)", "(b)", "(d)"])
arts = [("______ honest man returned the wallet to its owner.", "An"), ("______ Himalayas are in the north of India.", "The")]

A = ("Savita Ma&rsquo;am teaches Class V in a small school in Jodhpur. She never comes to class empty-handed. Some days she brings a story, on other days a puzzle or a leaf from her garden. "
     "When a child is weak in reading, she sits beside him and reads slowly with him. On 5 September, we celebrate Teachers&rsquo; Day because it is the birthday of Dr Sarvepalli Radhakrishnan, "
     "a great scholar and teacher who later became the second President of India. This year, our class secretly made a big card for Savita Ma&rsquo;am. Every child wrote one thing "
     "that she had taught us. When she read the card, her eyes filled with tears. &ldquo;The best gift for a teacher,&rdquo; she said, &ldquo;is a student who learns and is kind to others.&rdquo;")
readA = (A, "Our Teacher", [
    [("Where does Savita Ma&rsquo;am teach, and which class?", "She teaches Class V in a small school in Jodhpur.", 2),
     ("What does she bring to class on different days?", "She brings a story, a puzzle or a leaf from her garden.", 2),
     ("Find a word from the passage that means <i>learned person</i>.", "scholar", 1)],
    [("Why is Teachers&rsquo; Day celebrated on 5 September?", "It is the birthday of Dr Sarvepalli Radhakrishnan, a great teacher who became the second President of India.", 2),
     ("How does Savita Ma&rsquo;am help a child who is weak in reading?", "She sits beside the child and reads slowly with him.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>big</i>.", "small", 1)],
    [("What did the class make for Savita Ma&rsquo;am, and what did every child write on it?", "They made a big card; every child wrote one thing she had taught them.", 2),
     ("According to Savita Ma&rsquo;am, what is the best gift for a teacher?", "A student who learns and is kind to others.", 2),
     ("Write the plural form of <b>child</b>.", "children", 1)]])

B = ("It was raining hard when Imran was returning from the market lane to his house in Udaipur. Near the gate of a temple he heard a weak cry. Under a broken cart sat a tiny brown puppy, "
     "shivering with cold and wet from head to tail. Imran looked around, but nobody was there. He took off his jacket, wrapped the puppy in it and carried it home. "
     "His mother gave the puppy a little warm milk and dried it with a soft cloth. Imran made a bed for it in an old basket. &ldquo;We cannot keep him forever,&rdquo; said his mother, &ldquo;but we can look after him until he is strong.&rdquo; "
     "After a week, the puppy was running around the house. A neighbour, Mrs Kapoor, who had no pet, asked if she could adopt him. Imran agreed happily. He visits his little friend every evening.")
readB = (B, "The Puppy Under the Cart", [
    [("Where did Imran find the puppy, and in what condition was it?", "He found it under a broken cart near the gate of a temple, wet and shivering with cold.", 2),
     ("What did Imran do to keep the puppy warm?", "He wrapped the puppy in his jacket and carried it home.", 2),
     ("Find a word from the passage that means <i>trembling</i> (because of cold).", "shivering", 1)],
    [("How did Imran&rsquo;s mother help the puppy?", "She gave it warm milk and dried it with a soft cloth.", 2),
     ("What did Imran&rsquo;s mother say about keeping the puppy?", "She said they could not keep him forever but could look after him until he was strong.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>strong</i> (describing the cry).", "weak", 1)],
    [("What happened after a week?", "The puppy was running around the house.", 2),
     ("Who adopted the puppy in the end, and why was Imran happy?", "Mrs Kapoor adopted him; Imran was happy because the puppy would have a home and he could visit him every evening.", 2),
     ("Write the past tense of <b>take</b> (see &lsquo;He ___ off his jacket&rsquo;).", "took", 1)]])

letter = Q("You are Aarav/Aarti, a student of Class V, Government Senior Primary School, Alwar. The swings in your school playground are broken. Write an <b>application</b> to the Headmaster requesting him to get them repaired.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Sample:</i> To, The Headmaster, Government Senior Primary School, Alwar. Date: 10 Aug 2026. Subject: Request to repair the swings. Respected Sir, "
    "With due respect I wish to say that the swings in our playground have been broken for a month and the children cannot play safely. Some children may get hurt. Kindly get them repaired soon. "
    "Thanking you. Yours obediently, Aarav, Class V.",
    alt=Q("Write a <b>letter</b> to your grandfather thanking him for the storybook he sent you on your birthday.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Points:</i> address and date; Respected Grandpa/Dear Dadaji; thanks for the book; what you liked in it; how you are doing in school; promise to visit; regards to Grandma; closing (Your loving grandson/granddaughter, name)."))

scene = "<div style='font-size:26px;line-height:1.35'>🏫 &nbsp;👩‍🏫 &nbsp;🧒 &nbsp;👧 &nbsp;📚 &nbsp;✏️<br>🖍️ &nbsp;🎒 &nbsp;🪑 &nbsp;🌐 &nbsp;⏰ &nbsp;🗑️</div>"
pic = Q("Look at the picture of a classroom. Write <b>four</b> sentences about it. (2 marks each)", 8,
    "<b>Any four correct sentences, 2 marks each (1 for content, 1 for grammar).</b><br><i>Sample:</i> The teacher is standing in the classroom. Two children are sitting on chairs. There are many books and pencils on the desk. A clock and a globe are in the room. (Also: A school bag is kept near the desk; a dustbin is in the corner.)",
    fig=scene,
    alt=Q("Complete the story using the words given: <i>peacock, forest, thirsty, river, water</i>.<br>A peacock lived in a dry forest &hellip;", 8,
    "<b>Marking: sense 3 + use of the five words 3 + language 2.</b><br><i>Sample:</i> A peacock lived in a dry forest. One hot day he felt very thirsty, but all the ponds were empty. He flew far and at last saw a river. He drank cool water and told all the other birds about it. The birds thanked him and drank water happily."))

make(3, lex, jumble, choose2, fill3, choose5, cloze, match, arts, readA, readB, letter, pic)
