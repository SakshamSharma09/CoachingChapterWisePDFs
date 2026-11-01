"""Class 8 Maths Ch 8 - Fractions in Disguise (percentages, profit/loss, discount, GST, simple & compound interest)."""
from c8m_u import *

SLUG, NAME, CHNO = "Fractions_in_Disguise", "Fractions in Disguise", 8

def SI(P, R, T): return Fr(P * R * T, 100)
def CI(P, R, n): return Fr(P) * (Fr(100 + R, 100) ** n)
def sp_gain(cp, p): return Fr(cp) * (100 + p) / 100
def sp_loss(cp, p): return Fr(cp) * (100 - p) / 100

# ================= EASY =================
e1 = [ND(rf"$ {fr(n,d)} $ expressed as a percentage is:", Fr(n * 100, d), f"Multiply by 100: ${fr(n,d)}\\times100={g(Fr(n*100,d))}$", fmt=g, post="%") for n, d in [(1, 4), (3, 5), (7, 10), (9, 20), (11, 25), (13, 50), (17, 20), (3, 25)]]
e2 = [M4(f"{p}% written as a fraction in lowest terms is:", f"${frs(Fr(p,100))}$", [f"${frs(Fr(p,10))}$" if Fr(p, 10).denominator != 1 else f"${p}$", f"${fr(100,p)}$", f"${fr(p+5,100)}$"], f"${p}\\%={fr(p,100)}={frs(Fr(p,100))}$") for p in [20, 35, 45, 60, 85, 15]]
e3 = [ND(f"{p}% of {n} is:", Fr(p * n, 100), f"{p}/100 × {n}") for p, n in [(10, 250), (20, 450), (25, 360), (50, 780), (5, 600), (30, 150)]]
e4 = [ND(f"The price ₹ {n} is increased by {p}%. The new price (in ₹) is:", Fr(n * (100 + p), 100), f"Increase = {g(Fr(n*p,100))}; new = {g(Fr(n*(100+p),100))}") for n, p in [(500, 10), (800, 25), (240, 5), (1200, 15), (350, 20), (900, 30)]]
e5 = [ND(f"The simple interest on ₹ {P} at {R}% per annum for {T} years (in ₹) is:", SI(P, R, T), "SI = PRT/100") for P, R, T in [(1000, 5, 2), (2000, 10, 3), (1500, 4, 2), (3000, 6, 1), (5000, 8, 2), (2500, 12, 2)]]
e6 = [ND(f"The marked price of a shirt is ₹ {mp} and the discount is {d}%. The selling price (in ₹) is:", sp_loss(mp, d), "SP = MP − discount") for mp, d in [(1000, 10), (600, 20), (1500, 5), (800, 25), (2000, 15), (450, 10)]]
EASY_A = [e1, e2, e3, e4, e5, e6]
EASY_B = ([Q(rf"Express ${fr(n,d)}$ as a percentage.", rf"${fr(n,d)}\times100=" + g(Fr(n * 100, d)) + r"\%$ (2).", "2") for n, d in [(3, 8), (7, 8), (5, 16), (9, 40)]]
          + [Q(f"Find {p}% of ₹ {n}.", f"${p}/100\\times{n}=$ ₹ {g(Fr(p*n,100))} (2).", "2") for p, n in [(12, 500), (35, 200), (18, 350), (45, 640)]]
          + [Q(f"An article is bought for ₹ {cp} and sold for ₹ {sp}. Find the {'profit' if sp > cp else 'loss'}.", f"{'Profit' if sp > cp else 'Loss'} = SP − CP (or CP − SP) (1) = ₹ {abs(sp-cp)} (1).", "1+1") for cp, sp in [(400, 460), (750, 700), (1200, 1350), (980, 900)]])
