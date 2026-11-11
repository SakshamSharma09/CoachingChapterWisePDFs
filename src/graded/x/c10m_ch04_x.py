"""Class 10 Maths Ch 4 Quadratic Equations - extras (factorisation, quadratic formula, discriminant)."""
from common import AR4, Q

AR = [
 AR4(r"The equation $2x^2-3x+5=0$ has no real roots.", r"If the discriminant $b^2-4ac<0$, a quadratic equation has no real roots.", "a",
     r"$D=9-40=-31<0$, so there are no real roots, as stated in R."),
 AR4(r"The equation $x^2-6x+9=0$ has two equal real roots.", r"A quadratic equation always has two distinct real roots.", "c",
     r"$D=36-36=0$ gives equal roots (3 and 3): A true; R is false."),
 AR4(r"The equation $x^2-4x+5=0$ has real and distinct roots.", r"If $b^2-4ac>0$, the roots of $ax^2+bx+c=0$ are real and distinct.", "d",
     r"$D=16-20=-4<0$, so there are no real roots: A false; R is a true statement."),
 AR4(r"The roots of $x^2-5x+6=0$ are 2 and 3.", r"A quadratic equation has at most two roots.", "b",
     r"$(x-2)(x-3)=0$ gives 2 and 3. Both statements are true, but R does not explain why these particular numbers are roots."),
 AR4(r"$(x+2)^3=x^3-4$ is a quadratic equation.", r"An equation of the form $ax^2+bx+c=0$ with $a\neq0$ is a quadratic equation.", "a",
     r"Expanding: $x^3+6x^2+12x+8=x^3-4\Rightarrow6x^2+12x+12=0$ which is of the form in R."),
 AR4(r"The roots of $2x^2-7x+3=0$ are 3 and $\tfrac12$.", r"The quadratic formula gives the roots as $\dfrac{-b\pm\sqrt{b^2+4ac}}{2a}$.", "c",
     r"$2x^2-7x+3=(2x-1)(x-3)$ so A is true; the formula has $b^2-4ac$, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> A rectangular park has an area of 180 square metres. Its length is 3 m more than its breadth. Let the breadth be x metres. "
   r"(i) Form the quadratic equation in x. (ii) Solve it by factorisation. (iii) Find the length and breadth of the park. (iv) A fence of 3 rounds of wire is put around the park. Find the total length of wire and its cost at ₹ 20 per metre.",
   r"(i) $x(x+3)=180\Rightarrow x^2+3x-180=0$ (1). (ii) $(x+15)(x-12)=0$, so $x=12$ (rejecting $-15$) (1). (iii) Breadth 12 m, length 15 m (1). (iv) Perimeter $=2(15+12)=54$ m; wire $=3\times54=162$ m (1); cost $=162\times20=₹\,3240$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A train travels 360 km at a uniform speed of x km/h. Had the speed been 5 km/h more, it would have taken 1 hour less for the same journey. "
   r"(i) Write the equation for the given condition. (ii) Reduce it to $x^2+5x-1800=0$ and find its discriminant. (iii) Find the original speed of the train. (iv) Find the time taken at the original speed and at the increased speed, and verify the 1-hour difference.",
   r"(i) $\dfrac{360}{x}-\dfrac{360}{x+5}=1$ (1). (ii) $360(x+5)-360x=x(x+5)\Rightarrow x^2+5x-1800=0$; $D=25+7200=7225=85^2$ (1). (iii) $x=\dfrac{-5\pm85}{2}$, so $x=40$ km/h (speed cannot be negative) (1). (iv) Time at 40 km/h $=9$ h (1); at 45 km/h $=8$ h; difference $=1$ h, verified (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Ananya checks the nature of roots of three equations without solving them: $2x^2-6x+3=0$, $3x^2-4\sqrt3\,x+4=0$ and $x^2+2x+5=0$. "
   r"(i) Find the discriminant of the first equation. (ii) What is the nature of the roots of the second equation? (iii) Does the third equation have real roots? Give a reason. (iv) Find the values of k for which $2x^2+kx+3=0$ has equal roots.",
   r"(i) $D=36-24=12$ (1). (ii) $D=48-48=0$, so roots are real and equal (1). (iii) $D=4-20=-16<0$, so no real roots (1). (iv) Equal roots need $D=k^2-4(2)(3)=0$ (1), so $k^2=24$, $k=\pm2\sqrt6$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Standard form", [r"$ax^2+bx+c=0$, where $a,b,c$ are real and $a\neq0$. A root $\alpha$ satisfies $a\alpha^2+b\alpha+c=0$.",
   r"A quadratic equation has at most 2 roots."]),
 ("Solving by factorisation", [r"Split the middle term: find two numbers with product $ac$ and sum $b$; factorise; put each factor equal to zero.",
   r"Example: $x^2-5x+6=(x-2)(x-3)=0\Rightarrow x=2,3$."]),
 ("Quadratic formula", [r"$x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$, valid when $b^2-4ac\ge0$."]),
 ("Discriminant $D=b^2-4ac$", [r"$D>0$: two distinct real roots.",
   r"$D=0$: two equal real roots, $x=-\dfrac{b}{2a}$.",
   r"$D<0$: no real roots."]),
 ("Word problems", [r"Form the equation from the story (area, consecutive integers, speed-distance-time, age, etc.).",
   r"Time $=\dfrac{\text{distance}}{\text{speed}}$; area of rectangle $=l\times b$.",
   r"Reject roots that are negative or otherwise impossible for the situation, and verify the answer."]),
]

MISTAKES = [
 r"Writing the formula as $\dfrac{-b\pm\sqrt{b^2+4ac}}{2a}$ or dividing only part of the numerator by $2a$.",
 r"Forgetting the sign of b: for $x^2-5x+6=0$, $-b=+5$.",
 r"Not shifting everything to one side to get the standard form $ax^2+bx+c=0$ before using $D$ or factorising.",
 r"Cancelling a common factor containing x from both sides, which loses a root (e.g. $x(x-2)=3x$).",
 r"Not rejecting a negative root for length, speed, age or time in word problems.",
 r"Saying $D=0$ means no roots; it means two <i>equal</i> real roots.",
]
