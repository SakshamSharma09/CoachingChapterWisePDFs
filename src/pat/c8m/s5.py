from lib8 import *
q1 = mcqgroup([
 m("Which of the following is a perfect square?", "1296", ["1200","1250","1300"], "36² = 1296."),
 m("The cube root of −343 is:", "−7", ["7","−49","−3.5"], "(−7)³ = −343."),
 m("The units digit of 17² is:", "9", ["7","1","4"], "17² = 289."),
 m("The value of (−2)<sup>−3</sup> is:", "−1/8", ["1/8","−8","8"], "(−2)⁻³ = 1/(−2)³ = −1/8."),
 m("349 in Roman numerals is:", "CCCXLIX", ["CCCIL","CCXXXXIX","CCCXXXXIX"], "300 = CCC, 40 = XL, 9 = IX."),
 m("(1010)<sub>2</sub> in decimal is:", "10", ["8","12","5"], "8 + 0 + 2 + 0 = 10."),
 m("A quadrilateral whose diagonals are equal and bisect each other at right angles is a:", "square", ["rectangle","rhombus","kite"], "Only a square has all these properties together."),
 m("The diagonals of a kite meet at:", "right angles", ["60°","45°","any angle"], "The diagonals of a kite are perpendicular."),
 m("(x − 5)(x + 5) equals:", "x² − 25", ["x² + 25","x² − 10x + 25","x² − 10"], "(a − b)(a + b) = a² − b²."),
 m("If x + 1/x = 3, then x² + 1/x² equals:", "7", ["9","11","5"], "9 − 2 = 7."),
 m("If 4 : 7 = 20 : x, then x is:", "35", ["28","32","40"], "4x = 140 ⇒ x = 35."),
 m("6 men build a wall in 10 days. 15 men will build it in:", "4 days", ["25 days","6 days","9 days"], "Inverse variation: 6 × 10 = 15 × d ⇒ d = 4.")])
b = [
 sa("Find the square root of 1521 by prime factorisation.", 2, "1521 = 3² × 13² (1 mark)<br>√1521 = 3 × 13 = 39 (1 mark)"),
 sa("Find the smallest number by which 500 must be multiplied to get a perfect cube.", 2, "500 = 2² × 5³ (1 mark)<br>Multiply by 2: 1000 = 10³ (1 mark)"),
 sa("Write 0.0000081 in standard form and 7.5 × 10⁴ in usual form.", 2, "8.1 × 10⁻⁶ (1 mark)<br>75000 (1 mark)"),
 OR(sa("Write the Roman numeral MCDXLVII in the Hindu-Arabic system.", 2, "1000 + 400 + 40 + 7 (1 mark) = 1447 (1 mark)"),
    sa("Convert (321)₄ into a decimal number.", 2, "3×16 + 2×4 + 1 (1 mark) = 57 (1 mark)")),
 sa("Two adjacent angles of a parallelogram are in the ratio 1 : 4. Find them.", 2, "Sum = 180° ⇒ 5 parts = 180°, 1 part = 36° (1 mark)<br>Angles: 36° and 144° (1 mark)"),
 sa("Expand (2a − 3)² and (x + 7)(x + 3).", 2, "(2a − 3)² = 4a² − 12a + 9 (1 mark)<br>(x + 7)(x + 3) = x² + 10x + 21 (1 mark)")]
c = [
 sa("Find the cube root of −1.331 and the square root of 0.0625.", 3, "∛(−1.331) = −∛(1331/1000) = −11/10 = −1.1 (1½ marks)<br>√0.0625 = √(625/10000) = 25/100 = 0.25 (1½ marks)"),
 OR(sa("The angles of a quadrilateral are x°, (x + 10)°, (x + 20)° and (x + 30)°. Find each angle.", 3, "4x + 60 = 360 (1 mark) ⇒ x = 75 (1 mark)<br>Angles: 75°, 85°, 95°, 105° (1 mark)"),
    sa("The diagonals of rectangle ABCD meet at O. If OA = 5 cm and ∠AOB = 60°, find BD and AB.", 3, "Diagonals are equal and bisect each other: OB = OA = 5 cm, BD = 10 cm (1½ marks)<br>ΔOAB has OA = OB and ∠AOB = 60°, so it is equilateral ⇒ AB = 5 cm (1½ marks)")),
 sa("Using identities, find: (i) 103² &nbsp; (ii) 59 × 61 &nbsp; (iii) (2.1)²", 3, "(i) (100 + 3)² = 10000 + 600 + 9 = 10609 (1 mark)<br>(ii) (60 − 1)(60 + 1) = 3600 − 1 = 3599 (1 mark)<br>(iii) (2 + 0.1)² = 4 + 0.4 + 0.01 = 4.41 (1 mark)")]
