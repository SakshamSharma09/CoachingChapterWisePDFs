"""Class 9 Maths Ch 9 - Propositions and their Converses (if-then form, converse, counterexample, simple proofs)."""
from g9m import *

SLUG, NAME, CHNO = "Propositions_and_Converses", "Propositions and their Converses", 9

# true propositions "If P, then Q": (P, Q, converse_is_true, counterexample for the converse)
TP = [
    ("a number is divisible by 6", "it is divisible by 3", False, "$9$ is divisible by 3 but not by 6"),
    ("a number is divisible by 10", "its ones digit is 0", True, ""),
    ("a quadrilateral is a square", "it is a rectangle", False, "a $4$ cm by $6$ cm rectangle is not a square"),
    ("a quadrilateral is a rhombus", "its diagonals are perpendicular", False, "a kite that is not a rhombus has perpendicular diagonals"),
    ("a triangle is equilateral", "it is isosceles", False, "a triangle with sides $5, 5, 8$ is isosceles but not equilateral"),
    ("two lines are parallel", "the alternate interior angles made by a transversal are equal", True, ""),
    ("a number is a multiple of 4", "it is even", False, "$6$ is even but not a multiple of 4"),
    ("$x=3$", "$x^2=9$", False, "$x=-3$ gives $x^2=9$ but $x\\ne3$"),
    ("a number ends in 5", "it is divisible by 5", False, "$10$ is divisible by 5 but does not end in 5"),
    ("a number is prime and greater than 2", "it is odd", False, "$9$ is odd but not prime"),
    ("a triangle is right-angled", "the square of its longest side equals the sum of the squares of the other two sides", True, ""),
    ("a parallelogram is a rectangle", "its diagonals are equal", True, ""),
    ("a number is a perfect square", "it has an odd number of factors", True, ""),
    ("a triangle has two equal angles", "the sides opposite those angles are equal", True, ""),
    ("an integer $n$ is even", "$n^2$ is even", True, ""),
    ("two angles are vertically opposite", "the two angles are equal", False, "two angles of $60^\\circ$ in an equilateral triangle are equal but not vertically opposite"),
    ("a number is divisible by 9", "the sum of its digits is divisible by 9", True, ""),
    ("a number is a multiple of 8", "it is a multiple of 4", False, "$12$ is a multiple of 4 but not of 8"),
    ("an integer $n$ is odd", "$n^2$ is odd", True, ""),
    ("a number is a multiple of 15", "it is a multiple of 5", False, "$20$ is a multiple of 5 but not of 15"),
    ("a number is divisible by 12", "it is divisible by 4", False, "$8$ is divisible by 4 but not by 12"),
    ("a triangle is equilateral", "all its angles are $60^\\circ$", True, ""),
]
# false propositions: (statement, counterexample, three options that are NOT counterexamples, working)
FP = [
    ("The sum of two prime numbers is even", "$2$ and $3$", ["$3$ and $5$", "$5$ and $7$", "$7$ and $11$"], "$2+3=5$ is odd"),
    ("Every prime number is odd", "$2$", ["$3$", "$5$", "$7$"], "$2$ is prime and even"),
    ("If $a<b$, then $a^2<b^2$", "$a=-3,\\ b=2$", ["$a=1,\\ b=4$", "$a=2,\\ b=5$", "$a=3,\\ b=6$"], "$a^2=9>b^2=4$"),
    ("$n^2+n+41$ is prime for every natural number $n$", "$n=40$", ["$n=5$", "$n=10$", "$n=20$"], "$1600+40+41=1681=41^2$"),
    ("Every odd number is prime", "$9$", ["$7$", "$11$", "$13$"], "$9=3\\times3$"),
    ("If $x^2>9$, then $x>3$", "$x=-4$", ["$x=5$", "$x=6$", "$x=10$"], "$16>9$ but $-4<3$"),
    ("The product of two irrational numbers is irrational", "$\\sqrt2\\times\\sqrt2$", ["$\\sqrt2\\times1$", "$\\sqrt3\\times\\sqrt5\\ $ (irrational product $\\sqrt{15}$)", "$\\sqrt2\\times\\sqrt7\\ $ (irrational product $\\sqrt{14}$)"], "$\\sqrt2\\times\\sqrt2=2$ is rational"),
    ("Every multiple of 3 is odd", "$6$", ["$3$", "$9$", "$15$"], "$6$ is even"),
    ("If a number is divisible by 4 and by 6, then it is divisible by 24", "$12$", ["$24$", "$48$", "$72$"], "$12$ is divisible by 4 and 6 but not by 24"),
    ("$2n+1$ is prime for every natural number $n$", "$n=4$", ["$n=1$", "$n=2$", "$n=3$"], "$2(4)+1=9=3\\times3$"),
    ("$n^2-n+11$ is prime for all natural numbers $n$", "$n=11$", ["$n=2$", "$n=5$", "$n=8$"], "$121-11+11=121=11^2$"),
    ("The sum of two irrational numbers is irrational", "$\\sqrt2$ and $-\\sqrt2$", ["$\\sqrt2$ and $\\sqrt3$", "$\\sqrt5$ and $\\sqrt7$", "$\\sqrt3$ and $\\sqrt{11}$"], "$\\sqrt2+(-\\sqrt2)=0$ is rational"),
    ("The difference of two primes is prime", "$11$ and $3$", ["$7$ and $2$", "$5$ and $2$", "$13$ and $2$"], "$11-3=8$"),
    ("If $n$ is prime, then $2n+1$ is prime", "$n=7$", ["$n=2$", "$n=3$", "$n=5$"], "$2(7)+1=15=3\\times5$"),
    ("Every quadrilateral with equal diagonals is a rectangle", "an isosceles trapezium", ["a rectangle", "a square", "a $3$ cm by $5$ cm rectangle"], "An isosceles trapezium has equal diagonals but is not a rectangle"),
    ("If $x>y$, then $x^2>y^2$", "$x=-1,\\ y=-4$", ["$x=5,\\ y=2$", "$x=6,\\ y=1$", "$x=8,\\ y=3$"], "$1<16$"),
    ("A number divisible by 3 and by 9 must be divisible by 27", "$18$", ["$27$", "$54$", "$81$"], "$18$ is divisible by 3 and 9, not 27"),
]

