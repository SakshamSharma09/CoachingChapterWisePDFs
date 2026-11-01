import random
from c7maths.h import *
R = random.Random(705)
A = []; B = []; C = []; D = []
def deg(x): return f"{x}°"
for x in [25, 38, 47, 62, 73, 16]:
    A.append(M4(f"The complement of {deg(x)} is:", deg(90 - x), [deg(180 - x), deg(90 + x), deg(x)], "angles sum to 90°"))
for x in [35, 72, 118, 143, 105, 64]:
    A.append(M4(f"The supplement of {deg(x)} is:", deg(180 - x), [deg(90 - x) if x < 90 else deg(x - 90), deg(360 - x), deg(x)], "angles sum to 180°"))
for x in [40, 55, 125, 68]:
    A.append(M4(f"Two lines intersect and one angle is {deg(x)}. The vertically opposite angle is:", deg(x), [deg(180 - x), deg(90 - x) if x < 90 else deg(x - 90), deg(360 - 2 * x)], "vertically opposite angles are equal"))
for x in [50, 112, 85, 133]:
    A.append(M4(f"In a linear pair, one angle is {deg(x)}. The other is:", deg(180 - x), [deg(x), deg(90 - x) if x < 90 else deg(x - 90), deg(360 - x)], "linear pair sums to 180°"))
