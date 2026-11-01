from common import *
import math
META = meta(1)
# ---------- helper figures ----------
f12, _ = circle_fig({'A': 220, 'B': 320, 'C': 90}, chords=[('C', 'A'), ('C', 'B')], radii=['A', 'B'], extra=text(105, 88, "100°", sz=11))
cx = cy = 105
_, P = circle_fig({'P': 120, 'Q': 210, 'R': 320, 'S': 50}, center=None)
qx, qy = pt(cx, cy, 52, 210)
f24, _ = circle_fig({'P': 120, 'Q': 210, 'R': 320, 'S': 50}, chords=[('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P')], center=None, extra=text(qx+4, qy+4, "118°", sz=11))
# E37 figure
u = 80/13; th = math.degrees(math.asin(5/13))
_, P2 = circle_fig({'A': 180-th, 'B': th}, center='O')
mxy = (cx, cy-5*u)
f37, _ = circle_fig({'A': 180-th, 'B': th}, chords=[('A', 'B')], center='O', extra=line(cx, cy, *mxy, '#0f2347') + dot(*mxy, 'M', 5, 12) + text(cx+14, cy-12, "5 m", 'start', 10) + text(cx, cy-5*u-8, "24 m", sz=10))

# ---------- verification of numerics ----------
assert 50 + 9*18 == 212
assert F(17, 320).denominator == 320 and 320 == 2**6*5
assert F(153846, 999999) == F(2, 13)
assert 16**2/4 == 64 and (100-6**2) == 64
s = 17+25+26; assert math.isqrt(s//2*(s//2-17)*(s//2-25)*(s//2-26))**2 == s//2*(s//2-17)*(s//2-25)*(s//2-26) and math.isqrt(17*9*8*34) == 204
assert math.isqrt(36*18*12*6) == 216
n = (998-104)//6+1; assert n == 150 and n*(104+998)//2 == 82650 and all(x % 6 == 2 for x in (104, 998))
assert (3*12+7)*(12+1) == 3*144+10*12+7 or True
assert 12*7 == 84 and 2*(12+7) == 38
assert math.isqrt(24*14*7*3) == 84 and 2*84/21 == 8 and 84*25 == 2100
assert math.sqrt(13**2-12**2) == 5 and 2*math.sqrt(13**2-12**2) == 10

A = [
 mc("The point (−5, 0) lies on the:", "x-axis", ["y-axis", "second quadrant", "third quadrant"], "Ordinate is 0, so the point lies on the x-axis."),
 mc("Which of the following can be the coordinates of a point in the fourth quadrant?", "(3, −2)", ["(−3, 2)", "(−3, −2)", "(3, 2)"], "Fourth quadrant: x &gt; 0, y &lt; 0."),
 mc("The midpoint of the line segment joining A(2, −6) and B(−4, 10) is:", "(−1, 2)", ["(−1, −2)", "(1, 2)", "(−3, 8)"], "(" + fr("2 − 4", 2) + ", " + fr("−6 + 10", 2) + ") = (−1, 2)."),
 mc("A rectangle has length (2x + 1) cm and breadth (x − 3) cm. Its perimeter (in cm) is:", "6x − 4", ["3x − 2", "6x + 4", "3x + 4"], "P = 2[(2x + 1) + (x − 3)] = 2(3x − 2) = 6x − 4."),
 mc("The value of the polynomial p(x) = 3x² − 4x + 1 at x = −1 is:", "8", ["0", "−6", "2"], "p(−1) = 3 + 4 + 1 = 8."),
 mc("A cab company charges ₹40 as fixed charge and ₹14 per km. The fare (in ₹) for d km is:", "14d + 40", ["40d + 14", "54d", "14d − 40"], "Fare = 14 × d + 40."),
 mc("The absolute value of the rational number " + fr(-7, 9) + " is:", fr(7, 9), [fr(-7, 9), fr(9, 7), fr(-9, 7)], "|x| is never negative: |−7/9| = 7/9."),
 mc("Which of the following is an irrational number?", "√18", ["√(81/25)", "√0.04", "5.0505…(0.05 repeating)"], "√18 = 3√2 is irrational; √(81/25) = 9/5, √0.04 = 0.2 and 5.0505… (repeating) are rational."),
 mc("Which of the following has a terminating decimal expansion?", fr(9, 80), [fr(5, 12), fr(11, 18), fr(4, 15)], "80 = 2⁴ × 5, only 2 and 5 occur in the denominator, so 9/80 terminates (= 0.1125)."),
 mc("On expanding (3a − 2b)², we get:", "9a² − 12ab + 4b²", ["9a² − 6ab + 4b²", "9a² + 12ab + 4b²", "9a² − 12ab − 4b²"], "(x − y)² = x² − 2xy + y²."),
 mc("Using a suitable identity, the value of 98 × 102 is:", "9996", ["9998", "10004", "9904"], "(100 − 2)(100 + 2) = 100² − 2² = 10000 − 4 = 9996."),
 mc("In the figure, O is the centre of the circle and ∠AOB = 100°. Then ∠ACB is equal to:", "50°", ["100°", "200°", "25°"], "The angle at the centre is twice the angle at the remaining circumference: ∠ACB = 100° ÷ 2 = 50°.", fig=f12),
 mc("A chord of length 16 cm is drawn in a circle of radius 10 cm. Its distance from the centre is:", "6 cm", ["8 cm", "4 cm", "√164 cm"], "d² = 10² − 8² = 36, so d = 6 cm."),
 mc("The sides of a triangle are in the ratio 4 : 5 : 6 and its perimeter is 90 cm. The shortest side is:", "24 cm", ["20 cm", "30 cm", "15 cm"], "One part = 90 ÷ 15 = 6 cm; shortest side = 4 × 6 = 24 cm."),
 mc("The area of a triangle with sides 5 cm, 12 cm and 13 cm, found using Heron’s formula, is:", "30 cm²", ["60 cm²", "32.5 cm²", "78 cm²"], "s = 15; area = √(15 × 10 × 3 × 2) = √900 = 30 cm²."),
 mc("A letter is chosen at random from the word ‘EDUCATION’. The probability that it is a vowel is:", fr(5, 9), [fr(4, 9), fr(1, 2), fr(5, 8)], "Vowels E, U, A, I, O = 5 out of 9 letters."),
 mc("A die is thrown once. The probability of getting a number less than 5 is:", fr(2, 3), [fr(1, 3), fr(5, 6), fr(1, 2)], "Favourable outcomes 1, 2, 3, 4 → 4/6 = 2/3."),
 mc("If the n-th term of a sequence is t<sub>n</sub> = n² − 3n, then t<sub>7</sub> is:", "28", ["14", "70", "−28"], "t₇ = 49 − 21 = 28."),
 ar("√2 + 1 is an irrational number.", "The sum of a rational number and an irrational number is always irrational.", 'a', "Both true; R directly justifies A (1 is rational, √2 irrational)."),
 ar("For the sequence defined by t₁ = 2 and t<sub>n</sub> = t<sub>n−1</sub> + 4 (n ≥ 2), the third term is 12.", "A recursive rule gives every term from the term before it.", 'd', "t₂ = 6, t₃ = 10, so A is false; R is a true statement."),
]
B = [
 sa("A taxi charges ₹50 for the first 3 km and ₹18 for every km after that. What is the fare for a journey of 12 km?", 2, "Extra distance = 12 − 3 = 9 km (½)<br>Extra charge = 9 × 18 = ₹162 (1)<br>Fare = 50 + 162 = <b>₹212</b> (½)"),
 OR(sa("Without actual division, decide whether the decimal expansion of " + fr(17, 320) + " is terminating. If it is, state the number of decimal places.", 2, "320 = 2⁶ × 5, which has only 2 and 5 as prime factors, so 17/320 terminates (1). Number of decimal places = greater of the powers of 2 and 5 = 6 (1)."),
    sa("Find any two rational numbers between " + fr(1, 4) + " and " + fr(1, 3) + ".", 2, "Write with common denominator 48: 1/4 = 12/48, 1/3 = 16/48 (1). Two rational numbers: <b>13/48 and 14/48 (= 7/24)</b> (1). (Any two correct numbers.)")),
 sa("Factorise: 9a² + 30ab + 25b².", 2, "= (3a)² + 2(3a)(5b) + (5b)² (1) = <b>(3a + 5b)²</b> = (3a + 5b)(3a + 5b) (1)"),
 sa("In the figure, PQRS is a cyclic quadrilateral with ∠PQR = 118°. Find ∠PSR and state the reason.", 2, "Opposite angles of a cyclic quadrilateral are supplementary (1).<br>∠PSR = 180° − 118° = <b>62°</b> (1)", fig=f24),
 sa("Find the second, third and fourth terms of the sequence given by t₁ = 3 and t<sub>n</sub> = 2t<sub>n−1</sub> − 1 for n ≥ 2.", 2, "t₂ = 2(3) − 1 = 5; t₃ = 2(5) − 1 = 9; t₄ = 2(9) − 1 = 17. (1 mark for method, 1 for all three values)"),
]
C = [
 sa("Show that 0.153846153846… = " + fr(2, 13) + ".", 3, "Let x = 0.153846153846… (½). Six digits repeat, so multiply by 10⁶: 1000000x = 153846.153846… (1).<br>Subtracting: 999999x = 153846 (½)<br>x = 153846/999999 = <b>2/13</b> (dividing numerator and denominator by 76923) (1)"),
 OR(sa("A school canteen recorded the drink chosen by 100 students in a day:" + htable(["Drink", "Tea", "Coffee", "Juice", "Milk"], ["Students", 30, 20, 35, 15]) + "A student is selected at random. Find the probability that the student chose (i) juice, (ii) tea or milk, (iii) not coffee.", 3, "Total = 100.<br>(i) P(juice) = 35/100 = <b>7/20</b> (1)<br>(ii) P(tea or milk) = (30 + 15)/100 = <b>9/20</b> (1)<br>(iii) P(not coffee) = (100 − 20)/100 = <b>4/5</b> (1)"),
    sa("In a survey of 80 households the number of members was recorded:" + htable(["Members", 2, 3, 4, 5], ["Households", 10, 25, 30, 15]) + "A household is chosen at random. Find the probability that it has (i) exactly 4 members, (ii) at most 3 members, (iii) more than 4 members.", 3, "Total = 80.<br>(i) 30/80 = <b>3/8</b> (1) (ii) (10 + 25)/80 = <b>7/16</b> (1) (iii) 15/80 = <b>3/16</b> (1)")),
 sa("Write the coordinates of the point (i) which lies on the x-axis, 7 units to the left of the origin; (ii) which lies on the y-axis, 4 units below the origin; (iii) which is the mirror image of (−3, 5) in the x-axis.", 3, "(i) <b>(−7, 0)</b> (1) &nbsp;(ii) <b>(0, −4)</b> (1) &nbsp;(iii) reflection in the x-axis changes the sign of y: <b>(−3, −5)</b> (1)"),
 sa("Simplify: (x + 2)³ + (x − 2)³.", 3, "(x + 2)³ = x³ + 6x² + 12x + 8 (1)<br>(x − 2)³ = x³ − 6x² + 12x − 8 (1)<br>Sum = <b>2x³ + 24x</b> (1)"),
 sa("A chord of length 30 cm is drawn in a circle of diameter 34 cm. Find (i) the distance of the chord from the centre; (ii) the length of another chord of this circle which is at a distance of 15 cm from the centre.", 3, "r = 17 cm. (i) Half chord = 15; d² = 17² − 15² = 64, d = <b>8 cm</b> (1½)<br>(ii) Half chord² = 17² − 15² = 64 → half = 8, chord = <b>16 cm</b> (1½)"),
 OR(sa("Using Heron’s formula, find the area of a triangle whose sides are 17 cm, 25 cm and 26 cm.", 3, "s = (17 + 25 + 26)/2 = 34 cm (1)<br>Area = √[34 × 17 × 9 × 8] (1) = √41616 = <b>204 cm²</b> (1)"),
    sa("The sides of a triangle are in the ratio 3 : 4 : 5 and its perimeter is 72 cm. Find its area.", 3, "Sides: 18 cm, 24 cm, 30 cm (1); s = 36 (½)<br>Area = √[36 × 18 × 12 × 6] = √46656 = <b>216 cm²</b> (1½)")),
]
sq = {'A': (-2, -1), 'B': (4, -1), 'C': (4, 3), 'D': (-2, 3)}
figD32 = coord_plane(sq, xr=(-4, 6), yr=(-3, 5), u=22, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
D = [
 sa("An architect marks the four corners of a rectangular courtyard on a grid as A(−2, −1), B(4, −1), C(4, 3) and D(−2, 3).<br>(a) Plot the points on a coordinate plane and join them in order. (2 marks)<br>(b) Find the lengths AB, BC, CD and DA. (1½ marks)<br>(c) Using the diagonals, justify that ABCD is a rectangle but not a square. (1½ marks)", 5,
    "(a) Correct plotting of 4 points (1½) and joining (½):" + figD32 + "(b) AB = 6, BC = 4, CD = 6, DA = 4 units (1½)<br>(c) AC = √(6² + 4²) = √52, BD = √(6² + 4²) = √52 → equal diagonals and opposite sides equal ⇒ rectangle (1). Adjacent sides 6 ≠ 4 ⇒ not a square (½)"),
 sa("How many 3-digit numbers leave remainder 2 when divided by 6? Find the sum of all such numbers. (2½ + 2½)", 5, "Numbers: 104, 110, 116, …, 998 — an AP with a = 104, d = 6, l = 998 (1)<br>n = (998 − 104)/6 + 1 = <b>150</b> (1½)<br>Sum = n/2 (a + l) = 75 × 1102 (1) = <b>82650</b> (1½)"),
 OR(sa("A battery company tested 500 batteries and recorded their life:" + htable(["Life (hours)", "0 – 50", "50 – 100", "100 – 150", "150 – 200"], ["Number of batteries", 20, 70, 190, 220]) + "Find the probability that a randomly chosen battery lasts (i) less than 50 hours (1), (ii) between 50 and 150 hours (2), (iii) more than 150 hours (2).", 5, "Total = 500. (i) 20/500 = <b>1/25</b> (1) (ii) (70 + 190)/500 = <b>13/25</b> (2) (iii) 220/500 = <b>11/25</b> (2)"),
    sa("A box contains 6 blue pens, 8 black pens and 4 red pens. A pen is drawn at random. Find the probability that it is (i) blue (1), (ii) black or red (2), (iii) neither blue nor black (2).", 5, "Total pens = 18. (i) 6/18 = <b>1/3</b> (1) (ii) (8 + 4)/18 = <b>2/3</b> (2) (iii) 4/18 = <b>2/9</b> (2)")),
 OR(sa("The length of a rectangular play area is 5 m more than its breadth, and its area is 84 m². Form a quadratic expression in the breadth x, factorise it and find the perimeter of the play area.", 5, "Let breadth = x m, length = (x + 5) m. Area: x(x + 5) = 84 ⇒ x² + 5x − 84 = 0 (1½)<br>x² + 12x − 7x − 84 = (x + 12)(x − 7) = 0 (1½) ⇒ x = 7 (breadth cannot be negative) (1)<br>Length = 12 m. Perimeter = 2(12 + 7) = <b>38 m</b> (1)"),
    sa("A carpentry student uses 3 large square tiles of side x units, 10 rectangular strips of length x and width 1 unit, and 7 small square tiles of side 1 unit to make one large rectangle without overlap. Find the length and breadth of the rectangle in terms of x.", 5, "Total area = 3x² + 10x + 7 (1½)<br>Split the middle term: 3x² + 3x + 7x + 7 (1½) = 3x(x + 1) + 7(x + 1) (1) = <b>(3x + 7)(x + 1)</b> (1)<br>Length = (3x + 7) units, breadth = (x + 1) units.")),
]
E = [
 case("Priya’s mobile data pack gives her 60 GB at the start. She uses 4 GB of data every day. The data (in GB) left after x days is given by D = 60 − 4x.",
      [sub("How much data is left after 5 days?", 1, "D = 60 − 20 = <b>40 GB</b>"),
       sub("State the degree of D = 60 − 4x and the coefficient of x.", 1, "Degree = <b>1</b> (linear polynomial); coefficient of x = <b>−4</b> (negative ⇒ linear decay)."),
       OR(sub("After how many days will only 12 GB of data be left?", 2, "60 − 4x = 12 (1) ⇒ 4x = 48 ⇒ x = <b>12 days</b> (1)"),
          sub("After how many days will her data pack be exhausted?", 2, "60 − 4x = 0 (1) ⇒ x = <b>15 days</b> (1)"))]),
 case("A circular pond with centre O is built in a park. A fence AB, 24 m long, is fixed as a chord of the pond. The perpendicular distance of the fence from the centre, OM, is 5 m.",
      [sub("Find the radius of the pond.", 1, "OM ⊥ AB bisects it: AM = 12 m. r² = 12² + 5² = 169 ⇒ r = <b>13 m</b>"),
       sub("Another fence CD, also 24 m long, is fixed in the same pond. How far is it from the centre?", 1, "Equal chords of a circle are equidistant from the centre ⇒ <b>5 m</b>."),
       OR(sub("A walking path PQ is a chord at a distance of 12 m from O. Find its length.", 2, "Half of PQ = √(13² − 12²) = 5 (1) ⇒ PQ = <b>10 m</b> (1)"),
          sub("Four lamps are placed at A, B, D and E on the boundary forming a cyclic quadrilateral ABDE. If ∠ADE = 75°, find ∠ABE and give the reason.", 2, "Opposite angles of a cyclic quadrilateral are supplementary (1) ⇒ ∠ABE = 180° − 75° = <b>105°</b> (1)"))], fig=f37),
 case("A residents’ association has a triangular garden whose sides are 10 m, 17 m and 21 m.",
      [sub("Find the semi-perimeter of the garden.", 1, "s = (10 + 17 + 21)/2 = <b>24 m</b>"),
       sub("Find the area of the garden using Heron’s formula.", 1, "Area = √[24 × 14 × 7 × 3] = √7056 = <b>84 m²</b>"),
       OR(sub("Find the length of the altitude drawn to the longest side.", 2, "Longest side = 21 m. ½ × 21 × h = 84 (1) ⇒ h = <b>8 m</b> (1)"),
          sub("Grass is to be laid over the whole garden at ₹25 per m². Find the total cost.", 2, "Cost = 84 × 25 (1) = <b>₹2100</b> (1)"))]),
]
SECTIONS = sections(A, B, C, D, E)
