"""Class 9 Maths Ch 1 - Coordinates (Cartesian plane, quadrants, reflections, distance and midpoint)."""
from c9h import *

SLUG, NAME, CHNO = "Coordinates", "Coordinates", 1

QN = {1: "Quadrant I", 2: "Quadrant II", 3: "Quadrant III", 4: "Quadrant IV"}
def quad(x, y): return 1 if x > 0 and y > 0 else 2 if x < 0 < y else 3 if x < 0 and y < 0 else 4
def qopts(q): return [QN[i] for i in (1, 2, 3, 4) if i != q]
def d2(p, q): return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
def tri_pts(a, b, x0=0, y0=0): return (x0, y0), (x0 + a, y0), (x0 + a, y0 + b)   # right angle at 2nd vertex

def dist_q(p, q): return f"${P(*p)}$ and ${P(*q)}$"

# ------------------------------------------------------------------ EASY
eA1 = [M4(f"The point ${P(x, y)}$ lies in:", QN[quad(x, y)], qopts(quad(x, y)), "Check the signs of the abscissa and ordinate.")
       for x, y in [(3, 5), (-4, 2), (-6, -1), (7, -3), (-2, -8), (9, 4), (-5, 6), (1, -9)]]
eA2 = [nm(f"The abscissa of the point ${P(x, y)}$ is:", x, "The abscissa is the $x$-coordinate.", pos=False) for x, y in [(6, -2), (-7, 3), (4, 9), (-8, -5)]]
eA3 = [nm(f"The ordinate of the point ${P(x, y)}$ is:", y, "The ordinate is the $y$-coordinate.", pos=False) for x, y in [(2, -6), (-3, 7), (5, 8), (-9, -4)]]
eA4 = [nm(f"The distance of the point ${P(a, b)}$ from the origin is:", c, rf"$\sqrt{{{a}^2+{b}^2}}={c}$") for a, b, c in TRI[:4]]
eA5 = [M4(f"The midpoint of the segment joining ${P(2*a, 2*b)}$ and ${P(2*c, 2*d)}$ is:", TP(a + c, b + d), optpts(a + c, b + d), "Average the abscissae and the ordinates.")
       for a, b, c, d in [(1, 2, 3, 4), (2, 1, 4, 5), (0, 3, 6, 1), (3, 0, 1, 2), (4, 4, 2, 6)]]
eA6 = [M4(t, c, w, "Recall the properties of the axes.") for t, c, w in [
    ("A point on the $x$-axis has:", "ordinate $0$", ["abscissa $0$", "both coordinates $0$", "equal coordinates"]),
    ("A point on the $y$-axis has:", "abscissa $0$", ["ordinate $0$", "both coordinates $0$", "equal coordinates"]),
    ("The coordinates of the origin are:", "$(0, 0)$", ["$(1, 0)$", "$(0, 1)$", "$(1, 1)$"]),
    ("The number of quadrants in the Cartesian plane is:", "4", ["2", "3", "8"])]]
eA7 = [M4(f"The reflection of ${P(a, b)}$ in the $x$-axis is:", TP(a, -b), optpts(a, -b), "Only the sign of the ordinate changes.") for a, b in [(3, 4), (-2, 5), (6, -1), (-7, -3)]]
eA8 = [nm(f"The distance between ${P(x1, k)}$ and ${P(x2, k)}$ is:", abs(x2 - x1), "Same ordinate: distance $=|x_2-x_1|$.") for x1, x2, k in [(1, 8, 3), (-2, 5, 4), (-6, -1, 2), (3, 12, -5)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Write the coordinates of the point that lies ${abs(x)}$ units {'right' if x > 0 else 'left'} of the $y$-axis and ${abs(y)}$ units {'above' if y > 0 else 'below'} the $x$-axis.",
              f"Abscissa $={x}$, ordinate $={y}$", f"Point $={P(x, y)}$ in {QN[quad(x, y)]}") for x, y in [(4, 3), (-5, 2), (-3, -6), (7, -4)]]
          + [QQ(f"Find the distance of the point ${P(a, b)}$ from the origin.", rf"$d=\sqrt{{{a}^2+{b}^2}}=\sqrt{{{a*a+b*b}}}$", f"$d={c}$ units") for a, b, c in TRI[4:8]]
          + [QQ(f"Find the midpoint of the segment joining ${P(2*a, 2*b)}$ and ${P(2*c, 2*d)}$.", rf"$\left(\frac{{{2*a}+{2*c}}}{{2}},\frac{{{2*b}+{2*d}}}{{2}}\right)$", f"Midpoint $={P(a + c, b + d)}$")
             for a, b, c, d in [(1, 5, 3, 2), (4, 1, 2, 7), (3, 3, 5, 1), (0, 6, 4, 2)]])
