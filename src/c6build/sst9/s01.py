from sst9.common import mcq, Q, OR, AR
from mk9 import M4, build
def fm(x):
    return str(int(x)) if x == int(x) else f"{x:.2f}".rstrip("0").rstrip(".")
A = []
# opportunity cost numeric (6)
for what, give, units, why in [("a farmer shifts one hectare from wheat to barley, losing 30 quintals of wheat", "30 quintals of wheat", ["30 quintals of barley", "60 quintals of wheat", "nothing, since barley is gained"], "next best alternative given up"),
    ("Meena spends ₹100 on a notebook instead of a story book that costs ₹100", "the story book", ["₹100 in cash", "the notebook", "nothing"], "forgone alternative"),
    ("a student spends 3 hours on a video game instead of studying", "3 hours of studying", ["the video game", "3 hours of sleep always", "₹3"], "time has an opportunity cost"),
    ("the government builds a hospital on land that could have been a school", "the school that could have been built", ["the hospital", "the land price only", "no cost"], "scarce land"),
    ("a factory uses ₹10 lakh to buy a machine instead of hiring workers", "the benefit of hiring workers", ["the machine", "₹10 lakh only", "nothing"], "alternative use of money"),
    ("a family uses a bonus of ₹20,000 for a holiday instead of repairing the roof", "repairing the roof", ["the holiday", "the bonus", "₹20,000 interest"], "next best use")]:
    A.append(M4(f"The opportunity cost when {what} is:", give, units, why))
# PPC numeric (4)
for pts, q, ans in [(("A: 100 wheat, 0 barley", "B: 70 wheat, 30 barley"), "Moving from A to B, the opportunity cost of 30 barley is:", "30 wheat"),
                    (("A: 80 cloth, 0 steel", "B: 50 cloth, 20 steel"), "Moving from A to B, the opportunity cost of 20 steel is:", "30 cloth"),
                    (("A: 60 rice, 10 pulses", "B: 40 rice, 25 pulses"), "Moving from A to B, the opportunity cost of 15 more pulses is:", "20 rice"),
                    (("A: 90 laptops, 0 phones", "B: 60 laptops, 30 phones"), "Moving from A to B, the opportunity cost of 30 phones is:", "30 laptops")]:
    n = int(ans.split()[0]); u = ans.split()[1]
    A.append(M4(f"On a Production Possibility Curve, {pts[0]} and {pts[1]}. {q}", ans, [f"{n+10} {u}", f"{max(n-10,5)} {u}", f"{n*2} {u}"], "difference in the good given up"))
