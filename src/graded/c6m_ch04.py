"""Class 6 Maths Ch 4 - Data Handling and Presentation."""
import random
from g67 import *

SLUG, NAME, CHNO = "Data_Handling", "Data Handling and Presentation", 4

def tbl(items, h=("Item", "Number")):
    return table(list(h), [[k, v] for k, v in items])
def raw_list(seed, n=20, lo=1, hi=6):
    k = 0
    while True:
        r = random.Random(seed + 1000 * k); xs = [r.randint(lo, hi) for _ in range(n)]
        cnt = sorted((xs.count(v) for v in set(xs)), reverse=True)
        if len(cnt) == 1 or cnt[0] > cnt[1]: return xs
        k += 1
def lst(xs): return ", ".join(map(str, xs))
def tally(n):
    f, e = divmod(n, 5)
    a = f"{f} bundle{'s' if f != 1 else ''} of five" if f else ""
    b = f"{e} single stroke{'s' if e != 1 else ''}" if e else ""
    return (a + " and " + b) if a and b else (a or b)
FRUITS = ["Apple", "Mango", "Banana", "Orange", "Guava", "Grapes"]
SPORTS = ["Cricket", "Football", "Hockey", "Kabaddi", "Tennis", "Chess"]
def D(seed, names, lo=10, hi=60, step=5, k=5):
    j = 0
    while True:
        r = random.Random(seed + 1000 * j); d = [(nm_, r.randrange(lo, hi, step)) for nm_ in r.sample(names, k)]
        v = sorted(x[1] for x in d)
        if v[-1] > v[-2] and v[0] < v[1]: return d
        j += 1
def top(d): return max(d, key=lambda x: x[1]);
def bot(d): return min(d, key=lambda x: x[1])

# ---------- EASY ----------
eA1 = [nw(f"In a pictograph, one symbol stands for {k} children. The number of children shown by {s} symbols is:", k * s, [k + s, k * (s + 1), k * (s - 1)], "Multiply the symbols by the value of one symbol.") for k, s in [(5, 6), (10, 7), (4, 8), (20, 5), (25, 4)]]
eA2 = [nw(f"A bar graph uses a scale of 1 cm = {k} books. A bar of height {h} cm shows how many books?", k * h, [k + h, k * (h + 1), k * (h - 1)], "Multiply the height by the scale.") for k, h in [(5, 7), (10, 6), (20, 8), (4, 9), (50, 5)]]
eA3 = [tm(f"The tally marks for {n} are shown as:", tally(n), [tally(n + 1), tally(n - 1), tally(n + 5)], "Every fifth stroke crosses the four before it, making a bundle of five.") for n in [7, 12, 18, 23]]
eA4 = []
for sd in [1, 2, 3, 4, 5]:
    d = D(sd, FRUITS, 10, 50, 5, 4); t = top(d)
    eA4.append(tm("In the table, which fruit has the highest number?<br>" + tbl(d), t[0], [x[0] for x in d if x[0] != t[0]], "Look for the largest number."))
eA5 = []
for sd in [11, 12, 13, 14, 15]:
    d = D(sd, SPORTS, 10, 50, 5, 4); b = bot(d)
    eA5.append(tm("Which sport is the least liked?<br>" + tbl(d, ("Sport", "Students")), b[0], [x[0] for x in d if x[0] != b[0]], "Look for the smallest number."))
eA6 = []
for sd in [21, 22, 23, 24, 25]:
    xs = raw_list(sd, 12, 1, 5); v = (sd % 5) + 1; c = xs.count(v)
    eA6.append(nw(f"In the data {lst(xs)}, how many times does {v} occur?", c, [c + 1, c - 1, c + 2, len(xs) - c, c + 3], "Count (tally) the number of times."))
