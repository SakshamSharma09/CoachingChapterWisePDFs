"""Class 6 Maths Ch 3 - Number Play."""
from g67 import *

SLUG, NAME, CHNO = "Number_Play", "Number Play", 3

def rev(n): return int(str(n)[::-1])
def ispal(n): return str(n) == str(n)[::-1]
def big(ds): return int("".join(sorted(map(str, ds), reverse=True)))
def small(ds):
    s = sorted(map(str, ds))
    if s[0] == "0":
        i = next(i for i, c in enumerate(s) if c != "0"); s[0], s[i] = s[i], s[0]
    return int("".join(s))
def kap(n, w=4):
    d = list(str(n).zfill(w)); a = int("".join(sorted(d, reverse=True))); b = int("".join(sorted(d)))
    return a - b
def kapchain(n, w=4):
    out = [n]
    while True:
        m = kap(out[-1], w)
        out.append(m)
        if m == out[-2] or len(out) > 12: break
    return out
def rap(n):
    steps = 0; out = [n]
    while not ispal(out[-1]) and steps < 20:
        out.append(out[-1] + rev(out[-1])); steps += 1
    return out
def col(n):
    out = [n]
    while n != 1: n = n // 2 if n % 2 == 0 else 3 * n + 1; out.append(n)
    return out
