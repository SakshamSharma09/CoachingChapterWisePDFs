import random
from lib import mcq, Q, OR
from mk9 import M4, build
R = random.Random(909)

def nf(n): return sum(1 for d in range(1, n + 1) if n % d == 0)
def isp(n): return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
def issq(n): return int(round(n ** .5)) ** 2 == n

A = []; B = []; C = []; D = []

# ---- A1: forming converses (6)
for p, cv, wr in [
    ("If a number is divisible by 10, then it is divisible by 5.", "If a number is divisible by 5, then it is divisible by 10.", ["If a number is not divisible by 10, then it is not divisible by 5.", "If a number is not divisible by 5, then it is not divisible by 10.", "A number is divisible by 10 only if it is divisible by 5."]),
    ("If two angles are vertically opposite, then they are equal.", "If two angles are equal, then they are vertically opposite.", ["If two angles are not vertically opposite, then they are not equal.", "If two angles are not equal, then they are not vertically opposite.", "Vertically opposite angles are equal."]),
    ("If a quadrilateral is a rhombus, then its diagonals bisect each other.", "If the diagonals of a quadrilateral bisect each other, then it is a rhombus.", ["If a quadrilateral is not a rhombus, then its diagonals do not bisect each other.", "If the diagonals of a quadrilateral do not bisect each other, then it is not a rhombus.", "A rhombus has diagonals that bisect each other."]),
    ("If it is Sunday, then the school is closed.", "If the school is closed, then it is Sunday.", ["If it is not Sunday, then the school is not closed.", "If the school is not closed, then it is not Sunday.", "The school is closed on Sunday."]),
    ("If a number is a perfect square, then it is non-negative.", "If a number is non-negative, then it is a perfect square.", ["If a number is not a perfect square, then it is negative.", "If a number is negative, then it is not a perfect square.", "Every non-negative number is a perfect square and vice versa."]),
    ("If $x=3$, then $x^2=9$.", "If $x^2=9$, then $x=3$.", ["If $x\\ne3$, then $x^2\\ne9$.", "If $x^2\\ne9$, then $x\\ne3$.", "If $x=-3$, then $x^2=9$."]),
]:
    A.append(M4(f"The converse of the proposition “{p}” is:", cv, wr, "swap the ‘if’ part and the ‘then’ part"))

# ---- A2: counterexamples to false propositions (4)
for stm, ce, wr in [
    ("If a number is odd, then it is prime.", "9", ["7", "5", "11"]),
    ("If a number is divisible by 3, then it is divisible by 9.", "12", ["27", "45", "9"]),
    ("If $n$ is a prime number, then $n+2$ is also a prime number.", "7", ["3", "5", "11"]),
    ("If a number is a multiple of 4, then it is a multiple of 8.", "20", ["16", "24", "8"]),
]:
    A.append(M4(f"Which of the following is a counterexample to the proposition “{stm}”?", ce, wr, "it satisfies the ‘if’ part but not the ‘then’ part"))
assert not isp(9) and 12 % 3 == 0 and 12 % 9 and isp(7) and not isp(9) and 20 % 4 == 0 and 20 % 8

# ---- A3: truth of converse for number facts (4)
A += [
    M4("The proposition “If a number is a multiple of 12, then it is a multiple of 4” is true. Its converse is:", "false; 8 is a multiple of 4 but not of 12", ["true; every multiple of 4 is a multiple of 12", "false; 12 is not a multiple of 4", "true; 12 is a multiple of 4"], "8 = 4×2 is a counterexample"),
    M4("“If a number is divisible by both 3 and 5, then it is divisible by 15.” Its converse “If a number is divisible by 15, then it is divisible by both 3 and 5” is:", "true", ["false, since 15 is odd", "false, since 30 is divisible by 15", "neither true nor false"], "15 = 3 × 5 with 3 and 5 having no common factor"),
    M4("The converse of “If $n$ is even, then $n^2$ is even” is “If $n^2$ is even, then $n$ is even”. Which statement is correct?", "both the proposition and its converse are true", ["only the proposition is true", "only the converse is true", "both are false"], "the square of an odd number is odd"),
    M4("Proposition: “If $x>5$, then $x>2$.” Its converse is false because:", "$x=3$ satisfies $x>2$ but not $x>5$", ["no number is greater than 2", "$x=10$ is greater than 5", "$x=6$ satisfies both"], "a counterexample for the converse"),
]
assert 8 % 4 == 0 and 8 % 12