EASY_C = ([Q(f"An article costing ₹ {cp} is sold for ₹ {sp}. Find the {'profit' if sp > cp else 'loss'} percent.", f"{'Profit' if sp>cp else 'Loss'} = ₹ {abs(sp-cp)} (1); percent = {abs(sp-cp)}/{cp}×100 (1) = {g(Fr(abs(sp-cp)*100,cp))}% (1).", "1+1+1") for cp, sp in [(200, 250), (500, 450), (800, 880), (1000, 920), (250, 300), (400, 340)]]
          + [Q(f"The marked price of a bag is ₹ {mp}. A discount of {d}% is given. Find the discount and the selling price.", f"Discount = {d}/100×{mp} = ₹ {g(Fr(mp*d,100))} (2); SP = {mp} − {g(Fr(mp*d,100))} = ₹ {g(sp_loss(mp,d))} (1).", "2+1") for mp, d in [(1200, 10), (850, 20), (640, 25), (2400, 5), (3000, 12), (1800, 30)]]
          + [Q(f"Find the simple interest and the amount on ₹ {P} for {T} years at {R}% per annum.", f"SI = {P}×{R}×{T}/100 = ₹ {g(SI(P,R,T))} (2); amount = P + SI = ₹ {g(P+SI(P,R,T))} (1).", "2+1") for P, R, T in [(4000, 5, 2), (6000, 10, 3), (7500, 4, 2), (10000, 6, 3), (8000, 5, 4), (2400, 15, 5)]])
def e_d1(inc, a, b):
    sa, sb = Fr(inc * a, 100), Fr(inc * b, 100)
    return Q(f"A family earns ₹ {inc} a month. It spends {a}% on food and {b}% on rent. Find the amount spent on each item and the amount left.",
             f"Food = {a}% of {inc} = ₹ {g(sa)} (2); rent = {b}% of {inc} = ₹ {g(sb)} (2); left = {inc} − {g(sa+sb)} = ₹ {g(inc-sa-sb)} (1).", "2+2+1")
def e_d2(cp, p, q):
    return Q(f"A trader buys a table for ₹ {cp}. Find the selling price if he sells it at (i) a gain of {p}% (ii) a loss of {q}%. Also find the difference of the two selling prices.",
             f"(i) SP = {cp}×{100+p}/100 = ₹ {g(sp_gain(cp,p))} (2); (ii) SP = {cp}×{100-q}/100 = ₹ {g(sp_loss(cp,q))} (2); difference = ₹ {g(sp_gain(cp,p)-sp_loss(cp,q))} (1).", "2+2+1")
EASY_D = ([e_d1(*x) for x in [(20000, 30, 25), (36000, 40, 20), (15000, 35, 15), (50000, 25, 30), (24000, 45, 10), (80000, 20, 35)]]
          + [e_d2(*x) for x in [(2000, 10, 5), (4500, 20, 10), (3200, 25, 15), (1600, 5, 10), (6000, 15, 20), (2500, 12, 8)]])

