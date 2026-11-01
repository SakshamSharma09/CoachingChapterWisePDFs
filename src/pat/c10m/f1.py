from common import *
import math

def make():
    m = Mk(101)
    f = frac
    # ---------- figures ----------
    fig_tri = figx.tri_parallel(0.5, ('A', 'B', 'C', 'D', 'E'), notes=[('A', 'D', 'x', -10, 0), ('D', 'B', 'x − 2', -22, 0), ('A', 'E', 'x + 2', 24, 0), ('E', 'C', 'x − 1', 24, 0)])
    fig_tri2 = figx.tri_parallel(0.4, ('A', 'B', 'C', 'D', 'E'), notes=[('A', 'D', '1.5 cm', -24, 0), ('D', 'B', '3 cm', -22, 0), ('A', 'E', '1 cm', 24, 0)])
    fig_tan = figx.circle_tangents()
    fig_h30 = figx.height_dist(30)
    # square with 4 quadrants
    s = 150; o = 15
    pa = f"<rect x='{o}' y='{o}' width='{s}' height='{s}' fill='#cfd8ea' stroke='#000' stroke-width='1.4'/>"
    r = s/2
    for (cx, cy, sx, sy) in [(o, o, 1, 1), (o+s, o, -1, 1), (o+s, o+s, -1, -1), (o, o+s, 1, -1)]:
        pa += f"<path d='M {cx} {cy} L {cx+sx*r} {cy} A {r} {r} 0 0 {1 if sx*sy>0 else 0} {cx} {cy+sy*r} Z' fill='#fff' stroke='#000' stroke-width='1.2'/>"
    pa += figs.text(o-8, o-4, 'A') + figs.text(o+s+8, o-4, 'B') + figs.text(o+s+8, o+s+14, 'C') + figs.text(o-8, o+s+14, 'D')
    fig_sq = figs.svg(190, 185, pa)
    # toy: cone on hemisphere
    toy = (figs.line(110, 8, 70, 150) + figs.line(110, 8, 150, 150) + "<path d='M 70 150 A 40 40 0 0 0 150 150' fill='none' stroke='#000' stroke-width='1.4'/>" + figs.line(70, 150, 150, 150, dash='4,3')
           + figs.line(110, 8, 110, 150, '#0f2347', 1, '3,3') + "<rect x='112' y='68' width='44' height='16' fill='#fff'/>" + figs.text(114, 80, '24 cm', 'start', 11) + figs.text(90, 166, '7 cm', 'middle', 11))
    fig_toy = figs.svg(220, 200, toy)
    # tower fig for case 2
    P, Q, B = (20, 170), (140, 170), (200, 170); A_ = (200, 66)
    tw = (figs.line(10, 170, 250, 170, w=1.2) + figs.line(*B, *A_, w=3) + figs.line(*P, *A_, '#0f2347', 1.2) + figs.line(*Q, *A_, '#0f2347', 1.2)
          + figs.text(20, 188, 'P') + figs.text(140, 188, 'Q') + figs.text(205, 188, 'B') + figs.text(205, 60, 'A', 'start')
          + figs.text(60, 165, '30°', 'middle', 11, '#c00') + figs.text(152, 164, '60°', 'middle', 11, '#c00') + figs.text(80, 188, '60 m', 'middle', 11) + figs.text(215, 125, 'h', 'start', 12))
    fig_case = figs.svg(260, 200, tw)

    # ---------- SECTION A ----------
    A = [
     m.mc("If the HCF of 65 and 117 is expressible in the form 65<i>m</i> − 117, then the value of <i>m</i> is", "2", ["1", "3", "4"], "HCF(65, 117) = 13. 65m − 117 = 13 ⇒ 65m = 130 ⇒ m = 2."),
     m.mc("If one zero of the quadratic polynomial <i>x</i>² + 3<i>x</i> + <i>k</i> is 2, then the value of <i>k</i> is", "−10", ["10", "5", "−5"], "p(2) = 4 + 6 + k = 0 ⇒ k = −10."),
     m.mc("The pair of linear equations <i>x</i> + 2<i>y</i> − 5 = 0 and −3<i>x</i> − 6<i>y</i> + 15 = 0 has", "infinitely many solutions", ["a unique solution", "exactly two solutions", "no solution"], f"a₁/a₂ = b₁/b₂ = c₁/c₂ = −1/3 (coincident lines)."),
     m.mc("The values of <i>k</i> for which the equation 2<i>x</i>² + <i>kx</i> + 3 = 0 has equal roots are", "± 2√6", ["± √6", "± 24", "6, −6 only if k > 0"], "D = k² − 24 = 0 ⇒ k = ±√24 = ±2√6."),
     m.mc("Which of the following quadratic equations has two distinct real roots?", "2<i>x</i>² − 6<i>x</i> + 3 = 0", ["<i>x</i>² + <i>x</i> + 1 = 0", "<i>x</i>² − 4<i>x</i> + 4 = 0", "3<i>x</i>² + 2<i>x</i> + 1 = 0"], "D = 36 − 24 = 12 > 0 for the correct option; D = −3, 0, −8 for the others."),
     m.mc("The 10th term from the end of the AP 4, 9, 14, …, 254 is", "209", ["199", "204", "214"], "10th from end = l − 9d = 254 − 45 = 209."),
     m.mc("The <i>n</i>th term of an AP is 3<i>n</i> + 5. The sum of its first 10 terms is", "215", ["185", "230", "245"], "a = 8, d = 3; S₁₀ = 5(16 + 27) = 215."),
     m.mc("In the given figure, DE ∥ BC. If AD = <i>x</i>, DB = <i>x</i> − 2, AE = <i>x</i> + 2 and EC = <i>x</i> − 1, then the value of <i>x</i> is", "4", ["3", "5", "6"], "x/(x−2) = (x+2)/(x−1) ⇒ x² − x = x² − 4 ⇒ x = 4 (BPT).", fig=fig_tri),
     m.mc("ΔABC ~ ΔPQR and ar(ΔABC) : ar(ΔPQR) = 9 : 16. If AB = 6 cm, then PQ equals", "8 cm", ["4.5 cm", "9 cm", "10.5 cm"], "AB/PQ = √(9/16) = 3/4 ⇒ PQ = 8 cm."),
     m.mc("The point on the <i>x</i>-axis which is equidistant from (3, 2) and (−5, −2) is", "(−1, 0)", ["(1, 0)", "(0, −1)", "(−2, 0)"], "(x−3)² + 4 = (x+5)² + 4 ⇒ −6x + 9 = 10x + 25 ⇒ x = −1."),
     m.mc("If 4 tan θ = 3, then " + f("4 sin θ − cos θ", "4 sin θ + cos θ") + " equals", f(1, 2), [f(1, 3), f(2, 3), f(3, 4)], "Divide by cos θ: (4tanθ − 1)/(4tanθ + 1) = (3 − 1)/(3 + 1) = 1/2."),
     m.mc("Which of the following statements is INCORRECT?", "sec 60° = 2 cos 60°", ["sin 30° = cos 60°", "tan 45° · cot 45° = 1", "sin² 45° + cos² 45° = 1"], "sec 60° = 2 whereas 2 cos 60° = 1."),
     m.mc("The angle of elevation of the top of a tower from a point on the ground, 30 m away from its foot, is 30°. The height of the tower is", "10√3 m", ["30√3 m", "15 m", "10 m"], "h = 30 tan 30° = 30/√3 = 10√3 m.", fig=fig_h30),
     m.mc("In the figure, AP and AQ are tangents from A to a circle with centre O. If ∠PAQ = 80°, then ∠POA is", "50°", ["40°", "80°", "100°"], "∠POQ = 180° − 80° = 100°; OA bisects it ⇒ ∠POA = 50°.", fig=fig_tan),
     m.mc("The perimeter of a square of side 22 cm is equal to the circumference of a circle. The radius of the circle is", "14 cm", ["7 cm", "22 cm", "28 cm"], "2πr = 88 ⇒ r = 88 × 7/44 = 14 cm."),
     m.mc("A solid sphere of radius 3 cm is melted and recast into small spheres of radius 1 cm. The number of small spheres formed is", "27", ["9", "18", "81"], "n = (3)³/(1)³ = 27."),
     m.mc("For the distribution below, the sum of the lower limits of the median class and the modal class is<br>" + htbl(["Class", "0–10", "10–20", "20–30", "30–40", "40–50"], ["Frequency", "6", "14", "12", "18", "10"]), "50", ["40", "60", "70"], "N = 60, N/2 = 30; cf: 6, 20, 32 ⇒ median class 20–30. Highest f = 18 ⇒ modal class 30–40. 20 + 30 = 50."),
     m.mc("Two coins are tossed together. The probability of getting at most one head is", f(3, 4), [f(1, 4), f(1, 2), "1"], "Outcomes HH, HT, TH, TT; at most one head: HT, TH, TT = 3/4."),
     ar("The probability that a leap year selected at random has 53 Sundays is 2/7.", "A leap year has 52 weeks and 2 extra days; the pair of extra days can occur in 7 equally likely ways, 2 of which contain a Sunday.", 'a', "Both true; R explains A."),
     ar("The quadratic equation 2<i>x</i>² − 4<i>x</i> + 3 = 0 has two distinct real roots.", "A quadratic equation has real roots if and only if its discriminant is non-negative.", 'd', "D = 16 − 24 = −8 < 0 ⇒ A is false; R is true."),
    ]
    # ---------- SECTION B ----------
    B = [
     S("Find the HCF and LCM of 26 and 91 by the prime factorisation method. Hence verify that HCF × LCM = product of the two numbers.", 2, "26 = 2 × 13, 91 = 7 × 13 ⇒ HCF = 13, LCM = 2 × 7 × 13 = 182 (1).<br>HCF × LCM = 13 × 182 = 2366 = 26 × 91 ✓ (1)."),
     OR(S("In the figure (DE ∥ BC), AD = 1.5 cm, DB = 3 cm and AE = 1 cm. Find EC.", 2, "By BPT: AD/DB = AE/EC (1) ⇒ 1.5/3 = 1/EC ⇒ EC = 2 cm (1).", fig=fig_tri2),
        S("The diagonals of a trapezium ABCD (AB ∥ DC) intersect at O. If AB = 2 CD, find the ratio of the areas of ΔAOB and ΔCOD.", 2, "ΔAOB ~ ΔCOD (AA) (1). Ratio of areas = (AB/CD)² = 4 : 1 (1).")),
     OR(S("Two concentric circles have radii 7 cm and 25 cm. Find the length of the chord of the larger circle which touches the smaller circle.", 2, "Half-chord² = 25² − 7² = 576 (1) ⇒ half-chord = 24 ⇒ chord = 48 cm (1)."),
        S("In the figure, AP and AQ are tangents from A to a circle with centre O and ∠PAQ = 70°. Find ∠OPQ.", 2, "∠POQ = 180° − 70° = 110° (1). OP = OQ ⇒ ∠OPQ = (180° − 110°)/2 = 35° (1).", fig=fig_tan)),
     S("Find the zeros of the polynomial 6<i>x</i>² − 7<i>x</i> − 3 and verify the relationship between the zeros and the coefficients.", 2, "6x² − 9x + 2x − 3 = (2x − 3)(3x + 1) ⇒ zeros 3/2, −1/3 (1). Sum = 7/6 = −(−7)/6 ✓; product = −1/2 = −3/6 ✓ (1)."),
     S("A bag contains 5 red, 3 white and 2 black balls. A ball is drawn at random. Find the probability that it is (i) white (ii) neither red nor white.", 2, "Total = 10. (i) P(white) = 3/10 (1). (ii) neither red nor white = black: 2/10 = 1/5 (1)."),
    ]
    # ---------- SECTION C ----------
    C = [
     S("Find the ratio in which the <i>y</i>-axis divides the line segment joining A(−4, −6) and B(10, 12). Also find the point of division.", 3, "Let ratio be k : 1; x-coordinate = (10k − 4)/(k + 1) = 0 (1) ⇒ k = 2/5 i.e. 2 : 5 (1).<br>y = (2 × 12 + 5 × (−6))/7 = −6/7. Point = (0, −6/7) (1)."),
     OR(S("Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.", 3, "Let tangent XY touch circle (centre O) at P; take Q ≠ P on XY. Q lies outside the circle ⇒ OQ > OP (1). This holds for every Q ≠ P, so OP is the shortest distance from O to XY (1) ⇒ OP ⊥ XY (1)."),
        S("Prove that the lengths of the two tangents drawn from an external point to a circle are equal.", 3, "Tangents PA, PB from P; join OA, OB, OP. OA ⊥ PA, OB ⊥ PB (1). In ΔOAP and ΔOBP: OA = OB (radii), OP common, ∠OAP = ∠OBP = 90° (1) ⇒ RHS congruence ⇒ PA = PB (1).")),
     S("The daily wages (in ₹ hundreds) of 35 workers are given. Find the mean wage.<br>" + htbl(["Wage", "10–20", "20–30", "30–40", "40–50", "50–60"], ["No. of workers", "4", "7", "12", "9", "3"]), 3, "Mid-values 15, 25, 35, 45, 55; Σf = 35 (½). Σfx = 60 + 175 + 420 + 405 + 165 = 1225 (1½). Mean = 1225/35 = 35 (hundreds) = ₹ 3500 (1)."),
     S("A toy is in the form of a cone of radius 7 cm and height 24 cm mounted on a hemisphere of the same radius. Find the total surface area of the toy. (Use π = 22/7)", 3, "Slant height l = √(7² + 24²) = 25 cm (1). TSA = πrl + 2πr² (1) = (22/7)(7)(25) + 2(22/7)(49) = 550 + 308 = 858 cm² (1).", fig=fig_toy),
     OR(S("Prove that (sin θ + cosec θ)² + (cos θ + sec θ)² = 7 + tan² θ + cot² θ.", 3, "LHS = sin²θ + cosec²θ + 2 + cos²θ + sec²θ + 2 (1) = (sin²θ + cos²θ) + 4 + (1 + cot²θ) + (1 + tan²θ) (1) = 1 + 4 + 2 + tan²θ + cot²θ = RHS (1)."),
        S("If tan θ + sin θ = <i>m</i> and tan θ − sin θ = <i>n</i>, show that (<i>m</i>² − <i>n</i>²)² = 16<i>mn</i>.", 3, "m² − n² = 4 tanθ sinθ (1) ⇒ (m² − n²)² = 16 tan²θ sin²θ. mn = tan²θ − sin²θ = sin²θ(sec²θ − 1) = sin²θ tan²θ (1) ⇒ (m² − n²)² = 16mn (1).")),
     S("A train travels 360 km at a uniform speed. Had the speed been 5 km/h more, it would have taken 1 hour less for the same journey. Find the original speed of the train.", 3, "360/x − 360/(x + 5) = 1 ⇒ x² + 5x − 1800 = 0 (1) ⇒ (x + 45)(x − 40) = 0 (1) ⇒ x = 40 km/h (1)."),
    ]
    # ---------- SECTION D ----------
    D = [
     OR(S("Show that the points A(1, 7), B(4, 2), C(−1, −1) and D(−4, 4) are the vertices of a square.", 5, "AB = √(9 + 25) = √34, BC = √(25 + 9) = √34, CD = √(9 + 25) = √34, DA = √(25 + 9) = √34 (2). All sides equal (1). AC = √(4 + 64) = √68, BD = √(64 + 4) = √68 — diagonals equal (2). Hence ABCD is a square."),
        S("Find the coordinates of the points which divide the line segment joining A(−2, 2) and B(2, 8) into four equal parts.", 5, "Midpoint of AB: (0, 5) (1). Midpoint of A and (0, 5): (−1, 3.5) (2). Midpoint of (0, 5) and B: (1, 6.5) (2). Points: (−1, 3.5), (0, 5), (1, 6.5).")),
     S("The following table shows the marks of 50 students. Find the median marks.<br>" + htbl(["Marks", "0–10", "10–20", "20–30", "30–40", "40–50", "50–60"], ["No. of students", "5", "8", "15", "12", "6", "4"]), 5, "cf: 5, 13, 28, 40, 46, 50 (2). N/2 = 25 ⇒ median class 20–30 (1). l = 20, cf = 13, f = 15, h = 10 (1). Median = 20 + (25 − 13)/15 × 10 = 28 (1)."),
     OR(S("Prove that the ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding sides.", 5, "Given ΔABC ~ ΔPQR. Draw AM ⊥ BC, PN ⊥ QR (1). ar(ABC)/ar(PQR) = (½·BC·AM)/(½·QR·PN) = BC·AM/(QR·PN) (1). ΔABM ~ ΔPQN (AA) ⇒ AM/PN = AB/PQ (1). Also AB/PQ = BC/QR = CA/RP (1). ⇒ ar(ABC)/ar(PQR) = (BC/QR)(AB/PQ) = (AB/PQ)² = (BC/QR)² = (CA/RP)² (1)."),
        S("In an equilateral triangle ABC, D is a point on side BC such that BD = ⅓ BC. Prove that 9 AD² = 7 AB².", 5, "Let side = a. Draw AE ⊥ BC; BE = a/2, AE² = 3a²/4 (2). DE = BE − BD = a/2 − a/3 = a/6 (1). AD² = AE² + DE² = 3a²/4 + a²/36 = 28a²/36 = 7a²/9 (1) ⇒ 9AD² = 7AB² (1).")),
     S("In the figure, ABCD is a square of side 14 cm. With the vertices A, B, C, D as centres, four quadrants of radius 7 cm are drawn (unshaded). Find the area and the perimeter of the shaded region. (Use π = 22/7)", 5, "Area of square = 196 cm² (1). Area of 4 quadrants = 4 × ¼ × (22/7) × 49 = 154 cm² (2). Shaded area = 196 − 154 = 42 cm² (1).<br>Perimeter = 4 arcs, each ¼ × 2π × 7 = 11 cm ⇒ 44 cm (1).", fig=fig_sq),
    ]
    # ---------- SECTION E ----------
    E = [
     case("The canteen of Navodaya Public School sells samosas and cups of tea. On Monday, Ritu bought 3 samosas and 2 cups of tea for ₹ 70. On Tuesday, Karan bought 2 samosas and 5 cups of tea for ₹ 76. Let the price of one samosa be ₹ <i>x</i> and of one cup of tea be ₹ <i>y</i>.",
          [sub("Write the pair of linear equations formed by the given information.", 1, "3x + 2y = 70 and 2x + 5y = 76 (1)."),
           sub("Without solving, state with a reason whether the pair has a unique solution.", 1, "a₁/a₂ = 3/2, b₁/b₂ = 2/5; a₁/a₂ ≠ b₁/b₂ ⇒ unique solution (1)."),
           OR(sub("Find the price of one samosa and one cup of tea.", 2, "Multiply (1) by 5, (2) by 2: 15x + 10y = 350, 4x + 10y = 152 ⇒ 11x = 198 ⇒ x = 18 (1½). y = (70 − 54)/2 = 8. Samosa ₹ 18, tea ₹ 8 (½)."),
              sub("Find the cost of 5 samosas and 3 cups of tea at these prices.", 2, "Solve for x = 18, y = 8 (1). Cost = 5 × 18 + 3 × 8 = 90 + 24 = ₹ 114 (1)."))]),
     case("The students of Class X measured the height of the school water tank AB using a clinometer. From a point P on the level ground, the angle of elevation of the top A of the tank is 30°. They walk 60 m towards the tank to a point Q, from where the angle of elevation of A is 60°. Let AB = <i>h</i> metres. (Take √3 = 1.73)",
          [sub("Express BQ in terms of <i>h</i>.", 1, "In ΔABQ, tan 60° = h/BQ ⇒ BQ = h/√3 (1).", fig=None),
           sub("Express BP in terms of <i>h</i>.", 1, "In ΔABP, tan 30° = h/BP ⇒ BP = h√3 (1)."),
           OR(sub("Find the height of the tank.", 2, "BP − BQ = PQ ⇒ h√3 − h/√3 = 60 ⇒ 2h/√3 = 60 (1) ⇒ h = 30√3 = 51.9 m (1)."),
              sub("Find the distances BQ and BP.", 2, "h = 30√3 m. BQ = h/√3 = 30 m (1); BP = h√3 = 90 m (1)."))], fig=fig_case),
     case("Shruti starts a saving plan to buy a bicycle. She saves ₹ 150 in the first month and increases her saving by ₹ 25 every month. Her monthly savings form an AP.",
          [sub("Write the first three terms of the AP and its common difference.", 1, "150, 175, 200; d = 25 (1)."),
           sub("How much does she save in the 12th month?", 1, "a₁₂ = 150 + 11 × 25 = ₹ 425 (1)."),
           OR(sub("In which month will she save ₹ 600?", 2, "150 + (n − 1)25 = 600 ⇒ n − 1 = 18 (1) ⇒ n = 19, the 19th month (1)."),
              sub("Find her total savings in the first 12 months.", 2, "S₁₂ = 12/2 [2(150) + 11 × 25] = 6 × 575 (1) = ₹ 3450 (1)."))]),
    ]
    return assemble(1, A, B, C, D, E, kind='FULL SYLLABUS PRACTICE PAPER')
