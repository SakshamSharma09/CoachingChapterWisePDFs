"""Class 9 Maths Ch 6 - Perimeter and Area (circle, arc, parallelogram, triangle, Heron's formula, Brahmagupta's formula)."""
from c9h import *

SLUG, NAME, CHNO = "Perimeter_and_Area", "Perimeter and Area", 6
PI = "$\\pi=\\frac{22}{7}$"

def heron(a, b, c):
    s2 = a + b + c; p = s2 * (s2 - 2 * a) * (s2 - 2 * b) * (s2 - 2 * c)
    r = isqrt(p); assert r * r == p and r % 4 == 0, (a, b, c)
    return r // 4
def hsteps(a, b, c):
    s = Fr(a + b + c, 2); A = heron(a, b, c)
    return s, A
def sh(s): return fx(s)
def brah(a, b, c, d):
    p2 = (-a + b + c + d) * (a - b + c + d) * (a + b - c + d) * (a + b + c - d)
    r = isqrt(p2); assert r * r == p2 and r % 4 == 0, (a, b, c, d)
    return r // 4
def search_br():
    out = []
    for a in range(4, 31):
        for b in range(a + 1, 31):
            for c in range(b + 1, 31):
                for d in range(c + 1, 31):
                    if d >= a + b + c or (a + b + c + d) % 2: continue
                    p2 = (-a + b + c + d) * (a - b + c + d) * (a + b - c + d) * (a + b + c - d)
                    r = isqrt(p2)
                    if r * r == p2 and r % 4 == 0: out.append((a, b, c, d, r // 4))
    return sorted(out, key=lambda t: (sum(t[:4]), t))
BR = search_br()
BR_N, BR_M, BR_H = BR[0:60:10], BR[4:64:10], BR[8:68:10]
def circ(r): return 2 * 22 * r // 7          # r a multiple of 7
def carea(r): return 22 * r * r // 7
def arc(r, th):
    v = Fr(th, 360) * Fr(44 * r, 7); return v
def axx(v):
    v = Fr(v); return str(v.numerator) if v.denominator == 1 else fx(v)

# ------------------------------------------------------------------ EASY
eA1 = [nm(f"The area of a rectangle of length ${l}$ cm and breadth ${b}$ cm is (cm$^2$):", l * b, "Area $=l\\times b$.") for l, b in [(12, 7), (15, 9), (18, 6), (25, 8)]]
eA2 = [nm(f"The perimeter of a rectangle of length ${l}$ cm and breadth ${b}$ cm is (cm):", 2 * (l + b), "Perimeter $=2(l+b)$.") for l, b in [(14, 9), (20, 11), (16, 13), (30, 12)]]
eA3 = [nm(f"The perimeter of a square of side ${s}$ cm is (cm):", 4 * s, "Perimeter $=4\\times$ side.") for s in [9, 13, 17, 25]]
eA4 = [nm(f"The area of a triangle with base ${b}$ cm and height ${h}$ cm is (cm$^2$):", b * h // 2, "Area $=\\frac12\\times$ base $\\times$ height.") for b, h in [(12, 8), (16, 9), (14, 11), (20, 7)]]
eA5 = [nm(f"The area of a parallelogram with base ${b}$ cm and height ${h}$ cm is (cm$^2$):", b * h, "Area $=$ base $\\times$ height.") for b, h in [(15, 8), (12, 13), (18, 7), (25, 4)]]
eA6 = [nm(f"The circumference of a circle of radius ${r}$ cm (take {PI}) is (cm):", circ(r), "$C=2\\pi r$.") for r in [7, 14, 21, 35]]
eA7 = [nm(f"The area of a circle of radius ${r}$ cm (take {PI}) is (cm$^2$):", carea(r), "$A=\\pi r^2$.") for r in [7, 14, 21, 28]]
eA8 = [nm(f"A circle has circumference ${circ(r)}$ cm (take {PI}). Its radius is (cm):", r, "$r=\\frac{C}{2\\pi}$.") for r in [7, 21, 35, 49]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Find the circumference of a circle of radius ${r}$ cm (take {PI}).", f"$C=2\\pi r=2\\times\\frac{{22}}{{7}}\\times{r}$", f"$C={circ(r)}$ cm") for r in [21, 42, 56, 63]]
          + [QQ(f"Find the area of a circle of radius ${r}$ cm (take {PI}).", f"$A=\\pi r^2=\\frac{{22}}{{7}}\\times{r}\\times{r}$", f"$A={carea(r)}$ cm$^2$") for r in [7, 14, 35, 42]]
          + [QQ(f"Find the area of a triangle with base ${b}$ cm and height ${h}$ cm.", f"$A=\\frac12\\times{b}\\times{h}$", f"$A={b * h // 2}$ cm$^2$") for b, h in [(18, 10), (24, 7), (30, 16), (22, 9)]])
EASY_C = ([QQ(f"The area of a parallelogram is ${b * h}$ cm$^2$ and its base is ${b}$ cm. Find its height.", f"Area $=$ base $\\times$ height", f"${b * h}={b}\\times h$", f"$h={h}$ cm") for b, h in [(12, 9), (15, 8), (20, 7), (16, 11), (25, 6), (18, 13)]]
          + [QQ(f"Find the area of a triangle with sides ${a}$ cm, ${b}$ cm and ${c}$ cm using Heron's formula.", f"$s=\\frac{{{a}+{b}+{c}}}{{2}}={sh(hsteps(a, b, c)[0])}$", f"$A=\\sqrt{{s(s-a)(s-b)(s-c)}}$", f"$A={heron(a, b, c)}$ cm$^2$") for a, b, c in [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15), (8, 15, 17), (7, 24, 25)]]
          + [QQ(f"Find the area of a trapezium with parallel sides ${a}$ cm and ${b}$ cm and height ${h}$ cm.", "$A=\\frac12(a+b)h$", f"$A=\\frac12\\times({a}+{b})\\times{h}$", f"$A={(a + b) * h // 2}$ cm$^2$") for a, b, h in [(10, 14, 6), (12, 18, 8), (9, 15, 10), (16, 20, 5), (7, 13, 12), (11, 19, 4)]])
EASY_D = ([QQ(f"A rectangular field is ${l}$ m long and ${b}$ m wide. Find its perimeter and area, and the cost of fencing it at ₹{r} per metre.", f"Perimeter $=2({l}+{b})={2 * (l + b)}$ m", f"Area $={l}\\times{b}={l * b}$ m$^2$", f"Cost $={2 * (l + b)}\\times{r}$", f"$=$ ₹{2 * (l + b) * r}", "Units stated") for l, b, r in [(40, 25, 12), (60, 35, 15), (45, 30, 20), (50, 28, 18), (72, 48, 10), (55, 45, 25)]]
          + [QQ(f"A circular park has radius ${r}$ m. Find its circumference and area (take {PI}), and the cost of fencing it at ₹{c} per metre.", f"$C=2\\pi r={circ(r)}$ m", f"$A=\\pi r^2={carea(r)}$ m$^2$", f"Cost $={circ(r)}\\times{c}$", f"$=$ ₹{circ(r) * c}", "Units stated") for r, c in [(14, 15), (21, 12), (28, 10), (35, 8), (42, 5), (49, 6)]])

# ------------------------------------------------------------------ NCERT
nA1 = [nm(f"The area of a triangle with sides ${a}$ cm, ${b}$ cm and ${c}$ cm is (cm$^2$):", heron(a, b, c), "Use Heron's formula.") for a, b, c in [(13, 14, 15), (7, 15, 20), (9, 10, 17), (10, 17, 21), (4, 13, 15)]]
nA2 = [nm(f"The semi-perimeter of a triangle with sides ${a}$ cm, ${b}$ cm and ${c}$ cm is (cm):", (a + b + c) // 2, "$s=\\frac{a+b+c}{2}$.") for a, b, c in [(13, 14, 15), (9, 10, 17), (10, 10, 12), (11, 25, 30)]]
nA3 = [nm(f"The area of a circle with circumference ${circ(r)}$ cm (take {PI}) is (cm$^2$):", carea(r), "Find $r$ from $C=2\\pi r$, then use $A=\\pi r^2$.") for r in [14, 21, 35, 42]]
nA4 = [nm(f"A wheel of radius ${r}$ cm (take {PI}) makes one full turn. The distance covered (in cm) is:", circ(r), "Distance in one turn $=$ circumference.") for r in [28, 35, 42, 56]]
nA5 = [nm(f"The area of a rhombus with diagonals ${d1}$ cm and ${d2}$ cm is (cm$^2$):", d1 * d2 // 2, "Area $=\\frac12 d_1d_2$.") for d1, d2 in [(14, 10), (16, 12), (18, 15), (24, 20)]]
nA6 = [nm(f"The area of a cyclic quadrilateral with sides ${a}$ cm, ${b}$ cm, ${c}$ cm and ${d}$ cm is (cm$^2$):", ar, "Use Brahmagupta's formula $\\sqrt{(s-a)(s-b)(s-c)(s-d)}$.") for a, b, c, d, ar in BR_N[:4]]
nA7 = [nm(f"The length of an arc of angle ${th}^\\circ$ in a circle of radius ${r}$ cm (take {PI}) is (cm):", arc(r, th), "Arc $=\\frac{\\theta}{360}\\times2\\pi r$.") for r, th in [(21, 120), (14, 90), (35, 180), (42, 60)]]
nA8 = [nm(f"A square has the same perimeter as a circle of circumference ${circ(r)}$ cm. The side of the square (cm) is:", circ(r) // 4, "Perimeters are equal.") for r in [14, 28, 42]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([QQ(f"Find the area of a triangle with sides ${a}$ cm, ${b}$ cm, ${c}$ cm.", f"$s={sh(hsteps(a, b, c)[0])}$ cm", f"$A=\\sqrt{{s(s-a)(s-b)(s-c)}}={heron(a, b, c)}$ cm$^2$") for a, b, c in [(13, 14, 15), (7, 15, 20), (9, 10, 17), (10, 17, 21)]]
           + [QQ(f"A wheel of radius ${r}$ cm covers a distance of ${circ(r) * n}$ cm. How many revolutions does it make (take {PI})?", f"Circumference $={circ(r)}$ cm", f"Revolutions $=\\frac{{{circ(r) * n}}}{{{circ(r)}}}={n}$") for r, n in [(28, 25), (35, 40), (21, 50), (14, 100)]]
           + [QQ(f"Find the length of an arc of ${th}^\\circ$ in a circle of radius ${r}$ cm (take {PI}).", f"Arc $=\\frac{{{th}}}{{360}}\\times2\\pi r$", f"$={axx(arc(r, th))}$ cm") for r, th in [(21, 120), (14, 90), (35, 180), (28, 45)]])
NCERT_C = ([QQ(f"Find the area of the triangle with sides ${a}$ cm, ${b}$ cm and ${c}$ cm, and the length of the altitude on the side of ${c}$ cm.", f"$s={sh(hsteps(a, b, c)[0])}$ cm", f"$A={heron(a, b, c)}$ cm$^2$", f"$h=\\frac{{2A}}{{{c}}}=\\frac{{{2 * heron(a, b, c)}}}{{{c}}}={axx(Fr(2 * heron(a, b, c), c))}$ cm") for a, b, c in [(13, 14, 15), (10, 17, 21), (9, 10, 17), (7, 15, 20), (4, 13, 15), (10, 10, 12)]]
           + [QQ(f"Find the area of the quadrilateral with sides ${a}$, ${b}$, ${c}$, ${d}$ cm that is inscribed in a circle.", f"$s={sh(Fr(a + b + c + d, 2))}$ cm", f"$A=\\sqrt{{(s-a)(s-b)(s-c)(s-d)}}$", f"$A={ar}$ cm$^2$") for a, b, c, d, ar in BR_N]
           + [QQ(f"Find the area of a parallelogram with base ${b}$ cm and height ${h}$ cm, and the base of a triangle of height ${h * 2}$ cm having the same area.", f"Parallelogram: $A={b}\\times{h}={b * h}$ cm$^2$", f"Triangle: $\\frac12\\times\\text{{base}}\\times{h * 2}={b * h}$", f"$\\text{{base}}={b}$ cm") for b, h in [(14, 9), (18, 7), (22, 5), (16, 12), (25, 6), (20, 8)]])
NCERT_D = ([QQ(f"A circular track has inner radius ${r}$ m and outer radius ${r + w}$ m (take {PI}). Find the area of the track and the cost of levelling it at ₹{c} per m$^2$.", f"Outer area $=\\frac{{22}}{{7}}\\times{r + w}^2={carea(r + w)}$ m$^2$", f"Inner area $={carea(r)}$ m$^2$", f"Track area $={carea(r + w) - carea(r)}$ m$^2$", f"Cost $={carea(r + w) - carea(r)}\\times{c}$", f"$=$ ₹{(carea(r + w) - carea(r)) * c}") for r, w, c in [(14, 7, 5), (21, 7, 4), (28, 14, 3), (35, 7, 6), (14, 14, 2), (42, 7, 5)]]
           + [QQ(f"A rectangular lawn ${l}$ m $\\times$ ${b}$ m has a path ${w}$ m wide all around it, outside the lawn. Find the area of the path.", f"Outer length $={l + 2 * w}$ m, outer breadth $={b + 2 * w}$ m", f"Outer area $={(l + 2 * w) * (b + 2 * w)}$ m$^2$", f"Lawn area $={l * b}$ m$^2$", f"Path area $={(l + 2 * w) * (b + 2 * w) - l * b}$ m$^2$", "Units stated") for l, b, w in [(30, 20, 2), (40, 25, 3), (50, 30, 2), (36, 24, 4), (45, 35, 3), (60, 40, 5)]])

# ------------------------------------------------------------------ MEDIUM
mA1 = [nm(f"The length of the arc of a sector of angle ${th}^\\circ$ in a circle of radius ${r}$ cm (take {PI}) is (cm):", arc(r, th), "Arc $=\\frac{\\theta}{360}\\times2\\pi r$.") for r, th in [(14, 90), (21, 240), (35, 36), (63, 80), (28, 135)]]
mA2 = [nm(f"A triangle has area ${heron(a, b, c)}$ cm$^2$ and one side ${s}$ cm. The altitude on this side (cm) is:", Fr(2 * heron(a, b, c), s), "$h=\\frac{2A}{b}$.") for a, b, c, s in [(13, 14, 15, 14), (10, 17, 21, 21), (25, 25, 14, 14), (9, 10, 17, 9), (15, 15, 24, 24)]]
mA3 = [nm(f"The height of a parallelogram of area ${s * h}$ cm$^2$ and base ${s}$ cm is (cm):", h, "$h=\\frac{A}{b}$.") for s, h in [(17, 12), (23, 8), (19, 14), (26, 9)]]
mA4 = [nm(f"A square has area ${s * s}$ cm$^2$. Its perimeter (cm) is:", 4 * s, "Side $=\\sqrt{A}$.") for s in [13, 18, 24, 32]]
mA5 = [nm(f"The area of a quadrilateral whose diagonal is ${d}$ cm and whose offsets from the diagonal are ${p}$ cm and ${q}$ cm is (cm$^2$):", d * (p + q) // 2, "Area $=\\frac12 d(h_1+h_2)$.") for d, p, q in [(20, 6, 8), (18, 7, 5), (24, 9, 11), (30, 10, 4)]]
mA6 = [nm(f"A rectangle of perimeter ${2 * (l + b)}$ cm has length ${l}$ cm. Its area (cm$^2$) is:", l * b, "Find the breadth first.") for l, b in [(18, 7), (22, 9), (26, 10), (30, 12)]]
mA7 = [nm(f"A circular wire of radius ${r}$ cm (take {PI}) is bent into a square. The side of the square (cm) is:", circ(r) // 4, "Perimeter is unchanged.") for r in [7, 21, 35, 49]]
mA8 = [nm(f"A wheel of diameter ${2 * r}$ cm (take {PI}) makes ${n}$ revolutions. The distance covered (in metres) is:", Fr(circ(r) * n, 100), "Distance $=n\\times$ circumference.") for r, n in [(35, 50), (28, 25), (21, 100), (49, 20)] if (circ(r) * n) % 100 == 0]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"A triangle has sides ${a}$ cm, ${b}$ cm and ${c}$ cm. Find its area and the altitude on the side ${c}$ cm.", f"$s={sh(hsteps(a, b, c)[0])}$, $A={heron(a, b, c)}$ cm$^2$", f"$h=\\frac{{2\\times{heron(a, b, c)}}}{{{c}}}={axx(Fr(2 * heron(a, b, c), c))}$ cm") for a, b, c in [(25, 25, 14), (13, 20, 21), (15, 15, 24), (11, 25, 30)]]
         + [QQ(f"Find the area of a quadrilateral $ABCD$ in which diagonal $AC={d}$ cm and the perpendiculars from $B$ and $D$ to $AC$ are ${p}$ cm and ${q}$ cm.", f"$A=\\frac12\\times{d}\\times{p}+\\frac12\\times{d}\\times{q}$", f"$A={d * (p + q) // 2}$ cm$^2$") for d, p, q in [(26, 9, 7), (30, 8, 12), (22, 10, 6), (28, 5, 9)]]
         + [QQ(f"Find the arc length for ${th}^\\circ$ in a circle of radius ${r}$ cm (take {PI}).", f"Arc $=\\frac{{{th}}}{{360}}\\times2\\times\\frac{{22}}{{7}}\\times{r}$", f"$={axx(arc(r, th))}$ cm") for r, th in [(63, 40), (35, 72), (21, 240), (42, 150)]])
MED_C = ([QQ(f"Find the area of the cyclic quadrilateral with sides ${a}$ cm, ${b}$ cm, ${c}$ cm and ${d}$ cm.", f"$s={sh(Fr(a + b + c + d, 2))}$ cm", f"$s-a={sh(Fr(-a + b + c + d, 2))}$, $s-b={sh(Fr(a - b + c + d, 2))}$, $s-c={sh(Fr(a + b - c + d, 2))}$, $s-d={sh(Fr(a + b + c - d, 2))}$", f"$A={ar}$ cm$^2$") for a, b, c, d, ar in BR_M]
         + [QQ(f"A rectangular sheet ${l}$ cm $\\times$ ${b}$ cm has a semicircle of diameter ${b}$ cm added on one breadth (take {PI}). Find the perimeter and the area of the whole figure.", f"Perimeter $=2\\times{l}+{b}+\\frac12\\pi\\times{b}={2 * l + b}+{axx(Fr(11 * b, 7))}$", f"$={axx(2 * l + b + Fr(11 * b, 7))}$ cm", f"Area $={l * b}+\\frac12\\pi\\left(\\frac{{{b}}}{{2}}\\right)^2$", f"$={axx(l * b + Fr(11, 7) * Fr(b * b, 4))}$ cm$^2$") for l, b in [(30, 14), (25, 28), (40, 14), (35, 28), (21, 14), (50, 28)]]
         + [QQ(f"The sides of a parallelogram are ${a}$ cm and ${b}$ cm and the height on the side ${a}$ cm is ${h}$ cm. Find its area and the height on the side ${b}$ cm.", f"$A={a}\\times{h}={a * h}$ cm$^2$", f"$h'=\\frac{{{a * h}}}{{{b}}}={axx(Fr(a * h, b))}$ cm") for a, b, h in [(15, 12, 8), (18, 9, 5), (20, 16, 12), (24, 18, 9), (30, 25, 10), (14, 21, 12)]])
MED_D = ([QQ(f"A rectangular plot ${l}$ m $\\times$ ${b}$ m has a circular pond of radius ${r}$ m in it (take {PI}). Find the area of the plot left, and the cost of turfing it at ₹{c} per m$^2$.", f"Plot area $={l * b}$ m$^2$", f"Pond area $=\\frac{{22}}{{7}}\\times{r}^2={carea(r)}$ m$^2$", f"Remaining $={l * b - carea(r)}$ m$^2$", f"Cost $={l * b - carea(r)}\\times{c}$", f"$=$ ₹{(l * b - carea(r)) * c}") for l, b, r, c in [(40, 30, 7, 6), (50, 40, 14, 4), (60, 35, 14, 5), (45, 45, 7, 8), (80, 50, 21, 3), (70, 42, 14, 7)]]
          + [QQ(f"A triangular field has sides ${a}$ m, ${b}$ m and ${c}$ m. Find its area, and the cost of ploughing it at ₹{r} per m$^2$.", f"$s={sh(hsteps(a, b, c)[0])}$ m", f"$A=\\sqrt{{s(s-a)(s-b)(s-c)}}={heron(a, b, c)}$ m$^2$", f"Cost $={heron(a, b, c)}\\times{r}$", f"$=$ ₹{heron(a, b, c) * r}", "Units stated") for (a, b, c), r in zip([(13, 13, 10), (15, 15, 24), (25, 25, 14), (17, 25, 26), (12, 17, 25), (20, 21, 29)], [5, 4, 3, 2, 6, 2])])

# ------------------------------------------------------------------ HARD
hA1 = [nm(f"The area of a cyclic quadrilateral with sides ${a}$ cm, ${b}$ cm, ${c}$ cm and ${d}$ cm is (cm$^2$):", ar, "Use Brahmagupta's formula.") for a, b, c, d, ar in BR_H[:4]]
hA2 = [nm(f"A circle of radius ${r}$ cm (take {PI}) is inscribed in a square. The area of the square not covered by the circle is (cm$^2$):", 4 * r * r - carea(r), "Side of square $=2r$.") for r in [7, 14, 21, 35]]
hA3 = [nm(f"Two concentric circles have radii ${r}$ cm and ${r + w}$ cm (take {PI}). The area of the ring between them is (cm$^2$):", carea(r + w) - carea(r), "Difference of the two areas.") for r, w in [(14, 7), (21, 14), (28, 7), (35, 14)]]
hA4 = [nm(f"A wheel makes ${n}$ revolutions to cover ${circ(r) * n // 100}$ m (take {PI}). Its radius (cm) is:", r, "Distance $=n\\times2\\pi r$.") for r, n in [(35, 100), (28, 250), (21, 50), (49, 200)] if (circ(r) * n) % 100 == 0]
hA5 = [nm(f"The area of a rhombus of side ${s}$ cm and one diagonal ${d}$ cm is (cm$^2$):", d * isqrt(4 * s * s - d * d) // 2, "Diagonals bisect at right angles: the other diagonal is $2\\sqrt{s^2-(d/2)^2}$.") for s, d in [(13, 10), (17, 16), (25, 14), (10, 12)] if isqrt(4 * s * s - d * d) ** 2 == 4 * s * s - d * d]
hA6 = [nm(f"A triangle has sides ${a}$ cm, ${b}$ cm, ${c}$ cm. The length of the shortest altitude (cm) is:", Fr(2 * heron(a, b, c), max(a, b, c)), "The shortest altitude stands on the longest side.") for a, b, c in [(10, 17, 21), (15, 15, 24), (13, 20, 21), (15, 20, 25), (10, 10, 12)]]
hA7 = [nm(f"A rope of length ${circ(r)}$ cm (take {PI}) forms a circle. The same rope forms a square. The area of the square (cm$^2$) is:", (circ(r) // 4) ** 2, "Side $=\\frac{\\text{perimeter}}{4}$.") for r in [14, 28, 35, 42]]
hA8 = [M4(t, c, w, "Reason with the area formulas.") for t, c, w in [
    ("If the radius of a circle is doubled, its area becomes:", "four times", ["two times", "three times", "eight times"]),
    ("If the radius of a circle is doubled, its circumference becomes:", "two times", ["four times", "three times", "unchanged"]),
    ("A parallelogram and a triangle on the same base and between the same parallels have areas in the ratio:", "$2:1$", ["$1:1$", "$1:2$", "$3:1$"]),
    ("If the sides of a triangle are doubled, its area becomes:", "four times", ["two times", "three times", "eight times"])]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"Find the area of a cyclic quadrilateral with sides ${a}$, ${b}$, ${c}$ and ${d}$ cm.", f"$s={sh(Fr(a + b + c + d, 2))}$ cm", f"$A=\\sqrt{{(s-a)(s-b)(s-c)(s-d)}}={ar}$ cm$^2$") for a, b, c, d, ar in BR_H[:4]]
          + [QQ(f"A circle of radius ${r}$ cm is inscribed in a square (take {PI}). Find the area of the square left uncovered by the circle.", f"Side of square $={2 * r}$ cm, area $={4 * r * r}$ cm$^2$", f"Circle area $={carea(r)}$ cm$^2$; difference $={4 * r * r - carea(r)}$ cm$^2$") for r in [7, 14, 21, 28]]
          + [QQ(f"The area of a rhombus is ${d1 * d2 // 2}$ cm$^2$ and one diagonal is ${d1}$ cm. Find the other diagonal and the side of the rhombus.", f"$d_2=\\frac{{2\\times{d1 * d2 // 2}}}{{{d1}}}={d2}$ cm", f"Side $=\\sqrt{{{d1 // 2}^2+{d2 // 2}^2}}={axx(Fr(isqrt((d1 // 2) ** 2 + (d2 // 2) ** 2)))}$ cm") for d1, d2 in [(10, 24), (16, 12), (24, 18), (30, 16)]])
HARD_C = ([QQ(f"A rope ${circ(r)}$ cm long is first formed into a circle and then into a square (take {PI}). Find the radius of the circle, the side of the square, and which encloses the larger area.", f"Radius $=\\frac{{{circ(r)}}}{{2\\pi}}={r}$ cm", f"Side $=\\frac{{{circ(r)}}}{{4}}={circ(r) // 4}$ cm", f"Circle area $={carea(r)}$ cm$^2$", f"Square area $={(circ(r) // 4) ** 2}$ cm$^2$", f"The {'circle' if carea(r) > (circ(r) // 4) ** 2 else 'square'} encloses the larger area") for r in [7, 14, 21, 28, 35, 42]]
          + [QQ(f"A running track is made of a rectangle ${l}$ m $\\times$ ${2 * r}$ m with a semicircle (radius ${r}$ m) on each of the two shorter sides (take {PI}). Find the length of the track along its boundary and the area enclosed.", f"Boundary $=2\\times{l}+2\\pi r$", f"$={2 * l}+{circ(r)}={2 * l + circ(r)}$ m", f"Area $={l}\\times{2 * r}+\\pi r^2$", f"$={l * 2 * r}+{carea(r)}={l * 2 * r + carea(r)}$ m$^2$") for l, r in [(60, 14), (80, 7), (70, 21), (90, 14), (100, 28), (50, 35)]]
          + [QQ(f"The sides of a triangle are ${a}$ cm, ${b}$ cm and ${c}$ cm. Find its area and the altitudes on the sides ${a}$ cm and ${b}$ cm.", f"$s={sh(hsteps(a, b, c)[0])}$, $A={heron(a, b, c)}$ cm$^2$", f"Altitude on ${a}$ cm $=\\frac{{{2 * heron(a, b, c)}}}{{{a}}}={axx(Fr(2 * heron(a, b, c), a))}$ cm", f"Altitude on ${b}$ cm $=\\frac{{{2 * heron(a, b, c)}}}{{{b}}}={axx(Fr(2 * heron(a, b, c), b))}$ cm") for a, b, c in [(13, 14, 15), (15, 20, 25), (17, 25, 26), (20, 21, 29), (12, 17, 25), (25, 25, 14)]])
HARD_D = ([QQ(f"In quadrilateral $ABCD$, $AB={a}$ cm, $BC={b}$ cm, $CD={c}$ cm, $DA={d}$ cm and $\\angle ABC=90^\\circ$. Find the area of $ABCD$.", f"$AC=\\sqrt{{{a}^2+{b}^2}}={rt(a * a + b * b)}$ cm", f"Area $\\triangle ABC=\\frac12\\times{a}\\times{b}={a * b // 2}$ cm$^2$", f"$\\triangle ACD$ has sides ${rt(a * a + b * b)}$, ${c}$, ${d}$ cm: $s={sh(Fr(rt(a * a + b * b) + c + d, 2))}$ cm", f"Area $\\triangle ACD={heron(rt(a * a + b * b), c, d)}$ cm$^2$", f"Area $ABCD={a * b // 2 + heron(rt(a * a + b * b), c, d)}$ cm$^2$") for a, b, c, d in [(6, 8, 17, 21), (5, 12, 14, 15), (9, 12, 20, 25), (8, 15, 25, 26), (7, 24, 25, 14), (12, 16, 21, 29)]]
          + [QQ(f"A park is a rectangle ${l}$ m $\\times$ ${b}$ m. A circular flower bed of radius ${r}$ m (take {PI}) is in it, and a path ${w}$ m wide runs round the park inside its boundary. Find the area of the park excluding the path, the area of the grass if the bed is removed from this, and the cost of turfing the grass at ₹{c} per m$^2$.", f"Inner rectangle: ${l - 2 * w}$ m $\\times$ ${b - 2 * w}$ m", f"Area $={(l - 2 * w) * (b - 2 * w)}$ m$^2$", f"Bed area $={carea(r)}$ m$^2$", f"Grass $={(l - 2 * w) * (b - 2 * w) - carea(r)}$ m$^2$", f"Cost $=$ ₹{((l - 2 * w) * (b - 2 * w) - carea(r)) * c}") for l, b, w, r, c in [(60, 40, 5, 7, 3), (80, 50, 5, 14, 2), (70, 50, 5, 14, 4), (90, 60, 10, 21, 2), (100, 60, 10, 28, 3), (50, 40, 5, 7, 5)]]
          + [QQ(f"Two concentric circles have radii ${r}$ cm and ${r + w}$ cm (take {PI}). Find the area of the ring and the difference between the two circumferences.", f"Ring area $=\\pi\\left({r + w}^2-{r}^2\\right)$", f"$={carea(r + w) - carea(r)}$ cm$^2$", f"Difference in circumferences $=2\\pi\\times{w}$", f"$={circ(w) if w % 7 == 0 else axx(Fr(44 * w, 7))}$ cm", "Units stated") for r, w in [(21, 7), (35, 14), (14, 21), (28, 7), (42, 14), (49, 7)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
