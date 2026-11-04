"""Class 10 Science Ch 13 - Our Environment (hand-written graded banks)."""
from scix import tier

SLUG, NAME, CHNO = "Our_Environment", "Our Environment", 13

# ============================ NCERT-TYPE ============================
nA = """
An ecosystem consists of ~~ biotic and abiotic components ~~ only plants ~~ only animals ~~ only non-living things ~~ All living and non-living parts interact.
Which of the following is an abiotic component of an ecosystem? ~~ Temperature ~~ Bacteria ~~ Fungi ~~ Grass ~~ Non-living factor.
Which of the following are producers? ~~ Green plants ~~ Deer ~~ Fungi ~~ Snakes ~~ They make food by photosynthesis.
Organisms that depend on others for food are called ~~ consumers ~~ producers ~~ autotrophs ~~ decomposers only ~~ Heterotrophs.
Which one of the following is a decomposer? ~~ Fungi ~~ Grass ~~ Hawk ~~ Frog ~~ They break down dead remains.
Organisms that feed on plants are called ~~ herbivores ~~ carnivores ~~ omnivores ~~ decomposers ~~ Primary consumers.
Which of these is an omnivore? ~~ Human beings ~~ Cow ~~ Tiger ~~ Lion ~~ Eats both plants and animals.
An artificial ecosystem is ~~ a crop field ~~ a forest ~~ a pond ~~ a lake ~~ Man-made, e.g. crop field or aquarium.
A natural ecosystem is ~~ a forest ~~ a garden ~~ an aquarium ~~ a crop field ~~ Not man-made.
The ultimate source of energy for all ecosystems is ~~ the Sun ~~ the Moon ~~ water ~~ wind ~~ Producers capture solar energy.

A food chain always begins with ~~ producers ~~ herbivores ~~ carnivores ~~ decomposers ~~ Green plants fix energy.
Which of the following is a correct food chain? ~~ Grass, grasshopper, frog, snake ~~ Frog, grass, snake, grasshopper ~~ Snake, frog, grasshopper, grass ~~ Grass, snake, frog, grasshopper ~~ Producer to consumers in order.
The various steps in a food chain are called ~~ trophic levels ~~ habitats ~~ niches ~~ ecosystems ~~ Each is a feeding level.
In a food chain, the first trophic level is occupied by ~~ producers ~~ herbivores ~~ carnivores ~~ decomposers ~~ Plants and algae.
The primary consumers in a food chain occupy the ~~ second trophic level ~~ first trophic level ~~ third trophic level ~~ fourth trophic level ~~ Herbivores.
Only about this percentage of energy passes from one trophic level to the next ~~ 10 ~~ 90 ~~ 50 ~~ 1 ~~ The 10 per cent law.
In a food chain, energy flow is ~~ unidirectional ~~ cyclic ~~ bidirectional ~~ random ~~ It flows from producers to consumers and is not reused.
A network of many interconnected food chains is called ~~ a food web ~~ a pyramid ~~ a niche ~~ a habitat ~~ Several chains.
If 10,000 J of energy is available at the producer level, the energy available to the secondary consumer is ~~ 100 J ~~ 1000 J ~~ 10 J ~~ 10,000 J ~~ 10 per cent of 10 per cent.
Number of trophic levels in a food chain is usually limited to 3 or 4 because ~~ energy is lost at each step ~~ food is not available ~~ predators are few ~~ plants are few ~~ Little energy remains at higher levels.

The ozone layer is present in the ~~ stratosphere ~~ troposphere ~~ lithosphere ~~ hydrosphere ~~ In the upper atmosphere.
Ozone is a molecule made of ~~ three oxygen atoms ~~ two oxygen atoms ~~ one oxygen atom ~~ oxygen and nitrogen ~~ O3.
The ozone layer protects the earth from ~~ harmful ultraviolet radiation ~~ infrared rays ~~ visible light ~~ sound waves ~~ UV rays can cause skin cancer.
The ozone layer is depleted mainly by ~~ chlorofluorocarbons (CFCs) ~~ carbon dioxide ~~ oxygen ~~ nitrogen ~~ Used in refrigerators and aerosols.
Which of the following is a biodegradable substance? ~~ Vegetable peels ~~ Plastic bags ~~ Glass bottles ~~ Aluminium cans ~~ Broken down by microbes.
Which of the following is non-biodegradable? ~~ Plastic ~~ Paper ~~ Cotton ~~ Wool ~~ Persists in the environment.
Substances which can be broken down by microorganisms are ~~ biodegradable ~~ non-biodegradable ~~ synthetic ~~ inorganic only ~~ Natural decomposition.
The increase in concentration of harmful chemicals at successive trophic levels is called ~~ biomagnification ~~ eutrophication ~~ photosynthesis ~~ decomposition ~~ Accumulates in the food chain.
Which trophic level has the highest concentration of harmful chemicals like pesticides? ~~ Top carnivore ~~ Producer ~~ Herbivore ~~ Decomposer ~~ Biomagnification.
Use of dustbins, recycling and composting are methods of ~~ waste management ~~ food preservation ~~ water purification ~~ air purification ~~ Reducing pollution.
""".strip()
nB = """
Differentiate between biotic and abiotic components of an ecosystem. ~~ Biotic: all living organisms|1 ~~ Abiotic: non-living factors like air, water, soil and temperature|1
What are producers? Give two examples. ~~ Organisms that make their own food by photosynthesis|1 ~~ Green plants, algae|1
What are decomposers? Mention their role. ~~ Microorganisms like bacteria and fungi|1 ~~ Break down dead remains and wastes into simple substances, recycling nutrients|1
Define a food chain. Give an example. ~~ A series of organisms in which food and energy pass from one to another|1 ~~ Grass, grasshopper, frog, snake|1
What is a trophic level? ~~ Each step of a food chain|1 ~~ Where the organisms obtain food in the same manner|1
State the 10 per cent law. ~~ Only 10% of the energy is passed to the next trophic level|1 ~~ The rest is lost as heat or used in life processes|1
Why can a food chain not have more than 4 or 5 trophic levels? ~~ Energy decreases at each successive level|1 ~~ Too little energy remains for higher levels|1
What are CFCs? Name one use. ~~ Chlorofluorocarbons|1 ~~ Used as refrigerants and in aerosol sprays|1
What is the role of the ozone layer? ~~ It absorbs harmful UV radiation of the Sun|1 ~~ It protects living beings|1
What is biomagnification? ~~ Accumulation of non-degradable chemicals in successive trophic levels|1 ~~ Concentration increases up the food chain|1
Differentiate between biodegradable and non-biodegradable waste. ~~ Biodegradable: broken down by microbes, e.g. paper|1 ~~ Non-biodegradable: not broken down, e.g. plastic|1
Why should we avoid using plastic bags? ~~ They are non-biodegradable|1 ~~ They cause pollution and harm animals|1
""".strip()
nC = """
Explain the difference between a food chain and a food web. ~~ Food chain: a single linear sequence of organisms|1 ~~ Food web: many interconnected food chains|1 ~~ Food web gives stability to the ecosystem|1
Describe the flow of energy in an ecosystem. ~~ Sun is the source of energy|1 ~~ Producers trap solar energy in food|1 ~~ Energy passes along the chain, with a loss at each level|1
Why is the flow of energy in an ecosystem unidirectional? ~~ Energy captured by producers passes to consumers|1 ~~ It cannot return to the Sun|1 ~~ Energy lost as heat is not reused|1
How does energy get lost at each trophic level? ~~ Used in respiration and movement|1 ~~ Lost as heat to the environment|1 ~~ Only about 10% is stored in the body|1
Calculate the energy available to the third trophic level if the producers have 20,000 J of energy. ~~ Second level: 10% of 20,000 = 2000 J|1 ~~ Third level: 10% of 2000|1 ~~ 200 J|1
Why are producers called the base of the food chain? ~~ They make food by photosynthesis|1 ~~ All consumers depend on them|1 ~~ They capture solar energy first|1
State three reasons for the role of decomposers in the ecosystem. ~~ They break down dead organisms|1 ~~ They return nutrients to the soil|1 ~~ They keep the environment clean|1
What would happen if all the decomposers were removed from the ecosystem? ~~ Dead organisms and wastes would pile up|1 ~~ Nutrients would not be recycled|1 ~~ The producers would suffer for lack of nutrients|1
What is the effect of the removal of a trophic level in a food chain? Is it the same for all levels? ~~ Removal of one level disturbs the chain|1 ~~ Removing herbivores affects both plants and carnivores|1 ~~ Impact is greater for some levels than others|1
What is ozone? How is it formed in the upper atmosphere? ~~ Ozone is a molecule of three oxygen atoms|1 ~~ UV radiation splits O2 into atomic oxygen|1 ~~ Atomic oxygen combines with O2 to form O3|1
How does the ozone layer get damaged? State its effects. ~~ By CFCs|1 ~~ Ozone hole allows more UV to reach the earth|1 ~~ Causes skin cancer, cataract and damage to crops|1
How can we reduce the damage to the ozone layer? ~~ Reduce the use of CFC-containing products|1 ~~ Use CFC-free refrigerants|1 ~~ Follow international agreements (UNEP)|1
Differentiate between a natural and an artificial ecosystem with examples. ~~ Natural: forest, pond, lake|1 ~~ Artificial: crop fields, aquarium, garden|1 ~~ Natural has self-sustaining balance; artificial needs human care|1
Explain how the biomagnification of pesticides occurs. ~~ Pesticides enter the food chain from crops and water|1 ~~ They are non-degradable and get stored in bodies|1 ~~ Concentration rises at higher trophic levels|1
Why do human beings have the highest level of pesticides in their bodies? ~~ Humans are at the top of the food chain|1 ~~ Pesticides get accumulated through biomagnification|1 ~~ Foods like grains, vegetables and milk carry them|1
List three problems caused by the disposal of waste generated by us. ~~ Non-biodegradable waste persists|1 ~~ Pollutes soil and water|1 ~~ Harms animals and creates health hazards|1
What are the harmful effects of plastics on the environment? ~~ They are non-biodegradable|1 ~~ Block drains and cause water-logging|1 ~~ Harm animals when eaten|1
Suggest three ways of reducing the waste produced at home. ~~ Reduce, reuse, recycle|1 ~~ Compost vegetable waste|1 ~~ Use cloth or jute bags|1
""".strip()
nD = """
What is an ecosystem? Describe its biotic and abiotic components with examples. ~~ Ecosystem: all living and non-living things interacting in an area|1 ~~ Biotic: producers, consumers, decomposers|1 ~~ Examples: plants, deer, fungi|1 ~~ Abiotic: air, water, soil, sunlight, temperature|1 ~~ Biotic components depend on abiotic components|1
Explain the different types of organisms in an ecosystem (producers, consumers, decomposers) and their roles with examples. ~~ Producers make food by photosynthesis|1 ~~ Consumers: herbivores, carnivores, omnivores|1 ~~ Decomposers break down dead matter|1 ~~ Examples: grass, deer, lion|1 ~~ Bacteria and fungi are decomposers|1
What is a food chain? Construct a food chain of four trophic levels and name each level. Explain why the number of levels is limited. ~~ Series of organisms linked by feeding|1 ~~ Grass, grasshopper, frog, snake|1 ~~ Producer, primary consumer, secondary consumer, tertiary consumer|1 ~~ Energy decreases up the levels|1 ~~ Only 10% passes on, so chains are short|1
Explain the 10 per cent law. In a food chain grass, deer, tiger, if the grass has 10,000 J, how much energy reaches the tiger? ~~ Only 10% of energy is transferred to the next level|1 ~~ Rest lost as heat and used in life processes|1 ~~ Deer: 1000 J|1 ~~ Tiger: 100 J|1 ~~ Energy decreases at each trophic level|1
Explain the flow of energy in an ecosystem and why it is called unidirectional. ~~ Sun is the source|1 ~~ Producers convert solar energy into chemical energy|1 ~~ Energy passes to consumers|1 ~~ It does not return to the previous level|1 ~~ Energy is lost as heat at each level|1
Describe the effects of ozone depletion. Name the chemicals causing it and the steps taken to reduce it. ~~ UV radiation increases|1 ~~ Causes skin cancer and cataract|1 ~~ Chemicals: CFCs from refrigerators and aerosols|1 ~~ UNEP agreed in 1987 to freeze CFC production|1 ~~ Later CFC-free products were developed|1
What is biomagnification? Explain with an example of a food chain how a non-degradable pesticide gets concentrated. ~~ Increase in concentration of harmful chemicals along a food chain|1 ~~ Pesticide in water or crops|1 ~~ Consumed by herbivores and accumulates|1 ~~ Carnivores accumulate even more|1 ~~ Top consumers like humans have the highest level|1
Distinguish between biodegradable and non-biodegradable substances with examples. Explain the problem each poses when thrown away. ~~ Biodegradable: broken down by microbes|1 ~~ Examples: food, paper, cotton|1 ~~ Non-biodegradable: plastic, glass, DDT|1 ~~ They persist for a long time|1 ~~ They pollute and harm living beings|1
Describe the effects of garbage and waste disposal on the environment and ways of waste management. ~~ Waste can pollute air, soil and water|1 ~~ Plastic and chemicals harm animals|1 ~~ Solutions: reduce, reuse and recycle|1 ~~ Composting biodegradable waste|1 ~~ Segregation of waste at home|1
What is a food web? Explain how it differs from a food chain and why it gives stability to an ecosystem. ~~ Food web is a network of interconnected food chains|1 ~~ In a food chain, one path|1 ~~ In a food web, many alternate pathways|1 ~~ If one species is lost, others can take over|1 ~~ So the ecosystem remains stable|1
How is ozone formed in the stratosphere and how is it destroyed by CFCs? Why is its depletion a concern? ~~ O2 is split by UV into oxygen atoms|1 ~~ Atoms combine with O2 to form O3|1 ~~ CFC releases chlorine atoms in the stratosphere|1 ~~ Chlorine breaks ozone into oxygen|1 ~~ Depletion lets harmful UV reach the earth|1
Explain how human activities have affected the environment, with reference to plastics, CFCs, and pesticides. Suggest how each can be controlled. ~~ Plastics: non-degradable, so use alternatives and recycle|1 ~~ CFCs: use CFC-free products|1 ~~ Pesticides: biomagnification, so use organic farming|1 ~~ These have affected living beings|1 ~~ Awareness and rules are needed|1
""".strip()