# ---- A4: Pythagoras converse (4)
for (a, b, c) in [(7, 24, 25), (6, 8, 11), (20, 21, 29), (9, 12, 16)]:
    right = a * a + b * b == c * c
    ans = "right-angled, since $a^2+b^2=c^2$" if right else "not right-angled, since $a^2+b^2\\ne c^2$"
    wr = ["right-angled, since $a+b>c$", "right-angled, since all sides are different", "not right-angled, since the sides are not equal"] if right else ["right-angled, since $a+b>c$", "right-angled, since $a^2+b^2=c^2$", "right-angled, since the sides are in increasing order"]
    A.append(M4(f"A triangle has sides {a} cm, {b} cm and {c} cm. By the converse of the Baudhāyana–Pythagoras theorem it is:", ans, wr, f"${a*a}+{b*b}={a*a+b*b}$ and ${c}^2={c*c}$"))

# ---- A5: factor counts and squares (4)
for n in [36, 48, 49, 100]:
    f = nf(n)
    ans = f"{f} factors; it is a perfect square" if issq(n) else f"{f} factors; it is not a perfect square"
    wr = [f"{f+1} factors; it is {'not ' if issq(n) else ''}a perfect square", f"{f-1} factors; it is a perfect square" if not issq(n) else f"{f+2} factors; it is a perfect square", f"{f+2} factors; it is not a perfect square"]
    A.append(M4(f"The number {n} has:", ans, wr, "count the factor pairs; an odd count signals a repeated pair"))

# ---- A6: primes and factors (4)
for stm, ans, wr, why in [
    ("A number that is the square of a prime has exactly:", "3 factors", ["2 factors", "4 factors", "an even number of factors"], "$p^2$ has $1, p, p^2$"),
    ("A number that is the product of two different primes has exactly:", "4 factors", ["2 factors", "3 factors", "6 factors"], "$pq$ has $1,p,q,pq$"),
    ("The number of factors of 121 is:", "3", ["2", "4", "11"], "$121=11^2$"),
    ("The number of factors of 35 is:", "4", ["2", "3", "5"], "$35=5\\times7$"),
]:
    A.append(M4(stm, ans, wr, why))
assert nf(121) == 3 and nf(35) == 4

# ---- A7: concept items (8)
A += [
    M4("A proposition is a statement that is:", "either true or false", ["always true", "always false", "a question"], "definition"),
    M4("A counterexample to a proposition is an instance that:", "satisfies the ‘if’ part but fails the ‘then’ part", ["satisfies both parts", "satisfies neither part", "proves the proposition"], "it shows the proposition is false"),
    M4("The statements “If X then Y” and “X implies Y” have:", "the same meaning", ["opposite meanings", "unrelated meanings", "the meaning of the converse"], "interchangeable forms"),
    M4("The sentence “$Y$ when $X$” conveys the same meaning as:", "If $X$ then $Y$", ["If $Y$ then $X$", "If not $X$ then not $Y$", "$X$ and $Y$ are false"], "another way to write the proposition"),
    M4("If a proposition is true, its converse:", "may be true or false", ["is always true", "is always false", "is never a proposition"], "e.g. “if it rains, the road is wet”"),
    M4("Fermat claimed that every number of the form $2^{2^n}+1$ is prime. Euler disproved this by showing that for $n=5$ the number is:", "composite", ["prime", "negative", "a perfect square"], "$2^{32}+1=641\\times6700417$"),
    M4("It is possible that a proposition and its converse are:", "both true, or both false, or one true and one false", ["only both true", "only one true", "never both false"], "all four combinations can occur in general"),
]
assert 2 ** 32 + 1 == 641 * 6700417

