"""Class 8 Science Ch 13 - Our Home: Earth, a Unique Life-sustaining Planet: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8s_ch13"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_sci" / f"ch{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric checks
assert 450 - 170 == 280 and 450 - 15 == 435 and 15 - (-200) == 215

WS = [
# ---------------- EASY ----------------
 W("The hottest planet in the solar system is:", 1, "(c) Venus, because of its thick carbon dioxide atmosphere (1).", "E",
   opts=["Mercury", "Mars", "Venus", "Earth"]),
 W("The habitable zone of a star is the range of distances at which:", 1, "(a) water can stay in the liquid state (1).", "E",
   opts=["water can stay liquid", "planets are rocky", "the temperature is exactly 0 °C", "gravity is zero"]),
 W("The ozone layer protects living things by blocking:", 1, "(b) harmful ultraviolet (UV) rays from the Sun (1).", "E",
   opts=["visible light", "ultraviolet rays", "sound waves", "oxygen"]),
 W("Which of the following is an example of asexual reproduction?", 1, "(d) budding in Hydra (1).", "E",
   opts=["a frog laying eggs", "pollination by bees", "a human baby's birth", "budding in Hydra"]),
 W("The male gamete in a flowering plant is the:", 1, "(a) pollen grain (1).", "E",
   opts=["pollen grain", "ovule", "seed", "egg"]),
 W("All the water on the Earth together forms the:", 1, "(c) hydrosphere (1).", "E",
   opts=["geosphere", "atmosphere", "hydrosphere", "biosphere"]),
 W("Which of the following planets is made mostly of gases?", 1, "(b) Jupiter. Mercury, Venus, Earth and Mars are small and rocky (1).", "E",
   opts=["Mars", "Jupiter", "Venus", "Mercury"]),
 W("Name the four rocky planets of the solar system in order of increasing distance from the Sun.", 2,
   "Mercury, Venus, Earth, Mars (all four in correct order = 2; three = 1) (2).", "E"),
 W("From space the Earth looks blue and is called the Blue Planet. Why?", 2,
   "Water covers most (about 70%) of the Earth's surface (1), and water looks blue from space (1).", "E", wp=True),
 W("True or false? Give a reason. 'Mars has no atmosphere at all, like Mercury.'", 2,
   "False (1). Mars has an atmosphere, but it is about 100 times thinner than Earth's; Mercury has none (1).", "E"),
 W("Name one plant that can be grown from a stem cutting and one that can be grown from its 'eyes'.", 2,
   "Stem cutting: money plant (sugarcane, bamboo) (1); eyes: potato (1).", "E", wp=True),
 W("Name two greenhouse gases that are released by burning coal and oil.", 1, "Carbon dioxide and methane (1).", "E"),
 W("A small banyan plant is seen growing in a crack in an old wall of a Jaipur haveli. How did the seed reach there?", 2,
   "Birds or other animals eat the fruits (1) and drop the seeds in the crack, where they sprout (1).", "E", wp=True),
 W("Name the three problems that together are called the triple planetary crisis.", 2, "Climate change, biodiversity loss and pollution (2: 1 for two, 2 for three).", "E"),
 W("Which planet is closest to the Sun and which is the farthest?", 1, "Mercury is closest, Neptune is the farthest (1).", "E"),
 W("In the apple comparison, the Earth's crust is as thin as the apple's skin. What does this tell us about where all life exists?", 2,
   "All mountains, rivers, forests, animals and people exist in a very thin layer at the surface (1) of the Earth, a tiny part compared with its size (1).", "E", wp=True),
 W("What are gametes?", 1, "The special reproductive cells (male and female) made by parents in sexual reproduction (1).", "E"),

# ---------------- MEDIUM ----------------
 W("A student says: 'Mercury is the hottest planet because it is the closest to the Sun.' Find the mistake and correct it.", 2,
   "Mercury is not the hottest (1). Venus is hotter (about 450 °C) because its thick carbon dioxide atmosphere traps heat (greenhouse effect), whereas Mercury has no atmosphere (1).", "M"),
 W("Explain what would happen to water on Earth if it were much nearer to the Sun, and if it were much farther from the Sun.", 3,
   "Nearer: too hot, water would evaporate and not stay liquid (1.5). Farther: too cold, water would freeze (1.5). Liquid water is essential for life, so Earth's position in the habitable zone matters.", "M", wp=True),
 W("What would happen to the Earth's atmosphere if the Earth were much smaller? Give an example from the solar system.", 3,
   "Gravity would be weaker (1) and could not hold the gases, which would escape to space (1). Mars has a much thinner atmosphere, and Mercury has none (1).", "M", wp=True),
 W("How is the ozone layer formed and why is it important?", 3,
   "Some oxygen (two-atom molecules) forms ozone, O<sub>3</sub>, a three-atom molecule, creating the ozone layer (1.5). It blocks harmful ultraviolet rays from the Sun, which could damage living things (1.5).", "M"),
 W("How does Earth's magnetic field protect life? What produces the field?", 3,
   "The field acts as a shield (1) that pushes away many cosmic rays and solar wind particles, which could damage the atmosphere and ozone (1). It is probably produced by the moving molten iron in the Earth's core (1).", "M"),
 W("Name the sphere (atmosphere, hydrosphere, geosphere, biosphere) to which each belongs: (i) river water (ii) a granite rock (iii) a banyan tree (iv) the oxygen we breathe.", 3,
   "(i) hydrosphere (ii) geosphere (iii) biosphere (iv) atmosphere (all four = 3; any three = 2) (3).", "M", wp=True),
 W("Differentiate between the greenhouse effect on planets and a greenhouse used for plants.", 3,
   "On planets: gases like CO<sub>2</sub> in the atmosphere absorb radiation given off by the warmed surface and keep the planet warm (e.g. Venus, Earth) (1.5). In a plant greenhouse: glass walls form a closed space that traps warm air, keeping plants warm in a cool climate (1.5).", "M"),
 W("Differentiate between asexual and sexual reproduction in three points.", 3,
   "Asexual: one parent; sexual: two parents (1). Asexual: offspring are exact copies; sexual: offspring have a mix of both parents' genes (1). Examples: binary fission, budding, vegetative propagation vs flowering plants, fish, birds, humans (1).", "M"),
 W("Meena plants a piece of ginger in moist soil. What conditions does it need and what type of reproduction is this? Name two other examples.", 3,
   "It needs water, air and sunlight (1). This is vegetative propagation, a kind of asexual reproduction (1). Other examples: money plant stem cutting, potato eyes, bamboo, sugarcane (any two, 1).", "M", wp=True),
 W("How do Hydra and planaria reproduce or regrow? Name the type of reproduction for Hydra.", 2,
   "Hydra grows buds that break off and become new individuals (budding, asexual) (1). A planaria (flatworm) can regrow from a small fragment (regeneration) (1).", "M"),
 W("Even brothers and sisters of the same parents look different. Explain.", 2,
   "Each gamete carries a different mix of the parents' genetic instructions (1), so each child gets a unique combination of traits (1).", "M", wp=True),
 W("Write the steps from pollination to the formation of a fruit in a flowering plant.", 3,
   "Pollen is carried to another flower by wind, insects or animals (pollination) (1). The male gamete joins the female gamete (ovule) - fertilisation - forming a zygote (1). The zygote becomes the seed, and the fleshy part around the ovule becomes the fruit (1).", "M"),
 W("What is the role of seeds and fruits in the life of a plant?", 2,
   "A seed contains the zygote/embryo with stored food and grows into a new plant when it gets water (1). The fruit protects the seeds and helps their spread when animals and birds eat it (1).", "M"),
 W("How does development take place in (i) fish and frogs (ii) birds (iii) most mammals?", 3,
   "(i) In water, after eggs and sperm are released into it (1). (ii) The egg is laid, and the embryo develops outside the mother with food stored in the egg (1). (iii) The embryo develops inside the mother, who supplies food and oxygen (1).", "M"),
 W("Why does each gamete carry only half of the genetic material of the parent?", 2,
   "When the male and female gametes join, the zygote gets a complete set (1); if each gamete carried a full set, the amount would double in every generation (1).", "M"),
 W("Camels have humps that store fat; some bacteria become resistant to antibiotics. What do these two examples show about reproduction and variation?", 2,
   "Reproduction allows small changes (variations) in offspring (1); some changes help survival in the surroundings, such as desert life or antibiotics, and over generations can produce new features (1).", "M", wp=True),
 W("Explain how burning coal and oil in power plants and vehicles leads to climate change and its effects.", 3,
   "Burning releases extra CO<sub>2</sub> and methane that were locked underground (1); Earth cannot absorb them fast enough, so more heat is trapped - global warming (1). Effects: melting ice caps, rising sea levels flooding coastal cities, extreme weather, loss of species (1).", "M", wp=True),
 W("How can the loss of grasses in a forest harm tigers and foxes? What does this show?", 2,
   "Without grasses, herbivores such as deer and grasshoppers suffer and decrease (1), so predators like tigers and foxes lose their food (1). Every organism has a role in the web.", "M", wp=True),
 W("Name three kinds of pollution and one harmful effect of each.", 3,
   "Air pollution: breathing problems/smog/acid rain/crop damage (1). Water pollution: harms aquatic life (1). Soil pollution: lower crop yields, harmful substances enter the food chain (1).", "M", wp=True),
 W("Match the agreement with its aim: (i) Montreal Protocol (ii) Kyoto Protocol (iii) Paris Agreement (iv) Earth Summit.  Aims: limit warming below 1.5 °C; cut greenhouse gases; reduce CFCs; international efforts for climate and biodiversity.", 3,
   "(i) reduce CFCs, protecting the ozone layer (ii) countries committed to cut greenhouse gases (iii) limit warming to below 1.5 °C (iv) international efforts on climate and biodiversity (all four = 3; three = 2) (3).", "M"),

# ---------------- HARD ----------------
 W("<b>Case study.</b> The table shows facts about four planets. Mercury: average temperature about 170 °C, no atmosphere. Venus: about 450 °C, thick atmosphere, radius 0.95 of Earth. Earth: about 15 °C, atmosphere with oxygen. Neptune: about −200 °C, large gas planet. (i) Which planet is hottest and by how many °C is it hotter than Earth? (ii) Why is Venus hotter than Mercury although it is farther from the Sun? (iii) Name two rocky and two gaseous planets. (iv) Which factor keeps Earth's temperature suitable for life?", 5,
   "(i) Venus; 450 − 15 = 435 °C hotter (1). (ii) Its thick, almost entirely carbon dioxide atmosphere traps heat (greenhouse effect), while Mercury has no atmosphere to hold heat (1.5). (iii) Rocky: Mercury, Venus, Earth, Mars (any two); gaseous: Jupiter, Saturn, Uranus, Neptune (any two) (1). (iv) Right distance from the Sun together with a mild greenhouse effect of its atmosphere, so water stays liquid (1.5).", "H", wp=True),
 W("Explain why we can say the greenhouse effect is both useful and dangerous for the Earth.", 3,
   "Useful: gases such as CO<sub>2</sub> absorb heat radiated by the Earth and keep it warm enough for liquid water; without an atmosphere the Earth would be too cold (1.5). Dangerous: extra CO<sub>2</sub> and methane from burning fuels trap too much heat, causing global warming and climate change; Venus shows how a thick CO<sub>2</sub> atmosphere makes a planet extremely hot (1.5).", "H"),
 W("A spaceship carries soil and water to Mars. Will plants grow there? Give two difficulties that you can think of from what you have learnt in this chapter.", 4,
   "Not easily (1). Mars is farther from the Sun than Earth and so receives less heat; it is cold and water would tend to freeze (1.5). Its atmosphere is about 100 times thinner than Earth's, so it holds little heat and gives little protection (1.5). (Any two sensible difficulties.)", "H", wp=True),
 W("Assertion (A): The Earth's magnetic field is a protective shield for life. Reason (R): It pushes away many cosmic rays and solar wind particles that could damage the atmosphere and reduce ozone. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). Cosmic rays and solar wind could damage the atmosphere and reduce the ozone layer, letting in more UV (1); by deflecting them the field protects life (1).", "H"),
 W("Assertion (A): Offspring in sexual reproduction are not identical to their parents. Reason (R): Offspring get a mixture of genes from two parents. Is A true? Is R true? Does R explain A? Justify.", 3,
   "A is true and R is true (1). Each gamete carries half of the genetic material, and a different mix (1); the zygote gets a new combination from both parents, so R explains A (1).", "H"),
 W("In a hill village near Mount Abu many trees are cut for fuelwood and building roads. Using the four spheres, explain at least four ways this can affect the environment.", 4,
   "Biosphere: loss of plants and habitats, so animals suffer (1). Atmosphere: less oxygen released and more CO<sub>2</sub> left in the air, and changes in rainfall (1). Geosphere: soil becomes loose and erodes, less humus and fertile soil (1). Hydrosphere: less rain, less groundwater and drying of streams (1).", "H", wp=True),
 W("What was the Montreal Protocol? How does the ozone layer help life and why was action needed?", 3,
   "A 1987 international agreement to reduce CFCs (1). The ozone layer blocks harmful UV rays (1); damage to it would let more UV reach the Earth, so action was needed, and the layer is now slowly recovering (1).", "H"),
 W("Your school wants to run a campaign on the 'triple planetary crisis'. Suggest four actions students can take, each linked to one of the three crises.", 4,
   "Climate change: use renewable energy such as solar, save electricity, choose green travel (1). Biodiversity loss: plant native trees, protect habitats, support sustainable use of resources (1). Pollution: better waste management, reduce plastic, stop dumping in water bodies (1). All: reuse, repair, recycle and save energy and water (1).", "H", wp=True),
 W("Compare sexual reproduction in a flowering plant with that in a mammal, using male gamete, female gamete, joining and development.", 4,
   "Male gamete: pollen grain / sperm (1). Female gamete: ovule / egg (1). Joining: pollination then fertilisation giving a zygote that becomes a seed / fertilisation giving a zygote that becomes an embryo (1). Development: seed grows into a plant using stored food after dispersal / embryo develops inside the mother, who supplies food and oxygen (1).", "H"),
 W("Why does life need both reproduction that gives copies of the parent and reproduction that allows variation?", 3,
   "Reproduction passes genes so that a calf grows into a cow and a kitten into a cat - continuity of the species (1). Sexual reproduction gives variation, and some variations help survival when surroundings change (1). Asexual reproduction can quickly multiply an organism (such as a plant from a cutting) with the same useful features (1).", "H"),
 W("A farmer in Sri Ganganagar grows sugarcane from stem pieces every year. (i) Which type of reproduction is this? (ii) Give one advantage. (iii) Why might the whole crop be at risk if a disease affects one plant?", 3,
   "(i) Vegetative propagation (asexual) (1). (ii) The new plants are exact copies, with the same useful qualities, and grow quickly (1). (iii) All plants are identical copies with no variation, so they all share the same weakness (1).", "H", wp=True),
 W("'A small change in oxygen, temperature or ozone could endanger life.' Explain this statement with three examples from the chapter.", 3,
   "Oxygen: needed for breathing and respiration, so a large change would affect all animals (1). Temperature: a change would alter whether water stays liquid, as on Mercury/Venus or distant planets (1). Ozone: less ozone lets in more harmful UV rays (1).", "H"),
 W("Why does a bird's egg have a store of food while a mammal's embryo gets food from the mother? Compare the two ways of development.", 3,
   "In birds the egg is laid and the embryo develops outside the mother, so the egg has to hold the stored food (1.5). In most mammals the embryo develops inside the mother, who supplies food and oxygen directly (1.5).", "H", wp=True),
]

_base = _old(13)
_i = max(i for i, b in enumerate(_base["blocks"]) if b[0] == "h2")
_extra = [
 ("h2", "Worked Examples and Reasoning Skills"),
 ("steps", [
   ("Example 1 — Why is Venus hotter than Mercury?", "Mercury (≈ 170 °C average) is closer to the Sun but has **no atmosphere** to hold heat. Venus (≈ 450 °C) has a thick atmosphere of almost pure **carbon dioxide** that traps heat by the **greenhouse effect**. So atmosphere, and not distance alone, decides the temperature. Difference = 450 − 170 = 280 °C; Venus is 450 − 15 = 435 °C hotter than Earth."),
   ("Example 2 — What if Earth were somewhere else?", "Nearer the Sun → too hot, liquid water evaporates. Farther → too cold, water freezes. Only in the **habitable zone** does water stay liquid. Smaller size → weak gravity, gases escape (Mars' atmosphere ≈ 100 times thinner, Mercury none). Much bigger → gravity so strong it would crush bones."),
   ("Example 3 — Identify the type of reproduction", "Potato 'eyes', ginger, money-plant cutting, sugarcane, bamboo: **vegetative propagation** (asexual, one parent, identical copies). Hydra buds, amoeba and bacteria dividing in two: **asexual**. Fish, frogs, birds, mammals, flowering plants with pollen and ovule: **sexual** (two gametes join into a zygote)."),
   ("Example 4 — Sequence in a flowering plant", "Pollen grains (male gametes in the anther) → carried by wind, water, insects, bats or birds (**pollination**) → male gamete joins the **ovule** (**fertilisation**) → **zygote** → becomes the **seed**, while the fleshy part around the ovule becomes the **fruit** → animals eat the fruit and spread the seeds."),
   ("Example 5 — Chain of effects of burning fuels", "Burning coal/oil → extra CO₂ and methane → more heat trapped (**global warming**) → melting ice caps → rising sea level → flooding of coastal cities; also extreme weather and loss of species. This is **climate change**, the first part of the triple planetary crisis."),
   ("Example 6 — Connecting the four spheres", "Cutting a forest (**biosphere**) → less oxygen added and rainfall change (**atmosphere**) → less water soaked into the ground, streams dry (**hydrosphere**) → soil washed away (**geosphere**). One change spreads through all four, so balance matters."),
 ]),
 ("h2", "Quick Reference Tables"),
 ("table", ["Planet type", "Planets", "Features"], [
   ["Rocky (inner)", "Mercury, Venus, Earth, Mars", "Small, rocky; closer to the Sun"],
   ["Gaseous (outer)", "Jupiter, Saturn, Uranus, Neptune", "Large, mostly gases; farther from the Sun"]]),
 ("table", ["Threat", "Main causes", "Effects", "Possible action"], [
   ["Climate change", "Burning coal and oil: CO₂, methane", "Global warming, melting ice, rising seas, extreme weather", "Renewable energy, saving energy, green travel"],
   ["Biodiversity loss", "Habitat destruction", "Species disappear; food webs break", "Protect habitats, sustainable use by local communities"],
   ["Pollution", "Factories, vehicles, plastic, fertilisers, waste", "Smog, acid rain, harm to aquatic life, poor soil", "Waste management, sustainable farming, reuse-repair-recycle"]]),
 ("note", "REMEMBER", "**Common mistakes:** (1) Venus is hotter than Mercury because of its atmosphere, not its distance. (2) Pollination is transfer of pollen; fertilisation is joining of gametes — they are different. (3) Asexual reproduction gives **identical copies**, not variation. (4) Each gamete carries **half** the genetic material, not all. (5) Ozone is O₃ (three atoms), ordinary oxygen is O₂. (6) The magnetic field protects against cosmic rays and solar wind, not against heat or gravity. (7) The greenhouse effect is natural and useful; the **extra** greenhouse gases are the problem."),
 ("h2", "Real-Life Connections"),
 ("ul", ["**Everyday gardening:** growing money plant stem cuttings, potatoes from eyes, ginger and sugarcane pieces is asexual reproduction; seeds of mango, banyan and neem come from sexual reproduction.",
         "**Weather and climate:** hot summers, floods and cyclones more often than before are linked to climate change; coastal cities worry about rising sea levels.",
         "**Health and sunshine:** the ozone layer shields us from UV rays; the Montreal Protocol shows countries can work together.",
         "**Space and technology:** ISRO's satellite images and the Mangalyaan Mars Orbiter Mission (2013) help study Earth and Mars with low-cost technology.",
         "**What students can do:** reuse, repair, recycle, save water and electricity, use public transport or walk, plant trees, and share ideas."]),
]
_qa2 = [
  ("Why do we say Earth is a Goldilocks planet?", "It lies in the habitable zone: not too hot, not too cold, so water stays liquid."),
  ("Why do sexual reproduction offspring differ from parents?", "They receive a new mix of genes from the male and female gametes."),
  ("What can each of us do about the triple planetary crisis?", "Use renewable energy, conserve resources and biodiversity, manage waste, reuse-repair-recycle."),
]
_blocks = list(_base["blocks"])
_blocks[_i + 1] = ("qa", list(_blocks[_i + 1][1]) + _qa2)
CH = dict(_base, blocks=_blocks[:_i] + _extra + _blocks[_i:],
          takeaways=_base["takeaways"] + ["Planets: four **rocky** (Mercury, Venus, Earth, Mars) and four **gaseous** (Jupiter, Saturn, Uranus, Neptune).",
                                          "Gametes carry **half** the genetic material; pollination (transfer of pollen) comes before fertilisation (joining of gametes)."])

if __name__ == "__main__":
    run(__file__, BANK, 8, "Science", WS, CH)
