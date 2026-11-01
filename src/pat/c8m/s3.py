from lib8 import *
q1 = mcqgroup([
 m("A perfect square can never end with the digit:", "8", ["1","4","9"], "Squares end only in 0, 1, 4, 5, 6 or 9."),
 m("The cube root of 0.027 is:", "0.3", ["0.03","3","0.9"], "0.027 = 27/1000 = (3/10)³ ⇒ 0.3."),
 m("The sum of the first 12 odd natural numbers is:", "144", ["24","132","156"], "Sum of first n odd numbers = n² = 12² = 144."),
 m("The value of (−3)<sup>−2</sup> is:", "1/9", ["−1/9","−9","9"], "(−3)⁻² = 1/(−3)² = 1/9."),
 m("1999 written in Roman numerals is:", "MCMXCIX", ["MDCCCCLXXXXVIIII","MCMXCVIIII","MXMIX"], "1000 = M, 900 = CM, 90 = XC, 9 = IX."),
 m("Which of the following is NOT a valid base-4 numeral?", "1234", ["1302","2031","3210"], "Digits in base 4 can only be 0, 1, 2, 3; ‘4’ is not allowed."),
 m("Three angles of a quadrilateral are 80°, 100° and 70°. The fourth angle is:", "110°", ["100°","90°","120°"], "360° − (80 + 100 + 70) = 110°."),
 m("The diagonals of a rhombus:", "bisect each other at right angles", ["are always equal","are parallel","do not intersect"], "Property of a rhombus: diagonals are perpendicular bisectors of each other."),
 m("Which of the following numbers is divisible by 11?", "3025", ["2728 + 1 = 2729","3026","3035"], "(3 + 2) − (0 + 5) = 0 ⇒ 3025 is divisible by 11 (3025 = 11 × 275)."),
 m("(x + 2)(x + 3) equals:", "x² + 5x + 6", ["x² + 6x + 5","x² + 5x + 5","x² + 6"], "x² + 3x + 2x + 6."),
 m("If a + b = 10 and ab = 21, then (a − b)² equals:", "16", ["79","58","100"], "(a − b)² = (a + b)² − 4ab = 100 − 84 = 16."),
 m("A car travels 150 km in 3 hours. At the same speed it will travel in 5 hours:", "250 km", ["200 km","300 km","350 km"], "Speed = 50 km/h ⇒ 5 × 50 = 250 km.")])
b = [
 sa("Find the cube root of 1728 by prime factorisation.", 2, "1728 = 2⁶ × 3³ (1 mark)<br>∛1728 = 2² × 3 = 12 (1 mark)"),
 sa("Write 3.56 × 10<sup>5</sup> and 2.1 × 10<sup>−3</sup> in usual form.", 2, "3.56 × 10⁵ = 356000 (1 mark)<br>2.1 × 10⁻³ = 0.0021 (1 mark)"),
 sa("Write 1999 in Roman numerals.", 2, "1000 + 900 + 90 + 9 (1 mark) = MCMXCIX (1 mark)"),
 OR(sa("Add (1101)₂ and (1011)₂ and give the answer in base 2.", 2, "13 + 11 = 24 (1 mark); 24 = (11000)₂ (1 mark). Direct binary addition is also accepted."),
    sa("Convert the decimal number 100 into base 7.", 2, "100 = 2×49 + 0×7 + 2 (1 mark) ⇒ (202)₇ (1 mark)")),
 sa("In parallelogram ABCD, ∠A = (2x + 10)° and ∠C = (3x − 20)°. Find x and ∠A.", 2, "Opposite angles are equal: 2x + 10 = 3x − 20 ⇒ x = 30 (1 mark)<br>∠A = 70° (1 mark)"),
 sa("Find the ratio of 3 m 60 cm to 2.4 m in simplest form.", 2, "3 m 60 cm = 360 cm; 2.4 m = 240 cm (1 mark)<br>360 : 240 = 3 : 2 (1 mark)")]