EASY_C = ([QQ(f"Find the distance between $A{P(x, y)}$ and $B{P(x + a, y + b)}$.", rf"$AB=\sqrt{{({x+a}-({x}))^2+({y+b}-({y}))^2}}=\sqrt{{({a})^2+({b})^2}}$", f"$AB=\\sqrt{{{a*a}+{b*b}}}=\\sqrt{{{a*a+b*b}}}$", f"$AB={c}$ units")
           for (a, b, c), (x, y) in zip(TRI[:6], [(1, 2), (-2, 1), (0, -3), (4, -1), (-3, -2), (2, 5)])]
          + [QQ(f"Write the quadrant of ${P(x, y)}$, and the reflections of this point in the $x$-axis and in the $y$-axis.", f"Signs $({'+' if x > 0 else '-'},{'+' if y > 0 else '-'})$: {QN[quad(x, y)]}", f"Reflection in $x$-axis: ${P(x, -y)}$", f"Reflection in $y$-axis: ${P(-x, y)}$")
             for x, y in [(5, 8), (-4, 6), (-9, -2), (3, -7), (-1, 10), (8, -5)]]
          + [QQ(f"Find the midpoint of $A{P(x, y)}$ and $B{P(x + 2*a, y + 2*b)}$ and its distance from the origin.", f"Midpoint $={P(x + a, y + b)}$", rf"$d=\sqrt{{({x+a})^2+({y+b})^2}}$", f"$d={sur((x+a)**2+(y+b)**2)}$ units")
             for (a, b), (x, y) in zip([(1, 2), (3, 1), (2, 4), (1, 3), (5, 2), (4, 1)], [(0, 0), (1, 1), (2, 0), (0, 3), (1, 2), (3, 3)])])
EASY_D = ([QQ(f"The vertices of a triangle are $A{P(*tri_pts(a, b, x, y)[0])}$, $B{P(*tri_pts(a, b, x, y)[1])}$ and $C{P(*tri_pts(a, b, x, y)[2])}$. Find the three sides and show that the triangle is right-angled at $B$.",
              f"$AB=\\sqrt{{{a}^2+0^2}}={a}$", f"$BC=\\sqrt{{0^2+{b}^2}}={b}$", f"$AC=\\sqrt{{{a*a}+{b*b}}}={c}$",
              f"$AB^2+BC^2={a*a}+{b*b}={a*a+b*b}$", f"$AC^2={c*c}$, so $AB^2+BC^2=AC^2$: right angle at $B$")
           for (a, b, c), (x, y) in zip(TRI[8:14], [(0, 0), (1, 2), (-2, 3), (4, -1), (-3, -4), (2, 2)])]
          + [QQ(f"For the point $P{P(x, y)}$, state its quadrant, its distances from the two axes and from the origin, and its reflection in the origin.",
                f"Quadrant: {QN[quad(x, y)]}", f"Distance from $x$-axis $=|{y}|={abs(y)}$; from $y$-axis $=|{x}|={abs(x)}$",
                f"$OP=\\sqrt{{{x*x}+{y*y}}}={c}$", f"Reflection in the origin: ${P(-x, -y)}$", f"The origin is the midpoint of $P$ and its image: $\\left(\\frac{{{x}+({-x})}}{{2}},\\frac{{{y}+({-y})}}{{2}}\\right)=(0, 0)$")
             for (x, y, c) in [(3, 4, 5), (-5, 12, 13), (-8, -15, 17), (7, -24, 25), (-6, 8, 10), (9, 12, 15)]])

