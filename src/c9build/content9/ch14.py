from fractions import Fraction as F
from math import isqrt
from lib import mcq, Q, OR
from mk9 import M4, build

PI = F(22, 7)
AR_OPTS = ["Both A and R are true and R is the correct explanation of A",
           "Both A and R are true but R is not the correct explanation of A",
           "A is true but R is false",
           "A is false but R is true"]
def AR(a, r, ans, why):
    return mcq(f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}", list(AR_OPTS), ans, why)

def fm(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    s = f"{float(x):.2f}".rstrip("0").rstrip(".")
    return s
def dist(vals, c):
    out = []
    for v in vals:
        if v != c and v > 0 and v not in out: out.append(v)
    return out
def opts(c, cands, unit):
    return [f"{fm(x)} {unit}" for x in dist(cands, c)[:3]]
PIS = r"$\pi=\frac{22}7$"

# ---- solids (Part 2, ch 14): all values computed with exact fractions ----
def tsa_cuboid(l, w, h): return 2*(l*w + w*h + l*h)
def v_cuboid(l, w, h): return F(l)*w*h
def csa_cyl(r, h): return 2*PI*r*h
def tsa_cyl(r, h): return 2*PI*r*(r + h)
def v_cyl(r, h): return PI*r*r*h
def csa_cone(r, l): return PI*r*l
def tsa_cone(r, l): return PI*r*(l + r)
def v_cone(r, h): return PI*r*r*h/3
def sa_sph(r): return 4*PI*r*r
def v_sph(r): return F(4, 3)*PI*r**3
def csa_hem(r): return 2*PI*r*r
def tsa_hem(r): return 3*PI*r*r
def v_hem(r): return F(2, 3)*PI*r**3
def v_pyr(base, h): return F(base)*h/3

A = []; B = []; C = []; D = []

# ===== A: 40 MCQ =====
# cuboid TSA (4)
for l, w, h in [(8, 5, 3), (10, 6, 4), (12, 5, 4), (9, 7, 2)]:
    t = tsa_cuboid(l, w, h)
    cands = [l*w*h, t//2, l*w + w*h + l*h + 10, t + 12, 2*l*w*h]
    A.append(M4(f"The total surface area of a cuboid of length ${l}$ cm, width ${w}$ cm and height ${h}$ cm is:", f"{t} cm$^2$", opts(t, cands, "cm$^2$"),
                f"$2(lw+wh+lh)=2({l*w}+{w*h}+{l*h})={t}$"))
# cuboid volume (3)
for l, w, h in [(7, 6, 5), (12, 10, 5), (15, 6, 4)]:
    v = l*w*h
    cands = [tsa_cuboid(l, w, h), l + w + h, v + 20, v//2, 3*v]
    A.append(M4(f"The volume of a cuboid measuring ${l}$ cm $\\times$ ${w}$ cm $\\times$ ${h}$ cm is:", f"{v} cm$^3$", opts(v, cands, "cm$^3$"), f"$lwh={l}\\times{w}\\times{h}={v}$"))
# cube (3)
for a in [3, 4, 5]:
    v = a**3; t = 6*a*a
    cands = [a*a, 4*a*a, 3*a*a, 12*a*a, v]
    A.append(M4(f"The volume of a cube is ${v}$ cm$^3$. Its total surface area is:", f"{t} cm$^2$", opts(t, cands, "cm$^2$"), f"side $={a}$ cm, TSA $=6a^2={t}$"))
# cylinder CSA (3)
for r, h in [(7, 10), (F(7, 2), 12), (14, 6)]:
    c = csa_cyl(r, h)
    cands = [c/2, v_cyl(r, h), c + 22, c*2, tsa_cyl(r, h)]
    A.append(M4(f"Taking {PIS}, the curved surface area of a cylinder of radius ${fm(r)}$ cm and height ${h}$ cm is:", f"{fm(c)} cm$^2$", opts(c, cands, "cm$^2$"), f"$2\\pi rh={fm(c)}$"))
# cylinder volume (3)
for r, h in [(7, 10), (14, 3), (F(7, 2), 8)]:
    v = v_cyl(r, h)
    cands = [v/2, v*2, csa_cyl(r, h), v + 22, v*3]
    A.append(M4(f"Taking {PIS}, the volume of a cylinder of radius ${fm(r)}$ cm and height ${h}$ cm is:", f"{fm(v)} cm$^3$", opts(v, cands, "cm$^3$"), f"$\\pi r^2h={fm(v)}$"))
# cone CSA (2)
for r, l in [(7, 25), (14, 15)]:
    c = csa_cone(r, l)
    cands = [c/2, c*2, c + 154, c - 22, c*3]
    A.append(M4(f"Taking {PIS}, the curved surface area of a cone of base radius ${r}$ cm and slant height ${l}$ cm is:", f"{fm(c)} cm$^2$", opts(c, cands, "cm$^2$"), f"$\\pi rl={fm(c)}$"))
# cone volume (2)
for r, h in [(7, 24), (6, 7)]:
    v = v_cone(r, h)
    cands = [v*3, v/2, v + 22, v*2, v - 22]
    A.append(M4(f"Taking {PIS}, the volume of a cone of base radius ${r}$ cm and height ${h}$ cm is:", f"{fm(v)} cm$^3$", opts(v, cands, "cm$^3$"), f"$\\frac13\\pi r^2h={fm(v)}$"))
# slant height (2)
for r, h, l in [(6, 8, 10), (5, 12, 13)]:
    assert r*r + h*h == l*l
    A.append(M4(f"A cone has base radius ${r}$ cm and height ${h}$ cm. Its slant height is:", f"{l} cm", [f"{l-1} cm", f"{l+1} cm", f"{r+h} cm"], f"$l=\\sqrt{{{r}^2+{h}^2}}={l}$"))
# sphere SA (2), volume (2)
for r in [7, F(7, 2)]:
    s = sa_sph(r)
    cands = [s/2, s*2, s/4, s + 44, csa_hem(r) + 10]
    A.append(M4(f"Taking {PIS}, the surface area of a sphere of radius ${fm(r)}$ cm is:", f"{fm(s)} cm$^2$", opts(s, cands, "cm$^2$"), f"$4\\pi r^2={fm(s)}$"))
for r in [21, F(21, 2)]:
    v = v_sph(r)
    cands = [v*3/4, v/2, v*2, v + 100, v_hem(r)*3]
    A.append(M4(f"Taking {PIS}, the volume of a sphere of radius ${fm(r)}$ cm is:", f"{fm(v)} cm$^3$", opts(v, cands, "cm$^3$"), f"$\\frac43\\pi r^3={fm(v)}$"))
# hemisphere (3)
r = 7; c = csa_hem(r)
A.append(M4(f"Taking {PIS}, the curved surface area of a hemisphere of radius $7$ cm is:", f"{fm(c)} cm$^2$", opts(c, [c*2, c/2, tsa_hem(r), sa_sph(r) + 22], "cm$^2$"), "$2\\pi r^2$"))
r = 14; t = tsa_hem(r)
A.append(M4(f"Taking {PIS}, the total surface area of a hemisphere of radius $14$ cm is:", f"{fm(t)} cm$^2$", opts(t, [csa_hem(r), sa_sph(r), t + 154, t/2], "cm$^2$"), "$3\\pi r^2$ (curved + base)"))
r = 21; v = v_hem(r)
A.append(M4(f"Taking {PIS}, the volume of a hemisphere of radius $21$ cm is:", f"{fm(v)} cm$^3$", opts(v, [v*2, v/2, v_sph(r), v + 154], "cm$^3$"), "$\\frac23\\pi r^3$"))
# pyramid (2)
A.append(M4("A pyramid has a square base of side $6$ cm and a height of $10$ cm. Its volume is:", "120 cm$^3$", ["360 cm$^3$", "60 cm$^3$", "240 cm$^3$"], "$\\frac13\\times36\\times10=120$"))
A.append(M4("A pyramid has a base of area $48$ cm$^2$ and a height of $9$ cm. Its volume is:", "144 cm$^3$", ["432 cm$^3$", "216 cm$^3$", "72 cm$^3$"], "$\\frac13\\times48\\times9=144$"))
# conceptual (4)
A.append(M4("The volume of a cone is _____ the volume of a cylinder with the same base and the same height.", "one-third of", ["half of", "one-fourth of", "twice"], "salt-filling experiment: three cones fill one cylinder"))
A.append(M4("The surface area of a cylindrical tumbler closed at one end and open at the other (radius $r$, height $h$) is:", r"$\pi r(2h+r)$", [r"$2\pi r(h+r)$", r"$2\pi rh$", r"$\pi r(h+2r)$"], "curved surface plus one base"))
A.append(M4("If the radius of a sphere is doubled, its volume becomes:", "8 times", ["2 times", "4 times", "6 times"], "$V\\propto r^3$"))
A.append(M4("The surface area of a sphere of radius $r$ equals the curved surface area of a cylinder that tightly fits over it. The height of this cylinder is:", "$2r$", ["$r$", "$4r$", "$\\pi r$"], "$2\\pi r\\times2r=4\\pi r^2$"))
# assertion-reason (5)
A += [
 AR("A cube and a cuboid of equal volume need not have equal total surface areas.", "Total surface area depends on the individual dimensions, not only on the product $lwh$.", "a", "e.g. $8\\times8\\times8$ and $16\\times8\\times4$ both have volume 512 but TSA 384 and 448"),
 AR("The volume of a cone is $\\frac13\\pi r^2h$.", "Three cones of the same base and height fill exactly one cylinder of that base and height.", "a", "experimental verification"),
 AR("If the radius of a sphere is doubled, its surface area is also doubled.", "The surface area of a sphere is $4\\pi r^2$.", "d", "SA becomes four times; A is false"),
 AR("The surface area of a sphere of radius $r$ equals the curved surface area of a cylinder of radius $r$ and height $r$.", "The curved surface area of a cylinder is $2\\pi rh$.", "c", "the cylinder has height $2r$; A is false"),
 AR("The volume of a pyramid with base area $B$ and height $h$ is $\\frac13Bh$.", "The volume of a cuboid is $lwh$.", "b", "both true; the cuboid formula does not explain the pyramid formula"),
]
assert len(A) == 40, len(A)

# ===== B: 16 two-mark =====
B += [
 Q(r"The volume of a cube is $343$ cm$^3$. Find its side and total surface area.", r"Side $=\sqrt[3]{343}=7$ cm (1). TSA $=6\times49=294$ cm$^2$ (1).", "1+1"),
 Q(r"Find the volume of a water tank measuring $2.5$ m $\times$ $2$ m $\times$ $1.2$ m. How many litres does it hold?", r"$V=2.5\times2\times1.2=6$ m$^3$ (1) $=6000$ litres (1).", "1+1"),
 Q(r"Find the curved surface area of a cylinder of radius $7$ cm and height $20$ cm ($\pi=\frac{22}7$).", r"CSA $=2\pi rh=2\times\frac{22}7\times7\times20$ (1) $=880$ cm$^2$ (1).", "1+1"),
 Q(r"A cone has height $24$ cm and base radius $7$ cm. Find its slant height.", r"$l=\sqrt{r^2+h^2}=\sqrt{49+576}$ (1) $=25$ cm (1).", "1+1"),
 Q(r"Find the volume of a hemisphere of radius $10.5$ cm ($\pi=\frac{22}7$).", r"$V=\frac23\pi r^3=\frac23\times\frac{22}7\times10.5^3$ (1) $=2425.5$ cm$^3$ (1).", "1+1"),
 Q(r"Write the formulas for the surface area and the volume of a sphere of radius $r$.", r"Surface area $=4\pi r^2$ (1); volume $=\frac43\pi r^3$ (1).", "1+1"),
 Q(r"Why does the formula for the volume of a cone contain the factor $\frac13$? How can this be shown by an experiment?", r"A cone has one-third the volume of the cylinder with the same base and height (1). Fill the cone with salt and empty it into the cylinder; it takes exactly three fills (1).", "1+1"),
 Q(r"How many cubes of side $2$ cm can be cut from a cuboid of $10$ cm $\times$ $8$ cm $\times$ $6$ cm?", r"Volume of cuboid $=480$ cm$^3$; volume of one cube $=8$ cm$^3$ (1). Number $=60$ (1).", "1+1"),
 Q(r"A cone and a cylinder have the same base radius and the same height. Find the ratio of their volumes.", r"$V_{cone}:V_{cyl}=\frac13\pi r^2h:\pi r^2h$ (1) $=1:3$ (1).", "1+1"),
 Q(r"Write the total surface area of a cylinder closed at both ends, and explain each part.", r"TSA $=2\pi rh+2\pi r^2=2\pi r(h+r)$ (1). $2\pi rh$ is the curved surface; $2\pi r^2$ is the two circular ends (1).", "1+1"),
 Q(r"The radii of two spheres are in the ratio $1:2$. Find the ratio of their surface areas.", r"Surface areas are in the ratio $r_1^2:r_2^2$ (1) $=1:4$ (1).", "1+1"),
 Q(r"If the edge of a cube is doubled, by what factor do its surface area and volume change?", r"Surface area becomes $4$ times (1); volume becomes $8$ times (1).", "1+1"),
 Q(r"What is a cross-section of a solid? What shape is the cross-section of a cylinder when it is cut parallel to its base?", r"A cross-section is the shape obtained by taking a very thin slice of the solid (1). Parallel to the base the slice is a circle (1).", "1+1"),
 Q(r"Find the volume of a pyramid with a square base of side $5$ cm and a height of $12$ cm.", r"$V=\frac13\times\text{area of base}\times\text{height}=\frac13\times25\times12$ (1) $=100$ cm$^3$ (1).", "1+1"),
 Q(r"A tank is $2$ m long, $1$ m wide and $1.5$ m deep. How many litres of water can it hold? ($1$ m$^3=1000$ litres)", r"Volume $=2\times1\times1.5=3$ m$^3$ (1) $=3000$ litres (1).", "1+1"),
 Q(r"How is a right circular cone obtained from a right-angled triangle?", r"Rotate the triangle through $360^\circ$ about one of its two perpendicular sides (1); this side becomes the height, the other becomes the radius and the hypotenuse the slant height (1).", "1+1"),
]
assert len(B) == 16, len(B)

# ===== C: 24 three-mark =====
a = 6; big = tsa_cuboid(a, a, a); small = 6*1*a**3
assert (big, small) == (216, 1296)
C.append(Q(r"A cube of side $6$ cm is cut into cubes of side $1$ cm. Find the ratio of the surface area of the original cube to the total surface area of all the small cubes.", r"Original TSA $=6\times36=216$ cm$^2$ (1). Number of small cubes $=216$, each of TSA $6$ cm$^2$, total $=1296$ cm$^2$ (1). Ratio $=216:1296=1:6$ (1).", "1+1+1"))
assert 30*20*8 / (F(5, 2)) == 1920
C.append(Q(r"A godown measures $30$ m $\times$ $20$ m $\times$ $8$ m. How many cuboidal boxes of size $2$ m $\times$ $1.25$ m $\times$ $1$ m can be stored in it?", r"Volume of godown $=4800$ m$^3$ (1). Volume of one box $=2.5$ m$^3$ (1). Number of boxes $=4800\div2.5=1920$ (1).", "1+1+1"))
assert (8, 24, 24, 8) == (8, 12*2, 6*4, 2**3) and 8 + 24 + 24 + 8 == 64
C.append(Q(r"A cube of side $4$ cm is painted on all faces and then cut into $64$ cubes of side $1$ cm. How many small cubes have (i) three faces painted, (ii) two faces painted, (iii) one face painted, (iv) no face painted?", r"(i) corner cubes: $8$ (1). (ii) $12$ edges $\times$ $2$ cubes $=24$ (1). (iii) $6$ faces $\times$ $4$ cubes $=24$ (½); (iv) inner cube $2\times2\times2=8$ (½). Check: $8+24+24+8=64$.", "1+1+½+½"))
v = v_cyl(F(7, 10), F(3, 2)); assert v == F(231, 100)
C.append(Q(r"A cylindrical drum has radius $0.7$ m and height $1.5$ m. Find the volume of oil it can hold in litres ($\pi=\frac{22}7$, $1$ m$^3=1000$ litres).", r"$V=\pi r^2h=\frac{22}7\times0.49\times1.5$ (1) $=2.31$ m$^3$ (1) $=2310$ litres (1).", "1+1+1"))
r = F(264) / (2*PI*7); assert r == 6; assert v_cyl(6, 7) == 792
C.append(Q(r"The curved surface area of a cylinder is $264$ cm$^2$ and its height is $7$ cm. Find its radius and volume ($\pi=\frac{22}7$).", r"$2\pi rh=264\Rightarrow r=\frac{264}{2\times\frac{22}7\times7}=6$ cm (1). $V=\pi r^2h=\frac{22}7\times36\times7$ (1) $=792$ cm$^3$ (1).", "1+1+1"))
assert F(1*1*4, 2*2*3) == F(1, 3) and F(1*4, 2*3) == F(2, 3)
C.append(Q(r"The radii of two cylinders are in the ratio $1:2$ and their heights are in the ratio $4:3$. Find the ratio of (i) their volumes, (ii) their curved surface areas.", r"(i) $V_1:V_2=r_1^2h_1:r_2^2h_2=(1\times4):(4\times3)$ (1) $=1:3$ (1). (ii) $\text{CSA}_1:\text{CSA}_2=r_1h_1:r_2h_2=4:6=2:3$ (1).", "1+1+1"))
C.append(Q(r"A metal sphere of radius $3$ cm is melted and recast into small cones of radius $1$ cm and height $3$ cm. How many cones are made?", r"Volume of sphere $=\frac43\pi(27)=36\pi$ cm$^3$ (1). Volume of one cone $=\frac13\pi(1)(3)=\pi$ cm$^3$ (1). Number $=36\pi\div\pi=36$ (1).", "1+1+1"))
c = csa_cone(7, 25); assert c == 550 and c*120 == 66000
C.append(Q(r"A conical tent has base radius $7$ m and height $24$ m. Find the canvas needed and its cost at ₹$120$ per m$^2$ ($\pi=\frac{22}7$).", r"$l=\sqrt{49+576}=25$ m (1). Canvas $=\pi rl=\frac{22}7\times7\times25=550$ m$^2$ (1). Cost $=550\times120=$ ₹$66{,}000$ (1).", "1+1+1"))
assert F(462) / (PI*21) == 7 and tsa_cone(7, 21) == 616
C.append(Q(r"The curved surface area of a cone is $462$ cm$^2$ and its slant height is $21$ cm. Find the base radius and the total surface area ($\pi=\frac{22}7$).", r"$\pi rl=462\Rightarrow r=\frac{462}{\frac{22}7\times21}=7$ cm (1). Base area $=\frac{22}7\times49=154$ cm$^2$ (1). TSA $=462+154=616$ cm$^2$ (1).", "1+1+1"))
assert v_cone(7, 24) == 1232 and csa_cone(7, 25) == 550
C.append(Q(r"A right-angled triangle with sides $7$ cm, $24$ cm and $25$ cm is rotated through $360^\circ$ about the side of $24$ cm. Find the volume and the curved surface area of the solid formed ($\pi=\frac{22}7$).", r"The solid is a cone with $r=7$, $h=24$, $l=25$ (1). $V=\frac13\times\frac{22}7\times49\times24=1232$ cm$^3$ (1). CSA $=\pi rl=550$ cm$^2$ (1).", "1+1+1"))
C.append(Q(r"A conical cup of height $18$ cm is filled with water up to a depth of $6$ cm (measured from the apex). What fraction of the cup's volume is occupied by water?", r"Water forms a similar cone of height $\frac13$ the cup's height (1), so its radius is also $\frac13$ (1). Volume ratio $=\left(\frac13\right)^3=\frac1{27}$ (1).", "1+1+1"))
assert v_pyr(81, 10) == 270
C.append(Q(r"A pyramid has a square base of side $9$ cm and height $10$ cm. Find its volume. How does it compare with a prism of the same base and height?", r"$V=\frac13\times81\times10=270$ cm$^3$ (2). Prism volume $=810$ cm$^3$, so the pyramid is one-third of it (1).", "2+1"))
assert sa_sph(7) == 616 and sa_sph(7)*F(1, 4) == 154
C.append(Q(r"A ball of radius $7$ cm is to be painted. Find the area to be painted and the cost at ₹$0.25$ per cm$^2$ ($\pi=\frac{22}7$).", r"Area $=4\pi r^2=4\times\frac{22}7\times49$ (1) $=616$ cm$^2$ (1). Cost $=616\times0.25=$ ₹$154$ (1).", "1+1+1"))
C.append(Q(r"The radii of two spheres are in the ratio $3:5$. Find the ratio of their (i) surface areas, (ii) volumes.", r"(i) $3^2:5^2=9:25$ (1.5). (ii) $3^3:5^3=27:125$ (1.5).", "1½+1½"))
assert v_hem(F(21, 2)) == F(4851, 2)
C.append(Q(r"A hemispherical bowl has an inner radius of $10.5$ cm. Find the volume of liquid it can hold in litres ($\pi=\frac{22}7$).", r"$V=\frac23\pi r^3=\frac23\times\frac{22}7\times10.5^3$ (1) $=2425.5$ cm$^3$ (1) $=2.4255$ litres (1).", "1+1+1"))
r = F(66) / (2*PI); assert r == F(21, 2) and csa_hem(r) == 693 and csa_hem(r)*40 == 27720
C.append(Q(r"The base circumference of a hemispherical dome is $66$ m. Find the cost of painting its outer curved surface at ₹$40$ per m$^2$ ($\pi=\frac{22}7$).", r"$2\pi r=66\Rightarrow r=10.5$ m (1). CSA $=2\pi r^2=2\times\frac{22}7\times110.25=693$ m$^2$ (1). Cost $=693\times40=$ ₹$27{,}720$ (1).", "1+1+1"))
assert F(3, 2)**2 == F(9, 4) and F(3, 2)**3 == F(27, 8)
C.append(Q(r"The edge of a cube is increased by $50\%$. Find the percentage increase in (i) its total surface area, (ii) its volume.", r"New edge $=1.5a$ (1). (i) TSA becomes $2.25\times$ the original: increase $125\%$ (1). (ii) Volume becomes $3.375\times$ the original: increase $237.5\%$ (1).", "1+1+1"))
assert F(36) * PI / (F(4, 3) * PI) == 27
C.append(Q(r"A cylindrical glass has radius $3$ cm and contains water to a height of $10$ cm. How many marbles of radius $1$ cm must be dropped in so that the water level rises to $14$ cm? (Marbles sink fully.)", r"Extra volume $=\pi(3)^2(4)=36\pi$ cm$^3$ (1). Volume of one marble $=\frac43\pi$ cm$^3$ (1). Number $=36\pi\div\frac43\pi=27$ (1).", "1+1+1"))
assert isqrt(12*20*15)**2 == 12*20*15 and isqrt(12*20*15) == 60
C.append(Q(r"The areas of three faces of a cuboid that meet at a corner are $12$ cm$^2$, $20$ cm$^2$ and $15$ cm$^2$. Find its volume.", r"$lw\cdot wh\cdot lh=(lwh)^2=12\times20\times15=3600$ (2). So $V=lwh=60$ cm$^3$ (1).", "2+1"))
assert PI*F(7, 2)*(2*10 + F(7, 2)) == F(517, 2)
C.append(Q(r"A steel tumbler is open at the top and has radius $3.5$ cm and height $10$ cm. Find the area of steel used in making it ($\pi=\frac{22}7$).", r"Area $=\pi r(2h+r)$ (1) $=\frac{22}7\times3.5\times(20+3.5)$ (1) $=11\times23.5=258.5$ cm$^2$ (1).", "1+1+1"))
assert v_cyl(7, 12) == 1848 and v_cone(7, 12) == 616
C.append(Q(r"A cylinder and a cone have the same base radius $7$ cm and the same height $12$ cm. Find the volume of each and the difference between them ($\pi=\frac{22}7$).", r"Cylinder $=\frac{22}7\times49\times12=1848$ cm$^3$ (1). Cone $=\frac13\times1848=616$ cm$^3$ (1). Difference $=1232$ cm$^3$ (1).", "1+1+1"))
assert 25*10*2 == 500 and F(500000, 2500) == 200
C.append(Q(r"A swimming pool is $25$ m long, $10$ m wide and $2$ m deep. How many litres of water does it hold when full? How long will a pump delivering $2500$ litres per minute take to fill it?", r"$V=25\times10\times2=500$ m$^3$ (1) $=5{,}00{,}000$ litres (1). Time $=\frac{500000}{2500}=200$ min $=3$ h $20$ min (1).", "1+1+1"))
assert tsa_hem(14) == 1848 and csa_hem(14) == 1232
C.append(Q(r"Find the curved surface area and the total surface area of a solid hemisphere of radius $14$ cm ($\pi=\frac{22}7$).", r"CSA $=2\pi r^2=2\times\frac{22}7\times196=1232$ cm$^2$ (1.5). TSA $=3\pi r^2=1848$ cm$^2$ (1.5).", "1½+1½"))
assert v_pyr(24, 9) == 72
C.append(Q(r"A pyramid has a triangular base with sides $6$ cm, $8$ cm and $10$ cm and a height of $9$ cm. Find its volume.", r"$6^2+8^2=10^2$, so the base is a right triangle (1) of area $\frac12\times6\times8=24$ cm$^2$ (1). $V=\frac13\times24\times9=72$ cm$^3$ (1).", "1+1+1"))
assert len(C) == 24, len(C)

# ===== D: 16 five-mark =====
assert csa_cyl(7, 15) == 660 and tsa_cyl(7, 15) == 968
D.append(Q(r"Derive the formulas for the curved surface area and total surface area of a cylinder of radius $r$ and height $h$. Hence find both for $r=7$ cm and $h=15$ cm ($\pi=\frac{22}7$).", r"Cut the curved surface along a line parallel to the axis and open it out: it is a rectangle with sides $2\pi r$ and $h$, so CSA $=2\pi rh$ (2). Adding two circular ends, TSA $=2\pi rh+2\pi r^2=2\pi r(h+r)$ (1). For $r=7$, $h=15$: CSA $=660$ cm$^2$ (1); TSA $=660+308=968$ cm$^2$ (1).", "2+1+1+1"))
assert v_cyl(F(7, 5), 3) == F(1848, 100)
D.append(Q(r"<b>Case study:</b> A cylindrical water tank has radius $1.4$ m and height $3$ m ($\pi=\frac{22}7$). (i) Find its capacity in litres. (ii) Find the area of the curved surface to be painted. (iii) Find the cost of painting at ₹$25$ per m$^2$. (iv) A family uses $120$ litres a day. For how many days does a full tank last?", r"(i) $V=\frac{22}7\times1.96\times3=18.48$ m$^3=18{,}480$ litres (1½). (ii) CSA $=2\times\frac{22}7\times1.4\times3=26.4$ m$^2$ (1). (iii) Cost $=26.4\times25=$ ₹$660$ (1). (iv) $18480\div120=154$ days (1½).", "1½+1+1+1½"))
assert tsa_cone(7, 25) == 704
D.append(Q(r"A cone has base radius $7$ cm and height $24$ cm ($\pi=\frac{22}7$). (i) Find its slant height. (ii) Find its curved and total surface area. (iii) Find its volume. (iv) State how the volume compares with a cylinder of the same base and height.", r"(i) $l=\sqrt{49+576}=25$ cm (1). (ii) CSA $=\pi rl=550$ cm$^2$ (1); TSA $=550+154=704$ cm$^2$ (1). (iii) $V=\frac13\pi r^2h=1232$ cm$^3$ (1). (iv) The cylinder has volume $3696$ cm$^3$, three times the cone (1).", "1+2+1+1"))
assert v_cone(7, 24) / 11 == 112
D.append(Q(r"<b>Case study:</b> A conical tent has base radius $7$ m and height $24$ m ($\pi=\frac{22}7$). (i) Find the slant height. (ii) Find the canvas required. (iii) Find the volume of air inside. (iv) If each person needs $11$ m$^3$ of air, how many people can sleep in the tent?", r"(i) $l=25$ m (1). (ii) Canvas $=\pi rl=550$ m$^2$ (1½). (iii) $V=\frac13\pi r^2h=1232$ m$^3$ (1½). (iv) $1232\div11=112$ people (1).", "1+1½+1½+1"))
assert sa_sph(F(21, 2)) == 1386 and v_sph(F(21, 2)) == 4851
D.append(Q(r"(i) Show how Archimedes' cylinder gives the surface area of a sphere. (ii) For a sphere of radius $10.5$ cm find the surface area and the volume ($\pi=\frac{22}7$).", r"(i) A cylinder of radius $r$ and height $2r$ fits tightly over the sphere; its curved surface area is $2\pi r\times2r=4\pi r^2$, which equals the sphere's surface area (2). (ii) Surface area $=4\pi r^2=4\times\frac{22}7\times110.25=1386$ cm$^2$ (1½). Volume $=\frac43\pi r^3=4851$ cm$^3$ (1½).", "2+1½+1½"))
assert 21*7*7 == 1029 and 3*v_sph(F(7, 2)) == 539 and 1029 - 539 == 490
D.append(Q(r"<b>Case study:</b> Three identical metal spheres, each of radius $3.5$ cm, fit exactly in a row inside a closed cuboidal box. (i) Write the internal dimensions of the box. (ii) Find the volume of the box. (iii) Find the total volume of the three spheres. (iv) The remaining space is filled with preservative liquid; find its volume ($\pi=\frac{22}7$).", r"(i) $21$ cm $\times$ $7$ cm $\times$ $7$ cm (1). (ii) $21\times7\times7=1029$ cm$^3$ (1). (iii) $3\times\frac43\times\frac{22}7\times3.5^3=539$ cm$^3$ (2). (iv) $1029-539=490$ cm$^3$ (1).", "1+1+2+1"))
assert (v_cone(F(21, 2), 14), v_hem(F(21, 2))) == (1617, F(4851, 2)) and 1617 + F(4851, 2) == F(8085, 2)
assert csa_cone(F(21, 2), F(35, 2)) == F(1155, 2) and F(35, 2)**2 == F(21, 2)**2 + 14**2
D.append(Q(r"A solid toy is a cone of base radius $10.5$ cm and height $14$ cm with a hemisphere of the same radius fixed on its base. ($\pi=\frac{22}7$) (i) Find the slant height of the cone. (ii) Find the total outer surface area of the toy. (iii) Find the total volume of the toy.", r"(i) $l=\sqrt{10.5^2+14^2}=\sqrt{306.25}=17.5$ cm (1). (ii) Cone CSA $=\pi rl=\frac{22}7\times10.5\times17.5=577.5$ cm$^2$ (1); hemisphere CSA $=2\pi r^2=693$ cm$^2$ (1); total $=1270.5$ cm$^2$ (1). (iii) $V=1617+2425.5=4042.5$ cm$^3$ (1).", "1+3+1"))
vv = v_cyl(12, 35); assert vv == 15840
gb = v_sph(F(21, 10)); assert gb == F(38808, 1000); gp = gb/2; n = vv / gp
D.append(Q(r"<b>Case study:</b> A golgappa vendor's cylindrical vessel has radius $12$ cm and holds spiced water to a height of $35$ cm. Assume each golgappa is a sphere of radius $2.1$ cm and takes pani equal to $50\\%$ of its volume ($\pi=\frac{22}7$). (i) Find the volume of pani in the vessel. (ii) Find the volume of one golgappa. (iii) Find the pani used in one golgappa. (iv) Estimate how many golgappas can be served. (v) Why would a different assumption change the answer?".replace("\\\\", "\\"),
           rf"(i) $V=\pi r^2h=\frac{{22}}7\times144\times35=15{{,}}840$ cm$^3$ (1). (ii) $\frac43\pi r^3=38.808$ cm$^3$ (1). (iii) $50\%$ of $38.808=19.404$ cm$^3$ (1). (iv) $15840\div19.404\approx{int(n)}$ golgappas (1). (v) The result depends on the estimated size and the fraction of pani; guesstimates give a range, not an exact value (1).", "1+1+1+1+1"))
assert tsa_cuboid(8, 8, 8) == 384 and tsa_cuboid(16, 8, 4) == 448 and 16*8*4 == 512
D.append(Q(r"<b>Case study:</b> A company packs the same volume of product in either a cube of side $8$ cm or a cuboid of $16$ cm $\times$ $8$ cm $\times$ $4$ cm. (i) Show that both boxes have the same volume. (ii) Find the surface area of each. (iii) Which needs less cardboard and by how much? (iv) Cardboard costs ₹$0.50$ per cm$^2$; find the extra cost for $100$ cuboid boxes. (v) Name one situation where a larger surface area is useful.", r"(i) Cube $=8^3=512$ cm$^3$; cuboid $=16\times8\times4=512$ cm$^3$ (1). (ii) Cube TSA $=6\times64=384$ cm$^2$; cuboid TSA $=2(128+32+64)=448$ cm$^2$ (1½). (iii) The cube needs less, by $64$ cm$^2$ (1). (iv) $64\times0.5\times100=$ ₹$3200$ (1). (v) Cooling or heat transfer (radiators), or absorption in biological cells (½).", "1+1½+1+1+½"))
assert (F(1, 3)*PI*9*6, v_sph(3)/PI, v_cyl(3, 6)/PI) == (F(1, 3)*PI*54, 36, 54)
D.append(Q(r"A cone, a sphere and a cylinder each have radius $r$; the cone and the cylinder have height $2r$ (the sphere's diameter). Show that their volumes are in the ratio $1:2:3$. Verify with $r=3$ cm (leave answers in terms of $\pi$).", r"Cone $=\frac13\pi r^2(2r)=\frac23\pi r^3$ (1). Sphere $=\frac43\pi r^3$ (1). Cylinder $=\pi r^2(2r)=2\pi r^3$ (1). Dividing by $\frac23\pi r^3$: $1:2:3$ (1). For $r=3$: $18\pi:36\pi:54\pi=1:2:3$ (1).", "1+1+1+1+1"))
assert v_cyl(3, 8)/PI == 72 and v_sph(F(3, 2))/PI == F(9, 2) and F(72) / F(9, 2) == 16
D.append(Q(r"A solid metal cylinder of radius $3$ cm and height $8$ cm is melted and recast into small solid spheres of radius $1.5$ cm. (i) Find the volume of the cylinder. (ii) Find the volume of one sphere. (iii) How many spheres are formed? (iv) Find the total surface area of all the spheres. Leave answers in terms of $\pi$.", r"(i) $V=\pi\times9\times8=72\pi$ cm$^3$ (1). (ii) $\frac43\pi(1.5)^3=4.5\pi$ cm$^3$ (1½). (iii) $72\pi\div4.5\pi=16$ (1). (iv) One sphere: $4\pi(2.25)=9\pi$ cm$^2$ (1); total $=16\times9\pi=144\pi$ cm$^2$ (½).", "1+1½+1+1½"))
D.append(Q(r"The radius of a cylinder is increased by $20\%$ while its height is unchanged. Find the percentage change in (i) the curved surface area, (ii) the volume, and (iii) the total surface area when $h=r$.", r"New radius $=1.2r$ (1). (i) CSA $=2\pi rh$ becomes $1.2\times$: increase $20\%$ (1). (ii) Volume $=\pi r^2h$ becomes $1.44\times$: increase $44\%$ (1). (iii) With $h=r$: old TSA $=2\pi r(2r)=4\pi r^2$; new TSA $=2\pi(1.2r)(r+1.2r)=5.28\pi r^2$, an increase of $32\%$ (2).", "1+1+1+2"))
walls = 2*(20 + 10)*F(9, 5); floor = 20*10; area = walls + floor
assert (walls, floor, area, area*250) == (108, 200, 308, 77000) and F(360000, 3000) == 120
D.append(Q(r"<b>Case study:</b> A swimming pool is a cuboid $20$ m long, $10$ m wide and $1.8$ m deep. (i) Find its capacity in litres. (ii) Find the area of the floor and four walls to be tiled. (iii) Find the tiling cost at ₹$250$ per m$^2$. (iv) A pump fills $3000$ litres per minute; find the time to fill the pool.", r"(i) $V=20\times10\times1.8=360$ m$^3=3{,}60{,}000$ litres (1). (ii) Floor $=200$ m$^2$; walls $=2(20+10)\times1.8=108$ m$^2$; total $=308$ m$^2$ (2). (iii) $308\times250=$ ₹$77{,}000$ (1). (iv) $360000\div3000=120$ min $=2$ h (1).", "1+2+1+1"))
rise = v_sph(F(7, 2)) / (PI*49); assert rise == F(7, 6) and 3*rise == F(7, 2)
D.append(Q(r"A cylindrical jar of radius $7$ cm contains water. A solid sphere of radius $3.5$ cm is dropped in and sinks completely without any water overflowing ($\pi=\frac{22}7$). (i) Find the volume of the sphere. (ii) By how much does the water level rise? (iii) By how much would it rise if three such spheres were dropped in? (iv) Explain why the rise depends on the jar's base area.", r"(i) $V=\frac43\times\frac{22}7\times3.5^3=179\frac23\approx179.67$ cm$^3$ (1). (ii) Rise $=\frac{179.67}{\pi\times49}=\frac{179.67}{154}=\frac76\approx1.17$ cm (2). (iii) $3\times\frac76=3.5$ cm (1). (iv) Displaced volume equals base area $\times$ rise; a larger base gives a smaller rise (1).", "1+2+1+1"))
slant = isqrt(8*8 + 15*15); assert slant == 17
assert 4*F(1, 2)*16*17 == 544 and v_pyr(256, 15) == 1280 and 544 + 256 == 800
D.append(Q(r"<b>Case study:</b> A model of a pyramid has a square base of side $16$ cm and a vertical height of $15$ cm. (i) Find the slant height of each triangular face. (ii) Find the area of the four triangular faces. (iii) Find the total surface area including the base. (iv) Find the volume. (v) Why is no separate surface-area formula needed for pyramids?", r"(i) Half the side is $8$; $l=\sqrt{8^2+15^2}=17$ cm (1). (ii) $4\times\frac12\times16\times17=544$ cm$^2$ (1). (iii) $544+256=800$ cm$^2$ (1). (iv) $V=\frac13\times256\times15=1280$ cm$^3$ (1). (v) Surface area is just the sum of the areas of the faces (1).", "1+1+1+1+1"))
assert v_sph(F(21, 2)) == F(1, 3)*sa_sph(F(21, 2))*F(21, 2) == 4851
D.append(Q(r"(i) Using the picture of a sphere divided into many thin cones with apex at the centre, show that $V=\frac13\times\text{surface area}\times r$ and hence $V=\frac43\pi r^3$. (ii) Find the volume of a sphere whose surface area is $1386$ cm$^2$ ($\pi=\frac{22}7$).", r"(i) Each tiny region of area $a_i$ with the centre forms a cone of height $r$ and volume $\frac13a_ir$ (1); adding all, $V=\frac13r\times\sum a_i=\frac13r\times4\pi r^2$ (2) $=\frac43\pi r^3$ (1). (ii) $4\pi r^2=1386\Rightarrow r=10.5$ cm, $V=\frac13\times1386\times10.5=4851$ cm$^3$ (1).", "1+2+1+1"))
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
