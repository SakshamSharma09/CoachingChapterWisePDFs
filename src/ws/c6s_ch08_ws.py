"""Class 6 Science Ch 8 - A Journey through States of Water: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch08"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch08", str(REPO / "src/rn_work/c6_sci/ch08.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Ice, water and water vapour are:", 1, "(c) three states of the same substance", "E", opts=["three different substances", "two substances", "three states of the same substance", "all solids"]),
W("The change of liquid water into water vapour is called:", 1, "(a) evaporation", "E", opts=["evaporation", "condensation", "freezing", "melting"]),
W("Droplets on the outside of a glass of ice-cold water come from:", 1, "(d) water vapour of the air", "E", opts=["water seeping through the glass", "melted glass", "the ice outside", "water vapour of the air"]),
W("The amount of water vapour present in air is called:", 1, "(b) humidity", "E", opts=["pressure", "humidity", "wind", "density"]),
W("Which of these makes clothes dry the slowest?", 1, "(c) a rainy, humid day", "E", opts=["a hot sunny day", "a windy day", "a rainy, humid day", "spreading the clothes wide"]),
W("Water in a matka stays cool because of:", 1, "(b) evaporation from the pores", "E", opts=["the colour of clay", "evaporation from the pores", "heat of the Sun", "freezing of water"]),
W("Clouds are formed when water vapour condenses around tiny ______.", 1, "dust particles.", "E"),
W("Write True or False: Water vapour is visible.", 1, "False. Water vapour is invisible; the white 'steam' we see is tiny water droplets. (1)", "E"),
W("Name the process by which ice changes into water.", 1, "Melting. (1)", "E"),
W("Name the process by which water changes into ice.", 1, "Freezing. (1)", "E"),
W("Name the three states of water.", 2, "Solid (ice), liquid (water) and gas (water vapour). (2)", "E"),
W("Give two examples of evaporation from daily life.", 2, "Any two: wet clothes drying, puddles disappearing, a mopped floor drying, sweat drying, hand sanitiser disappearing. (1+1)", "E"),
W("Write two examples of condensation.", 2, "Any two: dew on leaves in the morning, drops on the outside of a cold glass, drops on the inner side of a lid covering boiling water. (1+1)", "E"),
W("Name two other substances, besides water, that can exist as solid and liquid.", 2, "Any two: wax, coconut oil, ghee. (1+1)", "E"),
W("Which state of water has no fixed shape and flows?", 1, "Liquid water. (1)", "E"),
W("What is the water cycle? Answer in one line.", 2, "The continuous circulation of water between the Earth's surface and the atmosphere through evaporation, condensation and rain. (2)", "E"),
W("Name two forms in which water falls from clouds.", 2, "Rain and snow (or hail). (1+1)", "E"),
W("Why does the smell of food cooking in the kitchen reach us in other rooms?", 1, "Gases spread out in all directions through the air. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Activity: a tablespoon of water is put on a steel plate in the Sun. After some time the plate is dry. Where did the water go? Why can we say it did not seep into the plate?", 2, "It changed into water vapour by evaporation (1). Steel has no pores for water to seep through (1).", "M"),
W("Puneet says, \"The drops on the outside of my cold water glass came out from inside through the glass.\" How can you show he is wrong?", 3, "Mark the water level inside the glass before and after (1). If the level does not go down, no water has seeped out (1). The drops come from water vapour in air condensing on the cold surface (1).", "M", wp=True),
W("Arrange the processes for the formation of rain in order: condensation, cooling of vapour high above, evaporation, falling of rain.", 2, "Evaporation, cooling of vapour high above, condensation (cloud formation), falling of rain. (2)", "M"),
W("Why does a wet cloth spread on a clothesline dry faster than the same cloth kept folded?", 2, "A spread cloth has a larger exposed area (1) and more air passes over it, so evaporation is faster (1).", "M", wp=True),
W("Give any two reasons why clothes dry faster in summer than in the rainy season.", 2, "In summer the temperature is higher and the air is less humid (1+1). In the rainy season humidity is high so evaporation is slow.", "M", wp=True),
W("Why does a person sitting under a fan feel cooler when sweating?", 2, "Moving air helps sweat evaporate faster (1), and evaporation takes heat from the body and cools it (1).", "M", wp=True),
W("A steel pot and an earthen pot (matka) are filled with water on a summer day. Which water will be cooler after some hours and why?", 2, "The water in the matka (1), because water seeps through its tiny pores and evaporates from the outer surface, cooling the water inside; steel has no pores (1).", "M", wp=True),
W("Prepare a table to compare the three states of water on shape and flow.", 3, "Ice: fixed shape, does not flow. Water: takes shape of container, flows. Water vapour: no fixed shape, spreads in all available space. (1 each)", "M"),
W("Complete: (i) Solid to liquid is ____ (ii) Liquid to solid is ____ (iii) Liquid to gas is ____ (iv) Gas to liquid is ____", 2, "(i) melting (ii) freezing (iii) evaporation (iv) condensation. (½ each)", "M"),
W("Why do we sprinkle water on a hot floor or rooftop in summer?", 2, "Water evaporates and takes heat from the floor, cooling it and the surrounding air. (2)", "M", wp=True),
W("Coconut oil kept in a bottle becomes solid in winter in North India. Which change of state is it? How can it be changed back?", 2, "Freezing (solidifying) (1). Keeping it in a warm place or warming it makes it melt back to liquid (1).", "M", wp=True),
W("Why are droplets seen on the inner side of the lid of a pan in which water is boiling?", 2, "Hot water vapour rising from the pan touches the cooler lid and condenses into drops. (2)", "M", wp=True),
W("In a mass-measuring activity a tumbler of ice water covered with a steel plate is weighed every 5 minutes. The reading increased from 250 g to 256 g. Explain.", 3, "Water vapour of the air touched the cold tumbler and condensed (1). This added water on the tumbler, so the mass increased (1) by 256 – 250 = 6 g (1).", "M", wp=True),
W("List the four things that affect the speed of evaporation.", 2, "Exposed area, temperature (sunlight), wind (air movement) and humidity. (½ each)", "M"),
W("Why is it advised to change only one condition at a time when testing the speed of evaporation?", 2, "If two things change together we cannot tell which one caused the difference in speed. (2)", "M"),
W("Find the mistake: \"Steam coming out of a kettle is water vapour and we can see it clearly.\"", 2, "Water vapour is invisible (1). What we see is tiny droplets of water formed when some vapour cools (1).", "M"),
W("What is a pot-in-pot cooler? Why is the sand between the pots kept wet?", 3, "A small earthen pot kept inside a larger one with sand packed between and covered with a lid or wet cloth (1). Water in the wet sand evaporates (1) and cools the inner pot, keeping vegetables and fruits fresh for some days (1).", "M"),
W("Why is a burnt piece of newspaper added in the activity in which a cloud is made in a bottle?", 2, "It gives dust (smoke) particles (1) around which water vapour can condense to form a clearer haze, like a cloud (1).", "M"),
W("Write two ways to save water at home, using ideas from the chapter.", 2, "Any two: do not waste water while brushing, close taps, reuse water used to wash vegetables for plants, keep water bodies clean. (1+1)", "M", wp=True),
# ---------------- HARD ----------------
W("Radha has 3 identical wet handkerchiefs. She spreads one in sunlight, spreads one in shade and keeps one folded in shade. Arrange them in the order in which they dry, first to last, and give reasons.", 3, "Order: spread in sunlight, spread in shade, folded in shade (1). The sunlit one has a larger area and higher temperature (1). The folded one has the smallest exposed area and no sun, so it dries last (1).", "H", wp=True),
W("A farmer sprinkled water on a straw roof every afternoon in May and found the house cooler inside. Explain the science involved and say whether the cooling would be better on a humid day.", 3, "Evaporation of sprinkled water takes heat from the roof (1) and cools the house (1). On a humid day the evaporation is slower, so the cooling is less (1).", "H", wp=True),
W("Why is the following statement incomplete? \"Puddles on the playground disappear because the water evaporates.\" What else may happen to the puddle water?", 3, "Part of the water evaporates (1) but part also seeps into the soil (1) (the ground has pores), so both processes cause the puddle to disappear (1).", "H", wp=True),
W("Seema wants to find out whether wind makes water evaporate faster. She pours 20 mL of water in two identical plates, keeps one under a fan and the other far from the fan. List what she must keep the same and what she must observe.", 3, "Keep the same: the quantity of water, the type and size of plate, the place or temperature and the time (any three, 1.5). Change only the wind (fan). Observe which plate becomes dry first (1.5); it will be the one under the fan.", "H", wp=True),
W("Explain the water cycle in steps, naming the four processes involved, and give one reason why we should conserve water although the cycle never ends.", 4, "Evaporation from oceans and land makes water vapour (1). Vapour rises, cools and condenses around dust particles to form clouds (1). Rain, snow or hail fall (1). Water flows through rivers and underground back to the ocean. Only a small fraction of the Earth's water is fit for use, so it must be conserved and not polluted (1).", "H"),
W("Three students say: Aman, \"Cloud droplets are water vapour.\" Bela, \"Clouds are made of tiny drops of liquid water.\" Chetan, \"Clouds are solid ice only.\" Who is correct and why?", 3, "Bela is correct (1). Vapour is invisible, so clouds, which we can see, are tiny water droplets formed by condensation (1). Ice or hail forms only in special conditions, so Chetan is wrong (1).", "H", wp=True),
W("A hot and humid city like Mumbai and a hot and dry city like Jodhpur both have the same temperature. Where will wet clothes dry faster? Explain using humidity.", 3, "In Jodhpur (1). The air there holds less water vapour (low humidity), so it can take up more water from the clothes and evaporation is faster (1). In humid Mumbai the air already has a lot of vapour, so evaporation is slower (1).", "H", wp=True),
W("Anu keeps two identical glasses, one with hot tea and the other with cold lemonade. After 10 minutes, droplets form on the outside of only one. Which one and why?", 3, "On the glass with cold lemonade (1), because its cold surface cools the air next to it and the water vapour in air condenses into droplets (1). The hot tea glass is not colder than the air, so no condensation happens on the outside (1).", "H", wp=True),
W("The mass of a tumbler of water was 300 g. It is kept open for two days on a table and its mass becomes 285 g. Find the loss and explain the cause. How can the loss be made faster?", 4, "Loss = 300 – 285 = 15 g (1). Water has evaporated slowly from the surface (1). To speed it up use a wider vessel, keep in warm sunlight, in moving air or a dry place (2).", "H", wp=True),
W("A student claims that the water in a matka stays cool even on a hot day because \"the clay is naturally cold\". Plan a test to show that the real reason is evaporation.", 4, "Take two similar pots, one clay matka and one steel pot, with the same water at the same start temperature (1). Keep them in the same place and read the temperature with a thermometer after a few hours (1). The water in the clay pot will be cooler (1). Then coat the matka with wax or paint to block the pores; its water will no longer stay cool, proving evaporation is the cause (1).", "H", wp=True),
W("Why should clothes not be hung in a closed, damp room? Explain using the idea of humidity and name two ways to dry them faster.", 3, "In a closed room the vapour from clothes stays in the air, so humidity rises and evaporation becomes slow (1). Open windows or use a fan so that moist air is removed (1), and spread the clothes fully or dry them in sunlight (1).", "H", wp=True),
W("Why do we say that evaporation takes place continuously at all temperatures? Give two proofs from the chapter that water does not need to boil to evaporate.", 3, "Water evaporates at room temperature, not only at boiling (1). Proof 1: wet clothes dry in the shade and puddles disappear on a cool day (1). Proof 2: water on a steel plate or sweat on our body disappears without boiling (1).", "H"),
W("Compare evaporation and condensation by writing two differences in a table, with one example of each.", 3, "Evaporation: liquid becomes gas; needs heat or occurs even at room temperature; example: drying of clothes. Condensation: gas becomes liquid; happens on cooling or when vapour touches a cold surface; example: drops on a cold glass. (1+1+1)", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "8.9 Words to Know"),
 ("table", ["Term", "Meaning", "Example"],
  [["**State of matter**", "The form of a substance: solid, liquid or gas", "Ice, water, vapour"],
   ["**Melting**", "Solid changes into liquid on heating", "Ice into water"],
   ["**Freezing**", "Liquid changes into solid on cooling", "Water into ice in a freezer"],
   ["**Evaporation**", "Liquid changes into vapour (gas); happens at any temperature", "Drying of wet clothes"],
   ["**Condensation**", "Vapour changes into liquid on cooling", "Dew; drops on a cold glass"],
   ["**Humidity**", "Amount of water vapour in air", "High on rainy days"],
   ["**Water cycle**", "Continuous circulation of water between earth and air", "Sea → clouds → rain → river → sea"]]),
 ("h2", "8.10 Activities and What They Show"),
 ("table", ["Activity", "What we do", "What we see", "What it shows"],
  [["8.1", "Keep an ice cube in a cup", "It turns to water", "Ice and water are one substance"],
   ["8.2", "Put a spoon of water on a steel plate in the Sun", "Plate dries, no seepage", "Water changes into vapour (evaporation)"],
   ["8.3", "Ice water in a glass tumbler", "Drops form on the outside", "Water vapour in air condenses on a cold surface"],
   ["8.4", "Weigh the covered tumbler every 5 minutes", "Mass increases; water level unchanged", "No seepage; condensation adds water"],
   ["8.9", "Pot-in-pot cooler with wet sand", "Inner pot becomes cooler", "Evaporation causes cooling"],
   ["8.10", "Squeeze and release a bottle with a little water and burnt paper", "A cloud-like haze appears", "Vapour condenses around dust particles"]]),
 ("h2", "8.11 Worked Examples and Reasoning"),
 ("steps", [("Example 1 — Why do clothes dry slowly in the monsoon?", "In the monsoon the air has a lot of water vapour (high humidity), so the clothes cannot give out more vapour easily. Evaporation is slow. Hanging them near a fan or in an open, airy place helps because moving air carries away the vapour."),
  ("Example 2 — Which tray will dry first?", "A wide flat plate and a narrow tall bottle hold the same 50 mL of water in the same place. The plate has the larger exposed area, so its water **evaporates first**. This shows area affects evaporation. Only area was different; everything else was kept the same (fair test)."),
  ("Example 3 — Change in mass", "A covered tumbler of ice water has mass 200 g at the start and 205 g after 30 minutes. Gain = 205 – 200 = **5 g**. The extra 5 g is water that condensed from the air on the cold tumbler."),
  ("Example 4 — From sea to rain", "The Sun heats the sea; water evaporates and rises as vapour; higher up it is cool and the vapour condenses on dust particles to form clouds; the drops grow heavy and fall as rain; the rain flows through rivers back to the sea."),
  ("Example 5 — Why does a hot tea glass not get droplets outside?", "Condensation on the outside needs a surface colder than the air. A cold drink's glass is colder, so vapour condenses on it. A hot tea glass is warmer than the air, so no drops form on its outer side.")]),
 ("note", "IMPORTANT", "**Seeping and evaporating are different.** Seeping means liquid going through pores into a solid; evaporation means liquid changing into vapour. A steel plate shows evaporation because steel has no pores."),
 ("h2", "8.12 Common Mistakes and Misconceptions"),
 ("table", ["Wrong idea", "Correct idea"],
  [["Ice, water and steam are different substances.", "They are three states of the same substance, water."],
   ["Water evaporates only when it boils.", "Evaporation occurs at all temperatures, e.g. wet clothes drying in shade."],
   ["The white cloud over a hot pan is water vapour.", "Water vapour is invisible; the white cloud is tiny water droplets."],
   ["Droplets on a cold glass seep out of the glass.", "They are condensed water vapour from the air."],
   ["Clothes dry faster when humidity is high.", "High humidity makes evaporation slower."],
   ["Clouds are made of water vapour.", "Clouds are made of tiny droplets formed when vapour condenses."]]),
 ("note", "REMEMBER", "Keep a small memory list: **melting** (solid → liquid), **freezing** (liquid → solid), **evaporation** (liquid → gas), **condensation** (gas → liquid)."),
 ("h2", "8.13 Higher Order Questions"),
 ("qa", [("Why should we not waste water even though the water cycle keeps recycling it?", "Only a small part of the Earth's water is fit for use. Demand grows with population, and polluted water cannot be used, so it must be saved."),
  ("How does the pot-in-pot cooler work without electricity?", "Water in the wet sand evaporates and takes heat from the inner pot, cooling it and the food inside."),
  ("Why do we feel cool when we put sanitiser on our hands?", "The sanitiser evaporates quickly and takes heat from the skin, causing a cooling effect."),
  ("Why do we feel more uncomfortable on a humid day even if the temperature is not very high?", "Sweat evaporates slowly in humid air, so the body does not cool well.")]),
]
CH["takeaways"] += ["**Seeping** is not the same as evaporation; a steel plate has no pores, yet water disappears by evaporation.", "Droplets on a cold glass come from condensation of vapour in the air, not from inside the glass."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
