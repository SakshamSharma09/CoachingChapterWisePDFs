from evs_h1 import *

T = ["Bharatpur", "Jodhpur", "Sawai Madhopur", "Udaipur"]
assert direction("Jaipur", "Bharatpur")[0] == "East" and direction("Jaipur", "Udaipur")[0] == "South-West"

q1 = mcq("Look at the picture. It is related to which profession?", ["pottery", "weaving", "carpentry", "farming"], 0,
         fig=emoji("&#127994; &#127994; &#127994; &#129489;&#8205;&#127912; &#128293;"))
q2 = mcq("Which folk dance of Rajasthan is performed by women in long swirling skirts?", ["Garba", "Bihu", "Ghoomar", "Bhangra"], 2)
q3 = parts("Write <b>one feature</b> by which each of the following can be recognised.", 3, [
    ("Peacock", 1, "Long, colourful tail feathers with eye-like spots; blue neck; it dances when clouds gather."),
    ("Chinkara (Indian gazelle)", 1, "A small, light brown deer with a slim body that runs very fast; the male has curved horns."),
    ("Camel", 1, "Hump on the back, long legs and neck, padded broad feet.")])
q4 = parts("Look at the schematic map of Rajasthan. The dots <b>A, B, C, D</b> show four districts.", 6, [
    ("A is the district where the Keoladeo bird sanctuary is situated. B is called the &lsquo;Blue City&rsquo;. Name A and B.", 2, "A &ndash; Bharatpur &nbsp;&nbsp; B &ndash; Jodhpur"),
    ("In which direction from Jaipur is the dot A? In which direction from Jaipur is the dot D?", 2, "A is to the <b>East</b> of Jaipur; D is to the <b>South-West</b> of Jaipur."),
    ("Name the district C, in which the Ranthambore Tiger Reserve lies.", 1, "Sawai Madhopur"),
    ("Name the district D, which has beautiful lakes such as Pichola and Fateh Sagar.", 1, "Udaipur")],
    fig=svg_locator(T))
q5 = mcq("Which tree is the State tree of Rajasthan?", ["Neem", "Banyan", "Khejri", "Peepal"], 2)
q6 = parts("Cactus grows well in deserts. Answer the following.", 3, [
    ("Why do most cacti have spines instead of broad leaves?", 1, "Spines lose very little water, so the plant saves water in the hot, dry desert."),
    ("Where does a cactus store water?", 1, "In its thick, fleshy stem."),
    ("Why can a cactus live where there is very little rain?", 1, "It stores water in its stem and loses very little of it, so it can survive long dry periods.")])
q7 = Q("", 8, parts=[
    P("(i)", "Write four rules that every family in your colony should follow to keep it clean.", 4,
      "Any four, e.g.: (1) Throw garbage only in the dustbin. (2) Keep wet and dry waste in separate bins. (3) Do not let water collect near houses. (4) Do not spit or litter on roads. (5) Plant and look after trees. [1 each]"),
    P("(ii)", "Look at the picture. Garbage is lying in a heap near the houses and children are playing near it. (a) Write two problems it can cause. (b) Write two things the children can do.", 4,
      "(a) [2] Bad smell; flies and mosquitoes breed and spread diseases; stray animals spread the garbage (any two). "
      "(b) [2] Tell elders / the municipal workers to remove it; stop throwing waste there; start a cleanliness drive and use dustbins (any two).",
      fig=emoji("&#127968; &#128465;&#65039;&#128465;&#65039; &#129712; &#128103; &#128102;"))])
q8 = mcq("Which of these is a <b>pulse</b> (dal) grown in Rajasthan?", ["Bajra", "Moong", "Jowar", "Maize"], 1)
q9 = mcq("Which nutrient is called the body-building food?", ["Carbohydrates", "Proteins", "Fats", "Water"], 1)
q10 = parts("Compare a kuccha house and a pucca house.", 3, [
    ("Write the materials used to build each of them.", 1, "Kuccha house: mud, straw, wood, bamboo. Pucca house: bricks, cement, sand, steel / stone."),
    ("Write one advantage of a pucca house.", 1, "It is strong and lasts long; it is safe in heavy rain and storm."),
    ("Why are houses with thick mud walls comfortable in the desert?", 1, "Thick walls do not let the heat of the day come inside quickly, so the house stays cool.")])
q11 = Q("Your class visits a potter (kumhar) in a village. Write <b>two questions</b> you would ask him about his work.", 3,
        "Any two sensible questions, e.g. (i) [2] What kind of clay do you use and how do you bake the pots? (ii) [1] How many pots can you make in a day?")
q12 = Q("An artisan of Sanganer (Jaipur) is showing the class how cloth is printed with wooden blocks. Write <b>two questions</b> you would ask to learn about this traditional art.", 3,
        "Any two sensible questions, e.g. (i) [2] How did you learn the art and how are the wooden blocks carved? (ii) [1] Which colours do you use and where do they come from?")
q13 = parts("Give reasons.", 3, [
    ("Why do houses in very rainy areas have slanting roofs?", 1, "Rainwater slides down quickly and does not collect on the roof."),
    ("Why do houses in the desert have small windows?", 1, "Small windows keep out the hot wind, dust and strong sunlight."),
    ("Why should every room have a ventilator or window?", 1, "Fresh air comes in and stale air goes out; it also lets in light.")])
