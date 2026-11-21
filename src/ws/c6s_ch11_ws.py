"""Class 6 Science Ch 11 - Nature's Treasures: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch11"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch11", str(REPO / "src/rn_work/c6_sci/ch11.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The gas that is present in the largest amount in air is:", 1, "(b) nitrogen", "E", opts=["oxygen", "nitrogen", "carbon dioxide", "argon"]),
W("Oxygen forms about how much percent of air?", 1, "(c) 21 %", "E", opts=["1 %", "78 %", "21 %", "50 %"]),
W("Which of the following is a fossil fuel?", 1, "(d) coal", "E", opts=["wood", "wind", "sunlight", "coal"]),
W("The main source of energy on the Earth is the:", 1, "(a) Sun", "E", opts=["Sun", "Moon", "wind", "coal"]),
W("Which of these is a renewable resource?", 1, "(b) water", "E", opts=["petroleum", "water", "coal", "natural gas"]),
W("Stepwells in Rajasthan are called:", 1, "(c) bawadi", "E", opts=["vav", "johad", "bawadi", "tanka"]),
W("The movement in which women hugged trees to save them from being cut was the:", 1, "(a) Chipko movement", "E", opts=["Chipko movement", "Dandi march", "Quit India movement", "Van Mahotsav"]),
W("Fill in the blank: Moving air is called ______.", 1, "wind.", "E"),
W("Fill in the blank: The fuel CNG stands for Compressed ______ Gas.", 1, "Natural.", "E"),
W("Write True or False: Most of the water on the Earth is fresh and fit for drinking.", 1, "False. Most of it is salty water in oceans and seas. (1)", "E"),
W("Write True or False: Soil is formed over thousands of years by the breaking of rocks.", 1, "True. (1)", "E"),
W("Name two fossil fuels besides coal.", 2, "Petroleum and natural gas. (1+1)", "E"),
W("Name two uses of wind energy.", 2, "Any two: running windmills, grinding flour, lifting water from wells, generating electricity. (1+1)", "E"),
W("On which day is World Water Day celebrated?", 1, "22 March. (1)", "E"),
W("Give two products that we get from a forest.", 2, "Any two: wood, fruits, honey, medicinal herbs, gum, bamboo, lac. (1+1)", "E"),
W("What is rainwater harvesting?", 2, "Collecting and storing rainwater for later use. (2)", "E"),
W("Name two devices that use the Sun's energy.", 2, "Any two: solar cooker, solar water heater, solar panel (cell). (1+1)", "E"),
W("Which gas in the air do we need to live?", 1, "Oxygen. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Air has 78 % nitrogen, 21 % oxygen and the rest other gases. Find the percentage of the other gases. If a room contains 200 L of air, how many litres of oxygen are there?", 3, "100 – 78 – 21 = 1 % (1). Oxygen = 21 % of 200 (1) = 21 × 200 ÷ 100 = 42 L (1).", "M", wp=True),
W("Why can we live for some days without food or water but not for a few minutes without air?", 2, "Our body needs oxygen from air all the time for respiration; it cannot store oxygen, but it can survive for days with stored food and water. (2)", "M"),
W("What is a windmill farm? Name two places in India that have large wind farms.", 3, "A place with many windmills that generate electricity (1). Any two: Muppandal (Tamil Nadu), Jaisalmer Wind Park (Rajasthan), Brahmanvel (Maharashtra) (1+1).", "M"),
W("Why is the seawater not suitable for drinking, farming or industries?", 2, "It is saline (salty) (1), and salt is harmful to plants and damages machines in industries (1).", "M"),
W("Write three ways in which a family can save water at home.", 3, "Close taps when not in use, repair leaking taps, reuse water used for washing vegetables for plants, harvest rainwater (any three, 1 each).", "M", wp=True),
W("Why is the water in a pond or river polluted when a large amount of garbage is thrown into it?", 2, "Garbage, plastic and waste make the water dirty and unfit for use, and harm the living beings in it. (2)", "M", wp=True),
W("The Sun is said to give energy to the cow grazing in a field even though the cow does not stand in sunlight for long. Explain.", 3, "Plants use sunlight to make food (1). The cow eats grass (plants) (1) and so gets the Sun's energy through the grass (1).", "M", wp=True),
W("List two ways in which solar panels help a village.", 2, "They produce electricity for street lights, pumps and homes (1); they save fuels like kerosene and coal (1).", "M", wp=True),
W("Why are forests called homes of wild animals? Give two reasons.", 2, "They give food (fruits, leaves) and shelter (trees, bushes) to animals, birds and insects. (1+1)", "M"),
W("How do the roots of trees help the soil?", 2, "They hold the soil firmly and stop it from being washed away by water or blown away by wind. (2)", "M"),
W("Fallen leaves in a forest decay and become part of the soil. Which idea of nature does this show?", 2, "Recycling in nature (1), because the leaves add nutrients back to the soil, which the plants then use again (1).", "M"),
W("What is the role of earthworms in soil?", 2, "They turn and loosen the soil, making spaces for air and roots to move (2).", "M"),
W("Which fossil fuel is used to make petrol, diesel and kerosene? Give one use for each of the three.", 3, "Petroleum (1). Petrol for scooters and cars, diesel for buses and tractors, kerosene for lamps and stoves (any two matched uses, 1+1).", "M"),
W("Why is CNG called a cleaner fuel than petrol?", 2, "It burns with little smoke and gives less pollution than petrol or diesel. (2)", "M"),
W("Why must we save fossil fuels?", 2, "They formed over millions of years and are limited; they will run out if used at the present rate, and burning them gives smoke and carbon dioxide (2).", "M"),
W("Suggest two ways in which students can reduce the use of petrol and diesel.", 2, "Walk or cycle for short distances; use public transport or share vehicles (1+1).", "M", wp=True),
W("Classify as natural or human-made resources: air, bicycle, soil, bulb, forest, table.", 3, "Natural: air, soil, forest. Human-made: bicycle, bulb, table. (3)", "M"),
W("Find the mistake: \"Renewable resources are unlimited, so we can use as much water and as many trees as we want.\"", 2, "Renewable resources are renewed in a reasonable time but not without limit (1). Water and forests can be used up or polluted, so we must use them wisely (1).", "M"),
W("What are the uses of rocks in daily life? Give any three.", 3, "Making houses, temples, roads, dams, table tops; slate for roofs; stone tools in the past (any three, 1 each).", "M"),
# ---------------- HARD ----------------
W("A village has a pond whose water level falls every summer. List two causes and two remedies.", 4, "Causes: evaporation in the hot sun, and too much use or trees cut around it (1+1). Remedies: harvest rainwater and clean the catchment so more water collects (1), and plant trees and use water carefully (1).", "H", wp=True),
W("A school has a roof of 500 square metres. In one rain, 2 cm of rainwater falls on it. Find the volume of rainwater in cubic metres that can be harvested (1 cm = 0.01 m), and in litres (1 cubic metre = 1000 L).", 4, "2 cm = 0.02 m (1). Volume = area × depth = 500 × 0.02 (1) = 10 cubic metres (1) = 10 × 1000 = 10,000 L (1).", "H", wp=True),
W("Why were stepwells like Toorji ka Jhalra in Jodhpur built in Rajasthan, and how do they save water?", 3, "Rajasthan has little rainfall and a dry climate (1). Stepwells store rainwater and water seeping from lakes and rivers through stone-lined trenches (1) so that people can use it throughout the year (1).", "H", wp=True),
W("Salman says, \"I use a solar cooker, so I use no natural resource.\" Is he right? Explain.", 3, "He is partly right (1). Sunlight is a natural resource that is used and it is renewable (1). The cooker itself is a human-made resource made from natural resources like metals and glass (1).", "H", wp=True),
W("Why can soil be called a non-renewable resource even though it forms again?", 3, "Soil forms from rocks very slowly, over thousands of years (1). We can use or wash it away much faster than it forms (1), so it is not renewed in a reasonable time (1).", "H"),
W("A forest next to a village is being cut for firewood. Write three arguments to persuade the villagers to stop it.", 3, "The forest holds soil and prevents floods and soil loss (1). It gives homes to animals and products like honey, fruit and medicine (1). A forest takes many years to grow back once cut (1).", "H", wp=True),
W("Explain the Chipko movement and say what we learn from it.", 3, "In the 1970s in Uttarakhand, villagers, mostly women, hugged trees so that they could not be felled (1+1). We learn to protect trees and forests and to work together for nature (1).", "H"),
W("In a city, nine out of ten people travel to work by separate cars. Suggest two changes to reduce use of fossil fuels and how each helps the environment.", 4, "Use public transport and share cars (1), so fewer vehicles burn fuels (1). Use cycles or electric vehicles for short trips (1), which emit no smoke (1).", "H", wp=True),
W("A scooter uses 2 L of petrol for 80 km. How many litres will it need for a journey of 200 km? If the journey is made by bus with 40 passengers, explain how fuel use per person changes.", 3, "For 80 km: 2 L, so for 200 km: 2 × 200 ÷ 80 = 5 L (2). A bus carries many passengers, so the fuel used per person is much less than for a scooter or car (1).", "H", wp=True),
W("Why do we call the following a 'treasure' of nature: air, water, Sun? Give one use of each and say what would happen if it were missing.", 4, "Air (oxygen) is needed for breathing; without it living beings die in minutes (1). Water is needed for drinking and farming; without it life is not possible (1). The Sun gives heat and light, and plants cannot make food without it (1). All three are essential for life, hence treasures (1).", "H"),
W("The table of a family's daily water use shows: bathing 40 L, washing clothes 30 L, cooking 10 L, drinking 5 L, toilet 15 L. Find the total and the percentage for bathing. Suggest one place to save water.", 4, "Total = 40 + 30 + 10 + 5 + 15 = 100 L (1). Bathing = 40 ÷ 100 × 100 = 40 % (1). Any sensible saving, e.g. use a bucket instead of a shower, reuse clothes-washing water for floors (2).", "H", wp=True),
W("A wind farm has 40 windmills and each one gives electricity to run 25 homes. How many homes are served? If 5 windmills stop in a calm period, how many are served now?", 3, "40 × 25 = 1000 homes (1). 40 – 5 = 35 windmills (1); 35 × 25 = 875 homes (1).", "H", wp=True),
W("Compare renewable and non-renewable resources in a table with two points each and two examples each.", 3, "Renewable: replenished by nature in a reasonable time; use wisely; examples air, water, forests (1.5). Non-renewable: limited, take millions of years to form, not replaced quickly; examples coal, petroleum, minerals (1.5).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "11.10 Resources at a Glance"),
 ("table", ["Resource", "Main uses", "How to conserve", "Renewable?"],
  [["Air", "Breathing (oxygen), wind energy", "Avoid smoke and dust, plant trees", "Renewable"],
   ["Water", "Drinking, cooking, farming, industry", "Save, recycle, harvest rain, avoid pollution", "Renewable (use wisely)"],
   ["Sun", "Heat, light, solar panels, solar cooker", "Use solar devices to save fuel", "Renewable"],
   ["Forests", "Wood, food, medicine, home for animals", "Plant trees, avoid cutting, protect forests", "Renewable (slow)"],
   ["Soil", "Growing plants, bricks, home for organisms", "Protect from erosion, keep it fertile", "Non-renewable (forms very slowly)"],
   ["Rocks and minerals", "Buildings, metals, electronics", "Use carefully, recycle metals", "Non-renewable"],
   ["Fossil fuels", "Vehicles, cooking, electricity", "Use less, walk, cycle, share vehicles", "Non-renewable"]]),
 ("h2", "11.11 Worked Examples"),
 ("steps", [("Example 1 — Air percentages", "Air contains 78 % nitrogen and 21 % oxygen. All other gases: 100 – (78 + 21) = **1 %**. In 500 L of air, oxygen = 21 ÷ 100 × 500 = **105 L**."),
  ("Example 2 — Rainwater from a roof", "A roof of 100 m² receives 5 cm = 0.05 m of rain. Volume = 100 × 0.05 = **5 m³** = 5 × 1000 = **5000 L** of water that can be stored."),
  ("Example 3 — Natural or human-made?", "A wooden chair is human-made, but wood is a natural resource from forests. Human-made things are made from natural resources, so saving natural resources saves the things we make as well."),
  ("Example 4 — Why is a cow's energy from the Sun?", "Sun → grass makes food by using sunlight → cow eats grass → we drink the cow's milk. The first source of energy in the chain is the Sun."),
  ("Example 5 — Saving fuel", "A family uses 12 L of petrol a week. If they cycle for short trips and save 3 L a week, in 4 weeks they save 12 L. This also means less smoke and carbon dioxide in the air.")]),
 ("note", "IMPORTANT", "**Renewable does not mean unlimited.** Water and forests are renewed by nature but we can use them faster than nature renews them. Always use all resources wisely, as Gandhiji said: the Earth provides enough for everyone's need but not for everyone's greed."),
 ("h2", "11.12 Traditions and People Who Protect Nature"),
 ("ul", ["**Stepwells:** bawadis of Rajasthan and vavs of Gujarat collect rainwater and seepage water.",
  "**Chipko movement:** women in Uttarakhand embraced trees to stop felling.",
  "**Van Mahotsav:** in July, a week of tree planting.",
  "**Sacred groves:** patches of forest protected by communities because of belief.",
  "**Village custom:** collecting only fallen fruits (like nellikai) so that birds and animals can eat from the tree.",
  "**World Water Day (22 March):** reminds everyone to save water."]),
 ("h2", "11.13 Common Mistakes and Misconceptions"),
 ("table", ["Wrong idea", "Correct idea"],
  [["Air is only oxygen.", "Air is a mixture; nitrogen is the largest part (78 %) and oxygen is about 21 %."],
   ["Most of the Earth's water can be used.", "Most is salty ocean water; only a very small part is easily usable fresh water."],
   ["Renewable resources never finish.", "They can be used up or polluted if used carelessly."],
   ["The Sun gives energy only as heat.", "It gives both heat and light, and plants use light to make food."],
   ["Burning fossil fuels has no ill effects.", "It gives smoke and carbon dioxide, which pollute the air."],
   ["Soil forms quickly.", "Soil takes thousands of years to form from rocks."]]),
 ("note", "REMEMBER", "Numbers to remember: nitrogen 78 %, oxygen 21 %, other gases 1 %; World Water Day 22 March; fossil fuels take **millions of years** to form."),
 ("h2", "11.14 Higher Order Questions"),
 ("qa", [("Why should we not think that rain will always give enough water?", "Rain is uneven; some places get little. Water that is not stored or conserved is lost, so rainwater harvesting and careful use are needed."),
  ("How does recycling of water help?", "Used water that is cleaned can be used again for gardening or cleaning, so less fresh water is taken."),
  ("Why are electric vehicles considered better for the air?", "They do not burn fuel and so give out no smoke."),
  ("What is the link between soil, forests and water?", "Tree roots hold the soil, soil stores water, and forests help rain; destroying one affects the others.")]),
]
CH["takeaways"] += ["Air = 78 % nitrogen + 21 % oxygen + 1 % other gases; the **Sun** is the main source of energy.", "**Renewable** resources must still be used wisely; fossil fuels and minerals are **non-renewable**."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
