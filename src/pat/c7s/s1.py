from h8 import *
import figs7 as F7
GRAPH = F7.dist_time([(0, 0), (1, 12), (2, 24), (3, 24), (4, 36)], xmax=4, ymax=36, ys=6)
# check: slope 12 km/h for 0-2 h, rest 2-3 h, 12 km/h for 3-4 h, average = 36/4
assert 24/2 == 12 and 36/4 == 9 and (36-24)/1 == 12
assert 150/2.5 == 60
A = [
 mc("A paper strip stained with turmeric is dipped in a soap solution. The strip turns:", "red", ["blue", "green", "colourless"], "Turmeric turns red in a basic solution such as soap solution; it stays yellow in acids and neutral solutions."),
 mc("The heating element of an electric heater is made of nichrome because nichrome has:", "high resistance and high melting point", ["low resistance and low melting point", "high resistance and low melting point", "zero resistance"], "A high-resistance wire gets very hot, and a high melting point stops it from melting."),
 mc("Which of the following non-metals is a good conductor of electricity?", "Graphite", ["Sulphur", "Iodine", "Phosphorus"], "Graphite, a form of carbon, conducts electricity (used in pencil leads and cell electrodes)."),
 mc("Which of the following is a chemical change?", "Curdling of milk", ["Melting of wax", "Dissolving sugar in water", "Tearing of paper"], "Curdling forms new substances (lactic acid, curd) and cannot be reversed; the rest are physical changes."),
 mc("A person's body does not make enough insulin. The gland that is affected is the:", "pancreas", ["thyroid", "pituitary", "adrenal"], "Insulin, which controls blood sugar, is made by the pancreas."),
 mc("Water in a pan on a stove is heated from below. The heat spreads through the water mainly by:", "convection", ["conduction", "radiation only", "none of these"], "Warm water rises and cooler water sinks, setting up convection currents."),
 mc("A car covers 150 km in 2 h 30 min. Its average speed is:", "60 km/h", ["50 km/h", "65 km/h", "75 km/h"], "Speed = 150 km ÷ 2.5 h = 60 km/h."),
 mc("Most of the digested food is absorbed into the blood in the:", "small intestine", ["stomach", "large intestine", "oesophagus"], "The small intestine has finger-like villi with a large surface area for absorption."),
 mc("Plants take in carbon dioxide for photosynthesis through tiny pores in the leaf called:", "stomata", ["xylem vessels", "root hairs", "veins"], "Stomata allow gases to enter and leave the leaf."),
 mc("The image formed by a plane mirror is:", "virtual, upright, of the same size and laterally inverted", ["real, inverted and of the same size", "real and magnified", "virtual and diminished"], "A plane mirror forms a virtual, erect image the same size as the object, with left and right interchanged."),
 mc("A solar eclipse can occur only on:", "a new moon day", ["a full moon day", "a half-moon day", "any day the Moon is bright"], "The Moon passes between the Sun and Earth only at new moon."),
 mc("Zinc granules are added to dilute hydrochloric acid and a burning matchstick is brought near the mouth of the test tube. A 'pop' sound is heard because the gas released is:", "hydrogen", ["oxygen", "carbon dioxide", "nitrogen"], "Metals react with acids to release hydrogen, which burns with a pop sound."),
]
B = [
 OR(sa("Farmers spread slaked lime on soil which has become too acidic. Name the type of reaction involved and state its result in one line.", 2, "Neutralisation (1) — the base in lime reacts with the acid in the soil to form salt and water, making the soil less acidic (1)."),
    sa("Name two natural indicators. How would turmeric and blue litmus behave when dipped in lemon juice?", 2, "Natural indicators: turmeric, litmus, China-rose petals, red cabbage (any two) (1). Turmeric stays yellow; blue litmus turns red (1).")),
 sa("Electric wires are made of copper but are covered with plastic. Give the reason for each choice.", 2, "Copper is a metal and a good conductor of electricity, so current flows easily (1). Plastic is an insulator; it prevents shocks and short circuits (1)."),
 sa("Classify each as a physical or chemical change: (a) melting of ice (b) rusting of an iron gate (c) dissolving salt in water (d) burning of a candle.", 2, "(a) Physical (b) Chemical (c) Physical (d) Chemical (½ mark each)"),
 sa("The Moon always shows the same face to us. Give the reason.", 2, "The Moon takes the same time (about 27.3 days) to rotate once on its axis as to revolve once around the Earth (1+1)."),
]
C = [
 OR(sa("(a) Write the word equation for the burning of magnesium ribbon in air. (b) A clean iron nail is kept in copper sulphate solution for 30 minutes. State two observations.", 3, "(a) Magnesium + oxygen → magnesium oxide (1)<br>(b) A reddish-brown deposit of copper forms on the nail (1); the blue colour of the solution fades to light green (1)."),
    sa("Rusting is a serious problem for iron bridges and railings. (a) Name the two things needed for rusting. (b) Give two methods to prevent it.", 3, "(a) Oxygen (air) and moisture (water) (1)<br>(b) Painting, oiling/greasing, galvanisation (zinc coating), making alloys like stainless steel (any two, ½ + ½ + 1 for correct description)")),
 sa("Describe a simple activity to show that a gas is produced when baking soda is mixed with vinegar. Name the gas and state how you will test it.", 3, "Take a little baking soda in a test tube and add vinegar; bubbles appear (fizzing) (1). The gas is carbon dioxide (1). Pass the gas into lime water: it turns milky (1)."),
 sa("A bulb in a house stops working suddenly and the fuse has blown. (a) What is a short circuit? (b) How does a fuse protect appliances? (c) Name a modern device that replaces the fuse.", 3, "(a) When live and neutral wires touch directly, a very large current flows (1). (b) The fuse wire has a low melting point; it melts and breaks the circuit (1). (c) MCB (miniature circuit breaker) (1)."),
]
TABLE = ("<table class='t'><tr><th>Solution</th><th>Observation</th></tr>"
 "<tr><td>P</td><td>Blue litmus turns red</td></tr><tr><td>Q</td><td>Red litmus turns blue; turmeric turns red</td></tr>"
 "<tr><td>R</td><td>No change in red or blue litmus or turmeric</td></tr><tr><td>S</td><td>Red litmus turns blue</td></tr></table>")
