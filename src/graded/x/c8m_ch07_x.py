"""Class 8 Maths Ch 7 Proportional Reasoning-1 - extras."""
from common import AR4, Q

AR = [
 AR4(r"The ratios $3:4$ and $9:12$ are in proportion.", r"Two ratios $a:b$ and $c:d$ are in proportion if they are equal, that is, if $ad=bc$.", "a",
     r"$3\times12=36=4\times9$, so the ratios are equal; R is the test."),
 AR4(r"The ratio $15:25$ in its simplest form is $3:5$.", r"The ratio of two quantities of the same kind has no unit.", "b",
     r"Dividing both terms by 5 gives $3:5$ so A is true; R is also true but does not explain the simplification."),
 AR4(r"If 6 pens cost ₹90, then 10 pens cost ₹150.", r"In the unitary method we first find the cost of 10 pens.", "c",
     r"Cost of 1 pen $=15$, so 10 pens cost 150 and A is true. The unitary method first finds the value of <b>one</b> unit, so R is false."),
 AR4(r"The ratio $2:3$ is greater than the ratio $3:4$.", r"Ratios can be compared by converting them to fractions with the same denominator.", "d",
     r"$\dfrac23=\dfrac8{12}$ and $\dfrac34=\dfrac9{12}$, so $2:3<3:4$; A is false, R is a true method."),
 AR4(r"If ₹1,200 is divided between A and B in the ratio $3:5$, B gets ₹750.", r"B's share is $\dfrac{5}{3+5}$ of the total amount.", "a",
     r"$\dfrac58\times1200=750$; R gives the formula used."),
 AR4(r"The ratio of 40 minutes to 2 hours is $1:3$.", r"The ratio of two quantities of the same kind has no unit.", "b",
     r"$40:120=1:3$ so A is true. R is true but only states that ratios are unitless; it does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Sunita in Amritsar mixes curd and water in the ratio $3:2$ to make 10 litres of lassi. "
   r"(i) What fraction of the lassi is curd? (ii) How many litres of curd are used? (iii) How many litres of water are used? (iv) She wants to make 25 litres of lassi in the same ratio. Find the quantities of curd and water and show that the ratio is unchanged.",
   r"(i) $\dfrac{3}{3+2}=\dfrac35$ (1). (ii) $\dfrac35\times10=6$ L (1). (iii) $10-6=4$ L (1). (iv) Curd $=\dfrac35\times25=15$ L and water $=10$ L (1); $15:10=3:2$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A mason in Kota earns ₹4,500 for 6 days of work, while another mason earns ₹3,900 for 5 days. Assume daily wages are fixed. "
   r"(i) Find the first mason's wage per day. (ii) How much does he earn in 10 days? (iii) In how many days does he earn ₹12,000? (iv) Who earns more per day, and by how much?",
   r"(i) $4500\div6=$ ₹750 (1). (ii) $750\times10=$ ₹7,500 (1). (iii) $12000\div750=16$ days (1). (iv) Second mason earns $3900\div5=$ ₹780 per day (1), which is ₹30 more per day than the first (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A prize of ₹15,000 won by a team is shared among three friends A, B and C in the ratio $2:3:5$. "
   r"(i) Find the total number of parts. (ii) Find A's share. (iii) Find C's share. (iv) Find B's share, and also B's share if the prize had been ₹24,000 shared in the same ratio.",
   r"(i) $2+3+5=10$ parts (1). (ii) $\dfrac2{10}\times15000=$ ₹3,000 (1). (iii) $\dfrac5{10}\times15000=$ ₹7,500 (1). (iv) B gets $\dfrac3{10}\times15000=$ ₹4,500 (1); for ₹24,000, B gets $\dfrac3{10}\times24000=$ ₹7,200 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Ratio", [
   r"Ratio of $a$ to $b$ (same kind, same unit): $a:b=\dfrac ab$, $b\neq0$.",
   r"Simplest form: divide both terms by their HCF. Equivalent ratios: $a:b=ka:kb$ ($k\neq0$).",
   r"Convert to the same unit before forming a ratio (e.g. 1 m : 40 cm = 100 : 40 = 5 : 2)."]),
 ("Proportion", [
   r"$a:b=c:d$ (written $a:b::c:d$) are in proportion if $ad=bc$ ($a,d$ extremes; $b,c$ means).",
   r"Comparing ratios: convert to fractions with a common denominator, or cross-multiply."]),
 ("Unitary method", [
   r"Find the value of one unit, then multiply: if $n$ items cost $C$, one costs $\dfrac Cn$ and $m$ items cost $\dfrac Cn\times m$.",
   r"Direct variation: the quotient $\dfrac{y}{x}$ is constant."]),
 ("Sharing in a ratio", [
   r"Share a quantity $T$ in the ratio $p:q$: first part $=\dfrac{p}{p+q}T$, second $=\dfrac{q}{p+q}T$.",
   r"Combining ratios: if $a:b$ and $b:c$ are given, make the $b$ terms equal to get $a:b:c$.",
   r"Speed $=\dfrac{\text{distance}}{\text{time}}$, rate $=\dfrac{\text{amount}}{\text{one unit}}$ (a ratio with units)."]),
]

MISTAKES = [
 r"Forming a ratio without converting units: 50 cm : 2 m is $50:200=1:4$, not $25:1$.",
 r"Writing the ratio in the wrong order: the ratio of A to B is not the same as B to A.",
 r"Dividing a total in the ratio $3:5$ by dividing it by 3 and 5 separately; first add the parts ($3+5=8$) and divide by 8.",
 r"Adding the same number to both terms to get an equivalent ratio ($2:3\ne4:5$); equivalent ratios are got by multiplying or dividing.",
 r"Comparing ratios by only looking at the first terms; convert to fractions with the same denominator.",
 r"Mixing up which quantities go together in the unitary method (e.g. dividing cost by the wrong number of items).",
]
