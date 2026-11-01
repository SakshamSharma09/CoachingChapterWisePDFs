from cm import *
import math
META = meta(3)

# ---------- figures ----------
f6, _ = circle_fig({'A': 230, 'B': 310}, chords=[('A', 'B')], radii=['A', 'B'], extra=text(64, 142, "50°", sz=10))
T = {'A': (125, 12), 'B': (20, 140), 'C': (230, 140)}
mid = lambda p, q: ((p[0]+q[0])/2, (p[1]+q[1])/2)
T.update({'F': mid(T['A'], T['B']), 'E': mid(T['A'], T['C']), 'D': mid(T['B'], T['C'])})
f25 = gfig(T, [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E'), ('E', 'F'), ('F', 'D')], w=250, h=165,
           off={'A': (0, -4), 'B': (-10, 12), 'C': (10, 12), 'D': (0, 14), 'E': (12, 0), 'F': (-12, 0)})
Q = {'A': (30, 120), 'B': (70, 20), 'C': (215, 45), 'D': (190, 140)}
Mq = {k: mid(Q[a], Q[b]) for k, (a, b) in {'P': ('A', 'B'), 'Q': ('B', 'C'), 'R': ('C', 'D'), 'S': ('D', 'A')}.items()}
f38 = gfig({**Q, **Mq}, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], w=250, h=165, off={'A': (-10, 10), 'B': (-6, -6), 'C': (10, -4), 'D': (10, 12), 'P': (-12, 0), 'Q': (4, -8), 'R': (12, 4), 'S': (0, 14)},
            extra=line(*Mq['P'], *Mq['Q'], '#c9a227', 1.8) + line(*Mq['Q'], *Mq['R'], '#c9a227', 1.8) + line(*Mq['R'], *Mq['S'], '#c9a227', 1.8) + line(*Mq['S'], *Mq['P'], '#c9a227', 1.8)
            + line(*Q['A'], *Q['C'], '#888', 1, '4,3') + line(*Q['B'], *Q['D'], '#888', 1, '4,3'))
ch_pts = {'A': 143.1, 'B': 36.9}   # chord 16 at distance 6 for r = 10  (angle where sin = 0.6)
u = 80/10
_, _P = circle_fig(ch_pts, center='O')
f37 = circle_fig(ch_pts, chords=[('A', 'B')], center='O', extra=line(105, 105, 105, 105-6*u, '#0f2347') + dot(105, 105-6*u, 'M', 5, 14) + text(118, 85, "6 m", 'start', 10) + text(105, 105-6*u-7, "16 m", sz=10))[0]

# ---------- numeric verification ----------
assert math.dist((-8, 15), (0, 0)) == 17 and 7**2 - 2*10 == 29 and 2**6 == 64 and 6+8+10 == 24 and math.isqrt(12*6*4*2) == 24
assert 3+7+11+15+19 == 55 and 5*(6+16)//2 == 55
assert (50*1+60*2+80*7)/10 == 73 and (100*5+300*15)/400 == 12.5
assert 2*3+3 == 9 and 5*3-6 == 9 and 12/2 == 6 and 18/2 == 9 and 2*(6+9) == 30
assert (12+16+10)/2 == 19
assert F(285, 90) == F(19, 6)
assert 3+4+5 == 12 and F(4, 12) == F(1, 3) and F(7, 12) == F(7, 12) and F(7, 12) == F(3+4, 12)
assert 18+20+8+4 == 50 and F(18, 50) == F(9, 25) and F(12, 50) == F(6, 25) and F(38, 50) == F(19, 25)
assert math.dist((0,0),(3,4)) == 5 == math.dist((6,0),(3,4))
assert 6000+4500+3000+1500 == 15000 and 6000/150 == 40 and 4500/150 == 30 and 3000/150 == 20
assert math.isqrt(100-64) == 6 and math.isqrt(100-36) == 8 and 8-6 == 2
assert math.isqrt(27*(27-21)*(27-20)*(27-13)) == 126
Pk = {'A': (-4, 1), 'B': (2, 1), 'C': (0, 5), 'D': (-2, 5)}
assert math.dist(Pk['A'], Pk['D']) == math.dist(Pk['B'], Pk['C']) == math.sqrt(20) and 0.5*(6+2)*4 == 16
d = [i for i in range(102, 600) if i % 6 == 0]; assert len(d) == 83 and sum(d) == 28884 and d[-1] == 594
assert 240+120+60+80 == 500 and F(240, 500) == F(120, 250) and F(380, 500) == F(19, 25) and F(140, 500) == F(7, 25)
assert (9*12+5*10+14*5)/19 == 12
assert 6*4+17*2+12 == 70 == 7*10 and 2*(7+10) == 34 and 8*9 == 72 and 8+9 == 17
assert 6**2 + 8**2 == 10**2 and 0.5*16*6 == 48 and math.isqrt(100-64) == 6 and 2*6 == 12
assert 30/2 == 15 and 40/2 == 20 and 2*(15+20) == 70
assert 45+30+25+20 == 120 and F(30, 120) == F(1, 4) and F(100, 120) == F(5, 6) and F(70, 120) == F(7, 12) and F(60, 150) == F(2, 5)

