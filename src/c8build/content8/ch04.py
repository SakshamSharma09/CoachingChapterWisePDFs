from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
# A: missing angle in a quadrilateral (6)
for a, b, c in [(80, 100, 90), (65, 85, 110), (70, 120, 75), (95, 105, 60), (50, 130, 90), (88, 92, 100)]:
    d = 360 - a - b - c
    A.append(M4(f"Three angles of a quadrilateral are {a}°, {b}° and {c}°. The fourth angle is:", f"{d}°", [f"{d+10}°", f"{d-10}°", f"{180-d}°", f"{d+20}°"], "Angle sum of a quadrilateral is 360°"))
# A: parallelogram angle (4)
for x in [65, 72, 108, 115]:
    A.append(M4(f"One angle of a parallelogram is {x}°. Its adjacent angle is:", f"{180-x}°", [f"{x}°", f"{abs(90-x)}°", f"{360-2*x}°", f"{x+20}°"], "Adjacent angles are supplementary"))
# A: rhombus / diagonals (4)
for d1, d2 in [(6, 8), (10, 24), (16, 30), (12, 16)]:
    side = ((d1/2) ** 2 + (d2/2) ** 2) ** .5
    A.append(M4(f"The diagonals of a rhombus are {d1} cm and {d2} cm. Its side is:", f"{side:g} cm", [f"{side+1:g} cm", f"{side-1:g} cm", f"{(d1+d2)/2:g} cm"], "Diagonals bisect at right angles; use Pythagoras"))
# A: rectangle diagonal (3)
for l, b in [(6, 8), (5, 12), (9, 12)]:
    dg = (l*l + b*b) ** .5
    A.append(M4(f"The diagonal of a rectangle with sides {l} cm and {b} cm is:", f"{dg:g} cm", [f"{l+b} cm", f"{dg+1:g} cm", f"{dg-1:g} cm"], r"$\sqrt{l^2+b^2}$"))
