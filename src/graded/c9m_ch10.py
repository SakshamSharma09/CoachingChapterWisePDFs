"""Class 9 Maths Ch 10 - How Quantities Combine (Understanding Data): combined and weighted averages, mixtures, stacked bars."""
from g9m import *
from fractions import Fraction as Fraction_

SLUG, NAME, CHNO = "Understanding_Data", "How Quantities Combine (Understanding Data)", 10

class Fr(Fraction_):
    """Fraction that prints as a terminating decimal when possible (for tidy working lines)."""
    def __str__(self):
        d = self.denominator
        while d % 2 == 0: d //= 2
        while d % 5 == 0: d //= 5
        if d == 1 and self.denominator != 1: return format(float(self), "g")
        return Fraction_.__str__(self)
    def __format__(self, spec): return str(self) if not spec else Fraction_.__format__(self, spec)

def I(x): return x.denominator == 1
def u(x): return s(x)

# ---------------- generators: each takes (rng, params) and returns an item or None ----------------
def comb_vals(r, nr, ar):
    n1, n2 = r.randint(*nr), r.randint(*nr); a1, a2 = r.randint(*ar), r.randint(*ar)
    if n1 == n2 or a1 == a2: return None
    t = Fr(n1 * a1 + n2 * a2, n1 + n2)
    return (n1, a1, n2, a2, t) if I(t) else None

def g_comb(nr, ar, ctx="students"):
    def f(r):
        v = comb_vals(r, nr, ar)
        if not v: return None
        n1, a1, n2, a2, t = v
        return nn(f"The average marks of {n1} {ctx} is ${a1}$ and of another {n2} {ctx} is ${a2}$. The average of all {n1+n2} {ctx} is:", t, f"$\\dfrac{{{n1}\\times{a1}+{n2}\\times{a2}}}{{{n1+n2}}}={t}$.", offs=(1, -1, 2, -2, 5, Fr(a1 + a2, 2) - t if Fr(a1 + a2, 2) != t else 3))
    return f

def q_comb(nr, ar, ctx="students"):
    def f(r):
        v = comb_vals(r, nr, ar)
        if not v: return None
        n1, a1, n2, a2, t = v
        return QQ(f"The average marks of {n1} {ctx} in a test is {a1} and that of {n2} {ctx} is {a2}. Find the average marks of all {n1+n2} {ctx} together.", f"Total of first group $={n1}\\times{a1}={n1*a1}$", f"Total of second group $={n2}\\times{a2}={n2*a2}$", f"Combined average $=\\dfrac{{{n1*a1+n2*a2}}}{{{n1+n2}}}={t}$")
    return f

def g_add(nr, ar, add=True):
    def f(r):
        n, a = r.randint(*nr), r.randint(*ar)
        if add:
            x = r.randint(*ar) + r.randint(-9, 25)
            t = Fr(n * a + x, n + 1)
            if not I(t) or x == a: return None
            return nn(f"The average of {n} numbers is ${a}$. When a number ${x}$ is included, the average of all {n+1} numbers becomes:", t, f"$\\dfrac{{{n}\\times{a}+{x}}}{{{n+1}}}={t}$.", offs=(1, -1, 2, -2, 5, a - t + 4))
        d = r.choice([-3, -2, -1, 1, 2, 3, 4]); x = a - (n - 1) * d; t = Fr(a + d)
        if x <= 0 or x == a: return None
        return nn(f"The average of {n} numbers is ${a}$. If the number ${x}$ is removed, the average of the remaining {n-1} numbers is:", t, f"$\\dfrac{{{n}\\times{a}-{x}}}{{{n-1}}}={t}$.", offs=(1, -1, 2, -2, 5, 4))
    return f

