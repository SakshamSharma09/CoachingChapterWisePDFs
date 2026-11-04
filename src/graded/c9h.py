"""Shared helpers for Class 9 Maths (Ganita Manjari) graded chapter modules c9m_chNN."""
from g67 import *  # noqa: F401,F403  (M4, Q, QQ, nm, tm, T, T4, fmt, fx, gcd, isqrt, Fr, Dc ...)
from math import gcd, isqrt, pi

TRI = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15), (20, 21, 29), (12, 16, 20), (15, 20, 25), (10, 24, 26),
       (9, 40, 41), (12, 35, 37), (18, 24, 30), (16, 30, 34), (21, 28, 35), (24, 32, 40), (11, 60, 61), (14, 48, 50), (27, 36, 45), (30, 40, 50)]

def P(x, y): return f"({fmt(x)}, {fmt(y)})"
def TP(x, y): return f"${P(x, y)}$"
def sur(n):
    """TeX for sqrt(n) simplified."""
    if n == 0: return "0"
    a, m = 1, n
    for k in range(isqrt(n), 1, -1):
        if n % (k * k) == 0: a, m = k, n // (k * k); break
    if m == 1: return str(a)
    return (str(a) if a > 1 else "") + rf"\sqrt{{{m}}}"
def sgn(v): return f"+{v}" if v >= 0 else f"-{-v}"
def lin(a, b, v="x"):
    """TeX of a*v + b."""
    s = (v if a == 1 else "-" + v if a == -1 else f"{a}{v}") if a else ""
    if b == 0: return s or "0"
    return (s + (f"+{b}" if b > 0 else f"-{-b}")) if s else str(b)
def half(n):
    """n/2 as exact string."""
    return str(n // 2) if n % 2 == 0 else f"{n // 2}.5" if n >= 0 else f"-{(-n) // 2}.5"
def optpts(x, y, k=6):
    c = [(y, x), (-x, y), (x, -y), (-x, -y), (x + 1, y), (x, y + 1), (x + 2, y - 1)]
    out = []
    for p in c:
        s = TP(*p)
        if s != TP(x, y) and s not in out: out.append(s)
    return out[:k]
def mpt(q, x, y, why=""): return M4(q, TP(x, y), optpts(x, y), why)
def rt(n):
    r = isqrt(n); assert r * r == n, n; return r

def expand(fr):
    """Decimal expansion of a non-negative Fraction -> (int_part, nonrepeating_digits, repeating_digits)."""
    fr = Fr(fr); ip, r = divmod(fr.numerator, fr.denominator); d = fr.denominator
    seen, digs = {}, []
    while r and r not in seen:
        seen[r] = len(digs); r *= 10; digs.append(str(r // d)); r %= d
    if not r: return ip, "".join(digs), ""
    k = seen[r]; return ip, "".join(digs[:k]), "".join(digs[k:])
def dtex(fr):
    ip, nr, rp = expand(fr)
    return f"{ip}." + (nr or ("" if rp else "0")) + (rf"\overline{{{rp}}}" if rp else "") if (nr or rp) else f"{ip}"
def rep_frac(ip, nr, rp):
    """Fraction value of ip.nr(rp repeating)."""
    n, k = len(nr), len(rp)
    return Fr(ip) + Fr(int(nr or "0"), 10 ** n) + (Fr(int(rp), 10 ** n * (10 ** k - 1)) if rp else 0)
def rtex(ip, nr, rp): return f"{ip}." + nr + rf"\overline{{{rp}}}"
def period(q):
    q2 = q
    for p in (2, 5):
        while q2 % p == 0: q2 //= p
    if q2 == 1: return 0
    k, v = 1, 10 % q2
    while v != 1: v = v * 10 % q2; k += 1
    return k
def term_ok(fr):
    q = Fr(fr).denominator
    for p in (2, 5):
        while q % p == 0: q //= p
    return q == 1
def fopts(fr):
    fr = Fr(fr); n, d = fr.numerator, fr.denominator
    out = []
    for c in (Fr(n + 1, d), Fr(n, d + 1), Fr(n - 1, d), Fr(n, d + 2), Fr(n + 2, d + 1), Fr(d, n) if n else Fr(1, d)):
        s = f"${fx(c)}$"
        if c != fr and s not in out: out.append(s)
    return out
def fq(q, fr, why=""): return M4(q, f"${fx(fr)}$", fopts(fr), why)

def ptex(terms):
    """terms: list of (coef, monomial TeX); zero coefficients skipped; returns TeX polynomial."""
    s = ""
    for c, m in terms:
        if c == 0: continue
        a = abs(c); body = (str(a) if (a != 1 or not m) else "") + m
        s += (("-" if c < 0 else "") + body) if not s else (" - " if c < 0 else " + ") + body
    return s or "0"
def polyopts(variants):
    """variants: list of term-lists, first is correct. Returns (correct_tex, wrong_tex_list)."""
    texs = []
    for v in variants:
        t = f"${ptex(v)}$"
        if t not in texs: texs.append(t)
    return texs[0], texs[1:]
def pm(q, variants, why=""):
    c, w = polyopts(variants); return M4(q, c, w, why)

def DG(n): return f"${n}^\\circ$"
def dgq(q, c, why="", offs=(10, -10, 20, -20, 30, 5, 15, 45)):
    out = []
    for o in offs:
        x = c + o
        if x != c and 0 < x < 360 and x not in out: out.append(x)
    return M4(q, DG(c), [DG(x) for x in out[:6]], why)