# ================= NCERT =================
n1 = [ND(f"A value changes from {a} to {b}. The percentage {'increase' if b > a else 'decrease'} is:", Fr(abs(b - a) * 100, a), f"Change/original × 100 = {abs(b-a)}/{a}×100", post="%") for a, b in [(80, 100), (250, 200), (60, 75), (400, 340), (150, 180), (500, 425)]]
n2 = [ND(f"{x} is what percent of {y}?", Fr(x * 100, y), f"{x}/{y}×100", post="%") for x, y in [(18, 72), (35, 140), (9, 60), (48, 80), (21, 56), (14, 40)]]
n3 = [ND(f"A cycle bought for ₹ {cp} is sold for ₹ {sp}. The {'gain' if sp > cp else 'loss'} percent is:", Fr(abs(sp - cp) * 100, cp), f"(SP−CP)/CP×100 = {abs(sp-cp)}/{cp}×100", post="%") for cp, sp in [(1500, 1800), (2400, 2160), (3200, 3520), (1250, 1000), (850, 1020), (640, 576)]]
n4 = [ND(f"The marked price of a jacket is ₹ {mp} and it is sold for ₹ {sp}. The discount percent is:", Fr((mp - sp) * 100, mp), f"Discount = {mp-sp}; {mp-sp}/{mp}×100", post="%") for mp, sp in [(2500, 2000), (1800, 1620), (960, 816), (4000, 3400), (750, 600), (1250, 1125)]]
n5 = [ND(f"The price of an article is ₹ {p} and GST is charged at {r}%. The bill amount (in ₹) is:", Fr(p * (100 + r), 100), f"GST = {g(Fr(p*r,100))}; bill = {g(Fr(p*(100+r),100))}") for p, r in [(2000, 5), (1500, 12), (800, 18), (3500, 28), (1200, 5), (4000, 12)]]
n6 = [ND(f"The compound interest on ₹ {P} for 2 years at {R}% per annum compounded annually (in ₹) is:", CI(P, R, 2) - P, f"Amount = {P}(1+{R}/100)² = {g(CI(P,R,2))}; CI = A − P", wrong=[SI(P, R, 2), CI(P, R, 2)]) for P, R in [(5000, 10), (2000, 20), (10000, 5), (8000, 15), (6400, 25)]]
NCERT_A = [n1, n2, n3, n4, n5, n6]
NCERT_B = ([Q(f"What percent of {y} is {x}?", f"${x}/{y}\\times100$ (1) $={g(Fr(x*100,y))}\\%$ (1).", "1+1") for x, y in [(36, 90), (27, 120), (45, 75), (63, 140)]]
           + [Q(f"A television bought for ₹ {cp} was sold at a loss of {p}%. Find the selling price.", f"Loss = {p}% of {cp} = ₹ {g(Fr(cp*p,100))} (1); SP = ₹ {g(sp_loss(cp,p))} (1).", "1+1") for cp, p in [(24000, 15), (18500, 8), (32000, 12), (9600, 25)]]
           + [Q(f"Find the rate of simple interest if ₹ {P} becomes ₹ {P+SI(P,R,T)} in {T} years.", f"SI = ₹ {g(SI(P,R,T))} (1); R = SI×100/(P×T) = {R}% p.a. (1).", "1+1") for P, R, T in [(4000, 6, 3), (7500, 8, 2), (12000, 5, 4), (9000, 7, 2)]])
def g_cgst(p, r): return Fr(p * r, 100)
NCERT_C = ([Q(f"The marked price of a laptop is ₹ {p}. GST at {r}% is added. Find the GST amount and the final bill.", f"GST = {r}% of {p} = ₹ {g(g_cgst(p,r))} (2); bill = {p} + {g(g_cgst(p,r))} = ₹ {g(p+g_cgst(p,r))} (1).", "2+1") for p, r in [(45000, 18), (36000, 12), (62000, 18), (28500, 5), (52000, 28), (15000, 12)]]
           + [Q(f"Find the amount and the compound interest on ₹ {P} for 2 years at {R}% per annum compounded annually.", f"A = P(1+R/100)² = {P}×{100+R}/100×{100+R}/100 = ₹ {g(CI(P,R,2))} (2); CI = ₹ {g(CI(P,R,2)-P)} (1).", "2+1") for P, R in [(12500, 8), (16000, 25), (4000, 15), (30000, 10), (22500, 20), (7200, 5)]]
           + [Q(f"The population of a town was {a} and became {b} in a year. Find the percentage {'growth' if b > a else 'fall'}.", f"Change = {abs(b-a)} (1); % = {abs(b-a)}/{a}×100 (1) = {g(Fr(abs(b-a)*100,a))}% (1).", "1+1+1") for a, b in [(40000, 44000), (25000, 22500), (56000, 61600), (84000, 79800), (32000, 36800), (72000, 64800)]])
