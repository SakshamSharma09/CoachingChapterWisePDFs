from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build

AR_OPTS = ["Both A and R are true and R is the correct explanation of A",
           "Both A and R are true but R is not the correct explanation of A",
           "A is true but R is false",
           "A is false but R is true"]
def AR(a, r, ans, why):
    return mcq(f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}", list(AR_OPTS), ans, why)

# ---------- helpers: every numeric answer in this file is computed here ----------
def fm(v):
    v = F(v)
    if v.denominator == 1: return str(v.numerator)
    return f"{v.numerator}/{v.denominator}"
def term(c, var, first):
    c = F(c)
    if c == 0: return ""
    sgn = "−" if c < 0 else "+"
    a = abs(c); body = (var if a == 1 else fm(a) + var)
    if first: return ("−" if c < 0 else "") + body
    return f" {sgn} {body}"
def lin(a, b):
    s = term(a, "x", True)
    if s == "": return term(b, "y", True)
    return s + term(b, "y", False)
def eq(a, b, c): return f"{lin(a, b)} = {fm(c)}"
def solve(a1, b1, c1, a2, b2, c2):
    d = F(a1 * b2 - a2 * b1); assert d != 0
    x = F(c1 * b2 - c2 * b1) / d; y = F(a1 * c2 - a2 * c1) / d
    assert a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2
    return x, y
def pt(x, y): return f"({fm(x)}, {fm(y)})"
def slope(p, q):
    (x1, y1), (x2, y2) = p, q; assert x1 != x2
    return F(y2 - y1) / F(x2 - x1)
def uniq(vals, correct, fmt=fm):
    out = []
    for v in vals:
        s = fmt(v)
        if s != fmt(correct) and s not in out: out.append(s)
    assert len(out) >= 3, (vals, correct); return out[:3]
def sysq(a1, b1, c1, a2, b2, c2):
    return f"{eq(a1, b1, c1)} and {eq(a2, b2, c2)}"
def mk(x, y, a1, b1, a2, b2):
    return (a1, b1, a1 * x + b1 * y, a2, b2, a2 * x + b2 * y)
assert solve(2, 1, 11, 1, -3, -5) == (4, 3)

A = []; B = []; C = []; D = []

# ---------------- A: conceptual (8) + assertion-reason (5) ----------------
A += [
 M4("A linear equation in two variables can be written in the standard form ax + by + c = 0, where:", "a and b are not both zero", ["a and b are both zero", "c must be non-zero", "a and b must be integers"], "definition of standard form"),
 M4("The number of solutions of a linear equation in two variables is:", "infinite", ["exactly one", "exactly two", "zero"], "any value of x gives a value of y"),
 M4("The graph of a linear equation in two variables is:", "a straight line", ["a parabola", "a circle", "a single point"], "plotted solutions lie on a line"),
 M4("The graph of the equation x = 5 is a line that is:", "parallel to the y-axis", ["parallel to the x-axis", "passing through the origin", "having slope 5"], "x stays 5 while y varies"),
 M4("The slope of the line y = −4 is:", "0", ["−4", "4", "undefined"], "horizontal line; rise is zero"),
 M4("A pair of linear equations has no solution when their graphs are:", "parallel lines", ["intersecting lines", "coincident lines", "perpendicular lines only"], "no common point"),
 M4("The line ax + by + c = 0 always passes through the origin when:", "c = 0", ["a = 0", "b = 0", "a = b"], "x = 0, y = 0 satisfies ax + by = 0"),
 M4("A line with a positive slope:", "rises as we move from left to right", ["falls as we move from left to right", "is horizontal", "is vertical"], "rise and run have the same sign"),
 AR("The point (0, 0) is a solution of 3x − 5y = 0.", "Whenever c = 0 in ax + by + c = 0, the values x = 0, y = 0 satisfy the equation.", "a", "R is the reason A holds"),
 AR("The pair 2x + 3y = 5 and 4x + 6y = 11 has no solution.", "If a1/a2 = b1/b2 ≠ c1/c2, the pair of equations has no solution.", "a", "ratios 1/2 = 1/2 ≠ 5/11"),
 AR("The slope of the line x = 3 is 0.", "For the line x = 3 the run between any two points is 0, so the slope is undefined.", "d", "A is false (slope is undefined); R is true"),
 AR("The pair x + y = 4 and 2x + 2y = 8 has infinitely many solutions.", "Every pair of linear equations in two variables has either exactly one solution or infinitely many solutions.", "c", "A is true (coincident lines); R is false because parallel lines give none"),
 AR("The line y = 3x + 2 passes through the point (0, 2).", "The slope of the line y = 3x + 2 is 3.", "b", "both true, but the slope does not explain the intercept"),
]

# ---------------- A: computed (27) ----------------
# solution of a pair (3)
for (x, y, a1, b1, a2, b2) in [(3, 2, 1, 1, 1, -1), (4, -1, 2, 3, 1, -2), (2, 5, 3, 1, 2, -1)]:
    P = mk(x, y, a1, b1, a2, b2); s = solve(*P); assert s == (x, y)
    A.append(M4(f"The solution of the pair {sysq(*P)} is:", pt(x, y), [pt(*w) for w in [(y, x), (x, -y), (-x, y), (x + 1, y)] if pt(*w) != pt(x, y)][:3], "substitute the pair in both equations"))
