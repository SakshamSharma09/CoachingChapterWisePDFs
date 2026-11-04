"""Class 7 Maths Ch 5 - Parallel and Intersecting Lines (angle pairs, transversal)."""
from g67 import *

SLUG, NAME, CHNO = "Parallel_and_Intersecting_Lines", "Parallel and Intersecting Lines", 5

def ang(q, c, why="", offs=(10, -10, 20, -20, 30, 90, 5)):
    return nm(q, c, why, offs=offs, pos=True)
def D(n): return f"${n}^\\circ$"
def M(n): return f"{n}^\\circ"

def nm_deg(q, c, why="", offs=(10, -10, 20, -20, 30, 5, 15)):
    out = []
    for o in offs:
        x = c + o
        if x != c and x > 0 and x not in out: out.append(x)
    return M4(q, D(c), [D(x) for x in out[:6]], why)

# ---------------- EASY
eA1 = [nm_deg(f"The complement of ${a}^\\circ$ is:", 90 - a, "Complementary angles add up to $90^\\circ$.") for a in (30, 65, 48, 72, 15)]
eA2 = [nm_deg(f"The supplement of ${a}^\\circ$ is:", 180 - a, "Supplementary angles add up to $180^\\circ$.") for a in (50, 115, 78, 140, 95)]
eA3 = [nm_deg(f"Two lines intersect and one angle is ${a}^\\circ$. Its vertically opposite angle is:", a, "Vertically opposite angles are equal.") for a in (40, 75, 110, 135)]
eA4 = [nm_deg(f"Two angles forming a linear pair: one is ${a}^\\circ$. The other is:", 180 - a, "A linear pair adds up to $180^\\circ$.") for a in (60, 100, 125, 35)]
eA5 = [tm(t, c, w, "Recall the definition.") for t, c, w in [
    ("Lines in a plane that never meet are called:", "parallel lines", ["intersecting lines", "perpendicular lines", "transversals"]),
    ("A line that cuts two or more lines at different points is called a:", "transversal", ["parallel line", "bisector", "median"]),
    ("Two angles whose sum is $90^\\circ$ are:", "complementary", ["supplementary", "vertically opposite", "adjacent only"]),
    ("Two lines meeting at $90^\\circ$ are:", "perpendicular", ["parallel", "skew", "equal"])]]
eA6 = [nm_deg(f"Corresponding angles formed by a transversal on parallel lines are equal. If one is ${a}^\\circ$, the corresponding angle is:", a, "Corresponding angles are equal when the lines are parallel.") for a in (55, 82, 118, 67)]
eA7 = [nm_deg(f"Alternate interior angles on parallel lines are equal. If one is ${a}^\\circ$, the other is:", a, "Alternate interior angles are equal.") for a in (48, 73, 99, 125)]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([QQ(f"Find the complement of ${a}^\\circ$ and the supplement of ${b}^\\circ$.", f"Complement $=90^\\circ-{a}^\\circ={90-a}^\\circ$", f"Supplement $=180^\\circ-{b}^\\circ={180-b}^\\circ$") for a, b in [(35, 110), (62, 75), (18, 140), (47, 98)]]
          + [QQ(f"Two lines intersect. One of the angles is ${a}^\\circ$. Find the other three angles.", f"Vertically opposite $={a}^\\circ$", f"Other two $=180^\\circ-{a}^\\circ={180-a}^\\circ$ each") for a in (65, 110, 40, 125)]
          + [QQ(f"A transversal cuts two parallel lines. One corresponding angle is ${a}^\\circ$. Write the corresponding angle and the co-interior (same-side interior) angle partner type.", f"Corresponding angle $={a}^\\circ$", f"Co-interior angles are supplementary: ${180-a}^\\circ$") for a in (70, 105, 58, 132)])
