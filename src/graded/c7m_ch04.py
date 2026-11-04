"""Class 7 Maths Ch 4 - Expressions using Letter-Numbers (variables, forming/evaluating/simplifying expressions)."""
from g67 import *

SLUG, NAME, CHNO = "Letter_Numbers", "Expressions using Letter-Numbers", 4

def term(c, v, first=False):
    if c == 0: return ""
    s = ("-" if c < 0 else ("" if first else "+")) 
    a = abs(c)
    body = (str(a) if (a != 1 or not v) else "") + v
    return s + body
def lin(*ts):
    """ts = (coef, var) pairs -> '3x-2y+5' ; var '' means constant"""
    out = ""
    for c, v in ts:
        t = term(c, v, first=(out == ""))
        out += t
    return out or "0"
def L(*ts): return "$" + lin(*ts) + "$"
def sp(*ts): return lin(*ts).replace("+", " + ").replace("-", " - ").lstrip(" ").replace("- ", "-", 1) if lin(*ts).startswith("-") else lin(*ts).replace("+", " + ").replace("-", " - ")
def E(*ts): return "$" + sp(*ts) + "$"
def num(q, c, why="", offs=(1, -1, 2, -2, 3, 5, 10)): return nm(q, c, why, offs=offs, pos=False)

# ------------------------------------------------ EASY
eA1 = [num(f"If $x={x}$, the value of ${a}x+{b}$ is:", a * x + b, "Replace x by its value and calculate.") for a, b, x in [(2, 3, 4), (3, 1, 5), (5, 2, 3), (4, 6, 2), (6, 5, 1)]]
eA2 = [num(f"If $y={y}$, the value of ${a}y-{b}$ is:", a * y - b, "Substitute and subtract.") for a, b, y in [(3, 4, 5), (2, 7, 6), (4, 3, 4), (5, 8, 3)]]
eA3 = [tm(t, c, w, "Translate the words into a letter-number expression.") for t, c, w in [
    ("5 more than a number $n$ is:", "$n+5$", ["$5n$", "$n-5$", "$5-n$"]),
    ("3 times a number $m$ is:", "$3m$", ["$m+3$", "$m-3$", "$m/3$"]),
    ("7 less than a number $p$ is:", "$p-7$", ["$7-p$", "$7p$", "$p+7$"]),
    ("A number $k$ divided by 4 is:", "$k/4$", ["$4k$", "$k+4$", "$4/k$"]),
    ("Twice a number $t$ increased by 1 is:", "$2t+1$", ["$2(t+1)$", "$t+2$", "$2t-1$"])]]
eA4 = [tm(f"The number of terms in the expression {E(*ts)} is:", str(len(ts)), [str(len(ts) + 1), str(len(ts) + 2), str(max(1, len(ts) - 1))], "Terms are separated by + or - signs.") for ts in [((3, "x"), (2, "y"), (5, "")), ((4, "a"), (7, "")), ((1, "p"), (1, "q"), (1, "r"), (9, "")), ((6, "m"),)]]
eA5 = [tm(f"The coefficient of $x$ in {E(*ts)} is:", str(ts[0][0]), [str(ts[0][0] + 1), str(ts[0][0] + 2), str(-ts[0][0] if ts[0][0] else 1)], "The coefficient is the number multiplying the letter.") for ts in [((7, "x"), (2, "")), ((3, "x"), (4, "y")), ((9, "x"), (5, "")), ((12, "x"), (1, "z"))]]
eA6 = [tm(f"Which pair are like terms?", c, w, "Like terms have the same letter part.") for c, w in [
    ("$3x$ and $9x$", ["$3x$ and $9y$", "$2x$ and $2x^2$", "$5$ and $5x$"]),
    ("$4y$ and $-y$", ["$4y$ and $4z$", "$y$ and $y^2$", "$4$ and $y$"]),
    ("$7ab$ and $2ab$", ["$7ab$ and $2a$", "$7a$ and $2b$", "$ab$ and $a^2b$"]),
    ("$6p$ and $p$", ["$6p$ and $6$", "$6p$ and $q$", "$p^2$ and $p$"])]]
