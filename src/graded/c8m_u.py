"""Shared helpers for Class 8 Maths graded banks (ch 8-14)."""
from fractions import Fraction as Fr
from math import gcd, isqrt, sqrt
from common import M4, Q, grp

def g(x):
    r = round(float(x), 2)
    return f"{int(r)}" if r == int(r) else f"{r:.2f}".rstrip("0").rstrip(".")
def rs(x): return "₹ " + g(x)
def pc(x): return g(x) + "%"
def fr(n, d): return r"\frac{%d}{%d}" % (n, d)
def frs(f):
    f = Fr(f)
    return str(f.numerator) if f.denominator == 1 else fr(f.numerator, f.denominator)
def lcm(a, b): return a * b // gcd(a, b)

def wrongs(v, n=3):
    """plausible numeric distractors for value v (unformatted floats)"""
    v = float(v); isint = abs(v - round(v)) < 1e-9
    step = max(1, abs(v) * 0.1)
    c = [v + step, v - step, v * 2, v / 2, v * 1.25, v * 0.75, v + 2 * step, v - 2 * step, v + 10, v + 5, v - 5, v + 1]
    out = []
    for x in c:
        if isint: x = round(x)
        x = round(x, 2)
        if x < 0 and v >= 0: continue
        if abs(x - v) < 1e-9 or x in out: continue
        out.append(x)
    return out

def ND(q, v, why="", wrong=None, fmt=g, pre="", post=""):
    """numeric MCQ: correct value v (+ optional list of intended wrong values)"""
    cs = pre + fmt(v) + post
    ws = []
    for x in (list(wrong or []) + wrongs(v, 8)):
        s = pre + fmt(x) + post
        if s != cs and s not in ws: ws.append(s)
    return M4(q, cs, ws[:3], why)

def split_marks(*m): return "+".join(str(x) for x in m)
