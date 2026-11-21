"""Class 8 Science Ch 8 - Nature of Matter: Elements, Compounds and Mixtures: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8s_ch08"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_sci" / f"ch{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric checks
assert 118 - 11 - 2 == 105
assert 20 * 4 // 5 == 16 and 20 - 16 == 4          # 20 kg bronze, 4:1
assert abs(5.6 / 3.2 - 11.2 / 6.4) < 1e-9 and abs(11.2 + 6.4 - 17.6) < 1e-9 and abs(8 - 6.4 - 1.6) < 1e-9

WS = [
# ---------------- EASY ----------------
 W("Sand mixed with water is an example of a:", 1, "(b) non-uniform mixture. The sand grains can be seen separately from the water (1).", "E",
   opts=["uniform mixture", "non-uniform mixture", "compound", "element"]),
 W("In science, which of the following is a pure substance?", 1, "(c) distilled water. It contains only one kind of particle, whereas milk, soil and juice are mixtures (1).", "E",
   opts=["packed fruit juice", "milk", "distilled water", "soil"]),
 W("The two elements that are liquid at room temperature are:", 1, "(a) mercury and bromine (1).", "E",
   opts=["mercury and bromine", "mercury and gallium", "bromine and caesium", "sulfur and bromine"]),
 W("Lime water turns milky when a gas is passed through it. The gas is:", 1, "(d) carbon dioxide, which forms insoluble white calcium carbonate (1).", "E",
   opts=["hydrogen", "oxygen", "nitrogen", "carbon dioxide"]),
 W("A gas that burns with a 'pop' sound when a burning candle is brought near it is:", 1, "(b) hydrogen (1).", "E",
   opts=["oxygen", "hydrogen", "nitrogen", "carbon dioxide"]),
 W("Brass is a uniform mixture (alloy) of:", 1, "(a) copper and zinc (1).", "E",
   opts=["copper and zinc", "copper and tin", "iron and nickel", "zinc and carbon"]),
 W("Which of the following is NOT matter?", 1, "(c) light. Light, heat, electricity, thoughts and emotions are not matter (1).", "E",
   opts=["air", "water", "light", "sugar"]),
 W("True or false? Give a reason. 'Milk sold as pure milk is a pure substance in science.'", 2,
   "False (1). Milk is a mixture of many substances (water, fat, proteins, sugar etc.); 'pure' in daily life only means unadulterated (1).", "E"),
 W("Name two native minerals (minerals that are pure elements).", 2, "Any two of: gold, silver, copper, sulfur, carbon (1 + 1).", "E"),
 W("Classify each as an element, a compound or a mixture: oxygen, sugar, brass, soil.", 2,
   "Oxygen: element; sugar: compound; brass: mixture (alloy); soil: mixture (all 4 correct = 2 marks; 3 correct = 1) (2).", "E"),
 W("In water the atoms of hydrogen and oxygen are in the ratio ___ : ___. In common salt the atoms of sodium and chlorine are in the ratio ___ : ___.", 2,
   "2 : 1 for water (1); 1 : 1 for sodium chloride (1).", "E"),
 W("Which gas, smelling of rotten eggs, is given off when iron sulfide is treated with dilute hydrochloric acid?", 1, "Hydrogen sulfide (1).", "E"),
 W("Meena's lunch box has poha with peanuts, peas and curry leaves. Is this a uniform or a non-uniform mixture? Give a reason.", 2,
   "Non-uniform (1), because the peanuts, peas and curry leaves can be seen separately by the naked eye (1).", "E", wp=True),
 W("A blacksmith in Jodhpur says stainless steel utensils last longer than iron ones. What is stainless steel made of, and why is it preferred?", 2,
   "Stainless steel is an alloy of iron + nickel + chromium + a little carbon (1). Alloys are usually stronger and more durable than the pure metal (1).", "E", wp=True),
 W("A black sheet of paper kept near an open window for a few hours becomes covered with tiny specks. What are the specks? Are they a real part of air?", 2,
   "Dust particles (1). No - dust is suspended in air, is not a real part of air, varies from place to place and counts as a pollutant (1).", "E", wp=True),
 W("What does the Air Quality Index (AQI) tell us?", 1, "It describes the quality of the air, i.e. how polluted it is (1).", "E"),
 W("Give the scientific meaning of the word 'element' in one sentence and give one example.", 2,
   "An element is a pure substance made of only one kind of atom that cannot be broken down into simpler substances (1); e.g. gold / oxygen (1).", "E"),

# ---------------- MEDIUM ----------------
 W("A student writes: 'Sugar is an element because it is a pure substance.' Find the mistake and correct it.", 2,
   "Mistake: not every pure substance is an element (1). Sugar is a pure substance but it breaks down on heating into carbon and water, so it is a compound of carbon, hydrogen and oxygen (1).", "M"),
 W("Why does lime water kept in an open dish for a few hours turn milky? Write the reaction in words.", 2,
   "Carbon dioxide in the air reacts with calcium hydroxide (lime water) (1): calcium hydroxide + carbon dioxide → calcium carbonate + water; the insoluble white calcium carbonate makes it milky (1).", "M"),
 W("Two tubes collect gas when electricity is passed through acidified water. A student says the gas must be water vapour. Give two reasons why this is wrong.", 2,
   "Water vapour would condense back to water (1). One gas burns with a pop and the other makes a flame brighter, so they are hydrogen and oxygen, not vapour (1).", "M"),
 W("Of the 118 known elements, 11 are gases and 2 are liquids at room temperature. How many are solids? Name two of the gases.", 2,
   "118 − 11 − 2 = 105 solids (1). Gases (any two): oxygen, nitrogen, hydrogen, helium, etc. (1).", "M", wp=True),
 W("When sugar is heated gently in a boiling tube, it turns brown, then black, and droplets appear near the mouth of the tube. State what the droplets and the black residue are, and what this shows.", 3,
   "Droplets = water (1); black residue = carbon (charcoal) (1). Sugar splits into carbon and water, so it is not an element but a compound containing carbon, hydrogen and oxygen (1).", "M"),
 W("Name two tests by which you can tell Sample A (iron + sulfur mixed) from Sample B (iron + sulfur heated to a black mass).", 3,
   "Magnet: A - iron is attracted; B - not attracted (1.5). Dilute HCl: A gives hydrogen (pop sound, no smell); B gives hydrogen sulfide (rotten-egg smell) (1.5).", "M"),
 W("Ritu leaves salt solution in a plate in the sun and white salt remains. Her friend says this shows salt is a mixture of sodium and chlorine. Is the friend right? Explain.", 3,
   "No (1). Evaporation only separates salt from water, i.e. it separates a mixture (salt solution) (1). Sodium and chlorine are chemically combined 1 : 1 in salt and cannot be separated by any physical method, so salt is a compound (1).", "M", wp=True),
 W("In an experiment 30 mL of hydrogen is collected in the electrolysis of acidified water. Roughly how much oxygen is collected at the other terminal? Which tube would show the brighter flame with a candle?", 2,
   "Hydrogen : oxygen volumes are about 2 : 1, so oxygen ≈ 15 mL (1). The oxygen tube makes the candle flame glow brighter (1).", "M", wp=True),
 W("A traditional bronze (Kamsya) statue is made of 4 parts copper and 1 part tin. How much copper and tin are needed for a 20 kg statue?", 3,
   "Total parts = 5 (1). Copper = 4/5 × 20 = 16 kg (1); tin = 1/5 × 20 = 4 kg (1).", "M", wp=True),
 W("Gold is called a metal as well as a mineral. Explain.", 2,
   "As an element it is a metal by its type/properties (1); it is also a mineral because it occurs naturally in the Earth as a solid of fixed composition (a native mineral) (1).", "M"),
 W("Atoms of most elements cannot exist alone. How do hydrogen and oxygen exist in nature? Write the number of atoms in one molecule of each.", 2,
   "Two or more atoms join to form a stable molecule (1). A hydrogen molecule has 2 hydrogen atoms; an oxygen molecule has 2 oxygen atoms (1).", "M"),
 W("Match each substance to its category: (i) air (ii) mercury (iii) iron sulfide (iv) seawater.  Categories: element, compound, uniform mixture.", 3,
   "(i) uniform mixture (ii) element (iii) compound (iv) uniform mixture (all four correct = 3 marks; any three = 2) (3).", "M"),
 W("A dairy seller in Pushkar adds water to milk to increase its quantity. In daily life and in science, is the milk 'pure'? Explain both meanings.", 3,
   "Daily life: not pure, because it is adulterated (a cheaper substance was added) (1). Science: milk, with or without added water, is a mixture and so never 'pure' (1). Adulteration lowers quality and can harm health (1).", "M", wp=True),
 W("Classify as uniform or non-uniform: sugar in water, muddy water, vinegar, poha, air, sand and water.", 3,
   "Uniform: sugar in water, vinegar, air (1.5). Non-uniform: muddy water, poha, sand and water (1.5).", "M"),
 W("Name the physical state of the components in: (i) soda water (ii) smoke (soot in air) (iii) baking powder.", 3,
   "(i) gas in liquid (carbon dioxide dissolved in water) (1) (ii) solid in gas (soot particles in air) (1) (iii) solid + solid (baking soda and tartaric acid) (1).", "M"),
 W("Why must we never smell a gas by putting our nose directly over the test tube? What should we do instead?", 2,
   "Some gases (such as hydrogen sulfide) are harmful or irritating (1). Waft a little of the fumes towards the nose with the hand (1).", "M", wp=True),
 W("Explain how graphene aerogel might help during an oil-spill clean-up.", 2,
   "It is among the lightest materials, highly porous and absorbent (1), so it can soak up oil from the water (1).", "M"),
 W("In the school demonstration for splitting water, a few drops of dilute sulfuric acid are added to the water. Why? Which type of battery should not be used?", 2,
   "The acid helps the water to conduct electricity so that it can be split (1). A lithium-ion battery must not be used; a 9 V battery is used (1).", "M"),
 W("Describe how Dhokra metal-casters of Bihar and Odisha use an alloy.", 3,
   "The design is shaped in beeswax (1); it is covered with clay to make a mould and the wax is melted out (1); molten brass or bronze (alloys) is poured into the mould (1).", "M", wp=True),
 W("A mobile phone uses more than 45 different elements. Why is it important for engineers and chemists to know about elements and their properties?", 3,
   "Each element has particular properties (e.g. copper conducts, silicon is a metalloid, lithium in batteries) (1.5); knowing them lets engineers choose the right element or alloy for each part and chemists make new compounds, medicines and materials (1.5).", "M", wp=True),

# ---------------- HARD ----------------
 W("Water breaks into hydrogen and oxygen on passing electricity. A student concludes that water is just a mixture of hydrogen and oxygen. Give three arguments to prove water is a compound.", 3,
   "The two gases are combined in a fixed ratio (2 : 1) (1). Water's properties are totally different from those of hydrogen (fuel) and oxygen (supports burning) - water puts out fire (1). No physical method can separate the gases; electricity (a chemical change) is needed (1).", "H"),
 W("Iron filings (5.6 g) and sulfur powder (3.2 g) react completely on heating. Mohit takes 11.2 g of iron filings. (i) How much sulfur is needed to react completely? (ii) What mass of iron sulfide is formed? (iii) If he takes 8 g of sulfur instead, what is left over after heating, and is the final product pure?", 4,
   "(i) 11.2 g is twice 5.6 g, so sulfur = 2 × 3.2 = 6.4 g (1). (ii) 11.2 + 6.4 = 17.6 g of iron sulfide (1). (iii) 8 − 6.4 = 1.6 g sulfur is left (1); the product is iron sulfide mixed with unreacted sulfur, so it is a mixture, not pure (1).", "H", wp=True),
 W("Describe a simple experiment, with observations, to show that air contains (a) carbon dioxide and (b) dust particles.", 4,
   "(a) Leave lime water in a petri dish for a few hours, stirring now and then (1); it turns milky due to calcium carbonate, showing CO<sub>2</sub> (1). (b) Leave a clean black paper near an open window for some hours (1); tiny specks seen with a magnifier are dust (1).", "H"),
 W("Sample P is grey, shiny, attracted by a magnet and gives hydrogen (pop) with dilute HCl. Sample Q is black, not attracted by a magnet and gives a rotten-egg smelling gas with dilute HCl. Sample R is an even blend of P and a yellow powder S that can be separated with a magnet. Identify P, Q, R and S, and say which are pure substances.", 4,
   "P = iron (element) (1); S = sulfur (element) (0.5); Q = iron sulfide (compound) (1); R = mixture of iron and sulfur (1). Pure substances: P, S and Q; R is not pure (0.5).", "H"),
 W("Why is an alloy such as brass called a uniform mixture and not a compound? Give two points.", 3,
   "Copper and zinc in brass are not combined in a fixed ratio (the proportion can vary) (1.5); each metal keeps its own properties and can in principle be separated physically (1.5).", "H"),
 W("A factory wants a cheap compound to absorb carbon dioxide from air. Using what you learnt from lime water, suggest a compound, name the product formed and explain why it is a chemical change.", 3,
   "Calcium hydroxide (lime water / its solution) (1). It reacts with CO<sub>2</sub> to give calcium carbonate and water (1). A new substance with new properties (an insoluble white solid) is formed, so it is a chemical change (1).", "H", wp=True),
 W("A cement plant near Chittorgarh crushes rocks that contain calcite and quartz. (i) Is a rock a pure substance? (ii) What are calcite and quartz? (iii) Name two minerals and one product made from minerals.", 3,
   "(i) No - most rocks are mixtures of minerals (1). (ii) Minerals: natural solids found in the Earth with a fixed chemical composition (1). (iii) Quartz, calcite, mica, talc (any two); cement or talcum powder (1).", "H", wp=True),
 W("Assertion (A): Hydrogen is a fuel and oxygen supports burning, yet water extinguishes fire. Reason (R): A compound has properties different from the elements it is made of. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). Water is a new substance formed by chemical combination of H and O in 2 : 1 (1); its properties differ from both elements, which explains why it puts out fire (1).", "H"),
 W("Assertion (A): Evaporation can recover salt from salt solution. Reason (R): Salt is therefore a mixture of sodium and chlorine. Is A true? Is R true? Explain.", 3,
   "A is true: water evaporates leaving salt, a physical separation of a mixture (1). R is false (1): sodium and chlorine are chemically combined in a fixed 1 : 1 ratio in salt, and no physical method can separate them (1).", "H"),
 W("Compare the iron-sulfur mixture and iron sulfide under: appearance, effect of a magnet, effect of dilute HCl, and type of change in making each.", 4,
   "Appearance: mixture - black iron and yellow sulfur seen separately, non-uniform; iron sulfide - uniform black (1). Magnet: mixture - iron attracted; iron sulfide - not attracted (1). Dilute HCl: mixture - hydrogen (pop) with sulfur left unchanged; iron sulfide - rotten-egg smelling hydrogen sulfide (1). Change: mixing is physical, heating gives a chemical change (1).", "H"),
 W("<b>Case study.</b> Kavita's group heats sugar in a boiling tube and collects the following data. Observation 1: crystals turn brown, then black. Observation 2: droplets form near the open end. Observation 3: the black residue burns like coal. (i) Name the residue. (ii) Where do the droplets come from? Why not from the air? (iii) What type of substance is sugar? (iv) A student says 'the sugar melted, so it is a physical change'. Comment.", 5,
   "(i) Carbon / charcoal (1). (ii) From the sugar itself, which decomposes; the heated tube is not cooling air, so the water cannot be from the air (1). (iii) Compound of carbon, hydrogen and oxygen (1). (iv) Wrong - sugar does not just melt; new substances (carbon and water) form, so it is a chemical change (2).", "H", wp=True),
 W("A student reported: 'On adding dilute HCl to the iron-sulfur mixture I got a gas with a rotten-egg smell.' Which part of the report is probably wrong, and what would really be seen? Explain what the sample might have been instead.", 3,
   "The mixture contains free iron, which gives hydrogen, colourless and odourless, burning with a pop, with sulfur left as yellow solid (1.5). A rotten-egg smell is given by iron sulfide, so the sample was probably the heated black compound (1.5).", "H"),
 W("Arun says: 'Air is a compound because it is made of nitrogen, oxygen and other gases.' Rakhi says it is a mixture. Who is right? Give two pieces of evidence and name the main gas in air with its approximate percentage.", 3,
   "Rakhi is right (1). Evidence: the gases are not chemically combined in a fixed ratio and each keeps its own properties (e.g. oxygen supports burning, nitrogen does not); the amounts of water vapour, CO<sub>2</sub> and dust vary from place to place (1). Main gas: nitrogen, about 78% (1).", "H"),
]

_base = _old(8)
_i = max(i for i, b in enumerate(_base["blocks"]) if b[0] == "h2")      # 'Quick Questions' section
_extra = [
 ("h2", "Worked Examples and Reasoning Skills"),
 ("steps", [
   ("Example 1 — Classify the substance: element, compound or mixture?", "Ask three questions. (1) Can it be separated by a *physical* method (filtering, evaporating, magnet)? If yes, it is a **mixture**. (2) If it is pure but can be broken into simpler substances by a chemical change (heating, electricity), it is a **compound**. (3) If it cannot be broken down at all, it is an **element**. So: seawater → mixture; water → compound (electricity gives hydrogen and oxygen); mercury → element."),
   ("Example 2 — Iron and sulfur by mass", "From Activity 8.5, 5.6 g of iron reacts completely with 3.2 g of sulfur, so the two combine in the fixed ratio 5.6 : 3.2 = 7 : 4. For 11.2 g of iron, sulfur needed = 11.2 × 4/7 = 6.4 g and 11.2 + 6.4 = 17.6 g of iron sulfide is formed. If 8 g of sulfur was taken, 8 − 6.4 = **1.6 g sulfur is left over**, so the product is iron sulfide **plus** sulfur, a mixture. The *fixed ratio* is the signature of a compound."),
   ("Example 3 — Alloy by parts", "Bronze (*Kamsya*) = 4 parts copper (*Tamra*) + 1 part tin (*Vanga*). For a 20 kg statue the total parts = 5, so copper = 4/5 × 20 = 16 kg and tin = 1/5 × 20 = 4 kg. An alloy can be made in different proportions, which is why it is a mixture and not a compound."),
   ("Example 4 — Count the solids", "118 elements are known; 11 are gases and 2 are liquids (mercury, bromine) at room temperature. Solids = 118 − 11 − 2 = 105. Gallium and caesium are counted as solids because they melt only at about 30 °C."),
   ("Example 5 — Electrolysis of water by volume", "Hydrogen and oxygen collect in the volume ratio about 2 : 1. If 30 mL of hydrogen collects, about 15 mL of oxygen collects. The tube with *more* gas is hydrogen (pop with a flame); the other gives a brighter candle flame (oxygen)."),
 ]),
 ("h2", "Physical Change, Chemical Change and Separation"),
 ("table", ["Question to ask", "If the answer is yes", "Example from the chapter"], [
   ["Are new substances with new properties formed?", "**Chemical change**; a compound may be formed or broken", "Heating iron + sulfur; passing electricity through water; heating sugar; lime water + CO<sub>2</sub>"],
   ["Do the components keep their own properties?", "**Mixture** (physical mixing only)", "Iron filings + sulfur powder mixed cold; sprout salad; air"],
   ["Can a magnet / filter / evaporation separate the parts?", "Physical separation; it was a **mixture**", "Iron from sulfur with a magnet; salt from salt solution by evaporation"],
   ["Can no physical method split it, but electricity or heat does?", "**Compound**", "Water, sugar, sodium chloride"]]),
 ("note", "REMEMBER", "**Common mistakes:** (1) 'Pure' in daily life means unadulterated; in science it means one kind of particle. (2) Every element is a pure substance and so is every compound, but not every pure substance is an element. (3) Evaporating salt from salt solution does **not** prove salt is a mixture — it separates the *solution*. (4) Hydrogen sulfide (rotten egg) comes from iron **sulfide** + HCl, hydrogen (pop, no smell) from iron + HCl. (5) Air is a mixture even though we call it 'pure air' in daily life. (6) Dust is not a component of air; it is a pollutant."),
 ("h2", "Real-Life Connections"),
 ("ul", ["**Kitchen:** salad, poha, lemonade, soup are mixtures; sugar and salt are pure substances; heating sugar to caramel shows it can decompose.",
         "**Metals at home:** brass pots (copper + zinc), bronze bells and statues (copper + tin) and stainless-steel utensils (iron, nickel, chromium, carbon) are alloys chosen for strength and durability.",
         "**Health and farming:** chemists combine elements to make medicines, vaccines and fertilisers; adulteration lowers quality, so buying from reliable sources and checking labels matters.",
         "**Environment:** the Air Quality Index tells us about particulate matter and gases such as CO, O<sub>3</sub>, NO<sub>2</sub> and SO<sub>2</sub>; lime water in the lab shows carbon dioxide; graphene aerogel is a research material for oil-spill clean-up.",
         "**Earth materials:** cement from calcite, quartz, alumina and iron oxide; talcum powder from talc; Dhokra art in brass and bronze."]),
 ("h2", "Differences at a Glance: Quick Comparison Table"),
 ("table", ["Pair", "First", "Second"], [
   ["Uniform / non-uniform mixture", "Parts evenly spread, cannot be distinguished (sugar in water, air, brass)", "Parts visible separately (sand and water, poha, salad)"],
   ["Everyday / scientific 'pure'", "Not adulterated", "Only one kind of particle"],
   ["Atom / molecule", "Smallest unit of an element", "Two or more atoms joined (H<sub>2</sub>, O<sub>2</sub>, H<sub>2</sub>O)"],
   ["Metal / non-metal / metalloid", "Metal: gold, iron, aluminium", "Non-metal: carbon, sulfur, oxygen; metalloid: silicon, boron"],
   ["Mineral / native mineral", "Natural solid of fixed composition (quartz, calcite)", "A mineral that is a single element (gold, sulfur, carbon)"]]),
]
_qa2 = [
  ("How can you show that the gas collected on passing electricity through water is not water vapour?", "Vapour would condense back to water; instead one gas burns with a pop (hydrogen) and the other brightens a candle flame (oxygen)."),
  ("A teacher says the iron-sulfur mixture and iron sulfide look different. Why?", "The mixture is a physical blend (each keeps its properties); heating makes a new compound with new properties."),
  ("Why is air a mixture and not a compound?", "Its gases (mostly nitrogen, about 78%, and oxygen) are not chemically combined in a fixed ratio and each keeps its own properties."),
]
_blocks = list(_base["blocks"])
_blocks[_i + 1] = ("qa", list(_blocks[_i + 1][1]) + _qa2)
CH = dict(_base, blocks=_blocks[:_i] + _extra + _blocks[_i:],
          takeaways=_base["takeaways"] + ["The **fixed mass ratio** (iron : sulfur = 7 : 4) shows a compound; a variable proportion shows a mixture or alloy.",
                                          "Test gases: **hydrogen** burns with a pop; **oxygen** brightens a flame; **CO<sub>2</sub>** turns lime water milky; **H<sub>2</sub>S** smells of rotten eggs."])

if __name__ == "__main__":
    run(__file__, BANK, 8, "Science", WS, CH)
