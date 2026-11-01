"""Class 5 reading sets 6-10 (original)."""
from eng9_lib import P, S
def m(q, o): return S(q, "a", 1, o)
TF = "State whether True or False: "
SETS = {}
T1 = "Read the passage carefully and answer the questions that follow."
T2 = "Read the story carefully and answer the questions that follow."

SETS[6] = dict(
P1=P("""<p>Mahatma Gandhi was born on 2 October 1869 in Porbandar, Gujarat. As a boy, he was shy and honest. He studied law in London and later worked in South Africa, where he saw how unfairly Indians were treated.</p>
<p>After returning to India, Gandhiji led the people in the freedom struggle. He believed in truth and non-violence. He never used weapons; instead he used peaceful ways like fasting and marches. The Dandi March of 1930, in which he walked to the sea to make salt, is very famous.</p>
<p>India became free on 15 August 1947. Gandhiji is lovingly called 'Bapu' or the Father of the Nation. His birthday, 2 October, is celebrated as Gandhi Jayanti all over India.</p>""",
[m("Gandhiji was born in:", ["Porbandar", "Delhi", "Mumbai", "Ahmedabad"]),
 m("He studied law in:", ["London", "Paris", "Delhi", "Cape Town"]),
 m("Gandhiji believed in truth and:", ["non-violence", "weapons", "anger", "money"]),
 m("The Dandi March was held to make:", ["salt", "sugar", "cloth", "rice"]),
 m("India became free in:", ["1947", "1930", "1869", "1950"]),
 S("When was Gandhiji born?", "On 2 October 1869.", 1),
 S("Why did Gandhiji feel sad in South Africa?", "He saw that Indians were treated unfairly.", 1),
 S(TF + "Gandhiji fought for freedom with weapons.", "False.", 1),
 S("By what name do people lovingly call Gandhiji?", "Bapu (Father of the Nation).", 1),
 S("Find a word in the passage which means 'quiet and not bold'.", "Shy.", 1)], title=T1),
P2=P("""<p>A greedy dog once found a big bone. He picked it up and ran towards home to eat it in peace. On the way, he had to cross a small bridge over a stream.</p>
<p>As he walked on the bridge, he looked down and saw another dog in the water. That dog also had a bone in his mouth. The greedy dog thought, "His bone looks bigger than mine. I will take it too!"</p>
<p>He opened his mouth and barked loudly at the dog in the water. At once his own bone fell into the stream with a splash and sank. The other dog in the water was only his own shadow. The poor dog had lost everything because of greed. He went home hungry and sad.</p>""",
[m("The dog found a:", ["big bone", "piece of bread", "fish", "ball"]),
 m("He was crossing a:", ["bridge", "road", "field", "gate"]),
 m("The dog in the water was actually his:", ["shadow", "friend", "brother", "enemy"]),
 m("His bone fell into the stream when he:", ["barked", "slipped", "ran", "slept"]),
 m("At the end the dog felt:", ["sad and hungry", "happy", "proud", "angry"]),
 S("Why did the dog want the other bone?", "It looked bigger than his own.", 1),
 S("What sound came when the bone fell?", "A splash.", 1),
 S(TF + "The dog got two bones.", "False.", 1),
 S("Find a word in the story which means 'wanting more than you need'.", "Greedy / greed.", 1),
 S("What does the story teach us?", "We should not be greedy; greed makes us lose what we have.", 1)], title=T2),
)