def q_add(nr, ar, add=True):
    def f(r):
        n, a = r.randint(*nr), r.randint(*ar)
        d = r.choice([-3, -2, -1, 1, 2, 3, 4])
        x = a + r.randint(5, 30) if add else a - (n - 1) * d
        t = Fr(n * a + x, n + 1) if add else Fr(a + d)
        if not I(t) or x == a or t <= 0 or x <= 0: return None
        if add:
            return QQ(f"The mean of {n} observations is {a}. A new observation {x} is added. Find the new mean.", f"Sum of {n} observations $={n}\\times{a}={n*a}$", f"New sum $={n*a}+{x}={n*a+x}$", f"New mean $=\\dfrac{{{n*a+x}}}{{{n+1}}}={t}$")
        return QQ(f"The mean of {n} observations is {a}. One observation {x} is removed. Find the mean of the remaining observations.", f"Sum $={n}\\times{a}={n*a}$", f"Remaining sum $={n*a}-{x}={n*a-x}$", f"New mean $=\\dfrac{{{n*a-x}}}{{{n-1}}}={t}$")
    return f

def g_wt(wr, sr):
    def f(r):
        w = [r.randint(*wr) for _ in range(3)]; sc = [r.randint(*sr) for _ in range(3)]
        t = Fr(sum(a * b for a, b in zip(w, sc)), sum(w))
        if not I(t) or len(set(sc)) < 3: return None
        return nn(f"Marks of ${sc[0]}$, ${sc[1]}$ and ${sc[2]}$ are given weights ${w[0]}$, ${w[1]}$ and ${w[2]}$ respectively. The weighted average is:", t, f"$\\dfrac{{{sc[0]}\\times{w[0]}+{sc[1]}\\times{w[1]}+{sc[2]}\\times{w[2]}}}{{{sum(w)}}}={t}$.", offs=(1, -1, 2, -2, 5, Fr(sum(sc), 3) - t + 3))
    return f

def q_wt(wr, sr, n=3):
    def f(r):
        w = [r.randint(*wr) for _ in range(n)]; sc = [r.randint(*sr) for _ in range(n)]
        t = Fr(sum(a * b for a, b in zip(w, sc)), sum(w))
        if not I(t) or len(set(sc)) < n: return None
        names = ["Maths", "Science", "English", "Hindi"][:n]
        return QQ("A final score combines " + ", ".join(f"{nm} (score {a}, weight {b})" for nm, a, b in zip(names, sc, w)) + ". Find the weighted average score.", "Weighted sum $=" + "+".join(f"{a}\\times{b}" for a, b in zip(sc, w)) + f"={sum(a*b for a,b in zip(w,sc))}$", f"Sum of weights $={sum(w)}$", f"Weighted average $={t}$")
    return f

def mix_vals(r, vr, cr):
    v1, v2 = r.randint(*vr) * 10, r.randint(*vr) * 10; c1, c2 = r.randint(*cr), r.randint(*cr)
    if v1 == v2 or c1 == c2: return None
    t = Fr(v1 * c1 + v2 * c2, v1 + v2)
    return (v1, c1, v2, c2, t) if I(t) else None

def g_mix(vr, cr, thing="sugar solution"):
    def f(r):
        z = mix_vals(r, vr, cr)
        if not z: return None
        v1, c1, v2, c2, t = z
        return nn(f"{v1} mL of a ${c1}\\%$ {thing} is mixed with {v2} mL of a ${c2}\\%$ {thing}. The concentration of the mixture is:", t, f"$\\dfrac{{{v1}\\times{c1}+{v2}\\times{c2}}}{{{v1+v2}}}={t}\\%$.", offs=(1, -1, 2, -2, 5, Fr(c1 + c2, 2) - t + 3), fmtf=lambda x: f"${s(x)}\\%$")
    return f

def q_mix(vr, cr, thing="sugar solution"):
    def f(r):
        z = mix_vals(r, vr, cr)
        if not z: return None
        v1, c1, v2, c2, t = z
        return QQ(f"{v1} mL of a {c1}% {thing} is mixed with {v2} mL of a {c2}% {thing}. Find the percentage concentration of the mixture.", f"Pure part in the first $={v1}\\times\\frac{{{c1}}}{{100}}={Fr(v1*c1,100)}$ mL", f"Pure part in the second $={Fr(v2*c2,100)}$ mL", f"Total $={Fr(v1*c1+v2*c2,100)}$ mL in ${v1+v2}$ mL", f"Concentration $={t}\\%$")
    return f

