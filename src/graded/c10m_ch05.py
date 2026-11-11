"""Class 10 Maths Ch 5 - Arithmetic Progressions (graded banks)."""
from mg import *

SLUG, NAME, CHNO = "Arithmetic_Progressions", "Arithmetic Progressions", 5

def an(a, d, n): return F(a) + (n - 1) * F(d)
def sn(a, d, n): return F(n) * (2 * F(a) + (n - 1) * F(d)) / 2
def lst(a, d, k=4): return ", ".join(t(an(a, d, i)) for i in range(1, k + 1)) + ", \\dots"
def AP(a, d): return f"${lst(a,d)}$"
def PA(x): return t(x) if x >= 0 else f"({t(x)})"

def NTH(a, d, n):
    return Q(f"Find the {og(n)} term of the AP {AP(a,d)}", f"$a={t(a)}$, $d={t(d)}$ (1); $a_n=a+(n-1)d$ (1); $a_{{{n}}}={t(a)}+{n-1}({t(d)})={t(an(a,d,n))}$ (1).", "1+1+1")
def SUMQ(a, d, n):
    return Q(f"Find the sum of the first {n} terms of the AP {AP(a,d)}", f"$a={t(a)}$, $d={t(d)}$ (1); $S_n=\\frac{{n}}{{2}}[2a+(n-1)d]$ (1); $S_{{{n}}}=\\frac{{{n}}}{{2}}[{t(2*F(a))}+{n-1}({t(d)})]={t(sn(a,d,n))}$ (1).", "1+1+1")
def WHICH(a, d, n):
    N = an(a, d, n)
    return Q(f"Which term of the AP {AP(a,d)} is {t(N)}?", f"$a_n=a+(n-1)d$: ${t(N)}={t(a)}+(n-1)({t(d)})$ (1); $n-1={n-1}$ (1); $n={n}$, so it is the {og(n)} term (1).", "1+1+1")
def LASTN(a, d, n):
    l = an(a, d, n)
    return Q(f"How many terms are there in the AP ${t(a)}, {t(an(a,d,2))}, {t(an(a,d,3))}, \\dots, {t(l)}$?", f"$a={t(a)}$, $d={t(d)}$, $l={t(l)}$ (1); $l=a+(n-1)d$ gives $n-1={n-1}$ (1); $n={n}$ (1).", "1+1+1")
def TWO(a, d, p, q, r):
    return Q(f"In an AP, the {og(p)} term is {t(an(a,d,p))} and the {og(q)} term is {t(an(a,d,q))}. Find the AP and its {og(r)} term.", f"$a+{co(p-1,"d")}={t(an(a,d,p))}$, $a+{co(q-1,"d")}={t(an(a,d,q))}$ (2); subtracting, $d={t(d)}$, $a={t(a)}$ (2); $a_{{{r}}}={t(an(a,d,r))}$ (1).", "2+2+1")
def SFIND(a, d, n):
    S = sn(a, d, n)
    return Q(f"How many terms of the AP {AP(a,d)} must be taken so that the sum is {t(S)}?", f"$S_n=\\frac{{n}}{{2}}[2({t(a)})+(n-1)({t(d)})]={t(S)}$ (1); form quadratic in $n$ (2); $n={n}$ (the other root is rejected) (2).", "1+2+2")
def MID(a, d, n, k):
    return Q(f"In an AP, $a={t(a)}$, $d={t(d)}$, $n={n}$. Find $a_n$ and $S_n$.", f"$a_n={t(a)}+{n-1}({t(d)})={t(an(a,d,n))}$ (1); $S_n=\\frac{{{n}}}{{2}}({t(a)}+{t(an(a,d,n))})={t(sn(a,d,n))}$ (2).", "1+2")
def INST(a, d, n):
    return Q(f"A loan is repaid in {n} monthly instalments; the first is ₹{a} and each later instalment is ₹{d} more than the previous. Find the instalment in the last month and the total amount repaid.", f"AP: $a={a}$, $d={d}$, $n={n}$ (1); last $=a+(n-1)d={a+(n-1)*d}$ (2); total $=S_n=\\frac{{{n}}}{{2}}({a}+{a+(n-1)*d})={sn(a,d,n)}$ (2).", "1+2+2")