SETS[7] = dict(
P1=P("""<p>Our body needs food to grow strong. But all foods are not equally good. Some foods, like fruits, vegetables, milk, pulses and eggs, are healthy. Others, like chips, cold drinks and sweets, give us only sugar and fat. If we eat too much of them, we become weak and fat.</p>
<p>A healthy meal has many colours. Green vegetables give us iron, oranges give us vitamin C, and milk gives us calcium for strong bones. We should drink at least eight glasses of water a day.</p>
<p>Good habits keep us fit. We should wash our hands before eating, chew food well and eat at fixed times. A little exercise or play every day also keeps our body active. Remember, a healthy body keeps the mind happy.</p>""",
[m("Which of these is a healthy food?", ["Milk", "Chips", "Cold drinks", "Candy"]),
 m("Calcium for strong bones comes from:", ["milk", "oranges", "chips", "tea"]),
 m("Oranges give us:", ["vitamin C", "iron", "calcium", "sugar"]),
 m("We should drink at least ______ glasses of water a day.", ["eight", "two", "four", "twenty"]),
 m("Before eating we should:", ["wash our hands", "run", "sleep", "drink tea"]),
 S("What happens if we eat too many chips and sweets?", "We become weak and fat.", 1),
 S("Why should a healthy meal have many colours?", "Different foods give different things the body needs.", 1),
 S(TF + "Exercise keeps the body active.", "True.", 1),
 S("Name two foods that are healthy.", "Fruits, vegetables, milk, pulses, eggs (any two).", 1),
 S("Find a word in the passage that means 'in good health'.", "Fit / healthy.", 1)], title=T1),
P2=P("""<p class='h'>My School Bag</p>
<p>My bag is blue and big,<br>With pockets here and there.<br>It holds my books and pencil box,<br>And a little bear.</p>
<p>It goes with me to school each day,<br>On my back so snug,<br>My lunch box sits inside it too,<br>Packed with mother's hug.</p>
<p>When school is done I run back home,<br>And put it by the door.<br>Tomorrow it will come again,<br>With me to learn once more.</p>""",
[m("The colour of the bag is:", ["blue", "red", "green", "black"]),
 m("The bag holds books and a:", ["pencil box", "football", "doll", "kite"]),
 m("The lunch box is packed by:", ["mother", "father", "teacher", "sister"]),
 m("The child puts the bag:", ["by the door", "on the bed", "under the table", "on the roof"]),
 m("Where does the bag sit when the child goes to school?", ["on the back", "in the car", "in hand", "on the head"]),
 S("What toy is inside the bag?", "A little bear.", 1),
 S("What does 'packed with mother's hug' mean?", "The lunch is made with a mother's love.", 1),
 S(TF + "The child leaves the bag at school.", "False.", 1),
 S("Pick two rhyming words from the third stanza.", "door – more.", 1),
 S("Write the line that tells you the child will go to school again.", "Tomorrow it will come again, with me to learn once more.", 1)], title="Read the poem carefully and answer the questions that follow."),
)

