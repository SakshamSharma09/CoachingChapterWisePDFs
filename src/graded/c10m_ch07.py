"""Class 10 Maths Ch 7 - Coordinate Geometry (graded banks)."""
from mg import *

SLUG, NAME, CHNO = "Coordinate_Geometry", "Coordinate Geometry", 7

def pt(p): return f"({t(p[0])},\\,{t(p[1])})"
def d2(p, q): return (F(p[0]) - q[0]) ** 2 + (F(p[1]) - q[1]) ** 2
def dist_tex(p, q):
    s = d2(p, q)
    if s.denominator == 1 and isqrt(int(s)) ** 2 == s: return str(isqrt(int(s)))
    return f"\\sqrt{{{t(s)}}}"
def mid(p, q): return (F(p[0] + q[0], 2), F(p[1] + q[1], 2))
def sect(p, q, m, n): return ((n * F(p[0]) + m * q[0]) / (m + n), (n * F(p[1]) + m * q[1]) / (m + n))
def area(p, q, r): return abs(F(p[0]) * (q[1] - r[1]) + F(q[0]) * (r[1] - p[1]) + F(r[0]) * (p[1] - q[1])) / 2
def PM(p, q):  # option text of a point
    return f"${pt((F(p[0]),F(p[1])))}$"

def DIST(p, q):
    s = d2(p, q)
    return Q(f"Find the distance between the points ${pt(p)}$ and ${pt(q)}$.", f"$d=\\sqrt{{(x_2-x_1)^2+(y_2-y_1)^2}}$ (1); $=\\sqrt{{({t(F(q[0])-p[0])})^2+({t(F(q[1])-p[1])})^2}}=\\sqrt{{{t(s)}}}$ (1); $={dist_tex(p,q)}$ units (1).", "1+1+1")
def MIDQ(p, q):
    return Q(f"Find the midpoint of the segment joining ${pt(p)}$ and ${pt(q)}$.", f"Midpoint $=\\left(\\frac{{x_1+x_2}}{{2}},\\frac{{y_1+y_2}}{{2}}\\right)$ (1); $={pt(mid(p,q))}$ (1).", "1+1")
def SECT(p, q, m, n):
    return Q(f"Find the coordinates of the point which divides the join of ${pt(p)}$ and ${pt(q)}$ internally in the ratio ${m}:{n}$.", f"Section formula $\\left(\\frac{{mx_2+nx_1}}{{m+n}},\\frac{{my_2+ny_1}}{{m+n}}\\right)$ (1); $x=\\frac{{{m}({t(q[0])})+{n}({t(p[0])})}}{{{m+n}}}={t(sect(p,q,m,n)[0])}$ (1); $y={t(sect(p,q,m,n)[1])}$ (1).", "1+1+1")
def AREAQ(p, q, r):
    return Q(f"Find the area of the triangle with vertices ${pt(p)}$, ${pt(q)}$ and ${pt(r)}$.", f"Area $=\\frac12|x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)|$ (1); $=\\frac12|{t(F(p[0])*(q[1]-r[1]))}{sg(F(q[0])*(r[1]-p[1]))}{sg(F(r[0])*(p[1]-q[1]))}|$ (1); $={t(area(p,q,r))}$ sq. units (1).", "1+1+1")
def COLL(p, q, kx, ky_known):
    # points p, q and (kx, k) collinear : k found
    k = F(p[1]) + (F(q[1]) - p[1]) * (F(kx) - p[0]) / (F(q[0]) - p[0])
    return Q(f"Find the value of $k$ for which the points ${pt(p)}$, ${pt(q)}$ and $({kx},\\,k)$ are collinear.", f"Area of triangle must be 0 (1); $\\frac12|{t(p[0])}({t(q[1])}-k)+{t(q[0])}(k-{t(p[1])})+{kx}({t(p[1])}-{t(q[1])})|=0$ (1); $k={t(k)}$ (1).", "1+1+1")
