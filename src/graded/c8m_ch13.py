"""Class 8 Maths Ch 13 - Algebra Play (expressions, number tricks, patterns, identities)."""
from c8m_u import *

SLUG, NAME, CHNO = "Algebra_Play", "Algebra Play", 13

def P(*ts, raw=False):
    s = ""
    for c, v in ts:
        if c == 0: continue
        a = abs(c); body = (str(a) if (a != 1 or v == "") else "") + v
        s += (("-" if c < 0 else "") + body) if not s else (("-" if c < 0 else "+") + body)
    s = s or "0"
    return s if raw else "$" + s + "$"
def PM(q, ans, wrongs, why=""):
    return M4(q, ans, wrongs, why)
def rev(n): return int(str(n)[::-1])

# ================= EASY =================
e1 = [PM(f"The expression for '{c} more than {k} times a number $x$' is:", P((k, "x"), (c, "")), [P((c, "x"), (k, "")), P((k, ""), (0, ""), (c + k, "x")), f"${k}(x+{c})$"], f"{k} times $x$ is ${k}x$; add {c}") for k, c in [(2, 5), (3, 4), (5, 7), (4, 9), (6, 2), (7, 3), (8, 1), (9, 6)]]
e2 = [ND(f"The value of ${a}x+{b}$ when $x={v}$ is:", a * v + b, f"${a}\\times{v}+{b}$") for a, b, v in [(3, 4, 5), (2, 7, 6), (5, 3, 4), (4, 9, 3), (6, 2, 7), (7, 5, 2)]]
e3 = [PM(f"On simplifying ${a}x+{b}+{c}x+{d}$ we get:", P((a + c, "x"), (b + d, "")), [P((a * c, "x"), (b + d, "")), P((a + c, "x"), (b * d, "")), P((a + c + b + d, "x"))], "Add like terms") for a, b, c, d in [(2, 3, 4, 5), (3, 7, 5, 1), (6, 2, 3, 8), (4, 9, 2, 6), (7, 4, 1, 3), (5, 5, 6, 2)]]
e4 = [PM(f"The two-digit number with tens digit $x$ and ones digit {c} is written as:", P((10, "x"), (c, "")), [P((1, "x"), (c, "")), P((10 * c, ""), (1, "x")), P((c, "x"))], "Place value: tens × 10 + ones") for c in [2, 3, 4, 5, 6, 7]]
e5 = [ND(f"In a calendar, the four dates {d}, {d+1}, {d+7} and {d+8} form a $2\\times2$ block. Their sum is:", 4 * d + 16, f"${d}+{d+1}+{d+7}+{d+8}$", wrong=[4 * d + 8, 4 * d + 14, 4 * d + 18]) for d in [3, 6, 9, 11, 15, 19]]
e6 = [M4("In the expression $5x+7$, the coefficient of $x$ is:", "5", ["7", "12", "x"], "Number multiplying the variable"),
      M4("Which pair are like terms?", "$3x$ and $9x$", ["$3x$ and $9y$", "$3x$ and $9x^2$", "$3x$ and $9$"], "Same variable and power"),
      M4("The number of terms in $3x+2y-5$ is:", "3", ["2", "4", "1"], "Terms separated by + or −"),
      M4("If $x=0$, the value of $9x+4$ is:", "4", ["0", "9", "13"], "$9\\times0+4$"),
      M4("The expression 'a number $y$ decreased by 6' is:", "$y-6$", ["$6-y$", "$6y$", "$y+6$"], "Subtract 6"),
      M4("The expression 'three times the sum of $x$ and 2' is:", "$3(x+2)$", ["$3x+2$", "$x+6$", "$3x\\times2$"], "Sum first, then multiply")]
EASY_A = [e1, e2, e3, e4, e5, e6]
EASY_B = ([Q(f"Write an algebraic expression for: {w}.", f"{ex} (2).", "2") for w, ex in [("the sum of 7 and 5 times a number $n$", P((5, "n"), (7, ""))), ("a number $y$ multiplied by 4 and then reduced by 9", P((4, "y"), (-9, ""))), ("6 less than twice $m$", P((2, "m"), (-6, ""))), ("one-third of $x$ increased by 8", "$\\frac{x}{3}+8$")]]
          + [Q(f"Find the value of ${a}x+{b}y$ when $x={p}$ and $y={r}$.", f"${a}\\times{p}+{b}\\times{r}={a*p+b*r}$ (1+1).", "1+1") for a, b, p, r in [(3, 2, 4, 5), (5, 4, 2, 6), (7, 3, 3, 4), (6, 5, 5, 2)]]
          + [Q(f"Simplify ${a}x+{b}y+{c}x+{d}y$.", f"{P((a+c,'x'),(b+d,'y'))} (1+1).", "1+1") for a, b, c, d in [(2, 3, 5, 4), (6, 1, 2, 8), (4, 7, 3, 2), (9, 5, 1, 6)]])