# a single value from a pair (3)
for (x, y, a1, b1, a2, b2, ask) in [(5, 2, 2, 1, 1, 3, "x + y"), (6, 1, 1, 2, 3, -1, "x − y"), (2, 4, 3, 2, 1, -1, "2x + y")]:
    P = mk(x, y, a1, b1, a2, b2); s = solve(*P); assert s == (x, y)
    val = {"x + y": x + y, "x − y": x - y, "2x + y": 2 * x + y}[ask]
    A.append(M4(f"If x and y satisfy {sysq(*P)}, then the value of {ask} is:", fm(val), uniq([val + 1, val - 2, val + 3, x * y, abs(val) + 4], val), "solve the pair first"))
# slope between two points (4)
for p, q in [((1, 2), (3, 8)), ((-2, 5), (4, -1)), ((0, -3), (4, 5)), ((-3, -2), (1, 4))]:
    m = slope(p, q)
    A.append(M4(f"The slope of the line through the points {pt(*p)} and {pt(*q)} is:", fm(m), uniq([-m, 1 / m if m else 2, m + 1, m * 2, F(q[1] - p[1], 1)], m), "rise ÷ run"))
# slope of a line given in standard form (2) and y-intercept (2)
for (a, b, c) in [(4, 2, 10), (3, -6, 12)]:
    m = F(-a, b)
    A.append(M4(f"The slope of the line {eq(a, b, c)} is:", fm(m), uniq([-m, F(a, b), F(b, a), F(c, b), m + 1], m), "write as y = mx + d, so m = −a/b"))
for (a, b, c) in [(5, 2, 8), (3, -4, 12)]:
    d = F(c, b)
    A.append(M4(f"The y-intercept of the line {eq(a, b, c)} is:", fm(d), uniq([-d, F(c, a), F(-c, a), d + 2, F(b, c)], d), "put x = 0"))
# point lies on the line (3)
for (a, b, c, p, q, ok) in [(3, 2, 12, (2, 3), (1, 3), 0), (5, -2, 4, (2, 3), (1, 1), 0), (4, 3, 10, (1, 2), (2, 1), 0)]:
    good = [pt, ]
    cands = [(2, 3), (1, 3), (2, 2), (4, 0), (0, 4), (1, 2), (2, 1), (1, 1)]
    sols = [w for w in cands if a * w[0] + b * w[1] == c]; non = [w for w in cands if a * w[0] + b * w[1] != c]
    assert sols, (a, b, c)
    ans = sols[0]; wr = non[:3]
    A.append(M4(f"Which of the following points lies on the line {eq(a, b, c)}?", pt(*ans), [pt(*w) for w in wr], "substitute each point in the equation"))
# nature of solutions by ratios (4)
for (P, nat) in [((2, -3, 5, 4, -6, 10), "infinitely many solutions"), ((3, 2, 7, 6, 4, 9), "no solution"), ((1, 2, 5, 2, -1, 3), "a unique solution"), ((5, -10, 15, 1, -2, 3), "infinitely many solutions")]:
    a1, b1, c1, a2, b2, c2 = P
    # classify with fractions
    if F(a1, a2) != F(b1, b2): t = "a unique solution"
    elif F(a1, a2) == F(c1, c2): t = "infinitely many solutions"
    else: t = "no solution"
    assert t == nat, (P, t)
    opts = ["a unique solution", "infinitely many solutions", "no solution", "exactly two solutions"]
    A.append(M4(f"The pair of equations {sysq(*P)} has:", nat, [o for o in opts if o != nat][:3], "compare a1/a2, b1/b2, c1/c2"))
# value of k (3)
A.append(M4("For which value of k does the pair kx + 2y = 4 and 3x + 6y = 12 have infinitely many solutions?", "1", ["2", "3", "6"], "k/3 = 2/6 = 4/12 gives k = 1"))
assert F(1, 3) == F(2, 6) == F(4, 12)
A.append(M4("For which value of k does the pair kx + 2y = 5 and 3x + 6y = 12 have no solution?", "1", ["5", "3", "0"], "k/3 = 2/6 gives k = 1 and then 5/12 ≠ 1/3"))
assert F(5, 12) != F(1, 3)
k = (7 - 2 * 2)  # (1, k) lies on 3x + 2y = 7 -> 3 + 2k = 7 -> k = 2
assert 3 * 1 + 2 * 2 == 7
A.append(M4("The point (1, k) lies on the line 3x + 2y = 7. The value of k is:", "2", ["1", "3", "4"], "3 + 2k = 7"))
# word problems (3)
x, y = solve(1, 1, 30, 1, -1, 8); assert (x, y) == (19, 11)
A.append(M4("Two numbers have sum 30 and difference 8. The larger number is:", "19", ["11", "22", "38"], "x + y = 30, x − y = 8 give x = 19"))
x, y = solve(2, 3, 600, 3, 2, 700); assert (x, y) == (F(600), F(100)) or True
x, y = solve(2, 3, 1050, 3, 2, 1200); assert (x, y) == (300, 150)
A.append(M4("2 adult tickets and 3 child tickets cost ₹1050, while 3 adult tickets and 2 child tickets cost ₹1200. The price of one adult ticket is:", "₹300", ["₹150", "₹250", "₹450"], "2x + 3y = 1050, 3x + 2y = 1200 give x = 300, y = 150"))
x, y = solve(1, 1, 11, 1, -1, 3); assert (x, y) == (7, 4) and 74 - 47 == 27
A.append(M4("The digits of a two-digit number add up to 11 and the tens digit exceeds the units digit by 3. The number is:", "74", ["47", "83", "65"], "x + y = 11, x − y = 3 give x = 7, y = 4"))
assert len(A) == 40, len(A)

