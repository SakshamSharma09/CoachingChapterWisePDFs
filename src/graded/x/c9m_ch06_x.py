"""Class 9 Maths Ch 6 Perimeter and Area - extras."""
from common import AR4, Q

AR = [
 AR4(r"The area of a triangle with sides 13 cm, 14 cm and 15 cm is 84 cm$^2$.", r"By Heron's formula the area is $\sqrt{s(s-a)(s-b)(s-c)}$, where $s$ is the semi-perimeter.", "a",
     r"$s=21$, area $=\sqrt{21\times8\times7\times6}=\sqrt{7056}=84$, using R."),
 AR4(r"The circumference of a circle of radius 7 cm is 44 cm (take $\pi=\frac{22}{7}$).", r"The area of a circle of radius $r$ is $\pi r^2$.", "b",
     r"$2\pi r=2\times\frac{22}{7}\times7=44$, so A is true; R is true but is the area formula, not the reason for A."),
 AR4(r"The area of a parallelogram is base $\times$ corresponding height.", r"The area of a parallelogram is the product of two adjacent sides.", "c",
     r"A is correct; R is false because the product of adjacent sides is not the area unless the angle between them is $90^\circ$."),
 AR4(r"The area of a circle of radius 7 cm is 44 cm$^2$ (take $\pi=\frac{22}{7}$).", r"The area of a circle of radius $r$ is $\pi r^2$.", "d",
     r"Area $=\frac{22}{7}\times49=154$ cm$^2$, so A is false (44 is the circumference); R is true."),
 AR4(r"The length of the arc of a circle of radius 14 cm subtending $90^\circ$ at the centre is 22 cm (take $\pi=\frac{22}{7}$).", r"Arc length $=\dfrac{\theta}{360}\times2\pi r$.", "a",
     r"$\dfrac{90}{360}\times2\times\dfrac{22}{7}\times14=22$ cm, using R."),
 AR4(r"By Brahmagupta's formula, the area of a cyclic quadrilateral with sides 6 cm, 8 cm, 6 cm, 8 cm is 48 cm$^2$.", r"A rectangle is a cyclic quadrilateral.", "b",
     r"$s=14$, area $=\sqrt{8\times6\times8\times6}=48$; both statements are true, but R only says the formula applies, it does not give the value."),
]

CASE = [
 Q(r"<b>Case study.</b> A circular pond of radius 14 m in a village in Kerala is surrounded by a 7 m wide path. Take $\pi=\dfrac{22}{7}$. "
   r"(i) Find the circumference of the pond. (ii) Find the area of the pond. (iii) Find the radius and the area of the outer circle formed by the path. (iv) Find the area of the path and the cost of paving it at Rs 40 per m$^2$.",
   r"(i) $2\pi r=2\times\frac{22}{7}\times14=88$ m (1). (ii) $\pi r^2=\frac{22}{7}\times196=616$ m$^2$ (1). (iii) Outer radius $=21$ m, area $=\frac{22}{7}\times441=1386$ m$^2$ (1). (iv) Path area $=1386-616=770$ m$^2$ (1); cost $=770\times40=$ Rs 30800 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A triangular plot ABC belonging to a farmer has sides AB $=13$ m, BC $=14$ m and CA $=15$ m. "
   r"(i) Find the semi-perimeter of the plot. (ii) Find its area using Heron's formula. (iii) Find the altitude on the side BC. (iv) Find the cost of levelling the plot at Rs 30 per m$^2$ and the altitude on the side CA.",
   r"(i) $s=\dfrac{13+14+15}{2}=21$ m (1). (ii) $\sqrt{21\times8\times7\times6}=84$ m$^2$ (1). (iii) $\tfrac12\times14\times h=84\Rightarrow h=12$ m (1). (iv) Cost $=84\times30=$ Rs 2520 (1); altitude on CA $=\dfrac{2\times84}{15}=11.2$ m (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A cyclic quadrilateral field has sides 25 m, 60 m, 52 m and 39 m, taken in order. "
   r"(i) Find its perimeter. (ii) Find its semi-perimeter $s$. (iii) Find the four values $s-a$, $s-b$, $s-c$, $s-d$. (iv) Use Brahmagupta's formula to find the area of the field and the cost of sowing it at Rs 10 per m$^2$.",
   r"(i) $25+60+52+39=176$ m (1). (ii) $s=88$ m (1). (iii) $63,\ 28,\ 36,\ 49$ (1). (iv) Area $=\sqrt{63\times28\times36\times49}=\sqrt{3111696}=1764$ m$^2$ (1); cost $=1764\times10=$ Rs 17640 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Circle and arc ($\\pi=\\frac{22}{7}$ or 3.14)", [r"Circumference $=2\pi r=\pi d$; area $=\pi r^2$.",
   r"Arc of a circle with angle $\theta$ at the centre: length $=\dfrac{\theta}{360}\times2\pi r$.",
   r"Area of a ring (path of width $w$ round a circle of radius $r$): $\pi\left[(r+w)^2-r^2\right]$."]),
 ("Parallelogram and triangle", [r"Parallelogram: area $=$ base $\times$ height; perimeter $=2(a+b)$.",
   r"Triangle: area $=\tfrac12\times$ base $\times$ height.",
   r"Equilateral triangle of side $a$: area $=\dfrac{\sqrt3}{4}a^2$.",
   r"Altitude on a side $=\dfrac{2\times\text{area}}{\text{that side}}$."]),
 ("Heron's formula", [r"$s=\dfrac{a+b+c}{2}$.", r"Area $=\sqrt{s(s-a)(s-b)(s-c)}$.",
   r"Example: sides $13, 14, 15$ give $s=21$ and area $84$."]),
 ("Brahmagupta's formula (cyclic quadrilateral)", [r"$s=\dfrac{a+b+c+d}{2}$.", r"Area $=\sqrt{(s-a)(s-b)(s-c)(s-d)}$; it applies only when the quadrilateral is cyclic.",
   r"Units: lengths in cm or m, area in cm$^2$ or m$^2$; cost $=$ area $\times$ rate per unit area."]),
]

MISTAKES = [
 r"Mixing up circumference ($2\pi r$) and area ($\pi r^2$), or writing the area in cm instead of cm$^2$.",
 r"In Heron's formula, using the perimeter instead of the semi-perimeter $s$ in the factors $(s-a)$.",
 r"Using a slanting side instead of the perpendicular height in the area of a parallelogram or triangle.",
 r"Treating the width of a path as the outer radius; the outer radius is $r+w$ and the area of the path is the <i>difference</i> of the two circle areas.",
 r"Forgetting the factor $\dfrac{\theta}{360}$ in the arc length formula, or using the area formula $\pi r^2$ for arc length.",
 r"Applying Brahmagupta's formula to a quadrilateral that is not cyclic.",
]
