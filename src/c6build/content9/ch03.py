from fractions import Fraction as F
from math import gcd
from lib import mcq, Q, OR
from mk9 import M4, build
def fr(f):
    f = F(f)
    return f"{f.numerator}" if f.denominator == 1 else (f"-\\frac{{{-f.numerator}}}{{{f.denominator}}}" if f < 0 else f"\\frac{{{f.numerator}}}{{{f.denominator}}}")
def pdec(digits, nonrep=""):
    """LaTeX for 0.nonrep(overline digits)"""
    return f"0.{nonrep}\\overline{{{digits}}}"
def rep_frac(nonrep, rep):
    m, n = len(nonrep), len(rep)
    num = int(nonrep + rep) - (int(nonrep) if nonrep else 0)
    den = (10**n - 1) * 10**m
    return F(num, den)
def dec_type(q):
    q = F(q).denominator
    while q % 2 == 0: q //= 2
    while q % 5 == 0: q //= 5
    return q == 1
A = []; B = []; C = []; D = []
# A: terminating vs repeating (7)
for p, q in [(3, 8), (5, 6), (7, 20), (4, 15), (11, 40), (9, 14), (13, 25)]:
    t = dec_type(F(p, q)); f = F(p, q)
    ans = "terminating" if t else "non-terminating repeating"
    A.append(M4(f"The decimal expansion of $\\frac{{{f.numerator}}}{{{f.denominator}}}$ is:", ans, [o for o in ["non-terminating repeating", "terminating", "non-terminating non-repeating", "cannot be determined"] if o != ans],
                f"denominator ${f.denominator}$ " + ("is of the form $2^a5^b$" if t else "has a prime factor other than 2 and 5")))
# A: convert repeating decimals (6)
for rep, nonrep in [("6", ""), ("45", ""), ("3", ""), ("27", ""), ("6", "1"), ("7", "35")]:
    f = rep_frac(nonrep, rep)
    wrong = [F(f.numerator + 1, f.denominator), F(f.denominator, f.numerator), f + F(1, 10)]
    A.append(M4(f"The number ${pdec(rep, nonrep)}$ in the form $\\frac pq$ is:", f"${fr(f)}$", [f"${fr(w)}$" for w in wrong], f"standard method ⇒ ${fr(f)}$"))
# A: classify (7)
for lbl, ans, why in [(r"$\sqrt{81}$", "rational", "$=9$"), (r"$\sqrt{12}$", "irrational", "12 is not a perfect square"), (r"$0.333\ldots$", "rational", "repeating decimal $=\\frac13$"),
                      (r"$1.01001000100001\ldots$", "irrational", "non-terminating and non-repeating"), (r"$\pi$", "irrational", "not a ratio of integers"), (r"$\frac{22}7$", "rational", "ratio of integers"), (r"$3+\sqrt5$", "irrational", "rational + irrational")]:
    A.append(M4(f"The number {lbl} is:", ans, [o for o in ["rational", "irrational", "neither rational nor irrational", "not a real number"] if o != ans], why))
# A: decimal places (3)
for den, dp in [("2^3\\times5", 3), ("2\\times5^2", 2), ("2^2\\times5^4", 4)]:
    A.append(M4(f"A rational number in lowest terms has denominator ${den}$. Its decimal expansion terminates after how many places?", f"{dp}", [str(x) for x in (dp - 1, dp + 1, dp + 2)], "number of places $=\\max(a,b)$ in $2^a5^b$"))
# A: integers/Brahmagupta (4)
for e, v in [(r"$(-12)\times5$", -60), (r"$(-8)\times(-7)$", 56), (r"$0-(-14)$", 14), (r"$(-20)\div4$", -5)]:
    A.append(M4(f"The value of {e} is:", str(v), [str(-v), str(v + 2), str(abs(v) - 1 if v < 0 else v + 4)], "Brahmagupta's rules for signs"))
