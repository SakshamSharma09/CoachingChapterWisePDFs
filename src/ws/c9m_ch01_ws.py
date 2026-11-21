"""Class 9 Maths Ch 1 - Coordinates: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch01"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c9_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

from math import isqrt, sqrt
assert 3**2 + 4**2 == 5**2 and 6**2 + 8**2 == 10**2 and 5**2 + 12**2 == 13**2
assert 8**2 + 6**2 == 10**2 and 6 + 8 + 10 == 24 and 24 * 50 == 1200 and 2 * (8 + 6) * 5 == 140 and 140 * 40 == 5600
assert (2 - 5)**2 + (1 + 1)**2 == (2 - 0)**2 + (1 + 2)**2 == 13
assert (-2 - 1)**2 + 4**2 == (4 - 1)**2 + 4**2 == 25
assert 3**2 + 4**2 == 5**2 and 0.5 * 3 * 4 == 6
assert (8 - 5)**2 + 4**2 == 25 and (2 - 5)**2 + 4**2 == 25
assert (3 - 1)**2 + (2 - 0)**2 == 8 and (7 - 5)**2 + (6 - 2)**2 == 20
assert (-1 + 3) // 1 == 2 and (-1 + 5) == 4 and (-1 - 3 + 4 + 3 * 0) == 0
# equidistant point on x-axis from (1,2),(5,-2): x=3
assert (3 - 1)**2 + 4 == (3 - 5)**2 + 4
# distance table: (3,4)->5, (-6,2)->sqrt40, (0,-7)->7, (-5,-5)->sqrt50
assert [9 + 16, 36 + 4, 49, 25 + 25] == [25, 40, 49, 50]
# pond: centre (3,-1), end (7,2) -> other (-1,-4), radius 5
assert (2 * 3 - 7, 2 * -1 - 2) == (-1, -4) and (7 - 3)**2 + (2 + 1)**2 == 25
# y-axis equidistant from (-3,2) and (5,-2): y=-2
assert 9 + (-2 - 2)**2 == 25 + (-2 + 2)**2 == 25
# parallelogram (-1,-1),(5,1),(7,5),(1,3)
assert (-1 + 7, -1 + 5) == (5 + 1, 1 + 3) and 36 + 4 == 40 and 4 + 16 == 20 and 64 + 36 == 100 and 16 + 4 == 20
# section 2:3 for (-4,1),(6,-4): (0,-1)
assert (2 * 6 + 3 * -4, 2 * -4 + 3 * 1) == (0, -5) and 0 // 5 == 0 and -5 // 5 == -1
# rhombus A(0,0) B(3,4) C(8,4) D(5,0)
assert 9 + 16 == 25 and 25 + 0 == 25 and 9 + 16 == 25 and 25 == 25 and 64 + 16 == 80 and 4 + 16 == 20 and 80 * 20 == 1600 and isqrt(1600) // 2 == 20
# lighthouse ranges
assert 25 + 144 == 169 and 144 + 25 == 169 and 100 + 81 == 181 > 169
# square diag (1,1),(7,7): B(1,7), D(7,1); side 6
assert 36 + 0 == 36 and 72 == 2 * 36
# reflections P(-3,4)
assert 36 + 64 == 100
# isosceles H(-2,1) S(4,9) L(10,1)
assert 36 + 64 == 100 == 36 + 64 and 12 * 8 // 2 == 48
# taxi 14 vs 10, saving 4, cost 48
assert 8 + 6 == 14 and 8**2 + 6**2 == 100 and 4 * 12 == 48
# midpoint a,b
assert (2 + 6, 2 + 8) == (8, 10) and 16 + 36 == 52
# kite
assert 4 + 9 == 13 and 4 + 25 == 29 and 13 != 29
# Jaipur grid: H(0,0) J(3,4) A(-3,4)
assert 9 + 16 == 25 and 36 == 6**2 and 5 + 6 + 5 == 16 and 16 * 15 == 240

WS = [
# ---------------- EASY ----------------
W("The point $(-4, 7)$ lies in:", 1, "(b) Quadrant II. The $x$-coordinate is negative and the $y$-coordinate is positive. (1)", "E", opts=["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV"]),
W("Which of these points lies on the $y$-axis?", 1, "(c) $(0, -5)$. Every point on the $y$-axis has abscissa $0$. (1)", "E", opts=["$(-5, 0)$", "$(5, 5)$", "$(0, -5)$", "$(-5, -5)$"]),
W("The reflection of the point $(3, -2)$ in the $x$-axis is:", 1, "(b) $(3, 2)$. Reflection in the $x$-axis changes only the sign of the $y$-coordinate. (1)", "E", opts=["$(-3, -2)$", "$(3, 2)$", "$(-3, 2)$", "$(2, 3)$"]),
W("The distance of the point $(6, 8)$ from the origin is:", 1, "(d) $10$ units. $\\sqrt{6^2+8^2}=\\sqrt{100}=10$. (1)", "E", opts=["$14$ units", "$2$ units", "$7$ units", "$10$ units"]),
W("The midpoint of the segment joining $(2, 4)$ and $(8, 10)$ is:", 1, "(a) $(5, 7)$. $\\left(\\frac{2+8}{2}, \\frac{4+10}{2}\\right)=(5,7)$. (1)", "E", opts=["$(5, 7)$", "$(10, 14)$", "$(6, 6)$", "$(3, 3)$"]),
W("A point has ordinate $0$ and abscissa $-6$. It lies:", 1, "(c) on the negative $x$-axis. Ordinate $0$ means the point is on the $x$-axis, and $-6$ is to the left of the origin. (1)", "E", opts=["on the positive $y$-axis", "in Quadrant III", "on the negative $x$-axis", "on the negative $y$-axis"]),
W("The coordinates $(3, 5)$ and $(5, 3)$ represent the same point. True or false? Give a reason.", 1, "**False.** The order matters: the first number is the abscissa ($x$) and the second the ordinate ($y$), so the two points are at different places. (1)", "E"),
W("On a map of Kota city drawn on a grid, the railway station is at the origin $(0,0)$. Anil walks $5$ blocks east and then $3$ blocks north. Write his final position as an ordered pair.", 1, "East is the positive $x$-direction and north the positive $y$-direction, so the position is $(5, 3)$. (1)", "E", wp=True),
W("In a treasure-hunt game you start at the origin and move $4$ units right and then $6$ units down. Write the coordinates of the treasure and name its quadrant.", 2, "Right $+4$ gives $x=4$; down $6$ gives $y=-6$, so the treasure is at $(4,-6)$ (1). Positive $x$ and negative $y$: Quadrant IV (1).", "E", wp=True),
W("Name the quadrant or axis in which each point lies: $(-2,-3)$, $(0,5)$, $(7,-1)$, $(-8,0)$.", 2, "$(-2,-3)$: Quadrant III; $(0,5)$: $y$-axis; $(7,-1)$: Quadrant IV; $(-8,0)$: $x$-axis. (Half mark each)", "E"),
W("Write the reflections of the point $(5, -7)$ in (i) the $x$-axis and (ii) the $y$-axis.", 2, "(i) $(5, 7)$ (1). (ii) $(-5, -7)$ (1).", "E"),
W("The cinema hall is at $(1, 2)$ and the park is at $(1, 8)$ on a town map in which $1$ unit $=100$ m. Find the distance between them in metres.", 2, "Same $x$-coordinate, so the distance is $|8-2|=6$ units (1) $=600$ m (1).", "E", wp=True),
W("The school gate is at $(0,0)$ on a map drawn in units of $10$ m, and the library is at $(3,4)$. How far is the library from the gate?", 2, "Distance $=\\sqrt{3^2+4^2}=5$ units (1) $=5\\times10=50$ m (1).", "E", wp=True),
W("Two friends live at $(2, 6)$ and $(10, 2)$ on a grid map. They decide to meet at the midpoint of their houses. Find the meeting point.", 2, "$\\left(\\frac{2+10}{2},\\frac{6+2}{2}\\right)$ (1) $=(6,4)$ (1).", "E", wp=True),
W("Find $x$ if the point $(x, 4)$ lies on the $y$-axis, and find $y$ if the point $(-3, y)$ lies on the $x$-axis.", 2, "A point on the $y$-axis has abscissa $0$, so $x=0$ (1). A point on the $x$-axis has ordinate $0$, so $y=0$ (1).", "E"),
W("Three vertices of a rectangle $ABCD$ are $A(1,1)$, $B(5,1)$ and $C(5,4)$. Write the coordinates of $D$.", 2, "$AB$ is horizontal and $BC$ is vertical (1), so $D$ has the $x$-coordinate of $A$ and the $y$-coordinate of $C$: $D(1,4)$ (1).", "E"),
W("Find the distance of the point $(-5, 12)$ from the origin.", 2, "$\\sqrt{(-5)^2+12^2}=\\sqrt{25+144}$ (1) $=\\sqrt{169}=13$ units (1).", "E"),
# ---------------- MEDIUM ----------------
W("On a map (1 unit $=1$ km) the post office is at $P(-3, 2)$ and the hospital is at $H(5, -4)$. Find the distance between them.", 3, "$PH=\\sqrt{(5+3)^2+(-4-2)^2}$ (1) $=\\sqrt{64+36}$ (1) $=\\sqrt{100}=10$ km (1).", "M", wp=True),
W("A well is to be dug exactly midway between two villages at $A(-4, 7)$ and $B(6, -3)$. Find its position.", 2, "Midpoint $=\\left(\\frac{-4+6}{2},\\frac{7-3}{2}\\right)$ (1) $=(1,2)$ (1).", "M", wp=True),
W("Ravi says the distance between $(1,2)$ and $(4,6)$ is $(4-1)+(6-2)=7$. Find his mistake and give the correct distance.", 2, "He added the horizontal and vertical differences instead of using the distance formula (the straight-line distance is the hypotenuse) (1). Correct: $\\sqrt{3^2+4^2}=5$ (1).", "M"),
W("Meena found the midpoint of $(2,8)$ and $(6,4)$ as $(4,-2)$ by subtracting the coordinates. What is wrong? Write the correct midpoint.", 2, "The midpoint is the **average** (sum divided by $2$), not the difference (1). Correct: $\\left(\\frac{2+6}{2},\\frac{8+4}{2}\\right)=(4,6)$ (1).", "M"),
W("A lamp post stands at $P(2, 1)$. Two stalls are at $A(5,-1)$ and $B(0,-2)$. Show that the lamp post is equally far from both stalls.", 3, "$PA^2=(5-2)^2+(-1-1)^2=9+4=13$ (1). $PB^2=(0-2)^2+(-2-1)^2=4+9=13$ (1). $PA=PB=\\sqrt{13}$, so the lamp post is equidistant (1).", "M", wp=True),
W("Three flags are planted at $A(-2,0)$, $B(4,0)$ and $C(1,4)$. Show that the triangle they form is isosceles.", 3, "$AC=\\sqrt{(1+2)^2+4^2}=5$ (1). $BC=\\sqrt{(1-4)^2+4^2}=5$ (1). $AB=6$. Since $AC=BC$ the triangle is isosceles (1).", "M", wp=True),
W("A triangular park has corners at $A(1,2)$, $B(4,2)$ and $C(4,6)$. Show that it is right-angled and find its area (units in metres).", 3, "$AB=3$, $BC=4$, $AC=\\sqrt{9+16}=5$ (1). $AB^2+BC^2=9+16=25=AC^2$, so the angle at $B$ is $90^\\circ$ (1). Area $=\\frac12\\times3\\times4=6$ m$^2$ (1).", "M", wp=True),
W("For what value(s) of $k$ is the distance between $(k, 2)$ and $(5, 6)$ equal to $5$ units?", 3, "$(k-5)^2+(2-6)^2=25$ (1). $(k-5)^2=9$, so $k-5=\\pm3$ (1). $k=8$ or $k=2$ (1).", "M"),
W("A rope is stretched between two poles at $(-1,2)$ and $(8,11)$. Two knots divide it into three equal parts. Find the coordinates of the knots.", 3, "The knots divide the segment in the ratios $1:2$ and $2:1$ (1). Add one third of $(9,9)$ to the start: $(-1+3,2+3)=(2,5)$ (1). Add two thirds: $(-1+6,2+6)=(5,8)$ (1).", "M", wp=True),
W("Three vertices of a parallelogram $PQRS$ are $P(0,0)$, $Q(5,1)$ and $R(7,4)$. Find $S$.", 3, "Diagonals $PR$ and $QS$ bisect each other (1). Midpoint of $PR=(3.5,2)$ (1). If $S=(a,b)$: $\\frac{5+a}{2}=3.5$ and $\\frac{1+b}{2}=2$, so $S=(2,3)$ (1).", "M"),
W("Three lamp posts stand at $A(1,1)$, $B(3,5)$ and $C(5,9)$. Check whether they are in a straight line.", 3, "$AB=\\sqrt{4+16}=2\\sqrt5$, $BC=\\sqrt{4+16}=2\\sqrt5$ (1). $AC=\\sqrt{16+64}=4\\sqrt5$ (1). $AB+BC=AC$, so they are collinear (1).", "M", wp=True),
W("The point $P(-4, 5)$ is reflected in the $x$-axis, the $y$-axis and the origin. Write the three images and the quadrant of each.", 3, "$x$-axis: $(-4,-5)$, Quadrant III (1). $y$-axis: $(4,5)$, Quadrant I (1). Origin: $(4,-5)$, Quadrant IV (1).", "M"),
W("A drone starts at the origin, flies to $A(6,0)$, then to $B(6,8)$ and then straight back to the origin. If $1$ unit $=50$ m, find the total distance flown.", 3, "$OA=6$, $AB=8$ (1). $BO=\\sqrt{36+64}=10$ (1). Total $=24$ units $=24\\times50=1200$ m (1).", "M", wp=True),
W("A rectangular field $ABCD$ has $A(0,0)$, $B(8,0)$, $C(8,6)$, $D(0,6)$, where $1$ unit $=5$ m. Find the length of the diagonal $AC$ in metres and the cost of fencing the field at ₹ $40$ per metre.", 3, "$AC=\\sqrt{64+36}=10$ units $=50$ m (1). Perimeter $=2(8+6)=28$ units $=140$ m (1). Cost $=140\\times40=$ ₹ $5600$ (1).", "M", wp=True),
W("Find the point on the $x$-axis that is equidistant from $A(1,2)$ and $B(5,-2)$.", 3, "Let $P(x,0)$. $PA^2=(x-1)^2+4$, $PB^2=(x-5)^2+4$ (1). Equating: $x^2-2x+1=x^2-10x+25$ (1), so $8x=24$, $x=3$; $P(3,0)$ (1).", "M"),
W("Four shops on a market map (units in 100 m) are at $S_1(3,4)$, $S_2(-6,2)$, $S_3(0,-7)$ and $S_4(-5,-5)$. The bus stop is at the origin. Which shop is nearest to the bus stop?", 3, "Squared distances: $S_1:9+16=25$; $S_2:36+4=40$; $S_3:49$; $S_4:25+25=50$ (2). The smallest is $25$, so $S_1(3,4)$ is nearest, at $5$ units $=500$ m (1).", "M", wp=True),
W("A circular pond has a diameter with one end at $(7,2)$ and the centre at $(3,-1)$. Find the other end of the diameter and the radius of the pond.", 3, "The centre is the midpoint, so the other end is $(2\\times3-7,\\ 2\\times(-1)-2)=(-1,-4)$ (2). Radius $=\\sqrt{(7-3)^2+(2+1)^2}=5$ units (1).", "M", wp=True),
W("The vertices of a quadrilateral are $A(1,1)$, $B(4,1)$, $C(4,5)$ and $D(1,5)$. Show that $ABCD$ is a rectangle and find the length of its diagonals.", 3, "$AB=CD=3$ and $BC=DA=4$ (1). $AC=\\sqrt{9+16}=5$ and $BD=\\sqrt{9+16}=5$ (1). Opposite sides equal and diagonals equal, so it is a rectangle with diagonals of length $5$ (1).", "M"),
W("State true or false with a reason: (i) the point $(-3,0)$ lies in Quadrant II; (ii) the distance of the point $(x,y)$ from the $y$-axis is $|x|$.", 2, "(i) **False**: its ordinate is $0$, so it lies on the $x$-axis and in no quadrant (1). (ii) **True**: the distance from the $y$-axis is the horizontal distance, which is $|x|$ (1).", "M"),
W("A cyclist rides in a straight line from $A(-2,-1)$ to $B(4,7)$ on a map where $1$ unit $=1$ km. If she cycles at $12$ km/h, how long does she take?", 3, "$AB=\\sqrt{(4+2)^2+(7+1)^2}=\\sqrt{36+64}=10$ km (2). Time $=\\frac{10}{12}$ h $=50$ minutes (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Show that the points $A(0,0)$, $B(6,0)$ and $C(3,3\\sqrt3)$ are the vertices of an equilateral triangle.", 3, "$AB=6$ (1). $AC=\\sqrt{9+27}=6$ (1). $BC=\\sqrt{(3-6)^2+27}=\\sqrt{36}=6$. All three sides are $6$, so the triangle is equilateral (1).", "H"),
W("A taxi has to go from home $(1,2)$ to the office $(9,8)$ in a city whose roads run only east-west and north-south ($1$ unit $=1$ km). Compare the road distance with the straight-line distance and find the extra money the passenger pays at ₹ $12$ per km.", 3, "Road distance $=|9-1|+|8-2|=8+6=14$ km (1). Straight line $=\\sqrt{64+36}=10$ km (1). Extra distance $=4$ km, so extra cost $=4\\times12=$ ₹ $48$ (1).", "H", wp=True),
W("A point $P$ lies on the $y$-axis and is equidistant from $A(-3,2)$ and $B(5,-2)$. Find $P$ and verify your answer.", 4, "Let $P(0,y)$. $PA^2=9+(y-2)^2$, $PB^2=25+(y+2)^2$ (1). Equating: $13-4y=29+4y$ (1), so $y=-2$, $P(0,-2)$ (1). Check: $PA^2=9+16=25$, $PB^2=25+0=25$ (1).", "H"),
W("A boat is at $A(-4,1)$ and a buoy at $B(6,-4)$. A signal station is placed on $AB$ so that its distance from $A$ and from $B$ are in the ratio $2:3$. Find its coordinates.", 3, "Use the section formula with $m:n=2:3$ (1). $x=\\frac{2(6)+3(-4)}{5}=0$ (1), $y=\\frac{2(-4)+3(1)}{5}=-1$ (1). The station is at $(0,-1)$.", "H", wp=True),
W("A lighthouse stands at the origin and its beam reaches $13$ km ($1$ unit $=1$ km). Three ships are at $A(5,12)$, $B(-12,-5)$ and $C(10,9)$. Which ships are inside the range, which are exactly on the boundary and which are outside?", 4, "$OA^2=25+144=169$, so $OA=13$ (1). $OB^2=144+25=169$, so $OB=13$ (1). $OC^2=100+81=181>169$, so $OC>13$ (1). Ships $A$ and $B$ are exactly on the boundary; ship $C$ is outside; none is strictly inside (1).", "H", wp=True),
W("Rahul's house is $H(-2,1)$, the school is $S(4,9)$ and the library is $L(10,1)$ (1 unit $=100$ m). Show that $\\triangle HSL$ is isosceles, find the midpoint $M$ of $HL$, and hence find the area of the triangle in square units.", 4, "$HS=\\sqrt{36+64}=10$, $SL=\\sqrt{36+64}=10$, so isosceles (1). $M=\\left(\\frac{-2+10}{2},\\frac{1+1}{2}\\right)=(4,1)$ (1). $SM=9-1=8$ is the height (1). $HL=12$, area $=\\frac12\\times12\\times8=48$ sq. units (1).", "H", wp=True),
W("If the midpoint of the line segment joining $(a,2)$ and $(6,b)$ is $(4,5)$, find $a$ and $b$ and then the length of the segment.", 4, "$\\frac{a+6}{2}=4$ gives $a=2$ (1). $\\frac{2+b}{2}=5$ gives $b=8$ (1). The points are $(2,2)$ and $(6,8)$ (1). Length $=\\sqrt{16+36}=\\sqrt{52}=2\\sqrt{13}$ (1).", "H"),
W("A point $P(-3,4)$ is reflected in the $x$-axis to get $Q$, and $Q$ is reflected in the $y$-axis to get $R$. Name the quadrants of $Q$ and $R$, and find the length $PR$. What is the relation between $P$ and $R$?", 4, "$Q(-3,-4)$, Quadrant III (1). $R(3,-4)$, Quadrant IV (1). $PR=\\sqrt{(3+3)^2+(-4-4)^2}=\\sqrt{36+64}=10$ (1). $R$ is the reflection of $P$ in the origin (both signs changed) (1).", "H"),
W("Show that $A(0,3)$, $B(2,0)$, $C(0,-5)$ and $D(-2,0)$ form a kite but not a rhombus.", 4, "$AB=\\sqrt{4+9}=\\sqrt{13}$, $AD=\\sqrt{4+9}=\\sqrt{13}$ (1). $CB=\\sqrt{4+25}=\\sqrt{29}$, $CD=\\sqrt{4+25}=\\sqrt{29}$ (1). Two pairs of equal adjacent sides make a kite (1). $\\sqrt{13}\\ne\\sqrt{29}$, so the four sides are not all equal and it is not a rhombus (1).", "H"),
W("The diagonal of a square garden has end points $A(1,1)$ and $C(7,7)$. Find the other two vertices $B$ and $D$ and the side of the square.", 4, "The diagonals bisect each other at right angles: centre $=(4,4)$ (1). The other diagonal is perpendicular to $AC$ and equal in length, so $B$ and $D$ are $(4\\mp3,4\\pm3)$, i.e. $B(1,7)$ and $D(7,1)$ (2). Side $=AB=\\sqrt{0+36}=6$ (1).", "H"),
W("Show that $A(0,0)$, $B(3,4)$, $C(8,4)$ and $D(5,0)$ are the vertices of a rhombus. Use the diagonals to find its area.", 5, "$AB=\\sqrt{9+16}=5$, $BC=5$, $CD=\\sqrt{9+16}=5$, $DA=5$ (2). All sides equal, so it is a rhombus (1). $AC=\\sqrt{64+16}=\\sqrt{80}$, $BD=\\sqrt{4+16}=\\sqrt{20}$ (1). Area $=\\frac12\\times AC\\times BD=\\frac12\\sqrt{1600}=20$ sq. units (1).", "H"),
W("The vertices of a quadrilateral are $A(-1,-1)$, $B(5,1)$, $C(7,5)$ and $D(1,3)$. Show that $ABCD$ is a parallelogram but neither a rectangle nor a rhombus.", 5, "Midpoint of $AC=(3,2)$ and of $BD=(3,2)$; diagonals bisect each other, so it is a parallelogram (2). $AB=\\sqrt{40}$, $BC=\\sqrt{20}$, adjacent sides unequal, so not a rhombus (1). $AC=\\sqrt{64+36}=10$, $BD=\\sqrt{16+4}=\\sqrt{20}$, unequal diagonals, so not a rectangle (2).", "H"),
W("On a simplified tourist grid of Jaipur ($1$ unit $=1$ km) the Hawa Mahal is at $H(0,0)$, Jantar Mantar at $J(3,4)$ and Amer Fort at $A(-3,4)$. (i) Find $HJ$, $HA$ and $JA$. (ii) A tea stall is built at the midpoint of $JA$; find its position and its distance from $H$. (iii) A tourist bus goes $H\\to J\\to A\\to H$ at ₹ $15$ per km. Find the fare for the whole trip.", 5, "(i) $HJ=\\sqrt{9+16}=5$, $HA=\\sqrt{9+16}=5$, $JA=|3-(-3)|=6$ km (2). (ii) Midpoint $=(0,4)$ (1); distance from $H=4$ km (1). (iii) Trip $=5+6+5=16$ km, fare $=16\\times15=$ ₹ $240$ (1).", "H", wp=True),
]

_o = _old(1)
_pre, _tail = _o["blocks"][:-2], _o["blocks"][-2:]
_extra = [
 ("h2", "1.6 Worked Examples"),
 ("steps", [("Example 1 — Locating a point from directions", "A kite is flown from the origin 12 m east and 5 m south. Position: (12, −5), Quadrant IV. Distance from the origin = √(144 + 25) = √169 = **13 m**.")]),
 ("steps", [("Example 2 — Distance on a map", "School S(−3, 2) and hospital H(5, −4), 1 unit = 1 km. SH = √[(5 + 3)² + (−4 − 2)²] = √(64 + 36) = **10 km**. Notice that the differences are found with signs and then squared, so (5 − (−3)) = 8 and not 2.")]),
 ("steps", [("Example 3 — Midpoint as a meeting place", "Two friends at (−4, 7) and (6, −3) meet halfway. Midpoint = ((−4 + 6)/2, (7 − 3)/2) = **(1, 2)**. If the midpoint and one end are known, the other end = 2 × midpoint − known end. Midpoint (3, −1), end (7, 2) gives the other end (−1, −4).")]),
 ("steps", [("Example 4 — Equidistant point on an axis", "Find the point on the x-axis equidistant from A(1, 2) and B(5, −2). Let P(x, 0). PA² = (x − 1)² + 4 and PB² = (x − 5)² + 4. Equate: x² − 2x + 1 = x² − 10x + 25, so 8x = 24 and x = 3. **P(3, 0)**. The x² terms cancel, so the equation is always linear.")]),
 ("steps", [("Example 5 — Proving a triangle is right-angled", "A(1, 2), B(4, 2), C(4, 6): AB = 3, BC = 4, AC = 5. AB² + BC² = 9 + 16 = 25 = AC², so ∠B = 90°. Area = ½ × 3 × 4 = **6 square units**. Always test the two smaller squares against the largest.")]),
 ("steps", [("Example 6 — Rhombus from coordinates", "A(0, 0), B(3, 4), C(8, 4), D(5, 0). All four sides are 5, so it is a rhombus. Diagonals AC = √80 and BD = √20, so area = ½ × √80 × √20 = ½ × 40 = **20 square units**.")]),
 ("h2", "1.7 Word Problems: How to Translate"),
 ("ol", ["**Choose the origin and the unit.** The school gate, a station or a corner of the field is usually taken as (0, 0). Note what 1 unit stands for (10 m, 100 m, 1 km).", "**Convert directions to signs.** East or right = +x, west or left = −x, north or up = +y, south or down = −y.", "**Name the points** with letters and write each as an ordered pair before using any formula.", "**Pick the tool.** 'How far' = distance formula. 'Halfway', 'meeting point', 'centre' = midpoint. 'Equally far from' = equate squared distances. 'In a straight line' = sum of two distances equals the third.", "**Convert units at the end** (units × scale) and attach the unit (m, km, ₹). Money questions: multiply the length by the rate."]),
 ("table", ["Words in the problem", "Maths meaning", "Example"], [
  ["walks 5 blocks east, 3 blocks north", "(5, 3) from the start", "start at the origin"],
  ["equally far from two places", "PA = PB, so PA² = PB²", "lamp post P(2, 1), stalls (5, −1) and (0, −2)"],
  ["midway, exactly in the middle", "midpoint formula", "well between two villages"],
  ["centre of a pond, circle or square", "midpoint of a diameter or a diagonal", "other end = 2 × centre − known end"],
  ["travels only along roads in a grid", "|Δx| + |Δy| (not the distance formula)", "(1, 2) to (9, 8): 14 km by road, 10 km straight"],
  ["within the range of a lighthouse or tower", "distance from the centre ≤ range", "compare squared distances 169 and 181"]]),
 ("note", "REMEMBER", "**Common mistakes.** (1) Writing the point as (y, x). (2) Adding the differences instead of squaring and adding, giving 3 + 4 = 7 instead of 5. (3) Dividing by 2 only once in the midpoint (it applies to the sum of each coordinate separately). (4) Calling (0, 5) a point in the first quadrant: it lies on the axis. (5) Forgetting that the reflection in the x-axis changes the sign of y only. (6) Forgetting the unit scale and the final multiplication by the rate."),
 ("note", "IMPORTANT", "**Section formula idea.** A point that divides AB in the ratio m : n is ((m x₂ + n x₁)/(m + n), (m y₂ + n y₁)/(m + n)). Boat A(−4, 1), buoy B(6, −4), ratio 2 : 3 gives ((12 − 12)/5, (−8 + 3)/5) = (0, −1). The midpoint is the special case m = n."),
 ("h2", "1.8 Taxi Distance and Straight-line Distance"),
 ("p", "In a city where roads run only east–west and north–south, the road distance between (x₁, y₁) and (x₂, y₂) is |x₂ − x₁| + |y₂ − y₁|, while the straight-line distance is √[(x₂ − x₁)² + (y₂ − y₁)²]. The road distance is never smaller. From (1, 2) to (9, 8): road = 8 + 6 = 14 km and straight = 10 km, so a taxi charging ₹ 12 per km costs ₹ 48 more by road than the straight path would. The two are equal only when the points lie on the same horizontal or vertical line."),
 ("h2", "1.9 More Shapes Checklist"),
 ("table", ["Shape", "Test using coordinates", "Verdict example"], [
  ["Kite", "two pairs of equal adjacent sides, not all four equal", "A(0, 3), B(2, 0), C(0, −5), D(−2, 0): √13, √13, √29, √29"],
  ["Square", "four equal sides and equal diagonals", "(1, 1), (7, 7) as a diagonal gives vertices (1, 7), (7, 1)"],
  ["Rhombus", "four equal sides, or a parallelogram with unequal diagonals meeting at 90°", "area = ½ × d₁ × d₂"],
  ["Parallelogram, not a rectangle", "diagonals share a midpoint but have different lengths", "(−1, −1), (5, 1), (7, 5), (1, 3)"],
  ["Equilateral triangle", "all three distances equal (surds are allowed)", "(0, 0), (6, 0), (3, 3√3): all sides 6"]]),
]
CH = dict(_o, blocks=_pre + _extra + _tail, takeaways=_o["takeaways"] + ["In word problems fix the **origin and the unit scale** first, turn directions into signs, then choose distance, midpoint or equidistance.", "**Road (grid) distance = |Δx| + |Δy|** is at least as large as the straight-line distance from the distance formula.", "If the midpoint M and one end A are known, the other end is **2M − A**."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
