"""Class 10 Maths Ch 3 - Pair of Linear Equations in Two Variables (graded banks)."""
from mg import *

SLUG, NAME, CHNO = "Pair_of_Linear_Equations_in_Two_Variables", "Pair of Linear Equations in Two Variables", 3

def lx(a, b):
    a, b = F(a), F(b)
    s = co(a, "x") if a != 0 else ""
    if b != 0: s += (("+" if b > 0 else "-") if a != 0 else ("-" if b < 0 else "")) + co(abs(b), "y")
    return s
def E(a, b, c): return f"{lx(a,b)}={t(c)}"
def sysk(a1, b1, a2, b2, x0, y0):
    return (a1, b1, a1 * x0 + b1 * y0, a2, b2, a2 * x0 + b2 * y0, x0, y0)
def SY(r):
    a1, b1, c1, a2, b2, c2, x0, y0 = r
    return f"${E(a1,b1,c1)}$ and ${E(a2,b2,c2)}$"
def ELIM(r):
    a1, b1, c1, a2, b2, c2, x0, y0 = r
    return (f"Multiply (i) by ${b2}$ and (ii) by ${b1}$ and subtract: $({a1*b2-a2*b1})x={c1*b2-c2*b1}$ (2); $x={x0}$ (1); put in (i): $y={y0}$ (1); check in (ii) (1).")
def SUB(r):
    a1, b1, c1, a2, b2, c2, x0, y0 = r
    return (f"From (i): $y=\\dfrac{{{c1}{sg(-a1)}x}}{{{b1}}}$ (1); substitute in (ii) (1); simplify to $({a2*b1-a1*b2})x={c2*b1-c1*b2}$ (1); $x={x0}$ (1); $y={y0}$ (1).")
def kind(a1, b1, c1, a2, b2, c2):
    if a1 * b2 != a2 * b1: return "unique"
    return "infinite" if F(a1, a2) == F(c1, c2) else "none"
KT = {"unique": "exactly one solution (intersecting lines)", "none": "no solution (parallel lines)", "infinite": "infinitely many solutions (coincident lines)"}
KW = ["exactly one solution (intersecting lines)", "no solution (parallel lines)", "infinitely many solutions (coincident lines)"]
def MK(q, k, why=""):
    return MS(q, KT[k], [KT[z] for z in KT if z != k] + ["exactly two solutions"], why)

R6 = [sysk(1, 1, 1, -1, 5, 3), sysk(2, 1, 1, -1, 4, 2), sysk(1, 2, 3, -1, 3, 1), sysk(3, 1, 1, 1, 2, 5), sysk(1, 3, 2, 1, 6, 2), sysk(2, 3, 1, 1, 3, 4)]
R6b = [sysk(2, 3, 5, 4, 3, 2), sysk(3, 2, 2, -3, 4, 1), sysk(4, 3, 3, 2, 3, 2), sysk(5, 2, 3, 4, 2, 5), sysk(2, -3, 3, 2, 6, 2), sysk(3, 4, 5, -2, 4, 2)]
R6c = [sysk(7, 2, 3, 5, -2, 4), sysk(5, 3, 4, 7, 4, 3), sysk(6, 5, 7, 4, 5, 6), sysk(9, 2, 5, 3, 4, 7), sysk(8, 3, 3, 5, 3, 2), sysk(4, -7, 5, 6, 8, 6)]
R6d = [sysk(11, 4, 5, 3, 3, 5), sysk(13, 5, 6, 7, 4, 3), sysk(9, 7, 4, 5, 3, 6), sysk(12, 5, 7, 8, 5, 2), sysk(15, 4, 7, 6, 2, 9), sysk(17, 3, 8, 5, 2, 7)]

