from evs_h1 import *

T = ["Nagaur", "Ajmer", "Sikar", "Barmer"]
assert direction("Jaipur", "Nagaur")[0] == "West" and direction("Jaipur", "Sikar")[0] == "North-West"

q1 = mcq("Look at the picture. It is related to which of the following?", ["wildlife and forest", "railways", "festivals", "markets"], 0,
         fig=emoji("&#127795;&#127795; &#129434; &#128038; &#128063;&#65039; &#129421;"))
q2 = mcq("The Gangaur festival of Rajasthan is dedicated to which goddess?", ["Gauri (Parvati)", "Lakshmi", "Saraswati", "Sita"], 0)
q3 = parts("Write <b>one fact</b> about each of the following.", 3, [
    ("Rohida", 1, "It is the State flower of Rajasthan (orange-yellow flowers); a tree of the dry areas."),
    ("Banyan", 1, "It is the National tree of India; it has hanging roots and gives dense shade and a home to birds."),
    ("Lotus", 1, "It is the National flower of India; it grows in ponds and its roots are in the mud.")])
q4 = parts("Look at the schematic map of Rajasthan. The dots <b>A, B, C, D</b> show four districts.", 6, [
    ("A is the district from where the Makrana marble comes. B has the Brahma temple of Pushkar and the Ana Sagar lake. Name A and B.", 2, "A &ndash; Nagaur &nbsp;&nbsp; B &ndash; Ajmer"),
    ("In which direction from Jaipur is the dot A? In which direction from Jaipur is the dot C?", 2, "A is to the <b>West</b> of Jaipur; C is to the <b>North-West</b> of Jaipur."),
    ("Name the district C, in which the Khatu Shyam temple is situated and which is part of the Shekhawati region.", 1, "Sikar"),
    ("Name the large desert district D, which touches the border with Pakistan.", 1, "Barmer")],
    fig=svg_locator(T))
q5 = mcq("The National Chambal Sanctuary is mainly known for protecting which animal?", ["Gharial", "Tiger", "Peacock", "Camel"], 0)
q6 = parts("A fish lives in water. Answer the following.", 3, [
    ("With which organs does a fish breathe?", 1, "Gills."),
    ("Which body parts help a fish to swim?", 1, "Fins and tail."),
    ("What covers the body of a fish?", 1, "Scales.")])
q7 = Q("", 8, parts=[
    P("(i)", "Your class is starting a &lsquo;Plastic-free school&rsquo; campaign. Write four slogans or rules.", 4,
      "Any four, e.g.: (1) Say no to plastic bags, carry a cloth bag. (2) Plastic harms animals and soil. (3) Do not throw plastic in the open. (4) Bring tiffin and water in steel boxes and bottles. (5) Reduce, reuse, recycle. [1 each]"),
    P("(ii)", "Look at the picture. A cow on the road is eating a plastic bag along with the leftover food. (a) Why is it dangerous for the cow? (b) What can people do to stop this?", 4,
      "(a) [2] Plastic cannot be digested; it blocks the stomach and can make the cow very sick or even kill it. "
      "(b) [2] Do not throw food in plastic bags; use cloth / paper bags; put waste in dustbins; clean-up drives.",
      fig=emoji("&#128004; &#128717;&#65039; &#127835; &#128683;"))])
q8 = mcq("Which of these foods is the richest source of <b>vitamin C</b>?", ["Lemon", "Rice", "Sugar", "Butter"], 0)
q9 = mcq("Which of these vegetables is a <b>root</b>?", ["Spinach", "Carrot", "Cauliflower", "Tomato"], 1)
q10 = parts("Compare wild animals and pet animals.", 3, [
    ("Where does each live?", 1, "Wild animals live in forests / natural homes; pet animals live with people in or near homes."),
    ("Who looks after the food of each?", 1, "Wild animals find their own food; pet animals are fed by their owners."),
    ("Give one example of each.", 1, "Wild: tiger / chinkara / fox. Pet: dog / cat / parrot (any one each).")])
q11 = Q("A forest guard of the Sariska Tiger Reserve is visiting your school. Write <b>two questions</b> you would ask him.", 3,
        "Any two sensible questions, e.g. (i) [2] How do you protect the tigers and other animals from hunters and fires? (ii) [1] Which animals live in the forest apart from tigers?")
q12 = Q("An elder from the Bishnoi community is talking to your class about their traditions. Write <b>two questions</b> you would ask to learn about the rich culture of protecting nature.", 3,
        "Any two sensible questions, e.g. (i) [2] Why do your people protect trees and animals so strongly and how do you teach children this? (ii) [1] What are the main rules you follow?")
q13 = parts("Give reasons.", 3, [
    ("Why is a tiger reserve like Ranthambore important?", 1, "It gives tigers and other wild animals a safe home, so they are protected from hunters and from losing their forest."),
    ("Why should we keep a bowl of water for birds on the roof in summer?", 1, "In very hot weather birds cannot find water and may become sick or die of thirst."),
    ("Why should we not disturb the nests of birds?", 1, "The eggs and chicks may get hurt or die, and the birds may leave their home.")])
