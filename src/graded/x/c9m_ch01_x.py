"""Class 9 Maths Ch 1 Coordinates - extras."""
from common import AR4, Q

AR = [
 AR4(r"The point $(-3, 4)$ lies in Quadrant II.", r"In Quadrant II the abscissa is negative and the ordinate is positive.", "a",
     r"$x=-3<0$ and $y=4>0$, which is exactly the sign pattern of Quadrant II."),
 AR4(r"The point $(0, -6)$ lies on the y-axis.", r"Every point on the x-axis has ordinate 0.", "b",
     r"A point with abscissa 0 is on the y-axis, so A is true; R is also true but is a statement about the x-axis, so it does not explain A."),
 AR4(r"The point $(4, -2)$ lies in Quadrant IV.", r"In Quadrant IV both the abscissa and the ordinate are negative.", "c",
     r"$x>0,\ y<0$ gives Quadrant IV, so A is true. In Quadrant IV the abscissa is positive, so R is false."),
 AR4(r"The points $(2, 3)$ and $(3, 2)$ represent the same point on the Cartesian plane.", r"The order of the numbers in an ordered pair matters.", "d",
     r"$(2,3)$ and $(3,2)$ are different points, so A is false; R is true."),
 AR4(r"The reflection of the point $(3, -5)$ in the x-axis is $(3, 5)$.", r"The reflection of a point in the x-axis keeps its abscissa and changes the sign of its ordinate.", "a",
     r"Reflection in the x-axis: $(x, y)\to(x, -y)$, which gives $(3, 5)$."),
 AR4(r"The distance between the points $(1, 2)$ and $(4, 6)$ is 5 units.", r"The distance between two points on the plane is never negative.", "b",
     r"$\sqrt{3^2+4^2}=5$, so A is true; R is true but does not give the value 5."),
]

CASE = [
 Q(r"<b>Case study.</b> On the map of a town drawn on a grid (1 unit = 1 km), Kavya's school is at A$(-3, 4)$, a park is at B$(-3, -2)$ and the market is at C$(5, -2)$. "
   r"(i) In which quadrant does the school lie? (ii) Write the coordinates of the reflection of the school in the x-axis. (iii) Find the distance between the school and the park. (iv) A bus stop is to be placed midway between the school A and the market C. Find its coordinates and the distance AC.",
   r"(i) $x<0,\ y>0$, so Quadrant II (1). (ii) $(-3, -4)$ (1). (iii) Same abscissa, so $AB=|4-(-2)|=6$ km (1). (iv) Midpoint $=\left(\dfrac{-3+5}{2},\dfrac{4-2}{2}\right)=(1,1)$ (1); $AC=\sqrt{8^2+6^2}=10$ km (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In a treasure-hunt game on a coordinate grid, Imran buries a flag at F$(4, -3)$. His friend Tanvir must find the flag using reflections of this point. "
   r"(i) In which quadrant is the flag? (ii) Find the reflection of F in the y-axis. (iii) Find the reflection of F in the x-axis. (iv) Find the point F$'$ obtained by reflecting F in both axes, and the distance FF$'$.",
   r"(i) $x>0,\ y<0$, so Quadrant IV (1). (ii) $(-4, -3)$ (1). (iii) $(4, 3)$ (1). (iv) $F'=(-4, 3)$ (1); $FF'=\sqrt{8^2+6^2}=10$ units (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A rectangular garden is drawn on a coordinate plane (1 unit = 1 m) with corners P$(0, 0)$, Q$(8, 0)$, R$(8, 6)$ and S$(0, 6)$. A sprinkler is to be fixed at the midpoint of the diagonal PR. "
   r"(i) Find the length of PQ. (ii) Find the coordinates of the midpoint of PR. (iii) Find the length of the diagonal PR. (iv) Show that the diagonal QS has the same length and the same midpoint as PR.",
   r"(i) $PQ=8$ m (1). (ii) $\left(\dfrac{0+8}{2},\dfrac{0+6}{2}\right)=(4,3)$ (1). (iii) $PR=\sqrt{8^2+6^2}=10$ m (1). (iv) $QS=\sqrt{(0-8)^2+(6-0)^2}=10$ m, equal to $PR$ (1); midpoint of $QS=\left(\dfrac{8+0}{2},\dfrac{0+6}{2}\right)=(4,3)$, the same point (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Cartesian plane", [r"Two perpendicular number lines meet at the origin $O(0,0)$: the horizontal x-axis and the vertical y-axis.",
   r"A point is written as an ordered pair $(x, y)$: $x$ is the abscissa (distance along the x-axis) and $y$ is the ordinate.",
   r"Point on the x-axis: $(x, 0)$. Point on the y-axis: $(0, y)$. Axis points lie in no quadrant."]),
 ("Quadrants", [r"Quadrant I: $(+,+)$. Quadrant II: $(-,+)$. Quadrant III: $(-,-)$. Quadrant IV: $(+,-)$.",
   r"Quadrants are numbered anticlockwise starting from the top right."]),
 ("Reflections", [r"In the x-axis: $(x, y)\to(x, -y)$.", r"In the y-axis: $(x, y)\to(-x, y)$.",
   r"In both axes (through the origin): $(x, y)\to(-x, -y)$."]),
 ("Distance and midpoint", [r"Distance between $A(x_1, y_1)$ and $B(x_2, y_2)$: $AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$.",
   r"Distance of $(x, y)$ from the origin: $\sqrt{x^2+y^2}$.",
   r"Points with the same $y$: distance $=|x_2-x_1|$. Points with the same $x$: distance $=|y_2-y_1|$.",
   r"Midpoint of $AB$: $\left(\dfrac{x_1+x_2}{2},\ \dfrac{y_1+y_2}{2}\right)$."]),
]

MISTAKES = [
 r"Writing the point as $(y, x)$: the abscissa $x$ always comes first, so $(2,3)\ne(3,2)$.",
 r"Mixing up the signs of the quadrants, e.g. placing $(-3, 4)$ in Quadrant IV; Quadrant II is $(-,+)$.",
 r"Reflecting in the x-axis but changing the sign of the abscissa (that is a reflection in the y-axis).",
 r"Saying that $(0, -6)$ or $(5, 0)$ lies in a quadrant; points on the axes belong to no quadrant.",
 r"In the distance formula, forgetting the square root or adding the coordinates instead of subtracting them.",
 r"In the midpoint formula, dividing only one coordinate by 2, or subtracting instead of adding.",
]
