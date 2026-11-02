"""Class 10 Maths Ch 4 - Quadratic Equations (graded banks)."""
from mg import *

SLUG, NAME, CHNO = "Quadratic_Equations", "Quadratic Equations", 4

def QI(r1, r2):
    """integer coefficients of (d1 x - n1)(d2 x - n2) with roots r1, r2"""
    p = from_roots(r1, r2); L = 1
    for c in p: L = lcm(L, F(c).denominator)
    return [int(c * L) for c in p]
def EQ(cs): return poly(cs) + "=0"
def DD(cs): return cs[1] ** 2 - 4 * cs[0] * cs[2]
def split(cs):
    a, b, c = cs; ac = a * c
    for m in range(-abs(ac) - abs(b) - 2, abs(ac) + abs(b) + 3):
        if m != 0 and ac % m == 0 and m + ac // m == b: return m, ac // m
    return None
def rts(r1, r2): return f"{t(r1)}, {t(r2)}" if r1 != r2 else t(r1)
def nature(D): return "two distinct real roots" if D > 0 else ("two equal real roots" if D == 0 else "no real roots")
NAT = ["two distinct real roots", "two equal real roots", "no real roots", "one real root and one imaginary root"]
def MNAT(cs, why=""):
    D = DD(cs); return MS(f"The nature of the roots of ${EQ(cs)}$ is:", nature(D), [x for x in NAT if x != nature(D)], f"$D=b^2-4ac={D}$")

def SOLF(r1, r2):
    cs = QI(r1, r2); m, n = split(cs)
    return Q(f"Solve by factorisation: ${EQ(cs)}$.", f"Split the middle term: ${cs[1]}={m}{sg(n)}$ because $ac={cs[0]*cs[2]}$ (1); regroup and factorise (1); roots $x={rts(r1,r2)}$ (1).", "1+1+1")
def SOLQ(cs):
    a, b, c = cs; D = DD(cs); sq_ = isqrt(D) if D >= 0 else 0
    if D >= 0 and sq_ * sq_ == D:
        r1, r2 = F(-b + sq_, 2 * a), F(-b - sq_, 2 * a)
        res = f"$D=({b})^2-4({a})({c})={D}$ (1); $x=\\dfrac{{{-b}\\pm{sq_}}}{{{2*a}}}$ (1); roots $x={rts(r1,r2)}$ (1)."
    elif D > 0:
        res = f"$D=({b})^2-4({a})({c})={D}>0$ (1); $x=\\dfrac{{{-b}\\pm\\sqrt{{{D}}}}}{{{2*a}}}$ (1); roots $\\dfrac{{{-b}+\\sqrt{{{D}}}}}{{{2*a}}}$ and $\\dfrac{{{-b}-\\sqrt{{{D}}}}}{{{2*a}}}$ (1)."
    else:
        res = f"$D=({b})^2-4({a})({c})={D}<0$ (2); no real roots (1)."
    return Q(f"Find the roots of ${EQ(cs)}$ using the quadratic formula (if they exist).", res, "1+1+1")
def SOLC(r1, r2):
    cs = QI(r1, r2); a, b, c = cs
    return Q(f"Solve by completing the square: ${EQ(cs)}$.", f"Divide by ${a}$: $x^2{sg(F(b,a))}x{sg(F(c,a))}=0$ (1); $\\left(x{sg(F(b,2*a))}\\right)^2={t(F(b*b,4*a*a)-F(c,a))}$ (1); $x{sg(F(b,2*a))}=\\pm{t(abs(r1-r2)/2)}$, so $x={rts(r1,r2)}$ (1).", "1+1+1")
def CONS(n):
    return Q(f"The product of two consecutive positive integers is {n*(n+1)}. Find the integers.", f"Let integers be $x$ and $x+1$: $x(x+1)={n*(n+1)}$ (1); $x^2+x-{n*(n+1)}=0$ (1); $(x-{n})(x+{n+1})=0$, $x={n}$ (1); integers ${n}$ and ${n+1}$ (1).", "1+1+1+1")
def RECT(b, d):
    A = b * (b + d)
    return Q(f"The length of a rectangular plot exceeds its breadth by {d} m and its area is {A} m². Find its dimensions.", f"Breadth $x$, length $x+{d}$: $x(x+{d})={A}$ (1); $x^2+{d}x-{A}=0$ (1); $(x-{b})(x+{b+d})=0$ (1); $x={b}$ m (breadth), length ${b+d}$ m (reject negative) (2).", "1+1+1+2")