for x in [48, 77, 130, 104]:
    A.append(M4(f"A transversal cuts two parallel lines. A corresponding angle to {deg(x)} is:", deg(x), [deg(180 - x), deg(90 - x) if x < 90 else deg(x - 90), deg(2 * x) if 2 * x < 180 else deg(x // 2)], "corresponding angles are equal"))
for x in [58, 120, 95, 41]:
    A.append(M4(f"A transversal cuts parallel lines. If an alternate interior angle is {deg(x)}, its pair is:", deg(x), [deg(180 - x), deg(90 - x) if x < 90 else deg(x - 90), deg(x + 10)], "alternate angles are equal"))
A += [
 M4("Two lines in a plane that never meet are called:", "parallel lines", ["perpendicular lines", "intersecting lines", "transversals"], "constant distance apart"),
 M4("Lines that meet at 90° are called:", "perpendicular lines", ["parallel lines", "oblique lines", "skew lines"], "right angle"),
 M4("A line that cuts two or more lines at different points is a:", "transversal", ["bisector", "perpendicular", "diameter"], "definition"),
 M4("The sum of co-interior angles on the same side of a transversal between parallel lines is:", "180°", ["90°", "360°", "Equal"], "supplementary"),
 M4("Vertically opposite angles are always:", "equal", ["supplementary", "complementary", "unequal"], "formed by two intersecting lines"),
 M4("An angle of 90° is called a:", "right angle", ["straight angle", "acute angle", "reflex angle"], "perpendicular"),
 M4("The angles on a straight line add up to:", "180°", ["90°", "360°", "270°"], "straight angle"),
 M4("Angles around a point add up to:", "360°", ["180°", "90°", "720°"], "full turn"),
 M4("An angle greater than 90° and less than 180° is:", "obtuse", ["acute", "reflex", "right"], "definition"),
 M4("If two angles are supplementary and one is 60°, the other is:", "120°", ["30°", "300°", "60°"], "180 − 60"),
 M4("Parallel lines can be drawn using a set square and a:", "ruler", ["compass only", "protractor only", "divider"], "slide the set square along a ruler"),
 M4("If a transversal makes alternate angles equal, the two lines are:", "parallel", ["perpendicular", "intersecting at 90°", "equal"], "converse of alternate angle property"),
 M4("The number of angles formed when a transversal cuts two lines is:", "8", ["4", "6", "2"], "four at each intersection"),
 M4("If one angle of a linear pair is acute, the other is:", "obtuse", ["acute", "right", "reflex"], "sum is 180°"),
 M4("The railway tracks give an example of:", "parallel lines", ["intersecting lines", "perpendicular lines", "transversals"], "constant distance"),
]
A = A[:40]
B = [
 Q("Define parallel and intersecting lines.", "Parallel lines never meet however far extended (1); intersecting lines meet at a point (1).", "1+1"),
 Q("State the vertically opposite angle property.", "Vertically opposite angles formed by two intersecting lines are equal (2).", "2"),
 Q("Find the complement and supplement of 35°.", "55° (1); 145° (1).", "1+1"),
 Q("What is a linear pair? Give its measure.", "Two adjacent angles on a straight line (1); they add to 180° (1).", "1+1"),
 Q("Name the pairs of angles formed by a transversal across two parallel lines (any three).", "Corresponding, alternate interior, co-interior (2).", "2"),
 Q("Two angles are in a linear pair and one is 3 times the other. Find them.", "45° and 135° (2).", "2"),
 Q("If two intersecting lines make an angle of 70°, find the other three angles.", "70°, 110°, 110° (2).", "2"),
 Q("How can you check if two lines are parallel using a transversal?", "If corresponding (or alternate) angles are equal (2).", "2"),
 Q("Two lines are perpendicular. How many right angles do they form?", "Four (2).", "2"),
 Q("What is the angle between the hands of a clock at 3 o'clock?", "90° (2).", "2"),
 Q("Find x if x and 2x are supplementary.", "3x = 180°, x = 60° (2).", "2"),
 Q("Find x if angles x and (x + 20°) are complementary.", "2x + 20 = 90; x = 35° (2).", "2"),
 Q("What are alternate interior angles?", "Pairs of angles on opposite sides of the transversal, between the lines (2).", "2"),
 Q("In a pair of parallel lines cut by a transversal, one co-interior angle is 110°. Find the other.", "70° (2).", "2"),
 Q("Write one real-life example each of parallel lines and perpendicular lines.", "Railway tracks (1); the corner of a table (1).", "1+1"),
 Q("The angles around a point are 90°, 120°, 100° and x. Find x.", "50° (2).", "2"),
]
C = [
 Q("Two lines intersect so that one angle is 4x and the adjacent angle is 5x. Find all four angles.", "9x = 180, x = 20 (1.5); 80°, 100°, 80°, 100° (1.5).", "1½+1½"),
 Q("A transversal cuts two parallel lines. A corresponding angle is 65°. Find all eight angles' values.", "Four angles 65° and four angles 115° (3).", "3"),
 Q("Find x if corresponding angles are (3x + 10)° and (5x − 30)° and lines are parallel.", "3x + 10 = 5x − 30 (1.5); x = 20 (1.5).", "1½+1½"),
 Q("If a transversal cuts two lines and alternate angles are 72° and 72°, what do you conclude?", "The lines are parallel (1.5); converse of alternate angles property (1.5).", "1½+1½"),
 Q("Explain how to draw a line through P parallel to a given line using ruler and set square.", "Place ruler along the line (1); slide set square to touch P (1); draw line along edge (1).", "1+1+1"),
 Q("Two co-interior angles are (2x + 15)° and (3x + 5)°. If lines are parallel, find x.", "5x + 20 = 180 (1.5); x = 32 (1.5).", "1½+1½"),
 Q("Find the angle whose supplement is thrice its complement.", "180 − x = 3(90 − x) (1.5); x = 45° (1.5).", "1½+1½"),
 Q("Four angles at a point are x, 2x, 3x and 4x. Find x.", "10x = 360 (1.5); x = 36° (1.5).", "1½+1½"),
 Q("Prove that vertically opposite angles are equal.", "a + b = 180 and b + c = 180 (1.5); so a = c (1.5).", "1½+1½"),
 Q("A ladder leans making 70° with the ground. Find the angle with the wall.", "90 − 70 = 20° (3).", "3"),
 Q("Two lines AB and CD meet at O, with ∠AOC = 125°. Find ∠BOD, ∠AOD.", "∠BOD = 125° (1.5); ∠AOD = 55° (1.5).", "1½+1½"),
 Q("State true or false with reason: Two acute angles can be supplementary.", "False (1); acute + acute < 180° (2).", "1+2"),
 Q("The complement of an angle is 20° more than the angle. Find it.", "90 − x = x + 20 (1.5); x = 35° (1.5).", "1½+1½"),
 Q("What kind of angle is formed at 6 o'clock and at 4 o'clock by the clock hands?", "180° straight (1.5); 120° obtuse (1.5).", "1½+1½"),
 Q("In a figure two parallel lines are cut by a transversal; angle 1 = 4x and angle 2 (co-interior) = 5x. Find angles.", "9x = 180 (1.5); 80° and 100° (1.5).", "1½+1½"),
 Q("The angles of a linear pair are in ratio 2 : 3. Find them.", "72° and 108° (3).", "3"),
 Q("Give a method to check if two lines in a notebook are perpendicular.", "Use a set square corner or measure 90° with a protractor (3).", "3"),
 Q("Two parallel lines are cut by a transversal. Alternate angle is (2x + 10)° and (x + 40)°. Find x.", "2x + 10 = x + 40 (1.5); x = 30 (1.5).", "1½+1½"),
 Q("Find ∠x in a straight line with angles 40°, 65° and x.", "x = 75° (3).", "3"),
 Q("Why are the opposite edges of a ruler parallel? What measurement shows it?", "Distance stays the same everywhere (3).", "3"),
 Q("A transversal cuts parallel lines; angle ∠1 = 52°. Find the alternate and co-interior angles of ∠1.", "Alternate 52° (1.5); co-interior 128° (1.5).", "1½+1½"),
 Q("Find the reflex angle formed by the hands of a clock at 9 o'clock.", "270° (3).", "3"),
 Q("Three lines meet at a point forming angles x, x + 30° and 2x + 30° on a straight line. Find x.", "4x + 60 = 180 (1.5); x = 30° (1.5).", "1½+1½"),
 Q("Explain why intersecting lines produce two pairs of equal angles.", "Opposite angles equal, adjacent are linear pairs (3).", "3"),
]
D = [
 Q("(i) Define a transversal. (ii) Name the angle pairs formed. (iii) If a corresponding angle is 75°, find the other seven angles.", "(i) A line cutting two lines at distinct points (1). (ii) Corresponding, alternate, co-interior, vertically opposite (2). (iii) four of 75°, four of 105° (2).", "1+2+2"),
 Q("<b>Case study:</b> Two roads AB and CD are parallel and a road EF crosses them. At A the angle ∠EAB = 68°. (i) Find the angle at C corresponding to it. (ii) Find the alternate angle. (iii) Find the co-interior angle. (iv) Are AB and CD parallel? Why?", "(i) 68° (1). (ii) 68° (1). (iii) 112° (1). (iv) Yes, equal corresponding angles (2).", "1+1+1+2"),
 Q("(i) Find x: angles (4x − 10)° and (2x + 30)° are alternate on parallel lines. (ii) Find the angles. (iii) Find their co-interior angles.", "(i) x = 20 (2). (ii) 70° each (1). (iii) 110° (2).", "2+1+2"),
 Q("(i) Prove that a linear pair sums to 180°. (ii) Find the angles if one is 40° more than the other. (iii) Name each.", "(i) Straight angle (2). (ii) 70° and 110° (2). (iii) acute and obtuse (1).", "2+2+1"),
 Q("<b>Case study:</b> A kite flies with its string making 62° with the ground; a flag pole is vertical. (i) Angle between string and pole. (ii) Name the types. (iii) What angle at the foot? (iv) Supplementary of 62°.", "(i) 28° (1). (ii) 62° acute (1). (iii) 90° (1). (iv) 118° (2).", "1+1+1+2"),
 Q("(i) Draw a line l and a point P outside it and describe the construction of a parallel line. (ii) Verify with alternate angles.", "(i) Steps with set square and ruler (3). (ii) Equal alternate angles measured (2).", "3+2"),
 Q("(i) Find x and y in two intersecting lines where angles are (3x + 20)°, (y)°, (5x − 40)°. (ii) State property used.", "(i) 3x + 20 = 5x − 40; x = 30; the angle is 110°; y = 70° (4). (ii) Vertically opposite angles equal (1).", "4+1"),
 Q("(i) The supplement of an angle is 5 times its complement. Form the equation. (ii) Find the angle. (iii) Verify.", "(i) 180 − x = 5(90 − x) (1). (ii) x = 67.5° (2). (iii) 112.5 = 5 × 22.5 (2).", "1+2+2"),
 Q("<b>Case study:</b> The two railway tracks are parallel and a road crosses them making 105° with one track. (i) Corresponding angle. (ii) Co-interior angle. (iii) Number of different angle measures. (iv) Are the tracks parallel to each other?", "(i) 105° (1). (ii) 75° (1). (iii) Two (1). (iv) Yes (2).", "1+1+1+2"),
 Q("(i) Six angles around a point are x, 2x, 3x, 3x, 4x and 5x. Find x. (ii) Find the largest angle. (iii) Is it obtuse?", "(i) 18x = 360, x = 20° (3). (ii) 100° (1). (iii) Yes (1).", "3+1+1"),
 Q("(i) In a figure ∠1 and ∠2 are a linear pair, ∠1 = 3y + 15, ∠2 = 2y + 15. Find y. (ii) Find angles. (iii) Vertically opposite angles?", "(i) 5y + 30 = 180, y = 30 (2). (ii) 105° and 75° (2). (iii) 105°, 75° (1).", "2+2+1"),
 Q("(i) Why are alternate angles equal for parallel lines? (ii) Use a diagram idea to explain. (iii) Give a daily-life use.", "(i) Corresponding equal and vertically opposite equal (2). (ii) combine two properties (2). (iii) Ladder rungs, road design (1).", "2+2+1"),
 Q("(i) Find the angle between the hands at 4:00, 6:30. (ii) At 3:30. (iii) Explain the 6:30 case.", "(i) 120°; 15° (2). (ii) 75° (1). (iii) minute hand 180°, hour hand 195° (2).", "2+1+2"),
 Q("<b>Case study:</b> A carpenter fixes a wooden frame with two parallel bars and a slanting bar making 58° with the upper bar. (i) Angle at lower bar (corresponding). (ii) Alternate angle. (iii) Co-interior angle. (iv) Check parallelism.", "(i) 58° (1). (ii) 58° (1). (iii) 122° (1). (iv) equal corresponding angles (2).", "1+1+1+2"),
 Q("(i) State the converse of the corresponding angles property. (ii) Use it to show two lines are parallel if corresponding angles are 80° each. (iii) Why not if one is 80° and the other 100°?", "(i) If corresponding angles are equal the lines are parallel (2). (ii) 80 = 80 (1). (iii) Not equal, so not parallel (2).", "2+1+2"),
 Q("(i) Three angles at a point on a straight line are x, 2x and 3x. Find x. (ii) Name the largest. (iii) Is it obtuse?", "(i) 30° (2). (ii) 90° (2). (iii) No, right angle (1).", "2+2+1"),
]
D = D[:16]
SETS, POOL = build(A, B, C, D)