# ============================ EASY ============================
eA = """
All the living organisms in an environment are called ~~ biotic components ~~ abiotic components ~~ producers only ~~ decomposers only ~~ Living things.
Which of the following is a non-living factor? ~~ Sunlight ~~ Frog ~~ Plant ~~ Fungus ~~ Abiotic.
Green plants are called ~~ producers ~~ consumers ~~ decomposers ~~ parasites ~~ They make their own food.
Animals which eat only plants are ~~ herbivores ~~ carnivores ~~ omnivores ~~ scavengers ~~ Plant-eaters.
Animals which eat only flesh are ~~ carnivores ~~ herbivores ~~ omnivores ~~ decomposers ~~ Meat-eaters.
Animals which eat both plants and animals are ~~ omnivores ~~ herbivores ~~ carnivores ~~ producers ~~ Like humans and crows.
A lion is a ~~ carnivore ~~ herbivore ~~ producer ~~ decomposer ~~ Eats animals.
A goat is a ~~ herbivore ~~ carnivore ~~ omnivore ~~ decomposer ~~ Eats grass.
Bacteria that break down dead plants and animals are called ~~ decomposers ~~ producers ~~ herbivores ~~ carnivores ~~ Recyclers.
A pond is an example of ~~ a natural ecosystem ~~ an artificial ecosystem ~~ a desert ~~ a garden ~~ Not man-made.

A series of organisms through which food energy passes is a ~~ food chain ~~ food web ~~ pyramid ~~ habitat ~~ Linear.
In the food chain, plants are eaten by ~~ herbivores ~~ carnivores ~~ decomposers ~~ the Sun ~~ Primary consumers.
Which of the following is a primary consumer? ~~ Rabbit ~~ Tiger ~~ Snake ~~ Hawk ~~ A herbivore.
The source of energy for a food chain is the ~~ Sun ~~ Moon ~~ stars ~~ wind ~~ Producers use it.
A food chain starts with a ~~ producer ~~ consumer ~~ decomposer ~~ carnivore ~~ Plants.
Interconnected food chains form a ~~ food web ~~ food line ~~ ladder ~~ cycle ~~ Network.
The percentage of energy transferred to the next trophic level is ~~ 10% ~~ 50% ~~ 90% ~~ 100% ~~ 10 per cent law.
The producers in the ocean food chains are ~~ phytoplankton ~~ whales ~~ fish ~~ crabs ~~ They carry out photosynthesis.
The second trophic level consists of ~~ herbivores ~~ producers ~~ carnivores ~~ decomposers ~~ Primary consumers.
In which of the following does energy flow only one way? ~~ A food chain ~~ Water cycle ~~ Nitrogen cycle ~~ Carbon cycle ~~ Unidirectional.

The ozone layer protects us from ~~ ultraviolet rays ~~ infrared rays ~~ radio waves ~~ sound ~~ UV.
Ozone is formed of ~~ three atoms of oxygen ~~ two atoms of oxygen ~~ one atom of oxygen ~~ nitrogen ~~ O3.
Which gas harms the ozone layer? ~~ CFCs ~~ Oxygen ~~ Nitrogen ~~ Helium ~~ Chlorofluorocarbons.
Plastic bags are ~~ non-biodegradable ~~ biodegradable ~~ edible ~~ living ~~ They stay for years.
Which of the following is biodegradable? ~~ Leaves ~~ Polythene ~~ Glass ~~ Iron ~~ Microbes act on them.
Which of the following is non-biodegradable? ~~ DDT ~~ Banana peel ~~ Paper ~~ Cotton ~~ A persistent pesticide.
The 3 R's of waste management are ~~ reduce, reuse, recycle ~~ run, rest, relax ~~ read, write, remember ~~ rent, refill, repair ~~ Environment friendly.
Waste from kitchens can be changed into manure by ~~ composting ~~ burning ~~ burying plastic ~~ dumping ~~ Decomposition.
Dustbins with two colours are used to ~~ separate biodegradable and non-biodegradable waste ~~ decorate roads ~~ store water ~~ hold toys ~~ Segregation.
The harmful chemicals in the food chain are highest in ~~ top consumers ~~ producers ~~ herbivores ~~ soil ~~ Biomagnification.
""".strip()
eB = """
What is an ecosystem? ~~ Living and non-living components interacting with each other|2
Name two abiotic factors. ~~ Temperature|1 ~~ Rainfall, soil or light|1
Define a producer. ~~ An organism that makes its own food|1 ~~ By photosynthesis|1
What is a consumer? Give two examples. ~~ An organism that depends on others for food|1 ~~ Cow, lion|1
Name any two decomposers. ~~ Bacteria|1 ~~ Fungi|1
What is a trophic level? ~~ A step in a food chain|2
Write one food chain involving three organisms. ~~ Grass, deer, tiger|2
State the 10 per cent law. ~~ Only 10% of energy passes to the next trophic level|2
What is the full form of CFC? ~~ Chlorofluorocarbons|2
Name the layer of the atmosphere that has ozone. ~~ Stratosphere|2
What is a biodegradable substance? ~~ Substance broken down by living organisms like bacteria|2
What is biomagnification? ~~ Increase of harmful chemicals along the food chain|2
""".strip()
eC = """
Give three examples each of natural and artificial ecosystems. ~~ Natural: forest, pond, lake|1 ~~ Artificial: aquarium, garden, crop field|1 ~~ Natural ecosystems are not made by humans|1
Classify the following into producers, consumers and decomposers: mushroom, grass, deer, bacteria, tiger. ~~ Producers: grass|1 ~~ Consumers: deer, tiger|1 ~~ Decomposers: mushroom, bacteria|1
What are herbivores, carnivores and omnivores? Give one example of each. ~~ Herbivore: eats plants (goat)|1 ~~ Carnivore: eats flesh (lion)|1 ~~ Omnivore: eats both (humans)|1
What is the source of energy in an ecosystem? How is it passed to the next level? ~~ The Sun|1 ~~ Producers capture sunlight|1 ~~ Consumers eat producers and get energy|1
Write a food chain of four organisms and name the trophic levels. ~~ Plant, insect, frog, snake|1 ~~ T1 producer, T2 primary consumer|1 ~~ T3 secondary consumer, T4 tertiary consumer|1
What is the importance of decomposers in the environment? ~~ Break down dead organisms|1 ~~ Return nutrients to the soil|1 ~~ Keep the environment clean|1
Calculate the energy available at the second trophic level if producers have 5000 J. ~~ 10% passes on|1 ~~ 10 per cent of 5000|1 ~~ 500 J|1
Calculate the energy available at the third trophic level if producers have 1000 J. ~~ Second level: 100 J|1 ~~ Third level: 10% of 100|1 ~~ 10 J|1
Differentiate between a food chain and a food web. ~~ A chain is a single path|1 ~~ A web has many paths|1 ~~ A web is more stable|1
Why does energy decrease as we go up in a food chain? ~~ Energy is used for life processes|1 ~~ Some is lost as heat|1 ~~ Only 10% passes to the next level|1
What are the functions of the ozone layer? ~~ Absorbs UV rays|1 ~~ Protects living organisms|1 ~~ Prevents skin cancer|1
How is the ozone layer damaged? ~~ By CFCs|1 ~~ Used in refrigerators and aerosols|1 ~~ Chlorine destroys ozone|1
Give three examples each of biodegradable and non-biodegradable substances. ~~ Biodegradable: vegetable peels, paper, cotton|1 ~~ Non-biodegradable: plastic, DDT, glass|1 ~~ Microbes act on biodegradable ones|1
What is the harm in using plastic? ~~ It is non-biodegradable|1 ~~ It pollutes soil and water|1 ~~ Animals eat it and may die|1
State three ways in which you can reduce waste. ~~ Reduce use of things|1 ~~ Reuse them|1 ~~ Recycle them|1
Why should we use compost bins? ~~ Vegetable waste is converted into manure|1 ~~ Reduces garbage|1 ~~ Reduces pollution|1
Explain biomagnification in your own words. ~~ Harmful chemicals enter the food chain|1 ~~ They do not break down|1 ~~ Concentration increases at higher levels|1
Why are the number of organisms at higher levels of a food chain fewer? ~~ Less energy is available at higher levels|1 ~~ Few organisms can be supported|1 ~~ Top consumers are very few|1
""".strip()
eD = """
Explain the components of an ecosystem with examples. ~~ Ecosystem: living and non-living parts|1 ~~ Abiotic: air, water, sunlight|1 ~~ Biotic: producers|1 ~~ Biotic: consumers|1 ~~ Biotic: decomposers|1
Describe the roles of producers, consumers and decomposers. ~~ Producers make food|1 ~~ Consumers eat food|1 ~~ Herbivores, carnivores and omnivores|1 ~~ Decomposers break down remains|1 ~~ Nutrients are returned to the soil|1
What is a food chain? Draw a food chain of a grassland and name each trophic level. ~~ Series of organisms feeding on each other|1 ~~ Grass, grasshopper, frog, snake, hawk|1 ~~ Grass: producer|1 ~~ Grasshopper: primary consumer; frog: secondary|1 ~~ Snake and hawk: higher consumers|1
Explain the 10 per cent law with the help of an example. ~~ Only 10% energy is passed on|1 ~~ Producers: 10,000 J|1 ~~ Herbivores: 1000 J|1 ~~ Carnivores: 100 J|1 ~~ Top carnivores: 10 J|1
Why is the flow of energy unidirectional in an ecosystem? ~~ Producers get energy from the Sun|1 ~~ They give it to the herbivores|1 ~~ Herbivores give to carnivores|1 ~~ Energy does not return|1 ~~ It is lost as heat|1
What is the ozone layer? Explain why it is important and what is damaging it. ~~ A layer of ozone gas in the stratosphere|1 ~~ Absorbs UV rays|1 ~~ Protects living beings|1 ~~ Damaged by CFCs|1 ~~ Produces an ozone hole|1
Explain biomagnification with an example. ~~ Harmful pesticide enters the water|1 ~~ Taken by plants|1 ~~ Eaten by herbivores|1 ~~ Eaten by carnivores|1 ~~ Highest concentration at the top level|1
What are biodegradable and non-biodegradable substances? Give examples and effects. ~~ Biodegradable: decomposed by microbes|1 ~~ Examples: food waste, paper|1 ~~ Non-biodegradable: not decomposed|1 ~~ Examples: plastics, DDT|1 ~~ They cause pollution|1
Explain how we can manage the waste at home. ~~ Segregate biodegradable and non-biodegradable waste|1 ~~ Compost the biodegradable waste|1 ~~ Recycle paper and glass|1 ~~ Reduce plastic use|1 ~~ Reuse bags and bottles|1
Describe the effects of ozone depletion and how to reduce it. ~~ More UV reaches the earth|1 ~~ Causes skin cancer|1 ~~ Cataract in eyes|1 ~~ Reduce CFC use|1 ~~ Use eco-friendly refrigerants|1
What is a food web? Draw a simple food web of a pond or a forest in words. ~~ A network of food chains|1 ~~ Algae eaten by tadpoles and small fish|1 ~~ Small fish eaten by large fish|1 ~~ Large fish eaten by birds|1 ~~ Many connections form the web|1
Distinguish between natural and artificial ecosystems with examples. ~~ Natural: not made by humans|1 ~~ Artificial: man-made|1 ~~ Natural: forest, pond|1 ~~ Artificial: aquarium, garden|1 ~~ Artificial needs maintenance|1
""".strip()

