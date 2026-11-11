"""Class 10 Maths Ch 3 Pair of Linear Equations in Two Variables - extras."""
from common import AR4, Q

AR = [
 AR4(r"The graphs of $x+y=4$ and $x-y=2$ intersect at the point $(3,1)$.", r"The coordinates of the point of intersection of the lines of a pair of linear equations give the solution of the pair.", "a",
     r"$3+1=4$ and $3-1=2$; the common point satisfies both equations, which is exactly the solution (R)."),
 AR4(r"The pair $x+2y=4$, $2x+4y=12$ has no solution.", r"Two lines with $\dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}$ always intersect at exactly one point.", "c",
     r"$\tfrac12=\tfrac24\neq\tfrac4{12}$, so the lines are parallel and there is no solution: A true; R is false."),
 AR4(r"The lines $3x+2y=5$ and $2x-3y=7$ are parallel.", r"A pair of linear equations is consistent if its lines intersect or coincide.", "d",
     r"$\tfrac32\neq\tfrac{2}{-3}$, so the lines intersect (not parallel): A false; R is true."),
 AR4(r"$x=3,\ y=2$ is the solution of $x+y=5$ and $x-y=1$.", r"A consistent pair of linear equations has at least one solution.", "b",
     r"$3+2=5$ and $3-2=1$, so A is true; R is also true but it does not verify A."),
 AR4(r"The pair $kx+3y=3$ and $12x+ky=6$ has no solution when $k=-6$.", r"A pair has no solution when $\dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}\neq\dfrac{c_1}{c_2}$.", "a",
     r"For $k=-6$: $\tfrac{-6}{12}=\tfrac3{-6}=-\tfrac12$ but $\tfrac{3}{6}=\tfrac12$; this is exactly the condition in R."),
 AR4(r"If $2x+y=5$ and $4x+2y=k$ have infinitely many solutions, then $k=10$.", r"A pair of linear equations in two variables can have exactly two solutions.", "c",
     r"Need $\tfrac24=\tfrac12=\tfrac5k\Rightarrow k=10$: A true. R is false: a pair has 0, 1 or infinitely many solutions."),
]

CASE = [
 Q(r"<b>Case study.</b> Rohan buys 3 notebooks and 2 pens for ₹ 70, while Priya buys 2 notebooks and 3 pens for ₹ 65 from the same shop. Let the price of a notebook be ₹ n and of a pen be ₹ p. "
   r"(i) Write the pair of linear equations. (ii) Solve by elimination to find the price of a notebook. (iii) Find the price of a pen. (iv) Aman has ₹ 200. He buys 6 notebooks and spends the rest on as many pens as possible. How many pens does he buy and how much money is left?",
   r"(i) $3n+2p=70$ and $2n+3p=65$ (1). (ii) Multiply by 3 and 2: $9n+6p=210$, $4n+6p=130$; subtract: $5n=80$, so $n=₹\,16$ (1). (iii) $3(16)+2p=70\Rightarrow p=₹\,11$ (1). (iv) 6 notebooks cost ₹ 96; remaining ₹ 104; $104\div11=9$ remainder 5, so 9 pens (1) and ₹ 5 left (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A town planner models pairs of roads by linear equations. Pair A: $2x+3y=12$ and $4x+6y=24$. Pair B: $x+y=5$ and $2x+2y=7$. Pair C: $x-y=1$ and $x+y=7$. "
   r"(i) What is the geometrical relation between the roads of Pair A? (ii) Do the roads of Pair B ever meet? (iii) Find the junction where the roads of Pair C meet. (iv) For what value of k are the roads $kx+3y=12$ and $4x+6y=24$ coincident? For which values of k do they meet at exactly one point?",
   r"(i) $\tfrac24=\tfrac36=\tfrac{12}{24}$: the roads coincide (1). (ii) $\tfrac12=\tfrac12\neq\tfrac57$: parallel, never meet (1). (iii) Adding: $2x=8$, $x=4$, $y=3$; junction $(4,3)$ (1). (iv) Coincident when $\tfrac k4=\tfrac36$, so $k=2$ (1); for $k\neq2$ the ratios $\tfrac k4\neq\tfrac36$ and they meet at exactly one point (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Kavita thinks of a two-digit number. The sum of its digits is 9, and the number exceeds the number obtained by reversing its digits by 27. Let the tens digit be x and the units digit be y. "
   r"(i) Write the equation for the sum of digits. (ii) Write and simplify the equation for the difference. (iii) Find the number. (iv) Show that no two-digit number has digit sum 9 and exceeds its reversal by 36.",
   r"(i) $x+y=9$ (1). (ii) $(10x+y)-(10y+x)=27\Rightarrow 9(x-y)=27\Rightarrow x-y=3$ (1). (iii) Adding: $2x=12$, $x=6$, $y=3$; the number is 63 (1). (iv) $9(x-y)=36\Rightarrow x-y=4$; with $x+y=9$ we get $x=6.5$, not a digit, so no such number exists (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Standard form and solutions", [r"$a_1x+b_1y+c_1=0,\quad a_2x+b_2y+c_2=0$ with $a_i^2+b_i^2\neq0$.",
   r"A solution is a pair $(x,y)$ satisfying both equations; geometrically, a common point of the two lines."]),
 ("Nature of solutions (graphical view)", [r"$\dfrac{a_1}{a_2}\neq\dfrac{b_1}{b_2}$: lines intersect at one point; unique solution; <b>consistent</b>.",
   r"$\dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}=\dfrac{c_1}{c_2}$: lines coincide; infinitely many solutions; consistent (dependent).",
   r"$\dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}\neq\dfrac{c_1}{c_2}$: lines are parallel; no solution; <b>inconsistent</b>."]),
 ("Graphical method", [r"Draw both lines using a table of 2 or 3 points each; read the common point of intersection.",
   r"Check by substituting the point in both equations."]),
 ("Substitution method", [r"Express one variable in terms of the other from one equation, substitute in the other, solve, then back-substitute."]),
 ("Elimination method", [r"Multiply the equations by suitable numbers to make the coefficients of one variable equal in magnitude; add or subtract to eliminate it.",
   r"Solve for the remaining variable, then substitute back.",
   r"A false statement such as $0=5$ means no solution; a true statement such as $0=0$ means infinitely many solutions."]),
 ("Word problems", [r"Define two variables, translate two conditions into two equations, solve, and check against the original statement.",
   r"Two-digit number: $10x+y$; reversed: $10y+x$."]),
]

MISTAKES = [
 r"Applying the ratio test with the wrong pairing, e.g. comparing $\dfrac{a_1}{b_2}$ instead of $\dfrac{a_1}{a_2}$.",
 r"Saying a pair with $\dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}$ always has no solution; check $\dfrac{c_1}{c_2}$ to separate coincident lines from parallel lines.",
 r"Subtracting only some terms in elimination, or forgetting to multiply the right-hand side as well as the left.",
 r"Reading the result $0=0$ as 'no solution'; it signals infinitely many solutions, while $0=5$ signals none.",
 r"Not substituting back to find the second variable, or stating only x when the question asks for both.",
 r"Writing the reversed number as $10x+y$ again instead of $10y+x$ in digit problems.",
]
