"""Class 6 Science Ch 10 - Living Creatures: Exploring their Characteristics: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch10"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch10", str(REPO / "src/rn_work/c6_sci/ch10.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Anything that makes a living being respond is called a:", 1, "(b) stimulus", "E", opts=["response", "stimulus", "reaction time", "habit"]),
W("Which plant folds its leaves when touched?", 1, "(c) touch-me-not (mimosa)", "E", opts=["rose", "grass", "touch-me-not (mimosa)", "banyan"]),
W("Plants take in air through tiny pores on leaves called:", 1, "(a) stomata", "E", opts=["stomata", "roots", "petals", "spawn"]),
W("The correct order of the life cycle of a mosquito is:", 1, "(d) egg, larva, pupa, adult", "E", opts=["egg, pupa, larva, adult", "larva, egg, pupa, adult", "egg, adult, larva, pupa", "egg, larva, pupa, adult"]),
W("A group of frog eggs in water is called:", 1, "(b) spawn", "E", opts=["larva", "spawn", "pupa", "seedling"]),
W("Seeds that are kept in water-logged soil do not germinate because they do not get enough:", 1, "(c) air", "E", opts=["light", "heat", "air", "soil"]),
W("The scientist who built the crescograph is:", 1, "(a) Jagadish Chandra Bose", "E", opts=["Jagadish Chandra Bose", "Anna Mani", "C. V. Raman", "Aryabhata"]),
W("Fill in the blank: When a seed sprouts, we say it has ______.", 1, "germinated.", "E"),
W("Fill in the blank: The removal of waste products from the body is called ______.", 1, "excretion.", "E"),
W("Write True or False: Movement alone is enough to say that something is living.", 1, "False. A car moves but is non-living. We need to look at many characteristics. (1)", "E"),
W("Write True or False: Plants do not move at all.", 1, "False. Plants show movements, such as opening of flowers and shoots bending towards light, without changing place. (1)", "E"),
W("Name any four characteristics of living beings.", 2, "Any four: movement, growth, nutrition, respiration, excretion, response to stimuli, reproduction, death. (½ each)", "E"),
W("What does the root of a seedling do: grow upward or downward?", 1, "Downward. (1)", "E"),
W("In which direction does the shoot grow when light comes from one side?", 1, "Towards the light. (1)", "E"),
W("Name the four stages in the life cycle of a silk moth.", 2, "Egg, larva, pupa and adult. (½ each)", "E"),
W("Why are mosquito eggs laid on stagnant water a worry for us?", 2, "Female mosquitoes breed there and spread diseases like malaria and dengue. (2)", "E", wp=True),
W("Name two ways in which plants respond to a stimulus.", 2, "Touch-me-not folds leaves on touch; shoots grow towards light; amla leaves fold after sunset. (any two, 1+1)", "E"),
W("What helps a tadpole to swim?", 1, "Its tail. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Explain why a stone does not have the characteristics of a living being, using three points.", 3, "A stone does not grow or need food (1), does not breathe or excrete (1), and does not respond to stimuli or have young ones (1).", "M"),
W("Anu says that a seed in the packet is non-living because it does not move or eat. Is she correct? Explain.", 2, "No (1). A seed is living; when it gets water and air it germinates and grows into a plant (1).", "M", wp=True),
W("Pooja's grandmother says her breathing rate is faster after climbing stairs. Which life process is this and why does it become faster?", 2, "It is respiration (1). The body needs more energy after exercise, so we breathe faster (1).", "M", wp=True),
W("Explain why the grass blades and rose leaves have tiny drops of water in the morning. Name the life process (do not confuse with dew).", 2, "Plants give out extra water and minerals as droplets (excretion) (2).", "M"),
W("In the seed germination activity, why did the seeds in pot B (always covered with water) not germinate even though water is needed?", 2, "Too much water filled all the space in the soil (1) and the seeds could not get air, which is also needed (1).", "M"),
W("Which pots gave sprouts: A (no water, sunlight), B (excess water, sunlight), C (moist, dark), D (moist, sunlight)? What can be concluded about light?", 3, "C and D (1+1). Seeds germinate in the dark too, so most seeds do not need light to germinate (1).", "M"),
W("Why do farmers store grains and pulses in a dry place?", 2, "Moisture and air together could make the seeds sprout or spoil (1). Dry storage keeps them from germinating (1).", "M", wp=True),
W("Name two seeds that need light to germinate and two that need darkness.", 2, "Need light: coleus, petunia (1). Need darkness: calendula, zinnia (1).", "M"),
W("Describe in four steps what a gardener should do to sow a bean seed so that it germinates.", 3, "Choose good soil and loosen it (1); place the seed in the soil and cover it lightly (1); water it moderately so that the soil is moist but not flooded (1); keep it in a place where it gets air.", "M", wp=True),
W("In a seedling experiment, the pot is turned upside down. What happens to the root and shoot after some days?", 2, "The root bends and grows downward (1) and the shoot bends and grows upward (1).", "M"),
W("Name the stages in the life cycle of a bean plant in order.", 2, "Seed, germination (root and shoot), leaves, flowers, fruits (pods) with seeds. (2)", "M"),
W("Why does a tadpole not look like an adult frog? Name two changes seen during its growth.", 2, "A tadpole has a tail and lives in water (1). Hind legs develop and the tail shrinks and disappears as it becomes a frog (1).", "M"),
W("Explain with a reason why kerosene is sprayed on water collected in a pit.", 2, "A thin layer of kerosene stops air from reaching the larvae and pupae, which breathe at the surface, so they die (2).", "M", wp=True),
W("Write two precautions that you can take at home to prevent mosquito breeding.", 2, "Do not allow water to stand in desert coolers, pots, tyres or open containers; empty and dry them weekly; cover water tanks. (1+1)", "M", wp=True),
W("Find the mistake: \"Sana thinks that a mosquito's life cycle is egg, pupa, larva, adult because the pupa looks small.\"", 2, "Larva comes before pupa (1). Larvae turn into pupae and pupae into adults (1).", "M", wp=True),
W("Why does the touch-me-not plant fold its leaves when touched? Give the stimulus and the response.", 2, "Stimulus: touch (1). Response: the leaves fold (1).", "M"),
W("Write two similarities between the life cycle of a plant and that of an animal.", 2, "Both start as a seed or egg and grow (1); both reproduce to give new ones of their kind and finally die (1).", "M"),
W("How does the stalk of a climber show movement? Give the use of this movement to the plant.", 2, "The stem winds around a support (1) to climb up and get sunlight (1).", "M"),
W("Why should we not water a pot so much that it is full of water above the soil level?", 2, "The seeds or roots will not get air to breathe, so the seeds will not sprout and the roots can rot (2).", "M", wp=True),
# ---------------- HARD ----------------
W("Meena puts four moist bean seeds in different pots: P in the dark, Q in sunlight, R in a refrigerator and S in a freezing cold box. P and Q germinated; R slowly; S did not. What can you say about conditions necessary for germination?", 3, "Water and air alone are not enough; the right temperature is also needed (1). P and Q show light is not necessary (1). Very cold temperature in S stopped the process (1).", "H", wp=True),
W("Rohan put a bean seedling in a box with a hole on one side. After a week the shoot is bent towards the hole. Name the stimulus and the response and say what the root would do.", 3, "Stimulus: light from one side (1). Response: the shoot grows towards the light (1). The root keeps growing downward (1).", "H", wp=True),
W("Design an experiment to show that seeds need air to germinate. Mention what you would keep the same.", 4, "Take two identical pots with the same soil, same number of seeds, same amount of water (1). Keep one pot with soil only moist and the other flooded with water above the soil (1). Place both at the same place and temperature (1). The moist pot germinates, the flooded one does not, showing the need for air (1).", "H", wp=True),
W("List the characteristics of living beings in a table and give one animal and one plant example for any two of them.", 4, "Table of movement, growth, nutrition, respiration, excretion, response, reproduction, death (2). Examples: movement - dog moves, flowers open; response - cow moves away from a thorn, touch-me-not folds leaves (1+1).", "H"),
W("A frog takes about 14 weeks to grow from an egg to an adult. The tadpole with legs is seen at 8 to 10 weeks and the froglet at 12 weeks. (i) How many weeks after the froglet stage does the adult appear? (ii) How does the froglet differ from the adult frog?", 4, "(i) 14 – 12 = 2 weeks (2). (ii) The froglet still has a shrinking tail and is small, the adult has no tail and strong legs for jumping (2).", "H", wp=True),
W("A drain behind a house has stagnant water and many mosquitoes. A student says, \"Spray a mosquito repellent on the adults.\" Give a better, longer-lasting plan based on the life cycle.", 3, "Stop the breeding by removing the stagnant water or covering it (1). Spray kerosene or clean the drain so that larvae and pupae cannot breathe or grow (1). This breaks the life cycle, so adults are not produced (1).", "H", wp=True),
W("Which characteristics of life does a growing banana plant show? Give one example of each from the plant.", 4, "Growth: gets taller and bigger (1). Nutrition: makes food with sunlight, water and minerals (1). Respiration: exchanges air through stomata (1). Reproduction: gives suckers and seeds or fruits (1).", "H"),
W("Compare a seed and a pebble. Which living characteristics does the seed show under right conditions and which does the pebble never show?", 3, "A seed germinates, grows into a plant, needs water and air and can produce new seeds (2). A pebble shows none of these (1).", "H"),
W("Why is it wrong to say, \"A mosquito's larva and adult live in the same place and look alike\"? Give two differences between them.", 3, "They look very different and live in different places (1). The larva lives in water and has a worm-like body (1). The adult has wings and flies in the air (1).", "H"),
W("Describe how J. C. Bose's crescograph helped in showing that plants respond to stimuli. Why is this important?", 3, "The crescograph recorded growth and movement of plants (1) when light, heat, electricity and gravity acted on them (1). It showed that plants can sense and respond to stimuli, so they are living (1).", "H"),
W("Neelam touches a mimosa plant and its leaves fold. A friend says, \"It is just a machine, not alive.\" Using the characteristics of life, give two reasons to show the plant is living.", 3, "The plant responds to the stimulus of touch (1). It also grows, makes food, respires through stomata and reproduces through seeds (1+1), which a machine does not do.", "H", wp=True),
W("Based on the activity with the bean seedlings in beakers A, B and C, write the observation, inference and one real-life use of the knowledge.", 4, "Observation: roots grow down, shoots grow up and shoots turn towards light (2). Inference: roots respond to gravity, and shoots respond to gravity and light (1). Use: plants on balconies and indoor pots are turned towards light, or a leaning plant grows up again (1).", "H", wp=True),
W("Why can we say that reproduction is necessary for the continuity of life even though a single plant or animal can live without reproducing?", 3, "Every living being dies after some time (1). Reproduction produces new ones of the same kind (1), so the kind or species continues even when the old ones die (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "10.7 Living or Non-living: Test Table"),
 ("table", ["Thing", "Moves", "Grows", "Needs food", "Breathes", "Reproduces", "Living?"],
  [["Dog", "Yes", "Yes", "Yes", "Yes", "Yes", "Living"],
   ["Mango tree", "Slight movement (leaves, shoots)", "Yes", "Yes (makes it)", "Yes (stomata)", "Yes (seeds)", "Living"],
   ["Car", "Yes", "No", "Needs fuel, not food", "No", "No", "Non-living"],
   ["Stone", "No", "No", "No", "No", "No", "Non-living"],
   ["Seed (dry)", "No (not yet)", "Germinates with water and air", "Uses stored food", "Yes", "Grows into a plant that reproduces", "Living"]]),
 ("note", "IMPORTANT", "A single characteristic cannot decide whether something is living. A car moves and uses fuel but does not grow, breathe or reproduce. Look at **all** the characteristics together."),
 ("h2", "10.8 Worked Examples and Activity Results"),
 ("steps", [("Example 1 — Why a dry seed is living", "A dry bean seed looks lifeless, but when it is kept in moist soil with air it sprouts, grows roots and shoots and later forms flowers and new seeds. It therefore has the characteristics of a living thing."),
  ("Example 2 — Seed germination pots", "Pot A: no water → no germination. Pot B: too much water, no air → no germination. Pot C: moist soil in dark → germination. Pot D: moist soil in sunlight → germination. **Conclusion:** the right amounts of water and air are needed; light is not needed for beans."),
  ("Example 3 — Where does the shoot go?", "In beaker B the seedling is upside down. After some days the root bends downward and the shoot bends upward. The plant parts respond to gravity (and to light) and grow in their natural directions."),
  ("Example 4 — Breaking the mosquito life cycle", "Larvae and pupae must reach the water surface to breathe. A thin layer of kerosene stops air from entering, so they die and no adult mosquito comes out. Better still, do not let water stand in coolers, pots or tyres."),
  ("Example 5 — Count of days", "A frog's egg takes about 14 weeks to become an adult. If tadpoles get legs at 8 to 10 weeks and the froglet appears at 12 weeks, the adult appears 14 – 12 = **2 weeks** after the froglet stage.")]),
 ("h2", "10.9 Differences at a Glance"),
 ("table", ["Mosquito", "Frog"],
  [["Egg, larva, pupa, adult", "Egg (spawn), tadpole, froglet, adult"],
   ["Eggs laid on stagnant water", "Eggs laid in water as a jelly-like spawn"],
   ["Larva and pupa live in water but come to the surface to breathe", "Tadpole lives in water and swims using its tail"],
   ["Adult flies in air; female sucks blood and spreads diseases", "Adult lives on land and water, with strong legs for jumping"],
   ["Adult lives about 10–15 days", "Takes about 14 weeks to become an adult"]]),
 ("h2", "10.10 Common Mistakes and Misconceptions"),
 ("table", ["Wrong idea", "Correct idea"],
  [["Anything that moves is alive.", "A car and a river move but are non-living; judge by many characteristics."],
   ["Plants do not respond to anything.", "Plants respond to touch, light, gravity and so on, though slowly."],
   ["More water is always better for seeds.", "Too much water cuts off air, and the seeds do not germinate."],
   ["All seeds need sunlight to germinate.", "Most seeds do not need light; some need light, some need dark."],
   ["The pupa comes before the larva.", "The larva comes before the pupa in mosquito and silk moth."],
   ["A seed is a non-living object.", "A seed is living; it germinates under suitable conditions."]]),
 ("note", "REMEMBER", "**Germination** needs the right amount of **water and air**. **Later growth** of the seedling needs **sunlight** for making food."),
 ("h2", "10.11 Higher Order Questions"),
 ("qa", [("Can there be living beings that do not move from place to place?", "Yes, plants stay fixed in one place but show other movements such as opening of flowers and bending of shoots."),
  ("Why is it said that a dead seed cannot germinate even in good conditions?", "A dead living being cannot show life characteristics even if food, air and water are available."),
  ("What is the use of the tail of a tadpole and what happens to it?", "It helps in swimming; as the tadpole becomes a frog the tail shrinks and disappears."),
  ("What is common in the life cycles of a bean plant and a frog?", "Both start small, grow, change form, reproduce and finally die, which maintains the continuity of life.")]),
]
CH["takeaways"] += ["A **seed is living**; it germinates when it gets the right amount of water and air.", "In the mosquito and the silk moth the **larva comes before the pupa**; kerosene on stagnant water stops larvae and pupae from breathing."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
