"""Class 10 Maths Ch 9 Some Applications of Trigonometry - extras (heights and distances, angles 30/45/60 only)."""
from common import AR4, Q

AR = [
 AR4(r"When an observer walks towards the foot of a tower, the angle of elevation of its top increases.", r"For a tower of fixed height h at horizontal distance d, $\tan\theta=\dfrac hd$, which increases as d decreases.", "a",
     r"With h fixed, smaller d gives larger $\tan\theta$, hence larger $\theta$; R is the explanation."),
 AR4(r"A tower $10\sqrt3$ m high casts a shadow 10 m long when the angle of elevation of the Sun is $60^\circ$.", r"$\tan60^\circ=\dfrac1{\sqrt3}$.", "c",
     r"$\tan60^\circ=\dfrac{10\sqrt3}{10}=\sqrt3$ so A is true; R is false because $\tan60^\circ=\sqrt3$."),
 AR4(r"The angle of elevation of an object can be $120^\circ$.", r"The angle of depression of a point on the ground seen from the top of a tower equals the angle of elevation of the top seen from that point.", "d",
     r"The angle of elevation is measured from the horizontal and lies between $0^\circ$ and $90^\circ$, so A is false; R is true (alternate angles)."),
 AR4(r"A 20 m high pole casts a shadow 20 m long when the angle of elevation of the Sun is $45^\circ$.", r"The angle of elevation is measured from the horizontal line through the eye of the observer.", "b",
     r"$\tan45^\circ=1=\tfrac{20}{20}$ so A is true; R is also true but it is not the reason for the equal lengths."),
 AR4(r"A 10 m ladder leaning against a wall makes an angle of $60^\circ$ with the ground. It reaches a height of $5\sqrt3$ m.", r"In a right triangle, $\sin\theta=\dfrac{\text{perpendicular}}{\text{hypotenuse}}$.", "a",
     r"Height $=10\sin60^\circ=10\times\tfrac{\sqrt3}2=5\sqrt3$ m, using R."),
 AR4(r"A kite string 100 m long, taut and inclined at $30^\circ$ to the ground, has the kite at a height of 50 m.", r"$\sin30^\circ=\dfrac{\sqrt3}{2}$.", "c",
     r"Height $=100\sin30^\circ=50$ m: A true; $\sin30^\circ=\tfrac12$, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> A vertical tower stands on level ground. From a point P on the ground, 20 m from the foot of the tower, the angle of elevation of its top is $60^\circ$. (Use $\sqrt3=1.73$.) "
   r"(i) Name the trigonometric ratio that relates the height of the tower to the distance of P from the foot of the tower. (ii) Write the value of $\tan60^\circ$. (iii) Find the height of the tower. (iv) The observer moves back until the angle of elevation becomes $30^\circ$. Find the new distance from the foot of the tower and how far the observer moved.",
   r"(i) $\tan\theta$ (1). (ii) $\sqrt3$ (1). (iii) $h=20\tan60^\circ=20\sqrt3=34.6$ m (1). (iv) New distance $=\dfrac{20\sqrt3}{\tan30^\circ}=20\sqrt3\times\sqrt3=60$ m (1); distance moved $=60-20=40$ m (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Rahul is flying a kite. The string is 60 m long and is stretched straight, making an angle of $30^\circ$ with the horizontal ground (assume no slack, and use $\sqrt3=1.73$). "
   r"(i) Which ratio connects the height of the kite with the length of the string? (ii) Find the height of the kite. (iii) Find the horizontal distance of the kite from Rahul. (iv) If the string, still 60 m long, now makes an angle of $60^\circ$ with the ground, find the new height and its increase.",
   r"(i) $\sin\theta$ (1). (ii) $60\sin30^\circ=30$ m (1). (iii) $60\cos30^\circ=30\sqrt3=51.9$ m (1). (iv) New height $=60\sin60^\circ=30\sqrt3=51.9$ m (1); increase $=51.9-30=21.9$ m (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> From the top of a 60 m high lighthouse, the angles of depression of two ships on the same side of the lighthouse (in line with its foot) are $60^\circ$ and $30^\circ$. (Use $\sqrt3=1.73$.) "
   r"(i) What is the angle of elevation of the top of the lighthouse from the nearer ship? (ii) Find the distance of the nearer ship from the foot of the lighthouse. (iii) Find the distance of the farther ship from the foot of the lighthouse. (iv) Find the distance between the two ships.",
   r"(i) $60^\circ$ (angle of depression = angle of elevation, alternate angles) (1). (ii) $\dfrac{60}{\tan60^\circ}=20\sqrt3=34.6$ m (1). (iii) $\dfrac{60}{\tan30^\circ}=60\sqrt3=103.8$ m (1). (iv) $60\sqrt3-20\sqrt3=40\sqrt3=69.2$ m (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Terms", [r"<b>Line of sight</b>: line from the eye to the object. <b>Angle of elevation</b>: angle between the line of sight and the horizontal when the object is above the horizontal.",
   r"<b>Angle of depression</b>: angle between the line of sight and the horizontal when the object is below the horizontal. Angle of depression from the top = angle of elevation from the object (alternate angles)."]),
 ("Ratios used", [r"$\sin\theta=\dfrac{\text{height}}{\text{line of sight}}$, $\ \cos\theta=\dfrac{\text{horizontal distance}}{\text{line of sight}}$, $\ \tan\theta=\dfrac{\text{height}}{\text{horizontal distance}}$."]),
 ("Standard values (angles in this chapter)", [r"$\sin30^\circ=\tfrac12$, $\ \sin45^\circ=\tfrac1{\sqrt2}$, $\ \sin60^\circ=\tfrac{\sqrt3}2$.",
   r"$\cos30^\circ=\tfrac{\sqrt3}2$, $\ \cos45^\circ=\tfrac1{\sqrt2}$, $\ \cos60^\circ=\tfrac12$.",
   r"$\tan30^\circ=\tfrac1{\sqrt3}$, $\ \tan45^\circ=1$, $\ \tan60^\circ=\sqrt3$.",
   r"$\sqrt2\approx1.41$, $\ \sqrt3\approx1.73$ (as given in the question)."]),
 ("Method", [r"Draw a neat figure; mark the right angle, the given angle and the unknown; choose the ratio containing the known and unknown sides.",
   r"Two observation points in line with the tower: height h, distances $d_1=\dfrac h{\tan\alpha},\ d_2=\dfrac h{\tan\beta}$; distance between points $=|d_1-d_2|$ (same side) or $d_1+d_2$ (opposite sides).",
   r"Add the height of the observer when the angle is measured from the eye."]),
]

MISTAKES = [
 r"Measuring the angle from the vertical or from the line of sight instead of from the horizontal.",
 r"Using $\tan30^\circ=\sqrt3$ or $\tan60^\circ=\dfrac1{\sqrt3}$; the values are the other way round.",
 r"Confusing the angle of depression with the angle at the foot of the tower; use alternate angles and the horizontal at the top.",
 r"Forgetting to add the observer's height (or subtract it) when the angle is measured from the eye level.",
 r"Subtracting the distances when the two observation points are on opposite sides of the tower (they must be added).",
 r"Giving the final answer without units or leaving $\sqrt3$ unsubstituted when the question asks for a decimal value.",
]
