"""Class 10 Science Ch 3 Metals and Non-metals - extras."""
from common import AR4, Q

AR = [
 AR4(r"Sodium is stored under kerosene oil.", r"Sodium reacts vigorously with oxygen and moisture of the air and may catch fire.", "a",
     r"Kerosene cuts off air and moisture, preventing the violent reaction."),
 AR4(r"Aluminium oxide is an amphoteric oxide.", r"Aluminium is widely used for making cooking utensils.", "b",
     r"Both true: $\ce{Al2O3}$ reacts with acids and bases; utensils use depends on good conductivity of heat and malleability, so R does not explain A."),
 AR4(r"Iron articles are galvanised by coating them with zinc.", r"Zinc is less reactive than iron and so cannot be corroded.", "c",
     r"Galvanisation is true, but zinc is <i>more</i> reactive than iron and protects it even if the coating is broken; R is false."),
 AR4(r"All non-metals are bad conductors of electricity.", r"Graphite, an allotrope of carbon, is a good conductor of electricity.", "d",
     r"Graphite is a non-metal that conducts, so A is false; R is true."),
 AR4(r"Metals are electropositive elements.", r"Metals tend to lose electrons to form positive ions.", "a",
     r"Electropositive means forming cations by loss of electrons, which R states."),
 AR4(r"Sodium chloride conducts electricity in the molten state but not in the solid state.", r"Ionic compounds have high melting points.", "b",
     r"Both true; conduction in the molten state occurs because ions become free to move, not because of the high melting point."),
]

CASE = [
 Q(r"<b>Case study.</b> In an experiment, equal-sized pieces of magnesium, zinc, iron and copper were dropped into separate test tubes containing dilute hydrochloric acid. Bubbles of a gas appeared vigorously on magnesium, slowly on zinc, very slowly on iron and no bubbles appeared on copper. "
   r"(i) Which metal does not react with dilute HCl? (ii) Name the gas evolved and give its test. (iii) Write the equation for the reaction of zinc with dilute HCl. (iv) Arrange the four metals in decreasing order of reactivity and state the conclusion drawn from the rate of bubbling.",
   r"(i) Copper (1). (ii) Hydrogen; it burns with a pop sound with a burning matchstick (1). (iii) $\ce{Zn + 2HCl -> ZnCl2 + H2}$ (1). (iv) Mg > Zn > Fe > Cu (1); the faster the bubbling, the more reactive the metal is (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A mining company at Zawar in Rajasthan obtains zinc from its sulphide ore, zinc blende (ZnS), and from zinc carbonate ($\ce{ZnCO3}$). The sulphide ore is heated strongly in excess air, and the carbonate ore is heated in limited air. The oxide formed in each case is then reduced with carbon. "
   r"(i) What is heating a sulphide ore in excess air called? (ii) What is heating a carbonate ore in limited air called? (iii) Write the equation for the conversion of ZnS to ZnO. (iv) Write the equation for the reduction of ZnO with carbon and state why electrolysis is not needed for zinc.",
   r"(i) Roasting (1). (ii) Calcination (1). (iii) $\ce{2ZnS + 3O2 -> 2ZnO + 2SO2}$ (1). (iv) $\ce{ZnO + C -> Zn + CO}$ (1); zinc lies in the middle of the reactivity series, so carbon can reduce its oxide (electrolysis is needed only for highly reactive metals like Na, Ca, Al) (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Magnesium (atomic number 12) reacts with chlorine (atomic number 17) to form a compound. The compound is a white crystalline solid with a high melting point; it does not conduct electricity as a solid but conducts when molten or dissolved in water. "
   r"(i) How many electrons does a magnesium atom lose? (ii) Write the formula of the compound. (iii) Name the type of bond. (iv) Explain why the compound conducts electricity in the molten state but not in the solid state.",
   r"(i) Two (electronic configuration 2, 8, 2) (1). (ii) $\ce{MgCl2}$ (1). (iii) Ionic bond (1). (iv) In the solid the ions are held in fixed positions and cannot move (1); in the molten state or solution the ions are free to move and carry charge (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Properties", [r"Metals: lustrous, malleable, ductile, good conductors of heat and electricity, sonorous, usually hard with high melting points (exceptions: Na and K soft, Hg liquid, Ga and Cs melt in the hand).",
   r"Non-metals: dull, brittle, poor conductors (graphite conducts), low melting points (diamond is the hardest natural substance; iodine is lustrous)."]),
 ("Reactions of metals", [r"Metal + oxygen $\rightarrow$ metal oxide: $\ce{4Al + 3O2 -> 2Al2O3}$. Na and K are stored under kerosene.",
   r"Amphoteric oxides ($\ce{Al2O3}$, $\ce{ZnO}$): $\ce{Al2O3 + 6HCl -> 2AlCl3 + 3H2O}$ and $\ce{Al2O3 + 2NaOH -> 2NaAlO2 + H2O}$.",
   r"Water: $\ce{2Na + 2H2O -> 2NaOH + H2}$; steam: $\ce{3Fe + 4H2O -> Fe3O4 + 4H2}$ (Mg, Al, Zn, Fe react with steam).",
   r"Dilute acid: metal + acid $\rightarrow$ salt + $\ce{H2}$ (Cu, Ag, Au, Hg do not displace hydrogen).",
   r"Displacement: $\ce{Fe + CuSO4 -> FeSO4 + Cu}$ (more reactive metal displaces less reactive)."]),
 ("Reactivity series (decreasing)", [r"K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au."]),
 ("Ionic compounds", [r"Formed by transfer of electrons: $\ce{Na -> Na+ + e-}$; $\ce{Cl + e- -> Cl-}$; $\ce{Mg}$ with 2, 8, 2 gives $\ce{Mg^{2+}}$.",
   r"Properties: solid, hard and brittle, high melting and boiling points, soluble in water, conduct only in molten state or in solution."]),
 ("Metallurgy", [r"Steps: concentration of ore $\rightarrow$ extraction of metal $\rightarrow$ refining.",
   r"Low reactivity (Hg): $\ce{2HgS + 3O2 -> 2HgO + 2SO2}$, then $\ce{2HgO -> 2Hg + O2}$. Middle (Zn, Fe, Pb): roast/calcine, then reduce with carbon (e.g. $\ce{ZnO + C -> Zn + CO}$).",
   r"High reactivity (Na, Ca, Al): electrolysis of molten chloride/oxide; cathode gets the metal. Thermit: $\ce{Fe2O3 + 2Al -> 2Fe + Al2O3}$ + heat.",
   r"Refining: electrolytic refining (anode impure metal, cathode pure metal, electrolyte a salt solution of the metal)."]),
 ("Corrosion", [r"Rusting needs air and moisture; prevented by painting, oiling, galvanising, alloying. Silver turns black, copper gets a green coating. Alloy = homogeneous mixture of metals (brass, bronze, solder)."]),
]

MISTAKES = [
 r"Storing sodium or potassium in water; they are stored under kerosene because they react violently with water and air.",
 r"Confusing <b>roasting</b> (sulphide ore, excess air) with <b>calcination</b> (carbonate ore, limited air).",
 r"Writing the product of iron with steam as $\ce{Fe2O3}$; it is $\ce{Fe3O4}$ and hydrogen gas is released.",
 r"Thinking that all metals are hard solids and all non-metals are non-conductors; Na is soft, Hg is a liquid and graphite conducts.",
 r"Saying that an ionic solid conducts electricity; it conducts only when molten or in aqueous solution.",
 r"Writing that copper can displace hydrogen from dilute acids or iron from $\ce{FeSO4}$; a less reactive metal cannot displace a more reactive one.",
]
