"""Class 6 Maths Ch 5 - Prime Time."""
from g67 import *

SLUG, NAME, CHNO = "Prime_Time", "Prime Time", 5

def factors(n): return [d for d in range(1, n + 1) if n % d == 0]
def nf(n):
    r = 1
    for e in fac(n).values(): r *= e + 1
    return r
def primes_between(a, b): return [p for p in range(a, b + 1) if isprime(p)]
def comps(p, k=3):
    out = []; x = p + 1
    while len(out) < k:
        if not isprime(x): out.append(x)
        x += 1
    return out
def prime_q(p): return tm("Which of the following is a prime number?", str(p), [str(c) for c in comps(p)], f"{p} has only two factors, 1 and {p}.")
def comp_q(c):
    ps = [p for p in range(c - 8, c + 9) if isprime(p) and p != c][:3]
    return tm("Which of the following is a composite number?", str(c), [str(p) for p in ps], f"{c} has more than two factors.")
def L(xs): return ", ".join(map(str, xs))
def pf(n): return " \\times ".join(str(p) for p, e in sorted(fac(n).items()) for _ in range(e))
def hcf(a, b): return gcd(a, b)
def ncomp(n): return n - 1 - len([p for p in range(2, n + 1) if isprime(p)])

# ---------- EASY ----------
eA1 = [prime_q(p) for p in [13, 29, 37, 53, 71]]
eA2 = [comp_q(c) for c in [27, 49, 51, 63, 91]]
eA3 = [nm(f"The number of factors of {n} is:", nf(n), f"Factors: {L(factors(n))}.", offs=(1, -1, 2, 3)) for n in [12, 18, 20, 28, 30]]
eA4 = [nm(f"The {k}th multiple of {n} is:", n * k, f"${n}\\times{k}$", offs=(n, -n, 1, 2 * n)) for n, k in [(7, 6), (9, 8), (12, 5), (15, 7), (11, 9)]]
eA5 = [tm(f"Which of these numbers is divisible by {d}?", str(d * k), [str(d * k + 1), str(d * k + 2), str(d * k - 1)], f"Divisibility test of {d}.") for d, k in [(3, 121), (5, 87), (9, 63), (2, 45), (10, 52)]]
eA6 = [nm(f"The sum of the first {k} prime numbers is:", sum(primes_between(1, 100)[:k]), "Add the primes 2, 3, 5, 7, ...", offs=(1, -1, 2, 5, 10)) for k in [3, 4, 5, 6]]
eA7 = [tm(q, a, w, "Definition") for q, a, w in [("The smallest prime number is:", "2", ["1", "3", "0"]), ("The only even prime number is:", "2", ["4", "6", "0"]), ("The number 1 is:", "neither prime nor composite", ["prime", "composite", "even prime"])]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([QQ(f"List all the factors of {n}.", f"Find pairs whose product is {n}", f"Factors: {L(factors(n))}") for n in [16, 24, 35, 42]]
          + [QQ(f"Write the first five multiples of {n}.", f"Multiply {n} by 1, 2, 3, 4, 5", L([n * k for k in range(1, 6)])) for n in [6, 8, 13, 17]]
          + [QQ(f"Is {n} prime or composite? Give a reason.", f"Factors of {n}: {L(factors(n))}", "Prime: only two factors" if isprime(n) else "Composite: more than two factors") for n in [31, 39, 57, 61]])
EASY_C = ([QQ(f"Find the prime factorisation of {n}.", f"Divide by primes in turn", f"${n}={pf(n)}$", "Only prime factors appear") for n in [36, 48, 60, 72, 84, 90]]
          + [QQ(f"Using divisibility rules, check whether {n} is divisible by 2, 3 and 5.", f"By 2: {'yes' if n%2==0 else 'no'} (last digit {n%10})", f"By 3: {'yes' if ds(n)%3==0 else 'no'} (digit sum {ds(n)})", f"By 5: {'yes' if n%5==0 else 'no'}") for n in [135, 246, 330, 411, 520, 765]]
          + [QQ(f"Write all prime numbers between {a} and {b}.", "Test each number for factors", L(primes_between(a, b))) for a, b in [(10, 30), (30, 50), (50, 70), (70, 90), (20, 40), (40, 60)]])
EASY_D = ([QQ(f"Find the prime factors of {a} and {b}. Write the common prime factors.", f"${a}={pf(a)}$", f"${b}={pf(b)}$", f"Common prime factors: {L(sorted(set(fac(a)) & set(fac(b))) or ['none'])}") for a, b in [(12, 18), (20, 30), (28, 42), (15, 35), (24, 40), (45, 60)]]
          + [QQ(f"Find all the factors of {n}. How many are there? Is {n} a perfect number (sum of factors other than itself equals the number)? Also check whether {n} is even.", f"Factors: {L(factors(n))}", f"Count $={nf(n)}$", f"Sum of factors except {n} $={sum(factors(n))-n}$", "Perfect" if sum(factors(n)) - n == n else "Not perfect", "Even" if n % 2 == 0 else "Odd") for n in [28, 30, 36, 45, 50, 56]])

# ---------- NCERT ----------
nA1 = [tm(f"Which of the following is divisible by {d}?", str(v), [str(v + a) for a in (1, 2, 3)], f"Apply the divisibility rule of {d}.") for d, v in [(4, 3516), (8, 5128), (6, 4218), (11, 2728), (4, 7924), (8, 6040)]]
nA2 = [tm(f"Which pair is a pair of co-prime numbers?", f"{a} and {b}", [f"{c} and {d}" for c, d in cp_wrong], "Co-prime numbers have no common factor other than 1.") for a, b, cp_wrong in [(8, 15, [(6, 9), (12, 18), (10, 25)]), (14, 25, [(14, 21), (9, 15), (16, 24)]), (9, 28, [(12, 20), (15, 30), (9, 21)]), (21, 22, [(21, 28), (24, 36), (14, 35)])]]
nA3 = [tm(f"Which of these is a pair of twin primes?", f"{p} and {p+2}", [f"{q} and {q+2}" for q in [x for x in range(p + 1, 200) if not (isprime(x) and isprime(x + 2))][:3]], "Twin primes are primes that differ by 2.") for p in [11, 17, 29, 41, 59]]
nA4 = [nm(f"The number of prime numbers between {a} and {b} is:", len(primes_between(a + 1, b - 1)), "Check each number.", offs=(1, -1, 2, 3)) for a, b in [(10, 30), (20, 50), (40, 70), (60, 100), (5, 25)]]
nA5 = [nm(f"The prime factorisation of {n} has how many prime factors (counting repeats)?", sum(fac(n).values()), f"${n}={pf(n)}$", offs=(1, -1, 2, 3)) for n in [72, 120, 144, 210, 360]]
nA6 = [tm(f"Using the Sieve of Eratosthenes, which is the first prime whose multiples we cross out after crossing multiples of 2?", "3", ["4", "5", "1"], "The next un-crossed number after 2 is 3.")] + [nm(f"In the Sieve of Eratosthenes up to {n}, we need to cross out multiples of primes up to:", max(p for p in range(2, n) if isprime(p) and p * p <= n), "Primes $p$ with $p\\times p\\le n$.", offs=(2, -2, 1, 4)) for n in [50, 100, 150]]
nA7 = [nm(f"The smallest prime number that is a factor of {n} is:", min(fac(n)), "Test 2, 3, 5, 7, ...", offs=(2, 4, 6, 1)) for n in [105, 143, 221, 391]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Test whether {n} is divisible by 4 and by 8.", f"Last two digits {n%100} give {'divisible' if n%100%4==0 else 'not divisible'} by 4", f"Last three digits {n%1000}: {'divisible' if n%1000%8==0 else 'not divisible'} by 8") for n in [3216, 7424, 5348, 9136]]
           + [QQ(f"Write two prime numbers whose sum is {n}.", f"Try prime pairs", f"{[p for p in range(2,n) if isprime(p) and isprime(n-p)][0]} + {n-[p for p in range(2,n) if isprime(p) and isprime(n-p)][0]} = {n}") for n in [24, 36, 48, 56]]
           + [QQ(f"Are {a} and {b} co-prime? Give the reason.", f"Factors of {a}: {L(factors(a))}; of {b}: {L(factors(b))}", "Co-prime (only common factor is 1)" if gcd(a, b) == 1 else f"Not co-prime (common factor {gcd(a,b)})") for a, b in [(14, 15), (18, 27), (25, 36), (21, 49)]])
NCERT_C = ([QQ(f"Use the divisibility test for 11 to check whether {n} is divisible by 11.", f"Sum of digits at odd places and even places", f"Difference $={abs(sum(int(c) for c in str(n)[::2])-sum(int(c) for c in str(n)[1::2]))}$", "Divisible by 11" if n % 11 == 0 else "Not divisible by 11") for n in [2728, 5412, 3849, 6094, 8173, 9625]]
           + [QQ(f"Draw a factor tree (describe) for {n} and write its prime factorisation.", "Split the number into two factors repeatedly", f"${n}={pf(n)}$", f"Product check: ${n}$") for n in [96, 108, 126, 150, 198, 240]]
           + [QQ(f"Find the first {k} common multiples of {a} and {b}.", f"LCM $={lcm(a,b)}$", f"Common multiples: {L([lcm(a,b)*i for i in range(1,k+1)])}", "Each is a multiple of the LCM") for a, b, k in [(4, 6, 4), (6, 8, 3), (5, 10, 4), (9, 12, 3), (3, 7, 3), (8, 12, 3)]])
NCERT_D = ([QQ(f"Find all prime numbers between {a} and {b} using the Sieve of Eratosthenes idea. State which primes you cross out multiples of.", f"Cross out multiples of 2, 3, 5, 7", f"Primes: {L(primes_between(a, b))}", f"Number of primes $={len(primes_between(a,b))}$", "Check by testing factors") for a, b in [(1, 40), (41, 80), (60, 100), (1, 30), (31, 70), (50, 90)]]
           + [QQ(f"A number is divisible by both {a} and {b}. Show that it is divisible by {a*b} when {a} and {b} are co-prime. Give an example with {a*b*k}.", f"{a} and {b} have no common factor", f"Example: {a*b*k}$\\div{a}={a*b*k//a}$ and $\\div{b}={a*b*k//b}$", f"${a*b*k}\\div{a*b}={k}$", "So both factors divide it and their product also divides") for a, b, k in [(3, 4, 5), (4, 5, 7), (5, 6, 3), (3, 8, 4), (7, 9, 2), (5, 8, 6)]])

# ---------- MEDIUM ----------
mA1 = [nm(f"The number of factors of {n} is:", nf(n), f"${n}={ftex(n)}$; use $(e_1+1)(e_2+1)\\ldots$", offs=(1, -1, 2, 3)) for n in [48, 54, 72, 100, 120]]
mA2 = [nm(f"The HCF of {a} and {b} is:", gcd(a, b), "Highest common factor.", offs=(1, -1, 2, gcd(a, b))) for a, b in [(36, 48), (45, 75), (56, 84), (63, 91), (54, 90)]]
mA3 = [nm(f"The LCM of {a} and {b} is:", lcm(a, b), "Lowest common multiple.", offs=(a, -a, b, gcd(a, b))) for a, b in [(12, 18), (8, 20), (15, 25), (14, 35), (16, 24)]]
mA4 = [nm(f"The smallest digit to put in the blank to make {str(n)[:-1]}_ divisible by 3 is:", (-ds(n // 10)) % 3, "Digit sum must be a multiple of 3.", offs=(3, 1, 2, 6, 9)) for n in [4521, 7632, 8195, 3647]]
mA5 = [nm(f"The largest 3-digit multiple of {n} is:", 999 // n * n, "Divide 999 by the number.", offs=(n, -n, 1, 2 * n)) for n in [7, 13, 17, 23]]
mA6 = [nm(f"How many prime numbers are there between {a} and {b}?", len(primes_between(a + 1, b - 1)), "Count them carefully.", offs=(1, -1, 2, 3)) for a, b in [(20, 60), (50, 90), (30, 80), (70, 110)]]
mA7 = [nm(f"The sum of all prime factors (distinct) of {n} is:", sum(fac(n)), f"${n}={ftex(n)}$", offs=(1, -1, 2, 4)) for n in [210, 330, 390, 462]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([QQ(f"Find the HCF and LCM of {a} and {b} using prime factorisation.", f"${a}={pf(a)}$, ${b}={pf(b)}$", f"HCF $={gcd(a,b)}$, LCM $={lcm(a,b)}$") for a, b in [(24, 36), (30, 45), (42, 56), (48, 72)]]
          + [QQ(f"Find the smallest number that must be added to {n} to make it divisible by {d}.", f"{n} divided by {d} leaves remainder {n%d}", f"Add ${(-n)%d}$ to get {n+(-n)%d}") for n, d in [(1234, 9), (5678, 11), (3456, 7), (7891, 8)]]
          + [QQ(f"Find the missing digit so that {str(n)[:-1]}_ is divisible by 9.", f"Digit sum of known digits is {ds(n//10)}", f"Missing digit $={(-ds(n//10))%9}$") for n in [4561, 7832, 6195, 9047]])
MED_C = ([QQ(f"Find the prime factorisation of {n} and the number of its factors.", f"${n}={ftex(n)}$", f"Number of factors $=" + "\\times".join(f"({e}+1)" for e in fac(n).values()) + f"={nf(n)}$") for n in [180, 200, 252, 300, 392, 450]]
          + [QQ(f"Two bells ring every {a} minutes and every {b} minutes. They ring together at 9 am. When do they next ring together?", f"LCM of {a} and {b} is {lcm(a,b)}", f"After {lcm(a,b)} minutes", f"Time: {(9*60+lcm(a,b))//60}:{(9*60+lcm(a,b))%60:02d}") for a, b in [(12, 18), (15, 20), (20, 30), (24, 36), (10, 25), (16, 20)]]
          + [QQ(f"What is the greatest number that divides {a} and {b} exactly? How many equal groups of each kind can be made?", f"HCF of {a} and {b} is {gcd(a,b)}", f"Groups of {gcd(a,b)}: {a//gcd(a,b)} and {b//gcd(a,b)}") for a, b in [(48, 72), (60, 84), (90, 126), (56, 98), (75, 100), (105, 135)]])
MED_D = ([QQ(f"A room is {a} cm long and {b} cm wide. Find the side of the largest square tile that fits exactly, and the number of tiles.", f"Side $=\\text{{HCF}}({a},{b})={gcd(a,b)}$ cm", f"Along the length: ${a//gcd(a,b)}$ tiles", f"Along the width: ${b//gcd(a,b)}$ tiles", f"Total $={a//gcd(a,b)*(b//gcd(a,b))}$ tiles") for a, b in [(450, 360), (540, 420), (600, 480), (390, 330), (720, 540), (840, 630)]]
          + [QQ(f"Find the smallest number that leaves a remainder 1 when divided by {a}, {b} and {c}, and the next such number.", f"LCM of {a}, {b}, {c} $={lcm(lcm(a,b),c)}$", f"Smallest number $={lcm(lcm(a,b),c)+1}$", f"Next number $={2*lcm(lcm(a,b),c)+1}$", "Check remainders") for a, b, c in [(4, 5, 6), (3, 4, 8), (5, 6, 10), (6, 8, 9), (4, 6, 9), (3, 5, 9)]])

# ---------- HARD ----------
hA1 = [nm(f"The smallest 4-digit number divisible by {n} is:", -(-1000 // n) * n, "Divide 1000 by the number and round up.", offs=(n, -n, 1, 2 * n)) for n in [13, 17, 19, 23]]
hA2 = [nm(f"The number of composite numbers between 1 and {n} is:", ncomp(n), "Total minus primes minus 1.", offs=(1, -1, 2, 3)) for n in [30, 50, 70, 100]]
hA3 = [nm(f"The smallest number divisible by each of {a}, {b} and {c} is:", lcm(lcm(a, b), c), "LCM.", offs=(1, -1, a, gcd(a, b))) for a, b, c in [(6, 8, 12), (10, 15, 20), (9, 12, 18), (14, 21, 28)]]
hA4 = [nm(f"The greatest number that divides {a}, {b} and {c} leaving no remainder is:", gcd(gcd(a, b), c), "HCF of three numbers.", offs=(1, -1, 2, 3)) for a, b, c in [(48, 72, 120), (60, 90, 150), (84, 126, 210), (36, 54, 90)]]
hA5 = [nm(f"For the 3-digit number {a}d{b}, the digit d that makes it divisible by 9 (smallest such d) is:", (-(a + b)) % 9, "Digit sum must be a multiple of 9.", offs=(9, 1, 2, 3)) for a, b in [(1, 3), (2, 5), (3, 7), (4, 9)]]
hA6 = [nm(f"Which is the greatest 3-digit number that leaves remainder {r} when divided by {d}?", (999 - r) // d * d + r, "Subtract the remainder first.", offs=(d, -d, 1, 2 * d)) for d, r in [(7, 3), (9, 4), (11, 5), (13, 6)]]
hA7 = [nm(f"The sum of the first {k} prime numbers after 10 is:", sum(primes_between(11, 200)[:k]), "List the primes after 10.", offs=(1, -1, 2, 6)) for k in [3, 4, 5, 6]]
hA8 = [nm(f"The largest prime number less than {n} is:", max(primes_between(2, n - 1)), "Check numbers just below.", offs=(1, -1, 2, 4)) for n in [100, 150, 200, 250]]
hA9 = [nm(f"The product of the two smallest prime factors of {n} is:", sorted(fac(n))[0] * sorted(fac(n))[1], f"${n}={ftex(n)}$", offs=(1, 2, -1, 6)) for n in [330, 420, 570, 910]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8, hA9]
HARD_B = ([QQ(f"Find the smallest number divisible by {a}, {b} and {c}.", f"LCM of {a}, {b}, {c}", f"$={lcm(lcm(a,b),c)}$") for a, b, c in [(8, 12, 18), (10, 14, 35), (9, 15, 21), (12, 16, 24)]]
          + [QQ(f"Show that the product of {k} consecutive numbers starting from {n} is divisible by {k}.", f"The numbers include a multiple of {k}", f"Hence the product is divisible by {k}") for n, k in [(14, 3), (23, 4), (31, 3), (47, 5)]]
          + [QQ(f"Find the prime factors of {n} and the smallest number to multiply to make it divisible by {d}.", f"${n}={ftex(n)}$", f"Needed multiplier: ${d//gcd(n,d)}$") for n, d in [(84, 45), (66, 40), (90, 77), (105, 44)]])
HARD_C = ([QQ(f"Three traffic lights change every {a}, {b} and {c} seconds. If they change together at 8:00 am, after how many seconds do they next change together and at what time?", f"LCM of {a}, {b}, {c} is {lcm(lcm(a,b),c)} seconds", f"That is {lcm(lcm(a,b),c)//60} minutes {lcm(lcm(a,b),c)%60} seconds", f"Time: 8:{lcm(lcm(a,b),c)//60:02d}:{lcm(lcm(a,b),c)%60:02d} am") for a, b, c in [(48, 72, 108), (30, 45, 60), (36, 60, 90), (40, 50, 100), (24, 40, 60), (45, 75, 90)]]
          + [QQ(f"Find the greatest number that divides {a} and {b} leaving remainder {r} in each case.", f"Subtract the remainder: {a-r} and {b-r}", f"HCF of {a-r} and {b-r} is {gcd(a-r,b-r)}", f"The number is {gcd(a-r,b-r)} (it must exceed {r})") for a, b, r in [(76, 100, 4), (130, 175, 5), (95, 119, 7), (200, 242, 2), (160, 205, 5), (113, 155, 8)]]
          + [QQ(f"Find the smallest number which when divided by {a}, {b} and {c} leaves remainder {r} each time.", f"LCM $={lcm(lcm(a,b),c)}$", f"Required number $=LCM+{r}={lcm(lcm(a,b),c)+r}$", "Check each remainder") for a, b, c, r in [(6, 8, 12, 5), (10, 12, 15, 3), (8, 9, 12, 4), (12, 15, 20, 7), (6, 9, 15, 2), (14, 21, 28, 6)]])
HARD_D = ([QQ(f"A rectangular garden is {a} m by {b} m. Square flower beds of the largest possible equal size are to be made covering the garden. Find (i) the side of each bed, (ii) the number of beds, (iii) the cost of fencing all beds at ₹{c} per metre if each bed is fenced separately.", f"(i) Side $=\\text{{HCF}}={gcd(a,b)}$ m", f"(ii) Beds $={a//gcd(a,b)}\\times{b//gcd(a,b)}={a//gcd(a,b)*(b//gcd(a,b))}$", f"(iii) Perimeter of one bed $={4*gcd(a,b)}$ m", f"Total fencing $={4*gcd(a,b)*a//gcd(a,b)*(b//gcd(a,b))}$ m", f"Cost $=₹{4*gcd(a,b)*(a//gcd(a,b)*(b//gcd(a,b)))*c}$") for a, b, c in [(60, 36, 5), (72, 48, 4), (84, 60, 6), (90, 54, 3), (96, 72, 8), (108, 84, 5)]]
          + [QQ(f"Find the smallest 4-digit number divisible by {a}, {b} and {c}. Also find the largest 4-digit number divisible by all three.", f"LCM $={lcm(lcm(a,b),c)}$", f"Smallest 4-digit multiple: ${-(-1000//lcm(lcm(a,b),c))*lcm(lcm(a,b),c)}$", f"Largest 4-digit multiple: ${9999//lcm(lcm(a,b),c)*lcm(lcm(a,b),c)}$", "Verify divisibility") for a, b, c in [(6, 8, 12), (10, 15, 18), (9, 12, 15), (14, 16, 24), (12, 20, 25), (18, 24, 30)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
