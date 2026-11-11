"""Class 10 Science Ch 7 How do Organisms Reproduce - extras."""
from common import AR4, Q

AR = [
 AR4(r"Plants raised by vegetative propagation show characters identical to the parent plant.", r"Vegetative propagation involves only one parent and no fusion of gametes.", "a",
     r"With a single parent and no gamete fusion there is no mixing of DNA, so the offspring are almost identical clones."),
 AR4(r"Hydra reproduces by budding.", r"Planaria can regenerate a complete individual from a cut piece.", "b",
     r"Both true; they are different modes of asexual reproduction, and R does not explain A."),
 AR4(r"Sperms are produced in the testes.", r"The testes are located inside the abdominal cavity of a male.", "c",
     r"Testes lie outside the abdomen in the scrotum, where the temperature is lower, which is needed for sperm formation; R is false."),
 AR4(r"Fertilisation in human beings takes place in the uterus.", r"The zygote gets implanted in the lining of the uterus.", "d",
     r"Fertilisation takes place in the oviduct (fallopian tube), so A is false; implantation in the uterus is true."),
 AR4(r"The placenta is essential for the development of the embryo in human beings.", r"The placenta provides oxygen and nutrients from the mother's blood to the embryo and removes its wastes.", "a",
     r"R describes the function that makes the placenta essential."),
 AR4(r"In Amoeba, binary fission produces two daughter cells.", r"Multiple fission, in which many daughter cells form at once, occurs in Plasmodium.", "b",
     r"Both true, but they describe different organisms; R does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Lakshmi dissected a hibiscus flower in her biology class. She saw sepals, petals, several stamens and a pistil in the centre. A bee had been visiting the flower and carrying yellow dust from one flower to another. "
   r"(i) Name the male reproductive part of the flower. (ii) What is the transfer of pollen from anther to stigma called? (iii) After fertilisation, which part of the flower develops into the fruit? (iv) Differentiate between self-pollination and cross-pollination and name one agent of cross-pollination.",
   r"(i) Stamen (anther produces pollen) (1). (ii) Pollination (1). (iii) Ovary (1). (iv) Self-pollination: pollen from the anther reaches the stigma of the same flower (or another flower of the same plant); cross-pollination: pollen reaches the stigma of a flower of a different plant (1); agent: wind, water, insects or animals (any one) (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A gardener, Ramu, grows new rose plants from cuttings of stems and sprouts new potato plants from the buds (eyes) of old potatoes. In his bakery, he uses yeast to make bread, and notices small outgrowths on yeast cells under the microscope. "
   r"(i) What is the method of growing plants from vegetative parts called? (ii) Name the part of the potato that gives rise to new plants. (iii) Name the mode of reproduction in yeast. (iv) Why is vegetative propagation preferred for growing banana and rose plants?",
   r"(i) Vegetative propagation (1). (ii) The eyes (buds) (1). (iii) Budding (1). (iv) Banana and rose do not produce viable seeds (or seeds are slow) (1); the new plants are genetically identical to the parent, flower and fruit earlier and retain good characters (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Dr Kaur explained human reproduction to a class of 10th graders. She said that the egg is released from the ovary and is fertilised in the oviduct. The zygote then moves to the uterus and is implanted. If the egg is not fertilised, a bleeding occurs from the vagina about every month. "
   r"(i) Where does fertilisation take place? (ii) Name the tissue that provides nutrition to the embryo. (iii) Name the male hormone secreted by the testes at puberty. (iv) What is the monthly bleeding called, and why does it occur?",
   r"(i) Oviduct (fallopian tube) (1). (ii) Placenta (1). (iii) Testosterone (1). (iv) Menstruation (1); the thick, spongy lining of the uterus prepared for the embryo is shed as the egg is not fertilised (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Asexual reproduction", [r"Fission: binary (Amoeba, Leishmania has a definite plane) and multiple (Plasmodium). Fragmentation: Spirogyra.",
   r"Regeneration: Hydra, Planaria (specialised cells form new tissue). Budding: Hydra, yeast. Spore formation: Rhizopus.",
   r"Vegetative propagation: cutting, layering, grafting, tissue culture; Bryophyllum (leaf), potato (eyes), rose, banana, jasmine.",
   r"Single parent, no gametes, offspring identical; small variations arise from errors in DNA copying."]),
 ("Sexual reproduction in flowering plants", [r"Flower: sepals, petals, stamen (anther + filament; male), pistil/carpel (stigma, style, ovary; female).",
   r"Pollination (anther $\rightarrow$ stigma): self or cross. Pollen tube grows through the style to the ovule.",
   r"Fertilisation: male gamete + egg $\rightarrow$ zygote $\rightarrow$ embryo (in ovule). After fertilisation: ovule $\rightarrow$ seed, ovary $\rightarrow$ fruit, other parts wither.",
   r"Seed: embryo (plumule, radicle), cotyledon(s), seed coat. Germination gives a seedling."]),
 ("Human reproduction", [r"Male: testes (sperms and testosterone), scrotum (lower temperature), vas deferens, prostate and seminal vesicles (secretions), urethra.",
   r"Female: ovary (eggs and hormones), oviduct (fertilisation site), uterus (implantation), cervix, vagina.",
   r"Zygote $\rightarrow$ embryo $\rightarrow$ foetus; placenta: provides oxygen and nutrients and removes wastes; gestation about 9 months.",
   r"Puberty: boys, facial hair and voice change; girls, breast development and menstruation (about monthly if the egg is not fertilised).",
   r"Number of organisms after $n$ binary fissions $=2^n$."]),
]

MISTAKES = [
 r"Writing that Plasmodium reproduces by binary fission; it undergoes <b>multiple</b> fission, whereas Amoeba shows binary fission.",
 r"Using 'fertilisation' for pollination; pollination is transfer of pollen, fertilisation is fusion of male and female gametes.",
 r"Saying that fertilisation takes place in the uterus; it occurs in the oviduct and the zygote is implanted in the uterus.",
 r"Confusing regeneration with reproduction by fragmentation; regeneration uses specialised cells to rebuild a missing part, e.g. Planaria, Hydra.",
 r"Stating that asexual reproduction produces absolutely identical offspring; tiny variations are produced by errors in DNA copying.",
 r"Believing that the testes lie inside the abdomen; they are in the scrotum because sperm formation requires a lower temperature.",
]