EASY_C = ([QQ(f"Two angles of a linear pair are in the ratio ${a}:{b}$. Find them.", f"Sum $=180^\\circ$, total parts ${a+b}$", f"One part $={180//(a+b)}^\\circ$", f"Angles ${a*180//(a+b)}^\\circ$ and ${b*180//(a+b)}^\\circ$") for a, b in [(1, 2), (1, 5), (2, 3), (4, 5), (1, 3), (2, 7)] if 180 % (a + b) == 0]
          + [QQ(f"Find $x$ if the angles $x^\\circ$ and ${a}^\\circ$ are supplementary, and name the type of angle $x$.", f"$x+{a}=180$", f"$x={180-a}$", f"Angle is {'acute' if 180-a<90 else 'obtuse'}") for a in (110, 135, 150, 95, 70, 160)]
          + [QQ(f"A transversal crosses two parallel lines. Angle 1 $={a}^\\circ$ is an alternate interior angle with angle 2. Find angle 2 and the co-interior angle with angle 1.", f"Angle 2 $={a}^\\circ$ (alternate interior)", f"Co-interior $=180^\\circ-{a}^\\circ={180-a}^\\circ$", "Reason: parallel lines") for a in (52, 66, 74, 88, 103, 117)])
EASY_D = ([QQ(f"Two lines intersect at O forming angles ${a}^\\circ$ and $(x)^\\circ$ as a linear pair. Find $x$, and then all four angles formed.", f"$x={180-a}$", f"Vertically opposite pairs: ${a}^\\circ,{a}^\\circ$ and ${180-a}^\\circ,{180-a}^\\circ$", f"Sum check: ${2*a+2*(180-a)}^\\circ$", "Four angles around a point make $360^\\circ$") for a in (35, 50, 65, 80, 115, 130)]
          + [QQ(f"A transversal cuts parallel lines $l$ and $m$. One angle at $l$ is ${a}^\\circ$. Find all eight angles formed.", f"Angles equal to ${a}^\\circ$: vertically opposite, corresponding, alternate (4 in all)", f"Angles equal to ${180-a}^\\circ$: the other 4", f"Linear pair: ${a}+{180-a}=180$", "State reasons for each") for a in (40, 55, 70, 85, 100, 125)])