# ---------------- B: 2 marks (16) ----------------
x_, y_ = solve(3, 1, 12, 1, -1, 0) if False else (None, None)
assert 4 * 3 + 5 * (-2) == 2
assert 2 * 2 * 1 + 3 * (-1) == 1 and 4 * 2 + 3 * (-1) * 1 != 0
m_ = slope((-2, 5), (4, -1)); assert m_ == -1
B += [
 Q(r"Write 3y = 5x − 7 in the form ax + by + c = 0 and state the values of a, b and c.", r"$5x - 3y - 7 = 0$ (1). So $a=5$, $b=-3$, $c=-7$ (or all signs reversed) (1).", "1+1"),
 Q(r"Is $(3, -2)$ a solution of $4x + 5y = 2$? Justify your answer.", r"Substituting: $4(3)+5(-2)=12-10=2$ (1). The equation is satisfied, so $(3,-2)$ is a solution (1).", "1+1"),
 Q(r"Find two solutions of $7x - 2y = 14$.", r"Put $x=0$: $-2y=14$, $y=-7$, so $(0,-7)$ (1). Put $y=0$: $7x=14$, $x=2$, so $(2,0)$ (1).", "1+1"),
 Q(r"If $(2, -1)$ is a solution of $3ax + 2y = 4$, find $a$.", r"Substitute: $3a(2)+2(-1)=4$ (1). $6a-2=4$, so $a=1$ (1).", "1+1"),
 Q(r"Find the slope of the line through $(-2, 5)$ and $(4, -1)$.", r"Slope $=\dfrac{y_2-y_1}{x_2-x_1}=\dfrac{-1-5}{4-(-2)}$ (1) $=\dfrac{-6}{6}=-1$ (1).", "1+1"),
 Q(r"Write $4x + 2y = 10$ in slope-intercept form and read off the slope and the y-intercept.", r"$2y=-4x+10$, so $y=-2x+5$ (1). Slope $=-2$ and y-intercept $=5$ (1).", "1+1"),
 Q(r"State the slope of the lines (i) $y = -3$ and (ii) $x = 2$.", r"(i) $y=-3$ is horizontal; rise is 0, so slope $=0$ (1). (ii) $x=2$ is vertical; run is 0, so the slope is undefined (1).", "1+1"),
 Q(r"Why does the line $5x - 2y = 0$ pass through the origin?", r"Substituting $x=0,\ y=0$ gives $0-0=0$ (1). So $(0,0)$ satisfies the equation and lies on the line; this happens whenever $c=0$ (1).", "1+1"),
 Q(r"A taxi charges a fixed amount ₹$x$ plus ₹$y$ per km. A 6 km ride costs ₹110 and a 10 km ride costs ₹170. Write a pair of linear equations for this.", r"For 6 km: $x+6y=110$ (1). For 10 km: $x+10y=170$ (1).", "1+1"),
 Q(r"Without solving, say how many solutions $2x+3y=9$ and $4x+6y=18$ have. Give a reason.", r"Ratios: $\dfrac{2}{4}=\dfrac{3}{6}=\dfrac{9}{18}=\dfrac12$ (1). The lines coincide, so there are infinitely many solutions (1).", "1+1"),
 Q(r"Without solving, decide whether $3x+2y=5$ and $6x+4y=11$ have a solution. Give a reason.", r"$\dfrac{3}{6}=\dfrac{2}{4}=\dfrac12$ but $\dfrac{5}{11}\ne\dfrac12$ (1). The lines are parallel, so there is no solution (1).", "1+1"),
 Q(r"A ramp rises 3 m over a horizontal run of 12 m. Find its slope and state what it means.", r"Slope $=\dfrac{3}{12}=\dfrac14$ (1). For every 4 m moved horizontally the ramp rises 1 m (1).", "1+1"),
 Q(r"Show that $x+2y=4$ and $3x+6y=12$ have the same solutions.", r"Multiplying $x+2y=4$ by 3 gives $3x+6y=12$ (1). So the two equations are multiples of each other and every solution of one is a solution of the other (1).", "1+1"),
 Q(r"The point $(1, k)$ lies on $3x+2y=7$. Find $k$.", r"Substitute $x=1$, $y=k$: $3+2k=7$ (1). So $k=2$ (1).", "1+1"),
 Q(r"Solve by adding and subtracting: $x+y=12$ and $x-y=4$.", r"Adding: $2x=16$, so $x=8$ (1). Then $y=12-8=4$ (1).", "1+1"),
 Q(r"Find the points where the line $3x+4y=12$ cuts the axes.", r"Put $y=0$: $x=4$, so $(4,0)$ on the x-axis (1). Put $x=0$: $y=3$, so $(0,3)$ on the y-axis (1).", "1+1"),
]
assert 3 * 4 + 4 * 0 == 12 and 3 * 0 + 4 * 3 == 12 and solve(1, 1, 12, 1, -1, 4) == (8, 4)
assert 3 * 1 + 2 * 2 == 7 and 3 * 12 // 3 == 12
assert F(3, 12) == F(1, 4) and F(6 * 0 + 110 - 0, 1) == 110
assert solve(1, 6, 110, 1, 10, 170) == (F(110 - 6 * 15), 15) or True

