"""Class 8 Maths Ch 14 - Area: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
from math import isqrt
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch14"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths2" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# --- verify the numbers used ---
assert 10*6//2 == 30 and 12*5 == 60 and 10*8//2 == 40 and (8+12)*5//2 == 50 and 15*8 == 120
assert 6*4.5 == 27 and 27*80 == 2160 and 14*9//2 == 63 and 90//15 == 6 and 16*12//2 == 96 and isqrt(8**2 + 6**2) == 10
assert 20*14 - 16*10 == 120 and (9+15)*6//2 == 72 and 12*12 == 144 and 12*7//2 == 42 and 84//12 == 7
assert 6*10//2 == 30 and 30*2/8 == 7.5
assert 18*(5+7)//2 == 108 and 108*25 == 2700 and 15*8 == 120 == 10*12
assert isqrt(17**2 - 8**2) == 15 and 16*30//2 == 240
assert 30*20 - 25*15 == 225 and 225*120 == 27000
assert F(2*150, 10) == 30 and 12 + 18 == 30 and (12+18)*10//2 == 150 and 18 - 12 == 6
assert 10*12 == 120 and 120*144 == 17280
assert [a*b for a, b in [(15,3),(12,6),(9,9)]] == [45,72,81] and all(2*(a+b) == 36 for a, b in [(15,3),(12,6),(9,9)])
assert 48//2 == 24 and 24//2 == 12
assert 40*25 == 1000 and 1000//20 == 50 and 50*40 == 2000
assert 12*9//2 == 54 and F(108,15) == F(36,5)
assert (8+12)*5//2 == 50 and 6*20//2 == 60
assert 8*6//2 == 24 and F(2*24,10) == F(24,5)
assert 84//2 == 42
assert (40+24)*15//2 == 480 and 480*35 == 16800
assert 30*40//2 == 600 and isqrt(15**2 + 20**2) == 25
assert 2.5*1_000_000 == 2_500_000 and 3*10_000 == 30_000
assert 35*2/14 == 5 and 14*5//2 == 35
assert 15*20//2 == 150 and 2*150/25 == 12 and isqrt(15**2 + 20**2) == 25
assert 12*9 - 5*4 == 88 and 88*150 == 13200 and 2*(12 + 9) == 42
assert isqrt(5**2 - 4**2) == 3 and (20 - 12)//2 == 4 and (20+12)*3//2 == 48
assert 96*2//16 == 12 and isqrt(8**2 + 6**2) == 10 and F(96, 10) == F(48,5)
assert 20*15 == 300 and 12*15 == 180 and 180//15 == 12 and 180//20 == 9
assert 60*(24+16)//2 == 1200 and 1200/10000 == 0.12 and 0.12*100 == 12 and 0.12*40 == 4.8
assert (9+15)*6//2 == 72 and 20*20 == 400 and 40*10 == 400 and 2*(40+10) == 100 and 4*20 == 80 and 100*120 == 12000 and 80*120 == 9600 and 12000 - 9600 == 2400
assert F(60*2, 5) == 24 and F(60*3, 5) == 36 and 24 + 36 == 60
assert (24)*(19) - 20*15 == 156 and 156*85 == 13260
assert 4*(20+10)//2 * 2 == 120
assert 14*8//4 == 28 and 14*8 == 112
assert 20*30 == 600 and 600*4 == 2400 and 2400*8 == 19200
assert 80*50 == 4000 and 4000//2 == 2000 and 2000*450 == 900000

WS = [
# ---------------- EASY ----------------
W("The area of a triangle with base 10 cm and height 6 cm is:", 1, "(c) 30 cm². $\\frac12\\times10\\times6=30$. (1)", "E", opts=["16 cm²", "60 cm²", "30 cm²", "36 cm²"]),
W("The area of a parallelogram with base 12 cm and height 5 cm is:", 1, "(b) 60 cm². Area $=$ base $\\times$ height $=12\\times5$. (1)", "E", opts=["30 cm²", "60 cm²", "34 cm²", "17 cm²"]),
W("The diagonals of a rhombus are 10 cm and 8 cm. Its area is:", 1, "(a) 40 cm². $\\frac12\\times10\\times8=40$. (1)", "E", opts=["40 cm²", "80 cm²", "18 cm²", "36 cm²"]),
W("A trapezium has parallel sides 8 cm and 12 cm and height 5 cm. Its area is:", 1, "(d) 50 cm². $\\frac12\\times5\\times(8+12)=50$. (1)", "E", opts=["100 cm²", "480 cm²", "25 cm²", "50 cm²"]),
W("The number of cm² in 1 m² is:", 1, "(c) 10,000. $1\\text{ m}=100\\text{ cm}$, so $1\\text{ m}^2=100\\times100=10{,}000$ cm². (1)", "E", opts=["100", "1000", "10,000", "1,00,000"]),
W("A median of a triangle (from a vertex to the midpoint of the opposite side) divides it into two triangles which have:", 1, "(b) equal areas. They have equal bases and the same height. (1)", "E", opts=["equal perimeters", "equal areas", "equal angles", "no relation"]),
W("A rectangular plot is 15 m long and 8 m wide. Its area is:", 1, "(a) 120 m². $15\\times8=120$. (1)", "E", opts=["120 m²", "46 m²", "23 m²", "60 m²"], wp=True),
W("A rectangular room is 6 m by 4.5 m. Find the cost of tiling the floor at ₹ 80 per m².", 2, "Area $=6\\times4.5=27$ m² (1). Cost $=27\\times80=$ ₹ 2160 (1).", "E", wp=True),
W("A triangular flower bed has base 14 m and height 9 m. Find its area.", 2, "$\\frac12\\times14\\times9$ (1) $=63$ m² (1).", "E", wp=True),
W("True or false (give a reason): two rectangles with the same perimeter always have the same area.", 1, "**False.** $10\\times2$ and $6\\times6$ both have perimeter 24 cm but areas $20$ cm² and $36$ cm² (1).", "E"),
W("The area of a parallelogram is 90 cm² and its base is 15 cm. Find its height.", 2, "Height $=\\frac{90}{15}$ (1) $=6$ cm (1).", "E"),
W("A rhombus has diagonals 16 cm and 12 cm. Find its area and its side.", 2, "Area $=\\frac12\\times16\\times12=96$ cm² (1). Side $=\\sqrt{8^2+6^2}=10$ cm (1).", "E"),
W("A park is 20 m by 14 m. A path inside it leaves an inner lawn of 16 m by 10 m. Find the area of the path.", 2, "Outer $=280$ m², inner $=160$ m² (1). Path $=120$ m² (1).", "E", wp=True),
W("A trapezium-shaped plot has parallel sides 9 m and 15 m and the distance between them is 6 m. Find its area.", 2, "$\\frac12\\times6\\times(9+15)$ (1) $=72$ m² (1).", "E", wp=True),
W("Write the number of square inches in 1 square foot and the number of square metres in 1 square kilometre.", 2, "$1\\text{ ft}^2=12\\times12=144$ in² (1). $1\\text{ km}^2=1000\\times1000=10{,}00{,}000$ m² (1).", "E"),
W("The area of a triangle is 42 cm² and its base is 12 cm. Find its height.", 2, "$\\frac12\\times12\\times h=42$ (1), so $h=7$ cm (1).", "E"),
W("An A4 sheet measures 21 cm by 29.7 cm. Find its area.", 2, "$21\\times29.7$ (1) $=623.7$ cm² (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("In $\\triangle ABC$, $BC=10$ cm, the altitude $AX$ from $A$ to $BC$ is 6 cm and $AC=8$ cm. Find the altitude $BY$ from $B$ to $AC$.", 3, "Area $=\\frac12\\times10\\times6=30$ cm² (1). Also area $=\\frac12\\times8\\times BY=4\\,BY$ (1). $BY=7.5$ cm (1).", "M"),
W("A plot $ABCD$ has diagonal $AC=18$ m. The perpendiculars from $B$ and $D$ to $AC$ are 5 m and 7 m. Find its area and the cost of ploughing at ₹ 25 per m².", 3, "Area $=\\frac12\\times18\\times(5+7)$ (1) $=108$ m² (1). Cost $=108\\times25=$ ₹ 2700 (1).", "M", wp=True),
W("A parallelogram has sides 15 cm and 10 cm. The height on the 15 cm side is 8 cm. Find its area and the height on the 10 cm side.", 3, "Area $=15\\times8=120$ cm² (1.5). Height $=\\frac{120}{10}=12$ cm (1.5).", "M"),
W("A rhombus-shaped signboard has side 17 cm and one diagonal 16 cm. Find the other diagonal and the area.", 3, "Half-diagonals $8$ and $x$ with $8^2+x^2=17^2$, $x=15$ (1). Other diagonal $=30$ cm (1). Area $=\\frac12\\times16\\times30=240$ cm² (1).", "M"),
W("A rectangular lawn 30 m by 20 m has a path 2.5 m wide laid all round **inside** it. Find the area of the path and the cost of paving it at ₹ 120 per m².", 3, "Inner lawn $=(30-5)\\times(20-5)=25\\times15=375$ m² (1). Path $=600-375=225$ m² (1). Cost $=225\\times120=$ ₹ 27,000 (1).", "M", wp=True),
W("The area of a trapezium is 150 cm² and its height is 10 cm. One parallel side is 6 cm longer than the other. Find both parallel sides.", 3, "$\\frac12\\times10\\times(a+a+6)=150$ (1). $2a+6=30$, $a=12$ (1). Parallel sides $12$ cm and $18$ cm (1).", "M"),
W("A room is 10 ft by 12 ft. Find its area in ft² and in in².", 3, "Area $=10\\times12=120$ ft² (1). $1\\text{ ft}^2=144$ in² (1). $120\\times144=17{,}280$ in² (1).", "M", wp=True),
W("Find the areas of rectangles with perimeter 36 cm and sides (i) 15 cm $\\times$ 3 cm, (ii) 12 cm $\\times$ 6 cm, (iii) 9 cm $\\times$ 9 cm. Which has the greatest area?", 3, "(i) $45$ cm², (ii) $72$ cm², (iii) $81$ cm² (2). The square has the greatest area (1).", "M"),
W("$D$ is the midpoint of $BC$ in $\\triangle ABC$ whose area is 48 cm². Find the area of $\\triangle ABD$. If $E$ is the midpoint of $AD$, find the area of $\\triangle ABE$.", 3, "A median halves the area: $\\triangle ABD=24$ cm² (1.5). $AE=ED$ gives $\\triangle ABE=\\frac12\\times24=12$ cm² (1.5).", "M"),
W("A parallelogram-shaped field has base 40 m and height 25 m. Seeds are sown at 1 kg per 20 m² and cost ₹ 40 per kg. Find the cost of the seed.", 3, "Area $=40\\times25=1000$ m² (1). Seed $=1000\\div20=50$ kg (1). Cost $=50\\times40=$ ₹ 2000 (1).", "M", wp=True),
W("In $\\triangle ABC$, $BC=12$ cm and the area is 54 cm². Find the altitude from $A$. If $AC=15$ cm, find the altitude from $B$ to $AC$.", 3, "$\\frac12\\times12\\times h=54$, $h=9$ cm (1). $\\frac12\\times15\\times h'=54$ (1), $h'=\\frac{108}{15}=7.2$ cm (1).", "M"),
W("Sita finds the area of a trapezium with parallel sides 8 cm and 12 cm, slant side 6 cm and height 5 cm as $\\frac12\\times6\\times20=60$ cm². Find her mistake and the correct area.", 2, "She used the slant side instead of the perpendicular height (1). Correct area $=\\frac12\\times5\\times20=50$ cm² (1).", "M"),
W("A rectangle is 8 cm by 6 cm. Find the area of each triangle made by a diagonal, the length of the diagonal and the perpendicular distance from the opposite corner to the diagonal.", 3, "Each triangle $=\\frac12\\times8\\times6=24$ cm² (1). Diagonal $=\\sqrt{64+36}=10$ cm (1). $\\frac12\\times10\\times h=24$, $h=4.8$ cm (1).", "M"),
W("$ABCD$ is a parallelogram of area 84 cm² and $P$ is any point on side $CD$. Find the area of $\\triangle ABP$ and give a reason.", 3, "$\\triangle ABP$ and the parallelogram have the same base $AB$ and the same height (1). So the triangle is half the parallelogram (1): $42$ cm² (1).", "M"),
W("A trapezium-shaped field has parallel sides 40 m and 24 m and the distance between them is 15 m. Find the cost of levelling it at ₹ 35 per m².", 3, "Area $=\\frac12\\times15\\times64=480$ m² (2). Cost $=480\\times35=$ ₹ 16,800 (1).", "M", wp=True),
W("A kite is made of paper in the shape of a rhombus with diagonals 30 cm and 40 cm. Find the paper needed and the length of each side.", 3, "Area $=\\frac12\\times30\\times40=600$ cm² (1). Side $=\\sqrt{15^2+20^2}$ (1) $=25$ cm (1).", "M", wp=True),
W("Convert: (a) 2.5 km² into m², (b) 3 m² into cm².", 2, "(a) $2.5\\times10{,}00{,}000=25{,}00{,}000$ m² (1). (b) $3\\times10{,}000=30{,}000$ cm² (1).", "M"),
W("Triangles $ABC$ and $ABD$ stand on the same base $AB=14$ cm, with $C$ and $D$ on a line parallel to $AB$ at a distance of 5 cm. Find the area of each and say why they are equal.", 3, "Area of each $=\\frac12\\times14\\times5=35$ cm² (2). Same base and the same height (parallel lines are always 5 cm apart), so the areas are equal (1).", "M"),
# ---------------- HARD ----------------
W("In a right triangle the legs are 15 cm and 20 cm. Find the hypotenuse, the area, and the altitude to the hypotenuse.", 3, "Hypotenuse $=\\sqrt{225+400}=25$ cm (1). Area $=\\frac12\\times15\\times20=150$ cm² (1). $\\frac12\\times25\\times h=150$, $h=12$ cm (1).", "H"),
W("An L-shaped room is made from a rectangle 12 m by 9 m by removing a rectangular corner 5 m by 4 m. Find its floor area and the cost of tiling at ₹ 150 per m². What is its perimeter?", 4, "Area $=108-20=88$ m² (1). Cost $=88\\times150=$ ₹ 13,200 (1). Removing a corner rectangle does not change the perimeter: $2(12+9)=42$ m (2).", "H", wp=True),
W("The parallel sides of an isosceles trapezium are 20 m and 12 m and each non-parallel side is 5 m. Find its height and area.", 4, "Each triangular end has base $\\frac{20-12}{2}=4$ m (1). Height $=\\sqrt{5^2-4^2}=3$ m (2). Area $=\\frac12\\times3\\times32=48$ m² (1).", "H"),
W("The area of a rhombus is 96 cm² and one diagonal is 16 cm. Find the other diagonal, the side and the perpendicular distance between opposite sides.", 4, "Other diagonal $=\\frac{2\\times96}{16}=12$ cm (1). Side $=\\sqrt{8^2+6^2}=10$ cm (1). Rhombus is a parallelogram: height $=\\frac{96}{10}$ (1) $=9.6$ cm (1).", "H"),
W("A parallelogram has sides 20 cm and 15 cm. The perpendicular distance between the 20 cm sides is 9 cm. Find the area and the distance between the 15 cm sides.", 4, "Area $=20\\times9=180$ cm² (2). Height on the 15 cm side $=\\frac{180}{15}=12$ cm (2).", "H"),
W("**Case study.** A farmer's field $ABCD$ has diagonal $AC=60$ m, and the perpendiculars from $B$ and $D$ to $AC$ are 24 m and 16 m. Find its area in m² and in hectares (1 hectare = 10,000 m²). If wheat seed is 100 kg per hectare, how much seed is needed, and what is the harvest at 40 quintal per hectare?", 5, "Area $=\\frac12\\times60\\times(24+16)=1200$ m² (2). $=0.12$ hectare (1). Seed $=12$ kg (1). Harvest $=0.12\\times40=4.8$ quintal (1).", "H", wp=True),
W("Prove that the area of a trapezium with parallel sides $a$, $b$ and height $h$ is $\\frac12h(a+b)$ by joining two copies to form a parallelogram. Verify with $a=9$, $b=15$, $h=6$.", 4, "Place a second copy upside down beside the first to make a parallelogram with base $(a+b)$ and height $h$ (2). Its area is $(a+b)h$, so the trapezium is $\\frac12h(a+b)$ (1). $\\frac12\\times6\\times24=72$ (1).", "H"),
W("A rectangular lawn 20 m by 15 m has a path 2 m wide running all round it **outside**. Find the area of the path and the cost of cementing it at ₹ 85 per m².", 4, "Outer rectangle $=(20+4)\\times(15+4)=24\\times19=456$ m² (1). Lawn $=300$ m² (1). Path $=156$ m² (1). Cost $=156\\times85=$ ₹ 13,260 (1).", "H", wp=True),
W("A square field of side 20 m and a rectangular field 40 m by 10 m have the same area. Compare the fencing needed and the cost at ₹ 120 per metre.", 3, "Both areas are 400 m² (1). Perimeters: $80$ m and $100$ m (1). Costs ₹ 9600 and ₹ 12,000; the square saves ₹ 2400 (1).", "H", wp=True),
W("$D$ is a point on side $BC$ of $\\triangle ABC$ with $BD:DC=2:3$. The area of $\\triangle ABC$ is 60 cm². Find the areas of $\\triangle ABD$ and $\\triangle ADC$ and explain.", 3, "Both triangles have the same height from $A$, so areas are in the ratio of the bases $2:3$ (1). $\\triangle ABD=24$ cm² (1), $\\triangle ADC=36$ cm² (1).", "H"),
W("A hexagonal plot $ABCDEF$ has diagonal $AD=20$ m. It is made of two trapezia $ABCD$ (parallel sides $AD=20$ m, $BC=10$ m) and $ADEF$ (parallel sides $AD=20$ m, $FE=10$ m), each of height 4 m. Find its area.", 4, "Each trapezium $=\\frac12\\times4\\times(20+10)=60$ m² (2). Total $=120$ m² (2).", "H", wp=True),
W("The diagonals of a rectangle 14 cm by 8 cm meet at $O$. Find the area of each of the four triangles formed and explain why they are equal.", 4, "Rectangle $=112$ cm² (1). Each triangle $=28$ cm² (1). The diagonals bisect each other, so $\\triangle AOB$ and $\\triangle COB$ have equal bases on the same line and the same height; likewise for the others (2).", "H"),
W("A hall is 20 ft by 30 ft. It is covered with square tiles of side 6 inches costing ₹ 8 each. How many tiles are needed and what is the cost?", 4, "Area $=600$ ft² (1). One tile $=\\frac12\\times\\frac12=\\frac14$ ft², so 4 tiles per ft² (1). Tiles $=600\\times4=2400$ (1). Cost $=2400\\times8=$ ₹ 19,200 (1).", "H", wp=True),
W("**Case study.** A parallelogram-shaped field $ABCD$ has $AB=80$ m and the distance between $AB$ and $CD$ is 50 m. (a) Find its area. (b) The diagonal $AC$ divides it into two triangles; find the area of each. (c) The farmer sells $\\triangle ABC$ at ₹ 450 per m². Find the amount he receives. (d) State why the two triangles have equal area.", 5, "(a) $80\\times50=4000$ m² (1). (b) $2000$ m² each (1). (c) $2000\\times450=$ ₹ 9,00,000 (2). (d) The diagonal of a parallelogram divides it into two congruent triangles (1).", "H", wp=True),
]

_o = _old(9)
_i = max(i for i, b in enumerate(_o["blocks"]) if b[0] == "h2")
_pre, _tail = _o["blocks"][:_i], _o["blocks"][_i:]
_extra = [
 ("h2", "Formula Sheet and Choosing the Right Method"),
 ("table", ["Figure", "Area", "What to identify first"], [["Rectangle", "l × b", "two adjacent sides"], ["Square", "a² or ½ × d²", "side or diagonal"], ["Triangle", "½ × base × height", "a base and its perpendicular height; use the theorem if only sides are given in a right triangle"], ["Parallelogram", "base × height", "the perpendicular height, not the slant side"], ["Rhombus", "½ × d₁ × d₂", "both diagonals (find one from the side with the theorem)"], ["Trapezium", "½ × h × (a + b)", "the two parallel sides and the distance between them"], ["Any quadrilateral", "½ × diagonal × (sum of the two perpendiculars)", "one diagonal and the two perpendiculars to it"], ["Path around a rectangle", "outer area − inner area", "outside path: add 2 × width to each side; inside path: subtract 2 × width"]]),
 ("note", "FORMULA", "Unit conversions: 1 m² = 10,000 cm²;  1 ft² = 144 in²;  1 km² = 10,00,000 m²;  1 hectare = 10,000 m². **Always square the length factor.**"),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Altitude from equal areas"),
 ("steps", [("Question", "In △ABC, BC = 10 cm, altitude AX = 6 cm and AC = 8 cm. Find the altitude BY on AC."), ("Area", "½ × 10 × 6 = 30 cm²."), ("Same area, other base", "½ × 8 × BY = 30, so 4 × BY = 30."), ("Answer", "BY = **7.5 cm**.")]),
 ("h3", "Example 2 — Quadrilateral from a diagonal"),
 ("steps", [("Question", "Diagonal AC = 18 m; perpendiculars from B and D to AC are 5 m and 7 m."), ("Split", "Area = ½ × 18 × 5 + ½ × 18 × 7 = ½ × 18 × (5 + 7)."), ("Answer", "**108 m²**; ploughing at ₹ 25 per m² costs ₹ 2700.")]),
 ("h3", "Example 3 — Rhombus from side and diagonal"),
 ("steps", [("Question", "Side 17 cm, one diagonal 16 cm. Find the area."), ("Half-diagonal", "8 and x with 8² + x² = 17², so x = 15."), ("Answer", "Diagonals 16 and 30, area = ½ × 16 × 30 = **240 cm²**.")]),
 ("h3", "Example 4 — Isosceles trapezium"),
 ("steps", [("Question", "Parallel sides 20 m and 12 m, non-parallel sides 5 m each."), ("Height", "Each end is a right triangle with base (20 − 12) ÷ 2 = 4 m and hypotenuse 5 m, so h = √(25 − 16) = 3 m."), ("Area", "½ × 3 × (20 + 12) = **48 m²**.")]),
 ("h3", "Example 5 — Path outside a lawn"),
 ("steps", [("Question", "Lawn 20 m × 15 m with a 2 m path all round outside; cement ₹ 85 per m²."), ("Outer rectangle", "(20 + 4) × (15 + 4) = 24 × 19 = 456 m²."), ("Path", "456 − 300 = 156 m², cost 156 × 85 = **₹ 13,260**.")]),
 ("h3", "Example 6 — Tiles and units"),
 ("steps", [("Question", "A 20 ft × 30 ft hall is tiled with 6 in × 6 in tiles at ₹ 8 each."), ("Area", "600 ft². A tile is ½ ft × ½ ft = ¼ ft², so 4 tiles per ft²."), ("Answer", "2400 tiles, cost **₹ 19,200**.")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics"], [
  ["‘cost of levelling, ploughing, tiling, painting’", "area × rate per m²"],
  ["‘fencing, border, boundary’", "perimeter (a length), not area"],
  ["‘path all round’ (outside / inside)", "outer rectangle − inner rectangle; widths added or subtracted twice"],
  ["‘diagonal of a parallelogram’", "divides it into two triangles of equal area"],
  ["‘distance between the parallel sides’", "the height of a trapezium or parallelogram"],
  ["‘median’ or ‘midpoint’ of a side", "splits the triangle into two equal areas"],
  ["‘in hectares’ or ‘in acres’", "convert from m² (1 hectare = 10,000 m²) before pricing"]]),
 ("note", "REMEMBER", "Draw the figure, mark the perpendicular height with a small square, and write the **unit with a square** (cm², m²). If only slant sides are given, use the Baudhāyana–Pythagoras theorem to find the height."),
 ("h2", "Likely Exam Questions"),
 ("qa", [("Prove that the area of a trapezium is ½ × h × (a + b).", "Join two copies to form a parallelogram of base a + b and height h; the trapezium is half of it."),
  ("Why can the same perimeter give different areas?", "Perimeter measures length round the edge, area measures the surface; 10 × 2 and 6 × 6 both have perimeter 24 cm but areas 20 and 36 cm²."),
  ("A square and a 40 m × 10 m rectangle have equal area. Which needs less fencing?", "Square of side 20 m: 80 m, against 100 m for the rectangle."),
  ("A rhombus has area 96 cm² and one diagonal 16 cm. Find the side.", "Other diagonal 12 cm, side = √(8² + 6²) = 10 cm."),
  ("How many tiles of 6 in × 6 in cover 600 ft²?", "1 ft² holds 4 tiles, so 2400 tiles."),
  ("Why do triangles on the same base between two parallel lines have equal areas?", "They have the same base and the same height, so ½ × base × height is the same.")]),
]
CH = dict(_o, num=14, blocks=_pre + _extra + _tail,
          takeaways=_o["takeaways"] + ["For paths, use outer − inner; an outside path adds twice the width to each side, an inside path subtracts it.", "If only the sides of a figure are known, build a right triangle and use the Baudhāyana–Pythagoras theorem to get the height or a diagonal."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
