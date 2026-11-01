from math import gcd
from lib import mcq, Q, OR
from mk9 import M4, build

AR_OPTS = ["Both A and R are true and R is the correct explanation of A",
           "Both A and R are true but R is not the correct explanation of A",
           "A is true but R is false",
           "A is false but R is true"]
def AR(a, r, ans, why):
    return mcq(f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}", list(AR_OPTS), ans, why)

# ---------- helper algorithms (used to compute every numeric answer) ----------
def divisors(n):
    return [j for j in range(1, n + 1) if n % j == 0]
def sub_steps(m, n):
    """number of times Step 3 of Euclid's subtraction algorithm is applied"""
    c = 0
    while True:
        if m < n: m, n = n, m
        if n == 0: return c, m
        m, n = n, m - n; c += 1
def div_steps(m, n):
    c = 0
    while True:
        if m < n: m, n = n, m
        if n == 0: return c, m
        m, n = n, m % n; c += 1
def carries(a, b):
    x, y = str(a)[::-1], str(b)[::-1]; L = max(len(x), len(y)); c = 0; n = 0; seq = []
    for i in range(L):
        s = (int(x[i]) if i < len(x) else 0) + (int(y[i]) if i < len(y) else 0) + c
        c = 1 if s >= 10 else 0; n += c; seq.append(c)
    return n, seq
def dist(vals, c):
    out = []
    for v in vals:
        if v != c and v >= 0 and v not in out: out.append(v)
    return out
assert sub_steps(825, 375) == (7, 75) and div_steps(60, 16) == (3, 4) and div_steps(99, 2) == (2, 1)
assert divisors(18) == [1, 2, 3, 6, 9, 18]

A = []; B = []; C = []; D = []
# ---------------- A: conceptual (12) ----------------
A += [
 M4("An algorithm is best described as:", "a precise step-by-step procedure that solves a problem", ["a single number obtained by guessing", "a table of answers learnt by heart", "a calculator button"], "definition of an algorithm"),
 M4("In the column-addition algorithm, the basic step we assume we can do directly is:", "adding two single-digit numbers", ["adding two 10-digit numbers", "counting dots one by one", "dividing by 10"], "algorithms are built from basic steps we can already perform"),
 M4("While adding two numbers digit by digit, the carry from any column can never exceed 1 because:", "the largest possible column total is 9 + 9 + 1 = 19", ["the digits are always less than 5", "carry is always reset to 0", "the numbers are written in base 5"], "19 = 9 + 10 so carry is at most 1"),
 M4("If Step 5 (writing the final carry) is skipped, then 856 + 479 would be written as:", "335", ["1335", "1235", "3350"], "the leading 1 of 1335 is lost"),
 M4("In the addition algorithm the digits are aligned from the right because:", "units must be added to units, tens to tens, and so on", ["the right digit is the largest", "we read numbers from right to left", "carries move to the right"], "place-value grouping"),
 M4("When we move from adding 3-digit numbers to adding 5-digit numbers, which statement is correct?", "counting dots needs about 100 times as many dots, but the column method needs only 2 more columns", ["counting dots needs 2 times as many dots and the column method 100 times as many steps", "both methods need about 100 times as much work", "both methods need only 2 more steps"], "dots grow with the value, columns grow with the number of digits"),
 M4("At the start of the algorithm for the divisors of n, the list-of-divisors is:", "empty", ["[1]", "[n]", "[1, n]"], "we do not yet know any divisor"),
 M4("A list, which is used to store divisors in order, is an example of a:", "data structure", ["theorem", "fraction", "variable"], "data structures organise information"),
 M4("Euclid's subtraction algorithm is based on the fact that for m ≥ n, gcd(m, n) equals:", "gcd(n, m − n)", ["gcd(m, m + n)", "gcd(m − n, m + n)", "gcd(m × n, n)"], "every common divisor of m and n also divides m − n"),
 M4("In Euclid's algorithm the answer is reported as m when we reach gcd(m, n) with:", "n = 0", ["n = 1", "m = n + 1", "m = 0"], "gcd(m, 0) = m"),
 M4("The ‘long division’ method of finding the gcd using Indian place-value numerals is found in the work of:", "Āryabhaṭa", ["Al-Khwārizmī", "Euclid", "Archimedes"], "Āryabhaṭīya, 499 CE"),
 M4("The word ‘algorithm’ is derived from the name of:", "Al-Khwārizmī", ["Euclid", "Āryabhaṭa", "Pythagoras"], "Algoritmi → algorism → algorithm"),
]
# ---------------- A: A-R (4) ----------------
A += [
 AR("Euclid's subtraction algorithm finds gcd(375, 825) = 75.", "Every common divisor of m and n is also a common divisor of n and m − n, and conversely.", "a", "the set of common divisors does not change at each reduction"),
 AR("The division algorithm of Āryabhaṭa needs fewer reductions than Euclid's subtraction algorithm for gcd(99, 2).", "Repeated subtraction of 2 from 99 is replaced by one division giving the remainder.", "a", "99 mod 2 = 1 in one step"),
 AR("The simplest gcd algorithm that scans every j from 1 to min(m, n) takes 10 times as much work when the smaller number goes from 3 digits to 4 digits.", "The work of that algorithm is proportional to the digits of the numbers.", "c", "work is proportional to the value, not to the number of digits"),
 AR("In the addition algorithm, the carry is never more than 1.", "The sum of two digits and a carry of at most 1 is at most 19.", "a", "so the units digit is written and 1 carried"),
]
# ---------------- A: computed items (24) ----------------
for a, b in [(478, 385), (999, 1), (2764, 3589), (268, 175), (7777, 3333)]:
    n, seq = carries(a, b); assert a + b == int(str(a + b))
    A.append(M4(f"While adding {a} and {b} by the column algorithm, the number of columns that produce a carry of 1 is:", f"{n}", [str(x) for x in dist([n + 1, max(n - 1, 0), n + 2, 0, 1, 2], n)][:3], f"carries by column: {seq}"))