def LAD(top, bot, n):
    return Q(f"A ladder has {n} rungs whose lengths decrease uniformly from {top} cm at the bottom to {bot} cm at the top. Find the length of the wood needed for the rungs and the length of the middle rung." , f"AP with $a={top}$, $l={bot}$, $n={n}$ (1); $S_n=\\frac{{{n}}}{{2}}({top}+{bot})={t(F(n*(top+bot),2))}$ cm (2); middle term $=\\frac{{{top}+{bot}}}{{2}}={t(F(top+bot,2))}$ cm (2).", "1+2+2")

E1 = [(3, 4, 12), (5, 3, 10), (2, 7, 8), (10, 5, 15), (1, 6, 9), (4, 2, 20)]
def CHK(a, d):
    return MS(f"The common difference of the AP {AP(a,d)} is:", n(d), [n(-d), n(d + 1), n(2 * d)], f"$a_2-a_1={t(d)}$")
eA = [[CHK(a, d) for a, d in [(3, 4), (10, -3), (7, 5), (-2, 6), (1, F(1, 2)), (20, -4)]],
      [MN(f"The {og(n)} term of the AP {AP(a,d)} is:", an(a, d, n), [a + n * d, a + (n - 2) * d, n * d, a * n], why=f"$a+(n-1)d={t(an(a,d,n))}$") for a, d, n in [(3, 4, 10), (5, 3, 8), (2, 7, 6), (10, 5, 5), (1, 6, 7)]],
      [MN(f"The sum of the first {n} terms of {AP(a,d)} is:", sn(a, d, n), [n * (2 * a + (n - 1) * d), sn(a, d, n - 1), sn(a, d, n + 1)], why="$S_n=\\frac n2[2a+(n-1)d]$") for a, d, n in [(1, 1, 10), (2, 2, 8), (5, 5, 6), (1, 2, 5), (3, 3, 4)]],
      [MS("Which of the following sequences is an AP?", AP(a, d), [f"${t(a)}, {t(a+d)}, {t(a+3*d)}, {t(a+4*d)}, \\dots$", f"${t(a)}, {t(a+d)}, {t(a+3*d)}, {t(a+6*d)}, \\dots$", f"${t(a)}, {t(a+d)}, {t(a+2*d+1)}, {t(a+3*d+2)}, \\dots$"], f"Only {AP(a,d)} has the same difference ${t(d)}$ between consecutive terms") for a, d in [(4, 3), (9, -2), (1, 5), (6, 6), (-3, 4)]],
      [MN(f"In an AP with $a={a}$ and $d={d}$, the 2nd term is:", a + d, [a - d, a + 2 * d, a * d], why="$a_2=a+d$") for a, d in [(5, 3), (8, -2), (11, 4), (6, 6), (12, -1)]],
      [MN(f"The 1st term of an AP is {a} and the 3rd term is {a+2*d}. The common difference is:", d, [2 * d, d + a, F(d, 2), 3 * d], why="$a_3=a+2d$") for a, d in [(4, 3), (7, 5), (2, 6), (10, 2)]]]
eB = ([Q(f"Write the first four terms of the AP with $a={a}$ and $d={d}$.", f"${lst(a,d)}$ (2).", "2") for a, d in [(5, 3), (10, -2), (7, 4), (-3, 5)]]
      + [Q(f"Find the common difference of the AP {AP(a,d)}", f"$d=a_2-a_1={t(an(a,d,2))}-({t(a)})$ (1) $={t(d)}$ (1).", "1+1") for a, d in [(6, 5), (20, -3), (4, F(3, 2)), (-8, 4)]]
      + [Q(f"Is {AP(a,d)} an AP? If so, find the next term.", f"$d={t(d)}$ constant (1); next term ${t(an(a,d,5))}$ (1).", "1+1") for a, d in [(2, 9), (15, -4), (3, 6), (11, 7)]])
eC = ([NTH(a, d, n) for a, d, n in E1] + [SUMQ(a, d, n) for a, d, n in [(2, 3, 10), (5, 5, 8), (1, 4, 12), (7, 2, 15), (3, 6, 9), (10, 3, 6)]]
      + [WHICH(a, d, n) for a, d, n in [(4, 5, 11), (3, 7, 9), (2, 4, 14), (10, 3, 8), (5, 6, 13), (1, 8, 7)]])
