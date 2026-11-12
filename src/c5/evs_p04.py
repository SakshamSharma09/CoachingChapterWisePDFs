from evs_h1 import *

T = ["Banswara", "Sri Ganganagar", "Bundi", "Dholpur"]
assert direction("Jaipur", "Bundi")[0] == "South" and direction("Jaipur", "Dholpur")[0] == "East"

q1 = mcq("Look at the picture. It is related to which festival?", ["Holi", "Diwali", "Raksha Bandhan", "Makar Sankranti"], 1,
         fig=emoji("&#129684; &#127878; &#127879; &#127856; &#127968;"))
q2 = mcq("The festival of Teej is celebrated in which season?", ["Summer", "Rainy season (monsoon)", "Winter", "Spring only"], 1)
q3 = parts("Write what each of these places or things of Rajasthan is famous for.", 3, [
    ("Sanganer (Jaipur)", 1, "Hand-block printing on cloth (also handmade paper)."),
    ("Bikaner", 1, "Bikaneri bhujia and papad; the Camel Festival; Junagarh Fort."),
    ("Kota", 1, "Kota Doria sarees (also the Chambal gardens, coaching centres).")])
q4 = parts("Look at the schematic map of Rajasthan. The dots <b>A, B, C, D</b> show four districts.", 6, [
    ("A is known as the &lsquo;City of Hundred Islands&rsquo; on the Mahi river. B is the northernmost district, where the Indira Gandhi Canal brings water to the fields. Name A and B.", 2, "A &ndash; Banswara &nbsp;&nbsp; B &ndash; Sri Ganganagar"),
    ("In which direction from Jaipur is the dot C? In which direction from Jaipur is the dot D?", 2, "C is to the <b>South</b> of Jaipur; D is to the <b>East</b> of Jaipur."),
    ("Name the district C, which is famous for its many beautiful stepwells (baoris), such as Raniji ki Baori.", 1, "Bundi"),
    ("Name the district D, whose red-pink sandstone is used in many buildings.", 1, "Dholpur")],
    fig=svg_locator(T))
q5 = mcq("Which of these animals is a <b>carnivore</b> (eats only flesh)?", ["Camel", "Tiger", "Goat", "Chinkara"], 1)
q6 = parts("Plants make their own food. Answer the following.", 3, [
    ("What is the process of making food by green plants called?", 1, "Photosynthesis."),
    ("Which gas do plants give out during this process?", 1, "Oxygen."),
    ("Which part of the plant absorbs water from the soil?", 1, "Roots.")])
q7 = Q("", 8, parts=[
    P("(i)", "On Van Mahotsav your school will plant saplings. Write four slogans or rules for the plantation drive.", 4,
      "Any four, e.g.: (1) Plant a tree, save the earth. (2) One child, one tree. (3) Water the sapling regularly. (4) Never pluck leaves or break branches. (5) Trees give us air, shade and fruits. [1 each]"),
    P("(ii)", "Look at the picture. Workers have come to cut many trees for widening a road. Meena, a girl of Class 5, sees them. (a) Write two harms of cutting the trees. (b) What can Meena do?", 4,
      "(a) [2] Less shade and oxygen; birds lose homes; soil erodes; more heat and pollution (any two). "
      "(b) [2] Tell elders / the forest department; ask for new trees to be planted in place of those cut; gather friends to spread awareness.",
      fig=emoji("&#129683; &#127795;&#127795; &#128119; &#128103;"))])
q8 = mcq("Ghewar, a sweet popular in the season of Teej, is made mainly from flour, ghee and", ["sugar syrup", "tomato puree", "salt water", "lemon juice"], 0)
q9 = mcq("Which of these crops gives us <b>fibre</b> for making cloth?", ["Wheat", "Cotton", "Gram", "Mustard"], 1)
q10 = parts("Compare life in a village and in a city.", 3, [
    ("Write the main occupation of most people in a village.", 1, "Farming and animal rearing (also crafts)."),
    ("Name one occupation which is more common in cities.", 1, "Office jobs / factory work / shop-keeping / banking / driving (any one)."),
    ("Which has cleaner air &ndash; a village or a city? Give one reason.", 1, "Village &ndash; there are fewer vehicles and factories, and more trees.")])
q11 = Q("The grandson of a freedom fighter has come to your school. Write <b>two questions</b> you would like to ask him.", 3,
        "Any two sensible questions, e.g. (i) [2] What difficulties did your grandfather face while fighting for freedom? (ii) [1] How did people celebrate on 15 August 1947?")
q12 = Q("A Kalbeliya dancer of Rajasthan has come to perform in your school. Write <b>two questions</b> you would ask her about her art and culture.", 3,
        "Any two sensible questions, e.g. (i) [2] How did you learn this dance and which songs do you dance to? (ii) [1] Why do you wear such colourful costumes?")
q13 = parts("Give reasons.", 3, [
    ("Why is the khejri tree called the lifeline of the desert?", 1, "It gives shade, fodder for animals, sangri for food and wood, and grows with very little water."),
    ("Why should old forts and monuments be protected?", 1, "They show our history and culture and they belong to all of us and to the future generations."),
    ("Why should we not write or scratch our names on the walls of forts?", 1, "It spoils the monument and its beauty; it is damage to our heritage.")])
