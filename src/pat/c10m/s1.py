from common import *

def make():
    m = Mk(201); f = frac
    fig_sin = figx.right_tri('BC = 8', 'AC = 15', 'AB = ?')
    fig_tw = figx.shadow_fig()
    fig_tri = figx.tri_parallel(0.5, ('P', 'Q', 'R', 'S', 'T'), notes=[('P', 'S', '6', -10, 0), ('S', 'Q', '2x + 2', -30, 0), ('P', 'T', '9', 24, 0), ('T', 'R', 'x + 13', 30, 0)])
    fig_zoxy = figx.zoxy()
    fig_grid = figx.coord_grid({'A': (6, 8), 'B': (15, 17)}, xr=(0, 17), yr=(0, 19), u=13, segs=[('A', 'B')])
    A = [
     m.mc("The value of sin α from the given figure is", f(15, 17), [f(8, 17), f(15, 8), f(8, 15)], "AB = √(8² + 15²) = 17; sin α = AC/AB = 15/17.", fig=fig_sin),
     m.mc("D and E are points on the sides AB and AC of ΔABC such that ∠ADE = ∠ACB. Then", "ΔADE ~ ΔACB", ["ΔADE ~ ΔABC", "ΔAED ~ ΔACB", "ΔAED ~ ΔABC"], "∠A common and ∠ADE = ∠ACB ⇒ ΔADE ~ ΔACB (AA), with A↔A, D↔C, E↔B."),
     m.mc("The HCF and LCM of 12, 18 and 30 are respectively", "6, 180", ["2, 360", "6, 360", "3, 180"], "12 = 2²·3, 18 = 2·3², 30 = 2·3·5. HCF = 2·3 = 6; LCM = 2²·3²·5 = 180."),
     m.mc("Arun and Bela were both born in September 2010. The probability that they have the same date of birth is", f(1, 30), [f(1, 31), f(1, 365), f(1, 60)], "September has 30 days; Bela's date matches Arun's in 1 of 30 equally likely ways."),
     m.mc("The distance of a point A from the <i>y</i>-axis is 4 units. Which of the following cannot be the coordinates of A?", "(2, 4)", ["(−4, 2)", "(4, −5)", "(4, 0)"], "Distance from y-axis = |x-coordinate| = 4 ⇒ x = ±4. (2, 4) has x = 2."),
     m.mc("The value of (3 + √5)(3 − √5) − (√2)² is", "2", ["4", "6", "7 − 2√2"], "(9 − 5) − 2 = 2."),
     m.mc("(√7)² − (2 − √3)² equals", "4√3", ["4 − 4√3", "2√3 + 1", "4√3 − 3"], "(2 − √3)² = 7 − 4√3; 7 − (7 − 4√3) = 4√3."),
     m.mc("Meera saves ₹ 200 in January and every following month she saves ₹ 25 more than the previous month. Her saving in July is", "₹ 350", ["₹ 325", "₹ 375", "₹ 400"], "a = 200, d = 25; July is the 7th month: a₇ = 200 + 6 × 25 = 350."),
     m.mc("If the system of equations (<i>a</i> − 1)<i>x</i> + 3<i>y</i> = 6 and 4<i>x</i> + 6<i>y</i> = 12 has infinitely many solutions, then <i>a</i> equals", "3", ["2", "4", "5"], "(a−1)/4 = 3/6 = 6/12 = 1/2 ⇒ a − 1 = 2 ⇒ a = 3."),
     m.mc("Which of the following is true for all values of θ for which the expressions are defined?", "cosec² θ = 1 + cot² θ", ["sin² θ = 1 + cos² θ", "sec² θ − tan² θ = 0", "tan θ = cot θ"], "cosec²θ − cot²θ = 1 is a standard identity."),
     m.mc("The point on the <i>y</i>-axis which is equidistant from A(3, 5) and B(−3, 1) is", "(0, 3)", ["(0, 2)", "(0, 4)", "(3, 0)"], "Let (0, y): 9 + (y−5)² = 9 + (y−1)² ⇒ −10y + 25 = −2y + 1 ⇒ y = 3."),
     m.mc("A 2-digit number less than 50 is chosen at random. The probability that it is a multiple of 3 and 4 but not of 5 is", f(1, 10), [f(1, 5), f(1, 8), f(3, 40)], "Numbers 10–49: 40. Multiples of 12: 12, 24, 36, 48 (none divisible by 5) ⇒ 4/40 = 1/10."),
     m.mc("The solution of the pair of linear equations 3<i>x</i> + 2<i>y</i> = 16 and <i>x</i> − 2<i>y</i> = 0 is", "x = 4, y = 2", ["x = 2, y = 4", "x = 6, y = 3", "x = 3, y = 4"], "Adding: 4x = 16 ⇒ x = 4; y = x/2 = 2."),
     m.mc("If <i>a</i> and <i>b</i> are two different prime numbers, the HCF of <i>a</i>³<i>b</i>² and <i>a</i>²<i>b</i>⁵ is", "a²b²", ["a³b⁵", "a²b⁵", "ab"], "HCF takes the smallest power of each prime: a²b²."),
     m.mc("Two dice are thrown together. The probability that the sum of the numbers is a prime number is", f(5, 12), [f(1, 3), f(7, 12), f(11, 36)], "Prime sums 2, 3, 5, 7, 11 occur 1 + 2 + 4 + 6 + 2 = 15 times out of 36 ⇒ 5/12."),
     m.mc("If tan θ = " + f(8, 15) + ", then cos θ equals", f(15, 17), [f(8, 17), f(17, 15), f(15, 8)], "Take perpendicular 8, base 15 ⇒ hypotenuse 17; cos θ = 15/17."),
     m.mc("The pair of linear equations 2<i>x</i> − 5<i>y</i> = 3 and 4<i>x</i> − 10<i>y</i> = 7 represents two lines which are", "parallel", ["coincident", "intersecting at exactly one point", "intersecting at exactly two points"], "2/4 = −5/−10 ≠ 3/7 ⇒ no solution ⇒ parallel lines."),
     m.mc("The common difference of the AP √12, √27, √48, … is", "√3", ["2√3", "3√3", "5√3"], "√12 = 2√3, √27 = 3√3, √48 = 4√3 ⇒ d = √3."),
     ar("The points (1, 1), (−1, −1) and (−√3, √3) are the vertices of an equilateral triangle.", "If three points P, Q and R are collinear, then PQ + QR = PR.", 'b', "Each side² = 8 ⇒ equilateral, so A is true. R is also true, but it does not explain A (the triangle is non-degenerate)."),
     ar("The value of sec θ can be less than 1 for an acute angle θ.", "sec θ = 1/cos θ and 0 < cos θ ≤ 1 for an acute angle θ.", 'd', "For acute θ, 0 < cos θ ≤ 1 ⇒ sec θ ≥ 1, so A is false; R is true."),
    ]
    B = [
     OR(S("Explain why 11 × 13 × 17 + 17 and 5 × 4 × 3 × 2 × 1 + 5 are composite numbers.", 2, "11×13×17 + 17 = 17(143 + 1) = 17 × 144 (1). 5×4×3×2×1 + 5 = 5(24 + 1) = 5 × 25. Each is a product of numbers greater than 1, so each is composite (1)."),
        S("Three bells toll at intervals of 8, 12 and 20 minutes. If they start tolling together, after what time will they next toll together?", 2, "Required time = LCM(8, 12, 20) (1) = 120 minutes = 2 hours (1).")),
     S("A vertical pole 5 m long casts a shadow 3 m long on the ground. At the same time a tower casts a shadow 21 m long. Find the height of the tower.", 2, "ΔABC ~ ΔPQR (both right triangles with equal sun angle) (1) ⇒ 5/3 = h/21 ⇒ h = 35 m (1).", fig=fig_tw),
     OR(S("In ΔPQR, S and T are points on PQ and PR such that ST ∥ QR. If PS = 6 cm, SQ = (2<i>x</i> + 2) cm, PT = 9 cm and TR = (<i>x</i> + 13) cm, find <i>x</i>.", 2, "BPT: PS/SQ = PT/TR (½) ⇒ 6/(2x + 2) = 9/(x + 13) ⇒ 6x + 78 = 18x + 18 (1) ⇒ x = 5 (½).", fig=fig_tri),
        S("In the figure, Z is a point on side BC of ΔABC such that XZ ∥ AB and YZ ∥ AC. If XY and CB produced meet at O, prove that ZO² = OB × OC.", 2, "XZ ∥ AB, i.e. XZ ∥ BY in ΔOBY ⇒ OZ/OB = OX/OY … (i) (½). YZ ∥ AC, i.e. ZY ∥ CX in ΔOCX ⇒ OZ/OC = OY/OX … (ii) (½). Multiplying (i) and (ii): OZ²/(OB·OC) = 1 (½) ⇒ OZ² = OB × OC (½).", fig=fig_zoxy)),
     S("From a point on the ground 24 m away from the foot of a vertical tower, the angle of elevation of the top of the tower is 30°. Find the height of the tower. (Take √3 = 1.732)", 2, "tan 30° = h/24 (1) ⇒ h = 24/√3 = 8√3 = 13.856 m (1)."),
     S("The HCF of two numbers is 9 and their LCM is 270. If one of the numbers is 54, find the other.", 2, "HCF × LCM = product of numbers (1) ⇒ other = 9 × 270 / 54 = 45 (1)."),
    ]
    C = [
     S("Prove that 3 − 2√5 is an irrational number, given that √5 is irrational.", 3, "Assume 3 − 2√5 = p/q rational (q ≠ 0) (1). Then √5 = (3 − p/q)/2 = (3q − p)/(2q) is rational (1) — contradicts the fact that √5 is irrational. Hence 3 − 2√5 is irrational (1)."),
     S("Solve the pair of linear equations: 99<i>x</i> + 101<i>y</i> = 499; 101<i>x</i> + 99<i>y</i> = 501.", 3, "Adding: 200(x + y) = 1000 ⇒ x + y = 5 (1). Subtracting: −2x + 2y = −2 ⇒ y − x = −1 (1). Hence y = 2, x = 3 (1)."),
     OR(S("How many terms of the AP 24, 21, 18, … must be taken so that the sum is 78? Explain the reason for the double answer.", 3, "S_n = n/2[48 − 3(n − 1)] = 78 ⇒ n² − 17n + 52 = 0 (1) ⇒ n = 4 or 13 (1). a₉ = 0 and the terms a₅ to a₁₃ are 12, 9, 6, 3, 0, −3, −6, −9, −12 whose sum is 0, so 13 terms give the same sum as 4 terms (1)."),
        S("The 8th term of an AP is 31 and its 15th term is 16 more than its 11th term. Find the AP and the sum of its first 11 terms.", 3, "a + 7d = 31; a + 14d = a + 10d + 16 ⇒ d = 4, a = 3 (1½). AP: 3, 7, 11, … (½). S₁₁ = 11/2 [6 + 40] = 253 (1).")),
     OR(S("Find the ratio in which the <i>x</i>-axis divides the line segment joining (3, −6) and (5, 3). Also find the point of division.", 3, "Let ratio k : 1; y = (3k − 6)/(k + 1) = 0 ⇒ k = 2 ⇒ 2 : 1 (1½). x = (2×5 + 1×3)/3 = 13/3. Point (13/3, 0) (1½)."),
        S("Show that A(3, 0), B(4, 5), C(−1, 4) and D(−2, −1) are the vertices of a rhombus.", 3, "AB = BC = CD = DA = √26 (2). Diagonals AC = √32 ≠ BD = √72, so it is a rhombus, not a square (1).")),
     S("If sec θ = " + f(13, 12) + ", evaluate " + f("2 sin θ − 3 cos θ", "4 sin θ − 9 cos θ") + ".", 3, "cos θ = 12/13, sin θ = 5/13 (1). Numerator: 10/13 − 36/13 = −26/13; Denominator: 20/13 − 108/13 = −88/13 (1). Value = 26/88 = 13/44 (1)."),
     S("Cards numbered 21 to 70 are kept in a box and one card is drawn at random. Find the probability that the number is (a) a multiple of 5 (b) a perfect square (c) a prime number less than 33.", 3, "Total 50 cards (½). (a) 25, 30, …, 70 → 10 ⇒ 1/5 (1). (b) 25, 36, 49, 64 → 4 ⇒ 2/25 (1). (c) 23, 29, 31 → 3 ⇒ 3/50 (½)."),
    ]
    D = [
     S("Prove that if a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.", 5, "Given ΔABC, DE ∥ BC; to prove AD/DB = AE/EC (1). Join BE, CD; draw DM ⊥ AC and EN ⊥ AB (1). ar(ADE)/ar(BDE) = AD/DB and ar(ADE)/ar(CDE) = AE/EC (1½). ar(BDE) = ar(CDE) (same base DE, between same parallels) (1) ⇒ AD/DB = AE/EC (½)."),
     OR(S("A fraction becomes 9/11 if 2 is added to both numerator and denominator. If 3 is added to both, it becomes 5/6. Find the fraction.", 5, "Let fraction x/y: (x + 2)/(y + 2) = 9/11 ⇒ 11x − 9y = −4 (1½); (x + 3)/(y + 3) = 5/6 ⇒ 6x − 5y = −3 (1½). Solving: x = 7, y = 9 (2). Fraction = 7/9."),
        S("Solve graphically: 2<i>x</i> + <i>y</i> = 8 and <i>x</i> − <i>y</i> = 1. From the graph also find the points where the lines meet the <i>y</i>-axis.", 5, "Table: 2x + y = 8: (0, 8), (3, 2), (4, 0); x − y = 1: (0, −1), (1, 0), (3, 2) (2). Correct graph (1½). Intersection (3, 2) ⇒ x = 3, y = 2 (1). Meets y-axis at (0, 8) and (0, −1) (½).")),
     S("The angle of elevation of the top of a building from the foot of a tower is 30° and the angle of elevation of the top of the tower from the foot of the building is 60°. If the tower is 54 m high, find the height of the building.", 5, "Let PQ = d. Tower QT = 54 m, building PB = h. tan 60° = 54/d ⇒ d = 54/√3 = 18√3 (2). tan 30° = h/d ⇒ h = 18√3/√3 = 18 m (2). Figure (1).", fig=figx.tower_building()),
     OR(S("Prove that " + f("sin θ − cos θ + 1", "sin θ + cos θ − 1") + " = " + f(1, "sec θ − tan θ") + ".", 5, "LHS: divide numerator and denominator by cos θ: (tanθ − 1 + secθ)/(tanθ + 1 − secθ) (1½). Use 1 = sec²θ − tan²θ = (secθ − tanθ)(secθ + tanθ): numerator = (secθ + tanθ) − (secθ − tanθ)(secθ + tanθ) = (secθ + tanθ)(1 − secθ + tanθ) (2). Cancel with denominator ⇒ secθ + tanθ = 1/(secθ − tanθ) (1½)."),
        S("If sin(A + B) = 1 and cos(A − B) = √3/2, 0° < A + B ≤ 90°, A > B, find A and B. Hence find (i) tan A + cot B (ii) sec A − cosec B.", 5, "A + B = 90°, A − B = 30° ⇒ A = 60°, B = 30° (2). tan 60° + cot 30° = √3 + √3 = 2√3 (1½). sec 60° − cosec 30° = 2 − 2 = 0 (1½).")),
    ]
    E = [
     case("The Class X students of a school organised a tombola at the annual fair. A box has 40 coupons numbered 1 to 40. A participant draws one coupon at random. A multiple of 7 wins a book, a perfect square wins a pen set, and every other draw wins a toffee.",
          [sub("Find the probability of winning a book.", 1, "Multiples of 7: 7, 14, 21, 28, 35 ⇒ 5/40 = 1/8 (1)."),
           sub("Find the probability that the coupon drawn is a multiple of 10.", 1, "10, 20, 30, 40 ⇒ 4/40 = 1/10 (1)."),
           OR(sub("Find the probability that the participant wins a book or a pen set.", 2, "Squares: 1, 4, 9, 16, 25, 36 (6); multiples of 7: 5; no overlap ⇒ 11/40 (2)."),
              sub("The first participant draws coupon 16 and keeps it. Find the probability that the next participant draws a perfect square.", 2, "39 coupons remain; squares left 5 (1, 4, 9, 25, 36) ⇒ 5/39 (2)."))]),
     case("The layout of a new housing society is drawn on a coordinate plane with the main gate at the origin O(0, 0). A fountain is at A(6, 8) and the community hall is at B(15, 17), joined by a straight pathway. A bench P is to be placed on AB.",
          [sub("Find the distance of the fountain A from the gate.", 1, "OA = √(36 + 64) = 10 units (1)."),
           sub("Find the coordinates of the midpoint of the pathway AB.", 1, "((6 + 15)/2, (8 + 17)/2) = (10.5, 12.5) (1)."),
           OR(sub("If the bench P divides AB internally in the ratio 1 : 2, find the coordinates of P.", 2, "P = ((1×15 + 2×6)/3, (1×17 + 2×8)/3) = (9, 11) (2)."),
              sub("Find a relation between <i>x</i> and <i>y</i> such that the point (<i>x</i>, <i>y</i>) is equidistant from A and B.", 2, "(x−6)² + (y−8)² = (x−15)² + (y−17)² ⇒ 18x + 18y = 414 ⇒ x + y = 23 (2)."))], fig=fig_grid),
     case("A stadium has seats arranged in rows. The first row has 20 seats and each next row has 4 seats more than the row in front of it. The seat numbers in the rows form an AP.",
          [sub("Find the first term <i>a</i> and common difference <i>d</i> of the AP.", 1, "a = 20, d = 4 (1)."),
           sub("Write the formula for the <i>n</i>th term of this AP.", 1, "aₙ = 20 + (n − 1) × 4 = 4n + 16 (1)."),
           OR(sub("How many seats are there in the 10th row?", 2, "a₁₀ = 20 + 9 × 4 = 56 (2)."),
              sub("Find the total number of seats in the first 15 rows.", 2, "S₁₅ = 15/2 [40 + 14 × 4] = 15/2 × 96 = 720 (2)."))]),
    ]
    return assemble(1, A, B, C, D, E)
