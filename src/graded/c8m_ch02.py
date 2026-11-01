"""Class 8 Maths Ch 2 - Power Play. Graded banks (NCERT / Easy / Medium / Hard); everything computed in code."""
from decimal import Decimal as Dc
from c8m_h import *

SLUG, NAME, CHNO = "Power_Play", "Power Play", 2

def DD(x): return Dc(str(x))
def P(a, n): return f"${pw(a, n)}$"
def sciM4(q, d, why=""):
    m, e = sci(d)
    return M4(q, scitx(d), [rf"${m}\times10^{{{e+1}}}$", rf"${m}\times10^{{{e-1}}}$", rf"${dfm(DD(m)*10)}\times10^{{{e}}}$"], why)
def dfm(d): return format(DD(d).normalize(),'f')
def sg(q): return f"{q:+d}"
def lin(p, q): return f"{p}x{q:+d}" if q else f"{p}x"
def pv(a, n): return tx(F(a) ** n)
def cyc(a):
    u = a % 10; s = [u]
    while True:
        n = s[-1] * u % 10
        if n == s[0]: break
        s.append(n)
    return s
def X(m, e): return rf"${m}\times10^{{{e}}}$"

# ================= EASY =================
eA1 = [M4(rf"${pw(a,m)}\times{pw(a,n)}$ equals:", P(a, m + n), [P(a, m * n), P(a * a, m + n), P(a, abs(m - n) + 1)], f"Add the exponents: ${m}+{n}={m+n}$") for a, m, n in [(2, 3, 4), (3, 2, 5), (5, 3, 2), (7, 2, 4), (4, 3, 5), (6, 2, 3)]]
eA2 = [M4(rf"${pw(a,m)}\div{pw(a,n)}$ equals:", P(a, m - n), [P(a, m + n), P(a, m * n), P(a, m - n + 1)], f"Subtract the exponents: ${m}-{n}={m-n}$") for a, m, n in [(2, 9, 4), (3, 8, 3), (5, 7, 2), (7, 10, 6), (4, 9, 5), (6, 8, 2)]]
eA3 = [M4(rf"$({pw(a,m)})^{{{n}}}$ equals:", P(a, m * n), [P(a, m + n), P(a, m ** n), P(a, m * n + 1)], "Multiply the exponents") for a, m, n in [(2, 3, 2), (3, 2, 4), (5, 2, 3), (10, 4, 2), (4, 3, 3)]]
eA4 = [M4(rf"The value of ${pw(a,-n)}$ is:", tx(F(1, a ** n)), [tx(-a ** n), tx(F(1, a * n)), tx(a ** n)], rf"$a^{{-n}}=\frac1{{a^n}}=\frac1{{{a**n}}}$") for a, n in [(2, 4), (3, 3), (5, 3), (10, 2), (4, 3), (6, 2)]]
eA5 = [sciM4(f"{s} in scientific notation is:", s, "One non-zero digit before the decimal point") for s in ["3200", "58000", "470000", "0.0072", "0.00091", "906000"]]
eA6 = [M4(rf"${m}\times10^{{{k}}}$ in usual form is:", usual(m, k), [usual(m, k + 1), usual(m, k - 1), usual(m, -k)], "Move the decimal point right for a positive power and left for a negative power") for m, k in [(3.4, 3), (6.5, 5), (2.7, -2), (8.1, -4)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6]
EASY_B = ([Q(rf"Find the value of ${pw(a,m)}\times{pw(a,n)}$.", rf"Add exponents: ${pw(a,m+n)}$ (1); $={a**(m+n)}$ (1).", "1+1") for a, m, n in [(2, 2, 3), (3, 1, 3), (5, 2, 1), (10, 3, 2)]]
          + [Q(rf"Write ${pw(a,-n)}$ as a fraction.", rf"${pw(a,-n)}=\frac1{{{pw(a,n)}}}$ (1) $=\frac1{{{a**n}}}$ (1).", "1+1") for a, n in [(2, 6), (3, 4), (7, 2), (10, 4)]]
          + [Q(f"Express {s} in scientific notation.", rf"{scitx(s)} (2).", "2") for s in ["28000", "0.0053", "1450000", "0.00021"]])
EASY_C = ([Q(rf"Simplify ${pw(a,m)}\times{pw(a,n)}\div{pw(a,p)}$ and find its value.", rf"${pw(a,m)}\times{pw(a,n)}={pw(a,m+n)}$ (1); ${pw(a,m+n)}\div{pw(a,p)}={pw(a,m+n-p)}$ (1); value ${a**(m+n-p)}$ (1).", "1+1+1") for a, m, n, p in [(2, 5, 4, 6), (3, 4, 3, 5), (5, 3, 2, 4), (7, 2, 3, 3), (10, 4, 5, 6), (4, 2, 3, 2)]]
          + [Q(rf"Write ${m}\times10^{{{k}}}$ and ${n}\times10^{{{j}}}$ in usual form.", rf"${m}\times10^{{{k}}}={usual(m,k)}$ (1); ${n}\times10^{{{j}}}={usual(n,j)}$ (1); move the decimal point right for a positive power and left for a negative power (1).", "1+1+1") for m, k, n, j in [(4.2, 5, 3.5, -3), (7.1, 4, 6.2, -2), (2.9, 6, 8.4, -4), (5.3, 3, 9.7, -5), (1.6, 7, 4.8, -1), (3.8, 2, 2.5, -6)]]
          + [Q(f"Express {a} and {b} in scientific notation.", rf"{a} $={sci(a)[0]}\times10^{{{sci(a)[1]}}}$ (1); {b} $={sci(b)[0]}\times10^{{{sci(b)[1]}}}$ (1); one non-zero digit before the decimal point (1).", "1+1+1")
             for a, b in [("73000000", "0.0000064"), ("4200000", "0.0081"), ("560000", "0.000092"), ("9100000000", "0.00037"), ("38000", "0.00000025"), ("620000000", "0.0043")]])
EASY_D = ([Q(rf"Find the values of (i) ${pw(a,m)}$, (ii) ${pw(b,-n)}$, (iii) ${c}^0$ and (iv) the sum of the three values.",
             rf"(i) ${a**m}$ (1); (ii) $\frac1{{{b**n}}}$ (1); (iii) $1$ (1); (iv) sum $={a**m}+\frac1{{{b**n}}}+1={fr(a**m+1+F(1,b**n))}$ (2).", "1+1+1+2") for a, m, b, n, c in [(2, 5, 3, 2, 7), (3, 3, 2, 4, 9), (5, 2, 4, 2, 11), (4, 3, 5, 2, 6), (6, 2, 10, 3, 13), (7, 2, 2, 5, 8)]]
          + [Q(rf"Simplify $({pw(a,m)})^{{{n}}}\div{pw(a,p)}\times{pw(a,q)}$ and find its value.", rf"$({pw(a,m)})^{{{n}}}={pw(a,m*n)}$ (1); divide: ${pw(a,m*n-p)}$ (1); multiply: ${pw(a,m*n-p+q)}$ (2); value ${a**(m*n-p+q)}$ (1).", "1+1+2+1")
             for a, m, n, p, q in [(2, 2, 3, 4, 1), (3, 3, 2, 4, 2), (5, 2, 2, 3, 1), (2, 3, 3, 5, 2), (4, 2, 3, 4, 1), (10, 2, 3, 4, 2)]])

# ================= NCERT TYPE =================
nA1 = [M4(rf"The value of $\dfrac{{1}}{{{pw(a,-n)}}}$ is:", tx(a ** n), [tx(F(1, a ** n)), tx(-a ** n), tx(a * n)], rf"$\frac1{{a^{{-n}}}}=a^n={a**n}$") for a, n in [(2, 3), (3, 2), (5, 2), (10, 3), (4, 2)]]
nA2 = [M4(rf"The value of $(-{a})^{{{n}}}$ is:", tx((-a) ** n), [tx(-((-a) ** n)), tx(a * n), tx(abs((-a) ** n) + n)], "Even power gives a positive value; odd power gives a negative value") for a, n in [(3, 4), (2, 5), (5, 3), (4, 2), (7, 2), (2, 7)]]
nA3 = [sciM4(f"The standard form of {s} is:", s, "Place the decimal point after the first non-zero digit") for s in ["60000000", "384400", "0.0000052", "149600000", "0.00000012"]]
nA4 = [M4(rf"Which of the following equals ${m}\times10^{{{k}}}$?", usual(m, k), [usual(m, k + 1), usual(m, k - 1), usual(m, -k)], "Move the decimal point according to the sign of the exponent") for m, k in [(4.07, -3), (5.62, 4), (9.1, -5), (1.25, 6), (6.3, -1)]]
nA5 = [M4(rf"$\dfrac{{1}}{{{a**k}}}$ expressed as a power of ${a}$ is:", P(a, -k), [P(a, k), P(a, -(k + 1)), P(a, -(k - 1))], rf"$\frac1{{{a}^{{{k}}}}}={a}^{{-{k}}}$") for a, k in [(2, 6), (3, 4), (5, 3), (10, 5), (4, 3)]]
nA6 = ([M4(rf"In ${pw(a,n)}$, the base is:", str(a), [str(n), str(a * n), str(a ** n)], "The number being multiplied repeatedly is the base") for a, n in [(7, 4), (3, 5), (11, 2)]]
       + [M4(rf"In ${pw(a,n)}$, the exponent is:", str(n), [str(a), str(a * n), str(a ** n)], "The exponent tells how many times the base is used as a factor") for a, n in [(2, 9), (5, 6), (8, 3)]])
nA7 = [M4(f"How many zeros are there in one {nm} written in figures?", str(z), [str(z + 1), str(z - 1), str(z + 2)], f"One {nm} is $10^{{{z}}}$") for nm, z in [("lakh", 5), ("crore", 7), ("million", 6), ("billion", 9), ("thousand", 3)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([Q(rf"Express $({pw(a,m)})^{{{n}}}\times{pw(a,-p)}$ as a single power of ${a}$.", rf"$({pw(a,m)})^{{{n}}}={pw(a,m*n)}$ (1); ${pw(a,m*n)}\times{pw(a,-p)}={pw(a,m*n-p)}$ (1).", "1+1") for a, m, n, p in [(2, 3, 4, 5), (3, 2, 5, 4), (5, 2, 3, 2), (7, 3, 2, 4)]]
           + [Q(rf"Write $\left(\dfrac{{{a}}}{{{b}}}\right)^{{-{n}}}$ in simplest form.", rf"$\left(\dfrac{{{b}}}{{{a}}}\right)^{{{n}}}$ (1) $={fr(F(b,a)**n)}$ (1).", "1+1") for a, b, n in [(2, 3, 3), (5, 2, 2), (4, 3, 2), (3, 10, 2)]]
           + [Q(f"{c} Express it in standard form.", rf"{scitx(s)} (2).", "2") for c, s in [("The Earth is about 149600000 km from the Sun.", "149600000"), ("The mass of a dust particle is 0.000000753 kg.", "0.000000753"), ("India's population is about 1400000000.", "1400000000"), ("The diameter of a red blood cell is 0.0000075 m.", "0.0000075")]])
NCERT_C = ([Q(rf"Express each as a single power of ${a}$: (i) ${pw(a,m)}\times{pw(a,-n)}$ (ii) $({pw(a,p)})^{{-{q}}}$ (iii) ${pw(a,r)}\div{pw(a,-s)}$.", rf"(i) ${pw(a,m-n)}$ (1); (ii) ${pw(a,-p*q)}$ (1); (iii) ${pw(a,r+s)}$ (1).", "1+1+1") for a, m, n, p, q, r, s in [(2, 5, 2, 3, 2, 4, 3), (3, 4, 6, 2, 3, 5, 2), (5, 2, 4, 3, 1, 1, 3), (7, 3, 1, 2, 2, 2, 2), (10, 6, 9, 2, 4, 3, 5), (4, 3, 5, 1, 3, 2, 4)]]
           + [Q(rf"Find the value of $\left(\dfrac{{{a}}}{{{b}}}\right)^{{-{m}}}\times\left(\dfrac{{{a}}}{{{b}}}\right)^{{-{n}}}$.", rf"Add the exponents: $\left(\frac{{{a}}}{{{b}}}\right)^{{-{m+n}}}$ (1); $=\left(\frac{{{b}}}{{{a}}}\right)^{{{m+n}}}$ (1); value ${fr(F(b,a)**(m+n))}$ (1).", "1+1+1") for a, b, m, n in [(2, 3, 1, 1), (3, 2, 2, 1), (5, 4, 1, 2), (2, 5, 2, 1), (4, 1, 1, 1), (3, 5, 1, 1)]]
           + [Q(f"Express the following in standard form: (i) {a} (ii) {b} (iii) {c}.", rf"(i) {scitx(a)} (1); (ii) {scitx(b)} (1); (iii) {scitx(c)} (1).", "1+1+1") for a, b, c in [("5900000", "0.00074", "80000"), ("12300000", "0.0000058", "6500"), ("750000000", "0.0029", "41000"), ("3600000", "0.000041", "990000"), ("45000000", "0.00000078", "2300"), ("186000", "0.0000031", "72000000")]])
def nd1(a, p, q, r, s, t, u):
    return Q(rf"Find $x$ if (i) ${pw(a,'x')}\times{pw(a,p)}={pw(a,q)}$ (ii) $({pw(a,'x')})^{{{r}}}={pw(a,s)}$ (iii) ${pw(a,'x-'+str(t))}=\dfrac{{1}}{{{pw(a,u)}}}$.",
             rf"(i) $x+{p}={q}$, $x={q-p}$ (2); (ii) ${r}x={s}$, $x={s//r}$ (2); (iii) $x-{t}=-{u}$, $x={t-u}$ (1).", "2+2+1")
def nd2(p, j, q, k):
    n1, n2 = DD(p).scaleb(j), DD(q).scaleb(k); pr = (DD(p) * DD(q)).scaleb(j + k); qu = (DD(p) / DD(q)).scaleb(j - k)
    return Q(rf"Write {format(n1,'f')} and {format(n2,'f')} in standard form. Then find their product and quotient in standard form.",
             rf"{format(n1,'f')} $={X(*sci(n1))[1:-1]}$ (1); {format(n2,'f')} $={X(*sci(n2))[1:-1]}$ (1); product {scitx(pr)} (2); quotient {scitx(qu)} (1).", "1+1+2+1")
NCERT_D = ([nd1(*r) for r in [(2, 3, 11, 4, 20, 2, 3), (3, 2, 9, 5, 35, 4, 1), (5, 4, 10, 3, 18, 3, 2), (7, 1, 6, 2, 14, 5, 3), (2, 5, 13, 6, 18, 6, 4), (10, 2, 7, 4, 28, 2, 5)]]
           + [nd2(*r) for r in [(6, 5, 2, 3), (8, 7, 4, 2), (9, -3, 3, -5), (4.5, 6, 1.5, 2), (7.2, 4, 1.2, -2), (5, -4, 2, -6)]])

# ================= MEDIUM =================
mA1 = [M4(rf"$\dfrac{{{pw(a,m)}\times{pw(a,n)}}}{{{pw(a,p)}}}$ equals:", P(a, m + n - p), [P(a, m + n + p), P(a, m * n - p), P(a, m - n + p)], "Add the exponents on top, then subtract the bottom exponent") for a, m, n, p in [(3, 6, 4, 5), (5, 7, 3, 6), (2, 9, 5, 7), (7, 4, 8, 3), (11, 5, 2, 4)]]
mA2 = [M4(rf"The value of $\left(\dfrac{{{a}}}{{{b}}}\right)^{{-{n}}}$ is:", tx(F(b, a) ** n), [tx(F(a, b) ** n), tx(F(b, a) * n), tx(-(F(b, a) ** n))], r"$(a/b)^{-n}=(b/a)^n$") for a, b, n in [(2, 3, 2), (3, 5, 2), (4, 3, 3), (5, 2, 3), (2, 5, 2)]]
mA3 = [M4(rf"If ${pw(a,'x')}\times{pw(a,p)}={pw(a,q)}$, then $x$ is:", str(q - p), [str(q + p), str(q * p), str(q - p + 2)], f"$x+{p}={q}$") for a, p, q in [(3, 4, 11), (5, 2, 9), (2, 6, 15), (7, 3, 8), (10, 5, 12)]]
mA3b = [M4(rf"If $({pw(a,m)})^{{x}}={pw(a,N)}$, then $x$ is:", str(N // m), [str(N - m), str(N + m), str(N * m)], f"${m}x={N}$") for a, m, N in [(2, 3, 12), (5, 4, 20), (3, 5, 35), (7, 2, 18)]]
mA4 = [M4(rf"${pw(a,m)}\times{pw(b,m)}$ equals:", str((a * b) ** m), [str(a * b * m), str(a ** m + b ** m), str(a * b ** m)], rf"$a^m\times b^m=(ab)^m=({a*b})^{{{m}}}$") for a, b, m in [(2, 5, 3), (4, 25, 2), (5, 6, 2), (2, 15, 2), (25, 4, 3)]]
def prod(p, j, q, k): return (DD(p) * DD(q)).scaleb(j + k)
mA5 = [sciM4(rf"The product $({p}\times10^{{{j}}})\times({q}\times10^{{{k}}})$ in scientific notation is:", prod(p, j, q, k), "Multiply the numbers, add the exponents, then adjust") for p, j, q, k in [(2, 3, 3, 4), (1.5, 2, 4, 5), (2.5, 4, 2, 3), (6, -2, 1.5, 5), (3, -3, 2, -2)]]
def bigger(a, m, b, n): return (P(a, m), P(b, n)) if a ** m > b ** n else (P(b, n), P(a, m))
mA6 = [M4(rf"Which is greater: ${pw(a,m)}$ or ${pw(b,n)}$?", bigger(a, m, b, n)[0], [bigger(a, m, b, n)[1], "Both are equal", "Cannot be determined"], f"${a**m}$ and ${b**n}$") for a, m, b, n in [(2, 9, 9, 2), (3, 4, 4, 3), (5, 3, 3, 5), (2, 12, 12, 2)]]
mA7 = [M4(rf"${pw(a,-1)}+{pw(b,-1)}$ equals:", tx(F(1, a) + F(1, b)), [tx(F(1, a + b)), tx(F(1, a * b)), tx(F(2, a + b))], rf"$\frac1{{{a}}}+\frac1{{{b}}}$") for a, b in [(2, 3), (3, 4), (2, 5), (4, 5), (3, 7)]]
MED_A = [mA1, mA2, mA3, mA3b, mA4, mA5, mA6, mA7]
MED_B = ([Q(rf"Find the value of $({pw(a,m)})^{{{n}}}\div{pw(a,p)}$.", rf"$({pw(a,m)})^{{{n}}}={pw(a,m*n)}$, so ${pw(a,m*n)}\div{pw(a,p)}={pw(a,m*n-p)}$ (1) $={a**(m*n-p)}$ (1).", "1+1") for a, m, n, p in [(2, 3, 3, 5), (3, 2, 4, 5), (5, 2, 3, 4), (4, 3, 2, 4)]]
         + [Q(rf"Find $x$ if ${pw(a,'x')}=\dfrac{{1}}{{{a**k}}}$.", rf"$\frac1{{{a**k}}}={pw(a,-k)}$ (1); so $x=-{k}$ (1).", "1+1") for a, k in [(2, 5), (3, 3), (5, 2), (10, 4)]]
         + [Q(rf"Write $({p}\times10^{{{j}}})\div({q}\times10^{{{k}}})$ in scientific notation.", rf"${fmt(F(p)/F(q))}\times10^{{{j}-({k})}}$ (1) = {scitx((DD(p)/DD(q)).scaleb(j-k))} (1).", "1+1") for p, j, q, k in [(6, 8, 2, 3), (9, -2, 3, 2), (8, 6, 4, -2), (7.5, 5, 2.5, 1)]])
MED_C = ([Q(rf"Simplify $\dfrac{{{pw(a,m)}\times{pw(b,n)}}}{{{pw(a,p)}\times{pw(b,q)}}}$ and find its value.", rf"${pw(a,m-p)}\times{pw(b,n-q)}$ (1+1); value ${a**(m-p)}\times{b**(n-q)}={a**(m-p)*b**(n-q)}$ (1).", "1+1+1") for a, m, p, b, n, q in [(2, 5, 3, 3, 4, 2), (3, 7, 5, 2, 6, 3), (5, 4, 2, 3, 5, 3), (2, 8, 5, 7, 3, 1), (3, 6, 3, 4, 4, 2), (5, 5, 3, 2, 4, 1)]]
         + [Q(rf"Evaluate ${pw(a,-m)}+{pw(b,-n)}$ as a single fraction.", rf"$\frac1{{{a**m}}}+\frac1{{{b**n}}}$ (1); common denominator (1); sum ${fr(F(1,a**m)+F(1,b**n))}$ (1).", "1+1+1") for a, m, b, n in [(2, 3, 3, 2), (2, 4, 5, 2), (3, 2, 2, 5), (4, 2, 5, 2), (6, 2, 3, 3), (10, 2, 2, 4)]]
         + [Q(rf"A factory makes ${p}\times10^{{{j}}}$ bolts each day. How many bolts does it make in {d} days? Give the answer in scientific notation.", rf"Total $={p}\times10^{{{j}}}\times{d}$ (1) $={fmt(F(str(p))*d)}\times10^{{{j}}}$ (1); in scientific notation {scitx((DD(p)*d).scaleb(j))} (1).", "1+1+1") for p, j, d in [(2.5, 4, 12), (1.5, 3, 40), (4, 5, 30), (6.4, 2, 25), (7.5, 3, 16), (8, 4, 125)]])
def md1(a, m, b, n, p, q):
    return Q(rf"Simplify $\dfrac{{{pw(a,m)}\times{pw(b,-n)}}}{{{pw(a,-p)}\times{pw(b,q)}}}$ and write the answer with positive exponents. Then find its value.",
             rf"Numerator power of ${a}$: ${pw(a,m)}\div{pw(a,-p)}={pw(a,m+p)}$ (2); for ${b}$: ${pw(b,-n)}\div{pw(b,q)}={pw(b,-(n+q))}=\frac1{{{pw(b,n+q)}}}$ (1); result $\frac{{{pw(a,m+p)}}}{{{pw(b,n+q)}}}$ (1); value ${fr(F(a**(m+p), b**(n+q)))}$ (1).", "2+1+1+1")
def md2(p, j, L, k):
    n = (DD(L) / DD(p)).scaleb(k + j)
    return Q(rf"The diameter of a cell is ${p}\times10^{{-{j}}}$ cm. How many such cells placed side by side in a straight line make a length of ${L}\times10^{{{k}}}$ cm? Give the answer in scientific notation.",
             rf"Number of cells $=\dfrac{{{L}\times10^{{{k}}}}}{{{p}\times10^{{-{j}}}}}$ (2); $=\frac{{{L}}}{{{p}}}\times10^{{{k}+{j}}}$ (2); {scitx(n)} (1).", "2+2+1")
MED_D = ([md1(*r) for r in [(2, 3, 3, 1, 2, 1), (3, 2, 2, 1, 1, 2), (5, 1, 2, 2, 2, 1), (2, 4, 5, 1, 1, 1), (3, 3, 4, 2, 1, 1), (5, 2, 3, 1, 1, 2)]]
         + [md2(*r) for r in [(2, 5, 8, 1), (4, 6, 12, 2), (5, 4, 15, 1), (2.5, 3, 7.5, 2), (8, 5, 24, 1), (3, 7, 9, 2)]])

# ================= HARD =================
hA1 = [M4(rf"${pw(a,n)}$ added {a} times equals:", P(a, n + 1), [P(a, a * n), P(a, n + a), P(a * a, n)], f"${a}\\times{a}^{{{n}}}={a}^{{{n+1}}}$") for a, n in [(2, 7), (3, 5), (4, 6), (5, 3), (2, 11)]]
hA2 = [M4(rf"If ${pw(a,lin(p,q))}={pw(a,r)}$, the value of $x$ is:", str((r - q) // p), [str((r + q) // p), str(r - q), str((r - q) // p + 1)], f"${lin(p,q)}={r}$") for a, p, q, r in [(2, 2, 1, 9), (3, 3, -2, 13), (5, 2, 3, 13), (7, 4, -1, 15), (2, 3, 2, 20), (3, 5, -3, 12)]]
hA3 = [M4(rf"The number of digits in ${pw(2,m)}\times{pw(5,n)}$ is:", str(len(str(2 ** m * 5 ** n))), [str(len(str(2 ** m * 5 ** n)) + d) for d in (1, -1, 2)], rf"${pw(2,m)}\times{pw(5,n)}={pw(10,m)}\times{5**(n-m)}$") for m, n in [(4, 7), (6, 9), (5, 8), (3, 7), (7, 10)]]
hA4 = [M4(f"The ones digit of ${a}^{{{n}}}$ is:", str(pow(a, n, 10)), [str((pow(a, n, 10) + d) % 10) for d in (2, 4, 6, 8)], f"Ones digits repeat in the cycle {cyc(a)}") for a, n in [(7, 23), (13, 42), (8, 35), (9, 51), (3, 66)]]
hA5 = [M4(rf"If ${pw(a,'x')}={a**x}$, then ${pw(a,'x-'+str(k))}$ equals:", str(a ** (x - k)), [str(a ** (x + k)), str(a ** k), str(a ** x - k)], f"$x={x}$, so ${a}^{{{x-k}}}$") for a, x, k in [(3, 5, 2), (2, 9, 4), (5, 4, 3), (4, 5, 3), (7, 3, 2)]]
hA6 = [M4(rf"The value of $({pw(a,-1)}+{pw(b,-1)})^{{-1}}$ is:", tx(F(a * b, a + b)), [tx(F(a + b, a * b)), tx(F(1, a + b)), tx(a * b)], rf"$\left(\frac1{{{a}}}+\frac1{{{b}}}\right)^{{-1}}$") for a, b in [(2, 3), (3, 6), (4, 12), (5, 20)]]
HS = [[(3.2, 5), (45, 4), (0.5, 6), (480, 3)], [(7.5, -3), (0.9, -2), (85, -4), (0.06, -1)], [(2.5, 7), (30, 6), (0.28, 8), (310, 5)], [(64, -5), (0.7, -3), (5.2, -4), (8, -5)]]
def big(s): b = max(s, key=lambda t: DD(t[0]).scaleb(t[1])); return [X(*b)] + [X(*t) for t in s if t != b]
hA7 = [M4("Which of the following numbers is the greatest?", big(s)[0], big(s)[1:], "Convert each to usual form and compare") for s in HS]
hA8 = [M4(rf"If ${pw(a,'x')}={k}$, then ${pw(a,'x+'+str(m))}$ equals:", str(k * a ** m), [str(k + a ** m), str(k * m), str(a ** (k + m))], rf"${a}^{{x+{m}}}={a}^x\times{a}^{{{m}}}$") for a, k, m in [(2, 5, 3), (3, 4, 2), (5, 3, 2), (2, 9, 4)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([Q(rf"Find $x$ if ${pw(a,lin(p,q))}={a**(p*x+q)}$.", rf"${a**(p*x+q)}={pw(a,p*x+q)}$ (1); ${lin(p,q)}={p*x+q}$ gives $x={x}$ (1).", "1+1") for a, p, q, x in [(3, 2, -1, 3), (2, 3, 2, 4), (5, 2, -3, 3), (7, 3, -1, 1)]]
          + [Q(rf"Write $({p}\times10^{{{j}}})+({q}\times10^{{{k}}})$ in scientific notation.", rf"Convert to the same power or usual form: {format(DD(p).scaleb(j)+DD(q).scaleb(k),'f')} (1); {scitx(DD(p).scaleb(j)+DD(q).scaleb(k))} (1).", "1+1") for p, j, q, k in [(3, 5, 4, 4), (2.5, 6, 5, 5), (7, -2, 3, -3), (6, 4, 8, 3)]]
          + [Q(rf"Find the ones digit of ${a}^{{{n}}}$.", rf"Ones digits of powers of {a} repeat as {cyc(a)} (1); {n} leaves position {(n-1)%len(cyc(a))+1} in the cycle, so the digit is {pow(a,n,10)} (1).", "1+1") for a, n in [(2, 47), (4, 61), (6, 99), (8, 102)]])
HARD_C = ([Q(rf"A sheet of paper {t} mm thick is folded in half {n} times (assume this is possible). Find the thickness of the folded paper in mm and in cm.", rf"Thickness doubles at each fold: ${t}\times2^{{{n}}}$ (1); $={fmt(F(str(t))*2**n)}$ mm (1); in cm $={fmt(F(str(t))*2**n/10)}$ cm (1).", "1+1+1") for t, n in [(0.1, 10), (0.2, 8), (0.05, 12), (0.4, 6), (0.1, 15), (0.25, 9)]]
          + [Q(rf"Light travels ${3}\times10^{{8}}$ m in one second. How far does it travel in {t} minutes? Give the answer in scientific notation.", rf"{t} min $={60*t}$ s (1); distance $=3\times10^8\times{60*t}$ (1); ={scitx(DD(3*60*t).scaleb(8))} m (1).", "1+1+1") for t in [2, 5, 8, 12, 15, 20]]
          + [Q(rf"Find the value of $\dfrac{{{pw(a,n+1)}+{pw(a,n)}}}{{{pw(a,n-1)}\times({a}+1)}}$.", rf"Take ${pw(a,n)}$ common in the numerator: ${pw(a,n)}({a}+1)$ (1); cancel $({a}+1)$ (1); ${pw(a,n)}\div{pw(a,n-1)}={a}$ (1).", "1+1+1") for a, n in [(2, 5), (3, 4), (5, 3), (4, 6), (7, 2), (6, 3)]])
HARD_D = ([Q(rf"A culture has {p} bacteria and the number becomes {r} times every hour. Write the number after {h} hours as an expression with a power, find its value, and say how many times the original number it is.", rf"Number $={p}\times{r}^{{{h}}}$ (2); value ${p*r**h}$ (2); it is ${r}^{{{h}}}={r**h}$ times the original (1).", "2+2+1") for p, r, h in [(5, 3, 4), (2, 4, 3), (10, 2, 6), (3, 5, 3), (4, 3, 5), (6, 2, 7)]]
          + [Q(rf"Body A has mass ${p}\times10^{{{j}}}$ kg and body B has mass ${q}\times10^{{{k}}}$ kg. Which is heavier? How many times as heavy is it? Find the total mass in scientific notation.", rf"A is heavier (1); ratio $=\frac{{{p}}}{{{q}}}\times10^{{{j}-{k}}}={dfm((DD(p)/DD(q)).scaleb(j-k))}$ times (2); total {scitx(DD(p).scaleb(j)+DD(q).scaleb(k))} kg (2).", "1+2+2") for p, j, q, k in [(6, 24, 3, 22), (9, 12, 3, 9), (8, 7, 2, 5), (1.8, 15, 6, 12), (7.5, 10, 2.5, 8), (4.8, 18, 1.2, 15)]])

def TT(A, B, C, D): return T(A, B, C, D)
TIERS = {"NCERT": TT(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": TT(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": TT(MED_A, MED_B, MED_C, MED_D), "Hard": TT(HARD_A, HARD_B, HARD_C, HARD_D)}
