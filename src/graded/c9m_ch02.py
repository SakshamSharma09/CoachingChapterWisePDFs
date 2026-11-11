"""Class 9 Maths Ch 2 - Linear Polynomials (degree, value, zero, graph, slope and intercepts, nth term, real-life rates)."""
from c9h import *

SLUG, NAME, CHNO = "Linear_Polynomials", "Linear Polynomials", 2

def pl(a, b, v="x"): return f"${lin(a, b, v)}$"
def eq(a, b): return f"$y={lin(a, b)}$"
def ln(a, b, v="x"): return lin(a, b, v)
def optlin(a, b, v="n"):
    c = [(a, b + 1), (a + 1, b), (a, b - 1), (b, a), (a - 1, b), (a, -b)]
    out = []
    for p in c:
        s = pl(*p, v)
        if s != pl(a, b, v) and s not in out: out.append(s)
    return out
def mq(q, a, b, why="", v="n"): return M4(q, pl(a, b, v), optlin(a, b, v), why)

# ------------------------------------------------------------------ EASY
eA1 = [nm(f"The degree of the polynomial ${t}$ is:", d, "The degree is the highest power of the variable.") for t, d in
       [("5x-7", 1), ("x^3-2x+1", 3), ("4x^2+x", 2), ("9", 0), ("x^5", 5), ("3-2x", 1)]]
eA2 = [nm(f"If $p(x)={ln(a, b)}$, then $p({k})=$", a * k + b, "Substitute $x$ and simplify.", pos=False) for a, b, k in [(2, 3, 4), (5, -1, 3), (3, 4, 2), (-2, 9, 3), (4, -5, 2), (6, 1, 5)]]
eA3 = [nm(f"The zero of the polynomial ${ln(a, -a * z)}$ is:", z, "Solve $p(x)=0$.") for a, z in [(1, 5), (2, 3), (3, 4), (5, 2), (4, 6), (2, 7)]]
eA4 = [nm(f"The $y$-intercept of the line {eq(m, c)} is:", c, "Put $x=0$: $y=c$.", pos=False) for m, c in [(2, 5), (-3, 7), (4, -1), (5, 6)]]
eA5 = [nm(f"The slope of the line {eq(m, c)} is:", m, "In $y=mx+c$ the slope is $m$.", pos=False) for m, c in [(3, 2), (-4, 1), (6, -3), (7, 5)]]
eA6 = [M4(t, c, w, "Recall the definition.") for t, c, w in [
    ("The graph of a linear polynomial is a:", "straight line", ["parabola", "circle", "pair of points"]),
    ("A linear polynomial $ax+b$ ($a\\ne0$) has exactly:", "one zero", ["two zeros", "no zero", "infinitely many zeros"]),
    ("A polynomial of degree $0$ is called a:", "constant polynomial", ["linear polynomial", "quadratic polynomial", "cubic polynomial"]),
    ("A polynomial of degree $1$ is called a:", "linear polynomial", ["constant polynomial", "quadratic polynomial", "cubic polynomial"])]]
eA7 = [mq(f"The $n$th term of the pattern {', '.join(str(a1 + d * i) for i in range(4))}, ... is:", d, a1 - d, "$a_n=a_1+(n-1)d$.") for a1, d in [(5, 3), (4, 2), (7, 5), (2, 4)]]
eA8 = [M4(f"The graph of {eq(m, c)} cuts the $y$-axis at:", TP(0, c), optpts(0, c), "At $x=0$, $y=c$.") for m, c in [(2, 4), (3, -2), (-1, 6), (5, 3)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"If $p(x)={ln(a, b)}$, find $p({k})$.", f"$p({k})={a}({k})+({b})$" if b >= 0 else f"$p({k})={a}({k})-{-b}$", f"$p({k})={a * k + b}$") for a, b, k in [(3, 5, 2), (4, -3, 5), (-2, 8, 3), (7, 1, 4)]]
          + [QQ(f"Find the zero of the polynomial ${ln(a, -a * z)}$.", f"Put ${ln(a, -a * z)}=0$", f"$x={z}$") for a, z in [(3, 5), (2, 9), (6, 2), (5, 4)]]
          + [QQ(f"Write the degree of ${t}$ and say whether it is constant, linear or quadratic.", f"Degree $={d}$", f"The polynomial is {['constant', 'linear', 'quadratic'][d]}") for t, d in [("8x+3", 1), ("6", 0), ("x^2-4", 2), ("11-5x", 1)]])