q14 = Q("", 6, parts=[
    P("(i)", "Name any <b>three</b> rivers which flow in Rajasthan.", 3, "Any three: Chambal, Banas, Luni, Mahi, Banganga, Ghaggar (seasonal), etc. [1 each]"),
    P("(ii)", "Write one fact about each.<br>(a) Rana Sanga &nbsp; (b) Maharaja Surajmal &nbsp; (c) Maharana Udai Singh II", 3,
      "(a) A brave Mewar king who fought Babur in the Battle of Khanwa (1527). (b) The famous ruler of Bharatpur who built the Lohagarh Fort and the Deeg palaces. "
      "(c) Founded the city of Udaipur. [1 each]")])
q15 = Q("", 8, parts=[
    P("(i)", "Arrange these four in a food chain, starting with the plant: <b>snake, grass, frog, grasshopper</b>.", 4,
      "Grass &rarr; Grasshopper &rarr; Frog &rarr; Snake. [1 for each correct place]"),
    P("(ii)", "Many years ago peacocks were seen in large numbers in Ravi&rsquo;s village. Now very few come. (a) Write two reasons why the birds have become fewer. (b) Write two things that the villagers can do.", 4,
      "(a) [2] Trees were cut so they have lost homes; chemicals / pesticides in fields harm them; hunting; no water in ponds (any two). "
      "(b) [2] Plant more trees; keep ponds and water for birds; avoid harmful chemicals; protect them (any two).")])
q16 = Q("", 6, parts=[
    P("(i)", "Write what happens when: (a) ice is kept in the sun (b) water is boiled for a long time (c) water is kept in the freezer.", 3,
      "(a) It melts and becomes water. (b) It changes to steam / vapour. (c) It freezes and becomes ice. [1 each]"),
    P("(ii)", "(a) Why do pans have wooden or plastic handles? (b) Which will become hot first in a cup of hot tea &ndash; a steel spoon or a plastic spoon? (c) Why do people hold hot vessels with a cloth?", 3,
      "(a) Wood and plastic do not allow heat to pass easily, so the handle does not burn the hand. (b) The steel spoon. (c) Cloth does not conduct heat quickly, so the hand is not burnt. [1 each]")])
q17 = Q("", 6, parts=[
    P("(i)", "Write any <b>three</b> things we can do to reduce global warming.", 3, "Plant trees; use public transport or a cycle; save electricity; avoid burning waste; use less plastic (any three)."),
    P("(ii)", "Write three ways in which water used at home can be <b>reused</b>.", 3,
      "Water used for washing vegetables / rice for plants; water from the bucket-bath for cleaning the floor; the RO reject water for mopping or the garden; water of washing clothes for the toilet (any three).")])
q18 = mcq("A road sign showing a white letter H on a blue board tells that there is a ______ ahead.", ["hospital", "hotel", "hill", "harbour"], 0)
q19 = parts("In the desert, villagers dry vegetables like sangri and ker in the sun and keep them for the whole year.", 3, [
    ("Why do people dry these vegetables?", 1, "Fresh vegetables are scarce in the desert, so they store dried ones for use later."),
    ("Name two such dried items or foods used in Rajasthan.", 1, "Ker, sangri, papad, dried gwar phali, dried methi (any two)."),
    ("Write one more way of keeping food from spoiling.", 1, "Making pickles, keeping food in a fridge, boiling and covering it (any one).")])
q20 = Q("", 6, parts=[
    P("(i)", "Match the place with what it is famous for.<br>" + table([["1. Ranthambore", "(a) migratory birds"], ["2. Keoladeo National Park", "(b) tigers"], ["3. Desert National Park", "(c) Godawan (Great Indian Bustard)"]], ["Column A", "Column B"]), 3,
      "1 &rarr; (b) &nbsp; 2 &rarr; (a) &nbsp; 3 &rarr; (c)"),
    P("(ii)", "Fill in the blanks. (a) People who travel in a bus are called ______. (b) A ship sails on ______. (c) The red light of a signal means ______.", 3,
      "(a) passengers (b) water / sea (c) stop [1 each]")])
q21 = mcq("Which of these was an old means of sending messages?", ["E-mail", "Pigeon (messenger bird)", "Video call", "Mobile app"], 1)
q22 = Q("", 6, parts=[
    P("(i)", "Who is the head of: (a) a district (as an officer) (b) a police station (c) the State government?", 3,
      "(a) District Collector (b) SHO / Station House Officer (Thanedar) (c) Chief Minister [1 each]"),
    P("(ii)", "Write one use of each medicinal plant or spice. (a) Haldi (turmeric) (b) Pudina (mint) (c) Ginger (adrak)", 3,
      "(a) Helps wounds heal, antiseptic. (b) Helps digestion. (c) Helps in cough and cold. [1 each]")])

run(5, [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22])
