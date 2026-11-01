import random
from c7maths.h import *
R = random.Random(706)
A = []; B = []; C = []; D = []
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
for k in [6, 7, 8, 9]:
    v = fib[k]
    A.append(M4(f"In the Virahāṅka sequence 1, 2, 3, 5, 8, … the term after {fib[k-1]} is:", str(v), [str(v + 1), str(v - 1), str(fib[k-1] * 2)], "each term is the sum of the two before it"))
for a, b in [(7, 8), (14, 9), (25, 6), (36, 11), (45, 12)]:
    s = a + b
    A.append(M4(f"The sum of {a} and {b} is:", "odd" if s % 2 else "even", ["even" if s % 2 else "odd", "neither", "both"], f"{'odd' if a%2 else 'even'} + {'odd' if b%2 else 'even'}"))
for a, b in [(7, 9), (12, 5), (8, 6), (13, 11)]:
    p = a * b
    A.append(M4(f"The product {a} × {b} is:", "odd" if p % 2 else "even", ["even" if p % 2 else "odd", "neither", "both"], "a product is odd only if both numbers are odd"))
A += [
 M4("The sum of two odd numbers is always:", "even", ["odd", "prime", "a multiple of 3"], "odd + odd"),
 M4("The sum of an even and an odd number is always:", "odd", ["even", "zero", "prime"], "parity rule"),
 M4("The product of an even number and any whole number is:", "even", ["odd", "prime", "always 0"], "has a factor 2"),
 M4("Which number is NOT a palindrome?", "1234", ["1331", "4554", "909"], "reads differently from the right"),
 M4("Kaprekar's constant for 4-digit numbers is:", "6174", ["1729", "1089", "9999"], "repeated rearrangement process"),
 M4("The number 1729 is famous as the:", "Hardy–Ramanujan number", ["Kaprekar number", "smallest prime", "square number"], "smallest sum of two cubes in two ways"),
 M4("A number is divisible by 9 if the sum of its digits is divisible by:", "9", ["3 only", "6", "2"], "digit-sum rule"),
 M4("A number is divisible by 5 if its last digit is:", "0 or 5", ["5 only", "0 only", "any odd digit"], "rule"),
 M4("A number is divisible by 4 if its last two digits form a number divisible by:", "4", ["2 only", "8", "5"], "100 is divisible by 4"),
 M4("Which of these is divisible by 3?", "4,512", ["4,513", "4,511", "4,510"], "4+5+1+2 = 12"),
 M4("The sum of the first 5 odd numbers is:", "25", ["15", "20", "30"], "1+3+5+7+9 = 5²"),
 M4("The sum of the first n odd numbers is:", "n²", ["2n", "n + 1", "n(n + 1)"], "a square-number pattern"),
 M4("In the sequence 2, 4, 6, 8, … the 10th term is:", "20", ["18", "22", "10"], "2n"),
 M4("A 3 × 3 magic square has a magic sum of 15 when it uses:", "1 to 9", ["1 to 10", "0 to 8", "2 to 10"], "each row, column, diagonal adds to 15"),
 M4("In a magic square the centre of 1–9 is:", "5", ["1", "9", "3"], "middle of the arithmetic sequence"),
 M4("A letter puzzle: if 3A + 2 = 17 then A =", "5", ["4", "6", "3"], "3 × 5 = 15"),
 M4("In a cryptarithm A + A = 10 gives A =", "5", ["4", "6", "2"], "5 + 5"),
 M4("The number 100 is a ___ number.", "square", ["prime", "odd", "triangular only"], "10 × 10"),
 M4("Consecutive numbers always have a sum that is:", "odd", ["even", "multiple of 4", "multiple of 3"], "n + (n + 1) = 2n + 1"),
 M4("The Virahāṅka numbers were first studied in India while counting:", "rhythm patterns (long and short beats)", ["planet orbits", "coins", "triangles"], "poetic metres"),
 M4("The number of ways to make a 5-beat rhythm using 1-beat and 2-beat sounds is:", "8", ["5", "6", "10"], "Virahāṅka number"),
 M4("The digit sum of 3,456 is:", "18", ["17", "19", "15"], "3+4+5+6"),
 M4("The smallest 3-digit palindrome is:", "101", ["100", "111", "121"], "1 0 1"),
 M4("Reverse of 4,521 is:", "1,254", ["1,452", "2,541", "5,412"], "digits read backwards"),
 M4("If 6 × B ends in 4, one value of B is:", "4", ["3", "5", "7"], "6 × 4 = 24"),
 M4("The next number in 1, 4, 9, 16, … is:", "25", ["20", "24", "36"], "squares"),
]
A.append(M4("The number of odd numbers between 1 and 10 (inclusive) is:", "5", ["4", "6", "10"], "1, 3, 5, 7, 9"))
A = A[:40]
B = [
 Q("State the rule for the sum of two odd numbers and give an example.", "The sum is even (1); 7 + 9 = 16 (1).", "1+1"),
 Q("Is the product of two odd numbers odd or even? Explain.", "Odd (1); no factor 2 is present (1).", "1+1"),
 Q("Write the first 8 terms of the Virahāṅka sequence.", "1, 2, 3, 5, 8, 13, 21, 34 (2).", "2"),
 Q("What is a palindrome? Give two examples.", "A number that reads the same both ways (1); 121 and 4554 (1).", "1+1"),
 Q("Is 3,654 divisible by 9? Show.", "3 + 6 + 5 + 4 = 18 (1); yes (1).", "1+1"),
 Q("Find the sum of the first 6 odd numbers.", "36 (2).", "2"),
 Q("Is 2,35,716 even or odd? Why?", "Even, as it ends in 6 (2).", "2"),
 Q("In a magic square of 1–9, what is the magic sum and centre?", "15; 5 (1+1).", "1+1"),
 Q("Solve the puzzle: 4 + A = 12.", "A = 8 (2).", "2"),
 Q("Which is bigger: 99 × 99 or 100 × 98? Check by calculation.", "9,801 vs 9,800; first is bigger (2).", "2"),
 Q("State the divisibility rule for 11 using 121 as example.", "Difference of alternate digit sums is 0 or multiple of 11: 1 + 1 − 2 = 0 (2).", "2"),
 Q("Reverse 7,251 and find the difference with it.", "1,527; 5,724 (2).", "2"),
 Q("Why is 0 considered an even number?", "0 = 2 × 0 so it is divisible by 2 (2).", "2"),
 Q("Find the next two numbers: 3, 6, 12, 24, …", "48, 96 (2).", "2"),
 Q("A number is 9 times a digit and has digit sum 9. Name two such 2-digit numbers.", "18 and 27 (2).", "2"),
 Q("Add: 1 + 3 + 5 + 7 + 9 + 11. Which pattern is shown?", "36 = 6² (2).", "2"),
]
C = [
 Q("Prove that the sum of three consecutive numbers is divisible by 3.", "n + (n + 1) + (n + 2) = 3n + 3 (1.5); = 3(n + 1) (1.5).", "1½+1½"),
 Q("Show how a Virahāṅka number can count rhythms of 6 beats.", "Possible with 1 and 2 beats: 13 ways (3).", "3"),
 Q("Take the number 3,524. Apply the Kaprekar step once.", "5432 − 2345 = 3087 (3).", "3"),
 Q("Solve the cryptarithm: A B + A B = B C where A, B, C digits.", "e.g. 25 + 25 = 50 (A=2, B=5, C=0) (3).", "3"),
 Q("Complete the 3 × 3 magic square with centre 5 whose first row is 2, _, 6.", "2 7 6 / 9 5 1 / 4 3 8 (3).", "3"),
 Q("Is the number 7,284 divisible by 3 and 4? Show.", "7 + 2 + 8 + 4 = 21, divisible by 3 (1.5); 84 divisible by 4 (1.5).", "1½+1½"),
 Q("Find the sum of first 10 odd numbers and explain without adding.", "10² = 100 (1.5); pattern n² (1.5).", "1½+1½"),
 Q("Explain why the sum of two even numbers is even.", "2a + 2b = 2(a + b) (3).", "3"),
 Q("Write the grid pattern for multiples of 9 up to 99 and state one observation.", "9, 18, 27 … digits add to 9 (3).", "3"),
 Q("Make 3 palindromes from the sum of a number and its reverse: 12 + 21 = 33; do 25 + 52.", "77 (1.5); palindrome (1.5).", "1½+1½"),
 Q("Find the missing digit: 5,_,3 is divisible by 9 for what digit?", "5 + x + 3 divisible by 9: x = 1 (3).", "3"),
 Q("Is the product 13 × 14 × 15 odd or even? Explain.", "Even; it has the even factors 14 (3).", "3"),
 Q("Write the first 6 triangular numbers and their pattern.", "1, 3, 6, 10, 15, 21; differences 2, 3, 4, … (3).", "3"),
 Q("Show 1089 trick: choose 321, reverse 123, subtract, reverse the result and add.", "321 − 123 = 198; 198 + 891 = 1089 (3).", "3"),
 Q("Using parity, show that 2 + 4 + 6 + 8 + 9 is odd.", "Only one odd number so sum is odd (3).", "3"),
 Q("If a sum of 5 odd numbers is S, is S odd or even? Why?", "Odd, as an odd count of odd numbers sums to odd (3).", "3"),
 Q("A 4 × 4 grid has each cell with the sum of row and column numbers. Find the cell (3, 5).", "3 + 5 = 8 (3).", "3"),
 Q("Which is greater: sum of first 8 odd numbers or 60? Show.", "8² = 64 > 60 (3).", "3"),
 Q("In a letter puzzle 7 × K = 63. Find K and K × K.", "K = 9; 81 (3).", "3"),
 Q("Explain the digit root of 478 and check whether 478 is divisible by 3.", "4 + 7 + 8 = 19; 1 + 9 = 10; 1; not divisible (3).", "3"),
 Q("Find two numbers between 50 and 70 that are both palindromes.", "55 and 66 (3).", "3"),
 Q("Explain whether 3,001 × 5 is odd or even and what its last digit is.", "Odd; ends in 5 (3).", "3"),
 Q("Write 36 as a sum of consecutive odd numbers starting from 1.", "1 + 3 + 5 + 7 + 9 + 11 (3).", "3"),
 Q("Explain why any number and its digit-reverse differ by a multiple of 9 (two digits).", "(10a + b) − (10b + a) = 9(a − b) (3).", "3"),
]
D = [
 Q("(i) Write the first 10 terms of the Virahāṅka sequence. (ii) Show each rule step. (iii) Which term is 144?", "(i) 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 (2). (ii) Add previous two (1). (iii) 11th term (2).", "2+1+2"),
 Q("<b>Case study:</b> A poet makes lines using short (1-beat) and long (2-beat) syllables. (i) How many lines of 4 beats? (ii) List them. (iii) How many for 5 beats? (iv) Name the sequence.", "(i) 5 (1). (ii) 1111, 112, 121, 211, 22 (2). (iii) 8 (1). (iv) Virahāṅka (1).", "1+2+1+1"),
 Q("(i) Prove that the sum of two odd numbers is even. (ii) Prove that odd × odd is odd. (iii) Use these to decide the parity of 7 × 9 + 11.", "(i) (2a + 1) + (2b + 1) = 2(a + b + 1) (1.5). (ii) (2a + 1)(2b + 1) = 2(…) + 1 (1.5). (iii) 63 + 11 = even (2).", "1½+1½+2"),
 Q("(i) Apply the Kaprekar routine to 4,321. (ii) Repeat until it stops. (iii) What constant do you get?", "(i) 4321 − 1234 = 3087 (1). (ii) 8730 − 378 = 8352; 8532 − 2358 = 6174 (3). (iii) 6174 (1).", "1+3+1"),
 Q("<b>Case study:</b> Meena builds a 3 × 3 magic square with centre 5 and 1–9. (i) What is the magic sum? (ii) Which numbers go at corners? (iii) Give one full square. (iv) Check one diagonal.", "(i) 15 (1). (ii) Even numbers 2, 4, 6, 8 (1). (iii) 2 7 6 / 9 5 1 / 4 3 8 (2). (iv) 2 + 5 + 8 = 15 (1).", "1+1+2+1"),
 Q("(i) State divisibility tests for 2, 3, 5, 9, 10. (ii) Test 8,730. (iii) Test 4,725.", "(i) Last digit even; digit sum by 3; last digit 0/5; digit sum by 9; last digit 0 (2). (ii) Divisible by 2, 3, 5, 9, 10 (1.5). (iii) By 3, 5, 9 (1.5).", "2+1½+1½"),
 Q("(i) Solve the cryptarithm: 3A + 2B = 28 and A + B = 10 for digits. (ii) Check.", "(i) A = 8, B = 2 (4). (ii) 24 + 4 = 28 (1).", "4+1"),
 Q("(i) Show 1 + 3 + 5 + 7 = 16. (ii) Express the sum of first 12 odd numbers. (iii) Explain through square arrays.", "(i) 4² (1). (ii) 144 (2). (iii) Each L-shaped layer adds the next odd number (2).", "1+2+2"),
 Q("(i) A 2-digit number and its reverse add to 121. Show the digit sum a + b is 11. (ii) Give two such numbers. (iii) Why is the sum always a multiple of 11?", "(i) 11(a + b) = 121, so a + b = 11 (2). (ii) 56 and 47 (2). (iii) 10a + b + 10b + a = 11(a + b) (1).", "2+2+1"),
 Q("<b>Case study:</b> In a grid, numbers are written row by row 1–100. (i) Where are multiples of 9 found? (ii) Observe the pattern of digit sums. (iii) Which row has no multiples of 10? (iv) What diagonal pattern?", "(i) On diagonals going down-left (1). (ii) Each sums to 9 or 18 (1). (iii) All rows have one (1). (iv) Differences 9 (2).", "1+1+1+2"),
 Q("(i) Prove that the sum of any 4 consecutive numbers is not divisible by 4. (ii) Test with 3, 4, 5, 6.", "(i) 4n + 6 leaves remainder 2 (3). (ii) 18 not divisible by 4 (2).", "3+2"),
 Q("(i) Find 1 + 2 + … + 9 using pairs. (ii) Show 45 is a triangular number. (iii) Find the next triangular number after 45.", "(i) 45 (2). (ii) 9 × 10 ÷ 2 (2). (iii) 55 (1).", "2+2+1"),
 Q("(i) Write 3 palindromic numbers between 100 and 200. (ii) Make one by reverse-and-add on 68. (iii) Explain.", "(i) 101, 111, 121 (2). (ii) 68 + 86 = 154; 154 + 451 = 605; 605 + 506 = 1111 (2). (iii) Repeated steps give palindrome (1).", "2+2+1"),
 Q("<b>Case study:</b> Ravi says the product of any three consecutive numbers is divisible by 6. (i) Test 2, 3, 4. (ii) Test 5, 6, 7. (iii) Explain why. (iv) Is it divisible by 12 always?", "(i) 24 (1). (ii) 210 (1). (iii) One is even and one multiple of 3 (2). (iv) No: 3 × 4 × 5 = 60 yes, 1 × 2 × 3 = 6 no (1).", "1+1+2+1"),
 Q("(i) Find the digit D if 3 × 1D5 is divisible by 9. (ii) Find the number. (iii) Check.", "(i) 3 × (100 + 10D + 5) digit sum: 1 + D + 5 must be a multiple of 3 (2). (ii) D = 0, 3, 6, 9 give multiples of 9 after ×3 (2). (iii) 3 × 105 = 315, digit sum 9 (1).", "2+2+1"),
 Q("(i) Find the sum 1 + 2 + … + 20 by pairing. (ii) Explain pairing.", "(i) 210 (3). (ii) 21 × 10 pairs (2).", "3+2"),
]

D = D[:16]
SETS, POOL = build(A, B, C, D)
