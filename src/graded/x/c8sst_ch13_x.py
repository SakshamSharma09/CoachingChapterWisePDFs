"""Class 8 SST Ch 13 Dynamics of Population - extras."""
from common import AR4, Q

AR = [
 AR4("If fertility stays below the replacement level for a long time, a population will eventually shrink.", "The replacement level of about 2.1 children per woman is just enough for parents to be replaced.", "a",
     "Fewer births than replacement leads to decline, as R explains."),
 AR4("India's sex ratio in the 2011 census was 943.", "The sex ratio is the number of females per 1,000 males.", "b",
     "Both are true, but R is only a definition and does not explain why the figure was 943."),
 AR4("A population pyramid with a wide base indicates a young population.", "A wide base means that there are very few children.", "c",
     "A is true. R is false: a wide base means many children and a high birth rate."),
 AR4("In Stage 2 of the demographic transition the birth rate falls rapidly while the death rate stays high.", "In Stage 2 the death rate falls while the birth rate stays high.", "d",
     "A is false and R is true."),
 AR4("Education of girls and women's employment tend to lower fertility rates.", "Educated women are more likely to take decisions about family size and marriage.", "a",
     "R gives a reason for the trend."),
 AR4("World population rose rapidly after 1950 mainly because death rates fell.", "China introduced its One-Child Policy in 1979.", "b",
     "Both are true but unrelated."),
]

CASE = [
 Q("<b>Case study.</b> In a year, a town of 5,000 people recorded 150 births and 50 deaths. The town's birth rate is high compared with its death rate, a pattern typical of the second stage of the demographic transition. (i) Calculate the birth rate per 1,000. (ii) Calculate the death rate per 1,000. (iii) At which stage of the transition is this town? (iv) Find the natural increase per 1,000 and give one cause of the falling death rate.",
   "(i) 150/5000 x 1000 = 30 per 1,000 (1). (ii) 50/5000 x 1000 = 10 per 1,000 (1). (iii) Stage 2: death rate falls while birth rate stays high (1). (iv) 30 - 10 = 20 per 1,000 (2 per cent); better medicine and sanitation lowered deaths (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Country A has a population pyramid with a very wide base and a narrow top. Country B has a pyramid that is narrow at the base and wide at the top. Japan is an example of a country like B. (i) What does the pyramid of Country A show? (ii) What does the pyramid of Country B show? (iii) Name one country that resembles B. (iv) Which services should each country plan for?",
   "(i) A young population with a high birth rate (1). (ii) An ageing population (1). (iii) Japan (1). (iv) A needs schools and jobs; B needs health care and pension services (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Sunita left her village in Odisha, where there were few jobs, and moved to Bengaluru, which offered better jobs. She is one of many migrants who shift between places. The census, held every 10 years, helps planners estimate how many homes, schools and hospitals cities need. (i) What is migration? (ii) Name the push factor in the passage. (iii) Name the pull factor in the passage. (iv) Explain how census data is useful for planners.",
   "(i) Moving from one place to another to live, temporarily or permanently (1). (ii) Lack of jobs at home (1). (iii) Better jobs in the city (1). (iv) It gives population size, age and distribution, so services such as schools, housing and health care can be planned (2).", "1+1+1+2"),
]

MISTAKES = [
 "Forgetting that birth rate and death rate are per <b>1,000</b> people per year, and that sex ratio is <b>females per 1,000 males</b> (943 in 2011, not 94.3 or 1.06).",
 "Mixing fertility rate (children per woman, replacement level about 2.1) with birth rate (births per 1,000 population).",
 "Reversing demographic transition stages: Stage 1 both rates high; Stage 2 death rate falls, birth rate high (rapid growth).",
 "Reading a wide-based pyramid as an ageing population; a wide base means young, a wide top means ageing.",
 "Confusing push factors (lack of jobs at home) with pull factors (better jobs in cities).",
 "Saying a large young population automatically gives a demographic dividend; it needs skills and jobs. Population density is per square kilometre, and the census is every 10 years.",
]
