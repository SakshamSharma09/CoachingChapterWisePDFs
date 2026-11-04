"""Helpers for Class 9 Maths graded chapter modules (own helper; framework files untouched)."""
from fractions import Fraction as Fr
from math import gcd, isqrt, pi
import g67
import re as _re
# g67.fixord contains a stray backspace char in its regex (never matches); patch it at runtime here (g67.py itself untouched).
g67.fixord = lambda s: _re.sub(r"(?<![\d.])(\d+)th\b", g67._ord, s) if isinstance(s, str) else s
from g67 import *  # M4, Q, QQ, T, T4, nm, tm, fx, lcm, flat, tri ...

def s(x):
    """LaTeX-friendly number: int/Fraction -> string."""
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    return ("-" if x < 0 else "") + f"\\frac{{{abs(x.numerator)}}}{{{x.denominator}}}"

def o(x): return f"${s(x)}$"

def nn(q, c, why="", offs=(1, -1, 2, -2, 5, -5, 10, 3, -3, 4), pos=False, fmtf=None):
    """Numeric MCQ with $..$ options; distractors c+offset."""
    f = fmtf or o
    out = []
    for d in offs:
        x = Fr(c) + d
        if x != Fr(c) and not (pos and x < 0) and f(x) not in out: out.append(f(x))
    return M4(q, f(c), out[:6], why)

def tx(q, c, wrongs, why=""): return M4(q, c, wrongs, why)

def lst(a, d, k=4, geo=False):
    xs = [a * d ** i if geo else a + i * d for i in range(k)]
    return ", ".join(s(x) for x in xs)

def mc_words(items, why="Recall the definition."):
    return [M4(q, c, w, why) for q, c, w in items]

import random as _random
def draw(seed, n, f, tries=20000):
    """Deterministically draw n distinct items from generator f(rng) (f returns None to reject)."""
    rng = _random.Random(seed); out = []; seen = set(); t = 0
    while len(out) < n and t < tries:
        t += 1
        r = f(rng)
        if r is None: continue
        key = (r["q"], tuple(r.get("opts") or ()))
        if key in seen: continue
        seen.add(key); out.append(r)
    assert len(out) == n, (seed, len(out), n)
    return out

def drawA(seed, f, groups=8, per=4):
    """Return `groups` groups of `per` MCQs; f is a list of generators (one per group) taking rng."""
    return [draw(seed + i, per, g) for i, g in enumerate(f)]
