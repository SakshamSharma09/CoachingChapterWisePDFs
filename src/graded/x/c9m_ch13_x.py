"""Class 9 Maths Ch 13 Two Variables, One Line - extras."""
from common import AR4, Q

AR = [
 AR4(r"The pair $(2, 3)$ is a solution of $3x+2y=12$.", r"A pair $(x, y)$ is a solution of an equation if substituting it makes both sides equal.", "a",
     r"$3(2)+2(3)=12$, so the pair satisfies the equation; R is the definition used."),
 AR4(r"A linear equation in two variables has infinitely many solutions.", r"The graph of a linear equation in two variables is a straight line.", "b",
     r"Both are true; R describes the shape of the graph but does not by itself say why there are infinitely many solutions."),
 AR4(r"The line $2x+3y=12$ cuts the x-axis at $(6, 0)$.", r"Every point on the x-axis has x-coordinate 0.", "c",
     r"Putting $y=0$ gives $x=6$, so A is true; R is false because points on the x-axis have y-coordinate 0."),
 AR4(r"The equation $x=5$, considered in two variables, represents a single point on the Cartesian plane.", r"The graph of $x=5$ is a line parallel to the y-axis.", "d",
     r"A is false because $x=5$ gives the line through $(5,0),(5,1),(5,-2),\ldots$; R is true."),
 AR4(r"The slope of the line $3x+y=7$ is $-3$.", r"Writing $3x+y=7$ as $y=-3x+7$ shows that the slope is the coefficient of $x$.", "a",
     r"$y=-3x+7$ has slope $-3$, found as R describes."),
 AR4(r"The line $y=2x$ passes through the origin.", r"The slope of the line $y=2x$ is 2.", "b",
     r"At $x=0$, $y=0$, so A is true; R is true, but the slope does not decide that the line passes through the origin."),
]

CASE = [
 Q(r"<b>Case study.</b> Rahul has Rs 100 to spend at a stationery shop in Delhi. A pen costs Rs 5 and a notebook costs Rs 20. He buys $x$ pens and $y$ notebooks and spends exactly Rs 100. "
   r"(i) Write the linear equation in $x$ and $y$. (ii) Is $(4, 4)$ a solution? (iii) If he buys 2 notebooks, how many pens does he buy? (iv) Find the x-intercept and y-intercept of the line and interpret them.",
   r"(i) $5x+20y=100$ (1). (ii) $5(4)+20(4)=100$, so yes (1). (iii) $5x+40=100\Rightarrow x=12$ pens (1). (iv) x-intercept $=20$ (put $y=0$): 20 pens and no notebook (1); y-intercept $=5$ (put $x=0$): 5 notebooks and no pen (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A gardener lays a water pipe along the line $2x+y=8$ on a grid of the garden (1 unit = 1 m). "
   r"(i) Write the equation in the form $y=mx+c$ and state the slope. (ii) Find the y-intercept. (iii) Find the x-intercept. (iv) Check whether the point $(3, 2)$ lies on the pipe, and find the y-coordinate of the point of the pipe with $x=-1$.",
   r"(i) $y=-2x+8$; slope $=-2$ (1). (ii) $8$, i.e. the point $(0, 8)$ (1). (iii) $2x=8\Rightarrow x=4$, i.e. $(4, 0)$ (1). (iv) $2(3)+2=8$, so $(3, 2)$ lies on it (1); at $x=-1$: $y=8+2=10$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A rectangular field has a perimeter of 30 m. Its length is $l$ m and its breadth is $b$ m. "
   r"(i) Write a linear equation in $l$ and $b$. (ii) Find $b$ when $l=9$. (iii) Is $(10, 6)$ a possible pair of length and breadth? (iv) How many solutions in positive whole numbers are possible, and what are the intercepts of the line?",
   r"(i) $2l+2b=30$, i.e. $l+b=15$ (1). (ii) $b=6$ m (1). (iii) $10+6=16\ne15$, so no (1). (iv) $l=1, 2, \ldots, 14$ gives 14 solutions (1); intercepts $(15, 0)$ and $(0, 15)$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Linear equation in two variables", [r"Standard form: $ax+by=c$ with $a$ and $b$ not both zero.",
   r"A solution is a pair $(x, y)$ that satisfies the equation; there are infinitely many solutions.",
   r"Each solution is a point on the line; every point of the line is a solution."]),
 ("Graph and intercepts", [r"The graph is a straight line; two points are enough to draw it (a third checks it).",
   r"x-intercept: put $y=0$, giving $\left(\dfrac ca, 0\right)$. y-intercept: put $x=0$, giving $\left(0, \dfrac cb\right)$.",
   r"Slope of $ax+by=c$ (with $b\ne0$): $-\dfrac ab$; rewrite as $y=-\dfrac abx+\dfrac cb$."]),
 ("Special lines", [r"$x=k$: vertical line parallel to the y-axis. $y=k$: horizontal line parallel to the x-axis.",
   r"$y=mx$: a line through the origin with slope $m$; $ax+by=0$ also passes through the origin.",
   r"Slope-intercept form: $y=mx+c$ has slope $m$ and y-intercept $c$."]),
 ("Using equations", [r"Translate the situation: total $=$ (rate $\times$ number) $+$ (rate $\times$ number).",
   r"To test a point, substitute: it lies on the line only if both sides are equal."]),
]

MISTAKES = [
 r"Finding the x-intercept by putting $x=0$ (that is the y-intercept); for the x-intercept put $y=0$.",
 r"Writing the slope of $ax+by=c$ as $\dfrac ab$ instead of $-\dfrac ab$.",
 r"Saying a linear equation in two variables has one solution; it has infinitely many.",
 r"Treating $x=5$ as a point; in the plane it is a vertical line.",
 r"Plotting the pair as $(y, x)$ instead of $(x, y)$.",
 r"Making a sign slip while transposing, e.g. $2x+y=8\Rightarrow y=2x+8$ instead of $y=-2x+8$.",
]
