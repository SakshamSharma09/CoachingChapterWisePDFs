"""Class 9 SST Ch 13 Managing Your Personal Finances - Hard-tier extras (AR, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("Compounding benefits the person who starts investing early.", "Returns earn further returns over a longer period.", "a",
     "Interest on interest accumulates over more years for an early investor."),
 AR4("Insurance works on the principle of risk sharing.", "A premium is the amount paid for insurance.", "b",
     "Both are true but the second does not explain why insurance is risk sharing."),
 AR4("Rs 10,000 invested at 10% compound interest for 2 years becomes Rs 12,100.", "Compound interest is calculated only on the original principal.", "c",
     "10,000 x 1.1 x 1.1 = 12,100 so A is true; compound interest is on principal and earlier interest, so R is false."),
 AR4("Indirect taxes are paid directly on a person's income.", "GST is an indirect tax.", "d",
     "Indirect taxes are paid on goods and services, not directly on income, so A is false; R is true."),
 AR4("Inflation reduces purchasing power.", "Prices of goods and services rise over time.", "a",
     "With rising prices the same money buys less."),
 AR4("A progressive tax system taxes higher incomes at higher rates.", "GST is levied on goods and services.", "b",
     "Both are true but GST is not an example of progressive taxation."),
]

CASE = [
 Q("<b>Case study.</b> Meena earns Rs 40,000 a month and spends Rs 32,000 on food, rent, school fees and other needs. She keeps a monthly budget. She wants to buy a Rs 24,000 laptop in 6 months by saving equal amounts each month. "
   "(i) How much does she save in a month? (ii) What percentage of her income is this? (iii) How much must she save each month for the laptop? (iv) What is a budget, and how does it help her?",
   "(i) Rs 40,000 - Rs 32,000 = Rs 8,000 (1). (ii) 8,000/40,000 x 100 = 20% (1). (iii) 24,000/6 = Rs 4,000 per month (1). (iv) A budget is a written plan that balances income and expenses (1); it helps her track spending and set aside savings for goals (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Ravi invests Rs 10,000 at 8% simple interest for 3 years. His friend invests Rs 10,000 at 10% compound interest for 2 years. A shop sells a Rs 30,000 fridge on 12 equal monthly instalments (EMIs) of Rs 3,000. "
   "(i) Find Ravi's simple interest. (ii) Find the amount of his friend's investment after 2 years. (iii) How much is paid in all for the fridge on EMIs? (iv) How much extra is paid, and why?",
   "(i) 10,000 x 8 x 3/100 = Rs 2,400 (1). (ii) 10,000 x 1.1 x 1.1 = Rs 12,100 (1). (iii) 12 x 3,000 = Rs 36,000 (1). (iv) Rs 6,000 extra, because interest is added to the loan amount in the EMIs (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A family has health insurance under Ayushman Bharat PM-JAY and pays a premium for a general insurance cover on its cattle. The father buys shares of a company and keeps some savings in a fixed deposit. He also follows the SENSEX of the BSE. "
   "(i) What does PM-JAY provide? (ii) What do shares represent? (iii) How many companies does the SENSEX track? (iv) Why do experts advise diversification, and how do a fixed deposit and shares differ in risk?",
   "(i) Health insurance for eligible households (1). (ii) Part-ownership of a company (1). (iii) 30 large companies (1). (iv) Diversification spreads risk across assets (1); a fixed deposit gives an assured return with low risk, whereas shares carry higher risk but can give higher returns (1).", "1+1+1+2"),
]

MISTAKES = [
 "Simple interest is on the principal only: SI = P x R x T/100. Compound interest is on principal <b>and</b> earlier interest, so it is larger over 2 or more years.",
 "The five pillars are income, budgeting, saving, investing and protection; exports are not one of them.",
 "GST is an <b>indirect</b> tax (on goods and services); income tax is a direct tax. In a progressive system higher incomes pay higher rates.",
 "An EMI purchase costs <b>more</b> than the price: total paid = EMI x number of months (e.g. 12 x 3,000 = 36,000 for a 30,000 fridge).",
 "Inflation is a rise in prices, which lowers purchasing power; money kept idle in cash loses value over time.",
 "Higher risk goes with higher possible return and fixed deposits are low-risk; a premium is paid for insurance and a SENSEX is an index of the BSE.",
]