for m, n in [(375, 825), (1001, 143), (84, 60), (252, 198)]:
    g = gcd(m, n)
    A.append(M4(f"By Euclid's algorithm, gcd({m}, {n}) is:", f"{g}", [str(x) for x in dist([g * 2, max(g // 2, 1), g + 1, g + 2, 1, 3], g)][:3], f"repeated reduction ends at gcd({g}, 0)"))
for m, n in [(825, 375), (21, 6), (50, 8), (35, 10)]:
    s, g = sub_steps(m, n)
    A.append(M4(f"The number of times Step 3 of Euclid's subtraction algorithm is applied while computing gcd({m}, {n}) is:", f"{s}", [str(x) for x in dist([s + 1, s + 2, max(s - 1, 1), s + 3, s * 2], s)][:3], f"the chain of reductions ends at gcd({g}, 0)"))
for m, n in [(60, 16), (99, 2), (825, 375)]:
    s, g = div_steps(m, n)
    A.append(M4(f"Using the long-division (Āryabhaṭa) form of Euclid's algorithm, the number of reductions needed for gcd({m}, {n}) is:", f"{s}", [str(x) for x in dist([s + 1, s + 2, max(s - 1, 1), s + 3], s)][:3], f"each reduction replaces (m, n) by (n, m mod n); ends at gcd({g}, 0)"))
for n in [18, 36]:
    d = divisors(n)
    A.append(M4(f"The list of divisors of {n} produced by the divisor algorithm has how many entries?", f"{len(d)}", [str(x) for x in dist([len(d) + 1, len(d) - 1, len(d) + 2, len(d) * 2], len(d))][:3], f"divisors({n}) = {d}"))
for m, n in [(54000, 81000), (12, 30)]:
    A.append(M4(f"The improved gcd algorithm that keeps most-recent-common-divisor scans k from 2 up to min({m}, {n}). The number of values of k scanned is:", f"{min(m, n) - 1}", [str(min(m, n)), str(min(m, n) - 2), str(max(m, n) - 1)], "values 2, 3, …, min(m, n)"))
A.append(M4("The prime divisors of 60 (from divisors(60) = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]) are:", "2, 3, 5", ["1, 2, 3, 5", "2, 3, 4, 5", "2, 3, 5, 6"], "prime divisors have exactly two divisors; 1 is not prime"))
A.append(M4("The prime divisors of 90 (from divisors(90) = [1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90]) are:", "2, 3, 5", ["2, 3, 5, 9", "1, 2, 3, 5", "3, 5, 9"], "9 = 3 × 3 is not prime"))
for m, n in [(375, 825), (60, 24)]:
    cd = [x for x in divisors(m) if n % x == 0]
    A.append(M4(f"The list of common divisors of {m} and {n}, in increasing order, ends with:", f"{cd[-1]}", [str(x) for x in dist([max(m, n), min(m, n) // 2 + 1, cd[-1] + 1, cd[-2] if len(cd) > 1 else 2], cd[-1])][:3], "the rightmost element is the gcd"))
assert len(A) == 40, len(A)

# ---------------- B (16) ----------------
B += [
 Q(r"Define an algorithm and give one example from this chapter.", r"An algorithm is a step-by-step procedure that leads to the answer of a problem (1). Example: the digit-by-digit addition algorithm / Euclid's gcd algorithm (1).", "1+1"),
 Q(r"Add 5987 and 4376 using the column algorithm and state in which columns a carry is generated.", r"Sum $=10363$ (1). Carries: units (7+6=13), tens (8+7+1=16), hundreds (9+3+1=13) and thousands (5+4+1=10) — all four columns; the last carry is written as the leading 1 (1).", "1+1"),
 Q(r"Why is the final carry written in Step 5 of the addition algorithm? Give an example in which omitting it gives a wrong answer.", r"After the leftmost column a carry of 1 may remain; if not written, a place value is lost (1). E.g. $95+17=112$, but without Step 5 we get $12$ (1).", "1+1"),
 Q(r"Execute the divisor algorithm for 20 and write the final list.", r"Check j = 1, 2, …, 20: 1, 2, 4, 5, 10, 20 divide 20 (1). List $=[1, 2, 4, 5, 10, 20]$ (1).", "1+1"),
 Q(r"How many numbers must be checked to compute divisors(n) by the algorithm of the chapter? Why can the list of divisors be in increasing order?", r"All $j=1,2,\ldots,n$ — that is $n$ numbers (1). We test j in increasing order and append at the end, so the list stays in increasing order (1).", "1+1"),
 Q(r"Compute gcd(48, 18) by listing the common divisors.", r"divisors(48) $=[1,2,3,4,6,8,12,16,24,48]$, divisors(18) $=[1,2,3,6,9,18]$ (1). Common $=[1,2,3,6]$; gcd $=6$ (1).", "1+1"),
 Q(r"What is the first improvement made to the gcd algorithm in Section 11.3.1? How many numbers need checking after it?", r"Both lists of divisors are found in one scan of $j$ from 1 to $\max(m,n)$ (1), so $\max(m,n)$ numbers are checked instead of $m+n$ (1).", "1+1"),
 Q(r"Why is it enough to check common divisors only up to min(m, n)?", r"A common divisor divides both numbers, so it cannot be larger than the smaller number (2).", "2"),
 Q(r"State Euclid's observation used to reduce gcd(m, n), where m ≥ n.", r"$\gcd(m,n)=\gcd(n,\,m-n)$ (1); every common divisor of $m$ and $n$ divides $m-n$ and conversely (1).", "1+1"),
 Q(r"Apply Euclid's subtraction algorithm to gcd(18, 12). Write the sequence of pairs.", r"$(18,12)\to(12,6)\to(6,6)\to(6,0)$ (1); gcd $=6$ (1).", "1+1"),
 Q(r"Compute gcd(60, 16) by the long-division (division) algorithm.", r"$60 = 16\times3+12$; $16=12\times1+4$; $12=4\times3+0$ (1). gcd $=4$ (1).", "1+1"),
 Q(r"What is 17 mod 5 and 33 mod 7? What do they represent?", r"$17\bmod5=2$ and $33\bmod7=5$ (1). They are the remainders on division (1).", "1+1"),
 Q(r"Why does gcd(99, 2) need many steps in Euclid's subtraction algorithm but only two in the division algorithm?", r"Subtraction removes 2 each time (about 49 reductions) (1); division removes all the 2s at once by taking $99\bmod2=1$ (1).", "1+1"),
 Q(r"Write a short note on the origin of the word ‘algorithm’.", r"Al-Khwārizmī (c. 820 CE) wrote on Indian numerals; the Latin form of his name, Algoritmi, gave algorismus → algorism → algorithm (2).", "2"),
 Q(r"Write an algorithm prime(n) to test whether n is prime, using divisors(n).", r"Compute divisors(n) (1). If the list has exactly two entries (1 and n), report ‘prime’; otherwise ‘not prime’ (1).", "1+1"),
 Q(r"The prime factorisation of 180 is $2^2\times3^2\times5^1$. Suggest a way to store it as a list and give the list.", r"Store (prime, power) pairs: $[(2,2),(3,2),(5,1)]$ (2).", "2"),
]
assert len(B) == 16, len(B)

# ---------------- C (24) ----------------
C += [
 Q(r"Add 7968 and 5479 following the steps of the algorithm precisely, showing the carry in each column.", r"Units $8+9=17$: write 7, carry 1 (1). Tens $6+7+1=14$: write 4, carry 1 (1). Hundreds $9+4+1=14$: write 4, carry 1; thousands $7+5+1=13$: write 3, carry 1; final carry written: sum $=13447$ (1).", "1+1+1"),
 Q(r"What happens when a 5-digit number is added to a 3-digit number by this algorithm? Explain how the steps handle it.", r"The numbers are aligned on the right (1). Once the digits of the shorter number are exhausted, the missing places are treated as 0 and only carries are added (1), e.g. $99\,999+123=100\,122$ is handled correctly (1).", "1+1+1"),
 Q(r"Explain why the column-addition algorithm gives the correct sum.", r"Each number is grouped into units, tens, hundreds … (1). We add each group separately (1). Whenever a group of ten forms in a column, it is carried to the next higher place (1).", "1+1+1"),
 Q(r"Compare the time to add 3347 + 2729 by counting dots (1 dot per second) with the time by the column method (15 seconds per single-digit addition with carry).", r"Counting: $3347+2729=6076$ dots, about $6076$ s, over 1 h 40 min (1). Column method: 4 columns × 15 s $=60$ s (1). Column method is far faster; its time grows with the number of digits (1).", "1+1+1"),
 Q(r"Execute the divisor algorithm for 28 and write list-of-divisors after j = 1, 2, 4, 7 and at the end.", r"After j=1: [1]; j=2: [1,2]; j=4: [1,2,4]; j=7: [1,2,4,7] (2). Final: [1, 2, 4, 7, 14, 28] (1).", "2+1"),
 Q(r"Find the common divisors of 36 and 60 by the algorithm of Section 11.2.3 and hence gcd(36, 60).", r"divisors(36) $=[1,2,3,4,6,9,12,18,36]$; divisors(60) $=[1,2,3,4,5,6,10,12,15,20,30,60]$ (1). Common $=[1,2,3,4,6,12]$ (1). gcd $=12$ (1).", "1+1+1"),
 Q(r"Describe how the last improved gcd algorithm (using most-recent-common-divisor) works. Apply it to m = 8, n = 12.", r"Start with most-recent-common-divisor $=1$; for each $k$ from 2 to $\min(m,n)$, if $k$ divides both, update it to $k$ (1). $\min=8$: $k=2$ ✓ → 2; $k=3$ ✗; $k=4$ ✓ → 4; $k=5,6,7$ ✗; $k=8$ ✗ (does not divide 12) (1). gcd $=4$ (1).", "1+1+1"),
 Q(r"Why does the work in the divisor-scan gcd algorithm grow 10 times when the smaller number goes from 3 digits to 4 digits? Why is this a drawback?", r"It scans every value from 1 to $\min(m,n)$, and a 4-digit number is about 10 times as large as a 3-digit one (1, 1). Work is proportional to the value, not to the number of digits, so it is slow for large numbers (1).", "1+1+1"),
 Q(r"Prove: if d divides both m and n (m ≥ n), then d divides m − n.", r"Write $m=ad$, $n=bd$ for natural numbers $a,b$ (1). $m-n=ad-bd=(a-b)d$ (1). Hence $d$ divides $m-n$ (1).", "1+1+1"),
 Q(r"Prove: if d divides both n and m − n, then d divides m.", r"Write $n=xd$ and $m-n=yd$ (1). $m=n+(m-n)=xd+yd=(x+y)d$ (1). So $d$ divides $m$ (1).", "1+1+1"),
 Q(r"Compute gcd(42, 30) by Euclid's subtraction algorithm, writing each pair, and say how many times Step 3 was applied.", r"$(42,30)\to(30,12)\to(12,18)\to$ swap $(18,12)\to(12,6)\to(6,6)\to(6,0)$ (2). Step 3 is applied 5 times (the swaps are Step 1); gcd $=6$ (1).", "2+1"),
 Q(r"Show that gcd(2k + 1, 2) needs many reductions in Euclid's subtraction algorithm but only 2 in the division algorithm. Take k = 4.", r"Subtraction: $(9,2)\to(2,7)\to(7,2)\to(2,5)\to(5,2)\to(2,3)\to(3,2)\to(2,1)\to(1,1)\to(1,0)$: Step 3 is applied 6 times (2). Division: $9\bmod2=1$: $(2,1)\to(1,0)$: 2 reductions (1).", "2+1"),
 Q(r"Use the division algorithm (long division) to find gcd(825, 375) and state the number of reductions.", r"$825=375\times2+75$; $375=75\times5+0$ (2). gcd $=75$, in 2 reductions (1).", "2+1"),
 Q(r"Find gcd(2430, 1215) by the division algorithm.", r"$2430=1215\times2+0$ (2). gcd $=1215$ (1).", "2+1"),
 Q(r"Verify, for m = 33 and n = 7, that the common divisors of m and n are the same as the common divisors of n and m mod n.", r"$33\bmod7=5$ (1). Common divisors of 33 and 7: only 1 (1). Common divisors of 7 and 5: only 1; so the two sets of common divisors are the same, as claimed (1).", "1+1+1"),
 Q(r"Describe an algorithm to find the least common multiple (lcm) of two numbers m and n.", r"Examine the multiples $m,\,2m,\,3m,\ldots$ one by one (1). Stop at the first multiple that is divisible by $n$ (1). Report that multiple as the lcm (1).", "1+1+1"),
 Q(r"If List 1 and List 2 are in increasing order, write an algorithm to find elements of List 1 that are not in List 2.", r"Start with empty list $L$ (1). For each $x$ in List 1: if $x$ does not appear in List 2, append $x$ to $L$ (1). Report $L$ (1).", "1+1+1"),
 Q(r"Divisors occur in pairs. Write the divisors of 36 in pairs and state how many numbers need to be examined to find all divisors of 36.", r"Pairs: $(1,36),(2,18),(3,12),(4,9),(6,6)$ (2). Only numbers up to $6=\sqrt{36}$ need to be examined (1).", "2+1"),
 Q(r"<b>Case study:</b> A student adds 4856 and 3779 on paper. She writes 8625 as the answer. (i) Find the correct sum. (ii) In which column did she fail to add the carry? (iii) Which step of the algorithm did she ignore?", r"(i) $4856+3779=8635$ (1). (ii) The tens column: $5+7+1=13$ should give 3, but she wrote 2 (she forgot the carry 1 from $6+9=15$) (1). (iii) Step 3 (add the carry along with the digits) (1).", "1+1+1"),
 Q(r"<b>Case study:</b> Rohan lists divisors(50) = [1, 2, 5, 10, 25, 50] and divisors(75) = [1, 3, 5, 15, 25, 75]. (i) Write the list of common divisors. (ii) Find gcd(50, 75). (iii) Why is the gcd the rightmost element?", r"(i) $[1,5,25]$ (1). (ii) gcd $=25$ (1). (iii) Lists are in increasing order, so the common list is too, and the largest common divisor is last (1).", "1+1+1"),
 Q(r"<b>Case study:</b> A delivery company packs 144 apples and 108 oranges into identical boxes with no fruit left over. (i) Which gcd gives the largest number of fruits possible in each box if boxes hold only one fruit type? (ii) Compute it by the division algorithm. (iii) How many boxes of each fruit?", r"(i) gcd(144, 108) (1). (ii) $144=108\times1+36$; $108=36\times3+0$ ⇒ gcd $=36$ (1). (iii) Apples $144/36=4$ boxes, oranges $108/36=3$ boxes (1).", "1+1+1"),
 Q(r"<b>Case study:</b> Adding two numbers by counting dots takes 1 second per dot. Ria adds 3-digit numbers (about 800 dots in all). (i) How long, in minutes, for 800 dots? (ii) About how many dots for 5-digit numbers (100 times as many)? (iii) How many extra columns does the column method need for 5-digit numbers?", r"(i) $800\ \text{s}\approx13.3$ min (1). (ii) $80\,000$ dots (1). (iii) Only 2 more columns (1).", "1+1+1"),
 Q(r"<b>Case study:</b> Meera follows the algorithm: ‘Start with count = 0. For each j from 1 to 12, if j divides 12, add 1 to count.’ (i) What is the final value of count? (ii) What does count represent? (iii) Which numbers j add to count?", r"(i) $6$ (1). (ii) The number of divisors of 12 (1). (iii) j = 1, 2, 3, 4, 6, 12 (1).", "1+1+1"),
 Q(r"<b>Case study:</b> Arjun runs Euclid's subtraction algorithm on gcd(7, 3) and Āryabhaṭa's algorithm on the same pair. (i) Write the chain of pairs for subtraction. (ii) Write the chain for division. (iii) Which is shorter and by how many reductions?", r"(i) $(7,3)\to(3,4)\to(4,3)\to(3,1)\to(1,2)\to(2,1)\to(1,1)\to(1,0)$ i.e. 5 applications of Step 3 (1). (ii) $(7,3)\to(3,1)\to(1,0)$: 2 reductions (1). (iii) Division is shorter by 3 reductions (1).", "1+1+1"),
]
assert len(C) == 24, len(C)

# ---------------- D (16) ----------------
D += [
 Q(r"Write the algorithm to add two numbers digit by digit. Execute it for 6785 + 2748, showing the carry in each column, and state why Step 5 is needed.", r"Steps: align right; add the rightmost digits, write the units digit and set carry (0 or 1); add next column with carry; repeat; write a final carry (2). Execution: $5+8=13$ → 3, c=1; $8+4+1=13$ → 3, c=1; $7+7+1=15$ → 5, c=1; $6+2+1=9$ → 9, c=0; sum $=9533$ (2). Step 5 writes any leftover carry; without it, e.g. $9999+1$ would give $0000$ (1).", "2+2+1"),
 Q(r"Write the algorithm for divisors(n). Execute it for n = 24 and write the list. Why is the list in increasing order?", r"Algorithm: start with empty list; for each $j=1,2,\ldots,n$, if $j$ divides $n$, add $j$ at the end (2). For 24: $[1,2,3,4,6,8,12,24]$ (2). j is tested in increasing order and appended, so the list is increasing (1).", "2+2+1"),
 Q(r"Write the complete first algorithm for gcd(m, n) using lists of divisors. Execute it for gcd(30, 45).", r"Steps: get divisors(m), divisors(n); empty common list; for each $x$ in divisors(m), if $x$ in divisors(n) add to common; report the rightmost element (2). divisors(30) $=[1,2,3,5,6,10,15,30]$; divisors(45) $=[1,3,5,9,15,45]$ (1). Common $=[1,3,5,15]$ (1); gcd $=15$ (1).", "2+1+1+1"),
 Q(r"Describe the three successive improvements to the first gcd algorithm (Section 11.3.1) and how many numbers are checked after each for m = 36, n = 60.", r"(i) Combine the scans: check $j$ up to $\max(m,n)=60$ instead of $m+n=96$ (2). (ii) Directly compute common divisors, using up to $\min(m,n)=36$ (2). (iii) Drop lists: keep only most-recent-common-divisor, scanning $k=2$ to 36 (1).", "2+2+1"),
 Q(r"State and prove the observation behind Euclid's algorithm: for m ≥ n, gcd(m, n) = gcd(n, m − n).", r"Statement (1). Let $d$ divide $m$ and $n$: $m=ad,\ n=bd$, so $m-n=(a-b)d$ and $d$ divides $m-n$ (2). Conversely let $d$ divide $n$ and $m-n$: $n=xd$, $m-n=yd$, so $m=(x+y)d$ (1). The sets of common divisors are equal, hence the gcds are equal (1).", "1+2+1+1"),
 Q(r"Apply Euclid's subtraction algorithm to gcd(375, 825) showing every reduction (as the chapter does). State how many times Step 3 is used and why the algorithm is still slow for large inputs.", r"$(825,375)\to(375,450)\to(450,375)\to(375,75)\to(75,300)\to(300,75)\to(75,225)\to(225,75)\to(75,150)\to(150,75)\to(75,75)\to(75,0)$ (2). Step 3 used 7 times; gcd $=75$ (1). It is slow because repeated subtraction of a small number from a large one takes about as many steps as the quotient, e.g. gcd(99, 2) (2).", "2+1+2"),
 Q(r"Explain Āryabhaṭa's division algorithm. Compute gcd(2587392, 157656) by this method and give all the divisions.", r"Replace subtraction by remainder: reduce gcd(m, n) to gcd(n, m mod n) until n = 0 (2). $2587392=157656\times16+64896$; $157656=64896\times2+27864$; $64896=27864\times2+9168$ (1). $27864=9168\times3+360$; $9168=360\times25+168$; $360=168\times2+24$; $168=24\times7+0$ (1). gcd $=24$ (1).", "2+1+1+1"),
 Q(r"Compute (i) gcd(51000, 81000) by the improved Euclid algorithm, showing each division, and (ii) gcd(1789287, 237656), stating the number of reductions.", r"(i) $81000=51000\times1+30000$; $51000=30000\times1+21000$; $30000=21000\times1+9000$; $21000=9000\times2+3000$; $9000=3000\times3+0$ ⇒ gcd $=3000$ (3). (ii) The remainders are $125695, 111961, 13734, 2089, 1200, 889, 311, 267, 44, 3, 2, 1, 0$: 13 reductions, gcd $=1$ (2).", "3+2"),
 Q(r"Write an algorithm prime(n). Execute it for n = 21 and n = 23.", r"Compute divisors(n); if the list has exactly the two entries 1 and n, report prime; else not prime (2). divisors(21) $=[1,3,7,21]$ — 4 entries ⇒ not prime (1). divisors(23) $=[1,23]$ ⇒ prime (2).", "2+1+2"),
 Q(r"Write an algorithm primedivisors(n). Execute it for n = 60.", r"Compute divisors(n); keep each divisor $x$ for which divisors(x) has exactly two entries (2). divisors(60) $=[1,2,3,4,5,6,10,12,15,20,30,60]$ (1). Prime ones: $2,3,5$ (2).", "2+1+2"),
 Q(r"Use prime factorisations to compute gcd(180, 300). Show how the factorisations may be stored as lists and compared.", r"$180=2^2\cdot3^2\cdot5$, $300=2^2\cdot3\cdot5^2$ (1). Store as $[(2,2),(3,2),(5,1)]$ and $[(2,2),(3,1),(5,2)]$ (2). For each common prime take the smaller power: $2^2,3^1,5^1$ (1). gcd $=60$ (1).", "1+2+1+1"),
 Q(r"<b>Case study:</b> A tile shop has a 360 cm × 270 cm floor to cover with square tiles of the largest possible side, with no cutting. (i) Which number must the tile side be the gcd of? (ii) Compute it using the division algorithm. (iii) How many tiles are needed? (iv) How many fewer reductions does the division algorithm need than the subtraction algorithm?", r"(i) gcd(360, 270) (1). (ii) $360=270\times1+90$; $270=90\times3+0$ ⇒ 90 cm (1). (iii) $(360/90)\times(270/90)=4\times3=12$ tiles (1). (iv) Division: 2 reductions; subtraction: $(360,270)\to(270,90)\to(90,180)\to(180,90)\to(90,90)\to(90,0)$ is 4 applications of Step 3, so 2 fewer (2).", "1+1+1+2"),
 Q(r"<b>Case study:</b> A school wants to seat 84 boys and 126 girls in rows so that each row has only boys or only girls and every row has the same number of students. (i) What is the largest row size? (ii) Show the divisor lists' common part. (iii) How many rows of boys and girls result? (iv) Which algorithm would you use for 8400 and 12600 and why?", r"(i) gcd(84, 126) $=42$ (1). (ii) Common divisors $=[1,2,3,6,7,14,21,42]$ (1). (iii) Boys $84/42=2$ rows; girls $126/42=3$ rows (1). (iv) The division algorithm — its number of steps depends on the digits, not the values, so it stays fast (2).", "1+1+1+2"),
 Q(r"<b>Case study:</b> Ishaan wants to know how the work in the column-addition algorithm grows with the number of digits. (i) How many single-digit additions does one column need at most? (ii) For two n-digit numbers, how many columns? (iii) For n = 4 and 15 s per column, find the time. (iv) By counting dots at 1 s per dot, estimate the time for 4-digit numbers whose sum is about 6000 and compare.", r"(i) One (digit + digit + carry) (1). (ii) $n$ columns (1). (iii) $4\times15=60$ s (1). (iv) About 6000 s $=100$ min, which is 100 times slower than 60 s (2).", "1+1+1+2"),
 Q(r"<b>Case study:</b> Neha writes the algorithm: ‘Start with most-recent-common-divisor = 1. For each k from 2 to min(m, n): if k divides both m and n, update to k.’ (i) Execute it for m = 20, n = 30 and list the k that update the value. (ii) What is the final value and what does it equal? (iii) How many values of k were examined? (iv) Suggest how to reduce the number of checks using Euclid's idea.", r"(i) $k=2$ ✓, $k=5$ ✓, $k=10$ ✓ (others up to 20 ✗) (1). (ii) Final value $10=\gcd(20,30)$ (1). (iii) $k=2,\ldots,20$: 19 values (1). (iv) Use $\gcd(m,n)=\gcd(n,m\bmod n)$: $30=20\times1+10$; $20=10\times2+0$ gives 10 in 2 steps (2).", "1+1+1+2"),
 Q(r"<b>Case study:</b> The chapter says the number of reductions in Euclid's subtraction algorithm for gcd(2k + 1, 2) is about k. (i) For k = 5, write the pair-chain for gcd(11, 2) and count the reductions. (ii) Write the division-algorithm chain. (iii) Compare. (iv) What does this show about the efficiency of the two algorithms?", r"(i) $(11,2)\to(2,9)\to(9,2)\to(2,7)\to(7,2)\to(2,5)\to(5,2)\to(2,3)\to(3,2)\to(2,1)\to(1,1)\to(1,0)$: Step 3 is applied 7 times (2). (ii) $(11,2)\to(2,1)\to(1,0)$ (1). (iii) 7 versus 2 (1). (iv) Subtraction depends on the value, the division algorithm does not grow with the value (1).", "2+1+1+1"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
