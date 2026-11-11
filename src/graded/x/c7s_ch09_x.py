"""Class 7 Science Ch 9 Life Processes in Plants - extras."""
from common import AR4, Q

AR = [
 AR4("Photosynthesis takes place in the presence of sunlight and chlorophyll.", "Chlorophyll absorbs the energy of sunlight needed to make food.", "a",
     "The green pigment traps light energy, which explains why chlorophyll is needed."),
 AR4("Stomata help in the exchange of gases in a leaf.", "Guard cells control the opening and closing of stomata.", "b",
     "Both are true, but guard cells do not explain why gases exchange occurs through stomata."),
 AR4("Transpiration is the loss of water vapour from the leaves through stomata.", "Transpiration takes place only through the roots of a plant.", "c",
     "A is true; transpiration occurs mainly through stomata in leaves, so R is false."),
 AR4("Xylem carries the food made in the leaves to all parts of the plant.", "Phloem carries the food made in the leaves to other parts.", "d",
     "Xylem carries water and minerals, so A is false; phloem carries food, so R is true."),
 AR4("Pulse crops need less nitrogen fertiliser.", "Rhizobium bacteria in their root nodules convert atmospheric nitrogen into usable form.", "a",
     "Rhizobium fixes nitrogen for the plant, so less fertiliser is needed."),
 AR4("Cuscuta is a parasitic plant.", "The pitcher plant traps insects to obtain nitrogen.", "b",
     "Both are true statements about non-green or special nutrition, but they are unrelated."),
]

CASE = [
 Q("<b>Case study.</b> Anita keeps a potted plant in a dark room for two days. Then she covers part of a leaf with black paper, keeps the plant in sunlight for a few hours, plucks the leaf, boils it in alcohol and adds a few drops of iodine solution. "
   "(i) Why was the plant kept in the dark first? (ii) Which solution is used to test for starch? (iii) What colour will the uncovered part of the leaf turn? (iv) What will happen to the covered part, and what does this show?",
   "(i) To use up (remove) the stored starch from the leaf (1). (ii) Iodine solution (1). (iii) Blue-black (1). (iv) The covered part does not turn blue-black (1), which shows that light is necessary for photosynthesis (starch formation) (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Ravi covers a leafy branch of a plant growing in a pot with a transparent polythene bag and keeps it in the sun. After some hours, tiny water droplets appear inside the bag. "
   "(i) Name the process that released the water vapour. (ii) Name the tiny pores through which it was lost. (iii) Name the tissue that carries water from roots to leaves. (iv) State one benefit of this process to the plant.",
   "(i) Transpiration (1). (ii) Stomata (1). (iii) Xylem (1). (iv) It cools the plant (1) and helps pull water and minerals upward from the roots (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A farmer in Haryana notices a yellow, leafless creeper twining around a hedge. In a botanical garden he sees a pitcher plant, and in his pulse field he finds small swellings on the roots of the plants. "
   "(i) What is the mode of nutrition of the yellow creeper? (ii) Name the creeper. (iii) Name the bacteria found in the root swellings. (iv) Explain why the pitcher plant traps insects and why the hedge plant becomes weak.",
   "(i) Parasitic nutrition (1). (ii) Cuscuta (1). (iii) Rhizobium (1). (iv) The pitcher plant grows in nitrogen-poor soil and obtains nitrogen from insects (1); Cuscuta takes ready-made food from the hedge plant, leaving less food for it (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Photosynthesis", [
   "Carbon dioxide + water $\\xrightarrow{\\text{sunlight, chlorophyll}}$ glucose (starch) + oxygen.",
   "Occurs in green parts (mainly leaves) containing chlorophyll in chloroplasts; plants are autotrophs.",
   "Carbon dioxide enters through stomata; water enters through root hairs; oxygen is released.",
   "Starch test: iodine solution turns blue-black."]),
 ("Stomata and transpiration", [
   "Stomata: tiny pores on the leaf surface, opened and closed by guard cells; exchange of gases and loss of water vapour.",
   "Transpiration: loss of water vapour from leaves; it cools the plant and helps in upward movement of water."]),
 ("Transport and respiration", [
   "Xylem carries water and minerals from roots to leaves; phloem carries food from leaves to other parts.",
   "Respiration in plants: glucose + oxygen $\\rightarrow$ energy + carbon dioxide + water; takes place day and night in all living cells."]),
 ("Other modes of nutrition", [
   "Parasites: take food from a host (Cuscuta). Saprotrophs: feed on dead matter (fungi, mushroom).",
   "Insectivorous plants (pitcher plant) trap insects to get nitrogen. Rhizobium in root nodules of pulses fixes nitrogen.",
   "Fertilisers and manure supply nutrients like nitrogen to the soil."]),
]

MISTAKES = [
 "Saying that photosynthesis takes place only at night, or that respiration takes place only at night; photosynthesis needs <b>light</b>, respiration goes on <b>all the time</b>.",
 "Confusing xylem and phloem: <b>xylem</b> = water and minerals up, <b>phloem</b> = food from leaves.",
 "Writing that oxygen is a raw material of photosynthesis; the raw materials are carbon dioxide and water, and oxygen is the <i>by-product</i>.",
 "Mixing up transpiration (loss of water vapour through stomata) with absorption of water by the root hairs.",
 "Writing that Cuscuta makes its own food; it is a <b>parasite</b> without chlorophyll.",
 "Forgetting that iodine test shows <b>starch</b> (blue-black), not glucose, and that the leaf should first be boiled in alcohol to remove chlorophyll.",
]
