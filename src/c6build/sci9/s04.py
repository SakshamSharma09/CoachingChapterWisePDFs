from lib import mcq, Q, OR
from mk9 import M4, build
EL = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F", 10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca"}
NM = {"Na": "sodium", "Cl": "chlorine", "Ca": "calcium", "Al": "aluminium", "Fe": "iron", "C": "carbon", "K": "potassium", "S": "sulfur", "Mg": "magnesium"}
def conf(z):
    out = []; cap = [2, 8, 8, 2]
    for c in cap:
        t = min(z, c); out.append(t); z -= t
        if z <= 0: break
    return ", ".join(map(str, out))
A = []
# neutrons (6)
for sym, z, a in [("Na", 11, 23), ("Cl", 17, 35), ("Ca", 20, 40), ("Al", 13, 27), ("Fe", 26, 56), ("C", 6, 12)]:
    n = a - z
    w = [x for x in dict.fromkeys([z, a, n + 1, n - 1, n + 2, a + z]) if x != n][:3]
    A.append(M4(f"An atom of {NM[sym]} has atomic number {z} and mass number {a}. The number of neutrons in it is:", str(n), [str(x) for x in w], f"neutrons = {a} − {z}"))
# electronic configuration (6)
for sym, z in [("Na", 11), ("Cl", 17), ("S", 16), ("K", 19), ("Ca", 20), ("Al", 13)]:
    c = conf(z); parts = c.split(", ")
    cands = []
    alt1 = ", ".join(map(str, [2, 8, z - 10])) if z - 10 > 0 and z <= 18 else ", ".join(map(str, [2, 8, 9, z - 19]))
    alt2 = ", ".join(map(str, [2, 8, int(parts[-1]) + 1])) if len(parts) == 3 else ", ".join(map(str, [2, 8, 8, int(parts[-1]) + 1]))
    alt3 = ", ".join(map(str, [2, 9, z - 11])) if z - 11 > 0 else "2, 9"
    alt4 = ", ".join(map(str, [8, 2, z - 10])) if z > 10 else "8, 2"
    ws = [x for x in dict.fromkeys([alt1, alt2, alt3, alt4]) if x != c][:3]
    A.append(M4(f"The electronic configuration (K, L, M, N shells) of the {NM[sym]} atom (Z = {z}) is:", c, ws, "fill shells in order with maximum 2, 8, 8, 2"))
# valency (4)
for sym, z, v in [("Mg", 12, 2), ("Al", 13, 3), ("Cl", 17, 1), ("O", 8, 2)]:
    nm = NM.get(sym, "oxygen")
    A.append(M4(f"The valency of {nm} (Z = {z}) is:", str(v), [str(x) for x in dict.fromkeys([v + 1, v - 1 if v > 1 else 4, 4, 0, v + 2]) if x != v][:3], "electrons lost, gained or shared to complete the octet"))
