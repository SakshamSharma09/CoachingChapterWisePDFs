"""Shared helpers for Class 8 Maths graded chapters 2-7 (authoring agent's own module)."""
from fractions import Fraction as F
from decimal import Decimal
from math import gcd
from common import M4, Q, grp

def fr(f):
    f = F(f); s = "-" if f < 0 else ""; f = abs(f)
    return s + (str(f.numerator) if f.denominator == 1 else rf"\frac{{{f.numerator}}}{{{f.denominator}}}")

def tx(f): return "$" + fr(f) + "$"
def pw(a, n): return f"{a}^{{{n}}}"
def sci(s):
    d = Decimal(str(s)); e = d.adjusted(); m = d.scaleb(-e).normalize()
    return format(m, "f"), e
def usual(m, k): return format(Decimal(str(m)).scaleb(k), "f")
def scitx(s):
    m, e = sci(s); return rf"${m}\times10^{{{e}}}$"
def lcm(a, b): return a * b // gcd(a, b)
def fmt(x):
    """Plain number string (int or exact decimal) from Fraction/int/Decimal."""
    if isinstance(x, F):
        if x.denominator == 1: return str(x.numerator)
        return format(Decimal(x.numerator) / Decimal(x.denominator), "f")
    return str(x)

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))

def lin(p, q, v="x"):
    s = f"{p}{v}" if p != 1 else v
    return s + (f"{q:+d}" if q else "")
def dg(v): return f"{v}^{{\circ}}"
def Dg(v): return f"${v}^{{\circ}}$"