# ------------------------------------------------------------------ NCERT
nA1 = [M4(f"The point ${P(x, y)}$ is reflected in the $y$-axis. The image is:", TP(-x, y), optpts(-x, y), "Reflection in the $y$-axis changes the sign of the abscissa.") for x, y in [(5, -2), (-3, 8), (7, 4), (-9, -6)]]
nA2 = [nm(f"The distance between ${P(x1, y1)}$ and ${P(x2, y2)}$ is:", c, "Apply the distance formula.") for (x1, y1, x2, y2, c) in
       [(1, 2, 4, 6, 5), (-1, -1, 4, 11, 13), (2, 3, 10, 18, 17), (0, 0, -7, 24, 25), (-3, 2, 3, 10, 10)]]
nA3 = [M4(f"The midpoint of the segment joining ${P(x1, y1)}$ and ${P(x2, y2)}$ is:", TP(*m), optpts(*m), "Use $\\left(\\frac{x_1+x_2}{2},\\frac{y_1+y_2}{2}\\right)$.")
       for (x1, y1, x2, y2, m) in [(-4, 6, 8, -2, (2, 2)), (-6, -2, 2, 10, (-2, 4)), (5, 9, -3, 1, (1, 5)), (-8, 4, -2, -6, (-5, -1)), (10, -4, -6, 12, (2, 4))]]
