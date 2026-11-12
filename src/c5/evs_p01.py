from evs_h1 import *

T = ["Udaipur", "Jaisalmer", "Kota", "Alwar"]
assert direction("Jaipur", "Kota")[0] == "South" and direction("Jaipur", "Alwar")[0] == "North-East"

q1 = mcq("Look at the picture. It is related to which of the following?", ["fishing", "farming", "weaving", "mining"], 1,
         fig=emoji("&#129489;&#8205;&#127806; &#127806;&#127806;&#127806; &#128002; &#128668; &#9728;&#65039;"))
q2 = mcq("On which festival do people of Rajasthan fly kites in large numbers?",
         ["Teej", "Makar Sankranti", "Gangaur", "Pushkar fair"], 1)
q3 = parts("Write <b>one use</b> of each of the following trees.", 3, [
    ("Neem", 1, "Its leaves and twigs are used as medicine / its twig is used as a datun to clean teeth; it gives shade."),
    ("Khejri", 1, "Its pods (sangri) are eaten as a vegetable; its leaves (loong) are fodder for goats and camels; it gives shade in the desert."),
    ("Mango", 1, "It gives tasty fruit (raw mango is used for pickle and chutney); its wood is used for furniture.")])
q4 = parts("Look at the schematic map of Rajasthan. The dots <b>A, B, C, D</b> show four districts.", 6, [
    ("Name the district shown by A (the City of Lakes) and by B (the Golden City, famous for its sand dunes and a yellow sandstone fort).", 2, "A &ndash; Udaipur &nbsp;&nbsp; B &ndash; Jaisalmer"),
    ("In which direction from Jaipur is the dot C? In which direction from Jaipur is the dot D?", 2, "C is to the <b>South</b> of Jaipur; D is to the <b>North-East</b> of Jaipur."),
    ("Name the district C, which is on the bank of the river Chambal and is famous as a coaching centre.", 1, "Kota"),
    ("Name the district D, in which the Sariska Tiger Reserve is situated.", 1, "Alwar")],
    fig=svg_locator(T))
q5 = mcq("Which bird is the State bird of Rajasthan?", ["Peacock", "Godawan (Great Indian Bustard)", "Sparrow", "Kingfisher"], 1)
q6 = parts("The camel is called the &lsquo;ship of the desert&rsquo;. Answer the following.", 3, [
    ("Why can a camel walk easily on hot, soft sand?", 1, "Its feet are broad and padded, so it does not sink in the sand."),
    ("Which part of its body stores fat so that it can live for many days without food?", 1, "The hump."),
    ("Why does a camel have long eyelashes?", 1, "They protect its eyes from sand and dust during sandstorms.")])
q7 = Q("", 8, parts=[
    P("(i)", "Your school is celebrating <b>&lsquo;Save Water Week&rsquo;</b>. Write four slogans or rules for the notice board.", 4,
      "Any four, e.g.: (1) Save water, save life. (2) Close the tap when you brush your teeth. (3) Report a leaking tap at once. (4) Reuse the water after washing vegetables for plants. (5) Do not waste even a drop. [1 mark each]"),
    P("(ii)", "Read the situation. In the school playground a tap is leaking and water flows into the drain the whole day. Rani sees it while going home.<br>"
      "(a) Why is it wrong to let the water run away like this? (b) What should Rani do?", 4,
      "(a) [2] Water is precious and limited; wasting it means less water for drinking and for the people and animals who need it, especially in dry Rajasthan. "
      "(b) [2] She should tell the teacher or the watchman immediately so that the tap is repaired, and tell her friends not to waste water.",
      fig=emoji("&#127979; &#128703; &#128167;&#128167; &#128103; &#128064;"))])
q8 = mcq("Which of these crops is a <b>rabi</b> crop?", ["Bajra", "Wheat", "Maize", "Rice"], 1)
q9 = mcq("Rajasthan is the largest producer in India of which of these crops?", ["Rice", "Bajra", "Sugarcane", "Tea"], 1)
q10 = parts("Kharif and rabi are two cropping seasons of farmers.", 3, [
    ("When are kharif crops sown (at the start of which season)?", 1, "In the rainy season (June&ndash;July), with the first monsoon rains."),
    ("When are rabi crops sown?", 1, "In the winter season (October&ndash;November)."),
    ("Name one kharif and one rabi crop.", 1, "Kharif: bajra / maize / moong / rice. Rabi: wheat / mustard / gram (barley).")])
q11 = Q("Your class visits a farm in a village near Jaipur and meets a farmer who grows bajra. Write <b>two questions</b> that you would like to ask the farmer.", 3,
        "Any two sensible questions, e.g. (i) [2] How much water does bajra need and how do you irrigate your field? (ii) [1] In which month do you sow and harvest the crop? "
        "(Award 2 marks to the more thoughtful question and 1 to the other.)")
q12 = Q("A group of Langa and Manganiyar folk singers is visiting your school. Write <b>two questions</b> you would like to ask them about the rich culture of Rajasthan.", 3,
        "Any two sensible questions, e.g. (i) [2] Which instruments do you play and how did you learn this music from your elders? (ii) [1] On which occasions do you sing these songs?")