EASY_C = ([QQ(f"Find the zero of ${ln(a, b)}$ and verify it.", f"${ln(a, b)}=0$ gives $x={-b // a}$", f"Check: $p({-b // a})={a}({-b // a})+({b})=0$", "Hence the zero is verified") for a, b in [(2, -10), (3, 12), (4, -20), (5, 15), (7, -21), (6, 18)]]
          + [QQ(f"Complete the table of values for $y={ln(a, b)}$ at $x=0,1,2$.", f"$x=0$: $y={b}$", f"$x=1$: $y={a + b}$", f"$x=2$: $y={2 * a + b}$") for a, b in [(3, 1), (2, 5), (4, -2), (5, 0), (-1, 7), (6, -4)]]
          + [QQ(f"Find the $n$th term and the {t}th term of the pattern {', '.join(str(a1 + d * i) for i in range(4))}, ...", f"$d={d}$", f"$a_n={ln(d, a1 - d, 'n')}$", f"$a_{{{t}}}={d * t + a1 - d}$") for (a1, d), t in zip([(3, 4), (6, 5), (10, 3), (2, 6), (9, 7), (1, 8)], [10, 12, 15, 11, 20, 9])])
EASY_D = ([QQ(f"A taxi charges a fixed fare of ₹{f} plus ₹{r} per km. Write the fare $F(x)$ for $x$ km, find the fare for {k} km and the distance covered for a fare of ₹{f + r * j}.", f"$F(x)={ln(r, f)}$", f"$F({k})={r}\\times{k}+{f}$", f"$F({k})=₹{r * k + f}$", f"${ln(r, f)}={f + r * j}$", f"$x={j}$ km")
           for f, r, k, j in [(30, 10, 6, 8), (20, 12, 5, 7), (40, 15, 4, 9), (25, 8, 10, 6), (50, 20, 3, 5), (15, 9, 7, 12)]]
          + [QQ(f"For the line {eq(m, c)}, write the slope, the $y$-intercept, the $x$-intercept, and say whether the point ${P(k, m * k + c + o)}$ lies on it.", f"Slope $={m}$", f"$y$-intercept $={c}$", f"$x$-intercept: $0={m}x+({c})$, $x={-c // m}$", f"At $x={k}$: $y={m * k + c}$", "So the point lies on the line" if o == 0 else f"The point has $y={m * k + c + o}\\ne{m * k + c}$, so it does not lie on the line")
             for (m, c, k), o in zip([(2, 6, 3), (3, -9, 4), (4, 8, 2), (5, -10, 5), (6, 12, 1), (2, -8, 6)], [0, 2, 0, 3, 0, -1])])

# ------------------------------------------------------------------ NCERT
nA1 = [M4(f"Which of these is a linear polynomial?", c, w, "Linear means degree exactly $1$.") for c, w in
       [("$3x+4$", ["$x^2+4$", "$7$", "$x^3-x$"]), ("$5-2x$", ["$x^2-5$", "$9$", "$x^3$"]), ("$\\frac{x}{3}+1$", ["$x^2+1$", "$\\frac{3}{x}+1$", "$\\sqrt{x}+1$"]), ("$4x$", ["$4$", "$4x^2$", "$4x^3$"])]]
