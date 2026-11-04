"""Class 10 Science Ch 8 - Heredity (hand-written graded banks)."""
from scix import tier

SLUG, NAME, CHNO = "Heredity", "Heredity", 8

# ============================ NCERT-TYPE ============================
nA = """
Who is called the Father of Genetics? ~~ Gregor Johann Mendel ~~ Charles Darwin ~~ Louis Pasteur ~~ Robert Hooke ~~ Mendel worked on garden pea plants.
Mendel chose the garden pea for his experiments because ~~ it has many contrasting characters and is easy to grow ~~ it grows only in cold regions ~~ it has no flowers ~~ it reproduces only asexually ~~ Pea has clear contrasting traits and short life cycle.
The transmission of characters from parents to offspring is called ~~ heredity ~~ evolution ~~ variation ~~ regeneration ~~ Definition of heredity.
When pure tall (TT) and pure dwarf (tt) pea plants are crossed, the F1 generation is ~~ all tall ~~ all dwarf ~~ half tall and half dwarf ~~ three tall to one dwarf ~~ Tallness is dominant.
When F1 plants of the tall x dwarf cross are self-pollinated, the F2 phenotypic ratio is ~~ 3 tall : 1 dwarf ~~ 1 tall : 3 dwarf ~~ 1 : 1 ~~ all tall ~~ Monohybrid ratio is 3 : 1.
The genotypic ratio of the F2 generation in a monohybrid cross is ~~ 1 : 2 : 1 ~~ 3 : 1 ~~ 9 : 3 : 3 : 1 ~~ 1 : 1 ~~ TT : Tt : tt.
A trait which expresses itself in the F1 generation is called ~~ dominant ~~ recessive ~~ acquired ~~ mutated ~~ It masks the other trait.
The trait that is not seen in F1 but reappears in F2 is ~~ recessive ~~ dominant ~~ acquired ~~ sex-linked ~~ It is hidden in F1.
Alternate forms of a gene are called ~~ alleles ~~ gametes ~~ zygotes ~~ chromosomes ~~ For example T and t.
The physical appearance of an organism for a trait is its ~~ phenotype ~~ genotype ~~ allele ~~ genome ~~ It is the observable character.

In a dihybrid cross between round yellow (RRYY) and wrinkled green (rryy) seeds, the F1 seeds are ~~ all round yellow ~~ all wrinkled green ~~ round green ~~ wrinkled yellow ~~ Round and yellow are dominant.
The F2 phenotypic ratio in the dihybrid cross is ~~ 9 : 3 : 3 : 1 ~~ 3 : 1 ~~ 1 : 2 : 1 ~~ 1 : 1 : 1 : 1 ~~ Four phenotypes appear.
In the dihybrid F2, the number of round green seeds out of 16 is ~~ 3 ~~ 9 ~~ 1 ~~ 4 ~~ The 3 round green seeds are R_yy.
The new combinations of traits (round green and wrinkled yellow) in F2 show that ~~ traits are inherited independently ~~ traits are always linked ~~ no dominant trait exists ~~ F1 gets only one parent's traits ~~ Independent assortment.
Genes are located on ~~ chromosomes ~~ ribosomes ~~ cell wall ~~ mitochondria only ~~ Chromosomes carry genes made of DNA.
The set of genes of an organism is its ~~ genotype ~~ phenotype ~~ allele ~~ gamete ~~ Genotype is the genetic make-up.
A plant that has two different alleles for a trait is called ~~ heterozygous ~~ homozygous ~~ pure line ~~ recessive ~~ Example: Tt.
A homozygous plant is ~~ TT or tt ~~ Tt ~~ always tall ~~ always short ~~ Both alleles are the same.
A cross between F1 (Tt) and the recessive parent (tt) is called ~~ a test cross ~~ a dihybrid cross ~~ self-cross ~~ reciprocal cross ~~ It reveals the genotype of F1.
The gametes of a Tt plant are ~~ T and t in equal numbers ~~ only Tt ~~ only T ~~ only t ~~ Alleles separate during gamete formation.

In human beings, the sex of the child is determined by ~~ the type of sperm that fertilises the egg ~~ the egg alone ~~ the mother's diet ~~ environmental temperature ~~ Father's sperm may carry X or Y.
A normal human female has the sex chromosomes ~~ XX ~~ XY ~~ YY ~~ XO ~~ Both are X.
A normal human male has the sex chromosomes ~~ XY ~~ XX ~~ YY ~~ XXY ~~ One X and one Y.
The total number of chromosomes in a human body cell is ~~ 46 ~~ 23 ~~ 44 ~~ 48 ~~ 23 pairs.
The number of autosomes in a human body cell is ~~ 44 ~~ 46 ~~ 22 ~~ 23 ~~ 22 pairs, i.e. 44.
The probability that a child will be a boy is ~~ 50% ~~ 25% ~~ 75% ~~ 100% ~~ XY and XX are equally likely.
Traits that a parent acquires during life, such as a bodybuilder's muscle, are ~~ not inherited ~~ inherited always ~~ transmitted by DNA ~~ inherited only by sons ~~ Acquired traits do not change DNA of germ cells.
Which of the following is an inherited trait? ~~ Eye colour ~~ A scar on the hand ~~ Tanned skin ~~ Learning to cycle ~~ Eye colour is genetic.
Free earlobes and attached earlobes are examples of ~~ variation within a species ~~ acquired traits ~~ sex determination ~~ no variation ~~ Differences are inherited.
Which gamete decides that the baby is a girl? ~~ Sperm with X chromosome ~~ Sperm with Y chromosome ~~ Egg with Y ~~ Egg with O ~~ X sperm gives XX.
""".strip()
nB = """
What is the difference between heredity and variation? ~~ Heredity: transmission of characters from parents to offspring|1 ~~ Variation: differences among individuals of a species|1
Why did Mendel choose pea plants? ~~ They have clear contrasting characters|1 ~~ They are easily grown and have a short life cycle|1
Define dominant and recessive traits. ~~ Dominant trait expresses in the F1|1 ~~ Recessive trait is hidden in F1 and appears in F2|1
Differentiate between genotype and phenotype. ~~ Genotype: genetic make-up of an organism|1 ~~ Phenotype: its observable characteristics|1
What is a monohybrid cross? Give the F2 ratio. ~~ A cross involving one pair of contrasting characters|1 ~~ F2 ratio is 3 : 1|1
State Mendel's law of independent assortment. ~~ Genes for different traits are inherited independently of each other|2
How many chromosomes does a human sperm and egg have each? ~~ 23 in each|1 ~~ Zygote has 46|1
How is the sex of a child determined? ~~ Egg carries X; sperm carries X or Y|1 ~~ X sperm gives a girl and Y sperm gives a boy|1
What is an acquired trait? Give an example. ~~ A trait gained during the lifetime of an individual|1 ~~ Example: loss of body weight due to starvation|1
Why are traits like muscle size not passed on to offspring? ~~ They are not coded in the germ-cell DNA|1 ~~ Changes in body cells are not inherited|1
Why does the F2 generation show the F1 hidden trait again? ~~ F1 plants carry both alleles|1 ~~ Alleles separate and combine in F2|1
What is a gene? Where is it present? ~~ A segment of DNA that codes for a protein|1 ~~ Present on chromosomes in the nucleus|1
""".strip()
nC = """
A pure tall plant is crossed with a pure dwarf plant. Write the genotype and phenotype of F1 and the F2 ratio. ~~ F1: genotype Tt, phenotype tall|1 ~~ F2 phenotypic ratio 3 tall : 1 dwarf|1 ~~ F2 genotypic ratio 1 TT : 2 Tt : 1 tt|1
How do Mendel's experiments show that traits are inherited independently? ~~ Round yellow x wrinkled green gives round yellow F1|1 ~~ F2 shows round green and wrinkled yellow|1 ~~ New combinations show independent assortment|1
List three differences between acquired and inherited traits. ~~ Inherited traits are controlled by genes; acquired are not|1 ~~ Inherited traits are passed on; acquired are not|1 ~~ Example: eye colour (inherited) and a scar (acquired)|1
A man and a woman have a baby. Explain how the child receives traits from both parents. ~~ Each parent contributes one set of chromosomes|1 ~~ The child gets 23 from the father and 23 from the mother|1 ~~ Hence it has a mix of traits from both|1
Explain with a cross why a tall F1 plant may produce dwarf offspring. ~~ F1 is Tt|1 ~~ Gametes T and t combine at random|1 ~~ tt (dwarf) appears with probability 1/4|1
Explain sex determination in humans with a chart. ~~ Mother: XX produces only X eggs|1 ~~ Father: XY produces X and Y sperms|1 ~~ XX (girl) or XY (boy) in the ratio 1 : 1|1
Explain why the father, not the mother, determines the sex of the child. ~~ Eggs always carry an X chromosome|1 ~~ Sperm can carry X or Y|1 ~~ The sperm that fertilises the egg decides the sex|1
Differentiate between dominant and recessive traits with the help of a pea example. ~~ Tall (T) is dominant over dwarf (t)|1 ~~ In Tt, tallness is expressed|1 ~~ Dwarfness appears only in tt|1
What are autosomes and sex chromosomes? How many pairs are there in humans? ~~ Autosomes: chromosomes that do not decide sex, 22 pairs|1 ~~ Sex chromosomes decide sex, 1 pair|1 ~~ Total 23 pairs|1
How does the accumulation of variation take place over generations in asexually reproducing organisms? ~~ Small copying errors occur in DNA|1 ~~ These errors are passed to daughter cells|1 ~~ Variations accumulate over generations|1
In pea plants, round seeds (R) are dominant to wrinkled (r). What is the result of crossing Rr x rr? ~~ Gametes R, r and r, r|1 ~~ Genotypes Rr and rr in 1 : 1|1 ~~ Half round, half wrinkled|1
Why is variation more in sexual reproduction? ~~ Two parents contribute genes|1 ~~ Gametes combine in many ways|1 ~~ Crossing over and copying errors add to it|1
What is the role of DNA in heredity? ~~ DNA carries genetic information|1 ~~ Segments called genes control traits|1 ~~ DNA is passed from parents to offspring through gametes|1
Explain the term 'F1' and 'F2' generations. ~~ F1 is the first filial generation from the cross of parents|1 ~~ F2 is produced by self-pollination of F1|1 ~~ F2 shows the reappearance of recessive trait|1
How many different types of gametes can a plant with genotype RrYy produce? Name them. ~~ Four types|1 ~~ RY, Ry, rY, ry|1 ~~ Each in equal proportion|1
Why can the wrinkled-green seeds appear only in the F2 and not in the F1? ~~ F1 has one dominant allele for each trait|1 ~~ Recessive alleles are masked|1 ~~ rryy forms only when both recessives combine in F2|1
How does the Y chromosome influence the sex of a baby? ~~ A Y-bearing sperm gives XY|1 ~~ XY is male|1 ~~ Absence of Y gives XX female|1
State the difference between a test cross and a self-cross. ~~ Test cross: F1 crossed with a recessive parent|1 ~~ Self cross: F1 crossed with itself|1 ~~ Test cross reveals the genotype of F1|1
""".strip()
nD = """
Explain Mendel's monohybrid cross with tall and dwarf pea plants. Show the F1 and F2 generations with a Punnett square and the ratios. ~~ Parents: TT x tt|1 ~~ F1: all Tt, tall|1 ~~ F1 self-pollinated: gametes T and t|1 ~~ F2: TT, Tt, Tt, tt|1 ~~ Phenotypic ratio 3 : 1 and genotypic ratio 1 : 2 : 1|1
Describe Mendel's dihybrid cross using round yellow and wrinkled green seeds. Give the phenotypes and ratio in F2. ~~ Parents RRYY x rryy|1 ~~ F1 all RrYy, round yellow|1 ~~ F1 forms four gametes RY, Ry, rY, ry|1 ~~ F2 round yellow 9, round green 3, wrinkled yellow 3, wrinkled green 1|1 ~~ Ratio 9 : 3 : 3 : 1 proves independent assortment|1
What is meant by (a) dominant trait, (b) recessive trait, (c) homozygous, (d) heterozygous? Give an example for each. ~~ Dominant: expressed in F1, e.g. T|1 ~~ Recessive: hidden in F1, e.g. t|1 ~~ Homozygous: TT or tt|1 ~~ Heterozygous: Tt|1 ~~ Examples are from tall and dwarf pea|1
Explain how sex is determined in human beings. What are the chances of having a boy or a girl? ~~ Women have XX and men have XY|1 ~~ Egg always carries X|1 ~~ Sperm carries X or Y with equal probability|1 ~~ X sperm gives girl, Y sperm gives boy|1 ~~ The chance of a boy or a girl is 50% each|1
Differentiate between acquired and inherited traits with two examples each. Why do acquired traits not pass on? ~~ Inherited: controlled by genes|1 ~~ Acquired: gained during lifetime|1 ~~ Examples: eye colour, hair colour (inherited)|1 ~~ Examples: scars, tanned skin (acquired)|1 ~~ Acquired changes do not alter germ-cell DNA|1
How do traits get expressed? Explain the link between genes, proteins and traits with the example of plant height. ~~ Genes are DNA segments that make proteins|1 ~~ Proteins control body characters|1 ~~ Gene for the plant hormone enzyme controls height|1 ~~ An efficient enzyme gives more hormone, so a tall plant|1 ~~ Less efficient enzyme gives dwarf plants|1
Explain Mendel's experiments and the conclusions drawn from them. ~~ He crossed plants having contrasting traits|1 ~~ F1 showed only one parent's trait|1 ~~ F2 had both traits in 3 : 1|1 ~~ Traits are controlled by pairs of factors|1 ~~ Factors segregate in gametes and are independently inherited|1
A cross is made between tall plants (Tt) and dwarf plants (tt). Show the result with a Punnett square and give genotypic and phenotypic ratios. ~~ Gametes: T, t and t, t|1 ~~ Offspring: Tt, Tt, tt, tt|1 ~~ Genotypic ratio 1 : 1|1 ~~ Phenotypic ratio 1 tall : 1 dwarf|1 ~~ Such a cross is a test cross|1
How is variation produced in a population that reproduces sexually? Explain its importance. ~~ Gametes carry different gene combinations|1 ~~ Fertilisation combines the genes of two parents|1 ~~ Copying errors add new variations|1 ~~ Variations help survival under changes|1 ~~ Variation is the basis of the diversity in nature|1
Why are the chromosomes present in pairs? Explain how the number of chromosomes remains constant from generation to generation. ~~ One chromosome of each pair comes from each parent|1 ~~ Gametes have half the number|1 ~~ 23 in sperm, 23 in egg|1 ~~ Fertilisation restores 46|1 ~~ So the number is constant|1
Explain why a child may resemble the parents but also differ from them. ~~ Child gets half the genes from each parent|1 ~~ Traits are combined from both|1 ~~ Alleles may be recombined differently|1 ~~ Copying errors produce new variations|1 ~~ So the child has both resemblance and differences|1
Describe the different ways in which variations arise in sexually reproducing organisms. ~~ DNA copying errors|1 ~~ Combination of gametes from two parents|1 ~~ Independent assortment of traits|1 ~~ Random fusion of gametes|1 ~~ Variation is passed to the next generation|1
""".strip()

