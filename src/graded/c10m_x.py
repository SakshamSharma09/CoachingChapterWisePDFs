"""Helpers for Class 10 Maths graded banks, chapters 9-14 (exact arithmetic with Fractions)."""
from fractions import Fraction as F
from math import gcd, isqrt
from decimal import Decimal, ROUND_HALF_UP
from mg import t, Q, M4, grp, T, pp
import lib

# ---- exact numbers a + b*sqrt(3) as tuples of Fractions ----
def S(a=0, b=0): return (F(a), F(b))
def sadd(x, y): return (x[0] + y[0], x[1] + y[1])
def ssub(x, y): return (x[0] - y[0], x[1] - y[1])
def smul(x, y): return (x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def sinv(x):
    n = x[0] ** 2 - 3 * x[1] ** 2
    assert n != 0
    return (x[0] / n, -x[1] / n)
def sdiv(x, y): return smul(x, sinv(y))
def sfrac(c, v):
    c = F(c)
    n = "" if c.numerator == 1 else str(c.numerator)
    if c.denominator == 1: return f"{n}{v}"
    return f"\\frac{{{n}{v}}}{{{c.denominator}}}"
def stex(x):
    a, b = x
    if b == 0: return t(a)
    bp = "\\sqrt3" if abs(b) == 1 else sfrac(abs(b), "\\sqrt3")
    bp = ("-" if b < 0 else "") + bp
    if a == 0: return bp
    if a < 0 and b > 0: return bp + "-" + t(-a)
    return t(a) + ("" if b < 0 else "+") + bp
def snice(x): return x[0].denominator == 1 and x[1].denominator == 1
TAN = {30: S(0, F(1, 3)), 45: S(1), 60: S(0, 1)}
COT = {30: S(0, 1), 45: S(1), 60: S(0, F(1, 3))}
SIN = {30: S(F(1, 2)), 60: S(0, F(1, 2))}
COS = {30: S(0, F(1, 2)), 60: S(F(1, 2))}

# ---- decimals / money-like formatting ----
def dec(x, places=2):
    """exact terminating decimal string (<= places), else None"""
    x = F(x); d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d != 1: return None
    s = format(Decimal(x.numerator) / Decimal(x.denominator), "f")
    if "." in s: s = s.rstrip("0").rstrip(".")
    if "." in s and len(s.split(".")[1]) > places: return None
    return s
def nd(x):
    """plain number text; asserts that x is a clean (terminating) decimal"""
    s = dec(x)
    assert s is not None, x
    return s
def rnd2(x):
    x = F(x)
    return str((Decimal(x.numerator) / Decimal(x.denominator)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def pad_wrong(c, cands, fmt):
    out = []
    for x in cands:
        s = fmt(x)
        if s != fmt(c) and s not in out: out.append(s)
    return out

def steps(parts, total):
    """parts: exactly 3 step strings -> (marking text, split string) for a question of `total` marks (2, 3 or 5)"""
    assert len(parts) == 3, parts
    if total == 2: parts, split = [parts[0] + "; " + parts[1], parts[2]], [1, 1]
    elif total == 3: split = [1, 1, 1]
    elif total == 5: split = [2, 2, 1]
    else: raise ValueError(total)
    return "; ".join(f"{p} ({m})" for p, m in zip(parts, split)) + ".", "+".join(map(str, split))

def QS(stem, parts, total):
    txt, sp = steps(parts, total)
    return Q(stem, txt, sp)

# ---- generic scenario machinery (numeric chapters) ----
def SCG(stem0, ask, ans, wrongs, parts, fmt):
    ans = ans if isinstance(ans, list) else [ans]
    return dict(stem0=stem0, ask=ask, ans=ans, wrongs=list(wrongs), parts=parts, fmt=fmt)
def MC(sc, tail=None):
    assert len(sc["ans"]) == 1, sc["stem0"]
    f = sc["fmt"]; c = sc["ans"][0]
    ws = []
    for w in sc["wrongs"]:
        try: fw = f(w)
        except AssertionError: continue      # distractor that is not a clean decimal is skipped
        if fw != f(c) and fw not in ws: ws.append(fw)
    if tail is None: tail = f"The {sc['ask']} is:"
    return M4(f"{sc['stem0']} {tail}", f(c), ws, sc["parts"][1] + "; " + sc["parts"][2])
def SQ(sc, total):
    return QS(f"{sc['stem0']} Find the {sc['ask']}.", sc["parts"], total)
def pyth(a, b, c):
    assert a * a + b * b == c * c
    return a, b, c
def triples(cmax):
    out = []
    for c in range(5, cmax + 1):
        for a in range(3, c):
            b2 = c * c - a * a; b = isqrt(b2)
            if b * b == b2 and a < b: out.append((a, b, c))
    return out
def nums_near(c, ex=()):
    c = F(c); out = []
    for x in list(ex) + [c + 1, c - 1, c + 2, c - 2, c * 2, c + 3, c + 5, c - 3]:
        x = F(x)
        if x != c and x > 0 and x not in out: out.append(x)
    return out
