from h8 import *
import figs6s as G
# ---------- Science Set 3 : emphasis Materials, Beyond Earth, Mindful Eating, Living Creatures, Separation ----------
A = [
 mc("Which of the following is NOT a good practice for a scientist?", "Accepting the result of a single trial without repeating the experiment", ["Recording observations honestly", "Repeating the experiment to check the result", "Changing only one variable at a time"], "Reliable results need repeated trials."),
 mc("Which of the following groups contains only trees?", "Neem, banyan, mango", ["Tulsi, mint, coriander", "Rose, hibiscus, jasmine", "Money plant, pumpkin, grape vine"], "Neem, banyan and mango are tall, woody plants with a thick trunk."),
 mc("Chips and other fried packaged snacks are called junk food mainly because they are:", "high in fat, salt and sugar but low in useful nutrients", ["full of proteins and vitamins", "rich in roughage", "made only of water"], "Junk foods give energy but few nutrients and can harm health when eaten often."),
 mc("Which of the following will NOT be attracted by a magnet?", "An aluminium foil", ["An iron nail", "A steel pin", "An iron key"], "Aluminium is a non-magnetic material."),
 mc("Which of these is a standard unit of length?", "Centimetre", ["Handspan", "Cubit", "Footstep"], "Handspan, cubit and footstep differ from person to person; the centimetre is fixed."),
 mc("Which of the following will float on water?", "A wooden cork", ["An iron nail", "A stone", "A steel spoon"], "A cork is lighter for its size than water, so it floats."),
 mc("The laboratory thermometer in the figure shows the temperature of water. If the water cools by 15 °C, the new reading will be:", "25 °C", ["55 °C", "15 °C", "40 °C"], "The thermometer reads 40 °C; 40 − 15 = 25 °C.", fig=G.thermo(40)),
 mc("Water changing into ice in a freezer is called:", "freezing", ["melting", "evaporation", "condensation"], "Liquid to solid is freezing."),
 mc("Cream is obtained from milk by churning. This method works because:", "the lighter fat separates out from the liquid when the milk is rotated rapidly", ["fat dissolves in water", "milk evaporates", "milk is a pure substance"], "Churning separates lighter butter/cream from the rest."),
 mc("A cow gives birth to a calf. This is an example of which characteristic of living things?", "Reproduction", ["Growth", "Movement", "Excretion"], "Producing young ones of the same kind is reproduction."),
 mc("Which of the following habits helps in saving water at home?", "Fixing leaking taps promptly", ["Leaving the tap running while brushing", "Washing a car daily with a hosepipe", "Throwing waste into ponds"], "A dripping tap wastes several litres a day."),
 mc("Day and night occur on the Earth because the Earth:", "rotates on its axis", ["revolves around the Moon", "moves away from the Sun", "stops for some hours"], "As the Earth spins, one side faces the Sun (day) while the other is dark (night)."),
]
B = [
 sa("Write two differences between a herb and a tree.", 2, "Herb: small, soft green stem, short-lived. Tree: tall, thick woody trunk, long-lived (1 mark per correct pair of points; two differences)."),
 sa("Why does a clinical thermometer have a kink near its bulb?", 2, "The kink prevents the mercury from sliding back on its own (1) so the reading can be noted after removing it from the mouth/armpit (1)."),
 OR(sa("Name the method used to separate (i) wheat grains from stones (ii) a mixture of oil and water in a separating funnel.", 2, "(i) Hand-picking (or sieving) (1) (ii) Decantation / separating funnel (1)"),
    sa("Why do we use a sieve while grinding grains at home? Name the method.", 2, "Fine flour passes through the holes while bigger pieces remain (1); the method is sieving (1).")),
 sa("Why should we not waste natural resources such as water? Give two reasons.", 2, "They are limited (1); they are needed by all living things and for future generations (1)."),
]
C = [
 sa("Arun wants to know if a plant grows better with fertiliser. Write (i) a question (ii) a hypothesis (iii) one thing he must keep the same for both plants.", 3, "(i) Does fertiliser make a plant grow taller? (1) (ii) A plant given fertiliser will grow taller (1) (iii) Same amount of water/sunlight/soil/pot size (1)"),
 sa("A student measures the length of a pencil as 14 cm and the width of a book as 0.21 m. (i) Convert the width of the book into cm. (ii) Which is longer? (iii) By how much?", 3, "(i) 0.21 × 100 = 21 cm (1) (ii) The book's width (1) (iii) 21 − 14 = 7 cm (1)"),
 sa("Write any three differences between living and non-living things, with an example for each.", 3, "Any three (1 each): living things grow, respire, need food, respond to stimuli, reproduce (e.g. a dog, a tree); non-living things (e.g. a stone, a table) do not do these things."),
]
D = [
 OR(sa("Classify the following into transparent, translucent and opaque: clear glass, butter paper, wooden door, plain water, oiled paper.", 5, "Transparent: clear glass, plain water (2); translucent: butter paper, oiled paper (2); opaque: wooden door (1)."),
    sa("Give reasons: (i) Utensils for cooking are made of metals such as steel. (ii) Window panes are made of glass. (iii) The handle of a frying pan is made of plastic or wood. (iv) Raincoats are made of plastic. (v) Mirrors are coated with a shiny metal.", 5, "(i) Metals are hard and good conductors of heat (1) (ii) Glass is transparent (1) (iii) Plastic/wood is a poor conductor so the hand does not burn (1) (iv) Plastic does not allow water to pass (1) (v) Shiny (lustrous) metals reflect light (1)")),
 OR(sa("List the eight planets of the solar system in the order of their distance from the Sun. Name the planet (i) with rings (ii) known as the 'Red planet'.", 5, "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune (3 marks); (i) Saturn (1) (ii) Mars (1)"),
    sa("Explain why the Moon seems to change shape every night. Name the full-moon day and the new-moon day.", 5, "The Moon does not shine itself; it reflects sunlight (1). It revolves around the Earth in about a month (1). Different amounts of its lit half are visible from Earth, giving phases (2). Full-moon day: Poornima; new-moon day: Amavasya (1).")),
 match(["Carbohydrates", "Proteins", "Fats", "Vitamins and minerals", "Roughage"], ["Help in digestion and prevent constipation", "Give the most energy per gram", "Help in growth and repair", "Protect the body and keep it healthy", "Give quick energy"], ["a–v", "b–iii", "c–ii", "d–iv", "e–i"], "Match the nutrient in Column I with its use in Column II."),
]
E = [
 c4("In an experiment, Sneha placed some ice cubes in a steel plate and kept it in the sun. After some time the ice changed into water. She then left the plate in the sun for the whole afternoon, and the water disappeared.",
    ("What is the change of ice into water called?", "Melting."),
    ("Name the process by which the water in the plate disappeared.", "Evaporation."),
    ("If she puts the water in a refrigerator's freezer, what will happen? Name the process.", "It will turn back into ice; freezing."),
    ("Will the water evaporate faster if she spreads it on a wide tray? Why?", "Yes. A larger surface area exposes more water to air and speeds up evaporation.")),
 c4("Rani went to the market with her mother. They bought fresh green vegetables, fruits, pulses, milk and rice for the week. Rani's mother said, \"Local, seasonal and fresh food is cheap and healthy; packaged chips and cold drinks harm our body.\"",
    ("Name the food group to which pulses mainly belong.", "Proteins."),
    ("Name a vitamin and a mineral that fruits and vegetables supply.", "Vitamin C/A and iron/potassium/calcium (any one each, 1 mark for both)."),
    ("Why is it better to eat seasonal and local food?", "It is fresher, has more nutrients, costs less and saves transport energy/pollution."),
    ("Suggest two healthy eating habits for a child.", "Eat a balanced diet; wash hands/fruits before eating; eat slowly; avoid wasting food; limit junk food; drink enough water (any two).")),
 c4("Maya's grandfather uses a small magnet attached to a string to pick up pins that fall on the floor of his tailoring shop. Maya noticed that the magnet attracts iron pins from a little distance, but not brass buttons or plastic buttons.",
    ("Which material in the story is attracted by the magnet?", "Iron (steel) pins."),
    ("Is magnetic force a contact force or a force that acts from a distance?", "It acts from a distance (non-contact)."),
    ("Why is the magnet unable to pick up brass buttons?", "Brass is a non-magnetic material."),
    ("How can Maya prove that the magnet has two poles?", "Dip the magnet in iron filings: they cluster at two ends (poles) and fewer in the middle; or hang it freely and see it point N–S.")),
 c4("A group of students noted the lengths of five leaves with a ruler: 6.5 cm, 7.0 cm, 5.5 cm, 8.0 cm and 7.5 cm. Their teacher advised them to hold the ruler so that the zero mark is exactly at one end of the leaf and to read the scale with the eye directly above the mark.",
    ("Name the longest of the five leaves.", "The leaf of length 8.0 cm."),
    ("What is the difference in length between the longest and shortest leaves?", "8.0 − 5.5 = 2.5 cm."),
    ("Name the error that occurs if the scale is read from an angle. How can it be avoided?", "Parallax error; look straight above the mark."),
    ("Find the total length if all five leaves are placed end to end.", "6.5 + 7.0 + 5.5 + 8.0 + 7.5 = 34.5 cm.")),
]
make(3, 'Full Syllabus · Chapters 1–12', A, B, C, D, E, 'Set_03')
