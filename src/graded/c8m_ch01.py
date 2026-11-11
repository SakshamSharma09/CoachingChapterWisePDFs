"""Class 8 Maths Ch 1 — A Square and a Cube. Graded banks (NCERT / Easy / Medium / Hard).
Template for all other chapters: every question and answer is computed in code; tiers use disjoint parameter lists."""
from math import isqrt, gcd
from common import M4, Q, grp

SLUG, NAME, CHNO = "Square_and_Cube", "A Square and a Cube", 1

def fac(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def ftex(n):
    return r"\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(fac(n).items()))
def croot(n): return round(n ** (1 / 3))
def sq_mult(n):  # smallest multiplier for perfect square
    m = 1
    for p, e in fac(n).items():
        if e % 2: m *= p
    return m
def cube_mult(n):
    m = 1
    for p, e in fac(n).items():
        m *= p ** ((-e) % 3)
    return m
def cube_div(n):
    m = 1
    for p, e in fac(n).items():
        m *= p ** (e % 3)
    return m
def lcm(a, b): return a * b // gcd(a, b)
def lcm_all(xs):
    r = 1
    for x in xs: r = lcm(r, x)
    return r
def tri(n): return n * (n + 1) // 2
def issq(n): return isqrt(n) ** 2 == n
def near_nonsq(s, offs): return [str(s + o) for o in offs if not issq(s + o) and s + o > 0]

# ======================= EASY =======================
eA1 = [M4("Which of the following is a perfect square?", str(n * n), near_nonsq(n * n, [2, -3, 6, 9, -5]), f"${n}\\times{n}={n*n}$") for n in [7, 8, 9, 10, 11, 12, 13, 15]]
eA2 = [M4(f"The value of ${n}^2$ is:", str(n * n), [str(2 * n), str(n * n + n), str(n * n - n)], f"${n}\\times{n}={n*n}$") for n in [12, 14, 16, 18, 21, 25, 30, 35]]
eA3 = [M4(rf"$\sqrt{{{n*n}}}$ is equal to:", str(n), [str(n + 1), str(n - 1), str(n + 2)], f"${n}\\times{n}={n*n}$") for n in [13, 17, 19, 22, 24, 26]]
eA4 = [M4(f"The value of ${n}^3$ is:", str(n ** 3), [str(3 * n), str(n * n * 3), str(n ** 3 + n)], f"${n}\\times{n}\\times{n}={n**3}$") for n in [4, 5, 7, 8, 10, 12]]
eA5 = [M4(rf"$\sqrt[3]{{{n**3}}}$ is:", str(n), [str(n + 1), str(n - 1), str(n + 2)], f"${n}^3={n**3}$") for n in [4, 5, 6, 7, 8, 10]]
eA6 = [M4(f"The sum of the first {n} odd natural numbers is:", str(n * n), [str(n * (n + 1)), str(2 * n), str(n * n - 1)], f"Sum of first $n$ odd numbers $=n^2={n*n}$") for n in [5, 7, 9, 10]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6]
EASY_B = ([Q(f"Find the value of ${n}^2$.", f"${n}^2={n}\\times{n}={n*n}$ (2).", "2") for n in [27, 33, 41, 52]]
          + [Q(f"Is {n} a perfect square? Give a reason.", ("Yes, " + f"${n}={isqrt(n)}\\times{isqrt(n)}$ (1+1).") if issq(n) else (f"No (1), because it lies between ${isqrt(n)}^2={isqrt(n)**2}$ and ${isqrt(n)+1}^2={(isqrt(n)+1)**2}$ (1)."), "1+1") for n in [225, 250, 361, 500]]
          + [Q(f"Find the value of ${n}^3$.", f"${n}^3={n}\\times{n}\\times{n}={n**3}$ (2).", "2") for n in [13, 15, 16, 20]])
EASY_C = ([Q(rf"Find $\sqrt{{{n}}}$ by prime factorisation.", rf"${n}={ftex(n)}$ (1); pairing equal factors (1); $\sqrt{{{n}}}={isqrt(n)}$ (1).", "1+1+1") for n in [196, 324, 441, 576, 784, 900]]
          + [Q(rf"Find $\sqrt[3]{{{n}}}$ by prime factorisation.", rf"${n}={ftex(n)}$ (1); grouping equal factors in triplets (1); $\sqrt[3]{{{n}}}={croot(n)}$ (1).", "1+1+1") for n in [512, 729, 1728, 2197, 2744, 3375]]
          + [Q(f"Write ${n*n}$ as the sum of the first {n} odd natural numbers (show the sum pattern).", "$" + "+".join(str(2 * i - 1) for i in range(1, n + 1)) + f"={n*n}$ (3).", "3") for n in [6, 7, 8, 9, 11, 12]])
EASY_D = ([Q(f"Find the smallest number by which {n} must be multiplied so that the product is a perfect square. Also find the square root of the product.",
             rf"${n}={ftex(n)}$ (1); primes with odd power: multiplier $={sq_mult(n)}$ (2); product $={n*sq_mult(n)}$ (1); square root $={isqrt(n*sq_mult(n))}$ (1).", "1+2+1+1") for n in [180, 252, 300, 450, 490, 588]]
          + [Q(f"Find the smallest number by which {n} must be divided so that the quotient is a perfect cube. Also find the cube root of the quotient.",
               rf"${n}={ftex(n)}$ (1); smallest divisor $={cube_div(n)}$ (2); quotient $={n//cube_div(n)}$ (1); cube root $={croot(n//cube_div(n))}$ (1).", "1+2+1+1") for n in [108, 500, 1080, 1350, 2000, 3240]])

# ======================= NCERT TYPE =======================
nA1 = [M4(rf"How many non-square numbers lie between ${n}^2$ and ${n+1}^2$?", str(2 * n), [str(2 * n + 1), str(2 * n - 1), str(n)], f"There are $2n={2*n}$ numbers between $n^2$ and $(n+1)^2$") for n in [9, 12, 16, 20, 25]]
nA2 = [M4(rf"The value of ${n+1}^2-{n}^2$ is:", str(2 * n + 1), [str(2 * n), str(2 * n + 2), str(n + 1)], f"$(n+1)^2-n^2=2n+1={2*n+1}$") for n in [14, 19, 24, 30, 49]]
nA3 = [M4(f"The triangular number $T_{{{n}}}$ (sum of 1 to {n}) is:", str(tri(n)), [str(tri(n) + n), str(tri(n) - n), str(n * n)], f"$T_n=n(n+1)/2={tri(n)}$") for n in [8, 10, 12, 15, 20]]
nA4 = [M4(f"The sum of the consecutive triangular numbers $T_{{{n}}}$ and $T_{{{n+1}}}$ is:", str((n + 1) ** 2), [str(n * n), str((n + 1) ** 2 + 1), str(tri(n + 1) * 2)], f"$T_n+T_{{n+1}}=(n+1)^2={(n+1)**2}$") for n in [6, 9, 11, 14, 17]]
nA5 = [M4(f"For m = {m}, the Pythagorean triplet $(2m,\\,m^2-1,\\,m^2+1)$ is:", f"{2*m}, {m*m-1}, {m*m+1}", [f"{2*m}, {m*m+1}, {m*m+2}", f"{m}, {m*m-1}, {m*m+1}", f"{2*m}, {m*m-2}, {m*m+2}"], f"$2m={2*m}$, $m^2-1={m*m-1}$, $m^2+1={m*m+1}$") for m in [4, 5, 6, 7, 9]]
nA6 = [M4(f"The sum of the cubes of the first {n} natural numbers is:", str(tri(n) ** 2), [str(tri(n)), str(tri(n) ** 2 + n), str(tri(n) * 2)], f"$1^3+\\dots+n^3=\\left(\\frac{{n(n+1)}}{{2}}\\right)^2={tri(n)**2}$") for n in [4, 5, 6, 8, 10]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6]
NCERT_B = ([Q(f"Express ${n*n}$ as the sum of consecutive odd numbers starting from 1.", "$" + "+".join(str(2 * i - 1) for i in range(1, n + 1)) + f"={n*n}$ (2).", "2") for n in [10, 13, 15, 16]]
           + [Q(f"Find the Pythagorean triplet whose smallest member is {2*m}.", rf"Take $2m={2*m}$, $m={m}$ (1); triplet $({2*m},\,{m*m-1},\,{m*m+1})$ (1).", "1+1") for m in [3, 8, 10, 12]]
           + [Q(rf"Express ${n}^3$ as the sum of {n} consecutive odd numbers.", rf"The first odd number is $n^2-n+1={n*n-n+1}$ (1); $" + "+".join(str(n * n - n + 1 + 2 * i) for i in range(n)) + f"={n**3}$ (1).", "1+1") for n in [3, 4, 5, 6]])
NCERT_C = ([Q(rf"Show that $T_{{{n}}}+T_{{{n+1}}}$ is a perfect square.", rf"$T_{{{n}}}={tri(n)}$, $T_{{{n+1}}}={tri(n+1)}$ (1+1); sum $={tri(n)+tri(n+1)}={n+1}^2$ (1).", "1+1+1") for n in [5, 8, 10, 12, 15, 18]]
           + [Q(f"Check whether $({2*m},\\,{m*m-1},\\,{m*m+1})$ is a Pythagorean triplet.", rf"${2*m}^2={4*m*m}$, ${m*m-1}^2={(m*m-1)**2}$ (1); sum $={4*m*m+(m*m-1)**2}$ (1); ${m*m+1}^2={(m*m+1)**2}$ equals the sum, so it is a triplet (1).", "1+1+1") for m in [11, 13, 14, 15, 16, 17]]
           + [Q(rf"Find $\sqrt{{{n}}}$ by prime factorisation.", rf"${n}={ftex(n)}$ (1); pairing (1); $\sqrt{{{n}}}={isqrt(n)}$ (1).", "1+1+1") for n in [1156, 2116, 3136, 4356, 5625, 7056]])
NCERT_D = ([Q(rf"Verify that ${N}$ can be written as the sum of two cubes in two different ways: ${a}^3+{b}^3$ and ${c}^3+{d}^3$.",
              rf"${a}^3+{b}^3={a**3}+{b**3}={N}$ (2); ${c}^3+{d}^3={c**3}+{d**3}={N}$ (2); two different ways, so it is a taxicab number (1).", "2+2+1")
            for (N, a, b, c, d) in [(1729, 1, 12, 9, 10), (4104, 2, 16, 9, 15), (13832, 2, 24, 18, 20), (20683, 10, 27, 19, 24), (39312, 2, 34, 15, 33), (64232, 17, 39, 26, 36)]]
           + [Q(rf"Find $\sqrt[3]{{{n}}}$ by prime factorisation and verify the result by cubing.", rf"${n}={ftex(n)}$ (1); triplets give $\sqrt[3]{{{n}}}={croot(n)}$ (2); check ${croot(n)}^3={n}$ (2).", "1+2+2")
              for n in [13824, 17576, 21952, 32768, 46656, 59319]])
for g in (NCERT_A,):
    pass

# ======================= MEDIUM =======================
mA1 = [M4(f"The smallest number by which {n} must be multiplied to get a perfect square is:", str(sq_mult(n)), [str(sq_mult(n) + 1), str(sq_mult(n) * 2), str(sq_mult(n) + 2)], f"${n}={ftex(n)}$; multiply by the primes with odd power") for n in [72, 98, 128, 162, 200, 242]]
mA2 = [M4(f"The smallest number by which {n} must be divided to get a perfect cube is:", str(cube_div(n)), [str(cube_div(n) + 1), str(cube_div(n) * 2), str(cube_div(n) + 2)], f"${n}={ftex(n)}$") for n in [192, 250, 297, 375, 686, 1350]]
mA3 = [M4(f"The ones digit of ${n}^2$ is:", str(n * n % 10), dd, f"Only the ones digit {n%10} matters: ${n%10}^2$ ends in {n*n%10}") for n, dd in [(127, ["7", "4", "1"]), (238, ["8", "6", "2"]), (349, ["9", "4", "3"]), (453, ["3", "6", "1"]), (568, ["8", "6", "0"]), (679, ["9", "8", "4"])]]
mA4 = [M4(rf"$\sqrt{{{d}}}$ is equal to:", str(r), [str(round(r * 10, 4)), str(round(r / 10, 5)), str(round(r + 0.1, 4))], f"${d}$ is the square of ${r}$") for d, r in [(1.44, 1.2), (2.25, 1.5), (0.0169, 0.13), (6.25, 2.5), (0.0081, 0.09), (12.25, 3.5)]]
mA5 = [M4(rf"$\sqrt[3]{{{d}}}$ is equal to:", str(r), [str(round(r * 10, 4)), str(round(r / 10, 5)), str(round(r + 0.1, 4))], f"${d}={r}^3$") for d, r in [(0.027, 0.3), (0.125, 0.5), (1.331, 1.1), (0.064, 0.4)]]
mA6 = [M4(f"The value of ${n}^2$ is:", str(n * n), [str(n * n + 5), str(n * n - 25), str(n * n + 25)], f"Numbers ending in 5: ${n//10}\\times{n//10+1}$ then 25 gives {n*n}") for n in [45, 65, 75, 85]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6]
MED_B = ([Q(rf"Find $\sqrt{{{n}}}$ by prime factorisation.", rf"${n}={ftex(n)}$ (1); $\sqrt{{{n}}}={isqrt(n)}$ (1).", "1+1") for n in [2916, 4624, 6084, 8100]]
         + [Q(rf"Evaluate $\sqrt[3]{{\dfrac{{{a**3}}}{{{b**3}}}}}$.", rf"$\dfrac{{\sqrt[3]{{{a**3}}}}}{{\sqrt[3]{{{b**3}}}}}$ (1) $=\dfrac{{{a}}}{{{b}}}$ (1).", "1+1") for a, b in [(3, 8), (5, 6), (7, 9), (4, 11)]]
         + [Q(rf"Evaluate $\sqrt{{\dfrac{{{a*a}}}{{{b*b}}}}}$.", rf"$\dfrac{{\sqrt{{{a*a}}}}}{{\sqrt{{{b*b}}}}}$ (1) $=\dfrac{{{a}}}{{{b}}}$ (1).", "1+1") for a, b in [(9, 16), (13, 21), (15, 28), (17, 24)]])
MED_C = ([Q(f"Find the smallest number by which {n} must be multiplied to make it a perfect square. Find the square root of the product.", rf"${n}={ftex(n)}$ (1); multiplier ${sq_mult(n)}$ (1); product ${n*sq_mult(n)}$, root ${isqrt(n*sq_mult(n))}$ (1).", "1+1+1") for n in [1872, 2646, 3042, 4500, 5292, 6760]]
         + [Q(f"Find the smallest number by which {n} must be divided to make it a perfect cube. Find the cube root of the quotient.", rf"${n}={ftex(n)}$ (1); divisor ${cube_div(n)}$ (1); quotient ${n//cube_div(n)}$, root ${croot(n//cube_div(n))}$ (1).", "1+1+1") for n in [4000 * 3, 5488 * 2, 6750, 8624, 10125, 9072]]
         + [Q(rf"Find $\sqrt{{{d}}}$ using prime factorisation of the whole number obtained after removing the decimal point.", rf"${int(round(d*100))}={ftex(int(round(d*100)))}$ (1); root of the whole number ${isqrt(int(round(d*100)))}$ (1); so $\sqrt{{{d}}}={isqrt(int(round(d*100)))/10}$ (1).", "1+1+1") for d in [1.96, 3.24, 5.76, 7.84, 9.61, 12.96]])
MED_D = ([Q(f"A school has {n} students who are to stand in rows so that the number of rows equals the number of students in each row. How many more students are needed to complete the arrangement? What is the number of rows then?",
            rf"Next perfect square above {n} is ${isqrt(n)+1}^2={(isqrt(n)+1)**2}$ (2); students needed $={(isqrt(n)+1)**2-n}$ (2); rows $={isqrt(n)+1}$ (1).", "2+2+1") for n in [1500, 2000, 2500, 3000, 3600 - 55, 4100]]
         + [Q(f"The volume of a cube is {n**3} cm³. Find the side of the cube and its total surface area.", rf"$\sqrt[3]{{{n**3}}}={n}$ cm (2); TSA $=6s^2=6\times{n}^2={6*n*n}$ cm² (3).", "2+3") for n in [12, 14, 15, 18, 21, 25]])

# ======================= HARD =======================
hA1 = [M4(f"The number of perfect squares between {a} and {b} (both excluded) is:", str(sum(1 for x in range(a + 1, b) if issq(x))), [str(sum(1 for x in range(a + 1, b) if issq(x)) + d) for d in (1, 2, -1)], f"Squares from ${isqrt(a)+1}^2$ to ${isqrt(b-1)}^2$") for a, b in [(200, 900), (1000, 3000), (500, 2000), (150, 1250)]]
hA2 = [M4(f"The smallest number to be added to {n} to make it a perfect square is:", str((isqrt(n) + 1) ** 2 - n), [str((isqrt(n) + 1) ** 2 - n + d) for d in (1, 2, -1)], f"Next square is ${isqrt(n)+1}^2={(isqrt(n)+1)**2}$") for n in [1234, 2345, 3456, 4567]]
hA3 = [M4(f"The largest number to be subtracted from {n} to make it a perfect square is:", str(n - isqrt(n) ** 2), [str(n - isqrt(n) ** 2 + d) for d in (1, 2, 3)], f"Previous square is ${isqrt(n)}^2={isqrt(n)**2}$") for n in [2500 + 77, 5000 + 91, 7000 + 33, 9000 + 18]]
hA4 = [M4(f"The difference of the squares of two consecutive natural numbers is {2*n+1}. The numbers are:", f"{n} and {n+1}", [f"{n-1} and {n}", f"{n+1} and {n+2}", f"{n} and {n+2}"], f"$(n+1)^2-n^2=2n+1$ gives $n={n}$") for n in [29, 44, 59, 74]]
hA5 = [M4(f"The number of digits in the square root of a {k}-digit perfect square is:", str((k + 1) // 2), [str((k + 1) // 2 + d) for d in (1, -1, 2)], "A $k$-digit square has $\\lceil k/2\\rceil$ digits in its root") for k in [5, 6, 7, 8]]
hA6 = [M4(rf"$\sqrt[3]{{-{n**3}}}$ is:", f"-{n}", [str(n), f"-{n+1}", f"{n+1}"], rf"$(-{n})^3=-{n**3}$") for n in [9, 11, 13, 15]]
hA7 = [M4(f"The ones digit of ${n}^3$ is:", str(n ** 3 % 10), dd, f"${n%10}^3$ ends in {n**3%10}") for n, dd in [(127, ["7", "9", "1"]), (238, ["8", "4", "6"]), (349, ["1", "7", "3"]), (453, ["3", "9", "1"])]]
hA8 = [M4(f"The value of $\\sqrt{{{a*a}}}+\\sqrt{{{b*b}}}$ is:", str(a + b), [str(a * b), str(abs(a - b)), str(a + b + 1)], f"${a}+{b}={a+b}$") for a, b in [(14, 19), (23, 8), (31, 16), (18, 25)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([Q(f"Find the smallest number to be added to {n} to make it a perfect square. What is the square root of the result?", rf"Next square ${(isqrt(n)+1)**2}$ (1); add ${(isqrt(n)+1)**2-n}$, root ${isqrt(n)+1}$ (1).", "1+1") for n in [3900, 5680, 8140, 9800]]
         + [Q(f"The difference between the squares of two consecutive numbers is {2*n+1}. Find the numbers.", rf"$(n+1)^2-n^2=2n+1$ (1) so $n={n}$; numbers ${n}$ and ${n+1}$ (1).", "1+1") for n in [37, 52, 68, 85]]
         + [Q(f"Find the number of non-square numbers between ${n}^2$ and ${n+3}^2$.", rf"Between $n^2$ and $(n+3)^2$ there are ${(n+3)**2-n*n-1}$ numbers (1); squares inside: ${(n+1)**2}$ and ${(n+2)**2}$, so non-squares $={(n+3)**2-n*n-3}$ (1).", "1+1") for n in [6, 8, 11, 13]])
HARD_C = ([Q(f"A square garden has area {n*n} m². Fencing costs ₹{c} per metre. Find the total cost of fencing it.", rf"Side $=\sqrt{{{n*n}}}={n}$ m (1); perimeter $=4\times{n}={4*n}$ m (1); cost $={4*n}\times{c}=$ ₹{4*n*c} (1).", "1+1+1") for n, c in [(35, 40), (48, 35), (52, 30), (64, 25), (75, 20), (84, 15)]]
         + [Q(f"A solid cube of side {n} cm is cut into small cubes of side 1 cm. How many small cubes are formed? How many have exactly three painted faces if the big cube was painted all over?", rf"Number $={n}^3={n**3}$ (1); corner cubes have three painted faces (1); there are 8 of them (1).", "1+1+1") for n in [6, 7, 9, 10, 11, 12]]
         + [Q(f"A rectangular hall {a} m by {b} m is to be paved with equal square tiles, the largest possible. Find the side of each tile and the number of tiles.", rf"Side $=\text{{HCF}}({a},{b})={gcd(a,b)}$ m (1); area ${a*b}$ m² (1); tiles $=\dfrac{{{a*b}}}{{{gcd(a,b)**2}}}={a*b//gcd(a,b)**2}$ (1).", "1+1+1") for a, b in [(36, 48), (42, 56), (45, 60), (54, 72), (60, 84), (66, 88)]])
def lsq(xs): L = lcm_all(xs); return L, L * sq_mult(L)
def lcu(xs): L = lcm_all(xs); return L, L * cube_mult(L)
HARD_D = ([Q(f"Find the smallest square number that is divisible by each of {', '.join(map(str, xs[:-1]))} and {xs[-1]}.", rf"LCM $={lsq(xs)[0]}={ftex(lsq(xs)[0])}$ (2); multiplier to make a perfect square ${sq_mult(lsq(xs)[0])}$ (2); required number ${lsq(xs)[1]}$ (1).", "2+2+1")
           for xs in [(6, 8, 12), (4, 9, 15), (10, 12, 18), (8, 14, 21), (9, 12, 20), (15, 18, 24)]]
          + [Q(f"Find the smallest cube number that is divisible by each of {', '.join(map(str, xs[:-1]))} and {xs[-1]}.", rf"LCM $={lcu(xs)[0]}={ftex(lcu(xs)[0])}$ (2); multiplier to make a perfect cube ${cube_mult(lcu(xs)[0])}$ (2); required number ${lcu(xs)[1]}$ (1).", "2+2+1")
             for xs in [(4, 6, 9), (6, 10, 15), (8, 12, 18), (9, 14, 21), (10, 25, 30), (12, 20, 45)]])

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}
