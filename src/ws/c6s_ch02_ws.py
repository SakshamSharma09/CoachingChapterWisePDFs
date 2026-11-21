"""Class 6 Science Ch 2 - Diversity in the Living World: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch02"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch02", str(REPO / "src/rn_work/c6_sci/ch02.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The variety of plants and animals found in a region is called its:", 1, "(b) biodiversity", "E", opts=["habitat", "biodiversity", "adaptation", "venation"]),
W("A tall plant with a hard, thick, woody stem and branches high above the ground is a:", 1, "(a) tree", "E", opts=["tree", "herb", "shrub", "creeper"]),
W("The pattern of veins in a leaf is called:", 1, "(c) venation", "E", opts=["adaptation", "habitat", "venation", "cotyledon"]),
W("Which plant has parallel venation?", 1, "(d) wheat", "E", opts=["hibiscus", "chickpea", "sadabahar", "wheat"]),
W("Which of these has a taproot?", 1, "(b) mustard", "E", opts=["grass", "mustard", "lemongrass", "wheat"]),
W("An animal that can live both in water and on land is an:", 1, "(c) amphibian", "E", opts=["insect", "aquatic bird", "amphibian", "reptile"]),
W("Fill in the blank: A chickpea seed splits into two parts, each called a ______.", 1, "cotyledon.", "E"),
W("Fill in the blank: The place where a plant or animal lives is called its ______.", 1, "habitat.", "E"),
W("Name the type of root system found in grass.", 1, "Fibrous roots. (1)", "E"),
W("Write True or False: A shrub has soft, green stems and is smaller than a herb.", 1, "False. A herb has a soft, green stem and is small; a shrub has hard, woody stems and branches near the ground. (1)", "E"),
W("Name two examples of terrestrial habitats.", 2, "Any two: forests, deserts, grasslands, mountains. (1+1)", "E"),
W("Name two examples of aquatic habitats.", 2, "Any two: ponds, lakes, rivers, oceans. (1+1)", "E"),
W("Why do we group plants and animals? Give one reason.", 1, "Grouping on common features makes it easier to study and understand them. (1)", "E"),
W("Which Indian scientist is known as the Birdman of India?", 1, "Salim Ali. (1)", "E"),
W("What kind of plant is a cactus adapted to? Name the feature that stores water.", 2, "Cactus is adapted to the hot desert (1). Its thick, fleshy stem stores water (1).", "E"),
W("Name the tree whose conical shape and sloping branches let snow slide off.", 1, "Deodar. (1)", "E"),
W("Give one example each of a herb, a shrub and a tree.", 2, "Herb: tomato; shrub: rose; tree: mango. (Other correct examples accepted; all three correct 2, two correct 1.)", "E"),
# ---------------- MEDIUM ----------------
W("Differentiate between a herb and a tree on any three points.", 3, "Herb: small, soft green stem, branches near the ground. Tree: very tall, hard thick woody stem, branches start high above the ground. (Any three comparisons, 1 each)", "M"),
W("Raju collected a leaf with parallel veins and a plant with a bunch of thin roots of equal size. Which group of plants (dicot or monocot) does it belong to? Give two reasons.", 3, "Monocot (1). Parallel venation (1) and fibrous roots (1) are features of monocots.", "M", wp=True),
W("Complete the table: Dicot seeds have ____ cotyledons, ____ venation and ____ roots; monocot seeds have ____ cotyledon, ____ venation and ____ roots.", 3, "Dicot: two, reticulate, taproot (1.5). Monocot: one, parallel, fibrous (1.5).", "M"),
W("Priya's class collected these: hibiscus, wheat, banana, chickpea. Sort them into reticulate and parallel venation.", 2, "Reticulate: hibiscus, chickpea. Parallel: wheat, banana. (2)", "M", wp=True),
W("Why do plants in a desert and plants on the Himalayan mountains look different?", 3, "Conditions differ: the desert has little water and high heat, mountains have snow and cold (1). Plants have different adaptations, e.g. fleshy stem in cactus, conical shape of deodar (1). So the biodiversity of each region is different (1).", "M"),
W("Define adaptation and give two examples.", 3, "Adaptations are special features that help plants and animals survive in a particular region (1). Examples: the fleshy stem of a cactus and the streamlined body of a fish (1+1).", "M"),
W("Write two differences between the camel of the hot desert in Rajasthan and the camel of the cold desert in Ladakh.", 2, "Hot-desert camel has one hump and long legs with wide hooves; the cold-desert camel has two humps and long hair and shorter legs. (Any two, 1 each)", "M"),
W("A fish is taken out of water and put on the ground. Why does it die? What does this show about habitat?", 2, "A fish is adapted to live in water, with fins and a streamlined body. A habitat gives the food, water, air and shelter that an organism needs. (2)", "M", wp=True),
W("Why is the frog called an amphibian? Is a fish an amphibian?", 2, "A frog can live both in water and on land (1). A fish lives only in water, so it is an aquatic animal and not an amphibian (1).", "M"),
W("Table: Animal - Ant, Goat, Pigeon, Fish. Write the body part used for movement by each.", 2, "Ant: legs; Goat: legs; Pigeon: legs and wings; Fish: fins. (4 x 0.5)", "M"),
W("Meena observes a lizard, a crow, and a butterfly. Which of these can both walk and fly? Suggest one basis of grouping all three.", 2, "The crow and the butterfly can walk and fly (1). They may be grouped by type of movement or habitat. (1)", "M", wp=True),
W("Why is it wrong to pluck flowers and leaves during a nature walk?", 2, "We should respect living things and observe them without disturbing them; plucking harms the plants and the animals that depend on them. (2)", "M", wp=True),
W("What is a sacred grove? How does it help biodiversity?", 3, "A sacred grove is an undisturbed patch of forest protected by the local community (1). No one harms animals or cuts trees (1), so many plants including medicinal ones and animals stay safe (1).", "M"),
W("Name two efforts made in India to protect animals, with years.", 2, "Project Tiger (1973) and the Cheetah Reintroduction Project (2022). (1+1)", "M"),
W("Savita says, \"A bunch of similar thin roots is a taproot.\" Find the mistake and correct it.", 2, "A taproot has one main root with side roots (1). A bunch of similar thin roots is a fibrous root system (1).", "M", wp=True),
W("How are trees helpful to birds and how are birds helpful to trees?", 3, "Trees give food and shelter to birds (1). Birds eat fruits and spread seeds (1). This shows that plants and animals depend on each other (1).", "M"),
W("Write True or False with a reason: Different groups of students can group the same plants in different ways and all can be right.", 2, "True. Groups can use different bases such as height, flower colour or stem type, and each basis is correct for its own purpose. (2)", "M"),
W("Rhododendron is shorter with smaller leaves in the Nilgiris but taller in Sikkim. What does this show?", 2, "Even the same kind of plant can differ with the region because conditions such as wind and temperature differ. (2)", "M"),
W("Name two Indian scientists in this chapter and one work of each.", 3, "Janaki Ammal: botanist who helped the Save Silent Valley movement (1.5). Salim Ali: bird expert who wrote books on birds and helped protect bird areas (1.5).", "M"),
# ---------------- HARD ----------------
W("Hari found a plant with soft thin stem, two cotyledons in the seed and net-like veins. Can it be a grass? Explain.", 3, "No. Grass is a monocot with one cotyledon, parallel venation and fibrous roots (1.5). The plant described is a dicot, probably a herb with reticulate venation (1.5).", "H", wp=True),
W("A student finds a plant with a hard, brown stem that has many branches starting close to the ground. Classify it and say how it differs from a tree.", 3, "It is a shrub (1). A tree is much taller (1), has a thick woody trunk and branches that start higher up (1).", "H", wp=True),
W("The hot-desert camel can go many days without water. List three features of it that help.", 3, "Wide hooves and long legs for sand (1); one hump for storing food (1); little urine, dry dung and no sweating so water is saved (1).", "H"),
W("Explain how the Save Silent Valley movement shows that common people can protect biodiversity.", 4, "A hydroelectric dam on the Kunthipuzha river threatened the moist evergreen forest in Palakkad, Kerala (1). Common people campaigned for 10 years (1) using awareness programmes, newspaper articles, seminars, petitions and court appeals (1). They saved the forest and its biodiversity (1).", "H"),
W("A farmer in Rajasthan wants to plant one species in a very dry field. Between cactus and a leafy herb that needs daily water, which would you advise and why?", 3, "Cactus (1). Its fleshy stem stores water (1), so it survives with very little water, while the herb would dry up (1).", "H", wp=True),
W("Your class sees many birds on a school tree. Suggest three ways to observe them without harming them.", 3, "Keep quiet and stand still (1). Do not throw stones or climb the tree (1). Use a notebook to record the type, colour, sound and food, from a distance (1).", "H", wp=True),
W("Why does loss of habitat lead to loss of biodiversity? Explain with an example.", 3, "Habitat gives food, water and shelter (1). If it is damaged, organisms lose these (1), e.g. a fish cannot live without water and a goat needs grass; they decrease or disappear (1).", "H"),
W("Elders in the village say they saw many birds as children but now see very few. Give two possible reasons and one action.", 3, "Reasons: trees were cut and the habitat was damaged (1), less food and shelter for birds (1). Action: plant trees and protect habitats (1).", "H", wp=True),
W("Compare dicots and monocots in a table using four features.", 4, "Cotyledons: two vs one (1). Venation: reticulate vs parallel (1). Roots: taproot vs fibrous (1). Examples: chickpea, hibiscus vs maize, wheat (1).", "H"),
W("Why are Project Tiger and the Cheetah Reintroduction Project needed?", 3, "Human activities have reduced the Bengal tiger and the cheetah (1). Project Tiger (1973) protects tigers (1), and the Cheetah project (2022) brings cheetahs back to India (1).", "H"),
W("Mustard and wheat plants are grown in a field. Give two differences in their root and leaf structure.", 3, "Mustard has a taproot and net-like veins in the leaf (1.5). Wheat has fibrous roots and parallel veins (1.5).", "H", wp=True),
W("Why can we say that the whole of biodiversity is like a web where each member has a role? Give two examples.", 3, "Each living thing depends on others (1). Trees give food and shelter to birds and insects (1) and animals spread seeds after eating fruits (1).", "H"),
W("Two groups grouped animals differently: one by food, one by movement. A student says one of them must be wrong. Do you agree? Justify.", 3, "No (1). Animals can be grouped in many ways such as food, habitat, colour and movement (1). Each basis shows different similarities and is correct for its own purpose (1).", "H"),
W("The Great Indian Bustard lives in parts of Gujarat, Rajasthan and Maharashtra. Why are its habitats being protected?", 3, "The number of Great Indian Bustards has gone down because of human activities (1). Protecting its habitats gives it food and shelter (1) and prevents the loss of this bird from our biodiversity (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "2.7 Worked Examples: Classifying Plants and Animals"),
 ("steps", [("Example 1 — Classify a plant from clues", "Clues: soft green stem, small height, leaves with net-like veins, a main root with side roots. **Soft stem and small** → herb. **Net-like veins** → reticulate venation. **Main root with side roots** → taproot. Reticulate + taproot → dicot plant, such as tomato or mustard."),
  ("Example 2 — Classify a plant from the seed", "A seed splits into two halves and each half is a cotyledon, so it is a dicot. We expect reticulate venation in its leaf and a taproot below the ground. Chickpea is an example."),
  ("Example 3 — Group animals by movement", "Ant (walks, crawls on legs), goat (walks, jumps on legs), pigeon (walks and flies using legs and wings), fish (swims using fins). Groups: only legs → ant, goat; legs and wings → pigeon; fins → fish.")]),
 ("note", "REMEMBER", "Rule of thumb: **reticulate venation + taproot + two cotyledons = dicot; parallel venation + fibrous roots + one cotyledon = monocot.** There are exceptions in the wider world, but this is the rule studied in Class 6."),
 ("h2", "2.8 Adaptation in Different Regions: Summary Table"),
 ("table", ["Organism", "Region", "Special feature (adaptation)", "How it helps"],
  [["Cactus", "Hot desert", "Thick, fleshy stem", "Stores water"],
   ["Deodar", "Cold mountains", "Conical shape, sloping flexible branches", "Snow slides off"],
   ["Fish", "Water", "Streamlined body, fins", "Easy swimming"],
   ["Camel (Rajasthan)", "Hot desert", "Long legs, wide hooves, one hump, little urine, no sweating", "Walks on sand, survives without water"],
   ["Camel (Ladakh)", "Cold desert", "Two humps, long hair, shorter legs", "Survives winter and walks on mountains"],
   ["Rhododendron", "Mountains", "Shorter, smaller leaves in strong winds (Nilgiris)", "Resists wind"]]),
 ("h2", "2.9 Common Mistakes"),
 ("ul", ["Do not mix up **herb** (soft stem) and **shrub** (many hard stems close to the ground).",
  "Do not call a bunch of thin roots a taproot; it is a **fibrous root system**.",
  "A habitat is **not** only a home; it provides food, water, air, shelter and other needs.",
  "Amphibians live in **both** water and on land; not all animals living near water are amphibians.",
  "Different ways of grouping are all correct if the basis is clear.",
  "When observing nature, **do not disturb or pluck**; observe and record."]),
 ("h2", "2.10 Environment Care: What Can a Class 6 Student Do?"),
 ("ul", ["Plant a tree or a few herbs in the school garden and look after them.",
  "Keep a small dish of water for birds in summer.",
  "Do not throw plastic and waste into ponds and rivers, where it harms aquatic animals.",
  "Learn about local sacred groves, birds and trees and share the knowledge.",
  "Respect the work of conservation efforts such as Project Tiger and the Silent Valley campaign."]),
 ("h2", "2.11 Higher Order Questions"),
 ("qa", [("Why is it said that biodiversity of one region differs from another?", "Conditions such as rainfall, temperature and soil differ from region to region, so different plants and animals have adapted to live there."),
  ("Why would a deodar not survive in a hot desert?", "Its conical shape and branches are suited to snow in cold mountains and it needs more water than a desert offers."),
  ("How can a tree change the biodiversity of a place?", "It gives food and shelter to birds and insects and attracts other animals, adding to the variety of life."),
  ("Is a frog terrestrial or aquatic?", "Neither only; it is an amphibian that lives in water as well as on land.")]),
]
CH["takeaways"] += ["Common people can protect biodiversity, as in the **Save Silent Valley** movement.", "Habitats give food, water, air and shelter; **loss of habitat means loss of biodiversity**."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