CONV = [
    "If a number is divisible by 3, then it is divisible by 6.", "If the ones digit of a number is 0, then the number is divisible by 10.",
    "If a quadrilateral is a rectangle, then it is a square.", "If the diagonals of a quadrilateral are perpendicular, then it is a rhombus.",
    "If a triangle is isosceles, then it is equilateral.", "If the alternate interior angles made by a transversal are equal, then the two lines are parallel.",
    "If a number is even, then it is a multiple of 4.", "If $x^2=9$, then $x=3$.", "If a number is divisible by 5, then it ends in 5.",
    "If a number is odd, then it is prime and greater than 2.", "If the square of the longest side of a triangle equals the sum of the squares of the other two sides, then the triangle is right-angled.",
    "If the diagonals of a parallelogram are equal, then it is a rectangle.", "If a number has an odd number of factors, then it is a perfect square.",
    "If two sides of a triangle are equal, then the angles opposite them are equal.", "If $n^2$ is even, then the integer $n$ is even.",
    "If two angles are equal, then they are vertically opposite.", "If the sum of the digits of a number is divisible by 9, then the number is divisible by 9.",
    "If a number is a multiple of 4, then it is a multiple of 8.", "If $n^2$ is odd, then the integer $n$ is odd.", "If a number is a multiple of 5, then it is a multiple of 15.",
    "If a number is divisible by 4, then it is divisible by 12.", "If all angles of a triangle are $60^\\circ$, then the triangle is equilateral."]
assert len(CONV) == len(TP)
def qt(i): return f"If {TP[i][0]}, then {TP[i][1]}."
def qs(i): return f"If {TP[i][0]}, then {TP[i][1]}"

def tick(x): return f"${x}$"

def factors(n): return sum(1 for d in range(1, n + 1) if n % d == 0)

def first_fail(k, sg=1):  # smallest natural n with n^2 + sg*n + k composite
    for n in range(1, 200):
        v = n * n + sg * n + k
        if v > 3 and any(v % p == 0 for p in range(2, isqrt(v) + 1)): return n, v

