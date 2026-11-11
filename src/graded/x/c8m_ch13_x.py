"""Class 8 Maths Ch 13 Algebra Play - extras."""
from common import AR4, Q

AR = [
 AR4(r"For any whole number $n$, the number $2n$ is even and $2n+1$ is odd.", r"Even numbers are multiples of 2, and odd numbers leave remainder 1 when divided by 2.", "a",
     r"$2n$ is a multiple of 2 and $2n+1=2n+1$ leaves remainder 1; R is the definition behind the expressions."),
 AR4(r"The expression $3x+5$ has the value 17 when $x=4$.", r"Terms with the same variable part are called like terms.", "b",
     r"$3(4)+5=17$ so A is true; R is also true but it does not explain the value."),
 AR4(r"The sum of three consecutive numbers $n$, $n+1$, $n+2$ is $3(n+1)$.", r"The sum of three consecutive numbers is always divisible by 6.", "c",
     r"$n+(n+1)+(n+2)=3n+3=3(n+1)$ so A is true; $2+3+4=9$ is not divisible by 6, so R is false."),
 AR4(r"$3x+4x=7x^2$.", r"Like terms can be added by adding their coefficients.", "d",
     r"$3x+4x=7x$, so A is false; R is the correct rule."),
 AR4(r"The difference of the squares of two consecutive numbers $n+1$ and $n$ is $2n+1$.", r"$a^2-b^2=(a+b)(a-b)$.", "a",
     r"$(n+1)^2-n^2=(2n+1)(1)=2n+1$ by the identity in R."),
 AR4(r"If the digits of a two-digit number are $a$ (tens) and $b$ (units), the number obtained by reversing the digits is $10b+a$.", r"The sum of a two-digit number and its reverse is $11(a+b)$.", "b",
     r"A is true by place value; R is true since $(10a+b)+(10b+a)=11(a+b)$, but R does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Aarav performs a number trick: <i>Think of a number $n$. Multiply it by 6. Add 12. Divide by 3. Subtract twice your original number. The answer is always 4.</i> "
   r"(i) Write the expression after multiplying by 6. (ii) Write it after adding 12. (iii) Write it after dividing by 3. (iv) Complete the algebra to show the answer is always 4 and check with $n=7$.",
   r"(i) $6n$ (1). (ii) $6n+12$ (1). (iii) $\dfrac{6n+12}{3}=2n+4$ (1). (iv) Subtract $2n$: $2n+4-2n=4$, independent of $n$ (1); for $n=7$: $42,54,18,18-14=4$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Ishita arranges matchsticks to make a row of squares: 1 square needs 4 sticks, 2 squares need 7 sticks and 3 squares need 10 sticks, and so on. "
   r"(i) How many sticks are needed for 4 squares? (ii) Write an expression for the number of sticks for $n$ squares. (iii) How many sticks are needed for 20 squares? (iv) How many squares can be made with 100 sticks?",
   r"(i) 13 (1). (ii) $3n+1$ (1). (iii) $3(20)+1=61$ (1). (iv) $3n+1=100$ gives $3n=99$, $n=33$ squares (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A teacher says: Take any two-digit number, add the number formed by reversing its digits, and the sum is always a multiple of 11. Let the tens digit be $a$ and the units digit $b$. "
   r"(i) Write the number in terms of $a$ and $b$. (ii) Write the number formed by reversing the digits. (iii) Find the sum of the two. (iv) Hence show that the sum is a multiple of 11 and find it for 47.",
   r"(i) $10a+b$ (1). (ii) $10b+a$ (1). (iii) $11a+11b=11(a+b)$ (1). (iv) The sum has the factor 11 for every $a,b$ (1); for 47: $47+74=121=11\times11$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Expressions", [
   r"Variable: a letter standing for a number; term: a product of numbers and variables; like terms have the same variable part.",
   r"Add or subtract only like terms: $ax+bx=(a+b)x$.",
   r"Value of an expression: substitute the given value of the variable."]),
 ("Useful expressions", [
   r"Even number: $2n$; odd number: $2n+1$; consecutive numbers: $n,\ n+1,\ n+2$.",
   r"Multiple of $k$: $kn$. Two-digit number with digits $a,b$: $10a+b$; reversed: $10b+a$.",
   r"Three-digit number: $100a+10b+c$."]),
 ("Identities", [
   r"$(a+b)^2=a^2+2ab+b^2$; $(a-b)^2=a^2-2ab+b^2$; $(a+b)(a-b)=a^2-b^2$.",
   r"$(n+1)^2-n^2=2n+1$; $(a+b)^2-(a-b)^2=4ab$."]),
 ("Patterns and number tricks", [
   r"A rule for a pattern (e.g. matchsticks $3n+1$): find the difference between successive terms; it is the coefficient of $n$.",
   r"To prove a trick works for every number, express the steps in a variable and simplify.",
   r"$\overline{ab}+\overline{ba}=11(a+b)$; $\overline{ab}-\overline{ba}=9(a-b)$."]),
]

MISTAKES = [
 r"Adding unlike terms: $3x+4x^2=7x^3$; only like terms are combined, and $3x+4x=7x$ (not $7x^2$).",
 r"Writing the two-digit number as $ab$ (product) instead of $10a+b$.",
 r"Checking a trick or identity with one example only and calling it a proof; use a variable for the general case.",
 r"Sign mistakes when removing brackets: $-(x-3)=-x+3$, not $-x-3$.",
 r"Writing $(a+b)^2=a^2+b^2$ or $(a-b)^2=a^2-b^2$ while simplifying expressions.",
 r"Deriving a pattern rule from the first term only; check that the rule works for every given term (e.g. $3n+1$ for $n=1,2,3$).",
]