D = [
 sa("Rina tested four colourless solutions P, Q, R and S with indicators. Her observations are in the table.<br>" + TABLE + "(i) Classify P, Q, R and S as acidic, basic or neutral. (ii) Name one household substance which could be R. (iii) If P and S are mixed in the right amount, what type of reaction takes place and what is formed?", 5, "(i) P — acidic; Q — basic; R — neutral; S — basic (2 marks, ½ each)<br>(ii) Common salt solution / sugar solution / distilled water (1 mark)<br>(iii) Neutralisation (1 mark); salt and water are formed (1 mark)"),
 OR(sa("(a) Differentiate between metals and non-metals on any four properties (lustre, malleability/ductility, sound and conduction). (4)<br>(b) Name one metal that is a liquid at room temperature. (1)", 5, "(a) Any four (1 each): Metals — lustrous; malleable and ductile; sonorous; good conductors of heat and electricity. Non-metals — dull; brittle; non-sonorous; poor conductors (graphite excepted)<br>(b) Mercury (1)"),
    sa("(a) Describe an experiment to find out the conditions needed for rusting using three test tubes. (3)<br>(b) In which test tube will rust form fastest and why? (2)", 5, "(a) Tube 1: iron nail with water and air; Tube 2: nail in boiled water covered with oil (no air); Tube 3: nail with dry air/calcium chloride (no water) (2); observe after a few days (1)<br>(b) Tube 1, because both oxygen and moisture are present (2)")),
 OR(sa("The graph shows the journey of a cyclist. Use it to answer: (i) Find the speed during the first 2 hours. (ii) What does the horizontal part between 2 h and 3 h show? (iii) What distance was covered in 4 h? (iv) Find the average speed for the whole journey. (v) Is the motion uniform or non-uniform?", 5, "(i) 24 km ÷ 2 h = 12 km/h (1)<br>(ii) The cyclist is at rest (distance does not change) (1)<br>(iii) 36 km (1)<br>(iv) 36 km ÷ 4 h = 9 km/h (1)<br>(v) Non-uniform (speed changes/stops) (1)", fig=GRAPH),
    sa("(a) Explain conduction, convection and radiation with one everyday example each. (3)<br>(b) Why do we prefer to wear light-coloured clothes in summer? (1)<br>(c) Name the instrument used to measure human body temperature and write its range. (1)", 5, "(a) Conduction: heat flows through a solid, e.g. a spoon heated in tea (1); Convection: heat flows through liquids/gases by movement of particles, e.g. sea breeze/boiling water (1); Radiation: heat travels without a medium, e.g. warmth from the Sun/fire (1)<br>(b) Light colours reflect more heat (1)<br>(c) Clinical thermometer; 35 °C to 42 °C (1)")),
]
E = [
 c4("Meera, who is 13, tells her friend that her height has increased quickly in the past year, she has begun to feel moody, and she is worried about her skin developing pimples. Her friend Arjun says his voice has become deep and cracks sometimes.",
    ("Name the stage of life in which these changes occur.", "Adolescence (puberty)."),
    ("Which structure in the throat grows larger in boys and causes the voice to deepen?", "The larynx (voice box)/Adam's apple."),
    ("Name two chemical messengers that bring these changes and the glands that release them.", "Hormones, e.g. testosterone from testes and oestrogen from ovaries; (growth hormone from pituitary) — any two correctly matched."),
    ("Suggest two healthy habits for adolescents.", "Balanced diet with iron, calcium; regular exercise; sleep; personal hygiene; avoid junk food; talk to trusted elders — any two.")),
 c4("Ravi had a heavy lunch of dal, roti, rice and curd. After some time he felt his heart beating fast while playing, and his breathing became deeper.",
    ("In which organ does the digestion of proteins begin?", "Stomach."),
    ("Which blood cells carry oxygen, and which pigment helps in this?", "Red blood cells; haemoglobin."),
    ("Explain why breathing and heartbeat rates increase during exercise.", "Muscles need more energy so cells need more oxygen/food for respiration; faster breathing brings in more oxygen and a faster heartbeat carries it quickly to the cells and removes carbon dioxide."),
    ("Write the word equation of cellular respiration.", "Glucose + oxygen → carbon dioxide + water + energy.")),
 c4("In a school experiment, Shreya covered a part of a leaf of a potted geranium plant with black paper and kept it in sunlight for a day. She then boiled the leaf in alcohol and tested it with iodine.",
    ("What is the purpose of boiling the leaf in alcohol?", "To remove chlorophyll (green colour) so that the colour change with iodine can be seen."),
    ("Which part of the leaf will turn blue-black with iodine?", "The uncovered part which received sunlight."),
    ("What does the result show about the conditions for photosynthesis?", "Photosynthesis (starch formation) needs light; the covered part got no light so no starch formed."),
    ("Name the gas given out and the raw material taken in by leaves during photosynthesis.", "Oxygen is given out; carbon dioxide (and water) is taken in.")),
 c4("A bus conductor sits near the rear-view mirror and a dentist uses a small curved mirror to see teeth. A student makes a pinhole camera from a shoe box and observes a candle flame through it.",
    ("What type of mirror is used as a rear-view mirror in vehicles?", "A convex mirror."),
    ("State the nature of the image seen in the pinhole camera.", "Inverted (and real) image."),
    ("Why is a convex mirror preferred as a rear-view mirror?", "It always forms an upright, smaller image and gives a wider field of view of traffic behind."),
    ("Why does the dentist use a concave mirror?", "A concave mirror held close to the tooth forms an enlarged, upright image of the tooth.")),
]
make(1, 'Set 01 · Emphasis: Materials & Chemical Changes', A, B, C, D, E, 'Set_01')
