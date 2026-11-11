"""Class 7 Maths Ch 5 - Parallel and Intersecting Lines (complementary and supplementary angles, linear pair, vertically opposite angles, transversal angle pairs, test for parallel lines)."""
from g67 import *

SLUG, NAME, CHNO = "Parallel_and_Intersecting_Lines", "Parallel and Intersecting Lines", 5

def D(n): return f"${n}^\\circ$"
def kind(a): return "acute" if a < 90 else "right" if a == 90 else "obtuse" if a < 180 else "straight" if a == 180 else "reflex"
def dg(q, c, why="", offs=(10, -10, 20, -20, 30, 5, 15), extra=()):
    """MCQ whose options are angles in degrees (extra = hand-picked typical mistakes tried first)."""
    out = []
    for x in list(extra) + [c + o for o in offs]:
        if x != c and x > 0 and x not in out: out.append(x)
    return M4(q, D(c), [D(x) for x in out[:6]], why)
def split(total, *parts):
    """Share `total` degrees in the ratio of `parts`; the parts must divide it exactly."""
    s = sum(parts); assert total % s == 0
    return [total // s * p for p in parts]
def seq(vals): return ", ".join(f"${v}^\\circ$" for v in vals)
def ratio(parts): return ":".join(map(str, parts))

# ---------------------------------------------------------------- EASY
eA1 = [dg(f"The complement of ${a}^\\circ$ is:", 90 - a, "Complementary angles add up to $90^\\circ$.", extra=(180 - a, a, 90 + a)) for a in (30, 65, 48, 72, 15)]
eA2 = [dg(f"The supplement of ${a}^\\circ$ is:", 180 - a, "Supplementary angles add up to $180^\\circ$.", extra=(90 - a, a, 360 - a)) for a in (50, 115, 78, 140, 95)]
eA3 = [dg(f"Two lines intersect and one of the angles formed is ${a}^\\circ$. The angle vertically opposite to it is:", a, "Vertically opposite angles are equal.") for a in (40, 75, 110, 135)]
eA4 = [dg(f"Two angles form a linear pair and one of them is ${a}^\\circ$. The other is:", 180 - a, "A linear pair adds up to $180^\\circ$.") for a in (60, 100, 125, 35)]
eA5 = [tm(q, c, w, "Recall the definition.") for q, c, w in [
    ("Lines in a plane that never meet are called:", "parallel lines", ["intersecting lines", "perpendicular lines", "transversals"]),
    ("A line that cuts two or more lines at different points is called a:", "transversal", ["parallel line", "bisector", "median"]),
    ("Two angles whose sum is $90^\\circ$ are called:", "complementary angles", ["supplementary angles", "vertically opposite angles", "alternate angles"]),
    ("Two lines that meet at $90^\\circ$ are called:", "perpendicular lines", ["parallel lines", "transversal lines", "bisecting lines"])]]
eA6 = [dg(f"A transversal cuts two parallel lines. One angle is ${a}^\\circ$. The corresponding angle is:", a, "Corresponding angles are equal when the lines are parallel.") for a in (55, 82, 118, 67)]
eA7 = [dg(f"A transversal cuts two parallel lines. One interior angle is ${a}^\\circ$. Its alternate interior angle is:", a, "Alternate interior angles are equal when the lines are parallel.") for a in (48, 73, 99, 125)]
eA8 = [dg(f"A transversal cuts two parallel lines. Two interior angles on the same side are ${a}^\\circ$ and $x^\\circ$. Then $x=$", 180 - a, "Interior angles on the same side add up to $180^\\circ$.") for a in (62, 85, 104, 127)]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Find the complement of ${a}^\\circ$ and the supplement of ${b}^\\circ$.", f"Complement $=90^\\circ-{a}^\\circ={90 - a}^\\circ$", f"Supplement $=180^\\circ-{b}^\\circ={180 - b}^\\circ$") for a, b in [(35, 110), (62, 75), (18, 140), (47, 98)]]
          + [QQ(f"Two lines intersect and one of the four angles is ${a}^\\circ$. Find the other three angles.", f"Vertically opposite angle $={a}^\\circ$", f"The other two angles form a linear pair with it: $180^\\circ-{a}^\\circ={180 - a}^\\circ$ each") for a in (65, 110, 40, 125)]
          + [QQ(f"A transversal cuts two parallel lines and one of the angles formed is ${a}^\\circ$. Find the angle vertically opposite to it and the angle forming a linear pair with it.", f"Vertically opposite angle $={a}^\\circ$", f"Linear pair: $180^\\circ-{a}^\\circ={180 - a}^\\circ$") for a in (70, 105, 58, 132)])
