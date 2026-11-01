from h8 import *
A = [
 mc("Which of the following is a mixture?", "Sea water", ["Distilled water", "Iron", "Carbon dioxide"], "Sea water has salts dissolved in water."),
 mc("The solvent in a solution of sugar in water is:", "water", ["sugar", "both", "none of these"], "The substance present in larger amount that dissolves the solute."),
 mc("The image of an object kept in front of a plane mirror is formed:", "behind the mirror at the same distance as the object", ["on the mirror", "in front of the mirror at half the distance", "at infinity"], "Plane mirror image distance equals object distance."),
 mc("In a food chain, grass → grasshopper → frog → snake, the secondary consumer is the:", "frog", ["grass", "grasshopper", "snake"], "Grasshopper is primary, frog is secondary, snake tertiary."),
 mc("In the food web shown, the hawk gets energy directly from:", "snake", ["grass", "mouse", "frog"], "Arrow from snake to hawk shows energy flow.", fig=F.food_web()),
 mc("Which organisms break down dead plants and animals and return nutrients to the soil?", "Decomposers", ["Producers", "Herbivores", "Carnivores"], "Fungi and bacteria are decomposers."),
 mc("If all frogs in the food web disappear, which effect is MOST likely?", "Grasshopper numbers rise and snake feeds more on mice", ["Grass numbers rise, grasshoppers fall", "Hawks multiply rapidly", "Nothing changes"], "Fewer predators for grasshopper; snake shifts to mice."),
 mc("In the figure, the layer labelled A is the:", "crust", ["mantle", "outer core", "inner core"], "The outermost thin solid layer of the Earth is the crust.", fig=F.earth_layers()),
 mc("Which layer of the atmosphere contains the ozone layer that absorbs harmful ultraviolet rays?", "Stratosphere", ["Troposphere", "Mesosphere", "Exosphere"], "Ozone is in the stratosphere."),
 mc("Seasons on the Earth are caused mainly by:", "the tilt of the Earth's axis as it revolves around the Sun", ["distance of Earth from the Moon", "rotation of the Earth", "phases of the Moon"], "Tilted axis + revolution = changing day length and sunlight angle."),
 mc("The Moon takes about ______ to complete one phase cycle from one new moon to the next.", "29.5 days", ["7 days", "15 days", "365 days"], "Synodic month ≈ 29.5 days."),
 mc("A simple pendulum completes 20 oscillations in 40 s. Its time period is:", "2 s", ["0.5 s", "20 s", "800 s"], "T = 40/20 = 2 s."),
]
B = [
 OR(sa("What is a food chain? Give an example of a food chain with three organisms.", 2, "A sequence of organisms in which each is eaten by the next, showing flow of energy (1). Grass → grasshopper → frog (1)."),
    sa("Define producer and consumer with an example each.", 2, "Producers make their own food by photosynthesis, e.g., green plants (1); consumers depend on others for food, e.g., cow/lion (1).")),
 sa("Name the four spheres of the Earth.", 2, "Lithosphere, hydrosphere, atmosphere and biosphere (½ each)."),
 sa("What is meant by the time period of a pendulum? Give its SI unit.", 2, "Time taken for one complete oscillation (1); second (1)."),
 sa("Why is the Moon visible although it does not produce light?", 2, "Moon reflects sunlight (1) that falls on it, and this reflected light reaches our eyes (1)."),
]
C = [
 OR(sa("How do decomposers help in the ecosystem? Give two examples.", 3, "Break down dead organisms and wastes into simple substances which are returned to soil and absorbed by plants (2). Fungi, bacteria (1)."),
    sa("Explain why cutting of forests disturbs the balance of an ecosystem. Give two points.", 3, "Loss of habitat and food for animals; fewer producers; soil erosion; less rainfall; more carbon dioxide (any three points – 1 each).")),
 sa("Distinguish between rotation and revolution of the Earth and state one result of each.", 3, "Rotation: spinning on axis in 24 h – day and night (1½). Revolution: movement around the Sun in 365¼ days – seasons/year (1½)."),
 OR(sa("What are the four layers of the Earth? Arrange them from the surface to the centre.", 3, "Crust, mantle, outer core, inner core (3 for correct order)."),
    sa("Describe the water cycle in three steps.", 3, "Evaporation of water from water bodies/transpiration; condensation into clouds; precipitation (rain/snow); run-off collects in rivers and seas (1 each, any three).")),
]
D = [
 fill(["Ecosystem", "Biosphere", "Lunar", "Producers", "Pendulum"],
      ["Green plants are ________ because they make their own food.", "A community of living organisms together with its non-living surroundings is an ________.", "A ________ month is based on phases of the Moon.", "The ________ is the zone of the Earth where life exists.", "A ________ swings to and fro and can be used to measure small intervals of time."],
      ["Producers", "Ecosystem", "Lunar", "Biosphere", "Pendulum"]),
 match(["Crust", "Troposphere", "Producer", "Full moon", "Pendulum"],
       ["lowest layer of the atmosphere with weather", "outermost layer of the Earth", "uses sunlight to make food", "Moon's whole face is lit as seen from Earth", "bob that oscillates to and fro", "fixed star"],
       ["a–ii", "b–i", "c–iii", "d–iv", "e–v"]),
 OR(sa("(a) With a diagram, show the food web of five organisms and name one herbivore. (3)<br>(b) What will happen to the grasshoppers if the frogs are removed? (2)", 5, "(a) Any valid food web, e.g., grass → grasshopper → frog → snake; grass → mouse → snake; herbivore: grasshopper/mouse (3). (b) Grasshoppers increase due to fewer predators; they would damage the grass (2).", fig=F.food_web()),
    sa("(a) Explain how the tilt of the Earth's axis causes unequal day and night (3)<br>(b) Why is summer hotter than winter in the same place? (2)", 5, "(a) Axis tilted 23.5° so different parts face the Sun differently during revolution; days longer in the hemisphere tilted towards the Sun (3). (b) In summer, Sun's rays fall more directly and daylight is longer, giving more heat (2).")),
]
E = [
 c4("A pond has water plants, small fish, large fish, frogs, insects, and bacteria at the bottom. A farmer sprays heavy pesticide near it and many small fish die.",
    ("Name the producers in the pond.", "Water plants (algae)."),
    ("Which organisms act as decomposers?", "Bacteria (and fungi)."),
    ("What will happen to the number of large fish if the small fish decrease?", "They will decrease due to lack of food."),
    ("Suggest two ways to protect this ecosystem.", "Reduce pesticide use; prevent dumping waste; plant trees; regulate fishing (any two).")),
 c4("Arjun made a pendulum using a string of 1 m and a stone. He counted 10 oscillations in 20 s. Then he shortened the string to 0.5 m.",
    ("What is the time period of the first pendulum?", "2 s."),
    ("What is the frequency of the first pendulum?", "0.5 Hz (1/T)."),
    ("What will happen to the time period when the string is shortened?", "Decreases."),
    ("Why can pendulum clocks be used to measure time?", "Each oscillation takes the same time (regular period) for a fixed length.")),
 c4("The diagram of the Moon shows four positions P, Q, R and S in a month. At P no part of the Moon facing Earth is lit and at R the whole face is lit.",
    ("Name the phase at P.", "New moon."),
    ("Name the phase at R.", "Full moon."),
    ("Why do we see different phases of the Moon?", "Moon revolves around Earth, and we see different parts of its sunlit half from Earth."),
    ("Why do we always see the same face of the Moon from the Earth?", "Moon rotates once on its axis in the same time it takes to revolve once around Earth."),
    fig=F.moon_phase_row()),
 c4("In a hill area, a farmer cuts trees on the slopes. In the next rainy season, rain washes soil downhill, springs dry up and many birds disappear.",
    ("Which sphere of the Earth is directly disturbed by cutting trees?", "Biosphere (and lithosphere)."),
    ("What is soil erosion?", "Removal of the top layer of soil by wind or water."),
    ("Explain how forest loss affects the water cycle.", "Less transpiration means fewer clouds/ rainfall; less infiltration so springs dry up."),
    ("Suggest two actions to restore the hill ecosystem.", "Plant trees; terrace farming; stop overgrazing; avoid cutting (any two).")),
]
make(5, 'Term II · Chapters 8–13', A, B, C, D, E, 'Set_05')
