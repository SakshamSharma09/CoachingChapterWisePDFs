"""Class 8 Maths Ch 8 Fractions in Disguise - extras."""
from common import AR4, Q

AR = [
 AR4(r"25% of 360 is 90.", r"$x\%$ of a quantity $N$ equals $\dfrac{x}{100}\times N$.", "a",
     r"$\dfrac{25}{100}\times360=90$; R is the rule used."),
 AR4(r"A shirt marked at ₹800 is sold at a 10% discount; its selling price is ₹720.", r"Profit or loss percent is calculated on the cost price.", "b",
     r"$800-80=720$, so A is true. R is also true but concerns profit and loss, not the discount, so it does not explain A."),
 AR4(r"The compound interest on ₹1,000 at 10% per annum for 2 years is ₹210.", r"Compound interest and simple interest on the same sum for 2 years are always equal.", "c",
     r"Amount $=1000\times1.1^2=1210$, so CI $=210$ and A is true. SI would be ₹200, so R is false."),
 AR4(r"An item bought for ₹500 and sold at a loss of 20% is sold for ₹600.", r"Loss percent is calculated on the cost price.", "d",
     r"SP $=500\times0.8=400$, so A is false; R is a true statement."),
 AR4(r"The simple interest on ₹2,000 at 5% per annum for 3 years is ₹300.", r"Simple interest $=\dfrac{P\times R\times T}{100}$.", "a",
     r"$\dfrac{2000\times5\times3}{100}=300$; R is the formula used."),
 AR4(r"The compound interest on ₹5,000 at 10% per annum for 2 years is ₹1,050.", r"For the first year, simple interest and compound interest on the same principal at the same rate are equal.", "b",
     r"Amount $=5000\times1.21=6050$, CI $=1050$, so A is true. R is true but does not give the value of the two-year interest."),
]

CASE = [
 Q(r"<b>Case study.</b> Arjun buys a jacket with a marked price of ₹2,500 at a 20% discount. GST of 12% is then added on the discounted price. "
   r"(i) Find the discount. (ii) Find the price after the discount. (iii) Find the GST amount. (iv) Find the final amount Arjun pays and by how much it is less than the marked price.",
   r"(i) $20\%$ of $2500=$ ₹500 (1). (ii) $2500-500=$ ₹2,000 (1). (iii) $12\%$ of $2000=$ ₹240 (1). (iv) Final amount $=2000+240=$ ₹2,240 (1); it is ₹$2500-2240=$ ₹260 less than the marked price (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A shopkeeper in Surat buys 40 notebooks at ₹25 each. He sells 30 of them at ₹35 each and the remaining at ₹20 each. "
   r"(i) Find the total cost price. (ii) Find the selling price of the 30 notebooks. (iii) Find the selling price of the remaining notebooks. (iv) Find his overall profit or loss and the percent.",
   r"(i) $40\times25=$ ₹1,000 (1). (ii) $30\times35=$ ₹1,050 (1). (iii) $10\times20=$ ₹200 (1). (iv) Total SP $=$ ₹1,250; profit $=1250-1000=$ ₹250 (1); profit $\%=\dfrac{250}{1000}\times100=25\%$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Farmer Gurmeet takes a loan of ₹8,000 at 10% per annum. "
   r"(i) Find the simple interest for 1 year. (ii) Find the simple interest for 3 years. (iii) Find the amount payable after 2 years at compound interest. (iv) Find the difference between the compound interest and the simple interest for 2 years.",
   r"(i) $\dfrac{8000\times10\times1}{100}=$ ₹800 (1). (ii) ₹800 $\times3=$ ₹2,400 (1). (iii) $8000\times1.1^2=8000\times1.21=$ ₹9,680 (1). (iv) CI $=1680$, SI $=1600$ (1); difference ₹80 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Percentages", [
   r"$x\%=\dfrac{x}{100}$; $x\%$ of $N=\dfrac{x}{100}\times N$.",
   r"Percentage change $=\dfrac{\text{change}}{\text{original}}\times100$.",
   r"After an increase of $x\%$: $N\left(1+\dfrac x{100}\right)$; after a decrease: $N\left(1-\dfrac x{100}\right)$."]),
 ("Profit, loss, discount", [
   r"Profit $=$ SP $-$ CP (if SP $>$ CP); Loss $=$ CP $-$ SP (if CP $>$ SP).",
   r"Profit% $=\dfrac{\text{Profit}}{\text{CP}}\times100$; Loss% $=\dfrac{\text{Loss}}{\text{CP}}\times100$.",
   r"Discount $=$ MP $-$ SP; Discount% $=\dfrac{\text{Discount}}{\text{MP}}\times100$.",
   r"GST: price with GST $=$ price before tax $\times\left(1+\dfrac{\text{rate}}{100}\right)$."]),
 ("Simple interest", [
   r"$SI=\dfrac{P\times R\times T}{100}$; Amount $A=P+SI$."]),
 ("Compound interest", [
   r"$A=P\left(1+\dfrac R{100}\right)^n$ (interest compounded yearly); $CI=A-P$.",
   r"For 1 year, CI = SI. For 2 years, CI $-$ SI $=P\left(\dfrac R{100}\right)^2$.",
   r"Successive percentage changes: multiply the factors, e.g. $+10\%$ then $-10\%$ gives $1.1\times0.9=0.99$ (a $1\%$ decrease)."]),
]

MISTAKES = [
 r"Calculating profit or loss percent on the selling price; it is always on the <b>cost price</b>.",
 r"Calculating discount on the selling price; it is on the <b>marked price</b>.",
 r"Adding two successive percent changes: $+10\%$ then $-10\%$ is a $1\%$ decrease, not 0%.",
 r"Using the simple interest formula for compound interest, or forgetting to subtract $P$ from the amount to get CI.",
 r"Applying GST on the marked price when the question says it is charged after the discount.",
 r"Writing a percentage without dividing by 100 in calculations (e.g. $12\%$ of 2000 as $12\times2000$).",
]
