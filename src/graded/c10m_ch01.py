"""Class 10 Maths Ch 1 - Real Numbers (graded banks)."""
from mg import *

SLUG, NAME, CHNO = "Real_Numbers", "Real Numbers", 1

def hcf(*a):
    r = 0
    for x in a: r = gcd(r, x)
    return r
def lcmm(*a):
    r = 1
    for x in a: r = lcm(r, x)
    return r
def terminates(p, q):
    d = F(p, q).denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    return d == 1
def places(p, q):
    d = F(p, q).denominator; a = b = 0
    while d % 2 == 0: d //= 2; a += 1
    while d % 5 == 0: d //= 5; b += 1
    return max(a, b)
def eu(a, b):
    lines = []; x, y = a, b
    while y:
        lines.append(f"${x}={y}\\times{x//y}+{x%y}$"); x, y = y, x % y
    return "; ".join(lines), x
pf = ftex
def fr(p, q): return f"\\frac{{{p}}}{{{q}}}"

# ---------------- EASY ----------------
eA = [[MN(f"The HCF of {a} and {b} is:", hcf(a, b), why=f"Common prime factors give HCF $={hcf(a,b)}$") for a, b in [(12, 18), (20, 30), (24, 36), (15, 25), (28, 42), (16, 24)]],
      [MN(f"The LCM of {a} and {b} is:", lcmm(a, b), [a * b, hcf(a, b)], f"LCM $=\\dfrac{{{a}\\times{b}}}{{{hcf(a,b)}}}={lcmm(a,b)}$") for a, b in [(4, 6), (6, 9), (8, 12), (10, 15), (12, 16), (14, 21)]],
      [MN(f"The number of prime factors (counted with repetition) of {k} is:", sum(fac(k).values()), why=f"${k}={pf(k)}$") for k in [12, 30, 48, 72, 90]],
      [MS("Which of the following is an irrational number?", f"$\\sqrt{{{k}}}$", [f"$\\sqrt{{{s*s}}}$", f"${s*s}$", f"$\\dfrac{{{s}}}{{{s+3}}}$"], f"${k}$ is not a perfect square, so $\\sqrt{{{k}}}$ is irrational") for k, s in [(7, 5), (11, 6), (13, 7), (15, 4), (17, 8)]],
      [MS(f"The prime factorisation of {k} is:", f"${pf(k)}$", [f"${pf(k+2)}$", f"${pf(k-2)}$", f"${pf(k+4)}$"], f"Divide repeatedly by primes: ${k}={pf(k)}$") for k in [60, 84, 90, 126]],
      [MS(f"The decimal expansion of ${fr(p,q)}$ is:", "terminating" if terminates(p, q) else "non-terminating repeating", ["non-terminating repeating" if terminates(p, q) else "terminating", "non-terminating non-repeating", "an integer"], f"Denominator ${F(p,q).denominator}$: " + ("only 2 and 5 as prime factors" if terminates(p, q) else "has a prime factor other than 2 and 5")) for p, q in [(3, 8), (7, 15), (9, 20), (5, 12)]]]
eB = ([Q(f"Find the HCF of {a} and {b} by prime factorisation.", f"${a}={pf(a)}$, ${b}={pf(b)}$ (1); HCF $={hcf(a,b)}$ (1).", "1+1") for a, b in [(18, 24), (30, 45), (36, 60), (42, 70)]]
      + [Q(f"Express ${a}$ as a product of prime factors.", f"Divide repeatedly by primes (1); ${a}={pf(a)}$ (1).", "1+1") for a in [140, 252, 396, 504]]
      + [Q(f"Without long division, state whether ${fr(p,q)}$ is terminating or non-terminating.", f"${q}={pf(q)}$ (1); " + ("it has only 2 and/or 5, so terminating (1)." if terminates(p, q) else "it has another prime factor, so non-terminating repeating (1)."), "1+1") for p, q in [(11, 16), (13, 30), (17, 125), (19, 21)]])
