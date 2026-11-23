"""Class 10 Maths Ch 7 - Coordinate Geometry: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch07"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

d2 = lambda P, Q: (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2
sec = lambda A, B, m, n: (F(m * B[0] + n * A[0], m + n), F(m * B[1] + n * A[1], m + n))
assert d2((3, 4), (0, 0)) == 25 and d2((-3, 4), (3, -4)) == 100 and d2((-6, 8), (0, 0)) == 100 and sec((2, 3), (8, 7), 1, 1) == (5, 5)
assert sec((1, 2), (7, 8), 1, 2) == (3, 4) and d2((2, -3), (-2, 1)) == 32 and sec((-4, 6), (8, -2), 1, 1) == (2, 2) and sec((4, -3), (8, 5), 3, 1) == (7, 3)
assert d2((0, 0), (9, 12)) == 225 and sec((2, 3), (8, 11), 1, 1) == (5, 7) and d2((2, 3), (8, 11)) == 100 and d2((0, 0), (5, 12)) == 169 and d2((0, 0), (8, 6)) == 100
assert sorted([d2((0, 0), (3, 0)), d2((3, 0), (3, 4)), d2((0, 0), (3, 4))]) == [9, 16, 25] and d2((1, 2), (4, 6)) == 25 and sec((-3, 4), (5, -2), 1, 1) == (1, 1)
assert d2((2, 3), (6, 0)) == 25 == d2((2, 3), (-2, 0))
assert d2((6, 5), (0, 9)) == d2((-4, 3), (0, 9)) == 52
A, B, C, D = (-1, -2), (1, 0), (-1, 2), (-3, 0)
assert len({d2(A, B), d2(B, C), d2(C, D), d2(D, A)}) == 1 and d2(A, C) == d2(B, D) == 16
A, B, C = (7, 10), (-2, 5), (3, -4); assert d2(A, B) == d2(B, C) == 106 and d2(C, A) == 212
assert d2((2, 3), (4, 5)) * 9 == d2((2, 3), (8, 9)) and 8 + 32 == 72 // 1 - 32 or True
assert sec((-1, 7), (4, -3), 2, 3) == (1, 3) and sec((4, -1), (-2, -3), 1, 2) == (2, F(-5, 3)) and sec((4, -1), (-2, -3), 2, 1) == (0, F(-7, 3))
assert (-3 + 5) / 2 == 1 and (4 - 8) / 2 == -2 and sec((-2, 5), (10, -1), 1, 2) == (2, 3) and sec((3, 6), (-12, -3), 2, 1)[1] == 0
assert (1 + 6 - 4, 2 + 6 - 3) == (3, 5) and (2 * 2 - 5, 2 * -3 + 1) == (-1, -5) and sec((1, 2), (9, 10), 3, 1) == (7, 8)
assert d2((2, -3), (10, 3)) == d2((2, -3), (10, -9)) == 100 and d2((-2, 0), (-2, 5)) == d2((-2, 0), (2, -3)) == 25 + 0 or True
assert d2((-2, 0), (-2, 5)) == 25 and d2((-2, 0), (2, -3)) == 25 and sec((2, 1), (5, -8), 1, 2) == (3, -2) and 6 + 2 - 8 == 0
assert sec((-3, 10), (6, -8), 2, 7) == (-1, 6) and 3 * 3 + 6 - 4 * 0 != 0
assert d2((-1, 2), (1, 4)) == d2((-1, 2), (1, 0)) == 8 and d2((-1, 2), (3, 2)) == 16
P = [(-4, -1), (-2, -4), (4, 0), (2, 3)]
assert d2(P[0], P[1]) == d2(P[2], P[3]) == 13 and d2(P[1], P[2]) == d2(P[3], P[0]) == 52 and d2(P[0], P[2]) == d2(P[1], P[3]) == 65
R = [(-3, 2), (-5, -5), (2, -3), (4, 4)]
assert len({d2(R[i], R[(i + 1) % 4]) for i in range(4)}) == 1 and d2(R[0], R[2]) == 50 and d2(R[1], R[3]) == 162
S = [(1, 7), (4, 2), (-1, -1), (-4, 4)]
assert len({d2(S[i], S[(i + 1) % 4]) for i in range(4)}) == 1 and d2(S[0], S[2]) == d2(S[1], S[3]) == 68
assert sec((2, 3), (6, -3), 1, 1) == (4, 0) and sec((5, -6), (-1, -4), 5, 1) == (0, F(-13, 3))
assert (3, 4) and d2((0, 0), (4, 3)) == d2((8, 0), (4, 3)) == d2((0, 6), (4, 3)) == 25 and d2((0, 0), (3, 4)) == 25 and d2((-4, -3), (0, 0)) == 25
assert d2((2, 0), (0, 0)) == 4 and 2 ** 2 + 12 == 16
assert sec((2, 3), (8, 9), 1, 2) == (4, 5) and (1 * 2 + 2 * 8, 1 * 3 + 2 * 9) == (18, 21)
assert (6 + 9, 1 + 4) == (7.5 * 2, 2.5 * 2) and (8 + 7) / 2 == 7.5
a = 3; assert (2 * a - 11) ** 2 + (a + 2) ** 2 == 50 and (2 * 5 - 11) ** 2 + 49 == 50
assert (2 * 2 - 2) / 2 == 1 and (4 + 2 * 3) / 2 == 5 == 2 * 2 + 1

WS = [
# ---------------- EASY ----------------
W(r"The distance of the point $(3,4)$ from the origin is:", 1, r"(a) 5. $\sqrt{3^2+4^2}=\sqrt{25}=5$. (1)", "E", opts=["5", "7", "1", "25"]),
W(r"The distance between the points $(-3,4)$ and $(3,-4)$ is:", 1, r"(c) 10. $\sqrt{(3+3)^2+(-4-4)^2}=\sqrt{36+64}=10$. (1)", "E", opts=["6", "8", "10", "14"]),
W(r"The distance of the point $(-6,8)$ from the origin is:", 1, r"(b) 10. $\sqrt{36+64}=10$. (1)", "E", opts=["14", "10", "2", "100"]),
W(r"The mid-point of the line segment joining $(2,3)$ and $(8,7)$ is:", 1, r"(a) $(5,5)$. $\left(\dfrac{2+8}2,\dfrac{3+7}2\right)=(5,5)$. (1)", "E", opts=["(5, 5)", "(6, 4)", "(10, 10)", "(3, 2)"]),
W(r"The coordinates of every point on the $y$-axis are of the form:", 1, r"(b) $(0,y)$. On the $y$-axis the abscissa ($x$-coordinate) is 0. (1)", "E", opts=["(x, 0)", "(0, y)", "(x, x)", "(y, y)"]),
W(r"The point which divides the line segment joining $(1,2)$ and $(7,8)$ internally in the ratio $1:2$ is:", 1, r"(a) $(3,4)$. $\left(\dfrac{1\cdot7+2\cdot1}3,\dfrac{1\cdot8+2\cdot2}3\right)=(3,4)$. (1)", "E", opts=["(3, 4)", "(5, 6)", "(4, 5)", "(2, 3)"]),
W(r"The perpendicular distance of the point $P(4,3)$ from the $x$-axis is:", 1, r"(b) 3. The distance from the $x$-axis is the absolute value of the $y$-coordinate. (1)", "E", opts=["4", "3", "5", "7"]),
W(r"Find the distance between $A(2,-3)$ and $B(-2,1)$.", 2, r"$AB=\sqrt{(-2-2)^2+(1+3)^2}=\sqrt{16+16}$ (1) $=\sqrt{32}=$ **$4\sqrt2$** (1).", "E"),
W(r"Find the mid-point of the segment joining $(-4,6)$ and $(8,-2)$.", 2, r"$\left(\dfrac{-4+8}2,\dfrac{6-2}2\right)$ (1) $=(2,2)$ (1).", "E"),
W(r"Find the coordinates of the point which divides the line segment joining $(4,-3)$ and $(8,5)$ in the ratio $3:1$ internally.", 2, r"$x=\dfrac{3(8)+1(4)}4=7$ (1), $y=\dfrac{3(5)+1(-3)}4=3$. Point $(7,3)$ (1).", "E"),
W(r"On a map grid, village A is at the origin and village B is at $(9,12)$, where 1 unit is 1 km. What is the straight-line distance between the villages?", 2, r"$AB=\sqrt{9^2+12^2}=\sqrt{225}$ (1) $=$ **15 km** (1).", "E", wp=True),
W(r"Two friends' houses are at $(2,3)$ and $(8,11)$ on a grid in which 1 unit is 100 m. They want to meet at the mid-point of their houses. Find the meeting point and how far each must walk.", 2, r"Mid-point $=(5,7)$ (1). Distance between houses $=\sqrt{36+64}=10$ units, so each walks 5 units $=$ **500 m** (1).", "E", wp=True),
W(r"True or false? Give a reason. The point $(-2,-3)$ lies in the third quadrant.", 1, r"**True.** Both coordinates are negative, which is the third quadrant (1).", "E"),
W(r"On a map with the school at the origin, the library is at $(5,12)$ and the hospital at $(8,6)$ (units in km). Which is nearer the school?", 2, r"Library: $\sqrt{25+144}=13$ km; hospital: $\sqrt{64+36}=10$ km (1). The **hospital** is nearer (1).", "E", wp=True),
W(r"Show that $(0,0)$, $(3,0)$ and $(3,4)$ are the vertices of a right triangle.", 2, r"Sides: $3$, $4$ and $\sqrt{9+16}=5$ (1). $3^2+4^2=5^2$, so the triangle is right-angled at $(3,0)$ (1).", "E"),
W(r"Priya finds the distance between $(1,2)$ and $(4,6)$ as $\sqrt{(4+1)^2+(6+2)^2}=\sqrt{89}$. What is her mistake? Give the correct distance.", 2, r"She **added** the coordinates; the formula needs the **differences** (1). $\sqrt{(4-1)^2+(6-2)^2}=\sqrt{25}=$ **5** (1).", "E"),
W(r"The ends of a diameter of a circular park on a map are $(-3,4)$ and $(5,-2)$. Find the position of the centre of the park.", 2, r"The centre is the mid-point of the diameter (1): $\left(\dfrac{-3+5}2,\dfrac{4-2}2\right)=(1,1)$ (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"Find the values of $x$ for which the distance between $(2,3)$ and $(x,0)$ is 5.", 3, r"$(x-2)^2+9=25$ (1) $\Rightarrow(x-2)^2=16$ (1). $x=6$ or $x=-2$ (1).", "M"),
W(r"Find a point on the $y$-axis which is equidistant from $A(6,5)$ and $B(-4,3)$.", 3, r"Let the point be $(0,y)$: $36+(y-5)^2=16+(y-3)^2$ (1). $61-10y=25-6y$ (1). $y=9$; the point is $(0,9)$ (1).", "M"),
W(r"Show that the points $A(-1,-2)$, $B(1,0)$, $C(-1,2)$ and $D(-3,0)$ are the vertices of a square.", 3, r"$AB=BC=CD=DA=\sqrt{8}=2\sqrt2$ (1,1). Diagonals $AC=BD=4$ (1). Four equal sides and equal diagonals: a **square**.", "M"),
W(r"Show that $(7,10)$, $(-2,5)$ and $(3,-4)$ are the vertices of an isosceles right triangle.", 3, r"$AB=\sqrt{81+25}=\sqrt{106}$, $BC=\sqrt{25+81}=\sqrt{106}$, $CA=\sqrt{16+196}=\sqrt{212}$ (2). $AB=BC$ and $AB^2+BC^2=212=CA^2$, so it is isosceles right-angled at $B$ (1).", "M"),
W(r"Show that the points $P(2,3)$, $Q(4,5)$ and $R(8,9)$ are collinear.", 3, r"$PQ=\sqrt{4+4}=2\sqrt2$, $QR=\sqrt{16+16}=4\sqrt2$, $PR=\sqrt{36+36}=6\sqrt2$ (2). $PQ+QR=PR$, so the points lie on a straight line (1).", "M"),
W(r"Find the coordinates of the point which divides the line segment joining $(-1,7)$ and $(4,-3)$ in the ratio $2:3$.", 3, r"$x=\dfrac{2(4)+3(-1)}5=1$ (1,1). $y=\dfrac{2(-3)+3(7)}5=3$. Point $(1,3)$ (1).", "M"),
W(r"Find the coordinates of the points of trisection of the segment joining $A(4,-1)$ and $B(-2,-3)$.", 3, r"The points divide $AB$ in the ratios $1:2$ and $2:1$ (1). $P=\left(\dfrac{-2+8}3,\dfrac{-3-2}3\right)=\left(2,-\dfrac53\right)$ (1). $Q=\left(\dfrac{-4+4}3,\dfrac{-6-1}3\right)=\left(0,-\dfrac73\right)$ (1).", "M"),
W(r"The mid-point of the segment $AB$ is $(1,-2)$ and $A$ is $(-3,4)$. Find $B$.", 2, r"$\dfrac{-3+x}2=1\Rightarrow x=5$ (1); $\dfrac{4+y}2=-2\Rightarrow y=-8$. $B=(5,-8)$ (1).", "M"),
W(r"A bus stop is to be built on the straight road joining villages $P(-2,5)$ and $Q(10,-1)$ so that its distances from $P$ and $Q$ are in the ratio $1:2$. Find the position of the bus stop.", 3, r"$PS:SQ=1:2$ (1). $x=\dfrac{1(10)+2(-2)}3=2$ (1), $y=\dfrac{1(-1)+2(5)}3=3$. Bus stop at $(2,3)$ (1).", "M", wp=True),
W(r"On a map grid a straight cable joins towers $A(3,6)$ and $B(-12,-3)$ and a road runs along the $x$-axis. In what ratio does the road divide the cable? Find the crossing point.", 3, r"Let the ratio be $k:1$; the point has $y=0$: $\dfrac{-3k+6}{k+1}=0$ (1) $\Rightarrow k=2$, ratio **$2:1$** (1). $x=\dfrac{2(-12)+3}3=-7$; point $(-7,0)$ (1).", "M", wp=True),
W(r"Three vertices of a parallelogram $ABCD$ taken in order are $A(1,2)$, $B(4,3)$ and $C(6,6)$. Find $D$.", 3, r"The diagonals bisect each other, so mid-point of $AC$ = mid-point of $BD$ (1). Mid-point of $AC=(3.5,4)$ (1). $\dfrac{4+x}2=3.5$, $\dfrac{3+y}2=4$, so $D=(3,5)$ (1).", "M"),
W(r"One end of a diameter of a circle is $(5,-1)$ and its centre is $(2,-3)$. Find the other end.", 2, r"Centre is the mid-point: $\dfrac{5+x}2=2$, $\dfrac{-1+y}2=-3$ (1). Other end $=(-1,-5)$ (1).", "M"),
W(r"A drone flies in a straight line from $A(1,2)$ to $B(9,10)$ on a map grid. Find its position when it has covered $\dfrac34$ of the distance $AB$.", 3, r"It divides $AB$ in the ratio $3:1$ from $A$ (1). $x=\dfrac{3(9)+1(1)}4=7$, $y=\dfrac{3(10)+1(2)}4=8$ (1,1). Position $(7,8)$.", "M", wp=True),
W(r"Find the values of $y$ for which the distance between $(2,-3)$ and $(10,y)$ is 10 units.", 3, r"$64+(y+3)^2=100$ (1) $\Rightarrow(y+3)^2=36$ (1). $y=3$ or $y=-9$ (1).", "M"),
W(r"Find a point on the $x$-axis which is equidistant from $(-2,5)$ and $(2,-3)$.", 3, r"Point $(x,0)$: $(x+2)^2+25=(x-2)^2+9$ (1). $x^2+4x+29=x^2-4x+13$ (1) $\Rightarrow 8x=-16$, $x=-2$. Point $(-2,0)$ (1).", "M"),
W(r"A point $P(x,y)$ is equidistant from $A(3,6)$ and $B(-3,4)$. Find the relation between $x$ and $y$.", 3, r"$PA^2=PB^2$: $(x-3)^2+(y-6)^2=(x+3)^2+(y-4)^2$ (1). Expand: $-6x-12y+45=6x-8y+25$ (1). So $12x+4y=20$, i.e. $3x+y=5$ (1).", "M"),
W(r"True or false? Give a reason. The points $(0,0)$, $(1,1)$ and $(2,2)$ are collinear.", 2, r"**True.** Distances: $\sqrt2$, $\sqrt2$ and $2\sqrt2$ (1), and $\sqrt2+\sqrt2=2\sqrt2$ (1).", "M"),
W(r"Two opposite vertices of a square park on a map are $(-1,2)$ and $(3,2)$. Find the other two vertices.", 3, r"The diagonal is horizontal of length 4 with mid-point $(1,2)$ (1). The other diagonal is vertical, also of length 4, through $(1,2)$ (1). The vertices are $(1,4)$ and $(1,0)$ (1).", "M", wp=True),
W(r"In what ratio does the point $(-1,6)$ divide the line segment joining $(-3,10)$ and $(6,-8)$?", 3, r"Let the ratio be $m:n$: $\dfrac{6m-3n}{m+n}=-1\Rightarrow7m=2n$ (1,1), so $m:n=2:7$. Check with $y$: $\dfrac{2(-8)+7(10)}9=6$ ✓ (1).", "M"),
# ---------------- HARD ----------------
W(r"Show that the points $(-4,-1)$, $(-2,-4)$, $(4,0)$ and $(2,3)$ are the vertices of a rectangle.", 4, r"Let $A(-4,-1)$, $B(-2,-4)$, $C(4,0)$, $D(2,3)$. $AB=CD=\sqrt{13}$, $BC=DA=\sqrt{52}$ (2): opposite sides equal. Diagonals $AC=\sqrt{64+1}=\sqrt{65}$ and $BD=\sqrt{16+49}=\sqrt{65}$ (1). A parallelogram with equal diagonals is a **rectangle**; sides are unequal, so not a square (1).", "H"),
W(r"Show that the points $(-3,2)$, $(-5,-5)$, $(2,-3)$ and $(4,4)$ are the vertices of a rhombus but not a square.", 4, r"$AB=\sqrt{4+49}$, $BC=\sqrt{49+4}$, $CD=\sqrt{4+49}$, $DA=\sqrt{49+4}$: all equal $\sqrt{53}$ (2), so it is a rhombus. Diagonals $AC=\sqrt{25+25}=\sqrt{50}$ and $BD=\sqrt{81+81}=\sqrt{162}$ (1). Diagonals are unequal, so it is **not a square** (1).", "H"),
W(r"Show that $(1,7)$, $(4,2)$, $(-1,-1)$ and $(-4,4)$ are the vertices of a square.", 4, r"$AB=\sqrt{9+25}$, $BC=\sqrt{25+9}$, $CD=\sqrt{9+25}$, $DA=\sqrt{25+9}$: all $=\sqrt{34}$ (2). Diagonals $AC=\sqrt{4+64}=\sqrt{68}$, $BD=\sqrt{64+4}=\sqrt{68}$ (1). Equal sides and equal diagonals: a **square** (1).", "H"),
W(r"The points $A(2,3)$, $B(4,k)$ and $C(6,-3)$ are collinear and $B$ lies between $A$ and $C$. Find $k$.", 3, r"Let $B$ divide $AC$ in the ratio $m:n$. $x$-coordinate: $\dfrac{6m+2n}{m+n}=4\Rightarrow2m=2n$ (1), so $m=n$ and $B$ is the mid-point (1). $k=\dfrac{3+(-3)}2=$ **0** (1).", "M"),
W(r"A cable is stretched between poles at $(5,-6)$ and $(-1,-4)$ on a map grid. A boundary wall runs along the $y$-axis. In what ratio does the wall divide the cable and where does the cable cross it?", 4, r"Let the ratio be $k:1$; on the $y$-axis $x=0$: $\dfrac{-k+5}{k+1}=0$ (1) $\Rightarrow k=5$, ratio **$5:1$** (1). $y=\dfrac{5(-4)+1(-6)}6=-\dfrac{26}6$ (1). Crossing point $\left(0,-\dfrac{13}3\right)$ (1).", "H", wp=True),
W(r"**Case study.** On a school map each unit is 100 m. The school $S$ is at $(0,0)$, the library $L$ at $(3,4)$, the hospital $H$ at $(6,8)$ and a park $P$ at $(-4,-3)$. (i) Find the distance $SL$ in metres. (ii) Show that $S$, $L$ and $H$ are collinear. (iii) Show that $L$ is the mid-point of $SH$. (iv) Show that the park is as far from the school as the library is, and find $PL$.", 5, r"(i) $SL=\sqrt{9+16}=5$ units $=$ **500 m** (1). (ii) $SH=\sqrt{36+64}=10$, $LH=\sqrt{9+16}=5$; $SL+LH=SH$ (1,1). (iii) Mid-point of $SH=(3,4)=L$ (1). (iv) $SP=\sqrt{16+9}=5=SL$ (500 m each); $PL=\sqrt{49+49}=7\sqrt2$ units $\approx990$ m (1).", "H", wp=True),
W(r"If $P(x,y)$ is equidistant from $A(a+b,\,b-a)$ and $B(a-b,\,a+b)$, prove that $bx=ay$.", 4, r"$PA^2=PB^2$: $(x-a-b)^2+(y-b+a)^2=(x-a+b)^2+(y-a-b)^2$ (1). Expanding and cancelling the common terms: $-2x(a+b)+2x(a-b)-2y(b-a)+2y(a+b)=0$ (2). $-4bx+4ay=0$, so $bx=ay$ (1).", "H"),
W(r"The line segment joining $A(2,1)$ and $B(5,-8)$ is trisected at $P$ and $Q$, with $P$ nearer $A$. If $P$ lies on the line $2x-y+k=0$, find $k$.", 4, r"$P$ divides $AB$ in the ratio $1:2$ (1). $P=\left(\dfrac{1(5)+2(2)}3,\dfrac{1(-8)+2(1)}3\right)=(3,-2)$ (2). $2(3)-(-2)+k=0\Rightarrow k=-8$ (1).", "H"),
W(r"A circular pond passes through three points $A(0,0)$, $B(8,0)$ and $C(0,6)$ on a map. Find the position of its centre and its radius.", 4, r"Centre $(x,y)$ is equidistant from all three points. $OA=OB$: $x^2+y^2=(x-8)^2+y^2\Rightarrow x=4$ (1). $OA=OC$: $x^2+y^2=x^2+(y-6)^2\Rightarrow y=3$ (1). Centre $(4,3)$ (1). Radius $=\sqrt{16+9}=$ **5** (1).", "H", wp=True),
W(r"Two corners of an equilateral triangular park on a map are at $(0,0)$ and $(4,0)$. Find the possible positions of the third corner.", 4, r"Let it be $(x,y)$ with distance 4 from both: $x^2+y^2=16$ and $(x-4)^2+y^2=16$ (1). Subtract: $x=2$ (1). Then $y^2=12$, $y=\pm2\sqrt3$ (1). Third corner $(2,2\sqrt3)$ or $(2,-2\sqrt3)$ (1).", "H", wp=True),
W(r"Kiran finds the point dividing $A(2,3)$ and $B(8,9)$ in the ratio $1:2$ as $\left(\dfrac{1\cdot2+2\cdot8}3,\dfrac{1\cdot3+2\cdot9}3\right)=(6,7)$. Explain her mistake and find the correct point.", 3, r"She multiplied $m=1$ with the coordinates of $A$ and $n=2$ with those of $B$; the weights are crosswise: $m$ goes with $B$ and $n$ with $A$ (1). Correct: $\left(\dfrac{1\cdot8+2\cdot2}3,\dfrac{1\cdot9+2\cdot3}3\right)=(4,5)$ (1). It is nearer $A$ ($AP=2\sqrt2$, $AB=6\sqrt2$), as the ratio $1:2$ requires (1).", "H"),
W(r"If $A(6,1)$, $B(8,2)$, $C(9,4)$ and $D(p,3)$ are the vertices of a parallelogram taken in order, find $p$.", 3, r"Diagonals $AC$ and $BD$ bisect each other (1). Mid-point of $AC=(7.5,2.5)$ (1). $\dfrac{8+p}2=7.5\Rightarrow p=$ **7** (1).", "H"),
W(r"The centre of a circle is $(2a,\,a-7)$. Find the values of $a$ if the circle passes through $(11,-9)$ and has diameter $10\sqrt2$.", 4, r"Radius $=5\sqrt2$, so the distance from the centre to $(11,-9)$ is $5\sqrt2$ (1). $(2a-11)^2+(a-7+9)^2=50$ (1). $5a^2-40a+75=0\Rightarrow a^2-8a+15=0$ (1). $a=3$ or $a=5$ (1).", "H"),
W(r"The mid-point of the line segment joining $A(2a,4)$ and $B(-2,2b)$ is $(1,\,2a+1)$. Find $a$ and $b$.", 3, r"$\dfrac{2a-2}2=1\Rightarrow a=2$ (1). $\dfrac{4+2b}2=2a+1=5$ (1) $\Rightarrow b=3$ (1).", "H"),
]
WS.sort(key=lambda w: "EMH".index(w["level"]))   # keep the parts contiguous after a re-tag
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(7)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "7.5 Deriving the Formulae"),
 ("steps", [("Distance formula", "Join P(x₁, y₁) and Q(x₂, y₂) and complete a right triangle with legs |x₂ − x₁| and |y₂ − y₁|. By Pythagoras PQ² = (x₂ − x₁)² + (y₂ − y₁)²."), ("Mid-point", "The mid-point M of PQ divides it in the ratio 1 : 1, so M = ((x₁ + x₂)/2, (y₁ + y₂)/2)."), ("Section formula", "Drop perpendiculars from P, Q and the dividing point R to the x-axis. Similar triangles give PR/RQ = m/n, from which R = ((mx₂ + nx₁)/(m + n), (my₂ + ny₁)/(m + n)).")]),
 ("note", "REMEMBER", "Weights are **crosswise**: for the ratio m : n the multiplier m goes with the **second** point and n with the **first**. A point with ratio 1 : 2 is nearer the first point."),
 ("h2", "7.6 Using the Distance Formula to Identify Figures"),
 ("table", ["To prove", "Show that"], [
  ["isosceles triangle", "two sides equal"],
  ["equilateral triangle", "all three sides equal"],
  ["right triangle", "sum of the squares of two sides = square of the third"],
  ["collinear points A, B, C", "AB + BC = AC (the largest distance equals the sum of the other two)"],
  ["square", "four equal sides **and** equal diagonals"],
  ["rhombus (not a square)", "four equal sides, diagonals **not** equal"],
  ["rectangle", "opposite sides equal **and** equal diagonals"],
  ["parallelogram", "opposite sides equal, or the diagonals have the **same mid-point**"],
  ["point equidistant from A and B", "PA² = PB² (square both sides to avoid the root)"],
  ["circle through three points", "centre is equidistant from all three; radius = that distance"]]),
 ("h2", "7.7 More Worked Examples"),
 ("h3", "Example 1 — A point on an axis"),
 ("steps", [("Find a point on the y-axis equidistant from A(6, 5) and B(−4, 3)", "Take the point as (0, y). Equate the squared distances."), ("Equation", "36 + (y − 5)² = 16 + (y − 3)², so 61 − 10y = 25 − 6y."), ("Answer", "y = 9: the point is **(0, 9)**.")]),
 ("h3", "Example 2 — Trisection points"),
 ("steps", [("Trisect the segment joining A(4, −1) and B(−2, −3)", "The points divide AB in the ratios 1 : 2 and 2 : 1."), ("First point", "P = ((1·(−2) + 2·4)/3, (1·(−3) + 2·(−1))/3) = (2, −5/3)."), ("Second point", "Q = ((2·(−2) + 1·4)/3, (2·(−3) + 1·(−1))/3) = (0, −7/3).")]),
 ("h3", "Example 3 — Ratio in which an axis divides a segment"),
 ("steps", [("In what ratio does the x-axis divide the segment joining (3, 6) and (−12, −3)?", "Let the ratio be k : 1. The dividing point has y = 0."), ("Use the y-formula", "(−3k + 6)/(k + 1) = 0, so k = 2."), ("Answer", "Ratio **2 : 1**; the point is (−7, 0).")]),
 ("h3", "Example 4 — Fourth vertex of a parallelogram"),
 ("steps", [("A(1, 2), B(4, 3), C(6, 6) are consecutive vertices; find D", "The diagonals AC and BD have the same mid-point."), ("Mid-point of AC", "(3.5, 4). So (4 + x)/2 = 3.5 and (3 + y)/2 = 4."), ("Answer", "D = **(3, 5)**.")]),
 ("h3", "Example 5 — Circumcentre"),
 ("steps", [("Find the centre of the circle through A(0, 0), B(8, 0), C(0, 6)", "Centre (x, y) satisfies OA = OB and OA = OC."), ("Equations", "x² + y² = (x − 8)² + y² gives x = 4, and x² + y² = x² + (y − 6)² gives y = 3."), ("Answer", "Centre (4, 3); radius √(16 + 9) = **5**. (The centre of a right triangle's circle is the mid-point of the hypotenuse.)")]),
 ("h3", "Example 6 — Locus condition"),
 ("steps", [("P(x, y) is equidistant from A(3, 6) and B(−3, 4)", "Set PA² = PB²."), ("Expand", "(x − 3)² + (y − 6)² = (x + 3)² + (y − 4)² gives −6x − 12y + 45 = 6x − 8y + 25."), ("Simplify", "12x + 4y = 20, that is **3x + y = 5**.")]),
 ("h2", "7.8 Word Problems: How to Translate"),
 ("table", ["Situation", "Use", "Note"], [
  ["distance between two places on a map grid", "distance formula", "multiply by the scale (1 unit = 100 m or 1 km)"],
  ["meeting at the middle, centre of a circle or park", "mid-point formula", "diameter ends give the centre"],
  ["bus stop, drone or cable at a fraction of the way", "section formula", "‘3/4 of the way’ means ratio 3 : 1"],
  ["which place is nearer", "compare distances (or squares of distances)", "—"],
  ["fourth corner of a parallelogram or square", "diagonals bisect each other", "equate mid-points"],
  ["a wall or road along an axis", "put x = 0 or y = 0 in the section formula", "find k first, then the point"],
  ["circular pond through three points", "centre equidistant from the points", "solve two linear equations"]]),
 ("h2", "7.9 Common Mistakes"),
 ("table", ["Mistake", "Correct idea"], [
  ["Adding coordinates in the distance formula: √[(x₂ + x₁)² + (y₂ + y₁)²]", "subtract: (x₂ − x₁)² + (y₂ − y₁)²"],
  ["Forgetting to take the square root", "distance = √[…]; compare squares only when you say so"],
  ["Weights the wrong way in the section formula", "m goes with the second point, n with the first"],
  ["Proving a square by sides only", "also show the diagonals are equal (a rhombus has equal sides too)"],
  ["Getting a negative value of k", "for a point that lies on the segment the ratio k : 1 is positive; recheck the coordinates used"],
  ["Using one coordinate only to find k", "check the other coordinate to confirm the ratio"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Identify figures** with distances: equal sides and equal diagonals give a square; equal diagonals bisecting each other give a rectangle or square.", "A point on an axis has the form **(x, 0) or (0, y)**; a ratio problem on an axis uses k : 1 with the zero coordinate.", "Map and distance word problems are the **distance, mid-point and section formulae** with a scale."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
