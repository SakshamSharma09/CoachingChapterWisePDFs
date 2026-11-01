import random
from lib import mcq, Q, OR
from mk9 import M4, build
R = random.Random(901)
def P(x, y): return f"({x},\\,{y})"
def rt(n):
    r = int(round(n ** .5))
    return str(r) if r * r == n else f"\\sqrt{{{n}}}"

A = []; B = []; C = []; D = []

# ---- A: quadrants (6)
for x, y in [(-3, 5), (4, -7), (-6, -2), (8, 1), (0, -4), (-5, 0)]:
    if x == 0: ans, why = "on the $y$-axis", "$x=0$, so the point lies on the $y$-axis"
    elif y == 0: ans, why = "on the $x$-axis", "$y=0$, so the point lies on the $x$-axis"
    else:
        qd = {(1, 1): "Quadrant I", (-1, 1): "Quadrant II", (-1, -1): "Quadrant III", (1, -1): "Quadrant IV"}[(1 if x > 0 else -1, 1 if y > 0 else -1)]
        ans, why = qd, f"signs of $(x,y)$ are $({'+' if x>0 else '−'},{'+' if y>0 else '−'})$"
    pool = ["Quadrant I", "Quadrant II", "Quadrant III", "Quadrant IV", "on the $x$-axis", "on the $y$-axis"]
    A.append(M4(f"The point ${P(x,y)}$ lies:", ans, [o for o in pool if o != ans][:3] if x and y else [o for o in pool[:4]], why))
# ---- A: distance (7)
for (x1, y1, x2, y2) in [(1, 2, 4, 6), (-2, 3, 3, -9), (0, 0, 6, 8), (5, 1, -7, 6), (-4, -3, 4, 3), (2, -1, 10, 14), (-1, -1, 4, 11)]:
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5; d = int(round(d))
    A.append(M4(f"The distance between $A{P(x1,y1)}$ and $B{P(x2,y2)}$ is:", f"{d} units", [f"{d+1} units", f"{d-1} units", f"{d+2} units"],
                f"$\\sqrt{{({x2}-({x1}))^2+({y2}-({y1}))^2}}=\\sqrt{{{(x2-x1)**2}+{(y2-y1)**2}}}={d}$"))