# ---------------- NCERT
nA1 = [nm_deg(f"If $x$ and ${a}^\\circ$ are complementary, $x=$", 90 - a, "Sum is $90^\\circ$.") for a in (24, 37, 51, 68, 83)]
nA2 = [nm_deg(f"In a linear pair, one angle is {k} times the other. The smaller angle is:", 180 // (k + 1), "Total parts $=k+1$.") for k in (2, 4, 5, 8)]
nA3 = [nm_deg(f"Two parallel lines are cut by a transversal. If an interior angle is ${a}^\\circ$, the co-interior angle on the same side is:", 180 - a, "Co-interior angles are supplementary.") for a in (65, 80, 112, 135)]
nA4 = [tm(t, c, w, "Use the property of parallel lines.") for t, c, w in [
    ("If corresponding angles are equal, the lines are:", "parallel", ["perpendicular", "intersecting", "coincident only"]),
    ("If co-interior angles add to $180^\\circ$, the lines are:", "parallel", ["perpendicular", "intersecting", "unequal"]),
    ("If alternate interior angles are not equal, the lines are:", "not parallel", ["parallel", "perpendicular", "coincident"]),
    ("The number of angles formed by a transversal on two lines is:", "8", ["4", "6", "12"])]]
nA5 = [nm_deg(f"Angle $A={a}^\\circ$ and angle $B$ are vertically opposite. Angle $B$ is:", a, "Vertically opposite angles are equal.") for a in (28, 64, 97, 143)]
nA6 = [tm(f"An angle of ${a}^\\circ$ is:", t, [w for w in ["acute", "right", "obtuse", "reflex"] if w != t][:3], "Classify by measure.") for a, t in [(35, "acute"), (90, "right"), (125, "obtuse"), (210, "reflex"), (89, "acute")]]
nA7 = [nm_deg(f"The sum of angles around a point is $360^\\circ$. If three angles are ${a}^\\circ$, ${b}^\\circ$, ${c}^\\circ$ the fourth is:", 360 - a - b - c, "Total is $360^\\circ$.") for a, b, c in [(100, 90, 80), (120, 70, 60), (95, 85, 110), (130, 65, 75)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Find $x$ if $(2x+{a})^\\circ$ and $({x0}^\\circ)$ form a linear pair.", f"$2x+{a}+{x0}=180$", f"$x={(180-a-x0)//2}$") for a, x0 in [(10, 70), (20, 100), (30, 80), (6, 94)]]
           + [QQ(f"Lines $l\\parallel m$ and a transversal. A pair of alternate interior angles are $(x+{a})^\\circ$ and ${b}^\\circ$. Find $x$.", "Alternate interior angles are equal", f"$x+{a}={b}$, so $x={b-a}$") for a, b in [(10, 65), (25, 80), (15, 110), (30, 95)]]
           + [QQ(f"Two angles are supplementary and one is ${k}$ times the other. Find them.", f"$x+{k}x=180$", f"$x={180//(k+1)}^\\circ$, other ${k*180//(k+1)}^\\circ$") for k in (2, 3, 4, 5)])
NCERT_C = ([QQ(f"Lines $l\\parallel m$, transversal $t$. Angle $\\angle 1=(3x+{a})^\\circ$ and its corresponding angle $=(2x+{b})^\\circ$. Find $x$ and the angle.", "Corresponding angles equal", f"$3x+{a}=2x+{b}$ so $x={b-a}$", f"Angle $={3*(b-a)+a}^\\circ$") for a, b in [(5, 40), (10, 55), (15, 60), (8, 45), (20, 70), (12, 50)]]
           + [QQ(f"Co-interior angles on parallel lines are $(4x+{a})^\\circ$ and $(2x+{b})^\\circ$. Find $x$ and both angles.", "Sum is $180^\\circ$", f"$6x={180-a-b}$ so $x={(180-a-b)//6}$", f"Angles ${4*((180-a-b)//6)+a}^\\circ$ and ${2*((180-a-b)//6)+b}^\\circ$") for a, b in [(6, 12), (10, 20), (12, 18), (4, 14), (8, 10), (6, 24)]]
           + [QQ(f"Two lines intersect forming angles $(5x-{a})^\\circ$ and $(3x+{b})^\\circ$ as vertically opposite angles. Find $x$ and all four angles.", "Vertically opposite angles are equal", f"$5x-{a}=3x+{b}$ so $x={(a+b)//2}$", f"Equal angles ${5*((a+b)//2)-a}^\\circ$ each", f"Other two ${180-(5*((a+b)//2)-a)}^\\circ$ each") for a, b in [(10, 20), (6, 14), (8, 18), (12, 30), (4, 16), (2, 12)]])
NCERT_D = ([QQ(f"Lines $l\\parallel m$ and transversal $t$. Angles at $l$: $\\angle 1={a}^\\circ$. Write the values of the corresponding, alternate interior, vertically opposite and co-interior angles of $\\angle1$ at $m$, with reasons.", f"Corresponding $={a}^\\circ$", f"Alternate interior $={a}^\\circ$ (it is vertically opposite to the corresponding angle)", f"Vertically opposite to $\\angle1$ $={a}^\\circ$", f"Co-interior $={180-a}^\\circ$", "Give a reason for each") for a in (50, 65, 75, 110, 125, 140)]
           + [QQ(f"Two parallel lines are cut by a transversal and one of the eight angles is ${a}^\\circ$. How many of the eight angles measure ${a}^\\circ$ and how many measure ${180-a}^\\circ$? Give reasons.", f"Equal to ${a}^\\circ$: vertically opposite, corresponding and alternate angles (4 angles)", f"Remaining 4 angles form linear pairs with it, so ${180-a}^\\circ$ each", "Linear pair: sum $180^\\circ$", "Co-interior pairs are supplementary", f"Check: $4({a})+4({180-a})=720^\\circ$") for a in (50, 65, 75, 110, 125, 140)])

# ---------------- MEDIUM
mA1 = [tm(f"If $(x+{a})^\\circ$ and $(2x-{b})^\\circ$ are supplementary, $x$ equals:", str((180 - a + b) // 3), [str((180 - a + b) // 3 + 5), str((180 - a + b) // 3 - 5), str((180 - a + b) // 3 + 10)], "$3x+a-b=180$.") for a, b in [(10, 4), (20, 8), (5, 14), (15, 6)] if (180 - a + b) % 3 == 0]
mA2 = [nm_deg(f"If $l\\parallel m$ and two co-interior angles are ${a}^\\circ$ and $(x)^\\circ$, then $x=$", 180 - a, "Co-interior angles are supplementary.") for a in (68, 87, 99, 123)]
mA3 = [nm_deg(f"The angle which is {k} times its complement is:", 90 * k // (k + 1), "$x=k(90-x)$.") for k in (2, 5, 8, 1, 9, 17)]
mA4 = [nm_deg(f"Half of the supplement of ${a}^\\circ$ is:", (180 - a) // 2, "Supplement first, then halve.") for a in (40, 60, 100, 120)]
mA5 = [nm_deg(f"The angle bisector of a ${a}^\\circ$ angle makes each part:", a // 2, "Bisector splits equally.") for a in (70, 110, 130, 150)]
mA6 = [tm(t, c, w, "Check the angle relation.") for t, c, w in [
    ("A transversal makes alternate interior angles of $65^\\circ$ and $65^\\circ$. The two lines are:", "parallel", ["intersecting", "perpendicular", "cannot say"]),
    ("A transversal makes corresponding angles of $70^\\circ$ and $75^\\circ$. The two lines are:", "not parallel", ["parallel", "perpendicular", "equal"]),
    ("A transversal makes co-interior angles of $110^\\circ$ and $70^\\circ$. The two lines are:", "parallel", ["not parallel", "perpendicular", "cannot say"]),
    ("Three distinct lines pass through one point. The number of pairs of vertically opposite angles is:", "3", ["2", "4", "6"])]]
mA7 = [nm_deg(f"A transversal makes co-interior angles in the ratio ${a}:{b}$ on parallel lines. The smaller angle is:", 180 * a // (a + b), "Total $180^\\circ$.") for a, b in [(1, 2), (2, 3), (1, 5), (4, 5)] if 180 % (a + b) == 0]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([QQ(f"Find the angle that is ${a}^\\circ$ less than its supplement.", f"$x=(180-x)-{a}$", f"$2x={180-a}$, $x={(180-a)//2}^\\circ$") for a in (20, 40, 60, 100)]
         + [QQ(f"Find $x$ if $(3x-{a})^\\circ$ and $(x+{b})^\\circ$ are vertically opposite angles.", "Vertically opposite angles are equal", f"$2x={a+b}$, $x={(a+b)//2}$") for a, b in [(10, 20), (6, 14), (12, 40), (8, 30)]]
         + [QQ(f"Is $l\\parallel m$ if a transversal gives corresponding angles ${a}^\\circ$ and ${b}^\\circ$? Give reason.", f"Compare ${a}^\\circ$ and ${b}^\\circ$", "Equal corresponding angles imply parallel lines" if a == b else "Unequal, so not parallel") for a, b in [(75, 75), (110, 105), (62, 62), (48, 84)]])
MED_C = ([QQ(f"A transversal cuts parallel lines. Interior angles on the same side are $(2x+{a})^\\circ$ and $(3x+{b})^\\circ$. Find $x$ and the two angles.", "Co-interior angles sum to $180^\\circ$", f"$5x={180-a-b}$, $x={(180-a-b)//5}$", f"Angles ${2*((180-a-b)//5)+a}^\\circ$, ${3*((180-a-b)//5)+b}^\\circ$") for a, b in [(10, 15), (5, 20), (15, 10), (20, 25), (5, 25), (10, 30)] if (180 - a - b) % 5 == 0]
         + [QQ(f"In a pair of intersecting lines, the angles are $(x+{a})^\\circ$, $(2x-{b})^\\circ$ forming a linear pair. Find $x$ and the vertically opposite angles.", f"$3x+{a-b}=180$", f"$x={(180-a+b)//3}$", f"Angles ${(180-a+b)//3+a}^\\circ$ and ${2*((180-a+b)//3)-b}^\\circ$", "Each equals its vertically opposite") for a, b in [(15, 9), (30, 6), (12, 3), (24, 12), (9, 6), (21, 3)] if (180 - a + b) % 3 == 0]
         + [QQ(f"An angle is ${a}^\\circ$ more than twice its complement. Find the angle and its complement.", f"$x=2(90-x)+{a}$", f"$3x={180+a}$, $x={(180+a)//3}^\\circ$", f"Complement ${90-(180+a)//3}^\\circ$") for a in (6, 15, 30, 45, 12, 24)])
MED_D = ([QQ(f"Lines $l\\parallel m$, transversal $t$. $\\angle1=(2x+{a})^\\circ$, $\\angle2=(3x-{b})^\\circ$ are alternate interior angles; $\\angle3$ is the co-interior angle of $\\angle1$. Find $x$, $\\angle1$, $\\angle2$ and $\\angle3$.", "Alternate interior equal: $2x+a=3x-b$", f"$x={a+b}$", f"$\\angle1=\\angle2={2*(a+b)+a}^\\circ$", f"$\\angle3=180^\\circ-{2*(a+b)+a}^\\circ={180-2*(a+b)-a}^\\circ$", "Reasons") for a, b in [(10, 20), (15, 10), (5, 25), (20, 15), (8, 22), (12, 18)]]
         + [QQ(f"Around a point, angles are $x^\\circ$, $2x^\\circ$, $3x^\\circ$ and ${a}^\\circ$. Find $x$ and each angle, and say which are acute, right or obtuse.", f"$6x+{a}=360$", f"$x={(360-a)//6}$", f"Angles ${(360-a)//6}^\\circ,{2*((360-a)//6)}^\\circ,{3*((360-a)//6)}^\\circ,{a}^\\circ$", "Classify each") for a in (30, 60, 90, 120, 150, 36) if (360 - a) % 6 == 0])

# ---------------- HARD
hA1 = [nm_deg(f"Lines $l\\parallel m$. If $(3x+{a})^\\circ$ and $(2x+{b})^\\circ$ are co-interior, the larger angle is:", max(3 * ((180 - a - b) // 5) + a, 2 * ((180 - a - b) // 5) + b), "Find $x$ first.") for a, b in [(10, 20), (5, 25), (15, 10), (20, 30)] if (180 - a - b) % 5 == 0]
hA2 = [nm_deg(f"In a pattern, $\\angle A$ is supplementary to $\\angle B$ and $\\angle B$ is complementary to $\\angle C={c}^\\circ$. $\\angle A=$", 180 - (90 - c), "Find B, then A.") for c in (20, 35, 50, 65)]
hA3 = [tm("The angle between the bisectors of the two angles of a linear pair is:", "$90^\\circ$", ["$45^\\circ$", "$180^\\circ$", "$60^\\circ$"], "Half of $180^\\circ$.")]
hA3 += [tm(t, c, w, "Use linear pairs and parallel-line properties.") for t, c, w in [
    ("If $l\\parallel m$, the bisectors of a pair of alternate interior angles are:", "parallel", ["perpendicular", "intersecting at $45^\\circ$", "equal in length"]),
    ("An angle is equal to its supplement. The angle is:", "$90^\\circ$", ["$45^\\circ$", "$180^\\circ$", "$60^\\circ$"]),
    ("An angle equals its complement. The angle is:", "$45^\\circ$", ["$90^\\circ$", "$30^\\circ$", "$60^\\circ$"]),
    ("Two angles are both supplementary to the same angle. They are:", "equal", ["complementary", "supplementary", "unequal"]),
    ("Two angles are both complementary to the same angle. They are:", "equal", ["supplementary", "complementary", "unequal"])]]
hA4 = [nm_deg(f"A transversal cuts parallel lines; the interior angle on one side is $({3}x)^\\circ$ and the alternate angle is $(x+{a})^\\circ$. The angle (in degrees) is:", 3 * (a // 2), "Equate.") for a in (30, 50, 70, 90)]
hA5 = [nm_deg(f"Two angles are supplementary; the difference is ${d}^\\circ$. The larger is:", (180 + d) // 2, "$x+y=180$, $x-y=d$.") for d in (20, 40, 60, 100)]
hA6 = [nm_deg(f"Two angles are complementary; the ratio is ${a}:{b}$. The larger is:", 90 * max(a, b) // (a + b), "Share $90^\\circ$ by the ratio.") for a, b in [(1, 2), (2, 3), (4, 5), (1, 5)] if 90 % (a + b) == 0]
hA7 = [tm(t, c, w, "Reason with angle relations.") for t, c, w in [
    ("If a transversal is perpendicular to one of two parallel lines, it is also:", "perpendicular to the other", ["parallel to it", "bisecting it", "equal to it"]),
    ("Lines perpendicular to the same line (in a plane) are:", "parallel", ["intersecting", "perpendicular", "equal"]),
    ("If $l\\parallel m$ and $m\\parallel n$, then:", "$l\\parallel n$", ["$l\\perp n$", "$l$ meets $n$", "cannot say"]),
    ("The sum of all angles at a point on one side of a straight line is:", "$180^\\circ$", ["$90^\\circ$", "$360^\\circ$", "$270^\\circ$"])]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7]
HARD_B = ([QQ(f"Two lines intersect forming angles $a$ and $b$ (vertically opposite) with $c$ adjacent to both. Show that $a=b$ using linear pairs, and verify with $c={c}^\\circ$.", "$a+c=180^\\circ$ and $b+c=180^\\circ$", "Hence $a=b$", f"With $c={c}^\\circ$: $a=b={180-c}^\\circ$") for c in (40, 75, 110, 140)]
          + [QQ(f"Lines $l\\parallel m$; $\\angle1=(5x-{a})^\\circ$ and $\\angle2=(4x+{b})^\\circ$ are corresponding angles. Find $x$ and $\\angle1$.", "Corresponding angles are equal", f"$5x-{a}=4x+{b}$, so $x={a+b}$", f"$\\angle1={5*(a+b)-a}^\\circ$") for a, b in [(10, 15), (20, 5), (8, 12), (25, 10)]]
          + [QQ(f"Find the angle whose supplement is ${k}$ times its complement.", f"$180-x={k}(90-x)$", f"$({k}-1)x={90*k-180}$", f"$x={(90*k-180)//(k-1)}^\\circ$") for k in (3, 4, 6, 7)])
HARD_C = ([QQ(f"A transversal makes angles $(2x+{a})^\\circ$ and $(x+{b})^\\circ$ with parallel lines as alternate exterior angles (equal for parallel lines). Find $x$, then the co-interior-supplementary partner of the angle.", f"$2x+{a}=x+{b}$ gives $x={b-a}$", f"Angle $={2*(b-a)+a}^\\circ$", f"Supplementary partner $={180-2*(b-a)-a}^\\circ$") for a, b in [(10, 40), (15, 55), (20, 60), (5, 35), (25, 65), (12, 48)]]
          + [QQ(f"Angles on one side of a straight line are $x^\\circ$, $(x+{a})^\\circ$, $(2x-{b})^\\circ$ and ${c}^\\circ$. Find $x$ and each angle.", "Angles on a line sum to $180^\\circ$", f"$4x+{a-b+c}=180$", f"$x={(180-a+b-c)//4}$", f"Angles ${(180-a+b-c)//4}^\\circ$, ${(180-a+b-c)//4+a}^\\circ$, ${2*((180-a+b-c)//4)-b}^\\circ$, ${c}^\\circ$") for a, b, c in [(10, 2, 20), (12, 4, 24), (20, 4, 16), (8, 2, 30), (6, 2, 20), (14, 2, 28)]]
          + [QQ(f"Show that if two parallel lines are cut by a transversal, the bisectors of a pair of alternate interior angles are parallel. Verify with the angle ${2*a}^\\circ$ (each half ${a}^\\circ$).", "Alternate interior angles equal, so halves equal", f"Halves ${a}^\\circ$ are alternate angles on the bisectors", "Equal alternate angles imply parallel", f"Check: ${a}^\\circ={a}^\\circ$") for a in (20, 25, 30, 35, 40, 45)])
HARD_D = ([QQ(f"Lines $l\\parallel m$ and transversal $t$. $\\angle1=(4x+{a})^\\circ$ and $\\angle2=(5x-{b})^\\circ$ are co-interior angles. A second transversal gives $\\angle3$ corresponding to $\\angle1$. Find $x$, all three angles and state reasons.", "Co-interior angles sum to $180^\\circ$", f"$9x+{a-b}=180$, so $x={(180-a+b)//9}$", f"$\\angle1={4*((180-a+b)//9)+a}^\\circ$", f"$\\angle2={5*((180-a+b)//9)-b}^\\circ$ and $\\angle3=\\angle1$", "Reasons stated") for a, b in [(10, 1), (20, 2), (30, 3), (40, 4), (18, 0), (25, 7)]]
          + [QQ(f"Lines $l\\parallel m$ are cut by a transversal; two co-interior angles are in the ratio ${p}:{q}$. Find both angles, the corresponding angle of the larger one at the other line, and the vertically opposite angle of the smaller one.", f"Sum $180^\\circ$, parts ${p+q}$", f"Angles ${180*p//(p+q)}^\\circ$ and ${180*q//(p+q)}^\\circ$", f"Corresponding angle of larger $={max(p,q)*180//(p+q)}^\\circ$", f"Vertically opposite of smaller $={min(p,q)*180//(p+q)}^\\circ$", "Reasons stated") for p, q in [(1, 2), (2, 3), (1, 5), (4, 5), (1, 3), (2, 7)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
