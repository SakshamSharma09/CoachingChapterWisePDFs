"""Class 9 Maths Ch 11 World of Algorithms - extras."""
from common import AR4, Q

AR = [
 AR4(r"The greatest common divisor of 48 and 18 is 6.", r"The gcd of two numbers is the largest number that divides both of them.", "a",
     r"$48=6\times8$ and $18=6\times3$, and no larger number divides both; R is the definition of gcd."),
 AR4(r"$29\bmod7=1$.", r"$7\bmod29=7$.", "b",
     r"$29=4\times7+1$, so A is true; $7=0\times29+7$, so R is true; the two statements are unrelated."),
 AR4(r"The gcd of 36 and 60 is 12.", r"The gcd of two numbers is always larger than both numbers.", "c",
     r"$36=12\times3,\ 60=12\times5$, so A is true; R is false because the gcd never exceeds the smaller number."),
 AR4(r"The number 12 has exactly 5 divisors.", r"The divisors of 12 are 1, 2, 3, 4, 6 and 12.", "d",
     r"There are 6 divisors, so A is false; R lists them correctly."),
 AR4(r"In the column addition $478+369$, a carry is generated in the ones column.", r"$8+9=17$, which is greater than 9.", "a",
     r"Digit 7 is written and 1 is carried to the tens column because the column sum exceeds 9."),
 AR4(r"$24\bmod6=0$.", r"$0\bmod6=0$.", "b",
     r"Both are true, but R is about a different number and does not explain A (the reason for A is that 6 divides 24)."),
]

CASE = [
 Q(r"<b>Case study.</b> Ananya adds $586+947$ column by column, starting from the ones column, and records the carry from each column. "
   r"(i) What digit is written and what is carried from the ones column? (ii) What digit is written and what is carried from the tens column? (iii) What digit is written in the hundreds column, and what is the carry? (iv) Write the final sum and the total number of carries produced.",
   r"(i) $6+7=13$: write 3, carry 1 (1). (ii) $8+4+1=13$: write 3, carry 1 (1). (iii) $5+9+1=15$: write 5, carry 1 (1). (iv) The last carry becomes the thousands digit, so the sum is 1533 (1) and 3 carries are produced (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A floor measures 84 cm by 36 cm. Dev wants to cover it exactly with the largest possible square tiles, so he finds gcd$(84, 36)$ using Euclid's subtraction method: repeatedly replace the larger number by the difference until the two numbers are equal. "
   r"(i) What is the pair after the first subtraction? (ii) What is the pair after the second subtraction? (iii) What is the gcd? (iv) State the side of the largest square tile and the number of tiles needed.",
   r"(i) $(84,36)\to(48,36)$ (1). (ii) $(48,36)\to(12,36)$ (1). (iii) $(12,36)\to(12,24)\to(12,12)$, so the gcd is 12 (1). (iv) Side $=12$ cm (1); number of tiles $=\dfrac{84}{12}\times\dfrac{36}{12}=7\times3=21$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Weekdays repeat after every 7 days, so Rohan uses the remainder after division by 7 (the mod operation) to find the day of the week. Number the days Sunday $=0$, Monday $=1$, Tuesday $=2$, Wednesday $=3$, Thursday $=4$, Friday $=5$, Saturday $=6$. "
   r"(i) Find $29\bmod7$. (ii) Find $100\bmod7$. (iii) Today is Monday. What day will it be after 100 days? (iv) Today is Thursday. What day will it be after 45 days?",
   r"(i) $29=4\times7+1$, so 1 (1). (ii) $100=14\times7+2$, so 2 (1). (iii) Monday is 1, and $(1+2)\bmod7=3$, which is Wednesday (1). (iv) $45\bmod7=3$ (1); $(4+3)\bmod7=0$, which is Sunday (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Algorithms", [r"An algorithm is a finite, precise, step-by-step procedure that gives the answer for every valid input and stops.",
   r"Tracing an algorithm means writing the values of the variables after each step in a table."]),
 ("Column addition", [r"Add digits column by column from the right: column sum $=$ digit $+$ digit $+$ carry in.",
   r"Digit written $=$ column sum $\bmod10$; carry out $=$ column sum $\div10$ (quotient).",
   r"A carry occurs when a column sum is 10 or more; the carry out is at most 1 for two numbers."]),
 ("Divisors and gcd", [r"$d$ is a divisor of $n$ if $n\bmod d=0$. Every $n>1$ has divisors 1 and $n$; a prime has exactly 2 divisors.",
   r"gcd$(m, n)$ = the largest number dividing both $m$ and $n$.",
   r"Euclid's subtraction method: replace the larger of the two numbers by the difference of the two; repeat until both are equal; that number is the gcd.",
   r"Example: $(84,36)\to(48,36)\to(12,36)\to(12,24)\to(12,12)$, gcd $=12$.",
   r"gcd is also the side of the largest square tile that covers an $m\times n$ rectangle exactly."]),
 ("Remainder (mod)", [r"$m\bmod n$ is the remainder when $m$ is divided by $n$: $m=qn+r$ with $0\le r<n$.",
   r"$m\bmod n=0$ exactly when $n$ divides $m$.", r"Cyclic patterns (days of the week, clock hours) repeat with period $n$ and are handled by mod $n$."]),
]

MISTAKES = [
 r"Forgetting to add the carry from the previous column in column addition.",
 r"Counting a carry when the column sum is exactly 9 (a carry needs a sum of 10 or more).",
 r"Leaving out the divisors 1 and the number itself when listing divisors, or listing a divisor twice (as in $36=6\times6$).",
 r"In Euclid's subtraction method, subtracting the larger number from the smaller or stopping before the two numbers are equal.",
 r"Reading $m\bmod n$ as the quotient of $m\div n$; it is the remainder, and it is always less than $n$.",
 r"Skipping steps when tracing an algorithm, so that a variable's value is not updated in the table.",
]