eC = ([Q(f"Find the LCM and HCF of {a} and {b} by prime factorisation.", f"${a}={pf(a)}$, ${b}={pf(b)}$ (1); HCF $={hcf(a,b)}$ (1); LCM $={lcmm(a,b)}$ (1).", "1+1+1") for a, b in [(26, 91), (96, 404), (72, 108), (60, 84), (45, 75), (54, 90)]]
      + [Q(f"Verify that HCF $\\times$ LCM $=$ product of the numbers for {a} and {b}.", f"HCF $={hcf(a,b)}$, LCM $={lcmm(a,b)}$ (1+1); HCF$\\times$LCM $={hcf(a,b)*lcmm(a,b)}={a}\\times{b}$ (1).", "1+1+1") for a, b in [(12, 30), (14, 35), (18, 48), (20, 50), (24, 40), (28, 70)]]
      + [Q(f"Express ${fr(p,q)}$ as a decimal after checking its type.", f"${q}={pf(q)}$ (1); " + ("terminating (1); " if terminates(p, q) else "non-terminating repeating (1); ") + f"value $\\approx{d2(p/q,4)}$ (1).", "1+1+1") for p, q in [(3, 16), (7, 25), (9, 40), (2, 3), (5, 6), (4, 9)]])
eD = ([Q(f"Find the HCF and LCM of {a} and {b} by prime factorisation and verify that HCF $\times$ LCM $=$ product.", f"${a}={pf(a)}$, ${b}={pf(b)}$ (2); HCF $={hcf(a,b)}$ (1); LCM $={lcmm(a,b)}$ (1); ${hcf(a,b)}\times{lcmm(a,b)}={a*b}$ verified (1).", "2+1+1+1") for a, b in [(135, 225), (196, 280), (867, 255), (240, 360), (306, 408), (420, 588)]]
      + [Q(f"Find the LCM and HCF of {a}, {b} and {c} using prime factorisation.", f"${a}={pf(a)}$, ${b}={pf(b)}$, ${c}={pf(c)}$ (3); HCF $={hcf(a,b,c)}$ (1); LCM $={lcmm(a,b,c)}$ (1).", "3+1+1") for a, b, c in [(12, 18, 24), (20, 30, 45), (16, 40, 56), (15, 21, 35), (18, 27, 36), (24, 36, 60)]])

# ---------------- NCERT ----------------
nA = [[MS(f"The exponent of {p} in the prime factorisation of {k} is:", str(fac(k)[p]), [str(fac(k)[p] + 1), str(fac(k)[p] + 2), str(fac(k)[p] + 3)], f"${k}={pf(k)}$") for k, p in [(2250, 3), (3600, 5), (1176, 7), (4320, 2), (2646, 3)]],
      [MN(f"If HCF({a}, {b}) = {hcf(a,b)}, then LCM({a}, {b}) is:", lcmm(a, b), [a * b, hcf(a, b) * a, a + b], f"LCM $=\\dfrac{{{a}\\times{b}}}{{{hcf(a,b)}}}$") for a, b in [(306, 657), (510, 92), (336, 54), (144, 198), (95, 152)]],
      [MS(f"The product of a non-zero rational and an irrational number such as ${a}\\sqrt{{{p}}}$ is:", "always irrational", ["always rational", "sometimes rational", "always an integer"], "If it were rational, dividing by the rational would make the irrational rational") for a, p in [(2, 3), (3, 5), (5, 2), (4, 7), (6, 11)]],
      [MS(f"The decimal expansion of ${fr(p,q)}$ terminates after how many places of decimals?", str(places(p, q)), [str(places(p, q) + 1), str(places(p, q) + 2), str(places(p, q) + 3)], f"${q}={pf(q)}$; the number of places is the larger of the powers of 2 and 5") for p, q in [(13, 3125), (17, 8), (23, 200), (15, 1600), (29, 80)]],
      [MS("Which of the following is irrational?", f"$\\sqrt{{{k}}}+{s}$", [f"$\\sqrt{{{s*s}}}+{s}$", f"$\\sqrt{{{k*k}}}-{s}$", f"${s}\\times\\sqrt{{{s*s}}}$"], "Rational + irrational is irrational") for k, s in [(5, 3), (7, 2), (3, 4), (11, 5), (2, 6)]],
      [MS(f"For which of the following is $n$ such that ${a}^n$ ends with the digit 0?", "no natural number $n$", ["$n=2$ only", "every $n$", "only even $n$"], f"${a}={pf(a)}$ lacks the prime factor " + ("5" if a % 5 else "2")) for a in [3, 7, 9, 21, 27]],
      [MN(f"The exponent of 2 in the prime factorisation of {k} is:", fac(k).get(2, 0), [fac(k).get(2, 0) + 1, fac(k).get(2, 0) + 2, fac(k).get(2, 0) + 3], f"${k}={pf(k)}$") for k in [480, 1344, 2400, 3584, 4160]]]