# ============================ EASY ============================
eA = """
Genetics is the study of ~~ heredity and variation ~~ plants only ~~ animal fossils ~~ digestion ~~ Genetics deals with inheritance.
Mendel worked on ~~ garden pea ~~ wheat ~~ maize ~~ mango ~~ Pisum sativum.
A character such as tallness or dwarfness is called a ~~ trait ~~ gene ~~ cell ~~ gamete ~~ Observable feature.
The part of the cell that contains genes is the ~~ nucleus ~~ cell wall ~~ vacuole ~~ ribosome ~~ Chromosomes are in the nucleus.
Chromosomes are made of ~~ DNA and protein ~~ only lipids ~~ only starch ~~ cellulose ~~ Genetic material.
Variations among individuals are ~~ differences in characters ~~ always harmful ~~ not inherited ~~ absent in humans ~~ Variation is the basis of diversity.
In pea plants, the dominant trait for stem height is ~~ tall ~~ dwarf ~~ medium ~~ none ~~ T is dominant over t.
In pea plants, the recessive form of seed shape is ~~ wrinkled ~~ round ~~ green ~~ yellow ~~ r is recessive.
A pair of contrasting characters is ~~ tall and dwarf ~~ tall and round ~~ green and tall ~~ yellow and wrinkled ~~ Both are forms of the same character.
Mendel's first generation of the cross is called ~~ F1 ~~ F2 ~~ P ~~ F3 ~~ First filial generation.

Number of chromosomes in a human body cell is ~~ 46 ~~ 23 ~~ 23 pairs plus 1 ~~ 44 ~~ 23 pairs.
Sex chromosomes in a human male are ~~ XY ~~ XX ~~ YY ~~ XO ~~ One X and one Y.
Sex chromosomes in a human female are ~~ XX ~~ XY ~~ YY ~~ XYY ~~ Two X.
Chromosomes that determine sex are called ~~ sex chromosomes ~~ autosomes ~~ plasmids ~~ genes ~~ X and Y.
The egg of a human female contains ~~ one X chromosome as a sex chromosome ~~ one Y chromosome ~~ two X chromosomes ~~ no sex chromosomes ~~ Each egg has an X.
A sperm can contain ~~ X or Y ~~ only X ~~ only Y ~~ XX ~~ Half the sperms have X, half have Y.
A child who is XX is ~~ a girl ~~ a boy ~~ a twin ~~ neither ~~ XX is female.
The zygote formed from X sperm and X egg develops into ~~ a girl ~~ a boy ~~ a twin boy ~~ no baby ~~ XX.
The chance that a newborn is a girl is ~~ 50% ~~ 25% ~~ 75% ~~ 100% ~~ Equal probabilities.
Who decides the sex of the child? ~~ Father ~~ Mother ~~ Grandmother ~~ Doctor ~~ Because the sperm may carry X or Y.

Which is an inherited trait? ~~ Colour of the eyes ~~ Knowing how to swim ~~ A broken arm ~~ A tan ~~ Controlled by genes.
Which is an acquired trait? ~~ A scar from an accident ~~ Hair colour ~~ Blood group ~~ Height potential ~~ Gained in life.
Acquired traits are ~~ not passed to the next generation ~~ always passed on ~~ coded in DNA ~~ present at birth ~~ They do not change germ cells.
The tall x dwarf F1 plants are ~~ heterozygous tall ~~ homozygous tall ~~ homozygous dwarf ~~ pure dwarf ~~ Tt.
The F2 ratio for a monohybrid cross is ~~ 3 : 1 ~~ 1 : 3 ~~ 9 : 3 : 3 : 1 ~~ 2 : 1 ~~ Three dominant to one recessive.
The F2 ratio of the dihybrid cross is ~~ 9 : 3 : 3 : 1 ~~ 3 : 1 ~~ 1 : 1 ~~ 1 : 2 : 1 ~~ Four types of phenotypes.
Gametes carry ~~ half the number of chromosomes ~~ twice the number ~~ no chromosomes ~~ only X ~~ Haploid.
Fertilisation restores the ~~ full number of chromosomes ~~ half the number ~~ zero ~~ double number ~~ Zygote has 46.
A bodybuilder's well-developed muscles will be passed to children? ~~ No ~~ Yes ~~ Only to sons ~~ Only to daughters ~~ It is acquired.
Alleles are ~~ different forms of a gene ~~ two chromosomes ~~ gametes ~~ proteins ~~ Alternate forms.
""".strip()
eB = """
Who is the Father of Genetics? ~~ Gregor Mendel|2
Define heredity. ~~ Transmission of traits from parents to offspring|2
What is variation? ~~ Differences in characters among individuals|2
Name the plant on which Mendel experimented. ~~ Garden pea|1 ~~ Pisum sativum|1
What are chromosomes? ~~ Thread-like structures in the nucleus|1 ~~ Made of DNA and protein, carrying genes|1
What is a gene? ~~ A unit of heredity|1 ~~ A segment of DNA|1
Name the sex chromosomes in a male and a female. ~~ Male: XY|1 ~~ Female: XX|1
What does F1 stand for? ~~ First filial generation|2
What is the F2 phenotypic ratio of a monohybrid cross? ~~ 3 : 1|2
What is an allele? ~~ Alternative form of a gene|2
Give one example of an acquired trait. ~~ Scar|1 ~~ Tanned skin or muscles|1
Which parent determines the sex of the child? ~~ Father|1 ~~ His sperm carries X or Y|1
""".strip()
eC = """
Mention any three traits that Mendel studied in pea plants. ~~ Seed shape (round or wrinkled)|1 ~~ Seed colour (yellow or green)|1 ~~ Plant height (tall or dwarf)|1
Differentiate between dominant and recessive traits. ~~ Dominant trait appears in F1|1 ~~ Recessive trait is hidden in F1|1 ~~ Recessive shows only when both alleles are recessive|1
What are autosomes? How many are present in a human cell? ~~ Chromosomes other than the sex chromosomes|1 ~~ 22 pairs|1 ~~ 44 autosomes in all|1
Distinguish between genotype and phenotype with an example. ~~ Genotype is genetic make-up, e.g. Tt|1 ~~ Phenotype is outward appearance, e.g. tall|1 ~~ One phenotype can have different genotypes|1
Write the genotype of a pure tall and a pure dwarf pea plant. State the genotype of F1. ~~ Pure tall TT|1 ~~ Pure dwarf tt|1 ~~ F1 Tt|1
State the proportion of tall and dwarf plants in the F2 generation in a monohybrid cross. ~~ Tall 3/4|1 ~~ Dwarf 1/4|1 ~~ Ratio 3 : 1|1
How many types of gametes are produced by TT, Tt and tt? ~~ TT gives only T|1 ~~ Tt gives T and t|1 ~~ tt gives only t|1
What is the importance of variation to a species? ~~ It helps survival in changed conditions|1 ~~ It allows adaptation|1 ~~ It leads to diversity|1
Give three examples of traits that are inherited in humans. ~~ Eye colour|1 ~~ Hair colour|1 ~~ Blood group|1
Explain why the sex of a child cannot depend on the mother. ~~ Mother has two X chromosomes|1 ~~ All her eggs have X|1 ~~ Only the sperm can bring Y|1
How are the chromosomes passed from one generation to the next? ~~ Through gametes|1 ~~ Each parent gives half|1 ~~ Zygote has the full number|1
Why do the children in a family look different from each other? ~~ Each gamete has a different gene combination|1 ~~ Fertilisation combines them differently|1 ~~ So each child is unique|1
What do you understand by the term 'independent assortment'? ~~ Genes for different traits sort separately|1 ~~ This forms new combinations|1 ~~ It is seen in the dihybrid cross|1
What is a Punnett square? ~~ A chart to show crosses|1 ~~ It lists gametes of each parent|1 ~~ It shows possible offspring genotypes|1
State two ways to differentiate a trait that is inherited from one that is acquired. ~~ Inherited traits are in genes|1 ~~ Acquired traits are due to environment or use|1 ~~ Only inherited traits pass to offspring|1
What type of sperm gives a boy and what type gives a girl? ~~ Y-carrying sperm gives a boy|1 ~~ X-carrying sperm gives a girl|1 ~~ Both are equally likely|1
Name the contrasting traits of seed colour and seed shape in pea. ~~ Yellow and green|1 ~~ Round and wrinkled|1 ~~ Yellow and round are dominant|1
Name the type of cross between parents differing in two traits and give the F2 ratio. ~~ Dihybrid cross|1 ~~ F2 ratio is 9 : 3 : 3 : 1|1 ~~ Four types of phenotype|1
""".strip()
eD = """
Explain the monohybrid cross between a tall and a dwarf pea plant. ~~ Parents TT x tt|1 ~~ F1 is Tt, all tall|1 ~~ Gametes of F1 are T and t|1 ~~ F2 has TT, Tt, Tt, tt|1 ~~ Ratio is 3 tall : 1 dwarf|1
Describe the dihybrid cross of round yellow and wrinkled green seeds. ~~ Parents RRYY x rryy|1 ~~ F1 is RrYy round yellow|1 ~~ F2 gives four phenotypes|1 ~~ Ratio 9 : 3 : 3 : 1|1 ~~ New combinations show independent assortment|1
How is sex determined in humans? ~~ Female has XX|1 ~~ Male has XY|1 ~~ Egg has X|1 ~~ Sperm may have X or Y|1 ~~ Boy or girl each have 50% chance|1
What are inherited and acquired traits? Give two examples of each. ~~ Inherited: passed by genes|1 ~~ Acquired: gained during life|1 ~~ Inherited: eye colour, hair colour|1 ~~ Acquired: scar, tan|1 ~~ Acquired traits are not inherited|1
Explain how variation arises in sexual reproduction. ~~ Gametes carry different genes|1 ~~ Fertilisation combines parents' genes|1 ~~ Copying errors occur in DNA|1 ~~ New combinations are formed|1 ~~ Variation helps the species survive|1
Why is the garden pea suitable for Mendel's experiments? Give four reasons. ~~ Many contrasting traits|1 ~~ Short life cycle|1 ~~ Self-pollinating and easy to cross artificially|1 ~~ Produces many seeds|1 ~~ Easy to grow|1
Explain the terms: allele, homozygous, heterozygous, F1, F2. ~~ Allele: alternative form of a gene|1 ~~ Homozygous: same alleles|1 ~~ Heterozygous: different alleles|1 ~~ F1: first filial generation|1 ~~ F2: second filial generation|1
How do chromosomes and genes control the inheritance of traits? ~~ Genes are on chromosomes|1 ~~ Each trait is controlled by a pair of genes|1 ~~ One gene of each pair comes from each parent|1 ~~ Gametes carry one of each pair|1 ~~ Zygote has the full pair|1
Show by a Punnett square that a cross between two heterozygous tall plants gives dwarf plants. ~~ Parents Tt x Tt|1 ~~ Gametes T, t and T, t|1 ~~ Offspring TT, Tt, Tt, tt|1 ~~ tt is dwarf|1 ~~ Dwarf are 25%|1
Explain why the ratios 3 : 1 and 9 : 3 : 3 : 1 are significant. ~~ 3 : 1 shows dominance and segregation|1 ~~ Mendel obtained it in the monohybrid cross|1 ~~ 9 : 3 : 3 : 1 shows independent assortment|1 ~~ These are obtained in dihybrid crosses|1 ~~ They show traits are controlled by factors|1
Describe how the number of chromosomes remains the same in successive generations. ~~ Gametes have half the number|1 ~~ Sperm has 23|1 ~~ Egg has 23|1 ~~ Zygote has 46|1 ~~ So every generation has 46|1
Why do some traits not appear in the F1 generation but appear in the F2? Explain. ~~ F1 has two alleles|1 ~~ Dominant allele masks recessive|1 ~~ Alleles separate in gametes|1 ~~ In F2 two recessives may combine|1 ~~ The recessive trait then appears|1
""".strip()