def g_pct(tr, pr, thing="electricity"):
    def f(r):
        T = r.randint(*tr) * 20; p = r.randint(*pr)
        x = Fr(T * p, 100)
        if not I(x): return None
        return nn(f"In a 100% stacked bar of a household's monthly {thing} use, appliances take ${p}\\%$ of ${T}$ units. The units used by the appliances are:", x, f"${p}\\%$ of ${T}=\\frac{{{p}}}{{100}}\\times{T}={x}$.", offs=(1, -1, 2, 10, -10, 20))
    return f

def g_stack(cr, nc=3):
    def f(r):
        c = [r.randint(*cr) for _ in range(nc)]
        names = ["rice", "wheat", "pulses", "oil"][:nc]
        return nn("A stacked bar for a family's monthly food use shows " + ", ".join(f"{n_} {k} kg" for n_, k in zip(names, c)) + ". The total length of the bar is (in kg):", sum(c), "Total length is the sum of the components.", offs=(1, -1, 2, 5, 10, -5))
    return f

def g_miss(nr, ar):
    def f(r):
        n1, n2 = r.randint(*nr), r.randint(*nr); a1, m = r.randint(*ar), r.randint(*ar)
        if n1 == n2 or a1 == m: return None
        a2 = Fr(m * (n1 + n2) - n1 * a1, n2)
        if not I(a2) or not 0 < a2 <= 150: return None
        return nn(f"The average of {n1} numbers is ${a1}$. The average of all {n1+n2} numbers (including {n2} more numbers) is ${m}$. The average of the {n2} additional numbers is:", a2, f"Sum of the extra numbers $={m}\\times{n1+n2}-{n1}\\times{a1}={m*(n1+n2)-n1*a1}$; divide by ${n2}$.", offs=(1, -1, 2, -2, 5, 10), pos=True)
    return f

def q_miss(nr, ar):
    def f(r):
        n1, n2 = r.randint(*nr), r.randint(*nr); a1, m = r.randint(*ar), r.randint(*ar)
        if n1 == n2 or a1 == m: return None
        a2 = Fr(m * (n1 + n2) - n1 * a1, n2)
        if not I(a2) or not 20 <= a2 <= 98 or max(a1, m) > 95: return None
        return QQ(f"The average score of {n1} students in a test is {a1}. When {n2} more students take the test, the average score of all {n1+n2} students becomes {m}. Find the average score of the {n2} additional students.", f"Total score of all $={m}\\times{n1+n2}={m*(n1+n2)}$", f"Total score of the first group $={n1}\\times{a1}={n1*a1}$", f"Total score of the additional group $={m*(n1+n2)-n1*a1}$", f"Average $=\\dfrac{{{m*(n1+n2)-n1*a1}}}{{{n2}}}={a2}$")
    return f

def g_findn(nr, ar):
    def f(r):
        n1 = r.randint(*nr); a1, a2 = r.randint(*ar), r.randint(*ar); m = r.randint(min(a1, a2) + 1, max(a1, a2) - 1) if abs(a1 - a2) > 2 else None
        if m is None or a1 == a2: return None
        n2 = Fr(n1 * (m - a1), a2 - m)
        if not I(n2) or n2 <= 0: return None
        return nn(f"A group of {n1} people has average weight ${a1}$ kg. Another group has average weight ${a2}$ kg. Together the average weight is ${m}$ kg. The number of people in the second group is:", n2, f"${n1}({m}-{a1})=n_2({a2}-{m})$.", offs=(1, -1, 2, -2, 5, n1), pos=True)
    return f

