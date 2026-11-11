"""Class 7 Maths Ch 6 - Number Play (parity, digit games, reversals, Collatz, Kaprekar, consecutive sums, divisibility by 2, 3, 5, 9, 10)."""
from g67 import *
from itertools import permutations

SLUG, NAME, CHNO = "Number_Play", "Number Play", 6

def rev(n): return int(str(n)[::-1])
def dsum(n): return sum(map(int, str(n)))
def collatz(n):
    out = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        out.append(n)
    return out
def kap(n):
    s = str(n).zfill(4); big = int("".join(sorted(s, reverse=True))); small = int("".join(sorted(s)))
    return big, small, big - small
def kap_path(n):
    path = [n]
    while path[-1] != 6174:
        path.append(kap(path[-1])[2])
    return path
def rac(n):
    sums = []
    while str(n) != str(n)[::-1]:
        n = n + rev(n); sums.append(n)
        assert len(sums) <= 10, n
    return sums
def seq(xs): return "$" + ", ".join(map(str, xs)) + "$"
def par(n): return "even" if n % 2 == 0 else "odd"
def nn(q, c, why="", offs=(1, -1, 2, -2, 3, 10, 9)): return nm(q, c, why, offs=offs, pos=True)

# ------------------------------------------------ EASY
eA1 = [tm(t, c, w, "Use the even/odd rules.") for t, c, w in [
    ("The sum of two odd numbers is always:", "even", ["odd", "a multiple of 5", "a prime number"]),
    ("The sum of an even number and an odd number is:", "odd", ["even", "a multiple of 3", "zero"]),
    ("The product of two odd numbers is:", "odd", ["even", "a multiple of 2", "zero"]),
    ("The product of an even number and any whole number is:", "even", ["odd", "a multiple of 3", "a prime number"]),
    ("The sum of three odd numbers is:", "odd", ["even", "a multiple of 3", "zero"])]]
eA2 = [nn(f"The sum of the digits of ${n}$ is:", dsum(n), "Add all the digits.") for n in (47, 385, 2906, 7254, 99)]
eA3 = [tm(f"The reverse of ${n}$ is:", str(rev(n)), [str(n), str(int(str(n)[1:] + str(n)[0])), "".join(sorted(str(n)))], "Write the digits in the opposite order.") for n in (3475, 1208, 9051, 5684)]
eA4 = [tm("Which of these numbers is a palindrome?", c, w, "A palindrome reads the same from both ends.") for c, w in [
    ("1331", ["1313", "1231", "1332"]), ("4554", ["4545", "4455", "4564"]), ("27872", ["27782", "27827", "28772"]), ("90609", ["90690", "96009", "90906"])]]
eA5 = [tm("Which of these numbers is divisible by 9?", c, w, "A number is divisible by 9 if its digit sum is.") for c, w in [
    ("1827", ["1828", "1829", "1830"]), ("4563", ["4562", "4564", "4565"]), ("2358", ["2357", "2359", "2360"]), ("7893", ["7892", "7894", "7895"])]]
