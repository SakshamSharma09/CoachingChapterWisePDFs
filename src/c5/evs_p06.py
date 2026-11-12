from evs_common6 import *

q = []
q.append(mcq("Look at the picture. It is related to:", ["rainwater harvesting", "a flood", "a drought", "a forest fire"], 0,
             fig=pic("🏠🌧️ ➡️ 🛢️ 💧")))
q.append(mcq("Which folk dance of Rajasthan is performed by women in long, swirling skirts?", ["Bhangra", "Garba", "Ghoomar", "Bihu"], 2))
q.append(Q("Write one line about each of the following water structures of Rajasthan.", 3, "",
           parts=[P("(i)", "Johad", 1, "A small earthen dam / pond that stores rainwater."),
                  P("(ii)", "Tanka (Kund)", 1, "A covered tank (often underground) that stores rainwater, used in desert areas."),
                  P("(iii)", "Baori (step well)", 1, "A deep well with steps going down to the water.")]))
q.append(cities_q([dq("(a)", "Jaipur", "Jodhpur", 2, "west"), dq("(b)", "Jodhpur", "Bikaner", 2, "north"),
                   P("(c)", "Which city shown in the figure lies in the extreme north?", 1, "Ganganagar."),
                   P("(d)", "Name the state that lies to the south-west of Rajasthan.", 1, "Gujarat.")]))
q.append(mcq("Which of these crops needs the <b>least</b> water?", ["Paddy (rice)", "Sugarcane", "Bajra", "Banana"], 2))
q.append(Q("Write any three ways of saving water at home.", 3, "Any three: close the tap while brushing / soaping; repair leaking taps; use a bucket and mug instead of a shower or hose; reuse water used for washing vegetables to water plants; collect rainwater."))
q.append(Q("", 8, "", parts=[
    P("(i)", "Write <b>four</b> short slogans or points for a poster on <i>'Save Every Drop'</i> to be put near the school taps.", 4,
      "Any four, e.g. Every drop counts; Close the tap, save a life; Water saved is water earned; Do not waste water, tomorrow needs it; Fix a leaking tap today."),
    P("(ii)", "Look at the picture: " + pic("🚿💧 👦🪥 &nbsp; 🚰💧💧 &nbsp; 🚗🚿 &nbsp; 🪣") +
      "A boy brushes his teeth with the tap running, a tap is leaking and a man washes his car with a hose pipe. (a) Which habits are wrong? (b) What would you advise them?", 4,
      "(a) Leaving the tap running while brushing, the leaking tap, washing a car with a running hose (2). (b) Use a mug of water, repair the tap at once, wash the car with a bucket and wet cloth (2).")]))
q.append(mcq("Which of these crops needs the <b>most</b> water?", ["Gram", "Mustard", "Bajra", "Paddy (rice)"], 3))
q.append(mcq("Which of these is a <b>Rabi</b> crop (sown in winter)?", ["Bajra", "Maize", "Wheat", "Cotton"], 2))
q.append(Q("Write any three differences between <b>surface water</b> and <b>ground water</b>.", 3,
           "Surface water is found on the earth's surface (river, lake, pond); ground water is found under the ground. Surface water can be seen; ground water is taken out with wells, handpumps or tube wells. Ground water is refilled when rainwater seeps into the soil."))
q.append(Q("Some people say that using a bucket and mug is better than taking a shower. Do you agree?", 3, "", parts=[
    P("(i)", "Give two reasons for your opinion.", 2, "Yes. A bucket and mug use much less water than a running shower; saves water for others and for the future."),
    P("(ii)", "Write one more thing you can do to save water.", 1, "Any: reuse water for plants, close taps tightly.")]))
q.append(Q("Women in many desert villages walk long distances to fetch water in matkas.", 3, "", parts=[
    P("(i)", "Write two questions you would ask them.", 2, "e.g. How far do you walk every day? How long does it take? Is the water clean? What do you do if the pond dries?"),
    P("(ii)", "Write one way to make their work easier.", 1, "e.g. a handpump or a pipe supply near the village, a johad or tanka close by.")]))
q.append(Q("Desert houses keep their water tanks (kunds) <b>covered</b>. Give three reasons.", 3,
           "Covering stops water evaporating in the heat; keeps dust, leaves and insects out so the water stays clean; stops mosquitoes breeding and children or animals falling in."))
