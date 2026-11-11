from h8 import *
import figs6s as G
# ---------- Science Set 2 : emphasis Measurement, States of Water, Diversity, Magnets, Materials ----------
A = [
 mc("Sunita thinks, \"Plants kept in sunlight grow taller than plants kept in the dark.\" In the scientific method this statement is a:", "hypothesis", ["conclusion", "result", "measurement"], "A testable guess made before the experiment is a hypothesis."),
 mc("Which of the following animal–habitat pairs is correctly matched?", "Camel – desert", ["Polar bear – desert", "Fish – forest floor", "Penguin – grassland"], "A camel lives in hot deserts; polar bears live in cold polar regions; penguins in Antarctica."),
 mc("Which of the following foods is the best source of dietary fibre (roughage)?", "Vegetables and whole-wheat chapati", ["Butter and ghee", "Sugar and jaggery", "Fried samosa"], "Whole grains and vegetables contain plant fibre that helps digestion."),
 mc("Two bar magnets P and Q are placed as shown. They will:", "repel each other", ["attract each other", "not affect each other", "lose their magnetism"], "The facing ends are both North poles, and like poles repel.", fig=G.bar_magnets(('S', 'N'), ('N', 'S'))),
 mc("The most suitable unit for expressing the thickness of a coin is the:", "millimetre", ["kilometre", "metre", "hour"], "A coin is only a few millimetres thick; km and m are too big."),
 mc("Salt disappears when stirred in water but sand does not. This shows that salt is:", "soluble in water", ["transparent", "lustrous", "magnetic"], "Salt dissolves (soluble); sand does not dissolve (insoluble)."),
 mc("A steel spoon is left in a cup of hot tea. After some time the handle becomes warm. Heat reaches the handle by:", "conduction", ["evaporation", "condensation", "melting"], "In solids, heat travels from the hot part to the colder part by conduction."),
 mc("Drops of water appear on the outside of a glass filled with ice-cold water. This happens because:", "water vapour in air condenses on the cold glass", ["water leaks through the glass", "ice melts and passes through the glass", "the glass sweats like skin"], "Water vapour in the air cools on touching the cold surface and turns into liquid."),
 mc("Muddy pond water is left undisturbed. The mud settles down and the clear water is then poured into another vessel. The two methods used are:", "sedimentation and decantation", ["winnowing and sieving", "evaporation and churning", "magnetic separation and filtration"], "Settling of heavy particles is sedimentation; pouring off clear liquid is decantation."),
 mc("Which of the following shows 'response to stimulus'?", "A touch-me-not plant folds its leaves when touched", ["A pebble rolls down a slope", "Ice melts in sunlight", "A cloud floats in the sky"], "Only living things respond to a stimulus such as touch."),
 mc("Which of the following activities helps in conserving soil on a hill slope?", "Planting trees and terrace farming", ["Cutting trees for fuel", "Burning dry leaves", "Digging up the slope"], "Roots and terraces hold the soil and stop it from being washed away."),
 mc("The star nearest to the Earth is the:", "Sun", ["Pole Star", "Sirius", "Moon"], "The Sun is a star and is by far the nearest one to us."),
]
B = [
 sa("List two habits that a good scientist should have.", 2, "Any two (1 each): curiosity/asking questions, careful observation, honesty in recording, repeating experiments, patience, open-mindedness, working in a team."),
 OR(sa("Name two uses of magnets in daily life.", 2, "Any two: fridge door seals, magnetic toys, compass, pencil-box clasps, speakers, cranes in scrapyards (1 each)."),
    sa("How can you find the poles of an unmarked bar magnet using another bar magnet whose N pole is marked?", 2, "Bring the marked N pole near one end of the unmarked magnet (1). If the end is repelled it is also N; if attracted it is S (1).")),
 sa("Give two examples each of materials that are (i) soluble in water and (ii) insoluble in water.", 2, "(i) Salt, sugar (ii) sand, chalk powder, oil/wood (any two each; 1 mark per part)"),
 sa("Name the centre of our solar system and write the names of any two planets, one nearer and one farther from it.", 2, "Sun (1). Example: Mercury/Venus/Earth (near) and Saturn/Uranus/Neptune (far) (1)."),
]
C = [
 sa("Dev eats only rice, potatoes and sugary sweets every day. (i) Which nutrient does he get mostly? (ii) Name one nutrient he is missing. (iii) Suggest two foods to add.", 3, "(i) Carbohydrates (1) (ii) Proteins (or vitamins/minerals/fibre) (1) (iii) Dal/milk/eggs/vegetables/fruits (two foods; 1)"),
 sa("Write the steps for measuring the temperature of hot water with a laboratory thermometer.", 3, "Any three (1 each): hold thermometer upright; place its bulb in the water without touching the bottom/sides; wait until the mercury stops rising; read with eye in line with the level; do not hold by the bulb."),
 sa("Name three natural resources. Why should we use them wisely? Write one way of doing so.", 3, "Air, water, soil, forests, minerals, sunlight (any three; 1). They are limited and needed by all living things now and in future (1). Reduce, reuse, recycle/ save water/ plant trees (1)."),
]
D = [
 OR(sa("Describe how you can measure the length of a curved line (such as a road on a map) with the help of a thread and a ruler.", 5, "Take a thread (1); place it carefully along the curved line, marking its start (1); mark the point where the curve ends (1); straighten the thread without stretching and place it along the ruler (1); read the length between the two marks and write it with a unit (1)."),
    sa("Convert (i) 4 m into cm (ii) 250 cm into m (iii) 3.2 km into m (iv) 7 cm into mm (v) 4500 m into km.", 5, "(i) 400 cm (ii) 2.5 m (iii) 3200 m (iv) 70 mm (v) 4.5 km (1 mark each)")),
 OR(sa("Draw or describe the water cycle and name its main stages.", 5, "Sun heats oceans, rivers and lakes (1); evaporation: water becomes vapour (1); vapour rises and cools, condensation forms clouds (1); precipitation as rain/snow/hail (1); water flows back to rivers and seas / seeps underground (1)."),
    sa("Explain any five factors or conditions that make evaporation of water faster, giving a daily-life example for each of two.", 5, "Any five (1 each): higher temperature, more surface area, wind/moving air, low humidity, sunshine. Two examples e.g. clothes dry faster in the sun, spread-out clothes dry faster than folded clothes.")),
 fill(["habitat", "adaptation", "herb", "tree", "shrub"],
      ["The place where a plant or animal lives is its ________.", "A feature that helps a living thing survive in its surroundings is an ________.", "A small plant with a soft green stem, like coriander, is a ________.", "A plant with a hard woody trunk and many branches high above the ground is a ________.", "A plant with many woody stems growing from the base, like hibiscus, is a ________."],
      ["habitat", "adaptation", "herb", "tree", "shrub"]),
]
E = [
 c4("Rohit has two bar magnets, P and Q. He also has an iron nail, a plastic scale and a steel needle. When he brings the magnet near these things, the nail and needle stick to it but the plastic scale does not. He then hangs magnet P freely with a thread and finds that one end always points towards the North.",
    ("Name two magnetic materials from the above case.", "Iron (nail) and steel (needle)."),
    ("Which pole of the freely hanging magnet points towards the North?", "The North-seeking (N) pole."),
    ("What will happen if Rohit brings the S pole of magnet Q near the S pole of magnet P? Give a reason.", "They repel each other because like poles repel."),
    ("Why is a magnetic compass useful for a traveller?", "A compass needle is a small magnet that points north–south, so it shows directions anywhere."),
    fig=G.bar_magnets(('S', 'N'), ('N', 'S'))),
 c4("In Grandmother's kitchen, many separations take place. Rice is checked for tiny stones, tea is poured through a strainer, and cream is separated from curd by churning it into butter.",
    ("Which method is used to remove stones from rice?", "Hand-picking."),
    ("Name the device used to separate tea leaves from tea.", "Strainer (sieve) — sieving/filtration."),
    ("What happens when curd is churned? Name the method.", "Butter separates from buttermilk; the lighter butter floats (churning)."),
    ("Name the method you would use to separate salt from sea-water and explain in one line.", "Evaporation — heating/leaving in the Sun makes water vapour go away and salt remains.")),
 c4("In the Thar desert, a cactus has thick, fleshy stems that store water, its leaves are tiny spines, and its roots spread wide near the surface. A camel has long eyelashes, wide padded feet and a hump of fat.",
    ("What is the habitat described here?", "Desert."),
    ("Name the part of a cactus that stores water.", "The thick fleshy stem."),
    ("How do the spines help the cactus?", "Spines reduce water loss through leaves and protect it from animals."),
    ("Explain how wide padded feet help a camel.", "They spread its weight and prevent sinking in loose sand.")),
 c4("In a school mid-day meal in Jaipur, the cook prepares dal, roti, mixed vegetables, rice and a bowl of curd. A banana is given as dessert on Fridays. The teacher says it is a balanced meal.",
    ("Name one food from the meal that is rich in proteins.", "Dal / curd."),
    ("Which food in the meal gives mainly carbohydrates?", "Roti / rice."),
    ("What is a balanced diet?", "A diet containing all nutrients (carbohydrates, proteins, fats, vitamins, minerals, fibre and water) in the right amounts."),
    ("Why is eating too many fried and packaged snacks not good for children?", "They are high in fat, sugar and salt but low in useful nutrients, leading to obesity and poor health.")),
]
make(2, 'Full Syllabus · Chapters 1–12', A, B, C, D, E, 'Set_02')