# ---- A8: iff / both true (4)
A += [
    M4("Which pair of statements are converses of each other and both true?", "“If a triangle is equilateral, then all its angles are equal” and “If all angles of a triangle are equal, then it is equilateral”", ["“If $x=2$, then $x^2=4$” and “If $x^2=4$, then $x=2$”", "“If a number ends in 0, then it is even” and “If a number is even, then it ends in 0”", "“If it rains, the road is wet” and “If the road is wet, it has rained”"], "both directions hold"),
    M4("‘$n$ is a perfect square’ and ‘$n$ has an odd number of factors’ are related as:", "each implies the other", ["only the first implies the second", "only the second implies the first", "neither implies the other"], "both the proposition and its converse are true"),
    M4("“If $a=b$, then $a+5=b+5$.” This proposition and its converse are:", "both true", ["both false", "only the proposition is true", "only the converse is true"], "adding 5 can be undone by subtracting 5"),
    M4("Which of the following converses is true?", "If the angles opposite two sides of a triangle are equal, the two sides are equal.", ["If two triangles have equal areas, they are congruent.", "If a number is divisible by 3, it is divisible by 6.", "If a number is prime, it is odd."], "the base-angle theorem and its converse"),
]

# ---- A9: assertion–reason (3)
AR_OPTS = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"]
def AR(a, r, ans, why): return mcq(f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}", list(AR_OPTS), ans, why)
A += [
    AR("The converse of the Baudhāyana–Pythagoras theorem is true.", "If $a^2+b^2=c^2$, a right triangle with legs $a,b$ has hypotenuse $c$, so the given triangle is congruent to it by SSS.", "a", "SSS congruence proves the converse"),
    AR("If a proposition is true, its converse must also be true.", "The proposition “If a number is a multiple of 6, then it is a multiple of 3” is true, but 9 is a multiple of 3 and not of 6.", "d", "A is false; R is a true fact that in fact contradicts A"),
    AR("The number 12 is a counterexample to “If a number is a multiple of 3, then it is a multiple of 9”.", "12 is a multiple of 3 but not a multiple of 9.", "a", "satisfies ‘if’, fails ‘then’"),
]
assert len(A) == 40, len(A)

# ---- B (16): 2 marks
B += [
    Q("Write the converse of “If two lines are parallel, then the alternate interior angles formed by a transversal are equal.” Is the converse true?", "Converse: If the alternate interior angles formed by a transversal are equal, then the two lines are parallel (1). It is true (1).", "1+1"),
    Q("State the converse of “If a number is divisible by 18, then it is divisible by 9.” Is it true? Justify.", "Converse: If a number is divisible by 9, then it is divisible by 18 (1). False: 27 is divisible by 9 but not by 18 (1).", "1+1"),
    Q("Write the converse of “If $x=y$, then $x^2=y^2$” and give a counterexample for it.", "Converse: If $x^2=y^2$, then $x=y$ (1). Counterexample: $x=3,\\ y=-3$ gives $x^2=y^2$ but $x\\ne y$ (1).", "1+1"),
    Q("Give a counterexample to show that “All numbers of the form $n^2+n+11$ are prime” is false.", "For $n=11$: $121+11+11=143=11\\times13$, which is composite (2).", "1+1"),
    Q("Give a counterexample to “If $n$ is prime, then $2^n-1$ is prime.”", "For $n=11$: $2^{11}-1=2047=23\\times89$ is composite although 11 is prime (2).", "1+1"),
    Q("Show that the number 9 is a counterexample to the proposition “If a number is odd, then it is prime”.", "9 is odd, so the ‘if’ part holds (1). $9=3\\times3$ is not prime, so the ‘then’ part fails (1).", "1+1"),
    Q("Write the converse of “If a triangle is right-angled with sides $a,b,c$ (hypotenuse $c$), then $a^2+b^2=c^2$.” Is it true?", "Converse: If $a^2+b^2=c^2$ in a triangle with sides $a,b,c$, then it is right-angled (1). It is true, by SSS congruence with a right triangle of legs $a$ and $b$ (1).", "1+1"),
    Q("Is the proposition “If a quadrilateral is a rectangle, then its diagonals are equal” true? Write its converse and give a counterexample for it.", "True (½). Converse: If the diagonals of a quadrilateral are equal, then it is a rectangle (½). Counterexample: an isosceles trapezium has equal diagonals but is not a rectangle (1).", "½+½+1"),
    Q("Write the proposition “A number has an odd number of factors when it is a perfect square” in ‘If … then …’ form.", "If a number is a perfect square, then it has an odd number of factors (2).", "2"),
    Q("How many factors does 64 have? Is the number of factors odd or even? What does this say about 64?", "$64=2^6$ has factors $1,2,4,8,16,32,64$: 7 factors (1). Odd number of factors, and 64 is a perfect square ($8\\times8$) (1).", "1+1"),
    Q("Write the converse of “If $n$ is the square of a prime, then $n$ has exactly 3 factors.” Give a counterexample if it is false.", "Converse: If $n$ has exactly 3 factors, then $n$ is the square of a prime (1). It is true: three factors means $1,p,p^2$ for a prime $p$ (1). (No counterexample exists.)", "1+1"),
    Q("A student says “If a number is divisible by 6, then it is divisible by 2 and 3.” Write the converse and state whether both are true.", "Converse: If a number is divisible by both 2 and 3, then it is divisible by 6 (1). Both are true because 2 and 3 have no common factor (1).", "1+1"),
    Q("Give a real-life example of a proposition that is true but whose converse is false.", "Proposition: If a person lives in Jaipur, then the person lives in Rajasthan (1). Converse: If a person lives in Rajasthan, then the person lives in Jaipur — false (a person in Jodhpur) (1).", "1+1"),
    Q("Test using the converse of the Baudhāyana–Pythagoras theorem whether a triangle with sides 9 cm, 40 cm, 41 cm is right-angled.", "$9^2+40^2=81+1600=1681=41^2$ (1). So the triangle is right-angled, with the right angle opposite the 41 cm side (1).", "1+1"),
    Q("Find a counterexample to “If $n$ is an even number, then $2^n+1$ is a prime number”.", "For $n=4$: $2^4+1=17$ is prime, but for $n=6$: $2^6+1=65=5\\times13$ is composite (2).", "1+1"),
    Q("Explain with an example why finding one counterexample is enough to disprove a proposition.", "A proposition claims truth for all cases (1). One case where the ‘if’ part holds but the ‘then’ part fails contradicts the claim, e.g. 9 for “every odd number is prime” (1).", "1+1"),
]
assert 11 * 11 + 11 + 11 == 143 and 2 ** 11 - 1 == 2047 == 23 * 89 and 9 * 9 + 40 * 40 == 41 * 41 and 2 ** 6 + 1 == 65 and nf(64) == 7 and isp(17)
assert len(B) == 16, len(B)

