"""Class 9 Maths Ch 13 - Two Variables, One Line (linear equations in two variables, solutions, intercepts, slope)."""
from g9m import *

SLUG, NAME, CHNO = "Two_Variables_One_Line", "Two Variables, One Line", 13

def term(c, v, first=False):
    if c == 0: return ""
    a = abs(c); body = (v if a == 1 else f"{a}{v}")
    if first: return ("-" if c < 0 else "") + body
    return ("-" if c < 0 else "+") + body
def lin(a, b, c):
    """a x + b y = c"""
    left = term(a, "x", True) + term(b, "y", a == 0)
    return f"{left}={c}"
def lin0(a, b, c):
    """a x + b y + c = 0"""
    left = term(a, "x", True) + term(b, "y", a == 0) + (f"+{c}" if c > 0 else (f"{c}" if c < 0 else ""))
    return f"{left}=0"
def pt(p, q): return f"$({p},{q})$"
def slope_f(m): return s(Fr(m))
def P(r, lo=-9, hi=9): return r.randint(lo, hi)

def sol_point(r, lo, hi):
    """Random line a x + b y = c (a > 0, c > 0, b sometimes negative) with a known solution (x0, y0)."""
    while True:
        a, b = P(r, 1, 7), P(r, 1, 7) * r.choice([1, 1, 1, -1]); x0, y0 = P(r, lo, hi), P(r, lo, hi)
        if a * x0 + b * y0 > 0: return a, b, x0, y0, a * x0 + b * y0

# ---------------- MCQ generators ----------------
def g_coef(lo=1, hi=9):
    def f(r):
        a, b, c = r.choice([-1, 1]) * r.randint(lo, hi), r.choice([-1, 1]) * r.randint(lo, hi), r.randint(lo, hi)
        w = r.choice(["a", "b", "c"]); v = {"a": a, "b": b, "c": -c}[w]
        return nn(f"Writing ${lin(a, b, c)}$ in the form $ax+by+c=0$, the value of ${w}$ is:", v, f"${lin(a, b, c)}$ becomes ${lin0(a, b, -c)}$.", offs=(-2 * v if v else 3, 1, -1, 2, c, -c), fmtf=lambda x: f"${s(x)}$") if v != 0 else None
    return f