def AGEQ(a, b, k):
    return Q(f"The sum of the ages of two friends is {a+b} years. {k} years ago the product of their ages was {(a-k)*(b-k)}. Find their present ages.", f"Ages $x$ and ${a+b}-x$: $(x-{k})({a+b-k}-x)={(a-k)*(b-k)}$ (1); simplifying $x^2-{a+b}x+{a*b}=0$ (2); $(x-{a})(x-{b})=0$ (1); ages ${a}$ and ${b}$ years (1).", "1+2+1+1")
def SPEED(m, s, h):
    v = s * m; D = h * m * (m + 1) * s
    return Q(f"A train travels {D} km at a uniform speed. If the speed had been {s} km/h more, it would have taken {h} hour{'s' if h>1 else ''} less for the journey. Find the original speed.", f"Speed $x$: $\\dfrac{{{D}}}{{x}}-\\dfrac{{{D}}}{{x+{s}}}={h}$ (1); ${D*s}={h}x(x+{s})$ so $x^2+{s}x-{D*s//h}=0$ (2); $(x-{v})(x+{v+s})=0$ (1); speed ${v}$ km/h (1).", "1+2+1+1")
def TRI(a, b, c):
    d = b - a
    return Q(f"The altitude of a right triangle is {d} cm less than its base and the hypotenuse is {c} cm. Find the base and altitude.", f"Base $x$, altitude $x-{d}$: $x^2+(x-{d})^2={c*c}$ (1); $2x^2-{2*d}x+{d*d-c*c}=0$, i.e. $x^2-{d}x-{F(c*c-d*d,2)}=0$ (2); $(x-{b})(x+{a})=0$ (1); base ${b}$ cm, altitude ${a}$ cm (1).", "1+2+1+1")
def STREAM(v, w, d1):
    T = F(d1, v - w) + F(d1, v + w)
    return Q(f"A motorboat goes {d1} km upstream and {d1} km downstream in {t(T)} hours. If the speed of the stream is {w} km/h, find the speed of the boat in still water.", f"Boat speed $x$: $\\dfrac{{{d1}}}{{x-{w}}}+\\dfrac{{{d1}}}{{x+{w}}}={t(T)}$ (1); ${d1}(2x)={t(T)}(x^2-{w*w})$ (1); roots of the resulting quadratic: $x={v}$ or negative (1); speed ${v}$ km/h (1).", "1+1+1+1")

# ---------------- EASY ----------------
E1 = [(2, 3), (-1, 4), (3, 5), (-2, 6), (1, 7), (4, 5), (-3, -4), (2, -5), (6, -1), (-2, 3)]
eA = [[MS("Which of the following is a quadratic equation?", f"$x^2{sg(b)}x{sg(c)}=0$", [f"$x^3{sg(b)}x{sg(c)}=0$", f"${b}x{sg(c)}=0$", f"$x{sg(b)}={c}$"], "Degree must be 2") for b, c in [(3, 2), (-5, 6), (4, 1), (7, -2), (2, 9), (-1, 3)]],
      [MS(f"Is $x={k}$ a root of ${EQ(cs)}$?", "Yes" if ev(cs, k) == 0 else "No", ["No" if ev(cs, k) == 0 else "Yes", "Cannot say", "Only for $x>0$"], f"LHS $={t(ev(cs,k))}$ at $x={k}$") for cs, k in [([1, -5, 6], 2), ([1, -5, 6], 4), ([1, 2, -8], 2), ([1, 3, 2], -1), ([1, -3, 4], 1)]],
      [MN(f"In ${EQ([a,b,c])}$, the value of $b$ is:", b, why="Compare with $ax^2+bx+c=0$") for a, b, c in [(2, -3, 5), (3, 7, -2), (1, -4, 9), (5, 6, 1), (4, -8, 3)]],
      [MS(f"The roots of $(x{sg(-r1)})(x{sg(-r2)})=0$ are:", rts(r1, r2).replace(", ", " and "), [f"{t(-r1)} and {t(-r2)}" if r1 != -r2 else "1 and 2", f"{t(r1)} and {t(-r2)}" if r2 != 0 else "0 and 1", f"{t(r1+r2)} and {t(r1*r2)}"], "Put each factor equal to zero") for r1, r2 in E1[:5]],
      [MN(f"The discriminant of ${EQ(cs)}$ is:", DD(cs), why="$D=b^2-4ac$") for cs in [[1, -5, 6], [2, 3, 1], [1, 4, 4], [3, -2, -1], [1, 1, 3]]],
      [MNAT(cs) for cs in [[1, -5, 6], [1, 2, 1], [1, 1, 3], [2, -4, 2]]]]
