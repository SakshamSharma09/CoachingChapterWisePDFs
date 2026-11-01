from math import isqrt
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def dist(vals, c):
    out = []
    for v in vals:
        if v != c and v > 0 and v not in out: out.append(v)
    return out
# A1: chord length from r, d (8)
for r, d, h in [(13, 5, 12), (5, 3, 4), (10, 6, 8), (17, 8, 15), (25, 7, 24), (15, 9, 12), (13, 12, 5), (10, 8, 6)]:
    assert d*d + h*h == r*r
    L = 2*h
    w = dist([h, L+2, L-2, r+d, d+h, 2*d], L)[:3]
    A.append(M4(f"In a circle of radius ${r}$ cm, a chord is ${d}$ cm from the centre. The length of the chord is:", f"{L} cm", [f"{x} cm" for x in w], f"half-chord $=\\sqrt{{{r}^2-{d}^2}}={h}$, so chord $=2\\times{h}={L}$"))
# A2: radius from chord and d (6)
for L, d, r in [(16, 6, 10), (24, 5, 13), (30, 8, 17), (48, 7, 25), (18, 12, 15), (14, 24, 25)]:
    h = L//2; assert h*h + d*d == r*r
    w = dist([h+d, L, r+1, r-1, L+d, d+2], r)[:3]
    A.append(M4(f"A chord of length ${L}$ cm is at a distance of ${d}$ cm from the centre of a circle. The radius of the circle is:", f"{r} cm", [f"{x} cm" for x in w], f"$r=\\sqrt{{{h}^2+{d}^2}}={r}$"))
# A3: distance from centre (4)
for stem, d, r, h in [("The diameter of a circle is 26 cm and a chord is 24 cm long.", 5, 13, 12), ("A chord of length 16 cm is drawn in a circle of radius 17 cm.", 15, 17, 8),
                      ("A chord of length 12 cm is drawn in a circle of radius 10 cm.", 8, 10, 6), ("A chord of length 14 cm is drawn in a circle of radius 25 cm.", 24, 25, 7)]:
    assert d*d + h*h == r*r
    w = dist([r-h, r+h, h+1, d+2, d-1, d+3], d)[:3]
    A.append(M4(f"{stem} The distance of the chord from the centre is:", f"{d} cm", [f"{x} cm" for x in w], f"$d=\\sqrt{{{r}^2-{h}^2}}={d}$"))
# A4: angle at circle from centre (5)
for c in [70, 100, 130, 84, 150]:
    a = c//2
    A.append(M4(f"An arc subtends an angle of ${c}^\\circ$ at the centre. The angle it subtends at a point on the remaining part of the circle is:", f"${a}^\\circ$", [f"${c}^\\circ$", f"${2*c}^\\circ$", f"${180-a}^\\circ$"], "angle at the centre is double the angle on the circle"))
# A5: cyclic quad opposite (5)
for a in [75, 110, 92, 65, 123]:
    A.append(M4(f"ABCD is a cyclic quadrilateral with $\\angle A={a}^\\circ$. Then $\\angle C$ is:", f"${180-a}^\\circ$", [f"${a}^\\circ$", f"${90-a//2}^\\circ$" if a != 90 else "$45^\\circ$", f"${360-a}^\\circ$"], "opposite angles of a cyclic quadrilateral add to $180^\\circ$"))
# A6: circle -> centre (2)
for a in [28, 41]:
    A.append(M4(f"An arc subtends ${a}^\\circ$ at a point on the circle. The angle subtended by the same arc at the centre is:", f"${2*a}^\\circ$", [f"${a}^\\circ$", f"${a//2}^\\circ$" if a%2==0 else f"${a+1}^\\circ$", f"${180-a}^\\circ$"], "central angle is double"))