# ============================ MEDIUM ============================
mA = """
In the food chain Phytoplankton, Zooplankton, Small fish, Large fish the secondary consumer is ~~ small fish ~~ zooplankton ~~ large fish ~~ phytoplankton ~~ Zooplankton are primary consumers.
Which of the following is the correct food chain? ~~ Plant, caterpillar, bird, hawk ~~ Hawk, bird, caterpillar, plant ~~ Bird, plant, hawk ~~ Plant, hawk, bird ~~ Order of feeding.
If the producers of a food chain have 50,000 J of energy, the tertiary consumers receive ~~ 50 J ~~ 500 J ~~ 5000 J ~~ 5 J ~~ Three transfers of 10%.
If a top carnivore receives 10 J of energy through 3 transfers from producers, the energy at the producers is ~~ 10,000 J ~~ 1000 J ~~ 100 J ~~ 100,000 J ~~ 10 x 1000.
Which of these organisms is at the lowest trophic level? ~~ Grass ~~ Grasshopper ~~ Frog ~~ Snake ~~ Producers form the first trophic level.
In an ecosystem, the decomposers ~~ recycle nutrients ~~ make food ~~ eat producers ~~ are not needed ~~ They return materials to the soil.
Which of these maintain the balance in an ecosystem? ~~ All organisms ~~ Only plants ~~ Only animals ~~ Only decomposers ~~ Interdependence.
Removal of snakes from a grassland food chain will ~~ increase the frog population ~~ decrease the frogs ~~ not affect any organism ~~ remove grass ~~ Predators control populations.
In a food web, the same organism can occupy ~~ more than one trophic level ~~ only one level ~~ no level ~~ decomposer level only ~~ E.g. an omnivore.
The trophic level occupied by humans eating rice is ~~ second ~~ first ~~ third ~~ fourth ~~ Herbivore position.

In a food chain, DDT concentration is highest in ~~ eagle ~~ phytoplankton ~~ zooplankton ~~ small fish ~~ Top consumer.
Which of the following would show the greatest biomagnification? ~~ A hawk that eats snakes ~~ Grass ~~ A grasshopper ~~ A snail ~~ Higher level.
Which one is a harmful effect of CFCs? ~~ Destroying the ozone layer ~~ Increasing oxygen ~~ Cooling the sun ~~ Making plants grow ~~ Chlorine destroys ozone.
The ozone layer absorbs ~~ UV rays of the sun ~~ visible light ~~ infrared rays ~~ X-rays only ~~ Protects from skin cancer.
The ozone hole was first reported over ~~ Antarctica ~~ the Sahara ~~ India ~~ the Pacific Ocean ~~ In 1985.
The ozone is O3 and the oxygen we breathe is ~~ O2 ~~ O ~~ O4 ~~ O3 ~~ The diatomic form.
International agreement to restrict CFCs was done under ~~ UNEP ~~ WHO ~~ UNICEF ~~ FIFA ~~ In 1987.
Excessive use of fertilisers and pesticides leads to ~~ pollution and biomagnification ~~ better ecosystem ~~ more decomposers ~~ no effect ~~ Harmful.
Chemicals that cannot be broken by microorganisms are ~~ non-biodegradable ~~ biodegradable ~~ natural ~~ organic ~~ Accumulate.
A rise in pesticide in a lake water makes fish unfit to eat due to ~~ biomagnification ~~ photosynthesis ~~ respiration ~~ digestion ~~ Accumulation.

Segregation of waste means ~~ separating biodegradable from non-biodegradable ~~ burning ~~ burying ~~ dumping in sea ~~ For proper treatment.
A sewage treatment plant converts waste into ~~ manure and clean water ~~ plastic ~~ fuel only ~~ glass ~~ Waste management.
Composting is the process of ~~ converting vegetable waste into manure ~~ burning plastic ~~ recycling glass ~~ melting metals ~~ Natural decomposition.
Which of the following should be put in a green dustbin? ~~ Vegetable peels ~~ Plastic bottles ~~ Glass pieces ~~ Metal cans ~~ Biodegradable waste.
Recycling paper helps to ~~ save trees ~~ pollute air ~~ produce plastic ~~ increase waste ~~ Conserves resources.
Which of these is an eco-friendly practice? ~~ Using cloth bags ~~ Using plastic bags ~~ Burning waste ~~ Dumping into rivers ~~ Reduces plastic.
Discarded polythene in a field makes the soil ~~ infertile ~~ fertile ~~ rich in humus ~~ more porous ~~ It stays unchanged.
Burning of plastic releases ~~ toxic gases ~~ oxygen ~~ nitrogen ~~ helium ~~ Pollutes air.
Which of the following is not a biodegradable material? ~~ Aluminium foil ~~ Fruit peel ~~ Jute rope ~~ Wooden stick ~~ It does not decay easily.
To reduce the harm of waste, the first step is to ~~ reduce its production ~~ burn it ~~ bury it ~~ flush it ~~ Reduce at source.
""".strip()
mB = """
A food chain has the organisms: grass, frog, grasshopper, snake. Arrange them in the correct order and identify the tertiary consumer. ~~ Grass, grasshopper, frog, snake|1 ~~ Tertiary consumer: snake|1
If a lake has producers with 20,000 J, find the energy available to the primary and the secondary consumer. ~~ Primary consumer: 2000 J|1 ~~ Secondary consumer: 200 J|1
Why do the top carnivores have the least biomass? ~~ Energy available is very low at the top level|1 ~~ Only a small population can be supported|1
Why are the decomposers called the cleaners of the ecosystem? ~~ They decompose dead organisms and wastes|1 ~~ They return minerals to the soil|1
How can a food web be more stable than a food chain? ~~ Alternate food sources exist|1 ~~ Loss of one species does not break the system|1
Name the harmful radiation absorbed by ozone and one harmful effect on humans. ~~ Ultraviolet radiation|1 ~~ Skin cancer|1
How do the CFCs reach the stratosphere? ~~ They are stable gases that rise|1 ~~ They are broken by UV to release chlorine|1
Why is it a better practice to use cloth or jute bags instead of plastic bags? ~~ They are biodegradable|1 ~~ Reduce pollution|1
Why is DDT concentration in humans higher than in plants? ~~ DDT is non-degradable|1 ~~ Biomagnification along the food chain|1
Why does the amount of energy decrease from producers to top carnivores? ~~ Lost in respiration and as heat|1 ~~ Only 10% is passed on|1
What is the difference between a grazing food chain and decomposer chain? ~~ Grazing chain starts with green plants|1 ~~ The decomposer chain starts with dead matter|1
Why is the use of fertilisers and pesticides in excess dangerous? ~~ They pollute soil and water|1 ~~ They enter the food chain and get biomagnified|1
""".strip()
mC = """
In a food chain, Grass, Deer, Tiger, find the energy available to the deer and to the tiger if grass has 12,000 J. State the law used. ~~ 10 per cent law|1 ~~ Deer: 1200 J|1 ~~ Tiger: 120 J|1
Why do we get less energy by eating meat than by eating plants? ~~ Meat is at a higher trophic level|1 ~~ Energy is lost at each level|1 ~~ Plants are at the first level with more energy|1
Why is it more efficient for humans to be vegetarian from the standpoint of energy? ~~ Plant foods are at the first level|1 ~~ Less energy lost from fewer transfers|1 ~~ More people can be fed from the same land|1
Explain what happens if all the producers of an ecosystem are removed. ~~ No food is made|1 ~~ Consumers starve|1 ~~ The whole ecosystem collapses|1
How does the removal of a herbivore like a deer affect the grass and the tiger? ~~ Grass grows in excess|1 ~~ The tiger loses its prey and its numbers fall|1 ~~ The balance of the ecosystem is disturbed|1
State the causes and effects of ozone layer depletion in brief. ~~ Cause: CFCs|1 ~~ More UV rays reach the earth|1 ~~ Effects: skin cancer, cataract and crop damage|1
A farmer sprays pesticide on a crop. Describe how it reaches the top consumers. ~~ Pesticide gets into crops and water|1 ~~ Eaten by herbivores and accumulates|1 ~~ Carnivores accumulate more through biomagnification|1
Why are the plastics a great threat to the environment although they are used widely? ~~ Non-biodegradable|1 ~~ They block drains, harm animals|1 ~~ Burning them releases toxic gases|1
Explain the process of composting and its benefits. ~~ Biodegradable waste is decomposed by microbes|1 ~~ Forms manure|1 ~~ Reduces waste and improves the soil|1
Explain how recycling helps to conserve resources and reduce pollution. ~~ Waste is converted into new products|1 ~~ Saves raw materials|1 ~~ Reduces the amount of garbage|1
What is the role of a food web in the stability of an ecosystem? ~~ Provides alternate food sources|1 ~~ Organisms can shift diets|1 ~~ The system is balanced|1
Differentiate between producers and consumers on the basis of mode of nutrition and energy source. ~~ Producers: autotrophic|1 ~~ Consumers: heterotrophic|1 ~~ Producers use solar energy; consumers use food|1
Why is there no use of 'dead end' in a food chain of an ecosystem which has decomposers? ~~ Decomposers act on dead matter at each level|1 ~~ Nutrients return to the producers|1 ~~ Materials are recycled|1
Explain why the number of trophic levels is limited to four or five. ~~ Energy falls by 90% at each step|1 ~~ Very little energy is left at the fifth level|1 ~~ Not enough to support another level|1
Why is the use of CFC-based aerosols banned in many countries? ~~ CFCs release chlorine in the stratosphere|1 ~~ Chlorine destroys ozone|1 ~~ Ozone depletion harms life|1
Explain the importance of segregating waste into two separate dustbins. ~~ Biodegradable waste can be composted|1 ~~ Non-biodegradable waste can be recycled|1 ~~ It reduces pollution|1
In a pond, a bird eats fish which eat zooplankton. Identify the trophic levels. ~~ Phytoplankton: producer|1 ~~ Zooplankton: primary consumer; fish: secondary consumer|1 ~~ Bird: tertiary consumer|1
How do the activities of humans harm the environment? Give three examples. ~~ Using CFCs|1 ~~ Excess use of plastics|1 ~~ Use of pesticides and improper waste disposal|1
""".strip()
mD = """
Construct a food chain of a pond with five organisms and calculate the energy available at each level if the producers have 100,000 J. Which level has the least energy? ~~ Phytoplankton, zooplankton, small fish, large fish, fish-eating bird|1 ~~ T1: 100,000 J|1 ~~ T2: 10,000 J; T3: 1000 J|1 ~~ T4: 100 J; T5: 10 J|1 ~~ The top level (T5) has the least energy|1
Explain why the number of individuals decreases at each successive trophic level and why the energy transfer is only 10 per cent. ~~ Energy is lost at each level|1 ~~ Used in respiration, movement and body activity|1 ~~ Lost as heat|1 ~~ Only 10% stored in the body|1 ~~ So fewer organisms are supported at higher levels|1
Describe biomagnification with an example of DDT in a lake ecosystem. Why are humans most affected? ~~ DDT enters the lake from run-off|1 ~~ Taken by the plankton|1 ~~ Concentrated in fish|1 ~~ More concentrated in the fish-eating birds|1 ~~ Humans at the top get the highest dose|1
What is ozone? Describe how it is formed and how it is destroyed. Explain the effects of its depletion and the steps taken to protect it. ~~ Ozone is O3, found in the stratosphere|1 ~~ UV splits O2 into atoms which combine with O2 to form O3|1 ~~ CFCs release chlorine that breaks ozone|1 ~~ More UV reaches the earth causing skin cancer|1 ~~ UNEP framework to freeze CFC production in 1987|1
Draw a grassland food web (in words) with at least five organisms and explain how it provides stability. ~~ Grass eaten by grasshopper and rabbit|1 ~~ Grasshopper eaten by frog and bird|1 ~~ Rabbit eaten by snake and hawk|1 ~~ Frog eaten by snake; snake by hawk|1 ~~ If one species is lost, others sustain the web|1
What are the problems caused by non-biodegradable waste? Explain with plastics, DDT and glass, and suggest a plan for a school to reduce waste. ~~ Non-biodegradable materials remain for years|1 ~~ Plastics clog drains and harm animals|1 ~~ DDT biomagnifies|1 ~~ Plan: separate dustbins, compost pit, no plastic|1 ~~ Reuse paper; recycle bottles|1
Explain the flow of energy in an ecosystem. Why can the energy not be recycled? ~~ Sun gives energy to producers|1 ~~ Producers convert it into chemical energy|1 ~~ Passed on to consumers|1 ~~ Energy lost as heat at each step|1 ~~ Heat energy cannot be used by organisms, so it is not recycled|1
Explain the roles of producers, herbivores, carnivores and decomposers in the ecosystem and how the removal of any one of them can affect the others. ~~ Producers: base of the food chain|1 ~~ Herbivores: link producers to carnivores|1 ~~ Carnivores: control herbivore numbers|1 ~~ Decomposers: recycle nutrients|1 ~~ Removal of one disturbs the balance of all|1
A farmer uses pesticides to protect crops. Evaluate the advantages, disadvantages and alternatives, with reference to biomagnification and soil health. ~~ Advantage: protects crops|1 ~~ Disadvantage: harms useful organisms|1 ~~ Non-degradable pesticides undergo biomagnification|1 ~~ Pollutes water and soil|1 ~~ Alternatives: organic farming, biological control, crop rotation|1
Discuss how the choices of a consumer (cloth bags, reusable bottles, compost, recycled paper, CFC-free refrigerators) can protect the environment. ~~ Cloth bags reduce plastic|1 ~~ Reusable bottles reduce waste|1 ~~ Compost converts kitchen waste into manure|1 ~~ Recycled paper saves trees|1 ~~ CFC-free refrigerators protect the ozone layer|1
Compare natural and artificial ecosystems with respect to energy source, human dependence, biodiversity and stability. Give two examples of each. ~~ Natural: self-sustaining, e.g. forest, pond|1 ~~ Artificial: needs human care, e.g. crop field, aquarium|1 ~~ Natural has high biodiversity|1 ~~ Artificial has low biodiversity|1 ~~ Energy source is the Sun in both|1
Using an example, explain the idea that 'every organism in an ecosystem is important'. ~~ In a grassland chain, removal of snakes increases frogs|1 ~~ More frogs reduce insects|1 ~~ Insects increase and damage grass|1 ~~ The balance is disturbed|1 ~~ So every organism has a role|1
""".strip()

