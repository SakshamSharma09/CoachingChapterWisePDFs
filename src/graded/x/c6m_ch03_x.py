"""Class 6 Maths Ch 3 Number Play - extras."""
from common import AR4, Q

AR = [
 AR4("The largest number that can be made from the digits 3, 0, 7, 5 (each used once) is 7530.", "To make the largest number, arrange the digits in descending order.", "a",
     "7, 5, 3, 0 in descending order gives 7530."),
 AR4("In the hailstone (Collatz) sequence, the number after 7 is 22.", "If the number is odd, multiply by 3 and add 1; if it is even, divide by 2.", "a",
     "7 is odd: 3 x 7 + 1 = 22."),
 AR4("A Kaprekar step on 5432 gives 5432 - 2345 = 3087.", "A Kaprekar step adds the largest and the smallest arrangements of the digits.", "c",
     "A is true (5432 - 2345 = 3087). A Kaprekar step subtracts the smallest from the largest arrangement, so R is false."),
 AR4("The smallest 3-digit number that can be formed from the digits 4, 0, 6 is 046.", "A 3-digit number cannot have 0 in the hundreds place.", "d",
     "046 is not a 3-digit number; the smallest is 406. So A is false and R is true."),
 AR4("The digit sum of 123 is 6.", "123 is divisible by 3.", "b",
     "1 + 2 + 3 = 6 and 123 = 3 x 41. Both are true, but R does not explain why the digit sum is 6."),
 AR4("In a supercell pyramid with bottom row 3, 5, 2 the top number is 15.", "Each number in a supercell pyramid is the sum of the two numbers just below it.", "a",
     "Middle row: 3+5 = 8 and 5+2 = 7; top: 8+7 = 15."),
]

CASE = [
 Q(r"<b>Case study.</b> Kavya has four digit cards: 5, 0, 8 and 3. She forms 4-digit numbers using every card exactly once. (i) What is the largest number she can form? (ii) What is the smallest 4-digit number she can form? (iii) Find the difference between the largest and the smallest. (iv) Find the smallest odd number she can form and explain why it is the smallest.",
   r"(i) 8530 (1). (ii) 3058 (1). (iii) $8530-3058=5472$ (1). (iv) An odd number must end in 5 or 3. The smallest start is 3 then 0, giving 3058 (even) or 3085; 3085 ends in 5 and is the smallest odd number (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Priya plays the hailstone game. If the number is even she halves it; if it is odd she multiplies it by 3 and adds 1. She stops when she reaches 1. She starts with 6. (i) What number comes after 6? (ii) What number comes after 3? (iii) How many steps does she take to reach 1 from 6? (iv) Write the sequence starting from 5, say how many steps it takes and name the largest number reached.",
   r"(i) 3 (1). (ii) $3\times3+1=10$ (1). (iii) 6, 3, 10, 5, 16, 8, 4, 2, 1 is 8 steps (1). (iv) 5, 16, 8, 4, 2, 1 (1); 5 steps and the largest number is 16 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Arjun plays the reverse-and-add game. He takes a number, adds its reverse, and repeats until he gets a palindrome (a number that reads the same both ways). He starts with 57. (i) What is the reverse of 57? (ii) What is $57+75$? (iii) How many reverse-and-add steps does 57 take to reach a palindrome? (iv) Do the same for 68 and give the palindrome and the number of steps.",
   r"(i) 75 (1). (ii) 132 (1). (iii) $132+231=363$ is a palindrome, so 2 steps (1). (iv) $68+86=154$, $154+451=605$, $605+506=1111$ (1); 3 steps and the palindrome is 1111 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Making numbers from digits", [r"Largest number: arrange the digits in <b>descending</b> order.",
   r"Smallest number: arrange in ascending order, but a non-zero digit must come first (no leading 0).",
   r"Even number: last digit is 0, 2, 4, 6 or 8. Odd number: last digit is 1, 3, 5, 7 or 9.",
   r"Successor $=n+1$; predecessor $=n-1$."]),
 ("Digit games", [r"Palindrome: reads the same forwards and backwards, e.g. $121$, $4334$.",
   r"Reverse-and-add: add a number to its reverse; repeat until a palindrome appears.",
   r"Kaprekar step: (largest arrangement of digits) $-$ (smallest arrangement). For 4-digit numbers, repeating reaches $6174$.",
   r"Digit sum: add all the digits; a number is divisible by 3 (or 9) if its digit sum is."]),
 ("Hailstone (Collatz) sequence", [r"If $n$ is even, next term $=\dfrac n2$.  If $n$ is odd, next term $=3n+1$.",
   r"Example: $6\to3\to10\to5\to16\to8\to4\to2\to1$ (8 steps)."]),
 ("Supercells", [r"Each cell equals the sum of the two cells just below it. Work upward from the bottom row; to find a missing cell, subtract."]),
]

MISTAKES = [
 r"Writing 0 first when forming the smallest number (e.g. 046); the smallest 3-digit number from 4, 0, 6 is 406.",
 r"In a Kaprekar step, subtracting the larger from the smaller or adding the two arrangements.",
 r"Applying the odd rule ($3n+1$) to an even number or halving an odd number in the hailstone game.",
 r"Reversing digits wrongly in reverse-and-add (the reverse of 68 is 86) or stopping one step early.",
 r"Counting the starting number as a step when counting steps to reach 1 or a palindrome.",
]