# ---- MCQ builders ----
def a_conv(i):
    P, Q_, _, _ = TP[i]
    return M4(f"The converse of the proposition “If {P}, then {Q_}” is:", CONV[i], [qt(i), f"If it is not true that {P}, then it is not true that {Q_}.", f"If it is not true that {Q_}, then {P}."], "Interchange the hypothesis and the conclusion.")
def a_cvt(i):
    P, Q_, t, cex = TP[i]
    c = "True" if t else "False"
    w = ["False" if t else "True", "True only for some values", "It cannot be decided"]
    return M4(f"The proposition “If {P}, then {Q_}” is true. Its converse “If {Q_}, then {P}” is:", c, w, ("The converse holds." if t else f"Counterexample: {cex}."))
def a_hyp(i):
    P, Q_, _, _ = TP[i]
    return M4(f"In “If {P}, then {Q_}”, the hypothesis is:", P, [Q_, f"it is not true that {P}", f"{P}, then {Q_}"], "The part after ‘if’ is the hypothesis.")
def a_con(i):
    P, Q_, _, _ = TP[i]
    return M4(f"In “If {P}, then {Q_}”, the conclusion is:", Q_, [P, f"it is not true that {Q_}", f"{P}, then {Q_}"], "The part after ‘then’ is the conclusion.")
def a_cex(i):
    s_, c, w, why = FP[i]
    return M4(f"Which of the following is a counterexample to the statement “{s_}”?", c, w, why + ".")
def a_fac(n):
    f = factors(n); sq = isqrt(n) ** 2 == n
    return nn(f"The number of factors of ${n}$ is:", f, f"List the factors of ${n}$ in pairs; the count is {f} ({'odd, so ' + str(n) + ' is a perfect square' if sq else 'even, so ' + str(n) + ' is not a perfect square'}).", offs=(1, -1, 2, -2, 3))
def a_pyth(a, b, c):
    ok = a * a + b * b == c * c
    return M4(f"A triangle has sides ${a}$ cm, ${b}$ cm and ${c}$ cm. Using the converse of the Baudhāyana–Pythagoras theorem, the triangle is:", "right-angled" if ok else "not right-angled", ["not right-angled" if ok else "right-angled", "equilateral", "isosceles"], f"${a}^2+{b}^2={a*a+b*b}$ and ${c}^2={c*c}$.")
def expr(k, sg): return f"n^2{'+' if sg > 0 else '-'}n+{k}"
def a_fail(k, sg=1):
    n, v = first_fail(k, sg)
    return nn(f"For the expression ${expr(k, sg)}$, the smallest natural number $n$ for which the value is NOT prime is:", n, f"$n={n}$ gives ${v}$, which is composite.", offs=(1, -1, 2, 3, 5), pos=True)
def a_sq_odd(lo, hi):
    c = [n for n in range(lo, hi) if isqrt(n) ** 2 == n][0]
    w = [n for n in range(lo, hi) if isqrt(n) ** 2 != n][:3]
    return M4(f"Which of the following numbers has an odd number of factors?", str(c), [str(x) for x in (w[0], w[1] + 3, w[2] + 5) if isqrt(x) ** 2 != x][:3], f"Only a perfect square has an odd number of factors; ${c}={isqrt(c)}^2$.")