eD = ([LASTN(a, d, n) for a, d, n in [(7, 3, 20), (5, 5, 16), (2, 6, 12), (10, 4, 25), (4, 7, 15), (3, 9, 10)]]
      + [MID(a, d, n, 0) for a, d, n in [(6, 4, 20), (9, 3, 14), (2, 5, 18), (15, 2, 25), (8, 6, 12), (4, 3, 30)]])

nA = [[MN(f"The {og(n)} term of {AP(a,d)} is:", an(a, d, n), [a + n * d, a + (n - 2) * d, n * d, a * n], why="$a_n=a+(n-1)d$") for a, d, n in [(21, 18 - 21, 10), (8, 5, 15), (-5, 2, 12), (14, 3, 9), (11, -4, 7)]],
      [MN(f"The {og(n)} term from the end of the AP with last term {l} and $d={d}$ is:", l - (n - 1) * d, [l + (n - 1) * d, l - n * d, l - (n - 2) * d, l - d], why="Reverse AP has difference $-d$") for l, d, n in [(100, 4, 5), (80, 3, 8), (150, 5, 6), (90, 6, 4), (60, 2, 10)]],
      [MN(f"If $a_n=3n+{c}$, then the common difference is:", 3, [c, 3 + c, 6, 3 * c, 9], why="$a_{n+1}-a_n=3$") for c in [2, 5, 7, 1, 9]],
      [MN(f"If $S_n=n^2+{c}n$, then $a_1=$", 1 + c, [c, 1, 2 + c, 2 * c + 1], why="$a_1=S_1$") for c in [2, 3, 4, 5, 6]],
      [MN(f"The sum of first {n} positive odd numbers is:", n * n, [n * (n + 1), n * (n - 1), 2 * n * n, n * n + 1], why="$S_n=n^2$") for n in [6, 8, 10, 12, 15]],
      [MN(f"The 10th term of the AP {AP(a,d)} is:", an(a, d, 10), [a + 10 * d, a + 8 * d, 10 * d, 10 * a, a + 11 * d], why="$a+9d$") for a, d in [(F(1, 2), F(1, 2)), (7, -3), (-4, 5), (2, F(3, 2)), (9, 2)]]]
nB = ([Q(f"Which term of the AP {AP(a,d)} is {t(an(a,d,n))}?", f"$a_n={t(a)}+(n-1)({t(d)})$ (1); $n={n}$ (1).", "1+1") for a, d, n in [(3, 5, 13), (8, 3, 22), (-2, 4, 10), (20, -3, 8)]]
      + [Q(f"Find the sum of the first {n} multiples of {m}.", f"AP: ${m}, {2*m}, {3*m},\\dots$ (1); $S_n=\\frac{{{n}}}{{2}}[{2*m}+{(n-1)*m}]={sn(m,m,n)}$ (1).", "1+1") for n, m in [(10, 3), (12, 5), (15, 4), (20, 7)]]
      + [Q(f"Find the sum of the AP ${t(a)}, {t(an(a,d,2))}, \\dots, {t(an(a,d,n))}$.", f"$n={n}$ (1); $S=\\frac{{{n}}}{{2}}({t(a)}+{t(an(a,d,n))})={t(sn(a,d,n))}$ (1).", "1+1") for a, d, n in [(-5, 3, 12), (8, 4, 15), (12, -2, 10), (2, 5, 20)]])
nC = ([TWO(a, d, p, q, r) for a, d, p, q, r in [(3, 4, 2, 5, 10), (5, 3, 3, 7, 12), (-2, 6, 4, 6, 9), (10, -2, 5, 9, 15), (1, 5, 3, 8, 11), (7, 2, 2, 10, 20)]]
      + [LASTN(a, d, n) for a, d, n in [(18, F(-5, 2), 12), (6, 4, 21), (9, 11, 16), (-7, 3, 30), (4, 6, 18), (12, 5, 22)]]
      + [SUMQ(a, d, n) for a, d, n in [(15, 4, 22), (-9, 2, 25), (8, F(1, 2), 20), (33, -3, 14), (5, 8, 18), (21, 6, 16)]])
