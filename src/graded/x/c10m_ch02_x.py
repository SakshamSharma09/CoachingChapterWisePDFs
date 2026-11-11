"""Class 10 Maths Ch 2 Polynomials - extras (zeros, graphs, relation between zeros and coefficients of quadratics)."""
from common import AR4, Q

AR = [
 AR4(r"A quadratic polynomial whose graph is a parabola cutting the x-axis at two distinct points has two real zeros.", r"The zeros of a polynomial $p(x)$ are the x-coordinates of the points where the graph of $y=p(x)$ meets the x-axis.", "a",
     r"Each point where the graph meets the x-axis has $y=0$, i.e. $p(x)=0$; so R explains A."),
 AR4(r"The sum of the zeros of $2x^2-8x+6$ is 4.", r"For $ax^2+bx+c$ with zeros $\alpha,\beta$, the sum of the zeros is $\dfrac{c}{a}$.", "c",
     r"Sum $=-\dfrac{b}{a}=\dfrac{8}{2}=4$, so A is true; R is false because $\dfrac ca$ is the product."),
 AR4(r"The polynomial $x^2+1$ has two real zeros.", r"A quadratic polynomial can have at most two zeros.", "d",
     r"$x^2+1\ge1>0$, so its graph never meets the x-axis and it has no real zero: A is false; R is true."),
 AR4(r"The degree of the polynomial $5x^3-x+7$ is 3.", r"Every linear polynomial has exactly one zero.", "b",
     r"Both statements are true, but the degree is the highest power of x, which has nothing to do with R."),
 AR4(r"The polynomial $x^2-x-6$ has zeros 3 and $-2$.", r"A quadratic polynomial with sum of zeros S and product of zeros P is $k\,(x^2-Sx+P)$, $k\neq0$.", "a",
     r"$S=3+(-2)=1$, $P=-6$, so the polynomial is $x^2-x-6$; R is the rule used."),
 AR4(r"The graph of $y=x^2-4x+4$ touches the x-axis at exactly one point.", r"Every quadratic polynomial has two distinct real zeros.", "c",
     r"$x^2-4x+4=(x-2)^2$ has the single (repeated) zero 2, so A is true; R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> Meera is designing a parabola-shaped flower bed in her school garden. She models its boundary by the graph of $y=p(x)=x^2-8x+15$, where x is measured in metres along the ground. "
   r"(i) Find the zeros of $p(x)$. (ii) Find the sum and the product of the zeros. (iii) How many times does the graph of $y=p(x)$ meet the x-axis, and at which points? (iv) Form a quadratic polynomial whose zeros are the reciprocals of the zeros of $p(x)$.",
   r"(i) $x^2-8x+15=(x-3)(x-5)$, so zeros are 3 and 5 (1). (ii) Sum $=8$, product $=15$ (1). (iii) Twice, at $(3,0)$ and $(5,0)$ (1). (iv) Reciprocal zeros $\tfrac13,\tfrac15$: sum $=\tfrac{8}{15}$, product $=\tfrac1{15}$, polynomial $x^2-\tfrac{8}{15}x+\tfrac1{15}$, i.e. $15x^2-8x+1$ (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Sunita's rectangular vegetable plot has length and breadth (in metres) that are the zeros of the polynomial $x^2-30x+216$. "
   r"(i) Find the sum of the length and breadth. (ii) Find the length and the breadth by factorising. (iii) Without finding the zeros, state the area of the plot. (iv) Find the perimeter of the plot and the cost of fencing it at ₹ 50 per metre.",
   r"(i) Sum of zeros $=30$ m (1). (ii) $x^2-30x+216=(x-12)(x-18)$, so breadth 12 m and length 18 m (1). (iii) Area $=$ product of zeros $=216\ \text{m}^2$ (1). (iv) Perimeter $=2(18+12)=60$ m (1); cost $=60\times50=₹\,3000$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Three students sketch graphs of polynomials. Arjun's parabola opens upwards and just touches the x-axis at $(2,0)$. Bela's parabola cuts the x-axis at $(-1,0)$ and $(3,0)$ and cuts the y-axis at $(0,-6)$. Chirag's graph is the straight line $y=2x-8$. "
   r"(i) Write the zeros of Bela's polynomial. (ii) How many zeros does Arjun's polynomial have? (iii) Find the zero of Chirag's polynomial. (iv) Find Bela's quadratic polynomial.",
   r"(i) $-1$ and $3$ (1). (ii) One zero, namely 2 (repeated), since the graph touches the x-axis at one point (1). (iii) $2x-8=0\Rightarrow x=4$ (1). (iv) $p(x)=k(x+1)(x-3)=k(x^2-2x-3)$; $p(0)=-3k=-6\Rightarrow k=2$ (1); $p(x)=2x^2-4x-6$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Polynomials and degree", [r"A polynomial $p(x)=a_nx^n+\dots+a_1x+a_0$; degree = highest power of x.",
   r"Linear: $ax+b$ (degree 1). Quadratic: $ax^2+bx+c$, $a\neq0$ (degree 2). Cubic: degree 3."]),
 ("Zeros of a polynomial", [r"A real number k is a zero of $p(x)$ if $p(k)=0$.",
   r"Zeros are the x-coordinates of the points where the graph of $y=p(x)$ meets the x-axis."]),
 ("Zeros and graphs", [r"A linear polynomial has exactly one zero; its graph is a straight line cutting the x-axis once.",
   r"A quadratic polynomial has at most 2 zeros; its graph is a parabola (opening upwards if $a>0$, downwards if $a<0$).",
   r"Parabola cuts the x-axis at two points: 2 zeros. Touches it at one point: 1 (repeated) zero. Does not meet it: no real zero.",
   r"A cubic polynomial has at most 3 zeros."]),
 ("Relationship between zeros and coefficients (quadratic)", [r"If $\alpha,\beta$ are the zeros of $ax^2+bx+c$:",
   r"$\alpha+\beta=-\dfrac{b}{a}$, $\qquad\alpha\beta=\dfrac{c}{a}$.",
   r"Polynomial from zeros: $k\,[x^2-(\alpha+\beta)x+\alpha\beta]$, $k\neq0$.",
   r"Useful: $\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta$, $\ \dfrac1\alpha+\dfrac1\beta=\dfrac{\alpha+\beta}{\alpha\beta}$."]),
]

MISTAKES = [
 r"Writing sum of zeros as $\dfrac ca$ and product as $-\dfrac ba$; it is sum $=-\dfrac ba$ and product $=\dfrac ca$.",
 r"Forgetting the sign: for $x^2-8x+15$ the sum of zeros is $+8$, not $-8$.",
 r"Counting the zeros of $y=p(x)$ as the y-intercept; zeros are where the graph meets the <i>x</i>-axis.",
 r"Counting a parabola that only touches the x-axis as having no zeros or two different zeros; it has one repeated zero.",
 r"Writing the polynomial from its zeros as $x^2+(\alpha+\beta)x+\alpha\beta$ instead of $x^2-(\alpha+\beta)x+\alpha\beta$.",
 r"Claiming a quadratic polynomial always has two real zeros (e.g. $x^2+1$ has none).",
]