EASY_C = ([QQ(f"Two angles of a linear pair are in the ratio ${a}:{b}$. Find them.", f"Sum $=180^\\circ$ and the number of parts $={a + b}$", f"One part $={180 // (a + b)}^\\circ$", f"The angles are ${a * 180 // (a + b)}^\\circ$ and ${b * 180 // (a + b)}^\\circ$") for a, b in [(1, 2), (1, 5), (2, 3), (4, 5), (1, 3), (2, 7)]]
          + [QQ(f"The angles $x^\\circ$ and ${a}^\\circ$ are supplementary. Find $x$ and say whether the angle $x^\\circ$ is acute, right or obtuse.", f"$x=180-{a}={180 - a}$", f"The angle ${180 - a}^\\circ$ is {kind(180 - a)}") for a in (110, 135, 150, 95, 70, 160)]
          + [QQ(f"A transversal cuts two parallel lines. An interior angle is ${a}^\\circ$. Find (i) its alternate interior angle and (ii) the interior angle on the same side as it.", f"(i) Alternate interior angles are equal: ${a}^\\circ$", f"(ii) Interior angles on the same side add up to $180^\\circ$: ${180 - a}^\\circ$") for a in (52, 66, 74, 88, 103, 117)])
def cross(a):
    return QQ(f"Two lines intersect at O and one angle is ${a}^\\circ$. Find the other three angles and show that the four angles add up to $360^\\circ$.", f"Vertically opposite angle $={a}^\\circ$", f"The other two angles are ${180 - a}^\\circ$ each (linear pair)", f"Sum $={a}+{a}+{180 - a}+{180 - a}=360$", "The four angles around the point add up to $360^\\circ$")
def comp_k(k):
    x = 90 * k // (k + 1)
    return QQ(f"An angle is ${k}$ times its complement. Find the angle and its complement.", f"Let the complement be $y$; the angle is ${k}y$ and ${k}y+y=90$", f"$y={90 // (k + 1)}$", f"The angle is ${x}^\\circ$ and its complement is ${90 - x}^\\circ$")
EASY_D = [cross(a) for a in (35, 50, 65, 80, 115, 130)] + [comp_k(k) for k in (2, 4, 5, 8, 14, 17)]

