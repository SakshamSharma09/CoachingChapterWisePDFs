"""Class 9 Maths Ch 12 - Quadrilaterals: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch12"

def _old(n):
    d = "c9_maths1" if n < 9 else "c9_maths2"
    p = Path(__file__).resolve().parents[1] / "rn_work" / d / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def _lt(x):
    if isinstance(x, str): return x.replace(" < ", " &lt; ").replace(" > ", " &gt; ")
    if isinstance(x, (list, tuple)): return type(x)(_lt(i) for i in x)
    return x

assert 360-80-95-110 == 75 and 360-90-75-100 == 95 and 2*(8+5) == 26 and 36*3 == 108 and 36*2 == 72 and 12/2 == 6 and 16/2 == 8
assert 2*35 == 70 and 15*2 == 30
assert 15*(2+3+4+6)//15 == 15 and 360/15 == 24 and [24*k for k in (2, 3, 4, 6)] == [48, 72, 96, 144]
assert 2*30+10 == 3*30-20 == 70 and 180-70 == 110 and 3*60 == 180 and 180/3 == 60 and 2*60 == 120
assert (16+20+24)/2 == 30 and 2*40 == 80 and 80*120 == 9600 and 24*2/3 == 16 and 24/3 == 8 and 18/3 == 6 and 18*2/3 == 12
assert 14+10 == 24 and 14/2 == 7 and 10/2 == 5 and sqrt(8**2+6**2) == 10 and 4*10*75 == 3000 and (180-80)/2 == 50 and 90-50 == 40
assert 30/2 == 15 and 360/108 != int(360/108) and 360/135 != int(360/135) and 24/2 == 12 and 32/2 == 16 and sqrt(12**2+16**2) == 20 and 4*20 == 80
assert 180-65 == 115 and sqrt(5**2+12**2) == 13 and 2*(5+12) == 34 and 36*2/3 == 24 and 36/3 == 12 and sqrt(30**2+40**2) == 50
assert 2*(30+40) == 140 and 140*50 == 7000 and (180-80)/2 == 50 and 360-60-50-200 == 50
assert [33*2/3, 27*2/3, 45*2/3] == [22, 18, 30] and [33/3, 27/3, 45/3] == [11, 9, 15] and 22+18+30 == 70 == 2*(33+27+45)/3
assert [(n-2)*180/n for n in (3, 4, 5, 6, 8)] == [60, 90, 108, 120, 135] and 135+135+90 == 360 and 18*2/3+0 == 12
assert 18*2//3 == 12 and 24*2//3 == 16 and 30*2//3 == 20 and 6+8+10 == 24 and 12+16+20 == 48

WS = [
# ---------------- EASY ----------------
W(r"The sum of the interior angles of any quadrilateral is:", 1, r"(c) $360^\circ$. A diagonal splits the quadrilateral into two triangles, each with angle sum $180^\circ$. (1)", "E", opts=[r"$180^\circ$", r"$270^\circ$", r"$360^\circ$", r"$540^\circ$"]),
W(r"In a parallelogram ABCD, $\angle A=70^\circ$. Then $\angle B$ equals:", 1, r"(b) $110^\circ$. Adjacent angles of a parallelogram add up to $180^\circ$: $180^\circ-70^\circ=110^\circ$. (1)", "E", opts=[r"$70^\circ$", r"$110^\circ$", r"$290^\circ$", r"$20^\circ$"]),
W(r"Which quadrilateral always has diagonals that bisect each other at right angles?", 1, r"(c) a rhombus. The diagonals of a rhombus bisect each other at $90^\circ$. In a rectangle they bisect each other but are not perpendicular (unless it is a square); a general parallelogram's diagonals bisect each other but are not perpendicular; a trapezium's diagonals need not bisect each other. (1)", "E", opts=["a parallelogram", "a rectangle", "a rhombus", "a trapezium"]),
W(r"In $\triangle ABC$, P and Q are the midpoints of AB and AC and $BC=14$ cm. Then $PQ$ is:", 1, r"(a) 7 cm. By the Midpoint Theorem $PQ=\frac12BC=7$ cm. (1)", "E", opts=["7 cm", "14 cm", "28 cm", "3.5 cm"]),
W(r"A median of a triangle is 30 cm long. The centroid is at what distance from the vertex along the median?", 1, r"(d) 20 cm. The centroid divides the median $2:1$ from the vertex, so $\frac23\times30=20$ cm. (1)", "E", opts=["10 cm", "15 cm", "25 cm", "20 cm"]),
W(r"Which condition is enough to say that a quadrilateral is a parallelogram?", 1, r"(b) One pair of opposite sides equal and parallel. One pair of equal sides alone fails (an isosceles trapezium); equal diagonals alone fails (also an isosceles trapezium); one right angle alone fails. (1)", "E",
  opts=["One pair of opposite sides equal", "One pair of opposite sides equal and parallel", "Diagonals are equal", "One angle is $90^\\circ$"]),
W(r"Three angles of a quadrilateral are $80^\circ$, $95^\circ$ and $110^\circ$. Find the fourth angle.", 2, r"Sum is $360^\circ$ (1). Fourth angle $=360^\circ-(80^\circ+95^\circ+110^\circ)=75^\circ$ (1).", "E"),
W(r"A plot ABCD has $\angle A=90^\circ$, $\angle B=75^\circ$ and $\angle C=100^\circ$. Find $\angle D$.", 2, r"Angle sum $=360^\circ$ (1). $\angle D=360^\circ-265^\circ=95^\circ$ (1).", "E", wp=True),
W(r"In parallelogram ABCD, $AB=8$ cm and $BC=5$ cm. Find CD, AD and the perimeter.", 2, r"Opposite sides are equal: $CD=8$ cm and $AD=5$ cm (1). Perimeter $=2(8+5)=26$ cm (1).", "E"),
W(r"In a parallelogram-shaped signboard ABCD, $\angle A=3x$ and $\angle B=2x$ (in degrees). Find $x$ and all four angles.", 2, r"Adjacent angles: $3x+2x=180^\circ$, $x=36^\circ$ (1). $\angle A=\angle C=108^\circ$ and $\angle B=\angle D=72^\circ$ (1).", "E", wp=True),
W(r"The diagonals of parallelogram ABCD meet at O. If $AC=12$ cm and $BD=16$ cm, find OA and OB.", 2, r"The diagonals of a parallelogram bisect each other (1). $OA=6$ cm and $OB=8$ cm (1).", "E"),
W(r"P and Q are the midpoints of AB and AC of a triangular plot ABC. A path PQ is 35 m long. How long is the side BC? What can you say about the directions of PQ and BC?", 2, r"$PQ=\frac12BC$, so $BC=70$ m (1). PQ is parallel to BC (1).", "E", wp=True),
W(r"True or false (give a reason): (i) Every rhombus is a parallelogram. (ii) Every parallelogram is a rhombus.", 2, r"(i) True: opposite sides of a rhombus are parallel (equal sides, and both pairs of opposite sides parallel) (1). (ii) False: a parallelogram with unequal adjacent sides (for example a rectangle $6\times4$) is not a rhombus (1).", "E"),
W(r"The diagonal AC of rectangle ABCD is 10 cm. Find BD and OA, where O is the point where the diagonals meet.", 2, r"The diagonals of a rectangle are equal: $BD=10$ cm (1). They bisect each other: $OA=5$ cm (1).", "E"),
W(r"A carpenter makes a quadrilateral frame ABCD with $AB=CD=60$ cm and $BC=DA=40$ cm. Name the shape, the test you used and the length of the wood needed for the frame.", 2, r"Both pairs of opposite sides are equal, so it is a parallelogram (1). Wood $=2(60+40)=200$ cm (1).", "E", wp=True),
W(r"Which of the parallelogram, rectangle, rhombus and square always have equal diagonals?", 2, r"The rectangle and the square (1). The diagonals of a general parallelogram and of a rhombus are not equal unless the rhombus is a square (1).", "E"),
W(r"A triangular metal plate has a median AD of 18 cm. The plate balances at the centroid G. Find AG and GD.", 2, r"The centroid divides the median in the ratio $2:1$ (1). $AG=\frac23\times18=12$ cm and $GD=6$ cm (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"The angles of a quadrilateral field are in the ratio $2:3:4:6$. Find the four angles.", 3, r"Sum of ratio parts $=15$, and $360^\circ\div15=24^\circ$ (1). Angles: $48^\circ, 72^\circ, 96^\circ, 144^\circ$ (2).", "M", wp=True),
W(r"In parallelogram ABCD, $\angle A=(2x+10)^\circ$ and $\angle C=(3x-20)^\circ$. Find $x$ and all the angles of the parallelogram.", 3, r"Opposite angles are equal: $2x+10=3x-20$, so $x=30$ (1). $\angle A=\angle C=70^\circ$ (1). $\angle B=\angle D=180^\circ-70^\circ=110^\circ$ (1).", "M"),
W(r"In a parallelogram, one angle is twice its adjacent angle. Find all four angles.", 2, r"Adjacent angles add to $180^\circ$: $2y+y=180^\circ$, $y=60^\circ$ (1). Angles: $120^\circ, 60^\circ, 120^\circ, 60^\circ$ (1).", "M"),
W(r"In $\triangle ABC$, P, Q and R are the midpoints of AB, BC and CA. If $AB=16$ cm, $BC=20$ cm and $CA=24$ cm, find the perimeter of $\triangle PQR$.", 3, r"Each side of $\triangle PQR$ is half of a side of $\triangle ABC$: $PQ=12$, $QR=8$, $RP=10$ (2). Perimeter $=30$ cm, half of 60 cm (1).", "M"),
W(r"D and E are the midpoints of AB and AC in a triangular park ABC, and $DE=40$ m. A fence has to be put along BC at ₹ 120 per metre. Find the cost.", 3, r"$BC=2\times DE=80$ m (Midpoint Theorem) (2). Cost $=80\times120=$ ₹ 9,600 (1).", "M", wp=True),
W(r"Medians AD and BE of $\triangle ABC$ meet at G. If $AD=24$ cm and $BE=18$ cm, find AG, GD and GE.", 3, r"$AG=\frac23AD=16$ cm (1). $GD=\frac13AD=8$ cm (1). $GE=\frac13BE=6$ cm (1).", "M"),
W(r"The diagonals of a quadrilateral are 14 cm and 10 cm. P, Q, R and S are the midpoints of its sides in order. Find the sides and perimeter of PQRS and name the figure.", 3, r"PQRS is a parallelogram (Varignon) (1). Its sides are $\frac{14}2=7$ cm and $\frac{10}2=5$ cm (1). Perimeter $=2(7+5)=24$ cm $=14+10$ (1).", "M"),
W(r"In quadrilateral PQRS the diagonals meet at O with $OP=OR=4$ cm and $OQ=OS=5$ cm. Name the quadrilateral and the test you used. Is it a rectangle?", 3, r"The diagonals bisect each other, so PQRS is a parallelogram (Theorem 4) (1.5). $PR=8$ cm and $QS=10$ cm are not equal, so it is not a rectangle (1.5).", "M"),
W(r"Ravi says: 'A quadrilateral with one pair of opposite sides equal is a parallelogram.' Find a counterexample and state the correct test.", 2, r"An isosceles trapezium has one pair of equal (non-parallel) opposite sides but is not a parallelogram (1). Correct test: one pair of opposite sides must be both **equal and parallel** (1).", "M"),
W(r"The diagonals of a rhombus-shaped garden are 16 m and 12 m. Find the length of its side, the cost of fencing at ₹ 75 per metre and say how the diagonals meet.", 3, r"The diagonals bisect each other at right angles, so half-diagonals are 8 m and 6 m (1). Side $=\sqrt{8^2+6^2}=10$ m (1). Perimeter $=40$ m; cost $=40\times75=$ ₹ 3,000 (1).", "M", wp=True),
W(r"In rectangle ABCD the diagonals meet at O and $\angle AOB=80^\circ$. Find $\angle OAB$ and $\angle OAD$.", 3, r"$OA=OB$ (diagonals of a rectangle are equal and bisect each other) (1). $\angle OAB=\frac{180^\circ-80^\circ}2=50^\circ$ (1). $\angle OAD=90^\circ-50^\circ=40^\circ$ (1).", "M"),
W(r"P, Q, R and S are the midpoints of the sides AB, BC, CD and DA of a quadrilateral field ABCD with diagonal $AC=30$ m. Find PQ and SR and explain why PQ is parallel to SR.", 3, r"In $\triangle ABC$, $PQ\parallel AC$ and $PQ=15$ m (1). In $\triangle ADC$, $SR\parallel AC$ and $SR=15$ m (1). So $PQ\parallel SR$ and $PQ=SR$ (both parallel and equal to half of AC) (1).", "M", wp=True),
W(r"Prove that the opposite sides of a parallelogram ABCD are equal. (Use the diagonal AC.)", 3, r"In $\triangle ABC$ and $\triangle CDA$: $\angle BAC=\angle DCA$ (alternate angles, $AB\parallel DC$) (1), $\angle BCA=\angle DAC$ (alternate angles, $BC\parallel AD$) (1), $AC$ common. So the triangles are congruent by ASA, and $AB=CD$, $BC=DA$ by CPCT (1).", "M"),
W(r"Can copies of a regular pentagon (interior angle $108^\circ$) tile the plane alone? Can copies of a regular octagon (interior angle $135^\circ$)? Explain with the angles at a point.", 3, r"At a point the angles must add up to $360^\circ$ with no gap (1). $360\div108=3.33$ is not a whole number, so pentagons cannot tile alone (1). $360\div135\approx2.67$, so octagons alone cannot tile either (1).", "M"),
W(r"A rhombus ABCD has $\angle A=60^\circ$ and side 8 cm. Find the other angles and the length of diagonal BD.", 3, r"$\angle C=60^\circ$ and $\angle B=\angle D=120^\circ$ (1). In $\triangle ABD$, $AB=AD=8$ and $\angle A=60^\circ$, so it is equilateral (1). $BD=8$ cm (1).", "M"),
W(r"The diagonals of a quadrilateral are perpendicular and have lengths 10 cm and 24 cm. The midpoints of its sides are joined in order. Name the new figure and find its sides and the length of its diagonal.", 3, r"Diagonals perpendicular, so the figure is a rectangle (1). Sides $\frac{10}2=5$ cm and $\frac{24}2=12$ cm (1). Diagonal $=\sqrt{25+144}=13$ cm (1).", "M"),
W(r"A triangular plate hangs balanced at its centroid, which is 12 cm from the midpoint of one side along a median. Find the length of that median and the distance of the centroid from the vertex.", 3, r"The centroid is $\frac13$ of the median from the side's midpoint, so median $=36$ cm (2). Distance from the vertex $=\frac23\times36=24$ cm (1).", "M", wp=True),
W(r"In quadrilateral ABCD, $AB=CD$ and $AB\parallel CD$ and $\angle A=65^\circ$. Name the quadrilateral and find $\angle B$, $\angle C$ and $\angle D$.", 3, r"One pair of opposite sides equal and parallel, so ABCD is a parallelogram (1). $\angle B=180^\circ-65^\circ=115^\circ$ (1). $\angle C=65^\circ$, $\angle D=115^\circ$ (1).", "M"),
W(r"A rectangular sheet is 24 cm by 32 cm. The midpoints of its sides are joined in order to make a paper decoration. Name the figure, find its side and its perimeter.", 3, r"The diagonals of the rectangle are equal, so the figure is a rhombus (1). Diagonal of the sheet $=\sqrt{24^2+32^2}=40$ cm, so each side $=20$ cm (1). Perimeter $=80$ cm (1).", "M", wp=True),
W(r"Prove that the diagonals of a rectangle are equal.", 3, r"Let ABCD be a rectangle. In $\triangle ABC$ and $\triangle DCB$: $AB=DC$ (opposite sides of a parallelogram) (1), $\angle ABC=\angle DCB=90^\circ$ (1), $BC$ common. So $\triangle ABC\cong\triangle DCB$ (SAS) and $AC=DB$ (1).", "M"),
# ---------------- HARD ----------------
W(r"Prove that the midpoints P, Q, R, S of the sides AB, BC, CD, DA of any quadrilateral ABCD form a parallelogram.", 4, r"Join AC. In $\triangle ABC$, P and Q are midpoints so $PQ\parallel AC$ and $PQ=\frac12AC$ (1.5). In $\triangle ADC$, S and R are midpoints so $SR\parallel AC$ and $SR=\frac12AC$ (1.5). So $PQ\parallel SR$ and $PQ=SR$; one pair of opposite sides equal and parallel, so PQRS is a parallelogram (1).", "H"),
W(r"In $\triangle ABC$, P and Q are the midpoints of AB and AC. D is any point on BC and AD meets PQ at X. Prove that X is the midpoint of AD.", 4, r"$PQ\parallel BC$ (Midpoint Theorem), so $PX\parallel BD$ (1). In $\triangle ABD$, P is the midpoint of AB and $PX\parallel BD$ (1). By the converse of the Midpoint Theorem, the line through P parallel to BD bisects AD, so X is the midpoint of AD (2).", "H"),
W(r"Medians AD, BE and CF of $\triangle ABC$ have lengths 18 cm, 24 cm and 30 cm and meet at G. Find AG, BG, CG, GD, GE and GF, and the sum $AG+BG+CG$.", 4, r"The centroid divides each median $2:1$ from the vertex (1). $AG=12$, $BG=16$, $CG=20$ (1.5). $GD=6$, $GE=8$, $GF=10$ (1). $AG+BG+CG=48=\frac23(18+24+30)$ (0.5).", "H"),
W(r"Prove that the bisectors of two adjacent angles of a parallelogram meet at a right angle.", 4, r"Let ABCD be a parallelogram with bisectors of $\angle A$ and $\angle B$ meeting at P. Since $AD\parallel BC$, $\angle A+\angle B=180^\circ$ (1). In $\triangle APB$, $\angle PAB+\angle PBA=\frac12(\angle A+\angle B)=90^\circ$ (2). So $\angle APB=180^\circ-90^\circ=90^\circ$ (1).", "H"),
W(r"**Case study (tiling a floor).** The interior angle of a regular $n$-sided polygon is $\frac{(n-2)\times180^\circ}{n}$. (i) Find it for $n=3,4,5,6,8$. (ii) Which of these regular polygons can tile a floor alone, and why? (iii) Show that two regular octagons and one square can meet at a point without a gap.", 5, r"(i) $60^\circ, 90^\circ, 108^\circ, 120^\circ, 135^\circ$ (1.5). (ii) Triangle ($6\times60^\circ$), square ($4\times90^\circ$) and hexagon ($3\times120^\circ$) fit exactly 360° at a point, so they tile; 108° and 135° do not divide 360° (2). (iii) $135^\circ+135^\circ+90^\circ=360^\circ$, so the angles fill the point (1.5).", "H", wp=True),
W(r"ABCD is a parallelogram and E, F are the midpoints of AB and CD. Prove that AECF is a parallelogram.", 4, r"$AB=CD$ (opposite sides), so $AE=\frac12AB=\frac12CD=CF$ (1.5). $AB\parallel CD$ means $AE\parallel CF$ (1.5). One pair of opposite sides is equal and parallel, so AECF is a parallelogram (1).", "H"),
W(r"In rhombus ABCD, $\angle ABC=80^\circ$. Find $\angle BAC$, $\angle ABD$ and $\angle AOB$, where O is the intersection of the diagonals.", 3, r"$AB=BC$, so $\angle BAC=\angle BCA=\frac{180^\circ-80^\circ}2=50^\circ$ (1). The diagonal BD bisects $\angle B$: $\angle ABD=40^\circ$ (1). The diagonals of a rhombus are perpendicular, so $\angle AOB=90^\circ$ (1).", "H"),
W(r"Prove that if the diagonals of a parallelogram are equal, then it is a rectangle.", 4, r"In parallelogram ABCD, $AC=BD$. In $\triangle ABC$ and $\triangle DCB$: $AB=DC$ (1), $BC$ common (0.5), $AC=DB$ (given) (0.5). So the triangles are congruent (SSS) and $\angle ABC=\angle DCB$ (1). As $AB\parallel DC$, $\angle ABC+\angle DCB=180^\circ$, so each is $90^\circ$ (1). A parallelogram with one right angle is a rectangle.", "H"),
W(r"A farmer's field ABCD has diagonals $AC=60$ m and $BD=80$ m that cut each other at right angles. A pond is made by joining the midpoints of the sides in order. Name its shape, find its sides and the cost of fencing it at ₹ 50 per metre.", 4, r"The midpoint figure is a parallelogram; since the diagonals are perpendicular it is a rectangle (1). Sides $=30$ m and $40$ m (1). Perimeter $=2(30+40)=140$ m (1). Cost $=140\times50=$ ₹ 7,000 (1).", "H", wp=True),
W(r"In $\triangle ABC$, D, E and F are the midpoints of BC, CA and AB. (i) Prove that AFDE is a parallelogram. (ii) What extra condition on $\triangle ABC$ makes AFDE a rhombus? (iii) What extra condition makes it a rectangle?", 5, r"(i) By the Midpoint Theorem $DE\parallel AB$ (so $DE\parallel AF$) and $DF\parallel AC$ (so $DF\parallel AE$); both pairs of opposite sides are parallel, so AFDE is a parallelogram (2). (ii) $AF=\frac12AB$ and $AE=\frac12AC$; adjacent sides are equal if $AB=AC$, so it is a rhombus when $\triangle ABC$ is isosceles with $AB=AC$ (1.5). (iii) It has a right angle at A if $\angle A=90^\circ$, giving a rectangle (1.5).", "H"),
W(r"A non-convex quadrilateral ABCD has $\angle A=60^\circ$, $\angle B=50^\circ$ and the interior angle at D is the reflex angle $200^\circ$. Find $\angle C$. Does the angle sum $360^\circ$ still hold?", 3, r"The angle sum of a quadrilateral is $360^\circ$ even when it is not convex (1). $\angle C=360^\circ-(60^\circ+50^\circ+200^\circ)=50^\circ$ (2).", "H"),
W(r"The three medians of a triangular wooden plate are 33 cm, 27 cm and 45 cm. Find the distances of the balancing point G from the three vertices and from the three midpoints, and show that the sum of the distances from the vertices is $\frac23$ of the sum of the medians.", 4, r"From the vertices: $\frac23\times33=22$, $\frac23\times27=18$, $\frac23\times45=30$ cm (1.5). From the midpoints: $11$, $9$, $15$ cm (1). Sum from the vertices $=22+18+30=70$ cm and $\frac23(33+27+45)=\frac23\times105=70$ ✓ (1.5).", "H", wp=True),
W(r"Explain why copies of any triangle tile the plane, using the angles at a point. (Hint: two copies make a parallelogram.)", 4, r"Two copies of the triangle, one turned $180^\circ$ about the midpoint of a side, form a parallelogram (1.5). Parallelograms tile the plane in rows (1). At each vertex of the tiling the angles are $A, B, C$ from one triangle and $A, B, C$ from the rotated one: $2(A+B+C)=2\times180^\circ=360^\circ$ (1.5), so there is no gap or overlap.", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(12)
_pre = _lt(_o["blocks"][:-2])
_extra = [
 ("h2", "Special Quadrilaterals at a Glance"),
 ("table", ["Property", "Parallelogram", "Rectangle", "Rhombus", "Square"], [
  ["Opposite sides parallel", "Yes", "Yes", "Yes", "Yes"],
  ["Opposite sides equal", "Yes", "Yes", "Yes (all four equal)", "Yes (all four equal)"],
  ["All angles 90°", "No", "Yes", "No", "Yes"],
  ["Opposite angles equal", "Yes", "Yes", "Yes", "Yes"],
  ["Diagonals bisect each other", "Yes", "Yes", "Yes", "Yes"],
  ["Diagonals equal", "No", "Yes", "No", "Yes"],
  ["Diagonals perpendicular", "No", "No", "Yes", "Yes"],
  ["Diagonals bisect the angles", "No", "No", "Yes", "Yes"]]),
 ("note", "REMEMBER", "A **square** is both a rectangle and a rhombus. Each special quadrilateral is a parallelogram, but a parallelogram is a rectangle only if it has a right angle (or equal diagonals), and a rhombus only if its adjacent sides are equal (or its diagonals are perpendicular)."),
 ("h2", "Proofs to Know"),
 ("h3", "Proof of Theorem 1(a): opposite sides of a parallelogram are equal"),
 ("steps", [("Given", "ABCD is a parallelogram: AB ∥ DC and AD ∥ BC. Draw the diagonal AC."), ("Congruent triangles", "In △ABC and △CDA: ∠BAC = ∠DCA (alternate angles, AB ∥ DC), ∠BCA = ∠DAC (alternate angles, BC ∥ AD), AC is common."), ("Conclusion", "△ABC ≅ △CDA (ASA), so AB = CD and BC = DA (CPCT). The same congruence gives ∠B = ∠D.")]),
 ("h3", "Proof: diagonals of a rectangle are equal"),
 ("steps", [("Triangles", "In rectangle ABCD, take △ABC and △DCB."), ("Match", "AB = DC (opposite sides), BC is common, ∠ABC = ∠DCB = 90°."), ("Conclusion", "△ABC ≅ △DCB (SAS), so AC = DB.")]),
 ("h3", "Proof: bisectors of adjacent angles of a parallelogram meet at 90°"),
 ("steps", [("Adjacent angles are supplementary", "∠A + ∠B = 180° since AD ∥ BC."), ("In the triangle APB formed by the bisectors", "∠PAB + ∠PBA = ½(∠A + ∠B) = 90°."), ("Third angle", "∠APB = 180° − 90° = 90°.")]),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Angles of a quadrilateral in a ratio"),
 ("steps", [("Angles in the ratio 2 : 3 : 4 : 6", "Total parts = 15."), ("One part", "360° ÷ 15 = 24°."), ("The angles", "48°, 72°, 96°, 144°.")]),
 ("h3", "Example 2 — Angles of a parallelogram with algebra"),
 ("steps", [("∠A = (2x + 10)° and ∠C = (3x − 20)°", "Opposite angles are equal: 2x + 10 = 3x − 20, so x = 30."), ("Find ∠A and ∠B", "∠A = ∠C = 70°; ∠B = 180° − 70° = 110°."), ("All angles", "70°, 110°, 70°, 110°.")]),
 ("h3", "Example 3 — Midpoint Theorem in a word problem"),
 ("steps", [("D and E are midpoints of AB and AC; DE = 40 m", "DE = ½ BC and DE ∥ BC."), ("Find BC", "BC = 80 m."), ("Fencing cost at ₹120 per metre", "80 × 120 = ₹9,600.")]),
 ("h3", "Example 4 — Centroid"),
 ("steps", [("Medians AD = 24 cm and BE = 18 cm meet at G", "G divides each median 2 : 1 from the vertex."), ("AG and GD", "AG = ⅔ × 24 = 16 cm; GD = 8 cm."), ("GE", "GE = ⅓ × 18 = 6 cm.")]),
 ("h3", "Example 5 — Varignon parallelogram"),
 ("steps", [("Quadrilateral with perpendicular diagonals 60 m and 80 m", "Midpoint figure PQRS has sides 30 m and 40 m (half the diagonals)."), ("Shape", "Sides are parallel to perpendicular diagonals, so PQRS is a rectangle."), ("Perimeter and cost", "2(30 + 40) = 140 m; at ₹50 per metre, ₹7,000. Its diagonal is √(30² + 40²) = 50 m.")]),
 ("h3", "Example 6 — Proving a parallelogram"),
 ("steps", [("ABCD is a parallelogram; E, F are midpoints of AB, CD", "AE = ½ AB and CF = ½ CD, and AB = CD, so AE = CF."), ("Parallel", "AE lies along AB and CF along CD, and AB ∥ CD, so AE ∥ CF."), ("Test", "One pair of opposite sides equal and parallel, so AECF is a parallelogram.")]),
 ("h3", "Example 7 — Tiling with regular polygons"),
 ("steps", [("Interior angle of a regular n-gon", "(n − 2) × 180° ÷ n gives 60°, 90°, 108°, 120°, 135° for n = 3, 4, 5, 6, 8."), ("Fit at a point", "Angles must add to exactly 360°: six triangles, four squares or three hexagons work; 108° and 135° do not divide 360°."), ("Mixed tiles", "135° + 135° + 90° = 360°: two octagons and one square fit at a point.")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Words", "Geometry", "Example"], [
  ["‘plot with four corners’", "angle sum 360°", "∠A = 90°, ∠B = 75°, ∠C = 100°: ∠D = 95°"],
  ["‘path joining midpoints of two sides’", "Midpoint Theorem: parallel to the third side and half as long", "PQ = 35 m means BC = 70 m"],
  ["‘balances at its centre’", "centroid, 2 : 1 on each median", "median 18 cm: 12 cm and 6 cm"],
  ["‘pond made by joining midpoints of the sides’", "Varignon parallelogram with sides ½ AC and ½ BD", "diagonals 60 m, 80 m perpendicular: rectangle 30 m × 40 m"],
  ["‘frame with opposite sides equal’", "parallelogram test", "60 cm, 40 cm: perimeter 200 cm"],
  ["‘rhombus-shaped garden, diagonals given’", "half-diagonals and Pythagoras", "16 m, 12 m: side 10 m"],
  ["‘tiles of one shape cover the floor’", "angles at a point add to 360°", "regular pentagon cannot tile"]]),
 ("h2", "Common Mistakes"),
 ("table", ["Wrong idea", "Why it is wrong", "Correct"], [
  ["One pair of equal opposite sides makes a parallelogram", "an isosceles trapezium has this", "the pair must be equal **and** parallel"],
  ["Diagonals of a rectangle are perpendicular", "that is true only for a square", "they are equal and bisect each other"],
  ["Centroid is the midpoint of the median", "it divides 2 : 1", "AG = ⅔ AD"],
  ["PQ = BC in the Midpoint Theorem", "PQ is half of BC", "PQ = ½ BC and PQ ∥ BC"],
  ["Angle sum of a non-convex quadrilateral is more than 360°", "it is always 360°", "use the reflex angle as the interior angle"],
  ["Regular pentagons tile because they look regular", "108° does not divide 360°", "angles at a point must total 360°"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Special quadrilaterals** share the parallelogram properties; rectangles have equal diagonals, rhombuses perpendicular diagonals, squares both.", "**Prove with congruent triangles:** draw a diagonal and use ASA, SAS or SSS, then CPCT.", "The **bisectors of adjacent angles** of a parallelogram meet at 90°.", "In word problems, the Midpoint Theorem turns a **half-length** into a full length; the centroid turns a median into **⅔ and ⅓** parts."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
