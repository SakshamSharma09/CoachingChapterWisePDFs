"""Class 9 Maths Ch 5 Circles - extras."""
from common import AR4, Q

AR = [
 AR4(r"In a circle of radius 5 cm, a chord at a distance of 3 cm from the centre has length 8 cm.", r"The perpendicular from the centre of a circle to a chord bisects the chord.", "a",
     r"Half-chord $=\sqrt{5^2-3^2}=4$ cm, using the perpendicular bisection in R; chord $=8$ cm."),
 AR4(r"Equal chords of a circle are equidistant from the centre.", r"The perpendicular from the centre of a circle to a chord bisects the chord.", "b",
     r"Both are true theorems, but R does not by itself explain why equal chords are equidistant."),
 AR4(r"The opposite angles of a cyclic quadrilateral are supplementary.", r"The opposite angles of a cyclic quadrilateral are equal.", "c",
     r"A is the cyclic-quadrilateral theorem; R is false in general (e.g. angles $80^\circ$ and $100^\circ$)."),
 AR4(r"A chord of a circle can be longer than its diameter.", r"The diameter is the longest chord of a circle.", "d",
     r"A is false because every chord is at most as long as the diameter; R is true."),
 AR4(r"If the angle subtended by an arc at the centre is $100^\circ$, the angle it subtends at a point on the remaining part of the circle is $50^\circ$.", r"The angle subtended by an arc at the centre is double the angle it subtends at any point on the remaining part of the circle.", "a",
     r"$\tfrac12\times100^\circ=50^\circ$, directly from R."),
 AR4(r"Angles in the same segment of a circle are equal.", r"An angle in a semicircle is a right angle.", "b",
     r"Both are true theorems, but R is a special case about semicircles and does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> A circular garden in a Chandigarh park has radius 13 m. A straight path, 24 m long, joins two points on its boundary (a chord of the circle). "
   r"(i) Find the half-length of the chord. (ii) Find the perpendicular distance of the path from the centre. (iii) Find the length of another chord which is at a distance of 12 m from the centre. (iv) If the two chords lie on opposite sides of the centre and are parallel, find the distance between them.",
   r"(i) The perpendicular from the centre bisects the chord, so the half-length is 12 m (1). (ii) $\sqrt{13^2-12^2}=5$ m (1). (iii) Half-chord $=\sqrt{13^2-12^2}=5$, so the chord is 10 m (1). (iv) Distances from the centre are 5 m and 12 m on opposite sides, so the distance between them is $5+12=17$ m (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A circular track has centre O. Points A and B lie on the track such that the arc AB subtends $\angle AOB=110^\circ$ at the centre. A point C lies on the major arc AB and a point E lies on the minor arc AB. "
   r"(i) Find $\angle ACB$. (ii) What is the angle subtended at any point of the circle by a diameter? (iii) If D is another point on the major arc, find $\angle ADB$. (iv) Find $\angle AEB$ and give the reason.",
   r"(i) $\angle ACB=\tfrac12\times110^\circ=55^\circ$ (1). (ii) $90^\circ$ (angle in a semicircle) (1). (iii) Angles in the same segment are equal, so $\angle ADB=55^\circ$ (1). (iv) ACBE is a cyclic quadrilateral, so $\angle AEB=180^\circ-55^\circ=125^\circ$ (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A kite maker draws a cyclic quadrilateral ABCD on a circular board, with $\angle B=95^\circ$. The angles $\angle A=(2x+10)^\circ$ and $\angle C=(3x-10)^\circ$ are opposite angles. "
   r"(i) Find $\angle D$. (ii) Find the value of $x$. (iii) Find $\angle A$ and $\angle C$. (iv) The side BC is extended to E. Find the exterior angle $\angle DCE$ and show that it equals $\angle A$.",
   r"(i) $\angle D=180^\circ-95^\circ=85^\circ$ (1). (ii) $(2x+10)+(3x-10)=180\Rightarrow x=36$ (1). (iii) $\angle A=82^\circ$, $\angle C=98^\circ$ (1). (iv) $\angle DCE=180^\circ-98^\circ=82^\circ$ (1), which equals $\angle A=82^\circ$ because $\angle A+\angle C=180^\circ$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Chords", [r"The perpendicular from the centre to a chord bisects the chord; the line from the centre to the midpoint of a chord is perpendicular to it.",
   r"Equal chords are equidistant from the centre, and chords equidistant from the centre are equal. Equal chords subtend equal angles at the centre.",
   r"Chord length: $2\sqrt{r^2-d^2}$ where $r$ is the radius and $d$ the distance from the centre.",
   r"The diameter is the longest chord."]),
 ("Angles in a circle", [r"Angle at the centre $=2\times$ angle at any point of the remaining circle (same arc).",
   r"Angles in the same segment are equal.", r"Angle in a semicircle $=90^\circ$."]),
 ("Cyclic quadrilateral", [r"Opposite angles are supplementary: $\angle A+\angle C=180^\circ$, $\angle B+\angle D=180^\circ$.",
   r"Exterior angle $=$ interior opposite angle.", r"A parallelogram inscribed in a circle is a rectangle."]),
]

MISTAKES = [
 r"Using the full chord instead of the half-chord in $r^2=d^2+(\text{half-chord})^2$.",
 r"Forgetting that the perpendicular distance, not the slant distance, is used when finding the distance of a chord from the centre.",
 r"Applying the angle theorems to an arc without checking the angle is at the <i>centre</i> (double) or on the <i>remaining</i> circle (half).",
 r"For two parallel chords, adding the distances when they are on the same side or subtracting them when they are on opposite sides (the reverse is correct).",
 r"Assuming that opposite angles of a cyclic quadrilateral are equal; they are supplementary (sum $180^\circ$).",
 r"Using the angle in a semicircle theorem when the chord is not a diameter.",
]