# A: concepts (23)
A += [
 M4("A quadrilateral with all sides equal and all angles 90° is a:", "square", ["rhombus", "rectangle", "kite"], "Regular quadrilateral"),
 M4("A quadrilateral with only one pair of parallel sides is a:", "trapezium", ["parallelogram", "kite", "rhombus"], "Trapezium"),
 M4("The diagonals of a rectangle are:", "equal and bisect each other", ["perpendicular", "unequal", "parallel"], "Rectangle property"),
 M4("Diagonals that bisect each other at right angles but are unequal belong to a:", "rhombus", ["rectangle", "kite", "trapezium"], "Rhombus property"),
 M4("The sum of the interior angles of a quadrilateral is:", "360°", ["180°", "270°", "540°"], "Two triangles"),
 M4("Opposite sides of a parallelogram are:", "parallel and equal", ["only parallel", "only equal", "perpendicular"], "Basic property"),
 M4("Which quadrilateral has two pairs of equal adjacent sides?", "kite", ["parallelogram", "rectangle", "trapezium"], "Kite"),
 M4("In a kite, the diagonals:", "meet at right angles", ["are equal", "bisect each other", "are parallel"], "Kite property"),
 M4("Every square is a:", "rhombus", ["kite only", "trapezium only", "scalene triangle"], "Square has all sides equal"),
 M4("Every rectangle is a:", "parallelogram", ["square", "rhombus", "kite"], "Opposite sides are parallel"),
 M4("A parallelogram with equal diagonals is a:", "rectangle", ["rhombus", "kite", "trapezium"], "Rectangle property"),
 M4("The diagonals of a parallelogram:", "bisect each other", ["are equal", "are perpendicular", "are parallel"], "Parallelogram property"),
 M4("The number of diagonals of a quadrilateral is:", "2", ["1", "3", "4"], "Two diagonals"),
 M4("A rhombus is a parallelogram in which:", "all sides are equal", ["all angles are 90°", "diagonals are equal", "one pair is parallel"], "Rhombus"),
 M4("In a parallelogram ABCD, angle A is 110°. Angle C is:", "110°", ["70°", "90°", "250°"], "Opposite angles are equal"),
 M4("An isosceles trapezium has:", "equal non-parallel sides", ["equal parallel sides", "four right angles", "perpendicular diagonals"], "Property"),
 M4("The exterior angle sum of any quadrilateral is:", "360°", ["180°", "720°", "540°"], "One at each vertex"),
 M4("A rectangle that is also a rhombus is a:", "square", ["kite", "trapezium", "parallelogram only"], "Both properties"),
 M4("Which of the following cannot have a pair of parallel sides?", "kite (in general)", ["rectangle", "rhombus", "trapezium"], "Kite need not be parallel"),
 M4("A diagonal of a rectangle divides it into:", "two congruent right triangles", ["two equilateral triangles", "two parallelograms", "three triangles"], "Property"),
 M4("The angles of a rectangle are each:", "90°", ["60°", "45°", "180°"], "Four right angles"),
 M4("In rhombus ABCD, diagonal AC bisects angle:", "A and C", ["B only", "D only", "none"], "Diagonals bisect vertex angles"),
 M4("A quadrilateral in which both pairs of opposite angles are equal is a:", "parallelogram", ["trapezium", "kite", "scalene quad"], "Converse property"),
]
assert len(A) == 40, len(A)
B = [
 Q("State the angle sum property of a quadrilateral.", "The four interior angles add up to $360^\\circ$ (2).", "2"),
 Q("Three angles of a quadrilateral are 75°, 105° and 90°. Find the fourth.", "$360-270=90^\\circ$ (2).", "2"),
 Q("List two properties of the diagonals of a rectangle.", "They are equal (1); they bisect each other (1).", "1+1"),
 Q("List two properties of the diagonals of a rhombus.", "They bisect each other at right angles (1); they bisect the vertex angles (1).", "1+1"),
 Q("Why is every square a rectangle?", "A square has four right angles and opposite sides equal (2).", "2"),
 Q("Differentiate between a kite and a rhombus.", "Kite: two pairs of equal adjacent sides (1); rhombus: all four sides equal (1).", "1+1"),
 Q("In a parallelogram, one angle is 70°. Find the other three.", "Opposite 70°, adjacent angles 110° and 110° (2).", "2"),
 Q("Which quadrilateral has exactly one pair of parallel sides? Give an example from daily life.", "Trapezium (1); e.g. a tabletop shape or a bucket's side (1).", "1+1"),
 Q("Can a quadrilateral have all four angles acute? Why?", "No, the sum would be less than 360° (2).", "2"),
 Q("What is the sum of adjacent angles of a parallelogram?", "180° (2).", "2"),
 Q("Name the special quadrilaterals whose diagonals are perpendicular.", "Rhombus, square and kite (2).", "2"),
 Q("The diagonals of a rectangle are 26 cm each. Find AC and BD and say if they bisect each other.", "AC = BD = 26 cm (1); they bisect at the centre, each half 13 cm (1).", "1+1"),
 Q("Draw/describe a quadrilateral with equal diagonals that are not perpendicular.", "A rectangle (2).", "2"),
 Q("An isosceles trapezium has base angles 65°. Find the other two angles.", "$180-65=115^\\circ$ each (2).", "2"),
 Q("Find each angle of a rhombus if one angle is 4 times its adjacent angle.", "$x+4x=180$, $x=36^\\circ$ and $144^\\circ$ (2).", "2"),
 Q("State why a square is a special rhombus.", "It has all sides equal and also right angles (2).", "2"),
]
for r in [(2, 3, 4, 3), (1, 2, 3, 4), (3, 4, 5, 6), (2, 2, 3, 3), (4, 5, 6, 5), (1, 3, 4, 7)]:
    t = sum(r); x = 360 / t
    C.append(Q(f"The angles of a quadrilateral are in the ratio {':'.join(map(str, r))}. Find all the angles.", f"Let angles be ${r[0]}x,{r[1]}x,{r[2]}x,{r[3]}x$ (1); $x=360/{t}={x:g}$ (1); angles {', '.join(f'{int(v*x) if (v*x).is_integer() else round(v*x,1)}°' for v in r)} (1).", "1+1+1"))
for d1, d2 in [(10, 24), (14, 48), (16, 30), (18, 24)]:
    s = ((d1/2) ** 2 + (d2/2) ** 2) ** .5
    C.append(Q(f"Diagonals of a rhombus are {d1} cm and {d2} cm. Find the side and perimeter.", f"Half-diagonals {d1//2}, {d2//2} form a right triangle (1); side $={s:g}$ cm (1); perimeter $={4*s:g}$ cm (1).", "1+1+1"))
