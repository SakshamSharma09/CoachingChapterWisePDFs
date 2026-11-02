"""Helpers for Class 9/10 Maths graded banks (mine). All numbers exact via Fraction."""
from fractions import Fraction as F
from math import gcd, isqrt, sqrt, comb, factorial, pi
from common import M4, Q, grp

def t(x):
    """tex (no $) of int/Fraction"""
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return ("-" if x < 0 else "") + f"\\frac{{{abs(x.numerator)}}}{{{x.denominator}}}"

def n(x):
    """option text for a number"""
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"${t(x)}$"

def d2(x, p=2):
    """decimal string with p places trimmed"""
    s = f"{float(x):.{p}f}"
    return s.rstrip("0").rstrip(".") if "." in s else s

def sg(x):
    """signed term for '+ x' constructions: returns '+3' or '-3'"""
    x = F(x)
    return ("+" if x >= 0 else "-") + t(abs(x))

def co(c, v="x"):
    """coefficient*variable, e.g. co(1,'x')='x', co(-1)='-x', co(3)='3x'"""
    c = F(c)
    if c == 1: return v
    if c == -1: return "-" + v
    return t(c) + v

def lin(a, b, v="x"):
    """ax+b as tex"""
    a, b = F(a), F(b)
    s = ""
    if a != 0: s = co(a, v)
    if b != 0 or a == 0: s += (sg(b) if a != 0 else t(b))
    return s

def poly(cs, v="x"):
    """cs highest degree first: poly([1,-5,6]) -> x^2-5x+6"""
    deg = len(cs) - 1; s = ""
    for i, c in enumerate(cs):
        c = F(c); e = deg - i
        if c == 0: continue
        sign = "-" if c < 0 else ("+" if s else "")
        a = abs(c)
        body = (t(a) if (a != 1 or e == 0) else "") + (v if e >= 1 else "") + (f"^{{{e}}}" if e > 1 else "")
        s += sign + body
    return s or "0"

def ev(cs, x):
    r = F(0)
    for c in cs: r = r * F(x) + F(c)
    return r

def pad(c, extra=()):
    """list of wrong numeric options near c (deduped, c excluded)"""
    c = F(c); out = []
    for x in list(extra) + [c + 1, c - 1, c + 2, c - 2, 2 * c, -c, c + 3, c - 3, c + 4, c + 5]:
        x = F(x)
        if x != c and x not in out: out.append(x)
    return out

def MN(q, c, w=(), why="", tex=None):
    """numeric MCQ: c correct value, w wrong values (auto padded)"""
    c = F(c); ws = pad(c, w)[:3] if len(set(map(F, w)) - {c}) >= 3 else None
    if ws is None:
        ws = []
        for x in list(w) + pad(c):
            x = F(x)
            if x != c and x not in ws: ws.append(x)
        ws = ws[:3]
    return M4(q, n(c), [n(x) for x in ws], why)

def MS(q, c, w, why=""):
    return M4(q, c, w, why)

def T(A, B, C, D):
    return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))

def pp(*xs):
    """flatten helper"""
    out = []
    for x in xs: out += x
    return out

def lcm(a, b): return a * b // gcd(a, b)
def isp(k): return k > 1 and all(k % d for d in range(2, isqrt(k) + 1))
def fac(k):
    f = {}; p = 2
    while p * p <= k:
        while k % p == 0: f[p] = f.get(p, 0) + 1; k //= p
        p += 1
    if k > 1: f[k] = f.get(k, 0) + 1
    return f
def ftex(k):
    return r"\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(fac(k).items()))
def sq(x): return F(x) * F(x)

def pdiv(n, d):
    """polynomial long division, coef lists highest first. returns (q, r) as lists of Fractions"""
    n = [F(x) for x in n]; d = [F(x) for x in d]; q = []
    while len(n) >= len(d):
        c = n[0] / d[0]; q.append(c)
        for i in range(len(d)): n[i] -= c * d[i]
        n.pop(0)
    while n and n[0] == 0 and len(n) > 1: n.pop(0)
    return q or [F(0)], n or [F(0)]