# =============================== EASY ===============================
e1 = [a_hyp(i) for i in (1, 5, 11, 14)]
e2 = [a_con(i) for i in (1, 2, 5, 18)]
e3 = [M4(f"The statement “{s_}” is:", "false", ["true", "true only for even numbers", "true only for prime numbers"], f"Counterexample: {c}. {w}.") for (s_, c, _, w) in [(FP[1][0], FP[1][1], 0, FP[1][3]), (FP[4][0], FP[4][1], 0, FP[4][3]), (FP[7][0], FP[7][1], 0, FP[7][3]), (FP[0][0], FP[0][1], 0, FP[0][3])]]
e4 = [M4(f"“{u}” can be written in if–then form as:", f"If {p}, then {q}.", [f"If {q}, then {p}.", f"If not ({p}), then {q}.", f"{p.capitalize()} or {q}."], "Subject becomes the hypothesis.") for u, p, q in [("Every square is a rectangle", "a figure is a square", "it is a rectangle"), ("All multiples of 10 end in 0", "a number is a multiple of 10", "it ends in 0"), ("Every equilateral triangle is isosceles", "a triangle is equilateral", "it is isosceles"), ("Every multiple of 6 is even", "a number is a multiple of 6", "it is even")]]
e5 = [a_fac(n) for n in (9, 12, 16, 20)]
e6 = [a_conv(i) for i in (17, 19, 20, 12)]
e7 = [M4(f"Which of the following numbers is divisible by 9?", str(c), [str(x) for x in w], f"Digit sum of ${c}$ is ${sum(map(int, str(c)))}$, a multiple of 9.") for c, w in [(729, (730, 725, 731)), (4536, (4537, 4530, 4533)), (810, (811, 812, 815)), (3627, (3628, 3625, 3620))]]
e8 = [a_cvt(i) for i in (1, 5, 11, 14)]
EASY_A = [e1, e2, e3, e4, e5, e6, e7, e8]

def conv_ans(i):
    P, Q_, t, cex = TP[i]
    return (f"Converse: {CONV[i]} (1); " + ("it is true (1)." if t else f"it is false, counterexample: {cex} (1)."))
def Bconv(i): return Q(f"Write the converse of “If {TP[i][0]}, then {TP[i][1]}”. Is it true?", conv_ans(i), "1+1")
EASY_B = ([Bconv(i) for i in (1, 5, 10, 14)]
          + [Q(f"Write “{u}” in if–then form and name the hypothesis.", f"If {p}, then {q} (1); hypothesis: {p} (1).", "1+1") for u, p, q in [("A square has four equal sides", "a figure is a square", "it has four equal sides"), ("Multiples of 5 end in 0 or 5", "a number is a multiple of 5", "it ends in 0 or 5"), ("A rhombus is a parallelogram", "a quadrilateral is a rhombus", "it is a parallelogram"), ("Even numbers are divisible by 2", "a number is even", "it is divisible by 2")]]
          + [Q(f"Find the number of factors of ${n}$. Is ${n}$ a perfect square?", f"Factors: {', '.join(str(d) for d in range(1, n + 1) if n % d == 0)} (1); total {factors(n)}; {'odd, so it is a perfect square' if isqrt(n)**2 == n else 'even, so it is not a perfect square'} (1).", "1+1") for n in (9, 15, 25, 18)])
def Cc(i):
    P, Q_, tr, cex = TP[i]
    if tr:
        return QQ(f"Write the converse of “If {P}, then {Q_}”. Is the converse true? Justify.", f"Converse: {CONV[i]}", "The converse is also true", "Both the proposition and its converse hold, so we may write the two as a single ‘if and only if’ statement")
    return QQ(f"Write the converse of “If {P}, then {Q_}”. Is the converse true? Justify.", f"Converse: {CONV[i]}", f"Counterexample: {cex}", "It satisfies the hypothesis of the converse but not its conclusion, so the converse is false")
def Ccex(i): return QQ(f"Show that the statement “{FP[i][0]}” is false by giving a counterexample.", "A false statement needs only one counterexample", f"Take {FP[i][1]}", f"{FP[i][3]}, so the statement is false")
EASY_C = ([Cc(i) for i in (3, 6, 8, 9, 15, 16)]
          + [Ccex(i) for i in (5, 8, 9, 10, 11, 12)]
          + [QQ(f"Is a triangle with sides ${a}$ cm, ${b}$ cm and ${c}$ cm right-angled? Use the converse of the Baudhāyana–Pythagoras theorem.", f"${a}^2+{b}^2={a*a}+{b*b}={a*a+b*b}$", f"${c}^2={c*c}$", "Right-angled" if a*a + b*b == c*c else "Not right-angled, as the two values differ") for a, b, c in [(6, 8, 10), (5, 12, 14), (8, 15, 17), (7, 24, 26), (9, 12, 16), (20, 21, 29)]])