nA2 = [nm(f"If $x={z}$ is a zero of the polynomial ${ln(a, 0)}+k$, then $k=$", -a * z, "Put $x$ in $p(x)=0$.", pos=False) for a, z in [(2, 5), (3, 4), (5, 2), (4, 6)]]
nA3 = [nm(f"The value of ${ln(a, b)}$ at $x=-{k}$ is:", -a * k + b, "Substitute $x=-k$.", pos=False) for a, b, k in [(3, 5, 2), (2, 7, 4), (5, 1, 3), (4, 9, 5)]]
nA4 = [nm(f"The line {eq(m, c)} passes through $(2, p)$. The value of $p$ is:", 2 * m + c, "Put $x=2$.", pos=False) for m, c in [(3, 1), (4, -2), (5, 3), (-2, 9), (6, -5)]]
nA5 = [M4(f"The graph of {eq(m, c)} cuts the $x$-axis at:", TP(-c // m, 0), optpts(-c // m, 0), "Put $y=0$.") for m, c in [(2, -8), (3, 12), (5, -25), (4, 16)]]
nA6 = [nm(f"The sum of the zeros of ${ln(a, -a * z)}$ and ${ln(b, -b * w)}$ is:", z + w, "Find each zero.") for a, z, b, w in [(2, 3, 5, 4), (3, 6, 4, 2), (1, 7, 6, 3), (5, 5, 2, 8)]]
nA7 = [mq(f"The $n$th term of the pattern {', '.join(str(a1 + d * i) for i in range(4))}, ... is:", d, a1 - d, "Use $a_n=a_1+(n-1)d$.") for a1, d in [(1, 6), (8, 3), (3, 9), (12, 4)]]
nA8 = [nm(f"A plumber charges ₹{f} plus ₹{r} per hour. For {h} hours he charges ₹:", f + r * h, "Fare $=$ fixed $+$ rate $\\times$ time.") for f, r, h in [(100, 50, 3), (150, 60, 4), (80, 40, 5), (200, 75, 2)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([QQ(f"Find the zero of ${ln(a, b)}$ and show that it lies on the $x$-axis of the graph $y={ln(a, b)}$.", f"${ln(a, b)}=0$ gives $x={-b // a}$", f"The graph meets the $x$-axis at ${P(-b // a, 0)}$") for a, b in [(3, -18), (5, 20), (2, 14), (7, -28)]]
           + [QQ(f"Find $p({k})$ and $p(-{k})$ for $p(x)={ln(a, b)}$.", f"$p({k})={a * k + b}$", f"$p(-{k})={-a * k + b}$") for a, b, k in [(4, 3, 2), (3, -5, 4), (6, 2, 1), (5, 7, 3)]]
           + [QQ(f"Write the slope and intercept of {eq(m, c)}, and the coordinates of the point where it cuts the $y$-axis.", f"Slope $={m}$, intercept $={c}$", f"Cuts $y$-axis at ${P(0, c)}$") for m, c in [(8, 3), (-5, 9), (9, -2), (-7, -4)]])
NCERT_C = ([QQ(f"Draw up a table for $y={ln(a, b)}$ for $x=-1,0,1,2$ and state the slope and the $y$-intercept.", f"$x=-1$: $y={-a + b}$; $x=0$: $y={b}$", f"$x=1$: $y={a + b}$; $x=2$: $y={2 * a + b}$", f"Slope $={a}$, $y$-intercept $={b}$") for a, b in [(2, 3), (3, -1), (-2, 5), (4, 2), (5, -3), (-3, 6)]]
           + [QQ(f"The line $y={ln(k_m, 0)}+k$ has slope ${k_m}$ and passes through ${P(x, y)}$. Find $k$ and write the line.", f"Substitute: ${y}={k_m * x}+k$", f"$k={y - k_m * x}$", f"Line: $y={ln(k_m, y - k_m * x)}$") for k_m, x, y in [(2, 3, 11), (3, 2, 4), (4, 1, 9), (5, 3, 6), (2, 5, 3), (3, 4, 20)]]
           + [QQ(f"If $p(x)={ln(a, b)}$ and $q(x)={ln(c, d)}$, find $p(x)+q(x)$ and its zero.", f"$p+q={ln(a + c, b + d)}$", f"Put ${ln(a + c, b + d)}=0$", f"Zero $x={-(b + d) // (a + c)}$") for a, b, c, d in [(2, 3, 3, 7), (1, -4, 3, 0), (4, 2, 2, 4), (5, 1, 1, 5), (3, -6, 3, 0), (2, -10, 3, 0)]])
NCERT_D = ([QQ(f"The cost of $x$ notebooks is a linear polynomial: a shop charges ₹{f} for the bag plus ₹{r} per notebook. Write the cost $C(x)$, find the cost of {k} notebooks and how many notebooks can be bought for ₹{f + r * j}.", f"$C(x)={ln(r, f)}$", f"$C({k})={r * k + f}$", f"${ln(r, f)}={f + r * j}$", f"$x={j}$", "Hence the number of notebooks is " + str(j))
            for f, r, k, j in [(60, 12, 5, 9), (45, 15, 4, 7), (90, 20, 3, 8), (70, 14, 6, 10), (55, 11, 7, 6), (120, 25, 2, 11)]]
           + [QQ(f"For $y={ln(m, c)}$: (i) find $y$ at $x=0,1,2$; (ii) find the point where the graph crosses the $x$-axis; (iii) state the slope and say whether the graph rises or falls from left to right.", f"$y(0)={c}$, $y(1)={m + c}$, $y(2)={2 * m + c}$", f"Crosses $x$-axis: $x={-c // m}$", f"Point ${P(-c // m, 0)}$", f"Slope $={m}$", f"Slope is {'positive: the graph rises' if m > 0 else 'negative: the graph falls'}")
              for m, c in [(4, -12), (-3, 9), (5, 10), (-2, -8), (6, -18), (-4, 20)]])

# ------------------------------------------------------------------ MEDIUM
mA1 = [nm(f"If $x={z}$ is a zero of ${ln(a, 0)}+m$, then $m=$", -a * z, "Put $p(z)=0$.", pos=False) for a, z in [(7, 2), (6, 5), (9, 3), (8, 4), (5, 7)]]
mA2 = [nm(f"The slope of the line through ${P(x1, y1)}$ and ${P(x2, y2)}$ is:", (y2 - y1) // (x2 - x1), "Slope $=\\frac{y_2-y_1}{x_2-x_1}$.", pos=False) for x1, y1, x2, y2 in [(1, 3, 3, 9), (0, -2, 4, 10), (-1, 5, 2, -4), (2, 1, 6, 17), (-3, -7, 1, 5)]]
mA3 = [nm(f"The $x$-intercept of the line {eq(m, m * k)} is:", -k, "Put $y=0$.", pos=False) for m, k in [(4, 3), (6, -2), (3, 7), (5, 5)]]
mA4 = [nm(f"The point $(k, {m * k + c})$ lies on {eq(m, c)}. Then $k=$", k, "Substitute $y$ and solve for $x$.", pos=False) for m, c, k in [(7, 3, 4), (5, -4, 6), (8, 2, 3), (9, -5, 2)]]
mA5 = [M4(f"If $p(x)={ln(a, b)}$ and $q(x)={ln(c, d)}$, then $p(x)+q(x)=$", pl(a + c, b + d), optlin(a + c, b + d, "x"), "Add like terms.") for a, b, c, d in [(5, 2, 3, -7), (4, -6, 2, 1), (7, 3, -2, 8), (3, 9, 6, -4)]]
mA6 = [nm(f"A linear polynomial $p(x)=ax+b$ has $p(1)={a + b}$ and $p(2)={2 * a + b}$. Then $b=$", b, "$p(2)-p(1)=a$.", pos=False) for a, b in [(7, 4), (5, 9), (8, -3), (6, 11)]]
mA7 = [nm(f"The $n$th term of a pattern is ${ln(d, e, 'n')}$. Its {t}th term is:", d * t + e, "Substitute $n$.", pos=False) for d, e, t in [(7, -2, 12), (9, 4, 15), (6, -5, 20), (11, 3, 9)]]
mA8 = [M4(t, c, w, "Use the slope-intercept form.") for t, c, w in [
    ("Lines $y=3x+2$ and $y=3x-7$ are:", "parallel", ["perpendicular", "intersecting at one point", "identical"]),
    ("The line $y=5$ is parallel to the:", "$x$-axis", ["$y$-axis", "line $y=x$", "line $y=-x$"]),
    ("If $p(x)=ax+b$ and $b=0$, the graph passes through:", "the origin", ["$(0, 1)$", "$(1, 0)$", "the $x$-axis only"]),
    ("The slope of the line $y=-6x+1$ is:", "$-6$", ["$6$", "$1$", "$-1$"])]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Find the slope of the line through ${P(x1, y1)}$ and ${P(x2, y2)}$.", f"$m=\\frac{{{y2}-({y1})}}{{{x2}-({x1})}}$", f"$m={(y2 - y1) // (x2 - x1)}$") for x1, y1, x2, y2 in [(2, 4, 5, 13), (-1, 0, 3, 8), (0, 7, 4, -1), (-2, -3, 2, 9)]]
         + [QQ(f"For $p(x)={ln(a, b)}$ and $q(x)={ln(c, d)}$, find the zero of $p(x)-q(x)$.", f"$p-q={ln(a - c, b - d)}$", f"Zero $x={-(b - d) // (a - c)}$") for a, b, c, d in [(5, 1, 2, -8), (7, 4, 3, -4), (6, -3, 2, 9), (9, 2, 4, 12)]]
         + [QQ(f"The $n$th term of a pattern is ${ln(d, e, 'n')}$. Find its first three terms and the {t}th term.", f"$a_1={d + e}$, $a_2={2 * d + e}$, $a_3={3 * d + e}$", f"$a_{{{t}}}={d * t + e}$") for d, e, t in [(8, -3, 10), (5, 6, 14), (9, -4, 8), (4, 7, 25)]])
MED_C = ([QQ(f"The line $y=mx+{c}$ passes through ${P(x, m * x + c)}$. Find $m$, then the $x$-intercept of the line.", f"${m * x + c}=m({x})+{c}$", f"$m={m}$", f"$x$-intercept: $0={m}x+{c}$, $x={-c // m}$") for m, c, x in [(3, 12, 2), (4, 20, 3), (5, 15, 4), (2, 18, 5), (6, 24, 1), (7, 21, 2)]]
         + [QQ(f"Find three points on the line $y={ln(m, c)}$ and show that the slope between the first and last is ${m}$.", f"Points ${P(0, c)}$, ${P(1, m + c)}$, ${P(2, 2 * m + c)}$", f"Slope $=\\frac{{{2 * m + c}-({c})}}{{2-0}}$", f"$={m}$") for m, c in [(-4, 5), (9, -6), (-5, -2), (8, 3), (-6, 7), (10, -9)]]
         + [QQ(f"A pattern has first term {a1} and common difference {d}. Find its $n$th term and the term number whose value is {a1 + d * (j - 1)}.", f"$a_n={ln(d, a1 - d, 'n')}$", f"${ln(d, a1 - d, 'n')}={a1 + d * (j - 1)}$", f"$n={j}$") for a1, d, j in [(6, 7, 13), (11, 4, 17), (3, 9, 12), (14, 6, 21), (9, 8, 15), (20, 3, 30)]])
MED_D = ([QQ(f"A linear polynomial $p(x)$ has $p({a})={m * (a - z)}$ and $p({b})={m * (b - z)}$. Find $p(x)$, its zero and $p({k})$.", f"Slope $=\\frac{{{m * (b - z)}-({m * (a - z)})}}{{{b}-({a})}}={m}$", f"$p(x)={ln(m, -m * z)}$", f"Zero: $x={z}$", f"$p({k})={m * (k - z)}$")
          for m, z, a, b, k in [(4, -1, 1, 3, 5), (5, 2, 3, 6, 4), (3, -4, 0, 4, 6), (6, 1, 2, 5, 3), (2, -5, -1, 3, 7), (7, 3, 4, 6, 2)]]
          + [QQ(f"A salesperson earns ₹{f} per month plus ₹{r} for each item sold. Write her earning $E(n)$, find the earning for {k} items, the number of items sold for ₹{f + r * j}, and the extra items needed to raise earning by ₹{r * q}.", f"$E(n)={ln(r, f, 'n')}$", f"$E({k})={r * k + f}$", f"${ln(r, f, 'n')}={f + r * j}$, $n={j}$", f"Extra items $=\\frac{{{r * q}}}{{{r}}}={q}$")
             for f, r, k, j, q in [(5000, 150, 20, 60, 8), (6000, 200, 15, 45, 6), (4500, 120, 25, 50, 9), (7000, 250, 12, 36, 7), (3000, 80, 30, 75, 10), (8000, 300, 10, 40, 5)]])

# ------------------------------------------------------------------ HARD
hA1 = [nm(f"The area (in square units) of the triangle formed by the line {eq(m, m * k)} and the two axes is:", abs(m * k * k) // 2, "Intercepts are $c$ and $-c/m$; area $=\\frac12|c|\\cdot|c/m|$.") for m, k in [(2, 5), (4, 3), (6, 4), (10, 3)]]
hA2 = [nm(f"The $x$-coordinate of the point where $y={ln(m1, c1)}$ and $y={ln(m2, c1 + (m1 - m2) * x0)}$ meet is:", x0, "Equate the two expressions.", pos=False) for m1, m2, c1, x0 in [(5, 2, 1, 4), (7, 3, -2, 5), (6, -1, 4, 3), (8, 4, 3, 6)]]
hA3 = [nm(f"If $p(x)={ln(a, b)}$, then $p(p({k}))=$", a * (a * k + b) + b, "Evaluate the inner value first.", pos=False) for a, b, k in [(2, 3, 4), (3, -1, 2), (4, 1, 3), (2, -5, 6)]]
hA4 = [nm(f"A plan costs ₹{a1} plus ₹{b1} per unit; another costs ₹{a2} plus ₹{b2} per unit. They cost the same for ___ units.", u, "Equate $a_1+b_1x=a_2+b_2x$.") for a1, b1, a2, b2, u in [(100, 20, 220, 10, 12), (50, 15, 170, 5, 12), (80, 25, 200, 15, 12), (60, 30, 360, 10, 15)]]
hA5 = [nm(f"If $x={z}$ is the zero of $kx-{c}$, then $k=$", c // z, "$k z-c=0$.") for z, c in [(4, 28), (7, 56), (3, 33), (9, 72)]]
hA6 = [M4(t, c, w, "Reason about linear polynomials.") for t, c, w in [
    ("If a linear polynomial $ax+b$ has zero $0$, then:", "$b=0$", ["$a=0$", "$a=b$", "$b=1$"]),
    ("The graph of $y=7$ (a constant polynomial) is:", "a horizontal line", ["a vertical line", "a line through the origin", "a point"]),
    ("A linear polynomial whose zero is $-3$ and which takes value $6$ at $x=0$ is:", "$2x+6$", ["$3x+6$", "$2x-6$", "$x+6$"]),
    ("The lines $y=ax+1$ and $y=2x+5$ are parallel when $a=$:", "$2$", ["$5$", "$-2$", "$1$"])]]
hA7 = [nm(f"For the pattern with $n$th term ${ln(d, e, 'n')}$, the sum of the 1st and {t}th terms is:", (d + e) + (d * t + e), "Find each term.", pos=False) for d, e, t in [(6, -1, 10), (5, 2, 12), (9, -4, 8), (7, 3, 15)]]
hA8 = [nm(f"For which value of $n$ is ${ln(d, e, 'n')}={d * j + e}$?", j, "Solve the linear equation.") for d, e, j in [(13, -4, 17), (12, 7, 22), (14, -9, 19), (15, 2, 24)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"Plan A costs ₹{a1} plus ₹{b1} per unit; Plan B costs ₹{a2} plus ₹{b2} per unit. For how many units do both cost the same?", f"${a1}+{b1}x={a2}+{b2}x$", f"$x={u}$ units") for a1, b1, a2, b2, u in [(200, 30, 440, 10, 12), (150, 25, 390, 5, 12), (90, 40, 330, 20, 12), (500, 55, 740, 35, 12)]]
          + [QQ(f"If $p(x)={ln(a, b)}$, find $p(p(x))$ and its value at $x={k}$.", f"$p(p(x))={a}({ln(a, b)})+({b})={ln(a * a, a * b + b)}$", f"Value $={a * a * k + a * b + b}$") for a, b, k in [(3, 4, 2), (2, -7, 5), (4, 3, 1), (5, -2, 3)]]
          + [QQ(f"Find the area of the triangle formed with the axes by the line $y={ln(m, m * k)}$.", f"Intercepts: $y={m * k}$ and $x={-k}$", f"Area $=\\frac12\\times{m * k}\\times{k}={m * k * k // 2}$ sq. units") for m, k in [(2, 7), (4, 5), (6, 2), (10, 5)] if (m * k * k) % 2 == 0])
HARD_C = ([QQ(f"Find the point of intersection of $y={ln(m1, c1)}$ and $y={ln(m2, c2)}$.", f"${ln(m1, c1)}={ln(m2, c2)}$", f"$x={(c2 - c1) // (m1 - m2)}$", f"$y={m1 * ((c2 - c1) // (m1 - m2)) + c1}$") for m1, c1, m2, c2 in [(5, 2, 2, 11), (7, -3, 3, 9), (4, 8, -2, -4), (6, 1, 1, 21), (9, 4, 4, 34), (8, -5, 3, 15)]]
          + [QQ(f"A linear polynomial has $p(1)={a + b}$ and $p(3)={3 * a + b}$. Find $p(x)$, its zero and $p({k})$.", f"$p(3)-p(1)=2a={2 * a}$, so $a={a}$", f"$b={b}$, $p(x)={ln(a, b)}$", f"Zero $x=-\\frac{{{b}}}{{{a}}}$" if (b % a) else f"Zero $x={-b // a}$", f"$p({k})={a * k + b}$") for a, b, k in [(4, 8, 6), (5, -15, 4), (6, 12, 3), (3, -21, 10), (7, 14, 2), (8, -16, 5)]]
          + [QQ(f"The $n$th term of a pattern is ${ln(d, e, 'n')}$. Find the number of terms that are less than {d * j + e} and the sum of the first two terms.", f"${ln(d, e, 'n')}<{d * j + e}$ gives $n<{j}$", f"Terms: $n=1,2,\\dots,{j - 1}$, number $={j - 1}$", f"$a_1+a_2={d + e}+{2 * d + e}={3 * d + 2 * e}$") for d, e, j in [(14, 3, 10), (11, -4, 12), (16, 5, 9), (12, -2, 15), (18, 1, 8), (13, 6, 11)]])
HARD_D = ([QQ(f"Two taxi services: A charges ₹{a1} plus ₹{b1} per km; B charges ₹{a2} plus ₹{b2} per km. Find the distance for which both charge equally, the common fare, and which is cheaper for {k} km.", f"$A(x)={ln(b1, a1)}$, $B(x)={ln(b2, a2)}$", f"${ln(b1, a1)}={ln(b2, a2)}$ gives $x={u}$ km", f"Common fare $={a1 + b1 * u}$", f"For {k} km: A $={a1 + b1 * k}$, B $={a2 + b2 * k}$", f"{'A' if a1 + b1 * k < a2 + b2 * k else 'B'} is cheaper")
           for a1, b1, a2, b2, u, k in [(40, 14, 100, 8, 10, 15), (30, 12, 90, 7, 12, 8), (50, 15, 110, 10, 12, 20), (20, 9, 80, 4, 12, 6), (60, 16, 150, 6, 9, 14), (35, 13, 95, 8, 12, 10)]]
          + [QQ(f"A line passes through ${P(x1, m * x1 + c)}$ and ${P(x2, m * x2 + c)}$. Find its slope, equation, intercepts and the area of the triangle it forms with the axes.", f"Slope $={m}$", f"Equation $y={ln(m, c)}$", f"$y$-intercept ${c}$, $x$-intercept ${-c // m}$", f"Area $=\\frac12\\times{abs(c)}\\times{abs(c // m)}$", f"$={abs(c) * abs(c // m) // 2}$ sq. units" if (abs(c) * abs(c // m)) % 2 == 0 else f"$=\\frac{{{abs(c) * abs(c // m)}}}{{2}}$ sq. units")
             for m, c, x1, x2 in [(3, 12, 1, 4), (5, -10, 2, 6), (4, 16, 0, 3), (6, -12, 1, 5), (2, 14, 3, 7), (7, 21, 2, 8)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