# ---------------- EASY ----------------
eA = [[MK(f"The pair of equations ${E(a1,b1,c1)}$ and ${E(a2,b2,c2)}$ has:", kind(a1, b1, c1, a2, b2, c2), f"$\\frac{{a_1}}{{a_2}}={t(F(a1,a2))}$, $\\frac{{b_1}}{{b_2}}={t(F(b1,b2))}$, $\\frac{{c_1}}{{c_2}}={t(F(c1,c2))}$") for a1, b1, c1, a2, b2, c2 in [(1, 2, 3, 2, 4, 6), (1, 1, 5, 2, 2, 7), (2, 3, 4, 4, 5, 9), (3, 1, 6, 6, 2, 12), (1, 2, 4, 3, 6, 8), (2, -1, 3, 4, 1, 5)]],
      [MS(f"Which of the following pairs $(x,y)$ is a solution of ${E(a,b,c)}$?", f"$({x0},{y0})$", [f"$({u},{v})$" for u, v in [(y0, x0), (-x0, y0), (x0, -y0), (x0 + 1, y0), (x0, y0 + 1), (x0 - 1, y0 + 1)] if a * u + b * v != c][:3], f"${a}({x0}){sg(b)}({y0})={a*x0+b*y0}={c}$") for a, b, c, x0, y0 in [(2, 3, 12, 3, 2), (3, 1, 11, 2, 5), (1, 2, 9, 3, 3), (2, 1, 7, 2, 3), (5, 1, 14, 2, 4), (4, 1, 9, 2, 1)]],
      [MN(f"If $x={x0},y={y0}$ is a solution of ${lx(a,b)}=k$, then $k$ is:", a * x0 + b * y0, [a * y0 + b * x0, a * x0 - b * y0, (a + b) * (x0 + y0), a * b * (x0 + y0)], why=f"$k={a}({x0}){sg(b)}({y0})$") for a, b, x0, y0 in [(2, 3, 2, 1), (3, 1, 4, 2), (1, 5, 3, 2), (4, 2, 1, 3), (5, 3, 2, 2)]],
      [MN(f"The sum of two numbers is {s} and their difference is {d}. The larger number is:", (s + d) // 2, [(s - d) // 2, s + d, s - d], why=f"$x+y={s}$, $x-y={d}$ gives $2x={s+d}$") for s, d in [(10, 4), (14, 6), (20, 8), (18, 2), (30, 12)]],
      [MS(f"The graph of $x={c}$ is a line parallel to the:", "$y$-axis", ["$x$-axis", "line $y=x$", "none of the axes"], "All points have the same $x$-coordinate") for c in [2, 3, 4, 5]],
      [MS(f"The lines ${E(a,b,c)}$ and ${E(a*m,b*m,c*m)}$ are:", "coincident", ["parallel", "intersecting at one point", "perpendicular"], "One equation is a multiple of the other") for a, b, c, m in [(1, 2, 3, 2), (2, 1, 5, 3), (3, 1, 4, 2), (1, 3, 6, 4)]]]
eB = ([Q(f"Check whether the pair ${E(a1,b1,c1)}$, ${E(a2,b2,c2)}$ is consistent.", f"$\\dfrac{{a_1}}{{a_2}}={t(F(a1,a2))}$, $\\dfrac{{b_1}}{{b_2}}={t(F(b1,b2))}$ (1); " + ("ratios differ, one solution, consistent (1)." if kind(a1, b1, c1, a2, b2, c2) == "unique" else ("all ratios equal, infinitely many solutions, consistent (1)." if kind(a1, b1, c1, a2, b2, c2) == "infinite" else "$a_1/a_2=b_1/b_2\\ne c_1/c_2$, no solution, inconsistent (1).")), "1+1") for a1, b1, c1, a2, b2, c2 in [(2, 3, 7, 4, 6, 14), (1, 1, 4, 2, 2, 9), (3, 2, 5, 1, -1, 2), (5, -2, 3, 10, -4, 6)]]
      + [Q(f"Solve: $x+y={s}$, $x-y={d}$.", f"Adding: $2x={s+d}$ (1) so $x={(s+d)//2}$, $y={(s-d)//2}$ (1).", "1+1") for s, d in [(12, 4), (20, 6), (15, 3), (30, 10)]]
      + [Q(f"Find the value of $k$ if $x={x0},y={y0}$ is a solution of ${lx(a,b)}=k$.", f"$k={a}({x0}){sg(b)}({y0})$ (1) $={a*x0+b*y0}$ (1).", "1+1") for a, b, x0, y0 in [(3, 2, 2, 5), (4, -1, 3, 2), (2, 7, 1, 1), (5, 3, 2, -1)]])
eC = ([Q(f"Solve by elimination: {SY(r)}.", ELIM(r), "2+1+1+1") for r in R6]
      + [Q(f"Solve by the substitution method: {SY(r)}.", SUB(r), "1+1+1+1+1") for r in R6[::-1]]
      + [Q(f"The sum of two numbers is {x0+y0} and their difference is {x0-y0}. Find the numbers.", f"Let numbers be $x,y$: $x+y={x0+y0}$, $x-y={x0-y0}$ (1); adding $2x={2*x0}$ (1); numbers ${x0}$ and ${y0}$ (1).", "1+1+1") for x0, y0 in [(18, 7), (25, 9), (32, 11), (40, 13), (27, 14), (45, 8)]])
eD = ([Q(f"Solve by elimination: {SY(r)}.", ELIM(r), "2+1+1+1") for r in R6b]
      + [Q(f"{a} pencils and {b} erasers cost ₹{a*p+b*e}, while {a2} pencils and {b2} erasers cost ₹{a2*p+b2*e}. Find the cost of one pencil and one eraser.", f"Let pencil $=x$, eraser $=y$: ${E(a,b,a*p+b*e)}$, ${E(a2,b2,a2*p+b2*e)}$ (2); solving, $x={p}$, $y={e}$ (2); pencil ₹{p}, eraser ₹{e} (1).", "2+2+1") for a, b, a2, b2, p, e in [(2, 3, 3, 2, 5, 4), (4, 1, 1, 3, 6, 3), (3, 2, 5, 1, 8, 5), (2, 5, 6, 1, 7, 2), (5, 2, 2, 3, 4, 9), (3, 4, 4, 1, 9, 6)]])

# ---------------- NCERT ----------------
def sol_cost(a1, b1, c1, a2, b2, c2): return (F(c1 * b2 - c2 * b1, a1 * b2 - a2 * b1), F(a1 * c2 - a2 * c1, a1 * b2 - a2 * b1))
nA = [[MK(f"The pair of equations ${E(a1,b1,c1)}$ and ${E(a2,b2,c2)}$ is:", kind(a1, b1, c1, a2, b2, c2), f"Compare $a_1/a_2$, $b_1/b_2$, $c_1/c_2$") for a1, b1, c1, a2, b2, c2 in [(3, 2, 5, 9, 6, 15), (2, 3, 8, 4, 6, 12), (1, -2, 3, 2, 1, 5), (6, -3, 10, 2, -1, 9), (5, 4, 3, 10, 8, 6)]],
      [MN(f"The solution of ${E(a1,b1,c1)}$, ${E(a2,b2,c2)}$ has $x=$", x0, [y0, -x0, x0 + y0, x0 * y0], why="Solve by elimination") for a1, b1, c1, a2, b2, c2, x0, y0 in R6[:5]],
      [MN(f"The solution of ${E(a1,b1,c1)}$, ${E(a2,b2,c2)}$ has $y=$", y0, [x0, -y0, x0 + y0, x0 * y0], why="Solve by elimination") for a1, b1, c1, a2, b2, c2, x0, y0 in R6b[:5]],
      [MN(f"For the pair $x+y={s}$ and $x-y={d}$, the value of $xy$ is:", F(s + d, 2) * F(s - d, 2), [F(s * s - d * d, 2), s, F(s * s + d * d, 4)], why=f"$x={t(F(s+d,2))}$, $y={t(F(s-d,2))}$") for s, d in [(10, 2), (14, 4), (16, 6), (20, 4), (24, 8)]],
      [MN(f"The pair $x+{b}y={c}$ and ${m}x+ky={m*c+1}$ has no solution when $k=$", m * b, [b, m * b + 1, m * c, 2 * m * b], why=f"$\\frac{{1}}{{{m}}}=\\frac{{{b}}}{{k}}\\ne\\frac{{{c}}}{{{m*c+1}}}$") for b, c, m in [(2, 3, 2), (3, 4, 3), (2, 5, 4), (4, 3, 2), (5, 2, 3)]],
      [MN(f"The point where the lines ${E(a1,b1,c1)}$ and ${E(a2,b2,c2)}$ intersect has $x+y=$", x0 + y0, [x0, y0, x0 - y0, x0 * y0], why="Solve, then add") for a1, b1, c1, a2, b2, c2, x0, y0 in R6c[:5]]]
nB = ([Q(f"A man tells his daughter, \"Seven years ago I was {m} times as old as you were. Three years from now I shall be {n} times as old as you will be.\" Form the pair of linear equations (do not solve).", f"Let father $x$, daughter $y$ now (1); $x-7={m}(y-7)$ and $x+3={n}(y+3)$ (1).", "1+1") for m, n in [(7, 3), (6, 3), (5, 3), (8, 3)]]
      + [Q(f"Solve by substitution: ${E(a1,b1,c1)}$, ${E(a2,b2,c2)}$.", f"Express one variable, substitute: $x={x0}$ (1), $y={y0}$ (1).", "1+1") for a1, b1, c1, a2, b2, c2, x0, y0 in R6[:4]]
      + [Q(f"Find the value of $k$ for which the pair $x+{b}y={c}$, ${m}x+ky={m*c+1}$ has no solution.", f"$\\frac{{1}}{{{m}}}=\\frac{{{b}}}{{k}}\\ne\\frac{{{c}}}{{{m*c+1}}}$ (1); $k={m*b}$ (1).", "1+1") for b, c, m in [(2, 3, 2), (3, 4, 3), (2, 5, 4), (4, 3, 2)]])
nC = ([Q(f"On comparing the ratios, find whether the lines ${E(a1,b1,c1)}$ and ${E(a2,b2,c2)}$ intersect, are parallel or coincide.", f"$\\frac{{a_1}}{{a_2}}={t(F(a1,a2))}$, $\\frac{{b_1}}{{b_2}}={t(F(b1,b2))}$, $\\frac{{c_1}}{{c_2}}={t(F(c1,c2))}$ (2); " + {"unique": "ratios $a_1/a_2\\ne b_1/b_2$: lines intersect (1).", "none": "$a_1/a_2=b_1/b_2\\ne c_1/c_2$: lines are parallel (1).", "infinite": "all ratios equal: lines coincide (1)."}[kind(a1, b1, c1, a2, b2, c2)], "2+1") for a1, b1, c1, a2, b2, c2 in [(5, -4, 8, 7, 6, 9), (9, 3, 12, 18, 6, 24), (6, -3, 10, 2, -1, 9), (3, 2, 5, 9, 6, 15), (2, 3, 8, 4, 6, 20), (7, -3, 11, 14, -6, 22)]]
      + [Q(f"Solve by elimination method: {SY(r)}.", ELIM(r), "2+1+1+1") for r in R6b]
      + [DIG(a_, b_) for a_, b_ in [(7, 2), (6, 3), (8, 1), (5, 4), (9, 2), (7, 4)]])
nD = ([AGE(*p) for p in [(8, 5, 9), (7, 4, 6)]] + [BOAT(*p) for p in [(5, 9, 30, 45, 40, 27), (4, 10, 28, 30, 21, 50)]] + [FRAC(*p) for p in [(5, 8, 1, 3), (4, 9, 2, 5)]]
      + [TAXI(*p) for p in [(30, 14, 10, 15, 25), (45, 12, 8, 14, 30)]] + [RECT(*p) for p in [(20, 15, 5, 3, 3, 2), (18, 12, 4, 2, 2, 3)]] + [TRAIN(*p) for p in [(60, 80, 480, 240, 300), (40, 50, 360, 160, 200)]])

# ---------------- MEDIUM ----------------
def CROSS(r):
    a1, b1, c1, a2, b2, c2, x0, y0 = r
    return Q(f"Solve by the cross-multiplication method: {SY(r)}.", f"Write as ${a1}x{sg(b1)}y{sg(-c1)}=0$, ${a2}x{sg(b2)}y{sg(-c2)}=0$ (1); $\\dfrac{{x}}{{{b1*(-c2)-b2*(-c1)}}}=\\dfrac{{y}}{{{(-c1)*a2-(-c2)*a1}}}=\\dfrac{{1}}{{{a1*b2-a2*b1}}}$ (1); $x={x0}$, $y={y0}$ (1).", "1+1+1")
mA = [[MN(f"The value of $x$ in ${E(a1,b1,c1)}$, ${E(a2,b2,c2)}$ is:", x0, [y0, -x0, x0 + y0, x0 * y0], why="Eliminate $y$") for a1, b1, c1, a2, b2, c2, x0, y0 in R6c[:5]],
      [MN(f"The value of $y$ in ${E(a1,b1,c1)}$, ${E(a2,b2,c2)}$ is:", y0, [x0, -y0, x0 + y0, x0 * y0], why="Eliminate $x$") for a1, b1, c1, a2, b2, c2, x0, y0 in R6d[:5]],
      [MN(f"The pair ${p}x+ky={p*3}$, ${2*p}x+{2*p}y={p*6}$ has infinitely many solutions when $k=$", p, [2 * p, 3 * p, p + 1, 6], why="All ratios equal") for p in [2, 3, 4, 5, 6]],
      [MN(f"For the pair $kx+{b1}y={c1}$ and ${a2}x+{b2}y={c2}$ to have a unique solution, $k$ must NOT equal:", F(a2 * b1, b2), [F(a2 * b2, b1), a2 + b1, F(c1 * a2, c2), F(b1 * b2, a2)], why="$\\frac{k}{a_2}\\ne\\frac{b_1}{b_2}$ for a unique solution") for b1, c1, a2, b2, c2 in [(2, 5, 6, 1, 3), (3, 4, 8, 2, 5), (4, 7, 9, 3, 2), (5, 1, 6, 2, 7), (2, 9, 5, 4, 3)]],
      [MN(f"If ${a}x+{b}y={c1}$ and ${b}x+{a}y={c2}$, then $x+y=$", F(c1 + c2, a + b), [c1 + c2, F(c1 - c2, a - b), F(c1 + c2, 2), F(c1 + c2, a * b)], why="Add the two equations") for a, b, c1, c2 in [(3, 2, 25, 20), (4, 3, 31, 25), (5, 2, 33, 27), (6, 5, 52, 49), (7, 3, 60, 40)]],
      [MN(f"If $x+y={s}$ and $x-y={d}$, then $x^2-y^2=$", s * d, [s + d, s * s - d * d, s * s + d * d], why=f"$(x+y)(x-y)={s}\\times{d}$") for s, d in [(9, 3), (11, 5), (13, 4), (15, 7), (12, 6)]]]
mB = ([CROSS(r) for r in R6c[:4]]
      + [Q(f"For what value of $k$ does the pair $kx+{b1}y={c1}$, ${a2}x+{b2}y={c2}$ have a unique solution?", f"Unique solution when $\\dfrac{{a_1}}{{a_2}}\\ne\\dfrac{{b_1}}{{b_2}}$ (1): $\\dfrac{{k}}{{{a2}}}\\ne\\dfrac{{{b1}}}{{{b2}}}$, i.e. $k\\ne{t(F(a2*b1,b2))}$ (1).", "1+1") for b1, c1, a2, b2, c2 in [(2, 5, 6, 1, 3), (3, 4, 8, 2, 5), (4, 7, 9, 3, 2), (5, 1, 6, 2, 7)]]
      + [Q(f"Find $k$ so that the pair ${p}x+ky={3*p}$ and ${2*p}x+{2*p}y={6*p}$ has infinitely many solutions.", f"$\\frac{{{p}}}{{{2*p}}}=\\frac{{k}}{{{2*p}}}=\\frac{{{3*p}}}{{{6*p}}}$ (1) gives $k={p}$ (1).", "1+1") for p in [2, 3, 5, 7]])
mC = ([Q(f"Solve by elimination: {SY(r)}.", ELIM(r), "2+1+1+1") for r in R6c]
      + [DIG(a_, b_) for a_, b_ in [(3, 8), (4, 9), (2, 7), (1, 6), (4, 8), (3, 9)]]
      + [Q(f"Find the value of $k$ for which the pair $kx+{pp}y=k-{pp}$ and ${4*pp}x+ky=k$ has infinitely many solutions.", f"$\\dfrac{{k}}{{{4*pp}}}=\\dfrac{{{pp}}}{{k}}$ gives $k^2={4*pp*pp}$ (1); $k=\\pm{2*pp}$ (1); only $k={2*pp}$ also satisfies $\\dfrac{{{pp}}}{{k}}=\\dfrac{{k-{pp}}}{{k}}$ (1).", "1+1+1") for pp in [1, 2, 3, 4, 5, 6]])
mD = ([AGE(*p) for p in [(10, 4, 6), (6, 5, 10), (9, 5, 12)]] + [TAXI(*p) for p in [(20, 10, 5, 12, 20), (50, 8, 10, 25, 40), (35, 15, 6, 14, 22)]]
      + [FRAC(*p) for p in [(3, 7, 1, 2), (5, 9, 3, 6), (7, 11, 2, 4)]] + [RECT(*p) for p in [(15, 10, 3, 2, 2, 2), (24, 16, 6, 3, 4, 2), (14, 9, 2, 3, 3, 1)]])

# ---------------- HARD ----------------
hA = [[MN(f"The pair $kx+{p}y=k-{p}$ and ${4*p}x+ky=k$ has no solution when $k=$", -2 * p, [2 * p, 4 * p, p], "$k^2=4p^2$; $k=2p$ gives coincident lines, $k=-2p$ gives parallel lines") for p in [2, 3, 4, 5, 6]],
      [MN(f"The pair $kx+{p}y=k-{p}$ and ${4*p}x+ky=k$ has infinitely many solutions when $k=$", 2 * p, [-2 * p, 4 * p, p], "Needs $\\frac{k}{4p}=\\frac{p}{k}=\\frac{k-p}{k}$") for p in [1, 7, 8, 9, 10]],
      [MN(f"If ${E(a1,b1,c1)}$ and ${E(a2,b2,c2)}$, then $x+y=$", x0 + y0, [x0, y0, x0 * y0, x0 - y0], why="Solve for $x$ and $y$") for a1, b1, c1, a2, b2, c2, x0, y0 in R6d[:5]],
      [MN(f"The area (in sq. units) of the triangle formed by the line ${E(a,b,c)}$ and the coordinate axes is:", F(c * c, 2 * a * b), [F(c * c, a * b), F(c, 2 * a), F(c * c, 2)], f"Intercepts ${t(F(c,a))}$ and ${t(F(c,b))}$; area $=\\frac12\\times{t(F(c,a))}\\times{t(F(c,b))}$") for a, b, c in [(2, 3, 12), (3, 4, 12), (5, 2, 20), (4, 5, 20), (6, 3, 18)]],
      [MN(f"If $x+y={s}$ and $xy={p}$, then $x^2+y^2=$", s * s - 2 * p, [s * s + 2 * p, s * s - p, s * s, s + p], why=f"$(x+y)^2-2xy={s*s}-{2*p}$") for s, p in [(7, 10), (9, 20), (10, 21), (12, 35), (11, 24)]],
      [MN(f"If ${a}x+{b}y={c1}$ and ${b}x+{a}y={c2}$, then $x-y=$", F(c1 - c2, a - b), [F(c1 - c2, a + b), c1 - c2, F(c1 + c2, a - b), F(c1 + c2, 2)], why="Subtract the equations") for a, b, c1, c2 in [(5, 3, 47, 41), (7, 4, 61, 54), (6, 2, 38, 30), (9, 5, 66, 58), (8, 3, 44, 37)]]]
hB = ([Q(f"Find $k$ so that the pair $kx+{p}y=k-{p}$, ${4*p}x+ky=k$ has no solution.", f"$\\dfrac{{k}}{{{4*p}}}=\\dfrac{{{p}}}{{k}}\\Rightarrow k=\\pm{2*p}$ (1); $k={2*p}$ gives coincident lines, so $k=-{2*p}$ (1).", "1+1") for p in [2, 3, 4, 5]]
      + [Q(f"Solve: ${a}x+{b}y={c1}$ and ${b}x+{a}y={c2}$.", f"Adding: ${a+b}(x+y)={c1+c2}$ so $x+y={t(F(c1+c2,a+b))}$ (1); subtracting: $x-y={t(F(c1-c2,a-b))}$, so $x={t((F(c1+c2,a+b)+F(c1-c2,a-b))/2)}$, $y={t((F(c1+c2,a+b)-F(c1-c2,a-b))/2)}$ (1).", "1+1") for a, b, c1, c2 in [(5, 3, 47, 41), (7, 4, 61, 54), (6, 2, 38, 30), (9, 5, 66, 58)]]
      + [Q(f"Find the points where the line ${E(a,b,c)}$ meets the coordinate axes and the area of the triangle so formed.", f"$x$-intercept $\\left({t(F(c,a))},0\\right)$, $y$-intercept $\\left(0,{t(F(c,b))}\\right)$ (1); area $=\\frac12\\times{t(F(c,a))}\\times{t(F(c,b))}={t(F(c*c,2*a*b))}$ (1).", "1+1") for a, b, c in [(3, 2, 12), (4, 5, 20), (6, 4, 24), (5, 3, 15)]])
INF = [(3, 1, 7, 2), (5, 3, 4, 3), (7, 1, 5, 2), (4, 2, 3, 3), (5, 1, 9, 2), (3, 1, 2, 4)]
def AREAX(a1, b1, c1, a2, b2, c2):
    x0, y0 = sol_cost(a1, b1, c1, a2, b2, c2); base = abs(F(c1, a1) - F(c2, a2))
    return Q(f"Find the area of the triangle formed by the lines ${E(a1,b1,c1)}$, ${E(a2,b2,c2)}$ and the $x$-axis.", f"Intersection $({t(x0)},{t(y0)})$ (1); $x$-intercepts ${t(F(c1,a1))}$ and ${t(F(c2,a2))}$ (1); area $=\\frac12\\times{t(base)}\\times{t(abs(y0))}={t(base*abs(y0)/2)}$ (1).", "1+1+1")
hC = ([RED(*p) for p in [(2, 3, 2, 3, 3, 5), (4, 2, 3, 4, 5, 2), (5, 4, 2, 5, 3, 2), (3, 6, 4, 3, 2, 5), (2, 5, 3, 2, 4, 5), (6, 3, 5, 2, 3, 4)]]
      + [Q(f"Find $a$ and $b$ for which the pair ${p}x+{q}y={r}$ and $(a+b)x+(a-b)y={m*r}$ has infinitely many solutions.", f"Need $\\dfrac{{a+b}}{{{p}}}=\\dfrac{{a-b}}{{{q}}}=\\dfrac{{{m*r}}}{{{r}}}={m}$ (1); $a+b={m*p}$, $a-b={m*q}$ (1); $a={t(F(m*(p+q),2))}$, $b={t(F(m*(p-q),2))}$ (1).", "1+1+1") for p, q, r, m in INF]
      + [AREAX(*p) for p in [(1, 1, 6, 1, -1, 2), (2, 1, 8, 1, 1, 5), (1, 2, 8, 2, 1, 7), (3, 1, 9, 1, 1, 5), (1, 3, 9, 2, 1, 8), (2, 3, 12, 1, 1, 5)]])
hD = ([BOAT(*p) for p in [(6, 10, 36, 40, 24, 70), (3, 11, 21, 33, 12, 55), (4, 12, 40, 36, 28, 72), (5, 15, 45, 60, 30, 90)]]
      + [TRAIN(*p) for p in [(50, 75, 600, 300, 400), (45, 60, 540, 270, 360), (30, 40, 360, 150, 240), (80, 100, 900, 480, 600)]]
      + [KTRI(*p) for p in [(1, 1, 8, 2, -1, 4), (2, 1, 10, 1, -1, 2), (1, 2, 11, 2, -1, 7), (3, 1, 13, 1, -2, 5)]])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