def parity(a, b): return QQ(f"Verify with ${a}$ and ${b}$ that the sum of two odd numbers is even, and then prove it for any two odd numbers.", f"${a}+{b}={a+b}$, which is even", "Let the numbers be $2m+1$ and $2n+1$", "Sum $=2m+2n+2=2(m+n+1)$", "A multiple of 2, so even")
EASY_D = ([parity(a, b) for a, b in [(3, 5), (7, 11), (9, 13), (15, 21), (17, 9), (23, 5)]]
          + [QQ(f"Prove that the product of two consecutive integers is even. Verify it for ${n}$ and ${n+1}$.", f"${n}\\times{n+1}={n*(n+1)}$, even", "Of two consecutive integers one is even", "So the product has the factor 2", "Hence even") for n in (6, 9, 13, 14, 17, 22)])

# =============================== NCERT ===============================
n1 = [a_conv(i) for i in (0, 2, 3, 6)]
n2 = [a_cvt(i) for i in (0, 2, 3, 6)]
n3 = [a_cex(i) for i in (2, 3, 5, 6)]
n4 = [a_fac(n) for n in (36, 48, 49, 100)]
n5 = [a_pyth(*t) for t in [(9, 40, 41), (10, 24, 26), (11, 60, 62), (12, 35, 37)]]
n6 = [a_fail(k) for k in (11, 17, 5, 41)]
n7 = [M4(q, c, w, why) for q, c, w, why in [
    ("A proposition that is false can be shown to be false by giving:", "a counterexample", ["many examples that satisfy it", "its converse", "a definition"], "One counterexample is enough."),
    ("Many examples that satisfy a statement:", "do not prove it for all cases", ["prove it for all cases", "show it is false", "prove its converse"], "Examples are not proofs."),
    ("If a proposition and its converse are both true, we write:", "P if and only if Q", ["P only", "not P", "P or Q only"], "Both directions hold."),
    ("The converse of a true proposition is:", "may or may not be true", ["always true", "always false", "never a proposition"], "It must be checked separately.")]]
n8 = [a_sq_odd(lo, hi) for lo, hi in [(20, 50), (50, 90), (30, 70), (90, 140)]]
NCERT_A = [n1, n2, n3, n4, n5, n6, n7, n8]
NCERT_B = ([Bconv(i) for i in (0, 2, 4, 9)]
           + [Q(f"Give a counterexample to the statement “{FP[i][0]}”.", f"Take {FP[i][1]} (1); {FP[i][3]} (1).", "1+1") for i in (0, 3, 6, 10)]
           + [Q(f"How many factors does ${n}$ have? What does the answer tell you about ${n}$?", f"${n}$ has {factors(n)} factors (1); " + ("odd number, so it is a perfect square (1)." if isqrt(n) ** 2 == n else "even number, so it is not a perfect square (1)."), "1+1") for n in (64, 72, 81, 90)])
NCERT_C = ([Cc(i) for i in (0, 2, 4, 7, 9, 17)]
           + [Ccex(i) for i in (1, 2, 4, 13, 14, 15)]
           + [QQ(f"Use the converse of the Baudhāyana–Pythagoras theorem to decide whether ${a}$ cm, ${b}$ cm, ${c}$ cm are the sides of a right triangle.", f"Longest side ${c}$; ${a}^2+{b}^2={a*a+b*b}$", f"${c}^2={c*c}$", "Right-angled" if a*a + b*b == c*c else "Not right-angled") for a, b, c in [(15, 36, 39), (16, 30, 34), (13, 84, 85), (14, 48, 50), (18, 24, 31), (28, 45, 54)]])