A += [
 M4("The angle subtended by a diameter at any point on the circle is:", r"$90^\circ$", [r"$60^\circ$", r"$180^\circ$", r"$45^\circ$"], "angle in a semicircle"),
 M4("A perpendicular drawn from the centre of a circle to a chord:", "bisects the chord", ["is equal to the chord", "is equal to the radius", "is parallel to the chord"], "perpendicular from the centre bisects the chord"),
 M4("Equal chords of a circle are at ______ distances from the centre.", "equal", ["unequal", "double", "half"], "equal chords ⇔ equal distances"),
 M4("The greatest chord of a circle is:", "the diameter", ["the radius", "a chord of length equal to the radius", "a chord at distance $r$ from the centre"], "it passes through the centre"),
 M4("Through three non-collinear points the number of circles that can be drawn is:", "exactly one", ["none", "two", "infinitely many"], "unique circumcircle"),
 M4("Through two given points the number of circles that can be drawn is:", "infinitely many", ["exactly one", "exactly two", "none"], "centre can be anywhere on the perpendicular bisector"),
 M4("Points lying on the same circle are called:", "concyclic points", ["collinear points", "coplanar points", "concurrent points"], "definition"),
 M4("Of two chords of a circle, the one nearer to the centre is:", "longer", ["shorter", "equal in length", "cannot be compared"], "longer chord ⇔ closer to the centre"),
 M4("The sum of either pair of opposite angles of a cyclic quadrilateral is:", r"$180^\circ$", [r"$90^\circ$", r"$270^\circ$", r"$360^\circ$"], "Theorem 11"),
 M4("The perpendicular bisector of a chord of a circle always passes through:", "the centre of the circle", ["the midpoint of the arc only", "a point outside the circle", "no fixed point"], "centre is equidistant from the chord's endpoints"),
]
assert len(A) == 8+6+4+5+5+2+10 == 40, len(A)
# B (16)
B += [
 Q(r"A chord of a circle of radius 17 cm is 8 cm away from the centre. Find its length.", r"Half-chord $=\sqrt{17^2-8^2}=\sqrt{225}=15$ cm; chord $=30$ cm.", "1+1"),
 Q(r"A chord of length 40 cm is 21 cm from the centre of a circle. Find the radius.", r"Half-chord 20; $r=\sqrt{20^2+21^2}=\sqrt{841}=29$ cm.", "1+1"),
 Q(r"A cyclic quadrilateral has angles $\angle A=80^\circ,\angle B=110^\circ,\angle C=100^\circ,\angle D=70^\circ$. Can it be drawn? Why?", r"$\angle A+\angle C=180^\circ$ and $\angle B+\angle D=180^\circ$, so yes — opposite angles add up to $180^\circ$ and the quadrilateral is cyclic.", "1+1"),
 Q(r"An arc subtends $70^\circ$ at the centre. Find the angle it subtends at a point on the circle outside the arc.", r"Half of the central angle: $35^\circ$.", "2"),
 Q(r"AB is a diameter of a circle and C is a point on the circle. Find $\angle ACB$ and give the reason.", r"$90^\circ$ — the angle subtended by a diameter at any point of the circle (angle in a semicircle).", "1+1"),
 Q(r"Show that the length of a chord at distance $d$ from the centre of a circle of radius $r$ is $2\sqrt{r^2-d^2}$.", r"The perpendicular from the centre bisects the chord; by the Baudhāyana–Pythagoras Theorem half-chord $=\sqrt{r^2-d^2}$, so chord $=2\sqrt{r^2-d^2}$.", "1+1"),
 Q(r"PQRS is cyclic with $\angle P=(2x+10)^\circ$ and $\angle R=(3x-20)^\circ$. Find $x$.", r"$2x+10+3x-20=180\Rightarrow5x=190\Rightarrow x=38$; $\angle P=86^\circ,\angle R=94^\circ$.", "1+1"),
 Q(r"ABCD is cyclic with $\angle A=75^\circ$ and $\angle B=110^\circ$. Find $\angle C$ and $\angle D$.", r"$\angle C=180^\circ-75^\circ=105^\circ$; $\angle D=180^\circ-110^\circ=70^\circ$.", "1+1"),
 Q(r"In a circle of radius 12 cm, the chord AB subtends $60^\circ$ at the centre O. Find AB.", r"$OA=OB$ and $\angle AOB=60^\circ$ ⇒ $\triangle OAB$ is equilateral, so $AB=12$ cm.", "1+1"),
 Q(r"A circle has radius 13 cm. Two chords of length 10 cm each are drawn. Find their distance from the centre and state the relation between the distances.", r"$d=\sqrt{13^2-5^2}=12$ cm for each; equal chords are equidistant from the centre.", "1+1"),
 Q(r"In a circle of radius 5 cm, one chord is 3 cm from the centre and another is 4 cm from the centre. Which is longer? Find both lengths.", r"Chord at 3 cm: $2\sqrt{25-9}=8$ cm; chord at 4 cm: $2\sqrt{25-16}=6$ cm. The chord nearer the centre is longer.", "1+1"),
 Q(r"Points C and D lie on the same side of AB and $\angle ACB=\angle ADB$. What can you say about A, B, C, D?", r"The four points are concyclic (Theorem 10): they lie on one circle.", "2"),
 Q(r"ABCD is a cyclic quadrilateral with $\angle A=3x^\circ$ and $\angle C=(2x+30)^\circ$. Find $x$ and $\angle A$.", r"$5x+30=180\Rightarrow x=30$; $\angle A=90^\circ$.", "1+1"),
 Q(r"An arc subtends an angle of $50^\circ$ at a point on the circle. What angle does it subtend at the centre?", r"$2\times50^\circ=100^\circ$.", "2"),
 Q(r"In quadrilateral ABCD, $\angle A=100^\circ$ and $\angle C=80^\circ$. Is it cyclic? Give a reason.", r"$\angle A+\angle C=180^\circ$, so by the converse (Theorem 12) the vertices are concyclic.", "1+1"),
 Q(r"Side BC of cyclic quadrilateral ABCD is produced to E and $\angle DCE=70^\circ$. Find $\angle A$.", r"$\angle BCD=180^\circ-70^\circ=110^\circ$; opposite angle $\angle A=180^\circ-110^\circ=70^\circ$.", "1+1"),
]
assert len(B) == 16, len(B)
# C (24)
C += [
 Q(r"Prove that the perpendicular from the centre of a circle to a chord bisects the chord.", r"Let $OM\perp AB$. In right triangles $OMA$ and $OMB$: $OA=OB$ (radii), $OM$ common, $\angle OMA=\angle OMB=90^\circ$ ⇒ congruent (RHS) (2). So $AM=MB$ (1).", "2+1"),
 Q(r"Prove that the angle subtended by a diameter at any point on the circle is $90^\circ$.", r"The arc not containing $D$ subtends a straight angle $180^\circ$ at the centre (1). The angle at $D$ is half of this (1): $\angle ADB=\frac12\times180^\circ=90^\circ$ (1).", "1+1+1"),
 Q(r"Prove that the sum of the opposite angles of a cyclic quadrilateral ABCD is $180^\circ$ (use the angle-at-centre theorem).", r"Arcs BCD and BAD together make the whole circle. $\angle BAD=\frac12$(reflex $\angle BOD$) and $\angle BCD=\frac12\angle BOD$ (2). Sum $=\frac12\times360^\circ=180^\circ$ (1).", "2+1"),
 Q(r"A chord is 9 cm from the centre of a circle of radius 15 cm. Find its length.", r"Half-chord $=\sqrt{15^2-9^2}=12$; chord $=24$ cm.", "2+1"),
 Q(r"Two chords AB (30 cm) and CD (16 cm) lie on the same side of the centre of a circle of radius 17 cm. Find the distance between them.", r"Distance of AB: $\sqrt{17^2-15^2}=8$; of CD: $\sqrt{17^2-8^2}=15$ (2). Same side ⇒ $15-8=7$ cm (1).", "2+1"),
 Q(r"Two parallel chords of length 6 cm and 8 cm are in a circle of radius 5 cm. Find the distance between them if they are on opposite sides of the centre.", r"Distances: $\sqrt{25-9}=4$ and $\sqrt{25-16}=3$ (2). Opposite sides: $4+3=7$ cm (1).", "2+1"),
 Q(r"Prove that equal chords of a circle are equidistant from the centre.", r"Let $AB=CD$ with perpendiculars $OM,ON$ from $O$. Then $AM=\frac12AB=\frac12CD=CN$ (1). In right triangles $OMA,ONC$: $OA=OC$, $AM=CN$ ⇒ congruent (RHS) (1), so $OM=ON$ (1).", "1+1+1"),
 Q(r"ABCD is a cyclic quadrilateral with $\angle ABC=110^\circ$. Find the reflex angle $AOC$ at the centre $O$, where the arc is ADC.", r"B lies on the circle outside arc ADC, so the angle at the centre is double: $2\times110^\circ=220^\circ$.", "2+1"),
 Q(r"A triangle ABC is inscribed in a circle with centre O and $\angle BAC=50^\circ$. Find $\angle BOC$ and $\angle OBC$.", r"$\angle BOC=2\times50^\circ=100^\circ$ (1). $OB=OC$ ⇒ $\angle OBC=\angle OCB=\frac{180^\circ-100^\circ}2=40^\circ$ (2).", "1+2"),
 Q(r"AB is a diameter of a circle, C is on the circle and $\angle CAB=35^\circ$. Find $\angle ABC$.", r"$\angle ACB=90^\circ$ (angle in a semicircle) (1); $\angle ABC=180^\circ-90^\circ-35^\circ=55^\circ$ (2).", "1+2"),
 Q(r"If two equal chords of a circle intersect inside the circle, show that the segments of one chord are equal to the corresponding segments of the other.", r"Let chords AB, CD (equal) meet at P and draw $OM\perp AB,ON\perp CD$; $OM=ON$ (equal chords) (1). Right triangles $OMP,ONP$ are congruent (RHS) ⇒ $PM=PN$ (1). Since $AM=CN$ (halves of equal chords), $AP=CP$ and so $PB=PD$ (1).", "1+1+1"),
 Q(r"A cyclic quadrilateral has sides 5, 5, 12, 12 units in order. Find its area.", r"The diagonal is $\sqrt{5^2+12^2}=13$; the quadrilateral is made of two right triangles with legs 5 and 12 (1+1): area $=2\times\frac12\times5\times12=60$ square units (1).", "1+1+1"),
 Q(r"In cyclic quadrilateral ABCD, $\angle A=(4x-4)^\circ$ and $\angle C=(2x+16)^\circ$. Find $x$ and both angles.", r"$6x+12=180\Rightarrow x=28$ (2). $\angle A=108^\circ,\angle C=72^\circ$ (1).", "2+1"),
 Q(r"Show that a cyclic parallelogram is a rectangle.", r"In a parallelogram opposite angles are equal: $\angle A=\angle C$ (1). In a cyclic quadrilateral $\angle A+\angle C=180^\circ$ (1). So each is $90^\circ$ ⇒ rectangle (1).", "1+1+1"),
 Q(r"ABCD is a cyclic trapezium with $AB\parallel CD$. Show that its non-parallel sides AD and BC are equal.", r"$\angle A+\angle D=180^\circ$ (co-interior) and $\angle A+\angle C=180^\circ$ (cyclic) ⇒ $\angle C=\angle D$ (2). Base angles equal ⇒ $AD=BC$ (1).", "2+1"),
 Q(r"ABCD is cyclic, $\angle BAC=30^\circ$ and $\angle BCD=100^\circ$. Find $\angle CBD$.", r"$\angle BDC=\angle BAC=30^\circ$ (angles in the same segment) (1+1). $\angle CBD=180^\circ-100^\circ-30^\circ=50^\circ$ (1).", "2+1"),
 Q(r"A chord of a circle of radius $r$ is at distance $d$ from the centre. Derive the chord length. Hence find it for $r=10$ and $d=6$.", r"Half-chord $=\sqrt{r^2-d^2}$ (Baudhāyana–Pythagoras) (1); chord $=2\sqrt{r^2-d^2}$ (1). For $r=10,d=6$: $2\sqrt{64}=16$ (1).", "1+1+1"),
 Q(r"In a circle of radius 10 cm there are two chords at distances 6 cm and 8 cm from the centre. Find their lengths and show that the nearer one is longer.", r"At 6 cm: $2\sqrt{100-36}=16$ cm; at 8 cm: $2\sqrt{100-64}=12$ cm (2). $16>12$ and $6<8$: the chord nearer the centre is longer (1).", "2+1"),
 Q(r"Three friends stand at three points of a park that are not in a line. Where should a fountain be placed so that it is equally far from all three? Justify.", r"At the point where the perpendicular bisectors of the segments joining the friends meet (the circumcentre) (2). Points on a perpendicular bisector are equidistant from the ends, so this point is equidistant from all three (1).", "2+1"),
 Q(r"Find the centre and radius of the circle through $(0,0)$, $(6,0)$ and $(0,8)$.", r"The angle at the origin is $90^\circ$, so the hypotenuse joining $(6,0)$ and $(0,8)$ is a diameter (1). Its midpoint $(3,4)$ is the centre (1); radius $=\frac12\sqrt{36+64}=5$ (1).", "1+1+1"),
 Q(r"Prove that equal chords of a circle subtend equal angles at the centre.", r"Let $AB=CD$. In $\triangle AOB$ and $\triangle COD$: $OA=OC$, $OB=OD$, $AB=CD$ ⇒ congruent (SSS) (2). So $\angle AOB=\angle COD$ (1).", "2+1"),
 Q(r"An arc AB subtends $\angle AOB=(6x-10)^\circ$ at the centre and $\angle ACB=(2x+5)^\circ$ at a point C on the circle. Find $x$.", r"Central angle is double: $6x-10=2(2x+5)=4x+10$ (2) ⇒ $x=10$; angles $50^\circ$ and $25^\circ$ (1).", "2+1"),
 Q(r"The angles A and C of a cyclic quadrilateral are in the ratio 4 : 5. Find them.", r"$4k+5k=180^\circ\Rightarrow k=20^\circ$ (2); $\angle A=80^\circ,\angle C=100^\circ$ (1).", "2+1"),
 Q(r"Explain why three collinear points cannot lie on a circle.", r"A line meets a circle in at most two points; hence three points on a line cannot all be on one circle (equivalently, a circle can be drawn through three points only if they are non-collinear).", "1+2"),
]
assert len(C) == 24, len(C)
# D (16)
D += [
 Q(r"Prove that the angle subtended by an arc at the centre of a circle is double the angle subtended by it at any point on the circle outside the arc (take the case where DC produced meets the circle at E on the arc).", r"Join $D$ to $C$ and extend to $E$ on arc AFB (1). $\triangle DCB$ is isosceles ($CB=CD$) ⇒ $\angle CBD=\angle CDB$; exterior angle $\angle BCE=2\angle BDC$ (2). Likewise $\angle ACE=2\angle CDA$ (1). Add: $\angle BCA=2(\angle BDC+\angle CDA)=2\angle BDA$ (1).", "1+2+1+1"),
 Q(r"Prove that the sum of the opposite angles of a cyclic quadrilateral is $180^\circ$.", r"Let ABCD be cyclic with centre $O$. Arc BCD: A is outside it, so $\angle BAD=\frac12$(reflex $\angle BOD$) (2). Arc BAD: C is outside it, so $\angle BCD=\frac12\angle BOD$ (2). Sum $=\frac12\times360^\circ=180^\circ$ (1).", "2+2+1"),
 Q(r"Prove that of two chords of a circle, the longer chord is nearer to the centre.", r"Let $AB>DE$ with perpendiculars $CF,CG$ from the centre $C$. $AC=CD$ (radii). By Pythagoras: $CF^2+AF^2=CG^2+GD^2$ (2). F and G are midpoints, so $AF>GD$ (1) ⇒ $AF^2>GD^2$ ⇒ $CF^2<CG^2$ (1) ⇒ $CF<CG$ (1).", "2+1+1+1"),
 Q(r"<b>Case study:</b> A circular park has radius 25 m. Two straight paths (chords) of lengths 14 m and 48 m are laid. (i) Find the distance of each path from the centre. (ii) Which is nearer the centre and why? (iii) Find the distance between the paths if they are parallel and on opposite sides of the centre. (iv) Find it if they are on the same side.", r"(i) 14 m path: $\sqrt{25^2-7^2}=24$ m. 48 m path: $\sqrt{25^2-24^2}=7$ m (2). (ii) The 48 m path (longer chord is nearer) (1). (iii) $24+7=31$ m (1). (iv) $24-7=17$ m (1).", "2+1+1+1"),
 Q(r"<b>Case study:</b> Points A(0,0), B(8,0), C(0,6) and D(8,6) are corners of a rectangular plot. (i) Find the length of diagonal BC. (ii) Find the centre and radius of the circle through A, B, C. (iii) Show that D lies on the same circle. (iv) What type of quadrilateral is ABDC and why is it cyclic?", r"(i) $BC=\sqrt{64+36}=10$ (1). (ii) $\angle A=90^\circ$ ⇒ BC is a diameter; centre $(4,3)$, radius 5 (2). (iii) Distance from $(4,3)$ to $(8,6)$ $=\sqrt{16+9}=5$ (1). (iv) A rectangle; opposite angles are $90^\circ+90^\circ=180^\circ$ so it is cyclic (1).", "1+2+1+1"),
 Q(r"Prove that if the opposite angles of a quadrilateral ABCD add up to $180^\circ$, then it is cyclic (do the case where C lies outside the circle through A, B, D).", r"Draw the circle through A, B, D (1). Suppose it cuts CD at E. ABED is cyclic ⇒ $\angle BAD+\angle BED=180^\circ$ (1). Given $\angle BAD+\angle BCD=180^\circ$ ⇒ $\angle BED=\angle BCD$ (1). But $\angle BED$ is the exterior angle of $\triangle BEC$ so $\angle BED>\angle BCD$ — a contradiction (2). Hence C lies on the circle.", "1+1+1+2"),
 Q(r"Prove that the perpendicular bisector of a chord of a circle passes through the centre.", r"Let $AB$ be a chord with midpoint $M$ and centre $O$. $OA=OB$ (radii), $AM=MB$, $OM$ common ⇒ $\triangle OMA\cong\triangle OMB$ (SSS) (2). So $\angle OMA=\angle OMB=90^\circ$ (1) ⇒ $OM\perp AB$ at its midpoint, i.e. $O$ lies on the perpendicular bisector of $AB$ (2).", "2+1+2"),
 Q(r"ABCD is a cyclic quadrilateral with $\angle A=(3x+5)^\circ$, $\angle B=(2y+10)^\circ$, $\angle C=(5x-25)^\circ$, $\angle D=(4y-10)^\circ$. (i) Find $x$ and $y$. (ii) Find all four angles. (iii) Verify that the angle sum is $360^\circ$.", r"(i) $A+C=180$: $8x-20=180\Rightarrow x=25$; $B+D=180$: $6y=180\Rightarrow y=30$ (2). (ii) $\angle A=80^\circ,\angle B=70^\circ,\angle C=100^\circ,\angle D=110^\circ$ (2). (iii) $80+70+100+110=360$ ✓ (1).", "2+2+1"),
 Q(r"<b>Case study:</b> A round table has centre O and radius 60 cm. Three diners sit at A, B, C on its edge with $\angle BAC=40^\circ$. (i) Find $\angle BOC$. (ii) Find $\angle OBC$. (iii) A fourth diner sits at D on the same arc as A; find $\angle BDC$. (iv) If M is the midpoint of BC and $OM=36$ cm, find BC.", r"(i) $80^\circ$ (1). (ii) $OB=OC$ ⇒ $\angle OBC=50^\circ$ (1). (iii) Same segment ⇒ $\angle BDC=40^\circ$ (1). (iv) Half-chord $=\sqrt{60^2-36^2}=48$; $BC=96$ cm (2).", "1+1+1+2"),
 Q(r"Prove that if two chords of a circle are equidistant from the centre, they are equal; then find the length of each chord if the distance is 12 cm and the radius is 13 cm.", r"Let $OM=ON$ with $OM\perp AB,ON\perp CD$. Right triangles $OMA,ONC$: $OA=OC$, $OM=ON$ ⇒ congruent (RHS) ⇒ $AM=CN$ (2). Halves equal ⇒ $AB=CD$ (1). Length $=2\sqrt{169-144}=10$ cm (2).", "2+1+2"),
 Q(r"Prove that the angle subtended by an arc at a point on the circle is half the angle at the centre in the case where the line DC produced meets the circle at a point E outside the arc.", r"$CA=CD$ ⇒ $\angle ACE=2\angle ADC$ (exterior angle) (2). $CB=CD$ ⇒ $\angle BCE=2\angle BDC$ (2). Subtract: $\angle ACB=\angle ACE-\angle BCE=2(\angle ADC-\angle BDC)=2\angle ADB$ (1).", "2+2+1"),
 Q(r"<b>Case study:</b> In a circle with centre O, AB is a diameter and C, D are points on the circle on opposite sides of AB. $\angle CAB=30^\circ$ and $\angle ABD=50^\circ$. (i) Find $\angle ACB$ and $\angle ADB$. (ii) Find $\angle ABC$. (iii) Find $\angle BAD$. (iv) State whether ACBD is cyclic and why.", r"(i) Both are angles in a semicircle: $90^\circ$ each (2). (ii) $180-90-30=60^\circ$ (1). (iii) $180-90-50=40^\circ$ (1). (iv) ACBD has all four vertices on the circle, so it is cyclic (1).", "2+1+1+1"),
 Q(r"Prove that a cyclic parallelogram is a rectangle and that its diagonals are diameters of the circle.", r"Opposite angles of a parallelogram are equal and in a cyclic quadrilateral they add to $180^\circ$, so each is $90^\circ$: a rectangle (3). Each diagonal then subtends $90^\circ$ at the other two vertices, so it is a diameter (2).", "3+2"),
 Q(r"<b>Case study:</b> A ground is a circle of radius 13 m. Two parallel boundary ropes (chords) are 10 m and 24 m long. (i) Find the distance of each from the centre. (ii) How far apart are they if on opposite sides of the centre? (iii) How far if on the same side? (iv) Which rope is longer and which is nearer to the centre?", r"(i) 10 m rope: $\sqrt{169-25}=12$ m; 24 m rope: $\sqrt{169-144}=5$ m (2). (ii) $12+5=17$ m (1). (iii) $12-5=7$ m (1). (iv) 24 m rope is longer and nearer to the centre (1).", "2+1+1+1"),
 Q(r"A cyclic quadrilateral has sides 5, 5, 12, 12 (in order). (i) Show that its diagonal is a diameter and find the radius. (ii) Find its area. (iii) Explain why this quadrilateral is not a rectangle.", r"(i) Diagonal $=\sqrt{25+144}=13$; angle in a semicircle ⇒ it is a diameter, radius 6.5 (2). (ii) $2\times\frac12\times5\times12=60$ sq. units (2). (iii) Its sides in order are 5,5,12,12 (a kite) — opposite sides are not equal, so it is not a rectangle (1).", "2+2+1"),
 Q(r"(i) Prove that an angle inscribed in a semicircle is $90^\circ$. (ii) Chord AB subtends $\angle ACB=62^\circ$ at C on the major arc. Find the angle AB subtends at the centre and at a point D on the minor arc.", r"(i) The arc on the other side of the diameter subtends $180^\circ$ at the centre, so the inscribed angle is $90^\circ$ (2). (ii) Centre: $2\times62^\circ=124^\circ$ (1). ACBD is cyclic so $\angle ADB=180^\circ-62^\circ=118^\circ$ (2).", "2+1+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
