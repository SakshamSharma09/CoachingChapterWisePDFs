from h8 import *
import figs6s as G
# ---------- Science Set 1 : emphasis Food, Magnets, Separation, Temperature, Beyond Earth ----------
A = [
 mc("Meena sees ants gathering near some spilled sugar and wonders, \"Do ants prefer sugar to salt?\" The best way to find out is to:", "place equal amounts of sugar and salt at equal distances from the ants and watch where they go", ["ask her friends what they think", "put only sugar and look at the ants", "read a story about ants"], "A fair test changes only one thing (sugar or salt) and keeps other conditions the same."),
 mc("A plant has a thin, weak stem and holds a fence with its tendrils to grow upwards. It is a:", "climber", ["herb", "shrub", "tree"], "Plants with weak stems that climb by tendrils or twining are climbers."),
 mc("Ravi's gums bleed often. The doctor advises more amla, lemon and guava. These foods mainly contain:", "vitamin C", ["vitamin D", "iron", "starch"], "Lack of vitamin C causes scurvy (bleeding gums); citrus fruits and amla are rich in it."),
 mc("A bar magnet is hung freely from a thread. It comes to rest pointing roughly:", "north–south", ["east–west", "up–down", "in any direction"], "A freely suspended magnet aligns itself in the north–south direction."),
 mc("The left end of a ruler is broken and its first visible mark is 2 cm. A pencil starts at the 2 cm mark and ends at 9 cm. The length of the pencil is:", "7 cm", ["9 cm", "11 cm", "2 cm"], "Length = 9 − 2 = 7 cm; measure from a clear mark and subtract.", fig=G.ruler(2, 12, 2, 9)),
 mc("A window pane should be made of a material that is:", "transparent", ["opaque", "rough", "magnetic"], "We need to see through a window, so the material must be transparent, like glass."),
 mc("A clinical thermometer is given a sharp jerk before use, so that:", "the mercury level falls below 35 °C", ["the mercury becomes hotter", "the bulb breaks", "the scale gets cleaned"], "The kink stops mercury from falling back on its own, so it must be shaken down."),
 mc("Wet clothes will dry the fastest on a:", "hot, dry and windy day", ["cold, humid and still day", "cool and rainy day", "cold and foggy day"], "Evaporation is faster in heat, wind and low humidity."),
 mc("After harvest, a farmer separates light husk from heavy wheat grains by dropping the mixture from a height on a windy day. This method is:", "winnowing", ["sieving", "filtration", "evaporation"], "Wind blows the lighter husk away, while the heavier grains fall down."),
 mc("A camel can live for many days in a desert with little water. This is an example of:", "adaptation", ["reproduction", "growth", "migration only"], "Features that help a living thing survive in its habitat are adaptations."),
 mc("Which of the following is a renewable natural resource?", "Wind", ["Coal", "Petroleum", "Natural gas"], "Wind is replaced by nature continuously; coal, petroleum and natural gas take millions of years to form."),
 mc("On a clear night, Aarav sees a bright point of light that shines steadily without twinkling. It is most likely a:", "planet", ["star", "comet", "galaxy"], "Stars twinkle because of Earth's moving air; planets are closer and appear steady."),
]
B = [
 sa("Name the nutrient needed for growth and repair of the body. Give two food sources of it.", 2, "Proteins (1). Sources: dal/pulses, milk, paneer, eggs, fish, soybean (any two; 1)."),
 OR(sa("Convert: (i) 2.5 km into metres (ii) 350 cm into metres.", 2, "(i) 2.5 × 1000 = 2500 m (1) (ii) 350 ÷ 100 = 3.5 m (1)"),
    sa("Name the type of motion in each case: (i) a child on a swing (ii) a car moving on a straight road.", 2, "(i) Periodic (to-and-fro) motion (1) (ii) Linear (rectilinear) motion (1)")),
 sa("Why do puddles of water on the road disappear on a sunny day? Name the process.", 2, "Water changes into water vapour by evaporation (1); heat of the Sun speeds up evaporation, so the puddle dries up (1)."),
 sa("Write two characteristics of living things with one example of each.", 2, "Any two: they grow (a plant grows from a seed), respire, respond to stimuli (touch-me-not folds leaves), reproduce (hen lays eggs), need food (1 mark each)."),
]
C = [
 sa("Classify the following plants as herb, shrub or tree and write one difference between a shrub and a tree: tulsi, rose, mango.", 3, "Tulsi — herb; rose — shrub; mango — tree (2 marks). A shrub has many branches near the ground and is not very tall, a tree has a single thick, tall, woody trunk (1 mark)."),
 sa("Pooja sorted some objects: glass tumbler, eraser, steel spoon, wooden ruler. (i) Which is transparent? (ii) Which has lustre (shine)? (iii) Name one property that makes steel suitable for making a spoon.", 3, "(i) Glass tumbler (1) (ii) Steel spoon (1) (iii) Hard / strong / does not break or rust easily (any one) (1)."),
 sa("Name the best method of separating: (i) sand from water (ii) salt from salt solution (iii) iron filings from sand.", 3, "(i) Filtration or sedimentation and decantation (1) (ii) Evaporation (1) (iii) Magnetic separation using a magnet (1)"),
]
D = [
 match(["Vitamin A", "Vitamin C", "Vitamin D", "Iron", "Iodine"], ["Bleeding gums (scurvy)", "Goitre", "Weak bones (rickets)", "Night blindness", "Anaemia"], ["a–iv", "b–i", "c–iii", "d–v", "e–ii"], "Match the nutrient in Column I with the deficiency problem in Column II."),
 OR(sa("A mixture contains salt, sand and iron filings. Describe the steps to separate all three components.", 5, "Step 1: pass a magnet over the mixture — iron filings stick to it (1). Step 2: add water and stir — salt dissolves (1). Step 3: filter — sand remains on the filter paper (1). Step 4: heat the filtrate (salt solution) in a dish to evaporate the water (1). Salt crystals are left behind (1)."),
    sa("(a) Name the apparatus shown in the figure and the process. (b) What is the residue and what is the filtrate if muddy water is poured through it? (c) Why do we use a filter paper?", 5, "(a) Funnel with filter paper — filtration (2). (b) Residue: mud/sand particles on the paper; filtrate: clear water in the beaker (2). (c) Its tiny pores let water pass but hold back the insoluble particles (1).", fig=G.funnel())),
 OR(sa("Describe an activity to find out which of these objects are attracted by a magnet: iron nail, plastic comb, copper coin, steel key, rubber band.", 5, "Collect the objects and a bar magnet (1). Bring the magnet near each object one by one (1). Observe and record in a table (1). Iron nail and steel key are attracted (magnetic materials) (1); plastic comb, copper coin and rubber band are not (non-magnetic materials) (1)."),
    sa("Describe any five properties of a magnet.", 5, "Any five (1 each): attracts iron, nickel, cobalt; has two poles (N and S); strongest at the poles; freely suspended it points north–south; like poles repel and unlike poles attract; can lose magnetism if heated or hammered; magnetic force acts at a distance.")),
]
E = [
 c4("In a science lab Rohit dipped a laboratory thermometer in a beaker of hot water for the first time. The figure shows the thermometer reading just after he took it out of the heat source.",
    ("What is the temperature shown in the figure?", "60 °C (the mercury thread stops at the 60 mark)."),
    ("Name the unit in which the temperature is measured.", "Degree Celsius (°C)."),
    ("Rohit wants to measure his body temperature. Why should he not use this thermometer?", "Its range is −10 °C to 110 °C and it has no kink, so the reading can fall when taken out and it is not designed for body temperature; a clinical thermometer (35–42 °C) is used."),
    ("State two precautions while using a laboratory thermometer.", "Hold it upright; bulb should be in the liquid and not touch the walls/bottom; eye in line with the mercury thread; do not hold it by the bulb (any two)."), fig=G.thermo(60)),
 c4("In Rajasthan, the villagers of a dry village built a johad (small earthen check dam) to store rainwater. Within two years the water level of their wells rose, and the fields became green again. The village also protects its sacred groves (orans) and does not cut the trees.",
    ("Name the natural resource conserved by the johad.", "Water."),
    ("Name one more natural resource the villagers are protecting.", "Forests/trees (or soil)."),
    ("How did the johad help raise the water level in the wells?", "Rainwater is held and slowly seeps into the ground, recharging groundwater."),
    ("Suggest two things students can do at home to save water.", "Close taps when not in use; fix leaks; reuse washing water for plants; harvest rainwater (any two).")),
 c4("The students of Class 6 watched the sky after sunset for three nights. On the first night the Moon looked like a thin bright curve; a few nights later more of it was bright. They also noticed that one bright, non-twinkling object stayed near the Moon.",
    ("What are the different shapes of the bright part of the Moon called?", "Phases of the Moon."),
    ("Is the Moon a star? Give a reason.", "No — it does not give its own light; it reflects sunlight (it is a natural satellite of Earth)."),
    ("Why does the Moon look different on different nights?", "The Moon revolves around the Earth, so we see different portions of its sunlit half on different days."),
    ("Name the day when the Moon is not visible and the day when the full Moon is seen.", "New-moon day (Amavasya) and full-moon day (Poornima).")),
 c4("In the salt pans of Sambhar Lake in Rajasthan, salty water is collected in shallow pits and left in the hot Sun. After some days white salt crystals are seen at the bottom of the pits.",
    ("Name the process by which water leaves the pits.", "Evaporation."),
    ("Why are the pits made shallow and kept in the Sun?", "A large surface area and heat speed up evaporation."),
    ("Name the substance that remains behind when water evaporates.", "Salt (the dissolved solid)."),
    ("Describe in words what happens to this water vapour after it leaves the pits.", "Water vapour rises, cools and condenses to form clouds; falls as rain/snow back to the Earth (2 marks: evaporation → condensation → rain).")),
]
make(1, 'Full Syllabus · Chapters 1–12', A, B, C, D, E, 'Set_01')