# A: hand (13)
A += [
 M4(r"The set of all rational numbers is denoted by:", r"$\mathbb Q$", [r"$\mathbb Z$", r"$\mathbb N$", r"$\mathbb R$"], "Q for quotient"),
 M4(r"Which number is both rational and an integer?", "−7", [r"$\frac37$", r"$\sqrt2$", r"$\pi$"], "−7 is an integer"),
 M4(r"The average of $\frac12$ and $\frac34$ is a rational number lying between them. It is:", r"$\frac58$", [r"$\frac45$", r"$\frac78$", r"$\frac14$"], "$\\frac12\\left(\\frac12+\\frac34\\right)=\\frac58$"),
 M4(r"Rational numbers are NOT closed under:", "division by zero (undefined)", ["addition", "subtraction", "multiplication"], "division by 0 is not defined"),
 M4(r"0.999… (0.$\overline9$) is equal to:", "1", ["0.9", "slightly less than 1", "0.99"], "$x=0.\\overline9,\\ 9x=9$"),
 M4(r"Who gave the first proof of the irrationality of $\sqrt2$ by contradiction (c. 400 BCE)?", "Hippasus", ["Brahmagupta", "Āryabhaṭa", "Lambert"], "as per the chapter"),
 M4(r"Brahmagupta defined zero as the result of:", r"subtracting a number from itself ($a-a=0$)", ["adding two equal numbers", "multiplying by 1", "dividing a number by itself"], "Brāhmasphuṭasiddhānta (628 CE)"),
 M4(r"The absolute value $|-\frac35|$ is:", r"$\frac35$", [r"$-\frac35$", "0", r"$\frac53$"], "distance from 0"),
 M4(r"The distance between $-4$ and $3$ on the number line is:", "7", ["1", "−7", "12"], "$|-4-3|=7$"),
 M4(r"A student claims: “$\sqrt2\times\sqrt2$ is irrational, as both numbers are irrational.” The correct response is:", r"False; $\sqrt2\times\sqrt2=2$ is rational", ["True", "True only for square roots", "Cannot be determined"], "product of irrationals can be rational"),
 M4(r"Between any two rational numbers there are:", "infinitely many rational numbers", ["no rational number", "exactly one rational number", "exactly two rational numbers"], "density of $\\mathbb Q$"),
 M4(r"Which of the following has a non-terminating repeating decimal expansion?", r"$\frac{1}{7}$", [r"$\frac{1}{8}$", r"$\frac{3}{20}$", r"$\frac{7}{25}$"], "7 is a prime other than 2, 5"),
 M4(r"The block 142857 repeats in the decimal of:", r"$\frac17$", [r"$\frac13$", r"$\frac19$", r"$\frac1{11}$"], "$\\frac17=0.\\overline{142857}$"),
]
assert len(A) == 7+6+7+3+4+13 == 40, len(A)

# B (16)
for rep, nonrep in [("6", ""), ("45", ""), ("3", "1"), ("18", "")]:
    f = rep_frac(nonrep, rep)
    if not nonrep:
        n = len(rep)
        sol = f"Let $x={pdec(rep)}$. Then ${10**n}x={rep}.\\overline{{{rep}}}$; subtracting, ${10**n-1}x={rep}\\Rightarrow x={fr(f)}$"
    else:
        sol = f"Let $x={pdec(rep, nonrep)}$. $10x={nonrep}.\\overline{{{rep}}}$ and $100x={nonrep}{rep}.\\overline{{{rep}}}$; subtracting, $90x={int(nonrep+rep)-int(nonrep)}\\Rightarrow x={fr(f)}$"
    B.append(Q(f"Express ${pdec(rep, nonrep)}$ in the form $\\frac pq$.", sol, "2"))
for p, q in [(3, 8), (7, 12), (11, 20), (5, 9)]:
    f = F(p, q); t = dec_type(f)
    ans = f"${f.denominator}$ " + ("has prime factors only 2 and/or 5 ($" + ("2^a5^b" ) + "$) ⇒ terminating" if t else "has a prime factor other than 2 and 5 ⇒ non-terminating repeating")
    B.append(Q(f"Without long division, state whether $\\frac{{{p}}}{{{q}}}$ has a terminating or a repeating decimal. Give a reason.", ans, "1+1"))
