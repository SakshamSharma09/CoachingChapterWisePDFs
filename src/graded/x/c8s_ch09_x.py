"""Class 8 Science Ch 9 Solutes, Solvents and Solutions - extras."""
from common import AR4, Q

AR = [
 AR4("A solution of salt in water does not scatter a beam of light.", "The particles in a true solution are extremely small.", "a", "Very small particles cannot scatter light, so there is no Tyndall effect."),
 AR4("A soft drink fizzes when its cap is opened.", "Carbon dioxide dissolved under pressure escapes when the pressure is reduced.", "a", "Solubility of a gas falls when pressure falls."),
 AR4("Sugar crystals dissolve faster than powdered sugar in water.", "Powdered sugar has a larger surface area exposed to water.", "d", "A is false (powder dissolves faster); R is true."),
 AR4("Muddy water can be separated into mud and water by filtration.", "A suspension has particles large enough to settle and be held back by filter paper.", "a", "Large suspended particles are trapped on the filter paper."),
 AR4("Muddy water is a suspension.", "Milk is a colloid.", "b", "Both are true, but the nature of milk does not explain why muddy water is a suspension."),
 AR4("Sugar dissolves in water, but chalk powder does not.", "Water can dissolve all substances.", "c", "A is true; R is false, water dissolves many but not all substances."),
]

CASE = [
 Q("<b>Case study.</b> Meena dissolves 25 g of sugar in 225 g of water to make sharbat for her family in Jaipur. She stirs it until no sugar crystals are visible and notices that the liquid looks clear and the sweetness is the same in every spoonful. "
   "(i) Name the solute and the solvent. (ii) What is the mass of the solution? (iii) Why is the sweetness the same everywhere? (iv) Calculate the mass percentage of sugar in the solution.",
   "(i) Solute: sugar; solvent: water (1). (ii) 25 + 225 = 250 g (1). (iii) It is a homogeneous mixture, so the solute is evenly spread (1). (iv) Mass percentage = (25/250) x 100 = 10 per cent (2).", "1+1+1+2"),
 Q("<b>Case study.</b> In a school laboratory in Pune, Arjun finds that 100 g of water at room temperature dissolves at most 36 g of common salt. He adds 50 g of salt to 100 g of water and stirs well; some salt remains undissolved at the bottom. He then heats the mixture gently. "
   "(i) What is the maximum amount of salt that dissolves in 100 g of water called? (ii) How much salt remains undissolved at room temperature? (iii) Is the solution saturated or unsaturated? (iv) Suggest what happens on heating and give a reason.",
   "(i) Solubility (1). (ii) 50 - 36 = 14 g (1). (iii) Saturated (1). (iv) More salt dissolves, because the solubility of most solids in water increases with temperature (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Fatima's teacher gives three samples: muddy pond water, milk, and sugar solution. A torch beam is passed through each one. The beam is clearly visible in milk and in muddy water, but not in the sugar solution. When left undisturbed for an hour, only the muddy water shows particles settling at the bottom. "
   "(i) Which sample is a true solution? (ii) Which sample is a suspension? (iii) What is the scattering of light by particles called? (iv) Milk does not settle but scatters light; explain what this shows about its particle size.",
   "(i) Sugar solution (1). (ii) Muddy water (1). (iii) Tyndall effect (1). (iv) Its particles are larger than those of a solution, so they scatter light, but small enough that they do not settle; it is a colloid (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Terms", ["Solution: homogeneous mixture of solute and solvent. Solute: the substance dissolved; solvent: the substance in which it dissolves.",
   "Mass of solution = mass of solute + mass of solvent.", "Water is called the universal solvent as it dissolves a very large number of substances (not all)."]),
 ("Concentration and solubility", ["$\text{Mass percentage} = \dfrac{\text{mass of solute}}{\text{mass of solution}} \times 100$",
   "Saturated solution: cannot dissolve more solute at that temperature. Unsaturated: can dissolve more.",
   "Solubility: maximum mass of solute that dissolves in 100 g of solvent at a given temperature."]),
 ("Factors affecting dissolving", ["Solubility of most solids in water increases with temperature.", "Solubility of gases in water decreases as temperature rises and increases with pressure.",
   "Stirring, heating and powdering increase the rate of dissolving."]),
 ("Solutions, suspensions and colloids", ["Solution: very small particles; clear; does not settle; passes through filter paper; no Tyndall effect.",
   "Suspension (muddy water): large particles; settle on standing; can be filtered; scatter light.", "Colloid (milk): intermediate particles; do not settle; show the Tyndall effect."]),
]

MISTAKES = [
 "Mixing up solute and solvent; the solvent is the component present in larger amount that dissolves the other.",
 "Dividing the solute mass by the <i>solvent</i> mass instead of the mass of the <i>solution</i> in the percentage formula.",
 "Saying water dissolves everything; it is the universal solvent only in the sense that it dissolves many substances.",
 "Writing that the solubility of gases increases with temperature; it decreases.",
 "Calling milk a true solution; it is a colloid and shows the Tyndall effect.",
 "Forgetting that solubility is stated for 100 g of solvent at a given temperature, so the temperature must be mentioned.",
]
