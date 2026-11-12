from evs_common6 import *

q = []
q.append(mcq("These pots are made by a:", ["potter (kumhar)", "carpenter", "weaver", "blacksmith"], 0, fig=pic("🏺🏺🏺 🔥")))
q.append(mcq("The famous 'blue pottery' is associated with which city of Rajasthan?", ["Jodhpur", "Jaipur", "Udaipur", "Kota"], 1))
q.append(Q("Write the main building material of each house.", 3, "", parts=[
    P("(i)", "Haveli of Jaisalmer", 1, "Yellow sandstone."),
    P("(ii)", "Igloo (home of people in the Arctic)", 1, "Blocks of ice / hard snow."),
    P("(iii)", "Kuccha village house", 1, "Mud, straw / bamboo / thatch.")]))
q.append(cities_q([dq("(a)", "Jodhpur", "Mount Abu", 2, "south"), dq("(b)", "Jaipur", "Alwar", 2, "north-east"),
                   P("(c)", "Which city shown in the figure lies farthest to the south?", 1, "Banswara."),
                   P("(d)", "Name one state that lies to the north of Rajasthan.", 1, "Punjab or Haryana.")]))
q.append(mcq("Which animal gives us wool?", ["Sheep", "Cow", "Hen", "Dog"], 0))
q.append(Q("Write any three things that a safe and healthy house should have.", 3, "Any three: fresh air and light (windows); clean drinking water; toilet and drainage; strong roof and walls; kitchen with smoke outlet; garbage disposal."))
q.append(Q("", 8, "", parts=[
    P("(i)", "Write <b>four</b> tips to keep your house clean and safe.", 4,
      "Any four: sweep and mop daily; keep dustbin covered; do not let water collect (mosquitoes); keep medicines and sharp tools away from small children; switch off electric switches properly."),
    P("(ii)", "Look at the picture: " + pic("🏗️🧱 👷 &nbsp; 🧒") + "A child is playing near a building under construction while a worker is working. (a) What danger do you see? (b) What would you tell the child?", 4,
      "(a) Bricks or tools may fall on the child; the site has machines and holes (2). (b) Do not play at a construction site; play in a safe park and tell an adult (2).")]))
q.append(mcq("Poha is made from:", ["wheat", "rice", "maize", "bajra"], 1))
q.append(mcq("Jaggery (gur) is made from the juice of:", ["sugarcane", "wheat", "mustard", "gram"], 0))
q.append(Q("Write any three differences between a <b>kuccha</b> house and a <b>pucca</b> house.", 3,
           "Kuccha: mud, straw, bamboo; weak, damaged by heavy rain; needs frequent repair. Pucca: bricks, cement, stone; strong and long-lasting; safe in rain."))
q.append(Q("People say that all professions deserve equal respect. Do you agree?", 3, "", parts=[
    P("(i)", "Give two reasons.", 2, "Yes. Every worker (farmer, sweeper, teacher, mason) does useful work and society depends on all of them."),
    P("(ii)", "Name one profession you admire.", 1, "Any, e.g. doctor, farmer, teacher.")]))
q.append(Q("A Kathputli (string puppet) artist performs at a village fair.", 3, "", parts=[
    P("(i)", "Write two questions you would ask him about his art.", 2, "e.g. Who makes the puppets? How long did you take to learn to move the strings? Whose stories do you tell?"),
    P("(ii)", "Write one way to help such artists.", 1, "Watch and buy their work; encourage children to learn the art.")]))
q.append(Q("Houses in the desert have thick walls, small windows and are painted in light colours. Give three reasons.", 3,
           "Thick walls keep the heat out and the house cool; small windows keep out hot winds and dust; light colours reflect sunlight."))
q.append(Q("", 6, "", parts=[
    P("(a)", "Match the area with the kind of house." + match(["Snowy hills", "Heavy rain / flood-prone Assam", "Hot, dry desert"],
        ["Thick walls and flat roof", "Sloping roofs so that snow slides off", "House raised on stilts"]), 3, "1-b, 2-c, 3-a."),
    P("(b)", "Match the city with its founder." + match(["Jaipur", "Jodhpur", "Udaipur"],
        ["Rao Jodha", "Maharana Udai Singh II", "Sawai Jai Singh II"]), 3, "1-c, 2-a, 3-b.")]))
