"""Class 10 Maths Ch 10 Circles - extras (tangent perpendicular to radius; equal tangents from an external point)."""
from common import AR4, Q

AR = [
 AR4(r"A tangent PT touches a circle with centre O at P. If $OP=5$ cm and $PT=12$ cm, then $OT=13$ cm.", r"The tangent at any point of a circle is perpendicular to the radius through the point of contact.", "a",
     r"$\angle OPT=90^\circ$, so $OT^2=5^2+12^2=169$ and $OT=13$ cm; R is what makes the triangle right-angled."),
 AR4(r"Exactly two tangents can be drawn to a circle from a point outside it.", r"A tangent to a circle intersects the circle at two points.", "c",
     r"A is true; a tangent meets the circle at exactly one point, so R is false."),
 AR4(r"The number of tangents that can be drawn to a circle from a point lying inside the circle is 2.", r"There is exactly one tangent to a circle at each point of the circle.", "d",
     r"From an interior point no tangent can be drawn, so A is false; R is true."),
 AR4(r"A line which touches a circle at exactly one point is a tangent to the circle.", r"A circle has infinitely many tangents.", "b",
     r"A is the definition of a tangent and R is also true (one at each point), but R does not explain A."),
 AR4(r"A circle has radius 3 cm. The length of the tangent from a point P at distance 5 cm from the centre is 4 cm.", r"The tangent at a point is perpendicular to the radius through that point, so the Pythagoras theorem can be applied.", "a",
     r"Tangent length $=\sqrt{5^2-3^2}=4$ cm, found by using the right angle given in R."),
 AR4(r"If PA and PB are tangents from an external point P to a circle with centre O, then $\angle AOB+\angle APB=180^\circ$.", r"The tangent at a point of a circle is parallel to the radius through that point.", "c",
     r"In quadrilateral OAPB, $\angle OAP=\angle OBP=90^\circ$, so the other two angles sum to $180^\circ$: A true; the tangent is perpendicular, not parallel, to the radius, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> A circular park has centre O and radius 6 m. A gate P is at a distance of 10 m from O, outside the park. Two straight paths PA and PB touch the park at the points A and B. "
   r"(i) What is the measure of the angle between OA and the path PA? (ii) Find the length of the path PA. (iii) Write the length of the path PB. (iv) Find the area of the quadrilateral OAPB.",
   r"(i) $90^\circ$ (tangent is perpendicular to the radius at the point of contact) (1). (ii) $PA=\sqrt{OP^2-OA^2}=\sqrt{100-36}=8$ m (1). (iii) $PB=PA=8$ m, tangents from an external point are equal (1). (iv) $\triangle OAP\cong\triangle OBP$, so area $=2\times\tfrac12\times6\times8=48\ \text{m}^2$ (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Two tangents PA and PB are drawn from an external point P to a circular fountain with centre O, and $\angle APB=80^\circ$. "
   r"(i) Find $\angle OAP$. (ii) Find $\angle AOB$. (iii) Find $\angle OPA$. (iv) Find $\angle OAB$ and $\angle PAB$.",
   r"(i) $90^\circ$ (1). (ii) In quadrilateral OAPB, $\angle AOB=360^\circ-90^\circ-90^\circ-80^\circ=100^\circ$ (1). (iii) OP bisects $\angle APB$, so $\angle OPA=40^\circ$ (1). (iv) $OA=OB$, so $\angle OAB=\dfrac{180^\circ-100^\circ}{2}=40^\circ$ (1); $PA=PB$, so $\angle PAB=\dfrac{180^\circ-80^\circ}{2}=50^\circ$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Two concentric circles have radii 13 cm and 5 cm. A chord AB of the larger circle touches the smaller circle at the point P. Centre is O. "
   r"(i) What is the measure of $\angle OPA$ and why? (ii) Find the length AP. (iii) Find the length of the chord AB. (iv) If the radii were 17 cm and 8 cm instead, find the length of such a chord.",
   r"(i) $90^\circ$, since AB is a tangent to the smaller circle and OP is the radius through the contact point (1). (ii) $AP=\sqrt{13^2-5^2}=12$ cm (1). (iii) The perpendicular from the centre bisects the chord, so $AB=2\times12=24$ cm (1). (iv) $AP=\sqrt{17^2-8^2}=15$ cm, so the chord $=30$ cm (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Tangent and secant", [r"A <b>tangent</b> meets the circle at exactly one point (the point of contact). A <b>secant</b> meets it at two points.",
   r"At each point of a circle there is exactly one tangent. A circle has infinitely many tangents.",
   r"From a point inside a circle no tangent can be drawn; from a point on it 1; from a point outside it 2."]),
 ("Theorems", [r"The tangent at any point of a circle is <b>perpendicular</b> to the radius through the point of contact.",
   r"The lengths of the two tangents drawn from an external point to a circle are <b>equal</b>."]),
 ("Consequences used in problems", [r"For a point P at distance d from the centre of a circle of radius r: tangent length $=\sqrt{d^2-r^2}$.",
   r"If PA, PB are tangents from P with centre O: $\angle OAP=\angle OBP=90^\circ$; $\angle AOB+\angle APB=180^\circ$; OP bisects $\angle APB$ and $\angle AOB$.",
   r"Concentric circles: chord of the larger circle touching the smaller has length $2\sqrt{R^2-r^2}$.",
   r"Tangents drawn at the two ends of a diameter are parallel."]),
]

MISTAKES = [
 r"Taking the tangent as perpendicular to the <i>chord</i> or parallel to the radius; it is perpendicular to the radius at the contact point.",
 r"Using the Pythagoras theorem with the wrong hypotenuse: in $\triangle OPT$ the hypotenuse is OT (from the centre to the external point).",
 r"Forgetting that the tangent lengths from one external point are equal and stopping after finding only one of them.",
 r"Claiming a line meeting the circle at two points is a tangent; that line is a secant.",
 r"Writing $\angle AOB+\angle APB=90^\circ$; the correct sum is $180^\circ$.",
 r"Assuming a tangent can be drawn from a point inside the circle.",
]
