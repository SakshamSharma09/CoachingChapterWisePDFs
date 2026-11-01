from sst9.common import mcq, Q, OR, AR
from mk9 import M4, build
A = []
# --- numeric / scenario (14) ---
for amt, rate, ans in [(500, 8, 540), (2000, 5, 2100), (1000, 6, 1060), (800, 10, 880)]:
    A.append(M4(f"₹{amt:,} is put in a savings scheme that earns {rate}% interest a year. The amount after one year is:", f"₹{ans:,}",
                [f"₹{amt+rate:,}", f"₹{amt:,}", f"₹{ans+amt//10:,}"], "principal + interest for one year"))
A.append(M4("A bond worth ₹10,000 pays 5% interest per year. The interest received after one year is:", "₹500", ["₹50", "₹5,000", "₹1,000"], "5% of 10,000"))
A.append(M4("A bond worth ₹20,000 pays 6% interest per year. The total received at maturity after one year is:", "₹21,200", ["₹1,200", "₹20,600", "₹26,000"], "20,000 + 1,200"))
A.append(M4("To save ₹3,000 in six months for a bicycle, a child must save every month:", "₹500", ["₹300", "₹600", "₹1,000"], "3,000 ÷ 6"))
A.append(M4("Ravi wants to save ₹12,000 in 8 months. The monthly saving required is:", "₹1,500", ["₹1,200", "₹2,000", "₹1,000"], "12,000 ÷ 8"))
A.append(M4("A refrigerator costing ₹30,000 is bought on EMI of ₹3,000 for 12 months. The extra amount paid is:", "₹6,000", ["₹3,000", "₹36,000", "₹30,000"], "36,000 − 30,000"))
A.append(M4("A family has an income of ₹1,00,000 and saves ₹20,000 first. By the rule Expenses = Income − Savings, the money available for spending is:", "₹80,000", ["₹20,000", "₹1,20,000", "₹70,000"], "save first, spend the rest"))
A.append(M4("₹10,000 is invested for 2 years at 10% compound interest per year. The final amount is:", "₹12,100", ["₹12,000", "₹11,000", "₹12,200"], "10,000 × 1.1 × 1.1"))
A.append(M4("A person has a taxable income of ₹3,80,000 under the slabs given in the chapter. The income tax payable is:", "nil", ["₹19,000", "₹3,800", "₹38,000"], "up to ₹4 lakh is exempt"))
A.append(M4("Using the slab rates of the chapter, the tax on a taxable income of ₹8,00,000 is:", "₹20,000", ["₹40,000", "₹80,000", "nil"], "5% of ₹4 lakh"))
A.append(M4("A salaried person earns ₹9,75,000 and gets a standard deduction of ₹75,000. The taxable income is:", "₹9,00,000", ["₹9,75,000", "₹10,50,000", "₹75,000"], "salary − deduction"))
# --- concept (22) ---
A += [
 M4("Personal finance means:", "planning and managing an individual's money to meet needs and wants", ["only borrowing from banks", "the finances of a government", "printing of currency"], "definition"),
 M4("Which of the following is NOT one of the five pillars of personal finance?", "exports", ["income", "budgeting", "protection and risk management"], "five pillars: income, budgeting, saving, investing, protection"),
 M4("Rent received from letting out a house is an example of:", "income", ["budgeting", "insurance", "inflation"], "regular receipt of money"),
 M4("A written plan that balances income and expenses is called a:", "budget", ["premium", "bond", "dividend"], "budgeting"),
 M4("Which is the FIRST step in budgeting?", "identify your expenses", ["review and adjust the budget", "track your spending", "buy insurance"], "list all expenses"),
 M4("Comparing actual spending with the budget is the step of:", "tracking your spending", ["setting a savings goal", "identifying expenses", "filing tax returns"], "step 3"),
 M4("Keeping aside a part of income for future use is:", "saving", ["borrowing", "taxation", "spending"], "financial surplus"),
 M4("Putting savings into assets to protect their value and earn returns is:", "investing", ["budgeting", "borrowing", "paying a premium"], "wealth growth"),
 M4("The rise in prices of goods and services over time is called:", "inflation", ["liquidity", "compounding", "maturity"], "reduces purchasing power"),
 M4("How quickly an asset can be converted into cash without losing value is its:", "liquidity", ["risk", "maturity", "premium"], "definition"),
 M4("Earning returns on both the principal and the returns already earned is called:", "compounding", ["inflation", "diversification", "taxation"], "interest on interest"),
 M4("Bhavisha starts saving ₹1,000 a year at 25 and Dhruv at 35. At 65 Dhruv has about 40% of Bhavisha's amount because:", "compounding gave her money more time to grow", ["he saved less every year", "he paid more tax", "she earned a higher rate"], "the power of early investing"),
 M4("The safest investment option listed in the chapter is:", "a fixed deposit", ["shares", "a mutual fund", "a speculative scheme"], "assured returns"),
 M4("In a bond the investor:", "lends money to the government or a company", ["becomes a part-owner of the company", "pays an insurance premium", "pays income tax"], "bondholder earns interest"),
 M4("Buying shares makes a person:", "a part-owner of the company", ["a lender to the government", "an insurer", "a tax collector"], "equity"),
 M4("The BSE SENSEX tracks the performance of:", "30 large and actively traded companies", ["all banks in India", "50 small firms", "government bonds"], "benchmark index"),
 M4("Mutual funds reduce risk mainly through:", "portfolio diversification", ["fixed interest only", "guaranteed returns", "avoiding all shares"], "spreading across assets"),
 M4("The regular amount paid to an insurance company is called the:", "premium", ["dividend", "EMI", "principal"], "insurance contract"),
 M4("Crop insurance protects farmers against:", "losses from disasters, pests and price changes", ["rise in fertiliser tax", "bank holidays", "income tax"], "general insurance"),
 M4("Ayushman Bharat PM-JAY is a government scheme providing:", "health insurance to eligible low-income households", ["crop loans", "life insurance for all", "tax rebates"], "health cover"),
 M4("GST is an example of a:", "indirect tax", ["direct tax", "bond", "premium"], "added to price of goods"),
 M4("Under progressive taxation:", "higher incomes are taxed at higher rates", ["all incomes pay the same rate", "poor people pay more", "no one pays tax"], "reduces inequality"),
]
# --- assertion-reason (replace last few concept items to keep 40) ---
A = A[:35]
A += [
 AR("Keeping savings only in a piggy bank may reduce their purchasing power.", "Inflation raises prices of goods over time.", "a", "cash earns no return while prices rise"),
 AR("Insurance works on the principle of risk sharing.", "Many people pay premiums into a common pool from which losses are met.", "a", "pooled premiums"),
 AR("Shares are suitable for every investor.", "Share prices fluctuate with market conditions.", "d", "A is false; shares are risky"),
 AR("A fixed deposit offers assured returns.", "The interest rate of an FD changes every day during its tenure.", "c", "A true, R false: rate stays fixed"),
 AR("Higher potential returns usually come with higher risk.", "Fixed deposits offer higher returns than shares.", "c", "A true, R false"),
]
assert len(A) == 40, len(A)
B = [
 Q("What is personal finance?", "The planning and management of an individual's money to meet needs and wants, including how much to spend, save and invest (2).", "2"),
 Q("Name the five pillars of personal finance.", "Income, budgeting, saving, investing, and protection and risk management (2).", "2"),
 Q("What is a budget? State one benefit.", "A written plan that balances income and expenses (1); it controls unnecessary spending (1).", "1+1"),
 Q("Why should a budget be reviewed from time to time?", "Income, costs and goals change, for example rising transport costs, so regular review keeps it realistic (2).", "2"),
 Q("Why do people save money?", "To meet emergencies and future needs and to invest in assets (2).", "2"),
 Q("Distinguish saving from investing.", "Saving is keeping aside part of income (1); investing puts savings into assets to earn returns (1).", "1+1"),
 Q("What is inflation? How does it affect purchasing power?", "A rise in prices over time (1); the same money buys fewer goods, so purchasing power falls (1).", "1+1"),
 Q("Define compounding.", "Returns earned not only on the principal but also on the returns already earned, so money grows faster over time (2).", "2"),
 Q("What is a fixed deposit? Why is it considered safe?", "A lump sum deposited with a bank or post office for a fixed period (1); it pays assured interest at a fixed rate (1).", "1+1"),
 Q("What is a bond?", "A loan given to the government or a company for a fixed period in return for regular interest and repayment of principal at maturity (2).", "2"),
 Q("What is a mutual fund?", "A fund that pools money of many investors and invests it in shares, bonds and other assets, managed by professionals (2).", "2"),
 Q("What is insurance? Name the payment made for it.", "A contract under which the insurer compensates specified losses (1); the payment is the premium (1).", "1+1"),
 Q("Name any two types of general insurance.", "Motor insurance, property insurance, crop insurance or cattle insurance (1+1).", "1+1"),
 Q("What is an EMI?", "Equated monthly instalment: the fixed amount paid every month to repay a loan, covering principal and interest (2).", "2"),
 Q("Distinguish direct taxes from indirect taxes with an example each.", "Direct taxes are paid directly on income, e.g. income tax (1); indirect taxes are added to the price of goods, e.g. GST (1).", "1+1"),
 Q("What is progressive taxation?", "A system in which the tax rate rises as income rises, so richer people pay a larger share (2).", "2"),
]
C = [
 Q("Explain the meaning of income with three examples.", "Income is money received regularly or occasionally for goods sold or services rendered (1); salary of a teacher, profit of a shopkeeper, rent from property (2).", "1+2"),
 Q("State the four questions that help in setting a financial goal.", "What do I want to achieve? How much money will I need? By when? What steps will help me reach it? (3/4 mark each, awarded as 3).", "3"),
 Q("Explain the four steps in budgeting.", "Identify expenses (¾); set a savings goal (¾); track spending (¾); review and adjust the budget (¾).", "3"),
 Q("Ria wants to buy a ₹3,000 bicycle in six months. How much must she save monthly? Why does a goal make saving easier?", "₹3,000 ÷ 6 = ₹500 per month (1½); a clear goal with an amount and date motivates regular saving (1½).", "1½+1½"),
 Q("Why is saving important even for people with low incomes?", "Life is uncertain and emergencies arise (1½); even small regular savings build a surplus for future needs and investments (1½).", "1½+1½"),
 Q("Priya keeps ₹500 in a piggy bank and Sameer invests it at 8% a year. Compare their position after one year.", "Priya still has ₹500 (1); Sameer has ₹540 (1); investing earned a return and protects against inflation (1).", "1+1+1"),
 Q("Explain how inflation reduces the value of money, using the school bag example.", "A bag costing ₹1,000 may cost ₹1,060 after a year at 6% inflation (1½); money lying idle buys less, so purchasing power falls (1½).", "1½+1½"),
 Q("Explain the idea of compounding with the example of Bhavisha and Dhruv.", "Both save ₹1,000 yearly at 7%, but Bhavisha starts at 25 and Dhruv at 35 (1); returns earn further returns over a longer time, so Dhruv has only about 40% of her amount at 65 (2).", "1+2"),
 Q("Explain fixed deposits and small savings schemes as investment options.", "FDs give fixed, assured interest for a fixed period (1½); PPF, NSC and Sukanya Samriddhi Yojana are government-backed safe long-term schemes (1½).", "1½+1½"),
 Q("A ₹10,000 bond pays 5% a year and matures in a year. Find the interest and total received. Why are government bonds considered safer?", "Interest ₹500 and total ₹10,500 (1½); the government is less likely to default than a company (1½).", "1½+1½"),
 Q("Why do shares carry higher risk but also higher potential return?", "Share prices fluctuate with market conditions, company performance and the economy (1½); over the long term they can give higher returns through dividends and price rise (1½).", "1½+1½"),
 Q("How do mutual funds help investors who lack time or knowledge?", "Money is pooled and invested by professional fund managers (1½); diversification across assets reduces risk, though returns are not guaranteed (1½).", "1½+1½"),
 Q("Explain the four factors to consider before investing.", "Risk, return, time horizon and liquidity (¾ each, awarded as 3).", "3"),
 Q("Explain the risk–return trade-off with examples.", "Low-risk options such as FDs give lower returns (1½); higher-risk options such as shares may give higher returns (1½).", "1½+1½"),
 Q("How does insurance provide financial security?", "Premiums are pooled and losses are compensated (1); it reduces the impact of accidents, illness and damage, helps families recover and encourages saving (2).", "1+2"),
 Q("Distinguish health insurance from life insurance.", "Health insurance covers hospital and treatment expenses (1½); life insurance supports the family if the policyholder dies (1½).", "1½+1½"),
 Q("Describe crop insurance and cattle insurance.", "Crop insurance compensates farmers for losses due to disasters, pests and price changes (1½); cattle insurance covers loss from the death or disability of animals (1½).", "1½+1½"),
 Q("When is borrowing helpful and when is it harmful? Give examples.", "Productive borrowing such as an education loan helps (1½); borrowing for unnecessary goods causes a debt burden (1½).", "1½+1½"),
 Q("A family buys a ₹30,000 refrigerator on EMI of ₹3,000 for 12 months. Find the extra cost. Why may too many EMIs be harmful?", "Total ₹36,000, so ₹6,000 extra (1½); fixed monthly payments reduce savings and the emergency fund (1½).", "1½+1½"),
 Q("Why are taxes levied? Name the two main types.", "To fund public services such as schools, hospitals, roads and defence (1); direct and indirect taxes (2).", "1+2"),
 Q("Explain the slab system of income tax.", "Taxable income is divided into slabs, each taxed at a specified rate (1½); only the portion within a slab is taxed at that slab's rate, and rates rise with income (1½).", "1½+1½"),
 Q("Sai's taxable income is ₹3,80,000 and Meena's is ₹6,00,000. Find the tax of each under the chapter's slabs.", "Sai: nil as income is up to ₹4 lakh (1); Meena: 5% of ₹2,00,000 = ₹10,000 (2).", "1+2"),
 Q("Why is paying tax honestly the responsibility of every citizen?", "Tax revenue funds public services and development (1½); honest payment lets the government serve everyone fairly (1½).", "1½+1½"),
 Q("<b>Case study:</b> Arjun receives ₹2,000 as gifts. He spends ₹500, saves ₹500 in a piggy bank and invests ₹1,000 at 6% a year. (i) How much does he have from the investment after a year? (ii) Which part loses purchasing power? (iii) Name the pillar for the ₹1,000.", "(i) ₹1,060 (1). (ii) The money in the piggy bank (1). (iii) Investing (1).", "1+1+1"),
]
D = [
 Q("(i) Define personal finance. (ii) Explain the five pillars with an example each.", "(i) Planning and managing an individual's money for needs and wants (1). (ii) Income: salary; budgeting: monthly plan for rent and food; saving: money set aside for emergencies; investing: buying a bond or FD; protection: health insurance (4).", "1+4"),
 Q("(i) What is a budget? (ii) Describe the four steps of budgeting. (iii) State two benefits of budgeting.", "(i) A written plan balancing income and expenses (1). (ii) Identify expenses, set a savings goal, track spending, review and adjust (2). (iii) Controls unnecessary spending, helps live within means and prioritise (2).", "1+2+2"),
 Q("<b>Case study:</b> The Sharma family has an income of ₹1,00,000. They save ₹20,000 first and invest ₹30,000 at 8% compound interest per year for 5 years (amount ≈ ₹44,080). (i) How much can they spend? (ii) Interest earned? (iii) Name the principle. (iv) Why is saving first useful?", "(i) ₹80,000 (1). (ii) About ₹14,080 (1). (iii) Compounding (1). (iv) It ensures money is kept for future needs and emergencies before spending (2).", "1+1+1+2"),
 Q("(i) Why is saving alone not enough to build wealth? (ii) Explain with the example of inflation. (iii) How does investing help?", "(i) Idle money earns nothing while prices rise (1). (ii) A ₹1,000 bag costs ₹1,060 next year at 6% inflation, so the same money buys less (2). (iii) Investments earn returns that can beat inflation (2).", "1+2+2"),
 Q("(i) Explain compounding with the example of Bhavisha and Dhruv. (ii) Why do the curves in Fig. 5.4 become steeper later? (iii) What lesson does it give?", "(i) Both save ₹1,000 yearly at 7%, starting at 25 and 35; Bhavisha has about ₹1,99,635 and Dhruv about ₹94,460 at 65 (2). (ii) Returns earn returns, so growth accelerates (2). (iii) Start investing early (1).", "2+2+1"),
 Q("(i) Describe fixed deposits, bonds, shares and mutual funds. (ii) Rank them by risk.", "(i) FD: fixed assured interest; bond: loan to government or company with interest; shares: ownership with dividends and price changes; mutual fund: pooled and diversified (4). (ii) FD and government bonds lowest, mutual funds moderate, shares highest (1).", "4+1"),
 Q("<b>Case study:</b> Mohan has ₹50,000 and may choose an FD, shares or a mutual fund. He needs the money after 6 months for fees. (i) Which factor is important here? (ii) Which option suits him? (iii) Why not shares? (iv) What is the risk–return trade-off?", "(i) Time horizon and liquidity (1). (ii) A fixed deposit (1). (iii) Share prices may fall in the short term (1). (iv) Lower risk gives lower return and higher risk gives higher potential return (2).", "1+1+1+2"),
 Q("(i) What is insurance? (ii) Explain how it works. (iii) Describe health, life and general insurance.", "(i) A contract for compensation against specified losses on payment of a premium (1). (ii) Risk sharing through a common pool of premiums (1). (iii) Health: medical expenses; life: support to family on death; general: vehicles, property, crops, cattle (3).", "1+1+3"),
 Q("(i) Why do people buy insurance though they may never face a major loss? (ii) How does it encourage saving? (iii) Name a government health scheme.", "(i) To avoid heavy financial loss from uncertain events (2). (ii) Regular premiums create a habit of planning finances (2). (iii) Ayushman Bharat PM-JAY (1).", "2+2+1"),
 Q("(i) Distinguish productive and harmful borrowing. (ii) What is an EMI? (iii) A ₹30,000 fridge is bought on 12 EMIs of ₹3,000; find the extra cost and one disadvantage.", "(i) Education loan versus buying unnecessary goods (2). (ii) Fixed monthly repayment of principal plus interest (1). (iii) ₹6,000 extra; many EMIs reduce savings (2).", "2+1+2"),
 Q("(i) What are taxes and why are they collected? (ii) Distinguish direct and indirect taxes. (iii) Who administers direct tax laws in India?", "(i) Compulsory payments to the government to fund public services (2). (ii) Income tax is paid directly on income; GST is added to prices (2). (iii) The Central Board of Direct Taxes under the Ministry of Finance (1).", "2+2+1"),
 Q("<b>Case study:</b> Priya earns ₹14 lakh a year with a standard deduction of ₹75,000. (i) Find her taxable income. (ii) Find the tax using the slabs 0% up to ₹4 lakh, 5% to ₹8 lakh, 10% to ₹12 lakh, 15% to ₹16 lakh. (iii) What type of taxation is this?", "(i) ₹13,25,000 (1). (ii) 0 + ₹20,000 + ₹40,000 + 15% of ₹1,25,000 = ₹18,750; total ₹78,750 (3). (iii) Progressive taxation (1).", "1+3+1"),
 Q("(i) Explain progressive taxation and its aim. (ii) Why should citizens pay taxes honestly? (iii) What is the standard deduction?", "(i) Higher incomes taxed at higher rates to reduce inequality (2). (ii) It funds schools, hospitals, roads and security (2). (iii) A fixed amount salaried employees and pensioners may deduct before computing tax (1).", "2+2+1"),
 Q("<b>Case study:</b> A farming family earns ₹1,00,000 from crops, livestock and a small business. (i) Suggest a budget category list. (ii) Classify school fees, a new phone and better seeds as needs or wants. (iii) Which insurance should the family take? (iv) Why keep an emergency fund?", "(i) Savings, education, household, health and emergency, farm investment, festivals (1). (ii) Fees and seeds are needs; new phone is a want (2). (iii) Crop, cattle and health insurance (1). (iv) To meet uncertain events without borrowing (1).", "1+2+1+1"),
 Q("(i) Why is managing money wisely important irrespective of income? (ii) How does budgeting balance present needs and future goals?", "(i) Money is limited and needs, emergencies and goals exist at every income level (2). (ii) A budget allots money to present needs and sets aside savings for future goals (3).", "2+3"),
 Q("(i) Explain the four factors of investing: risk, return, time horizon and liquidity. (ii) How would you choose an investment for a goal five years away?", "(i) Risk is the chance of loss; return is profit; time horizon is the length of investment; liquidity is ease of conversion to cash (3). (ii) Match goal, risk tolerance and time: FD or bonds for safety, mutual funds for moderate growth (2).", "3+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
