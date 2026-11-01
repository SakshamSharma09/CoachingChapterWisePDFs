from fractions import Fraction as F
from math import isqrt
from lib import mcq, Q, OR
from mk9 import M4, build
PI = F(22, 7)
def fm(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    v = float(x)
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s
def dist(vals, c):
    out = []
    for v in vals:
        if v != c and v > 0 and v not in out: out.append(v)
    return out
A = []; B = []; C = []; D = []
# circumference (5)
for r in [7, 14, 21, F(7, 2), 35]:
    c = 2*PI*r
    w = dist([c/2, c*2, PI*r*r, c+2, c-2], c)[:3]
    A.append(M4(f"Taking $\\pi=\\frac{{22}}7$, the circumference of a circle of radius ${fm(r)}$ cm is:", f"{fm(c)} cm", [f"{fm(x)} cm" for x in w], f"$2\\pi r=2\\times\\frac{{22}}7\\times{fm(r)}={fm(c)}$"))
# radius from circumference (4)
for c in [44, 88, 132, 66]:
    r = F(c)/(2*PI)
    w = dist([r*2, r/2, F(c)/PI, r+1, r-1], r)[:3]
    A.append(M4(f"The perimeter of a circle is ${c}$ cm. Taking $\\pi=\\frac{{22}}7$, its radius is:", f"{fm(r)} cm", [f"{fm(x)} cm" for x in w], f"$r=\\frac{{C}}{{2\\pi}}=\\frac{{{c}\\times7}}{{44}}={fm(r)}$"))
# arc length (6)
for r, t in [(21, 60), (21, 90), (14, 180), (7, 90), (14, 45), (42, 30)]:
    L = F(t, 360)*2*PI*r
    w = dist([L*2, L/2, 2*PI*r, L+2, L-1], L)[:3]
    A.append(M4(f"The length of an arc subtending ${t}^\\circ$ at the centre of a circle of radius ${r}$ cm ($\\pi=\\frac{{22}}7$) is:", f"{fm(L)} cm", [f"{fm(x)} cm" for x in w], f"$\\frac{{{t}}}{{360}}\\times2\\pi r={fm(L)}$"))
# Heron (6)
for a, b, c, ar in [(3, 4, 5, 6), (5, 12, 13, 30), (13, 14, 15, 84), (8, 15, 17, 60), (10, 17, 21, 84), (9, 10, 17, 36)]:
    s = F(a+b+c, 2); assert isqrt(int(s*(s-a)*(s-b)*(s-c))) == ar
    w = dist([ar+6, ar-6, a*b, ar*2, ar+12, ar//2 + 1], ar)[:3]
    A.append(M4(f"By Heron's formula, the area of a triangle with sides ${a}$ cm, ${b}$ cm and ${c}$ cm is:", f"{ar} cm$^2$", [f"{x} cm$^2$" for x in w], f"$s={fm(s)}$, area $=\\sqrt{{{fm(s)}\\cdot{fm(s-a)}\\cdot{fm(s-b)}\\cdot{fm(s-c)}}}={ar}$"))
# parallelogram (3) triangle (3)
for b, h in [(12, 7), (15, 8), (20, 9)]:
    ar = b*h
    A.append(M4(f"The area of a parallelogram with base ${b}$ cm and height ${h}$ cm is:", f"{ar} cm$^2$", [f"{ar//2} cm$^2$", f"{2*(b+h)} cm$^2$", f"{ar+b} cm$^2$"], "area $=bh$"))
for b, h in [(10, 7), (16, 9), (24, 5)]:
    ar = F(b*h, 2)
    A.append(M4(f"The area of a triangle with base ${b}$ cm and height ${h}$ cm is:", f"{fm(ar)} cm$^2$", [f"{b*h} cm$^2$", f"{b+h} cm$^2$", f"{fm(ar+b)} cm$^2$"], "area $=\\frac12bh$"))
# Brahmagupta (3)
for sides, ar in [((3, 4, 3, 4), 12), ((5, 5, 5, 5), 25), ((5, 5, 12, 12), 60)]:
    a, b, c, d = sides; s = F(sum(sides), 2)
    assert isqrt(int((s-a)*(s-b)*(s-c)*(s-d))) == ar
    A.append(M4(f"By Brahmagupta's formula, the area of a cyclic quadrilateral with sides ${a},{b},{c},{d}$ is:", f"{ar} sq. units", [f"{ar+4} sq. units", f"{ar-2} sq. units", f"{ar*2} sq. units"], f"$s={fm(s)}$; $\\sqrt{{(s-a)(s-b)(s-c)(s-d)}}={ar}$"))
# circle area (4)
for r in [7, 14, 21, F(7, 2)]:
    ar = PI*r*r
    A.append(M4(f"Taking $\\pi=\\frac{{22}}7$, the area of a circle of radius ${fm(r)}$ cm is:", f"{fm(ar)} cm$^2$", [f"{fm(2*PI*r)} cm$^2$", f"{fm(ar*2)} cm$^2$", f"{fm(ar/2)} cm$^2$"], f"$\\pi r^2=\\frac{{22}}7\\times{fm(r)}^2={fm(ar)}$"))
A += [
 M4("The ratio of the circumference of a circle to its diameter is:", r"the same for all circles ($\pi$)", ["different for different circles", "equal to 2", "equal to the radius"], "the C/D ratio is the constant $\\pi$"),
 M4("A median of a triangle divides it into two triangles of:", "equal area", ["equal perimeter", "equal angles", "one double the other"], "equal bases and the same height"),
 M4(r"The length of a semicircle of radius $r$ is:", r"$\pi r$", [r"$2\pi r$", r"$\frac{\pi r}{2}$", r"$\pi r^2$"], "half of $2\\pi r$"),
 M4(r"The area of an equilateral triangle of side $a$ is:", r"$\frac{\sqrt3}{4}a^2$", [r"$\frac{\sqrt3}{2}a^2$", r"$\frac{a^2}{2}$", r"$\sqrt3a^2$"], "Heron with $s=\\frac{3a}2$"),
 M4(r"In Heron's formula, $s$ stands for:", "the semi-perimeter of the triangle", ["the area of the triangle", "the longest side", "the perimeter"], "$s=\\frac{a+b+c}2$"),
 M4(r"Āryabhaṭa called his value $3.1416$ for $\pi$ ‘āsanna’, meaning:", "approximate (approaching)", ["exact", "wrong", "largest possible"], "he realised the ratio could not be exact"),
]
assert len(A) == 5+4+6+6+3+3+3+4+6 == 40, len(A)
# B (16)
B += [
 Q(r"The perimeter of a circle is 44 cm. Find its radius ($\pi=\frac{22}7$).", r"$2\pi r=44\Rightarrow r=\frac{44\times7}{2\times22}=7$ cm.", "1+1"),
 Q(r"Find, correct to 3 significant figures, the circumference of a circle of radius 10 cm ($\pi=\frac{22}7$).", r"$2\times\frac{22}7\times10=62.857\ldots\approx62.9$ cm.", "1+1"),
 Q(r"Find the length of the arc of a circle of radius 3.5 cm if the angle at the centre is $60^\circ$ ($\pi=\frac{22}7$).", r"$\frac{60}{360}\times2\times\frac{22}7\times3.5=\frac{11}3\approx3.67$ cm.", "1+1"),
 Q(r"Find the perimeter of a sector of a circle of radius 14 cm and sector angle $75^\circ$ ($\pi=\frac{22}7$).", r"Arc $=\frac{75}{360}\times2\times\frac{22}7\times14=\frac{55}3$ cm; perimeter $=\frac{55}3+14+14=\frac{139}3\approx46.3$ cm.", "1+1"),
 Q(r"The diameter of a car tyre is 56 cm. How far does the car travel in 100 complete revolutions of the tyre? ($\pi=\frac{22}7$)", r"Circumference $=\frac{22}7\times56=176$ cm; distance $=100\times176=17600$ cm $=176$ m.", "1+1"),
 Q(r"The perimeters of two circles are in the ratio 5 : 4. What is the ratio of their radii?", r"Perimeter $=2\pi r$, so the ratio of perimeters equals the ratio of radii: $5:4$.", "2"),
 Q(r"Find the perimeter of a semicircular plate of radius 7 cm (including the diameter). ($\pi=\frac{22}7$)", r"Arc $=\pi r=22$ cm; diameter $=14$ cm; perimeter $=36$ cm.", "1+1"),
 Q(r"Find the area of an equilateral triangle of side 8 cm using Heron's formula.", r"$s=12$; area $=\sqrt{12\times4\times4\times4}=\sqrt{768}=16\sqrt3\ \text{cm}^2$.", "1+1"),
 Q(r"Use Heron's formula to find the area of a triangle of sides 3 cm, 4 cm and 5 cm and verify with $\frac12bh$.", r"$s=6$; area $=\sqrt{6\times3\times2\times1}=6$ cm$^2$. Right-angled: $\frac12\times3\times4=6$ ✓", "1+1"),
 Q(r"The area of a parallelogram is 96 cm$^2$ and its base is 12 cm. Find its height.", r"$bh=96\Rightarrow h=\frac{96}{12}=8$ cm.", "1+1"),
 Q(r"In $\triangle ABC$ of area 48 cm$^2$, AD is a median. Find the area of $\triangle ABD$ and give the reason.", r"A median divides a triangle into two triangles of equal area (equal bases, same height): $\text{ar}(ABD)=24$ cm$^2$.", "1+1"),
 Q(r"Among all rectangles with perimeter 40 units, which has the greatest area? State that area.", r"The square with side 10 units; area $100$ sq. units (e.g. $9\times11=99<100$).", "1+1"),
 Q(r"An isosceles triangle has equal sides 5 cm and base 6 cm. Find its area.", r"Height $=\sqrt{25-9}=4$ cm; area $=\frac12\times6\times4=12$ cm$^2$.", "1+1"),
 Q(r"Find the area of a triangle with sides 7 cm, 15 cm and 20 cm.", r"$s=21$; area $=\sqrt{21\times14\times6\times1}=\sqrt{1764}=42$ cm$^2$.", "1+1"),
 Q(r"Why does an inscribed regular hexagon show that $\pi>3$?", r"The hexagon's perimeter is $6r=3\times(2r)=3D$, and the circle is longer than the polygon inside it, so $C>3D$, i.e. $\pi>3$.", "1+1"),
 Q(r"Find the perimeter of a quadrant (quarter-circle) of radius 14 cm, including the two radii. ($\pi=\frac{22}7$)", r"Arc $=\frac14\times2\times\frac{22}7\times14=22$ cm; perimeter $=22+28=50$ cm.", "1+1"),
]
assert len(B) == 16, len(B)
# C (24)
C += [
 Q(r"A track has two straight sections of 84.39 m each and two semicircular ends of radius 36.5 m. Find the length of the innermost edge (use $\pi=3.1416$).", r"Straights: $2\times84.39=168.78$ m (1). Two semicircles make one circle: $2\pi r=2\times3.1416\times36.5=229.34$ m (1). Total $\approx398.12$ m (1).", "1+1+1"),
 Q(r"The lanes on a circular bend are 1.2 m wide. By how much does the length of a full semicircular bend differ between two adjacent lanes (the stagger needed)? Use $\pi=3.14$.", r"Radius increases by 1.2 m (1). Two semicircles: extra distance $=2\pi\times1.2=2\times3.14\times1.2$ (1) $=7.536\approx7.54$ m (1).", "1+1+1"),
 Q(r"Two circles of radius $r$ each pass through the centre of the other. Find the perimeter of the shape formed by the outer arcs.", r"Triangle ABC (the centres and an intersection point) is equilateral, so $\angle CAD=120^\circ$ (1). Each outer arc is $240^\circ=\frac23$ of a circle (1). Perimeter $=2\times\frac23\times2\pi r=\frac{8\pi r}3$ (1).", "1+1+1"),
 Q(r"Semicircle $a$ on diameter PQ is compared with three semicircles $b,c,d$ on adjacent parts of PQ. Show that the two paths from P to Q are equal in length.", r"Radii $a',b',c',d'$. Path $a=\pi a'$; path $b+c+d=\pi(b'+c'+d')$ (1). $PQ=2a'=2b'+2c'+2d'\Rightarrow a'=b'+c'+d'$ (1). Hence the lengths are equal (1).", "1+1+1"),
 Q(r"Show, using inscribed and circumscribed hexagons of a circle of radius $r$, that $3<\pi<2\sqrt3$.", r"Inscribed hexagon perimeter $=6r<2\pi r$ ⇒ $\pi>3$ (1). Circumscribed hexagon has side $\frac{2r}{\sqrt3}$ (from Pythagoras with half-side $\frac r{\sqrt3}$) so perimeter $=\frac{12r}{\sqrt3}=4\sqrt3r>2\pi r$ ⇒ $\pi<2\sqrt3\approx3.46$ (2).", "1+2"),
 Q(r"Find the area of a triangle with sides 13 cm, 14 cm and 15 cm and the height on the side of 14 cm.", r"$s=21$; area $=\sqrt{21\times8\times7\times6}=84$ cm$^2$ (2). $\frac12\times14\times h=84\Rightarrow h=12$ cm (1).", "2+1"),
 Q(r"Find the length of the altitude on the shortest side of a triangle with sides 7 cm, 15 cm and 20 cm.", r"Area $=42$ cm$^2$ (Heron, $s=21$) (2). $\frac12\times7\times h=42\Rightarrow h=12$ cm (1).", "2+1"),
 Q(r"Prove that a median of a triangle divides it into two triangles of equal area.", r"In $\triangle ABC$ let $AD$ be the median, $BD=DC$ (1). $\triangle ABD$ and $\triangle ACD$ have the same height $h$ from $A$ (1). Areas $\frac12\cdot BD\cdot h=\frac12\cdot DC\cdot h$ — equal (1).", "1+1+1"),
 Q(r"Use Heron's formula to show that the area of an equilateral triangle of side $a$ is $\frac{\sqrt3}4a^2$.", r"$s=\frac{3a}2$, $s-a=\frac a2$ (1). Area $=\sqrt{\frac{3a}2\cdot\frac a2\cdot\frac a2\cdot\frac a2}$ (1) $=\frac{\sqrt3}4a^2$ (1).", "1+1+1"),
 Q(r"Verify Brahmagupta's formula for a square of side $a$.", r"$s=2a$; area $=\sqrt{(2a-a)^4}=\sqrt{a^4}=a^2$ (3), which is the known area of the square.", "3"),
 Q(r"Find the area of the cyclic quadrilateral with sides 25 cm, 39 cm, 52 cm and 60 cm.", r"$s=88$; $s-a=63,49,36,28$ (1). Area $=\sqrt{63\times49\times36\times28}=1764$ cm$^2$ (2).", "1+2"),
 Q(r"Find the area of a circle of radius 21 cm and of the sector of angle $60^\circ$ ($\pi=\frac{22}7$).", r"Circle $=\frac{22}7\times21^2=1386$ cm$^2$ (1+1). Sector $=\frac{60}{360}\times1386=231$ cm$^2$ (1).", "2+1"),
 Q(r"The circumferences of two circles are in the ratio 5 : 4. Find the ratio of their areas.", r"Radii are in the ratio $5:4$ (1). Areas $\pi r^2$ in the ratio $25:16$ (2).", "1+2"),
 Q(r"A circular park has perimeter 88 m. Find its area and the cost of fencing it at ₹12 per metre ($\pi=\frac{22}7$).", r"$r=14$ m (1); area $=\frac{22}7\times196=616$ m$^2$ (1); cost $=88\times12=₹1056$ (1).", "1+1+1"),
 Q(r"A circular ring has outer radius 14 cm and inner radius 7 cm. Find its area ($\pi=\frac{22}7$).", r"$\pi(14^2-7^2)=\frac{22}7\times147=462$ cm$^2$.", "2+1"),
 Q(r"A wheel has diameter 56 cm. How many revolutions will it make to cover 1.76 km? ($\pi=\frac{22}7$)", r"Circumference $=176$ cm (1). $1.76\text{ km}=176000$ cm (1). Revolutions $=\frac{176000}{176}=1000$ (1).", "1+1+1"),
 Q(r"A parallelogram has base 20 cm, height 9 cm and one side 15 cm. Find its area and the distance between its other pair of parallel sides.", r"Area $=20\times9=180$ cm$^2$ (1+1). Using the 15 cm side as base: $15\times h=180\Rightarrow h=12$ cm (1).", "2+1"),
 Q(r"Find the area of a trapezium with parallel sides 12 cm and 20 cm and distance 7 cm between them.", r"Area $=\frac12(12+20)\times7=112$ cm$^2$.", "2+1"),
 Q(r"Baudhāyana's method: find the side of a square whose area equals that of a $16\text{ cm}\times9\text{ cm}$ rectangle.", r"Area $=144$ cm$^2$ (1). Side $=\sqrt{144}=12$ cm (1). (Construction: the mean proportional of 16 and 9.)", "2+1"),
 Q(r"ABCD is a parallelogram of area 84 cm$^2$. Find the area of $\triangle ABD$ and justify.", r"Diagonal BD splits the parallelogram into two congruent triangles (1), so $\text{ar}(ABD)=42$ cm$^2$ (2).", "1+2"),
 Q(r"Find the perimeter of a sector of radius 21 cm and angle $60^\circ$ ($\pi=\frac{22}7$).", r"Arc $=\frac{60}{360}\times2\times\frac{22}7\times21=22$ cm (2). Perimeter $=22+21+21=64$ cm (1).", "2+1"),
 Q(r"Show that Heron's formula is a special case of Brahmagupta's formula.", r"A triangle is a cyclic 4-gon with $d=0$ (1). Then $s=\frac{a+b+c}2$ and $\sqrt{(s-a)(s-b)(s-c)(s-0)}=\sqrt{s(s-a)(s-b)(s-c)}$ (2), Heron's formula.", "1+2"),
 Q(r"The minute hand of a clock is 14 cm long. Find the distance its tip travels in 30 minutes and the area swept in that time ($\pi=\frac{22}7$).", r"30 min = half a turn: arc $=\pi r=44$ cm (1). Area $=\frac12\pi r^2=\frac12\times\frac{22}7\times196=308$ cm$^2$ (2).", "1+2"),
 Q(r"A rectangle has perimeter 36 cm. Find the dimensions of the rectangle with the greatest area and that area.", r"Half-perimeter 18; the maximum area occurs for the square: side 9 cm (2); area 81 cm$^2$ (1).", "2+1"),
]
assert len(C) == 24, len(C)
# D (16)
D += [
 Q(r"Prove that the area of a parallelogram with base $b$ and height $h$ is $bh$. What changes if the parallelogram is ‘thin’?", r"Cut the right triangle off one side and attach it to the other to form a rectangle of the same base $b$ and height $h$ (2). Rectangle area $=bh$ (1). For a thin parallelogram the foot of the perpendicular lies outside the base: shift triangles repeatedly (equal congruent triangles $CDD'$, $BAA'$) until the construction works (2).", "2+1+2"),
 Q(r"Prove that the area of a triangle is $\frac12bh$ and deduce that a median divides it into two triangles of equal area.", r"Two congruent copies fit to make a parallelogram of base $b$ and height $h$ (2) ⇒ triangle $=\frac12bh$ (1). Median $AD$: bases $BD=DC$, same height ⇒ equal areas (2).", "2+1+2"),
 Q(r"<b>Case study:</b> A 400 m track has two straights of 84.39 m each and two semicircular ends. The innermost semicircle has radius 36.5 m and each lane is 1.22 m wide. A runner keeps 0.3 m from the inner edge. (i) Find her radius on the bends. (ii) Find the distance she runs in one circuit ($\pi=3.1416$). (iii) Find the stagger needed between adjacent lanes. (iv) Why must the stagger be the same for every pair of adjacent lanes?", r"(i) $36.5+0.3=36.8$ m (1). (ii) $168.78+2\pi(36.8)=168.78+231.22=400$ m (2). (iii) Extra radius 1.22 m: $2\pi\times1.22\approx7.67$ m (1). (iv) Each lane's radius increases by the same 1.22 m, so the extra bend distance is the same $2\pi\times1.22$ for each pair (1).", "1+2+1+1"),
 Q(r"(i) Using Heron's formula show that the area of an isosceles triangle with equal sides $a$ and base $2b$ is $b\sqrt{a^2-b^2}$. (ii) Check with $a=5,b=3$ by the formula $\frac12bh$.", r"(i) $s=a+b$; area $=\sqrt{(a+b)(b)(b)(a-b)}=b\sqrt{a^2-b^2}$ (3). (ii) $h=\sqrt{25-9}=4$, base 6: $\frac12\times6\times4=12$; formula: $3\sqrt{16}=12$ ✓ (2).", "3+2"),
 Q(r"(i) Verify Brahmagupta's formula for a rectangle with sides $a,b$. (ii) Verify it for an isosceles trapezium with parallel sides 6 cm and 14 cm and legs 5 cm.", r"(i) $s=a+b$; $\sqrt{b\cdot a\cdot b\cdot a}=ab$ ✓ (2). (ii) $s=15$; area $=\sqrt{(15-6)(15-14)(15-5)(15-5)}=\sqrt{900}=30$ (2). Height $=\sqrt{25-16}=3$; $\frac12(6+14)\times3=30$ ✓ (1).", "2+2+1"),
 Q(r"<b>Case study:</b> A circular garden of radius 14 m has a 7 m wide path around it. ($\pi=\frac{22}7$) (i) Find the area of the garden. (ii) Find the outer radius and the area of the garden together with the path. (iii) Find the area of the path. (iv) Find the cost of paving it at ₹50 per m$^2$.", r"(i) $\frac{22}7\times196=616$ m$^2$ (1). (ii) Outer radius 21 m; area $\frac{22}7\times441=1386$ m$^2$ (2). (iii) $1386-616=770$ m$^2$ (1). (iv) $770\times50=₹38{,}500$ (1).", "1+2+1+1"),
 Q(r"<b>Case study:</b> A car tyre has diameter 56 cm. ($\pi=\frac{22}7$) (i) How far does the car move in one revolution? (ii) How many revolutions does the tyre make in 1.76 km? (iii) If the tyre turns 500 times per minute, find the speed in km/h. (iv) A tyre of diameter 70 cm turns the same number of times; compare the distances covered.", r"(i) $\frac{22}7\times56=176$ cm (1). (ii) $\frac{176000}{176}=1000$ (1). (iii) $500\times176=88000$ cm/min $=880$ m/min $=52.8$ km/h (2). (iv) Circumference 220 cm; ratio of distances $=176:220=4:5$ (1).", "1+1+2+1"),
 Q(r"(i) Use Heron's formula to find the area of the triangle with sides 17 cm, 25 cm and 26 cm. (ii) Find the lengths of its three altitudes. (iii) Which altitude is the longest?", r"(i) $s=34$; area $=\sqrt{34\times17\times9\times8}=204$ cm$^2$ (2). (ii) Altitudes $\frac{2\times204}{17}=24$, $\frac{408}{25}=16.32$, $\frac{408}{26}\approx15.69$ cm (2). (iii) The altitude on the shortest side (24 cm) (1).", "2+2+1"),
 Q(r"Prove, using the inscribed and circumscribed regular hexagons of a circle of radius $r$, that $3<\pi<2\sqrt3$. Why is Archimedes' extension to 96 sides useful?", r"Inscribed hexagon: six equilateral triangles of side $r$ ⇒ perimeter $6r<2\pi r$ ⇒ $\pi>3$ (2). Circumscribed hexagon: side $=\frac{2r}{\sqrt3}$ ⇒ perimeter $4\sqrt3r>2\pi r$ ⇒ $\pi<2\sqrt3\approx3.46$ (2). More sides squeeze the two perimeters closer, trapping $\pi$ more tightly (1).", "2+2+1"),
 Q(r"Two congruent circles of radius $r$ with centres A and B each pass through the other's centre and meet at C and D. (i) Prove that $\triangle ABC$ is equilateral. (ii) Find $\angle CAD$. (iii) Find the perimeter of the outer boundary of the figure.", r"(i) $AB=AC=BC=r$ (radii) (1). (ii) $\angle CAB=\angle BAD=60^\circ$, so $\angle CAD=120^\circ$ (2). (iii) Each outer arc subtends $240^\circ$ at its centre: total $=2\times\frac{240}{360}\times2\pi r=\frac{8\pi r}3$ (2).", "1+2+2"),
 Q(r"<b>Case study:</b> A pizza of radius 14 cm is cut into 8 equal sectors. ($\pi=\frac{22}7$) (i) Find the angle of each sector. (ii) Find the arc length of one slice. (iii) Find the perimeter of one slice. (iv) Find the area of one slice.", r"(i) $\frac{360}8=45^\circ$ (1). (ii) $\frac{45}{360}\times2\pi\times14=11$ cm (1). (iii) $11+14+14=39$ cm (1). (iv) $\frac{45}{360}\times\frac{22}7\times196=77$ cm$^2$ (2).", "1+1+1+2"),
 Q(r"<b>Case study:</b> A cyclic plot has sides 25 m, 39 m, 52 m and 60 m. (i) Find its semi-perimeter. (ii) Find its area by Brahmagupta's formula. (iii) Show that the plot's diagonal of length 65 m is a diameter by finding the area as two right triangles (25-60-65 and 39-52-65). (iv) Find the cost of levelling at ₹20 per m$^2$.", r"(i) $s=88$ m (1). (ii) $\sqrt{63\times49\times36\times28}=1764$ m$^2$ (2). (iii) $25^2+60^2=65^2$ and $39^2+52^2=65^2$, so both triangles are right-angled; areas $750+1014=1764$ ✓ (1). (iv) $1764\times20=₹35{,}280$ (1).", "1+2+1+1"),
 Q(r"(i) List the integer-sided rectangles of perimeter 40 units and find their areas. (ii) Which has the greatest area and which the least? (iii) What do you notice about the shape of the rectangle of greatest area?", r"(i) $1\times19=19$, $2\times18=36$, $3\times17=51$, $4\times16=64$, $5\times15=75$, $6\times14=84$, $7\times13=91$, $8\times12=96$, $9\times11=99$, $10\times10=100$ (3). (ii) Greatest 100 ($10\times10$), least 19 ($1\times19$) (1). (iii) It is a square (1).", "3+1+1"),
 Q(r"(i) Prove that the two paths from P to Q — one a semicircle and the other made of $n$ semicircles on adjacent parts of PQ — have equal length. (ii) Hence find the length of each path if $PQ=28$ cm and the smaller semicircles have diameters 7, 7, 14 cm. ($\pi=\frac{22}7$)", r"(i) If the diameters are $d_1,\dots,d_n$ then $d_1+\dots+d_n=PQ$; length $=\pi(d_1+\dots+d_n)/2=\pi PQ/2$, the same as the big semicircle (3). (ii) $\frac{22}7\times\frac{28}2=44$ cm; also $\frac{22}7\times\frac{7+7+14}2=44$ cm ✓ (2).", "3+2"),
 Q(r"Baudhāyana's problem: (i) Explain what it means to ‘square a rectangle’. (ii) Find the side of the square equal in area to a $25\text{ cm}\times4\text{ cm}$ rectangle. (iii) Find its perimeter and compare it with the rectangle's perimeter.", r"(i) Construct a square with the same area as the rectangle (1). (ii) Area $=100$ cm$^2$; side $=10$ cm (2). (iii) Square perimeter $=40$ cm; rectangle perimeter $=58$ cm — the square has the smaller perimeter for the same area (2).", "1+2+2"),
 Q(r"<b>Case study:</b> A circular park of radius 35 m has a circular fountain of radius 7 m at its centre. ($\pi=\frac{22}7$) (i) Find the area of the park. (ii) Find the area of the fountain. (iii) Find the area of grass. (iv) Find the length of railing needed to fence the fountain and the park boundary together.", r"(i) $\frac{22}7\times1225=3850$ m$^2$ (1). (ii) $\frac{22}7\times49=154$ m$^2$ (1). (iii) $3850-154=3696$ m$^2$ (1). (iv) $2\pi(35)+2\pi(7)=220+44=264$ m (2).", "1+1+1+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
