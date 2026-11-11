"""Class 7 Maths Ch 5 Parallel and Intersecting Lines - extras."""
from common import AR4, Q

AR = [
 AR4(r"The complement of $35^\circ$ is $55^\circ$.", r"Two angles are complementary if their sum is $90^\circ$.", "a",
     "90 - 35 = 55."),
 AR4("The two angles of a linear pair are supplementary.", "Vertically opposite angles are equal.", "b",
     "Both are true, but equality of vertically opposite angles does not explain the linear pair."),
 AR4("Vertically opposite angles are equal.", r"Vertically opposite angles always add up to $180^\circ$.", "c",
     "A is true. Vertically opposite angles are equal, they do not always add up to 180 degrees, so R is false."),
 AR4("When a transversal cuts two parallel lines, the corresponding angles are supplementary.", "When a transversal cuts two parallel lines, the corresponding angles are equal.", "d",
     "Corresponding angles are equal, so A is false and R is true."),
 AR4(r"A transversal cuts two lines making alternate interior angles of $65^\circ$ each. The lines are parallel.", "If a pair of alternate interior angles is equal, the two lines are parallel.", "a",
     "R is the test for parallel lines."),
 AR4(r"The angles of a linear pair are $110^\circ$ and $70^\circ$.", r"The sum of all angles around a point is $360^\circ$.", "b",
     "110 + 70 = 180. Both true, but R does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Two railway tracks are parallel. A road crosses them and acts as a transversal. At the first crossing, one of the angles is $65^\circ$. (i) What is the corresponding angle at the second crossing? (ii) What is the alternate interior angle? (iii) What is the angle on the same side of the transversal, between the tracks (same-side interior angle)? (iv) Of the eight angles formed, how many measure $65^\circ$ and how many measure $115^\circ$?",
   r"(i) $65^\circ$ (1). (ii) $65^\circ$ (1). (iii) $180^\circ-65^\circ=115^\circ$ (1). (iv) Four angles are $65^\circ$ (1) and four angles are $115^\circ$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Two roads cross at a point O, forming four angles. One of the angles is $40^\circ$. (i) What is the angle vertically opposite to it? (ii) What is the angle adjacent to it? (iii) What is the sum of the four angles? (iv) In another crossing, two adjacent angles are $(2x+10)^\circ$ and $(3x-20)^\circ$. Find $x$ and the two angles.",
   r"(i) $40^\circ$ (1). (ii) $180^\circ-40^\circ=140^\circ$ (1). (iii) $360^\circ$ (1). (iv) They form a linear pair, so $5x-10=180$ and $x=38$ (1); the angles are $86^\circ$ and $94^\circ$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A ladder leans against a vertical wall. It makes an angle of $70^\circ$ with the horizontal ground. The wall makes $90^\circ$ with the ground. (i) What is the angle between the ladder and the wall? (ii) What is the supplement of $70^\circ$? (iii) Are $40^\circ$ and $50^\circ$ complementary? (iv) An angle is $20^\circ$ more than its complement. Find the angle and its complement.",
   r"(i) $90^\circ-70^\circ=20^\circ$ (1). (ii) $180^\circ-70^\circ=110^\circ$ (1). (iii) Yes, because $40^\circ+50^\circ=90^\circ$ (1). (iv) Let the angle be $x$: $x=(90-x)+20$ gives $x=55^\circ$ (1); its complement is $35^\circ$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Pairs of angles", [r"Complementary angles: sum $=90^\circ$; the complement of $x$ is $90^\circ-x$.",
   r"Supplementary angles: sum $=180^\circ$; the supplement of $x$ is $180^\circ-x$.",
   r"Linear pair: two adjacent angles on a straight line; they are supplementary.",
   r"Angles around a point: sum $=360^\circ$."]),
 ("Intersecting lines", [r"Two lines crossing form four angles; vertically opposite angles are equal.",
   r"Adjacent angles at the crossing form a linear pair: sum $=180^\circ$."]),
 ("Parallel lines and a transversal", [r"A transversal is a line that cuts two (or more) lines at different points and forms eight angles.",
   r"If the lines are parallel: corresponding angles are equal; alternate interior angles are equal; same-side interior angles add up to $180^\circ$.",
   r"Of the eight angles, there are only two different values, and they add up to $180^\circ$."]),
 ("Test for parallel lines", [r"If a pair of corresponding angles, or a pair of alternate interior angles, is equal, or a pair of same-side interior angles is supplementary, then the two lines are parallel."]),
]

MISTAKES = [
 r"Mixing up complementary ($90^\circ$) and supplementary ($180^\circ$) angles.",
 r"Saying vertically opposite angles are supplementary; they are equal.",
 r"Saying corresponding or alternate interior angles are supplementary; same-side interior angles are the supplementary pair.",
 r"Using the corresponding angle result when the lines are not known to be parallel.",
 r"Forgetting that the four angles around a point add up to $360^\circ$, not $180^\circ$.",
]
