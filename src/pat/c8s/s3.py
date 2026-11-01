from h8 import *
A = [
 mc("A student claims that plants grow faster in music. To test it fairly she should:", "grow two identical plants under the same conditions, one with music and one without", ["play music to only one plant and give it extra water", "use plants of different species", "keep both plants in the dark"], "A fair test changes only one variable."),
 mc("Which of the following is used to make bread soft and spongy?", "Yeast", ["Rhizobium", "Amoeba", "Lactobacillus"], "Yeast produces carbon dioxide that makes dough rise."),
 mc("A person has repeated cold, fever and is infected by a virus. Which medicine will NOT help in killing the virus?", "Antibiotic", ["Rest and fluids", "Vaccine given earlier for prevention", "Antiviral drug prescribed by a doctor"], "Antibiotics do not work on viruses."),
 mc("A cell in a circuit is shown by a long line and a short line. The longer line represents the:", "positive terminal", ["negative terminal", "switch", "bulb"], "The long line is the positive terminal."),
 mc("In the figure of the electromagnet, the iron pins are attracted when the switch is:", "closed", ["open", "removed from the circuit", "connected to a wooden nail"], "Current flows only when the circuit is closed.", fig=F.electromagnet()),
 mc("A boy pushes a heavy wall but it does not move. The reason is that:", "the net force on the wall is zero as friction and other forces balance his push", ["he applied no force", "walls cannot experience force", "gravity cancels friction only"], "Balanced forces – no change in state of motion."),
 mc("An object weighs 60 N on Earth. Its mass is nearly (g = 10 m/s²):", "6 kg", ["60 kg", "600 kg", "0.6 kg"], "m = W/g = 60/10 = 6 kg."),
 mc("In the figure, water comes out fastest and farthest from hole:", "C, the lowest hole", ["A, the topmost hole", "B, the middle hole", "All holes equally"], "Pressure increases with depth.", fig=F.pressure_tank()),
 mc("Which of these will be helpful when a cyclone warning is announced?", "Move to a cyclone shelter and keep a radio/battery and emergency kit ready", ["Go to the seashore to see it", "Stand under tall trees", "Fly a kite"], "Follow safety instructions."),
 mc("The pressure exerted by a gas in a closed container is due to:", "continuous collisions of its particles with the walls", ["gravity pulling the gas down only", "attraction between the particles", "its colour"], "Particles strike the wall and exert force."),
 mc("Which statement is correct about solids?", "Particles vibrate about fixed positions", ["Particles move freely everywhere", "There is no force between particles", "They have no definite volume"], "Solids keep their shape as particles vibrate in place."),
 mc("A pressure cooker cooks food faster mainly because:", "the increased pressure raises the boiling point of water", ["it makes water colder", "it removes all air pressure", "it uses more water"], "Higher pressure → higher boiling point."),
]
B = [
 sa("Why is it important to record observations carefully during an investigation?", 2, "Observations are the evidence used to draw conclusions (1); careless records cause wrong inferences and prevent repeating the investigation (1)."),
 OR(sa("Name two harmful effects of microorganisms.", 2, "Cause diseases in humans, animals and plants (cholera, rust of wheat); spoil food and other materials (any two, 1 each)."),
    sa("How do Lactobacillus bacteria help in the formation of curd? (Answer in two points.)", 2, "They multiply in warm milk (1) and change the milk sugar to lactic acid, which sets the milk into curd (1).")),
 sa("Why do electric wires used in houses have a plastic/rubber coating?", 2, "Plastic/rubber is an insulator (1); it prevents electric shocks and short circuits (1)."),
 sa("Why does an inflated balloon burst when it is squeezed hard at a point, but not when pressed by a flat hand?", 2, "A small area of contact gives high pressure (1); the flat hand spreads the force over a large area, so the pressure is small (1)."),
]
C = [
 OR(sa("Differentiate between communicable and non-communicable diseases (any two points) and give one example of each.", 3, "Communicable: spread from person to person through air/water/food/vectors; caused by microorganisms; e.g., tuberculosis. Non-communicable: do not spread; due to lifestyle/genes/diet; e.g., diabetes. (any two points + examples)"),
    sa("List three ways to prevent infectious diseases.", 3, "Vaccination; clean drinking water and food; hand washing; covering nose while sneezing; controlling mosquito breeding; avoiding contact with ill persons (any three).")),
 sa("An electric heater of a room warms up in a few minutes, yet the wire joining it to the plug stays cool. Explain.", 3, "The heating element has high resistance, so it produces large heat (1). Supply wires have very low resistance (1), hence the same current produces negligible heating in them (1)."),
 OR(sa("A force of 400 N acts on a surface of area 0.2 m². Calculate the pressure. What will be the pressure if the area is doubled for the same force?", 3, "P = F/A = 400/0.2 = 2000 Pa (1½). New area 0.4 m²: P = 400/0.4 = 1000 Pa (1½)."),
    sa("Explain why it is easier to cut with a sharp knife than a blunt knife and why heavy vehicles have wide tyres. Use the idea of pressure.", 3, "Sharp knife: small area, high pressure (1). Wide tyres: large area, low pressure, so they do not sink (1). Pressure = force/area (1).")),
]
D = [
 fill(["Antibiotic", "Barometer", "Fertilisation?", "Hypothesis", "Diffusion"],
      ["A ________ is a tentative explanation that can be tested by an experiment.", "The movement of particles from a region of higher concentration to lower concentration is ________.", "A ________ is an instrument used to measure atmospheric pressure.", "An ________ such as penicillin kills bacteria.", "Particles of gases show ________ rapidly."],
      ["Hypothesis", "Diffusion", "Barometer", "Antibiotic", "Diffusion"]) if False else
 fill(["Antibiotic", "Barometer", "Hypothesis", "Diffusion", "Gravity"],
      ["A ________ is a tentative explanation that can be tested by experiment.", "The spreading of particles of one substance into another on their own is called ________.", "A ________ is an instrument used to measure atmospheric pressure.", "An ________ such as penicillin kills bacteria.", "The force of ________ pulls objects towards the centre of the Earth."],
      ["Hypothesis", "Diffusion", "Barometer", "Antibiotic", "Gravity"]),
 match(["Amoeba", "Rhizobium", "Nichrome", "Friction", "Liquid"],
       ["protozoan", "fixes nitrogen in root nodules", "alloy used in heating elements", "force opposing relative motion", "takes the shape of the container but has fixed volume", "SI unit of pressure"],
       ["a–i", "b–ii", "c–iii", "d–iv", "e–v"]),
 OR(sa("(a) In the circuit shown, a coil is wound round an iron nail. Name the device and state two factors on which its strength depends. (3)<br>(b) How can its poles be reversed? (2)", 5, "(a) Electromagnet (1); strength depends on number of turns and current (and core material) (2). (b) By reversing the direction of current (2).", fig=F.electromagnet()),
    sa("(a) Name the three states of matter and give one example of each. (3)<br>(b) Why can a gas fill the whole container but a solid cannot? (2)", 5, "(a) Solid – wood/ice; liquid – water/milk; gas – air/oxygen (3×1). (b) Gas particles have very weak attraction, large spaces and move freely in all directions (2).")),
]
E = [
 c4("Ravi saw white fur-like growth on a piece of bread kept in a warm damp cupboard for a week.",
    ("Which group of microorganisms has grown on the bread?", "Fungi (bread mould)."),
    ("Name one condition that helped the growth.", "Warmth and moisture/ dampness."),
    ("Suggest two ways to prevent food from such spoilage.", "Refrigeration; drying; keep in airtight containers; use preservatives (any two)."),
    ("Name one useful fungus and its use.", "Yeast – baking/ fermentation; Penicillium – antibiotic penicillin.")),
 c4("Sara tested two bulbs: one bulb had a thin tungsten filament and the other a thick copper wire in place of the filament. The tungsten bulb glowed bright, the copper wire only became slightly warm.",
    ("What effect of current makes the filament glow?", "Heating effect."),
    ("Which has more resistance – tungsten filament or copper wire?", "Tungsten filament."),
    ("Why is tungsten used as the filament material?", "It has a very high melting point and high resistance so it can glow white-hot without melting."),
    ("Name two appliances that work on the heating effect of current.", "Electric iron, toaster, heater, kettle, geyser (any two).")),
 c4("A girl of mass 40 kg stands on a bathroom weighing scale. The scale reads 400 N. The next day her brother of mass 30 kg stands on the same scale.",
    ("What quantity does the scale actually measure here?", "Weight (force) in newton."),
    ("What will the scale read for her brother (g = 10 m/s²)?", "300 N."),
    ("Would their masses change on the Moon? Would their weights change? Explain.", "Mass does not change; weight becomes about one-sixth because the Moon's gravity is weaker."),
    ("Give two differences between mass and weight.", "Mass – quantity of matter, kg, constant; weight – force of gravity, N, depends on place (any two).")),
 c4("A balloon filled with air is tied tightly and kept in the hot sun. After some time it bursts. Rohit recalled that pressure of a gas depends on the movement of its particles.",
    ("What causes the pressure of a gas in a balloon?", "Particles colliding with the walls."),
    ("What happens to the speed of particles when the gas is heated?", "Increases."),
    ("Explain why the balloon burst in the sun.", "Heating increases particle speed and collisions, so internal pressure increases beyond what the balloon can withstand."),
    ("Why does a gas fill a container completely?", "Particles move randomly in all directions with little attraction and large spaces.")),
]
make(3, 'Term I · Chapters 1–7', A, B, C, D, E, 'Set_03')
