"""Class 7 Maths Ch 6 Number Play - extras."""
from common import AR4, Q

AR = [
 AR4("The sum of two odd numbers is even.", "An odd number is of the form 2n + 1, so the sum of two odd numbers is 2(m + n + 1).", "a",
     "2m + 1 + 2n + 1 = 2(m + n + 1), which is even."),
 AR4("5832 is divisible by 9.", "5832 is an even number.", "b",
     "5 + 8 + 3 + 2 = 18 is divisible by 9, so A is true. R is true but does not explain A."),
 AR4("The sum of a two-digit number and its reverse is divisible by 11.", "(10a + b) + (10b + a) = 10(a + b).", "c",
     "The sum is 11(a + b), so A is true; R is false because the correct result is 11(a + b)."),
 AR4("The product of two odd numbers is even.", "The product of an even number and any whole number is even.", "d",
     "The product of two odd numbers is odd (e.g. 3 x 5 = 15), so A is false. R is true."),
 AR4("7 + 8 + 9 = 24 is divisible by 3.", "The sum of three consecutive numbers equals 3 times the middle number.", "a",
     "24 = 3 x 8."),
 AR4("The hailstone sequence starting from 6 reaches 1.", "Kaprekar's routine on a 4-digit number leads to 6174.", "b",
     "6, 3, 10, 5, 16, 8, 4, 2, 1 reaches 1. Both are true, but they are separate facts."),
]

CASE = [
 Q(r"<b>Case study.</b> Teacher Neha shows how 15 can be written as a sum of consecutive numbers: $15=7+8=4+5+6=1+2+3+4+5$. (i) Which of these sums uses exactly three numbers? (ii) Write 21 as the sum of three consecutive numbers. (iii) Is the sum of three consecutive numbers always divisible by 3? Give the reason. (iv) Write 33 as the sum of three consecutive numbers and also as the sum of two consecutive numbers.",
   r"(i) $4+5+6$ (1). (ii) $6+7+8=21$ (1). (iii) Yes; the sum is $(n-1)+n+(n+1)=3n$ (1). (iv) $10+11+12=33$ (1) and $16+17=33$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Arjun adds a two-digit number to its reverse. For 47 he gets $47+74=121$. (i) Find the sum for 83. (ii) Show that the sum for 47 is divisible by 11. (iii) For a number with digits $a$ and $b$, show that the sum of the number and its reverse equals $11(a+b)$. (iv) Without adding, use the rule to find the sum of 62 and its reverse.",
   r"(i) $83+38=121$ (1). (ii) $121=11\times11$ (1). (iii) $(10a+b)+(10b+a)=11a+11b=11(a+b)$ (1). (iv) $11\times(6+2)=88$ (1); check: $62+26=88$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A ticket has the number 63*8, where * is a missing digit. Rakesh wants the number to be divisible by 3 or 9. (i) What is the sum of the known digits? (ii) For which digits * is the number divisible by 3? (iii) For which digit * is it divisible by 9? (iv) Write the number for part (iii) and verify by finding its quotient when divided by 9.",
   r"(i) $6+3+8=17$ (1). (ii) $17+*$ must be a multiple of 3, so $*=1, 4$ or $7$ (1). (iii) $17+*=18$ gives $*=1$ (1). (iv) The number is 6318 (1); $6318\div9=702$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Odd and even", [r"Even number: $2n$.  Odd number: $2n+1$.",
   r"Even $\pm$ even $=$ even;  odd $\pm$ odd $=$ even;  even $\pm$ odd $=$ odd.",
   r"Even $\times$ any whole number $=$ even;  odd $\times$ odd $=$ odd."]),
 ("Digits and reversals", [r"Two-digit number with digits $a, b$: $10a+b$; its reverse: $10b+a$.",
   r"Sum $=11(a+b)$, so the sum is divisible by 11; difference $=9(a-b)$, divisible by 9.",
   r"Palindrome: reads the same both ways."]),
 ("Divisibility", [r"By 3 (or 9): digit sum divisible by 3 (or 9).  By 2, 5, 10: look at the last digit.",
   r"By 4: last two digits;  by 8: last three digits;  by 11: alternating digit sum."]),
 ("Consecutive numbers", [r"Three consecutive numbers: $(n-1)+n+(n+1)=3n$.  Two consecutive numbers: $n+(n+1)=2n+1$ (odd).",
   r"Sum of the first $n$ odd numbers $=n^2$."]),
 ("Number sequences", [r"Collatz: even $\to n\div2$; odd $\to3n+1$; ends in the loop $4,2,1$.",
   r"Kaprekar routine: (largest arrangement) $-$ (smallest arrangement); 4-digit numbers (not all digits equal) reach $6174$."]),
]

MISTAKES = [
 r"Saying the sum of two odd numbers is odd; it is even.",
 r"Treating the product of two odd numbers as even; it is odd.",
 r"Writing the reverse of $10a+b$ as $10a+b$ again; the reverse is $10b+a$.",
 r"Using the divisibility test for 9 as if it were for 3 (digit sum 12 is divisible by 3 but not 9).",
 r"In Kaprekar's routine, forgetting to keep leading zeros when the smaller arrangement starts with 0.",
]
