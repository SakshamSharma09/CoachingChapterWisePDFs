"""Class 9 Maths Ch 2 Linear Polynomials - extras."""
from common import AR4, Q

AR = [
 AR4(r"The zero of the polynomial $p(x)=3x-12$ is 4.", r"The zero of $ax+b$ ($a\ne0$) is $-\dfrac{b}{a}$.", "a",
     r"$-\dfrac{-12}{3}=4$; R is the general rule that gives it."),
 AR4(r"The graph of $y=2x-6$ cuts the x-axis at $(3, 0)$.", r"The graph of $y=2x-6$ cuts the y-axis at $(0, -6)$.", "b",
     r"Putting $y=0$ gives $x=3$, so A is true; putting $x=0$ gives $y=-6$, so R is true. R gives the other intercept, so it does not explain A."),
 AR4(r"The slope of the line $y=-4x+7$ is $-4$.", r"For the line $y=ax+b$ the slope is $b$.", "c",
     r"The slope is the coefficient of $x$, i.e. $-4$, so A is true; R is false because $b$ is the y-intercept."),
 AR4(r"The expression $x^2-5$ is a linear polynomial.", r"The degree of a linear polynomial is 1.", "d",
     r"$x^2-5$ has degree 2, so A is false; R is true."),
 AR4(r"The nth term of the sequence $5, 8, 11, 14, \ldots$ is $3n+2$.", r"The terms increase by a constant amount 3, so the nth term is a linear polynomial in $n$ with coefficient 3.", "a",
     r"$t_n=3n+2$ gives $5, 8, 11, 14$; the constant difference 3 is the coefficient of $n$."),
 AR4(r"The value of the polynomial $p(x)=5x-2$ at $x=2$ is 8.", r"A linear polynomial has exactly one zero.", "b",
     r"$p(2)=10-2=8$, so A is true; R is true but is not the reason for the value."),
]

CASE = [
 Q(r"<b>Case study.</b> A taxi company in Jaipur charges a fixed amount of Rs 50 plus Rs 12 for every kilometre travelled. The fare for $x$ km is given by a polynomial $C(x)$. "
   r"(i) Write $C(x)$. (ii) Find the fare for a 10 km ride. (iii) For what distance is the fare Rs 230? (iv) State the slope and the y-intercept of the graph of $y=C(x)$ and say what each means.",
   r"(i) $C(x)=12x+50$ (1). (ii) $C(10)=120+50=$ Rs 170 (1). (iii) $12x+50=230\Rightarrow x=15$ km (1). (iv) Slope $=12$: the rate of Rs 12 per km (1); y-intercept $=50$: the fixed charge of Rs 50 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Seema saves money in her piggy bank every week: Rs 7 in week 1, Rs 12 in week 2, Rs 17 in week 3, Rs 22 in week 4, and so on, the amount increasing by the same sum each week. "
   r"(i) Find the common difference. (ii) Write the amount $t_n$ saved in week $n$ as a polynomial in $n$. (iii) In which week does she save Rs 87? (iv) Can she save exactly Rs 100 in some week? Give a reason.",
   r"(i) $12-7=5$ (1). (ii) $t_n=5n+2$ (1). (iii) $5n+2=87\Rightarrow n=17$ (1). (iv) $5n+2=100\Rightarrow n=\dfrac{98}{5}$, not a whole number (1), so no week gives exactly Rs 100 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A water tank in a school holds 120 cm of water. It is being emptied by a pump so that the height of water after $t$ minutes is $h(t)=120-4t$ centimetres. "
   r"(i) What is the height at the start? (ii) What is the height after 10 minutes? (iii) Find the zero of $h(t)$. (iv) Find the slope and intercepts of the graph of $h=120-4t$ and interpret the slope.",
   r"(i) $h(0)=120$ cm (1). (ii) $h(10)=120-40=80$ cm (1). (iii) $120-4t=0\Rightarrow t=30$ minutes (1). (iv) Slope $=-4$; intercepts $(0,120)$ and $(30,0)$ (1); the height falls by 4 cm every minute (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Linear polynomial", [r"A linear polynomial in $x$ has the form $p(x)=ax+b$ with $a\ne0$; its degree is 1.",
   r"Value of $p(x)$ at $x=k$: replace $x$ by $k$, i.e. $p(k)=ak+b$.",
   r"Zero of $p(x)$: the value $k$ with $p(k)=0$; for $ax+b$ it is $k=-\dfrac{b}{a}$. A linear polynomial has exactly one zero."]),
 ("Graph of $y=ax+b$", [r"The graph is a straight line.", r"Slope $=a$ (the coefficient of $x$): the change in $y$ for a change of 1 in $x$.",
   r"y-intercept $=b$: the line meets the y-axis at $(0, b)$.", r"x-intercept $=-\dfrac{b}{a}$: the line meets the x-axis at $\left(-\dfrac{b}{a}, 0\right)$ (the zero of the polynomial).",
   r"$a>0$: the line rises to the right; $a<0$: it falls."]),
 ("Nth term and real-life rates", [r"If a sequence increases by a constant $d$ each time and starts at $t_1$, then $t_n=dn+(t_1-d)$, a linear polynomial in $n$.",
   r"Total $=$ (rate) $\times$ (quantity) $+$ fixed amount; the rate is the slope and the fixed amount is the y-intercept.",
   r"To find the input for a given output, solve $ax+b=\text{output}$."]),
]

MISTAKES = [
 r"Writing the zero of $ax+b$ as $\dfrac{b}{a}$ instead of $-\dfrac{b}{a}$.",
 r"Taking the slope of $y=ax+b$ to be $b$; the slope is the coefficient $a$ and $b$ is the y-intercept.",
 r"Calling $x^2-5$ or $\dfrac{1}{x}+2$ a linear polynomial; the degree must be exactly 1.",
 r"Finding the x-intercept by putting $x=0$ (that gives the y-intercept); for the x-intercept put $y=0$.",
 r"In the nth term of a sequence, writing $t_n=dn+t_1$ instead of $dn+(t_1-d)$, so that $t_1$ does not match.",
 r"Reading the fixed charge as the slope, and the per-unit rate as the intercept, in word problems.",
]