eB = ([Q(f"Check whether $x={k}$ is a root of ${EQ(cs)}$.", f"Put $x={k}$: LHS $={t(ev(cs,k))}$ (1); " + ("equals RHS 0, so it is a root (1)." if ev(cs, k) == 0 else "not equal to 0, so it is not a root (1)."), "1+1") for cs, k in [([1, -7, 10], 2), ([1, -7, 10], 3), ([2, -5, 3], 1), ([1, 0, -16], -4)]]
      + [Q(f"Find the roots of $(x{sg(-r1)})(x{sg(-r2)})=0$.", f"$x{sg(-r1)}=0$ or $x{sg(-r2)}=0$ (1); $x={t(r1)}$ or $x={t(r2)}$ (1).", "1+1") for r1, r2 in E1[5:9]]
      + [Q(f"Find the discriminant of ${EQ(cs)}$ and state the nature of its roots.", f"$D=({cs[1]})^2-4({cs[0]})({cs[2]})={DD(cs)}$ (1); {nature(DD(cs))} (1).", "1+1") for cs in [[1, -6, 8], [1, -4, 4], [2, 1, 3], [3, -7, 2]]])
eC = ([SOLF(r1, r2) for r1, r2 in [(2, 3), (-1, 5), (4, 6), (-3, 7), (1, 8), (-4, -2)]]
      + [Q(f"Find the discriminant of ${EQ(cs)}$ and hence the nature of its roots.", f"$a={cs[0]}$, $b={cs[1]}$, $c={cs[2]}$ (1); $D={DD(cs)}$ (1); {nature(DD(cs))} (1).", "1+1+1") for cs in [[2, -4, 3], [1, -8, 16], [3, 5, -2], [1, 6, 10], [5, -10, 5], [2, 7, 3]]]
      + [CONS(n) for n in [4, 6, 8, 11, 13, 15]])
eD = ([SOLF(*r) for r in [(F(1, 2), 3), (F(-2, 3), 1), (F(3, 2), -2), (F(1, 3), 2), (F(-3, 4), 2), (F(5, 2), -1)]]
      + [RECT(b, d) for b, d in [(6, 5), (8, 4), (10, 3), (7, 6), (9, 8), (12, 5)]])

# ---------------- NCERT ----------------
N1 = [(3, 5), (-4, 6), (2, 9), (-5, 3), (1, 10), (7, -2), (4, 8)]
nA = [[MN(f"For the equation ${EQ([1,-b,c])}$, the sum of the roots is:", b, why="Sum $=-b/a$") for b, c in [(7, 12), (9, 20), (11, 28), (8, 15), (13, 36)]],
      [MN(f"For $x^2-{2*m}x+k=0$ to have equal roots, $k=$", m * m, why="$D=0$: $4m^2-4k=0$") for m in [3, 4, 5, 6, 7]],
      [MN(f"If one root of $x^2-{r1+r2}x+k=0$ is {r1}, then $k$ is:", r1 * r2, why=f"Other root ${r2}$; product $=k$") for r1, r2 in [(2, 7), (3, 8), (4, 9), (5, 6), (6, 10)]],
      [MS(f"The roots of $x^2{sg(-(r1+r2))}x{sg(r1*r2)}=0$ are:", f"{t(r1)} and {t(r2)}", [f"{t(-r1)} and {t(-r2)}", f"{t(r1)} and {t(-r2)}", f"{t(-r1)} and {t(r2)}"], "Factorise") for r1, r2 in N1[:5]],
      [MN(f"The discriminant of ${EQ(cs)}$ is:", DD(cs), why="$D=b^2-4ac$") for cs in [[2, -7, 3], [3, 2, 5], [1, -9, 20], [4, 4, 1], [5, 3, -1]]],
      [MNAT(cs) for cs in [[2, -6, 3], [3, 2, 1], [1, -10, 25], [4, -4, 1], [2, 5, 4]]]]
