"""Shared helpers for Class 6 / Class 7 Maths graded chapter modules (own helper; framework files untouched)."""
from fractions import Fraction as Fr
from decimal import Decimal as Dc
from math import gcd, isqrt
import re
from common import M4 as _M4, Q as _Q, grp

def _ord(m):
    n = int(m.group(1)); suf = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"
def fixord(s):
    return re.sub(r"(?<![\d.])(\d+)th", _ord, s) if isinstance(s, str) else s
def M4(q, c, w, why=""): return _M4(fixord(q), c, w, fixord(why))
def Q(q, ans, split="", fig=None): return _Q(fixord(q), fixord(ans), split, fig)
import lib
from lib import table  # noqa: F401

def refit(item, total):
    """Re-split a QQ item's marking steps so the marks add up to `total`."""
    st = item.get("steps")
    if not st: return item
    texts = [t for t, _ in st]; n = len(texts)
    if n > total:
        sizes = [n // total + (1 if i < n % total else 0) for i in range(total)]
        out = []; k = 0
        for sz in sizes: out.append("; ".join(texts[k:k + sz])); k += sz
        texts = out; marks = [1] * total
    else:
        marks = [1] * n; extra = total - n; idx = n - 1
        while extra > 0: marks[idx] += 1; extra -= 1; idx = (idx - 1) % n
    it = dict(item)
    it["ans"] = "; ".join(f"{t} ({m})" for t, m in zip(texts, marks)) + "."
    it["split"] = "+".join(map(str, marks))
    return it

def T(A, B, C, D):
    return dict(A=A, B=grp([refit(x, 2) for x in B], 4), C=grp([refit(x, 3) for x in C], 6), D=grp([refit(x, 5) for x in D], 6))

def QQ(q, *steps, fig=None):
    """Question with marking steps (each 'text' is worth 1 mark; marks are re-fitted to the section total by T)."""
    st = [(s, 1) if isinstance(s, str) else s for s in steps]
    it = Q(q, "; ".join(f"{t} ({m})" for t, m in st) + ".", "+".join(str(m) for _, m in st), fig)
    it["steps"] = st
    return it

def nm(q, c, why="", offs=(1, -1, 2, -2, 10, 3), pos=True):
    """Numeric MCQ; distractors are c+offset (offsets may be numbers or Decimals)."""
    out = []
    for o in offs:
        x = c + o
        if x != c and x not in out and not (pos and c >= 0 and x < 0): out.append(x)
    return M4(q, fmt(c), [fmt(x) for x in out], why)

def tm(q, c, wrongs, why=""):
    """Text MCQ: correct answer then list of wrong options."""
    return M4(q, c, wrongs, why)

def fmt(x):
    if isinstance(x, Dc):
        s = format(x.normalize(), "f")
        return s
    if isinstance(x, float):
        return format(Dc(repr(x)).normalize(), "f")
    return str(x)

def fx(f):
    f = Fr(f)
    return str(f.numerator) if f.denominator == 1 else (f"-\\frac{{{-f.numerator}}}{{{f.denominator}}}" if f < 0 else f"\\frac{{{f.numerator}}}{{{f.denominator}}}")

def mx(f):
    f = Fr(f)
    if f.denominator == 1: return str(f.numerator)
    w, r = divmod(f.numerator, f.denominator)
    return f"{w}\\frac{{{r}}}{{{f.denominator}}}" if w else fx(f)

def raw(n, d): return f"\\frac{{{n}}}{{{d}}}"

def dec(x):
    return fmt(Dc(str(x)))

def lcm(a, b): return a * b // gcd(a, b)

def fac(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def ftex(n):
    return r"\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(fac(n).items()))

def isprime(n): return n > 1 and all(n % p for p in range(2, isqrt(n) + 1))

def money(n): return f"₹{n}"

def swap_ok(lst):
    return lst

def T4(NC, EZ, MD, HD):
    return {"NCERT": T(*NC), "Easy": T(*EZ), "Medium": T(*MD), "Hard": T(*HD)}

def flat(*gs):
    out = []
    for g in gs: out += g
    return out

def tri(n): return n * (n + 1) // 2

def fib(n, a=1, b=1):
    out = [a, b]
    while len(out) < n: out.append(out[-1] + out[-2])
    return out[:n]

def ds(n): return sum(map(int, str(n)))

def ind(n):
    n = int(n); neg = n < 0; s = str(abs(n))
    if len(s) > 3:
        h, t = s[:-3], s[-3:]; parts = []
        while len(h) > 2: parts.insert(0, h[-2:]); h = h[:-2]
        if h: parts.insert(0, h)
        s = ",".join(parts + [t])
    return ("-" if neg else "") + s

def intl(n):
    return f"{int(n):,}"

def rnd(n, p): return (n + p // 2) // p * p