def g_is_sol(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        yes = r.random() < 0.5
        px, py = (x0, y0) if yes else (x0 + r.choice([-2, -1, 1, 2]), y0 + r.choice([-1, 1, 2]))
        ok = a * px + b * py == c
        return M4(f"Is the point ${'(' + str(px) + ',' + str(py) + ')'}$ a solution of ${lin(a, b, c)}$?", "Yes" if ok else "No", ["No" if ok else "Yes", "Only for $x=0$", "Cannot be said"], f"${a}({px})+({b})({py})={a*px+b*py}$, {'equal to' if ok else 'not equal to'} ${c}$.")
    return f

def g_y_for_x(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        if abs(b) == 1 and r.random() < .5: return None
        return nn(f"For the equation ${lin(a, b, c)}$, when $x={x0}$ the value of $y$ is:", y0, f"${b}y={c}-({a})({x0})$ gives $y={y0}$.", offs=(1, -1, 2, -2, 3, y0 * -1 if y0 else 5))
    return f

def g_xint(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        xi = Fr(c, a); yi = Fr(c, b)
        if c == 0: return None
        w = r.choice(["x", "y"]); v = xi if w == "x" else yi
        return nn(f"The {w}-intercept of the line ${lin(a, b, c)}$ is:", v, f"Put {'y' if w == 'x' else 'x'}=0: ${w}={s(v)}$.", offs=(1, -1, 2, -v * 2 if v else 4, 5, -5), fmtf=lambda x: f"${s(x)}$")
    return f

def g_slope2(lo, hi):
    def f(r):
        x1, y1, x2, y2 = P(r, lo, hi), P(r, lo, hi), P(r, lo, hi), P(r, lo, hi)
        if x1 == x2 or y1 == y2: return None
        m = Fr(y2 - y1, x2 - x1)
        return nn(f"The slope of the line through $({x1},{y1})$ and $({x2},{y2})$ is:", m, f"$\\dfrac{{{y2}-({y1})}}{{{x2}-({x1})}}={s(m)}$.", offs=(1, -1, 2, Fr(1, 2), -m * 2 if m else 3, 3), fmtf=lambda x: f"${s(x)}$")
    return f

def g_slope_eq(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        m = Fr(-a, b)
        return nn(f"The slope of the line ${lin(a, b, c)}$ is:", m, f"Rewrite as $y={s(m)}x+\\dots$; slope $=-\\frac{{a}}{{b}}$.", offs=(1, -1, 2, -2 * m if m else 4, Fr(1, 2), 3), fmtf=lambda x: f"${s(x)}$")
    return f

def g_k_on(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        return nn(f"The point $({x0},k)$ lies on the line ${lin(a, b, c)}$. The value of $k$ is:", y0, f"${a}({x0})+({b})k={c}$ gives $k={y0}$.", offs=(1, -1, 2, -2, 3, 5))
    return f

def g_a_sol(lo, hi):
    def f(r):
        k = P(r, 2, 9); b = P(r, 1, 6); x0, y0 = P(r, lo, hi), P(r, lo, hi); c = k * x0 + b * y0
        if x0 == 0: return None
        return nn(f"If $({x0},{y0})$ is a solution of $kx{term(b,'y')}={c}$, then $k$ is:", k, f"$k({x0})+{b}({y0})={c}$ gives $k={k}$.", offs=(1, -1, 2, -2, 3, 5))
    return f

def g_slope_int(lo, hi):
    def f(r):
        m, c = r.choice([-1, 1]) * r.randint(1, 9), r.randint(lo, hi)
        w = r.choice(["slope", "y-intercept"])
        v = m if w == "slope" else c
        return nn(f"For the line $y={term(m,'x',True)}{('+' if c >= 0 else '') + str(c)}$, the {w} is:", v, "Compare with $y=mx+c$.", offs=(1, -1, 2, -2, -v * 2 if v else 5, 3))
    return f

def g_through(lo, hi):
    def f(r):
        m = r.randint(1, 6) * r.choice([-1, 1]); x0, y0 = P(r, lo, hi), P(r, lo, hi); c = y0 - m * x0
        return nn(f"A line with slope ${m}$ passes through $({x0},{y0})$. Its $y$-intercept is:", c, f"$y=mx+c$ with $y={y0}$ at $x={x0}$: $c={y0}-({m})({x0})$.", offs=(1, -1, 2, -2, m, 5))
    return f

def g_par_c(lo, hi):
    def f(r):
        a, b = P(r, 1, 6), P(r, 1, 7); m = r.randint(2, 5)
        if a == b: return None
        return nn(f"The line ${lin(a, b, 9)}$ is parallel to the line $kx+{m*b}y=11$. The value of $k$ is:", m * a, f"Equal slopes: $-\\frac{{{a}}}{{{b}}}=-\\frac{{k}}{{{m*b}}}$, so $k={m*a}$.", offs=(1, -1, 2, a, b, 5))
    return f

def g_collin(lo, hi):
    def f(r):
        x1, y1 = P(r, lo, hi), P(r, lo, hi); m = r.choice([-3, -2, -1, 1, 2, 3, 4]); d = r.choice([1, 2, 3]); x2, y2 = x1 + d, y1 + m * d; x3 = x1 + 2 * d
        k = y1 + 2 * m * d
        return nn(f"The points $({x1},{y1})$, $({x2},{y2})$ and $({x3},k)$ are collinear. The value of $k$ is:", k, "Equal slopes between consecutive points.", offs=(1, -1, m, 2, -2, 5))
    return f

def g_num_sol():
    def f(r):
        a, b = r.randint(2, 9), r.randint(2, 9); x0, y0 = r.randint(-5, 8), r.randint(-5, 8); c = a * x0 + b * y0
        pts = [(x0, y0), (x0 + 1, y0), (x0, y0 + 1), (y0, x0)]
        if len(set(pts)) < 4 or any(a * u + b * v == c for u, v in pts[1:]): return None
        t = lambda q: f"$({q[0]},{q[1]})$"
        return M4(f"Which of the following points lies on the line ${lin(a, b, c)}$?", t(pts[0]), [t(q) for q in pts[1:]], f"${a}({x0})+{b}({y0})={c}$".replace("+-", "-"))
    return f

def g_area(lo, hi):
    def f(r):
        p, q = r.randint(lo, hi), r.randint(lo, hi)
        if p == q: return None
        a, b = q, p; c = p * q
        return nn(f"The line ${lin(a, b, c)}$ cuts the axes at two points. The area of the triangle it forms with the axes (square units) is:", Fr(p * q, 2), f"Intercepts ${p}$ and ${q}$; area $=\\frac12\\times{p}\\times{q}$.", offs=(1, -1, 2, p * q, -2, 5), fmtf=lambda x: f"${s(x)}$")
    return f

def g_taxi(lo, hi):
    def f(r):
        fixed, rate = r.randint(*lo), r.randint(*hi); d1, d2 = r.randint(2, 6), r.randint(8, 15); n = r.randint(20, 40)
        return nn(f"A taxi fare is ₹{fixed + rate*d1} for {d1} km and ₹{fixed + rate*d2} for {d2} km (fare is a linear function of distance). The fare for {n} km (in ₹) is:", fixed + rate * n, f"Rate $=\\dfrac{{{rate*(d2-d1)}}}{{{d2-d1}}}={rate}$ per km; fixed charge ${fixed}$.", offs=(rate, -rate, fixed, 10, -10, 20))
    return f

def g_temp(lo, hi):
    def f(r):
        c = r.randint(lo, hi) * 5
        return nn(f"Using $F=\\frac95C+32$, the temperature ${c}^\\circ$C in degrees Fahrenheit is:", c * 9 // 5 + 32, f"$\\frac95\\times{c}+32$.", offs=(1, -1, 9, -9, 10, 18))
    return f

def g_horiz_list(r):
    k = r.randint(2, 9); h = r.choice([True, False])
    return M4(f"The slope of the line ${'y' if h else 'x'}={k}$ is:", "0" if h else "undefined", ["undefined" if h else "0", "1", f"{k}"], "A horizontal line has slope 0; a vertical line has no (undefined) slope.")

CONCEPT = [tx(q, c, w, why) for q, c, w, why in [
    ("The graph of a linear equation in two variables is:", "a straight line", ["a parabola", "a circle", "a pair of points"], "Fact."),
    ("A linear equation in two variables has:", "infinitely many solutions", ["exactly one solution", "exactly two solutions", "no solution"], "Each point on the line."),
    ("The line $ax+by=0$ always passes through:", "the origin", ["$(1,1)$", "$(0,1)$", "no fixed point"], "$(0,0)$ satisfies it."),
    ("The slope of a line measures:", "its steepness", ["its length", "its colour", "its area"], "Rise over run."),
    ("Two lines with the same slope are:", "parallel (or the same line)", ["perpendicular", "always intersecting once", "never straight"], "Equal slopes."),
    ("The line $x=5$ is:", "a vertical line", ["a horizontal line", "a line through the origin", "a line with slope 5"], "All points have $x=5$."),
    ("The line $y=-3$ is:", "a horizontal line", ["a vertical line", "a line through the origin", "a line with slope $-3$"], "All points have $y=-3$."),
    ("A point lies on a line if:", "its coordinates satisfy the equation of the line", ["it is near the line", "its x-coordinate is zero", "its coordinates are equal"], "Definition.")]]

# =============================== EASY ===============================
EASY_A = [draw(100, 4, g_coef(1, 6)), draw(101, 4, g_is_sol(1, 5)), draw(102, 4, g_y_for_x(1, 5)), CONCEPT[:4], draw(103, 4, g_slope_int(-5, 5)), CONCEPT[4:], draw(104, 4, g_k_on(1, 5)), draw(105, 4, g_xint(1, 5))]

def q_coef(r):
    a, b, c = r.choice([-1, 1]) * r.randint(1, 9), r.choice([-1, 1]) * r.randint(1, 9), r.randint(1, 9)
    return QQ(f"Write ${lin(a, b, c)}$ in the form $ax+by+c=0$ and state $a$, $b$ and $c$.", f"${lin0(a, b, -c)}$", f"$a={a}$, $b={b}$, $c={-c}$")
def q_is_sol(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi); yes = r.random() < 0.5
        px, py = (x0, y0) if yes else (x0 + r.choice([-2, -1, 1, 2]), y0 + r.choice([-1, 1, 2]))
        ok = a * px + b * py == c
        return QQ(f"Check whether $({px},{py})$ is a solution of ${lin(a, b, c)}$.", f"Left side $={a}({px})+({b})({py})={a*px+b*py}$", f"Right side $={c}$", "Yes, it is a solution" if ok else "No, it is not a solution")
    return f
def q_two_sol(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        if a * b == 0 or c % a or c % b or c == 0: return None
        return QQ(f"Find two solutions of ${lin(a, b, c)}$ by putting $x=0$ and $y=0$.", f"$x=0$: ${term(b,'y',True)}={c}$ gives $y={s(Fr(c, b))}$, so $(0,{s(Fr(c, b))})$", f"$y=0$: ${term(a,'x',True)}={c}$ gives $x={s(Fr(c, a))}$, so $({s(Fr(c, a))},0)$")
    return f
def q_slope2(lo, hi):
    def f(r):
        x1, y1, x2, y2 = P(r, lo, hi), P(r, lo, hi), P(r, lo, hi), P(r, lo, hi)
        if x1 == x2 or y1 == y2: return None
        m = Fr(y2 - y1, x2 - x1)
        return QQ(f"Find the slope of the line through $({x1},{y1})$ and $({x2},{y2})$.", f"Slope $=\\dfrac{{y_2-y_1}}{{x_2-x_1}}=\\dfrac{{{y2}-({y1})}}{{{x2}-({x1})}}$", f"$={s(m)}$")
    return f
def q_k_on(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        return QQ(f"The point $({x0},k)$ lies on the line ${lin(a, b, c)}$. Find $k$.", f"Substitute $x={x0}$: ${a}({x0})+({b})k={c}$", f"${b}k={c-a*x0}$", f"$k={y0}$")
    return f
def q_si(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        if abs(a) == abs(b) or abs(b) == 1: return None
        m = Fr(-a, b); k = Fr(c, b)
        return QQ(f"Write ${lin(a, b, c)}$ in the form $y=mx+c$ and read off the slope and the $y$-intercept.", f"${term(b,'y',True)}={term(-a,'x',True)}+{c}$", f"$y={s(m)}x{'+' if k >= 0 else ''}{s(k)}$", f"Slope $={s(m)}$, $y$-intercept $={s(k)}$")
    return f
EASY_B = draw(110, 4, q_coef) + draw(111, 4, q_is_sol(1, 5)) + draw(112, 4, q_k_on(1, 5))
EASY_C = draw(113, 6, q_two_sol(1, 6)) + draw(114, 6, q_slope2(0, 6)) + draw(115, 6, q_is_sol(2, 7))
def q_hv(r):
    k = r.randint(2, 9); h = r.choice(["y", "x"])
    return QQ(f"Draw the line ${h}={k}$ in the Cartesian plane (name two points on it) and state its slope.", f"Points: " + (f"$(0,{k})$ and $(5,{k})$" if h == "y" else f"$({k},0)$ and $({k},5)$"), "It is a horizontal line" if h == "y" else "It is a vertical line", "Slope $=0$" if h == "y" else "Slope is undefined (run is 0)")
def q_taxi_e(r):
    rate = r.randint(8, 20); fixed = r.randint(20, 60); n = r.randint(3, 9)
    return QQ(f"A taxi charges ₹{fixed} fixed and ₹{rate} per km. Write the equation relating the fare $y$ (in ₹) and the distance $x$ km and find the fare for {n} km.", f"$y={rate}x+{fixed}$", f"For $x={n}$: $y={rate}\\times{n}+{fixed}$", f"Fare ₹{rate*n+fixed}")
EASY_D = draw(116, 6, q_si(1, 6)) + draw(117, 6, q_taxi_e)

# =============================== NCERT ===============================
NCERT_A = [draw(200, 4, g_is_sol(-6, 6)), draw(201, 4, g_xint(3, 9)), draw(202, 4, g_slope2(-8, 8)), draw(203, 4, g_slope_eq(-6, 6)), draw(204, 4, g_a_sol(1, 6)), draw(205, 4, g_num_sol()), draw(206, 4, g_through(-5, 5)), draw(207, 4, g_horiz_list)]
def q_xy_int(lo, hi):
    def f(r):
        a, b, x0, y0, c = sol_point(r, lo, hi)
        if c == 0 or c % a or c % b: return None
        return QQ(f"Find the points where the line ${lin(a, b, c)}$ cuts the $x$-axis and the $y$-axis.", f"$y=0$: ${term(a,'x',True)}={c}$ gives $x={s(Fr(c,a))}$; point $({s(Fr(c,a))},0)$", f"$x=0$: ${term(b,'y',True)}={c}$ gives $y={s(Fr(c,b))}$; point $(0,{s(Fr(c,b))})$")
    return f
def q_a_sol(lo, hi):
    def f(r):
        k = P(r, 2, 9); b = P(r, 1, 6); x0, y0 = P(r, lo, hi), P(r, lo, hi); c = k * x0 + b * y0
        if x0 == 0: return None
        return QQ(f"If $({x0},{y0})$ is a solution of $kx{term(b,'y')}={c}$, find $k$.", f"Substitute: $k({x0})+{b}({y0})={c}$", f"${x0}k={c-b*y0}$", f"$k={k}$")
    return f
NCERT_B = draw(210, 4, q_xy_int(2, 8)) + draw(211, 4, q_a_sol(-6, 6)) + draw(212, 4, q_si(2, 9))
def q_collin(lo, hi):
    def f(r):
        x1, y1 = P(r, lo, hi), P(r, lo, hi); m = r.choice([-3, -2, -1, 1, 2, 3, 4]); d = r.choice([1, 2, 3]); x2, y2 = x1 + d, y1 + m * d; x3 = x1 + 2 * d; k = y1 + 2 * m * d
        return QQ(f"Find $k$ if the points $({x1},{y1})$, $({x2},{y2})$ and $({x3},k)$ lie on one straight line.", f"Slope of the first two points $=\\dfrac{{{y2}-({y1})}}{{{x2}-({x1})}}={m}$", f"Slope between $({x2},{y2})$ and $({x3},k)$ must also be ${m}$: $\\dfrac{{k-({y2})}}{{{x3-x2}}}={m}$", f"$k={y2}+{m}\\times{x3-x2}={k}$")
    return f
def q_through(lo, hi):
    def f(r):
        m = r.randint(1, 6) * r.choice([-1, 1]); x0, y0 = P(r, lo, hi), P(r, lo, hi); c = y0 - m * x0
        return QQ(f"Find the equation of the line with slope ${m}$ that passes through $({x0},{y0})$, in the form $y=mx+c$.", "Use $y=mx+c$", f"${y0}={m}({x0})+c$ gives $c={c}$", f"$y={term(m,'x',True)}{'+' if c >= 0 else ''}{c}$")
    return f
NCERT_C = draw(213, 6, q_collin(-5, 5)) + draw(214, 6, q_through(-6, 6)) + draw(215, 6, q_slope2(-9, 9))
def q_tab(lo, hi):
    def f(r):
        m, k = r.choice([-1, 1]) * r.randint(1, 4), P(r, lo, hi)
        xs = [-1, 0, 1, 2]; ys = [m * x + k for x in xs]
        return QQ(f"Draw the graph of ${lin(-m, 1, k)}$ using a table of values for $x=-1, 0, 1, 2$. State its slope and where it cuts the $y$-axis.", f"Rewrite as $y={term(m,'x',True)}{'+' if k >= 0 else ''}{k}$; table: " + ", ".join(f"$x={x}\\Rightarrow y={y}$" for x, y in zip(xs, ys)), "Plot the four points; they lie on one straight line", f"Slope $={m}$", f"$y$-intercept $={k}$, i.e. the point $(0,{k})$")
    return f
def q_fahr(r):
    c = r.randint(1, 20) * 5
    return QQ(f"The relation between Fahrenheit $F$ and Celsius $C$ is $F=\\frac95C+32$. Find $F$ when $C={c}$, find $C$ when $F=212$, and say what the slope $\\frac95$ means.", f"$F=\\frac95\\times{c}+32={c*9//5+32}$", "For $F=212$: $\\frac95C=180$, so $C=100$", "Slope $\\frac95$: each $1^\\circ$C rise raises $F$ by $1.8^\\circ$")
NCERT_D = draw(216, 6, q_tab(-4, 4)) + draw(217, 6, q_fahr)

# =============================== MEDIUM ===============================
MED_A = [draw(300, 4, g_slope_eq(-9, 9)), draw(301, 4, g_collin(-9, 9)), draw(302, 4, g_par_c(1, 8)), draw(303, 4, g_area(2, 8)), draw(304, 4, g_taxi((20, 60), (8, 20))),
         draw(305, 4, g_k_on(-9, 9)), draw(306, 4, g_num_sol()), draw(307, 4, g_through(-9, 9))]
def q_taxi2(lo, hi):
    def f(r):
        fixed, rate = r.randint(*lo), r.randint(*hi); d1, d2 = r.randint(2, 6), r.randint(8, 15); n = r.randint(18, 40)
        return QQ(f"A taxi fare is ₹{fixed + rate*d1} for {d1} km and ₹{fixed + rate*d2} for {d2} km. Assuming the fare is linear in the distance, find the fare per km, the fixed charge and the fare for {n} km.", f"Rate $=\\dfrac{{{fixed+rate*d2}-{fixed+rate*d1}}}{{{d2}-{d1}}}={rate}$ per km", f"Fixed charge $={fixed+rate*d1}-{rate}\\times{d1}={fixed}$", f"Fare for {n} km $={rate}\\times{n}+{fixed}$", f"$=$ ₹{fixed+rate*n}")
    return f
def q_par(lo, hi):
    def f(r):
        a, b = P(r, 1, 6), P(r, 1, 7); m = r.randint(2, 5)
        if a == b: return None
        return QQ(f"Find $k$ if the lines ${lin(a, b, 9)}$ and $kx+{m*b}y=11$ are parallel. Why are they not the same line?", f"Slope of the first line $=-\\frac{{{a}}}{{{b}}}$", f"Slope of the second $=-\\frac{{k}}{{{m*b}}}$; equal slopes give $k={m*a}$", f"Constants: $\\frac{{9}}{{11}}\\ne\\frac{{{a}}}{{{m*a}}}$, i.e. the equations are not multiples of each other, so the lines are distinct")
    return f
MED_B = draw(310, 4, q_taxi2((20, 60), (8, 20))) + draw(311, 4, q_par(1, 8)) + draw(312, 4, q_si(7, 12))
def q_area(lo, hi):
    def f(r):
        p, q = r.randint(lo, hi), r.randint(lo, hi)
        if p == q: return None
        return QQ(f"Find the area of the triangle formed by the line ${lin(q, p, p*q)}$ and the coordinate axes.", f"$x$-intercept: put $y=0$: ${q}x={p*q}$, so $x={p}$", f"$y$-intercept: put $x=0$: ${p}y={p*q}$, so $y={q}$", f"Area $=\\frac12\\times{p}\\times{q}={s(Fr(p*q,2))}$ square units")
    return f
def q_line2(lo, hi):
    def f(r):
        m = r.choice([-1, 1]) * r.randint(1, 5); x1, x2 = P(r, lo, hi), P(r, lo, hi); c = P(r, lo, hi)
        if x1 == x2: return None
        y1, y2 = m * x1 + c, m * x2 + c
        return QQ(f"Find the equation of the line through $({x1},{y1})$ and $({x2},{y2})$ in the form $y=mx+c$.", f"Slope $=\\dfrac{{{y2}-({y1})}}{{{x2}-({x1})}}={m}$", f"Use $({x1},{y1})$: ${y1}={m}({x1})+c$", f"$c={c}$", f"$y={term(m,'x',True)}{'+' if c >= 0 else ''}{c}$")
    return f
MED_C = draw(313, 6, q_area(2, 9)) + draw(314, 6, q_collin(-9, 9)) + draw(315, 6, q_line2(-6, 6))
def q_print(lo, hi):
    def f(r):
        fixed, rate = r.randint(*lo), r.randint(*hi); n1, n2, n3 = r.randint(10, 30), r.randint(40, 90), r.randint(100, 200)
        amt = fixed + rate * n3
        return QQ(f"A printing shop charges ₹{fixed + rate*n1} for {n1} pages and ₹{fixed + rate*n2} for {n2} pages (linear charge). Find the equation of the charge $y$ in terms of the number of pages $x$, the charge for {n3} pages and the number of pages for which the charge is ₹{amt + 10*rate}.", f"Slope $=\\dfrac{{{rate*(n2-n1)}}}{{{n2-n1}}}={rate}$", f"Intercept $={fixed+rate*n1}-{rate}\\times{n1}={fixed}$, so $y={rate}x+{fixed}$", f"$x={n3}$: $y={amt}$", f"${amt+10*rate}={rate}x+{fixed}$ gives $x={n3+10}$")
    return f
def q_pairtype(r):
    m = r.choice([2, 3, 4, 5, -2, -3]); k = r.randint(1, 6); x0 = r.randint(1, 5); y0 = m * x0 + m * k; t = r.randint(2, 6)
    c = y0 - m * x0
    return QQ(f"A line has slope ${m}$ and passes through $({x0},{y0})$. Find its equation in the form $y=mx+c$, its $x$-intercept and the value of $y$ when $x={t}$.", f"$y=mx+c$ with $m={m}$: ${y0}={m}({x0})+c$ gives $c={c}$", f"Equation: $y={m}x+{c}$".replace("+-", "-"), f"$x$-intercept: $0={m}x+{c}$ gives $x={-k}$".replace("+-", "-"), f"At $x={t}$: $y={m*t+c}$")
MED_D = draw(316, 6, q_print((10, 40), (2, 9))) + draw(317, 6, q_pairtype)

# =============================== HARD ===============================
def g_inf_k(r):
    b = r.randint(2, 6); sl = r.randint(1, 5); x0, y0 = r.randint(1, 6), r.randint(-4, 6); k = sl * b; c = k * x0 + b * y0
    return nn(f"The line $kx+{b}y={c}$ passes through $({x0},{y0})$. Its slope is:", -sl, f"${k}({x0})+{b}({y0})={c}$ gives $k={k}$; slope $=-\\frac{{k}}{{{b}}}={-sl}$.", offs=(1, -1, 2, -2, sl, 3), pos=False)
def g_sum_int(lo, hi):
    def f(r):
        p, q = r.randint(lo, hi), r.randint(lo, hi)
        if p == q: return None
        return nn(f"The line ${lin(q, p, p*q)}$ has intercepts $p$ on the $x$-axis and $q$ on the $y$-axis. The value of $p+q$ is:", p + q, f"$x$-intercept ${p}$, $y$-intercept ${q}$.", offs=(1, -1, p * q, 2, -2, 5))
    return f
HARD_A = [draw(400, 4, g_area(9, 25)), draw(401, 4, g_taxi((50, 150), (20, 60))), draw(402, 4, g_par_c(7, 16)), draw(403, 4, g_collin(-20, 20)),
          draw(404, 4, g_inf_k), draw(405, 4, g_sum_int(4, 20)), draw(406, 4, g_temp(5, 24)), draw(407, 4, g_slope2(-30, 30))]
def q_inf_k(r):
    b = r.randint(2, 6); sl = r.randint(1, 5); x0, y0 = r.randint(1, 6), r.randint(-4, 6); k = sl * b; c = k * x0 + b * y0
    return QQ(f"The line $kx+{b}y={c}$ passes through the point $({x0},{y0})$. Find $k$, the slope and the $y$-intercept of the line.", f"Substitute: $k({x0})+{b}({y0})={c}$ gives $k={k}$", f"Line: ${lin(k, b, c)}$; $y=-{sl}x+\\frac{{{c}}}{{{b}}}$".replace("+-", "-"), f"Slope $=-\\frac{{{k}}}{{{b}}}=-{sl}$", f"$y$-intercept $=\\frac{{{c}}}{{{b}}}$")
HARD_B = draw(410, 4, q_inf_k) + draw(411, 4, q_area(9, 25)) + draw(412, 4, q_line2(-15, 15))
def q_two_area(lo, hi):
    def f(r):
        p, q = r.randint(lo, hi), r.randint(lo, hi)
        if p == q: return None
        return QQ(f"A line cuts the $x$-axis at $({p},0)$ and the $y$-axis at $(0,{q})$. Find its equation, its slope and the area of the triangle it makes with the axes.", f"Slope $=\\dfrac{{{q}-0}}{{0-{p}}}=-\\frac{{{q}}}{{{p}}}$", f"Equation: $y=-\\frac{{{q}}}{{{p}}}x+{q}$, i.e. ${lin(q, p, p*q)}$", f"Check: $(${p}, 0)$ gives ${q}\\times{p}={p*q}$", f"Area $=\\frac12\\times{p}\\times{q}={s(Fr(p*q, 2))}$ square units")
    return f
def q_cost(r):
    c1, c2 = r.randint(1, 5) * 10, r.randint(6, 12) * 10; n1, n2 = r.randint(2, 6), r.randint(8, 15)
    rate = r.randint(6, 18); fixed = r.randint(30, 90)
    return QQ(f"A water supplier charges a fixed amount plus a rate per kilolitre. For {n1} kL the bill is ₹{fixed + rate*n1} and for {n2} kL it is ₹{fixed + rate*n2}. Find the equation of the bill, and the usage whose bill is ₹{fixed + rate*(n2+7)}. Also find the bill for no usage.", f"Rate $=\\dfrac{{{rate*(n2-n1)}}}{{{n2-n1}}}={rate}$ per kL", f"Fixed charge $={fixed}$; equation $y={rate}x+{fixed}$", f"${fixed+rate*(n2+7)}={rate}x+{fixed}$ gives $x={n2+7}$ kL", f"Bill for 0 kL $={fixed}$, the $y$-intercept")
HARD_C = draw(413, 6, q_two_area(5, 18)) + draw(414, 6, q_cost) + draw(415, 6, q_collin(-30, 30))
def q_midpoint_line(r):
    m = r.choice([-1, 1]) * r.randint(1, 4); x1, x2 = P(r, -9, 0), P(r, 1, 9); c = P(r, -6, 6)
    y1, y2 = m * x1 + c, m * x2 + c
    return QQ(f"A line passes through $({x1},{y1})$ and $({x2},{y2})$. Find its equation, then find $k$ if the point $(k, {m*7+c})$ lies on it, and the $x$-intercept.", f"Slope $=\\dfrac{{{y2}-({y1})}}{{{x2}-({x1})}}={m}$; $y={m}x{'+' if c >= 0 else ''}{c}$", f"${m*7+c}={m}k{'+' if c >= 0 else ''}{c}$ gives $k=7$", f"$x$-intercept: $y=0$ gives $x={s(Fr(-c, m))}$")
HARD_D = draw(416, 6, q_midpoint_line) + draw(417, 6, q_taxi2((50, 150), (20, 60)))

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
