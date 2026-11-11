"""Class 9 Maths Ch 4 - Algebraic Identities (square and cube identities, products, factorisation, numerical use)."""
from c9h import *

SLUG, NAME, CHNO = "Algebraic_Identities", "Algebraic Identities", 4

def sqt(p, q, two=False, s=1):
    """terms of (p x + s q y)^2 (y optional)."""
    return [(p * p, "x^2"), (2 * s * p * q, "xy" if two else "x"), (q * q, "y^2" if two else "")]
def sq_opts(p, q, two=False, s=1):
    return [sqt(p, q, two, s), [(p * p, "x^2"), (s * p * q, "xy" if two else "x"), (q * q, "y^2" if two else "")],
            [(p * p, "x^2"), (-2 * s * p * q, "xy" if two else "x"), (q * q, "y^2" if two else "")], [(p * p, "x^2"), (0, ""), (q * q, "y^2" if two else "")],
            [(p * p, "x^2"), (2 * s * p * q, "xy" if two else "x"), (-q * q, "y^2" if two else "")]]
def lf(p, q, two=False, s=1):
    """TeX of p x + s q (y or 1)."""
    return ptex([(p, "x"), (s * q, "y" if two else "")])
def prod_terms(p, a, q, b): return [(p * q, "x^2"), (p * b + q * a, "x"), (a * b, "")]
def prod_opts(p, a, q, b):
    return [prod_terms(p, a, q, b), [(p * q, "x^2"), (p * b + q * a + 1, "x"), (a * b, "")], [(p * q, "x^2"), (p * b - q * a, "x"), (a * b, "")], [(p * q, "x^2"), (p * b + q * a, "x"), (-a * b, "")], [(p * q, "x^2"), (a + b, "x"), (a * b, "")]]
def cube_terms(p, q, s=1): return [(p ** 3, "x^3"), (3 * s * p * p * q, "x^2"), (3 * p * q * q, "x"), (s * q ** 3, "")]
def cube_opts(p, q, s=1):
    return [cube_terms(p, q, s), [(p ** 3, "x^3"), (3 * s * p * q, "x^2"), (3 * p * q, "x"), (s * q ** 3, "")], [(p ** 3, "x^3"), (3 * s * p * p * q, "x^2"), (3 * p * q * q, "x"), (-s * q ** 3, "")], [(p ** 3, "x^3"), (0, ""), (0, ""), (s * q ** 3, "")]]
def fac(s_, p_):
    """roots a,b of t^2 - ... : returns pair with a+b=s_, ab=p_ via search."""
    for a in range(-60, 61):
        b = s_ - a
        if a * b == p_ and a <= b: return a, b
    raise ValueError((s_, p_))
def cx(p, v='x'): return ('' if p == 1 else str(p)) + v
def lin1(a): return ptex([(1, "x"), (a, "")])

