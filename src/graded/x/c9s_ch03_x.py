"""Class 9 Science Ch 3 The Atomic Foundations of Matter - extras. Atomic masses (u): H 1, C 12, N 14, O 16, Na 23, S 32, Cl 35.5, Ca 40."""
from common import AR4, Q

AR = [
 AR4("The total mass of the products equals the total mass of the reactants in a chemical reaction carried out in a closed vessel.", "Atoms are neither created nor destroyed in a chemical reaction; they are only rearranged.", "a",
     "Since the number and kind of atoms stay the same, the total mass is conserved."),
 AR4("In water, hydrogen and oxygen are always present in the fixed mass ratio 1 : 8.", "Water is a compound of hydrogen and oxygen.", "b",
     "Both are true, but the fixed ratio is explained by the law of constant proportions, not just by water being a compound."),
 AR4("The chemical formula of aluminium oxide is $\\ce{Al2O3}$.", "Aluminium has valency 2 and oxygen has valency 3.", "c",
     "Aluminium has valency 3 and oxygen has valency 2, so criss-crossing gives $\\ce{Al2O3}$; R is false."),
 AR4("Sodium chloride exists as separate $\\ce{NaCl}$ molecules.", "Ionic compounds consist of oppositely charged ions held together by electrostatic forces.", "d",
     "NaCl is a crystal lattice of $\\ce{Na+}$ and $\\ce{Cl-}$ ions, not discrete molecules, so A is false; R is true."),
 AR4("The atomicity of ozone is 3.", "A molecule of ozone is made up of three oxygen atoms.", "a",
     "Atomicity is the number of atoms in a molecule; ozone is $\\ce{O3}$."),
 AR4("The molecular mass of water is 18 u.", "The atomic mass of an element is expressed in the unified atomic mass unit (u).", "b",
     "$2(1)+16=18$ u; both statements are true but R does not explain the value 18."),
]

