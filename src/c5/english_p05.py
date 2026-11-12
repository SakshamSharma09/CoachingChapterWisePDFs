from english_common import *

lex = [
    ("The teacher praised Ritu and ______ for our neat work.", ["I", "me", "my", "mine"], 1),
    ("Look! The baby ______ at the pictures.", ["laughs", "is laughing", "laughed", "laugh"], 1),
    ("Choose the word closest in meaning to <b>glad</b>.", ["angry", "happy", "tired", "afraid"], 1),
    ("Choose the word opposite in meaning to <b>rough</b>.", ["hard", "thick", "smooth", "heavy"], 2),
    ("In which word does the underlined <b>ea</b> sound different from the others?", ["br<u>ea</u>d", "h<u>ea</u>d", "t<u>ea</u>m", "r<u>ea</u>dy"], 2),
    ("Which is the correctly spelt word formed by adding the suffix <b>-ly</b> to <b>quick</b>?", ["quickly", "quickely", "quicklly", "quickily"], 0),
    ("Choose the word that sounds like <b>hear</b> but has a different spelling and meaning.", ["here", "hair", "heard", "hare"], 0),
]
jumble = [("SLSAC", "children of the same age study in it together", "CLASS"), ("WOLFER", "it blooms in a garden and smells sweet", "FLOWER")]
choose2 = [("The child (laughed / laugh) loudly at the joke.", "laughed"), ("I have (much / many) friends in my class.", "many")]
fill3 = (["computer", "switch", "slowly"],
         ["My father works on a ______ in his office.",
          "Please ______ off the fan before leaving the room.",
          "The snail moves very ______ on the wall."],
         ["computer", "switch", "slowly"])
choose5 = [("Neha (didn&rsquo;t / don&rsquo;t / doesn&rsquo;t) like bitter gourd.", "doesn&rsquo;t"),
           ("I will call you (yesterday / tomorrow / last week).", "tomorrow"),
           ("The monkey jumped (over / under / into) the wall.", "over"),
           ("The Sun (always / sometimes / never) rises in the east.", "always"),
           ("Ram and Shyam (is / are / was) brothers.", "are")]
cloze = ("My grandmother lives in an old (1)______ near Lake Pichola in Udaipur. Every evening she sits on the (2)______ and waters her pots. She grows roses, jasmine and (3)______. "
         "After the first rain, the garden smells (4)______.",
         ["sweet", "balcony", "tunnel", "haveli", "bitter", "marigolds"], ["haveli", "balcony", "marigolds", "sweet"])
match = (["A doctor", "A pilot", "A farmer", "A tailor", "A librarian"],
         ["flies an aeroplane", "stitches clothes", "looks after the books", "treats sick people", "grows wheat and vegetables"],
         ["(d)", "(a)", "(e)", "(b)", "(c)"])
arts = [("My brother wants to become ______ engineer.", "an"), ("Kabir is ______ best singer in our school.", "the")]

A = ("My grandfather, Dadaji, lives in a village near Sikar. He had never seen a smartphone until last year. When my father gave him one, he held it carefully, as if it were made of glass. "
     "I taught him to touch the green button and see his family on the screen. On Diwali, my aunt in Mumbai called him on video. Dadaji saw her face and the lit lamps behind her, and he laughed with joy. "
     "&ldquo;It is like she is sitting in my room,&rdquo; he said. Now he video calls us every evening and shows us his cows. Technology can bring faraway people close, but it must be used wisely. "
     "That is why my mother allows us only one hour a day on the phone, and Dadaji says, &ldquo;Even a good friend must not be allowed to stay too long.&rdquo;")
readA = (A, "Dadaji&rsquo;s First Video Call", [
    [("Where does Dadaji live, and what had he never seen until last year?", "He lives in a village near Sikar; he had never seen a smartphone.", 2),
     ("How did Dadaji hold the phone when he first got it? Why?", "He held it carefully, as if it were made of glass.", 2),
     ("Find a word from the passage that means <i>far away</i>.", "faraway", 1)],
    [("Who called Dadaji on Diwali, and what did he see?", "His aunt from Mumbai called; he saw her face and the lit lamps behind her.", 2),
     ("What did Dadaji say about the video call?", "He said, &ldquo;It is like she is sitting in my room.&rdquo;", 2),
     ("Write the word from the passage that is opposite in meaning to <i>carelessly</i>.", "carefully", 1)],
    [("What does Dadaji do every evening now?", "He video calls the family and shows them his cows.", 2),
     ("Why does the writer&rsquo;s mother allow only one hour a day on the phone?", "Because technology must be used wisely and not for too long.", 2),
     ("Write the plural form of <b>family</b>.", "families", 1)]])

