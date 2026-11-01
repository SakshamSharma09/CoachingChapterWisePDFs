from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def fm(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}".rstrip("0").rstrip(".")
A = []
# molecular / formula unit mass (8)
for nm, fx, m, why in [("water, $\\ce{H2O}$", "u", 18, "2×1 + 16"), ("carbon dioxide, $\\ce{CO2}$", "u", 44, "12 + 2×16"), ("ammonia, $\\ce{NH3}$", "u", 17, "14 + 3×1"),
                       ("sulfuric acid, $\\ce{H2SO4}$", "u", 98, "2 + 32 + 64"), ("hydrogen chloride, $\\ce{HCl}$", "u", F(73, 2), "1 + 35.5"),
                       ("sodium chloride, $\\ce{NaCl}$ (formula unit mass)", "u", F(117, 2), "23 + 35.5"), ("calcium carbonate, $\\ce{CaCO3}$ (formula unit mass)", "u", 100, "40 + 12 + 48"),
                       ("magnesium chloride, $\\ce{MgCl2}$ (formula unit mass)", "u", 95, "24 + 71")]:
    w = [x for x in dict.fromkeys([m + 2, m - 2, m * 2, m + 10, m - 10]) if x != m][:3]
    A.append(M4(f"The molecular/formula unit mass of {nm} is (H = 1, C = 12, N = 14, O = 16, Na = 23, Mg = 24, S = 32, Cl = 35.5, Ca = 40):", f"{fm(m)} u", [f"{fm(x)} u" for x in w], why))
# conservation of mass (3)
for r1, r2, p1 in [(4.0, 2.92, 6.92), (12, 32, 44), (8, 2, 10)]:
    pass
A += [
 M4("4.0 g of CaCO$_3$ reacts with 2.92 g of HCl in a closed vessel. If 1.76 g CO$_2$ and 0.72 g H$_2$O are formed, the mass of CaCl$_2$ formed is:", "4.44 g", ["4.04 g", "5.44 g", "6.92 g"], "6.92 − (1.76 + 0.72) = 4.44 g"),
 M4("12 g of carbon burns in 32 g of oxygen. The mass of carbon dioxide formed is:", "44 g", ["20 g", "32 g", "12 g"], "mass is conserved"),
 M4("If 2.4 g of carbon reacts completely with oxygen (C : O = 12 : 32), the mass of CO$_2$ formed is:", "8.8 g", ["4.4 g", "6.2 g", "10.4 g"], "$\\frac{44}{12}\\times2.4=8.8$"),
 M4("Water always contains hydrogen and oxygen in the mass ratio:", "1 : 8", ["1 : 1", "8 : 1", "2 : 1"], "Law of constant proportions"),
 M4("On decomposing 18 g of pure water, the masses of hydrogen and oxygen obtained are:", "2 g and 16 g", ["1 g and 17 g", "9 g and 9 g", "4 g and 14 g"], "1 : 8 by mass"),
 M4("In NaCl, Na : Cl is 23 : 35.5 by mass. 46 g of sodium needs how much chlorine?", "71 g", ["35.5 g", "46 g", "92 g"], "$\\frac{35.5}{23}\\times46=71$"),
 M4("Carbon monoxide has C : O = 3 : 4. The mass of oxygen that combines with 9 g carbon is:", "12 g", ["9 g", "6 g", "16 g"], "$\\frac43\\times9=12$"),
]
# formulae (5)
for nm, fx, why in [("aluminium oxide", r"$\ce{Al2O3}$", "Al³⁺ and O²⁻ cross over"), ("calcium chloride", r"$\ce{CaCl2}$", "Ca²⁺ and 2 Cl⁻"), ("sodium sulfate", r"$\ce{Na2SO4}$", "2 Na⁺ and SO₄²⁻"),
                    ("magnesium oxide", r"$\ce{MgO}$", "Mg²⁺ and O²⁻"), ("calcium carbonate", r"$\ce{CaCO3}$", "Ca²⁺ and CO₃²⁻")]:
    pool = [r"$\ce{Al2O3}$", r"$\ce{CaCl2}$", r"$\ce{Na2SO4}$", r"$\ce{MgO}$", r"$\ce{CaCO3}$", r"$\ce{Al3O2}$", r"$\ce{CaCl}$", r"$\ce{NaSO4}$", r"$\ce{Mg2O}$", r"$\ce{Ca2CO3}$", r"$\ce{AlO}$", r"$\ce{Ca2Cl}$"]
    wr = {"aluminium oxide": [r"$\ce{Al3O2}$", r"$\ce{AlO}$", r"$\ce{Al2O}$"], "calcium chloride": [r"$\ce{CaCl}$", r"$\ce{Ca2Cl}$", r"$\ce{Ca2Cl2}$"], "sodium sulfate": [r"$\ce{NaSO4}$", r"$\ce{Na2S}$", r"$\ce{Na(SO4)2}$"],
          "magnesium oxide": [r"$\ce{Mg2O}$", r"$\ce{MgO2}$", r"$\ce{Mg2O2}$"], "calcium carbonate": [r"$\ce{Ca2CO3}$", r"$\ce{CaC2O3}$", r"$\ce{Ca(CO3)2}$"]}[nm]
    A.append(M4(f"The chemical formula of {nm} is:", fx, wr, why))
