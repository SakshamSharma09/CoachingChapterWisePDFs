"""Class 8 Science Ch 12 - How Nature Works in Harmony: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8s_ch12"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_sci" / f"ch{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

WS = [
# ---------------- EASY ----------------
 W("Which of the following is an abiotic component of a pond?", 1, "(c) sunlight. Fish, algae and frogs are living (biotic) components (1).", "E",
   opts=["fish", "algae", "sunlight", "frogs"]),
 W("Organisms that make their own food by photosynthesis are called:", 1, "(a) producers (autotrophs) (1).", "E",
   opts=["producers", "consumers", "decomposers", "parasites"]),
 W("Which of the following are decomposers?", 1, "(d) fungi and bacteria (1).", "E",
   opts=["grass and trees", "deer and hare", "tiger and leopard", "fungi and bacteria"]),
 W("In a relationship in which both organisms benefit, such as a honeybee and a flower, the interaction is called:", 1, "(b) mutualism (1).", "E",
   opts=["parasitism", "mutualism", "commensalism", "competition"]),
 W("A group of organisms of the same kind living in a habitat at a given time is a:", 1, "(a) population (1).", "E",
   opts=["population", "community", "ecosystem", "food web"]),
 W("Which of the following food chains is written correctly?", 1, "(c) Grass → Grasshopper → Frog → Snake. The arrow points from the food to the eater (1).", "E",
   opts=["Snake → Frog → Grasshopper → Grass", "Frog → Grass → Snake → Grasshopper", "Grass → Grasshopper → Frog → Snake", "Grasshopper → Grass → Frog → Snake"]),
 W("The world's largest mangrove forest is the:", 1, "(d) Sundarbans (1).", "E",
   opts=["Chilika forest", "Jim Corbett forest", "Eaglenest forest", "Sundarbans"]),
 W("Classify each organism as producer, herbivore, carnivore, omnivore or decomposer: tiger, mushroom, grass, crow, deer.", 2,
   "Tiger: carnivore; mushroom: decomposer; grass: producer; crow: omnivore; deer: herbivore (all 5 = 2; 3 or 4 correct = 1) (2).", "E"),
 W("Define a habitat and give two examples.", 2, "The place where an organism lives (1); e.g. a pond, a forest, a farm, tree bark (1).", "E"),
 W("Priya visits a pond near Udaipur. Name two biotic and two abiotic components she might see.", 2,
   "Biotic: any two of fish, frogs, algae, lotus, snails, ducks (1). Abiotic: any two of water, sunlight, air, soil, temperature (1).", "E", wp=True),
 W("During the rains, Rahul sees mushrooms growing on a rotting log in his garden. What kind of organisms are mushrooms and what do they do?", 2,
   "Fungi - decomposers (1). They break down dead matter into simple substances, returning nutrients to the soil (1).", "E", wp=True),
 W("True or false? Give a reason. 'In a food chain the arrow points from the eater to the organism that is eaten.'", 2,
   "False (1). The arrow points to the eater, from the food towards the organism that eats it (1).", "E"),
 W("Elephants have started entering farms in some Indian states. Give two reasons for this.", 2,
   "Habitat loss, as forests shrink because trees are cut for roads and buildings (1); less vegetation and drying waterholes due to changes in rainfall and temperature, so they look for crops like banana and sugarcane (1).", "E", wp=True),
 W("In a pyramid of numbers, which organisms are most numerous and which are fewest in a chain millet → grasshopper → frog → snake → eagle?", 1, "Most: millet (producers at the base); fewest: eagle (top) (1).", "E"),
 W("Why do Demoiselle cranes visit Khichan near Jodhpur in winter?", 2,
   "Migratory birds move to avoid harsh climate (1) and to find food at a more suitable place (1).", "E", wp=True),
 W("Give one example of parasitism.", 1, "A tick feeding on a dog's blood (the dog is harmed) (1).", "E"),
 W("Reena counts 20 neem plants in a 1 m × 1 m patch of the school garden. Is this a population or a community? Explain.", 2,
   "A population (1), because all are plants of the same kind in one habitat (1).", "E", wp=True),

# ---------------- MEDIUM ----------------
 W("A student says: 'Decomposers are useless, because dead plants and animals will disappear on their own.' Find the mistake and correct it.", 2,
   "Dead matter does not disappear by itself; fungi and bacteria break it down (1) and return nutrients to the soil for plants (recycling), so decomposers are essential (1).", "M"),
 W("In Pond A there were fish and many flowering plants with more seeds nearby; Pond B had no fish and fewer seeds. Explain this using dragonflies and pollination.", 3,
   "Fish eat dragonfly larvae, so Pond A had fewer dragonflies (1). Dragonflies eat flies, bees and butterflies, so with fewer dragonflies there were more pollinators (1), giving more pollination and more seeds near Pond A (1).", "M"),
 W("From the organisms - hawk, grasshopper, grass, snake, frog - make a food chain and name the trophic level of each.", 3,
   "Grass → grasshopper → frog → snake → hawk (1). Grass: producer, level 1 (0.5); grasshopper: herbivore, level 2 (0.5); frog: level 3 small carnivore (0.5); snake and hawk: higher carnivores (0.5).", "M"),
 W("In the 1980s India exported many frog legs. Explain how this affected farmers and what the government did.", 3,
   "Frog numbers fell (1). Frogs eat insect pests, so pests increased and farmers used more synthetic pesticides that harmed soil, water and health (1). The government banned the export of frog legs (1).", "M", wp=True),
 W("In a food web, grass is eaten by grasshoppers and mice; frogs eat grasshoppers; snakes eat frogs and mice; hawks eat snakes and mice. What will happen to the frogs and the mice if all snakes die?", 3,
   "Frogs: no snake to eat them, so they increase at first (1.5). Mice: less eaten by snakes (but hawks still eat them), so they increase and eat more grass (1.5).", "M", wp=True),
 W("Name the type of relationship in each case: (i) a bee and a flower (ii) an orchid growing on a tree (iii) a tick on a dog (iv) two plants fighting for sunlight.", 3,
   "(i) mutualism (ii) commensalism (iii) parasitism (iv) competition (all four = 3; three = 2) (3).", "M", wp=True),
 W("What is competition? How does it help keep the number of organisms of a species under control?", 2,
   "Organisms struggle for limited food, water, space or sunlight (1); because resources are limited, competition keeps any one species from multiplying too much (1).", "M"),
 W("Classify these interactions as biotic-abiotic, abiotic-abiotic or biotic-biotic: (i) earthworms living in moist soil (ii) sunlight evaporating pond water (iii) a frog eating insects.", 3,
   "(i) biotic-abiotic (ii) abiotic-abiotic (iii) biotic-biotic (1 each).", "M"),
 W("1000 grass plants, 100 grasshoppers, 10 frogs and 1 snake live in a meadow. Draw the pyramid of numbers in words and explain why the numbers fall as we go up the chain.", 3,
   "Wide base of 1000 grass plants, then 100, 10 and 1 at the top - a pyramid shape (1). Each level needs many organisms of the level below as food (1), so fewer organisms can be supported at each higher level (1).", "M", wp=True),
 W("Why is the Sundarbans important? State two benefits and two threats.", 3,
   "Benefits: slows winds and waves in storms and floods; absorbs CO<sub>2</sub> and gives oxygen; shelters wildlife; a UNESCO World Heritage Site (any two, 1.5). Threats: cutting mangroves for fuelwood and farming; illegal hunting; industrial waste and sewage (any two, 1.5).", "M", wp=True),
 W("How did mangroves protect Selvam's village in the 2004 tsunami?", 2,
   "The mangroves slowed down the winds and waves (1), reducing the force of the waves, so less damage reached the village (1).", "M", wp=True),
 W("What was the Green Revolution and what problems does its farming style bring now?", 3,
   "Between 1950 and 1965 India faced a food crisis, and tractors, machines, synthetic fertilisers and pesticides raised production (1). Problems: overuse of chemicals, excessive groundwater extraction (1) and monoculture, which are unsustainable (1).", "M"),
 W("A farmer in Sri Ganganagar uses large amounts of chemical fertiliser and pesticide every year, and now finds fewer earthworms and more pests. Explain.", 3,
   "Excess fertiliser kills useful soil microorganisms and reduces humus (1). Pesticides kill natural predators of pests such as beetles (1), so the pests increase and may become resistant to pesticides (1).", "M", wp=True),
 W("What is monoculture? Give two ways in which it harms an ecosystem.", 2,
   "Growing the same crop repeatedly (1). It reduces biodiversity and the number of pollinators, and degrades the soil (any two, 1).", "M"),
 W("What is Kunapa Jala? What does it show about traditional farming knowledge?", 2,
   "A fermented liquid fertiliser made from animal and plant waste, mentioned in the Vrikshayurveda (1). It shows that ancient farming nourished the soil with organic manure instead of chemicals (1).", "M"),
 W("What are elephant corridors? Why are they needed?", 2,
   "Strips of land connecting forest habitats (1). They let elephants move safely between forests without entering villages and fields, reducing human-animal conflict (1).", "M", wp=True),
 W("What is pollination? Name two agents of pollination.", 2,
   "Transfer of pollen (from the stamen, the male part) to the female part of the flower (1). Agents: wind, water, insects, bats and birds (any two, 1).", "M"),
 W("A nocturnal snake and a day-active rodent live in the same forest. How do they manage to coexist?", 2,
   "They are active at different times of the day (1) and so use the same resources such as space and food under different conditions without much competition (1).", "M"),
 W("Name three types of protected areas and give one example of an area in India.", 2,
   "Any three of: national parks, wildlife sanctuaries, biosphere reserves, community conserved areas (1); e.g. Jim Corbett, Manas, Nilgiri Biosphere Reserve, Chilika Lake (1).", "M"),
 W("What did the wildlife biologist A. J. T. Johnsingh show about tigers and leopards in Bandipur?", 2,
   "That predators like tigers and leopards depend on a healthy prey population (1) such as deer and wild boar; if the prey decline, the predators suffer (1).", "M"),

# ---------------- HARD ----------------
 W("<b>Case study.</b> A village pond near Bikaner is polluted with detergent and plastic waste. Within weeks the water plants die, fish float dead, insects multiply and spread to the nearby fields, and farmers start spraying more pesticide. (i) Why do the fish die? (ii) Why do insects increase? (iii) What is the effect of the extra pesticide? (iv) Name the idea that this chain of events illustrates and suggest one remedy.", 5,
   "(i) Pollution kills plants, so less oxygen in the water, and fish die (1). (ii) Fish (consumers of insects/larvae) die, so insects increase (1). (iii) Pesticides harm soil, water, helpful predators and health (1). (iv) One change leads to another - a chain of effects showing the balance of the ecosystem is disturbed (1); remedy: stop dumping waste, clean the pond, restore plants, use less pesticide (1).", "H", wp=True),
 W("In a field survey the counts are: grass 5000, grasshoppers 500, frogs 50, snakes 5, eagles 1. (i) Write the food chain. (ii) Name the producer and the top carnivore. (iii) State what the pattern of numbers shows. (iv) If frogs are removed, what changes would you expect in grasshoppers and snakes?", 4,
   "(i) Grass → grasshopper → frog → snake → eagle (1). (ii) Producer: grass; top carnivore: eagle (1). (iii) Numbers decrease at each higher level, giving a pyramid (1). (iv) Grasshoppers increase (no frogs to eat them); snakes decrease (less food) (1).", "H", wp=True),
 W("Hawks eat snakes, mice and small birds; snakes eat frogs and mice; mice eat grain; frogs eat grasshoppers; grasshoppers eat grass. Draw the food web in words and predict the effect on mice and hawks if farmers poison all the snakes.", 4,
   "Grass → grasshopper → frog → snake → hawk; grain → mouse → snake → hawk; mouse → hawk; small birds → hawk (2). Without snakes mice increase (and eat more grain) (1), hawks then rely on mice and birds and may go down if the food is not enough, so poisoning the snakes disturbs the whole web (1).", "H", wp=True),
 W("Can the Earth thrive without humans? Can humans survive without the Earth's ecosystems? Give two points for each answer.", 3,
   "The Earth (nature) has thrived without humans: ecosystems with producers, consumers and decomposers recycle nutrients without our help (1). Humans, on the other hand, depend on ecosystems for air, water, food, fibre, timber and medicines, so humans cannot survive without them (2).", "H"),
 W("Assertion (A): When the Indian bullfrog was exported in large numbers, the use of pesticides in farms increased. Reason (R): Frogs feed on insects that are agricultural pests. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). With fewer frogs, more insect pests survived (1), so farmers used more synthetic pesticides to control them (1).", "H"),
 W("Assertion (A): Decomposers are needed for nutrient recycling. Reason (R): Decomposers make food by photosynthesis. Is A true? Is R true? Explain.", 3,
   "A is true: decomposers break down dead matter and return nutrients to the soil (1). R is false (1): decomposers (saprotrophs) feed on dead and rotting matter and do not make food by photosynthesis - producers do (1).", "H"),
 W("Your class wants to estimate how many plants of one kind grow in the school garden. Describe a simple method with steps, and say what a pooled result tells.", 4,
   "Mark out a 1 m × 1 m area (a quadrat) in the garden (1). Identify the organisms in it and count the plants of one kind - this is the population in the patch (1). Different groups do this at different spots (1). Pooling the group data gives an idea of how many organisms of each kind live in the garden (1).", "H", wp=True),
 W("A village pond is overfished and almost no fish remain. Using Pond A and Pond B, predict what happens to dragonflies, pollinators and the seeds of the flowering plants around the pond.", 4,
   "Fish eat dragonfly larvae; without fish, dragonflies increase (1.5). Dragonflies eat flies, bees and butterflies, so pollinators decrease (1.5). Fewer pollinators means less pollination and fewer seeds (1).", "H", wp=True),
 W("Compare a natural ecosystem (a forest) with a human-made ecosystem (a farm) in terms of who maintains it, variety of organisms and effect on the environment.", 3,
   "Forest: maintained by nature itself, has many kinds of organisms, regulates climate, gives air, soil and water (1.5). Farm: needs human care and management, usually has one or few crop types and fewer kinds of organisms, may cause pollution through chemicals if poorly designed (1.5).", "H"),
 W("Pesticides kill pests at first, but after some years the pests are back in larger numbers. Give three reasons.", 3,
   "Pesticides also kill natural predators of pests, such as beetles (1). Pests that survive become resistant to the pesticide and multiply (1). Heavy use damages soil and microorganisms, upsetting the natural balance that controls pests (1).", "H", wp=True),
 W("A farmer in Jaipur wants to shift to organic and natural farming. Suggest four practices and explain how each helps the ecosystem.", 4,
   "Use organic manure (e.g. Kunapa Jala) to nourish the soil (1). Grow different crops (crop variety) to avoid monoculture and support pollinators (1). Recycle farm waste to return nutrients (1). Use few or no chemical pesticides and fertilisers, protecting soil microorganisms, earthworms and natural predators (1).", "H", wp=True),
 W("Elephants raid crops in many parts of eastern India. Explain the chain of causes, and suggest two ways of reducing the conflict.", 4,
   "Trees are felled for roads and buildings and the climate/rainfall changes, so forests shrink and waterholes dry (1.5); elephants lose their habitat and food and enter farms for bananas and sugarcane (1). Solutions: elephant corridors, protecting and restoring forests, providing water and food in forests (any two, 1.5).", "H", wp=True),
 W("Migratory birds such as the Demoiselle cranes help nature and farmers. Give three ways in which they do so.", 3,
   "They act as pollinators and seed dispersers (1). They link different habitats (1). They eat insect pests, helping farmers (1).", "H", wp=True),
]

_base = _old(12)
_i = max(i for i, b in enumerate(_base["blocks"]) if b[0] == "h2")
_extra = [
 ("h2", "Worked Examples and Reasoning Skills"),
 ("steps", [
   ("Example 1 — Build a food chain and label trophic levels", "From the organisms *hawk, grasshopper, grass, snake, frog*: Grass → Grasshopper → Frog → Snake → Hawk. Grass = **producer** (level 1); grasshopper = **herbivore** (level 2, primary consumer); frog = **small carnivore** (level 3); snake and hawk = **larger carnivores** (higher levels). The arrow always points **to the eater**."),
   ("Example 2 — Pyramid of numbers", "Counts: grass 5000, grasshoppers 500, frogs 50, snakes 5, eagle 1. Numbers fall at each step, because each level needs many organisms of the level below as food. This gives the **pyramid** shape (wide base, narrow top)."),
   ("Example 3 — Cascade after removing an organism", "If **frogs** vanish: grasshoppers (their food) **increase**, so grass is eaten more; snakes (that ate frogs) **decrease** or turn to other prey. If **snakes** vanish: frogs and mice increase, hawks lose one food source. Always trace *who eats it* and *whom it eats*."),
   ("Example 4 — Direct and indirect effects (Pond A / Pond B)", "Fish eat dragonfly larvae → fewer dragonflies → fewer pollinators eaten (dragonflies eat bees and butterflies) → more pollination → more seeds. The effect of fish on seeds is **indirect**; the effect of fish on dragonfly larvae is **direct**."),
   ("Example 5 — Identify the relationship", "Honeybee and flower: **mutualism** (both gain). Orchid on a tree branch: **commensalism** (orchid gains, tree unaffected). Tick on a dog: **parasitism** (tick gains, dog harmed). Two plants for the same sunlight: **competition**."),
 ]),
 ("h2", "Summary Tables"),
 ("table", ["Level of organisation", "What it includes", "Example"], [
   ["Organism", "A single living thing", "One fish"],
   ["Population", "Same kind of organisms in a habitat", "All the fish of one kind in a pond"],
   ["Community", "All populations in a habitat", "Fish, frogs, algae, insects"],
   ["Ecosystem", "Community + abiotic components interacting", "A pond, a forest, a farm"]]),
 ("table", ["Pesticide chain", "Effect"], [
   ["Frogs are exported", "Fewer frogs → more insect pests"],
   ["More pests", "Farmers use more synthetic pesticides"],
   ["Pesticides", "Harm soil, water, helpful predators, health; pests become resistant"],
   ["Government action", "Ban on frog-leg export; shift to organic and natural farming"]]),
 ("note", "REMEMBER", "**Common mistakes:** (1) Putting the arrow in a food chain from the eater to the food — it goes **towards the eater**. (2) Calling decomposers producers — they do not make food. (3) Mixing population with community. (4) Saying commensalism harms the second organism — it is **unaffected**. (5) Thinking a small change affects only one organism — changes **cascade** through the web. (6) Writing that humans are outside the ecosystem — we depend on it."),
 ("h2", "Real-Life Connections"),
 ("ul", ["**Rajasthan:** Demoiselle cranes at Khichan (Jodhpur) in winter; farm ecosystems in Sri Ganganagar and Jaipur districts where overuse of chemicals and groundwater is a concern.",
         "**Kitchen gardens and farms:** earthworms, snails, beetles and bees are part of a healthy farm; organic manure (like Kunapa Jala), crop variety and recycling farm waste help.",
         "**Coasts:** mangroves such as the Sundarbans slow storms and tsunamis; cutting them for fuelwood and farming removes this protection.",
         "**Wildlife:** elephant corridors and protected areas (Jim Corbett, Manas, Nilgiri, Chilika, Hemis) reduce conflict and conserve biodiversity.",
         "**Daily life:** buying fish, using pesticides or throwing waste in ponds affects other organisms through food webs."]),
]
_qa2 = [
  ("What happens to a pond's fish if plants die due to pollution?", "Oxygen falls, fish die, insects increase and may reach farms, leading to more pesticide use."),
  ("How are trophic levels related to the pyramid of numbers?", "Numbers decrease at each higher trophic level, giving a pyramid with producers at the base."),
  ("Why should we avoid monoculture and excess chemicals in farms?", "They reduce biodiversity, pollinators and soil microorganisms and make pests resistant."),
]
_blocks = list(_base["blocks"])
_blocks[_i + 1] = ("qa", list(_blocks[_i + 1][1]) + _qa2)
CH = dict(_base, blocks=_blocks[:_i] + _extra + _blocks[_i:],
          takeaways=_base["takeaways"] + ["In a food chain the **arrow points to the eater**; numbers (and energy available) fall at each higher trophic level, giving a pyramid.",
                                          "Removing one organism **cascades**: prey increase and predators decrease, as in the frog-leg export story."])

if __name__ == "__main__":
    run(__file__, BANK, 8, "Science", WS, CH)
