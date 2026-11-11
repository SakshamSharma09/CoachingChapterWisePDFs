"""Class 6 Maths Ch 6 Perimeter and Area - extras."""
from common import AR4, Q

AR = [
 AR4("The perimeter of a rectangle 12 m long and 5 m wide is 34 m.", "Perimeter of a rectangle = 2 x (length + breadth).", "a",
     "2 x (12 + 5) = 34."),
 AR4("The area of a square of side 7 cm is 49 cm$^2$.", "Area is measured in square units.", "b",
     "7 x 7 = 49 and area is in square units, but R does not explain the value 49."),
 AR4("A rectangle has area 48 cm$^2$ and length 8 cm. Its breadth is 6 cm.", "Breadth = area x length.", "c",
     "Breadth = 48 / 8 = 6, so A is true. Breadth = area / length, so R is false."),
 AR4("A rectangle and a square with the same perimeter always have the same area.", "The area of a square of side a is a x a.", "d",
     "A square of perimeter 16 cm has area 16 cm$^2$ but a 6 cm by 2 cm rectangle with perimeter 16 cm has area 12 cm$^2$. A is false, R is true."),
 AR4("The area of a triangle with base 10 cm and height 6 cm is 30 cm$^2$.", r"Area of a triangle = $\frac12$ x base x height.", "a",
     "Half of 10 x 6 = 30."),
 AR4("To fence a field we find its perimeter, not its area.", "A fence goes along the boundary of the field.", "a",
     "Perimeter is the length of the boundary."),
]

CASE = [
 Q(r"<b>Case study.</b> Farmer Ramesh has a rectangular field 40 m long and 25 m wide. He will fence it with wire and then sow seeds. (i) Find the perimeter of the field. (ii) Find the area of the field. (iii) Find the cost of fencing at ₹20 per metre. (iv) 2 kg of seeds are needed for every 50 m$^2$. How many kg of seeds does he need?",
   r"(i) $2\times(40+25)=130$ m (1). (ii) $40\times25=1000$ m$^2$ (1). (iii) $130\times20=₹2600$ (1). (iv) $1000\div50=20$ parts, so $20\times2=40$ kg (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A school courtyard is 12 m long and 9 m wide. It is paved with square slabs of side 3 m. (i) Find the area of the courtyard. (ii) Find the area of one slab. (iii) How many slabs are needed? (iv) Each slab costs ₹450. Find the total cost and the cost per square metre.",
   r"(i) $12\times9=108$ m$^2$ (1). (ii) $3\times3=9$ m$^2$ (1). (iii) $108\div9=12$ slabs (1). (iv) Total cost $=12\times450=₹5400$ (1); cost per m$^2$ $=450\div9=₹50$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A garden bed is in the shape of a right-angled triangle. Its two shorter sides are 12 m and 9 m and its longest side is 15 m. (i) Find its perimeter. (ii) Find its area. (iii) What is the area of a rectangle 12 m by 9 m? (iv) Edging costs ₹30 per metre. Find the cost of edging the bed all round, and say how the area of the bed compares with the rectangle.",
   r"(i) $12+9+15=36$ m (1). (ii) $\frac12\times12\times9=54$ m$^2$ (1). (iii) $12\times9=108$ m$^2$ (1). (iv) Cost $=36\times30=₹1080$ (1); the triangle is half of the rectangle ($54=108\div2$) (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Perimeter", [r"Perimeter = total length of the boundary. Units: cm, m, km.",
   r"Rectangle: $P=2(l+b)$.   Square: $P=4a$.",
   r"Triangle: $P=a+b+c$ (sum of three sides).   Any polygon: sum of all sides."]),
 ("Area", [r"Area = the surface a shape covers. Units: cm$^2$, m$^2$, km$^2$.",
   r"Rectangle: $A=l\times b$.   Square: $A=a\times a=a^2$.",
   r"Triangle: $A=\dfrac12\times\text{base}\times\text{height}$ (half of the rectangle on the same base and height).",
   r"Finding a side: $b=\dfrac Al$ for a rectangle; $a=\dfrac P4$ for a square."]),
 ("Units", [r"$1\text{ m}=100\text{ cm}$, so $1\text{ m}^2=100\times100=10000\text{ cm}^2$.",
   r"Cost of fencing $=$ perimeter $\times$ rate per metre.   Cost of paving/tiling $=$ area $\times$ rate per m$^2$.",
   r"Number of tiles $=$ area of floor $\div$ area of one tile."]),
 ("Composite shapes", [r"Split an L-shaped or odd shape into rectangles, find each area, and add; or subtract the cut-out part from the big rectangle.",
   r"Same perimeter does not mean same area."]),
]

MISTAKES = [
 r"Using area units (cm$^2$) for perimeter or linear units (cm) for area.",
 r"Forgetting the $\frac12$ in the area of a triangle.",
 r"Using the sloping side instead of the perpendicular height in the triangle area.",
 r"Writing $P=l+b$ for a rectangle (it needs $2(l+b)$) or $A=2(l+b)$.",
 r"Mixing units: multiplying metres by centimetres without converting first.",
 r"Using area when the question is about fencing (perimeter) and the reverse for paving or tiling.",
]
