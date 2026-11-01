from lib8 import *
q1 = mcqgroup([
 m("The square root of 0.0081 is:", "0.09", ["0.9","0.009","0.081"], "0.0081 = 81/10000 ⇒ √ = 9/100 = 0.09."),
 m("The cube of −4 is:", "−64", ["64","−16","16"], "(−4)³ = −64."),
 m("The number of non-square numbers between 6² and 7² is:", "12", ["6","13","24"], "Between n² and (n+1)² there are 2n non-squares: 2 × 6 = 12."),
 m("The value of 2<sup>−3</sup> × 2<sup>5</sup> is:", "4", ["2","8","1/4"], "2^(−3+5) = 2² = 4."),
 m("The Roman numeral XLIV stands for:", "44", ["46","64","36"], "XL = 40 and IV = 4 ⇒ 44."),
 m("(101)<sub>2</sub> in the decimal system is:", "5", ["3","6","7"], "1×4 + 0×2 + 1 = 5."),
 m("A quadrilateral with all sides equal and one angle 90° is a:", "square", ["rhombus that is not a square","kite","trapezium"], "A rhombus with a right angle is a square."),
 m("The diagonals of every parallelogram:", "bisect each other", ["are equal","are perpendicular","are parallel"], "Basic property of a parallelogram."),
 m("(a + b)² − (a − b)² equals:", "4ab", ["2ab","2a² + 2b²","0"], "(a² + 2ab + b²) − (a² − 2ab + b²) = 4ab."),
 m("5 kg : 500 g in simplest form is:", "10 : 1", ["1 : 10","5 : 500","1 : 100"], "5000 g : 500 g = 10 : 1."),
 m("x² − 49 can be factorised as:", "(x − 7)(x + 7)", ["(x − 7)²","(x + 7)²","(x − 49)(x + 1)"], "a² − b² = (a − b)(a + b)."),
 m("If 3 : 5 :: x : 20, then x equals:", "12", ["15","8","10"], "5x = 60 ⇒ x = 12.")])
b = [
 sa("Find the square root of 2025 by prime factorisation.", 2, "2025 = 3⁴ × 5² (1 mark)<br>√2025 = 3² × 5 = 45 (1 mark)"),
 sa("Is 392 a perfect cube? If not, find the smallest number by which it must be multiplied to get a perfect cube.", 2, "392 = 2³ × 7²; 7 appears twice, not a multiple of 3 times, so not a perfect cube (1 mark)<br>Multiply by 7: 2744 = 14³ (1 mark)"),
 sa("Write 53,000,000 and 0.000345 in standard form.", 2, "5.3 × 10⁷ (1 mark)<br>3.45 × 10⁻⁴ (1 mark)"),
 OR(sa("Write 2024 in Roman numerals.", 2, "2000 = MM, 20 = XX, 4 = IV (1 mark) ⇒ MMXXIV (1 mark)"),
    sa("Convert (234)₅ into a decimal number.", 2, "2×25 + 3×5 + 4 (1 mark) = 69 (1 mark)")),
 sa("In rhombus ABCD, ∠A = 70°. Find ∠B and ∠C.", 2, "Adjacent angles are supplementary: ∠B = 110° (1 mark)<br>Opposite angles are equal: ∠C = ∠A = 70° (1 mark)"),
 sa("Expand (x + 4)² and (3x + 2)(3x − 2).", 2, "(x + 4)² = x² + 8x + 16 (1 mark)<br>(3x + 2)(3x − 2) = 9x² − 4 (1 mark)")]
c = [
 sa("Find the square root of 1.69 and the cube root of 0.512.", 3, "√1.69 = √(169/100) = 13/10 = 1.3 (1½ marks)<br>∛0.512 = ∛(512/1000) = 8/10 = 0.8 (1½ marks)"),
 OR(sa("The angles of a quadrilateral are in the ratio 2 : 3 : 3 : 4. Find each angle.", 3, "Total parts = 12; 1 part = 360°/12 = 30° (1 mark)<br>Angles: 60°, 90°, 90°, 120° (2 marks)"),
    sa("In parallelogram PQRS, ∠P : ∠Q = 2 : 3. Find all four angles.", 3, "∠P + ∠Q = 180° ⇒ 5 parts = 180°, 1 part = 36° (1 mark)<br>∠P = 72° = ∠R, ∠Q = 108° = ∠S (2 marks)")),
 sa("Using identities, evaluate: (i) (1.02)² &nbsp; (ii) 48 × 52 &nbsp; (iii) 302²", 3, "(i) (1 + 0.02)² = 1 + 0.04 + 0.0004 = 1.0404 (1 mark)<br>(ii) (50 − 2)(50 + 2) = 2500 − 4 = 2496 (1 mark)<br>(iii) (300 + 2)² = 90000 + 1200 + 4 = 91204 (1 mark)")]
