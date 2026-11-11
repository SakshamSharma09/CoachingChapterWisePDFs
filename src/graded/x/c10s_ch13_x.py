"""Class 10 Science Ch 13 Our Environment - extras."""
from common import AR4, Q

AR = [
 AR4(r"Decomposers maintain the nutrient cycle in an ecosystem.", r"They break down dead organic matter into simple inorganic substances that return to the soil.", "a",
     r"The simple substances released are taken up again by the producers."),
 AR4(r"The use of chlorofluorocarbons (CFCs) has damaged the ozone layer.", r"The ozone layer absorbs the harmful ultraviolet radiation from the Sun.", "b",
     r"Both true; R states the function of ozone, which is not the reason CFCs damage it."),
 AR4(r"The number of trophic levels in a food chain is limited to three or four.", r"About 90 percent of the energy is passed on from one trophic level to the next.", "c",
     r"Only about 10 percent of the energy is passed on; the rest is lost, so long chains are not possible. R is false."),
 AR4(r"The ozone layer is formed by the action of infrared radiation on oxygen.", r"Ozone absorbs the harmful ultraviolet radiation of the Sun.", "d",
     r"Ozone is formed when UV radiation splits $\ce{O2}$ into atoms; A is false, R is true."),
 AR4(r"Harmful chemicals have the highest concentration in the top consumers of a food chain.", r"These chemicals are non-biodegradable and accumulate at each successive trophic level.", "a",
     r"This is biomagnification, and R explains it."),
 AR4(r"Biodegradable substances are broken down by microorganisms.", r"Non-biodegradable substances such as plastics persist in the environment for a very long time.", "b",
     r"Both true; the second is a contrast and does not explain the first."),
]

CASE = [
 Q(r"<b>Case study.</b> In a pond ecosystem, phytoplankton are eaten by small fish, small fish are eaten by big fish and big fish are eaten by fish-eating birds. The phytoplankton in the pond capture 10,000 J of solar energy. "
   r"(i) Name the producer in this food chain. (ii) At which trophic level is the big fish? (iii) How much energy is available to the big fish? (iv) How much energy is available to the bird and why are food chains usually short?",
   r"(i) Phytoplankton (1). (ii) Third trophic level (secondary consumer) (1). (iii) 10% of 10,000 J is 1000 J (small fish), and 10% of this is 100 J (big fish) (1). (iv) 10 J (1); only about 10% of energy passes to the next level, the rest is lost as heat, so very little energy is left for further levels (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In a farming village in Punjab, farmers sprayed the pesticide DDT on crops. Later, tests showed a small amount of DDT in the grains and in the bodies of insects that fed on them, a higher amount in the frogs that ate those insects and the highest amount in the snakes and the birds of prey that ate the frogs. "
   r"(i) Name the phenomenon of increasing concentration of harmful chemicals at higher trophic levels. (ii) Which organisms have the highest concentration? (iii) Why do these chemicals accumulate? (iv) Suggest two measures to reduce this problem.",
   r"(i) Biomagnification (1). (ii) Top consumers such as snakes and birds of prey (and humans, if they eat the grains and animals) (1). (iii) They are non-biodegradable and are not broken down or excreted, so they accumulate in the body (1). (iv) Organic farming, biological pest control, using less or safer pesticides, washing vegetables (any two) (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Scientists observed in 1980s that the amount of ozone in the upper atmosphere over Antarctica fell sharply, creating a hole. Chlorofluorocarbons (CFCs) used in refrigerators and aerosol sprays were identified as the cause. In 1987 the United Nations Environment Programme (UNEP) succeeded in forging an agreement to freeze CFC production. "
   r"(i) Write the molecular formula of ozone. (ii) How is ozone formed in the upper atmosphere? (iii) What is the function of the ozone layer? (iv) State two harmful effects of ozone depletion on human beings.",
   r"(i) $\ce{O3}$ (1). (ii) UV radiation splits $\ce{O2}$ into free atoms, which combine with $\ce{O2}$ to form ozone: $\ce{O2 -> O + O}$; $\ce{O + O2 -> O3}$ (1). (iii) It absorbs the harmful ultraviolet radiation of the Sun (1). (iv) Skin cancer, cataract (damage to eyes), weakening of the immune system (any two) (1+1).", "1+1+1+2"),
]

FORMULAS = [
 ("Ecosystem", [r"Ecosystem = biotic (producers, consumers, decomposers) + abiotic (light, temperature, water, soil) components. Natural (forest, pond) or artificial (garden, crop field, aquarium).",
   r"Producers: green plants and some bacteria (autotrophs). Consumers: herbivores, carnivores, omnivores, parasites. Decomposers: bacteria and fungi (natural cleaners)."]),
 ("Food chain, web and energy flow", [r"Food chain: grass $\rightarrow$ grasshopper $\rightarrow$ frog $\rightarrow$ snake $\rightarrow$ hawk (arrows point towards the eater). Trophic levels: producer (T1), primary consumer (T2), secondary (T3), tertiary (T4).",
   r"Food web: many interlinked food chains. Energy flow is unidirectional (Sun $\rightarrow$ producers $\rightarrow$ consumers).",
   r"10 per cent law: only about 10% of energy passes to the next trophic level; so energy at level $n$ is $E_n = E_1\times(0.1)^{n-1}$ and food chains have 3 to 4 trophic levels.",
   r"Example: producer 10,000 J $\rightarrow$ primary 1000 J $\rightarrow$ secondary 100 J $\rightarrow$ tertiary 10 J."]),
 ("Human activities and the ozone layer", [r"Ozone formation: $\ce{O2 ->[UV] O + O}$; $\ce{O + O2 -> O3}$. Ozone shields the Earth from UV radiation.",
   r"CFCs (refrigerators, aerosols, fire extinguishers) deplete ozone; UNEP agreement in 1987 froze CFC production. Effects: skin cancer, cataract."]),
 ("Waste", [r"Biodegradable (broken down by microorganisms): vegetable peels, paper, cotton, dung. Non-biodegradable: plastics, glass, metals, DDT.",
   r"Biomagnification: non-biodegradable chemicals (pesticides) accumulate and increase along the food chain; highest in top consumers.",
   r"Waste management: segregation (green and blue bins), reduce-reuse-recycle, composting, landfills."]),
]

MISTAKES = [
 r"Drawing arrows in a food chain from the eater to the food; the arrow points from the organism that is eaten to the one that eats it.",
 r"Writing that 90% of the energy passes on to the next level; only 10% is transferred and 90% is lost, so energy flows in one direction and does not cycle.",
 r"Counting decomposers as a trophic level of the food chain, or calling the Sun a producer; green plants are producers, the Sun is the source of energy.",
 r"Confusing ozone ($\ce{O3}$) with oxygen ($\ce{O2}$), and writing that $\ce{CO2}$ (instead of CFCs) is the main cause of ozone depletion.",
 r"Saying that all waste is non-biodegradable or that plastics decompose quickly; plastics, glass and DDT are non-biodegradable.",
 r"Explaining biomagnification as increase of pesticide in producers only; the concentration is highest in the <b>top</b> consumers.",
]
