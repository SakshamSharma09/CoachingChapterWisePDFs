from cm import *
import math
META = meta(4)
mid = lambda p, q: ((p[0]+q[0])/2, (p[1]+q[1])/2)

# ---------- figures ----------
f6, _ = circle_fig({'A': 100, 'B': 200, 'C': 300, 'D': 25}, chords=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], center=None,
                   extra=text(*[v + o for v, o in zip(pt(105, 105, 52, 200), (8, 3))], "112°", sz=10))
Pp = {'A': (30, 135), 'B': (170, 135), 'C': (225, 30), 'D': (85, 30)}
O = mid(Pp['A'], Pp['C'])
f25 = gfig({**Pp, 'O': O}, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], w=255, h=165,
           off={'A': (-10, 12), 'B': (10, 12), 'C': (10, -4), 'D': (-10, -4), 'O': (10, 14)})
Tq = {'A': (125, 12), 'B': (20, 140), 'C': (230, 140)}
Tq['P'] = mid(Tq['A'], Tq['B']); Tq['Q'] = mid(Tq['A'], Tq['C'])
f17 = gfig(Tq, [('A', 'B'), ('B', 'C'), ('C', 'A'), ('P', 'Q')], w=250, h=165, off={'A': (0, -4), 'B': (-10, 12), 'C': (10, 12), 'P': (-12, 4), 'Q': (12, 4)})

# ---------- numeric verification ----------
assert 3*4 - 12 == 0 and 3**3 == 27 and 9**2 + 12**2 == 15**2
assert math.isqrt(25*8*8*9) == 120 and 17*2+16 == 50 and 180-112 == 68
assert 8 == len([p for p in range(2, 21) if all(p % q for q in range(2, p))]) and (-1)**5*(3*5-1) == -14
assert 7+4*14 == 63 and (12*150+18*145)/30 == 147 and (200*.12+300*.07)/500 == .09
assert (85+47) % 100 == 32 and 4*20 == 80 and 180/9*4 == 80
assert 10+4*7 == 38 and 999**2 == 998001 and F(7, 32).denominator == 32 and F(7, 24).denominator == 24
assert F(1, 3) < F(13, 36) < F(14, 36) < F(1, 2)
assert 3*4-2 == 4+6 == 10 and 2*10 == 20
assert F(25, 90) == F(5, 18)
assert 20+15+10+15 == 60 and F(20, 60) == F(1, 3) and F(45, 60) == F(3, 4) and F(25, 60) == F(5, 12)
assert 14+18+16+20+17+15 == 100 and 18+20+15 == 53 and 17+15 == 32 and 14+18 == 32
assert math.dist((-2, -3), (4, 5)) == 10 and mid((-2, -3), (4, 5)) == (1, 1) and math.dist((1, 1), (-2, -3)) == 5 == math.dist((1, 1), (4, 5))
assert (3*40 + 2*55)/5 == 46
assert math.isqrt(70*45*18*7) == 630 and 70 == (25+52+63)//2
A1 = (1, 0); B1 = (4, 1); C1 = (3, 4); D1 = (0, 3)
assert len({round(math.dist(a, b), 9) for a, b in ((A1, B1), (B1, C1), (C1, D1), (D1, A1))}) == 1 and math.dist(A1, C1) == math.dist(B1, D1)
assert 18+2*14 == 46 and 15*(36+28)//2 == 480 and 15*(18+46)//2 == 480
assert 30+90+210+170 == 500 and F(380, 500) == F(19, 25) and F(30, 500) == F(3, 50) and F(300, 500) == F(3, 5)
assert 0.2*50 == 10 and (200*.15+.4*50) == .2*(200+50)
assert 11*13 == 143 and 11+2 == 13 and (3*2+4)*(2+2) != 0 and (3*2+4)*(2+2) == 3*4+10*2+8
assert 22-2*10 == 2 and 10*(20+2)//2 == 110 and 22-2*7 == 8

