"""Class 6 Science Ch 9 Methods of Separation in Everyday Life - extras."""
from common import AR4, Q

AR = [
 AR4("Winnowing is used to separate heavier grains from lighter husk.", "Wind blows away the lighter husk while the heavier grains fall down.", "a",
     "The difference in weight is used with wind, so R explains A."),
 AR4("A mixture of sand and water can be separated by filtration.", "Salt can be obtained from sea water by evaporation.", "b",
     "Both true, but they are different mixtures and methods; R does not explain A."),
 AR4("Salt dissolved in water can be separated by filtration.", "The particles of dissolved salt are too small and pass through filter paper.", "d",
     "A is false: filtration cannot separate a dissolved solid. R is true, which is why evaporation is used."),
 AR4("Sieving separates flour from bran.", "Sieving works because the particles are of different sizes.", "a",
     "Small flour particles pass through the holes while larger bran stays on the sieve."),
 AR4("Churning of curd gives butter.", "Churning separates the lighter fat from the other parts of curd or milk.", "a",
     "The lighter fat collects as butter, so R explains A."),
 AR4("Iron nails can be separated from a mixture with sand using a magnet.", "Sand is attracted by a magnet.", "c",
     "A is true. R is false: sand is non-magnetic."),
]

CASE = [
 Q("<b>Case study.</b> After harvest, farmers in Punjab beat the wheat stalks to loosen the grains. Then they pour the grain and husk from a height in the wind, and the husk blows away to a side. The cleaned grain is later passed through a sieve to remove small stones. "
   "(i) Name the process of beating the stalks. (ii) Name the process using wind. (iii) Which method removes small stones? (iv) Why is winnowing not suitable for separating sand from water?",
   "(i) Threshing (1). (ii) Winnowing (1). (iii) Sieving (or handpicking) (1). (iv) Winnowing needs a dry mixture of light and heavy solids, and wind cannot separate a solid from a liquid (1); sand in water is separated by sedimentation and filtration (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Rubina's well water in Raipur looks muddy. Her mother lets it stand in a bucket for an hour. The mud settles at the bottom. She then pours the clear water slowly into another vessel and then passes it through a clean cotton cloth. "
   "(i) What is the settling of mud called? (ii) What is the slow pouring of clear water called? (iii) Which method uses the cloth? (iv) Why is the water still not fit to drink even after this? What should be done?",
   "(i) Sedimentation (1). (ii) Decantation (1). (iii) Filtration (1). (iv) It may still have dissolved impurities and germs (1); it should be boiled (or purified) before drinking (1).", "1+1+1+2"),
 Q("<b>Case study.</b> At a salt farm near the coast of Gujarat, sea water is let into shallow pans. Under the hot sun the water slowly disappears, leaving white salt crystals. In a school lab, Hari does the same with salty water in a dish, then tries to collect the vapour on a cool plate held above. "
   "(i) Name the process that leaves salt behind. (ii) Name the change of vapour into drops on the cool plate. (iii) Which solid is left in the pans? (iv) If Hari wants the water as well as the salt, how can he get both?",
   "(i) Evaporation (1). (ii) Condensation (1). (iii) Salt (1). (iv) Heat the salt solution; salt remains in the dish after the water evaporates (1) and the vapour is cooled so that it condenses into pure water (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Methods for solid mixtures", ["Handpicking: large pieces of different kinds (stones from rice).", "Winnowing: heavy grain and light husk, using wind.", "Threshing: separate grain from stalks by beating.",
   "Sieving: different particle sizes (flour and bran).", "Magnetic separation: iron objects from non-magnetic ones."]),
 ("Solid in liquid", ["Sedimentation: heavier insoluble particles settle down.", "Decantation: pour off the clear liquid slowly.", "Filtration: filter paper or cloth keeps the residue; filtrate passes through.",
   "Evaporation: dissolved solid left behind (salt from sea water)."]),
 ("Other methods", ["Condensation: vapour cooled to liquid.", "Churning: separates butter from curd or cream.", "Evaporation then condensation can give pure water from salt water."]),
 ("Choosing a method", ["Look at size, weight, solubility and magnetic nature of the parts.", "Dissolved solid: evaporation. Insoluble solid in liquid: sedimentation and filtration."]),
]

MISTAKES = [
 "Choosing filtration for salt in water; dissolved salt passes through the filter, so <b>evaporation</b> is needed.",
 "Mixing <b>sedimentation</b> (settling) with <b>decantation</b> (pouring off the clear liquid).",
 "Mixing <b>threshing</b> (beating stalks to free grain) with winnowing (blowing away husk).",
 "Calling the liquid that passes through filter paper the residue; it is the <b>filtrate</b>.",
 "Using a magnet to separate sand or salt; only magnetic substances like iron are attracted.",
 "Believing that filtered or settled water is always safe to drink.",
]
