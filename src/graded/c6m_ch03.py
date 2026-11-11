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
    out = [n]
    while not ispal(out[-1]):
        out.append(out[-1] + rev(out[-1]))
        assert len(out) < 12, n
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
def adj(n, i):
    t = list(str(n)); t[i], t[i + 1] = t[i + 1], t[i]
    return int("".join(t)) if t[0] != "0" else n + 90
def digs(n): return sorted(map(int, str(n)))
def ev(d):
    import itertools
    return sorted({int("".join(map(str, p))) for p in itertools.permutations(d) if p[0] != 0 and p[-1] % 2 == 0})
def prevpal(n):
    n -= 1
    while not ispal(n): n -= 1
    return n
def nextpal(n):
    n += 1
    while not ispal(n): n += 1
    return n
def ds(n): return sum(map(int, str(n)))

# ---------- EASY ----------
eA1 = [nw(f"The largest number that can be formed by using each of the digits {', '.join(map(str, d))} once is:", big(d), [adj(big(d), 2), adj(big(d), 1), small(d)], "Write the digits in decreasing order.") for d in [(3, 8, 1, 5), (6, 2, 9, 4), (7, 0, 5, 3), (4, 1, 8, 6)]]
eA2 = [nw(f"The smallest number that can be formed by using each of the digits {', '.join(map(str, d))} once is:", small(d), [adj(small(d), 2), adj(small(d), 1), big(d)], "Write the digits in increasing order (a non-zero digit first).") for d in [(3, 8, 1, 5), (6, 2, 9, 4), (7, 0, 5, 3), (4, 1, 8, 6)]]
eA3 = [tm("Which of these is a palindrome?", str(p), w, "A palindrome reads the same forwards and backwards.") for p, w in [(454, ["455", "445", "544"]), (3223, ["3232", "3224", "3322"]), (7887, ["7878", "7788", "7877"]), (12521, ["12512", "12125", "12251"]), (6556, ["6565", "6655", "5656"])]]
eA4 = [nw(f"The successor of {n} is:", n + 1, [n - 1, n + 10, int(str(n)[:-1] + str((n % 10 + 1) % 10))], "Add 1.") for n in [999, 4569, 10099, 78999]]
eA5 = [nw(f"The predecessor of {n} is:", n - 1, [n + 1, n - 10, n - 100], "Subtract 1.") for n in [1000, 5230, 24001, 90000]]
eA6 = [nw(f"The place value of the digit {int(str(n)[-k])} in {n} is:", int(str(n)[-k]) * 10 ** (k - 1), [int(str(n)[-k]) * 10 ** k, int(str(n)[-k]) * 10 ** (k - 2), int(str(n)[-k]), int(str(n)[-k]) * 10 ** (k + 1)], "Place value $=$ digit $\\times$ value of its place.") for n, k in [(38462, 3), (70591, 5), (92836, 2), (45718, 4)]]
eA7 = [tm(q, a, w, "Rule") for q, a, w in [("The sum of two even numbers is always:", "even", ["odd", "a multiple of 4", "a multiple of 10"]), ("The sum of two odd numbers is always:", "even", ["odd", "a multiple of 3", "a multiple of 5"]), ("The sum of an even number and an odd number is always:", "odd", ["even", "a multiple of 3", "a multiple of 5"])]]
eA8 = [nw(f"The digit in the thousands place of {n} is:", int(str(n)[-4]), [int(str(n)[-5]), int(str(n)[-3]), int(str(n)[-2]), int(str(n)[-1])], "Count places from the right: ones, tens, hundreds, thousands.") for n in [48765, 29341, 70582, 61937]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Write the largest and the smallest numbers formed from the digits {', '.join(map(str,d))}, using each digit once.", f"Largest ${big(d)}$", f"Smallest ${small(d)}$") for d in [(5, 2, 7, 9), (1, 6, 3, 8), (9, 0, 4, 2), (2, 5, 0, 7)]]
          + [QQ(f"Is {n} a palindrome? Write its reverse.", f"Reverse of {n} is {rev(n)}", "Yes, it is a palindrome" if ispal(n) else "No, it is not a palindrome") for n in [636, 1234, 4994, 5605]]
          + [QQ(f"Write the successor and the predecessor of {n}.", f"Successor $={n}+1={n+1}$", f"Predecessor $={n}-1={n-1}$") for n in [4999, 10000, 36070, 89999]])