NCERT_D = ([QQ(f"Prove that the sum of any {k} consecutive integers is divisible by {k}. Verify for the numbers starting at ${s0}$.", f"Let the integers be $n, n+1, \\ldots, n+{k-1}$", f"Sum $={k}n+{k*(k-1)//2}={k}(n+{(k-1)//2})$", f"A multiple of ${k}$, proved", f"Check: ${'+'.join(str(s0+j) for j in range(k))}={sum(s0+j for j in range(k))}={k}\\times{sum(s0+j for j in range(k))//k}$") for k, s0 in [(3, 8), (5, 12), (7, 4), (3, 25), (5, 31), (9, 6)]]
           + [QQ(f"Prove that the square of an odd integer is odd and write the converse. Is the converse true? Test it with ${n}$.", "Let the integer be $2m+1$; its square $=4m^2+4m+1=2(2m^2+2m)+1$ is odd", "Converse: if $n^2$ is odd then $n$ is odd", f"For ${n}^2={n*n}$ ({'odd' if n % 2 else 'even'}), $n$ is {'odd' if n % 2 else 'even'}", "If $n$ were even, $n^2$ would be even, so the converse is true") for n in (7, 11, 15, 9, 13, 21)])

# =============================== MEDIUM ===============================
CEXS = [x[3] for x in TP if x[3]]
m1 = [M4(f"The converse of “If {TP[i][0]}, then {TP[i][1]}” is false because:", TP[i][3], [[c for c in CEXS if c != TP[i][3]][k * 3 + 1] for k in (0, 1, 2)], "Counterexample for the converse.") for i in (0, 2, 4, 7)]
m2 = [a_cex(i) for i in (7, 8, 9, 12)]
m3 = [a_fail(101), a_fail(107), a_fail(29, -1), a_fail(59, -1)]
m4 = [a_fac(n) for n in (72, 180, 144, 210)]
m5 = [a_pyth(*t) for t in [(33, 56, 65), (20, 99, 101), (39, 80, 89), (45, 60, 76)]]
m6 = [M4(q, c, w, why) for q, c, w, why in [
    ("Which statement is true for every integer $n$?", "$n(n+1)$ is even", ["$n(n+1)$ is odd", "$n^2$ is even", "$n+1$ is even"], "One of two consecutive integers is even."),
    ("Which statement is true for every integer $n$?", "$n^2+n$ is even", ["$n^2+n$ is odd", "$n^2-1$ is even", "$2n+1$ is even"], "$n^2+n=n(n+1)$."),
    ("Which statement is true for every integer $n$?", "$2n+1$ is odd", ["$2n+1$ is even", "$3n$ is odd", "$n+2$ is even"], "$2n$ is even."),
    ("Which statement is true for every integer $n$?", "$n^3-n$ is divisible by 2", ["$n^3-n$ is odd", "$n^3+n$ is odd", "$n^3$ is even"], "$n^3-n=(n-1)n(n+1)$ has an even factor.")]]
m7 = [nn(f"The sum of the {k} consecutive integers starting from ${s0}$ is:", sum(s0 + j for j in range(k)), f"It equals ${k}\\times{s0+(k-1)//2}$ (number of terms times the middle term).", offs=(k, -k, 1, -1, 5)) for k, s0 in [(5, 17), (7, 23), (3, 41), (9, 12)]]
m8 = [nn(f"The number of integers from 1 to {N} that have an odd number of factors is:", isqrt(N), "Only perfect squares have an odd number of factors.", offs=(1, -1, 2, -2, 5), pos=True) for N in (50, 130, 200, 400)]
MED_A = [m1, m2, m3, m4, m5, m6, m7, m8]
MED_B = ([Q(f"Write the converse of “If {TP[i][0]}, then {TP[i][1]}” and test it.", conv_ans(i), "1+1") for i in (12, 13, 15, 16)]
         + [Q(f"Find the smallest natural number $n$ for which ${expr(k, sg)}$ is not prime, and the value obtained.", f"$n={first_fail(k, sg)[0]}$ (1); value ${first_fail(k, sg)[1]}$ is composite (1).", "1+1") for k, sg in [(5, 1), (11, 1), (3, -1), (5, -1)]]
         + [Q(f"Is the number ${n}$ a perfect square? Decide by counting its factors.", f"{factors(n)} factors (1); {'odd, so a perfect square' if isqrt(n)**2 == n else 'even, so not a perfect square'} (1).", "1+1") for n in (121, 150, 169, 200)])