# naming (4)
for fx, nm, ws in [(r"$\ce{CS2}$", "carbon disulfide", ["monocarbon disulfide", "carbon sulfur two", "carbon sulfide"]), (r"$\ce{N2O4}$", "dinitrogen tetroxide", ["dinitrogen tetraoxide", "nitrogen oxide", "nitrogen tetroxide(II)"]),
                   (r"$\ce{PCl3}$", "phosphorus trichloride", ["phosphorus chloride", "monophosphorus trichloride", "phosphoric chloride"]), (r"$\ce{SF6}$", "sulfur hexafluoride", ["sulfur hexafluorine", "disulfur hexafluoride", "sulfur fluoride"])]:
    A.append(M4(f"The correct name of the covalent compound {fx} is:", nm, ws, "prefixes show the number of atoms; second element ends in -ide"))
A += [
 M4("The Law of Conservation of Mass was proposed by:", "Antoine Lavoisier", ["Joseph Proust", "John Dalton", "Mendeleev"], "father of modern chemistry"),
 M4("The Law of Constant (Definite) Proportions was proposed by:", "Joseph Proust", ["Lavoisier", "Dalton", "Rutherford"], "fixed mass ratio in a compound"),
 M4("Which postulate of Dalton's atomic theory is correct?", "Atoms cannot be created or destroyed in a chemical reaction", ["Atoms of different elements are identical", "Atoms can be divided in a chemical reaction", "Atoms combine in any ratio"], "indivisible and conserved in reactions"),
 M4("A molecule is best defined as:", "an electrically neutral entity of more than one atom capable of independent existence", ["a charged particle of an element", "a single atom of any element", "only a particle of a compound"], "definition"),
 M4("The chemical bond formed by sharing of electrons is called:", "covalent bond", ["ionic bond", "metallic bond only", "hydrogen bond"], "shared electron pair"),
 M4("In an oxygen molecule O$_2$ the two atoms are joined by:", "a double bond", ["a single bond", "a triple bond", "an ionic bond"], "two shared pairs"),
 M4("In a nitrogen molecule the number of shared electron pairs is:", "3", ["1", "2", "4"], "N≡N triple bond (5 valence electrons each)"),
 M4("In the formation of NaCl, sodium:", "loses one electron to form Na$^+$", ["gains one electron to form Na$^-$", "shares one electron", "loses two electrons"], "completes octet by losing its single valence electron"),
 M4("The chlorine in NaCl is present as:", "Cl$^-$ ion", ["Cl$^+$ ion", "Cl$_2$ molecule", "neutral atom"], "chlorine gains one electron"),
 M4("The bond between oppositely charged ions is called:", "ionic bond", ["covalent bond", "metallic bond", "hydrogen bond"], "electrostatic attraction"),
 M4("Which compound is ionic?", "MgCl$_2$", ["CO$_2$", "CH$_4$", "HCl"], "metal + non-metal; electron transfer"),
 M4("Which of the following is a typical property of ionic compounds?", "high melting and boiling points", ["low melting point", "soft and flammable", "poor solubility in water always"], "strong attraction between ions"),
 M4("Ionic compounds conduct electricity:", "in molten state and in aqueous solution", ["in the solid state only", "never", "only as gases"], "ions are free to move"),
 M4("Covalent compounds generally have:", "low melting and boiling points", ["high melting points", "high electrical conductivity", "no definite shape"], "weak intermolecular forces"),
 M4("Sugar solution does not conduct electricity because:", "sugar is covalent and does not form ions", ["sugar is a metal", "water is a conductor only", "sugar forms Na$^+$ ions"], "no free charge carriers"),
 M4("A formula unit mass is used for:", "ionic compounds", ["covalent compounds", "elements only", "gases only"], "no discrete molecules in ionic solids"),
]
assert len(A) == 40, len(A)
B = [
 Q("State the Law of Conservation of Mass.", "In a chemical reaction matter can neither be created nor destroyed; total mass of reactants equals total mass of products (2).", "2"),
 Q("Why did the balloon experiment (open flask) show a loss in mass while the closed set-up did not?", "In the open set-up the CO$_2$ produced escaped; in the closed set-up it stayed inside, so the total mass was unchanged (2).", "2"),
 Q("4.0 g CaCO$_3$ reacts with 2.92 g HCl to give 1.76 g CO$_2$, 0.72 g H$_2$O and 4.44 g CaCl$_2$. Verify the Law of Conservation of Mass.", "Reactants $=6.92$ g; products $=1.76+0.72+4.44=6.92$ g; equal, hence verified (1+1).", "1+1"),
 Q("If 12 g carbon combines with 32 g oxygen, how much CO$_2$ forms from 6 g carbon?", "Carbon 6 g needs 16 g oxygen, so $6+16=22$ g of CO$_2$ (1+1).", "1+1"),
 Q("State the Law of Constant Proportions with an example.", "A compound always contains the same elements in a fixed ratio by mass irrespective of the source (1); water: H : O = 1 : 8 (1).", "1+1"),
 Q("9 g of water is decomposed. What are the masses of hydrogen and oxygen obtained?", "H : O = 1 : 8, so 1 g H and 8 g O (2).", "1+1"),
 Q("Why does the law of definite proportions apply to compounds and not to mixtures?", "In a compound elements are chemically combined in fixed ratio; in a mixture the components can be mixed in any ratio (2).", "2"),
 Q("State any two postulates of Dalton's atomic theory.", "All matter is made of atoms; atoms are indivisible and cannot be created or destroyed; atoms of an element are identical; atoms combine in simple whole-number ratios (any two) (1+1).", "1+1"),
 Q("Define a molecule. Give one example each of a molecule of an element and of a compound.", "Neutral entity of more than one atom capable of independent existence (1); H$_2$ / O$_2$ and H$_2$O / HCl (1).", "1+1"),
 Q("How is a covalent bond formed? Give one example.", "By sharing of electron pairs between atoms to complete the octet/duplet (1); e.g. H$_2$, Cl$_2$ or HCl (1).", "1+1"),
 Q("Name the compounds: (a) CO (b) N$_2$O$_5$ (c) H$_2$S (d) SF$_6$.", "(a) carbon monoxide (b) dinitrogen pentoxide (c) hydrogen sulfide (d) sulfur hexafluoride (½ each).", "½+½+½+½"),
 Q("How does sodium chloride form? Write the ions.", "Na (2,8,1) loses one electron to form Na$^+$; Cl (2,8,7) gains it to form Cl$^-$; the ions attract (2).", "1+1"),
 Q("Write the formulae of (a) calcium chloride (b) aluminium oxide.", "(a) CaCl$_2$ (b) Al$_2$O$_3$ (1+1).", "1+1"),
 Q("Calculate the molecular mass of CO$_2$ and NH$_3$ (C=12, O=16, N=14, H=1).", "CO$_2$: $12+32=44$ u; NH$_3$: $14+3=17$ u (1+1).", "1+1"),
 Q("Differentiate between molecular mass and formula unit mass.", "Molecular mass is for covalent compounds made of discrete molecules (1); formula unit mass is for ionic compounds, using the simplest formula (1).", "1+1"),
 Q("Give two reasons why ionic compounds have high melting points.", "Strong electrostatic force between oppositely charged ions (1); they form a regular crystal lattice needing much energy to break (1).", "1+1"),
]
C = [
 Q("Explain the Law of Conservation of Mass with the help of the reaction between sodium sulfate and barium chloride solutions.", "Weigh both solutions together before mixing (1); on mixing a white precipitate of barium sulfate forms with sodium chloride (1); the total mass remains unchanged — the law is verified (1).", "1+1+1"),
 Q("In a closed vessel 4.0 g CaCO$_3$ and 2.92 g HCl react to give 1.76 g CO$_2$, 0.72 g H$_2$O and some CaCl$_2$. Find the mass of CaCl$_2$ formed.", "Total reactants $=6.92$ g (1); mass of products must equal this (1); CaCl$_2=6.92-(1.76+0.72)=4.44$ g (1).", "1+1+1"),
 Q("A student burns 10 g of ethanol in an open beaker and finds the mass decreased. Is the law of conservation of mass violated? Explain.", "No (1). The gaseous products (CO$_2$ and water vapour) escape into the air (1), so a closed system would show the same total mass (1).", "1+1+1"),
 Q("12 g of carbon combines with 32 g of oxygen to form CO$_2$. How much CO$_2$ is formed from 2.4 g of carbon? Which law is used?", "12 g C → 44 g CO$_2$; 2.4 g C → $\\frac{44}{12}\\times2.4=8.8$ g (2); Law of Conservation of Mass / Constant Proportions (1).", "2+1"),
 Q("Sodium chloride has Na : Cl = 23 : 35.5 by mass. How much chlorine reacts with 46 g of sodium? How much NaCl is formed?", "Cl $=\\frac{35.5}{23}\\times46=71$ g (2); NaCl $=46+71=117$ g (1).", "2+1"),
 Q("A compound has 40 % sulfur and 60 % oxygen by mass. How much oxygen is present in a sample with 20 g sulfur?", "S : O = 40 : 60 = 2 : 3 (1); oxygen $=\\frac{3}{2}\\times20=30$ g (2).", "1+2"),
 Q("Carbon monoxide has C : O = 3 : 4. How much oxygen combines with 9 g carbon?", "$\\frac{4}{3}\\times9=12$ g (3).", "1+1+1"),
 Q("Students X and Y made oxides of copper in the ratios Cu : O = 4 : 1 and 8 : 2. Do these results justify the law of constant proportions?", "$8:2=4:1$, the same ratio (2). So yes — the compound has a fixed ratio irrespective of how it is prepared (1).", "2+1"),
 Q("State the main postulates of Dalton's atomic theory (any four).", "All matter is made of atoms (1); atoms are indivisible and are neither created nor destroyed in reactions (1); atoms of an element are identical, of different elements different; they combine in simple whole-number ratios (1)", "1+1+1"),
 Q("How do Dalton's postulates explain (i) the law of conservation of mass (ii) the law of constant proportions?", "(i) Atoms are neither created nor destroyed, only rearranged, so mass is conserved (1.5). (ii) Atoms combine in fixed simple ratios, giving fixed mass ratios (1.5).", "1½+1½"),
 Q("Show the formation of a chlorine molecule by sharing of electrons.", "Cl (2,8,7) needs one electron; each atom shares one electron, forming one shared pair (1+1); Cl—Cl single bond, each atom now has 8 electrons (1).", "1+1+1"),
 Q("Show the formation of an oxygen molecule. What type of bond is formed?", "O (2,6) needs two electrons; each shares two electrons (2); two shared pairs give a double bond O=O (1).", "2+1"),
 Q("Explain the formation of a water molecule by sharing of electrons.", "O (2,6) needs two electrons; each H (1) needs one (1); O shares one electron with each of two H atoms (1); H$_2$O has two single bonds (1)—each atom becomes stable.", "1+1+1"),
 Q("Explain the formation of sodium chloride from its atoms.", "Na (2,8,1) loses 1 electron to become Na$^+$ (2,8) (1); Cl (2,8,7) gains 1 electron to become Cl$^-$ (2,8,8) (1); opposite charges attract forming an ionic bond (1).", "1+1+1"),
 Q("Explain the formation of magnesium chloride.", "Mg (2,8,2) loses two electrons to form Mg$^{2+}$ (1); each Cl gains one electron: two Cl$^-$ (1); formula MgCl$_2$ — two chloride ions per magnesium ion (1).", "1+1+1"),
 Q("Write the formulae of (i) aluminium oxide (ii) calcium carbonate (iii) sodium sulfate using the criss-cross method for one of them.", "Al$^{3+}$, O$^{2-}$ → Al$_2$O$_3$ (1); CaCO$_3$ (1); Na$_2$SO$_4$ (1).", "1+1+1"),
 Q("Write the names of: (a) CS$_2$ (b) N$_2$O$_4$ (c) PCl$_3$ (d) H$_2$S (e) NH$_3$ (common name). State the rule for prefixes.", "carbon disulfide; dinitrogen tetroxide; phosphorus trichloride; hydrogen sulfide; ammonia (2). Prefixes mono, di, tri… show numbers of atoms; no prefix on hydrogen or mono for the first element (1).", "2+1"),
 Q("Distinguish between ionic and covalent compounds on the basis of (i) bonding (ii) melting point (iii) conduction of electricity.", "(i) Transfer vs sharing of electrons (1); (ii) high vs low (1); (iii) conduct in molten/aqueous state vs generally non-conductors (1).", "1+1+1"),
 Q("Calculate the molecular mass of H$_2$SO$_4$ and the formula unit mass of CaCl$_2$ (H=1, S=32, O=16, Ca=40, Cl=35.5).", "H$_2$SO$_4$: $2+32+64=98$ u (1.5); CaCl$_2$: $40+71=111$ u (1.5).", "1½+1½"),
 Q("Why does NaCl conduct electricity in solution but sugar does not?", "NaCl forms free Na$^+$ and Cl$^-$ ions in water which carry current (2); sugar is covalent and does not produce ions (1).", "2+1"),
 Q("Why do ionic compounds have high melting points and are usually hard but brittle?", "Strong electrostatic attraction between ions (1); regular lattice needs much energy to melt (1); displacement of layers brings like charges together causing brittleness (1).", "1+1+1"),
 Q("Why do noble gases exist as single atoms? Give two examples.", "Their valence shell is complete (8 electrons or duplet for helium) so they are stable and do not combine (2); helium, neon, argon (1).", "2+1"),
 Q("What are the energy changes when atoms combine? Why are molecules more stable than separate atoms?", "When atoms combine the energy of the system becomes lower than that of the separate atoms (2), so the arrangement is more stable (1).", "2+1"),
 Q("Why is hydrogen written first without a prefix in H$_2$S? Name H$_2$O and NH$_3$ using common names.", "When hydrogen is the first element no prefix is used, so H$_2$S is hydrogen sulfide (1.5); H$_2$O is water and NH$_3$ is ammonia — known by common names (1.5).", "1½+1½"),
]
D = [
 Q("(i) State the Law of Conservation of Mass. (ii) Describe an experiment to verify it using sodium sulfate and barium chloride. (iii) Why is a closed system required if gas is produced?", "(i) Mass of reactants equals mass of products (1). (ii) Weigh flasks containing the two solutions, mix them to get a white precipitate of barium sulfate, reweigh; the masses are equal (3). (iii) Escaping gas would carry away mass (1).", "1+3+1"),
 Q("<b>Case study:</b> Students react 4.0 g calcium carbonate with 2.92 g hydrochloric acid in a closed container and obtain 1.76 g CO$_2$, 0.72 g H$_2$O and CaCl$_2$. (i) Find the mass of CaCl$_2$. (ii) Which law is verified? (iii) What would happen to the measured mass if the vessel were open? (iv) Why?", "(i) $6.92-2.48=4.44$ g (2). (ii) Law of Conservation of Mass (1). (iii) Final mass would appear less (1). (iv) CO$_2$ would escape (1).", "2+1+1+1"),
 Q("(i) State the Law of Constant Proportions and name the scientist. (ii) Water from a river and from the sea each give H : O = 1 : 8. Explain. (iii) 36 g of water is decomposed; find the masses of hydrogen and oxygen. (iv) Does the law hold for mixtures?", "(i) A compound always contains the same elements in a fixed mass ratio; Proust (1). (ii) Water is a compound; its composition does not depend on the source (1). (iii) H : O = 1 : 8 → H 4 g, O 32 g (2). (iv) No — mixtures can have any ratio (1).", "1+1+2+1"),
 Q("<b>Case study:</b> Sodium chloride contains sodium and chlorine in the ratio 23 : 35.5 by mass. (i) How much chlorine reacts with 46 g of sodium? (ii) How much NaCl forms? (iii) How much sodium is in 117 g of NaCl? (iv) Which law helps?", "(i) 71 g (2). (ii) 117 g (1). (iii) 46 g (1). (iv) Law of Constant Proportions (1).", "2+1+1+1"),
 Q("(i) State the postulates of Dalton's atomic theory. (ii) How does it explain the laws of chemical combination? (iii) Which postulate was later shown to be incorrect and why?", "(i) Atoms; indivisible; identical for an element; different for different elements; simple whole-number ratios; constant relative number (3). (ii) Atoms are conserved ⇒ mass conserved; simple ratios ⇒ fixed ratio by mass (1). (iii) Atoms are divisible into subatomic particles (electrons, protons, neutrons) (1).", "3+1+1"),
 Q("(i) What is a covalent bond? (ii) Show the formation of H$_2$, Cl$_2$ and HCl by sharing of electrons. (iii) How many shared pairs are there in O$_2$ and N$_2$?", "(i) A bond formed by sharing electron pairs (1). (ii) Each H shares 1 e⁻ forming H—H; each Cl shares 1 e⁻ forming Cl—Cl; H and Cl share 1 pair forming H—Cl (3). (iii) O$_2$: two pairs (double bond); N$_2$: three pairs (triple bond) (1).", "1+3+1"),
 Q("<b>Case study:</b> Water is formed when hydrogen and oxygen combine. (i) Give the electronic configurations of H and O. (ii) Explain the bonding in H$_2$O. (iii) Why does water have different properties from H$_2$ and O$_2$? (iv) What is the mass ratio of H : O in water?", "(i) H: 1; O: 2,6 (1). (ii) O shares one electron with each of two H atoms giving two single bonds; each H gets duplet and O gets octet (2). (iii) A compound has properties different from its elements (1). (iv) 1 : 8 (1).", "1+2+1+1"),
 Q("(i) Explain the formation of an ionic bond in NaCl. (ii) Name the ions and write their electronic configurations. (iii) Write the formula of magnesium oxide and explain how it forms.", "(i) Na loses one electron, Cl gains it; the ions are held by electrostatic attraction (2). (ii) Na$^+$ (2,8), Cl$^-$ (2,8,8) (1). (iii) MgO: Mg (2,8,2) loses 2 e⁻ to O (2,6) forming Mg$^{2+}$ and O$^{2-}$ (2).", "2+1+2"),
 Q("<b>Case study:</b> A student compares sodium chloride and sugar. (i) Which conducts electricity in aqueous solution? (ii) Why? (iii) Compare their melting points. (iv) Classify them as ionic or covalent.", "(i) NaCl solution (1). (ii) It forms free ions Na$^+$ and Cl$^-$; sugar does not form ions (2). (iii) NaCl has a high melting point; sugar has low (1). (iv) NaCl ionic; sugar covalent (1).", "1+2+1+1"),
 Q("(i) Write the chemical formulae of calcium chloride, aluminium oxide, sodium sulfate, magnesium oxide and ammonia. (ii) Name the rule used. (iii) Name CO, CO$_2$, CS$_2$, N$_2$O$_4$, PCl$_3$.", "(i) CaCl$_2$, Al$_2$O$_3$, Na$_2$SO$_4$, MgO, NH$_3$ (2.5). (ii) Cross-over of valencies / criss-cross method (1). (iii) carbon monoxide, carbon dioxide, carbon disulfide, dinitrogen tetroxide, phosphorus trichloride (1.5).", "2½+1+1½"),
 Q("(i) Compare ionic and covalent compounds in four points. (ii) Why do ionic compounds dissolve in water while many covalent compounds do not?", "(i) Bond: transfer vs sharing of electrons (1); state: crystalline solids vs gases/liquids/soft solids (1); melting point: high vs low (1); conductivity: conduct when molten/dissolved vs non-conductors (1). (ii) Water molecules stabilise the ions and separate them; covalent compounds have no ions (1).", "4+1"),
 Q("<b>Case study:</b> A chemist records the substances CO$_2$, NH$_3$, NaCl and MgCl$_2$. (i) Classify each as molecular (covalent) or ionic. (ii) Find the molecular mass of CO$_2$ and NH$_3$. (iii) Find the formula unit mass of NaCl and MgCl$_2$. (iv) Why are formula unit masses used for ionic compounds? (H=1, C=12, N=14, O=16, Na=23, Mg=24, Cl=35.5)", "(i) CO$_2$ and NH$_3$ covalent; NaCl and MgCl$_2$ ionic (1). (ii) 44 u and 17 u (1). (iii) 58.5 u and 95 u (1). (iv) Ionic solids are lattices of ions without discrete molecules, so the simplest formula is used (2).", "1+1+1+2"),
 Q("(i) What is nuclear energy? Name one use. (ii) Name the scientist called the Father of the Indian Nuclear Programme. (iii) How does a nuclear power plant produce electricity?", "(i) Energy released when nuclei split or combine; used in electricity generation, medicine, research (2). (ii) Raja Ramanna (1). (iii) Heat from nuclear reactions makes steam that drives turbines (2).", "2+1+2"),
 Q("<b>Case study:</b> A student reacted zinc with dilute hydrochloric acid in an open test tube and found the mass decreased. (i) Name the products. (ii) Why did the mass decrease? (iii) How can she modify the set-up to verify the conservation of mass? (iv) What result should she get?", "(i) Zinc chloride and hydrogen gas (1). (ii) Hydrogen escaped (1). (iii) Use a closed flask with a balloon or stopper (2). (iv) Equal masses before and after (1).", "1+1+2+1"),
 Q("(i) What is a molecule? (ii) Distinguish between a molecule of an element and of a compound with two examples each. (iii) Why does helium exist as single atoms?", "(i) A neutral entity of more than one atom that can exist independently (1). (ii) Element: H$_2$, O$_2$, Cl$_2$; compound: H$_2$O, HCl, CO$_2$ (3). (iii) Its valence shell is already full (1).", "1+3+1"),
 Q("(i) Show that the combining ratio of carbon and oxygen in CO$_2$ is 3 : 8. (ii) How much carbon is in 22 g of CO$_2$? (iii) Find the mass of oxygen needed to burn 6 g of carbon completely.", "(i) 12 : 32 = 3 : 8 (1). (ii) $\\frac{12}{44}\\times22=6$ g (2). (iii) $\\frac{8}{3}\\times6=16$ g (2).", "1+2+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
