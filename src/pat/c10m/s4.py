from common import *

def make():
    m = Mk(304); f = frac
    fig_tan = figx.right_tri('BC = 20', 'AC = 21', 'AB = 29')
    fig_zoxy = figx.zoxy()
    g = 170
    fig_tw = figx.tower_building()
    A = [
     m.mc("From the given figure, the value of sin α is", f(21, 29), [f(20, 29), f(21, 20), f(20, 21)], "sin α = AC/AB = 21/29.", fig=fig_tan),
     m.mc("In ΔABC, D and E are points on AB and AC with DE ∥ BC. If AD = 2 cm, AB = 6 cm and AC = 9 cm, then AE is", "3 cm", ["4 cm", "6 cm", "2 cm"], "AD/AB = AE/AC ⇒ 2/6 = AE/9 ⇒ AE = 3 cm."),
     m.mc("The HCF and LCM of 6, 72 and 120 are respectively", "6, 360", ["12, 720", "6, 720", "12, 360"], "6 = 2·3; 72 = 2³·3²; 120 = 2³·3·5 ⇒ HCF = 2·3 = 6; LCM = 2³·3²·5 = 360."),
     m.mc("A natural number is chosen at random from 1 to 60. The probability that it is a multiple of 7 is", f(2, 15), [f(7, 60), f(3, 20), f(1, 7)], "Multiples of 7 up to 60: 7, …, 56 = 8 numbers ⇒ 8/60 = 2/15."),
     m.mc("Which of the following points CANNOT lie on the line <i>x</i> + <i>y</i> = 0?", "(2, 2)", ["(0, 0)", "(3, −3)", "(−5, 5)"], "For (2, 2): 2 + 2 = 4 ≠ 0."),
     m.mc("(5 + √7)(5 − √7) equals", "18", ["32", "12", "25 − 7√7"], "25 − 7 = 18."),
     m.mc("If the HCF of 65 and 117 is expressible as 65<i>m</i> − 117, then the value of <i>m</i> is", "2", ["1", "3", "4"], "HCF = 13 ⇒ 65m = 130 ⇒ m = 2."),
     m.mc("A person saves ₹ 100 in the first month and ₹ 20 more every following month. The saving in the 8th month is", "₹ 240", ["₹ 220", "₹ 260", "₹ 200"], "a₈ = 100 + 7 × 20 = 240."),
     m.mc("For which value of <i>k</i> do 3<i>x</i> + <i>ky</i> = 9 and 6<i>x</i> + 8<i>y</i> = 18 have infinitely many solutions?", "4", ["3", "6", "8"], "3/6 = k/8 = 9/18 ⇒ k = 4."),
     m.mc("The value of sec²θ − tan²θ is", "1", ["0", "−1", "sin²θ"], "Identity sec²θ − tan²θ = 1."),
     m.mc("The point on the <i>x</i>-axis equidistant from (3, 0)... A(−2, 0) and B(6, 0)... is", "(2, 0)", ["(4, 0)", "(0, 2)", "(−2, 6)"], "Midpoint = (2, 0)."),
     m.mc("Two coins are tossed together. The probability of getting at most one head is", f(3, 4), [f(1, 4), f(1, 2), "1"], "HH excluded: TT, HT, TH ⇒ 3/4."),
     m.mc("The solution of <i>x</i> + <i>y</i> = 11 and <i>x</i> − <i>y</i> = 3 is", "x = 7, y = 4", ["x = 4, y = 7", "x = 8, y = 3", "x = 6, y = 5"], "2x = 14 ⇒ x = 7, y = 4."),
     m.mc("The LCM of two numbers is 2400 and HCF is 20. If one is 400, the other is", "120", ["60", "240", "100"], "2400 × 20/400 = 120."),
     m.mc("A die is thrown once. The probability of getting a prime number greater than 2 is", f(1, 3), [f(1, 2), f(1, 6), f(2, 3)], "3 and 5 ⇒ 2/6 = 1/3."),
     m.mc("If sin θ = " + f(3, 5) + ", then 4 tan θ − 3 cos θ... is, tan θ equals", f(3, 4), [f(4, 3), f(3, 5), f(5, 4)], "cos θ = 4/5 ⇒ tan θ = 3/4."),
     m.mc("The lines 2<i>x</i> + 3<i>y</i> = 5 and 4<i>x</i> + 6<i>y</i> = 7 are", "parallel", ["coincident", "intersecting", "perpendicular"], "2/4 = 3/6 ≠ 5/7 ⇒ no solution, parallel."),
     m.mc("The 5th term of the AP −3, −1, 1, 3, … is", "5", ["7", "4", "3"], "a₅ = −3 + 4 × 2 = 5."),
     ar("The point (−4, 0) lies on the x-axis.", "The y-coordinate of every point on the x-axis is zero.", 'a', "Both true; R explains A."),
     ar("The sum of two irrational numbers is always irrational.", "√2 and −√2 are irrational.", 'd', "A is false: √2 + (−√2) = 0 is rational. R is true ⇒ (d)."),
    ]
    A[10] = m.mc("The point on the <i>x</i>-axis equidistant from A(−2, 0) and B(6, 0) is", "(2, 0)", ["(4, 0)", "(0, 2)", "(−2, 6)"], "Midpoint of AB = (2, 0).")
    A[15] = m.mc("If sin θ = " + f(3, 5) + " for an acute angle θ, then tan θ equals", f(3, 4), [f(4, 3), f(3, 5), f(5, 4)], "cos θ = 4/5 ⇒ tan θ = 3/4.")
    B = [
     OR(S("Show that 12<sup>n</sup> cannot end with the digit 0 for any natural number <i>n</i>.", 2, "12ⁿ = 2²ⁿ · 3ⁿ has no factor 5 (1); a number ending in 0 is divisible by 5 ⇒ impossible (1)."),
        S("Two runners take 12 min and 18 min to complete a round of a park. If they start together, after how many minutes will they meet again at the start?", 2, "LCM(12, 18) = 36 (1) ⇒ 36 minutes (1).")),
     S("A girl 1.5 m tall casts a shadow 2 m long. At the same time a tree casts a shadow 12 m long. Find the height of the tree.", 2, "1.5/2 = h/12 (1) ⇒ h = 9 m (1)."),
     OR(S("In the figure, Z is on BC, X on AC and Y on AB. State why the triangle ratio AB/AC = BZ/ZC applies when AZ bisects ∠A, and find BZ if AB = 6, AC = 9 and BC = 10.", 2, "Angle bisector theorem: BZ/ZC = AB/AC = 2/3 (1) ⇒ BZ = 4 cm (1).", fig=fig_zoxy),
        S("If ΔABC ~ ΔDEF, AB = 4 cm, DE = 6 cm, EF = 9 cm and FD = 12 cm, find the perimeter of ΔABC.", 2, "Scale 4/6 = 2/3 (1); perimeter of DEF = 27 ⇒ ABC = 18 cm (1).")),
     S("A ladder 10 m long reaches a window 5√3 m above the ground. Find the angle the ladder makes with the ground.", 2, "sin θ = 5√3/10 = √3/2 (1) ⇒ θ = 60° (1)."),
     S("Find the value of <i>k</i> for which the points (<i>k</i>, 3) and (6, −2)... are 5 units apart with <i>k</i> positive: (<i>k</i>, 3) and (6, 3).", 2, "|k − 6| = 5 ⇒ k = 11 or 1 (2)."),
    ]
    B[4] = S("Find the distance between the points (2, −3) and (−4, 5).", 2, "d = √(36 + 64) = 10 (2).")
    B = B[:4] + [B[4]]
    B[3:] = [B[3], S("Find the distance between the points (2, −3) and (−4, 5).", 2, "d = √((−6)² + 8²) = √100 = 10 (2).")]
    B = [B[0], B[1], B[2], B[3] if False else S("A ladder 10 m long reaches a window 5√3 m above the ground. Find the angle the ladder makes with the ground.", 2, "sin θ = 5√3/10 = √3/2 (1) ⇒ θ = 60° (1)."), B[4]]
    C = [
     S("Prove that 3 + 2√5 is irrational, given √5 is irrational.", 3, "Assume 3 + 2√5 = p/q (1) ⇒ √5 = (p − 3q)/(2q) is rational (1), a contradiction. Hence 3 + 2√5 is irrational (1)."),
     S("Solve: 4<i>x</i> + 3<i>y</i> = 25 and 3<i>x</i> − 2<i>y</i> = 4.", 3, "×2 and ×3: 8x + 6y = 50; 9x − 6y = 12 ⇒ 17x = 62... check separately."),
     OR(S("How many terms of the AP 9, 17, 25, … must be taken so that the sum is 636?", 3, "n/2 [18 + (n − 1)8] = 636 ⇒ 4n² + 5n − 636 = 0 ⇒ n = 12 (3)."),
        S("The 4th term of an AP is 0. Prove that its 25th term is triple its 11th term.", 3, "a + 3d = 0 ⇒ a = −3d (1). a₂₅ = a + 24d = 21d (1); a₁₁ = a + 10d = 7d ⇒ a₂₅ = 3a₁₁ (1).")),
     OR(S("Find the ratio in which the point P(2, y) divides A(−2, 2) and B(3, 7). Also find y.", 3, "2 = (3k − 2)/(k + 1) ⇒ k = 4 (1½); y = (7×4 + 2)/5 = 6 (1½). Ratio 4 : 1."),
        S("Find the area of the triangle with vertices (1, −1), (−4, 6) and (−3, −5).", 3, "½|1(6+5) + (−4)(−5+1) + (−3)(−1−6)| = ½|11 + 16 + 21| = 24 sq. units (3).")),
     S("If cos θ = " + f(8, 17) + ", find the value of sin θ and tan θ.", 3, "sin θ = 15/17 (1½); tan θ = 15/8 (1½)."),
     S("Two dice are thrown together. Find the probability that the sum of the numbers is (a) 8 (b) at least 10 (c) a perfect square.", 3, "(a) 5/36 (1). (b) (4,6),(5,5),(6,4),(5,6),(6,5),(6,6) = 6/36 = 1/6 (1). (c) sums 4 (3 ways) and 9 (4 ways) ⇒ 7/36 (1)."),
    ]
    C[1] = S("Solve: 4<i>x</i> + 3<i>y</i> = 25 and 3<i>x</i> − 2<i>y</i> = 4... use the equations 5<i>x</i> + 3<i>y</i> = 21 and 2<i>x</i> − <i>y</i> = 1.", 3, "From the second y = 2x − 1 (1); 5x + 6x − 3 = 21 ⇒ x = 24/11... ")
    C[1] = S("Solve: 3<i>x</i> + 4<i>y</i> = 10 and 2<i>x</i> − 2<i>y</i> = 2.", 3, "x − y = 1 ⇒ x = y + 1 (1); 3y + 3 + 4y = 10 ⇒ y = 1 (1), x = 2 (1).")
    D = [
     S("If a line is drawn parallel to one side of a triangle to intersect the other two sides at distinct points, prove that the other two sides are divided in the same ratio.", 5, "Given ΔABC, DE ∥ BC (½); to prove AD/DB = AE/EC (½). Join BE, CD; draw EM ⊥ AB, DN ⊥ AC (1). ar(ADE)/ar(BDE) = AD/DB; ar(ADE)/ar(CED) = AE/EC (1½). ΔBDE and ΔCED on the same base DE, between same parallels ⇒ equal areas (1). Hence AD/DB = AE/EC (½)."),
     OR(S("The sum of the digits of a two-digit number is 9. Nine times the number is twice the number obtained by reversing the digits. Find the number.", 5, "x + y = 9 (1); 9(10x + y) = 2(10y + x) ⇒ 88x = 11y ⇒ y = 8x (1½) ⇒ 9x = 9, x = 1, y = 8 (1½). Number = 18 (1)."),
        S("Solve graphically: <i>x</i> + <i>y</i> = 6 and <i>x</i> − <i>y</i> = 2. Find the area of the triangle formed by the lines and the <i>x</i>-axis.", 5, "Tables (2); graph (1); solution (4, 2) (1); x-intercepts 6 and 2 ⇒ base 4, height 2 ⇒ area 4 sq. units (1).")),
     S("A man on a tower 60 m high observes two cars on the same side of the tower, in a line with its foot, at angles of depression 30° and 60°. Find the distance between the cars. (Take √3 = 1.732)", 5, "Distances from the foot: 60/tan 30° = 60√3 and 60/tan 60° = 20√3 (2+2). Difference = 40√3 = 69.28 m (1)."),
     OR(S("Prove that (sin θ + cosec θ)² + (cos θ + sec θ)² = 7 + tan²θ + cot²θ.", 5, "LHS = sin²θ + cosec²θ + 2 + cos²θ + sec²θ + 2 (2) = 1 + 4 + (1 + cot²θ) + (1 + tan²θ) (2) = 7 + tan²θ + cot²θ (1)."),
        S("If tan(A + B) = √3 and tan(A − B) = " + f(1, "√3") + ", 0° < A + B ≤ 90°, A > B, find A and B and the value of sin A cos B + cos A sin B.", 5, "A + B = 60°, A − B = 30° (2) ⇒ A = 45°, B = 15° (2). sin(A + B) = √3/2 (1).")),
    ]
    E = [
     case("A school organises a mathematics fair. In a spinner game, a pointer spins on a circle divided into 20 equal sectors numbered 1 to 20.",
          [sub("Find the probability of getting an even number.", 1, "10/20 = 1/2 (1)."),
           sub("Find the probability of getting a number divisible by 3.", 1, "3, 6, 9, 12, 15, 18 ⇒ 6/20 = 3/10 (1)."),
           OR(sub("Find the probability of getting a prime number greater than 10.", 2, "11, 13, 17, 19 ⇒ 4/20 = 1/5 (2)."),
              sub("Find the probability of getting a number that is neither a multiple of 4 nor of 5.", 2, "Multiples of 4: 5; of 5: 4; common: 20 (1) ⇒ 8 numbers ⇒ 12/20 = 3/5 (2)."))]),
     case("A village is mapped on a grid. The school S is at (2, 3), the hospital H is at (8, 11) and the market M is at (5, 7). Distances are in km.",
          [sub("Find the distance between the school and the hospital.", 1, "SH = √(36 + 64) = 10 km (1)."),
           sub("Show that the market lies at the midpoint of SH.", 1, "((2+8)/2, (3+11)/2) = (5, 7) = M (1)."),
           OR(sub("A new point P lies on SH with SP : PH = 1 : 4. Find its coordinates.", 2, "P = ((1×8 + 4×2)/5, (1×11 + 4×3)/5) = (16/5, 23/5) (2)."),
              sub("Find the point on the x-axis equidistant from S and H.", 2, "x² − 4x + 4 + 9 = x² − 16x + 64 + 121 ⇒ 12x = 172 ⇒ x = 43/3 ⇒ (43/3, 0) (2)."))]),
     case("A library arranges books on a staircase-shaped rack. The bottom shelf holds 40 books and each shelf above holds 3 fewer books than the one below. There are 12 shelves.",
          [sub("Write the first term and the common difference of the AP.", 1, "a = 40, d = −3 (1)."),
           sub("How many books are on the 12th shelf?", 1, "a₁₂ = 40 − 33 = 7 (1)."),
           OR(sub("Find the total number of books on the rack.", 2, "S₁₂ = 6(40 + 7) = 282 (2)."),
              sub("Which shelf holds 22 books?", 2, "40 − 3(n − 1) = 22 ⇒ n = 7 (2)."))]),
    ]
    return assemble(4, A, B, C, D, E)