# ============================ MEDIUM ============================
mA = """
A heterozygous tall plant (Tt) is crossed with a dwarf plant (tt). The fraction of dwarf plants in the offspring is ~~ 1/2 ~~ 1/4 ~~ 3/4 ~~ 0 ~~ Offspring Tt and tt in 1 : 1.
Two tall plants produce 75 tall and 25 dwarf plants. The parents were most likely ~~ both Tt ~~ both TT ~~ TT and Tt ~~ Tt and tt ~~ 3 : 1 ratio arises from Tt x Tt.
Out of 160 F2 plants in a monohybrid cross, the expected number of dwarf plants is ~~ 40 ~~ 120 ~~ 80 ~~ 20 ~~ 1/4 of 160.
Which of the following genotypes will produce only one type of gamete? ~~ TT ~~ Tt ~~ Both TT and Tt ~~ None ~~ Homozygous gives one type.
A plant with genotype RrYy forms how many types of gametes? ~~ 4 ~~ 2 ~~ 8 ~~ 16 ~~ RY, Ry, rY, ry.
In a dihybrid cross, if 144 F2 seeds are obtained, expected round green seeds are ~~ 27 ~~ 81 ~~ 9 ~~ 54 ~~ 3/16 of 144 = 27.
In a dihybrid F2, the proportion of seeds with both recessive traits is ~~ 1/16 ~~ 3/16 ~~ 9/16 ~~ 1/4 ~~ Only rryy.
A cross of RrYy with rryy gives offspring in the ratio ~~ 1 : 1 : 1 : 1 ~~ 9 : 3 : 3 : 1 ~~ 3 : 1 ~~ 1 : 1 ~~ Test cross for two traits.
In the F2 of a dihybrid cross between round yellow and wrinkled green parents, which combination is a new (non-parental) type? ~~ round green ~~ round yellow ~~ wrinkled green ~~ all of these are parental ~~ Round green and wrinkled yellow are new combinations.
Mendel's experiments disproved the idea that ~~ traits of parents blend in offspring ~~ plants have traits ~~ characters can be inherited ~~ pea plants have flowers ~~ Recessive traits reappear intact in F2.

The sex of a baby is determined at the time of ~~ fertilisation ~~ birth ~~ implantation ~~ puberty ~~ The sperm type decides.
A couple already has two daughters. The probability that their third child is a boy is ~~ 1/2 ~~ 1/4 ~~ 1 ~~ 0 ~~ Each birth is independent.
Which of the following statements about sex determination is correct? ~~ Sperm decides the sex ~~ Egg decides the sex ~~ Both eggs and sperm always give girls ~~ Mother's age decides ~~ The father's gamete is X or Y.
If a human sperm has 22 autosomes and the Y chromosome, the number of chromosomes is ~~ 23 ~~ 22 ~~ 46 ~~ 44 ~~ 22 + 1 = 23.
In a human egg, the number of autosomes is ~~ 22 ~~ 23 ~~ 44 ~~ 46 ~~ 22 autosomes plus one X.
Total autosomes in a normal human zygote ~~ 44 ~~ 46 ~~ 22 ~~ 23 ~~ 22 pairs.
Which cell has half the number of chromosomes of a body cell? ~~ Sperm ~~ Skin cell ~~ Muscle cell ~~ Zygote ~~ Gametes are haploid.
A woman with two X chromosomes passes ~~ one X to each child ~~ a Y to sons ~~ both X to daughters ~~ nothing ~~ Her eggs carry one X.
A man passes his X chromosome to ~~ all his daughters ~~ all his sons ~~ none ~~ half of his sons ~~ Daughters receive his X.
A man passes his Y chromosome to ~~ all his sons ~~ all his daughters ~~ none ~~ half of his daughters ~~ Only sons get Y.

A trait that is controlled by a recessive allele appears in a plant when ~~ both alleles are recessive ~~ one allele is recessive ~~ both are dominant ~~ no allele is present ~~ Only tt shows dwarf.
A bacterium reproducing asexually will show variation because of ~~ minor DNA copying errors ~~ gamete fusion ~~ crossing of two parents ~~ meiosis in parents ~~ Copying errors create small differences.
Plants of a clone are grown in different soils and show different heights. This difference is ~~ an acquired trait due to environment ~~ inherited ~~ a mutation of germ cells ~~ dominant ~~ Environment affects the phenotype.
A short plant sprayed with a growth hormone becomes tall. Its offspring will be ~~ short ~~ tall ~~ medium ~~ dwarf only in F1 ~~ The genotype is unchanged.
The expected genotypic ratio of the cross Tt x Tt is ~~ 1 : 2 : 1 ~~ 3 : 1 ~~ 1 : 1 ~~ 9 : 3 : 3 : 1 ~~ TT : Tt : tt.
The probability that offspring of Tt x Tt are heterozygous is ~~ 1/2 ~~ 1/4 ~~ 3/4 ~~ 1 ~~ Tt in the middle, 2 out of 4.
Which cross will always give all tall offspring? ~~ TT x tt ~~ Tt x Tt ~~ Tt x tt ~~ tt x tt ~~ F1 will all be Tt.
In which cross would 50% of the offspring be dwarf? ~~ Tt x tt ~~ TT x tt ~~ Tt x TT ~~ TT x TT ~~ Tt and tt in 1 : 1.
Free earlobe (F) is dominant over attached (f). A child with attached earlobes can be born to parents with ~~ both heterozygous free earlobes ~~ both homozygous free earlobes ~~ FF x ff ~~ FF x Ff ~~ Both must give an f gamete.
Which of the following is an example of a character controlled by a pair of genes? ~~ Seed shape in peas ~~ A scar ~~ A haircut ~~ Language spoken ~~ Mendel's traits are gene controlled.
""".strip()
mB = """
In pea plants, tall (T) is dominant. A tall plant is crossed with a dwarf plant and 50% dwarf offspring result. Find the genotype of the tall parent. ~~ Dwarf offspring need a t allele from the tall parent|1 ~~ Tall parent is Tt|1
Why does a dwarf trait reappear in the F2 generation though absent in the F1? ~~ F1 plants are Tt carrying the t allele|1 ~~ In F2 two t alleles may combine giving tt|1
Why is it impossible for a mother to pass a Y chromosome to her child? ~~ A woman has only X chromosomes (XX)|1 ~~ Her eggs carry only X|1
Out of 400 F2 plants of a monohybrid cross, how many are expected to be homozygous? ~~ Homozygous TT and tt = 1/2|1 ~~ 200 plants|1
If a plant with genotype Rr produces 400 seeds by self-fertilisation, how many wrinkled seeds are expected? ~~ Wrinkled (rr) are 1/4|1 ~~ 100 seeds|1
How does a dihybrid cross show that two traits are inherited independently? ~~ Parental combinations (round yellow, wrinkled green) appear in F2|1 ~~ New combinations (round green, wrinkled yellow) also appear|1
A woman has three daughters and wishes for a son. Explain why her genes cannot be responsible. ~~ Sex depends on the sperm|1 ~~ Her eggs carry only X|1
Distinguish between a homozygous and a heterozygous tall plant by a test cross. ~~ Cross with dwarf (tt)|1 ~~ Homozygous gives all tall, heterozygous gives half dwarf|1
What fraction of the F2 progeny in a dihybrid cross is round (R_)? ~~ Round = 9 + 3 = 12 out of 16|1 ~~ 3/4|1
How can two parents with free earlobes have a child with attached earlobes? ~~ Both parents are heterozygous Ff|1 ~~ The child gets f from each parent: ff|1
Why can a trait disappear in one generation and reappear in the next? ~~ It is recessive and masked in heterozygotes|1 ~~ It appears when homozygous recessive|1
A sperm has 22 + Y. What is the sex of the child it fertilises? ~~ The zygote has XY|1 ~~ The child is a boy|1
""".strip()
mC = """
A tall pea plant is crossed with a dwarf and the F1 are all tall. When the F1 are self-pollinated, 300 plants result. Find the numbers of tall and dwarf plants and the genotypes. ~~ F1 Tt; F2 ratio 3 : 1|1 ~~ Tall = 225, dwarf = 75|1 ~~ Genotypes TT 75, Tt 150, tt 75|1
Show with a Punnett square the cross Rr x Rr for seed shape and give the genotypic and phenotypic ratio. ~~ Gametes R, r and R, r|1 ~~ Offspring RR, Rr, Rr, rr|1 ~~ Genotypic 1 : 2 : 1 and phenotypic 3 round : 1 wrinkled|1
In pea plants, yellow (Y) is dominant to green (y). A yellow plant crossed with a green plant gives 50 yellow and 48 green plants. Find the genotype of the yellow parent. Give the reasoning. ~~ About half the offspring are green|1 ~~ Yellow parent must give y gametes|1 ~~ Yellow parent is Yy|1
Explain why some traits are inherited and some are not, giving a suitable example for each. ~~ Traits coded in germ-cell DNA are inherited, e.g. eye colour|1 ~~ Traits gained during life affect only body cells|1 ~~ These are not inherited, e.g. a scar|1
A woman who has XX gets married to a man with XY. Using a flow chart, state the possible sex of children and the ratio. ~~ Egg: X; sperm: X or Y|1 ~~ XX (girl) and XY (boy)|1 ~~ Ratio 1 : 1|1
How does Mendel's experiment explain that factors for a trait exist as pairs and separate during gamete formation? ~~ F1 hides the recessive factor|1 ~~ F2 shows it again in 1/4|1 ~~ Pairs must separate in gametes and rejoin randomly|1
Calculate the number of seeds of each phenotype expected in the F2 of a dihybrid cross, if 800 seeds are obtained. ~~ Round yellow 9/16 = 450|1 ~~ Round green 3/16 = 150, wrinkled yellow = 150|1 ~~ Wrinkled green 1/16 = 50|1
What is the role of environment in determining traits? Give an example for plants and humans. ~~ Environment can change the phenotype|1 ~~ Plants: a genetically tall plant grows short in poor soil|1 ~~ Humans: tan or body weight depends on conditions|1
Why is the proportion of boys and girls expected to be nearly equal in a large population? ~~ X and Y sperms are produced in equal numbers|1 ~~ Each has the same chance of fertilising the egg|1 ~~ Hence half the children are boys and half girls|1
Differentiate between the monohybrid and dihybrid crosses on the basis of number of characters, F1 and F2 ratios. ~~ Monohybrid: one character; dihybrid: two characters|1 ~~ F2 ratio: 3 : 1 and 9 : 3 : 3 : 1|1 ~~ F1 is all dominant in both|1
If both parents have the heterozygous genotype Rr for a trait, what is the probability that a child is rr? Explain. ~~ Gametes R and r from each parent|1 ~~ Combination rr arises with 1/4 probability|1 ~~ Probability = 25%|1
Explain how DNA gets copied and passed on, and why copying errors matter to heredity. ~~ DNA makes a copy during cell division|1 ~~ The copy is passed to daughter cells and gametes|1 ~~ Errors create new variations|1
What would the F1 look like if Mendel had crossed a pure round yellow plant with a pure wrinkled green plant, according to blending theory? Why was blending theory rejected? ~~ Blending would give intermediate seeds|1 ~~ Mendel found all F1 were round yellow|1 ~~ F2 showed original traits again, rejecting blending|1
A pea plant (Tt) is crossed with another pea plant (Tt). Of 20 offspring, how many will be tall (approx.)? Explain the reasoning behind approximate values. ~~ Expected ratio 3 : 1|1 ~~ Tall about 15, dwarf about 5|1 ~~ The ratio holds well for large numbers of offspring|1
How is a trait expressed from gene to protein? Explain using the example of plant height. ~~ A gene codes for an enzyme|1 ~~ The enzyme helps make the plant growth hormone|1 ~~ Efficient enzyme gives tall, less efficient gives dwarf|1
Describe the contribution of chromosomes of each parent to a child's genetic make-up. ~~ The child gets 23 chromosomes from the mother|1 ~~ 23 from the father|1 ~~ So traits are a mix of both|1
Why do the two daughters of the same parents not look exactly alike? ~~ Every egg and sperm has a different set of genes|1 ~~ The fusion is random|1 ~~ Hence each child is unique|1
Explain why a recessive trait can be present in a person who does not show it. ~~ Person is heterozygous|1 ~~ The dominant allele masks the recessive|1 ~~ The recessive allele may be passed on|1
""".strip()
mD = """
In pea plants, round seed (R) is dominant to wrinkled (r), and yellow (Y) to green (y). A plant RrYy is self-pollinated. Make a Punnett square outline: list gametes, give the F2 phenotypes and the ratio. ~~ Gametes RY, Ry, rY, ry|1 ~~ 16 combinations|1 ~~ 9 round yellow|1 ~~ 3 round green and 3 wrinkled yellow|1 ~~ 1 wrinkled green|1
A pure tall plant with round seeds is crossed with a dwarf plant with wrinkled seeds. Give the genotype of F1 and the number of each phenotype in F2 out of 160 plants. ~~ Parents TTRR x ttrr|1 ~~ F1 is TtRr, tall round|1 ~~ Tall round 90|1 ~~ Tall wrinkled 30 and dwarf round 30|1 ~~ Dwarf wrinkled 10|1
Explain with the help of a cross how a Tt tall plant crossed with a tt plant helps to identify the genotype of an unknown tall plant. ~~ Unknown tall may be TT or Tt|1 ~~ Cross with tt|1 ~~ If TT, all offspring are tall|1 ~~ If Tt, half are dwarf|1 ~~ So the test cross reveals the genotype|1
Explain how the sex of the child is determined and why the number of boys and girls is almost equal. Is the mother responsible for the birth of a girl? ~~ Mother XX produces only X eggs|1 ~~ Father XY produces X and Y sperms equally|1 ~~ X sperm gives a girl and Y sperm gives a boy|1 ~~ Chances are equal for boy and girl|1 ~~ The mother cannot influence it as the father's sperm decides|1
Differentiate between acquired and inherited traits with examples. Explain with an example how a trait acquired by an individual does not get inherited, and why a trait inherited by the sperm may be expressed in the offspring. ~~ Inherited: controlled by genes, passed on|1 ~~ Acquired: gained in life, not passed on|1 ~~ Example: a mouse whose tail is cut, its offspring have normal tails|1 ~~ Germ-cell DNA remains unchanged|1 ~~ A gene for an inherited trait is passed through the gamete|1
Mendel crossed tall pea plants with dwarf plants and recorded the F1 and F2. Explain how he concluded that the factors are particulate and not blending. ~~ F1 plants were all tall|1 ~~ No intermediate height was seen|1 ~~ F2 had tall and dwarf in 3 : 1|1 ~~ Dwarf trait reappeared unchanged|1 ~~ So factors are separate and not blended|1
Explain the terms: genotype, phenotype, dominant, recessive and allele, with the help of the cross Tt x Tt. ~~ Genotypes TT, Tt and tt|1 ~~ Phenotypes tall and dwarf|1 ~~ T is dominant|1 ~~ t is recessive|1 ~~ T and t are alleles|1
In humans, free earlobe (F) is dominant over attached (f). A man with attached earlobes marries a woman with free earlobes whose mother had attached earlobes. Predict the children. ~~ Man is ff|1 ~~ Woman is Ff (her mother gave f)|1 ~~ Offspring Ff and ff|1 ~~ Half free and half attached earlobes|1 ~~ Ratio 1 : 1|1
Explain how variation is inherited and accumulated. Compare the amount of variation in an asexually reproducing organism with that in a sexually reproducing organism. ~~ DNA copying errors cause variations|1 ~~ Daughter cells inherit them|1 ~~ Asexual reproduction gives small variations|1 ~~ Sexual reproduction mixes two sets of genes|1 ~~ So it gives more variation|1
Describe how the chromosome number is maintained from parents to offspring, and how the sex chromosomes of both parents decide the sex. ~~ Body cell 46 chromosomes in 23 pairs|1 ~~ Gametes have 23|1 ~~ Zygote regains 46|1 ~~ 22 pairs are autosomes, one pair sex chromosomes|1 ~~ Mother gives X; father gives X or Y|1
Using a cross, prove that the F2 of a dihybrid cross contains 4 types of phenotypes and 9 types of genotypes. ~~ Gametes: RY, Ry, rY, ry|1 ~~ 16 combinations|1 ~~ 4 phenotypes: round yellow, round green, wrinkled yellow, wrinkled green|1 ~~ 9 genotypes|1 ~~ Ratio 9 : 3 : 3 : 1|1
A pea plant with round yellow seeds is crossed with a plant having wrinkled green seeds and all offspring are round yellow. Give the genotypes and explain. A second cross gives half round yellow and half round green. Give the genotypes. ~~ Cross 1: RRYY x rryy|1 ~~ F1 RrYy all round yellow|1 ~~ Cross 2: RRYy x rryy|1 ~~ Offspring RrYy and Rryy|1 ~~ Round yellow : round green = 1 : 1|1
""".strip()