nB = ([Q(f"Check whether ${a}^n$ can end with the digit 0 for any natural number $n$.", f"${a}={pf(a)}$ has " + ("no factor 5" if a % 5 else "no factor 2") + f" (1); so ${a}^n$ never ends in 0 (1).", "1+1") for a in [6, 14, 21, 35]]
      + [Q(f"Given that HCF({a},{b})={hcf(a,b)}, find LCM({a},{b}).", f"LCM $=\\dfrac{{{a}\\times{b}}}{{{hcf(a,b)}}}$ (1) $={lcmm(a,b)}$ (1).", "1+1") for a, b in [(306, 657), (336, 54), (510, 92), (144, 198)]]
      + [Q(f"Explain why ${a}\\times{b}+{a}$ is a composite number.", f"${a}\\times{b}+{a}={a}({b}+1)$ (1) has factors {a} and {b+1}, other than 1 and itself (1).", "1+1") for a, b in [(7, 6), (7, 11), (5, 9), (3, 8)]])
nC = ([Q(f"Prove that $\\sqrt{{{p}}}$ is irrational.", f"Assume $\\sqrt{{{p}}}=a/b$ in lowest terms, $b\\ne0$ (1); then ${p}b^2=a^2$, so ${p}\\mid a^2$ hence ${p}\\mid a$ (1); put $a={p}c$: $b^2={p}c^2$ so ${p}\\mid b$ - contradicts coprime (1).", "1+1+1") for p in [2, 3, 5, 7, 11, 13]]
      + [Q(f"Show that ${a}+{b}\\sqrt{{{p}}}$ is irrational, given that $\\sqrt{{{p}}}$ is irrational.", f"Assume ${a}+{b}\\sqrt{{{p}}}=r$ rational (1); then $\\sqrt{{{p}}}=\\dfrac{{r-{a}}}{{{b}}}$ is rational (1) - contradiction; so it is irrational (1).", "1+1+1") for a, b, p in [(3, 2, 5), (2, 3, 7), (5, 4, 3), (7, 1, 2), (4, 5, 11), (6, 2, 13)]]
      + [Q(f"Find the HCF and LCM of {a} and {b} by prime factorisation and verify HCF $\\times$ LCM $=$ product.", f"${a}={pf(a)}$, ${b}={pf(b)}$ (1); HCF $={hcf(a,b)}$, LCM $={lcmm(a,b)}$ (1); ${hcf(a,b)}\\times{lcmm(a,b)}={a*b}$ verified (1).", "1+1+1") for a, b in [(26, 91), (510, 92), (336, 54), (144, 198), (306, 657), (95, 152)]])
nD = ([Q(f"Prove that $\\sqrt{{{p}}}$ is irrational.", f"Assume $\\sqrt{{{p}}}=a/b$, with $a,b$ coprime integers, $b\\ne0$ (1); squaring, ${p}b^2=a^2$, so ${p}\\mid a^2$ and hence ${p}\\mid a$ (1); write $a={p}c$: $b^2={p}c^2$, so ${p}\\mid b$ (1); then ${p}$ is a common factor of $a$ and $b$, contradicting coprimality (1); so $\\sqrt{{{p}}}$ is irrational (1).", "1+1+1+1+1") for p in [17, 19, 23, 29, 31, 37]]
      + [Q(f"A sweet seller has {a} kg of kaju barfi and {b} kg of badam barfi. She packs them into trays of the same weight, each tray holding one kind only. Find the maximum weight of a tray and the number of trays.", f"Maximum weight $=$ HCF$({a},{b})={hcf(a,b)}$ kg (3); trays $=\dfrac{{{a}}}{{{hcf(a,b)}}}+\dfrac{{{b}}}{{{hcf(a,b)}}}={a//hcf(a,b)}+{b//hcf(a,b)}={(a+b)//hcf(a,b)}$ (2).", "3+2") for a, b in [(420, 130), (300, 175), (252, 180)]]
      + [Q(f"Prove that $\\sqrt{{{p}}}$ is irrational and hence that ${a}-{b}\\sqrt{{{p}}}$ is irrational.", f"Assume $\\sqrt{{{p}}}=x/y$, coprime (1); ${p}y^2=x^2\\Rightarrow {p}|x$, $x={p}c$, ${p}|y$ - contradiction (2); if ${a}-{b}\\sqrt{{{p}}}=r$ were rational then $\\sqrt{{{p}}}=({a}-r)/{b}$ would be rational - contradiction (2).", "1+2+2") for p, a, b in [(3, 5, 2), (5, 3, 4), (7, 2, 3)]])

