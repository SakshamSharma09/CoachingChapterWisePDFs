"""Class 8 Maths Ch 9 The Baudhayana-Pythagoras Theorem - extras."""
from common import AR4, Q

AR = [
 AR4(r"A triangle with sides 6 cm, 8 cm and 10 cm is right-angled.", r"If the square of the longest side equals the sum of the squares of the other two sides, the triangle is right-angled.", "a",
     r"$6^2+8^2=36+64=100=10^2$; R is the converse of the theorem."),
 AR4(r"$(5,12,13)$ is a Pythagorean triplet.", r"$(3,4,5)$ is a Pythagorean triplet.", "b",
     r"$25+144=169$ and $9+16=25$, so both are true; but R does not explain A."),
 AR4(r"In a right-angled triangle the hypotenuse is the longest side.", r"In a right-angled triangle the square of any side equals the sum of the squares of the other two sides.", "c",
     r"The hypotenuse is opposite the largest angle, so A is true; R is false since it holds only for the hypotenuse."),
 AR4(r"The diagonal of a square of side 5 cm is 10 cm.", r"The diagonal of a square of side $a$ is $a\sqrt2$.", "d",
     r"Diagonal $=5\sqrt2\approx7.07$ cm, so A is false; R is true."),
 AR4(r"The diagonal of a rectangle of length 12 cm and breadth 5 cm is 13 cm.", r"The diagonal divides the rectangle into two right-angled triangles whose hypotenuse is the diagonal.", "a",
     r"$\sqrt{12^2+5^2}=\sqrt{169}=13$, obtained by applying the theorem in one of the right triangles."),
 AR4(r"A triangle with sides 4 cm, 5 cm and 6 cm is not right-angled.", r"In every triangle the sum of the squares of the two shorter sides equals the square of the longest side.", "c",
     r"$4^2+5^2=41\ne36=6^2$ so A is true; R is false since it holds only in right-angled triangles."),
]

CASE = [
 Q(r"<b>Case study.</b> A 13 m ladder leans against a vertical wall with its foot 5 m from the wall. "
   r"(i) How high up the wall does the ladder reach? (ii) Which Pythagorean triplet does this give? (iii) If the foot is pulled out to 12 m from the wall, how high does the ladder reach? (iv) By how much does the top of the ladder slip down?",
   r"(i) $\sqrt{13^2-5^2}=\sqrt{144}=12$ m (1). (ii) $(5,12,13)$ (1). (iii) $\sqrt{13^2-12^2}=\sqrt{25}=5$ m (1). (iv) $12-5=7$ m (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Raju must go from corner A to the opposite corner C of a rectangular field 40 m long and 30 m wide, either along the two sides or straight across along the diagonal. "
   r"(i) Find the length of the diagonal. (ii) Find the distance along the two sides. (iii) How much distance does he save by walking across? (iv) Kavya says $(15,20,25)$ is also a Pythagorean triplet because it is half of the field's triplet. Verify her statement.",
   r"(i) $\sqrt{40^2+30^2}=50$ m (1). (ii) $40+30=70$ m (1). (iii) $70-50=20$ m (1). (iv) $15^2+20^2=225+400=625=25^2$, so it is a triplet (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A carpenter checks whether the corners of triangular frames are right angles using side lengths. Frame P has sides 9, 12, 15 cm; Frame Q has sides 7, 24, 25 cm; Frame R has sides 8, 10, 12 cm. "
   r"(i) Is frame P right-angled? (ii) Is frame Q right-angled? (iii) Is frame R right-angled? (iv) A fourth frame is right-angled with perpendicular sides 20 cm and 21 cm; find its hypotenuse and perimeter.",
   r"(i) $9^2+12^2=225=15^2$, yes (1). (ii) $7^2+24^2=625=25^2$, yes (1). (iii) $8^2+10^2=164\ne144=12^2$, no (1). (iv) Hypotenuse $=\sqrt{400+441}=\sqrt{841}=29$ cm (1); perimeter $=20+21+29=70$ cm (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Baudhayana-Pythagoras theorem", [
   r"In a right-angled triangle: (hypotenuse)$^2=$ (base)$^2+$ (perpendicular)$^2$, i.e. $c^2=a^2+b^2$.",
   r"The hypotenuse is the side opposite the right angle and is the longest side."]),
 ("Converse", [
   r"If $c^2=a^2+b^2$ for the sides of a triangle with $c$ the longest, the triangle is right-angled and the right angle is opposite $c$."]),
 ("Pythagorean triplets", [
   r"Common triplets: $(3,4,5)$, $(5,12,13)$, $(8,15,17)$, $(7,24,25)$, $(20,21,29)$; multiples of a triplet are triplets.",
   r"For $m>1$: $(2m,\ m^2-1,\ m^2+1)$ is a Pythagorean triplet."]),
 ("Applications", [
   r"Diagonal of a rectangle $=\sqrt{l^2+b^2}$; diagonal of a square of side $a=a\sqrt2$.",
   r"Rhombus with diagonals $d_1,d_2$: side $=\sqrt{\left(\dfrac{d_1}2\right)^2+\left(\dfrac{d_2}2\right)^2}$.",
   r"Ladder/pole/wall problems: form a right triangle with ground, wall, ladder as the hypotenuse."]),
]

MISTAKES = [
 r"Applying $c^2=a^2+b^2$ with the wrong side as hypotenuse; $c$ is always the side opposite the right angle (the longest).",
 r"Forgetting to take the square root at the end (giving 169 instead of 13).",
 r"Adding the squares when finding a leg: leg $=\sqrt{c^2-a^2}$ (subtract).",
 r"Using the converse with the wrong pairing: always square the <b>longest</b> side on one side of the equation.",
 r"Writing $\sqrt{a^2+b^2}=a+b$; for example $\sqrt{9+16}=5$, not $3+4=7$.",
 r"Assuming three consecutive numbers such as 2, 3, 4 form a right triangle; always verify $a^2+b^2=c^2$ (here $4+9\ne16$).",
]