nB = ([Q(f"Represent the situation as a quadratic equation: The product of two consecutive positive integers is {n*(n+1)}.", f"Integers $x,x+1$: $x(x+1)={n*(n+1)}$ (1); $x^2+x-{n*(n+1)}=0$ (1).", "1+1") for n in [8, 9, 10, 12]]
      + [Q(f"Find the roots of ${EQ(QI(*r))}$ by factorisation.", f"Split the middle term and factorise (1); roots ${rts(*r)}$ (1).", "1+1") for r in [(F(3, 2), 2), (F(-1, 2), 3), (F(2, 3), -1), (F(-5, 2), 1)]]
      + [Q(f"Find $k$ for which $x^2-{2*m}x+k=0$ has two equal roots.", f"$D=0$: $({2*m})^2-4k=0$ (1); $k={m*m}$ (1).", "1+1") for m in [4, 5, 6, 8]])
nC = ([SOLQ(cs) for cs in [[2, -7, 3], [1, -6, 4], [3, -5, 1], [2, 5, -3], [1, 2, 5], [5, -3, -2]]]
      + [SOLC(*r) for r in [(2, 4), (-3, 5), (F(1, 2), 3), (-2, 6), (1, -7), (F(-1, 3), 2)]]
      + [Q(f"Find the values of $k$ for which $x^2+kx+{m*m}=0$ has equal roots.", f"$D=k^2-4({m*m})=0$ (1); $k^2={4*m*m}$ (1); $k=\\pm{2*m}$ (1).", "1+1+1") for m in [2, 3, 4, 5, 6, 7]])
nD = ([SPEED(*p) for p in [(8, 5, 1), (6, 10, 1), (5, 4, 2)]] + [TRI(*p) for p in [(8, 15, 17), (12, 16, 20), (9, 12, 15)]]
      + [RECT(b, d) for b, d in [(15, 7), (11, 9), (20, 5)]] + [AGEQ(*p) for p in [(30, 12, 5), (27, 9, 6), (35, 14, 7)]])

# ---------------- MEDIUM ----------------
M1 = [(F(1, 2), 4), (F(2, 3), -3), (-F(3, 2), 5), (F(1, 3), 6), (F(3, 4), -2), (-F(2, 5), 3)]
def SOLR(r1, r2):
    cs = QI(r1, r2)
    return Q(f"Solve for $x$: ${EQ(cs)}$ by the quadratic formula.", f"$D=({cs[1]})^2-4({cs[0]})({cs[2]})={DD(cs)}$ (1); $x=\\dfrac{{{-cs[1]}\\pm{isqrt(DD(cs))}}}{{{2*cs[0]}}}$ (1); roots ${rts(r1,r2)}$ (1).", "1+1+1")
def KEQ(m, p):
    return Q(f"If $x={p}$ is a root of $x^2-{m}x+k=0$, find $k$ and the other root.", f"Put $x={p}$: ${p*p}-{m*p}+k=0$ (1); $k={m*p-p*p}$ (1); other root $={m}-{p}={m-p}$ (1).", "1+1+1")
mA = [[MN(f"The sum of the roots of ${EQ(cs)}$ is:", F(-cs[1], cs[0]), why="Sum $=-b/a$") for cs in [QI(*r) for r in M1[:5]]],
      [MN(f"The product of the roots of ${EQ(cs)}$ is:", F(cs[2], cs[0]), why="Product $=c/a$") for cs in [QI(*r) for r in M1[:5]]],
      [MN(f"The roots of ${EQ(QI(r1,r2))}$ differ by:", abs(r1 - r2), why="Roots are " + rts(r1, r2)) for r1, r2 in [(2, 9), (-3, 5), (4, 11), (-6, 2), (1, 8)]],
      [MN(f"If $x={p}$ is a root of $x^2-{m}x+k=0$, then $k=$", m * p - p * p, why=f"${p*p}-{m*p}+k=0$") for m, p in [(9, 4), (11, 5), (10, 3), (13, 6), (12, 7)]],
      [MS(f"The equation $x^2+{b}x+{c}=0$ has:", nature(b * b - 4 * c), [x for x in NAT if x != nature(b * b - 4 * c)], f"$D={b*b-4*c}$") for b, c in [(6, 8), (4, 4), (3, 5), (7, 10), (2, 9), (8, 16)]],
      [MN(f"The larger root of $x^2-{r1+r2}x+{r1*r2}=0$ is:", max(r1, r2), why="Factorise") for r1, r2 in [(3, 8), (5, 9), (4, 12), (6, 7), (2, 13)]]]
