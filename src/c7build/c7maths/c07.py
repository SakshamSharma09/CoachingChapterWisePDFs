import random
from c7maths.h import *
R = random.Random(707)
A = []; B = []; C = []; D = []
def deg(x): return f"{x}°"
for a, b in [(50, 60), (35, 75), (45, 85), (28, 112), (64, 38), (90, 25), (72, 54), (33, 47)]:
    A.append(M4(f"Two angles of a triangle are {deg(a)} and {deg(b)}. The third angle is:", deg(180 - a - b), [deg(a + b), deg(180 - a), deg(90 - a)], "angle sum is 180°"))
for a, b in [(45, 60), (30, 70), (55, 40), (65, 35)]:
    A.append(M4(f"An exterior angle of a triangle is {deg(a + b)}. If one interior opposite angle is {deg(a)}, the other is:", deg(b), [deg(180 - a - b), deg(a + b + a), deg(180 - b)], "exterior angle = sum of the two interior opposite angles"))
for s in [(3, 4, 5), (2, 3, 6), (5, 7, 12), (6, 8, 10), (4, 4, 9), (7, 10, 12)]:
    a, b, c = s; ok = a + b > c and a + c > b and b + c > a
    A.append(M4(f"Sides {a} cm, {b} cm and {c} cm form a triangle?", "Yes" if ok else "No", ["No" if ok else "Yes", "Only if equal", "Cannot say"], "sum of any two sides must exceed the third"))
