"""Class 9 Science Ch 2 Exploring Mixtures and Their Separation - extras."""
from common import AR4, Q

AR = [
 AR4("A mixture of salt and sand can be separated by dissolving it in water, filtering and evaporating the filtrate.", "Sand is insoluble in water, whereas salt is soluble in water.", "a",
     "Sand stays on the filter paper while the salt solution passes through; the difference in solubility explains the method."),
 AR4("Fractional distillation is used to separate two miscible liquids whose boiling points differ by less than 25 K.", "Simple distillation can separate a volatile liquid from a non-volatile dissolved solid.", "b",
     "Both are true statements, but R does not explain why a fractionating column is needed in A."),
 AR4("A suspension is a heterogeneous mixture.", "The particles of a suspension do not settle down when the mixture is left undisturbed.", "c",
     "Suspension particles are large and settle on standing, so R is false."),
 AR4("A true solution scatters a beam of light passing through it.", "The solute particles of a true solution are very small (diameter less than 1 nm).", "d",
     "Particles of a true solution are too small to scatter light, so A is false; R is true."),
 AR4("Paper chromatography can separate the different dyes present in black ink.", "Different dyes have different solubilities in the solvent and are carried to different heights on the paper.", "a",
     "The more soluble dye moves farther up the paper, which is what separates the dyes."),
 AR4("Air is a homogeneous mixture of gases.", "Nitrogen forms about 78 per cent of air by volume.", "b",
     "Both statements are true; the percentage of nitrogen does not explain why air is homogeneous."),
]

CASE = [
 Q("<b>Case study.</b> A student in Pune dissolves 20 g of common salt in 180 g of water to prepare a solution for an experiment. "
   "(i) Name the solute and the solvent. (ii) Find the mass of the solution. (iii) Find the mass percentage of salt in the solution. (iv) How much more water must be added to this solution to make a 5 per cent (by mass) solution?",
   r"(i) Solute: salt; solvent: water (1). (ii) $20+180=200$ g (1). (iii) $\dfrac{20}{200}\times100=10\%$ (1). (iv) For 5 per cent, total mass $=\dfrac{20}{0.05}=400$ g (1); water to be added $=400-200=200$ g (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In the salt pans of Gujarat, sea water is let into shallow fields and left in the sunshine. After many days white crystals of salt are collected. The crude salt is later dissolved in water, filtered and crystallised again to make it purer. "
   "(i) Name the process by which water is removed in the salt pans. (ii) Why can salt not be separated from sea water by filtration? (iii) Name the method used to purify the crude salt crystals. (iv) Why is sunshine used for evaporation instead of boiling the water to dryness?",
   "(i) Evaporation (1). (ii) Salt is dissolved in the water as very small particles and passes through the filter paper (1). (iii) Crystallisation (recrystallisation) (1). (iv) Sunlight is free and gives slow evaporation, so crystals of salt form (1); boiling to dryness would waste fuel and leave the impurities mixed with the salt (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A dairy in Anand separates cream from milk using a machine that spins the milk at high speed. The lighter cream collects near the centre while the heavier skimmed milk moves to the outside. "
   "(i) Name the separation method used. (ii) Which component of milk is lighter? (iii) Give one other use of this method. (iv) Explain the principle on which the method works.",
   "(i) Centrifugation (1). (ii) Cream (1). (iii) Any one: separating blood cells from plasma, separating butter from curd or cream, drying clothes in a washing machine (1). (iv) The spinning produces a strong outward force (1); denser particles are thrown to the bottom or outside while lighter particles stay near the centre (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Matter and mixtures", ["Pure substance: single kind of particle, fixed composition and fixed melting/boiling point (elements and compounds).",
   "Mixture: two or more substances mixed in any proportion; components keep their properties.",
   "Homogeneous mixture (solution, e.g. brass, air): uniform composition. Heterogeneous mixture (e.g. sand and iron filings): visibly different parts."]),
 ("Solutions, colloids, suspensions", ["Solution: solute particles $<1$ nm, do not scatter light, do not settle, pass through filter paper.",
   "Colloid (e.g. milk, fog): particles 1 to 1000 nm, scatter light (Tyndall effect), do not settle, not separated by filtration.",
   "Suspension (e.g. muddy water): particles $>1000$ nm, scatter or block light, settle on standing, separated by filtration."]),
 ("Concentration", ["Mass per cent $=\\dfrac{\\text{mass of solute}}{\\text{mass of solution}}\\times100$, where mass of solution = mass of solute + mass of solvent.",
   "Volume per cent $=\\dfrac{\\text{volume of solute}}{\\text{volume of solution}}\\times100$.",
   "Saturated solution: cannot dissolve more solute at that temperature. Solubility of most solids increases with temperature; of gases decreases."]),
 ("Separation methods and principle", ["Filtration: insoluble solid from liquid. Evaporation: dissolved solid from solvent. Crystallisation: pure crystals of a dissolved solid.",
   "Simple distillation: liquid from a non-volatile solute. Fractional distillation: miscible liquids with boiling points differing by $<25$ K.",
   "Separating funnel: immiscible liquids. Centrifugation: denser particles settle (cream from milk). Chromatography: differing solubilities (dyes in ink).",
   "Sublimation: e.g. ammonium chloride, camphor from a non-subliming solid. Magnetic separation: iron from sulphur or sand."]),
 ("Dilution", ["Mass of solute is unchanged on dilution: $\\text{per cent}_1\\times\\text{mass}_1=\\text{per cent}_2\\times\\text{mass}_2$."]),
]

MISTAKES = [
 "Calculating mass per cent using the mass of the <i>solvent</i> instead of the mass of the <i>solution</i> (solute + solvent).",
 "Saying that a clear liquid must be a pure substance; a clear solution such as salt water is a mixture.",
 "Using filtration to separate a dissolved solid; filtration works only for insoluble particles, not for a solute.",
 "Confusing evaporation (solvent lost, solid left) with distillation (solvent collected by condensing); and using fractional distillation when the boiling points differ by more than 25 K.",
 "Thinking that the solubility of a gas also increases when the temperature rises; the solubility of gases in water decreases.",
 "Forgetting that a colloid does not settle and cannot be filtered, but still shows the Tyndall effect.",
]