MED_C = ([Cc(i) for i in (10, 11, 19, 20, 21, 16)]
         + [Ccex(i) for i in (16, 7, 3, 12, 8, 6)]
         + [QQ(f"If $n$ is a multiple of {a}, is $n$ a multiple of {b}? Write the converse and give a counterexample if false.", f"Multiple of {a} is a multiple of {b} as ${a}={b}\\times{a//b}$", f"Converse: if $n$ is a multiple of {b}, then of {a}", f"Counterexample: ${b}$ is a multiple of {b} but not of {a}", "Converse is false") for a, b in [(18, 6), (24, 8), (30, 10), (36, 9), (28, 7), (45, 15)]])
def evsum(k, n): return QQ(f"Prove that the sum of {k} consecutive even numbers starting at $2n$ is a multiple of {2*k}. Check with $n={n}$.", f"Numbers $2n, 2n+2, \\ldots, 2n+{2*(k-1)}$", f"Sum $={2*k}n+{k*(k-1)}={2*k}(n+{(k-1)//2})$", f"For $n={n}$: ${sum(2*n+2*j for j in range(k))}$", f"${sum(2*n+2*j for j in range(k))}={2*k}\\times{sum(2*n+2*j for j in range(k))//(2*k)}$")
MED_D = ([evsum(k, n) for k, n in [(3, 4), (5, 7), (7, 3), (3, 10), (5, 12), (9, 2)]]
         + [QQ(f"Take the two-digit number ${t}$. Subtract the sum of its digits and show that the result is divisible by 9. Prove the same for any two-digit number.", f"${t}-({t//10}+{t%10})={t-t//10-t%10}$", f"${t-t//10-t%10}={(t-t//10-t%10)//9}\\times9$", "General number $10a+b$", "$10a+b-(a+b)=9a$", "A multiple of 9") for t in (47, 63, 85, 92, 38, 71)])

