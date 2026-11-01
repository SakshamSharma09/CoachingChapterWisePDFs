from h8 import *
A = [
 mc("Which of the following is an element?", "Sulphur", ["Water", "Common salt", "Sugar"], "Sulphur has only one kind of atom; the others are compounds."),
 mc("Which of these is a property of most non-metals?", "Poor conductors of heat and electricity", ["Malleable", "Lustrous and ductile", "Sonorous"], "Non-metals (except graphite) are poor conductors and brittle in solid form."),
 mc("Which of these is a mixture?", "Air", ["Pure water", "Carbon dioxide", "Oxygen"], "Air contains nitrogen, oxygen, argon and other gases."),
 mc("Iron filings can be separated from a mixture of iron filings and sand by:", "magnetic separation", ["filtration", "evaporation", "sublimation"], "Iron is attracted by a magnet; sand is not."),
 mc("A mixture of water and kerosene oil can be best separated using:", "a separating funnel", ["a magnet", "sieving", "sublimation"], "The two liquids are immiscible and form separate layers."),
 mc("In a salt solution, salt is the:", "solute", ["solvent", "solution", "precipitate"], "The substance that dissolves is the solute."),
 mc("A solution in which no more solute can dissolve at a given temperature is called:", "saturated solution", ["dilute solution", "unsaturated solution", "suspension"], "Saturated = holds the maximum amount of solute."),
 mc("The solubility of most solids in water generally:", "increases with increase in temperature", ["decreases with temperature", "does not depend on temperature", "becomes zero on heating"], "More sugar/salt dissolves in hot water."),
 mc("The image formed by a plane mirror is:", "virtual, upright and of the same size as the object", ["real and inverted", "real and magnified", "virtual and smaller"], "Plane mirror image properties."),
 mc("A ray of light strikes a plane mirror at an angle of incidence of 35°. The angle between the incident ray and the reflected ray is:", "70°", ["35°", "55°", "110°"], "∠r = ∠i = 35°, total = 70°."),
 mc("A shaving mirror gives an enlarged, upright image. It is a:", "concave mirror", ["convex mirror", "plane mirror", "concave lens"], "A concave mirror gives magnified upright image when the object is close (within F)."),
 mc("In the figure the object is placed beyond C of a concave mirror. The image is formed:", "between F and C, real and inverted", ["behind the mirror", "at infinity", "at the pole, virtual"], "Object beyond C → image between F and C, real, inverted, diminished.", fig=F.concave_mirror()),
]
B = [
 OR(sa("Name two metals and two non-metals.", 2, "Metals: iron, copper, aluminium (any two); non-metals: sulphur, carbon, oxygen, iodine (any two) – ½ mark each."),
    sa("Why are aluminium and copper used for making cooking vessels and electric wires respectively?", 2, "Metals are good conductors of heat (1) and electricity (1); aluminium for heat, copper for electricity.")),
 sa("Differentiate between an element and a compound with one example each.", 2, "Element: one kind of atom, e.g., oxygen (1). Compound: two or more elements chemically combined in a fixed ratio, e.g., water (1)."),
 sa("What is meant by solubility? Name one factor that affects it.", 2, "Maximum amount of solute that dissolves in a given amount of solvent at a given temperature (1); temperature (1)."),
 sa("State the two laws of reflection of light.", 2, "(1) Angle of incidence = angle of reflection. (2) Incident ray, reflected ray and normal lie in the same plane."),
]
C = [
 OR(sa("Describe how you would separate a mixture of salt and sand. Name the techniques used.", 3, "Add water and stir – salt dissolves (1). Filter – sand stays on the filter paper (1). Evaporate the filtrate to get salt (1)."),
    sa("How can ammonium chloride be separated from a mixture of ammonium chloride and sand? Name the process and give the reason.", 3, "By sublimation (1); on heating ammonium chloride changes directly from solid to vapour (1) and the vapour is cooled to get solid back, sand remains (1).")),
 sa("Rohan added 10 g of sugar to 50 mL of water and stirred. Some sugar remained undissolved. What does this show? What can he do to dissolve it? Name the solute and the solvent.", 3, "Solution has become saturated (1). Heat the water or add more water (1). Sugar is solute, water is solvent (1)."),
 OR(sa("Distinguish between a concave mirror and a convex mirror on the basis of reflecting surface and one use of each.", 3, "Concave: reflecting surface curved inward; used in torches, shaving mirror, dentist's mirror. Convex: curved outward; used as rear-view mirror (1+1+1)."),
    sa("A convex lens is used as a magnifying glass. Where should the object be placed to get an enlarged image? Why is a convex lens called a converging lens?", 3, "Within the focal length (1); it brings parallel rays of light to meet at a point (the focus) (1); it bends them towards the principal axis (1).")),
]
D = [
 fill(["Sublimation", "Saturated", "Dispersion", "Lustre", "Alloy"],
      ["The shine of the surface of a metal is called ________.", "A mixture of two or more metals, or a metal and non-metal, is an ________.", "The change of a solid directly to a gas on heating is ________.", "A ________ solution cannot dissolve any more solute at that temperature.", "The splitting of white light into its colours is ________."],
      ["Lustre", "Alloy", "Sublimation", "Saturated", "Dispersion"]),
 match(["Filtration", "Distillation", "Chromatography", "Sieving", "Winnowing"],
       ["separating the components of ink or dyes", "separating insoluble solid from a liquid", "separating large from small particles", "obtaining pure water from salt water", "separating light husk from heavier grains", "separating a magnetic substance"],
       ["a–ii", "b–iv", "c–i", "d–iii", "e–v"]),
 OR(sa("(a) Differentiate between a real image and a virtual image (any three points). (3)<br>(b) Why does a concave mirror used by a dentist show an enlarged image? (2)", 5, "(a) Real: formed on screen, inverted; virtual: cannot be taken on a screen, upright (any 3 points). (b) The tooth is placed within the focal length of the concave mirror, so the image is virtual, upright and magnified (2)."),
    sa("(a) With a labelled sketch, show reflection of a ray at a plane mirror. (3)<br>(b) What is the angle of reflection if the incident ray makes 30° with the mirror? (2)", 5, "(a) Incident ray, normal, reflected ray, mirror with angles i and r equal (3). (b) Angle of incidence = 90° – 30° = 60°; angle of reflection = 60° (2).")),
]
E = [
 c4("Meena stirred some soil in a beaker of water. After standing for a while, the soil settled at the bottom and the water on top was clear. She then poured the water through filter paper.",
    ("What is the mixture of soil and water called?", "Suspension (heterogeneous mixture)."),
    ("Name the method used for separating clear water from the settled soil by pouring.", "Decantation."),
    ("Meena wants to obtain pure water from salty sea water. Which method will she use? Give the principle.", "Distillation; water evaporates and is condensed, salt remains."),
    ("Why is the filtrate of the soil-water mixture still not completely pure?", "Some dissolved substances/ soluble impurities and microorganisms may remain in the water.")),
 c4("A student measured how much of a certain salt dissolved in 100 mL water at different temperatures: 20 °C – 36 g; 40 °C – 37 g; 60 °C – 38 g; 80 °C – 40 g.",
    ("What happens to the solubility of salt as temperature rises?", "It increases slightly."),
    ("How much salt will dissolve in 100 mL of water at 60 °C?", "38 g."),
    ("A solution at 20 °C has 30 g salt in 100 mL water. Is it saturated, unsaturated or supersaturated? Why?", "Unsaturated, since 36 g can dissolve at that temperature but only 30 g is present."),
    ("Suggest one way to dissolve more sugar in a given quantity of water.", "Raise the temperature of the water.")),
 c4("Ria placed a pencil in front of three mirrors – plane, concave and convex – and observed the images. In the plane mirror the image was the same size. In the second mirror the image was larger. In the third the image was smaller.",
    ("Which mirror produced the larger image?", "Concave mirror."),
    ("Which mirror produced a smaller, upright image?", "Convex mirror."),
    ("Name one use of a convex mirror and give a reason.", "Rear-view mirror in vehicles; gives a wider field of view and an upright image."),
    ("Why does a person see lateral inversion of the letters in a plane mirror?", "The left side of the object appears as right side of the image, so the image is laterally inverted.")),
 c4("A teacher shows two samples: a shining yellowish metal rod that can be beaten into a sheet, and a dull brittle yellow solid that breaks when hammered.",
    ("What property of the first sample allows it to be beaten into sheets?", "Malleability."),
    ("Identify the second sample as a metal or a non-metal.", "Non-metal (e.g., sulphur)."),
    ("Give two more differences between metals and non-metals.", "Metals are good conductors, sonorous, lustrous; non-metals are poor conductors, non-sonorous, dull (any two)."),
    ("Name a metal that is liquid at room temperature and a non-metal that is a good conductor of electricity.", "Mercury; graphite.")),
]
make(4, 'Term II · Chapters 8–13', A, B, C, D, E, 'Set_04')
