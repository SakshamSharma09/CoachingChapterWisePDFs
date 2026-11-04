"""Class 7 Maths Ch 7 - A Tale of Three Intersecting Lines (triangles: inequality, angle sum, exterior angle, isosceles, congruence by SSS/SAS/ASA)."""
from g67 import *
from itertools import combinations

SLUG, NAME, CHNO = "Three_Intersecting_Lines", "A Tale of Three Intersecting Lines", 7

def D(n): return f"${n}^\\circ$"
def dg(n): return f"{n}^\\circ"
def ad(q, c, why="", offs=(10, -10, 20, -20, 30, 5, 15)):
    out = []
    for o in offs:
        x = c + o
        if x != c and x > 0 and x not in out: out.append(x)
    return M4(q, D(c), [D(x) for x in out[:6]], why)
def cnt(q, c, why="", offs=(1, -1, 2, -2, 3, 4)): return nm(q, c, why, offs=offs, pos=True)
def ok3(a, b, c): return a + b > c and b + c > a and a + c > b
def yn(v): return "Yes" if v else "No"
def lst(xs): return "$" + ", ".join(map(str, xs)) + "$"

# ------------------------------------------------ EASY
eA1 = [tm(f"Can a triangle have sides ${a}$ cm, ${b}$ cm and ${c}$ cm?", yn(ok3(a, b, c)), [x for x in ["Yes", "No", "Only if it is right-angled", "Only if it is isosceles"] if x != yn(ok3(a, b, c))][:3], "Two sides together must be longer than the third.")
       for a, b, c in [(3, 4, 5), (2, 3, 6), (5, 5, 9), (4, 4, 8), (7, 8, 10)]]
eA2 = [ad(f"Two angles of a triangle are ${a}^\\circ$ and ${b}^\\circ$. The third angle is:", 180 - a - b, "The three angles add up to $180^\\circ$.") for a, b in [(50, 60), (35, 75), (90, 28), (64, 46), (100, 30)]]
eA3 = [tm(t, c, w, "Recall the definition.") for t, c, w in [
    ("A triangle with all three sides equal is called:", "equilateral", ["isosceles", "scalene", "right-angled"]),
    ("A triangle with exactly two equal sides is called:", "isosceles", ["equilateral", "scalene", "obtuse"]),
    ("A triangle with all sides of different lengths is called:", "scalene", ["isosceles", "equilateral", "right-angled"]),
    ("Each angle of an equilateral triangle measures:", "$60^\\circ$", ["$30^\\circ$", "$45^\\circ$", "$90^\\circ$"]),
    ("A triangle with one angle of $90^\\circ$ is called:", "right-angled", ["acute-angled", "obtuse-angled", "equilateral"])]]