eA7 = [num(f"If $a={a}$ and $b={b}$, then $a+b$ is:", a + b, "Add the two values.") for a, b in [(3, 9), (12, 5), (8, 8), (15, 6)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([QQ(f"Find the value of ${a}x+{b}$ when $x={x}$.", f"Substitute: ${a}({x})+{b}$", f"$={a*x+b}$") for a, b, x in [(2, 5, 3), (4, 1, 6), (3, 7, 5), (6, 2, 4)]]
          + [QQ(f"Write as an expression: {t}.", f"Identify the operations", f"Expression: ${e}$") for t, e in [("7 added to 4 times $n$", "4n+7"), ("3 subtracted from twice $m$", "2m-3"), ("5 times the sum of $a$ and 2", "5(a+2)"), ("$x$ taken away from 20", "20-x")]]
          + [QQ(f"Add {E(*u)} and {E(*v)}.", "Group like terms", f"Sum ${lin((u[0][0]+v[0][0],'x'),(u[1][0]+v[1][0],''))}$") for u, v in [(((3, "x"), (4, "")), ((2, "x"), (1, ""))), (((5, "x"), (2, "")), ((4, "x"), (6, ""))), (((7, "x"), (3, "")), ((1, "x"), (8, ""))), (((2, "x"), (9, "")), ((6, "x"), (5, "")))]])
EASY_C = ([QQ(f"Find the value of ${a}x+{b}y$ when $x={x}$ and $y={y}$.", f"Substitute: ${a}({x})+{b}({y})$", f"$={a*x}+{b*y}$", f"$={a*x+b*y}$") for a, b, x, y in [(2, 3, 4, 5), (3, 2, 6, 7), (5, 4, 2, 3), (4, 1, 8, 9), (6, 5, 3, 2), (7, 2, 4, 6)]]
          + [QQ(f"Simplify: ${a}x+{b}x-{c}x$.", "All terms are like terms", f"Coefficients: ${a}+{b}-{c}={a+b-c}$", f"Answer ${a+b-c}x$") for a, b, c in [(7, 4, 3), (9, 6, 5), (12, 5, 8), (15, 3, 9), (10, 10, 4), (8, 7, 6)]]
          + [QQ(f"Write an expression and find its value: the cost of {n} pens at ₹$p$ each, if $p={p}$.", f"Cost $={n}p$", f"At $p={p}$: ${n}\\times{p}$", f"$=₹{n*p}$") for n, p in [(5, 12), (8, 15), (6, 20), (9, 11), (12, 8), (7, 14)]])
EASY_D = ([QQ(f"Anil is $x$ years old. His sister is {k} years younger. Write the expressions for sister's age and the sum of both ages. Find both when $x={x}$.", f"Sister $=x-{k}$", f"Sum $=2x-{k}$", f"At $x={x}$: sister $={x-k}$", f"Sum $={2*x-k}$") for k, x in [(3, 15), (5, 18), (4, 20), (2, 12), (6, 25), (7, 22)]]
          + [QQ(f"A rectangle has length $l$ cm and breadth {b} cm. Write expressions for its perimeter and area, and find both when $l={l}$.", f"Perimeter $=2(l+{b})$", f"Area $={b}l$", f"At $l={l}$: perimeter $={2*(l+b)}$ cm", f"Area $={b*l}$ cm$^2$") for b, l in [(4, 9), (5, 12), (3, 10), (6, 8), (7, 11), (2, 15)]])

# ------------------------------------------------ NCERT
nA1 = [num(f"The perimeter of a square of side $s$ is ${4}s$. For $s={s}$ cm it is (cm):", 4 * s, "Perimeter = 4 × side.") for s in (7, 12, 9, 15, 20)]
nA2 = [tm(t, c, w, "Write the rule using a letter-number.") for t, c, w in [
    ("The rule 'multiply by 5 and add 2' for the input $n$ is:", "$5n+2$", ["$5(n+2)$", "$n+7$", "$2n+5$"]),
    ("A rule gives 7, 12, 17, 22 for $n=1,2,3,4$. The rule is:", "$5n+2$", ["$5n$", "$n+6$", "$7n$"]),
    ("The $n$th even number is:", "$2n$", ["$2n+1$", "$n+2$", "$2n-1$"]),
    ("The $n$th odd number is:", "$2n-1$", ["$2n$", "$2n+2$", "$n-1$"])]]
nA3 = [num(f"If $m={m}$, the value of ${a}m^2$... is skipped; $m+{a}m$ equals:", m + a * m, "Combine like terms $m+am=(1+a)m$.") if False else num(f"If $m={m}$, the value of $m+{a}m$ is:", m + a * m, "Combine like terms first: $(1+a)m$.") for m, a in [(4, 3), (6, 2), (5, 4), (3, 7)]]
nA4 = [tm(f"Subtract ${b}x$ from ${a}x$: the result is:", f"${a-b}x$", [f"${a+b}x$", f"${b-a}x$", f"${a-b}$"], "Subtract the coefficients of like terms.") for a, b in [(9, 4), (12, 5), (15, 8), (20, 11)]]
nA5 = [num(f"The value of ${a}(x+{b})$ for $x={x}$ is:", a * (x + b), "Add inside the bracket first.") for a, b, x in [(2, 3, 4), (3, 2, 5), (4, 1, 6), (5, 3, 2)]]
nA6 = [tm(t, c, w, "Use brackets to keep the order of operations.") for t, c, w in [
    ("'Four times the sum of $x$ and 3' is:", "$4(x+3)$", ["$4x+3$", "$x+12$", "$4+3x$"]),
    ("'Sum of $y$ and twice $z$' is:", "$y+2z$", ["$2(y+z)$", "$2yz$", "$y\\cdot z+2$"]),
    ("'Difference of $a$ and $b$, doubled' is:", "$2(a-b)$", ["$2a-b$", "$a-2b$", "$2a-2$"])]]
nA6 += [tm("'Product of $p$ and $q$, increased by 5' is:", "$pq+5$", ["$p(q+5)$", "$p+q+5$", "$5pq$"], "Product first, then add."), tm("'Half of the sum of $a$ and $b$' is:", "$(a+b)/2$", ["$a+b/2$", "$2(a+b)$", "$a/2b$"], "Brackets keep the sum together.")]
nA7 = [num(f"A taxi charges ₹{f} fixed plus ₹{r} per km. For $k={k}$ km the fare is (₹):", f + r * k, "Fare $=f+rk$.") for f, r, k in [(50, 12, 5), (40, 15, 4), (60, 10, 8), (30, 18, 3)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Find the number of matchsticks needed for {n} squares in a row if each square needs 4 sticks but neighbours share one: use $3n+1$.", f"Rule: $3n+1$", f"For $n={n}$: $3({n})+1={3*n+1}$") for n in (5, 8, 10, 12)]
           + [QQ(f"Simplify: ${a}x+{b}-{c}x+{d}$.", f"Like terms: $({a}-{c})x$ and $({b}+{d})$", f"${a-c}x+{b+d}$") for a, b, c, d in [(7, 4, 3, 6), (9, 2, 5, 8), (12, 5, 7, 3), (10, 9, 4, 1)]]
           + [QQ(f"Find the value of ${a}p-{b}q$ for $p={p}$, $q={q}$.", f"Substitute: ${a}({p})-{b}({q})$", f"$={a*p-b*q}$") for a, b, p, q in [(5, 3, 6, 4), (4, 7, 9, 2), (8, 2, 5, 3), (6, 5, 7, 6)]])
NCERT_C = ([QQ(f"In a pattern, the number of dots in figure $n$ is $3n+2$. Find the dots in figure {n}, and which figure has {3*m+2} dots.", f"Figure {n}: $3({n})+2={3*n+2}$", f"Solve $3n+2={3*m+2}$", f"$n={m}$") for n, m in [(4, 9), (6, 11), (10, 7), (8, 12), (5, 15), (12, 6)]]
           + [QQ(f"Add ${a}x+{b}y$ and ${c}x-{d}y$.", "Group the x-terms and y-terms", f"$x$: ${a}+{c}={a+c}$", f"Sum ${a+c}x+{b-d}y$" if b - d >= 0 else f"Sum ${a+c}x{b-d}y$") for a, b, c, d in [(5, 9, 3, 4), (7, 6, 2, 1), (4, 8, 6, 3), (9, 5, 1, 2), (2, 10, 8, 7), (6, 4, 5, 3)]]
           + [QQ(f"The age of a father is {k} times his son's age $s$ plus {a} years. Write the expression, and find the father's age when $s={s}$.", f"Father $={k}s+{a}$", f"At $s={s}$: ${k}({s})+{a}$", f"$={k*s+a}$ years") for k, a, s in [(3, 2, 10), (2, 8, 14), (3, 5, 12), (4, 2, 9), (2, 6, 16), (3, 1, 11)]])
NCERT_D = ([QQ(f"A school buys $n$ notebooks at ₹{a} each and {k} pens at ₹{b} each. Write the total cost, and find it when $n={n}$. If ₹{pay} is paid, find the change.", f"Notebooks cost ${a}n$", f"Total $={a}n+{k*b}$", f"At $n={n}$: ${a*n+k*b}$", f"Change $={pay-(a*n+k*b)}$") for a, b, k, n, pay in [(12, 5, 4, 10, 200), (15, 8, 3, 8, 200), (9, 6, 5, 12, 200), (20, 4, 6, 7, 200), (18, 10, 2, 9, 250), (14, 7, 3, 15, 300)]]
           + [QQ(f"A hall has {a} rows of $r$ chairs and {b} extra chairs at the back. Write the total number of chairs. Find it for $r={r}$, and the value of $r$ if the total is {a*s+b}.", f"Total $={a}r+{b}$", f"At $r={r}$: ${a*r+b}$", f"Solve ${a}r+{b}={a*s+b}$", f"${a}r={a*s}$", f"$r={s}$") for a, b, r, s in [(8, 6, 12, 15), (10, 4, 9, 14), (6, 8, 15, 20), (12, 5, 10, 8), (9, 3, 11, 13), (7, 9, 14, 18)]])

# ------------------------------------------------ MEDIUM
mA1 = [num(f"Value of ${a}x+{b}y-{c}$ for $x={x}$, $y={y}$ is:", a * x + b * y - c, "Substitute both values.") for a, b, c, x, y in [(3, 2, 5, 4, 6), (5, 3, 7, 2, 9), (4, 6, 10, 5, 3), (7, 2, 4, 3, 8)]]
mA2 = [tm(f"Simplify ${a}x+{b}y-{c}x+{d}y$:", f"${a-c}x+{b+d}y$", [f"${a+c}x+{b+d}y$", f"${a-c}x+{b-d}y$", f"${a-c+b+d}xy$"], "Collect like terms separately.") for a, b, c, d in [(9, 4, 5, 3), (12, 7, 4, 2), (8, 5, 3, 6), (15, 2, 9, 8)]]
mA3 = [num(f"If $x={x}$, then ${a}(x-{b})+{c}$ equals:", a * (x - b) + c, "Brackets first.") for a, b, c, x in [(3, 2, 5, 8), (4, 3, 7, 9), (5, 1, 2, 6), (2, 4, 9, 10)]]
mA4 = [tm(f"Subtract ${a}x+{b}$ from ${c}x+{d}$:", f"${c-a}x+{d-b}$" if d - b >= 0 else f"${c-a}x{d-b}$", [f"${c+a}x+{d+b}$", f"${a-c}x+{b-d}$", f"${c-a}x+{d+b}$"], "Change signs of the subtracted expression.") for a, b, c, d in [(3, 2, 8, 9), (4, 1, 10, 7), (2, 5, 9, 8), (6, 3, 11, 12)]]
mA5 = [num(f"The nth term of a pattern is ${a}n+{b}$. Its {n}th term is:", a * n + b, "Substitute n.") for a, b, n in [(4, 3, 10), (6, 1, 12), (5, 7, 8), (3, 9, 15)]]
mA6 = [tm(f"If a pencil costs ₹$x$ and an eraser ₹$y$, the cost of {a} pencils and {b} erasers is:", f"${a}x+{b}y$", [f"${a+b}xy$", f"${a}y+{b}x$", f"${a*b}(x+y)$"], "Multiply price by quantity.") for a, b in [(3, 5), (6, 2), (4, 7), (8, 3)]]
mA7 = [num(f"If $a={a}$, the value of $a^2+{k}a$ is:", a * a + k * a, "Square first.") for a, k in [(3, 2), (4, 5), (5, 3), (6, 4)]]
mA7 += [num(f"If $x={x}$, the value of $\\frac{{{a}x+{b}}}{{{c}}}$ is:", (a*x+b)//c, "Substitute then divide.") for a, b, c, x in [(4, 2, 2, 5), (6, 3, 3, 4)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([QQ(f"Simplify: ${a}(x+{b})+{c}x$.", f"Expand: ${a}x+{a*b}$", f"Add ${c}x$: ${a+c}x+{a*b}$") for a, b, c in [(3, 4, 5), (2, 7, 6), (4, 3, 2), (5, 2, 8)]]
         + [QQ(f"Subtract ${a}x-{b}$ from ${c}x+{d}$.", f"$({c}x+{d})-({a}x-{b})$", f"$={c-a}x+{d+b}$") for a, b, c, d in [(3, 5, 9, 2), (4, 1, 11, 6), (2, 7, 8, 3), (5, 4, 12, 9)]]
         + [QQ(f"Find the value of $x^2+{a}x-{b}$ when $x={x}$.", f"Substitute: ${x}^2+{a}({x})-{b}$", f"$={x*x+a*x-b}$") for a, b, x in [(3, 4, 5), (2, 9, 6), (5, 7, 4), (4, 3, 7)]])
MED_C = ([QQ(f"The sum of two numbers is $s$ and one of them is ${a}s/{b}$... " , "") if False else QQ(f"A number is ${a}n+{b}$. Another is ${c}n-{d}$. Find their sum and difference (first minus second), and evaluate both for $n={n}$.", f"Sum $={a+c}n+{b-d}$", f"Difference $={a-c}n+{b+d}$", f"At $n={n}$: sum $={(a+c)*n+b-d}$, difference $={(a-c)*n+b+d}$") for a, b, c, d, n in [(7, 5, 3, 2, 4), (9, 4, 5, 1, 3), (8, 6, 2, 3, 5), (10, 3, 6, 4, 2), (12, 7, 5, 6, 3), (11, 2, 4, 1, 6)]]
         + [QQ(f"Matchsticks make a row of triangles: $n$ triangles need $2n+1$ sticks. How many sticks for {n} triangles? How many triangles can be made with {2*m+1} sticks?", f"For {n}: $2({n})+1={2*n+1}$", f"Solve $2n+1={2*m+1}$", f"$n={m}$") for n, m in [(9, 14), (12, 20), (15, 25), (7, 18), (20, 30), (11, 16)]]
         + [QQ(f"A cab charges ₹{f} plus ₹{r} per km. Write the fare for $k$ km. A rider pays ₹{f+r*k}. Find $k$, and the fare for {k+5} km.", f"Fare $={f}+{r}k$", f"${f}+{r}k={f+r*k}$ gives ${r}k={r*k}$", f"$k={k}$", f"Fare for {k+5} km $=₹{f+r*(k+5)}$") for f, r, k in [(45, 11, 8), (60, 9, 12), (35, 14, 6), (50, 13, 10), (40, 16, 7), (55, 12, 9)]])
MED_D = ([QQ(f"A shopkeeper sells $x$ kg of rice at ₹{a} per kg and $y$ kg of wheat at ₹{b} per kg. Write his earning. Find it for $x={x}$, $y={y}$ and the average price per kg (to the nearest rupee).", f"Earning $={a}x+{b}y$", f"At given values: ${a*x}+{b*y}$", f"$=₹{a*x+b*y}$", f"Average $=\\frac{{{a*x+b*y}}}{{{x+y}}}\\approx₹{round((a*x+b*y)/(x+y))}$") for a, b, x, y in [(48, 36, 10, 15), (52, 40, 12, 8), (45, 30, 20, 10), (60, 44, 5, 15), (38, 28, 16, 24), (55, 35, 8, 12)]]
         + [QQ(f"Raju is $r$ years old. His mother is {a} years older than 3 times his age. In {k} years, find the expressions for each age and the sum of ages. Evaluate at $r={r}$.", f"Mother now $=3r+{a}$", f"Raju after {k} years $=r+{k}$", f"Mother after {k} years $=3r+{a+k}$", f"Sum $=4r+{a+2*k}$; at $r={r}$: ${4*r+a+2*k}$") for a, k, r in [(4, 5, 10), (6, 3, 12), (2, 8, 9), (5, 6, 11), (3, 4, 14), (7, 2, 8)]])

# ------------------------------------------------ HARD
hA1 = [num(f"If $a={a}$, $b={b}$, the value of ${p}a^2-{q}b$ is:", p * a * a - q * b, "Square first, then multiply.") for a, b, p, q in [(3, 4, 5, 6), (4, 5, 3, 7), (5, 2, 2, 9), (6, 3, 4, 8)]]
hA2 = [num(f"If $x={x}$, the value of $(x+{a})(x-{b})$ is:", (x + a) * (x - b), "Evaluate each bracket then multiply.") for a, b, x in [(3, 2, 7), (5, 4, 9), (2, 1, 8), (6, 3, 10)]]
hA3 = [tm(f"The expression for the area of a square of side $({a}x+{b})$... skip" if False else f"Perimeter of a rectangle with sides ${a}x+{b}$ and ${c}x-{d}$ is:", f"${2*(a+c)}x+{2*(b-d)}$", [f"${a+c}x+{b-d}$", f"${2*(a-c)}x+{2*(b+d)}$", f"${2*(a*c)}x$"], "Perimeter $=2(l+b)$.") for a, b, c, d in [(5, 4, 3, 1), (7, 6, 2, 3), (4, 9, 6, 5), (8, 2, 5, 1)]]
hA4 = [num(f"If $n={n}$, then $\\frac{{n(n+1)}}{{2}}$ equals:", n * (n + 1) // 2, "Triangular numbers.") for n in (10, 14, 20, 25)]
hA5 = [tm(t, c, w, "Check by substituting a value.") for t, c, w in [
    ("Which is always an even number for integer $n$?", "$2n+4$", ["$2n+1$", "$n+2$", "$3n$"]),
    ("Which is always an odd number for integer $n$?", "$4n+3$", ["$4n+2$", "$n+3$", "$2n+4$"]),
    ("Which is a multiple of 5 for every integer $n$?", "$10n+5$", ["$5n+1$", "$10n+2$", "$n+5$"]),
    ("The sum of three consecutive integers starting at $n$ is:", "$3n+3$", ["$3n+1$", "$n+3$", "$3n$"])]]
hA6 = [num(f"If $x={x}$ and $y={y}$, the value of ${a}x-{b}y+xy$ is:", a * x - b * y + x * y, "Substitute carefully; xy is a product.") for a, b, x, y in [(3, 2, 4, 5), (5, 4, 3, 6), (2, 7, 5, 2), (6, 3, 4, 4)]]
hA7 = [num(f"Rule: output $=3\\times$input$-{k}$. The output for input {i} is:", 3 * i - k, "Apply the rule.") for k, i in [(4, 9), (7, 12), (2, 15), (5, 20)]]
hA7 += [num(f"If $x={x}$, the value of $x^2-{a}x+{b}$ is:", x*x-a*x+b, "Substitute and simplify.") for a, b, x in [(5, 6, 8), (7, 10, 9)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7]
HARD_B = ([QQ(f"Simplify: ${a}(x-{b})-{c}(x-{d})$.", f"Expand: ${a}x-{a*b}-{c}x+{c*d}$", f"${a-c}x{c*d-a*b:+d}$") for a, b, c, d in [(7, 2, 3, 5), (9, 3, 4, 2), (8, 1, 5, 4), (6, 4, 2, 7)]]
          + [QQ(f"Show that the sum of {k} consecutive integers starting at $n$ is divisible by {k}... for k=3: $n+(n+1)+(n+2)$." , "") if False else QQ(f"Write the sum of the three consecutive multiples of {k}, starting with ${k}n$, and simplify.", f"${k}n+{k}(n+1)+{k}(n+2)$", f"$={3*k}n+{3*k}={3*k}(n+1)$") for k in (2, 5, 4, 6)]
          + [QQ(f"Find the value of ${a}x^2-{b}x+{c}$ at $x={x}$.", f"Substitute: ${a}({x})^2-{b}({x})+{c}$", f"$={a*x*x-b*x+c}$") for a, b, c, x in [(2, 3, 4, 5), (3, 5, 1, 4), (4, 2, 6, 3), (5, 6, 7, 2)]])
HARD_C = ([QQ(f"A rectangle has length $({a}x+{b})$ and breadth $({c}x-{d})$ cm. Find the perimeter as an expression and its value for $x={x}$.", f"$P=2[({a}x+{b})+({c}x-{d})]$", f"$=2[{a+c}x+{b-d}]$", f"$={2*(a+c)}x+{2*(b-d)}$", f"At $x={x}$: ${2*(a+c)*x+2*(b-d)}$ cm") for a, b, c, d, x in [(5, 4, 3, 1, 6), (7, 3, 2, 1, 5), (4, 6, 5, 2, 8), (6, 2, 4, 3, 7), (8, 5, 3, 2, 4), (3, 7, 6, 4, 9)]]
          + [QQ(f"Show that ${a}n+{b}$ is always odd for every whole number $n$ when {a} is even and {b} is odd. Verify for $n={n}$ and $n={n+1}$.", f"${a}n$ is even (even × any integer)", "Even + odd = odd", f"$n={n}$: ${a*n+b}$ odd", f"$n={n+1}$: ${a*(n+1)+b}$ odd") for a, b, n in [(4, 3, 5), (6, 1, 7), (8, 5, 3), (10, 7, 4), (12, 9, 6), (2, 11, 8)]]
          + [QQ(f"Two taxis: A charges ₹{fa} plus ₹{ra} per km, B charges ₹{fb} plus ₹{rb} per km. Write both fares for $k$ km. For which $k$ are they equal? (Solve ${fa}+{ra}k={fb}+{rb}k$.)", f"A $={fa}+{ra}k$, B $={fb}+{rb}k$", f"Equate: ${ra-rb}k={fb-fa}$", f"$k={(fb-fa)//(ra-rb)}$ km", f"Fare then ₹{fa+ra*((fb-fa)//(ra-rb))}") for fa, ra, fb, rb in [(20, 15, 60, 10), (30, 12, 90, 7), (10, 18, 70, 8), (25, 14, 85, 9), (40, 13, 100, 8), (15, 20, 75, 10)]])
HARD_D = ([QQ(f"In a pattern of figures, figure $n$ has ${a}n+{b}$ tiles. (i) Tiles in figure {n}. (ii) Which figure has {a*m+b} tiles? (iii) Is {a*m+b+1} tiles possible (give reason)? (iv) Total tiles in figures 1 and 2.", f"(i) ${a*n+b}$", f"(ii) ${a}n={a*m}$ so $n={m}$", f"(iii) ${a}n={a*m+1-b+b-0}$..." , "") if False else QQ(f"In a pattern, figure $n$ has ${a}n+{b}$ tiles. Find (i) tiles in figure {n}; (ii) the figure with {a*m+b} tiles; (iii) the total tiles in figures 1 and 2.", f"(i) ${a}({n})+{b}={a*n+b}$", f"(ii) ${a}n+{b}={a*m+b}$ gives ${a}n={a*m}$", f"$n={m}$", f"(iii) Figure 1 $={a+b}$, figure 2 $={2*a+b}$", f"Total $={3*a+2*b}$") for a, b, n, m in [(4, 3, 15, 22), (5, 2, 12, 18), (6, 1, 20, 25), (3, 7, 30, 14), (7, 4, 10, 16), (8, 5, 9, 13)]]
          + [QQ(f"Priya has ₹$x$. Her brother has ₹{a} more than twice her money. Together they have ₹{3*x0+a}. Write the expression for the total, form the equation, and find $x$. Also find the brother's money.", f"Brother $=2x+{a}$", f"Total $=x+2x+{a}=3x+{a}$", f"$3x+{a}={3*x0+a}$ so $3x={3*x0}$", f"$x={x0}$", f"Brother $=₹{2*x0+a}$") for a, x0 in [(15, 40), (20, 35), (12, 50), (30, 25), (18, 45), (25, 60)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
