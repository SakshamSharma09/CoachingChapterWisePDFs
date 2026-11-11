"""Class 8 Maths Ch 5 - Number Play. Graded banks; everything computed in code."""
from math import gcd
from c8m_h import *

SLUG, NAME, CHNO = "Number_Play", "Number Play", 5

def dsum(n): return sum(map(int, str(n)))
def rev(n): return int(str(n)[::-1])
def alt(n):
    s = str(n)[::-1]; return sum(int(c) for c in s[::2]), sum(int(c) for c in s[1::2])
def div11(n): a, b = alt(n); return (a - b) % 11 == 0
def divtest(n, d):
    return {2: n % 2 == 0, 3: dsum(n) % 3 == 0, 4: n % 100 % 4 == 0, 5: n % 10 in (0, 5), 8: n % 1000 % 8 == 0, 9: dsum(n) % 9 == 0, 10: n % 10 == 0, 11: div11(n), 6: n % 6 == 0}[d]
def why(n, d):
    if d == 3 or d == 9: return f"digit sum {dsum(n)} {'is' if dsum(n)%d==0 else 'is not'} a multiple of {d}"
    if d == 2: return f"last digit {n%10} {'is' if n%2==0 else 'is not'} even"
    if d == 5: return f"last digit {n%10} {'is' if n%10 in (0,5) else 'is not'} 0 or 5"
    if d == 10: return f"last digit {n%10} {'is' if n%10==0 else 'is not'} 0"
    if d == 4: return f"last two digits {n%100} {'are' if n%100%4==0 else 'are not'} divisible by 4"
    if d == 8: return f"last three digits {n%1000} {'are' if n%1000%8==0 else 'are not'} divisible by 8"
    if d == 11: a, b = alt(n); return f"alternate digit sums {a} and {b} differ by {abs(a-b)}, {'a multiple' if (a-b)%11==0 else 'not a multiple'} of 11"
    if d == 6: return f"{'even' if n%2==0 else 'odd'} and digit sum {dsum(n)} {'is' if dsum(n)%3==0 else 'is not'} a multiple of 3"
def yn(b): return "Yes" if b else "No"
def DV(d, good):
    """Which of the following is divisible by d? One multiple (good) and three near-miss non-multiples."""
    assert divtest(good, d)
    bad = []
    for k in (1, -1, 2, -2, 3, -3, 4):
        if not divtest(good + k, d) and len(bad) < 3: bad.append(good + k)
    return M4(f"Which of the following numbers is divisible by {d}?", good, bad, why(good, d))
def kap(n):
    s = sorted(f"{n:04d}"); return int("".join(reversed(s))) - int("".join(s))
def ksteps(n):
    L = [n]
    while L[-1] != 6174: L.append(kap(L[-1]))
    return L
def lcm_all(xs):
    r = 1
    for x in xs: r = lcm(r, x)
    return r
def first_nd(d, k, up=False):
    lo, hi = 10 ** (k - 1), 10 ** k - 1
    return (hi - hi % d) if up else (lo + (-lo) % d)
def blank(pat, d):
    return [x for x in range(10) if int(pat.replace("*", str(x))) % d == 0 if d != 11] if d != 11 else [x for x in range(10) if div11(int(pat.replace("*", str(x))))]
def nonmult(n, d, c=3):
    out = []; k = 1
    while len(out) < c:
        if (n + k) % d: out.append(n + k)
        k += 1
    return out

