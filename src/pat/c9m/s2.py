from common import *
import math
META = meta(2)
cx = cy = 105
# Q24: A,B,C on circle with O; angle ACB = 62
f24, _ = circle_fig({'A': 215, 'B': 325, 'C': 90}, chords=[('A', 'B'), ('C', 'A'), ('C', 'B')], radii=['A', 'B'], center='O')
# Q32 cyclic quad
f32, _ = circle_fig({'A': 100, 'B': 205, 'C': 295, 'D': 20}, chords=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], radii=['B', 'D'], center='O')
# Q37 coordinate case
pts = {'A': (2, 3), 'B': (6, 3), 'C': (6, -1)}
f37 = coord_plane(pts, xr=(0, 8), yr=(-3, 5), u=22, segs=[('A', 'B'), ('B', 'C')])
sol37 = coord_plane({'A': (2, 3), 'B': (6, 3), 'C': (6, -1), 'D': (2, -1)}, xr=(0, 8), yr=(-3, 5), u=22, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
# ---- checks ----
assert 4*(3*4-2) == 40 and F(13, 40).denominator == 40 and 30 == 2*3*5
assert 103*107 == 105**2-4 == 11021 and 51**2 == 2601
assert F(2, 3) < F(11, 16) < F(17, 24) < F(3, 4)
assert (2**2-1, (2**2-1)**2-1, (((2**2-1)**2-1)**2-1)) == (3, 8, 63)
assert 180-124 == 56 and 56//2 == 28 and 62*2 == 124
s = 21; assert math.isqrt(21*14*6*1) == 42 and 21*14*6*1 == 1764 and 24*8*8*8 == 12288 == 4096*3
assert 8*6 == 48 and math.hypot(8, 6) == 10
assert F(31, 12) == abs(F(-7, 4)-F(5, 6)) and abs(F(-7, 4))*abs(F(5, 6)) == F(35, 24)
n = (96-12)//4+1; assert n == 22 and n*(12+96)//2 == 1188 and 12 % 4 == 0 and 8 % 4 == 0
assert 250//25+1 == 11 and 11*(45+25)//2 == 385
assert math.isqrt(30*15*10*5) == 150 and 150*0+60*30 == 1800 and 150*8 == 1200
assert math.isqrt(18*5*5*8) == 60 and 2*60/10 == 12
assert 50*6+50 == 350 and 50*19+50 == 1000 and 10*(100+550)//2 == 3250
assert 4**2+4**2 == 32
A = [
 mc("A point P(a, b) lies in the second quadrant. Then:", "a &lt; 0 and b &gt; 0", ["a &gt; 0 and b &gt; 0", "a &lt; 0 and b &lt; 0", "a &gt; 0 and b &lt; 0"], "Second quadrant: abscissa negative, ordinate positive."),
 mc("The distance between the points (−2, 5) and (−2, −3) is:", "8 units", ["2 units", "5 units", "√8 units"], "Same x-coordinate, so distance = |5 − (−3)| = 8."),
 mc("The reflection of the point (4, −7) in the y-axis is:", "(−4, −7)", ["(4, 7)", "(−4, 7)", "(4, −7)"], "Reflection in the y-axis changes the sign of the x-coordinate."),
 mc("Which of the following is a linear polynomial?", "2x − 5", ["x² − 1", "√x + 3", "1/x + 2"], "Degree 1 polynomial in x."),
 mc("The zero of the polynomial p(x) = 5x − 15 is:", "3", ["−3", "15", "5"], "5x − 15 = 0 ⇒ x = 3."),
 mc("A notebook costs ₹x and a pen costs ₹20. The cost (in ₹) of 6 notebooks and one pen is:", "6x + 20", ["26x", "6x − 20", "x + 120"], "6 × x + 20."),
 mc("Which of the following numbers lies between √2 and √3?", "1.5", ["1.3", "1.8", "2"], "√2 ≈ 1.414 and √3 ≈ 1.732; only 1.5 lies between them."),
 mc("The decimal expansion of √5 is:", "non-terminating and non-repeating", ["terminating", "non-terminating and repeating", "1.5"], "√5 is irrational."),
 mc("If |x| = " + fr(5, 3) + " for a rational number x, then x is:", "± 5/3", ["5/3 only", "−5/3 only", "0"], "Both 5/3 and −5/3 have absolute value 5/3."),
 mc("On simplification, (x + 4)(x − 4) is equal to:", "x² − 16", ["x² + 16", "x² − 8x + 16", "x² + 8x − 16"], "(a + b)(a − b) = a² − b²."),
 mc("Using a suitable identity, 51² is equal to:", "2601", ["2501", "2611", "2651"], "(50 + 1)² = 2500 + 100 + 1 = 2601."),
 mc("Two equal chords AB and CD of a circle with centre O subtend ∠AOB = 70° at the centre. Then ∠COD is:", "70°", ["35°", "140°", "110°"], "Equal chords subtend equal angles at the centre."),
 mc("The longest chord of a circle of diameter 18 cm has length:", "18 cm", ["9 cm", "36 cm", "√18 cm"], "The diameter is the longest chord."),
 mc("An equilateral triangle has perimeter 36 cm. Its area (by Heron’s formula) is:", "36√3 cm²", ["72√3 cm²", "36 cm²", "18√3 cm²"], "Side 12 cm, s = 18: √(18 × 6 × 6 × 6) = 36√3."),
 mc("The sides of a triangular plot are in the ratio 5 : 12 : 13 and its perimeter is 120 m. The longest side is:", "52 m", ["48 m", "20 m", "60 m"], "One part = 120 ÷ 30 = 4 m; 13 × 4 = 52 m."),
 mc("Two coins are tossed together. The probability of getting exactly one head is:", fr(1, 2), [fr(1, 4), fr(3, 4), "1"], "Outcomes HH, HT, TH, TT; exactly one head: HT, TH → 2/4."),
 mc("A letter is picked at random from the word ‘PROBABILITY’. The probability of picking the letter B is:", fr(2, 11), [fr(1, 11), fr(3, 11), fr(4, 11)], "11 letters, B appears twice."),
 mc("The 20th term of the sequence 3, 7, 11, 15, … is:", "79", ["83", "77", "80"], "t₂₀ = 3 + 19 × 4 = 79."),
 ar("The perpendicular drawn from the centre of a circle to a chord bisects the chord.", "The perpendicular bisector of a chord of a circle passes through the centre of the circle.", 'b', "Both are true (a theorem and its converse), but R does not explain A."),
 ar("The probability of an event can be 1.2.", "The probability of any event lies between 0 and 1, both inclusive.", 'd', "A is false because P(E) ≤ 1; R is a true statement."),
]
B = [
 sa("The side of a square is (3x − 2) cm. Write the expression for its perimeter and find its value for x = 4.", 2, "Perimeter = 4(3x − 2) = <b>12x − 8</b> cm (1)<br>At x = 4: 12 × 4 − 8 = <b>40 cm</b> (1)"),
 OR(sa("Without actual division, state which of " + fr(13, 40) + " and " + fr(7, 30) + " has a terminating decimal expansion. Give a reason.", 2, "40 = 2³ × 5 (only 2 and 5) ⇒ 13/40 terminates (1). 30 = 2 × 3 × 5 has the prime factor 3 ⇒ 7/30 does not terminate (1)."),
    sa("Find two rational numbers between " + fr(2, 3) + " and " + fr(3, 4) + ".", 2, "2/3 = 32/48 and 3/4 = 36/48 (1). Two rational numbers: <b>33/48 and 34/48</b> (= 11/16, 17/24) (1). Any two correct numbers.")),
 sa("Evaluate 103 × 107 using a suitable identity.", 2, "103 × 107 = (105 − 2)(105 + 2) (1) = 105² − 2² = 11025 − 4 = <b>11021</b> (1)"),
 sa("In the figure, O is the centre of the circle and ∠ACB = 62°. Find ∠OAB.", 2, "∠AOB = 2∠ACB = 124° (1)<br>OA = OB ⇒ ∠OAB = ∠OBA = (180° − 124°)/2 = <b>28°</b> (1)", fig=f24),
 sa("Find the second, third and fourth terms of the sequence given by t₁ = 2 and t<sub>n</sub> = (t<sub>n−1</sub>)² − 1 for n ≥ 2.", 2, "t₂ = 2² − 1 = 3; t₃ = 3² − 1 = 8; t₄ = 8² − 1 = 63. (1 for method, 1 for values)"),
]
C = [
 sa("Show that 0.428571428571… = " + fr(3, 7) + ".", 3, "Let x = 0.428571428571… Six digits repeat ⇒ 10⁶x = 428571.428571… (1)<br>10⁶x − x = 428571 ⇒ 999999x = 428571 (1)<br>x = 428571/999999 = <b>3/7</b> (since 428571 = 3 × 142857 and 999999 = 7 × 142857) (1)"),
 OR(sa("In a school, 100 students chose their favourite sport:" + htable(["Sport", "Cricket", "Football", "Kabaddi", "Hockey"], ["Students", 40, 25, 20, 15]) + "A student is chosen at random. Find the probability that the student chose (i) kabaddi, (ii) cricket or hockey, (iii) not football.", 3, "(i) 20/100 = <b>1/5</b> (1) (ii) (40 + 15)/100 = <b>11/20</b> (1) (iii) 75/100 = <b>3/4</b> (1)"),
    sa("The ages of 100 members of a club were recorded:" + htable(["Age (years)", 11, 12, 13, 14, 15], ["Members", 12, 18, 30, 25, 15]) + "A member is chosen at random. Find the probability that the member is (i) 13 years old, (ii) older than 13 years, (iii) younger than 12 years.", 3, "(i) 30/100 = <b>3/10</b> (1) (ii) (25 + 15)/100 = <b>2/5</b> (1) (iii) 12/100 = <b>3/25</b> (1)")),
 sa("A(−3, 2), B(5, 2) and C(5, −4) are three vertices of a rectangle ABCD. Find (i) the coordinates of D, (ii) the length of the diagonal AC, (iii) the area of the rectangle.", 3, "(i) D has the x-coordinate of A and the y-coordinate of C: <b>D(−3, −4)</b> (1)<br>(ii) AB = 8, BC = 6 ⇒ AC = √(64 + 36) = <b>10 units</b> (1)<br>(iii) Area = 8 × 6 = <b>48 square units</b> (1)"),
 sa("Expand: (2x − 3y + 1)².", 3, "Use (a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca with a = 2x, b = −3y, c = 1 (1)<br>= 4x² + 9y² + 1 − 12xy − 6y + 4x (2)<br>= <b>4x² + 9y² + 1 − 12xy + 4x − 6y</b>"),
 sa("In a circle with centre O, chords AB and CD are equal. Prove that they subtend equal angles at the centre.", 3, "In △AOB and △COD: OA = OC, OB = OD (radii) (1); AB = CD (given) (1)<br>△AOB ≅ △COD (SSS) ⇒ ∠AOB = ∠COD (CPCT) (1)"),
 OR(sa("Find the area of the triangle whose sides are 7 cm, 15 cm and 20 cm, using Heron’s formula.", 3, "s = (7 + 15 + 20)/2 = 21 (1)<br>Area = √[21 × 14 × 6 × 1] (1) = √1764 = <b>42 cm²</b> (1)"),
    sa("Using Heron’s formula, find the area of an equilateral triangle of side 16 cm. (Leave the answer in terms of √3.)", 3, "s = 24 (1); Area = √[24 × 8 × 8 × 8] (1) = √12288 = <b>64√3 cm²</b> (1)")),
]
D = [
 sa("Prove that the sum of either pair of opposite angles of a cyclic quadrilateral is 180°.", 5, "Given: cyclic quadrilateral ABCD with centre O. To prove: ∠A + ∠C = 180°, ∠B + ∠D = 180°. Construction: join OB and OD. (1)<br>Arc BCD subtends ∠BOD at the centre and ∠BAD at point A on the remaining circle ⇒ ∠BOD = 2∠BAD (1)<br>The same arc BAD subtends the reflex angle ∠BOD at the centre and ∠BCD at C ⇒ reflex ∠BOD = 2∠BCD (1)<br>Adding: ∠BOD + reflex ∠BOD = 2(∠BAD + ∠BCD) (1)<br>360° = 2(∠A + ∠C) ⇒ ∠A + ∠C = 180°; similarly ∠B + ∠D = 180°. (1)", fig=f32),
 sa("(i) Express 3.2444… (that is, 3.24 with the 4 repeating) in the form p/q in lowest terms. (2½)<br>(ii) If x = −" + fr(7, 4) + " and y = " + fr(5, 6) + ", find |x − y| and |x|·|y|. (2½)", 5, "(i) Let x = 3.2444…; 100x = 324.444…, 10x = 32.444… (1) ⇒ 90x = 292 (1) ⇒ x = 292/90 = <b>146/45</b> (½)<br>(ii) x − y = −7/4 − 5/6 = −31/12 ⇒ |x − y| = <b>31/12</b> (1½); |x||y| = 7/4 × 5/6 = <b>35/24</b> (1)"),
 OR(sa("How many two-digit numbers are divisible by 4? Find their sum. (2½ + 2½)", 5, "Numbers: 12, 16, …, 96 — AP with a = 12, d = 4, l = 96 (1)<br>n = (96 − 12)/4 + 1 = <b>22</b> (1½)<br>Sum = 22/2 × (12 + 96) = 11 × 108 = <b>1188</b> (2½)"),
    sa("The rungs of a ladder decrease uniformly in length from 45 cm at the bottom to 25 cm at the top. The rungs are 25 cm apart and the top rung is 2½ m above the bottom rung. Find the number of rungs and the total length of wood needed for the rungs.", 5, "Number of rungs = 250/25 + 1 = <b>11</b> (2)<br>Lengths form an AP with a = 45, l = 25 (1)<br>Total length = 11/2 × (45 + 25) = <b>385 cm</b> (= 3.85 m) (2)")),
 OR(sa("A triangular park has sides 15 m, 20 m and 25 m. Find (i) its area using Heron’s formula, (ii) the cost of fencing it at ₹30 per metre, (iii) the cost of turfing it at ₹8 per m². (2 + 1½ + 1½)", 5, "(i) s = 30; area = √(30 × 15 × 10 × 5) = √22500 = <b>150 m²</b> (2)<br>(ii) Perimeter = 60 m; cost = 60 × 30 = <b>₹1800</b> (1½)<br>(iii) Cost = 150 × 8 = <b>₹1200</b> (1½)"),
    sa("An isosceles triangle has perimeter 36 cm and each of its equal sides is 13 cm. Find the area of the triangle and the length of the altitude on its base.", 5, "Base = 36 − 26 = 10 cm (1); s = 18 (½)<br>Area = √[18 × 5 × 5 × 8] = √3600 = <b>60 cm²</b> (2½)<br>½ × 10 × h = 60 ⇒ h = <b>12 cm</b> (1)")),
]
E = [
 case("Aarav starts saving for a school trip. He saves ₹100 in the first month and increases his saving by ₹50 every month, so his saving in the n-th month is t<sub>n</sub> = 50n + 50.",
      [sub("How much does he save in the 6th month?", 1, "t₆ = 50 × 6 + 50 = <b>₹350</b>"),
       sub("The monthly savings form an AP. Write its common difference.", 1, "t₂ − t₁ = 150 − 100 = <b>₹50</b>"),
       OR(sub("In which month will he save ₹1000?", 2, "50n + 50 = 1000 (1) ⇒ n = <b>19th month</b> (1)"),
          sub("Find the total amount he saves in the first 10 months.", 2, "a = 100, l = t₁₀ = 550 (1); S = 10/2 × (100 + 550) = <b>₹3250</b> (1)"))]),
 case("The map of a colony is drawn on a grid (1 unit = 100 m). Meera’s house is at A(2, 3), Karan’s house is at B(6, 3) and Zoya’s house is at C(6, −1).",
      [sub("Find the distance between Meera’s and Karan’s houses (in units).", 1, "AB = |6 − 2| = <b>4 units</b> (= 400 m)"),
       sub("The school is at the midpoint of AC. Find its coordinates.", 1, "(" + fr("2 + 6", 2) + ", " + fr("3 − 1", 2) + ") = <b>(4, 1)</b>"),
       OR(sub("A park is to be located at D so that ABCD is a square. Find the coordinates of D.", 2, "AB = BC = 4 and angle B is a right angle (1) ⇒ D(2, −1) (1)" + sol37),
          sub("Find the straight-line distance between the houses of Meera and Zoya.", 2, "AC = √[(6 − 2)² + (−1 − 3)²] (1) = √32 = <b>4√2 units</b> (1)"))], fig=f37),
 case("A spinner is divided into 8 equal sectors numbered 1 to 8. The spinner is spun once and the number on the sector that stops at the pointer is noted.",
      [sub("Find the probability of getting the number 7.", 1, "P = <b>1/8</b>"),
       sub("Find the probability of getting a prime number.", 1, "Primes: 2, 3, 5, 7 ⇒ P = 4/8 = <b>1/2</b>"),
       OR(sub("Find the probability of getting a number greater than 5.", 2, "Favourable: 6, 7, 8 (1) ⇒ P = <b>3/8</b> (1)"),
          sub("Find the probability of getting a multiple of 3 or a multiple of 4.", 2, "Favourable: 3, 4, 6, 8 (1) ⇒ P = 4/8 = <b>1/2</b> (1)"))]),
]
SECTIONS = sections(A, B, C, D, E)
