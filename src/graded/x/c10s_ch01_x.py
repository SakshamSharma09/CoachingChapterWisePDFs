"""Class 10 Science Ch 1 Chemical Reactions and Equations - extras."""
from common import AR4, Q

AR = [
 AR4(r"Burning of magnesium ribbon in air is a combination reaction.", r"In a combination reaction two or more substances combine to form a single product.", "a",
     r"$\ce{2Mg + O2 -> 2MgO}$: two reactants give one product, so R explains A."),
 AR4(r"A white precipitate is formed when barium chloride solution is mixed with sodium sulphate solution.", r"The reaction between barium chloride and sodium sulphate is a double displacement reaction.", "b",
     r"$\ce{BaCl2 + Na2SO4 -> BaSO4 + 2NaCl}$; both true, but the white precipitate is due to the insolubility of $\ce{BaSO4}$, not because the reaction is called double displacement."),
 AR4(r"Rusting of iron is an oxidation process.", r"During rusting, iron is reduced by oxygen and moisture.", "c",
     r"Iron gains oxygen (oxidation), so A is true; iron is oxidised, not reduced, so R is false."),
 AR4(r"Decomposition of calcium carbonate on heating is an exothermic reaction.", r"Decomposition reactions require energy in the form of heat, light or electricity.", "d",
     r"$\ce{CaCO3 ->[heat] CaO + CO2}$ absorbs heat (endothermic), so A is false; R is true."),
 AR4(r"The blue colour of copper sulphate solution fades when a zinc strip is dipped in it.", r"Zinc is more reactive than copper and displaces it from its salt solution.", "a",
     r"$\ce{Zn + CuSO4 -> ZnSO4 + Cu}$; blue $\ce{Cu^{2+}}$ is replaced by colourless $\ce{Zn^{2+}}$."),
 AR4(r"When water is electrolysed, the volume of hydrogen collected is twice that of oxygen.", r"The electrolysis of water is a decomposition reaction.", "b",
     r"Both statements are true, but the 2 : 1 ratio comes from the formula $\ce{H2O}$ ($\ce{2H2O -> 2H2 + O2}$), which R does not state."),
]

