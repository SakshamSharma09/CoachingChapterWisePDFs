"""Class 10 Maths Ch 11 Areas Related to Circles - extras (sector, segment, combinations; pi = 22/7)."""
from common import AR4, Q

AR = [
 AR4(r"The area of a sector of a circle of radius 7 cm and angle $90^\circ$ is $38.5\ \text{cm}^2$ (use $\pi=\tfrac{22}{7}$).", r"The area of a sector of angle $\theta$ is $\dfrac{\theta}{360^\circ}\times\pi r^2$.", "a",
     r"$\tfrac14\times\tfrac{22}{7}\times49=38.5$; R is the formula used."),
 AR4(r"The length of the arc of a sector of radius 21 cm and angle $60^\circ$ is 22 cm (use $\pi=\tfrac{22}{7}$).", r"The length of the arc of a sector of angle $\theta$ is $\dfrac{\theta}{360^\circ}\times\pi r^2$.", "c",
     r"Arc $=\tfrac16\times2\times\tfrac{22}7\times21=22$ cm: A true; arc length is $\dfrac\theta{360^\circ}\times2\pi r$, so R is false."),
 AR4(r"If the radius of a circle is doubled, its area also becomes double.", r"The area of a circle of radius r is $\pi r^2$.", "d",
     r"Area becomes $\pi(2r)^2=4\pi r^2$, four times: A false; R is true."),
 AR4(r"The area of a circle of diameter 14 cm is $154\ \text{cm}^2$ (use $\pi=\tfrac{22}{7}$).", r"The area of a sector of a circle is less than the area of the circle.", "b",
     r"$\tfrac{22}{7}\times7^2=154$ so A is true; R is true but not related to computing the area."),
 AR4(r"The area of a ring between two concentric circles of radii 14 cm and 7 cm is $462\ \text{cm}^2$ (use $\pi=\tfrac{22}{7}$).", r"The area of a ring between concentric circles of radii R and r $(R>r)$ is $\pi(R^2-r^2)$.", "a",
     r"$\tfrac{22}{7}(196-49)=\tfrac{22}{7}\times147=462$; R is the formula used."),
 AR4(r"In 30 minutes the minute hand, 7 cm long, of a clock sweeps an area of $77\ \text{cm}^2$ (use $\pi=\tfrac{22}{7}$).", r"The minute hand of a clock turns through $90^\circ$ in 30 minutes.", "c",
     r"In 30 minutes it turns through $180^\circ$, so area $=\tfrac12\times154=77$: A true; R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> A lawn sprinkler is fixed at a point and waters a sector-shaped region of radius 21 m with a sector angle of $60^\circ$. (Take $\pi=\tfrac{22}{7}$.) "
   r"(i) Find the area of the lawn watered. (ii) Find the length of the curved boundary (arc). (iii) Find the perimeter of the watered region. (iv) If the sprinkler is adjusted so that the angle becomes $120^\circ$, find the new area and compare it with the old one.",
   r"(i) $\tfrac{60}{360}\times\tfrac{22}{7}\times21^2=\tfrac16\times1386=231\ \text{m}^2$ (1). (ii) $\tfrac{60}{360}\times2\times\tfrac{22}{7}\times21=22$ m (1). (iii) $22+21+21=64$ m (1). (iv) $\tfrac{120}{360}\times1386=462\ \text{m}^2$ (1), which is double the old area, since the area is proportional to the angle (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A decorative circular window has radius 14 cm. A straight metal strip is fixed along a chord AB that subtends a right angle at the centre O. The region between the chord and the minor arc is filled with coloured glass. (Take $\pi=\tfrac{22}{7}$.) "
   r"(i) Find the area of the sector OAB. (ii) Find the area of $\triangle OAB$. (iii) Find the area of the coloured (minor) segment. (iv) Find the area of the major segment.",
   r"(i) $\tfrac14\times\tfrac{22}{7}\times196=154\ \text{cm}^2$ (1). (ii) $\tfrac12\times14\times14=98\ \text{cm}^2$ (1). (iii) Minor segment $=154-98=56\ \text{cm}^2$ (1). (iv) Circle $=\tfrac{22}{7}\times196=616$; major segment $=616-56=560\ \text{cm}^2$ (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A circular running track has an inner boundary of radius 28 m and an outer boundary of radius 35 m, so the track is 7 m wide. (Take $\pi=\tfrac{22}{7}$.) "
   r"(i) Find the area enclosed by the inner circle. (ii) Find the area enclosed by the outer circle. (iii) Find the area of the track. (iv) Find the cost of paving the track at ₹ 25 per square metre and the length of the inner boundary.",
   r"(i) $\tfrac{22}{7}\times28^2=2464\ \text{m}^2$ (1). (ii) $\tfrac{22}{7}\times35^2=3850\ \text{m}^2$ (1). (iii) $3850-2464=1386\ \text{m}^2$ (1). (iv) Cost $=1386\times25=₹\,34{,}650$ (1); inner boundary $=2\times\tfrac{22}{7}\times28=176$ m (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Circle", [r"Circumference $=2\pi r=\pi d$. Area $=\pi r^2$. Take $\pi=\dfrac{22}{7}$ unless told otherwise.",
   r"Ring (annulus) between radii R and r: area $=\pi(R^2-r^2)=\pi(R+r)(R-r)$."]),
 ("Sector of angle $\theta$ (in degrees)", [r"Length of arc $=\dfrac{\theta}{360^\circ}\times2\pi r$.",
   r"Area of sector $=\dfrac{\theta}{360^\circ}\times\pi r^2=\dfrac12\,l\,r$ (l = arc length).",
   r"Perimeter of sector $=2r+\text{arc length}$.",
   r"Quadrant: $\theta=90^\circ$. Semicircle: $\theta=180^\circ$."]),
 ("Segment of a circle", [r"Area of minor segment $=$ area of sector $-$ area of $\triangle OAB$.",
   r"Area of major segment $=\pi r^2-$ area of minor segment.",
   r"$\triangle OAB$: $\theta=90^\circ$: $\tfrac12r^2$; $\theta=60^\circ$: $\tfrac{\sqrt3}{4}r^2$; $\theta=120^\circ$: $\tfrac{\sqrt3}{4}r^2$."]),
 ("Clocks and wheels", [r"Minute hand turns $360^\circ$ in 60 min ($6^\circ$ per minute); hour hand $360^\circ$ in 12 h ($0.5^\circ$ per minute).",
   r"Distance covered by a wheel in n revolutions $=n\times2\pi r$."]),
 ("Combinations", [r"Area of shaded region $=$ area of larger figure $-$ area of smaller figures (squares, triangles, circles, quadrants)."]),
]

MISTAKES = [
 r"Using $\pi r^2$ in the arc-length formula or $2\pi r$ in the sector-area formula.",
 r"Forgetting to add the two radii when asked for the <i>perimeter</i> of a sector.",
 r"Using diameter in place of radius in $\pi r^2$.",
 r"Subtracting the wrong figure for a segment: minor segment $=$ sector $-$ triangle, not sector $+$ triangle.",
 r"Mixing units (cm and m) or writing cm instead of cm$^2$ for areas.",
 r"Thinking the area of a circle doubles when the radius doubles; it becomes four times.",
]
