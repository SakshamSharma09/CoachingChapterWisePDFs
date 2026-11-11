"""Class 8 Maths Ch 6 - We Distribute, Yet Things Multiply. Graded banks; algebra computed with small polynomial helpers."""
from c8m_h import *

SLUG, NAME, CHNO = "Distributive_Property", "We Distribute, Yet Things Multiply", 6

def sp(items):
    """items: list of (coef, suffix) -> tex polynomial string."""
    s = ""
    for c, suf in items:
        if c == 0: continue
        a = abs(c); body = (str(a) if (a != 1 or not suf) else "") + suf
        s += (("-" if c < 0 else ("+" if s else "")) + body)
    return s or "0"
def P2(c2, c1, c0, v="x"): return sp([(c2, f"{v}^{{2}}"), (c1, v), (c0, "")])
def PL(c1, c0, v="x"): return sp([(c1, v), (c0, "")])
def T_(s): return f"${s}$"
def mul(p, q, r, s): return (p * r, p * s + q * r, q * s)     # (px+q)(rx+s)
def wr(c, extra=None):
    c2, c1, c0 = c
    cand = [(c2, 0, c0), (c2, -c1, c0), (c2, c1, -c0), (c2, c1 + (2 if c1 >= 0 else -2), c0), (c2 + 1, c1, c0), (c2, c1, c0 + 1)]
    out = []
    for t in cand:
        if t != c and t not in out: out.append(t)
    return [T_(P2(*t)) for t in out[:3]]
def n3(v, d=(1, -1, 2)): return [v + x for x in d]
def ev(c, k): return c[0] * k * k + c[1] * k + c[2]
def sqn(n): return n * n
def split100(n):
    b = round(n, -1) if n > 20 else n
    return b, n - b

# ================= EASY =================
eA1 = [M4(f"The value of ${a}\\times{b}$ is:", a * b, [a * b + b, a * b - b, a * b + 10], f"${a}\\times{b}=(100{'+' if a>100 else '-'}{abs(a-100)})\\times{b}$") for a, b in [(99, 13), (101, 24), (98, 15), (102, 18), (97, 20), (103, 12)]]
eA2 = [M4(f"The value of ${a}\\times({b}+{c})$ is:", a * (b + c), [a * b + c, a * b * c, a * (b + c) + a], f"${a}\\times{b}+{a}\\times{c}$") for a, b, c in [(7, 10, 3), (6, 50, 4), (8, 20, 5), (9, 30, 2), (5, 40, 7)]]
eA3 = [M4(f"Expanding ${p}(x+{q})$ gives:", T_(PL(p, p * q)), [T_(PL(p, q)), T_(PL(1, p * q)), T_(PL(p, p + q))], "Multiply each term inside by the outside number") for p, q in [(3, 4), (5, 2), (4, 6), (2, 9), (6, 3)]]
eA4 = [M4("$(a+b)^2$ equals:", "$a^2+2ab+b^2$", ["$a^2+b^2$", "$a^2+ab+b^2$", "$2a+2b$"], "Standard identity"),
       M4("$(a-b)^2$ equals:", "$a^2-2ab+b^2$", ["$a^2-b^2$", "$a^2+2ab+b^2$", "$a^2-ab+b^2$"], "Standard identity"),
       M4("$(a+b)(a-b)$ equals:", "$a^2-b^2$", ["$a^2+b^2$", "$a^2-2ab+b^2$", "$(a-b)^2$"], "Standard identity")]
