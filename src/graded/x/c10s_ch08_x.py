"""Class 10 Science Ch 8 Heredity - extras."""
from common import AR4, Q

AR = [
 AR4(r"When pure tall (TT) and pure dwarf (tt) pea plants are crossed, all the F1 plants are tall.", r"Tallness is the dominant trait over dwarfness.", "a",
     r"Every F1 plant is Tt; the dominant allele T masks t, so R explains A."),
 AR4(r"Both parents contribute equally to the genetic material of a human child.", r"The sex of a human child is determined by the sperm that fertilises the egg.", "b",
     r"Both true; the second statement concerns the sex chromosome carried by sperm and does not explain the equal contribution."),
 AR4(r"The sex of a human baby is decided by the type of sperm that fertilises the egg.", r"A woman produces two types of eggs, one with X and the other with Y chromosome.", "c",
     r"Sperms are of two types (X or Y), but all eggs carry only X; R is false."),
 AR4(r"The phenotypic ratio in the F2 generation of a monohybrid cross is 1 : 2 : 1.", r"The genotypic ratio in the F2 generation of a monohybrid cross is 1 : 2 : 1.", "d",
     r"The phenotypic ratio is 3 : 1; 1 : 2 : 1 is the genotypic ratio TT : Tt : tt, so A is false and R is true."),
 AR4(r"A recessive trait appears in a plant only when it has two copies of the recessive allele.", r"A dominant allele masks the effect of a recessive allele in the heterozygote.", "a",
     r"In Tt the dominant T masks t; the recessive trait shows only in tt."),
 AR4(r"A cross between a round-seeded plant (Rr) and a wrinkled-seeded plant (rr) gives round and wrinkled seeds in the ratio 1 : 1.", r"When pure round and pure wrinkled pea plants are crossed, all F1 seeds are round.", "b",
     r"Rr x rr gives Rr : rr = 1 : 1, so A is true; R is also true but about a different cross and does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Sunita crossed a pure tall pea plant (TT) with a pure dwarf pea plant (tt). All the F1 plants were tall. She allowed the F1 plants to self-pollinate and obtained 480 F2 plants. "
   r"(i) Write the genotype of the F1 plants. (ii) What is the F2 phenotypic ratio? (iii) How many of the 480 F2 plants are expected to be dwarf? (iv) How many of the 480 F2 plants are expected to be tall with genotype Tt? Give the genotypic ratio.",
   r"(i) Tt (1). (ii) 3 tall : 1 dwarf (1). (iii) $480/4=120$ dwarf plants (1). (iv) Genotypic ratio TT : Tt : tt = 1 : 2 : 1 (1); Tt plants $=480\times\dfrac12=240$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Neha and Ajay are expecting a baby. Ajay's grandmother tells them that the mother decides whether the baby will be a boy or a girl. Neha's biology teacher friend says that the claim is not true. "
   r"(i) Write the sex chromosomes of a human male. (ii) Which sex chromosome is present in all the eggs of a woman? (iii) What is the chance that the baby will be a boy? (iv) Explain, with reasoning, who determines the sex of the child.",
   r"(i) XY (1). (ii) X (1). (iii) 50% (1 in 2) (1). (iv) The father determines the sex (1): sperms carry X or Y in equal numbers; an X sperm gives XX (girl) and a Y sperm gives XY (boy), while all eggs carry X (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A single bacterium divides to form two bacteria, and each of these divides again. The four bacteria are very similar but show slight differences due to small errors in DNA copying. In humans, who reproduce sexually, much greater variations are seen among individuals. During a heat wave, only some of the bacteria with a particular variation survive. "
   r"(i) What is meant by heredity? (ii) What causes variation in asexual reproduction? (iii) Why is variation greater in sexual reproduction? (iv) Explain why variation is useful for the survival of a species.",
   r"(i) Transmission of characters/traits from parents to offspring (1). (ii) Small inaccuracies (errors) in DNA copying (1). (iii) DNA of two parents combines, giving new combinations of traits (1). (iv) Some variants are better suited to changing conditions (e.g. heat-resistant bacteria) and survive (1), so the species is not wiped out (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Basic terms", [r"Heredity: transmission of characters from parents to offspring. Variation: differences among individuals of a species.",
   r"Gene: unit of DNA controlling a trait. Allele: version of a gene (T or t). Dominant: expressed in F1; recessive: expressed only when both alleles are recessive.",
   r"Genotype: gene combination (TT, Tt, tt); phenotype: visible trait (tall/dwarf). Homozygous: same alleles; heterozygous: different alleles.",
   r"Father and mother contribute equally to the genetic material of the child; each trait has two versions in the child."]),
 ("Mendel's monohybrid cross", [r"Garden pea: contrasting traits (tall/dwarf, round/wrinkled seed, violet/white flower).",
   r"P: TT $\times$ tt $\rightarrow$ F1: all Tt (tall). F1 $\times$ F1 $\rightarrow$ F2: 1 TT : 2 Tt : 1 tt.",
   r"F2 phenotypic ratio $=3:1$ (tall : dwarf); F2 genotypic ratio $=1:2:1$. Tt $\times$ tt gives 1 : 1.",
   r"Traits are inherited independently; recessive trait reappears in F2."]),
 ("Sex determination in humans", [r"23 pairs of chromosomes: 22 pairs autosomes + 1 pair of sex chromosomes. Female XX; male XY.",
   r"Eggs: all carry X. Sperms: half X, half Y. XX = girl; XY = boy. Probability of boy = girl $=\dfrac12$; sex decided by the father's sperm."]),
 ("Variation", [r"Asexual reproduction: small variations from DNA copying errors. Sexual reproduction: DNA of two parents combines $\rightarrow$ more variation.",
   r"Variations help the species survive in a changing environment."]),
]

MISTAKES = [
 r"Giving 1 : 2 : 1 as the F2 <i>phenotypic</i> ratio of a monohybrid cross; it is 3 : 1 phenotypic and 1 : 2 : 1 genotypic.",
 r"Saying that the dominant trait is 'stronger' or 'more common'; it simply masks the recessive allele in the heterozygote.",
 r"Writing the genotype of F1 as TT or tt; the cross of pure TT and pure tt gives only Tt.",
 r"Saying that the mother decides the sex of the child; all eggs carry X, and the father's sperm (X or Y) determines it.",
 r"Forgetting that a recessive trait is expressed only in the homozygous recessive (tt), so it disappears in F1 but reappears in F2.",
 r"Writing the number of chromosomes of the sex cells as 46; gametes contain 23 chromosomes (22 autosomes + 1 sex chromosome).",
]