def pmul(a, b):
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += F(x) * F(y)
    return r

def from_roots(*rs, a=1):
    p = [F(a)]
    for r in rs: p = pmul(p, [1, -F(r)])
    return p

# ---------------- linear-system word-problem factories (Class 10 Ch3) ----------------
def lx(a, b):
    a, b = F(a), F(b)
    s = co(a, "x") if a != 0 else ""
    if b != 0: s += (("+" if b > 0 else "-") if a != 0 else ("-" if b < 0 else "")) + co(abs(b), "y")
    return s
def E(a, b, c): return f"{lx(a,b)}={t(c)}"
def sol_cost(a1, b1, c1, a2, b2, c2):
    return (F(c1 * b2 - c2 * b1, a1 * b2 - a2 * b1), F(a1 * c2 - a2 * c1, a1 * b2 - a2 * b1))
def DIG(a_, b_):
    s = a_ + b_; df = b_ - a_
    return Q(f"The sum of the digits of a two-digit number is {s}. If the digits are interchanged, the number becomes {abs(9*df)} {'more' if df > 0 else 'less'}. Find the number.",
             f"Let tens digit $x$, ones digit $y$: $x+y={s}$ (1); $(10y+x)-(10x+y)={9*df}$ so $y-x={df}$ (1); $x={a_}$, $y={b_}$, number ${10*a_+b_}$ (1).", "1+1+1")
def AGE(m, n, y):
    x = F(y * (n - 1), m - n)
    return Q(f"A father is {m} times as old as his son. After {y} years the father will be {n} times as old as the son will be. Find their present ages.",
             f"Son $x$, father ${m}x$ (1); ${m}x+{y}={n}(x+{y})$ (2); $x={t(x)}$ (1); son {t(x)} years, father {t(m*x)} years (1).", "1+2+1+1")
def BOAT(u, v, d1, d2, d3, d4):
    h1 = F(d1, u) + F(d2, v); h2 = F(d3, u) + F(d4, v)
    return Q(f"A boat goes {d1} km upstream and {d2} km downstream in {t(h1)} hours, and {d3} km upstream and {d4} km downstream in {t(h2)} hours. Find the speed of the boat in still water and the speed of the stream.",
             f"Let boat $x$ km/h, stream $y$ km/h; put $p=\\frac{{1}}{{x-y}}$, $q=\\frac{{1}}{{x+y}}$: ${d1}p+{d2}q={t(h1)}$, ${d3}p+{d4}q={t(h2)}$ (2); $p=\\frac{{1}}{{{u}}}$, $q=\\frac{{1}}{{{v}}}$ (1); $x-y={u}$, $x+y={v}$ (1); boat ${t(F(u+v,2))}$ km/h, stream ${t(F(v-u,2))}$ km/h (1).", "2+1+1+1")
def FRAC(x, y, a, b):
    f1 = F(x + a, y + a); f2 = F(x + b, y + b)
    return Q(f"A fraction becomes ${t(f1)}$ when {a} is added to both the numerator and the denominator, and becomes ${t(f2)}$ when {b} is added to both. Find the fraction.",
             f"Let fraction $\\frac{{x}}{{y}}$: ${f1.denominator}(x+{a})={f1.numerator}(y+{a})$ and ${f2.denominator}(x+{b})={f2.numerator}(y+{b})$ (2); simplify and solve (2); $x={x}$, $y={y}$, fraction $\\frac{{{x}}}{{{y}}}$ (1).", "2+2+1")
