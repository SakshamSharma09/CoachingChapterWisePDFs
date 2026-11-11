"""Class 9 SST Ch 2 The Price Puzzle - Hard-tier extras (AR, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("At a price below the equilibrium price there is excess demand.", "At a lower price buyers want to buy more while sellers are willing to supply less.", "a",
     "Quantity demanded exceeds quantity supplied at a low price, so a shortage appears and price tends to rise."),
 AR4("Tea and coffee are substitutes.", "Smartphones and earphones are complements.", "b",
     "Both are true but the second statement about complements does not explain why tea and coffee are substitutes."),
 AR4("The demand curve usually slopes downward.", "When the price of a good rises, buyers always want to buy more of it.", "c",
     "By the law of demand a rise in price reduces quantity demanded; so A is true and R is false."),
 AR4("A minimum price fixed below the equilibrium price makes a difference to the market.", "In such a case the market price is already higher than the minimum price.", "d",
     "A price floor below equilibrium is not binding, so A is false; R is true."),
 AR4("Hoarding reduces the supply of a good in the market.", "Hoarders store goods beyond need in the hope of selling them later at higher prices.", "a",
     "Goods kept back from sale reduce market supply, which pushes up the price in the short run."),
 AR4("Better technology that lowers the cost of production raises supply.", "At market equilibrium the quantity demanded equals the quantity supplied.", "b",
     "Both are true, but R is the definition of equilibrium and has no link with the effect of technology on supply."),
]

CASE = [
 Q("<b>Case study.</b> In a mango market the quantities demanded and supplied (kg) at different prices are: at Rs 50, demand 18 and supply 6; at Rs 100, demand 12 and supply 12; at Rs 150, demand 6 and supply 18. "
   "(i) What is the equilibrium price and quantity? (ii) What is the situation at Rs 50 and by how many kg? (iii) What is the situation at Rs 150 and by how many kg? (iv) In which direction will the price move in (ii) and (iii) and why?",
   "(i) Rs 100 and 12 kg, where demand equals supply (1). (ii) Excess demand (shortage) of 18 - 6 = 12 kg (1). (iii) Excess supply (surplus) of 18 - 6 = 12 kg (1). (iv) In (ii) price tends to rise because buyers compete for scarce mangoes; in (iii) price tends to fall because sellers cut prices to clear the unsold stock; both movements push the market back to Rs 100 (2).", "1+1+1+2"),
 Q("<b>Case study.</b> In 2020 the demand for hand sanitisers rose sharply while supply could not keep pace, and prices shot up. Some traders stored large stocks to sell later at higher prices. The government declared sanitisers essential commodities under the Essential Commodities Act, 1955, and fixed a maximum price. "
   "(i) What is a maximum price fixed by the government called? (ii) Name the Act under which the cap was fixed. (iii) What is hoarding? (iv) If the maximum price is set below the equilibrium price, state its likely effect on the market and one problem it can create.",
   "(i) Price ceiling (1). (ii) The Essential Commodities Act, 1955 (1). (iii) Storing goods beyond need so as to sell them later at higher prices (1). (iv) It creates excess demand (shortage) because buyers want more and sellers offer less at the lower price (1); it can lead to black marketing or lower incentive to produce (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In Shimla, sales of woollens rise every December. When the price of coffee rises sharply, many customers switch to tea. Buyers of smartphones usually also buy earphones. A family hears that a TV sale will be held next month, so it decides to wait before buying one. "
   "(i) Which factor explains the rise in woollen sales in December? (ii) What type of goods are tea and coffee? (iii) What type of goods are smartphones and earphones? (iv) How will expectation of a sale next month affect today's demand for TVs, and why?",
   "(i) Seasonality (1). (ii) Substitutes (1). (iii) Complements (1). (iv) Current demand falls (1), because buyers expect the price to fall and postpone their purchases (1).", "1+1+1+2"),
]

MISTAKES = [
 "Do not confuse a <b>movement along</b> a demand or supply curve (caused by a change in the good's own price) with a <b>shift</b> of the curve (caused by income, tastes, related goods, technology, etc.).",
 "Excess demand = shortage (price below equilibrium); excess supply = surplus (price above equilibrium). Students often reverse these.",
 "Substitutes (tea and coffee) move in the same direction of demand when the price of the other changes; complements (smartphone and earphones) go together. Do not interchange them.",
 "A price ceiling is a <b>maximum</b> price and a price floor (e.g. minimum wage) is a <b>minimum</b> price; a floor below equilibrium or a ceiling above equilibrium has no effect.",
 "Market demand is the <b>sum</b> of all buyers' demands at a price (e.g. 1 + 2 + 3 = 6 kg); write the values for the same price, not different prices.",
 "In the real world equilibrium is not stable because demand and supply keep changing (pandemics, weather); the regulators are RBI (banking), SEBI (securities), TRAI (telecom) and CCPA (consumers).",
]
