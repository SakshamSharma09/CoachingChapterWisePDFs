from evs_common6 import *

q = []
q.append(mcq("Look at the picture. It shows:", ["harvesting of crops", "a flood", "a fair", "road building"], 0, fig=pic("🌾🌾 🚜 🧑‍🌾 🌾🌾")))
q.append(mcq("Which sweet is specially made in Rajasthan during the festival of Teej?", ["Rasgulla", "Ghewar", "Sandesh", "Peda"], 1))
q.append(Q("Name the main ingredient of each Rajasthani dish.", 3, "", parts=[
    P("(i)", "Bajra roti", 1, "Bajra (pearl millet) flour."),
    P("(ii)", "Gatte ki sabzi", 1, "Besan (gram flour)."),
    P("(iii)", "Baati (of Dal-Baati)", 1, "Wheat flour (cooked with ghee).")]))
q.append(cities_q([dq("(a)", "Jaipur", "Bharatpur", 2, "east"), dq("(b)", "Jaipur", "Kota", 2, "south"),
                   P("(c)", "Which city shown in the figure lies farthest to the west?", 1, "Jaisalmer."),
                   P("(d)", "Name the state that lies to the south-east of Rajasthan.", 1, "Madhya Pradesh.")]))
q.append(mcq("Which part of the carrot plant do we eat?", ["Root", "Stem", "Leaf", "Flower"], 0))
q.append(Q("Write any three ways of keeping food safe from germs.", 3, "Any three: wash hands before eating or cooking; wash fruits and vegetables; keep food covered; drink boiled / clean water; keep cooked food in clean, closed containers; do not eat stale food."))
q.append(Q("", 8, "", parts=[
    P("(i)", "Write <b>four</b> points or slogans for a school poster <i>'Eat Healthy, Stay Healthy'</i>.", 4,
      "Any four: eat fruits and green vegetables daily; drink milk; avoid too much junk food; wash hands before eating; eat at fixed times; drink enough water."),
    P("(ii)", "Look at the two tiffins: Tiffin A " + pic("🍟🥤🍫") + " Tiffin B " + pic("🥗🍎🥛🫓") + "(a) Which tiffin is better for health? Why? (b) What would you tell the child who brings Tiffin A?", 4,
      "(a) Tiffin B: it has vegetables, fruit, milk and roti which give energy and protect the body (2). (b) Eat such snacks only sometimes; bring a roti with vegetables and fruit (2).")]))
q.append(mcq("Rajasthan grows a large amount of which oilseed?", ["Mustard", "Mango", "Rice", "Tea"], 0))
q.append(mcq("Which of these is a <b>body-building</b> food?", ["Rice", "Dal", "Ghee", "Sugar"], 1))
q.append(Q("Write any three differences between <b>Kharif</b> and <b>Rabi</b> crops.", 3,
           "Kharif crops are sown in the rainy season (June-July), Rabi crops in winter (October-November). Kharif are harvested about October; Rabi about March-April. Examples: Kharif - bajra, maize; Rabi - wheat, mustard, gram."))
q.append(Q("Your friend says fast food is better than home-cooked food because it is tasty. Do you agree?", 3, "", parts=[
    P("(i)", "Give two reasons for your opinion.", 2, "No. Home food is fresh, clean and balanced; fast food has too much oil, salt or sugar and little nutrition."),
    P("(ii)", "Write one thing you would tell your friend.", 1, "Eat fast food rarely and eat dal, vegetables and roti regularly.")]))
q.append(Q("A guest from Tamil Nadu is staying in your home during Gangaur.", 3, "", parts=[
    P("(i)", "Write two questions she may ask about the festival.", 2, "e.g. Who is worshipped on Gangaur? Why do women sing and carry the idols? What special food is made?"),
    P("(ii)", "Write one thing you would like to learn about her state's festival.", 1, "e.g. How is Pongal celebrated?")]))
q.append(Q("Bajra and jowar are grown in Rajasthan more than rice. Give three reasons.", 3,
           "Rajasthan gets little rain; bajra and jowar need little water; they grow well in sandy / dry soil and heat; rice needs a lot of water."))