CASE = [
 Q(r"<b>Case study.</b> In a school laboratory, Rohan took about 2 g of green ferrous sulphate crystals in a dry boiling tube and heated it strongly. The crystals first lost water and turned white, then changed to a reddish-brown solid, and a smell like burning sulphur was noticed. "
   r"(i) What is the colour of the final solid residue? (ii) Name the type of reaction taking place on strong heating. (iii) Write the balanced chemical equation for the decomposition of anhydrous ferrous sulphate. (iv) Name the two gaseous products and state whether the reaction is endothermic or exothermic, with a reason.",
   r"(i) Reddish brown (the solid is $\ce{Fe2O3}$) (1). (ii) Thermal decomposition (1). (iii) $\ce{2FeSO4 ->[heat] Fe2O3 + SO2 + SO3}$ (1). (iv) Sulphur dioxide and sulphur trioxide (1); endothermic, because heat has to be supplied continuously for the reaction to proceed (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Meena placed a clean iron nail in a blue copper sulphate solution. After about 30 minutes she observed that the nail was covered with a brownish deposit and the blue colour of the solution had changed to pale green. "
   r"(i) What is the brown deposit on the nail? (ii) Name the type of reaction. (iii) Write the balanced equation. (iv) Meena now dips a copper strip in iron(II) sulphate solution. Predict, with reason, what she will observe.",
   r"(i) Copper metal (1). (ii) Displacement reaction (1). (iii) $\ce{Fe + CuSO4 -> FeSO4 + Cu}$ (1). (iv) No reaction / no change (1), because copper is less reactive than iron and cannot displace iron from its salt solution (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Mrs Verma lives in a coastal town in Kerala. She notices that the oil kept in an open jar has developed an unpleasant smell and taste, while the packet of potato chips she bought is filled with nitrogen gas. The iron gate of her house has also developed reddish-brown flakes. "
   r"(i) What is the spoilage of fats and oils called? (ii) Why is nitrogen gas filled in chips packets? (iii) Name the two substances necessary for rusting of iron. (iv) Why does the gate rust faster in a coastal town? Suggest one way to prevent it.",
   r"(i) Rancidity (1). (ii) Nitrogen is unreactive and prevents oxidation of the fats and oils in chips (1). (iii) Oxygen (air) and moisture (water) (1). (iv) Salt in the moist sea air speeds up corrosion (1); painting, galvanising (zinc coating) or greasing prevents rusting (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Chemical equations", [r"Reactants $\rightarrow$ products; a balanced equation has the same number of atoms of each element on both sides (law of conservation of mass).",
   r"Physical states: (s), (l), (g), (aq). Condition (heat, catalyst, light) is written over the arrow. $\uparrow$ = gas evolved, $\downarrow$ = precipitate.",
   r"Balancing: do not change formulas; change only coefficients."]),
 ("Types of reactions", [r"Combination: $\ce{A + B -> AB}$, e.g. $\ce{CaO + H2O -> Ca(OH)2}$ (exothermic, slaking of lime).",
   r"Decomposition: $\ce{AB -> A + B}$; thermal: $\ce{CaCO3 -> CaO + CO2}$; electrolytic: $\ce{2H2O -> 2H2 + O2}$; photolytic: $\ce{2AgCl -> 2Ag + Cl2}$.",
   r"Displacement: $\ce{A + BC -> AC + B}$, e.g. $\ce{Fe + CuSO4 -> FeSO4 + Cu}$ (A more reactive than B).",
   r"Double displacement: $\ce{AB + CD -> AD + CB}$, e.g. $\ce{Na2SO4 + BaCl2 -> BaSO4 + 2NaCl}$ (precipitation reaction)."]),
 ("Oxidation and reduction", [r"Oxidation = gain of oxygen / loss of hydrogen. Reduction = loss of oxygen / gain of hydrogen.",
   r"Redox: both occur together, e.g. $\ce{CuO + H2 -> Cu + H2O}$ ($\ce{CuO}$ reduced, $\ce{H2}$ oxidised).",
   r"The substance oxidised is the reducing agent; the substance reduced is the oxidising agent."]),
 ("Energy changes", [r"Exothermic: heat released (burning, respiration, slaking of lime, decomposition of vegetable matter).",
   r"Endothermic: heat absorbed (decomposition of $\ce{CaCO3}$, photosynthesis, electrolysis)."]),
 ("Key reactions to remember", [r"$\ce{2Pb(NO3)2 -> 2PbO + 4NO2 + O2}$ (brown fumes of $\ce{NO2}$).",
   r"$\ce{2FeSO4 -> Fe2O3 + SO2 + SO3}$ (green crystals to brown residue).",
   r"$\ce{Ca(OH)2 + CO2 -> CaCO3 + H2O}$ (lime water turns milky)."]),
 ("Corrosion and rancidity", [r"Corrosion: slow attack on metals by air, moisture or acids (rusting of iron needs both air and water; green coating on copper, black coating on silver).",
   r"Prevention: painting, oiling, galvanising, alloying. Rancidity: oxidation of fats and oils giving bad smell and taste; prevented by antioxidants, airtight containers, flushing with nitrogen, refrigeration."]),
]

MISTAKES = [
 r"Changing the subscripts (formulae) instead of the coefficients while balancing; $\ce{H2O}$ must not be written as $\ce{H2O2}$ to balance oxygen.",
 r"Writing $\ce{Mg + O2 -> MgO}$ without balancing, or $\ce{MgO2}$ for magnesium oxide.",
 r"Calling every reaction in which heat is given out 'decomposition'; identify the type from the reactants and products (one product = combination).",
 r"Forgetting that in a displacement reaction the displacing metal must be <b>more reactive</b>; $\ce{Cu + FeSO4}$ gives no reaction.",
 r"Mixing up oxidation and reduction: gain of oxygen is oxidation, loss of oxygen is reduction.",
 r"Writing that rusting needs only oxygen; it needs <b>both</b> oxygen and moisture. Slaking of lime is exothermic, not endothermic.",
]