# ---- C (24): 3 marks
C += [
    Q("Write the converse of “If a number is divisible by 15, then it is divisible by 5.” Decide whether each is true and give a counterexample if one is false.", "Proposition: true, since $15=5\\times3$ (1). Converse: If a number is divisible by 5, then it is divisible by 15 (1). False: 10 is divisible by 5 but not by 15 (1).", "1+1+1"),
    Q("Write the converse of “If two triangles are congruent, then their corresponding angles are equal.” Is the converse true? Give a counterexample if false.", "Converse: If the corresponding angles of two triangles are equal, then the triangles are congruent (1). False (1). Counterexample: two equilateral triangles with sides 3 cm and 5 cm have equal angles but are not congruent (1).", "1+1+1"),
    Q("Show that the number 143 gives a counterexample to the claim “$n^2+n+11$ is prime for every natural number $n$”. State the value of $n$ used.", "For $n=11$: $n^2+n+11=121+11+11=143$ (1). $143=11\\times13$ (1), so it is composite and the claim is false (1).", "1+1+1"),
    Q("Test whether the triangle with sides 12 cm, 35 cm, 37 cm is right-angled. Name the theorem you use.", "Largest side 37: $12^2+35^2=144+1225=1369$ (1). $37^2=1369$ (1). By the converse of the Baudhāyana–Pythagoras theorem the triangle is right-angled (1).", "1+1+1"),
    Q("Write the converse of “If a number is a multiple of 6, then it is a multiple of 3”. Justify the proposition and give a counterexample for the converse.", "Justification: $6=3\\times2$, so every multiple of 6 is a multiple of 3 (1). Converse: If a number is a multiple of 3, then it is a multiple of 6 (1). Counterexample: 9 (1).", "1+1+1"),
    Q("List the factors of 36 as factor–partner pairs. Which pair repeats a number? What does this tell you about the number of factors?", "Pairs: (1,36), (2,18), (3,12), (4,9), (6,6) (1½). The pair (6,6) repeats (½). The count is $2\\times4+1=9$, odd, because 36 is a perfect square (1).", "1½+½+1"),
    Q("Explain why a number that has exactly one repeated factor pair must have an odd number of factors.", "All other factors form pairs of two different numbers, giving an even count (1). The repeated pair $(f,f)$ contributes just one factor $f$ (1). Even + 1 = odd (1).", "1+1+1"),
    Q("Write the converse of “If $a$ and $b$ are perfect squares, then $ab$ is a perfect square”. Is the proposition true? Is the converse true? Justify.", "Proposition: true, $a=m^2,\\ b=n^2\\Rightarrow ab=(mn)^2$ (1). Converse: If $ab$ is a perfect square, then $a$ and $b$ are perfect squares (1). False: $a=2,\\ b=8$ gives $ab=16$ but 2 is not a perfect square (1).", "1+1+1"),
    Q("Find a counterexample to each: (i) If $n$ is prime, then $n+4$ is prime. (ii) If $n$ is a multiple of 5, then $n$ ends in 5.", "(i) $n=5$ is prime but $n+4=9=3\\times3$ is not prime, so $n=5$ is a counterexample (1½). (ii) $n=10$ is a multiple of 5 but does not end in 5 (1½).", "1½+1½"),
    Q("State the converse of “If $n$ is divisible by 60, then it is divisible by both 5 and 12”. Is the converse true? Justify.", "Converse: If $n$ is divisible by both 5 and 12, then it is divisible by 60 (1). 5 and 12 have no common factor (1), so $5\\times12=60$ divides $n$: the converse is true (1).", "1+1+1"),
    Q("Show that “If $n$ is divisible by 4 and by 6, then it is divisible by 24” is false. Give a counterexample and explain why the idea ‘4×6 = 24’ fails.", "$n=12$ is divisible by 4 and 6 but not by 24 (1½). 4 and 6 share the factor 2, so their product 24 is not the smallest common multiple; the LCM is 12 (1½).", "1½+1½"),
    Q("A class says “If it is Monday, our school has an assembly.” Write the converse and explain why it may not be true.", "Converse: If our school has an assembly, then it is Monday (1). The school may also hold assemblies on other days, e.g. on Independence Day (1). So an assembly day need not be Monday; the converse can be false (1).", "1+1+1"),
    Q("The number $2^{2^3}+1=257$ is prime. Explain why this does not prove that all numbers of the form $2^{2^n}+1$ are prime.", "Checking a few cases gives support only (1). A general claim needs a proof for every $n$ (1). In fact $2^{2^5}+1=2^{32}+1=4294967297=641\\times6700417$ is composite, so the claim fails (1).", "1+1+1"),
    Q("Write the following in ‘If … then …’ form and write its converse: “A number has exactly 3 factors when it is the square of a prime.”", "If a number is the square of a prime, then it has exactly 3 factors (1½). Converse: If a number has exactly 3 factors, then it is the square of a prime (1½).", "1½+1½"),
    Q("A sticks-and-diagonals model: a quadrilateral is of type Q when it has equal diagonals. (a) Must the two sticks have equal length? (b) Does the way they are placed matter if the diagonals only need to be equal?", "(a) Yes, the sticks must be equal since the diagonals are the sticks (1½). (b) Yes, it matters: if the sticks cross at their midpoints a rectangle results; if they cross elsewhere an isosceles trapezium can result, so equal sticks alone do not fix the shape (1½).", "1½+1½"),
    Q("Use the converse of the Baudhāyana–Pythagoras theorem to find which of these triples can be the sides of a right triangle: (i) 8, 15, 17 (ii) 10, 24, 27.", "(i) $64+225=289=17^2$ ✓ right-angled (1½). (ii) $100+576=676$ but $27^2=729$ ✗ (1½).", "1½+1½"),
    Q("Write the converse of “If a triangle is isosceles, then it has two equal angles”. Is it true? Briefly justify using an altitude.", "Converse: If a triangle has two equal angles, then it is isosceles (1). It is true (1). Draw the altitude from the third vertex; the two right triangles are congruent by AAS, so the sides opposite the equal angles are equal (1).", "1+1+1"),
    Q("Give two examples (one from number theory and one from geometry) of propositions that are true but whose converses are false.", "Number theory: If $n$ is a multiple of 8, then it is a multiple of 4; converse false (12) (1½). Geometry: If a quadrilateral is a square, then all angles are equal; converse false (a rectangle) (1½).", "1½+1½"),
    Q("Check whether the numbers $n=1,2,3,4,5$ make $n^2-n+41$ prime. Does this prove that it is always prime? Find an $n$ that gives a counterexample.", "Values: 41, 43, 47, 53, 61 are prime (1). Checking a few cases does not prove it (1). $n=41$ gives $41^2-41+41=1681=41\\times41$, composite (1).", "1+1+1"),
    Q("Write the converse of “If $x=y$, then $a+x=a+y$”. Show that both are true and say where this is used.", "Converse: If $a+x=a+y$, then $x=y$ (1). Proposition: adding $a$ to equals gives equals; converse: subtract $a$ from both sides (1). Used while solving equations by balancing (1).", "1+1+1"),
    Q("If $n$ and $n+3$ have no common factor, then $n$ is not a multiple of 3. Write the converse. Is the converse true?", "Converse: If $n$ is not a multiple of 3, then $n$ and $n+3$ have no common factor (1). Their common factors divide the difference 3, so only 1 or 3 can be common (1). If $n$ is not a multiple of 3, 3 does not divide $n$, so the converse is true (1).", "1+1+1"),
    Q("A teacher says “If a number is a multiple of 8, it is a multiple of 2 and of 4.” Write the converse. Does ‘divisible by 2 and 4’ suffice to test divisibility by 8? Give an example.", "Converse: If a number is a multiple of 2 and of 4, then it is a multiple of 8 (1). Not sufficient (1): 12 is divisible by 2 and 4 but not by 8 (1).", "1+1+1"),
    Q("Write the converse of “If the sum of the digits of a number is a multiple of 3, then the number is divisible by 3.” Is it true?", "Converse: If a number is divisible by 3, then the sum of its digits is a multiple of 3 (1½). It is true: the divisibility rule works in both directions, e.g. 741 and $7+4+1=12$ (1½).", "1½+1½"),
    Q("Show with an example that “If two triangles have equal areas, then they are congruent” is false, and write its converse and its truth.", "Counterexample: a 6 cm × 4 cm right triangle and a 12 cm × 2 cm right triangle both have area 12 cm² but are not congruent (1½). Converse: If two triangles are congruent, they have equal area — true (1½).", "1½+1½"),
]
assert 8 * 8 + 15 * 15 == 17 * 17 and 10 * 10 + 24 * 24 == 676 != 27 * 27 and 41 * 41 - 41 + 41 == 1681 and 2 ** 32 + 1 == 4294967297 and 12 % 4 == 0 and 12 % 6 == 0 and 12 % 24 and 741 % 3 == 0 and 7 + 4 + 1 == 12
assert len(C) == 24, len(C)