SETS[8] = dict(
P1=P("""<p>Rajasthan is the largest state of India. It is a land of forts, palaces and colourful fairs. The Thar Desert covers a big part of the state, and the Aravalli Hills run across it from the south-west to the north-east.</p>
<p>The people of Rajasthan are known for their warm welcome. The men wear bright turbans and the women wear colourful ghagras and odhnis. Their folk songs and dances, like Ghoomar and Kalbelia, are loved by everyone.</p>
<p>Jaipur is the capital of Rajasthan and is called the 'Pink City'. Jodhpur is known as the 'Blue City' and Udaipur as the 'City of Lakes'. Tourists from all over the world come here to see the forts, enjoy the food and ride on camels.</p>""",
[m("The largest state of India is:", ["Rajasthan", "Gujarat", "Punjab", "Kerala"]),
 m("The desert in Rajasthan is the:", ["Thar", "Sahara", "Gobi", "Kalahari"]),
 m("The capital of Rajasthan is:", ["Jaipur", "Jodhpur", "Udaipur", "Ajmer"]),
 m("Udaipur is called the:", ["City of Lakes", "Pink City", "Blue City", "Golden City"]),
 m("Ghoomar is a:", ["folk dance", "festival", "fort", "food"]),
 S("What do the men of Rajasthan wear on their heads?", "Bright turbans.", 1),
 S("Name the hills that run across Rajasthan.", "The Aravalli Hills.", 1),
 S(TF + "Jodhpur is known as the Blue City.", "True.", 1),
 S("Why do tourists come to Rajasthan? Give one reason.", "To see the forts, enjoy the food, ride camels (any one).", 1),
 S("Find a word in the passage which means 'friendly greeting for guests'.", "Welcome.", 1)], title=T1),
P2=P("""<p>Ravi and Raju were best friends. They sat on the same bench and played together every day. One afternoon, they were walking home when they saw a big bear coming out of the forest.</p>
<p>Ravi quickly climbed up a tree and left Raju alone on the road. Raju did not know how to climb. He remembered that bears do not touch dead bodies, so he lay down on the ground and held his breath.</p>
<p>The bear came near, sniffed at Raju's ear and went away. Ravi came down and asked, "What did the bear whisper in your ear?" Raju replied, "He told me never to trust a friend who leaves you in danger."</p>""",
[m("Ravi and Raju were:", ["best friends", "brothers", "neighbours only", "cousins"]),
 m("They saw a bear coming out of the:", ["forest", "house", "school", "river"]),
 m("Ravi:", ["climbed a tree", "ran home", "stayed with Raju", "shouted"]),
 m("Raju lay on the ground and:", ["held his breath", "ran", "cried", "climbed"]),
 m("The bear:", ["went away", "attacked Raju", "ate a fruit", "followed Ravi"]),
 S("Why could Raju not climb the tree?", "He did not know how to climb.", 1),
 S("What did Ravi ask Raju?", "What did the bear whisper in your ear?", 1),
 S(TF + "Ravi was a true friend.", "False.", 1),
 S("Find a word in the story which means 'to smell something closely'.", "Sniffed.", 1),
 S("What did Raju learn from the bear's visit?", "Never to trust a friend who leaves you in danger.", 1)], title=T2),
)

SETS[9] = dict(
P1=P("""<p>Water on the Earth goes round and round. This is called the water cycle. The heat of the Sun warms the water of rivers, lakes and seas. The water turns into tiny drops of vapour and rises into the sky. This is called evaporation.</p>
<p>High up in the sky, the air is cold. The vapour cools down and becomes tiny drops of water that join together to make clouds. This is called condensation.</p>
<p>When the clouds become heavy, the water falls down as rain. In very cold places, it may fall as snow or hail. The rain water flows into rivers and seas, and the cycle starts again. Without the water cycle, there would be no rain, and no life on Earth.</p>""",
[m("The water cycle begins with the heat of the:", ["Sun", "Moon", "wind", "clouds"]),
 m("Water turning into vapour is called:", ["evaporation", "condensation", "rain", "freezing"]),
 m("Clouds are made of tiny drops of:", ["water", "smoke", "dust", "cotton"]),
 m("In very cold places water may fall as:", ["snow", "dew", "mist", "fog"]),
 m("Rain water finally flows into:", ["rivers and seas", "clouds", "the sun", "mountains"]),
 S("Why does the vapour cool down in the sky?", "The air high up in the sky is cold.", 1),
 S("What is condensation?", "Vapour cooling and turning into tiny drops of water to form clouds.", 1),
 S(TF + "There would be no rain without the water cycle.", "True.", 1),
 S("Find a word in the passage which means 'very small'.", "Tiny.", 1),
 S("Write the correct order: rain, evaporation, clouds.", "Evaporation, clouds, rain.", 1)], title=T1),
P2=P("""<p>Sita's grandmother lived in a village. Every summer holiday, Sita went there. She loved to run in the fields and eat fresh mangoes from the garden.</p>
<p>One day Grandmother said, "Today we will plant a mango seed." They dug a small hole and put the seed in it. Sita watered it every morning. Many days passed, but nothing happened. She became sad and said, "Dadi, will it ever grow?" Grandmother smiled, "Wait with patience, my child."</p>
<p>After two weeks, a tiny green shoot came out of the soil. Sita jumped with joy. She learned that good things take time. Years later, the little plant became a tall tree and gave sweet mangoes to the whole village.</p>""",
[m("Sita went to her grandmother's house during the:", ["summer holidays", "winter holidays", "Diwali", "exams"]),
 m("They planted a:", ["mango seed", "rose", "banana", "coconut"]),
 m("Sita watered the seed:", ["every morning", "every night", "once a week", "never"]),
 m("The shoot came out after:", ["two weeks", "two days", "one year", "ten minutes"]),
 m("The plant finally became a:", ["tall tree", "bush", "flower", "creeper"]),
 S("Why did Sita become sad?", "Nothing happened for many days.", 1),
 S("What did Grandmother tell her?", "Wait with patience, my child.", 1),
 S(TF + "Sita learned that good things take time.", "True.", 1),
 S("Find a word in the story which means 'a very small, young growth of a plant'.", "Shoot.", 1),
 S("How did the tree help the village?", "It gave sweet mangoes to the whole village.", 1)], title=T2),
)