B += [
 Q(r"Find two rational numbers between $\frac12$ and $\frac34$.", r"Average $=\frac58$; average of $\frac12$ and $\frac58$ $=\frac9{16}$. So $\frac9{16}$ and $\frac58$ (any two valid).", "1+1"),
 Q(r"A spice trader has a loan of ₹850, makes a profit of ₹1,200 and then a loss of ₹450. Write the sum using integers and find his final standing.", r"$-850+1200-450=-100$: he is in debt of ₹100.", "1+1"),
 Q(r"The temperature in Ladakh is 4 °C at noon and drops by 15 °C by midnight. Find the midnight temperature.", r"$4-15=-11$ °C.", "1+1"),
 Q(r"Show that $\frac{4}{6}$ and $\frac{10}{15}$ are equal rational numbers.", r"$4\times15=60$ and $6\times10=60$, so $ad=bc$ ⇒ equal. (Both equal $\frac23$.)", "1+1"),
 Q(r"Locate $\frac34$ on the number line by describing the steps.", r"Divide the unit interval $[0,1]$ into 4 equal parts and move 3 parts to the right of 0.", "2"),
 Q(r"Show that $0.\overline9=1$ using algebra.", r"$x=0.\overline9$; $10x=9.\overline9$; $10x-x=9\Rightarrow x=1$.", "1+1"),
 Q(r"Find the distance between $-\frac12$ and $\frac52$ on the number line.", r"$\left|-\frac12-\frac52\right|=3$.", "1+1"),
 Q(r"A rational number in lowest form has denominator $2^3\times5$. How many decimal places does its expansion have? Why?", r"3 decimal places. Multiply numerator and denominator by $5^2$ to get denominator $10^3$.", "1+1"),
]
assert len(B) == 16, len(B)