mB = ([SOLR(*r) for r in M1[:4]] + [KEQ(*p) for p in [(9, 4), (11, 5), (10, 3), (13, 6)]]
      + [Q(f"Find $k$ so that $kx^2-{2*m}x+{n}=0$ has equal roots.", f"$D=0$: $({2*m})^2-4k({n})=0$ (1); $k={t(F(m*m,n))}$ (1).", "1+1") for m, n in [(3, 1), (4, 2), (6, 3), (5, 5)]])
mC = ([Q(f"Solve for $x$: $\\dfrac{{1}}{{x}}+\\dfrac{{1}}{{x+{d}}}={t(F(1,r1)+F(1,r1+d))}$.", f"Multiply by $x(x+{d})$: $2x+{d}={t(F(1,r1)+F(1,r1+d))}x(x+{d})$ (1); form the quadratic with integer coefficients (1); positive root $x={r1}$ (1).", "1+1+1") for r1, d in [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (5, 1)]]
      + [Q(f"Find the nature of the roots of ${EQ(cs)}$ and, if real, find them.", f"$D={DD(cs)}$ (1); {nature(DD(cs))} (1); " + (f"roots ${rts(F(-cs[1]+isqrt(DD(cs)),2*cs[0]),F(-cs[1]-isqrt(DD(cs)),2*cs[0]))}$ (1)." if DD(cs) >= 0 and isqrt(DD(cs)) ** 2 == DD(cs) else "no real roots exist (1)."), "1+1+1") for cs in [[3, -7, 2], [2, 5, 4], [4, -12, 9], [1, -2, 5], [5, 6, 1], [2, -3, 4]]]
      + [SOLC(*r) for r in [(3, 7), (-4, 2), (F(1, 2), 5), (-1, 9), (2, -6), (F(2, 3), 4)]])
mD = ([SPEED(*p) for p in [(4, 5, 2), (7, 5, 1), (6, 5, 2), (5, 8, 1)]] + [TRI(*p) for p in [(5, 12, 13), (7, 24, 25), (20, 21, 29), (8, 15, 17)][:3]] + [STREAM(*p) for p in [(8, 2, 15), (10, 2, 24), (9, 3, 24)]] + [AGEQ(*p) for p in [(25, 11, 4), (32, 14, 8)]])

# ---------------- HARD ----------------
def PQ(p, q): return QI(p, q)
hA = [[MN(f"If the roots of $x^2-{s}x+{pp}=0$ are $\\alpha,\\beta$, then $\\alpha^2+\\beta^2=$", s * s - 2 * pp, why="$(\\alpha+\\beta)^2-2\\alpha\\beta$") for s, pp in [(7, 10), (9, 14), (10, 21), (11, 24), (8, 12)]],
      [MN(f"If the roots of $x^2-{s}x+k=0$ differ by {d}, then $k=$", F(s * s - d * d, 4), why="$(\\alpha-\\beta)^2=(\\alpha+\\beta)^2-4\\alpha\\beta$") for s, d in [(10, 2), (12, 4), (14, 6), (16, 2), (18, 8)]],
      [MN(f"For which value of $k$ does $x^2+kx+{m}=0$ have equal roots (take $k>0$)?", F(2 * isqrt(m), 1), why="$D=0$ gives $k^2=4m$") for m in [9, 16, 25, 36, 49]],
      [MN(f"The value of $k$ for which $x={r}$ is a root of $kx^2+{b}x{sg(c)}=0$ with $b={b}$, $c={c}$ is:", F(-(b * r + c), r * r), why="Substitute the root") for r, b, c in [(1, 3, -5), (2, -3, -2), (-1, 4, 6), (3, -5, -3), (2, 1, -10)]],
      [MS(f"The equation $kx^2+{b}x+{c}=0$ has real roots when:", f"$k\\le{t(F(b*b,4*c))}$ and $k\\ne0$", [f"$k\\ge{t(F(b*b,4*c))}$", f"$k<{t(F(b*b,4*c))}$ only", f"$k>0$"], f"$D={b*b}-{4*c}k\\ge0$") for b, c in [(6, 3), (4, 2), (8, 4), (10, 5), (2, 1)]],
      [MN(f"If $\\alpha,\\beta$ are roots of $x^2-{s}x+{pp}=0$, then $\\dfrac{{1}}{{\\alpha}}+\\dfrac{{1}}{{\\beta}}=$", F(s, pp), why="$\\dfrac{\\alpha+\\beta}{\\alpha\\beta}$") for s, pp in [(5, 6), (7, 12), (9, 20), (8, 15), (11, 18)]]]
