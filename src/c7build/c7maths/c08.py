import random
from fractions import Fraction as F
from c7maths.h import *
R = random.Random(708)
def fs(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"
def mix(x):
    x = F(x); w = x.numerator // x.denominator; r = x - w
    return f"{w} {fs(r)}" if w and r else (str(w) if w else fs(r))
A = []; B = []; C = []; D = []
prs = [(F(2, 3), F(3, 4)), (F(5, 6), F(3, 10)), (F(4, 5), F(15, 16)), (F(7, 8), F(2, 7)), (F(3, 5), F(10, 9)), (F(9, 4), F(2, 3)), (F(5, 7), F(14, 15)), (F(11, 6), F(3, 4))]
for a, b in prs:
    v = a * b
    A.append(M4(f"{fs(a)} × {fs(b)} =", fs(v), [fs(a + b), fs(a / b), fs(v + F(1, 6))], "multiply numerators and denominators, then simplify"))
for a, b in [(F(3, 4), F(1, 2)), (F(5, 6), F(5, 12)), (F(2, 3), F(4, 9)), (F(7, 8), F(3, 4)), (F(9, 10), F(3, 5)), (F(4, 7), F(2, 3))]:
    v = a / b
    A.append(M4(f"{fs(a)} ÷ {fs(b)} =", fs(v), [fs(a * b), fs(b / a), fs(a - b)], "multiply by the reciprocal of the divisor"))
for a in [F(3, 5), F(7, 4), F(9, 11), F(1, 8), F(13, 6)]:
    A.append(M4(f"The reciprocal of {fs(a)} is:", fs(1 / a), [fs(-a), fs(a), fs(1 - a) if a < 1 else fs(a - 1)], "interchange numerator and denominator"))
for n, a in [(24, F(3, 8)), (45, F(2, 5)), (60, F(5, 6)), (36, F(7, 9)), (28, F(3, 4)), (72, F(5, 8))]:
    v = n * a
    A.append(M4(f"{fs(a)} of {n} is:", fs(v), [fs(n / a), fs(n + a), fs(v + 3)], "‘of’ means multiply"))
for a, b in [(F(2, 5), 10), (F(3, 7), 14), (F(5, 9), 18)]:
    pass
A += [
 M4("The product of a fraction and its reciprocal is:", "1", ["0", "the fraction", "2"], "(a/b) × (b/a)"),
 M4("The reciprocal of 0 is:", "not defined", ["0", "1", "∞ and defined"], "cannot divide by 0"),
 M4("Dividing by a fraction is the same as:", "multiplying by its reciprocal", ["multiplying by the fraction", "adding the reciprocal", "subtracting"], "rule"),
 M4("Multiplying a number by a proper fraction gives a result that is:", "smaller than the number", ["greater than the number", "equal to the number", "always 0"], "e.g. 1/2 × 8 = 4"),
 M4("Dividing a number by a proper fraction gives a result that is:", "greater than the number", ["smaller than the number", "equal to the number", "always 1"], "e.g. 8 ÷ 1/2 = 16"),
 M4("1/2 of 1/2 is:", "1/4", ["1", "1/2", "2"], "1/2 × 1/2"),
 M4("How many 1/4 are there in 3?", "12", ["3/4", "4/3", "7"], "3 ÷ 1/4 = 12"),
 M4("The mixed number 2 1/3 as an improper fraction is:", "7/3", ["6/3", "5/3", "3/7"], "2 × 3 + 1"),
 M4("The area of a rectangle 2/3 m by 3/5 m is:", "2/5 m²", ["19/15 m²", "9/10 m²", "10/9 m²"], "2/3 × 3/5"),
 M4("The reciprocal of 1 is:", "1", ["0", "−1", "not defined"], "1 × 1 = 1"),
 M4("5 ÷ (1/3) =", "15", ["5/3", "3/5", "8"], "5 × 3"),
 M4("A rope of 6 m is cut into pieces of 3/4 m. The number of pieces is:", "8", ["6", "9", "4.5"], "6 ÷ 3/4 = 8"),
]
A += [
 M4("Which of these is the reciprocal of 2 1/2?", "2/5", ["5/2", "1/2", "2 1/5"], "2 1/2 = 5/2"),
 M4("3/4 of 1/2 equals:", "3/8", ["3/2", "1/4", "5/4"], "3/4 × 1/2"),
 M4("A pizza is cut into 8 equal slices. Each is what fraction of 1/2 pizza?", "1/4", ["1/8", "2", "4"], "1/8 ÷ 1/2"),
]
A = A[:40]
B = [
 Q("Multiply 3/5 × 10/21 and write the answer in the lowest terms.", "30/105 = 2/7 (2).", "2"),
 Q("Find the reciprocal of 7/9 and of 5.", "9/7 (1); 1/5 (1).", "1+1"),
 Q("Divide 5/6 by 10/9.", "5/6 × 9/10 = 3/4 (2).", "2"),
 Q("Find 2/3 of 45 litres.", "30 litres (2).", "2"),
 Q("Write 3 1/2 × 2/7 and evaluate.", "7/2 × 2/7 = 1 (2).", "2"),
 Q("Why is dividing by 1/2 the same as multiplying by 2?", "Two halves fit in each whole (2).", "2"),
 Q("How many pieces of 1/8 m can be cut from 3 m ribbon?", "24 (2).", "2"),
 Q("Is 4/5 ÷ 2/3 equal to 2/3 ÷ 4/5? Check.", "6/5 and 5/6: not equal (2).", "2"),
 Q("Find the area of a rectangle 3/4 m by 5/6 m.", "5/8 m² (2).", "2"),
 Q("Simplify 12/25 × 15/16.", "9/20 (2).", "2"),
 Q("Convert 2 3/4 to improper fraction and find its reciprocal.", "11/4 (1); 4/11 (1).", "1+1"),
 Q("A bottle holds 3/4 L. How many litres in 6 bottles?", "4 1/2 L (2).", "2"),
 Q("Which is larger, 3/4 × 2/3 or 3/4 ÷ 2/3? Why?", "Division gives 9/8, larger since divisor <1 (2).", "2"),
 Q("Find 1/3 of 1/4.", "1/12 (2).", "2"),
 Q("Find the number which when multiplied by 4/9 gives 8/27.", "2/3 (2).", "2"),
 Q("Divide 7 by 1 3/4.", "7 ÷ 7/4 = 4 (2).", "2"),
]
C = [
 Q("Find 2 2/5 × 1 7/8 and write as a mixed number.", "12/5 × 15/8 = 9/2 (1.5); 4 1/2 (1.5).", "1½+1½"),
 Q("Divide 3 1/3 by 5/6.", "10/3 × 6/5 = 4 (3).", "3"),
 Q("A car runs 15 km per litre. How far will it go on 2 2/5 litres?", "15 × 12/5 = 36 km (3).", "3"),
 Q("A rope is 9 m long. How many pieces of 3/4 m can be cut and what remains?", "12 pieces (2); nothing remains (1).", "2+1"),
 Q("Find the product 5/8 × 16/25 × 5/6.", "1/3 (3).", "3"),
 Q("What is the reciprocal of (2/3 + 1/2)?", "7/6 → reciprocal 6/7 (3).", "3"),
 Q("A tank is 3/5 full. After using 1/4 of the water it holds, what fraction is full?", "3/5 × 3/4 = 9/20 (3).", "3"),
 Q("A recipe uses 3/4 cup of flour for one batch. How much for 2 1/2 batches?", "3/4 × 5/2 = 15/8 = 1 7/8 cups (3).", "3"),
 Q("Divide 2/3 by 4 and 4 by 2/3.", "1/6 (1.5); 6 (1.5).", "1½+1½"),
 Q("Rahul spent 2/5 of ₹750 on books and 1/3 of the rest on food. Find the amount left.", "Books ₹300, rest ₹450; food ₹150; left ₹300 (3).", "3"),
 Q("The product of two fractions is 3/10; one is 3/5. Find the other.", "1/2 (3).", "3"),
 Q("Which is greater: 5/6 × 3/4 or 5/6 ÷ 3/4?", "5/8 vs 10/9; division (3).", "3"),
 Q("A farmer has 5 1/4 acres. He plants 2/3 of it with wheat. How many acres is wheat?", "7/2 = 3 1/2 acres (3).", "3"),
 Q("A bus takes 1 1/2 hours for 63 km. Find its average speed.", "63 ÷ 3/2 = 42 km/h (3).", "3"),
 Q("A cloth of 7 1/2 m is cut into pieces of 3/4 m. How many pieces?", "10 (3).", "3"),
 Q("Evaluate 2/3 × (3/4 + 1/6).", "2/3 × 11/12 = 11/18 (3).", "3"),
 Q("Simplify 1 1/2 ÷ 3/4 × 2/5.", "2 × 2/5 = 4/5 (3).", "3"),
 Q("What fraction of an hour is 18 minutes? Of a day is 6 hours?", "3/10 (1.5); 1/4 (1.5).", "1½+1½"),
 Q("A can holds 5/8 L. How many cans fill a 10 L drum?", "16 cans (3).", "3"),
 Q("Find the sides if a square has area 4/9 m².", "2/3 m (3).", "3"),
 Q("One-third of a number is 12. Find three-fourths of it.", "Number 36; 27 (3).", "3"),
 Q("A man walks 3/4 km each morning. How far in 12 days?", "9 km (3).", "3"),
 Q("A shopkeeper sold 3/5 of 2 1/2 kg sugar. How much was left?", "Sold 1 1/2 kg; left 1 kg (3).", "3"),
 Q("Which one is smaller: 3/8 of 24 or 5/6 of 12?", "9 vs 10; first smaller (3).", "3"),
]
D = [
 Q("(i) Multiply 3 1/3 by 2 1/4. (ii) Divide the answer by 5/6. (iii) Write each as a mixed number.", "(i) 7 1/2 (2). (ii) 9 (2). (iii) as shown (1).", "2+2+1"),
 Q("<b>Case study:</b> A farmer has 12 acres. 3/4 is used for wheat, 1/6 of the remainder for vegetables and the rest is empty. (i) Wheat area. (ii) Remainder. (iii) Vegetables. (iv) Empty land.", "(i) 9 (1). (ii) 3 (1). (iii) 1/2 acre (1). (iv) 2 1/2 acres (2).", "1+1+1+2"),
 Q("(i) Explain division of fractions using 3 ÷ 1/4. (ii) Find 2/5 ÷ 3/10. (iii) Check by multiplication.", "(i) 12 fourths (2). (ii) 4/3 (2). (iii) 4/3 × 3/10 = 2/5 (1).", "2+2+1"),
 Q("(i) A tank holds 240 L; 3/8 is empty. (ii) Water poured is 5/12 of the empty part. (iii) Find the water poured and the new empty part.", "(i) Empty 90 L (2). (ii) 37.5 L (2). (iii) 52.5 L empty (1).", "2+2+1"),
 Q("<b>Case study:</b> A ribbon of 15 m is cut into pieces of 5/6 m for gift wrapping. (i) Number of pieces. (ii) If each piece costs ₹12, total. (iii) Left if 4 pieces damaged. (iv) Length wasted.", "(i) 18 (1). (ii) ₹216 (1). (iii) 14 pieces (1). (iv) 10/3 m (2).", "1+1+1+2"),
 Q("(i) Find the reciprocal of 1 2/3. (ii) Verify the product with the number is 1. (iii) Find (1 2/3)².", "(i) 3/5 (1). (ii) 5/3 × 3/5 = 1 (2). (iii) 25/9 (2).", "1+2+2"),
 Q("(i) Show 3/4 × 8/9 = 2/3. (ii) Find 2/3 ÷ 8/9. (iii) Compare with 3/4.", "(i) 24/36 (2). (ii) 3/4 (2). (iii) Equal (1).", "2+2+1"),
 Q("(i) A cyclist covers 4 1/2 km in 3/4 hour. Find speed. (ii) Distance in 2 1/2 h. (iii) Time for 27 km.", "(i) 6 km/h (2). (ii) 15 km (2). (iii) 4 1/2 h (1).", "2+2+1"),
 Q("<b>Case study:</b> A tailor needs 1 3/4 m of cloth per shirt. He has 21 m. (i) Shirts. (ii) Cloth left. (iii) If each shirt sells for ₹450, income. (iv) Cost of cloth at ₹120/m.", "(i) 12 (1). (ii) 0 (1). (iii) ₹5,400 (1). (iv) ₹2,520 (2).", "1+1+1+2"),
 Q("(i) Find the area of a rectangle 5 1/2 m by 2 2/3 m. (ii) The cost of flooring at ₹90 per m². (iii) Perimeter.", "(i) 44/3 m² (2). (ii) ₹1,320 (2). (iii) 16 1/3 m (1).", "2+2+1"),
 Q("(i) Why does multiplying by a proper fraction reduce a number? (ii) Why does dividing by a proper fraction increase it? (iii) Give examples.", "(i) Takes a part (2). (ii) More parts fit (2). (iii) 1/2 × 8 = 4; 8 ÷ 1/2 = 16 (1).", "2+2+1"),
 Q("(i) Simplify 2/3 + 1/4 × 8/9. (ii) Simplify (2/3 + 1/4) × 8/9. (iii) Compare.", "(i) 8/9 (2). (ii) 22/27 (2). (iii) 8/9 = 24/27 larger (1).", "2+2+1"),
 Q("<b>Case study:</b> A mixture is made of 2/5 part syrup and the rest water. A bottle holds 1 1/2 L. (i) Syrup. (ii) Water. (iii) Number of 3/10 L glasses from the bottle. (iv) Syrup in one glass.", "(i) 3/5 L (1). (ii) 9/10 L (1). (iii) 5 (1). (iv) 3/25 L (2).", "1+1+1+2"),
 Q("(i) Find x if 3/4 × x = 15. (ii) Find y if y ÷ 2/5 = 10. (iii) Check.", "(i) 20 (2). (ii) 4 (2). (iii) 15 = 3/4 × 20 and 4 ÷ 0.4 = 10 (1).", "2+2+1"),
 Q("(i) A book of 360 pages: Meena read 2/9, then 3/8 of the rest. Pages left. (ii) What fraction remains?", "(i) Read 80; rest 280; then 105; left 175 (3). (ii) 175/360 = 35/72 (2).", "3+2"),
 Q("(i) Express 3/4 km in metres. (ii) 2/5 of an hour in minutes. (iii) 5/8 kg in grams.", "(i) 750 m (2). (ii) 24 min (2). (iii) 625 g (1).", "2+2+1"),
]
D = D[:16]
SETS, POOL = build(A, B, C, D)
