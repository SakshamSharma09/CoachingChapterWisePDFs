from lib8 import *
q1 = mcqgroup([
 m("The number of non-square natural numbers between 9² and 10² is:", "18", ["17","19","20"], "Between n² and (n+1)² there are 2n non-square numbers: 2 × 9 = 18."),
 m("Which of the following is a perfect cube?", "1728", ["1800","2025","3000"], "1728 = 12³ (2⁶ × 3³)."),
 m("The value of 2<sup>−4</sup> is:", "1/16", ["−16","−8","1/8"], "2⁻⁴ = 1/2⁴ = 1/16."),
 m("(3<sup>5</sup>)<sup>2</sup> ÷ 3<sup>7</sup> equals:", "27", ["3","9","81"], "3¹⁰ ÷ 3⁷ = 3³ = 27."),
 m("The standard form of 6,50,000 is:", "6.5 × 10<sup>5</sup>", ["65 × 10<sup>4</sup>","6.5 × 10<sup>4</sup>","0.65 × 10<sup>5</sup>"], "650000 = 6.5 × 100000 = 6.5 × 10⁵."),
 m("449 written in Roman numerals is:", "CDXLIX", ["CCCXLIX","CDLIX","CDXLVIIII"], "400 = CD, 40 = XL, 9 = IX ⇒ CDXLIX."),
 m("The base-3 number 212 equals which decimal number?", "23", ["21","22","25"], "2×9 + 1×3 + 2×1 = 23."),
 m("A quadrilateral with exactly one pair of parallel sides is a:", "Trapezium", ["Parallelogram","Rhombus","Rectangle"], "By definition, a trapezium has exactly one pair of parallel sides."),
 m("In an isosceles trapezium ABCD with AB ∥ DC, if ∠A = 70°, then ∠D is:", "110°", ["70°","90°","100°"], "∠A + ∠D = 180° (co-interior angles) ⇒ ∠D = 110°."),
 m("Kaprekar’s constant for 4-digit numbers is:", "6174", ["495","1089","9999"], "The routine on 4-digit numbers (not all digits same) always ends at 6174."),
 m("(a + b)² − (a − b)² equals:", "4ab", ["2ab","2a² + 2b²","0"], "(a² + 2ab + b²) − (a² − 2ab + b²) = 4ab."),
 m("If 4 pencils cost ₹ 30, the cost of 10 pencils is:", "₹ 75", ["₹ 70","₹ 80","₹ 120"], "4 : 30 = 10 : x ⇒ x = 300/4 = 75.")])
b = [
 sa("Find the smallest number by which 72 must be multiplied to get a perfect cube.", 2, "72 = 2³ × 3² (1 mark)<br>3² needs one more 3 to make 3³ ⇒ multiply by 3 (product 216 = 6³) (1 mark)"),
 sa("Evaluate: (2<sup>−1</sup> + 3<sup>−1</sup>)<sup>−1</sup>", 2, "2⁻¹ + 3⁻¹ = 1/2 + 1/3 = 5/6 (1 mark)<br>(5/6)⁻¹ = 6/5 (1 mark)"),
 sa("Convert (110101)₂ into a decimal number.", 2, "1×32 + 1×16 + 0×8 + 1×4 + 0×2 + 1×1 (1 mark)<br>= 53 (1 mark)"),
 OR(sa("Without actual division, check whether 234567 is divisible by 9.", 2, "Digit sum = 2+3+4+5+6+7 = 27 (1 mark)<br>27 is divisible by 9 ⇒ 234567 is divisible by 9 (1 mark)"),
    sa("Find the digit * so that 3*76 is divisible by 11.", 2, "(Sum of digits at odd places) − (sum at even places) = (3+7) − (*+6) = 4 − * (1 mark)<br>This must be 0 ⇒ * = 4 (3476 = 11 × 316) (1 mark)")),
 sa("The diagonals of a rectangle are (3x + 5) cm and (5x − 7) cm. Find x and the length of each diagonal.", 2, "Diagonals of a rectangle are equal: 3x + 5 = 5x − 7 ⇒ x = 6 (1 mark)<br>Each diagonal = 3(6) + 5 = 23 cm (1 mark)"),
 sa("Divide ₹ 540 between Meena and Neha in the ratio 4 : 5.", 2, "Total parts = 9; 1 part = ₹ 60 (1 mark)<br>Meena = ₹ 240, Neha = ₹ 300 (1 mark)")]