# shell capacity (3)
for n, mx in [(3, 18), (2, 8), (4, 32)]:
    A.append(M4(f"The maximum number of electrons that the shell with n = {n} can hold is:", str(mx), [str(x) for x in dict.fromkeys([mx // 2, mx * 2, mx + 2, 2 * n, n * n]) if x != mx][:3], f"2n² = 2 × {n}² = {mx}"))
A += [
 M4("Acharya Kanada called the smallest indivisible particles of matter:", "parmanus", ["atomos", "electrons", "quarks"], "Vaisesika Sutras"),
 M4("The Greek philosophers who proposed indivisible particles called ‘atomos’ were:", "Leucippus and Democritus", ["Thomson and Rutherford", "Bohr and Bury", "Dalton and Proust"], "ancient Greece"),
 M4("Cathode rays were shown by J. J. Thomson to be:", "streams of negatively charged particles", ["streams of positive ions", "neutral waves", "protons"], "electrons"),
 M4("In Thomson's plum pudding model the electrons are:", "embedded in a sphere of positive charge", ["orbiting a nucleus", "inside the nucleus", "absent"], "positive sphere with negative charges"),
 M4("In the gold foil experiment most α-particles passed straight through. This showed that:", "most of the atom is empty space", ["atoms are solid spheres", "gold is radioactive", "α-particles are neutral"], "Rutherford's inference"),
 M4("A few α-particles rebounded at large angles. This led Rutherford to conclude that:", "the positive charge is concentrated in a tiny dense nucleus", ["positive charge is spread evenly", "electrons have no charge", "neutrons exist"], "nuclear model"),
 M4("The nucleus is about ______ times smaller than the atom.", "$10^5$ (one lakh)", ["10", "$10^2$", "$10^{10}$"], "10⁻¹⁰ m versus 10⁻¹⁵ m"),
 M4("Rutherford's model could NOT explain:", "the stability of the atom", ["the existence of a nucleus", "the neutrality of atoms", "scattering of α-particles"], "an orbiting electron would lose energy"),
 M4("Bohr's model proposes that electrons:", "revolve in fixed shells without losing energy", ["move randomly with changing energy", "are fixed at the nucleus", "have no energy"], "stationary states"),
 M4("The neutron was discovered by:", "James Chadwick", ["J. J. Thomson", "Niels Bohr", "Goldstein"], "1932"),
 M4("Which of the following particles has a negligible mass compared to others?", "electron", ["proton", "neutron", "α-particle"], "about 1/1836 of a proton"),
 M4("Which subatomic particle is neutral and found in the nucleus?", "neutron", ["proton", "electron", "cation"], "no charge"),
 M4("The atomic number of an element is equal to the number of:", "protons in its nucleus", ["neutrons", "nucleons", "valence electrons"], "defines the element"),
 M4("The mass number of an atom is the sum of its:", "protons and neutrons", ["protons and electrons", "electrons and neutrons", "shells and electrons"], "nucleons"),
 M4("Which pair are isotopes?", r"$^{35}_{17}\mathrm{Cl}$ and $^{37}_{17}\mathrm{Cl}$", [r"$^{40}_{18}\mathrm{Ar}$ and $^{40}_{20}\mathrm{Ca}$", r"$^{12}_{6}\mathrm{C}$ and $^{14}_{7}\mathrm{N}$", r"$^{1}_{1}\mathrm{H}$ and $^{4}_{2}\mathrm{He}$"], "same Z, different A"),
 M4("Atoms with the same mass number but different atomic numbers are called:", "isobars", ["isotopes", "isomers", "isotones only"], "e.g. ⁴⁰Ar and ⁴⁰Ca"),
 M4("The isotope used in the treatment of goitre is:", "iodine-131", ["uranium-235", "cobalt-60", "carbon-14"], "radioactive iodine"),
 M4("The isotope used for determining the age of fossils is:", "carbon-14", ["cobalt-60", "iodine-131", "uranium-235"], "radiocarbon dating"),
 M4("Isotopes of an element have similar chemical properties because they have the same:", "number of electrons and electronic configuration", ["mass number", "number of neutrons", "physical properties"], "chemical properties depend on valence electrons"),
 M4("The weighted average atomic mass of chlorine (35 u : 37 u = 3 : 1) is:", "35.5 u", ["36 u", "35 u", "37 u"], "(35 × 0.75) + (37 × 0.25)"),
 M4("An atom with an octet in its valence shell is generally:", "unreactive and stable", ["highly reactive", "radioactive", "negatively charged always"], "complete valence shell"),
]
assert len(A) == 6 + 6 + 4 + 3 + 21, len(A)
A = A[:40]
B = [
 Q("Name the ancient Indian and Greek thinkers who proposed that matter is made of indivisible particles.", "Acharya Kanada (parmanus) and Leucippus/Democritus (atomos) (1+1).", "1+1"),
 Q("Why did Thomson conclude that electrons are present in all atoms?", "Cathode rays were the same irrespective of the cathode material or the gas used, so electrons are a basic component of all atoms (2).", "2"),
 Q("Describe Thomson's plum pudding model.", "An atom is a sphere of positive charge in which negatively charged electrons are embedded, like plums in a pudding; overall neutral (2).", "1+1"),
 Q("What did most α-particles do in the gold foil experiment and what does it show?", "Most passed straight through (1); most of the atom is empty space (1).", "1+1"),
 Q("State two conclusions of Rutherford's gold foil experiment.", "The nucleus is small, dense and positively charged containing most of the mass; electrons revolve around it; most of the atom is empty (1+1).", "1+1"),
 Q("State one limitation of Rutherford's atomic model.", "It could not explain the stability of the atom — an orbiting (accelerating) electron should lose energy and spiral into the nucleus (2).", "2"),
 Q("State two postulates of Bohr's model.", "Electrons revolve in fixed shells/energy levels without losing energy; they move between shells by absorbing/releasing fixed energy; shells hold a fixed number of electrons (1+1).", "1+1"),
 Q("Why was the neutron needed to explain atomic masses? Give an example.", "A helium atom has 2 protons but mass about 4 times that of hydrogen, so uncharged particles must be present (1); Chadwick discovered the neutron (1).", "1+1"),
 Q("Define atomic number and mass number.", "Atomic number = number of protons in the nucleus (1); mass number = protons + neutrons (1).", "1+1"),
 Q("An atom has atomic number 26 and mass number 56. Find the number of protons, electrons and neutrons.", "Protons = electrons = 26 (1); neutrons = 56 − 26 = 30 (1).", "1+1"),
 Q("State the rules for filling of electrons in shells (Bohr–Bury).", "Maximum electrons in a shell = 2n² (K:2, L:8, M:18); outermost shell holds at most 8; shells fill in order K, L, M… (2).", "1+1"),
 Q("Write the electronic configuration of sodium (Z = 11) and chlorine (Z = 17). Give the valency of each.", "Na: 2, 8, 1 (valency 1); Cl: 2, 8, 7 (valency 1) (1+1).", "1+1"),
 Q("What is valency? How is it related to the valence shell?", "The number of electrons gained, lost or shared by an atom to complete its octet (1); decided by the electrons in the valence shell (1).", "1+1"),
 Q("Define isotopes with an example of hydrogen.", "Atoms of the same element with the same atomic number but different mass numbers (1); protium, deuterium, tritium (1).", "1+1"),
 Q("Why do isotopes of an element have similar chemical properties?", "They have the same number of electrons and the same electronic configuration (2).", "2"),
 Q("Define isobars with an example.", "Atoms of different elements with the same mass number but different atomic numbers (1); ⁴⁰Ar and ⁴⁰Ca (1).", "1+1"),
]
C = [
 Q("Explain the concept of the atom in ancient India and Greece and how Dalton's idea differed from it.", "Kanada's parmanus and Democritus' atomos were imagined indivisible particles (1.5); Dalton's atomic theory (1808) was based on experiments (1.5).", "1½+1½"),
 Q("Describe Thomson's cathode ray experiment and what he concluded.", "Gas at low pressure in a tube with two electrodes and high voltage; rays travelled from cathode to anode (1); bent by electric and magnetic fields so they are negatively charged particles with mass much smaller than atoms (1); present in every element (1).", "1+1+1"),
 Q("Why was Thomson's model rejected after the gold foil experiment?", "It predicted that α-particles would pass through or be deflected slightly (1); observed: some deflected sharply, a few rebounded (1); positive charge is concentrated, not spread (1).", "1+1+1"),
 Q("Describe the gold foil experiment and its observations.", "α-particles aimed at a very thin gold foil (1); most passed undeflected, some deflected through small angles, very few rebounded (2).", "1+2"),
 Q("State the main features of Rutherford's nuclear (planetary) model.", "Positive charge and most mass concentrated in a tiny nucleus; electrons revolve around it like planets; most of the atom is empty (1+1+1).", "1+1+1"),
 Q("If the diameter of an atom is 10⁻¹⁰ m and of its nucleus 10⁻¹⁵ m, how many times smaller is the nucleus? Use the cricket ground analogy.", "$10^{-10}/10^{-15}=10^5$ times (1); if the atom were a 100 m cricket ground, the nucleus would be a black pepper grain (1) at the centre (1).", "1+1+1"),
 Q("How many atoms of diameter 10⁻¹⁰ m must be stacked to make a sheet 0.1 mm thick?", "$0.1\\text{ mm}=10^{-4}$ m (1); atoms $=10^{-4}/10^{-10}$ (1) $=10^6$ (about a million) (1).", "1+1+1"),
 Q("Explain how Bohr's model removed the difficulty of Rutherford's model.", "Electrons move in fixed shells called stationary states and do not lose energy while in them (1.5); so atoms are stable; electrons jump between shells by absorbing or emitting fixed energy (1.5).", "1½+1½"),
 Q("Why are the shells called K, L, M, N and not A, B, C, D?", "Charles Barkla named the first observed X-ray series K to leave room for series discovered earlier (1.5); Bohr adopted the same notation (1.5).", "1½+1½"),
 Q("How did Chadwick's discovery explain why a helium atom is four times heavier than hydrogen? Why are neutrons important in heavy nuclei?", "He found a neutral particle of mass about that of a proton (1); He: 2 p + 2 n; mass ≈ 4 u (1); neutrons reduce proton–proton repulsion and add to the nuclear force (1).", "1+1+1"),
 Q("Why are the symbols of elements written using Latin names? Give two examples with their norms.", "Berzelius proposed using Latin names for international use (1); Fe (ferrum), Na (natrium), Hg (hydrargyrum) (1); first letter capital, second small (1).", "1+1+1"),
 Q("An atom has 20 protons and its mass number is 40. Find the number of neutrons and electrons, its configuration and valency.", "Neutrons 20, electrons 20 (1); configuration 2, 8, 8, 2 (1); valency 2 (1).", "1+1+1"),
 Q("An atom has 18 neutrons and mass number 35. Find its atomic number, name and configuration.", "Z = 35 − 18 = 17, chlorine (1.5); 2, 8, 7 (1.5).", "1½+1½"),
 Q("An atom has atomic number 26 and 56 nucleons. Find the number of neutrons, electrons and its symbol.", "Neutrons 30, electrons 26 (2), symbol Fe (1).", "2+1"),
 Q("Explain with the examples of sodium, oxygen and carbon how the valency of an element is determined.", "Na (2,8,1) loses 1 electron, valency 1 (1); O (2,6) gains 2, valency 2 (1); C (2,4) shares 4, valency 4 (1).", "1+1+1"),
 Q("Distinguish between isotopes and isobars with one example each.", "Isotopes: same Z, different A; e.g. ¹²C and ¹⁴C (1.5). Isobars: same A, different Z; e.g. ⁴⁰Ar, ⁴⁰K, ⁴⁰Ca (1.5).", "1½+1½"),
 Q("Name the three isotopes of hydrogen and give the number of protons and neutrons in each.", "Protium (1p, 0n), deuterium (1p, 1n), tritium (1p, 2n) (1+1+1).", "1+1+1"),
 Q("State three uses of isotopes.", "U-235: nuclear fuel; Co-60: cancer treatment; I-131: goitre; C-14: dating fossils (any three) (1+1+1).", "1+1+1"),
 Q("Chlorine has two isotopes of mass 35 u and 37 u in the ratio 3 : 1. Calculate its average atomic mass.", "Weighted average $=35\\times0.75+37\\times0.25$ (1) $=26.25+9.25=35.5$ u (2).", "1+2"),
 Q("A bromine sample has isotopes 79 u (49.7 %) and 81 u (50.3 %). Find the average atomic mass.", "$79\\times0.497+81\\times0.503=39.263+40.743=80.006\\approx80.0$ u (3).", "1+1+1"),
 Q("Why is the weighted average atomic mass of chlorine 35.5 u even though no atom has this mass?", "Natural chlorine is a mixture of isotopes in unequal proportions (1); the weighted average takes abundances into account (1); no single atom has mass 35.5 u (1).", "1+1+1"),
 Q("Why are noble gases chemically unreactive? Give configurations of neon and argon.", "Their valence shells are complete (octet, or duplet for helium) (1); Ne 2, 8; Ar 2, 8, 8 (2).", "1+2"),
 Q("Two atoms have 11 protons each, one with 12 and the other with 13 neutrons. Compare their atomic numbers and mass numbers. Are they the same element?", "Atomic number 11 for both; mass numbers 23 and 24 (2); same element — they are isotopes (1).", "2+1"),
 Q("Why is it said that electrons do not move in well-defined orbits as in Bohr's model?", "In the modern model electrons exist as electron clouds; only the regions of highest probability can be predicted (3).", "1+1+1"),
]
D = [
 Q("(i) Describe Thomson's cathode ray tube experiment. (ii) What did he conclude? (iii) Describe the plum pudding model and why it was proposed.", "(i) Gas at low pressure in a glass tube with two electrodes and high voltage; rays from cathode deflected in electric and magnetic fields (2). (ii) Cathode rays are streams of negatively charged electrons, independent of the cathode material and the gas, so electrons are present in all atoms (1). (iii) A positive sphere with embedded electrons; atoms are neutral (2).", "2+1+2"),
 Q("(i) Describe the gold foil experiment with observations. (ii) State the conclusions drawn. (iii) What would you expect if a thicker foil were used?", "(i) α-particles on a thin foil: most undeflected, some slightly deflected, a few rebounded (2). (ii) Atom is mostly empty; positive charge and mass concentrated in a small nucleus; electrons revolve around (2). (iii) More deflections and fewer particles passing through (1).", "2+2+1"),
 Q("<b>Case study:</b> If an atom were the size of a cricket ground (100 m), its nucleus would be a black pepper grain. (i) How many times smaller is the nucleus than the atom? (ii) Which part contains nearly all the mass? (iii) What does this tell us about the structure of the atom? (iv) Why did Rutherford's model fail to explain stability?", "(i) About $10^5$ times (1). (ii) The nucleus (1). (iii) Most of the atom is empty space (1). (iv) Accelerating electrons would lose energy and spiral into the nucleus (2).", "1+1+1+2"),
 Q("(i) Describe Bohr's model. (ii) How does it explain the stability of atoms? (iii) Why are the shells called K, L, M and N?", "(i) Electrons move in fixed shells (energy levels) without losing energy; shells farther out have higher energy; transitions need fixed energy; each shell has a limited capacity (2). (ii) In stationary states the energy of the electron stays constant (1). (iii) From Barkla's X-ray series naming — K was the first observed; Bohr adopted it (2).", "2+1+2"),
 Q("<b>Case study:</b> A hydrogen atom has one proton and a helium atom has two protons, yet helium's mass is four times that of hydrogen. (i) What puzzle does this pose? (ii) Who resolved it and how? (iii) What are the nucleons? (iv) Why do heavier atoms contain many more neutrons than protons?", "(i) Mass of helium is twice what protons alone give (1). (ii) James Chadwick in 1932 discovered the neutral neutron (1). (iii) Protons and neutrons (1). (iv) Neutrons reduce repulsion between protons and strengthen the nuclear force (2).", "1+1+1+2"),
 Q("(i) State the rules of Bohr–Bury for distribution of electrons. (ii) Write the electronic configuration of Mg, Cl, S, K and Ca. (iii) Give their valencies.", "(i) Maximum 2n² per shell; outermost shell ≤ 8; filled stepwise K, L, M, N (2). (ii) 2,8,2; 2,8,7; 2,8,6; 2,8,8,1; 2,8,8,2 (2.5). (iii) 2, 1, 2, 1, 2 (½).", "2+2½+½"),
 Q("<b>Case study:</b> An atom X has atomic number 17 and mass number 35. (i) Find protons, neutrons and electrons. (ii) Write its electronic configuration. (iii) Find its valency and name the element. (iv) Predict whether it forms a cation or anion.", "(i) 17 p, 18 n, 17 e (1). (ii) 2, 8, 7 (1). (iii) Valency 1; chlorine (1). (iv) It gains one electron to form Cl⁻ (anion) (2).", "1+1+1+2"),
 Q("(i) Define valency and valence electrons. (ii) Explain with Na, O and C how valency is determined. (iii) Why are noble gases unreactive?", "(i) Valency: number of electrons gained, lost or shared to complete octet; valence electrons: electrons in the outermost shell (2). (ii) Na: loses 1 (valency 1); O: gains 2 (valency 2); C: shares 4 (valency 4) (2). (iii) They have complete valence shells (1).", "2+2+1"),
 Q("(i) Define isotopes. (ii) Name the three isotopes of hydrogen and give their compositions. (iii) Why are the chemical properties of isotopes similar but the physical properties different?", "(i) Atoms of the same element with the same atomic number but different mass numbers (1). (ii) Protium 1p, deuterium 1p+1n, tritium 1p+2n (2). (iii) Same number of electrons give similar chemistry; different masses change density, melting and boiling points (2).", "1+2+2"),
 Q("<b>Case study:</b> Natural chlorine consists of isotopes of mass 35 u and 37 u in the ratio 3 : 1. (i) Name the isotopes. (ii) Find the simple average mass. (iii) Find the weighted average atomic mass. (iv) Why is the weighted value used?", "(i) Chlorine-35 and chlorine-37 (1). (ii) (35 + 37)/2 = 36 u (1). (iii) 35 × 0.75 + 37 × 0.25 = 35.5 u (2). (iv) The isotopes are not present in equal amounts (1).", "1+1+2+1"),
 Q("(i) Define isobars and give an example. (ii) Calcium (Z = 20), potassium (Z = 19) and argon (Z = 18) each have mass number 40. Find the neutrons in each. (iii) Distinguish isotopes from isobars.", "(i) Same mass number, different atomic numbers, e.g. ⁴⁰Ca and ⁴⁰Ar (1). (ii) Ca 20, K 21, Ar 22 neutrons (2). (iii) Isotopes: same Z, different A; isobars: same A, different Z (2).", "1+2+2"),
 Q("(i) State five uses of isotopes. (ii) Why can one not use ordinary chlorine for the same purposes? (iii) Name one Indian scientist associated with nuclear energy.", "(i) U-235 fuel; Co-60 cancer therapy; I-131 goitre; C-14 age of fossils; Na-24 flow in pipes (any) (2.5). (ii) Only radioactive isotopes emit the required radiation (1). (iii) Homi Jehangir Bhabha / Raja Ramanna (1.5).", "2½+1+1½"),
 Q("<b>Case study:</b> Table of elements: Na (2,8,1), Mg (2,8,2), Cl (2,8,7), Ar (2,8,8). (i) Which has complete valence shell? (ii) Which will lose electrons? (iii) Which will gain? (iv) Predict the formula of the compound of Mg and Cl and explain.", "(i) Argon (1). (ii) Na and Mg (1). (iii) Cl (1). (iv) MgCl$_2$ — Mg loses two electrons, each Cl gains one (2).", "1+1+1+2"),
 Q("(i) Distinguish between Thomson, Rutherford and Bohr models in a table of three points. (ii) Which discovery showed that atoms are divisible? (iii) Name the discoverers of electron, proton and neutron.", "(i) Thomson: sphere of positive charge with electrons; Rutherford: central nucleus with orbiting electrons, stability problem; Bohr: fixed shells, stable (3). (ii) Discovery of electrons/radioactivity (1). (iii) Thomson, Rutherford, Chadwick (1).", "3+1+1"),
 Q("(i) Why were symbols introduced for elements? (ii) State the norms for writing symbols. (iii) Give the symbols of iron, mercury, sodium and potassium and their origins.", "(i) A standard international shorthand for communication (1). (ii) First letter capital, second letter small; many from first one or two letters; some from Latin, Greek or German names (2). (iii) Fe (ferrum), Hg (hydrargyros), Na (natrium), K (kalium) (2).", "1+2+2"),
 Q("(i) Explain why electrons were thought to be present in every atom. (ii) Why is the atom electrically neutral? (iii) Calculate the number of subatomic particles in an atom of aluminium (Z = 13, A = 27) and write its configuration and valency.", "(i) Cathode rays were identical for every cathode material and gas, so electrons are a common constituent (1). (ii) Number of protons equals number of electrons, so the charges cancel (1). (iii) 13 protons, 13 electrons, 14 neutrons (1.5); configuration 2, 8, 3 (1); valency 3 (0.5).", "1+1+3"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
