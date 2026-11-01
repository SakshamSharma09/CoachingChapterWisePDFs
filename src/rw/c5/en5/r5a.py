"""Class 5 reading sets 1-5 (original). P1 factual/information (10), P2 story/poem/notice (10)."""
from eng9_lib import P, S
def m(q, o): return S(q, "a", 1, o)
TF = "State whether True or False: "
SETS = {}
T1 = "Read the passage carefully and answer the questions that follow."
T2 = "Read the story carefully and answer the questions that follow."

SETS[1] = dict(
P1=P("""<p>Honeybees live together in a home called a hive. A hive may have thousands of bees, but only one queen. The queen lays the eggs. The worker bees do all the other jobs. They clean the hive, feed the young bees and guard the door.</p>
<p>Worker bees also fly out to flowers to collect a sweet juice called nectar. They carry it back and turn it into honey. While sitting on a flower, a bee gets yellow dust, called pollen, on its legs. When it flies to the next flower, some pollen falls there. This helps the plants to make seeds and fruits.</p>
<p>When a bee finds a good garden, it tells its friends by dancing. Its dance shows how far the flowers are and in which direction. Honeybees are small, but they are very hardworking and helpful to us.</p>""",
[m("A home of honeybees is called a:", ["hive", "nest", "den", "burrow"]),
 m("How many queens are there in a hive?", ["One", "Two", "Ten", "Thousands"]),
 m("Bees collect nectar from:", ["flowers", "leaves", "honey", "roots"]),
 m("The yellow dust on the bee's legs is called:", ["pollen", "honey", "sugar", "wax"]),
 m("A bee tells its friends about a garden by:", ["dancing", "singing", "buzzing loudly", "flying away"]),
 S("What does the queen bee do?", "She lays the eggs.", 1),
 S("Name one job of the worker bees in the hive.", "They clean the hive / feed the young bees / guard the door (any one).", 1),
 S(TF + "Bees make honey from nectar.", "True.", 1),
 S("Find a word in the passage which means 'strong effort in work' (describing bees).", "Hardworking.", 1),
 S("How do bees help plants?", "Pollen falls from flower to flower and helps plants make seeds and fruits.", 1)], title=T1),
P2=P("""<p>Meera had a small pet parrot named Mithu. Every morning she gave him a green chilli and some water. Mithu would say, "Good morning, Meera!" and she would laugh happily.</p>
<p>One day, Mithu's cage door was left open. He flew out and sat on a high branch of the neem tree. Meera called him again and again, but Mithu did not come back. She felt very sad and did not eat her lunch.</p>
<p>In the evening, dark clouds covered the sky and it began to rain. Suddenly Meera heard a thin voice, "Good morning, Meera!" Mithu was sitting on the window, wet and shivering. Meera took him in, dried him with a soft cloth and put him in his cage. She promised never to leave the door open again.</p>""",
[m("The name of Meera's parrot was:", ["Mithu", "Chintu", "Tota", "Moti"]),
 m("Mithu was given a green chilli:", ["every morning", "every night", "once a week", "at lunch"]),
 m("Mithu flew away and sat on a:", ["neem tree", "mango tree", "roof", "fence"]),
 m("Mithu came back when:", ["it began to rain", "Meera called him", "he was hungry", "it was night"]),
 m("Meera dried Mithu with a:", ["soft cloth", "towel", "paper", "blanket"]),
 S("What did Mithu say every morning?", "Good morning, Meera!", 1),
 S("Why did Meera not eat her lunch?", "She was very sad because Mithu had flown away.", 1),
 S(TF + "Mithu came back to the window in the evening.", "True.", 1),
 S("Find a word in the story which means 'shaking with cold'.", "Shivering.", 1),
 S("What did Meera promise at the end?", "She promised never to leave the cage door open again.", 1)], title=T2),
)