# ------------------------------------------------------------------ EASY
eA1 = [pm(f"$({lf(1, a)})^2=$", sq_opts(1, a), "$(a+b)^2=a^2+2ab+b^2$") for a in [2, 3, 5, 6, 7]]
eA2 = [pm(f"$({lf(1, a, s=-1)})^2=$", sq_opts(1, a, s=-1), "$(a-b)^2=a^2-2ab+b^2$") for a in [4, 5, 8, 9]]
eA3 = [pm(f"$(x+{a})(x-{a})=$", [[(1, "x^2"), (-a * a, "")], [(1, "x^2"), (a * a, "")], [(1, "x^2"), (-2 * a, "x"), (a * a, "")], [(1, "x^2"), (2 * a, "x"), (-a * a, "")]], "$(a+b)(a-b)=a^2-b^2$") for a in [3, 4, 6, 10]]
eA4 = [nm(f"Using $(a+b)^2$, the value of ${n}^2$ is:", n * n, f"${n}=({n - n % 10}+{n % 10})$, apply $(a+b)^2$") for n in [31, 41, 52, 61, 73]]
eA5 = [nm(f"Using $a^2-b^2$, the value of ${50 - k}\\times{50 + k}$ is:", 2500 - k * k, f"$(50-{k})(50+{k})=2500-{k * k}$") for k in [1, 2, 3, 4]]
eA6 = [M4(f"$x^2-{a * a}$ factorises as:", f"$(x+{a})(x-{a})$", [f"$(x-{a})^2$", f"$(x+{a})^2$", f"$(x+{a * a})(x-1)$"], "$a^2-b^2=(a+b)(a-b)$") for a in [5, 7, 9, 11]]
eA7 = [nm(f"If $a={a}$ and $b={b}$, then $(a+b)^2=$", (a + b) ** 2, "Add first, then square.") for a, b in [(2, 5), (3, 7), (4, 9), (6, 8)]]
eA8 = [pm(f"$(x+{a})(x+{b})=$", prod_opts(1, a, 1, b), "$(x+a)(x+b)=x^2+(a+b)x+ab$") for a, b in [(2, 3), (4, 5), (3, 7), (6, 2)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Expand $({lf(1, a)})^2$.", "Use $(a+b)^2=a^2+2ab+b^2$", f"$={ptex(sqt(1, a))}$") for a in [8, 10, 12, 4]]
          + [QQ(f"Expand $(x+{a})(x-{a})$.", "Use $(a+b)(a-b)=a^2-b^2$", f"$=x^2-{a * a}$") for a in [8, 12, 15, 2]]
          + [QQ(f"Find ${n}^2$ using $(a+b)^2$.", f"${n}=({n - n % 10}+{n % 10})$", f"${n}^2={(n // 10 * 10) ** 2}+{2 * (n // 10 * 10) * (n % 10)}+{(n % 10) ** 2}={n * n}$") for n in [42, 53, 64, 82]])
EASY_C = ([QQ(f"Expand $({lf(p, q)})^2$.", "Use $(a+b)^2=a^2+2ab+b^2$", f"$a={cx(p)}$, $b={q}$", f"$={ptex(sqt(p, q))}$") for p, q in [(2, 3), (3, 1), (4, 5), (5, 2), (2, 7), (3, 4)]]
          + [QQ(f"Factorise ${ptex([(1, 'x^2'), (2 * a, 'x'), (a * a, '')])}$.", "Compare with $a^2+2ab+b^2$", f"$a=x$, $b={a}$", f"$=(x+{a})^2$") for a in [3, 4, 5, 6, 7, 9]]
          + [QQ(f"Evaluate ${50 + k}\\times{50 - k}$ using an identity.", f"$=(50+{k})(50-{k})$", f"$=50^2-{k}^2=2500-{k * k}$", f"$={2500 - k * k}$") for k in [5, 6, 7, 8, 9, 10]])
EASY_D = ([QQ(f"Expand $({lf(p, q, True)})^2$ and find its value when $x=1$ and $y=1$.", "Use $(a+b)^2=a^2+2ab+b^2$", f"$({cx(p)})^2={cx(p * p, 'x^2')}$, $2({cx(p)})({cx(q, 'y')})={cx(2 * p * q, 'xy')}$", f"$={ptex(sqt(p, q, True))}$", f"At $x=y=1$: ${p * p + 2 * p * q + q * q}$")
           for p, q in [(2, 1), (3, 2), (1, 4), (2, 5), (4, 3), (3, 3)]]
          + [QQ(f"Factorise ${ptex([(1, 'x^2'), (S, 'x'), (Pp, '')])}$.", f"Find two numbers with sum ${S}$ and product ${Pp}$", f"The numbers are ${fac(S, Pp)[0]}$ and ${fac(S, Pp)[1]}$", f"$=(x{sgn(fac(S, Pp)[0])})(x{sgn(fac(S, Pp)[1])})$", "Check by expanding")
             for S, Pp in [(5, 6), (7, 12), (9, 20), (8, 15), (11, 30), (10, 21)]])

# ------------------------------------------------------------------ NCERT
nA1 = [pm(f"$({lf(p, q, True)})^2=$", sq_opts(p, q, True), "$(a+b)^2=a^2+2ab+b^2$") for p, q in [(2, 3), (3, 4), (5, 2), (4, 1)]]
nA2 = [pm(f"$({lf(p, q, True, -1)})^2=$", sq_opts(p, q, True, -1), "$(a-b)^2=a^2-2ab+b^2$") for p, q in [(3, 2), (2, 5), (4, 3), (5, 1)]]
nA3 = [pm(f"$(x+{a})(x-{b})=$", [[(1, "x^2"), (a - b, "x"), (-a * b, "")], [(1, "x^2"), (a + b, "x"), (-a * b, "")], [(1, "x^2"), (b - a, "x"), (-a * b, "")], [(1, "x^2"), (a - b, "x"), (a * b, "")]], "$(x+a)(x+b)=x^2+(a+b)x+ab$") for a, b in [(7, 3), (8, 5), (9, 2), (6, 4)]]
nA4 = [nm(f"By identity, ${n}^2=$", n * n, f"Write ${n}=100{'+' if n > 100 else '-'}{abs(n - 100)}$") for n in [103, 98, 102, 97]]
nA5 = [M4(f"$x^2+{2 * a}x+{a * a}$ is the square of:", f"$(x+{a})$", [f"$(x-{a})$", f"$(x+{2 * a})$", f"$(x+{a * a})$"], "$a^2+2ab+b^2=(a+b)^2$") for a in [4, 6, 8, 10]]
nA6 = [M4(f"Factorise ${ptex([(1, 'x^2'), (S, 'x'), (Pp, '')])}$:", f"$(x{sgn(fac(S, Pp)[0])})(x{sgn(fac(S, Pp)[1])})$", [f"$(x{sgn(fac(S, Pp)[0] + 1)})(x{sgn(fac(S, Pp)[1] - 1)})$", f"$(x{sgn(-fac(S, Pp)[0])})(x{sgn(-fac(S, Pp)[1])})$", f"$(x{sgn(fac(S, Pp)[0] + 2)})(x{sgn(fac(S, Pp)[1])})$"], "Find two numbers with the given sum and product.") for S, Pp in [(7, 10), (-9, 14), (2, -15), (-1, -12), (13, 36)]]
nA7 = [nm(f"If $x+y={S}$ and $xy={Pp}$, then $x^2+y^2=$", S * S - 2 * Pp, "$x^2+y^2=(x+y)^2-2xy$.") for S, Pp in [(9, 14), (10, 21), (7, 12), (8, 15)]]
nA8 = [M4(f"$(a+b)^3$ equals:", "$a^3+3a^2b+3ab^2+b^3$", ["$a^3+b^3$", "$a^3+3ab+b^3$", "$a^3+3a^2b-3ab^2+b^3$"], "Standard cube identity.")]
nA8 += [M4("$a^3+b^3$ factorises as:", "$(a+b)(a^2-ab+b^2)$", ["$(a+b)(a^2+ab+b^2)$", "$(a-b)(a^2+ab+b^2)$", "$(a+b)^3$"], "Sum of cubes identity."),
        M4("$a^3-b^3$ factorises as:", "$(a-b)(a^2+ab+b^2)$", ["$(a-b)(a^2-ab+b^2)$", "$(a+b)(a^2-ab+b^2)$", "$(a-b)^3$"], "Difference of cubes identity."),
        M4("$(a-b)^3$ equals:", "$a^3-3a^2b+3ab^2-b^3$", ["$a^3-b^3$", "$a^3-3a^2b-3ab^2-b^3$", "$a^3+3a^2b+3ab^2-b^3$"], "Standard cube identity.")]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([QQ(f"Expand $({lf(p, q, True, s)})^2$.", "Use the square identity", f"$={ptex(sqt(p, q, True, s))}$") for p, q, s in [(3, 5, 1), (2, 7, -1), (6, 1, 1), (4, 3, -1)]]
           + [QQ(f"Find ${n}^2$ using an identity.", f"${n}=100{'+' if n > 100 else '-'}{abs(n - 100)}$", f"${n}^2={n * n}$") for n in [104, 96, 105, 99]]
           + [QQ(f"Expand $(x+{a})(x+{b})$.", "Use $(x+a)(x+b)=x^2+(a+b)x+ab$", f"$={ptex(prod_terms(1, a, 1, b))}$") for a, b in [(5, 8), (-4, 9), (7, -2), (-6, -5)]])
NCERT_C = ([QQ(f"Expand $({lf(p, q, True, s)})^2$ and verify for $x=1$, $y=1$.", "Use the square identity", f"$={ptex(sqt(p, q, True, s))}$", f"LHS $=({p}{s * q:+d})^2={(p + s * q) ** 2}$, RHS $={p * p + 2 * s * p * q + q * q}$") for p, q, s in [(2, 3, 1), (3, 4, -1), (5, 2, 1), (4, 5, -1), (3, 1, 1), (6, 5, -1)]]
           + [QQ(f"Factorise ${ptex([(1, 'x^2'), (S, 'x'), (Pp, '')])}$.", f"Need two numbers with sum ${S}$ and product ${Pp}$", f"They are ${fac(S, Pp)[0]}$ and ${fac(S, Pp)[1]}$", f"$=(x{sgn(fac(S, Pp)[0])})(x{sgn(fac(S, Pp)[1])})$") for S, Pp in [(8, 12), (-7, 10), (3, -10), (-2, -24), (-10, 21), (4, -21)]]
           + [QQ(f"Evaluate ${a}\\times{b}$ using $(x+a)(x+b)$.", f"${a}\\times{b}=(100{sgn(a - 100)})(100{sgn(b - 100)})$", f"$=100^2+({a + b - 200})(100)+({(a - 100) * (b - 100)})$", f"$={a * b}$") for a, b in [(103, 107), (97, 95), (104, 98), (106, 102), (96, 108), (95, 105)]])
NCERT_D = ([QQ(f"Expand $({p}x-{q}y)^2$ and find its value when $x={u}$ and $y={v}$.", "Use $(a-b)^2=a^2-2ab+b^2$", f"$a={p}x$, $b={q}y$", f"Squares: ${p * p}x^2+{q * q}y^2$", f"Cross term: $-{2 * p * q}xy$", f"$={ptex([(p * p, 'x^2'), (-2 * p * q, 'xy'), (q * q, 'y^2')])}$; at $x={u}$, $y={v}$ the value is ${(p * u - q * v) ** 2}$") for p, q, u, v in [(2, 3, 3, 1), (3, 1, 2, 4), (4, 5, 2, 1), (5, 2, 1, 3), (3, 4, 4, 2), (2, 5, 5, 1)]]
           + [QQ(f"Expand $({lf(p, q)})^3$.", "Use $(a+b)^3=a^3+3a^2b+3ab^2+b^3$", f"$a={cx(p)}$, $b={q}$", f"$3a^2b={3 * p * p * q}x^2$, $3ab^2={3 * p * q * q}x$", f"$={ptex(cube_terms(p, q))}$", "Terms checked") for p, q in [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (1, 4)]])

# ------------------------------------------------------------------ MEDIUM
mA1 = [pm(f"$({lf(p, q, True, s)})^2=$", sq_opts(p, q, True, s), "Use the square identity.") for p, q, s in [(7, 4, 1), (6, 5, -1), (9, 2, 1), (8, 3, -1), (11, 2, 1)]]
mA2 = [pm(f"$({lf(p, a)})({lf(q, b)})=$", prod_opts(p, a, q, b), "Multiply term by term.") for p, a, q, b in [(2, 3, 3, 5), (3, 2, 2, 7), (2, -3, 5, 4), (4, 1, 3, -2)]]
mA3 = [nm(f"If $a-b={d}$ and $ab={Pp}$, then $a^2+b^2=$", d * d + 2 * Pp, "$a^2+b^2=(a-b)^2+2ab$.") for d, Pp in [(3, 18), (5, 24), (2, 35), (7, 30)]]
mA4 = [nm(f"If $x+\\frac1x={k}$, then $x^2+\\frac{{1}}{{x^2}}=$", k * k - 2, "Square both sides.") for k in [3, 4, 5, 7]]
mA5 = [nm(f"The value of ${n}^2$ is:", n * n, f"Write ${n}=1000{sgn(n - 1000)[0]}{abs(n - 1000)}$") for n in [1003, 997, 1005, 995]]
mA6 = [nm(f"The value of ${n}^2-{m}^2$ is:", n * n - m * m, "Use $a^2-b^2=(a+b)(a-b)$.") for n, m in [(78, 22), (93, 57), (126, 74), (205, 195)]]
mA7 = [M4(f"Factorise ${ptex([(1, 'x^2'), (S, 'x'), (Pp, '')])}$:", f"$(x{sgn(fac(S, Pp)[0])})(x{sgn(fac(S, Pp)[1])})$", [f"$(x{sgn(-fac(S, Pp)[0])})(x{sgn(-fac(S, Pp)[1])})$", f"$(x{sgn(fac(S, Pp)[0])})(x{sgn(-fac(S, Pp)[1])})$", f"$(x{sgn(fac(S, Pp)[0] + 1)})(x{sgn(fac(S, Pp)[1] + 1)})$"], "Find the pair of numbers.") for S, Pp in [(-3, -28), (1, -42), (-14, 48), (-5, -36)]]
mA8 = [nm(f"If $x+y={S}$ and $x-y={d}$, then $xy=$", (S * S - d * d) // 4, "$4xy=(x+y)^2-(x-y)^2$.") for S, d in [(12, 4), (14, 6), (20, 8), (18, 2)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Expand $({lf(p, a)})({lf(q, b)})$.", "Multiply term by term", f"$={ptex(prod_terms(p, a, q, b))}$") for p, a, q, b in [(2, 5, 3, 1), (3, 4, 2, -3), (4, -1, 2, 5), (5, 2, 3, -4)]]
         + [QQ(f"If $x+y={S}$ and $xy={Pp}$, find $x^2+y^2$.", "$x^2+y^2=(x+y)^2-2xy$", f"$={S * S}-{2 * Pp}={S * S - 2 * Pp}$") for S, Pp in [(11, 28), (13, 36), (15, 54), (9, 20)]]
         + [QQ(f"Find ${n}^2$ using an identity.", f"${n}=1000{sgn(n - 1000)}$", f"${n}^2={n * n}$") for n in [1002, 998, 1004, 996]])
MED_C = ([QQ(f"If $x+\\frac1x={k}$, find $x^2+\\frac{{1}}{{x^2}}$ and $\\left(x-\\frac1x\\right)^2$.", f"$x^2+\\frac1{{x^2}}=({k})^2-2={k * k - 2}$", f"$\\left(x-\\frac1x\\right)^2={k * k - 2}-2={k * k - 4}$") for k in [6, 8, 9, 10, 11, 12]]
         + [QQ(f"If $a-b={d}$ and $ab={Pp}$, find $a^2+b^2$ and $(a+b)^2$.", f"$a^2+b^2={d}^2+2({Pp})$", f"$={d * d + 2 * Pp}$", f"$(a+b)^2={d * d}+4({Pp})={d * d + 4 * Pp}$") for d, Pp in [(4, 21), (6, 40), (3, 28), (8, 33), (5, 36), (9, 52)]]
         + [QQ(f"Factorise ${ptex([(p * q, 'x^2'), (p * b + q * a, 'x'), (a * b, '')])}$.", f"Split the middle term: ${p * b + q * a}x={p * b}x+{q * a}x$", "Group the terms", f"$=({lf(p, a)})({lf(q, b)})$") for p, a, q, b in [(2, 3, 1, 4), (3, 1, 1, 5), (2, 1, 3, 2), (4, 3, 1, 2), (3, 2, 2, 5), (5, 1, 2, 3)]])
MED_D = ([QQ(f"If $x+y={S}$ and $x-y={D}$, find $x^2-y^2$, $xy$ and $x^2+y^2$.", "$x^2-y^2=(x+y)(x-y)$", f"$={S}\\times{D}={S * D}$", f"$4xy=(x+y)^2-(x-y)^2={S * S}-{D * D}$, so $xy={(S * S - D * D) // 4}$", f"$2(x^2+y^2)=(x+y)^2+(x-y)^2={S * S + D * D}$", f"$x^2+y^2={(S * S + D * D) // 2}$") for S, D in [(12, 4), (10, 6), (14, 8), (16, 4), (20, 6), (18, 10)]]
          + [QQ(f"If $a+b={S}$ and $ab={Q}$, find $a^2+b^2$ and $(a-b)^2$.", "$(a+b)^2=a^2+b^2+2ab$", f"${S * S}=a^2+b^2+{2 * Q}$", f"$a^2+b^2={S * S - 2 * Q}$", f"$(a-b)^2=(a+b)^2-4ab={S * S}-{4 * Q}={S * S - 4 * Q}$") for S, Q in [(9, 14), (12, 35), (10, 24), (15, 56), (11, 28), (13, 36)]])

# ------------------------------------------------------------------ HARD
hA1 = [nm(f"If $x+y={S}$ and $xy={Pp}$, then $x^3+y^3=$", S ** 3 - 3 * Pp * S, "$x^3+y^3=(x+y)^3-3xy(x+y)$.") for S, Pp in [(5, 6), (7, 10), (6, 8), (9, 20)]]
hA2 = [nm(f"If $x-y={d}$ and $xy={Pp}$, then $x^3-y^3=$", d ** 3 + 3 * Pp * d, "$x^3-y^3=(x-y)^3+3xy(x-y)$.") for d, Pp in [(2, 15), (3, 10), (1, 12), (4, 6)]]
hA3 = [nm(f"If $x+\\frac1x={k}$, then $x^3+\\frac{{1}}{{x^3}}=$", k ** 3 - 3 * k, "$x^3+\\frac1{x^3}=\\left(x+\\frac1x\\right)^3-3\\left(x+\\frac1x\\right)$.") for k in [3, 4, 5, 6]]
hA4 = [nm(f"The value of ${n}^3$ is:", n ** 3, f"${n}=100{sgn(n - 100)[0]}{abs(n - 100)}$; use $(a\\pm b)^3$.") for n in [101, 99, 102, 98]]
hA5 = [nm(f"If $x+y={S}$ and $x^2+y^2={T}$, then $xy=$", (S * S - T) // 2, "$2xy=(x+y)^2-(x^2+y^2)$.") for S, T in [(10, 58), (9, 53), (12, 90), (11, 65)]]
hA6 = [nm(f"If $x-y={S}$ and $x^2+y^2={T}$, then $xy=$", (T - S * S) // 2, "$2xy=(x^2+y^2)-(x-y)^2$.") for S, T in [(3, 65), (5, 73), (4, 40), (6, 90)]]
hA7 = [nm(f"If $x^2+\\frac1{{x^2}}={m}$, then $\\left(x+\\frac1x\\right)^2=$", m + 2, "Add $2$ to both sides.") for m in [14, 23, 34, 47]]
hA8 = [M4(t, c, w, "Use the factorisation identity.") for t, c, w in [
    ("$8x^3+27$ factorises as:", "$(2x+3)(4x^2-6x+9)$", ["$(2x+3)(4x^2+6x+9)$", "$(2x-3)(4x^2+6x+9)$", "$(2x+3)^3$"]),
    ("$27x^3-8$ factorises as:", "$(3x-2)(9x^2+6x+4)$", ["$(3x-2)(9x^2-6x+4)$", "$(3x+2)(9x^2-6x+4)$", "$(3x-2)^3$"]),
    ("$x^3-64$ factorises as:", "$(x-4)(x^2+4x+16)$", ["$(x-4)(x^2-4x+16)$", "$(x+4)(x^2-4x+16)$", "$(x-4)^3$"]),
    ("$125x^3+1$ factorises as:", "$(5x+1)(25x^2-5x+1)$", ["$(5x+1)(25x^2+5x+1)$", "$(5x-1)(25x^2+5x+1)$", "$(5x+1)^3$"])]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"If $x+y={S}$ and $xy={Pp}$, find $x^3+y^3$.", "$x^3+y^3=(x+y)^3-3xy(x+y)$", f"$={S ** 3}-{3 * Pp * S}={S ** 3 - 3 * Pp * S}$") for S, Pp in [(8, 12), (10, 16), (6, 5), (11, 24)]]
          + [QQ(f"Find the value of ${n}^3$ using an identity.", f"${n}=100{sgn(n - 100)}$", f"${n}^3={n ** 3}$") for n in [103, 97, 105, 95]]
          + [QQ(f"Factorise ${ptex([(k ** 3, 'x^3'), (m ** 3, '')])}$.", "Use $a^3+b^3=(a+b)(a^2-ab+b^2)$", f"$a={cx(k)}$, $b={m}$", f"$=({lf(k, m)})({ptex([(k * k, 'x^2'), (-k * m, 'x'), (m * m, '')])})$") for k, m in [(2, 1), (3, 2), (1, 5), (4, 3)]])
HARD_C = ([QQ(f"If $x+\\frac1x={k}$, find $x^3+\\frac1{{x^3}}$.", f"$\\left(x+\\frac1x\\right)^3=x^3+\\frac1{{x^3}}+3\\left(x+\\frac1x\\right)$", f"$x^3+\\frac1{{x^3}}={k}^3-3({k})$", f"$={k ** 3 - 3 * k}$") for k in [7, 8, 9, 10, 11, 12]]
          + [QQ(f"Factorise ${ptex([(1, 'x^2'), (-(a + b), 'x'), (a * b, '')])}$ and use it to find the value when $x={a + b + 1}$.", "Need two numbers with sum $" + str(-(a + b)) + "$ and product $" + str(a * b) + "$", f"They are ${-a}$ and ${-b}$", f"$=(x-{a})(x-{b})$" if a > 0 and b > 0 else f"$=(x{-a:+d})(x{-b:+d})$", f"At $x={a + b + 1}$: $({b + 1})({a + 1})={(a + 1) * (b + 1)}$") for a, b in [(1, 4), (2, 7), (3, 5), (2, 9), (6, 1), (4, 4)]]
          + [QQ(f"Factorise ${ptex([(k ** 3, 'x^3'), (-m ** 3, '')])}$.", "Use $a^3-b^3=(a-b)(a^2+ab+b^2)$", f"$a={cx(k)}$, $b={m}$", f"$=({lf(k, -m)})({ptex([(k * k, 'x^2'), (k * m, 'x'), (m * m, '')])})$") for k, m in [(2, 3), (3, 1), (1, 6), (5, 2), (4, 1), (2, 5)]])
HARD_D = ([QQ(f"If $x-y={d}$ and $xy={Pp}$, find $x^2+y^2$, $x^3-y^3$ and $(x+y)^2$.", f"$x^2+y^2={d * d}+{2 * Pp}={d * d + 2 * Pp}$", f"$x^3-y^3=(x-y)^3+3xy(x-y)={d ** 3}+{3 * Pp * d}$", f"$x^3-y^3={d ** 3 + 3 * Pp * d}$", f"$(x+y)^2=(x-y)^2+4xy={d * d}+{4 * Pp}$", f"$(x+y)^2={d * d + 4 * Pp}$") for d, Pp in [(3, 28), (2, 24), (5, 14), (4, 45), (6, 16), (1, 42)]]
          + [QQ(f"If $x+y={S}$ and $x^2+y^2={T}$, find $xy$, $(x-y)^2$ and $x^2-y^2$ given that $x>y$.", f"$2xy=(x+y)^2-(x^2+y^2)={S * S}-{T}={S * S - T}$", f"$xy={(S * S - T) // 2}$", f"$(x-y)^2=x^2+y^2-2xy={T}-{S * S - T}={2 * T - S * S}$", f"$x-y={isqrt(2 * T - S * S)}$", f"$x^2-y^2=(x+y)(x-y)={S * isqrt(2 * T - S * S)}$") for S, T in [(10, 58), (9, 45), (12, 80), (13, 89), (14, 100), (11, 61)] if isqrt(2 * T - S * S) ** 2 == 2 * T - S * S][:6])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
