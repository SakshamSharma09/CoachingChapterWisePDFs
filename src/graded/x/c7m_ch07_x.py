"""Class 7 Maths Ch 7 A Tale of Three Intersecting Lines - extras."""
from common import AR4, Q

AR = [
 AR4("A triangle cannot be formed with sides 3 cm, 4 cm and 8 cm.", "The sum of any two sides of a triangle must be greater than the third side.", "a",
     "3 + 4 = 7 < 8, so the rule fails."),
 AR4("A triangle can have at most one right angle.", "A scalene triangle has three unequal sides.", "b",
     "Two right angles would make 180 degrees with nothing left for the third angle. Both true, but R does not explain A."),
 AR4("The exterior angle of a triangle equals the sum of the two interior opposite angles.", "The exterior angle of a triangle always equals the adjacent interior angle.", "c",
     "A is true. The exterior angle and the adjacent interior angle form a linear pair (sum 180 degrees), so R is false."),
 AR4(r"A triangle can have angles $90^\circ$, $60^\circ$ and $40^\circ$.", r"The sum of the three angles of a triangle is $180^\circ$.", "d",
     "90 + 60 + 40 = 190, so A is false. R is true."),
 AR4(r"Two angles of a triangle are $50^\circ$ and $60^\circ$. The third angle is $70^\circ$.", r"The angle sum of a triangle is $180^\circ$.", "a",
     "180 - 110 = 70."),
 AR4("Sides of 5 cm, 7 cm and 10 cm can form a triangle.", "In a triangle the sum of any two sides is greater than the third side.", "a",
     "5 + 7 > 10, 5 + 10 > 7 and 7 + 10 > 5."),
]

CASE = [
 Q(r"<b>Case study.</b> Meena has sticks of various lengths and tries to make triangles. (i) Can she form a triangle with sticks of 4 cm, 5 cm and 9 cm? Give the reason. (ii) Can she form one with 5 cm, 6 cm and 10 cm? (iii) Can she form one with 7 cm, 7 cm and 12 cm? What type of triangle is it? (iv) Two sticks are 6 cm and 9 cm. Between which two lengths must the third stick lie, and how many whole-number lengths are possible?",
   r"(i) No, as $4+5=9$ is not greater than 9 (1). (ii) Yes, as the sum of any two sides exceeds the third (1). (iii) Yes, $7+7=14>12$; it is isosceles (1). (iv) The third side is greater than $9-6=3$ cm and less than $9+6=15$ cm (1); whole numbers 4 to 14, i.e. 11 lengths (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A roof frame is a triangle ABC with $\angle A=50^\circ$ and $\angle B=70^\circ$. Side BC is extended to D. (i) Find $\angle C$. (ii) Find the exterior angle $\angle ACD$. (iii) Verify that the exterior angle equals $\angle A+\angle B$. (iv) Name the triangle by its angles and by its sides, giving reasons.",
   r"(i) $\angle C=180^\circ-50^\circ-70^\circ=60^\circ$ (1). (ii) $\angle ACD=180^\circ-60^\circ=120^\circ$ (1). (iii) $50^\circ+70^\circ=120^\circ$ (1). (iv) All angles are less than $90^\circ$, so it is acute-angled (1); the three angles are different, so the sides are different and it is scalene (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A gable of a house is an isosceles triangle ABC with AB = AC and apex angle $\angle A=40^\circ$. (i) Find each base angle. (ii) Name the triangle by its angles. (iii) Find the exterior angle at B. (iv) The equal sides are 8 m each. Find the perimeter if the base is 5 m. Can the base be 17 m? Give a reason.",
   r"(i) $\dfrac{180^\circ-40^\circ}{2}=70^\circ$ (1). (ii) Acute-angled (1). (iii) $180^\circ-70^\circ=110^\circ$ (1). (iv) Perimeter $=8+8+5=21$ m (1); no, because $8+8=16<17$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Triangle inequality", [r"Sum of any two sides $>$ the third side; difference of any two sides $<$ the third side.",
   r"If two sides are $a$ and $b$, the third side $c$ satisfies $|a-b|<c<a+b$."]),
 ("Angle sum property", [r"Sum of the three angles of a triangle $=180^\circ$.",
   r"A triangle has at most one right angle or one obtuse angle."]),
 ("Exterior angle", [r"Exterior angle $=$ sum of the two interior opposite angles.",
   r"Exterior angle $+$ adjacent interior angle $=180^\circ$ (linear pair); the exterior angle is greater than either interior opposite angle."]),
 ("Types of triangles", [r"By sides: equilateral (3 equal sides, each angle $60^\circ$); isosceles (2 equal sides, angles opposite them equal); scalene (no equal sides).",
   r"By angles: acute (all $<90^\circ$); right (one $90^\circ$); obtuse (one $>90^\circ$).",
   r"Isosceles with apex angle $A$: each base angle $=\dfrac{180^\circ-A}{2}$."]),
 ("Perimeter", [r"Perimeter $=a+b+c$; for isosceles with equal sides $a$ and base $b$: $P=2a+b$."]),
]

MISTAKES = [
 r"Checking only one pair of sides in the triangle inequality; all three conditions must hold (the smallest pair is the critical one).",
 r"Saying a triangle is possible when two sides add up exactly to the third; the sum must be <i>greater</i>.",
 r"Using $90^\circ$ or $360^\circ$ instead of $180^\circ$ for the angle sum of a triangle.",
 r"Equating the exterior angle to the adjacent interior angle instead of the sum of the two interior opposite angles.",
 r"In an isosceles triangle, taking the angles opposite the unequal side as equal.",
]
