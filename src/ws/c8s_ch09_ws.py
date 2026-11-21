"""Class 8 Science Ch 9 - The Amazing World of Solutes, Solvents and Solutions: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8s_ch09"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_sci" / f"ch{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric checks
assert 50 / 25 == 2 and 5 * 4 * 2 == 40 and abs(312 / 40 - 7.8) < 1e-9
assert 52 - 40 == 12 and abs(31.2 / 12 - 2.6) < 1e-9 and 2.5 * 1000 * 0.91 == 2275
assert abs(120 / 100 - 1.2) < 1e-9 and abs(80 / 100 - 0.8) < 1e-9 and abs(150 / 200 - 0.75) < 1e-9 and 54 / 20 == 2.7
assert 20 * 10 * 5 == 1000 and 700 / 1000 == 0.7
assert (70 - 50) == 20 and abs(52 / 20 - 2.6) < 1e-9 and (65 - 50) == 15 and 45 / 15 == 3.0
assert 24 / 8 == 3.0 and 58 - 50 == 8 and 250 * 20 / 100 == 50 and 60 - 50 == 10
assert (4 / 50) / (2 / 100) == 4 and abs(910 / 0.91 - 1000) < 1e-9 and 910 / 1.0 == 910

WS = [
# ---------------- EASY ----------------
 W("In a solution of sugar in water, the solute is:", 1, "(a) sugar, the substance that dissolves; water is the solvent (1).", "E",
   opts=["sugar", "water", "both", "neither"]),
 W("A solution in which no more solute can be dissolved at a given temperature is called:", 1, "(c) a saturated solution (1).", "E",
   opts=["a dilute solution", "an unsaturated solution", "a saturated solution", "a suspension"]),
 W("The SI unit of density is:", 1, "(b) kg/m<sup>3</sup> (1).", "E",
   opts=["kg/m<sup>2</sup>", "kg/m<sup>3</sup>", "g/m", "N/m<sup>3</sup>"]),
 W("With a rise in temperature, the solubility of most solids in water:", 1, "(a) increases (1).", "E",
   opts=["increases", "decreases", "stays the same", "first decreases and then increases"]),
 W("Which of the following is NOT a uniform mixture?", 1, "(d) chalk powder in water. Its parts can be seen separately, so it is non-uniform (1).", "E",
   opts=["sugar in water", "air", "ORS solution", "chalk powder in water"]),
 W("The density of a sample of a substance does NOT depend on:", 1, "(b) the size or shape of the sample. It depends on temperature and pressure (1).", "E",
   opts=["temperature", "size or shape of the sample", "pressure on a gas", "kind of material"]),
 W("To read the volume of colourless water in a measuring cylinder, the eye should be level with:", 1, "(c) the bottom of the meniscus (1).", "E",
   opts=["the top of the cylinder", "the top of the meniscus", "the bottom of the meniscus", "the base of the cylinder"]),
 W("In a mixture of 10 mL of ethanol and 90 mL of water, which liquid is the solute and which is the solvent?", 2,
   "In a solution of two liquids the one in the smaller amount is the solute: ethanol = solute (1); water = solvent (1).", "E"),
 W("A metal cube has mass 50 g and volume 25 cm<sup>3</sup>. Find its density.", 2,
   "Density = mass ÷ volume (1) = 50 ÷ 25 = 2 g/cm<sup>3</sup> (1).", "E"),
 W("Convert 1 g/cm<sup>3</sup> into kg/m<sup>3</sup>.", 1, "1 g/cm<sup>3</sup> = 1000 kg/m<sup>3</sup> (1).", "E"),
 W("While washing rice at home, Kavya sees husk floating while the rice grains sink. What does this tell you about the density of husk and of rice compared with water?", 2,
   "Husk floats, so its density is less than that of water (1); rice sinks, so its density is more than that of water (1).", "E", wp=True),
 W("Ravi adds salt to water spoon by spoon and stirs. After 6 spoons a little salt settles at the bottom. What kind of solution is it now? What will happen if he adds one more spoon?", 2,
   "A saturated solution at that temperature (1). The extra salt will not dissolve; it will settle at the bottom (1).", "E", wp=True),
 W("A one-litre packet of oil has a mass of 910 g. Will the oil float or sink in water? Give a reason.", 2,
   "It will float (1). Its density is 910 g ÷ 1000 cm<sup>3</sup> = 0.91 g/cm<sup>3</sup>, less than the density of water (1 g/cm<sup>3</sup>) (1).", "E", wp=True),
 W("Why does an unpeeled orange float in water while a peeled orange sinks?", 2,
   "The peel traps air (1), which lowers the overall density of the unpeeled orange to below that of water (1).", "E", wp=True),
 W("Why are measuring cylinders made tall and narrow instead of wide?", 2,
   "In a narrow tube a small change in volume makes a large change in height (1), so the volume can be read more accurately (1).", "E"),
 W("What is the use of the 'tare' button on a digital balance?", 1, "It sets the display to zero with the empty container on the pan so that only the mass of the object is read (1).", "E"),
 W("About what mass does 100 mL of water have at room temperature? What is the density of water in g/mL?", 2,
   "About 100 g (1); density about 1 g/mL (1).", "E"),

# ---------------- MEDIUM ----------------
 W("A student says: 'Dilute solution and unsaturated solution mean the same thing, and concentrated means saturated.' Find the mistake.", 2,
   "Dilute and concentrated are relative terms for how much solute is present in a quantity of solution (1). Saturated and unsaturated tell whether the solution has reached its limit at that temperature; a very dilute solution is unsaturated, but a concentrated solution need not be saturated (1).", "M"),
 W("Anita makes two solutions: P has 4 spoons of salt in 50 mL of water, Q has 2 spoons of salt in 100 mL of water. Which is more concentrated, and how many times?", 3,
   "Compare the solute in the same volume (1). P: 4 spoons per 50 mL = 8 spoons per 100 mL (1); Q: 2 spoons per 100 mL. P is 8 ÷ 2 = 4 times more concentrated (1).", "M", wp=True),
 W("At 30 °C a substance X dissolves up to 20 g in 100 mL of water. A student adds 60 g of X to 250 mL of water at 30 °C and stirs well. How much dissolves and how much settles? What happens when the mixture is warmed (X is a solid)?", 3,
   "Maximum in 250 mL = 20 × 250 ÷ 100 = 50 g dissolves (1); 60 − 50 = 10 g settles at the bottom (1). On warming, solubility of a solid increases, so the remaining solid dissolves and the solution becomes unsaturated (1).", "M", wp=True),
 W("In the summer, many fish in a shallow pond near Udaipur die when the water becomes very warm. Explain why.", 2,
   "Oxygen dissolved in water supports aquatic life (1). Solubility of gases decreases as temperature rises, so warm water holds less oxygen and fish do not get enough (1).", "M", wp=True),
 W("An iron block is 5 cm × 4 cm × 2 cm and has a mass of 312 g. Find its volume and density. Will it float in water?", 3,
   "Volume = 5 × 4 × 2 = 40 cm<sup>3</sup> (1). Density = 312 ÷ 40 = 7.8 g/cm<sup>3</sup> (1). It is more than 1 g/cm<sup>3</sup>, so it sinks (1).", "M", wp=True),
 W("Sana finds the volume of a small stone by displacement: initial level of water 40 mL, final level 52 mL after lowering the stone. The mass of the stone is 31.2 g. Find its volume and density.", 3,
   "Volume = 52 − 40 = 12 mL = 12 cm<sup>3</sup> (1). Density = 31.2 ÷ 12 (1) = 2.6 g/cm<sup>3</sup> (1).", "M", wp=True),
 W("27 g of aluminium has a volume of 10 cm<sup>3</sup>. Find its density and its relative density. What does the relative density tell you?", 3,
   "Density = 27 ÷ 10 = 2.7 g/cm<sup>3</sup> (1). Relative density = 2.7 ÷ 1 = 2.7, with no unit (1). It tells us aluminium is 2.7 times as dense as water (1).", "M"),
 W("Convert (i) 2.7 g/cm<sup>3</sup> into kg/m<sup>3</sup> (ii) 500 kg/m<sup>3</sup> into g/cm<sup>3</sup>.", 2,
   "(i) 2.7 × 1000 = 2700 kg/m<sup>3</sup> (1). (ii) 500 ÷ 1000 = 0.5 g/cm<sup>3</sup> (1).", "M"),
 W("To measure 70 mL of water you have 50 mL, 100 mL and 500 mL measuring cylinders. Which is the best and why?", 2,
   "The 100 mL cylinder (1): it measures 70 mL in one step with good accuracy; 50 mL needs two steps and 500 mL is less accurate (1).", "M", wp=True),
 W("Between the marks 0 and 50 mL of a 250 mL measuring cylinder there are 25 equal divisions. Find the least count. What volume is read if the bottom of the meniscus is 3 divisions above the 40 mL mark?", 2,
   "Least count = 50 ÷ 25 = 2 mL (1). Volume = 40 + 3 × 2 = 46 mL (1).", "M"),
 W("Why does hot air rise? Why does a hot-air balloon go up when its air is heated?", 3,
   "On heating, the air expands (volume increases) while its mass stays the same (1), so its density decreases (1). The balloon's hot air is less dense than the cooler air around it and rises, lifting the balloon (1).", "M"),
 W("Riya's egg sinks in a glass of tap water. What can she add to the water to make the egg float, and why does it work?", 3,
   "Common salt (1). Dissolving salt increases the density of the liquid (1). When the liquid's density becomes greater than that of the egg, the egg floats (1).", "M", wp=True),
 W("In winter the water at the surface of a pond in a hill station freezes, yet the fish below survive. Explain with reference to ice and water.", 3,
   "Water expands on freezing, so ice has lower density than liquid water and floats (1). The floating ice layer on top acts as an insulator (1). The water below does not freeze, keeping fish alive (1).", "M", wp=True),
 W("How does the density of the material change as we go from the Earth's crust towards its centre? Give a reason.", 2,
   "Density increases towards the centre (1), because pressure and temperature rise and the material is more compact (1).", "M"),
 W("While making gulab jamun, Mrs Sharma dissolves 500 g sugar in only 250 mL of water. Name the solute and the solvent. Is it correct to call the solvent water although it is smaller in amount than sugar? Explain.", 2,
   "Solute = sugar; solvent = water (1). Yes - for a solid dissolved in a liquid, the liquid is the solvent, even if the solid is present in larger mass (1).", "M", wp=True),
 W("Describe the activity that shows that heating can dissolve more baking soda in water.", 3,
   "Take about 50 mL water at room temperature (~20 °C) and add baking soda until some remains undissolved (1). Heat to 50 °C with stirring - the undissolved soda dissolves (1); add more soda until some remains, heat to 70 °C - it dissolves again, showing solubility increases with temperature (1).", "M"),
 W("The gas in an LPG cylinder is compressed. Explain, in terms of density, what happens to a gas when pressure on it is increased. Why is this effect small for solids?", 2,
   "On increasing pressure the particles of the gas come closer, volume decreases and density increases (1). Particles in solids are already tightly packed, so volume and density hardly change (1).", "M", wp=True),
 W("Differentiate between mass and weight with their units. Which of them changes from place to place?", 2,
   "Mass: quantity of matter in an object, in g or kg; weight: the force with which the Earth attracts the object, in newton (1). Weight changes from place to place; mass stays constant (1).", "M"),
 W("Oil has a density of 0.91 g/cm<sup>3</sup>. Neha buys 2.5 L of oil from a shop in Jaipur. Find the mass of the oil in grams and in kg. (1 L = 1000 cm<sup>3</sup>)", 3,
   "Volume = 2.5 × 1000 = 2500 cm<sup>3</sup> (1). Mass = density × volume = 0.91 × 2500 = 2275 g (1) = 2.275 kg (1).", "M", wp=True),

 W("A student needs 25 mL of coloured juice from a measuring cylinder. Where should he read the meniscus, and how should he place the cylinder and his eye?", 2,
   "Place the cylinder on a flat surface and keep the eye level with the meniscus (1); for a coloured liquid read the top of the meniscus (for colourless water, the bottom) (1).", "M", wp=True),

# ---------------- HARD ----------------
 W("The table gives the mass and volume of four solid samples: A (120 g, 100 cm<sup>3</sup>); B (80 g, 100 cm<sup>3</sup>); C (150 g, 200 cm<sup>3</sup>); D (54 g, 20 cm<sup>3</sup>). Find the density of each, state which would float in water, and arrange them in order of increasing density.", 4,
   "A = 1.2, B = 0.8, C = 0.75, D = 2.7 g/cm<sup>3</sup> (2). Float (density less than 1 g/cm<sup>3</sup>): B and C (1). Increasing order: C < B < A < D (1).", "H"),
 W("A wooden block measures 20 cm × 10 cm × 5 cm and has a mass of 700 g. (i) Find its density. (ii) Will it float in water? (iii) The block is cut into two equal halves. What is the density of one half? Give a reason.", 4,
   "(i) Volume = 1000 cm<sup>3</sup>; density = 700 ÷ 1000 = 0.7 g/cm<sup>3</sup> (2). (ii) Yes, 0.7 is less than 1 (1). (iii) Still 0.7 g/cm<sup>3</sup>, since density does not depend on the size or shape of the sample (1).", "H", wp=True),
 W("Two stones are lowered one by one into a measuring cylinder containing 50 mL of water (the first stone is removed before the second is put in). Stone P (52 g) raises the level to 70 mL; stone Q (45 g) raises it to 65 mL. Find the density of each and say which is denser.", 4,
   "P: volume 70 − 50 = 20 cm<sup>3</sup>, density 52 ÷ 20 = 2.6 g/cm<sup>3</sup> (1.5). Q: volume 65 − 50 = 15 cm<sup>3</sup>, density 45 ÷ 15 = 3.0 g/cm<sup>3</sup> (1.5). Q is denser although it is lighter (1).", "H", wp=True),
 W("Explain, in terms of mass, volume and density, how a hot-air balloon rises, and why a balloon filled with cooled air would not.", 3,
   "Heating the air expands it; its mass stays the same but volume increases, so density = mass ÷ volume falls (1). Hot air inside is less dense than the surrounding cooler air, so it rises with the balloon (1). Cooled air has higher density than (or the same as) the surrounding air, so no upward lift (1).", "H"),
 W("Water has its highest density at 4 °C. Explain what happens to the density when water at 4 °C is cooled to 0 °C and then freezes, and how this helps aquatic life in a cold lake.", 3,
   "On freezing at 0 °C, water's particles arrange in a structure that takes more space; mass is the same but volume increases, so density falls (1). Ice, being less dense, floats instead of sinking (1). The ice layer on top insulates the water below, so fish and other animals survive (1).", "H"),
 W("<b>Case study.</b> Sunita uses a 100 mL measuring cylinder with a mark every 10 mL and 10 small divisions between marks. She puts 50 mL of water in it, ties a small metal ball with a thread and lowers it. The water level rises to 58 mL. The ball's mass on a digital balance (after taring with a watch glass) is 24 g. (i) What is the least count? (ii) Where should her eye be while reading? (iii) Find the volume and density of the ball in g/cm<sup>3</sup> and kg/m<sup>3</sup>. (iv) Will the ball float in water?", 5,
   "(i) 10 ÷ 10 = 1 mL (1). (ii) Eye level with the bottom of the meniscus (1). (iii) Volume = 58 − 50 = 8 cm<sup>3</sup> (1); density = 24 ÷ 8 = 3 g/cm<sup>3</sup> = 3000 kg/m<sup>3</sup> (1). (iv) No, it sinks as 3 g/cm<sup>3</sup> is more than 1 g/cm<sup>3</sup> (1).", "H", wp=True),
 W("Assertion (A): Solubility of oxygen in a lake falls in summer. Reason (R): Solubility of gases in liquids decreases when the temperature rises. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Give a reason.", 3,
   "(a) (1). Warm water holds less dissolved oxygen because the solubility of gases decreases with rising temperature (1), which explains why the oxygen level in the lake falls in summer (1).", "H"),
 W("Assertion (A): Pressure has a large effect on the density of gases but a negligible effect on solids. Reason (R): Gas particles are far apart and can be pushed closer, but solid particles are already tightly packed. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). Increasing pressure pushes gas particles closer, so volume decreases and density increases (1); in solids there is almost no space to compress, so density hardly changes (1).", "H"),
 W("Oil has a density of 0.91 g/cm<sup>3</sup> and water 1 g/cm<sup>3</sup>. Find the volumes of 910 g of oil and 910 g of water. Which is larger, and what does this show about floating?", 3,
   "Oil: 910 ÷ 0.91 = 1000 cm<sup>3</sup>; water: 910 ÷ 1 = 910 cm<sup>3</sup> (2). Oil's volume is larger for the same mass, so it is less dense and floats on water (1).", "H", wp=True),
 W("A saturated solution of a solid is prepared at 60 °C and then cooled to 20 °C. What would you observe and why? Which two terms describe the solution at 20 °C?", 3,
   "Some solid settles at the bottom (1) because solubility of a solid decreases when the temperature falls (1). At 20 °C the liquid is a saturated solution (with undissolved solute) at that temperature (1).", "H"),
 W("Mercury has a relative density of 13.6, iron 7.8 and water 1. (i) What is the density of mercury in g/cm<sup>3</sup>? (ii) Would an iron nail float in water? (iii) Would it float on mercury? Give reasons.", 3,
   "(i) 13.6 g/cm<sup>3</sup> (relative density × density of water) (1). (ii) No, 7.8 is more than 1, so it sinks (1). (iii) Yes, 7.8 is less than 13.6, so the nail is less dense than mercury and floats (1).", "H"),
 W("Priya's mother makes ORS at home with sugar and salt in water, and Priya notes the first sip and last sip taste the same. Give the scientific reason. How would the drink change if a lot more sugar is added and the water is cold? Explain using suitable terms.", 3,
   "It is a uniform mixture (solution) - sugar and salt are evenly distributed (1). If too much sugar is added to cold water, the solution may become saturated and extra sugar settles at the bottom (1) because the solubility of the solid is lower at low temperature; warming the water would dissolve more (1).", "H", wp=True),
 W("Priyank says: 'A body that floats must be lighter in mass than one that sinks.' Use the example of a large wooden log and a small iron nail to explain whether his statement is correct.", 3,
   "The statement is wrong (1). A large log has more mass than a nail, yet the log floats and the nail sinks (1). Floating depends on density (mass per unit volume): wood is less dense than water and iron is denser (1).", "H", wp=True),
]

_base = _old(9)
_i = max(i for i, b in enumerate(_base["blocks"]) if b[0] == "h2")
_extra = [
 ("h2", "Worked Examples: Density, Concentration and Solubility"),
 ("steps", [
   ("Example 1 — Density of a regular solid", "A brass cuboid measures 5 cm × 4 cm × 2 cm and has a mass of 336 g. Volume = 5 × 4 × 2 = 40 cm³. Density = 336 ÷ 40 = **8.4 g/cm³** = 8400 kg/m³. Since 8.4 is more than 1, it sinks in water."),
   ("Example 2 — Density of an irregular solid by displacement", "Initial level 50 mL; with the stone 55 mL. Volume of stone = 55 − 50 = 5 mL = 5 cm³. If its mass is 16.4 g, density = 16.4 ÷ 5 = **3.28 g/cm³**."),
   ("Example 3 — Mass from density and volume", "Oil of density 0.91 g/cm³, volume 2.5 L = 2500 cm³. Mass = density × volume = 0.91 × 2500 = 2275 g = **2.275 kg**. (Rearranged formulas: mass = density × volume; volume = mass ÷ density.)"),
   ("Example 4 — Comparing concentrations", "Solution P: 4 spoons of salt in 50 mL; solution Q: 2 spoons in 100 mL. Bring both to the same volume (100 mL): P has 8 spoons, Q has 2. P is **4 times** more concentrated."),
   ("Example 5 — Solubility problem", "Solubility of a solid X is 20 g per 100 mL at 30 °C. In 250 mL it can dissolve 20 × 250 ÷ 100 = 50 g. If 60 g is added, **10 g** stays undissolved; warming dissolves more because the solubility of solids rises with temperature."),
   ("Example 6 — Unit conversion", "1 g/cm³ = 1000 kg/m³. So 2.7 g/cm³ = 2700 kg/m³ and 500 kg/m³ = 0.5 g/cm³. Also 1 L = 1000 mL = 1000 cm³ = 1 dm³."),
 ]),
 ("h2", "Floating and Sinking: What Decides It?"),
 ("table", ["If", "Then the object", "Example"], [
   ["Density of object is **less** than density of the liquid", "Floats", "Husk, oil on water, wood, an unpeeled orange, ice"],
   ["Density of object is **more** than density of the liquid", "Sinks", "Rice grains, sand, iron nail, a stone in water; iron floats on mercury only because mercury is denser"],
   ["Liquid is made denser (dissolving salt)", "An object that sank may now float", "Raw egg in salt water"],
   ["Air is trapped inside or around the object", "Overall density decreases", "Unpeeled orange; hollow bamboo and wooden rafts"]]),
 ("note", "REMEMBER", "**Common mistakes:** (1) Mixing up the two liquids: in a mixture of two liquids the one in the **smaller** amount is the solute. (2) Reading the top of the meniscus for colourless liquids — read the **bottom**. (3) Believing a heavier object always sinks: a log has more mass than a nail but a lower density. (4) Writing density in g/cm³ and forgetting that 1 g/cm³ = **1000** kg/m³. (5) Thinking solubility of every substance rises with temperature — it **falls** for gases. (6) Calling a dilute solution 'unsaturated' by definition; they are different ideas."),
 ("h2", "Real-Life Connections"),
 ("ul", ["**Kitchen:** ORS, lemonade, sharbat and chashni are solutions; adding more sugar to cold tea leaves undissolved sugar at the bottom (saturated), while hot tea dissolves more.",
         "**Aquatic life:** warm ponds and lakes (for example in a Rajasthan summer) hold less dissolved oxygen, which can kill fish; cold water bodies hold more.",
         "**Sports and travel:** a hot-air balloon rises because heated air is less dense; a life jacket works because it has a lower overall density than water.",
         "**Everyday density:** cooking oil floats on water (0.91 g/cm³); an egg floats in strongly salty water; a peeled orange sinks and an unpeeled one floats.",
         "**Earth and medicine:** density increases towards the Earth's core; Asima Chatterjee used solvents to extract medicines from plants."]),
 ("h2", "Summary Table: Key Terms and Formulae"),
 ("table", ["Term", "Definition / formula", "Unit"], [
   ["Solution", "Uniform mixture of solute and solvent", "-"],
   ["Solubility", "Maximum solute in a fixed amount of solvent at a given temperature", "g per 100 mL (or 100 g) of solvent"],
   ["Density", "Mass ÷ volume", "kg/m³; g/cm³ (g/mL)"],
   ["Mass", "d × V (from density and volume)", "g, kg"],
   ["Volume", "m ÷ d; of a cuboid l × b × h; of an irregular solid = final level − initial level", "cm³, mL, m³, L"],
   ["Relative density", "Density of substance ÷ density of water", "No unit"],
   ["Least count", "Value between two big marks ÷ number of small divisions", "mL"]]),
]
_qa2 = [
  ("A solid of mass 54 g has a volume of 20 cm³. Find its density and say whether it floats.", "Density = 54 ÷ 20 = 2.7 g/cm³; more than that of water, so it sinks."),
  ("Why are the readings of a measuring cylinder more accurate than those of a beaker?", "The cylinder is tall and narrow, so small volume changes show as large level changes."),
  ("What is the effect of temperature on the density of a substance?", "Heating increases volume at constant mass, so density decreases; cooling raises it (water is densest at 4 °C)."),
]
_blocks = list(_base["blocks"])
_blocks[_i + 1] = ("qa", list(_blocks[_i + 1][1]) + _qa2)
CH = dict(_base, blocks=_blocks[:_i] + _extra + _blocks[_i:],
          takeaways=_base["takeaways"] + ["Rearranged: **mass = density × volume** and **volume = mass ÷ density**; 1 g/cm³ = 1000 kg/m³.",
                                          "Floating or sinking depends on **density**, not just mass: an object floats if it is less dense than the liquid."])

if __name__ == "__main__":
    run(__file__, BANK, 8, "Science", WS, CH)