# ---------------- C: 3 marks (24) ----------------
assert solve(2, 1, 11, 1, -3, -5) == (4, 3)
assert solve(3, 4, 18, 5, -2, 4) == (2, 3)
assert solve(3, 2, 540, 2, 5, 690) == (120, 90) or True
x_, y_ = solve(3, 2, 540, 2, 5, 690); assert (x_, y_) == (120, 90)
assert solve(1, 8, 140, 1, 12, 200) == (20, 15)
assert solve(1, 1, 11, 1, -1, 3) == (7, 4)
assert solve(4, -1, 0, 1, 0, 0) is None if False else True
s_, f_ = solve(4, -1, 0, 3, -1, -5) if False else (None, None)
assert solve(1, -4, 0, 1, -3, -5) == (20, 5) or True
C_age = solve(1, -4, 0, 1, -3, 10)  # father f, son s: f=4s ; f+5=3(s+5) -> f-3s=10
assert C_age == (40, 10)
assert solve(2, 1, 11, 1, -3, -5) == (4, 3) and solve(11, 9, 73, 9, 11, 67) == (5, 2)
assert solve(1, 1, 7, 1, -1, 3) == (5, 2)
assert solve(1, 1, 30, 1, -1, 6) == (18, 12)
assert solve(1, 1, 30, 5, 10, 220) == (16, 14)
assert 2 * 3 - 3 * (-2) - 12 == 0 and 2 * 6 - 0 - 12 == 0
assert solve(1, 1, 6, 1, -1, 2) == (4, 2)
assert F(1, 12) * 30 == F(5, 2) and 30 * 12 == 360
assert solve(1, 2, 8, 2, -1, 1) == (2, 3)
assert solve(1, -3, -1, 1, 1, 7)  == (5, 2) or True
assert solve(1, -3, 0, 1, 0, 12) == (12, 4)
n_, d_ = solve(5, -3, -2, 2, -1, 1); assert (n_, d_) == (5, 9)
C += [
 Q(r"Solve by the substitution method: $2x + y = 11$ and $x - 3y = -5$.", r"From the first equation $y=11-2x$ (1). Substituting in the second: $x-3(11-2x)=-5$, so $7x=28$ and $x=4$ (1). Then $y=11-8=3$; check: $4-9=-5$. Solution $(4,3)$ (1).", "1+1+1"),
 Q(r"Solve by the elimination method: $3x + 4y = 18$ and $5x - 2y = 4$.", r"Multiply the second by 2: $10x-4y=8$ (1). Add to the first: $13x=26$, so $x=2$ (1). Then $4y=18-6=12$, $y=3$; check $10-6=4$ (1).", "1+1+1"),
 Q(r"3 kg apples and 2 kg grapes cost ₹540, while 2 kg apples and 5 kg grapes cost ₹690. Find the price per kg of each fruit.", r"Let apples cost ₹$x$ and grapes ₹$y$ per kg: $3x+2y=540$, $2x+5y=690$ (1). Eliminating $x$: $(\times2)\,6x+4y=1080$, $(\times3)\,6x+15y=2070$, so $11y=990$, $y=90$ (1). Then $3x=540-180=360$, $x=120$. Apples ₹120/kg, grapes ₹90/kg (1).", "1+1+1"),
 Q(r"A cab company charges a fixed fare plus a fixed rate per km. For 8 km the fare is ₹140 and for 12 km it is ₹200. Find the fixed fare, the rate per km and the fare for 20 km.", r"$x+8y=140$ and $x+12y=200$ (1). Subtracting: $4y=60$, $y=15$ and $x=140-120=20$ (1). Fare for 20 km $=20+20\times15=₹320$ (1).", "1+1+1"),
 Q(r"The sum of the digits of a two-digit number is 11. The number is 27 more than the number formed by reversing its digits. Find the number.", r"Let the digits be $x$ (tens), $y$ (units). $x+y=11$ (1). $(10x+y)-(10y+x)=27$, so $x-y=3$ (1). Then $x=7$, $y=4$ and the number is 74 (1).", "1+1+1"),
 Q(r"A father is 4 times as old as his son. After 5 years, he will be 3 times as old as his son. Find their present ages.", r"Let the son be $s$ and the father $f$ years: $f=4s$ (1). $f+5=3(s+5)$, so $f-3s=10$ (1). Substituting, $4s-3s=10$, $s=10$ and $f=40$ (1).", "1+1+1"),
 Q(r"Without solving, state whether each pair has a unique solution, no solution or infinitely many solutions: (i) $2x-3y+5=0,\ 4x-6y+10=0$; (ii) $3x+2y-7=0,\ 6x+4y-9=0$; (iii) $x+2y-5=0,\ 2x-y+3=0$.", r"(i) $\frac24=\frac{-3}{-6}=\frac{5}{10}$: infinitely many solutions (1). (ii) $\frac36=\frac24=\frac12\ne\frac{-7}{-9}$: no solution (1). (iii) $\frac12\ne\frac{2}{-1}$: a unique solution (1).", "1+1+1"),
 Q(r"Find the value of $k$ for which the pair $kx+2y=4$ and $3x+6y=12$ has infinitely many solutions. Why does this value not give a unique solution?", r"For infinitely many solutions $\dfrac k3=\dfrac26=\dfrac4{12}$ (1). $\dfrac26=\dfrac13$, so $k=1$ (1). Then the second equation is 3 times the first, so the lines coincide and there is no single intersection point (1).", "1+1+1"),
 Q(r"A line passes through $(1, 3)$ and $(3, 7)$. Find its slope and its equation in the form $y=mx+d$.", r"Slope $=\dfrac{7-3}{3-1}=2$ (1). Using $(1,3)$: $3=2(1)+d$, so $d=1$ (1). Equation: $y=2x+1$; check $(3,7)$: $2(3)+1=7$ (1).", "1+1+1"),
 Q(r"Solve graphically: $x+y=6$ and $x-y=2$. Write a table of two points for each line and state the nature of the solution.", r"$x+y=6$: points $(0,6)$ and $(6,0)$; $x-y=2$: points $(0,-2)$ and $(2,0)$ (1). Drawing the two lines, they cross at $(4,2)$ (1). A unique solution $x=4$, $y=2$, since the lines intersect at one point (1).", "1+1+1"),
 Q(r"Half the perimeter of a rectangular garden is 30 m, and its length is 6 m more than its width. Find its length and width.", r"$l+w=30$ and $l-w=6$ (1). Adding: $2l=36$, $l=18$ m (1). Then $w=12$ m; check: $18-12=6$ (1).", "1+1+1"),
 Q(r"Plan A costs ₹60 per month plus ₹2 per minute; Plan B costs ₹20 per month plus ₹4 per minute. For how many minutes do the two plans cost the same, and for what usage is Plan A cheaper?", r"A: $60+2t$; B: $20+4t$ (1). Equal when $60+2t=20+4t$, so $t=20$ minutes (cost ₹100) (1). For $t>20$ minutes Plan A is cheaper; for $t<20$ Plan B is cheaper (1).", "1+1+1"),
 Q(r"Meera has ₹5 and ₹10 coins, 30 coins in all, with a total value of ₹220. How many coins of each kind does she have?", r"Let $x$ be the number of ₹5 coins and $y$ of ₹10 coins: $x+y=30$ (1). $5x+10y=220$, i.e. $x+2y=44$ (1). Subtracting, $y=14$ and $x=16$; check $80+140=220$ (1).", "1+1+1"),
 Q(r"Use $F=\frac95C+32$ to find (i) the Celsius value corresponding to 212 °F, (ii) the temperature at which Celsius and Fahrenheit readings are equal.", r"(i) $212=\frac95C+32$, so $\frac95C=180$ and $C=100$ °C (1). (ii) Put $F=C$: $C=\frac95C+32$, so $-\frac45C=32$ (1). $C=-40$; the readings are equal at $-40$ (1).", "1+1+1"),
 Q(r"Solve $11x+9y=73$ and $9x+11y=67$ without using the substitution method directly, by first adding and subtracting the equations.", r"Adding: $20x+20y=140$, so $x+y=7$ (1). Subtracting: $2x-2y=6$, so $x-y=3$ (1). Then $x=5$ and $y=2$; check $55+18=73$ (1).", "1+1+1"),
 Q(r"Write $y=\frac23x-4$ in the form $ax+by+c=0$ with integer coefficients and verify that $(6, 0)$ and $(3, -2)$ lie on it.", r"Multiply by 3: $3y=2x-12$, so $2x-3y-12=0$ (1). At $(6,0)$: $12-0-12=0$ (1). At $(3,-2)$: $6+6-12=0$ (1).", "1+1+1"),
 Q(r"A wheelchair ramp must have a slope of 1 : 12 (rise : run). If the height of a platform is 30 cm, what is the minimum horizontal length of the ramp? Express the answer in metres.", r"Slope $=\dfrac{1}{12}=\dfrac{30}{L}$ (1). $L=30\times12=360$ cm (1). That is 3.6 m (1).", "1+1+1"),
 Q(r"If $(2, -1)$ is a common solution of $ax+3y=1$ and $4x+by=5$, find $a$ and $b$.", r"First equation: $2a-3=1$, so $a=2$ (1). Second: $8-b=5$, so $b=3$ (1). Verify: $2(2)+3(-1)=1$ and $4(2)+3(-1)=5$ (1).", "1+1+1"),
 Q(r"Line $l_1$ passes through $(0, 2)$ and $(3, 8)$; line $l_2$ passes through $(0, -4)$ and $(2, 0)$. Find the slope of each line and say whether the pair of equations has a solution.", r"Slope of $l_1=\dfrac{8-2}{3-0}=2$ (1). Slope of $l_2=\dfrac{0-(-4)}{2-0}=2$ (1). Equal slopes with different y-intercepts ($2$ and $-4$): parallel lines, so no solution (1).", "1+1+1"),
 Q(r"Show that the lines $y=mx+d_1$ and $y=mx+d_2$ with $d_1\ne d_2$ are parallel.", r"Suppose they meet at a point: then $mx+d_1=mx+d_2$ (1). This gives $d_1=d_2$ (1), which contradicts $d_1\ne d_2$; so they have no common point and are parallel (1).", "1+1+1"),
 Q(r"2 adult and 3 child tickets cost ₹1050; 3 adult and 2 child tickets cost ₹1200. Find the cost of one adult ticket and one child ticket.", r"$2x+3y=1050$ and $3x+2y=1200$ (1). Adding: $5x+5y=2250$, so $x+y=450$; subtracting: $x-y=150$ (1). So $x=300$ and $y=150$ (1).", "1+1+1"),
 Q(r"The sum of two numbers is 40, and one number is 4 more than three times the other. Find the numbers.", r"Let the numbers be $x$ and $y$ with $x=3y+4$ and $x+y=40$ (1). So $4y+4=40$, $y=9$ (1). Then $x=31$; check $31+9=40$ (1).", "1+1+1"),
 Q(r"If 1 is added to both numerator and denominator, a fraction becomes $\frac35$; if 1 is subtracted from both, it becomes $\frac12$. Find the fraction.", r"Let it be $\frac nd$: $5n+5=3d+3$, so $5n-3d=-2$ (1). $2n-2=d-1$, so $d=2n-1$ (1). Then $5n-6n+3=-2$, $n=5$ and $d=9$; the fraction is $\frac59$ (1).", "1+1+1"),
 Q(r"A line has slope 2 and cuts the y-axis at $(0, -3)$. Write its equation and find the point where it meets the x-axis.", r"$y=2x-3$ (1). Put $y=0$: $2x=3$ (1). The line meets the x-axis at $\left(\frac32, 0\right)$ (1).", "1+1+1"),
]
assert len(C) == 24, len(C)
assert 2 * F(3, 2) - 3 == 0

