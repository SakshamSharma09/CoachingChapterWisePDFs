from sst9.common import mcq, Q, OR, AR
from mk9 import M4, build
A = []
# --- numeric / scenario (13) ---
for gl, pr, cost, prof in [(50, 10, 320, 180), (80, 15, 900, 300), (120, 12, 1000, 440), (60, 20, 1000, 200)]:
    A.append(M4(f"At a school stall, {gl} glasses of lemonade are sold at ₹{pr} each and the total expenses are ₹{cost}. The profit is:", f"₹{prof}",
                [f"₹{gl*pr}", f"₹{prof+100}", f"₹{cost}"], "profit = revenue − expenses"))
A.append(M4("A shop earns a revenue of ₹90,000 and has expenses of ₹1,05,000 in a month. It has made a:", "loss of ₹15,000", ["profit of ₹15,000", "profit of ₹1,95,000", "loss of ₹1,05,000"], "expenses exceed revenue"))
A.append(M4("In ABC Bakery's account, total income is ₹2,95,000 and total expenses are ₹2,22,000. The profit before tax is:", "₹73,000", ["₹60,000", "₹5,17,000", "₹13,000"], "2,95,000 − 2,22,000"))
A.append(M4("If ABC Bakery pays ₹13,000 tax on a profit before tax of ₹73,000, its profit after tax is:", "₹60,000", ["₹86,000", "₹13,000", "₹73,000"], "73,000 − 13,000"))
A.append(M4("In the bakery's account, sales of bread and buns ₹1,20,000, pastries ₹75,000, cake orders ₹85,000 and delivery ₹15,000 give a total income of:", "₹2,95,000", ["₹2,80,000", "₹2,22,000", "₹3,10,000"], "sum of the four items"))
A.append(M4("Which of these is a fixed cost for a bakery?", "monthly shop rent", ["flour used", "packaging material", "sugar purchased"], "does not change with output"))
A.append(M4("Which of these is a variable cost for a bakery?", "cost of ingredients", ["monthly rent", "insurance premium", "annual licence fee"], "changes with output"))
A.append(M4("A bakery pays rent ₹40,000 (fixed) and spends ₹10 per cake on materials (variable). The total cost of making 1,000 cakes is:", "₹50,000", ["₹10,000", "₹40,000", "₹4,10,000"], "40,000 + 1,000 × 10"))
A.append(M4("Lijjat began in 1959 with ₹80 and seven women. If its 2023 turnover was ₹1,600 crore, then compared to ₹100 crore it is:", "16 times larger", ["10 times larger", "160 times larger", "equal"], "1,600 ÷ 100"))
# --- concept (22) ---
A += [
 M4("Entrepreneurship is the process of:", "converting a potential business idea into a business venture", ["only lending money", "working for a fixed salary", "collecting taxes"], "definition"),
 M4("Which task is NOT performed by an entrepreneur?", "printing currency notes", ["taking risks", "combining factors of production", "making key business decisions"], "central bank function"),
 M4("The Jataka tale of the dead mouse teaches that:", "hard work and intelligence can turn a small start into a fortune", ["luck alone brings wealth", "business needs no planning", "rich merchants are always right"], "spotting opportunity"),
 M4("Shri Mahila Griha Udyog Lijjat Papad was registered as:", "a cooperative society", ["a joint stock company", "a government department", "a foreign firm"], "members are equal owners"),
 M4("Which of these is a feature of the Lijjat model?", "profits shared equally among members", ["profits kept by the founder", "no women members", "only exports"], "cooperative ownership"),
 M4("Mohan Singh Oberoi began his career as a:", "hotel desk clerk in Shimla", ["factory owner", "banker", "teacher"], "earned ₹50 a month"),
 M4("In 1934 Mohan Singh Oberoi bought a hotel by:", "mortgaging his wife's jewellery and investing his savings", ["receiving a government grant", "winning a lottery", "selling a factory"], "a bold risk"),
 M4("A written document that is a blueprint of business goals and the steps to reach them is a:", "business plan", ["balance of trade", "tax return", "price ceiling"], "roadmap"),
 M4("While drawing up a business plan, the question ‘Who will use the product?’ relates to:", "potential customers", ["location", "human resources", "challenges and risks"], "target group"),
 M4("The question ‘Will the bakery be set up near schools or online?’ relates to:", "location", ["pricing", "promotion", "money and costs"], "where to make and sell"),
 M4("Which of the following is NOT a functional area of a business?", "national defence", ["marketing and sales", "human resources", "finance and accounting"], "four functional areas"),
 M4("Recording, organising and reporting a firm's financial transactions is:", "accounting", ["marketing", "operations", "mortgage"], "finance and accounting"),
 M4("Hiring and training bakers and cleaners is the work of:", "human resources", ["marketing and sales", "accounting", "operations"], "managing people"),
 M4("Advertising, promotions and discounts belong to:", "marketing and sales", ["human resources", "finance", "operations"], "creating awareness"),
 M4("Profit is calculated as:", "total revenue − total expenses", ["total revenue + total expenses", "expenses − revenue", "revenue × expenses"], "basic formula"),
 M4("The profit and loss account shows:", "whether a business made a profit or loss in a period", ["the number of employees", "the location of the shop", "the tax slabs"], "income statement"),
 M4("The Chettiar community of Tamil Nadu was known for:", "trade, banking and trust-based lending", ["only farming", "defence", "mining"], "traditional entrepreneurs"),
 M4("A young early-stage company with an innovative product or service is a:", "startup", ["cooperative society", "mortgage", "bond"], "definition"),
 M4("A startup valued at over 1 billion dollars is called a:", "unicorn", ["bond", "franchise", "mutual fund"], "term used in startup world"),
 M4("The Government of India's scheme to support startups is:", "Startup India", ["Make Tax India", "Close India", "Loan Yatra"], "supports Atmanirbhar Bharat"),
 M4("Which city is mentioned as a major startup hub?", "Bengaluru", ["Shimla", "Leh", "Imphal"], "Bengaluru, Hyderabad, Mumbai, Delhi NCR"),
 M4("‘Viksit Bharat 2047’ refers to the vision of:", "making India a fully developed nation by 2047", ["ending taxes by 2047", "building 47 cities", "adopting a new constitution"], "100 years of independence"),
]
A.append(M4("Which statement about functional areas of a business is correct?", "they work together for the success of the business", ["only finance matters", "each works in isolation", "marketing alone ensures profit"], "all four are interdependent"))
A = A[:35]
A += [
 AR("A business plan should be reviewed from time to time.", "Costs, customers and competition keep changing.", "a", "dynamic roadmap"),
 AR("An entrepreneur takes risks.", "A business venture always guarantees profit.", "c", "A true, R false"),
 AR("Failure can be a learning experience for an entrepreneur.", "Every unsuccessful attempt offers lessons for better ventures.", "a", "R explains A"),
 AR("A weak finance department cannot harm a business with a great idea.", "Functional areas work independently of each other.", "d", "A and R false; areas work together"),
 AR("Startups contribute to economic growth.", "They create jobs, innovations and solutions to real problems.", "a", "contribution of startups"),
]
assert len(A) == 40, len(A)
B = [
 Q("What is entrepreneurship?", "The process through which a person or group turns a potential business idea into a business venture, identifying opportunities and creating value (2).", "2"),
 Q("Name any four tasks performed by an entrepreneur.", "Takes risks, combines factors of production, identifies a problem and solves it, makes key decisions, contributes to society (½ each).", "2"),
 Q("What did the Jataka story ‘From a Dead Mouse to Riches’ teach?", "Spotting opportunity, starting small and working hard with intelligence can build wealth, and success should be shared with society (2).", "2"),
 Q("Why is the Lijjat Papad enterprise called a cooperative?", "Every member is an equal owner and profits are shared equally (2).", "2"),
 Q("State two ways in which Lijjat helped its women members.", "It gave financial independence and provided scholarships for children and transport facilities (1+1).", "1+1"),
 Q("What risk did Mohan Singh Oberoi take in 1934?", "He mortgaged his wife's jewellery and invested all his savings to buy a small hotel (2).", "2"),
 Q("What is a business plan?", "A written document that is a blueprint of the goals of a business and the steps to achieve them (2).", "2"),
 Q("List any four aspects explored in a business plan.", "Needs and idea, potential customers, money and costs, location, human resources, pricing and profits, promotion, challenges and risks (½ each).", "2"),
 Q("Name the four functional areas of a business.", "Management and operations, finance and accounting, human resources, and marketing and sales (2).", "2"),
 Q("Distinguish fixed cost from variable cost.", "Fixed cost does not change with output, e.g. rent (1); variable cost changes with output, e.g. raw materials (1).", "1+1"),
 Q("What is the profit and loss account?", "A statement that shows revenue, expenses and whether the business made a profit or loss over a period (2).", "2"),
 Q("Write the formula for profit. A stall earns ₹800 and spends ₹550; find the profit.", "Profit = total revenue − total expenses (1); ₹800 − ₹550 = ₹250 (1).", "1+1"),
 Q("What is the role of the human resources function?", "Hiring, training and motivating staff and building a strong team (2).", "2"),
 Q("Why are the Chettiars an example of a traditional entrepreneurial community?", "They were traders and bankers in India and Southeast Asia known for ethics, trust-based lending and accounting skills (2).", "2"),
 Q("What is a startup? Name one startup field.", "A young early-stage company offering an innovative product or service (1); e.g. fin-tech, health-tech, agri-tech (1).", "1+1"),
 Q("What is Atmanirbhar Bharat?", "A national policy framework launched in 2020 to make the country self-reliant, boost domestic manufacturing and reduce import dependence (2).", "2"),
]
C = [
 Q("Explain the qualities of an entrepreneur using the stories in the chapter.", "Spots opportunities and solves problems (1); takes risks and works hard as Oberoi did (1); shares success with society (1).", "1+1+1"),
 Q("Describe how seven women started Lijjat.", "In 1959 they began on a rooftop in Mumbai with ₹80, a recipe and borrowed equipment (1½); they formed a cooperative with equal ownership and registered it in 1962 (1½).", "1½+1½"),
 Q("What problem did Lijjat solve beyond selling papads?", "It gave homemakers a source of income and independence (1½); it empowered communities and became self-reliant, with over 45,000 members by 2023 (1½).", "1½+1½"),
 Q("How did Mohan Singh Oberoi build a hospitality empire?", "He learnt every aspect of hotel work as a clerk (1); took a bold step by buying a hotel and managing staff, finances and quality (1); built a trusted luxury brand (1).", "1+1+1"),
 Q("Why is a business plan called a roadmap?", "It guides the entrepreneur from idea to launch (1½); it helps set priorities, organise resources and take decisions (1½).", "1½+1½"),
 Q("A group plans a bakery. Explain ‘needs and idea’ and ‘potential customers’.", "Study what customers need, such as fresh or healthy items (1½); identify who will buy: children, young adults or families (1½).", "1½+1½"),
 Q("For the bakery, explain ‘money and costs’ and ‘location’.", "Estimate initial investment (oven, rent, salaries, ingredients) and funding sources (1½); choose a busy place or online sales to reach customers (1½).", "1½+1½"),
 Q("Explain ‘pricing and profits’ and ‘promotion’ in a business plan.", "Prices must cover costs, give profit and stay affordable (1½); promotion uses social media, posters and offers (1½).", "1½+1½"),
 Q("What are challenges and risks in business? Give three examples.", "Threats that disrupt operations or cause losses (1); high competition, rising raw material costs, changing preferences (2).", "1+2"),
 Q("Explain management and operations with the bakery example.", "Management plans and guides resources to meet goals (1½); operations produces and delivers goods on time, choosing equipment and monitoring quality (1½).", "1½+1½"),
 Q("Explain finance and accounting.", "Finance plans, obtains and uses funds, pays fixed and variable costs and manages cash flow (1½); accounting records and reports transactions, e.g. the profit and loss account (1½).", "1½+1½"),
 Q("Distinguish revenue, expenses and profit.", "Revenue is money earned from sales (1); expenses are money spent on running the business (1); profit is revenue minus expenses (1).", "1+1+1"),
 Q("A stall sells 100 glasses at ₹12 each. Costs are lemons ₹300, sugar ₹100, glasses ₹250 and ₹50 other. Find the profit.", "Revenue = ₹1,200 (1); expenses = ₹700 (1); profit = ₹500 (1).", "1+1+1"),
 Q("Explain with examples fixed and variable costs of a bakery.", "Fixed: rent, oven and insurance, which stay constant (1½); variable: flour, sugar and packaging, which rise with production (1½).", "1½+1½"),
 Q("What are the tasks of the human resources and marketing departments?", "HR hires, trains and motivates staff (1½); marketing promotes products through names, social media and offers to increase sales (1½).", "1½+1½"),
 Q("How can an eco-friendly approach help a business?", "Recyclable packaging appeals to environmentally aware customers (1½); it reduces harm to the environment and builds brand image (1½).", "1½+1½"),
 Q("Explain the importance of failure in entrepreneurship.", "A venture may close even after honest effort (1); failures give lessons for stronger ideas later (2).", "1+2"),
 Q("State three features of India's startup ecosystem.", "Third-largest in the world (1); about 120 unicorns in 2025 in e-commerce, fin-tech, health-tech and agri-tech (1); hubs in Bengaluru, Hyderabad, Mumbai and Delhi NCR (1).", "1+1+1"),
 Q("How does the government support entrepreneurship?", "Through schemes such as Startup India (1½); aligned to Atmanirbhar Bharat to promote innovation and local solutions (1½).", "1½+1½"),
 Q("State any three ways in which businesses contribute to society and the economy.", "Create jobs and income, produce goods and services, pay taxes, make innovations, corporate social responsibility (1 each).", "1+1+1"),
 Q("What is corporate social responsibility? Give two areas.", "A business's voluntary contribution to society beyond profit (1); education, environment, healthcare (2).", "1+2"),
 Q("Why can a business fail even with a great idea if one functional area is weak?", "The areas depend on each other (1); e.g. poor finance or weak marketing stops growth despite good products (2).", "1+2"),
 Q("How did the Chettiar community use profits?", "They reinvested profits in trade, temples, education and community welfare (3).", "3"),
 Q("<b>Case study:</b> Two brothers start selling ink powder in recycled bottles in 1931, later learn colour chemistry abroad and set up a laboratory. (i) Name two qualities shown. (ii) Which functional area improved products? (iii) How did they serve society?", "(i) Innovation and willingness to take risks (1). (ii) Operations/research on quality (1). (iii) Provided good, affordable art materials to Indians (1).", "1+1+1"),
]
D = [
 Q("(i) Define entrepreneurship. (ii) Explain five tasks performed by an entrepreneur. (iii) How does an entrepreneur benefit society?", "(i) Turning an idea into a business venture (1). (ii) Takes risks; combines factors of production; identifies problems; makes key decisions; contributes to welfare (2½). (iii) Creates jobs, innovation and solutions (1½).", "1+2½+1½"),
 Q("(i) Narrate the Lijjat story briefly. (ii) Why is it an example of a successful cooperative? (iii) What can be learnt from it?", "(i) Seven homemakers in Mumbai, 1959, ₹80, papads, registered 1962 (2). (ii) Equal ownership and equal profit share; 45,000 members, 83 branches and ₹1,600 crore turnover by 2023 (2). (iii) Unity and quality can build a self-reliant enterprise (1).", "2+2+1"),
 Q("<b>Case study:</b> Mohan Singh Oberoi, born 1898, started as a ₹50-a-month clerk, mortgaged his wife's jewellery in 1934, and received the Padma Bhushan in 2001. (i) What is a mortgage? (ii) Name two qualities shown. (iii) Name two functional areas that helped. (iv) What does the story show about entrepreneurship?", "(i) A loan against collateral (1). (ii) Initiative and risk-taking (1). (iii) Human resources and operations (1). (iv) It needs planning, teamwork and management of many areas, not only an idea (2).", "1+1+1+2"),
 Q("(i) What is a business plan? (ii) Explain any four aspects with the bakery example. (iii) When should a plan be changed?", "(i) Written blueprint of goals and steps (1). (ii) Needs and idea, customers, costs, location, pricing, promotion; each described (3). (iii) When costs, customers or competition change (1).", "1+3+1"),
 Q("(i) List all eight aspects of a business plan. (ii) Explain how challenges and risks can be handled for a bakery.", "(i) Needs and idea, potential customers, money and costs, location, human resources, pricing and profits, promotion, challenges and risks (3). (ii) Manage perishable stock, ensure consistent quality, handle fluctuating demand and compete with other bakeries (2).", "3+2"),
 Q("(i) Name the four functional areas. (ii) Explain each with the bakery example. (iii) Why must they work together?", "(i) Management and operations; finance and accounting; HR; marketing and sales (1). (ii) Equipment and daily production; paying costs and recording accounts; hiring and training bakers; promotion and sales (3). (iii) Weakness in one harms the whole business (1).", "1+3+1"),
 Q("<b>Case study:</b> ABC Bakery for March 2026: income ₹2,95,000; raw materials ₹1,00,000, packaging ₹12,000, rent ₹40,000, salaries ₹30,000, utilities ₹15,000, advertising ₹8,000, miscellaneous ₹7,000 and loan interest ₹10,000; tax ₹13,000. (i) Total expenses? (ii) Profit before tax? (iii) Profit after tax? (iv) Name one fixed and one variable cost.", "(i) ₹2,22,000 (1). (ii) ₹73,000 (1). (iii) ₹60,000 (1). (iv) Fixed: rent; variable: raw materials (2).", "1+1+1+2"),
 Q("(i) What is profit? (ii) What is a profit and loss account? (iii) Why is accounting important for a business?", "(i) Money earned after paying the costs; revenue minus expenses (1). (ii) Statement of income, expenses and profit or loss over a period (2). (iii) Tracks performance, helps decisions and ensures tax compliance (2).", "1+2+2"),
 Q("(i) Distinguish fixed and variable costs with examples. (ii) A bakery has fixed cost ₹40,000 and variable cost ₹20 per cake. Find the total cost of 500 cakes.", "(i) Fixed: rent; do not change with output; variable: ingredients; change with output (3). (ii) 40,000 + 500 × 20 = ₹50,000 (2).", "3+2"),
 Q("(i) Who were the Chettiars? (ii) What made them successful? (iii) What can modern entrepreneurs learn?", "(i) A traditional trading and banking community of Tamil Nadu (1). (ii) Ethics, trust-based lending, accounting skills, reinvestment (2). (iii) Discipline, risk-taking and long-term vision (2).", "1+2+2"),
 Q("(i) Why do some startups fail? (ii) Why is failure not a disgrace? (iii) What is the quotation of Swami Vivekananda given in the chapter?", "(i) Competition, lack of funds, poor planning (2). (ii) Honest effort teaches lessons (2). (iii) ‘Arise, awake and stop not till the goal is reached’ (1).", "2+2+1"),
 Q("<b>Case study:</b> India has around 120 unicorns in 2025 in e-commerce, fin-tech, health-tech and agri-tech, concentrated in Bengaluru, Hyderabad, Mumbai and Delhi NCR. (i) What is a unicorn? (ii) Expand any one field named. (iii) Name a government scheme. (iv) How do startups help the economy?", "(i) A startup valued at over 1 billion dollars (1). (ii) Fin-tech means digital payments (1). (iii) Startup India (1). (iv) Create jobs, innovate and solve problems (2).", "1+1+1+2"),
 Q("(i) Explain Atmanirbhar Bharat and Viksit Bharat 2047. (ii) How can entrepreneurship contribute to them?", "(i) Self-reliance policy of 2020; vision of a developed India by 2047 (2). (ii) Employment, innovation, local production and community empowerment (3).", "2+3"),
 Q("(i) State six ways in which businesses contribute to society and the economy. (ii) Explain corporate social responsibility.", "(i) Quality of life, jobs and income, taxes, goods and services, innovations, CSR (3). (ii) Businesses give back to society through education, environment and healthcare (2).", "3+2"),
 Q("(i) Why is innovation alone not enough for success? (ii) Which functional area would you prioritise for a new bakery and why?", "(i) Needs finance, people, operations and marketing as well (2). (ii) Any reasoned choice such as finance for steady cash flow or operations for quality (3).", "2+3"),
 Q("<b>Case study:</b> A student group runs a lemonade stall: 100 glasses sold at ₹15, expenses ₹1,100. (i) Find revenue. (ii) Find profit. (iii) Name two functional areas involved in running it. (iv) Suggest one marketing idea.", "(i) ₹1,500 (1). (ii) ₹400 (1). (iii) Operations and finance (1). (iv) Posters, social media post or a discount offer (2).", "1+1+1+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