def q_findn(nr, ar):
    def f(r):
        n1 = r.randint(*nr); a1, a2 = r.randint(*ar), r.randint(*ar)
        if abs(a1 - a2) < 6 or max(a1, a2) > 98: return None
        m = r.randint(min(a1, a2) + 1, max(a1, a2) - 1)
        n2 = Fr(n1 * (m - a1), a2 - m)
        if not I(n2) or not 1 <= n2 <= 80: return None
        return QQ(f"In a class, {n1} students have an average of {a1} marks and the remaining students have an average of {a2} marks. The class average is {m}. Find the number of remaining students.", "Let the number of remaining students be $n$", f"${n1}\\times{a1}+{a2}n={m}({n1}+n)$", f"$n({a2}-{m})={n1}({m}-{a1})$", f"$n={n2}$")
    return f

def g_equal(wk):
    def f(r):
        k = r.randint(*wk); a = [r.randint(20, 60) for _ in range(k)]
        if Fr(sum(a), k).denominator != 1: return None
        return nn(f"Over {k} weeks of equal length a cyclist's weekly average distances were " + ", ".join(f"${x}$" for x in a) + " km per day. The average over the whole period (km per day) is:", Fr(sum(a), k), "Equal-sized groups: average of the averages.", offs=(1, -1, 2, -2, 5, 3))
    return f

def g_speed(sr):
    def f(r):
        a, b = r.randint(*sr), r.randint(*sr)
        if a >= b: return None
        t = Fr(2 * a * b, a + b)
        if not I(t): return None
        return nn(f"A bus goes from A to B at ${a}$ km/h and returns along the same road at ${b}$ km/h. The average speed for the whole journey (km/h) is:", t, f"$\\dfrac{{2\\times{a}\\times{b}}}{{{a}+{b}}}={t}$ (total distance / total time).", offs=(1, -1, 2, -2, Fr(a + b, 2) - t, 5))
    return f

def q_speed(sr):
    def f(r):
        a, b = r.randint(*sr), r.randint(*sr)
        if a >= b: return None
        t = Fr(2 * a * b, a + b)
        if not I(t): return None
        d = a * b // gcd(a, b)
        return QQ(f"A cyclist rides from home to a market at {a} km/h and returns by the same route at {b} km/h. Find the average speed for the whole trip.", f"Take distance each way $={d}$ km, so total distance $={2*d}$ km", f"Time $=\\frac{{{d}}}{{{a}}}+\\frac{{{d}}}{{{b}}}={Fr(d,a)+Fr(d,b)}$ h", f"Average speed $=\\dfrac{{{2*d}}}{{{Fr(d,a)+Fr(d,b)}}}={t}$ km/h (not the simple mean of ${a}$ and ${b}$)")
    return f