# ================= EASY =================
eA1 = [DV(3, n) for n in [2346, 8205, 6132, 5472, 7041, 4509]]
eA2 = [DV(9, n) for n in [4527, 6318, 7254, 5238, 9081, 3807]]
eA3 = [M4(f"Which of the following is divisible by {d}?", n, nonmult(n, d), why(n, d) if d in (2, 3, 4, 5, 8, 9, 10) else "") for d, n in [(2, 3846), (4, 5712), (5, 8365), (10, 7240), (3, 6213), (9, 4527 + 9), (8, 3456)]]
eA4 = [M4(f"The sum of the digits of {n} is:", dsum(n), [dsum(n) + 1, dsum(n) - 1, dsum(n) + 2], "Add all the digits") for n in [2748, 5093, 6184, 3927, 8506]]
eA5 = [M4("The sum of two odd numbers is always:", "even", ["odd", "a multiple of 3", "a prime number"], "Odd + odd = even"),
       M4("The sum of an even and an odd number is always:", "odd", ["even", "a multiple of 5", "zero"], "Even + odd = odd"),
       M4("The product of two odd numbers is always:", "odd", ["even", "a multiple of 4", "zero"], "Odd x odd = odd"),
       M4("The product of an even number and any whole number is always:", "even", ["odd", "a multiple of 3", "a prime number"], "One even factor makes the product even"),
       M4("The difference of two even numbers is always:", "even", ["odd", "a multiple of 3", "negative"], "Even - even = even"),
       M4("The sum of two consecutive whole numbers is always:", "odd", ["even", "a multiple of 3", "a multiple of 5"], "One of them is even and the other odd")]