def tot_si(P, R, T): return P + SI(P, R, T)
NCERT_D = ([Q(f"Find the compound interest on ₹ {P} for 3 years at {R}% per annum compounded annually. By how much does it exceed the simple interest for the same period?",
              f"A = P(1+R/100)³ = ₹ {g(CI(P,R,3))} (2); CI = ₹ {g(CI(P,R,3)-P)} (1); SI = {P}×{R}×3/100 = ₹ {g(SI(P,R,3))} (1); difference = ₹ {g(CI(P,R,3)-P-SI(P,R,3))} (1).", "2+1+1+1") for P, R in [(8000, 10), (5000, 20), (15000, 10), (12500, 20), (20000, 10), (6250, 20)]]
           + [Q(f"A refrigerator has marked price ₹ {mp}. The shopkeeper allows a discount of {d}% and then charges GST of {r}% on the discounted price. Find the amount payable.",
                f"Discount = ₹ {g(Fr(mp*d,100))} (1); discounted price = ₹ {g(sp_loss(mp,d))} (1); GST = {r}% of it = ₹ {g(sp_loss(mp,d)*r/100)} (1); payable = ₹ {g(sp_loss(mp,d)*(100+r)/100)} (2).", "1+1+1+2")
              for mp, d, r in [(30000, 10, 18), (25000, 20, 12), (40000, 15, 18), (18000, 5, 28), (50000, 12, 5), (24000, 25, 12)]])

# ================= MEDIUM =================
def cp_from(sp, p): return Fr(sp) * 100 / (100 + p)
def cp_from_loss(sp, p): return Fr(sp) * 100 / (100 - p)
m1 = [ND(f"An article is sold for ₹ {sp} at a profit of {p}%. Its cost price (in ₹) is:", cp_from(sp, p), f"CP = SP×100/(100+{p})", wrong=[Fr(sp * (100 - p), 100), sp - Fr(sp * p, 100)]) for sp, p in [(1260, 5), (2400, 20), (1750, 25), (3300, 10), (4590, 8)]]
m2 = [ND(f"A watch is sold for ₹ {sp} at a loss of {p}%. Its cost price (in ₹) is:", cp_from_loss(sp, p), f"CP = SP×100/(100−{p})", wrong=[Fr(sp * (100 + p), 100), sp + Fr(sp * p, 100)]) for sp, p in [(1530, 15), (2800, 20), (3600, 10), (4200, 30), (870, 13)]]
m3 = [ND(f"After a discount of {d}%, a pair of shoes is sold for ₹ {sp}. The marked price (in ₹) is:", Fr(sp * 100, 100 - d), f"MP = SP×100/(100−{d})", wrong=[Fr(sp * (100 + d), 100)]) for sp, d in [(1530, 15), (2240, 20), (1350, 10), (2100, 25), (3150, 30)]]
m4_ = [ND(f"The simple interest on a sum at {R}% p.a. for {T} years is ₹ {SI(P,R,T)}. The sum (in ₹) is:", P, "P = SI×100/(R×T)") for P, R, T in [(3000, 5, 4), (4500, 8, 2), (6400, 5, 5), (2800, 10, 3), (9000, 4, 5)]]
m5 = [ND(f"A number is increased by {p}% and the result is {Fr(n*(100+p),100)}. The original number is:", n, f"Original = result × 100/{100+p}") for n, p in [(240, 25), (360, 15), (520, 30), (850, 20), (480, 35)]]
m6 = [ND(f"The difference between CI and SI on ₹ {P} for 2 years at {R}% p.a. (in ₹) is:", CI(P, R, 2) - P - SI(P, R, 2), f"Difference = P(R/100)² = {P}×({R}/100)²") for P, R in [(5000, 4), (8000, 5), (10000, 3), (4000, 10), (2500, 8)]]
m7 = [ND(f"Two successive discounts of {a}% and {b}% are given on a marked price ₹ {mp}. The selling price (in ₹) is:", Fr(mp) * (100 - a) * (100 - b) / 10000, f"{mp}×{100-a}/100×{100-b}/100", wrong=[sp_loss(mp, a + b)]) for mp, a, b in [(2000, 10, 10), (5000, 20, 10), (1600, 25, 20), (3000, 10, 20)]]
MED_A = [m1, m2, m3, m4_, m5, m6, m7]
MED_B = ([Q(f"By selling an article for ₹ {sp}, a trader gains {p}%. Find the cost price.", f"CP = SP×100/(100+{p}) (1) = ₹ {g(cp_from(sp,p))} (1).", "1+1") for sp, p in [(1380, 15), (2520, 5), (4320, 8), (5850, 30)]]
         + [Q(f"A sum of ₹ {P} amounts to ₹ {P+SI(P,R,T)} in {T} years at simple interest. Find the rate per annum.", f"SI = ₹ {g(SI(P,R,T))} (1); R = SI×100/(P×T) = {R}% (1).", "1+1") for P, R, T in [(5600, 5, 3), (8400, 7, 2), (6500, 12, 4), (3600, 15, 3)]]
         + [Q(f"The price of a book rises from ₹ {a} to ₹ {b}. Find the percentage increase.", f"Increase = ₹ {b-a} (1); % = {b-a}/{a}×100 = {g(Fr((b-a)*100,a))}% (1).", "1+1") for a, b in [(160, 200), (225, 270), (320, 368), (125, 155)]])