# ---------------------------------------------------------------- NCERT
nA1 = [dg(f"If $x^\\circ$ and ${a}^\\circ$ are complementary, then $x=$", 90 - a, "Their sum is $90^\\circ$.") for a in (24, 37, 51, 68, 83)]
nA2 = [dg(f"In a linear pair one angle is {k} times the other. The smaller angle is:", 180 // (k + 1), f"The angles add up to $180^\\circ$ in {k + 1} equal parts.") for k in (2, 4, 5, 8)]
nA3 = [dg(f"Two parallel lines are cut by a transversal. An interior angle is ${a}^\\circ$. The interior angle on the same side is:", 180 - a, "Interior angles on the same side are supplementary.") for a in (65, 80, 112, 135)]
nA4 = [tm(q, c, w, "Use the tests for parallel lines.") for q, c, w in [
    ("If a transversal makes equal corresponding angles with two lines, the lines are:", "parallel", ["perpendicular", "intersecting", "coincident"]),
    ("If a transversal makes interior angles on the same side that add up to $180^\\circ$, the lines are:", "parallel", ["perpendicular", "intersecting", "unequal"]),
    ("If a transversal makes alternate interior angles that are not equal, the lines are:", "not parallel", ["parallel", "perpendicular", "coincident"]),
    ("The number of angles formed when a transversal cuts two lines is:", "8", ["4", "6", "12"])]]
nA5 = [dg(f"Angles $A$ and $B$ are vertically opposite and $A={a}^\\circ$. Then $B=$", a, "Vertically opposite angles are equal.") for a in (28, 64, 97, 143)]
nA6 = [tm(f"An angle of ${a}^\\circ$ is:", kind(a), [w for w in ("acute", "right", "obtuse", "reflex") if w != kind(a)][:3], "Classify by the measure: acute $<90^\\circ$, right $=90^\\circ$, obtuse between $90^\\circ$ and $180^\\circ$, reflex above $180^\\circ$.") for a in (35, 90, 125, 210, 89)]
nA7 = [dg(f"Three of the four angles around a point are ${a}^\\circ$, ${b}^\\circ$ and ${c}^\\circ$. The fourth angle is:", 360 - a - b - c, "The angles around a point add up to $360^\\circ$.") for a, b, c in [(100, 90, 80), (120, 70, 60), (95, 85, 110), (130, 65, 75)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Two supplementary angles are such that one is ${k}$ times the other. Find them.", f"The angles are $y$ and ${k}y$, so ${k + 1}y=180$", f"$y={180 // (k + 1)}$", f"The angles are ${180 // (k + 1)}^\\circ$ and ${k * 180 // (k + 1)}^\\circ$") for k in (2, 3, 4, 5)]
           + [QQ(f"A transversal cuts two lines and makes corresponding angles of ${a}^\\circ$ and ${b}^\\circ$. Are the lines parallel? Give a reason.", f"Compare ${a}^\\circ$ and ${b}^\\circ$", "Equal corresponding angles, so the lines are parallel" if a == b else "The corresponding angles are not equal, so the lines are not parallel") for a, b in [(75, 75), (110, 105), (62, 62), (48, 84)]]
           + [QQ(f"Find the angle that is ${a}^\\circ$ less than its supplement.", f"Let the angle be $y$; then $y+(y+{a})=180$", f"$2y={180 - a}$", f"$y={(180 - a) // 2}^\\circ$") for a in (20, 40, 60, 100)])
def around(a, b, c):
    d = 360 - a - b - c; vals = [a, b, c, d]
    return QQ(f"Three of the four angles around a point are ${a}^\\circ$, ${b}^\\circ$ and ${c}^\\circ$. Find the fourth angle and name the kind of each of the four angles.", f"Fourth angle $=360^\\circ-({a}+{b}+{c})^\\circ={d}^\\circ$", "Kinds: " + ", ".join(f"${v}^\\circ$ {kind(v)}" for v in vals))
def parallel_test(kind_name, a, b):
    rule = {"corresponding angles": "equal", "alternate interior angles": "equal", "interior angles on the same side": "supplementary"}[kind_name]
    ok = (a == b) if rule == "equal" else (a + b == 180)
    return QQ(f"A transversal cuts two lines and makes {kind_name} of ${a}^\\circ$ and ${b}^\\circ$. Are the lines parallel? Give a reason.", f"For parallel lines these angles must be {rule}", f"Here ${a}^\\circ$ and ${b}^\\circ$ {'are' if ok else 'are not'} {rule}", "The lines are parallel" if ok else "The lines are not parallel")
def comp_ratio(a, b):
    x, y = split(90, a, b)
    return QQ(f"Two complementary angles are in the ratio ${a}:{b}$. Find them.", f"The sum is $90^\\circ$ and the number of parts is ${a + b}$", f"One part $={90 // (a + b)}^\\circ$", f"The angles are ${x}^\\circ$ and ${y}^\\circ$")
NCERT_C = ([around(*x) for x in [(95, 85, 110), (120, 70, 60), (45, 150, 100), (80, 130, 40), (60, 60, 140), (200, 50, 70)]]
           + [parallel_test(*x) for x in [("corresponding angles", 65, 65), ("alternate interior angles", 70, 75), ("interior angles on the same side", 110, 70), ("corresponding angles", 120, 60), ("alternate interior angles", 98, 98), ("interior angles on the same side", 100, 85)]]
           + [comp_ratio(a, b) for a, b in [(1, 2), (1, 5), (2, 3), (4, 5), (1, 8), (7, 2)]])
def parallel_eight(a):
    return QQ(f"A transversal cuts two parallel lines and one of the eight angles is ${a}^\\circ$. How many of the eight angles measure ${a}^\\circ$ and how many measure ${180 - a}^\\circ$? Give reasons.", f"Equal to ${a}^\\circ$: the angle itself, its vertically opposite angle, its corresponding angle and its alternate interior angle, that is 4 angles", f"Every other angle forms a linear pair with one of these, so it measures ${180 - a}^\\circ$ (4 angles)", f"Check: ${a}+{180 - a}=180$")
def supp_times(k):
    x = 180 * k // (k + 1)
    return QQ(f"An angle is ${k}$ times its supplement. Find the angle and its supplement.", f"Let the supplement be $y$; then the angle is ${k}y$ and ${k}y+y=180$", f"$y={180 // (k + 1)}$", f"The angle is ${x}^\\circ$ and its supplement is ${180 - x}^\\circ$")
NCERT_D = [parallel_eight(a) for a in (50, 110, 65, 130, 75, 145)] + [supp_times(k) for k in (2, 3, 4, 5, 8, 9)]

# ---------------------------------------------------------------- MEDIUM
mA1 = [dg(f"An angle is {k} times its complement. The angle is:", 90 * k // (k + 1), "The angle and its complement add up to $90^\\circ$.", offs=(5, -5, 10, -10, 15, 20)) for k in (2, 5, 8, 17)]
mA2 = [dg(f"Half of the supplement of ${a}^\\circ$ is:", (180 - a) // 2, "Find the supplement first, then halve it.") for a in (40, 60, 100, 120)]
mA3 = [dg(f"Two interior angles on the same side of a transversal cutting parallel lines are in the ratio ${a}:{b}$. The smaller angle is:", split(180, a, b)[0], "They add up to $180^\\circ$.") for a, b in [(1, 2), (2, 3), (1, 5), (4, 5)]]
mA4 = [dg(f"Four angles around a point are ${a}^\\circ$, ${b}^\\circ$, ${c}^\\circ$ and $x^\\circ$. Then $x=$", 360 - a - b - c, "The angles around a point add up to $360^\\circ$.") for a, b, c in [(75, 105, 90), (110, 120, 45), (60, 140, 85), (95, 80, 130)]]
mA5 = [dg(f"An angle is ${a}^\\circ$ less than its supplement. The angle is:", (180 - a) // 2, "Let the angle be $y$; its supplement is $y+a$.") for a in (30, 50, 80, 120)]
mA6 = [tm(q, c, w, "Check the angle relation.") for q, c, w in [
    ("A transversal makes alternate interior angles of $65^\\circ$ and $65^\\circ$. The two lines are:", "parallel", ["intersecting", "perpendicular", "not parallel"]),
    ("A transversal makes corresponding angles of $70^\\circ$ and $75^\\circ$. The two lines are:", "not parallel", ["parallel", "perpendicular", "equal"]),
    ("A transversal makes interior angles on the same side of $110^\\circ$ and $70^\\circ$. The two lines are:", "parallel", ["not parallel", "perpendicular", "equal"]),
    ("Two supplementary angles are both acute. This is:", "not possible", ["possible", "possible only if they are equal", "possible only for $45^\\circ$ each"])]]
mA7 = [dg(f"Two supplementary angles differ by ${d}^\\circ$. The larger angle is:", (180 + d) // 2, "Larger $+$ smaller $=180^\\circ$ and larger $-$ smaller $=d$.") for d in (20, 40, 60, 100)]
mA8 = [dg(f"Two complementary angles are in the ratio ${a}:{b}$. The larger angle is:", split(90, a, b)[1], "Share $90^\\circ$ in the given ratio.") for a, b in [(1, 2), (2, 3), (4, 5), (1, 5)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"An angle is ${a}^\\circ$ more than its complement. Find the angle.", f"Let the complement be $y$; the angle is $y+{a}$ and $y+(y+{a})=90$", f"$2y={90 - a}$, so $y={(90 - a) // 2}$", f"The angle is ${(90 + a) // 2}^\\circ$") for a in (20, 40, 60, 10)]
         + [QQ(f"Two angles forming a linear pair differ by ${a}^\\circ$. Find both angles.", f"Larger $+$ smaller $=180$ and larger $-$ smaller $={a}$", f"Larger $=(180+{a})\\div2={(180 + a) // 2}$", f"The angles are ${(180 + a) // 2}^\\circ$ and ${(180 - a) // 2}^\\circ$") for a in (20, 40, 60, 100)]
         + [QQ(f"A transversal cuts two lines and makes alternate interior angles of ${a}^\\circ$ and ${b}^\\circ$. Are the lines parallel? Give a reason.", f"Compare ${a}^\\circ$ and ${b}^\\circ$", "Equal alternate interior angles, so the lines are parallel" if a == b else "The alternate interior angles are not equal, so the lines are not parallel") for a, b in [(80, 80), (115, 125), (47, 47), (92, 88)]])
def lp_ratio(a, b):
    x, y = split(180, a, b)
    return QQ(f"Two lines intersect and two adjacent angles are in the ratio ${a}:{b}$. Find all four angles.", f"Adjacent angles form a linear pair: ${a + b}$ parts $=180^\\circ$", f"One part $={180 // (a + b)}^\\circ$, so the adjacent angles are ${x}^\\circ$ and ${y}^\\circ$", f"Vertically opposite angles are equal, so the four angles are {seq([x, y, x, y])}")
def comp_more(a):
    x = (180 + a) // 3
    return QQ(f"An angle is ${a}^\\circ$ more than twice its complement. Find the angle and its complement.", f"Let the complement be $y$; the angle is $2y+{a}$ and $y+(2y+{a})=90$", f"$3y={90 - a}$, so $y={(90 - a) // 3}$", f"The angle is ${x}^\\circ$ and its complement is ${90 - x}^\\circ$")
def comp_ratio_pair(a, b):
    x, y = split(180, a, b)
    return QQ(f"Two supplementary angles are in the ratio ${a}:{b}$. Find both angles and the complement of the smaller one.", f"${a + b}$ parts $=180^\\circ$, one part $={180 // (a + b)}^\\circ$", f"The angles are ${x}^\\circ$ and ${y}^\\circ$", f"Complement of the smaller angle $=90^\\circ-{x}^\\circ={90 - x}^\\circ$")
MED_C = [lp_ratio(a, b) for a, b in [(1, 4), (1, 8), (1, 9), (2, 13), (7, 5), (1, 14)]] + [comp_more(a) for a in (6, 15, 30, 45, 12, 24)] + [comp_ratio_pair(a, b) for a, b in [(1, 3), (2, 7), (1, 17), (4, 11), (5, 7), (1, 19)]]
def point_ratio(parts):
    vals = split(360, *parts)
    return QQ(f"The four angles around a point are in the ratio ${ratio(parts)}$. Find the angles and say which of them are acute, right or obtuse.", f"Total parts $={sum(parts)}$ and $360^\\circ\\div{sum(parts)}={360 // sum(parts)}^\\circ$", f"The angles are {seq(vals)}", "Kinds: " + ", ".join(f"${v}^\\circ$ {kind(v)}" for v in vals))
def cointerior(a, b):
    x, y = split(180, a, b)
    return QQ(f"Two interior angles on the same side of a transversal cutting two parallel lines are in the ratio ${a}:{b}$. Find both angles and the angle forming a linear pair with the larger one.", f"They are supplementary: ${a + b}$ parts $=180^\\circ$", f"One part $={180 // (a + b)}^\\circ$, so the angles are ${x}^\\circ$ and ${y}^\\circ$", f"Linear pair with the larger: $180^\\circ-{y}^\\circ={180 - y}^\\circ$")
MED_D = [cointerior(a, b) for a, b in [(2, 3), (1, 5), (4, 5), (1, 11), (3, 7), (1, 2)]] + [point_ratio(p) for p in [(1, 2, 3, 4), (2, 3, 4, 6), (1, 2, 4, 5), (1, 3, 4, 4), (2, 2, 3, 5), (1, 2, 3, 6)]]

# ---------------------------------------------------------------- HARD
hA1 = [tm(q, c, w, "Reason with the angle relations.") for q, c, w in [
    ("The angle between the bisectors of the two angles of a linear pair is:", "$90^\\circ$", ["$45^\\circ$", "$180^\\circ$", "$60^\\circ$"]),
    ("If $l\\parallel m$, the bisectors of a pair of alternate interior angles are:", "parallel", ["perpendicular", "intersecting", "coincident"]),
    ("An angle is equal to its supplement. The angle is:", "$90^\\circ$", ["$45^\\circ$", "$180^\\circ$", "$60^\\circ$"]),
    ("An angle is equal to its complement. The angle is:", "$45^\\circ$", ["$90^\\circ$", "$30^\\circ$", "$60^\\circ$"]),
    ("Two angles are both supplementary to the same angle. They are:", "equal", ["complementary", "supplementary", "unequal"]),
    ("Two angles are both complementary to the same angle. They are:", "equal", ["supplementary", "complementary", "unequal"]),
    ("If a transversal is perpendicular to one of two parallel lines, it is:", "also perpendicular to the other", ["parallel to the other", "a bisector of both", "equal to one of them"]),
    ("If $l\\parallel m$ and $m\\parallel n$, then:", "$l\\parallel n$", ["$l\\perp n$", "$l$ meets $n$", "nothing can be said"]),
    ("The sum of all the angles on one side of a straight line at a point is:", "$180^\\circ$", ["$90^\\circ$", "$360^\\circ$", "$270^\\circ$"])]]
hA2 = [dg(f"Two supplementary angles are in the ratio ${a}:{b}$. The larger angle is:", split(180, a, b)[1], "Share $180^\\circ$ in the given ratio.") for a, b in [(1, 2), (2, 3), (4, 5), (1, 5)]]
hA3 = [dg(f"The supplement of the complement of ${a}^\\circ$ is:", 90 + a, "Complement $=90^\\circ-a$; supplement of that $=180^\\circ-(90^\\circ-a)$.") for a in (20, 35, 50, 65)]
hA4 = [dg(f"The reflex angle that goes with an angle of ${a}^\\circ$ (so that together they make a complete turn) is:", 360 - a, "A complete turn is $360^\\circ$.", offs=(10, -10, 20, -20, 30, 90)) for a in (70, 135, 100, 25)]
hA5 = [dg(f"Two complementary angles differ by ${d}^\\circ$. The larger angle is:", (90 + d) // 2, "Larger $+$ smaller $=90^\\circ$ and larger $-$ smaller $=d$.") for d in (20, 30, 10, 40)]
hA6 = [dg(f"Two angles of a linear pair differ by ${d}^\\circ$. The smaller angle is:", (180 - d) // 2, "Larger $+$ smaller $=180^\\circ$.") for d in (20, 40, 60, 100)]
hA7 = [dg(f"One angle of a linear pair is {k} times the other. The larger angle is:", 180 * k // (k + 1), f"Total $=180^\\circ$ in {k + 1} equal parts.") for k in (2, 3, 4, 5)]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7]
HARD_B = ([QQ(f"Find the angle whose supplement is ${k}$ times its complement.", f"Let the angle be $y$: $180-y={k}(90-y)$", f"${k - 1}y={90 * k - 180}$", f"$y={(90 * k - 180) // (k - 1)}^\\circ$") for k in (3, 4, 6, 7)]
          + [QQ(f"An angle is ${a}^\\circ$ more than 3 times its complement. Find the angle.", f"Let the complement be $y$; the angle is $3y+{a}$ and $y+(3y+{a})=90$", f"$4y={90 - a}$, so $y={(90 - a) // 4}$", f"The angle is ${90 - (90 - a) // 4}^\\circ$") for a in (6, 10, 14, 18)]
          + [QQ(f"Two supplementary angles differ by ${d}^\\circ$. Find both angles and the complement of the smaller one.", f"Larger $=(180+{d})\\div2={(180 + d) // 2}^\\circ$", f"Smaller $=(180-{d})\\div2={(180 - d) // 2}^\\circ$", f"Complement of the smaller $=90^\\circ-{(180 - d) // 2}^\\circ={90 - (180 - d) // 2}^\\circ$") for d in (18, 34, 46, 72)])
def straight(a, b, c):
    d = 180 - a - b - c
    return QQ(f"Angles on one side of a straight line at a point are ${a}^\\circ$, ${b}^\\circ$, ${c}^\\circ$ and a fourth angle. Find the fourth angle and name the kind of each angle.", f"Angles on a straight line add up to $180^\\circ$", f"Fourth angle $=180^\\circ-({a}+{b}+{c})^\\circ={d}^\\circ$", "Kinds: " + ", ".join(f"${v}^\\circ$ {kind(v)}" for v in (a, b, c, d)))
def half_angles(a):
    return QQ(f"Two adjacent angles form a linear pair and one of them is ${a}^\\circ$. Find the other angle, the half of each angle and the angle between the two bisectors.", f"Other angle $=180^\\circ-{a}^\\circ={180 - a}^\\circ$", f"Halves: ${a // 2}^\\circ$ and ${(180 - a) // 2}^\\circ$", f"Angle between the bisectors $={a // 2}^\\circ+{(180 - a) // 2}^\\circ=90^\\circ$")
def supp_small_comp(a, b):
    x, y = split(180, a, b)
    return QQ(f"Two supplementary angles are in the ratio ${a}:{b}$. Find the complement of the smaller angle and the supplement of the larger angle.", f"One part $=180^\\circ\\div{a + b}={180 // (a + b)}^\\circ$", f"Smaller $={x}^\\circ$ and larger $={y}^\\circ$", f"Complement of the smaller $={90 - x}^\\circ$ and supplement of the larger $={180 - y}^\\circ$")
HARD_C = [straight(*x) for x in [(35, 45, 50), (20, 75, 30), (40, 60, 25), (15, 85, 45), (30, 30, 70), (55, 25, 65)]] + [supp_small_comp(a, b) for a, b in [(1, 4), (1, 8), (1, 9), (2, 13), (3, 7), (1, 14)]] + [half_angles(a) for a in (40, 70, 100, 110, 130, 150)]
def line_ratio(parts):
    vals = split(180, *parts)
    return QQ(f"Three angles on one side of a straight line at a point are in the ratio ${ratio(parts)}$. Find the three angles and name the kind of each.", f"Total parts $={sum(parts)}$ and $180^\\circ\\div{sum(parts)}={180 // sum(parts)}^\\circ$", f"The angles are {seq(vals)}", "Kinds: " + ", ".join(f"${v}^\\circ$ {kind(v)}" for v in vals))
def eight(a, b):
    x, y = split(180, a, b)
    return QQ(f"A transversal cuts two parallel lines and two interior angles on the same side are in the ratio ${a}:{b}$. Find these two angles and say how many of the eight angles measure ${x}^\\circ$ and how many ${y}^\\circ$.", f"They are supplementary: one part $=180^\\circ\\div{a + b}={180 // (a + b)}^\\circ$", f"The angles are ${x}^\\circ$ and ${y}^\\circ$", "Four of the eight angles equal the smaller angle (vertically opposite, corresponding and alternate angles of it)", f"The other four equal ${y}^\\circ$ (linear pairs)")
HARD_D = [line_ratio(p) for p in [(1, 2, 3), (2, 3, 4), (1, 3, 5), (2, 3, 7), (1, 4, 7), (3, 4, 5)]] + [eight(a, b) for a, b in [(2, 3), (1, 4), (5, 7), (1, 11), (4, 11), (1, 17)]]

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