nD = ([SFIND(a, d, n) for a, d, n in [(24, -2, 9), (9, 8, 10), (30, -3, 8), (5, 4, 12), (17, 6, 11), (45, -4, 10)]]
      + [INST(a, d, n) for a, d, n in [(100, 10, 20), (200, 15, 12), (500, 25, 10), (50, 5, 16), (300, 20, 15), (1000, 50, 8)]])

mA = [[MN(f"The {og(n)} term of the AP whose 1st term is {a} and {og(k)} term is {an(a,d,k)} is:", an(a, d, n), [a + n * d, a + (n - 2) * d, n * d, a * n], why=f"First find $d={d}$") for a, d, k, n in [(7, 3, 5, 12), (4, 6, 4, 9), (11, 2, 6, 15), (3, 5, 3, 10), (9, 4, 5, 14)]],
      [MN(f"The number of terms in the AP ${t(a)}, {t(a+d)}, \\dots, {t(an(a,d,n))}$ is:", n, [n - 1, n + 1, n + 2, n - 2], why="$n=\\frac{l-a}{d}+1$") for a, d, n in [(5, 4, 24), (8, 3, 31), (2, 6, 17), (11, 5, 26), (7, 9, 19)]],
      [MN(f"The sum of all two-digit multiples of {m} is:", sum(x for x in range(10, 100) if x % m == 0), [sum(x for x in range(m, 100, m)), sum(x for x in range(10, 101) if x % m == 0), sum(x for x in range(10, 100) if x % m == 0) - max(x for x in range(10, 100) if x % m == 0), sum(x for x in range(10, 100) if x % m == 0) - min(x for x in range(10, 100) if x % m == 0)], why="AP of two-digit multiples") for m in [3, 4, 5, 6, 7]],
      [MN(f"The sum of the first {n} terms of the AP {AP(a,d)} is:", sn(a, d, n), [n * (2 * a + (n - 1) * d), sn(a, d, n - 1), sn(a, d, n + 1)], why="Use $S_n$") for a, d, n in [(12, 5, 14), (-6, 4, 20), (30, -3, 12), (9, 7, 16), (2, 9, 11)]],
      [MN(f"The middle term of an AP with {2*k+1} terms, first term {a} and last term {a+2*k*d}, is:", a + k * d, [a + (k + 1) * d, a + (k - 1) * d, a + 2 * k * d, k * d], why="Middle term $=\\frac{a+l}{2}$") for a, d, k in [(5, 3, 6), (8, 4, 5), (2, 7, 4), (10, 5, 7), (3, 6, 8)]],
      [MN(f"If $a_{{{p}}}={an(a,d,p)}$ and $d={d}$, then $a=$", a, [an(a, d, p) - p * d, an(a, d, p) - (p - 2) * d, an(a, d, p) + (p - 1) * d, an(a, d, p) - d], why="$a=a_p-(p-1)d$") for a, d, p in [(4, 3, 8), (10, 2, 12), (7, 5, 6), (1, 4, 9), (13, 3, 7)]]]
mB = ([WHICH(a, d, n) for a, d, n in [(7, 6, 21), (11, 4, 18), (-3, 5, 14), (30, -2, 12)]] + [SUMQ(a, d, n) for a, d, n in [(14, 6, 18), (-12, 4, 26), (6, F(3, 2), 20), (27, -2, 15)]]
      + [Q(f"Find the sum of all natural numbers between {a} and {b} that are divisible by {m}.", f"First term {m*(a//m+1)}, last term {m*((b-1)//m)} (1); $n={(m*((b-1)//m)-m*(a//m+1))//m+1}$, sum $={sum(x for x in range(a+1,b) if x%m==0)}$ (1).", "1+1") for a, b, m in [(1, 100, 4), (10, 200, 5), (5, 150, 6), (20, 300, 7)]])
