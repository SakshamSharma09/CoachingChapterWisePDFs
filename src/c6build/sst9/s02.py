from sst9.common import mcq, Q, OR, AR
from mk9 import M4, build
A = []
# market demand sums (4)
for pr, d in [(150, (1, 2, 3)), (100, (2, 4, 5)), (50, (3, 6, 9)), (60, (2, 3, 6))]:
    tot = sum(d)
    ws = [x for x in dict.fromkeys([tot + 2, tot - 1, max(d), tot * 2, d[0]]) if x != tot][:3]
    A.append(M4(f"At ₹{pr} per kg, three consumers demand {d[0]} kg, {d[1]} kg and {d[2]} kg of mangoes. The market demand is:", f"{tot} kg", [f"{x} kg" for x in ws], "sum of individual demands"))
# equilibrium price from schedule (4)
EQ = [("Price (₹): 10, 20, 30, 40; Quantity demanded: 100, 80, 60, 40; Quantity supplied: 20, 40, 60, 80", "₹30", ["₹10", "₹20", "₹40"], "QD = QS = 60"),
      ("Price (₹): 5, 10, 15, 20; Quantity demanded: 90, 70, 50, 30; Quantity supplied: 10, 30, 50, 70", "₹15", ["₹5", "₹10", "₹20"], "QD = QS = 50"),
      ("Price (₹): 2, 4, 6, 8; Quantity demanded: 60, 50, 40, 30; Quantity supplied: 20, 30, 40, 50", "₹6", ["₹2", "₹4", "₹8"], "QD = QS = 40")]
for tab, ans, w, why in EQ[:3]:
    A.append(M4(f"From the schedule — {tab} — the equilibrium price is:", ans, w, why))
# excess demand / supply (4)
for tab, ask, ans, w in [("At ₹10, quantity demanded is 100 and quantity supplied is 20", "the excess demand is:", "80", ["20", "100", "120"]),
                         ("At ₹40, quantity demanded is 40 and quantity supplied is 80", "the excess supply is:", "40", ["80", "120", "0"]),
                         ("At ₹15, quantity demanded is 50 and quantity supplied is 50", "the market is:", "in equilibrium", ["in excess demand", "in excess supply", "closed"]),
                         ("At ₹5, quantity demanded is 90 and quantity supplied is 10", "the situation is called:", "excess demand (shortage)", ["excess supply (surplus)", "equilibrium", "price floor"])]:
    A.append(M4(f"{tab}; {ask}", ans, w, "QD − QS"))