q.append(Q("", 8, "", parts=[
    P("(i)", "Raju's house: after the front door you enter the verandah. Straight ahead is the living room. The kitchen is to the right of the living room and the bedroom is to its left. The bathroom is behind the bedroom and the store room is behind the kitchen. "
      "(a) Which room do you enter first? (b) Which room is on the left of the living room? (c) Which room is behind the kitchen? (d) Name the two rooms at the back of the house.", 4,
      "(a) Verandah (b) Bedroom (c) Store room (d) Bathroom and store room."),
    P("(ii)", "Shanti makes cloth bags from old sarees and sells them at the fair. (a) Why is this good for the environment? (b) Name one other useful thing that can be made from waste.", 4,
      "(a) Old cloth is reused, so less waste and fewer plastic bags are used (2). (b) e.g. a pen stand from a tin, a toy from waste cloth, a flower pot from a bottle (2).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "A metal spoon and a wooden spoon are left in hot tea. (i) Which gets hot? (ii) Why do cooking pans have wooden or plastic handles? (iii) Name one more material that is a good conductor of heat.", 3,
      "(i) Metal spoon (1). (ii) They do not get hot, so we can hold them (1). (iii) Iron / copper / aluminium (1)."),
    P("(b)", "Cities are hotter than nearby villages. Write two reasons and one way to reduce the heat.", 3,
      "Reasons: concrete and tar take in heat; few trees; smoke of vehicles / air conditioners (2). Plant more trees (1).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Give a reason: (i) walls are white-washed in summer (ii) old havelis have stone <i>jaalis</i> (lattice) (iii) a house needs windows opposite each other.", 3,
      "(i) White reflects the sun's heat. (ii) Let air in and give shade / privacy. (iii) Fresh air flows through (ventilation)."),
    P("(b)", "Arrange the steps of rooftop rainwater harvesting in order: (A) water goes to the tank (B) rain falls on the roof (C) pipe carries the water down (D) water passes through a filter.", 3,
      "B, C, D, A.")]))
q.append(mcq("Road signs shaped like a triangle usually give:", ["an order", "a warning", "a prohibition", "information about food"], 1))
q.append(Q("On Makar Sankranti people eat til-gur laddoos and fly kites.", 3, "", parts=[
    P("(i)", "Why are til (sesame) and gur (jaggery) good in winter?", 1, "They give warmth and energy."),
    P("(ii)", "Why is kite string with glass (manjha) dangerous?", 1, "It can cut people and kill birds."),
    P("(iii)", "Where should you fly a kite safely?", 1, "On an open ground / terrace away from roads and electric wires.")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Match the professional with the tool." + match(["Farmer", "Carpenter", "Potter"], ["Wheel (chaak)", "Saw and hammer", "Plough"]), 3, "1-c, 2-b, 3-a."),
    P("(b)", "Fill in the blanks: (i) A ___ is needed to drive a car. (ii) An overloaded vehicle is ___. (iii) A helmet protects the ___.", 3,
      "(i) driving licence (ii) dangerous (iii) head.")]))
q.append(mcq("Who brings letters to our house?", ["Postman", "Pilot", "Conductor", "Guard"], 0))
q.append(Q("", 6, "", parts=[
    P("(a)", "Who is responsible? (i) keeping village land records (ii) giving vaccines at the village sub-centre (iii) registering a complaint (FIR).", 3,
      "(i) Patwari (ii) ANM / nurse (iii) Police."),
    P("(b)", "Write the use of each plant: (i) Aloe vera (ii) Giloy (iii) Haldi (turmeric).", 3,
      "(i) Gel soothes burns and skin. (ii) Helps in fever / immunity. (iii) Antiseptic for small cuts.")]))
run(8, q)