eA7 = [tm(q, a, w, "Definition") for q, a, w in [("Information collected for a purpose is called:", "data", ["a scale", "a key", "a symbol"]), ("A graph that uses pictures or symbols to show data is a:", "pictograph", ["bar graph", "number line", "tally chart"]), ("The explanation of what one symbol stands for is given in the:", "key", ["title", "tally", "table"])]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([QQ(f"A pictograph uses one symbol for {k} students. If there are {s} symbols for Class VI, how many students are there?", f"Each symbol is {k} students", f"${s}\\times{k}={s*k}$ students") for k, s in [(10, 6), (5, 9), (20, 4), (15, 5)]]
          + [QQ(f"Show {n} using tally marks (describe the bundles).", "Draw strokes; every fifth stroke crosses four", f"{n} = {tally(n)}") for n in [9, 14, 16, 22]]
          + [QQ(f"A bar graph has a scale 1 cm = {k} students. How many students are shown by a bar of {h} cm?", f"Multiply: ${h}\\times{k}$", f"${h*k}$ students") for k, h in [(10, 4), (5, 9), (20, 3), (50, 6)]])
EASY_C = ([QQ("Read the table and find the total number.<br>" + tbl(d), "Add all the numbers", f"Total $=" + "+".join(str(x[1]) for x in d) + f"={sum(x[1] for x in d)}$", "Hence the total is " + str(sum(x[1] for x in d))) for d in [D(s, FRUITS, 10, 40, 5, 4) for s in [31, 32, 33, 34, 35, 36]]]
          + [QQ(f"Make a frequency table with tally marks for the data: {lst(xs)}.", "Count each value", "; ".join(f"{v}: {xs.count(v)}" for v in sorted(set(xs))), f"Total $={len(xs)}$") for xs in [raw_list(s, 15, 1, 4) for s in [41, 42, 43, 44, 45, 46]]]
          + [QQ("Which is the most popular and which is the least popular item? Find the difference.<br>" + tbl(d), f"Most: {top(d)[0]} ({top(d)[1]})", f"Least: {bot(d)[0]} ({bot(d)[1]})", f"Difference $={top(d)[1]-bot(d)[1]}$") for d in [D(s, SPORTS, 10, 60, 5, 4) for s in [51, 52, 53, 54, 55, 56]]])
EASY_D = ([QQ(f"A pictograph uses one symbol = {k} students. Class A has {a} symbols, Class B has {b} symbols and Class C has {c} symbols. Find the number of students in each class and the total.", f"A: ${a}\\times{k}={a*k}$", f"B: ${b}\\times{k}={b*k}$", f"C: ${c}\\times{k}={c*k}$", f"Total $={(a+b+c)*k}$") for k, a, b, c in [(10, 4, 6, 5), (5, 7, 9, 6), (20, 3, 5, 4), (15, 4, 3, 6), (25, 2, 5, 3), (30, 3, 4, 5)]]
          + [QQ(f"A bar graph (scale 1 cm = {k} books) has bars of heights {a} cm, {b} cm and {c} cm for Monday, Tuesday and Wednesday. Find the books sold each day and the total.", f"Monday ${a*k}$", f"Tuesday ${b*k}$", f"Wednesday ${c*k}$", f"Total ${(a+b+c)*k}$ books") for k, a, b, c in [(10, 3, 5, 4), (20, 2, 4, 6), (5, 8, 6, 7), (25, 4, 3, 5), (15, 2, 6, 4), (50, 3, 2, 5)]])

# ---------- NCERT ----------
nA1 = [nw(f"In a pictograph one symbol stands for {k} units. How many symbols (counting a half symbol as half) are needed to show {n}?", Dc(n) / k, [n * k, Dc(n) // k, Dc(n) // k + 1, Dc(n) / k + 1, Dc(n) / k - 1], "Divide by the value of one symbol.") for k, n in [(10, 45), (20, 70), (5, 35), (4, 18), (50, 125)]]
nA2 = [nw(f"A bar graph has scale 1 cm = {k} students. A bar showing {n} students will have height (in cm):", n // k, [n * k, n - k, n // k + 2, n // k - 2], "Divide the number by the scale.") for k, n in [(5, 40), (10, 90), (20, 140), (4, 28)]]
nA3 = []
for sd in [61, 62, 63, 64]:
    d = D(sd, FRUITS, 10, 70, 5, 3); a, b = d[0], d[1]
    nA3.append(nw(f"Using the table, how many more are there of {a[0]} than {b[0]}?<br>" + tbl(d), abs(a[1] - b[1]) if a[1] > b[1] else None, [a[1] + b[1], a[1] - b[1] + 5, a[1] - b[1] - 5, a[1] - b[1] + 10], "Subtract the smaller number from the larger.") if a[1] > b[1] else nw(f"Using the table, how many more are there of {b[0]} than {a[0]}?<br>" + tbl(d), b[1] - a[1], [a[1] + b[1], b[1] - a[1] + 5, b[1] - a[1] - 5, b[1] - a[1] + 10], "Subtract the smaller number from the larger."))
nA4 = []
for sd in [71, 72, 73, 74]:
    d = D(sd, SPORTS, 10, 70, 5, 3); t = sum(x[1] for x in d)
    nA4.append(nw("The total number of students in the table is:<br>" + tbl(d, ("Sport", "Students")), t, [t - bot(d)[1], t + 10, t - 5, t + 5], "Add all."))
nA5 = [nw(f"The number which occurs most often in the data {lst(xs)} is:", max(set(xs), key=lambda v: xs.count(v)), [v for v in sorted(set(xs), key=lambda v: -xs.count(v)) if v != max(set(xs), key=lambda v: xs.count(v))][:3] + [max(xs), min(xs), 7], "Count how many times each value appears.") for xs in [raw_list(s, 12, 1, 5) for s in [81, 82, 83, 84]]]
nA6 = [nw(f"In the data {lst(xs)}, how many values are greater than {m}?", sum(1 for x in xs if x > m), [sum(1 for x in xs if x >= m), sum(1 for x in xs if x < m), sum(1 for x in xs if x > m) + 1, sum(1 for x in xs if x > m) - 1, sum(1 for x in xs if x > m) + 2, sum(1 for x in xs if x > m) + 3], "Count the values bigger than the given number (not equal to it).") for xs, m in [(raw_list(s, 12, 1, 5), 2 + s % 3) for s in [91, 92, 93, 94]]]
nA7 = [nw(f"A pictograph where one symbol = {k} shows {a} full symbols and a half symbol. The number shown is:", k * a + k // 2, [k * a, k * (a + 1), k * a + k, k * a + 1], "Count the half symbol as half the value.") for k, a in [(10, 5), (20, 3), (4, 6), (50, 2)]]
nA8 = [tm(q, a, w, "Definition") for q, a, w in [("The number of times a value occurs in the data is its:", "frequency", ["range", "scale", "key"]), ("In a bar graph, the bars should have:", "equal width and equal gaps", ["different widths", "no gaps and no scale", "only one colour"])]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([QQ(f"Draw (describe) a pictograph for: {', '.join(f'{x[0]} {x[1]}' for x in d)} with one symbol = 5.", "Number of symbols = number $\\div5$", "; ".join(f"{x[0]}: {x[1]//5} symbols" for x in d)) for d in [D(s, FRUITS, 10, 40, 5, 3) for s in [101, 102, 103, 104]]]
           + [QQ(f"A bar graph is drawn with a scale of 1 cm = {k} students for the data below. Find the height of each bar.<br>" + tbl(d), f"Height $=$ number $\\div{k}$", "; ".join(f"{x[0]}: {x[1]//k} cm" for x in d)) for k, d in [(5, D(111, SPORTS, 10, 40, 5, 3)), (10, D(112, SPORTS, 20, 80, 10, 3)), (5, D(113, SPORTS, 15, 45, 5, 3)), (10, D(114, SPORTS, 10, 70, 10, 3))]]
           + [QQ(f"Write the frequency of each number in the data: {lst(xs)}.", "Count each value", "; ".join(f"{v}: {xs.count(v)}" for v in sorted(set(xs)))) for xs in [raw_list(s, 14, 1, 4) for s in [121, 122, 123, 124]]])
NCERT_C = ([QQ("Study the table and answer: (i) the largest, (ii) the smallest, (iii) the total.<br>" + tbl(d), f"(i) {top(d)[0]}: {top(d)[1]}", f"(ii) {bot(d)[0]}: {bot(d)[1]}", f"(iii) total $={sum(x[1] for x in d)}$") for d in [D(s, FRUITS, 10, 70, 5, 3) for s in [131, 132, 133, 134, 135, 136]]]
           + [QQ(f"A scale 1 cm = {k} units is used. Bars are of height {a} cm, {b} cm and {c} cm. Find the values, and the difference between the largest and the smallest.", f"Values: ${a*k}$, ${b*k}$, ${c*k}$", f"Largest $={max(a,b,c)*k}$, smallest $={min(a,b,c)*k}$", f"Difference $={(max(a,b,c)-min(a,b,c))*k}$") for k, a, b, c in [(10, 4, 7, 5), (5, 9, 3, 6), (20, 2, 5, 4), (50, 3, 6, 2), (4, 8, 5, 9), (25, 4, 2, 6)]]
           + [QQ(f"Which scale is better to draw a bar graph for values {', '.join(map(str, v))}: 1 cm = 1 unit or 1 cm = {k} units? Give the height of the largest bar with your chosen scale.", "A bar graph should fit on the page, so use the bigger scale", f"Largest value {max(v)} gives {max(v)//k} cm with 1 cm = {k}", "Hence choose 1 cm = " + str(k)) for v, k in [((20, 40, 60), 10), ((50, 100, 150), 25), ((30, 45, 60), 15), ((200, 400, 600), 100), ((8, 12, 20), 4), ((75, 125, 175), 25)]])
NCERT_D = ([QQ("The table shows data on favourite sports of students. Draw a pictograph taking one symbol = 5 students, and find the total number of symbols. Data: " + ", ".join(f"{x[0]} {x[1]}" for x in d) + ".", "; ".join(f"{x[0]}: {x[1]//5} symbols" for x in d), f"Total symbols $={sum(x[1] for x in d)//5}$", f"Total students $={sum(x[1] for x in d)}$", "Write the key: 1 symbol = 5 students") for d in [D(s, SPORTS, 10, 45, 5, 3) for s in [141, 142, 143, 144, 145, 146]]]
           + [QQ(f"Data of {n} students' number of siblings: {lst(xs)}. Prepare a frequency table, and find the most common number of siblings and how many students have more than 2 siblings.", "Count each value: " + "; ".join(f"{v}: {xs.count(v)}" for v in sorted(set(xs))), f"Most common: {max(set(xs), key=lambda v: (xs.count(v), -v))}", f"More than 2: ${sum(1 for x in xs if x > 2)}$ students") for n, xs in [(len(x), x) for x in [raw_list(s, 14, 0, 5) for s in [151, 152, 153, 154, 155, 156]]]])

# ---------- MEDIUM ----------
mA1 = []
for sd in [201, 202, 203, 204, 205]:
    d = D(sd, FRUITS, 10, 80, 5, 3); v = sorted(x[1] for x in d)
    mA1.append(nw("The total of the two largest values in the table is:<br>" + tbl(d), v[-1] + v[-2], [v[-1] + v[-3], v[-1] + v[0], v[-1] - v[-2], v[-1] + v[-2] + 5], "Add the two biggest numbers."))
mA2 = [nw(f"A pictograph has one symbol = {k}. The number of symbols for A is {a} and for B is {b}. How many more does A have than B?", (a - b) * k, [(a + b) * k, a - b, (a - b) * k + k, (a - b) * k - k], "Find the difference in symbols then multiply.") for k, a, b in [(15, 9, 4), (25, 8, 3), (12, 10, 6), (30, 7, 2), (8, 11, 5)]]
mA3 = [nw(f"A bar of height {h} cm in a graph with scale 1 cm = {k} units, and another bar of {h2} cm. Together they show:", (h + h2) * k, [h + h2 + k, (h + h2) * k + k, (h + h2) * k - k, h * k], "Total height times scale.") for k, h, h2 in [(15, 6, 5), (25, 4, 7), (12, 8, 3), (40, 5, 6)]]
mA4 = []
for sd in [211, 212, 213, 214]:
    d = D(sd, SPORTS, 10, 70, 5, 4); tot = sum(x[1] for x in d); a = d[0][1]
    mA4.append(tm(f"What fraction of the total do {d[0][0]} players form?<br>" + tbl(d, ("Sport", "Students")), "$" + fx(Fr(a, tot)) + "$", ["$" + fx(Fr(tot - a, tot)) + "$", "$" + fx(Fr(a, tot - a)) + "$", "$" + fx(Fr(a, tot + 5)) + "$"], f"Fraction $=\\frac{{{a}}}{{{tot}}}$ (simplified)"))
mA5 = [nw(f"In a pictograph one symbol = {k}. Monday shows {a} symbols, Tuesday {b} symbols and Wednesday {c} symbols. The total number shown for the three days is:", (a + b + c) * k, [a + b + c, (a + b + c) * k + k, (a + b + c - 1) * k, (a + b + c) + k], "Add the symbols, then multiply by the value of one symbol.") for k, a, b, c in [(5, 4, 6, 3), (12, 3, 5, 4), (25, 2, 4, 3), (8, 6, 3, 5)]]
mA6 = [nw(f"In the data {lst(xs)}, the value {v} occurs how many times?", xs.count(v), [xs.count(v) + 1, xs.count(v) - 1, xs.count(v) + 2, xs.count(v) + 3], "Count.") for xs, v in [(raw_list(s, 15, 1, 6), (s % 6) + 1) for s in [221, 222, 223, 224]]]
mA7 = [nw(f"On a bar graph with scale 1 cm = {k} units a bar is {h} cm. If its value increases by {p} units, the new height (cm) is:", h + p // k, [h + p, h + p // k + 1, h + p // k - 1], "Convert the increase into cm.") for k, h, p in [(5, 6, 20), (10, 4, 50), (20, 5, 80), (4, 7, 12)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([QQ("Find the difference between the highest and lowest and the total of all.<br>" + tbl(d), f"Highest {top(d)[1]}, lowest {bot(d)[1]}", f"Difference $={top(d)[1]-bot(d)[1]}$", f"Total $={sum(x[1] for x in d)}$") for d in [D(s, FRUITS, 10, 80, 5, 3) for s in [231, 232, 233, 234]]]
          + [QQ(f"In a pictograph, one symbol = {k} students. {a} symbols show Class VI-A. Class VI-B has {b} students more. How many symbols show VI-B?", f"VI-A $={a*k}$ students", f"VI-B $={a*k+b}$ students", f"Symbols $={(a*k+b)//k}$") for k, a, b in [(10, 5, 20), (5, 8, 15), (20, 3, 40), (15, 4, 30)]]
          + [QQ(f"Prepare a frequency table for the data {lst(xs)} and say which value is repeated the most.", "Count each value", "; ".join(f"{v}: {xs.count(v)}" for v in sorted(set(xs))), f"Most repeated: {max(set(xs), key=lambda v: (xs.count(v), -v))}") for xs in [raw_list(s, 14, 1, 6) for s in [241, 242, 243, 244]]])
MED_C = ([QQ("Find the fraction of students liking " + d[0][0] + " and the number who do not like it.<br>" + tbl(d, ("Sport", "Students")), f"Total $={sum(x[1] for x in d)}$", f"Fraction $=\\frac{{{d[0][1]}}}{{{sum(x[1] for x in d)}}}=" + fx(Fr(d[0][1], sum(x[1] for x in d))) + "$", f"Others $={sum(x[1] for x in d)-d[0][1]}$") for d in [D(s, SPORTS, 10, 70, 5, 3) for s in [251, 252, 253, 254, 255, 256]]]
          + [QQ(f"A shop sold {a}, {b}, {c} and {d} kg of rice in four weeks. Find the total. For a bar graph with the scale 1 cm = {k} kg, find the height of each bar.", f"Total $={a+b+c+d}$ kg", f"Heights: {a//k}, {b//k}, {c//k}, {d//k} cm", f"Tallest bar: {max(a,b,c,d)//k} cm (week {[a,b,c,d].index(max(a,b,c,d))+1})") for a, b, c, d, k in [(40, 60, 80, 100, 20), (25, 50, 75, 100, 25), (30, 45, 60, 75, 15), (12, 24, 36, 48, 12), (50, 70, 90, 110, 10), (16, 32, 40, 64, 8)]]
          + [QQ(f"In a class of {n} students the data of the number of books read in a month is {lst(xs)}. How many read more than {m}, and how many read exactly {m}?", f"Count more than {m}: ${sum(1 for x in xs if x > m)}$", f"Count exactly {m}: ${xs.count(m)}$", "Use tally marks to count carefully") for n, xs, m in [(len(x), x, 2 + i % 2) for i, x in enumerate(raw_list(s, 15, 0, 5) for s in [261, 262, 263, 264, 265, 266])]])
MED_D = ([QQ(f"A pictograph (one symbol = {k}) shows {a} symbols on Monday, {b} on Tuesday and {c} on Wednesday. On Thursday the number of items sold equals the total of Monday and Tuesday. Find the number sold on each day, and the total for the four days.", f"Mon $={a*k}$, Tue $={b*k}$, Wed $={c*k}$", f"Thursday $={a*k}+{b*k}={(a+b)*k}$", f"Total for four days $={a*k}+{b*k}+{c*k}+{(a+b)*k}$", f"$={(2*a+2*b+c)*k}$", f"Symbols needed for Thursday: ${a+b}$") for k, a, b, c in [(12, 3, 6, 9), (15, 4, 5, 6), (6, 8, 7, 9), (9, 2, 4, 6), (30, 6, 3, 9), (18, 5, 7, 6)]]
          + [QQ("A school survey data is given. Find the total, the sport with maximum students, and the fraction who play it. Then choose a scale for a bar graph and give the height of the biggest bar. Data: " + ", ".join(f"{x[0]} {x[1]}" for x in d) + ".", f"Total $={sum(x[1] for x in d)}$", f"Maximum: {top(d)[0]} with {top(d)[1]}", f"Fraction $=\\frac{{{top(d)[1]}}}{{{sum(x[1] for x in d)}}}=" + fx(Fr(top(d)[1], sum(x[1] for x in d))) + "$", f"Scale 1 cm = 10 students: height $={top(d)[1]//10}$ cm" if top(d)[1] % 10 == 0 else f"Scale 1 cm = 5 students: height $={top(d)[1]//5}$ cm") for d in [D(s, SPORTS, 10, 80, 5, 3) for s in [271, 272, 273, 274, 275, 276]]])

# ---------- HARD ----------
hA1 = []
for sd in [301, 302, 303, 304]:
    d = D(sd, FRUITS, 10, 90, 5, 5); tot = sum(x[1] for x in d)
    hA1.append(nw("The total of the table, after removing the largest value, is:<br>" + tbl(d), tot - top(d)[1], [tot - bot(d)[1], tot, tot - top(d)[1] + 5, tot - top(d)[1] - 5], "Total minus the largest."))
hA2 = [nw(f"One symbol of a pictograph stands for {k}. Class A has {a} symbols and its total is 3 times Class B. How many symbols does Class B have?", a // 3, [a * 3, a - 3, a // 3 + 1, a // 3 - 1], "Divide by 3 (the symbols are in the same proportion).") for k, a in [(10, 12), (20, 15), (5, 18), (25, 9)]]
hA3 = [nw(f"A bar graph has scale 1 cm = {k} units. The heights of two bars differ by {d} cm. The values differ by:", k * d, [k + d, k * d + k, k * d - k], "Multiply.") for k, d in [(12, 7), (15, 6), (8, 9), (30, 4)]]
hA4 = [nw(f"A school bus carries {a} children on trip 1, {b} on trip 2 and {c} on trip 3. A pictograph uses one symbol for {k} children. The number of symbols needed for all three trips is:", (a + b + c) // k, [(a + b + c) // k + 1, (a + b + c) // k - 1, a // k + b // k + c // k + 2], "Add the children, then divide by the value of one symbol.") for a, b, c, k in [(30, 45, 60, 15), (40, 55, 35, 5), (24, 36, 48, 12), (50, 70, 80, 10)]]
hA5 = [nw(f"Out of {n} students, {a} play cricket and {b} play football, none plays both. How many play neither?", n - a - b, [n - a, n - b, n - a - b + 10, a + b], "Subtract.") for n, a, b in [(120, 45, 38), (200, 85, 64), (150, 52, 47), (90, 33, 28)]]
hA6 = [nw(f"A bar graph shows sales of ₹{a*k}, ₹{b*k}, ₹{c*k}. If the scale is 1 cm = ₹{k}, the total height of all three bars is (cm):", a + b + c, [a + b + c + 2, (a + b + c) * k, a + b + c - 2], "Add the heights.") for k, a, b, c in [(500, 4, 7, 5), (200, 9, 6, 8), (50, 12, 15, 10), (1000, 3, 5, 6)]]
hA7 = [nw(f"A pictograph has symbols worth {k} each. To show {n}, how many FULL symbols are needed (plus one part-symbol)?", n // k, [n // k + 1, n // k - 1, n // k + 2], "Integer division.") for k, n in [(12, 100), (15, 140), (25, 190), (30, 250)]]
hA8 = [nw(f"In a bar graph with scale 1 cm = {k} units, the value {n} is shown by a bar of height (cm):", Dc(n) / k, [Dc(n) // k, Dc(n) // k + 1, n - k, n * k], "Divide by the scale.") for k, n in [(8, 60), (12, 90), (20, 130), (6, 45)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"In a survey of {n} people, {a} like tea, {b} like coffee, and the rest like milk. Find the number liking milk and show data in a table.", f"Milk $={n}-{a}-{b}$", f"${n-a-b}$ people") for n, a, b in [(150, 62, 48), (200, 85, 77), (180, 70, 66), (250, 110, 95)]]
          + [QQ(f"A bar graph uses 1 cm = {k} units and a bar is {h} cm. Another bar is {s} cm shorter. Find the value of the shorter bar.", f"First bar $={h*k}$", f"Second bar height $={h-s}$ cm", f"Value $={(h-s)*k}$") for k, h, s in [(20, 9, 3), (15, 8, 2), (25, 10, 4), (12, 7, 3)]]
          + [QQ(f"The data shows the number of goals in {len(xs)} matches: {lst(xs)}. Find the total number of goals and in how many matches more than 2 goals were scored.", f"Total $={'+'.join(map(str, xs))}={sum(xs)}$", f"Matches with more than 2 goals: ${sum(1 for x in xs if x > 2)}$") for xs in [(2, 3, 1, 4, 0, 5), (3, 2, 4, 5, 6, 2), (1, 0, 2, 3, 4, 2), (5, 4, 6, 3, 2, 4)]])
HARD_C = ([QQ("The table shows two weeks of sales (units). Find the week with the larger total and by how much.<br>" + table(["Day", "Week 1", "Week 2"], [[dn, a, b] for dn, a, b in rows]), f"Week 1 total $={sum(r[1] for r in rows)}$", f"Week 2 total $={sum(r[2] for r in rows)}$", f"Larger: {'Week 1' if sum(r[1] for r in rows) > sum(r[2] for r in rows) else 'Week 2'}", f"Difference $={abs(sum(r[1] for r in rows)-sum(r[2] for r in rows))}$") for rows in [[("Mon", 12 + s, 15), ("Tue", 20, 18 + s), ("Wed", 9 + 2 * s, 14), ("Thu", 17, 11 + s)] for s in [1, 2, 3, 4, 5, 6]]]
           + [QQ(f"In a pictograph one symbol = {k}. A shop sold {a} symbols of pens, and the number of notebooks is {m} times the pens. Find the notebooks sold and total items sold.", f"Pens $={a*k}$", f"Notebooks $={a*k*m}$", f"Total $={a*k*(m+1)}$") for k, a, m in [(12, 3, 2), (15, 4, 3), (8, 5, 2), (20, 2, 4), (6, 7, 3), (25, 3, 2)]]
           + [QQ(f"For the data {lst(xs)} prepare a frequency table and find how many values are greater than {m}.", "Frequencies: " + "; ".join(f"{v}: {xs.count(v)}" for v in sorted(set(xs))), f"Values greater than {m}: " + " + ".join(f"{xs.count(v)}" for v in sorted(set(xs)) if v > m) + f" $={sum(1 for x in xs if x > m)}$") for xs, m in [(raw_list(s, 12, 1, 8), 3 + s % 3) for s in [311, 312, 313, 314, 315, 316]]])
HARD_D = ([QQ(f"A bar graph has scale 1 cm = {k} units. Bars A, B, C have heights {a} cm, {b} cm, {c} cm. The value of D equals A + B - C. Find the values of A, B, C and D, and the height of bar D.", f"A $={a*k}$, B $={b*k}$, C $={c*k}$", f"D $={a*k}+{b*k}-{c*k}$", f"D $={(a+b-c)*k}$", f"Height of D $={a+b-c}$ cm") for k, a, b, c in [(12, 3, 6, 9), (15, 6, 4, 8), (20, 3, 9, 6), (9, 4, 8, 6), (30, 2, 5, 8), (18, 5, 7, 9)]]
          + [QQ(f"{n} students were asked their favourite colour: {', '.join(f'{nm_} {v}' for nm_, v in zip(['red','blue','green','yellow'], vs))} and the rest chose pink. Find the number liking pink, the fraction liking blue, and draw the pictograph with one symbol = 5 (give symbol counts).", f"Pink $={n}-{sum(vs)}={n-sum(vs)}$", f"Blue fraction $=\\frac{{{vs[1]}}}{{{n}}}=" + fx(Fr(vs[1], n)) + "$", "Symbols: " + ", ".join(f"{c}: {v//5}" for c, v in zip(['red', 'blue', 'green', 'yellow', 'pink'], vs + (n - sum(vs),)))) for n, vs in [(100, (20, 25, 15, 10)), (80, (15, 20, 10, 5)), (120, (30, 25, 20, 15)), (90, (20, 15, 25, 10)), (150, (35, 30, 25, 20)), (60, (10, 15, 5, 10))]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