SETS[2] = dict(
P1=P("""<p>The Sun is a huge ball of hot gas. It is much bigger than the Earth. It looks small because it is very far away from us. The light of the Sun takes about eight minutes to reach the Earth.</p>
<p>The Sun gives us heat and light. Without it, the Earth would be dark and cold, and nothing could live here. Plants use sunlight to make their food. Animals and people eat plants or other animals that eat plants. So the Sun is the source of energy for all living things.</p>
<p>The Sun also helps us in many other ways. It dries our clothes, warms the sea water to make clouds, and gives us the seasons. But we should never look at the Sun directly, because its strong light can hurt our eyes.</p>""",
[m("The Sun is a ball of:", ["hot gas", "fire and stone", "ice", "water"]),
 m("The Sun looks small because it is:", ["very far away", "very cold", "made of gas", "behind the clouds"]),
 m("Sunlight takes how long to reach the Earth?", ["About eight minutes", "One hour", "One second", "One day"]),
 m("Plants use sunlight to:", ["make their food", "grow roots", "get water", "make clouds"]),
 m("We should not look at the Sun directly because it can:", ["hurt our eyes", "make us tall", "make us thirsty", "make us sleepy"]),
 S("What does the Sun give us?", "It gives us heat and light.", 1),
 S(TF + "The Sun is smaller than the Earth.", "False.", 1),
 S("Why would the Earth be dark and cold without the Sun?", "Because the Sun gives heat and light.", 1),
 S("Name one other way in which the Sun helps us.", "It dries clothes / helps make clouds / gives us seasons (any one).", 1),
 S("Find a word in the passage that means 'a very large size'.", "Huge.", 1)], title=T1),
P2=P("""<p class='h'>The Rainy Day</p>
<p>Drip, drop, drip, drop,<br>Rain is falling from the sky.<br>Puddles shine on the road,<br>Little boats go floating by.</p>
<p>Frogs jump out and sing their song,<br>Peacocks dance with feathers wide.<br>I wear my coat and yellow boots<br>And splash with joy outside.</p>
<p>Mother calls me for hot tea,<br>Grandma bakes some warm pakoras.<br>Rain, rain, stay a little more,<br>I love your cool, wet colours.</p>""",
[m("In the poem, the rain is falling from the:", ["sky", "tree", "roof", "river"]),
 m("The little boats are floating in the:", ["puddles", "pond", "sea", "bucket"]),
 m("Who dance with wide feathers?", ["Peacocks", "Frogs", "Parrots", "Sparrows"]),
 m("The child wears:", ["a coat and yellow boots", "a cap", "a raincoat and hat", "sandals"]),
 m("Grandma bakes:", ["pakoras", "cake", "bread", "biscuits"]),
 S("Name two things that the poet sees after the rain.", "Puddles, boats, frogs, peacocks (any two).", 1),
 S("What does Mother call the child for?", "For hot tea.", 1),
 S(TF + "The child is afraid of the rain.", "False.", 1),
 S("Pick two rhyming words from the first stanza.", "sky – by (also: drop – drop).", 1),
 S("Does the poet like the rain? How do you know?", "Yes; the poet says 'Rain, rain, stay a little more, I love your cool, wet colours.'", 1)], title="Read the poem carefully and answer the questions that follow."),
)

