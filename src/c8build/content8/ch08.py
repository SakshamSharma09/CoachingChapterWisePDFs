from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def g(x): return f"{x:g}"
# A: fraction -> percent (5)
for fr_, pc in [("\\frac{3}{4}", 75), ("\\frac{7}{20}", 35), ("\\frac{5}{8}", 62.5), ("\\frac{9}{25}", 36), ("\\frac{1}{16}", 6.25)]:
    A.append(M4(rf"${fr_}$ expressed as a percentage is:", f"{g(pc)}%", [f"{g(pc+5)}%", f"{g(pc*2)}%", f"{g(pc-5)}%"], "Multiply by 100"))
# A: percent of quantity (6)
for p, q in [(15, 240), (35, 600), (12.5, 480), (8, 350), (45, 1200), (7.5, 800)]:
    v = p * q / 100
    A.append(M4(f"{g(p)}% of {q} is:", g(v), [g(v+10), g(v*2), g(v-10)], f"{g(p)}/100 × {q}"))
# A: increase/decrease (5)
for q, p, up in [(800, 25, True), (1500, 12, False), (640, 15, True), (2000, 18, False), (450, 20, True)]:
    v = q * (1 + (p if up else -p) / 100)
    A.append(M4(f"A quantity of {q} is {'increased' if up else 'decreased'} by {p}%. The new value is:", g(v), [g(q*(1+(-p if up else p)/100)), g(v+q*p/100), g(q*p/100)], f"{q} × {(100+p if up else 100-p)}/100"))
# A: profit/loss/discount (7)
for cp, sp in [(500, 575), (800, 720), (1200, 1500), (250, 200)]:
    pl = (sp - cp) / cp * 100
    A.append(M4(f"An article bought for ₹ {cp} is sold for ₹ {sp}. The {'profit' if sp>cp else 'loss'} percent is:", f"{g(abs(pl))}%", [f"{g(abs(pl)+5)}%", f"{g(abs(sp-cp))}%", f"{g(abs(pl)/2)}%"], "Profit or loss on CP"))
for mp, d in [(1500, 20), (900, 10), (2400, 25)]:
    A.append(M4(f"The marked price is ₹ {mp} and the discount is {d}%. The selling price is:", f"₹ {g(mp*(100-d)/100)}", [f"₹ {g(mp*d/100)}", f"₹ {g(mp*(100+d)/100)}", f"₹ {g(mp-d)}"], "SP = MP − discount"))
# A: interest (6)
for P, r, t in [(5000, 8, 2), (12000, 5, 3), (8000, 10, 1), (6000, 12, 2), (15000, 6, 4), (4000, 7.5, 2)]:
    si = P * r * t / 100
    A.append(M4(f"The simple interest on ₹ {P} at {g(r)}% per annum for {t} year(s) is:", f"₹ {g(si)}", [f"₹ {g(si*2)}", f"₹ {g(P+si)}", f"₹ {g(si/2)}"], r"$SI=\dfrac{PRT}{100}$"))