mC = ([TWO(a, d, p, q, r) for a, d, p, q, r in [(5, 7, 3, 8, 15), (-4, 6, 2, 7, 12), (12, -3, 4, 9, 14), (8, 5, 3, 6, 20), (2, 9, 5, 10, 13), (15, 4, 2, 11, 18)]]
      + [Q(f"Find the sum of the first {n} terms of the AP whose $n$th term is $a_n={p}n{sg(c)}$.", f"$a_1={p+c}$, $a_{{{n}}}={p*n+c}$ (1); $d={p}$ (1); $S_{{{n}}}=\\frac{{{n}}}{{2}}({p+c}+{p*n+c})={sn(p+c,p,n)}$ (1).", "1+1+1") for p, c, n in [(3, 2, 20), (5, -1, 15), (4, 7, 12), (2, 9, 25), (6, -4, 10), (7, 3, 16)]]
      + [Q(f"The sum of the first {n} terms of an AP is {sn(a,d,n)} and the first term is {a}. Find $d$ and the {og(n)} term.", f"$S_n=\\frac{{n}}{{2}}[2a+(n-1)d]$: ${sn(a,d,n)}=\\frac{{{n}}}{{2}}[{2*a}+{n-1}d]$ (1); $d={d}$ (1); $a_{{{n}}}={an(a,d,n)}$ (1).", "1+1+1") for a, d, n in [(5, 3, 10), (8, 4, 12), (2, 6, 15), (11, 2, 20), (4, 5, 8), (7, 3, 16)]])
mD = ([SFIND(a, d, n) for a, d, n in [(54, -4, 10), (12, 6, 14), (-10, 4, 12), (36, -3, 11), (6, 5, 16), (60, -5, 9)]]
      + [LAD(a, b, n) for a, b, n in [(45, 25, 11), (60, 30, 13), (50, 20, 7), (80, 40, 9), (75, 35, 17), (66, 30, 19)]])

hA = [[MN(f"If the {og(p)} term of an AP is {q} and the {og(q)} term is {p}, then the {p+q}th term is:", 0, [1, p + q, p * q], "Common difference is $-1$; $a_{p+q}=0$") for p, q in [(4, 9), (5, 11), (3, 8), (6, 7), (2, 13)]],
      [MN(f"The sum of the first {n} terms of an AP is {sn(a,d,n)}, and its first term is {a}. The {og(n)} term is:", an(a, d, n), [F(2 * sn(a, d, n), n), F(sn(a, d, n), n) - a, F(2 * sn(a, d, n), n) + a, sn(a, d, n) - a], why="$a_n=\\frac{2S_n}{n}-a$") for a, d, n in [(6, 4, 13), (3, 7, 9), (10, 3, 15), (5, 8, 11), (12, 2, 17)]],
      [MN(f"In an AP, $S_{{{n}}}={sn(a,d,n)}$ and $S_{{{n-1}}}={sn(a,d,n-1)}$. Then $a_{{{n}}}=$", an(a, d, n), [an(a, d, n) + d, an(a, d, n) - d, sn(a, d, n) + sn(a, d, n - 1), sn(a, d, n) - sn(a, d, n - 2)], why="$a_n=S_n-S_{n-1}$") for a, d, n in [(4, 6, 8), (9, 5, 10), (3, 8, 12), (7, 4, 15), (2, 9, 7)]],
      [MN(f"The sum of the first $n$ terms of an AP is $S_n={p}n^2+{q}n$. Its common difference is:", 2 * p, [p, q, p + q, 4 * p], why="$d=2p$") for p, q, n in [(2, 3, 10), (3, 1, 8), (4, 5, 6), (5, 2, 9), (1, 7, 12)]],
      [MN(f"The sum of the series ${PA(a)}+{PA(a+d)}+{PA(a+2*d)}+\\dots+{PA(an(a,d,n))}$ is:", sn(a, d, n), [n * (2 * a + (n - 1) * d), sn(a, d, n - 1), sn(a, d, n + 1)], why="Find $n$ first") for a, d, n in [(5, 4, 25), (11, 6, 18), (-8, 3, 30), (14, 5, 21), (9, 8, 16)]],
      [MN(f"How many terms of the AP {AP(a,d)} give sum 0?", n, [n - 1, n + 1, 2 * n], why="$S_n=0\\Rightarrow n=1-\\frac{2a}{d}$") for a, d, n in [(20, -4, 11), (18, -3, 13), (30, -5, 13), (24, -4, 13), (14, -2, 15)]]]