SETS[3] = dict(
P1=P("""<p>Trees are our silent friends. They give us fruits, wood, shade and fresh air. During the day, trees take in a gas called carbon dioxide and give out oxygen. We need oxygen to breathe, so trees help us to stay alive.</p>
<p>The roots of a tree hold the soil firmly. When heavy rain falls, the roots stop the soil from being washed away. Trees also bring rain, because they help the clouds to form. Many birds build nests on trees, and squirrels and monkeys make them their home.</p>
<p>Today, many trees are being cut to make roads and buildings. This is a big problem. For every tree that is cut, we should plant two new trees and look after them. Let us promise to plant at least one sapling every year.</p>""",
[m("Trees give out:", ["oxygen", "carbon dioxide", "smoke", "dust"]),
 m("The roots of a tree:", ["hold the soil", "make fruits", "give shade", "build nests"]),
 m("Which animals make their home on trees?", ["Squirrels and monkeys", "Cows and goats", "Fish and frogs", "Lions and tigers"]),
 m("Many trees are being cut to make:", ["roads and buildings", "gardens", "nests", "ponds"]),
 m("The writer asks us to plant at least:", ["one sapling every year", "ten trees a day", "two trees a week", "a forest"]),
 S("Why are trees called our 'silent friends'?", "They give us many useful things like fruits, wood, shade and fresh air without saying anything.", 1),
 S("What do we need oxygen for?", "To breathe.", 1),
 S(TF + "Roots of the trees cannot stop soil from being washed away.", "False.", 1),
 S("Find a word in the passage which means 'a young plant'.", "Sapling.", 1),
 S("What should we do for every tree that is cut?", "Plant two new trees and look after them.", 1)], title=T1),
P2=P("""<p>Rohan was a boy who always came late to school. His teacher, Mr Verma, told him many times, "Rohan, start a little early." But Rohan only smiled and said, "Sir, the road is long."</p>
<p>One morning, a heavy truck broke down on the road and the traffic stopped. Rohan reached the school gate at nine o'clock, when the bell had already rung. He ran towards his class, but the gate was closed. He had missed the morning prayer and the first test.</p>
<p>That evening, Rohan set the alarm for six o'clock. From the next day, he reached school ten minutes before the bell. Mr Verma smiled and said, "Well done, Rohan. A little early is always better than a little late."</p>""",
[m("Rohan always came to school:", ["late", "early", "on time", "with his father"]),
 m("Rohan's teacher was:", ["Mr Verma", "Mr Sharma", "Mr Singh", "Mr Gupta"]),
 m("The traffic stopped because:", ["a truck broke down", "it rained", "there was a fair", "a bus turned over"]),
 m("Rohan reached the gate at:", ["nine o'clock", "eight o'clock", "ten o'clock", "seven o'clock"]),
 m("After that day, Rohan set the alarm for:", ["six o'clock", "five o'clock", "seven o'clock", "eight o'clock"]),
 S("What did Rohan say when the teacher told him to start early?", "He said, 'Sir, the road is long.'", 1),
 S("What did Rohan miss on that day? Name one.", "The morning prayer or the first test.", 1),
 S(TF + "Rohan became punctual after that day.", "True.", 1),
 S("Find a word in the story which means 'to break down in the middle of the road'. (Hint: used for the truck)", "Broke down.", 1),
 S("What lesson does the story teach?", "We should always start early and reach on time.", 1)], title=T2),
)

SETS[4] = dict(
P1=P("""<p>The camel is called the 'ship of the desert'. It can walk for many days on hot sand without drinking water. It stores fat, not water, in its hump. When it cannot find food, the body uses this fat for energy.</p>
<p>A camel's body is made for the desert. Its long eyelashes and two rows of lashes protect the eyes from blowing sand. It can close its nostrils during a sandstorm. Its feet are wide and soft, so they do not sink in the sand.</p>
<p>People of Rajasthan use camels to carry loads and to travel long distances. Camel milk is also drunk by many families. Every year, the famous Camel Fair is held at Pushkar, where thousands of people come to see decorated camels.</p>""",
[m("The camel is called the:", ["ship of the desert", "king of the desert", "friend of the desert", "boat of the sand"]),
 m("A camel stores ______ in its hump.", ["fat", "water", "food", "sand"]),
 m("Camels' wide feet help them to:", ["walk without sinking in sand", "run very fast", "climb hills", "swim"]),
 m("People use camels to:", ["carry loads", "plough fields only", "catch fish", "make honey"]),
 m("The Camel Fair is held at:", ["Pushkar", "Jaipur", "Jodhpur", "Udaipur"]),
 S(TF + "A camel stores water in its hump.", "False.", 1),
 S("How do the camel's long eyelashes help it?", "They protect its eyes from blowing sand.", 1),
 S("What can a camel do during a sandstorm?", "It can close its nostrils.", 1),
 S("Name two uses of camels for people.", "To carry loads, to travel long distances, milk (any two).", 1),
 S("Find a word in the passage which means 'to cover and keep safe'.", "Protect.", 1)], title=T1),
P2=P("""<p>Once there lived a crow who was very thirsty. He flew here and there looking for water, but the summer was hot and all the ponds had dried up.</p>
<p>At last he saw a pot lying under a tree. There was a little water at the bottom, but his beak could not reach it. The crow thought for a while. Then he saw some small stones on the ground.</p>
<p>He picked up the stones one by one and dropped them into the pot. Slowly the water rose up. Soon it came to the top and the crow drank to his heart's content. Then he flew away happily, thinking, "Where there is a will, there is a way."</p>""",
[m("The crow was very:", ["thirsty", "hungry", "sleepy", "angry"]),
 m("The ponds had dried up because:", ["it was a hot summer", "it was winter", "there was a flood", "people drank it"]),
 m("The crow found a pot under a:", ["tree", "bench", "bridge", "roof"]),
 m("The crow dropped ______ into the pot.", ["small stones", "leaves", "twigs", "sand"]),
 m("The water in the pot:", ["rose up", "dried up", "turned dirty", "went down"]),
 S("Why could the crow not drink water at first?", "There was little water at the bottom and his beak could not reach it.", 1),
 S("What did the crow do to get the water?", "He dropped small stones into the pot one by one.", 1),
 S(TF + "The crow gave up at once.", "False.", 1),
 S("Which word in the story means 'happily and completely'? (Hint: 'to his heart's ______')", "Content.", 1),
 S("What is the moral of the story?", "Where there is a will, there is a way.", 1)], title=T2),
)

