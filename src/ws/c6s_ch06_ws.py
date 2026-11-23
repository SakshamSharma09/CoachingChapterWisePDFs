"""Class 6 Science Ch 6 - Materials Around Us: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch06"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch06", str(REPO / "src/rn_work/c6_sci/ch06.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Any substance used to make an object is called a:", 1, "(c) material", "E", opts=["matter", "volume", "material", "mass"]),
W("Which of these is a lustrous material?", 1, "(b) copper", "E", opts=["wood", "copper", "paper", "jute"]),
W("Materials through which we cannot see at all are called:", 1, "(a) opaque", "E", opts=["opaque", "transparent", "translucent", "soluble"]),
W("Which of these dissolves completely in water?", 1, "(d) sugar", "E", opts=["sand", "chalk powder", "sawdust", "sugar"]),
W("The SI unit of mass is the:", 1, "(b) kilogram", "E", opts=["gram", "kilogram", "litre", "metre"]),
W("Anything that has mass and occupies space is called:", 1, "(c) matter", "E", opts=["energy", "light", "matter", "heat"]),
W("Fill in the blank: Butter paper is an example of a ______ material.", 1, "translucent.", "E"),
W("Fill in the blank: The space occupied by a material is called its ______.", 1, "volume.", "E"),
W("Name the SI unit of volume.", 1, "Cubic metre (m3). (1)", "E"),
W("Write True or False: All shiny objects are made of metals.", 1, "False. Polished or coated non-metals may also shine. (1)", "E"),
W("Write True or False: Air is matter.", 1, "True. Air has mass and occupies space. (1)", "E"),
W("Give two examples of hard materials and two of soft materials.", 2, "Hard: stone, iron, brick. Soft: eraser, sponge, candle. (Any two of each, 1+1)", "E"),
W("Give two examples of transparent materials.", 2, "Any two: glass, water, air, cellophane, window glass. (1+1)", "E"),
W("Name two non-lustrous materials.", 2, "Any two: paper, wood, rubber, jute. (1+1)", "E"),
W("What is classification?", 1, "Arranging objects into groups on the basis of a common property. (1)", "E"),
W("Write the units of volume mentioned in the chapter besides m3.", 1, "Litre (L) and millilitre (mL). (1)", "E"),
W("Name the baked clay that was used in ancient pottery.", 1, "Terracotta. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Classify these as soluble or insoluble in water: salt, sand, sugar, chalk powder, sawdust.", 3, "Soluble: salt, sugar. Insoluble: sand, chalk powder, sawdust. (1.5 for each group)", "M"),
W("Why are window panes made of glass and not of wood? Which property is used?", 2, "Glass is transparent, so we can see through it and light comes in; wood is opaque. (2)", "M", wp=True),
W("Why is a cooking pot not made of paper or cloth but of metal? Explain with properties.", 3, "A cooking utensil must be hard, strong and withstand heat, which paper cannot (1.5). Materials are chosen for their properties and the purpose of the object (1.5).", "M", wp=True),
W("Why are tennis, cricket and hand-exercise balls made of different materials?", 2, "Each game needs a different bounce, hardness and size, so the material is chosen for the purpose. (2)", "M", wp=True),
W("Hardness is called a relative property. Explain with rubber as an example.", 3, "Rubber is harder than a sponge (1) but softer than iron (1). So a material may be hard or soft only in comparison with another (1).", "M"),
W("How can you test whether a material is hard or soft in the class? Write two steps.", 2, "Try to scratch or press the material with a metal key or coin (1). If it is easily scratched or compressed it is soft, otherwise hard (1).", "M", wp=True),
W("Table: Glass, butter paper, plywood. Write transparent, translucent or opaque for each and give a use.", 3, "Glass: transparent, used in windows. Butter paper: translucent, used to wrap sweets. Plywood: opaque, used in furniture. (1 each)", "M", wp=True),
W("Why does a shopkeeper keep biscuits in transparent jars?", 1, "Customers can see the contents without opening the jar. (1)", "M", wp=True),
W("How is ORS prepared at home? Why is it useful?", 3, "Mix six teaspoons of sugar and half a teaspoon of salt in one litre of boiled and cooled water (2). It gives water, salt and sugar to a person suffering from dehydration (1).", "M", wp=True),
W("Why does an iron nail kept in the open lose its shine, but freshly cut iron shines?", 2, "Air and moisture act on iron and the surface loses its lustre (1). A freshly cut surface is clean and shows its shine (1).", "M"),
W("Two cups of equal size are half-filled with sand and with water. The cup with sand is heavier. Which quantity is different and what is the name for 'heaviness'?", 2, "Mass is different (1). The sand has more mass than the water. (1)", "M", wp=True),
W("Why is oxygen dissolved in water important?", 2, "Aquatic plants and animals use dissolved oxygen to survive. (2)", "M"),
W("Find the mistake: \"A glass of milk is matter but air is not, because we cannot see air.\"", 2, "Air is also matter; it has mass and occupies space even though we cannot see it. (2)", "M"),
W("Sort into lustrous / non-lustrous: gold ring, jute rope, aluminium foil, rubber band, copper wire.", 3, "Lustrous: gold ring, aluminium foil, copper wire. Non-lustrous: jute rope, rubber band. (1.5 + 1.5)", "M", wp=True),
W("Why do bottles and packets show units like 500 mL and 1 L?", 2, "They show the volume of the liquid inside. (2)", "M"),
W("Write the correct way of writing: 7 kgs; 500 ml.; 2 M3; 1 Litre.", 2, "7 kg; 500 mL; 2 m3; 1 L (any two corrected 1 mark, all four 2 marks).", "M"),
W("An object can be made of one material or many. Give one example of each.", 2, "One material: an iron nail. Many materials: a pen made of plastic, metal and ink. (1+1)", "M"),
W("Why are objects classified in kitchens and chemist shops?", 2, "Classification helps us to find things easily and quickly. (2)", "M", wp=True),
W("Ancient clay pots stored water for years without dissolving. Name two properties of baked clay that made this possible.", 2, "Baked clay is hard (1) and insoluble in water (1).", "M"),
W("Describe one feature of Harappan pottery (2600-1900 BCE).", 2, "Bright red surface with black geometric and animal designs. (2)", "M"),
# ---------------- HARD ----------------
W("Ritu stirs a spoon of salt in a glass of water and a spoon of sand in another glass. Describe what she sees and what she concludes in each case.", 4, "Salt disappears and the water remains clear (1). Salt is soluble (1). Sand settles at the bottom and can be seen (1). Sand is insoluble (1).", "H", wp=True),
W("A doctor advises a child with loose motions to drink ORS. The parent has sugar and salt at home. Explain how to prepare 2 litres and the quantity of each.", 3, "For 1 litre: 6 teaspoons sugar and half teaspoon salt (1). For 2 litres: 12 teaspoons sugar and 1 teaspoon salt (1) in boiled and cooled water (1).", "H", wp=True),
W("You are given a glass tumbler, a plastic mug and a steel tumbler. Mention one advantage and one disadvantage of each for use in school.", 4, "Glass: transparent but may break (1). Plastic: light but may not suit hot water (1). Steel: strong and lustrous but heavier (1). Choice depends on the purpose and safety (1).", "H", wp=True),
W("Design a table that classifies a notebook, steel scale, glass, rubber band and wooden ruler on the basis of transparency and lustre.", 4, "Notebook: opaque, non-lustrous (1). Steel scale: opaque, lustrous (1). Glass: transparent, shiny (1). Rubber band: opaque or translucent, non-lustrous; wooden ruler: opaque, non-lustrous (1).", "H", wp=True),
W("Why does Ayurveda classify materials in pairs of opposite properties? Name any three pairs.", 3, "Ayurveda describes matter using 20 properties (guna) in ten opposite pairs (1). Any two pairs shown: guru-laghu (heavy-light), sandra-drava (solid-liquid), mridu-kathina (soft-hard) (2).", "H"),
W("Two identical cups are filled, one with water and one with the same volume of sand. Which has more mass? Which has more volume? Explain.", 3, "Volume is the same, since equal amounts fill the cups (1). The cup with sand has more mass (1). Mass and volume are two different properties of matter (1).", "H", wp=True),
W("Explain why a tumbler of milk is matter but a shadow on the wall is not.", 3, "Matter has mass and occupies space (1). Milk has both (1). A shadow has no mass and occupies no space of its own, so it is not matter (1).", "H"),
W("A 1 m3 tank holds how many litres? How many 500 mL bottles can be filled from it?", 3, "1 m3 = 1000 L (1). 1000 L = 1000000 mL (1). Bottles = 1000000 / 500 = 2000 (1).", "H", wp=True),
W("A teacher shows a stone, a sponge and a rubber ball. Arrange them in order of hardness and give reasoning.", 3, "Stone (hardest), rubber ball, sponge (softest) (1). The stone cannot be pressed or scratched easily (1), the rubber compresses slightly and the sponge compresses most (1).", "H", wp=True),
W("Why are cooking utensils made of metals and not clay pots only? Mention two properties.", 3, "Metals are lustrous, hard and strong (1) and are not easily broken like clay pots (1). The choice depends on the purpose (1).", "H", wp=True),
W("Why is a transparent window useful in a school bus while an opaque wall is used in a bathroom? Explain with properties.", 3, "Transparent glass lets students see outside and lets light in (1). An opaque wall cannot be seen through, so it gives privacy (1). The material is chosen for the property that suits the purpose (1).", "H", wp=True),
W("Explain with an example how an object can be made from different materials and a material used for many objects.", 3, "A pen has plastic body, metal tip and ink (1). Plastic is used for pens, buckets and toys (1). So the relation is many-to-many (1).", "H"),
W("Anil says, \"Because a rubber ball is soft, it cannot be harder than anything.\" Correct him with an example.", 3, "Hardness is relative (1). A rubber ball is harder than a sponge or cotton (1) though it is softer than iron (1).", "H", wp=True),
W("Plan a simple test to find which of salt, sugar, sand and chalk powder are soluble in water. Write the steps and expected results.", 4, "Take four glasses with equal water (1). Add one spoon of each substance and stir (1). Salt and sugar disappear (1), sand and chalk powder stay as particles (1).", "H", wp=True),
]

CH = _base()
CH["blocks"] += [
 ("h2", "6.6 Worked Examples: Classifying and Choosing Materials"),
 ("steps", [("Example 1 — Classify using properties", "Take: aluminium foil, glass, wooden stick, butter paper. **Lustre:** aluminium foil is lustrous; the others are not. **Transparency:** glass is transparent, butter paper is translucent, aluminium foil and wood are opaque."),
  ("Example 2 — Choosing a material", "A tumbler must hold water, so it should be solid, not dissolve in water and be strong. Steel, glass and plastic are suitable; paper dissolves or becomes soft in water, so it is unsuitable for a long-lasting tumbler."),
  ("Example 3 — Soluble or insoluble?", "Stir a spoon of each in a glass of water: salt and sugar disappear (soluble); sand, chalk powder and sawdust remain (insoluble). Solubility is a property that decides the use: sugar sweetens a drink but sand does not."),
  ("Example 4 — Mass or volume?", "A cup full of sand and a cup of water have the same volume (same space). The sand has more mass, so it feels heavier. Mass (how heavy) and volume (how much space) are different properties.")]),
 ("note", "FORMULA", "Units: 1 kg = 1000 g;  1 L = 1000 mL;  1 m<sup>3</sup> = 1000 L.  Write units like 7 kg, 500 mL, 2 m<sup>3</sup> (no 's', no full stop, space after the number)."),
 ("h2", "6.7 Properties of Materials: Summary Table"),
 ("table", ["Property", "Types", "Test", "Examples"],
  [["Appearance", "Lustrous, non-lustrous", "Look at the surface or freshly cut part", "Copper, gold / paper, wood"],
   ["Hardness", "Hard, soft (relative)", "Press or scratch with a key", "Iron, stone / sponge, candle"],
   ["Transparency", "Transparent, translucent, opaque", "Look at an object through it", "Glass / butter paper / wood"],
   ["Solubility", "Soluble, insoluble", "Stir in water", "Sugar, salt / sand, chalk"],
   ["Mass", "Heavy, light", "Compare on a balance", "Water-filled cup vs empty cup"],
   ["Volume", "Space occupied", "Compare with units like mL, L", "Bottle with 1 L written"]]),
 ("h2", "6.8 Common Mistakes"),
 ("ul", ["Not all shiny objects are metals; some are polished or coated.",
  "Translucent is **not** the same as transparent: we see objects, but not clearly, through translucent materials.",
  "Air is matter; the fact that we cannot see it does not matter.",
  "Hardness is relative; do not call rubber 'hard' or 'soft' without comparing.",
  "Mass is not the same as volume: a small iron ball can have more mass than a large foam ball.",
  "Write units correctly: **kg, mL, m<sup>3</sup>**, not 'kgs' or 'ML'."]),
 ("h2", "6.9 Everyday Applications"),
 ("ul", ["Windows use transparent glass; bathroom windows use frosted (translucent) glass.",
  "Shopkeepers use transparent jars to display goods.",
  "ORS saves lives in dehydration; it uses the solubility of sugar and salt in water.",
  "Fish and water plants use oxygen dissolved in water.",
  "Different balls are made of different materials for different games.",
  "Pottery in India is thousands of years old and uses baked clay (terracotta)."]),
 ("h2", "6.10 Higher Order Questions"),
 ("qa", [("Why is clay suitable for pots?", "It can be shaped when wet and becomes hard when baked, and it holds water."),
  ("Why do some objects feel heavier than others of the same size?", "They are made of materials with more mass in the same volume."),
  ("Is sugar solution matter? Give reason.", "Yes, it has mass and occupies space."),
  ("Why is the word 'weight' used in daily talk for how heavy something is?", "Because mass is found by weighing, weight is sometimes used in common language for mass; the difference between mass and weight is learnt in higher classes.")]),
]
CH["takeaways"] += ["**Hardness is relative**, but mass and volume belong to **all** matter.", "ORS uses sugar and salt dissolved in boiled and cooled water."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