def KDIS(a, c):
    return Q(f"Find the values of $k$ for which $kx^2+{2*a}x+{c}=0$ has real and equal roots.", f"$D=({2*a})^2-4k({c})=0$ (1); $k={t(F(a*a,c))}$ (1).", "1+1")
hB = ([KDIS(*p) for p in [(2, 1), (3, 3), (4, 8), (5, 5)]]
      + [Q(f"If $\\alpha,\\beta$ are the roots of $x^2-{s}x+{pp}=0$, find $\\alpha^2+\\beta^2$.", f"$\\alpha+\\beta={s}$, $\\alpha\\beta={pp}$ (1); $\\alpha^2+\\beta^2={s}^2-2({pp})={s*s-2*pp}$ (1).", "1+1") for s, pp in [(6, 5), (8, 7), (9, 8), (10, 9)]]
      + [Q(f"The sum of a number and its reciprocal is ${t(F(n*n+1,n))}$. Find the number.", f"Let number $x$: $x+\\frac{{1}}{{x}}={t(F(n*n+1,n))}$ (1); $x={n}$ or $x=\\frac{{1}}{{{n}}}$ (1).", "1+1") for n in [2, 3, 4, 5]])
hC = ([Q(f"Solve for $x$: $\\dfrac{{x+{a}}}{{x-{a}}}+\\dfrac{{x-{a}}}{{x+{a}}}={t(F(2*(b*b+a*a),b*b-a*a))}$.", f"LHS $=\\dfrac{{2(x^2+{a*a})}}{{x^2-{a*a}}}$ (1); cross-multiplying: ${b*b-a*a}(x^2+{a*a})={b*b+a*a}(x^2-{a*a})$ (1); $x^2={b*b}$ so $x=\\pm{b}$ (1).", "1+1+1") for a, b in [(1, 2), (2, 3), (1, 3), (3, 5), (2, 5), (1, 4)]]
      + [Q(f"For what values of $k$ does $x^2+{b}x+k=0$ have real roots? Find the greatest integer value of $k$.", f"$D={b*b}-4k\\ge0$ (1); $k\\le{t(F(b*b,4))}$ (1); greatest integer $k={b*b//4}$ (1).", "1+1+1") for b in [5, 7, 9, 11, 13, 15]]
      + [Q(f"The sum of the squares of two consecutive odd positive integers is {a*a+(a+2)**2}. Find them.", f"Integers $x$, $x+2$: $x^2+(x+2)^2={a*a+(a+2)**2}$ (1); $x^2+2x-{(a*a+(a+2)**2-4)//2}=0$ (1); $x={a}$; integers ${a}$ and ${a+2}$ (1).", "1+1+1") for a in [5, 7, 9, 11, 13, 15]])
def TAPS(x, d):
    T = F(x * (x - d), 2 * x - d)
    return Q(f"Two taps running together fill a tank in ${t(T)}$ hours. The larger tap alone takes {d} hours less than the smaller one. Find the time each takes alone.", f"Smaller tap $x$ h, larger $x-{d}$ h: $\\dfrac{{1}}{{x}}+\\dfrac{{1}}{{x-{d}}}=\\dfrac{{1}}{{{t(T)}}}$ (2); simplify to a quadratic and solve, rejecting the root less than {d}: $x={x}$ (2); times ${x}$ h and ${x-d}$ h (1).", "2+2+1")
hD = ([TAPS(*p) for p in [(10, 5), (12, 4), (15, 5), (9, 3)]] + [STREAM(*p) for p in [(12, 3, 36), (15, 5, 40), (14, 2, 48), (16, 4, 60)]] + [SPEED(*p) for p in [(6, 10, 2), (8, 5, 3), (5, 12, 1), (9, 4, 2)]])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