SETS[5] = dict(
P1=P("""<p><b>LIBRARY RULES — Mastermind Public School</b></p>
<p>The library is open from <b>8:00 a.m. to 3:00 p.m.</b>, from Monday to Saturday. Students of Classes 3 to 5 may borrow <b>two books</b> at a time for <b>seven days</b>. A book can be renewed once if no one else has asked for it.</p>
<p>Please keep silence in the library. Do not write, fold or tear the pages of any book. If a book is lost, the student must give a new copy or pay its price. Books that are returned late will cost <b>Rs 2 per day</b> as a fine.</p>
<p>The Story Hour is held every <b>Friday at 1:30 p.m.</b> in the reading room. Students who read the most books in a month will get a <b>Book Worm</b> badge.</p>""",
[m("The library is open from Monday to:", ["Saturday", "Friday", "Sunday", "Thursday"]),
 m("A student of Class 4 can borrow:", ["two books", "five books", "one book", "ten books"]),
 m("A book can be kept for:", ["seven days", "two days", "one month", "fifteen days"]),
 m("The fine for late return is:", ["Rs 2 per day", "Rs 10 per day", "Rs 5 per week", "no fine"]),
 m("The Story Hour is on:", ["Friday", "Monday", "Wednesday", "Saturday"]),
 S("At what time does the library close?", "At 3:00 p.m.", 1),
 S(TF + "Students may fold the pages of a book.", "False.", 1),
 S("What must a student do if a book is lost?", "Give a new copy or pay its price.", 1),
 S("What will students get for reading the most books?", "A Book Worm badge.", 1),
 S("Where is the Story Hour held?", "In the reading room.", 1)], title="Read the notice carefully and answer the questions that follow."),
P2=P("""<p>Anu was walking home from school when she saw a small puppy sitting alone near the gate. It was shivering and its leg was hurt. Anu felt sorry for it. She sat down and gently patted its head.</p>
<p>She took out her water bottle and poured some water in the lid. The puppy drank it quickly. Then she shared her tiffin of bread and butter with it. "Come with me," said Anu softly, and lifted the puppy in her arms.</p>
<p>At home, Anu's mother cleaned the puppy's leg and tied a clean cloth over it. Father brought a small basket for its bed. In a few days the puppy was running around the house. Anu named him Bholu, and he became her best friend.</p>""",
[m("Anu saw the puppy near the:", ["school gate", "park", "market", "river"]),
 m("The puppy was hurt in its:", ["leg", "tail", "ear", "eye"]),
 m("Anu gave water in the:", ["lid of her bottle", "a bowl", "a glass", "her hands"]),
 m("Who cleaned the puppy's leg?", ["Anu's mother", "Anu's father", "Anu", "The doctor"]),
 m("Anu named the puppy:", ["Bholu", "Moti", "Tommy", "Sheru"]),
 S("What did Anu share with the puppy?", "Her tiffin of bread and butter.", 1),
 S("What did father bring?", "A small basket for its bed.", 1),
 S(TF + "The puppy got better in a few days.", "True.", 1),
 S("Find a word in the story which means 'in a kind and soft way'.", "Gently / softly.", 1),
 S("Is Anu a kind girl? Give one reason.", "Yes; she helped the hurt puppy / gave it water and food and took it home.", 1)], title=T2),
)
