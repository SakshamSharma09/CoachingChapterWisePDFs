import os; os.environ.setdefault('CHROMIUM_PATH', os.path.expanduser('~/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe'))
import sys; sys.path.insert(0, 'D:/Coaching Chapterwise PDFs/src/pat/c6m')
from lib8 import *
import figs6 as G
from fractions import Fraction as Fr
from math import gcd
def lcm(a, b): return a * b // gcd(a, b)
def fr(x):
    """Fraction -> html (mixed number if >1)."""
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    w, r = divmod(x.numerator, x.denominator)
    f = frac(r, x.denominator)
    return (f"{w} " if w else "") + f
def imp(x): x = Fr(x); return str(x.numerator) if x.denominator == 1 else frac(x.numerator, x.denominator)
def tri(n): return n * (n + 1) // 2
def opts3(c, cands):
    out = []
    for x in cands:
        if x != c and x not in out: out.append(x)
    return out[:3]
def mm(q, c, cands, sol='', fig=None):
    return m(q, str(c), [str(x) for x in opts3(c, cands)], sol, fig)
def collatz(n):
    s = [n]
    while n != 1: n = n // 2 if n % 2 == 0 else 3 * n + 1; s.append(n)
    return s
def kap(n):
    d = f"{n:04d}"; a = int("".join(sorted(d, reverse=True))); b = int("".join(sorted(d))); return a, b, a - b
def primes(a, b): return [n for n in range(a, b + 1) if n > 1 and all(n % k for k in range(2, int(n ** .5) + 1))]
def pf(n):
    out = []; k = 2
    while n > 1:
        while n % k == 0: out.append(k); n //= k
        k += 1
    return out
def pfs(n):
    f = pf(n); from collections import Counter
    c = Counter(f); return " × ".join(f"{p}<sup>{e}</sup>" if e > 1 else str(p) for p, e in sorted(c.items()))
def hcf_l(a, b): return gcd(a, b), lcm(a, b)
def kap_chain(n):
    out = []
    while n != 6174:
        a, b, r = kap(n); out.append((a, b, r)); n = r
        if len(out) > 10: break
    return out