c = [
 sa("Convert 69 into (i) base 5 and (ii) base 3.", 3, "(i) 69 = 2×25 + 3×5 + 4 ⇒ (234)₅ (1½ marks)<br>(ii) 69 = 2×27 + 1×9 + 2×3 + 0 ⇒ (2120)₃ (1½ marks)"),
 OR(sa("In a rhombus ABCD, ∠A = 70°. Find ∠B, ∠C and ∠D. State the property used.", 3, "Adjacent angles are supplementary ⇒ ∠B = 110° (1 mark)<br>Opposite angles are equal ⇒ ∠C = 70°, ∠D = 110° (1 mark)<br>Property: opposite angles of a parallelogram (rhombus) are equal and adjacent angles are supplementary (1 mark)"),
    sa("In trapezium PQRS, PQ ∥ SR, ∠P = 75° and ∠R = 110°. Find ∠S and ∠Q.", 3, "Co-interior angles between parallel sides PQ and SR: ∠P + ∠S = 180° ⇒ ∠S = 105° (1½ marks)<br>∠Q + ∠R = 180° ⇒ ∠Q = 70° (1½ marks)")),
 sa("Expand and simplify:<br>(i) (2a + 3)(a² − 4a + 5) &nbsp;&nbsp; (ii) (3x − 2y)(x + 5y)", 3, "(i) 2a³ − 8a² + 10a + 3a² − 12a + 15 = 2a³ − 5a² − 2a + 15 (2 marks)<br>(ii) 3x² + 15xy − 2xy − 10y² = 3x² + 13xy − 10y² (1 mark)")]
d = [
 OR(sa("(i) Find the smallest number by which 1176 must be multiplied so that the product is a perfect square. Find the square root of the product.<br>(ii) The area of a square field is 2704 m². Find the length of its side.", 5, "(i) 1176 = 2³ × 3 × 7² (1 mark); unpaired factors 2 and 3 ⇒ multiply by 2 × 3 = 6 (1 mark)<br>Product 7056 = 2⁴ × 3² × 7², √7056 = 4 × 3 × 7 = 84 (1 mark)<br>(ii) 2704 = 2⁴ × 13² ⇒ side = 4 × 13 = 52 m (2 marks)"),
    sa("(i) Find the smallest number by which 2000 must be divided so that the quotient is a perfect cube. Find the cube root of the quotient.<br>(ii) The volume of a cube is 4096 cm³. Find the length of its edge.", 5, "(i) 2000 = 2⁴ × 5³ (1 mark); divide by 2 (1 mark); quotient 1000, cube root 10 (1 mark)<br>(ii) 4096 = 2¹² ⇒ edge = 2⁴ = 16 cm (2 marks)")),
 OR(sa("If 17² = 289, find: (i) 1.7² (ii) 0.17² (iii) 170² (iv) 1700² (v) 0.017²", 5, "(i) 2.89 (ii) 0.0289 (iii) 28900 (iv) 2890000 (v) 0.000289 (1 mark each)"),
    sa("Simplify and write in exponential form: (i) 5⁻² × 5⁷ (ii) 2⁻³ ÷ 2⁻⁵ (iii) (9⁻³)² (iv) (3/4)⁻² (v) p⁶q² × (pq)⁻²", 5, "(i) 5⁵ (ii) 2² (iii) 9⁻⁶ (iv) (4/3)² = 16/9 (v) p⁴ (1 mark each)")),
 sa("(i) Apply Kaprekar’s routine to the 3-digit number 352 and show every step until it reaches 495.<br>(ii) What happens if the routine is applied to 111? Why?<br>(iii) Apply the routine to 2025 (4-digit) and state the number of steps taken to reach 6174.", 5,
    "(i) 532 − 235 = 297; 972 − 279 = 693; 963 − 369 = 594; 954 − 459 = 495 (2 marks: 4 steps, each correct = ½ mark)<br>(ii) 111 − 111 = 0: all digits are equal, so the routine collapses to 0 and never reaches 495 (1 mark)<br>(iii) 5220 − 0225 = 4995; 9954 − 4599 = 5355; 5553 − 3555 = 1998; 9981 − 1899 = 8082; 8820 − 0288 = 8532; 8532 − 2358 = 6174 ⇒ 6 steps (2 marks)")]
