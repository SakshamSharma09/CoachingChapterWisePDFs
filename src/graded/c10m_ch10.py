"""Class 10 Maths Ch 10 - Circles (graded banks). Tangent theorems only (no secant-tangent product, no alternate-segment theorem)."""
from c10m_x import *

SLUG, NAME, CHNO = "Circles", "Circles", 10
ALL = triples(100)
LO = [x for x in ALL if x[2] <= 30]
MID = [x for x in ALL if 30 < x[2] <= 65]
HI = [x for x in ALL if x[2] > 65]

def cm(x): return f"{nd(x)} cm"
def dg(x): return f"${nd(x)}^\\circ$"
def sc_(stem0, ask, ans, ex, parts, fmt=cm):
    ans = ans if isinstance(ans, list) else [ans]
    w = nums_near(ans[0], ex) if len(ans) == 1 else []
    return SCG(stem0, ask, ans, w, parts, fmt)

def tlen(r, d):
    p = isqrt(d * d - r * r); assert p * p + r * r == d * d
    return sc_(f"A point $P$ is {d} cm from the centre $O$ of a circle of radius {r} cm.", "length of the tangent drawn from $P$ to the circle", p, [d - r, d + r, d * d - r * r],
               ["The radius to the point of contact $T$ is perpendicular to the tangent, so $\\triangle OTP$ is right-angled at $T$", f"$PT^2=OP^2-OT^2={d}^2-{r}^2={d*d-r*r}$", f"$PT={p}$ cm"])
def rad(p, d):
    r = isqrt(d * d - p * p); assert r * r + p * p == d * d
    return sc_(f"The length of the tangent from an external point $P$ to a circle is {p} cm and $P$ is {d} cm from the centre.", "radius of the circle", r, [d - p, p + 1, d + p],
               ["Radius $\\perp$ tangent at the point of contact, so the triangle formed by $O$, $P$ and the point of contact is right-angled", f"$r^2=OP^2-PT^2={d}^2-{p}^2={d*d-p*p}$", f"$r={r}$ cm"])
def opd(r, p):
    d = isqrt(r * r + p * p); assert d * d == r * r + p * p
    return sc_(f"A tangent to a circle of radius {r} cm has length {p} cm from the external point $P$ to the point of contact.", "distance of $P$ from the centre of the circle", d, [r + p, p - r if p > r else r - p + 1, d * 2],
               ["Radius $\\perp$ tangent, so $OP$ is the hypotenuse of a right triangle with sides $r$ and $PT$", f"$OP^2=r^2+PT^2={r}^2+{p}^2={r*r+p*p}$", f"$OP={d}$ cm"])
def quadp(r, p):
    v = 2 * (r + p)
    return sc_(f"Tangents $PA$ and $PB$ are drawn from an external point $P$ to a circle of centre $O$ and radius {r} cm. The length of each tangent is {p} cm.", "perimeter of the quadrilateral $PAOB$", v, [r + p, 2 * p, 4 * r + p],
               ["$PA=PB$ (tangents from an external point) and $OA=OB=r$", f"Perimeter $=PA+AO+OB+BP=2({p})+2({r})$", f"Perimeter $={v}$ cm"])