d = [
 OR(sa("(i) Find the smallest number by which 288 must be multiplied so that the product is a perfect square. Find the square root of the product.<br>(ii) Find the square root of 5476 by prime factorisation.", 5, "(i) 288 = 2⁵ × 3² (1 mark); multiply by 2 (1 mark); 576 = 24² ⇒ √ = 24 (1 mark)<br>(ii) 5476 = 2² × 37² (1 mark) ⇒ √ = 2 × 37 = 74 (1 mark)"),
    sa("(i) Find the smallest number by which 1944 must be divided so that the quotient is a perfect cube. Find the cube root of the quotient.<br>(ii) The volume of a cube is 0.064 m³. Find the length of its edge.", 5, "(i) 1944 = 2³ × 3⁵ (1 mark); divide by 3² = 9 (1 mark); quotient 216 = 6³ ⇒ cube root 6 (1 mark)<br>(ii) 0.064 = 64/1000 = (4/10)³ ⇒ edge = 0.4 m (2 marks)")),
 OR(sa("Simplify: (i) 5⁻³ × 5⁵ (ii) (2/3)⁻³ (iii) 7⁶ ÷ 7⁸ (iv) (x⁻²y³)² (v) 3⁰ + 4⁻¹", 5, "(i) 5² = 25 (ii) 27/8 (iii) 7⁻² = 1/49 (iv) y⁶/x⁴ (v) 1 + 1/4 = 5/4 (1 mark each)"),
    sa("(i) Write 1994 in Roman numerals. (ii) Convert 45 to base 2. (iii) Convert (212)₃ to decimal. (iv) Add (110)₂ and (111)₂. (v) Convert 58 to base 8.", 5, "(i) MCMXCIV (ii) 45 = 32 + 8 + 4 + 1 = (101101)₂ (iii) 2×9 + 1×3 + 2 = 23 (iv) 6 + 7 = 13 = (1101)₂ (v) 58 = 7×8 + 2 = (72)₈ (1 mark each)")),
 sa("(i) Divide ₹ 2,400 among A, B and C in the ratio 3 : 5 : 4.<br>(ii) 12 workers finish a job in 15 days. How many days will 20 workers take?<br>(iii) Find x if 4 : 9 :: 16 : x.<br>(iv) A train travels 240 km in 4 hours. How long will it take for 420 km at the same speed?<br>(v) A 40-litre mixture has milk and water in the ratio 7 : 3. Find the quantity of water.", 5,
    "(i) 12 parts, 1 part = ₹ 200 ⇒ ₹ 600, ₹ 1000, ₹ 800 (1 mark)<br>(ii) Inverse variation: 12 × 15 = 20 × d ⇒ d = 9 days (1 mark)<br>(iii) 4x = 144 ⇒ x = 36 (1 mark)<br>(iv) 60 km/h ⇒ 420 ÷ 60 = 7 hours (1 mark)<br>(v) Water = 3/10 × 40 = 12 litres (1 mark)")]
rh = quad([(30,75),(110,25),(190,75),(110,125)], ['A','B','C','D'], F.line(30,75,190,75,'#555',1,'4,3')+F.line(110,25,110,125,'#555',1,'4,3')+F.text(116,70,'O','start'), 220, 150)
kite = quad([(110,29),(50,84),(110,149),(170,84)], ['A','B','C','D'], F.line(110,29,110,149,'#555',1,'4,3')+F.line(50,84,170,84,'#555',1,'4,3')+F.text(116,80,'O','start'), 220, 185)
e = [
 case("A rhombus-shaped garden ABCD has diagonals AC = 16 m and BD = 12 m meeting at O. Each side of the garden is 10 m. ∠ABC = 100°.",
      [sub("What is the angle between the diagonals AC and BD?", 1, "The diagonals of a rhombus are perpendicular: 90°"),
       sub("Find the length of AO.", 1, "Diagonals bisect each other: AO = 16/2 = 8 m"),
       OR(sub("Find the cost of fencing the garden at ₹ 50 per metre.", 2, "Perimeter = 4 × 10 = 40 m (1 mark); cost = 40 × 50 = ₹ 2000 (1 mark)"),
          sub("Find ∠BAD and ∠OAB.", 2, "∠BAD = 180° − 100° = 80° (1 mark); diagonal AC bisects ∠A ⇒ ∠OAB = 40° (1 mark)"))], fig=rh),
 case("In a laboratory, a bacterial culture doubles every hour. Starting with 1 bacterium, the number after n hours is 2<sup>n</sup>.",
      [sub("How many bacteria are there after 5 hours?", 1, "2⁵ = 32"),
       sub("How many bacteria are there after 10 hours?", 1, "2¹⁰ = 1024"),
       OR(sub("After how many hours will the count reach 4096?", 2, "4096 = 2¹² (1 mark) ⇒ 12 hours (1 mark)"),
          sub("How many times more bacteria are there at 12 hours than at 9 hours?", 2, "2¹² ÷ 2⁹ = 2³ (1 mark) = 8 times (1 mark)"))]),
 case("A fruit punch is made by mixing orange juice, pineapple juice and soda in the ratio 4 : 3 : 1. A party needs 4 litres of punch.",
      [sub("What is the total number of parts in the mixture?", 1, "4 + 3 + 1 = 8"),
       sub("How much orange juice is needed for 4 litres of punch?", 1, "1 part = 4/8 = 0.5 L; orange juice = 4 × 0.5 = 2 L"),
       OR(sub("How much soda is needed to make 10 litres of the same punch?", 2, "1 part = 10/8 = 1.25 L (1 mark); soda = 1 part = 1.25 L (1 mark)"),
          sub("Only 4.5 litres of pineapple juice is available. What is the maximum amount of punch that can be made keeping the same ratio?", 2, "3 parts = 4.5 L ⇒ 1 part = 1.5 L (1 mark); total = 8 × 1.5 = 12 L (1 mark)"))])]
META = meta(4); SECTIONS = secs(q1, b, c, d, e)