rect = quad([(20,30),(200,30),(200,110),(20,110)], ['A','B','C','D'], F.line(20,30,200,110,'#555',1,'4,3')+F.line(200,30,20,110,'#555',1,'4,3')+F.text(112,64,'O','start'), 230, 150)
e = [
 case("A rectangular herb garden ABCD has a diagonal path AC = 26 cm on the school’s model plan. The diagonals AC and BD meet at O, and the side AB = 10 cm.",
      [sub("Find the length of OB.", 1, "Diagonals of a rectangle are equal and bisect each other: OB = ½ × 26 = 13 cm"),
       sub("Find the length of the side BC.", 1, "BC = √(26² − 10²) = √576 = 24 cm"),
       OR(sub("Find the perimeter and the area of the rectangular garden.", 2, "Perimeter = 2(10 + 24) = 68 cm (1 mark); area = 10 × 24 = 240 cm² (1 mark)"),
          sub("A string is laid along both diagonals at ₹ 45 per cm on the model. Find the total cost.", 2, "Length = 26 + 26 = 52 cm (1 mark); cost = 52 × 45 = ₹ 2340 (1 mark)"))], fig=rect),
 case("In a laboratory a culture starts with 5 × 10⁴ cells, and the number of cells becomes 10 times larger every day.",
      [sub("How many cells will there be after 3 days? Give your answer in standard form.", 1, "5 × 10⁴ × 10³ = 5 × 10⁷"),
       sub("Write the number of cells after 3 days in usual form.", 1, "5 × 10⁷ = 5,00,00,000 (five crore)"),
       OR(sub("Find the ratio of the number of cells after 2 days to that after 5 days.", 2, "After 2 days: 5×10⁶; after 5 days: 5×10⁹ (1 mark); ratio = 10⁶ : 10⁹ = 1 : 1000 (1 mark)"),
          sub("After how many days will the culture first exceed 5 × 10⁹ cells?", 2, "Cells after n days = 5 × 10⁴⁺ⁿ; equals 5 × 10⁹ at n = 5 (1 mark), so it first exceeds this on day 6 (1 mark)"))]),
 case("A school canteen prepares a sherbet by mixing lemon juice, sugar and water in the ratio 1 : 2 : 7 to make 5 litres of sherbet in each batch.",
      [sub("How many litres of sugar are used in one batch?", 1, "Parts = 10; sugar = 2/10 × 5 = 1 litre"),
       sub("Write the ratio of lemon juice to water in simplest form.", 1, "1 : 7"),
       OR(sub("How much water is needed along with 2.4 litres of lemon juice (same ratio)?", 2, "1 part = 2.4 L (1 mark); water = 7 × 2.4 = 16.8 L (1 mark)"),
          sub("Lemon juice costs ₹ 60 per litre and sugar ₹ 40 per litre. Find the cost of the ingredients for one 5-litre batch (water is free).", 2, "Juice = 0.5 L → ₹ 30; sugar = 1 L → ₹ 40 (1 mark); total ₹ 70 (1 mark)"))])]
META = meta(2); SECTIONS = secs(q1, b, c, d, e)
