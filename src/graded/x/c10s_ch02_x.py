"""Class 10 Science Ch 2 Acids, Bases and Salts - extras."""
from common import AR4, Q

AR = [
 AR4(r"Dry hydrogen chloride gas does not change the colour of dry blue litmus paper.", r"Acids produce $\ce{H+}$ ions only in the presence of water.", "a",
     r"Without water the acid does not ionise, so no $\ce{H+}$ is available to change the litmus; R explains A."),
 AR4(r"Bleaching powder is used for disinfecting drinking water.", r"Bleaching powder is produced by the action of chlorine on dry slaked lime.", "b",
     r"Both true; the disinfecting action is due to the chlorine it releases, not due to the way it is manufactured."),
 AR4(r"Tooth decay starts when the pH of the mouth falls below 5.5.", r"Tooth enamel is dissolved by the bases produced by bacteria in the mouth.", "c",
     r"Enamel (calcium phosphate) is corroded below pH 5.5 by acids, formed when bacteria degrade sugar; R is false."),
 AR4(r"Washing soda has the formula $\ce{Na2CO3.5H2O}$.", r"Washing soda is obtained by recrystallisation of sodium carbonate.", "d",
     r"Washing soda is $\ce{Na2CO3.10H2O}$, so A is false; R is true."),
 AR4(r"Aqueous solutions of glucose and alcohol do not conduct electricity.", r"Glucose and alcohol do not produce ions in aqueous solution.", "a",
     r"Both contain hydrogen but do not release $\ce{H+}$ or other ions, so they are not acids and do not conduct."),
 AR4(r"Baking powder makes cakes soft and spongy.", r"Baking powder is a mixture of baking soda and a mild edible acid such as tartaric acid.", "b",
     r"Both true; the sponginess is due to $\ce{CO2}$ released when the mixture is heated or moistened. R only states the composition."),
]

