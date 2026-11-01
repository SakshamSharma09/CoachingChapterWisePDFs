from common import *
import math

def make():
    m = Mk(203); f = frac
    fig_tan = figx.right_tri('BC = 24', 'AC = 7', 'AB = ?')
    fig_tri = figx.tri_parallel(0.5, ('A', 'B', 'C', 'D', 'E'), notes=[('A', 'D', 'x + 3', -28, 0), ('D', 'B', '3x + 19', -34, 0), ('A', 'E', 'x', 20, 0), ('E', 'C', '3x + 4', 30, 0)])
    # building with flagpole
    g = 170
    fig_flag = figs.svg(260, 200, figs.line(10, g, 250, g, w=1.2) + figs.line(180, g, 180, 70, w=4) + figs.line(180, 70, 180, 22, '#c00', 3)
                        + figs.line(30, g, 180, 70, '#0f2347', 1.1) + figs.line(30, g, 180, 22, '#0f2347', 1.1)
                        + figs.text(30, g+14, 'P') + figs.text(188, g+14, 'Q') + figs.text(188, 74, 'B', 'start') + figs.text(188, 20, 'C', 'start')
                        + figs.text(66, g-4, '45°', 'middle', 11, '#c00') + figs.text(92, g-14, '60°', 'middle', 11, '#c00') + figs.text(105, g+14, '40 m', 'middle', 11))
    A = [
     m.mc("The value of tan α from the given figure is", f(7, 24), [f(24, 7), f(7, 25), f(24, 25)], "tan α = AC/BC = 7/24.", fig=fig_tan),
     m.mc("ΔABC ~ ΔPQR. The perimeters of the two triangles are 30 cm and 45 cm. If AB = 12 cm, then PQ is", "18 cm", ["8 cm", "16 cm", "27 cm"], "Ratio of corresponding sides = ratio of perimeters = 2/3 ⇒ PQ = 12 × 3/2 = 18 cm."),
     m.mc("The HCF and LCM of 8, 9 and 25 are respectively", "1, 1800", ["1, 200", "3, 1800", "1, 900"], "The numbers are pairwise co-prime ⇒ HCF = 1, LCM = 8 × 9 × 25 = 1800."),
     m.mc("Two cousins were both born in February 2024. The probability that they have the same birthday is", f(1, 29), [f(1, 28), f(1, 366), f(2, 29)], "2024 is a leap year, so February has 29 days ⇒ 1/29."),
     m.mc("A point lies on the <i>y</i>-axis at a distance of 6 units from the origin. Which of the following can be its coordinates?", "(0, −6)", ["(6, 0)", "(−6, 6)", "(6, 6)"], "A point on the y-axis has x = 0; at distance 6 its y = ±6."),
     m.mc("The value of (2 + √3)² + (2 − √3)² is", "14", ["7", "8√3", "4 + 7√3"], "(7 + 4√3) + (7 − 4√3) = 14."),
     m.mc("The number 7 × 11 × 13 + 13 is", "a composite number", ["a prime number", "neither prime nor composite", "an irrational number"], "= 13(77 + 1) = 13 × 78, a product of two numbers greater than 1."),
     m.mc("Rohit reads 12 pages on the first day and 4 pages more each day than on the previous day. The number of pages he reads on the 10th day is", "48", ["44", "52", "40"], "a₁₀ = 12 + 9 × 4 = 48."),
     m.mc("The system 2<i>x</i> + 3<i>y</i> = 7 and (<i>a</i> + <i>b</i>)<i>x</i> + (2<i>a</i> − <i>b</i>)<i>y</i> = 21 has infinitely many solutions. Then <i>a</i> − <i>b</i> equals", "4", ["6", "5", "1"], "2/(a+b) = 3/(2a−b) = 7/21 ⇒ a + b = 6, 2a − b = 9 ⇒ a = 5, b = 1 ⇒ a − b = 4."),
     m.mc("Which of the following is NOT possible for an acute angle θ?", "sin θ = " + f(4, 3), ["tan θ = 5", "sec θ = 1.2", "cos θ = 0.8"], "sin θ of any angle lies between −1 and 1; 4/3 > 1."),
     m.mc("The point P(<i>x</i>, <i>y</i>) divides the line segment joining A(−2, −2) and B(2, −4) in the ratio 3 : 7 internally. Then P is", "(" + f(-4, 5) + ", " + f(-13, 5) + ")", ["(" + f(4, 5) + ", " + f(13, 5) + ")", "(" + f(-4, 5) + ", " + f(13, 5) + ")", "(" + f(-8, 5) + ", " + f(-6, 5) + ")"], "x = (3×2 + 7×(−2))/10 = −4/5; y = (3×(−4) + 7×(−2))/10 = −13/5."),
     m.mc("A 2-digit number is selected at random. The probability that it is a multiple of 3 and 5 but not of 2 is", f(1, 30), [f(1, 15), f(1, 18), f(1, 10)], "Two-digit numbers: 90. Odd multiples of 15: 15, 45, 75 ⇒ 3/90 = 1/30."),
     m.mc("The solution of 2<i>x</i> + 3<i>y</i> = 12 and <i>x</i> − 3<i>y</i> = −3 is", "x = 3, y = 2", ["x = 2, y = 3", "x = 6, y = 0", "x = 1, y = 3"], "Adding: 3x = 9 ⇒ x = 3; then y = 2."),
     m.mc("If <i>x</i> and <i>y</i> are distinct primes, the HCF of <i>x</i>⁴<i>y</i> and <i>x</i>²<i>y</i>³ is", "x²y", ["x⁴y³", "x²y³", "xy"], "Smallest power of each prime: x²y."),
     m.mc("Two dice are thrown simultaneously. The probability that the product of the two numbers is 12 is", f(1, 9), [f(1, 12), f(1, 6), f(5, 36)], "(2,6), (6,2), (3,4), (4,3) ⇒ 4/36 = 1/9."),
     m.mc("If cosec θ = " + f(13, 12) + ", then cot θ equals", f(5, 12), [f(12, 5), f(5, 13), f(13, 5)], "sin θ = 12/13 ⇒ cos θ = 5/13 ⇒ cot θ = 5/12."),
     m.mc("The pair of equations 3<i>x</i> + 2<i>y</i> = 7 and 6<i>x</i> − <i>y</i> = 9 represents two lines which are", "intersecting at exactly one point", ["parallel", "coincident", "intersecting at exactly two points"], "3/6 = 1/2 ≠ 2/(−1) ⇒ a unique solution."),
     m.mc("The common difference of the AP √2, √8, √18, … is", "√2", ["2√2", "3√2", "4√2"], "√8 = 2√2, √18 = 3√2 ⇒ d = √2."),
     ar("The points (2, 3), (4, 5) and (6, 7) are collinear.", "If PQ + QR = PR for three points P, Q and R, then the points are collinear.", 'a', "PQ = QR = 2√2, PR = 4√2 = PQ + QR ⇒ collinear; R states the test used."),
     ar("The probability of an event always lies between 0 and 1, both inclusive.", "For any event E, P(E) + P(not E) = 1.", 'b', "Both A and R are true, but R (P(E) + P(not E) = 1 with both non-negative) is not the standard explanation of the range 0 to 1 as stated in A; taken as in the sample key, R is a correct but separate statement ⇒ (b)."),
    ]
    B = [
     OR(S("Use Euclid's division algorithm to find the HCF of 255 and 867.", 2, "867 = 255×3 + 102; 255 = 102×2 + 51 (1); 102 = 51×2 + 0 ⇒ HCF = 51 (1)."),
        S("Find the smallest number which leaves remainder 2 when divided by 8, 12 and 15.", 2, "LCM(8, 12, 15) = 120 (1) ⇒ required number = 120 + 2 = 122 (1).")),
     S("A flagpole 18 m high casts a shadow 9 m long. At the same time a building 30 m high casts a shadow of what length?", 2, "Similar triangles: 18/9 = 30/s (1) ⇒ s = 15 m (1)."),
     OR(S("In ΔABC, DE ∥ BC with AD = <i>x</i> + 3, DB = 3<i>x</i> + 19, AE = <i>x</i> and EC = 3<i>x</i> + 4. Find <i>x</i>.", 2, "BPT: (x + 3)(3x + 4) = x(3x + 19) (1) ⇒ 3x² + 13x + 12 = 3x² + 19x ⇒ x = 2 (1).", fig=fig_tri),
        S("The areas of two similar triangles are 36 cm² and 100 cm². If a side of the first triangle is 9 cm, find the corresponding side of the second.", 2, "Ratio of sides = √(36/100) = 6/10 (1) ⇒ side = 9 × 10/6 = 15 cm (1).")),
     S("A kite is flying at an angle of elevation of 30° with the ground and the string attached to it is taut and 80 m long. Find the height of the kite above the ground.", 2, "sin 30° = h/80 (1) ⇒ h = 40 m (1)."),
     S("The LCM of two numbers is 1200 and their HCF is 40. If one of the numbers is 240, find the other number.", 2, "Other = (HCF × LCM)/240 = (40 × 1200)/240 (1) = 200 (1)."),
    ]
    C = [
     S("Prove that 7√5 is irrational, given that √5 is irrational.", 3, "Assume 7√5 = p/q (q ≠ 0) rational (1) ⇒ √5 = p/(7q), a rational number (1), contradicting the given fact. Hence 7√5 is irrational (1)."),
     S("Solve the pair of equations: " + f(2, "x") + " + " + f(3, "y") + " = 13; " + f(5, "x") + " − " + f(4, "y") + " = −2.", 3, "Put p = 1/x, q = 1/y: 2p + 3q = 13; 5p − 4q = −2 (1). Eliminate: 8p + 12q = 52; 15p − 12q = −6 ⇒ 23p = 46 ⇒ p = 2, q = 3 (1). x = 1/2, y = 1/3 (1)."),
     OR(S("Which term of the AP 3, 8, 13, … is 78? Also find the sum of the terms up to that term.", 3, "78 = 3 + (n − 1)5 ⇒ n = 16 (1½). S₁₆ = 16/2 (3 + 78) = 648 (1½)."),
        S("The sum of the first 7 terms of an AP is 49 and that of the first 17 terms is 289. Find the sum of the first <i>n</i> terms.", 3, "7/2 (2a + 6d) = 49 ⇒ a + 3d = 7; 17/2 (2a + 16d) = 289 ⇒ a + 8d = 17 (1½) ⇒ d = 2, a = 1. Sₙ = n/2 [2 + 2(n − 1)] = n² (1½).")),
     OR(S("Find the coordinates of the point P on the line segment joining A(−6, 10) and B(3, −8) such that P divides AB in the ratio 2 : 7.", 3, "P = ((2×3 + 7×(−6))/9, (2×(−8) + 7×10)/9) (2) = (−4, 6) (1)."),
        S("Show that A(0, −1), B(−2, 3), C(6, 7) and D(8, 3) are the vertices of a rectangle.", 3, "AB = CD = √20, BC = DA = √80 (1½); diagonals AC = BD = 10 (1). Opposite sides equal and diagonals equal ⇒ rectangle (½).")),
     S("If tan θ = " + f(3, 4) + ", find the value of " + f("sin θ − cos θ", "sin θ + cos θ") + ".", 3, "Take perpendicular 3, base 4, hypotenuse 5 (1). sin θ = 3/5, cos θ = 4/5 (1). Value = (3/5 − 4/5)/(3/5 + 4/5) = −1/7 (1)."),
     S("A box contains 90 discs numbered 1 to 90. One disc is drawn at random. Find the probability that it bears (a) a two-digit number (b) a perfect square (c) a number divisible by 5.", 3, "(a) 81/90 = 9/10 (1). (b) 1, 4, 9, 16, 25, 36, 49, 64, 81 ⇒ 9/90 = 1/10 (1). (c) 18/90 = 1/5 (1)."),
    ]
    D = [
     S("State and prove the converse of the Basic Proportionality Theorem.", 5, "Statement: if a line divides two sides of a triangle in the same ratio, it is parallel to the third side (1). Given ΔABC, DE meets AB, AC with AD/DB = AE/EC; to prove DE ∥ BC (1). Suppose not; draw DE′ ∥ BC meeting AC at E′ (1). By BPT AD/DB = AE′/E′C. So AE/EC = AE′/E′C ⇒ (AE/EC) + 1 = (AE′/E′C) + 1 ⇒ AC/EC = AC/E′C ⇒ EC = E′C (1½), so E and E′ coincide ⇒ DE ∥ BC (½)."),
     OR(S("Meena withdrew ₹ 2000 from a bank in ₹ 50 and ₹ 100 notes and received 25 notes in all. How many notes of each kind did she receive?", 5, "Let ₹50 notes = x, ₹100 notes = y: x + y = 25 (1); 50x + 100y = 2000 ⇒ x + 2y = 40 (1½). Subtract: y = 15 (1½), x = 10 (1). Check: 500 + 1500 = 2000 ✓."),
        S("Solve graphically: 3<i>x</i> + <i>y</i> = 9 and <i>x</i> − <i>y</i> = −1. Find the points where the lines meet the <i>y</i>-axis.", 5, "Tables: 3x + y = 9: (0, 9), (2, 3), (3, 0); x − y = −1: (0, 1), (2, 3), (−1, 0) (2). Graph (1½). Solution x = 2, y = 3 (1). y-axis points (0, 9) and (0, 1) (½).")),
     S("From a point on a bridge across a river, the angles of depression of the two banks, on opposite sides of the river, are 30° and 45°. If the bridge is 3 m above the water, find the width of the river. (Take √3 = 1.732)", 5, "Let the point be A, 3 m above the water, and let the banks be B and C. Horizontal distance to one bank = 3/tan 30° = 3√3 m (2); to the other = 3/tan 45° = 3 m (2). Width = 3√3 + 3 = 3(1.732 + 1) = 8.196 m (1)."),
     OR(S("Prove that " + f("cos A − sin A + 1", "cos A + sin A − 1") + " = cosec A + cot A, using the identity cosec²A = 1 + cot²A.", 5, "Divide numerator and denominator by sin A: (cotA − 1 + cosecA)/(cotA + 1 − cosecA) (1½). Write 1 = cosec²A − cot²A in the numerator: (cotA + cosecA) − (cosecA − cotA)(cosecA + cotA) = (cotA + cosecA)(1 − cosecA + cotA) (2). Cancel ⇒ cosecA + cotA (1½)."),
        S("Prove that " + f(1, "cosec θ − cot θ") + " − " + f(1, "sin θ") + " = " + f(1, "sin θ") + " − " + f(1, "cosec θ + cot θ") + ".", 5, "1/(cosecθ − cotθ) = cosecθ + cotθ (multiply by conjugate; cosec²θ − cot²θ = 1) (1½). So LHS = cosecθ + cotθ − cosecθ = cotθ (1). 1/(cosecθ + cotθ) = cosecθ − cotθ (1) ⇒ RHS = cosecθ − (cosecθ − cotθ) = cotθ (1½). LHS = RHS (1)." )),
    ]
    E = [
     case("A pottery workshop makes 12 pots on the first day. It increases production by 3 pots every day. The number of pots made on successive days forms an AP.",
          [sub("State the first term and the common difference of the AP.", 1, "a = 12, d = 3 (1)."),
           sub("Find the number of pots made on the 10th day.", 1, "a₁₀ = 12 + 9 × 3 = 39 (1)."),
           OR(sub("On which day will the workshop make 60 pots?", 2, "12 + (n − 1)3 = 60 ⇒ n − 1 = 16 ⇒ n = 17 (2)."),
              sub("Find the total number of pots made in the first 12 days.", 2, "S₁₂ = 12/2 [24 + 33] = 6 × 57 = 342 (2)."))]),
     case("Students of Class X measure the height of their school building. They stand at a point P on level ground 40 m from the foot Q of the building. The angle of elevation of the top B of the building is 45°, and the angle of elevation of the top C of the flagpole fixed on the building is 60°. (Take √3 = 1.732)",
          [sub("Find the height of the building BQ.", 1, "tan 45° = BQ/40 ⇒ BQ = 40 m (1)."),
           sub("Find the height of the point C above the ground.", 1, "tan 60° = CQ/40 ⇒ CQ = 40√3 = 69.28 m (1)."),
           OR(sub("Find the length of the flagpole BC.", 2, "BC = CQ − BQ = 40(√3 − 1) = 40 × 0.732 = 29.28 m (2)."),
              sub("Find the distance of the point P from the top C of the flagpole.", 2, "PC = √(40² + (40√3)²) = √(1600 + 4800) = 80 m (2)."))], fig=fig_flag),
     case("In a lucky-draw box there are 30 cards bearing the numbers 1 to 30. A card is drawn at random.",
          [sub("Find the probability that the number is a multiple of 6.", 1, "6, 12, 18, 24, 30 ⇒ 5/30 = 1/6 (1)."),
           sub("Find the probability that the number is a perfect cube.", 1, "1, 8, 27 ⇒ 3/30 = 1/10 (1)."),
           OR(sub("Find the probability that the number is a prime or a multiple of 10.", 2, "Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 (10); multiples of 10: 10, 20, 30 (3); no overlap ⇒ 13/30 (2)."),
              sub("The card numbered 15 is drawn and not replaced. Find the probability that the next card drawn is a multiple of 5.", 2, "29 cards remain; multiples of 5 left: 5, 10, 20, 25, 30 ⇒ 5/29 (2)."))]),
    ]
    return assemble(3, A, B, C, D, E)
