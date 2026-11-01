from lib8 import *
S1 = "<sup>2</sup>"
q1 = mcqgroup([
 m("The smallest 4-digit perfect square number is:", "1024", ["1000","1089","1156"], "32² = 1024, and 31² = 961 has only 3 digits."),
 m("The cube root of 17576 is:", "26", ["24","28","36"], "17576 = 2³ × 13³ ⇒ ∛17576 = 2 × 13 = 26."),
 m("The standard form of 0.00045 is:", "4.5 × 10<sup>−4</sup>", ["4.5 × 10<sup>−3</sup>","45 × 10<sup>−5</sup>","4.5 × 10<sup>4</sup>"], "Move the decimal 4 places to the right: 4.5 × 10⁻⁴ (45 × 10⁻⁵ is not in standard form)."),
 m("The Roman numeral XCIV represents:", "94", ["86","106","114"], "XC = 90 and IV = 4, so XCIV = 94."),
 m("The binary number 1011 is equal to which decimal number?", "11", ["9","10","13"], "1×8 + 0×4 + 1×2 + 1×1 = 11."),
 m("Which quadrilateral always has equal diagonals that bisect each other, but the diagonals need not be perpendicular?", "Rectangle", ["Rhombus","Kite","Parallelogram"], "Rectangle: diagonals equal and bisect each other; they are perpendicular only if it is a square."),
 m("A number is divisible by 18 if it is divisible by:", "2 and 9", ["3 and 6","4 and 9","2 and 6"], "18 = 2 × 9 with 2 and 9 co-prime. (3 and 6 are not co-prime, so they do not guarantee divisibility by 18.)"),
 m("The value of 104² − 96² is:", "1600", ["800","1200","16"], "(104 + 96)(104 − 96) = 200 × 8 = 1600."),
 m("In the expansion of (7x − 3)², the middle term is:", "−42x", ["−21x","+42x","−9x"], "(7x − 3)² = 49x² − 2(7x)(3) + 9 = 49x² − 42x + 9."),
 m("Which of the following pairs of ratios forms a proportion?", "15 : 25 and 9 : 15", ["4 : 6 and 9 : 12","3 : 5 and 5 : 3","2 : 7 and 7 : 2"], "15/25 = 3/5 and 9/15 = 3/5, so 15 : 25 :: 9 : 15."),
 m("The ratio of 45 minutes to 1½ hours in simplest form is:", "1 : 2", ["3 : 2","1 : 3","2 : 3"], "1½ h = 90 min, so 45 : 90 = 1 : 2."),
 m("Sum of any two consecutive odd numbers is always divisible by:", "4", ["3","5","6"], "(2n−1)+(2n+1) = 4n, divisible by 4.")])
b = [
 sa("Find the square root of 2916 by prime factorisation.", 2, "2916 = 2² × 3⁶ (1 mark)<br>√2916 = 2 × 3³ = 54 (1 mark)"),
 sa("Write 0.000000837 in standard form.", 2, "Move the decimal 7 places right: 8.37 (1 mark)<br>0.000000837 = 8.37 × 10⁻⁷ (1 mark)"),
 sa("Write 2024 in Roman numerals.", 2, "2000 = MM, 20 = XX, 4 = IV (1 mark)<br>2024 = MMXXIV (1 mark)"),
 OR(sa("Convert the decimal number 45 into base 2.", 2, "45 ÷ 2 → remainders 1,0,1,1,0,1 (1 mark)<br>Reading upwards: 45 = (101101)₂ (1 mark)"),
    sa("Find the decimal value of (2314) in base 5.", 2, "2×5³ + 3×5² + 1×5 + 4 = 250 + 75 + 5 + 4 (1 mark)<br>= 334 (1 mark)")),
 sa("Two adjacent angles of a parallelogram are in the ratio 2 : 3. Find all the angles of the parallelogram.", 2, "Adjacent angles are supplementary: 2x + 3x = 180° ⇒ x = 36° (1 mark)<br>Angles: 72°, 108°, 72°, 108° (1 mark)"),
 sa("Find x if x : 12 :: 15 : 36.", 2, "Product of extremes = product of means: 36x = 12 × 15 (1 mark)<br>x = 180/36 = 5 (1 mark)")]
