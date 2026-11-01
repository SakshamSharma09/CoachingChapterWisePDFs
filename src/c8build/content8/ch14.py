from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def g(x): return f"{x:g}"
# A: rectangle area (4)
for l, b in [(12, 7), (15, 8), (24, 5), (18, 11)]:
    A.append(M4(f"The area of a rectangle of length {l} cm and breadth {b} cm is:", f"{l*b} cm²", [f"{2*(l+b)} cm²", f"{l+b} cm²", f"{l*b+b} cm²"], "$l\\times b$"))
# A: triangle (5)
for b, h in [(10, 6), (14, 9), (20, 7), (16, 15), (9, 12)]:
    A.append(M4(f"The area of a triangle with base {b} cm and height {h} cm is:", f"{g(b*h/2)} cm²", [f"{b*h} cm²", f"{b+h} cm²", f"{g(b*h/2+b)} cm²"], r"$\tfrac12\times b\times h$"))
# A: parallelogram (4)
for b, h in [(12, 5), (15, 8), (9, 7), (20, 6)]:
    A.append(M4(f"The area of a parallelogram with base {b} cm and height {h} cm is:", f"{b*h} cm²", [f"{b*h//2} cm²", f"{2*(b+h)} cm²", f"{b*h+h} cm²"], "base × height"))
# A: trapezium (5)
for a, b, h in [(10, 14, 6), (8, 12, 5), (15, 25, 8), (7, 11, 10), (12, 18, 9)]:
    A.append(M4(f"The area of a trapezium with parallel sides {a} cm and {b} cm and height {h} cm is:", f"{g((a+b)*h/2)} cm²", [f"{(a+b)*h} cm²", f"{a*b} cm²", f"{g((a+b)*h/2+a)} cm²"], r"$\tfrac12(a+b)h$"))
# A: rhombus (4)
for d1, d2 in [(10, 8), (24, 10), (16, 12), (18, 14)]:
    A.append(M4(f"The area of a rhombus with diagonals {d1} cm and {d2} cm is:", f"{d1*d2//2} cm²", [f"{d1*d2} cm²", f"{d1+d2} cm²", f"{d1*d2//4} cm²"], r"$\tfrac12 d_1d_2$"))
# A: missing dimension (4)
for area, l in [(96, 12), (150, 15), (84, 7), (200, 25)]:
    A.append(M4(f"A rectangle has area {area} cm² and length {l} cm. Its breadth is:", f"{area//l} cm", [f"{area//l+2} cm", f"{area//l-1} cm", f"{area-l} cm"], "Area ÷ length") if area % l == 0 else None)