def succ(mp, a, b): return Fr(mp) * (100 - a) * (100 - b) / 10000
MED_C = ([Q(f"A shopkeeper allows successive discounts of {a}% and {b}% on a marked price of ₹ {mp}. Find the selling price and the single equivalent discount percent.", f"After first discount: ₹ {g(sp_loss(mp,a))} (1); SP = ₹ {g(succ(mp,a,b))} (1); equivalent discount = {g(100-Fr(100-a)*(100-b)/100)}% (1).", "1+1+1") for mp, a, b in [(4000, 10, 5), (2500, 20, 10), (6000, 15, 10), (3600, 25, 20), (8000, 10, 20), (1500, 30, 10)]]
         + [Q(f"In how many years will ₹ {P} amount to ₹ {P+SI(P,R,T)} at {R}% simple interest per annum?", f"SI = ₹ {g(SI(P,R,T))} (1); T = SI×100/(P×R) (1) = {T} years (1).", "1+1+1") for P, R, T in [(7500, 8, 3), (4800, 5, 5), (9600, 12, 2), (3500, 10, 4), (6000, 9, 6), (2000, 15, 8)]]
         + [Q(f"A sum of ₹ {P} is lent for 2 years at {a}% for the first year and {b}% for the second year, compounded annually. Find the amount.", f"After year 1: {P}×{100+a}/100 = ₹ {g(Fr(P*(100+a),100))} (1); after year 2: ×{100+b}/100 = ₹ {g(Fr(P)*(100+a)*(100+b)/10000)} (2).", "1+2") for P, a, b in [(10000, 10, 20), (5000, 20, 10), (8000, 5, 10), (20000, 10, 5), (12500, 4, 8), (6000, 15, 20)]])
MED_D = ([Q(f"A trader sells a radio for ₹ {sp} and gains {p}%. If he had sold it for ₹ {sp2}, what would be his gain or loss percent?", f"CP = {sp}×100/{100+p} = ₹ {g(cp_from(sp,p))} (2); new SP − CP = ₹ {g(sp2-cp_from(sp,p))} (1); percent = {g(Fr(sp2-cp_from(sp,p))*100/cp_from(sp,p))}% {'gain' if sp2 > cp_from(sp,p) else 'loss'} (2).", "2+1+2")
           for sp, p, sp2 in [(2100, 5, 2400), (3300, 10, 2700), (4800, 20, 4000), (2760, 15, 2640), (5850, 30, 4950), (4620, 10, 4200)]]
          + [Q(f"A man deposits ₹ {P} at simple interest and another ₹ {Q2} at the same rate. After {T} years the total interest is ₹ {SI(P+Q2,R,T)}. Find the rate and the interest earned on each sum.", f"Total sum = ₹ {P+Q2} (1); R = SI×100/(sum×T) = {R}% (2); interest on first = ₹ {g(SI(P,R,T))} (1); on second = ₹ {g(SI(Q2,R,T))} (1).", "1+2+1+1")
             for P, Q2, R, T in [(4000, 6000, 5, 2), (3000, 5000, 8, 3), (7000, 3000, 6, 4), (2500, 7500, 4, 5), (6000, 9000, 10, 2), (1200, 1800, 7, 5)]])

