"""Class 9 Maths Ch 3 - World of Numbers (rational and irrational numbers, decimal expansions, Brahmagupta's rules)."""
from c9h import *

SLUG, NAME, CHNO = "World_of_Numbers", "World of Numbers", 3

def F(fr): return f"${fx(fr)}$"
def ds_opts(fr):
    """Wrong decimal-expansion options (as TeX) for a fraction."""
    fr = Fr(fr); n, d = fr.numerator, fr.denominator
    out = []
    for c in (fr / 10, fr * 10, Fr(n + 1, d), Fr(n, d + 1), Fr(n + 2, d)):
        t = f"${dtex(c)}$"
        if c != fr and t not in out: out.append(t)
    return out
def dec_q(q, fr, why=""):
    ans = f"${dtex(fr)}$"
    return M4(q, ans, [x for x in ds_opts(fr) if x != ans], why)
def red(n, d): return Fr(n, d)

# ------------------------------------------------------------------ EASY
eA1 = [M4("Which of the following is a rational number?", c, w, "A rational number can be written as $p/q$ with $q\\ne0$.") for c, w in
       [("$\\sqrt{49}$", ["$\\sqrt{2}$", "$\\sqrt{3}$", "$\\pi$"]), ("$\\frac{7}{9}$", ["$\\sqrt{5}$", "$\\sqrt{7}$", "$\\pi$"]), ("$0.\\overline{3}$", ["$\\sqrt{11}$", "$\\sqrt{13}$", "$\\pi$"]), ("$-\\frac{5}{8}$", ["$\\sqrt{17}$", "$\\sqrt{19}$", "$\\pi$"])]]
eA2 = [M4("Which of the following is an irrational number?", f"$\\sqrt{{{n}}}$", [f"$\\sqrt{{{a * a}}}$", f"$\\frac{{{a}}}{{{a + 2}}}$", f"${a}.5$"], "The square root of a non-square natural number is irrational.") for n, a in [(2, 4), (3, 5), (5, 6), (7, 8), (10, 9)]]
eA3 = [M4(f"The decimal expansion of $\\frac{{{n}}}{{{d}}}$ is:", f"${dtex(Fr(n, d))}$", ds_opts(Fr(n, d))[:3], "Divide the numerator by the denominator.") for n, d in [(3, 4), (7, 8), (4, 5), (9, 20), (13, 25), (3, 2)]]
eA4 = [M4(f"The decimal expansion of $\\frac{{{n}}}{{{d}}}$ is:", f"${dtex(Fr(n, d))}$", ds_opts(Fr(n, d))[:3], "Divide the numerator by the denominator.") for n, d in [(1, 3), (2, 3), (1, 9), (5, 6)]]
eA5 = [M4(t, c, w, "Recall the basic facts.") for t, c, w in [
    ("A decimal expansion that ends after a finite number of digits is called:", "terminating", ["non-terminating and non-repeating", "irrational", "recurring"]),
    ("The decimal expansion of an irrational number is:", "non-terminating and non-repeating", ["terminating", "repeating", "always a whole number"]),
    ("Every integer is a:", "rational number", ["irrational number", "decimal only", "fraction with denominator $0$"]),
    ("The number $0.\\overline{7}$ is:", "rational", ["irrational", "neither rational nor irrational", "an integer"])]]
eA6 = [nm(t, c, "Apply Brahmagupta's rules for signed numbers.", pos=False) for t, c in
       [("$(-7)\\times(-6)=$", 42), ("$(-12)\\div(-4)=$", 3), ("$-8-(-5)=$", -3), ("$0-(-9)=$", 9), ("$(-5)\\times 8=$", -40), ("$(-6)+(-9)=$", -15), ("$(-35)\\div 7=$", -5), ("$4-(-11)=$", 15)]]
