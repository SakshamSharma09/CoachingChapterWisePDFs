"""Class 10 Maths Ch 7 Coordinate Geometry - extras (distance, section and mid-point formulae)."""
from common import AR4, Q

AR = [
 AR4(r"The distance of the point $(3,4)$ from the origin is 5 units.", r"The distance of a point $(x,y)$ from the origin is $\sqrt{x^2+y^2}$.", "a",
     r"$\sqrt{9+16}=5$; R is the formula used."),
 AR4(r"The mid-point of the segment joining $(2,-3)$ and $(8,5)$ is $(5,1)$.", r"The mid-point of the segment joining $(x_1,y_1)$ and $(x_2,y_2)$ is $\left(\dfrac{x_1-x_2}{2},\dfrac{y_1-y_2}{2}\right)$.", "c",
     r"$\left(\tfrac{2+8}{2},\tfrac{-3+5}{2}\right)=(5,1)$: A true; the formula uses sums, not differences, so R is false."),
 AR4(r"The point $(0,5)$ lies on the x-axis.", r"The y-coordinate of every point on the x-axis is zero.", "d",
     r"$(0,5)$ has x-coordinate 0 so it is on the y-axis: A false; R is true."),
 AR4(r"The point dividing the segment joining $(1,2)$ and $(4,5)$ internally in the ratio $1:2$ is $(2,3)$.", r"The coordinates of the origin are $(0,0)$.", "b",
     r"$\left(\tfrac{1\cdot4+2\cdot1}{3},\tfrac{1\cdot5+2\cdot2}{3}\right)=(2,3)$ so A is true; R is true but unrelated to the section formula."),
 AR4(r"The triangle with vertices $(0,0)$, $(4,0)$ and $(0,3)$ is right-angled.", r"If the square of the longest side of a triangle equals the sum of the squares of the other two sides, the triangle is right-angled.", "a",
     r"Sides are 4, 3 and $\sqrt{16+9}=5$, and $5^2=4^2+3^2$; R is the converse of the Pythagoras theorem used."),
 AR4(r"The point $(-2,3)$ lies in the second quadrant.", r"In the second quadrant both coordinates are positive.", "c",
     r"x is negative and y is positive in the second quadrant, so A is true and R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> On a town map drawn on a grid (1 unit = 100 m), the school is at $S(2,3)$, the library at $L(8,11)$ and the hospital at $H(2,11)$. "
   r"(i) Find the coordinates of the mid-point of SL. (ii) Find the distance SL in units. (iii) Find the distance LH. (iv) Show that the triangle SHL is right-angled and state the right-angle vertex.",
   r"(i) $\left(\tfrac{2+8}{2},\tfrac{3+11}{2}\right)=(5,7)$ (1). (ii) $SL=\sqrt{6^2+8^2}=10$ units (1). (iii) $LH=\sqrt{(8-2)^2+0}=6$ units (1). (iv) $SH=8$; $SH^2+LH^2=64+36=100=SL^2$, so by the converse of Pythagoras the triangle is right-angled at H (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A straight road runs from town $A(-2,1)$ to town $B(10,13)$. The government places two rest-stops P and Q on the road, with P dividing AB internally in the ratio $1:2$ and Q dividing AB internally in the ratio $2:1$. "
   r"(i) Find the coordinates of P. (ii) Find the coordinates of the mid-point of AB. (iii) Find the coordinates of Q. (iv) Show that P and Q divide AB into three equal parts.",
   r"(i) $P=\left(\tfrac{1(10)+2(-2)}{3},\tfrac{1(13)+2(1)}{3}\right)=(2,5)$ (1). (ii) $(4,7)$ (1). (iii) $Q=\left(\tfrac{2(10)+1(-2)}{3},\tfrac{2(13)+1(1)}{3}\right)=(6,9)$ (1). (iv) $AP=\sqrt{16+16}=4\sqrt2$, $PQ=\sqrt{16+16}=4\sqrt2$, $QB=\sqrt{16+16}=4\sqrt2$; all equal (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Two shops are at $A(2,-5)$ and $B(-2,9)$ on a coordinate map. A lamp-post is to be placed on the x-axis at a point P that is equally far from both shops. "
   r"(i) Write the coordinates of a general point on the x-axis. (ii) Write $PA^2$ and $PB^2$ for $P(x,0)$. (iii) Find the position of P. (iv) Find the distance of P from each shop.",
   r"(i) $(x,0)$ (1). (ii) $PA^2=(x-2)^2+25$, $PB^2=(x+2)^2+81$ (1). (iii) $PA^2=PB^2\Rightarrow-4x+29=4x+85\Rightarrow x=-7$; $P(-7,0)$ (1). (iv) $PA=\sqrt{81+25}=\sqrt{106}$ units; $PB=\sqrt{25+81}=\sqrt{106}$ units (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Cartesian plane", [r"Point $(x,y)$: abscissa x, ordinate y. Quadrants: I $(+,+)$, II $(-,+)$, III $(-,-)$, IV $(+,-)$.",
   r"On the x-axis $y=0$; on the y-axis $x=0$."]),
 ("Distance formula", [r"$PQ=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$.",
   r"Distance from origin: $\sqrt{x^2+y^2}$.",
   r"Collinear points A, B, C: sum of two of AB, BC, CA equals the third."]),
 ("Section formula (internal)", [r"Point dividing $A(x_1,y_1)$, $B(x_2,y_2)$ internally in ratio $m_1:m_2$:",
   r"$\left(\dfrac{m_1x_2+m_2x_1}{m_1+m_2},\ \dfrac{m_1y_2+m_2y_1}{m_1+m_2}\right)$."]),
 ("Mid-point formula", [r"$\left(\dfrac{x_1+x_2}{2},\ \dfrac{y_1+y_2}{2}\right)$ (section formula with $m_1:m_2=1:1$)."]),
 ("Shapes using the distance formula", [r"Isosceles: two equal sides. Equilateral: three equal sides. Right-angled: $a^2+b^2=c^2$.",
   r"Parallelogram: diagonals have the same mid-point. Rectangle: also equal diagonals. Rhombus: all four sides equal. Square: equal sides and equal diagonals.",
   r"Centre of a circle through three points is equidistant from them (set $OA=OB=OC$)."]),
]

MISTAKES = [
 r"Using $(x_1-x_2)$ and $(y_2-y_1)$ inconsistently or forgetting to square a negative difference.",
 r"Leaving the square root out, giving $AB^2$ instead of $AB$.",
 r"In the section formula, swapping the ratio: the multiplier of $x_2$ is $m_1$ (not $m_2$).",
 r"Using the mid-point formula with differences instead of sums.",
 r"Writing a point on the x-axis as $(0,y)$; it is $(x,0)$.",
 r"Declaring a triangle right-angled without checking that the <i>longest</i> side squared equals the sum of the other two.",
]
