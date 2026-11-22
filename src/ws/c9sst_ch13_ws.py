"""Class 9 Social Science Ch 13 - Managing Your Personal Finances (Economics, Part 2): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c9sst_ch13"

def _base():
    s = importlib.util.spec_from_file_location("c9sst_c13", str(REPO / "src/rn_work/c9_sst2/c13.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The quantity of goods and services that one unit of money can buy is called:", 1, "(c) purchasing power", "E", opts=["liquidity", "compounding", "purchasing power", "maturity"]),
W("A general rise in prices over time, which reduces purchasing power, is:", 1, "(a) inflation", "E", opts=["inflation", "liquidity", "premium", "dividend"]),
W("The regular payment made to an insurance company is called a:", 1, "(d) premium", "E", opts=["dividend", "tax", "principal", "premium"]),
W("A fixed monthly repayment of a loan, including principal and interest, is a(n):", 1, "(b) EMI", "E", opts=["FD", "EMI", "GST", "SIP"]),
W("Which of the following is a direct tax?", 1, "(a) income tax", "E", opts=["income tax", "GST", "sales tax on a shirt", "tax added to the price of fuel"]),
W("The BSE SENSEX tracks the share prices of:", 1, "(c) 30 large, financially sound and actively traded companies", "E", opts=["all companies in India", "only government banks", "30 large, financially sound and actively traded companies", "100 small companies"]),
W("The financial year in India runs from:", 1, "(b) 1 April to 31 March", "E", opts=["1 January to 31 December", "1 April to 31 March", "1 July to 30 June", "15 August to 14 August"]),
W("Among the following, which usually carries the highest risk and highest long-term potential return?", 1, "(d) shares", "E", opts=["fixed deposit", "government bond", "Sukanya Samriddhi account", "shares"]),
W("Define personal finance.", 2, "Personal finance is the planning and management of an individual's money to meet needs and wants: how much to spend, save and invest and how to prepare for future needs. (2)", "E"),
W("What is a budget? State one benefit of making one.", 2, "A budget is a written plan that balances income and expenses (1). It helps people prioritise needs, avoid impulse buying and live within their means (any one, 1).", "E"),
W("What is compounding?", 2, "Compounding is earning returns on both the original principal and the returns earned earlier. (2)", "E"),
W("Name two government-backed small savings schemes mentioned in the chapter.", 2, "Any two of PPF, National Savings Certificate (NSC), Sukanya Samriddhi Yojana. (1+1)", "E"),
W("Write the four steps of making a budget.", 2, "Identify expenses; set a savings goal; track spending; review and adjust. (0.5 each)", "E"),
W("State True or False, with a reason: GST is a direct tax.", 2, "False (1). GST is an indirect tax added to the price of goods and services; a direct tax like income tax is paid directly on income (1).", "E"),
W("Fill in the blank: According to the 'save first' rule, Expenses = Income - ______.", 1, "Savings (1)", "E"),
W("Name the three types of insurance given in the chapter.", 2, "Health insurance, life insurance and general insurance. (2, 1 if only two)", "E"),
W("What is liquidity of an asset?", 1, "How quickly an asset can be converted into cash without losing value. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Kavya earns ₹45,000 a month and follows the rule 'save first, spend what is left', saving 20% of income. Find her savings and her expenses.", 3, "Savings = 20% of 45,000 = ₹9,000 (1.5). Expenses = Income - Savings = 45,000 - 9,000 = ₹36,000 (1.5).", "M", wp=True),
W("Ishaan wants to buy a ₹3,000 bicycle in six months by saving equal amounts every month. How much must he save each month? Suggest one way to keep to this plan.", 3, "3,000 ÷ 6 = ₹500 per month (2). He should track spending and avoid impulse buying, or put the money in a separate account or gullak (1).", "M", wp=True),
W("Riya keeps ₹10,000 in a cupboard, while Sana puts ₹10,000 in an account at 10% compounded annually for 2 years. Find Sana's amount, and say why Riya's money may buy less after two years.", 3, "Sana: A = 10,000 × (1.10)² = ₹12,100 (1.5). Riya's money stays at ₹10,000 and prices rise with inflation, so its purchasing power falls (1.5).", "M", wp=True),
W("Why is saving alone not enough to build wealth? Explain with the term inflation.", 3, "Savings kept idle do not grow (1). Inflation raises prices, so the same money buys less (e.g. a ₹1,000 bag costs about ₹1,060 after a year at 6%) (1). Investing can earn returns that beat inflation (1).", "M"),
W("A bond of ₹20,000 pays 6% interest every year. How much interest does the investor get in one year and in 5 years? Name one issuer of bonds.", 3, "Interest per year = 6% of 20,000 = ₹1,200 (1); in 5 years = ₹6,000 (1). Bonds are issued by the government or companies (1).", "M", wp=True),
W("Distinguish between a fixed deposit and shares on risk, return and liquidity.", 3, "FD: low risk, assured but lower return, locked for a fixed period (1.5). Shares: part-ownership, the highest risk, dividends and price rise give high long-term potential, can be sold on the market (1.5).", "M"),
W("Why are mutual funds considered less risky than buying the shares of one company?", 3, "Mutual funds pool money from many investors and spread it over many shares, bonds and other assets (diversification) (1.5), managed by professionals, so a loss in one asset is balanced by others; but they are still subject to market risk (1.5).", "M"),
W("Match the term with its meaning: (a) maturity period (b) risk (c) return (d) time horizon with (1) chance of losing money (2) profit earned (3) how long money can remain invested (4) time between issue of an investment and repayment of principal.", 3, "(a)-(4); (b)-(1); (c)-(2); (d)-(3). (3 for all four, 2 for three)", "M"),
W("Explain the 'risk-return trade-off' with an example.", 3, "Lower risk investments usually give lower returns, while higher risk investments may give higher returns (1.5). Example: FD is safe with a modest return while shares are riskier but may give more (1.5).", "M"),
W("Aarav buys a ₹24,000 phone on EMI of ₹2,200 for 12 months. Find the total paid and the extra cost. Why should people be careful about too many EMIs?", 3, "Total paid = 2,200 × 12 = ₹26,400 (1); extra = ₹2,400 (1). Too many EMIs eat into income, cut savings and the emergency fund (1).", "M", wp=True),
W("What is insurance? Explain 'risk sharing' in your own words.", 3, "Insurance is a legal contract in which a person pays a regular premium and the insurer compensates specified losses (1.5). Many people pay premiums into a common pool, and the few who suffer a loss are paid from it, so risk is shared (1.5).", "M"),
W("Match the insurance with the need: (a) health (b) life (c) general with (1) family's needs if the earner dies (2) hospital bills (3) vehicle, crop, cattle or house.", 3, "(a)-(2); (b)-(1); (c)-(3). (1 each)", "M"),
W("When is borrowing helpful and when harmful? Give one example of each.", 3, "Borrowing is helpful when productive, e.g. an education loan that raises future earning (1.5); harmful when used for unnecessary goods, creating a debt burden (1.5).", "M"),
W("Difference between direct and indirect taxes with one example each, and name the board that administers direct tax laws.", 3, "Direct tax is paid directly on income or profit, e.g. income tax (1); indirect tax is added to the price of goods and services, e.g. GST (1). The Central Board of Direct Taxes (CBDT) administers direct tax laws (1).", "M"),
W("Using the new-regime slabs (up to ₹4 lakh nil; 4-8 lakh 5%; 8-12 lakh 10%), find the tax on a taxable income of ₹9,00,000.", 3, "First 4 lakh: nil. Next 4 lakh at 5% = ₹20,000 (1). Next ₹1,00,000 at 10% = ₹10,000 (1). Total = ₹30,000 (1).", "M", wp=True),
W("What is progressive taxation? Why do governments use it?", 2, "Progressive taxation means the tax rate rises as income rises (1). It makes those with higher incomes pay more and reduces inequality (1).", "M"),
W("Find the mistake: 'If Meena's taxable income is ₹9,00,000, all of it is taxed at 10%.' Correct it.", 2, "Wrong (1). Only the part of income inside each slab is taxed at that slab's rate: nil on the first ₹4 lakh, 5% on the next ₹4 lakh and 10% on the remaining ₹1 lakh (1).", "M"),
W("What is a standard deduction? Salary ₹10,75,000 with a standard deduction of ₹75,000: find the taxable income.", 2, "A fixed amount which salaried employees and pensioners may deduct before tax is calculated (1). Taxable income = 10,75,000 - 75,000 = ₹10,00,000 (1).", "M", wp=True),
W("What does the 'Earn While You Learn' idea mean? Give two examples.", 2, "Students earn some income while studying and gain skills (1). Examples: part-time work, internships, apprenticeships (1).", "M"),
# ---------------- HARD ----------------
W("Case study. Rohit's monthly income is ₹30,000. His needs (rent, food, transport, fees) are ₹16,000, wants ₹6,000, and he wants to save ₹6,000. (i) Does the budget balance? (ii) After a rise in transport costs by ₹1,500, what should he adjust? (iii) Which budget step is this?", 4, "(i) 16,000 + 6,000 + 6,000 = ₹28,000, leaving ₹2,000 spare, so it balances (1). (ii) New needs = ₹17,500, total 29,500; he can reduce wants by about ₹1,500 or use the spare ₹2,000, protecting the ₹6,000 savings (1.5). (iii) Review and adjust (1). Note: savings should be planned first (0.5).", "H", wp=True),
W("Compute the tax. Priya's salary is ₹14,00,000 and the standard deduction is ₹75,000. Using slabs: up to 4 lakh nil; 4-8 lakh 5%; 8-12 lakh 10%; 12-16 lakh 15%, find her taxable income and tax.", 5, "Taxable income = 14,00,000 - 75,000 = ₹13,25,000 (1). Tax: nil on first 4 lakh; 5% of 4 lakh = ₹20,000 (1); 10% of 4 lakh = ₹40,000 (1); 15% of ₹1,25,000 = ₹18,750 (1); total = ₹78,750 (1).", "H", wp=True),
W("Compute the tax. A shopkeeper's taxable income is ₹18,00,000. Using slabs up to 4 lakh nil; 4-8 lakh 5%; 8-12 lakh 10%; 12-16 lakh 15%; 16-20 lakh 20%, find the tax and the average rate on his income.", 5, "5% of 4 lakh = 20,000; 10% of 4 lakh = 40,000; 15% of 4 lakh = 60,000; 20% of 2 lakh = 40,000 (3). Total = ₹1,60,000 (1). Average rate = 1,60,000 ÷ 18,00,000 × 100 = 8.9% (1).", "H", wp=True),
W("Case study. Bhavisha begins investing at 25 and Dhruv at 35, both at 7% return; at age 65 Bhavisha ends with about ₹1,99,635 and Dhruv about ₹94,460. (i) How many times larger is Bhavisha's amount (nearest whole number)? (ii) Why? (iii) What lesson follows?", 4, "(i) 1,99,635 ÷ 94,460 = about 2.1 times, nearest whole number 2 (1). (ii) Her money stayed invested for 10 more years and earned returns on returns (compounding) (2). (iii) Start investing early (1).", "H", wp=True),
W("Case study. A farmer in Rajasthan wants to protect his crop and his family. Suggest two types of insurance and explain how each helps, including how the premium works.", 4, "General insurance (crop and cattle insurance) compensates losses to crops and livestock (1.5); life and health insurance protect the family if he dies or is ill, with Ayushman Bharat PM-JAY for eligible low-income households (1.5). He pays a regular premium and the insurer pays compensation for covered losses from the common pool (1).", "H", wp=True),
W("Case study. Sunita has ₹1,00,000 for 10 years. Her options: FD, shares, mutual funds. She will need it for her daughter's college. Advise her using risk, return, time horizon and liquidity.", 4, "Time horizon is long (10 years), so some risk is possible (1). Education is an important goal and cannot be lost, so she can keep a safe part in FD or small savings (1). She can put a part in mutual funds for higher return with diversification (1). She should check liquidity near the date and not put all money in shares (1).", "H", wp=True),
W("HOTS. Two friends each earn ₹25,000. One spends first and saves what remains; the other saves ₹5,000 first. Explain why the second is more likely to build wealth.", 3, "Saving first makes savings a priority rather than a leftover that is often nothing (1.5). Expenses then fit within Income - Savings, and the regular savings can be invested and compound over time (1.5).", "H"),
W("Case study. Sai's taxable income is ₹3,80,000 and Raj's is ₹6,00,000. Calculate each tax and explain what it shows about slabs.", 4, "Sai: income is below ₹4 lakh, so tax is nil (1). Raj: first 4 lakh nil, next ₹2,00,000 at 5% = ₹10,000 (2). It shows that only the portion in each slab is taxed at its rate and low incomes pay no tax (1).", "H", wp=True),
W("Evaluate: 'Borrowing on EMI to buy a ₹30,000 fridge with 12 payments of ₹3,000 is always a bad idea.' Give two points for and two against.", 4, "Against: total ₹36,000, so ₹6,000 extra (1); too many EMIs reduce savings and emergency funds (1). For: it lets the household use the fridge now and spread the cost; useful if the item is needed (1) and the instalments fit within the budget (1).", "H", wp=True),
W("Explain why investment is compared to 'planting a mango tree'. Compare Priya's ₹500 in a piggy bank with Sameer's ₹500 at 8% after one year.", 3, "A tree gives fruit for many years, just as an investment protects value and keeps giving returns (1). Priya still has ₹500 (and inflation reduces its worth), while Sameer has 500 × 1.08 = ₹540 (2).", "H", wp=True),
W("Why does the government collect taxes? Explain how citizens benefit and why honest tax paying matters.", 3, "Taxes are compulsory payments that fund schools, hospitals, transport and defence (1.5). Honest payment gives the government resources for public services for all, and since the system is progressive it helps reduce inequality (1.5).", "H"),
W("Explain how the BSE SENSEX works as a benchmark and what it shows about investing in shares over short and long periods.", 3, "SENSEX is the benchmark index of the Bombay Stock Exchange tracking 30 large, financially sound and actively traded companies (1.5). It fluctuates in the short run but tends to rise in the long run, so shares suit long time horizons and investors who can tolerate risk (1.5).", "H"),
W("Essay. 'Managing money well is a life skill.' Discuss with reference to the five pillars of personal finance.", 5, "Income: money from work and assets (1). Budgeting: a plan matching spending to income (1). Saving: surplus for emergencies and goals, save first (1). Investing: protect value against inflation and use compounding with FD, bonds, shares, mutual funds weighing risk and return (1). Protection: insurance, careful borrowing and EMIs; also paying tax (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "Key Terms and Numbers"),
 ("table", ["Term", "Meaning"], [
  ["**Income**", "Money received for goods sold or services rendered"],
  ["**Budget**", "Written plan balancing income and expenses"],
  ["**Savings**", "Part of income kept aside for future use"],
  ["**Investment**", "Putting savings into assets to protect value and earn returns"],
  ["**Inflation, purchasing power**", "Rise in prices; what a unit of money can buy"],
  ["**Compounding**", "Returns on principal and earlier returns"],
  ["**Liquidity, maturity period**", "Ease of converting to cash; time to repayment of principal"],
  ["**FD, PPF, NSC, bond, share, mutual fund**", "Investment options with different risk and return"],
  ["**SENSEX**", "Benchmark index of 30 companies on the BSE"],
  ["**Premium, insurer**", "Regular payment; the company that compensates losses"],
  ["**EMI**", "Equated monthly instalment"],
  ["**Direct / indirect tax, GST, CBDT**", "Tax on income / tax in prices / board for direct taxes"],
  ["**Standard deduction**", "Fixed amount deducted from salary income before tax"],
  ["**Progressive tax**", "Rate rises with income"]]),
 ("h2", "Worked Examples"),
 ("steps", [
  ("Example 1 — Save first", "Income ₹45,000; save 20% = ₹9,000; expenses = 45,000 - 9,000 = ₹36,000."),
  ("Example 2 — Compounding", "₹10,000 at 10% for 2 years: A = 10,000 × 1.1 × 1.1 = ₹12,100, so interest ₹2,100."),
  ("Example 3 — EMI cost", "Phone ₹24,000; 12 EMIs of ₹2,200 = ₹26,400; extra cost ₹2,400."),
  ("Example 4 — Income tax on ₹9,00,000 taxable", "4 lakh nil; 4 lakh at 5% = ₹20,000; ₹1 lakh at 10% = ₹10,000; total ₹30,000."),
  ("Example 5 — Taxable income", "Salary ₹10,75,000 - standard deduction ₹75,000 = ₹10,00,000.")]),
 ("h2", "Comparison of Investment Options"),
 ("table", ["Option", "Risk", "Return", "Liquidity / lock-in", "Suitable for"], [
  ["FD", "Low", "Fixed, modest", "Fixed period", "Safe short and medium goals"],
  ["PPF / NSC / Sukanya", "Very low (government-backed)", "Reasonable", "Long-term", "Long-term savings, e.g. girl child"],
  ["Bonds", "Low to medium", "Regular interest", "Till maturity or sale", "Steady income"],
  ["Mutual funds", "Medium, market risk", "Moderate to high", "Fairly liquid", "Those who want diversification"],
  ["Shares", "High", "High potential", "Can be sold in the market", "Long horizon and risk tolerance"]]),
 ("h2", "Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Prices rise over time", "Idle money buys less: need to invest"],
  ["Returns earned on returns", "Early investors accumulate far more"],
  ["Too many EMIs", "Less savings and emergency funds"],
  ["No insurance", "A single illness or accident can wipe out savings"],
  ["Progressive tax slabs", "Higher earners pay more, reducing inequality"]]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "Tax is not charged on the whole income at one rate: each slab is taxed at its own rate. Also deduct the standard deduction **before** applying slabs."),
 ("note", "REMEMBER", "Compound interest uses A = P(1 + r)ⁿ: for 8% write 1.08, not 0.08. Insurance premium is what you pay; the sum insured is what is paid out."),
 ("h2", "More Likely Questions"),
 ("qa", [
  ("Why is personal finance important? (3 marks)", "Money is scarce, so it must be used wisely. Planning helps meet needs and goals, avoid debt, prepare for emergencies and build wealth for a future such as a house or education."),
  ("Explain the four steps of budgeting with an example. (5 marks)", "Identify all expenses; set a savings goal, e.g. ₹3,000 in six months means ₹500 a month; track spending and compare with the budget; review and adjust when income or costs change."),
  ("What is the importance of insurance? (3 marks)", "It shares risk: many people pay premiums into a common pool and those who suffer loss are compensated, protecting savings from illness, accident or damage."),
  ("Why do we pay taxes? (3 marks)", "Taxes fund public services such as schools, hospitals, transport and defence. Income tax is progressive and uses slabs."),
 ]),
]
CH["takeaways"] += ["Calculation drills: **Expenses = Income - Savings**; **A = P(1 + r)ⁿ**; EMI cost = EMI × months; tax = sum of slab portions after the standard deduction.",
  "New-regime slabs (FY 2025-26): **nil to 4 lakh; 5%; 10%; 15%; 20%; 25%; 30% above 24 lakh**."]

if __name__ == "__main__": run(__file__, BANK, 9, "Social_Science", WS, CH)