A += [
 M4("Demand means the quantity that consumers are:", "willing and able to buy at a given price", ["only willing to buy", "forced to buy", "able but unwilling to buy"], "desire plus purchasing power"),
 M4("The Law of Demand states that, other things remaining equal, as price rises:", "quantity demanded falls", ["quantity demanded rises", "quantity supplied falls", "demand never changes"], "inverse relationship"),
 M4("The demand curve usually slopes:", "downward from left to right", ["upward", "vertically", "horizontally"], "inverse relation"),
 M4("The sum of the demand of all individual buyers is called:", "market demand", ["supply", "equilibrium", "elasticity"], "adds up"),
 M4("Tea and coffee are examples of:", "substitutes", ["complements", "public goods", "luxury goods only"], "can replace each other"),
 M4("Printers and printer cartridges are examples of:", "complementary goods", ["substitute goods", "free goods", "inferior goods"], "used together"),
 M4("If the price of coffee rises, the demand for tea will:", "increase", ["decrease", "stay the same", "become zero"], "substitute"),
 M4("Rising incomes generally:", "raise the demand for most goods", ["reduce demand for all goods", "have no effect", "reduce supply"], "more purchasing power"),
 M4("The principle that additional satisfaction falls with each extra unit consumed is:", "diminishing marginal utility", ["law of supply", "equilibrium", "price floor"], "the third mango"),
 M4("Expectation of a future price fall makes consumers:", "postpone buying", ["buy more now", "ignore prices", "stop consuming"], "present demand falls"),
 M4("The law of supply states that as price rises, quantity supplied:", "rises", ["falls", "remains zero", "becomes infinite"], "higher profits"),
 M4("The supply curve generally slopes:", "upward", ["downward", "vertical only", "horizontal only"], "direct relation"),
 M4("Which of the following increases supply?", "a fall in the cost of inputs", ["a rise in the cost of inputs", "a bad monsoon", "a heavy tax on production"], "cheaper production"),
 M4("The price at which quantity demanded equals quantity supplied is the:", "equilibrium price", ["price ceiling", "price floor", "black market price"], "market clears"),
 M4("When price is above the equilibrium, there is:", "excess supply", ["excess demand", "equilibrium", "shortage"], "unsold goods"),
 M4("When price is below the equilibrium, there is:", "excess demand", ["excess supply", "equilibrium", "surplus"], "shortage pushes the price up"),
 M4("A maximum price fixed by the government is called a:", "price ceiling", ["price floor", "equilibrium price", "tax"], "e.g. on sanitisers in an emergency"),
 M4("A minimum price fixed by the government is called a:", "price floor", ["price ceiling", "market price", "subsidy"], "e.g. minimum wage or MSP"),
 M4("The Essential Commodities Act, 1955 allows the government to:", "control the supply and price of essential goods", ["ban all trade", "fix wages of all workers", "tax foreign goods"], "price control"),
 M4("A market in which a single seller controls the supply of a product is a:", "monopoly", ["perfect competition", "price floor", "mixed market"], "no close substitutes"),
 M4("Illegal sale of goods at higher than the legal price is called:", "black marketing", ["subsidy", "dumping", "price floor"], "banned or controlled goods"),
 M4("Street lighting and national defence are examples of:", "public goods", ["private goods", "luxury goods", "inferior goods"], "provided by government"),
 M4("Why does the market demand curve look flatter than an individual's curve?", "Many buyers respond to a price change together", ["There are fewer buyers", "The price is constant", "Supply is fixed"], "aggregation"),
 AR("A rise in the price of coffee can increase the demand for tea.", "Tea and coffee are substitutes.", "a", "buyers switch"),
 AR("A price ceiling is fixed above the equilibrium price.", "It is meant to protect consumers from high prices.", "d", "ceiling is below equilibrium"),
 M4("A fall in the price of a good leads to a:", "movement along the demand curve (rise in quantity demanded)", ["shift of the supply curve", "fall in income", "change in tastes"], "price effect"),
 M4("Which of the following would shift the demand curve for ice cream to the right?", "a rise in consumers' incomes in summer", ["a rise in the price of ice cream", "a fall in the temperature", "a rise in its cost of production"], "non-price factor"),
 M4("When two goods are complements, a rise in the price of one will:", "reduce the demand for the other", ["increase the demand for the other", "not affect the other", "make the other free"], "used together"),
 M4("Which of these is NOT a feature of a monopoly?", "many sellers offering close substitutes", ["a single seller", "no close substitutes", "control over price"], "monopoly vs competition"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Define demand.", "The quantity of a product that people are willing and able to buy at a particular price (2).", "2"),
 Q("State the Law of Demand.", "Other things remaining equal, a fall in price raises quantity demanded and a rise lowers it (2).", "2"),
 Q("What is a demand schedule?", "A table showing quantities a consumer will buy at different prices (2).", "2"),
 Q("Why does a demand curve slope downward?", "As price rises, people buy less; also marginal utility diminishes (2).", "2"),
 Q("Distinguish between substitute and complementary goods with one example each.", "Substitutes replace each other, tea and coffee; complements are used together, cars and petrol (1+1).", "1+1"),
 Q("State two factors other than price that affect demand.", "Income, tastes and preferences, population, season, expectations (1+1).", "1+1"),
 Q("What is diminishing marginal utility?", "The additional satisfaction from each extra unit falls as consumption increases (2).", "2"),
 Q("State the law of supply.", "As price rises, quantity supplied rises, and as it falls, supply falls (2).", "2"),
 Q("State two factors that increase supply.", "Fall in cost of inputs, improved technology, good weather, subsidies (1+1).", "1+1"),
 Q("What is market equilibrium?", "A situation where quantity demanded equals quantity supplied and the price is stable (2).", "2"),
 Q("What happens when price is above the equilibrium price?", "Supply exceeds demand, there is excess supply and the price tends to fall (2).", "2"),
 Q("Define price ceiling with one example.", "A maximum price fixed by the government, e.g. ₹100 cap on sanitisers (2).", "2"),
 Q("Define price floor with one example.", "A minimum price fixed above the market price, e.g. minimum support price (2).", "2"),
 Q("What is a monopoly? Why is it harmful?", "One seller controls the supply with no substitutes (1); it charges higher prices and offers poorer quality (1).", "1+1"),
 Q("What is black marketing?", "Selling goods at illegally high prices or selling banned goods (2).", "2"),
 Q("Give two examples of public goods.", "Street lights, roads, national defence, sanitation (1+1).", "1+1"),
]
C = [
 Q("Using Srivalli's example, explain the law of demand.", "At ₹150 she buys 1 kg, at ₹100 2 kg, at ₹50 3 kg (2); so quantity demanded rises as price falls (1).", "2+1"),
 Q("How is market demand derived from individual demand?", "Add the quantities demanded by all consumers at each price (1.5); plot to get the market demand curve (1.5).", "1½+1½"),
 Q("Three consumers want 1, 3 and 8 kg of mangoes at ₹50. What is the market demand? What happens at ₹150 if demands are 1, 2 and 4?", "Market demand = 12 kg (1.5); at ₹150 = 7 kg (1.5).", "1½+1½"),
 Q("Explain how the prices of related goods influence demand.", "A rise in the price of a substitute raises the demand for the other (1.5); a rise in the price of a complement lowers the demand for the other (1.5).", "1½+1½"),
 Q("How do income and tastes affect demand?", "A rise in income raises the demand for normal goods (1.5); a change in tastes shifts demand for specific goods (1.5).", "1½+1½"),
 Q("How does the size and composition of population affect demand? Give an example.", "More people means more demand (1); more children raise the demand for sports shoes, more elderly raise the demand for healthcare (2).", "1+2"),
 Q("Explain with an example how expectation of future prices influences current demand.", "If prices are expected to fall, people postpone purchases (1.5); if to rise, they buy immediately (1.5).", "1½+1½"),
 Q("Explain diminishing marginal utility with the example of mangoes.", "First mango gives high satisfaction (1); later ones give less, so willingness to pay falls (2).", "1+2"),
 Q("How do season and festivals affect demand? Give two examples.", "Demand for sweaters in winter, sweets during festivals (1.5+1.5).", "1½+1½"),
 Q("Explain the law of supply with a schedule.", "At ₹50 a seller supplies 1 kg, at ₹100 2 kg, at ₹150 3 kg (2); supply rises with price (1).", "2+1"),
 Q("Why do sellers supply more at higher prices?", "Higher prices raise profit (1.5); they also attract new firms (1.5).", "1½+1½"),
 Q("Explain three factors that change supply.", "Cost of inputs, technology, weather, taxes and subsidies (1+1+1).", "1+1+1"),
 Q("Explain how a market reaches equilibrium when price is too high.", "Excess supply creates unsold stock (1); sellers reduce price (1); price falls till QD = QS (1).", "1+1+1"),
 Q("Explain how a market reaches equilibrium when price is too low.", "Excess demand creates a shortage (1); buyers bid price up (1); price rises to equilibrium (1).", "1+1+1"),
 Q("From the schedule (₹10: D100, S20; ₹20: D80, S40; ₹30: D60, S60) find the equilibrium and excess demand at ₹10.", "Equilibrium price ₹30 with 60 units (1.5); excess demand at ₹10 = 100 − 20 = 80 (1.5).", "1½+1½"),
 Q("Why is equilibrium in the real world never stable?", "Demand and supply keep changing with income, weather, tastes and costs, so the price keeps adjusting (3).", "3"),
 Q("Why does the government intervene in markets?", "To ensure fairness for essential goods (1); to protect consumers, workers and producers (1); to prevent monopoly and black marketing (1).", "1+1+1"),
 Q("Explain price ceiling with the example of sanitisers.", "During an emergency prices rose sharply (1); the government capped the price at ₹100 under the Essential Commodities Act (1); it became available at fair prices (1).", "1+1+1"),
 Q("Explain price floor with the example of the minimum wage.", "A lower limit set above the market wage (1.5); it protects workers from exploitation (1.5).", "1½+1½"),
 Q("Why can monopoly harm consumers? How does the government respond?", "A single seller sets higher prices and lower quality (1.5); government regulates unfair practices and promotes competition (1.5).", "1½+1½"),
 Q("What are public goods? Why are they provided by the government?", "Goods for public use such as roads and defence (1); private firms cannot easily charge for them, so government provides them (2).", "1+2"),
 Q("What are the drawbacks of price control?", "May reduce supply and lead to shortages (1.5); black marketing may arise (1.5).", "1½+1½"),
 Q("Explain how regulations and licences can affect businesses.", "Too many licences and compliance procedures raise costs and delays (1.5); fewer start-ups and slower growth (1.5).", "1½+1½"),
 Q("How do the prices of inputs and technology affect the supply of a good? Give an example.", "Higher input costs reduce profit and supply (1.5); better technology lowers cost and raises supply, e.g. cold storage for mangoes (1.5).", "1½+1½"),
]
D = [
 Q("(i) State the law of demand. (ii) Explain it with a demand schedule and a curve. (iii) State two exceptions or limitations to the law.", "(i) Inverse relation between price and quantity demanded (1). (ii) Schedule of price and quantity, a downward sloping curve (2). (iii) Expected price rise, status goods (2).", "1+2+2"),
 Q("<b>Case study:</b> Three consumers demand mangoes: at ₹150: 1, 2, 3 kg; at ₹100: 2, 4, 5 kg; at ₹50: 3, 6, 9 kg. (i) Find the market demand at each price. (ii) Is the law of demand satisfied? (iii) By how much does market demand rise when the price falls from ₹150 to ₹50? (iv) Why is the market curve flatter?", "(i) 6, 11 and 18 kg (2). (ii) Yes (1). (iii) 12 kg (1). (iv) Many buyers respond together (1).", "2+1+1+1"),
 Q("(i) List five factors that affect demand. (ii) Explain related goods with examples. (iii) Explain diminishing marginal utility.", "(i) Price of related goods, income, tastes, population, season, expectations (2). (ii) Substitutes and complements (2). (iii) Falling utility from each extra unit (1).", "2+2+1"),
 Q("<b>Case study:</b> Before Diwali, people postpone the purchase of expensive durables, expecting discounts. (i) Which factor is it? (ii) How does it affect present demand? (iii) How might sellers respond? (iv) Give another example of seasonal demand.", "(i) Expectation of future prices (1). (ii) Present demand falls (1). (iii) Announce discounts (1). (iv) Sweaters in winter or umbrellas in monsoon (2).", "1+1+1+2"),
 Q("(i) State the law of supply. (ii) Draw and explain a supply curve. (iii) State the factors that change supply.", "(i) Direct relation between price and quantity supplied (1). (ii) Upward sloping curve; higher prices give higher profit (2). (iii) Cost, technology, weather, taxes and subsidies (2).", "1+2+2"),
 Q("<b>Case study:</b> Table — Price: 10, 20, 30, 40; QD: 100, 80, 60, 40; QS: 20, 40, 60, 80. (i) Find the equilibrium. (ii) Find the excess demand at ₹10. (iii) Find the excess supply at ₹40. (iv) Explain how the market moves from ₹40 to equilibrium.", "(i) ₹30, 60 units (1). (ii) 80 (1). (iii) 40 (1). (iv) Sellers lower the price; QD rises and QS falls until equal (2).", "1+1+1+2"),
 Q("(i) Define equilibrium price and quantity. (ii) Show how the market adjusts when price is above and below equilibrium. (iii) Does equilibrium exist in the real world?", "(i) Price at which QD = QS (1). (ii) Excess supply lowers price; excess demand raises it (2). (iii) Rarely stable because demand and supply keep changing (2).", "1+2+2"),
 Q("<b>Case study:</b> During an epidemic, sanitiser prices soared and the government capped the maximum retail price at ₹100. (i) Name the control. (ii) Which law was used? (iii) What happened to availability? (iv) Name a possible harm of such control.", "(i) Price ceiling (1). (ii) Essential Commodities Act, 1955 (1). (iii) Sanitisers became widely available at fair prices (1). (iv) Black marketing or lower supply (2).", "1+1+1+2"),
 Q("(i) Why does the government intervene in the market? (ii) Explain price ceiling and price floor. (iii) Give one example of each.", "(i) Fairness, protect consumers and workers (1). (ii) Maximum and minimum prices (2). (iii) Sanitiser price; minimum wage or MSP (2).", "1+2+2"),
 Q("(i) What is a monopoly? (ii) Why is it harmful? (iii) How does the government check it?", "(i) Single seller controlling supply (1). (ii) Higher price, poor quality, less choice (2). (iii) Regulations and competition laws (2).", "1+2+2"),
 Q("<b>Case study:</b> A black market for tickets sells them at three times the price. (i) Define black marketing. (ii) Why does it arise? (iii) Who loses? (iv) Suggest two ways to control it.", "(i) Illegal sale at higher prices (1). (ii) Shortage with high demand (1). (iii) Consumers (1). (iv) Strict laws, online booking, more supply (2).", "1+1+1+2"),
 Q("(i) What are public goods? (ii) Give four examples. (iii) Why is government provision necessary?", "(i) Goods used by all and not easily priced (1). (ii) Roads, parks, defence, sanitation (2). (iii) Private firms would not supply them without profit (2).", "1+2+2"),
 Q("(i) Explain how a change in demand and a change in supply affect the equilibrium price. (ii) Give examples.", "(i) Rise in demand raises price; rise in supply lowers price (3). (ii) Mangoes in season, onions after a bad harvest (2).", "3+2"),
 Q("<b>Case study:</b> At the start of the mango season supply is low and price high; mid-season supply rises and price falls. (i) Explain with demand and supply. (ii) What happens to quantity demanded? (iii) What is the role of price? (iv) Which factors might raise supply further?", "(i) Excess demand early; excess supply later (1). (ii) Rises as price falls (1). (iii) Signals scarcity and balances the market (1). (iv) Good weather, transport, storage (2).", "1+1+1+2"),
 Q("(i) How do licences and regulations affect businesses? (ii) How can markets be made more efficient? (iii) State the role of the government.", "(i) Raise cost and delay (2). (ii) Simplify rules, ensure competition (2). (iii) Protect fairness and provide public goods (1).", "2+2+1"),
 Q("(i) How are prices determined in a market? (ii) Explain the role of buyers and sellers in bargaining. (iii) Why do the prices of vegetables change between morning and evening?", "(i) By the interaction of demand and supply (1). (ii) Buyers offer what they are willing to pay and sellers what they will accept (2). (iii) Freshness and unsold stock force sellers to lower prices in the evening (2).", "1+2+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
