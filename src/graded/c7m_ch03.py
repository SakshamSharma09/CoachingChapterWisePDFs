"""Class 7 Maths Ch 3 - A Peek Beyond the Point (decimals: place value, comparing, rounding, operations, unit conversion, word problems)."""
from g67 import *

SLUG, NAME, CHNO = "Peek_Beyond_the_Point", "A Peek Beyond the Point", 3

def D(x): return Dc(str(x))
def t(x): return f"${fmt(D(x))}$"
def places(x): return max(0, -D(x).as_tuple().exponent)
def whole(x): return int(D(x).scaleb(places(x)))
def rd(x, n): return str(D(x).quantize(Dc(1).scaleb(-n), rounding="ROUND_HALF_UP"))
def ftex(x): f = Fr(D(x)); return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

def dm(q, c, why="", kind="near"):
    """Numeric MCQ. kind: 'near' (small slips), 'shift' (decimal point misplaced), 'int' (whole-number answer)."""
    c = D(c)
    if kind == "shift": cand = [c * 10, c / 10, c * 100, c / 100, c * 1000, c / 1000]
    elif kind == "int": cand = [c + 1, c - 1, c + 2, c - 2, c + 10, c * 10]
    else: cand = [c + D(o) for o in ("0.1", "-0.1", "1", "-1", "0.01", "-0.01", "10")]
    wrong = []
    for x in cand:
        if x != c and x >= 0 and x not in wrong: wrong.append(x)
    return M4(q, fmt(c), [fmt(x) for x in wrong[:6]], why)

def greatest(q, sets, why):
    return [tm(q, max(s, key=D), [x for x in s if x != max(s, key=D)], why) for s in sets]

def dec_frac(a_list, why):
    out = []
    for a in a_list:
        f = Fr(D(a)); n, d = f.numerator, f.denominator
        out.append(tm(f"${a}$ written as a fraction in simplest form is:", f"$\\frac{{{n}}}{{{d}}}$",
                      [f"$\\frac{{{d}}}{{{n}}}$", f"$\\frac{{{n + 1}}}{{{d}}}$", f"$\\frac{{{n}}}{{{2 * d}}}$"], why))
    return out

def conv(q_fmt, items, factor, why):
    return [dm(q_fmt.format(a=a), D(a) * factor, why, "shift") for a in items]

# ---------------------------------------------------------------- EASY
def digit_value(s, d):
    assert s.count(d) == 1
    dot = s.index("."); pos = s.index(d)
    return D(d) * Dc(10) ** (dot - pos - 1 if pos < dot else dot - pos)

eA1 = [dm(f"In ${s}$, the digit ${d}$ has the value:", digit_value(s, d), "Find the place of the digit: tenths, hundredths or thousandths.", "shift")
       for s, d in [("12.368", "6"), ("4.795", "9"), ("30.527", "2"), ("8.043", "4"), ("0.619", "1")]]