c = [
 sa("Without actual division, check whether 678432 is divisible by (i) 8 (ii) 11. Give reasons.", 3, "(i) Last three digits 432 = 8 × 54 ⇒ divisible by 8 (1½ marks)<br>(ii) (6 + 8 + 3) − (7 + 4 + 2) = 17 − 13 = 4, not 0 or a multiple of 11 ⇒ not divisible by 11 (1½ marks)"),
 OR(sa("In parallelogram ABCD, AB = (2x + 3) cm and DC = (3x − 5) cm. Find x and the length of AB.", 3, "Opposite sides are equal: 2x + 3 = 3x − 5 (1 mark) ⇒ x = 8 (1 mark)<br>AB = 2(8) + 3 = 19 cm (1 mark)"),
    sa("The diagonals PR and QS of a rectangle PQRS meet at O. If ∠POQ = 110°, find ∠OPQ.", 3, "Diagonals of a rectangle are equal and bisect each other ⇒ OP = OQ (1 mark)<br>In ΔOPQ: ∠OPQ = ∠OQP (1 mark) = (180° − 110°)/2 = 35° (1 mark)")),
 sa("Using suitable identities, find: (i) 97 × 103 &nbsp; (ii) 205² &nbsp; (iii) 99²", 3, "(i) (100 − 3)(100 + 3) = 10000 − 9 = 9991 (1 mark)<br>(ii) (200 + 5)² = 40000 + 2000 + 25 = 42025 (1 mark)<br>(iii) (100 − 1)² = 10000 − 200 + 1 = 9801 (1 mark)")]
d = [
 OR(sa("(i) Find the smallest number by which 3528 must be divided so that the quotient is a perfect square. Also find the square root of the quotient.<br>(ii) Find the square root of 0.0289.", 5, "(i) 3528 = 2³ × 3² × 7² (1 mark); divide by 2 (1 mark); quotient 1764 = 2² × 3² × 7², √ = 42 (1 mark)<br>(ii) 0.0289 = 289/10000 ⇒ √ = 17/100 = 0.17 (2 marks)"),
    sa("(i) Find the smallest number by which 1125 must be multiplied so that the product is a perfect cube. Also find the cube root of the product.<br>(ii) The volume of a cubical tank is 0.343 m³. Find the length of its edge.", 5, "(i) 1125 = 3² × 5³ (1 mark); multiply by 3 (1 mark); product 3375 = 3³ × 5³, cube root 15 (1 mark)<br>(ii) 0.343 = 343/1000 = (7/10)³ ⇒ edge = 0.7 m (2 marks)")),
 OR(sa("Write in standard form: (i) 4,56,00,000 (ii) 0.00000072. Write in usual form: (iii) 7.3 × 10⁻⁴ (iv) 5.2 × 10⁶. (v) Find 2 × 10⁵ + 3 × 10⁴ in standard form.", 5, "(i) 4.56 × 10⁷ (ii) 7.2 × 10⁻⁷ (iii) 0.00073 (iv) 5200000 (v) 2.3 × 10⁵ (1 mark each)"),
    sa("Simplify: (i) (2³)⁻² × 2⁷ (ii) 6⁵ ÷ 6⁻² (iii) (4⁻¹ + 2⁻¹)⁻¹ (iv) (10⁻³)⁻² (v) (a²b)³ ÷ (ab)²", 5, "(i) 2⁻⁶ × 2⁷ = 2 (ii) 6⁷ (iii) (1/4 + 1/2)⁻¹ = (3/4)⁻¹ = 4/3 (iv) 10⁶ (v) a⁶b³ ÷ a²b² = a⁴b (1 mark each)")),
 sa("(i) Write the ratio of 2.5 kg to 750 g in simplest form.<br>(ii) Divide ₹ 1,800 among A, B and C in the ratio 2 : 3 : 4.<br>(iii) If 8 pens cost ₹ 96, find the cost of 15 pens.<br>(iv) Find x if 6 : x :: 9 : 15.<br>(v) The ratio of boys to girls in a class is 5 : 4 and there are 36 students. Find the number of girls.", 5,
    "(i) 2500 g : 750 g = 10 : 3 (1 mark)<br>(ii) Total parts 9, 1 part = ₹ 200 ⇒ ₹ 400, ₹ 600, ₹ 800 (1 mark)<br>(iii) 1 pen = ₹ 12 ⇒ 15 pens = ₹ 180 (1 mark)<br>(iv) 9x = 6 × 15 ⇒ x = 10 (1 mark)<br>(v) Girls = 4/9 × 36 = 16 (1 mark)")]