# A: concepts (11)
A += [
 M4("Percent means:", "per hundred", ["per ten", "per thousand", "per unit"], "Latin per centum"),
 M4("0.45 as a percentage is:", "45%", ["4.5%", "0.45%", "450%"], "× 100"),
 M4("The compound interest on a sum for 2 years is greater than the simple interest because:", "interest is also earned on earlier interest", ["rate is higher", "time is longer", "principal increases at start"], "Compounding"),
 M4("Which is the best discount for a customer?", "Larger discount percentage on the same marked price", ["Smaller discount", "No discount", "Equal"], "More saving"),
 M4("A gain of 100% means the selling price is:", "twice the cost price", ["equal to cost price", "half of cost price", "10% more"], "SP = 2 CP"),
 M4("If the price of an item is increased by 10% and then decreased by 10%, the final price is:", "less than the original", ["the same", "more than the original", "double"], "0.99 of original"),
 M4("GST is a tax charged on:", "goods and services", ["income only", "land only", "property transfer only"], "Goods and Services Tax"),
 M4("The amount at the end of a period is:", "principal plus interest", ["interest only", "principal only", "rate × time"], "A = P + I"),
 M4("The percentage of 1/5 is:", "20%", ["5%", "15%", "25%"], "100/5"),
 M4("If 20% of a number is 45, the number is:", "225", ["90", "180", "270"], "45 × 5"),
 M4("₹ 1000 at 10% compound interest annually for 2 years gives an amount of:", "₹ 1210", ["₹ 1200", "₹ 1100", "₹ 1220"], "1000 × 1.1 × 1.1"),
]
assert len(A) == 40, len(A)
B = [
 Q("Express $\\frac{7}{25}$ as a percentage.", "$28\\%$ (2).", "2"),
 Q("Find 18% of 650.", "$117$ (2).", "2"),
 Q("What is the difference between cost price and selling price?", "CP is what the seller pays; SP is what he receives (2).", "2"),
 Q("A shirt of marked price ₹ 800 is sold at 15% discount. Find the selling price.", "Discount ₹ 120, SP ₹ 680 (2).", "2"),
 Q("Find the simple interest on ₹ 6000 at 5% for 3 years.", "₹ 900 (2).", "2"),
 Q("A price rises from ₹ 80 to ₹ 92. Find the percentage increase.", "$12/80\\times100=15\\%$ (2).", "2"),
 Q("Express 35 out of 140 as a percentage.", "25% (2).", "2"),
 Q("What is profit percent? Write its formula.", "Profit ÷ cost price × 100 (2).", "2"),
 Q("Convert 12.5% to a fraction in simplest form.", "$\\frac{1}{8}$ (2).", "2"),
 Q("Find the amount on ₹ 5000 at 10% simple interest for 2 years.", "SI ₹ 1000, amount ₹ 6000 (2).", "2"),
 Q("What is compound interest?", "Interest calculated on the principal and on the interest earned earlier (2).", "2"),
 Q("A town's population is 40000 and it grows 5% in a year. Find the new population.", "42000 (2).", "2"),
 Q("A number is increased by 20% to become 360. What was the number?", "$360/1.2=300$ (2).", "2"),
 Q("Write 3/8 as a percentage and a decimal.", "37.5% (1); 0.375 (1).", "1+1"),
 Q("The cost of an item with 18% GST on ₹ 500 is?", "GST ₹ 90; total ₹ 590 (2).", "2"),
 Q("Find the discount when SP is ₹ 540 and MP is ₹ 600. Express it as a percentage.", "₹ 60 (1); 10% (1).", "1+1"),
]
for cp, pr in [(400, 15), (650, 20), (1200, 12.5), (900, 8), (2500, 6), (840, 25)]:
    sp = cp * (100 + pr) / 100
    C.append(Q(f"A trader buys an article for ₹ {cp} and sells at {g(pr)}% profit. Find the selling price.", f"Profit $=\\dfrac{{{g(pr)}}}{{100}}\\times{cp}=₹ {g(cp*pr/100)}$ (2); SP $=₹ {g(sp)}$ (1).", "2+1"))
for mp, d1, d2 in [(2000, 20, 10), (1500, 30, 5), (800, 25, 10), (1200, 15, 5)]:
    C.append(Q(f"A shopkeeper allows successive discounts of {d1}% and {d2}% on a marked price of ₹ {mp}. Find the selling price.", f"After first discount: ₹ {g(mp*(100-d1)/100)} (1.5); final SP ₹ {g(mp*(100-d1)/100*(100-d2)/100)} (1.5).", "1½+1½"))
for P, r, t in [(10000, 8, 2), (5000, 10, 2), (8000, 5, 3), (12000, 6, 2)]:
    amt = P * (1 + r / 100) ** t
    C.append(Q(f"Find the compound interest on ₹ {P} at {r}% per annum for {t} years.", f"$A=P(1+r/100)^n={P}\\times(1+{r}/100)^{t}=₹ {amt:,.2f}$ (2); CI $=₹ {amt-P:,.2f}$ (1).", "2+1"))
for P, r, t in [(7500, 6, 3), (9000, 4, 5), (3500, 12, 2), (2400, 5, 4)]:
    si = P * r * t / 100
    C.append(Q(f"At what total amount will ₹ {P} grow in {t} years at {r}% simple interest?", f"SI $=₹ {g(si)}$ (2); amount $=₹ {g(P+si)}$ (1).", "2+1"))