EASY_C = ([Q(f"Evaluate ${a}p+{b}q-{c}$ for $p={p}$, $q={r}$.", f"${a}\\times{p}+{b}\\times{r}-{c}$ (2) $={a*p+b*r-c}$ (1).", "2+1") for a, b, c, p, r in [(3, 4, 5, 6, 2), (5, 2, 8, 4, 7), (6, 3, 9, 5, 4), (4, 5, 6, 8, 3), (7, 2, 10, 3, 9), (8, 6, 12, 2, 5)]]
          + [Q(f"Simplify ${a}x+{b}-{c}x+{d}-{e}$.", f"Like terms: ${a}x-{c}x={P((a-c,'x'),raw=True)}$ (1); constants ${b}+{d}-{e}={b+d-e}$ (1); result {P((a-c,'x'),(b+d-e,''))} (1).", "1+1+1") for a, b, c, d, e in [(9, 4, 5, 8, 2), (12, 3, 7, 6, 4), (8, 10, 3, 5, 9), (15, 6, 8, 2, 1), (11, 9, 6, 7, 5), (14, 5, 9, 4, 3)]]
          + [Q(f"Find the sum of {10*a+b} and its reverse {10*b+a}. Show that it is a multiple of 11.", f"${10*a+b}+{10*b+a}={11*(a+b)}$ (2); $={11}\\times{a+b}$, a multiple of 11 (1).", "2+1") for a, b in [(2, 3), (4, 5), (3, 6), (5, 7), (6, 2), (7, 4)]])
def pyr3(a, b, c): return a + b, b + c, a + 2 * b + c
EASY_D = ([Q(f"Think of a number $n$. Multiply it by {m}, add {c} and then subtract {c}. Show the result algebraically. What is the result when $n={v}$?", f"${m}n+{c}-{c}={m}n$ (3); for $n={v}$, result $={m*v}$ (2).", "3+2") for m, c, v in [(3, 5, 4), (4, 7, 6), (5, 2, 3), (6, 9, 5), (7, 4, 2), (8, 6, 7)]]
          + [Q(f"In a number pyramid each block is the sum of the two blocks below it. The bottom row is {a}, {b}, {c}. Find the middle row and the top block.", f"Middle row: {a}+{b}={a+b} (1), {b}+{c}={b+c} (1); top $={a+b}+{b+c}={a+2*b+c}$ (3).", "1+1+3") for a, b, c in [(2, 5, 3), (4, 1, 6), (7, 2, 4), (3, 8, 5), (6, 3, 9), (5, 7, 2)]])