eA2 = [dm(f"${a}+{b}=$", D(a) + D(b), "Line up the decimal points and add.") for a, b in [("3.4", "2.7"), ("5.25", "1.6"), ("12.5", "7.38"), ("0.85", "0.6"), ("9.07", "4.93")]]
eA3 = [dm(f"${a}-{b}=$", D(a) - D(b), "Line up the decimal points and subtract.") for a, b in [("8.5", "3.2"), ("10.4", "6.75"), ("7.06", "2.9"), ("15", "8.45"), ("6.3", "0.48")]]
eA4 = [dm(f"${a}\\times{m}=$", D(a) * m, f"Multiplying by {m} moves the decimal point {len(str(m)) - 1} place(s) to the right.", "shift") for a, m in [("4.52", 10), ("0.37", 100), ("6.8", 1000), ("12.04", 10), ("0.095", 100)]]
eA5 = [dm(f"${a}\\div{m}=$", D(a) / m, f"Dividing by {m} moves the decimal point {len(str(m)) - 1} place(s) to the left.", "shift") for a, m in [("45.6", 10), ("7.5", 100), ("382", 1000), ("0.9", 10), ("260", 100)]]
eA6 = greatest("Which of these is the greatest?", [("0.7", "0.69", "0.07", "0.699"), ("3.08", "3.8", "3.088", "3.008"), ("12.45", "12.5", "12.405", "12.054"), ("0.305", "0.35", "0.3", "0.053"), ("5.09", "5.1", "5.009", "5.01")], "Compare the whole parts, then tenths, then hundredths.")
eA7 = dec_frac(["0.5", "0.25", "0.75", "0.4"], "Write over 10, 100 or 1000 and reduce.")
eA8 = [tm(f"$\\frac{{{n}}}{{{d}}}$ written as a decimal is:", fmt(Dc(n) / Dc(d)), [fmt(Dc(n) / Dc(d) * 10), fmt(Dc(n) / Dc(d) / 10), fmt(Dc(n) / Dc(d) * 100)], "The denominator tells the place: 10 tenths, 100 hundredths, 1000 thousandths.")
       for n, d in [(7, 10), (3, 100), (9, 1000), (47, 100), (123, 1000)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]

def expanded(a):
    s = str(a); dot = s.index("."); parts = []
    for i, ch in enumerate(s):
        if ch in ".0": continue
        parts.append(fmt(D(ch) * Dc(10) ** (dot - i - 1 if i < dot else dot - i)))
    return " + ".join(parts)
EASY_B = ([QQ(f"Find ${a}+{b}$.", "Write the numbers with the decimal points one below the other", f"Sum $={fmt(D(a) + D(b))}$") for a, b in [("12.35", "4.8"), ("7.09", "3.95"), ("0.64", "9.7"), ("25.5", "14.75")]]
          + [QQ(f"Find ${a}-{b}$.", "Write the numbers with the decimal points one below the other", f"Difference $={fmt(D(a) - D(b))}$") for a, b in [("20.5", "8.75"), ("9.04", "3.6"), ("15", "7.25"), ("6.2", "5.84")]]
          + [QQ(f"Write ${a}$ in expanded form (as a sum of place values).", "Split the number by place value", f"${a}={expanded(a)}$") for a in ("34.56", "8.205", "120.4", "0.739")])
EASY_C = ([QQ(f"Write ${a}$ as a fraction in simplest form.", f"${a}=\\frac{{{whole(a)}}}{{{10 ** places(a)}}}$", "Divide numerator and denominator by their common factor", f"Simplest form: ${ftex(a)}$") for a in ("0.6", "0.35", "0.125", "0.04", "0.45", "0.8")]
          + [QQ(f"Arrange in ascending order: ${', '.join(v)}$.", "Compare whole parts, then tenths, then hundredths", "Ascending order: $" + ", ".join(fmt(D(x)) for x in sorted(v, key=D)) + "$") for v in [("0.5", "0.45", "0.505", "0.055"), ("3.2", "3.02", "3.22", "3.202"), ("1.09", "1.9", "1.099", "1.19"), ("0.8", "0.08", "0.88", "0.808"), ("2.5", "2.05", "2.55", "2.505"), ("4.1", "4.01", "4.11", "4.101")]]
          + [QQ(f"Round ${a}$ (i) to one decimal place and (ii) to the nearest whole number.", "Look at the digit just after the place being rounded", f"(i) ${rd(a, 1)}$", f"(ii) ${rd(a, 0)}$") for a in ("6.347", "12.968", "0.452", "25.555", "3.049", "9.951")])
EASY_D = ([QQ(f"A ribbon is ${a}$ m long and a piece of ${b}$ m is cut off. Find the length left in metres and in centimetres.", f"Left $={a}-{b}={fmt(D(a) - D(b))}$ m", f"In centimetres: ${fmt((D(a) - D(b)) * 100)}$ cm") for a, b in [("5.75", "2.4"), ("8.5", "3.65"), ("12.2", "7.85"), ("6.04", "2.5"), ("10.25", "4.75"), ("9.9", "6.45")]]
          + [QQ(f"A packet of sugar weighs ${a}$ kg. Find the weight of ${n}$ such packets in kilograms and in grams.", f"${a}\\times{n}={fmt(D(a) * n)}$ kg", f"In grams: ${fmt(D(a) * n * 1000)}$ g") for a, n in [("1.25", 6), ("0.75", 8), ("2.4", 5), ("1.5", 12), ("0.35", 10), ("3.2", 4)]])

# ---------------------------------------------------------------- NCERT
nA1 = [dm(f"${a}\\times{b}=$", D(a) * D(b), "Multiply as whole numbers, then count the decimal places in both factors.", "shift") for a, b in [("2.5", "0.4"), ("1.2", "3.5"), ("0.6", "0.07"), ("4.25", "2"), ("0.15", "0.3")]]
nA2 = [dm(f"${a}\\div{b}=$", D(a) / D(b), "Multiply both numbers by 10 or 100 so that the divisor becomes a whole number.", "shift") for a, b in [("4.8", "0.6"), ("7.5", "2.5"), ("0.36", "0.9"), ("9.6", "1.2"), ("12.6", "0.7")]]
nA3 = conv("${a}$ m expressed in cm is:", ["3.45", "0.8", "12.06", "0.075"], 100, "1 m = 100 cm.")
nA4 = conv("${a}$ kg expressed in grams is:", ["2.5", "0.375", "4.08", "0.06"], 1000, "1 kg = 1000 g.")
nA5 = conv("₹${a}$ expressed in paise is:", ["7.25", "0.85", "12.5", "3.05"], 100, "₹1 = 100 paise.")
nA6 = [dm(f"${a}$ rounded to the nearest tenth is:", rd(a, 1), "Look at the hundredths digit.") for a in ("4.37", "8.65", "0.449", "12.95", "5.04")]
nA7 = [dm(f"${c}-({a}+{b})=$", D(c) - D(a) - D(b), "Work out the bracket first.") for a, b, c in [("2.5", "3.75", "10"), ("1.25", "4.5", "9"), ("0.8", "2.35", "6"), ("5.6", "3.15", "12")]]
nA8 = [dm(f"$\\frac{{{n}}}{{{d}}}$ as a decimal is:", Dc(n) / Dc(d), "Divide the numerator by the denominator.") for n, d in [(3, 8), (7, 20), (9, 25), (11, 4)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([QQ(f"Find ${a}\\times{b}$.", f"Multiply without the decimal points: ${whole(a)}\\times{whole(b)}={whole(a) * whole(b)}$", f"Decimal places in the factors: ${places(a)}+{places(b)}={places(a) + places(b)}$, so the product is ${fmt(D(a) * D(b))}$") for a, b in [("3.2", "0.5"), ("0.45", "0.6"), ("2.5", "1.4"), ("0.08", "3.5")]]
           + [QQ(f"Find ${a}\\div{b}$.", f"Make the divisor a whole number: ${fmt(D(a) * 10)}\\div{fmt(D(b) * 10)}$", f"Answer: ${fmt(D(a) / D(b))}$") for a, b in [("3.6", "0.4"), ("8.4", "0.7"), ("0.96", "0.8"), ("15.5", "2.5")]]
           + [QQ(f"Convert (i) ${a}$ m to cm and (ii) ${b}$ kg to g.", f"(i) ${a}\\times100={fmt(D(a) * 100)}$ cm", f"(ii) ${b}\\times1000={fmt(D(b) * 1000)}$ g") for a, b in [("3.62", "2.45"), ("0.85", "0.075"), ("12.4", "5.06"), ("7.05", "0.9")]])
def fdec(n, d, cmp):
    v = Dc(n) / Dc(d)
    return QQ(f"Express $\\frac{{{n}}}{{{d}}}$ as a decimal and say whether it is greater than or less than ${cmp}$.", f"Divide: ${n}\\div{d}={fmt(v)}$", f"Compare ${fmt(v)}$ with ${cmp}$", f"$\\frac{{{n}}}{{{d}}}$ is {'greater' if v > D(cmp) else 'less'} than ${cmp}$")
NCERT_C = ([QQ(f"Cloth costs ₹${p}$ per metre. Find the cost of ${a}$ m of cloth.", f"Cost $={p}\\times{a}$", f"Cost $=$ ₹${fmt(D(p) * D(a))}$") for p, a in [("125.5", "3.5"), ("86.4", "2.5"), ("240", "1.75"), ("95.5", "4.2"), ("150.25", "2"), ("72.8", "3.5")]]
           + [fdec(n, d, c) for n, d, c in [(3, 8, "0.4"), (7, 20, "0.3"), (9, 25, "0.35"), (5, 8, "0.6"), (13, 20, "0.65"), (3, 16, "0.2")]]
           + [QQ(f"A rod ${a}$ m long is cut into pieces of ${b}$ m each. How many pieces are made?", f"Number of pieces $={a}\\div{b}$", f"$={fmt(D(a) / D(b))}$ pieces", f"Check: ${fmt(D(a) / D(b))}\\times{b}={a}$") for a, b in [("7.5", "0.25"), ("4.8", "0.6"), ("9", "0.75"), ("3.6", "0.3"), ("12.5", "2.5"), ("2.4", "0.08")]])
def shop(a, p, b, q, pay):
    r, w = D(a) * D(p), D(b) * D(q)
    return QQ(f"A shopkeeper buys ${a}$ kg of rice at ₹${p}$ per kg and ${b}$ kg of wheat at ₹${q}$ per kg. Find the total cost. He pays ₹${pay}$; find the balance.", f"Rice $={a}\\times{p}={fmt(r)}$", f"Wheat $={b}\\times{q}={fmt(w)}$", f"Total $={fmt(r + w)}$", f"Balance $={pay}-{fmt(r + w)}={fmt(D(pay) - r - w)}$")
def laps(a, b, c, goal):
    s = D(a) + D(b) + D(c); lo, hi = min(D(a), D(b), D(c)), max(D(a), D(b), D(c))
    return QQ(f"A runner covers ${a}$ km, ${b}$ km and ${c}$ km in three laps. Find the total distance, how much farther the longest lap is than the shortest, and how much more she must run to complete ${goal}$ km.", f"Total $={fmt(s)}$ km", f"Longest $={fmt(hi)}$ km, shortest $={fmt(lo)}$ km", f"Difference $={fmt(hi - lo)}$ km", f"Remaining $={goal}-{fmt(s)}={fmt(D(goal) - s)}$ km")
NCERT_D = ([shop(*x) for x in [("2.5", "48", "1.5", "36", "200"), ("3.5", "52", "2", "40", "300"), ("1.75", "60", "2.5", "32", "250"), ("4", "45.5", "3.5", "28", "400"), ("2.25", "64", "1.5", "38", "250"), ("5.5", "42", "2.5", "30", "400")]]
           + [laps(*x) for x in [("2.5", "3.25", "2.75", "10"), ("1.8", "2.45", "3.1", "10"), ("4.2", "3.75", "2.95", "12"), ("5.5", "4.8", "6.25", "20"), ("3.05", "2.9", "3.55", "10"), ("6.4", "5.75", "4.6", "20")]])

# ---------------------------------------------------------------- MEDIUM
mA1 = [dm(f"${a}\\times{b}=$", D(a) * D(b), "Count the total number of decimal places.", "shift") for a, b in [("12.5", "0.08"), ("0.75", "1.6"), ("3.05", "0.4"), ("2.4", "0.35"), ("0.125", "6")]]
mA2 = [dm(f"${a}\\div{b}=$", D(a) / D(b), "Shift the decimal points of both numbers equally.", "shift") for a, b in [("1.44", "1.2"), ("0.495", "0.9"), ("7.28", "0.8"), ("33.6", "0.07"), ("0.0756", "0.12")]]
mA3 = [dm(f"The value of ${a}\\times{b}+{c}$ is:", D(a) * D(b) + D(c), "Multiply first, then add.") for a, b, c in [("2.5", "4", "1.75"), ("0.6", "0.5", "2.2"), ("3.2", "1.5", "0.64"), ("1.25", "0.8", "4.5")]]
mA4 = [dm(f"${a}$ litres of milk is shared equally among ${n}$ persons. Each person gets (in litres):", D(a) / n, "Divide the total by the number of persons.") for a, n in [("7.5", 6), ("4.8", 8), ("9.6", 12), ("3.6", 5)]]
mA5 = [dm(f"The value of ${c}-{a}\\times{b}$ is:", D(c) - D(a) * D(b), "Multiply first, then subtract.") for a, b, c in [("2.5", "3.2", "20"), ("1.5", "0.6", "5"), ("0.4", "7.5", "10"), ("1.2", "2.5", "9")]]
def mixed(big, u1, small, u2, f): return dm(f"${big}$ {u1} ${small}$ {u2} expressed in {u1} is:", D(big) + D(small) / f, f"1 {u1} = {f} {u2}, so write the smaller unit as a decimal part.")
mA6 = [mixed(3, "m", 45, "cm", 100), mixed(2, "kg", 50, "g", 1000), mixed(7, "km", 80, "m", 1000), mixed(4, "L", 250, "mL", 1000)]
mA7 = [dm(f"${a}$ rounded to two decimal places is:", rd(a, 2), "Look at the thousandths digit.") for a in ("3.456", "7.894", "0.0649", "12.0051")]
def between(lo, hi, c, w): return tm(f"Which number lies between ${lo}$ and ${hi}$?", c, w, "A number between them is greater than the smaller and less than the larger.")
mA8 = [between("0.3", "0.4", "0.37", ["0.3", "0.04", "0.43"]), between("1.2", "1.3", "1.25", ["1.3", "1.02", "1.35"]),
       between("0.05", "0.06", "0.055", ["0.06", "0.5", "0.065"]), between("2.7", "2.8", "2.75", ["2.8", "2.07", "2.85"])]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Simplify ${a}+{b}-{c}$.", f"${a}+{b}={fmt(D(a) + D(b))}$", f"${fmt(D(a) + D(b))}-{c}={fmt(D(a) + D(b) - D(c))}$") for a, b, c in [("5.6", "3.45", "2.8"), ("12.05", "7.9", "6.35"), ("0.75", "8.4", "4.6"), ("15", "2.85", "9.7")]]
         + [QQ(f"Find $({a}\\times{b})\\div{c}$.", f"${a}\\times{b}={fmt(D(a) * D(b))}$", f"${fmt(D(a) * D(b))}\\div{c}={fmt(D(a) * D(b) / D(c))}$") for a, b, c in [("1.2", "0.5", "0.04"), ("2.4", "1.5", "0.9"), ("0.6", "0.7", "0.12"), ("3.5", "0.8", "1.4")]]
         + [QQ(f"Round ${a}$ (i) to the nearest tenth and (ii) to the nearest hundredth.", "Look at the digit after the place being rounded", f"(i) ${rd(a, 1)}$", f"(ii) ${rd(a, 2)}$") for a in ("8.746", "0.0853", "15.995", "2.3049")])
def car(a, b, k): return QQ(f"A car runs ${a}$ km on 1 litre of petrol. How far does it run on ${b}$ litres? How many litres are needed for ${fmt(D(a) * k)}$ km?", f"Distance $={a}\\times{b}={fmt(D(a) * D(b))}$ km", f"Litres $={fmt(D(a) * k)}\\div{a}={k}$")
def pens(a, n, pay): return QQ(f"A pen costs ₹${a}$. Riya buys ${n}$ pens and pays ₹${pay}$. Find the cost of the pens and the balance she gets back.", f"Cost $={n}\\times{a}={fmt(D(a) * n)}$", f"Balance $={pay}-{fmt(D(a) * n)}={fmt(D(pay) - D(a) * n)}$")
def desc(v):
    s = sorted(v, key=D, reverse=True)
    return QQ(f"Arrange ${', '.join(v)}$ in descending order and find the difference between the greatest and the smallest.", "Compare whole parts, then tenths, then hundredths", "Descending order: $" + ", ".join(fmt(D(x)) for x in s) + "$", f"Difference $={fmt(D(s[0]))}-{fmt(D(s[-1]))}={fmt(D(s[0]) - D(s[-1]))}$")
MED_C = ([car(*x) for x in [("12.5", "8", 6), ("15.5", "6", 4), ("9.5", "12", 8), ("18.5", "5", 7), ("11.25", "4", 9), ("14.4", "7", 5)]]
         + [pens(*x) for x in [("7.5", 8, 100), ("12.25", 6, 100), ("4.75", 12, 100), ("8.4", 5, 50), ("15.5", 4, 100), ("6.25", 10, 100)]]
         + [desc(v) for v in [("4.05", "4.5", "4.005", "4.55"), ("0.9", "0.09", "0.099", "0.19"), ("7.2", "7.02", "7.22", "7.202"), ("1.3", "1.03", "1.033", "1.31"), ("0.62", "0.6", "0.062", "0.26"), ("9.8", "9.08", "9.88", "9.808")]])
def pieces(L, p):
    n = int(D(L) // D(p)); left = D(L) - n * D(p)
    return QQ(f"A wire ${L}$ m long is cut into pieces of ${p}$ m each. How many whole pieces are made and what length is left over?", f"${L}\\div{p}$ gives ${n}$ whole pieces", f"Length used $={n}\\times{p}={fmt(n * D(p))}$ m", f"Left over $={L}-{fmt(n * D(p))}={fmt(left)}$ m")
def tap(T, p, mins):
    return QQ(f"A tank of capacity ${T}$ litres is filled by a tap at ${p}$ litres per minute. How many minutes does it take to fill the empty tank? How much water is in it after ${mins}$ minutes and how much more is needed?", f"Time $={T}\\div{p}={fmt(D(T) / D(p))}$ minutes", f"After ${mins}$ minutes: ${p}\\times{mins}={fmt(D(p) * D(mins))}$ litres", f"More needed $={T}-{fmt(D(p) * D(mins))}={fmt(D(T) - D(p) * D(mins))}$ litres")
MED_D = [pieces(*x) for x in [("9.5", "1.2"), ("7.8", "0.9"), ("12.4", "1.5"), ("6.5", "0.8"), ("10.2", "2.5"), ("5.3", "0.7")]] + \
        [tap(*x) for x in [("90", "7.5", "6"), ("72", "4.8", "9"), ("45", "2.5", "8"), ("63", "4.2", "5"), ("84", "3.5", "12"), ("56", "3.5", "10")]]

# ---------------------------------------------------------------- HARD
hA1 = [dm(f"${a}\\times{b}\\times{c}=$", D(a) * D(b) * D(c), "Multiply two at a time and count the decimal places carefully.", "shift") for a, b, c in [("0.2", "0.3", "0.4"), ("1.5", "0.2", "0.6"), ("0.5", "0.5", "0.8"), ("2.5", "0.04", "3")]]
hA2 = [dm(f"How many times does ${a}$ go into ${b}$?", D(b) / D(a), "Divide the larger number by the smaller.", "int") for a, b in [("0.05", "2.4"), ("0.25", "6"), ("0.04", "1.2"), ("0.15", "4.5")]]
hA3 = [dm(f"${k}$ of a number is ${v}$. The number is:", D(v) / D(k), "Divide the part by the fraction it represents.", "int") for k, v in [("0.6", "4.2"), ("0.4", "3.2"), ("0.25", "3.5"), ("0.05", "0.45")]]
hA4 = [dm(f"$({a}+{b})\\times{c}=$", (D(a) + D(b)) * D(c), "Work out the bracket first.") for a, b, c in [("2.5", "1.75", "0.4"), ("0.35", "0.65", "2.5"), ("3.2", "0.8", "1.5"), ("1.06", "0.94", "0.35")]]
def closest(s):
    d = sorted(abs(D(x) - 1) for x in s); assert d[0] != d[1]
    c = min(s, key=lambda x: abs(D(x) - 1))
    return tm("Which of these is closest to $1$?", c, [x for x in s if x != c], "Find how far each number is from 1.")
hA5 = [closest(s) for s in [("0.95", "1.08", "0.89", "1.2"), ("1.04", "0.93", "1.1", "0.8"), ("1.02", "0.97", "1.05", "0.9"), ("0.996", "1.01", "0.98", "1.1")]]
hA6 = [dm(f"What must be added to ${a}$ to get ${b}$?", D(b) - D(a), "Subtract the smaller number from the larger.") for a, b in [("2.35", "5"), ("0.875", "2"), ("7.6", "10"), ("3.045", "4")]]
def eqfrac(dec, w):
    for x in w: assert Fr(x) != Fr(D(dec))
    return tm(f"Which fraction is equal to ${dec}$?", f"$\\frac{{{Fr(D(dec)).numerator}}}{{{Fr(D(dec)).denominator}}}$", [f"$\\frac{{{x.numerator}}}{{{x.denominator}}}$" for x in map(Fr, w)], "Write over 1000, 100 or 10 and reduce.")
hA7 = [eqfrac("0.125", ["1/4", "1/12", "1/125"]), eqfrac("0.375", ["3/5", "3/7", "3/80"]), eqfrac("0.0625", ["1/8", "1/6", "1/625"]), eqfrac("0.08", ["1/8", "4/5", "8/25"])]
def mixgreat(s):
    vals = [v for _, v in s]; assert len(set(vals)) == 4
    best = max(s, key=lambda x: x[1])
    return tm("Which of these is the greatest?", best[0], [d for d, _ in s if d != best[0]], "Convert every number to a decimal and compare.")
hA8 = [mixgreat(s) for s in [
    [("$0.45$", Fr(9, 20)), ("$\\frac{1}{2}$", Fr(1, 2)), ("$0.405$", Fr(81, 200)), ("$\\frac{2}{5}$", Fr(2, 5))],
    [("$0.8$", Fr(4, 5)), ("$\\frac{7}{8}$", Fr(7, 8)), ("$0.85$", Fr(17, 20)), ("$\\frac{3}{4}$", Fr(3, 4))],
    [("$0.12$", Fr(3, 25)), ("$\\frac{1}{8}$", Fr(1, 8)), ("$0.102$", Fr(51, 500)), ("$\\frac{1}{10}$", Fr(1, 10))],
    [("$0.62$", Fr(31, 50)), ("$\\frac{3}{5}$", Fr(3, 5)), ("$0.602$", Fr(301, 500)), ("$\\frac{5}{8}$", Fr(5, 8))]]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]

def missing(a, x):
    p = D(a) * D(x)
    return QQ(f"Find the missing number: ${a}\\times\\square={fmt(p)}$.", "The missing number is the product divided by the known factor", f"$\\square={fmt(p)}\\div{a}={x}$")
def digits(ds):
    big = sorted(ds, reverse=True); small = sorted(ds)
    hi = D(f"{big[0]}{big[1]}.{big[2]}{big[3]}"); lo = D(f"{small[0]}{small[1]}.{small[2]}{small[3]}")
    return QQ(f"Using each of the digits ${', '.join(ds)}$ exactly once, form the largest and the smallest numbers having two digits before and two digits after the decimal point. Find their difference.", f"Largest: ${fmt(hi)}$ (digits in decreasing order)", f"Smallest: ${fmt(lo)}$ (digits in increasing order)", f"Difference $={fmt(hi)}-{fmt(lo)}={fmt(hi - lo)}$")
def halfway(a, b): return QQ(f"Find the decimal number exactly halfway between ${a}$ and ${b}$.", f"Add: ${a}+{b}={fmt(D(a) + D(b))}$", f"Halve: ${fmt(D(a) + D(b))}\\div2={fmt((D(a) + D(b)) / 2)}$")
HARD_B = ([missing(a, x) for a, x in [("0.6", "0.27"), ("1.5", "2.4"), ("0.35", "0.08"), ("2.5", "0.036")]]
          + [digits(ds) for ds in [("2", "5", "8", "4"), ("3", "9", "6", "1"), ("7", "2", "6", "5"), ("9", "4", "1", "8")]]
          + [halfway(*x) for x in [("0.3", "0.4"), ("1.26", "1.28"), ("4.5", "4.9"), ("0.07", "0.12")]])
def mix(a, b, c):
    v = D(a) * D(b) + D(c) / D(b)
    return QQ(f"Find the value of ${a}\\times{b}+{c}\\div{b}$.", f"${a}\\times{b}={fmt(D(a) * D(b))}$", f"${c}\\div{b}={fmt(D(c) / D(b))}$", f"Sum $={fmt(v)}$")
def apart(a, b, t, k):
    s = D(a) + D(b)
    return QQ(f"Two friends start from the same place and walk in opposite directions at ${a}$ km/h and ${b}$ km/h. How far apart are they after ${t}$ hours? After how many hours will they be ${fmt(s * k)}$ km apart?", f"They separate by ${a}+{b}={fmt(s)}$ km every hour", f"After ${t}$ hours: ${fmt(s)}\\times{t}={fmt(s * D(t))}$ km", f"Time $={fmt(s * k)}\\div{fmt(s)}={k}$ hours")
def rate(a, P, b):
    r = D(P) / D(a)
    return QQ(f"${a}$ kg of rice costs ₹${P}$. Find the price of 1 kg and the cost of ${b}$ kg.", f"Price per kg $={P}\\div{a}={fmt(r)}$", f"Cost of ${b}$ kg $={fmt(r)}\\times{b}={fmt(r * D(b))}$")
HARD_C = ([mix(*x) for x in [("2.5", "0.4", "1.6"), ("1.5", "0.6", "2.4"), ("0.8", "0.5", "3.5"), ("3.2", "1.5", "4.5"), ("0.75", "0.2", "1.2"), ("4.2", "0.3", "0.9")]]
          + [apart(*x) for x in [("3.5", "4.5", "2.5", 3), ("4.2", "3.8", "1.5", 4), ("5.5", "6.5", "2.5", 5), ("2.75", "3.25", "3.5", 6), ("6.4", "5.6", "1.25", 3), ("4.8", "5.2", "2.5", 7)]]
          + [rate(*x) for x in [("2.5", "135", "4.5"), ("1.5", "93", "2.5"), ("0.8", "50.4", "3.5"), ("4.5", "261", "2.5"), ("1.25", "70", "3"), ("3.5", "147", "1.5")]])
def leak(T, p, q):
    net = D(p) - D(q)
    return QQ(f"A tank of capacity ${T}$ litres is filled by a pipe at ${p}$ litres per minute, but a leak drains ${q}$ litres per minute. Find the net gain per minute and the time to fill the empty tank.", f"Net gain per minute $={p}-{q}={fmt(net)}$ litres", f"Time $={T}\\div{fmt(net)}={fmt(D(T) / net)}$ minutes")
def blend(a, x, b, y):
    cost = D(a) * D(x) + D(b) * D(y); kg = D(a) + D(b); per = cost / kg
    assert per == per.quantize(Dc("0.01"))
    return QQ(f"A shopkeeper mixes ${a}$ kg of tea costing ₹${x}$ per kg with ${b}$ kg of tea costing ₹${y}$ per kg. Find the total cost, the total weight and the cost of 1 kg of the mixture.", f"Total cost $={fmt(D(a) * D(x))}+{fmt(D(b) * D(y))}={fmt(cost)}$", f"Total weight $={fmt(kg)}$ kg", f"Cost per kg $={fmt(cost)}\\div{fmt(kg)}={fmt(per)}$")
HARD_D = ([leak(*x) for x in [("60", "7.5", "2.5"), ("84", "9.5", "2.5"), ("45", "6.25", "1.25"), ("72", "8.4", "2.4"), ("99", "5.75", "0.25"), ("52.5", "4.8", "1.3")]]
          + [blend(*x) for x in [("1.5", "120", "2.5", "200"), ("2", "240", "3", "180"), ("2.5", "160", "1.5", "240"), ("3.5", "80", "1.5", "120"), ("0.5", "300", "1.5", "180"), ("4", "150", "6", "225")]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