EASY_C = ([QQ(f"Find the sum and the difference of the largest and the smallest numbers from the digits {', '.join(map(str,d))}.", f"Largest $={big(d)}$, smallest $={small(d)}$", f"Sum $={big(d)+small(d)}$", f"Difference $={big(d)-small(d)}$") for d in [(4, 7, 1), (9, 3, 5), (6, 8, 2), (7, 1, 3), (8, 5, 4), (2, 9, 6)]]
          + [QQ(f"Reverse {n} and add it to {n}. Is the sum a palindrome?", f"Reverse $={rev(n)}$", f"Sum $={n}+{rev(n)}={n+rev(n)}$", "Yes, palindrome" if ispal(n + rev(n)) else "No, not a palindrome") for n in [12, 23, 34, 41, 52, 61]]
          + [QQ(f"In a supercell pyramid each number is the sum of the two numbers just below it. The bottom row is {a}, {b}, {c}. Find the middle row and the top number.", f"Middle row: ${a}+{b}={a+b}$ and ${b}+{c}={b+c}$", f"Top number $={a+b}+{b+c}$", f"$={a+2*b+c}$") for a, b, c in [(3, 5, 2), (4, 1, 6), (7, 2, 5), (6, 3, 8), (2, 9, 4), (8, 5, 7)]])
EASY_D = ([QQ(f"A school has {a} boys and {b} girls. Find the total strength, and how many more {'boys' if a>b else 'girls'} than {'girls' if a>b else 'boys'} there are.", f"Total $={a}+{b}={a+b}$", f"Difference $={max(a,b)}-{min(a,b)}={abs(a-b)}$", f"Total strength is {'even' if (a+b)%2==0 else 'odd'}") for a, b in [(1245, 1378), (2310, 1795), (1650, 2284), (3127, 1856), (2094, 2511), (1788, 1949)]]
          + [QQ(f"Use the digits {', '.join(map(str,d))}, each once, to form the greatest and the smallest 4-digit numbers. Find the difference and say whether it is even or odd.", f"Greatest $={big(d)}$", f"Smallest $={small(d)}$", f"Difference $={big(d)-small(d)}$", "Even" if (big(d) - small(d)) % 2 == 0 else "Odd") for d in [(2, 4, 6, 8), (1, 3, 5, 7), (9, 7, 2, 1), (3, 6, 0, 8), (5, 4, 1, 9), (8, 2, 7, 3)]])

