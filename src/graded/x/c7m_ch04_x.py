"""Class 7 Maths Ch 4 Expressions using Letter-Numbers - extras."""
from common import AR4, Q

AR = [
 AR4("'Five more than three times n' is written as 3n + 5.", "Three times n is written as 3n.", "a",
     "Three times n is 3n, and five more is 3n + 5."),
 AR4("The value of 2x + 3 when x = 4 is 11.", "In 2x, the number 2 and the letter x are multiplied.", "b",
     "2 x 4 + 3 = 11. Both are true, but R does not explain the value."),
 AR4("3a + 2a = 5a.", r"3a + 2a = 5a$^2$.", "c",
     "Like terms are added by adding their numbers: 5a. The letter part does not change, so R is false."),
 AR4("4x + 3y = 7xy.", "Only like terms can be added to give a single term.", "d",
     "4x and 3y are unlike terms and cannot be combined, so A is false. R is true."),
 AR4("The perimeter of a square of side s is 4s.", "The perimeter is the sum of all four equal sides, s + s + s + s.", "a",
     "Adding four equal sides gives 4s."),
 AR4("The expression 7n has the value 35 when n = 5.", "A letter-number can take different values in different situations.", "b",
     "7 x 5 = 35. Both true, but R does not explain the calculation."),
]

CASE = [
 Q(r"<b>Case study.</b> Sunita makes a row of triangles with matchsticks. One triangle needs 3 sticks, two triangles joined in a row need 5 sticks, and three triangles need 7 sticks. (i) How many sticks are needed for 5 triangles? (ii) Write an expression for the sticks for $n$ triangles. (iii) Find the sticks for 10 triangles. (iv) She has 41 sticks. How many triangles can she make?",
   r"(i) $2\times5+1=11$ sticks (1). (ii) $2n+1$ (1). (iii) $2\times10+1=21$ sticks (1). (iv) $2n+1=41$ gives $2n=40$, so $n=20$ triangles (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A taxi in Jaipur charges ₹30 as the fixed charge and ₹12 for each kilometre. (i) What is the fare for 5 km? (ii) Write an expression for the fare for $k$ km. (iii) Find the fare for 10 km. (iv) A passenger paid ₹138. How many kilometres did he travel? Show your working.",
   r"(i) $30+12\times5=₹90$ (1). (ii) $12k+30$ (1). (iii) $12\times10+30=₹150$ (1). (iv) $12k+30=138$ gives $12k=108$, so $k=9$ km (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Rohan is $r$ years old. His mother's age is 2 more than 3 times his age. His father is 6 years older than his mother. (i) Write an expression for the mother's age. (ii) Find the mother's age when $r=12$. (iii) Write an expression for the father's age. (iv) Write and simplify an expression for the sum of the ages of Rohan, his mother and his father. Find its value when $r=12$.",
   r"(i) $3r+2$ (1). (ii) $3\times12+2=38$ years (1). (iii) $3r+2+6=3r+8$ (1). (iv) $r+(3r+2)+(3r+8)=7r+10$ (1); for $r=12$: $7\times12+10=94$ years (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Letter-numbers and expressions", [r"A letter stands for a number that can change (variable). $3n$ means $3\times n$; $n\times n=n^2$.",
   r"Term: a part of an expression joined by $+$ or $-$. Expression: terms combined, e.g. $3n+5$.",
   r"Like terms have the same letter part ($4x$ and $9x$); unlike terms have different letter parts ($4x$ and $3y$)."]),
 ("Forming expressions", [r"'$n$ more than $a$' $\to a+n$;  '$n$ less than $a$' $\to a-n$;  '$k$ times $x$' $\to kx$.",
   r"Perimeter of a square $=4s$; of a rectangle $=2(l+b)$. Area of a rectangle $=lb$.",
   r"Cost of $n$ items at ₹$p$ each $=np$.  Fixed charge $+$ rate $\times$ units: $a+bn$."]),
 ("Evaluating", [r"Substitute the number for the letter and follow BODMAS: if $x=4$, then $2x+3=2\times4+3=11$."]),
 ("Adding and subtracting", [r"Add or subtract only like terms: $3a+2a=5a$;  $7x-4x=3x$.",
   r"$4x+3y$ cannot be simplified further.",
   r"Subtracting: change the sign of every term being subtracted: $(5x+3)-(2x-4)=3x+7$.",
   r"Brackets with a minus sign in front: $-(a-b)=-a+b$."]),
 ("Patterns", [r"A rule such as $2n+1$ gives the $n$th term; find $n$ for a given term by solving, e.g. $2n+1=41\Rightarrow n=20$."]),
]

MISTAKES = [
 r"Adding unlike terms: $4x+3y=7xy$ is wrong.",
 r"Writing $3a+2a=5a^2$; the letter part does not change when like terms are added.",
 r"Writing $3n$ as '3 plus n'; it means 3 times $n$.",
 r"Not changing all signs when subtracting an expression in brackets: $(5x+3)-(2x-4)\ne3x-1$.",
 r"Confusing 'n less than a' ($a-n$) with $n-a$.",
]