C += [
 Q("The price of petrol rises 20%. By what percent must consumption fall to keep the expense the same?", "New price 1.2; spending same so quantity $1/1.2=83.3\\%$ (2); falls by $16.67\\%$ (1).", "2+1"),
 Q("A student scored 432 out of 600. Express as a percentage and say the fraction.", "72% (2); $\\frac{18}{25}$ (1).", "2+1"),
 Q("If 30% of a school's 1200 students play sports, how many do not?", "360 play (1.5); 840 do not (1.5).", "1½+1½"),
 Q("A bicycle bought for ₹ 4000 is sold at a loss of 12.5%. Find the SP.", "Loss ₹ 500 (2); SP ₹ 3500 (1).", "2+1"),
]
C += [
 Q("A man saves ₹ 4500 per month, which is 15% of his salary. Find his salary and annual savings.", "Salary ₹ 30000 (2); annual savings ₹ 54000 (1).", "2+1"),
 Q("Find the rate of simple interest if ₹ 8000 earns ₹ 1920 interest in 3 years.", "$R=\\dfrac{100\\times1920}{8000\\times3}$ (2); $8\\%$ (1).", "2+1"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Define profit, loss and discount. (ii) A fan is marked ₹ 2500 and sold at 12% discount with 18% GST added on the discounted price. Find the final price.", "(i) Definitions (2). (ii) SP ₹ 2200; GST ₹ 396; total ₹ 2596 (3).", "2+3"),
 Q("(i) Find the CI on ₹ 20000 at 10% p.a. for 3 years. (ii) Compare with the SI.", "(i) $A=20000\\times1.331=26620$, CI ₹ 6620 (3). (ii) SI ₹ 6000, CI exceeds by ₹ 620 (2).", "3+2"),
 Q("<b>Case study:</b> A television is marked ₹ 30000. A store offers 15% discount, and a festival coupon of ₹ 1500 off. (i) Find the price after the discount. (ii) Price after the coupon. (iii) Effective discount percentage.", "(i) ₹ 25500 (2). (ii) ₹ 24000 (1). (iii) $6000/30000=20\\%$ (2).", "2+1+2"),
 Q("(i) A shopkeeper sells two articles at ₹ 1200 each, one at 20% profit and the other at 20% loss. Find the overall gain or loss. (ii) Explain.", "(i) CP₁ 1000, CP₂ 1500; total CP 2500, SP 2400; loss ₹ 100 (3). (ii) Loss percent on a larger base (2).", "3+2"),
 Q("(i) The population of a village rose from 8000 to 9680 in 2 years at a constant yearly rate. Find the rate. (ii) Predict next year's.", "(i) $8000(1+r)^2=9680$, $r=10\\%$ (3). (ii) 10648 (2).", "3+2"),
 Q("<b>Case study:</b> Meera deposits ₹ 25000 in a bank at 8% compound interest annually. (i) Find the amount after 2 years. (ii) The interest earned. (iii) If simple interest were paid instead, what would be the difference?", "(i) $25000\\times1.1664=29160$ (2). (ii) ₹ 4160 (1). (iii) SI ₹ 4000; difference ₹ 160 (2).", "2+1+2"),
 Q("(i) A trader marks goods 40% above cost and allows 25% discount. Find the profit percent. (ii) If CP is ₹ 500, find the SP.", "(i) MP 1.4, SP 1.05, profit 5% (3). (ii) ₹ 525 (2).", "3+2"),
 Q("(i) Salary of ₹ 40000 is increased by 15% and then decreased by 10%. Find the final salary. (ii) Net change percentage.", "(i) 46000 then 41400 (3). (ii) +3.5% (2).", "3+2"),
 Q("(i) How is GST calculated? (ii) A restaurant bill is ₹ 1800 with 5% GST; find the total.", "(i) Percentage of the value of goods or services added to it (2). (ii) ₹ 1890 (3).", "2+3"),
 Q("<b>Case study:</b> A shop reduces the price of a school bag from ₹ 900 to ₹ 765. (i) Find the discount. (ii) Discount percent. (iii) Find the price after a further 10% off.", "(i) ₹ 135 (1). (ii) 15% (2). (iii) ₹ 688.50 (2).", "1+2+2"),
 Q("(i) Find the principal that amounts to ₹ 5832 in 2 years at 8% CI. (ii) State what is compounding.", "(i) $P\\times1.1664=5832$, $P=5000$ (3). (ii) Interest added to principal each period (2).", "3+2"),
 Q("(i) In a class, 60% of 40 students are girls. Of these, 25% have bicycles. How many girls have bicycles? (ii) What percent of the class are they?", "(i) 24 girls, 6 with bicycles (3). (ii) 15% (2).", "3+2"),
 Q("(i) Show that two successive increases of 10% equal one increase of 21%. (ii) What about 10% increase followed by 10% decrease?", "(i) $1.1\\times1.1=1.21$ (3). (ii) $1.1\\times0.9=0.99$, a 1% decrease (2).", "3+2"),
 Q("<b>Case study:</b> A farmer borrows ₹ 50000 at 12% simple interest for 3 years. (i) Find the interest. (ii) Total to be repaid. (iii) Monthly instalment if repaid equally over 36 months.", "(i) ₹ 18000 (2). (ii) ₹ 68000 (1). (iii) ₹ 1888.89 (2).", "2+1+2"),
 Q("(i) Express the ratio 3 : 5 as percentages. (ii) A mixture is 35% acid; how much acid in 80 L?", "(i) 37.5% and 62.5% (2). (ii) 28 L (3).", "2+3"),
 Q("(i) A phone bought for ₹ 15000 loses 20% value in the first year and 10% in the second. Find its value after 2 years. (ii) Total depreciation percent.", "(i) 12000 then 10800 (3). (ii) 28% (2).", "3+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
