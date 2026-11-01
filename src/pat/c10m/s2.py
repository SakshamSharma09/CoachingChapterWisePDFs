from common import *

def make():
    m = Mk(202); f = frac
    fig_cos = figx.right_tri('BC = 12', 'AC = 5', 'AB = ?')
    fig_tri = figx.tri_parallel(0.5, ('A', 'B', 'C', 'D', 'E'), notes=[('A', 'D', '4x − 3', -26, 0), ('D', 'B', '3x − 1', -26, 0), ('A', 'E', '8x − 7', 28, 0), ('E', 'C', '5x − 3', 28, 0)])
    fig_trap = figs.svg(240, 150, figs.poly([(20, 120), (220, 120), (170, 30), (70, 30)]) + figs.line(20, 120, 170, 30) + figs.line(220, 120, 70, 30) + figs.dot(112, 75) + figs.text(108, 70, 'O', 'end') + figs.text(10, 130, 'D') + figs.text(230, 130, 'C') + figs.text(178, 24, 'B') + figs.text(62, 24, 'A'))
    fig_grid = figx.coord_grid({'A': (2, 3), 'B': (11, 15)}, xr=(0, 13), yr=(0, 17), u=14, segs=[('A', 'B')])
    A = [
     m.mc("The value of cos α from the given figure is", f(12, 13), [f(5, 13), f(5, 12), f(13, 12)], "AB = √(12² + 5²) = 13; cos α = BC/AB = 12/13.", fig=fig_cos),
     m.mc("In ΔABC and ΔDEF, AB/DE = BC/EF and ∠B = ∠E. Then", "ΔABC ~ ΔDEF", ["ΔABC ~ ΔEDF", "ΔABC ~ ΔFED", "ΔCBA ~ ΔDEF"], "Two sides proportional and the included angles equal ⇒ SAS similarity with A↔D, B↔E, C↔F."),
     m.mc("The HCF and LCM of 15, 20 and 25 are respectively", "5, 300", ["5, 150", "1, 300", "10, 300"], "15 = 3·5, 20 = 2²·5, 25 = 5². HCF = 5; LCM = 2²·3·5² = 300."),
     m.mc("Two friends were born in a leap year. The probability that they have the same birthday is", f(1, 366), [f(1, 365), f(1, 12), f(2, 366)], "A leap year has 366 days; the second friend's birthday matches the first in 1 of 366 ways."),
     m.mc("The distance of a point P from the <i>x</i>-axis is 5 units. Which of the following cannot be the coordinates of P?", "(5, 3)", ["(3, 5)", "(−3, −5)", "(0, 5)"], "Distance from x-axis = |y| = 5; (5, 3) has |y| = 3."),
     m.mc("The value of (4 + √3)(4 − √3) − (√5)² is", "8", ["11", "13", "18"], "(16 − 3) − 5 = 8."),
     m.mc("√8 + √18 − √50 equals", "0", ["2√2", "√26", "10√2"], "2√2 + 3√2 − 5√2 = 0."),
     m.mc("A taxi charges ₹ 40 for the first kilometre and ₹ 12 for each additional kilometre. The fare for a 10 km journey is", "₹ 148", ["₹ 160", "₹ 120", "₹ 172"], "Fares 40, 52, 64, … form an AP; a₁₀ = 40 + 9 × 12 = 148."),
     m.mc("The pair of equations <i>kx</i> + 2<i>y</i> = 7 and 3<i>x</i> + <i>y</i> = 5 has no solution when <i>k</i> equals", "6", ["2", "3", "7"], "k/3 = 2/1 ⇒ k = 6; then 2/1 ≠ 7/5, so the lines are parallel."),
     m.mc("The expression (1 − cos² θ) cosec² θ equals", "1", ["0", "sin² θ", "cosec² θ"], "(1 − cos²θ) = sin²θ; sin²θ · cosec²θ = 1."),
     m.mc("The mid-point of the line segment joining A(2<i>a</i>, 4) and B(−2, 2<i>b</i>) is (1, 2<i>a</i> + 1). Then <i>a</i> + <i>b</i> equals", "5", ["4", "6", "3"], "(2a − 2)/2 = 1 ⇒ a = 2; (4 + 2b)/2 = 2a + 1 = 5 ⇒ b = 3; a + b = 5."),
     m.mc("A 2-digit number less than 60 is selected at random. The probability that it is a multiple of 4 and 6 but not of 5 is", f(2, 25), [f(1, 10), f(1, 12), f(4, 59)], "Numbers 10–59: 50. Multiples of 12: 12, 24, 36, 48 (none divisible by 5) ⇒ 4/50 = 2/25."),
     m.mc("The solution of the pair 3<i>x</i> + 2<i>y</i> = 13 and 3<i>x</i> − 2<i>y</i> = 5 is", "x = 3, y = 2", ["x = 2, y = 3", "x = 4, y = 1", "x = 1, y = 5"], "Adding: 6x = 18 ⇒ x = 3; then y = 2."),
     m.mc("If <i>x</i> and <i>y</i> are different primes, the LCM of <i>x</i>²<i>y</i>³ and <i>x</i>³<i>y</i>² is", "x³y³", ["x²y²", "x⁵y⁵", "x³y²"], "LCM takes the greatest power of each prime."),
     m.mc("Two dice are thrown together. The probability that the difference of the numbers is 2 is", f(2, 9), [f(1, 6), f(5, 18), f(1, 9)], "Pairs (1,3), (2,4), (3,5), (4,6) and their reverses: 8 favourable out of 36 = 2/9."),
     m.mc("If sin θ = " + f(7, 25) + ", then tan θ equals", f(7, 24), [f(24, 7), f(7, 18), f(25, 24)], "cos θ = 24/25 ⇒ tan θ = 7/24."),
     m.mc("The pair of linear equations <i>x</i> + 2<i>y</i> = 4 and 3<i>x</i> + 6<i>y</i> = 12 represents two lines which are", "coincident", ["parallel", "intersecting at one point", "intersecting at two points"], "1/3 = 2/6 = 4/12 ⇒ coincident lines."),
     m.mc("The common difference of the AP " + f(1, "p") + ", " + f("1 − p", "p") + ", " + f("1 − 2p", "p") + ", … is", "−1", ["1", "p", "−p"], "d = (1 − p)/p − 1/p = −p/p = −1."),
     ar("The distance between the points (0, 0) and (−3, 4) is 5 units.", "The distance between (x₁, y₁) and (x₂, y₂) is √[(x₂ − x₁)² + (y₂ − y₁)²].", 'a', "√(9 + 16) = 5 using the distance formula."),
     ar("For every angle θ, (sin θ + cos θ)² = 1 + 2 sin θ cos θ.", "sin θ + cos θ = 1 for every angle θ.", 'c', "A is true by expanding; R is false (e.g. θ = 45°)."),
    ]
    B = [
     OR(S("Use Euclid's division algorithm to find the HCF of 96 and 404.", 2, "404 = 96×4 + 20; 96 = 20×4 + 16 (1); 20 = 16×1 + 4; 16 = 4×4 + 0 ⇒ HCF = 4 (1)."),
        S("Two traffic lights change after every 40 s and 60 s. If they change together at 8:00:00 a.m., when will they next change together?", 2, "LCM(40, 60) = 120 s (1) = 2 minutes ⇒ 8:02:00 a.m. (1).")),
     S("A girl 1.5 m tall casts a shadow 2 m long. At the same time a tree casts a shadow 12 m long. Find the height of the tree.", 2, "Similar right triangles (1): 1.5/2 = h/12 ⇒ h = 9 m (1)."),
     OR(S("In ΔABC, DE ∥ BC with AD = 4<i>x</i> − 3, DB = 3<i>x</i> − 1, AE = 8<i>x</i> − 7 and EC = 5<i>x</i> − 3. Find <i>x</i>.", 2, "BPT: (4x − 3)(5x − 3) = (3x − 1)(8x − 7) ⇒ 2x² − x − 1 = 0 (1) ⇒ x = 1 (x = −½ rejected as lengths would be negative) (1).", fig=fig_tri),
        S("In the trapezium ABCD (AB ∥ DC), the diagonals meet at O. Prove that OA/OC = OB/OD.", 2, "In ΔAOB and ΔCOD: ∠OAB = ∠OCD, ∠OBA = ∠ODC (alternate angles) ⇒ ΔAOB ~ ΔCOD (1) ⇒ OA/OC = OB/OD (1).", fig=fig_trap)),
     S("A ladder 10 m long just reaches a window 5√3 m above the ground. Find the angle the ladder makes with the ground.", 2, "sin θ = 5√3/10 = √3/2 (1) ⇒ θ = 60° (1)."),
     S("The LCM of two numbers is 2400 and their HCF is 20. If one number is 300, find the other.", 2, "Product = HCF × LCM = 20 × 2400 = 48000 (1) ⇒ other = 48000/300 = 160 (1)."),
    ]
    C = [
     S("Prove that 5 + 3√2 is irrational, given that √2 is irrational.", 3, "Suppose 5 + 3√2 = p/q, q ≠ 0, p, q integers (1) ⇒ √2 = (p − 5q)/(3q), which is rational (1). This contradicts the irrationality of √2, so 5 + 3√2 is irrational (1)."),
     S("Solve for <i>x</i> and <i>y</i>: 7<i>x</i> − 3<i>y</i> = 31; 9<i>x</i> − 5<i>y</i> = 41.", 3, "Multiply the first by 5 and the second by 3: 35x − 15y = 155; 27x − 15y = 123 (1). Subtract: 8x = 32 ⇒ x = 4 (1). Then y = (28 − 31)/3 = −1 (1)."),
     OR(S("Find the sum of all two-digit numbers divisible by 7.", 3, "14, 21, …, 98: a = 14, d = 7, l = 98 ⇒ n = 13 (1½). S = 13/2 (14 + 98) = 728 (1½)."),
        S("The sum of the first <i>n</i> terms of an AP is 3<i>n</i>² + 5<i>n</i>. Find its 20th term.", 3, "S₂₀ = 3(400) + 100 = 1300 (1); S₁₉ = 3(361) + 95 = 1178 (1); a₂₀ = 1300 − 1178 = 122 (1).")),
     OR(S("Find the point on the <i>x</i>-axis which is equidistant from (2, −5) and (−2, 9).", 3, "Let (x, 0): (x − 2)² + 25 = (x + 2)² + 81 (1½) ⇒ −8x = 56 ⇒ x = −7. Point (−7, 0) (1½)."),
        S("Find a relation between <i>x</i> and <i>y</i> such that the point P(<i>x</i>, <i>y</i>) is equidistant from A(5, 1) and B(−1, 5).", 3, "PA² = PB² ⇒ (x − 5)² + (y − 1)² = (x + 1)² + (y − 5)² (1½) ⇒ −12x + 8y = 0 ⇒ 3x = 2y (1½).")),
     S("If 7 sin² θ + 3 cos² θ = 4, show that tan θ = 1/√3.", 3, "7 sin²θ + 3(1 − sin²θ) = 4 ⇒ 4 sin²θ = 1 (1) ⇒ sin θ = ½ ⇒ θ = 30° (1) ⇒ tan θ = 1/√3 (1)."),
     S("Three coins are tossed together. Find the probability of getting (a) exactly two tails (b) at least two heads (c) no head.", 3, "Sample space of 8 outcomes (½). (a) HTT, THT, TTH ⇒ 3/8 (1). (b) HHH, HHT, HTH, THH ⇒ 4/8 = 1/2 (1). (c) TTT ⇒ 1/8 (½)."),
    ]
    D = [
     S("State and prove the Pythagoras theorem.", 5, "Statement: in a right triangle the square on the hypotenuse equals the sum of the squares on the other two sides (1). Given ΔABC right-angled at B; draw BD ⊥ AC (1). ΔADB ~ ΔABC ⇒ AB² = AD·AC; ΔBDC ~ ΔABC ⇒ BC² = DC·AC (2). Adding: AB² + BC² = AC(AD + DC) = AC² (1)."),
     OR(S("A boat goes 30 km upstream and 44 km downstream in 10 hours; it goes 40 km upstream and 55 km downstream in 13 hours. Find the speed of the stream and the speed of the boat in still water.", 5, "Let upstream speed u, downstream d: 30/u + 44/d = 10; 40/u + 55/d = 13 (1). Put p = 1/u, q = 1/d: 30p + 44q = 10, 40p + 55q = 13 (1). Solve: q = 1/11, p = 1/5 (2) ⇒ u = 5, d = 11. Boat = (11 + 5)/2 = 8 km/h; stream = (11 − 5)/2 = 3 km/h (1)."),
        S("Draw the graphs of <i>x</i> + <i>y</i> = 5 and 2<i>x</i> − <i>y</i> = 1 on the same axes. Find their point of intersection and the points where they meet the <i>y</i>-axis.", 5, "Tables: x + y = 5: (0, 5), (2, 3), (5, 0); 2x − y = 1: (0, −1), (1, 1), (2, 3) (2). Graph (1½). Intersection (2, 3) (1). y-intercepts (0, 5) and (0, −1) (½).")),
     S("From the top of a 60 m high building, the angles of depression of the top and the bottom of a tower are 30° and 60° respectively. Find the height of the tower.", 5, "Let building AB = 60 m, tower CD. Horizontal distance BD = 60/tan 60° = 20√3 m (2). Drop to top of tower: BD tan 30° = 20√3 × 1/√3 = 20 m (2). Height of tower = 60 − 20 = 40 m (1)."),
     OR(S("Prove that " + f("tan θ + sec θ − 1", "tan θ − sec θ + 1") + " = " + f("1 + sin θ", "cos θ") + ".", 5, "Use 1 = sec²θ − tan²θ: numerator = (secθ + tanθ) − (secθ − tanθ)(secθ + tanθ) = (secθ + tanθ)(1 − secθ + tanθ) (2½). So LHS = secθ + tanθ (1) = (1 + sinθ)/cosθ (1½)."),
        S("If tan(A + B) = √3 and tan(A − B) = 1/√3, 0° < A + B ≤ 90°, A > B, find A and B. Hence evaluate sin(A + B) + cos(A − B).", 5, "A + B = 60°, A − B = 30° ⇒ A = 45°, B = 15° (3). sin 60° + cos 30° = √3/2 + √3/2 = √3 (2).")),
    ]
    E = [
     case("At the sports-day lucky draw, 25 chits numbered 1 to 25 are placed in a box. A student draws one chit at random. Multiples of 4 win a badge, prime numbers win a pen, and a perfect square or a multiple of 10 wins a bonus ticket.",
          [sub("Find the probability of winning a badge.", 1, "4, 8, 12, 16, 20, 24 ⇒ 6/25 (1)."),
           sub("Find the probability that the chit drawn shows a prime number.", 1, "2, 3, 5, 7, 11, 13, 17, 19, 23 ⇒ 9/25 (1)."),
           OR(sub("Find the probability of winning a bonus ticket.", 2, "Squares: 1, 4, 9, 16, 25 (5); multiples of 10: 10, 20 (2); no overlap ⇒ 7/25 (2)."),
              sub("The first student draws chit 9 and keeps it. Find the probability that the next student draws a prime number.", 2, "24 chits remain; 9 primes ⇒ 9/24 = 3/8 (2)."))]),
     case("A treasure-hunt map of a school ground is drawn on a coordinate grid (1 unit = 10 m). The flag is at A(2, 3) and the treasure box is at B(11, 15). Teams must walk straight from A to B.",
          [sub("Find the distance AB in grid units.", 1, "AB = √(9² + 12²) = 15 units (1)."),
           sub("Find the coordinates of the midpoint of AB.", 1, "(6.5, 9) (1)."),
           OR(sub("A clue is hidden at point P on AB such that AP : PB = 1 : 2. Find the coordinates of P.", 2, "P = ((1×11 + 2×2)/3, (1×15 + 2×3)/3) = (5, 7) (2)."),
              sub("Find the point on the <i>x</i>-axis which is equidistant from A and B.", 2, "(x − 2)² + 9 = (x − 11)² + 225 ⇒ 18x = 333 ⇒ x = 37/2; point (37/2, 0) (2)."))], fig=fig_grid),
     case("Tarun is training for a 10 km run. On the first day he jogs 800 m and every day he increases the distance by 150 m. The distances covered on successive days form an AP.",
          [sub("Write the first term and the common difference.", 1, "a = 800 m, d = 150 m (1)."),
           sub("Write the expression for the distance he jogs on the <i>n</i>th day.", 1, "aₙ = 800 + (n − 1) × 150 = 650 + 150n (1)."),
           OR(sub("How many metres does he jog on the 8th day?", 2, "a₈ = 800 + 7 × 150 = 1850 m (2)."),
              sub("What is the total distance he covers in the first 10 days?", 2, "S₁₀ = 10/2 [1600 + 9 × 150] = 5 × 2950 = 14750 m (2)."))]),
    ]
    return assemble(2, A, B, C, D, E)