def EQUI(p, q):
    x = (F(q[0]) ** 2 + F(q[1]) ** 2 - F(p[0]) ** 2 - F(p[1]) ** 2) / (2 * (F(q[0]) - p[0]))
    return Q(f"Find the point on the $x$-axis which is equidistant from ${pt(p)}$ and ${pt(q)}$.", f"Let the point be $(x,0)$; $(x-{t(p[0])})^2+{t(F(p[1])**2)}=(x-{t(q[0])})^2+{t(F(q[1])**2)}$ (2); $x={t(x)}$ (2); point $({t(x)},0)$ (1).", "2+2+1")
def XRATIO(p, q):
    r = -F(p[1]) / q[1]
    return Q(f"In what ratio does the $x$-axis divide the segment joining ${pt(p)}$ and ${pt(q)}$? Find the point of division.", f"Let ratio $m:n$; $y=\\frac{{m({t(q[1])})+n({t(p[1])})}}{{m+n}}=0$ (2); $m:n={t(r)}:1$, i.e. {r.numerator}:{r.denominator} (1); point $x=\\frac{{{r.numerator}({t(q[0])})+{r.denominator}({t(p[0])})}}{{{r.numerator+r.denominator}}}={t((r.numerator*F(q[0])+r.denominator*F(p[0]))/(r.numerator+r.denominator))}$ (2).", "2+1+2")
def PARA(a, b, c):
    d = (F(a[0]) + c[0] - b[0], F(a[1]) + c[1] - b[1])
    return Q(f"Three vertices of a parallelogram $ABCD$ taken in order are $A{pt(a)}$, $B{pt(b)}$ and $C{pt(c)}$. Find the fourth vertex $D$.", f"Diagonals bisect each other: midpoint of $AC=$ midpoint of $BD$ (1); $\\left({t(mid(a,c)[0])},{t(mid(a,c)[1])}\\right)$ (1); $D=(x_a+x_c-x_b,\\ y_a+y_c-y_b)={pt(d)}$ (2).", "1+1+2") if False else \
        Q(f"Three vertices of a parallelogram $ABCD$ taken in order are $A{pt(a)}$, $B{pt(b)}$ and $C{pt(c)}$. Find the fourth vertex $D$.", f"Diagonals bisect each other: midpoint of $AC$ is $\\left({t(mid(a,c)[0])},{t(mid(a,c)[1])}\\right)$ (2); this is also the midpoint of $BD$ (1); $D={pt(d)}$ (2).", "2+1+2")
def CENT(a, b, c):
    return Q(f"Find the centroid of the triangle with vertices ${pt(a)}$, ${pt(b)}$ and ${pt(c)}$.", f"Centroid $=\\left(\\frac{{x_1+x_2+x_3}}{{3}},\\frac{{y_1+y_2+y_3}}{{3}}\\right)$ (1); $={pt(((F(a[0])+b[0]+c[0])/3,(F(a[1])+b[1]+c[1])/3))}$ (2).", "1+2")
def ISOS(a, b, c):
    da, db, dc = d2(a, b), d2(b, c), d2(a, c)
    return Q(f"Show that the points ${pt(a)}$, ${pt(b)}$ and ${pt(c)}$ are the vertices of an isosceles triangle.", f"$AB^2={t(da)}$, $BC^2={t(db)}$, $CA^2={t(dc)}$ (2); two sides are equal (1); hence isosceles (1).", "2+1+1")
def YPT(x1, y1, x2, yv, dd):
    # point (x2, y) at distance dd from (x1,y1)
    return Q(f"Find the values of $y$ for which the distance between $P({x2},\\,y)$ and $Q({x1},\\,{y1})$ is {dd} units.", f"$({x2-x1})^2+(y-{y1})^2={dd*dd}$ (1); $(y-{y1})^2={dd*dd-(x2-x1)**2}$ (1); $y={y1}\\pm{isqrt(dd*dd-(x2-x1)**2)}$, i.e. $y={y1+isqrt(dd*dd-(x2-x1)**2)}$ or ${y1-isqrt(dd*dd-(x2-x1)**2)}$ (1).", "1+1+1")

