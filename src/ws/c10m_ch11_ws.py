"""Class 10 Maths Ch 11 - Areas Related to Circles: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import isclose
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch11"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

P = 22 / 7
assert isclose(2 * P * 7, 44) and isclose(P * 49, 154) and isclose(P * 441 / 6, 231) and isclose(2 * P * 14 / 4, 22)
assert isclose(P * 14**2 / 8, 77) and isclose(P * (21**2 - 14**2), 770) and isclose(P * 14**2 / 2, 308)
assert isclose(P * 14**2 / 4, 154) and isclose(2 * P * 21 / 6, 22) and isclose(2 * P * 14 * 100 / 100, 88) and isclose(2 * P * 21 * 100 / 100, 132)
assert isclose(3.14 * 100 / 4 - 50, 28.5) and isclose(2 * P * 21**2 / 3, 924) and isclose(P * 21**2 / 3, 462)
assert isclose(P * (42**2 - 35**2), 1694) and 1694 * 20 == 33880 and isclose(P * 28**2 - 0 , 2464) and 28**2 - 154 == 630 and 14**2 - 154 == 42
assert isclose(P * 21**2 / 12, 115.5) and isclose(2 * P * 21 / 12, 11) and isclose(P * 14**2 / 2, 308) and isclose(P * (14**2 - 7**2), 462)
assert isclose(P * 21**2 / 4, 346.5) and isclose(P * (28**2 - 21**2) / 4, 269.5) and isclose(1100 / 2.2, 500) and isclose(2 * P * 42 / 12, 22)
assert isclose(P * 21**2 / 6, 231) and isclose(P * 21**2 - 231, 1155) and isclose(2 * 40 + 2 * P * 7, 124) and isclose(2 * P * 21, 132)
assert isclose(P * 21**2, 1386) and isclose(3.14 * 144 / 6 - 36 * 1.73, 13.08) and isclose(3.14 * 36 / 2, 56.52)
assert isclose(36 * 1.73 - 56.52, 5.76) and isclose(3.14 * 25 / 4, 19.625) and isclose(3.14 * 100 / 4 - 19.625, 58.875)
assert isclose(P * 14**2 - 6 * 49 * 1.73, 107.38) and 66000 / 60 * 10 / 2.2 == 5000 and isclose(2 * P * 14 / 4 + 28, 50)
assert isclose(P * 7**2 * 2, 308) and isclose(P * 98 - 196, 112) and isclose(3.14 * 100 / 2 - 100, 57) and isclose(P * 35**2, 3850)
assert isclose(2 * P * 42, 264) and 264 * 50 == 13200 and 1694 * 10 == 16940 and 77 - 35 == 42 and P * (42**2 - 35**2) == 1694
assert isclose(P * 7**2 * 2, 308) and isclose(2 * P * 14 + 0, 88) and 3 * 14 / 2 == 21

WS = [
# ---------------- EASY ----------------
W(r"The circumference of a circle of radius 7 cm is (take $\pi=\frac{22}7$):", 1, r"(b) 44 cm. $2\pi r=2\times\dfrac{22}7\times7=44$ cm. (1)", "E", opts=["22 cm", "44 cm", "154 cm", "49 cm"]),
W(r"The area of a circle of diameter 14 cm is (take $\pi=\frac{22}7$):", 1, r"(c) 154 cm². Radius 7 cm, so area $=\dfrac{22}7\times49=154$ cm². (1)", "E", opts=["44 cm²", "616 cm²", "154 cm²", "308 cm²"]),
W(r"The area of a sector of angle $60^\circ$ in a circle of radius 21 cm is (take $\pi=\frac{22}7$):", 1, r"(b) 231 cm². $\dfrac{60}{360}\times\dfrac{22}7\times441=\dfrac{1386}6=231$ cm². (1)", "E", opts=["462 cm²", "231 cm²", "132 cm²", "1386 cm²"]),
W(r"The length of the arc of a quadrant (angle $90^\circ$) of a circle of radius 14 cm is (take $\pi=\frac{22}7$):", 1, r"(a) 22 cm. $\dfrac{90}{360}\times2\times\dfrac{22}7\times14=\dfrac{88}4=22$ cm. (1)", "E", opts=["22 cm", "44 cm", "88 cm", "11 cm"]),
W(r"The circumference of a circle is 88 cm. Its radius is (take $\pi=\frac{22}7$):", 1, r"(c) 14 cm. $2\pi r=88\Rightarrow r=\dfrac{88\times7}{2\times22}=14$ cm. (1)", "E", opts=["7 cm", "28 cm", "14 cm", "44 cm"]),
W(r"The perimeter of a semicircle of radius 7 cm (including its diameter) is (take $\pi=\frac{22}7$):", 1, r"(d) 36 cm. Arc $=\pi r=22$ cm and diameter $=14$ cm, total $36$ cm. (1)", "E", opts=["22 cm", "44 cm", "29 cm", "36 cm"]),
W(r"The angle through which the minute hand of a clock turns in 10 minutes is:", 1, r"(b) $60^\circ$. In 60 minutes it turns $360^\circ$, so in 10 minutes $60^\circ$. (1)", "E", opts=[r"$30^\circ$", r"$60^\circ$", r"$90^\circ$", r"$120^\circ$"]),
W(r"A circular park has diameter 28 m. A fence is to be put along its boundary at ₹ 15 per metre. Find the cost. (Take $\pi=\frac{22}7$)", 2, r"Circumference $=\pi d=\dfrac{22}7\times28=88$ m (1). Cost $=88\times15=$ ₹ 1,320 (1).", "E", wp=True),
W(r"The wheel of a cart has diameter 42 cm. How far does the cart move in 100 complete revolutions? (Take $\pi=\frac{22}7$)", 2, r"One revolution $=\pi d=\dfrac{22}7\times42=132$ cm (1). $100$ revolutions $=13200$ cm $=132$ m (1).", "E", wp=True),
W(r"Find the area of the sector of a circle of radius 14 cm and angle $45^\circ$. (Take $\pi=\frac{22}7$)", 2, r"Area $=\dfrac{45}{360}\times\dfrac{22}7\times14^2=\dfrac18\times616$ (1) $=77$ cm² (1).", "E"),
W(r"Find the length of the arc of a sector of radius 21 cm and angle $60^\circ$. (Take $\pi=\frac{22}7$)", 2, r"Arc $=\dfrac{60}{360}\times2\times\dfrac{22}7\times21=\dfrac{132}6$ (1) $=22$ cm (1).", "E"),
W(r"A round pizza of radius 14 cm is cut into 8 equal slices. Find the area of one slice. (Take $\pi=\frac{22}7$)", 2, r"Area of the pizza $=\dfrac{22}7\times196=616$ cm² (1). One slice $=\dfrac{616}8=77$ cm² (1).", "E", wp=True),
W(r"A cow is tied with a 14 m rope at the corner of a large rectangular field. Find the area of the field it can graze (the rope can sweep a quadrant). (Take $\pi=\frac{22}7$)", 2, r"The corner angle is $90^\circ$, so the grazed region is a quadrant (1). Area $=\dfrac14\times\dfrac{22}7\times196=154$ m² (1).", "E", wp=True),
W(r"A circular lawn of radius 14 m has a 7 m wide circular path around it. Find the area of the path. (Take $\pi=\frac{22}7$)", 2, r"Outer radius $=21$ m (½). Area $=\pi(21^2-14^2)=\dfrac{22}7\times245$ (1) $=770$ m² (½).", "E", wp=True),
W(r"True or false? Give a reason. If the radius of a circle is doubled, its area is also doubled.", 2, r"**False** (1). Area $=\pi r^2$; with $2r$ the area is $\pi(2r)^2=4\pi r^2$, i.e. **four times** (1).", "E"),
W(r"The minute hand of a clock is 14 cm long. Find the area swept by it in 30 minutes. (Take $\pi=\frac{22}7$)", 2, r"In 30 minutes it turns $180^\circ$, a semicircle (1). Area $=\dfrac12\times\dfrac{22}7\times196=308$ cm² (1).", "E", wp=True),
W(r"Find the perimeter of a quadrant of a circle of radius 7 cm. (Take $\pi=\frac{22}7$)", 2, r"Arc $=\dfrac14\times2\pi r=11$ cm (1). Perimeter $=11+7+7=25$ cm (1).", "E"),
# ---------------- MEDIUM ----------------
W(r"A chord of a circle of radius 10 cm subtends a right angle at the centre. Find the area of the corresponding minor segment. (Take $\pi=3.14$)", 3, r"Sector $=\dfrac14\times3.14\times100=78.5$ cm² (1). Triangle $=\dfrac12\times10\times10=50$ cm² (1). Segment $=78.5-50=28.5$ cm² (1).", "M"),
W(r"Each of two windscreen wipers of a car has a blade 21 cm long and sweeps through an angle of $120^\circ$. Find the total area cleaned by the two blades in one sweep. (Take $\pi=\frac{22}7$; treat each as a sector)", 3, r"Area of one sector $=\dfrac{120}{360}\times\dfrac{22}7\times441=\dfrac{1386}3=462$ cm² (2). Two blades $=924$ cm² (1).", "M", wp=True),
W(r"A brooch is made with silver wire in the form of a circle of diameter 35 mm. The wire is also used to make 5 diameters which divide the circle into 10 equal sectors. Find the total length of silver wire required. (Take $\pi=\frac{22}7$)", 3, r"Circumference $=\dfrac{22}7\times35=110$ mm (1). Five diameters $=5\times35=175$ mm (1). Total $=110+175=285$ mm (1).", "M", wp=True),
W(r"A circular running track has inner radius 35 m and is 7 m wide throughout. Find the area of the track and the cost of laying a synthetic surface at ₹ 20 per m². (Take $\pi=\frac{22}7$)", 3, r"Outer radius $=42$ m (½). Area $=\dfrac{22}7(42^2-35^2)=\dfrac{22}7\times539$ (1) $=1694$ m² (1). Cost $=1694\times20=$ ₹ 33,880 (½).", "M", wp=True),
W(r"A circle is inscribed in a square of side 14 cm. Find the area of the region of the square that lies outside the circle. (Take $\pi=\frac{22}7$)", 2, r"Radius of circle $=7$ cm, area $=154$ cm² (1). Required area $=196-154=42$ cm² (1).", "M"),
W(r"A square carpet of side 28 cm has a quarter-circle of radius 7 cm cut off from each of its four corners for a design. Find the area of the remaining carpet. (Take $\pi=\frac{22}7$)", 3, r"Four quadrants of radius 7 together make one full circle: area $=\dfrac{22}7\times49=154$ cm² (2). Remaining area $=28^2-154=784-154=630$ cm² (1).", "M", wp=True),
W(r"The minute hand of a wall clock is 21 cm long. Find (i) the area swept in 5 minutes and (ii) the distance moved by its tip in 5 minutes. (Take $\pi=\frac{22}7$)", 3, r"In 5 minutes the hand turns $30^\circ$ (1). (i) Area $=\dfrac{30}{360}\times\dfrac{22}7\times441=115.5$ cm² (1). (ii) Arc $=\dfrac{30}{360}\times2\times\dfrac{22}7\times21=11$ cm (1).", "M", wp=True),
W(r"A semicircular plot of land has diameter 28 m. Find its perimeter and its area. (Take $\pi=\frac{22}7$)", 3, r"Radius $=14$ m. Arc $=\pi r=44$ m, perimeter $=44+28=72$ m (1,1). Area $=\dfrac12\pi r^2=\dfrac12\times\dfrac{22}7\times196=308$ m² (1).", "M", wp=True),
W(r"Sita finds the length of the arc of a sector of radius 21 cm and angle $60^\circ$ as $\dfrac{60}{360}\times\pi\times21^2$. What is her mistake? Find the correct length. (Take $\pi=\frac{22}7$)", 2, r"She used the formula for the **area** ($\theta/360\times\pi r^2$) instead of the arc length $\dfrac\theta{360}\times2\pi r$ (1). Correct arc $=\dfrac16\times2\times\dfrac{22}7\times21=22$ cm (1).", "M"),
W(r"The area of a sector of a circle of radius 21 cm is 154 cm². Find the angle of the sector. (Take $\pi=\frac{22}7$)", 2, r"$\dfrac\theta{360}\times\dfrac{22}7\times441=154$ gives $\dfrac\theta{360}\times1386=154$ (1). $\theta=\dfrac{154\times360}{1386}=40^\circ$ (1).", "M"),
W(r"A sector of a circle of radius 14 cm has an arc length of 22 cm. Find the angle of the sector. (Take $\pi=\frac{22}7$)", 2, r"Circumference $=88$ cm. $\dfrac\theta{360}\times88=22$ (1). $\theta=90^\circ$ (1).", "M"),
W(r"A horse is tied with a 21 m rope to a peg at one corner of a large square field. Find the area it can graze. If the rope is lengthened to 28 m, find the increase in the grazing area. (Take $\pi=\frac{22}7$)", 3, r"Area with 21 m $=\dfrac14\times\dfrac{22}7\times441=346.5$ m² (1). Area with 28 m $=\dfrac14\times\dfrac{22}7\times784=616$ m² (1). Increase $=616-346.5=269.5$ m² (1).", "M", wp=True),
W(r"Find the area of a ring (annulus) between two concentric circles of radii 14 cm and 7 cm. (Take $\pi=\frac{22}7$)", 2, r"Area $=\pi(R^2-r^2)=\dfrac{22}7(196-49)$ (1) $=\dfrac{22}7\times147=462$ cm² (1).", "M"),
W(r"A circular tablecloth has radius 35 cm. Lace is to be sewn along its edge at ₹ 0.50 per cm. Find the cost of the lace. (Take $\pi=\frac{22}7$)", 2, r"Edge $=2\pi r=2\times\dfrac{22}7\times35=220$ cm (1). Cost $=220\times0.50=$ ₹ 110 (1).", "M", wp=True),
W(r"The wheel of a bicycle has radius 35 cm. How many complete revolutions does it make to cover 1.1 km? (Take $\pi=\frac{22}7$)", 3, r"Circumference $=2\times\dfrac{22}7\times35=220$ cm $=2.2$ m (1,1). Revolutions $=\dfrac{1100}{2.2}=500$ (1).", "M", wp=True),
W(r"A pendulum of length 42 cm swings through an angle of $30^\circ$. Find the distance covered by the tip of the pendulum in one swing. (Take $\pi=\frac{22}7$)", 2, r"The tip moves along an arc of a circle of radius 42 cm (1). Arc $=\dfrac{30}{360}\times2\times\dfrac{22}7\times42=22$ cm (1).", "M", wp=True),
W(r"A sector of a circle of radius 21 cm has angle $60^\circ$. Find the areas of the minor sector and the corresponding major sector. (Take $\pi=\frac{22}7$)", 3, r"Whole circle $=\dfrac{22}7\times441=1386$ cm² (1). Minor sector $=\dfrac{1386}6=231$ cm² (1). Major sector $=1386-231=1155$ cm² (1).", "M"),
W(r"A running track has two straight sides of 40 m each, joined at both ends by semicircles of radius 7 m. Find the length of one complete lap along the inner edge. (Take $\pi=\frac{22}7$)", 3, r"The two semicircles make one circle of radius 7 m: $2\pi r=44$ m (2). Lap $=2\times40+44=124$ m (1).", "M", wp=True),
W(r"The circumference of a circle is 132 cm. Find its area. (Take $\pi=\frac{22}7$)", 2, r"$2\pi r=132\Rightarrow r=21$ cm (1). Area $=\dfrac{22}7\times441=1386$ cm² (1).", "M"),
# ---------------- HARD ----------------
W(r"Find the area of the minor segment of a circle of radius 12 cm whose chord subtends an angle of $60^\circ$ at the centre. (Take $\pi=3.14$, $\sqrt3=1.73$)", 4, r"Sector $=\dfrac{60}{360}\times3.14\times144=75.36$ cm² (1). The triangle with the two radii and angle $60^\circ$ is equilateral with side 12: area $=\dfrac{\sqrt3}4\times144=36\sqrt3=62.28$ cm² (2). Segment $=75.36-62.28=13.08$ cm² (1).", "H"),
W(r"A chord of a circle of radius 21 cm subtends an angle of $120^\circ$ at the centre. Find the area of the minor segment. (Take $\pi=\frac{22}7$, $\sqrt3=1.73$)", 5, r"Sector $=\dfrac{120}{360}\times\dfrac{22}7\times441=462$ cm² (1). Draw $OM\perp$ chord: $\angle AOM=60^\circ$, so $OM=21\cos60^\circ=10.5$ cm and $AM=21\sin60^\circ=\dfrac{21\sqrt3}2$ (2). Triangle $OAB=\dfrac12\times AB\times OM=\dfrac12\times21\sqrt3\times10.5=110.25\sqrt3\approx190.73$ cm² (1). Segment $=462-190.73=271.27$ cm² (1).", "H"),
W(r"Three circles of radius 6 cm are drawn with centres at the vertices of an equilateral triangle of side 12 cm, so that each pair touches. Find the area of the part of the triangle not covered by the circles. (Take $\pi=3.14$, $\sqrt3=1.73$)", 4, r"Triangle area $=\dfrac{\sqrt3}4\times144=36\sqrt3=62.28$ cm² (1). Each circle covers a $60^\circ$ sector inside the triangle; three such sectors make a semicircle of radius 6 (1): $\dfrac12\times3.14\times36=56.52$ cm² (1). Uncovered area $=62.28-56.52=5.76$ cm² (1).", "H"),
W(r"A round table cover has six equal designs, each a segment bounded by a chord of the circle of radius 14 cm that subtends $60^\circ$ at the centre, i.e. the six chords form a regular hexagon. Find the total area of the six designs. (Take $\pi=\frac{22}7$, $\sqrt3=1.73$)", 4, r"Area of the circle $=\dfrac{22}7\times196=616$ cm² (1). The hexagon is six equilateral triangles of side 14: $6\times\dfrac{\sqrt3}4\times196=294\sqrt3=508.62$ cm² (2). Designs $=616-508.62=107.38$ cm² (1).", "H", wp=True),
W(r"A horse is tied to a peg at one corner of a square field of side 15 m by a rope 5 m long. Find the area of the part of the field it can graze. If the rope is replaced by one 10 m long, find the increase in the grazing area. (Take $\pi=3.14$)", 4, r"With 5 m: quadrant $=\dfrac14\times3.14\times25=19.625$ m² (1,1). With 10 m: $\dfrac14\times3.14\times100=78.5$ m² (1). Increase $=78.5-19.625=58.875$ m² (1).", "H", wp=True),
W(r"Semicircles are drawn **inside** a square of side 14 cm, one on each side as diameter. They overlap to form four petals, and together they cover the whole square. Find the total area of the four overlapping petals. (Take $\pi=\frac{22}7$)", 4, r"Radius of each semicircle $=7$ cm; the four semicircles have total area $4\times\dfrac12\times\dfrac{22}7\times49=308$ cm² (2). They cover the square of area 196 cm², and the overlap (petals) is counted twice, so petals $=308-196=112$ cm² (2).", "H"),
W(r"The diameter of a car wheel is 70 cm. How many complete revolutions does it make in 10 minutes when the car travels at 66 km/h? (Take $\pi=\frac{22}7$)", 3, r"Distance in 10 min $=\dfrac{66}{60}\times10=11$ km $=11000$ m (1). Circumference $=\dfrac{22}7\times70=220$ cm $=2.2$ m (1). Revolutions $=\dfrac{11000}{2.2}=5000$ (1).", "H", wp=True),
W(r"The perimeter of a sector of a circle of radius 14 cm is 50 cm. Find the angle of the sector and its area. (Take $\pi=\frac{22}7$)", 3, r"Arc $=50-2\times14=22$ cm (1). $\dfrac\theta{360}\times88=22$, $\theta=90^\circ$ (1). Area $=\dfrac14\times\dfrac{22}7\times196=154$ cm² (1).", "H"),
W(r"The areas of two circles are in the ratio $4:9$. (i) Find the ratio of their radii and their circumferences. (ii) If the smaller circle has circumference 44 cm, find the radius of the larger. (Take $\pi=\frac{22}7$)", 3, r"(i) $\dfrac{\pi r_1^2}{\pi r_2^2}=\dfrac49\Rightarrow\dfrac{r_1}{r_2}=\dfrac23$; circumferences are in the same ratio $2:3$ (1,1). (ii) $2\pi r_1=44\Rightarrow r_1=7$ cm, so $r_2=\dfrac32\times7=10.5$ cm (1).", "H"),
W(r"A circle is drawn around a square of side 14 cm so that it passes through all four corners. Find the area of the circle that lies outside the square. (Take $\pi=\frac{22}7$)", 3, r"The diagonal of the square is $14\sqrt2$, and it is the diameter, so $r=7\sqrt2$ cm (1). Area of circle $=\dfrac{22}7\times98=308$ cm² (1). Outside area $=308-196=112$ cm² (1).", "H"),
W(r"**Case study.** A circular park of radius 35 m has a 7 m wide circular footpath running around it on the outside. (Take $\pi=\frac{22}7$) (i) Find the area of the park. (ii) Find the area of the footpath. (iii) Find the cost of fencing the outer boundary of the path at ₹ 50 per metre. (iv) Find the cost of paving the path at ₹ 10 per m².", 5, r"(i) $\dfrac{22}7\times35^2=3850$ m² (1). (ii) Outer radius $=42$ m: $\dfrac{22}7(42^2-35^2)=1694$ m² (1). (iii) Outer circumference $=2\times\dfrac{22}7\times42=264$ m, cost $=264\times50=$ ₹ 13,200 (2). (iv) $1694\times10=$ ₹ 16,940 (1).", "H", wp=True),
W(r"Two quadrants of radius 10 cm are drawn inside a square $ABCD$ of side 10 cm, one with centre $A$ and the other with centre $C$. Find the area of the region common to both quadrants (the shaded lens). (Take $\pi=3.14$)", 4, r"Area of each quadrant $=\dfrac14\times3.14\times100=78.5$ cm² (1). Together they cover the whole square, and the lens is counted twice (1,1). Lens $=2\times78.5-100=57$ cm² (1).", "H"),
W(r"The area of a circular path of uniform width 7 m around a circular garden is 1694 m². Find the radius of the garden. (Take $\pi=\frac{22}7$)", 4, r"Let the radius of the garden be $r$; outer radius $=r+7$ (1). $\dfrac{22}7\left[(r+7)^2-r^2\right]=1694$ gives $(r+7)^2-r^2=539$ (1). $14r+49=539\Rightarrow 14r=490$ (1). $r=35$ m (1).", "H", wp=True),
W(r"The minute hand of a clock is 21 cm long. Find the area swept by it between 7:10 a.m. and 7:50 a.m., and the distance moved by its tip. (Take $\pi=\frac{22}7$)", 3, r"40 minutes $\Rightarrow\dfrac{40}{60}\times360^\circ=240^\circ$ (1). Area $=\dfrac{240}{360}\times\dfrac{22}7\times441=924$ cm² (1). Distance $=\dfrac23\times132=88$ cm (1).", "H", wp=True),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(11)
def _fix(o, a, b):
    """patch one string of the borrowed notes (exactly one hit required)"""
    hit = [0]
    def walk(x):
        if isinstance(x, str) and a in x: hit[0] += 1; return x.replace(a, b)
        if isinstance(x, (list, tuple)): return type(x)(walk(i) for i in x)
        return x
    out = dict(o, blocks=walk(o["blocks"])); assert hit[0] == 1, (a, hit); return out
_o = _fix(_o, "18.86 cm", "18.85 cm")
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "11.5 More Worked Examples"),
 ("h3", "Example 1 — Area of a minor segment (angle 60°)"),
 ("steps", [("Radius 12 cm, chord subtends 60° at the centre. Find the area of the minor segment (π = 3.14, √3 = 1.73)", "Segment = sector − triangle OAB."), ("Sector", "(60/360) × 3.14 × 144 = 75.36 cm²."), ("Triangle", "OA = OB and ∠AOB = 60°, so the triangle is equilateral with side 12: area = (√3/4) × 144 = 36√3 = 62.28 cm²."), ("Answer", "75.36 − 62.28 = **13.08 cm²**.")]),
 ("h3", "Example 2 — Area of a minor segment (angle 120°)"),
 ("steps", [("Radius 21 cm, ∠AOB = 120° (π = 22/7, √3 = 1.73)", "Sector = (120/360) × (22/7) × 441 = 462 cm²."), ("Triangle", "Drop OM ⟂ AB: ∠AOM = 60°, OM = 21 cos 60° = 10.5 and AM = 21 sin 60° = 21√3/2. Area = ½ × AB × OM = ½ × 21√3 × 10.5 = 110.25√3 ≈ 190.73 cm²."), ("Segment", "462 − 190.73 = **271.27 cm²**.")]),
 ("h3", "Example 3 — Shaded region of a combination"),
 ("steps", [("Square of side 28 cm; a quadrant of radius 7 cm is cut from each corner", "Four quadrants of the same radius together make one full circle."), ("Cut-out area", "(22/7) × 49 = 154 cm²."), ("Remaining", "28² − 154 = 784 − 154 = **630 cm²**.")]),
 ("h3", "Example 4 — Path around a circle"),
 ("steps", [("A circular track of inner radius 35 m is 7 m wide. Find its area and the cost at ₹ 20 per m²", "Outer radius R = 35 + 7 = 42 m."), ("Area of the ring", "π(R² − r²) = (22/7)(1764 − 1225) = (22/7) × 539 = 1694 m²."), ("Cost", "1694 × 20 = **₹ 33,880**.")]),
 ("h3", "Example 5 — Finding the width of a path"),
 ("steps", [("The path around a garden is 7 m wide and its area is 1694 m². Find the garden's radius", "Let radius = r; outer radius = r + 7."), ("Equation", "(22/7)[(r + 7)² − r²] = 1694, so (r + 7)² − r² = 539, i.e. 14r + 49 = 539."), ("Solve", "14r = 490, so r = **35 m**.")]),
 ("h3", "Example 6 — Clock and pendulum problems"),
 ("steps", [("Minute hand 21 cm, from 7:10 to 7:50", "40 minutes = (40/60) × 360° = 240°."), ("Area swept", "(240/360) × (22/7) × 441 = **924 cm²**."), ("Tip distance", "(240/360) × 2 × (22/7) × 21 = **88 cm**."), ("Pendulum 42 cm swinging through 30°", "The tip covers an arc = (30/360) × 2 × (22/7) × 42 = **22 cm**.")]),
 ("h2", "11.6 Word Problems: How to Translate"),
 ("table", ["Real-life words", "Maths idea", "Formula"], [
  ["fence/border/lace/boundary of a round object", "circumference (perimeter)", "2πr; cost = length × rate per metre"],
  ["carpet/paint/turf/cleaning/area covered", "area", "πr²; cost = area × rate per m²"],
  ["wheel moves how far in n turns; how many turns to cover a distance", "distance = n × circumference", "n = distance ÷ 2πr"],
  ["clock hand, wiper, pendulum, hinged door sweeps an angle", "sector (area swept) and arc (distance moved by the tip)", "(θ/360)πr² and (θ/360)2πr"],
  ["a rope tied at a corner of a field / a cow tethered", "quadrant (θ = 90°) or the angle of the corner", "¼πr²"],
  ["path/track/ring of width w around a circle", "area between two concentric circles", "π(R² − r²) with R = r + w"],
  ["pizza/cake slices", "equal sectors", "area of circle ÷ number of slices"]]),
 ("note", "IMPORTANT", "Minute hand: 60 minutes = 360°, so **1 minute = 6°**. Hour hand: 12 hours = 360°, so **1 hour = 30°**. Convert the time interval into an angle first."),
 ("h2", "11.7 Common Mistakes"),
 ("table", ["Mistake", "Why it is wrong", "Correct idea"], [
  ["Using the area formula for an arc length (or the reverse)", "length has one power of r, area has two", "arc = (θ/360)2πr; area = (θ/360)πr²"],
  ["Using diameter as radius", "formulas need r", "r = d/2; read ‘diameter’ carefully"],
  ["Ring area = π(R − r)²", "squares are taken separately", "π(R² − r²)"],
  ["Forgetting to subtract the triangle for a segment", "a sector is bigger than the segment", "segment = sector − triangle (minor)"],
  ["Mixing π = 22/7 and 3.14 in one question", "inconsistent answers", "use the value the question gives; 22/7 for multiples of 7"],
  ["Perimeter of a sector = arc length only", "the two radii are part of the boundary", "perimeter = arc + 2r"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["Convert **time to angle** first (1 minute = 6° for the minute hand) before using sector formulas.", "Path or ring of width w: area = **π(R² − r²)** with R = r + w; cost = area × rate.", "For a segment, **subtract the triangle** from the sector; for 60° the triangle is equilateral (√3/4 × side²).", "A tethered animal at a corner of a field grazes a **quadrant**; four quadrants of equal radius make one circle."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
