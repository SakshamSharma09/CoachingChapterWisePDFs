import random
from c7maths.h import *
R = random.Random(704)
A = []; B = []; C = []; D = []
# substitute (8)
for a, b, x in [(3, 5, 4), (2, 7, 6), (4, 1, 9), (5, 3, 2), (6, 2, 5), (7, 4, 3), (3, 8, 7), (9, 2, 4)]:
    v = a * x + b
    A.append(M4(f"If x = {x}, the value of {a}x + {b} is:", str(v), [str(a + x + b), str(v + a), str(a * (x + b))], f"{a} × {x} + {b}"))
# like terms simplify (8)
for a, b, c in [(3, 5, 2), (7, 2, 4), (6, 3, 1), (9, 4, 5), (8, 6, 2), (5, 5, 3), (4, 9, 7), (2, 8, 3)]:
    A.append(M4(f"Simplify {a}x + {b}x − {c}x.", f"{a+b-c}x", [f"{a+b+c}x", f"{a+b-c}x²", f"{a*b-c}x", f"{a+b}x"], "combine like terms: add and subtract coefficients"))
# translate (8)
A += [
 M4("‘5 more than a number n’ is written as:", "n + 5", ["5n", "n − 5", "5 − n"], "more than means add"),
 M4("‘3 times a number y’ is written as:", "3y", ["y + 3", "y³", "y/3"], "multiplication by 3"),
 M4("‘A number m decreased by 7’ is written as:", "m − 7", ["7 − m", "7m", "m + 7"], "decreased means subtract"),
 M4("‘Twice a number plus 1’ is written as:", "2n + 1", ["2(n + 1)", "n + 2", "2n − 1"], "twice n then plus 1"),
 M4("The perimeter of a square of side s is:", "4s", ["s²", "2s", "s + 4"], "four equal sides"),
 M4("The area of a square of side s is:", "s²", ["4s", "2s", "s + s"], "side × side"),
 M4("The perimeter of a rectangle with length l and breadth b is:", "2(l + b)", ["l + b", "lb", "2lb"], "twice the sum"),
 M4("n pencils cost ₹4 each. The total cost is:", "₹4n", ["₹(n + 4)", "₹n/4", "₹(4 − n)"], "price × number"),
]
# patterns & concepts (16)
A += [
 M4("In the pattern 5, 8, 11, 14 … the nth term is:", "3n + 2", ["3n + 5", "n + 3", "5n − 2"], "n=1 gives 5"),
 M4("The nth even number is:", "2n", ["2n + 1", "n + 2", "n²"], "2, 4, 6 …"),
 M4("The nth odd number is:", "2n − 1", ["2n", "2n + 2", "n + 1"], "1, 3, 5 …"),
 M4("The coefficient of x in 7x + 3 is:", "7", ["3", "x", "10"], "number multiplying x"),
 M4("Which pair are like terms?", "4a and 9a", ["4a and 4b", "3x and 3x²", "5 and 5y"], "same letter part"),
 M4("The expression 3a + 5a simplifies to:", "8a", ["8a²", "15a", "35a"], "3 + 5 = 8"),
 M4("Which is a letter-number (variable) expression?", "4k − 3", ["4 × 3 − 2", "10 + 6", "8 ÷ 2"], "contains k"),
 M4("The value of 2a + 3b for a = 4, b = 2 is:", "14", ["20", "10", "18"], "8 + 6"),
 M4("The expression 2(x + 3) equals:", "2x + 6", ["2x + 3", "x + 6", "2x + 5"], "distributive property"),
 M4("What is 5x − 3x?", "2x", ["8x", "2", "15x"], "5 − 3 = 2"),
 M4("If a matchstick pattern uses 3n + 1 sticks for n squares, then 5 squares need:", "16", ["15", "18", "21"], "3 × 5 + 1"),
 M4("A number is 3 less than twice x. It is:", "2x − 3", ["3 − 2x", "2(x − 3)", "x − 6"], "twice x then subtract 3"),
 M4("An expression with a single term is called a:", "monomial", ["binomial", "trinomial", "polynomial of 3 terms"], "mono = one"),
 M4("The number of terms in 3x + 2y − 5 is:", "3", ["2", "4", "1"], "3x, 2y and −5"),
 M4("If x = 0, then 7x + 4 =", "4", ["0", "7", "11"], "7 × 0 = 0"),
 M4("Simplify: 4x + 3 − x + 2.", "3x + 5", ["5x + 5", "3x + 1", "4x + 5"], "like terms combine"),
]
A = A[:40]
B = [
 Q("What is a letter-number? Why do we use it?", "A letter standing for an unknown or changing number (1); it lets us write general rules (1).", "1+1"),
 Q("Write an expression: ‘7 less than 4 times a number x’.", "4x − 7 (2).", "2"),
 Q("Find the value of 5a − 2 for a = 6.", "5 × 6 − 2 = 28 (2).", "2"),
 Q("Simplify: 9y − 4y + 2y.", "7y (2).", "2"),
 Q("What are like terms? Give an example.", "Terms with the same letter part (1); 3x and 8x (1).", "1+1"),
 Q("Write the rule for the nth term of 4, 7, 10, 13 …", "3n + 1 (2).", "2"),
 Q("A notebook costs ₹p. Write the cost of 12 notebooks and of 12 notebooks and a ₹5 pen.", "12p (1); 12p + 5 (1).", "1+1"),
 Q("Expand 3(a + 4).", "3a + 12 (2).", "2"),
 Q("Simplify 5x + 3 + 2x − 1.", "7x + 2 (2).", "2"),
 Q("The side of a square is s. Write its perimeter and area. Evaluate for s = 5.", "4s = 20; s² = 25 (2).", "1+1"),
 Q("What is the difference between 2x and x²?", "2x means x + x; x² means x × x (1); for x = 3 they are 6 and 9 (1).", "1+1"),
 Q("A pattern is made with n tiles needing 2n + 3 sticks. How many for 10 tiles?", "23 sticks (2).", "2"),
 Q("Write an expression for the sum of three consecutive numbers starting with n.", "n + (n + 1) + (n + 2) = 3n + 3 (2).", "2"),
 Q("Find the value of 3x² for x = 4.", "3 × 16 = 48 (2).", "2"),
 Q("If a = 2 and b = 3, find ab + a + b.", "6 + 2 + 3 = 11 (2).", "2"),
 Q("Identify the coefficient and constant in 8k − 5.", "Coefficient 8 (1); constant −5 (1).", "1+1"),
]
C = [
 Q("Simplify 6a + 4b − 2a + b − 3.", "4a + 5b − 3 (3).", "3"),
 Q("A taxi charges ₹20 plus ₹12 per km. Write an expression and find the fare for 7 km.", "20 + 12k (1.5); ₹104 (1.5).", "1½+1½"),
 Q("Find the nth term of 7, 12, 17, 22 … and the 20th term.", "5n + 2 (1.5); 102 (1.5).", "1½+1½"),
 Q("Using x for the number of rows, write the number of chairs in a hall with 8 chairs per row and 5 extra chairs.", "8x + 5 (3).", "3"),
 Q("Evaluate 3a² − 2a + 1 for a = 3.", "27 − 6 + 1 (1.5); = 22 (1.5).", "1½+1½"),
 Q("Simplify: 3(x + 2) + 2(x − 1).", "3x + 6 + 2x − 2 (1.5); = 5x + 4 (1.5).", "1½+1½"),
 Q("Write the perimeter of a rectangle with sides (3x + 2) and (2x + 1).", "2(5x + 3) (1.5); = 10x + 6 (1.5).", "1½+1½"),
 Q("A square pattern uses 4n − (n − 1) sticks for n squares in a row. Simplify.", "4n − n + 1 = 3n + 1 (3).", "3"),
 Q("Ramu has ₹x. He spends ₹40 and gets ₹15 back. Write his money now and find it for x = 100.", "x − 40 + 15 = x − 25 (1.5); 75 (1.5).", "1½+1½"),
 Q("Show that 2(x + 4) and 2x + 8 give the same value for x = 5.", "2 × 9 = 18 (1.5); 10 + 8 = 18 (1.5).", "1½+1½"),
 Q("Three consecutive even numbers start at 2n. Write them and their sum.", "2n, 2n + 2, 2n + 4 (1.5); 6n + 6 (1.5).", "1½+1½"),
 Q("Subtract 3x − 2 from 7x + 5.", "7x + 5 − 3x + 2 = 4x + 7 (3).", "3"),
 Q("Ramu is r years old. His father is 4 years more than 3 times Ramu's age. Write the father's age and find it for r = 12.", "3r + 4 (1.5); 40 years (1.5).", "1½+1½"),
 Q("Find the value of (a + b)² for a = 2, b = 3 and compare it with a² + b².", "25 (1); 13 (1); not equal (1).", "1+1+1"),
 Q("Write the expression for the area of a rectangle of length (x + 3) and breadth 4 and expand.", "4(x + 3) = 4x + 12 (3).", "3"),
 Q("The cost of a pen is ₹a and a pencil is ₹b. Write the cost of 5 pens and 8 pencils and evaluate for a = 12, b = 3.", "5a + 8b (1.5); 60 + 24 = ₹84 (1.5).", "1½+1½"),
 Q("Rewrite 12x + 18 by taking out a common factor.", "6(2x + 3) (3).", "3"),
 Q("Find the missing term: 5m + __ = 9m.", "4m (3).", "3"),
 Q("Simplify 15x − 4(x − 2).", "15x − 4x + 8 = 11x + 8 (3).", "3"),
 Q("A rectangular garden has length l and width l − 2. Write its perimeter and find it for l = 9.", "2(2l − 2) = 4l − 4 (1.5); 32 (1.5).", "1½+1½"),
 Q("Add 4a + 3b and 2a − 5b.", "6a − 2b (3).", "3"),
 Q("A bus carries 40 passengers. At each stop x get off and y get on. Write the number after one stop.", "40 − x + y (3).", "3"),
 Q("A shopkeeper gives a discount of ₹d on each of 6 items priced ₹p. Write the total price.", "6(p − d) = 6p − 6d (3).", "3"),
 Q("Find the value of 5 − 2k for k = 3 and explain a negative result.", "5 − 6 = −1 (1.5); 6 is greater than 5 (1.5).", "1½+1½"),
]
D = [
 Q("(i) Simplify 7a + 3b − 2a + 5b. (ii) Evaluate it for a = 2, b = 3. (iii) Write the expression for 4 times it.", "(i) 5a + 8b (2). (ii) 34 (1). (iii) 20a + 32b (2).", "2+1+2"),
 Q("<b>Case study:</b> Matchsticks are used to make a row of triangles: 3 sticks for 1 triangle, 5 for 2, 7 for 3. (i) Write the rule. (ii) Sticks for 10 triangles. (iii) How many triangles with 41 sticks? (iv) Explain the rule.", "(i) 2n + 1 (1). (ii) 21 (1). (iii) 20 (2). (iv) 3 sticks first, then 2 more per triangle (1).", "1+1+2+1"),
 Q("(i) Expand 4(2x − 3). (ii) Simplify 4(2x − 3) + 5x. (iii) Evaluate for x = 2.", "(i) 8x − 12 (1.5). (ii) 13x − 12 (2). (iii) 14 (1.5).", "1½+2+1½"),
 Q("(i) A rectangle has length (2x + 5) and width x. Write perimeter. (ii) Write area. (iii) Evaluate both for x = 3.", "(i) 2(3x + 5) = 6x + 10 (1.5). (ii) x(2x + 5) = 2x² + 5x (1.5). (iii) 28 and 33 (2).", "1½+1½+2"),
 Q("<b>Case study:</b> A phone plan costs ₹199 plus ₹3 per extra GB. (i) Cost for g GB. (ii) Cost for 6 GB. (iii) GB used if bill is ₹250. (iv) Write the cost for a family of 3 with g GB each.", "(i) 199 + 3g (1). (ii) ₹217 (1). (iii) 17 GB (2). (iv) 3(199 + 3g) (1).", "1+1+2+1"),
 Q("(i) Show that the sum of two consecutive numbers is odd. (ii) Write the general form. (iii) Find the sum for 17 and 18.", "(i) n + (n + 1) = 2n + 1 (2). (ii) 2n + 1 (1). (iii) 35 (2).", "2+1+2"),
 Q("(i) Find the nth term of 2, 6, 10, 14 … (ii) Find the 25th term. (iii) Which term is 98?", "(i) 4n − 2 (2). (ii) 98 (1.5). (iii) 25th term (1.5).", "2+1½+1½"),
 Q("(i) Simplify 3(x + 4) − 2(x − 1) + 5. (ii) Evaluate at x = 6. (iii) Check by direct substitution.", "(i) x + 19 (2). (ii) 25 (1). (iii) 3 × 10 − 2 × 5 + 5 = 25 (2).", "2+1+2"),
 Q("(i) A square garden has side (x + 2). Write its perimeter and area. (ii) For x = 4, find them. (iii) Fencing costs ₹15 per m; find the cost.", "(i) 4x + 8 and (x + 2)² (2). (ii) 24 m, 36 m² (2). (iii) ₹360 (1).", "2+2+1"),
 Q("<b>Case study:</b> Rina thinks a number, adds 5, multiplies by 2, subtracts 6 and gets 18. (i) Write the steps as an expression. (ii) Simplify. (iii) Find the number. (iv) Verify.", "(i) 2(n + 5) − 6 (1). (ii) 2n + 4 (1). (iii) n = 7 (2). (iv) 2 × 12 − 6 = 18 (1).", "1+1+2+1"),
 Q("(i) Add 5x² + 3x − 2 and 2x² − x + 7. (ii) Subtract the second from the first. (iii) Evaluate the sum at x = 1.", "(i) 7x² + 2x + 5 (2). (ii) 3x² + 4x − 9 (2). (iii) 14 (1).", "2+2+1"),
 Q("(i) What is the rule for the perimeter of a regular pentagon of side a? (ii) Find for a = 7.5. (iii) Which regular polygon has perimeter 6a?", "(i) 5a (1). (ii) 37.5 (2). (iii) Hexagon (2).", "1+2+2"),
 Q("<b>Case study:</b> A hall has x rows of 12 chairs and 4 extra chairs. (i) Expression. (ii) For 15 rows. (iii) Chairs needed for 200 guests: rows required. (iv) Extra chairs if 15 rows hold 180.", "(i) 12x + 4 (1). (ii) 184 (1). (iii) at least 17 rows (2). (iv) 4 (1).", "1+1+2+1"),
 Q("(i) Verify (a + 2)(a + 3) = a² + 5a + 6 for a = 4. (ii) Verify for a = 1. (iii) State conclusion.", "(i) 42 = 16 + 20 + 6 (2). (ii) 12 = 1 + 5 + 6 (2). (iii) Identity holds (1).", "2+2+1"),
 Q("(i) Give a pattern from which 7n − 3 arises. (ii) List first 4 terms. (iii) Find the 12th term.", "(i) any like 4, 11, 18… (1). (ii) 4, 11, 18, 25 (2). (iii) 81 (2).", "1+2+2"),
 Q("(i) Why are letters useful in generalising? (ii) Give two uses in everyday life. (iii) Write the formula for simple interest in letters.", "(i) One rule for all numbers (2). (ii) Fares, bills, areas (2). (iii) SI = PRT/100 (1).", "2+2+1"),
]
D = D[:16]
SETS, POOL = build(A, B, C, D)