eA5 = [M4(f"The value of ${n}^2$ is:", n * n, [n * n + n, n * n - n, n * n + 10], f"${n}^2={n}\\times{n}$") for n in [21, 32, 41, 53, 61, 29]]
eA6 = [M4(f"The value of ${PL(p,q)}$ when $x={k}$ is:", p * k + q, [p * k - q, p + q + k, p * k + q + p], f"${p}\\times{k}+{q}$") for p, q, k in [(3, 5, 4), (2, 7, 6), (5, 1, 3), (4, 9, 5), (6, 2, 7), (8, 3, 2)]]
eA7 = [M4(f"The coefficient of $x$ in ${P2(p,q,r)}$ is:", q, [p, r, p + q], "The number multiplying $x$") for p, q, r in [(3, 7, 2), (5, 4, 9), (2, 8, 1), (6, 3, 5)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([Q(f"Find ${a}\\times{b}$ using the distributive property.", f"${a}\\times{b}=({100}{'+' if a>100 else '-'}{abs(a-100)})\\times{b}$ (1) $={100*b}{'+' if a>100 else '-'}{abs(a-100)*b}={a*b}$ (1).", "1+1") for a, b in [(99, 16), (102, 25), (98, 22), (104, 15)]]
          + [Q(f"Expand ${p}(x+{q})$.", f"${p}\\times x+{p}\\times{q}$ (1) $={PL(p,p*q)}$ (1).", "1+1") for p, q in [(7, 3), (4, 8), (9, 5), (6, 7)]]
          + [Q(f"Find ${n}^2$ using $(a+b)^2$.", f"${n}={n//10*10}+{n%10}$ (1); ${n//10*10}^2+2\\times{n//10*10}\\times{n%10}+{n%10}^2={n*n}$ (1).", "1+1") for n in [34, 52, 63, 47]])
EASY_C = ([Q(f"Expand and simplify ${p}(x+{q})+{r}(x+{s})$.", f"${p}x+{p*q}+{r}x+{r*s}$ (1); collect like terms $={PL(p+r,p*q+r*s)}$ (2).", "1+2") for p, q, r, s in [(2, 3, 4, 5), (3, 2, 5, 1), (4, 1, 2, 6), (5, 4, 3, 2), (6, 2, 7, 7), (2, 8, 3, 3)]]
          + [Q(f"Expand $(x+{p})(x+{q})$.", f"$x^2+{q}x+{p}x+{p*q}$ (2); $={P2(1,p+q,p*q)}$ (1).", "2+1") for p, q in [(2, 3), (4, 5), (8, 6), (3, 7), (2, 9), (5, 6)]]
          + [Q(f"Use the identity $(a+b)^2$ to find ${n}^2$.", f"${n}={n//10*10}+{n%10}$ (1); ${n//10*10}^2+2({n//10*10})({n%10})+{n%10}^2={(n//10*10)**2}+{2*(n//10*10)*(n%10)}+{(n%10)**2}$ (1); $={n*n}$ (1).", "1+1+1") for n in [24, 36, 43, 58, 62, 71]])
EASY_D = ([Q(f"Expand $(x+{p})(x+{q})$ and find its value when $x={k}$.", f"$x^2+{q}x+{p}x+{p*q}$ (2); $={P2(1,p+q,p*q)}$ (1); at $x={k}$: ${k*k}+{(p+q)*k}+{p*q}={ev((1,p+q,p*q),k)}$ (2).", "2+1+2") for p, q, k in [(2, 4, 3), (3, 5, 2), (8, 6, 4), (4, 7, 1), (2, 5, 5), (3, 6, 3)]]
          + [Q(f"Find ${a}\\times{b}$ using the distributive property and verify by direct multiplication.", f"${a}\\times{b}=({100 if a>100 else 100}{'+' if a>100 else '-'}{abs(a-100)})\\times{b}={100*b}{'+' if a>100 else '-'}{abs(a-100)*b}$ (2); $={a*b}$ (1); direct multiplication gives ${a*b}$ (2).", "2+1+2") for a, b in [(104, 25), (96, 35), (105, 18), (95, 24), (108, 15), (92, 30)]])

# ================= NCERT =================
nA1 = [M4(f"$(x+{p})^2$ equals:", T_(P2(1, 2 * p, p * p)), [T_(P2(1, 0, p * p)), T_(P2(1, p, p * p)), T_(P2(1, 2 * p, 0))], "$(a+b)^2=a^2+2ab+b^2$") for p in [3, 4, 5, 6, 7]]
nA2 = [M4(f"$(x-{p})^2$ equals:", T_(P2(1, -2 * p, p * p)), [T_(P2(1, 0, -p * p)), T_(P2(1, 2 * p, p * p)), T_(P2(1, -p, p * p))], "$(a-b)^2=a^2-2ab+b^2$") for p in [2, 5, 8, 9, 10]]
nA3 = [M4(f"$(x+{p})(x-{p})$ equals:", T_(P2(1, 0, -p * p)), [T_(P2(1, 0, p * p)), T_(P2(1, -2 * p, p * p)), T_(P2(1, 2 * p, -p * p))], "$(a+b)(a-b)=a^2-b^2$") for p in [3, 6, 7, 11]]
nA4 = [M4(f"$(x+{p})(x+{q})$ equals:", T_(P2(1, p + q, p * q)), [T_(P2(1, p * q, p + q)), T_(P2(1, p + q, p + q)), T_(P2(1, 0, p * q))], "$(x+a)(x+b)=x^2+(a+b)x+ab$") for p, q in [(2, 5), (3, 7), (4, 6), (1, 8), (5, 9)]]
nA5 = [M4(f"${100+d}\\times{100-d}$ equals:", 10000 - d * d, [10000 + d * d, 10000 - 2 * d, 10000 - d], f"$(100+{d})(100-{d})=100^2-{d}^2$") for d in [1, 2, 3, 4, 5]]
nA6 = [M4(f"In the expansion of $({lin(p,q)})({lin(r,s)})$ the coefficient of $x$ is:", p * s + q * r, [p * s, q * r, p * r + q * s], "Add the two cross products") for p, q, r, s in [(2, 3, 4, 5), (3, 1, 2, 6), (4, 2, 5, 3), (2, 7, 3, 2), (5, 4, 1, 8)]]
nA7 = [M4("Which of the following is true for all values of $a$ and $b$?", "$(a-b)^2=a^2-2ab+b^2$", ["$(a-b)^2=a^2-b^2$", "$(a+b)^2=a^2+b^2$", "$(a+b)(a-b)=a^2+b^2$"], "Check by expanding"),
       M4("$a^2-b^2$ equals:", "$(a+b)(a-b)$", ["$(a-b)^2$", "$(a+b)^2$", "$a(a-b)$"], "Difference of squares"),
       M4("The area of a square of side $(x+4)$ is:", "$x^2+8x+16$", ["$x^2+16$", "$4x+16$", "$x^2+4x+16$"], "$(x+4)^2$"),
       M4("The product of two numbers $(a+b)$ and $(a-b)$ is:", "the difference of the squares of $a$ and $b$", ["the sum of the squares of $a$ and $b$", "twice the product of $a$ and $b$", "the square of $a-b$"], "Standard identity")]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([Q(f"Expand $(x+{p})^2$ using an identity.", f"$x^2+2\\times x\\times{p}+{p}^2$ (1) $={P2(1,2*p,p*p)}$ (1).", "1+1") for p in [8, 9, 11, 12]]
           + [Q(f"Expand $({lin(p,q)})({lin(r,s)})$.", f"${p*r}x^2+{p*s}x+{q*r}x+{q*s}$ (1) $={P2(*mul(p,q,r,s))}$ (1).", "1+1") for p, q, r, s in [(2, 1, 3, 4), (3, 2, 1, 5), (4, 3, 2, 1), (5, 2, 3, 2)]]
           + [Q(f"Find ${a}\\times{b}$ using $(a+b)(a-b)$.", f"${a}\\times{b}=({(a+b)//2}-{(b-a)//2})({(a+b)//2}+{(b-a)//2})$ (1) $={((a+b)//2)**2}-{((b-a)//2)**2}={a*b}$ (1).", "1+1") for a, b in [(48, 52), (97, 103), (45, 55), (86, 94)]])
NCERT_C = ([Q(f"Expand $({lin(p,q)})^2$.", f"$({p}x)^2+2({p}x)({q})+{q}^2$ (2); $={P2(p*p,2*p*q,q*q)}$ (1).", "2+1") for p, q in [(2, 3), (3, 4), (5, 1), (4, 5), (2, 7), (3, 2)]]
           + [Q(f"Find ${a}\\times{b}$ using the identity $(a+b)(a-b)=a^2-b^2$.", f"${a}={(a+b)//2}{'+' if a>b else '-'}{abs(a-b)//2}$, ${b}={(a+b)//2}{'-' if a>b else '+'}{abs(a-b)//2}$ (1); product $={((a+b)//2)**2}-{(abs(a-b)//2)**2}$ (1); $={a*b}$ (1).", "1+1+1") for a, b in [(53, 47), (68, 72), (91, 109), (35, 45), (74, 86), (118, 122)]]
           + [Q(f"Simplify $(x+{p})(x+{q})+(x-{p})(x-{q})$.", f"$(x+{p})(x+{q})={P2(1,p+q,p*q)}$ (1); $(x-{p})(x-{q})={P2(1,-(p+q),p*q)}$ (1); sum $={P2(2,0,2*p*q)}$ (1).", "1+1+1") for p, q in [(2, 3), (4, 5), (1, 7), (3, 6), (2, 8), (5, 4)]])
NCERT_D = ([Q(f"A rectangle has length $(x+{p})$ cm and breadth $(x+{q})$ cm. Write an expression for its area and find the area when $x={k}$.", f"Area $=(x+{p})(x+{q})$ (1); $={P2(1,p+q,p*q)}$ (2); at $x={k}$: ${ev((1,p+q,p*q),k)}$ cm$^2$ (2).", "1+2+2") for p, q, k in [(3, 5, 4), (2, 6, 5), (4, 7, 3), (1, 9, 6), (5, 8, 2), (3, 4, 10)]]
           + [Q(f"Prove that $(a+b)^2-(a-b)^2=4ab$ and verify it for $a={a}$, $b={b}$.", f"$(a+b)^2=a^2+2ab+b^2$, $(a-b)^2=a^2-2ab+b^2$ (2); difference $=4ab$ (1); for $a={a}$, $b={b}$: ${(a+b)**2}-{(a-b)**2}={(a+b)**2-(a-b)**2}$ and $4ab={4*a*b}$ (2).", "2+1+2") for a, b in [(7, 3), (9, 4), (8, 5), (6, 2), (10, 3), (12, 5)]])

# ================= MEDIUM =================
mA1 = [M4(f"$({lin(p,q)})({lin(r,s)})$ equals:", T_(P2(*mul(p, q, r, s))), wr(mul(p, q, r, s)), "Multiply term by term and collect like terms") for p, q, r, s in [(3, 2, 2, 5), (4, 1, 3, 2), (2, 5, 3, 1), (5, 3, 2, 4), (3, 4, 4, 3)]]
mA2 = [M4(f"$({p}x-{q}y)^2$ equals:", f"${p*p}x^{{2}}-{2*p*q}xy+{q*q}y^{{2}}$", [f"${p*p}x^{{2}}-{q*q}y^{{2}}$", f"${p*p}x^{{2}}+{2*p*q}xy+{q*q}y^{{2}}$", f"${p*p}x^{{2}}-{p*q}xy+{q*q}y^{{2}}$"], "$(a-b)^2=a^2-2ab+b^2$") for p, q in [(2, 3), (3, 1), (4, 5), (5, 2), (3, 4)]]
mA3 = [M4(f"The value of ${a}^2-{b}^2$ is:", a * a - b * b, [(a - b) ** 2, a * a + b * b, (a + b) ** 2], f"$({a}+{b})({a}-{b})={a+b}\\times{a-b}$") for a, b in [(63, 37), (78, 22), (91, 9), (55, 45), (84, 16)]]
mA4 = [M4(f"The value of $(x+{p})^2$ when $x={k}$ is:", (k + p) ** 2, [k * k + p * p, (k + p) ** 2 + 2 * p, k * k + p * k + p * p], f"$({k}+{p})^2$") for p, k in [(3, 7), (4, 6), (5, 8), (2, 9), (6, 5)]]
mA5 = [M4(f"The value of $(x+{p})(x+{q})$ when $x={k}$ is:", (k + p) * (k + q), [k * k + p * q, (k + p) * (k + q) + k, k * k + (p + q) * k], f"$({k}+{p})({k}+{q})$") for p, q, k in [(2, 5, 4), (3, 4, 6), (1, 6, 5), (4, 7, 2)]]
mA6 = [M4(f"$(x+{p})^2-(x-{p})^2$ equals:", T_(PL(4 * p, 0)), [T_(P2(2, 0, 2 * p * p)), T_(PL(2 * p, 0)), T_(PL(4 * p, p * p))], "The $x^2$ and constant terms cancel") for p in [2, 3, 5, 7]]
mA7 = [M4(f"Simplifying ${p}(x+{q})-{r}(x-{s})$ gives:", T_(PL(p - r, p * q + r * s)), [T_(PL(p - r, p * q - r * s)), T_(PL(p + r, p * q + r * s)), T_(PL(p - r, p + q + r + s))], "Expand each bracket and collect like terms") for p, q, r, s in [(5, 2, 3, 4), (6, 1, 2, 5), (7, 3, 4, 2), (4, 6, 1, 3), (8, 2, 5, 7)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([Q(f"Expand $({p}x+{q}y)^2$.", f"$({p}x)^2+2({p}x)({q}y)+({q}y)^2$ (1) $={p*p}x^2+{2*p*q}xy+{q*q}y^2$ (1).", "1+1") for p, q in [(2, 5), (3, 2), (4, 3), (5, 4)]]
         + [Q(f"Find ${a}\\times{b}$ using $(a+b)(a-b)$.", f"${a}\\times{b}=({(a+b)//2})^2-({(b-a)//2})^2$ (1) $={((a+b)//2)**2}-{((b-a)//2)**2}={a*b}$ (1).", "1+1") for a, b in [(39, 41), (57, 63), (24, 36), (82, 98)]]
         + [Q(f"Simplify ${p}(x+{q})-{r}(x-{s})$.", f"${p}x+{p*q}-{r}x+{r*s}$ (1) $={PL(p-r,p*q+r*s)}$ (1).", "1+1") for p, q, r, s in [(9, 3, 4, 2), (7, 5, 2, 6), (8, 1, 3, 4), (6, 4, 1, 5)]])
MED_C = ([Q(f"Expand $({lin(p,q)})({lin(r,-s)})$.", f"${p*r}x^2-{p*s}x+{q*r}x-{q*s}$ (2); $={P2(*mul(p,q,r,-s))}$ (1).", "2+1") for p, q, r, s in [(3, 2, 2, 5), (4, 1, 3, 2), (2, 5, 5, 1), (5, 3, 2, 4), (3, 4, 4, 3), (6, 1, 2, 3)]]
         + [Q(f"Find ${n}^2$ using an algebraic identity.", f"${n}={round(n,-1)}{'+' if n>round(n,-1) else '-'}{abs(n-round(n,-1))}$ (1); $({round(n,-1)}{'+' if n>round(n,-1) else '-'}{abs(n-round(n,-1))})^2={round(n,-1)**2}{'+' if n>round(n,-1) else '-'}{2*round(n,-1)*abs(n-round(n,-1))}+{(n-round(n,-1))**2}$ (1); $={n*n}$ (1).", "1+1+1") for n in [197, 108, 299, 52, 98, 203]]
         + [Q(f"Verify that $(a+b)^2+(a-b)^2=2(a^2+b^2)$ for $a={a}$ and $b={b}$.", f"LHS $={(a+b)**2}+{(a-b)**2}={(a+b)**2+(a-b)**2}$ (1.5); RHS $=2({a*a}+{b*b})={2*(a*a+b*b)}$ (1.5).", "1½+1½") for a, b in [(5, 2), (7, 4), (9, 3), (6, 5), (8, 1), (10, 7)]])
def md1(p, q, r):
    c = (p * p - r * r, 2 * p * q, q * q)
    return Q(f"A square plot has side $({lin(p,q)})$ m. A square pond of side ${r}x$ m is dug inside it. Write the area of the remaining land as an expression in $x$ and find it when $x=10$.", f"Plot $=({lin(p,q)})^2={P2(p*p,2*p*q,q*q)}$ (2); pond $={P2(r*r,0,0)}$ (1); remaining $={P2(*c)}$ (1); at $x=10$: ${ev(c,10)}$ m$^2$ (1).", "2+1+1+1")
def md2(a, b, c, d, e, f):
    return Q(f"Use identities to evaluate: (i) ${a}^2$ (ii) ${b}\\times{c}$ (iii) ${d}^2-{e}^2$.", f"(i) ${a}^2={a*a}$ (1.5); (ii) ${b}\\times{c}={b*c}$ (1.5); (iii) $({d}+{e})({d}-{e})={d+e}\\times{d-e}={d*d-e*e}$ (2).", "1½+1½+2")
MED_D = [md1(*r) for r in [(3, 2, 2), (4, 5, 2), (5, 3, 3), (2, 7, 3), (6, 1, 4), (5, 4, 2)]] + [md2(*r) for r in [(103, 88, 92, 76, 24, 0), (97, 59, 61, 83, 17, 0), (205, 47, 53, 65, 35, 0), (302, 74, 66, 91, 19, 0), (99, 38, 42, 57, 43, 0), (1004, 95, 105, 72, 28, 0)]]

# ================= HARD =================
hA1 = [M4(f"If $x+y={s}$ and $xy={p}$, then $x^2+y^2$ equals:", s * s - 2 * p, [s * s + 2 * p, s * s - p, s * s], "$x^2+y^2=(x+y)^2-2xy$") for s, p in [(9, 14), (11, 28), (13, 36), (10, 21), (15, 54)]]
hA2 = [M4(f"If $x-y={d}$ and $xy={p}$, then $x^2+y^2$ equals:", d * d + 2 * p, [d * d - 2 * p, d * d + p, d * d], "$x^2+y^2=(x-y)^2+2xy$") for d, p in [(3, 20), (4, 45), (5, 24), (2, 35), (7, 60)]]
hA3 = [M4(f"The value of ${a}^2-{b}^2$ is:", a * a - b * b, [(a - b) ** 2, a * a + b * b, a * a - b * b + 100], f"$({a}+{b})({a}-{b})$") for a, b in [(512, 488), (754, 246), (635, 365), (903, 97), (848, 152)]]
hA4 = [M4(f"If $x+\\dfrac{{1}}{{x}}={k}$, then $x^2+\\dfrac{{1}}{{x^2}}$ equals:", k * k - 2, [k * k + 2, k * k, k * k - 1], "Square both sides") for k in [3, 4, 5, 6]]
hA5 = [M4(f"If $(x+p)(x+q)=x^2+{a}x+{b}$, then $p^2+q^2$ equals:", a * a - 2 * b, [a * a + 2 * b, a * a - b, a * a], "$p+q=a$, $pq=b$") for a, b in [(7, 12), (9, 20), (11, 28), (10, 24), (13, 36)]]
hA6 = [M4(f"The area of a square of side {n} cm exceeds that of a square of side {n-k} cm by:", n * n - (n - k) ** 2, [k * k, n * k, (n - k) ** 2], f"${n}^2-{n-k}^2$") for n, k in [(25, 3), (40, 7), (36, 4), (52, 8)]]
hA7 = [M4(f"The value of ${n}^2-{n-1}^2$ is:", 2 * n - 1, [2 * n + 1, 2 * n, n], "$n^2-(n-1)^2=2n-1$") for n in [24, 35, 48, 61]]
hA8 = [M4("$(a+b)^2=a^2+b^2$ is true only when:", "$ab=0$", ["$a=b$", "$a+b=0$", "$a=1$"], "Compare with $a^2+2ab+b^2$"),
       M4("For all real numbers $a$ and $b$, $(a-b)^2+2ab$ equals:", "$a^2+b^2$", ["$(a+b)^2$", "$a^2-b^2$", "$2a^2$"], "Expand"),
       M4("If $a^2-b^2=0$ then:", "$a=b$ or $a=-b$", ["$a=b$ only", "$a=0$ only", "$a+b=1$"], "$(a+b)(a-b)=0$"),
       M4("$(x+y)^2-(x-y)^2$ equals:", "$4xy$", ["$2xy$", "$2x^2+2y^2$", "$0$"], "Cross terms double")]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([Q(f"If $x+y={s}$ and $xy={p}$, find $x^2+y^2$.", f"$x^2+y^2=(x+y)^2-2xy$ (1) $={s*s}-{2*p}={s*s-2*p}$ (1).", "1+1") for s, p in [(12, 35), (8, 15), (14, 33), (17, 60)]]
          + [Q(f"Evaluate ${a}^2-{b}^2$ using an identity.", f"$({a}+{b})({a}-{b})={a+b}\\times{a-b}$ (1) $={a*a-b*b}$ (1).", "1+1") for a, b in [(612, 388), (845, 155), (703, 297), (960, 40)]]
          + [Q(f"If $(x+p)(x+q)=x^2+{a}x+{b}$, find $p^2+q^2$.", f"$p+q={a}$, $pq={b}$ (1); $p^2+q^2={a}^2-2({b})={a*a-2*b}$ (1).", "1+1") for a, b in [(8, 15), (12, 32), (15, 54), (9, 14)]])
HARD_C = ([Q(f"If $x-y={d}$ and $xy={p}$, find $x^2+y^2$ and $(x+y)^2$.", f"$x^2+y^2=(x-y)^2+2xy={d*d}+{2*p}={d*d+2*p}$ (1.5); $(x+y)^2=(x-y)^2+4xy={d*d}+{4*p}={d*d+4*p}$ (1.5).", "1½+1½") for d, p in [(4, 21), (6, 40), (3, 28), (5, 36), (7, 30), (8, 48)]]
          + [Q(f"Simplify $({lin(p,q)})^2-({lin(p,-q)})^2$.", f"$({p}x+{q})^2={P2(p*p,2*p*q,q*q)}$ (1); $({p}x-{q})^2={P2(p*p,-2*p*q,q*q)}$ (1); difference $={PL(4*p*q,0)}$ (1).", "1+1+1") for p, q in [(3, 2), (4, 5), (5, 3), (2, 7), (6, 1), (3, 8)]]
          + [Q(f"If $a+b={s}$ and $ab={p}$, find $a^2+b^2$ and $(a-b)^2$.", f"$a^2+b^2=({s})^2-2({p})={s*s-2*p}$ (1.5); $(a-b)^2=a^2+b^2-2ab={s*s-2*p}-{2*p}={s*s-4*p}$ (1.5).", "1½+1½") for s, p in [(10, 24), (13, 40), (9, 18), (15, 56), (11, 30), (14, 45)]])
def hd1(p, q, k):
    c = (p * p, 0, -q * q)
    return Q(f"The sides of a rectangle are $({lin(p,q)})$ m and $({lin(p,-q)})$ m. Find its area as an expression, its value at $x={k}$, and by how much it is less than the area of a square of side ${p}x$ m.", f"Area $=({lin(p,q)})({lin(p,-q)})={P2(*c)}$ (2); at $x={k}$: ${ev(c,k)}$ m$^2$ (1); square $={P2(p*p,0,0)}$, difference $={q*q}$ m$^2$ (2).", "2+1+2")
def hd2(x, y):
    s, t = x + y, x * x + y * y
    return Q(f"If $x+y={s}$ and $x^2+y^2={t}$, find $xy$, $(x-y)^2$ and $x-y$ (take $x>y$).", f"$xy=\\dfrac{{({s})^2-{t}}}{{2}}={x*y}$ (2); $(x-y)^2={t}-2({x*y})={(x-y)**2}$ (2); $x-y={x-y}$ (1).", "2+2+1")
HARD_D = [hd1(*r) for r in [(3, 2, 5), (4, 3, 6), (5, 4, 2), (2, 7, 8), (6, 5, 3), (7, 2, 4)]] + [hd2(*r) for r in [(9, 4), (11, 5), (8, 3), (12, 7), (10, 6), (13, 2)]]

TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}

from c8m_fix import tidy
tidy(TIERS)