# =============================== HARD ===============================
h1 = [nn(f"The number of perfect squares between ${lo}$ and ${hi}$ (both excluded) is:", len([x for x in range(lo + 1, hi) if isqrt(x) ** 2 == x]), "Squares have an odd number of factors; count the integers whose squares lie in the range.", offs=(1, -1, 2, -2, 3), pos=True) for lo, hi in [(100, 1000), (250, 2500), (400, 3000), (900, 5000)]]
h2 = [a_fail(k, -1) for k in (11, 17, 107, 137)]
h2b = [a_fail(191), a_fail(41, -1), a_fail(149, -1), a_fail(197, -1)]
h3 = [nn(f"The sum of {k} consecutive integers is ${k*m}$. The largest of them is:", m + (k - 1) // 2, f"The middle number is the average, ${m}$.", offs=(1, -1, 2, -2, 3)) for k, m in [(5, 36), (7, 45), (9, 51), (11, 62)]]
h4 = [M4(f"If $n$ is any integer not divisible by 3, then $n^2$ leaves a remainder ___ on division by 3. For ${n}$ this gives:", "1", ["0", "2", "3"], f"${n}^2={n*n}$ and ${n*n}=3\\times{n*n//3}+{n*n%3}$.") for n in (7, 11, 14, 20)]
h5 = [nn(f"For the two-digit number ${t}$, the value of (number − digit sum) ÷ 9 is:", (t - t // 10 - t % 10) // 9, "$10a+b-(a+b)=9a$, so the quotient is the tens digit.", offs=(1, -1, 2, -2, 5)) for t in (83, 56, 94, 67)]
h6 = [nn(f"If the sides of a triangle are ${a}$, ${b}$ and $x$ (with $x$ the longest side) and it is right-angled, then $x$ is:", c, f"$x^2={a}^2+{b}^2={c*c}$.", offs=(1, -1, 2, -2, 5), pos=True) for a, b, c in [(9, 40, 41), (28, 45, 53), (36, 77, 85), (48, 55, 73)]]
h7 = [nn(f"A number has exactly {f} factors if it equals $p^{{{f-1}}}$ for a prime $p$. The smallest such number for $f={f}$ is:", 2 ** (f - 1), "Take $p=2$.", offs=(1, -1, f, 2 * f, 4)) for f in (5, 6, 7, 8)]
h8 = [nn(f"The smallest natural number with exactly {t} factors (counting 1 and itself) is:", [x for x in range(1, 2000) if factors(x) == t][0], "Compare numbers of the form $p^a q^b$.", offs=(1, -2, 4, 6, 12), pos=True) for t in (6, 9, 10, 12)]
HARD_A = [h1, h2, h2b, h3, h4, h5, h6, h8]
def lcm2(a, b): return a * b // gcd(a, b)
HARD_B = ([QQ(f"Use the converse of the Baudhāyana–Pythagoras theorem: for what value of $x$ is a triangle with sides ${a}, {b}, x$ ($x$ the longest) right-angled?", f"$x^2={a}^2+{b}^2={a*a+b*b}$", f"$x={c}$") for a, b, c in [(20, 21, 29), (11, 60, 61), (13, 84, 85), (33, 56, 65)]]
          + [QQ(f"Show that “If a number is divisible by {a} and by {b}, then it is divisible by ${a*b}$” is false. Give a counterexample.", f"Take the LCM ${lcm2(a, b)}$", f"${lcm2(a, b)}$ is divisible by {a} and {b}", f"But ${lcm2(a, b)}$ is not divisible by ${a*b}$") for a, b in [(4, 6), (6, 9), (10, 15), (6, 8)]]
          + [QQ(f"Verify that $n^2-1$ is a multiple of 8 for the odd number $n={n}$. Write the converse of “If $n$ is odd, then $n^2-1$ is a multiple of 8”.", f"${n}^2-1={n*n-1}={8}\\times{(n*n-1)//8}$", "Converse: if $n^2-1$ is a multiple of 8, then $n$ is odd") for n in (11, 15, 19, 25)])
HARD_C = ([QQ(f"Prove that the sum of the squares of two consecutive integers is odd. Verify it for ${n}$ and ${n+1}$.", f"${n}^2+{n+1}^2={n*n}+{(n+1)**2}={n*n+(n+1)**2}$, odd", "General: $n^2+(n+1)^2=2n^2+2n+1$", "$=2(n^2+n)+1$", "Odd") for n in (8, 12, 15, 19, 24, 31)]
          + [QQ(f"Prove: if {a} divides $x$ and $x$ divides $y$, then {a} divides $y$. Verify with $x={a*k}$ and $y={a*k*j}$.", f"$x={a*k}$ is a multiple of {a}", f"$y={a*k*j}={a*k}\\times{j}$", "General: $x=ap$, $y=xq=a(pq)$", "A multiple of the given number") for a, k, j in [(3, 4, 5), (7, 2, 6), (5, 6, 3), (9, 2, 7), (4, 5, 9), (6, 3, 8)]]
          + [QQ(f"For $m={m}$ and $n={n}$ show that $({m*m-n*n},\\ {2*m*n},\\ {m*m+n*n})$ are the sides of a right triangle, using the converse of the Baudhāyana–Pythagoras theorem.", f"${m*m-n*n}^2={(m*m-n*n)**2}$ and ${2*m*n}^2={(2*m*n)**2}$", f"Sum $={(m*m-n*n)**2+(2*m*n)**2}$", f"${m*m+n*n}^2={(m*m+n*n)**2}$ equals the sum", "So the triangle is right-angled") for m, n in [(5, 2), (6, 1), (7, 4), (8, 3), (9, 2), (10, 7)]])
HARD_D = ([QQ(f"Prove that the product of three consecutive integers is divisible by 6. Verify it for ${n}, {n+1}, {n+2}$.", f"${n}\\times{n+1}\\times{n+2}={n*(n+1)*(n+2)}={n*(n+1)*(n+2)//6}\\times6$", "Among three consecutive integers one is a multiple of 3", "At least one is even", "Both factors 2 and 3 present, so divisible by 6") for n in (5, 9, 14, 17, 22, 28)]
          + [QQ(f"Prove that the square of any odd integer is $1$ more than a multiple of $8$. Verify it for ${n}$.", f"${n}^2={n*n}={(n*n-1)//8}\\times8+1$", "Let the odd integer be $2m+1$", "Square $=4m^2+4m+1=4m(m+1)+1$", "$m(m+1)$ is even, so $4m(m+1)$ is a multiple of 8", "Hence $8k+1$") for n in (9, 13, 17, 21, 27, 33)])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