C += [
 Q("Prove that the opposite angles of a parallelogram are equal.", "Adjacent angles are supplementary: $A+B=180^\\circ$, $B+C=180^\\circ$ (2); so $A=C$ (1).", "2+1"),
 Q("In parallelogram ABCD, $\\angle A=(3x+10)^\\circ$ and $\\angle B=(2x-10)^\\circ$. Find all angles.", "$5x=180$, $x=36$ (1); $A=118^\\circ$, $B=62^\\circ$ (1); $C=118^\\circ$, $D=62^\\circ$ (1).", "1+1+1"),
 Q("A kite has diagonals 12 cm and 16 cm. Find its area.", "Area $=\\tfrac12 d_1d_2=\\tfrac12\\times12\\times16$ (2); $96$ cm² (1).", "2+1"),
 Q("Show that diagonals of a rectangle are equal using Pythagoras.", "Both diagonals are hypotenuses of right triangles with legs $l$ and $b$ (2); so both $=\\sqrt{l^2+b^2}$ (1).", "2+1"),
 Q("A trapezium has parallel sides 10 cm and 6 cm and height 4 cm. Find its area.", "$\\tfrac12(10+6)\\times4$ (2); 32 cm² (1).", "2+1"),
 Q("Which special quadrilaterals have all of: four equal sides and equal diagonals?", "Only the square (1.5); because a rhombus has unequal diagonals (1.5).", "1½+1½"),
 Q("The diagonals of a quadrilateral bisect each other. Which quadrilaterals can it be? Why?", "Parallelogram, rectangle, rhombus, square (2); property of parallelograms (1).", "2+1"),
 Q("In kite ABCD, AB = AD and CB = CD. If $\\angle B=\\angle D=90^\\circ$ and $\\angle A=70^\\circ$, find $\\angle C$.", "Angle sum $=360^\\circ$ (1); $C=360-90-90-70$ (1); $110^\\circ$ (1).", "1+1+1"),
 Q("A rectangular park is 40 m by 30 m. Find the length of the diagonal path across it.", "$\\sqrt{40^2+30^2}$ (2); $50$ m (1).", "2+1"),
]
assert len(B) == 16, len(B)
C += [
 Q("A parallelogram has adjacent sides 12 cm and 9 cm. Find its perimeter. Is its area 108 cm²? Explain.", "Perimeter $=2(12+9)=42$ cm (1.5); area needs the height, not just sides (1.5).", "1½+1½"),
 Q("The angles of a quadrilateral are $x^\\circ,\\ (x+20)^\\circ,\\ (x+40)^\\circ,\\ (x+60)^\\circ$. Find $x$.", "Sum: $4x+120=360$ (1.5); $x=60$ (1.5).", "1½+1½"),
 Q("Explain with a figure idea why a trapezium is not a parallelogram.", "Only one pair of opposite sides is parallel in a trapezium (3).", "3"),
 Q("Name the quadrilateral formed by joining the midpoints of consecutive sides of a rectangle and state a reason.", "A rhombus (1); each side is half a diagonal and diagonals are equal (2).", "1+2"),
 Q("A square has diagonal 14 cm. Find its area using $\\tfrac12d^2$.", "$\\tfrac12\\times14^2=98$ cm² (3).", "3"),
]
C = C[:24]
assert len(C) == 24, len(C)
D = [
 Q("(i) Prove that the sum of the angles of a quadrilateral is 360°. (ii) Find the fourth angle if three are 85°, 95° and 70°.", "(i) A diagonal splits it into two triangles, each 180° (3). (ii) $360-250=110^\\circ$ (2).", "3+2"),
 Q("(i) List the properties of a parallelogram. (ii) In parallelogram PQRS, $\\angle P=(2x+20)^\\circ$, $\\angle Q=(3x-10)^\\circ$. Find $x$ and all angles.", "(i) Opposite sides and angles equal, diagonals bisect, adjacent angles supplementary (2). (ii) $5x+10=180$, $x=34$; $P=88^\\circ$, $Q=92^\\circ$, $R=88^\\circ$, $S=92^\\circ$ (3).", "2+3"),
 Q("(i) Compare a rhombus and a rectangle on sides, angles and diagonals. (ii) State the quadrilateral that is both.", "(i) Rhombus: equal sides, unequal diagonals meeting at right angles; rectangle: equal diagonals, right angles (3). (ii) Square (2).", "3+2"),
 Q("<b>Case study:</b> A kite-maker uses two sticks of length 60 cm and 40 cm placed perpendicular so that the shorter stick is bisected. (i) Name the shape. (ii) Find the area of paper. (iii) Is it a rhombus?", "(i) Kite (1). (ii) $\\tfrac12\\times60\\times40=1200$ cm² (2). (iii) Only if both sticks bisect each other (2).", "1+2+2"),
 Q("(i) The diagonals of a rhombus are 30 cm and 40 cm. Find its side, perimeter and area. (ii) Find the height if the base is the side.", "(i) Side 25 cm, perimeter 100 cm, area $\\tfrac12\\times30\\times40=600$ cm² (3). (ii) Height $600/25=24$ cm (2).", "3+2"),
 Q("(i) Prove that the diagonals of a rectangle are equal. (ii) Use it to find the diagonal of a 9 m by 12 m rectangle.", "(i) Congruent triangles by SAS (3). (ii) 15 m (2).", "3+2"),
 Q("<b>Case study:</b> A rectangular tabletop has sides 150 cm and 80 cm. (i) Find its diagonal. (ii) Find the perimeter. (iii) A ribbon is to cover both diagonals; find the length.", "(i) $\\sqrt{150^2+80^2}=170$ cm (2). (ii) $460$ cm (1). (iii) $340$ cm (2).", "2+1+2"),
 Q("(i) State five types of quadrilateral and one property of each. (ii) Which one has only one pair of parallel sides?", "(i) Parallelogram, rectangle, rhombus, square, trapezium, kite with properties (3). (ii) Trapezium (2).", "3+2"),
 Q("(i) In trapezium ABCD, AB ∥ CD and $\\angle A=70^\\circ$, $\\angle B=80^\\circ$. Find $\\angle C$ and $\\angle D$. (ii) Why?", "(i) $D=110^\\circ$, $C=100^\\circ$ (3). (ii) Co-interior angles are supplementary (2).", "3+2"),
 Q("(i) Show that the angle bisectors of a parallelogram form a rectangle (state the idea). (ii) Give the angle at each corner of this rectangle.", "(i) Adjacent angle bisectors meet at 90° because half of the supplementary angles is 90° (3). (ii) 90° (2).", "3+2"),
 Q("<b>Case study:</b> A tile is a rhombus of side 13 cm with a diagonal of 24 cm. (i) Find the other diagonal. (ii) Find the area. (iii) How many tiles cover 3 m²?", "(i) Half diagonals 12 and 5; other diagonal 10 cm (2). (ii) $\\tfrac12\\times24\\times10=120$ cm² (1). (iii) $30000/120=250$ tiles (2).", "2+1+2"),
 Q("(i) Find all angles of a quadrilateral whose angles are in ratio 1:2:3:4. (ii) Is it a trapezium? Explain.", "(i) $36^\\circ,72^\\circ,108^\\circ,144^\\circ$ (3). (ii) Yes, if the sides with 36° and 144° are parallel; angles sum to 180° (2).", "3+2"),
 Q("(i) Prove that a quadrilateral with equal opposite sides is a parallelogram (describe the proof). (ii) Give a real-life example.", "(i) A diagonal gives congruent triangles, so alternate angles equal (3). (ii) A folding gate or a parallelogram linkage (2).", "3+2"),
 Q("(i) Find the length of the sides of a square whose diagonal is $10\\sqrt2$ cm. (ii) Find its area.", "(i) Side $=10$ cm (3). (ii) 100 cm² (2).", "3+2"),
 Q("<b>Case study:</b> A farmer's field is a trapezium with parallel sides 90 m and 60 m, and height 40 m. (i) Find the area. (ii) Cost of levelling at ₹5 per m². (iii) Why is it a trapezium?", "(i) $\\tfrac12(90+60)\\times40=3000$ m² (2). (ii) ₹15000 (1). (iii) One pair of sides parallel (2).", "2+1+2"),
 Q("(i) What is an interior angle? Find each exterior angle of a rectangle. (ii) Show that the sum of exterior angles of a quadrilateral is 360°.", "(i) Angle inside at a vertex; exterior $90^\\circ$ (2). (ii) Each exterior = 180° − interior; total $720-360=360^\\circ$ (3).", "2+3"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
