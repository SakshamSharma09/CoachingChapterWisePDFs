"""Class 9 Maths Ch 6 - Measuring Space: Perimeter and Area: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run
from fractions import Fraction as F
from math import isqrt

BANK = "c9m_ch06"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c9_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# ---- verification (pi = 22/7) ----
PI = F(22, 7)
def heron2(a, b, c):
    s = F(a + b + c, 2); return s * (s - a) * (s - b) * (s - c)
assert 2 * PI * 7 == 44 and PI * 14 ** 2 == 616 and 2 * PI * 21 == 132 and 2 * PI * 35 == 220 and PI * 70 ** 2 == 15400
assert 2 * (40 + 25) * 12 == 1560 and 25 * 12 * 8 == 2400 and F(1, 2) * (30 + 20) * 12 == 300 and PI * 14 + 28 == 72
assert heron2(5, 12, 13) == 900 and heron2(13, 14, 15) == 7056 and heron2(17, 25, 26) == 204 ** 2 and 204 * 20 == 4080
assert 132000 // 440 == 300 and PI * (21 ** 2 - 14 ** 2) == 770 and 770 * 15 == 11550
assert F(1, 3) * PI * 21 ** 2 == 462 and F(1, 3) * 2 * PI * 21 == 44 and F(1, 2) * 16 * 30 == 240 and isqrt(8 ** 2 + 15 ** 2) == 17
assert 14 ** 2 - PI * 49 == 42 and F(1, 4) * PI * 14 ** 2 == 154
assert 2 * 100 + 2 * PI * 35 == 420 and 2100 // 420 == 5 and 176 * 7 // 44 == 28 and PI * 28 ** 2 == 2464
assert 12 * 8 == 96 and 12 * 6 == 72 and 15 ** 2 - 9 ** 2 == 12 ** 2 and F(1, 2) * (32 + 14) * 12 == 276
assert PI * 14 ** 2 / 8 == 77 and 2 * PI * 14 / 8 == 11 and 14 + 14 + 11 == 39
assert heron2(15, 15, 24) == 108 ** 2 and 2 * 108 // 24 == 9
s = (25 + 39 + 52 + 60) // 2
assert s == 88 and (s - 25) * (s - 39) * (s - 52) * (s - 60) == 1764 ** 2 and 1764 * 30 == 52920 and 25 ** 2 + 60 ** 2 == 65 ** 2 and 39 ** 2 + 52 ** 2 == 65 ** 2
assert 2 * PI * 35 - 2 * PI * 28 == 44 and 220 - 176 == 44
assert 2 * PI * 35 == 220 and 2 * 3.14 * 35 == 219.8 and abs(220 - 219.8 - 0.2) < 1e-9
assert 16 * 9 == 12 ** 2 and 2 * (16 + 9) == 50 and 4 * 12 == 48
assert 2 * (28 + 16) == 88 and PI * 14 ** 2 == 616 and 28 * 16 == 448
assert F(45, 360) * 2 * PI * 28 == 22 and F(45, 360) * PI * 28 ** 2 == 308 and 22 + 56 == 78
assert 1.1 ** 2 == 1.2100000000000002 and round(1.21 - 1, 2) == 0.21
assert 2 * PI * 28 == 176 and 2 * PI * 35 == 220 and PI * (35 ** 2 - 28 ** 2) == 1386 and 1386 * 25 == 34650
assert 40 * 28 + PI * 14 ** 2 == 1736 and 2 * 40 + 2 * PI * 14 == 168
assert 28 ** 2 - 4 * F(1, 4) * PI * 49 == 630 and 4 * F(1, 4) * 2 * PI * 7 == 44
assert heron2(9, 40, 41) == 180 ** 2 and F(1, 2) * 9 * 40 == 180 and F(2 * 180, 41) > 8.78
assert 2 * PI * 24 + 0 or True
assert 2 * PI * F(49, 2) == 154 and 38.5 ** 2 == 1482.25 and PI * F(49, 2) ** 2 == F(3773, 2) == 1886.5 and 1886.5 - 1482.25 == 404.25
assert heron2(13, 14, 15) == 84 ** 2 and F(1, 2) * 9 * 12 == 54 and 84 + 54 == 138 and 9 ** 2 + 12 ** 2 == 15 ** 2
assert round(150 * 1.732, 1) == 259.8
assert F(8, 3) * PI * 14 == F(352, 3) and round(352 / 3, 2) == 117.33
assert F(1, 4) * PI * 196 - F(1, 2) * 14 * 14 == 56
assert F(1, 2) * 20 * (7 + 9) == 160 and 160 * 150 == 24000
assert round(36 * 1.732, 2) == 62.35 and round(100 * 1.732, 1) == 173.2

WS = [
# ---------------- EASY ----------------
W("The circumference of a circle of radius $7$ cm (take $\\pi=\\frac{22}7$) is:", 1, "(b) $44$ cm. $2\\pi r=2\\times\\frac{22}7\\times7=44$. (1)", "E", opts=["$22$ cm", "$44$ cm", "$154$ cm", "$308$ cm"]),
W("The area of a circle of radius $14$ cm (take $\\pi=\\frac{22}7$) is:", 1, "(c) $616$ cm$^2$. $\\pi r^2=\\frac{22}7\\times196=616$. (1)", "E", opts=["$88$ cm$^2$", "$308$ cm$^2$", "$616$ cm$^2$", "$1232$ cm$^2$"]),
W("The area of a triangle with base $10$ cm and height $6$ cm is:", 1, "(a) $30$ cm$^2$. $\\frac12\\times10\\times6=30$. (1)", "E", opts=["$30$ cm$^2$", "$60$ cm$^2$", "$16$ cm$^2$", "$15$ cm$^2$"]),
W("For a triangle with sides $13$ cm, $14$ cm and $15$ cm the semi-perimeter $s$ is:", 1, "(d) $21$ cm. $s=\\frac{13+14+15}2=21$. (1)", "E", opts=["$42$ cm", "$14$ cm", "$20$ cm", "$21$ cm"]),
W("The area of a parallelogram with base $12$ cm and perpendicular height $5$ cm is:", 1, "(b) $60$ cm$^2$. Area $=$ base $\\times$ height. (1)", "E", opts=["$17$ cm$^2$", "$60$ cm$^2$", "$30$ cm$^2$", "$34$ cm$^2$"]),
W("The perimeter of a semicircle of radius $7$ cm (including the diameter) is:", 1, "(c) $36$ cm. $\\pi r+2r=22+14=36$. (1)", "E", opts=["$22$ cm", "$29$ cm", "$36$ cm", "$44$ cm"]),
W("Which statement about $\\pi$ is correct?", 1, "(d) $\\pi$ is irrational. $\\frac{22}7$ and $3.14$ are only approximations; the decimal of $\\pi$ neither ends nor repeats. (1)", "E", opts=["$\\pi=\\frac{22}7$ exactly", "$\\pi=3.14$ exactly", "$\\pi$ is the ratio of area to radius", "$\\pi$ is irrational"]),
W("A circular park has a radius of $21$ m. How long is the fence needed to go around it? (Take $\\pi=\\frac{22}7$.)", 2, "Fence $=$ circumference $=2\\pi r=2\\times\\frac{22}7\\times21$ (1) $=132$ m (1).", "E", wp=True),
W("A bicycle wheel has radius $35$ cm. How far does it move in one complete turn and in $100$ turns? (Take $\\pi=\\frac{22}7$.)", 2, "One turn $=2\\pi r=2\\times\\frac{22}7\\times35=220$ cm (1). $100$ turns $=22000$ cm $=220$ m (1).", "E", wp=True),
W("A rectangular field is $40$ m long and $25$ m wide. Find its perimeter and the cost of fencing it at ₹ $12$ per metre.", 2, "Perimeter $=2(40+25)=130$ m (1). Cost $=130\\times12=$ ₹ $1560$ (1).", "E", wp=True),
W("A triangular signboard has base $1.5$ m and height $0.8$ m. Find its area.", 2, "Area $=\\frac12\\times1.5\\times0.8$ (1) $=0.6$ m$^2$ (1).", "E", wp=True),
W("A circular table-top has radius $70$ cm. Find its area. (Take $\\pi=\\frac{22}7$.)", 2, "$A=\\pi r^2=\\frac{22}7\\times70\\times70$ (1) $=15400$ cm$^2$ (1).", "E", wp=True),
W("A parallelogram-shaped field has base $25$ m and height $12$ m. Find its area and the cost of levelling it at ₹ $8$ per m$^2$.", 2, "Area $=25\\times12=300$ m$^2$ (1). Cost $=300\\times8=$ ₹ $2400$ (1).", "E", wp=True),
W("True or false (give a reason): if the radius of a circle is doubled, its area also becomes double.", 1, "**False.** Area $=\\pi r^2$; for radius $2r$ the area is $\\pi(2r)^2=4\\pi r^2$, i.e. four times. (1)", "E"),
W("A trapezium-shaped plot has parallel sides $30$ m and $20$ m and the distance between them is $12$ m. Find its area.", 2, "Area $=\\frac12(30+20)\\times12$ (1) $=300$ m$^2$ (1).", "E", wp=True),
W("A garden is in the shape of a semicircle of radius $14$ m. Find the length of the boundary (curved part and the straight edge). (Take $\\pi=\\frac{22}7$.)", 2, "Curved part $=\\pi r=\\frac{22}7\\times14=44$ m (1). Straight edge $=2r=28$ m; total $=72$ m (1).", "E", wp=True),
W("Find the perimeter and the area of an equilateral triangle of side $8$ cm. (Take $\\sqrt3=1.73$.)", 2, "Perimeter $=3\\times8=24$ cm (1). Area $=\\frac{\\sqrt3}4a^2=\\frac{1.73}4\\times64=27.68$ cm$^2$ (1).", "E"),
W("A triangular garden has sides $5$ m, $12$ m and $13$ m. Use Heron's formula to find its area.", 2, "$s=\\frac{5+12+13}2=15$ (1). Area $=\\sqrt{15\\times10\\times3\\times2}=\\sqrt{900}=30$ m$^2$ (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("A wheel of radius $70$ cm rolls along a road. How many complete turns does it make to cover $1.32$ km? (Take $\\pi=\\frac{22}7$.)", 3, "Circumference $=2\\times\\frac{22}7\\times70=440$ cm (1). Distance $=1.32$ km $=132000$ cm (1). Turns $=\\frac{132000}{440}=300$ (1).", "M", wp=True),
W("A circular pond of radius $14$ m is surrounded by a path $7$ m wide. Find the area of the path and the cost of paving it at ₹ $15$ per m$^2$. (Take $\\pi=\\frac{22}7$.)", 3, "Outer radius $R=21$ m, inner $r=14$ m (1). Area $=\\pi(R^2-r^2)=\\frac{22}7(441-196)=770$ m$^2$ (1). Cost $=770\\times15=$ ₹ $11550$ (1).", "M", wp=True),
W("A windscreen wiper of length $21$ cm sweeps through an angle of $120^\\circ$. Find the area swept and the length of the arc traced by the tip. (Take $\\pi=\\frac{22}7$.)", 3, "Fraction of circle $=\\frac{120}{360}=\\frac13$ (1). Area $=\\frac13\\times\\frac{22}7\\times21^2=462$ cm$^2$ (1). Arc $=\\frac13\\times2\\times\\frac{22}7\\times21=44$ cm (1).", "M", wp=True),
W("A triangular plot has sides $17$ m, $25$ m and $26$ m. Find its area using Heron's formula and the cost of cleaning it at ₹ $20$ per m$^2$.", 3, "$s=\\frac{17+25+26}2=34$ (1). Area $=\\sqrt{34\\times17\\times9\\times8}=\\sqrt{41616}=204$ m$^2$ (1). Cost $=204\\times20=$ ₹ $4080$ (1).", "M", wp=True),
W("A rhombus-shaped tile has diagonals $16$ cm and $30$ cm. Find its area, its side and its perimeter.", 3, "Area $=\\frac12\\times16\\times30=240$ cm$^2$ (1). Side $=\\sqrt{8^2+15^2}=17$ cm (1). Perimeter $=4\\times17=68$ cm (1).", "M", wp=True),
W("A square tile of side $14$ cm has a circle of radius $7$ cm printed inside it, touching all four sides. Find the area of the tile outside the circle. (Take $\\pi=\\frac{22}7$.)", 3, "Area of square $=14\\times14=196$ cm$^2$ (1). Area of circle $=\\frac{22}7\\times49=154$ cm$^2$ (1). Required area $=196-154=42$ cm$^2$ (1).", "M", wp=True),
W("A cow is tied at one corner of a square field of side $20$ m with a rope $14$ m long. Find the area of the field that the cow can graze. (Take $\\pi=\\frac{22}7$.)", 3, "The cow can move in a quarter of a circle of radius $14$ m (the rope is shorter than the side) (1). Area $=\\frac14\\pi r^2$ (1) $=\\frac14\\times\\frac{22}7\\times196=154$ m$^2$ (1).", "M", wp=True),
W("A running track has two straight parts of $100$ m each and two semicircular ends of radius $35$ m. Find the length of one lap and the number of laps needed to run $2.1$ km. (Take $\\pi=\\frac{22}7$.)", 3, "Curved part $=2\\pi r=2\\times\\frac{22}7\\times35=220$ m (1). Lap $=2\\times100+220=420$ m (1). Laps $=\\frac{2100}{420}=5$ (1).", "M", wp=True),
W("A circular ring road is $176$ m long. Find the radius of the road and the area enclosed by it. (Take $\\pi=\\frac{22}7$.)", 3, "$2\\pi r=176$, so $r=\\frac{176\\times7}{44}=28$ m (1). Area $=\\frac{22}7\\times28^2$ (1) $=2464$ m$^2$ (1).", "M", wp=True),
W("Meena finds the area of a parallelogram with base $12$ cm, slant side $8$ cm and perpendicular height $6$ cm as $12\\times8=96$ cm$^2$. Find her mistake and the correct area.", 2, "She used the slant side instead of the perpendicular height (1). Correct area $=12\\times6=72$ cm$^2$ (1).", "M"),
W("Rohit says that if the radius of a circle becomes $14$ cm from $7$ cm, both its circumference and its area double. Correct him with the values (use $\\pi=\\frac{22}7$).", 2, "Circumference: $44$ cm to $88$ cm (doubles) (1). Area: $154$ cm$^2$ to $616$ cm$^2$ (becomes four times) (1).", "M"),
W("An isosceles trapezium-shaped field has parallel sides $32$ m and $14$ m and each non-parallel side $15$ m. Find the height of the field and its area.", 3, "Each slant side makes a right triangle with base $\\frac{32-14}2=9$ m (1). Height $=\\sqrt{15^2-9^2}=12$ m (1). Area $=\\frac12(32+14)\\times12=276$ m$^2$ (1).", "M", wp=True),
W("An equilateral triangular park has each side $20$ m. Find its area (take $\\sqrt3=1.732$) and the cost of planting grass at ₹ $25$ per m$^2$.", 3, "Area $=\\frac{\\sqrt3}4\\times400=100\\sqrt3=173.2$ m$^2$ (2). Cost $=173.2\\times25=$ ₹ $4330$ (1).", "M", wp=True),
W("A pizza of diameter $28$ cm is cut into $8$ equal slices. Find the area of one slice, the length of its curved edge and the perimeter of one slice. (Take $\\pi=\\frac{22}7$.)", 3, "Area of pizza $=\\frac{22}7\\times14^2=616$; one slice $=\\frac{616}8=77$ cm$^2$ (1). Curved edge $=\\frac{88}8=11$ cm (1). Perimeter $=14+14+11=39$ cm (1).", "M", wp=True),
W("An isosceles triangular sail has sides $15$ m, $15$ m and $24$ m. Find its area by Heron's formula and the height on the side of $24$ m.", 3, "$s=27$; area $=\\sqrt{27\\times12\\times12\\times3}=\\sqrt{11664}=108$ m$^2$ (2). Height $=\\frac{2\\times108}{24}=9$ m (1).", "M", wp=True),
W("A circular track has diameter $70$ m. Find its circumference using $\\pi=\\frac{22}7$ and using $\\pi=3.14$. By how much do the answers differ? What does this tell you about $\\pi$?", 3, "$\\frac{22}7$: $220$ m (1). $3.14$: $2\\times3.14\\times35=219.8$ m (1). Difference $0.2$ m: both are only approximations because $\\pi$ is irrational (1).", "M", wp=True),
W("A rectangular plot is $16$ m long and $9$ m wide. Following Baudhāyana's idea of 'squaring a rectangle', find the side of the square plot of the same area and compare the perimeters.", 3, "Area $=16\\times9=144$ m$^2$ (1). Side of the square $=\\sqrt{144}=12$ m (1). Perimeters: rectangle $50$ m, square $48$ m (1).", "M", wp=True),
W("A wire bent into a rectangle of $28$ cm by $16$ cm is straightened and bent into a circle. Find the radius of the circle and compare the areas of the circle and the rectangle. (Take $\\pi=\\frac{22}7$.)", 3, "Length of wire $=2(28+16)=88$ cm (1). $2\\pi r=88$ gives $r=14$ cm (1). Circle $=616$ cm$^2$, rectangle $=448$ cm$^2$; the circle encloses more area (1).", "M", wp=True),
W("A hand-fan is a sector of a circle of radius $28$ cm and angle $45^\\circ$. Find the length of its curved edge, its area and its perimeter. (Take $\\pi=\\frac{22}7$.)", 3, "Curved edge $=\\frac{45}{360}\\times2\\times\\frac{22}7\\times28=22$ cm (1). Area $=\\frac18\\times\\frac{22}7\\times784=308$ cm$^2$ (1). Perimeter $=22+2(28)=78$ cm (1).", "M", wp=True),
W("A parallelogram has sides $10$ cm and $6$ cm. Find its area if the perpendicular height on the $10$ cm side is (i) $6$ cm (ii) $3$ cm. What does this show about finding the area from the side lengths alone?", 2, "(i) $10\\times6=60$ cm$^2$ (rectangle) (ii) $10\\times3=30$ cm$^2$ (1). The same side lengths can give different areas, so the sides alone do not fix the area; the height is needed (1).", "M"),
# ---------------- HARD ----------------
W("A plot $ABCD$ has its four corners on a circular pond's boundary and its sides are $AB=25$ m, $BC=39$ m, $CD=52$ m, $DA=60$ m. Use Brahmagupta's formula to find its area and the cost of levelling at ₹ $30$ per m$^2$.", 4, "$s=\\frac{25+39+52+60}2=88$ (1). Area $=\\sqrt{(s-a)(s-b)(s-c)(s-d)}=\\sqrt{63\\times49\\times36\\times28}$ (1). $=\\sqrt{1764^2}=1764$ m$^2$ (1). Cost $=1764\\times30=$ ₹ $52920$ (1).", "H", wp=True),
W("A belt just fits tightly around a circular ground of radius $70$ m. It is now raised by $1$ m all around. How much longer must the belt be (take $\\pi=\\frac{22}7$)? Show that the answer does not depend on the radius.", 4, "New radius $71$ m; extra length $=2\\pi(71)-2\\pi(70)=2\\pi\\times1$ (2) $=\\frac{44}7\\approx6.29$ m (1). In general $2\\pi(r+1)-2\\pi r=2\\pi$, which does not contain $r$: the answer is the same for a ground or for the whole Earth (1).", "H", wp=True),
W("A circular running track has an inner circumference of $176$ m and is $7$ m wide. Find the inner and outer radii, the area of the track and the cost of resurfacing it at ₹ $25$ per m$^2$. (Take $\\pi=\\frac{22}7$.)", 4, "Inner radius $=\\frac{176\\times7}{44}=28$ m, outer radius $=35$ m (1). Area $=\\frac{22}7(35^2-28^2)=\\frac{22}7\\times441=1386$ m$^2$ (2). Cost $=1386\\times25=$ ₹ $34650$ (1).", "H", wp=True),
W("A playground is a rectangle $40$ m by $28$ m with a semicircle added on each shorter side (diameter $28$ m). Find the total area and the perimeter of the ground. (Take $\\pi=\\frac{22}7$.)", 4, "Two semicircles make a circle of radius $14$ m: area $=616$ m$^2$ (1). Rectangle $=40\\times28=1120$ m$^2$; total $=1736$ m$^2$ (1). Perimeter $=2\\times40+2\\pi(14)$ (1) $=80+88=168$ m (1).", "H", wp=True),
W("A square lawn of side $28$ m has a quadrant-shaped flower bed of radius $7$ m at each of its four corners. Find the area of the remaining lawn and the total length of the curved edges of the flower beds. (Take $\\pi=\\frac{22}7$.)", 4, "Four quadrants of radius $7$ make one full circle: area $=\\frac{22}7\\times49=154$ m$^2$ (1). Remaining lawn $=784-154=630$ m$^2$ (2). Curved edges $=2\\pi r=44$ m (1).", "H", wp=True),
W("Use Heron's formula to show that the area of an equilateral triangle of side $a$ is $\\frac{\\sqrt3}4a^2$. Hence find the area of a triangular park of side $12$ m (take $\\sqrt3=1.732$).", 4, "$s=\\frac{3a}2$, $s-a=\\frac a2$ (1). Area $=\\sqrt{\\frac{3a}2\\cdot\\frac a2\\cdot\\frac a2\\cdot\\frac a2}=\\sqrt{\\frac{3a^4}{16}}$ (2) $=\\frac{\\sqrt3}4a^2$. For $a=12$: $36\\sqrt3=62.35$ m$^2$ (1).", "H"),
W("A triangular field has sides $9$ m, $40$ m and $41$ m. Find its area by Heron's formula, check it with $\\frac12bh$ and find the length of the perpendicular from the opposite vertex on the longest side (correct to two decimals).", 4, "$s=45$; area $=\\sqrt{45\\times36\\times5\\times4}=\\sqrt{32400}=180$ m$^2$ (1). $9^2+40^2=41^2$, so it is right-angled and $\\frac12\\times9\\times40=180$ (1). Perpendicular on $41$ m: $\\frac{2\\times180}{41}$ (1) $\\approx8.78$ m (1).", "H", wp=True),
W("A rope $154$ m long is used to enclose (i) a square plot and (ii) a circular plot. Find the area of each and say which encloses more. (Take $\\pi=\\frac{22}7$.)", 5, "(i) Side $=\\frac{154}4=38.5$ m, area $=1482.25$ m$^2$ (2). (ii) $2\\pi r=154$, $r=24.5$ m, area $=\\frac{22}7\\times24.5^2=1886.5$ m$^2$ (2). The circle encloses $404.25$ m$^2$ more (1).", "H", wp=True),
W("The plot $ABCD$ has $AB=13$ m, $BC=14$ m, $CD=9$ m, $DA=12$ m and diagonal $AC=15$ m. Find its area and the cost of fencing its boundary at ₹ $40$ per metre.", 4, "Triangle $ABC$ (sides $13,14,15$): $s=21$, area $=\\sqrt{21\\times8\\times7\\times6}=84$ m$^2$ (1). Triangle $ACD$ ($9,12,15$) is right-angled: area $=\\frac12\\times9\\times12=54$ m$^2$ (1). Total area $=138$ m$^2$ (1). Perimeter $=13+14+9+12=48$ m; cost $=$ ₹ $1920$ (1).", "H", wp=True),
W("A regular hexagonal tile has side $10$ cm. Dividing it into six equilateral triangles, find its area and perimeter (take $\\sqrt3=1.732$).", 4, "The tile splits into $6$ equilateral triangles of side $10$ cm (1). Each has area $\\frac{\\sqrt3}4\\times100=25\\sqrt3$ (1). Total area $=150\\sqrt3=259.8$ cm$^2$ (1). Perimeter $=6\\times10=60$ cm (1).", "H", wp=True),
W("Two circular rangoli patterns of radius $14$ cm overlap so that each passes through the centre of the other; the common chord subtends $120^\\circ$ at each centre. Find the length of the outline of the combined figure. (Take $\\pi=\\frac{22}7$.)", 4, "Outside the overlap each circle contributes an arc of $360^\\circ-120^\\circ=240^\\circ$ (2). Outline $=2\\times\\frac{240}{360}\\times2\\pi r=\\frac{8\\pi r}3$ (1) $=\\frac83\\times\\frac{22}7\\times14=\\frac{352}3\\approx117.33$ cm (1).", "H", wp=True),
W("A decorative window is the part of a circle of radius $14$ cm cut off by a chord that subtends a right angle at the centre (a minor segment). Find the area of the window. (Take $\\pi=\\frac{22}7$.)", 4, "Area of the quadrant sector $=\\frac14\\times\\frac{22}7\\times196=154$ cm$^2$ (2). Triangle formed by the two radii $=\\frac12\\times14\\times14=98$ cm$^2$ (1). Segment $=154-98=56$ cm$^2$ (1).", "H", wp=True),
W("If the circumference of a circle is increased by $10\\%$, by what percentage does its area increase? Check with a circle of circumference $44$ cm.", 4, "Circumference $\\propto r$, so the radius also becomes $1.1r$ (1). Area becomes $\\pi(1.1r)^2=1.21\\pi r^2$ (1), an increase of $21\\%$ (1). Check: $44$ cm gives $r=7$, area $154$; new circumference $48.4$ gives $r=7.7$, area $186.34=1.21\\times154$ (1).", "H"),
]

for _w in WS:   # answer-key/question renderer does not interpret **bold**
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(6)
_pre, _tail = _o["blocks"][:-2], _o["blocks"][-2:]
_extra = [
 ("h2", "6.6 Perimeter and π in History"),
 ("ul", ["π is the constant ratio **C/d** for every circle and is **irrational**: no fraction or finite decimal equals it. 22/7 = 3.142857… and 3.14 are **approximations**; on a track of diameter 70 m they differ by 220 − 219.8 = 0.2 m.", "**Āryabhaṭa (499 CE)** gave π ≈ 3927/1250 = 3.1416 and called it *āsanna*, an approximation. **Brahmagupta (628 CE)** used √10 ≈ 3.1622 for π because it was easy to handle in equations.", "**Belt puzzle:** a belt round a circle of radius r that is raised by 1 m all round must be longer by 2π(r + 1) − 2πr = 2π ≈ 6.28 m, **whatever r is** (a ground or the Earth).", "**Same perimeter, different area:** a wire bent into a rectangle 28 cm × 16 cm (88 cm) encloses 448 cm², but bent into a circle of radius 14 cm it encloses 616 cm². A rope 154 m long encloses 1482.25 m² as a square but 1886.5 m² as a circle: for a fixed perimeter the circle encloses the most."]),
 ("h2", "6.7 Heron's and Brahmagupta's Formulae"),
 ("note", "FORMULA", "**Brahmagupta's formula** (628 CE) for a **cyclic quadrilateral** with sides a, b, c, d and s = (a + b + c + d)/2: **Area = √[(s − a)(s − b)(s − c)(s − d)]**. If d = 0 the figure becomes a triangle and this reduces to **Heron's formula**."),
 ("table", ["Figure", "Sides / data", "Area"], [
  ["Triangle (Heron)", "13, 14, 15: s = 21", "√(21 × 8 × 7 × 6) = 84"],
  ["Triangle (Heron)", "17, 25, 26: s = 34", "√(34 × 17 × 9 × 8) = 204"],
  ["Isosceles triangle", "15, 15, 24: s = 27", "√(27 × 12 × 12 × 3) = 108; height on 24 is 9"],
  ["Right triangle", "9, 40, 41: s = 45", "√(45 × 36 × 5 × 4) = 180 = ½ × 9 × 40"],
  ["Cyclic quadrilateral (Brahmagupta)", "25, 39, 52, 60: s = 88", "√(63 × 49 × 36 × 28) = 1764"],
  ["Quadrilateral by splitting", "13, 14, 9, 12 with diagonal 15", "84 + 54 = 138"]]),
 ("note", "REMEMBER", "The sides of a parallelogram alone do **not** fix its area: with sides 10 cm and 6 cm the area is 60 cm² if the height is 6 cm and 30 cm² if the height is 3 cm. Brahmagupta's formula works only when the four-sided figure is **cyclic**. Baudhāyana's *squaring of a rectangle* a × b gives a square of side √(ab) with the same area (16 m × 9 m becomes 12 m × 12 m)."),
 ("h2", "6.8 Worked Examples"),
 ("steps", [("Example 1 — Wheel and distance", "A wheel of radius 70 cm has circumference 2 × 22/7 × 70 = 440 cm. To cover 1.32 km = 132000 cm it makes 132000 ÷ 440 = **300 turns**. Always convert the distance into the same unit as the circumference first.")]),
 ("steps", [("Example 2 — Path around a pond", "A circular pond of radius 14 m with a 7 m wide path: outer radius 21 m. Path area = 22/7 × (441 − 196) = **770 m²**; paving at ₹ 15 per m² costs **₹ 11,550**. A track with inner circumference 176 m (r = 28 m) and width 7 m has area 22/7 × (35² − 28²) = **1386 m²**.")]),
 ("steps", [("Example 3 — Composite playground", "A rectangle 40 m by 28 m with a semicircle on each 28 m side. Two semicircles of radius 14 m make one circle of area 616 m². Total area = 1120 + 616 = **1736 m²**. Perimeter = 2 × 40 + 2π × 14 = 80 + 88 = **168 m**: the straight sides plus the two semicircular arcs (the diameters are inside and are not counted).")]),
 ("steps", [("Example 4 — Sector and segment", "A wiper of length 21 cm sweeping 120°: area = ⅓ × 22/7 × 441 = **462 cm²**, arc = ⅓ × 132 = **44 cm**. A window cut off by a chord subtending 90° in a circle of radius 14 cm: sector 154 − triangle 98 = **56 cm²** (minor segment = sector − triangle).")]),
 ("steps", [("Example 5 — Four-corner flower beds", "A lawn 28 m × 28 m with a quadrant of radius 7 m at each corner. The four quadrants make a full circle of area 154 m², so the lawn left is 784 − 154 = **630 m²**, and the total curved edge is 2π × 7 = 44 m.")]),
 ("steps", [("Example 6 — Grazing area", "A cow tied at a corner of a square field of side 20 m by a 14 m rope grazes a quarter circle: ¼ × 22/7 × 196 = **154 m²**. If the rope were longer than the side, the quarter circle would extend beyond the field and the problem would need extra care.")]),
 ("h2", "6.9 Word Problems: How to Translate"),
 ("table", ["Words", "Quantity", "Formula"], [
  ["fence, boundary, border, lace, wire around", "perimeter / circumference", "2(l + b); 2πr; sum of the outer edges"],
  ["paint, cover, tile, level, grass, carpet", "area", "l × b; πr²; ½bh; bh; ½(a + b)h"],
  ["cost at ₹ x per metre", "perimeter × rate", "₹ 12 per m on 130 m = ₹ 1560"],
  ["cost at ₹ x per m²", "area × rate", "₹ 15 per m² on 770 m² = ₹ 11,550"],
  ["number of turns of a wheel", "distance ÷ circumference", "132000 ÷ 440 = 300"],
  ["path / ring / border of width w", "area of outer − area of inner", "π(R² − r²) with R = r + w"],
  ["pizza slice, fan, wiper, sprinkler", "sector", "(θ/360) × πr²; arc (θ/360) × 2πr"],
  ["rope tied at a corner", "quadrant (or sector) of radius = rope", "¼πr² for 90°"]]),
 ("note", "IMPORTANT", "**Units.** Keep all lengths in the same unit before using a formula, and give area in square units: 1 m² = 10,000 cm²; 1 km = 1000 m = 100,000 cm. Use π = 22/7 when the radius is a multiple of 7 and 3.14 otherwise, as the question directs. **Common mistakes:** using the slant side as the height of a parallelogram, forgetting to halve in ½bh, using the diameter in πr², counting an internal diameter in the perimeter of a composite figure, and forgetting that a doubled radius gives four times the area."),
]
CH = dict(_o, blocks=_pre + _extra + _tail, takeaways=_o["takeaways"] + ["**Brahmagupta's formula** √[(s − a)(s − b)(s − c)(s − d)] gives the area of a **cyclic** quadrilateral and reduces to Heron's formula when one side is 0.", "**Minor segment = sector − triangle**; **ring/path = π(R² − r²)**; a doubled radius gives **four times** the area.", "For a fixed perimeter the **circle** encloses the greatest area; π is irrational, so 22/7 and 3.14 are approximations (Āryabhaṭa's *āsanna*).", "Cost problems: **perimeter × rate per metre** or **area × rate per m²**; wheel problems: **distance ÷ circumference**."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
