from h8 import *
import figs7 as F7
GR = F7.dist_time([(0, 0), (10, 20), (20, 40), (30, 40), (40, 40), (50, 60)], xmax=50, ymax=60, xl='Time (s)', yl='Distance (m)', xs=10, ys=10)
assert 20/10 == 2 and 40 == 40 and (60-40)/(50-40) == 2 and 60/50 == 1.2
A = [
 mc("Which of the following is an acid found in an ant's sting?", "Formic acid", ["Citric acid", "Acetic acid", "Tartaric acid"], "Ants inject formic acid; moist baking soda (a base) gives relief."),
 mc("Which of the following is an electrical insulator?", "Rubber", ["Copper", "Graphite", "Salt solution"], "Rubber does not allow electric current to pass."),
 mc("An iron nail dipped in copper sulphate solution gets a reddish-brown coating because:", "iron displaces copper from the solution", ["copper displaces iron", "iron dissolves completely", "the solution reacts with air"], "Iron is more reactive than copper, so it displaces copper which deposits on the nail."),
 mc("Obtaining crystals of copper sulphate from its hot saturated solution on cooling is a:", "physical change", ["chemical change", "nuclear change", "change in the type of atom"], "Only the state/form changes; the substance remains copper sulphate."),
 mc("Which hormone prepares the body of boys for changes at puberty such as the growth of a moustache and a deeper voice?", "Testosterone", ["Insulin", "Thyroxine", "Oestrogen"], "Testosterone from the testes brings the male changes."),
 mc("Heat from a hot pan travelling to its handle by direct contact is an example of:", "conduction", ["convection", "radiation", "evaporation"], "In conduction, heat moves through a solid from the hotter to the colder part."),
 mc("A horizontal line on a distance–time graph shows that the object is:", "at rest", ["moving at a uniform speed", "speeding up", "moving backwards"], "The distance does not change with time; the object is stationary."),
 mc("Blood vessels that carry blood away from the heart are called:", "arteries", ["veins", "capillaries", "lymph vessels"], "Arteries have thick, elastic walls to carry blood under high pressure away from the heart."),
 mc("The tissue that carries the food made in the leaves to other parts of the plant is the:", "phloem", ["xylem", "epidermis", "cuticle"], "Phloem transports food (sugar) to all parts."),
 mc("The wide field of view in the side mirror of a motorbike is possible because it is a:", "convex mirror", ["plane mirror", "concave mirror", "periscope"], "A convex mirror diverges light and shows a larger area."),
 mc("We see the Moon fully lit (round) on a:", "full moon day", ["new moon day", "first quarter day", "third quarter day"], "At full moon the whole lit half faces the Earth."),
 mc("The red pigment present in red blood cells that carries oxygen is:", "haemoglobin", ["chlorophyll", "insulin", "platelet"], "Haemoglobin is an iron-containing protein that binds oxygen."),
]
B = [
 sa("What is menstruation? State the approximate duration of the menstrual cycle and the age at which it begins in girls.", 2, "Menstruation is the monthly discharge of blood and the lining of the uterus when the egg released from the ovary is not fertilised (1). The cycle is about 28–30 days; it begins at puberty (roughly 10–14 years) (1)."),
 sa("Differentiate between breathing and respiration.", 2, "Breathing: taking in oxygen-rich air and giving out carbon dioxide — a physical process by lungs (1). Respiration: the chemical process in cells in which food (glucose) is broken down with oxygen to release energy (1)."),
 OR(sa("What is transpiration? State one advantage of it to the plant.", 2, "Loss of water as vapour from the aerial parts of the plant, mainly through stomata (1). It helps pull water up from roots (cooling effect/ transport of minerals) (1)."),
    sa("Name two plants that get nutrition in a way different from photosynthesis, stating the way.", 2, "Cuscuta (parasite — takes food from host); pitcher plant (insectivorous — traps insects); mushroom/bread mould (saprotroph — dead matter); Rhizobium-pulse plant (symbiosis) — any two with mode (½ + ½ each)")),
 sa("Why is burning of a candle regarded as both a physical and a chemical change? Identify each.", 2, "Melting of wax is a physical change (1); burning of wax with the wick forming carbon dioxide and water vapour (and soot) is a chemical change (1)."),
]
C = [
 sa("Trace the path of a piece of chapati through the human digestive system, naming the organs in order (mouth to anus) and what happens in the mouth.", 3, "Mouth (teeth chew, saliva starts digestion of starch) → oesophagus → stomach → small intestine → large intestine → rectum → anus (organs in order 2 marks); in the mouth saliva begins the digestion of starch (1)."),
 OR(sa("Give one example each of: (a) a parasitic plant (b) an insectivorous plant (c) a saprotrophic organism (d) an example of symbiosis. Explain one of these in a line.", 3, "(a) Cuscuta (b) pitcher plant/Venus flytrap (c) mushroom/bread mould (d) Rhizobium in pulses/lichen (½ each = 2); explanation of one (1)"),
    sa("Describe how the leaf of a green plant makes food. Write the word equation of photosynthesis.", 3, "Chlorophyll in leaves traps sunlight; carbon dioxide enters through stomata and water comes through xylem (1); they combine to form glucose and release oxygen (1). Carbon dioxide + water → (sunlight, chlorophyll) → glucose + oxygen (1).")),
 sa("An electric bulb glows when connected to a cell through a switch. (a) Name the part of the bulb that glows. (b) Why does only this part glow? (c) Write two precautions to be taken with household electrical appliances.", 3, "(a) The filament (1) (b) It is a thin wire of high resistance which gets heated by the current and glows (1) (c) Do not touch with wet hands; switch off before repair; do not overload sockets (any two, ½ each)"),
]
D = [
 sa("The table shows the blood circulation facts of four students. Use your knowledge to answer.<br><table class='t'><tr><th>Student</th><th>Pulse rate at rest (per min)</th><th>Pulse rate after running (per min)</th></tr><tr><td>Anil</td><td>72</td><td>120</td></tr><tr><td>Bina</td><td>78</td><td>126</td></tr><tr><td>Cyrus</td><td>70</td><td>112</td></tr><tr><td>Dia</td><td>75</td><td>129</td></tr></table>(i) Find the increase in pulse rate of each student. (ii) Who shows the greatest increase? (iii) Why does the pulse rate increase after running? (iv) Name the four chambers of the heart. (v) What does a pulse represent?", 5, "(i) Anil 48, Bina 48, Cyrus 42, Dia 54 (2 marks)<br>(ii) Dia (1)<br>(iii) Muscles need more oxygen and food; the heart pumps faster (1)<br>(iv) Right and left atria, right and left ventricles (½)<br>(v) Each heartbeat, as blood is pushed through arteries (½)"),
 OR(sa("(a) With the help of an activity, show that plants need sunlight for photosynthesis. (3)<br>(b) How is food transported in plants? (2)", 5, "(a) Cover part of a destarched leaf with black paper, keep in sunlight, remove chlorophyll in alcohol and add iodine; only the exposed part turns blue-black (3)<br>(b) Through phloem tubes: food is carried from leaves to all parts (and stored in roots/stem/fruits) (2)"),
    sa("(a) List any four physical changes that occur in boys and girls during adolescence. (2)<br>(b) Why is a balanced diet important for adolescents? (1)<br>(c) Suggest two hygiene tips during menstruation or puberty. (2)", 5, "(a) Any four (½ each): growth spurt; voice change; hair growth; breast development (girls); broader shoulders (boys); menstruation (girls); pimples<br>(b) Fast growth needs proteins, iron, calcium etc. (1)<br>(c) Bathe daily; use clean cloth/sanitary pads and change regularly; wash hands; (any two, 1 each)")),
 match(["Acid", "Rusting", "Fuse wire", "Mercury", "Insulin"],
       ["Controls blood sugar", "Chemical change of iron", "Metal that is a liquid", "Turns blue litmus red", "Low melting point wire", "Poor conductor of heat"],
       ["a–iv", "b–ii", "c–v", "d–iii", "e–i"]),
]
E = [
 c4("Sonu (12) eats mostly chips and sweets and has stopped eating vegetables. Her mother says that during the growing years, the body needs proper food, regular exercise and sleep. Sonu's school nurse also advises iodised salt for the thyroid.",
    ("Name the stage of growth Sonu is entering.", "Adolescence."),
    ("Which gland needs iodine to function properly?", "Thyroid gland."),
    ("Why is a balanced diet important at this stage? Name two nutrients that are particularly important.", "Rapid growth and development need adequate food; iron (to prevent anaemia in girls), calcium (bones), proteins — any two."),
    ("Suggest two reasons why peer pressure should not decide our food habits.", "Junk food gives energy but few nutrients; may cause obesity; irregular eating harms health; we should take decisions based on facts — any two.")),
 c4("A doctor listens to a patient's heartbeat with a stethoscope and takes a blood sample. The report shows a low level of haemoglobin, and the doctor advises iron-rich foods like spinach and jaggery.",
    ("Which blood cells contain haemoglobin?", "Red blood cells (RBCs)."),
    ("Name one disease caused by low haemoglobin.", "Anaemia."),
    ("State two functions of blood.", "Carries oxygen and food to cells; removes waste (CO₂, urea); WBCs fight germs; platelets clot blood — any two."),
    ("Why is it important to have blood clotting platelets?", "Platelets help blood to clot at a cut to stop bleeding and prevent infection.")),
 c4("Ria watered a cut celery stalk kept in coloured water. After a few hours, she saw the leaves and veins getting coloured. She also noted drops of water on the inner surface of a polythene bag tied around a leafy branch.",
    ("Which tissue carries coloured water up the stalk?", "Xylem."),
    ("What are the drops on the polythene bag due to?", "Transpiration — water vapour lost from leaves condenses."),
    ("Explain how a tall tree gets water from the roots to its top leaves.", "Roots absorb water; xylem vessels form continuous tubes; transpiration from leaves creates a pull that draws water up."),
    ("Write one function each of roots and stomata.", "Roots: absorb water and minerals/ anchor the plant; Stomata: gas exchange / transpiration.")),
 c4("In a science fair, Kabir plotted a distance–time graph of a toy car moving along a straight track, as shown, and a simple pendulum was timed using a stopwatch for 20 oscillations.",
    ("Name the instrument used for measuring time in the pendulum experiment.", "Stopwatch."),
    ("What does the slope (steepness) of a distance–time graph tell us?", "The speed: steeper = faster."),
    ("Find the speed of the car during the first 20 s from the graph.", "40 m in 20 s: speed = 2 m/s."),
    ("What does the horizontal part (20 s to 40 s) represent and what is the total distance covered in 50 s?", "The car is at rest; total distance = 60 m."), fig=GR),
]
make(3, 'Set 03 · Emphasis: Life Processes, Adolescence & Applications', A, B, C, D, E, 'Set_03')
