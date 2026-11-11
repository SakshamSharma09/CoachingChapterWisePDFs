"""Class 8 Science Ch 8 Nature of Matter: Elements, Compounds and Mixtures - extras."""
from common import AR4, Q

AR = [
 AR4("Oxygen is an element.", "Oxygen contains only one kind of atom and cannot be broken down into simpler substances by chemical methods.", "a", "R is the definition of an element."),
 AR4("Metals are generally good conductors of heat and electricity.", "Metals are malleable and ductile.", "b", "Both are true, but malleability and ductility do not explain conduction."),
 AR4("Sodium is stored under kerosene.", "Sodium is a very reactive metal that reacts vigorously with air and water.", "a", "Kerosene keeps air and moisture away from sodium."),
 AR4("A mixture of iron filings and sulphur can be separated using a magnet.", "Compounds can be separated into their elements by physical methods like filtration.", "c", "A is true (iron is attracted by a magnet); R is false: compounds need chemical methods."),
 AR4("Water is a mixture of hydrogen and oxygen.", "Water has a fixed composition and properties different from those of hydrogen and oxygen.", "d", "Water is a compound, so A is false; R is true."),
 AR4("Sulphur is brittle and has no lustre.", "Non-metals are generally brittle and not shiny.", "a", "Sulphur is a typical non-metal showing these properties."),
]

CASE = [
 Q("<b>Case study.</b> Rohit has a mixture of iron filings, sand and common salt. He first passes a magnet over it. He then adds the remaining solid to water, stirs, and filters it. Finally he heats the filtrate in a china dish until all the water has gone. "
   "(i) What does the magnet remove? (ii) What is left behind on the filter paper? (iii) What remains in the china dish at the end? (iv) Name the physical methods used, and explain why this is a mixture and not a compound.",
   "(i) Iron filings (1). (ii) Sand (residue) (1). (iii) Common salt (1). (iv) Magnetic separation, filtration and evaporation (1); the substances keep their own properties and are not chemically combined, and they were separated by physical methods (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A teacher shows two samples. Sample P is a shiny, silvery strip that bends without breaking and conducts electricity. Sample Q is a yellow powder that is dull, breaks easily when crushed, and does not conduct electricity. P produces a ringing sound when struck; Q does not. "
   "(i) Which sample is a metal? (ii) Name the property of P shown by the ringing sound. (iii) Give a non-metal that is a good conductor of electricity. (iv) Sample Q is sulphur; list two more properties of Q's type of element.",
   "(i) P (1). (ii) Sonority (1). (iii) Graphite (carbon) (1). (iv) Brittle, poor conductor of heat, not lustrous, not malleable/ductile (any two) (2).", "1+1+1+2"),
 Q("<b>Case study.</b> In an activity, iron filings and sulphur powder are mixed and a magnet is passed over the mixture; the iron is pulled out. In the second part, the mixture is heated strongly in a test tube; a black solid, iron sulphide, is formed, which a magnet does not attract. "
   "(i) Is the first sample a mixture or a compound? (ii) Name the compound formed on heating. (iii) Does the magnet attract the compound? (iv) Give two differences between a mixture and a compound shown by this activity.",
   "(i) Mixture (1). (ii) Iron sulphide (1). (iii) No (1). (iv) In the mixture the components keep their properties and can be separated physically; the compound has new properties and cannot be separated by a magnet; heat/energy change occurs on forming the compound (any two) (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Classification of matter", ["Pure substances: elements and compounds. Impure: mixtures.", "Element: one kind of atom; cannot be split by chemical methods (e.g. $\\mathrm{O_2}$, Fe, Na).",
   "Compound: two or more elements chemically combined in a fixed ratio (e.g. $\\mathrm{H_2O}$, $\\mathrm{CO_2}$, NaCl).", "Mixture: two or more substances not chemically combined, in any ratio; keep their properties."]),
 ("Symbols of elements", ["Na (sodium), K (potassium), Fe (iron), Cu (copper), Ag (silver), Au (gold), Pb (lead), Hg (mercury), C, S, O, H, N."]),
 ("Metals and non-metals", ["Metals: lustrous, malleable, ductile, sonorous, good conductors of heat and electricity (mercury is liquid).", "Non-metals: dull, brittle, poor conductors (exceptions: graphite conducts; iodine is lustrous).",
   "Sodium and potassium are stored under kerosene.", "Metal oxides are generally basic; non-metal oxides are generally acidic."]),
 ("Mixtures and separation", ["Homogeneous (uniform): salt solution, air, alloys. Heterogeneous: sand and water, muddy water.", "Methods: handpicking, sieving, filtration, evaporation, magnetic separation, decantation, sedimentation.",
   "Alloys are mixtures of metals: brass (Cu + Zn), bronze (Cu + Sn)."]),
]

MISTAKES = [
 "Calling a molecule such as $\\mathrm{O_2}$ a compound; a compound needs <i>different</i> elements.",
 "Saying air or an alloy is a compound; they are mixtures.",
 "Assuming all metals are hard and solid; mercury is a liquid and sodium is soft.",
 "Writing wrong symbols (S for sodium, P for potassium); use Na and K.",
 "Using a physical method (filtration, magnet) to separate the elements of a compound.",
 "Writing that all non-metals are poor conductors; graphite is an exception.",
]