# C (24)
C += [
 Q(r"Prove that $\sqrt2$ is irrational.", r"Assume $\sqrt2=\frac pq$ with $p,q$ co-prime, $q\ne0$ (1). $2q^2=p^2\Rightarrow p^2$ even $\Rightarrow p$ even; $p=2k$ (1). Then $q^2=2k^2\Rightarrow q$ even — so 2 divides both $p$ and $q$, contradicting co-primality. Hence $\sqrt2$ is irrational (1).", "1+1+1"),
 Q(r"Prove that $\sqrt3$ is irrational.", r"Assume $\sqrt3=\frac pq$ (co-prime). $3q^2=p^2\Rightarrow3\mid p$; $p=3k\Rightarrow q^2=3k^2\Rightarrow3\mid q$. Both divisible by 3 — contradiction. So $\sqrt3$ is irrational.", "1+1+1"),
 Q(r"Prove that $\sqrt5$ is an irrational number.", r"Assume $\sqrt5=\frac pq$ in lowest terms. $5q^2=p^2\Rightarrow5\mid p\Rightarrow p=5k\Rightarrow q^2=5k^2\Rightarrow5\mid q$. Contradiction ⇒ $\sqrt5$ is irrational.", "1+1+1"),
 Q(r"Show that $3+\sqrt2$ is irrational, given that $\sqrt2$ is irrational.", r"If $3+\sqrt2=r$ (rational), then $\sqrt2=r-3$ would be rational — contradiction. Hence $3+\sqrt2$ is irrational.", "1+1+1"),
 Q(r"Express $2.3\overline{57}$ in the form $\frac pq$.", r"Let $x=2.3\overline{57}$. $10x=23.\overline{57}$; $1000x=2357.\overline{57}$. Subtract: $990x=2334\Rightarrow x=\frac{2334}{990}=\frac{389}{165}$.", "1+1+1"),
 Q(r"Convert $0.1\overline6$ into the form $\frac pq$.", r"$x=0.1\overline6$; $10x=1.\overline6$; $100x=16.\overline6$. $90x=15\Rightarrow x=\frac16$.", "1+1+1"),
 Q(r"Express $2.45\overline{37}$ in the form $\frac pq$.", r"$x=2.45\overline{37}$. $100x=245.\overline{37}$; $10000x=24537.\overline{37}$. $9900x=24292\Rightarrow x=\frac{24292}{9900}=\frac{6073}{2475}$.", "1+1+1"),
 Q(r"Express $0.\overline{45}$ as a fraction in lowest terms and verify by dividing.", r"$100x=45.\overline{45}$, $99x=45\Rightarrow x=\frac{45}{99}=\frac5{11}$. Check: $5\div11=0.4545\ldots$ ✓", "2+1"),
 Q(r"Find three rational numbers between $\frac13$ and $\frac12$.", r"Common denominator 24: $\frac8{24}$ and $\frac{12}{24}$. Take $\frac9{24},\frac{10}{24},\frac{11}{24}$, i.e. $\frac38,\frac5{12},\frac{11}{24}$.", "1+1+1"),
 Q(r"Find five rational numbers between $3$ and $4$.", r"Write $3=\frac{18}6$ and $4=\frac{24}6$: $\frac{19}6,\frac{20}6,\frac{21}6,\frac{22}6,\frac{23}6$ (any five valid).", "1+1+1"),
 Q(r"Find three rational numbers between $3.1415$ and $3.1416$.", r"e.g. $3.14152$, $3.14155$, $3.14158$.", "1+1+1"),
 Q(r"Without long division state whether $\frac{77}{210}$ terminates. If it does, after how many places?", r"$\frac{77}{210}=\frac{11}{30}$; $30=2\times3\times5$ has factor 3 ⇒ non-terminating repeating.", "2+1"),
 Q(r"A rational number in its lowest form has denominator $2^3\times5$. How many decimal places will its expansion have? Explain.", r"Multiply numerator and denominator by $5^2$ to get $10^3$ in the denominator ⇒ exactly 3 decimal places (the last digit is non-zero).", "1+2"),
 Q(r"Explain, using a debt example, why $10-(-5)=15$.", r"Removing a debt of ₹5 from 10 rupees of wealth makes you ₹5 richer: $10-(-5)=10+5=15$. In Brahmagupta's language, taking away a debt is like adding a fortune.", "1+2"),
 Q(r"Verify the distributive law $\frac12\times\left(\frac14+\frac13\right)=\frac12\times\frac14+\frac12\times\frac13$.", r"LHS $=\frac12\times\frac7{12}=\frac7{24}$; RHS $=\frac18+\frac16=\frac3{24}+\frac4{24}=\frac7{24}$ ✓", "1+1+1"),
 Q(r"Find the rational number $x$ such that $\frac x3+\frac x2=\frac{16}3$.", r"$\frac x3+\frac x2=\frac{5x}6=\frac{16}3\Rightarrow x=\frac{32}5$.", "2+1"),
 Q(r"Show that $\sqrt2$ can be located on the number line and describe the construction.", r"Take $OA=1$; draw a perpendicular at $A$ and mark $AB=1$. By Baudhāyana–Pythagoras $OB=\sqrt2$. With centre $O$ and radius $OB$, draw an arc to cut the number line at $P$; $P$ represents $\sqrt2$.", "1+2"),
 Q(r"Classify as rational or irrational: (i) $\sqrt{81}$ (ii) $\sqrt{12}$ (iii) $0.\overline3$ (iv) $0.12345\,12345\ldots$ (repeating block). Give the fraction where rational.", r"(i) rational, $9$. (ii) irrational. (iii) rational, $\frac13$. (iv) rational (repeating block 12345): $\frac{12345}{99999}=\frac{4115}{33333}$. Marking: ½+½+1+1.", "½+½+1+1"),
 Q(r"A tailor has 15 m of silk and a kurta needs $2$ m. How many kurtas can be made and how much silk is left? Express the number of kurtas as a rational number.", r"$15\div2=\frac{15}2=7\frac12$: 7 kurtas, with 1 m left over.", "1+1+1"),
 Q(r"Prove that $5-\sqrt3$ is irrational, given that $\sqrt3$ is irrational.", r"If $5-\sqrt3=r$ (rational) then $\sqrt3=5-r$ is rational — contradiction. Hence irrational.", "1+1+1"),
 Q(r"Show that $\frac{2}{\sqrt3}$ is irrational given that $\sqrt3$ is irrational.", r"If $\frac2{\sqrt3}=r$ (rational, $r\ne0$) then $\sqrt3=\frac2r$ is rational — contradiction.", "1+1+1"),
 Q(r"Find the lengths of the first three hypotenuses in the square-root spiral starting with a right triangle of legs 1, 1.", r"$\sqrt{1^2+1^2}=\sqrt2$; then legs $\sqrt2,1\Rightarrow\sqrt3$; then legs $\sqrt3,1\Rightarrow\sqrt4=2$.", "1+1+1"),
 Q(r"Find the decimal expansion of $\frac17$ and identify its repeating block. What is special about it?", r"$\frac17=0.\overline{142857}$. The block 142857 is a cyclic number: multiplying by 2, 3, … 6 permutes the same digits cyclically.", "1+1+1"),
 Q(r"Show that the average $\frac{a+b}2$ of two rational numbers $a<b$ lies between them.", r"$\frac{a+b}2-a=\frac{b-a}2>0$ and $b-\frac{a+b}2=\frac{b-a}2>0$. So $a<\frac{a+b}2<b$; it is rational as sums and quotients of rationals are rational.", "1+1+1"),
]
assert len(C) == 24, len(C)