def rnd(n, p): return (n + p // 2) // p * p
def ind(n):
    s = str(n)
    if len(s) <= 3: return s
    h, t = s[:-3], s[-3:]; parts = []
    while len(h) > 2: parts.insert(0, h[-2:]); h = h[:-2]
    if h: parts.insert(0, h)
    return ",".join(parts + [t])
def digs(n): return sorted(map(int, str(n)))
def ds(n): return sum(map(int, str(n)))

# ---------- EASY ----------
eA1 = [nm(f"The largest number that can be formed by using each of the digits {', '.join(map(str, d))} once is:", big(d), "Write the digits in decreasing order.", offs=(9, -9, 90, 180, 27)) for d in [(3, 8, 1, 5), (6, 2, 9, 4), (7, 0, 5, 3), (4, 1, 8, 6)]]
eA2 = [nm(f"The smallest number that can be formed by using each of the digits {', '.join(map(str, d))} once is:", small(d), "Write the digits in increasing order (a non-zero digit first).", offs=(9, -9, 90, 180, 27)) for d in [(3, 8, 1, 5), (6, 2, 9, 4), (7, 0, 5, 3), (4, 1, 8, 6)]]
eA3 = [tm(f"Which of these is a palindrome?", str(p), [str(p + 1), str(p + 10), str(p + 12)], "A palindrome reads the same forwards and backwards.") for p in [454, 3223, 7887, 12521, 6556]]
eA4 = [nm(f"The successor of {n} is:", n + 1, "Add 1.", offs=(-1, 2, 10, -2)) for n in [999, 4569, 10099, 78999]]
eA5 = [nm(f"Rounding {n} to the nearest ten gives:", rnd(n, 10), "Look at the ones digit: 5 or more rounds up.", offs=(10, -10, 1, 100)) for n in [347, 4682, 5555, 7294]]
eA6 = [nm(f"Rounding {n} to the nearest hundred gives:", rnd(n, 100), "Look at the tens digit.", offs=(100, -100, 10, 1000)) for n in [3482, 6750, 9238, 1049]]
eA7 = [tm(q, a, w, "Rule") for q, a, w in [("The sum of two even numbers is always:", "even", ["odd", "either", "a palindrome"]), ("The sum of two odd numbers is always:", "even", ["odd", "either", "a multiple of 3"]), ("The sum of an even and an odd number is:", "odd", ["even", "always 0", "always 10"])]]
eA8 = [nm(f"The digit in the thousands place of {n} is:", int(str(n)[-4]), "Count places from the right: ones, tens, hundreds, thousands.", offs=(1, -1, 2, 3, 5)) for n in [48765, 29341, 70582, 61937]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Write the largest and the smallest numbers formed from the digits {', '.join(map(str,d))}, using each digit once.", f"Largest ${big(d)}$", f"Smallest ${small(d)}$") for d in [(5, 2, 7, 9), (1, 6, 3, 8), (9, 0, 4, 2), (2, 5, 0, 7)]]
          + [QQ(f"Is {n} a palindrome? Write its reverse.", f"Reverse of {n} is {rev(n)}", "Yes, it is a palindrome" if ispal(n) else "No, it is not a palindrome") for n in [636, 1234, 4994, 5605]]
          + [QQ(f"Round {n} to the nearest hundred and to the nearest thousand.", f"Nearest hundred: {rnd(n,100)}", f"Nearest thousand: {rnd(n,1000)}") for n in [4387, 6512, 8950, 2049]])
EASY_C = ([QQ(f"Find the sum and the difference of the largest and the smallest numbers from the digits {', '.join(map(str,d))}.", f"Largest $={big(d)}$, smallest $={small(d)}$", f"Sum $={big(d)+small(d)}$", f"Difference $={big(d)-small(d)}$") for d in [(4, 7, 1), (9, 3, 5), (6, 8, 2), (7, 1, 3), (8, 5, 4), (2, 9, 6)]]
          + [QQ(f"Reverse {n} and add it to {n}. Is the sum a palindrome?", f"Reverse $={rev(n)}$", f"Sum $={n}+{rev(n)}={n+rev(n)}$", "Yes, palindrome" if ispal(n + rev(n)) else "No, not a palindrome") for n in [12, 23, 34, 41, 52, 61]]
          + [QQ(f"Estimate {a} + {b} by rounding each to the nearest hundred. Find the exact sum too.", f"{a} rounds to {rnd(a,100)} and {b} rounds to {rnd(b,100)}", f"Estimate $={rnd(a,100)+rnd(b,100)}$", f"Exact $={a+b}$") for a, b in [(3482, 2619), (5764, 1348), (4125, 3987), (6291, 2433), (7048, 1556), (2874, 5321)]])
EASY_D = ([QQ(f"A school has {a} boys and {b} girls. Find the total strength, and the strength estimated to the nearest hundred.", f"Total $={a}+{b}={a+b}$", f"Nearest hundred: {rnd(a+b,100)}", "Estimate is close to the actual value") for a, b in [(1245, 1378), (2310, 1795), (1650, 2284), (3127, 1856), (2094, 2511), (1788, 1949)]]
          + [QQ(f"Use the digits {', '.join(map(str,d))}, each once, to form the greatest and the smallest 4-digit numbers. Find the difference and say whether it is even or odd.", f"Greatest $={big(d)}$", f"Smallest $={small(d)}$", f"Difference $={big(d)-small(d)}$", "Even" if (big(d) - small(d)) % 2 == 0 else "Odd") for d in [(2, 4, 6, 8), (1, 3, 5, 7), (9, 7, 2, 1), (3, 6, 0, 8), (5, 4, 1, 9), (8, 2, 7, 3)]])

# ---------- NCERT ----------
nA1 = [nm(f"Add {n} and its reverse {rev(n)}. The sum is:", n + rev(n), "Reverse and add.", offs=(11, -11, 10, 100)) for n in [14, 25, 36, 48, 59]]
nA2 = [nm(f"Kaprekar step: for {n}, (largest arrangement) - (smallest arrangement) of its digits is:", kap(n), "Arrange digits in descending and ascending order and subtract.", offs=(9, -9, 90, 99, 1)) for n in [3752, 8261, 4693, 5148]]
nA3 = [nm(f"In the Collatz sequence, the number after {n} is:", n // 2 if n % 2 == 0 else 3 * n + 1, "Even: halve it. Odd: multiply by 3 and add 1.", offs=(1, -1, 2, 10, n)) for n in [18, 11, 26, 7, 15]]
nA4 = [nm(f"The number of steps to reach a palindrome by repeatedly reversing and adding, starting from {n}:", len(rap(n)) - 1, "Keep reversing and adding.", offs=(1, -1, 2, 3)) for n in [57, 68, 75, 86]]
nA5 = [nm(f"The digit sum of {n} is:", ds(n), "Add all the digits.", offs=(1, -1, 9, 2, 10)) for n in [4567, 98765, 3829, 70512]]
nA6 = [nm(f"A supercell: the number in the middle cell is the sum of its two neighbours. If neighbours are {a} and {b}, the number is:", a + b, "Add the two neighbouring cells.", offs=(1, -1, 10, a)) for a, b in [(13, 18), (25, 47), (36, 58), (49, 62)]]
nA7 = [nm(f"Estimate {a} + {b} by rounding to the nearest thousand:", rnd(a, 1000) + rnd(b, 1000), "Round each number first.", offs=(1000, -1000, 100, 500)) for a, b in [(4876, 2123), (5649, 3281), (7312, 1489), (2750, 6450)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Apply the reverse-and-add process on {n} until a palindrome appears.", " then ".join(f"{x}" for x in rap(n)[:-1]) + " each gets reversed and added", f"Palindrome reached: {rap(n)[-1]} after {len(rap(n))-1} step(s)") for n in [47, 58, 69, 78]]
           + [QQ(f"Do one Kaprekar step on {n}.", f"Largest {int(''.join(sorted(str(n),reverse=True)))}, smallest {int(''.join(sorted(str(n))))}", f"Difference $={kap(n)}$") for n in [2961, 4073, 5381, 7652]]
           + [QQ(f"Write the Collatz sequence for {n}.", "Even: halve; odd: $3n+1$", "$" + ", ".join(map(str, col(n))) + "$") for n in [6, 9, 10, 12]])
NCERT_C = ([QQ(f"Show that the Kaprekar routine on {n} reaches 6174.", "Repeat the largest-minus-smallest step", "$" + " \\to ".join(map(str, kapchain(n)[:-1])) + "$", f"Number of steps $={len(kapchain(n))-2}$") for n in [3524, 4821, 6352, 8730, 2194, 5867]]
           + [QQ(f"Find the number of steps taken by the Collatz sequence starting at {n} to reach 1 and the largest number in it.", "Follow the rule step by step", "Sequence: " + ", ".join(map(str, col(n))), f"Steps $={len(col(n))-1}$, maximum $={max(col(n))}$") for n in [13, 14, 17, 19, 20, 22]]
           + [QQ(f"A number is made by writing {a} {b} times. Find its digit sum and say whether it is divisible by 3.", f"Digit sum $={a}\\times{b}={a*b}$", "Divisible by 3 since the digit sum is " + ("a multiple of 3" if (a * b) % 3 == 0 else "not a multiple of 3, so it is not divisible")) for a, b in [(7, 5), (8, 6), (4, 9), (5, 4), (2, 12), (9, 3)]])
NCERT_D = ([QQ(f"Take the digits of {n}. Form the largest and smallest numbers from them, subtract, and repeat the process twice more. Write each result and say what you notice.", f"Step 1: {big(digs(n)) if False else int(''.join(sorted(str(n),reverse=True)))}-{int(''.join(sorted(str(n))))}={kap(n)}", f"Step 2: result {kap(kap(n))}", f"Step 3: result {kap(kap(kap(n)))}", "The numbers move toward the Kaprekar constant 6174") for n in [3141, 2718, 6021, 8472, 5390, 4455]]
           + [QQ(f"Show with working that adding {a} and {b} (both palindromes) gives {a+b}. Is the sum a palindrome? Make a palindrome using the reverse-and-add process starting from {c}.", f"{a}+{b}={a+b}", "Palindrome" if ispal(a + b) else "Not a palindrome", f"Start {c}: " + ", ".join(map(str, rap(c))), f"Palindrome {rap(c)[-1]} after {len(rap(c))-1} steps") for a, b, c in [(121, 232, 29), (343, 454, 38), (565, 676, 49), (787, 898, 56), (161, 272, 67), (383, 494, 79)]])

# ---------- MEDIUM ----------
mA1 = [nm(f"The smallest 4-digit number with digits {', '.join(map(str,d))} (each used once) that is EVEN is:", min(int("".join(map(str, p))) for p in __import__("itertools").permutations(d) if p[0] != 0 and p[-1] % 2 == 0), "End with the smallest even digit, then arrange the rest in increasing order.", offs=(9, -9, 90, 180, 18)) for d in [(3, 1, 4, 2), (5, 6, 7, 2), (9, 8, 1, 3), (4, 3, 6, 5)]]
mA2 = [nm(f"The number of 3-digit palindromes is:", 90, "First digit 1-9 and middle digit 0-9, the last digit is fixed.", offs=(10, -10, 9, 81, 100)) for _ in [0]]
mA3 = [nm(f"The greatest 5-digit palindrome with first digit {a} is:", int(f"{a}9{9}9{a}"), "Fill the middle digits with 9.", offs=(10, -10, 100, 1000, 9)) for a in [2, 4, 6, 8]]
mA4 = [nm(f"Starting from {n}, the Collatz sequence reaches 1 in how many steps?", len(col(n)) - 1, "Count each step.", offs=(1, -1, 2, 3)) for n in [15, 21, 24, 27]]
mA5 = [nm(f"Round {n} to the nearest thousand, and the result is {rnd(n,1000)}. The difference between {n} and the rounded number is:", abs(n - rnd(n, 1000)), "Subtract.", offs=(1, -1, 10, 100, 1000)) for n in [48376, 63250, 71948, 85420]]
mA6 = [nm(f"The sum of the first {n} counting numbers {', '.join(map(str, range(1, 5)))}, ... is:", tri(n), "Triangular number.", offs=(n, -n, 1, 10, 2)) for n in [30, 45, 60, 100]]
mA7 = [nm(f"A Kaprekar step on {n} gives:", kap(n), "Largest - smallest.", offs=(9, -9, 90, 99, 1)) for n in [6174, 9821, 3087, 1953]]
def g9(s, w=4):
    ds_ = []
    for _ in range(w):
        d = min(9, s); ds_.append(d); s -= d
    return int("".join(map(str, ds_)))
mA8 = [nm(f"The greatest 4-digit number whose digit sum is {t} is:", g9(t), "Put 9s from the left until the sum is used up.", offs=(9, -9, 90, 99, 1)) for t in [10, 15, 20, 25, 30]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Find the greatest and the smallest 5-digit numbers formed from {', '.join(map(str,d))}, each digit once.", f"Greatest ${big(d)}$", f"Smallest ${small(d)}$") for d in [(4, 9, 1, 7, 3), (8, 2, 6, 0, 5), (9, 3, 7, 5, 1), (2, 0, 4, 6, 8)]]
          + [QQ(f"Apply the reverse-and-add steps on {n} and state the palindrome reached.", ", ".join(map(str, rap(n))), f"Palindrome {rap(n)[-1]}") for n in [87, 96, 175, 187]]
          + [QQ(f"Estimate {a} - {b} by rounding to the nearest hundred and find the actual difference.", f"Estimate $={rnd(a,100)}-{rnd(b,100)}={rnd(a,100)-rnd(b,100)}$", f"Exact $={a-b}$") for a, b in [(8764, 3198), (9325, 4678), (7510, 2849), (6483, 1975)]])
MED_C = ([QQ(f"Perform two Kaprekar steps on {n}.", f"Step 1: ${kap(n)}$", f"Step 2: ${kap(kap(n))}$", f"Digits used: arrange {str(kap(n)).zfill(4)} to get the next number") for n in [1795, 2863, 4172, 5039, 7261, 9418]]
          + [QQ(f"Find the largest palindrome less than {n} and the smallest palindrome greater than {n}.", f"Largest below: {max(x for x in range(n) if ispal(x))}", f"Smallest above: {min(x for x in range(n+1, 100000) if ispal(x))}", "Check by reversing") for n in [1300, 2450, 3820, 5090, 6740, 8210]]
          + [QQ(f"Find the sum of all numbers from 1 to {n} by pairing the first and last numbers.", f"Pairs sum to {n+1}", f"Number of pairs $={n}\\div2={n//2}$", f"Sum $={n//2}\\times{n+1}={tri(n)}$") for n in [40, 60, 80, 120, 150, 200]])
MED_D = ([QQ(f"A palindrome of the form {a}__{a} has its middle two digits equal and the digit sum {a*2+2*b}. Find the number and check that it reads the same backwards. Add 11 to it and see if the answer is a palindrome.", f"Middle digits equal; $2\\times{a}+2m={2*a+2*b}$ so $m={b}$", f"Number ${a}{b}{b}{a}$", "Reverse is the same: palindrome", f"Add 11: {int(f'{a}{b}{b}{a}')+11}", "Palindrome" if ispal(int(f'{a}{b}{b}{a}') + 11) else "Not a palindrome") for a, b in [(2, 3), (3, 4), (4, 1), (5, 6), (6, 2), (7, 5)]]
          + [QQ(f"Using the digits {', '.join(map(str,d))} once each, form a 4-digit number closest to {t}. Show the options you tried and the difference.", "Try arrangements", f"Closest number is {min((int(''.join(map(str,p))) for p in __import__('itertools').permutations(d) if p[0]!=0), key=lambda x: abs(x-t))}", f"Difference $={abs(min((int(''.join(map(str,p))) for p in __import__('itertools').permutations(d) if p[0]!=0), key=lambda x: abs(x-t))-t)}$") for d, t in [((3, 7, 5, 1), 5000), ((8, 2, 6, 4), 6000), ((9, 1, 4, 6), 4500), ((7, 3, 8, 2), 3000), ((5, 9, 2, 6), 7000), ((4, 1, 7, 8), 2000)]])

# ---------- HARD ----------
hA1 = [nm(f"How many steps does the Kaprekar routine take to reach 6174 from {n}?", len(kapchain(n)) - 2, "Repeat the largest-minus-smallest step.", offs=(1, -1, 2, 3)) for n in [3141, 5273, 7418, 9031]]
hA2 = [nm(f"The Collatz sequence of {n} has how many terms (including {n} and 1)?", len(col(n)), "List the sequence.", offs=(1, -1, 2, 5, 10)) for n in [9, 25, 28, 31]]
hA3 = [nm(f"The number of 4-digit palindromes with first digit {a} is:", 10, "The second digit can be any of 10 digits.", offs=(1, -1, 9, 100, 90)) for a in [2, 5, 8]]
hA4 = [nm(f"The sum of {n} consecutive counting numbers starting from {a} is:", n * a + tri(n - 1), "Add the numbers.", offs=(1, -1, n, 10)) for a, n in [(12, 10), (25, 8), (40, 6), (100, 5)]]
hA5 = [nm(f"A 5-digit number ends with digit {e} and has digit sum {s}; the sum of its other four digits is:", s - e, "Subtract.", offs=(1, -1, 9, 2)) for e, s in [(7, 31), (4, 28), (9, 35), (6, 24)]]
hA6 = [nm(f"The number of digits in the largest palindrome smaller than {n}:", len(str(max(x for x in range(n) if ispal(x)))), "Find the palindrome.", offs=(1, -1, 2)) for n in [10000, 1000, 100, 100000]]
hA7 = [nm(f"On reversing and adding {n}, the first sum is:", n + rev(n), "Reverse and add.", offs=(11, -11, 10, 99)) for n in [187, 265, 349, 478]]
hA8 = [nm(f"{a} is added to its reverse and the sum is {a+rev(a)}. How many reverse-and-add steps in all are needed to reach a palindrome?", len(rap(a)) - 1, "Continue the process.", offs=(1, -1, 2, 3)) for a in [89, 98, 59, 68]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"How many steps does the Kaprekar routine need for {n}? Write the chain.", "Largest minus smallest each time", "$" + " \\to ".join(map(str, kapchain(n)[:-1])) + "$", ) for n in [1234, 2002, 4651, 8532]]
          + [QQ(f"Find the number of terms in the Collatz sequence of {n} and its largest term.", "Apply the rule", f"Terms: {len(col(n))}, maximum: {max(col(n))}") for n in [11, 18, 26, 30]]
          + [QQ(f"A number has {k} digits, all equal to {d}. Find its digit sum and the remainder when the number is divided by 9.", f"Digit sum $={k}\\times{d}={k*d}$", f"Remainder $={k*d%9}$ (same as digit sum divided by 9)") for k, d in [(12, 5), (14, 7), (11, 4), (15, 6)]])
HARD_C = ([QQ(f"Find a 4-digit palindrome that is divisible by 11 and has digit sum {2*(a+b)}. Verify.", f"Form $abba$ with $a={a}$, $b={b}$", f"Number {a}{b}{b}{a} $={int(f'{a}{b}{b}{a}')}$", f"{int(f'{a}{b}{b}{a}')}$\\div11={int(f'{a}{b}{b}{a}')//11}$ exactly", "Palindrome reads the same backwards") for a, b in [(1, 5), (2, 8), (3, 6), (4, 9), (5, 2), (7, 4)]]
          + [QQ(f"Using the supercell idea, a row of {k} numbers starting {a}, {b}, then each next cell is the sum of the previous two. Find the {k}th number and the sum of all {k} numbers.", "Build the row", "Row: " + ", ".join(map(str, fib(k, a, b))), f"{k}th number $={fib(k,a,b)[-1]}$", f"Sum $={sum(fib(k,a,b))}$") for a, b, k in [(2, 3, 8), (1, 4, 8), (3, 5, 7), (2, 6, 8), (4, 7, 7), (1, 5, 9)]]
          + [QQ(f"How many 4-digit numbers can be formed from {', '.join(map(str,d))} using each digit once? What is the largest and the smallest? What is their difference?", "Arrangements: $4\\times3\\times2\\times1=24$", f"Largest ${big(d)}$, smallest ${small(d)}$", f"Difference ${big(d)-small(d)}$") for d in [(2, 5, 7, 9), (1, 3, 6, 8), (4, 5, 6, 9), (1, 2, 8, 9), (3, 4, 7, 9), (2, 6, 7, 8)]])
HARD_D = ([QQ(f"A palindromic number of 5 digits is formed as $abcba$ where $a={a}$, $b={b}$, $c={c}$. Write the number, find its digit sum, check if it is divisible by 9, and find the smallest number to add to make it divisible by 9.", f"Number ${a}{b}{c}{b}{a}$", f"Digit sum ${2*a+2*b+c}$", "Divisible by 9" if (2 * a + 2 * b + c) % 9 == 0 else "Not divisible by 9", f"Smallest number to add: ${(-int(f'{a}{b}{c}{b}{a}'))%9}$", "Check: new digit sum is a multiple of 9") for a, b, c in [(1, 2, 3), (2, 4, 5), (3, 1, 7), (4, 6, 2), (5, 0, 8), (6, 3, 9)]]
          + [QQ(f"Find the number of steps the reverse-and-add process takes from {n} to reach a palindrome, write each sum, and state whether the final palindrome has an even or odd number of digits.", "Reverse-and-add repeatedly", "Sums: " + ", ".join(map(str, rap(n)[1:])), f"Steps $={len(rap(n))-1}$", f"Palindrome {rap(n)[-1]} has {len(str(rap(n)[-1]))} digits ({'even' if len(str(rap(n)[-1])) % 2 == 0 else 'odd'})") for n in [67, 76, 85, 94, 165, 192]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
