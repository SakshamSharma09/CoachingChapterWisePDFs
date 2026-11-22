"""Class 9 Social Science Ch 14 - From Ideas to Startups (Economics, Part 2): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c9sst_ch14"

def _base():
    s = importlib.util.spec_from_file_location("c9sst_c14", str(REPO / "src/rn_work/c9_sst2/c14.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Lijjat Papad was started in 1959 by seven women in a Mumbai chawl with an initial amount of:", 1, "(a) ₹80", "E", opts=["₹80", "₹800", "₹8,000", "₹1,600"]),
W("Mohan Singh Oberoi bought his first hotel in 1934 by mortgaging his:", 1, "(c) wife's jewellery", "E", opts=["house", "shop", "wife's jewellery", "land"]),
W("The Dandekar brothers travelled to Glasgow to study:", 1, "(b) colour chemistry", "E", opts=["hotel management", "colour chemistry", "banking", "textile design"]),
W("Profit is calculated as:", 1, "(d) total revenue - total expenses", "E", opts=["total revenue + total expenses", "total expenses - total revenue", "total revenue × total expenses", "total revenue - total expenses"]),
W("Which of these is a fixed cost for a bakery?", 1, "(a) monthly rent of the shop", "E", opts=["monthly rent of the shop", "flour used", "packaging boxes", "sugar used"]),
W("A startup valued at over 1 billion dollars is called a:", 1, "(c) unicorn", "E", opts=["mortgage", "chawl", "unicorn", "cooperative"]),
W("India has the ______ largest startup ecosystem in the world.", 1, "(b) third", "E", opts=["first", "third", "fifth", "tenth"]),
W("Which functional area of a business deals with raising funds and keeping records of transactions?", 1, "(d) finance and accounting", "E", opts=["human resources", "marketing and sales", "operations", "finance and accounting"]),
W("Define entrepreneurship.", 2, "Entrepreneurship is the process through which an individual or group converts a potential business idea into a business venture. (2)", "E"),
W("What is a business plan?", 2, "A written blueprint or roadmap of a business's goals and the steps to achieve them (1); it guides decision-making and is revised as conditions change (1).", "E"),
W("Name the four functional areas of a business.", 2, "Management and operations; finance and accounting; human resources; marketing and sales. (0.5 each)", "E"),
W("Give one example each of a fixed cost and a variable cost for a bakery.", 2, "Fixed: rent, salaries or insurance (1). Variable: raw materials such as flour, or packaging (1).", "E"),
W("State True or False, with a reason: Failure is a waste and teaches an entrepreneur nothing.", 2, "False (1). Failure is a part of learning for startups and entrepreneurs; it shows what to change (1).", "E"),
W("Name two tasks of an entrepreneur.", 2, "Any two: takes risks; combines factors of production; identifies a problem and solves it; makes key decisions; contributes to society. (1+1)", "E"),
W("What is a chawl?", 1, "A multi-storey tenement of single-room units, as in Mumbai. (1)", "E"),
W("Fill in the blank: Mohan Singh Oberoi received the ______ in 2001.", 1, "Padma Bhushan (1)", "E"),
W("What is inventory?", 1, "Goods and assets held for production or resale. (1)", "E"),
# ---------------- MEDIUM ----------------
W("A baker spends ₹40,000 as monthly rent and ₹10 on materials for each cake. Find the total cost of making 1,000 cakes in a month, and the cost per cake.", 3, "Total cost = fixed + variable = 40,000 + 10 × 1,000 (1) = ₹50,000 (1). Cost per cake = 50,000 ÷ 1,000 = ₹50 (1).", "M", wp=True),
W("Anita sells 500 mini cakes a month at ₹120 each. Her costs are fixed ₹20,000 and ₹50 variable per cake. Find revenue, total cost and profit.", 3, "Revenue = 500 × 120 = ₹60,000 (1). Total cost = 20,000 + 50 × 500 = ₹45,000 (1). Profit = 60,000 - 45,000 = ₹15,000 (1).", "M", wp=True),
W("Why is the story of Lijjat Papad considered a cooperative success? State three features.", 3, "Seven homemakers started in 1959 with ₹80 (1). Members are equal owners and share profits equally; the cooperative was registered in 1962 (1). By 2023 it had over 45,000 women, 83 branches and a turnover of ₹1,600 crore, with scholarships and transport for members' children (1).", "M"),
W("Timeline. Arrange: (i) Oberoi mortgages jewellery to buy a hotel (ii) Dandekar brothers begin with ink powder (iii) Lijjat Papad cooperative registered (iv) Oberoi receives Padma Bhushan. Give the years.", 3, "(ii) 1931; (i) 1934; (iii) 1962 (started 1959); (iv) 2001. (3 for correct order with years, 2 for order)", "M"),
W("What lessons does Mohan Singh Oberoi's story give us about entrepreneurship? Give three.", 3, "He moved from a hotel clerk earning ₹50 a month to building the Oberoi Group (1). Showed initiative and risk-taking by mortgaging his wife's jewellery in 1934 (1). Success came through managing staff, finance and quality of service (1).", "M"),
W("How did the Dandekar brothers identify and use a market opportunity?", 3, "They started in 1931 making ink powder in recycled bottles to meet the need for ink (1). They saw the need for good art materials and went to Glasgow to study colour chemistry to improve quality (1), and expanded into pencils, crayons and paints (1).", "M"),
W("Who were the Chettiars of Tamil Nadu? Why are they a good example of ethical business?", 3, "They were traders, bankers and moneylenders across India and South-East Asia (1). They lent on trust, kept good accounts (1) and reinvested profits in temples, education and welfare (1).", "M"),
W("State any three aspects that a business plan should cover, using the bakery example.", 3, "Any three: needs and idea (what people want, fresh bread); potential customers (children, families); money and costs (oven, rent, ingredients); location; human resources; pricing and profits; promotion; challenges and risks. (1 each)", "M"),
W("Why is a business plan called a 'dynamic' roadmap?", 2, "Conditions such as competition, costs and tastes change (1), so the plan must be revised from time to time to remain useful (1).", "M"),
W("Match the functional area with the bakery task: (a) management and operations (b) finance and accounting (c) human resources (d) marketing and sales with (1) hiring and training bakers (2) social media offers and discounts (3) daily production plan and quality checks (4) paying costs and recording profit and loss.", 3, "(a)-(3); (b)-(4); (c)-(1); (d)-(2). (3 for all, 2 for three)", "M"),
W("Differentiate between fixed costs and variable costs with two examples each.", 3, "Fixed costs do not change with output, e.g. rent, salaries, insurance (1.5). Variable costs change with the amount produced, e.g. raw materials, packaging (1.5).", "M"),
W("Find the mistake: 'If a bakery sells goods for ₹2,00,000, its profit is ₹2,00,000.' Correct it with an example.", 2, "Wrong (1). Profit is revenue minus all expenses; if expenses are ₹1,50,000, profit is 2,00,000 - 1,50,000 = ₹50,000 (1).", "M", wp=True),
W("The ABC Bakery earned income of ₹2,95,000 and had expenses of ₹2,22,000 in March 2026. Find the profit before tax and, after paying ₹13,000 as tax, the profit after tax.", 3, "Profit before tax = 2,95,000 - 2,22,000 = ₹73,000 (1.5). Profit after tax = 73,000 - 13,000 = ₹60,000 (1.5).", "M", wp=True),
W("What is a startup? What are unicorns? Name two sectors where Indian startups work.", 3, "A startup is a young, early-stage company with an innovative product or service (1). A unicorn is a startup valued at over 1 billion dollars (1); about 120 existed in 2025 in e-commerce, fin-tech, health-tech or agri-tech (any two, 1).", "M"),
W("Name two ways in which businesses contribute to society beyond making profit.", 2, "Any two: create jobs and income; produce goods and services; pay taxes; innovate; corporate social responsibility in education, environment or healthcare. (1+1)", "M"),
W("Explain the story 'From a Dead Mouse to Riches' as an example of entrepreneurship.", 3, "A poor youth turned a dead mouse into a fortune step by step (1). He used intelligence, hard work and spotting opportunities (1), and then shared his wealth with the community (1).", "M"),
W("Why must the four functional areas work together? Give an example.", 3, "A great idea can fail if any area is weak (1.5). Example: a tasty bakery product with poor marketing will not sell, or good sales with poor accounting will hide losses (1.5).", "M"),
W("Name three hubs of startups in India and two government ideas linked to startups in the chapter.", 3, "Hubs: any three of Bengaluru, Hyderabad, Mumbai, Delhi NCR (1.5). Ideas: Startup India supporting Atmanirbhar Bharat, and the vision of Viksit Bharat 2047 (1.5).", "M"),
# ---------------- HARD ----------------
W("Case study. Rohini plans a small bakery in Jodhpur. Her fixed cost is ₹21,000 a month; each cake costs ₹50 in materials and sells for ₹120. (i) How much does each cake add towards covering fixed costs? (ii) How many cakes must she sell to just cover all costs? (iii) What is her profit at 500 cakes?", 4, "(i) 120 - 50 = ₹70 (1). (ii) 21,000 ÷ 70 = 300 cakes (1.5). (iii) Revenue 500 × 120 = ₹60,000; cost 21,000 + 25,000 = ₹46,000; profit ₹14,000 (1.5).", "H", wp=True),
W("Case study. Using the ABC Bakery data (income: bread 1,20,000, pastries 75,000, cakes 85,000, delivery 15,000; expenses: materials 1,00,000, packaging 12,000, rent 40,000, salaries 30,000, utilities 15,000, advertising 8,000, miscellaneous 7,000, interest 10,000), find the total income and expenses and name two ways to raise profit.", 4, "Total income = 2,95,000 (1). Total expenses = 2,22,000 (1). Profit before tax = ₹73,000 (0.5). Ways: reduce expenses such as materials or utilities, raise sales through marketing, add products or delivery, adjust prices (any two, 1.5).", "H", wp=True),
W("Lijjat's turnover was ₹1,600 crore with over 45,000 women members in 2023. (i) Find the average turnover per member in lakh rupees (1 crore = 100 lakh). (ii) What does it say about cooperative enterprise?", 4, "(i) 1,600 crore = 1,60,000 lakh; ÷ 45,000 = about ₹3.6 lakh per member (2). (ii) A cooperative with equal ownership and profit sharing can create livelihoods for thousands of women and a big business from a tiny start of ₹80 (2).", "H", wp=True),
W("Compare Lijjat Papad and the Oberoi Group as routes to entrepreneurial success on starting capital, who owns it, the risks taken and the lesson.", 4, "Lijjat: ₹80, seven homemakers, equal owners sharing profits, risk shared, lesson of grit, unity and quality (2). Oberoi: one individual who mortgaged his wife's jewellery, personal risk-taking, built a hotel group by managing staff, finance and quality; lesson of initiative (2).", "H"),
W("Case study. A group of students wants to sell lemonade at the school fair. Prepare a short business plan covering needs, customers, costs and sources of money, price and promotion, and risks.", 5, "One mark each: need (cool drinks in summer) and idea; customers (students, parents, teachers); costs (lemons, sugar, cups, stall) and money from savings or school fund; price to cover costs and give profit; promotion by posters and announcements; risk (rain, unsold stock, competition).", "H", wp=True),
W("Case study. A bakery has great products but its sales are falling and its staff keep leaving. Which functional areas are weak? Suggest two actions for each.", 4, "Marketing and sales (falling sales): use social media, offers, packaging, online ordering (2). Human resources (staff leaving): hiring, training, motivating and fair pay (2).", "H", wp=True),
W("Explain, with examples, how the knowledge of finance and accounting helps an entrepreneur decide whether the business is succeeding.", 4, "Finance gets funds and uses them wisely, e.g. loan or savings for an oven (1). Accounting records money flows so the owner knows performance (1). A profit and loss account shows income minus expenses, e.g. ₹73,000 profit before tax for ABC Bakery (1), and cash flow shows whether bills can be paid, helping decide on prices, costs and expansion (1).", "H"),
W("'Entrepreneurs create value for society.' Support this with three examples from the chapter.", 4, "Lijjat gave livelihoods and self-reliance to over 45,000 women and supports education of children (1.5). The Oberoi Group built a hotel business employing many people (1). The Dandekar brothers improved quality of ink and art materials (1). Chettiars reinvested profits in temples, education and welfare (0.5).", "H"),
W("HOTS. Why do many startups fail, yet India encourages startups? Give three reasons.", 3, "New ideas are risky and failure is part of learning (1). Startups create jobs, income and innovation, and some become unicorns (1). Policies such as Startup India support self-reliance (Atmanirbhar Bharat) and Viksit Bharat 2047 (1).", "H"),
W("The Chettiars lent money on trust, and reinvested profits in temples, education and welfare. Explain why trust and ethics are important for a business and give one modern example.", 3, "Customers, lenders and suppliers deal with a business they trust, so ethics bring repeat business and long-term growth (1.5). Example: a bakery that uses safe ingredients and honest billing, or a bank that keeps accurate accounts (1.5).", "H", wp=True),
W("Case study. Suresh wants to start a tiffin service from his home in Kota. Identify his possible customers, two fixed costs, two variable costs, and a risk. Calculate profit if he serves 600 meals at ₹60 with ₹30 variable cost per meal and fixed costs ₹9,000.", 5, "Customers: students, working people (0.5). Fixed: rent, salary of helper, equipment (any two, 0.5); variable: food ingredients, packaging, fuel (any two, 0.5); risk: change in demand, rising prices (0.5). Revenue = 600 × 60 = ₹36,000; variable cost = 600 × 30 = ₹18,000; total cost = 27,000; profit = ₹9,000 (3).", "H", wp=True),
W("Describe how a business supports national goals such as Atmanirbhar Bharat and Viksit Bharat 2047.", 3, "Businesses and startups make goods and services within the country, reduce dependence on others and create jobs (1.5). They bring innovation and pay taxes, supporting growth towards a developed India by 2047 (1.5).", "H"),
W("Essay. 'From idea to venture.' Describe the steps and skills needed to convert an idea into a successful business, using the stories and the business plan.", 5, "Identify a problem or opportunity (as the Dandekar brothers did) and the customers (1). Plan the business: costs, money, location, people, pricing, promotion and risks (1). Take a risk and mobilise resources (Oberoi, Lijjat) (1). Run the four functional areas well and track profit (1). Learn from failures and contribute to society (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "Timeline and Key Numbers"),
 ("table", ["Date / figure", "Event"], [
  ["1898", "Mohan Singh Oberoi born in Punjab"],
  ["1931", "Dandekar brothers start with ink powder"],
  ["1934", "Oberoi mortgages his wife's jewellery to buy a hotel"],
  ["1959", "Lijjat Papad started by seven women with ₹80"],
  ["1962", "Lijjat registered as Shri Mahila Griha Udyog Lijjat Papad"],
  ["2001 / 2002", "Oberoi gets the Padma Bhushan / passes away"],
  ["2020", "Atmanirbhar Bharat policy of self-reliance"],
  ["2023", "Lijjat: over 45,000 women, 83 branches, ₹1,600 crore turnover"],
  ["2025", "About 120 unicorns in India; third-largest startup ecosystem"],
  ["2047", "Target year of Viksit Bharat"]]),
 ("h2", "Key Terms"),
 ("table", ["Term", "Meaning"], [
  ["**Entrepreneur**", "Person who turns an idea into a venture and takes the risk"],
  ["**Factors of production**", "Land, labour, capital, technology"],
  ["**Revenue / income**", "Money earned from sales"],
  ["**Profit / loss**", "Revenue minus expenses, positive / negative"],
  ["**Fixed and variable costs**", "Do not change with output / change with output"],
  ["**Business plan**", "Written roadmap of goals and steps"],
  ["**Cooperative**", "Business owned by members who share profit equally"],
  ["**Mortgage, chawl**", "Loan against property; tenement of single-room units"],
  ["**Startup, unicorn**", "Young innovative company; startup valued over 1 billion dollars"],
  ["**CSR**", "Corporate social responsibility: help to society in education, environment, healthcare"]]),
 ("h2", "Worked Examples"),
 ("steps", [
  ("Example 1 — Cost and cost per cake", "Rent ₹40,000; materials ₹10 × 1,000 cakes = ₹10,000; total ₹50,000; per cake ₹50."),
  ("Example 2 — Profit", "500 cakes at ₹120 = ₹60,000. Cost = 20,000 + 50 × 500 = ₹45,000. Profit = ₹15,000."),
  ("Example 3 — Bakery account", "Income ₹2,95,000 - expenses ₹2,22,000 = ₹73,000; tax ₹13,000; profit after tax ₹60,000. Profit margin = 73 ÷ 295 ≈ 24.7%."),
  ("Example 4 — Cakes needed to cover costs", "Fixed ₹21,000; each cake gives 120 - 50 = ₹70 over its cost; 21,000 ÷ 70 = 300 cakes.")]),
 ("h2", "Comparison: The Four Stories"),
 ("table", ["Entrepreneur", "Idea / opportunity", "Resources and risk", "Result"], [
  ["Lijjat Papad", "Extra income by making papad", "₹80, borrowed equipment, shared risk", "Cooperative with 45,000+ women"],
  ["Mohan Singh Oberoi", "Hotels, learned as a clerk", "Mortgaged wife's jewellery", "Oberoi Group; Padma Bhushan"],
  ["Dandekar brothers", "Ink powder, art materials", "Studied in Glasgow", "Pencils, crayons, paints"],
  ["Chettiars", "Trade and banking", "Trust-based lending", "Wealth reinvested in welfare"]]),
 ("h2", "Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["A need or problem is identified", "A business idea and then a venture"],
  ["Weak marketing or finance", "A good product fails"],
  ["Costs not tracked", "Losses go unnoticed"],
  ["Equal ownership and profit sharing (Lijjat)", "Unity and commitment among members"],
  ["Startups grow and create jobs", "Support for Atmanirbhar Bharat and Viksit Bharat 2047"]]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "Profit = revenue - **all** expenses, not revenue minus materials only. Rent and salaries are fixed costs even if sales are low."),
 ("note", "REMEMBER", "Lijjat began in 1959 but was registered in 1962. Do not confuse the Dandekar brothers (ink, 1931) with Oberoi (hotels, 1934)."),
 ("h2", "More Likely Questions"),
 ("qa", [
  ("How does entrepreneurship impact society and the economy? (5 marks)", "Entrepreneurs spot problems and create products and services, give jobs and income, pay taxes, bring innovation and help the community through welfare and CSR. Lijjat gave livelihoods to 45,000 women; the Oberoi Group built a hotel industry; the Chettiars funded temples and education."),
  ("Why is it important to have a business plan? (3 marks)", "It guides decisions, sets priorities, shows the money needed and the risks, and helps the business grow. It is revised as conditions change."),
  ("Explain the functional areas of a business. (5 marks)", "Management and operations plan and run production and delivery; finance and accounting raise funds and record transactions; human resources hire, train and motivate people; marketing and sales build awareness and increase sales. All four must work together."),
  ("What is the difference between profit and revenue? (2 marks)", "Revenue is the total money earned from sales; profit is what is left after subtracting all costs."),
 ]),
]
CH["takeaways"] += ["Calculation drills: **Profit = revenue - expenses**; **total cost = fixed + variable × units**; cakes to cover fixed cost = fixed ÷ (price - variable cost).",
  "Remember: **₹80, 1959, 1962** (Lijjat); **1934, Padma Bhushan 2001** (Oberoi); **1931, Glasgow** (Dandekar); **about 120 unicorns in 2025**."]

if __name__ == "__main__": run(__file__, BANK, 9, "Social_Science", WS, CH)
