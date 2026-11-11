"""Class 8 Science Ch 12 How Nature Works in Harmony - extras."""
from common import AR4, Q

AR = [
 AR4("Green plants are called producers.", "Plants make their own food by photosynthesis using sunlight.", "a", "Making food from simple substances is what makes them producers."),
 AR4("Decomposers are essential in an ecosystem.", "Decomposers break down dead plants and animals and return nutrients to the soil.", "a", "Nutrient recycling depends on decomposers."),
 AR4("Energy flow in an ecosystem is one-way.", "Energy passes from producers to consumers, and part of it is lost as heat at each step.", "a", "Energy moves in one direction and is not recycled."),
 AR4("A food web is a network of many interlinked food chains.", "Decomposers break down dead organisms.", "b", "Both are true, but R does not explain A."),
 AR4("Removing all the frogs from a pond has no effect on the other organisms.", "Every organism in a food chain depends on others for food.", "d", "A is false, since snakes lose food and insects increase; R is true."),
 AR4("Food chains usually have only four or five links.", "All the energy in one trophic level passes to the next level without loss.", "c", "A is true; R is false, much energy is lost at each level."),
]

CASE = [
 Q("<b>Case study.</b> In a field in Punjab, wheat plants are eaten by grasshoppers, grasshoppers by frogs, frogs by snakes and snakes by eagles. Farmers killed many snakes, and soon the number of frogs increased and the number of grasshoppers fell sharply. "
   "(i) Name the producer in this food chain. (ii) Name the top carnivore. (iii) Name the primary consumer. (iv) Explain why killing snakes disturbed the balance of this ecosystem.",
   "(i) Wheat (1). (ii) Eagle (1). (iii) Grasshopper (1). (iv) With fewer snakes, more frogs survive and eat more grasshoppers, while eagles lose food; a change at one level affects all the others, so the balance is upset (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A village pond in Kerala has algae, small fish, big fish and a heron. Dead fish and fallen leaves at the bottom are slowly broken down by bacteria and fungi. The pond also has sunlight, dissolved oxygen and mud. "
   "(i) Name one biotic and one abiotic component. (ii) What role do bacteria and fungi play? (iii) Which organism is the producer? (iv) Why is the Sun called the ultimate source of energy for this pond?",
   "(i) Biotic: fish (or algae); abiotic: sunlight (or mud/oxygen) (1). (ii) Decomposers (1). (iii) Algae (1). (iv) Algae use sunlight to make food by photosynthesis, and all other organisms depend directly or indirectly on this food for energy (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Meera makes a compost pit in her garden in Ranchi using kitchen waste and dry leaves. After some weeks the waste turns into dark, crumbly manure. She mixes it with the soil in her vegetable garden and the plants grow well. "
   "(i) Which organisms act on the waste in the compost pit? (ii) What is formed from the waste? (iii) What does it add to the soil? (iv) Explain how this shows recycling of nutrients in nature.",
   "(i) Decomposers (bacteria, fungi) (1). (ii) Compost (manure) (1). (iii) Nutrients, improving soil fertility (1). (iv) Nutrients in dead matter are released by decomposers into the soil and are taken up again by plants, so they pass back into the food chain (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Components of an ecosystem", ["Biotic: producers, consumers, decomposers. Abiotic: sunlight, air, water, soil, temperature.", "Producers (green plants) make food by photosynthesis; the Sun is the ultimate source of energy."]),
 ("Consumers", ["Herbivores eat plants; carnivores eat animals; omnivores eat both.", "Primary consumers are herbivores; secondary consumers eat primary consumers; the top carnivore ends the chain."]),
 ("Chains and webs", ["Food chain example: grass $\\to$ grasshopper $\\to$ frog $\\to$ snake $\\to$ eagle (arrow points towards the eater).", "Food web: many interlinked food chains; more stable than a single chain."]),
 ("Energy and balance", ["Energy flows one way: producers $\\to$ consumers; part is lost as heat at each step.", "Number of organisms generally decreases from producers to top carnivores.", "Decomposers recycle nutrients; removing one species can upset the balance."]),
]

MISTAKES = [
 "Drawing food-chain arrows from the eater to the food; the arrow points towards the organism that eats.",
 "Leaving out decomposers or calling them consumers; bacteria and fungi form a separate group.",
 "Starting a food chain with an animal; it always starts with a producer.",
 "Saying energy is recycled like nutrients; it flows one way and is lost as heat.",
 "Treating a food chain and a food web as the same; a web has many interlinked chains.",
 "Calling sunlight or air a biotic component; they are abiotic.",
]
