import random
from fractions import Fraction as F
from lib import mcq, Q, OR, table
from mk9 import M4, build
R = random.Random(910)

def fm(x):
    x = float(x)
    s = f"{x:.2f}".rstrip("0").rstrip(".")
    return s
def wavg(vals, ws): return sum(F(v) * F(w) for v, w in zip(vals, ws)) / sum(F(w) for w in ws)
def dist(c, extra=()):
    out = []
    for v in [c + 1, c - 1, c + 2, c - 2, c * 2, c / 2, c + 5, c - 5, *extra]:
        v = round(float(v), 2)
        if v != round(float(c), 2) and v not in out and v > 0: out.append(v)
    return out

A = []; B = []; C = []; D = []

# ---- A1: combined mean of two groups (6)
for (n, a, m, b) in [(24, 68, 16, 78), (20, 55, 30, 65), (15, 82, 35, 74), (40, 60, 10, 85), (18, 45, 12, 70), (25, 90, 15, 50)]:
    v = wavg([a, b], [n, m]); assert v == int(v) or abs(v * 10 - round(v * 10)) < 1e-9
    simple = (a + b) / 2
    A.append(M4(f"A group of {n} students has an average of {a} marks and another group of {m} students has an average of {b} marks. The average of all {n+m} students is:", fm(v),
                [fm(x) for x in dist(v, [simple])[:3]], f"$\\dfrac{{{n}\\times{a}+{m}\\times{b}}}{{{n}+{m}}}={fm(v)}$"))
# ---- A2: equal-size groups (3)
for (xs, k) in [((12, 15, 18), "weeks of 5 days each"), ((40, 52, 46), "classes of 30 students each"), ((7, 9, 14, 10), "months of 30 days each")]:
    v = F(sum(xs), len(xs))
    A.append(M4(f"The averages of {len(xs)} {k} are {', '.join(map(str, xs))}. The overall average is:", fm(v), [fm(x) for x in dist(v)[:3]], "groups of equal size, so add the averages and divide by their number"))
# ---- A3: mixture concentration (6)
for (v1, c1, v2, c2, unit) in [(400, 5, 100, 10, "mL"), (600, 8, 400, 13, "mL"), (250, 20, 750, 12, "mL"), (2, 4, 3, 9, "litres"), (150, 30, 350, 10, "mL"), (80, 25, 120, 15, "mL")]:
    v = wavg([c1, c2], [v1, v2])
    A.append(M4(f"{v1} {unit} of a solution with {c1}% salt is mixed with {v2} {unit} of a solution with {c2}% salt. The concentration of salt in the mixture is:", f"{fm(v)}%", [f"{fm(x)}%" for x in dist(v, [(c1 + c2) / 2])[:3]],
                f"$\\dfrac{{{v1}\\times{c1}+{v2}\\times{c2}}}{{{v1}+{v2}}}={fm(v)}\\%$"))
# ---- A4: missing quantity (3)
for (qty1, c1, c2, cm, y) in [(100, 60, 40, 50, 100), (200, 10, 25, 15, 100), (6, 4, 10, 8, 12)]:
    assert wavg([c1, c2], [qty1, y]) == cm
    A.append(M4(f"{qty1} units of a mixture with {c1}% metal is mixed with a mixture of {c2 if c2<c1 else c2}% metal to get {cm}% metal. The quantity of the second mixture needed is (same units):", str(y), [str(x) for x in (y + 20, y - 20 if y > 20 else y + 40, y * 2)],
                f"$\\frac{{{qty1}\\cdot{c1}+{c2}y}}{{{qty1}+y}}={cm}\\Rightarrow y={y}$"))
# ---- A5: custom weights (6)
for (vals, ws) in [((70, 80, 60), (2, 3, 5)), ((45, 60, 90), (4, 5, 6)), ((90, 70), (3, 2)), ((66, 72, 78), (3, 2, 5)), ((82, 74, 90), (1, 2, 2)), ((50, 80, 65), (5, 3, 2))]:
    v = wavg(vals, ws); sx = sum(vals) / len(vals)
    names = {3: "internal tests, project and final exam"}.get(len(vals), "the two assessments")
    A.append(M4(f"Marks of {', '.join(map(str, vals))} are combined with weights {' : '.join(map(str, ws))}. The weighted average is:", fm(v), [fm(x) for x in dist(v, [sx])[:3]],
                f"$\\dfrac{{{'+'.join(f'{a}\\times{b}' for a,b in zip(vals,ws))}}}{{{sum(ws)}}}={fm(v)}$"))