A = [
 mc("Which of the following points lies in the second quadrant?", "(−3, 4)", ["(3, −4)", "(−3, −4)", "(3, 4)"], "Second quadrant: x &lt; 0 and y &gt; 0."),
 mc("The distance of the point (−8, 15) from the origin is:", "17 units", ["23 units", "7 units", "13 units"], "d = √(64 + 225) = √289 = 17."),
 mc("A rectangle has length (3x + 2) cm and breadth (x − 1) cm. Its perimeter (in cm) is:", "8x + 2", ["4x + 1", "8x − 2", "4x + 3"], "P = 2[(3x + 2) + (x − 1)] = 2(4x + 1) = 8x + 2."),
 mc("Which of the following is a rational number?", "√(121/9)", ["√7", "π", "√3 + 1"], "√(121/9) = 11/3 is rational; √7, π and √3 + 1 are irrational."),
 mc("If a + b = 7 and ab = 10, then a² + b² is equal to:", "29", ["49", "39", "24"], "a² + b² = (a + b)² − 2ab = 49 − 20 = 29."),
 mc("In the figure, O is the centre of the circle and ∠OAB = 50°. Then ∠AOB is equal to:", "80°", ["100°", "50°", "130°"], "OA = OB ⇒ ∠OBA = 50°; ∠AOB = 180° − 100° = 80°.", fig=f6),
 mc("Two chords of a circle which are at the same distance from the centre are:", "equal in length", ["parallel", "diameters", "perpendicular to each other"], "Chords equidistant from the centre are equal."),
 mc("The area of a triangle with sides 6 cm, 8 cm and 10 cm, found using Heron’s formula, is:", "24 cm²", ["48 cm²", "30 cm²", "40 cm²"], "s = 12; area = √(12 × 6 × 4 × 2) = √576 = 24 cm²."),
 mc("A fair die is thrown once. The probability of getting a multiple of 3 is:", fr(1, 3), [fr(1, 6), fr(1, 2), fr(2, 3)], "Favourable outcomes 3 and 6 ⇒ 2/6 = 1/3."),
 mc("If t<sub>n</sub> = 2<sup>n</sup>, then t<sub>6</sub> is:", "64", ["12", "36", "32"], "2⁶ = 64."),
 mc("The converse of ‘If n is the square of a prime number, then n has exactly 3 factors’ is:", "If n has exactly 3 factors, then n is the square of a prime number.", ["If n is not the square of a prime, then n does not have exactly 3 factors.", "If n is a prime number, then n has exactly 3 factors.", "If n has exactly 3 factors, then n is a prime number."], "Interchange the ‘if’ and ‘then’ parts."),
 mc("A counterexample to the claim ‘4<sup>n</sup> + 3 is prime for every positive integer n’ is:", "n = 4", ["n = 1", "n = 2", "n = 3"], "4⁴ + 3 = 259 = 7 × 37. (n = 1, 2, 3 give 7, 19, 67, all prime.)"),
 mc("A student scores 50, 60 and 80 in three components which carry weights in the ratio 1 : 2 : 7. The weighted mean score is:", "73", ["63.3", "70", "75"], "(50 × 1 + 60 × 2 + 80 × 7)/(1 + 2 + 7) = 730/10 = 73."),
 mc("100 mL of a solution with 5% spice is mixed with 300 mL of a solution with 15% spice. The concentration of spice in the mixture is:", "12.5%", ["10%", "11%", "15%"], "(100 × 0.05 + 300 × 0.15)/400 = 50/400 = 12.5%."),
 mc("To find gcd(m, n) by searching for common divisors, it is enough to check numbers up to:", "min(m, n)", ["m + n", "max(m, n)", "m × n"], "A common divisor cannot be larger than the smaller of the two numbers."),
 mc("In a parallelogram ABCD, AB = (2x + 3) cm and CD = (5x − 6) cm. Then the length of AB is:", "9 cm", ["6 cm", "7 cm", "15 cm"], "Opposite sides are equal: 2x + 3 = 5x − 6 ⇒ x = 3 ⇒ AB = 9 cm."),
 mc("The diagonals of a quadrilateral ABCD are 12 cm and 18 cm. The perimeter of the parallelogram formed by joining the midpoints of its sides is:", "30 cm", ["60 cm", "15 cm", "45 cm"], "Sides of the Varignon parallelogram are half the diagonals: 6 cm and 9 cm ⇒ perimeter = 2(6 + 9) = 30 cm."),
 mc("The sum of the first five terms of the AP 3, 7, 11, … is:", "55", ["45", "65", "50"], "S₅ = 5/2 × [2(3) + 4(4)] = 5/2 × 22 = 55."),
 ar("The probability of an event can be 1.2.", "The probability of any event lies between 0 and 1, both inclusive.", 'd', "A is false because probability never exceeds 1; R is a true statement."),
 ar("A quadrilateral in which one pair of opposite sides is equal and parallel is a parallelogram.", "In such a quadrilateral the diagonals bisect each other.", 'a', "Both true: the congruent triangles formed by the diagonals show that they bisect each other, which makes the quadrilateral a parallelogram."),
]
B = [
 sa("An internet café charges ₹20 for the first hour and ₹12 for every additional hour. Write an expression for the charge for h hours (h ≥ 1) and find the charge for 5 hours.", 2, "Charge = 20 + 12(h − 1) (1)<br>For h = 5: 20 + 12 × 4 = <b>₹68</b> (1)"),
 OR(sa("Without actual division, decide whether " + fr(13, 60) + " has a terminating decimal expansion. Give a reason.", 2, "60 = 2² × 3 × 5 (1). The prime factor 3 is present, so the decimal expansion is <b>non-terminating (repeating)</b> (1)"),
    sa("Find two rational numbers between 0.75 and 0.8.", 2, "0.75 = 0.750 and 0.8 = 0.800 (1). Two numbers: <b>0.76 and 0.77</b> (any two correct numbers) (1)")),
 sa("Factorise: 27a³ + 54a²b + 36ab² + 8b³.", 2, "= (3a)³ + 3(3a)²(2b) + 3(3a)(2b)² + (2b)³ (1) = <b>(3a + 2b)³</b> (1)"),
 sa("Execute the ‘divisors’ algorithm (check every j from 1 to n and add j to the list if it divides n) for n = 24 and write the final list.", 2, "j = 1, 2, 3, 4, 6, 8, 12 and 24 divide 24; the others do not (1)<br>List = <b>[1, 2, 3, 4, 6, 8, 12, 24]</b> (1)"),
 sa("In the figure, D, E and F are the midpoints of BC, CA and AB. If AB = 12 cm, BC = 16 cm and CA = 10 cm, find the perimeter of △DEF.", 2, "EF = ½BC = 8, DE = ½AB = 6, DF = ½CA = 5 (Midpoint Theorem) (1)<br>Perimeter = 8 + 6 + 5 = <b>19 cm</b> (1)", fig=f25),
]
C = [
 sa("Express 3.1666… (6 repeating) in the form p/q in lowest terms.", 3, "x = 3.1666…; 10x = 31.666…, 100x = 316.666… (1)<br>100x − 10x: 90x = 285 (1)<br>x = 285/90 = <b>19/6</b> (1)"),
 OR(sa("A box contains 3 red, 4 blue and 5 yellow marbles. One marble is drawn at random. Find the probability that it is (i) blue, (ii) not yellow, (iii) red or blue.", 3, "Total = 12. (i) 4/12 = <b>1/3</b> (1) (ii) 7/12 (1) (iii) (3 + 4)/12 = <b>7/12</b> (1)"),
    sa("A bus ran late on some of the 50 days of a month. The minutes it was late are recorded:" + htable(["Minutes late", 0, 1, 2, 3], ["Days", 18, 20, 8, 4]) + "Find the probability that on a day chosen at random the bus was (i) on time, (ii) at least 2 minutes late, (iii) at most 1 minute late.", 3, "Total = 50. (i) 18/50 = <b>9/25</b> (1) (ii) (8 + 4)/50 = <b>6/25</b> (1) (iii) (18 + 20)/50 = <b>19/25</b> (1)")),
 sa("The vertices of a triangle are A(0, 0), B(6, 0) and C(3, 4). Show that the triangle is isosceles and find its area.", 3, "AB = 6; AC = √(3² + 4²) = 5; BC = √(3² + 4²) = 5 (1½)<br>AC = BC ⇒ <b>isosceles</b> (½)<br>Base AB = 6 and height = 4 (the y-coordinate of C) ⇒ area = ½ × 6 × 4 = <b>12 square units</b> (1)"),
 sa("The monthly expenses of a family are: food ₹6000, rent ₹4500, education ₹3000 and others ₹1500. Find the total expense and the percentage share of each item in a 100% stacked bar.", 3, "Total = ₹15000 (1)<br>Food = 6000/15000 × 100 = <b>40%</b>; rent = <b>30%</b>; education = <b>20%</b>; others = <b>10%</b> (2: ½ each + check that the shares add up to 100%)"),
 OR(sa("A chord AB of length 16 cm and a chord CD of length 12 cm are drawn in a circle of radius 10 cm. Find their distances from the centre and show that the longer chord is nearer the centre.", 3, "d(AB): half = 8 ⇒ d = √(100 − 64) = 6 cm (1)<br>d(CD): half = 6 ⇒ d = √(100 − 36) = 8 cm (1)<br>6 cm &lt; 8 cm, so the longer chord AB is nearer the centre (by 2 cm) (1)"),
    sa("Using Heron’s formula, find the area of a triangle with sides 13 cm, 20 cm and 21 cm.", 3, "s = (13 + 20 + 21)/2 = 27 cm (1)<br>Area = √[27 × 14 × 7 × 6] (1) = √15876 = <b>126 cm²</b> (1)")),
 sa("Prove that the opposite angles of a parallelogram are equal.", 3, "Let ABCD be a parallelogram, so AB ∥ DC and AD ∥ BC. (½)<br>AD ∥ BC with transversal AB: ∠A + ∠B = 180° (co-interior angles) (1)<br>AB ∥ DC with transversal BC: ∠B + ∠C = 180° (1)<br>Hence ∠A = ∠C. In the same way ∠B = ∠D. (½)"),
]
Pk2 = {'A': (-4, 1), 'B': (2, 1), 'C': (0, 5), 'D': (-2, 5)}
figD = coord_plane(Pk2, xr=(-6, 4), yr=(-1, 7), u=22, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
D = [
 sa("A shopkeeper draws the plan of a stall on a grid with corners A(−4, 1), B(2, 1), C(0, 5) and D(−2, 5).<br>(a) Plot the points and join them in order. (2 marks)<br>(b) Show that AB ∥ DC and that AD = BC. (1½ marks)<br>(c) Name the quadrilateral and find its area. (1½ marks)", 5,
    "(a) Plotting 4 points (1½), joining (½):" + figD + "(b) AB and DC are both horizontal (same y-coordinate) ⇒ AB ∥ DC. AD = √(2² + 4²) = √20; BC = √(2² + 4²) = √20 ⇒ AD = BC (1½)<br>(c) One pair of parallel sides and equal non-parallel sides: <b>isosceles trapezium</b> (½). Parallel sides 6 and 2, height 4 ⇒ area = ½(6 + 2) × 4 = <b>16 square units</b> (1)"),
 OR(sa("How many multiples of 6 lie between 100 and 600? Find their sum. (2½ + 2½)", 5, "Multiples: 102, 108, …, 594 — an AP with a = 102, d = 6, l = 594 (1)<br>n = (594 − 102)/6 + 1 = <b>83</b> (1½)<br>Sum = 83/2 × (102 + 594) = 83 × 348 = <b>28884</b> (2½)"),
    sa("A traffic survey recorded the vehicles passing a crossing in an hour:" + htable(["Vehicle", "Two-wheeler", "Car", "Bus", "Truck"], ["Number", 240, 120, 60, 80]) + "A vehicle is chosen at random. Find the probability that it is (i) a two-wheeler (1), (ii) not a car (2), (iii) a bus or a truck (2).", 5, "Total = 500. (i) 240/500 = <b>12/25</b> (1) (ii) 1 − 120/500 = 380/500 = <b>19/25</b> (2) (iii) (60 + 80)/500 = <b>7/25</b> (2)")),
 OR(sa("State and prove the Baudhāyana–Pythagoras converse: if a² + b² = c² for the sides of a triangle, then the triangle is right-angled.", 5, "Let △ABC have BC = a, CA = b, AB = c with a² + b² = c². (1)<br>Draw △XYZ with ∠Z = 90°, YZ = a, XZ = b. By Pythagoras XY² = a² + b² = c² ⇒ XY = c (2)<br>△ABC ≅ △XYZ by SSS (1) ⇒ ∠C = ∠Z = 90° (½)<br>So <b>△ABC is right-angled at C</b>. (½)"),
    sa("A goldsmith melts 9 units of gold of purity 12 varṇa, 5 units of purity 10 varṇa and x units of purity 14 varṇa. The mixture has purity 12 varṇa. Find x.", 5, "Purity of mixture = (9 × 12 + 5 × 10 + x × 14)/(9 + 5 + x) (2)<br>12 = (108 + 50 + 14x)/(14 + x) ⇒ 168 + 12x = 158 + 14x (2)<br>2x = 10 ⇒ <b>x = 5 units</b> (1)")),
 OR(sa("The sum of the length and the breadth of a rectangular plot is 17 m and its area is 72 m². Form a quadratic expression in the breadth x, factorise it and find the dimensions.", 5, "Length = 17 − x; x(17 − x) = 72 ⇒ x² − 17x + 72 = 0 (1½)<br>(x − 8)(x − 9) = 0 (1½)<br>x = 8 or 9 (1). The plot is <b>9 m by 8 m</b> (1)"),
    sa("The area of a rectangular carpet is (6x² + 17x + 12) m² and its breadth is (2x + 3) m. Find its length and, for x = 2, its perimeter.", 5, "6x² + 17x + 12 = 6x² + 9x + 8x + 12 (1½) = 3x(2x + 3) + 4(2x + 3) = (2x + 3)(3x + 4) (1)<br>Length = <b>(3x + 4) m</b> (1)<br>For x = 2: breadth 7 m, length 10 m ⇒ perimeter = 2(7 + 10) = <b>34 m</b> (1½)")),
]
E = [
 case("A mobile shop sold items to 120 customers in a week: mobile phones 45, laptops 30, tablets 25 and accessories 20.",
      [sub("Find the probability that a customer chosen at random bought a laptop.", 1, "30/120 = <b>1/4</b>"),
       sub("Find the probability that the customer did not buy an accessory.", 1, "1 − 20/120 = 100/120 = <b>5/6</b>"),
       OR(sub("Find the probability that the customer bought a mobile phone or a tablet.", 2, "(45 + 25)/120 (1) = 70/120 = <b>7/12</b> (1)"),
          sub("Another 30 customers bought laptops. Find the new probability that a customer chosen from all customers bought a laptop.", 2, "Laptops = 60, total = 150 (1) ⇒ 60/150 = <b>2/5</b> (1)"))]),
 case("A circular pond has centre O and radius 10 m. A fence AB, 16 m long, is a chord of the pond. M is the midpoint of AB and OM = 6 m.",
      [sub("Find the length AM.", 1, "OM ⊥ AB bisects the chord ⇒ AM = 16/2 = <b>8 m</b>"),
       sub("Verify that the radius of the pond is 10 m.", 1, "OA² = OM² + AM² = 36 + 64 = 100 ⇒ OA = <b>10 m</b>"),
       OR(sub("A second fence CD is placed at a distance of 8 m from O. Find its length.", 2, "Half of CD = √(100 − 64) = 6 (1) ⇒ CD = <b>12 m</b> (1)"),
          sub("Find the area of the triangle OAB.", 2, "Area = ½ × AB × OM = ½ × 16 × 6 (1) = <b>48 m²</b> (1)"))], fig=f37),
 case("A farmer’s field is the quadrilateral ABCD. P, Q, R and S are the midpoints of AB, BC, CD and DA. The diagonals are AC = 30 m and BD = 40 m. The farmer fences the inner field PQRS.",
      [sub("Find the length PQ.", 1, "In △ABC, P and Q are midpoints ⇒ PQ = ½AC = <b>15 m</b>"),
       sub("Find the length QR.", 1, "In △BCD, Q and R are midpoints ⇒ QR = ½BD = <b>20 m</b>"),
       OR(sub("Find the length of fencing required for PQRS.", 2, "PQ = SR = 15 m and QR = PS = 20 m (1) ⇒ perimeter = 2(15 + 20) = <b>70 m</b> (1)"),
          sub("Name the shape PQRS and justify your answer.", 2, "PQ ∥ AC and SR ∥ AC (Midpoint Theorem) so PQ ∥ SR; also PQ = SR = ½AC (1). One pair of opposite sides equal and parallel ⇒ <b>PQRS is a parallelogram</b> (Varignon parallelogram) (1)"))], fig=f38),
]
import add14
A, B, C, E = add14.patch(META['set_no'], A, B, C, E)
SECTIONS = sections(A, B, C, D, E)
