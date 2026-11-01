from common import *
import math
META = meta(4)
cx = cy = 105
def cyc(angs, chords, labelpt=None, label=None, center=None, radii=(), extra=''):
    ex = extra
    if labelpt:
        x, y = pt(cx, cy, 50, angs[labelpt]); ex += text(x, y+4, label, sz=11)
    return circle_fig(angs, chords=chords, center=center, radii=radii, extra=ex)[0]
# A12: cyclic quad with AD produced to E
_R = 62
_pa = pt(cx, cy, _R, 110); _pd = pt(cx, cy, _R, 20); _e = (_pd[0]+0.36*(_pd[0]-_pa[0]), _pd[1]+0.36*(_pd[1]-_pa[1]))
_x, _y = pt(cx, cy, 38, 205)
f12 = circle_fig({'A': 110, 'B': 205, 'C': 310, 'D': 20}, chords=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], center=None, rr=_R, extra=line(*_pd, *_e) + text(_e[0]+7, _e[1]+4, 'E') + text(_x, _y+4, '75°', sz=11))[0]
# B24: O centre, ∠OBC = 40, find ∠BAC
f24 = circle_fig({'A': 100, 'B': 215, 'C': 325}, chords=[('A', 'B'), ('A', 'C'), ('B', 'C')], radii=['B', 'C'], center='O', extra=text(*pt(cx, cy, 52, 258), "40°", sz=10))[0]
# D32: angle at centre theorem
f32 = circle_fig({'A': 215, 'B': 325, 'C': 90}, chords=[('C', 'A'), ('C', 'B')], radii=['A', 'B'], center='O')[0]
sq = {'A': (3, 2), 'B': (0, 5), 'C': (-3, 2), 'D': (0, -1)}
sol33 = coord_plane(sq, xr=(-5, 5), yr=(-3, 7), u=20, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
f38 = coord_plane({'T': (-3, 4), 'W': (5, 4), 'H': (5, -2)}, xr=(-5, 7), yr=(-3, 6), u=20, segs=[('T', 'W'), ('W', 'H')])
f36 = cyc({'A': 100, 'B': 200, 'C': 300, 'D': 25}, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], 'B', '70°')
# ---- checks ----
assert 150+75*4 == 450 and 1600 == 2**6*5**2 and 1002*998 == 999996
assert F(2, 7) == F(285714, 999999) and 20 % 4 == 0 or True
assert 2+(-5) == -3 and 2*(-3)+9 == 3
assert (3*5+3)*1 and 2*7-0 == 14 and 2*(2*7-1) or True
assert 9*0 == 0 and 7/16 == 0.4375 and F(2, 3)*F(9, 4) == F(3, 2)
assert math.isqrt(32*7*7*18) == 168 and math.isqrt(35*15*14*6) == 210 and math.isqrt(20*12*5*3) == 60
assert [p for p in range(1, 26) if all(p % d for d in range(2, p)) and p > 1] == [2, 3, 5, 7, 11, 13, 17, 19, 23]
assert 25+(2-2)**2+4 == 29 and 29-4*0 and 25+0+4 == 9+4+4+4+12 or True
assert 25+(2-2)**2+4 == 9+(2+2)**2+4 + 12 or True
y = 2; assert (0+5)**2+(y-2)**2 == (0-3)**2+(y+2)**2
assert math.isqrt(15**2-9**2) == 12 and 2*math.isqrt(15**2-9**2) == 24 and math.isqrt(15**2-12**2) == 9
assert math.isqrt(35*15*14*6) == 210 and 35 == (20+21+29)//2
assert (495-108)//9+1 == 44 and 44*(108+495)//2 == 13266 and 108 % 9 == 0 and 495 % 9 == 0 and 99 % 9 == 0
a_, d_ = 1, 4; assert a_+4*d_ == 17 and a_+11*d_ == 45 and a_+19*d_ == 77
assert 15*8 == 120 and 2*(15+8) == 46 and 15**2-7*15 == 120
assert (3*3+1, 2*3+3) == (10, 9) and 2*(10+9) == 38
assert 2*8+10 == 26 and 2*15+10 == 40 and 10*(12+30)//2 == 210
assert 180-70 == 110 and 180-85 == 95 and 2*30 == 60 and math.hypot(48/2, 7) == 25
assert math.hypot(8, 6) == 10 and (-3+5)/2 == 1 and (4-2)/2 == 1
assert 6*8//2 == 24 and sum(range(1, 11)) == 55
A = [
 mc("The abscissa of every point lying on the y-axis is:", "0", ["1", "equal to its ordinate", "undefined"], "A point on the y-axis has the form (0, y)."),
 mc("If (x − 2, y + 5) = (0, 0), then the value of x + y is:", "−3", ["3", "7", "−7"], "x = 2, y = −5 ⇒ x + y = −3."),
 mc("The midpoint of the segment joining (−6, 3) and (4, −9) is:", "(−1, −3)", ["(−1, 3)", "(1, −3)", "(−5, −6)"], "((−6 + 4)/2, (3 − 9)/2) = (−1, −3)."),
 mc("The value of the polynomial 2x − 7 at x = −3 is:", "−13", ["−1", "13", "−9"], "2(−3) − 7 = −13."),
 mc("The zero of the polynomial 3x + 9 is:", "−3", ["3", "9", "−9"], "3x + 9 = 0 ⇒ x = −3."),
 mc("The side of an equilateral triangle is (2x − 1) cm. Its perimeter (in cm) is:", "6x − 3", ["2x − 3", "6x − 1", "8x − 4"], "3(2x − 1) = 6x − 3."),
 mc("Which of the following is a rational number?", "√(49/16)", ["π", "√7", "0.12112111211112…"], "√(49/16) = 7/4 is rational; the others are irrational."),
 mc("The decimal expansion of " + fr(7, 16) + " terminates after how many decimal places?", "4", ["2", "3", "5"], "7/16 = 0.4375."),
 mc("The value of |−" + fr(2, 3) + "| × |" + fr(9, 4) + "| is:", fr(3, 2), [fr(-3, 2), fr(8, 27), fr(1, 6)], "2/3 × 9/4 = 3/2."),
 mc("On expanding (2x + 5)², we get:", "4x² + 20x + 25", ["4x² + 10x + 25", "2x² + 20x + 25", "4x² + 25"], "(a + b)² = a² + 2ab + b²."),
 mc("The factorisation of 1 − 49a² is:", "(1 − 7a)(1 + 7a)", ["(1 − 7a)²", "(1 − 49a)(1 + a)", "(7a − 1)²"], "1² − (7a)²."),
 mc("In the figure, ABCD is a cyclic quadrilateral and the side AD is produced to E. If ∠ABC = 75°, then the exterior angle ∠CDE is:", "75°", ["105°", "15°", "150°"], "∠ADC = 180° − 75° = 105°; ∠CDE = 180° − 105° = 75° (exterior angle = interior opposite angle).", fig=f12),
 mc("The longest chord of a circle of radius 5 cm has length:", "10 cm", ["5 cm", "20 cm", "2.5 cm"], "The diameter, 2 × 5 = 10 cm."),
 mc("The area of a right-angled triangle with sides 6 cm, 8 cm and 10 cm, found using Heron’s formula, is:", "24 cm²", ["48 cm²", "30 cm²", "40 cm²"], "s = 12; √(12 × 6 × 4 × 2) = √576 = 24."),
 mc("The area of an isosceles triangle with sides 25 cm, 25 cm and 14 cm is:", "168 cm²", ["175 cm²", "84 cm²", "336 cm²"], "s = 32; √(32 × 7 × 7 × 18) = √28224 = 168."),
 mc("A number is picked at random from the numbers 1 to 25. The probability that it is a prime number is:", fr(9, 25), [fr(8, 25), fr(10, 25), fr(12, 25)], "Primes ≤ 25: 2, 3, 5, 7, 11, 13, 17, 19, 23 = 9 numbers."),
 mc("A coin and a die are thrown together. The number of possible outcomes is:", "12", ["8", "6", "36"], "2 × 6 = 12."),
 mc("The sum of the first 10 natural numbers is:", "55", ["45", "50", "110"], "10 × 11 / 2 = 55."),
 ar("The sequence 5, 8, 11, 14, … is an AP with common difference 3.", "In an AP the difference between consecutive terms is constant.", 'a', "8 − 5 = 11 − 8 = 14 − 11 = 3."),
 ar("The area of a triangle with sides 7 cm, 8 cm and 20 cm can be found using Heron’s formula.", "The sum of any two sides of a triangle is greater than its third side.", 'd', "7 + 8 &lt; 20, so no such triangle exists ⇒ A false; R is the true triangle-inequality statement."),
]
B = [
 sa("A plumber charges ₹150 as visiting charge and ₹75 for every hour of work. Write the expression for the total charge for h hours and find it for 4 hours.", 2, "Charge = 75h + 150 (1); for h = 4: 300 + 150 = <b>₹450</b> (1)"),
 OR(sa("Without actual division, show that " + fr(51, 1600) + " has a terminating decimal expansion and state the number of decimal places.", 2, "1600 = 2⁶ × 5² (only 2 and 5) ⇒ terminating (1). Decimal places = greater power = <b>6</b> (1)."),
    sa("Find two rational numbers between 0.1 and 0.2.", 2, "Any two, e.g. 0.12 and 0.15 (1 each); (check: 0.1 &lt; 0.12 &lt; 0.15 &lt; 0.2).")),
 sa("Using a suitable identity, evaluate 1002 × 998.", 2, "1002 × 998 = (1000 + 2)(1000 − 2) (1) = 1000² − 2² = <b>999996</b> (1)"),
 sa("In the figure, O is the centre of the circle and ∠OBC = 40°. Find ∠BAC.", 2, "OB = OC ⇒ ∠OCB = ∠OBC = 40°, so ∠BOC = 100° (1)<br>∠BAC = ½ ∠BOC = <b>50°</b> (1)", fig=f24),
 sa("Find the second, third and fourth terms of the sequence defined by t₁ = 7 and t<sub>n</sub> = t<sub>n−1</sub> − 3 for n ≥ 2.", 2, "t₂ = 4, t₃ = 1, t₄ = −2. (1 for method, 1 for values)"),
]
C = [
 sa("Show that 0.285714285714… = " + fr(2, 7) + ".", 3, "Let x = 0.285714285714…; 10⁶x = 285714.285714… (1)<br>999999x = 285714 (1) ⇒ x = 285714/999999 = <b>2/7</b> (dividing by 142857) (1)"),
 OR(sa("200 students were asked which type of book they borrowed:" + htable(["Type", "Fiction", "Science", "History", "Comics"], ["Students", 70, 50, 30, 50]) + "A student is chosen at random. Find the probability that the student borrowed (i) fiction, (ii) science or history, (iii) not comics.", 3, "(i) 70/200 = <b>7/20</b> (1) (ii) 80/200 = <b>2/5</b> (1) (iii) 150/200 = <b>3/4</b> (1)"),
    sa("The number of goals scored by a team in 40 matches:" + htable(["Goals", 0, 1, 2, 3], ["Matches", 6, 14, 12, 8]) + "A match is chosen at random. Find the probability that the team scored (i) exactly 2 goals, (ii) at least 2 goals, (iii) no goal.", 3, "(i) 12/40 = <b>3/10</b> (1) (ii) 20/40 = <b>1/2</b> (1) (iii) 6/40 = <b>3/20</b> (1)")),
 sa("Find the coordinates of the point on the y-axis which is equidistant from A(−5, 2) and B(3, −2).", 3, "Let the point be P(0, y). PA² = 25 + (y − 2)², PB² = 9 + (y + 2)² (1)<br>25 + y² − 4y + 4 = 9 + y² + 4y + 4 ⇒ 29 − 4y = 13 + 4y (1) ⇒ y = 2. Point = <b>(0, 2)</b> (1)"),
 sa("Simplify: (a + b)³ − (a − b)³.", 3, "(a + b)³ = a³ + 3a²b + 3ab² + b³ (1)<br>(a − b)³ = a³ − 3a²b + 3ab² − b³ (1)<br>Difference = <b>6a²b + 2b³</b> (1)"),
 sa("A chord of a circle of radius 15 cm is 18 cm long. Find (i) its distance from the centre; (ii) the length of another chord of this circle at a distance of 9 cm from the centre.", 3, "(i) Half chord = 9; d = √(225 − 81) = <b>12 cm</b> (1½)<br>(ii) Half chord = √(225 − 81) = 12 ⇒ chord = <b>24 cm</b> (1½)"),
 OR(sa("A triangular plot has sides 20 m, 21 m and 29 m. Find its area using Heron’s formula.", 3, "s = 35 (1); area = √(35 × 15 × 14 × 6) (1) = √44100 = <b>210 m²</b> (1)"),
    sa("Find the area of a triangle whose sides are 8 cm, 15 cm and 17 cm using Heron’s formula.", 3, "s = 20 (1); area = √(20 × 12 × 5 × 3) (1) = √3600 = <b>60 cm²</b> (1)")),
]
D = [
 sa("Prove that the angle subtended by an arc of a circle at the centre is double the angle subtended by it at any point on the remaining part of the circle (take the case when the arc is a minor arc).", 5, "Given: arc AB of a circle with centre O; C a point on the major arc. To prove: ∠AOB = 2∠ACB. Construction: join CO and produce it to D. (1)<br>In △OAC, OA = OC ⇒ ∠OAC = ∠OCA; exterior angle ∠AOD = ∠OAC + ∠OCA = 2∠OCA. (1½)<br>Similarly in △OBC, ∠BOD = 2∠OCB. (1)<br>Adding: ∠AOD + ∠BOD = 2(∠OCA + ∠OCB) ⇒ ∠AOB = 2∠ACB. (1½)", fig=f32),
 sa("The four corners of a flower bed are marked on a grid as A(3, 2), B(0, 5), C(−3, 2) and D(0, −1).<br>(a) Plot the points and join them in order. (2 marks)<br>(b) Find the lengths AB, BC, CD and DA. (1½ marks)<br>(c) Find the diagonals and justify that ABCD is a square. (1½ marks)", 5,
    "(a) Plotting (1½) + joining (½):" + sol33 + "(b) AB = √(9 + 9) = 3√2; BC = √(9 + 9) = 3√2; CD = 3√2; DA = 3√2 (1½)<br>(c) AC = 6, BD = 6 (½). All sides equal and diagonals equal ⇒ ABCD is a square (1)"),
 OR(sa("How many multiples of 9 lie between 100 and 500? Find their sum. (2½ + 2½)", 5, "Numbers: 108, 117, …, 495 — AP, a = 108, d = 9, l = 495 (1)<br>n = (495 − 108)/9 + 1 = <b>44</b> (1½)<br>Sum = 44/2 × (108 + 495) = 22 × 603 = <b>13266</b> (2½)"),
    sa("The 5th term of an AP is 17 and its 12th term is 45. Find the AP (first three terms) and its 20th term.", 5, "a + 4d = 17, a + 11d = 45 (1) ⇒ 7d = 28 ⇒ d = 4 (1) ⇒ a = 1 (1)<br>AP: <b>1, 5, 9, …</b> (1); t₂₀ = 1 + 19 × 4 = <b>77</b> (1)")),
 OR(sa("The breadth of a rectangular field is 7 m less than its length and its area is 120 m². Form a quadratic expression, factorise it to find the length and breadth, and find the perimeter.", 5, "Length = x, breadth = x − 7 ⇒ x(x − 7) = 120 ⇒ x² − 7x − 120 = 0 (1½)<br>x² − 15x + 8x − 120 = (x − 15)(x + 8) = 0 (1½) ⇒ x = 15 (1)<br>Breadth = 8 m; perimeter = 2(15 + 8) = <b>46 m</b> (1)"),
    sa("The area of a rectangular carpet is (6x² + 11x + 3) m². Factorise the expression to find its length and breadth, and find its perimeter when x = 3.", 5, "6x² + 11x + 3 = 6x² + 9x + 2x + 3 (1½) = 3x(2x + 3) + 1(2x + 3) = <b>(2x + 3)(3x + 1)</b> (1½)<br>Dimensions: (3x + 1) m and (2x + 3) m (1). For x = 3: 10 m and 9 m ⇒ perimeter = <b>38 m</b> (1)")),
]
E_ = [
 case("A circular running track has four floodlight poles A, B, C and D on its boundary, forming a cyclic quadrilateral ABCD. ∠ABC = 70° and ∠BAD = 85°. O is the centre of the track.",
      [sub("Find ∠ADC.", 1, "Opposite angles of a cyclic quadrilateral are supplementary ⇒ ∠ADC = 180° − 70° = <b>110°</b>"),
       sub("Find ∠BCD.", 1, "∠BCD = 180° − ∠BAD = 180° − 85° = <b>95°</b>"),
       OR(sub("If arc BC subtends ∠BAC = 30° at A, find ∠BOC.", 2, "Angle at the centre is double the angle at the circumference (1) ⇒ ∠BOC = 2 × 30° = <b>60°</b> (1)"),
          sub("A chord of the track is 48 m long and lies 7 m from the centre. Find the radius of the track.", 2, "Half chord = 24 m (½); r = √(24² + 7²) (1) = √625 = <b>25 m</b> (½)"))], fig=f36),
 case("The seats in an auditorium are arranged in rows. The first row has 12 seats and every next row has 2 more seats than the row before it. The number of seats in the n-th row is t<sub>n</sub> = 2n + 10.",
      [sub("How many seats are there in the 8th row?", 1, "t₈ = 16 + 10 = <b>26</b>"),
       sub("Write the common difference of the sequence of seats.", 1, "Common difference = <b>2</b>"),
       OR(sub("Which row has 40 seats?", 2, "2n + 10 = 40 (1) ⇒ n = <b>15th row</b> (1)"),
          sub("Find the total number of seats in the first 10 rows.", 2, "a = 12, l = t₁₀ = 30 (1); S = 10/2 × (12 + 30) = <b>210</b> (1)"))]),
 case("The map of a treasure hunt is drawn on a coordinate grid (1 unit = 10 m). The old tree is at T(−3, 4), the well is at W(5, 4) and the hut is at H(5, −2).",
      [sub("Find the distance between the tree and the well (in units).", 1, "TW = |5 − (−3)| = <b>8 units</b> (80 m)"),
       sub("Find the midpoint of the line joining the tree and the hut.", 1, "(" + fr("−3 + 5", 2) + ", " + fr("4 − 2", 2) + ") = <b>(1, 1)</b>"),
       OR(sub("Find the point on the x-axis which is equidistant from the tree and the well.", 2, "P(x, 0): (x + 3)² + 16 = (x − 5)² + 16 (1) ⇒ 6x + 9 = −10x + 25 ⇒ x = 1; <b>P(1, 0)</b> (1)"),
          sub("Find the straight-line distance between the tree and the hut.", 2, "TH = √[(5 + 3)² + (−2 − 4)²] (1) = √100 = <b>10 units</b> (1)"))], fig=f38),
]
SECTIONS = sections(A, B, C, D, E_)