c = [
 sa("Find the sum without converting to Hindu-Arabic numerals:<br>(i) XLVII + LXIII &nbsp; (ii) CCXLIII + DCLVII", 3, "(i) XLVII + LXIII → (XL + VII) + (LX + III): XL + LX = C and VII + III = X, so the sum is CX [47 + 63 = 110] (2 marks)<br>(ii) CCXLIII + DCLVII: 243 + 657 = 900 = CM (1 mark)"),
 OR(sa("The diagonals of a rhombus are 16 cm and 30 cm. Find the length of its side and its perimeter.", 3, "Diagonals bisect at right angles: half-diagonals 8 cm and 15 cm (1 mark)<br>Side = √(8² + 15²) = √289 = 17 cm (1 mark)<br>Perimeter = 4 × 17 = 68 cm (1 mark)"),
    sa("In parallelogram PQRS, ∠P = (3x + 10)° and ∠Q = (2x − 10)°. Find x and all the angles.", 3, "Adjacent angles are supplementary: 3x + 10 + 2x − 10 = 180 ⇒ x = 36 (1 mark)<br>∠P = 118°, ∠Q = 62° (1 mark)<br>∠R = 118°, ∠S = 62° (opposite angles equal) (1 mark)")),
 sa("Expand and simplify:<br>(i) (x + 4)(x² − 2x + 3) &nbsp;&nbsp; (ii) (2m − 1)(m + 3)", 3, "(i) x³ − 2x² + 3x + 4x² − 8x + 12 = x³ + 2x² − 5x + 12 (2 marks)<br>(ii) 2m² + 6m − m − 3 = 2m² + 5m − 3 (1 mark)")]
d = [
 OR(sa("(i) Find the smallest number by which 5292 must be multiplied so that the product is a perfect square. Also find the square root of the product.<br>(ii) Find the side of a square whose area is 1296 m².", 5, "(i) 5292 = 2² × 3³ × 7² (1 mark); 3 is unpaired, so multiply by 3 (1 mark)<br>Product = 15876 = 2² × 3⁴ × 7², √ = 2 × 9 × 7 = 126 (1 mark)<br>(ii) side = √1296 = 36 m (2 marks: 2² × 2² × 3⁴ → 2·2·9 = 36)"),
    sa("(i) Find the smallest number by which 3087 must be divided so that the quotient is a perfect cube. Also find the cube root of the quotient.<br>(ii) The volume of a cube is 5832 cm³. Find the length of its edge.", 5, "(i) 3087 = 3² × 7³ (1 mark); divide by 3² = 9 (1 mark)<br>Quotient 343 = 7³, cube root = 7 (1 mark)<br>(ii) 5832 = 2³ × 3⁶ (1 mark); edge = 2 × 3² = 18 cm (1 mark)")),
 OR(sa("If 13² = 169, find the values of: (i) 1.3² (ii) 0.13² (iii) 130² (iv) 1300² (v) 0.013²", 5, "(i) 1.69 (ii) 0.0169 (iii) 16900 (iv) 1690000 (v) 0.000169 (1 mark each; place the decimal using 2n places)"),
    sa("Simplify and write in exponential form: (i) 7⁻³ × 7⁻² (ii) 3⁹ ÷ 3⁵ (iii) (5⁻²)⁻³ (iv) 2⁷ ÷ 2⁻³ (v) a⁴b⁶ × (ab)³", 5, "(i) 7⁻⁵ (ii) 3⁴ (iii) 5⁶ (iv) 2¹⁰ (v) a⁷b⁹ (1 mark each)")),
 sa("(i) Find the digit(s) that can replace * in 52*8 so that the number is divisible by 3.<br>(ii) Is 3141592 divisible by 11? Show your work.<br>(iii) Find the smallest 3-digit number divisible by 4 and 9 both.<br>(iv) Replace the blank to make 7_6 divisible by 4 (smallest digit).<br>(v) A number is divisible by 6. Name its two divisibility conditions.", 5,
    "(i) 5+2+*+8 = 15 + *, so * = 0, 3, 6, 9 (1 mark)<br>(ii) (3+4+5+2) − (1+1+9) = 14 − 11 = 3, not 0 or a multiple of 11 ⇒ NOT divisible (1 mark)<br>(iii) LCM(4,9) = 36; smallest 3-digit multiple = 108 (1 mark)<br>(iv) last two digits _6 must be divisible by 4: 16 → digit 1 (1 mark)<br>(v) divisible by 2 and by 3 (1 mark)")]