# ============================ HARD ============================
hA = """
AR ~~ The number of trophic levels in a food chain is limited. ~~ About 90 per cent of energy is lost at each trophic level. ~~ a ~~ The energy left is too little to support further levels.
AR ~~ Decomposers are called the cleaners of the environment. ~~ They break down dead organisms into simple substances. ~~ a ~~ Decomposition recycles nutrients.
AR ~~ Energy flow in an ecosystem is cyclic. ~~ Energy is lost as heat at every trophic level and cannot be reused by the organisms. ~~ d ~~ A is false: energy flows in one direction; R is true.
AR ~~ Top carnivores contain the highest concentration of pesticides. ~~ Pesticides are non-degradable and accumulate along the food chain. ~~ a ~~ Biomagnification.
AR ~~ The ozone layer protects life on the earth. ~~ It absorbs the harmful ultraviolet radiation of the Sun. ~~ a ~~ UV absorption is the reason.
AR ~~ CFCs are widely used as refrigerants. ~~ CFCs are the main reason for the depletion of ozone. ~~ b ~~ Both true; R is not an explanation of A.
AR ~~ Plastic is a biodegradable material. ~~ Plastics are non-biodegradable and persist in the environment. ~~ d ~~ A is false; R is true.
AR ~~ Green plants are producers. ~~ They convert solar energy into chemical energy. ~~ a ~~ Photosynthesis.
AR ~~ A food web is more stable than a food chain. ~~ In a food web many alternative paths are available for the flow of energy. ~~ a ~~ Alternative paths.
AR ~~ Herbivores have less energy than producers. ~~ Only 10 per cent of the energy is transferred from producers to herbivores. ~~ a ~~ 10 per cent law.

A food chain has four trophic levels. If the energy at the fourth level is 5 J, the energy at the first level is ~~ 5000 J ~~ 500 J ~~ 50 J ~~ 50,000 J ~~ 5 x 10 x 10 x 10.
If the energy available at the producer level is 4000 kJ, the energy transferred to the third trophic level is ~~ 40 kJ ~~ 400 kJ ~~ 4 kJ ~~ 4000 kJ ~~ Two transfers.
In a food chain: plants, insects, frogs, snakes, eagles, the primary and the quaternary consumers are ~~ insects and eagles ~~ frogs and snakes ~~ plants and insects ~~ snakes and eagles ~~ Insects (T2) and eagle (T5).
In which of the following food chains is the energy available to the final consumer the greatest? ~~ Grass, goat, human ~~ Grass, insect, bird, snake ~~ Plankton, fish, bird ~~ Grass, grasshopper, frog, snake, eagle ~~ Fewer levels lose less energy.
If the population of herbivores in a grassland dropped sharply, the immediate effects are ~~ grass increases and carnivores decrease ~~ grass decreases and carnivores increase ~~ both decrease ~~ both increase ~~ Fewer plant-eaters and less prey.
A top carnivore receives 1 J of energy. The energy of the producers in a four-level food chain would be about ~~ 1000 J ~~ 100 J ~~ 10 J ~~ 10,000 J ~~ Three transfers.
Which of the following would lead to a disturbance in the pond ecosystem? ~~ Dumping of pesticide-laced waste ~~ Rain ~~ Sunlight ~~ Growth of algae in balance ~~ Pollution.
A pond contains DDT at 0.003 ppm in water, 0.04 ppm in plankton, 2 ppm in fish and 25 ppm in fish-eating birds. This shows ~~ biomagnification ~~ photosynthesis ~~ decomposition ~~ eutrophication ~~ Concentration increases up the chain.
Which statement about decomposers is correct? ~~ They can act at every trophic level on dead matter ~~ They are at only the last level ~~ They are producers ~~ They are consumers of living plants ~~ They break down remains from every level.
Which of the following lists organisms in decreasing order of the energy available to them? ~~ Producers, herbivores, carnivores ~~ Carnivores, herbivores, producers ~~ Herbivores, producers, carnivores ~~ Producers, carnivores, herbivores ~~ Energy decreases at each higher trophic level.

Ozone in the stratosphere is formed by the action of ~~ UV radiation on oxygen ~~ visible light on nitrogen ~~ CFCs on oxygen ~~ infrared on ozone ~~ O2 splits and recombines.
A student claims that eating at a lower trophic level gives more energy. This is because ~~ lower levels have more energy ~~ food at lower levels is tastier ~~ plants are free ~~ the Sun is nearer ~~ Less loss in the chain.
Which of the following does NOT contribute to biomagnification? ~~ Biodegradable waste ~~ DDT ~~ Mercury ~~ Non-degradable pesticides ~~ It is easily decomposed.
CFC-free refrigerators were developed to ~~ protect the ozone layer ~~ save electricity only ~~ add more cooling ~~ increase noise ~~ Chlorine is avoided.
Which of the following is the best way to dispose of kitchen waste? ~~ Composting ~~ Burning ~~ Dumping in drains ~~ Throwing in a river ~~ Gives manure.
An environmentally sound action is ~~ using paper bags and reusing bottles ~~ burning polythene ~~ dumping waste in drains ~~ using aerosols ~~ Protects environment.
If the herbivores are removed from a food chain, the secondary consumers ~~ lose their food source ~~ increase in number ~~ are not affected ~~ become producers ~~ Dependent on the primary consumers.
A heavy rainfall washes pesticides from a farm into a pond. Within a food chain in the pond, the organism with the highest concentration is ~~ a fish-eating bird ~~ phytoplankton ~~ zooplankton ~~ small fish ~~ Top.
The reason that non-biodegradable substances are harmful is that they ~~ persist and accumulate ~~ decompose too quickly ~~ release oxygen ~~ increase soil fertility ~~ Remain in the environment.
Which of these best describes an artificial ecosystem? ~~ Crop field maintained by farmers ~~ A tropical rainforest ~~ A coral reef ~~ A natural lake ~~ Man-made and managed.
""".strip()
hB = """
In a food chain, grass, grasshopper, frog and snake, the energy in the frog is 50 J. Find the energy in the grass and in the snake. ~~ Grass = 50 x 100 = 5000 J|1 ~~ Snake = 5 J|1
If the grass in a field has 8000 J of energy, find the energy in the tertiary consumer in the chain grass, rabbit, fox, wolf. ~~ Fox (T3) 80 J|1 ~~ Wolf (T4) = 8 J|1
Why is it unsafe to feed on the top level of the food chain of a polluted lake? ~~ Pesticides get biomagnified|1 ~~ Top consumers hold the greatest concentration|1
How does the loss of ozone in Antarctica affect marine ecosystems there? ~~ More UV reaches the surface|1 ~~ Harms phytoplankton, the producers, and the food chains|1
Why is it not possible to have a food chain with 10 trophic levels? ~~ Energy decreases to 10^-9 of the original at the 10th level|1 ~~ Too little energy to sustain organisms|1
What is meant by decomposers acting as the 'nature's recyclers'? ~~ They convert dead organisms into simple inorganic substances|1 ~~ These are used again by plants|1
One per cent of the sunlight falling on a field, 1,000,000 J, is captured by plants. Find the energy at the herbivore level (use the 10 per cent law). ~~ Producers: 10,000 J|1 ~~ Herbivores: 1000 J|1
Why does the amount of usable energy decrease at each higher trophic level? ~~ Part is used in life processes like respiration|1 ~~ Part is lost as heat, so only 10% is passed on|1
In what way is a crop field different from a forest with respect to the diversity and the self-sustaining nature? ~~ Crop field has few species and needs inputs|1 ~~ Forest has many species and is self-sustaining|1
Why is the biodegradable waste disposed of better by composting than by burning? ~~ Composting gives manure|1 ~~ Burning pollutes the air|1
Why do we say that pesticides sprayed on crops affect organisms far away? ~~ They run off into water bodies|1 ~~ They enter food chains and biomagnify|1
Give two reasons why it is advisable to use fewer aerosol sprays. ~~ Many contain CFCs that harm ozone|1 ~~ They pollute the air|1
""".strip()
hC = """
In a pond food chain with plankton, small fish, big fish and kingfisher, the concentration of a pesticide in the plankton is 0.02 ppm. If it rises 10 times at each level, find the concentration in the kingfisher. ~~ Small fish: 0.2 ppm|1 ~~ Big fish: 2 ppm|1 ~~ Kingfisher: 20 ppm|1
Explain why a rise in the population of one species may affect many others in a food web. ~~ Food web has several connections|1 ~~ More predators or competitors for food|1 ~~ Chain reaction changes populations|1
A forest has been cleared and replaced by a crop field. Compare the two ecosystems in terms of the number of species, food web and stability. ~~ Forest: many species, complex food web|1 ~~ Crop field: few species, simple chain|1 ~~ Crop field is less stable and needs human inputs|1
Why are decomposers important even though they are not part of the grazing food chain? ~~ They act on dead remains of all levels|1 ~~ They return nutrients to the soil|1 ~~ Producers need these nutrients|1
Give reasons: (a) a food web is stable (b) a pesticide such as DDT is banned (c) the energy of the Sun is needed daily. ~~ (a) Many alternative pathways|1 ~~ (b) It biomagnifies and harms birds and humans|1 ~~ (c) Energy is not recycled and is lost as heat|1
Why does the ozone hole form mainly over polar regions? ~~ Very cold polar clouds help CFC reactions|1 ~~ Chlorine released destroys ozone|1 ~~ Sunlight in spring triggers the reaction|1
Suggest three activities that a school can take up to promote the 3 R's and explain how they help. ~~ Use both sides of paper (reduce)|1 ~~ Reuse bottles and bags|1 ~~ Recycle paper and glass; helps to conserve resources|1
How does the burning of plastic waste affect the ecosystem? ~~ Releases toxic gases|1 ~~ Pollutes the air and harms organisms|1 ~~ Disturbs the food chains|1
If the pesticide DDT is banned today, why will it continue to be found in organisms for some years? ~~ It is non-biodegradable|1 ~~ It persists in soil and water|1 ~~ It remains in food chains|1
Why is the 10 per cent of energy only an average value? ~~ It varies from organism to organism|1 ~~ Depends on the efficiency of use|1 ~~ But generally a small fraction is transferred|1
Explain how an increase in the human population may affect trophic levels. ~~ More demand for food|1 ~~ Plants and animals used excessively|1 ~~ Disturbs the balance and increases waste|1
How can you reduce the use of plastic at home? Mention three steps and the benefit of each. ~~ Use cloth bags: no polythene waste|1 ~~ Use steel or glass bottles: reuse|1 ~~ Buy loose items: less packaging waste|1
Why can the fish in a river downstream of a factory die? ~~ Toxic chemicals in effluents|1 ~~ Reduce oxygen levels|1 ~~ Poisoned food chain|1
In an experiment, a beaker of vegetable waste and a beaker of plastic scraps are buried in soil. After a month what will be found? Explain. ~~ Vegetable waste decays|1 ~~ Plastic remains almost unchanged|1 ~~ Microbes decompose biodegradable matter only|1
What would happen to the grassland food chain if the carnivores were all killed? ~~ Herbivores would increase|1 ~~ Grass would be overgrazed|1 ~~ Eventually herbivores would starve|1
A student claims 'Energy is recycled in an ecosystem'. Give two arguments to correct this. ~~ Energy flows in one direction|1 ~~ It is lost as heat at each step|1 ~~ Materials, not energy, are recycled|1
Why is the removal of green cover from a hill-slope harmful to the ecosystem? ~~ Producers are lost|1 ~~ The food chains that depend on them collapse|1 ~~ Soil is washed away and habitats are lost|1
Explain why dumping untreated sewage into a pond may eventually destroy the pond ecosystem. ~~ Organic waste is decomposed using oxygen|1 ~~ Oxygen level falls|1 ~~ Fish and other organisms die|1
""".strip()
hD = """
In a food chain: Phytoplankton, Zooplankton, Small fish, Large fish, Fish-eating birds, the energy at the producer level is 2,000,000 J. Calculate the energy at each level using the 10 per cent law. At which level are the largest losses in terms of the actual energy? ~~ Zooplankton: 200,000 J|1 ~~ Small fish: 20,000 J|1 ~~ Large fish: 2000 J; birds: 200 J|1 ~~ Energy lost at the first transfer = 1,800,000 J|1 ~~ The first transfer has the largest loss|1
Explain why the biomass of organisms decreases at each higher trophic level in a food chain. Give two consequences for the numbers of top carnivores in a forest. ~~ Energy available decreases by 90% at each step|1 ~~ Less energy can support less biomass|1 ~~ Top carnivores are few in number|1 ~~ They need a large area to find food|1 ~~ They are the most affected by loss of energy at lower levels|1
A lake ecosystem is contaminated with a non-degradable pesticide at 0.01 ppm in water. The concentrations in plankton, small fish, large fish and gulls are 0.1, 1, 10 and 100 ppm. Compute the magnification factor at each step and explain why humans eating large fish are at risk. ~~ Water to plankton: 10 times|1 ~~ Plankton to small fish: 10 times|1 ~~ Small fish to large fish: 10 times|1 ~~ Large fish to gulls: 10 times|1 ~~ Humans at high level accumulate harmful quantity|1
Describe the sequence of events by which CFCs cause ozone depletion, the consequences, and the international measures taken. Also state two actions that individuals can take. ~~ CFCs rise to the stratosphere|1 ~~ UV breaks CFCs and releases chlorine|1 ~~ Chlorine breaks down ozone to oxygen|1 ~~ Consequences: skin cancer, cataract, crop damage|1 ~~ Measures: UNEP agreement in 1987; individuals avoid CFC-based goods and aerosols|1
Plan an integrated waste management scheme for a colony of 500 houses covering segregation, composting, recycling and disposal of hazardous waste. Mention the benefits. ~~ Segregation into dry and wet waste|1 ~~ Compost pits for wet waste|1 ~~ Recycling of paper, plastic, glass|1 ~~ Safe disposal of hazardous waste|1 ~~ Benefits: less pollution, manure, resource savings|1
Evaluate the claim: 'If all the carnivores in a forest are killed, the herbivores will flourish forever.' Use the food web idea. ~~ Initially herbivores increase|1 ~~ Plants are overgrazed|1 ~~ Food becomes scarce and herbivores starve|1 ~~ Disease and competition rise|1 ~~ So the claim is false; the balance is vital|1
A farmer notices that crops are attacked by insects, so he uses pesticide. Birds that eat insects start to die. Explain the reason with reference to the food chain and propose two sustainable alternatives. ~~ Pesticide kills insects and remains in their bodies|1 ~~ Birds that eat insects accumulate it|1 ~~ Biomagnification poisons the birds|1 ~~ Alternative: biological control with natural predators|1 ~~ Alternative: crop rotation or organic farming|1
Describe in terms of trophic levels and energy why 1 hectare of land can feed more people if it is used to grow cereals than if it is used to rear cattle. Use numbers with the 10 per cent law. ~~ Cereals: humans at the second level|1 ~~ Cattle: humans at the third level|1 ~~ If plants hold 10,000 J, humans eating cereals get 1000 J|1 ~~ Via cattle: cattle 1000 J, humans 100 J|1 ~~ So cereals feed about 10 times as many|1
Compare the roles of an ecosystem's producers and decomposers in the cycling of materials and flow of energy. Why is an ecosystem impossible without either? ~~ Producers bring in energy and fix carbon|1 ~~ Decomposers recycle nutrients from dead matter|1 ~~ Energy flows one way and materials cycle|1 ~~ Without producers, no energy enters|1 ~~ Without decomposers, nutrients are locked in dead matter|1
Discuss how the following actions affect the environment and the organisms: (a) burning plastic (b) using CFC-based sprays (c) dumping sewage in rivers (d) overuse of pesticides. Give one remedy for each. ~~ (a) Toxic gases; remedy: recycle|1 ~~ (b) Ozone depletion; remedy: CFC-free products|1 ~~ (c) Water pollution, oxygen loss; remedy: sewage treatment|1 ~~ (d) Biomagnification; remedy: organic methods|1 ~~ Every action disturbs food chains|1
Explain how a food chain in a forest and a food chain in a crop field may differ in the number of trophic levels and stability. Show how the removal of one species may affect each. ~~ Forest: complex web with many species|1 ~~ Crop field: simple, few species|1 ~~ Forest recovers by alternate pathways|1 ~~ Crop field is disturbed more strongly|1 ~~ Crop field needs human care|1
A forest ecosystem has trees, deer, rabbits, tigers, snakes, fungi and bacteria. Classify the organisms by role, write two food chains from the list, and explain what would happen if the fungi and bacteria disappeared. ~~ Producers: trees|1 ~~ Consumers: deer, rabbits, tigers, snakes; decomposers: fungi, bacteria|1 ~~ Chains: tree, deer, tiger and tree, rabbit, snake|1 ~~ Without decomposers dead matter and wastes would pile up|1 ~~ Nutrients would not be recycled and the producers would suffer|1
""".strip()

TIERS = {"NCERT": tier(nA, nB, nC, nD), "Easy": tier(eA, eB, eC, eD), "Medium": tier(mA, mB, mC, mD), "Hard": tier(hA, hB, hC, hD)}