hB = ([Q(f"The {og(p)} term of an AP is {q} and the {og(q)} term is {p}. Find the {p+q}th term.", f"$a+{p-1}d={q}$, $a+{q-1}d={p}$ (1); $d=-1$, $a={p+q-1}$ so $a_{{{p+q}}}=0$ (1).", "1+1") for p, q in [(4, 9), (5, 12), (6, 11), (3, 14)]]
      + [Q(f"If $S_n={p}n^2+{q}n$, find the first term and the common difference.", f"$a_1=S_1={p+q}$ (1); $S_2={4*p+2*q}$, $a_2={3*p+q}$, $d={2*p}$ (1).", "1+1") for p, q in [(3, 4), (2, 5), (4, 1), (5, 3)]]
      + [Q(f"In an AP, $a_3+a_7={an(a,d,3)+an(a,d,7)}$ and $a_2+a_9={an(a,d,2)+an(a,d,9)}$. Find $a$ and $d$.", f"$2a+8d={an(a,d,3)+an(a,d,7)}$, $2a+9d={an(a,d,2)+an(a,d,9)}$ (1); $d={d}$, $a={a}$ (1).", "1+1") for a, d in [(5, 3), (2, 4), (8, 2), (1, 6)]])
def SQ(a, d):
    return Q(f"The sum of the first $n$ terms of an AP is $S_n={t(F(d,2))}n^2+{t(F(2*a-d,2))}n$. Find the 7th term.", f"$a_n=S_n-S_{{n-1}}$ (1); $a_n={t(an(a,d,1))}+(n-1){t(d)}$ (2); $a_7={t(an(a,d,7))}$ (2).", "1+2+2")
hC = ([Q(f"In an AP, $S_{{{n}}}={sn(a,d,n)}$ and $S_{{{m}}}={sn(a,d,m)}$. Find the AP.", f"$\\frac{{{n}}}{{2}}(2a+{n-1}d)={sn(a,d,n)}$ and $\\frac{{{m}}}{{2}}(2a+{m-1}d)={sn(a,d,m)}$ (1); simplify to linear equations in $a,d$ (1); $a={a}$, $d={d}$, AP ${lst(a,d)}$ (1).", "1+1+1") for a, d, n, m in [(5, 3, 6, 10), (2, 4, 5, 9), (8, 2, 7, 12), (3, 5, 4, 8), (10, 3, 6, 11), (1, 7, 5, 10)]]
      + [Q(f"Find the sum of the first {n} terms of the AP whose {og(p)} term is {an(a,d,p)} and {og(q)} term is {an(a,d,q)}.", f"$d={d}$, $a={a}$ (2); $S_{{{n}}}={t(sn(a,d,n))}$ (1).", "2+1") for a, d, p, q, n in [(6, 4, 3, 8, 16), (9, 5, 2, 7, 20), (12, 3, 4, 9, 14), (4, 7, 3, 6, 18), (15, 2, 5, 12, 22), (7, 6, 2, 5, 12)]]
      + [Q(f"Find the sum of all integers between {a} and {b} that leave remainder {r} when divided by {m}.", f"Terms form an AP with $d={m}$ (1); count and endpoints (1); sum $={sum(x for x in range(a+1,b) if x%m==r)}$ (1).", "1+1+1") for a, b, m, r in [(10, 200, 7, 3), (20, 300, 9, 4), (5, 150, 6, 1), (30, 400, 11, 5), (0, 120, 8, 2), (50, 500, 13, 6)]])
hD = ([LAD(a, b, n) for a, b, n in [(100, 40, 21), (90, 30, 31), (70, 22, 25), (120, 48, 19)]]
      + [INST(a, d, n) for a, d, n in [(1500, 100, 24), (800, 60, 30), (2500, 150, 18), (600, 45, 40)]]
      + [Q(f"A sum of ₹{S} is to be given as {n} prizes, each prize ₹{d} less than the preceding one. Find the value of the first and last prize.", f"$S_n=\\frac{{{n}}}{{2}}[2a-{(n-1)*d}]={S}$ (2); $a={a0}$ (2); last prize ₹{a0-(n-1)*d} (1).", "2+2+1") for n, d, a0 in [(8, 20, 180), (10, 30, 250), (6, 50, 400), (12, 15, 200)] for S in [sn(a0, -d, n)]])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