# ---------------- MEDIUM ----------------
mA = [[MN(f"The HCF of {a}, {b} and {c} is:", hcf(a, b, c), why="Take the lowest powers of common primes") for a, b, c in [(24, 36, 60), (45, 75, 90), (56, 84, 140), (72, 108, 180), (42, 63, 105)]],
      [MN(f"The LCM of {a}, {b} and {c} is:", lcmm(a, b, c), [lcmm(a, b), a * b * c // 10], "Take the highest powers of all primes") for a, b, c in [(6, 8, 12), (10, 15, 20), (9, 12, 18), (12, 15, 20), (14, 21, 28)]],
      [MN(f"The largest number that divides {a} and {b} leaving remainders {r1} and {r2} respectively is:", hcf(a - r1, b - r2), why=f"HCF of ${a-r1}$ and ${b-r2}$") for a, b, r1, r2 in [(70, 125, 5, 8), (58, 98, 3, 2), (110, 170, 5, 2), (86, 133, 2, 7), (97, 172, 7, 7)]],
      [MN(f"The least number which when divided by {a}, {b} and {c} leaves remainder {r} each time is:", lcmm(a, b, c) + r, [lcmm(a, b, c), lcmm(a, b, c) - r], "LCM $+$ remainder") for a, b, c, r in [(6, 8, 12, 3), (4, 6, 10, 2), (9, 12, 15, 4), (5, 10, 15, 1), (8, 12, 20, 5)]],
      [MS(f"The decimal expansion of ${fr(p,q)}$ is:", "terminating" if terminates(p, q) else "non-terminating repeating", ["non-terminating repeating" if terminates(p, q) else "terminating", "non-terminating non-repeating", "an integer"], f"${q}={pf(q)}$") for p, q in [(77, 210), (129, 78125 * 4), (35, 50), (13, 75), (87, 160)]],
      [MS(f"If $\\sqrt{{{k}}}$ is irrational, then $\\sqrt{{{k}}}\\times\\sqrt{{{k}}}$ is:", "rational", ["irrational", "non-terminating non-repeating", "not defined"], f"$\\sqrt{{{k}}}\\times\\sqrt{{{k}}}={k}$") for k in [3, 5, 7, 11, 13]]]
mB = ([Q(f"Find the largest number which divides {a} and {b} leaving remainders {r1} and {r2} respectively.", f"Numbers exactly divisible: ${a-r1}$, ${b-r2}$ (1); HCF $={hcf(a-r1,b-r2)}$ (1).", "1+1") for a, b, r1, r2 in [(245, 1029, 5, 5), (398, 436, 7, 11), (615, 963, 3, 6), (1251, 9377, 1, 2)]]
      + [Q(f"Find the smallest number which leaves remainder {r} when divided by {a}, {b} and {c}.", f"LCM$({a},{b},{c})={lcmm(a,b,c)}$ (1); number $={lcmm(a,b,c)}+{r}={lcmm(a,b,c)+r}$ (1).", "1+1") for a, b, c, r in [(12, 16, 18, 5), (15, 20, 25, 6), (14, 21, 35, 3), (8, 18, 24, 7)]]
      + [Q(f"Without actual division, find how many decimal places ${fr(p,q)}$ has.", f"${q}={pf(q)}$ (1); places $=\\max$ of the powers of 2 and 5 $={places(p,q)}$ (1).", "1+1") for p, q in [(23, 200), (7, 32), (31, 625), (9, 500)]])
mC = ([Q(f"The HCF of two numbers is {h} and their LCM is {l}. If one number is {a}, find the other.", f"HCF $\\times$ LCM $=$ product of numbers (1); other $=\\dfrac{{{h}\\times{l}}}{{{a}}}$ (1) $={h*l//a}$ (1).", "1+1+1") for h, l, a in [(9, 360, 72), (12, 504, 84), (8, 240, 48), (15, 450, 90), (6, 396, 66), (14, 420, 70)]]
      + [Q(f"Three bells toll at intervals of {a}, {b} and {c} minutes. If they toll together at 8:00 a.m., after how many minutes will they next toll together?", f"Required time $=$ LCM$({a},{b},{c})$ (1); ${a}={pf(a)}$, ${b}={pf(b)}$, ${c}={pf(c)}$ (1); LCM $={lcmm(a,b,c)}$ minutes (1).", "1+1+1") for a, b, c in [(12, 15, 18), (6, 10, 14), (8, 20, 30), (9, 12, 21), (10, 16, 24), (14, 18, 21)]]
      + [Q(f"Show that $({a}+{b}\\sqrt{{{p}}})({a}-{b}\\sqrt{{{p}}})$ is rational but ${a}+{b}\\sqrt{{{p}}}$ is irrational.", f"Product $={a}^2-{b*b}\\times{p}={a*a-b*b*p}$ is rational (2); ${a}+{b}\\sqrt{{{p}}}$ is irrational as sum of rational and irrational (1).", "2+1") for a, b, p in [(5, 2, 3), (7, 3, 2), (6, 1, 5), (8, 2, 7), (9, 3, 5), (4, 1, 11)]])
mD = ([Q(f"Two tankers contain {a} litres and {b} litres of fuel. Find the maximum capacity of a container that measures both exactly. How many measures does each tanker need?", f"Capacity $=$ HCF$({a},{b})={hcf(a,b)}$ L (3); measures ${a//hcf(a,b)}$ and ${b//hcf(a,b)}$ (2).", "3+2") for a, b in [(850, 680), (612, 918), (420, 546), (360, 504), (468, 624), (720, 960)]]
      + [Q(f"A rectangular courtyard is {a} m by {b} m. Find the side of the largest square tile that fits exactly, and the number of tiles.", f"Side $=$ HCF$({a},{b})={hcf(a,b)}$ m (2); tiles $=\\dfrac{{{a}\\times{b}}}{{{hcf(a,b)**2}}}={a*b//hcf(a,b)**2}$ (3).", "2+3") for a, b in [(24, 16), (45, 30), (72, 48), (96, 60), (84, 56), (90, 54)]])

# ---------------- HARD ----------------
hA = [[MN(f"The LCM of {a}, {b} and {c} is:", lcmm(a, b, c), [a * b, lcmm(a, b) * c // 2], f"Highest powers of ${pf(a)}$, ${pf(b)}$, ${pf(c)}$") for a, b, c in [(30, 42, 66), (36, 48, 72), (45, 60, 75), (52, 78, 104), (28, 42, 63)]],
      [MN(f"The least number that is divisible by every number from 1 to {k} is:", lcmm(*range(1, k + 1)), [lcmm(*range(1, k)), factorial(k) // 2], f"LCM of 1 to {k}") for k in [6, 7, 8, 9, 10]],
      [MN(f"The largest number dividing {a}, {b} and {c} leaving remainder {r} in each case is:", hcf(a - r, b - r, c - r), why="HCF of the differences from the remainder") for a, b, c, r in [(67, 103, 175, 4), (75, 123, 195, 3), (85, 145, 205, 5), (113, 197, 281, 1), (59, 101, 143, 3)]],
      [MN(f"When the odd number {a} is squared and divided by 8, the remainder is:", a * a % 8, [0, 2, 3], f"${a}^2={a*a}$; for odd $n$, $n^2$ leaves remainder 1 on division by 8") for a in [11, 13, 15, 17, 19]],
      [MS("Which of these is a rational number?", f"$\\dfrac{{\\sqrt{{{a*a*3}}}}}{{\\sqrt{{3}}}}$", [f"$\\sqrt{{{a}}}+\\sqrt{{{a+1}}}$", f"${a}\\sqrt{{{a+3}}}$", f"$\\sqrt{{{a+2}}}$"], f"$\\sqrt{{{a*a*3}}}/\\sqrt3={a}$") for a in [2, 5, 6, 7, 10]],
      [MS(f"A number ends with exactly {z} zeros if its prime factorisation (other factor 3) is:", f"$2^{z+1}\\times5^{z}\\times 3$", [f"$2^{z-1}\\times5^{z}\\times3$", f"$2^{z+1}\\times5^{z-1}\\times3$", f"$3^{z}\\times7$"], "Zeros at the end = min(power of 2, power of 5)") for z in [2, 3, 4, 5, 6]]]
hB = ([Q(f"Two numbers have HCF {h} and are in the ratio ${m}:{nn}$. Find the numbers and their LCM.", f"Numbers are ${h}\\times{m}={h*m}$ and ${h}\\times{nn}={h*nn}$ (1); LCM $={h*m*nn}$ (1).", "1+1") for h, m, nn in [(12, 3, 5), (15, 4, 7), (9, 5, 8), (18, 2, 7)]]
      + [Q(f"Find the smallest positive integer that leaves remainders {r1} and {r2} when divided by {a} and {b} respectively.", f"Each remainder is short of the divisor by {a-r1} (1); LCM$({a},{b})={lcmm(a,b)}$, number $={lcmm(a,b)}-{a-r1}={lcmm(a,b)-(a-r1)}$ (1).", "1+1") for a, b, r1, r2 in [(12, 18, 7, 13), (15, 20, 11, 16), (10, 14, 4, 8), (16, 24, 9, 17)]]
      + [Q(f"Prove that ${a}\\sqrt{{{p}}}$ is irrational, given that $\\sqrt{{{p}}}$ is irrational.", f"If ${a}\\sqrt{{{p}}}=r$ were rational, $\\sqrt{{{p}}}=r/{a}$ would be rational (1) - a contradiction (1).", "1+1") for a, p in [(3, 7), (5, 2), (4, 11), (6, 3)]])
hC = ([Q(f"A, B and C take {a}, {b} and {c} minutes per round of a circular track. They start together. After how many minutes do they meet at the start again, and how many rounds has each completed?", f"LCM$({a},{b},{c})={lcmm(a,b,c)}$ min (2); rounds ${lcmm(a,b,c)//a}$, ${lcmm(a,b,c)//b}$, ${lcmm(a,b,c)//c}$ (1).", "2+1") for a, b, c in [(18, 24, 36), (20, 28, 35), (15, 40, 60), (16, 24, 30), (22, 33, 44), (14, 35, 49)]]
      + [Q(f"Find the greatest number that divides {a} and {b} leaving remainder {r} in each case.", f"Required number $=$ HCF$({a-r},{b-r})$ (1); HCF$({a-r},{b-r})={hcf(a-r,b-r)}$ (2).", "1+2") for a, b, r in [(1251, 9377, 1), (1020, 1632, 4), (945, 1393, 5), (2041, 2457, 7), (1815, 2415, 3), (3011, 3431, 11)]]
      + [Q(f"Is ${k}\\times{k+1}\\times{k+2}+{k+2}$ a composite number? Justify.", f"Take {k+2} common: ${k+2}({k}\\times{k+1}+1)$ (2); ${k}\\times{k+1}+1={k*(k+1)+1}>1$, so there are two factors greater than 1 (1); composite.", "2+1") for k in [5, 6, 7, 8, 9, 10]])
hD = ([Q(f"Three sets of English, Hindi and Mathematics books have {a}, {b} and {c} books. They are stacked so that each stack has the same number of books of one subject and all stacks have the same height. Find the minimum number of stacks.", f"Books per stack $=$ HCF$({a},{b},{c})={hcf(a,b,c)}$ (3); stacks $=\\dfrac{{{a+b+c}}}{{{hcf(a,b,c)}}}={(a+b+c)//hcf(a,b,c)}$ (2).", "3+2") for a, b, c in [(96, 240, 336), (144, 192, 288), (120, 180, 300), (168, 252, 420), (90, 150, 210), (108, 162, 270)]]
      + [Q(f"Prove that $\\dfrac{{1}}{{\\sqrt{{{p}}}}}$ is irrational and hence that $\\dfrac{{{a}}}{{\\sqrt{{{p}}}}}$ is irrational.", f"If $1/\\sqrt{{{p}}}=r$ were rational then $\\sqrt{{{p}}}=1/r$ would be rational - contradiction (3); $\\dfrac{{{a}}}{{\\sqrt{{{p}}}}}={a}\\times\\dfrac{{1}}{{\\sqrt{{{p}}}}}$ is a non-zero rational times an irrational, hence irrational (2).", "3+2") for p, a in [(2, 3), (3, 5), (5, 7), (7, 4), (11, 2), (13, 6)]])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
