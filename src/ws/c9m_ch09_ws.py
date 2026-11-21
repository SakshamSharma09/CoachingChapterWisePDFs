"""Class 9 Maths Ch 9 - Propositions and their Converses: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch09"

def _old(n):
    d = "c9_maths1" if n < 9 else "c9_maths2"
    p = Path(__file__).resolve().parents[1] / "rn_work" / d / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def isprime(n): return n > 1 and all(n % i for i in range(2, int(n**.5) + 1))
def nf(n): return sum(1 for i in range(1, n + 1) if n % i == 0)
assert 9*3 == 27 and 9**2+12**2 == 15**2 and 60**2+80**2 == 100**2 and 8**2+15**2 == 17**2 and 5**2+12**2 == 13**2
assert 6**2+8**2 != 11**2 and 7**2+9**2 != 12**2 and 4**2+5**2 != 6**2 and 3**2+4**2 == 5**2
assert nf(36) == 9 and nf(49) == 3 and nf(50) == 6 and nf(48) == 10 and nf(30) == 8 and nf(64) == 7
assert 10**2+10+11 == 121 == 11*11 and 11**2+11+11 == 143 == 11*13 and 2**11-1 == 2047 == 23*89
assert all(isprime(2**p-1) for p in (2, 3, 5, 7)) and not isprime(2**11-1)
assert all(isprime(n*n-n+41) for n in range(1, 6)) and 41*41-41+41 == 1681 == 41**2
assert [2**(2**k)+1 for k in range(5)] == [3, 5, 17, 257, 65537] and 641*6700417 == 2**32+1 == 4294967297
assert 20**2+21**2 == 841 and 28**2 == 784 and 8**2+15**2 == 289 and 15**2+8**2 == 17**2 and 21**2+20**2 == 29**2 and 15**2+8**2 == 289
assert 5*5-2*2 == 21 and 2*5*2 == 20 and 5*5+2*2 == 29 and 4*4-1 == 15 and 8*15//2 == 60 and 60*120 == 7200
assert [k for k in range(1, 21) if nf(k) % 2] == [1, 4, 9, 16] and len([k for k in range(1, 101) if nf(k) % 2]) == 10
assert 6 % 4 and 12 % 24 and 12 % 4 == 0 and 12 % 6 == 0 and 12 % 8 and 2*4 % 2 == 0
assert 6 % 2 == 0 and 6 % 3 == 0 and 6 % 4 != 0   # 6 | 2*3 but 6 divides neither 2 nor 3 (a=6,b=2,c=3 -> bc=6)

WS = [
# ---------------- EASY ----------------
W(r"The converse of 'If it is Monday, then the school is open' is:", 1, r"(b) If the school is open, then it is Monday. The 'if' and 'then' parts are swapped. (1)", "E",
  opts=["If it is not Monday, then the school is closed", "If the school is open, then it is Monday", "If the school is closed, then it is Monday", "If it is Monday, then the school is closed"]),
W(r"Which of the following is a proposition (a statement that is either true or false)?", 1, r"(c) 'The sum of the angles of a triangle is $180^\circ$' is a true statement. 'Close the door' is a command, 'Is 7 prime?' is a question and '$x+2=5$' is true or false depending on $x$. (1)", "E",
  opts=["Close the door", "Is 7 prime?", r"The sum of the angles of a triangle is $180^\circ$", "$x+2=5$"]),
W(r"A counterexample to the claim 'If a number is odd, then it is prime' is:", 1, r"(d) 9. It is odd but $9=3\times3$ is not prime. (1)", "E", opts=["3", "5", "7", "9"]),
W(r"The converse of the Baudhāyana-Pythagoras theorem is:".replace(r"ā", "ā"), 1, r"(c) If $a^2+b^2=c^2$ for the sides of a triangle, then the triangle is right-angled. (1)", "E",
  opts=["If a triangle is right-angled, then $a^2+b^2=c^2$", "If a triangle is equilateral, then it is right-angled", "If $a^2+b^2=c^2$ for the sides of a triangle, then the triangle is right-angled", "If $a+b=c$, then the triangle is right-angled"]),
W(r"Which set of sides makes a right-angled triangle?", 1, r"(b) $5, 12, 13$ since $25+144=169=13^2$. For the others: $36+64=100\neq121$; $49+81=130\neq144$; $16+25=41\neq36$. (1)", "E", opts=["$6, 8, 11$", "$5, 12, 13$", "$7, 9, 12$", "$4, 5, 6$"]),
W(r"The number of factors of 36 is:", 1, r"(a) 9. Factors: $1,2,3,4,6,9,12,18,36$. The pair $(6,6)$ gives only one factor, so the count is odd. (1)", "E", opts=["9", "8", "10", "6"]),
W(r"Write 'A square has four equal sides' in the 'if ... then ...' form and write its converse.", 2, r"If a figure is a square, then it has four equal sides (1). Converse: if a figure has four equal sides, then it is a square (false, since a rhombus has four equal sides) (1).", "E"),
W(r"'If it rains, the road is wet.' Write the converse. Is the converse always true? Give a situation.", 2, r"Converse: if the road is wet, then it has rained (1). Not always true: a water tanker may have spilled water on a dry day (1).", "E", wp=True),
W(r"A school says: 'If Ravi scores above 90%, he gets a medal.' Ravi has a medal. Can we be sure that he scored above 90%? Explain using the converse.", 2, r"No (1). The converse 'if he has a medal, then he scored above 90%' is not given; he may have won the medal in sports (1).", "E", wp=True),
W(r"State the converse of 'If two angles are vertically opposite, then they are equal.' Is the converse true? Give a reason.", 2, r"Converse: if two angles are equal, then they are vertically opposite (1). False: two angles of an equilateral triangle are equal but are not vertically opposite (1).", "E"),
W(r"At a museum the rule is 'If a visitor is under 5 years old, entry is free.' Senior citizens also enter free. Aarav's entry was free. Can we conclude that he is under 5? Explain.", 2, r"No (1). The rule is one-way; the converse 'free entry implies under 5' is false, because senior citizens also get free entry (1).", "E", wp=True),
W(r"Give a counterexample to the statement: 'If a number is a multiple of 3, then it is odd.'", 2, r"$6$ is a multiple of 3 (1) but it is even, so the statement is false (1).", "E"),
W(r"True or false (give a reason or counterexample): every prime number is odd.", 2, r"**False.** The prime number 2 is even, so 2 is a counterexample (2).", "E"),
W(r"State the converse of 'If a number is divisible by 10, then it is divisible by 5.' Is the converse true? Give a counterexample if it is false.", 2, r"Converse: if a number is divisible by 5, then it is divisible by 10 (1). False: 15 is divisible by 5 but not by 10 (1).", "E"),
W(r"Rohan's mother says: 'If you finish your homework, you can play.' Rohan is playing. Can we conclude that he finished his homework? Explain.", 2, r"No (1). The statement tells what happens when the homework is finished; it does not say that play happens only then. The converse is not given (1).", "E", wp=True),
W(r"Check whether a triangle with sides 9 cm, 12 cm and 15 cm is right-angled.", 2, r"$9^2+12^2=81+144=225$ (1) $=15^2$, so by the converse of the Baudhāyana-Pythagoras theorem it is right-angled (1).".replace(r"ā", "ā"), "E"),
W(r"A carpenter measures the sides of a door frame as 60 cm and 80 cm and the diagonal as 100 cm. Is the corner a right angle?", 2, r"$60^2+80^2=3600+6400=10000$ (1) $=100^2$, so the triangle formed is right-angled and the corner is a right angle (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"Write the converse of 'If a quadrilateral is a square, then all its angles are right angles.' Is the converse true? Support your answer.", 2, r"Converse: if all angles of a quadrilateral are right angles, then it is a square (1). False; a rectangle with unequal sides is a counterexample (1).", "M"),
W(r"Show that the claim '$n^2-n+41$ is prime for every natural number $n$' is false.", 2, r"For $n=41$: $41^2-41+41=41^2=1681$ (1), which is not prime. So $n=41$ is a counterexample (1).", "M"),
W(r"A claim says: 'If $n$ is prime, then $2^n-1$ is prime.' Check it for $n=2,3,5,7$ and then show that it is false using $n=11$.", 3, r"$n=2,3,5,7$ give $3, 7, 31, 127$, all prime (1). $n=11$ gives $2^{11}-1=2047$ (1) $=23\times89$, composite; so the claim is false (1).", "M"),
W(r"Write the converse of 'If a number is divisible by 24, then it is divisible by 4 and by 6.' Is it true? Explain with an example.", 3, r"Converse: if a number is divisible by 4 and by 6, then it is divisible by 24 (1). False: 12 is divisible by 4 and 6 but not by 24 (1). 4 and 6 have a common factor 2, so $4\times6=24$ is not their least common multiple (1).", "M"),
W(r"Sunita says: 'If a number is divisible by 2 and by 4, then it is divisible by 8.' Find a counterexample. Write a correct 'if ... then ...' statement connecting 8 with 2 and 4.", 2, r"12 is divisible by 2 and by 4 but $12\div8$ is not a whole number (1). Correct: if a number is divisible by 8, then it is divisible by 2 and by 4 (1).", "M"),
W(r"A library rule says: 'If a book is returned late, a fine is charged.' Neha was charged a fine. Is her book necessarily late? Give another reason that can lead to a fine and name the converse involved.", 2, r"Not necessarily (1). The converse 'if a fine is charged, then the book was late' need not hold; the book could have been damaged or lost (1).", "M", wp=True),
W(r"Prove that the sum of two even numbers is even. Write the converse and show that it is false.", 3, r"Let the numbers be $2a$ and $2b$; the sum is $2(a+b)$, which is even (1). Converse: if the sum of two numbers is even, both are even (1). False: $3+5=8$ is even but 3 and 5 are odd (1).", "M"),
W(r"Prove that if $n$ is odd, then $n^2$ is odd. Is the converse 'if $n^2$ is odd then $n$ is odd' true? Explain.", 3, r"Let $n=2k+1$; $n^2=4k^2+4k+1=2(2k^2+2k)+1$, which is odd (1). Converse is true (1): if $n$ were even, $n=2k$ and $n^2=4k^2$ would be even, so an odd square forces an odd $n$ (1).", "M"),
W(r"Write each statement in the 'if ... then ...' form: (i) All squares are rectangles. (ii) A number is divisible by 6 only if it is even. (iii) The sum of the angles of a triangle is $180^\circ$.", 3, r"(i) If a figure is a square, then it is a rectangle (1). (ii) If a number is divisible by 6, then it is even (1). (iii) If a figure is a triangle, then the sum of its angles is $180^\circ$ (1).", "M"),
W(r"In the old method of 'rope-stretching', a rope with 12 equally spaced knots (12 equal parts) is pegged to form a triangle with sides of 3, 4 and 5 parts. Explain why the corner between the sides of 3 and 4 parts is a right angle.", 2, r"$3^2+4^2=9+16=25=5^2$ (1). By the converse of the Baudhāyana-Pythagoras theorem the triangle is right-angled, the right angle being opposite the longest side, i.e. between the sides 3 and 4 (1).".replace(r"ā", "ā"), "M", wp=True),
W(r"A triangular plot has sides 20 m, 21 m and 28 m. Is it right-angled? Show your working.", 2, r"$20^2+21^2=400+441=841$ (1). $28^2=784\neq841$, so the plot is not right-angled (1).", "M", wp=True),
W(r"A farmer's triangular plot has sides 15 m, 20 m and 25 m. Show that it is right-angled, name the sides that meet at the right angle and find the area of the plot.", 3, r"$15^2+20^2=225+400=625=25^2$ (1). The right angle is between the 15 m and 20 m sides, opposite the longest side (1). Area $=\frac12\times15\times20=150$ m² (1).", "M", wp=True),
W(r"State the converse of 'If a quadrilateral is a rectangle, then its diagonals are equal.' Show that the converse is false using an isosceles trapezium.", 3, r"Converse: if the diagonals of a quadrilateral are equal, then it is a rectangle (1). An isosceles trapezium has equal diagonals (1) but its angles are not all right angles, so it is not a rectangle (1).", "M"),
W(r"Find the number of factors of 49 and of 50. Which of the two numbers is a perfect square, and how does the number of factors show it?", 2, r"49 has factors $1, 7, 49$ (3, odd); 50 has $1,2,5,10,25,50$ (6, even) (1). 49 is the perfect square: a square has an odd number of factors because one pair repeats, $(7,7)$ (1).", "M"),
W(r"**Lockers.** There are 20 lockers, all closed. Student 1 changes (opens or closes) every locker, student 2 changes every 2nd locker, student 3 every 3rd locker, and so on up to student 20. Which lockers are open at the end? Give the reason.", 3, r"Locker $k$ is changed once for each factor of $k$ (1). It ends open if it is changed an odd number of times, i.e. if $k$ has an odd number of factors (1). Only perfect squares do, so lockers 1, 4, 9 and 16 are open (1).", "M", wp=True),
W(r"Kabir tests $n^2-n+41$ for $n=1,2,3,4,5$ and gets $41, 43, 47, 53, 61$, all prime. He concludes that it is always prime. Explain why his reasoning is not a proof.", 3, r"Testing a few cases only supports a claim; a proof must cover every case (1.5). In fact $n=41$ gives $41^2=1681$, which is not prime, so the claim is false (1.5).", "M"),
W(r"Decide whether each statement is true or false, giving a proof or a counterexample: (i) The product of two odd numbers is odd. (ii) The sum of two odd numbers is odd.", 3, r"(i) True: $(2a+1)(2b+1)=4ab+2a+2b+1=2(2ab+a+b)+1$, odd (1.5). (ii) False: $3+5=8$ is even (1.5).", "M"),
W(r"Write the converse of each statement and say whether it is true: (i) If a number ends in 0, it is divisible by 10. (ii) If a number is divisible by 9, it is divisible by 3. (iii) If two triangles are congruent, they have equal areas.", 3, r"(i) If a number is divisible by 10, it ends in 0: true (1). (ii) If a number is divisible by 3, it is divisible by 9: false, e.g. 6 (1). (iii) If two triangles have equal areas, they are congruent: false, e.g. $3\times4$ and $2\times6$ right triangles (1).", "M"),
W(r"A 17 m ladder has its foot 8 m from a wall and its top touches the wall at a height of 15 m. Use the converse of the Baudhāyana-Pythagoras theorem to show that the wall is perpendicular to the ground (assume the ground is level).".replace(r"ā", "ā"), 3, r"The ladder, the wall from the ground to the top and the ground from the wall to the foot form a triangle with sides 8, 15 and 17 (1). $8^2+15^2=64+225=289=17^2$ (1). So the triangle is right-angled at the corner where the wall meets the ground, so the wall is perpendicular to the ground (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"Prove, for a three-digit number $N=100a+10b+c$, that $N$ is divisible by 3 if and only if its digit sum $a+b+c$ is divisible by 3. State clearly both directions.", 4, r"$N=99a+9b+(a+b+c)=3(33a+3b)+(a+b+c)$ (1). If $(a+b+c)$ is divisible by 3, both parts are multiples of 3, so $N$ is (1.5). Conversely, if $N$ is divisible by 3, then $a+b+c=N-3(33a+3b)$ is a difference of multiples of 3, so it is divisible by 3 (1.5).", "H"),
W(r"List the factors of 36 as pairs and explain why 36 has an odd number of factors. Then use factors to show that 48 is not a perfect square.", 4, r"Pairs: $(1,36),(2,18),(3,12),(4,9),(6,6)$ (1). The pair $(6,6)$ is a single factor, so the count is $4\times2+1=9$, odd (1.5). 48 has factors $1,2,3,4,6,8,12,16,24,48$: ten, an even number, so it is not a perfect square (1.5).", "H"),
W(r"**Lockers again.** A school has 100 lockers, all closed. Student $k$ ($k=1$ to 100) changes every $k$th locker. (i) How many lockers are open at the end? (ii) Is locker 30 open? Explain with factors. (iii) Is locker 64 open?", 4, r"(i) Open lockers are those with an odd number of factors, i.e. the perfect squares $1,4,9,\ldots,100$: 10 lockers (2). (ii) 30 has 8 factors ($1,2,3,5,6,10,15,30$), even, so it is closed (1). (iii) 64 is a perfect square with 7 factors, so it is open (1).", "H", wp=True),
W(r"Triangle ABC has sides $AB=13$, $BC=5$ and $CA=12$. Prove that it is right-angled by constructing a triangle XYZ with $YZ=5$, $ZX=12$ and $\angle Z=90^\circ$. Find XY and complete the argument.", 4, r"In XYZ, $XY^2=5^2+12^2=169$, so $XY=13$ (1.5). Triangles ABC and XYZ have $BC=YZ$, $CA=ZX$, $AB=XY$ (1). So they are congruent by SSS and $\angle C=\angle Z=90^\circ$ (1.5).", "H"),
W(r"For positive integers $m>n$, the numbers $m^2-n^2$, $2mn$ and $m^2+n^2$ are often the sides of a right triangle. (i) Prove $(m^2-n^2)^2+(2mn)^2=(m^2+n^2)^2$. (ii) Find the sides for $m=5$, $n=2$. (iii) What does the converse of the Baudhāyana-Pythagoras theorem tell us about the triangle?".replace(r"ā", "ā"), 4, r"(i) $(m^2-n^2)^2+4m^2n^2=m^4-2m^2n^2+n^4+4m^2n^2=m^4+2m^2n^2+n^4=(m^2+n^2)^2$ (2). (ii) $21, 20, 29$; check $441+400=841=29^2$ (1). (iii) The sides satisfy $a^2+b^2=c^2$, so the triangle is right-angled, with the right angle between the sides 21 and 20 (1).", "H"),
W(r"A sail-maker cuts triangular sails with sides $2x$, $x^2-1$ and $x^2+1$ metres. For $x=4$, show that the sail is right-angled, name the sides at the right angle, find the area and the cost of the cloth at ₹ 120 per m².", 4, r"Sides: $8, 15, 17$ m (1). $8^2+15^2=64+225=289=17^2$, so it is right-angled, with the right angle between the 8 m and 15 m sides (1). Area $=\frac12\times8\times15=60$ m² (1). Cost $=60\times120=$ ₹ 7,200 (1).", "H", wp=True),
W(r"Consider: A: 'If a figure is a square, then it is a rhombus.' B: 'If a figure is a rhombus, then it is a square.' Which is true? Are A and B converses? Explain with a counterexample and say what extra condition makes B true.", 3, r"A is true: a square has four equal sides (1). B is false: a rhombus with angles $60^\circ$ and $120^\circ$ is not a square (1). A and B are converses of each other. B becomes true if one angle is a right angle (rhombus with a right angle is a square) (1).", "H"),
W(r"(i) Give a proposition about numbers such that both it and its converse are false, and justify with counterexamples. (ii) Can this happen for 'If a number is divisible by 6, then it is divisible by 3'? Explain.", 3, r"(i) 'If a number is a multiple of 3, then it is a multiple of 5.' Counterexample: 3. Converse 'multiple of 5 implies multiple of 3': counterexample 5 (1.5). (ii) No: the proposition is true (every multiple of 6 is a multiple of 3); only its converse is false, since 9 is divisible by 3 but not by 6 (1.5).", "H"),
W(r"**Case study (Fermat and Euler).** Fermat guessed that every number $F_n=2^{2^n}+1$ is prime. (i) Find $F_0, F_1, F_2, F_3$ and check that they are prime (257 is prime). (ii) Euler found $F_5=2^{32}+1=4294967297=641\times6700417$. Verify the product. (iii) Explain what this shows about proving a claim from examples.", 5, r"(i) $F_0=2^1+1=3$, $F_1=2^2+1=5$, $F_2=2^4+1=17$, $F_3=2^8+1=257$; all prime (2). (ii) $6700417\times641=4020250200+274717097=4294967297$ (1.5). (iii) $F_5$ is a single counterexample, so Fermat's claim is false although it held for the first several cases; examples never prove a claim (1.5).", "H"),
W(r"Prove that the product of two consecutive whole numbers is even. Write the converse and show that it is false.", 4, r"Of two consecutive numbers $n$ and $n+1$ exactly one is even (1). So the product contains the factor 2 and is even (1.5). Converse: if the product of two numbers is even, they are consecutive (1). False: $2\times4=8$ is even but 2 and 4 are not consecutive (0.5).", "H"),
W(r"A shop board says: 'If today is Sunday, the shop is closed.' (i) You find the shop closed. What can you say about the day? (ii) You find the shop open. What can you say? Explain your reasoning.", 4, r"(i) Nothing definite (1). The statement does not say that the shop is closed only on Sundays; it may also be closed on another holiday (1). (ii) Today is not Sunday (1), because if it were Sunday the shop would have to be closed (1).", "H", wp=True),
W(r"The converse of 'If two sides of a triangle are equal, then the angles opposite them are equal' is 'If two angles of a triangle are equal, then the sides opposite them are equal.' Prove the converse: in triangle ABC with $\angle B=\angle C$, draw $AD\perp BC$ and prove $AB=AC$.", 4, r"In triangles ABD and ACD: $\angle B=\angle C$ (given) (1), $\angle ADB=\angle ADC=90^\circ$ (1), $AD=AD$ common (1). Hence the triangles are congruent by AAS and $AB=AC$ by CPCT (1).", "H"),
W(r"Is the statement 'If $a$ divides $bc$, then $a$ divides $b$ or $a$ divides $c$' true? Test it with $a=6$, $b=2$, $c=3$, and say when it does hold.", 3, r"$bc=6$ and $6$ divides 6, but 6 divides neither 2 nor 3 (1.5). So the statement is false; $a=6,b=2,c=3$ is a counterexample. It does hold when $a$ is a prime number (1.5).", "H"),
W(r"If $(a, b, c)$ is a right-angled triple ($a^2+b^2=c^2$), show that $(2a, 2b, 2c)$ is also one. Is the converse (if $(2a,2b,2c)$ is a triple then so is $(a,b,c)$) true? Use it to test sides 18, 24, 30.", 3, r"$(2a)^2+(2b)^2=4(a^2+b^2)=4c^2=(2c)^2$ (1). Converse: $4a^2+4b^2=4c^2$ gives $a^2+b^2=c^2$, true (1). For 18, 24, 30: halves $9, 12, 15$ satisfy $81+144=225$, so it is right-angled (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(9)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "9.5 Writing and Reading Statements"),
 ("table", ["Wording", "Means", "Example"], [
  ["If X, then Y", "X ⇒ Y", "If a figure is a square, then it is a rectangle"],
  ["X implies Y", "X ⇒ Y", "x = 3 implies x² = 9"],
  ["X only if Y", "X ⇒ Y (not Y ⇒ X)", "A number is divisible by 6 only if it is even"],
  ["Y whenever X; Y when X", "X ⇒ Y", "The road is wet whenever it rains"],
  ["All A are B", "If it is an A, then it is a B", "All squares are rectangles"],
  ["X if and only if Y", "both X ⇒ Y and Y ⇒ X", "A number is divisible by 3 iff its digit sum is"]]),
 ("note", "IMPORTANT", "**Reading a one-way statement.** ‘If it rains, the road is wet’ lets you conclude from rain to a wet road. A wet road tells you nothing sure about rain. But if the road is **dry**, you can say it has **not** rained (rain would have made it wet)."),
 ("h2", "9.6 Proving with Even and Odd Numbers"),
 ("p", "Algebra turns ‘for every number’ into a proof. An **even** number is 2k and an **odd** number is 2k + 1 (k a whole number). A proof must work for all k, not just a few."),
 ("table", ["Claim", "Proof idea", "Converse"], [
  ["Sum of two even numbers is even", "2a + 2b = 2(a + b)", "False: 3 + 5 = 8"],
  ["Product of two odd numbers is odd", "(2a + 1)(2b + 1) = 2(2ab + a + b) + 1", "False: 3 × 4 is even but 3 and 4 are not both odd"],
  ["If n is odd, n² is odd", "(2k + 1)² = 2(2k² + 2k) + 1", "True: if n were even, n² = 4k² would be even"],
  ["Product of two consecutive numbers is even", "one of n, n + 1 is even", "False: 2 × 4 is even"],
  ["3-digit number: divisible by 3 ⇔ digit sum divisible by 3", "100a + 10b + c = 3(33a + 3b) + (a + b + c)", "True (both ways)"]]),
 ("h2", "9.7 Worked Examples"),
 ("h3", "Example 1 — Writing and testing a converse"),
 ("steps", [("Proposition", "If a quadrilateral is a rectangle, then its diagonals are equal. (True)"), ("Converse", "If the diagonals of a quadrilateral are equal, then it is a rectangle."), ("Test", "An isosceles trapezium has equal diagonals but its angles are not all right angles. The converse is **false**.")]),
 ("h3", "Example 2 — Disproving a claim by a counterexample"),
 ("steps", [("Claim", "n² − n + 41 is prime for every natural number n."), ("Tests", "n = 1 to 5 give 41, 43, 47, 53, 61, all prime. This only supports the claim."), ("Counterexample", "n = 41 gives 41² − 41 + 41 = 41² = 1,681 = 41 × 41, which is not prime. The claim is false.")]),
 ("h3", "Example 3 — Is it a right angle? (converse of Baudhāyana–Pythagoras)"),
 ("steps", [("A plot has sides 15 m, 20 m, 25 m", "Square them: 225, 400, 625."), ("Test", "225 + 400 = 625 = 25², so the plot is right-angled; the right angle is between the 15 m and 20 m sides."), ("Area", "½ × 15 × 20 = 150 m². Compare sides 20, 21, 28: 400 + 441 = 841 ≠ 784, so that plot is not right-angled.")]),
 ("h3", "Example 4 — Lockers and perfect squares"),
 ("steps", [("Student k changes every kth locker", "Locker n is changed once for each factor of n."), ("Which lockers end up open?", "Those changed an odd number of times, i.e. with an odd number of factors: the perfect squares."), ("For 100 lockers", "1, 4, 9, 16, 25, 36, 49, 64, 81, 100: ten lockers are open. Locker 30 has eight factors (1, 2, 3, 5, 6, 10, 15, 30), so it is closed.")]),
 ("h3", "Example 5 — Proof of a converse by congruence"),
 ("steps", [("To prove", "If ∠B = ∠C in triangle ABC, then AB = AC."), ("Construction", "Draw AD ⊥ BC. In triangles ABD and ACD: ∠B = ∠C, ∠ADB = ∠ADC = 90°, AD common."), ("Conclusion", "The triangles are congruent (AAS), so AB = AC by CPCT.")]),
 ("h3", "Example 6 — Reasoning from a one-way rule"),
 ("steps", [("Rule: If today is Sunday, the shop is closed", "Shop found closed: no sure conclusion (it may be another holiday)."), ("Shop found open", "Then today is not Sunday, because on Sunday it would be closed."), ("Why", "The rule fixes the shop for Sunday; it never says what happens on other days.")]),
 ("h3", "Example 7 — Fermat's claim and Euler's counterexample"),
 ("steps", [("Fermat's numbers 2^(2ⁿ) + 1", "n = 0, 1, 2, 3, 4 give 3, 5, 17, 257, 65,537, all prime."), ("Euler's counterexample", "n = 5 gives 2³² + 1 = 4,294,967,297 = 641 × 6,700,417, which is composite."), ("Lesson", "Five true cases did not make the claim true; one failure ended it.")]),
 ("h2", "9.8 Word Problems: How to Translate"),
 ("table", ["Situation", "If–then statement", "What you can and cannot conclude"], [
  ["Entry free for children under 5", "If a visitor is under 5, then entry is free", "Free entry does not prove under 5 (senior citizens may be free too)"],
  ["A medal for above 90%", "If a student scores above 90%, then she gets a medal", "Medal does not prove above 90% (sports medals exist)"],
  ["Fine for late return", "If a book is late, then a fine is charged", "Fine does not prove late (damage fine); no fine means not late"],
  ["Door frame 60, 80, diagonal 100", "If a² + b² = c², then the corner is a right angle", "3,600 + 6,400 = 10,000, so it is square"],
  ["Ladder 8 m, 15 m, 17 m", "If a² + b² = c², the triangle is right-angled", "The wall is perpendicular to the ground"],
  ["Knotted 12-part rope", "Sides 3, 4, 5 satisfy 9 + 16 = 25", "A right angle is formed; used by ancient builders"]]),
 ("h2", "9.9 Common Mistakes"),
 ("table", ["Wrong idea", "Why it is wrong", "Correct"], [
  ["‘The proposition is true, so the converse is true’", "the converse is a different statement", "check it separately; e.g. multiple of 6 ⇒ multiple of 3 but not conversely"],
  ["‘It worked for n = 1, 2, 3, 4, 5, so it is proved’", "examples do not cover every case", "give a general proof or find one counterexample"],
  ["Using a counterexample to prove a statement true", "a counterexample only disproves", "prove with algebra or reasoning for every case"],
  ["‘4 and 6 divide n, so 24 divides n’", "4 and 6 share the factor 2", "use 3 and 8 (no common factor): 24 divides n"],
  ["a² + b² = c² used for any triangle", "it holds only for right-angled ones", "check it first; if true, the converse gives a right angle"],
  ["‘The road is dry, so I do not know if it rained’", "dry road means no rain (rain makes it wet)", "from not-Y you may conclude not-X"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Proofs with even/odd:** write even numbers as 2k and odd numbers as 2k + 1 to prove claims for all numbers.", "**One-way rules:** from ‘If X then Y’ you may conclude Y from X and, equally, not-X from not-Y; but you may **not** conclude X from Y.", "The words ‘only if’, ‘implies’, ‘whenever’ and ‘all … are …’ all hide an ‘if … then …’ statement.", "In a **word problem**, decide the one-way rule first, then ask whether the conclusion you want is the rule or its converse."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
