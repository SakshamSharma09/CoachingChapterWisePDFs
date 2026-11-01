from cm import *
import math
META = meta(5)
mid = lambda p, q: ((p[0]+q[0])/2, (p[1]+q[1])/2)

# ---------- figures ----------
f6, _ = circle_fig({'A': 230, 'B': 310, 'C': 90}, chords=[('C', 'A'), ('C', 'B')], radii=['A', 'B'], extra=text(105, 122, "", sz=1) + text(98, 76, "40°", sz=10))
Tt = {'A': (125, 12), 'B': (20, 140), 'C': (230, 140)}
Tt['D'] = mid(Tt['A'], Tt['B']); Tt['E'] = mid(Tt['A'], Tt['C'])
f25 = gfig(Tt, [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E')], w=250, h=165, off={'A': (0, -4), 'B': (-10, 12), 'C': (10, 12), 'D': (-12, 4), 'E': (12, 4)},
           extra=text(125, 126, "24 cm", sz=10) + text(185, 80, "20 cm", sz=10))
ca = pt(105, 105, 80, 220); cb = pt(105, 105, 80, 320)
f37, _ = circle_fig({'A': 220, 'B': 320, 'C': 90, 'D': 270}, chords=[('C', 'A'), ('C', 'B'), ('D', 'A'), ('D', 'B')], radii=['A', 'B'], center='O', extra=text(105, 90, "100°", sz=10))
Pp = {'A': (30, 135), 'B': (190, 135), 'C': (235, 40), 'D': (75, 40)}
Pp['O'] = mid(Pp['A'], Pp['C'])
f38 = gfig(Pp, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')], w=260, h=165, off={'A': (-10, 12), 'B': (10, 12), 'C': (10, -4), 'D': (-10, -4), 'O': (10, 14)}, extra=text(58, 125, "70°", sz=10) + text(110, 150, "12 cm", sz=10) + text(222, 90, "8 cm", sz=10))

# ---------- numeric verification ----------
assert 250+3*60 == 430 and abs(math.sqrt(20)*math.sqrt(5)-10) < 1e-9 and 5**2-2 == 23 and 2*40 == 80
assert 13**2 == 12**2+5**2 and 18*6*6*6 == (36**2)*3 and 1+2+3+4+5 == 15
assert (8*40+12*50)/20 == 46 and (3*60+3*70+4*90)/10 == 75 and 20-1 == 19
assert F(99+15*5, 1) == 174 and F(21, 400).denominator == 400 == 2**4*5**2 and F(-1, 2) < F(-1, 4) < 0 < F(1, 4)
assert (95+67) == 162 and (5+7) % 10 == 2 and (9+6+1) % 10 == 6
assert 55 + 55 == 110 and 24/2 == 12 and 20/2 == 10 and 24+1 == 25
assert F(123, 99) == F(41, 33)
assert 60+45+30+15 == 150 and F(60, 150) == F(2, 5) and F(75, 150) == F(1, 2) and F(15, 150) == F(1, 10)
assert 'PROBABILITY' and len('PROBABILITY') == 11 and sum(c in 'AEIOU' for c in 'PROBABILITY') == 4 and 'PROBABILITY'.count('B') == 2
assert 9+(3-2)**2 == 9+(3-4)**2
assert 41**2 - 41 + 41 == 41**2 and 2**6+1 == 65 == 5*13
assert math.isqrt(42*30*7*5) == 210 and 12**2+35**2 == 37**2
assert math.isqrt(15**2-9**2) == 12 and math.isqrt(15**2-12**2) == 9 and 2*12 == 24 and 18/2 == 9
P = (-2, -2); Q = (4, -2); R = (4, 2)
assert math.dist(P, Q) == 6 and math.dist(Q, R) == 4 and abs(6**2+4**2 - math.dist(P, R)**2) < 1e-9 and 0.5*6*4 == 12
d = [i for i in range(51, 251) if i % 5 == 3]; assert d[0] == 53 and d[-1] == 248 and len(d) == 40 and sum(d) == 6020
assert 16+44+80+40+20 == 200 and F(60, 200) == F(3, 10) and F(120, 200) == F(3, 5)
assert (100*.8+200*.5+.3*150) == .5*(300+150)
assert 25*0+10*15 == 150 and 10+15 == 25 and (2*2+1)*(2*2+5) == 4*4+12*2+5 and 2*(5+9) == 28
assert 500-20*8 == 340 and 500/20 == 25 and (500-120)/20 == 19 and 500/5 == 100
assert 180-80 == 100 and 180-2*40 == 100
assert 180-70 == 110 and 2*(12+8) == 40 and 8+5 == 13

A = [
 mc("The point which lies on both the x-axis and the y-axis is:", "(0, 0)", ["(1, 0)", "(0, 1)", "(1, 1)"], "Only the origin has both coordinates zero."),
 mc("The ordinate of the point (−2, 9) is:", "9", ["−2", "7", "−9"], "Ordinate = y-coordinate = 9."),
 mc("A tailor charges ₹250 as a fixed charge and ₹60 per metre of cloth. The charge (in ₹) for 3 m is:", "430", ["180", "810", "490"], "250 + 60 × 3 = 430."),
 mc("Which of the following is a rational number?", "√20 × √5", ["√2 × √3", "√7 + √3", "π + 1"], "√20 × √5 = √100 = 10 is rational; √6, √7 + √3 and π + 1 are irrational."),
 mc("If x + 1/x = 5, then x² + 1/x² is equal to:", "23", ["25", "27", "21"], "(x + 1/x)² = x² + 2 + 1/x² ⇒ x² + 1/x² = 25 − 2 = 23."),
 mc("In the figure, O is the centre of the circle and ∠ACB = 40°. Then ∠AOB is equal to:", "80°", ["20°", "40°", "160°"], "Angle at the centre is twice the angle at the circumference: 2 × 40° = 80°.", fig=f6),
 mc("A chord is 12 cm from the centre of a circle and its length is 10 cm. The radius of the circle is:", "13 cm", ["11 cm", "√119 cm", "17 cm"], "Half chord = 5 cm; r² = 12² + 5² = 169 ⇒ r = 13 cm."),
 mc("The area of an equilateral triangle of perimeter 36 cm, by Heron’s formula, is:", "36√3 cm²", ["72√3 cm²", "18√3 cm²", "144 cm²"], "Side = 12 cm, s = 18; area = √(18 × 6 × 6 × 6) = 36√3 cm²."),
 mc("A day of the week is chosen at random. The probability that its name begins with the letter ‘T’ is:", fr(2, 7), [fr(1, 7), fr(3, 7), fr(1, 2)], "Tuesday and Thursday ⇒ 2/7."),
 mc("A sequence is defined by t₁ = 1 and t<sub>n</sub> = t<sub>n−1</sub> + n for n ≥ 2. Then t<sub>5</sub> is:", "15", ["10", "21", "12"], "1, 3, 6, 10, 15."),
 mc("The converse of ‘If x = y, then x³ = y³’ is:", "If x³ = y³, then x = y.", ["If x ≠ y, then x³ ≠ y³.", "If x = y, then x² = y².", "If x³ = y³, then x² = y²."], "Interchange the two parts. (For real numbers this converse is also true.)"),
 mc("Euler disproved Fermat’s claim that all numbers of the form 2<sup>2<sup>n</sup></sup> + 1 are prime by showing that the number obtained for n = 5 is composite. That number is:", "2³² + 1", ["2¹⁶ + 1", "2⁸ + 1", "2⁴ + 1"], "For n = 5, 2^(2⁵) + 1 = 2³² + 1 is composite. The numbers for n = 0 to 4 (3, 5, 17, 257, 65537) are prime."),
 mc("Section A has 8 students with an average score of 40 and Section B has 12 students with an average score of 50. The combined average is:", "46", ["45", "47", "44"], "(8 × 40 + 12 × 50)/20 = 920/20 = 46."),
 mc("A student scores 60, 70 and 90 in components weighted in the ratio 3 : 3 : 4. The weighted mean is:", "75", ["73.3", "70", "78"], "(180 + 210 + 360)/10 = 75."),
 mc("The final gcd algorithm checks every k from 2 to min(m, n). For m = 20 and n = 50, the number of values of k checked is:", "19", ["20", "48", "49"], "k = 2, 3, …, 20 ⇒ 19 values."),
 mc("A quadrilateral whose diagonals bisect each other is always a:", "parallelogram", ["rectangle", "rhombus", "trapezium"], "Diagonals bisecting each other is a test for a parallelogram."),
 mc("In the figure, P and Q are the midpoints of AB and AC. If ∠ABC = 55°, then ∠APQ is:", "55°", ["125°", "35°", "70°"], "PQ ∥ BC (Midpoint Theorem), so corresponding angles are equal: ∠APQ = ∠ABC = 55°.", fig=gfig({'A': (125, 12), 'B': (20, 140), 'C': (230, 140), 'P': (72.5, 76), 'Q': (177.5, 76)}, [('A', 'B'), ('B', 'C'), ('C', 'A'), ('P', 'Q')], w=250, h=165, off={'A': (0, -4), 'B': (-10, 12), 'C': (10, 12), 'P': (-12, 4), 'Q': (12, 4)}, extra=text(46, 130, "55°", sz=10))),
 mc("The sum of the first 10 terms of the AP 3, 7, 11, … is:", "210", ["200", "220", "230"], "S₁₀ = 10/2 × [2(3) + 9(4)] = 5 × 42 = 210."),
 ar("(a + b)² = a² + b² for all real numbers a and b.", "(a + b)² = a² + 2ab + b².", 'd', "A is false (e.g. a = b = 1 gives 4 ≠ 2); R is the true identity."),
 ar("The number 36 has an odd number of factors.", "36 is a perfect square, and a perfect square has an odd number of factors.", 'a', "36 has the 9 factors 1, 2, 3, 4, 6, 9, 12, 18, 36. The factor pairs have the single repeated pair (6, 6) – so R explains A."),
]
B = [
 sa("A mobile data plan costs ₹99 and includes 1 GB. Every additional GB costs ₹15. Find the cost of using 6 GB.", 2, "Extra data = 6 − 1 = 5 GB (½)<br>Extra cost = 5 × 15 = ₹75 (1)<br>Cost = 99 + 75 = <b>₹174</b> (½)"),
 OR(sa("Without actual division, show that " + fr(21, 400) + " has a terminating decimal expansion and state the number of decimal places.", 2, "400 = 2⁴ × 5² has only 2 and 5 as prime factors ⇒ terminates (1). Number of decimal places = <b>4</b> (0.0525) (1)"),
    sa("Find two rational numbers between " + fr(-1, 2) + " and " + fr(1, 4) + ".", 2, "−1/2 = −2/4, so any two numbers in between, e.g. <b>−1/4 and 0</b> (1 each)")),
 sa("Factorise: 25a² − 64b².", 2, "= (5a)² − (8b)² (1) = <b>(5a − 8b)(5a + 8b)</b> (1)"),
 sa("Using the digit-by-digit addition algorithm, add 95 and 67. What would the answer be if the last step (writing the final carry) were omitted?", 2, "5 + 7 = 12 → write 2, carry 1; 9 + 6 + 1 = 16 → write 6, carry 1; final carry written: <b>162</b> (1)<br>Without the last step the answer would be <b>62</b> (1)"),
 sa("In the figure, D is the midpoint of AB and DE ∥ BC. If BC = 24 cm and AC = 20 cm, find DE and AE, giving reasons.", 2, "By the converse of the Midpoint Theorem E is the midpoint of AC ⇒ <b>AE = 10 cm</b> (1)<br>By the Midpoint Theorem <b>DE = ½BC = 12 cm</b> (1)", fig=f25),
]
C = [
 sa("Express 1.2424… (24 repeating) in the form p/q in lowest terms.", 3, "x = 1.2424…; 100x = 124.2424… (1)<br>99x = 123 (1)<br>x = 123/99 = <b>41/33</b> (1)"),
 OR(sa("In a survey of 150 people, their favourite drink was recorded:" + htable(["Drink", "Tea", "Coffee", "Juice", "None"], ["People", 60, 45, 30, 15]) + "A person is chosen at random. Find the probability that the person (i) prefers tea, (ii) prefers coffee or juice, (iii) has no favourite.", 3, "Total = 150. (i) 60/150 = <b>2/5</b> (1) (ii) 75/150 = <b>1/2</b> (1) (iii) 15/150 = <b>1/10</b> (1)"),
    sa("A letter is chosen at random from the word ‘PROBABILITY’. Find the probability that it is (i) a vowel, (ii) the letter B, (iii) not the letter I.", 3, "11 letters. (i) Vowels O, A, I, I = 4 ⇒ <b>4/11</b> (1) (ii) B occurs twice ⇒ <b>2/11</b> (1) (iii) I occurs twice ⇒ 9/11 (1)")),
 sa("Find the coordinates of the point P on the y-axis which is equidistant from A(−3, 2) and B(3, 4).", 3, "Let P(0, y). PA² = 9 + (y − 2)², PB² = 9 + (y − 4)² (1)<br>PA = PB ⇒ (y − 2)² = (y − 4)² ⇒ −4y + 4 = −8y + 16 (1) ⇒ y = 3: <b>P(0, 3)</b> (1)"),
 sa("Give a counterexample to each claim: (i) ‘n² − n + 41 is prime for every positive integer n’; (ii) ‘If n is even, then 2<sup>n</sup> + 1 is prime’.", 3, "(i) n = 41: 41² − 41 + 41 = 41² = 1681 is not prime (1½)<br>(ii) n = 6: 2⁶ + 1 = 65 = 5 × 13 is not prime (1½)"),
 OR(sa("Using Heron’s formula, find the area of a triangle whose sides are 12 cm, 35 cm and 37 cm.", 3, "s = (12 + 35 + 37)/2 = 42 cm (1)<br>Area = √[42 × 30 × 7 × 5] (1) = √44100 = <b>210 cm²</b> (1)"),
    sa("A chord AB of length 18 cm is 12 cm from the centre of a circle. Find the radius, and the length of another chord CD of the same circle that is 9 cm from the centre.", 3, "r² = 12² + 9² = 225 ⇒ <b>r = 15 cm</b> (1)<br>Half of CD = √(225 − 81) = 12 (1) ⇒ <b>CD = 24 cm</b> (1)")),
 sa("The diagonals of a parallelogram ABCD are equal. Show that ABCD is a rectangle.", 3, "In △ABC and △DCB: AB = DC (opposite sides), BC = CB (common), AC = DB (given) ⇒ △ABC ≅ △DCB (SSS) ⇒ ∠ABC = ∠DCB (1½)<br>AB ∥ DC, so ∠ABC + ∠DCB = 180° ⇒ each angle = 90° (1)<br>A parallelogram with a right angle is a rectangle. (½)"),
]
Pr = {'A': (-2, -2), 'B': (4, -2), 'C': (4, 2)}
figD = coord_plane(Pr, xr=(-4, 6), yr=(-4, 4), u=22, segs=[('A', 'B'), ('B', 'C'), ('C', 'A')])
D = [
 sa("A triangular signboard has its corners at A(−2, −2), B(4, −2) and C(4, 2) on a grid.<br>(a) Plot the points and join them. (2 marks)<br>(b) Find the lengths AB, BC and AC. (1½ marks)<br>(c) Use the converse of the Baudhāyana–Pythagoras theorem to show that the triangle is right-angled and find its area. (1½ marks)", 5,
    "(a) Plotting 3 points (1½), joining (½):" + figD + "(b) AB = 6, BC = 4, AC = √(6² + 4²) = √52 (1½)<br>(c) AB² + BC² = 36 + 16 = 52 = AC² ⇒ the triangle is right-angled at B (converse of the theorem) (1). Area = ½ × 6 × 4 = <b>12 square units</b> (½)"),
 OR(sa("Find the sum of all natural numbers between 50 and 250 which leave remainder 3 when divided by 5. (How many such numbers are there? 2½ + 2½)", 5, "Numbers: 53, 58, …, 248 — an AP with a = 53, d = 5, l = 248 (1)<br>n = (248 − 53)/5 + 1 = <b>40</b> (1½)<br>Sum = 40/2 × (53 + 248) = 20 × 301 = <b>6020</b> (2½)"),
    sa("The marks of 200 students in an examination were recorded:" + htable(["Marks", "0 – 20", "20 – 40", "40 – 60", "60 – 80", "80 – 100"], ["Students", 16, 44, 80, 40, 20]) + "Find the probability that a student chosen at random scored (i) 60 marks or more (1), (ii) less than 40 marks (1), (iii) 40 or more but less than 80 marks (2), and (iv) comment on the sum of the probabilities of the five classes (1).", 5, "Total = 200. (i) (40 + 20)/200 = <b>3/10</b> (1) (ii) (16 + 44)/200 = <b>3/10</b> (1) (iii) (80 + 40)/200 = <b>3/5</b> (2) (iv) The five probabilities 2/25, 11/50, 2/5, 1/5, 1/10 add up to <b>1</b> (1)")),
 OR(sa("Prove that if the opposite sides of a quadrilateral are equal, then it is a parallelogram.", 5, "Let ABCD be a quadrilateral with AB = CD and AD = BC. Join AC. (1)<br>In △ACD and △CAB: AC = CA (common), CD = AB, AD = CB ⇒ △ACD ≅ △CAB (SSS) (1½)<br>So ∠DAC = ∠BCA ⇒ AD ∥ BC (alternate angles) (1)<br>and ∠DCA = ∠BAC ⇒ DC ∥ AB (1)<br>Both pairs of opposite sides are parallel ⇒ <b>ABCD is a parallelogram</b>. (½)"),
    sa("Batch A of brass weighs 100 kg and is 80% copper; Batch B weighs 200 kg and is 50% copper. Batch C is 30% copper. The three batches are melted together to give an alloy that is 50% copper. Find the weight of Batch C.", 5, "Let Batch C weigh y kg. Copper: A = 80 kg, B = 100 kg, C = 0.3y (1½)<br>0.50 = (80 + 100 + 0.3y)/(300 + y) (1½)<br>150 + 0.5y = 180 + 0.3y (1) ⇒ 0.2y = 30 ⇒ <b>y = 150 kg</b> (1)")),
 OR(sa("The perimeter of a rectangular field is 50 m and its area is 150 m². Form a quadratic expression in the breadth x, factorise it and find the length and breadth.", 5, "Length + breadth = 25 ⇒ length = 25 − x. Area: x(25 − x) = 150 ⇒ x² − 25x + 150 = 0 (1½)<br>(x − 10)(x − 15) = 0 (1½)<br>x = 10 or 15 (1) ⇒ the field is <b>15 m by 10 m</b> (1)"),
    sa("The area of a rectangular garden is (4x² + 12x + 5) m². Factorise the expression to find its length and breadth. If x = 2, find the perimeter.", 5, "4x² + 12x + 5 = 4x² + 2x + 10x + 5 (1½) = 2x(2x + 1) + 5(2x + 1) = (2x + 1)(2x + 5) (1)<br>Dimensions: <b>(2x + 1) m and (2x + 5) m</b> (1)<br>For x = 2: 5 m and 9 m ⇒ perimeter = 2(5 + 9) = <b>28 m</b> (1½)")),
]
E = [
 case("A water tank holds 500 litres. It is emptied at the rate of 20 litres per minute, so the water left after t minutes is W = 500 − 20t litres.",
      [sub("How much water is left after 8 minutes?", 1, "W = 500 − 160 = <b>340 litres</b>"),
       sub("Find the zero of the polynomial W = 500 − 20t and say what it means.", 1, "500 − 20t = 0 ⇒ t = <b>25</b>; the tank is empty after 25 minutes."),
       OR(sub("After how many minutes will 120 litres be left?", 2, "500 − 20t = 120 (1) ⇒ t = <b>19 minutes</b> (1)"),
          sub("Water is poured in at 15 litres per minute while the tank is being emptied at 20 litres per minute. Write the new expression for the water left and find when the tank is empty.", 2, "W = 500 − 20t + 15t = 500 − 5t (1) ⇒ empty when t = <b>100 minutes</b> (1)"))]),
 case("On a circular dance floor with centre O, two lights A and B are fixed on the boundary so that the chord AB subtends an angle of 100° at O. A speaker C is placed on the major arc and another speaker D on the minor arc.",
      [sub("Find ∠ACB.", 1, "Angle at the circumference = ½ × angle at the centre = <b>50°</b>"),
       sub("Find ∠ADB.", 1, "ACBD is a cyclic quadrilateral ⇒ ∠ADB = 180° − 50° = <b>130°</b>"),
       OR(sub("Find ∠OAB.", 2, "OA = OB ⇒ ∠OAB = ∠OBA (½); ∠OAB = (180° − 100°)/2 (1) = <b>40°</b> (½)"),
          sub("State the relation between ∠ACB and ∠ADB and name the property used.", 2, "∠ACB + ∠ADB = 180° (1), because opposite angles of a cyclic quadrilateral are supplementary (1)."))], fig=f37),
 case("A mechanic makes a frame ABCD that is a parallelogram. Its sides are AB = 12 cm and BC = 8 cm and ∠A = 70°. The diagonals AC and BD meet at O.",
      [sub("Find ∠B.", 1, "Adjacent angles are supplementary: ∠B = 180° − 70° = <b>110°</b>"),
       sub("Find the perimeter of the frame.", 1, "Opposite sides are equal: perimeter = 2(12 + 8) = <b>40 cm</b>"),
       OR(sub("If AC = 16 cm and BD = 10 cm, find OA + OB.", 2, "Diagonals bisect each other: OA = 8 cm, OB = 5 cm (1) ⇒ OA + OB = <b>13 cm</b> (1)"),
          sub("The frame is pressed until its diagonals become equal. Name the shape now formed and justify your answer.", 2, "A parallelogram with equal diagonals is a <b>rectangle</b> (1): the triangles ABC and DCB become congruent (SSS), so ∠ABC = ∠DCB = 90° (1)."))], fig=f38),
]
import add14
A, B, C, E = add14.patch(META['set_no'], A, B, C, E)
SECTIONS = sections(A, B, C, D, E)
