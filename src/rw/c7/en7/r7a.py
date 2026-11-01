"""Class 7 reading skill sets 1-5 (original). P1 factual/discursive (10 marks), P2 literary: story or poem (10 marks)."""
from eng9_lib import P, S

def m(q, o):
    return S(q, "a", 1, o)

SETS = {}

SETS[1] = dict(
P1=P("""<p><b>The Busy Honeybee</b></p>
<p>A honeybee lives in a large family called a colony. A single colony may have fifty thousand bees, and every bee has a job. The queen is the only bee who lays eggs. The worker bees, who are all female, clean the hive, feed the young bees and guard the door. The male bees, called drones, do very little work, and their main purpose is to mate with a queen.</p>
<p>The most interesting work is done by the bees that collect food. A worker flies from flower to flower and sucks a sweet liquid called nectar. She carries it home in a special stomach and turns it into honey. While she moves among the flowers, tiny grains of pollen stick to her legs and fall on the next flower she visits. In this way bees help plants to produce fruits and seeds. Many of the fruits we eat would not exist without them.</p>
<p>When a bee finds a good patch of flowers, she returns to the hive and performs a dance. The direction and length of her dance tell the other bees where the flowers are and how far they must fly. Scientists call this the 'waggle dance'. Today, however, honeybees are in danger because of pesticides and the loss of wild flowers. If we wish to save them, we must grow more flowering plants and use fewer chemicals.</p>""",
[m("Who is the only bee that lays eggs in the colony?", ["The queen", "The drone", "The worker", "The guard"]),
 m("Worker bees are:", ["all female", "all male", "both male and female", "only young bees"]),
 m("Bees help plants by carrying:", ["pollen", "water", "honey", "wax"]),
 S("State whether True or False: Drone bees do most of the work in the hive.", "b", 1, ["True", "False"]),
 m("The 'waggle dance' is used to tell other bees:", ["where the flowers are", "that the queen is ill", "when it will rain", "how to make honey"]),
 S("Name two jobs of the worker bees.", "Any two: cleaning the hive, feeding the young bees, guarding the door, collecting food.", 1),
 S("How does a worker bee carry nectar to the hive?", "In a special stomach.", 1),
 S("Why are honeybees in danger today?", "Because of pesticides and the loss of wild flowers.", 1),
 S("Find a word in the passage that means 'a large number of bees living together'.", "Colony.", 1),
 S("What does 'she' in the last paragraph ('she returns to the hive') refer to?", "The worker honeybee that found a good patch of flowers.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>The Lost Kite</b></p>
<p>It was the last day of the kite festival, and the sky over Jaipur was full of colours. Meena stood on her terrace holding a bright red kite that her grandfather had made for her. "Hold the string gently," he had said, "and let the wind do the work."</p>
<p>The kite rose higher and higher until it looked like a small red flower in the blue sky. Meena laughed with joy. Suddenly a boy on a nearby roof sent his green kite across her string. Snap! Her red kite jerked, tore free and floated away over the houses.</p>
<p>Meena's eyes filled with tears. She ran down the stairs and out into the lane, following the kite with her eyes. It dropped at last near the old well at the end of the street. When she reached the spot, she found the green-kite boy already there. He was holding her red kite carefully in his hands.</p>
<p>"I am sorry," he said. "I was only trying to win, but I never wished to spoil your day. I have mended the torn corner with a little glue." Meena looked at the neat repair and smiled. "Thank you," she said. "Come, let us fly it together." That evening, two kites, one red and one green, danced side by side above the town.</p>""",
[m("Who had made the red kite for Meena?", ["Her grandfather", "Her father", "Her brother", "The green-kite boy"]),
 m("Why did Meena's kite float away?", ["Another kite cut her string", "The wind stopped", "She let go of it", "It was too heavy"]),
 m("Where did the red kite fall?", ["Near the old well", "On a roof", "In a garden", "In a river"]),
 S("State whether True or False: The boy refused to return the kite.", "b", 1, ["True", "False"]),
 m("The word 'mended' in the passage means:", ["repaired", "broke", "painted", "lost"]),
 S("What advice did the grandfather give Meena about flying the kite?", "To hold the string gently and let the wind do the work.", 1),
 S("How did Meena feel when the kite went away?", "She felt sad and her eyes filled with tears.", 1),
 S("Why did the boy say he was sorry?", "He had only wished to win and had not meant to spoil her day.", 1),
 S("How did the boy repair the kite?", "He mended the torn corner with a little glue.", 1),
 S("What does the ending of the story show about Meena? Choose one quality and give a reason.", "She is forgiving/kind; she accepted his apology and invited him to fly the kite together.", 1)],
 title="Read the story and answer the questions that follow."),
)

SETS[2] = dict(
P1=P("""<p><b>Where Does the Rain Come From?</b></p>
<p>The rain that falls on our fields has a long story behind it. It begins when the heat of the sun warms the water in oceans, rivers and ponds. Some of this water turns into an invisible gas called water vapour and rises into the air. This process is known as evaporation. Plants also give out water vapour through their leaves.</p>
<p>As the vapour rises, it meets colder air and cools down. The cooled vapour changes back into tiny drops of water. This is called condensation. Millions of such drops gather around dust particles and join together to form clouds. When the drops become too heavy to stay in the air, they fall to the earth as rain. In very cold places the drops freeze and fall as snow or hail.</p>
<p>The rainwater flows into streams and rivers, soaks into the ground or fills lakes and ponds, and the journey starts again. This endless movement of water is called the water cycle. Because the same water is used again and again, the earth never runs out of it, but clean and drinkable water is limited. That is why we should not waste it and should save rainwater wherever we can.</p>""",
[m("The process by which water turns into vapour is called:", ["evaporation", "condensation", "freezing", "melting"]),
 m("Clouds are formed when:", ["tiny water drops join together", "dust rises from the ground", "the wind blows hard", "the sun sets"]),
 m("In very cold places the drops may fall as:", ["snow or hail", "dew", "fog", "steam"]),
 S("State whether True or False: Plants also give out water vapour.", "a", 1, ["True", "False"]),
 m("The writer suggests that we should:", ["save rainwater", "stop using water", "avoid rivers", "dig more wells"]),
 S("What makes water in oceans and rivers turn into vapour?", "The heat of the sun.", 1),
 S("What is the name of the process in which vapour changes back into drops?", "Condensation.", 1),
 S("What happens to the rainwater after it falls on the earth?", "It flows into streams and rivers, soaks into the ground or fills lakes and ponds.", 1),
 S("Find a word in the passage that means 'cannot be seen'.", "Invisible.", 1),
 S("Why is it important not to waste water even though the water cycle never ends?", "Because clean and drinkable water is limited.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p style="text-align:center"><b>The Rain Song</b></p>
<p style="text-align:center">The sky wears a coat of grey today,<br>
And the thunder begins to drum;<br>
The crows fly home in a noisy line<br>
To say that the rains have come.</p>
<p style="text-align:center">The dusty road turns shining wet,<br>
The leaves bend down to drink;<br>
A frog sits up on a little stone<br>
And gives me a bright green wink.</p>
<p style="text-align:center">My paper boat, so small and white,<br>
Goes sailing down the lane;<br>
It dips and bobs and spins around,<br>
Then sails off in the rain.</p>
<p style="text-align:center">Mother calls me in for tea,<br>
But I would rather stay<br>
And dance with the drops on the open road<br>
Till the clouds have gone away.</p>""",
[m("The poet says the sky wears a coat of:", ["grey", "gold", "red", "white"]),
 m("The crows fly home because:", ["the rains have come", "it is night", "they are hungry", "they are afraid of the frog"]),
 m("The leaves 'bend down to drink' means that they:", ["are heavy with rain", "are dying", "are falling", "are dry"]),
 S("State whether True or False: The poet's paper boat sinks at once.", "b", 1, ["True", "False"]),
 m("The poet's mood in the poem is:", ["joyful", "angry", "lonely", "frightened"]),
 S("What does the thunder sound like in the poem?", "A drum.", 1),
 S("What does the frog do?", "It sits on a little stone and gives the poet a bright green wink.", 1),
 S("Why does Mother call the poet inside?", "For tea.", 1),
 S("Pick out a pair of rhyming words from the first stanza.", "drum – come.", 1),
 S("Why does the poet not want to go in? Answer in one sentence.", "He/she would rather stay and dance in the rain until the clouds go away.", 1)],
 title="Read the poem and answer the questions that follow."),
)

SETS[3] = dict(
P1=P("""<p><b>The Joy of Reading</b></p>
<p>A book is a window that opens on the whole world. When we read, we can sail across oceans with a sailor, climb mountains with an explorer or travel into space with an astronaut, and all this without leaving our chair. Readers learn new words, think more clearly and write better than those who rarely read. Most importantly, a good book gives us company in moments when we feel alone.</p>
<p>Yet many children today spend more time with phones and television than with books. Screens are not bad in themselves, but they ask us to sit back and watch, while a book asks us to imagine. When we read about a forest, we must draw the trees and the birds in our own minds. This exercise makes the imagination strong, just as running makes the legs strong.</p>
<p>Developing the habit of reading is not difficult. One can begin with just ten minutes each day, choosing stories about subjects that one enjoys. A library card is free in many places, so cost need not stop anyone. Parents and teachers can help by reading aloud and by letting children choose their own books. A child who learns to love books carries a treasure that can never be stolen.</p>""",
[m("The writer compares a book to:", ["a window", "a door", "a mirror", "a ladder"]),
 m("Readers usually:", ["learn new words", "forget words", "speak less", "write badly"]),
 m("Screens ask us to:", ["sit back and watch", "imagine the scene", "draw pictures", "run and play"]),
 S("State whether True or False: A library card is free in many places.", "a", 1, ["True", "False"]),
 m("Which of these is the best title for the last paragraph?", ["Forming the Reading Habit", "The Cost of Books", "Dangers of Television", "A Visit to a Library"]),
 S("Name one thing we can do through reading without leaving our chair.", "Any one: sail across oceans, climb mountains, travel into space.", 1),
 S("How does reading make the imagination strong?", "We have to picture the scenes in our own minds, which is an exercise like running for the legs.", 1),
 S("How much time does the writer suggest for beginning the reading habit?", "Ten minutes each day.", 1),
 S("Find a word in the passage that means 'a person who travels to unknown places to discover things'.", "Explorer.", 1),
 S("What does 'a treasure that can never be stolen' mean?", "The love of reading/knowledge stays with a person for life and no one can take it away.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>The Clay Horse</b></p>
<p>In a small village by the river lived an old potter named Haridas. Every morning he sat at his wheel and made pots, lamps and toys of clay. The best of his toys was a little horse with a proud neck and bright painted eyes. He kept it on the shelf and would not sell it to anyone.</p>
<p>One day a poor boy called Gopal stood outside the shop for a long time. His clothes were torn, but his eyes were fixed on the clay horse. "Do you like it?" asked the potter. Gopal nodded. "I have only two coins," he said, "but my sister is ill, and I wished to bring her something to smile at."</p>
<p>Haridas looked at the boy and then at the horse. For a moment he said nothing. Then he took the horse down, wrapped it in a cloth and put it in Gopal's hands. "Keep your coins," he said, "and take it home." The boy ran off with shining eyes.</p>
<p>A week later the village fair was held. The potter's shop was crowded as never before, for Gopal's sister had shown the horse to all her friends, and every child wanted one. That day Haridas sold more toys than he had in a whole year. He smiled and said to himself, "A kindness never goes empty-handed."</p>""",
[m("Haridas was a:", ["potter", "farmer", "teacher", "painter"]),
 m("Why did Gopal come to the shop?", ["He wished to buy a toy for his sick sister", "He wished to sell coins", "He wanted to learn pottery", "He was lost"]),
 m("How many coins did Gopal have?", ["Two", "Five", "Ten", "None"]),
 S("State whether True or False: Haridas took money from Gopal for the horse.", "b", 1, ["True", "False"]),
 m("The moral of the story is that:", ["kindness is rewarded", "toys are costly", "fairs are crowded", "rivers are useful"]),
 S("Describe the clay horse in your own words.", "It had a proud neck and bright painted eyes.", 1),
 S("Why did Gopal want the horse?", "He wanted to give his ill sister something to smile at.", 1),
 S("Why did the potter's shop become crowded at the fair?", "Gopal's sister showed the horse to her friends and every child wanted one.", 1),
 S("Find a word in the passage that means 'stared steadily'. (Hint: second paragraph)", "Fixed (his eyes were fixed).", 1),
 S("What did Haridas mean by 'A kindness never goes empty-handed'?", "A good deed always brings some good return to the doer.", 1)],
 title="Read the story and answer the questions that follow."),
)

SETS[4] = dict(
P1=P("""<p><b>The Roof of the World</b></p>
<p>Mountains are among the most magnificent features of the earth. They rise high above the land around them, and their tops are often covered with snow throughout the year. The highest mountain in the world is Mount Everest in the Himalayas. It is about 8,849 metres tall and lies on the border between Nepal and Tibet. Because of its height, Everest is sometimes called 'the roof of the world'.</p>
<p>Climbing a high mountain is a difficult task. The air at great heights is thin, which means there is less oxygen to breathe, and climbers often carry cylinders of oxygen with them. The temperature can fall far below zero, and fierce winds and sudden storms add to the danger. Climbers therefore train for months and travel with guides who know the mountain well.</p>
<p>In 1953 Edmund Hillary of New Zealand and Tenzing Norgay, a Sherpa from Nepal, became the first people to reach the top of Everest. Years later, in 1984, Bachendri Pal became the first Indian woman to do so. Her success inspired thousands of girls in India to take up adventure sports. Mountains teach us patience, courage and respect for nature, and they remind us that great goals are reached one careful step at a time.</p>""",
[m("Mount Everest is situated in the:", ["Himalayas", "Alps", "Andes", "Aravallis"]),
 m("Everest is sometimes called:", ["the roof of the world", "the king of hills", "the white giant", "the sky tower"]),
 m("Climbers carry oxygen cylinders because:", ["the air is thin at great heights", "they are afraid of snow", "the guides ask them to", "water is scarce"]),
 S("State whether True or False: Bachendri Pal was the first Indian woman to climb Everest.", "a", 1, ["True", "False"]),
 m("Which of the following was NOT mentioned as a danger of climbing?", ["Wild animals", "Fierce winds", "Sudden storms", "Very low temperature"]),
 S("How tall is Mount Everest?", "About 8,849 metres.", 1),
 S("Who were the first people to reach the top of Everest, and in which year?", "Edmund Hillary and Tenzing Norgay, in 1953.", 1),
 S("Why do climbers train for months and take guides?", "Because climbing is difficult and dangerous, and guides know the mountain well.", 1),
 S("Find a word in the passage that means 'very grand and beautiful'.", "Magnificent.", 1),
 S("What do mountains teach us, according to the writer? Mention any two things.", "Any two: patience, courage, respect for nature.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p style="text-align:center"><b>Grandmother's Garden</b></p>
<p style="text-align:center">Behind my grandmother's old stone house<br>
There is a garden small,<br>
With marigolds and curry leaves<br>
Along the crumbling wall.</p>
<p style="text-align:center">She wakes before the sparrows do<br>
And waters every plant;<br>
She talks to them in a whisper-song<br>
As though each one could chant.</p>
<p style="text-align:center">"A seed," she says, "is a promise, child,<br>
Which must be kept with care;<br>
A little water, a little love,<br>
And the sun will do its share."</p>
<p style="text-align:center">Now Grandma's gone, but every spring<br>
The marigolds still smile,<br>
And I keep her promise in my heart<br>
And in a flowerbed pile.</p>""",
[m("The garden is situated:", ["behind the grandmother's house", "in front of a school", "near a river", "on a hill"]),
 m("Which plants grow in the garden?", ["Marigolds and curry leaves", "Roses and lilies", "Mango trees", "Cactus"]),
 m("According to the grandmother, a seed is:", ["a promise", "a toy", "a burden", "a puzzle"]),
 S("State whether True or False: The grandmother woke up after the sparrows.", "b", 1, ["True", "False"]),
 m("The last stanza suggests that the grandmother is:", ["no longer alive", "travelling", "asleep", "angry"]),
 S("How does the grandmother talk to the plants?", "In a whisper-song.", 1),
 S("What three things does a seed need, according to the grandmother?", "A little water, a little love and the sun.", 1),
 S("What does the poet do to remember the grandmother?", "She/he keeps the grandmother's promise in the heart and tends the flowerbed.", 1),
 S("Pick out a pair of rhyming words from the second stanza.", "plant – chant.", 1),
 S("What value does the poem teach? Answer in one sentence.", "Caring for nature and keeping the memory of loved ones alive through our actions.", 1)],
 title="Read the poem and answer the questions that follow."),
)

SETS[5] = dict(
P1=P("""<p><b>Safe on the Road</b></p>
<p>Every year thousands of people are hurt in road accidents, and many of these could be avoided if everyone followed a few simple rules. The first rule for a pedestrian is to walk on the footpath. Where there is no footpath, one should walk on the right side of the road, facing the traffic, so that vehicles coming from the front can be seen in time. Roads should be crossed only at zebra crossings or where the signal is green for pedestrians.</p>
<p>Traffic lights use three colours. Red means 'stop', yellow means 'get ready', and green means 'go'. Drivers who jump a red light put themselves and others in great danger. A person riding a two-wheeler must wear a helmet, and passengers in a car should fasten their seat belts. Children below a certain age should never be allowed to drive.</p>
<p>Good road sense is a habit that must be learnt early. Schools can help by organising road safety weeks and by inviting traffic police officers to talk to students. At home, parents should set an example by following the rules themselves. A few seconds saved by breaking a rule can cost a life, but a few seconds spent in waiting can save one.</p>""",
[m("A pedestrian should cross the road at:", ["a zebra crossing", "any bend", "the middle of the road", "a petrol pump"]),
 m("The yellow light in a traffic signal means:", ["get ready", "stop", "go", "turn back"]),
 m("Where there is no footpath, one should walk:", ["on the right side facing the traffic", "on the left with traffic behind", "in the middle", "behind a vehicle"]),
 S("State whether True or False: Riders of two-wheelers must wear helmets.", "a", 1, ["True", "False"]),
 m("Which is the best title for the passage?", ["Rules for Road Safety", "A Day at the Zebra Crossing", "The Traffic Police", "How to Drive"]),
 S("Why should one walk facing the traffic?", "So that vehicles coming from the front can be seen in time.", 1),
 S("What should passengers in a car do for safety?", "Fasten their seat belts.", 1),
 S("How can schools help in teaching road sense?", "By organising road safety weeks and inviting traffic police officers to talk to students.", 1),
 S("Find a word in the passage that means 'a person who walks on the road'.", "Pedestrian.", 1),
 S("Explain the last sentence of the passage in your own words.", "Breaking a rule to save a little time may cost a life, but waiting a few seconds can save a life.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>The Last Bus</b></p>
<p>Arjun stood at the bus stop with his school bag and an umbrella. It was nearly seven in the evening, and the rain had been falling since afternoon. He had stayed back for the science club meeting, and now the streets were almost empty. A cold wind blew, and the streetlights flickered on one by one.</p>
<p>At last the headlights of the last bus shone through the rain. Arjun was about to step in when he noticed a small girl sitting on the bench, hugging a wet bag and trying hard not to cry. "I have missed my bus," she said in a trembling voice. "I do not know the way home."</p>
<p>Arjun thought for a moment. If he helped the girl, he would reach home late, and his mother would worry. But he could not leave a child alone in the dark. He asked her where she lived. It was a lane close to his own colony. "Come with me," he said, and held the umbrella over her head.</p>
<p>They rode together, and Arjun walked her to her door. Her father hugged her tightly and thanked him again and again. When Arjun reached his own house, his mother was waiting anxiously at the gate. She listened to the whole story and then said softly, "I am not angry. I am proud of you."</p>""",
[m("Why was Arjun late at school?", ["He attended the science club meeting", "He missed the bus", "He was ill", "He had a test"]),
 m("What was the weather like?", ["Rainy and windy", "Hot and sunny", "Foggy", "Snowy"]),
 m("The girl was upset because she had:", ["missed her bus", "lost her umbrella", "lost her friend", "failed a test"]),
 S("State whether True or False: Arjun left the girl alone at the bus stop.", "b", 1, ["True", "False"]),
 m("Arjun's mother was:", ["proud of him", "angry with him", "unaware of anything", "unhappy with the girl"]),
 S("Where did Arjun hold the umbrella?", "Over the little girl's head.", 1),
 S("What worry did Arjun have before deciding to help?", "He would reach home late and his mother would worry.", 1),
 S("How did the girl's father react?", "He hugged his daughter tightly and thanked Arjun again and again.", 1),
 S("Find a word in the passage that means 'worried and nervous'.", "Anxiously.", 1),
 S("What quality of Arjun is shown in the story? Give one reason.", "Kindness/responsibility; he helped a lost child even though he would be late.", 1)],
 title="Read the story and answer the questions that follow."),
)
