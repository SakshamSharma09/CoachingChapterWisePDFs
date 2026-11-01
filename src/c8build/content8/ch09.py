from math import isqrt
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
TR = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (6, 8, 10), (12, 16, 20), (15, 20, 25), (10, 24, 26)]
# A: hypotenuse (8)
for a, b, c in TR[:8]:
    A.append(M4(f"The legs of a right triangle are {a} cm and {b} cm. Its hypotenuse is:", f"{c} cm", [f"{c+1} cm", f"{c-1} cm", f"{a+b} cm", f"{c+2} cm"], rf"$\sqrt{{{a}^2+{b}^2}}={c}$"))
# A: missing leg (6)
for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]:
    A.append(M4(f"The hypotenuse of a right triangle is {c} cm and one leg is {a} cm. The other leg is:", f"{b} cm", [f"{b+1} cm", f"{b-1} cm", f"{c-a} cm", f"{b+2} cm"], rf"$\sqrt{{{c}^2-{a}^2}}={b}$"))
# A: is it a right triangle (6)
for a, b, c in [(6, 8, 10), (9, 12, 16), (11, 60, 61), (7, 9, 11), (14, 48, 50), (10, 11, 15)]:
    ok = a*a + b*b == c*c
    A.append(M4(f"Is a triangle with sides {a}, {b} and {c} a right triangle?", "Yes" if ok else "No", ["No" if ok else "Yes", "Only if it is isosceles", "Cannot say"], rf"${a}^2+{b}^2$ {'=' if ok else '≠'} ${c}^2$"))
# A: diagonal of square (4)
for s in [4, 7, 10, 12]:
    A.append(M4(f"The diagonal of a square of side {s} cm is:", rf"${s}\sqrt2$ cm", [rf"${2*s}$ cm", rf"${s}\sqrt3$ cm", rf"${s}$ cm"], r"Hypotenuse of isosceles right triangle"))
# A: concepts (16)
A += [
 M4("The Baudhayana–Pythagoras theorem states that in a right triangle, the square on the hypotenuse equals:", "the sum of squares on the other two sides", ["the difference of the squares", "twice the product of the legs", "the sum of the legs"], "$c^2=a^2+b^2$"),
 M4("Baudhayana's Shulba Sutra describes how to:", "construct altars using rectangles and squares", ["calculate profit", "write numbers", "measure time"], "Vedic geometry"),
 M4("The side of a square whose area is double that of a square of side $a$ is:", r"$a\sqrt2$", ["$2a$", r"$a\sqrt3$", "$a+2$"], "Diagonal of the original square"),
 M4("A Pythagorean triplet is:", "three numbers satisfying $a^2+b^2=c^2$", ["three consecutive numbers", "three numbers with $a+b=c$", "three prime numbers"], "Definition"),
 M4("The side of an isosceles right triangle is 5 cm. Its hypotenuse is:", r"$5\sqrt2$ cm", ["10 cm", r"$5\sqrt3$ cm", "7 cm"], "$\\sqrt{25+25}$"),
 M4("Which is the longest side of a right triangle?", "hypotenuse", ["base", "altitude", "median"], "Opposite the right angle"),
 M4("If $a^2+b^2<c^2$ in a triangle, the triangle is:", "obtuse-angled", ["acute-angled", "right-angled", "equilateral"], "Converse idea"),
 M4("The triplet obtained from 2, 1 using $(m^2-n^2,\\,2mn,\\,m^2+n^2)$ is:", "(3, 4, 5)", ["(2, 3, 5)", "(1, 2, 3)", "(4, 5, 6)"], "m=2, n=1"),
 M4("The triplet from $m=3$, $n=2$ is:", "(5, 12, 13)", ["(6, 8, 10)", "(3, 4, 5)", "(9, 12, 15)"], "$9-4,\\,12,\\,13$"),
 M4("Multiplying a Pythagorean triplet by a constant gives:", "another Pythagorean triplet", ["a non-triplet", "a prime triplet", "a square"], "Scaling"),
 M4("A ladder 10 m long reaches 8 m up a wall. The foot of the ladder is how far from the wall?", "6 m", ["2 m", "4 m", "8 m"], "$\\sqrt{100-64}$"),
 M4("The diagonal of a rectangle 8 cm by 15 cm is:", "17 cm", ["23 cm", "13 cm", "19 cm"], "$\\sqrt{64+225}$"),
 M4("The area of a square drawn on the hypotenuse of a right triangle with legs 6 and 8 is:", "100 cm²", ["14 cm²", "48 cm²", "196 cm²"], "$6^2+8^2$"),
 M4("Which of these is a Pythagorean triplet?", "(8, 15, 17)", ["(5, 7, 9)", "(6, 7, 10)", "(4, 6, 8)"], "$64+225=289$"),
 M4("The distance between points (0, 0) and (5, 12) is:", "13", ["17", "7", "12"], "$\\sqrt{25+144}$"),
 M4("If the diagonal of a square is 10 cm, its side is:", r"$5\sqrt2$ cm", ["5 cm", "10 cm", "20 cm"], "$d/\\sqrt2$"),
]
assert len(A) == 40, len(A)
B = [
 Q("State the Baudhayana–Pythagoras theorem.", "In a right triangle, the square on the hypotenuse equals the sum of the squares on the other two sides (2).", "2"),
 Q("Find the hypotenuse of a right triangle with legs 9 cm and 12 cm.", "$\\sqrt{81+144}=15$ cm (2).", "2"),
 Q("Write the triplet that contains 12 and 35.", "(12, 35, 37) (2).", "2"),
 Q("Is (10, 24, 26) a Pythagorean triplet? Verify.", "$100+576=676=26^2$, yes (2).", "2"),
 Q("A ladder 13 m long reaches 12 m up a wall. How far is its foot from the wall?", "5 m (2).", "2"),
 Q("Find the diagonal of a square of side 6 cm.", "$6\\sqrt2\\approx8.49$ cm (2).", "2"),
 Q("How can you construct a square double the area of a given square?", "Draw a square on its diagonal (2).", "2"),
 Q("What is the converse of the theorem?", "If $a^2+b^2=c^2$ in a triangle then it is right-angled with hypotenuse $c$ (2).", "2"),
 Q("Find the area of a right triangle with hypotenuse 17 cm and one leg 8 cm.", "Other leg 15 cm (1); area 60 cm² (1).", "1+1"),
 Q("Name the hypotenuse in a right triangle PQR right-angled at Q.", "PR (2).", "2"),
 Q("Write two triplets in which the smallest member is even and one with smallest member odd.", "(6, 8, 10), (8, 15, 17); (5, 12, 13) (2).", "2"),
 Q("What does Baudhayana's rectangle-diagonal rule say?", "The diagonal of a rectangle produces an area equal to the sum of the areas produced by its length and breadth (2).", "2"),
 Q("Is the triangle with sides 5 cm, 6 cm and 8 cm right-angled?", "$25+36=61\\ne64$, no (2).", "2"),
 Q("The sides of a rectangle are 20 m and 21 m. Find its diagonal.", "29 m (2).", "2"),
 Q("Find the length of the diagonal of a cube face of edge 5 cm.", "$5\\sqrt2$ cm (2).", "2"),
 Q("What is the side of a square whose diagonal is 14 cm?", "$7\\sqrt2\\approx9.9$ cm (2).", "2"),
]
for a, b, c in TR[2:10]:
    C.append(Q(f"A ladder of length {c} m rests against a wall with its foot {a} m from the wall. How high up the wall does it reach?", rf"By the theorem, height $=\sqrt{{{c}^2-{a}^2}}$ (2); $={b}$ m (1).", "2+1"))