SETS[10] = dict(
P1=P("""<p><b>SCHOOL TIME-TABLE — CLASS 5 (Monday)</b></p>
<table><tr><th>Period</th><th>Time</th><th>Subject</th></tr>
<tr><td>1</td><td>8:00 – 8:40</td><td>English</td></tr>
<tr><td>2</td><td>8:40 – 9:20</td><td>Mathematics</td></tr>
<tr><td>3</td><td>9:20 – 10:00</td><td>Hindi</td></tr>
<tr><td colspan="3"><i>Break: 10:00 – 10:30</i></td></tr>
<tr><td>4</td><td>10:30 – 11:10</td><td>Environmental Studies</td></tr>
<tr><td>5</td><td>11:10 – 11:50</td><td>Computer</td></tr>
<tr><td>6</td><td>11:50 – 12:30</td><td>Games</td></tr></table>
<p>School ends at 12:30 p.m. Students should bring their own water bottles. The English teacher will conduct a spelling test in the first period every Monday.</p>""",
[m("The first period is:", ["English", "Hindi", "Computer", "Games"]),
 m("Break is for:", ["30 minutes", "40 minutes", "10 minutes", "one hour"]),
 m("Computer period begins at:", ["11:10", "10:30", "11:50", "9:20"]),
 m("School ends at:", ["12:30 p.m.", "1:00 p.m.", "11:50 a.m.", "2:00 p.m."]),
 m("Which subject comes just after the break?", ["Environmental Studies", "Computer", "Games", "Hindi"]),
 S("How long is each period?", "40 minutes.", 1),
 S("Which period is Mathematics?", "The second period.", 1),
 S(TF + "The spelling test is held on Fridays.", "False (it is held every Monday).", 1),
 S("What should students bring from home?", "Their own water bottles.", 1),
 S("At what time is the Games period over?", "At 12:30 p.m.", 1)], title="Read the time-table and the notes below it, and answer the questions that follow."),
P2=P("""<p class='h'>The Moon</p>
<p>The moon looks like a silver plate,<br>Hanging high at night,<br>Sometimes round and sometimes thin,<br>Always shining bright.</p>
<p>It follows me when I walk,<br>It peeps behind a tree,<br>When I wave, it waves to me,<br>A friendly sight to see.</p>
<p>The stars are little twinkling lamps,<br>The moon, their king so grand,<br>Goodnight, dear moon, I'll sleep now,<br>And dream of fairyland.</p>""",
[m("The moon looks like a:", ["silver plate", "golden coin", "red ball", "white cloud"]),
 m("The moon hangs in the sky at:", ["night", "noon", "morning", "dawn"]),
 m("The stars are compared to:", ["twinkling lamps", "diamonds", "flowers", "balloons"]),
 m("The child will now:", ["sleep", "play", "study", "sing"]),
 m("The poet calls the moon the stars':", ["king", "queen", "teacher", "friend"]),
 S("What does the moon do when the child walks?", "It follows the child.", 1),
 S("Name two shapes of the moon mentioned.", "Round and thin.", 1),
 S(TF + "The poet is afraid of the moon.", "False.", 1),
 S("Pick two rhyming words from the first stanza.", "night – bright.", 1),
 S("What will the child dream of?", "Fairyland.", 1)], title="Read the poem carefully and answer the questions that follow."),
)