eA6 = [M4(f"The number obtained by reversing the digits of {n} is:", rev(n), [n + 9, rev(n) + 10, rev(n) - 9], "Write the digits in the opposite order") for n in [3472, 5081, 9264, 7315]]
eA7 = [M4("Which of the following is a palindrome?", p, [p + 1, p + 10, p - 11], "A palindrome reads the same from both ends") for p in [4554, 7227, 12921, 3883]]
eA8 = [M4(f"The LCM of {a} and {b} is:", lcm(a, b), [gcd(a, b), a + b, a * b if a * b != lcm(a, b) else 2 * lcm(a, b)], "Smallest common multiple") for a, b in [(4, 6), (6, 9), (10, 15), (8, 12), (5, 7)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([Q(f"Is {n} divisible by 3? Give a reason.", f"{yn(divtest(n,3))} (1); {why(n,3)} (1).", "1+1") for n in [4821, 7352, 9063, 5419]]
          + [Q(f"Find the smallest digit to put in the blank so that the number {p} is divisible by 9.", f"Known digit sum $={dsum(int(p.replace('_','0')))}$ (1); smallest digit $={blank(p.replace('_','*'),9)[0]}$ (1).", "1+1") for p in ["47_8", "6_25", "31_4", "_839"]]
          + [Q(f"Find the LCM of {a} and {b} by listing multiples.", f"Multiples of {a}: {', '.join(str(a*i) for i in range(1,lcm(a,b)//a+1))} (1); LCM $={lcm(a,b)}$ (1).", "1+1") for a, b in [(3, 4), (4, 10), (6, 8), (9, 12)]])
EASY_C = ([Q(f"Test whether {n} is divisible by 2, 5 and 10.", f"By 2: {yn(divtest(n,2))}, {why(n,2)} (1); by 5: {yn(divtest(n,5))}, {why(n,5)} (1); by 10: {yn(divtest(n,10))}, {why(n,10)} (1).", "1+1+1") for n in [4730, 2865, 7312, 6590, 1485, 8002]]
          + [Q(f"Replace * by every possible digit so that {p} is divisible by 3.", f"Digit sum of the other digits $={dsum(int(p.replace('*','0')))}$ (1); need a total that is a multiple of 3 (1); digits: {', '.join(map(str, blank(p,3)))} (1).", "1+1+1") for p in ["2*41", "5*73", "8*16", "6*52", "3*94", "7*28"]]
          + [Q(f"Find the HCF and LCM of {a} and {b}.", f"{a} and {b}: common factors give HCF $={gcd(a,b)}$ (1.5); LCM $={lcm(a,b)}$ (1.5).", "1½+1½") for a, b in [(12, 16), (18, 24), (20, 30), (14, 35), (16, 40), (15, 45)]])
EASY_D = ([Q(f"Check whether {n} is divisible by 2, 3, 5, 9 and 10. Give a reason in each case.", " ".join(f"By {d}: {yn(divtest(n,d))}, {why(n,d)} (1);" for d in [2, 3, 5, 9, 10]), "1+1+1+1+1") for n in [3690, 4725, 8316, 5240, 2907, 6615]]
          + [Q(f"Find the smallest number that must be added to {n} so that it becomes divisible by {d}.", f"Remainder when {n} is divided by {d} is {n%d} (2); number to add $={d}-{n%d}={(-n)%d}$ (2); new number {n+(-n)%d} (1).", "2+2+1") for n, d in [(4537, 9), (6182, 9), (7345, 3), (2918, 5), (5603, 10), (3874, 9)]])

# ================= NCERT =================
nA1 = [DV(11, n) for n in [3465, 8239, 5214, 7183, 9372]]
nA2 = [DV(6, n) for n in [4518, 6150, 7296, 5322, 8112]]
nA3 = [M4(f"For the number {n}, (largest 4-digit arrangement of its digits) - (smallest arrangement) is:", kap(n), [kap(n) + 90, kap(n) - 90, kap(n) + 9], "Kaprekar routine: arrange digits in descending and ascending order and subtract") for n in [2538, 4721, 9053, 6184, 3076]]
nA4 = [M4(f"The sum of the three consecutive numbers {a}, {a+1} and {a+2} is:", 3 * a + 3, [3 * a, 3 * a + 1, 3 * a + 6], "Sum $=3\\times$ middle number") for a in [12, 25, 37, 48, 61]]
nA5 = [M4(f"The sum of the five consecutive numbers starting from {a} is:", 5 * a + 10, [5 * a, 5 * a + 5, 5 * a + 15], "Sum $=5\\times$ middle number") for a in [14, 29, 33, 40]]
nA6 = [M4(f"Think of {n}. Add {a}, multiply by {m} and subtract {m*a}. The result is:", m * n, [m * n + a, n + m, m * n - a], f"$({n}+{a})\\times{m}-{m*a}={m}\\times{n}$") for n, a, m in [(7, 5, 2), (9, 4, 3), (12, 6, 4), (15, 3, 5), (8, 10, 6)]]
def pm(pat, d): return blank(pat, d)[0]
nA7 = [M4(f"The smallest digit that can replace * in {p} so that the number is divisible by {d} is:", pm(p, d), [(pm(p, d) + 1) % 10, (pm(p, d) + 4) % 10, (pm(p, d) + 7) % 10], f"Check the rule for {d}") for p, d in [("63*8", 9), ("5*34", 3), ("27*5", 9), ("4*61", 11), ("38*2", 3)]]
nA8 = [M4("The sum of three odd numbers is:", "odd", ["even", "a multiple of 3", "always prime"], "Odd + odd = even, even + odd = odd"),
       M4("The product of three consecutive natural numbers is always:", "even", ["odd", "a prime number", "a perfect square"], "One of them is even"),
       M4("If a number is divisible by both 4 and 3, it is also divisible by:", "12", ["7", "24", "9"], "4 and 3 have no common factor"),
       M4("The Kaprekar constant for 4-digit numbers is:", "6174", ["1089", "9999", "4617"], "Repeated Kaprekar routine ends at 6174"),
       M4("A number which reads the same from left to right and right to left is called a:", "palindrome", ["prime", "perfect number", "Kaprekar number"], "Palindrome"),
       M4("The sum of an odd number of consecutive numbers starting from a is always divisible by the:", "middle number", ["first number", "last digit", "number 10"], "Sum $=$ count $\\times$ middle number")]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([Q(f"Use the divisibility rule for 11 to test {n}.", f"Sum of digits at odd places and even places: {alt(n)[0]} and {alt(n)[1]} (1); difference {abs(alt(n)[0]-alt(n)[1])}, so {yn(div11(n)).lower()} (1).", "1+1") for n in [6578, 4829, 9152, 7316]]
           + [Q(f"Apply one step of the Kaprekar routine to {n}.", f"Largest arrangement {int(''.join(sorted(f'{n:04d}', reverse=True)))}, smallest {''.join(sorted(f'{n:04d}'))} (1); difference {kap(n)} (1).", "1+1") for n in [5632, 8741, 2091, 4350]]
           + [Q(f"Take {n}. Add {a}, multiply by {m}, then subtract {m*a}. What is the result? How is it related to {n}?", f"$({n}+{a})\\times{m}={(n+a)*m}$; minus {m*a} gives {m*n} (1); result $={m}\\times{n}$ (1).", "1+1") for n, a, m in [(13, 6, 3), (21, 4, 5), (17, 7, 2), (26, 3, 4)]])
def kstr(n):
    L = ksteps(n); out = []
    for x in L[:-1]:
        s = sorted(f"{x:04d}"); hi = int("".join(reversed(s))); lo = int("".join(s)); out.append(f"{hi}-{lo:04d}={kap(x)}")
    return "; ".join(out)
NCERT_C = ([Q(f"Check whether {n} is divisible by 8 and by 11.", f"By 8: {yn(divtest(n,8))}, {why(n,8)} (1); by 11: {yn(divtest(n,11))}, {why(n,11)} (1); conclusion (1).", "1+1+1") for n in [35640, 73128, 49896, 91728, 52624, 80652]]
           + [Q(f"Apply the Kaprekar routine to {n} repeatedly until you reach 6174. Write each step.", f"Steps: {kstr(n)} (2); reaches 6174 after {len(ksteps(n))-1} steps (1).", "2+1") for n in [3521, 7840, 2963, 5108, 8216, 4390]]
           + [Q(f"Show that the sum of {n} and its reverse is divisible by 11.", f"{n}+{rev(n)}={n+rev(n)} (1); {n+rev(n)}$=11\\times{(n+rev(n))//11}$ (1); in general $10a+b+10b+a=11(a+b)$ (1).", "1+1+1") for n in [47, 63, 29, 85, 38, 74]])
NCERT_D = ([Q(f"Replace the stars so that the number {p} is divisible by both {d1} and {d2}. Find all possibilities.", f"Conditions of {d1} and {d2} on the stars (2); numbers: {', '.join(str(int(p.replace('*','{}').format(a,b))) for a in range(10) for b in range(10) if int(p.replace('*','{}').format(a,b))%d1==0 and int(p.replace('*','{}').format(a,b))%d2==0)} (2); verify one (1).", "2+2+1") for p, d1, d2 in [("4*3*", 5, 9), ("6*5*", 10, 9), ("2*4*", 10, 9), ("8*1*", 5, 9), ("3*7*", 10, 3), ("7*6*", 10, 9)]]
           + [Q(f"Take {n} and its reverse {rev(n)}. Find the difference and show that it is divisible by 9. Prove it in general for $10a+b$.", f"${max(n,rev(n))}-{min(n,rev(n))}={abs(n-rev(n))}=9\\times{abs(n-rev(n))//9}$ (2); in general $(10a+b)-(10b+a)=9(a-b)$ (2); hence divisible by 9 (1).", "2+2+1") for n in [83, 61, 94, 52, 71, 85]])

# ================= MEDIUM =================
mA1 = [M4(f"The digit that replaces * in {p} so that the number is divisible by 11 is:", blank(p, 11)[0], [(blank(p, 11)[0] + k) % 10 for k in (1, 3, 6)], "Alternate digit sums must differ by 0 or 11") for p in ["7*93", "6*81", "2*64", "9*17", "4*85"]]
mA2 = [M4(f"The smallest digit that replaces * in {p} so that the number is divisible by 6 is:", blank(p, 6)[0], [(blank(p, 6)[0] + k) % 10 for k in (1, 2, 5)], "The number must be even and its digit sum a multiple of 3") for p in ["52*8", "71*4", "46*0", "93*2", "28*6"]]
mA3 = [M4(f"One step of the Kaprekar routine applied to {n} gives:", kap(n), [kap(n) + 99, kap(n) - 99, kap(n) + 18], "Largest arrangement minus smallest arrangement") for n in [1895, 6230, 7714, 3409, 9326]]
mA4 = [M4(f"The smallest number divisible by {', '.join(map(str, xs[:-1]))} and {xs[-1]} is:", lcm_all(xs), [lcm_all(xs) * 2, lcm_all(xs) // 2 if lcm_all(xs) % 2 == 0 else lcm_all(xs) + 1, lcm_all(xs) + xs[0]], "Find the LCM") for xs in [(4, 6, 10), (6, 8, 12), (9, 12, 15), (10, 14, 35), (8, 18, 24)]]
mA5 = [M4(f"The smallest number to be added to {n} to make it divisible by {d} is:", (-n) % d, [((-n) % d + k) % d if ((-n) % d + k) % d != (-n) % d else d for k in (1, 2, 3)], f"{n} leaves remainder {n%d} when divided by {d}") for n, d in [(4829, 8), (6713, 11), (5207, 6), (9154, 9), (7381, 12)]]
mA6 = [M4(f"The smallest 4-digit number divisible by {d} is:", first_nd(d, 4), [first_nd(d, 4) - d, first_nd(d, 4) + d, 1000], f"Smallest 4-digit number is 1000; add what is needed to reach a multiple of {d}") for d in [7, 12, 15, 18, 25]]
mA7 = [M4(f"The value of {n} - {rev(n)} is:", n - rev(n), [n - rev(n) + 9, n - rev(n) - 9, n - rev(n) + 90], "Subtract the reverse") for n in [83, 92, 74, 65, 91]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([Q(f"Find the smallest number to be added to {n} to make it divisible by {d}.", f"{n} divided by {d} leaves remainder {n%d} (1); add ${d}-{n%d}={(-n)%d}$ (1).", "1+1") for n, d in [(8456, 11), (3721, 8), (6094, 12), (5518, 7)]]
         + [Q(f"Check whether {n} is divisible by 12 using the rules for 3 and 4.", f"By 3: {yn(divtest(n,3))}, {why(n,3)} (1); by 4: {yn(divtest(n,4))}, {why(n,4)} (1).", "1+1") for n in [3516, 7248, 4950, 8124]]
         + [Q(f"Find {n} - {rev(n)} for the 3-digit number {n} and check whether it is divisible by 99.", f"{n}-{rev(n)}={n-rev(n)} (1); ${n-rev(n)}=99\\times{(n-rev(n))//99}$, so divisible (1).", "1+1") for n in [842, 753, 961, 634]])
MED_C = ([Q(f"Find the smallest 4-digit number divisible by both {a} and {b}.", f"LCM of {a} and {b} is {lcm(a,b)} (1); first multiple not below 1000 (1); {first_nd(lcm(a,b),4)} (1).", "1+1+1") for a, b in [(12, 15), (14, 21), (16, 24), (18, 27), (20, 30), (9, 25)]]
         + [Q(f"Find the digit * so that {p} is divisible by 11. Show your working.", f"Alternate sums for each trial; need difference 0 or 11 (1); {blank(p,11) and ''}* $={blank(p,11)[0]}$ (1); check {int(p.replace('*',str(blank(p,11)[0])))} (1).", "1+1+1") for p in ["83*5", "6*19", "8*47", "5*82", "37*4", "9*36"]]
         + [Q(f"Express {n} as the sum of three consecutive natural numbers.", f"Middle number $=\\frac{{{n}}}{{3}}={n//3}$ (1); numbers {n//3-1}, {n//3}, {n//3+1} (1); check sum $={n}$ (1).", "1+1+1") for n in [54, 81, 111, 150, 213, 333]])
def md1(n):
    return Q(f"Apply the Kaprekar routine to {n} until you reach 6174. Write every step and state the number of steps.", f"Steps: {kstr(n)} (3); total {len(ksteps(n))-1} steps (2).", "3+2")
def md2(a, b, c, r):
    L = lcm_all([a, b, c])
    return Q(f"Find the smallest number which leaves remainder {r} when divided by {a}, {b} and {c}.", f"LCM({a}, {b}, {c}) $={L}$ (3); required number $={L}+{r}={L+r}$ (2).", "3+2")
MED_D = [md1(n) for n in [1495, 8620, 3187, 5942, 7061, 2618]] + [md2(*r) for r in [(6, 8, 12, 3), (10, 15, 20, 4), (9, 12, 18, 5), (8, 12, 20, 7), (4, 14, 21, 2), (12, 16, 24, 6)]]

# ================= HARD =================
def minrem(a, b, r): return lcm(a, b) + r
hA1 = [M4(f"The smallest number which leaves remainder {r} when divided by {a} and {b} is:", minrem(a, b, r), [lcm(a, b), minrem(a, b, r) + lcm(a, b), a * b + r if a * b + r != minrem(a, b, r) else a * b + r + 1], "LCM plus the common remainder") for a, b, r in [(12, 18, 5), (15, 20, 7), (14, 21, 4), (16, 24, 9), (18, 30, 11)]]
cnt = lambda lo, hi, d: hi // d - (lo - 1) // d
hA2 = [M4(f"The number of multiples of {d} between {lo} and {hi} (both included) is:", cnt(lo, hi, d), [cnt(lo, hi, d) + 1, cnt(lo, hi, d) - 1, cnt(lo, hi, d) + 2], f"{hi//d} multiples up to {hi} minus {(lo-1)//d} multiples below {lo}") for lo, hi, d in [(100, 500, 7), (200, 900, 12), (50, 1000, 15), (300, 2000, 25), (111, 999, 9)]]
hA3 = [M4(f"The number of 3-digit numbers divisible by {d} is:", cnt(100, 999, d), [cnt(100, 999, d) + 1, cnt(100, 999, d) - 1, 999 // d], "Count multiples from 100 to 999") for d in [8, 13, 17, 22, 35]]
def pal(d):
    return min(p for p in range(100, 1000) if str(p) == str(p)[::-1] and p % d == 0)
hA4 = [M4(f"The smallest 3-digit palindrome divisible by {d} is:", pal(d), [pal(d) + 10, pal(d) - 10, pal(d) + d], "Test palindromes 101, 111, 121, ...") for d in [3, 4, 6, 7, 9]]
def ab(t, d):
    return [(a, b) for a in range(10) for b in range(10) if int(t.replace("a", str(a)).replace("b", str(b))) % d == 0]
hA5 = [M4(f"If the number {t} is divisible by 90, then $a+b$ equals:", sum(ab(t, 90)[0]), [sum(ab(t, 90)[0]) + k for k in (1, 2, 3)], "Divisible by 10 and 9") for t in ["6a2b", "1a4b", "5a8b", "4a6b", "9a1b"]]
hA6 = [M4(f"The number of steps the Kaprekar routine needs to reach 6174 starting from {n} is:", len(ksteps(n)) - 1, [len(ksteps(n)), len(ksteps(n)) - 2 if len(ksteps(n)) > 2 else len(ksteps(n)) + 2, len(ksteps(n)) + 1], "Apply the routine and count") for n in [2111, 5555 - 1, 9831, 1004, 7766]]
hA7 = [M4(f"A number is divisible by both {a} and {b}. It must be divisible by:", a * b, [a + b, a * b * 2, a * b // gcd(a, b) + a], f"{a} and {b} have no common factor") for a, b in [(9, 11), (8, 9), (5, 7), (7, 8), (11, 13)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7]
HARD_B = ([Q(f"Find the smallest number which leaves remainder {r} when divided by {a} and {b}.", f"LCM({a}, {b}) $={lcm(a,b)}$ (1); number $={lcm(a,b)}+{r}={lcm(a,b)+r}$ (1).", "1+1") for a, b, r in [(20, 25, 3), (24, 36, 5), (28, 42, 9), (30, 45, 8)]]
          + [Q(f"How many multiples of {d} lie between {lo} and {hi} (both included)?", f"{hi//d} multiples up to {hi} (1); minus {(lo-1)//d} below {lo}, giving {cnt(lo,hi,d)} (1).", "1+1") for lo, hi, d in [(150, 800, 11), (250, 1500, 14), (75, 600, 6), (1000, 5000, 125)]]
          + [Q(f"The sum of five consecutive numbers is {S}. Find the numbers.", f"Middle number $={S}\\div5={S//5}$ (1); numbers {S//5-2}, {S//5-1}, {S//5}, {S//5+1}, {S//5+2} (1).", "1+1") for S in [45, 80, 115, 150]])
HARD_C = ([Q(f"Show that the six-digit number {n}{n} is divisible by 7, 11 and 13.", f"{n}{n} $={n}\\times1001$ (1); $1001=7\\times11\\times13$ (1); so divisible by 7, 11 and 13 (quotients {n*1001//7}, {n*1001//11}, {n*1001//13}) (1).", "1+1+1") for n in [247, 358, 429, 516, 683, 791]]
          + [Q(f"Find the greatest 4-digit number divisible by {a}, {b} and {c}.", f"LCM $={lcm_all([a,b,c])}$ (1); {9999} divided by it leaves remainder {9999%lcm_all([a,b,c])} (1); number {9999-9999%lcm_all([a,b,c])} (1).", "1+1+1") for a, b, c in [(6, 8, 12), (10, 12, 15), (9, 15, 18), (14, 21, 28), (16, 20, 30), (12, 18, 27)]]
          + [Q(f"How many 3-digit numbers are divisible by both {a} and {b}?", f"LCM $={lcm(a,b)}$ (1); multiples from 100 to 999: ${999//lcm(a,b)}-{99//lcm(a,b)}$ (1); {cnt(100,999,lcm(a,b))} (1).", "1+1+1") for a, b in [(6, 8), (9, 12), (10, 14), (15, 20), (12, 21), (16, 18)]])
def hd1(t, d):
    s = ab(t, d); sols = ", ".join(f"a = {a}, b = {b} (number {t.replace('a',str(a)).replace('b',str(b))})" for a, b in s)
    return Q(f"Find the digits $a$ and $b$ if the number {t} is divisible by {d}. List all possibilities.", f"Splitting {d} into coprime factors and applying the rules (2); possibilities: {sols} (2); verification (1).", "2+2+1")
def hd2(n):
    d = n - rev(n); r = rev(d)
    return Q(f"Take the number {n}. Subtract its reverse. Add the reverse of the result to the result. What do you get? Show that this always happens for 3-digit numbers whose first and last digits differ by 2 or more.", f"{n}-{rev(n)}={d} (1); reverse of {d} is {r} (1); {d}+{r}={d+r} (1); in general the difference is $99(a-c)$, whose digits are $(a-c-1),9,(10-a+c)$ and the sum is always 1089 (2).", "1+1+1+2")
HARD_D = [hd1(t, d) for t, d in [("4a3b", 45), ("6a2b", 90), ("5a7b", 36), ("8a1b", 45), ("3a9b", 72), ("2a5b", 18)]] + [hd2(n) for n in [832, 641, 954, 723, 865, 971]]

TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}