for a in [40, 50, 70, 80]:
    A.append(M4(f"In an isosceles triangle the vertex angle is {deg(a)}. Each base angle is:", deg((180 - a) // 2), [deg(a), deg(180 - a), deg(90 - a)], "base angles are equal"))
A += [
 M4("Each angle of an equilateral triangle measures:", "60°", ["30°", "90°", "45°"], "180 ÷ 3"),
 M4("A triangle with all sides different is called:", "scalene", ["isosceles", "equilateral", "right"], "no two sides equal"),
 M4("A triangle with one angle 90° is:", "right-angled", ["acute-angled", "obtuse-angled", "equilateral"], "definition"),
 M4("A triangle with one angle greater than 90° is:", "obtuse-angled", ["right-angled", "acute-angled", "equiangular"], "definition"),
 M4("The perpendicular from a vertex to the opposite side is the:", "altitude", ["median", "bisector", "diagonal"], "forms 90° at the foot"),
 M4("The line joining a vertex to the midpoint of the opposite side is the:", "median", ["altitude", "bisector", "diameter"], "definition"),
 M4("The three altitudes of a triangle meet at a point called:", "orthocentre", ["centroid", "incentre", "circumcentre"], "concurrent"),
 M4("The three medians of a triangle meet at the:", "centroid", ["orthocentre", "incentre", "circumcentre"], "balance point"),
 M4("The number of altitudes in a triangle is:", "3", ["1", "2", "4"], "one from each vertex"),
 M4("The sum of the angles of a triangle is:", "180°", ["90°", "360°", "270°"], "angle sum property"),
 M4("The longest side of a right triangle is called the:", "hypotenuse", ["altitude", "median", "base"], "opposite the right angle"),
 M4("A triangle can have at most ___ obtuse angle(s).", "one", ["two", "three", "none"], "sum is 180°"),
 M4("To construct a triangle uniquely which set is enough?", "three sides", ["three angles", "two angles only", "one side and one angle"], "SSS"),
 M4("The point where the perpendicular bisectors of the sides meet is the:", "circumcentre", ["centroid", "orthocentre", "incentre"], "equidistant from vertices"),
 M4("The exterior angle of a triangle is always:", "greater than each interior opposite angle", ["less than each", "equal to 90°", "equal to 180°"], "sum of the two opposite angles"),
 M4("The perimeter of an equilateral triangle of side 7 cm is:", "21 cm", ["14 cm", "49 cm", "28 cm"], "3 × 7"),
 M4("An equilateral triangle is also:", "equiangular and isosceles", ["right-angled", "scalene", "obtuse"], "all sides equal"),
 M4("In which triangle can the altitude lie outside the triangle?", "obtuse-angled", ["acute-angled", "equilateral", "isosceles acute"], "from the acute vertices"),
]
A = A[:40]
B = [
 Q("State the angle sum property of a triangle.", "The three interior angles of a triangle add to 180° (2).", "2"),
 Q("Find the third angle of a triangle with angles 52° and 68°.", "60° (2).", "2"),
 Q("Define an altitude and a median.", "Altitude is perpendicular from a vertex to the opposite side (1); median joins vertex to midpoint of opposite side (1).", "1+1"),
 Q("Can a triangle have sides 4 cm, 5 cm and 10 cm? Why?", "No; 4 + 5 < 10 (2).", "2"),
 Q("Each angle of an equilateral triangle is how many degrees? Why?", "60°; angles equal and sum 180° (2).", "2"),
 Q("State the exterior angle property.", "An exterior angle equals the sum of the two interior opposite angles (2).", "2"),
 Q("Name the types of triangles based on sides.", "Equilateral, isosceles, scalene (2).", "2"),
 Q("Name the types of triangles based on angles.", "Acute-angled, right-angled, obtuse-angled (2).", "2"),
 Q("If two angles of a triangle are equal to 55° each, find the third and name the triangle.", "70°; isosceles (2).", "2"),
 Q("How many altitudes does a triangle have? Where do they meet?", "Three (1); at the orthocentre (1).", "1+1"),
 Q("Find the perimeter of a triangle with sides 7.5 cm, 6 cm and 9.2 cm.", "22.7 cm (2).", "2"),
 Q("In a right triangle one acute angle is 38°. Find the other.", "52° (2).", "2"),
 Q("Is a triangle with angles 90°, 60°, 40° possible? Why?", "No; sum is 190° (2).", "2"),
 Q("What is the angle between an altitude and the side it falls on?", "90° (2).", "2"),
 Q("Can a triangle have two right angles? Explain.", "No, the sum would be 180° leaving 0 for the third (2).", "2"),
 Q("State the condition for constructing a triangle with sides a, b, c.", "a + b > c, b + c > a and a + c > b (2).", "2"),
]
C = [
 Q("The angles of a triangle are in ratio 2 : 3 : 4. Find them.", "x = 20 (1); 40°, 60°, 80° (2).", "1+2"),
 Q("An exterior angle of a triangle is 110° and one interior opposite angle is 45°. Find the other two angles.", "65° (1.5); 70° (1.5).", "1½+1½"),
 Q("In an isosceles triangle the equal angles are each 4 times the third angle. Find the angles.", "9x = 180; x = 20 (1.5); 20°, 80°, 80° (1.5).", "1½+1½"),
 Q("Check whether sides 5 cm, 6 cm and 12 cm form a triangle. Which side must be reduced?", "5 + 6 < 12 so no (1.5); shorten 12 below 11 (1.5).", "1½+1½"),
 Q("Describe the steps to construct an equilateral triangle of side 5 cm.", "Draw 5 cm base (1); arcs of 5 cm from both ends (1); join the point (1).", "1+1+1"),
 Q("A triangle has angles (x + 10)°, (2x)° and (3x − 10)°. Find x and the angles.", "6x = 180, x = 30 (1.5); 40°, 60°, 80° (1.5).", "1½+1½"),
 Q("How do you construct an altitude of a triangle?", "Place a set square on a side (1); slide so it touches the opposite vertex (1); draw perpendicular (1).", "1+1+1"),
 Q("Find the largest angle of a triangle with angles x, x + 10, x + 20.", "3x + 30 = 180; x = 50 (1.5); largest 70° (1.5).", "1½+1½"),
 Q("Draw the idea of a median and show that a triangle has three.", "Each vertex joins the midpoint of the opposite side (1.5); gives three medians (1.5).", "1½+1½"),
 Q("A right triangle's acute angles differ by 20°. Find them.", "x + x + 20 = 90 (1.5); 35° and 55° (1.5).", "1½+1½"),
 Q("The perimeter of an isosceles triangle is 36 cm and the base 10 cm. Find the equal sides.", "(36 − 10) ÷ 2 = 13 cm (3).", "3"),
 Q("Is a triangle with sides 3 cm, 4 cm, 5 cm right-angled? Verify with squares.", "9 + 16 = 25 (2); yes (1).", "2+1"),
 Q("Find the angles of an equilateral triangle and an exterior angle at one vertex.", "60° each (1.5); exterior 120° (1.5).", "1½+1½"),
 Q("In triangle ABC, ∠A = 70°, ∠B = ∠C. Find ∠B.", "55° (3).", "3"),
 Q("State the difference between acute-angled and obtuse-angled triangles with example angles.", "All angles < 90° (1.5); one angle > 90° (1.5).", "1½+1½"),
 Q("Two sides of a triangle are 8 cm and 5 cm. Between which values must the third side lie?", "Greater than 3 cm and less than 13 cm (3).", "3"),
 Q("Name the centre where the three perpendicular bisectors meet and state its property.", "Circumcentre (1); equidistant from the three vertices (2).", "1+2"),
 Q("If each angle of a triangle is less than 60° is it possible? Explain.", "No, the sum would be less than 180° (3).", "3"),
 Q("What is the sum of exterior angles (one at each vertex) of a triangle?", "360° (3).", "3"),
 Q("A ladder 5 m long leans on a wall reaching 4 m. How far is its foot from the wall?", "3 m (3).", "3"),
 Q("Draw a triangle with sides 4 cm, 5 cm and 6 cm and describe steps.", "Draw 6 cm base (1); arcs 4 cm and 5 cm (1); join (1).", "1+1+1"),
 Q("Find x in a triangle with angles 2x, 3x and 4x.", "9x = 180 (1.5); x = 20° (1.5).", "1½+1½"),
 Q("Find the angle between two equal sides of an isosceles triangle with base angle 65°.", "50° (3).", "3"),
 Q("The altitude of an equilateral triangle bisects the base. Explain.", "Two congruent right triangles formed (3).", "3"),
]
D = [
 Q("(i) Prove the angle sum property by tearing the corners. (ii) Find the missing angle if two are 63° and 47°. (iii) Name the triangle.", "(i) The three corners form a straight line (2). (ii) 70° (2). (iii) acute scalene (1).", "2+2+1"),
 Q("<b>Case study:</b> A roof truss is an isosceles triangle with apex 100°. (i) Find base angles. (ii) Find the exterior angle at the apex. (iii) Name the type of triangle. (iv) The two equal rafters are 4 m each; find the perimeter if the base is 6 m.", "(i) 40° each (1). (ii) 80° (1). (iii) Obtuse isosceles (1). (iv) 14 m (2).", "1+1+1+2"),
 Q("(i) Construct a triangle with sides 4 cm, 5 cm, 6 cm — list the steps. (ii) Draw an altitude from the 6 cm side. (iii) Mark the orthocentre.", "(i) Base 6; arcs 4 and 5 (2). (ii) Set square (2). (iii) Intersection of altitudes (1).", "2+2+1"),
 Q("(i) State the triangle inequality. (ii) Which sets form triangles: (3,4,8), (5,6,10), (2,2,3)? (iii) Justify one.", "(i) Sum of any two sides exceeds the third (1). (ii) No, yes, yes (3). (iii) 3 + 4 < 8 (1).", "1+3+1"),
 Q("<b>Case study:</b> A triangular plot ABC has ∠A = 50°, ∠B = 60°. (i) Find ∠C. (ii) Which side is the longest? (iii) An exterior angle at C. (iv) The type of triangle.", "(i) 70° (1). (ii) Opposite the largest angle: AB (1). (iii) 110° (1). (iv) acute-angled scalene (2).", "1+1+1+2"),
 Q("(i) Find the angles of a triangle if they are in ratio 1 : 2 : 3. (ii) Name the triangle. (iii) Find the exterior angle at the largest.", "(i) 30°, 60°, 90° (2). (ii) right-angled (1). (iii) 90° (2).", "2+1+2"),
 Q("(i) Show the exterior angle property using a diagram. (ii) If the interior opposite angles are 38° and 52°, find the exterior. (iii) Find the third angle.", "(i) Exterior + interior adjacent = 180 (2). (ii) 90° (1.5). (iii) 90° (1.5).", "2+1½+1½"),
 Q("(i) Construct a right triangle with hypotenuse 5 cm and a side 3 cm. (ii) Find the third side. (iii) Find the area.", "(i) Steps (2). (ii) 4 cm (1.5). (iii) 6 cm² (1.5).", "2+1½+1½"),
 Q("<b>Case study:</b> Three villages A, B, C are at distances AB = 6 km, BC = 8 km, CA = 10 km. (i) Do they form a triangle? (ii) Is it right-angled? (iii) The shortest path from A to C via B. (iv) The extra distance compared with the direct road.", "(i) Yes (1). (ii) Yes: 36 + 64 = 100 (1). (iii) 14 km (1). (iv) 4 km (2).", "1+1+1+2"),
 Q("(i) How many medians does a triangle have? (ii) What is their meeting point called? (iii) State a property of it.", "(i) Three (1). (ii) Centroid (1). (iii) Divides each median in the ratio 2 : 1 (3).", "1+1+3"),
 Q("(i) The vertex angle of an isosceles triangle is 40°. Find each base angle. (ii) Name the type of triangle. (iii) Find an exterior angle at the vertex.", "(i) 70° each (2). (ii) acute isosceles (1). (iii) 140° (2).", "2+1+2"),
 Q("(i) Find the perimeter of an equilateral triangle of side 8.5 cm. (ii) Find the side if the perimeter is 40.5 cm. (iii) Find each angle.", "(i) 25.5 cm (2). (ii) 13.5 cm (2). (iii) 60° (1).", "2+2+1"),
 Q("<b>Case study:</b> A kite-shaped frame uses triangles. One triangle has ∠P = 90°, ∠Q = 37°. (i) Find ∠R. (ii) Largest side. (iii) Exterior angle at Q. (iv) If PQ = 6, QR = 10, find PR.", "(i) 53° (1). (ii) QR (1). (iii) 143° (1). (iv) 8 (2).", "1+1+1+2"),
 Q("(i) Why can there be no triangle with two obtuse angles? (ii) Give an example of sides that fail. (iii) Verify with 100° + 100°.", "(i) Sum would exceed 180° (2). (ii) 2, 3, 6 (1). (iii) 200° > 180° (2).", "2+1+2"),
 Q("(i) Draw an obtuse triangle and show its three altitudes. (ii) Where does the orthocentre lie? (iii) Does it lie inside?", "(i) Two altitudes outside (2). (ii) Outside the triangle (2). (iii) No (1).", "2+2+1"),
 Q("(i) Show that the sum of exterior angles is 360°. (ii) Find the third exterior angle if two are 130° and 120°. (iii) Check.", "(i) 3 × 180 − 180 = 360 (2). (ii) 110° (2). (iii) 130 + 120 + 110 = 360 (1).", "2+2+1"),
]
D = D[:16]
SETS, POOL = build(A, B, C, D)