# ================= HARD =================
h1 = [ND(f"Two articles are sold at ₹ {s} each, one at a gain of {p}% and the other at a loss of {p}%. The overall result is a loss of (in %):", Fr(p * p, 100), f"Loss % = (p²/100) = {p}²/100", wrong=[0, p, Fr(p, 2)], post="%") for s, p in [(1800, 10), (2400, 20), (3000, 15), (1500, 30)]]
h2 = [ND(f"The population of a town is {P} and it grows at {r}% per annum. After 2 years it will be:", CI(P, r, 2), f"{P}×(1+{r}/100)²", wrong=[P + SI(P, r, 2)]) for P, r in [(50000, 10), (40000, 5), (62500, 20), (80000, 25)]]
h3 = [ND(f"A machine worth ₹ {P} depreciates at {r}% per annum. Its value after 2 years (in ₹) is:", Fr(P) * (100 - r) * (100 - r) / 10000, f"{P}×(1−{r}/100)²", wrong=[P - SI(P, r, 2)]) for P, r in [(50000, 10), (80000, 20), (62500, 20), (40000, 5)]]
h4 = [ND(f"A price is first increased by {a}% and then decreased by {b}%. The net change (as percent, + for increase, − for decrease) is:", Fr(100 + a) * (100 - b) / 100 - 100, f"(1+{a}/100)(1−{b}/100) − 1", wrong=[a - b], post="%", fmt=lambda x: ("+" if x > 0 else "−" if x < 0 else "") + g(abs(x))) for a, b in [(20, 20), (10, 25), (30, 10), (50, 40)]]
h5 = [ND(f"The CI on a sum for 2 years at {R}% p.a. is ₹ {CI(P,R,2)-P}. The sum (in ₹) is:", P, f"A = P(1+{R}/100)², CI = A − P", wrong=[Fr(P * 2)]) for P, R in [(2500, 20), (4000, 10), (6400, 25), (1600, 5)]]
h6 = [ND(f"A trader marks his goods {m}% above cost and allows a discount of {d}%. His gain percent is:", Fr(100 + m) * (100 - d) / 100 - 100, f"(1+{m}/100)(1−{d}/100) − 1", wrong=[m - d], post="%") for m, d in [(40, 10), (50, 20), (60, 25), (25, 10)]]
h7 = [ND(f"If the difference between the CI and the SI on a sum for 2 years at {R}% is ₹ {g(Fr(P*R*R,10000))}, the sum (in ₹) is:", P, "Difference = P(R/100)²") for P, R in [(7500, 4), (15000, 8), (4000, 5), (12000, 10)]]
h8 = [ND(f"A sum triples in {T} years at simple interest. The rate of interest per annum is:", Fr(200, T), "SI = 2P so 2P = P×R×T/100 and R = 200/T", post="%") for T in [4, 8, 10, 16]]
HARD_A = [h1, h2, h3, h4, h5, h6, h7, h8]
HARD_B = ([Q(f"A number is increased by {a}% and the result is decreased by {b}%. Is the final number more or less than the original? By what percent?", f"Final = (1+{a}/100)(1−{b}/100) (1) = {g(Fr(100+a)*(100-b)/100)}% of original, so {'more' if Fr(100+a)*(100-b)/100>100 else 'less'} by {g(abs(Fr(100+a)*(100-b)/100-100))}% (1).", "1+1") for a, b in [(25, 10), (40, 30), (15, 10), (60, 50)]]
         + [Q(f"The cost of an item is ₹ {cp}. It is marked {m}% above the cost price and sold at {d}% discount. Find the selling price.", f"Marked price = ₹ {g(sp_gain(cp,m))} (1); SP = ₹ {g(sp_gain(cp,m)*(100-d)/100)} (1).", "1+1") for cp, m, d in [(1500, 40, 10), (2400, 25, 20), (3600, 50, 30), (2000, 60, 25)]]
         + [Q(f"Rahul invests ₹ {P} at {R}% p.a. compounded annually. Find the amount after 2 years and write it as a fraction of the principal.", f"A = {P}({100+R}/100)² = ₹ {g(CI(P,R,2))} (1); A/P = {g(Fr(CI(P,R,2),P))} (1).", "1+1") for P, R in [(2500, 20), (4000, 10), (1600, 25), (1000, 30)]])