# ---- D (16): 5 marks
D += [
    Q("<b>Case study:</b> Anu writes: “If it rains, the road is wet.” (i) Write the converse. (ii) Give a situation showing the converse can be false. (iii) Is the original proposition always true? (iv) Define a counterexample and explain how it helps.", "(i) If the road is wet, then it has rained (1). (ii) A water tanker spills water on the road, or a drain overflows (1). (iii) Yes, in normal situations rain makes roads wet (1). (iv) A counterexample is an instance that satisfies the ‘if’ part but not the ‘then’ part (1); one such case shows quickly that a proposition is false (1).", "1+1+1+1+1"),
    Q("Prove that the converse of the Baudhāyana–Pythagoras theorem is true: if a triangle $ABC$ has $a^2+b^2=c^2$, then it is right-angled.", "Construct right triangle $XYZ$ with perpendicular sides $YZ=a$, $XZ=b$ (1). By the theorem $XY^2=a^2+b^2=c^2$, so $XY=c$ (1). In triangles $ABC$ and $XYZ$: $BC=YZ=a$, $AC=XZ=b$, $AB=XY=c$ (1). By SSS the triangles are congruent (1). So $\\angle C=\\angle Z=90^\\circ$ and $\\triangle ABC$ is right-angled (1).", "1+1+1+1+1"),
    Q("(i) Show that a perfect square has an odd number of factors by pairing factors, using the number 49 and the number 100. (ii) Write the converse and say whether it is true.", "(i) 49: pairs (1,49), (7,7) → factors 1, 7, 49: 3 (odd) (1). 100: pairs (1,100), (2,50), (4,25), (5,20), (10,10) → 9 factors (odd) (1½). (ii) Converse: If a number has an odd number of factors, then it is a perfect square (1). True: an odd count forces a repeated pair $(f,f)$, so $n=f\\times f$ (1½).", "2½+2½"),
    Q("<b>Case study:</b> Ravi tests the formula $n^2+n+11$ for $n=1,2,3,4$ and finds 13, 17, 23, 31, all prime. (i) Compute these values. (ii) Can Ravi conclude the formula always gives primes? (iii) Find the smallest $n$ in $\\{1,\\dots,11\\}$ for which the value is not prime. (iv) Name the idea of the example you found.", "(i) $1+1+11=13$, $4+2+11=17$, $9+3+11=23$, $16+4+11=31$ (1½). (ii) No — a few cases do not prove a general claim (1). (iii) $n=10$: $100+10+11=121=11^2$ is not prime; (smaller $n$ up to 9 give 13, 17, 23, 31, 41, 53, 67, 83, 101 — all prime) (1½). (iv) It is a counterexample (1).", "1½+1+1½+1"),
    Q("Write the converse of each proposition and decide whether each of the two statements is true. (i) If $x=y$, then $x^3=y^3$. (ii) If $x=y$, then $x^2=y^2$.", "(i) Proposition true (½). Converse: If $x^3=y^3$ then $x=y$ — true for real numbers because the cube is one-to-one (e.g. $x^3=-8\\Rightarrow x=-2$) (2). (ii) Proposition true (½). Converse: If $x^2=y^2$ then $x=y$ — false: $x=2,\\ y=-2$ (2).", "2½+2½"),
    Q("Show that the triangle with vertices on the grid $A(0,0),\\ B(7,0),\\ C(0,24)$ is right-angled using the Baudhāyana–Pythagoras converse, and find its hypotenuse and area.", "$AB=7$, $AC=24$, $BC=\\sqrt{49+576}=\\sqrt{625}=25$ (2). $AB^2+AC^2=49+576=625=BC^2$, so by the converse the triangle is right-angled at $A$ (1½). Area $=\\frac12\\times7\\times24=84$ square units (1½).", "2+1½+1½"),
    Q("<b>Case study:</b> A carpenter wants a corner to be exactly $90^\\circ$. He marks 3 units on one wall edge, 4 units on the other and checks that the distance across is 5 units. (i) Which result is used? (ii) Show the calculation. (iii) Is the converse needed or the theorem itself? (iv) Will 5-12-13 work too? Verify.", "(i) The converse of the Baudhāyana–Pythagoras theorem (1). (ii) $3^2+4^2=9+16=25=5^2$ (1). (iii) The converse: we know the sides and want to conclude the right angle (1). (iv) Yes, $5^2+12^2=25+144=169=13^2$ (2).", "1+1+1+2"),
    Q("(i) Prove that “If $n$ is the square of a prime $p$, then $n$ has exactly 3 factors.” (ii) State and prove the converse.", "(i) Factors of $p^2$ are $1, p, p^2$ only, because the only divisors of $p^2$ are products of the single prime $p$: 3 factors (2). (ii) Converse: If $n$ has exactly 3 factors, then $n=p^2$ for a prime $p$ (1). Three factors is odd, so $n$ is a perfect square $f\\times f$; if $f$ had a proper factor $g$ other than 1, then $g$ would give a fourth factor beyond $1,f,f^2$; so $f$ is prime (2).", "2+3"),
    Q("(i) Show that “If $n$ is a product of two unequal primes, then it has exactly 4 divisors” is true using 15 and 33. (ii) Is the converse true? Find a counterexample if any.", "(i) 15: 1, 3, 5, 15; 33: 1, 3, 11, 33 — 4 divisors each (2). (ii) Converse: If $n$ has exactly 4 divisors, then it is a product of two unequal primes (1). False: 8 has divisors 1, 2, 4, 8 (four divisors) but $8=2^3$ is not a product of two unequal primes (2).", "2+3"),
    Q("<b>Case study:</b> Meera notices: “All the rectangles I drew had equal diagonals.” (i) Write this as a proposition. (ii) Write the converse. (iii) Draw (describe) an isosceles trapezium to show the converse is false. (iv) Name a type of quadrilateral for which the converse is true under an extra condition.", "(i) If a quadrilateral is a rectangle, then its diagonals are equal (1). (ii) If a quadrilateral has equal diagonals, then it is a rectangle (1). (iii) An isosceles trapezium with parallel sides 6 cm and 10 cm and legs 5 cm has equal diagonals but no right angle (1½). (iv) A parallelogram: if a parallelogram has equal diagonals, it is a rectangle (1½).", "1+1+1½+1½"),
    Q("(i) Test whether the triples (a) 15, 20, 25 and (b) 11, 60, 62 can form right-angled triangles. (ii) Explain why a triple that satisfies $a^2+b^2=c^2$ must form a right-angled triangle.", "(i)(a) $225+400=625=25^2$ ✓ right-angled (1½). (b) $121+3600=3721$; $62^2=3844$ ✗ not right-angled (1½). (ii) Build a right triangle with legs $a,b$; its hypotenuse is $\\sqrt{a^2+b^2}=c$; both triangles have the same three sides, so they are congruent by SSS and the given one has a right angle (2).", "3+2"),
    Q("Show that the following propositions are false by giving a counterexample: (i) If $n$ is an odd number, then $n^2+2$ is prime. (ii) If $n$ is a prime, then $n^2-1$ is a multiple of 4. (iii) If $n$ is divisible by 9, then it is divisible by 27.", "(i) $n=7$: $49+2=51=3\\times17$ is not prime (1½). (ii) $n=2$ is prime but $4-1=3$ is not a multiple of 4 (1½). (iii) $n=18$ is divisible by 9, not by 27 (2).", "1½+1½+2"),
    Q("Explain (i) why a proposition and its converse can both be true, using the statement about equal angles opposite equal sides in a triangle, and (ii) the example of both being false.", "(i) Proposition: equal sides ⇒ equal opposite angles (isosceles triangle theorem); converse: equal angles ⇒ equal opposite sides, proved by the altitude and AAS (2½). (ii) Proposition: “If a number is a multiple of 3, it is a multiple of 5” is false (e.g. 6); its converse “If a number is a multiple of 5, it is a multiple of 3” is also false (e.g. 10) (2½).", "2½+2½"),
    Q("<b>Case study:</b> The statement “If a number is divisible by 6, then it is divisible by 3” is checked on the numbers 18, 24, 30. (i) Verify. (ii) Write the converse. (iii) Test it on 9, 15, 21, 12 and find which of these are counterexamples. (iv) What fraction of the tested numbers is divisible by 6?", "(i) 18=3×6, 24=3×8, 30=3×10 ✓ (1). (ii) If a number is divisible by 3, then it is divisible by 6 (1). (iii) 9, 15, 21 are divisible by 3 but not by 6: counterexamples; 12 is divisible by both (2). (iv) Of 9, 15, 21, 12 only 12 is divisible by 6: $\\frac14$ (1).", "1+1+2+1"),
    Q("(i) Why does the argument “the number of factors is odd, so a factor pair repeats” prove only the converse of ‘perfect squares have an odd number of factors’? (ii) How can the argument be extended to prove the proposition itself?", "(i) The argument starts from ‘odd number of factors’ and ends at ‘perfect square’, i.e. the direction (odd factors ⇒ square), the converse (2). (ii) Start from $n=f\\times f$; the pair $(f,f)$ exists; two such repeated pairs cannot exist, so all other factors pair up in twos and the count is odd ⇒ proposition proved (3).", "2+3"),
    Q("A trader says: “If I sell more articles, my profit is more.” (i) Write the converse. (ii) A shop sells 10 pens at ₹4 profit each and then 20 pens at ₹1 profit each; show that selling more gave less profit. (iii) Give a situation to show that the converse can be false. (iv) What are such examples called?", "(i) If my profit is more, then I have sold more articles (1). (ii) 10 pens × ₹4 = ₹40; 20 pens × ₹1 = ₹20; more pens, less profit (1½). (iii) 5 laptops at ₹2000 profit = ₹10000 versus 50 pens at ₹10 profit = ₹500: more profit with fewer articles sold (1½). (iv) Counterexamples (1).", "1+1½+1½+1"),
]
assert 7 ** 2 + 24 ** 2 == 25 ** 2 and 7 ** 2 + 2 == 51 and 15 ** 2 + 20 ** 2 == 25 ** 2 and 11 ** 2 + 60 ** 2 == 3721 != 62 ** 2 and nf(8) == 4 and nf(15) == 4 and nf(33) == 4 and 10 ** 2 + 10 + 11 == 121
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