# ---------- NCERT ----------
nA1 = [nw(f"Add {n} and its reverse {rev(n)}. The sum is:", n + rev(n), [n + rev(n) + 11, n + rev(n) - 11, n + rev(n) + 22, n + rev(n) - 22], "Reverse and add.") for n in [14, 25, 36, 48, 59]]
nA2 = [nw(f"Kaprekar step: for {n}, (largest arrangement) - (smallest arrangement) of its digits is:", kap(n), [kap(n) + 9, kap(n) - 9, kap(n) + 90, kap(n) - 90, kap(n) + 900], "Arrange digits in descending and ascending order and subtract.") for n in [3752, 8261, 4693, 5148]]
nA3 = [nw(f"In the hailstone (Collatz) sequence, the number after {n} is:", n // 2 if n % 2 == 0 else 3 * n + 1, ([3 * n + 1, n // 2 + 1, 2 * n] if n % 2 == 0 else [n // 2, 3 * n, 3 * n + 2, (n + 1) // 2]), "Even: halve it. Odd: multiply by 3 and add 1.") for n in [18, 11, 26, 7, 15]]
nA4 = [nw(f"The number of steps to reach a palindrome by repeatedly reversing and adding, starting from {n}:", len(rap(n)) - 1, [len(rap(n)), len(rap(n)) + 1, len(rap(n)) - 2, len(rap(n)) + 2], "Keep reversing and adding.") for n in [57, 68, 79, 69]]
nA5 = [nw(f"The digit sum of {n} is:", ds(n), [ds(n) - int(str(n)[0]), ds(n) + int(str(n)[-1]), ds(n) + 9, ds(n) - 9], "Add all the digits.") for n in [4567, 98765, 3829, 70512]]
nA6 = [nw(f"In a supercell pyramid each number is the sum of the two numbers just below it. If the two numbers below are {a} and {b}, the number above them is:", a + b, [abs(a - b), a * b, a + b + 10, a + b - 10], "Add the two cells below.") for a, b in [(13, 18), (25, 47), (36, 58), (49, 62)]]
nA7 = [nw(f"In a supercell pyramid each number is the sum of the two numbers just below it. The bottom row is {a}, {b}, {c}. The top number is:", a + 2 * b + c, [a + b + c, 2 * (a + b + c), a + 3 * b + c, a + b + c + b + b + 1], "Middle row: $a+b$ and $b+c$; top $=a+2b+c$.") for a, b, c in [(4, 6, 3), (7, 2, 5), (9, 4, 1), (6, 8, 2)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Apply the reverse-and-add process on {n} until a palindrome appears.", " then ".join(f"{x}" for x in rap(n)[:-1]) + " each gets reversed and added", f"Palindrome reached: {rap(n)[-1]} after {len(rap(n))-1} step(s)") for n in [47, 58, 69, 78]]
           + [QQ(f"Do one Kaprekar step on {n}.", f"Largest {int(''.join(sorted(str(n),reverse=True)))}, smallest {int(''.join(sorted(str(n))))}", f"Difference $={kap(n)}$") for n in [2961, 4073, 5381, 7652]]
           + [QQ(f"Write the hailstone (Collatz) sequence for {n}.", "Even: halve it; odd: multiply by 3 and add 1", "$" + ", ".join(map(str, col(n))) + "$") for n in [6, 9, 10, 12]])
NCERT_C = ([QQ(f"Show that the Kaprekar routine on {n} reaches 6174.", "Repeat the largest-minus-smallest step", "$" + " \\to ".join(map(str, kapchain(n)[:-1])) + "$", f"Number of steps $={len(kapchain(n))-2}$") for n in [3524, 4821, 6352, 8730, 2194, 5867]]
           + [QQ(f"Find the number of steps taken by the Collatz sequence starting at {n} to reach 1 and the largest number in it.", "Follow the rule step by step", "Sequence: " + ", ".join(map(str, col(n))), f"Steps $={len(col(n))-1}$, maximum $={max(col(n))}$") for n in [13, 14, 17, 19, 20, 22]]
           + [QQ(f"A number is formed by writing the digit {a} exactly {b} times in a row. Find its digit sum and say whether the number is divisible by 3.", f"Digit sum $={a}\\times{b}={a*b}$", ("Divisible by 3, because the digit sum is a multiple of 3" if (a * b) % 3 == 0 else "Not divisible by 3, because the digit sum is not a multiple of 3")) for a, b in [(7, 5), (8, 6), (4, 9), (5, 4), (2, 12), (9, 3)]])
NCERT_D = ([QQ(f"Take the digits of {n}. Form the largest and smallest numbers from them, subtract, and repeat the process twice more. Write each result and say what you notice.", f"Step 1: {int(''.join(sorted(str(n),reverse=True)))}-{int(''.join(sorted(str(n))))}={kap(n)}", f"Step 2: result {kap(kap(n))}", f"Step 3: result {kap(kap(kap(n)))}", "The numbers move toward the Kaprekar constant 6174") for n in [3141, 2718, 6021, 8472, 5390, 4455]]
           + [QQ(f"Show with working that adding {a} and {b} (both palindromes) gives {a+b}. Is the sum a palindrome? Make a palindrome using the reverse-and-add process starting from {c}.", f"{a}+{b}={a+b}", "Palindrome" if ispal(a + b) else "Not a palindrome", f"Start {c}: " + ", ".join(map(str, rap(c))), f"Palindrome {rap(c)[-1]} after {len(rap(c))-1} step(s)") for a, b, c in [(121, 232, 29), (343, 454, 38), (565, 676, 49), (787, 898, 56), (161, 272, 67), (383, 494, 79)]])

# ---------- MEDIUM ----------
mA1 = [nw(f"The smallest EVEN number that can be formed by using each of the digits {', '.join(map(str,d))} once is:", ev(d)[0], [ev(d)[1], ev(d)[2], ev(d)[-1]], "End with the smallest even digit, then arrange the rest in increasing order.") for d in [(3, 1, 4, 2), (5, 6, 7, 2), (9, 8, 1, 3), (4, 3, 6, 5)]]
mA2 = [nw("The number of 3-digit palindromes is:", 90, [100, 81, 99, 80], "First digit 1-9 and middle digit 0-9, the last digit is fixed: $9\\times10$.") for _ in [0]]
mA3 = [nw(f"The greatest 5-digit palindrome with first digit {a} is:", int(f"{a}999{a}"), [int(f"{a}989{a}"), 99999, int(f"{a}99{a}")], "Fill the middle digits with 9.") for a in [2, 4, 6, 8]]
mA4 = [nw(f"Starting from {n}, the hailstone (Collatz) sequence reaches 1 in how many steps?", len(col(n)) - 1, [len(col(n)), len(col(n)) - 2, len(col(n)) + 1, len(col(n)) + 3], "Count each step.") for n in [16, 21, 24, 20]]
mA5 = [nw(f"The next palindrome after {n} is:", nextpal(n), [n + 11, prevpal(n), nextpal(n) + 110], "Keep the first half and mirror it; if that is not bigger, increase the middle.") for n in [1331, 4883, 3002, 7650]]
mA6 = [nw(f"The sum of the first {n} counting numbers $1+2+3+\\dots+{n}$ is:", tri(n), [n * n, n * (n + 1), tri(n) + n], "Pair the numbers: first with last.") for n in [30, 45, 60, 100]]
mA7 = [nw(f"A Kaprekar step on {n} gives:", kap(n), [kap(n) + 9, kap(n) - 9, kap(n) + 90, kap(n) - 90], "Largest - smallest.") for n in [6174, 9821, 3087, 1953]]
def g9(s, w=4):
    ds_ = []
    for _ in range(w):
        d = min(9, s); ds_.append(d); s -= d
    return int("".join(map(str, ds_)))
mA8 = [nw(f"The greatest 4-digit number whose digit sum is {t} is:", g9(t), w, "Put 9s from the left until the sum is used up.") for t, w in [(10, [8200, 9010, 5500]), (15, [9510, 6900, 8700]), (20, [9911, 9830, 9290]), (25, [9961, 9790, 7990]), (30, [9984, 9939, 9399])]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Find the greatest and the smallest 5-digit numbers formed from {', '.join(map(str,d))}, each digit once.", f"Greatest ${big(d)}$", f"Smallest ${small(d)}$") for d in [(4, 9, 1, 7, 3), (8, 2, 6, 0, 5), (9, 3, 7, 5, 1), (2, 0, 4, 6, 8)]]
          + [QQ(f"Apply the reverse-and-add steps on {n} and state the palindrome reached.", ", ".join(map(str, rap(n))), f"Palindrome {rap(n)[-1]}") for n in [87, 96, 175, 192]]
          + [QQ(f"In a supercell pyramid each number is the sum of the two numbers just below it. The bottom row is {a}, {b}, {c}, {d}. Find the top number.", f"Second row: {a+b}, {b+c}, {c+d}", f"Third row: {a+2*b+c}, {b+2*c+d}", f"Top $={a+3*b+3*c+d}$") for a, b, c, d in [(2, 3, 1, 4), (5, 1, 2, 3), (4, 2, 6, 1), (3, 5, 4, 2)]])
MED_C = ([QQ(f"Perform two Kaprekar steps on {n}.", f"Step 1: ${kap(n)}$", f"Step 2: ${kap(kap(n))}$", f"Digits used: arrange {str(kap(n)).zfill(4)} to get the next number") for n in [1795, 2863, 4172, 5039, 7261, 9418]]
          + [QQ(f"Find the largest palindrome less than {n} and the smallest palindrome greater than {n}.", f"Largest below: {max(x for x in range(n) if ispal(x))}", f"Smallest above: {min(x for x in range(n+1, 100000) if ispal(x))}", "Check by reversing") for n in [1300, 2450, 3820, 5090, 6740, 8210]]
          + [QQ(f"Find the sum of all numbers from 1 to {n} by pairing the first and last numbers.", f"Pairs sum to {n+1}", f"Number of pairs $={n}\\div2={n//2}$", f"Sum $={n//2}\\times{n+1}={tri(n)}$") for n in [40, 60, 80, 120, 150, 200]])
MED_D = ([QQ(f"A 4-digit palindrome has first digit {a} and digit sum {a*2+2*b}. Find the number. Add 11 to it and see if the answer is a palindrome.", f"The last digit is also {a}, and the middle two digits are equal: $2\\times{a}+2m={2*a+2*b}$ so $m={b}$", f"Number ${a}{b}{b}{a}$", "Reverse is the same: palindrome", f"Add 11: {int(f'{a}{b}{b}{a}')+11}", "Palindrome" if ispal(int(f'{a}{b}{b}{a}') + 11) else "Not a palindrome") for a, b in [(2, 3), (3, 4), (4, 1), (5, 6), (6, 2), (7, 5)]]
          + [QQ(f"Using the digits {', '.join(map(str,d))} once each, form a 4-digit number closest to {t}. Show the options you tried and the difference.", "Try arrangements", f"Closest number is {min((int(''.join(map(str,p))) for p in __import__('itertools').permutations(d) if p[0]!=0), key=lambda x: abs(x-t))}", f"Difference $={abs(min((int(''.join(map(str,p))) for p in __import__('itertools').permutations(d) if p[0]!=0), key=lambda x: abs(x-t))-t)}$") for d, t in [((3, 7, 5, 1), 5000), ((8, 2, 6, 4), 6000), ((9, 1, 4, 6), 4500), ((7, 3, 8, 2), 3000), ((5, 9, 2, 6), 7000), ((4, 1, 7, 8), 2000)]])

# ---------- HARD ----------
hA1 = [nm(f"How many steps does the Kaprekar routine take to reach 6174 from {n}?", len(kapchain(n)) - 2, "Repeat the largest-minus-smallest step.", offs=(1, -1, 2, 3)) for n in [3141, 5273, 7418, 9031]]
hA2 = [nw(f"The hailstone (Collatz) sequence of {n} has how many terms (including {n} and 1)?", len(col(n)), [len(col(n)) - 1, len(col(n)) + 1, len(col(n)) - 2, len(col(n)) + 2], "List the sequence.") for n in [25, 28, 15, 22]]
hA3 = [nw(f"The number of 4-digit palindromes with first digit {a} is:", 10, [9, 90, 100], "The second digit can be any of 10 digits.") for a in [2, 5, 8]]
hA4 = [nw(f"The sum of {n} consecutive counting numbers starting from {a} is:", n * a + tri(n - 1), [n * a, n * a + tri(n), n * (a + n)], "Add the numbers.") for a, n in [(12, 10), (25, 8), (40, 6), (100, 5)]]
hA5 = [nw(f"A 5-digit number ends with digit {e} and has digit sum {s}; the sum of its other four digits is:", s - e, [s + e, s - e + 9, s - e - 9, s], "Subtract.") for e, s in [(7, 31), (4, 28), (9, 35), (6, 24)]]
hA6 = [nw(f"The number of digits in the largest palindrome smaller than {n} is:", len(str(max(x for x in range(n) if ispal(x)))), [len(str(n)), len(str(n)) + 1, len(str(n)) - 2], "Find the palindrome.") for n in [10000, 1000, 100, 100000]]
hA7 = [nw(f"On reversing and adding {n}, the first sum is:", n + rev(n), [n + rev(n) + 11, n + rev(n) - 11, n + rev(n) + 99, n + rev(n) - 99], "Reverse and add.") for n in [187, 265, 349, 478]]
hA8 = [nw(f"{a} is added to its reverse and the sum is {a+rev(a)}. How many reverse-and-add steps in all are needed to reach a palindrome?", len(rap(a)) - 1, [len(rap(a)), len(rap(a)) + 1, len(rap(a)) - 2, len(rap(a)) + 2], "Continue the process.") for a in [68, 59, 79, 69]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"How many steps does the Kaprekar routine need for {n}? Write the chain.", "Largest minus smallest each time", "$" + " \\to ".join(map(str, kapchain(n)[:-1])) + "$", f"Steps $={len(kapchain(n))-2}$") for n in [1234, 2002, 4651, 8532]]
          + [QQ(f"Find the number of terms in the hailstone (Collatz) sequence of {n} and its largest term.", "Apply the rule", f"Terms: {len(col(n))}, maximum: {max(col(n))}") for n in [11, 18, 26, 30]]
          + [QQ(f"A number has {k} digits, all equal to {d}. Find its digit sum, and say whether the number is divisible by 3 and whether it is divisible by 9.", f"Digit sum $={k}\\times{d}={k*d}$", f"Divisible by 3: {'yes' if (k*d)%3==0 else 'no'}; divisible by 9: {'yes' if (k*d)%9==0 else 'no'}") for k, d in [(12, 5), (14, 7), (11, 4), (15, 6)]])
HARD_C = ([QQ(f"Find a 4-digit palindrome of the form $abba$ with $a={a}$ and $b={b}$. Show that it is divisible by 11.", f"Number {a}{b}{b}{a} $={int(f'{a}{b}{b}{a}')}$", f"{int(f'{a}{b}{b}{a}')}$\\div11={int(f'{a}{b}{b}{a}')//11}$ exactly", f"Digit sum $={2*(a+b)}$", "Palindrome reads the same backwards") for a, b in [(1, 5), (2, 8), (3, 6), (4, 9), (5, 2), (7, 4)]]
          + [QQ(f"A row of {k} numbers starts {a}, {b} and each next number is the sum of the previous two. Find the {k}th number and the sum of all {k} numbers.", "Build the row", "Row: " + ", ".join(map(str, fib(k, a, b))), f"{k}th number $={fib(k,a,b)[-1]}$", f"Sum $={sum(fib(k,a,b))}$") for a, b, k in [(2, 3, 8), (1, 4, 8), (3, 5, 7), (2, 6, 8), (4, 7, 7), (1, 5, 9)]]
          + [QQ(f"How many 4-digit numbers can be formed from {', '.join(map(str,d))} using each digit once? What is the largest and the smallest? What is their difference?", "Arrangements: $4\\times3\\times2\\times1=24$", f"Largest ${big(d)}$, smallest ${small(d)}$", f"Difference ${big(d)-small(d)}$") for d in [(2, 5, 7, 9), (1, 3, 6, 8), (4, 5, 6, 9), (1, 2, 8, 9), (3, 4, 7, 9), (2, 6, 7, 8)]])
HARD_D = ([QQ(f"A palindromic number of 5 digits is formed as $abcba$ where $a={a}$, $b={b}$, $c={c}$. Write the number, find its digit sum, check if it is divisible by 9, and find the smallest number to add to make it divisible by 9.", f"Number ${a}{b}{c}{b}{a}$", f"Digit sum ${2*a+2*b+c}$", "Divisible by 9" if (2 * a + 2 * b + c) % 9 == 0 else "Not divisible by 9", f"Smallest number to add: ${(-int(f'{a}{b}{c}{b}{a}'))%9}$", "Check: new digit sum is a multiple of 9") for a, b, c in [(1, 2, 3), (2, 4, 5), (3, 1, 7), (4, 6, 2), (5, 0, 8), (6, 3, 9)]]
          + [QQ(f"Find the number of steps the reverse-and-add process takes from {n} to reach a palindrome, write each sum, and state whether the final palindrome has an even or odd number of digits.", "Reverse-and-add repeatedly", "Sums: " + ", ".join(map(str, rap(n)[1:])), f"Steps $={len(rap(n))-1}$", f"Palindrome {rap(n)[-1]} has {len(str(rap(n)[-1]))} digits ({'even' if len(str(rap(n)[-1])) % 2 == 0 else 'odd'})") for n in [67, 76, 85, 94, 165, 192]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
