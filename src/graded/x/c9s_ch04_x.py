"""Class 9 Science Ch 4 Journey Inside the Atom - extras."""
from common import AR4, Q

AR = [
 AR4("In Rutherford's experiment most alpha particles passed straight through the gold foil.", "Most of the space inside an atom is empty.", "a",
     "Alpha particles pass through the empty space and are deflected only when they come close to the tiny nucleus."),
 AR4("Rutherford's nuclear model could not explain the stability of the atom.", "The neutron was discovered by James Chadwick in 1932.", "b",
     "Both are true, but the discovery of the neutron is not the reason for the model's failure (a revolving electron should lose energy and spiral into the nucleus)."),
 AR4("The mass number of an atom equals the number of protons plus the number of neutrons.", "Electrons contribute most of the mass of an atom.", "c",
     "A is true; electrons are about 1/1836 of the mass of a proton, so R is false."),
 AR4("A single chlorine atom has a mass of exactly 35.5 u.", "Naturally occurring chlorine is a mixture of the isotopes $\\ce{^{35}Cl}$ and $\\ce{^{37}Cl}$.", "d",
     "35.5 u is the average atomic mass; individual atoms have mass number 35 or 37, so A is false; R is true."),
 AR4("Neon (atomic number 10) is chemically inert.", "Its outermost shell is completely filled with 8 electrons.", "a",
     "A filled octet gives a stable configuration with valency zero."),
 AR4("Isotopes of an element have the same chemical properties.", "Isotopes of an element have different mass numbers.", "b",
     "Both are true; the chemical properties are the same because the number of electrons is the same, not because of the mass numbers."),
]

CASE = [
 Q("<b>Case study.</b> An atom of an element X has 11 protons and 12 neutrons. Meena is asked to describe it using what she has learnt about atomic structure. "
   "(i) Find the atomic number and the mass number of X. (ii) Write its electronic configuration. (iii) What is its valency? (iv) What happens to the electronic configuration when the atom forms an ion of valency 1, and how many electrons does the ion have?",
   "(i) Atomic number = number of protons = 11; mass number = 11 + 12 = 23 (1). (ii) 2, 8, 1 (1). (iii) Valency = 1 (it has 1 valence electron) (1). (iv) The atom loses its one outer electron (1) to give $\\ce{X+}$ with 10 electrons and configuration 2, 8 (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Boron occurs naturally as two isotopes: boron-10 (20 per cent) and boron-11 (80 per cent). Both have atomic number 5. A student has to find the average atomic mass of boron and explain why the two isotopes behave alike chemically. "
   "(i) What are isotopes? (ii) Find the number of neutrons in each isotope. (iii) Find the average atomic mass of boron. (iv) Why do isotopes have the same chemical properties, and name one use of a radioactive isotope?",
   r"(i) Atoms of the same element with the same atomic number but different mass numbers (1). (ii) Boron-10: $10-5=5$ neutrons; boron-11: $11-5=6$ neutrons (1). (iii) $0.20\times10+0.80\times11=2+8.8=10.8$ u (1). (iv) They have the same number of electrons and the same electronic configuration (1); use: cobalt-60 for cancer treatment, iodine-131 for thyroid, carbon-14 dating (any one) (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In a historic experiment a thin gold foil was bombarded with fast-moving alpha particles. Most particles passed straight through, a small number were deflected through small angles, and very few rebounded almost straight back. "
   "(i) Name the scientist who performed this experiment. (ii) What did the passage of most particles show? (iii) What did the large deflection of a few particles show about the charge on the centre of the atom? (iv) State two conclusions about the nucleus drawn from the experiment.",
   "(i) Ernest Rutherford (with Geiger and Marsden) (1). (ii) Most of the atom is empty space (1). (iii) The centre is positively charged, since positive alpha particles were repelled (1). (iv) Any two: the nucleus is very small compared with the atom; it is very dense and holds nearly all the mass; it is positively charged; electrons move around it (1+1).", "1+1+1+2"),
]

FORMULAS = [
 ("Sub-atomic particles", ["Electron (J. J. Thomson): charge $-1$, mass $\\approx\\dfrac{1}{1836}$ u (negligible). Proton (Rutherford/Goldstein): charge $+1$, mass 1 u. Neutron (Chadwick, 1932): no charge, mass 1 u.",
   "Neutral atom: number of protons = number of electrons. Nucleus holds the protons and neutrons (nucleons)."]),
 ("Atomic number and mass number", ["Atomic number $Z$ = number of protons.",
   "Mass number $A$ = protons + neutrons; number of neutrons $=A-Z$.",
   "Notation: $\\ce{^{A}_{Z}X}$, e.g. $\\ce{^{23}_{11}Na}$ has 11 protons, 11 electrons, 12 neutrons."]),
 ("Electronic configuration", ["Bohr's model: electrons revolve in fixed orbits (shells) K, L, M, N without radiating energy; energy changes only when an electron jumps between shells.",
   "Maximum electrons in shell $n$: $2n^2$ ($K=2$, $L=8$, $M=18$); the outermost shell holds at most 8 electrons (2 for K).",
   "Examples: Li 2, 1; N 2, 5; Na 2, 8, 1; Ca 2, 8, 8, 2."]),
 ("Valency", ["Valency = number of electrons an atom gains, loses or shares to complete its outer shell (octet or duet).",
   "Valence electrons $\\le4$: valency = number of valence electrons (Na 1, Mg 2, Al 3). More than 4: valency $=8-$ valence electrons (N 3, O 2, F 1).",
   "Noble gases (He, Ne, Ar) have complete outer shells and valency 0."]),
 ("Isotopes and isobars", ["Isotopes: same $Z$, different $A$ (e.g. $\\ce{^{35}Cl}$ and $\\ce{^{37}Cl}$, protium, deuterium, tritium).",
   "Isobars: same $A$, different $Z$ (e.g. $\\ce{^{40}Ca}$ and $\\ce{^{40}Ar}$).",
   "Average atomic mass $=\\sum(\\text{mass}\\times\\text{fraction of abundance})$; for Cl: $0.75\\times35+0.25\\times37=35.5$ u."]),
]

MISTAKES = [
 "Confusing atomic number with mass number, or finding neutrons as $A+Z$ instead of $A-Z$.",
 "Filling the M shell with 18 electrons for elements up to calcium; the outer shell cannot hold more than 8, so Ca is 2, 8, 8, 2 and not 2, 8, 10.",
 "Taking the valency of an element like nitrogen (2, 5) as 5 instead of $8-5=3$.",
 "Saying that isotopes differ in the number of protons or electrons; they differ only in the number of neutrons.",
 "Assuming the atomic mass of chlorine is a whole number or that every chlorine atom weighs 35.5 u; it is a weighted average of isotopes.",
 "Attributing the discovery of the nucleus to Thomson, or the neutron to Rutherford (nucleus: Rutherford; neutron: Chadwick; electron: Thomson).",
]
