from h8 import *
A = [
 mc("Two identical beakers have cold and hot water. Equal spoons of sugar are added to test where sugar dissolves faster. Which should be kept the SAME in both beakers?", "Volume of water and amount of sugar", ["Temperature of water", "Time taken to dissolve", "Speed of dissolving"], "Only the variable under test (temperature) changes; everything else is a controlled variable."),
 mc("Which of the following is a unicellular protozoan?", "Amoeba", ["Penicillium", "Spirogyra", "Mucor"], "Amoeba is a single-celled protozoan; the others are fungi/algae."),
 mc("Rhizobium bacteria living in the root nodules of pulse plants help the plant by:", "fixing atmospheric nitrogen into usable form", ["absorbing sunlight", "making curd", "causing root rot"], "Rhizobium fixes nitrogen."),
 mc("Which of these diseases can be prevented by vaccination?", "Measles", ["Diabetes", "Cancer", "High blood pressure"], "Measles is a vaccine-preventable communicable disease."),
 mc("Which statement about antibiotics is correct?", "They act on bacteria and should be taken only on a doctor's advice", ["They cure viral infections such as the common cold", "They can be taken in any quantity for any illness", "They are made only from viruses"], "Antibiotics are effective against bacteria, not viruses."),
 mc("Which change will NOT increase the strength of an electromagnet?", "Replacing the iron core with a wooden rod", ["Increasing the number of turns in the coil", "Connecting one more cell in series", "Using a soft iron core"], "A wooden rod is not magnetic, so the field gets weaker."),
 mc("A fuse wire is chosen because it has:", "a low melting point", ["a very high melting point", "a very high conductivity only", "no resistance"], "It melts quickly when excess current flows, breaking the circuit."),
 mc("A football rolling on the ground gradually slows down and stops. The force mainly responsible is:", "friction", ["magnetic force", "electrostatic force", "buoyant force"], "Friction between ball and ground opposes the motion."),
 mc("A force of 200 N acts perpendicularly on an area of 0.5 m². The pressure is:", "400 Pa", ["100 Pa", "200 Pa", "0.0025 Pa"], "P = F/A = 200 ÷ 0.5 = 400 Pa."),
 mc("The wall of a dam is made thicker at the bottom because:", "pressure of water increases with depth", ["water is heavier at the surface", "pressure decreases with depth", "water exerts no pressure sideways"], "Liquid pressure increases with depth."),
 mc("A drop of ink spreads evenly in a glass of still water after some time. This shows that:", "particles of matter move and mix by themselves", ["water particles are at rest", "ink and water react chemically", "ink particles are heavier than water"], "Diffusion."),
 mc("Which of the following is TRUE for particles of matter?", "They are always in motion and have spaces between them", ["They are completely at rest in solids", "They have no force of attraction", "They are very large and visible to eye"], "Particles of all states are in motion (vibrating in solids) with inter-particle space."),
]
B = [
 OR(sa("Differentiate between an <i>observation</i> and an <i>inference</i> with one example.", 2, "Observation: what we directly see/measure with senses or instruments (e.g., the leaf is yellow). Inference: explanation drawn from observations (e.g., the plant lacks nutrients). (1 + 1)"),
    sa("What is a <i>variable</i> in an experiment? Give one example of a variable that is kept constant.", 2, "A factor that can change/be changed in an experiment (1). Example controlled variable: amount of water given to each plant (1).")),
 sa("Why is it advised to boil drinking water in flood-affected areas?", 2, "Floodwater mixes with sewage and carries disease-causing microorganisms (1). Boiling kills them and prevents water-borne diseases like cholera and typhoid (1)."),
 sa("State any two differences between a permanent magnet and an electromagnet.", 2, "Permanent magnet: keeps magnetism, fixed strength, poles cannot be reversed. Electromagnet: magnetic only while current flows, strength can be changed, polarity can be reversed by reversing current. (any two, 1 each)"),
 sa("A sharp knife cuts a vegetable easily but a blunt knife does not, though the same force is applied. Why?", 2, "Sharp edge has a smaller area (1); same force on smaller area gives larger pressure (P = F/A), so it cuts easily (1)."),
]
C = [
 OR(sa("Name the three groups of microorganisms other than viruses and give one example of each.", 3, "Bacteria (Lactobacillus/Rhizobium), fungi (yeast/Penicillium/mushroom), protozoa (Amoeba/Paramecium), algae (Spirogyra) — any three groups with examples (1 each)."),
    sa("Explain how milk is converted into curd.", 3, "A small amount of curd (containing Lactobacillus bacteria) is added to warm milk (1). The bacteria multiply in warmth and turn milk sugar into lactic acid (1). Lactic acid coagulates milk proteins and sets it as curd (1).")),
 sa("Design a simple activity to show that liquids exert pressure on the walls of a container.", 3, "Take a plastic bottle and make three holes at different heights on its side (1). Fill it with water and observe water jets (1). Water spurts out sideways, and the jet from the lowest hole travels farthest, showing sideways pressure that increases with depth (1)."),
 OR(sa("Distinguish between solids, liquids and gases on the basis of arrangement of particles, inter-particle space and shape.", 3, "Solids: particles closely packed, very little space, definite shape. Liquids: particles slightly apart, can slide, take shape of container. Gases: particles far apart, large space, no fixed shape/volume. (1 mark for each state)"),
    sa("Perfume sprayed in one corner of a room can be smelt in the opposite corner after some time. Explain, using the particle idea.", 3, "Perfume particles are in constant random motion (1). There is a lot of space between air particles (1). Perfume particles intermix with air particles (diffusion) and spread throughout the room (1).")),
]
D = [
 fill(["Bacteria", "Vaccine", "Electromagnet", "Pascal", "Friction"],
      ["A ________ is a preparation that trains the body to fight a specific disease.", "The SI unit of pressure is the ________.", "A temporary magnet made by passing current through a coil wound over soft iron is a(n) ________.", "________ opposes the relative motion between two surfaces in contact.", "________ are microorganisms that are single-celled and have no true nucleus."],
      ["Vaccine", "Pascal", "Electromagnet", "Friction", "Bacteria"]),
 match(["Barometer", "Heating element", "Penicillin", "Weight", "Diffusion"],
       ["alloy of high resistance and high melting point", "measures atmospheric pressure", "force with which Earth attracts a body, measured in newton", "mixing of particles of one substance into another on their own", "first antibiotic obtained from a mould", "force that opposes motion"],
       ["a–ii", "b–i", "c–v", "d–iii", "e–iv"]),
 OR(sa("(a) Describe an activity to show that a current-carrying wire deflects a magnetic compass needle. (3)<br>(b) What happens to the deflection when the direction of the current is reversed? (2)", 5, "(a) Place a compass below a straight wire lying along the N–S direction (1). Connect wire to a cell through a switch and close the circuit (1). Needle deflects from N–S, showing a current produces a magnetic effect (Oersted) (1). (b) Deflection reverses direction (1) and the magnitude depends on current strength (1).", fig=F.compass_wire()),
    sa("(a) Distinguish between mass and weight (any three points). (3)<br>(b) A body has mass 5 kg. Find its weight on Earth (g = 10 m/s²). (2)", 5, "(a) Mass: amount of matter, SI unit kg, constant everywhere, scalar. Weight: force of gravity on the body, SI unit newton, changes with place, acts towards centre of the Earth. (any three, 1 each) (b) W = mg = 5 × 10 = 50 N (2).")),
]
E = [
 c4("In Class VIII many students of Meena's class came to school with cough, running nose and fever. The teacher told them to stay at home, rest and drink plenty of fluids, and informed that the disease spreads from person to person.",
    ("Name the type of disease that spreads from one person to another.", "Communicable (infectious) disease."),
    ("Name one way through which such a disease can spread.", "Through droplets from coughing/sneezing, contaminated surfaces or direct contact (any one)."),
    ("Suggest two precautions to prevent the spread of this disease in the class.", "Cover mouth and nose when sneezing/coughing; wash hands; keep distance from the ill; stay at home when sick (any two)."),
    ("Why will an antibiotic tablet not cure this illness if it is caused by a virus?", "Antibiotics act on bacteria; viruses lack the cell machinery that antibiotics target, so they are not affected.")),
 c4("In the school science club, Arjun wound 40 turns of insulated copper wire around an iron nail and connected the ends to a 3 V cell through a switch. The nail picked up a few iron pins when the switch was closed.", 
    ("What type of magnet was formed?", "A temporary electromagnet."),
    ("What happens to the pins when the switch is opened?", "They fall because the nail loses its magnetism."),
    ("State any two ways by which Arjun can make the nail pick up more pins.", "Increase the number of turns; add more cells in series (increase current); use a thicker soft iron core (any two)."),
    ("Why is insulated wire used to make the coil?", "So that current passes through each turn of the coil (does not short-circuit through the nail or neighbouring turns), producing a strong field."),),
 c4("On a hot summer evening dark clouds gathered, strong winds blew and a thunderstorm with lightning occurred. Roof sheets of a few houses were blown off.",
    ("What causes lightning?", "Discharge of electric charges between clouds or between cloud and ground."),
    ("Why do high-speed winds blow off roofs?", "High-speed wind lowers the air pressure above the roof; the higher pressure inside pushes the roof upwards."),
    ("Mention two safety measures one should follow during a thunderstorm.", "Stay indoors; avoid standing under trees/open fields; do not use electrical appliances/telephones; keep away from water (any two)."),
    ("Why is it unsafe to stand under a tall tree during lightning?", "A tall tree is a good path to the ground for charge; lightning may strike it and the person standing nearby can be hurt.")),
 c4("A cricket ball rolled on a smooth cement pitch stopped after travelling 30 m. When the same ball was rolled with the same push on a grass field, it stopped after only 12 m.",
    ("Name the force that stops the ball.", "Friction."),
    ("Is friction a contact force or a non-contact force?", "Contact force."),
    ("Why does the ball stop earlier on grass than on cement?", "Grass is rougher, so friction is greater and the ball loses its speed sooner."),
    ("Mention two ways in which friction can be reduced.", "Use lubricants (oil/grease), ball bearings/wheels, make surfaces smoother, streamlining (any two).")),
]
make(1, 'Term I · Chapters 1–7', A, B, C, D, E, 'Set_01')
