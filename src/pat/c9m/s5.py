from common import *
import math
META = meta(5)
cx = cy = 105
# figures
f13 = circle_fig({'A': 200, 'B': 340, 'D': 270, 'C': 90}, chords=[('A', 'D'), ('D', 'B')], radii=['A', 'B'], center='O', extra=text(105, 90, '140°', sz=11))[0]
_f24 = circle_fig({'A': 65, 'B': 15, 'C': 200, 'D': 40}, chords=[('A', 'C'), ('C', 'B'), ('A', 'D'), ('D', 'B')], radii=['A', 'B'], center='O', extra=text(*pt(cx, cy, 28, 40), '50°', sz=10))[0]
sol32 = coord_plane({'A': (0, 10), 'B': (3, 5), 'C': (6, 0)}, xr=(-1, 8), yr=(-1, 11), u=20, segs=[('A', 'B'), ('B', 'C')])
# ---- checks ----
assert 40+15*7 == 145 and 1200-500 == 700
assert F(49, 2**3*5**4*7) == F(7, 2**3*5**4)
assert F(5, 8) < F(11, 16) < F(23, 32) < F(3, 4)
assert 2*7*6 == 84 and 7*7 == 49 and 6*6 == 36
assert 2*3+2 == 8 and 2*8+3 == 19 and 2*19+4 == 42
assert 3**2+4**2 == 5**2 and 3**2+4**2 == 25 and 5**2-3**2 == 16
assert 10**2-2*31 == 38 and 3*3+0 == 9 and abs(3-7)+abs(-2) == 6 and 9**2+1 == 82
assert math.isqrt(18*9*8*1) == 36 and 36**2 == 18*9*8 and 180-70 == 110
assert (F(36, 99), F(27, 99)) == (F(4, 11), F(3, 11)) and F(4, 11)+F(3, 11) == F(7, 11)
assert 10+28+30+12 == 80 and 28+10 == 38 and 8+12+10+9+11+10 == 60 and 12+9+10 == 31 and 11+10 == 21
assert math.hypot(5, 12) == 13 and (-6-1)/2 == -3.5 and (7-5)/2 == 1
assert 12**3-6*12**2+12*12-8 == 1000 == 10**3
assert (399-101)//2+1 == 150 and 150*(101+399)//2 == 37500
assert 40+160+450+350 == 1000 and 160+450 == 610 and F(610, 1000) == F(61, 100) and F(350, 1000) == F(7, 20)
assert 22+90+70+18 == 200 and 22+90 == 112 and F(112, 200) == F(14, 25) and F(70, 200) == F(7, 20) and F(18, 200) == F(9, 100)
assert 7+24+25 == 56 and 168//56 == 3 and (21+72+75) == 168 and math.isqrt(84*63*12*9) == 756 and 756**2 == 84*63*12*9
assert 45*(45-9)*(45-40)*(45-41) == 32400 and math.isqrt(32400) == 180
assert 10*13 == 130 and 13-10 == 3 and 2*(10+13) == 46 and 46*40 == 1840 and 10**2+30-130 == 0
assert (2*5+1)*(5+4) == 99 and 2*25+45+4 == 99 and 2*(11+9) == 40 and (2*x+1)*(x+4) == 2*x*x+9*x+4 if (x := 7) else 0
assert 45*20*16*9 == 129600 and math.isqrt(129600) == 360 and 360**2 == 129600 and 360*5 == 1800 and 2*360//36 == 20 and (45-25, 45-29, 45-36) == (20, 16, 9)
assert 36+30+24+30 == 120 and F(36, 120) == F(3, 10) and F(96, 120) == F(4, 5) and F(60, 120) == F(1, 2) and F(24+20, 140) == F(11, 35)
assert 200+40*6 == 440 and (800-200)//40 == 15 and 200+40*12 == 680 and 680-(200+40*4) == 320
assert sum(1 for c in "STATISTICS" if c == 'T') == 3 and len("STATISTICS") == 10
A = [
 mc("Which of the following points lies on neither axis?", "(3, −2)", ["(0, 5)", "(−4, 0)", "(0, 0)"], "A point lies on an axis if one coordinate is 0. Only (3, −2) has both coordinates non-zero."),
 mc("The distance between the points (−2, 0) and (2, 0) is:", "4 units", ["0 units", "2 units", "8 units"], "Both points lie on the x-axis: |2 − (−2)| = 4."),
 mc("If the point P(a, 3) is at a distance of 5 units from the point (0, −1), then the value of a is:", "±3", ["3 only", "±4", "±5"], "a² + (3 + 1)² = 25 ⇒ a² = 9 ⇒ a = ±3."),
 mc("If p(x) = 4x² − 3x + 7, then p(0) is:", "7", ["0", "8", "−3"], "p(0) = 7."),
 mc("The degree of the polynomial (x + 1)(x − 1) is:", "2", ["0", "1", "3"], "(x + 1)(x − 1) = x² − 1, degree 2."),
 mc("The area of a rectangular garden is (x² − 9) m² and its breadth is (x − 3) m. Its length is:", "(x + 3) m", ["(x − 3) m", "(x + 9) m", "(x² − 6) m"], "x² − 9 = (x − 3)(x + 3) ⇒ length = (x + 3) m."),
 mc("Which of the following has a non-terminating repeating decimal expansion?", fr(5, 6), [fr(3, 16), fr(7, 25), fr(9, 40)], "6 = 2 × 3 has the factor 3 (not 2 or 5) ⇒ non-terminating. The others have denominators 2⁴, 5², 2³ × 5."),
 mc("The irrational number √3 lies between:", "1 and 2", ["0 and 1", "2 and 3", "3 and 4"], "1² = 1 &lt; 3 &lt; 4 = 2²."),
 mc("The value of |3 − 7| + |−2| is:", "6", ["2", "−6", "−2"], "|−4| + 2 = 4 + 2 = 6."),
 mc("The expression x² − 6x + 9 can be written as:", "(x − 3)²", ["(x + 3)²", "(x − 3)(x + 3)", "(x − 9)²"], "a² − 2ab + b² with a = x, b = 3."),
 mc("If a + b + c = 10 and ab + bc + ca = 31, then a² + b² + c² is:", "38", ["41", "69", "100"], "a² + b² + c² = (a + b + c)² − 2(ab + bc + ca) = 100 − 62 = 38."),
 mc("In a circle with centre O, chords AB and CD are equal. If the perpendicular distance of AB from O is 7 cm, the perpendicular distance of CD from O is:", "7 cm", ["14 cm", "3.5 cm", "cannot be found"], "Equal chords of a circle are equidistant from the centre."),
 mc("In the figure, O is the centre of the circle and ∠AOB = 140°. If D is a point on the minor arc AB, then ∠ADB is:", "110°", ["70°", "140°", "220°"], "Angle on the major arc = 70°; ADCB is cyclic ⇒ ∠ADB = 180° − 70° = 110°.", fig=f13),
 mc("The area of an equilateral triangle of side 8 cm is:", "16√3 cm²", ["32√3 cm²", "64√3 cm²", "8√3 cm²"], "(√3/4) × 8² = 16√3."),
 mc("The area of a triangle with sides 9 cm, 10 cm and 17 cm is:", "36 cm²", ["72 cm²", "45 cm²", "90 cm²"], "s = 18; √(18 × 9 × 8 × 1) = √1296 = 36."),
 mc("Two dice are thrown together. The probability that the sum of the numbers is 12 is:", fr(1, 36), [fr(1, 12), fr(1, 6), fr(1, 18)], "Only (6, 6) out of 36 outcomes."),
 mc("A letter is chosen at random from the word STATISTICS. The probability that it is T is:", fr(3, 10), [fr(1, 10), fr(1, 5), fr(2, 5)], "T appears 3 times in 10 letters."),
 mc("If the n-th term of a sequence is t<sub>n</sub> = n² + 1, then t₉ is:", "82", ["81", "19", "10"], "81 + 1 = 82."),
 ar("The point (−3, 0) lies on the x-axis.", "Every point on the x-axis has ordinate 0.", 'a', "Ordinate of (−3, 0) is 0, so it lies on the x-axis; R explains A."),
 ar("(a + b)² = a² + b² for all real numbers a and b.", "(a + b)² = a² + 2ab + b².", 'd', "R is the true identity; the extra term 2ab makes A false in general (e.g. a = b = 1: 4 ≠ 2)."),
]
B = [
 sa("A courier company charges ₹40 for the first 500 g and ₹15 for every additional 100 g (or part thereof). Write the charge for n additional units of 100 g and find the charge for a parcel of 1.2 kg.", 2, "Charge = 40 + 15n (1). 1.2 kg = 1200 g; additional 700 g = 7 units ⇒ 40 + 105 = <b>₹145</b> (1)"),
 OR(sa("Without performing division, show that " + fr(49, "2³ × 5⁴ × 7") + " is a terminating decimal and state the number of decimal places.", 2, "Simplify: 49/(2³ × 5⁴ × 7) = 7/(2³ × 5⁴) (½). Only 2 and 5 in the denominator ⇒ terminating (½). Decimal places = greater power = <b>4</b> (1)."),
    sa("Find two rational numbers between " + fr(5, 8) + " and " + fr(3, 4) + ".", 2, "5/8 = 10/16 = 20/32 and 3/4 = 24/32; so e.g. 11/16 and 23/32 (1 each). Check: 5/8 &lt; 11/16 &lt; 23/32 &lt; 3/4.")),
 sa("Factorise: 49x² + 84xy + 36y².", 2, "= (7x)² + 2(7x)(6y) + (6y)² (1) = <b>(7x + 6y)²</b> (1)"),
 sa("In the figure, O is the centre of the circle and ∠AOB = 50°. Find ∠ACB and ∠ADB.", 2, "∠ACB = ½ × 50° = <b>25°</b> (1)<br>ACBD is cyclic ⇒ ∠ADB = 180° − 25° = <b>155°</b> (1)", fig=_f24),
 sa("Find the second, third and fourth terms of the sequence defined by t₁ = 3 and t<sub>n</sub> = 2t<sub>n−1</sub> + n for n ≥ 2.", 2, "t₂ = 2(3) + 2 = 8; t₃ = 2(8) + 3 = 19; t₄ = 2(19) + 4 = 42. (½ for method + 1½ for values)"),
]
C = [
 sa("Express 0.363636… + 0.272727… as a fraction in the form p/q.", 3, "0.3636… = 36/99 = 4/11 (1); 0.2727… = 27/99 = 3/11 (1)<br>Sum = 7/11 (1)"),
 OR(sa("A coin was tossed 80 times and the number of heads was recorded:" + htable(["Heads", 3, 2, 1, 0], ["Frequency", 10, 28, 30, 12]) + "Find the probability of getting (i) at least 2 heads, (ii) exactly 1 head, (iii) no head.", 3, "(i) (10 + 28)/80 = <b>19/40</b> (1) (ii) 30/80 = <b>3/8</b> (1) (iii) 12/80 = <b>3/20</b> (1)"),
    sa("A die was thrown 60 times with the following results:" + htable(["Outcome", 1, 2, 3, 4, 5, 6], ["Frequency", 8, 12, 10, 9, 11, 10]) + "Find the probability of getting (i) an even number, (ii) a number greater than 4, (iii) the number 1.", 3, "(i) (12 + 9 + 10)/60 = <b>31/60</b> (1) (ii) (11 + 10)/60 = <b>7/20</b> (1) (iii) 8/60 = <b>2/15</b> (1)")),
 sa("Find the distance between the points A(−6, 7) and B(−1, −5), and the coordinates of the midpoint of AB.", 3, "AB = √[(−1 + 6)² + (−5 − 7)²] (1) = √(25 + 144) = <b>13 units</b> (1)<br>Midpoint = ((−6 − 1)/2, (7 − 5)/2) = <b>(−7/2, 1)</b> (1)"),
 sa("Factorise x³ − 6x² + 12x − 8 and hence find its value for x = 12.", 3, "= x³ − 3·x²·2 + 3·x·2² − 2³ = (x − 2)³ (2)<br>For x = 12: 10³ = <b>1000</b> (1)"),
 sa("Prove that the perpendicular drawn from the centre of a circle to a chord bisects the chord.", 3, "Given: chord AB of a circle with centre O; OM ⊥ AB. To prove: AM = MB. Join OA and OB. (½)<br>In △OMA and △OMB: ∠OMA = ∠OMB = 90°, OA = OB (radii), OM = OM (common) (1½)<br>So △OMA ≅ △OMB (RHS) (½) ⇒ AM = MB (CPCT). (½)"),
 OR(sa("The sides of a triangular park are in the ratio 7 : 24 : 25 and its perimeter is 168 m. Find its area using Heron’s formula.", 3, "Sides = 7k, 24k, 25k; 56k = 168 ⇒ k = 3: 21 m, 72 m, 75 m (1)<br>s = 84; area = √(84 × 63 × 12 × 9) (1) = <b>756 m²</b> (1)"),
    sa("Find the area of a triangle with sides 9 cm, 40 cm and 41 cm using Heron’s formula.", 3, "s = 45 (1); area = √(45 × 36 × 5 × 4) (1) = √32400 = <b>180 cm²</b> (1)")),
]
D = [
 sa("Riya buys x pencils at ₹5 each and y erasers at ₹3 each and spends exactly ₹30.<br>(a) Write this as a linear equation in x and y, in the form ax + by + c = 0, and write a, b, c. (1 mark)<br>(b) Complete a table of three solutions (x, y). (1 mark)<br>(c) Draw the graph of the equation on a graph paper. (2 marks)<br>(d) Use the graph to find the number of erasers she buys if she buys 3 pencils. (1 mark)", 5,
    "(a) 5x + 3y = 30 ⇒ 5x + 3y − 30 = 0; a = 5, b = 3, c = −30 (1)<br>(b) " + htable(["x", 0, 3, 6], ["y", 10, 5, 0]) + " (1)<br>(c) Plot (0, 10), (3, 5), (6, 0) (1) and join with a straight line (1):" + sol32 + "(d) At x = 3, y = <b>5 erasers</b> (1)"),
 sa("(a) How many odd numbers lie between 100 and 400? (b) Find their sum. (c) Is 305 a term of this list? Give a reason. (2 + 2 + 1 marks)", 5, "Numbers: 101, 103, …, 399; AP with a = 101, d = 2, l = 399 (1)<br>(a) n = (399 − 101)/2 + 1 = <b>150</b> (1)<br>(b) S = 150/2 × (101 + 399) = 75 × 500 = <b>37500</b> (2)<br>(c) Yes, 305 is odd and lies between 100 and 400 (1)"),
 OR(sa("The lifetimes of 1000 electric bulbs were recorded:" + htable(["Lifetime (hours)", "0 – 300", "300 – 600", "600 – 900", "900 – 1200"], ["Number of bulbs", 40, 160, 450, 350]) + "A bulb is chosen at random. Find the probability that its lifetime is (i) less than 300 hours, (ii) between 300 and 900 hours, (iii) more than 900 hours.", 5, "Total = 1000 (1)<br>(i) 40/1000 = <b>1/25</b> (1½)<br>(ii) (160 + 450)/1000 = 610/1000 = <b>61/100</b> (2)<br>(iii) 350/1000 = <b>7/20</b> (½ + ½)"),
    sa("A survey of 200 families recorded the number of children in each family:" + htable(["Children", 0, 1, 2, 3], ["Families", 22, 90, 70, 18]) + "A family is chosen at random. Find the probability that it has (i) exactly 2 children, (ii) at most 1 child, (iii) more than 2 children.", 5, "Total = 200 (1)<br>(i) 70/200 = <b>7/20</b> (1½)<br>(ii) (22 + 90)/200 = 112/200 = <b>14/25</b> (2)<br>(iii) 18/200 = <b>9/100</b> (½ + ½)")),
 OR(sa("The length of a rectangular park is 3 m more than its breadth and its area is 130 m². Form a quadratic expression, factorise it to find the dimensions, and find the cost of fencing the park at ₹40 per metre.", 5, "Breadth = b, length = b + 3 ⇒ b(b + 3) = 130 ⇒ b² + 3b − 130 = 0 (1½)<br>b² + 13b − 10b − 130 = (b + 13)(b − 10) = 0 ⇒ b = 10 (1½)<br>Breadth = 10 m, length = 13 m (½); perimeter = 2(10 + 13) = 46 m (½); cost = 46 × 40 = <b>₹1840</b> (1)"),
    sa("A mosaic is made of 2 big square tiles of side x, 9 long strips of size x × 1 and 4 small unit squares, so its area is (2x² + 9x + 4). Factorise the expression to find the dimensions of the rectangle formed. Find its perimeter and area when x = 5.", 5, "2x² + 9x + 4 = 2x² + 8x + x + 4 (1½) = 2x(x + 4) + 1(x + 4) = <b>(2x + 1)(x + 4)</b> (1½)<br>Dimensions: (2x + 1) and (x + 4) (½). For x = 5: 11 and 9 units ⇒ perimeter = 2(11 + 9) = <b>40 units</b> (1), area = 99 square units (½)")),
]
E_ = [
 case("A triangular plot of land has sides 25 m, 29 m and 36 m.",
      [sub("Find the semi-perimeter of the plot.", 1, "s = (25 + 29 + 36)/2 = <b>45 m</b>"),
       sub("Find the area of the plot using Heron’s formula.", 1, "√(45 × 20 × 16 × 9) = √129600 = <b>360 m²</b>"),
       OR(sub("The plot is to be levelled at ₹5 per m². Find the total cost.", 2, "Cost = 360 × 5 (1) = <b>₹1800</b> (1)"),
          sub("Find the altitude of the plot on its longest side.", 2, "½ × 36 × h = 360 (1) ⇒ h = <b>20 m</b> (1)"))]),
 case("In a school sports day, 120 entries were received for four events:" + htable(["Event", "Races", "Jumps", "Throws", "Relays"], ["Entries", 36, 30, 24, 30]) + "One entry form is picked at random.",
      [sub("Find the probability that it is for a race.", 1, "36/120 = <b>3/10</b>"),
       sub("Find the probability that it is not for a throw.", 1, "96/120 = <b>4/5</b>"),
       OR(sub("Find the probability that it is for a jump or a relay.", 2, "(30 + 30)/120 (1) = <b>1/2</b> (1)"),
          sub("If 20 more entries are received, all for throws, find the new probability that a randomly picked entry is for a throw.", 2, "Throws = 44, total = 140 (1) ⇒ 44/140 = <b>11/35</b> (1)"))]),
 case("Kabir saves money in a jar. He starts with ₹200 and adds ₹40 every week. The amount in the jar after w weeks is M = 200 + 40w.",
      [sub("How much money is there in the jar after 6 weeks?", 1, "M = 200 + 240 = <b>₹440</b>"),
       sub("What does the number 40 in the equation represent?", 1, "The amount (₹) added to the jar every week."),
       OR(sub("After how many weeks will the jar have ₹800?", 2, "200 + 40w = 800 (1) ⇒ w = <b>15 weeks</b> (1)"),
          sub("Find the amount after 12 weeks and its increase over the amount after 4 weeks.", 2, "M(12) = <b>₹680</b>; M(4) = 360 (1); increase = <b>₹320</b> (1)"))]),
]
SECTIONS = sections(A, B, C, D, E_)