q14 = Q("", 6, parts=[
    P("(i)", "Name any <b>three</b> famous forts of Rajasthan.", 3, "Any three: Amer, Chittorgarh, Kumbhalgarh, Mehrangarh (Jodhpur), Jaisalmer, Ranthambore, Junagarh (Bikaner), Nahargarh. [1 each]"),
    P("(ii)", "Write one fact about each.<br>(a) Bhamashah &nbsp; (b) Guru Jambheshwar &nbsp; (c) Rao Jodha", 3,
      "(a) Gave his wealth to help Maharana Pratap continue the struggle. (b) Founded the Bishnoi community and asked people to protect trees and animals. "
      "(c) Founded the city of Jodhpur and built the Mehrangarh Fort. [1 each]")])
q15 = Q("", 8, parts=[
    P("(i)", "Group these four into <b>natural</b> and <b>built (man-made)</b> heritage: <b>Hawa Mahal, Ranthambore forest, Chittorgarh Fort, Chambal river</b>.", 4,
      "Natural: Ranthambore forest, Chambal river [2]. Built (man-made): Hawa Mahal, Chittorgarh Fort [2]."),
    P("(ii)", "Grandmother says, &ldquo;When I was small, we went to the fair on camel carts and sent letters to relatives.&rdquo; (a) Write two ways in which travel has changed since then. (b) Write two ways in which keeping in touch with relatives has changed.", 4,
      "(a) [2] Now we have buses, cars, trains, metro and aeroplanes, which are faster. (b) [2] Now we use mobile phones, video calls, email and messages, so news reaches in seconds.")])
q16 = Q("", 6, parts=[
    P("(i)", "Eating fried junk food daily and watching TV for hours can harm us. Write any <b>three</b> ill effects.", 3,
      "Becoming overweight; weak eyes; stomach trouble; less energy / tiredness; poor sleep; tooth decay (any three)."),
    P("(ii)", "Give a reason. (a) Why do we wear light cotton clothes in summer? (b) Why do we wear woollen clothes in winter? (c) Why do people of the desert tie a cloth around the head?", 3,
      "(a) Cotton absorbs sweat and keeps the body cool. (b) Wool traps air and keeps the body heat in. (c) It protects from the hot sun, dust and loo (hot wind). [1 each]")])
q17 = Q("", 6, parts=[
    P("(i)", "Write two reasons why forests are disappearing and one way to save them.", 3,
      "Cutting of trees for houses, roads and farms; forest fires; mining (any two causes &ndash; 2 marks). Way to save: plant more trees / make laws against cutting / use less paper (1 mark)."),
    P("(ii)", "Write any <b>three</b> fire-safety rules for a house.", 3,
      "Do not play with matches or crackers indoors; switch off the gas / switches when not in use; keep a bucket of sand or fire extinguisher ready; call 101; keep exits clear (any three).")])
q18 = mcq("A blue, circular road sign with a white arrow shows a ______ sign.", ["cautionary", "mandatory (tells what we must do)", "informatory", "advertisement"], 1)
q19 = parts("Summer in Rajasthan is very hot, and hot winds called <i>loo</i> blow in the afternoon.", 3, [
    ("Why should we drink plenty of water and buttermilk in summer?", 1, "We lose water through sweat; buttermilk and water replace it and keep the body cool."),
    ("Why should we avoid going out in the afternoon without a cap or cloth on the head?", 1, "To avoid the heat stroke caused by the loo and strong sun."),
    ("Name one seasonal fruit or drink of summer.", 1, "Mango, watermelon, muskmelon, aam panna, lemon water, chhach (any one).")])
q20 = Q("", 6, parts=[
    P("(i)", "Match the following.<br>" + table([["1. Bicycle", "(a) travels in the air"], ["2. Aeroplane", "(b) travels on rails below or above the city roads"], ["3. Metro", "(c) needs no fuel"]], ["Column A", "Column B"]), 3,
      "1 &rarr; (c) &nbsp; 2 &rarr; (a) &nbsp; 3 &rarr; (b)"),
    P("(ii)", "Fill in the blanks. (a) A letter is dropped in a red ______ box. (b) The address and PIN code are written on the ______. (c) A message sent through a mobile phone is called an ______.", 3,
      "(a) letter (post) (b) envelope / postcard (c) SMS / text message [1 each]")])
q21 = mcq("Which organisation broadcasts radio programmes all over India?", ["Indian Railways", "All India Radio (Akashvani)", "Reserve Bank", "Election Commission"], 1)
q22 = Q("", 6, parts=[
    P("(i)", "Write the level at which each body works. (a) Gram Panchayat (b) Zila Parishad (c) Municipal Corporation", 3,
      "(a) village (b) district (c) city [1 each]"),
    P("(ii)", "What will you do if: (a) you see a water tap left open on the road? (b) a new student has no friends in your class? (c) you smell gas in the kitchen?", 3,
      "(a) Close it, or tell an elder. (b) Talk to the student, include him / her in games. (c) Do not switch on any switch or light; open the windows, close the regulator and tell elders. [1 each]")])

run(4, [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22])
