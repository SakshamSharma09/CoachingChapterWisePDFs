"""Class 10 SST Ch 18 Development - extras."""
from common import AR4, Q

AR = [
 AR4(r"Different persons can have different developmental goals.", r"What one person considers development may not be so for another, as they have different life situations and aspirations.", "a",
     r"Because people's situations differ, their goals differ; R explains A."),
 AR4(r"Per capita income is the average income of a country.", r"It is calculated by dividing the total income of the country by its total population.", "a",
     r"Total income divided by total population gives the average income per person, which is exactly what per capita income means; R explains A."),
 AR4(r"Haryana has a higher per capita income than Kerala.", r"Haryana does better than Kerala on every indicator, such as infant mortality rate and literacy.", "c",
     r"A is true. R is false: Kerala does better than Haryana on infant mortality and literacy."),
 AR4(r"Per capita income is a complete measure of development.", r"Income by itself does not show the quality of health, education and other facilities available to people.", "d",
     r"A is false because income does not show everything. R is true."),
 AR4(r"The Human Development Report is published by the United Nations Development Programme.", r"The World Development Report, which classifies countries by income, is brought out by the World Bank.", "b",
     r"Both are true statements about two different reports, but R does not explain A."),
 AR4(r"Development must be sustainable.", r"Non-renewable resources like crude oil will be exhausted if they are used up faster than they can be replaced, and future generations also need them.", "a",
     r"Overuse that harms future generations makes sustainability a necessity; R explains A."),
]

CASE = [
 Q(r"<b>Case study.</b> A village has five families whose monthly incomes are Rs 8,000, Rs 12,000, Rs 10,000, Rs 6,000 and Rs 14,000. Another village also has five families but each family earns Rs 10,000. Villagers of both places think that they are developing, yet the first village has families earning much less than the second village's families. "
   r"(i) Find the average monthly income of the first village. (ii) What is the average of the second village? (iii) Can the averages tell us everything about the villages? (iv) What do the averages hide?",
   r"(i) Total Rs 50,000 divided by 5 = Rs 10,000 (1). (ii) Rs 10,000 (1). (iii) No (1). (iv) Averages hide the differences in income between people: the first village has more unequal incomes and some families earn much less than the average, though the averages are equal (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A table shows data for three states. Per capita income (Rs, 2023-24): Haryana 3,25,759; Kerala 2,81,001; Bihar 60,337. Infant mortality rate per 1000 live births: Haryana 28, Kerala 6, Bihar 27. A student concludes that since Haryana has the highest income, it must be the best on all counts. "
   r"(i) Which state has the highest per capita income? (ii) Which state has the lowest infant mortality rate? (iii) Which state has the lowest per capita income? (iv) Why is the student's conclusion not correct?",
   r"(i) Haryana (1). (ii) Kerala (1). (iii) Bihar (1). (iv) Income alone does not show other aspects of development: Kerala has a lower IMR than Haryana despite its lower income, because money cannot buy all goods and services needed to live well; health and education facilities matter too (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A forest group in a hilly area allows only so much firewood and timber to be collected as the trees can regrow. Elsewhere a company drills groundwater excessively for its factory. The groundwater table falls and the neighbouring farmers' wells dry up. The group argues that resources must also be saved for those who will live in the future. "
   r"(i) What is meant by 'sustainable development'? (ii) Is groundwater a renewable resource? (iii) Name any one non-renewable resource. (iv) How does the overuse of groundwater create a problem for development?",
   r"(i) Development that meets present needs without harming the needs of future generations (1). (ii) It is renewable but gets exhausted if used faster than it is replenished (1). (iii) Any one: crude oil, coal, minerals (1). (iv) Falling water levels hurt farmers' output and livelihoods and the environment, so the gains of one group come at the cost of others and of the future (2).", "1+1+1+2"),
]

MISTAKES = [
 r"Defining development only as <b>higher income</b>; the chapter also counts health, education, equal treatment, freedom and sustainability.",
 r"Treating <b>per capita income</b> as showing how income is distributed; it is only the <b>average</b> (total income / total population) and hides inequality.",
 r"Mixing up the organisations: the <b>World Bank</b> classifies countries by income (World Development Report), the <b>UNDP</b> publishes the Human Development Report.",
 r"Assuming that higher income means better health and education: <b>Kerala</b> has a lower per capita income than Haryana but a lower infant mortality rate (6 vs 28).",
 r"Forgetting that for people the goals differ: what is development for <b>a rich person</b> may not be development for <b>a landless labourer</b>, and one person's gain may harm another.",
 r"Writing that sustainable development means no use of resources; it means using them so that <b>future generations</b> are not deprived.",
]