# ---------------- EASY ----------------
P5 = [((0, 0), (3, 4)), ((1, 2), (4, 6)), ((-2, 1), (1, 5)), ((2, -1), (10, 5)), ((-3, -2), (2, 10)), ((5, 5), (8, 9)), ((-4, 3), (2, 11)), ((6, -2), (14, 13))]
eA = [[MN(f"The distance of the point $({a},{b})$ from the origin is:", isqrt(a * a + b * b), why="$\\sqrt{x^2+y^2}$") for a, b in [(3, 4), (5, 12), (8, 15), (6, 8), (20, 21)]],
      [MS(f"The midpoint of the join of ${pt(p)}$ and ${pt(q)}$ is:", PM(mid(p, q), 0)[:], [PM((mid(p, q)[0] + 1, mid(p, q)[1]), 0), PM((mid(p, q)[0], mid(p, q)[1] + 1), 0), PM((p[0] + q[0], p[1] + q[1]), 0)], "Average the coordinates") for p, q in [((2, 4), (6, 8)), ((0, 0), (8, 6)), ((-2, 3), (4, 7)), ((1, 5), (9, 1)), ((-4, -2), (2, 6))]],
      [MS(f"The point $({a},{b})$ lies in the:", q_, [x for x in ["first quadrant", "second quadrant", "third quadrant", "fourth quadrant"] if x != q_], "Signs of coordinates") for a, b, q_ in [(3, 4, "first quadrant"), (-2, 5, "second quadrant"), (-3, -1, "third quadrant"), (4, -6, "fourth quadrant"), (7, 2, "first quadrant")]],
      [MS(f"The coordinates of the point on the $x$-axis at distance {abs(a)} from the origin on the {'right' if a>0 else 'left'} are:", f"${pt((a,0))}$", [f"${pt((0,a))}$", f"${pt((-a,0))}$", f"${pt((a,a))}$"], "$y=0$ on the $x$-axis") for a in [3, -4, 5, -7, 6]],
      [MN(f"The distance between $({a},0)$ and $(0,{b})$ is (a={a}, b={b}):", isqrt(a * a + b * b), why="Distance formula") for a, b in [(6, 8), (5, 12), (9, 12), (8, 15), (7, 24)]],
      [MS(f"The abscissa of the point $({a},{b})$ is:", str(a), [str(b), str(a + b), str(-a)], "Abscissa is the $x$-coordinate") for a, b in [(5, 2), (7, -3), (-4, 9), (6, 1), (8, -2)]]]
eB = ([DIST(p, q) for p, q in P5[:4]] + [MIDQ(p, q) for p, q in [((2, 6), (8, 10)), ((-4, 3), (6, -1)), ((0, 5), (10, 15)), ((7, -2), (-3, 4))]]
      + [Q(f"Name the quadrant of the point $({a},{b})$ and the coordinates of its reflection in the $x$-axis.", f"Quadrant {q_} (1); reflection $({a},{-b})$ (1).", "1+1") for a, b, q_ in [(3, 5, "I"), (-4, 2, "II"), (-6, -3, "III"), (5, -4, "IV")]])
eC = ([DIST(p, q) for p, q in P5[2:]] + [MIDQ(p, q) for p, q in [((1, 7), (9, 3)), ((-6, -2), (4, 8)), ((3, -5), (11, 7)), ((0, 0), (-6, 10)), ((2, 2), (12, 6)), ((-1, 8), (5, -4))]]
      + [SECT(p, q, m, n) for p, q, m, n in [((0, 0), (6, 9), 1, 2), ((2, 1), (8, 7), 1, 1), ((1, 3), (11, 8), 2, 3), ((0, 4), (10, 14), 3, 2), ((-2, 0), (4, 6), 1, 2), ((1, 1), (9, 5), 3, 1)]])