CASE = [
 Q(r"<b>Case study.</b> A gardener, Harpal, tested four soil-water samples with a pH paper. Sample P showed pH 5, sample Q pH 7, sample R pH 9 and sample S pH 13. "
   r"(i) Which sample is neutral? (ii) Which sample is the strongest base? (iii) Which sample(s) will turn red litmus blue? (iv) Harpal wants to grow a crop in the acidic sample P. Name a substance he can add to the soil to bring the pH nearer to 7 and give the reason.",
   r"(i) Sample Q (pH = 7) (1). (ii) Sample S (highest pH) (1). (iii) R and S (pH greater than 7) (1). (iv) Quick lime / slaked lime / chalk (any one) (1), because it is basic and neutralises the excess acid in the soil (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In a chemical factory, a concentrated solution of sodium chloride (brine) is electrolysed. Three useful substances are formed: gas X at the anode, gas Y at the cathode and a solution Z near the cathode. The gas X is used to prepare bleaching powder. "
   r"(i) Name the process. (ii) Identify X and Y. (iii) Name the solution Z. (iv) Write the balanced equation for the electrolysis and the equation for the formation of bleaching powder from X.",
   r"(i) Chlor-alkali process (1). (ii) X is chlorine, Y is hydrogen (1). (iii) Z is sodium hydroxide solution (1). (iv) $\ce{2NaCl + 2H2O -> 2NaOH + Cl2 + H2}$ (1); $\ce{Ca(OH)2 + Cl2 -> CaOCl2 + H2O}$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A doctor puts a plaster cast on the fractured arm of a child. The white powder used for the cast is prepared by heating gypsum at 373 K in a kiln. The powder is always stored in a moisture-proof container. "
   r"(i) Name the white powder. (ii) Write its chemical formula. (iii) Name the substance obtained when it is mixed with water. (iv) Why must it be kept in a moisture-proof container? Write the equation.",
   r"(i) Plaster of Paris (1). (ii) $\ce{CaSO4.1/2H2O}$ (1). (iii) Gypsum, $\ce{CaSO4.2H2O}$ (1). (iv) It absorbs moisture and sets into a hard mass of gypsum (1); $\ce{CaSO4.1/2H2O + 3/2H2O -> CaSO4.2H2O}$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Indicators and pH", [r"Acid: turns blue litmus red; base: turns red litmus blue; phenolphthalein is pink in base and colourless in acid; methyl orange is red in acid, yellow in base.",
   r"pH scale 0-14: pH < 7 acidic, pH = 7 neutral, pH > 7 basic. Lower pH = stronger acid; higher pH = stronger base.",
   r"Acid + water: $\ce{HCl -> H+ + Cl-}$; $\ce{H+}$ exists as $\ce{H3O+}$. Always add acid to water, never water to acid."]),
 ("Reactions of acids and bases", [r"Acid + metal $\rightarrow$ salt + $\ce{H2}$: $\ce{Zn + 2HCl -> ZnCl2 + H2}$ (gas burns with a pop sound).",
   r"Acid + metal carbonate / hydrogencarbonate $\rightarrow$ salt + $\ce{CO2}$ + $\ce{H2O}$: $\ce{Na2CO3 + 2HCl -> 2NaCl + H2O + CO2}$.",
   r"Base + metal (e.g. Zn): $\ce{Zn + 2NaOH -> Na2ZnO2 + H2}$. Base + non-metal oxide $\rightarrow$ salt + water.",
   r"Neutralisation: acid + base $\rightarrow$ salt + water, e.g. $\ce{NaOH + HCl -> NaCl + H2O}$.",
   r"Lime water test: $\ce{Ca(OH)2 + CO2 -> CaCO3 + H2O}$ (milky); excess $\ce{CO2}$ gives soluble $\ce{Ca(HCO3)2}$."]),
 ("Common salts", [r"Common salt: $\ce{NaCl}$. Chlor-alkali: $\ce{2NaCl + 2H2O -> 2NaOH + Cl2 + H2}$ (anode $\ce{Cl2}$, cathode $\ce{H2}$).",
   r"Bleaching powder: $\ce{Ca(OH)2 + Cl2 -> CaOCl2 + H2O}$; uses: bleaching, disinfecting water.",
   r"Baking soda: $\ce{NaHCO3}$, from $\ce{NaCl + H2O + CO2 + NH3 -> NH4Cl + NaHCO3}$; heating: $\ce{2NaHCO3 -> Na2CO3 + H2O + CO2}$.",
   r"Washing soda: $\ce{Na2CO3.10H2O}$ (from $\ce{Na2CO3}$ by recrystallisation).",
   r"Plaster of Paris: $\ce{CaSO4.1/2H2O}$ from $\ce{CaSO4.2H2O}$ (gypsum) heated at 373 K; $\ce{CaSO4.1/2H2O + 3/2H2O -> CaSO4.2H2O}$."]),
 ("Everyday applications", [r"Antacids (mild bases, e.g. $\ce{Mg(OH)2}$) relieve indigestion; tooth decay begins at pH < 5.5; acid rain pH < 5.6.",
   r"Water of crystallisation: fixed number of water molecules in a salt crystal (blue $\ce{CuSO4.5H2O}$ becomes white on heating)."]),
]

MISTAKES = [
 r"Pouring water into concentrated acid; always add the acid slowly to water with stirring because the process is highly exothermic.",
 r"Writing that a solution with pH 3 is 'less acidic' than one with pH 5; a lower pH means a <b>stronger</b> acid.",
 r"Mixing up the formulae: baking soda is $\ce{NaHCO3}$, washing soda is $\ce{Na2CO3.10H2O}$, plaster of Paris is $\ce{CaSO4.1/2H2O}$ and bleaching powder is $\ce{CaOCl2}$.",
 r"Thinking that all compounds containing hydrogen are acids; glucose and alcohol do not release $\ce{H+}$ ions.",
 r"Writing $\ce{H2}$ as the gas formed when an acid reacts with a carbonate; the gas is $\ce{CO2}$.",
 r"Assuming neutralisation always gives a neutral solution; a strong acid with a weak base gives an acidic salt solution (and vice-versa).",
]