A += [
 M4("The word ‘Economics’ comes from the Greek word oikonomia meaning:", "household management", ["market place", "money", "taxation"], "oikos + nemein"),
 M4("The basic economic problem arises because:", "resources are limited while wants are unlimited", ["wants are limited", "money is unlimited", "there is no choice"], "scarcity"),
 M4("Scarcity means:", "resources are limited in relation to wants", ["resources are free", "resources are absent", "resources are unlimited"], "basic economic problem"),
 M4("Which of the following is a need rather than a want?", "food and water", ["a luxury car", "a holiday abroad", "branded shoes"], "essentials for survival"),
 M4("Opportunity cost is:", "the value of the next best alternative given up", ["the money cost of a good", "the profit made", "the price in the market"], "trade-off"),
 M4("The three central questions of an economy are:", "what, how and for whom to produce", ["when, where and why to produce", "how to save, spend, borrow", "who, what, when"], "all economies face them"),
 M4("The question ‘for whom to produce’ concerns:", "distribution of goods among people", ["choice of technology", "the quantity of crops", "foreign trade"], "who will use the goods"),
 M4("Choosing between labour-intensive and capital-intensive methods answers:", "how to produce", ["what to produce", "for whom to produce", "when to produce"], "technique of production"),
 M4("The Production Possibility Curve shows:", "the trade-off between two goods with given resources", ["the demand curve", "the price of a good", "the total income"], "maximum combinations"),
 M4("A point inside the PPC indicates:", "under-use of resources", ["full employment of resources", "an impossible output", "perfect efficiency"], "inefficiency"),
 M4("A point outside the PPC is:", "not attainable with the present resources", ["attainable", "inefficient", "the best point"], "beyond capacity"),
 M4("In a planned economy, major economic decisions are taken by:", "the government or central authority", ["consumers", "private firms", "foreign countries"], "central planning"),
 M4("A market economy is mainly driven by:", "demand and supply", ["government orders", "the planning commission", "religious laws"], "private ownership"),
 M4("A mixed economy combines features of:", "market and planned economies", ["traditional and tribal economies", "barter and credit economies", "closed and open economies"], "private and public sectors"),
 M4("India adopted a more market-oriented approach after:", "1991", ["1947", "1971", "2008"], "economic reforms"),
 M4("Which country is an example of a largely market economy?", "United States of America", ["former Soviet Union", "North Korea", "Cuba"], "private ownership"),
 M4("In a planned economy, a major weakness is that:", "enterprises have little motivation to innovate", ["prices are always low", "private profit is too high", "government has no role"], "no competition"),
 M4("The role of the government in a pure market economy is compared to:", "a referee in a football match", ["a coach", "a goalkeeper", "a player"], "law and order"),
 M4("The Economic Survey is useful because it:", "reports how the Indian economy is performing", ["sets stock prices", "prints currency", "decides taxes"], "data and analysis"),
 M4("Good economic decisions depend on:", "data and analysis", ["guesswork", "luck", "rumours"], "surveys and reports"),
 M4("Choosing millets over sugarcane in a drought-prone region saves:", "water and improves soil health", ["labour only", "money in all cases", "profit"], "sustainable choice"),
 M4("An example of an economic entity is:", "a household", ["a mountain", "the weather", "a river"], "consumers, producers, government"),
 M4("When resources have alternative uses, it becomes necessary to:", "make choices", ["stop production", "print more money", "avoid trade"], "allocation"),
 M4("The demand for goods ‘for whom to produce’ depends on:", "income, tastes and needs of people", ["only the weather", "colour of the product", "the number of shops"], "purchasing power"),
 M4("Which of these is a labour-intensive activity?", "handloom weaving", ["steel manufacturing by machines", "automatic car assembly", "robotic welding"], "uses many workers"),
 AR("Every choice involves an opportunity cost.", "Resources are scarce and have competing uses.", "a", "scarcity forces trade-off"),
 AR("Pure economic systems rarely exist in reality.", "Most economies combine features of market and planned systems.", "a", "mixed economies"),
 AR("A point inside the Production Possibility Curve shows full use of resources.", "The PPC shows the maximum combinations of goods that can be produced.", "d", "inside = under-utilisation"),
 AR("In a planned economy enterprises have little motivation to innovate.", "Planned economies were common in several countries during the twentieth century.", "b", "true but R does not explain A"),
 AR("A market economy ensures that all people get essential goods at low prices.", "In a market economy goods go to those who are willing and able to pay.", "d", "A is false"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("What is meant by scarcity?", "Resources are limited in relation to the wants of people; this forces choices (2).", "2"),
 Q("Distinguish between needs and wants with an example each.", "Needs are essentials such as food; wants are things we desire such as a holiday or gadgets (1+1).", "1+1"),
 Q("Define opportunity cost with an example.", "The value of the next best alternative given up (1); spending ₹100 on a notebook means giving up a story book (1).", "1+1"),
 Q("What is the meaning of ‘Economics’ according to the Greek origin of the word?", "Oikonomia means household management; it deals with the management of limited resources (2).", "2"),
 Q("Name the three central problems of every economy.", "What to produce, how to produce and for whom to produce (2).", "2"),
 Q("What does the Production Possibility Curve show?", "The different combinations of two goods that can be produced with given resources and the trade-off between them (2).", "2"),
 Q("What does a point inside a PPC indicate?", "Resources are not fully or efficiently used (2).", "2"),
 Q("Why is economics called a study of choice?", "Resources are limited with alternative uses, so choices have to be made (2).", "2"),
 Q("What is a planned economy? Give one example.", "An economy in which the government makes the main economic decisions and owns most resources (1); former Soviet Union or China before 1978 (1).", "1+1"),
 Q("What is a market economy?", "An economy in which production and prices are decided mainly by demand and supply with private ownership (2).", "2"),
 Q("What is a mixed economy? Name two examples.", "An economy combining features of market and planned systems (1); India after 1991 and Germany (1).", "1+1"),
 Q("State two advantages of a market economy.", "Competition improves quality and lowers prices; encourages innovation and efficiency (1+1).", "1+1"),
 Q("State one drawback of a planned economy.", "Little motivation for innovation and quality, and delay in decisions (2).", "2"),
 Q("How does data help in economic decision making?", "It gives facts on production, prices, population and trends so choices are based on evidence, not guesswork (2).", "2"),
 Q("What is the purpose of the Economic Survey?", "It reports how the Indian economy performed and guides the Union Budget (2).", "2"),
 Q("Why do we say that economics is not only about money?", "It studies how choices are made on limited resources, including time, labour and land (2).", "2"),
]
C = [
 Q("Distinguish between scarcity and shortage with examples.", "Scarcity is a permanent limit on resources compared to wants (1.5); shortage is a temporary lack of supply, such as sugar after a poor harvest (1.5).", "1½+1½"),
 Q("Explain why human wants are unlimited and how this affects production.", "Wants keep changing with income, tastes and technology (1.5); production must keep changing and economies must choose what to produce (1.5).", "1½+1½"),
 Q("A farmer can produce 100 quintals of wheat or 40 of barley; he changes to 70 wheat and 30 barley. Explain opportunity cost using the PPC.", "To increase barley from 0 to 30, he gives up 30 wheat (1.5); the PPC shows this trade-off (1.5).", "1½+1½"),
 Q("A student has ₹100 and must choose between a notebook and a story book. Explain the opportunity cost.", "Whichever is chosen, the other is given up (1.5); the value of the story book is the opportunity cost of buying the notebook (1.5).", "1½+1½"),
 Q("Explain the problem ‘what to produce’ with an example from agriculture.", "Choosing between water-intensive sugarcane and drought-resistant millets (1.5); each has benefits and an opportunity cost (1.5).", "1½+1½"),
 Q("Explain the problem ‘how to produce’ with the labour and capital-intensive techniques.", "Techniques may use more labour (handlooms) or more machinery (steel) (1.5); the choice depends on cost and availability of labour (1.5).", "1½+1½"),
 Q("Explain ‘for whom to produce’.", "Goods must reach people according to income, tastes and needs (1.5); e.g. leather shoes target office-goers (1.5).", "1½+1½"),
 Q("Why must every economy face the three central problems?", "Because resources are limited and have alternative uses (1.5); allocation must be decided in any system (1.5).", "1½+1½"),
 Q("Compare planned and market economies in three points.", "Decision maker: government vs market; ownership: public vs private; efficiency/incentives: low incentives vs high (1+1+1).", "1+1+1"),
 Q("What is the role of the government in a market economy?", "Ensures law and order, safety and public goods and infrastructure (1.5); it does not control prices and production in a pure market (1.5).", "1½+1½"),
 Q("Why is a mixed economy common in the world?", "It uses the efficiency of markets (1.5) along with government intervention for welfare and infrastructure (1.5).", "1½+1½"),
 Q("How has India's economic system evolved over time?", "After independence India used planning and the public sector (1.5); in 1991 reforms opened trade and investment and increased competition (1.5).", "1½+1½"),
 Q("Why do economists use surveys and reports?", "Surveys collect data on behaviour of households and firms (1.5); the data help analyse alternatives and policies (1.5).", "1½+1½"),
 Q("State three scope areas of economics in daily life.", "Households allocating income; firms deciding production; government deciding taxes and welfare (1+1+1).", "1+1+1"),
 Q("A government has to choose between a hospital and a school on a plot. Apply the idea of opportunity cost.", "Building one means giving up the other (1.5); the benefit of the next best option is the opportunity cost (1.5).", "1½+1½"),
 Q("Why do pure economic systems rarely exist in reality?", "Pure markets ignore welfare and public goods; pure planning lacks incentives (1.5); hence most economies are mixed (1.5).", "1½+1½"),
 Q("Differentiate between labour-intensive and capital-intensive production.", "Labour-intensive uses more workers, e.g. handloom (1.5); capital-intensive uses more machines, e.g. automobile plants (1.5).", "1½+1½"),
 Q("How does opportunity cost improve decision making?", "It makes people compare alternatives (1.5), so that scarce resources are put to their best use (1.5).", "1½+1½"),
 Q("Explain how a country's present choices can shape its future.", "Investing in education and infrastructure raises future growth (1.5); heavy consumption now may reduce future savings (1.5).", "1½+1½"),
 Q("What is a trade-off? Give an example from daily life.", "Giving up one thing to get another (1); more time on games means less time to study (2).", "1+2"),
 Q("Why are choices necessary even for a rich country?", "Resources are limited relative to wants for every country (3).", "3"),
 Q("State the significance of studying economics for a citizen.", "Helps in personal choices such as budgeting; helps understand policies and the Union Budget; helps evaluate the use of public resources (1+1+1).", "1+1+1"),
 Q("Differentiate between needs, wants and luxuries.", "Needs are essentials (food); wants are desires (gadgets); luxuries are costly wants beyond normal income (1+1+1).", "1+1+1"),
 Q("Why does a farmer's choice between crops involve both economic and ecological considerations?", "Profit and market demand matter (1.5); water use and soil health decide sustainability (1.5).", "1½+1½"),
]
D = [
 Q("(i) Define scarcity. (ii) How does scarcity give rise to choice? (iii) Explain opportunity cost with two examples.", "(i) Limited resources relative to unlimited wants (1). (ii) Resources have alternative uses so some uses must be given up (2). (iii) Notebook vs story book; wheat vs barley on a farm (2).", "1+2+2"),
 Q("<b>Case study:</b> A farm has resources to produce wheat and barley: A (100, 0), B (70, 30), C (40, 55), D (0, 70). (i) What curve is formed? (ii) Find the opportunity cost of moving A to B. (iii) Find the opportunity cost of moving B to C per unit of barley. (iv) What does a point inside the curve show?", "(i) The PPC (1). (ii) 30 wheat for 30 barley (1). (iii) 30 wheat for 25 barley, i.e. 1.2 wheat per barley (2). (iv) Unused or wasted resources (1).", "1+1+2+1"),
 Q("(i) State the central problems of an economy. (ii) Explain each with an example. (iii) Why do they arise in all economies?", "(i) What, how, for whom (1). (ii) What: sugarcane or millets; how: handloom or power loom; for whom: shoes for office-goers (3). (iii) Scarce resources with alternative uses (1).", "1+3+1"),
 Q("<b>Case study:</b> A farmer in a dry region debates sugarcane (high profit, much water) and millets (less profit, little water). (i) Which central problem is it? (ii) State the opportunity cost of sugarcane. (iii) Which choice is more sustainable? (iv) How can government policy help?", "(i) What to produce (1). (ii) The benefit of growing millets, water saved and soil health (1). (iii) Millets (1). (iv) By giving support price, irrigation and market access (2).", "1+1+1+2"),
 Q("(i) Describe a market economy and its merits and demerits. (ii) Describe a planned economy and its merits and demerits.", "(i) Private ownership, prices by demand and supply; competition and innovation, but inequality and neglect of public goods (2.5). (ii) Government decisions; equality and planning but no incentive and delay (2.5).", "2½+2½"),
 Q("(i) What is a mixed economy? (ii) Why do most countries follow it? (iii) Trace the movement of the Indian economy towards a mixed economy.", "(i) Mix of market and planned features (1). (ii) Benefits of both systems (2). (iii) Planning and public sector after 1947; 1991 reforms opening to markets (2).", "1+2+2"),
 Q("<b>Case study:</b> A newspaper reports that the price of tomatoes has risen sharply because of heavy rains. (i) Which questions of economics are involved? (ii) Which data would an economist use? (iii) How may the government respond? (iv) What can households do?", "(i) How much to produce or supply and for whom (1). (ii) Production, arrival in markets and price data (1). (iii) Importing, releasing stock or price monitoring (1). (iv) Substitute vegetables and reduce quantity (2).", "1+1+1+2"),
 Q("(i) Why is data important in economics? (ii) Name two sources of data. (iii) How does the Economic Survey help?", "(i) Evidence-based decisions (2). (ii) Surveys and government reports (1). (iii) Shows how the economy is performing and guides the Budget (2).", "2+1+2"),
 Q("(i) What is the Production Possibility Curve? (ii) Explain its shape with an example. (iii) What do the points inside and outside the curve show?", "(i) Curve showing maximum combinations of two goods with given resources (1). (ii) More of one good requires giving up the other; curve bends outwards because resources are not equally suitable (2). (iii) Inside: under-utilisation; outside: not attainable (2).", "1+2+2"),
 Q("<b>Case study:</b> Meena has ₹200 and wants a bag (₹150), a book (₹100) and a pen (₹50). (i) Name the problem. (ii) List two possible choices. (iii) Find the opportunity cost of each. (iv) What decision rule would you give?", "(i) Scarcity of income, so a choice (1). (ii) Bag + pen or book + pen (1). (iii) Book or bag respectively (1). (iv) Pick the combination with greatest benefit (2).", "1+1+1+2"),
 Q("(i) How do consumers, producers, governments and financial institutions interact in an economy? (ii) Give two examples.", "(i) Consumers buy, producers supply, government regulates, banks lend (3). (ii) Wages earned and spent; taxes used for welfare (2).", "3+2"),
 Q("(i) Why do economists study ‘for whom to produce’? (ii) How do income and tastes affect it? (iii) Give an example from India.", "(i) To decide distribution (1). (ii) Rich buy more and different goods (2). (iii) Affordable shoes for students and leather shoes for office-goers (2).", "1+2+2"),
 Q("<b>Case study:</b> A small factory can use either 50 workers or 5 machines. (i) Name the techniques. (ii) Which is suitable if labour is cheap? (iii) Which is suitable for high precision? (iv) What are the social effects of each?", "(i) Labour-intensive and capital-intensive (1). (ii) Labour-intensive (1). (iii) Capital-intensive (1). (iv) Labour gives jobs; machines raise output but reduce employment (2).", "1+1+1+2"),
 Q("(i) Explain why scarcity exists in rich and poor countries alike. (ii) How can better choices reduce its effects?", "(i) Wants always exceed resources (2). (ii) Setting priorities, saving, reducing waste and using technology (3).", "2+3"),
 Q("(i) Differentiate market, planned and mixed economies in a table of four points. (ii) Which do you think suits India? Justify.", "(i) Ownership, decision maker, role of prices, examples (3). (ii) Mixed, because it combines efficiency with welfare (2).", "3+2"),
 Q("(i) What is meant by trade-off? (ii) Explain with a PPC how producing more of one good reduces another. (iii) How can a country shift its PPC outward?", "(i) Giving up one thing to get another (1). (ii) With fixed resources, moving along the curve gives up one good for the other (2). (iii) By more resources, better technology and skills (2).", "1+2+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