eA6 = [nn(f"In the Collatz rule (halve if even, multiply by 3 and add 1 if odd), the number after ${n}$ is:", n // 2 if n % 2 == 0 else 3 * n + 1, "Check whether the number is even or odd.") for n in (7, 12, 9, 20, 15)]
eA7 = [nn(f"The sum of the first {n} odd numbers is:", n * n, "The sum of the first $n$ odd numbers is $n^2$.") for n in (6, 9, 12, 15)]
eA8 = [nn(f"A two-digit number has tens digit ${a}$ and units digit ${b}$. Its value is:", 10 * a + b, "Value $=10\\times$ tens $+$ units.") for a, b in [(7, 4), (3, 9), (8, 0)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]

def col_b(n):
    s = collatz(n)
    return QQ(f"Write the Collatz sequence that starts from ${n}$ (halve if even; triple and add 1 if odd) until you reach 1.", f"Apply the rule to each number in turn", f"Sequence: {seq(s)}", f"It reaches 1 after ${len(s) - 1}$ steps")
def rac_b(n):
    sums = rac(n); lines = []; cur = n
    for s in sums: lines.append(f"${cur}+{rev(cur)}={s}$"); cur = s
    return QQ(f"Use reverse-and-add on ${n}$ until a palindrome appears.", "Add the number to its reverse", "; ".join(lines), f"Palindrome obtained: ${sums[-1]}$")
def div_b(n):
    d = dsum(n)
    return QQ(f"Without dividing, test whether ${n}$ is divisible by 3 and by 9.", f"Digit sum $={d}$", f"Divisible by 3: {'yes' if d % 3 == 0 else 'no'} (digit sum {'is' if d % 3 == 0 else 'is not'} a multiple of 3)", f"Divisible by 9: {'yes' if d % 9 == 0 else 'no'} (digit sum {'is' if d % 9 == 0 else 'is not'} a multiple of 9)")
EASY_B = [col_b(n) for n in (6, 5, 10, 3)] + [rac_b(n) for n in (29, 48, 35, 67)] + [div_b(n) for n in (4725, 5136, 2548, 3282)]
def kap_c(n):
    big, small, d = kap(n)
    return QQ(f"Apply one step of Kaprekar's routine to ${n}$ (largest arrangement of the digits minus smallest arrangement).", f"Largest $={big}$", f"Smallest $={small}$ (digits arranged in increasing order)", f"Difference $={big}-{small}={d}$")
def cons3(S):
    m = S // 3
    return QQ(f"The sum of three consecutive numbers is ${S}$. Find the numbers.", f"Middle number $={S}\\div3={m}$", f"The numbers are ${m - 1}$, ${m}$ and ${m + 1}$", f"Check: ${m - 1}+{m}+{m + 1}={S}$")
def par_c(a, b, c):
    v = a * b + c
    return QQ(f"Without calculating, decide whether ${a}\\times{b}+{c}$ is even or odd, and give a reason.", f"${a}\\times{b}$ is {par(a * b)} ({par(a)} $\\times$ {par(b)})", f"${c}$ is {par(c)}", f"The sum is {par(v)}")
EASY_C = ([kap_c(n) for n in (3524, 8153, 4271, 6309, 7502, 9631)] + [cons3(S) for S in (48, 75, 102, 123, 87, 156)]
          + [par_c(*t) for t in [(13, 7, 4), (12, 9, 5), (15, 11, 8), (8, 6, 9), (21, 3, 7), (14, 5, 10)]])
def rev_d(a, b):
    N = 10 * a + b; R = 10 * b + a
    return QQ(f"Take the two-digit number ${N}$. Add it to its reverse, show that the sum is divisible by 11 and find the quotient.", f"Reverse $={R}$", f"Sum $={N}+{R}={N + R}$", f"${N + R}=11\\times{a + b}$", f"Divisible by 11; quotient $={a + b}$")
def col_d(n):
    s = collatz(n)
    return QQ(f"Write the Collatz sequence starting from ${n}$. Find the number of steps to reach 1, the largest number reached and how many even numbers occur.", f"Sequence: {seq(s)}", f"Steps $={len(s) - 1}$", f"Largest number $={max(s)}$", f"Even numbers: ${sum(1 for x in s if x % 2 == 0)}$", "Ends in the loop 4, 2, 1")
EASY_D = [rev_d(a, b) for a, b in [(2, 6), (4, 7), (3, 8), (5, 9), (1, 4), (6, 8)]] + [col_d(n) for n in (9, 11, 12, 13, 14, 15)]

def small_star(pre, post, k):
    for d in range(10):
        if dsum(int(f"{pre}{d}{post}")) % k == 0: return d
# ------------------------------------------------ NCERT
nA1 = [nn(f"A two-digit number has digits ${a}$ and ${b}$. The sum of the number and its reverse is:", 11 * (a + b), "Sum $=11(a+b)$.") for a, b in [(2, 5), (3, 6), (4, 8), (6, 7)]]
nA2 = [nn(f"A two-digit number has digits ${a}$ (tens) and ${b}$ (units). Number minus its reverse is:", 9 * (a - b), "Difference $=9(a-b)$.") for a, b in [(9, 2), (7, 3), (6, 1), (8, 5)]]
nA3 = [nn(f"The number of steps the Collatz sequence from ${n}$ takes to reach 1 is:", len(collatz(n)) - 1, "List the terms and count the steps.") for n in (5, 6, 7, 10)]
nA4 = [nn(f"The smallest digit $*$ making ${a}*{b}$ divisible by 9 is:", small_star(a, b, 9), "Digit sum must be a multiple of 9.") for a, b in [("4", "3"), ("8", "4"), ("6", "7"), ("1", "3")]]
nA5 = [nn(f"The sum $1+2+3+\\dots+{n}$ is:", tri(n), "Triangular number $\\frac{n(n+1)}{2}$.") for n in (10, 20, 30, 40)]
nA6 = [tm(t, c, w, "Recall the divisibility test.") for t, c, w in [
    ("A number is divisible by 5 if its last digit is:", "0 or 5", ["0 or 2", "5 only", "any odd digit"]),
    ("A number is divisible by 2 if its last digit is:", "0, 2, 4, 6 or 8", ["0 or 5", "any odd digit", "1, 3 or 7"]),
    ("A number is divisible by 10 if its last digit is:", "0", ["5", "0 or 5", "any even digit"]),
    ("A number is divisible by 3 if:", "its digit sum is divisible by 3", ["its last digit is 3", "its last digit is even", "its digits are all odd"]),
    ("A number is divisible by 9 if:", "its digit sum is divisible by 9", ["its digit sum is divisible by 3", "its last digit is 9", "its last digit is 0"])]]
nA7 = [nn(f"The sum of five consecutive numbers with middle number ${m}$ is:", 5 * m, "Pairs around the middle cancel out.") for m in (8, 13, 20, 31)]
nA8 = [tm(f"The largest number that can be made using the digits ${' , '.join(sorted(str(n), reverse=True))}$ once each is:".replace(" , ", ", "), "".join(sorted(str(n), reverse=True)), ["".join(sorted(str(n))), str(n), "".join(sorted(str(n), reverse=True))[::-1][:2] + "".join(sorted(str(n), reverse=True))[:2]], "Write the digits in decreasing order.") for n in (3715, 8204, 6931)]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]

def why_b(a, b):
    return QQ(f"Show that $(10a+b)+(10b+a)=11(a+b)$ and verify for $a={a}$, $b={b}$.", "$10a+b+10b+a=11a+11b$", "$=11(a+b)$", f"For $a={a},b={b}$: ${10 * a + b}+{10 * b + a}={11 * (a + b)}=11\\times{a + b}$")
def star_b(pat, pos_before, pos_after):
    for d in range(1, 9):
        if dsum(int(f"{pos_before}{d}{pos_after}")) % 9 == 0: break
    N = f"{pos_before}{d}{pos_after}"
    return QQ(f"Find the digit $*$ so that ${pos_before}*{pos_after}$ is divisible by 9.", f"Known digit sum $={dsum(int(pos_before + pos_after))}$", f"Total $=({dsum(int(pos_before + pos_after))}+*)$ must be a multiple of 9", f"$*={d}$", f"Check: ${N}$ has digit sum ${dsum(int(N))}$")
def even5_b(m):
    nums = [m - 4, m - 2, m, m + 2, m + 4]
    return QQ(f"The sum of five consecutive even numbers is ${5 * m}$. Find the numbers.", f"Middle number $={5 * m}\\div5={m}$", f"The numbers are {seq(nums)}", f"Check: sum $={sum(nums)}$")
NCERT_B = ([why_b(a, b) for a, b in [(3, 5), (4, 7), (2, 9), (6, 1)]]
           + [star_b(None, x, y) for x, y in [("4", "27"), ("73", "5"), ("1", "962"), ("58", "1")]]
           + [even5_b(m) for m in (22, 36, 14, 50)])
def kap2(n):
    p = kap_path(n)[:3]
    b1, s1, d1 = kap(p[0]); b2, s2, d2 = kap(p[1])
    return QQ(f"Apply Kaprekar's routine twice to ${n}$.", f"Step 1: ${b1}-{str(s1).zfill(4)}={d1}$", f"Step 2: ${b2}-{str(s2).zfill(4)}={d2}$", f"After two steps the number is ${d2}$")
def rac_c(n):
    sums = rac(n); lines = []; cur = n
    for s in sums: lines.append(f"${cur}+{rev(cur)}={s}$"); cur = s
    return QQ(f"Find how many reverse-and-add steps turn ${n}$ into a palindrome, showing each step.", "; ".join(lines), f"Number of steps $={len(sums)}$", f"Palindrome: ${sums[-1]}$")
def sum3_c(S):
    if S % 3 == 0:
        m = S // 3
        return QQ(f"Can ${S}$ be written as the sum of three consecutive numbers? If yes, find them.", f"Sum of three consecutive numbers $=3\\times$ middle", f"${S}\\div3={m}$ is a whole number, so yes", f"The numbers are ${m - 1},{m},{m + 1}$")
    return QQ(f"Can ${S}$ be written as the sum of three consecutive numbers? If yes, find them.", "Sum of three consecutive numbers $=3\\times$ middle, a multiple of 3", f"Digit sum of ${S}$ is ${dsum(S)}$, not a multiple of 3", f"${S}$ is not a multiple of 3, so it cannot be written in this way")
NCERT_C = [kap2(n) for n in (5296, 2751, 8420, 6082, 3951, 7136)] + [rac_c(n) for n in (57, 49, 59, 38, 18, 26)] + [sum3_c(S) for S in (63, 100, 111, 145, 150, 98)]
def rev3_d(a, b, c):
    N = 100 * a + 10 * b + c; R = 100 * c + 10 * b + a
    return QQ(f"For the three-digit number ${N}$, find its reverse, the difference, and show that the difference is divisible by 99.", f"Reverse $={R}$", f"Difference $={N}-{R}={N - R}$", f"$={99}\\times{(N - R) // 99}$", f"In general $100a+c-100c-a=99(a-c)$", "So the difference is always a multiple of 99")
def col_cnt(n):
    s = collatz(n); h = sum(1 for x in s[:-1] if x % 2 == 0); t = len(s) - 1 - h
    return QQ(f"Write the Collatz sequence from ${n}$. Count how many times the number is halved and how many times it is tripled and increased by 1.", f"Sequence: {seq(s)}", f"Halvings $={h}$", f"Triple-and-add-1 steps $={t}$", f"Total steps $={len(s) - 1}$")
NCERT_D = [rev3_d(*t) for t in [(7, 3, 2), (9, 4, 5), (8, 1, 3), (6, 5, 1), (9, 0, 4), (5, 2, 1)]] + [col_cnt(n) for n in (17, 19, 21, 22, 24, 25)]

# ------------------------------------------------ MEDIUM
mA1 = [nn(f"The smallest digit $*$ making ${a}*{b}$ divisible by 3 is:", small_star(a, b, 3), "Digit sum must be a multiple of 3.") for a, b in [("5", "48"), ("7", "21"), ("26", "5"), ("91", "4")]]
mA2 = [nn(f"The Collatz sequence from ${n}$ (including ${n}$ and 1) has how many terms?", len(collatz(n)), "Count the terms.") for n in (8, 11, 14, 16)]
mA3 = [nn(f"Applying Kaprekar's routine once to ${n}$ gives:", kap(n)[2], "Largest arrangement minus smallest arrangement.") for n in (4172, 9360, 5018, 2943)]
mA4 = [nn(f"The number of ${k}$-digit palindromes is:", {2: 9, 3: 90, 4: 90, 5: 900}[k], "The first half decides the number.") for k in (2, 3, 4, 5)]
mA5 = [nn(f"The sum of {k} consecutive numbers starting at ${s}$ is:", sum(range(s, s + k)), "Use the middle number times the count when the count is odd.") for s, k in [(10, 5), (21, 3), (16, 7), (7, 9)]]
mA6 = [tm(t, c, w, "Test with small values of $n$.") for t, c, w in [
    ("For every whole number $n$, $n^2+n$ is always:", "even", ["odd", "a multiple of 3", "a prime number"]),
    ("For every whole number $n$, $2n+1$ is always:", "odd", ["even", "a multiple of 3", "a multiple of 4"]),
    ("For every whole number $n$, $n+(n+1)$ is always:", "odd", ["even", "a multiple of 3", "a perfect square"]),
    ("For every whole number $n$, $4n+2$ is always:", "even but not a multiple of 4", ["odd", "a multiple of 4", "a multiple of 3"])]]
def dv(S): return "both 3 and 9" if S % 9 == 0 else ("3 but not 9" if S % 3 == 0 else "neither 3 nor 9")
mA7 = [tm(f"A number has digit sum ${S}$. It is divisible by:", dv(S), [x for x in ["both 3 and 9", "3 but not 9", "neither 3 nor 9", "9 but not 3"] if x != dv(S)][:3], "Use the digit-sum tests.") for S in (12, 18, 20, 27)]
mA8 = [nn(f"Adding ${n}$ and its reverse gives:", n + rev(n), "Reverse the digits, then add.") for n in (72, 385, 4026)]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]

def star9(pre, post):
    d = next(d for d in range(1, 9) if dsum(int(f"{pre}{d}{post}")) % 9 == 0); T = dsum(int(pre + post))
    return QQ(f"The number ${pre}*{post}$ is divisible by 9. Find the digit $*$ and write the number.", f"Digit sum $={T}+*$", f"Must be a multiple of 9, so $*={d}$", f"Number $={pre}{d}{post}$")
def odd3(S):
    m = S // 3
    return QQ(f"The sum of three consecutive odd numbers is ${S}$. Find them.", f"Middle odd number $={S}\\div3={m}$", f"Others differ by 2: ${m - 2}$ and ${m + 2}$", f"Numbers: ${m - 2}, {m}, {m + 2}$", f"Check sum $={3 * m}$")
def rac_m(n):
    sums = rac(n); lines = []; cur = n
    for s in sums: lines.append(f"${cur}+{rev(cur)}={s}$"); cur = s
    return QQ(f"Use reverse-and-add on ${n}$ and state how many steps are needed to get a palindrome.", "; ".join(lines), f"Steps $={len(sums)}$; palindrome ${sums[-1]}$")
MED_B = [star9(a, b) for a, b in [("5", "14"), ("62", "7"), ("3", "86"), ("81", "6")]] + [odd3(S) for S in (51, 87, 117, 159)] + [rac_m(n) for n in (39, 58, 153, 162)]
def kap_full(n):
    p = kap_path(n); lines = []
    for x in p[:-1]:
        b, s, d = kap(x); lines.append(f"${b}-{str(s).zfill(4)}={d}$")
    return QQ(f"Apply Kaprekar's routine to ${n}$ repeatedly until you reach 6174.", "; ".join(lines), f"Steps needed $={len(p) - 1}$")
def digpuz(S, d):
    a, b = (S // 11 + d) // 2, (S // 11 - d) // 2
    return QQ(f"The sum of a two-digit number and its reverse is ${S}$, and its digits differ by ${d}$. Find the number (tens digit larger).", f"$11(a+b)={S}$, so $a+b={S // 11}$", f"$a-b={d}$", f"$a={a}$, $b={b}$", f"Number $={10 * a + b}$")
def consec_k(N, k):
    m = N // k; first = m - k // 2
    return QQ(f"Write ${N}$ as the sum of {k} consecutive numbers.", f"Middle number $={N}\\div{k}={m}$", f"First number $={m}-{k // 2}={first}$", f"Numbers: {seq(list(range(first, first + k)))}", f"Check sum $={N}$")
MED_C = ([kap_full(n) for n in (7621, 9810, 5432, 1827, 8531, 4852)]
         + [digpuz(*t) for t in [(99, 3), (121, 1), (110, 4), (143, 5), (88, 6), (77, 5)]]
         + [consec_k(*t) for t in [(75, 5), (63, 7), (99, 9), (84, 3), (130, 5), (105, 7)]])
def col_m(n):
    s = collatz(n); ev = sum(1 for x in s if x % 2 == 0)
    return QQ(f"Write the Collatz sequence from ${n}$. Find the largest number reached, the number of even terms and the number of odd terms.", f"Sequence: {seq(s)}", f"Largest $={max(s)}$", f"Even terms $={ev}$", f"Odd terms $={len(s) - ev}$", f"Total terms $={len(s)}$")
def pal3(a):
    ps = [100 * a + 10 * b + a for b in range(10) if (2 * a + b) % 3 == 0]
    return QQ(f"List all three-digit palindromes with first digit ${a}$ that are divisible by 3.", f"Palindrome form ${a}b{a}$ with digit sum $=2\\times{a}+b$", f"Need ${2 * a}+b$ to be a multiple of 3", f"Possible $b$: {seq([b for b in range(10) if (2 * a + b) % 3 == 0])}", f"Palindromes: {seq(ps)}")
MED_D = [col_m(n) for n in (7, 20, 21, 22, 24, 18)] + [pal3(a) for a in (1, 2, 4, 5, 7, 8)]

# ------------------------------------------------ HARD
def small_k(k): return next(n for n in range(10 ** (k - 1), 10 ** k) if n % 9 == 0)
hA1 = [nn(f"The smallest {k}-digit number divisible by 9 is:", small_k(k), "Find the first multiple of 9.", offs=(1, -1, 9, -9, 18, 10)) for k in (3, 4, 5)]
def largest_distinct(div):
    return max(int("".join(p)) for p in permutations("0123456789", 4) if p[0] != "0" and int("".join(p)) % div == 0)
hA2 = [nn(f"The largest 4-digit number with all digits different that is divisible by {d} is:", largest_distinct(d), "Start from 9876 and test downwards.", offs=(1, -1, 2, -2, 10, -10)) for d in (9, 5, 10, 3)]
hA3 = [nn(f"Kaprekar's routine on ${n}$ reaches 6174 after how many steps?", len(kap_path(n)) - 1, "Repeat the routine and count.") for n in (2111, 6321, 1459, 4176)]
hA4 = [nn(f"The Collatz sequence from ${n}$ needs how many steps to reach 1?", len(collatz(n)) - 1, "Follow the rule term by term.") for n in (12, 15, 17, 19)]
hA5 = [tm(t, c, w, "Test with small values.") for t, c, w in [
    ("For every whole number $n$, $n(n+1)$ is:", "even", ["odd", "a multiple of 3", "a perfect square"]),
    ("For every whole number $n$, $n+(n+1)+(n+2)$ is always a multiple of:", "3", ["2", "4", "6"]),
    ("For every whole number $n$, $6n+3$ is:", "an odd multiple of 3", ["even", "a multiple of 6", "a multiple of 9"]),
    ("A two-digit number plus its reverse is always a multiple of:", "11", ["9", "10", "7"])]]
hA6 = [nn(f"If $1+2+3+\\dots+n={tri(n)}$, then $n$ is:", n, "Triangular numbers: $n(n+1)/2$.", offs=(1, -1, 2, -2, 5, 10)) for n in (21, 28, 36, 45, 15)]
hA7 = [nn(f"The number of reverse-and-add steps for ${n}$ to become a palindrome is:", len(rac(n)), "Add the reverse each time.") for n in (59, 79, 69, 68)]
hA8 = [tm("Which expression is a multiple of 9 for every digit pair $(a,b)$ with $a>b$?", "$(10a+b)-(10b+a)$", ["$(10a+b)+(10b+a)$", "$10a+b$", "$a+b$"], "Difference of a number and its reverse is $9(a-b)$.")]
hA8 += [tm("Which expression is a multiple of 11 for every digit pair $(a,b)$?", "$(10a+b)+(10b+a)$", ["$(10a+b)-(10b+a)$", "$10a+b$", "$a-b$"], "The sum is $11(a+b)$.")]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]

def sumdiff(S, D):
    a, b = (S // 11 + D // 9) // 2, (S // 11 - D // 9) // 2
    return QQ(f"A two-digit number added to its reverse gives ${S}$ and subtracted from it gives ${D}$. Find the number.", f"$11(a+b)={S}$ so $a+b={S // 11}$", f"$9(a-b)={D}$ so $a-b={D // 9}$", f"$a={a}$, $b={b}$", f"Number $={10 * a + b}$")
def nnp(n):
    return QQ(f"Show that $n(n+1)$ is even, and verify for $n={n}$.", f"If $n$ is even, $n(n+1)$ is even $\\times$ odd, so even", "If $n$ is odd, $n+1$ is even, so the product is even", f"For $n={n}$: ${n}\\times{n + 1}={n * (n + 1)}$, which is even")
def best_arr(ds, div):
    ok = [int("".join(p)) for p in permutations(ds) if p[0] != "0" and int("".join(p)) % div == 0]
    return QQ(f"Using each of the digits ${', '.join(ds)}$ once, make the largest 4-digit number divisible by {div}.", f"Digit sum $={sum(map(int, ds))}$", f"Divisibility by {div} {'is satisfied by every arrangement' if div in (3, 9) else 'needs the right last digit'}", f"Largest arrangement: ${max(ok)}$")
HARD_B = [sumdiff(*t) for t in [(110, 36), (143, 45), (121, 63), (99, 27)]] + [nnp(n) for n in (13, 24, 37, 50)] + [best_arr(d, k) for d, k in [("7341", 3), ("6410", 5), ("9482", 2), ("8541", 9)]]
def star2(pre, mid, post):
    sols = [d for d in range(10) if dsum(int(f"{pre}{d}{mid}{d}{post}")) % 9 == 0]
    T = dsum(int(pre + mid + post))
    return QQ(f"The number ${pre}*{mid}*{post}$ has the same digit $*$ in both blanks and is divisible by 9. Find all possible values of $*$.", f"Digit sum $={T}+2\\times*$", f"Need a multiple of 9", f"Possible $*$: {seq(sols)}", f"Numbers: {seq([int(f'{pre}{d}{mid}{d}{post}') for d in sols])}")
def kap_hard(n):
    p = kap_path(n); lines = []
    for x in p[:-1]:
        b, s, d = kap(x); lines.append(f"${b}-{str(s).zfill(4)}={d}$")
    return QQ(f"Start with ${n}$ and apply Kaprekar's routine until 6174 appears. Show every step.", "; ".join(lines), f"Steps $={len(p) - 1}$ and the sequence is {seq(p)}")
def ways(N):
    out = []
    for k in range(2, N):
        top = N - k * (k - 1) // 2
        if top > 0 and top % k == 0:
            f = top // k; out.append(list(range(f, f + k)))
    return out
def ways_q(N):
    w = ways(N)
    return QQ(f"In how many ways can ${N}$ be written as the sum of two or more consecutive positive whole numbers? List them.", "Try 2, 3, 4, ... numbers in turn", "; ".join("$" + "+".join(map(str, x)) + "$" for x in w), f"Number of ways $={len(w)}$")
HARD_C = ([star2(*t) for t in [("4", "3", "6"), ("7", "2", "1"), ("5", "8", "4"), ("3", "6", "9"), ("8", "1", "5"), ("2", "7", "3")]]
          + [kap_hard(n) for n in (1235, 1259, 1279, 1327, 1368, 1374)]
          + [ways_q(N) for N in (15, 21, 27, 33, 36, 45)])
def rac_hard(n):
    sums = rac(n); lines = []; cur = n
    for s in sums: lines.append(f"${cur}+{rev(cur)}={s}$"); cur = s
    return QQ(f"Use reverse-and-add on ${n}$ until a palindrome is formed. Show each step, state the number of steps and the final palindrome.", "; ".join(lines), f"Steps $={len(sums)}$", f"Palindrome $={sums[-1]}$")
def ktimes(k):
    sol = [10 * a + b for a in range(1, 10) for b in range(10) if 10 * a + b == k * (a + b)]
    return QQ(f"Find all two-digit numbers that are exactly {k} times the sum of their digits.", f"$10a+b={k}(a+b)$", f"Simplify: ${10 - k}a={str(k - 1) if k > 2 else ''}b$", f"Check digit pairs: numbers {seq(sol)}", f"Number of such numbers $={len(sol)}$; their sum $={sum(sol)}$")
HARD_D = [rac_hard(n) for n in (69, 155, 164, 174, 195, 156)] + [ktimes(k) for k in (2, 3, 4, 5, 6, 8)]

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
