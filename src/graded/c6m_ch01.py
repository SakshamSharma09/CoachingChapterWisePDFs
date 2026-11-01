"""Class 6 Maths Ch 1 - Patterns in Mathematics."""
from g67 import *

SLUG, NAME, CHNO = "Patterns_in_Mathematics", "Patterns in Mathematics", 1

def seq(a, d, n=5): return [a + d * i for i in range(n)]
def sj(xs): return ", ".join(map(str, xs))
def fib(n, a=1, b=1):
    out = [a, b]
    while len(out) < n: out.append(out[-1] + out[-2])
    return out[:n]

# ---------------- EASY ----------------
eA1 = [nm(f"The next number in the pattern ${sj(seq(a,d))}$, ... is:", a + 5 * d, f"The common difference is {d}, so add {d} to the last term.") for a, d in [(2, 3), (5, 4), (7, 2), (10, 5), (3, 6)]]
eA2 = [nm(f"The {n}th odd number is:", 2 * n - 1, "The $n$th odd number is $2n-1$.") for n in [8, 12, 15, 20, 25]]
eA3 = [nm(f"The {n}th even number is:", 2 * n, "The $n$th even number is $2n$.") for n in [7, 11, 14, 18, 30]]
eA4 = [nm(f"The value of ${n}^2$ (the {n}th square number) is:", n * n, f"${n}\\times{n}={n*n}$.", offs=(n, -n, 1, 2, 10)) for n in [6, 9, 11, 13, 15]]
eA5 = [nm(f"The {n}th triangular number $1+2+\\dots+{n}$ is:", tri(n), f"$\\frac{{{n}\\times{n+1}}}{{2}}={tri(n)}$.", offs=(n, -n, 1, 2, 10)) for n in [4, 5, 6, 7, 8]]
eA6 = [nm(f"The value of ${n}^3$ (the {n}th cube number) is:", n ** 3, f"${n}\\times{n}\\times{n}={n**3}$.", offs=(n, -n, n * n, 3 * n, 10)) for n in [2, 3, 4, 5, 6]]
eA7 = [nm(f"The first {n} odd numbers add up to:", n * n, "The sum of the first $n$ odd numbers is $n\\times n$.", offs=(n, -n, 1, 2, 10)) for n in [4, 6, 8, 9]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([QQ(f"Write the next three numbers: ${sj(seq(a,d,4))}$, ...", f"Common difference $={d}$", f"Next three: ${sj(seq(a+4*d,d,3))}$") for a, d in [(4, 5), (9, 3), (6, 7), (15, 4)]]
          + [QQ(f"Write the first {n} square numbers.", f"Squares are $1\\times1,2\\times2,\\dots$", "$" + sj([i * i for i in range(1, n + 1)]) + "$") for n in [5, 6, 7, 8]]
          + [QQ(f"Write the first {n} triangular numbers.", "Add 1, then 2, then 3, ... one at a time", "$" + sj([tri(i) for i in range(1, n + 1)]) + "$") for n in [5, 6, 7, 8]])
EASY_C = ([QQ(f"Find the {n}th term of the pattern ${sj(seq(a,d,4))}$, ... by adding the common difference repeatedly.", f"Common difference $={d}$", f"Term $n$ is $a+(n-1)d={a}+{n-1}\\times{d}$", f"${a+(n-1)*d}$") for a, d, n in [(3, 2, 8), (5, 3, 7), (2, 5, 9), (4, 4, 10), (6, 3, 8), (1, 6, 7)]]
          + [QQ(f"Show that the sum of the first {n} odd numbers is a square number.", "$" + "+".join(str(2 * i - 1) for i in range(1, n + 1)) + f"={n*n}$", f"${n*n}={n}\\times{n}$ is a square number") for n in [5, 6, 7, 9, 10, 12]]
          + [QQ(f"Write the numbers 1 to {n} as a growing sum and find the {n}th triangular number.", f"$1+2+\\dots+{n}$", f"$={tri(n)}$") for n in [9, 10, 11, 12, 13, 14]])
EASY_D = ([QQ(f"Write the first 6 terms of the pattern which starts at {a} and adds {d} each time. Is the number {a+7*d} in this pattern? Which term is it?", f"First 6 terms: ${sj(seq(a,d,6))}$", f"Term 7 is {a+6*d} and term 8 is {a+7*d}", f"Yes, {a+7*d} is the 8th term") for a, d in [(2, 3), (4, 5), (1, 7), (6, 4), (3, 8), (5, 6)]]
          + [QQ(f"Write {n*n} as the sum of consecutive odd numbers starting from 1, and write it as a product of two equal numbers. Then write the sum of the first {n+1} odd numbers.", "$" + "+".join(str(2 * i - 1) for i in range(1, n + 1)) + f"={n*n}$", f"${n*n}={n}\\times{n}$", f"Sum of first {n+1} odd numbers $={n+1}\\times{n+1}={(n+1)**2}$") for n in [4, 5, 6, 7, 8, 9]])

# ---------------- NCERT ----------------
def virahanka(k, a=1, b=2):
    s = [a, b]
    while len(s) < k: s.append(s[-1] + s[-2])
    return s
nA1 = [nm(f"In the Virahanka (Fibonacci) sequence $1,2,3,5,8,\\dots$ the {k}th term is:", virahanka(k)[-1], "Each term is the sum of the two terms before it.", offs=(1, -1, 2, -2, 5, 8)) for k in [7, 8, 9, 10, 11]]
nA2 = [nm(f"A complete graph has {n} points, each joined to every other point. How many lines are there?", n * (n - 1) // 2, f"Number of lines $=\\frac{{{n}\\times{n-1}}}{{2}}$.", offs=(1, -1, n, -n)) for n in [3, 4, 5, 6, 7]]
nA3 = [nm(f"The sum of the triangular numbers {tri(n)} and {tri(n+1)} is:", (n + 1) ** 2, "Two consecutive triangular numbers add up to a square number.", offs=(1, -1, n, 2, 10)) for n in [4, 5, 6, 7, 8]]
nA4 = [nm(f"What is the sum of the first {n} natural numbers $1+2+3+\\dots+{n}$?", tri(n), f"Triangular number $T_{{{n}}}=\\frac{{{n}({n+1})}}{{2}}$.", offs=(n, -n, 1, 2, 10)) for n in [15, 20, 25, 30, 40]]
nA5 = [nm(f"The numbers 1, 4, 9, 16, 25, ... are called square numbers. The {n}th one is:", n * n, f"${n}\\times{n}$.", offs=(n, -n, 1, 2, 10)) for n in [16, 17, 19, 21, 22]]
nA6 = [nm(f"In the pattern $1,3,6,10,\\dots$ what is the {n}th term?", tri(n), "Triangular numbers: term $n$ is $1+2+\\dots+n$.", offs=(1, -1, n, 2, 10)) for n in [9, 12, 13, 14, 16]]
nA7 = [nm(f"In the pattern of cube numbers $1,8,27,64,\\dots$ the term after {n**3} is:", (n + 1) ** 3, "Cube numbers are $1^3,2^3,3^3,\\dots$", offs=(1, -1, 10, n, 2 * n)) for n in [5, 6, 7, 8]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Write the first 10 terms of the Virahanka sequence that starts with {a}, {b}.", "Each term is the sum of the previous two", "$" + sj(virahanka(10, a, b)) + "$") for a, b in [(1, 1), (1, 3), (2, 3), (1, 4)]]
           + [QQ(f"How many lines are needed to join all pairs among {n} points (a complete graph)?", f"Each point joins to {n-1} others, and every line is counted twice", f"Lines $=\\frac{{{n}\\times{n-1}}}{{2}}={n*(n-1)//2}$") for n in [8, 9, 10, 12]]
           + [QQ(f"Find the sum $1+3+5+\\dots$ of the first {n} odd numbers without adding one by one.", "Sum of first $n$ odd numbers is $n\\times n$", f"${n}\\times{n}={n*n}$") for n in [13, 15, 17, 20]])
NCERT_C = ([QQ(f"Add the triangular numbers {tri(n)} and {tri(n+1)}. What do you notice about the answer?", f"Sum $={tri(n)}+{tri(n+1)}={tri(n)+tri(n+1)}$", f"${(n+1)**2}={n+1}\\times{n+1}$", "Two consecutive triangular numbers always add to a square number") for n in [9, 10, 11, 12, 13, 14]]
           + [QQ(f"Write the sum $1^3+2^3+\\dots+{n}^3$ and show it equals the square of $1+2+\\dots+{n}$.", f"$1+2+\\dots+{n}={tri(n)}$", f"$1^3+\\dots+{n}^3=" + "+".join(str(i ** 3) for i in range(1, n + 1)) + f"={sum(i**3 for i in range(1,n+1))}$", f"${tri(n)}^2={tri(n)**2}$, so they match") for n in [3, 4, 5, 6, 7, 8]]
           + [QQ(f"Look at the sequence ${sj(seq(a,d,5))}$. Find the pattern and the 10th term.", f"Difference between terms is {d}", f"10th term $=a+9d={a}+9\\times{d}$", f"$={a+9*d}$") for a, d in [(5, 2), (8, 3), (11, 4), (1, 9), (7, 6), (13, 5)]])
NCERT_D = ([QQ(f"A group of {n} friends shake hands with each other exactly once. Using the idea of a complete graph, find the number of handshakes. Show the working.", f"First person shakes {n-1} hands, next {n-2} new hands, ... down to 1", "Total $=" + "+".join(str(i) for i in range(n - 1, 0, -1)) + "$", f"$={n*(n-1)//2}$ handshakes", "This is the triangular number $T_{" + str(n - 1) + "}$") for n in [6, 7, 8, 9, 10, 11]]
           + [QQ(f"In the Virahanka sequence $1,2,3,5,8,\\dots$ the {k}th and {k+1}th terms are {virahanka(k+1)[-2]} and {virahanka(k+1)[-1]}. Find the next three terms and add the first {k} terms.", f"Next term $={virahanka(k+1)[-2]}+{virahanka(k+1)[-1]}={virahanka(k+2)[-1]}$", f"Then {virahanka(k+3)[-1]} and {virahanka(k+4)[-1]}", f"Sum of first {k} terms $={sum(virahanka(k))}$ (equals the term two places ahead minus 2: {virahanka(k+2)[-1]}-2)") for k in [5, 6, 7, 8, 9, 10]])

# ---------------- MEDIUM ----------------
mA1 = [nm(f"The nth term of the pattern ${sj(seq(a,d,4))}$, ... is $a+(n-1)d$. The {n}th term is:", a + (n - 1) * d, f"{a}+({n}-1)x{d}", offs=(d, -d, 1, 2, 10)) for a, d, n in [(4, 7, 12), (9, 6, 15), (13, 8, 11), (5, 9, 14), (16, 11, 9)]]
mA2 = [nm(f"In the pattern ${sj(seq(a,d,4))}$, ... which term number equals {a+(n-1)*d}?", n, "Solve $a+(n-1)d=$ the given number.", offs=(1, -1, 2, -2, 5)) for a, d, n in [(3, 5, 18), (7, 4, 25), (2, 9, 13), (10, 6, 22), (8, 3, 31)]]
mA3 = [nm(f"What is the sum of the first {n} even numbers $2+4+6+\\dots$?", n * (n + 1), "Sum of first $n$ even numbers is $n(n+1)$.", offs=(n, -n, 1, 2, 10)) for n in [12, 15, 18, 22, 25]]
mA4 = [nm(f"Which triangular number comes just after {tri(n)}?", tri(n + 1), f"Add {n+1}.", offs=(1, -1, n, n + 2, 10)) for n in [19, 23, 27, 31, 35]]
mA5 = [nm(f"A pattern of stacked sticks uses 3 sticks for 1 triangle and 2 more sticks for each extra triangle added in a row. Sticks for {n} triangles:", 3 + 2 * (n - 1), "Sticks $=3+2(n-1)=2n+1$.", offs=(1, -1, 2, -2, n)) for n in [10, 15, 20, 25, 30]]
mA6 = [nm(f"The sum of the first {n} natural numbers added to the sum of the first {n+1} natural numbers is:", (n + 1) ** 2, "Consecutive triangular numbers add to a square.", offs=(1, -1, n, 2, 10)) for n in [24, 29, 34, 39]]
mA7 = [nm(f"Powers of 2: $2,4,8,16,\\dots$ The {n}th term is:", 2 ** n, "Each term is double the one before it.", offs=(2 ** (n - 1) // 2 * 0 + 2, -2, 2 ** (n - 1), 2 ** n // 4, 6)) for n in [7, 8, 9, 10]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([QQ(f"Find the nth term formula of ${sj(seq(a,d,4))}$, ... and the {n}th term.", f"Formula $a+(n-1)d={a}+(n-1)\\times{d}={d}n+{a-d}$", f"{n}th term $={a+(n-1)*d}$") for a, d, n in [(5, 3, 20), (2, 7, 15), (11, 4, 18), (6, 5, 25)]]
          + [QQ(f"Is {a+(n-1)*d+1} a term of ${sj(seq(a,d,4))}$, ...? Give a reason.", f"Terms are {a}, {a+d}, ... each {d} more than the last", f"{a+(n-1)*d} is a term but {a+(n-1)*d+1} lies between two terms, so it is not a term") for a, d, n in [(3, 4, 9), (6, 5, 12), (2, 6, 14), (9, 8, 10)]]
          + [QQ(f"Find the sum of the first {n} odd numbers and the first {n} even numbers.", f"Odd: ${n}^2={n*n}$", f"Even: ${n}\\times{n+1}={n*(n+1)}$") for n in [30, 35, 40, 50]])
MED_C = ([QQ(f"How many triangles' worth of sticks: a row of {n} triangles needs 3 sticks for the first triangle and 2 more for each new one. Find the sticks needed and the number of triangles that can be made with {3+2*(n+4)} sticks.", f"Sticks for {n} triangles $=3+2({n}-1)={2*n+1}$", f"For {3+2*(n+4)} sticks: $2n+1={3+2*(n+4)}$ so $n={n+4}$", f"{n+4} triangles") for n in [12, 15, 18, 21, 24, 27]]
          + [QQ(f"Find the sum of all odd numbers from 1 to {2*n-1}. Hence find the sum of all even numbers from 2 to {2*n}.", f"There are {n} odd numbers, sum $={n*n}$", f"Even numbers: sum $={n}\\times{n+1}$", f"$={n*(n+1)}$") for n in [30, 40, 45, 50, 60, 75]]
          + [QQ(f"Write the {n}th and {n+1}th triangular numbers and check that they add to a square.", f"$T_{{{n}}}={tri(n)}$, $T_{{{n+1}}}={tri(n+1)}$", f"Sum $={tri(n)+tri(n+1)}$", f"${(n+1)}^2={(n+1)**2}$ matches") for n in [20, 24, 28, 32, 36, 40]])
MED_D = ([QQ(f"A pattern of squares: the first figure has {a} squares and each next figure has {d} more. Find the number of squares in the {n}th figure, and the first figure that has more than {a+(n-1)*d+50} squares.", f"{n}th figure $={a}+({n}-1)\\times{d}={a+(n-1)*d}$", f"More than {a+(n-1)*d+50} needs $({a+(n-1)*d+50}-{a})\\div{d}$ more steps", f"Steps needed: {(50 + d) // d}", f"Figure number {n+(50+d)//d}", "Check by substituting") for a, d, n in [(5, 4, 10), (3, 5, 12), (8, 6, 9), (4, 7, 11), (6, 3, 14), (2, 8, 8)]]
          + [QQ(f"Show that the sum of the cubes of the first {n} numbers is a perfect square, and find the sum of the first {n} numbers.", f"Sum of first {n} numbers $=\\frac{{{n}\\times{n+1}}}{{2}}={tri(n)}$", f"Sum of cubes $={sum(i**3 for i in range(1,n+1))}$", f"${tri(n)}^2={tri(n)**2}$", "They are equal, so the cube sum is a perfect square") for n in [9, 10, 11, 12, 13, 14]])

# ---------------- HARD ----------------
hA1 = [nm(f"In a party {n} people greet each other once with a hug. Number of hugs:", n * (n - 1) // 2, "Complete graph on $n$ points.", offs=(n, -n, 1, 2, 10)) for n in [15, 18, 20, 25]]
hA2 = [nm(f"The sum $1+2+3+\\dots+n$ equals {tri(n)}. Then $n$ is:", n, "Try triangular numbers.", offs=(1, -1, 2, -2, 5)) for n in [37, 44, 52, 63]]
hA3 = [nm(f"The sum of the first {n} odd numbers is {n*n}. The sum of the odd numbers from {2*a+1} to {2*n-1} is:", n * n - a * a, f"Subtract the first {a} odd numbers, whose sum is {a*a}.", offs=(1, -1, a, 2, 10)) for n, a in [(30, 10), (35, 15), (40, 12), (50, 20)]]
hA4 = [nm(f"The difference between the squares of the {n+1}th and {n}th numbers is:", 2 * n + 1, f"${n+1}^2-{n}^2$ is the next odd number.", offs=(1, -1, 2, -2, n)) for n in [19, 24, 29, 34]]
hA5 = [nm(f"The first term of a pattern is {a} and the {n}th term is {a+(n-1)*d}. The common difference is:", d, "Divide the total increase by the number of steps.", offs=(1, -1, 2, -2, 5)) for a, d, n in [(7, 11, 14), (12, 13, 17), (9, 8, 21), (4, 15, 12)]]
hA6 = [nm(f"A pattern adds 1, then 2, then 3, ... Starting at {a}, the term after {n} additions is:", a + tri(n), "Add the triangular number.", offs=(1, -1, n, 2, 10)) for a, n in [(10, 12), (25, 15), (7, 18), (40, 20)]]
hA7 = [nm(f"The sum $1^3+2^3+\\dots+{n}^3$ equals:", tri(n) ** 2, "Square of the triangular number.", offs=(1, -1, tri(n), 10, 2 * n)) for n in [9, 10, 11, 12]]
hA8 = [nm(f"The {n}th triangular number minus the {n-1}th triangular number is:", n, "Each triangular number adds the next counting number.", offs=(1, -1, 2, -2, 10)) for n in [41, 57, 68, 79]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"{n} cricket teams play a league in which every team plays every other team once. Find the number of matches.", "Complete graph idea: each pair plays once", f"$\\frac{{{n}\\times{n-1}}}{{2}}={n*(n-1)//2}$") for n in [14, 16, 17, 19]]
          + [QQ(f"The sum of the first $n$ odd numbers is {n*n}. Find $n$ and the {n}th odd number.", f"$n\\times n={n*n}$ so $n={n}$", f"{n}th odd number $=2\\times{n}-1={2*n-1}$") for n in [31, 38, 43, 55]]
          + [QQ(f"Find the sum of odd numbers from {2*a+1} to {2*n-1}.", f"Sum of first {n} odd numbers $={n*n}$ and first {a} odd numbers $={a*a}$", f"Required sum $={n*n-a*a}$") for n, a in [(24, 9), (28, 11), (33, 13), (41, 16)]])
HARD_C = ([QQ(f"In a pattern the 1st term is {a}, the 2nd is {a+d}, and so on by adding {d}. Which term of the pattern equals {a+(n-1)*d}? Find also the term just before it.", f"$a+(n-1)d={a+(n-1)*d}$ gives $n-1=({a+(n-1)*d}-{a})\\div{d}$", f"$n={n}$", f"Term before it $={a+(n-2)*d}$") for a, d, n in [(14, 9, 40), (23, 7, 45), (6, 13, 32), (31, 12, 28), (17, 8, 52), (4, 14, 36)]]
          + [QQ(f"Sums of consecutive odd numbers give squares. Find the sum of the odd numbers from 1 to {2*n-1} and use it to find {n}$^2$. Then evaluate the sum from {2*n+1} to {2*n+2*b-1}.", f"First {n} odd numbers sum to ${n*n}$", f"First {n+b} odd numbers sum to ${(n+b)**2}$", f"Required sum $={(n+b)**2-n*n}$") for n, b in [(20, 5), (25, 6), (30, 8), (35, 7), (40, 10), (45, 9)]]
          + [QQ(f"A tower is built with rows of cubes: row 1 has 1 cube, row 2 has 3, row 3 has 6, and so on (triangular numbers). How many cubes are in row {n}, and in the first {n} rows together?", f"Row {n} has $T_{{{n}}}={tri(n)}$ cubes", f"Total in {n} rows uses the idea of adding triangular numbers", f"Sum $=\\frac{{{n}({n+1})({n+2})}}{{6}}={n*(n+1)*(n+2)//6}$") for n in [6, 7, 8, 9, 10, 12]])
HARD_D = ([QQ(f"Look at the pattern: the {k}th figure has {a+(k-1)*d} dots. How many dots are in figure {k+m}? If a figure has {a+(k+m+5-1)*d} dots, which figure is it? Show that the dots form a pattern with common difference {d}.", f"Difference between consecutive figures $={d}$", f"Figure {k+m}: $a={a}$, so dots $={a+(k+m-1)*d}$", f"For {a+(k+m+4)*d} dots: $n-1=({a+(k+m+4)*d}-{a})\\div{d}$", f"$n={k+m+5}$", "Verification by substitution") for a, d, k, m in [(4, 6, 8, 7), (5, 9, 6, 9), (7, 4, 10, 8), (3, 11, 5, 10), (9, 5, 7, 12), (6, 8, 9, 6)]]
          + [QQ(f"Two sequences: A is ${sj(seq(a,d,4))}$, ... and B is ${sj(seq(b,e,4))}$, .... Find the {n}th term of each and decide which is larger and by how much.", f"{n}th term of A $={a}+{n-1}\\times{d}={a+(n-1)*d}$", f"{n}th term of B $={b}+{n-1}\\times{e}={b+(n-1)*e}$", f"Larger: {'A' if a+(n-1)*d>b+(n-1)*e else 'B' if b+(n-1)*e>a+(n-1)*d else 'neither (equal)'}", f"Difference $={abs(a+(n-1)*d-b-(n-1)*e)}$") for a, d, b, e, n in [(5, 4, 20, 2, 12), (3, 7, 40, 3, 15), (8, 5, 2, 9, 11), (11, 6, 6, 8, 14), (25, 3, 4, 7, 20), (9, 9, 30, 5, 13)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