eD = ([AREAQ(*p) for p in [((0, 0), (4, 0), (0, 3)), ((1, 1), (5, 1), (3, 6)), ((2, 3), (6, 3), (4, 8)), ((0, 0), (6, 0), (3, 5)), ((-1, 0), (3, 0), (1, 6)), ((1, 2), (5, 2), (2, 7))]]
      + [CENT(*p) for p in [((0, 0), (6, 0), (0, 9)), ((1, 2), (4, 6), (7, 4)), ((-3, 1), (3, 5), (6, 0)), ((2, 2), (8, 4), (5, 9)), ((0, 3), (6, 3), (3, 9)), ((-2, -1), (4, 5), (1, 8))]])

# ---------------- NCERT ----------------
nA = [[MN(f"The distance between $({x1},{y1})$ and $({x2},{y2})$ is:", isqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), why="Distance formula") for x1, y1, x2, y2 in [(2, 3, 5, 7), (-1, 2, 4, 14), (0, 0, 9, 12), (3, -2, 11, 4), (-5, -1, 7, 4)]],
      [MS(f"The point which divides the join of $({x1},{y1})$ and $({x2},{y2})$ in the ratio 1:2 internally is:", PM(sect((x1, y1), (x2, y2), 1, 2), 0), [PM(sect((x1, y1), (x2, y2), 2, 1), 0), PM(mid((x1, y1), (x2, y2)), 0), PM((x2, y2), 0)], "Section formula") for x1, y1, x2, y2 in [(0, 0, 6, 9), (3, 3, 9, 12), (-3, 0, 6, 6), (1, 2, 7, 11), (0, 6, 9, 0)]],
      [MN(f"The area of the triangle with vertices $(0,0)$, $({a},0)$ and $(0,{b})$ is:", F(a * b, 2), why="$\\frac12\\times$ base $\\times$ height") for a, b in [(4, 6), (8, 5), (10, 3), (7, 6), (9, 4)]],
      [MN(f"If the midpoint of $({a},{b})$ and $(x,y)$ is $({m},{n})$, then $x=$", 2 * m - a, why="$x=2m-a$") for a, b, m, n in [(2, 3, 5, 6), (4, 1, 7, 2), (-2, 5, 3, 4), (6, 0, 1, 1), (3, -4, 8, 5)]],
      [MN(f"The distance of $({a},{b})$ from the $y$-axis is:", abs(a), why="Distance from $y$-axis $=|x|$") for a, b in [(5, 3), (-7, 2), (9, -4), (-6, 6), (8, 1)]],
      [MN(f"The point $({x},0)$ is equidistant from $({a},{b})$ and $({c},{d})$ for $x=$", F(c * c + d * d - a * a - b * b, 2 * (c - a)), why="Equate the squared distances") for a, b, c, d, x in [(2, 3, 6, 1, 0), (1, 4, 5, 2, 0), (0, 3, 8, 1, 0), (3, 2, 9, 4, 0), (2, 5, 8, 3, 0)]]]
nB = ([DIST(p, q) for p, q in [((2, 3), (4, 1)), ((-5, 7), (-1, 3)), ((6, -2), (1, 10)), ((0, 5), (12, 0))]] + [SECT(p, q, m, n) for p, q, m, n in [((4, -3), (8, 5), 3, 1), ((-1, 7), (4, -3), 2, 3), ((2, 5), (10, 1), 1, 3), ((-4, 0), (6, 5), 2, 3)]]
      + [YPT(*p) for p in [(2, -3, 10, 0, 10), (4, 1, 10, 0, 10), (0, 2, 6, 0, 10), (3, 5, 11, 0, 10)]])
nC = ([COLL(p, q, kx, 0) for p, q, kx in [((1, 2), (3, 6), 5), ((2, 1), (4, 5), 6), ((-1, 3), (1, 7), 3), ((0, 1), (3, 7), 4), ((1, -1), (3, 5), 4), ((2, 3), (6, 7), 8)]]
      + [AREAQ(*p) for p in [((1, 1), (4, 5), (7, 2)), ((2, 3), (-1, 0), (2, -4)), ((0, 2), (5, 6), (3, -1)), ((-3, 1), (3, 5), (1, -3)), ((4, 4), (8, 1), (1, 0)), ((1, -2), (5, 4), (7, 0))]]
      + [XRATIO(*p) for p in [((-4, -6), (3, 8)), ((2, -3), (6, 9)), ((0, -4), (6, 8)), ((-2, -2), (4, 4)), ((1, -5), (7, 10)), ((3, -6), (9, 6))]])
