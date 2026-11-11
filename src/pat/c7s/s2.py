from h8 import *
import figs7 as F7
CIRC = F7.circuit(('A', 'B', 'C', 'D'))
REFL = F7.reflection(35, 'i', 'r')
assert 72*5/18 == 20 and 54*5/18 == 15 and 40/20 == 2 and 35+35 == 70 and 90-35 == 55
assert 200/80 == 2.5 and 90*5/18 == 25
A = [
 mc("Which of the following substances turns blue litmus paper red?", "Vinegar", ["Soap solution", "Baking soda solution", "Lime water"], "Vinegar contains acetic acid, and acids turn blue litmus red."),
 mc("In an LED, the longer leg is connected to the:", "positive terminal of the cell", ["negative terminal of the cell", "switch only", "either terminal; it does not matter"], "An LED allows current in one direction only; the longer leg is the positive terminal."),
 mc("A metal that gives a ringing sound when struck is called:", "sonorous", ["malleable", "ductile", "brittle"], "Metals produce a ringing sound — they are sonorous."),
 mc("Which of the following changes can be reversed easily?", "Melting of ice", ["Burning of paper", "Ripening of a mango", "Rusting of iron"], "Melting of ice is a physical change; water can be frozen back to ice."),
 mc("Deficiency of iodine in the diet may cause the enlargement of which gland, called goitre?", "Thyroid", ["Pancreas", "Pituitary", "Adrenal"], "Thyroid needs iodine to make its hormone; this is why iodised salt is advised."),
 mc("The range of a clinical thermometer is:", "35 °C to 42 °C", ["−10 °C to 110 °C", "0 °C to 100 °C", "20 °C to 60 °C"], "A clinical thermometer measures human body temperature, so its range is 35–42 °C."),
 mc("A bike moves at 72 km/h. Its speed in m/s is:", "20 m/s", ["72 m/s", "15 m/s", "25 m/s"], "1 km/h = 5/18 m/s, so 72 × 5/18 = 20 m/s."),
 mc("Which organs of the human body remove nitrogenous wastes from the blood?", "Kidneys", ["Lungs", "Liver only", "Stomach"], "Kidneys filter blood and form urine."),
 mc("Water and minerals taken up by roots are carried to the leaves through the:", "xylem", ["phloem", "stomata", "cuticle"], "Xylem conducts water and minerals upwards; phloem carries food."),
 mc("A ray of light strikes a plane mirror at an angle of incidence of 35°. The angle of reflection is:", "35°", ["55°", "70°", "145°"], "Law of reflection: angle of incidence = angle of reflection."),
 mc("The Earth takes about 365¼ days to complete one revolution around the Sun. To adjust for the ¼ day, a leap year of ___ days is added once in four years.", "366", ["364", "365", "367"], "Four quarter days add up to one extra day, which is added to February."),
 mc("A simple pendulum completes 20 oscillations in 40 s. Its time period is:", "2 s", ["20 s", "0.5 s", "60 s"], "Time period = 40 s ÷ 20 = 2 s."),
]
B = [
 sa("Ritu connected a cell, a bulb and a switch in a circuit but the bulb did not glow even after she closed the switch. Give any two possible reasons.", 2, "(Any two, 1 each) The cell may be dead; a loose/broken connecting wire; the bulb's filament has fused; the bulb is not fixed properly in the holder; wrong polarity of an LED."),
 sa("Why does an antacid tablet give relief from acidity (indigestion)? Name the type of substance it contains.", 2, "Excess acid in the stomach causes indigestion (1). Antacids contain a base (e.g. magnesium hydroxide, milk of magnesia) that neutralises the acid (1)."),
 OR(sa("Convert the speed 54 km/h to m/s. How long will a bus moving at this speed take to travel 300 m?", 2, "54 × 5/18 = 15 m/s (1); time = 300 ÷ 15 = 20 s (1)"),
    sa("Define the time period of a simple pendulum. Mention two ways in which the time period can be found more accurately.", 2, "Time period is the time taken for one complete oscillation (1). Measure the time for 20 or more oscillations and divide by the number; repeat and average (1).")),
 sa("Explain with an activity or a daily-life example how a shadow is formed. Why is a shadow darker than its surroundings?", 2, "Light travels in straight lines; an opaque object blocks the light and a dark region (shadow) forms behind it (1). Light does not reach that region, so it is darker (1)."),
]
C = [
 sa("Compare a plane mirror, a concave mirror and a convex mirror by giving one use of each.", 3, "Plane mirror — dressing table / bathroom mirror, periscope (1). Concave mirror — torch/headlight reflector, shaving mirror, dentist's mirror (1). Convex mirror — rear-view mirror of vehicles, shop security mirror (1)."),
 OR(sa("Explain why we have different seasons on the Earth. Why does the length of day vary?", 3, "The Earth's axis is tilted by about 23.5° to its orbit (1). As the Earth revolves round the Sun, different hemispheres tilt towards or away from the Sun and receive more or less direct sunlight (1). So days are longer in summer and shorter in winter (1)."),
    sa("Distinguish between a solar eclipse and a lunar eclipse (any three points).", 3, "Solar: Moon comes between Sun and Earth, on a new moon day, Moon's shadow falls on Earth, seen only from some places. Lunar: Earth comes between Sun and Moon on a full moon day, Earth's shadow falls on Moon, visible from the whole night side of Earth (any three, 1 each).")),
 sa("Explain the formation of a sea breeze. Why does it blow during the day?", 3, "During the day the land heats up faster than the sea (1). Warm air above the land rises (1) and cooler air from the sea moves in to take its place, giving the sea breeze (1)."),
]
D = [
 OR(sa("Study the circuit shown. (i) Name the parts A, B, C and D. (ii) Will the bulb glow? Give a reason. (iii) What should be done to make it glow?", 5, "(i) A — electric cell; B — bulb; C — switch (open); D — connecting wire (2 marks, ½ each)<br>(ii) No, because the switch is open and the circuit is incomplete (1.5)<br>(iii) Close the switch to complete the circuit (1.5)", fig=CIRC),
    sa("(i) How does the heating effect of current help in an electric geyser? (ii) Why is the wire in a geyser made of nichrome? (iii) Why should we not touch bare electric wires? (iv) Differentiate between a conductor and an insulator with two examples each.", 5, "(i) Current passing through a high-resistance coil produces heat which warms the water (1)<br>(ii) High resistance and high melting point (1)<br>(iii) The body conducts electricity and we may get a shock (1)<br>(iv) Conductors allow current, e.g. copper, aluminium; insulators do not, e.g. rubber, plastic, wood (2)")),
 sa("The figure shows a ray striking a plane mirror. (i) Name the normal and mark the angles i and r. (ii) Find the angle of reflection if the angle of incidence is 35°. (iii) What is the angle between the incident ray and the reflected ray? (iv) What is the angle between the incident ray and the mirror surface? (v) State the second law of reflection.", 5, "(i) The dotted line N perpendicular to the mirror at O (1)<br>(ii) 35° (1)<br>(iii) 35° + 35° = 70° (1)<br>(iv) 90° − 35° = 55° (1)<br>(v) The incident ray, the reflected ray and the normal lie in the same plane (1)", fig=REFL),
 OR(sa("(a) Explain the phases of the Moon. (3)<br>(b) How many days does the Moon take to complete one cycle of phases (new moon to new moon)? (1)<br>(c) Name the phase when the whole of the Moon's lit side faces the Earth. (1)", 5, "(a) The Moon does not emit light; it reflects sunlight. As it revolves around the Earth, we see different portions of the lit half — crescent, quarter, gibbous, full — then they wane back to new moon (3)<br>(b) About 29.5 days (1)<br>(c) Full moon (1)"),
    sa("A train 200 m long moving at 90 km/h crosses a pole. (i) Express its speed in m/s. (ii) Find the time taken to cross the pole. (iii) A motorist travels 200 km at 80 km/h; find the time taken. (iv) What is the formula for speed? (v) Give two units of speed.", 5, "(i) 90 × 5/18 = 25 m/s (1)<br>(ii) 200 ÷ 25 = 8 s (1)<br>(iii) 200 ÷ 80 = 2.5 h (1)<br>(iv) Speed = distance ÷ time (1)<br>(v) m/s and km/h (1)")),
]
E = [
 c4("Aman's mother notices that the lights flicker whenever the geyser, iron and air-conditioner are switched on together in their house. The electrician says that the circuit is overloaded and advises installing an MCB.",
    ("Which effect of electric current is used in an electric iron?", "Heating effect."),
    ("Why does an overloaded circuit become dangerous?", "Too much current flows and the wires heat up; this may cause a fire."),
    ("How does an MCB protect the house wiring?", "It automatically trips (switches off) when the current exceeds a safe limit and can be reset; unlike a fuse it need not be replaced."),
    ("Mention two safety rules while using electrical appliances.", "Do not touch with wet hands; use proper earthing/insulated plugs; do not overload sockets; switch off before repair; use ISI-marked appliances (any two).")),
 c4("In winter Nisha wears a woollen sweater and feels warm. At home she notes that the metal spoon in a hot cup of tea quickly becomes too hot to hold, while a wooden spoon does not.",
    ("Which mode of heat transfer heats the metal spoon?", "Conduction."),
    ("Name one good and one poor conductor of heat from the passage.", "Good: metal (spoon); poor: wood (spoon) / wool."),
    ("Why does a woollen sweater keep us warm?", "Wool is a poor conductor and traps air between its fibres; this reduces the loss of body heat."),
    ("Why do we wear white or light-coloured clothes in summer?", "Light colours reflect most of the heat radiated by the Sun.")),
 c4("A rusted iron gate was painted by a painter. Another gate, made by a fabricator, was coated with zinc (galvanised). After two rainy seasons, the painted gate has again shown rust at some scratched places, but the galvanised gate remained shiny.",
    ("Name the two substances necessary for rusting.", "Oxygen (air) and moisture."),
    ("Is rusting a physical or a chemical change?", "Chemical change (a new substance, iron oxide, forms)."),
    ("Why did the painted gate rust at scratched places?", "Scratches expose the iron to air and moisture because the protective layer of paint has been removed."),
    ("Name another method of preventing rusting and one metal that does not rust easily.", "Oiling/greasing, alloying (stainless steel); gold, platinum, aluminium (forms a protective oxide layer) — any correct one each.")),
 c4("After a meal, a cow's food travels through its digestive tract while the farmer's blood carries oxygen to every cell. Anita learns in class that animals take food, digest it, take in oxygen and send out wastes.",
    ("Name the organ in humans where most of the water from undigested food is absorbed.", "Large intestine."),
    ("Which blood vessels carry blood away from the heart?", "Arteries."),
    ("Explain the role of the kidneys in the human body.", "Kidneys filter blood, remove nitrogenous waste (urea) and excess water and salts as urine; they help to keep water balance."),
    ("Name the part through which the earthworm and frog partly breathe.", "Skin (moist skin).")),
]
make(2, 'Set 02 · Emphasis: Physical Science – Electricity, Heat, Motion, Light, Earth-Moon-Sun', A, B, C, D, E, 'Set_02')
