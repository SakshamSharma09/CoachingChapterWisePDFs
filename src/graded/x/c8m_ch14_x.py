"""Class 8 Maths Ch 14 Area - extras."""
from common import AR4, Q

AR = [
 AR4(r"The area of a parallelogram with base 12 cm and height 5 cm is 60 cm$^2$.", r"Area of a parallelogram $=$ base $\times$ corresponding height.", "a",
     r"$12\times5=60$ cm$^2$; R is the formula used."),
 AR4(r"The area of a triangle with base 10 cm and height 8 cm is 40 cm$^2$.", r"The area of a rectangle of length 10 cm and breadth 8 cm is 80 cm$^2$.", "b",
     r"A is true by $\tfrac12\times10\times8=40$; R is also true but is a separate fact, so it does not explain A."),
 AR4(r"A trapezium with parallel sides 8 cm and 12 cm and height 5 cm has area 50 cm$^2$.", r"Area of a trapezium $=$ (sum of parallel sides) $\times$ height.", "c",
     r"$\tfrac12(8+12)\times5=50$, so A is true. R omits the factor $\tfrac12$, so it is false."),
 AR4(r"Two triangles with equal bases and equal heights must be congruent.", r"Triangles with equal bases and equal heights have equal areas.", "d",
     r"They have equal areas but need not be congruent, so A is false; R is true."),
 AR4(r"A rhombus with diagonals 10 cm and 24 cm has area 120 cm$^2$.", r"Area of a rhombus $=\tfrac12\times d_1\times d_2$.", "a",
     r"$\tfrac12\times10\times24=120$; R is the formula used."),
 AR4(r"A square of side 9 cm has area 81 cm$^2$.", r"The area of a triangle is half the product of its base and height.", "b",
     r"A is true ($9^2=81$); R is true but unrelated to the area of a square."),
]

CASE = [
 Q(r"<b>Case study.</b> A trapezium-shaped field has parallel sides of 50 m and 30 m, and the distance between them is 20 m. The owner wants to level it. "
   r"(i) Find the area of the field. (ii) Find the cost of levelling at ₹15 per m$^2$. (iii) How many mats of area 4 m$^2$ are needed to cover the field? (iv) If each parallel side is increased by 10 m with the same height, find the new area and the increase.",
   r"(i) $\tfrac12(50+30)\times20=800$ m$^2$ (1). (ii) $800\times15=$ ₹12,000 (1). (iii) $800\div4=200$ mats (1). (iv) New area $=\tfrac12(60+40)\times20=1000$ m$^2$ (1); increase $=200$ m$^2$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A parallelogram-shaped lawn in a park has a base of 24 m and a height of 15 m. Grass planting costs ₹40 per m$^2$. "
   r"(i) Find the area of the lawn. (ii) Find the area of a triangular flower bed with the same base and height. (iii) Another parallelogram has the same area and a base of 18 m; find its height. (iv) Find the cost of planting grass on the lawn and on half of it.",
   r"(i) $24\times15=360$ m$^2$ (1). (ii) $\tfrac12\times24\times15=180$ m$^2$ (1). (iii) $360\div18=20$ m (1). (iv) Lawn: $360\times40=$ ₹14,400 (1); half: ₹7,200 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> An L-shaped hall is formed from a rectangular hall 12 m long and 8 m wide by cutting off a rectangular corner 5 m long and 4 m wide. The floor is to be tiled. "
   r"(i) Find the area of the full rectangle. (ii) Find the area of the corner removed. (iii) Find the area of the L-shaped hall. (iv) Find the cost of flooring at ₹250 per m$^2$.",
   r"(i) $12\times8=96$ m$^2$ (1). (ii) $5\times4=20$ m$^2$ (1). (iii) $96-20=76$ m$^2$ (1). (iv) $76\times250=$ ₹19,000 (1+1).", "1+1+1+2"),
]

FORMULAS = [
 ("Quadrilaterals", [
   r"Rectangle: $A=l\times b$. Square: $A=a^2$.",
   r"Parallelogram: $A=b\times h$ ($h$ is the perpendicular height).",
   r"Rhombus: $A=\tfrac12d_1d_2$ (also $b\times h$).",
   r"Trapezium: $A=\tfrac12(a+b)\times h$, where $a,b$ are the parallel sides."]),
 ("Triangle", [
   r"$A=\tfrac12\times\text{base}\times\text{height}$.",
   r"A diagonal of a parallelogram divides it into two triangles of equal area.",
   r"Triangles on the same base and between the same parallels have equal areas."]),
 ("Composite figures", [
   r"Split into rectangles, triangles, trapezia, etc.; add the areas, or subtract the area removed.",
   r"Cost of work $=$ area $\times$ rate per unit area."]),
 ("Units", [
   r"1 m $=100$ cm, so 1 m$^2=10\,000$ cm$^2$; 1 km$^2=10^6$ m$^2$.",
   r"1 hectare $=10\,000$ m$^2$.",
   r"Area is expressed in square units; perimeter in linear units."]),
]

MISTAKES = [
 r"Using the slant side instead of the perpendicular height in the area of a parallelogram or triangle.",
 r"Forgetting the factor $\tfrac12$ in the area of a triangle, trapezium or rhombus.",
 r"Mixing units: multiplying a length in metres by one in centimetres; convert first.",
 r"Writing area in cm instead of cm$^2$, or converting m$^2$ to cm$^2$ by multiplying by 100 (it is 10 000).",
 r"Using the sum of the non-parallel sides for a trapezium; only the <b>parallel</b> sides enter the formula.",
 r"Adding instead of subtracting when an L-shaped region is obtained by removing a corner.",
]
