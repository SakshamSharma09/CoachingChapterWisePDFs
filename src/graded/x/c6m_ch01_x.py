"""Class 6 Maths Ch 1 Patterns in Mathematics - extras."""
from common import AR4, Q

AR = [
 AR4(r"In the sequence $3, 7, 11, 15, \dots$ the next term is 19.", "Each term of this sequence is obtained by adding 4 to the term before it.", "a",
     "15 + 4 = 19, and R is the rule of the pattern."),
 AR4("The sum of the first 5 odd numbers is 25.", "25 is a square number.", "b",
     "1+3+5+7+9 = 25, and 25 = 5 x 5 is a square, but R does not explain why the sum is 25."),
 AR4(r"The sum $1+2+3+\dots+10$ is 55.", r"The sum of the first $n$ natural numbers is $n \times n$.", "c",
     r"1+2+...+10 = 10 x 11 / 2 = 55, so A is true. The sum of the first n natural numbers is $\frac{n(n+1)}{2}$, not $n\times n$, so R is false."),
 AR4(r"The sequence $2, 4, 8, 16, \dots$ has a common difference.", "A sequence in which the same number is added every time has a common difference.", "d",
     "The differences are 2, 4, 8, which are not equal, so A is false. R is true."),
 AR4(r"In the Virahanka sequence $1, 2, 3, 5, 8, 13, \dots$ the term after 13 is 21.", "Each term after the first two is the sum of the two terms just before it.", "a",
     "8 + 13 = 21, and R is the rule that builds the sequence."),
 AR4("36 is both a square number and a triangular number.", "A number is a square number if it is a number multiplied by itself.", "b",
     "36 = 6 x 6 and 36 = 1+2+...+8, so A is true. R is true but only explains the square part."),
]

CASE = [
 Q(r"<b>Case study.</b> Ravi makes a row of squares with matchsticks. One square needs 4 sticks, two squares joined side by side need 7 sticks, and three squares need 10 sticks. He keeps adding one square at a time. (i) How many sticks are needed for 4 squares? (ii) How many sticks does each new square add? (iii) How many sticks are needed for 10 squares? (iv) Ravi has exactly 40 sticks. How many squares can he make in a row? Show how you found it.",
   r"(i) 13 sticks (1). (ii) 3 sticks (1). (iii) $4+9\times3=31$ sticks (1). (iv) $40-4=36$ and $36\div3=12$ more squares, so $1+12=13$ squares (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A fruit seller stacks oranges in a triangle. The top row has 1 orange, the second row has 2, the third row has 3, and so on. (i) How many oranges are in a stack of 6 rows? (ii) How many oranges are in a stack of 8 rows? (iii) How many oranges are in the 10th row alone? (iv) The seller has 50 oranges. What is the biggest full triangle he can make, and how many oranges are left over?",
   r"(i) $1+2+3+4+5+6=21$ (1). (ii) $1+2+\dots+8=36$ (1). (iii) 10 oranges (1). (iv) 45 oranges make a full stack of 9 rows ($1+2+\dots+9=45$) (1); $50-45=5$ oranges are left (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Meena is tiling a square floor. A $5\times5$ floor uses 25 tiles. To make a bigger square she adds an L-shaped border of tiles around two sides. (i) How many tiles are in a $5\times5$ square floor? (ii) How many tiles does she add to make it $6\times6$? (iii) Which odd number is this? (iv) Find the sum of the first 9 odd numbers. How many tiles must she add to go from $9\times9$ to $10\times10$?",
   r"(i) 25 tiles (1). (ii) $36-25=11$ tiles (1). (iii) 11 is the 6th odd number (1). (iv) The sum of the first 9 odd numbers is $9\times9=81$ (1); she adds the 10th odd number, 19 tiles ($100-81=19$) (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Number patterns", [r"Sequence: a list of numbers following a rule; the numbers are called terms.",
   r"Common difference: the same number added each time, e.g. $5, 9, 13, 17,\dots$ (add 4).",
   r"Counting numbers: $1,2,3,4,\dots$; odd numbers: $1,3,5,7,\dots$; even numbers: $2,4,6,8,\dots$",
   r"The $n$th odd number $=2n-1$; the $n$th even number $=2n$."]),
 ("Special number families", [r"Square numbers: $1,4,9,16,25,\dots$ ($n\times n$).",
   r"Cube numbers: $1,8,27,64,125,\dots$ ($n\times n\times n$).",
   r"Triangular numbers: $1,3,6,10,15,21,\dots$ (add $1,2,3,4,\dots$ in turn).",
   r"Virahanka (Fibonacci) numbers: $1,2,3,5,8,13,\dots$ (each term = sum of the two before)."]),
 ("Useful results", [r"Sum of the first $n$ odd numbers $=n\times n$.",
   r"Sum of the first $n$ natural numbers $=\dfrac{n(n+1)}{2}$ (the $n$th triangular number).",
   r"Two consecutive triangular numbers add up to a square number, e.g. $6+10=16$.",
   r"Complete graph on $n$ points: number of lines $=\dfrac{n(n-1)}{2}$."]),
 ("Steps to explore a pattern", [r"Write the first few terms; find the difference between neighbours; state the rule; test the rule on the next term."]),
]

MISTAKES = [
 r"Thinking the sum of the first $n$ natural numbers is $n\times n$; that is the sum of the first $n$ <b>odd</b> numbers.",
 r"Guessing a rule from only two terms. Always check the rule on at least three terms.",
 r"Mixing up the $n$th odd number $2n-1$ with the $n$th even number $2n$.",
 r"Treating $2, 4, 8, 16$ as having a common difference; the gaps are $2, 4, 8$, so no constant is added.",
 r"In the Virahanka sequence, adding the wrong two terms (the rule uses the <i>two terms just before</i>).",
]