B = ("A marigold grew in the corner of a big garden, between a rosebush and a jasmine creeper. Every morning she saw people stop to smell the roses and say, &ldquo;How lovely!&rdquo; Nobody looked at her. "
     "&ldquo;I wish I were a rose,&rdquo; she sighed. One day, an old gardener named Hari Kaka came with a basket. He plucked the marigold&rsquo;s golden flowers one by one. "
     "&ldquo;Tomorrow is Dussehra,&rdquo; he said, &ldquo;and these flowers will make garlands for the temple and for the doors of the houses.&rdquo; The next morning, the marigold looked at the garden. "
     "The roses stood alone on their stems, but the whole town was smiling under her golden garlands. A little bee whispered to her, &ldquo;Every flower has a special work. Do not wish to be someone else.&rdquo; "
     "From that day, the marigold was happy with her own colour and her own fragrance.")
readB = (B, "The Marigold&rsquo;s Wish", [
    [("Where did the marigold grow in the garden?", "She grew in a corner of the garden between a rosebush and a jasmine creeper.", 2),
     ("What did the marigold wish, and why?", "She wished to be a rose because people stopped to smell the roses and nobody looked at her.", 2),
     ("Find a word from the passage that means <i>made a long, sad breath</i>.", "sighed", 1)],
    [("Why did Hari Kaka pluck the marigold flowers?", "Because the next day was Dussehra and the flowers were needed for garlands for the temple and the doors of houses.", 2),
     ("What did the whole town look like the next morning?", "The whole town was smiling under the golden garlands.", 2),
     ("Write the word from the passage that is opposite in meaning to <i>young</i>.", "old", 1)],
    [("What did the little bee tell the marigold?", "The bee said that every flower has a special work and she should not wish to be someone else.", 2),
     ("How did the marigold feel at the end?", "She was happy with her own colour and fragrance.", 2),
     ("Write the singular form of <b>roses</b>.", "rose", 1)]])

letter = Q("You are Kavya/Kunal of Class V, Government Model School, Sikar. Write an <b>application</b> to the Principal requesting that a computer class be started in your school once a week.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Sample:</i> To, The Principal, Government Model School, Sikar. Date: 20 Jan 2027. Subject: Request to start a computer class. Respected Sir/Madam, "
    "With due respect I wish to say that students of Class V are very interested in computers, but we do not have a class for them. Kindly start a computer class once a week so that we can learn typing and drawing. "
    "Thanking you. Yours obediently, Kunal, Class V.",
    alt=Q("Write a <b>letter</b> to your pen-friend Joseph, telling him about yourself, your family and your hobbies.", 8,
    "<b>Marking: format 2 + content 4 + language 2.</b><br><i>Points:</i> address and date; Dear Joseph; your name, age, class and school; family members; hobbies (reading, cricket, drawing); favourite food or festival; request him to write back; closing (Your friend, name)."))

scene = "<div style='font-size:26px;line-height:1.35'>🎡 &nbsp;🎈🎈 &nbsp;🐪 &nbsp;🎪 &nbsp;🍦 &nbsp;🥁<br>👫 &nbsp;👴 &nbsp;🧒 &nbsp;🍭 &nbsp;🚩 &nbsp;🎠</div>"
pic = Q("Look at the picture of a fair. Write <b>four</b> sentences about it. (2 marks each)", 8,
    "<b>Any four correct sentences, 2 marks each (1 for content, 1 for grammar).</b><br><i>Sample:</i> There is a big wheel at the fair. A camel is standing near the tent. A boy is buying an ice cream. Some balloons are flying in the air. (Also: A drummer is playing a drum; a flag is flying; a merry-go-round is moving.)",
    fig=scene,
    alt=Q("Complete the story using the words given: <i>lamp, village, night, light, proud</i>.<br>In a small village there was no electricity &hellip;", 8,
    "<b>Marking: sense 3 + use of the five words 3 + language 2.</b><br><i>Sample:</i> In a small village there was no electricity. At night the roads were very dark. A girl named Gauri placed a small lamp outside every house. The light helped everyone to walk safely. The villagers were proud of her and called her &lsquo;Deepa&rsquo;."))

make(5, lex, jumble, choose2, fill3, choose5, cloze, match, arts, readA, readB, letter, pic)
