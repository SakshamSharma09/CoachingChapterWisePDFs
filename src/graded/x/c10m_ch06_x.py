"""Class 10 Maths Ch 6 Triangles - extras (similarity, BPT, area ratio, Pythagoras theorem and converse)."""
from common import AR4, Q

AR = [
 AR4(r"In $\triangle ABC$, $DE\parallel BC$ with D on AB and E on AC. If $AD=2$ cm, $DB=3$ cm and $AE=4$ cm, then $EC=6$ cm.", r"A line parallel to one side of a triangle, meeting the other two sides at distinct points, divides those sides in the same ratio.", "a",
     r"$\tfrac{AD}{DB}=\tfrac{AE}{EC}\Rightarrow\tfrac23=\tfrac4{EC}\Rightarrow EC=6$; R is the Basic Proportionality Theorem."),
 AR4(r"In a triangle ABC right-angled at B, with $AB=6$ cm and $BC=8$ cm, the hypotenuse $AC=10$ cm.", r"The Pythagoras theorem holds only for isosceles right-angled triangles.", "c",
     r"$AC^2=36+64=100$, so $AC=10$: A true; the theorem holds for every right-angled triangle, so R is false."),
 AR4(r"A triangle with sides 5 cm, 6 cm and 7 cm is right-angled.", r"If in a triangle the square of one side equals the sum of the squares of the other two sides, the angle opposite the first side is a right angle.", "d",
     r"$5^2+6^2=61\neq49=7^2$, so it is not right-angled: A false; R is the (true) converse of the Pythagoras theorem."),
 AR4(r"The triangles with sides 3, 4, 5 and 6, 8, 10 are similar.", r"The hypotenuse is the longest side of a right-angled triangle.", "b",
     r"The sides are in the ratio $1:2$ (SSS similarity), so A is true; R is true but does not explain the similarity."),
 AR4(r"Any two equilateral triangles are similar.", r"If two angles of one triangle are equal to two angles of another triangle, the triangles are similar.", "a",
     r"All angles of an equilateral triangle are $60^\circ$, so two angles match; this is the AA criterion in R."),
 AR4(r"If two similar triangles have areas $16\ \text{cm}^2$ and $81\ \text{cm}^2$, their corresponding sides are in the ratio $4:9$.", r"The ratio of the areas of two similar triangles equals the ratio of their corresponding sides.", "c",
     r"The ratio of areas equals the <i>square</i> of the ratio of sides, so $\sqrt{16/81}=4/9$: A is true; R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> At the same time of the day, a girl of height 1.5 m casts a shadow 2 m long, while a tower casts a shadow 24 m long on level ground. "
   r"(i) Name the similarity criterion that makes the two triangles formed (object, shadow, sun's ray) similar. (ii) Find the height of the tower. (iii) At that time, a pole 6 m high will cast a shadow of what length? (iv) Find the distance from the top of the tower to the tip of its shadow.",
   r"(i) AA (each has a right angle and the same sun-angle) (1). (ii) $\tfrac{h}{24}=\tfrac{1.5}{2}\Rightarrow h=18$ m (1). (iii) $\tfrac{6}{s}=\tfrac{1.5}{2}\Rightarrow s=8$ m (1). (iv) $\sqrt{18^2+24^2}=\sqrt{900}=30$ m by the Pythagoras theorem (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A triangular plot ABC has a straight fence DE with D on AB and E on AC such that $DE\parallel BC$. It is given that $AD=6$ m, $DB=4$ m and $AE=9$ m. "
   r"(i) State the theorem used to relate the segments. (ii) Find EC. (iii) Find the lengths AB and AC. (iv) If $BC=20$ m, find DE, and the ratio of the areas of $\triangle ADE$ and $\triangle ABC$.",
   r"(i) Basic Proportionality (Thales) theorem (1). (ii) $\tfrac{6}{4}=\tfrac9{EC}\Rightarrow EC=6$ m (1). (iii) $AB=10$ m, $AC=15$ m (1). (iv) $\triangle ADE\sim\triangle ABC$: $\tfrac{DE}{20}=\tfrac{6}{10}\Rightarrow DE=12$ m (1); area ratio $=\left(\tfrac{6}{10}\right)^2=\tfrac{9}{25}$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A 17 m long ladder rests against a vertical wall with its top at a window 15 m above the ground. "
   r"(i) Which side of the right triangle formed is the hypotenuse? (ii) Find the distance of the foot of the ladder from the wall. (iii) Find the perimeter of the triangle formed by the ladder, the wall and the ground. (iv) The top of the ladder slides down the wall to a height of 8 m. How far is the foot of the ladder from the wall now, and how far did the foot move?",
   r"(i) The ladder (1). (ii) $\sqrt{17^2-15^2}=\sqrt{64}=8$ m (1). (iii) $8+15+17=40$ m (1). (iv) New distance $=\sqrt{17^2-8^2}=\sqrt{225}=15$ m (1); the foot moved $15-8=7$ m (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Similar triangles", [r"Similar: corresponding angles equal and corresponding sides in the same ratio.",
   r"<b>AA</b> (two angles equal), <b>SSS</b> (three pairs of sides proportional), <b>SAS</b> (one equal angle between two proportional sides).",
   r"All circles are similar, all squares are similar, all equilateral triangles are similar."]),
 ("Basic Proportionality Theorem (Thales)", [r"If $DE\parallel BC$ in $\triangle ABC$ (D on AB, E on AC): $\dfrac{AD}{DB}=\dfrac{AE}{EC}$.",
   r"Converse: if $\dfrac{AD}{DB}=\dfrac{AE}{EC}$ then $DE\parallel BC$.",
   r"Also $\dfrac{AD}{AB}=\dfrac{AE}{AC}=\dfrac{DE}{BC}$ when $DE\parallel BC$."]),
 ("Areas of similar triangles", [r"$\dfrac{\text{ar}(\triangle ABC)}{\text{ar}(\triangle PQR)}=\left(\dfrac{AB}{PQ}\right)^2=\left(\dfrac{BC}{QR}\right)^2=\left(\dfrac{CA}{RP}\right)^2$.",
   r"Ratio of areas = square of the ratio of corresponding sides."]),
 ("Pythagoras theorem and converse", [r"In a right triangle: $(\text{hypotenuse})^2=(\text{base})^2+(\text{perpendicular})^2$.",
   r"Converse: if $c^2=a^2+b^2$ then the angle opposite c is $90^\circ$.",
   r"Common triples: $(3,4,5),\ (5,12,13),\ (8,15,17),\ (7,24,25)$."]),
 ("Applications", [r"Shadow problems: $\dfrac{\text{height}}{\text{shadow}}$ is the same for all objects at the same time.",
   r"Altitude to hypotenuse creates triangles similar to the whole triangle."]),
]

MISTAKES = [
 r"Writing the BPT as $\dfrac{AD}{AB}=\dfrac{AE}{EC}$; mix of a part-to-whole and a part-to-part ratio.",
 r"Equating the <i>areas</i> ratio to the <i>sides</i> ratio instead of its square.",
 r"Matching vertices in the wrong order while writing similarity ($\triangle ABC\sim\triangle PQR$ must have A to P, B to Q, C to R).",
 r"Applying the Pythagoras theorem with the wrong side as hypotenuse (hypotenuse is opposite the right angle and is the longest side).",
 r"Using the converse of Pythagoras without squaring all three sides, or comparing with the wrong side.",
 r"Saying two triangles are similar because they have equal ratio of only two pairs of sides (SAS needs the included angle).",
]
