import random
from c7maths.h import *
R = random.Random(702)
A = []; B = []; C = []; D = []
# A: evaluate (BODMAS) 14
ex = [("8 + 6 × 3", 26), ("(8 + 6) × 3", 42), ("40 − 12 ÷ 4", 37), ("(40 − 12) ÷ 4", 7), ("5 × 4 + 6 × 2", 32), ("100 − 4 × (6 + 9)", 40),
      ("48 ÷ 6 × 2", 16), ("48 ÷ (6 × 2)", 4), ("3 + 4 × 5 − 6", 17), ("(3 + 4) × (5 − 2)", 21), ("2 × [18 − (4 + 5)]", 18), ("7 + 56 ÷ 8 − 3", 11),
      ("9 × 9 − 9 ÷ 9", 80), ("30 − 5 × 2 + 4", 24)]
for e, v in ex:
    A.append(M4(f"The value of {e} is:", str(v), [str(v + 2), str(v - 3), str(v * 2 if v < 50 else v // 2)], "follow brackets, then ×/÷ left to right, then +/−"))
# A: concepts 14
A += [
 M4("In an expression, the operation done first is the one inside:", "brackets", ["addition", "subtraction", "the last number"], "brackets are evaluated first"),
 M4("Which of these is NOT an arithmetic expression?", "8 + × 3", ["8 + 3", "(8 + 3) × 2", "15 ÷ 3"], "an operation sign has no number after it"),
 M4("The expression for ‘5 more than the product of 4 and 6’ is:", "4 × 6 + 5", ["(4 + 6) × 5", "4 + 6 + 5", "5 × (4 + 6)"], "product first, then add 5"),
 M4("The expression for ‘the sum of 7 and 9, multiplied by 3’ is:", "(7 + 9) × 3", ["7 + 9 × 3", "7 × 9 + 3", "7 × 3 + 9"], "brackets show the sum is done first"),
 M4("23 × 99 can be calculated quickly as:", "23 × 100 − 23", ["23 × 100 + 23", "23 × 90 + 9", "23 + 99"], "99 = 100 − 1"),
 M4("The distributive property says a × (b + c) =", "a × b + a × c", ["a + b × c", "a × b × c", "(a + b) × c"], "multiplication distributes over addition"),
 M4("12 × 25 is easily found as:", "12 × 100 ÷ 4", ["12 × 25 + 4", "12 + 100 ÷ 4", "(12 + 25) × 4"], "25 = 100 ÷ 4"),
 M4("Which expression equals 24?", "(2 + 4) × 4", ["2 + 4 × 4", "2 × 4 + 4", "2 + 4 + 4"], "6 × 4 = 24"),
 M4("17 + 25 + 3 is easily found by adding:", "17 + 3 first", ["25 + 3 first", "all three digit by digit", "17 + 25 first"], "17 + 3 = 20 makes a tens number"),
 M4("The value of 50 − (20 − 5) is:", "35", ["25", "65", "30"], "bracket gives 15, 50 − 15"),
 M4("Which pair of expressions has equal value?", "6 × (5 + 2) and 6 × 5 + 6 × 2", ["6 × 5 + 2 and 6 × 7", "(6 + 5) × 2 and 6 × 5", "6 + 5 × 2 and 11 × 2"], "distributive property"),
 M4("A pen costs ₹12 and a notebook ₹30. The cost of 3 pens and 2 notebooks is:", "₹96", ["₹126", "₹66", "₹106"], "3 × 12 + 2 × 30 = 36 + 60"),
 M4("‘Divide 90 by the difference of 11 and 5’ is written as:", "90 ÷ (11 − 5)", ["90 ÷ 11 − 5", "(90 ÷ 11) − 5", "90 − 11 ÷ 5"], "bracket for difference"),
 M4("Without evaluating, which is greater: 15 × 12 or 15 × 11 + 12?", "15 × 12", ["15 × 11 + 12", "they are equal", "cannot say"], "15 × 12 = 15 × 11 + 15 and 15 > 12"),
]
# A: simple numeric word items 12
for a, b, c in [(6, 7, 8), (9, 4, 5), (12, 3, 7), (15, 5, 2), (20, 4, 6), (18, 3, 9)]:
    v = a * b + c
    A.append(M4(f"The value of {a} × {b} + {c} is:", str(v), [str(a * (b + c)), str(v + a), str(v - c * 2)], "multiply first, then add"))
for a, b, c in [(4, 6, 3), (7, 8, 2), (5, 9, 6), (3, 12, 4), (6, 10, 5), (8, 7, 9)]:
    v = (a + b) * c
    A.append(M4(f"Evaluate ({a} + {b}) × {c}.", str(v), [str(a + b * c), str(v + c), str(v - a), str(v + 1)], "brackets first"))
A = A[:40]
B = [
 Q("What is an arithmetic expression? Give an example.", "A combination of numbers and operation signs that has a value (1); e.g. 5 × 4 + 3 (1).", "1+1"),
 Q("Evaluate: 18 − 6 ÷ 3 + 4 × 2.", "18 − 2 + 8 = 24 (2).", "2"),
 Q("Write the expression: ‘twice the sum of 9 and 14, decreased by 5’. Evaluate it.", "2 × (9 + 14) − 5 = 46 − 5 = 41 (2).", "2"),
 Q("State the order in which operations are done in an expression.", "Brackets, then multiplication and division from left, then addition and subtraction from left (2).", "2"),
 Q("Use the distributive property to find 17 × 102.", "17 × (100 + 2) = 1700 + 34 = 1734 (2).", "2"),
 Q("Find 25 × 48 quickly.", "25 × 4 × 12 = 100 × 12 = 1,200 (2).", "2"),
 Q("Insert brackets so that 8 + 4 × 3 − 2 = 34.", "(8 + 4) × 3 − 2 = 34 (2).", "2"),
 Q("Is 30 − (12 − 4) the same as (30 − 12) − 4? Check.", "30 − 8 = 22 and 18 − 4 = 14, so they are different (2).", "2"),
 Q("Find the value of 100 ÷ (4 × 5) and 100 ÷ 4 × 5. Are they equal?", "5 and 125; not equal (2).", "1+1"),
 Q("Rewrite 36 + 24 as a multiple of a common factor.", "12 × (3 + 2) = 60 (2).", "2"),
 Q("A book costs ₹45 and a pen ₹15. Write an expression for the cost of 4 books and 5 pens and find it.", "4 × 45 + 5 × 15 = 180 + 75 = ₹255 (2).", "2"),
 Q("Compare without evaluating: 9 × 14 and 9 × 13 + 10.", "9 × 14 = 9 × 13 + 9, so 9 × 13 + 10 is greater (2).", "2"),
 Q("Find the missing number: 7 × __ + 3 = 59.", "7 × 8 + 3 = 59, so 8 (2).", "2"),
 Q("Evaluate 6 + 6 ÷ 6 − 6 × 6.", "6 + 1 − 36 = −29 (2).", "2"),
 Q("What does the bracket do in 5 × (3 + 4)?", "It makes 3 + 4 be done first, so the value is 35 (2).", "2"),
 Q("Write ‘the difference of 50 and 18, divided by 8’ as an expression and evaluate.", "(50 − 18) ÷ 8 = 4 (2).", "2"),
]
C = [
 Q("Evaluate: 72 ÷ 8 + 5 × (9 − 4) − 3.", "9 + 25 − 3 (1.5); = 31 (1.5).", "1½+1½"),
 Q("Evaluate 2 × [30 − (6 + 4 × 3)].", "6 + 12 = 18 (1); 30 − 18 = 12 (1); 24 (1).", "1+1+1"),
 Q("Use the distributive property: 35 × 98 + 35 × 2.", "35 × (98 + 2) (1); = 35 × 100 = 3,500 (2).", "1+2"),
 Q("Find 64 × 25 easily and explain.", "64 × 100 ÷ 4 (1.5); = 1,600 (1.5).", "1½+1½"),
 Q("A shopkeeper sells 12 pens at ₹8 and 15 pencils at ₹4. Write an expression for the total and evaluate.", "12 × 8 + 15 × 4 (1.5); = 96 + 60 = ₹156 (1.5).", "1½+1½"),
 Q("Insert one pair of brackets in 4 + 5 × 6 − 2 to make the value (a) 52 (b) 24.", "(a) (4 + 5) × 6 − 2 = 52 (1.5); (b) 4 + 5 × (6 − 2) = 24 (1.5).", "1½+1½"),
 Q("Is 9 × (12 − 7) equal to 9 × 12 − 9 × 7? Show.", "45 and 108 − 63 = 45 (2); equal by distributive property (1).", "2+1"),
 Q("Write an expression for: ‘three times the sum of 14 and 6, less the quotient of 48 and 6’. Evaluate.", "3 × (14 + 6) − 48 ÷ 6 (1.5); = 60 − 8 = 52 (1.5).", "1½+1½"),
 Q("Compare 13 × 15 and 14 × 14 using expressions.", "13 × 15 = 195; 14 × 14 = 196 (2); 196 is greater (1).", "2+1"),
 Q("The cost of 4 kg of rice at ₹52 per kg and 3 kg of dal at ₹90 per kg is paid with a ₹500 note. How much change?", "500 − (4 × 52 + 3 × 90) (1.5); = 500 − 478 = ₹22 (1.5).", "1½+1½"),
 Q("Why is 8 + 4 ÷ 2 equal to 10 and not 6?", "Division is done before addition (1.5); 4 ÷ 2 = 2, then 8 + 2 = 10 (1.5).", "1½+1½"),
 Q("Evaluate 15 − 3 × 4 + 18 ÷ 6 and also (15 − 3) × 4 + 18 ÷ 6.", "15 − 12 + 3 = 6 (1.5); 12 × 4 + 3 = 51 (1.5).", "1½+1½"),
 Q("Find the value of 999 × 7 using a short method.", "(1000 − 1) × 7 = 7,000 − 7 (1.5); = 6,993 (1.5).", "1½+1½"),
 Q("Fill in with +, −, ×, ÷ to make it true: 12 __ 3 __ 2 = 6.", "12 ÷ 3 + 2 = 6 (3).", "3"),
 Q("Simplify using brackets: 50 − 10 + 5. Then simplify 50 − (10 + 5). Explain the difference.", "45 and 35 (2); a bracket after a minus sign changes the order (1).", "2+1"),
 Q("A rectangle has length 24 m and width 15 m. Write an expression for its perimeter and evaluate.", "2 × (24 + 15) (1.5); = 78 m (1.5).", "1½+1½"),
 Q("Find 17 × 5 + 17 × 15 + 17 × 80 quickly.", "17 × (5 + 15 + 80) = 17 × 100 = 1,700 (3).", "3"),
 Q("Write two different expressions that equal 36 using 4 and 9.", "4 × 9 = 36 (1.5); 9 × 4 + 0 or (9 × 8) ÷ 2 = 36 (1.5).", "1½+1½"),
 Q("Raju says 12 − 4 − 2 = 10. Is he right? Explain.", "Left to right: 8 − 2 = 6 (2); he subtracted 4 − 2 first, which is wrong (1).", "2+1"),
 Q("Evaluate 100 − 2 × (15 + 5) + 6.", "100 − 40 + 6 (1.5); = 66 (1.5).", "1½+1½"),
 Q("Find the number: if 3 × (a number + 5) = 36.", "number + 5 = 12 (1.5); number = 7 (1.5).", "1½+1½"),
 Q("Estimate 49 × 51 using the expression (50 − 1)(50 + 1) pattern or by rounding.", "≈ 50 × 50 = 2,500 (1.5); exact 2,499 (1.5).", "1½+1½"),
 Q("Write the expression for the perimeter of a square of side 13 cm and the area. Evaluate both.", "4 × 13 = 52 cm (1.5); 13 × 13 = 169 cm² (1.5).", "1½+1½"),
Q("Evaluate 45 − 3 × (6 + 2) + 10 ÷ 5.", "45 − 24 + 2 (1.5); = 23 (1.5).", "1½+1½"),
]
D = [
 Q("(i) Evaluate 5 × (18 − 6) ÷ 4 + 7. (ii) Evaluate 5 × 18 − 6 ÷ 4 + 7. (iii) Why are the answers different?", "(i) 5 × 12 ÷ 4 + 7 = 22 (2). (ii) 90 − 1.5 + 7 = 95.5 (2). (iii) Brackets change the order (1).", "2+2+1"),
 Q("<b>Case study:</b> A canteen sells tea at ₹12 and samosa at ₹15. Meena buys 4 teas and 3 samosas; Rohan buys 5 teas and 2 samosas. (i) Write expressions. (ii) Evaluate both. (iii) Who pays more and by how much? (iv) Write the total cost of both.", "(i) 4 × 12 + 3 × 15 and 5 × 12 + 2 × 15 (1). (ii) ₹93 and ₹90 (2). (iii) Meena by ₹3 (1). (iv) 93 + 90 = ₹183 (1).", "1+2+1+1"),
 Q("(i) State the distributive property. (ii) Use it to find 47 × 103. (iii) Use it to find 56 × 99. (iv) Verify 7 × (8 + 5) = 7 × 8 + 7 × 5.", "(i) a × (b + c) = a × b + a × c (1). (ii) 4,841 (1.5). (iii) 5,544 (1.5). (iv) 91 = 56 + 35 (1).", "1+1½+1½+1"),
 Q("(i) Find the value of 6 + 9 ÷ 3 × 2. (ii) Insert brackets to make it 10. (iii) Insert brackets to make it 7.5.", "(i) 6 + 3 × 2 = 12 (1). (ii) (6 + 9) ÷ 3 × 2 = 10 (2). (iii) 6 + 9 ÷ (3 × 2) = 7.5 (2).", "1+2+2"),
 Q("(i) Write expressions for these. (a) 7 less than the product of 8 and 9. (b) The quotient of 96 and the sum of 5 and 7. (ii) Evaluate each. (iii) Which is bigger?", "(i) 8 × 9 − 7; 96 ÷ (5 + 7) (2). (ii) 65 and 8 (2). (iii) The first (1).", "2+2+1"),
 Q("<b>Case study:</b> A school buys 25 chairs at ₹640 each and 12 tables at ₹1,250 each. (i) Write an expression. (ii) Evaluate it. (iii) A discount of ₹2,500 is given; find the amount paid. (iv) Write the final expression.", "(i) 25 × 640 + 12 × 1,250 (1). (ii) 16,000 + 15,000 = 31,000 (2). (iii) ₹28,500 (1). (iv) 25 × 640 + 12 × 1,250 − 2,500 (1).", "1+2+1+1"),
 Q("(i) Find 25 × 36 using 25 = 100 ÷ 4. (ii) Find 125 × 48. (iii) Find 15 × 16 using 15 × 16 = 15 × 2 × 8.", "(i) 900 (1.5). (ii) 6,000 (2). (iii) 240 (1.5).", "1½+2+1½"),
 Q("(i) Show that (a) 13 × 17 and 15 × 15 − 4 are equal. (ii) Find another pair of numbers near 20 that follows the pattern. (iii) State the pattern.", "(i) 221 and 225 − 4 = 221 (2). (ii) 19 × 21 = 399 = 20 × 20 − 1 (2). (iii) (n − k)(n + k) = n² − k² (1).", "2+2+1"),
 Q("(i) Evaluate 8 + 8 × 8 − 8 ÷ 8. (ii) Evaluate (8 + 8) × (8 − 8 ÷ 8). (iii) Which is larger and by how much?", "(i) 8 + 64 − 1 = 71 (1.5). (ii) 16 × 7 = 112 (1.5). (iii) (ii), by 41 (2).", "1½+1½+2"),
 Q("(i) A train has 12 coaches with 72 seats each. 4 coaches are removed. Write an expression for the remaining seats. (ii) Evaluate. (iii) 480 passengers want seats; how many cannot sit?", "(i) (12 − 4) × 72 (1). (ii) 576 (2). (iii) none; 96 seats left (2).", "1+2+2"),
 Q("<b>Case study:</b> Sita says 36 ÷ 4 × 3 = 3 and Gita says it is 27. (i) Who is right? (ii) Show the steps. (iii) What rule decides? (iv) Write 36 ÷ (4 × 3).", "(i) Gita (1). (ii) 9 × 3 = 27 (1). (iii) Left to right for × and ÷ (1). (iv) 3 (2).", "1+1+1+2"),
 Q("(i) Make 100 using four 9s and operations. (ii) Make 24 using 3, 3, 8, 8 with operations. (iii) Explain why brackets are needed.", "(i) 99 + 9 ÷ 9 = 100 (2). (ii) 8 ÷ (3 − 8 ÷ 3) = 24 (2). (iii) They set the order (1).", "2+2+1"),
 Q("(i) Find the perimeter of a rectangle 18 m by 11 m. (ii) Find its area. (iii) Write both as expressions. (iv) Find the cost of fencing at ₹35 per metre.", "(i) 58 m (1). (ii) 198 m² (1). (iii) 2 × (18 + 11), 18 × 11 (1). (iv) 58 × 35 = ₹2,030 (2).", "1+1+1+2"),
 Q("(i) Show that 2 × (a + b) equals 2a + 2b for a = 5, b = 9. (ii) Show that it fails for 2 + a × b. (iii) State what this tells about brackets.", "(i) 28 = 10 + 18 (2). (ii) 2 + 45 = 47 ≠ 28 (2). (iii) Brackets change meaning (1).", "2+2+1"),
 Q("(i) Calculate 4,995 + 3,005 + 2,000 using a convenient grouping. (ii) Calculate 99 × 12. (iii) Calculate 1,002 × 15.", "(i) 4,995 + 3,005 = 8,000; + 2,000 = 10,000 (2). (ii) 1,188 (1.5). (iii) 15,030 (1.5).", "2+1½+1½"),
 Q("(i) Write an expression for the area of a floor 12 m × 9 m with a 3 m × 2 m rug removed. (ii) Evaluate. (iii) Cost to tile at ₹80 per m².", "(i) 12 × 9 − 3 × 2 (1). (ii) 102 m² (2). (iii) ₹8,160 (2).", "1+2+2"),
]
D = D[:16]
SETS, POOL = build(A, B, C, D)
