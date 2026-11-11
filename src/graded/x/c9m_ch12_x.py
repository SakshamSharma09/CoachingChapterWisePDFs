"""Class 9 Maths Ch 12 Quadrilaterals - extras."""
from common import AR4, Q

AR = [
 AR4(r"The sum of the angles of a quadrilateral is $360^\circ$.", r"A diagonal divides a quadrilateral into two triangles, each with angle sum $180^\circ$.", "a",
     r"$2\times180^\circ=360^\circ$; R is the standard proof."),
 AR4(r"The diagonals of a parallelogram bisect each other.", r"The diagonals of a parallelogram are always equal.", "c",
     r"A is a property of parallelograms; R is false (the diagonals of a non-rectangular parallelogram are unequal)."),
 AR4(r"The diagonals of a rhombus are equal.", r"The diagonals of a rhombus bisect each other at right angles.", "d",
     r"A is false (the diagonals of a rhombus are equal only if it is a square); R is true."),
 AR4(r"Every rectangle is a parallelogram.", r"The diagonals of a rectangle are equal.", "b",
     r"A is true because the opposite sides of a rectangle are parallel; R is true but does not explain A."),
 AR4(r"In $\triangle ABC$, D and E are the midpoints of AB and AC. If $BC=10$ cm, then $DE=5$ cm.", r"The line segment joining the midpoints of two sides of a triangle is parallel to the third side and half of it.", "a",
     r"$DE=\tfrac12BC=5$ cm, directly from the midpoint theorem."),
 AR4(r"In a parallelogram, if one angle is $70^\circ$, then each adjacent angle is $110^\circ$.", r"The adjacent angles of a parallelogram are supplementary.", "a",
     r"$180^\circ-70^\circ=110^\circ$, using R."),
]

CASE = [
 Q(r"<b>Case study.</b> A land surveyor in Nagpur marks a plot ABCD whose four angles are in the ratio $2:3:4:6$. "
   r"(i) What is the sum of the four angles? (ii) Find the value of one part of the ratio. (iii) Find the largest angle. (iv) Is the plot a parallelogram? Give a reason.",
   r"(i) $360^\circ$ (1). (ii) $2+3+4+6=15$ parts, so one part $=\dfrac{360^\circ}{15}=24^\circ$ (1). (iii) $6\times24^\circ=144^\circ$ (1). (iv) The angles are $48^\circ, 72^\circ, 96^\circ, 144^\circ$ (1); a parallelogram has equal opposite angles, but opposite angles such as $48^\circ$ and $96^\circ$ differ, so it is not a parallelogram (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A tile in the shape of a parallelogram PQRS is used in a floor design. $\angle P=65^\circ$, $PQ=8$ cm, $QR=5$ cm. Its diagonals PR and QS meet at O, with $PR=14$ cm and $QS=10$ cm. "
   r"(i) Find $\angle R$. (ii) Find $\angle Q$. (iii) Find the perimeter of the tile. (iv) Find OP and OQ and state the property used.",
   r"(i) Opposite angles are equal, so $\angle R=65^\circ$ (1). (ii) $\angle Q=180^\circ-65^\circ=115^\circ$ (1). (iii) $2(8+5)=26$ cm (1). (iv) $OP=7$ cm and $OQ=5$ cm (1); the diagonals of a parallelogram bisect each other (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A triangular park ABC has $AB=18$ m, $BC=24$ m and $CA=26$ m. A pole D is at the midpoint of AB and a pole E is at the midpoint of AC. A rope is stretched from D to E. "
   r"(i) Find the length of the rope DE. (ii) How is DE related to BC in direction? (iii) Find AD and AE. (iv) Find the perimeter of $\triangle ADE$ and compare it with the perimeter of $\triangle ABC$.",
   r"(i) $DE=\tfrac12\times24=12$ m (1). (ii) DE is parallel to BC (1). (iii) $AD=9$ m, $AE=13$ m (1). (iv) Perimeter of $\triangle ADE=9+13+12=34$ m (1); perimeter of $\triangle ABC=18+24+26=68$ m, so it is half (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Angle sum", [r"Sum of the angles of a quadrilateral $=360^\circ$ (a diagonal splits it into two triangles)."]),
 ("Parallelogram", [r"Opposite sides are parallel and equal; opposite angles are equal; adjacent angles are supplementary ($180^\circ$).",
   r"Diagonals bisect each other (but are not equal in general).",
   r"A quadrilateral with one pair of opposite sides equal and parallel is a parallelogram; so is one whose diagonals bisect each other.",
   r"Area $=$ base $\times$ height; perimeter $=2(a+b)$."]),
 ("Special parallelograms", [r"Rectangle: all angles $90^\circ$; diagonals equal and bisect each other.",
   r"Rhombus: all sides equal; diagonals bisect each other at right angles; side $=\sqrt{\left(\tfrac{d_1}2\right)^2+\left(\tfrac{d_2}2\right)^2}$; area $=\tfrac12d_1d_2$.",
   r"Square: all sides equal, all angles $90^\circ$, diagonals equal and perpendicular, bisecting each other.",
   r"Rectangle diagonal $=\sqrt{l^2+b^2}$; square diagonal $=a\sqrt2$."]),
 ("Midpoint theorem", [r"In $\triangle ABC$, if D and E are the midpoints of AB and AC, then $DE\parallel BC$ and $DE=\tfrac12BC$.",
   r"Converse: a line through the midpoint of one side parallel to the second side bisects the third side.",
   r"The triangle cut off by the midpoint segment has half the perimeter of the original triangle."]),
]

MISTAKES = [
 r"Saying the diagonals of every parallelogram are equal; that holds only for a rectangle (and square).",
 r"Saying the diagonals of a rhombus are equal; they are perpendicular bisectors of each other, equal only in a square.",
 r"Taking adjacent angles of a parallelogram to be equal; they add up to $180^\circ$ and the <i>opposite</i> angles are equal.",
 r"Using the full diagonals instead of half-diagonals when finding the side of a rhombus with the Pythagoras theorem.",
 r"In the midpoint theorem, writing $DE=2BC$ or $DE=\tfrac12AB$; the segment is half the <i>third</i> side that it is parallel to.",
 r"Forgetting that a quadrilateral's angles must add up to $360^\circ$ (not $180^\circ$) when solving for $x$.",
]
