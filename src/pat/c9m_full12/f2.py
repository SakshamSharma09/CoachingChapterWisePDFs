from cm import *
import math
META = meta(2)

# ---------- figures ----------
f6, _ = circle_fig({'A': 215, 'B': 325}, chords=[('A', 'B')], radii=['A', 'B'], extra=text(64, 146, "35°", sz=10))
Pp25 = {'A': (40, 130), 'B': (170, 130), 'C': (210, 30), 'D': (80, 30)}
f25 = gfig(Pp25, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], w=250, h=160, off={'A': (-10, 12), 'B': (10, 12), 'C': (10, -4), 'D': (-10, -4)}, extra=text(96, 44, "105°", sz=10))
qx, qy = pt(105, 105, 50, 215)
f37, _ = circle_fig({'P': 120, 'Q': 215, 'R': 330, 'S': 40}, chords=[('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P')], center=None, extra=text(qx+8, qy+3, "100°", sz=10))

# ---------- numeric verification ----------
assert math.dist((-5, 12), (0, 0)) == 13
assert (6 + 4)/2 == 5 and (-4+6)/2 == 1 and (7-3)/2 == 2
assert 30 + 9*6 == 84 and 51**2 - 49**2 == 200 and 180-2*35 == 110
assert math.isqrt(10**2 - 8**2) == 6 and 15*5*5*5 == (25**2)*3
assert 7*5 == 35 and 4+9*5 == 49 and 5+4+3+2 == 14
assert 10**2 + 10 + 11 == 121 == 11**2
assert (12+18+15)/3 == 15 and (6*12+4*8)/10 == 10.4
assert 9+9+1 == 19 and 7+5 == 12 and (10+14+18)/2 == 21
assert (400*3+100*8)/500 == 4
assert F(26, 11) == F(234, 99) and 99*F(26, 11) == 234
assert F(3, 8) < F(13, 32) < F(14, 32) < F(1, 2)
assert F(7, 125) and 125 == 5**3
assert 30+80+70+20 == 200 and F(30, 200) == F(3, 20) and F(80, 200) == F(2, 5) and F(90, 200) == F(9, 20)
assert 7+5+8 == 20 and F(7, 20) == F(7, 20) and F(15, 20) == F(3, 4) and F(13, 20) == F(13, 20)
assert math.isqrt(10**2-8**2) == 6 and math.isqrt(10**2-6**2) == 8 and 2*8 == 16
s = 45; assert math.isqrt(45*30*9*6) == 270 and 15**2+36**2 == 39**2
P = (-3, -2); Q = (5, -2); R = (1, 4)
assert math.dist(P, R) == math.dist(Q, R) == math.sqrt(52) and 0.5*8*6 == 24
d = [i for i in range(200, 501) if i % 8 == 0 and i > 200]; assert d[0] == 208 and d[-1] == 496 and len(d) == 37 and sum(d) == 13024
assert (5+4*3, 5+11*3) == (17, 38) and 10*(10+57) == 670
assert 8*9+14*3+3 == 117 == 9*13 and 2*(9+13) == 44 and (2*3+3, 4*3+1) == (9, 13)
assert 5*12 == 60 and 5+12 == 17
assert math.dist((0, 0), (6, 8)) == 10 == math.dist((0, 0), (-6, 8)) and math.dist((-3, -4), (6, 8)) == 15
assert [i for i in range(1, 31) if 30 % i == 0] == [1, 2, 3, 5, 6, 10, 15, 30]
assert [i for i in range(1, 19) if 18 % i == 0] == [1, 2, 3, 6, 9, 18] and len(range(2, 19)) == 17
def lcm_trace(m, n):
    L = max(m, n); st = [L]
    while not (L % m == 0 and L % n == 0): L += 1; st.append(L)
    return L, st
assert lcm_trace(4, 6) == (12, [6, 7, 8, 9, 10, 11, 12])