q.append(Q("", 6, "", parts=[
    P("(a)", "Which of these states have a sea coast? Write the names of any three.<br>Gujarat, Rajasthan, Kerala, Haryana, Odisha, Madhya Pradesh", 3, "Gujarat, Kerala, Odisha (any three of these)."),
    P("(b)", "Match the person with the work." + match(["Rajendra Singh", "Maharana Pratap", "Bhamashah"],
        ["Gave his wealth to help Maharana Pratap", "Fought the battle of Haldighati", "Revived johads in Alwar villages"]), 3, "1-c, 2-b, 3-a.")]))
q.append(Q("", 8, "", parts=[
    P("(i)", "Write whether each use of water is a <b>home</b> use or a <b>farm</b> use: (a) cooking (b) watering the wheat field (c) bathing (d) irrigating the mustard field.", 4,
      "(a) home (b) farm (c) home (d) farm. (1 mark each)"),
    P("(ii)", "The people of Dhani village cleaned their old johad and built a bund before the monsoon. Next year the water in their wells rose. (a) Why did the water level in the wells rise? (b) What lesson do we learn?", 4,
      "(a) The johad held the rainwater, which slowly seeped into the ground and refilled the wells (2). (b) Working together to store rainwater solves water problems (2).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Sort these into things that <b>float</b>, <b>sink</b> or <b>dissolve</b> in water: cork, stone, sugar, iron nail, leaf, salt.", 3,
      "Float: cork, leaf. Sink: stone, iron nail. Dissolve: sugar, salt. (1 mark per group)"),
    P("(b)", "Why is it cooler near a pond under a tree than on a tar road at noon?", 3,
      "Tar/concrete roads take in a lot of heat and give it out (1); water evaporates and cools the air (1); the tree gives shade (1).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "A leaking tap wastes 5 litres of water every hour. How many litres are wasted in one day? How many 10-litre buckets is that?", 3,
      "5 x 24 = 120 litres (2). 120 / 10 = 12 buckets (1)."),
    P("(b)", "Climate is changing and rains have become uneven. Write two causes of climate change and one thing you can do.", 3,
      "Causes: burning petrol, diesel and coal; cutting down forests (2). Plant trees / save energy (1).")]))
q.append(mcq("A round red road sign with a white horizontal bar means:", ["No entry", "Hospital ahead", "School ahead", "Turn left"], 0))
q.append(Q("In summer, people set up <b>pyau</b> (water huts) on roadsides in Rajasthan.", 3, "", parts=[
    P("(i)", "Why do people set up pyau?", 1, "To give free drinking water to thirsty travellers."),
    P("(ii)", "Why does water in a clay matka stay cool?", 1, "Water seeps through tiny pores and evaporates, which cools the matka."),
    P("(iii)", "Why should the matka be covered?", 1, "To keep out dust and insects.")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Match the transport with its use." + match(["Boat", "Camel", "Aeroplane"],
        ["Travelling quickly between far-away cities", "Carrying people and loads across sand", "Crossing a river"]), 3, "1-c, 2-b, 3-a."),
    P("(b)", "Fill in the blanks: (i) Always wear a ___ while riding a two-wheeler. (ii) Cross the road at the ___ crossing. (iii) A ___ traffic light means stop.", 3,
      "(i) helmet (ii) zebra (iii) red.")]))
q.append(mcq("Which is the fastest way to send a written message to a friend living in another country?", ["Postcard", "A letter sent by bus", "E-mail", "A messenger on foot"], 2))
q.append(Q("", 6, "", parts=[
    P("(a)", "Answer: (i) Who elects the members of a Gram Panchayat? (ii) Which local body removes garbage from city streets? (iii) To whom would you complain about a broken village handpump?", 3,
      "(i) The villagers (voters). (ii) The Municipality / Nagar Nigam. (iii) The Sarpanch / Gram Panchayat."),
    P("(b)", "You see a water pipe burst on the road and water flowing away. What three things would you do?", 3,
      "Tell an elder / call the water department or Panchayat; keep children away from the flowing water and the road; do not waste time, inform at once so the water supply is repaired.")]))
run(6, q)