def quada(r, p):
    v = r * p
    return sc_(f"Tangents $PA$ and $PB$ are drawn from an external point $P$ to a circle of centre $O$ and radius {r} cm. The length of each tangent is {p} cm.", "area of the quadrilateral $PAOB$ (in cm$^2$)", v, [2 * v, v // 2 if v % 2 == 0 else v + 1, (r + p) * 2],
               ["$\\angle OAP=\\angle OBP=90^\\circ$, so $PAOB$ is made of two congruent right triangles", f"Area $=2\\times\\frac12\\times{r}\\times{p}$", f"Area $={v}$ cm$^2$"], fmt=lambda x: f"{nd(x)} cm²")
def angpa(x):
    return sc_(f"$PA$ and $PB$ are tangents from an external point $P$ to a circle with centre $O$, touching it at $A$ and $B$. $\\angle AOB={x}^\\circ$.", "$\\angle APB$", 180 - x, [x, 90 - x // 2 if x % 2 == 0 else 90 - x, 2 * x if 2 * x != 180 - x else 90],
               ["$OA\\perp PA$ and $OB\\perp PB$, so $\\angle OAP=\\angle OBP=90^\\circ$", f"In quadrilateral $OAPB$: $\\angle APB=360^\\circ-90^\\circ-90^\\circ-{x}^\\circ$", f"$\\angle APB={180-x}^\\circ$"], fmt=dg)
def oab(y):
    return sc_(f"$PA$ and $PB$ are tangents from an external point $P$ to a circle with centre $O$, touching it at $A$ and $B$. $\\angle APB={y}^\\circ$.", "$\\angle OAB$", y // 2, [y, 90 - y // 2 if y // 2 != 90 - y // 2 else 30, (180 - y) // 2 if (180 - y) // 2 != y // 2 else 20, 90 - y, 180 - y, 2 * y, y + 30],
               [f"$PA=PB$, so $\\angle PAB=\\frac{{180^\\circ-{y}^\\circ}}{{2}}={90-y//2}^\\circ$", "$\\angle OAP=90^\\circ$ (radius $\\perp$ tangent)", f"$\\angle OAB=90^\\circ-{90-y//2}^\\circ={y//2}^\\circ$"], fmt=dg)
def apb_from_pab(x):
    return sc_(f"$PA$ and $PB$ are tangents from an external point $P$ to a circle, and $\\angle PAB={x}^\\circ$.", "$\\angle APB$", 180 - 2 * x, [x, 2 * x, 90 - x],
               ["$PA=PB$, so $\\triangle PAB$ is isosceles and $\\angle PBA=\\angle PAB$", f"$\\angle APB=180^\\circ-{x}^\\circ-{x}^\\circ$", f"$\\angle APB={180-2*x}^\\circ$"], fmt=dg)
def aop(x):
    return sc_(f"$PA$ is a tangent at $A$ to a circle with centre $O$, and $\\angle OPA={x}^\\circ$.", "$\\angle AOP$", 90 - x, [x, 180 - x, 90 + x],
               ["$OA\\perp PA$, so $\\triangle OAP$ is right-angled at $A$", f"$\\angle AOP=180^\\circ-90^\\circ-{x}^\\circ$", f"$\\angle AOP={90-x}^\\circ$"], fmt=dg)
def circq(ab, bc, cd):
    ad = ab + cd - bc
    return sc_(f"A quadrilateral $ABCD$ is drawn about a circle so that all four sides touch the circle. $AB={ab}$ cm, $BC={bc}$ cm and $CD={cd}$ cm.", "length of $AD$", ad, [ab + bc + cd, ab + bc - cd if ab + bc > cd else 1, bc + cd - ab],
               ["For a quadrilateral circumscribed about a circle, $AB+CD=AD+BC$", f"${ab}+{cd}=AD+{bc}$", f"$AD={ad}$ cm"])
def incirc(a, b, c):
    s2 = a + b + c; assert s2 % 2 == 0
    s = s2 // 2; x, y, z = s - a, s - b, s - c   # AF=AE=x, BD=BF=y, CD=CE=z (a=BC, b=CA, c=AB)
    return sc_(f"The incircle of $\\triangle ABC$ touches $BC$, $CA$ and $AB$ at $D$, $E$ and $F$. $AB={c}$ cm, $BC={a}$ cm and $CA={b}$ cm.", "lengths $AF$, $BD$ and $CE$ (in this order)", [x, y, z], (),
               ["Tangent lengths from a vertex are equal: $AF=AE=x$, $BD=BF=y$, $CD=CE=z$", f"$x+y={c}$, $y+z={a}$, $z+x={b}$; adding, $x+y+z={s}$", f"$AF={x}$ cm, $BD={y}$ cm, $CE={z}$ cm"])
def inrad(a, b, c):
    r = (a + b - c) // 2; assert (a + b - c) % 2 == 0
    return sc_(f"In $\\triangle ABC$, right-angled at $B$, $AB={a}$ cm and $BC={b}$ cm. A circle is inscribed in the triangle.", "radius of the inscribed circle", r, [a + b - c, (a + b + c) // 2 - c + 1, c // 2],
               [f"$AC={c}$ cm; the incircle touches $AB$, $BC$ at $F$, $D$ and $BDOF$ is a square of side $r$", f"$AF=AB-r={a}-r$, $CD=BC-r={b}-r$ and $AF+CD=AC$ (tangent lengths)", f"$({a}-r)+({b}-r)={c}$ gives $r={r}$ cm"])
def conc(R, r):
    h = isqrt(R * R - r * r); assert h * h + r * r == R * R
    return sc_(f"Two concentric circles have radii {R} cm and {r} cm. A chord of the larger circle touches the smaller circle.", "length of the chord", 2 * h, [h, R + r, 2 * (R - r), 2 * r, R - r, 2 * R],
               ["The chord touches the smaller circle at $M$, so $OM\\perp$ chord and $M$ is the midpoint of the chord", f"Half-chord $=\\sqrt{{{R}^2-{r}^2}}={h}$ cm", f"Chord $=2\\times{h}={2*h}$ cm"])
def eqt(a, b, c, d):
    x = F(d - b, a - c); pa = a * x + b; assert x.denominator == 1
    return sc_(f"Tangents $QA$ and $QB$ are drawn from an external point $Q$ to a circle, and $QA=({a}x+{b})$ cm and $QB=({c}x+{d})$ cm.", "length of $QA$", pa, [x, pa + 2, a * x + d],
               ["Tangents from an external point are equal: $QA=QB$", f"${a}x+{b}={c}x+{d}$ gives $x={nd(x)}$", f"$QA={a}({nd(x)})+{b}={nd(pa)}$ cm"])
def chord_contact(r, p, d):
    ab = F(2 * r * p, d)
    return sc_(f"Tangents $PA$ and $PB$ are drawn from a point $P$, {d} cm from the centre $O$ of a circle of radius {r} cm. The length of each tangent is {p} cm.", "length of the chord $AB$", ab, [2 * p, 2 * r, F(r * p, d)],
               [f"Area of $\\triangle OAP=\\frac12\\times{r}\\times{p}$ and also $=\\frac12\\times OP\\times AM$ where $AM\\perp OP$ ($M$ is the midpoint of $AB$)", f"$AM=\\frac{{{r}\\times{p}}}{{{d}}}={nd(F(r*p,d))}$ cm", f"$AB=2AM={nd(ab)}$ cm"])
def third_tangent(pa):
    return sc_(f"$PA$ and $PB$ are tangents from $P$ to a circle, each of length {pa} cm. A third tangent touches the circle at $E$ on the minor arc $AB$ and meets $PA$ at $C$ and $PB$ at $D$.", "perimeter of $\\triangle PCD$", 2 * pa, [pa, 3 * pa, pa + 2],
               ["$CA=CE$ and $DB=DE$ (tangents from $C$ and $D$)", "Perimeter $=PC+CE+ED+DP=PC+CA+DB+DP=PA+PB$", f"Perimeter $=2\\times{pa}={2*pa}$ cm"])

CE = [M4("A tangent to a circle meets the circle in exactly:", "one point", ["two points", "no point", "three points"], "Definition of a tangent"),
      M4("The angle between a tangent to a circle and the radius through the point of contact is:", "$90^\\circ$", ["$0^\\circ$", "$45^\\circ$", "$180^\\circ$"], "Radius $\\perp$ tangent"),
      M4("The number of tangents that can be drawn to a circle from a point lying inside it is:", "0", ["1", "2", "infinite"], "Every line through an inside point cuts the circle in two points"),
      M4("The number of tangents that can be drawn to a circle from a point lying on it is:", "1", ["0", "2", "infinite"], "Only one tangent at a point of the circle"),
      M4("The number of tangents that can be drawn to a circle from an external point is:", "2", ["1", "0", "4"], "Two equal tangents"),
      M4("A line that intersects a circle at two distinct points is called a:", "secant", ["tangent", "radius", "diameter"], "Definition of a secant"),
      M4("The tangents drawn at the two ends of a diameter of a circle are:", "parallel", ["perpendicular", "intersecting at the centre", "equal in length and intersecting"], "Both are perpendicular to the diameter")]
CN = [M4("If tangents $PA$ and $PB$ from an external point $P$ to a circle with centre $O$ are inclined to each other at $80^\\circ$, then $\\angle POA$ is:", "$50^\\circ$", ["$100^\\circ$", "$40^\\circ$", "$80^\\circ$"], "$\\angle AOB=100^\\circ$ and $OP$ bisects it"),
      M4("A tangent $PQ$ at a point $P$ of a circle of radius 5 cm meets a line through the centre $O$ at a point $Q$ so that $OQ=12$ cm. The length of $PQ$ is:", "$\\sqrt{119}$ cm", ["12 cm", "13 cm", "$8.5$ cm"], "$PQ^2=144-25=119$"),
      M4("From a point $Q$ the length of the tangent to a circle is 24 cm and the distance of $Q$ from the centre is 25 cm. The radius of the circle is:", "7 cm", ["12 cm", "24 cm", "25 cm"], "$r^2=625-576=49$"),
      M4("If a tangent $PQ$ at a point $Q$ of a circle with centre $O$ makes $\\angle OPQ=30^\\circ$, then $\\angle POQ$ is:", "$60^\\circ$", ["$30^\\circ$", "$90^\\circ$", "$120^\\circ$"], "$\\angle OQP=90^\\circ$"),
      M4("A quadrilateral $ABCD$ is drawn to circumscribe a circle. Which of the following is true?", "$AB+CD=AD+BC$", ["$AB+AD=BC+CD+1$", "$AB=CD$", "$AB+BC=AD$"], "Property of a circumscribed quadrilateral"),
      M4("A circle touches all four sides of a parallelogram. The parallelogram must be a:", "rhombus", ["rectangle", "square only", "trapezium"], "$AB+CD=AD+BC$ gives $AB=BC$")]
CM = [M4("The length of a tangent from a point $P$ to a circle is 12 cm and the radius is 5 cm. The distance of $P$ from the centre is:", "13 cm", ["17 cm", "$\\sqrt{119}$ cm", "7 cm"], "$OP^2=144+25=169$"),
      M4("Two tangents $PA$ and $PB$ are drawn from $P$ and $\\angle APB=90^\\circ$. The quadrilateral $OAPB$ is a:", "square", ["rectangle that is not a square", "kite that is not a rhombus", "trapezium"], "Four right angles and $OA=OB=PA=PB$"),
      M4("The centre of a circle is $O$ and $PT$ is a tangent from $P$. If $OP=2\\cdot OT$, then $\\angle TOP$ is:", "$60^\\circ$", ["$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], "$\\cos\\angle TOP=OT/OP=\\frac12$"),
      M4("If a circle is inscribed in $\\triangle ABC$ touching $AB$ at $F$ and $AC$ at $E$, then:", "$AF=AE$", ["$AF=BF$", "$AE=EC$", "$AF=BC$"], "Tangents from $A$"),
      M4("The sides of a quadrilateral circumscribing a circle, in order, are $a$, $b$, $c$, $d$. Then:", "$a+c=b+d$", ["$a+b=c+d$", "$a+d=b+c+1$", "$a=c$"], "Opposite sides sum equal")]
CH = [M4("$AB$ is a chord of a circle with centre $O$ and $PA$, $PB$ are tangents. Then the line $OP$ is:", "the perpendicular bisector of $AB$", ["parallel to $AB$", "equal to $AB$", "a tangent to the circle"], "$PA=PB$ and $OA=OB$"),
      M4("The radius of the incircle of a right triangle with legs $a$, $b$ and hypotenuse $c$ is:", "$\\dfrac{a+b-c}{2}$", ["$\\dfrac{a+b+c}{2}$", "$\\dfrac{ab}{c}$", "$\\dfrac{a+b}{2}$"], "$r=s-c$ for a right angle"),
      M4("A circle has centre $O$. Tangents at $A$ and $B$ meet at $P$ and $\\angle AOB=2\\angle APB$. Then $\\angle APB$ equals:", "$60^\\circ$", ["$45^\\circ$", "$90^\\circ$", "$30^\\circ$"], "$3\\angle APB=180^\\circ$"),
      M4("Two tangents are drawn from $P$ to a circle of radius $r$ and the angle between them is $60^\\circ$. The distance $OP$ is:", "$2r$", ["$r$", "$\\sqrt2\\,r$", "$\\sqrt3\\,r$"], "$\\sin30^\\circ=r/OP$"),
      M4("If a parallelogram $ABCD$ has an inscribed circle and $AB=8$ cm, then its perimeter is:", "32 cm", ["16 cm", "24 cm", "64 cm"], "It is a rhombus of side 8 cm")]

def dcomp(r, d):
    p = isqrt(d * d - r * r); assert p * p + r * r == d * d
    return SCG(f"Tangents $PA$ and $PB$ are drawn from a point $P$ at a distance of {d} cm from the centre $O$ of a circle of radius {r} cm.", "length of each tangent, the perimeter and the area of the quadrilateral $PAOB$ (in this order)", [p, 2 * (p + r), p * r], [],
               ["$OA\\perp PA$, so $PA^2=OP^2-OA^2$ and $PA=PB$", f"$PA=\\sqrt{{{d}^2-{r}^2}}={p}$ cm; perimeter $=2({p}+{r})$", f"Perimeter ${2*(p+r)}$ cm; area $=2\\times\\frac12\\times{r}\\times{p}={p*r}$ cm$^2$"],
               lambda x: nd(x))
def dcomp2(a, b, c):
    r = (a + b - c) // 2
    return SCG(f"In $\\triangle ABC$, $\\angle B=90^\\circ$, $AB={a}$ cm and $BC={b}$ cm. A circle touching all three sides touches $AB$ at $F$ and $BC$ at $D$.", "radius of the circle and the lengths $AF$ and $CD$ (in this order)", [r, a - r, b - r], [],
               [f"$AC=\\sqrt{{{a}^2+{b}^2}}={c}$ cm; $BDOF$ is a square of side $r$, so $BF=BD=r$", f"$AF=AE={a}-r$ and $CD=CE={b}-r$ and $AE+EC=AC$: $({a}-r)+({b}-r)={c}$", f"$r={r}$ cm, $AF={a-r}$ cm, $CD={b-r}$ cm"],
               cm)

def PRF(stem, steps_):
    return Q(f"Prove that {stem}", "; ".join(f"{s} ({m})" for s, m in steps_) + ".", "+".join(str(m) for _, m in steps_))
P = {
 1: PRF("the tangent at any point of a circle is perpendicular to the radius through the point of contact.", [("Let the tangent $XY$ touch the circle with centre $O$ at $P$, and take any other point $Q$ on $XY$", 1), ("$Q$ lies outside the circle (a tangent meets the circle only at $P$), so $OQ>OP$", 1), ("This holds for every point $Q\\neq P$ on $XY$, so $OP$ is the shortest distance from $O$ to the line $XY$", 2), ("The shortest distance is the perpendicular, so $OP\\perp XY$", 1)]),
 2: PRF("the lengths of the tangents drawn from an external point to a circle are equal.", [("Let $PA$ and $PB$ be tangents from $P$ to the circle with centre $O$; join $OA$, $OB$, $OP$", 1), ("$\\angle OAP=\\angle OBP=90^\\circ$ (radius $\\perp$ tangent)", 1), ("In $\\triangle OAP$ and $\\triangle OBP$: $OA=OB$ (radii), $OP$ common, right angles equal", 1), ("$\\triangle OAP\\cong\\triangle OBP$ (RHS)", 1), ("Hence $PA=PB$ (CPCT)", 1)]),
 3: PRF("a parallelogram circumscribing a circle is a rhombus.", [("Let the circle touch $AB$, $BC$, $CD$, $DA$ at $P$, $Q$, $R$, $S$; tangents from a point are equal: $AP=AS$, $BP=BQ$, $CR=CQ$, $DR=DS$", 2), ("Add: $AB+CD=AD+BC$", 1), ("In a parallelogram $AB=CD$ and $AD=BC$, so $2AB=2AD$", 1), ("$AB=AD$, so all four sides are equal and $ABCD$ is a rhombus", 1)]),
 4: PRF("if a quadrilateral $ABCD$ is drawn to circumscribe a circle, then $AB+CD=AD+BC$.", [("Let the circle touch $AB$, $BC$, $CD$, $DA$ at $P$, $Q$, $R$, $S$", 1), ("Tangents from an external point are equal: $AP=AS$, $BP=BQ$, $CR=CQ$, $DR=DS$", 2), ("Adding: $(AP+BP)+(CR+DR)=(AS+DS)+(BQ+CQ)$", 1), ("So $AB+CD=AD+BC$", 1)]),
 5: PRF("the tangents drawn at the ends of a diameter of a circle are parallel.", [("Let $AB$ be a diameter and $PQ$, $RS$ the tangents at $A$ and $B$", 1), ("$OA\\perp PQ$ and $OB\\perp RS$ (radius $\\perp$ tangent), so $\\angle PAB=90^\\circ$ and $\\angle ABS=90^\\circ$", 2), ("These are alternate interior angles with transversal $AB$ and they are equal", 1), ("Hence $PQ\\parallel RS$", 1)]),
 6: PRF("if $PA$ and $PB$ are tangents from $P$ to a circle with centre $O$, then $\\angle APB+\\angle AOB=180^\\circ$.", [("$OA\\perp PA$ and $OB\\perp PB$, so $\\angle OAP=\\angle OBP=90^\\circ$", 2), ("In quadrilateral $OAPB$ the angle sum is $360^\\circ$", 1), ("$\\angle APB+\\angle AOB=360^\\circ-90^\\circ-90^\\circ=180^\\circ$", 2)]),
 7: PRF("if $PA$ and $PB$ are tangents from $P$ to a circle with centre $O$, then $OP$ is the perpendicular bisector of $AB$.", [("$PA=PB$ and $OA=OB$, so $P$ and $O$ both lie on the perpendicular bisector of $AB$ (points equidistant from $A$ and $B$)", 2), ("Alternatively, let $OP$ meet $AB$ at $M$; $\\triangle PAM\\cong\\triangle PBM$ (SAS, since $\\angle APM=\\angle BPM$)", 2), ("So $AM=MB$ and $\\angle PMA=\\angle PMB=90^\\circ$", 1)]),
 8: PRF("in two concentric circles, a chord of the larger circle which touches the smaller circle is bisected at the point of contact.", [("Let the chord $AB$ of the larger circle touch the smaller circle at $M$; join $OM$", 1), ("$OM\\perp AB$ (radius of the smaller circle $\\perp$ tangent $AB$)", 2), ("A perpendicular from the centre of the larger circle to a chord bisects the chord", 1), ("Hence $AM=MB$", 1)]),
 9: PRF("if a circle touches the sides $BC$, $CA$, $AB$ of $\\triangle ABC$ at $D$, $E$, $F$, then $AF+BD+CE=\\frac12(AB+BC+CA)$.", [("Tangents from an external point are equal: $AF=AE$, $BF=BD$, $CD=CE$", 2), ("Perimeter $=AB+BC+CA=(AF+FB)+(BD+DC)+(CE+EA)$", 1), ("$=2(AF+BD+CE)$ using the equalities above", 1), ("Hence $AF+BD+CE=\\frac12(AB+BC+CA)$", 1)]),
 10: PRF("if $PA$ and $PB$ are tangents from $P$ and a third tangent touches the circle at $C$ on the minor arc $AB$, meeting $PA$ at $X$ and $PB$ at $Y$, then $XY=AX+BY$ and the perimeter of $\\triangle PXY$ is $2PA$.", [("$XA=XC$ (tangents from $X$) and $YB=YC$ (tangents from $Y$)", 2), ("$XY=XC+CY$ since $C$ lies on $XY$, so $XY=AX+BY$", 1), ("Perimeter of $\\triangle PXY=PX+XY+YP=PX+XA+BY+YP$", 1), ("$=PA+PB=2PA$ because $PA=PB$", 1)]),
 11: PRF("in a right triangle $ABC$ with $\\angle B=90^\\circ$, the radius of the incircle is $r=\\frac{AB+BC-AC}{2}$.", [("Let the incircle touch $AB$, $BC$, $CA$ at $F$, $D$, $E$ and let the centre be $O$; $OF\\perp AB$, $OD\\perp BC$", 1), ("$BFOD$ has three right angles and $OF=OD=r$, so it is a square: $BF=BD=r$", 2), ("$AE=AF=AB-r$ and $CE=CD=BC-r$ (equal tangents)", 1), ("$AC=AE+EC=AB+BC-2r$, so $r=\\frac{AB+BC-AC}{2}$", 1)]),
 12: PRF("if tangents at $A$ and $B$ of a circle with centre $O$ meet at $P$, then $\\angle PAB=\\frac12\\angle AOB$.", [("$PA=PB$ (equal tangents), so $\\angle PAB=\\angle PBA$", 1), ("$\\angle APB+\\angle AOB=180^\\circ$ (quadrilateral $OAPB$ with two right angles)", 2), ("In $\\triangle PAB$: $2\\angle PAB=180^\\circ-\\angle APB=\\angle AOB$", 1), ("Hence $\\angle PAB=\\frac12\\angle AOB$", 1)]),
}

# ================= EASY =================
eA = [[MC(tlen(a, c)) for a, b, c in LO[:6]],
      [MC(rad(b, c)) for a, b, c in LO[1:6]],
      [MC(opd(a, b)) for a, b, c in LO[6:11]],
      [MC(quadp(a, b)) for a, b, c in LO[:5]],
      [MC(angpa(x)) for x in (110, 100, 130, 140, 70)],
      [MC(aop(x)) for x in (30, 35, 40, 55, 25)],
      CE]
eB = ([SQ(tlen(b, c), 2) for a, b, c in LO[7:11]] + [SQ(opd(b, a), 2) for a, b, c in LO[:4]] + [SQ(angpa(x), 2) for x in (120, 90, 150, 80)])
eC = ([SQ(quadp(a, b), 3) for a, b, c in LO[5:11]] + [SQ(quada(a, b), 3) for a, b, c in LO[:6]] + [SQ(aop(x), 3) for x in (20, 45, 50, 60, 15, 65)])
eD = [SQ(dcomp(a, c), 5) for a, b, c in LO[:6]] + [SQ(conc(c, a), 5) for a, b, c in LO[6:11]] + [SQ(conc(c, b), 5) for a, b, c in LO[1:2]]

# ================= NCERT =================
nA = [CN,
      [MC(tlen(a, c)) for a, b, c in MID[:5]],
      [MC(circq(*p)) for p in ((9, 11, 7), (12, 10, 8), (14, 9, 11), (8, 13, 10), (15, 12, 9))],
      [MC(oab(y)) for y in (60, 70, 80, 90, 100)],
      [MC(opd(a, b)) for a, b, c in MID[5:10]],
      [MC(inrad(*p)) for p in ((6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20))],
      [MC(eqt(*p)) for p in ((3, 5, 2, 9), (4, 1, 3, 6), (5, 2, 3, 12), (2, 7, 1, 12), (6, 4, 4, 14))]]
nB = ([SQ(eqt(*p), 2) for p in ((3, 4, 2, 9), (5, 1, 3, 9), (4, 3, 2, 11), (7, 2, 4, 14))] + [SQ(oab(y), 2) for y in (40, 50, 110, 120)] + [SQ(circq(*p), 2) for p in ((13, 9, 8), (11, 14, 12), (10, 6, 9), (16, 12, 7))])
nC = ([SQ(incirc(*p), 3) for p in ((7, 9, 12), (10, 12, 14), (11, 13, 12), (9, 15, 10), (13, 14, 15), (8, 9, 11))]
      + [SQ(inrad(*p), 3) for p in ((20, 21, 29), (24, 32, 40), (15, 36, 39), (21, 28, 35), (10, 24, 26), (27, 36, 45))] + [SQ(conc(a, b), 3) for a, b, c in ((5, 3, 4), (13, 5, 12), (10, 6, 8), (17, 8, 15), (25, 7, 24), (26, 10, 24))])
nD = [P[k] for k in (1, 2, 3, 4, 5, 9)] + [SQ(dcomp2(*p), 5) for p in ((6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20), (7, 24, 25))]

# ================= MEDIUM =================
mA = [[MC(rad(a, c)) for a, b, c in MID[:5]],
      [MC(quadp(b, a)) for a, b, c in MID[:5]],
      [MC(quada(b, a)) for a, b, c in MID[5:10]],
      [MC(conc(c, a)) for a, b, c in MID[10:15]],
      [MC(inrad(*p)) for p in MID[15:20]],
      [MC(eqt(*p)) for p in ((8, 3, 5, 18), (6, 5, 4, 15), (9, 2, 7, 14), (11, 1, 8, 16), (7, 3, 3, 23))],
      [MC(apb_from_pab(x)) for x in (35, 40, 50, 65, 25)],
      CM]
mB = ([SQ(apb_from_pab(x), 2) for x in (30, 55, 20, 70)] + [SQ(oab(y), 2) for y in (36, 72, 84, 96)] + [SQ(tlen(b, c), 2) for a, b, c in MID[10:14]])
mC = ([SQ(eqt(*p), 3) for p in ((9, 4, 5, 20), (7, 2, 4, 14), (10, 3, 6, 19), (12, 5, 9, 20), (8, 7, 5, 22), (13, 6, 9, 14))] + [SQ(circq(*p), 3) for p in ((18, 15, 12), (21, 17, 14), (25, 19, 16), (30, 24, 13), (22, 18, 20), (26, 20, 15))]
      + [SQ(quada(b, a), 3) for a, b, c in MID[:6]])
mD = [SQ(dcomp(a, c), 5) for a, b, c in MID[10:16]] + [P[k] for k in (6, 7, 8)] + [SQ(dcomp2(*p), 5) for p in MID[16:19]]

# ================= HARD =================
HC = [(30, 40, 50), (14, 48, 50), (24, 32, 40), (21, 28, 35), (36, 48, 60), (45, 60, 75), (21, 72, 75), (27, 36, 45), (33, 44, 55), (48, 64, 80)]
hA = [[MC(chord_contact(a, b, c)) for a, b, c in HC[:5]],
      [MC(third_tangent(x)) for x in (7, 11, 13, 19, 24)],
      [MC(eqt(*p)) for p in ((15, 4, 8, 25), (12, 7, 5, 28), (17, 3, 9, 27), (14, 6, 8, 30), (19, 2, 11, 18))],
      [MC(conc(c, a)) for a, b, c in HI[:5]],
      [MC(inrad(*p)) for p in HI[5:10]],
      [MC(tlen(b, c)) for a, b, c in HI[10:15]],
      CH]
hB = ([SQ(chord_contact(b, a, c), 2) for a, b, c in HC[5:9]] + [SQ(third_tangent(x), 2) for x in (9, 16, 21, 28)] + [SQ(conc(c, b), 2) for a, b, c in HI[15:19]])
hC = ([SQ(chord_contact(a, b, c), 3) for a, b, c in HC[:3] + HC[5:8]] + [SQ(inrad(*p), 3) for p in HI[10:16]] + [SQ(eqt(*p), 3) for p in ((21, 5, 13, 29), (18, 7, 11, 35), (16, 9, 9, 30), (23, 4, 15, 20), (20, 8, 12, 24), (25, 3, 17, 19))])
hD = [P[k] for k in (10, 11, 12)] + [SQ(chord_contact(a, b, c), 5) for a, b, c in HC[3:6]] + [SQ(chord_contact(b, a, c), 5) for a, b, c in HC[6:9]] + [SQ(dcomp2(*p), 5) for p in HI[16:19]]

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