q13 = parts("Give reasons.", 3, [
    ("Why were tankas, johads and baoris built in Rajasthan?", 1, "Rajasthan gets little rain, so rainwater was collected and stored in them to be used in the dry months."),
    ("Why should we drink boiled or filtered water?", 1, "It kills / removes the germs that cause diseases such as typhoid and diarrhoea."),
    ("Why should we not waste water?", 1, "Fresh water is limited; if we waste it, there will be less for the future and for others.")])
q14 = Q("", 6, parts=[
    P("(i)", "Name any <b>three</b> states which share their border with Rajasthan.", 3, "Any three: Punjab, Haryana, Uttar Pradesh, Madhya Pradesh, Gujarat. [1 each]"),
    P("(ii)", "Write one famous work or deed of each person.<br>(a) Maharana Pratap &nbsp; (b) Panna Dhai &nbsp; (c) Maharshi Dayanand Saraswati", 3,
      "(a) Fought the Mughal army bravely in the Battle of Haldighati (1576) and never bowed down. "
      "(b) Sacrificed her own son to save the life of the young prince Udai Singh. "
      "(c) Founded the Arya Samaj (spread education, opposed superstition; wrote Satyarth Prakash). [1 each]")])
q15 = Q("", 8, parts=[
    P("(i)", "Look at these four words: <b>tanka, river, johad, rain</b>. Write which two are <i>sources</i> of water and which two are <i>structures used to store water</i>.", 4,
      "Sources of water: river, rain [2]. Structures to store water: tanka, johad [2]."),
    P("(ii)", "The women of a village walked 3 km every day to get water. The villagers built a johad near the village.<br>(a) How does a johad get filled with water? (b) Write two benefits of it for the village.", 4,
      "(a) [2] It is a small earthen dam/pond that collects the rainwater flowing during the monsoon; the water also seeps into the ground. "
      "(b) [2] Water is available near the village for animals and fields; the underground water level and wells are recharged; women save time / any two.")])
q16 = Q("", 6, parts=[
    P("(i)", "Write whether each object will <b>float</b> or <b>sink</b> in water: (a) iron nail (b) wooden spoon (c) empty, closed plastic bottle", 3,
      "(a) sinks (b) floats (c) floats [1 each]"),
    P("(ii)", "Write whether each substance <b>dissolves</b> or <b>does not dissolve</b> in water: (a) sugar (b) sand (c) salt", 3,
      "(a) dissolves (b) does not dissolve (c) dissolves [1 each]")])
q17 = Q("", 6, parts=[
    P("(i)", "A tap drips and wastes 5 litres of water every hour. How many litres of water will it waste in one day (24 hours)? How many litres in 7 days?", 3,
      "In one day: 5 &times; 24 = <b>120 litres</b> [1&frac12;]. In 7 days: 120 &times; 7 = <b>840 litres</b> [1&frac12;]."),
    P("(ii)", "The temperature of the earth is slowly rising (climate change). Write any <b>three</b> effects of it.", 3,
      "Any three: glaciers and ice melt; sea level rises; floods in some places and droughts in others; very hot summers; harm to plants and animals. [1 each]")])
q18 = mcq("A road sign in the shape of a triangle with a red border (for example, &lsquo;School ahead&rsquo;) is a/an ______ sign.",
          ["mandatory", "cautionary (warning)", "informatory", "decorative"], 1)
q19 = parts("On Sheetla Saptami, many families in Rajasthan eat cold food (cooked the day before). The festival comes after Holi, when summer begins.", 3, [
    ("Name the season that begins around this time.", 1, "Summer."),
    ("Name one kind of food that gets spoiled quickly in hot weather.", 1, "Cooked rice / milk / curd / cut fruits / vegetables (any one)."),
    ("Write one way to keep food safe in summer.", 1, "Keep it covered, store it in a fridge or in an earthen pot (matka), eat fresh food, wash hands before eating (any one).")])
q20 = Q("", 6, parts=[
    P("(i)", "Match the following.<br>" + table([["1. Helmet", "(a) is used by people to cross the road safely"], ["2. Seat belt", "(b) protects the head of a two-wheeler rider"], ["3. Zebra crossing", "(c) protects the passenger of a car"]], ["Column A", "Column B"]), 3,
      "1 &rarr; (b) &nbsp; 2 &rarr; (c) &nbsp; 3 &rarr; (a)"),
    P("(ii)", "Fill in the blanks. (a) The ambulance can be called on the number ______. (b) A train runs on ______. (c) An aeroplane travels through the ______.", 3,
      "(a) 108 (b) rails / tracks (c) air [1 each]")])
q21 = mcq("Which of these is a means of <b>mass communication</b>?", ["Letter", "Television", "Postcard", "Greeting card"], 1)
q22 = Q("", 6, parts=[
    P("(i)", "Answer in one line each. (a) Who is the head of the Gram Panchayat? (b) Who keeps the records of farm land in a village? (c) Which health worker visits houses in a village to help mothers and children?", 3,
      "(a) Sarpanch (b) Patwari (c) ANM / ASHA (Anganwadi) worker [1 each]"),
    P("(ii)", "What will you do if: (a) you find a lost small child in a market? (b) a classmate who uses a wheelchair cannot enter the library? (c) you see a stray dog with an injured leg?", 3,
      "(a) Stay with the child, ask nearby elders/police for help and try to find the parents. (b) Ask the teacher to make a ramp and help the classmate to enter. (c) Tell an elder / animal helpline to get the dog treated; do not tease or hurt it. [1 each; any sensible answer]")])

run(1, [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22])
