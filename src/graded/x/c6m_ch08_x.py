"""Class 6 Maths Ch 8 Playing with Constructions - extras."""
from common import AR4, Q

AR = [
 AR4("The diameter is the longest chord of a circle.", "A diameter passes through the centre of the circle.", "a",
     "Every chord through the centre has length 2r, and no other chord is longer."),
 AR4("A circle has diameter 14 cm. Its radius is 7 cm.", "The radius of a circle is twice its diameter.", "c",
     "Radius = 14 / 2 = 7, so A is true. The diameter is twice the radius, so R is false."),
 AR4("A point 5 cm from the centre of a circle of radius 4 cm lies inside the circle.", "A point whose distance from the centre is less than the radius lies inside the circle.", "d",
     "5 > 4, so the point lies outside and A is false. R is true."),
 AR4("Each angle of a square is a right angle.", "All four sides of a square are equal.", "b",
     "Both are true, but equal sides do not explain the right angles."),
 AR4("In rectangle ABCD the diagonals meet at O and AC = 10 cm. Then OA = 5 cm.", "The diagonals of a rectangle are equal and bisect each other.", "a",
     "O is the midpoint of AC, so OA = 10 / 2 = 5 cm."),
 AR4("The perpendicular bisector of a segment AB cuts AB at its midpoint at right angles.", "Every point on the perpendicular bisector of AB is at the same distance from A and from B.", "b",
     "Both are true, but the second statement describes a different property."),
]

CASE = [
 Q(r"<b>Case study.</b> Anita draws three concentric circles with centre O and radii 3 cm, 5 cm and 8 cm for a rangoli design. (i) What is the diameter of the smallest circle? (ii) What is the width of the ring between the 5 cm and the 8 cm circles? (iii) What is the length of the longest chord of the largest circle? (iv) A point P is 5 cm from O. Say whether P is inside, on or outside each of the three circles.",
   r"(i) $2\times3=6$ cm (1). (ii) $8-5=3$ cm (1). (iii) The diameter, $2\times8=16$ cm (1). (iv) P is outside the 3 cm circle, on the 5 cm circle and inside the 8 cm circle (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A rectangular garden ABCD has AB = 12 m and BC = 5 m. Its diagonals AC and BD meet at O, and AC = 13 m. (i) What is the length of CD? (ii) What is the length of AD? (iii) Find OA. (iv) Find the length of the diagonal BD and the perimeter of the garden.",
   r"(i) CD $=$ AB $=12$ m (1). (ii) AD $=$ BC $=5$ m (1). (iii) OA $=\frac12\times13=6.5$ m (1). (iv) BD $=$ AC $=13$ m (1); perimeter $=2\times(12+5)=34$ m (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Two villages A and B are shown 8 cm apart on a map. The school must be built at a place that is the same distance from both villages. Ria draws the perpendicular bisector of AB with a compass and a ruler. (i) Which construction does Ria use? (ii) Where does the bisector cut AB and how far is that point from A? (iii) What angle does the bisector make with AB? (iv) Why must the compass opening be more than 4 cm? If the school P on the bisector is 5 cm from A, how far is it from B?",
   r"(i) Perpendicular bisector of a line segment (1). (ii) At the midpoint, 4 cm from A (1). (iii) $90^\circ$ (1). (iv) With an opening of 4 cm or less the arcs from A and B would not cross (1); every point on the bisector is equally far from A and B, so PB = 5 cm (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Circle terms", [r"Centre O; radius $r$ = distance from the centre to any point on the circle.",
   r"Chord: a segment joining two points of the circle. Diameter: a chord through the centre.",
   r"$d=2r$, so $r=\dfrac d2$. The diameter is the longest chord.",
   r"Point at distance $x$ from the centre: inside if $x<r$, on the circle if $x=r$, outside if $x>r$.",
   r"Concentric circles: same centre, different radii. Width of the ring $=R-r$."]),
 ("Rectangle and square", [r"Rectangle: opposite sides equal, all angles $90^\circ$, diagonals equal and bisect each other.",
   r"Square: all sides equal, all angles $90^\circ$, diagonals equal and bisect each other (and cut at right angles).",
   r"If the diagonals meet at O: $OA=OB=OC=OD=\dfrac12\times$ diagonal.",
   r"Perimeter: rectangle $2(l+b)$; square $4a$.   Area: rectangle $l\times b$; square $a^2$."]),
 ("Constructions with compass and ruler", [r"Circle: fix the compass to the radius, put the point at the centre, turn once.",
   r"Perpendicular bisector of AB: open the compass more than half of AB; from A and B draw arcs on both sides; join the crossing points.",
   r"Every point on the perpendicular bisector is equidistant from A and B; it meets AB at its midpoint at $90^\circ$."]),
]

MISTAKES = [
 r"Taking the radius to be twice the diameter; the diameter is twice the radius.",
 r"Choosing a compass opening of half AB or less for a perpendicular bisector, so the arcs do not meet.",
 r"Changing the compass opening between the arcs drawn from A and from B.",
 r"Calling every chord a diameter; only a chord through the centre is a diameter.",
 r"Forgetting that the diagonals of a rectangle are equal and bisect each other, but cut at right angles only in a square.",
]