def TAXI(f0, r, d1, d2, d3):
    return Q(f"The taxi charges consist of a fixed charge plus a charge per km. For {d1} km the fare is ₹{f0+r*d1} and for {d2} km it is ₹{f0+r*d2}. Find the fixed charge, the charge per km and the fare for {d3} km.",
             f"Fixed $x$, per km $y$: $x+{d1}y={f0+r*d1}$, $x+{d2}y={f0+r*d2}$ (2); subtract: ${d2-d1}y={r*(d2-d1)}$, $y={r}$ (1); $x={f0}$ (1); fare for {d3} km $={f0}+{r}\\times{d3}={f0+r*d3}$ (1).", "2+1+1+1")
def RECT(l, w, a, c, e, f):
    k1 = l * w - (l - a) * (w + c); k2 = (l + e) * (w + f) - l * w
    return Q(f"If the length of a rectangle is reduced by {a} units and its breadth is increased by {c} units, its area {'decreases' if k1>0 else 'increases'} by {abs(k1)} square units. If the length is increased by {e} units and the breadth by {f} units, the area increases by {k2} square units. Find the length and breadth.",
             f"Length $x$, breadth $y$: $(x-{a})(y+{c})=xy{sg(-k1)}$ gives ${c}x-{a}y={a*c-k1}$ (1.5); $(x+{e})(y+{f})=xy+{k2}$ gives ${f}x+{e}y={k2-e*f}$ (1.5); solving, $x={l}$, $y={w}$ (2).", "1.5+1.5+2")
def TRAIN(u, v, D, a, b):
    h1 = F(a, u) + F(D - a, v); h2 = F(b, u) + F(D - b, v)
    return Q(f"A man travels {D} km partly by train and partly by bus. If he travels {a} km by train and the rest by bus, he takes {t(h1)} hours; if he travels {b} km by train and the rest by bus, he takes {t(h2)} hours. Find the speeds of the train and the bus.",
             f"Let train $u$, bus $v$ km/h; $p=\\frac{{1}}{{u}}$, $q=\\frac{{1}}{{v}}$: ${a}p+{D-a}q={t(h1)}$, ${b}p+{D-b}q={t(h2)}$ (2); $p=\\frac{{1}}{{{u}}}$, $q=\\frac{{1}}{{{v}}}$ (2); train {u} km/h, bus {v} km/h (1).", "2+2+1")
def KTRI(a1, b1, c1, a2, b2, c2):
    x0, y0 = sol_cost(a1, b1, c1, a2, b2, c2)
    ar = abs(F(c1, b1) - F(c2, b2)) * abs(x0) / 2
    return Q(f"Draw the graphs of ${E(a1,b1,c1)}$ and ${E(a2,b2,c2)}$. Find the area of the triangle formed by these lines and the $y$-axis.",
             f"Intersection $({t(x0)},{t(y0)})$ (2); $y$-intercepts $\\left(0,{t(F(c1,b1))}\\right)$ and $\\left(0,{t(F(c2,b2))}\\right)$ (1); base $={t(abs(F(c1,b1)-F(c2,b2)))}$, height $={t(abs(x0))}$ (1); area $=\\frac12\\times$ base $\\times$ height $={t(ar)}$ sq. units (1).", "2+1+1+1")
def RED(x0, y0, a, b, d, e):
    c = a * F(1, x0) + b * F(1, y0); f = d * F(1, x0) + e * F(1, y0)
    return Q(f"Solve: $\\dfrac{{{a}}}{{x}}+\\dfrac{{{b}}}{{y}}={t(c)}$ and $\\dfrac{{{d}}}{{x}}+\\dfrac{{{e}}}{{y}}={t(f)}$.",
             f"Put $p=\\frac{{1}}{{x}}$, $q=\\frac{{1}}{{y}}$: ${a}p+{b}q={t(c)}$, ${d}p+{e}q={t(f)}$ (1); eliminating $q$: $({a*e-b*d})p={t(c*e-b*f)}$ so $p=\\frac{{1}}{{{x0}}}$ (1); $q=\\frac{{1}}{{{y0}}}$ (1); $x={x0}$, $y={y0}$ (1).", "1+1+1+1")

def og(n):
    n = int(n)
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n % 10, 'th')}"