# D (16)
D += [
 Q(r"(i) Prove that $\sqrt2$ is irrational. (ii) Hence show that $3\sqrt2-5$ is irrational.", r"(i) Contradiction proof: $\sqrt2=\frac pq$, $2q^2=p^2$, $p$ and $q$ both even — contradiction (3). (ii) If $3\sqrt2-5=r$ (rational) then $\sqrt2=\frac{r+5}3$ rational — contradiction (2).", "3+2"),
 Q(r"(i) Express $0.\overline{27}$ and $1.2\overline5$ in the form $\frac pq$. (ii) Write $0.\overline9$ as a fraction and comment.", r"(i) $0.\overline{27}=\frac{27}{99}=\frac3{11}$. $x=1.2\overline5$: $10x=12.\overline5$, $100x=125.\overline5$; $90x=113\Rightarrow x=\frac{113}{90}$. (ii) $9x=9\Rightarrow x=1$: so $0.\overline9=1$ exactly; decimal forms are not unique.", "2+2+1"),
 Q(r"<b>Case study:</b> The Ishango bone has a column of notches grouped as 11, 13, 17, 19. A merchant of Lothal gets 15 copper ingots for every 2 bags of spices. (i) What do 11, 13, 17, 19 have in common? Name the next three numbers of this kind. (ii) How many ingots will he get for 12 bags? (iii) Are natural numbers closed under subtraction? Give an example.", r"(i) All are primes between 10 and 20; next primes 23, 29, 31. (ii) $\frac{15}2\times12=90$ ingots. (iii) No: $3-5=-2$ is not a natural number.", "2+2+1"),
 Q(r"(i) Without long division, state which of $\frac{13}{80},\ \frac{5}{12},\ \frac{29}{343}$ have terminating decimals. (ii) For the terminating one, find the decimal expansion. (iii) Find the decimal of $\frac{5}{12}$ up to 5 places and state the repeating digit.", r"(i) $80=2^4\times5$ ⇒ $\frac{13}{80}$ terminates; $12=2^2\times3$ and $343=7^3$ ⇒ repeating. (ii) $\frac{13}{80}=\frac{13\times125}{10^4}=0.1625$. (iii) $\frac5{12}=0.41666\ldots=0.41\overline6$; repeating digit 6.", "2+1+2"),
 Q(r"<b>Case study:</b> A tailor has a roll of 15 m of silk; each kurta needs 2 m. Another roll has $12\frac12$ m. (i) How many kurtas from the 15 m roll and how much silk is left? (ii) How many from the second roll? (iii) Express the silk left in each case as a rational number and find the total silk left.", r"(i) 7 kurtas; left 1 m. (ii) $12.5\div2=6.25$: 6 kurtas; left 0.5 m $=\frac12$ m. (iii) Left: $1$ m and $\frac12$ m; total $\frac32$ m.", "2+2+1"),
 Q(r"(i) Prove that $\sqrt3$ is irrational. (ii) Hence prove that $2-\sqrt3$ is irrational.", r"(i) $\sqrt3=\frac pq$; $3q^2=p^2$ ⇒ $3\mid p$, $p=3k$ ⇒ $3\mid q$; contradiction (3). (ii) If $2-\sqrt3=r$, $\sqrt3=2-r$ rational — contradiction (2).", "3+2"),
 Q(r"Find 5 rational numbers between $\frac35$ and $\frac45$ by writing them with a common denominator large enough. Explain why the common denominator must be at least 6 times the difference of the numerators.", r"$\frac35=\frac{18}{30}$, $\frac45=\frac{24}{30}$ ⇒ $\frac{19}{30},\frac{20}{30},\frac{21}{30},\frac{22}{30},\frac{23}{30}$ (3). To fit 5 integers strictly between $k_1$ and $k_2$ we need $k_2-k_1>6$ — i.e. $\ge7$ (2). (With denominator 30 the difference is 6; the five values lie strictly between.)", "3+2"),
 Q(r"<b>Case study:</b> A square has side 1 unit. (i) Find the length of its diagonal. (ii) Show how to represent it on the number line. (iii) Why can this number not be written as $\frac pq$? (iv) Write its decimal expansion to 4 places and say what kind of decimal it is.", r"(i) $\sqrt2$. (ii) Draw $OA=1$, perpendicular $AB=1$, then arc of radius $OB$ meets the line at $P=\sqrt2$. (iii) Proof by contradiction shows $\sqrt2$ is irrational. (iv) $1.4142\ldots$ non-terminating, non-repeating.", "1+2+1+1"),
 Q(r"(i) Simplify $\left(\frac14-\frac5{12}\right)\div\frac{2}{3}$. (ii) Find the sum and the product of $\frac35$ and $\frac7{10}$.", r"(i) $\frac14-\frac5{12}=\frac{3-5}{12}=-\frac16$; $-\frac16\div\frac23=-\frac16\times\frac32=-\frac14$. (ii) Sum $=\frac6{10}+\frac7{10}=\frac{13}{10}$; product $=\frac{21}{50}$.", "3+2"),
 Q(r"<b>Case study:</b> Mādhava's series gives $\pi=4\left(1-\frac13+\frac15-\frac17+\cdots\right)$ and Āryabhaṭa gave $\pi\approx3.1416$. (i) Is $\pi$ rational? (ii) Compute $4\left(1-\frac13+\frac15-\frac17\right)$ and compare with 3.1416. (iii) Name the mathematician who proved π irrational and the year.", r"(i) No, π is irrational. (ii) $1-\frac13+\frac15-\frac17=\frac{105-35+21-15}{105}=\frac{76}{105}$; times 4 $=\frac{304}{105}\approx2.895$ — a rough value, improving with more terms. (iii) Lambert, 1761.", "1+2+2"),
 Q(r"Convert into $\frac pq$: (i) $12.6$ (ii) $0.0120$ (terminating) (iii) $3.052$ (terminating) (iv) $0.\overline{23}$ (v) $2.0\overline5$.", r"(i) $\frac{126}{10}=\frac{63}5$. (ii) $\frac{120}{10000}=\frac3{250}$. (iii) $\frac{3052}{1000}=\frac{763}{250}$. (iv) $\frac{23}{99}$. (v) $x=2.0\overline5$: $10x=20.\overline5$, $100x=205.\overline5$, $90x=185\Rightarrow x=\frac{37}{18}$.", "1+1+1+1+1"),
 Q(r"(i) Show that between any two rational numbers there is another rational number. (ii) Find the rational number midway between $-\frac14$ and $\frac5{12}$ and place it on the number line (describe).", r"(i) For $a<b$ the average $\frac{a+b}2$ is rational and lies between them (3). (ii) $\frac12\left(-\frac3{12}+\frac5{12}\right)=\frac1{12}$; it lies to the right of 0, one-twelfth of a unit from the origin (2).", "3+2"),
 Q(r"<b>Case study:</b> Brahmagupta's rules: fortune + fortune = fortune; debt + debt = debt; debt × fortune = debt; debt × debt = fortune. Using these, (i) compute $(-3)\times4$ and $(-3)\times(-4)$; (ii) a spice trader borrows ₹850, earns ₹1,200 and loses ₹450 — find his final standing; (iii) explain $(-3)\times(-4)=12$ in terms of debt.", r"(i) $-12$ and $12$. (ii) $-850+1200-450=-100$ ⇒ debt of ₹100. (iii) Removing 4 debts of ₹3 each makes one ₹12 richer.", "2+2+1"),
 Q(r"(i) Find the rational number $x$ such that $x\left(\frac13+\frac16\right)=\frac92$. (ii) Verify $\frac12\left(\frac34+\frac13\right)=\frac12\times\frac34+\frac12\times\frac13$.", r"(i) $\frac x2=\frac92\Rightarrow x=9$. (ii) LHS $=\frac12\times\frac{13}{12}=\frac{13}{24}$; RHS $=\frac38+\frac16=\frac9{24}+\frac4{24}=\frac{13}{24}$ ✓", "2+3"),
 Q(r"Show that $0.\overline{142857}=\frac17$ and verify the cyclic property by computing $2\times142857$ and $3\times142857$.", r"$x=0.\overline{142857}$, $10^6x=142857.\overline{142857}$, $999999x=142857\Rightarrow x=\frac{142857}{999999}=\frac17$ (3). $2\times142857=285714$, $3\times142857=428571$ — same digits cycled (2).", "3+2"),
 Q(r"(i) Find the distance between $-4$ and $3$, and between $-\frac52$ and $\frac72$, on the number line. (ii) Write $\left|-\frac79\right|$, $|0|$ and $\left|\frac53\right|$. (iii) Between which two consecutive integers does $\frac{13}4$ lie?", r"(i) $|-4-3|=7$; $\left|-\frac52-\frac72\right|=6$. (ii) $\frac79$, $0$, $\frac53$. (iii) $\frac{13}4=3.25$ lies between 3 and 4.", "2+1+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