def g_allig(cr):
    def f(r):
        c1, c2 = r.randint(*cr), r.randint(*cr)
        if c1 >= c2 or c2 - c1 < 10: return None
        m = r.randint(c1 + 1, c2 - 1); p, q = m - c1, c2 - m
        if min(p, q) * 5 < c2 - c1: return None
        g = gcd(p, q)
        return M4(f"In what ratio must a ${c1}\\%$ solution and a ${c2}\\%$ solution be mixed to obtain a ${m}\\%$ solution?", f"${q//g}:{p//g}$", [f"${p//g}:{q//g}$", f"${(q//g)+1}:{p//g}$", f"${q//g}:{(p//g)+1}$"], f"Amounts are in the ratio $({c2}-{m}):({m}-{c1})={q}:{p}$.") if (q // g, p // g) != (p // g, q // g) else None
    return f

def q_allig(cr):
    def f(r):
        c1, c2 = r.randint(*cr), r.randint(*cr)
        if c1 >= c2 or c2 - c1 < 10: return None
        m = r.randint(c1 + 1, c2 - 1); p, q = m - c1, c2 - m; g = gcd(p, q)
        if p == q or min(p, q) * 5 < c2 - c1: return None
        return QQ(f"A chemist has a {c1}% acid solution and a {c2}% acid solution. In what ratio must they be mixed to get a {m}% solution?", "Let amounts be $x$ and $y$", f"${c1}x+{c2}y={m}(x+y)$", f"${m-c1}x={c2-m}y$", f"$x:y={q//g}:{p//g}$")
    return f

def g_replace(nr, ar):
    def f(r):
        n, a, d = r.randint(*nr), r.randint(*ar), r.randint(2, 5); x = r.randint(20, 40)
        return nn(f"The average monthly salary of {n} employees is ₹{a} thousand. An employee earning ₹{x} thousand leaves and a new employee joins, and the average rises by ₹{d} thousand. The new employee's salary (in ₹ thousand) is:", x + n * d, f"New salary is higher by $n\\times{d}={n*d}$ thousand.", offs=(d, -d, 5, 10, -5, n))
    return f

def q_replace(nr, ar):
    def f(r):
        n, a, d = r.randint(*nr), r.randint(*ar), r.randint(2, 5); x = r.randint(20, 40)
        return QQ(f"The average monthly salary of {n} employees is ₹{a} thousand. An employee earning ₹{x} thousand leaves and a new employee joins; the average rises by ₹{d} thousand. Find the new employee's monthly salary.", f"Rise in total $={n}\\times{d}={n*d}$ thousand", "New salary $=$ old salary $+$ rise in total", f"$={x}+{n*d}={x+n*d}$ thousand, i.e. ₹{(x+n*d)*1000}")
    return f

def g_profit(pr):
    def f(r):
        s1, s2 = r.randint(2, 9) * 1000, r.randint(2, 9) * 1000; p1, p2 = r.randint(*pr), r.randint(*pr)
        if s1 == s2 or p1 == p2: return None
        t = Fr(s1 * p1 + s2 * p2, s1 + s2)
        if not I(t): return None
        return nn(f"A shop earns a profit of ${p1}\\%$ on sales of ₹{s1} and ${p2}\\%$ on sales of ₹{s2}. The overall profit percentage on total sales is:", t, f"$\\dfrac{{{s1}\\times{p1}+{s2}\\times{p2}}}{{{s1+s2}}}={t}\\%$.", offs=(1, -1, 2, -2, 3, Fr(p1 + p2, 2) - t + 1), fmtf=lambda x: f"${s(x)}\\%$")
    return f

def g_mean(kr, vr):
    def f(r):
        k = r.randint(*kr); v = [r.randint(*vr) for _ in range(k)]
        if sum(v) % k: return None
        return nn("The mean of " + ", ".join(map(str, v)) + " is:", Fr(sum(v), k), f"Sum ${sum(v)}$ divided by ${k}$.", offs=(1, -1, 2, -2, 5, 3))
    return f

CONC = [tx("The concentration of juice in a drink is $12\\%$. The amount of juice in 250 mL of the drink is:", "30 mL", ["12 mL", "25 mL", "3 mL"], "$\\frac{12}{100}\\times250=30$."),
        tx("The concentration of salt in 400 mL of brine is $5\\%$. The salt present is:", "20 mL", ["5 mL", "40 mL", "2 mL"], "$\\frac5{100}\\times400=20$."),
        tx("A 600 mL mixture has $15\\%$ colour. The colour present is:", "90 mL", ["15 mL", "60 mL", "9 mL"], "$\\frac{15}{100}\\times600=90$."),
        tx("A 800 g mixture has $35\\%$ nuts. The nuts present are:", "280 g", ["35 g", "350 g", "28 g"], "$\\frac{35}{100}\\times800=280$.")]
CONCEPT = [tx(q, c, w, why) for q, c, w, why in [
    ("When two groups of different sizes are combined, the combined average is found by:", "total of all values divided by the total number of values", ["adding the two averages and halving", "multiplying the two averages", "subtracting the smaller average from the larger"], "Use totals, not the plain mean of the two averages."),
    ("The plain mean of two group averages is certain to equal the combined average when:", "the two groups have the same size", ["the first group is larger", "one average is zero", "the second group is larger"], "Equal weights."),
    ("In a stacked bar chart, the length of the whole bar shows:", "the total of all the components", ["only the largest component", "the average of the components", "the percentage of the first component"], "Whole bar = total."),
    ("In a 100% stacked bar chart, every bar has the same length because:", "each bar shows shares of its own total as percentages", ["every total is equal", "only one component is plotted", "the bars show averages"], "Bars show proportions."),
    ("The weighted average of values $x_1, x_2$ with weights $w_1, w_2$ is:", "$\\dfrac{w_1x_1+w_2x_2}{w_1+w_2}$", ["$\\dfrac{x_1+x_2}{w_1+w_2}$", "$\\dfrac{w_1+w_2}{x_1+x_2}$", "$w_1x_1+w_2x_2$"], "Formula."),
    ("Mixing two solutions of different concentrations gives a concentration that lies:", "between the two concentrations", ["above both", "below both", "equal to the larger one"], "It is a weighted average."),
    ("The average speed over a return trip on the same route at two different speeds is:", "total distance divided by total time", ["the mean of the two speeds", "the larger speed", "the difference of the speeds"], "Definition of average speed."),
    ("If a new value larger than the current mean is added to a data set, the mean:", "increases", ["decreases", "stays the same", "becomes zero"], "A bigger value pulls the mean up.")]]

# ---- extra Q-generators ----
def q_mean(kr, vr):
    def f(r):
        k = r.randint(*kr); v = [r.randint(*vr) for _ in range(k)]
        if sum(v) % k: return None
        return QQ(f"Find the mean of the numbers {', '.join(map(str, v))}.", f"Sum $={'+'.join(map(str, v))}={sum(v)}$", f"Mean $=\\dfrac{{{sum(v)}}}{{{k}}}={Fr(sum(v), k)}$")
    return f

def q_pct(tr, pr):
    def f(r):
        T = r.randint(*tr) * 20; p = r.randint(*pr); x = Fr(T * p, 100)
        if not I(x): return None
        return QQ(f"A 100% stacked bar shows that ${p}\\%$ of a family's monthly spending of ₹{T} is on food. Find the amount spent on food and on everything else.", f"Food $=\\frac{{{p}}}{{100}}\\times{T}={x}$", f"Remaining share $={100-p}\\%$", f"Everything else $={T}-{x}={T-x}$")
    return f

def q_conc(vr, cr):
    def f(r):
        v = r.randint(*vr) * 50; c = r.randint(*cr); x = Fr(v * c, 100)
        if not I(x): return None
        return QQ(f"A {v} mL bottle of a drink contains {c}% fruit pulp. Find the volume of pulp and of the remaining liquid.", f"Pulp $=\\frac{{{c}}}{{100}}\\times{v}={x}$ mL", f"Remaining $={v}-{x}={v-x}$ mL")
    return f

def q_equal(wk):
    def f(r):
        k = r.randint(*wk); a = [r.randint(20, 60) for _ in range(k)]
        if sum(a) % k: return None
        return QQ(f"A girl cycles for {k} weeks of equal length. Her weekly averages are " + ", ".join(f"{x} min" for x in a) + " per day. Find the average over all the weeks and say why the simple mean of the averages can be used.", f"Sum of weekly averages $={sum(a)}$", f"Average $=\\frac{{{sum(a)}}}{{{k}}}={Fr(sum(a), k)}$ min per day", "Every week has the same number of days, so each average has the same weight")
    return f

def q_stackpct(tr, pr):
    def f(r):
        T = r.randint(*tr) * 100; p = [r.randint(*pr) for _ in range(2)]
        if sum(p) >= 90 or p[0] == p[1]: return None
        rest = 100 - sum(p)
        return QQ(f"A 100% stacked bar of a school's ₹{T} budget shows ${p[0]}\\%$ on books and ${p[1]}\\%$ on sports. Find the amount on books, on sports and on the remaining items.", f"Books $={Fr(T*p[0],100)}$", f"Sports $={Fr(T*p[1],100)}$", f"Remaining share ${rest}\\%$, amount $={Fr(T*rest,100)}$")
    return f

def q_comb3(nr, ar):
    def f(r):
        n = [r.randint(*nr) for _ in range(3)]; a = [r.randint(*ar) for _ in range(3)]
        if len(set(a)) < 3: return None
        t = Fr(sum(x * y for x, y in zip(n, a)), sum(n))
        if not I(t): return None
        return QQ(f"Three sections have {n[0]}, {n[1]} and {n[2]} students with average marks {a[0]}, {a[1]} and {a[2]} respectively. Find the average marks of all the students.", f"Totals: ${n[0]*a[0]}$, ${n[1]*a[1]}$, ${n[2]*a[2]}$", f"Grand total $={sum(x*y for x,y in zip(n,a))}$ for ${sum(n)}$ students", f"Average $={t}$")
    return f

def q_dilute(vr, cr):
    def f(r):
        v = r.randint(*vr) * 10; c = r.randint(*cr); w = r.randint(1, 8) * 10
        t = Fr(v * c, v + w)
        if not I(t): return None
        return QQ(f"{v} mL of a {c}% acid solution is diluted by adding {w} mL of water. Find the new concentration.", f"Acid present $=\\frac{{{c}}}{{100}}\\times{v}={Fr(v*c,100)}$ mL (unchanged)", f"New volume $={v}+{w}={v+w}$ mL", f"New concentration $=\\dfrac{{{Fr(v*c,100)}}}{{{v+w}}}\\times100={t}\\%$")
    return f

def q_cost(cr):
    def f(r):
        c1, c2 = r.randint(*cr) * 5, r.randint(*cr) * 5; a, b = r.randint(1, 5), r.randint(1, 5); pr = r.choice([10, 20, 25])
        if c1 >= c2 or a == b: return None
        cost = Fr(a * c1 + b * c2, a + b)
        if not I(cost): return None
        sp = cost * (100 + pr) / 100
        if not I(sp): return None
        return QQ(f"A trader mixes rice costing ₹{c1} per kg and rice costing ₹{c2} per kg in the ratio {a}:{b}. Find the cost price per kg of the mixture and the selling price per kg to earn a profit of {pr}%.", f"Cost of the mixture $=\\dfrac{{{a}\\times{c1}+{b}\\times{c2}}}{{{a+b}}}$", f"$={cost}$ per kg", f"Profit factor $=\\frac{{{100+pr}}}{{100}}$", f"Selling price $={sp}$ per kg")
    return f

def q_stackcmp(tr, pr):
    def f(r):
        T1, T2 = r.randint(*tr) * 100, r.randint(*tr) * 100; p1, p2 = r.randint(*pr), r.randint(*pr)
        a, b = Fr(T1 * p1, 100), Fr(T2 * p2, 100)
        if T1 >= T2 or p1 <= p2 or not (I(a) and I(b)) or a == b: return None
        w = "more" if b > a else "less"
        return QQ(f"A family spent ₹{T1} in January and ₹{T2} in February. Food took {p1}% of the January total and {p2}% of the February total (100% stacked bars). In which month was more money spent on food, and by how much?", f"January food $={a}$", f"February food $={b}$", f"{'February' if b > a else 'January'} is higher by ${abs(b-a)}$", "The larger total outweighs the smaller share in February" if b > a else "The larger share outweighs the smaller total in January")
    return f

def q_addtwo(nr, ar):
    def f(r):
        n, a = r.randint(*nr), r.randint(*ar); x, y = a + r.randint(5, 25), a - r.randint(1, 4)
        t = Fr(n * a + x + y, n + 2)
        if not I(t): return None
        return QQ(f"The mean of {n} numbers is {a}. Two more numbers {x} and {y} are added. Find the new mean and say whether it rises or falls.", f"Original sum $={n*a}$", f"New sum $={n*a}+{x}+{y}={n*a+x+y}$", f"New mean $=\\dfrac{{{n*a+x+y}}}{{{n+2}}}={t}$", "Rises" if t > a else "Falls")
    return f

# =============================== EASY ===============================
EASY_A = [draw(100, 4, g_mean((4, 6), (10, 60))), draw(101, 4, g_equal((3, 5))), draw(102, 4, g_pct((5, 15), (10, 40))), draw(103, 4, g_stack((10, 40))), draw(104, 4, g_comb((10, 30), (40, 60))),
          CONC, CONCEPT[:4], draw(105, 4, g_wt((1, 3), (40, 90)))]
EASY_B = draw(110, 4, q_mean((4, 6), (10, 70))) + draw(111, 4, q_pct((5, 12), (10, 40))) + draw(112, 4, q_conc((2, 8), (10, 40)))
EASY_C = draw(113, 6, q_comb((10, 30), (30, 70))) + draw(114, 6, q_equal((3, 5))) + draw(115, 6, q_wt((1, 4), (40, 95), 2))
EASY_D = draw(116, 6, q_add((5, 12), (20, 50))) + draw(117, 6, q_mix((2, 6), (10, 40)))

# =============================== NCERT ===============================
NCERT_A = [draw(200, 4, g_comb((20, 60), (35, 80))), draw(201, 4, g_add((8, 25), (30, 60))), draw(202, 4, g_wt((2, 6), (45, 95))), draw(203, 4, g_mix((5, 30), (10, 40))),
           draw(204, 4, g_pct((20, 60), (12, 45), "water")), CONCEPT[4:], draw(205, 4, g_miss((8, 30), (30, 60))), draw(206, 4, g_add((8, 25), (30, 60), add=False))]
NCERT_B = draw(210, 4, q_comb((25, 60), (35, 80))) + draw(211, 4, q_wt((2, 6), (45, 95), 3)) + draw(212, 4, q_stackpct((5, 30), (10, 40)))
NCERT_C = draw(213, 6, q_mix((10, 50), (12, 45))) + draw(214, 3, q_add((10, 30), (25, 60))) + draw(215, 3, q_add((10, 30), (25, 60), add=False)) + draw(216, 6, q_miss((10, 40), (30, 70)))
NCERT_D = draw(217, 6, q_comb3((15, 45), (35, 80))) + draw(218, 6, q_stackcmp((20, 40), (20, 60)))

# =============================== MEDIUM ===============================
MED_A = [draw(300, 4, g_add((12, 40), (50, 90))), draw(301, 4, g_add((12, 40), (50, 90), add=False)), draw(302, 4, g_miss((15, 50), (40, 80))), draw(303, 4, g_findn((10, 40), (35, 90))),
         draw(304, 4, g_mix((30, 80), (5, 60))), draw(305, 4, g_wt((3, 9), (50, 99))), draw(306, 4, g_replace((8, 20), (40, 60))), draw(307, 4, g_profit((8, 40)))]
MED_B = draw(310, 4, q_add((15, 45), (40, 80), add=False)) + draw(311, 4, q_replace((10, 30), (40, 70))) + draw(312, 4, q_speed((20, 60)))
MED_C = draw(313, 6, q_findn((10, 40), (35, 90))) + draw(314, 6, q_miss((20, 60), (40, 90))) + draw(315, 6, q_dilute((5, 20), (10, 50)))
MED_D = draw(316, 6, q_comb3((20, 60), (40, 90))) + draw(317, 6, q_mix((30, 90), (5, 60)))

# =============================== HARD ===============================
HARD_A = [draw(400, 4, g_findn((15, 60), (40, 120))), draw(401, 4, g_allig((5, 90))), draw(402, 4, g_speed((20, 90))), draw(403, 4, g_replace((15, 40), (45, 80))),
          draw(404, 4, g_miss((25, 80), (45, 95))), draw(405, 4, g_profit((10, 45))), draw(406, 4, g_mix((60, 150), (4, 70))), draw(407, 4, g_comb((50, 150), (45, 95)))]
HARD_B = draw(410, 4, q_allig((5, 90))) + draw(411, 4, q_speed((30, 90))) + draw(412, 4, q_replace((20, 50), (45, 80)))
HARD_C = draw(413, 6, q_findn((20, 80), (40, 98))) + draw(414, 6, q_wt((2, 8), (45, 99), 4)) + draw(415, 6, q_addtwo((10, 40), (30, 70)))
HARD_D = draw(416, 6, q_cost((10, 40))) + draw(417, 6, q_stackcmp((30, 80), (15, 70)))

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))

from c8m_fix import tidy
tidy(TIERS)