nA4 = [M4(f"A point on the $x$-axis at distance ${abs(x)}$ units to the {'right' if x > 0 else 'left'} of the origin has coordinates:", TP(x, 0), optpts(x, 0), "Ordinate is $0$ on the $x$-axis.") for x in (6, -4, 9, -7)]
nA5 = [M4(t, c, w, "Use the sign rules for the quadrants.") for t, c, w in [
    ("If $x<0$ and $y>0$, the point $(x, y)$ lies in:", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"]),
    ("If $x>0$ and $y<0$, the point $(x, y)$ lies in:", "Quadrant IV", ["Quadrant I", "Quadrant II", "Quadrant III"]),
    ("Both coordinates are negative in:", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"]),
    ("The point $(0, -5)$ lies on the:", "negative $y$-axis", ["positive $y$-axis", "negative $x$-axis", "positive $x$-axis"])]]
nA6 = [nm(f"The distance of ${P(a, b)}$ from the $x$-axis is:", abs(b), "The distance from the $x$-axis is $|y|$.") for a, b in [(5, -7), (-3, 11), (8, -2), (-6, -13)]]
nA7 = [M4(f"If the midpoint of $AB$ is ${P(*m)}$ and $A={P(*a)}$, then $B$ is:", TP(2*m[0] - a[0], 2*m[1] - a[1]), optpts(2*m[0] - a[0], 2*m[1] - a[1]), "$B=2M-A$ coordinatewise.")
       for a, m in [((2, 3), (5, 7)), ((-1, 4), (3, 2)), ((6, -2), (1, 1)), ((0, 8), (-4, 5))]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Find the distance between $P{P(x1, y1)}$ and $Q{P(x2, y2)}$.", rf"$PQ=\sqrt{{({x2-x1})^2+({y2-y1})^2}}$", f"$PQ={c}$ units") for x1, y1, x2, y2, c in [(2, -1, 5, 3, 5), (-4, 3, 4, -12, 17), (1, 1, 8, 25, 25), (-5, -2, 7, 3, 13)]]
           + [QQ(f"Find the midpoint of the segment with endpoints ${P(x1, y1)}$ and ${P(x2, y2)}$.", rf"$\left(\frac{{{x1}+({x2})}}{{2}},\frac{{{y1}+({y2})}}{{2}}\right)$", f"Midpoint $={P(*m)}$")
              for x1, y1, x2, y2, m in [(-3, 7, 9, 1, (3, 4)), (4, -8, -2, 2, (1, -3)), (-7, -5, 3, 11, (-2, 3)), (6, 0, -10, 8, (-2, 4))]]
           + [QQ(f"The midpoint of $AB$ is $M{P(*m)}$ and $A={P(*a)}$. Find $B$.", f"$B=(2\\cdot{m[0]}-({a[0]}),\\ 2\\cdot{m[1]}-({a[1]}))$", f"$B={P(2*m[0] - a[0], 2*m[1] - a[1])}$")
              for a, m in [((1, 2), (4, 6)), ((-3, 5), (0, 1)), ((7, -4), (2, 3)), ((-6, -2), (-1, 4))]])
NCERT_C = ([QQ(f"Show that the points $A{P(*a)}$, $B{P(*b)}$ and $C{P(*c)}$ are the vertices of an isosceles triangle.", f"$AB^2={d2(a, b)}$", f"$BC^2={d2(b, c)}$, $CA^2={d2(c, a)}$", "Two sides are equal, so the triangle is isosceles")
            for a, b, c in [((0, 0), (4, 3), (8, 0)), ((1, 1), (5, 4), (9, 1)), ((-2, 0), (1, 4), (4, 0)), ((0, 2), (3, 6), (6, 2)), ((-3, -1), (0, 3), (3, -1)), ((2, -2), (5, 2), (8, -2))]]
           + [QQ(f"Find the point on the $x$-axis which is equidistant from $A{P(x0 - p, q)}$ and $B{P(x0 + p, -q)}$.", "Let the point be $(x, 0)$; set $PA^2=PB^2$", f"$(x-({x0-p}))^2+{q*q}=(x-{x0+p})^2+{q*q}$", f"$x={x0}$, point ${P(x0, 0)}$")
              for x0, p, q in [(2, 3, 4), (-1, 4, 2), (3, 5, 1), (0, 2, 6), (-4, 3, 5), (5, 1, 3)]]
           + [QQ(f"A rectangle has vertices $A{P(x, y)}$, $B{P(x + a, y)}$, $C{P(x + a, y + b)}$ and $D$. Find $D$ and the length of diagonal $AC$.", f"$D={P(x, y + b)}$", f"$AC=\\sqrt{{{a}^2+{b}^2}}$", f"$AC={c}$ units")
              for (a, b, c), (x, y) in zip(TRI[14:20], [(1, 1), (-2, 3), (0, -4), (3, 2), (-5, -1), (2, 0)])])
NCERT_D = ([QQ(f"Show that the points $A{P(*a)}$, $B{P(*b)}$, $C{P(*c)}$ and $D{P(*d)}$ taken in order form a parallelogram.", f"$AB^2={d2(a, b)}$, $DC^2={d2(d, c)}$: $AB=DC$", f"$BC^2={d2(b, c)}$, $AD^2={d2(a, d)}$: $BC=AD$", f"Midpoint of $AC={P(half(a[0] + c[0]), half(a[1] + c[1]))}$",
              f"Midpoint of $BD={P(half(b[0] + d[0]), half(b[1] + d[1]))}$", "Opposite sides equal and diagonals bisect each other: parallelogram")
            for a, b, c, d in [((0, 0), (4, 1), (6, 4), (2, 3)), ((1, 1), (5, 2), (7, 5), (3, 4)), ((-1, 0), (3, -1), (6, 2), (2, 3)), ((0, 1), (3, 0), (5, 3), (2, 4)), ((-2, -1), (2, -2), (4, 1), (0, 2)), ((1, -2), (6, -1), (8, 2), (3, 1))]]
           + [QQ(f"The vertices of a triangle are $A{P(*a)}$, $B{P(*b)}$, $C{P(*c)}$. Find the lengths of its three sides and its perimeter.", f"$AB=\\sqrt{{{d2(a, b)}}}={rt(d2(a, b))}$", f"$BC=\\sqrt{{{d2(b, c)}}}={rt(d2(b, c))}$", f"$CA=\\sqrt{{{d2(c, a)}}}={rt(d2(c, a))}$", f"Perimeter $={rt(d2(a, b)) + rt(d2(b, c)) + rt(d2(c, a))}$ units")
              for a, b, c in [((0, 0), (-9, 12), (-9, 0)), ((0, 0), (8, 6), (8, -6)), ((1, 1), (7, 9), (7, 1)), ((-2, 3), (3, 15), (-2, 15)), ((0, 0), (5, 12), (5, -12)), ((-1, -1), (3, 2), (-5, 2))]])

# ------------------------------------------------------------------ MEDIUM
def d_surd(p, q): return d2(p, q)
mA1 = [M4(f"The square of the distance between ${P(*p)}$ and ${P(*q)}$ is:", str(d2(p, q)), [str(d2(p, q) + k) for k in (2, -3, 5)], "Use $d^2=(x_2-x_1)^2+(y_2-y_1)^2$.")
       for p, q in [((1, 4), (-3, 2)), ((-5, 3), (2, -1)), ((0, -6), (4, 5)), ((7, 1), (-2, 9)), ((-4, -4), (3, 1))]]
mA2 = [M4(f"The midpoint of ${P(x1, y1)}$ and ${P(x2, y2)}$ is:", f"$({half(x1 + x2)},\\ {half(y1 + y2)})$", [f"$({half(x1 + x2 + 1)},\\ {half(y1 + y2)})$", f"$({half(x1 + x2)},\\ {half(y1 + y2 + 2)})$", f"$({half(x1 - x2)},\\ {half(y1 - y2)})$"], "Average the coordinates.")
       for x1, y1, x2, y2 in [(3, 2, 6, 7), (-5, 4, 2, 9), (7, -3, -2, 8), (4, 5, -1, -2)]]
mA3 = [M4(f"One end of a diameter of a circle is ${P(*a)}$ and the centre is ${P(*m)}$. The other end is:", TP(2*m[0] - a[0], 2*m[1] - a[1]), optpts(2*m[0] - a[0], 2*m[1] - a[1]), "The centre is the midpoint of a diameter.")
       for a, m in [((5, 1), (2, -1)), ((-3, 6), (0, 3)), ((8, -5), (4, 0)), ((-6, -2), (-2, 5)), ((1, 9), (-3, 4))]]
mA4 = [M4(f"The point on the $x$-axis equidistant from ${P(x0 - p, q)}$ and ${P(x0 + p, -q)}$ is:", TP(x0, 0), optpts(x0, 0), "Set $PA=PB$ with $P=(x,0)$.") for x0, p, q in [(3, 2, 5), (-2, 6, 3), (4, 3, 7), (-5, 1, 2)]]
mA5 = [M4(t, c, w, "Use the sign conditions on the coordinates.") for t, c, w in [
    ("If $ab>0$ and $a+b<0$, the point $(a, b)$ lies in:", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"]),
    ("If $ab<0$ and $b>0$, the point $(a, b)$ lies in:", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"]),
    ("If $a-b>0$ and $ab<0$, the point $(a, b)$ lies in:", "Quadrant IV", ["Quadrant I", "Quadrant II", "Quadrant III"]),
    ("If $ab>0$ and $a+b>0$, the point $(a, b)$ lies in:", "Quadrant I", ["Quadrant II", "Quadrant III", "Quadrant IV"])]]
mA6 = [nm(f"The perimeter of the triangle with vertices $(0, 0)$, ${P(a, 0)}$ and ${P(0, b)}$ is:", a + b + c, "Add the three side lengths.") for a, b, c in TRI[5:9]]
mA7 = [M4(f"The point ${P(a, b)}$ is reflected first in the $x$-axis and then in the $y$-axis. The final point is:", TP(-a, -b), optpts(-a, -b), "Both signs change.") for a, b in [(4, 9), (-6, 2), (8, -5), (-3, -7)]]
mA8 = [nm(f"The area of the rectangle with opposite vertices ${P(x1, y1)}$ and ${P(x2, y2)}$ and sides parallel to the axes is:", abs(x2 - x1) * abs(y2 - y1), "Area $=$ length $\\times$ breadth.") for x1, y1, x2, y2 in [(1, 2, 6, 5), (-3, 1, 4, 6), (0, -4, 9, 3), (-5, -5, -1, 2)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Find the distance between ${P(*p)}$ and ${P(*q)}$.", f"$d^2=({q[0]}-({p[0]}))^2+({q[1]}-({p[1]}))^2={d2(p, q)}$", f"$d={sur(d2(p, q))}$ units") for p, q in [((1, 1), (4, 5)), ((-2, 3), (2, 6)), ((0, 5), (-3, 1)), ((6, -2), (1, 10))]]
         + [QQ(f"Find the midpoint of the segment joining ${P(x1, y1)}$ and ${P(x2, y2)}$.", rf"$\left(\frac{{{x1}+({x2})}}{{2}},\frac{{{y1}+({y2})}}{{2}}\right)$", f"Midpoint $=({half(x1 + x2)},\\ {half(y1 + y2)})$") for x1, y1, x2, y2 in [(3, -4, 6, 7), (-5, 2, 2, 5), (7, 1, -4, -8), (1, 6, 4, -3)]]
         + [QQ(f"One end of a diameter is $A{P(*a)}$ and the centre of the circle is $O{P(*m)}$. Find the other end $B$.", "Centre is the midpoint of the diameter", f"$B={P(2*m[0] - a[0], 2*m[1] - a[1])}$") for a, m in [((9, 4), (3, -1)), ((-7, 2), (-1, 6)), ((0, -8), (5, -3)), ((4, 10), (-2, 3))]])
MED_C = ([QQ(f"Show that $A{P(*a)}$, $B{P(*b)}$, $C{P(*c)}$ are collinear.", f"$AB={k1}\\times{cc}={k1*cc}$ (direction $({u},{v})$)", f"$BC={k2}\\times{cc}={k2*cc}$", f"$AC={(k1+k2)*cc}=AB+BC$", "So the points are collinear")
           for (u, v, cc), k1, k2, (x, y) in zip([TRI[0], TRI[1], TRI[2], TRI[0], TRI[1], TRI[3]], [1, 2, 1, 3, 1, 2], [2, 1, 3, 1, 3, 1], [(1, 1), (-2, 0), (0, -3), (4, 2), (-1, -2), (2, 5)])
           for a, b, c in [((x, y), (x + k1 * u, y + k1 * v), (x + (k1 + k2) * u, y + (k1 + k2) * v))]]
         + [QQ(f"Find the values of $k$ for which the distance between $P{P('k', y)}$ and $Q{P(x, y + b)}$ is ${c}$ units.", f"$({x}-k)^2+{b*b}={c*c}$", f"$({x}-k)^2={a*a}$", f"$k={x - a}$ or $k={x + a}$")
            for (a, b, c), x, y in zip(TRI[:6], [2, -3, 5, 0, 4, -1], [1, 2, -2, 3, 0, 4])]
         + [QQ(f"The vertices of a triangle are $A{P(*a)}$, $B{P(*b)}$, $C{P(*c)}$. Show that it is an isosceles right-angled triangle.", f"$AB^2={d2(a, b)}$, $BC^2={d2(b, c)}$", f"$CA^2={d2(c, a)}$", "Two sides equal", "$AB^2+BC^2=CA^2$: right angle at $B$")
            for a, b, c in [((0, 0), (3, 3), (6, 0)), ((1, 2), (4, 5), (7, 2)), ((-2, 1), (1, 4), (4, 1)), ((0, -1), (2, 1), (4, -1)), ((-3, -3), (0, 0), (3, -3)), ((2, 0), (5, 3), (8, 0))]])
MED_D = ([QQ(f"The vertices of a rhombus are $A{P(h - a, k)}$, $B{P(h, k - b)}$, $C{P(h + a, k)}$, $D{P(h, k + b)}$. Show that all four sides are equal and the diagonals are unequal, so that it is a rhombus and not a square.",
             f"$AB^2={a*a}+{b*b}={c*c}$", f"$BC^2=DA^2=CD^2={c*c}$: all sides equal ${c}$", f"$AC=2\\times{a}={2*a}$", f"$BD=2\\times{b}={2*b}$", f"${2*a}\\ne{2*b}$, so not a square")
          for (a, b, c), h, k in zip([TRI[0], TRI[1], TRI[2], TRI[3], TRI[6], TRI[4]], [1, -2, 0, 3, -1, 2], [2, 1, -3, 0, 4, -2])]
          + [QQ(f"Show that the quadrilateral with vertices $A{P(*a)}$, $B{P(*b)}$, $C{P(*c)}$, $D{P(a[0] + c[0] - b[0], a[1] + c[1] - b[1])}$ is a parallelogram and find the midpoint of the diagonals.",
                f"$D=A+C-B={P(a[0] + c[0] - b[0], a[1] + c[1] - b[1])}$", f"Midpoint of $AC={P(half(a[0] + c[0]), half(a[1] + c[1]))}$", f"Midpoint of $BD={P(half(a[0] + c[0]), half(a[1] + c[1]))}$ (same point)", "Diagonals bisect each other", "Hence $ABCD$ is a parallelogram")
             for a, b, c in [((0, 0), (5, 1), (7, 6)), ((1, 2), (6, 3), (8, 8)), ((-2, 1), (3, 0), (5, 5)), ((2, -1), (7, 0), (10, 4)), ((-3, -2), (1, -3), (4, 2)), ((0, 3), (4, 2), (7, 7))]])

# ------------------------------------------------------------------ HARD
hA1 = [nm(f"The area of the triangle with vertices $(0, 0)$, ${P(a, 0)}$ and ${P(0, b)}$ is:", a * b // 2, "Area $=\\frac12\\times a\\times b$.") for a, b in [(10, 14), (18, 8), (13, 6), (24, 7)]]
hA2 = [nm(f"The distance of the circumcentre of the right triangle with vertices $(0, 0)$, ${P(2*a, 0)}$ and ${P(0, 2*b)}$ from the origin is:", c, "The circumcentre is the midpoint of the hypotenuse; its distance from the right-angle vertex is half the hypotenuse.") for a, b, c in TRI[:4]]
hA3 = [nm(f"A circle has diameter with endpoints ${P(x1, y1)}$ and ${P(x1 + 2*a, y1 + 2*b)}$. Its radius is:", c, "Radius $=\\frac12\\times$ distance between the endpoints.") for (a, b, c), (x1, y1) in zip(TRI[10:14], [(1, -2), (-3, 4), (0, 0), (2, 2)])]
hA4 = [M4(f"The point on the $y$-axis equidistant from ${P(p, y0 - q)}$ and ${P(-p, y0 + q)}$ is:", TP(0, y0), optpts(0, y0), "Set $PA=PB$ with $P=(0,y)$.") for p, q, y0 in [(4, 3, 2), (6, 1, -3), (2, 5, 4), (3, 3, -1)]]
hA5 = [nm(f"If the distance between ${P('x', y)}$ and ${P(x0, y + b)}$ is ${c}$ and $x>{x0}$, then $x=$", x0 + a, "Solve $(x-x_0)^2+b^2=c^2$ and take the larger root.")
       for (a, b, c), x0, y in zip(TRI[:4], [1, -2, 3, 0], [2, 1, -4, 5])]
hA6 = [M4(f"The fourth vertex of the parallelogram with consecutive vertices ${P(*a)}$, ${P(*b)}$, ${P(*c)}$ (in order) is:", TP(a[0] + c[0] - b[0], a[1] + c[1] - b[1]), optpts(a[0] + c[0] - b[0], a[1] + c[1] - b[1]), "$D=A+C-B$.")
       for a, b, c in [((1, 1), (4, 2), (6, 5)), ((-2, 3), (2, 1), (5, 4)), ((0, -1), (3, -2), (5, 2)), ((2, 2), (7, 1), (9, 6))]]
hA7 = [nm(f"A point $P(x, 0)$ on the $x$-axis is ${c}$ units from ${P(a0, b)}$ with $x>{a0}$. The value of $x$ is:", a0 + a, "Solve $(x-a_0)^2+b^2=c^2$.") for (a, b, c), a0 in zip(TRI[4:8], [-3, 1, 0, -6]) ]
hA8 = [M4(t, c, w, "Reason with coordinates.") for t, c, w in [
    ("The points $(a, 0)$, $(0, a)$ and $(0, 0)$ form a triangle which is:", "isosceles right-angled", ["equilateral", "scalene", "obtuse-angled"]),
    ("The points $(2, 3)$, $(2, 8)$ and $(2, -1)$ are:", "collinear, on a vertical line", ["collinear, on a horizontal line", "vertices of a triangle", "vertices of a rectangle"]),
    ("The points $(-4, 5)$, $(0, 5)$ and $(7, 5)$ lie on a:", "horizontal line", ["vertical line", "line through the origin", "line in Quadrant III only"]),
    ("A point $(x, y)$ with $y=-x$ and $x>0$ lies in:", "Quadrant IV", ["Quadrant I", "Quadrant II", "Quadrant III"])]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"The vertices of a right triangle are $O{P(0, 0)}$, $A{P(2*a, 0)}$ and $B{P(0, 2*b)}$. Find the circumcentre and the circumradius.", f"Circumcentre is the midpoint of $AB={P(a, b)}$", f"Radius $=OM=\\sqrt{{{a*a}+{b*b}}}={c}$") for a, b, c in TRI[:4]]
          + [QQ(f"The end points of a diameter of a circle are $A{P(*p)}$ and $B{P(p[0] + 2*a, p[1] + 2*b)}$. Find the centre and the radius.", f"Centre $={P(p[0] + a, p[1] + b)}$", f"$AB=2\\sqrt{{{a*a}+{b*b}}}={2*c}$, radius $={c}$") for (a, b, c), p in zip(TRI[4:8], [(1, 1), (-4, 2), (0, -5), (3, -3)])]
          + [QQ(f"Find the distance between the points ${P(*p)}$ and ${P(*q)}$ and its square root form.", f"$d^2=({q[0]-p[0]})^2+({q[1]-p[1]})^2={d2(p, q)}$", f"$d={sur(d2(p, q))}$") for p, q in [((-7, 4), (2, -8)), ((5, -9), (-1, 2)), ((-3, -6), (6, 6)), ((8, 8), (-8, -4))]])
HARD_C = ([QQ(f"Find the points on the $x$-axis whose distance from $A{P(a0, b)}$ is ${c}$ units.", f"Let the point be $(x,0)$: $(x{sgn(-a0)})^2+{b*b}={c*c}$", f"$(x{sgn(-a0)})^2={a*a}$", f"$x={a0 + a}$ or $x={a0 - a}$") for (a, b, c), a0 in zip(TRI[8:14], [2, -1, 4, 0, -5, 3])]
          + [QQ(f"Three vertices of a rectangle $ABCD$ are $A{P(*A)}$, $B{P(A[0] + m*3, A[1] + m*4)}$ and $D{P(A[0] - n*4, A[1] + n*3)}$. Find $C$ and the diagonal $AC$.",
                f"$C=B+D-A={P(A[0] + 3*m - 4*n, A[1] + 4*m + 3*n)}$", f"$AB={5*m}$, $AD={5*n}$", f"$AC=\\sqrt{{{25*m*m}+{25*n*n}}}={5 * rt(m*m + n*n)}$")
             for A, m, n in [((0, 0), 3, 4), ((1, 2), 4, 3), ((-2, 1), 6, 8), ((2, -3), 5, 12), ((0, 4), 8, 6), ((-1, -1), 12, 5)]]
          + [QQ(f"Find the length of the median $AD$ of the triangle with $A{P(0, 0)}$, $B{P(2*a, 0)}$, $C{P(0, 2*b)}$, where $D$ is the midpoint of $BC$.", f"$D={P(a, b)}$", f"$AD=\\sqrt{{{a*a}+{b*b}}}$", f"$AD={c}$ units") for a, b, c in TRI[14:20]])
HARD_D = ([QQ(f"Show that $A{P(*A)}$, $B{P(A[0] + a, A[1] + b)}$, $C{P(A[0] + a - b, A[1] + b + a)}$, $D{P(A[0] - b, A[1] + a)}$ are the vertices of a square. Find its side, diagonal squared and area.",
              f"$AB^2=BC^2=CD^2=DA^2={a*a + b*b}$", f"Side $={c}$", f"$AC^2=({a - b})^2+({a + b})^2={2*c*c}$", f"$AC^2=BD^2={2*c*c}$: equal diagonals", f"Area $={c}^2={c*c}$ square units")
           for (a, b, c), A in zip(TRI[:6], [(0, 0), (1, -1), (-2, 3), (4, 0), (-1, -2), (0, 5)])]
          + [QQ(f"The point $P(x, 0)$ is equidistant from $A{P(x0 - p, q)}$ and $B{P(x0 + p, -q)}$. Find $P$ and the distance $PA$.", "$PA^2=PB^2$ with $P=(x, 0)$", f"$x={x0}$, so $P={P(x0, 0)}$", f"$PA^2={p*p}+{q*q}={p*p + q*q}$", f"$PA={sur(p*p + q*q)}$ units")
             for x0, p, q in [(6, 3, 4), (-5, 5, 12), (7, 8, 6), (-8, 7, 24), (10, 4, 3), (-3, 12, 5)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