eA4 = [ad(f"In a triangle, the two interior opposite angles are ${a}^\\circ$ and ${b}^\\circ$. The exterior angle is:", a + b, "Exterior angle = sum of the two interior opposite angles.") for a, b in [(40, 55), (62, 38), (70, 45), (28, 81)]]
eA5 = [ad(f"The apex angle of an isosceles triangle is ${a}^\\circ$. Each base angle is:", (180 - a) // 2, "Base angles are equal and the three angles add up to $180^\\circ$.") for a in (40, 80, 100, 120)]
eA6 = [cnt(f"The perimeter of a triangle with sides ${a}$ cm, ${b}$ cm and ${c}$ cm (in cm) is:", a + b + c, "Add the three sides.") for a, b, c in [(5, 7, 9), (6, 6, 11), (10, 12, 15), (8, 8, 8)]]
eA7 = [tm(t, c, w, "Compare the matching parts.") for t, c, w in [
    ("Two triangles with all three pairs of sides equal are congruent by:", "SSS", ["SAS", "ASA", "AAA"]),
    ("Two triangles with two sides and the angle between them equal are congruent by:", "SAS", ["SSS", "ASA", "AAA"]),
    ("Two triangles with two angles and the side between them equal are congruent by:", "ASA", ["SSS", "SAS", "AAA"]),
    ("Congruent triangles have the same:", "shape and size", ["shape only", "size only", "colour"])]]
eA8 = [ad(f"In a right-angled triangle one acute angle is ${a}^\\circ$. The other acute angle is:", 90 - a, "The two acute angles add up to $90^\\circ$.") for a in (25, 38, 52, 67)]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]

def inq(a, b, c):
    s = sorted([a, b, c])
    return QQ(f"Can a triangle be formed with sides ${a}$ cm, ${b}$ cm and ${c}$ cm? Give a reason.", f"Two shorter sides: ${s[0]}+{s[1]}={s[0] + s[1]}$", f"Compare with the longest side ${s[2]}$", f"{'Yes, ' + str(s[0] + s[1]) + ' > ' + str(s[2]) if ok3(a, b, c) else 'No, ' + str(s[0] + s[1]) + ' is not greater than ' + str(s[2])}")
def third(a, b):
    return QQ(f"Two angles of a triangle are ${a}^\\circ$ and ${b}^\\circ$. Find the third angle and name the triangle by its angles.", f"Third $=180^\\circ-({a}^\\circ+{b}^\\circ)$", f"$={180 - a - b}^\\circ$", f"The triangle is {'right-angled' if 90 in (a, b, 180 - a - b) else ('obtuse-angled' if max(a, b, 180 - a - b) > 90 else 'acute-angled')}")
def ext(a, b):
    return QQ(f"In $\\triangle ABC$, $\\angle A={a}^\\circ$ and $\\angle B={b}^\\circ$. Side BC is extended to D. Find the exterior angle $\\angle ACD$.", f"$\\angle C=180^\\circ-{a + b}^\\circ={180 - a - b}^\\circ$", f"$\\angle ACD=180^\\circ-{180 - a - b}^\\circ$", f"$={a + b}^\\circ$ (equal to $\\angle A+\\angle B$)")
EASY_B = [inq(*t) for t in [(6, 8, 10), (3, 5, 9), (7, 7, 12), (4, 6, 10)]] + [third(a, b) for a, b in [(48, 72), (90, 35), (110, 25), (55, 55)]] + [ext(a, b) for a, b in [(45, 60), (30, 85), (72, 38), (55, 50)]]
def ratio(p, q, r):
    u = 180 // (p + q + r)
    return QQ(f"The angles of a triangle are in the ratio ${p}:{q}:{r}$. Find the angles.", f"Total parts $={p + q + r}$; one part $=180^\\circ\\div{p + q + r}={u}^\\circ$", f"Angles ${p * u}^\\circ$, ${q * u}^\\circ$, ${r * u}^\\circ$", f"Check: ${p * u + q * u + r * u}^\\circ$")
def iso(a, k):
    if k == "apex": return QQ(f"The apex angle of an isosceles triangle is ${a}^\\circ$. Find the base angles.", f"Base angles are equal; their sum $=180^\\circ-{a}^\\circ={180 - a}^\\circ$", f"Each base angle $={(180 - a) // 2}^\\circ$", "Check: the three angles add up to $180^\\circ$")
    return QQ(f"A base angle of an isosceles triangle is ${a}^\\circ$. Find the apex angle.", f"Both base angles are ${a}^\\circ$, sum $={2 * a}^\\circ$", f"Apex angle $=180^\\circ-{2 * a}^\\circ$", f"$={180 - 2 * a}^\\circ$")
def extmiss(e, a):
    return QQ(f"An exterior angle of a triangle is ${e}^\\circ$ and one interior opposite angle is ${a}^\\circ$. Find the other interior opposite angle and the adjacent interior angle.", f"Exterior $=$ sum of interior opposite angles", f"Other $={e}^\\circ-{a}^\\circ={e - a}^\\circ$", f"Adjacent interior angle $=180^\\circ-{e}^\\circ={180 - e}^\\circ$")
EASY_C = [ratio(*t) for t in [(1, 2, 3), (2, 3, 4), (1, 1, 2), (3, 4, 5), (2, 3, 5), (1, 3, 5)]] + [iso(30, "apex"), iso(70, "base"), iso(110, "apex"), iso(50, "base"), iso(20, "apex"), iso(35, "base")] + [extmiss(*t) for t in [(120, 45), (110, 60), (135, 80), (100, 35), (150, 70), (125, 52)]]
def tri_d(a, b, c):
    s = sorted([a, b, c]); typ = "equilateral" if a == b == c else ("isosceles" if len({a, b, c}) == 2 else "scalene")
    return QQ(f"A triangle has sides ${a}$ cm, ${b}$ cm and ${c}$ cm. Check that it exists, name it by its sides and find its perimeter.", f"${s[0]}+{s[1]}={s[0] + s[1]}>{s[2]}$, so the triangle exists", f"It is {typ}", f"Perimeter $={a}+{b}+{c}$", f"$={a + b + c}$ cm", "Final statement")
def ang_d(a, b):
    c = 180 - a - b
    return QQ(f"In $\\triangle ABC$, $\\angle A={a}^\\circ$ and $\\angle B={b}^\\circ$. Find $\\angle C$, classify the triangle by its angles and find the exterior angle at C.", f"$\\angle C=180^\\circ-{a}^\\circ-{b}^\\circ={c}^\\circ$", f"Classification: {'right-angled' if 90 in (a, b, c) else ('obtuse-angled' if max(a, b, c) > 90 else 'acute-angled')}", f"Exterior angle at C $=180^\\circ-{c}^\\circ$", f"$={a + b}^\\circ$", f"It equals $\\angle A+\\angle B={a}^\\circ+{b}^\\circ$")
EASY_D = [tri_d(*t) for t in [(5, 5, 8), (6, 8, 10), (9, 9, 9), (7, 9, 12), (10, 10, 15), (4, 7, 9)]] + [ang_d(*t) for t in [(40, 65), (50, 40), (30, 50), (35, 105), (60, 60), (25, 45)]]

# ------------------------------------------------ NCERT
def thirdopts(a, b):
    lo, hi = abs(a - b), a + b
    good = lo + (hi - lo) // 3
    return tm(f"Two sides of a triangle are ${a}$ cm and ${b}$ cm. The third side could be:", f"${good}$ cm", [f"${lo}$ cm", f"${hi}$ cm", f"${hi + 2}$ cm"], "The third side lies between the difference and the sum of the other two.")
nA1 = [thirdopts(*t) for t in [(5, 9), (6, 12), (4, 10), (7, 15)]]
nA2 = [cnt(f"The angles of a triangle are $x^\\circ$, $2x^\\circ$ and ${k}x^\\circ$. The value of $x$ is:", 180 // (3 + k), "Add the angles: $(3+k)x=180$.") for k in (3, 6, 2)]
nA3 = [cnt(f"The exterior angle of a triangle is $(3x+{a})^\\circ$ and the interior opposite angles are ${b}^\\circ$ and ${c}^\\circ$. The value of $x$ is:", (b + c - a) // 3, "Exterior angle = sum of interior opposite angles.") for a, b, c in [(10, 50, 50), (20, 80, 45), (5, 45, 35), (15, 60, 60)]]
nA4 = [tm(t, c, w, "Use the idea of corresponding parts.") for t, c, w in [
    ("If $\\triangle ABC\\cong\\triangle PQR$, then side BC equals:", "QR", ["PQ", "PR", "AB"]),
    ("If $\\triangle ABC\\cong\\triangle PQR$, then $\\angle B$ equals:", "$\\angle Q$", ["$\\angle P$", "$\\angle R$", "$\\angle A$"]),
    ("If $\\triangle ABC\\cong\\triangle PQR$, then side AB equals:", "PQ", ["QR", "PR", "AC"]),
    ("If $\\triangle ABC\\cong\\triangle PQR$, then $\\angle C$ equals:", "$\\angle R$", ["$\\angle P$", "$\\angle Q$", "$\\angle A$"]),
    ("If $\\triangle ABC\\cong\\triangle XYZ$, then side AC equals:", "XZ", ["XY", "YZ", "AB"])]]
nA5 = [tm(t, c, w, "The included angle lies between the two given sides.") for t, c, w in [
    ("In $\\triangle ABC$, the angle included between sides AB and AC is:", "$\\angle A$", ["$\\angle B$", "$\\angle C$", "$\\angle A+\\angle B$"]),
    ("In $\\triangle PQR$, the angle included between sides PQ and QR is:", "$\\angle Q$", ["$\\angle P$", "$\\angle R$", "none of these"]),
    ("In $\\triangle XYZ$, the side included between $\\angle X$ and $\\angle Y$ is:", "XY", ["YZ", "XZ", "none of these"])]]
nA6 = [tm("Which set of angles can be the angles of a triangle?", c, w, "The three angles must add up to $180^\\circ$.") for c, w in [
    ("$50^\\circ, 60^\\circ, 70^\\circ$", ["$50^\\circ, 60^\\circ, 80^\\circ$", "$90^\\circ, 90^\\circ, 10^\\circ$", "$100^\\circ, 50^\\circ, 40^\\circ$"]),
    ("$35^\\circ, 45^\\circ, 100^\\circ$", ["$35^\\circ, 45^\\circ, 90^\\circ$", "$40^\\circ, 40^\\circ, 110^\\circ$", "$60^\\circ, 60^\\circ, 70^\\circ$"]),
    ("$20^\\circ, 80^\\circ, 80^\\circ$", ["$20^\\circ, 80^\\circ, 90^\\circ$", "$30^\\circ, 80^\\circ, 80^\\circ$", "$20^\\circ, 70^\\circ, 80^\\circ$"]),
    ("$15^\\circ, 75^\\circ, 90^\\circ$", ["$15^\\circ, 75^\\circ, 100^\\circ$", "$25^\\circ, 75^\\circ, 90^\\circ$", "$15^\\circ, 65^\\circ, 90^\\circ$"])]]
nA7 = [tm(t, c, w, "Equal angles and equal sides go together in an isosceles triangle.") for t, c, w in [
    ("In $\\triangle ABC$, $AB=AC$. Then equal angles are:", "$\\angle B=\\angle C$", ["$\\angle A=\\angle B$", "$\\angle A=\\angle C$", "all three"]),
    ("In $\\triangle PQR$, $PQ=PR$ and $\\angle Q=50^\\circ$. Then $\\angle R$ is:", "$50^\\circ$", ["$80^\\circ$", "$130^\\circ$", "$40^\\circ$"]),
    ("Each angle of a right-angled isosceles triangle other than the right angle is:", "$45^\\circ$", ["$30^\\circ$", "$60^\\circ$", "$90^\\circ$"]),
    ("In an equilateral triangle the number of pairs of equal sides is:", "3", ["1", "2", "6"])]]
nA8 = [tm(f"Two triangles have angles ${a}^\\circ,{b}^\\circ,{180 - a - b}^\\circ$ each. They are:", "not necessarily congruent", ["always congruent", "never congruent", "congruent by SSS"], "AAA does not guarantee congruence.") for a, b in [(50, 60), (40, 70)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
# add a couple more NCERT MCQs to keep >= 30
nA2 += [cnt(f"The three angles of a triangle are $({a}x)^\\circ$, $({b}x)^\\circ$ and ${c}^\\circ$. If $x={x}$, the sum of the first two is:", (a + b) * x, "Substitute $x$.") for a, b, c, x in [(2, 3, 50, 10), (4, 5, 30, 8)]]

def range_b(a, b):
    lo, hi = abs(a - b), a + b
    return QQ(f"Two sides of a triangle are ${a}$ cm and ${b}$ cm. Find the least and the greatest whole-number length of the third side.", f"Third side $>{a}-{b}$ in absolute value $={lo}$", f"Third side $<{a}+{b}={hi}$", f"Least whole number ${lo + 1}$ cm", f"Greatest whole number ${hi - 1}$ cm")
def angx(a, b, c):
    x = (180 - a + b - c) // 6
    return QQ(f"The angles of a triangle are $(2x+{a})^\\circ$, $(3x-{b})^\\circ$ and $(x+{c})^\\circ$. Find $x$ and the three angles.", f"$6x+{a - b + c}=180$", f"$x={x}$", f"Angles ${2 * x + a}^\\circ$, ${3 * x - b}^\\circ$, ${x + c}^\\circ$")
def extx(a, b, c):
    x = (a + b + c) // 2
    return QQ(f"In $\\triangle ABC$, side BC is extended to D, $\\angle ACD=(5x-{a})^\\circ$, $\\angle A=(2x+{b})^\\circ$ and $\\angle B=(x+{c})^\\circ$. Find $x$ and $\\angle ACD$.", "Exterior angle $=\\angle A+\\angle B$", f"$5x-{a}=3x+{b + c}$, so $2x={a + b + c}$", f"$x={x}$", f"$\\angle ACD={5 * x - a}^\\circ$")
NCERT_B = [range_b(*t) for t in [(6, 10), (4, 13), (8, 11), (5, 5)]] + [angx(*t) for t in [(10, 4, 12), (18, 12, 6), (20, 5, 15), (8, 10, 8)]] + [extx(*t) for t in [(10, 20, 30), (6, 14, 36), (8, 12, 30), (20, 8, 36)]]
def isox(a, b):
    x = (180 - a + 2 * b) // 5
    return QQ(f"In isosceles $\\triangle ABC$ with $AB=AC$, $\\angle A=(x+{a})^\\circ$ and $\\angle B=(2x-{b})^\\circ$. Find $x$ and all three angles.", f"$\\angle B=\\angle C$ (equal sides)", f"$(x+{a})+2(2x-{b})=180$, so $5x={180 - a + 2 * b}$", f"$x={x}$", f"$\\angle A={x + a}^\\circ$, $\\angle B=\\angle C={2 * x - b}^\\circ$")
def sas_c(a, b, t):
    c = a + b - 3
    return QQ(f"In $\\triangle ABC$ and $\\triangle PQR$, $AB=PQ={a}$ cm, $BC=QR={b}$ cm and $\\angle B=\\angle Q={t}^\\circ$. Name the congruence rule, and find $PR$ if $AC={c}$ cm. Find also the perimeter of $\\triangle PQR$.", "Two sides and the included angle are equal, so SAS", f"$\\triangle ABC\\cong\\triangle PQR$, hence $PR=AC={c}$ cm", f"Perimeter of PQR $={a}+{b}+{c}$", f"$={a + b + c}$ cm")
def extratio(e, p, q):
    u = e // (p + q)
    return QQ(f"The exterior angle at C of $\\triangle ABC$ is ${e}^\\circ$ and $\\angle A:\\angle B={p}:{q}$. Find all three angles of the triangle.", f"$\\angle A+\\angle B={e}^\\circ$", f"One part $={e}\\div{p + q}={u}^\\circ$", f"$\\angle A={p * u}^\\circ$, $\\angle B={q * u}^\\circ$", f"$\\angle C=180^\\circ-{e}^\\circ={180 - e}^\\circ$")
NCERT_C = [isox(*t) for t in [(10, 5), (20, 15), (30, 25), (15, 5), (25, 20), (5, 20)]] + [sas_c(*t) for t in [(5, 7, 50), (6, 9, 40), (8, 10, 65), (4, 12, 70), (9, 11, 55), (7, 8, 80)]] + [extratio(*t) for t in [(120, 1, 3), (140, 2, 5), (130, 6, 7), (150, 2, 3), (110, 4, 7), (100, 1, 4)]]
def angs_d(a, b, c):
    x = (180 - a + b - c) // 4
    A, B, C = x + a, x - b, 2 * x + c
    return QQ(f"The angles of a triangle are $(x+{a})^\\circ$, $(x-{b})^\\circ$ and $(2x+{c})^\\circ$. Find $x$, the three angles and classify the triangle. Also find the three exterior angles (one at each vertex).", f"$4x+{a - b + c}=180$, so $x={x}$", f"Angles ${A}^\\circ$, ${B}^\\circ$, ${C}^\\circ$", f"Classification: {'right-angled' if 90 in (A, B, C) else ('obtuse-angled' if max(A, B, C) > 90 else 'acute-angled')}", f"Exterior angles ${180 - A}^\\circ$, ${180 - B}^\\circ$, ${180 - C}^\\circ$", f"Their sum $={540 - 180}^\\circ=360^\\circ$")
def sides_d(a, b):
    lo, hi = abs(a - b), a + b; n = hi - lo - 1
    return QQ(f"Two sides of a triangle are ${a}$ cm and ${b}$ cm. (i) Between which two lengths does the third side lie? (ii) How many whole-number lengths are possible? (iii) Find the smallest and the largest possible perimeter in whole centimetres.", f"(i) Between ${lo}$ cm and ${hi}$ cm", f"(ii) Whole numbers ${lo + 1}$ to ${hi - 1}$: ${n}$ values", f"(iii) Smallest third side ${lo + 1}$: perimeter ${a + b + lo + 1}$ cm", f"Largest third side ${hi - 1}$: perimeter ${a + b + hi - 1}$ cm", "State the answers with units")
NCERT_D = [angs_d(*t) for t in [(10, 10, 20), (20, 10, 10), (30, 10, 20), (40, 8, 12), (35, 5, 6), (22, 12, 6)]] + [sides_d(*t) for t in [(7, 12), (5, 9), (8, 8), (6, 15), (10, 13), (9, 4)]]

# ------------------------------------------------ MEDIUM
mA1 = [ad(f"The angles of a triangle are in the ratio ${p}:{q}:{r}$. The largest angle is:", max(p, q, r) * (180 // (p + q + r)), "Share $180^\\circ$ in the ratio.") for p, q, r in [(2, 3, 4), (1, 4, 5), (3, 4, 5), (2, 5, 11)]]
mA2 = [ad(f"A base angle of an isosceles triangle is ${b}^\\circ$. The exterior angle at the apex is:", 2 * b, "Exterior angle equals the sum of the two base angles.") for b in (35, 50, 62, 70)]
mA3 = [ad(f"The exterior angle at B of $\\triangle ABC$ is ${e}^\\circ$ and $\\angle A={a}^\\circ$. Then $\\angle C$ is:", e - a, "Exterior angle $=\\angle A+\\angle C$.") for e, a in [(120, 45), (135, 70), (105, 30), (150, 85)]]
mA4 = [cnt(f"Two sides of a triangle are ${a}$ cm and ${b}$ cm. The number of possible whole-number lengths of the third side is:", 2 * min(a, b) - 1, "Count whole numbers strictly between the difference and the sum.", offs=(1, -1, 2, 3, -2)) for a, b in [(4, 9), (6, 7), (3, 11), (5, 5)]]
mA5 = [ad(f"The angles of a triangle are $(60-d)^\\circ$, $60^\\circ$ and $(60+d)^\\circ$. When $d={d}$, the largest angle is:", 60 + d, "Substitute $d$.") for d in (10, 20, 25, 15)]
mA6 = [tm(t, c, w, "Check which parts are given and where they sit.") for t, c, w in [
    ("In two triangles, $AB=PQ$, $BC=QR$, $\\angle B=\\angle Q$. They are congruent by:", "SAS", ["SSS", "ASA", "not congruent"]),
    ("In two triangles, $\\angle A=\\angle P$, $\\angle B=\\angle Q$, $AB=PQ$. They are congruent by:", "ASA", ["SAS", "SSS", "AAA"]),
    ("In two triangles, $AB=PQ$, $BC=QR$, $CA=RP$. They are congruent by:", "SSS", ["SAS", "ASA", "AAA"]),
    ("Two triangles have all three angles equal. They are:", "not necessarily congruent", ["congruent by ASA", "congruent by SAS", "congruent by SSS"])]]
mA7 = [cnt(f"An isosceles triangle has equal sides ${s}$ cm and base ${b}$ cm. Its perimeter (cm) is:", 2 * s + b, "Add the three sides.") for s, b in [(9, 6), (12, 10), (15, 8)]]
mA8 = [ad(f"In a right-angled triangle one acute angle is ${a}^\\circ$. The exterior angle at the other acute vertex is:", 90 + a, "The other acute angle is $90^\\circ-a$; the exterior angle is supplementary to it.") for a in (20, 35, 40, 55)]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]

def perim(P, s):
    b1 = P - 2 * s; e2 = Fr(P - s, 2)
    v1 = b1 > 0 and ok3(s, s, b1); v2 = ok3(s, e2, e2)
    r = []
    if v1: r.append(f"${s}, {s}, {b1}$")
    if v2: r.append(f"${float(e2):g}, {float(e2):g}, {s}$")
    c1 = "valid" if v1 else (f"not valid, since ${s}+{s}={2 * s}$ is not greater than ${b1}$" if b1 > 0 else "not valid")
    return QQ(f"An isosceles triangle has perimeter ${P}$ cm and one side ${s}$ cm. Find its other sides (check which case is possible).", f"Case 1: ${s}$ is an equal side, base $={P}-2\\times{s}={b1}$; {c1}", f"Case 2: ${s}$ is the base, equal sides $=({P}-{s})\\div2={float(e2):g}$; {'valid' if v2 else 'not valid'}", "Sides (cm): " + " or ".join(r))
def extx_m(a, b, c):
    x = (a + b + c) // 2
    return QQ(f"The exterior angle of a triangle is $(4x-{a})^\\circ$ and the interior opposite angles are $(x+{b})^\\circ$ and $(2x+{c})^\\circ$. Find $x$ and the exterior angle.", "Exterior $=$ sum of the interior opposite angles", f"$4x-{a}=3x+{b + c}$ so $x={a + b + c}$", f"Exterior angle $={4 * (a + b + c) - a}^\\circ$")
def isoang(e):
    return QQ(f"In isosceles $\\triangle ABC$, $AB=AC$ and the exterior angle at B is ${e}^\\circ$. Find all three angles.", f"$\\angle B=180^\\circ-{e}^\\circ={180 - e}^\\circ$", f"$\\angle C=\\angle B={180 - e}^\\circ$ (equal sides)", f"$\\angle A=180^\\circ-2({180 - e}^\\circ)={2 * e - 180}^\\circ$")
MED_B = [perim(*t) for t in [(26, 6), (22, 10), (36, 8), (18, 4)]] + [extx_m(*t) for t in [(10, 12, 18), (6, 14, 20), (8, 20, 30), (4, 16, 18)]] + [isoang(e) for e in (110, 130, 120, 140)]
def ratio_m(p, q, r, k):
    u = 180 // (p + q + r); A, B, C = p * u, q * u, r * u
    return QQ(f"The angles of $\\triangle ABC$ are in the ratio ${p}:{q}:{r}$. Find the angles and the exterior angle at the vertex of the {'largest' if k else 'smallest'} angle.", f"One part $=180^\\circ\\div{p + q + r}={u}^\\circ$", f"Angles ${A}^\\circ$, ${B}^\\circ$, ${C}^\\circ$", f"Exterior angle $=180^\\circ-{max(A, B, C) if k else min(A, B, C)}^\\circ$", f"$={180 - (max(A, B, C) if k else min(A, B, C))}^\\circ$")
def isox_m(a, b):
    x = (a + b) // 2
    return QQ(f"In $\\triangle PQR$, $PQ=PR$, $\\angle Q=(3x-{a})^\\circ$ and $\\angle R=(x+{b})^\\circ$. Find $x$, all three angles and the exterior angle at P.", "Equal sides, so $\\angle Q=\\angle R$", f"$3x-{a}=x+{b}$ so $x={x}$", f"$\\angle Q=\\angle R={x + b}^\\circ$", f"$\\angle P=180^\\circ-{2 * (x + b)}^\\circ={180 - 2 * (x + b)}^\\circ$", f"Exterior angle at P $={2 * (x + b)}^\\circ$")
def cong_x(p, q, r, s, c, d):
    x = (q - s) // (r - p)
    AB, DE = p * x + q, r * x + s
    return QQ(f"$\\triangle ABC\\cong\\triangle DEF$ with $AB=({p}x+{q})$ cm, $DE=({r}x+{s})$ cm, $BC={c}$ cm and $AC={d}$ cm. Find $x$, the length $DE$ and the perimeter of $\\triangle DEF$.", "Corresponding sides of congruent triangles are equal, so $AB=DE$", f"${p}x-{r}x={s}-{q}$, so ${p - r}x={s - q}$ and $x={x}$", f"$DE=AB={AB}$ cm", f"Perimeter $=AB+BC+AC={AB}+{c}+{d}$", f"$={AB + c + d}$ cm")
MED_C = [ratio_m(2, 3, 4, 1), ratio_m(1, 2, 3, 0), ratio_m(3, 4, 5, 1), ratio_m(1, 4, 7, 0), ratio_m(2, 5, 11, 1), ratio_m(1, 1, 2, 0)] + [isox_m(a, b) for a, b in [(10, 6), (20, 10), (6, 12), (14, 6), (12, 8), (18, 10)]] + [cong_x(*t) for t in [(5, 3, 2, 18, 7, 9), (4, 1, 2, 23, 6, 8), (7, 2, 3, 30, 5, 11), (6, 4, 2, 24, 8, 10), (8, 5, 3, 30, 9, 12), (9, 3, 4, 33, 10, 7)]]
def sticks(ls):
    rows = []; good = 0
    for t in combinations(ls, 3):
        s = sorted(t); v = s[0] + s[1] > s[2]; good += v
        rows.append(f"${t[0]},{t[1]},{t[2]}$: {s[0]}+{s[1]}={s[0] + s[1]} {'>' if v else 'not >'} {s[2]}, {'triangle' if v else 'no triangle'}")
    return QQ(f"Four sticks of lengths ${ls[0]}$ cm, ${ls[1]}$ cm, ${ls[2]}$ cm and ${ls[3]}$ cm are available. Choosing any three, how many different triangles can be made? Test each choice.", "; ".join(rows), f"Number of triangles $={good}$")
def isoalg(p, q, c):
    x = p + q; e = 2 * x + p; b = x + c
    return QQ(f"The equal sides of an isosceles triangle are $(2x+{p})$ cm and $(3x-{q})$ cm and its base is $(x+{c})$ cm. Find $x$, the three sides and the perimeter. Check that the triangle exists.", f"Equal sides: $2x+{p}=3x-{q}$, so $x={x}$", f"Each equal side $={e}$ cm", f"Base $={x}+{c}={b}$ cm", f"Perimeter $={e}+{e}+{b}={2 * e + b}$ cm", f"Existence: ${e}+{b}={e + b}>{e}$ and ${e}+{e}={2 * e}>{b}$")
MED_D = [isoalg(*t) for t in [(1, 4, 3), (2, 3, 6), (3, 5, 2), (4, 2, 7), (1, 9, 5), (5, 3, 4)]] + [sticks(t) for t in [(2, 4, 6, 7), (3, 5, 8, 9), (4, 5, 9, 10), (2, 3, 7, 8), (5, 6, 11, 12), (3, 4, 7, 12)]]

# ------------------------------------------------ HARD
def count_tri(P): return sum(1 for a in range(1, P) for b in range(a, P) for c in range(b, P) if a + b + c == P and a + b > c)
hA1 = [cnt(f"The number of triangles with whole-number sides (in cm) and perimeter ${P}$ cm is:", count_tri(P), "List the triples $a\\le b\\le c$ with $a+b>c$.", offs=(1, -1, 2, -2, 3)) for P in (9, 12, 14, 15)]
hA2 = [ad(f"The exterior angle at the base of an isosceles triangle is ${e}^\\circ$. The apex angle is:", 180 - 2 * (180 - e), "Base angle $=180^\\circ-e$; apex $=180^\\circ-2\\times$ base.") for e in (110, 125, 140, 150)]
hA3 = [tm(t, c, w, "Reason with the angle sum and exterior angle property.") for t, c, w in [
    ("In $\\triangle ABC$, $\\angle A=\\angle B+\\angle C$. Then $\\angle A$ is:", "$90^\\circ$", ["$60^\\circ$", "$45^\\circ$", "$120^\\circ$"]),
    ("The sum of the three exterior angles of a triangle (one at each vertex) is:", "$360^\\circ$", ["$180^\\circ$", "$270^\\circ$", "$540^\\circ$"]),
    ("An exterior angle of a triangle is always:", "greater than each interior opposite angle", ["smaller than each interior opposite angle", "equal to the adjacent interior angle", "equal to $90^\\circ$"]),
    ("A triangle cannot have:", "two right angles", ["two acute angles", "one obtuse angle", "three acute angles"])]]
def tri_angles(a, b, c, d, x):
    e = (a + b + d) * x + c - 180
    return [a * x, b * x + c, d * x - e], e
hA4 = [ad(f"The angles of a triangle are $({a}x)^\\circ$, $({b}x+{c})^\\circ$ and $({d}x-{tri_angles(a, b, c, d, x)[1]})^\\circ$. The largest angle is:", max(tri_angles(a, b, c, d, x)[0]), "Find $x$ from the angle sum, then compare the angles.", offs=(10, -10, 20, 5, -5))
       for a, b, c, d, x in [(2, 3, 5, 4, 25), (3, 2, 10, 4, 20), (2, 4, 8, 3, 22), (5, 2, 4, 4, 20)]]
hA5 = [tm(f"Sides ${a}$ cm, ${b}$ cm and ${c}$ cm are given. Which statement is true?", ("a triangle can be formed" if ok3(a, b, c) else "no triangle can be formed"), [x for x in ["a triangle can be formed", "no triangle can be formed", "only a right triangle is possible", "only an equilateral triangle is possible"] if x != ("a triangle can be formed" if ok3(a, b, c) else "no triangle can be formed")][:3], "Check the sum of the two shorter sides.") for a, b, c in [(11, 6, 5), (13, 6, 8), (15, 9, 5), (14, 7, 9)]]
hA6 = [cnt(f"In an isosceles triangle with perimeter ${P}$ cm the equal sides are ${s}$ cm each. The base (cm) is:", P - 2 * s, "Base $=P-2s$.") for P, s in [(34, 12), (50, 18), (41, 15), (29, 11)]]
hA7 = [ad(f"The two acute angles of a right triangle are in the ratio ${p}:{q}$. The smaller acute angle is:", 90 * min(p, q) // (p + q), "They add up to $90^\\circ$.") for p, q in [(1, 2), (2, 3), (4, 5), (1, 5)]]
hA7 += [tm("Two triangles have two equal sides and an equal angle that is not between them. They:", "need not be congruent", ["are always congruent", "are congruent by SAS", "are congruent by ASA"], "SSA is not a congruence rule.")]
hA8 = [cnt(f"The number of isosceles triangles with whole-number sides and perimeter ${P}$ cm (equilateral included) is:", sum(1 for a in range(1, P) if 0 < P - 2 * a < 2 * a), "List $a,a,b$ with $b=P-2a$ and $b<2a$.", offs=(1, -1, 2, -2, 3)) for P in (14, 15, 18)]
hA8 += [ad("The angle between a side of an equilateral triangle and the extension of an adjacent side is:", 120, "Exterior angle $=180^\\circ-60^\\circ$.")]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]

def cong_q(i, a, b, t, t2):
    cases = [
        (f"$AB=PQ={a}$ cm, $BC=QR={b}$ cm and $\\angle A=\\angle P={t}^\\circ$", False, "SSA: the equal angle is not between the equal sides, so this is not a congruence rule"),
        (f"$\\angle A=\\angle P={t}^\\circ$, $\\angle B=\\angle Q={t2}^\\circ$ and $\\angle C=\\angle R={180 - t - t2}^\\circ$", False, "AAA gives the same shape but not necessarily the same size"),
        (f"$AB=PQ={a}$ cm, $\\angle B=\\angle Q={t}^\\circ$ and $BC=QR={b}$ cm", True, "SAS: the equal angle lies between the two equal sides"),
        (f"$\\angle B=\\angle Q={t}^\\circ$, $BC=QR={b}$ cm and $\\angle C=\\angle R={t2}^\\circ$", True, "ASA: two angles and the side between them are equal"),
    ]
    txt, ok, why = cases[i]
    return QQ(f"In $\\triangle ABC$ and $\\triangle PQR$ it is known that {txt}. Are the triangles necessarily congruent? Give the rule or the reason.", "Check where the equal parts lie in each triangle", f"{'Yes' if ok else 'No'}: {why}", "Matching parts of congruent triangles are equal" if ok else "A different triangle with the same given parts can be drawn")
def isoext(e):
    return QQ(f"In isosceles $\\triangle ABC$ with $AB=AC$, side BC is extended to D and $\\angle ACD={e}^\\circ$. Find $\\angle A$ and $\\angle B$.", f"$\\angle ACB=180^\\circ-{e}^\\circ={180 - e}^\\circ$", f"$\\angle B=\\angle ACB={180 - e}^\\circ$ (equal sides)", f"$\\angle A=180^\\circ-2\\times{180 - e}^\\circ={2 * e - 180}^\\circ$")
def isocount(P):
    L = [(a, a, P - 2 * a) for a in range(1, P) if 0 < P - 2 * a < 2 * a]
    return QQ(f"List all isosceles triangles with whole-number sides and perimeter ${P}$ cm (equal sides $a$, base $b$). How many are there?", f"$b=P-2a={P}-2a$ and $b<2a$ so $a>{P / 4:g}$", f"Also $b>0$ so $a<{P / 2:g}$", "; ".join(f"${a},{a},{b}$" for a, _, b in L), f"Number of triangles $={len(L)}$")
HARD_B = [cong_q(i, *p) for i, p in zip((0, 1, 2, 3), [(5, 6, 50, 60), (4, 7, 40, 65), (6, 8, 55, 70), (5, 9, 45, 80)])] + [isoext(e) for e in (115, 130, 145, 160)] + [isocount(P) for P in (20, 17, 24, 22)]
def ext2(x, a, p, q, r):
    eB = p * x + q; eC = 180 + a - eB; s = eC - r * x
    return QQ(f"In $\\triangle ABC$, $\\angle A={a}^\\circ$. The exterior angles at B and C are $({p}x+{q})^\\circ$ and $({r}x{'+' if s >= 0 else '-'}{abs(s)})^\\circ$. Find $x$ and the angles B and C.", "Exterior angles at B and C add up to $180^\\circ+\\angle A$ because $(180-B)+(180-C)=360-(180-A)$", f"${p}x+{q}+{r}x{'+' if s >= 0 else '-'}{abs(s)}={180 + a}$", f"$x={x}$", f"Exterior angles ${eB}^\\circ$ and ${eC}^\\circ$", f"$\\angle B={180 - eB}^\\circ$, $\\angle C={180 - eC}^\\circ$")
def isoperim(P, k):
    e = (P + k) // 3; b = e - k
    return QQ(f"The perimeter of an isosceles triangle is ${P}$ cm. Each equal side is ${k}$ cm longer than the base. Find the sides and show that such a triangle exists.", f"Base $b$, equal sides $b+{k}$", f"$b+2(b+{k})={P}$, so $3b={P - 2 * k}$ and $b={(P - 2 * k) // 3}$", f"Sides ${e}, {e}, {b}$ cm", f"${b}+{e}={b + e}>{e}$, so the triangle exists")
def multiples(a, b, n):
    lo, hi = abs(a - b), a + b
    cs = [c for c in range(lo + 1, hi) if c % n == 0]
    return QQ(f"Two sides of a triangle are ${a}$ cm and ${b}$ cm. The third side is a whole number of cm divisible by ${n}$. List all possible lengths and the largest perimeter.", f"Third side between ${lo}$ and ${hi}$", f"Multiples of ${n}$ in this range: {lst(cs)}", f"Largest third side ${cs[-1]}$ cm", f"Largest perimeter $={a}+{b}+{cs[-1]}={a + b + cs[-1]}$ cm")
HARD_C = [ext2(*t) for t in [(10, 50, 4, 60, 3), (12, 40, 5, 50, 4), (15, 70, 2, 75, 5), (8, 60, 6, 62, 2), (20, 30, 3, 50, 2), (6, 80, 7, 58, 5)]] + [isoperim(*t) for t in [(40, 2), (45, 3), (38, 1), (47, 4), (52, 5), (34, 2)]] + [multiples(*t) for t in [(8, 21, 5), (6, 19, 4), (10, 27, 6), (9, 22, 3), (7, 25, 5), (12, 31, 7)]]
def extratio3(p, q, r):
    u = 360 // (p + q + r); e = [p * u, q * u, r * u]; i = [180 - x for x in e]
    return QQ(f"The exterior angles of a triangle (one at each vertex) are in the ratio ${p}:{q}:{r}$. Find the three exterior angles, the three interior angles and classify the triangle.", f"Exterior angles add up to $360^\\circ$; one part $=360^\\circ\\div{p + q + r}={u}^\\circ$", f"Exterior angles ${e[0]}^\\circ$, ${e[1]}^\\circ$, ${e[2]}^\\circ$", f"Interior angles ${i[0]}^\\circ$, ${i[1]}^\\circ$, ${i[2]}^\\circ$", f"Check: ${sum(i)}^\\circ$", f"The triangle is {'right-angled' if 90 in i else ('obtuse-angled' if max(i) > 90 else 'acute-angled')}")
def cong_xy(a, b, c, d, e):
    x = (a + b) // 2; y = c + d
    return QQ(f"$\\triangle ABC\\cong\\triangle DEF$ with $A\\leftrightarrow D$, $B\\leftrightarrow E$, $C\\leftrightarrow F$. Given $\\angle A=(3x+{a})^\\circ$, $\\angle D=(5x-{b})^\\circ$, $AB=(2y+{c})$ cm and $DE=(3y-{d})$ cm. Find $x$, $y$, $\\angle A$ and $AB$. If $\\angle B={e}^\\circ$, find $\\angle F$.", "Corresponding parts of congruent triangles are equal", f"$3x+{a}=5x-{b}$, so $2x={a + b}$ and $x={x}$", f"$\\angle A={3 * x + a}^\\circ$", f"$2y+{c}=3y-{d}$, so $y={y}$ and $AB={2 * y + c}$ cm", f"$\\angle C=180^\\circ-{3 * x + a}^\\circ-{e}^\\circ={180 - 3 * x - a - e}^\\circ=\\angle F$")
HARD_D = [extratio3(*t) for t in [(3, 4, 5), (4, 5, 6), (5, 6, 7), (2, 3, 4), (7, 8, 9), (3, 5, 7)]] + [cong_xy(*t) for t in [(10, 20, 4, 6, 40), (8, 14, 5, 3, 30), (12, 18, 2, 7, 35), (6, 24, 8, 1, 45), (16, 10, 3, 9, 25), (14, 22, 6, 4, 50)]]

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