# ============================ HARD ============================
hA = """
AR ~~ Sex of a child is determined by the father. ~~ Sperms carry either X or Y chromosome. ~~ a ~~ Fusion with X or Y sperm decides the sex.
AR ~~ Acquired traits are not inherited by the next generation. ~~ Changes in body cells do not change the DNA of germ cells. ~~ a ~~ Germ-cell DNA is unchanged, so acquired traits are not passed on.
AR ~~ A recessive trait is not seen in the F1 generation. ~~ The dominant allele masks the recessive allele in heterozygotes. ~~ a ~~ Masking explains absence of the recessive trait.
AR ~~ In a monohybrid cross the F2 genotypic ratio is 1 : 2 : 1. ~~ F1 plants form two kinds of gametes in equal numbers. ~~ a ~~ Equal gametes T and t give TT : Tt : tt = 1 : 2 : 1.
AR ~~ All the gametes of a heterozygous plant are the same. ~~ A heterozygous plant carries two different alleles. ~~ d ~~ A is false: Tt produces T and t gametes; R is true.
AR ~~ Mendel obtained a 9 : 3 : 3 : 1 ratio in the dihybrid cross. ~~ Genes for the two traits are inherited independently. ~~ a ~~ Independent assortment.
AR ~~ A woman is responsible for the birth of a girl child. ~~ Women have two X chromosomes. ~~ d ~~ A is false, sex is decided by the father; R is true.
AR ~~ Variations are important for the survival of species. ~~ They provide a chance to adapt to changing conditions. ~~ a ~~ True explanation.
AR ~~ Children resemble their parents but are not identical. ~~ They inherit genes from both parents in new combinations. ~~ a ~~ Gene combination explains it.
AR ~~ A test cross is carried out with a recessive parent. ~~ Recessive parent produces only one type of gamete. ~~ a ~~ A single gamete type shows F1's gametes.

A pea plant RrYy is crossed with rryy. Out of 200 offspring, the number of round green plants is expected to be ~~ 50 ~~ 100 ~~ 25 ~~ 150 ~~ 1/4 of 200 = 50 (Rryy).
In a cross Tt x Tt, three offspring are tall. The probability that the fourth is dwarf is ~~ 1/4 ~~ 1/2 ~~ 3/4 ~~ 1 ~~ Each birth is independent.
A tall plant is crossed with a dwarf plant; 52 of 100 offspring are tall. The tall parent was ~~ Tt ~~ TT ~~ tt ~~ cannot be determined ~~ 1 : 1 ratio.
A plant of genotype TtRr produces gametes TR, Tr, tR and tr in equal numbers. The probability of a gamete tr is ~~ 1/4 ~~ 1/2 ~~ 1/8 ~~ 1 ~~ Four equally likely types.
For a dihybrid cross, the number of genotypes in the F2 is ~~ 9 ~~ 4 ~~ 16 ~~ 8 ~~ Nine distinct genotypes.
If the F2 of a dihybrid cross has 80 wrinkled green seeds, the total number of seeds is approximately ~~ 1280 ~~ 80 ~~ 720 ~~ 960 ~~ 1/16 of total = 80, total = 1280.
A true-breeding tall plant is crossed with a dwarf plant. The F2 has 1200 plants. The number of heterozygous tall plants is ~~ 600 ~~ 300 ~~ 900 ~~ 1200 ~~ Half of F2 are Tt.
The probability that a couple's four children are all girls is ~~ 1/16 ~~ 1/4 ~~ 1/8 ~~ 1/2 ~~ (1/2)^4.
Of the children of a couple, which parent's chromosome decides that a son carries a Y? ~~ Father ~~ Mother ~~ Both ~~ Neither ~~ Y comes from the father.
A father passes the same sex chromosome to all his sons. It is the ~~ Y chromosome ~~ X chromosome ~~ both X and Y ~~ none ~~ Sons are XY and get Y from the father.

A pea plant that is tall and round (TtRr) is crossed with dwarf wrinkled (ttrr). The offspring ratio is ~~ 1 : 1 : 1 : 1 ~~ 9 : 3 : 3 : 1 ~~ 3 : 1 ~~ 1 : 1 ~~ Four gamete types x one.
In pea plants F2 seeds show round-green and wrinkled-yellow types that were absent in both parents. This happens due to ~~ new combinations of independently inherited genes ~~ blending of traits ~~ acquired traits ~~ loss of genes in F1 ~~ Independent assortment gives new combinations.
A farmer saves seeds from tall plants raised in good soil. The next generation is grown in poor soil and is short. This shows ~~ environment affects expression of the trait ~~ tall is recessive ~~ genes were lost ~~ blending ~~ Phenotype depends on environment.
A woman is XX and her husband is XY; their son has a disease on his X. From whom did he get the X? ~~ Mother ~~ Father ~~ Both ~~ Neither ~~ Sons get the Y from the father.
Two parents have free earlobes. Their first child has attached earlobes. For the second child, the probability of attached earlobes is ~~ 1/4 ~~ 1/2 ~~ 3/4 ~~ 0 ~~ Both parents are Ff.
Mendel's work was not recognised for many years chiefly because ~~ it was ahead of the knowledge of chromosomes and genes ~~ he used mice ~~ it was in a foreign language ~~ the traits were not clear ~~ The genetic basis was unknown then.
The number of chromosomes in a human sperm is 23 and in the egg is 23. In a normal human zygote and a skin cell, the numbers are respectively ~~ 46 and 46 ~~ 23 and 46 ~~ 46 and 23 ~~ 23 and 23 ~~ Both are diploid.
A population of asexually reproducing bacteria shows less variation than a population of humans because ~~ there is only one parent and only copying errors ~~ bacteria have no DNA ~~ humans have no mutation ~~ sexual reproduction reduces variation ~~ Single parent, little variation.
A plant with TtRr genotype is self-pollinated. The probability of an offspring being dwarf and wrinkled is ~~ 1/16 ~~ 3/16 ~~ 9/16 ~~ 1/4 ~~ ttrr.
The gene for a protein that makes a plant growth hormone is defective. The plant will likely be ~~ dwarf ~~ tall ~~ unchanged ~~ colourless ~~ Less hormone leads to a short plant.
""".strip()
hB = """
In a cross of two heterozygous tall plants (Tt x Tt), 240 plants were produced. Find the number of tall plants that are homozygous. ~~ TT fraction = 1/4|1 ~~ 60 plants|1
A tall plant when crossed with a dwarf plant gives 30 tall and 28 dwarf plants. Give the genotypes of the parents. ~~ Ratio about 1 : 1|1 ~~ Tall parent Tt, dwarf parent tt|1
A black-coated animal (B dominant) and a brown-coated (bb) mate and produce all black offspring. What are the genotypes of the parents? ~~ All offspring are black, so the black parent has only B|1 ~~ Black parent BB, brown parent bb|1
Find the probability that a child is a girl if the father's sperm carries a Y chromosome. ~~ Y sperm gives XY|1 ~~ Probability is 0 (the child is a boy)|1
Explain the reason a plant with 'Tt' genotype shows only the tall phenotype. ~~ T is dominant over t|1 ~~ The tall allele masks the dwarf allele|1
A dihybrid cross gives 9 : 3 : 3 : 1. What fraction of F2 seeds is different from the two parental types? ~~ New types: round green (3) and wrinkled yellow (3)|1 ~~ 6/16 = 3/8|1
Two daughters of the same parents both receive the father's X chromosome but may differ in other traits. Why? ~~ Each gets one of the mother's two different X chromosomes|1 ~~ Autosomes also combine differently in each gamete|1
How many types of gametes will be produced by TtRrYy? Show the reasoning. ~~ Each heterozygous gene gives 2 types|1 ~~ 2 x 2 x 2 = 8 types|1
A man with attached earlobes (ff) and a woman with free (Ff) have 4 children. Expected number with attached earlobes? ~~ Ff x ff gives 1 : 1|1 ~~ 2 children|1
Out of 640 F2 seeds in a dihybrid cross, how many are expected to be wrinkled yellow? ~~ Wrinkled yellow = 3/16|1 ~~ 3/16 x 640 = 120|1
If both parents are TT and tt, what is the probability that the F2 is tt? Explain. ~~ F1 is Tt|1 ~~ F2 tt probability is 1/4|1
Why can't an individual with recessive phenotype be heterozygous? ~~ Recessive trait shows only when both alleles are recessive|1 ~~ So the genotype has to be homozygous recessive|1
""".strip()
hC = """
A pea plant has yellow round seeds. How would you find its genotype? Describe the cross and the possible results. ~~ Cross with green wrinkled (yyrr)|1 ~~ All yellow round offspring means YYRR|1 ~~ Other phenotypes in offspring mean the plant is heterozygous|1
A couple has three sons. What is the probability that the fourth child is a girl? Explain how the answer is obtained. ~~ Each pregnancy is independent|1 ~~ X and Y sperm are equally likely|1 ~~ Probability = 1/2|1
A cross between two plants gives tall and dwarf offspring in a 3 : 1 ratio. Identify the genotypes of the parents and the offspring. ~~ Parents are both Tt|1 ~~ Offspring TT, Tt, Tt, tt|1 ~~ Tall 3 : dwarf 1|1
The F1 of a dihybrid cross RrYy is test-crossed. Give the genotypes and phenotypes of the offspring. ~~ Test parent is rryy|1 ~~ Offspring RrYy, Rryy, rrYy, rryy|1 ~~ Round yellow, round green, wrinkled yellow, wrinkled green in 1 : 1 : 1 : 1|1
Explain the fallacy in the statement: A man who exercises regularly will have sons with strong muscles. ~~ Muscle strength gained by exercise is an acquired trait|1 ~~ It does not change the DNA of the sperm|1 ~~ So it will not be inherited|1
Why is the chance of the first child being a boy the same as the chance of the second child being a boy? ~~ Each child is a separate fertilisation|1 ~~ X and Y sperm are equally likely each time|1 ~~ Previous births do not affect the next|1
How many chromosomes does each of the following have in humans: sperm, egg, zygote, liver cell? What is the number of autosomes in each? ~~ Sperm 23 (22 autosomes)|1 ~~ Egg 23 (22 autosomes); zygote 46 (44 autosomes)|1 ~~ Liver cell 46 (44 autosomes)|1
In a population of beetles, a green colour variant arises through a DNA copying error. Birds eat red beetles more. Explain what happens to the proportion of green beetles over generations. ~~ Green beetles are less easily seen|1 ~~ They survive and reproduce more|1 ~~ The proportion of green beetles increases|1
In pea plants, a gene produces an enzyme that makes a growth hormone. A mutation reduces the efficiency of the enzyme. Predict the phenotype and the effect of giving the hormone externally. ~~ Less hormone, so dwarf plant|1 ~~ Giving the hormone makes it taller|1 ~~ The offspring still inherit the dwarf allele|1
Describe how Mendel's use of statistical counting helped him discover the laws of inheritance. ~~ He counted a large number of plants in each generation|1 ~~ Ratios such as 3 : 1 appeared|1 ~~ Ratios led to the idea of dominant and recessive factors|1
A tall plant (Tt) is self-pollinated and gives 4 offspring. Can we say one will be dwarf? Explain. ~~ The ratio 3 : 1 is a probability|1 ~~ Small numbers may not show the ratio|1 ~~ It appears in a large number of offspring|1
Study the statement: Mendel's F1 had no dwarf plants, so the dwarf trait was lost. Evaluate. ~~ Dwarf allele was only masked in Tt|1 ~~ F2 showed dwarf plants again|1 ~~ So it was not lost|1
Explain why every egg of a woman carries an X chromosome, though she has two X chromosomes. ~~ A woman has two X chromosomes (XX)|1 ~~ Each egg receives only one of them|1 ~~ So each egg has one X and 22 autosomes|1
Why is it possible for two brown-eyed parents to have a blue-eyed child, if blue is recessive? ~~ Both parents are heterozygous|1 ~~ Each passes the recessive allele|1 ~~ The child is homozygous recessive|1
Compare dominant and recessive alleles in terms of their expression in homozygous and heterozygous states. ~~ Homozygous dominant: dominant trait|1 ~~ Heterozygous: dominant trait|1 ~~ Homozygous recessive: recessive trait|1
If all F1 plants in a cross of two plants are tall, what can be concluded about the parents? ~~ At least one parent is homozygous dominant|1 ~~ The other can be TT or tt|1 ~~ Tall allele is dominant|1
What is the effect of the environment on a person's height even if the genes for height are the same? ~~ Nutrition affects growth|1 ~~ Good diet and health can increase height|1 ~~ Genes set the potential only|1
A sperm contains 22 autosomes and X. Name the sex of the child and explain how the child gets its other sex chromosome. ~~ Child is a girl|1 ~~ Egg gives an X|1 ~~ Zygote is XX|1
""".strip()
hD = """
A pea plant homozygous for tall and round seeds is crossed with a dwarf plant having wrinkled seeds. Show the F1 and the F2 with the number of each phenotype in 1600 F2 plants, and the genotype of the dwarf round plants. ~~ F1: TtRr, tall round|1 ~~ F2 ratio 9 : 3 : 3 : 1|1 ~~ Tall round 900, tall wrinkled 300|1 ~~ Dwarf round 300, dwarf wrinkled 100|1 ~~ Dwarf round genotypes ttRR and ttRr|1
A tall plant with round seeds (TtRr) is crossed with a dwarf plant with round seeds (ttRr). Find the expected phenotypic ratio of the offspring. ~~ Tt x tt gives 1 tall : 1 dwarf|1 ~~ Rr x Rr gives 3 round : 1 wrinkled|1 ~~ Combine the independent ratios|1 ~~ Tall round 3, tall wrinkled 1, dwarf round 3, dwarf wrinkled 1|1 ~~ Ratio 3 : 1 : 3 : 1|1
Analyse the pedigree: both parents have free earlobes; of their four children, one has attached earlobes. Deduce the genotypes of the parents and children and the probability that the next child has free earlobes. ~~ Attached is recessive (ff)|1 ~~ Both parents must be Ff|1 ~~ Children: FF, Ff, Ff, ff possible|1 ~~ Probability of free earlobes = 3/4|1 ~~ Probability of attached = 1/4|1
A woman is told that she will have a boy as she has two daughters already. Evaluate the statement with respect to chromosomes, and also comment on the contribution of father and mother to the sex of the child. ~~ Each birth is an independent event|1 ~~ Probability of a boy is always 1/2|1 ~~ Eggs have X only|1 ~~ Sperm may have X or Y|1 ~~ Father's sperm decides the sex, not the mother|1
In a dihybrid cross of RrYy x RrYy, find (a) the fraction of seeds that are round yellow, (b) the fraction that are homozygous for both genes, and (c) the fraction that are both heterozygous. ~~ (a) Round yellow = 9/16|1 ~~ (b) RRYY, RRyy, rrYY, rryy|1 ~~ Each = 1/16 so 4/16 = 1/4|1 ~~ (c) RrYy = 2/4 x 2/4 = 1/4|1 ~~ Verify totals add to 16|1
Explain how Mendel's experiments and the idea of genes on chromosomes together explain why the F2 of a dihybrid cross has a 9 : 3 : 3 : 1 ratio. ~~ Genes for shape and colour are on different chromosomes|1 ~~ Alleles of each gene separate into gametes|1 ~~ Four gamete types in equal numbers|1 ~~ 16 random combinations|1 ~~ 9 : 3 : 3 : 1 ratio results|1
Two pea plants, both tall, produce offspring of which one-fourth are dwarf. A third tall plant crossed with a dwarf plant gives all tall offspring. Deduce the genotype of each of the three tall plants and justify. ~~ First two plants: dwarf offspring means each has t|1 ~~ 1/4 dwarf shows both are Tt|1 ~~ Third plant crossed with tt gives all tall|1 ~~ So it must be TT|1 ~~ If it were Tt, half would be dwarf|1
Discuss the sources of variation in a sexually reproducing population and show how variation can be useful for the species, by giving a human example. ~~ DNA copying errors|1 ~~ Random fusion of gametes|1 ~~ Independent assortment of genes|1 ~~ Variation helps in adapting|1 ~~ Example: people with different skin tones or blood groups|1
If a human sperm contains 22 autosomes and one sex chromosome, and an egg has 22 autosomes and X, find the possible chromosome composition of the zygotes and the sex of the child. State why the child is a mixture of both parents. ~~ Egg: 22 + X|1 ~~ Sperm: 22 + X or 22 + Y|1 ~~ Zygote: 44 + XX (girl) or 44 + XY (boy)|1 ~~ Half chromosomes from each parent|1 ~~ So child shows traits of both parents|1
A student crosses RrYy with rryy and gets 52 round yellow, 48 round green, 51 wrinkled yellow and 49 wrinkled green. Give the ratio and conclude what it shows about the parental genotype and the gene inheritance. ~~ Ratio close to 1 : 1 : 1 : 1|1 ~~ Parent RrYy forms four types of gametes|1 ~~ In equal proportion|1 ~~ Genes are inherited independently|1 ~~ Test parent rryy gives only ry|1
Describe how the knowledge of heredity is used to explain why an organism that has the same DNA as its clone-mate can look different. ~~ Genotype is the same|1 ~~ Environment affects the expression|1 ~~ Differences in nutrition or sunlight|1 ~~ The phenotype therefore varies|1 ~~ Such differences are not inherited|1
In humans, Rh positive is dominant over Rh negative. A heterozygous woman marries a Rh negative man. Show the possible children with their genotypes, phenotypes and the probability of each. ~~ Woman Rr, man rr|1 ~~ Gametes R, r and r|1 ~~ Children Rr and rr|1 ~~ Rr (positive) 1/2|1 ~~ rr (negative) 1/2|1
""".strip()

TIERS = {"NCERT": tier(nA, nB, nC, nD), "Easy": tier(eA, eB, eC, eD), "Medium": tier(mA, mB, mC, mD), "Hard": tier(hA, hB, hC, hD)}