for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 12, 15), (20, 21, 29)]:
    C.append(Q(f"A rectangular park measures {a} m by {b} m. A boy walks along the diagonal instead of two sides. How much distance does he save?", f"Diagonal ${c}$ m (1.5); saved ${a+b}-{c}={a+b-c}$ m (1.5).", "1½+1½"))
for n in [3, 5, 7, 9]:
    m = (n*n - 1) // 2
    C.append(Q(f"Using $(n,\\ \\frac{{n^2-1}}2,\\ \\frac{{n^2+1}}2)$ find the triplet for $n={n}$ and verify.", f"Triplet $({n},{m},{m+1})$ (1.5); ${n*n}+{m*m}={m*m+n*n}={(m+1)**2}$ (1.5).", "1½+1½"))
C += [
 Q("A flagpole is supported by a 15 m wire fixed 9 m from its foot. Find the height at which the wire is attached.", "$\\sqrt{225-81}=12$ m (3).", "3"),
 Q("Find the perimeter of a rhombus whose diagonals are 16 cm and 30 cm.", "Side 17 cm (2); perimeter 68 cm (1).", "2+1"),
]
C += [
 Q("The sides of a triangle are 15 cm, 20 cm and 25 cm. Show it is right-angled and find its area.", "$225+400=625$ (2); area 150 cm² (1).", "2+1"),
 Q("A man walks 12 m north and then 5 m east. How far is he from the start?", "13 m (3).", "3"),
 Q("Find the length of the diagonal of a rectangle whose perimeter is 34 cm and one side is 8 cm.", "Other side 9 cm (1); diagonal $\\sqrt{145}\\approx12.04$ cm (2).", "1+2"),
 Q("Show that (2, 3, 4) is not a Pythagorean triplet while (9, 12, 15) is.", "$4+9\\ne16$ (1.5); $81+144=225$ (1.5).", "1½+1½"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) State the theorem and prove it using a square of side $a+b$ (outline). (ii) Verify for the triangle with sides 7, 24, 25.", "(i) Four congruent triangles in a square give $c^2=a^2+b^2$ (3). (ii) $49+576=625$ (2).", "3+2"),
 Q("<b>Case study:</b> A television screen has width 40 cm and height 30 cm. (i) Find its diagonal. (ii) A 50 cm rod: can it lie flat inside? (iii) What diagonal would a screen of 24 cm × 32 cm have?", "(i) 50 cm (2). (ii) Yes, exactly (1). (iii) 40 cm (2).", "2+1+2"),
 Q("(i) Find the length of the altitude of an equilateral triangle of side 10 cm. (ii) Hence find its area.", "(i) $5\\sqrt3\\approx8.66$ cm (3). (ii) $25\\sqrt3\\approx43.3$ cm² (2).", "3+2"),
 Q("(i) The sides of a right triangle are $x$, $x+7$ and $x+8$ (hypotenuse). Form an equation in $x$. (ii) Find the sides.", "(i) $x^2+(x+7)^2=(x+8)^2$ gives $x^2-2x-15=0$ (3). (ii) $x=5$: sides 5, 12, 13 (2).", "3+2"),
 Q("(i) A rectangle has area 120 cm² and one side 15 cm. Find its diagonal. (ii) Find its perimeter.", "(i) Other side 8 cm, diagonal 17 cm (3). (ii) 46 cm (2).", "3+2"),
 Q("<b>Case study:</b> A ship sails 24 km east and then 7 km north. (i) How far is it from the start? (ii) If it returns directly, how much distance is saved compared to going back the same way? (iii) State the theorem used.", "(i) 25 km (2). (ii) $31-25=6$ km (2). (iii) Pythagoras (1).", "2+2+1"),
 Q("(i) Show that a square with side equal to the diagonal of a unit square has double area. (ii) Draw/describe how to halve a square.", "(i) Diagonal $\\sqrt2$, area 2 (3). (ii) Join midpoints of the sides to get a square of half the area (2).", "3+2"),
 Q("(i) Prove that the triangle with sides 20, 99, 101 is right-angled. (ii) Find its area.", "(i) $400+9801=10201=101^2$ (3). (ii) 990 square units (2).", "3+2"),
 Q("(i) A 17 m ladder reaches a window 15 m above ground. A second window is 8 m above ground; how far must the foot be moved? (ii) In which direction?", "(i) First foot distance 8 m; second 15 m (3). (ii) Moved 7 m away from the wall (2).", "3+2"),
 Q("<b>Case study:</b> A kite string of 125 m is fully out and the kite is vertically above a point 75 m from the boy. (i) Find the height of the kite. (ii) If 25 m more string is released and the kite is at the same height, how far horizontally is the kite? (iii) Name the triplet.", "(i) 100 m (2). (ii) $\\sqrt{150^2-100^2}\\approx111.8$ m (2). (iii) (75, 100, 125) i.e. (3, 4, 5)×25 (1).", "2+2+1"),
 Q("(i) Find the height of an isosceles trapezium with parallel sides 14 cm and 24 cm and slant sides 13 cm each. (ii) Find its area.", "(i) Height $\\sqrt{13^2-5^2}=12$ cm (3). (ii) Area $\\tfrac12(14+24)\\times12=228$ cm² (2).", "3+2"),
 Q("(i) State the Shulba rule for the diagonal of a rectangle. (ii) Use it to find the diagonal of a 12 by 35 rectangle.", "(i) The diagonal's square equals the sum of squares of the sides (2). (ii) 37 (3).", "2+3"),
 Q("(i) Show that the sum of the squares of the diagonals of a rhombus equals four times the square of its side. (ii) Verify for 6 and 8.", "(i) Half diagonals form a right triangle, so $(d_1^2+d_2^2)/4=s^2$ (3). (ii) $36+64=100=4\\times25$ (2).", "3+2"),
 Q("<b>Case study:</b> A rectangular field is 48 m long and 14 m wide. (i) Find the diagonal path. (ii) Cost of laying a path along it at ₹ 40/m. (iii) Compare with walking along the two sides.", "(i) 50 m (2). (ii) ₹ 2000 (1). (iii) 62 m, saving 12 m (2).", "2+1+2"),
 Q("(i) Find the radius of a circle if a chord 24 cm is 5 cm from the centre. (ii) Explain.", "(i) $r=\\sqrt{12^2+5^2}=13$ cm (3). (ii) Perpendicular from centre bisects the chord (2).", "3+2"),
 Q("(i) State the converse of Pythagoras theorem and give an application. (ii) Check if 16, 63, 65 is a triplet.", "(i) Statement and use in checking corners of a rectangle (3). (ii) $256+3969=4225=65^2$ (2).", "3+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