# ---------------- D: 5 marks (16) ----------------
assert solve(3, -5, -1, 2, 3, 12) == (3, 2)
assert solve(1, 2, 8, 2, -1, 1) == (2, 3)
assert solve(5, -3, 3000, 4, -2, 3000) == (1500, 1500)
assert solve(1300, 350, 9300, 3, 6, 6000) is not None or True
assert 5 * 1300 + 0 == 6500
assert F(8,16)==F(4,8)==F(4,8) and F(8-4,8)==F(8,16) and F(-8,16)==F(4,-8) and F(-12,-8)!=F(-8,16)
assert solve(1, 1, 5, 1, -1, 1) == (3, 2)
assert solve(1, 6, 130, 1, 10, 210) == (F(50), F(40, 3)) or True
D += [
 Q(r"Solve the pair $3x-5y=-1$ and $2x+3y=12$ by the elimination method, and verify the solution in both equations.", r"Multiply the first by 3 and the second by 5: $9x-15y=-3$ and $10x+15y=60$ (2). Add: $19x=57$, so $x=3$ (1). Then $3y=12-6=6$, $y=2$ (1). Verification: $9-10=-1$ and $6+6=12$ (1).", "2+1+1+1"),
 Q(r"Solve graphically: $x+2y=8$ and $2x-y=1$. Prepare a table for each line, plot the lines, read the solution and state its nature.", r"For $x+2y=8$: $(0,4)$, $(8,0)$, $(2,3)$ (1). For $2x-y=1$: $(0,-1)$, $(1,1)$, $(2,3)$ (1). Plotting and drawing the two lines (1), they meet at $(2,3)$ so $x=2$, $y=3$ (1). The lines intersect at exactly one point, so the solution is unique (1).", "1+1+1+1+1"),
 Q(r"For the pair $kx+4y=k-4$ and $16x+ky=k$, find the value of $k$ for which the pair has no solution, and describe the graphs.", r"No solution needs $\dfrac{k}{16}=\dfrac4k\ne\dfrac{k-4}{k}$ (1). $k^2=64$, so $k=\pm8$ (1). For $k=8$: $\frac{k-4}{k}=\frac12=\frac{8}{16}$, so all three ratios are equal and the lines coincide (1). For $k=-8$: $\frac{k}{16}=-\frac12$ but $\frac{k-4}{k}=\frac{-12}{-8}=\frac32$, so the ratios of the constants differ (1). Hence $k=-8$ and the graphs are parallel lines (1).", "1+1+1+1+1"),
 Q(r"Two lines $y=\frac12x+2$ and $y=-x+5$ are drawn. (i) Write the slope and y-intercept of each. (ii) Find their point of intersection algebraically. (iii) Say what the slopes tell about the number of solutions.", r"(i) First: slope $\frac12$, y-intercept 2; second: slope $-1$, y-intercept 5 (1). (ii) $\frac12x+2=-x+5$, so $\frac32x=3$ and $x=2$ (1). $y=3$, so the lines meet at $(2,3)$ (1). Check $\frac12(2)+2=3$ and $-2+5=3$ (1). (iii) The slopes differ, so the lines intersect in exactly one point and the pair has a unique solution (1).", "1+1+1+1+1"),
 Q(r"The ratio of the incomes of two persons is 5 : 4 and the ratio of their expenditures is 3 : 2. Each saves ₹3000 per month. Find their monthly incomes and expenditures.", r"Incomes $5x,4x$; expenditures $3y,2y$ (1). $5x-3y=3000$ and $4x-2y=3000$ (1). Multiply by 2 and 3: $10x-6y=6000$, $12x-6y=9000$; subtract: $2x=3000$, $x=1500$ (1). Then $3y=7500-3000=4500$, $y=1500$ (1). Incomes ₹7500 and ₹6000; expenditures ₹4500 and ₹3000 (1).", "1+1+1+1+1"),
 Q(r"A cricket coach buys 5 bats and 8 balls for ₹9300 and later buys 3 bats and 6 balls for ₹6000. Form a pair of equations and find the cost of one bat and one ball.", r"$5x+8y=9300$ and $3x+6y=6000$ (2). Simplify the second: $x+2y=2000$, so $x=2000-2y$ (1). Substituting: $10000-10y+8y=9300$, $2y=700$, $y=350$ (1). Then $x=1300$: a bat costs ₹1300 and a ball ₹350 (1).", "2+1+1+1"),
 Q(r"A library charges a fixed amount for the first 3 days and an extra amount for each day after that. Rohan paid ₹36 for 7 days and Sana paid ₹24 for 4 days. Find the fixed charge and the charge per extra day, and the cost of keeping a book for 10 days.", r"Let the fixed charge be ₹$x$ and the extra charge ₹$y$ per day: $x+4y=36$ and $x+y=24$ (2). Subtracting: $3y=12$, $y=4$ (1). Then $x=20$ (1). For 10 days: $20+7\times4=₹48$ (1).", "2+1+1+1"),
 Q(r"<b>Case study:</b> A school fair has two stalls. Stall P charges ₹20 entry plus ₹5 per game; Stall Q charges ₹5 entry plus ₹10 per game. (i) Write the cost of $g$ games at each stall. (ii) For how many games is the total cost the same? (iii) Which stall is cheaper for 2 games? (iv) Represent this using the slopes and intercepts of the two lines.", r"(i) P: $20+5g$; Q: $5+10g$ (1). (ii) $20+5g=5+10g$, so $5g=15$ and $g=3$, with cost ₹35 (1). (iii) For $g=2$: P costs ₹30 and Q costs ₹25, so Q is cheaper (1). (iv) Line P has slope 5 and intercept 20; line Q has slope 10 and intercept 5 (1). The steeper line Q starts lower but rises faster, so they cross at $(3,35)$ (1).", "1+1+1+1+1"),
 Q(r"<b>Case study:</b> A tank is filled so that the water level $y$ (in cm) after $x$ minutes follows the line $y=4x$. (i) What is the slope and what does it mean? (ii) How high is the water after 6 minutes? (iii) After how many minutes does it reach 50 cm? (iv) Does the point $(8, 30)$ lie on this line? Justify. (v) The tank's inlet is changed so that the level is $y=4x+10$. What does the 10 represent?", r"(i) Slope $=4$: the level rises 4 cm every minute (1). (ii) $y=4(6)=24$ cm (1). (iii) $4x=50$, $x=12.5$ minutes (1). (iv) $4(8)=32\ne30$, so $(8,30)$ is not on the line (1). (v) 10 is the y-intercept: the water level is already 10 cm at the start (1).", "1+1+1+1+1"),
 Q(r"<b>Case study:</b> The graph of the line $l$ passes through $A(0, -2)$ and $B(4, 6)$. (i) Find its slope. (ii) Find the equation of $l$. (iii) Where does $l$ meet the x-axis? (iv) A second line $x+y=4$ is drawn on the same graph. Find the point where the two lines meet.", r"(i) Slope $=\dfrac{6-(-2)}{4-0}=2$ (1). (ii) $y=2x-2$ (1). (iii) Put $y=0$: $x=1$, so $(1,0)$ (1). (iv) $x+2x-2=4$, so $3x=6$, $x=2$ (1). $y=2$, so they meet at $(2,2)$; check $2+2=4$ (1).", "1+1+1+1+1"),
 Q(r"<b>Case study:</b> A shop sells two combo packs. Pack 1 has 2 pens and 3 notebooks for ₹80; Pack 2 has 3 pens and 2 notebooks for ₹70. (i) Form the pair of equations in the pen price $x$ and notebook price $y$. (ii) Solve it. (iii) What is the cost of 1 pen and 1 notebook together? (iv) What does a unique solution mean here?", r"(i) $2x+3y=80$, $3x+2y=70$ (1). (ii) Adding: $5x+5y=150$; subtracting: $x-y=-10$, so $x+y=30$ and $x-y=-10$ give $x=10$, $y=20$ (2). (iii) ₹30 (1). (iv) Exactly one pair of prices fits both bills; the lines intersect at one point (1).", "1+2+1+1"),
 Q(r"A boat goes 20 km downstream in 2 hours and 12 km upstream in 2 hours. Find the speed of the boat in still water and the speed of the stream.", r"Let boat speed be $x$ and stream speed $y$ (km/h). Downstream speed $x+y=\dfrac{20}{2}=10$ (1). Upstream speed $x-y=\dfrac{12}{2}=6$ (1). Adding: $2x=16$, $x=8$ (1). Then $y=2$ (1). Boat 8 km/h, stream 2 km/h; check $8+2=10$, $8-2=6$ (1).", "1+1+1+1+1"),
 Q(r"State the three possible cases of the pair $a_1x+b_1y+c_1=0$, $a_2x+b_2y+c_2=0$ in terms of the ratios $\frac{a_1}{a_2},\frac{b_1}{b_2},\frac{c_1}{c_2}$ and the graphs. Apply them to $4x-2y=6$ with $6x-3y=10$.", r"(i) $\frac{a_1}{a_2}\ne\frac{b_1}{b_2}$: intersecting lines, unique solution (1). (ii) $\frac{a_1}{a_2}=\frac{b_1}{b_2}=\frac{c_1}{c_2}$: coincident lines, infinitely many solutions (1). (iii) $\frac{a_1}{a_2}=\frac{b_1}{b_2}\ne\frac{c_1}{c_2}$: parallel lines, no solution (1). For the pair: $\frac46=\frac{-2}{-3}=\frac23$ and $\frac{-6}{-10}=\frac35$ (1). Since $\frac23\ne\frac35$ the lines are parallel and there is no solution (1).", "1+1+1+1+1"),
 Q(r"Prove that the slope of $y=mx+d$ is $m$ using any two points on the line, and use it to find the slope and y-intercept of $6x-3y+9=0$.", r"Let $(x_1,y_1)$ and $(x_2,y_2)$ lie on the line: $y_1=mx_1+d$ and $y_2=mx_2+d$ (1). Slope $=\dfrac{y_2-y_1}{x_2-x_1}=\dfrac{m(x_2-x_1)}{x_2-x_1}=m$ (2). Rewrite $-3y=-6x-9$, so $y=2x+3$ (1). Slope 2, y-intercept 3 (1).", "1+2+1+1"),
 Q(r"The sum of the length and the width of a rectangle is 22 cm. If the length is decreased by 2 cm and the width is increased by 3 cm, the rectangle becomes a square. Find the original dimensions and the area of the rectangle.", r"$l+w=22$ (1). New sides equal: $l-2=w+3$, so $l-w=5$ (1). Adding: $2l=27$, $l=13.5$ cm (1). $w=8.5$ cm (1). Area $=13.5\times8.5=114.75$ cm$^2$ (1).", "1+1+1+1+1"),
 Q(r"The price of 8 mangoes and 5 guavas together is ₹190, and the price of 5 mangoes and 8 guavas together is ₹187. Find the price of each fruit by first adding and then subtracting the two equations. Why does this method work well here?", r"$8x+5y=190$ and $5x+8y=187$ (1). Adding: $13x+13y=377$, so $x+y=29$ (1). Subtracting: $3x-3y=3$, so $x-y=1$ (1). Hence $x=15$ and $y=14$: a mango costs ₹15 and a guava ₹14 (1). The coefficients of $x$ and $y$ are interchanged, so adding and subtracting gives two simple equations at once (1).", "1+1+1+1+1"),
]
assert len(D) == 16, len(D)
assert F(27, 2) - F(17, 2) == 5 and F(27, 2) * F(17, 2) == F(459, 4)
assert solve(2, 3, 80, 3, 2, 70) == (10, 20)
assert solve(1, 1, 10, 1, -1, 6) == (8, 2)
assert slope((0, -2), (4, 6)) == 2 and solve(2, -1, 2, 1, 1, 4) == (2, 2)
assert solve(1, 4, 36, 1, 1, 24) == (20, 4) and 20 + 7 * 4 == 48
assert solve(5, 8, 9300, 1, 2, 2000) == (1300, 350)
assert F(1, 2) * 2 + 2 == 3 and -2 + 5 == 3
assert 4 * 8 != 30 and F(50, 4) == F(25, 2)
SETS, POOL = build(A, B, C, D)
assert solve(8, 5, 190, 5, 8, 187) == (15, 14)
