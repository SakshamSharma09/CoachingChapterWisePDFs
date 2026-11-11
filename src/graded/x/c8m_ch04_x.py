"""Class 8 Maths Ch 4 Quadrilaterals - extras."""
from common import AR4, Q

AR = [
 AR4(r"The adjacent angles of a parallelogram are supplementary.", r"The opposite sides of a parallelogram are parallel, so adjacent angles are co-interior angles on a transversal.", "a",
     r"Co-interior angles between parallel lines add up to $180^\circ$, which gives A."),
 AR4(r"The diagonals of a rectangle are equal in length.", r"The diagonals of every parallelogram bisect each other.", "b",
     r"Both are true, but bisecting does not give equal lengths; equality follows from the right angles of the rectangle."),
 AR4(r"A parallelogram with one right angle is a rectangle.", r"A parallelogram with equal diagonals is a rhombus.", "c",
     r"A is true (all angles become $90^\circ$). R is false: equal diagonals make a parallelogram a rectangle, not a rhombus."),
 AR4(r"The diagonals of a rhombus are equal.", r"The diagonals of a rhombus bisect each other at right angles.", "d",
     r"A is false (equal diagonals belong to a rectangle or square); R is a true property of the rhombus."),
 AR4(r"If the angles of a quadrilateral are in the ratio $1:2:3:4$, the largest angle is $144^\circ$.", r"The sum of the interior angles of a quadrilateral is $360^\circ$.", "a",
     r"$1+2+3+4=10$ parts, one part $=36^\circ$, largest $=4\times36^\circ=144^\circ$; R is used."),
 AR4(r"A rhombus is a parallelogram.", r"All angles of a rhombus are equal.", "c",
     r"A is true; R is false, as only the opposite angles of a rhombus are equal."),
]

CASE = [
 Q(r"<b>Case study.</b> A carpenter makes a parallelogram-shaped window frame ABCD with $\angle A=70^\circ$, $AB=80$ cm and $BC=50$ cm. The diagonals AC and BD meet at O, with $AC=96$ cm and $BD=60$ cm. "
   r"(i) Find $\angle C$. (ii) Find $\angle B$. (iii) Find the perimeter of the frame. (iv) Find OA and OB, and state the property used.",
   r"(i) Opposite angles are equal, $\angle C=70^\circ$ (1). (ii) $\angle B=180^\circ-70^\circ=110^\circ$ (1). (iii) $2(80+50)=260$ cm (1). (iv) Diagonals of a parallelogram bisect each other, so $OA=48$ cm and $OB=30$ cm (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A rhombus-shaped tile has diagonals of length 16 cm and 12 cm. Another rhombus-shaped tile in the shop has one angle of $64^\circ$. "
   r"(i) At what angle do the diagonals meet? (ii) Find the length of each side of the tile. (iii) Find the perimeter. (iv) Find the other three angles of the second tile and verify that the four angles add up to $360^\circ$.",
   r"(i) $90^\circ$, as diagonals of a rhombus are perpendicular (1). (ii) Half-diagonals 8 cm and 6 cm, side $=\sqrt{8^2+6^2}=10$ cm (1). (iii) $4\times10=40$ cm (1). (iv) Opposite angle $64^\circ$, adjacent angles $116^\circ$ each (1); $64+116+64+116=360$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A plot ABCD in a village has its angles in the ratio $2:3:3:4$ (in order A, B, C, D). The panchayat wants to know the nature of the plot. "
   r"(i) State the sum of the angles of a quadrilateral. (ii) Find the value of one part if the angles are $2x, 3x, 3x, 4x$. (iii) Find the largest angle. (iv) Is the plot a parallelogram? Find a pair of parallel sides, giving reasons.",
   r"(i) $360^\circ$ (1). (ii) $12x=360^\circ$, $x=30^\circ$ (1). (iii) $4x=120^\circ$ (1). (iv) Angles are $60^\circ, 90^\circ, 90^\circ, 120^\circ$; opposite angles A and C are not equal, so it is not a parallelogram (1). $\angle A+\angle D=180^\circ$ so $AB\parallel DC$ (it is a trapezium) (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Quadrilateral", [
   r"Sum of the interior angles of a quadrilateral $=360^\circ$.",
   r"A quadrilateral has 4 sides, 4 angles and 2 diagonals."]),
 ("Parallelogram", [
   r"Opposite sides are parallel and equal; opposite angles are equal.",
   r"Adjacent angles are supplementary (sum $180^\circ$).",
   r"Diagonals bisect each other.",
   r"Perimeter $=2(a+b)$."]),
 ("Rectangle and square", [
   r"Rectangle: parallelogram with all angles $90^\circ$; diagonals are equal.",
   r"Square: rectangle with all sides equal; diagonals are equal and perpendicular bisectors of each other."]),
 ("Rhombus and kite", [
   r"Rhombus: parallelogram with all four sides equal; diagonals bisect each other at $90^\circ$ and bisect the angles.",
   r"Kite: two pairs of adjacent equal sides; one diagonal is the perpendicular bisector of the other and the angles between unequal sides are equal."]),
 ("Trapezium", [
   r"One pair of parallel sides; the angles on the same leg add up to $180^\circ$.",
   r"Isosceles trapezium: non-parallel sides equal, base angles equal, diagonals equal."]),
]

MISTAKES = [
 r"Saying the diagonals of a rhombus are equal, or the diagonals of a rectangle are perpendicular; it is the other way round.",
 r"Treating adjacent angles of a parallelogram as equal; <b>opposite</b> angles are equal and adjacent angles add up to $180^\circ$.",
 r"Forgetting that every square is a rectangle and a rhombus, and every rectangle or rhombus is a parallelogram.",
 r"Using the sum $180^\circ$ (triangle) instead of $360^\circ$ for the interior angles of a quadrilateral.",
 r"Saying a trapezium has two pairs of parallel sides; only one pair is parallel (two pairs make a parallelogram).",
 r"Assuming a quadrilateral with equal diagonals must be a rectangle; the diagonals must also bisect each other, and a parallelogram is needed first.",
]