# ---- A: midpoint (5)
def hf(v): return str(v//2) if v % 2 == 0 else f"{v/2:g}"
for (x1, y1, x2, y2) in [(2, 4, 6, 10), (-3, 5, 7, -1), (0, -8, 6, 0), (5, 9, -1, -3), (-6, -2, 2, 8)]:
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    A.append(M4(f"The midpoint of the segment joining $A{P(x1,y1)}$ and $B{P(x2,y2)}$ is:", f"$({mx:g},\\,{my:g})$",
                [f"$({(x1+x2):g},\\,{(y1+y2):g})$", f"$({mx:g},\\,{-my:g})$", f"$({(x2-x1)/2:g},\\,{(y2-y1)/2:g})$", f"$({mx+1:g},\\,{my+1:g})$"], f"$\\left(\\frac{{{x1}+({x2})}}2,\\frac{{{y1}+({y2})}}2\\right)$"))
# ---- A: missing endpoint (3)
for (mx, my, ax, ay) in [(3, 2, 1, -4), (-1, 4, 5, 6), (0, 0, -3, 7)]:
    bx, by = 2 * mx - ax, 2 * my - ay
    A.append(M4(f"$M{P(mx,my)}$ is the midpoint of $AB$ and $A{P(ax,ay)}$. The coordinates of $B$ are:", f"$({bx},\\,{by})$",
                [f"$({mx-ax},\\,{my-ay})$", f"$({bx},\\,{-by})$", f"$({ax+mx},\\,{ay+my})$", f"$({bx+1},\\,{by+1})$"], f"$B=(2x_M-x_A,\\,2y_M-y_A)$"))
# ---- A: distance from origin / axes (4)
for (x, y) in [(6, -8), (-5, 12), (9, 12), (-8, -15)]:
    d = int(round((x*x + y*y) ** .5))
    A.append(M4(f"The distance of the point ${P(x,y)}$ from the origin is:", f"{d} units", [f"{abs(x)+abs(y)} units", f"{d+1} units", f"{abs(x)} units"], f"$\\sqrt{{{x*x}+{y*y}}}={d}$"))
# ---- A: reflections / axes (4)
for (x, y) in [(3, -4), (-2, 6), (5, 7), (-8, -1)]:
    A.append(M4(f"The reflection of the point ${P(x,y)}$ in the $y$-axis is:", f"$({-x},\\,{y})$", [f"$({x},\\,{-y})$", f"$({-x},\\,{-y})$", f"$({y},\\,{x})$"], "reflection in the $y$-axis changes the sign of the $x$-coordinate"))
# ---- A: hand-written (11)
A += [
 M4(r"The coordinates of the origin are:", r"$(0,\,0)$", [r"$(1,\,1)$", r"$(0,\,1)$", r"$(1,\,0)$"], "intersection of the axes"),
 M4(r"A point lies on the $x$-axis. Its $y$-coordinate is:", "0", ["1", "equal to its $x$-coordinate", "negative"], "every point on the $x$-axis has $y=0$"),
 M4(r"A point lies on the $y$-axis at distance 5 units below the origin. Its coordinates are:", r"$(0,\,-5)$", [r"$(-5,\,0)$", r"$(5,\,0)$", r"$(0,\,5)$"], "$x=0$, and below the origin means $y<0$"),
 M4(r"The point $(a,\,b)$ coincides with the point $(b,\,a)$ if and only if:", r"$a=b$", [r"$a=-b$", r"$a=0$", r"$a+b=0$"], "the coordinates are equal in order only when $a=b$"),
 M4(r"The $x$-coordinate of a point is its perpendicular distance from the:", r"$y$-axis (measured along the $x$-axis)", [r"$x$-axis", r"origin", r"line $y=x$"], "definition of abscissa"),
 M4(r"Which of the following points does not lie in Quadrant II?", r"$(4,\,-4)$", [r"$(-4,\,4)$", r"$(-1,\,9)$", r"$(-7,\,2)$"], "Quadrant II needs $x<0,\\ y>0$"),
 M4(r"The three points $O(0,0)$, $A(3,4)$ and $B(-3,-4)$:", "are collinear", ["form an isosceles triangle", "form a right triangle", "form an equilateral triangle"], "$O$ is the midpoint of $AB$"),
 M4(r"A student says: “The points $(2,\,3)$ and $(3,\,2)$ are the same point.” The correct response is:", r"False; they are different because $(x,y)\ne(y,x)$ when $x\ne y$", ["True", "True only in Quadrant I", "True if they are on the same line"], "order of coordinates matters"),
 M4(r"Two vertices of a rectangle are $(1,\,2)$ and $(5,\,2)$ and one side has length 3 above the $x$-axis. The other two vertices are:", r"$(1,\,5)$ and $(5,\,5)$", [r"$(1,\,3)$ and $(5,\,3)$", r"$(4,\,2)$ and $(8,\,2)$", r"$(1,\,-1)$ and $(5,\,-1)$"], "shift vertically by 3"),
 M4(r"The distance of the point $(-7,\,4)$ from the $x$-axis is:", "4 units", ["7 units", "−4 units", "11 units"], "distance from the $x$-axis is $|y|$"),
 M4(r"The point $(3,\,0)$ is reflected in the $x$-axis. Its image is:", r"$(3,\,0)$", [r"$(-3,\,0)$", r"$(0,\,3)$", r"$(0,\,-3)$"], "a point on the axis is its own reflection"),
]
assert len(A) == 40, len(A)

# ---- B (16): 2 marks
for (x1, y1, x2, y2) in [(2, 3, 5, 7), (-1, 2, 4, -10), (0, 5, 12, 0), (-3, -3, 5, 3)]:
    d = int(round(((x2-x1)**2 + (y2-y1)**2) ** .5))
    B.append(Q(f"Find the distance between $A{P(x1,y1)}$ and $B{P(x2,y2)}$.", f"$AB=\\sqrt{{({x2}-({x1}))^2+({y2}-({y1}))^2}}=\\sqrt{{{(x2-x1)**2}+{(y2-y1)**2}}}=\\sqrt{{{d*d}}}=\\mathbf{{{d}}}$ units", "1+1"))
for (x1, y1, x2, y2) in [(4, 6, 10, -2), (-5, 3, 1, 9), (7, -4, -3, 2), (0, 0, -8, 10)]:
    B.append(Q(f"Find the coordinates of the midpoint of the segment joining $P{P(x1,y1)}$ and $Q{P(x2,y2)}$.", f"Midpoint $=\\left(\\frac{{{x1}+({x2})}}2,\\frac{{{y1}+({y2})}}2\\right)=\\mathbf{{({(x1+x2)/2:g},\\,{(y1+y2)/2:g})}}$", "1+1"))
B += [
 Q(r"Write the coordinates of the vertices of a rectangle with one vertex at the origin, length 7 units along the $x$-axis and breadth 4 units along the $y$-axis (in Quadrant I).", r"$O(0,0),\ A(7,0),\ B(7,4),\ C(0,4)$", "2"),
 Q(r"In which quadrant (or on which axis) do the points $(-2,\,5)$, $(6,\,-3)$, $(0,\,-4)$ and $(-1,\,-1)$ lie?", r"$(-2,5)$: Quadrant II; $(6,-3)$: Quadrant IV; $(0,-4)$: on the $y$-axis; $(-1,-1)$: Quadrant III", "½ × 4"),
 Q(r"Show that the points $A(1,\,1)$, $B(3,\,3)$ and $C(5,\,5)$ are collinear using distances.", r"$AB=\sqrt{4+4}=2\sqrt2,\ BC=2\sqrt2,\ AC=\sqrt{16+16}=4\sqrt2$. Since $AB+BC=AC$, the points are collinear.", "1+1"),
 Q(r"The midpoint of $AB$ is $M(2,\,-1)$ and $A=(-4,\,3)$. Find $B$.", r"$\frac{-4+x}2=2\Rightarrow x=8;\ \frac{3+y}2=-1\Rightarrow y=-5$. So $B=(8,\,-5)$", "1+1"),
 Q(r"Is the point $(-5,\,-12)$ at the same distance from the origin as $(13,\,0)$? Justify.", r"Distance of $(-5,-12)$ is $\sqrt{25+144}=13$; distance of $(13,0)$ is 13. Yes, both lie on the circle of radius 13 centred at the origin.", "1+1"),
 Q(r"The points $A(2,\,0)$, $B(0,\,2)$ and $C(-2,\,0)$ are joined to form a triangle. Name the type of triangle with reason.", r"$AB=\sqrt{4+4}=2\sqrt2,\ BC=2\sqrt2,\ AC=4$. $AB=BC$, and $AB^2+BC^2=8+8=16=AC^2$: a right-angled isosceles triangle.", "1+1"),
 Q(r"Write the coordinates of the point on the $y$-axis that is 6 units above the origin and of the point on the $x$-axis that is 4 units to the left of the origin. Find the distance between them.", r"$(0,6)$ and $(-4,0)$; distance $=\sqrt{16+36}=\sqrt{52}=2\sqrt{13}$ units.", "1+1"),
 Q(r"Check whether $P(1,\,0)$ is equidistant from $A(2,\,3)$ and $B(4,\,-1)$.", r"$PA^2=1+9=10$; $PB^2=9+1=10$. Yes, $P$ is equidistant.", "1+1"),
]
assert len(B) == 16, len(B)

# ---- C (24): 3 marks
def tri_case(i):
    pts = [((0, 0), (6, 0), (3, 4)), ((1, 1), (7, 1), (4, 5)), ((-2, 0), (4, 0), (1, 4)), ((2, 3), (8, 3), (5, 7))][i]
    return pts
for (a, b, c) in [((0, 0), (6, 0), (3, 4)), ((1, 1), (7, 1), (4, 5)), ((-2, 0), (4, 0), (1, 4)), ((2, 3), (8, 3), (5, 7))]:
    AB = ((b[0]-a[0])**2 + (b[1]-a[1])**2) ** .5; AC = ((c[0]-a[0])**2 + (c[1]-a[1])**2) ** .5; BC = ((c[0]-b[0])**2 + (c[1]-b[1])**2) ** .5
    C.append(Q(f"Show that the triangle with vertices $A{P(*a)}$, $B{P(*b)}$, $C{P(*c)}$ is isosceles.",
               f"$AB=\\sqrt{{{(b[0]-a[0])**2}+{(b[1]-a[1])**2}}}={AB:g}$; $AC=\\sqrt{{{(c[0]-a[0])**2}+{(c[1]-a[1])**2}}}={AC:g}$; $BC=\\sqrt{{{(c[0]-b[0])**2}+{(c[1]-b[1])**2}}}={BC:g}$. Two sides ($AC=BC={AC:g}$) are equal, so the triangle is isosceles.", "1+1+1"))
for (a, b, c, d) in [((0, 0), (4, 0), (4, 3), (0, 3)), ((1, 1), (5, 1), (5, 4), (1, 4)), ((-2, -1), (3, -1), (3, 2), (-2, 2)), ((0, 2), (6, 2), (6, 7), (0, 7))]:
    w = b[0]-a[0]; h = c[1]-b[1]
    C.append(Q(f"Show that $A{P(*a)}$, $B{P(*b)}$, $C{P(*c)}$, $D{P(*d)}$ are the vertices of a rectangle.",
               f"$AB={w}=DC$, $BC={h}=AD$ (opposite sides equal). Diagonals $AC=BD=\\sqrt{{{w*w}+{h*h}}}={rt(w*w+h*h)}$ (equal). A parallelogram with equal diagonals is a rectangle.", "1+1+1"))
for (a, b) in [((2, 5), (11, 14)), ((-4, 1), (8, 7))]:
    P1 = (a[0] + (b[0]-a[0])/3, a[1] + (b[1]-a[1])/3); P2 = (a[0] + 2*(b[0]-a[0])/3, a[1] + 2*(b[1]-a[1])/3)
    C.append(Q(f"Find the coordinates of the points of trisection of the segment joining $A{P(*a)}$ and $B{P(*b)}$.",
               f"Let $P$ be nearer $A$. $P=\\left(\\frac{{2({a[0]})+{b[0]}}}3,\\frac{{2({a[1]})+{b[1]}}}3\\right)=({P1[0]:g},{P1[1]:g})$; $Q=\\left(\\frac{{{a[0]}+2({b[0]})}}3,\\frac{{{a[1]}+2({b[1]})}}3\\right)=({P2[0]:g},{P2[1]:g})$", "1+1+1"))
C += [
 Q(r"The midpoints of the sides of a triangle are $D(5,\,1)$, $E(6,\,5)$ and $F(0,\,3)$. Find the vertices.", r"Sum of coordinates: if $A,B,C$ are vertices with $D$ mid of $BC$ etc., then $A=E+F-D=(1,7)$, $B=D+F-E=(-1,-1)$, $C=D+E-F=(11,3)$. Check: midpoint of $BC=(5,1)=D$ ✓", "1+1+1"),
 Q(r"Show that the points $M(-3,\,-4)$, $A(0,\,0)$ and $G(6,\,8)$ are collinear.", r"$MA=\sqrt{9+16}=5$, $AG=\sqrt{36+64}=10$, $MG=\sqrt{81+144}=15$. $MA+AG=MG$ ⇒ collinear.", "1+1+1"),
 Q(r"Show that $R(-5,\,-1)$, $B(-2,\,-5)$ and $C(4,\,-12)$ are not collinear.", r"$RB=\sqrt{9+16}=5$; $BC=\sqrt{36+49}=\sqrt{85}$; $RC=\sqrt{81+121}=\sqrt{202}$. $(RB+BC)^2=25+85+10\sqrt{85}=110+10\sqrt{85}\ne202=RC^2$, so $RB+BC\ne RC$. Hence the points are not collinear.", "1+1+1"),
 Q(r"Triangle $ADM$ has vertices $A(3,4)$, $D(7,1)$, $M(9,6)$. It is reflected in the $y$-axis. Write the image vertices and show that $A'D'=AD$.", r"$A'(-3,4),\ D'(-7,1),\ M'(-9,6)$. $AD=\sqrt{16+9}=5$; $A'D'=\sqrt{(-7+3)^2+(1-4)^2}=\sqrt{16+9}=5$. Reflection preserves lengths.", "1+1+1"),
 Q(r"Find a point on the $y$-axis equidistant from $A(6,\,5)$ and $B(-4,\,3)$.", r"Let $P(0,y)$. $PA^2=36+(y-5)^2$, $PB^2=16+(y-3)^2$. $36+y^2-10y+25=16+y^2-6y+9\Rightarrow 61-10y=25-6y\Rightarrow y=9$. $P=(0,9)$", "1+1+1"),
 Q(r"Show that the point $(0,\,-1)$ is equidistant from $(-4,\,3)$ and $(4,\,3)$. Hence name the type of triangle formed by the three points, with reason.", r"Distances: $\sqrt{16+16}=4\sqrt2$ from each. The three points form an isosceles triangle with the apex at $(0,-1)$; base $=8$ and $64=32+32$, so it is also right-angled at the apex.", "1+1+1"),
 Q(r"The points $(1,\,-8)$, $(-4,\,7)$ and $(-7,\,-4)$ lie on a circle with centre at the origin. Find its radius and say whether $(-5,\,6)$ lies inside, on or outside the circle.", r"Radius $=\sqrt{1+64}=\sqrt{65}$ (check $16+49=65$, $49+16=65$ ✓). $OD^2=25+36=61<65$ ⇒ $(-5,6)$ lies <b>inside</b> the circle.", "1+1+1"),
 Q(r"Find the coordinates of the fourth vertex of a parallelogram $ABCD$ with $A(1,\,2)$, $B(4,\,3)$, $C(6,\,6)$.", r"Diagonals bisect each other: midpoint of $AC=(3.5,4)$. If $D=(x,y)$ then $\frac{4+x}2=3.5\Rightarrow x=3$, $\frac{3+y}2=4\Rightarrow y=5$. $D=(3,5)$", "1+1+1"),
 Q(r"A school ground is plotted on a grid with the flag-post at $F(0,0)$, the main gate at $G(8,0)$ and the library at $L(0,6)$. Find the distance between the gate and the library and the midpoint of the gate–library path.", r"$GL=\sqrt{64+36}=10$ units; midpoint $=(4,3)$.", "2+1"),
 Q(r"Find the perimeter of the triangle with vertices $(0,\,0)$, $(4,\,0)$ and $(4,\,3)$.", r"Sides: 4, 3 and $\sqrt{16+9}=5$. Perimeter $=12$ units.", "2+1"),
 Q(r"Three vertices of a rectangle are $(2,\,1)$, $(8,\,1)$ and $(8,\,5)$. Find the fourth vertex and the length of the diagonal.", r"Fourth vertex $(2,5)$. Diagonal $=\sqrt{36+16}=2\sqrt{13}$ units.", "1+2"),
 Q(r"Given $A(2,\,-2)$ and $B(8,\,4)$, find the point $P$ on $AB$ that divides it in the ratio $1:2$ (nearer to $A$) and verify that $AP=\frac13AB$.", r"$P=\left(\frac{2(2)+8}3,\frac{2(-2)+4}3\right)=(4,0)$. $AP=\sqrt{4+4}=2\sqrt2$; $AB=\sqrt{36+36}=6\sqrt2$; $AP=\frac13AB$ ✓", "2+1"),
 Q(r"Find the length of the hypotenuse and the area of the triangle with vertices $O(0,0)$, $A(6,0)$ and $B(0,8)$.", r"Right angle at $O$. Hypotenuse $AB=\sqrt{36+64}=10$ units (1½). Area $=\frac12\times6\times8=24$ sq. units (1½).", "1½+1½"),
 Q(r"Show that $A(3,\,0)$, $B(6,\,4)$ and $C(-1,\,3)$ are the vertices of an isosceles right-angled triangle.", r"$AB=\sqrt{9+16}=5$, $AC=\sqrt{16+9}=5$, $BC=\sqrt{49+1}=\sqrt{50}$. $AB=AC$ (isosceles) and $AB^2+AC^2=50=BC^2$ (right angle at $A$).", "1+1+1"),
]
assert len(C) == 24, len(C)

# ---- D (16): 5 marks
D += [
 Q(r"<b>Case study:</b> A city has two main roads crossing at the centre, N–S and E–W. All other streets are parallel and 200 m apart, with 10 streets in each direction. A street intersection is named $(a,b)$ if the $a$-th N–S street meets the $b$-th E–W street. (i) How many intersections are there in all? (ii) How far apart are the crossings $(2,3)$ and $(6,3)$? (iii) Find the straight-line distance between $(2,3)$ and $(6,6)$ in metres.", r"(i) $10\times10=100$ intersections. (ii) Same E–W street; $6-2=4$ blocks apart ⇒ $4\times200=800$ m. (iii) Shifts: $4\times200=800$ m and $3\times200=600$ m ⇒ $\sqrt{800^2+600^2}=1000$ m.", "1+2+2"),
 Q(r"(i) Find the distance between $P(-2,\,3)$ and $Q(4,\,-5)$. (ii) Hence find the midpoint of $PQ$ and verify that it is equidistant from $P$ and $Q$.", r"(i) $PQ=\sqrt{36+64}=10$. (ii) $M=(1,-1)$. $MP=\sqrt{9+16}=5$, $MQ=\sqrt{9+16}=5$. Each $=\frac12PQ$ ✓", "2+3"),
 Q(r"Show that the points $A(1,7)$, $B(4,2)$, $C(-1,-1)$ and $D(-4,4)$ are the vertices of a square.", r"$AB=\sqrt{9+25}=\sqrt{34}$, $BC=\sqrt{25+9}=\sqrt{34}$, $CD=\sqrt{9+25}=\sqrt{34}$, $DA=\sqrt{25+9}=\sqrt{34}$ (all sides equal). $AC=\sqrt{4+64}=\sqrt{68}$, $BD=\sqrt{64+4}=\sqrt{68}$ (diagonals equal). Rhombus with equal diagonals ⇒ square.", "3+2"),
 Q(r"<b>Case study:</b> On a grid map of a school, the library is at $L(2,\,3)$, the canteen at $C(8,\,3)$ and the playground gate at $G(5,\,7)$ (units in 10 m). (i) Show that $LG=CG$. (ii) Find the midpoint of $LC$ (the shaded sitting area). (iii) Find the distance from $G$ to this midpoint and state what it represents.", r"(i) $LG=\sqrt{9+16}=5$, $CG=\sqrt{9+16}=5$ ✓. (ii) $M=(5,3)$. (iii) $GM=4$ units $=40$ m; it is the altitude to the base $LC$ of the isosceles triangle $LGC$.", "1+2+2"),
 Q(r"Show that the points $A(-3,\,-4)$, $B(0,\,0)$, $C(3,\,4)$ lie on a straight line, and find the ratio in which $B$ divides $AC$.", r"$AB=5$, $BC=5$, $AC=10$ ⇒ $AB+BC=AC$ (collinear). $B$ is the midpoint ⇒ ratio $1:1$.", "3+2"),
 Q(r"The vertices of a triangle are $A(0,\,0)$, $B(8,\,0)$, $C(4,\,6)$. (i) Find the lengths of the sides and state its type. (ii) Find the midpoints $D,E,F$ of $BC,CA,AB$ and the perimeter of triangle $DEF$.", r"(i) $AB=8$, $AC=BC=\sqrt{16+36}=2\sqrt{13}$ ⇒ isosceles. (ii) $D(6,3)$, $E(2,3)$, $F(4,0)$; $DE=4$, $EF=\sqrt{4+9}=\sqrt{13}$, $FD=\sqrt{4+9}=\sqrt{13}$. Perimeter $=4+2\sqrt{13}$ (half of that of $ABC$).", "2+3"),
 Q(r"Find the coordinates of the centre of the circle passing through $A(0,0)$, $B(6,0)$ and $C(0,8)$ and its radius.", r"Angle at $A$ is a right angle, so $BC$ is a diameter. Centre $=$ midpoint of $BC=(3,4)$; radius $=\frac12\sqrt{36+64}=5$.", "3+2"),
 Q(r"Plot (describe) the points $A(-3,\,2)$, $B(1,\,2)$, $C(1,\,-4)$, $D(-3,\,-4)$. (i) Name the figure. (ii) Find its area and the length of the diagonal. (iii) Write the coordinates of its centre.", r"(i) Rectangle. (ii) $AB=4$, $BC=6$; area $=24$ sq. units; diagonal $=\sqrt{16+36}=2\sqrt{13}$. (iii) Centre $=(-1,-1)$.", "1+2+2"),
]
D += [
 Q(r"Show that the points $A(2,\,-2)$, $B(-2,\,1)$ and $C(5,\,2)$ are the vertices of a right-angled triangle. Find its area.", r"$AB^2=16+9=25$; $BC^2=49+1=50$; $AC^2=9+16=25$. $AB^2+AC^2=BC^2$ ⇒ right angle at $A$. Area $=\frac12\times5\times5=12.5$ sq. units.", "3+2"),
 Q(r"<b>Case study:</b> A drone flies from the point $A(1,2)$ to $B(7,10)$ and then to $C(7,2)$ (units in 100 m). (i) Find the distance flown from $A$ to $B$. (ii) Find the total distance $A\to B\to C$. (iii) How much shorter is the direct path $A\to C$?", r"(i) $AB=\sqrt{36+64}=10$ ⇒ 1000 m. (ii) $BC=8$; total $=18$ units $=1800$ m. (iii) $AC=6$ ⇒ saves $18-6=12$ units $=1200$ m.", "2+2+1"),
 Q(r"Show that $(-4,\,-7)$, $(-1,\,2)$, $(8,\,5)$ and $(5,\,-4)$ are the vertices of a rhombus. Find its area using the diagonals.", r"Sides: $\sqrt{9+81}=\sqrt{90}$ each (check $\sqrt{81+9}=\sqrt{90}$, $\sqrt{9+81}$, $\sqrt{81+9}$). Diagonals: $\sqrt{144+144}=12\sqrt2$ and $\sqrt{36+36}=6\sqrt2$. Area $=\frac12\times12\sqrt2\times6\sqrt2=72$ sq. units.", "3+2"),
 Q(r"Find the point on the $x$-axis which is equidistant from $(-2,\,5)$ and $(2,\,-3)$, and find the common distance.", r"Let $P(x,0)$: $(x+2)^2+25=(x-2)^2+9\Rightarrow 8x=-16\Rightarrow x=-2$. $P(-2,0)$; distance $=\sqrt{0+25}=5$.", "3+2"),
 Q(r"The vertices of $\triangle ABC$ are $A(-2,\,0)$, $B(2,\,0)$ and $C(0,\,2)$, and those of $\triangle PQR$ are $P(-4,0)$, $Q(4,0)$, $R(0,4)$. Show that $\triangle ABC\sim\triangle PQR$ by finding the ratios of the sides.", r"$AB=4$, $BC=\sqrt{4+4}=2\sqrt2$, $CA=2\sqrt2$; $PQ=8$, $QR=\sqrt{16+16}=4\sqrt2$, $RP=4\sqrt2$. Ratios $\frac{AB}{PQ}=\frac{BC}{QR}=\frac{CA}{RP}=\frac12$ ⇒ similar.", "3+2"),
 Q(r"Find the value(s) of $k$ if the distance between $(k,\,2)$ and $(3,\,-4)$ is 10 units, and write the corresponding points.", r"$(k-3)^2+36=100\Rightarrow(k-3)^2=64\Rightarrow k=11$ or $k=-5$. Points $(11,2)$ and $(-5,2)$.", "3+2"),
 Q(r"<b>Case study:</b> A rectangular garden $OABC$ has $O(0,0)$, $A(12,0)$, $B(12,8)$, $C(0,8)$. A fountain is at the centre $F$, and lamps $L_1(0,4)$, $L_2(12,4)$. (i) Find the centre. (ii) Show $FL_1=FL_2$. (iii) Find the area of the garden and the distance between $O$ and $B$.", r"(i) $F=(6,4)$. (ii) $FL_1=6=FL_2$ ✓. (iii) Area $=96$ sq. units; $OB=\sqrt{144+64}=\sqrt{208}=4\sqrt{13}$ units.", "1+2+2"),
 Q(r"In $\triangle ABC$, $A=(1,\,2)$ and $B=(4,\,6)$. Find the midpoint $M$ of $AB$ and the length of the median $CM$, where $C=(7,\,2)$.", r"$M=(2.5,4)$. $CM=\sqrt{(7-2.5)^2+(2-4)^2}=\sqrt{20.25+4}=\frac{\sqrt{97}}2\approx4.92$ units.", "2+3"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
