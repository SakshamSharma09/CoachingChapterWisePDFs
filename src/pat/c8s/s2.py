from h8 import *
A = [
 mc("Anita collects a drop of pond water to look for tiny living organisms. Which instrument must she use?", "Compound microscope", ["Magnifying glass only", "Telescope", "Binoculars"], "Microorganisms are too small to see with the unaided eye."),
 mc("Which cell organelle is present in plant cells but absent in animal cells?", "Chloroplast", ["Nucleus", "Mitochondria", "Cytoplasm"], "Chloroplasts contain chlorophyll for photosynthesis."),
 mc("A child eating only polished rice develops swollen gums that bleed. The deficiency is most likely of:", "Vitamin C", ["Vitamin A", "Calcium", "Iron"], "Scurvy – bleeding gums – is caused by lack of vitamin C."),
 mc("Which of the following is a non-communicable disease?", "Diabetes", ["Typhoid", "Malaria", "Dengue"], "Diabetes does not spread from person to person."),
 mc("The energy conversion taking place in an electric heater is:", "electrical energy to heat energy", ["heat energy to electrical energy", "chemical energy to light energy", "electrical energy to sound energy"], "The heating element converts electrical energy into heat."),
 mc("The magnetic field around a straight current-carrying wire can be detected using:", "a magnetic compass", ["a thermometer", "a voltmeter only", "a lens"], "A compass needle deflects near the wire."),
 mc("Two equal forces act on a body in opposite directions along the same line. The net force on the body is:", "zero", ["double of one force", "equal to one force", "cannot be determined"], "Equal and opposite forces cancel."),
 mc("Which of these forces acts on a body without any contact?", "Gravitational force", ["Muscular force", "Frictional force", "Force of a push"], "Gravity acts at a distance."),
 mc("A drinking straw lets us sip a cold drink because:", "atmospheric pressure pushes the liquid up when pressure inside the straw is reduced", ["liquid is lighter than air", "the straw pulls the liquid", "liquid has no weight"], "Lower pressure in the straw; higher atmospheric pressure pushes liquid up."),
 mc("A tropical cyclone has at its centre:", "a calm region of very low pressure called the eye", ["a region of very high pressure", "strong sunshine and no winds", "a mountain"], "Eye: low pressure, calm."),
 mc("Gases can be compressed easily because:", "there is a large space between their particles", ["their particles are very heavy", "they have fixed shape", "their particles attract strongly"], "Large inter-particle space."),
 mc("When ice melts to form water, the particles:", "gain energy and the arrangement becomes less rigid", ["lose all their energy", "stop moving", "become heavier"], "Heating increases particle energy and weakens the rigid arrangement."),
]
B = [
 OR(sa("State any two functions of the cell membrane.", 2, "It encloses/protects the cell contents and gives shape (animal cell) (1); it controls entry and exit of substances (1)."),
    sa("Write any two differences between a plant cell and an animal cell.", 2, "Plant cell: has cell wall, chloroplasts, large vacuole, fixed shape. Animal cell: no cell wall/chloroplast, small vacuoles, irregular shape. (any two, 1 each)")),
 sa("Mention two benefits of vaccination.", 2, "Protects against specific diseases by building immunity (1); prevents spread of disease in the community / can eradicate diseases like smallpox (1)."),
 sa("What is the heating effect of electric current? Name one appliance based on it.", 2, "When current flows through a conductor of high resistance it produces heat (1). Examples: electric iron, heater, toaster, geyser (any one) (1)."),
 sa("Camels have broad, flat feet. How does this help them walk on soft desert sand?", 2, "Broad feet have a large area (1); pressure = force/area becomes small so the feet do not sink into the sand (1)."),
]
C = [
 OR(sa("Name the disease caused by the dengue virus, state any two symptoms and one preventive measure.", 3, "Dengue (1). Symptoms: high fever, severe headache, joint/muscle pain, rash (any two) (1). Prevention: avoid stagnant water so mosquitoes cannot breed; use nets/repellents (1)."),
    sa("Describe three habits of personal hygiene that help us stay healthy.", 3, "Washing hands with soap before eating and after using toilet; bathing daily, brushing teeth; keeping nails short and clothes clean; covering mouth when sneezing (any three, 1 each).")),
 sa("Explain why the filament of an electric bulb glows while the copper connecting wires do not.", 3, "The filament is a thin wire of tungsten with high resistance and high melting point (1). The same current produces more heat in it (1), so it becomes white hot and glows, whereas the thick copper wires have low resistance and stay cool (1)."),
 OR(sa("Two forces of 8 N and 5 N act on a block along the same straight line in opposite directions as shown. Find the net force and its direction. Is the force balanced?", 3, "Net force = 8 − 5 = 3 N (1) in the direction of the larger force (to the right) (1). Forces are unbalanced, so the block accelerates (1).", fig=F.block_forces((5, '5 N'), (8, '8 N'))),
    sa("What are balanced and unbalanced forces? Give one effect of an unbalanced force.", 3, "Balanced: equal and opposite forces giving zero net force (1). Unbalanced: net force not zero (1). Effect: changes speed/direction/shape or starts motion (1).")),
]
D = [
 fill(["Nucleus", "Chloroplast", "Cell wall", "Cyclone", "Fuse"],
      ["The ________ is the control centre of the cell.", "________ contains chlorophyll and traps sunlight for photosynthesis.", "A ________ is a safety device that melts and breaks the circuit when excess current flows.", "A ________ is a system of rapidly rotating winds around a low-pressure centre.", "The ________ gives a plant cell its rigid shape."],
      ["Nucleus", "Chloroplast", "Fuse", "Cyclone", "Cell wall"]),
 match(["Zinc container", "Lactobacillus", "Newton", "Gas", "Pascal"],
       ["negative terminal of a dry cell", "bacterium that turns milk into curd", "SI unit of force", "no definite shape and no definite volume", "SI unit of pressure", "force of attraction towards the Earth"],
       ["a–i", "b–ii", "c–iii", "d–iv", "e–v"]),
 OR(sa("The figure shows the particle arrangement of three states of matter P, Q and R.<br>(a) Identify P, Q and R and state which has the maximum inter-particle space. (3)<br>(b) Which one can be compressed easily and why? (2)", 5, "(a) P – solid, Q – liquid, R – gas (1½); R has maximum space (1½). (b) R (gas) (1) because of large spaces between particles (1).", fig=F.three_states()),
    sa("(a) Explain how a drinking straw works. (3)<br>(b) Why do we not feel the huge atmospheric pressure acting on our body? (2)", 5, "(a) Sucking lowers the air pressure inside the straw (1); atmospheric pressure on the liquid surface is higher (1) and pushes the liquid up the straw (1). (b) The pressure inside our body balances the outside pressure (1), so there is no net force felt (1).")),
]
E = [
 c4("Priya, a Class VIII student, often has bleeding gums and pain in the joints. The doctor advised her to include citrus fruits, tomatoes and green vegetables in her diet.",
    ("Deficiency of which vitamin is the likely cause?", "Vitamin C."),
    ("Name the deficiency disease caused by this vitamin deficiency.", "Scurvy."),
    ("Name two food items rich in this vitamin.", "Orange, lemon, amla, guava, tomato (any two)."),
    ("Why is a balanced diet important for adolescents?", "Provides all nutrients in proper amount for growth, energy, immunity and repair during rapid growth of adolescence.")),
 c4("After Rohan plugged a heater, an iron and a geyser into the same socket, the electric fuse of his house blew out and all lights went off.",
    ("Why did the fuse wire melt?", "Excess current heated the fuse wire above its melting point."),
    ("What is this situation of too many appliances in one socket called?", "Overloading."),
    ("State two precautions to avoid such accidents.", "Do not overload sockets; use correct rating fuse/MCB; avoid damaged wires; use earthing (any two)."),
    ("State one difference between a fuse and an MCB.", "A fuse wire melts and must be replaced; an MCB trips off and can be reset by switching on again.")),
 c4("In May 2019, Cyclone Fani crossed the coast of Odisha with winds of about 175 km/h. Early warnings from the weather department helped authorities shift lakhs of people to cyclone shelters in time.",
    ("Over which type of region do tropical cyclones form?", "Warm ocean waters."),
    ("What is the central calm part of a cyclone called?", "Eye."),
    ("Why do cyclones weaken after reaching land?", "They lose their supply of warm moist air/ energy from the ocean and friction with land slows the winds."),
    ("How do early warnings reduce loss of life?", "People can be evacuated to shelters, supplies arranged and fishermen stopped from going to sea.")),
 c4("In a tug-of-war, both teams pull the rope with a force of 500 N in opposite directions and the rope does not move.",
    ("What is the net force on the rope?", "Zero."),
    ("Are the forces balanced or unbalanced?", "Balanced."),
    ("What will happen to the rope if one team pulls with 600 N and the other with 500 N? Find the net force.", "Net force = 100 N towards the stronger team; the rope accelerates in that direction."),
    ("Give one example of balanced forces in daily life.", "A book resting on a table (weight balanced by normal reaction); a hanging lamp.")),
]
make(2, 'Term I · Chapters 1–7', A, B, C, D, E, 'Set_02')
