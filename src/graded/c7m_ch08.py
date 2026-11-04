"""Class 7 Maths Ch 8 - Working with Fractions (multiplying and dividing fractions, reciprocals, mixed numbers, fractions of quantities)."""
from g67 import *

SLUG, NAME, CHNO = "Working_with_Fractions", "Working with Fractions", 8

def F(a, b=1): return Fr(a, b)
def X(f): return "$" + mx(f) + "$"          # mixed-number form
def Z(f): return "$" + fx(f) + "$"          # plain fraction form
def R(a, b): return "$" + raw(a, b) + "$"

def fo(q, c, why="", bad=()):
    """MCQ whose answer is a Fraction; misconception distractors first, then scaled variants."""
    c = Fr(c); opts = []
    for x in list(bad) + [c * 2, c / 2, c + Fr(1, c.denominator + 1), c + 1, abs(c - 1), c + Fr(1, 2), c * 3]:
        x = Fr(x)
        if x > 0 and x != c and x not in opts: opts.append(x)
    return M4(q, X(c), [X(x) for x in opts[:5]], why)

def mixed(w, r, d): return Fr(w) + Fr(r, d)
def MX(w, r, d): return f"${w}\\frac{{{r}}}{{{d}}}$"

# ------------------------------------------------ EASY
eA1 = [fo(f"The product of {R(a, b)} and {R(c, d)} is:", F(a, b) * F(c, d), "Multiply numerators and multiply denominators, then simplify.", bad=[F(a + c, b + d)])
       for a, b, c, d in [(2, 3, 3, 5), (3, 4, 2, 7), (4, 5, 5, 8), (5, 6, 3, 10), (7, 9, 3, 14)]]
eA2 = [fo(f"{R(a, b)} of {n} is:", F(a, b) * n, "'Of' means multiply.", bad=[F(n, b), F(n * b, a)])
       for a, b, n in [(2, 5, 20), (3, 4, 16), (5, 6, 18), (3, 8, 24), (4, 9, 27)]]
eA3 = [tm(f"The reciprocal of {R(a, b)} is:", Z(F(b, a)), [Z(F(a, b)), "$-" + fx(F(b, a)) + "$", Z(F(a + 1, b + 1))], "Turn the fraction upside down.")
       for a, b in [(3, 7), (5, 2), (8, 9), (4, 11)]] + [tm("The reciprocal of $6$ is:", R(1, 6), ["$6$", "$-6$", "$0$"], "Reciprocal of $n$ is $\\frac1n$.")]
eA4 = [fo(f"{R(a, b)} $\\div {n}$ equals:", F(a, b) / n, "Dividing by $n$ means multiplying by $\\frac1n$.", bad=[F(a, b) * n])
       for a, b, n in [(3, 4, 3), (6, 7, 2), (5, 6, 5), (8, 9, 4)]]
eA5 = [tm(t, c, w, "Recall the idea from the chapter.") for t, c, w in [
    ("The product of two proper fractions is always:", "smaller than each of the fractions", ["larger than each of them", "equal to their sum", "a whole number"]),
    ("Multiplying a number by a fraction less than 1 makes it:", "smaller", ["larger", "unchanged", "negative"]),
    ("$\\frac12$ of $\\frac12$ is:", R(1, 4), [R(1, 2), "$1$", R(1, 8)]),
    ("Dividing by $\\frac14$ is the same as multiplying by:", "$4$", [R(1, 4), "$1$", "$-4$"]),
    ("The reciprocal of $1$ is:", "$1$", ["$0$", "$-1$", "$2$"])]]
eA6 = [tm(f"The mixed number {MX(w, r, d)} written as an improper fraction is:", R(w * d + r, d), [R(w + r, d), R(w * d - r, d), R(w * d + r, w)], "Whole $\\times$ denominator + numerator, over the denominator.")
       for w, r, d in [(2, 1, 3), (3, 2, 5), (1, 3, 4), (4, 1, 6)]]
