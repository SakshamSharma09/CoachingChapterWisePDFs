"""Class 7 reading skill sets 6-10 (original)."""
from eng9_lib import P, S

def m(q, o):
    return S(q, "a", 1, o)

SETS = {}

SETS[6] = dict(
P1=P("""<p><b>The Ship of the Desert</b></p>
<p>The camel is one of the few animals that can live comfortably in the hot, dry desert. Its body is perfectly suited to such a life, which is why it is often called 'the ship of the desert'. A camel can walk for many days across the sand with very little water. It does not store water in its hump, as many people think. The hump is a store of fat, which gives the animal energy when food is hard to find.</p>
<p>The camel has several other useful features. Its wide, soft feet do not sink in the sand. Its long eyelashes and thick eyebrows protect its eyes from dust, and it can close its nostrils during a sandstorm. When it finds water, a thirsty camel may drink as much as a hundred litres in just a few minutes.</p>
<p>For centuries, people in desert regions such as Rajasthan have used camels to carry goods and travellers. Camel milk is nutritious, and camel hair is used to make blankets and ropes. Every November, thousands of visitors come to the Pushkar Fair to see the decorated camels and enjoy the races. Although trucks and jeeps are now common, the camel remains a loyal friend of the desert people.</p>""",
[m("Why is the camel called the 'ship of the desert'?", ["It carries people across the sand", "It lives in water", "It looks like a boat", "It makes sounds like a ship"]),
 m("The camel's hump is a store of:", ["fat", "water", "air", "milk"]),
 m("Camels do not sink in sand because they have:", ["wide, soft feet", "long legs", "sharp nails", "thick fur"]),
 S("State whether True or False: A thirsty camel can drink a hundred litres of water in a few minutes.", "a", 1, ["True", "False"]),
 m("The Pushkar Fair is held every:", ["November", "March", "June", "January"]),
 S("What is the common belief about the camel's hump, and what is the truth?", "People think it stores water; actually it stores fat.", 1),
 S("How do the camel's eyelashes and nostrils help it in a sandstorm?", "Eyelashes and eyebrows protect the eyes from dust and the nostrils can be closed.", 1),
 S("Mention two uses of camels for people.", "Any two: carrying goods and travellers, milk, hair for blankets and ropes.", 1),
 S("Find a word in the passage that means 'giving the body what it needs to grow'.", "Nutritious.", 1),
 S("What does the phrase 'a loyal friend of the desert people' show?", "Camels have served desert people faithfully for a long time and are still valued by them.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p style="text-align:center"><b>The Lighthouse</b></p>
<p style="text-align:center">On a rock beside the roaring sea<br>
A lighthouse stands alone;<br>
Its lamp is lit when daylight fades,<br>
Its tower is tall as stone.</p>
<p style="text-align:center">The ships come sailing through the dark,<br>
They search for land and shore;<br>
And through the fog its steady beam<br>
Says, "Safe this way once more."</p>
<p style="text-align:center">It never sails, it never sleeps,<br>
Yet guides ten thousand boats;<br>
It asks no thanks from any one<br>
Of all the crews it floats.</p>
<p style="text-align:center">O may I be a lighthouse too,<br>
In times of storm and night,<br>
And lend to those who lose their way<br>
A little steady light.</p>""",
[m("The lighthouse stands:", ["on a rock beside the sea", "in a city", "in a forest", "on a mountain peak"]),
 m("When is the lamp lit?", ["When daylight fades", "At sunrise", "At noon", "Only in summer"]),
 m("What does the lighthouse beam tell the ships?", ["Which way is safe", "That a storm is coming", "That they must wait", "That it is morning"]),
 S("State whether True or False: The lighthouse asks for thanks from the crews.", "b", 1, ["True", "False"]),
 m("The poet wishes to be like a lighthouse in order to:", ["help others who are lost", "be famous", "sail ships", "live near the sea"]),
 S("Why do the ships need the lighthouse?", "To find land and shore safely in the dark and fog.", 1),
 S("How does the poet show that the lighthouse is very dependable?", "It never sails or sleeps and guides ten thousand boats.", 1),
 S("Pick out a pair of rhyming words from the last stanza.", "night – light.", 1),
 S("What does 'a little steady light' stand for in the last stanza?", "Help, guidance or hope given to people in trouble.", 1),
 S("What is the central idea of the poem? Answer in one sentence.", "We should help and guide others in difficulty without expecting thanks.", 1)],
 title="Read the poem and answer the questions that follow."),
)

SETS[7] = dict(
P1=P("""<p><b>From Waste to Wealth: Recycling Paper</b></p>
<p>Every day we use a great deal of paper, in notebooks, newspapers, boxes and packets. Paper is made from wood pulp, and wood comes from trees. To make one tonne of paper, many full-grown trees have to be cut. If we continue to waste paper, our forests will shrink, and animals and birds will lose their homes.</p>
<p>Recycling is a way of making new paper from old. First, waste paper is collected from homes, schools and offices. It is then sorted and sent to a factory, where it is soaked in water and broken into a soft pulp. Ink is removed from the pulp, which is then spread out, pressed and dried into fresh sheets. Recycled paper uses less water and energy than paper made from new wood, and it saves trees.</p>
<p>Each of us can do something to help. We can use both sides of a sheet, reuse old envelopes and give old newspapers to the raddiwala. Schools can set up collection bins for used paper. These small habits, if followed by everyone, will make a big difference. As the saying goes, 'Reduce, reuse and recycle', and in this order, because the best waste is the one that is never created.</p>""",
[m("Paper is made from:", ["wood pulp", "plastic", "cotton only", "sand"]),
 m("The first step of recycling is:", ["collecting waste paper", "removing ink", "pressing the sheets", "cutting trees"]),
 m("Recycled paper:", ["uses less water and energy", "uses more water", "is made from new wood", "cannot be written on"]),
 S("State whether True or False: Recycling saves trees.", "a", 1, ["True", "False"]),
 m("According to the saying, which comes first?", ["Reduce", "Reuse", "Recycle", "Remove"]),
 S("What will happen if we keep wasting paper?", "Forests will shrink and animals and birds will lose their homes.", 1),
 S("What is done to the waste paper at the factory? Mention two steps.", "Any two: soaked in water and broken into pulp, ink removed, spread, pressed and dried.", 1),
 S("Mention two ways in which students can save paper.", "Use both sides of a sheet, reuse old envelopes, give old newspapers to the raddiwala, set up collection bins.", 1),
 S("Find a word in the passage that means 'sorted and separated into groups'.", "Sorted.", 1),
 S("Why does the writer say 'the best waste is the one that is never created'?", "Because reducing use prevents waste in the first place and is better than recycling.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>Ravi's First Chess Match</b></p>
<p>Ravi had learnt chess from his uncle during the summer holidays, and he loved the game. When the school announced an inter-house chess competition, he put his name down at once. But as the day came closer, his stomach began to feel funny. What if he lost in front of everyone?</p>
<p>On the morning of the match he sat across the board from Nishant, the school champion. The hall was silent except for the soft click of pieces. Within ten moves Ravi lost his queen, and his hands began to shake. He wanted to stand up and walk away.</p>
<p>Then he remembered his uncle's words: "A game is never lost until you stop thinking." Ravi took a deep breath and looked at the board again. He saw that Nishant's king was not well guarded. Step by step, he moved his knight and then his rook. Nishant frowned and thought for a long time.</p>
<p>In the end Ravi lost the match by a single move, but the teacher clapped for both players. Nishant shook his hand and said, "You nearly beat me. Play again next month." Ravi walked home smiling. He had not won the trophy, but he had won something more valuable: the courage to try.</p>""",
[m("Who taught Ravi chess?", ["His uncle", "His teacher", "Nishant", "His father"]),
 m("Ravi felt nervous because:", ["he feared losing in front of everyone", "he had not learnt chess", "he was ill", "the hall was cold"]),
 m("Nishant was:", ["the school champion", "Ravi's brother", "the teacher", "a new student"]),
 S("State whether True or False: Ravi won the match.", "b", 1, ["True", "False"]),
 m("What did Ravi gain from the match?", ["Courage to try", "A trophy", "A new bat", "A holiday"]),
 S("What happened to Ravi in the first ten moves?", "He lost his queen.", 1),
 S("What did his uncle's words teach him?", "That a game is never lost until you stop thinking.", 1),
 S("How did Nishant behave at the end of the match?", "He shook Ravi's hand and invited him to play again next month.", 1),
 S("Find a word in the passage that means 'made an unhappy or serious face'.", "Frowned.", 1),
 S("Why did Ravi walk home smiling even though he lost?", "He had shown courage and played well, which he valued more than the trophy.", 1)],
 title="Read the story and answer the questions that follow."),
)

SETS[8] = dict(
P1=P("""<p><b>The Story of the Book</b></p>
<p>Long before paper was invented, people wrote on stones, clay tablets, palm leaves and bark. In India, scholars wrote on palm leaves and the inner bark of the birch tree, which were tied together with string. The Chinese invented paper nearly two thousand years ago, and the art of making it slowly spread across Asia to Europe.</p>
<p>For centuries, every book had to be copied by hand. A single copy could take months, and so books were rare and costly. Only kings, priests and rich people could afford them. This changed in the fifteenth century, when a German named Johannes Gutenberg built a printing machine that used movable metal letters. Many copies of a book could now be made in a short time, and the price of books fell sharply.</p>
<p>Today we can read a book on paper or on a screen, and an entire library can fit into a phone. But the purpose of a book has not changed: it carries ideas from one mind to another across space and time. A book written hundreds of years ago can still make a reader laugh or think today. That is the real magic of books.</p>""",
[m("Before paper, Indian scholars wrote on:", ["palm leaves and birch bark", "cloth only", "wooden boards only", "glass"]),
 m("Paper was first invented by the:", ["Chinese", "Greeks", "Egyptians", "Romans"]),
 m("Books were costly in the past because:", ["each was copied by hand", "paper was free", "there were many readers", "they were small"]),
 S("State whether True or False: Gutenberg's machine used movable metal letters.", "a", 1, ["True", "False"]),
 m("The last paragraph says that the purpose of a book is to:", ["carry ideas from one mind to another", "decorate a shelf", "make money", "replace phones"]),
 S("Why could only rich people afford books earlier?", "Because every copy was made by hand and took months, so books were rare and costly.", 1),
 S("What was the effect of Gutenberg's printing machine?", "Many copies could be made quickly and the price of books fell.", 1),
 S("Name two materials on which people wrote before paper.", "Any two: stones, clay tablets, palm leaves, bark.", 1),
 S("Find a word in the passage that means 'not common; seldom found'.", "Rare.", 1),
 S("What does the writer call 'the real magic of books'?", "That a book from hundreds of years ago can still make a reader laugh or think today.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p style="text-align:center"><b>Morning Market</b></p>
<p style="text-align:center">Before the sun has climbed the wall<br>
The market is awake;<br>
The vegetable sellers call<br>
And scales begin to shake.</p>
<p style="text-align:center">There are tomatoes, round and red,<br>
Green peas in a heap,<br>
Ripe mangoes piled upon a cart,<br>
And onions in a sweep.</p>
<p style="text-align:center">The flower-seller threads the buds<br>
Into a golden chain;<br>
The air smells sweet of jasmine<br>
And of the morning rain.</p>
<p style="text-align:center">Then slowly down the dusty street<br>
The buyers make their way,<br>
And the market sings its busy song<br>
Until the end of day.</p>""",
[m("When does the market wake up?", ["Before sunrise gets high", "At midnight", "In the afternoon", "At night"]),
 m("The vegetable sellers:", ["call out to the buyers", "sleep", "close shops", "sing songs"]),
 m("The flower-seller makes:", ["a golden chain of buds", "a basket", "a paper kite", "a drum"]),
 S("State whether True or False: The air smells of jasmine and morning rain.", "a", 1, ["True", "False"]),
 m("The mood of the poem is:", ["lively and cheerful", "sad", "angry", "silent"]),
 S("Name two things sold in the market.", "Any two: tomatoes, green peas, mangoes, onions, flowers.", 1),
 S("What does the phrase 'scales begin to shake' suggest?", "That selling and weighing of goods has begun.", 1),
 S("Pick out a pair of rhyming words from the third stanza.", "chain – rain.", 1),
 S("What does the poet mean by 'the market sings its busy song'?", "The market is full of lively sounds of buying and selling.", 1),
 S("Which senses does the poet appeal to in the poem? Mention any two.", "Sight (colours of vegetables), smell (jasmine), hearing (sellers calling).", 1)],
 title="Read the poem and answer the questions that follow."),
)

SETS[9] = dict(
P1=P("""<p><b>Start the Day with Breakfast</b></p>
<p>Many people say that breakfast is the most important meal of the day, and there is good reason for this. After a night's sleep, the body has gone without food for ten or twelve hours. Breakfast gives it the fuel it needs to begin the day. A child who skips breakfast often feels weak and sleepy by the second period, finds it hard to concentrate and may become cranky.</p>
<p>A healthy breakfast need not be fancy or costly. It should include something from each of the main food groups: grains such as roti, poha or oats; protein such as milk, eggs, sprouts or dal; and fruits or vegetables. Fried snacks, sugary biscuits and fizzy drinks may taste good, but they provide very little nourishment and make us hungry again within an hour.</p>
<p>Taking a few minutes for breakfast also teaches discipline. The family that sits together to eat in the morning shares news, jokes and plans for the day. Waking up ten minutes earlier is a small price to pay for such a good start. After all, a car cannot run without fuel, and neither can a student.</p>""",
[m("Why is breakfast important?", ["The body needs fuel after a night without food", "It is always costly", "It replaces lunch", "It is tasty"]),
 m("A child who skips breakfast often:", ["feels weak and sleepy", "feels energetic", "reads faster", "sleeps early"]),
 m("Which of these is a good source of protein?", ["Sprouts", "Fizzy drinks", "Sugary biscuits", "Fried snacks"]),
 S("State whether True or False: A healthy breakfast must be costly.", "b", 1, ["True", "False"]),
 m("The writer compares a student to:", ["a car that needs fuel", "a bird", "a ship", "a machine that never stops"]),
 S("For how long has the body gone without food by morning?", "Ten or twelve hours.", 1),
 S("Name two kinds of food that make a healthy breakfast.", "Any two: roti/poha/oats, milk/eggs/sprouts/dal, fruits or vegetables.", 1),
 S("Why are fizzy drinks and sugary biscuits not good for breakfast?", "They give very little nourishment and make us hungry again within an hour.", 1),
 S("Find a word in the passage that means 'bad-tempered'.", "Cranky.", 1),
 S("What is the benefit of eating breakfast together as a family?", "The family shares news, jokes and plans for the day.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>The Fisherman's Net</b></p>
<p>Rahim was a young fisherman who lived by a lake. Every morning he rowed out in his small boat and cast his net. Some days the net came back full of silver fish. On other days it came back empty, and then Rahim and his old mother went to bed hungry.</p>
<p>One windy morning he felt the net grow heavy. He pulled with all his strength, and up came a large, beautiful fish with golden scales. It looked at him with wide eyes. "Please let me go," it seemed to say. "I have little ones waiting." Rahim hesitated. This one fish would feed him for a week. But he thought of his own mother waiting at home, and he understood how the fish felt.</p>
<p>Gently he lowered the fish back into the water. It flipped its tail, gave him one last glance and vanished into the deep. Rahim cast the net again and again, but caught nothing that day. He rowed home slowly, wondering what he would tell his mother.</p>
<p>When he reached the shore, he was surprised to see a crowd. A merchant who had watched from the bank walked up to him. "I saw what you did," the man said. "A person who shows such mercy deserves a better living. Come and work in my fish market, and I shall pay you fairly." From that day Rahim never went to bed hungry again.</p>""",
[m("Rahim lived:", ["by a lake", "in a desert", "on a hill", "in a big city"]),
 m("What was special about the fish he caught?", ["It had golden scales", "It was very small", "It could speak", "It was black"]),
 m("Rahim let the fish go because:", ["he understood how it felt", "it was too heavy", "it was ill", "a man asked him"]),
 S("State whether True or False: Rahim caught many fish after releasing the golden fish.", "b", 1, ["True", "False"]),
 m("Who offered Rahim a job?", ["A merchant", "His mother", "A king", "A teacher"]),
 S("How did Rahim and his mother live on days when the net was empty?", "They went to bed hungry.", 1),
 S("Why did Rahim hesitate before releasing the fish?", "That one fish would have fed him for a week.", 1),
 S("What did the merchant say about Rahim?", "A person who shows such mercy deserves a better living.", 1),
 S("Find a word in the passage that means 'kindness shown to someone in trouble'.", "Mercy.", 1),
 S("What lesson does the story teach?", "Kindness and compassion are rewarded.", 1)],
 title="Read the story and answer the questions that follow."),
)

SETS[10] = dict(
P1=P("""<p><b>Power from the Sun</b></p>
<p>The sun is a giant ball of burning gas that gives us light and heat every day. This energy, called solar energy, is free, clean and will last for millions of years. Unlike coal and petrol, it does not produce smoke or harmful gases when we use it, and therefore it does not pollute the air.</p>
<p>We can capture the sun's energy in several ways. A solar water heater uses the heat of the sun to warm water for bathing. A solar cooker can cook rice and vegetables slowly in the sunshine. Solar panels are made of special cells that turn sunlight into electricity. Many villages in India that were once without power now have lights, fans and water pumps run by solar panels. Even streetlights and traffic signals in some cities use solar power.</p>
<p>Solar energy has its limits. Panels do not work well on cloudy days and stop working at night, so a battery is needed to store the power. The equipment can also be costly at the start, though it saves money in the long run. Still, because fuels like coal and petrol are running out, scientists believe that the sun will become our main source of energy in the future. A country like India, which receives bright sunshine for most of the year, is well placed to lead the way.</p>""",
[m("Solar energy is:", ["free and clean", "costly to produce daily", "made from coal", "harmful to the air"]),
 m("Solar panels turn sunlight into:", ["electricity", "water", "petrol", "oxygen"]),
 m("Why is a battery needed with solar panels?", ["To store power for night and cloudy days", "To make the panels heavier", "To cool the sun", "To clean the panels"]),
 S("State whether True or False: Solar panels work well at night.", "b", 1, ["True", "False"]),
 m("India is well placed for solar power because it:", ["gets bright sunshine most of the year", "has many mountains", "has cheap coal", "has long rivers"]),
 S("Why does solar energy not pollute the air?", "It does not produce smoke or harmful gases when used.", 1),
 S("Mention two uses of solar energy given in the passage.", "Any two: solar water heater, solar cooker, solar panels for lights, fans and pumps, streetlights.", 1),
 S("What are the two limits of solar energy mentioned?", "Panels do not work on cloudy days/at night, and the equipment is costly at the start.", 1),
 S("Find a word in the passage that means 'to take hold of or collect'.", "Capture.", 1),
 S("Why do scientists believe the sun will be our main source of energy in the future?", "Fuels like coal and petrol are running out.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p style="text-align:center"><b>A Seed's Dream</b></p>
<p style="text-align:center">Under the earth, in a quiet bed,<br>
A tiny seed lay sleeping;<br>
It dreamt of the sky and the singing birds<br>
While the cold dark rain was weeping.</p>
<p style="text-align:center">"Oh, when shall I see the light?" it said,<br>
"When will my roots grow strong?"<br>
The worm said, "Wait," and the soil said, "Wait,"<br>
"It won't be very long."</p>
<p style="text-align:center">One day the sun came warm and bright,<br>
And the seed gave a little shiver;<br>
It pushed a green head through the ground<br>
And stood by the shining river.</p>
<p style="text-align:center">Now it is a tree with a hundred arms<br>
And a nest in every one;<br>
It tells the seeds beneath the earth,<br>
"Just wait for the morning sun."</p>""",
[m("Where was the seed sleeping?", ["Under the earth", "In a river", "On a tree", "In a nest"]),
 m("The worm and the soil told the seed to:", ["wait", "hurry", "sleep forever", "go away"]),
 m("What made the seed come out of the ground?", ["The warm bright sun", "A strong wind", "A farmer", "The moon"]),
 S("State whether True or False: The seed grew into a tree with nests in its branches.", "a", 1, ["True", "False"]),
 m("The central message of the poem is:", ["patience brings success", "seeds are small", "rain is cold", "trees are tall"]),
 S("What did the seed dream about?", "The sky and the singing birds.", 1),
 S("Pick out a pair of rhyming words from the second stanza.", "strong – long.", 1),
 S("What does the tree tell the seeds beneath the earth?", "To wait for the morning sun.", 1),
 S("What does 'a tree with a hundred arms' mean?", "A tree with many branches.", 1),
 S("How can we say that the tree is useful to birds?", "It has a nest in every branch.", 1)],
 title="Read the poem and answer the questions that follow."),
)
