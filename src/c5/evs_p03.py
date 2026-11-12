from evs_h1 import *

T = ["Chittorgarh", "Bikaner", "Sirohi", "Jaisalmer"]
assert direction("Jaipur", "Sirohi")[0] == "South-West" and direction("Jaipur", "Jaisalmer")[0] == "West"

q1 = mcq("Look at the picture. It is related to which means of transport?", ["road transport", "railways", "air transport", "water transport"], 1,
         fig=emoji("&#128642;&#128643;&#128643;&#128643; &#128649; &#128738;&#65039;"))
q2 = mcq("The famous Pushkar fair, where camels are bought and sold, is held in the district of", ["Alwar", "Kota", "Ajmer", "Pali"], 2)
q3 = parts("Write <b>one use</b> of each of these animals to human beings.", 3, [
    ("Camel", 1, "Carries people and loads across the desert; its milk is drunk."),
    ("Cow", 1, "Gives milk (and curd, ghee); its dung is used as manure / fuel."),
    ("Goat", 1, "Gives milk and meat; its hair/wool is used by some communities.")])
q4 = parts("Look at the schematic map of Rajasthan. The dots <b>A, B, C, D</b> show four districts.", 6, [
    ("A has a large hill fort and the tall Vijay Stambh. B is famous for its bhujia and Camel Festival. Name A and B.", 2, "A &ndash; Chittorgarh &nbsp;&nbsp; B &ndash; Bikaner"),
    ("In which direction from Jaipur is the dot C? In which direction from Jaipur is the dot D?", 2, "C is to the <b>South-West</b> of Jaipur; D is to the <b>West</b> of Jaipur."),
    ("Name the district C, in which the hill station Mount Abu is situated.", 1, "Sirohi"),
    ("Name the district D, where the Desert Festival is held every year in February.", 1, "Jaisalmer")],
    fig=svg_locator(T))
q5 = mcq("Which animal is the National animal of India?", ["Lion", "Elephant", "Tiger", "Leopard"], 2)
q6 = parts("Birds are found everywhere around us. Answer the following.", 3, [
    ("What covers the body of a bird?", 1, "Feathers."),
    ("With which body part do most birds fly?", 1, "Wings."),
    ("How do baby birds come into the world?", 1, "Birds lay eggs, and the chicks hatch out of them.")])
q7 = Q("", 8, parts=[
    P("(i)", "Write four road-safety rules for children who walk to school.", 4,
      "Any four, e.g.: (1) Walk on the footpath. (2) Cross the road at the zebra crossing. (3) Look both sides before crossing. (4) Never run across the road. (5) Obey the traffic lights and the traffic police. [1 each]"),
    P("(ii)", "Look at the picture. The signal is red for vehicles but green for people. Some children are running across the road far from the zebra crossing. (a) What mistake are they making? (b) What should they do?", 4,
      "(a) [2] They are crossing away from the zebra crossing and running; this can lead to an accident. "
      "(b) [2] Walk to the zebra crossing, wait for the pedestrian signal, look at both sides and then cross slowly.",
      fig=emoji("&#128678; &#128652; &#128663; &#129489;&#8205;&#129309;&#8205;&#129489; &#127939;"))])
q8 = mcq("Dal-Baati-Churma is a favourite dish of Rajasthan. Baati is made from the flour of", ["rice", "wheat", "sugarcane", "tea leaves"], 1)
q9 = mcq("Rajasthan grows a large part of India&rsquo;s ______, from whose seeds we get oil.", ["mustard", "coconut", "cotton", "banana"], 0)
q10 = parts("Compare different means of transport.", 3, [
    ("Which is faster for a very long journey &ndash; an aeroplane or a bus?", 1, "Aeroplane."),
    ("Which transport can reach the smallest villages most easily?", 1, "Road transport (bus, tempo, tractor, bicycle)."),
    ("Write one advantage of travelling long distances by train.", 1, "It can carry many people and heavy goods at low cost; it is safe and comfortable.")])
q11 = Q("You are going to see the station master at a railway station. Write <b>two questions</b> you would like to ask him.", 3,
        "Any two sensible questions, e.g. (i) [2] How do you decide when a train should leave and who gives the signals? (ii) [1] How many trains stop at this station each day?")
q12 = Q("A guide is showing your class the Amer Fort. Write <b>two questions</b> you would ask him to learn about the rich heritage of Rajasthan.", 3,
        "Any two sensible questions, e.g. (i) [2] Who built the fort, and how long did it take? (ii) [1] How did people get water inside the fort?")
q13 = parts("Give reasons.", 3, [
    ("Why should a two-wheeler rider wear a helmet?", 1, "It protects the head from serious injury in case of an accident."),
    ("Why are footpaths made along roads?", 1, "So that people can walk safely, away from moving vehicles."),
    ("Why should passengers get into a bus only at a bus stop?", 1, "The bus stops there, so it is safe to get on and off, and traffic is not blocked.")])
