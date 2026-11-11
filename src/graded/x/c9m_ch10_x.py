"""Class 9 Maths Ch 10 How Quantities Combine (Understanding Data) - extras."""
from common import AR4, Q

AR = [
 AR4(r"Class A has 20 students with average 60 marks and Class B has 30 students with average 70 marks; the combined average is 66.", r"The combined average equals the total of all marks divided by the total number of students.", "a",
     r"$\dfrac{20\times60+30\times70}{50}=\dfrac{3300}{50}=66$, using R."),
 AR4(r"The combined average of two groups is always the simple mean of the two group averages.", r"The combined average is the total of all the values divided by the total number of values.", "d",
     r"A is false when the groups have different sizes (the weights differ); R is true."),
 AR4(r"The combined average of two groups lies between the smaller and the larger group average.", r"If two groups are of the same size, the combined average is the simple mean of the two group averages.", "b",
     r"Both are true; R is a special case and does not explain why the combined average lies between the two averages."),
 AR4(r"Mixing 200 mL of a 10% solution with 300 mL of a 20% solution gives a 16% solution.", r"The concentration of a mixture is the simple mean of the two concentrations, $\dfrac{10+20}{2}=15\%$.", "c",
     r"Pure amount $=20+60=80$ mL in 500 mL, i.e. 16%, so A is true; R is false because the volumes differ."),
 AR4(r"In a 100% stacked bar chart every bar has the same total length.", r"In a 100% stacked bar chart each bar shows the shares of its parts as percentages, which add up to 100%.", "a",
     r"Every bar represents 100%, so all bars have equal length."),
 AR4(r"If 2 kg of tea costing Rs 300 per kg is mixed with 3 kg of tea costing Rs 400 per kg, the mixture costs Rs 360 per kg.", r"The cost per kg of the mixture is the total cost divided by the total mass.", "a",
     r"$\dfrac{600+1200}{5}=360$, using R."),
]

CASE = [
 Q(r"<b>Case study.</b> In an annual test, Section A of Class 9 has 40 students with an average of 72 marks and Section B has 60 students with an average of 82 marks. "
   r"(i) Find the total marks of Section A. (ii) Find the total marks of Section B. (iii) Find the combined average of the two sections. (iv) A new Section C of 50 students with average 90 is added. Find the new combined average of the three sections.",
   r"(i) $40\times72=2880$ (1). (ii) $60\times82=4920$ (1). (iii) $\dfrac{2880+4920}{100}=78$ (1). (iv) Section C total $=50\times90=4500$ (1); new average $=\dfrac{7800+4500}{150}=\dfrac{12300}{150}=82$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A juice vendor in Mumbai mixes 4 litres of orange squash containing 30% pure juice with 6 litres of squash containing 20% pure juice. "
   r"(i) Find the pure juice in the first squash. (ii) Find the pure juice in the second squash. (iii) Find the concentration of the mixture. (iv) How much water must be added to the mixture to make it a 20% solution?",
   r"(i) $30\%$ of 4 L $=1.2$ L (1). (ii) $20\%$ of 6 L $=1.2$ L (1). (iii) Pure juice $=2.4$ L in 10 L, so $24\%$ (1). (iv) Let the total volume be $V$: $0.2V=2.4\Rightarrow V=12$ L (1); water to add $=12-10=2$ L (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Anil's final score in a course is a weighted average. His Test score is 85 with weight 2, his Project score is 95 with weight 3 and his Exam score is 75 with weight 5. "
   r"(i) Find the sum of the weights. (ii) Find the sum of weight $\times$ score. (iii) Find Anil's weighted average. (iv) Find the simple mean of the three scores and explain why the weighted average is lower.",
   r"(i) $2+3+5=10$ (1). (ii) $170+285+375=830$ (1). (iii) $\dfrac{830}{10}=83$ (1). (iv) Simple mean $=\dfrac{85+95+75}{3}=85$ (1); the Exam has the greatest weight and his lowest score, so the weighted average is pulled below the simple mean (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Averages", [r"Average $=\dfrac{\text{sum of values}}{\text{number of values}}$; sum $=$ average $\times$ number of values.",
   r"Combined average of two groups: $\dfrac{n_1a_1+n_2a_2}{n_1+n_2}$ (not $\dfrac{a_1+a_2}2$ unless $n_1=n_2$).",
   r"The combined average always lies between the two group averages, nearer the average of the larger group."]),
 ("Weighted average", [r"Weighted average $=\dfrac{w_1x_1+w_2x_2+\cdots}{w_1+w_2+\cdots}=\dfrac{\sum wx}{\sum w}$.",
   r"Equal weights give the simple mean."]),
 ("Mixtures and concentration", [r"Concentration $=\dfrac{\text{amount of ingredient}}{\text{total amount of mixture}}\times100\%$.",
   r"Amount of ingredient $=\dfrac{\text{concentration}}{100}\times\text{total}$.",
   r"On mixing: total ingredient $=$ sum of ingredients; total volume $=$ sum of volumes; new concentration $=\dfrac{\text{total ingredient}}{\text{total volume}}\times100\%$.",
   r"Adding pure water keeps the amount of ingredient the same and increases the total."]),
 ("Stacked bars", [r"A stacked bar chart shows the parts of each total on one bar; bar length $=$ total.",
   r"In a 100% stacked bar chart every bar has length 100% and shows only the shares of the parts."]),
]

MISTAKES = [
 r"Taking the combined average as $\dfrac{a_1+a_2}{2}$ when the groups have different sizes.",
 r"Adding the percentages of two solutions to find the mixture, or averaging the two concentrations without using the volumes.",
 r"Dividing the sum of weighted scores by the number of items instead of by the sum of the weights.",
 r"Forgetting to change the volume when water is added: the pure amount stays the same but the total increases.",
 r"Using a percentage as if it were an amount (e.g. $20\%$ of 5 L is 1 L, not 20 L).",
 r"Reading a 100% stacked bar as if the bar lengths showed the actual totals; the actual totals are not shown.",
]
