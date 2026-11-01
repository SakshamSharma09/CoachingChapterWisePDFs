from common import *
import math
META = meta(3)
cx = cy = 105
def cyc(angs, chords, labelpt=None, label=None, **kw):
    ex = ''
    if labelpt:
        x, y = pt(cx, cy, 50, angs[labelpt]); ex = text(x, y+4, label, sz=11)
    return circle_fig(angs, chords=chords, center=kw.get('center'), extra=ex)[0]
f12 = cyc({'A': 100, 'B': 200, 'C': 300, 'D': 20}, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], 'B', '95°')
th = math.degrees(math.asin(0.6)); u = 8
f24 = circle_fig({'A': 180-th, 'B': th}, chords=[('A', 'B')], center='O', extra=line(cx, cy, cx, cy-6*u, '#0f2347') + dot(cx, cy-6*u, 'M', 5, 12) + text(cx+16, cy-14, "6 cm", 'start', 10) + text(cx, cy-6*u-8, "16 cm", sz=10))[0]
f38 = cyc({'P': 95, 'Q': 190, 'R': 280, 'S': 25}, [('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P')], 'Q', '100°')
rh = {'A': (0, 3), 'B': (4, 0), 'C': (0, -3), 'D': (-4, 0)}
sol32 = coord_plane(rh, xr=(-5, 5), yr=(-4, 4), u=22, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
# ---- checks ----
assert 60+13*12 == 216 and 27 == 27 and F(3, 7) < F(25, 56) < F(26, 56) < F(4, 7) and 200 == 2**3*5**2
assert math.isqrt(10**2 - 8**2) == 6 and 16**2/4 == 64
assert F(2142855, 999999) == F(15, 7)
assert 18+42+36+24 == 120 and 8+22+15+5 == 50 and 20+5*0 == 20
assert (-7-2)**2+25 == (-7+2)**2+81 == 106
assert math.isqrt(45*36*5*4) == 180 and 45 == (9+40+41)//2
assert math.isqrt(66*55*6*5) == 330 and math.isqrt(30*20*6*4) == 120
assert 5*12*13 and 60//30 == 2 and (10, 24, 26) == (5*2, 12*2, 13*2)
assert (294-105)//7+1 == 28 and 28*(105+294)//2 == 5586 and 105 % 7 == 0 and 294 % 7 == 0 and 98 % 7 == 0 and 301 % 7 == 0
assert 60+180+120+40 == 400 and 5+7+8 == 20
assert 5*13 == 65 and 2*(5+13) == 36 and 2*5**2+3*5 == 65
assert 500+300*4 == 1700 and 500+300*10 == 3500 and 500+300*7 == 2600
assert 8*7 == 56 and 3**2+9*3+20 == 56 and 10**2+90+20 == 210 and (3+4, 3+5) == (7, 8) and 2*(7+8) == 30
assert 180-95 == 85 and 180-100 == 80 and 180-85 == 95 and math.isqrt(25**2-15**2) == 20 and 2*math.isqrt(25**2-15**2) == 40 and 25**2-20**2 == 225
assert (-1)**4*(3*4-2) == 10
A = [
 mc("The point on the y-axis, 5 units below the x-axis, is:", "(0, −5)", ["(−5, 0)", "(5, 0)", "(0, 5)"], "On the y-axis abscissa = 0; below ⇒ ordinate −5."),
 mc("The point (−3, −8) lies in the:", "third quadrant", ["first quadrant", "second quadrant", "fourth quadrant"], "Both coordinates are negative."),
 mc("The distance of the point (−5, 12) from the origin is:", "13 units", ["17 units", "7 units", "√119 units"], "√(25 + 144) = 13."),
 mc("The degree of the polynomial 2x⁵ − x³ + 9 is:", "5", ["3", "9", "2"], "Highest power of x is 5."),
 mc("The length and breadth of a rectangle are (x + 4) and (x − 1) respectively. Its area is:", "x² + 3x − 4", ["x² − 4", "2x + 6", "x² + 5x − 4"], "(x + 4)(x − 1) = x² + 3x − 4."),
 mc("A linear polynomial p(x) satisfies p(0) = 3 and p(2) = 7. Then p(x) is:", "2x + 3", ["3x + 2", "x + 5", "2x − 3"], "p(0) = 3 ⇒ constant 3; p(2) = 7 ⇒ 2a + 3 = 7 ⇒ a = 2."),
 mc("Which of the following is an irrational number?", fr("√2", 2), ["0.333… (3 repeating)", "√1.69", fr(22, 7)], "√2/2 = 1/√2 is irrational; √1.69 = 1.3 and the others are rational."),
 mc("The value of |−3.5| + |2.5| is:", "6", ["1", "−1", "−6"], "3.5 + 2.5 = 6."),
 mc("Which of the following rational numbers lies between " + fr(3, 5) + " and " + fr(4, 5) + "?", fr(7, 10), [fr(1, 2), fr(9, 10), fr(4, 5)], "3/5 = 0.6 &lt; 0.7 &lt; 0.8 = 4/5."),
 mc("The factorisation of x² + 10x + 25 is:", "(x + 5)²", ["(x − 5)²", "(x + 25)(x + 1)", "(x + 5)(x − 5)"], "x² + 2(x)(5) + 5²."),
 mc("If x + y = 8 and xy = 12, then x² + y² is equal to:", "40", ["64", "20", "52"], "x² + y² = (x + y)² − 2xy = 64 − 24 = 40."),
 mc("In the figure ABCD is a cyclic quadrilateral with ∠ABC = 95°. Then ∠ADC is:", "85°", ["95°", "75°", "170°"], "Opposite angles are supplementary: 180° − 95° = 85°.", fig=f12),
 mc("A chord of a circle of radius 13 cm is at a distance of 12 cm from the centre. The length of the chord is:", "10 cm", ["5 cm", "25 cm", "12 cm"], "Half chord = √(169 − 144) = 5 ⇒ chord = 10 cm."),
 mc("The area of a triangle with sides 9 cm, 40 cm and 41 cm is:", "180 cm²", ["360 cm²", "90 cm²", "369 cm²"], "s = 45; area = √(45 × 36 × 5 × 4) = √32400 = 180."),
 mc("The sides of a triangular field are in the ratio 3 : 5 : 7 and its perimeter is 150 m. The shortest side is:", "30 m", ["50 m", "10 m", "45 m"], "One part = 150 ÷ 15 = 10 m; 3 × 10 = 30 m."),
 mc("A bag has 3 red, 5 blue and 2 green balls. A ball is drawn at random. The probability that it is not blue is:", fr(1, 2), [fr(1, 5), fr(3, 10), fr(1, 10)], "Not blue = 3 + 2 = 5 out of 10."),
 mc("A number is chosen at random from the numbers 1 to 20. The probability that it is a multiple of 5 is:", fr(1, 5), [fr(1, 4), fr(1, 20), fr(3, 20)], "5, 10, 15, 20 ⇒ 4/20."),
 mc("If u<sub>n</sub> = (−1)<sup>n</sup>(3n − 2), then u₄ is:", "10", ["−10", "14", "−14"], "(−1)⁴ × 10 = 10."),
 ar("The number 0.1010010001… (with increasing number of zeros) is an irrational number.", "A non-terminating and non-repeating decimal is an irrational number.", 'a', "The decimal never ends and has no repeating block, so it is irrational; R states the reason."),
 ar("The polynomial 3x − 5 has exactly one zero.", "A linear polynomial ax + b (a ≠ 0) has exactly one zero, which is −b/a.", 'a', "Zero = 5/3; R is the general result."),
]
B = [
 sa("A cab charges ₹60 for the first 2 km and ₹12 for every additional km. Find the fare for a journey of 15 km.", 2, "Additional distance = 13 km (½); extra charge = 13 × 12 = ₹156 (1); fare = 60 + 156 = <b>₹216</b> (½)"),
 OR(sa("Without actual division, decide whether " + fr(27, 200) + " has a terminating decimal expansion. If it does, find the number of decimal places.", 2, "200 = 2³ × 5² ⇒ terminating (1). Decimal places = greater of the powers 3 and 2 = <b>3</b> (1)."),
    sa("Find two rational numbers between " + fr(3, 7) + " and " + fr(4, 7) + ".", 2, "3/7 = 24/56 and 4/7 = 32/56 (1). Two rational numbers: <b>25/56 and 26/56</b> (1). Any two valid numbers.")),
 sa("Factorise: 4x² − 20xy + 25y².", 2, "= (2x)² − 2(2x)(5y) + (5y)² (1) = <b>(2x − 5y)²</b> (1)"),
 sa("In the figure, O is the centre of the circle, chord AB = 16 cm and OM ⊥ AB with OM = 6 cm. Find the radius of the circle.", 2, "OM ⊥ AB bisects the chord: AM = 8 cm (1)<br>OA² = OM² + AM² = 36 + 64 = 100 ⇒ <b>radius = 10 cm</b> (1)", fig=f24),
 sa("Find the second, third and fourth terms of the sequence defined by t₁ = 1 and t<sub>n</sub> = t<sub>n−1</sub> + 2n for n ≥ 2.", 2, "t₂ = 1 + 4 = 5, t₃ = 5 + 6 = 11, t₄ = 11 + 8 = 19. (1 method, 1 values)"),
]
C = [
 sa("Show that 2.142857142857… = " + fr(15, 7) + ".", 3, "Let x = 2.142857142857…; six digits repeat ⇒ 10⁶x = 2142857.142857… (1)<br>10⁶x − x = 2142855 ⇒ 999999x = 2142855 (1)<br>x = 2142855/999999 = <b>15/7</b> (dividing by 142857) (1)"),
 OR(sa("A shopkeeper sold 120 shirts:" + htable(["Size", "S", "M", "L", "XL"], ["Shirts sold", 18, 42, 36, 24]) + "One shirt is chosen at random from those sold. Find the probability that it is of size (i) M, (ii) L or XL, (iii) not S.", 3, "(i) 42/120 = <b>7/20</b> (1) (ii) 60/120 = <b>1/2</b> (1) (iii) 102/120 = <b>17/20</b> (1)"),
    sa("The number of siblings of 50 students was recorded:" + htable(["Siblings", 0, 1, 2, 3], ["Students", 8, 22, 15, 5]) + "A student is chosen at random. Find the probability that the student has (i) exactly one sibling, (ii) at least two siblings, (iii) no sibling.", 3, "(i) 22/50 = <b>11/25</b> (1) (ii) (15 + 5)/50 = <b>2/5</b> (1) (iii) 8/50 = <b>4/25</b> (1)")),
 sa("Find the coordinates of the point on the x-axis which is equidistant from A(2, −5) and B(−2, 9).", 3, "Let the point be P(x, 0). PA² = (x − 2)² + 25, PB² = (x + 2)² + 81 (1)<br>PA = PB ⇒ x² − 4x + 29 = x² + 4x + 85 (1) ⇒ 8x = −56 ⇒ x = −7. Point = <b>(−7, 0)</b> (1)"),
 sa("Factorise: x³ + 6x² + 12x + 8.", 3, "x³ + 3·x²·2 + 3·x·2² + 2³ (1) = (x + 2)³ (identity (a + b)³ = a³ + 3a²b + 3ab² + b³) (1) = <b>(x + 2)(x + 2)(x + 2)</b> (1)"),
 sa("AB and CD are equal chords of a circle with centre O. OM ⊥ AB and ON ⊥ CD. Prove that OM = ON.", 3, "The perpendicular from the centre bisects a chord ⇒ AM = ½AB, CN = ½CD ⇒ AM = CN (1)<br>In right triangles OMA and ONC: OA = OC (radii), AM = CN ⇒ △OMA ≅ △ONC (RHS) (1) ⇒ <b>OM = ON</b> (CPCT) (1)"),
 OR(sa("A triangular plot has sides 11 m, 60 m and 61 m. Find its area using Heron’s formula.", 3, "s = 66 (1); area = √(66 × 55 × 6 × 5) (1) = √108900 = <b>330 m²</b> (1)"),
    sa("The sides of a triangle are in the ratio 5 : 12 : 13 and its perimeter is 60 cm. Find its area.", 3, "Sides 10, 24, 26 cm (1); s = 30; area = √(30 × 20 × 6 × 4) (1) = √14400 = <b>120 cm²</b> (1)")),
]
D = [
 sa("The corners of a rhombus-shaped garden are A(0, 3), B(4, 0), C(0, −3) and D(−4, 0) on a grid.<br>(a) Plot the points and join them in order. (2 marks)<br>(b) Find the lengths AB, BC, CD and DA. (1½ marks)<br>(c) Find the lengths of the diagonals and justify that ABCD is a rhombus but not a square. (1½ marks)", 5,
    "(a) Plotting (1½) + joining (½):" + sol32 + "(b) AB = √(16 + 9) = 5; BC = √(16 + 9) = 5; CD = 5; DA = 5 (1½)<br>(c) AC = 6, BD = 8 (½). All sides equal ⇒ rhombus; diagonals unequal ⇒ not a square (1)"),
 sa("Find how many natural numbers between 100 and 300 are multiples of 7, and find their sum. (2½ + 2½)", 5, "Numbers: 105, 112, …, 294 — AP with a = 105, d = 7, l = 294 (1)<br>n = (294 − 105)/7 + 1 = <b>28</b> (1½)<br>Sum = 28/2 × (105 + 294) = 14 × 399 = <b>5586</b> (2½)"),
 OR(sa("In a survey of 400 families, the number of vehicles owned was recorded:" + htable(["Vehicles", "0", "1", "2", "3 or more"], ["Families", 60, 180, 120, 40]) + "A family is chosen at random. Find the probability that it owns (i) no vehicle (1), (ii) exactly 2 vehicles (2), (iii) at least one vehicle (2).", 5, "(i) 60/400 = <b>3/20</b> (1) (ii) 120/400 = <b>3/10</b> (2) (iii) 340/400 = <b>17/20</b> (2)"),
    sa("A box contains 5 green, 7 yellow and 8 purple candies. One candy is drawn at random. Find the probability that it is (i) green (1), (ii) yellow or purple (2), (iii) neither green nor yellow (2).", 5, "Total = 20. (i) 5/20 = <b>1/4</b> (1) (ii) 15/20 = <b>3/4</b> (2) (iii) 8/20 = <b>2/5</b> (2)")),
 OR(sa("The length of a rectangular garden is 3 m more than twice its breadth, and its area is 65 m². Form an equation in the breadth x, solve it by factorisation and find the perimeter of the garden.", 5, "Breadth = x, length = 2x + 3 ⇒ x(2x + 3) = 65 ⇒ 2x² + 3x − 65 = 0 (1½)<br>2x² − 10x + 13x − 65 = (x − 5)(2x + 13) = 0 (1½) ⇒ x = 5 (negative rejected) (1)<br>Length = 13 m; perimeter = 2(5 + 13) = <b>36 m</b> (1)"),
    sa("A student arranges 2 square tiles of side x units, 7 rectangular strips (x units by 1 unit) and 6 small square tiles (1 unit by 1 unit) to form one rectangle. Find its length and breadth in terms of x and its perimeter when x = 3.", 5, "Area = 2x² + 7x + 6 (1)<br>= 2x² + 4x + 3x + 6 = 2x(x + 2) + 3(x + 2) = <b>(2x + 3)(x + 2)</b> (2)<br>Length = 2x + 3, breadth = x + 2 (1). For x = 3: 9 and 5 ⇒ perimeter = 2(9 + 5) = <b>28 units</b> (1)")),
]
assert 2*(9+5) == 28 and 2*3**2 == 18
E_ = [
 case("A gym charges a one-time joining fee of ₹500 and ₹300 per month. The total amount paid (in ₹) after m months is C = 500 + 300m.",
      [sub("What is the total amount paid after 4 months?", 1, "C = 500 + 1200 = <b>₹1700</b>"),
       sub("State the degree of C = 500 + 300m and its constant term.", 1, "Degree = <b>1</b> (linear polynomial); constant term = <b>500</b> (joining fee)."),
       OR(sub("After how many months will the total amount paid be ₹3500?", 2, "500 + 300m = 3500 (1) ⇒ m = <b>10 months</b> (1)"),
          sub("Find the total amount after 7 months. Does the situation show linear growth or linear decay? Why?", 2, "C = 500 + 2100 = <b>₹2600</b> (1). The amount increases at a constant rate (coefficient 300 &gt; 0) ⇒ linear growth (1)"))]),
 case("The area of a rectangular tabletop in a school workshop is given by the polynomial x² + 9x + 20 square units, where x is a positive number.",
      [sub("Factorise x² + 9x + 20.", 1, "x² + 4x + 5x + 20 = (x + 4)(x + 5)"),
       sub("If the breadth of the tabletop is (x + 4) units, write its length.", 1, "Length = <b>(x + 5) units</b>"),
       OR(sub("Find the perimeter of the tabletop when x = 3.", 2, "Length = 8, breadth = 7 (1) ⇒ perimeter = 2(8 + 7) = <b>30 units</b> (1)"),
          sub("Using the polynomial, find the area when x = 10. Verify with (x + 4)(x + 5).", 2, "100 + 90 + 20 = <b>210</b> (1); 14 × 15 = 210 ✓ (1)"))]),
 case("A circular running track has four floodlight poles P, Q, R and S on its boundary, forming a cyclic quadrilateral PQRS. ∠PQR = 100° and ∠QPS = 85°. The diameter of the track is 50 m.",
      [sub("Find ∠PSR.", 1, "Opposite angles of a cyclic quadrilateral are supplementary ⇒ ∠PSR = 180° − 100° = <b>80°</b>"),
       sub("Find ∠QRS.", 1, "∠QRS = 180° − ∠QPS = 180° − 85° = <b>95°</b>"),
       OR(sub("A straight path 40 m long is a chord of the track. Find its distance from the centre.", 2, "r = 25 m; half chord = 20 (½). d = √(25² − 20²) (1) = <b>15 m</b> (½)"),
          sub("Another straight path is a chord at a distance of 20 m from the centre. Find its length.", 2, "Half chord = √(25² − 20²) = 15 (1) ⇒ length = <b>30 m</b> (1)"))], fig=f38),
]
SECTIONS = sections(A, B, C, D, E_)