CASE = [
 Q("<b>Case study.</b> In a school laboratory, 10 g of calcium carbonate is heated strongly in a closed hard-glass tube fitted with a gas collector. It decomposes: $\\ce{CaCO3 -> CaO + CO2}$. The solid residue (calcium oxide) weighs 5.6 g. "
   "(i) State the law of conservation of mass. (ii) Find the mass of carbon dioxide formed. (iii) Who proposed this law? (iv) Another student heats the same carbonate in an open dish and finds that the residue is lighter than 10 g. Does this violate the law? Explain.",
   "(i) In a chemical reaction the total mass of the reactants equals the total mass of the products (mass is neither created nor destroyed) (1). (ii) $10-5.6=4.4$ g (1). (iii) Antoine Lavoisier (1). (iv) No (1); carbon dioxide escapes into the air from the open dish, and if its mass is included the total mass stays 10 g (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Two samples of water, one from a well in Pune and one from a river in Kerala, are decomposed. In each, hydrogen and oxygen are found in the mass ratio 1 : 8. A 27 g sample of water is then decomposed in the laboratory. "
   "(i) Which law is illustrated by the identical ratio in both samples? (ii) What fraction of the mass of water is hydrogen? (iii) Find the mass of hydrogen in the 27 g sample. (iv) Find the mass of oxygen obtained and say what the ratio would be in a sample made in a factory.",
   r"(i) Law of constant proportions (Proust) (1). (ii) $\dfrac{1}{9}$ (1). (iii) $27\times\dfrac19=3$ g (1). (iv) Oxygen $=27\times\dfrac89=24$ g (1); the ratio would again be 1 : 8 because a compound has fixed composition whatever its source (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A farmer in Punjab reads three labels: calcium carbonate $\\ce{CaCO3}$ (liming agent), sodium chloride $\\ce{NaCl}$, and ammonium sulphate $\\ce{(NH4)2SO4}$ (fertiliser). Atomic masses: H 1, C 12, N 14, O 16, S 32, Ca 40. "
   "(i) Find the formula unit mass of $\\ce{CaCO3}$. (ii) How many atoms are present in one formula unit of $\\ce{(NH4)2SO4}$? (iii) Find the formula unit mass of $\\ce{(NH4)2SO4}$. (iv) Find the percentage of nitrogen in $\\ce{(NH4)2SO4}$ (to one decimal place).",
   r"(i) $40+12+3(16)=100$ u (1). (ii) N: 2, H: 8, S: 1, O: 4, total 15 atoms (1). (iii) $2(14+4)+32+64=36+96=132$ u (1). (iv) $\dfrac{28}{132}\times100=21.2\%$ (1) with mass of N = $2\times14=28$ u (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Laws of chemical combination", ["Law of conservation of mass (Lavoisier): total mass of reactants = total mass of products.",
   "Law of constant proportions (Proust): a pure compound always contains the same elements in the same fixed mass ratio. In water $\\ce{H}:\\ce{O}=1:8$ by mass; in $\\ce{CO2}$ $\\ce{C}:\\ce{O}=3:8$.",
   "Dalton: matter is made of indivisible atoms; atoms of one element are identical; atoms combine in simple whole-number ratios; atoms are neither created nor destroyed in a reaction."]),
 ("Atoms, ions and molecules", ["Atomic mass unit: $1\\text{ u}=\\dfrac{1}{12}$ of the mass of one carbon-12 atom.",
   "Molecule: two or more atoms bonded together (e.g. $\\ce{O2}$, $\\ce{H2O}$). Atomicity = number of atoms in a molecule: $\\ce{He}$ 1, $\\ce{O2}$ 2, $\\ce{O3}$ 3, $\\ce{P4}$ 4, $\\ce{S8}$ 8.",
   "Ion: charged atom or group of atoms. Cation (positive), anion (negative); examples: $\\ce{Na+}$, $\\ce{Ca^{2+}}$, $\\ce{Cl-}$, $\\ce{SO4^{2-}}$, $\\ce{OH-}$, $\\ce{NH4+}$."]),
 ("Writing chemical formulae", ["Write symbols with the cation first, write valencies, then criss-cross them and reduce to the simplest ratio.",
   "Examples: $\\ce{Al^{3+}}$ and $\\ce{O^{2-}}\\rightarrow\\ce{Al2O3}$; $\\ce{Ca^{2+}}$ and $\\ce{OH-}\\rightarrow\\ce{Ca(OH)2}$; $\\ce{Na+}$ and $\\ce{SO4^{2-}}\\rightarrow\\ce{Na2SO4}$.",
   "Use brackets for polyatomic ions when more than one is needed, e.g. $\\ce{(NH4)2SO4}$."]),
 ("Masses", ["Molecular mass = sum of the atomic masses of all atoms in the molecule: $\\ce{H2O}=18$ u, $\\ce{CO2}=44$ u, $\\ce{O2}=32$ u.",
   "Formula unit mass (ionic compounds) = sum of atomic masses in the formula unit: $\\ce{NaCl}=58.5$ u, $\\ce{CaCO3}=100$ u, $\\ce{Al2O3}=102$ u.",
   "Mass per cent of an element $=\\dfrac{\\text{mass of the element in one formula}}{\\text{molecular or formula mass}}\\times100$."]),
 ("Ionic and molecular compounds", ["Ionic compounds (e.g. $\\ce{NaCl}$): crystalline solids, high melting points, conduct when molten or dissolved.",
   "Molecular compounds (e.g. $\\ce{CCl4}$, $\\ce{HCl}$): low melting and boiling points, mostly gases or liquids."]),
]

MISTAKES = [
 "Treating the subscript in a formula as the valency, or forgetting to reduce criss-crossed numbers to the simplest ratio (writing $\\ce{Ca2O2}$ for calcium oxide).",
 "Writing $\\ce{FeO3}$ or $\\ce{Al3O2}$ by swapping the wrong numbers; remember to criss-cross <i>valencies</i> (charges) and put the cation first.",
 "Forgetting the bracket when a polyatomic ion occurs more than once: $\\ce{Ca(OH)2}$, not $\\ce{CaOH2}$.",
 "Mixing atomicity with number of molecules: $\\ce{3O2}$ means three molecules, six atoms; $\\ce{O3}$ is one molecule of ozone.",
 "Adding the atomic mass of an element only once when the formula has a subscript or bracket (e.g. $\\ce{(NH4)2SO4}$: N counted twice, H eight times).",
 "Calling $\\ce{NaCl}$ a 'molecule' and giving it a 'molecular mass'; for ionic compounds use formula unit mass.",
]
