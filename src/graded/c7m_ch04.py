"""Class 7 Maths Ch 4 - Expressions using Letter-Numbers (forming, evaluating, adding, subtracting and simplifying expressions; patterns)."""
from g67 import *

SLUG, NAME, CHNO = "Letter_Numbers", "Expressions using Letter-Numbers", 4

def ex(*ts):
    """ts = (coefficient, letters) pairs, '' for a constant -> '3x - 2y + 5' (zero terms skipped)."""
    out = ""
    for c, v in ts:
        if c == 0: continue
        a = abs(c); body = (str(a) if a != 1 or not v else "") + v
        out += (("-" if c < 0 else "") + body) if not out else ((" - " if c < 0 else " + ") + body)
    return out or "0"
def X(*ts): return "$" + ex(*ts) + "$"
def num(q, c, why="", offs=(1, -1, 2, -2, 3, 5, 10)): return nm(q, c, why, offs=offs, pos=False)

# ---------------------------------------------------------------- EASY
eA1 = [nw(f"If $x={x}$, the value of ${a}x+{b}$ is:", a * x + b, [int(f"{a}{x}") + b, (a + b) * x, a + x + b, a * x + b + a], "Replace $x$ by its value and calculate.") for a, b, x in [(2, 3, 4), (3, 1, 5), (5, 2, 3), (4, 6, 2), (6, 5, 1)]]
eA2 = [nw(f"If $y={y}$, the value of ${a}y-{b}$ is:", a * y - b, [int(f"{a}{y}") - b, a * y + b, a + y - b, a * y - b + a], "Replace $y$ by its value and subtract.") for a, b, y in [(3, 4, 5), (2, 7, 6), (4, 3, 4), (5, 8, 3)]]
eA3 = [tm(q, c, w, "Translate the words into a letter-number expression.") for q, c, w in [
    ("5 more than a number $n$ is:", "$n+5$", ["$5n$", "$n-5$", "$5-n$"]),
    ("3 times a number $m$ is:", "$3m$", ["$m+3$", "$m-3$", "$m/3$"]),
    ("7 less than a number $p$ is:", "$p-7$", ["$7-p$", "$7p$", "$p+7$"]),
    ("A number $k$ divided by 4 is:", "$k/4$", ["$4k$", "$k+4$", "$4/k$"]),
    ("Twice a number $t$ increased by 1 is:", "$2t+1$", ["$2(t+1)$", "$t+2$", "$2t-1$"])]]
eA4 = [tm(f"The number of terms in the expression {X(*ts)} is:", str(len(ts)), [str(len(ts) - 1), str(len(ts) + 1), str(len(ts) + 2)], "Terms are separated by + or - signs.")
       for ts in [((3, "x"), (2, "y"), (5, "")), ((4, "a"), (7, "")), ((1, "p"), (1, "q"), (1, "r"), (9, "")), ((6, "m"), (2, "n"))]]
eA5 = [tm(f"The coefficient of $x$ in {X(*ts)} is:", str(ts[0][0]), [str(ts[0][0] + 1), str(ts[0][0] + 2), str(ts[0][0] - 1)], "The coefficient is the number multiplying the letter.")
       for ts in [((7, "x"), (2, "")), ((3, "x"), (4, "y")), ((9, "x"), (5, "")), ((12, "x"), (1, "z"))]]
eA6 = [tm("Which pair are like terms?", c, w, "Like terms have the same letter part.") for c, w in [
    ("$3x$ and $9x$", ["$3x$ and $9y$", "$2x$ and $2x^2$", "$5$ and $5x$"]),
    ("$4y$ and $-y$", ["$4y$ and $4z$", "$y$ and $y^2$", "$4$ and $y$"]),
    ("$7ab$ and $2ab$", ["$7ab$ and $2a$", "$7a$ and $2b$", "$ab$ and $a^2b$"]),
    ("$6p$ and $p$", ["$6p$ and $6$", "$6p$ and $q$", "$p^2$ and $p$"])]]