q14 = Q("", 6, parts=[
    P("(i)", "Rajasthan has no sea coast. Name any <b>three</b> coastal states of India.", 3, "Any three: Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Odisha, West Bengal. [1 each]"),
    P("(ii)", "Write one work of each person.<br>(a) Amrita Devi &nbsp; (b) Rajendra Singh &nbsp; (c) Sawai Jai Singh II", 3,
      "(a) Gave her life with many villagers of Khejarli to protect khejri trees from being cut. "
      "(b) Revived old johads in the villages of Alwar and helped bring water back (the &lsquo;Waterman of India&rsquo;). "
      "(c) Founded the city of Jaipur and built the Jantar Mantar observatory. [1 each]")])
q15 = Q("", 8, parts=[
    P("(i)", "Read: <i>The main door of Sita&rsquo;s house opens to the East into a hall. The kitchen is on the North side of the hall, and the bedroom is on the South side. The bathroom is behind the bedroom.</i><br>"
      "(a) On which side of the hall is the bedroom? (b) Which room is opposite the kitchen? (c) Sita enters and faces the kitchen. Which direction is she facing? (d) In which direction does the main door open?", 4,
      "(a) South (b) bedroom (c) North (d) East [1 each]"),
    P("(ii)", "Heavy rain damaged the mud house of Ramu&rsquo;s family and water entered it. They built a new pucca house. (a) Why did the rain damage the mud house? (b) Write two features the new house should have to keep water out.", 4,
      "(a) [2] Mud softens and washes away in water, so the walls and roof get weak. "
      "(b) [2] Raised floor (plinth), sloping / strong roof, drains around the house, strong brick-cement walls (any two).")])
q16 = Q("", 6, parts=[
    P("(i)", "Cities are often hotter than villages (the &lsquo;heat island&rsquo; effect). Write any <b>two</b> reasons.", 3,
      "Concrete buildings and tar roads absorb and hold heat; there are fewer trees; vehicles and air conditioners give out heat (any two; 1&frac12; each)."),
    P("(ii)", "Write any <b>three</b> ways to keep a city cooler.", 3, "Plant more trees and gardens; roof gardens; paint roofs white / light; use more public transport; open spaces and ponds (any three).")])
q17 = Q("", 6, parts=[
    P("(i)", "Write any <b>three</b> ways to save electricity at home.", 3, "Switch off lights and fans when not needed; use LED bulbs; open windows for daylight; use solar heaters; unplug devices (any three)."),
    P("(ii)", "Rainwater harvesting from a roof: arrange the steps in order &ndash; <i>water stored in a tank, rain falls on the roof, water passes through a filter, water flows through a pipe.</i>", 3,
      "Rain falls on the roof &rarr; water flows through a pipe &rarr; passes through a filter &rarr; stored in a tank. [3 for the correct order; 1 for each correct step if partly right]")])
q18 = mcq("You want to cross a road where there is no signal. What should you do?", ["Run across quickly", "Stop, look at both sides and then cross", "Close your eyes and walk", "Follow a vehicle closely"], 1)
q19 = parts("On Makar Sankranti people in Rajasthan eat til-gur laddoos and gajak.", 3, [
    ("In which season is this festival celebrated?", 1, "Winter."),
    ("Why are til and gur (jaggery) eaten in winter?", 1, "They give energy and warmth to the body."),
    ("Name one other food people eat in winter in Rajasthan.", 1, "Bajra roti with ghee and gur / gond laddoo / hot khichdi / kadhi (any one).")])
q20 = Q("", 6, parts=[
    P("(i)", "Match the worker with the tool.<br>" + table([["1. Farmer", "(a) saw"], ["2. Carpenter", "(b) needle"], ["3. Tailor", "(c) plough"]], ["Column A", "Column B"]), 3,
      "1 &rarr; (c) &nbsp; 2 &rarr; (a) &nbsp; 3 &rarr; (b)"),
    P("(ii)", "Fill in the blanks. (a) The person who brings letters to our house is called a ______. (b) A PIN code has ______ digits. (c) News of the world comes to us daily through a ______.", 3,
      "(a) postman (b) 6 (six) (c) newspaper [1 each]")])
q21 = mcq("Which of these is the fastest way of sending a written message?", ["Letter", "Email", "Telegram by hand", "Speaking to a neighbour"], 1)
q22 = Q("", 6, parts=[
    P("(i)", "Write one use of each medicinal plant. (a) Tulsi (b) Aloe vera (c) Neem", 3,
      "(a) Relieves cough and cold. (b) Gel is applied on burns and skin. (c) Antiseptic; leaves help in skin infections. [1 each]"),
    P("(ii)", "What will you do if: (a) the lights and fan of an empty classroom are on? (b) your friend throws a wrapper on the road? (c) a child is teased in your class?", 3,
      "(a) Switch them off. (b) Politely tell the friend to use a dustbin / pick it up. (c) Stop others, support the child and tell the teacher. [1 each; any sensible answer]")])

run(2, [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22])