kite = quad([(110,24),(55,74),(110,154),(165,74)], ['A','B','C','D'], F.line(110,24,110,154,'#555',1,'4,3')+F.line(55,74,165,74,'#555',1,'4,3')+F.text(122,70,'O','start'), 220, 180)
e = [
 case("Riya and Aarav are making a kite for the school exhibition. The kite ABCD has two pairs of adjacent equal sides: AB = AD = 6 cm and CB = CD = 9 cm. Its diagonals AC and BD meet at O (see figure).",
      [sub("What is the length of the side CD?", 1, "CD = CB = 9 cm"),
       sub("Name the pair of adjacent angles of the kite that are equal, and state the reason.", 1, "∠B = ∠D (angles between the unequal sides; ΔABC ≅ ΔADC by SSS) — accept ∠ABC = ∠ADC"),
       OR(sub("Show that the diagonal AC bisects ∠A and ∠C.", 2, "In ΔABC and ΔADC: AB = AD, CB = CD, AC common ⇒ ΔABC ≅ ΔADC (SSS) (1 mark)<br>So ∠BAC = ∠DAC and ∠BCA = ∠DCA (CPCT) ⇒ AC bisects ∠A and ∠C (1 mark)"),
          sub("If ∠AOB = x°, find x and give a reason.", 2, "In a kite the diagonals intersect at right angles (1 mark) ⇒ x = 90° (1 mark)"))], fig=kite),
 case("Aditi and Rahul prepare for a Mental Maths Quiz. Their teacher shows the identities: (A) (a + b)² = a² + 2ab + b²; (B) (a − b)² = a² − 2ab + b²; (C) a² − b² = (a + b)(a − b).",
      [sub("Find 53² using identity (A).", 1, "(50 + 3)² = 2500 + 300 + 9 = 2809"),
       sub("Find 1.02 × 0.98 using identity (C).", 1, "(1 + 0.02)(1 − 0.02) = 1 − 0.0004 = 0.9996"),
       OR(sub("Prove that (x + y)² + (x − y)² = 2(x² + y²).", 2, "LHS = x² + 2xy + y² + x² − 2xy + y² (1 mark) = 2x² + 2y² = 2(x² + y²) = RHS (1 mark)"),
          sub("Find 1003² − 997² using a suitable identity.", 2, "(1003 + 997)(1003 − 997) (1 mark) = 2000 × 6 = 12000 (1 mark)"))]),
 case("The school garden club prepares a fertiliser mixture of urea, potash and compost in the ratio 2 : 3 : 5. The total weight of the mixture is 40 kg.",
      [sub("How many kilograms of compost are in the mixture?", 1, "Total parts = 10; compost = 5/10 × 40 = 20 kg"),
       sub("Write the ratio of urea to compost in simplest form.", 1, "2 : 5"),
       OR(sub("The club uses 7.5 kg of potash in another batch of the same mixture. What is the total weight of that batch?", 2, "3 parts = 7.5 kg ⇒ 1 part = 2.5 kg (1 mark); total = 10 × 2.5 = 25 kg (1 mark)"),
          sub("Find the missing numbers so that these ratios are proportional to 2 : 5:  14 : __ and __ : 45", 2, "14 : 35 (1 mark) and 18 : 45 (1 mark)"))])]
META = meta(1); SECTIONS = secs(q1, b, c, d, e)