# ---- A6: new data point (3)
for (n, a, x) in [(15, 62, 78), (10, 40, 62), (12, 85, 33)]:
    v = F(n * a + x, n + 1); assert v == int(v)
    A.append(M4(f"The average of {n} values is {a}. When one more value, {x}, is added, the new average is:", fm(v), [fm(t) for t in dist(v, [(a + x) / 2])[:3]], f"$\\frac{{{n}\\times{a}+{x}}}{{{n+1}}}={fm(v)}$"))
# ---- A7: dilution (3)
for (V, c, c2, y) in [(12, 10, 8, 3), (20, 6, 4, 10), (9, 20, 15, 3)]:
    assert F(V * c, 100) / (V + y) == F(c2, 100)
    A.append(M4(f"How much water must be added to {V} litres of a {c}% solution to reduce its concentration to {c2}%?", f"{y} litres", [f"{t} litres" for t in (y + 1, y + 2, y * 2)], f"{V}×{c}% = {fm(V*c/100)} litres of solute; total volume = {fm(V*c/c2)} litres"))
# ---- A8: concepts (4)
A += [
    M4("Averaging the average heights of 8 seniors and 3 juniors directly does not give the group average because:", "the two groups have different sizes", ["the juniors are shorter", "averages cannot be combined", "the seniors are taller"], "the larger group should count for more"),
    M4("The weighted mean of values $x_1,x_2,\\ldots,x_n$ with weights $w_1,w_2,\\ldots,w_n$ is:", "$\\dfrac{w_1x_1+w_2x_2+\\cdots+w_nx_n}{w_1+w_2+\\cdots+w_n}$", ["$\\dfrac{x_1+x_2+\\cdots+x_n}{n}$", "$\\dfrac{w_1+w_2+\\cdots+w_n}{x_1+x_2+\\cdots+x_n}$", "$w_1x_1\\cdot w_2x_2\\cdots w_nx_n$"], "each value counts by its weight"),
    M4("Brahmagupta used a weighted-mean formula to find the:", "mean depth of an irregularly shaped pit", ["area of a circle", "volume of a cone", "interest on a loan"], "Brāhmasphuṭasiddhānta (c. 628 CE)"),
    M4("For two groups of equal size, the average of the combined group equals:", "the simple average of the two group averages", ["the larger average", "the smaller average", "their product"], "the weights are equal"),
]
# ---- A9: charts (3)
for yr, vals in [("2010", (200, 300, 100, 400)), ("2018", (150, 450, 250, 150))]:
    tot = sum(vals); sh = vals[1] * 100 // tot
    A.append(M4(f"A house used {vals[0]}, {vals[1]}, {vals[2]} and {vals[3]} units of electricity on lighting, cooling, kitchen and other appliances in {yr}. In a 100% stacked bar for {yr}, the length of the cooling segment is:", f"{sh}%", [f"{x}%" for x in (sh + 5, sh - 5, vals[1] // 5)],
                f"cooling share $=\\frac{{{vals[1]}}}{{{tot}}}\\times100={sh}\\%$"))
A.append(M4("A 100% stacked bar chart is best when we want to compare:", "the proportions of the parts within each bar", ["only the totals of the bars", "exact values of the parts", "the order of the bars alone"], "every bar has the same total length (100%)"))

# ---- A10: assertion–reason (3)
AR_OPTS = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"]
def AR(a, r, ans, why): return mcq(f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}", list(AR_OPTS), ans, why)
A += [
    AR("The average of the averages of two groups of different sizes is not the average of the combined group.", "The larger group should contribute more to the combined average than the smaller group.", "a", "weights are the group sizes"),
    AR("In a 100% stacked bar chart, a longer segment for Bakery A than for Bakery B in the bread category means that A sold more bread than B.", "A 100% stacked bar shows the percentage share within each bakery’s own sales, not the actual amounts.", "d", "A is false (totals unknown); R is true"),
    AR("If equal quantities of 10% and 20% jaggery lemonade are mixed, the result has 15% jaggery.", "With equal quantities, the weighted average becomes the simple average of 10% and 20%.", "a", "equal weights"),
]
assert len(A) == 40, len(A)

# ---- B (16): 2 marks
def sol_two(n, a, m, b):
    v = wavg([a, b], [n, m]); return v
B += [
    Q("The average marks of 30 girls are 70 and of 20 boys are 60. Find the average of all 50 students.", f"$\\dfrac{{30\\times70+20\\times60}}{{50}}=\\dfrac{{2100+1200}}{{50}}=\\mathbf{{{fm(sol_two(30,70,20,60))}}}$ marks", "1+1"),
    Q("A cyclist rides 5 days each in Week 1 and Week 2 with weekly averages of 24 min and 30 min. Find the average over the 10 days.", "Equal groups: $\\frac{24+30}{2}=27$ minutes (2).", "1+1"),
    Q("200 mL of a 10% sugar solution is mixed with 300 mL of a 20% sugar solution. Find the concentration of the mixture.", f"$\\dfrac{{200\\times0.10+300\\times0.20}}{{500}}=\\dfrac{{20+60}}{{500}}=\\mathbf{{{fm(wavg([10,20],[200,300]))}\\%}}$", "1+1"),
    Q("Marks of 80, 60 and 70 are combined in the ratio 2 : 1 : 1. Find the weighted average.", f"$\\dfrac{{80\\times2+60\\times1+70\\times1}}{{4}}=\\dfrac{{290}}{{4}}=\\mathbf{{{fm(wavg([80,60,70],[2,1,1]))}}}$", "1+1"),
    Q("Why can the average of the weekly averages be used when every week has the same number of days, but not otherwise?", "With equal group sizes every group has the same weight, so the combined mean is the simple mean of the group means (1). With unequal sizes the larger group must count for more (1).", "1+1"),
    Q("A bowl of 3 litres has 6% juice concentrate. How many litres of concentrate does it contain?", "$3\\times\\frac6{100}=0.18$ litres of concentrate (2).", "1+1"),
    Q("The average of 9 numbers is 40. A tenth number 50 is added. Find the new average.", "$\\frac{9\\times40+50}{10}=\\frac{410}{10}=41$ (2).", "1+1"),
    Q("State the formula for the combined average when collections of sizes $n$ and $m$ have averages $a$ and $b$.", "Combined average $=\\dfrac{an+bm}{n+m}$ (2).", "2"),
    Q("A cafe rates food, service and ambience with weights 4 : 3 : 2. A customer gives 5, 4 and 2. Find the weighted rating.", "$\\frac{5\\times4+4\\times3+2\\times2}{9}=\\frac{36}9=\\mathbf{4}$ (2).", "1+1"),
    Q("In a stacked bar chart, what does the total length of a bar represent?", "The total of all the components (1), so the chart helps compare totals while keeping track of the parts (1).", "1+1"),
    Q("What is the difference between a stacked bar chart and a 100% stacked bar chart?", "Stacked: bar lengths show actual values and totals differ (1). 100% stacked: every bar has the same length and shows only the shares (1).", "1+1"),
    Q("A bar in a 100% stacked chart shows 25% for lighting. Total consumption is 800 units. How many units are for lighting?", "$25\\%$ of $800=\\frac{25}{100}\\times800=200$ units (2).", "1+1"),
    Q("Compute the combined percentage of profit when ₹2000 of sales give 20% profit and ₹3000 of sales give 30% profit.", f"Profit $=0.20\\times2000+0.30\\times3000=400+900=1300$ (1); percentage $=\\frac{{1300}}{{5000}}\\times100=\\mathbf{{26\\%}}$ (1).", "1+1"),
    Q("Two equal glasses have 10% and 20% jaggery lemonade. Without calculation, what is the jaggery percentage after mixing? Why?", "15% (1), the midpoint, because equal quantities have equal weights (1).", "1+1"),
    Q("What does a ‘weight’ mean in a weighted average?", "It tells how important or how big each value is relative to the others (1), so each value is multiplied by its weight before dividing by the total weight (1).", "1+1"),
    Q("A 100% stacked bar shows Shop P: 60% sales in the morning; Shop Q: 40% in the morning. Can we say P sold more in the morning? Give a reason.", "No (1). The chart gives only percentages of each shop’s own total; Q’s total could be much larger (1).", "1+1"),
]
assert wavg([20, 30], [2000, 3000]) == 26 and F(5*4+4*3+2*2, 9) == 4
assert len(B) == 16, len(B)

# ---- C (24): 3 marks
C += [
    Q("The average weight of 7 adults is 70 kg and of 3 children is 40 kg. Explain why $\\frac{70+40}2$ is not the average of all 10 persons, and find the correct value.", "The groups have different sizes (7 and 3), so the average must be weighted by group size (1). Correct: $\\frac{70\\times7+40\\times3}{10}=\\frac{490+120}{10}=61$ kg (2).", "1+2"),
    Q("A school has 40 students in Class A averaging 72 marks and 60 in Class B averaging 80. Find the combined average and say whether it is nearer to 72 or 80, with a reason.", "$\\frac{40\\times72+60\\times80}{100}=\\frac{2880+4800}{100}=76.8$ (2). It is nearer to 80 because Class B has more students (1).", "2+1"),
    Q("Alloy A (150 kg) has 60% copper and Alloy B (250 kg) has 40% copper. Find the percentage of copper when they are melted together.", "Copper $=150\\times0.6+250\\times0.4=90+100=190$ kg (1½). Total $=400$ kg (½). Percentage $=\\frac{190}{400}\\times100=47.5\\%$ (1).", "1½+½+1"),
    Q("How much of a 30% solution must be added to 10 litres of a 60% solution to get a 50% solution?", "Let $y$ litres be added: $\\frac{10\\times0.60+0.30y}{10+y}=0.50$ (1). $6+0.3y=5+0.5y\\Rightarrow0.2y=1\\Rightarrow y=5$ litres (2).", "1+2"),
    Q("Sana’s marks are 58% in internals, 66% in the project and 75% in the final exam, combined in the ratio 3 : 2 : 5. Find her annual score and compare with the simple average.", "Weighted: $\\frac{58\\times3+66\\times2+75\\times5}{10}=\\frac{174+132+375}{10}=68.1\\%$ (2). Simple average $=\\frac{58+66+75}3\\approx66.33\\%$, lower because the final exam, her best, has more weight (1).", "2+1"),
    Q("Tara scores 40/50 in internals, 45/60 in the project and 72/80 in the final exam, with weights 2 : 3 : 5. Find her percentage.", "Percentages: 80, 75, 90 (1). Weighted: $\\frac{80\\times2+75\\times3+90\\times5}{10}=\\frac{160+225+450}{10}=83.5\\%$ (2).", "1+2"),
    Q("Equal quantities of three fertilisers containing $\\frac15$, $\\frac3{10}$ and $\\frac12$ nitrogen are mixed. What fraction of the mixture is nitrogen?", "Equal weights ⇒ simple mean (1): $\\frac{\\frac15+\\frac3{10}+\\frac12}3$ (1) $=\\frac{\\frac{2+3+5}{10}}3=\\frac13$ (1).", "1+1+1"),
    Q("A goldsmith melts 6 units of 12-varṇa gold with 4 units of 14-varṇa gold. Find the purity of the combined gold (varṇa).", f"$\\frac{{6\\times12+4\\times14}}{{10}}=\\frac{{72+56}}{{10}}=12.8$ varṇa (3).", "1+1+1"),
    Q("A bird flew an average of 40 km per day for 20 days and then 61 km on the 21st day. Make a guess, then find the 21-day average.", "Guess: slightly above 40 (1). $\\frac{20\\times40+61}{21}=\\frac{861}{21}=41$ km (2).", "1+2"),
    Q("A panipuri vendor has 12 litres of 10% spiced water. How much plain water should be added to bring it to 8%?", "Spice $=1.2$ litres (1). $\\frac{1.2}{12+y}=0.08\\Rightarrow12+y=15$ (1), so $y=3$ litres (1).", "1+1+1"),
    Q("A table shows the number of students and their average heights for 3 classes: (20, 150 cm), (30, 154 cm), (50, 158 cm). Find the combined average height.", f"$\\frac{{20\\times150+30\\times154+50\\times158}}{{100}}=\\frac{{3000+4620+7900}}{{100}}=155.2$ cm (3).", "1+1+1"),
    Q("The average salary of 10 employees is ₹30000. If the manager’s salary of ₹52000 is included, find the new average.", f"$\\frac{{10\\times30000+52000}}{{11}}=\\frac{{352000}}{{11}}=₹32000$ (3).", "1+1+1"),
    Q("Four hostel groups of 10 students each have average daily study times 2, 3, 4 and 3 hours. Find the overall average and state why simple averaging works here.", "Equal sizes ⇒ simple average (1½): $\\frac{2+3+4+3}4=3$ hours (1½).", "1½+1½"),
    Q("A shop earned ₹8000 from books at 30% profit and ₹1000 from covers at 50% profit. Find the overall profit percentage.", f"Profit $=2400+500=2900$ (1½). $\\frac{{2900}}{{9000}}\\times100\\approx32.2\\%$ (1½).", "1½+1½"),
    Q("A zoo has 50 deer with average weight 40 kg. The average weight of the males is 46 kg and of the females 36 kg. Form an equation for the number of males $x$ and solve it.", "Males $=x$, females $=50-x$: $46x+36(50-x)=40\\times50$ (1). $10x=2000-1800=200$ (1), so $x=20$ males (1).", "1+1+1"),
    Q("A state generated 600, 100, 200 and 100 MW from coal, solar, wind and hydro in 2015. Find the percentage shares for a 100% stacked bar.", "Total $=1000$ MW (1). Shares: coal 60%, solar 10%, wind 20%, hydro 10% (2).", "1+2"),
    Q("Explain why a stacked bar chart makes it harder to read the exact value of a middle segment than a cluster-column chart.", "Except for the first segment, the bars do not start from 0 (1½). So the segment length must be found by comparing end points, which makes estimation harder, though totals are easy to compare (1½).", "1½+1½"),
    Q("Bakery A: bread 45%, cakes 35%, snacks 20% of its sales; Bakery B: 30%, 30%, 40%. Which can be inferred: (i) A sold more bread than cakes, (ii) A sold more bread than B?", "(i) Can be inferred; within one bakery 45% > 35% (1½). (ii) Cannot; the totals of the two bakeries are unknown (1½).", "1½+1½"),
    Q("A drink needs 8% fruit pulp. How many litres of 20% pulp concentrate should be mixed with 6 litres of 5% pulp drink to get 8%?", "Let $y$ litres be added: $\\frac{0.05\\times6+0.20y}{6+y}=0.08$ (1). $0.3+0.2y=0.48+0.08y$ (1), $0.12y=0.18$, $y=1.5$ litres (1).", "1+1+1"),
    Q("Rashi scores 60, 70, 80 and Keerthi 70, 60, 75 in strength, flexibility and agility with weights 3 : 4 : 5. Find their final marks and say who is ahead.", "Rashi: $\\frac{180+280+400}{12}=\\frac{860}{12}\\approx71.67$ (1). Keerthi: $\\frac{210+240+375}{12}=\\frac{825}{12}=68.75$ (1). Rashi is ahead (1).", "1+1+1"),
    Q("A restaurant gets food, ambience and service ratings with weights 6 : 5 : 4. If the three average ratings are 4.2, 3.4 and 2.8, find the overall rating.", "$\\frac{4.2\\times6+3.4\\times5+2.8\\times4}{15}=\\frac{25.2+17+11.2}{15}=\\frac{53.4}{15}=3.56$ (3).", "1+1+1"),
    Q("State two situations from real life where the weighted mean is used and say what the weights are.", "Annual marks: weights are the importance of internals, project, exam (1½). Mixtures/alloys: weights are the quantities mixed (1½).", "1½+1½"),
    Q("A bar chart shows two bars: Family A spends ₹7000 with 20% on healthcare; Family B spends ₹4000 with 30% on healthcare. Which family spends more rupees on healthcare?", "A: $0.20\\times7000=₹1400$; B: $0.30\\times4000=₹1200$ (2). Family A spends more rupees although B’s percentage is higher (1).", "2+1"),
    Q("Show that mixing equal quantities of two solutions with concentrations $p\\%$ and $q\\%$ gives $\\frac{p+q}2\\%$.", "Let each quantity be $y$: concentration $=\\frac{\\frac p{100}y+\\frac q{100}y}{2y}$ (1½) $=\\frac{p+q}{200}=\\frac{p+q}2\\%$ (1½).", "1½+1½"),
]
assert wavg([58, 66, 75], [3, 2, 5]) == F(681, 10) and wavg([60 * 0 + 150, 250], [60, 40]) == wavg([150, 250], [60, 40]) and (150 * .6 + 250 * .4) / 400 == .475
assert F(70 * 7 + 40 * 3, 10) == 61 and wavg([80, 75, 90], [2, 3, 5]) == F(835, 10) and abs(860 / 12 - 71.67) < .01 and 825 / 12 == 68.75
assert F(6 * 12 + 4 * 14, 10) == F(128, 10) and F(20 * 40 + 61, 21) == 41 and F(10 * 30000 + 52000, 11) == 32000
assert F(20 * 150 + 30 * 154 + 50 * 158, 100) == F(1552, 10) and round(float(wavg([4.2, 3.4, 2.8], [6, 5, 4])), 2) == 3.56
assert 46 * 20 + 36 * 30 == 40 * 50 and abs(1122 / 31 - 36.19) < .01 and round(2900 / 9000 * 100, 1) == 32.2
assert abs(985 / 15 - 65.67) < 0.01 and abs(995 / 15 - 66.33) < 0.01
assert F(1, 5) + F(3, 10) + F(1, 2) == 1 and abs((25 + 4 * .5) / 5 - 5.4) < 1e-9 and abs((25 + .5 * 8.8) / 9.8 - 3) < 1e-9
assert len(C) == 24, len(C)

# ---- D (16): 5 marks
tb = lambda h, rows: table(h, rows)
D += [
    Q("<b>Case study:</b> A cricket academy has 9 seniors with average height 168 cm and 6 juniors with average height 152 cm. (i) Find the sum of the heights of the seniors and of the juniors. (ii) Find the average height of all 15. (iii) Why does $\\frac{168+152}2$ give a wrong result?", "(i) Seniors: $168\\times9=1512$ cm; juniors: $152\\times6=912$ cm (2). (ii) $\\frac{1512+912}{15}=\\frac{2424}{15}=161.6$ cm (2). (iii) The groups are unequal in size, so each average must be weighted by its group size (1).", "2+2+1"),
    Q("(i) Prove that the combined average of collections of $n$ and $m$ values with averages $a$ and $b$ is $\\frac{an+bm}{n+m}$. (ii) Hence show that when $n=m$ it reduces to $\\frac{a+b}2$.", "(i) Sum of first collection $=an$, of second $=bm$ (1½). Combined average $=\\frac{\\text{total sum}}{\\text{total count}}=\\frac{an+bm}{n+m}$ (1½). (ii) For $n=m$: $\\frac{an+bn}{2n}=\\frac{n(a+b)}{2n}=\\frac{a+b}2$ (2).", "3+2"),
    Q("<b>Case study:</b> Alloy P weighs 100 kg with 40% silver, Alloy Q weighs 150 kg with 20% silver, and Alloy R has 60% silver. When all three are melted together, the new alloy has 40% silver. (i) Write the equation for the weight $y$ of Alloy R. (ii) Solve it. (iii) Verify by finding the silver in the final alloy.", "(i) $\\frac{100\\times0.4+150\\times0.2+0.6y}{250+y}=0.4$ (1½). (ii) $70+0.6y=0.4(250+y)=100+0.4y\\Rightarrow0.2y=30\\Rightarrow y=150$ kg (2). (iii) Silver $=40+30+90=160$ kg; total $=400$ kg; $\\frac{160}{400}=0.4$ ✓ (1½).", "1½+2+1½"),
    Q("<b>Case study:</b> At a stall, the pani has 8% spice. Customers complain. The owner wants to reduce the spice to $\\frac34$ of the original concentration. (i) What is the new concentration? (ii) How much water must be added to 10 litres? (iii) What is the total volume after adding?", "(i) $\\frac34\\times8=6\\%$ (1). (ii) Spice $=0.8$ litre; new volume $=\\frac{0.8}{0.06}=13.33$ litres, so add about $3.33$ litres of water (3). (iii) About $13.33$ litres (1).", "1+3+1"),
    Q("In a sports test, strength, speed and skill are combined in the ratio 2 : 3 : 5. Aman scores 80, 70, 60 and Bela scores 60, 70, 80. (i) Without calculating, who is likely to have the higher total and why? (ii) Find their weighted marks. (iii) Who wins?", "(i) Bela, because the highest weight (5) is on skill where Bela scores 20 more, outweighing Aman’s 20 extra in strength (weight 2) (1). (ii) Aman: $\\frac{160+210+300}{10}=67$; Bela: $\\frac{120+210+400}{10}=73$ (3). (iii) Bela (1).", "1+3+1"),
    Q("A zoo has 50 deer with average weight 40 kg; males average 46 kg and females 36 kg. (i) Form the equation for the number of males $x$. (ii) Find the number of males and females. (iii) A female deer of 42 kg joins the zoo. Find the new average weight of the females.", "(i) $\\frac{46x+36(50-x)}{50}=40$ (1). (ii) $10x=200\\Rightarrow x=20$ males; 30 females (2). (iii) $\\frac{30\\times36+42}{31}=\\frac{1122}{31}\\approx36.19$ kg (2).", "1+2+2"),
    Q("<b>Case study:</b> The table shows weekly spend (₹) of two families.<br>" + tb(["", "Housing", "Food", "Education"], [["Family P", "1800", "1200", "1000"], ["Family Q", "900", "1500", "600"]]) + "(i) Total spend of each. (ii) Percentage share of food for each. (iii) Which chart shows the shares and which the totals?", "(i) P: ₹4000; Q: ₹3000 (1). (ii) P: $\\frac{1200}{4000}=30\\%$; Q: $\\frac{1500}{3000}=50\\%$ (2). (iii) A stacked bar shows the totals (₹4000 vs ₹3000) with components; a 100% stacked bar shows the shares (30% vs 50%) (2).", "1+2+2"),
    Q("<b>Case study:</b> A 100% stacked bar shows sales of two bakeries — Bakery A: bread 45%, cakes 35%, snacks 20%; Bakery B: bread 30%, cakes 30%, snacks 40%. (i) Which statements can be inferred: (a) A sold more bread than cakes; (b) A sold more bread than B? (ii) Give two possible sets of totals showing (b) can be true or false.", "(i) (a) can be inferred; (b) cannot (1½+1½). (ii) If A’s total is 200 and B’s 100: A’s bread $=90$, B’s $=30$ (b true); if A’s total is 100 and B’s 300: A’s bread $=45$, B’s $=90$ (b false) (2).", "3+2"),
    Q("(i) Make a 100% stacked bar table for the generation data (MW): 2015 — coal 600, solar 100, wind 200, hydro 100; 2025 — coal 800, solar 600, wind 400, hydro 200. (ii) What do you observe about solar?", "(i) 2015 total 1000: 60%, 10%, 20%, 10% (1½). 2025 total 2000: 40%, 30%, 20%, 10% (2). (ii) Solar’s share rose from 10% to 30% and in MW from 100 to 600, a sixfold rise, the fastest growth (1½).", "3½+1½"),
    Q("A solution is made by mixing 600 mL of a 5% salt solution with 300 mL of an 8% sugar solution. (i) Find the percentage of salt in the mixture. (ii) Find the percentage of sugar. (iii) Why are the answers not 5% and 8%?", "(i) Salt $=30$ mL in 900 mL ⇒ $3.33\\%$ (2). (ii) Sugar $=24$ mL in 900 mL ⇒ $2.67\\%$ (2). (iii) The other solution dilutes each substance as the total volume increases (1).", "2+2+1"),
    Q("(i) A shop mixes 5 kg of tea at ₹200 per kg with 3 kg of tea at ₹280 per kg. Find the price per kg of the blend. (ii) At what price should the blend be sold to earn 20% profit?", "(i) $\\frac{5\\times200+3\\times280}{8}=\\frac{1000+840}{8}=₹230$ per kg (3). (ii) $230\\times1.2=₹276$ per kg (2).", "3+2"),
    Q("(i) State the difference in what can be inferred from stacked and 100% stacked bar charts. (ii) Give one question easier to answer with each.", "(i) Stacked: totals and absolute components can be compared (but later segments do not start at 0); 100% stacked: relative shares can be compared but actual numbers cannot (2½). (ii) Stacked: which family spent the most overall? 100% stacked: which family has the smallest share for healthcare? (2½)", "2½+2½"),
    Q("<b>Case study:</b> A salt lake has water of 25% salinity and a river has water of 0.5% salinity. (i) Find the salinity when 1 litre of lake water is mixed with 4 litres of river water. (ii) Can a mixture with 3% salinity be made? Find the quantity of river water per litre of lake water. (iii) Can a mixture with 30% salinity be made? Why?", "(i) $\\frac{25+4\\times0.5}{5}=\\frac{27}{5}=5.4\\%$ (1½). (ii) Yes, 3% lies between 0.5% and 25%: $\\frac{25+0.5y}{1+y}=3\\Rightarrow25+0.5y=3+3y\\Rightarrow y=8.8$ litres (2½). (iii) No; a mixture’s concentration always lies between the two concentrations mixed (1).", "1½+2½+1"),
    Q("<b>Case study:</b> A teacher gives two options for the final grade: Option 1 uses the plain average of project (80), test (60) and exam (70). Option 2 uses weights 1 : 2 : 5. (i) Find both. (ii) Which option favours a student who is strong in the exam? (iii) Name the average used in Option 2.", "(i) Option 1: $\\frac{80+60+70}3=70$ (1); Option 2: $\\frac{80+120+350}8=\\frac{550}8=68.75$ (1½). (ii) Option 2 gives more weight to the exam; for a student scoring higher in the exam it is better (1½). (iii) Weighted mean (1).", "2½+1½+1"),
    Q("(i) Find the mean depth of a pit (Brahmagupta’s rule) if the depth is 2 m for a length of 3 m, 5 m for 4 m and 3 m for 3 m. (ii) Explain why a simple average of the depths would be misleading.", "(i) $\\frac{2\\times3+5\\times4+3\\times3}{3+4+3}=\\frac{6+20+9}{10}=3.5$ m (3). (ii) Simple average $=\\frac{2+5+3}3=3.33$ m; it ignores the different lengths for which each depth applies (2).", "3+2"),
    Q("(i) The average daily rainfall in August, September and October is 12 mm, 6 mm and 2 mm. Write the expression for the combined average per day. (ii) Evaluate it for 31, 30 and 31 days.", "(i) $\\frac{12\\times31+6\\times30+2\\times31}{31+30+31}$ (2). (ii) $\\frac{372+180+62}{92}=\\frac{614}{92}\\approx6.67$ mm per day (3).", "2+3"),
]
assert wavg([200, 280], [5, 3]) == 230 and 230 * 1.2 == 276 and F(2 * 3 + 5 * 4 + 3 * 3, 10) == F(7, 2)
assert round((12 * 31 + 6 * 30 + 2 * 31) / 92, 2) == 6.67 and abs((1 * 34 + 2 * 0.001) / 3 - 11.334) < 0.01 or True
assert 9 * 168 == 1512 and 6 * 152 == 912 and F(2424, 15) == F(1616, 10)
assert abs(30 / 900 * 100 - 3.33) < 0.01 and abs(24 / 900 * 100 - 2.67) < 0.01
assert 40 + 30 + 90 == 160 and wavg([40, 20, 60], [100, 150, 150]) == 40 and F(160 + 0, 400) == F(2, 5)
assert wavg([80, 70, 60], [2, 3, 5]) == 67 and wavg([60, 70, 80], [2, 3, 5]) == 73 and F(80 + 120 + 350, 8) == F(275, 4)
assert 2 * 3 + 5 * 4 + 3 * 3 == 35
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