par = quad([(50,110),(200,110),(240,30),(90,30)], ['A','B','C','D'], F.line(50,110,240,30,'#555',1,'4,3')+F.line(200,110,90,30,'#555',1,'4,3')+F.text(150,76,'O','start'), 270, 150)
e = [
 case("A flooring contractor cuts parallelogram-shaped tiles ABCD. In one tile, AB = 12 cm, BC = 8 cm and ∠A = 65°. The diagonals AC and BD intersect at O.",
      [sub("Write the length of CD.", 1, "Opposite sides of a parallelogram are equal: CD = AB = 12 cm"),
       sub("Find ∠B.", 1, "Adjacent angles are supplementary: ∠B = 180° − 65° = 115°"),
       OR(sub("Show that AO = OC.", 2, "In ΔAOB and ΔCOD: AB = CD, ∠OAB = ∠OCD, ∠OBA = ∠ODC (alternate angles) (1 mark) ⇒ ΔAOB ≅ ΔCOD (ASA), so AO = OC (1 mark)"),
          sub("Find the perimeter of the tile and the cost of an edging strip around 50 such tiles at ₹ 2 per cm.", 2, "Perimeter = 2(12 + 8) = 40 cm (1 mark); cost = 50 × 40 × 2 = ₹ 4000 (1 mark)"))], fig=par),
 case("Kabir arranges square tiles to form bigger and bigger squares: 1 tile (1×1), 4 tiles (2×2), 9 tiles (3×3), and so on. He notices that each new square needs the next odd number of extra tiles.",
      [sub("How many tiles are needed for the 8th square?", 1, "8² = 64 tiles"),
       sub("How many extra tiles are needed to change an 8 × 8 square into a 9 × 9 square?", 1, "81 − 64 = 17 tiles (the 9th odd number)"),
       OR(sub("Show that the sum of the first 10 odd numbers is a perfect square and name it.", 2, "1 + 3 + 5 + … + 19 = 100 (1 mark) = 10², a perfect square (1 mark)"),
          sub("A square arrangement uses 441 tiles. How many more tiles are needed to make the next larger square?", 2, "√441 = 21 (1 mark); next square 22² = 484 ⇒ 484 − 441 = 43 tiles (1 mark)"))]),
 case("Three friends — Ria, Sana and Tej — travel by a shared taxi for different distances: Ria 3 km, Sana 5 km and Tej 7 km. The total fare of ₹ 450 is divided in the ratio of the distances travelled.",
      [sub("Write the ratio of the shares of Ria, Sana and Tej.", 1, "3 : 5 : 7"),
       sub("Find Sana’s share of the fare.", 1, "Total parts = 15; 1 part = ₹ 30; Sana pays 5 × 30 = ₹ 150"),
       OR(sub("Find the difference between Tej’s share and Ria’s share.", 2, "Tej = 7 × 30 = ₹ 210; Ria = 3 × 30 = ₹ 90 (1 mark); difference = ₹ 120 (1 mark)"),
          sub("Another day the same three friends pay ₹ 600 for the same distances. Find the amount Ria pays and show that the ratio 3 : 5 : 7 is unchanged.", 2, "1 part = ₹ 40, Ria pays ₹ 120 (1 mark); shares 120 : 200 : 280 = 3 : 5 : 7 (1 mark)"))])]
META = meta(3); SECTIONS = secs(q1, b, c, d, e)