def eqloss(s, p):
    return Fr(2 * s) - (Fr(s) * 100 / (100 + p) + Fr(s) * 100 / (100 - p))
HARD_C = ([Q(f"A merchant sells two items at ₹ {s} each, one at a gain of {p}% and the other at a loss of {p}%. Find the overall gain or loss in rupees.", f"CP1 = {s}×100/{100+p} = {g(Fr(s*100,100+p))} (1); CP2 = {s}×100/{100-p} = {g(Fr(s*100,100-p))} (1); total CP − total SP = ₹ {g(-eqloss(s,p))}, a loss (1).", "1+1+1") for s, p in [(1980, 10), (2640, 20), (1950, 25), (3360, 40), (990, 10), (1200, 20)]]
         + [Q(f"The value of a car depreciates by {r}% every year. If its present value is ₹ {P}, find its value after 3 years.", f"V = P(1−r/100)³ (1) = {P}×{(100-r)}/100 three times (1) = ₹ {g(Fr(P)*(100-r)**3/10**6)} (1).", "1+1+1") for P, r in [(500000, 10), (400000, 20), (250000, 20), (800000, 10), (160000, 25), (625000, 20)]]
         + [Q(f"A shopkeeper buys an article at ₹ {cp}, marks it up by {m}% and gives a discount of {d}%. Find his gain or loss percent.", f"MP = ₹ {g(sp_gain(cp,m))} (1); SP = ₹ {g(sp_gain(cp,m)*(100-d)/100)} (1); gain/loss % = {g(Fr(sp_gain(cp,m)*(100-d)/100-cp)*100/cp)}% (1).", "1+1+1") for cp, m, d in [(800, 50, 20), (1200, 30, 20), (2000, 60, 30), (500, 30, 10), (1500, 20, 25), (900, 80, 40)]])
HARD_D = ([Q(f"A sum of ₹ {P} is invested for 3 years at {R}% p.a. compounded annually. Find the interest for each of the three years separately and verify that their total is the compound interest.",
             f"Year 1: A1 = ₹ {g(CI(P,R,1))}, interest ₹ {g(CI(P,R,1)-P)} (1); year 2: A2 = ₹ {g(CI(P,R,2))}, interest ₹ {g(CI(P,R,2)-CI(P,R,1))} (2); year 3: A3 = ₹ {g(CI(P,R,3))}, interest ₹ {g(CI(P,R,3)-CI(P,R,2))} (1); total ₹ {g(CI(P,R,3)-P)} = A3 − P (1).", "1+2+1+1") for P, R in [(10000, 20), (50000, 10), (25000, 20), (40000, 10), (15625, 20), (30000, 10)]]
          + [Q(f"A shopkeeper marks an article {m}% above its cost price. During a sale he gives a discount of {d}% and still earns a profit of ₹ {pr}. Find the cost price.", f"Let CP = x. SP = x(1+{m}/100)(1−{d}/100) = {g(Fr(100+m)*(100-d)/10000)}x (2); profit = {g(Fr(100+m)*(100-d)/10000-1)}x = {pr} (2); x = ₹ {g(Fr(pr)/(Fr(100+m)*(100-d)/10000-1))} (1).", "2+2+1")
             for m, d, pr in [(50, 20, 240), (60, 25, 100), (40, 10, 130), (80, 30, 260), (25, 10, 75), (100, 40, 400)]])

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}