eA7 = [num(f"If $a={a}$ and $b={b}$, then $a+b$ is:", a + b, "Add the two values.") for a, b in [(3, 9), (12, 5), (8, 8), (15, 6)]]
eA8 = [num(f"${a}x+{b}x$ equals ${a + b}x$. For $x={x}$ its value is:", (a + b) * x, "Multiply the coefficient by the value of $x$.") for a, b, x in [(2, 3, 4), (5, 4, 3), (6, 1, 5), (7, 2, 2)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Find the value of ${a}x+{b}$ when $x={x}$.", f"Substitute: ${a}({x})+{b}$", f"$={a * x + b}$") for a, b, x in [(2, 5, 3), (4, 1, 6), (3, 7, 5), (6, 2, 4)]]
          + [QQ(f"Write as an expression: {q}.", "Identify the operations", f"Expression: ${e}$") for q, e in [("7 added to 4 times $n$", "4n+7"), ("3 subtracted from twice $m$", "2m-3"), ("5 times the sum of $a$ and 2", "5(a+2)"), ("$x$ taken away from 20", "20-x")]]
          + [QQ(f"Add {X(*u)} and {X(*v)}.", "Group the like terms", f"Sum $={ex((u[0][0] + v[0][0], 'x'), (u[1][0] + v[1][0], ''))}$") for u, v in [(((3, "x"), (4, "")), ((2, "x"), (1, ""))), (((5, "x"), (2, "")), ((4, "x"), (6, ""))), (((7, "x"), (3, "")), ((1, "x"), (8, ""))), (((2, "x"), (9, "")), ((6, "x"), (5, "")))]])
EASY_C = ([QQ(f"Find the value of ${a}x+{b}y$ when $x={x}$ and $y={y}$.", f"Substitute: ${a}({x})+{b}({y})$", f"$={a * x}+{b * y}$", f"$={a * x + b * y}$") for a, b, x, y in [(2, 3, 4, 5), (3, 2, 6, 7), (5, 4, 2, 3), (4, 5, 8, 9), (6, 5, 3, 2), (7, 2, 4, 6)]]
          + [QQ(f"Simplify: ${a}x+{b}x-{c}x$.", "All three terms are like terms", f"Coefficients: ${a}+{b}-{c}={a + b - c}$", f"Answer: ${a + b - c}x$") for a, b, c in [(7, 4, 3), (9, 6, 5), (12, 5, 8), (15, 3, 9), (10, 10, 4), (8, 7, 6)]]
          + [QQ(f"Write an expression for the cost of ${n}$ pens at ₹$p$ each, and find the cost if $p={p}$.", f"Cost $={n}p$", f"At $p={p}$: ${n}\\times{p}$", f"Cost $=$ ₹${n * p}$") for n, p in [(5, 12), (8, 15), (6, 20), (9, 11), (12, 8), (7, 14)]])
EASY_D = ([QQ(f"Anil is $x$ years old. His sister is ${k}$ years younger. Write expressions for his sister's age and for the sum of their ages. Find both when $x={x}$.", f"Sister's age $=x-{k}$", f"Sum $=x+(x-{k})=2x-{k}$", f"At $x={x}$: sister $={x - k}$ years", f"Sum $={2 * x - k}$ years") for k, x in [(3, 15), (5, 18), (4, 20), (2, 12), (6, 25), (7, 22)]]
          + [QQ(f"A rectangle has length $l$ cm and breadth ${b}$ cm. Write expressions for its perimeter and area, and find both when $l={l}$.", f"Perimeter $=2(l+{b})$", f"Area $={b}l$", f"At $l={l}$: perimeter $={2 * (l + b)}$ cm", f"Area $={b * l}$ cm$^2$") for b, l in [(4, 9), (5, 12), (3, 10), (6, 8), (7, 11), (2, 15)]])

# ---------------------------------------------------------------- NCERT
nA1 = [num(f"The perimeter of a square of side $s$ is $4s$. For $s={s}$ cm it is (in cm):", 4 * s, "Perimeter $=4\\times$ side.") for s in (7, 12, 9, 15, 20)]
nA2 = [tm(q, c, w, "Write the rule using a letter-number.") for q, c, w in [
    ("The rule 'multiply by 5 and add 2' for the input $n$ is:", "$5n+2$", ["$5(n+2)$", "$n+7$", "$2n+5$"]),
    ("A rule gives 7, 12, 17, 22 for $n=1,2,3,4$. The rule is:", "$5n+2$", ["$5n$", "$n+6$", "$7n$"]),
    ("The $n$th even number is:", "$2n$", ["$2n+1$", "$n+2$", "$2n-1$"]),
    ("The $n$th odd number is:", "$2n-1$", ["$2n$", "$2n+2$", "$n-1$"])]]
nA3 = [num(f"If $m={m}$, the value of $m+{a}m$ is:", m + a * m, "Combine the like terms first: $m+am=(1+a)m$.") for m, a in [(4, 3), (6, 2), (5, 4), (3, 7)]]
nA4 = [tm(f"Subtract ${b}x$ from ${a}x$. The result is:", f"${a - b}x$", [f"${a + b}x$", f"${b - a}x$", f"${a - b}$"], "Subtract the coefficients of the like terms.") for a, b in [(9, 4), (12, 5), (15, 8), (20, 11)]]
nA5 = [num(f"The value of ${a}(x+{b})$ for $x={x}$ is:", a * (x + b), "Add inside the bracket first.") for a, b, x in [(2, 3, 4), (3, 2, 5), (4, 1, 6), (5, 3, 2)]]
nA6 = [tm(q, c, w, "Use brackets to keep the order of operations.") for q, c, w in [
    ("'Four times the sum of $x$ and 3' is:", "$4(x+3)$", ["$4x+3$", "$x+12$", "$4+3x$"]),
    ("'Sum of $y$ and twice $z$' is:", "$y+2z$", ["$2(y+z)$", "$2yz$", "$yz+2$"]),
    ("'Difference of $a$ and $b$, doubled' is:", "$2(a-b)$", ["$2a-b$", "$a-2b$", "$2a-2$"]),
    ("'Product of $p$ and $q$, increased by 5' is:", "$pq+5$", ["$p(q+5)$", "$p+q+5$", "$5pq$"]),
    ("'Half of the sum of $a$ and $b$' is:", "$(a+b)/2$", ["$a+b/2$", "$2(a+b)$", "$a/2b$"])]]
nA7 = [num(f"A taxi charges ₹{f} fixed plus ₹{r} per km. For $k={k}$ km the fare is (in ₹):", f + r * k, "Fare $=$ fixed charge $+$ rate $\\times$ distance.") for f, r, k in [(50, 12, 5), (40, 15, 4), (60, 10, 8), (30, 18, 3)]]
nA8 = [num(f"The number of matchsticks in a row of $n$ squares is $3n+1$. For $n={n}$ squares the number of matchsticks is:", 3 * n + 1, "Substitute the value of $n$.") for n in (6, 9, 11, 15)]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([QQ(f"The number of matchsticks needed for a row of $n$ squares is $3n+1$. How many matchsticks are needed for ${n}$ squares?", "Substitute $n$ in $3n+1$", f"$3({n})+1={3 * n + 1}$ matchsticks") for n in (5, 8, 10, 12)]
           + [QQ(f"Simplify: ${a}x+{b}-{c}x+{d}$.", f"Collect like terms: $({a}-{c})x$ and $({b}+{d})$", f"Answer: ${ex((a - c, 'x'), (b + d, ''))}$") for a, b, c, d in [(7, 4, 3, 6), (9, 2, 5, 8), (12, 5, 7, 3), (10, 9, 4, 1)]]
           + [QQ(f"Find the value of ${a}p-{b}q$ for $p={p}$ and $q={q}$.", f"Substitute: ${a}({p})-{b}({q})$", f"$={a * p - b * q}$") for a, b, p, q in [(5, 3, 6, 4), (4, 7, 9, 2), (8, 2, 5, 3), (6, 5, 7, 6)]])
NCERT_C = ([QQ(f"In a pattern, figure $n$ has $3n+2$ dots. Find the number of dots in figure ${n}$ and in figure ${n + 1}$. How many more dots does figure ${n + 1}$ have?", f"Figure {n}: $3({n})+2={3 * n + 2}$", f"Figure {n + 1}: $3({n + 1})+2={3 * n + 5}$", f"Difference $={3 * n + 5}-{3 * n + 2}=3$") for n in (4, 6, 10, 8, 5, 12)]
           + [QQ(f"Add ${ex((a, 'x'), (b, 'y'))}$ and ${ex((c, 'x'), (-d, 'y'))}$.", "Group the $x$-terms and the $y$-terms", f"$x$-terms: ${ex((a, 'x'), (c, 'x'))}={a + c}x$", f"Sum $={ex((a + c, 'x'), (b - d, 'y'))}$") for a, b, c, d in [(5, 9, 3, 4), (7, 6, 2, 1), (4, 8, 6, 3), (9, 5, 1, 2), (2, 10, 8, 7), (6, 4, 5, 3)]]
           + [QQ(f"A father's age is ${k}$ times his son's age $s$, plus ${a}$ years. Write an expression for the father's age and find it when $s={s}$.", f"Father's age $={k}s+{a}$", f"At $s={s}$: ${k}({s})+{a}$", f"Father's age $={k * s + a}$ years") for k, a, s in [(3, 2, 10), (2, 8, 14), (3, 5, 12), (4, 2, 9), (2, 6, 16), (3, 4, 11)]])
NCERT_D = ([QQ(f"A school buys $n$ notebooks at ₹{a} each and {k} pens at ₹{b} each. Write an expression for the total cost. Find the cost when $n={n}$ and the change from ₹{pay}.", f"Notebooks cost ${a}n$ and pens cost ${k * b}$", f"Total cost $={a}n+{k * b}$", f"At $n={n}$: ${a * n + k * b}$", f"Change $={pay}-{a * n + k * b}={pay - (a * n + k * b)}$") for a, b, k, n, pay in [(12, 5, 4, 10, 200), (15, 8, 3, 8, 200), (9, 6, 5, 12, 200), (20, 4, 6, 7, 200), (18, 10, 2, 9, 200), (14, 7, 3, 15, 300)]]
           + [QQ(f"A hall has {a} rows of $r$ chairs and {b} extra chairs at the back. Write an expression for the total number of chairs and find it for $r={r}$ and for $r={r + 2}$.", f"Total $={a}r+{b}$", f"For $r={r}$: ${a * r + b}$", f"For $r={r + 2}$: ${a * (r + 2) + b}$") for a, b, r in [(8, 6, 12), (10, 4, 9), (6, 8, 15), (12, 5, 10), (9, 3, 11), (7, 9, 14)]])

# ---------------------------------------------------------------- MEDIUM
mA1 = [num(f"The value of ${a}x+{b}y-{c}$ for $x={x}$ and $y={y}$ is:", a * x + b * y - c, "Substitute both values.") for a, b, c, x, y in [(3, 2, 5, 4, 6), (5, 3, 7, 2, 9), (4, 6, 10, 5, 3), (7, 2, 4, 3, 8)]]
mA2 = [tm(f"Simplify ${a}x+{b}y-{c}x+{d}y$:", X((a - c, "x"), (b + d, "y")), [X((a + c, "x"), (b + d, "y")), X((a - c, "x"), (b - d, "y")), f"${a - c + b + d}xy$"], "Collect the like terms separately.") for a, b, c, d in [(9, 4, 5, 3), (12, 7, 4, 2), (8, 5, 3, 6), (15, 2, 9, 8)]]
mA3 = [num(f"If $x={x}$, then ${a}(x-{b})+{c}$ equals:", a * (x - b) + c, "Work out the bracket first.") for a, b, c, x in [(3, 2, 5, 8), (4, 3, 7, 9), (5, 1, 2, 6), (2, 4, 9, 10)]]
mA4 = [tm(f"Subtract ${a}x+{b}$ from ${c}x+{d}$:", X((c - a, "x"), (d - b, "")), [X((c + a, "x"), (d + b, "")), X((a - c, "x"), (b - d, "")), X((c - a, "x"), (d + b, ""))], "Subtract the $x$-terms and the constants separately.") for a, b, c, d in [(3, 2, 8, 9), (4, 1, 10, 7), (2, 5, 9, 8), (6, 3, 11, 12)]]
mA5 = [num(f"The $n$th term of a pattern is ${a}n+{b}$. Its ${n}$th term is:", a * n + b, "Substitute the value of $n$.") for a, b, n in [(4, 3, 10), (6, 1, 12), (5, 7, 8), (3, 9, 15)]]
mA6 = [tm(f"A pencil costs ₹$x$ and an eraser costs ₹$y$. The cost of {a} pencils and {b} erasers is:", f"${a}x+{b}y$", [f"${a + b}xy$", f"${a}y+{b}x$", f"${a * b}(x+y)$"], "Multiply each price by its quantity.") for a, b in [(3, 5), (6, 2), (4, 7), (8, 3)]]
mA7 = [num(f"If $a={a}$, the value of $a^2+{k}a$ is:", a * a + k * a, "$a^2=a\\times a$.") for a, k in [(3, 2), (4, 5), (5, 3), (6, 4)]]
mA8 = [num(f"If $x={x}$, the value of $\\frac{{{a}x+{b}}}{{{c}}}$ is:", (a * x + b) // c, "Work out the numerator, then divide.") for a, b, c, x in [(4, 2, 2, 5), (6, 3, 3, 4), (8, 4, 4, 3), (10, 5, 5, 2)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Simplify: ${a}(x+{b})+{c}x$.", f"Expand the bracket: ${a}x+{a * b}$", f"Add ${c}x$: ${a + c}x+{a * b}$") for a, b, c in [(3, 4, 5), (2, 7, 6), (4, 3, 2), (5, 2, 8)]]
         + [QQ(f"Subtract ${a}x-{b}$ from ${c}x+{d}$.", f"$({c}x+{d})-({a}x-{b})$", f"Answer: ${ex((c - a, 'x'), (d + b, ''))}$") for a, b, c, d in [(3, 5, 9, 2), (4, 1, 11, 6), (2, 7, 8, 3), (5, 4, 12, 9)]]
         + [QQ(f"Find the value of $x^2+{a}x-{b}$ when $x={x}$.", f"Substitute: ${x}^2+{a}({x})-{b}$", f"$={x * x + a * x - b}$") for a, b, x in [(3, 4, 5), (2, 9, 6), (5, 7, 4), (4, 3, 7)]])
MED_C = ([QQ(f"Two numbers are ${ex((a, 'n'), (b, ''))}$ and ${ex((c, 'n'), (-d, ''))}$. Find their sum and their difference (first minus second), and evaluate both for $n={n}$.", f"Sum $={ex((a + c, 'n'), (b - d, ''))}$", f"Difference $={ex((a - c, 'n'), (b + d, ''))}$", f"At $n={n}$: sum $={(a + c) * n + b - d}$ and difference $={(a - c) * n + b + d}$") for a, b, c, d, n in [(7, 5, 3, 2, 4), (9, 4, 5, 1, 3), (8, 6, 2, 3, 5), (10, 3, 6, 4, 2), (12, 7, 5, 6, 3), (11, 2, 4, 1, 6)]]
         + [QQ(f"A row of $n$ triangles made with matchsticks needs $2n+1$ sticks. How many sticks are needed for ${n}$ triangles and for ${m}$ triangles?", f"For ${n}$ triangles: $2({n})+1={2 * n + 1}$", f"For ${m}$ triangles: $2({m})+1={2 * m + 1}$") for n, m in [(9, 14), (12, 20), (15, 25), (7, 18), (20, 30), (11, 16)]]
         + [QQ(f"A cab charges ₹{f} plus ₹{r} per km. Write the fare for $k$ km. Find the fare for ${k}$ km and for ${k + 5}$ km.", f"Fare $={f}+{r}k$", f"For ${k}$ km: ${f}+{r}({k})={f + r * k}$", f"For ${k + 5}$ km: ${f}+{r}({k + 5})={f + r * (k + 5)}$") for f, r, k in [(45, 11, 8), (60, 9, 12), (35, 14, 6), (50, 13, 10), (40, 16, 7), (55, 12, 9)]])
MED_D = ([QQ(f"A shopkeeper sells $x$ kg of rice at ₹{a} per kg and $y$ kg of wheat at ₹{b} per kg. Write an expression for his total sales and find it when $x={x}$ and $y={y}$.", f"Sales $={a}x+{b}y$", f"At the given values: ${a * x}+{b * y}$", f"Total sales $=$ ₹${a * x + b * y}$") for a, b, x, y in [(48, 36, 10, 15), (45, 30, 20, 10), (38, 28, 16, 24), (52, 40, 12, 8), (60, 35, 9, 14), (44, 32, 15, 20)]]
         + [QQ(f"Raju is $r$ years old. His mother's age is ${a}$ more than 3 times his age. After ${k}$ years, write the ages of both and the sum of their ages. Evaluate the sum for $r={r}$.", f"Mother now $=3r+{a}$", f"After ${k}$ years: Raju $=r+{k}$, mother $=3r+{a + k}$", f"Sum $=4r+{a + 2 * k}$", f"At $r={r}$: ${4 * r + a + 2 * k}$ years") for a, k, r in [(4, 5, 10), (6, 3, 12), (2, 8, 9), (5, 6, 11), (3, 4, 14), (7, 2, 13)]])

# ---------------------------------------------------------------- HARD
hA1 = [num(f"If $a={a}$ and $b={b}$, the value of ${p}a^2-{q}b$ is:", p * a * a - q * b, "Square first, then multiply.") for a, b, p, q in [(3, 4, 5, 6), (4, 5, 3, 7), (5, 2, 2, 9), (6, 3, 4, 8)]]
hA2 = [tm(f"Simplify ${a}(x+{b})-{c}(x-{d})$:", X((a - c, "x"), (a * b + c * d, "")), [X((a - c, "x"), (a * b - c * d, "")), X((a + c, "x"), (a * b + c * d, "")), X((a - c, "x"), (c * d - a * b, ""))], "Expand each bracket, watching the signs.") for a, b, c, d in [(5, 2, 3, 1), (7, 3, 4, 2), (6, 1, 2, 4), (9, 2, 5, 3)]]
hA3 = [tm(f"The perimeter of a rectangle with sides ${a}x+{b}$ and ${c}x-{d}$ is:", X((2 * (a + c), "x"), (2 * (b - d), "")), [X((a + c, "x"), (b - d, "")), X((2 * (a - c), "x"), (2 * (b + d), "")), X((2 * a * c, "x"))], "Perimeter $=2\\times$(length $+$ breadth).") for a, b, c, d in [(5, 4, 3, 1), (7, 6, 2, 3), (4, 9, 6, 5), (8, 2, 5, 1)]]
hA4 = [num(f"If $n={n}$, then $\\frac{{n(n+1)}}{{2}}$ equals:", n * (n + 1) // 2, "Substitute, multiply, then halve.") for n in (10, 14, 20, 25)]
hA5 = [tm(q, c, w, "Test the expressions with small values of $n$.") for q, c, w in [
    ("Which expression is always even for a whole number $n$?", "$2n+4$", ["$2n+1$", "$n+2$", "$3n$"]),
    ("Which expression is always odd for a whole number $n$?", "$4n+3$", ["$4n+2$", "$n+3$", "$2n+4$"]),
    ("Which expression is a multiple of 5 for every whole number $n$?", "$10n+5$", ["$5n+1$", "$10n+2$", "$n+5$"]),
    ("The sum of three consecutive numbers starting at $n$ is:", "$3n+3$", ["$3n+1$", "$n+3$", "$3n$"])]]
hA6 = [num(f"If $x={x}$ and $y={y}$, the value of ${a}x-{b}y+xy$ is:", a * x - b * y + x * y, "Substitute carefully; $xy$ means $x\\times y$.") for a, b, x, y in [(3, 2, 4, 5), (5, 4, 3, 6), (2, 7, 5, 2), (6, 3, 4, 4)]]
hA7 = [num(f"A rule is: output $=3\\times$ input $-{k}$. The output for the input {i} is:", 3 * i - k, "Apply the rule to the input.") for k, i in [(4, 9), (7, 12), (2, 15), (5, 20)]]
hA8 = [num(f"If $x={x}$, the value of ${a}x^2+{b}$ is:", a * x * x + b, "$x^2=x\\times x$.") for a, b, x in [(2, 5, 6), (3, 4, 5), (4, 1, 7), (5, 8, 3)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"Simplify: ${a}(x-{b})-{c}(x-{d})$.", f"Expand: ${a}x-{a * b}-{c}x+{c * d}$", f"Answer: ${ex((a - c, 'x'), (c * d - a * b, ''))}$") for a, b, c, d in [(7, 2, 3, 5), (9, 3, 4, 2), (8, 1, 5, 4), (6, 4, 2, 7)]]
          + [QQ(f"Write the sum of three consecutive multiples of ${k}$, starting with ${k}n$, and simplify it.", f"${k}n+{k}(n+1)+{k}(n+2)$", f"$={3 * k}n+{3 * k}={3 * k}(n+1)$") for k in (2, 5, 4, 6)]
          + [QQ(f"Find the value of ${a}x^2-{b}x+{c}$ when $x={x}$.", f"Substitute: ${a}({x})^2-{b}({x})+{c}$", f"$={a * x * x - b * x + c}$") for a, b, c, x in [(2, 3, 4, 5), (3, 5, 1, 4), (4, 2, 6, 3), (5, 6, 7, 2)]])
def consec(k, n):
    first = k * (k - 1) // 2
    return QQ(f"Write the sum of {k} consecutive numbers starting at $n$ as an expression in $n$, and evaluate it for $n={n}$.", f"Numbers: $n, n+1, \\dots, n+{k - 1}$", f"Sum $={k}n+{first}$", f"At $n={n}$: ${k * n + first}$")
def fares(fa, ra, fb, rb, K):
    A, B = fa + ra * K, fb + rb * K
    return QQ(f"Taxi A charges ₹{fa} plus ₹{ra} per km and taxi B charges ₹{fb} plus ₹{rb} per km. Write both fares for $k$ km. For a journey of ${K}$ km, which taxi is cheaper and by how much?", f"A: ${fa}+{ra}k$ and B: ${fb}+{rb}k$", f"For ${K}$ km: A $={A}$ and B $={B}$", f"Taxi {'A' if A < B else 'B'} is cheaper by ₹${abs(A - B)}$")
HARD_C = ([QQ(f"A rectangle has length $({a}x+{b})$ cm and breadth $({c}x-{d})$ cm. Find its perimeter as an expression and its value for $x={x}$.", f"$P=2[({a}x+{b})+({c}x-{d})]$", f"$=2({ex((a + c, 'x'), (b - d, ''))})$", f"$={ex((2 * (a + c), 'x'), (2 * (b - d), ''))}$", f"At $x={x}$: ${2 * (a + c) * x + 2 * (b - d)}$ cm") for a, b, c, d, x in [(5, 4, 3, 1, 6), (7, 3, 2, 1, 5), (4, 6, 5, 2, 8), (6, 2, 4, 3, 7), (8, 5, 3, 2, 4), (3, 7, 6, 4, 9)]]
          + [consec(k, n) for k, n in [(3, 7), (4, 5), (5, 6), (6, 4), (7, 3), (8, 2)]]
          + [fares(*x) for x in [(20, 15, 60, 10, 6), (30, 12, 90, 7, 15), (40, 13, 100, 8, 10), (25, 14, 65, 9, 9), (10, 18, 70, 8, 8), (35, 16, 95, 11, 14)]])
def tiles(a, b, n):
    return QQ(f"In a pattern, figure $n$ has ${a}n+{b}$ tiles. Find (i) the tiles in figure ${n}$, (ii) the total tiles in figures 1 and 2, and (iii) how many more tiles figure ${n}$ has than figure ${n - 1}$.", f"(i) ${a}({n})+{b}={a * n + b}$", f"(ii) Figure 1 $={a + b}$ and figure 2 $={2 * a + b}$", f"Total $={3 * a + 2 * b}$", f"(iii) ${a * n + b}-{a * (n - 1) + b}={a}$ more tiles")
def priya(a, x0):
    return QQ(f"Priya has ₹$x$. Her brother has ₹{a} more than twice her money. Write expressions for the brother's money and for their total money, and find both when $x={x0}$.", f"Brother's money $=2x+{a}$", f"Total $=x+(2x+{a})=3x+{a}$", f"At $x={x0}$: brother $=₹{2 * x0 + a}$", f"Total $=₹{3 * x0 + a}$")
HARD_D = [tiles(*x) for x in [(4, 3, 15), (5, 2, 12), (6, 1, 20), (3, 7, 30), (7, 4, 10), (8, 5, 9)]] + [priya(a, x0) for a, x0 in [(15, 40), (20, 35), (12, 50), (30, 25), (18, 45), (25, 60)]]

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