A = [
 mc("The point (−6, −2) lies in the:", "third quadrant", ["second quadrant", "fourth quadrant", "first quadrant"], "Both coordinates are negative ⇒ third quadrant."),
 mc("The point on the y-axis which is 5 units below the origin is:", "(0, −5)", ["(−5, 0)", "(5, 0)", "(0, 5)"], "On the y-axis x = 0; below the origin means y is negative."),
 mc("The zero of the linear polynomial 3x − 12 is:", "4", ["−4", "12", "−12"], "3x − 12 = 0 ⇒ x = 4."),
 mc("Which of the following is an irrational number?", "0.1010010001… (the number of zeros keeps increasing)", ["0.101010… (10 repeating)", "0.25", "3.14"], "A non-terminating, non-repeating decimal is irrational."),
 mc("The product (x − 3)(x² + 3x + 9) is equal to:", "x³ − 27", ["x³ + 27", "x³ − 9", "(x − 3)³"], "Using (a − b)(a² + ab + b²) = a³ − b³ with a = x, b = 3."),
 mc("ABCD is a cyclic quadrilateral with ∠ABC = 112°. Then ∠ADC is:", "68°", ["112°", "98°", "78°"], "Opposite angles of a cyclic quadrilateral are supplementary: 180° − 112° = 68°.", fig=f6),
 mc("The perpendicular from the centre of a circle to a chord is 12 cm long and the chord is 18 cm long. The radius of the circle is:", "15 cm", ["21 cm", "√63 cm", "30 cm"], "Half chord = 9 cm; r² = 12² + 9² = 225 ⇒ r = 15 cm."),
 mc("An isosceles triangle has equal sides of 17 cm and base 16 cm. Its area, by Heron’s formula, is:", "120 cm²", ["136 cm²", "240 cm²", "60 cm²"], "s = 25; area = √(25 × 8 × 8 × 9) = 120 cm²."),
 mc("A card is drawn at random from cards numbered 1 to 20. The probability that it is a prime number is:", fr(2, 5), [fr(1, 2), fr(3, 10), fr(9, 20)], "Primes ≤ 20: 2, 3, 5, 7, 11, 13, 17, 19 = 8 ⇒ 8/20 = 2/5."),
 mc("If t<sub>n</sub> = (−1)<sup>n</sup>(3n − 1), then t<sub>5</sub> is:", "−14", ["14", "−16", "16"], "t₅ = (−1)⁵ × 14 = −14."),
 mc("The converse of ‘If two lines are parallel, then the corresponding angles formed by a transversal are equal’ is:", "If the corresponding angles formed by a transversal are equal, then the two lines are parallel.", ["If two lines are not parallel, then the corresponding angles are not equal.", "If the corresponding angles are not equal, the lines are parallel.", "Parallel lines have equal alternate angles."], "Swap the ‘if’ part and the ‘then’ part."),
 mc("A counterexample to ‘If a number ends in 5, then it is a multiple of 10’ is:", "15", ["10", "20", "30"], "15 ends in 5 but is not a multiple of 10."),
 mc("A class has 12 boys of average height 150 cm and 18 girls of average height 145 cm. The average height of the class is:", "147 cm", ["147.5 cm", "148 cm", "146 cm"], "(12 × 150 + 18 × 145)/30 = 4410/30 = 147 cm."),
 mc("200 mL of a drink with 12% sugar is mixed with 300 mL of a drink with 7% sugar. The percentage of sugar in the mixture is:", "9%", ["9.5%", "10%", "8.5%"], "(200 × 0.12 + 300 × 0.07)/500 = 45/500 = 9%."),
 mc("If the last step (writing down the final carry) of the addition algorithm is left out, the result for 85 + 47 would be:", "32", ["132", "122", "42"], "5 + 7 = 12 → write 2, carry 1; 8 + 4 + 1 = 13 → write 3, carry 1 (not written) ⇒ 32 instead of 132."),
 mc("In a parallelogram ABCD, ∠A : ∠B = 4 : 5. Then ∠A is:", "80°", ["100°", "72°", "90°"], "∠A + ∠B = 180° ⇒ ∠A = 4/9 × 180° = 80°."),
 mc("In △ABC, P is the midpoint of AB and PQ ∥ BC meets AC at Q. If AC = 14 cm, then CQ is:", "7 cm", ["14 cm", "3.5 cm", "10 cm"], "By the converse of the Midpoint Theorem Q is the midpoint of AC: CQ = 7 cm.", fig=f17),
 mc("Which term of the AP 7, 11, 15, … is 63?", "15th", ["14th", "16th", "13th"], "7 + (n − 1) × 4 = 63 ⇒ n − 1 = 14 ⇒ n = 15."),
 ar("The point (−3, 0) lies on the y-axis.", "A point on the y-axis has its abscissa equal to zero.", 'd', "(−3, 0) has ordinate 0, so it lies on the x-axis; A is false. R is true."),
 ar("The simple average of two group averages equals the combined average only when the two groups are of equal size.", "The combined average is the total of all the values divided by the total number of values.", 'a', "Both true: R gives the combined average formula (an + bm)/(n + m), which reduces to (a + b)/2 only when n = m."),
]
B = [
 sa("A library charges a fine of ₹10 for the first 3 days a book is overdue and ₹4 for every extra day. Find the fine for a book that is 10 days overdue.", 2, "Extra days = 10 − 3 = 7 (½)<br>Extra fine = 7 × 4 = ₹28 (1)<br>Fine = 10 + 28 = <b>₹38</b> (½)"),
 OR(sa("Without actual division, state which of " + fr(7, 24) + " and " + fr(7, 32) + " has a terminating decimal expansion. Give reasons.", 2, "24 = 2³ × 3 contains the factor 3 ⇒ 7/24 does not terminate (1). 32 = 2⁵ ⇒ <b>7/32 terminates</b> (1)"),
    sa("Find two rational numbers between " + fr(1, 3) + " and " + fr(1, 2) + ".", 2, "1/3 = 12/36 and 1/2 = 18/36 (1). Two numbers: <b>13/36 and 14/36</b> (any two correct numbers) (1)")),
 sa("Using a suitable identity, evaluate 999².", 2, "999² = (1000 − 1)² (½) = 1000² − 2(1000)(1) + 1² (1) = 1000000 − 2000 + 1 = <b>998001</b> (½)"),
 sa("Write the converse of ‘If a number is a multiple of 10, then it is a multiple of 5.’ Is the converse true? Justify.", 2, "Converse: <b>If a number is a multiple of 5, then it is a multiple of 10.</b> (1)<br>False: 15 is a multiple of 5 but not of 10. (1)"),
 sa("In the parallelogram ABCD, the diagonals meet at O. If OA = (3x − 2) cm and OC = (x + 6) cm, find x and the length of AC.", 2, "Diagonals of a parallelogram bisect each other ⇒ OA = OC: 3x − 2 = x + 6 ⇒ <b>x = 4</b> (1)<br>OA = 10 cm ⇒ <b>AC = 20 cm</b> (1)", fig=f25),
]
C = [
 sa("Show that 0.2777… (7 repeating) = " + fr(5, 18) + ".", 3, "x = 0.2777…; 10x = 2.777…, 100x = 27.777… (1)<br>100x − 10x: 90x = 25 (1)<br>x = 25/90 = <b>5/18</b> (1)"),
 OR(sa("In a survey of 60 students, the pets they keep were recorded:" + htable(["Pet", "Dog", "Cat", "Fish", "None"], ["Students", 20, 15, 10, 15]) + "A student is chosen at random. Find the probability that the student (i) keeps a dog, (ii) keeps some pet, (iii) keeps a cat or a fish.", 3, "Total = 60. (i) 20/60 = <b>1/3</b> (1) (ii) 45/60 = <b>3/4</b> (1) (iii) (15 + 10)/60 = <b>5/12</b> (1)"),
    sa("A die was thrown 100 times and the outcomes recorded:" + htable(["Outcome", 1, 2, 3, 4, 5, 6], ["Frequency", 14, 18, 16, 20, 17, 15]) + "Find the experimental probability of getting (i) an even number, (ii) a number greater than 4, (iii) a number less than 3.", 3, "Total = 100. (i) (18 + 20 + 15)/100 = <b>53/100</b> (1) (ii) (17 + 15)/100 = <b>8/25</b> (1) (iii) (14 + 18)/100 = <b>8/25</b> (1)")),
 sa("Find the distance between P(−2, −3) and Q(4, 5). Find the midpoint M of PQ and show that M is at the same distance from P and Q.", 3, "PQ = √(6² + 8²) = <b>10 units</b> (1)<br>M = ((−2 + 4)/2, (−3 + 5)/2) = <b>(1, 1)</b> (1)<br>MP = √(3² + 4²) = 5 and MQ = √(3² + 4²) = 5 ⇒ MP = MQ = ½PQ (1)"),
 sa("A white stork flew 40 km per day for 3 days and 55 km per day for 2 days. Find its average daily distance over the 5 days and explain why (40 + 55)/2 would be wrong.", 3, "Average = (3 × 40 + 2 × 55)/(3 + 2) (1) = 230/5 = <b>46 km per day</b> (1)<br>(40 + 55)/2 = 47.5 treats both speeds as equally weighted although they last for different numbers of days. (1)"),
 OR(sa("In a circle with centre O, ∠AOB = 100°. Find ∠ACB, where C is a point on the major arc, and ∠ADB, where D is a point on the minor arc.", 3, "∠ACB = ½ ∠AOB = <b>50°</b> (1½)<br>ACBD is a cyclic quadrilateral: ∠ADB = 180° − 50° = <b>130°</b> (1½)"),
    sa("Using Heron’s formula, find the area of a triangle with sides 25 cm, 52 cm and 63 cm.", 3, "s = (25 + 52 + 63)/2 = 70 cm (1)<br>Area = √[70 × 45 × 18 × 7] (1) = √396900 = <b>630 cm²</b> (1)")),
 sa("Prove that the diagonals of a parallelogram bisect each other.", 3, "Let the diagonals of parallelogram ABCD meet at E. (½)<br>In △AED and △CEB: AD = CB (opposite sides), ∠EAD = ∠ECB and ∠EDA = ∠EBC (alternate angles, AD ∥ BC) ⇒ △AED ≅ △CEB (ASA) (1½)<br>Hence EA = EC and ED = EB. <b>The diagonals bisect each other.</b> (1)"),
]
Pg = {'A': (1, 0), 'B': (4, 1), 'C': (3, 4), 'D': (0, 3)}
figD = coord_plane(Pg, xr=(-1, 6), yr=(-1, 6), u=24, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
D = [
 sa("The corners of a square flower bed are marked on a grid as A(1, 0), B(4, 1), C(3, 4) and D(0, 3).<br>(a) Plot the points and join them in order. (2 marks)<br>(b) Find the lengths of the four sides. (1½ marks)<br>(c) Find the lengths of the diagonals AC and BD and justify that ABCD is a square. (1½ marks)", 5,
    "(a) Plotting 4 points (1½), joining (½):" + figD + "(b) AB = √(3² + 1²) = √10; BC = √(1² + 3²) = √10; CD = √(3² + 1²) = √10; DA = √(1² + 3²) = √10 (1½)<br>(c) AC = √(2² + 4²) = √20; BD = √(4² + 2²) = √20 (1). All sides equal and diagonals equal ⇒ ABCD is a <b>square</b> (½)."),
 OR(sa("The seats in a hall are arranged in 15 rows. The first row has 18 seats and every next row has 2 seats more than the row before. Find the number of seats in the last row and the total number of seats. (2 + 3)", 5, "a = 18, d = 2, n = 15 (1)<br>Last row = 18 + 14 × 2 = <b>46 seats</b> (1)<br>Total = 15/2 × (18 + 46) (1½) = 15 × 32 = <b>480 seats</b> (1½)"),
    sa("A company tested 500 batteries and recorded their lifetimes:" + htable(["Life (hours)", "0 – 100", "100 – 200", "200 – 300", "300 – 400"], ["Number of batteries", 30, 90, 210, 170]) + "A battery is chosen at random. Find the probability that it lasts (i) at least 200 hours (1), (ii) less than 100 hours (1), (iii) between 100 and 300 hours (2); (iv) verify that the four class probabilities add up to 1 (1).", 5, "Total = 500. (i) (210 + 170)/500 = <b>19/25</b> (1) (ii) 30/500 = <b>3/50</b> (1) (iii) (90 + 210)/500 = <b>3/5</b> (2) (iv) (30 + 90 + 210 + 170)/500 = 1 (1)")),
 OR(sa("Prove the converse of the Midpoint Theorem: the line drawn through the midpoint of one side of a triangle, parallel to another side, bisects the third side.", 5, "In △ABC, P is the midpoint of AB and the line through P parallel to BC meets AC at Q. To prove: Q is the midpoint of AC. (1)<br>Let M be the midpoint of AC and join PM. (1)<br>By the Midpoint Theorem PM ∥ BC (1½)<br>Through P there is only one line parallel to BC, so PQ and PM coincide ⇒ Q = M (1½)<br>Hence <b>AQ = QC</b>. (½)"),
    sa("A chemist has 200 mL of a 15% acid solution. How many millilitres of a 40% acid solution must be added to obtain a 20% solution?", 5, "Let x mL of the 40% solution be added. Acid = 200 × 0.15 + 0.40x = 30 + 0.4x (1½)<br>Concentration: (30 + 0.4x)/(200 + x) = 0.20 (1½)<br>30 + 0.4x = 40 + 0.2x (1) ⇒ 0.2x = 10 ⇒ <b>x = 50 mL</b> (1)")),
 OR(sa("The product of two consecutive positive odd integers is 143. Form a quadratic expression in the smaller integer x, factorise it and find the integers.", 5, "The integers are x and x + 2: x(x + 2) = 143 ⇒ x² + 2x − 143 = 0 (1½)<br>(x + 13)(x − 11) = 0 (1½)<br>x = 11 (x = −13 rejected) (1) ⇒ the integers are <b>11 and 13</b> (1)"),
    sa("A rectangle is formed from 3 square tiles of side x units, 10 strips of size x by 1 unit and 8 unit squares. Write the total area as a polynomial, factorise it and give the dimensions of the rectangle.", 5, "Area = 3x² + 10x + 8 (1)<br>3x² + 6x + 4x + 8 (1½) = 3x(x + 2) + 4(x + 2) = (3x + 4)(x + 2) (1½)<br>Dimensions: <b>(3x + 4) units by (x + 2) units</b> (1)")),
]
E = [
 case("A shopkeeper stacks tins in a display. The bottom row has 20 tins and every row above it has 2 tins fewer than the row below. The number of tins in the n-th row from the bottom is t<sub>n</sub> = 22 − 2n.",
      [sub("How many tins are in the first row?", 1, "t₁ = 22 − 2 = <b>20</b>"),
       sub("How many tins are in the 10th row?", 1, "t₁₀ = 22 − 20 = <b>2</b>"),
       OR(sub("Find the total number of tins in the display if it has 10 rows.", 2, "Sum = 10/2 × (20 + 2) (1) = <b>110 tins</b> (1)"),
          sub("Which row has exactly 8 tins?", 2, "22 − 2n = 8 (1) ⇒ n = 7, i.e. the <b>7th row</b> (1)"))]),
 case("A triangular park has sides 15 m, 41 m and 52 m.",
      [sub("Find the semi-perimeter of the park.", 1, "s = (15 + 41 + 52)/2 = <b>54 m</b>"),
       sub("Find the area of the park using Heron’s formula.", 1, "Area = √[54 × 39 × 13 × 2] = √54756 = <b>234 m²</b>"),
       OR(sub("Find the length of the perpendicular from the opposite vertex to the longest side.", 2, "½ × 52 × h = 234 (1) ⇒ h = <b>9 m</b> (1)"),
          sub("Grass is laid on the whole park at ₹15 per m². Find the total cost.", 2, "Cost = 234 × 15 (1) = <b>₹3510</b> (1)"))]),
 case("Arjun and Riya are discussing propositions. Riya states: ‘If a number is a multiple of 6, then it is a multiple of 3.’ Arjun recalls that a famous claim of Fermat about prime numbers was later disproved by a single counterexample.",
      [sub("Is Riya’s proposition true? Give a reason.", 1, "<b>True.</b> A multiple of 6 is 6k = 3(2k), which is a multiple of 3."),
       sub("Write the converse and state whether it is true.", 1, "Converse: <b>If a number is a multiple of 3, then it is a multiple of 6.</b> It is false (counterexample: 9)."),
       OR(sub("Fermat claimed that every number of the form 2<sup>2<sup>n</sup></sup> + 1 is prime. How did Euler disprove this?", 2, "Euler showed that the number 2<sup>32</sup> + 1 (n = 5) is composite (1), a single counterexample is enough to disprove the claim (1)."),
          sub("Give a counterexample to ‘n² + n + 11 is prime for every positive integer n’.", 2, "n = 10: 10² + 10 + 11 = 121 (1) = 11 × 11, which is not prime (1)"))]),
]
import add14
A, B, C, E = add14.patch(META['set_no'], A, B, C, E)
SECTIONS = sections(A, B, C, D, E)