A = [x for x in A if x]
# A: concepts (14)
A += [
 M4("Which of the following can be the same for two shapes with different areas?", "perimeter", ["length only", "angles", "colour"], "Perimeter is not a measure of area"),
 M4("The unit of area is:", "square units", ["units", "cubic units", "none"], "e.g. cm²"),
 M4("1 m² equals:", "10000 cm²", ["100 cm²", "1000 cm²", "100000 cm²"], "100 × 100"),
 M4("A diagonal of a rectangle divides it into two triangles of:", "equal area", ["unequal area", "double area", "no area"], "Congruent"),
 M4("A median of a triangle divides it into two parts of:", "equal area", ["unequal area", "area 1 : 2", "area 1 : 3"], "Same height and equal bases"),
 M4("Two triangles on the same base and between the same parallels have:", "equal area", ["different area", "double area", "zero area"], "Same base and height"),
 M4("A rectangle and a parallelogram on the same base and between the same parallels have:", "equal area", ["different area", "double area", "half area"], "Same base and height"),
 M4("If the base of a triangle is doubled and height kept the same, the area:", "doubles", ["halves", "stays the same", "becomes four times"], "Area ∝ base"),
 M4("The area of a square whose diagonal is 10 cm is:", "50 cm²", ["100 cm²", "25 cm²", "20 cm²"], "$\\tfrac12d^2$"),
 M4("A square park of side 40 m has area:", "1600 m²", ["160 m²", "800 m²", "400 m²"], "$40^2$"),
 M4("The perimeter of a square is 36 cm. Its area is:", "81 cm²", ["36 cm²", "144 cm²", "324 cm²"], "Side 9 cm"),
 M4("The height of a parallelogram of area 72 cm² and base 12 cm is:", "6 cm", ["60 cm", "12 cm", "24 cm"], "72 ÷ 12"),
 M4("Area of a triangle with sides 3, 4, 5 cm is:", "6 cm²", ["12 cm²", "10 cm²", "7.5 cm²"], "Right-angled: ½×3×4"),
 M4("The area of a rhombus with side 5 cm and one diagonal 6 cm is:", "24 cm²", ["30 cm²", "48 cm²", "12 cm²"], "Other diagonal 8"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Write the formulas for the area of a triangle and a parallelogram.", "$\\tfrac12bh$ (1); $bh$ (1).", "1+1"),
 Q("Find the area of a rectangle 18 m by 11 m.", "198 m² (2).", "2"),
 Q("Why is perimeter not a measure of area? Give an example.", "Different shapes with equal perimeter can have different areas (1); e.g. 6×2 and 4×4 rectangles (1).", "1+1"),
 Q("Find the area of a triangle with base 15 cm and height 8 cm.", "60 cm² (2).", "2"),
 Q("Find the area of a trapezium with parallel sides 9 cm, 13 cm and height 7 cm.", "77 cm² (2).", "2"),
 Q("A rhombus has diagonals 12 cm and 16 cm. Find its area.", "96 cm² (2).", "2"),
 Q("Find the base of a parallelogram of area 108 cm² and height 9 cm.", "12 cm (2).", "2"),
 Q("How many 25 cm × 20 cm tiles cover a floor of 5 m by 4 m?", "$200000/500=400$ tiles (2).", "2"),
 Q("Convert 3.5 m² to cm².", "35000 cm² (2).", "2"),
 Q("Find the area of a square of perimeter 52 cm.", "Side 13; area 169 cm² (2).", "2"),
 Q("A triangle has area 54 cm² and base 12 cm. Find its height.", "9 cm (2).", "2"),
 Q("The diagonal of a rectangle splits it into two triangles. If the rectangle has area 84 cm², find the area of each triangle.", "42 cm² (2).", "2"),
 Q("Two parallelograms on the same base have heights 5 cm and 8 cm. Find the ratio of their areas.", "5 : 8 (2).", "2"),
 Q("Find the side of a square whose area is 225 m².", "15 m (2).", "2"),
 Q("What is the area of a triangle with vertices forming a right angle with legs 9 and 40?", "180 square units (2).", "2"),
 Q("Find the area of a rhombus with each side 13 cm and one diagonal 10 cm.", "Other diagonal 24 (1); area 120 cm² (1).", "1+1"),
]
for l, b in [(14, 9), (20, 13), (25, 8), (32, 15), (18, 18), (27, 6)]:
    C.append(Q(f"A rectangular plot is {l} m by {b} m. Find its area and the cost of fencing at ₹ 30 per metre.", f"Area ${l*b}$ m² (1.5); perimeter ${2*(l+b)}$ m, cost ₹ {30*2*(l+b)} (1.5).", "1½+1½"))
for a, b, h in [(12, 20, 8), (9, 15, 10), (14, 22, 7), (18, 30, 12), (10, 26, 9), (16, 24, 15)]:
    C.append(Q(f"Find the area of a trapezium with parallel sides {a} cm and {b} cm and distance between them {h} cm. Also find the area of an equal-height rectangle with width {b} cm.", f"Trapezium $=\\tfrac12({a}+{b})\\times{h}={g((a+b)*h/2)}$ cm² (2); rectangle ${b*h}$ cm² (1).", "2+1"))
for b, h in [(18, 12), (25, 14), (30, 8), (22, 15)]:
    C.append(Q(f"A triangular field has base {b} m and height {h} m. Find its area and the cost of levelling at ₹ 12 per m².", f"Area $=\\tfrac12\\times{b}\\times{h}={b*h//2}$ m² (2); cost ₹ {12*b*h//2} (1).", "2+1"))
C += [
 Q("A path 2 m wide runs around a 20 m × 16 m rectangular garden outside it. Find the area of the path.", "Outer $24\\times20=480$ (1.5); path $480-320=160$ m² (1.5).", "1½+1½"),
 Q("A parallelogram has sides 13 cm and 20 cm and the height on 20 cm is 12 cm. Find its area and the height on the 13 cm side.", "Area 240 cm² (1.5); height $240/13\\approx18.5$ cm (1.5).", "1½+1½"),
 ]
C += [
 Q("The area of a rhombus is 168 cm² and one diagonal is 24 cm. Find the other diagonal and the side.", "Other diagonal 14 cm (1.5); side $\\sqrt{12^2+7^2}\\approx13.9$ cm (1.5).", "1½+1½"),
 Q("A rectangular carpet 6 m × 4 m is laid in a room 8 m × 6 m. Find the uncovered area.", "Room 48 m², carpet 24 m² (2); uncovered 24 m² (1).", "2+1"),
 Q("A triangle and a parallelogram are on the same base 10 cm and between the same parallels 6 cm apart. Compare their areas.", "Triangle 30 cm² (1); parallelogram 60 cm² (1); ratio 1 : 2 (1).", "1+1+1"),
 Q("A square of side 14 cm has a smaller square of side 6 cm removed from a corner. Find the remaining area.", "$196-36=160$ cm² (3).", "3"),
 Q("A trapezium has area 150 cm², parallel sides 12 cm and 18 cm. Find its height.", "$\\tfrac12(30)h=150$ (2); $h=10$ cm (1).", "2+1"),
 Q("Find the area of a right triangle with hypotenuse 25 cm and one leg 7 cm.", "Other leg 24 cm (2); area 84 cm² (1).", "2+1"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Derive the area of a triangle from a rectangle. (ii) Find the area of a triangle with sides 13, 14, 15 using height 12 on side 14.", "(i) A diagonal halves a rectangle; or two congruent triangles make a parallelogram (3). (ii) $\\tfrac12\\times14\\times12=84$ cm² (2).", "3+2"),
 Q("<b>Case study:</b> A farmer's field is a trapezium with parallel sides 60 m and 90 m, and the distance between them 40 m. (i) Find the area. (ii) Cost of ploughing at ₹ 2 per m². (iii) The area in hectares (1 ha = 10000 m²).", "(i) 3000 m² (2). (ii) ₹ 6000 (1). (iii) 0.3 ha (2).", "2+1+2"),
 Q("(i) Derive the area of a trapezium by dividing it into two triangles. (ii) Find the area of a trapezium with parallel sides 20 cm and 30 cm and height 12 cm.", "(i) $\\tfrac12ah+\\tfrac12bh$ (3). (ii) 300 cm² (2).", "3+2"),
 Q("(i) Show that a median divides a triangle into two equal areas. (ii) The area of triangle ABC is 80 cm²; D is the midpoint of BC. Find the area of triangle ABD.", "(i) Equal bases and common height (3). (ii) 40 cm² (2).", "3+2"),
 Q("<b>Case study:</b> A rhombus-shaped tile has diagonals 24 cm and 18 cm. (i) Find the area. (ii) Find the side. (iii) How many tiles to cover 5.4 m² (ignore waste)?", "(i) 216 cm² (2). (ii) 15 cm (1). (iii) $54000/216=250$ tiles (2).", "2+1+2"),
 Q("(i) A rectangle's length is increased by 20% and its breadth decreased by 20%. Find the percent change in area. (ii) Explain.", "(i) $1.2\\times0.8=0.96$, a 4% decrease (3). (ii) Changes multiply (2).", "3+2"),
 Q("(i) Find the area of a quadrilateral with a diagonal of 20 cm and offsets 7 cm and 9 cm to the diagonal. (ii) Name the method.", "(i) $\\tfrac12\\times20\\times(7+9)=160$ cm² (3). (ii) Dividing into two triangles on the diagonal (2).", "3+2"),
 Q("<b>Case study:</b> A rectangular hall 12 m × 8 m has a carpet in the middle leaving a 1 m border. (i) Area of the carpet. (ii) Area of the border. (iii) Cost of polishing the border at ₹ 55/m².", "(i) $10\\times6=60$ m² (2). (ii) $96-60=36$ m² (1). (iii) ₹ 1980 (2).", "2+1+2"),
 Q("(i) Find the area of a parallelogram with base 24 cm and height 15 cm. (ii) If its slant side is 17 cm, find the area of the triangle cut off by the height.", "(i) 360 cm² (2). (ii) Foot distance 8 cm; area $\\tfrac12\\times8\\times15=60$ cm² (3).", "2+3"),
 Q("(i) Rectangles of equal perimeter 40 cm can have different areas. Give four examples. (ii) Which is largest?", "(i) 10×10=100, 12×8=96, 15×5=75, 18×2=36 (3). (ii) 10 × 10 square (2).", "3+2"),
 Q("<b>Case study:</b> A kite-shaped garden has diagonals 40 m and 30 m perpendicular to each other. (i) Find its area. (ii) Compare with a rhombus of the same diagonals. (iii) Cost of grass at ₹ 8 per m².", "(i) 600 m² (2). (ii) Same area (1). (iii) ₹ 4800 (2).", "2+1+2"),
 Q("(i) Show that the area of a rhombus is $\\tfrac12 d_1d_2$. (ii) Find the diagonal if the area is 120 cm² and the other diagonal is 15 cm.", "(i) Four congruent right triangles (3). (ii) 16 cm (2).", "3+2"),
 Q("(i) Find the area of an L-shaped region made of rectangles 10×4 and 6×3. (ii) Suggest another method.", "(i) $40+18=58$ units² (3). (ii) Subtract a missing rectangle from a larger one (2).", "3+2"),
 Q("(i) A square and a rectangle have equal perimeter 48 cm; the rectangle's length is 16 cm. Compare their areas. (ii) What do you conclude?", "(i) Square 144, rectangle $16\\times8=128$ (3). (ii) Square has the larger area (2).", "3+2"),
 Q("<b>Case study:</b> A school ground is a trapezium with parallel sides 120 m and 80 m, and the non-parallel sides 50 m each. (i) Find the height. (ii) Find the area. (iii) Find the cost of turf at ₹ 15 per m².", "(i) Half difference 20; height $\\sqrt{50^2-20^2}\\approx45.8$ m (2). (ii) $\\tfrac12\\times200\\times45.8\\approx4580$ m² (1). (iii) ≈ ₹ 68700 (2).", "2+1+2"),
 Q("(i) Prove that parallelograms on the same base between the same parallels have equal area. (ii) Illustrate with an example.", "(i) Both equal base × common height (3). (ii) Base 10, height 6 gives 60 for both (2).", "3+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
