from evs_common6 import *

q = []
q.append(mcq("Look at the picture. It is related to life in:", ["a desert", "a sea shore", "a hill station", "a dense forest"], 0, fig=pic("🐪 🏜️ 🌵 ☀️")))
q.append(mcq("Which of these is a folk musical instrument of Rajasthan?", ["Mridangam", "Kamaicha", "Santoor", "Tabla"], 1))
q.append(Q("Write whether each is a <b>road</b>, <b>rail</b>, <b>water</b> or <b>air</b> means of transport.", 3, "", parts=[
    P("(i)", "Palace on Wheels", 1, "Rail."), P("(ii)", "Camel cart", 1, "Road."), P("(iii)", "Helicopter", 1, "Air.")]))
q.append(cities_q([dq("(a)", "Jodhpur", "Jaisalmer", 2, "west"), dq("(b)", "Jodhpur", "Ajmer", 2, "east"),
                   P("(c)", "Which city shown in the figure lies farthest to the east?", 1, "Bharatpur."),
                   P("(d)", "Which country lies to the west of Rajasthan?", 1, "Pakistan.")]))
q.append(mcq("The State Bird of Rajasthan is:", ["Peacock", "Godawan (Great Indian Bustard)", "Sparrow", "Parrot"], 1))
q.append(Q("Write any three services given by a post office.", 3, "Any three: delivering letters and parcels; speed post; money transfer (money order); savings accounts; selling stamps and envelopes."))
q.append(Q("", 8, "", parts=[
    P("(i)", "Write <b>four</b> road safety rules or slogans for a poster <i>'Be Safe on the Road'</i>.", 4,
      "Any four: wear a helmet; wear a seat belt; cross at the zebra crossing; obey traffic lights; do not use a phone while driving; do not overload vehicles."),
    P("(ii)", "Look at the picture: " + pic("🚦🔴 &nbsp; 🚶 &nbsp; 🛵 &nbsp; 🚸") +
      "The light is red. A scooter rider without a helmet is crossing and a child is waiting at the crossing. (a) What mistakes are shown? (b) What should be done?", 4,
      "(a) The rider ignores the red light and has no helmet (2). (b) Stop at red, wear a helmet; the child should cross only at the crossing when it is safe (2).")]))
q.append(mcq("Which of these is a pulse?", ["Wheat", "Moong", "Bajra", "Maize"], 1))
q.append(mcq("Which food helps to build strong bones?", ["Milk", "Sugar", "Oil", "Salt"], 0))
q.append(Q("Write any three differences between a <b>letter</b> and an <b>e-mail</b>.", 3,
           "A letter is written on paper and takes days; an e-mail is sent through the internet in seconds. A letter needs a stamp and a post box; e-mail needs a phone or computer with internet. A letter is handled by a postman; an e-mail reaches directly."))
q.append(Q("Your cousin plays mobile games all evening.", 3, "", parts=[
    P("(i)", "Give two reasons why this is harmful.", 2, "Weak eyesight and tiredness; no outdoor exercise; less time for study and family."),
    P("(ii)", "Suggest one better activity.", 1, "Playing outdoor games, reading, cycling.")]))
q.append(Q("The Camel Festival is held in Bikaner in January.", 3, "", parts=[
    P("(i)", "Write two questions you would ask a camel herder there.", 2, "e.g. How do you take care of your camel? What do camels eat? How far can a camel walk in a day?"),
    P("(ii)", "Write one thing you would like to see at the festival.", 1, "e.g. camel dance, race, decorated camels.")]))
q.append(Q("Give three reasons why we should use public transport (buses, metro) more.", 3,
           "Less smoke and air pollution; fewer vehicles and less traffic jam; costs less and saves fuel."))
q.append(Q("", 6, "", parts=[
    P("(a)", "True or false? (i) Rajasthan has a sea coast. (ii) Gujarat is a coastal state. (iii) Mumbai is a port on the Arabian Sea.", 3, "(i) False (ii) True (iii) True."),
    P("(b)", "Match the place with its fame." + match(["Ranthambore", "Keoladeo (Bharatpur)", "Chand Baori (Abhaneri)"],
        ["Famous step well", "Tiger reserve", "Bird sanctuary"]), 3, "1-b, 2-c, 3-a.")]))
q.append(Q("", 8, "", parts=[
    P("(i)", "Raman's directions to school: 'Walk straight 200 m to the post office. Turn left at the post office. The bank is on your right; the school is just after it.' "
      "(a) Where do you turn left? (b) Which building is on your right after the turn? (c) Which building comes after the bank? (d) Which building do you reach first?", 4,
      "(a) At the post office (b) The bank (c) The school (d) The post office."),
    P("(ii)", "The Jaipur Metro was started to reduce traffic. (a) Name two ways it helps the people of the city. (b) Name one way it helps the environment.", 4,
      "(a) Faster travel; fewer jams; safe and cheap (any two = 2). (b) Fewer vehicles, so less smoke and noise (2).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "An iron nail sinks but a big iron ship floats. Why? Name two other things that float.", 3,
      "The ship is hollow and wide; it pushes aside a lot of water so it floats (2). Cork, wood, leaf (1)."),
    P("(b)", "The number of cars in cities is rising. Write two effects and one alternative.", 3,
      "Air pollution, noise and traffic jams (2). Use bicycles or walk for short distances / public transport (1).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "The smoke of vehicles harms health. Write two harms to people and one harm to the earth.", 3,
      "Cough, breathing trouble, itchy eyes (2). Adds to global warming / climate change (1)."),
    P("(b)", "You have to travel from Jaipur to Jodhpur with your grandparents. Which transport would you choose and why?", 3,
      "Any sensible choice with reasons, e.g. train or bus: comfortable, safe, affordable, no worry of driving.")]))
q.append(mcq("Which traffic light colour means 'get ready / wait'?", ["Red", "Yellow (amber)", "Green", "Blue"], 1))
q.append(Q("", 3, "", parts=[
    P("(i)", "Why do people in desert areas wear a safa (turban)?", 1, "It protects the head from hot sun and dust."),
    P("(ii)", "Why should we wear light cotton clothes in summer?", 1, "Cotton lets air pass and absorbs sweat, so we feel cool."),
    P("(iii)", "Why do people wear woollen clothes in winter?", 1, "Wool keeps body heat in.")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Match the sign with its meaning." + match(["⛔", "🚸", "🅿️"], ["Parking place", "No entry", "Children crossing / school ahead"]), 3, "1-b, 2-c, 3-a."),
    P("(b)", "Fill in the blanks: (i) Drive ___ near a school. (ii) Cross the road only at a ___ crossing. (iii) Do not honk near a hospital because patients need ___.", 3,
      "(i) slowly (ii) zebra (iii) silence / quiet.")]))
q.append(mcq("How many digits does a PIN code in India have?", ["4", "5", "6", "8"], 2))
q.append(Q("", 6, "", parts=[
    P("(a)", "Name the head of: (i) Panchayat Samiti (ii) Zila Parishad (iii) Nagar Nigam (city corporation).", 3,
      "(i) Pradhan (ii) Zila Pramukh (iii) Mayor."),
    P("(b)", "You find a small lost child at a bus stand. What three things would you do?", 3,
      "Stay with the child and calm him; tell a police officer / bus staff or call 112; do not take him away alone.")]))
run(9, q)
