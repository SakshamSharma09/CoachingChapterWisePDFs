"""Class 9 Science Ch 12 Reproduction: How Life Continues - extras."""
from common import AR4, Q

AR = [
 AR4("Offspring produced by asexual reproduction are genetically identical to the parent.", "Asexual reproduction involves a single parent and no fusion of gametes.", "a",
     "With one parent and no gamete fusion, the offspring are clones of the parent."),
 AR4("Yeast reproduces by budding.", "<i>Amoeba</i> reproduces by binary fission.", "b",
     "Both statements are true but describe different organisms and methods."),
 AR4("Self-pollination occurs when pollen from an anther reaches the stigma of a flower of a different plant.", "Pollination is the transfer of pollen from the anther to the stigma.", "d",
     "Transfer to a flower of a different plant is cross-pollination, so A is false; R is true."),
 AR4("Identical twins are always of the same sex.", "Identical twins develop from a single fertilised egg that splits into two.", "a",
     "They share the same chromosomes, including the sex chromosomes, so the sex is the same."),
 AR4("Animals that show external fertilisation, such as frogs, lay a large number of eggs.", "Eggs fertilised outside the body are exposed to predators and other hazards, so few survive.", "a",
     "A large number of eggs compensates for the low survival chance."),
 AR4("The sex of a human baby is determined by the sperm.", "Every sperm carries a Y chromosome.", "c",
     "A is true, but sperm carry either X or Y (egg always X), so R is false."),
]

CASE = [
 Q("<b>Case study.</b> Rakesh observes a drop of pond water under a microscope. He sees an <i>Amoeba</i> whose nucleus has divided and the cell is pinching into two daughter cells. In another slide, he sees yeast cells with small outgrowths, and on a damp bread slice at home he finds a fuzzy growth of mould. "
   "(i) Name the method of reproduction seen in <i>Amoeba</i>. (ii) Name the method shown by yeast. (iii) How do bread moulds multiply? (iv) A single <i>Amoeba</i> divides every hour. How many <i>Amoeba</i> are produced from one after 4 hours?",
   r"(i) Binary fission (1). (ii) Budding (1). (iii) By spores formed in sporangia (1). (iv) Number doubles every hour: $2^4=16$ (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A rose plant in Bengaluru is grown from a stem cutting, while a mango tree is grown from seed. A flower of the mango has anthers that produce pollen and a pistil with stigma, style and ovary. "
   "(i) Name the male and female reproductive parts of a flower. (ii) What is pollination? (iii) Name the method by which the rose is multiplied. (iv) Give one advantage of growing plants by vegetative propagation instead of from seeds.",
   "(i) Male: stamen (anther and filament); female: pistil (stigma, style, ovary) (1). (ii) Transfer of pollen grains from the anther to the stigma (1). (iii) Vegetative propagation by stem cutting (1). (iv) The new plant is identical to the parent and bears flowers or fruits earlier / plants without seeds can be grown (1+1).", "1+1+1+2"),
 Q("<b>Case study.</b> A biology teacher explains human reproduction. A sperm fuses with an egg in the fallopian tube to form a zygote, which divides repeatedly to form an embryo. The embryo implants in the uterus and is nourished through the placenta for about nine months. "
   "(i) What is the fusion of a sperm and an egg called? (ii) Where does fertilisation take place? (iii) What is the function of the placenta? (iv) The zygote divides repeatedly. How many cells are present after 3 divisions, and what does the zygote carry in terms of the number of chromosomes?",
   r"(i) Fertilisation (1). (ii) In the fallopian tube (oviduct) (1). (iii) It supplies food and oxygen to the embryo and removes its wastes (1). (iv) $2^3=8$ cells (1); the zygote has 46 chromosomes (23 from the sperm and 23 from the egg) (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Asexual reproduction", ["Single parent, no gametes, offspring identical to the parent.",
   "Binary fission: <i>Amoeba</i>, bacteria. Budding: yeast, <i>Hydra</i>. Spore formation: bread mould (<i>Rhizopus</i>), ferns. Fragmentation: <i>Spirogyra</i>. Regeneration: <i>Planaria</i>, <i>Hydra</i>.",
   "Vegetative propagation: cutting (rose), layering (jasmine), grafting (mango), tubers (potato), bulbs (onion). Tissue culture: new plants from small pieces of tissue."]),
 ("Sexual reproduction", ["Two parents; fusion of male and female gametes gives a zygote; offspring show variation.",
   "Number of cells after $n$ divisions of a zygote $=2^{n}$ (equal divisions).",
   "Human chromosomes: 23 pairs (46); gametes have 23; sex chromosomes XX (female) and XY (male)."]),
 ("Flowering plants", ["Stamen (anther with pollen) is male; pistil (stigma, style, ovary with ovules) is female.",
   "Pollination $\\rightarrow$ pollen germinates, pollen tube $\\rightarrow$ fertilisation $\\rightarrow$ zygote $\\rightarrow$ embryo; ovule $\\rightarrow$ seed, ovary $\\rightarrow$ fruit.",
   "Self-pollination: same flower or same plant; cross-pollination: different plant, by wind, water, insects, birds. Seed dispersal by wind, water, animals, explosion."]),
 ("Human reproduction", ["Male: testes (make sperm; in scrotum), vas deferens, urethra, penis. Female: ovaries (make eggs), fallopian tubes (site of fertilisation), uterus (implantation), vagina.",
   "Fertilisation $\\rightarrow$ zygote $\\rightarrow$ embryo $\\rightarrow$ foetus; placenta supplies nutrients and oxygen; pregnancy about 9 months (about 40 weeks).",
   "Menstruation: shedding of the uterine lining about every 28 days when the egg is not fertilised."]),
 ("Fertilisation in animals", ["External fertilisation (outside the body, in water): fish, frogs; very many eggs. Internal fertilisation: birds, mammals, humans; fewer eggs, better protection.",
   "Identical twins: one zygote splits, same sex; fraternal twins: two eggs fertilised separately, may differ in sex."]),
]

MISTAKES = [
 "Saying that budding is the method of <i>Amoeba</i>; <i>Amoeba</i> divides by binary fission, whereas yeast and <i>Hydra</i> reproduce by budding.",
 "Confusing pollination (transfer of pollen) with fertilisation (fusion of male and female gametes).",
 "Saying that fertilisation takes place in the uterus; it takes place in the fallopian tube, and the embryo implants in the uterus.",
 "Writing that offspring of asexual reproduction show variation; they are identical to the parent (variation arises in sexual reproduction).",
 "Giving 46 as the number of chromosomes in a human sperm or egg; gametes have 23, the zygote has 46.",
 "Thinking the sex of the baby is decided by the mother; every egg carries X, so the type of sperm (X or Y) decides.",
]