q.append(Q("", 6, "", parts=[
    P("(a)", "Fill in the blanks: (i) The Thar Desert lies in the ___ part of Rajasthan. (ii) Mount Abu is a hill station in the ___ range. (iii) Sambhar is a ___ lake.", 3,
      "(i) western (ii) Aravali (iii) salt."),
    P("(b)", "Match the person with the work." + match(["Meerabai", "Pannadhay", "Rana Sanga"],
        ["Fought Babur in the battle of Khanwa", "Sang bhajans in devotion to Krishna", "Sacrificed her son to save the young prince of Mewar"]), 3, "1-b, 2-c, 3-a.")]))
q.append(Q("", 8, "", parts=[
    P("(i)", "Say whether each food mainly gives <b>energy</b>, builds the <b>body</b> or <b>protects</b> the body: (a) bajra roti (b) moong dal (c) spinach (palak) (d) sugar.", 4,
      "(a) energy (b) body-building (c) protective (d) energy."),
    P("(ii)", "Every summer Dadi dries ker and sangri in the sun and stores them in jars for the year. (a) Why does she dry them? (b) Why is this useful in a desert region?", 4,
      "(a) Drying removes water, so germs and fungus cannot grow and the food does not spoil (2). (b) Fresh green vegetables are scarce in the dry season; the stored ones give vegetables all year (2).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Items: salt, sand, sugar, iron filings. (i) Which two dissolve in water? (ii) How can you separate sand from sandy water? (iii) How can you get salt back from salty water?", 3,
      "(i) Salt and sugar (1). (ii) Let it settle and pour / filter it (1). (iii) Heat the water so that it evaporates (1)."),
    P("(b)", "Meena plays outdoors and eats home food. Rohan watches TV for five hours and eats packed snacks. Write two effects on Rohan's health and one change he should make.", 3,
      "Gets tired / becomes overweight; eyesight may weaken (2). He should play outdoors and eat home food (1).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Summer in Rajasthan can bring hot winds (loo). Write three ways to avoid sunstroke.", 3,
      "Drink plenty of water / ORS / lemon water; cover the head and wear light cotton clothes; avoid going out in the afternoon sun."),
    P("(b)", "Write three ways to avoid wasting food at school or home.", 3,
      "Take only as much as you can eat; share extra food; store leftovers safely and eat them in time; feed leftovers to animals / compost vegetable waste.")]))
q.append(mcq("White stripes painted across the road (a zebra crossing) are meant for:", ["buses to stop", "people on foot to cross", "parking cars", "cycles to race"], 1))
q.append(Q("On Sheetla Saptami many families eat food cooked the day before (basoda).", 3, "", parts=[
    P("(i)", "Which goddess is worshipped on this day?", 1, "Sheetla Mata."),
    P("(ii)", "Why does cooked food spoil faster in summer than in winter?", 1, "Germs multiply faster in warm temperatures."),
    P("(iii)", "Write one way to keep food safe when there is no fridge.", 1, "Keep it covered in a clean, closed container in a cool place.")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Match the transport with its description." + match(["Palace on Wheels", "Jaipur Metro", "Rajasthan Roadways bus"],
        ["Moves on roads and links towns and villages", "A luxury tourist train", "A city rail service that runs on tracks"]), 3, "1-b, 2-c, 3-a."),
    P("(b)", "Fill in the blanks: (i) Never get on or off a ___ bus. (ii) Wear a ___ belt in a car. (iii) Look ___ and ___ before crossing the road.", 3,
      "(i) moving (ii) seat (iii) left, right.")]))
q.append(mcq("Which medium gives us news with both pictures and sound?", ["Newspaper", "Letter", "Radio", "Television"], 3))
q.append(Q("", 6, "", parts=[
    P("(a)", "Write what each plant is used for: (i) Tulsi (ii) Neem (iii) Ginger (adrak).", 3,
      "(i) cough and cold (ii) skin problems / germs (iii) sore throat and cold."),
    P("(b)", "A classmate has forgotten her tiffin. What three things would you do?", 3,
      "Share my tiffin; tell the teacher so she is not hungry; be kind and do not tease her.")]))
run(7, q)
