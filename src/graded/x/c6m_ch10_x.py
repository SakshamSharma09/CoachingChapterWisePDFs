"""Class 6 Maths Ch 10 The Other Side of Zero - extras."""
from common import AR4, Q

AR = [
 AR4(r"$-7<-3$.", "On a number line, a number lying to the left of another number is smaller.", "a",
     "-7 lies to the left of -3."),
 AR4("The sum of 5 and -5 is 0.", "Zero is neither positive nor negative.", "b",
     "Both are true, but R does not explain why 5 + (-5) = 0."),
 AR4(r"$-4+6=2$.", "Subtracting a negative integer is the same as subtracting the corresponding positive integer.", "c",
     "-4 + 6 = 2 is true. Subtracting -3 is the same as adding 3, so R is false."),
 AR4("The successor of -1 is -2.", "The successor of an integer is obtained by adding 1 to it.", "d",
     "-1 + 1 = 0, so the successor of -1 is 0 and A is false. R is true."),
 AR4(r"The temperature falls from $3^\circ$C to $-4^\circ$C. The fall is $7^\circ$C.", r"The fall is $3-(-4)=3+4=7$.", "a",
     "The difference between the readings gives the fall."),
 AR4("The sum of two negative integers is a negative integer.", "Every positive integer is greater than every negative integer.", "b",
     "Both are true, but R does not explain why the sum is negative."),
]

CASE = [
 Q(r"<b>Case study.</b> The minimum temperatures (in $^\circ$C) in Shimla on four days were: Monday $-2$, Tuesday $-5$, Wednesday $1$, Thursday $-3$. (i) Which day was the coldest? (ii) By how many degrees did the temperature rise from Tuesday to Wednesday? (iii) Which was warmer, Monday or Thursday, and by how much? (iv) Find the sum of the four temperatures.",
   r"(i) Tuesday ($-5^\circ$C) (1). (ii) $1-(-5)=6^\circ$C (1). (iii) Monday, by $-2-(-3)=1^\circ$C (1). (iv) $-2+(-5)+1+(-3)=-9$ (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A mall has floors below the ground (basements) numbered $-1, -2, \dots$ and floors above the ground numbered $1, 2, \dots$. A lift starts at the ground floor (0), goes down 3 floors, then up 5 floors, then down 4 floors. (i) On which floor is the lift after the first move? (ii) On which floor after the second move? (iii) On which floor does it finish? (iv) How many floors did the lift travel in all? Say which basement it finishes in.",
   r"(i) $-3$ (1). (ii) $-3+5=2$ (1). (iii) $2-4=-2$ (1). (iv) Total travel $=3+5+4=12$ floors (1); it finishes at $-2$, the second basement (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Shopkeeper Mohan writes a profit as a positive number and a loss as a negative number (in ₹): Monday $+250$, Tuesday $-120$, Wednesday $-80$, Thursday $+300$. (i) On which days did he have a loss? (ii) What is the total of the loss days? (iii) What is his overall result for the four days? (iv) On Friday he wants the total for the five days to be 0. What must Friday's amount be? Is it profit or loss?",
   r"(i) Tuesday and Wednesday (1). (ii) $-120+(-80)=-200$, a loss of ₹200 (1). (iii) $250-120-80+300=350$, a profit of ₹350 (1). (iv) $350+x=0$ gives $x=-350$ (1); a loss of ₹350 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Integers and the number line", [r"Integers: $\dots,-3,-2,-1,0,1,2,3,\dots$ Zero is neither positive nor negative.",
   r"On the number line, numbers increase to the right. Every positive integer $>0>$ every negative integer.",
   r"Successor $=n+1$; predecessor $=n-1$. Opposite of $n$ is $-n$, and $n+(-n)=0$."]),
 ("Comparing", [r"Of two negative integers, the one with the smaller absolute value is greater: $-3>-7$.",
   r"Ascending order: smallest to greatest (left to right on the number line)."]),
 ("Addition", [r"Same signs: add the values and keep the sign: $(-4)+(-3)=-7$.",
   r"Different signs: subtract the smaller value from the larger and keep the sign of the larger: $(-4)+6=2$, $(-9)+5=-4$."]),
 ("Subtraction", [r"$a-b=a+(-b)$: subtracting an integer is adding its opposite.",
   r"$a-(-b)=a+b$, e.g. $3-(-4)=7$.   Change (rise or fall) $=$ final $-$ initial."]),
 ("Applications", [r"Temperature below zero, depths below sea level and floors below ground are written with a negative sign.",
   r"Profit $=+$, loss $=-$; overall result $=$ sum of all the amounts."]),
]

MISTAKES = [
 r"Saying $-7>-3$ because 7 is greater than 3; on the number line $-7$ lies to the left of $-3$.",
 r"Writing $-4-(-6)=-10$; the correct value is $-4+6=2$.",
 r"Dropping the sign of the bigger number when adding integers with different signs, e.g. $(-9)+5=4$ instead of $-4$.",
 r"Taking the successor of a negative integer as one smaller (successor of $-1$ is $0$, not $-2$).",
 r"Finding a fall or rise as initial $-$ final in the wrong order; use final $-$ initial and read the sign.",
]