# ================= NCERT =================
n1 = [PM(f"Think of a number $n$. Add {a}, multiply by {m}, then subtract {a*m}. The result is:", P((m, "n")), [P((m, "n"), (a, "")), P((1, "n"), (a, "")), P((a, "n"))], f"${m}(n+{a})-{a*m}={m}n$") for a, m in [(3, 5), (6, 4), (8, 2), (9, 3), (5, 6), (7, 4)]]
n2 = [PM(f"The sum of {k} consecutive integers starting with $n$ is:", P((k, "n"), (k * (k - 1) // 2, "")), [P((k, "n"), (k * (k - 1) // 2 + 1, "")), P((k, "n")), P((1, "n"), (k * (k - 1) // 2, ""))], f"$n+(n+1)+\\dots={k}n+{k*(k-1)//2}$") for k in [3, 4, 5, 6, 7, 8]]
n3 = [ND(f"In a number pyramid each block is the sum of the two below it. The bottom row is {a}, {b}, {c}, {d}. The top block is:", a + 3 * b + 3 * c + d, "Top $=a+3b+3c+d$", wrong=[a + b + c + d, 2 * (a + b + c + d), a + 2 * b + 2 * c + d]) for a, b, c, d in [(1, 2, 3, 4), (2, 5, 1, 3), (4, 1, 2, 6), (3, 3, 2, 5), (6, 2, 4, 1)]]
n4 = [ND(f"In a calendar the nine dates in a $3\\times3$ block have the middle date {c}. Their sum is:", 9 * c, "Sum $=9\\times$ middle date", wrong=[3 * c, 9 * c + 9, 9 * c - 9]) for c in [10, 12, 16, 19, 23]]
n5 = [ND(f"The value of ${n}\\times{n}-{n-1}\\times{n+1}$ is:", 1, "$n^2-(n-1)(n+1)=1$", wrong=[0, 2, n]) for n in [8, 12, 15, 25, 40]]
n6 = [PM(f"For any $n$, $(n+{a})^2-(n-{a})^2$ equals:", P((4 * a, "n")), [P((2 * a, "n")), P((2 * a * a, "")), P((4 * a * a, ""))], f"Expand: $4an=4\\times{a}n$") for a in [1, 2, 3, 4, 5, 6]]
NCERT_A = [n1, n2, n3, n4, n5, n6]
NCERT_B = ([Q(f"Show that the sum of {10*a+b} and its reverse is divisible by 11.", f"Sum $={10*a+b}+{10*b+a}={11*(a+b)}$ (1) $=11\\times{a+b}$ (1).", "1+1") for a, b in [(1, 6), (3, 8), (4, 9), (2, 7)]]
           + [Q(f"Think of a number $n$, add {a}, multiply by {m}, subtract {a*m}, divide by {m}. Show that the answer is $n$.", f"${m}(n+{a})-{a*m}={m}n$ (1); $\\div{m}$ gives $n$ (1).", "1+1") for a, m in [(4, 3), (7, 5), (9, 2), (6, 6)]]
           + [Q(f"Express the sum of two consecutive odd numbers starting with $2n+1$ and show that it is a multiple of 4.", "Numbers $2n+1$ and $2n+3$ (1); sum $=4n+4=4(n+1)$ (1).", "1+1") for _ in range(1)] + [Q(f"Find the sum of the {k} consecutive integers {a}, {a+1}, ..., {a+k-1} using the expression ${k}n+{k*(k-1)//2}$.", f"$n={a}$: ${k}\\times{a}+{k*(k-1)//2}$ (1) $={k*a+k*(k-1)//2}$ (1).", "1+1") for k, a in [(5, 12), (6, 20), (4, 33)]])
NCERT_C = ([Q(f"In a number pyramid with bottom row {a}, {b}, {c}, {d}, each block is the sum of the two below it. Find all the blocks.", f"Row 2: {a+b}, {b+c}, {c+d} (1); row 3: {a+2*b+c}, {b+2*c+d} (1); top $={a+3*b+3*c+d}$ (1).", "1+1+1") for a, b, c, d in [(2, 3, 1, 4), (5, 2, 3, 1), (1, 6, 2, 3), (4, 4, 1, 2), (3, 1, 5, 2), (6, 2, 2, 3)]]
           + [Q(f"Show that the difference of {10*a+b} and its reverse {10*b+a} is a multiple of 9.", f"${10*a+b}-{10*b+a}={9*(a-b)}$ (2) $=9\\times{a-b}$ (1).", "2+1") for a, b in [(8, 3), (9, 4), (7, 2), (6, 1), (9, 5), (8, 2)]]
           + [Q(f"A $3\\times3$ block of calendar dates has middle date {c}. Write the nine dates and show that their sum is 9 times the middle date.", f"Dates: {c-8}, {c-7}, {c-6}, {c-1}, {c}, {c+1}, {c+6}, {c+7}, {c+8} (1); sum $={9*c}$ (1); $=9\\times{c}$ (1).", "1+1+1") for c in [11, 13, 17, 20, 22, 24]])
NCERT_D = ([Q(f"Show that the sum of {k} consecutive integers starting with $n$ is {P((k,'n'),(k*(k-1)//2,''))} and verify it for $n={v}$.", f"Terms $n, n+1, \\dots, n+{k-1}$ (1); sum ${k}n+{k*(k-1)//2}$ (2); for $n={v}$ the numbers add to ${sum(range(v,v+k))}$ and ${k}\\times{v}+{k*(k-1)//2}={k*v+k*(k-1)//2}$ (2).", "1+2+2") for k, v in [(3, 14), (4, 9), (5, 21), (6, 7), (7, 15), (8, 30)]]
           + [Q(f"Think of a number $n$. Double it, add {a}, halve the result and subtract $n$. Show algebraically that the final answer is always {a//2}. Verify for $n={v}$.", f"$(2n+{a})/2-n=n+{a//2}-n={a//2}$ (3); for $n={v}$: $(2\\times{v}+{a})/2-{v}={(2*v+a)//2-v}$ (2).", "3+2") for a, v in [(10, 7), (14, 9), (8, 12), (16, 5), (12, 20), (18, 6)]])

# ================= MEDIUM =================
m1 = [PM(f"On expanding ${a}(x+{b})+{c}x$ we get:", P((a + c, "x"), (a * b, "")), [P((a + c, "x"), (b, "")), P((a, "x"), (a * b + c, "")), P((a * c, "x"), (a * b, ""))], f"${a}x+{a*b}+{c}x$") for a, b, c in [(3, 4, 2), (5, 2, 4), (4, 6, 3), (6, 3, 5), (7, 2, 9)]]
m2 = [PM(f"$(x+{a})(x+{b})$ equals:", P((1, "x^2"), (a + b, "x"), (a * b, "")), [P((1, "x^2"), (a * b, "x"), (a + b, "")), P((1, "x^2"), (a + b, "")), P((2, "x"), (a + b, ""))], "Multiply term by term") for a, b in [(2, 5), (3, 4), (6, 2), (7, 3), (5, 8)]]
m3 = [ND(f"If $a={a}$ and $b={b}$, the value of ${p}a-{q}b+{r}$ is:", p * a - q * b + r, f"${p}\\times{a}-{q}\\times{b}+{r}$") for a, b, p, q, r in [(9, 4, 3, 5, 8), (12, 3, 4, 6, 10), (8, 5, 6, 2, 7), (15, 2, 2, 9, 5), (10, 7, 5, 4, 12)]]
m4_ = [PM(f"A rectangle has length $({p}x+{q})$ cm and breadth $({r}x+{s})$ cm. Its perimeter (cm) is:", P((2 * (p + r), "x"), (2 * (q + s), "")), [P(((p + r), "x"), ((q + s), "")), P((p * r, "x^2"), (q * s, "")), P((2 * (p + r), "x"), (q + s, ""))], "Perimeter $=2(l+b)$") for p, q, r, s in [(3, 2, 2, 5), (4, 1, 3, 6), (5, 3, 1, 4), (2, 7, 6, 2), (6, 5, 2, 3)]]
m5 = [ND(f"If $x+y={s}$ and $xy={p}$, then $x^2+y^2$ equals:", s * s - 2 * p, "$(x+y)^2=x^2+y^2+2xy$", wrong=[s * s, s * s + 2 * p, s * s - p]) for s, p in [(9, 14), (10, 21), (12, 35), (7, 12), (15, 44)]]
m6 = [PM(f"The sum of {k} consecutive even numbers starting with $2n$ is:", P((2 * k, "n"), (k * (k - 1), "")), [P((2 * k, "n"), (k, "")), P((k, "n"), (k * (k - 1), "")), P((2 * k, "n"), (k * (k - 1) + 2, ""))], f"$2n+(2n+2)+\\dots$: ${2*k}n+{k*(k-1)}$") for k in [3, 4, 5, 6, 7]]
MED_A = [m1, m2, m3, m4_, m5, m6]
MED_B = ([Q(f"Expand and simplify ${a}(x+{b})+{c}(x-{d})$.", f"${a}x+{a*b}+{c}x-{c*d}$ (1); {P((a+c,'x'),(a*b-c*d,''))} (1).", "1+1") for a, b, c, d in [(2, 5, 3, 1), (4, 3, 2, 6), (5, 2, 4, 3), (3, 7, 6, 2)]]
         + [Q(f"Expand $(x+{a})(x+{b})$.", f"$x^2+{b}x+{a}x+{a*b}$ (1); {P((1,'x^2'),(a+b,'x'),(a*b,''))} (1).", "1+1") for a, b in [(4, 9), (3, 8), (5, 6), (2, 11)]]
         + [Q(f"A two-digit number has tens digit $a$ and ones digit $b$, and $a-b={d}$. Show that the number minus its reverse is {9*d}.", f"$(10a+b)-(10b+a)=9(a-b)$ (1) $=9\\times{d}={9*d}$ (1).", "1+1") for d in [2, 3, 4, 5]])
MED_C = ([Q(f"The sides of a triangle are $({a}x+{b})$ cm, $({c}x+{d})$ cm and $({e}x+{f})$ cm. Find its perimeter, and its value when $x={v}$.", f"Perimeter {P((a+c+e,'x'),(b+d+f,''))} cm (2); for $x={v}$: ${a+c+e}\\times{v}+{b+d+f}={(a+c+e)*v+b+d+f}$ cm (1).", "2+1") for a, b, c, d, e, f, v in [(2, 3, 3, 1, 4, 5, 2), (2, 4, 5, 2, 3, 6, 3), (4, 1, 2, 3, 3, 2, 5), (3, 5, 2, 2, 6, 4, 4), (5, 2, 2, 7, 3, 3, 6), (2, 6, 4, 3, 5, 1, 7)]]
         + [Q(f"If $x+y={s}$ and $xy={p}$, find $x^2+y^2$.", f"$x^2+y^2=(x+y)^2-2xy$ (1) $={s}^2-2\\times{p}$ (1) $={s*s-2*p}$ (1).", "1+1+1") for s, p in [(11, 28), (13, 40), (8, 15), (14, 33), (16, 55), (17, 60)]]
         + [Q(f"Show that the sum of {k} consecutive even numbers starting with $2n$ is ${2*k}n+{k*(k-1)}$ and verify it for $n={v}$.", f"Terms $2n, 2n+2, \dots, 2n+{2*(k-1)}$ (1); sum ${2*k}n+{k*(k-1)}$ (1); for $n={v}$ the numbers add to ${sum(2*v+2*i for i in range(k))}$ and ${2*k*v+k*(k-1)}$ agrees (1).", "1+1+1") for k, v in [(3, 4), (5, 3), (4, 6), (6, 2), (7, 5), (3, 9)]])
MED_D = ([Q(f"Expand and simplify $(x+{a})(x+{b})-x(x+{c})$. Find its value at $x={v}$.", f"$x^2+{a+b}x+{a*b}-x^2-{c}x$ (2); {P((a+b-c,'x'),(a*b,''))} (1); at $x={v}$: ${(a+b-c)*v+a*b}$ (2).", "2+1+2") for a, b, c, v in [(3, 5, 4, 2), (2, 7, 3, 4), (6, 4, 5, 3), (8, 2, 6, 5), (5, 5, 2, 6), (9, 3, 7, 2)]]
          + [Q(f"Think of a two-digit number with digits $a$ and $b$. Add its reverse. Show that the sum is {11}(a+b) and find the sum for the digits {a}, {b}. Is the sum divisible by 11?", f"$(10a+b)+(10b+a)=11a+11b=11(a+b)$ (3); for {a} and {b}: ${11*(a+b)}$ (1); divisible by 11 (1).", "3+1+1") for a, b in [(3, 9), (4, 8), (5, 6), (2, 8), (7, 9), (1, 9)]])

# ================= HARD =================
h1 = [ND(f"A two-digit number exceeds the number formed by reversing its digits by {9*d}. The difference of its digits is:", d, "$9(a-b)=9d$", wrong=[9 * d, d + 1, d - 1, 2 * d]) for d in [2, 4, 5, 6, 7]]
h2 = [ND(f"If $x+\\frac1x={s}$, then $x^2+\\frac1{{x^2}}$ equals:", s * s - 2, "$(x+1/x)^2=x^2+2+1/x^2$", wrong=[s * s, s * s + 2, 2 * s]) for s in [3, 4, 5, 6, 7]]
h3 = [ND(f"The sum of the dates in a $2\\times2$ calendar block is {4*d+16}. The smallest date in the block is:", d, "$4d+16$ = sum", wrong=[d + 1, d + 8, d - 1]) for d in [7, 12, 18, 4, 10]]
h4 = [ND(f"If $a^2-b^2={a*a-b*b}$ and $a-b={a-b}$, then $a+b$ equals:", a + b, "$a^2-b^2=(a-b)(a+b)$", wrong=[a - b, a * b, a + b + 1]) for a, b in [(13, 5), (17, 8), (21, 9), (19, 4), (25, 11)]]
h5 = [ND(f"The value of ${a}^2-{a-3}\\times{a+3}$ is:", 9, "$a^2-(a-3)(a+3)=9$", wrong=[0, 6, a]) for a in [18, 27, 35, 46]]
h6 = [ND(f"The sum of three consecutive integers is {3*n}. The largest of them is:", n + 1, f"Middle integer is ${n}$", wrong=[n, n - 1, n + 2]) for n in [21, 34, 50, 67, 88]]
h7 = [ND(f"A three-digit number with digits $a,b,c$ is reversed. If $a-c={d}$, the difference between the number and its reverse is:", 99 * d, "$(100a+10b+c)-(100c+10b+a)=99(a-c)$", wrong=[9 * d, 90 * d, 100 * d]) for d in [2, 3, 4, 5]]
HARD_A = [h1, h2, h3, h4, h5, h6, h7]
HARD_B = ([Q(f"The sum of the digits of a two-digit number is {s} and the tens digit exceeds the ones digit by {d}. Find the number.", f"$a+b={s}$, $a-b={d}$ (1); $a={(s+d)//2}$, $b={(s-d)//2}$, number ${10*((s+d)//2)+(s-d)//2}$ (1).", "1+1") for s, d in [(9, 3), (11, 5), (13, 1), (8, 4)]]
         + [Q(f"If $x+y={s}$ and $x-y={d}$, find $x^2-y^2$.", f"$x^2-y^2=(x+y)(x-y)$ (1) $={s*d}$ (1).", "1+1") for s, d in [(17, 5), (23, 7), (31, 4), (45, 6)]]
         + [Q(f"Prove that $(n+3)^2-(n-3)^2=12n$ and use it to find the value of $({n}+3)^2-({n}-3)^2$.", f"Identity $(n+3)^2-(n-3)^2=12n$ (1); $=12\\times{n}={12*n}$ (1).", "1+1") for n in [5, 8, 13, 20]])
HARD_C = ([Q(f"The sum of a two-digit number and its reverse is {11*s} and the digits differ by {d}. Find the number (tens digit larger).", f"$11(a+b)={11*s}$ so $a+b={s}$ (1); $a-b={d}$ gives $a={(s+d)//2}$, $b={(s-d)//2}$ (1); number $={10*((s+d)//2)+(s-d)//2}$ (1).", "1+1+1") for s, d in [(10, 4), (12, 2), (14, 2), (8, 2), (16, 2), (9, 3)]]
         + [Q(f"If $x+\\frac1x={s}$, find $x^2+\\frac1{{x^2}}$ and $x^4+\\frac1{{x^4}}$.", f"$x^2+1/x^2={s}^2-2={s*s-2}$ (1); $x^4+1/x^4=({s*s-2})^2-2={(s*s-2)**2-2}$ (2).", "1+2") for s in [3, 4, 5, 6, 7, 8]]
         + [Q(f"The sum of the dates of a $2\\times2$ block in a calendar is {4*d+16}. Find the four dates and show that the block's sum is always $4\\times$(smallest date)$+16$.", f"$4d+16={4*d+16}$ gives $d={d}$ (1); dates {d}, {d+1}, {d+7}, {d+8} (1); sum $=4d+16$ for any $d$ (1).", "1+1+1") for d in [5, 9, 13, 16, 21, 8]])
HARD_D = ([Q(f"Prove that $({a}n+{b})^2-({a}n-{b})^2={4*a*b}n$ and use it to evaluate it for $n={v}$.", f"Using $(p+q)^2-(p-q)^2=4pq$ (2); $4\\times{a}n\\times{b}={4*a*b}n$ (1); for $n={v}$: ${4*a*b*v}$ (2).", "2+1+2") for a, b, v in [(2, 3, 4), (3, 2, 5), (4, 1, 6), (5, 2, 3), (1, 7, 8), (6, 1, 2)]]
          + [Q(f"A three-digit number has digits $a, b, c$ with $a-c={d}$. Show that the number minus its reverse is divisible by 99 and find the difference.", f"$(100a+10b+c)-(100c+10b+a)=99a-99c$ (2); $=99(a-c)=99\\times{d}$ (1); difference $={99*d}$ (2).", "2+1+2") for d in [1, 2, 3, 4, 5, 6]])

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}

from c8m_fix import tidy
tidy(TIERS)