eA7 = [fo(f"A rectangle is {R(a, b)} m long and {R(c, d)} m wide. Its area in m$^2$ is:", F(a, b) * F(c, d), "Area = length $\\times$ breadth.", bad=[F(a, b) + F(c, d)])
       for a, b, c, d in [(1, 2, 2, 3), (3, 4, 2, 5), (5, 6, 3, 7), (2, 3, 3, 4)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]

def mulB(a, b, c, d):
    p = F(a, b) * F(c, d)
    return QQ(f"Multiply {R(a, b)} by {R(c, d)} and write in the lowest terms.", f"${raw(a, b)}\\times{raw(c, d)}={raw(f"{a}\\times{c}", f"{b}\\times{d}")}$", f"$={raw(a * c, b * d)}$", f"Lowest terms: {X(p)}")
def divB(a, b, c, d):
    p = F(a, b) / F(c, d)
    return QQ(f"Divide {R(a, b)} by {R(c, d)}.", f"Reciprocal of {R(c, d)} is {R(d, c)}", f"${raw(a, b)}\\times{raw(d, c)}={raw(a * d, b * c)}$", f"Answer {X(p)}")
def ofB(a, b, n, unit):
    return QQ(f"Find {R(a, b)} of {n} {unit}.", f"${raw(a, b)}\\times{n}$", f"$={raw(a * n, b)}$", f"Answer ${mx(F(a, b) * n)}$ {unit}")
EASY_B = ([mulB(*t) for t in [(3, 5, 10, 21), (4, 9, 3, 8), (5, 12, 6, 25), (7, 10, 15, 28)]]
          + [divB(*t) for t in [(3, 4, 9, 16), (5, 6, 10, 3), (7, 8, 21, 4), (2, 9, 4, 3)]]
          + [ofB(a, b, n, u) for a, b, n, u in [(3, 5, 40, "kg"), (5, 8, 64, "litres"), (2, 7, 49, "metres"), (7, 12, 60, "rupees")]])
def mixmul(w, r, d, c, e):
    f = mixed(w, r, d); p = f * F(c, e)
    return QQ(f"Find {MX(w, r, d)} $\\times$ {R(c, e)}.", f"Improper form: {MX(w, r, d)}$={raw(w * d + r, d)}$", f"${raw(w * d + r, d)}\\times{raw(c, e)}={raw((w * d + r) * c, d * e)}$", f"Answer {X(p)}")
def pieces(n, a, b):
    k = F(n) / F(a, b); assert k.denominator == 1
    return QQ(f"A ribbon {n} m long is cut into pieces of {R(a, b)} m each. How many pieces are made?", f"Pieces $=n\\div{raw(a, b)}$", f"${n}\\times{raw(b, a)}={raw(n * b, a)}$", f"Pieces $={k}$")
def rect(a, b, c, d):
    L, W = F(a, b), F(c, d)
    return QQ(f"A rectangular card is {R(a, b)} m long and {R(c, d)} m wide. Find its area and its perimeter.", f"Area $={raw(a, b)}\\times{raw(c, d)}$", f"Area $={mx(L * W)}$ m$^2$", f"Perimeter $=2({raw(a, b)}+{raw(c, d)})$", f"$=2\\times{raw(a * d + c * b, b * d)}$", f"Perimeter $={mx(2 * (L + W))}$ m")
EASY_C = ([mixmul(*t) for t in [(2, 1, 3, 3, 5), (1, 1, 2, 4, 9), (3, 1, 4, 2, 13), (2, 2, 5, 5, 6), (1, 2, 3, 3, 10), (4, 1, 2, 2, 3)]]
          + [pieces(*t) for t in [(6, 3, 4), (10, 5, 6), (9, 3, 8), (12, 2, 3), (14, 7, 10), (15, 5, 8)]]
          + [rect(*t) for t in [(3, 4, 2, 3), (5, 6, 3, 5), (2, 5, 5, 8), (7, 8, 4, 7), (3, 10, 5, 6), (4, 9, 3, 4)]])
def tank(n, a, b, c, d):
    full = F(a, b) * n; used = F(c, d) * full
    return QQ(f"A tank holds {n} litres. It is {R(a, b)} full. {R(c, d)} of the water in it is then used. Find the water at first, the water used and the water left.", f"At first ${raw(a, b)}\\times{n}={mx(full)}$ L", f"Used ${raw(c, d)}\\times{mx(full)}={mx(used)}$ L", f"Left $={mx(full)}-{mx(used)}$", f"$={mx(full - used)}$ L", "State all three answers")
def flour(w, a, b):
    k = F(w) / F(a, b); cakes = k.numerator // k.denominator; left = F(w) - cakes * F(a, b)
    return QQ(f"A baker has {w} kg of flour. One cake needs {R(a, b)} kg. How many full cakes can be made and how much flour is left over?", f"Cakes $={w}\\div{raw(a, b)}={mx(k)}$", f"Full cakes $={cakes}$", f"Flour used $={cakes}\\times{raw(a, b)}={mx(cakes * F(a, b))}$ kg", f"Left over $={mx(left)}$ kg", "Final statement")
EASY_D = ([tank(*t) for t in [(120, 3, 4, 2, 3), (80, 5, 8, 4, 5), (90, 2, 3, 3, 4), (150, 4, 5, 5, 6), (72, 7, 9, 3, 7), (60, 5, 6, 3, 5)]]
          + [flour(*t) for t in [(5, 3, 4), (7, 2, 3), (4, 5, 6), (9, 4, 5), (6, 7, 8), (8, 3, 10)]])

# ------------------------------------------------ NCERT
nA1 = [fo(f"How many pieces of length {R(a, b)} m can be cut from a rope of {n} m?", F(n) / F(a, b), "Number of pieces $=n\\div$ piece length.", bad=[F(n) * F(a, b)])
       for a, b, n in [(1, 4, 3), (1, 2, 7), (1, 3, 4), (3, 4, 6), (2, 5, 4)]]
nA2 = [fo(f"Scaling a drawing by {R(a, b)}: a line of {n} cm becomes (cm):", F(a, b) * n, "Scaling by a fraction is multiplication.", bad=[F(n * b, a)])
       for a, b, n in [(3, 4, 20), (2, 3, 21), (5, 6, 18), (3, 5, 35)]]
nA3 = [tm(t, c, w, "Use the meaning of multiplying and dividing fractions.") for t, c, w in [
    ("The number of $\\frac14$s in $2$ is:", "$8$", ["$4$", "$6$", "$2$"]),
    ("The number of $\\frac13$s in $\\frac23$ is:", "$2$", ["$3$", "$\\frac29$", "$1$"]),
    ("$\\frac34$ of $\\frac23$ is:", R(1, 2), [R(1, 3), R(5, 7), R(9, 8)]),
    ("Which is larger: $4\\times\\frac12$ or $4\\div\\frac12$?", "$4\\div\\frac12$", ["$4\\times\\frac12$", "they are equal", "cannot say"]),
    ("When a number is multiplied by $\\frac32$, the result is:", "greater than the number", ["less than the number", "equal to the number", "zero"])]]
nA4 = [fo(f"{MX(w, r, d)} $\\times {n}$ equals:", mixed(w, r, d) * n, "Convert to an improper fraction and multiply.", bad=[Fr(w * n) + Fr(r, d)])
       for w, r, d, n in [(1, 1, 2, 4), (2, 1, 3, 6), (3, 3, 4, 8), (1, 2, 5, 5)]]
nA5 = [fo(f"The reciprocal of {MX(w, r, d)} (as a fraction) is:", Fr(d, w * d + r), "Write as an improper fraction, then invert.", bad=[Fr(d, w * d + r) * 2])
       for w, r, d in [(1, 1, 2), (2, 1, 4), (3, 2, 3), (1, 3, 5)]]
nA6 = [fo(f"{R(a, b)} $\\div$ {R(c, d)} equals:", F(a, b) / F(c, d), "Multiply by the reciprocal of the divisor.", bad=[F(a, b) * F(c, d)])
       for a, b, c, d in [(1, 2, 1, 4), (3, 4, 3, 8), (5, 6, 5, 12), (2, 3, 4, 9), (7, 10, 7, 5)]]
nA7 = [fo(f"A recipe uses {R(a, b)} cup of sugar for one batch. For {n} batches the sugar needed (cups) is:", F(a, b) * n, "Multiply the quantity by the number of batches.")
       for a, b, n in [(3, 4, 6), (2, 3, 9), (5, 8, 4), (1, 6, 15)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]

def howmany(a, b, c, d):
    k = F(a, b) / F(c, d)
    return QQ(f"How many {R(c, d)}s are there in {R(a, b)}?", f"Count $={raw(a, b)}\\div{raw(c, d)}$", f"$={raw(a, b)}\\times{raw(d, c)}={raw(a * d, b * c)}$", f"Answer {X(k)}")
def fofof(a, b, c, d, n, u):
    return QQ(f"Find {R(a, b)} of {R(c, d)} of {n} {u}.", f"${raw(c, d)}$ of {n}$={mx(F(c, d) * n)}$", f"${raw(a, b)}\\times{mx(F(c, d) * n)}$", f"$={mx(F(a, b) * F(c, d) * n)}$ {u}")
def missing(a, b, c, d):
    x = F(c, d) / F(a, b)
    return QQ(f"What fraction multiplied by {R(a, b)} gives {R(c, d)}?", f"$x\\times{raw(a, b)}={raw(c, d)}$", f"$x={raw(c, d)}\\div{raw(a, b)}$", f"$x={mx(x)}$")
NCERT_B = ([howmany(*t) for t in [(3, 4, 1, 8), (5, 2, 5, 6), (2, 3, 1, 9), (7, 4, 7, 16)]]
           + [fofof(*t) for t in [(2, 3, 3, 4, 48, "kg"), (3, 5, 5, 6, 36, "litres"), (1, 2, 2, 7, 70, "metres"), (3, 4, 8, 9, 54, "rupees")]]
           + [missing(*t) for t in [(2, 5, 4, 15), (3, 4, 9, 20), (5, 6, 25, 36), (7, 8, 21, 40)]])
def photo(a, b, c, d):
    p = F(a, b) * F(c, d)
    return QQ(f"A rectangle has sides {R(a, b)} m and {R(c, d)} m. Show its area as the product of the sides and compare it with the area of the smaller side squared.", f"Area $={raw(a, b)}\\times{raw(c, d)}={mx(p)}$ m$^2$", f"Smaller side squared $={mx(min(F(a, b), F(c, d)) ** 2)}$ m$^2$", f"Difference $={mx(p - min(F(a, b), F(c, d)) ** 2)}$ m$^2$")
def mixdiv(w, r, d, e, f):
    q = mixed(w, r, d) / F(e, f)
    return QQ(f"Divide {MX(w, r, d)} by {R(e, f)} and write the answer as a mixed number.", f"Improper form ${raw(w * d + r, d)}$", f"${raw(w * d + r, d)}\\times{raw(f, e)}$", f"$={raw((w * d + r) * f, d * e)}$", f"Answer {X(q)}")
def cloth(w, r, d, n):
    each = mixed(w, r, d); tot = each * n
    return QQ(f"One shirt needs {MX(w, r, d)} m of cloth. How much cloth is needed for {n} shirts? How many shirts can be made from {mx(tot + each / 2)} m?", f"Cloth for {n} shirts $={n}\\times{raw(w * d + r, d)}$", f"$={mx(tot)}$ m", f"Shirts from {mx(tot + each / 2)} m $={mx((tot + each / 2) / each)}$", f"Full shirts $={n}$")
NCERT_C = ([photo(*t) for t in [(3, 4, 2, 5), (5, 6, 3, 10), (7, 8, 4, 9), (2, 3, 9, 10), (5, 8, 4, 15), (3, 7, 14, 15)]]
           + [mixdiv(*t) for t in [(2, 1, 2, 3, 4), (1, 2, 3, 5, 6), (3, 1, 3, 5, 9), (2, 3, 4, 8, 15), (1, 1, 4, 5, 12), (4, 1, 2, 3, 8)]]
           + [cloth(*t) for t in [(1, 1, 4, 8), (2, 1, 2, 6), (1, 2, 3, 9), (2, 1, 4, 12), (1, 3, 4, 10), (3, 1, 3, 9)]])
def trip(d, a, b, c, e):
    first = F(a, b) * d; rest = d - first; second = F(c, e) * rest
    return QQ(f"A journey of {d} km is done in three parts. The first part is {R(a, b)} of the journey; {R(c, e)} of the remaining distance is covered next. Find both distances and the distance still left.", f"First part $={raw(a, b)}\\times{d}={mx(first)}$ km", f"Remaining $={d}-{mx(first)}={mx(rest)}$ km", f"Second part $={raw(c, e)}\\times{mx(rest)}={mx(second)}$ km", f"Left $={mx(rest)}-{mx(second)}$", f"$={mx(rest - second)}$ km")
def garden(a, b, c, d, e, f):
    L, W = F(a, b), F(c, d); area = L * W; veg = F(e, f) * area
    return QQ(f"A garden is {R(a, b)} hm long and {R(c, d)} hm wide. {R(e, f)} of it is used for vegetables and the rest for flowers. Find the area of the garden, of the vegetable part and of the flower part (in hm$^2$).", f"Area $={raw(a, b)}\\times{raw(c, d)}={mx(area)}$", f"Vegetable part $={raw(e, f)}\\times{mx(area)}={mx(veg)}$", f"Flower part $={mx(area)}-{mx(veg)}$", f"$={mx(area - veg)}$", "State the three areas with units")
NCERT_D = ([trip(*t) for t in [(120, 1, 4, 2, 3), (90, 1, 3, 3, 4), (160, 3, 8, 2, 5), (84, 2, 7, 3, 5), (150, 2, 5, 5, 6), (200, 3, 10, 4, 7)]]
           + [garden(*t) for t in [(4, 5, 5, 6, 3, 4), (3, 4, 8, 9, 2, 3), (5, 6, 6, 7, 4, 5), (7, 8, 4, 5, 5, 7), (9, 10, 5, 6, 2, 5), (2, 3, 3, 8, 5, 6)]])

# ------------------------------------------------ MEDIUM
mA1 = [fo(f"{MX(w, r, d)} $\\times$ {MX(w2, r2, d2)} equals:", mixed(w, r, d) * mixed(w2, r2, d2), "Convert both to improper fractions first.", bad=[Fr(w * w2) + Fr(r * r2, d * d2)])
       for w, r, d, w2, r2, d2 in [(1, 1, 2, 2, 1, 3), (2, 1, 4, 1, 1, 3), (1, 2, 3, 3, 1, 5), (2, 1, 2, 2, 2, 5)]]
mA2 = [fo(f"{MX(w, r, d)} $\\div$ {R(a, b)} equals:", mixed(w, r, d) / F(a, b), "Improper form, then multiply by the reciprocal.", bad=[mixed(w, r, d) * F(a, b)])
       for w, r, d, a, b in [(1, 1, 2, 3, 4), (2, 2, 3, 4, 9), (3, 1, 3, 5, 6), (1, 3, 4, 7, 8)]]
mA3 = [fo(f"{R(a, b)} $\\times$ {R(c, d)} $\\div$ {R(e, f)} equals:", F(a, b) * F(c, d) / F(e, f), "Work from left to right.")
       for a, b, c, d, e, f in [(2, 3, 3, 4, 1, 2), (3, 5, 5, 6, 3, 4), (4, 7, 7, 8, 2, 3), (5, 9, 3, 10, 1, 6), (7, 10, 5, 14, 5, 8)]]
mA4 = [fo(f"If {R(a, b)} of a number is {c}, the number is:", F(c) / F(a, b), "Number $=$ part $\\div$ fraction.", bad=[F(c) * F(a, b)])
       for a, b, c in [(2, 3, 14), (3, 5, 18), (5, 8, 25), (3, 7, 12)]]
mA5 = [fo(f"A tap fills {R(a, b)} of a tank in 1 hour. The time (hours) to fill the whole tank is:", F(b, a), "Time $=1\\div$ rate.")
       for a, b in [(2, 5), (3, 8), (4, 9), (5, 7), (3, 10)]]
mA6 = [tm(t, c, w, "Compare by computing.") for t, c, w in [
    ("Which is the greatest?", "$\\frac34\\div\\frac18$", ["$\\frac34\\times\\frac18$", "$\\frac34$", "$\\frac18$"]),
    ("$\\frac25\\times\\frac52$ equals:", "$1$", [R(4, 25), R(2, 5), "$0$"]),
    ("The product of a number and its reciprocal is:", "$1$", ["$0$", "the number itself", "$2$"]),
    ("If $x\\times\\frac37=1$, then $x$ is:", R(7, 3), [R(3, 7), "$1$", R(10, 7)])]]
mA7 = [fo(f"A car travels {R(a, b)} km on 1 litre of petrol. On {n} litres it travels (km):", F(a, b) * n, "Distance = rate $\\times$ quantity.")
       for a, b, n in [(35, 2, 6), (47, 4, 8), (51, 3, 5), (29, 6, 12)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]

def simp(a, b, c, d, e, f):
    v = F(a, b) * F(c, d) / F(e, f)
    return QQ(f"Simplify {R(a, b)} $\\times$ {R(c, d)} $\\div$ {R(e, f)}.", f"Left to right: ${raw(a, b)}\\times{raw(c, d)}={mx(F(a, b) * F(c, d))}$", f"Then divide: ${mx(F(a, b) * F(c, d))}\\times{raw(f, e)}$", f"Answer {X(v)}")
def findnum(a, b, c):
    n = F(c) / F(a, b)
    return QQ(f"{R(a, b)} of a number is {c}. Find the number and also {R(b - a, b)} of it.", f"Number $={c}\\div{raw(a, b)}$", f"$={mx(n)}$", f"{R(b - a, b)} of it $={mx(F(b - a, b) * n)}$")
def mixsum(w, r, d, c, e):
    p = mixed(w, r, d) * F(c, e)
    return QQ(f"Find {MX(w, r, d)} $\\times$ {R(c, e)} and compare it with {MX(w, r, d)}. Is the product smaller or greater? Why?", f"Product $={mx(p)}$", f"Compare with {mx(mixed(w, r, d))}", f"The product is {'smaller' if p < mixed(w, r, d) else 'greater'}", f"Because the multiplier is {'less' if F(c, e) < 1 else 'more'} than 1")
MED_B = ([simp(*t) for t in [(2, 3, 9, 10, 3, 5), (5, 6, 4, 15, 2, 9), (7, 8, 16, 21, 4, 3), (3, 4, 8, 9, 5, 6)]]
         + [findnum(*t) for t in [(3, 4, 27), (2, 5, 18), (5, 6, 35), (4, 9, 32)]]
         + [mixsum(*t) for t in [(2, 1, 2, 3, 5), (1, 1, 3, 9, 8), (3, 1, 4, 2, 3), (2, 2, 5, 5, 4)]])
def sheet(w, r, d, w2, r2, d2):
    L, B = mixed(w, r, d), mixed(w2, r2, d2)
    return QQ(f"A sheet is {MX(w, r, d)} m long and {MX(w2, r2, d2)} m wide. Find its area and perimeter.", f"Area $={raw(w * d + r, d)}\\times{raw(w2 * d2 + r2, d2)}$", f"$={mx(L * B)}$ m$^2$", f"Perimeter $=2({mx(L)}+{mx(B)})$", f"$=2\\times{mx(L + B)}$", f"$={mx(2 * (L + B))}$ m")
def share(n, a, b, k):
    left = n - F(a, b) * n; each = left / k
    return QQ(f"Mohan has ₹{n}. He spends {R(a, b)} of it and shares the rest equally among {k} children. How much does each child get?", f"Spent $={raw(a, b)}\\times{n}={mx(F(a, b) * n)}$", f"Left $={n}-{mx(F(a, b) * n)}={mx(left)}$", f"Each $={mx(left)}\\div{k}$", f"$=₹{mx(each)}$")
def oper(a, b, c, d, e, f):
    v = (F(a, b) + F(c, d)) * F(e, f); s = F(a, b) + F(c, d)
    return QQ(f"Evaluate $\\left({raw(a, b)}+{raw(c, d)}\\right)\\times{raw(e, f)}$.", f"Bracket: ${raw(a, b)}+{raw(c, d)}={mx(s)}$", f"Multiply: ${mx(s)}\\times{raw(e, f)}$", f"$={mx(v)}$")
MED_C = ([sheet(*t) for t in [(1, 1, 2, 2, 1, 4), (2, 1, 3, 1, 1, 2), (3, 1, 2, 2, 1, 3), (1, 3, 4, 2, 1, 2), (2, 2, 3, 1, 1, 4), (4, 1, 2, 3, 1, 3)]]
         + [share(*t) for t in [(240, 1, 4, 6), (360, 2, 5, 9), (450, 1, 3, 5), (560, 3, 8, 7), (420, 2, 7, 10), (630, 4, 9, 7)]]
         + [oper(*t) for t in [(1, 2, 1, 3, 6, 5), (3, 4, 1, 6, 12, 7), (2, 3, 3, 5, 15, 19), (5, 8, 1, 4, 16, 21), (1, 4, 2, 5, 20, 9), (3, 5, 1, 10, 10, 7)]])
def painting(n, a, b, c, d):
    day1 = F(a, b) * n; rest = n - day1; day2 = F(c, d) * rest
    return QQ(f"A wall of {n} m$^2$ is painted in three days. On day 1, {R(a, b)} of it is painted; on day 2, {R(c, d)} of the remainder; the rest on day 3. Find the area painted on each day.", f"Day 1 $={raw(a, b)}\\times{n}={mx(day1)}$ m$^2$", f"Remainder $={mx(rest)}$ m$^2$", f"Day 2 $={raw(c, d)}\\times{mx(rest)}={mx(day2)}$ m$^2$", f"Day 3 $={mx(rest)}-{mx(day2)}$", f"$={mx(rest - day2)}$ m$^2$")
def mixture(w, r, d, a, b, k):
    tot = mixed(w, r, d); s = F(a, b) * tot; wat = tot - s; cups = tot / F(1, k)
    return QQ(f"A jug holds {MX(w, r, d)} litres of squash. {R(a, b)} of it is syrup and the rest is water. Find the syrup and the water. How many glasses of {R(1, k)} litre can be filled from the jug?", f"Syrup $={raw(a, b)}\\times{raw(w * d + r, d)}={mx(s)}$ L", f"Water $={mx(tot)}-{mx(s)}={mx(wat)}$ L", f"Glasses $={mx(tot)}\\div{raw(1, k)}$", f"$={mx(cups)}$", "Full glasses: " + str(cups.numerator // cups.denominator))
MED_D = ([painting(*t) for t in [(240, 1, 4, 2, 3), (180, 2, 5, 1, 3), (300, 3, 10, 5, 7), (210, 1, 6, 3, 5), (320, 3, 8, 4, 5), (270, 2, 9, 3, 7)]]
         + [mixture(*t) for t in [(2, 1, 2, 2, 5, 4), (1, 3, 4, 3, 7, 5), (3, 1, 3, 3, 10, 6), (2, 2, 3, 3, 8, 4), (1, 1, 2, 4, 9, 3), (2, 3, 4, 5, 11, 8)]])

# ------------------------------------------------ HARD
hA1 = [fo(f"{R(a, b)} $\\div$ ({R(c, d)} $\\div$ {R(e, f)}) equals:", F(a, b) / (F(c, d) / F(e, f)), "Work the bracket first.", bad=[F(a, b) / F(c, d) / F(e, f)])
       for a, b, c, d, e, f in [(3, 4, 3, 2, 1, 2), (5, 6, 5, 3, 2, 3), (2, 3, 4, 5, 2, 5), (7, 8, 7, 4, 1, 4), (9, 10, 3, 5, 3, 2)]]
hA2 = [fo(f"{R(a, b)} of a number is {n}. Three times the number is:", F(n) * 3 / F(a, b), "Find the number first.")
       for a, b, n in [(2, 5, 18), (3, 7, 12), (4, 9, 20), (2, 3, 14)]]
hA3 = [fo(f"A pipe fills {R(a, b)} of a tank in {c} minutes. The time to fill the whole tank (minutes) is:", F(c) / F(a, b), "Time for the whole $=$ time for the part $\\div$ fraction.")
       for a, b, c in [(2, 5, 12), (3, 4, 15), (5, 6, 20), (3, 8, 9)]]
hA4 = [fo(f"A wall is {R(a, b)} painted. After {R(c, d)} of the remaining part is painted, the fraction of the whole still unpainted is:", (1 - F(a, b)) * (1 - F(c, d)), "Unpainted = (unpainted before) $\\times$ (what is not painted of it).")
       for a, b, c, d in [(1, 3, 1, 2), (2, 5, 2, 3), (3, 8, 3, 5), (1, 4, 4, 9)]]
hA5 = [tm(t, c, w, "Reason about the size of products and quotients.") for t, c, w in [
    ("If $0<x<1$, then $\\frac{1}{x}$ is:", "greater than 1", ["less than 1", "equal to 1", "negative"]),
    ("For which $x$ is $x\\div\\frac13$ less than $x$?", "no positive $x$", ["$x>1$", "$x<1$", "every $x$"]),
    ("$\\frac23\\times\\frac32\\times\\frac45$ equals:", R(4, 5), ["$1$", R(8, 15), R(2, 3)]),
    ("Which has the greatest value?", "$6\\div\\frac23$", ["$6\\times\\frac23$", "$6\\div\\frac32$", "$6\\times\\frac34$"]),
    ("$\\frac{1}{\\frac{2}{5}}$ is equal to:", R(5, 2), [R(2, 5), "$2$", R(1, 5)])]]
hA6 = [fo(f"{R(a, b)} of {MX(w, r, d)} is:", F(a, b) * mixed(w, r, d), "Multiply the fraction by the mixed number.", bad=[F(a, b) + mixed(w, r, d)])
       for a, b, w, r, d in [(3, 5, 3, 1, 3), (5, 7, 2, 4, 5), (7, 9, 4, 1, 2), (5, 12, 2, 2, 5)]]
hA7 = [fo(f"If $x\\times{R(a, b)}={R(c, d)}$, then $x\\div{R(e, f)}$ is:", F(c, d) / F(a, b) / F(e, f), "Find $x$ first.")
       for a, b, c, d, e, f in [(3, 4, 9, 16, 3, 4), (2, 5, 4, 15, 2, 3), (5, 6, 5, 9, 5, 12), (7, 9, 7, 6, 3, 1)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7]

def nested(a, b, c, d, e, f):
    v = (F(a, b) + F(c, d)) / (F(a, b) - F(c, d)) * F(e, f)
    return QQ(f"Simplify $\\left({raw(a, b)}+{raw(c, d)}\\right)\\div\\left({raw(a, b)}-{raw(c, d)}\\right)\\times{raw(e, f)}$.", f"Sum $={mx(F(a, b) + F(c, d))}$", f"Difference $={mx(F(a, b) - F(c, d))}$", f"Quotient $={mx((F(a, b) + F(c, d)) / (F(a, b) - F(c, d)))}$", f"Final $={mx(v)}$")
def twothirds(a, b, c):
    n = F(c) / F(a, b)
    return QQ(f"After {R(a, b)} of a number is removed, {c} is left. Find the number and the part removed.", f"Left $=1-{raw(a, b)}={raw(b - a, b)}$ of the number", f"Number $={c}\\div{raw(b - a, b)}={mx(F(c) / F(b - a, b))}$", f"Removed $={mx(F(a, b) * F(c) / F(b - a, b))}$")
def mean2(a, b, c, d):
    m = (F(a, b) + F(c, d)) / 2
    return QQ(f"Find the fraction exactly halfway between {R(a, b)} and {R(c, d)}, and verify that its distance from each is the same.", f"Mean $=\\frac12\\left({raw(a, b)}+{raw(c, d)}\\right)$", f"$={mx(m)}$", f"Distance from {R(a, b)}: ${mx(m - F(a, b))}$", f"Distance from {R(c, d)}: ${mx(F(c, d) - m)}$ (equal)")
HARD_B = ([nested(*t) for t in [(5, 6, 1, 3, 1, 2), (7, 8, 3, 8, 4, 5), (3, 4, 1, 4, 2, 3), (2, 3, 1, 6, 5, 7)]]
          + [twothirds(*t) for t in [(2, 7, 35), (3, 8, 45), (4, 9, 60), (5, 11, 42)]]
          + [mean2(*t) for t in [(1, 3, 1, 2), (2, 5, 3, 4), (1, 6, 5, 6), (3, 8, 7, 12)]])
def work(a, b):
    r1, r2 = F(1, a), F(1, b); t = 1 / (r1 + r2)
    return QQ(f"Ravi alone can finish a job in {a} days and Sita alone in {b} days. What fraction of the job do they finish together in one day, and how many days do they take together?", f"Ravi's one day work $={raw(1, a)}$, Sita's $={raw(1, b)}$", f"Together in one day $={mx(r1 + r2)}$", f"Days $=1\\div{mx(r1 + r2)}$", f"$={mx(t)}$ days")
def speed(a, b, c, d, t1, t2):
    d1 = F(a, b) * t1; d2 = F(c, d) * t2
    return QQ(f"A cyclist rides at {R(a, b)} km per hour for {t1} hours, then at {R(c, d)} km per hour for {t2} hours. Find the total distance and the average speed for the whole journey.", f"First distance $={mx(d1)}$ km", f"Second distance $={mx(d2)}$ km", f"Total $={mx(d1 + d2)}$ km in ${t1 + t2}$ hours", f"Average speed $={mx((d1 + d2) / (t1 + t2))}$ km/h")
def lens(w, r, d, n):
    each = mixed(w, r, d); k = F(n) / each
    return QQ(f"A pole of {n} m is cut into pieces of {MX(w, r, d)} m each. How many pieces are obtained and how much is left?", f"Pieces $={n}\\div{raw(w * d + r, d)}={mx(k)}$", f"Full pieces $={k.numerator // k.denominator}$", f"Used $={mx(each * (k.numerator // k.denominator))}$ m", f"Left $={mx(n - each * (k.numerator // k.denominator))}$ m", "Final statement")
HARD_C = ([work(a, b) for a, b in [(6, 3), (10, 15), (12, 4), (20, 30), (8, 24), (9, 18)]]
          + [speed(*t) for t in [(9, 2, 15, 4, 2, 4), (21, 2, 35, 4, 4, 2), (27, 2, 18, 5, 2, 5), (45, 4, 15, 2, 4, 2), (33, 4, 11, 2, 4, 6), (25, 2, 35, 3, 6, 3)]]
          + [lens(*t) for t in [(1, 2, 3, 20), (2, 1, 4, 25), (1, 3, 4, 18), (3, 1, 2, 30), (1, 1, 5, 17), (2, 2, 3, 22)]])
def estate(n, a, b, c, d, e, f):
    s1 = F(a, b) * n; r1 = n - s1; s2 = F(c, d) * r1; r2 = r1 - s2; s3 = F(e, f) * r2
    return QQ(f"A farmer's land is {n} acres. He sells {R(a, b)} of it, gives {R(c, d)} of the remainder to his son and plants {R(e, f)} of what is left after that with sugarcane. Find each area and the area left unplanted.", f"Sold $={mx(s1)}$ acres; remainder $={mx(r1)}$", f"Given to son $={mx(s2)}$ acres; remainder $={mx(r2)}$", f"Sugarcane $={raw(e, f)}\\times{mx(r2)}={mx(s3)}$ acres", f"Unplanted $={mx(r2)}-{mx(s3)}={mx(r2 - s3)}$ acres", f"As a fraction of the whole land, unplanted $={mx((r2 - s3) / n)}$")
def cistern(a, b, c):
    r = F(1, a) + F(1, b) - F(1, c); t = 1 / r if r > 0 else None
    return QQ(f"Pipe A fills a tank in {a} hours, pipe B in {b} hours, and a drain empties the full tank in {c} hours. Find the fraction filled in 1 hour with all three open, and the time to fill the empty tank.", f"A: {R(1, a)}, B: {R(1, b)} per hour", f"Drain: {R(1, c)} per hour (emptying)", f"Net per hour $={mx(r)}$", f"Time $=1\\div{mx(r)}={mx(t)}$ hours")
HARD_D = ([estate(*t) for t in [(240, 1, 4, 1, 3, 3, 4), (360, 2, 5, 1, 6, 4, 5), (450, 1, 3, 3, 5, 5, 6), (180, 1, 6, 2, 5, 3, 8), (420, 3, 7, 1, 4, 2, 3), (300, 2, 5, 5, 9, 3, 5)]]
          + [cistern(*t) for t in [(6, 12, 24), (4, 12, 6), (10, 15, 30), (8, 24, 12), (5, 20, 10), (6, 9, 18)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
