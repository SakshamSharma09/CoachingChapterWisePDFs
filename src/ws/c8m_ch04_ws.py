"""Class 8 Maths Ch 4 - Quadrilaterals: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch04"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

from math import isqrt
assert 8**2 + 15**2 == 17**2 and 12**2 + 5**2 == 13**2 and 6**2 + 8**2 == 10**2 and 24**2 + 7**2 == 25**2
assert isqrt(25**2 - 24**2) == 7 and isqrt(30**2 - 24**2) == 18 and 7 + 18 == 25 and 25 * 48 // 2 == 600
assert (2*36-10) + (3*36+5) + (36+25) + (4*36-20) == 360 and 36 * 10 == 360
assert (30 + 18) * 12 // 2 == 288 and 288 * 50 == 14400 and 52 * 120 == 6240 and 62 * 80 == 4960
assert 3*(75) + 135 == 360 and 24**2 + 7**2 == 25**2 and 12 * 16 // 2 == 96

WS = [
# ---------------- EASY ----------------
W("Three angles of a quadrilateral are $80^\\circ$, $100^\\circ$ and $90^\\circ$. The fourth angle is:", 1, "(b) $90^\\circ$. $360^\\circ-(80^\\circ+100^\\circ+90^\\circ)=90^\\circ$. (1)", "E", opts=["$80^\\circ$", "$90^\\circ$", "$100^\\circ$", "$110^\\circ$"]),
W("In a parallelogram one angle is $65^\\circ$. An angle adjacent to it is:", 1, "(b) $115^\\circ$. Adjacent angles of a parallelogram add up to $180^\\circ$: $180^\\circ-65^\\circ=115^\\circ$. (1)", "E", opts=["$65^\\circ$", "$115^\\circ$", "$125^\\circ$", "$25^\\circ$"]),
W("Which quadrilateral always has equal diagonals?", 1, "(b) Rectangle. Its diagonals are equal and bisect each other; those of a general parallelogram, rhombus and kite are not equal. (1)", "E", opts=["Rhombus", "Rectangle", "Kite", "Parallelogram"]),
W("A rhombus has each side 9 cm. Its perimeter is:", 1, "(c) 36 cm. $4\\times9=36$. (1)", "E", opts=["18 cm", "27 cm", "36 cm", "81 cm"]),
W("Which of these is **not** always a parallelogram?", 1, "(c) Trapezium. It has only one pair of parallel sides; rectangle, rhombus and square have two. (1)", "E", opts=["Rectangle", "Rhombus", "Trapezium", "Square"]),
W("The diagonals of a quadrilateral bisect each other at right angles and are **not** equal. The quadrilateral is a:", 1, "(b) rhombus. A square has equal diagonals and a kite's diagonals do not bisect each other. (1)", "E", opts=["Rectangle", "Rhombus", "Square", "Kite"]),
W("A kite has two pairs of equal sides. These equal sides are:", 1, "(b) adjacent (neighbouring) sides, e.g. $AB=AD$ and $CB=CD$. (1)", "E", opts=["opposite sides", "adjacent sides", "parallel sides", "all four sides"]),
W("The angles of a quadrilateral are in the ratio $3:4:5:6$. Find the angles.", 2, "$3x+4x+5x+6x=360^\\circ$, $18x=360^\\circ$, $x=20^\\circ$ (1). Angles: $60^\\circ,80^\\circ,100^\\circ,120^\\circ$ (1).", "E"),
W("A picture frame is shaped like a parallelogram and one of its angles is $72^\\circ$. Find its other three angles.", 2, "Opposite angle $=72^\\circ$ (1). The two other angles are $180^\\circ-72^\\circ=108^\\circ$ each (1).", "E", wp=True),
W("A rhombus-shaped tile has side 12 cm. Find the length of the border strip needed to go all round it.", 1, "Perimeter $=4\\times12=48$ cm (1).", "E", wp=True),
W("True or false (give a reason): every square is a rectangle.", 1, "**True.** A square has all four angles $90^\\circ$ and opposite sides equal, so it satisfies the definition of a rectangle (1).", "E"),
W("The angles of a quadrilateral are $x$, $2x$, $3x$ and $4x$. Find them.", 2, "$10x=360^\\circ$, $x=36^\\circ$ (1). Angles: $36^\\circ,72^\\circ,108^\\circ,144^\\circ$ (1).", "E"),
W("The diagonal $AC$ of a rectangle $ABCD$ is 10 cm. What is the length of the other diagonal $BD$? Why?", 1, "10 cm, because the diagonals of a rectangle are equal (1).", "E"),
W("A parallelogram-shaped field has sides 7 m and 4 m. How much fencing is needed to enclose it?", 2, "Opposite sides are equal, so perimeter $=2(7+4)$ (1) $=22$ m (1).", "E", wp=True),
W("A quadrilateral has all four sides equal but its angles are not right angles. Name it.", 1, "A **rhombus** (1).", "E"),
W("The diagonals of a parallelogram $ABCD$ meet at $O$. If $AC=14$ cm and $BD=10$ cm, find $OA$ and $OB$.", 2, "The diagonals bisect each other (1): $OA=14\\div2=7$ cm and $OB=10\\div2=5$ cm (1).", "E"),
W("In trapezium $ABCD$, $AB\\parallel DC$ and $\\angle A=70^\\circ$. Find $\\angle D$.", 2, "$AD$ is a transversal, so co-interior angles add up to $180^\\circ$ (1): $\\angle D=180^\\circ-70^\\circ=110^\\circ$ (1).", "E"),
# ---------------- MEDIUM ----------------
W("The four angles of a quadrilateral are $(x+20)^\\circ$, $(x+40)^\\circ$, $(x+60)^\\circ$ and $(x+80)^\\circ$. Find $x$ and the angles.", 2, "$4x+200=360$, so $x=40$ (1). Angles: $60^\\circ,80^\\circ,100^\\circ,120^\\circ$ (1).", "M"),
W("In parallelogram $ABCD$, $\\angle A=(3x+10)^\\circ$ and $\\angle B=(2x-10)^\\circ$. Find $x$ and all four angles.", 3, "Adjacent angles add to $180^\\circ$: $5x=180$, $x=36$ (1). $\\angle A=118^\\circ$, $\\angle B=62^\\circ$ (1). $\\angle C=118^\\circ$, $\\angle D=62^\\circ$ (1).", "M"),
W("The diagonals of a rhombus are 16 cm and 30 cm. Find its side and perimeter.", 3, "Diagonals bisect at $90^\\circ$, so each side is the hypotenuse of a right triangle with legs 8 and 15 (1). Side $=\\sqrt{64+225}=\\sqrt{289}=17$ cm (1). Perimeter $=4\\times17=68$ cm (1).", "M"),
W("In rhombus $ABCD$, $\\angle A=70^\\circ$. Find $\\angle B$, $\\angle C$, $\\angle D$ and the angle that diagonal $AC$ makes with side $AB$.", 3, "$\\angle C=70^\\circ$ (opposite) (1). $\\angle B=\\angle D=180^\\circ-70^\\circ=110^\\circ$ (1). A diagonal of a rhombus bisects the angle, so $\\angle CAB=35^\\circ$ (1).", "M"),
W("In kite $ABCD$, $AB=AD$, $CB=CD$, $\\angle B=\\angle D=90^\\circ$ and $\\angle A=80^\\circ$. Find $\\angle C$.", 2, "$\\angle C=360^\\circ-(80^\\circ+90^\\circ+90^\\circ)$ (1) $=100^\\circ$ (1).", "M"),
W("A rectangular field is 24 m long and 7 m wide. Ritu walks from one corner to the opposite corner along the diagonal; Sonu walks along two sides. How much shorter is Ritu's path?", 3, "Diagonal $=\\sqrt{24^2+7^2}=\\sqrt{625}=25$ m (1). Sonu walks $24+7=31$ m (1). Ritu's path is $31-25=6$ m shorter (1).", "M", wp=True),
W("A trapezium-shaped plot has parallel sides 30 m and 18 m, and the distance between them is 12 m. Find its area and the cost of levelling it at ₹ 50 per m².", 3, "Area $=\\frac12\\times(30+18)\\times12$ (1) $=288$ m² (1). Cost $=288\\times50=$ ₹ 14,400 (1).", "M", wp=True),
W("Name the quadrilateral: (i) diagonals bisect each other at right angles and are equal; (ii) diagonals bisect each other and are equal but not perpendicular; (iii) only one pair of opposite sides parallel.", 3, "(i) Square (1). (ii) Rectangle (1). (iii) Trapezium (1).", "M"),
W("The adjacent sides of a parallelogram-shaped garden are in the ratio $3:2$ and the fencing needed all round is 60 m. Find the two sides.", 3, "Let the sides be $3x$ and $2x$. Perimeter $=2(3x+2x)=10x=60$, $x=6$ (2). Sides $18$ m and $12$ m (1).", "M", wp=True),
W("Reena says ‘every rhombus is a square’. Give an example to show that she is wrong.", 2, "A rhombus of side 5 cm with angles $60^\\circ$ and $120^\\circ$ has equal sides but no right angle (1), so it is not a square. A square needs all angles $90^\\circ$ as well (1).", "M"),
W("In rectangle $ABCD$ the diagonals meet at $O$ and $\\angle OAB=35^\\circ$. Find $\\angle OBA$ and $\\angle AOB$.", 3, "The diagonals of a rectangle are equal and bisect each other, so $OA=OB$ (1). $\\angle OBA=\\angle OAB=35^\\circ$ (1). $\\angle AOB=180^\\circ-70^\\circ=110^\\circ$ (1).", "M"),
W("In rhombus $ABCD$, side $=8$ cm and $\\angle A=60^\\circ$. Find the diagonal $BD$ and give a reason.", 3, "$AB=AD$ and $\\angle A=60^\\circ$, so the other two angles of $\\triangle ABD$ are equal and each $=60^\\circ$ (2). It is equilateral, so $BD=$ **8 cm** (1).", "M"),
W("Two adjacent angles of a parallelogram are in the ratio $2:7$. Find all its angles.", 2, "$2x+7x=180^\\circ$, $x=20^\\circ$ (1). Angles $40^\\circ,140^\\circ,40^\\circ,140^\\circ$ (1).", "M"),
W("Find the area of a square whose diagonal is 10 cm (a square is also a rhombus: area $=\\frac12d_1d_2$).", 2, "Area $=\\frac12\\times10\\times10$ (1) $=50$ cm² (1).", "M"),
W("A rhombus-shaped garden has diagonals 24 m and 10 m. Find the cost of fencing its boundary at ₹ 120 per metre.", 3, "Side $=\\sqrt{12^2+5^2}=13$ m (1). Perimeter $=52$ m (1). Cost $=52\\times120=$ ₹ 6,240 (1).", "M", wp=True),
W("In trapezium $ABCD$, $AB\\parallel DC$, $\\angle A=65^\\circ$ and $\\angle B=80^\\circ$. Find $\\angle D$ and $\\angle C$.", 2, "Angles on the same leg add up to $180^\\circ$: $\\angle D=180^\\circ-65^\\circ=115^\\circ$ (1), $\\angle C=180^\\circ-80^\\circ=100^\\circ$ (1).", "M"),
W("State true or false with a reason: (i) a rectangle is a rhombus; (ii) a square is a rhombus; (iii) a kite is a parallelogram.", 3, "(i) False: adjacent sides of a rectangle need not be equal (1). (ii) True: a square has four equal sides (1). (iii) False: in a kite only adjacent sides are equal and opposite sides are not (generally) equal or parallel (1).", "M"),
W("Three angles of a quadrilateral are equal and the fourth angle is $60^\\circ$ more than each of them. Find all the angles.", 2, "$3x+(x+60)=360$, $4x=300$, $x=75$ (1). Angles $75^\\circ,75^\\circ,75^\\circ,135^\\circ$ (1).", "M"),
W("A signboard is shaped like a parallelogram $ABCD$ with $\\angle A=\\frac45\\angle B$. Find all its angles.", 2, "$\\angle A+\\angle B=180^\\circ$ so $\\frac45\\angle B+\\angle B=180^\\circ$, $\\frac95\\angle B=180^\\circ$, $\\angle B=100^\\circ$ (1). $\\angle A=80^\\circ$; $\\angle C=80^\\circ$, $\\angle D=100^\\circ$ (1).", "M", wp=True),
# ---------------- HARD ----------------
W("The diagonals of a rhombus are in the ratio $3:4$ and its perimeter is 40 cm. Find the lengths of the diagonals and the area of the rhombus.", 4, "Side $=40\\div4=10$ cm (1). Let diagonals be $6k$, $8k$; half-diagonals $3k$, $4k$: $9k^2+16k^2=100$ so $k=2$ (1). Diagonals **12 cm and 16 cm** (1). Area $=\\frac12\\times12\\times16=$ **96 cm²** (1).", "H"),
W("Prove that the opposite angles of a parallelogram $ABCD$ are equal, using the fact that adjacent angles add up to $180^\\circ$.", 3, "$\\angle A+\\angle B=180^\\circ$ and $\\angle B+\\angle C=180^\\circ$ (1). Subtracting, $\\angle A=\\angle C$ (1). Similarly $\\angle B+\\angle C=180^\\circ$ and $\\angle C+\\angle D=180^\\circ$ give $\\angle B=\\angle D$ (1).", "H"),
W("In parallelogram $ABCD$ the bisectors of $\\angle A$ and $\\angle B$ meet at $P$. Show that $\\angle APB=90^\\circ$.", 4, "$\\angle A+\\angle B=180^\\circ$ (adjacent angles of a parallelogram) (1). The bisectors make $\\angle PAB=\\frac12\\angle A$ and $\\angle PBA=\\frac12\\angle B$ (1). So $\\angle PAB+\\angle PBA=90^\\circ$ (1). In $\\triangle APB$, $\\angle APB=180^\\circ-90^\\circ=90^\\circ$ (1).", "H"),
W("A rhombus-shaped flower bed has a side of 10 m and one diagonal of 12 m. Find the other diagonal and the area. What is the cost of planting at ₹ 25 per m²?", 4, "Half-diagonals are $6$ and $x$ with $6^2+x^2=10^2$, $x=8$ (1). Other diagonal $=16$ m (1). Area $=\\frac12\\times12\\times16=96$ m² (1). Cost $=96\\times25=$ ₹ 2,400 (1).", "H", wp=True),
W("The angles of a quadrilateral are $(2x-10)^\\circ$, $(3x+5)^\\circ$, $(x+25)^\\circ$ and $(4x-20)^\\circ$. Find $x$ and each angle.", 3, "$10x=360$, so $x=36$ (1). Angles: $62^\\circ$, $113^\\circ$, $61^\\circ$, $124^\\circ$ (1). Check: $62+113+61+124=360$ (1).", "H"),
W("Make a table showing which of parallelogram, rectangle, rhombus, square, kite and trapezium have: (a) diagonals that bisect each other, (b) equal diagonals, (c) perpendicular diagonals.", 5, "(a) bisect each other: parallelogram, rectangle, rhombus, square (1.5). (b) equal diagonals: rectangle, square (1.5). (c) perpendicular: rhombus, square, kite (2). A general trapezium has none of these properties.", "H"),
W("A rectangular playground has a diagonal of 25 m and one side of 24 m. Find the other side, the perimeter and the cost of fencing at ₹ 80 per metre.", 4, "Other side $=\\sqrt{25^2-24^2}=\\sqrt{49}=7$ m (1). Perimeter $=2(24+7)=62$ m (1). Cost $=62\\times80=$ ₹ 4,960 (2).", "H", wp=True),
W("In kite $ABCD$, $AB=AD=25$ cm, $CB=CD=30$ cm and diagonal $BD=48$ cm. The diagonal $AC$ is the perpendicular bisector of $BD$. Find $AC$ and the area of the kite ($\\frac12\\,d_1d_2$).", 5, "Let $AC$ meet $BD$ at $O$; $BO=24$ cm (1). $AO=\\sqrt{25^2-24^2}=7$ cm (1). $CO=\\sqrt{30^2-24^2}=\\sqrt{324}=18$ cm (1). $AC=7+18=25$ cm (1). Area $=\\frac12\\times25\\times48=600$ cm² (1).", "H"),
W("The area of a trapezium is 180 cm², its height is 12 cm and one parallel side is 18 cm. Find the other parallel side.", 3, "$\\frac12(a+18)\\times12=180$ (1), so $a+18=30$ (1), $a=12$ cm (1).", "H"),
W("**Case study.** A tile designer makes three tiles. Tile A: all four sides 10 cm, diagonals 12 cm and 16 cm. Tile B: sides 12 cm and 5 cm, both diagonals 13 cm. Tile C: sides 8 cm, 8 cm, 5 cm, 5 cm in order with the equal sides next to each other. Name the shape of each tile and find the perimeter of each.", 4, "Tile A: all sides equal and diagonals unequal, so a **rhombus**; perimeter 40 cm (1.5). Tile B: opposite sides equal and diagonals equal ($12^2+5^2=13^2$), so a **rectangle**; perimeter 34 cm (1.5). Tile C: two pairs of equal adjacent sides, a **kite**; perimeter $8+8+5+5=26$ cm (1).", "H", wp=True),
W("A quadrilateral has angles in the ratio $1:2:3:4$. Find the angles. Can it be a parallelogram? Can it be a trapezium? Explain.", 4, "$10x=360^\\circ$: angles $36^\\circ,72^\\circ,108^\\circ,144^\\circ$ (1). Not a parallelogram, since opposite angles are not equal (and adjacent angles do not add up to $180^\\circ$) (1). It can be a trapezium because $72^\\circ+108^\\circ=180^\\circ$ and $36^\\circ+144^\\circ=180^\\circ$, so the sides joining those pairs of vertices can be parallel with these as co-interior angles (2).", "H"),
W("Mohan says: ‘If the diagonals of a quadrilateral bisect each other, it must be a rectangle.’ Is he right? Give a counter-example and state the correct conclusion.", 3, "He is wrong (1). A rhombus with sides 5 cm and diagonals 6 cm and 8 cm has diagonals that bisect each other but are not equal, so it is not a rectangle (1). The correct conclusion is that it is a **parallelogram**; it is a rectangle only if the diagonals are also equal (1).", "H"),
W("A rhombus-shaped signboard has side 10 cm and $\\angle A=120^\\circ$. Find $\\angle B$, the angle each half of diagonal $AC$ makes with the side, and the length of the diagonal $AC$.", 4, "$\\angle B=180^\\circ-120^\\circ=60^\\circ$ (1). Diagonal $AC$ bisects $\\angle A$, so $\\angle CAB=60^\\circ$ (1). In $\\triangle ABC$, $\\angle B=\\angle CAB=60^\\circ$ so the third angle is $60^\\circ$ and the triangle is equilateral (1). Hence $AC=10$ cm (1).", "H", wp=True),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(4)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "4.5 Diagonal Properties at a Glance"),
 ("table", ["Shape", "Diagonals bisect each other", "Diagonals equal", "Diagonals perpendicular", "Diagonals bisect the angles"], [
  ["Parallelogram", "yes", "no", "no", "no"],
  ["Rectangle", "yes", "**yes**", "no", "no"],
  ["Rhombus", "yes", "no", "**yes**", "**yes**"],
  ["Square", "yes", "**yes**", "**yes**", "**yes**"],
  ["Kite", "no (only one diagonal is bisected)", "no", "**yes**", "one diagonal bisects the angles it joins"],
  ["Trapezium", "no", "no (equal only in an isosceles trapezium)", "no", "no"]]),
 ("h3", "Proof: opposite angles of a parallelogram are equal"),
 ("p", "In parallelogram ABCD, AB ∥ DC so ∠A + ∠D = 180° (co-interior angles); AD ∥ BC so ∠A + ∠B = 180°. Hence ∠B = ∠D. In the same way ∠A = ∠C. **Proof that the bisectors of ∠A and ∠B meet at 90°:** since ∠A + ∠B = 180°, half of each adds up to 90°, so in the triangle formed with the bisectors the third angle is 180° − 90° = 90°."),
 ("h2", "4.6 Worked Examples"),
 ("h3", "Example 1 — Angles with algebra"),
 ("steps", [("In a quadrilateral the angles are (2x − 10)°, (3x + 5)°, (x + 25)° and (4x − 20)°", "Sum = 360°: 10x + 0 = 360."), ("Solve", "x = 36."), ("Angles", "62°, 113°, 61°, 124°; check 62 + 113 + 61 + 124 = 360.")]),
 ("h3", "Example 2 — Rhombus from its diagonal and side"),
 ("steps", [("Side 10 m, one diagonal 12 m", "The diagonals bisect each other at 90°, so each half-diagonal and the side form a right triangle."), ("Other half-diagonal", "6² + x² = 10², so x = 8, and the other diagonal is 16 m."), ("Area", "½ × 12 × 16 = **96 m²**.")]),
 ("h3", "Example 3 — Kite with unequal sides"),
 ("steps", [("Kite ABCD, AB = AD = 25, CB = CD = 30, BD = 48", "AC is the perpendicular bisector of BD, so BO = 24 where O is the meeting point."), ("Find AO and CO", "AO = √(25² − 24²) = 7; CO = √(30² − 24²) = √324 = 18."), ("Diagonal and area", "AC = 7 + 18 = 25; area = ½ × 25 × 48 = **600 cm²**.")]),
 ("h3", "Example 4 — A parallelogram field"),
 ("steps", [("Adjacent sides in the ratio 3 : 2, fencing 60 m", "Sides 3x and 2x; perimeter = 2(3x + 2x) = 10x."), ("Solve", "10x = 60, x = 6."), ("Sides", "**18 m and 12 m**.")]),
 ("h3", "Example 5 — Rectangle and the diagonal"),
 ("steps", [("Diagonal 25 m, one side 24 m", "The diagonal splits the rectangle into a right triangle."), ("Other side", "√(25² − 24²) = √49 = 7 m."), ("Perimeter and cost", "2(24 + 7) = 62 m; at ₹ 80 per metre the cost is ₹ 4,960.")]),
 ("h3", "Example 6 — Trapezium area, finding a side"),
 ("steps", [("Area 180 cm², height 12 cm, one parallel side 18 cm", "½ × (a + 18) × 12 = 180."), ("Solve", "6(a + 18) = 180, a + 18 = 30."), ("Answer", "a = **12 cm**.")]),
 ("h2", "4.7 Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["fencing, border, frame all round", "perimeter; rhombus 4 × side, parallelogram 2 × (sum of adjacent sides)", "7 m × 4 m field: 22 m of fencing"],
  ["walking along the diagonal", "right triangle (Pythagorean triplets 3-4-5, 5-12-13, 7-24-25, 8-15-17)", "24 m × 7 m field: diagonal 25 m"],
  ["levelling, painting, planting cost", "area × rate", "trapezium plot: ½ × (30 + 18) × 12 = 288 m²"],
  ["signboard, picture frame shaped like a parallelogram", "adjacent angles add to 180°, opposite angles equal", "one angle 72°: others 108°, 72°, 108°"],
  ["angles ‘in the ratio’", "x multiples, total 360° for a quadrilateral", "3 : 4 : 5 : 6 gives 60°, 80°, 100°, 120°"]]),
 ("h2", "4.8 Common Mistakes"),
 ("table", ["Wrong idea", "Why it is wrong", "Correct"], [
  ["Every rhombus is a square", "a rhombus needs only equal sides", "a square is a rhombus with right angles"],
  ["A rectangle has perpendicular diagonals", "only if it is also a square", "rectangle: equal diagonals; rhombus: perpendicular diagonals"],
  ["Diagonals bisecting each other makes a rectangle", "it only proves a parallelogram", "equal diagonals as well give a rectangle"],
  ["Angle sum 180° for a quadrilateral", "that is for a triangle", "360° (two triangles)"],
  ["Opposite angles of a parallelogram add to 180°", "adjacent angles add to 180°; opposite angles are equal", "∠A = ∠C and ∠A + ∠B = 180°"]]),
 ]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["Use **right triangles** (half-diagonals, Pythagoras) to find sides or diagonals of rhombus, kite and rectangle in word problems.", "**Diagonals bisect each other** gives a parallelogram; add **equal** for a rectangle, add **perpendicular** for a rhombus."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