q14 = Q("", 6, parts=[
    P("(i)", "Name the three main seasons of Rajasthan and tell in which season the monsoon rains arrive.", 3,
      "Summer, rainy (monsoon) and winter [2]. Monsoon rains arrive in the rainy season (July&ndash;September) [1]."),
    P("(ii)", "Write one fact about each.<br>(a) Meerabai &nbsp; (b) Govind Guru &nbsp; (c) Rana Kumbha", 3,
      "(a) A great devotee-poet of Lord Krishna who wrote and sang bhajans. (b) A social reformer who worked for the education and upliftment of the Bhil tribe. "
      "(c) A Mewar ruler who built many forts, including Kumbhalgarh. [1 each]")])
q15 = Q("", 8, parts=[
    P("(i)", "A village bus goes from Ramgarh to Sikri (12 km), then to Dhani (8 km) and then to Nagar (15 km). (a) How far is Nagar from Ramgarh by this route? (b) How far does the bus travel for a return trip from Ramgarh to Nagar and back? (c) Which two stops are the farthest apart on this route? (d) How much farther is Nagar from Sikri than Dhani is from Sikri?", 4,
      "(a) 12 + 8 + 15 = <b>35 km</b> (b) 35 &times; 2 = <b>70 km</b> (c) Ramgarh and Nagar (d) Sikri&ndash;Nagar = 8 + 15 = 23 km; Sikri&ndash;Dhani = 8 km; difference = <b>15 km</b> [1 each]"),
    P("(ii)", "A new railway line is built near a village that had no train. (a) Write two benefits to the villagers. (b) Write one problem that may arise.", 4,
      "(a) [2] Easy and cheap travel; farmers can send vegetables / milk to cities; new jobs (any two). "
      "(b) [2] Noise and smoke; some farmland is lost; accidents at the crossings unless the gates are used carefully (any one, explained).")])
q16 = Q("", 6, parts=[
    P("(i)", "Which of these cause no air pollution: <b>bicycle, petrol car, walking, diesel truck</b>? Why do vehicles with engines pollute the air?", 3,
      "Bicycle and walking [1]. Engines burn petrol / diesel and release smoke and harmful gases into the air [2]."),
    P("(ii)", "A big ship is made of iron and still floats, but a small iron nail sinks. (a) Why does the nail sink? (b) Why does the ship float? (c) Name another thing that floats because of its hollow shape.", 3,
      "(a) It is small and heavy for its size, so it cannot push away enough water. (b) The ship is hollow and very wide; it pushes away a lot of water and so floats. (c) boat / empty bottle / tumbler turned upside down (any one). [1 each]")])
q17 = Q("", 6, parts=[
    P("(i)", "Write any <b>three</b> effects of air pollution on people and the environment.", 3, "Cough, asthma and eye irritation; haze / smog; harm to plants and animals; dirty buildings; heating of the earth (any three)."),
    P("(ii)", "Explain the 3Rs &ndash; reduce, reuse, recycle &ndash; with <b>one example</b> each.", 3,
      "Reduce: use less, e.g. avoid plastic bags. Reuse: use again, e.g. old jars to store things. Recycle: make new things from waste, e.g. old paper into new paper. [1 each]")])
q18 = mcq("What does the <b>yellow (amber)</b> light of a traffic signal tell the drivers?", ["Speed up", "Get ready and slow down", "Park the vehicle", "Blow the horn"], 1)
q19 = parts("A plate of Dal-Baati-Churma with salad is a traditional meal of Rajasthan.", 3, [
    ("Which nutrient do we mainly get from dal?", 1, "Protein."),
    ("Why is baati served with ghee? (Which nutrient does ghee give?)", 1, "Ghee is a fat, which gives a lot of energy."),
    ("Why is a salad of fresh vegetables served with the meal?", 1, "It gives vitamins, minerals and roughage (fibre) for good health and digestion.")])
q20 = Q("", 6, parts=[
    P("(i)", "Match the emergency number with the service.<br>" + table([["1. 100", "(a) Fire brigade"], ["2. 101", "(b) Ambulance"], ["3. 108", "(c) Police"]], ["Column A", "Column B"]), 3,
      "1 &rarr; (c) &nbsp; 2 &rarr; (a) &nbsp; 3 &rarr; (b)"),
    P("(ii)", "Fill in the blanks. (a) In India, vehicles keep to the ______ side of the road. (b) We should cross the road at a ______ crossing. (c) The footpath is meant for ______.", 3,
      "(a) left (b) zebra (c) pedestrians / people walking [1 each]")])
q21 = mcq("Which means of communication lets us see and talk to a person living far away?", ["Postcard", "Video call", "Newspaper", "Radio"], 1)
q22 = Q("", 6, parts=[
    P("(i)", "Who does this work in a city? (a) puts out a fire (b) keeps law and order (c) the office that looks after cleanliness and water supply", 3,
      "(a) Fire brigade (b) Police (c) Municipal Corporation / Nagar Nigam / Nagar Palika [1 each]"),
    P("(ii)", "Write one use of each medicinal plant. (a) Giloy (b) Ajwain (c) Amla", 3,
      "(a) Helps in fever and increases immunity (strength to fight diseases). (b) Helps in stomach ache and indigestion. (c) Rich in vitamin C; keeps us healthy. [1 each]")])

run(3, [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22])
