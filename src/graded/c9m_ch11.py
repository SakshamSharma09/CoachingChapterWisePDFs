"""Class 9 Maths Ch 11 - World of Algorithms (column addition, divisors, gcd by Euclid's subtraction method, mod, tracing procedures)."""
from g9m import *

SLUG, NAME, CHNO = "World_of_Algorithms", "World of Algorithms", 11

# ------------------------- simulators -------------------------
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def carries(a, b):
    sa, sb = str(a)[::-1], str(b)[::-1]; c = 0; out = []
    for i in range(max(len(sa), len(sb))):
        t = (int(sa[i]) if i < len(sa) else 0) + (int(sb[i]) if i < len(sb) else 0) + c
        c = t // 10; out.append(c)
    return out  # carry out of each column
def gcd_sub(m, n):
    """Euclid's subtraction algorithm: (m,n) -> (n, m-n) re-ordered; returns the list of pairs."""
    if m < n: m, n = n, m
    seq = [(m, n)]
    while n != 0:
        d = m - n; m, n = max(n, d), min(n, d); seq.append((m, n))
    return seq
def gcd_div(m, n):
    if m < n: m, n = n, m
    rows = []
    while n:
        rows.append((m, n, m // n, m % n)); m, n = n, m % n
    return rows, m
def pairs_txt(seq): return r"\to".join(f"({a},{b})" for a, b in seq)
def div_txt(rows): return "; ".join(f"${m}={n}\\times{q}+{r}$" for m, n, q, r in rows)
def is_prime(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
def collatz(n):
    c = 0
    while n != 1: n = n // 2 if n % 2 == 0 else 3 * n + 1; c += 1
    return c
def dsum(n): return sum(map(int, str(n)))

# ------------------------- generators -------------------------
def g_carry(lo, hi):
    def f(r):
        a, b = r.randint(lo, hi), r.randint(lo, hi)
        c = carries(a, b); k = sum(1 for i, x in enumerate(c) if x and i < len(c))
        return nn(f"Adding ${a}$ and ${b}$ by the column algorithm, the number of columns in which a carry is generated is:", k, f"Carries out of the columns: {c}.", offs=(1, -1, 2, -2, 3), pos=True)
    return f

def g_sumadd(lo, hi):
    return lambda r: (lambda a, b: nn(f"Using the column addition algorithm, ${a}+{b}$ equals:", a + b, f"Add column by column from the right, carrying 1 when a column sum exceeds 9.", offs=(10, -10, 100, -100, 1, 9)))(r.randint(lo, hi), r.randint(lo, hi))

def g_ndiv(lo, hi):
    def f(r):
        n = r.randint(lo, hi); d = divisors(n)
        return nn(f"The divisor algorithm applied to ${n}$ produces a list with how many entries?", len(d), f"Divisors of ${n}$: {', '.join(map(str, d))}.", offs=(1, -1, 2, -2, 3), pos=True)
    return f

def g_gcdl(lo, hi):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m == n or gcd(m, n) == 1: return None
        g = gcd(m, n)
        return nn(f"The greatest of the common divisors of ${m}$ and ${n}$, found from their divisor lists, is:", g, f"Common divisors: {', '.join(map(str, [d for d in divisors(m) if n % d == 0]))}.", offs=(1, -1, g, 2, -2, 3), pos=True)
    return f

def g_mod(lo, hi):
    def f(r):
        a, b = r.randint(lo, hi), r.randint(3, 12)
        return nn(f"The value of ${a} \\bmod {b}$ (remainder on dividing ${a}$ by ${b}$) is:", a % b, f"${a}={b}\\times{a//b}+{a%b}$.", offs=(1, -1, 2, a // b, b, -2), pos=True)
    return f

def g_gsteps(lo, hi, kind="sub", cap=9):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m <= n or gcd(m, n) == n: return None
        seq = gcd_sub(m, n); k = len(seq) - 1
        if k > cap or k < 3: return None
        return nn(f"Using Euclid's subtraction algorithm for gcd(${m}$, ${n}$), the number of subtraction steps needed is:", k, f"Pairs: ${pairs_txt(seq)}$.", offs=(1, -1, 2, -2, 3), pos=True)
    return f

def g_gval(lo, hi, kind="sub"):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m <= n: return None
        g = gcd(m, n)
        if g == 1 and r.random() < 0.7: return None
        if len(gcd_sub(m, n)) > 16: return None
        return nn(f"By Euclid's algorithm, gcd(${m}$, ${n}$) is:", g, f"Pairs: ${pairs_txt(gcd_sub(m, n))}$.", offs=(1, -1, 2, -2, g, 3), pos=True)
    return f

def g_trace(kind, ar):
    def f(r):
        a = r.randint(*ar)
        if kind == "sum_even":
            n = r.randint(8, 20); v = sum(i for i in range(1, n + 1) if i % 2 == 0)
            return nn(f"Set total = 0. For i = 1, 2, …, {n}: if i is even, add i to total. The final value of total is:", v, f"Sum of even numbers up to {n}.", offs=(1, -1, 2, 10, -10, n))
        if kind == "double":
            k = r.randint(3, 6); c = r.randint(1, 5); x = a
            for _ in range(k): x = 2 * x - c
            return nn(f"Set x = {a}. Repeat {k} times: x = 2x − {c}. The final value of x is:", x, "Apply the rule each time.", offs=(1, -1, 2, -2, c, 10))
        if kind == "mult3":
            n = r.randint(20, 60); v = sum(1 for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)
            return nn(f"A counter starts at 0. For i = 1, 2, …, {n}, the counter increases by 1 whenever i is divisible by 3 or by 5. The final counter value is:", v, f"Multiples of 3: {n//3}; of 5: {n//5}; of both: {n//15}.", offs=(1, -1, 2, -2, 3), pos=True)
        if kind == "digits":
            n = r.randint(1000, 99999); v = dsum(n)
            return nn(f"Set s = 0. While n > 0: add (n mod 10) to s, then replace n by the quotient of n divided by 10. Starting with n = {n}, the final s is:", v, "The algorithm adds the digits.", offs=(1, -1, 2, -2, 9, 3), pos=True)
        if kind == "rev":
            n = r.randint(100, 9999)
            if n % 10 == 0: return None
            rv = int(str(n)[::-1])
            return nn(f"Set r = 0. While n > 0: r = 10r + (n mod 10), then n = quotient of n by 10. Starting with n = {n}, the final r is:", rv, "The algorithm reverses the digits.", offs=(9, -9, 90, 10, -10, 1))
    return f

def g_prime(lo, hi):
    def f(r):
        n = r.randint(lo, hi)
        if not is_prime(n): return None
        return M4(f"To test whether ${n}$ is prime, we check divisibility by 2, 3, 4, … up to $\\lfloor\\sqrt{{{n}}}\\rfloor$. The last number checked is:", str(isqrt(n)), [str(isqrt(n) + 1), str(isqrt(n) - 1), str(n // 2)], f"$\\lfloor\\sqrt{{{n}}}\\rfloor={isqrt(n)}$.")
    return f

def g_lcm(lo, hi):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m == n or gcd(m, n) == 1: return None
        return nn(f"Using gcd(${m}$, ${n}$) $={gcd(m,n)}$, the LCM of ${m}$ and ${n}$ is:", m * n // gcd(m, n), f"LCM $=\\dfrac{{{m}\\times{n}}}{{{gcd(m,n)}}}$.", offs=(gcd(m, n), -gcd(m, n), m, n, 10, -10), pos=True)
    return f

def g_col(lo, hi):
    def f(r):
        n = r.randint(lo, hi); c = collatz(n)
        return nn(f"Start with $n={n}$. Repeat: if $n$ is even replace it by $n/2$, otherwise by $3n+1$. The number of steps needed to reach 1 is:", c, "Trace the sequence step by step.", offs=(1, -1, 2, -2, 3, 5), pos=True)
    return f

def g_pcount(lo, hi):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m <= n or gcd(m, n) == n: return None
        seq = gcd_sub(m, n); k = len(seq) - 1
        if k < 4 or k > 13: return None
        return nn(f"Euclid's subtraction algorithm is applied to find gcd(${m}$, ${n}$). The number of subtractions performed (until a pair with 0 appears) is:", k, f"Pairs: ${pairs_txt(seq)}$.", offs=(1, -1, 2, -2, 3), pos=True)
    return f

DEFS = [tx(q, c, w, why) for q, c, w, why in [
    ("An algorithm is best described as:", "a step-by-step procedure that solves a problem", ["a single formula", "a diagram only", "a guess"], "Definition."),
    ("The word ‘algorithm’ comes from the name of:", "Al-Khwārizmī", ["Euclid", "Pythagoras", "Brahmagupta"], "Origin of the word."),
    ("In the column algorithm for addition, a carry is generated when a column sum is:", "greater than 9", ["less than 9", "exactly 0", "an even number"], "Digit would not fit in one place."),
    ("The remainder when 29 is divided by 6 is written:", "$29 \\bmod 6 = 5$", ["$29 \\bmod 6 = 4$", "$29 \\bmod 6 = 6$", "$29 \\bmod 6 = 0$"], "$29=6\\times4+5$."),
    ("Euclid's observation used in the gcd algorithm is that gcd(m, n) equals:", "gcd(n, m − n) for $m\\ge n$", ["gcd(m, m + n)", "gcd(m × n, n)", "m − n"], "Common divisors divide the difference."),
    ("The gcd algorithm stops when:", "one of the numbers becomes 0", ["both numbers are equal to 1 always", "the numbers are odd", "the sum is 10"], "gcd(g, 0) = g."),
    ("Which of these must be true of every step of an algorithm?", "it is clear and unambiguous", ["it can be skipped", "it depends on luck", "it is different each time"], "Algorithms must be precise."),
    ("An algorithm that never stops for some input:", "is not a valid algorithm for that problem", ["is always the fastest", "gives the correct output", "needs no steps"], "It must terminate.")]]

DEFS2 = [tx(q, c, w, why) for q, c, w, why in [
    ("In the divisor algorithm for $n$, the numbers $j$ that are checked are:", "$1, 2, \\ldots, n$", ["only the primes up to $n$", "only the even numbers up to $n$", "$2, 3, \\ldots, n-1$ only"], "Every $j$ from 1 to $n$ is tested."),
    ("gcd(48, 0) equals:", "48", ["0", "1", "24"], "gcd(g, 0) = g."),
    ("In Euclid's subtraction algorithm, the pair $(m, n)$ with $m\\ge n$ is replaced by:", "the numbers $n$ and $m-n$", ["$(m+n,\\ n)$", "$(m,\\ n+1)$", "$(n,\\ m\\times n)$"], "Replace by the smaller number and the difference."),
    ("Every algorithm has input, output and:", "a finite sequence of well-defined steps", ["an unlimited number of steps", "random choices", "no stopping rule"], "Finiteness.")]]

# =============================== EASY ===============================
EASY_A = [draw(100, 4, g_sumadd(120, 480)), draw(101, 4, g_ndiv(6, 30)), draw(102, 4, g_mod(20, 90)), draw(103, 4, g_gcdl(8, 36)), DEFS[:4], draw(104, 4, g_trace("sum_even", (1, 2))), DEFS[4:], draw(105, 4, g_carry(10, 99))]
def q_sumadd(lo, hi):
    def f(r):
        a, b = r.randint(lo, hi), r.randint(lo, hi); c = carries(a, b)
        return QQ(f"Add ${a}$ and ${b}$ using the column algorithm. State in which columns a carry is produced.", f"Add from the units column, carry 1 when a column sum exceeds 9", "Columns with a carry: " + (", ".join(["units", "tens", "hundreds", "thousands"][i] for i, x in enumerate(c) if x and i < 4) or "none"), f"${a}+{b}={a+b}$")
    return f
def q_divl(lo, hi):
    def f(r):
        n = r.randint(lo, hi); d = divisors(n)
        return QQ(f"Run the divisor algorithm for {n}: check j = 1, 2, …, {n}. Write the list of divisors and say how many numbers are checked.", f"Check each $j$ from 1 to {n}: {n} numbers are checked", f"List $=[{', '.join(map(str, d))}]$", f"It has {len(d)} entries")
    return f
def q_modl(lo, hi):
    def f(r):
        a, b = r.randint(lo, hi), r.randint(3, 12)
        return QQ(f"Find ${a} \\bmod {b}$ and ${a+b} \\bmod {b}$. What do you notice?", f"${a}={b}\\times{a//b}+{a%b}$, so remainder ${a%b}$", f"${a+b}={b}\\times{a//b+1}+{a%b}$, so remainder ${a%b}$", "Adding the divisor does not change the remainder")
    return f
def q_gcdl(lo, hi):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m == n or gcd(m, n) == 1: return None
        cm = [d for d in divisors(m) if n % d == 0]
        return QQ(f"Find gcd({m}, {n}) by listing the divisors of both numbers.", f"divisors({m}) $=[{', '.join(map(str, divisors(m)))}]$", f"divisors({n}) $=[{', '.join(map(str, divisors(n)))}]$", f"Common divisors $=[{', '.join(map(str, cm))}]$, greatest is ${gcd(m, n)}$")
    return f
def q_gsub(lo, hi, cap=8):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m <= n or gcd(m, n) == n: return None
        seq = gcd_sub(m, n)
        if not 3 <= len(seq) - 1 <= cap: return None
        return QQ(f"Apply Euclid's subtraction algorithm to find gcd({m}, {n}). Write the sequence of pairs and count the subtractions.", "Replace $(m,n)$ by $(n, m-n)$ re-ordered so the larger is first", f"${pairs_txt(seq)}$", f"{len(seq)-1} subtractions, gcd $={gcd(m, n)}$")
    return f
def q_gdiv(lo, hi): return q_gsub(lo, hi, 9)
EASY_B = draw(110, 4, q_sumadd(120, 480)) + draw(111, 4, q_divl(8, 28)) + draw(112, 4, q_modl(20, 90))
EASY_C = draw(113, 6, q_gcdl(10, 40)) + draw(114, 6, q_gsub(24, 60, 7)) + draw(115, 6, q_sumadd(1200, 9800))
def q_sumeven(r):
    n = r.randint(6, 14); ev = [i for i in range(1, n + 1) if i % 2 == 0]
    return QQ(f"Trace this procedure: total = 0; for i = 1 to {n}, if i is even add i to total. Write the values added and the final total.", f"Even values: {', '.join(map(str, ev))}", f"Total $={'+'.join(map(str, ev))}$", f"Final total $={sum(ev)}$")
EASY_D = draw(116, 6, q_sumeven) + draw(117, 6, q_gcdl(40, 100))

# =============================== NCERT ===============================
NCERT_A = [draw(200, 4, g_carry(1000, 9999)), draw(201, 4, g_ndiv(36, 100)), draw(202, 4, g_gval(30, 120, "sub")), draw(203, 4, g_mod(100, 400)),
           DEFS2, draw(204, 4, g_gsteps(40, 120, "sub")), draw(205, 4, g_trace("double", (2, 9))), draw(206, 4, g_gval(60, 200, "div"))]
NCERT_B = draw(210, 4, q_gsub(30, 80)) + draw(211, 4, q_gdiv(40, 120)) + draw(212, 4, q_divl(30, 60))
NCERT_C = draw(213, 6, q_gsub(60, 150)) + draw(214, 6, q_gdiv(80, 200)) + draw(215, 6, q_sumadd(2500, 9999))
def q_trace_double(lo, hi):
    def f(r):
        a = r.randint(lo, hi); k = r.randint(3, 5); c = r.randint(1, 5); x = a; vals = [a]
        for _ in range(k): x = 2 * x - c; vals.append(x)
        return QQ(f"Trace: x = {a}; repeat {k} times: x = 2x − {c}. Write the value of x after each repetition and the final value.", f"Rule: new $x=2x-{c}$", "Values: " + ", ".join(map(str, vals)), f"Final $x={x}$")
    return f
def q_digits(r):
    n = r.randint(1000, 9999); ds = [int(c) for c in str(n)[::-1]]
    return QQ(f"Trace: s = 0; while n > 0, add (n mod 10) to s and replace n by its quotient on division by 10. Start with n = {n}. Write the digits picked and the final s.", "Digits picked (from the right): " + ", ".join(map(str, ds)), f"Sum $={'+'.join(map(str, ds))}$", f"Final $s={sum(ds)}$ (the digit sum)")
NCERT_D = draw(216, 6, q_trace_double(2, 9)) + draw(217, 6, q_digits)

# =============================== MEDIUM ===============================
MED_A = [draw(300, 4, g_gsteps(150, 400, "sub")), draw(301, 4, g_gsteps(150, 500, "div")), draw(302, 4, g_trace("mult3", (1, 2))), draw(303, 4, g_trace("digits", (1, 2))),
         draw(304, 4, g_lcm(12, 60)), draw(305, 4, g_prime(50, 400)), draw(306, 4, g_pcount(100, 600)), draw(307, 4, g_gval(200, 900, "div"))]
def q_lcm(lo, hi):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m <= n or gcd(m, n) == 1 or gcd(m, n) == n: return None
        seq = gcd_sub(m, n)
        if len(seq) - 1 > 12: return None
        g = gcd(m, n)
        return QQ(f"Find the gcd of {m} and {n} by Euclid's subtraction algorithm and use it to find their LCM.", f"${pairs_txt(seq)}$", f"gcd $={g}$", f"LCM $=\\dfrac{{{m}\\times{n}}}{{{g}}}={m*n//g}$")
    return f
def q_prime(lo, hi):
    def f(r):
        n = r.randint(lo, hi); ps = [d for d in range(2, isqrt(n) + 1) if n % d == 0]
        return QQ(f"To test whether {n} is prime, check divisibility by 2, 3, … up to $\\lfloor\\sqrt{{{n}}}\\rfloor$. Carry out the test and give the conclusion.", f"$\\lfloor\\sqrt{{{n}}}\\rfloor={isqrt(n)}$, so check $2,\\ldots,{isqrt(n)}$", (f"The smallest divisor found is ${ps[0]}$ since ${n}={ps[0]}\\times{n//ps[0]}$" if ps else "No number in this range divides it"), f"{n} is {'composite' if ps else 'prime'}")
    return f
MED_B = draw(310, 4, q_lcm(36, 150)) + draw(311, 4, q_prime(101, 200)) + draw(312, 4, q_gsub(90, 250))
def q_cmp(lo, hi):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m <= n or gcd(m, n) == n: return None
        s_ = len(gcd_sub(m, n)) - 1
        if s_ < 3 or s_ > 9: return None
        g = gcd(m, n)
        return QQ(f"Find gcd({m}, {n}) in two ways: (i) by listing the divisors of both numbers, (ii) by Euclid's subtraction algorithm. Check that the answers agree.", f"divisors({m}) $={divisors(m)}$, divisors({n}) $={divisors(n)}$", f"Greatest common divisor from the lists $={g}$", f"Subtraction: ${pairs_txt(gcd_sub(m, n))}$, {s_} subtractions", f"gcd $={g}$ by both methods")
    return f
def q_mult(r):
    n = r.randint(20, 40); a = n // 3; b = n // 5; c = n // 15
    return QQ(f"A counter starts at 0 and for i = 1, 2, …, {n} increases by 1 whenever i is a multiple of 3 or of 5. Find the final count without listing everything.", f"Multiples of 3: {a}; multiples of 5: {b}", f"Multiples of both (counted twice): {c}", f"Count $={a}+{b}-{c}={a+b-c}$")
MED_C = draw(313, 6, q_cmp(40, 120)) + draw(314, 6, q_mult) + draw(315, 6, q_trace_double(10, 30))
def q_rev(r):
    n = r.randint(1000, 9999)
    if n % 10 == 0: return None
    ds = [int(c) for c in str(n)[::-1]]; rv = 0; steps = []
    for d_ in ds: rv = 10 * rv + d_; steps.append(rv)
    return QQ(f"Trace: r = 0; while n > 0: r = 10r + (n mod 10), then n = quotient of n by 10. Start with n = {n}. List r after each pass and say what the procedure does.", "Values of $r$: " + ", ".join(map(str, steps)), f"Final $r={rv}$", "It reverses the digits")
def q_col(lo, hi):
  def f(r):
    n = r.randint(lo, hi); seq = [n]
    while seq[-1] != 1: x = seq[-1]; seq.append(x // 2 if x % 2 == 0 else 3 * x + 1)
    return QQ(f"Start with n = {n}. Repeat: if n is even replace it by n/2, otherwise by 3n + 1, until n = 1. Write the sequence and the number of steps.", "Sequence: " + ", ".join(map(str, seq)), f"Number of steps $={len(seq)-1}$")
  return f
MED_D = draw(316, 6, q_rev) + draw(317, 6, q_col(6, 12))

# =============================== HARD ===============================
HARD_A = [draw(400, 4, g_col(7, 40)), draw(401, 4, g_gsteps(500, 2000, "sub", 14)), draw(402, 4, g_gsteps(300, 1500, "sub", 13)), draw(403, 4, g_trace("rev", (1, 2))),
          draw(404, 4, g_lcm(60, 300)), draw(405, 4, g_prime(500, 3000)), draw(406, 4, g_trace("mult3", (1, 2))), draw(407, 4, g_gval(900, 5000, "div"))]
def q_hard_gcd3(lo, hi):
    def f(r):
        a, b, c = r.randint(lo, hi), r.randint(lo, hi), r.randint(lo, hi)
        g1 = gcd(a, b); g = gcd(g1, c)
        if g == 1 or len({a, b, c}) < 3 or g1 == c or g1 == min(a, b) or len(gcd_sub(max(a, b), min(a, b))) > 12 or len(gcd_sub(max(g1, c), min(g1, c))) > 12: return None
        return QQ(f"Find the gcd of {a}, {b} and {c} by applying Euclid's subtraction algorithm twice: first to two numbers and then to the result and the third.", f"gcd({a}, {b}): ${pairs_txt(gcd_sub(max(a, b), min(a, b)))}$ giving ${g1}$", f"gcd({g1}, {c}): ${pairs_txt(gcd_sub(max(g1, c), min(g1, c)))}$", f"gcd of the three numbers $={g}$")
    return f
def q_grid(lo, hi):
    def f(r):
        a, b = r.randint(lo, hi), r.randint(lo, hi)
        if a == b or gcd(a, b) < 4 or gcd(a, b) == min(a, b): return None
        g = gcd(a, b)
        if len(gcd_sub(max(a, b), min(a, b))) > 12: return None
        return QQ(f"A floor of {a} cm by {b} cm is to be covered by identical square tiles, as large as possible, with no cutting. Use Euclid's subtraction algorithm to find the tile side and the number of tiles.", f"Tile side $=\\gcd({a},{b})$", f"${pairs_txt(gcd_sub(max(a, b), min(a, b)))}$", f"Side ${g}$ cm", f"Number of tiles $=\\dfrac{{{a}\\times{b}}}{{{g}^2}}={a*b//g**2}$")
    return f
HARD_B = draw(410, 4, q_hard_gcd3(100, 600)) + draw(411, 4, q_grid(100, 500)) + draw(412, 4, q_lcm(100, 400))
def q_nested(r):
    n = r.randint(4, 12)
    cnt = sum(1 for i in range(1, n + 1) for j in range(i, n + 1))
    s_ = sum(i * j for i in range(1, n + 1) for j in range(1, i + 1))
    return QQ(f"Trace: count = 0; for i = 1 to {n}: for j = i to {n}: count = count + 1. Find the final count and explain the pattern.", f"For $i=1$ the inner loop runs {n} times, for $i=2$ it runs {n-1} times, and so on", f"Count $={n}+{n-1}+\\cdots+1=\\frac{{{n}\\times{n+1}}}2$", f"Count $={cnt}$")
def q_sumsq(r):
    n = r.randint(5, 12); k = r.randint(2, 4)
    tot = sum(i * i for i in range(1, n + 1) if i % k == 0)
    ts = [i * i for i in range(1, n + 1) if i % k == 0]
    return QQ(f"Trace: total = 0; for i = 1 to {n}: if i is a multiple of {k}, add i² to total. List the numbers added and the final total.", "Squares added: " + ", ".join(map(str, ts)), f"Total $={'+'.join(map(str, ts))}$", f"Final total $={tot}$")
HARD_C = draw(413, 6, q_nested) + draw(414, 6, q_sumsq) + draw(415, 6, q_col(13, 30))
def q_chain(lo, hi):
    def f(r):
        m, n = r.randint(lo, hi), r.randint(lo, hi)
        if m <= n or gcd(m, n) < 6 or gcd(m, n) == n: return None
        seq = gcd_sub(m, n)
        if len(seq) - 1 > 12: return None
        g = gcd(m, n); dv = divisors(g)
        return QQ(f"Find the largest number that divides both {m} and {n} exactly, using Euclid's subtraction algorithm. Hence list all the common divisors of the two numbers.", f"${pairs_txt(seq)}$", f"Largest common divisor $=\\gcd={g}$", f"Every common divisor divides {g}", f"Common divisors: {', '.join(map(str, dv))}")
    return f
HARD_D = draw(416, 6, q_chain(120, 700)) + draw(417, 6, q_hard_gcd3(150, 900))

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
