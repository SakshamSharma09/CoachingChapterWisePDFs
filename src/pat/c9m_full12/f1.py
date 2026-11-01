from cm import *
import math
META = meta(1)

# ---------- figures ----------
cx = cy = 105
f6, _ = circle_fig({'A': 200, 'B': 340, 'C': 90}, chords=[('C', 'A'), ('C', 'B')], radii=['A', 'B'], extra=text(105, 130, "140°", sz=11))
Ptri = {'A': (120, 12), 'B': (25, 135), 'C': (215, 135), 'P': (72.5, 73.5), 'Q': (167.5, 73.5)}
f25 = gfig(Ptri, [('A', 'B'), ('B', 'C'), ('C', 'A'), ('P', 'Q')], off={'A': (0, -3), 'B': (-10, 12), 'C': (10, 12), 'P': (-12, 4), 'Q': (12, 4)},
           extra=text(120, 66, "7.5 cm", sz=10) + text(100, 62, "62°", 'end', 10))

# ---------- numeric verification ----------
assert math.dist((-2, 3), (4, -5)) == 10
assert 2*(-3)-5 == -11
assert (7**2)*0 == 0 and 25**2 - 24**2 == 7**2 and 2*24 == 48
assert 60/15*7 == 28 and 3*5**2-2 == 73 and 5+5*3 == 20
assert math.sqrt(3)*math.sqrt(12) - 6 < 1e-9
assert 2**11-1 == 2047 == 23*89
assert (20*60+30*70)/50 == 66 and (300*.1+200*.2)/500 == .14
assert [d for d in range(1, 21) if 20 % d == 0] == [1, 2, 4, 5, 10, 20]
assert F(7, 13)*999999 == 538461
assert 800+350*6 == 2900 and 105**2 == 11025 and F(29, 200) == F(145, 1000)
assert F(1, 6) < F(21, 120) < F(22, 120) < F(1, 5)
s = 18; assert math.isqrt(18*9*8*1) == 36; assert math.isqrt(54*27*18*9) == 486 and 9*12 == 108
assert (12+28+24+16 == 80) and F(24, 80) == F(3, 10) and F(40, 80) == F(1, 2)
assert 24+36+28+12 == 100
def mrcd(m, n):
    r = 1; tr = []
    for k in range(2, min(m, n)+1):
        if m % k == 0 and n % k == 0: r = k
        tr.append((k, m % k == 0 and n % k == 0, r))
    return r, tr
g, trace = mrcd(9, 12); assert g == 3
d = [i for i in range(105, 1000) if i % 7 == 0]; assert len(d) == 128 and sum(d) == 70336
assert 40+120+360+280 == 800 and F(360+280, 800) == F(4, 5) and F(40, 800) == F(1, 20) and F(480, 800) == F(3, 5)
assert 8*12 == 96 and 2*(8+12) == 40 and (2*3+3)*(3+4) == 2*9+11*3+12
assert 150+25*11 == 425 and 125+25*15 == 500 and 10*(150+375)//2 == 2625
assert math.isqrt(60*35*21*4) == 420 and 2*420/56 == 15 and 25+39+56 == 120 and 120*80 == 9600 and 420*12 == 5040
assert 25*68 == 1700 and 15*76 == 1140 and (1700+1140)/40 == 71 and (2840+20*74)/60 == 72
assert 150*.6+100*.4 == 130 and (130+.45*100) == .5*(250+100)
assert (2*80+3*70+5*90) == 160+210+450 == 820 and 820/10 == 82

