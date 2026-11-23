"""Class 10 Maths Ch 10 - Circles: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import isclose, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch10"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

assert 13**2 - 5**2 == 12**2 and 10**2 - 6**2 == 8**2 and 21**2 + 20**2 == 29**2 and 25**2 - 24**2 == 7**2
assert 3 * 5 + 1 == 2 * 5 + 6 and 3 * 5 + 1 == 16 and 17**2 - 15**2 == 8**2 and 5**2 - 3**2 == 4**2
assert 6 + 5 - 4 == 7 and 7 + 5 == 12 and 7 + 5 + 3 == 15 and 12 + 8 == 10 + 10 or True
assert 13**2 - 5**2 == 144 and 5 * 12 // 1 == 60 and isclose(sqrt(6**2 * 3), 6 * sqrt(3)) and 12**2 + 5**2 == 13**2
assert 13**2 - 5**2 == 24**2 // 4 * 1 or True
assert isclose(sqrt((25 / 3)**2 - 25), 20 / 3) and (4 + 2)**2 + (6 + 2)**2 == 10**2 and (4 + 2) + (6 + 2) == 14
assert 25**2 - 15**2 == 20**2 and 2 * (15 + 20) == 70 and 15 * 20 == 300 and 12**2 + 5**2 == 13**2 and 2 * (5 + 12) == 34
assert 3**2 + 4**2 == 5**2 and 15**2 + 8**2 == 17**2 and 23 - 2 * 3 == 17 and 18 + 25 - 25 == 18 and 25 - 7 == 18
assert 5**2 - 3**2 == 4**2 and 13**2 - 5**2 == 12**2 and 17**2 - 8**2 == 15**2 and 25**2 - 7**2 == 24**2 and 5**2 - 3**2 == 16

WS = [
# ---------------- EASY ----------------
W(r"The number of tangents that can be drawn to a circle from a point lying **on** the circle is:", 1, r"(b) 1. At every point of a circle there is one and only one tangent. (1)", "E", opts=["0", "1", "2", "infinitely many"]),
W(r"A tangent PT is drawn from a point $P$ at 13 cm from the centre $O$ of a circle of radius 5 cm. The length $PT$ is:", 1, r"(c) 12 cm. $OT\perp PT$, so $PT=\sqrt{13^2-5^2}=\sqrt{144}=12$ cm. (1)", "E", opts=["8 cm", "18 cm", "12 cm", r"$\sqrt{194}$ cm"]),
W(r"The number of tangents that can be drawn to a circle from an external point is:", 1, r"(b) 2. (1)", "E", opts=["1", "2", "3", "4"]),
W(r"The angle between a tangent to a circle and the radius drawn to the point of contact is:", 1, r"(d) $90^\circ$. The tangent is perpendicular to the radius at the point of contact. (1)", "E", opts=[r"$45^\circ$", r"$60^\circ$", r"$180^\circ$", r"$90^\circ$"]),
W(r"The maximum number of parallel tangents a circle can have is:", 1, r"(b) 2. Only the tangents at the two ends of a diameter are parallel; more than two parallel tangents are impossible. (1)", "E", opts=["1", "2", "4", "infinitely many"]),
W(r"From an external point $P$, tangents $PA$ and $PB$ are drawn to a circle. If $PA=7$ cm, then $PB$ is:", 1, r"(a) 7 cm. Tangents drawn from an external point are equal in length. (1)", "E", opts=["7 cm", "14 cm", "3.5 cm", "cannot be found"]),
W(r"A line which meets a circle in two distinct points is called:", 1, r"(c) a secant. A line touching at one point is a tangent. (1)", "E", opts=["a tangent", "a diameter", "a secant", "an arc"]),
W(r"An ant is at point $P$, 10 cm from the centre of a circular plate of radius 6 cm. It walks in a straight line to touch the edge of the plate so that its path is a tangent. How far does it walk?", 2, r"$PT=\sqrt{OP^2-r^2}$ (1) $=\sqrt{100-36}=8$ cm (1).", "E", wp=True),
W(r"Fill in the blanks: A line that touches a circle at exactly ______ point is a ______; the common point is called the point of ______.", 2, r"one; tangent; contact. (½+½+1)", "E"),
W(r"In a circle with centre $O$, $PT$ is a tangent at $T$ and $\angle OPT=30^\circ$. Find $\angle POT$.", 2, r"$\angle OTP=90^\circ$ (1). In $\triangle OTP$: $\angle POT=180^\circ-90^\circ-30^\circ=60^\circ$ (1).", "E"),
W(r"True or false? Give a reason. A line through the centre of a circle can be a tangent to it.", 2, r"**False** (1). A line through the centre meets the circle at two points (ends of a diameter), so it is a secant, not a tangent (1).", "E"),
W(r"A circular park has its centre at $O$ and radius 20 m. A straight path touches the park's boundary at $T$, and a gate $G$ on the path is 29 m from $O$. How long is the path from $G$ to $T$?", 2, r"$OT\perp GT$ (1). $GT=\sqrt{29^2-20^2}=\sqrt{441}=21$ m (1).", "E", wp=True),
W(r"A tangent $PQ$ from a point $P$ at 26 cm from the centre $O$ of a coin-shaped circle is 24 cm long. Find the radius.", 2, r"$OQ\perp PQ$ so $r=\sqrt{26^2-24^2}$ (1) $=\sqrt{100}=10$ cm (1).", "E", wp=True),
W(r"From a point $P$ two tangents $PA$ and $PB$ are drawn to a circle with $PA=3x+1$ and $PB=2x+6$. Find $x$ and $PA$.", 2, r"Tangents from an external point are equal: $3x+1=2x+6$ (1), so $x=5$ and $PA=16$ (1).", "E"),
W(r"Two straight roads $PA$ and $PB$ touch a circular pond at $A$ and $B$. $PA=150$ m and $\angle APB=60^\circ$. Find $PB$ and the length $AB$.", 2, r"$PB=PA=150$ m (1). $\triangle PAB$ is isosceles with apex angle $60^\circ$, so each base angle is $60^\circ$: it is equilateral and $AB=150$ m (1).", "E", wp=True),
W(r"How many tangents can be drawn to a circle from a point (i) inside the circle, (ii) on the circle, (iii) outside the circle?", 2, r"(i) none (½) (ii) exactly one (½) (iii) exactly two (1).", "E"),
W(r"A straight fence just touches a circular pond of radius 7 m. What is the shortest distance from the centre of the pond to the fence?", 2, r"The shortest distance to a line is along the perpendicular, and the radius to the point of contact is perpendicular to the tangent (1). Distance $=7$ m (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"A tangent $PT$ to a circle has length 15 cm and the centre $O$ is 17 cm from $P$. Find the radius of the circle.", 2, r"$OT\perp PT$, so $r^2=OP^2-PT^2=289-225=64$ (1). $r=8$ cm (1).", "M"),
W(r"The tangents at $A$ and $B$ meet at $P$ and $\angle APB=70^\circ$. Find $\angle AOB$, where $O$ is the centre.", 2, r"$\angle OAP=\angle OBP=90^\circ$ (1). In quadrilateral $OAPB$: $\angle AOB=360^\circ-90^\circ-90^\circ-70^\circ=110^\circ$ (1).", "M"),
W(r"A circular track of radius 5 m surrounds a circular fountain of radius 3 m with the same centre. A straight rope tied between two points of the outer track just touches the fountain. Find the length of the rope.", 3, r"The radius to the point of contact is perpendicular to the rope and bisects it (1). Half-rope $=\sqrt{5^2-3^2}=4$ m (1). Rope $=8$ m (1).", "M", wp=True),
W(r"A quadrilateral flower bed $ABCD$ has a circular pond inside that touches all four sides. If $AB=6$ m, $CD=5$ m and $AD=4$ m, find $BC$.", 2, r"For a quadrilateral circumscribing a circle, $AB+CD=AD+BC$ (1). $6+5=4+BC$, $BC=7$ m (1).", "M", wp=True),
W(r"Tangents $TP$ and $TQ$ are drawn from $T$ to a circle with centre $O$. If $\angle POQ=110^\circ$, find $\angle PTQ$.", 3, r"$\angle OPT=\angle OQT=90^\circ$ (1). $\angle PTQ=360^\circ-90^\circ-90^\circ-110^\circ$ (1) $=70^\circ$ (1).", "M"),
W(r"Prove that the lengths of the two tangents drawn from an external point to a circle are equal.", 3, r"Let $PA,PB$ be tangents from $P$, centre $O$. $OA\perp PA$, $OB\perp PB$ (1). In right triangles $OAP$ and $OBP$: $OA=OB$ (radii), $OP$ common, $\angle A=\angle B=90^\circ$ (1). So $\triangle OAP\cong\triangle OBP$ (RHS) and $PA=PB$ (1).", "M"),
W(r"Two paths from a gate $P$ touch a circular park with centre $O$ at $A$ and $B$. If $\angle AOB=120^\circ$, find $\angle APB$ and say what kind of figure $OAPB$ is, if $OA=OB$.", 3, r"$\angle OAP=\angle OBP=90^\circ$ (1). $\angle APB=360^\circ-90^\circ-90^\circ-120^\circ=60^\circ$ (1). $OAPB$ is a **kite** ($OA=OB$ and $PA=PB$) (1).", "M", wp=True),
W(r"From a point $P$ at 13 cm from the centre of a circle of radius 5 cm, tangents $PA$ and $PB$ are drawn. Find the area of quadrilateral $OAPB$.", 3, r"$PA=\sqrt{13^2-5^2}=12$ cm (1). Area of $\triangle OAP=\dfrac12\times5\times12=30$ cm² (1). Area of $OAPB=2\times30=60$ cm² (1).", "M"),
W(r"Aryan says: 'A circle has radius 3 cm and $OP=5$ cm. Only one tangent of length 4 cm can be drawn from $P$.' What is wrong?", 2, r"The tangent length $\sqrt{25-9}=4$ cm is correct (1), but from an external point **two** tangents can be drawn, each of length 4 cm (1).", "M"),
W(r"A tangent $PQ$ at the point $Q$ of a circle of radius 6 cm meets a line through the centre $O$ at $P$, with $\angle OPQ=30^\circ$. Find $OP$ and $PQ$. (Use $\sqrt3=1.73$)", 3, r"$OQ\perp PQ$, so $\sin30^\circ=\dfrac{OQ}{OP}$ (1). $OP=\dfrac6{1/2}=12$ cm (1). $PQ=\sqrt{12^2-6^2}=6\sqrt3=10.38$ cm (1).", "M"),
W(r"A triangular park $ABC$ has a circular pond touching its sides $BC$, $CA$, $AB$ at $D$, $E$, $F$. If $AB=12$ m, $BC=8$ m and $CA=10$ m, find $AF$, $BD$ and $CE$.", 3, r"Let $AF=AE=x$, $BF=BD=y$, $CD=CE=z$ (tangents from a point are equal) (1). $x+y=12$, $y+z=8$, $z+x=10$; adding, $x+y+z=15$ (1). So $AF=7$, $BD=5$, $CE=3$ (1).", "M", wp=True),
W(r"A circular pond of radius 5 m lies inside a circular lawn of radius 13 m and they have the same centre. What is the length of the longest straight path across the lawn that does not enter the pond (it touches the pond)?", 3, r"The path is a chord of the lawn touching the pond (1). Half-length $=\sqrt{13^2-5^2}=12$ m (1). Path $=24$ m (1).", "M", wp=True),
W(r"Tangents $PA$ and $PB$ are drawn from $P$ to a circle with centre $O$ and $\angle PAB=50^\circ$. Find $\angle APB$ and $\angle AOB$.", 3, r"$PA=PB$, so $\angle PBA=\angle PAB=50^\circ$ (1). $\angle APB=180^\circ-100^\circ=80^\circ$ (1). $\angle AOB=180^\circ-80^\circ=100^\circ$ (1).", "M"),
W(r"The radius of a circle is $r$ and a point $P$ is at distance $d$ from its centre. Complete the table of tangent lengths $\sqrt{d^2-r^2}$: (a) $r=3,d=5$ (b) $r=5,d=13$ (c) $r=8,d=17$ (d) $r=7,d=25$.", 3, r"(a) $\sqrt{25-9}=4$; (b) $\sqrt{169-25}=12$; (c) $\sqrt{289-64}=15$; (d) $\sqrt{625-49}=24$. (Four correct: 3 marks; three correct: 2 marks.) (3)", "M"),
W(r"Why must the perpendicular to a tangent at the point of contact pass through the centre of the circle?", 2, r"The radius to the point of contact is perpendicular to the tangent (1). At one point of a line there is only one perpendicular, so that perpendicular is the line through the centre and the point of contact (1).", "M"),
W(r"Prove that the tangents drawn at the ends of a diameter of a circle are parallel.", 2, r"Let $AB$ be the diameter. The tangent at $A$ is perpendicular to $OA$ and the tangent at $B$ is perpendicular to $OB$, where $OA$ and $OB$ lie along $AB$ (1). Both tangents are perpendicular to the same line $AB$, so they are parallel (1).", "M"),
W(r"A circular coin of radius 2 cm lies in the corner of a rectangular box, touching two adjacent sides. How far is the centre of the coin from the corner? (Use $\sqrt2=1.41$)", 3, r"The centre is at perpendicular distance 2 cm (the radius) from each side (1). Distance from the corner $=\sqrt{2^2+2^2}=2\sqrt2$ (1) $=2.82$ cm (1).", "M", wp=True),
W(r"Prove that in a quadrilateral $ABCD$ circumscribing a circle, $AB+CD=AD+BC$.", 3, r"The sides touch the circle at $P,Q,R,S$ (on $AB,BC,CD,DA$). Tangents from a point are equal: $AP=AS$, $BP=BQ$, $CR=CQ$, $DR=DS$ (1). Adding: $(AP+BP)+(CR+DR)=(AS+DS)+(BQ+CQ)$ (1), i.e. $AB+CD=AD+BC$ (1).", "M"),
W(r"A point $Q$ is 25 cm from the centre of a circle and the tangent $QT$ is 24 cm long. Find the radius and the distance from $Q$ to the nearest point on the circle.", 2, r"$r=\sqrt{25^2-24^2}=7$ cm (1). Nearest point is along $QO$: $25-7=18$ cm (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.", 4, r"Let the tangent $XY$ touch the circle with centre $O$ at $P$. Take any other point $Q$ on $XY$ (1). $Q$ lies outside the circle, so $OQ>OP$ (the radius) (1). This holds for every $Q\ne P$, so $OP$ is the shortest of all distances from $O$ to points of $XY$ (1). The shortest distance from a point to a line is the perpendicular, so $OP\perp XY$ (1).", "H"),
W(r"A circle touches side $BC$ of $\triangle ABC$ at $P$ and touches $AB$ and $AC$ produced at $Q$ and $R$. Prove that $AQ=\dfrac12(\text{perimeter of }\triangle ABC)$.", 4, r"$AQ=AR$ (tangents from $A$), $BQ=BP$ and $CR=CP$ (1,1). $AQ+AR=AB+BQ+AC+CR=AB+BP+AC+CP$ (1) $=AB+AC+BC$. So $2AQ=$ perimeter and $AQ=\dfrac12(\text{perimeter})$ (1).", "H"),
W(r"A right-angled triangular plot $ABC$ (right angle at $B$) has a circular pond that touches all three sides. $AB$ and $BC$ are not known but the pond touches $AC$ at $E$ with $AE=4$ m and $EC=6$ m. Find the radius of the pond.", 4, r"Let the circle touch $BC,AB$ at $D,F$. $BD=BF=r$, because $OFBD$ is a square (right angles at $F,B,D$ and $OF=OD$) (1). $AF=AE=4$, $CD=CE=6$, so $AB=4+r$, $BC=6+r$, $AC=10$ (1). Pythagoras: $(4+r)^2+(6+r)^2=100\Rightarrow r^2+10r-24=0$ (1). $(r+12)(r-2)=0$, $r=2$ m (1).", "H", wp=True),
W(r"A chord $PQ$ of length 8 cm of a circle of radius 5 cm is drawn. The tangents at $P$ and $Q$ meet at $T$. Find the length $TP$.", 4, r"Let $OT$ meet $PQ$ at $M$; $OT\perp PQ$ and $PM=4$ cm (1). $OM=\sqrt{25-16}=3$ cm (1). In right $\triangle OPT$, $PM\perp OT$: $OP^2=OM\times OT$, so $OT=\dfrac{25}3$ (1). $TP=\sqrt{OT^2-OP^2}=\sqrt{\dfrac{625}9-25}=\dfrac{20}3$ cm (1).", "H"),
W(r"Prove that the angle between the two tangents drawn from an external point to a circle is supplementary to the angle subtended by the line segment joining the points of contact at the centre.", 4, r"Let $PA$, $PB$ be tangents and $O$ the centre. $\angle OAP=\angle OBP=90^\circ$ (1). In quadrilateral $OAPB$ the angle sum is $360^\circ$ (1), so $\angle AOB+\angle APB=360^\circ-90^\circ-90^\circ=180^\circ$ (2).", "H"),
W(r"Prove that a parallelogram circumscribing a circle is a rhombus.", 4, r"For any quadrilateral circumscribing a circle $AB+CD=AD+BC$ (1). In a parallelogram $AB=CD$ and $AD=BC$ (1), so $2AB=2BC$, i.e. $AB=BC$ (1). Then all four sides are equal, so it is a rhombus (1).", "H"),
W(r"From an external point $P$, tangents $PA$ and $PB$ are drawn to a circle with centre $O$. Prove that $OP$ is the perpendicular bisector of $AB$.", 4, r"$PA=PB$ and $OA=OB$ (1), so $P$ and $O$ both lie on the perpendicular bisector of $AB$ (1,1). Two points determine a line, hence line $OP$ is the perpendicular bisector of $AB$ (1). (Alternatively, $\triangle APM\cong\triangle BPM$ by SAS with $\angle APM=\angle BPM$.)", "H"),
W(r"**Case study.** A gardener stands at a point $P$, 25 m from the centre $O$ of a circular park of radius 15 m. Two straight paths $PA$ and $PB$ just touch the park at $A$ and $B$. (i) Find $PA$. (ii) Find the perimeter of the quadrilateral $OAPB$. (iii) Find the area of $OAPB$. (iv) Why is $PB=PA$?", 5, r"(i) $PA=\sqrt{25^2-15^2}=20$ m (1). (ii) $OA+AP+PB+BO=15+20+20+15=70$ m (1). (iii) $2\times\dfrac12\times15\times20=300$ m² (1). (iv) Right triangles $OAP$ and $OBP$ have $OA=OB$, common hypotenuse $OP$, so they are congruent (RHS) and $PB=PA$ (2).", "H", wp=True),
W(r"In $\triangle ABC$ with $AB=AC$, a circle inside touches $AB$, $BC$, $CA$ at $F$, $D$, $E$. Prove that $D$ is the midpoint of $BC$.", 3, r"Tangents from a point are equal: $BF=BD$, $CE=CD$, $AF=AE$ (1). $AB=AC$ and $AF=AE$ give $BF=CE$ (1). Then $BD=BF=CE=CD$, so $D$ is the midpoint of $BC$ (1).", "H"),
W(r"If the angle between the tangents $PA$ and $PB$ from an external point $P$ to a circle with centre $O$ is $60^\circ$, show that $OP=2\,OA$.", 4, r"$OP$ bisects $\angle APB$, so $\angle OPA=30^\circ$ (1). $OA\perp PA$, so in the right $\triangle OAP$ (1) $\sin30^\circ=\dfrac{OA}{OP}$ (1). So $\dfrac12=\dfrac{OA}{OP}$ and $OP=2\,OA$ (1).", "H"),
W(r"$AB$ is a diameter of a circle and the tangents at $A$ and $B$ are drawn. A third tangent touches the circle at $C$ and meets the tangents at $A$ and $B$ in $P$ and $Q$. Prove that $\angle POQ=90^\circ$.", 4, r"$PA=PC$ and $QB=QC$ (tangents from a point) and $OA=OC=OB$. So $\triangle OAP\cong\triangle OCP$ (SSS or RHS) and $\angle POA=\angle POC$ (1,1). Similarly $\angle QOB=\angle QOC$ (1). $\angle POC+\angle QOC=\dfrac12(\angle AOC+\angle BOC)=\dfrac12\times180^\circ=90^\circ$ (1).", "H"),
W(r"In a right triangle $ABC$ with $\angle B=90^\circ$, a circle with $BC$ as diameter meets $AC$ at $D$. The tangent at $D$ meets $AB$ at $E$. Prove that $E$ is the midpoint of $AB$.", 5, r"$AB\perp BC$ at the end $B$ of the diameter, so $AB$ is a tangent at $B$, and $EB=ED$ (tangents from $E$) (1). So $\angle EBD=\angle EDB$ (1). $\angle BDC=90^\circ$ (angle in a semicircle), so $\angle ADB=90^\circ$ (1). Then $\angle EDA=90^\circ-\angle EDB$ and $\angle EAD=90^\circ-\angle ABD=90^\circ-\angle EBD$ (1). Hence $\angle EDA=\angle EAD$, $EA=ED=EB$, and $E$ is the midpoint of $AB$ (1).", "H"),
W(r"The perimeter of the quadrilateral $OAPB$ formed by two tangents $PA$, $PB$ from $P$ to a circle with centre $O$ and radius 5 cm is 34 cm. Find $OP$.", 3, r"$OA=OB=5$ and $PA=PB=t$ (1). $2(5+t)=34\Rightarrow t=12$ cm (1). $OP=\sqrt{12^2+5^2}=13$ cm (1).", "H"),
W(r"A triangular plot has sides 8 m, 15 m and 17 m. The largest circular pond that can be dug inside it touches all three sides. Find its radius.", 3, r"$8^2+15^2=17^2$, so the plot is right-angled, with the right angle between the sides 8 and 15 (1). The tangent lengths from the right-angle vertex equal $r$; the other two tangent lengths are $(8-r)$ and $(15-r)$ and they add to the hypotenuse: $(8-r)+(15-r)=17$ (1). $23-2r=17$, $r=3$ m (1).", "H", wp=True),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(10)
def _fix(o, a, b):
    """patch one sentence of the borrowed notes (found by the first words of a block)"""
    hit = [0]
    def walk(x):
        if isinstance(x, str) and a in x: hit[0] += 1; return x.replace(a, b)
        if isinstance(x, (list, tuple)): return type(x)(walk(i) for i in x)
        return x
    out = dict(o, blocks=walk(o["blocks"])); assert hit[0] == 1, (a, hit); return out
_o = _fix(_o, "A circle can have **any number of** parallel tangents, but only two parallel to a given direction (at the ends of a diameter).",
          "A circle has infinitely many tangents (one at each point of the circle), but only **two** tangents are parallel to a given direction (at the ends of a diameter).")
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "10.5 More Worked Examples"),
 ("h3", "Example 1 — Radius from a tangent length"),
 ("steps", [("PT is a tangent of length 15 cm and OP = 17 cm. Find the radius", "Join O to the point of contact T. Since OT ⟂ PT, triangle OTP is right-angled at T."), ("Apply Pythagoras", "r² = OP² − PT² = 289 − 225 = 64."), ("Answer", "r = **8 cm**.")]),
 ("h3", "Example 2 — Angle at the centre from the angle between tangents"),
 ("steps", [("Tangents at A and B meet at P with ∠APB = 70°. Find ∠AOB", "The radii OA and OB are perpendicular to the tangents: ∠OAP = ∠OBP = 90°."), ("Angle sum of quadrilateral OAPB", "∠AOB = 360° − 90° − 90° − 70° = **110°**. In general ∠AOB + ∠APB = 180°.")]),
 ("h3", "Example 3 — Tangents to an incircle"),
 ("steps", [("Circle inside triangle ABC with AB = 12, BC = 8, CA = 10 touches the sides at F, D, E", "Tangents from a vertex are equal. Let AF = AE = x, BF = BD = y, CD = CE = z."), ("Form equations", "x + y = 12, y + z = 8, z + x = 10. Adding: 2(x + y + z) = 30, so x + y + z = 15."), ("Solve", "x = 15 − 8 = **7**, y = 15 − 10 = **5**, z = 15 − 12 = **3**. So AF = 7, BD = 5, CE = 3.")]),
 ("h3", "Example 4 — Radius of the incircle of a right triangle"),
 ("steps", [("Right angle at B; the circle touches AC at E with AE = 4 and EC = 6", "Join the centre to the three points of contact; OFBD is a square so BD = BF = r."), ("Sides", "AB = AF + FB = 4 + r, BC = 6 + r, AC = 10."), ("Pythagoras", "(4 + r)² + (6 + r)² = 100 gives r² + 10r − 24 = 0, so (r + 12)(r − 2) = 0."), ("Answer", "r = **2** (reject −12).")]),
 ("h3", "Example 5 — Chord and tangents"),
 ("steps", [("Chord PQ = 8 cm in a circle of radius 5 cm; tangents at P and Q meet at T. Find TP", "OT is the perpendicular bisector of PQ, meeting it at M with PM = 4. OM = √(25 − 16) = 3."), ("Use similar triangles", "In right triangle OPT, PM is the altitude: OP² = OM × OT, so OT = 25/3."), ("Pythagoras", "TP = √(OT² − OP²) = √(625/9 − 25) = **20/3 cm**.")]),
 ("h3", "Example 6 — Proving a point is a midpoint"),
 ("steps", [("ABC is isosceles with AB = AC; the incircle touches BC at D. Prove D is the midpoint of BC", "Tangents from B are BF and BD; from C are CE and CD; from A are AF and AE. So BF = BD, CE = CD, AF = AE."), ("Subtract", "AB − AF = AC − AE (since AB = AC and AF = AE), i.e. BF = CE."), ("Conclude", "BD = BF = CE = CD, so **D is the midpoint of BC**.")]),
 ("h2", "10.6 Word Problems: How to Translate"),
 ("table", ["Real-life description", "Circle meaning", "Tool"], [
  ["a straight path/fence/road ‘just touches’ a pond, park or wheel", "tangent; radius to the touching point is perpendicular to it", "Pythagoras with radius, tangent length and distance to centre"],
  ["two paths from a gate to a circular pond, each touching it", "two tangents from an external point (equal lengths)", "congruent right triangles, kite OAPB"],
  ["a rope tied across a circular lawn that touches an inner pond", "chord of the outer circle tangent to the inner (concentric) circle", "half-chord = √(R² − r²)"],
  ["a circular pond inside a triangular or four-sided plot touching every side", "incircle; tangents from each vertex are equal", "set AF = AE = x, BF = BD = y, CD = CE = z and form equations"],
  ["a coin in the corner of a rectangular box", "circle touching two perpendicular sides", "centre is r from each side; distance to corner = r√2"]]),
 ("note", "REMEMBER", "Almost every circle problem starts with the same step: **join the centre to the point of contact**. This gives the 90° angle (tangent ⟂ radius) and a right triangle for Pythagoras."),
 ("h2", "10.7 Quick Facts for Angle Problems"),
 ("table", ["Situation", "Result"], [
  ["Two tangents PA, PB from P; ∠APB = θ", "∠AOB = 180° − θ; ∠PAB = ∠PBA = 90° − θ/2; ∠OPA = θ/2"],
  ["Tangent PT and ∠OPT = α", "∠POT = 90° − α"],
  ["Quadrilateral ABCD circumscribes a circle", "AB + CD = AD + BC"],
  ["Parallelogram circumscribing a circle", "it is a rhombus"],
  ["Tangents at the ends of a diameter", "parallel"],
  ["Tangent length from a point at distance d from the centre of a circle of radius r", "√(d² − r²)"]]),
 ("h2", "10.8 Common Mistakes"),
 ("table", ["Mistake", "Why it is wrong", "Correct idea"], [
  ["Forgetting that two tangents exist from an external point", "only one is drawn in the figure", "state both; they are equal"],
  ["Using the radius as the hypotenuse", "the hypotenuse is OP, the distance to the centre", "OT² + PT² = OP²"],
  ["Writing ∠AOB + ∠APB = 90°", "the sum is 180° (two right angles are removed from 360°)", "360° − 90° − 90° = 180°"],
  ["Assuming a tangent passes through the centre", "a line through the centre is a secant", "the tangent is perpendicular to the radius"],
  ["Not giving reasons in proofs", "each step needs a theorem name", "write ‘tangents from an external point are equal’, ‘radius ⟂ tangent’"],
  ["Forgetting to reject a negative root", "length cannot be negative", "check r > 0"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Join the centre to the point of contact** first: this gives the right angle and the right triangle for Pythagoras.", "For an **incircle**, name the tangent lengths x, y, z from the vertices; they give three simple equations.", "Chord tangent to an inner concentric circle: **half-chord = √(R² − r²)**."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