nD = ([EQUI(*p) for p in [((7, 6), (-3, 4)), ((2, 3), (8, 1)), ((-1, 5), (5, 3)), ((4, 2), (-2, 6)), ((1, 7), (9, 1)), ((3, 2), (7, 8))]]
      + [PARA(*p) for p in [((1, 2), (4, 3), (5, 7)), ((2, 1), (6, 2), (7, 6)), ((-1, 0), (3, 1), (4, 5)), ((0, 3), (5, 4), (6, 9)), ((2, 4), (7, 5), (8, 10)), ((1, 1), (5, 2), (6, 6))]])

# ---------------- MEDIUM ----------------
mA = [[MN(f"The perimeter of the triangle with vertices $(0,0)$, $({a},0)$, $(0,{b})$ is:", a + b + c, why="Find the hypotenuse") for a, b, c in [(6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (7, 24, 25)]],
      [MN(f"The point which divides $({a},0)$ and $(0,{b})$ in the ratio 1:1 has coordinates summing to:", F(a + b, 2), why="Midpoint") for a, b in [(6, 10), (8, 4), (12, 6), (14, 2), (10, 10)]],
      [MN(f"The centroid of the triangle with vertices $({a},{b})$, $({c},{d})$, $({e},{f})$ has $x$-coordinate:", F(a + c + e, 3), why="$\\frac{x_1+x_2+x_3}{3}$") for a, b, c, d, e, f in [(1, 2, 4, 6, 7, 1), (0, 0, 6, 3, 3, 9), (2, 5, 8, 1, 5, 6), (-3, 2, 3, 4, 9, 0), (4, 4, 10, 2, 1, 6)]],
      [MN(f"A circle has centre $({a},{b})$ and passes through $({c},{d})$. Its radius is:", isqrt((a - c) ** 2 + (b - d) ** 2), why="Distance from centre") for a, b, c, d in [(1, 2, 4, 6), (0, 0, 5, 12), (-2, 3, 4, 11), (3, -1, 12, 11), (5, 5, 8, 9)]],
      [MN(f"The ratio in which $({a},{b})$-axis... " if False else f"The ratio $k:1$ in which the line $x={m}$ divides the join of $({a},0)$ and $({c},0)$, with $a<{m}<c$, has $k=$", F(m - a, c - m), why="$x=\\frac{kc+a}{k+1}=m$") for a, m, c in [(2, 5, 11), (1, 4, 10), (0, 3, 9), (-2, 2, 6), (3, 6, 15)]],
      [MN(f"If $({a},{b})$, $({c},{d})$ and $({e},k)$ are collinear, then $k=$", F(b) + F(d - b, c - a) * (e - a), why="Area $=0$") for a, b, c, d, e in [(1, 2, 3, 6, 5), (0, 1, 2, 5, 4), (2, 3, 4, 7, 6), (1, 0, 4, 6, 7), (-1, 1, 1, 5, 3)]]]
mB = ([YPT(*p) for p in [(1, 2, 7, 0, 10), (3, -1, 9, 0, 10), (2, 4, 14, 0, 13), (0, 0, 5, 0, 13)]] + [PARA(*p) for p in [((3, 1), (6, 2), (8, 6)), ((0, 0), (4, 1), (6, 5)), ((2, 2), (5, 3), (7, 7)), ((1, 4), (5, 5), (8, 9))]]
      + [CENT(*p) for p in [((3, 7), (9, 1), (6, 4)), ((0, 5), (6, 8), (3, -1)), ((2, 2), (8, 5), (5, 11)), ((-4, 3), (2, 9), (8, -3))]])
mC = ([ISOS(*p) for p in [((0, 0), (4, 0), (2, 3)), ((1, 1), (5, 1), (3, 5)), ((-2, 0), (2, 0), (0, 4)), ((3, 3), (9, 3), (6, 8)), ((0, 1), (6, 1), (3, 7)), ((2, -1), (8, -1), (5, 4))]]
      + [SECT(p, q, m, n) for p, q, m, n in [((-2, 3), (8, 13), 2, 3), ((1, -4), (7, 8), 3, 1), ((0, 0), (10, 15), 2, 3), ((5, 2), (-5, 12), 3, 2), ((4, 1), (-8, 13), 1, 3), ((-6, 4), (6, 10), 5, 1)]]
      + [AREAQ(*p) for p in [((2, 5), (6, 1), (8, 7)), ((-4, -2), (2, 4), (6, -4)), ((0, 4), (5, 0), (7, 9)), ((3, 6), (9, 2), (5, 10)), ((-1, 1), (5, 7), (3, -5)), ((1, 1), (7, 3), (4, 8))]])
mD = ([XRATIO(*p) for p in [((-3, -5), (6, 4)), ((1, -8), (4, 7)), ((-2, -3), (10, 9)), ((0, -6), (8, 10)), ((2, -4), (5, 8)), ((-1, -7), (3, 5))]]
      + [EQUI(*p) for p in [((1, 5), (7, 3)), ((-3, 2), (5, 6)), ((2, 8), (10, 2)), ((4, 5), (-2, 1)), ((0, 4), (6, 2)), ((3, 6), (11, 4))]])

# ---------------- HARD ----------------
def QUAD(a, b, c, d):
    return Q(f"Show that the points $A{pt(a)}$, $B{pt(b)}$, $C{pt(c)}$, $D{pt(d)}$ are the vertices of a {'rhombus' if d2(a,b)==d2(b,c) else 'parallelogram'}.", f"$AB^2={t(d2(a,b))}$, $BC^2={t(d2(b,c))}$, $CD^2={t(d2(c,d))}$, $DA^2={t(d2(d,a))}$ (2); " + (f"all four sides equal (1); diagonals $AC^2={t(d2(a,c))}$, $BD^2={t(d2(b,d))}$ differ so it is a rhombus, not a square (2)." if d2(a, b) == d2(b, c) else "opposite sides equal (1); diagonals bisect each other (2)."), "2+1+2")
hA = [[MN(f"The point on the $y$-axis equidistant from $({a},{b})$ and $({c},{d})$ has $y=$", F(c * c + d * d - a * a - b * b, 2 * (d - b)), why="Let the point be $(0,y)$") for a, b, c, d in [(2, 3, 6, 5), (1, 2, 5, 4), (3, 1, 7, 7), (0, 2, 4, 6), (2, 5, 8, 1)]],
      [MN(f"The area of the triangle formed by $({a},0)$, $(0,{b})$ and the origin, doubled, is:", a * b, why="Twice the area") for a, b in [(7, 9), (11, 4), (6, 13), (8, 15), (12, 5)]],
      [MN(f"If $P(x,y)$ is equidistant from $({a},{b})$ and $({c},{d})$ and lies on $y=0$, then $x=$", F(c * c + d * d - a * a - b * b, 2 * (c - a)), why="Equate squared distances") for a, b, c, d in [(1, 3, 7, 5), (2, 4, 8, 2), (0, 6, 10, 2), (3, 5, 9, 1), (4, 2, 12, 6)]],
      [MN(f"The ratio in which $({a},{b})$ and $({c},{d})$ are joined by the $y$-axis is {-a}:", c, why="$x=0$: $mc+na=0$") for a, b, c, d in [(-3, 2, 6, 5), (-2, 4, 8, 1), (-5, 0, 10, 3), (-4, 3, 12, 6), (-6, 1, 9, 7)]],
      [MN(f"The side of the square with diagonal endpoints $({a},{b})$ and $({c},{d})$ has squared length:", F(d2((a, b), (c, d)), 2), why="$s^2=d^2/2$") for a, b, c, d in [(0, 0, 6, 8), (1, 1, 7, 9), (2, 3, 8, 11), (0, 2, 10, 12), (-3, -1, 3, 7)]],
      [MN(f"The three points $({a},{b})$, $({c},{d})$ and $({e},{f})$ enclose area:", area((a, b), (c, d), (e, f)), why="Use the area formula") for a, b, c, d, e, f in [(0, 0, 8, 0, 3, 7), (1, 1, 9, 1, 4, 8), (2, 3, 12, 3, 6, 9), (0, 0, 10, 4, 4, 10), (1, 2, 11, 2, 5, 12)]]]
hB = ([QUAD(*p) for p in [((0, 0), (3, 4), (8, 4), (5, 0)), ((1, 2), (4, 6), (9, 6), (6, 2)), ((0, 0), (4, 3), (9, 3), (5, 0)), ((2, 1), (5, 5), (10, 5), (7, 1))]]
      + [COLL(p, q, kx, 0) for p, q, kx in [((1, 5), (2, 8), 4), ((-2, 3), (0, 7), 3), ((2, -3), (4, 1), 5), ((3, 2), (6, 8), 9)]]
      + [Q(f"The vertices of a triangle are ${pt(a)}$, ${pt(b)}$, ${pt(c)}$. Find the length of the median from the first vertex.", f"Midpoint of the opposite side $={pt(mid(b,c))}$ (1); length $={dist_tex(a,mid(b,c))}$ (1).", "1+1") for a, b, c in [((0, 0), (6, 0), (0, 8)), ((2, 2), (8, 2), (2, 10)), ((1, 1), (7, 1), (1, 9)), ((3, 0), (9, 0), (3, 8))]])
hC = ([QUAD(*p) for p in [((1, 1), (5, 4), (10, 4), (6, 1)), ((0, 0), (6, 8), (16, 8), (10, 0)), ((2, 3), (5, 7), (10, 7), (7, 3)), ((0, 1), (4, 4), (9, 4), (5, 1)), ((3, 0), (6, 4), (11, 4), (8, 0)), ((1, 0), (4, 4), (9, 4), (6, 0))]]
      + [Q(f"The line joining ${pt(a)}$ and ${pt(b)}$ is trisected by points $P$ and $Q$. Find their coordinates.", f"$P$ divides $AB$ in $1:2$: ${pt(sect(a,b,1,2))}$ (1.5); $Q$ divides $AB$ in $2:1$: ${pt(sect(a,b,2,1))}$ (1.5).", "1.5+1.5") for a, b in [((0, 0), (9, 6)), ((3, 3), (12, 9)), ((-3, 6), (6, 0)), ((1, -2), (10, 7)), ((2, 5), (11, -1)), ((0, 3), (12, 9))]]
      + [YPT(*p) for p in [(2, 3, 8, 0, 10), (5, 1, 17, 0, 13), (-1, 2, 7, 0, 10), (4, 4, 4, 0, 5) if False else (0, 0, 12, 0, 13), (3, 2, 11, 0, 10), (6, -1, 14, 0, 17)]])
hD = ([Q(f"The vertices of $\\triangle ABC$ are $A{pt(a)}$, $B{pt(b)}$ and $C{pt(c)}$. Find the coordinates of the centroid and the area of the triangle.", f"Centroid $={pt(((F(a[0])+b[0]+c[0])/3,(F(a[1])+b[1]+c[1])/3))}$ (2); area $=\\frac12|\\dots|={t(area(a,b,c))}$ sq. units (3).", "2+3") for a, b, c in [((0, 0), (12, 0), (6, 8)), ((1, 2), (7, 2), (4, 8)), ((2, 1), (10, 1), (6, 7)), ((3, 3), (9, 3), (6, 12)), ((0, 1), (8, 1), (4, 9)), ((-2, 0), (4, 0), (1, 6))]]
      + [PARA(*p) for p in [((-2, 1), (1, 0), (4, 3)), ((1, 5), (7, 3), (10, 9)), ((0, 2), (6, 1), (9, 7)), ((3, -2), (8, 0), (11, 6)), ((-4, 0), (2, -2), (5, 4)), ((2, 6), (9, 4), (12, 10))]])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
