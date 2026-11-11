"""Class 7 Maths Ch 2 Arithmetic Expressions - extras."""
from common import AR4, Q

AR = [
 AR4(r"$5+3\times4=17$.", "In an expression without brackets, multiplication is done before addition.", "a",
     "3 x 4 = 12 and 5 + 12 = 17."),
 AR4(r"$(3+4)\times2=14$.", r"$3+4\times2=11$.", "b",
     "Both are true, but R does not explain A."),
 AR4(r"$20-8-4=8$.", r"$20-(8-4)$ has the same value as $(20-8)-4$.", "c",
     "(20 - 8) - 4 = 8, so A is true. 20 - (8 - 4) = 16, so R is false."),
 AR4(r"$12\div3\times2=2$.", "Multiplication and division are done from left to right.", "d",
     "12 / 3 x 2 = 4 x 2 = 8, so A is false. R is true."),
 AR4(r"$8\times99=792$.", r"$99=100-1$, so $8\times99=8\times100-8\times1$.", "a",
     "800 - 8 = 792, using the distributive property."),
 AR4(r"$6+2\times(9-4)=16$.", "The brackets are worked out first.", "a",
     "9 - 4 = 5, 2 x 5 = 10 and 6 + 10 = 16."),
]

CASE = [
 Q(r"<b>Case study.</b> Ramesh buys 3 notebooks at ₹25 each and 2 pens at ₹10 each. He pays with a ₹100 note. (i) Write one expression for the total cost. (ii) Find its value. (iii) How much change does he get? (iv) Next day he buys 5 notebooks and 2 pens and pays with ₹200. Write an expression for the cost and find the change.",
   r"(i) $3\times25+2\times10$ (1). (ii) $75+20=95$ (1). (iii) $100-95=₹5$ (1). (iv) Cost $=5\times25+2\times10=125+20=145$ (1); change $=200-145=₹55$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A hall has 12 rows of seats. In each row, 18 seats are in the left block and 12 seats are in the right block. (i) Write an expression for the total number of seats using brackets. (ii) Find its value. (iii) Write the same total without brackets using the distributive property and check it. (iv) Use the distributive property to find $12\times98$.",
   r"(i) $12\times(18+12)$ (1). (ii) $12\times30=360$ (1). (iii) $12\times18+12\times12=216+144=360$ (1). (iv) $12\times98=12\times(100-2)=1200-24=1176$ (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A teacher gives the expression $8+4\times3-2$ and asks students to place brackets to change its value. (i) Find the value without brackets. (ii) Find the value of $(8+4)\times3-2$. (iii) Find the value of $8+4\times(3-2)$. (iv) Which of the three has the greatest value and how much more is it than the value without brackets?",
   r"(i) $8+12-2=18$ (1). (ii) $12\times3-2=34$ (1). (iii) $8+4\times1=12$ (1). (iv) $(8+4)\times3-2=34$ is the greatest (1); $34-18=16$ more (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Order of operations (BODMAS)", [r"Brackets first, then multiplication and division (left to right), then addition and subtraction (left to right).",
   r"Example: $6+2\times(9-4)=6+2\times5=16$.   $12\div3\times2=4\times2=8$."]),
 ("Properties", [r"Commutative: $a+b=b+a$, $a\times b=b\times a$ (not true for subtraction and division).",
   r"Associative: $(a+b)+c=a+(b+c)$; $(a\times b)\times c=a\times(b\times c)$.",
   r"Distributive: $a\times(b+c)=a\times b+a\times c$ and $a\times(b-c)=a\times b-a\times c$.",
   r"Subtraction: $a-(b-c)\ne(a-b)-c$ in general."]),
 ("Quick calculations", [r"$a\times99=a\times100-a$,  $a\times101=a\times100+a$,  $a\times9=a\times10-a$."]),
 ("Forming expressions", [r"'Sum of $a$ and $b$' $\to a+b$; 'product' $\to a\times b$; 'difference' $\to a-b$; 'increased by' $\to +$; 'decreased by' $\to -$.",
   r"Two expressions are equal if they have the same value; check by evaluating both."]),
]

MISTAKES = [
 r"Working strictly left to right, e.g. $5+3\times4=32$; multiplication comes first.",
 r"Doing $12\div3\times2$ as $12\div6$; division and multiplication are done left to right.",
 r"Treating subtraction as associative: $20-(8-4)\ne20-8-4$.",
 r"Using the distributive property wrongly: $a\times(b+c)\ne a\times b+c$.",
 r"Forgetting to evaluate the bracket first, e.g. taking $2\times(9-4)$ as $18-4$.",
]