d = [
 OR(sa("(i) Find the smallest number by which 2700 must be divided so that the quotient is a perfect square. Also find the square root of the quotient.<br>(ii) Find the smallest number to be added to 1000 to make it a perfect square.", 5, "(i) 2700 = 2² × 3³ × 5² (1 mark); divide by 3 (1 mark); quotient 900, √900 = 30 (1 mark)<br>(ii) 31² = 961 < 1000 < 32² = 1024 (1 mark); add 1024 − 1000 = 24 (1 mark)"),
    sa("(i) Find the cube root of 17576 by prime factorisation.<br>(ii) A cubical box has volume 5.832 m³. Find the length of its edge.", 5, "(i) 17576 = 2³ × 13³ (2 marks); cube root = 2 × 13 = 26 (1 mark)<br>(ii) 5.832 = 5832/1000 = (18/10)³ ⇒ edge = 1.8 m (2 marks)")),
 OR(sa("Simplify: (i) 3⁻¹ + 5⁻¹ (ii) (2⁵ × 2⁻²) ÷ 2⁻¹ (iii) (−5)⁰ × 5⁻² (iv) Write 0.00000052 in standard form (v) Find x if 2ˣ ÷ 2⁻³ = 2⁸", 5, "(i) 1/3 + 1/5 = 8/15 (ii) 2³ ÷ 2⁻¹ = 2⁴ = 16 (iii) 1 × 1/25 = 1/25 (iv) 5.2 × 10⁻⁷ (v) x + 3 = 8 ⇒ x = 5 (1 mark each)"),
    sa("(i) Write 1994 in Roman numerals. (ii) Convert 77 to base 2. (iii) Add (101)₂ and (11)₂. (iv) Convert (143)₅ to decimal. (v) Convert 100 to base 3.", 5, "(i) MCMXCIV (ii) 77 = 64 + 8 + 4 + 1 = (1001101)₂ (iii) 5 + 3 = 8 = (1000)₂ (iv) 25 + 20 + 3 = 48 (v) 100 = 81 + 18 + 1 = (10201)₃ (1 mark each)")),
 sa("(i) Divide ₹ 5,400 among three persons in the ratio 2 : 3 : 4.<br>(ii) If 12 notebooks cost ₹ 180, find the cost of 20 notebooks.<br>(iii) 3 pumps empty a tank in 8 hours. How long will 4 pumps take?<br>(iv) Find x if 5 : 8 :: x : 56.<br>(v) The ages of two brothers are in the ratio 4 : 5 and their sum is 45 years. Find their ages.", 5,
    "(i) 9 parts, 1 part = ₹ 600 ⇒ ₹ 1200, ₹ 1800, ₹ 2400 (1 mark)<br>(ii) 1 notebook = ₹ 15 ⇒ ₹ 300 (1 mark)<br>(iii) Inverse: 3 × 8 = 4 × t ⇒ t = 6 hours (1 mark)<br>(iv) 8x = 280 ⇒ x = 35 (1 mark)<br>(v) 9 parts = 45 ⇒ 20 and 25 years (1 mark)")]
kite = quad([(110,29),(50,84),(110,149),(170,84)], ['A','B','C','D'], F.line(110,29,110,149,'#555',1,'4,3')+F.line(50,84,170,84,'#555',1,'4,3')+F.text(116,80,'O','start'), 220, 185)
e = [
 case("A kite-shaped decoration ABCD is cut from coloured paper. AB = AD = 5 cm, CB = CD = 9 cm, ∠BAD = 70° and ∠ABC = ∠ADC = 100°. The diagonals AC and BD meet at O.",
      [sub("Which two angles of the kite are equal?", 1, "∠ABC = ∠ADC (= 100°)"),
       sub("Find the perimeter of the decoration.", 1, "2(5 + 9) = 28 cm"),
       OR(sub("Find ∠BCD.", 2, "Angle sum 360°: ∠C = 360° − (70° + 100° + 100°) (1 mark) = 90° (1 mark)"),
          sub("Find ∠AOB and ∠ABO.", 2, "Diagonals of a kite are perpendicular ⇒ ∠AOB = 90° (1 mark); AC bisects ∠A ⇒ ∠BAO = 35°, so ∠ABO = 90° − 35° = 55° (1 mark)"))], fig=kite),
 case("A square garden has an area of 2025 m². The owner wants to fence it on all four sides.",
      [sub("Find the side of the garden.", 1, "√2025 = 45 m"),
       sub("Find the length of fencing required.", 1, "4 × 45 = 180 m"),
       OR(sub("Find the cost of fencing at ₹ 120 per metre.", 2, "180 × 120 (1 mark) = ₹ 21,600 (1 mark)"),
          sub("The side is increased by 4 m. Find the area of the new square garden.", 2, "New side = 49 m (1 mark); area = 49² = 2401 m² (1 mark)"))]),
 case("A rectangular hall has length (x + 7) m and width (x + 3) m, where x is a number of metres chosen by the architect. The floor is to be carpeted.",
      [sub("Write the area of the hall as a polynomial in x.", 1, "(x + 7)(x + 3) = x² + 10x + 21"),
       sub("Find the area when x = 5.", 1, "25 + 50 + 21 = 96 m² (dimensions 12 m × 8 m)"),
       OR(sub("Find the cost of carpeting at ₹ 150 per m² when x = 5.", 2, "Area = 96 m² (1 mark); cost = 96 × 150 = ₹ 14,400 (1 mark)"),
          sub("Show that (x + 7)(x + 3) = (x + 5)² − 4.", 2, "(x + 5)² − 4 = x² + 10x + 25 − 4 (1 mark) = x² + 10x + 21 = (x + 7)(x + 3) (1 mark)"))])]
META = meta(5); SECTIONS = secs(q1, b, c, d, e)