A = [
 mc("The mirror image of the point (5, −2) in the x-axis is:", "(5, 2)", ["(−5, −2)", "(−5, 2)", "(2, −5)"], "Reflection in the x-axis changes only the sign of the y-coordinate."),
 mc("The midpoint of the segment joining A(−4, 7) and B(6, −3) is:", "(1, 2)", ["(5, 2)", "(1, 5)", "(−5, 5)"], "((−4 + 6)/2, (7 − 3)/2) = (1, 2)."),
 mc("A phone plan costs ₹199 plus ₹3 for every extra GB used. The cost (in ₹) for g extra GB is:", "199 + 3g", ["199g + 3", "202g", "3g − 199"], "Fixed charge + (rate × quantity) = 199 + 3g."),
 mc("Which of the following has a terminating decimal expansion?", fr(7, 40), [fr(5, 6), fr(4, 15), fr(9, 14)], "40 = 2³ × 5 has only the prime factors 2 and 5, so 7/40 = 0.175 terminates."),
 mc("The value of 51² − 49² is:", "200", ["100", "2", "2500"], "a² − b² = (a + b)(a − b) = (100)(2) = 200."),
 mc("In the figure, O is the centre of the circle and ∠OAB = 35°. Then ∠AOB is equal to:", "110°", ["70°", "35°", "145°"], "OA = OB (radii) ⇒ ∠OBA = 35°; ∠AOB = 180° − 35° − 35° = 110°.", fig=f6),
 mc("A chord of length 16 cm is drawn in a circle of diameter 20 cm. Its distance from the centre is:", "6 cm", ["8 cm", "2 cm", "12 cm"], "r = 10 cm; half chord = 8 cm; d² = 100 − 64 = 36 ⇒ d = 6 cm."),
 mc("The area of an equilateral triangle of side 10 cm, obtained from Heron’s formula, is:", "25√3 cm²", ["50√3 cm²", "100√3 cm²", "25 cm²"], "s = 15; area = √(15 × 5 × 5 × 5) = 25√3 cm²."),
 mc("A bag contains 5 red, 3 green and 2 blue balls. A ball is drawn at random. The probability that it is not red is:", fr(1, 2), [fr(1, 5), fr(3, 10), fr(2, 5)], "Not red = 3 + 2 = 5 balls out of 10 ⇒ 1/2."),
 mc("The n-th term of a sequence is t<sub>n</sub> = n(n − 2). Then t<sub>7</sub> is:", "35", ["49", "21", "14"], "t₇ = 7 × 5 = 35."),
 mc("In which of the following are BOTH the proposition and its converse true?", "If n is a perfect square, then n has an odd number of factors.", ["If x = y, then x² = y².", "If a number is a multiple of 8, then it is a multiple of 4.", "If two triangles have the same area, then they are congruent."], "A positive integer has an odd number of factors exactly when it is a perfect square. In the other three the converse (or the proposition) is false."),
 mc("A counterexample to the claim ‘n² + n + 11 is prime for every positive integer n’ is:", "n = 10", ["n = 1", "n = 2", "n = 3"], "For n = 10: 100 + 10 + 11 = 121 = 11², which is not prime. (n = 1, 2, 3 give 13, 17, 23.)"),
 mc("Jaspreet cycled for 5 days in each of three weeks. Her weekly averages were 12, 18 and 15 minutes. Her average for the 15 days is:", "15 minutes", ["14 minutes", "16 minutes", "45 minutes"], "All weeks have the same number of days, so the simple average (12 + 18 + 15)/3 = 15 minutes is correct."),
 mc("A goldsmith melts 6 units of gold of purity 12 varṇa with 4 units of purity 8 varṇa. The purity of the mixture is:", "10.4 varṇa", ["10 varṇa", "9.6 varṇa", "11.2 varṇa"], "(6 × 12 + 4 × 8)/(6 + 4) = 104/10 = 10.4 varṇa."),
 mc("In the digit-by-digit addition algorithm the carry can never exceed 1 because the largest possible column total is:", "9 + 9 + 1 = 19", ["9 + 9 = 18 only", "9 + 9 + 9 = 27", "10 + 10 = 20"], "Each column adds two digits (at most 9 each) and a carry of at most 1, giving at most 19, i.e. a units digit and carry 1."),
 mc("The diagonals AC and BD of a parallelogram ABCD meet at O. If AC = 14 cm and BD = 10 cm, then OA + OB is:", "12 cm", ["24 cm", "7 cm", "10 cm"], "Diagonals bisect each other: OA = 7 cm, OB = 5 cm."),
 mc("The sides of a triangle are 10 cm, 14 cm and 18 cm. The perimeter of the triangle formed by joining the midpoints of its sides is:", "21 cm", ["42 cm", "14 cm", "28 cm"], "Each side of the new triangle is half of a side of the original (Midpoint Theorem), so the perimeter is 42 ÷ 2 = 21 cm."),
 mc("The 10th term of the arithmetic progression 4, 9, 14, … is:", "49", ["54", "45", "44"], "a = 4, d = 5: t₁₀ = 4 + 9 × 5 = 49."),
 ar("0.333… (3 repeating) is a rational number.", "Every repeating decimal can be written in the form p/q, where p and q are integers and q ≠ 0.", 'a', "Both true; R explains A since 0.333… = 1/3."),
 ar("If a proposition is true, then its converse is always true.", "The proposition ‘If it rains, then the road is wet’ is true, but the road can be wet without rain.", 'd', "R is a true counterexample to A, so A is false."),
]
B = [
 sa("An e-rickshaw charges ₹30 for the first 2 km and ₹9 for every additional km. Find the fare for a journey of 8 km.", 2, "Extra distance = 8 − 2 = 6 km (½)<br>Extra charge = 6 × 9 = ₹54 (1)<br>Fare = 30 + 54 = <b>₹84</b> (½)"),
 OR(sa("Without actual division, decide whether " + fr(7, 125) + " has a terminating decimal expansion. If so, state the number of decimal places.", 2, "125 = 5³ has only the prime factor 5 ⇒ terminates (1). Number of decimal places = <b>3</b> (0.056) (1)"),
    sa("Find two rational numbers between " + fr(3, 8) + " and " + fr(1, 2) + ".", 2, "3/8 = 12/32 and 1/2 = 16/32 (1). Two numbers: <b>13/32 and 14/32</b> (any two correct numbers) (1)")),
 sa("Factorise: 16x² − 40xy + 25y².", 2, "= (4x)² − 2(4x)(5y) + (5y)² (1) = <b>(4x − 5y)²</b> (1)"),
 sa("A dairy mixes 400 litres of milk containing 3% fat with 100 litres of milk containing 8% fat. Find the percentage of fat in the mixture.", 2, "Fat = 400 × 0.03 + 100 × 0.08 = 12 + 8 = 20 litres (1)<br>Percentage = 20 ÷ 500 × 100 = <b>4%</b> (1)"),
 sa("In the parallelogram ABCD shown, ∠ADC = 105°. Find ∠DAB and ∠ABC, giving reasons.", 2, "Adjacent angles of a parallelogram are supplementary: <b>∠DAB = 180° − 105° = 75°</b> (1)<br>Opposite angles are equal: <b>∠ABC = ∠ADC = 105°</b> (1)", fig=f25),
]
C = [
 sa("Express 2.3636… (36 repeating) in the form p/q in lowest terms.", 3, "x = 2.3636…; 100x = 236.3636… (1)<br>100x − x: 99x = 234 (1)<br>x = 234/99 = <b>26/11</b> (1)"),
 OR(sa("A survey of 200 families recorded the number of children in each family:" + htable(["Children", 0, 1, 2, 3], ["Families", 30, 80, 70, 20]) + "A family is chosen at random. Find the probability that it has (i) no child, (ii) exactly one child, (iii) at least two children.", 3, "Total = 200. (i) 30/200 = <b>3/20</b> (1) (ii) 80/200 = <b>2/5</b> (1) (iii) (70 + 20)/200 = <b>9/20</b> (1)"),
    sa("A bag contains 7 red, 5 white and 8 black balls. One ball is drawn at random. Find the probability that it is (i) red, (ii) not white, (iii) white or black.", 3, "Total = 20. (i) <b>7/20</b> (1) (ii) 15/20 = <b>3/4</b> (1) (iii) (5 + 8)/20 = <b>13/20</b> (1)")),
 sa("Simplify: (a + 2b)³ − (a − 2b)³.", 3, "(a + 2b)³ = a³ + 6a²b + 12ab² + 8b³ (1)<br>(a − 2b)³ = a³ − 6a²b + 12ab² − 8b³ (1)<br>Difference = <b>12a²b + 16b³</b> (1)"),
 sa("Write the converse of the proposition ‘If a quadrilateral is a rhombus, then its diagonals are perpendicular.’ Decide whether the converse is true and give a counterexample if it is not.", 3, "Converse: <b>If the diagonals of a quadrilateral are perpendicular, then it is a rhombus.</b> (1)<br>False (1). Counterexample: a kite with unequal adjacent sides has perpendicular diagonals but is not a rhombus (1)."),
 OR(sa("A chord of length 12 cm is drawn in a circle of radius 10 cm. Find (i) its distance from the centre; (ii) the length of another chord of the same circle at a distance of 6 cm from the centre.", 3, "(i) Half chord = 6: d² = 100 − 36 = 64 ⇒ <b>d = 8 cm</b> (1½)<br>(ii) Half chord² = 100 − 36 = 64 ⇒ half chord 8 ⇒ chord = <b>16 cm</b> (1½)"),
    sa("Using Heron’s formula, find the area of a triangle with sides 15 cm, 36 cm and 39 cm.", 3, "s = (15 + 36 + 39)/2 = 45 cm (1)<br>Area = √[45 × 30 × 9 × 6] (1) = √72900 = <b>270 cm²</b> (1)")),
 sa("Write an algorithm to find the lcm of two numbers m and n by testing the numbers max(m, n), max(m, n) + 1, … in turn. Execute it for m = 4 and n = 6.", 3, "Algorithm: (1) Let L = max(m, n). (2) If both m and n divide L, report L and stop. (3) Otherwise increase L by 1 and go back to step 2. (1½)<br>For 4 and 6: L = 6, 7, 8, 9, 10, 11 fail; <b>L = 12</b> is divisible by both ⇒ lcm = 12 (1½)"),
]
Pt = {'A': (-3, -2), 'B': (5, -2), 'C': (1, 4)}
figD = coord_plane(Pt, xr=(-5, 7), yr=(-4, 6), u=20, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')])
D = [
 sa("The three corners of a triangular flag are marked on a grid as A(−3, −2), B(5, −2) and C(1, 4).<br>(a) Plot the points and join them. (2 marks)<br>(b) Find the lengths AB, BC and CA. (1½ marks)<br>(c) Name the type of triangle on the basis of its sides and find its area. (1½ marks)", 5,
    "(a) Plotting 3 points (1½), joining (½):" + figD + "(b) AB = 8; BC = √(4² + 6²) = √52; CA = √(4² + 6²) = √52 (1½)<br>(c) BC = CA ⇒ <b>isosceles triangle</b> (½). Base AB = 8 and the height from C = 4 − (−2) = 6, so area = ½ × 8 × 6 = <b>24 square units</b> (1)"),
 OR(sa("How many multiples of 8 lie between 200 and 500? Find their sum. (2½ + 2½)", 5, "Multiples: 208, 216, …, 496 — an AP with a = 208, d = 8, l = 496 (1)<br>n = (496 − 208)/8 + 1 = <b>37</b> (1½)<br>Sum = 37/2 × (208 + 496) = 37 × 352 = <b>13024</b> (2½)"),
    sa("The 5th term of an AP is 17 and its 12th term is 38. Find the AP and the sum of its first 20 terms. (2 + 3)", 5, "a + 4d = 17 and a + 11d = 38 ⇒ 7d = 21 ⇒ d = 3, a = 5 (1½): AP: 5, 8, 11, … (½)<br>S₂₀ = 20/2 × [2(5) + 19(3)] (1½) = 10 × 67 = <b>670</b> (1½)")),
 OR(sa("Prove that if the diagonals of a quadrilateral bisect each other, then it is a parallelogram.", 5, "Let diagonals AC and BD of quadrilateral ABCD meet at E with EA = EC and EB = ED. (1)<br>In △AEB and △CED: EA = EC, EB = ED, ∠AEB = ∠CED (vertically opposite) ⇒ △AEB ≅ △CED (SAS) ⇒ ∠ABE = ∠CDE (1½)<br>These are alternate angles for AB and DC with transversal BD, so AB ∥ DC (½)<br>Similarly △AED ≅ △CEB (SAS) ⇒ ∠ADE = ∠CBE ⇒ AD ∥ BC (1½)<br>Both pairs of opposite sides are parallel ⇒ <b>ABCD is a parallelogram</b>. (½)"),
    sa("State and prove the converse of the Baudhāyana–Pythagoras theorem: if a² + b² = c² for the sides of a triangle, then it is right-angled.", 5, "Statement: in △ABC with BC = a, CA = b, AB = c, if a² + b² = c², then ∠C = 90°. (1)<br>Construct a right triangle XYZ with ∠Z = 90°, YZ = a and XZ = b (1)<br>By the Pythagoras theorem XY² = a² + b² = c² ⇒ XY = c (1½)<br>Now △ABC and △XYZ have BC = YZ, CA = ZX and AB = XY ⇒ △ABC ≅ △XYZ (SSS) (1)<br>Hence ∠C = ∠Z = 90°: <b>△ABC is right-angled</b>. (½)")),
 OR(sa("The area of a rectangular carpet is (8x² + 14x + 3) m² and its breadth is (2x + 3) m. Factorise the expression to find its length. If x = 3, find the perimeter of the carpet.", 5, "8x² + 14x + 3 = 8x² + 2x + 12x + 3 (1½) = 2x(4x + 1) + 3(4x + 1) = (2x + 3)(4x + 1) (1)<br>Length = <b>(4x + 1) m</b> (1)<br>For x = 3: breadth 9 m, length 13 m ⇒ perimeter = 2(9 + 13) = <b>44 m</b> (1½)"),
    sa("The sum of the length and breadth of a rectangular notice-board is 17 dm and its area is 60 dm². Form a quadratic expression in the breadth x, factorise it and find the length and breadth.", 5, "Length = (17 − x). Area: x(17 − x) = 60 ⇒ x² − 17x + 60 = 0 (1½)<br>Factorise: (x − 5)(x − 12) = 0 (1½)<br>x = 5 or 12 (1). The board is <b>12 dm by 5 dm</b> (1)")),
]
Pc = {'W': (0, 0), 'S': (6, 8), 'T': (-6, 8), 'H': (-3, -4)}
E = [
 case("A drone delivery company maps its city on a coordinate grid (1 unit = 100 m). The warehouse W is at the origin, the shop S is at (6, 8), the school T is at (−6, 8) and a house H is at (−3, −4).",
      [sub("Find the distance of the shop S from the warehouse W (in grid units).", 1, "WS = √(6² + 8²) = <b>10 units</b>"),
       sub("Find the coordinates of the midpoint of the segment ST.", 1, "((6 − 6)/2, (8 + 8)/2) = <b>(0, 8)</b>"),
       OR(sub("Show that the warehouse is at the same distance from S and T.", 2, "WS = 10 (½); WT = √((−6)² + 8²) = 10 (1) ⇒ WS = WT (½)"),
          sub("A drone flies directly from H to S. Find the distance it covers in metres.", 2, "HS = √[(6 + 3)² + (8 + 4)²] = √(81 + 144) = 15 units (1) ⇒ 15 × 100 = <b>1500 m</b> (1)"))]),
 case("Four floodlights P, Q, R and S are fixed on the boundary of a circular ground (in that order). It is known that ∠PQR = 100° and ∠QPS = 85°.",
      [sub("Find ∠PSR.", 1, "Opposite angles of a cyclic quadrilateral are supplementary: ∠PSR = 180° − 100° = <b>80°</b>"),
       sub("Find ∠QRS.", 1, "∠QRS = 180° − ∠QPS = 180° − 85° = <b>95°</b>"),
       OR(sub("If ∠QPR = 40°, find ∠QSR and state the reason.", 2, "Angles in the same segment (on chord QR) are equal (1) ⇒ <b>∠QSR = 40°</b> (1)"),
          sub("The side PS is produced to a point T. Find the exterior angle ∠RST and state the property used.", 2, "Exterior angle of a cyclic quadrilateral equals the interior opposite angle (1) ⇒ ∠RST = ∠PQR = <b>100°</b> (1). (Also ∠RST = 180° − 80° = 100°.)"))], fig=f37),
 case("In the computer lab, Kavya runs the algorithms from her book to find gcd(18, 30). The ‘divisors’ algorithm checks every j from 1 up to the number and adds j to the list when it divides the number.",
      [sub("Write the list divisors(18) produced by the algorithm.", 1, "<b>[1, 2, 3, 6, 9, 18]</b>"),
       sub("Given divisors(30) = [1, 2, 3, 5, 6, 10, 15, 30], write the list of common divisors of 18 and 30 and the gcd.", 1, "Common divisors: [1, 2, 3, 6]; the rightmost (largest) element gives <b>gcd = 6</b>."),
       OR(sub("In the final version of the algorithm (start with 1 and check each k from 2 to min(m, n)), how many values of k are checked for m = 18 and n = 30?", 2, "min(18, 30) = 18, so k = 2, 3, …, 18 (1) ⇒ <b>17 values</b> (1)"),
          sub("Explain why it is enough to check k only up to min(m, n).", 2, "A common divisor must divide both numbers, so it cannot exceed the smaller number (1). Checking beyond min(m, n) cannot find a larger common divisor, so the work is saved (1)."))]),
]
import add14
A, B, C, E = add14.patch(META['set_no'], A, B, C, E)
SECTIONS = sections(A, B, C, D, E)
