from common import *

def make():
    m = Mk(405); f = frac
    fig_tan = figx.right_tri('BC = 15', 'AC = 8', 'AB = 17')
    fig_tri = figx.tri_parallel(0.5, ('A', 'B', 'C', 'D', 'E'))
    A = [
     m.mc("From the given figure, the value of cos α is", f(15, 17), [f(8, 17), f(8, 15), f(15, 8)], "cos α = BC/AB = 15/17.", fig=fig_tan),
     m.mc("In the figure DE ∥ BC, D and E are the midpoints of AB and AC. If BC = 14 cm, then DE is", "7 cm", ["14 cm", "28 cm", "3.5 cm"], "By the midpoint theorem DE = ½ BC = 7 cm.", fig=fig_tri),
     m.mc("The HCF and LCM of 24, 36 and 60 are respectively", "12, 360", ["6, 360", "12, 720", "24, 180"], "24 = 2³·3, 36 = 2²·3², 60 = 2²·3·5 ⇒ HCF = 2²·3 = 12, LCM = 2³·3²·5 = 360."),
     m.mc("The probability that a randomly chosen day of a non-leap year is in the month of April is", f(30, 365), [f(1, 12), f(31, 365), f(30, 366)], "April has 30 days ⇒ 30/365."),
     m.mc("Which of the following points CANNOT lie on the <i>y</i>-axis?", "(−3, 0)", ["(0, −3)", "(0, 0)", "(0, 7)"], "A point on the y-axis has x = 0; (−3, 0) has x ≠ 0."),
     m.mc("The value of (√5 + √2)² − 2√10 is", "7", ["7 + 4√10", "3", "5 + 2√10"], "5 + 2 + 2√10 − 2√10 = 7."),
     m.mc("The number 5 × 7 × 11 + 7 × 5 is", "composite", ["prime", "irrational", "neither prime nor composite"], "= 35(11 + 1) = 35 × 12, composite."),
     m.mc("The fares of a taxi are ₹ 30 for the first km and ₹ 12 for each additional km. The fare for 9 km is", "₹ 126", ["₹ 120", "₹ 138", "₹ 108"], "30 + 8 × 12 = 126."),
     m.mc("The pair 5<i>x</i> − 2<i>y</i> = 4 and 10<i>x</i> − 4<i>y</i> = <i>k</i> is coincident for", "k = 8", ["k = 4", "k = 2", "k ≠ 8"], "5/10 = 2/4 = 4/k ⇒ k = 8."),
     m.mc("The value of (1 + tan²θ)cos²θ is", "1", ["sin²θ", "tan²θ", "0"], "sec²θ · cos²θ = 1."),
     m.mc("The distance of the point (−6, 8) from the origin is", "10", ["14", "2", "6"], "√(36 + 64) = 10."),
     m.mc("A bag has 3 red, 5 white and 2 blue balls. One ball is drawn at random. The probability that it is not white is", f(1, 2), [f(1, 5), f(3, 10), f(2, 5)], "Not white = 5/10 = 1/2."),
     m.mc("If 2<i>x</i> + <i>y</i> = 8 and <i>x</i> − <i>y</i> = 1, then <i>x</i> + <i>y</i> equals", "5", ["3", "4", "7"], "3x = 9 ⇒ x = 3, y = 2 ⇒ x + y = 5."),
     m.mc("If the HCF of 45 and 75 is 15, then their LCM is", "225", ["150", "450", "1125"], "45 × 75/15 = 225."),
     m.mc("Two dice are thrown together. The probability that the sum is 7 is", f(1, 6), [f(1, 12), f(5, 36), f(7, 36)], "6 outcomes ⇒ 6/36 = 1/6."),
     m.mc("If tan θ = " + f(5, 12) + ", then sin θ equals", f(5, 13), [f(12, 13), f(5, 12), f(13, 5)], "Hypotenuse 13 ⇒ sin θ = 5/13."),
     m.mc("The equations <i>x</i> + 2<i>y</i> = 4 and 2<i>x</i> + 4<i>y</i> = 12 have", "no solution", ["one solution", "two solutions", "infinitely many solutions"], "1/2 = 2/4 ≠ 4/12 ⇒ parallel."),
     m.mc("The common difference of the AP in which a₁₈ − a₁₄ = 32 is", "8", ["4", "−8", "−4"], "4d = 32 ⇒ d = 8."),
     ar("Assertion (A): The mid-point of the segment joining (2, 5) and (6, 9) is (4, 7).", "Reason (R): The mid-point of (x₁, y₁) and (x₂, y₂) is ((x₁ + x₂)/2, (y₁ + y₂)/2).", 'a', "Both true; R is the formula used."),
     ar("Assertion (A): The probability of an impossible event is 0.", "Reason (R): The probability of a sure event is 1.", 'b', "Both are true, but R does not explain A."),
    ]
    for a in A[18:]:
        pass
    B = [
     OR(S("Find the HCF of 396 and 1080 using Euclid's division algorithm.", 2, "1080 = 396 × 2 + 288; 396 = 288 × 1 + 108 (1); 288 = 108 × 2 + 72; 108 = 72 × 1 + 36; 72 = 36 × 2 + 0 ⇒ HCF = 36 (1)."),
        S("Three bells toll at intervals of 9, 12 and 15 minutes. If they toll together at 8 a.m., when will they next toll together?", 2, "LCM(9, 12, 15) = 180 min (1) ⇒ 11:00 a.m. (1).")),
     S("A pole 6 m high casts a shadow 4 m long. At the same time a tower casts a shadow 50 m long. Find the height of the tower.", 2, "6/4 = h/50 (1) ⇒ h = 75 m (1)."),
     OR(S("In ΔABC, DE ∥ BC with AD = 4 cm, DB = 6 cm and AE = 6 cm. Find EC.", 2, "AD/DB = AE/EC ⇒ 4/6 = 6/EC (1) ⇒ EC = 9 cm (1)."),
        S("Two similar triangles have areas 49 cm² and 81 cm². If a side of the smaller is 14 cm, find the corresponding side of the larger.", 2, "Ratio = 7/9 (1) ⇒ 14 × 9/7 = 18 cm (1).")),
     S("A rope tied to the top of a vertical pole makes 30° with the level ground and is 24 m long. Find the height of the pole.", 2, "sin 30° = h/24 (1) ⇒ h = 12 m (1)."),
     S("Find the value of <i>y</i> if the distance between (2, <i>y</i>) and (10, −3) is 10 units.", 2, "64 + (y + 3)² = 100 (1) ⇒ y + 3 = ±6 ⇒ y = 3 or −9 (1)."),
    ]
    B = [B[0], B[1], B[2], B[3], B[4]]
    # section B must have exactly 5 items: replace distance item by choice-free item
    B = [B[0], B[1], B[2], B[3], B[4]]
    C = [
     S("Prove that 5 − 3√2 is irrational, given that √2 is irrational.", 3, "Assume 5 − 3√2 = p/q (1) ⇒ √2 = (5q − p)/(3q) rational (1), contradiction ⇒ 5 − 3√2 is irrational (1)."),
     S("Solve: 3<i>x</i> − 5<i>y</i> = −1 and <i>x</i> − <i>y</i> = −1.", 3, "x = y − 1 (1); 3y − 3 − 5y = −1 ⇒ y = −1 (1), x = −2 (1)."),
     OR(S("Find the sum of all three-digit natural numbers which are multiples of 11.", 3, "110, 121, …, 990: n = (990 − 110)/11 + 1 = 81 (1½); S = 81/2 × (110 + 990) = 44550 (1½)."),
        S("The 9th term of an AP is 0. Prove that its 29th term is twice its 19th term.", 3, "a + 8d = 0 ⇒ a = −8d (1); a₂₉ = 20d (1), a₁₉ = 10d ⇒ a₂₉ = 2a₁₉ (1).")),
     OR(S("Find the ratio in which the <i>y</i>-axis divides the line segment joining A(−4, −6) and B(10, 12). Also find the point of division.", 3, "x = 0 ⇒ (10k − 4)/(k + 1) = 0 ⇒ k = 2/5, ratio 2 : 5 (1½); y = (2 × 12 + 5 × (−6))/7 = −6/7 ⇒ (0, −6/7) (1½)."),
        S("The vertices of a triangle are (0, 0), (6, 0) and (3, 3√3). Show that it is equilateral.", 3, "Sides: 6, √(9 + 27) = 6, 6 (3) ⇒ equilateral.")),
     S("If sin θ = " + f(7, 25) + ", find the value of (1 + cos θ)(1 − cos θ)... sec θ + tan θ.", 3, "cos θ = 24/25 (1); sec θ = 25/24, tan θ = 7/24 (1); sum = 32/24 = 4/3 (1)."),
     S("A bag contains 4 red, 5 black and 6 green balls. A ball is drawn at random. Find the probability that it is (a) red (b) not green (c) red or black.", 3, "Total 15. (a) 4/15 (1). (b) 9/15 = 3/5 (1). (c) 9/15 = 3/5 (1)."),
    ]
    C[4] = S("If sin θ = " + f(7, 25) + ", find the value of sec θ + tan θ.", 3, "cos θ = 24/25 (1); sec θ = 25/24, tan θ = 7/24 (1); sum = 32/24 = 4/3 (1).")
    D = [
     S("Prove that the ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding sides.", 5, "Given ΔABC ~ ΔPQR; to prove ar(ABC)/ar(PQR) = (AB/PQ)² = (BC/QR)² = (CA/RP)² (1). Draw AM ⊥ BC, PN ⊥ QR (½). ar(ABC)/ar(PQR) = (½·BC·AM)/(½·QR·PN) = (BC·AM)/(QR·PN) (1). ΔAMB ~ ΔPNQ (AA) ⇒ AM/PN = AB/PQ (1). Also AB/PQ = BC/QR ⇒ ratio = (BC/QR)·(AB/PQ) = (AB/PQ)² (1). Similarly equal to the other ratios (½)."),
     OR(S("A fraction becomes 9/11 if 2 is added to both numerator and denominator, and 5/6 if 3 is added to both. Find the fraction.", 5, "(x + 2)/(y + 2) = 9/11 ⇒ 11x − 9y = −4 (1½); (x + 3)/(y + 3) = 5/6 ⇒ 6x − 5y = −3 (1½). Solve: x = 7, y = 9 (1½). Fraction 7/9 (½)."),
        S("Draw the graphs of 2<i>x</i> + <i>y</i> = 6 and 2<i>x</i> − <i>y</i> = 2 and find the area of the triangle formed with the <i>y</i>-axis.", 5, "Tables (2); graph (1); solution (2, 2) (1); y-intercepts 6 and −2 ⇒ base 8, height 2 ⇒ area 8 sq. units (1).")),
     S("From the top of a 75 m high lighthouse the angles of depression of two ships on opposite sides are 30° and 45°. Find the distance between the ships. (Take √3 = 1.732)", 5, "Distances: 75/tan 30° = 75√3 (2); 75/tan 45° = 75 (2). Total = 75(√3 + 1) = 75 × 2.732 = 204.9 m (1)."),
     OR(S("Prove that " + f("sin θ − 2 sin³θ", "2 cos³θ − cos θ") + " = tan θ.", 5, "LHS = sin θ(1 − 2sin²θ)/[cos θ(2cos²θ − 1)] (2); 1 − 2sin²θ = 2cos²θ − 1 (2) ⇒ tan θ (1)."),
        S("If sin(A − B) = ½ and cos(A + B) = ½, 0° < A + B ≤ 90°, A > B, find A and B.", 5, "A − B = 30° (1½), A + B = 60° (1½) ⇒ A = 45°, B = 15° (2).")),
    ]
    E = [
     case("A cricket academy holds a prize draw. 40 tickets numbered 1 to 40 are placed in a drum and one is drawn at random.",
          [sub("Find the probability that the number is a multiple of 5.", 1, "8/40 = 1/5 (1)."),
           sub("Find the probability that the number is a perfect square.", 1, "1, 4, 9, 16, 25, 36 ⇒ 6/40 = 3/20 (1)."),
           OR(sub("Find the probability that the number is prime and odd.", 2, "Primes ≤ 40: 12; odd ones: 11 ⇒ 11/40 (2)."),
              sub("A ticket numbered 10 is drawn and kept aside. Find the probability that the next ticket drawn is even.", 2, "39 left; evens left: 19 ⇒ 19/39 (2)."))]),
     case("A farmer plots a field on a grid in which one unit is 10 m. The corners are A(1, 2), B(7, 2), C(7, 10) and D(1, 10).",
          [sub("Find the length AB in metres.", 1, "AB = 6 units = 60 m (1)."),
           sub("Find the length of the diagonal AC in metres.", 1, "AC = √(36 + 64) = 10 units = 100 m (1)."),
           OR(sub("Find the coordinates of the point where the diagonals meet.", 2, "Midpoint of AC = (4, 6) (2)."),
              sub("A well is at the point P on AC with AP : PC = 3 : 2. Find P.", 2, "P = ((3×7 + 2×1)/5, (3×10 + 2×2)/5) = (23/5, 34/5) (2)."))]),
     case("A cinema hall has 20 rows of seats. The first row has 15 seats and each next row has 2 more seats than the row before it.",
          [sub("Write the first term and common difference of the AP.", 1, "a = 15, d = 2 (1)."),
           sub("How many seats are in the 10th row?", 1, "15 + 9 × 2 = 33 (1)."),
           OR(sub("Find the total seats in the hall.", 2, "S₂₀ = 10(30 + 38) = 680 (2)."),
              sub("Which row has 45 seats?", 2, "15 + 2(n − 1) = 45 ⇒ n = 16 (2)."))]),
    ]
    return assemble(5, A, B, C, D, E)