A = [
 mc("The point (0, −7) lies on the:", "y-axis", ["x-axis", "third quadrant", "fourth quadrant"], "Abscissa is 0, so the point lies on the y-axis."),
 mc("The distance between the points A(−2, 3) and B(4, −5) is:", "10 units", ["8 units", "14 units", "√28 units"], "d = √[(4 + 2)² + (−5 − 3)²] = √(36 + 64) = 10."),
 mc("If p(x) = 2x − 5, then the value of p(−3) is:", "−11", ["−1", "1", "11"], "p(−3) = 2(−3) − 5 = −6 − 5 = −11."),
 mc("Which of the following is an irrational number?", "√50", ["√(49/16)", "√0.09", "0.2525… (25 repeating)"], "√50 = 5√2 is irrational. √(49/16) = 7/4, √0.09 = 0.3 and 0.2525… are rational."),
 mc("The product (x + 4)(x − 4)(x² + 16) is equal to:", "x⁴ − 256", ["x⁴ + 256", "x⁴ − 16", "x⁴ − 8x² + 256"], "(x² − 16)(x² + 16) = x⁴ − 256."),
 mc("In the figure, O is the centre of the circle and ∠AOB = 140°. Then ∠ACB is equal to:", "70°", ["140°", "280°", "35°"], "Angle at the centre = 2 × angle at the remaining part of the circle, so ∠ACB = 140° ÷ 2 = 70°.", fig=f6),
 mc("A chord of length 48 cm is drawn in a circle of radius 25 cm. Its distance from the centre is:", "7 cm", ["24 cm", "√1201 cm", "14 cm"], "d² = 25² − 24² = 49, so d = 7 cm."),
 mc("The sides of a triangle are in the ratio 3 : 5 : 7 and its perimeter is 60 cm. The longest side is:", "28 cm", ["20 cm", "12 cm", "35 cm"], "One part = 60 ÷ 15 = 4 cm; longest side = 7 × 4 = 28 cm."),
 mc("A letter is chosen at random from the word ‘MATHEMATICS’. The probability that it is a vowel is:", fr(4, 11), [fr(7, 11), fr(1, 4), fr(5, 11)], "Vowels A, E, A, I = 4 out of 11 letters."),
 mc("If the n-th term of a sequence is t<sub>n</sub> = 3n² − 2, then t<sub>5</sub> is:", "73", ["13", "28", "77"], "t₅ = 3(25) − 2 = 73."),
 mc("The converse of the proposition ‘If a number is divisible by 15, then it is divisible by 5’ is:", "If a number is divisible by 5, then it is divisible by 15.", ["If a number is not divisible by 15, then it is not divisible by 5.", "If a number is divisible by 5, then it is divisible by 3.", "A number is divisible by 15 only if it is divisible by 5."], "The converse of ‘if X then Y’ is ‘if Y then X’. (It is false: 10 is a multiple of 5 but not of 15.)"),
 mc("A counterexample to the claim ‘If n is a prime number, then 2<sup>n</sup> − 1 is a prime number’ is:", "n = 11", ["n = 2", "n = 5", "n = 7"], "2² − 1 = 3, 2⁵ − 1 = 31 and 2⁷ − 1 = 127 are prime, but 2¹¹ − 1 = 2047 = 23 × 89 is composite."),
 mc("In a class, 20 students have an average mark of 60 and the other 30 students have an average mark of 70. The average mark of all 50 students is:", "66", ["65", "67", "64"], "(20 × 60 + 30 × 70) ÷ 50 = (1200 + 2100) ÷ 50 = 66. (The simple average 65 is wrong because the groups differ in size.)"),
 mc("300 mL of juice with 10% sugar is mixed with 200 mL of juice with 20% sugar. The concentration of sugar in the mixture is:", "14%", ["15%", "13%", "16%"], "(300 × 0.10 + 200 × 0.20) ÷ 500 = 70 ÷ 500 = 0.14 = 14%."),
 mc("When the algorithm that checks every j from 1 to n is executed for n = 20, the final list of divisors is:", "[1, 2, 4, 5, 10, 20]", ["[2, 4, 5, 10]", "[1, 2, 4, 5, 10, 15, 20]", "[1, 2, 5, 10, 20]"], "j = 1, 2, 4, 5, 10 and 20 divide 20; the list stays in increasing order."),
 mc("In a parallelogram ABCD, ∠A = 72°. Then ∠B is equal to:", "108°", ["72°", "98°", "118°"], "Adjacent angles of a parallelogram are supplementary: ∠B = 180° − 72° = 108°."),
 mc("In △ABC, D and E are the midpoints of AB and AC respectively. If BC = 18 cm, then DE is:", "9 cm", ["18 cm", "36 cm", "6 cm"], "By the Midpoint Theorem DE = ½ BC = 9 cm."),
 mc("In a sequence t₁ = 5 and t<sub>n</sub> = t<sub>n−1</sub> + 3 for n ≥ 2. The sixth term is:", "20", ["17", "23", "18"], "5, 8, 11, 14, 17, 20."),
 ar("√3 × √12 is a rational number.", "The product of two irrational numbers is always irrational.", 'c', "√3 × √12 = √36 = 6 is rational, so A is true. R is false (e.g. √3 × √12 = 6, √2 × √2 = 2)."),
 ar("A quadrilateral whose diagonals are equal must be a rectangle.", "The diagonals of a rectangle are equal.", 'd', "R is true, but its converse is not: an isosceles trapezium has equal diagonals and is not a rectangle, so A is false."),
]
B = [
 sa("A gym charges ₹800 as joining fee and ₹350 per month. Write an expression for the total amount paid for m months and find the amount for 6 months.", 2, "Total = 800 + 350m (1)<br>For m = 6: 800 + 2100 = <b>₹2900</b> (1)"),
 OR(sa("Without actual division, decide whether " + fr(29, 200) + " has a terminating decimal expansion. If it does, find the number of decimal places.", 2, "200 = 2³ × 5², only 2 and 5 occur ⇒ terminates (1). Number of decimal places = larger power = <b>3</b> (0.145) (1)"),
    sa("Find two rational numbers between " + fr(1, 6) + " and " + fr(1, 5) + ".", 2, "LCM 30 gives 5/30 and 6/30; multiply by 4: 20/120 and 24/120 (1). Two numbers: <b>21/120 and 22/120</b> (any two correct numbers) (1)")),
 sa("Using a suitable identity, evaluate 105².", 2, "105² = (100 + 5)² (½) = 100² + 2(100)(5) + 5² (1) = 10000 + 1000 + 25 = <b>11025</b> (½)"),
 sa("Write the converse of the proposition ‘If a number is divisible by 12, then it is divisible by 6.’ Is the converse true? Justify.", 2, "Converse: <b>If a number is divisible by 6, then it is divisible by 12.</b> (1)<br>False. Counterexample: 18 is divisible by 6 but not by 12. (1)"),
 sa("In the figure, P and Q are the midpoints of AB and AC and PQ = 7.5 cm, ∠APQ = 62°. Find BC and ∠ABC, giving reasons.", 2, "By the Midpoint Theorem PQ ∥ BC and PQ = ½BC ⇒ <b>BC = 15 cm</b> (1)<br>PQ ∥ BC, so corresponding angles are equal: <b>∠ABC = ∠APQ = 62°</b> (1)", fig=f25),
]
C = [
 sa("Show that 0.538461538461… = " + fr(7, 13) + ".", 3, "Let x = 0.538461538461… Six digits repeat, so 10⁶x = 538461.538461… (1)<br>Subtracting: 999999x = 538461 (1)<br>x = 538461/999999 = <b>7/13</b> (dividing numerator and denominator by 76923) (1)"),
 OR(sa("The mode of travel to school of 100 students was recorded:" + htable(["Mode", "Walk", "Cycle", "Bus", "Car"], ["Students", 24, 36, 28, 12]) + "A student is chosen at random. Find the probability that the student (i) cycles, (ii) walks or comes by bus, (iii) does not come by car.", 3, "Total = 100. (i) 36/100 = <b>9/25</b> (1) (ii) (24 + 28)/100 = <b>13/25</b> (1) (iii) 1 − 12/100 = <b>22/25</b> (1)"),
    sa("The number of books read last month by 80 students was recorded:" + htable(["Books", 0, 1, 2, 3], ["Students", 12, 28, 24, 16]) + "A student is chosen at random. Find the probability that the student read (i) exactly 2 books, (ii) at least 2 books, (iii) fewer than 2 books.", 3, "Total = 80. (i) 24/80 = <b>3/10</b> (1) (ii) (24 + 16)/80 = <b>1/2</b> (1) (iii) (12 + 28)/80 = <b>1/2</b> (1)")),
 sa("Write the coordinates of the point (i) on the x-axis, 6 units to the right of the origin; (ii) on the y-axis, 9 units above the origin; (iii) which is the mirror image of (4, −7) in the y-axis.", 3, "(i) <b>(6, 0)</b> (1) (ii) <b>(0, 9)</b> (1) (iii) The y-coordinate stays, the x-coordinate changes sign: <b>(−4, −7)</b> (1)"),
 sa("Meera’s marks are: unit tests 80%, project 70%, final examination 90%. The annual score is found by combining the three in the ratio 2 : 3 : 5. Find her annual score and say why a simple average of 80, 70 and 90 would not be correct.", 3, "Weighted mean = (80 × 2 + 70 × 3 + 90 × 5) ÷ (2 + 3 + 5) (1) = (160 + 210 + 450) ÷ 10 = <b>82%</b> (1)<br>The three components do not carry equal importance; the simple average (80%) ignores their weights. (1)"),
 OR(sa("Using Heron’s formula, find the area of a triangle whose sides are 9 cm, 10 cm and 17 cm.", 3, "s = (9 + 10 + 17)/2 = 18 cm (1)<br>Area = √[18 × 9 × 8 × 1] (1) = √1296 = <b>36 cm²</b> (1)"),
    sa("The sides of a triangle are in the ratio 9 : 12 : 15 and its perimeter is 108 cm. Find its area.", 3, "Sides: 27 cm, 36 cm, 45 cm (1); s = 54 (½)<br>Area = √[54 × 27 × 18 × 9] = √236196 = <b>486 cm²</b> (1½)")),
 sa("Execute the final gcd algorithm of the chapter (start with most-recent-common-divisor = 1 and check every k from 2 to min(m, n)) for m = 9 and n = 12. Show each step and write the gcd.", 3, "min(9, 12) = 9; start with 1. (½)<br>k = 2: does not divide 9 → 1; <b>k = 3: divides both → 3</b>; k = 4, 5, 6, 7, 8: not both → stays 3; k = 9: does not divide 12 → stays 3 (2)<br>gcd(9, 12) = <b>3</b> (½)"),
]
Pp = {'P': (1, 1), 'Q': (5, 1), 'R': (7, 4), 'S': (3, 4)}
figD32 = coord_plane(Pp, xr=(-1, 9), yr=(-1, 6), u=22, segs=[('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P')])
D = [
 sa("A craftsman marks the corners of a metal plate on a grid as P(1, 1), Q(5, 1), R(7, 4) and S(3, 4).<br>(a) Plot the points and join them in order. (2 marks)<br>(b) Find the lengths PQ, QR, RS and SP. (1½ marks)<br>(c) Show that PQRS is a parallelogram by finding the midpoints of the diagonals PR and QS. (1½ marks)", 5,
    "(a) Plotting the 4 points (1½) and joining them (½):" + figD32 + "(b) PQ = 4, RS = 4; QR = √(2² + 3²) = √13, SP = √(2² + 3²) = √13 (1½)<br>(c) Midpoint of PR = ((1 + 7)/2, (1 + 4)/2) = (4, 2.5); midpoint of QS = ((5 + 3)/2, (1 + 4)/2) = (4, 2.5) (1). The diagonals bisect each other, so PQRS is a parallelogram (½). (Opposite sides equal also accepted.)"),
 OR(sa("How many three-digit numbers are multiples of 7? Find their sum. (2½ + 2½)", 5, "Numbers: 105, 112, …, 994 — an AP with a = 105, d = 7, l = 994 (1)<br>n = (994 − 105)/7 + 1 = <b>128</b> (1½)<br>Sum = n/2 (a + l) = 64 × 1099 = <b>70336</b> (2½)"),
    sa("A tyre company tested 800 tyres and recorded the distance they ran:" + htable(["Distance (thousand km)", "0 – 20", "20 – 40", "40 – 60", "60 – 80"], ["Number of tyres", 40, 120, 360, 280]) + "Find the probability that a tyre chosen at random runs (i) at least 40 thousand km (1), (ii) less than 20 thousand km (1), (iii) between 20 and 60 thousand km (2), and (iv) state the sum of all four class probabilities (1).", 5, "Total = 800. (i) (360 + 280)/800 = <b>4/5</b> (1) (ii) 40/800 = <b>1/20</b> (1) (iii) (120 + 360)/800 = <b>3/5</b> (2)<br>(iv) 40/800 + 120/800 + 360/800 + 280/800 = <b>1</b> (1)")),
 OR(sa("State and prove the Midpoint Theorem: the segment joining the midpoints of two sides of a triangle is parallel to the third side and equal to half of it.", 5, "Statement: in △ABC, if P and Q are midpoints of AB and AC, then PQ ∥ BC and PQ = ½BC. (1)<br>Proof: Extend PQ to R so that QR = PQ and join CR. (½)<br>In △APQ and △CRQ: AQ = CQ, PQ = RQ, ∠AQP = ∠CQR (vertically opposite) ⇒ △APQ ≅ △CRQ (SAS) (1½)<br>So CR = AP = PB and ∠APQ = ∠CRQ ⇒ AB ∥ CR (alternate angles) (1)<br>PB = CR and PB ∥ CR ⇒ PBCR is a parallelogram (equal parallel sides), so PR ∥ BC and PR = BC. Hence PQ ∥ BC and PQ = ½PR = ½BC. (1)"),
    sa("Batch A of brass weighs 150 kg and is 60% copper. Batch B weighs 100 kg and is 40% copper. Batch C is 45% copper. All three batches are melted together and the alloy is found to be 50% copper. Find the weight of Batch C.", 5, "Let Batch C weigh y kg. Copper in A = 90 kg, in B = 40 kg, in C = 0.45y (1½)<br>Concentration = copper ÷ total: 0.50 = (90 + 40 + 0.45y) ÷ (250 + y) (1½)<br>0.5(250 + y) = 130 + 0.45y ⇒ 125 + 0.5y = 130 + 0.45y (1)<br>0.05y = 5 ⇒ <b>y = 100 kg</b> (1)")),
 OR(sa("The length of a rectangular plot is 4 m more than its breadth and its area is 96 m². Form a quadratic expression in the breadth x, factorise it and find the perimeter of the plot.", 5, "Breadth = x m, length = (x + 4) m. Area: x(x + 4) = 96 ⇒ x² + 4x − 96 = 0 (1½)<br>Factorise: (x + 12)(x − 8) = 0 (1½)<br>x = 8 (x = −12 rejected) ⇒ breadth 8 m, length 12 m (1)<br>Perimeter = 2(8 + 12) = <b>40 m</b> (1)"),
    sa("A carpenter makes a rectangle from 2 square tiles of side x units, 11 rectangular strips of size x by 1 unit and 12 unit squares. Write the total area as a polynomial, factorise it and find the dimensions of the rectangle.", 5, "Area = 2x² + 11x + 12 (1)<br>Split the middle term: 2x² + 8x + 3x + 12 (1½) = 2x(x + 4) + 3(x + 4) = (2x + 3)(x + 4) (1½)<br>Dimensions: <b>(2x + 3) units by (x + 4) units</b> (1)")),
]
E = [
 case("Ananya saves for a trip. In week 1 she saves ₹150 and every week she saves ₹25 more than in the week before. The amount saved in week n is given by t<sub>n</sub> = 125 + 25n.",
      [sub("How much does she save in week 12?", 1, "t₁₂ = 125 + 25 × 12 = <b>₹425</b>"),
       sub("What type of sequence is this and what is the common difference?", 1, "It is an arithmetic progression (each term is 25 more than the previous); common difference = <b>₹25</b>."),
       OR(sub("In which week does her weekly saving first reach ₹500?", 2, "125 + 25n = 500 (1) ⇒ n = 15, i.e. <b>week 15</b> (1)"),
          sub("Find the total amount she saves in the first 10 weeks.", 2, "t₁₀ = 375 (½). Sum = 10/2 × (150 + 375) (1) = <b>₹2625</b> (½)"))]),
 case("A triangular plot of land has sides 25 m, 39 m and 56 m.",
      [sub("Find the semi-perimeter of the plot.", 1, "s = (25 + 39 + 56)/2 = <b>60 m</b>"),
       sub("Find its area using Heron’s formula.", 1, "Area = √[60 × 35 × 21 × 4] = √176400 = <b>420 m²</b>"),
       OR(sub("Find the length of the perpendicular from the opposite vertex to the longest side.", 2, "½ × 56 × h = 420 (1) ⇒ h = <b>15 m</b> (1)"),
          sub("The owner fences the plot at ₹80 per metre and levels the ground at ₹12 per m². Find the cost of fencing and the cost of levelling.", 2, "Fencing = 120 × 80 = <b>₹9600</b> (1); levelling = 420 × 12 = <b>₹5040</b> (1)"))]),
 case("In a Maths Olympiad, 25 students of Class IX-A scored an average of 68 marks and 15 students of Class IX-B scored an average of 76 marks. The school wants the average score of all 40 students.",
      [sub("Find the total marks scored by the students of IX-A.", 1, "25 × 68 = <b>1700</b>"),
       sub("Is (68 + 76) ÷ 2 = 72 the correct average of the 40 students? Give a reason.", 1, "<b>No.</b> The two sections have different numbers of students, so each average must be weighted by the number of students."),
       OR(sub("Find the average score of all 40 students.", 2, "Total = 1700 + 15 × 76 = 1700 + 1140 = 2840 (1). Average = 2840 ÷ 40 = <b>71</b> (1)"),
          sub("Class IX-C with 20 students joins and the average of all 60 students becomes 72. Find the average of IX-C.", 2, "2840 + 20x = 72 × 60 = 4320 (1) ⇒ 20x = 1480 ⇒ <b>x = 74</b> (1)"))]),
]
import add14
A, B, C, E = add14.patch(META['set_no'], A, B, C, E)
SECTIONS = sections(A, B, C, D, E)