eA7 = [nm(f"$\\sqrt{{{n * n}}}=$", n, f"${n}^2={n * n}$") for n in [14, 17, 19, 23, 25]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([QQ(f"Write $\\frac{{{n}}}{{{d}}}$ as a decimal.", f"Divide ${n}$ by ${d}$", f"$\\frac{{{n}}}{{{d}}}={dtex(Fr(n, d))}$") for n, d in [(3, 5), (5, 8), (11, 20), (17, 25)]]
          + [QQ(f"Is ${t}$ rational or irrational? Give a reason.", reason, f"So it is {kind}") for t, reason, kind in
             [("\\sqrt{16}", "$\\sqrt{16}=4=\\frac41$", "rational"), ("\\sqrt{7}", "$7$ is not a perfect square", "irrational"), ("0.25", "$0.25=\\frac14$", "rational"), ("\\sqrt{10}", "$10$ is not a perfect square", "irrational")]]
          + [QQ(f"Evaluate: ${t}$.", f"Use the sign rule for ${t}$", f"$={c}$") for t, c in [("(-9)\\times(-4)", 36), ("(-18)\\div 3", -6), ("-7-(-12)", 5), ("(-5)+(-13)", -18)]])
def mid(a, b): return (a + b) / 2
EASY_C = ([QQ(f"Express $0.\\overline{{{d}}}$ in the form $\\frac{{p}}{{q}}$.", f"Let $x=0.\\overline{{{d}}}$; $10x={d}.\\overline{{{d}}}$", f"$10x-x={d}$, so $9x={d}$", f"$x={fx(Fr(d, 9))}$") for d in [2, 4, 5, 7, 8, 1]]
          + [QQ(f"Express $\\frac{{{n}}}{{{d}}}$ as a decimal and say whether it terminates or repeats.", f"Divide ${n}$ by ${d}$", f"${fx(Fr(n, d))}={dtex(Fr(n, d))}$", "Terminates" if term_ok(Fr(n, d)) else f"Repeats: block ${expand(Fr(n, d))[2]}$") for n, d in [(5, 12), (7, 15), (9, 11), (4, 9), (13, 40), (11, 30)]]
          + [QQ(f"Find a rational number between ${fx(Fr(a, b))}$ and ${fx(Fr(c, d))}$.", f"Add: ${fx(Fr(a, b))}+{fx(Fr(c, d))}={fx(Fr(a, b) + Fr(c, d))}$", f"Halve it: $\\frac12\\times{fx(Fr(a, b) + Fr(c, d))}$", f"A rational number between them is ${fx((Fr(a, b) + Fr(c, d)) / 2)}$") for a, b, c, d in [(1, 4, 1, 2), (1, 3, 2, 3), (1, 5, 3, 5), (2, 7, 4, 7), (1, 6, 1, 3), (3, 8, 5, 8)]])
EASY_D = ([QQ(f"Classify each of $\\sqrt{{{a}}}$, $\\sqrt{{{b}}}$, $\\sqrt{{{c}}}$, $\\frac{{{p}}}{{{q}}}$, $0.{r}$ as rational or irrational.", f"$\\sqrt{{{a}}}$ is {'rational' if isqrt(a) ** 2 == a else 'irrational'}", f"$\\sqrt{{{b}}}$ is {'rational' if isqrt(b) ** 2 == b else 'irrational'}", f"$\\sqrt{{{c}}}$ is {'rational' if isqrt(c) ** 2 == c else 'irrational'}", f"$\\frac{{{p}}}{{{q}}}$ and $0.{r}$ are rational (terminating or fraction)")
           for a, b, c, p, q, r in [(25, 6, 36, 3, 7, 6), (2, 49, 64, 5, 9, 45), (81, 11, 12, 2, 5, 125), (13, 100, 15, 7, 8, 8), (144, 17, 18, 9, 4, 2), (19, 121, 20, 4, 3, 75)]]
          + [QQ(f"Divide ${n}$ by ${d}$ and write $\\frac{{{n}}}{{{d}}}$ as a repeating decimal. After how many digits does the block repeat?", f"Long division gives remainders that repeat", f"$\\frac{{{n}}}{{{d}}}={dtex(Fr(n, d))}$", f"Repeating block ${expand(Fr(n, d))[2]}$", f"Block length $={len(expand(Fr(n, d))[2])}$", "The expansion is non-terminating and repeating, so the number is rational")
             for n, d in [(5, 11), (7, 33), (2, 11), (4, 33), (8, 11), (13, 33)]])

# ------------------------------------------------------------------ NCERT
nA1 = [nm(f"The number of decimal places in the expansion of $\\frac{{{n}}}{{2^{m}\\times5^{k}}}$ is:", max(m, k), "It is the larger of the two powers.") for n, m, k in [(3, 3, 2), (7, 2, 4), (11, 1, 3), (9, 5, 2), (13, 4, 4)]]
nA2 = [fq(f"$x=0.\\overline{{{ab}}}$ equals:", Fr(ab, 99), "Multiply by $100$ and subtract.") for ab in [27, 45, 63, 18]] 
nA3 = [M4(f"An irrational number between ${a}$ and ${a + 1}$ is:", f"$\\sqrt{{{n}}}$", [f"$\\sqrt{{{w1}}}$", f"$\\sqrt{{{w2}}}$", f"$\\sqrt{{{w3}}}$"], f"${a}^2<{n}<{(a + 1) ** 2}$") for a, n, w1, w2, w3 in [(2, 5, 3, 10, 11), (3, 11, 7, 17, 18), (4, 18, 12, 26, 27), (5, 28, 22, 37, 38)]]
nA4 = [M4(t, c, w, "Use the rules for sums and products of rational and irrational numbers.") for t, c, w in [
    ("The sum of a rational number and an irrational number is:", "irrational", ["rational", "an integer", "zero"]),
    ("The product of a non-zero rational number and an irrational number is:", "irrational", ["rational", "an integer", "zero"]),
    ("$\\sqrt{2}\\times\\sqrt{8}$ is:", "rational", ["irrational", "not a real number", "negative"]),
    ("$(\\sqrt{3}+\\sqrt{2})(\\sqrt{3}-\\sqrt{2})$ equals:", "$1$", ["$5$", "$\\sqrt{6}$", "$\\sqrt{3}-\\sqrt{2}$"])]]
nA5 = [fq(f"A rational number $\\frac{{p}}{{q}}$ equal to $0.{n}\\overline{{{r}}}$ is:", rep_frac(0, str(n), str(r)), "Use the repeating-decimal method.") for n, r in [(1, 6), (2, 3), (5, 3), (4, 6)]]
nA6 = [nm(t, c, "Use Brahmagupta's rules.", pos=False) for t, c in [("$(-15)-(-23)=$", 8), ("$(-4)\\times(-13)\\times 2=$", 104), ("$7-12=$", -5), ("$(-48)\\div(-6)=$", 8), ("$0\\times(-17)=$", 0)]]
nA7 = [M4(f"Which of the following has a terminating decimal expansion?", f"$\\frac{{{n}}}{{{d}}}$", [f"$\\frac{{{a}}}{{{b}}}$", f"$\\frac{{{c}}}{{{e}}}$", f"$\\frac{{{g}}}{{{h}}}$"], "Terminates when the denominator has only $2$ and $5$ as prime factors.") for n, d, a, b, c, e, g, h in [(7, 16, 1, 3, 5, 6, 2, 7), (9, 40, 4, 9, 1, 11, 5, 12), (17, 50, 2, 21, 3, 13, 1, 15), (11, 125, 5, 14, 7, 18, 1, 19)]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([QQ(f"Express $0.\\overline{{{d}}}$ as a fraction in lowest terms.", f"$x=0.\\overline{{{d}}}$, $10x-x={d}$", f"$x={fx(Fr(d, 9))}$") for d in [3, 6, 9, 5]]
           + [QQ(f"Write $\\frac{{{n}}}{{{d}}}$ as a decimal.", f"Divide ${n}$ by ${d}$", f"$={dtex(Fr(n, d))}$") for n, d in [(1, 6), (2, 15), (5, 16), (7, 40)]]
           + [QQ(f"Find a rational number between ${fx(Fr(a))}$ and ${fx(Fr(a + 1))}$.", f"Average: $\\frac{{{a}+{a + 1}}}{{2}}$", f"$={fx(Fr(2 * a + 1, 2))}$") for a in [3, 5, 8, 11]])
NCERT_C = ([QQ(f"Express $0.\\overline{{{ab:02d}}}$ in the form $\\frac{{p}}{{q}}$.", f"$x=0.\\overline{{{ab:02d}}}$, $100x={ab}.\\overline{{{ab:02d}}}$", f"$99x={ab}$", f"$x={fx(Fr(ab, 99))}$") for ab in [36, 15, 72, 48, 81, 27]]
           + [QQ(f"Express $0.{n}\\overline{{{r}}}$ in the form $\\frac{{p}}{{q}}$.", f"$x=0.{n}\\overline{{{r}}}$; $10x={n}.\\overline{{{r}}}$ and $100x={n}{r}.\\overline{{{r}}}$", f"$90x={int(str(n) + str(r)) - n}$", f"$x={fx(rep_frac(0, str(n), str(r)))}$") for n, r in [(1, 6), (2, 7), (3, 5), (4, 8), (5, 2), (7, 1)]]
           + [QQ(f"Find three rational numbers between ${fx(Fr(a, b))}$ and ${fx(Fr(c, b))}$.", f"Write with denominator ${b * 4}$: $\\frac{{{a * 4}}}{{{b * 4}}}$ and $\\frac{{{c * 4}}}{{{b * 4}}}$", f"Numerators ${a * 4 + 1}$, ${a * 4 + 2}$, ${a * 4 + 3}$ lie between", f"Numbers: $\\frac{{{a * 4 + 1}}}{{{b * 4}}}$, $\\frac{{{a * 4 + 2}}}{{{b * 4}}}$, $\\frac{{{a * 4 + 3}}}{{{b * 4}}}$") for a, b, c in [(1, 3, 2), (1, 5, 2), (2, 7, 3), (1, 4, 2), (3, 8, 4), (1, 6, 2)]])
NCERT_D = ([QQ(f"Find the decimal expansion of $\\frac{{1}}{{{q}}}$ by long division and state the length of the repeating block.", f"Remainders repeat after {period(q)} steps", f"$\\frac{{1}}{{{q}}}={dtex(Fr(1, q))}$", f"Block length $={period(q)}$", "Non-terminating and repeating: rational") for q in [7, 13, 21, 37, 27, 41]]
           + [QQ(f"Simplify $({a}+\\sqrt{{{b}}})({a}-\\sqrt{{{b}}})$ and $({a}+\\sqrt{{{b}}})^2$ and say which result is rational.", f"First $={a}^2-{b}={a * a - b}$ (rational)", f"Second $={a * a}+{b}+{2 * a}\\sqrt{{{b}}}$", f"$={a * a + b}+{2 * a}\\sqrt{{{b}}}$", "Irrational (contains a surd)", "Hence only the first result is rational") for a, b in [(5, 3), (4, 7), (6, 5), (3, 2), (7, 11), (2, 5)]])



# ------------------------------------------------------------------ MEDIUM
mA1 = [M4("Which of the following has a terminating decimal expansion?", f"$\\frac{{{n}}}{{{d}}}$", [f"$\\frac{{{a}}}{{{b}}}$", f"$\\frac{{{c}}}{{{e}}}$", f"$\\frac{{{g}}}{{{h}}}$"], "Reduce the fraction; only $2$ and $5$ may remain in the denominator.")
       for n, d, a, b, c, e, g, h in [(39, 65, 3, 7, 14, 21, 5, 18), (21, 70, 8, 15, 11, 39, 4, 33), (51, 85, 1, 13, 9, 14, 2, 63), (63, 140, 5, 12, 17, 51, 7, 24), (27, 45, 4, 27, 1, 7, 8, 21)]]
mA2 = [nm(f"The number of decimal places in the decimal expansion of $\\frac{{{n}}}{{{2 ** m * 5 ** k}}}$ is:", max(m, k), f"${2 ** m * 5 ** k}=2^{m}\\times5^{k}$") for n, m, k in [(7, 4, 2), (13, 1, 3), (9, 5, 3), (11, 2, 6), (3, 6, 1)]]
mA3 = [fq(f"$0.\\overline{{{ab:02d}}}$ in lowest terms is:", Fr(ab, 99), "$x=\\frac{ab}{99}$, then reduce.") for ab in [12, 54, 84, 35, 63]]
mA4 = [nm(f"The length of the repeating block in the decimal expansion of $\\frac{{1}}{{{q}}}$ is:", period(q), "Find how many digits repeat.") for q in [7, 11, 13, 37, 101]]
mA5 = [nm(f"$\\sqrt{{{a}}}\\times\\sqrt{{{b}}}=$", isqrt(a * b), "Multiply under the root.") for a, b in [(3, 12), (5, 20), (2, 18), (7, 28), (8, 50)]]
mA6 = [M4(t, c, w, "Collect the rational and irrational parts.") for t, c, w in [
    ("$\\sqrt{3}+(5-\\sqrt{3})$ is:", "rational", ["irrational", "zero", "negative"]),
    ("$(2+\\sqrt{5})+(2-\\sqrt{5})$ is:", "rational", ["irrational", "zero", "negative"]),
    ("$\\sqrt{7}+\\sqrt{7}$ is:", "irrational", ["rational", "zero", "an integer"]),
    ("$3\\times\\sqrt{2}$ is:", "irrational", ["rational", "an integer", "zero"])]]
mA7 = [M4(f"A rational number between ${fx(Fr(a, b))}$ and ${fx(Fr(c, b))}$ is:", f"${fx(Fr(a + c, 2 * b))}$", [f"${fx(Fr(c + 1, b))}$", f"${fx(Fr(a - 1, b))}$", f"${fx(Fr(c + 2, b))}$"], "Take the average.") for a, b, c in [(2, 7, 4), (3, 11, 7), (1, 9, 5), (5, 13, 9)]]
mA8 = [nm(t, c, "Apply Brahmagupta's rules in order.", pos=False) for t, c in [("$-9+(-4)\\times(-5)=$", 11), ("$(-6)\\times(-3)-(-8)=$", 26), ("$-20\\div(-5)+(-7)=$", -3), ("$(-2)\\times(-3)\\times(-4)=$", -24)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7, mA8]
MED_B = ([QQ(f"Express $0.{n}\\overline{{{r}}}$ as a fraction.", f"Multiply by $10$ and by $100$ and subtract: $90x={int(str(n) + str(r)) - n}$", f"$x={fx(rep_frac(0, str(n), str(r)))}$") for n, r in [(8, 3), (6, 1), (9, 2), (1, 8)]]
         + [QQ(f"Find the decimal expansion of $\\frac{{{n}}}{{{d}}}$.", f"Long division of ${n}$ by ${d}$", f"$={dtex(Fr(n, d))}$, block ${expand(Fr(n, d))[2]}$") for n, d in [(5, 22), (7, 36), (17, 30), (11, 18)]]
         + [QQ(f"Simplify $({a}+\\sqrt{{{b}}})({a}-\\sqrt{{{b}}})$.", f"$={a}^2-({sur(b)})^2$", f"$={a * a - b}$") for a, b in [(8, 5), (9, 7), (6, 11), (10, 3)]])
MED_C = ([QQ(f"Express $0.\\overline{{{abc:03d}}}$ as a fraction in lowest terms.", f"$1000x-x={abc}$", f"$999x={abc}$", f"$x={fx(Fr(abc, 999))}$") for abc in [27, 135, 148, 259, 333 - 111 + 1, 481]]
         + [QQ(f"Express ${ip}.{n}\\overline{{{r}}}$ in the form $\\frac{{p}}{{q}}$.", f"$x={ip}+0.{n}\\overline{{{r}}}$", f"$0.{n}\\overline{{{r}}}={fx(rep_frac(0, str(n), str(r)))}$", f"$x={fx(rep_frac(ip, str(n), str(r)))}$") for ip, n, r in [(1, 2, 3), (2, 4, 6), (3, 1, 6), (1, 5, 8), (4, 3, 3), (2, 7, 5)]]
         + [QQ(f"Without dividing, state whether $\\frac{{{n}}}{{{d}}}$ has a terminating decimal expansion.", f"Lowest terms: ${fx(Fr(n, d))}$", f"Denominator $={Fr(n, d).denominator}={ftex(Fr(n, d).denominator)}$", "Terminates, since only $2$ and $5$ occur" if term_ok(Fr(n, d)) else "Does not terminate: a prime factor other than $2$ and $5$ occurs") for n, d in [(21, 75), (13, 80), (14, 63), (33, 110), (7, 60), (19, 400)]])
MED_D = ([QQ(f"Express ${ip}.{n}\\overline{{{r}}}$ as $\\frac{{p}}{{q}}$ and verify by long division of $p$ by $q$.", f"Let $x={ip}.{n}\\overline{{{r}}}$; $10x$ and $100x$ give $90x={int(str(ip) + str(n) + str(r)) - int(str(ip) + str(n))}$", f"$x={fx(rep_frac(ip, str(n), str(r)))}$", f"Long division: ${dtex(rep_frac(ip, str(n), str(r)))}$", "Matches the given decimal") for ip, n, r in [(1, 1, 6), (2, 3, 3), (3, 2, 5), (1, 4, 7), (2, 6, 1), (4, 5, 2)]]
          + [QQ(f"Simplify $({a}+\\sqrt{{{b}}})^2+({a}-\\sqrt{{{b}}})^2$ and state whether the result is rational.", f"$({a}+\\sqrt{{{b}}})^2={a * a + b}+{2 * a}\\sqrt{{{b}}}$", f"$({a}-\\sqrt{{{b}}})^2={a * a + b}-{2 * a}\\sqrt{{{b}}}$", f"Sum $={2 * (a * a + b)}$", "The surd terms cancel", "Result is rational") for a, b in [(3, 5), (4, 3), (2, 7), (5, 2), (6, 7), (1, 11)]])

# ------------------------------------------------------------------ HARD
hA1 = [fq(f"The value of $0.\\overline{{{a}}}+0.\\overline{{{b}}}$ is:", Fr(a + b, 9), "Each is $\\frac{d}{9}$.") for a, b in [(2, 5), (4, 8), (3, 7), (1, 4)]]
hA2 = [fq(f"$0.\\overline{{{a}{b}}}+0.\\overline{{{b}{a}}}$ equals:", Fr((a + b) * 11, 99), "Add the numerators over $99$.") for a, b in [(1, 3), (2, 6), (4, 5), (3, 8)]]
hA3 = [nm(f"The smallest natural number $n$ for which $\\frac{{n}}{{{d}}}$ has a terminating decimal expansion is:", n, "Cancel every prime factor other than $2$ and $5$.") for d, n in [(2 ** 3 * 3 * 5, 3), (2 * 5 * 7 * 7, 49), (2 ** 2 * 3 * 7, 21), (5 ** 2 * 11, 11)]]
hA4 = [nm(f"If $x={a}+\\sqrt{{{b}}}$ with ${a}^2-{b}=1$, then $x+\\frac{{1}}{{x}}=$", 2 * a, f"$\\frac1x={a}-\\sqrt{{{b}}}$, so the sum is $2\\times{a}$.") for a, b in [(2, 3), (3, 8), (4, 15), (5, 24)]]
hA5 = [fq(f"$1.\\overline{{{ab:02d}}}$ in the form $\\frac{{p}}{{q}}$ is:", rep_frac(1, "", f"{ab:02d}"), "Write as $1+0.\\overline{ab}$.") for ab in [27, 36, 45, 63]]
hA6 = [M4(t, c, w, "Reason about decimal expansions.") for t, c, w in [
    ("The value of $0.\\overline{9}$ is:", "$1$", ["$0.9$", "$0.99$", "just less than $1$"]),
    ("A number whose decimal expansion is $0.1010010001\\ldots$ (the number of zeros increasing) is:", "irrational", ["rational", "an integer", "a terminating decimal"]),
    ("Between any two distinct rational numbers there are:", "infinitely many rational numbers", ["no rational numbers", "exactly one rational number", "exactly two rational numbers"]),
    ("If $\\sqrt{2}$ is irrational, then $3+\\sqrt{2}$ is:", "irrational", ["rational", "an integer", "zero"])]]
hA7 = [nm(f"The length of the repeating block of $\\frac{{1}}{{{q}}}$ is:", period(q), "Find the order of $10$ modulo $q$.") for q in [41, 27, 21, 101]]
hA8 = [fq(f"$0.\\overline{{{ab:02d}}}\\times 11$ equals:", Fr(ab * 11, 99), "Multiply the fraction by $11$ and reduce.") for ab in [18, 27, 45, 72]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"Express $0.\\overline{{{a}{b}}}+0.\\overline{{{b}{a}}}$ as a single fraction in lowest terms.", f"$0.\\overline{{{a}{b}}}=\\frac{{{a * 10 + b}}}{{99}}$, $0.\\overline{{{b}{a}}}=\\frac{{{b * 10 + a}}}{{99}}$", f"Sum $={fx(Fr(11 * (a + b), 99))}$") for a, b in [(1, 7), (2, 9), (3, 6), (5, 8)]]
          + [QQ(f"Find the smallest natural number $n$ such that $\\frac{{n}}{{{d}}}$ has a terminating decimal expansion.", f"${d}={ftex(d)}$", f"Cancel the factors other than $2$ and $5$: $n={n}$") for d, n in [(2 ** 2 * 3 * 5 * 7, 21), (3 ** 2 * 2 * 5, 9), (2 * 5 * 11 * 13, 143), (2 ** 3 * 3 ** 2 * 7, 63)]]
          + [QQ(f"If $x={a}+\\sqrt{{{b}}}$, find $\\frac1x$ and $x+\\frac1x$.", f"$\\frac1x=\\frac{{{a}-\\sqrt{{{b}}}}}{{{a}^2-{b}}}={a}-\\sqrt{{{b}}}$", f"$x+\\frac1x={2 * a}$") for a, b in [(6, 35), (7, 48), (8, 63), (9, 80)]])
HARD_C = ([QQ(f"Express ${ip}.{n}\\overline{{{r}}}$ as a fraction in lowest terms and verify by long division.", f"$x={ip}.{n}\\overline{{{r}}}$: $100x-10x={int(str(ip) + str(n) + str(r)) - int(str(ip) + str(n))}$", f"$x={fx(rep_frac(ip, str(n), str(r)))}$", f"Long division of $p$ by $q$ gives ${dtex(rep_frac(ip, str(n), str(r)))}$") for ip, n, r in [(0, 4, 7), (5, 3, 2), (6, 7, 9), (0, 9, 4), (7, 1, 8), (8, 2, 3)]]
          + [QQ(f"If $x={a}+\\sqrt{{{b}}}$, find $x^2+\\frac{{1}}{{x^2}}$.", f"$\\frac1x={a}-\\sqrt{{{b}}}$ since ${a}^2-{b}=1$, so $x+\\frac1x={2 * a}$", f"$x^2+\\frac{{1}}{{x^2}}=\\left(x+\\frac1x\\right)^2-2$", f"$={4 * a * a}-2={4 * a * a - 2}$") for a, b in [(2, 3), (3, 8), (4, 15), (5, 24), (6, 35), (7, 48)]]
          + [QQ(f"Given that $\\sqrt{{{b}}}$ is irrational, prove that ${a}+\\sqrt{{{b}}}$ is irrational.", f"Suppose ${a}+\\sqrt{{{b}}}=r$ is rational", f"Then $\\sqrt{{{b}}}=r-{a}$", "$r-" + str(a) + "$ is rational, so $\\sqrt{" + str(b) + "}$ would be rational", "This contradicts the given fact") for a, b in [(3, 2), (5, 3), (7, 5), (4, 6), (2, 7), (9, 10)]])
HARD_D = ([QQ(f"Find the decimal expansion of $\\frac{{{p}}}{{{q}}}$ by long division, state the repeating block and its length, and hence write $\\frac{{{p}}}{{{q}}}$ as a repeating decimal.", f"Divide ${p}$ by ${q}$ until a remainder repeats", f"$\\frac{{{p}}}{{{q}}}={dtex(Fr(p, q))}$", f"Block ${expand(Fr(p, q))[2]}$", f"Block length $={period(q)}$", "Repeating, so the number is rational")
           for p, q in [(3, 7), (5, 13), (4, 41), (10, 37), (7, 27), (12, 101)]]
          + [QQ(f"Simplify $(\\sqrt{{{a}}}+\\sqrt{{{b}}})^2+(\\sqrt{{{a}}}-\\sqrt{{{b}}})^2$ and $(\\sqrt{{{a}}}+\\sqrt{{{b}}})(\\sqrt{{{a}}}-\\sqrt{{{b}}})$. Which are rational?", f"First $=2({a}+{b})={2 * (a + b)}$", f"Second $={a}-{b}={a - b}$", "Both are rational", f"In the first, the cross terms $\\pm2\\sqrt{{{a * b}}}$ cancel") for a, b in [(7, 5), (11, 3), (13, 2), (10, 6), (17, 8), (19, 7)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
