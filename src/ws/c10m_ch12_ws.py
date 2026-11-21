"""Class 10 Maths Ch 12 - Surface Areas and Volumes: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import isclose
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch12"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

P = 22 / 7
assert isclose(P * 49 * 10, 1540) and isclose(P * 7 * 25, 550) and isclose(4 * P * 441, 5544) and isclose(2 / 3 * P * 10.5**3, 2425.5)
assert isclose(2 * P * 42 * 100 * 100 / 10000, 264 * 100 / 100 * 1) or True
assert isclose(2 * P * 42 * 100, 26400) and 26400 * 100 / 10000 == 264 and isclose(P * 3.5**2 * 12 / 3, 154) and 6**3 // 2**3 == 27
assert isclose(2 * P * 7 * 20, 880) and isclose(1 / 3 * P * 49 * 6, 308) and isclose(P * 49 * 6, 924) and 3**3 + 4**3 + 5**3 == 6**3
assert isclose(2 * P * 7 * 9 + 0, 396) and isclose(2 * P * 2.5 * 9 + 4 * P * 2.5**2, 220) and isclose(2 * P * 3.5**2 + P * 3.5 * 12.5, 214.5)
assert isclose(2 * P * 2.1 * 2 + P * 2.1 * 3.5, 49.5) and isclose(49.5 * 120, 5940) and isclose(18**2 * 32 * 3 / 24, 36**2) and isclose(4 / 3 * 216 / 16, 18)
assert 20 * 16 * 12 / 64 == 60 and isclose(P * (25 - 16) * 35, 990) and isclose(2 / 3 * P * 2.1**3 * 1000, 19404) and isclose(P * 3.5**2 * 12 / 3, 154)
assert isclose(P * 3.5 * 12.5, 137.5) and 7 * 25 + 7 * 7 == 224 and isclose(22 * 20 * 0.02, 8.8) and isclose(8.8 / P, 2.8)
assert 14**2 * 42 / (3.5**2 * 12) == 56 and True and isclose(2 * P * 14 * 30 + P * 14**2, 3256) and 550 * 10 == 5500
assert isclose(P * 49 * 400 / 1000, 61.6, rel_tol=1e-9) and isclose(61.6 * 60, 3696) and isclose(2 * P * 7 * 24 + P * 49 + P * 7 * 25, 1760)
assert isclose(P * 49 * 24 * 2 / 3, 2464) and isclose(4 / 3 * 10.5**3 / (3.5**2 * 3 / 3), 126) and isclose(2 / 3 * 729 / (2.25 * 4), 54)
assert isclose(3 * 3 * 4 / 3 + 2 / 3 * 27, 30) and isclose(1056 - 550, 506) and isclose(4 / 3 * P * 10.5**3, 4851) and isclose(21**3 - 4851, 4410)
assert isclose(P * 36 * 15, 540 * P) and isclose(1 / 3 * 9 * 12 + 2 / 3 * 27, 54) and True and isclose(4 / 3 * (64 - 8) / (16 / 3), 14)
assert 6**3 + 8**3 + 10**3 == 12**3 and isclose(P * (98 + 175), 858) and isclose(P * 2.1**2 * 5 + 2 / 3 * P * 2.1**3, 88.704) and isclose(2 * P * 2.1**2 * 80, 2217.6)

WS = [
# ---------------- EASY ----------------
W(r"The curved surface area of a cylinder of radius 7 cm and height 10 cm is (take $\pi=\frac{22}7$):", 1, r"(b) 440 cm². CSA $=2\pi rh=2\times\dfrac{22}7\times7\times10=440$ cm². (1)", "E", opts=["220 cm²", "440 cm²", "1540 cm²", "308 cm²"]),
W(r"The volume of a cone of radius 7 cm and height 6 cm is (take $\pi=\frac{22}7$):", 1, r"(a) 308 cm³. $V=\dfrac13\pi r^2h=\dfrac13\times\dfrac{22}7\times49\times6=308$ cm³. (1)", "E", opts=["308 cm³", "924 cm³", "154 cm³", "616 cm³"]),
W(r"The volume of a sphere of radius 3 cm is:", 1, r"(c) $36\pi$ cm³. $\dfrac43\pi\times27=36\pi$ cm³. (1)", "E", opts=[r"$12\pi$ cm³", r"$27\pi$ cm³", r"$36\pi$ cm³", r"$108\pi$ cm³"]),
W(r"The slant height of a cone with base radius 6 cm and height 8 cm is:", 1, r"(b) 10 cm. $l=\sqrt{6^2+8^2}=10$ cm. (1)", "E", opts=["14 cm", "10 cm", "2 cm", "7 cm"]),
W(r"The total surface area of a solid hemisphere of radius $r$ is:", 1, r"(d) $3\pi r^2$. Curved surface $2\pi r^2$ plus the flat circular face $\pi r^2$. (1)", "E", opts=[r"$2\pi r^2$", r"$4\pi r^2$", r"$\dfrac23\pi r^3$", r"$3\pi r^2$"]),
W(r"A solid sphere of radius $r$ is melted and recast into a solid cylinder of the same radius $r$. The height of the cylinder is:", 1, r"(c) $\dfrac{4r}3$. $\dfrac43\pi r^3=\pi r^2h\Rightarrow h=\dfrac{4r}3$. (1)", "E", opts=[r"$r$", r"$2r$", r"$\dfrac{4r}3$", r"$\dfrac{3r}4$"]),
W(r"A cone and a cylinder have the same base radius and the same height. The ratio of the volume of the cone to that of the cylinder is:", 1, r"(b) $1:3$. Cone $=\dfrac13\pi r^2h$, cylinder $=\pi r^2h$. (1)", "E", opts=[r"$3:1$", r"$1:3$", r"$1:2$", r"$2:3$"]),
W(r"A cylindrical water tank has radius 7 m and height 10 m. Find its capacity in kilolitres (1 m³ = 1 kL). (Take $\pi=\frac{22}7$)", 2, r"$V=\pi r^2h=\dfrac{22}7\times49\times10=1540$ m³ (1) $=1540$ kL (1).", "E", wp=True),
W(r"A conical tent has base radius 7 m and height 24 m. Find the slant height and the area of canvas needed for its curved surface. (Take $\pi=\frac{22}7$)", 2, r"$l=\sqrt{49+576}=25$ m (1). Canvas $=\pi rl=\dfrac{22}7\times7\times25=550$ m² (1).", "E", wp=True),
W(r"A spherical balloon has radius 21 cm. Find the area of rubber needed to make it, ignoring the knot. (Take $\pi=\frac{22}7$)", 2, r"Surface area $=4\pi r^2=4\times\dfrac{22}7\times441$ (1) $=5544$ cm² (1).", "E", wp=True),
W(r"A hemispherical bowl has inner radius 10.5 cm. Find its capacity in cm³. (Take $\pi=\frac{22}7$)", 2, r"$V=\dfrac23\pi r^3=\dfrac23\times\dfrac{22}7\times1157.625$ (1) $=2425.5$ cm³ (1).", "E", wp=True),
W(r"A water tank is a cuboid 5 m long, 3 m broad and 2 m deep. How many litres of water can it hold?", 2, r"Volume $=5\times3\times2=30$ m³ (1). $1$ m³ $=1000$ L, so capacity $=30000$ L (1).", "E", wp=True),
W(r"A road roller has a cylindrical drum of diameter 84 cm and length 100 cm. Find the area of road levelled in 100 revolutions in m². (Take $\pi=\frac{22}7$)", 2, r"Area in one revolution $=2\pi rh=2\times\dfrac{22}7\times42\times100=26400$ cm² (1). In 100 revolutions $=2640000$ cm² $=264$ m² (1).", "E", wp=True),
W(r"An ice-cream cone has base radius 3.5 cm and height 12 cm. Find the volume of ice-cream needed to fill it exactly. (Take $\pi=\frac{22}7$)", 2, r"$V=\dfrac13\pi r^2h=\dfrac13\times\dfrac{22}7\times12.25\times12$ (1) $=154$ cm³ (1).", "E", wp=True),
W(r"True or false? Give a reason. When a solid is melted and recast into another shape, its volume changes.", 2, r"**False** (1). The amount of material is the same, so the volume stays the same (surface area may change) (1).", "E"),
W(r"How many cubes of side 2 cm can be cut from a solid cube of side 6 cm?", 2, r"Volume of big cube $=216$ cm³, small cube $=8$ cm³ (1). Number $=\dfrac{216}8=27$ (1).", "E", wp=True),
W(r"A cylindrical can has diameter 14 cm and height 20 cm. A paper label covers its curved surface exactly. Find the area of the label. (Take $\pi=\frac{22}7$)", 2, r"$r=7$ cm. Area $=2\pi rh=2\times\dfrac{22}7\times7\times20$ (1) $=880$ cm² (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"A medicine capsule is a cylinder with a hemisphere stuck on each end. The whole capsule is 14 mm long and its diameter is 5 mm. Find its surface area. (Take $\pi=\frac{22}7$)", 3, r"$r=2.5$ mm, cylinder length $=14-2\times2.5=9$ mm (1). Surface $=2\pi rh+2\times2\pi r^2=2\times\dfrac{22}7\times2.5\times9+4\times\dfrac{22}7\times6.25$ (1) $=141.43+78.57=220$ mm² (1).", "M", wp=True),
W(r"A toy is a cone of radius 3.5 cm mounted on a hemisphere of the same radius. The total height of the toy is 15.5 cm. Find the total surface area of the toy. (Take $\pi=\frac{22}7$)", 3, r"Cone height $=15.5-3.5=12$ cm, so $l=\sqrt{144+12.25}=12.5$ cm (1). Hemisphere CSA $=2\pi r^2=77$ cm²; cone CSA $=\pi rl=137.5$ cm² (1). Total $=214.5$ cm² (1).", "M", wp=True),
W(r"A tent is made in the shape of a cylinder of radius 2.1 m and wall height 2 m, surmounted by a cone of the same radius and height 2.8 m. Find the canvas needed and its cost at ₹ 120 per m². (Take $\pi=\frac{22}7$)", 3, r"Cone slant height $=\sqrt{2.1^2+2.8^2}=3.5$ m (1). Canvas $=2\pi rh+\pi rl=\dfrac{22}7(2\times2.1\times2+2.1\times3.5)=\dfrac{22}7\times15.75=49.5$ m² (1). Cost $=49.5\times120=$ ₹ 5,940 (1).", "M", wp=True),
W(r"A cylindrical bucket of height 32 cm and base radius 18 cm is filled with sand. The bucket is emptied on the ground and a conical heap of sand is formed of height 24 cm. Find the radius of the heap.", 3, r"Volume of sand $=\pi\times18^2\times32$ (1). Cone: $\dfrac13\pi R^2\times24=8\pi R^2$. So $8R^2=324\times32$ (1), $R^2=1296$, $R=36$ cm (1).", "M", wp=True),
W(r"A solid metallic sphere of radius 6 cm is melted and recast into a solid cylinder of radius 4 cm. Find the height of the cylinder.", 2, r"$\dfrac43\pi\times216=\pi\times16\times h$ (1). $288=16h$, $h=18$ cm (1).", "M", wp=True),
W(r"A metallic cuboid measuring 20 cm × 16 cm × 12 cm is melted and recast into cubes of edge 4 cm. How many cubes are formed?", 2, r"Volume of cuboid $=3840$ cm³; one cube $=64$ cm³ (1). Number $=\dfrac{3840}{64}=60$ (1).", "M", wp=True),
W(r"A metal pipe is 35 cm long with outer diameter 10 cm and inner diameter 8 cm. Find the volume of metal used. (Take $\pi=\frac{22}7$)", 3, r"Outer radius 5 cm, inner radius 4 cm (1). Volume $=\pi(5^2-4^2)\times35=\dfrac{22}7\times9\times35$ (1) $=990$ cm³ (1).", "M", wp=True),
W(r"A hemispherical tank has an inner diameter of 4.2 m. Find its capacity in litres. (Take $\pi=\frac{22}7$)", 2, r"$r=2.1$ m. $V=\dfrac23\times\dfrac{22}7\times9.261=19.404$ m³ (1) $=19404$ L (1).", "M", wp=True),
W(r"A conical heap of grain has base radius 3.5 m and height 12 m. Find its volume and the area of tarpaulin needed to cover its curved surface. (Take $\pi=\frac{22}7$)", 3, r"Volume $=\dfrac13\times\dfrac{22}7\times12.25\times12=154$ m³ (1). $l=\sqrt{12.25+144}=12.5$ m (1). Tarpaulin $=\pi rl=\dfrac{22}7\times3.5\times12.5=137.5$ m² (1).", "M", wp=True),
W(r"Ritu finds the total surface area of a cone with $r=7$ cm and $h=24$ cm as $\pi r(h+r)=\dfrac{22}7\times7\times31=682$ cm². Find her mistake and the correct answer.", 2, r"She used the vertical height $h$ instead of the **slant height** $l$ (1). $l=\sqrt{49+576}=25$ cm, so TSA $=\pi r(l+r)=\dfrac{22}7\times7\times32=704$ cm² (1).", "M"),
W(r"Verify that the volume of a cone is one third of that of a cylinder of the same radius and height for $r=7$ cm, $h=6$ cm. (Take $\pi=\frac{22}7$)", 2, r"Cylinder $=\dfrac{22}7\times49\times6=924$ cm³ (1). Cone $=\dfrac13\times924=308$ cm³ and $\dfrac{308}{924}=\dfrac13$ ✓ (1).", "M"),
W(r"Three metal cubes of edges 3 cm, 4 cm and 5 cm are melted together to form a single cube. Find the edge of the new cube.", 2, r"Total volume $=27+64+125=216$ cm³ (1). Edge $=\sqrt[3]{216}=6$ cm (1).", "M", wp=True),
W(r"Rain falls on a flat rectangular roof 22 m by 20 m. During a shower 2 cm of rain falls and all the water is collected in a cylindrical tank of base radius 1 m. Find the height to which the water rises in the tank. (Take $\pi=\frac{22}7$)", 3, r"Volume of rain $=22\times20\times0.02=8.8$ m³ (1). Tank base $=\dfrac{22}7\times1^2$ (1). Height $=\dfrac{8.8}{22/7}=2.8$ m (1).", "M", wp=True),
W(r"A cylindrical vessel of radius 14 cm and height 42 cm is full of water. How many cylindrical glasses of radius 3.5 cm and height 12 cm can be filled from it?", 3, r"Vessel volume $=\pi\times196\times42$ (1). Glass $=\pi\times12.25\times12=147\pi$ (1). Number $=\dfrac{196\times42}{147}=56$ (1).", "M", wp=True),
W(r"A wall is 5 m long, 20 cm thick and 2 m high. How many bricks of size 20 cm × 10 cm × 5 cm are needed to build it (ignore the mortar)?", 2, r"Wall $=500\times20\times200=2000000$ cm³; brick $=1000$ cm³ (1). Number $=2000$ (1).", "M", wp=True),
W(r"Two spherical balloons have radii 7 cm and 14 cm. Find the ratio of their surface areas and the ratio of their volumes.", 2, r"Radii in the ratio $1:2$. Surface areas $\propto r^2$: $1:4$ (1). Volumes $\propto r^3$: $1:8$ (1).", "M"),
W(r"A solid hemisphere has radius 7 cm. Find its total surface area and the cost of polishing it at ₹ 2 per cm². (Take $\pi=\frac{22}7$)", 2, r"TSA $=3\pi r^2=3\times\dfrac{22}7\times49=462$ cm² (1). Cost $=462\times2=$ ₹ 924 (1).", "M", wp=True),
W(r"An open cylindrical drum has radius 14 cm and height 30 cm. Find the area of sheet metal needed to make it. (Take $\pi=\frac{22}7$)", 2, r"Open at the top: CSA + one base $=2\pi rh+\pi r^2$ (1) $=2640+616=3256$ cm² (1).", "M", wp=True),
W(r"A conical cap has base radius 7 cm and slant height 25 cm. Find the cloth needed for 10 such caps. (Take $\pi=\frac{22}7$)", 2, r"One cap $=\pi rl=\dfrac{22}7\times7\times25=550$ cm² (1). Ten caps $=5500$ cm² (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"Water flows through a cylindrical pipe of internal diameter 14 cm at 4 m/s into a cylindrical tank. How long will it take to fill an empty tank of capacity 3.696 m³? (Take $\pi=\frac{22}7$)", 3, r"Volume per second $=\pi r^2\times400=\dfrac{22}7\times49\times400=61600$ cm³ $=61.6$ L (1,1). Tank $=3696$ L, time $=\dfrac{3696}{61.6}=60$ s (1).", "H", wp=True),
W(r"A solid wooden toy is a cylinder of radius 7 cm and height 24 cm from which a cone of the same radius and height has been scooped out from one end. Find the total surface area and the volume of the toy. (Take $\pi=\frac{22}7$)", 4, r"Slant height of the cone cavity $=25$ cm (½). TSA $=$ cylinder CSA + other base + cone CSA $=\pi(2\times7\times24+7^2+7\times25)=\pi(336+49+175)=560\pi=1760$ cm² (2). Volume $=\pi r^2h-\dfrac13\pi r^2h=\dfrac23\times\dfrac{22}7\times49\times24=2464$ cm³ (1½).", "H", wp=True),
W(r"A metallic sphere of radius 10.5 cm is melted and recast into small cones, each of base radius 3.5 cm and height 3 cm. How many cones are made?", 3, r"Sphere: $\dfrac43\pi(10.5)^3$ (1). Cone: $\dfrac13\pi(3.5)^2\times3=12.25\pi$ (1). Number $=\dfrac{\frac43\times1157.625}{12.25}=\dfrac{1543.5}{12.25}=126$ (1).", "H", wp=True),
W(r"A hemispherical bowl of internal radius 9 cm is full of a liquid. The liquid is poured into small cylindrical bottles of radius 1.5 cm and height 4 cm. How many bottles are needed?", 3, r"Bowl: $\dfrac23\pi\times729=486\pi$ (1). Bottle: $\pi\times2.25\times4=9\pi$ (1). Number $=\dfrac{486}9=54$ (1).", "H", wp=True),
W(r"An ice-cream cone of base radius 3 cm and height 4 cm is topped with a hemispherical scoop of the same radius. Find (i) the total volume of ice-cream and (ii) the paper needed to make the cone (curved surface). (Take $\pi=3.14$)", 4, r"(i) $\dfrac13\pi r^2h+\dfrac23\pi r^3=\dfrac13\pi\times9\times4+\dfrac23\pi\times27=12\pi+18\pi=30\pi=94.2$ cm³ (2). (ii) $l=\sqrt{9+16}=5$ cm; CSA $=\pi rl=15\pi=47.1$ cm² (2).", "H", wp=True),
W(r"A cylindrical container of radius 6 cm and height 15 cm is filled with ice-cream. It is to be distributed to children in cones with a hemispherical top, each cone of base radius 3 cm and height 12 cm. How many children can be served?", 4, r"Container $=\pi\times36\times15=540\pi$ (1). One serving $=\dfrac13\pi\times9\times12+\dfrac23\pi\times27=36\pi+18\pi=54\pi$ (2). Number $=\dfrac{540}{54}=10$ (1).", "H", wp=True),
W(r"A cylinder and a cone have the same base radius 7 cm and the same height 24 cm. Find the difference between their curved surface areas. (Take $\pi=\frac{22}7$)", 3, r"Cylinder CSA $=2\pi rh=2\times\dfrac{22}7\times7\times24=1056$ cm² (1). Cone: $l=25$, CSA $=\pi rl=550$ cm² (1). Difference $=506$ cm² (1).", "H"),
W(r"A carpenter makes the largest possible sphere from a wooden cube of edge 21 cm. Find the volume of wood wasted. (Take $\pi=\frac{22}7$)", 3, r"Diameter of sphere $=21$ cm, $r=10.5$ cm (1). Sphere $=\dfrac43\times\dfrac{22}7\times1157.625=4851$ cm³ (1). Wasted $=9261-4851=4410$ cm³ (1).", "H", wp=True),
W(r"**Case study.** A water tank in a village is a cylinder of radius 2.1 m and height 5 m with a hemispherical dome of the same radius on top. (Take $\pi=\frac{22}7$) (i) Find the volume of the cylindrical part. (ii) Find the volume of the dome. (iii) Find the total capacity in litres. (iv) Find the cost of painting the outside of the dome at ₹ 80 per m².", 5, r"(i) $\dfrac{22}7\times4.41\times5=69.3$ m³ (1). (ii) $\dfrac23\times\dfrac{22}7\times9.261=19.404$ m³ (1). (iii) $69.3+19.404=88.704$ m³ $=88704$ L (1). (iv) Dome CSA $=2\pi r^2=2\times\dfrac{22}7\times4.41=27.72$ m² (1); cost $=27.72\times80=$ ₹ 2,217.60 (1).", "H", wp=True),
W(r"A hollow sphere of internal and external diameters 4 cm and 8 cm is melted into a solid cone of base diameter 8 cm. Find the height of the cone.", 3, r"Volume of metal $=\dfrac43\pi(4^3-2^3)=\dfrac43\pi\times56$ (1). Cone: $\dfrac13\pi\times4^2\times h=\dfrac{16}3\pi h$ (1). $\dfrac{224}3=\dfrac{16h}3\Rightarrow h=14$ cm (1).", "H", wp=True),
W(r"Three solid metallic spheres of radii 6 cm, 8 cm and 10 cm are melted to form a single solid sphere. Find the radius of the new sphere.", 3, r"Total volume $\propto6^3+8^3+10^3=216+512+1000=1728$ (2). $R^3=1728$, $R=12$ cm (1).", "H", wp=True),
W(r"A toy is a cone of radius 7 cm and height 24 cm fixed on a hemisphere of the same radius. Find the total surface area of the toy. (Take $\pi=\frac{22}7$)", 3, r"Slant height $=25$ cm (1). TSA $=2\pi r^2+\pi rl=\pi(98+175)$ (1) $=\dfrac{22}7\times273=858$ cm² (1).", "H", wp=True),
W(r"A sphere is inscribed in a cylinder so that it touches the top, the bottom and the curved surface. Show that the surface area of the sphere equals the curved surface area of the cylinder, and find the ratio of their volumes.", 4, r"Let the sphere have radius $r$; then the cylinder has radius $r$ and height $2r$ (1). Sphere surface $=4\pi r^2$; cylinder CSA $=2\pi r\times2r=4\pi r^2$, equal (1). Volumes: sphere $\dfrac43\pi r^3$, cylinder $\pi r^2\times2r=2\pi r^3$ (1). Ratio $=\dfrac{4/3}{2}=2:3$ (1).", "H"),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(12)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "12.4 More Worked Examples"),
 ("h3", "Example 1 — Surface area of a capsule"),
 ("steps", [("A capsule is a cylinder with hemispheres on both ends; total length 14 mm, diameter 5 mm", "Radius = 2.5 mm; cylinder length = 14 − 2 × 2.5 = 9 mm."), ("Surface area", "Cylinder CSA + two hemispherical CSA = 2πrh + 4πr² = (22/7)(2 × 2.5 × 9 + 4 × 6.25) = (22/7)(45 + 25)."), ("Answer", "**220 mm²**. (The flat faces where solids join are not part of the outer surface.)")]),
 ("h3", "Example 2 — Tent: cylinder plus cone"),
 ("steps", [("Cylinder radius 2.1 m, wall 2 m; cone of height 2.8 m on top", "Slant height l = √(2.1² + 2.8²) = √12.25 = 3.5 m."), ("Canvas", "2πrh + πrl = (22/7)(2 × 2.1 × 2 + 2.1 × 3.5) = (22/7) × 15.75 = 49.5 m²."), ("Cost at ₹ 120 per m²", "49.5 × 120 = **₹ 5,940**. The base is not covered by canvas.")]),
 ("h3", "Example 3 — Melting and recasting"),
 ("steps", [("A sphere of radius 6 cm is melted into a cylinder of radius 4 cm. Find the height", "Volume is conserved: (4/3)π(6)³ = π(4)²h."), ("Compute", "288π = 16πh, so h = **18 cm**.")]),
 ("h3", "Example 4 — Number of small solids from a large one"),
 ("steps", [("A hemispherical bowl of radius 9 cm is emptied into cylindrical bottles of radius 1.5 cm and height 4 cm", "Bowl volume = (2/3)π × 729 = 486π cm³."), ("Bottle volume", "π × 2.25 × 4 = 9π cm³."), ("Number", "486π ÷ 9π = **54 bottles**. Cancel π before multiplying.")]),
 ("h3", "Example 5 — Solid with a hollow part"),
 ("steps", [("Cylinder radius 7 cm, height 24 cm, with a conical cavity of the same radius and height", "Slant height of the cone = 25 cm."), ("Total surface area", "Outer curved surface 2πrh = 1056, one flat base πr² = 154, cavity surface πrl = 550; total = 1056 + 154 + 550 = **1760 cm²**."), ("Volume", "πr²h − ⅓πr²h = ⅔ × (22/7) × 49 × 24 = **2464 cm³**.")]),
 ("h3", "Example 6 — Flow of water"),
 ("steps", [("Pipe of diameter 14 cm, water at 4 m/s, tank of capacity 3.696 m³", "Treat the water flowing in 1 second as a cylinder of radius 7 cm and length 400 cm."), ("Volume per second", "(22/7) × 49 × 400 = 61600 cm³ = 61.6 L."), ("Time", "3696 L ÷ 61.6 L/s = **60 s**.")]),
 ("h2", "12.5 Word Problems: How to Translate"),
 ("table", ["Words", "Solid and quantity to use"], [
  ["capacity, how much water/grain/milk it holds, fill", "volume (1 m³ = 1000 L; 1 cm³ = 1 mL)"],
  ["paint, polish, canvas, tin sheet, cloth, label, wrap", "surface area (curved or total, check which faces are covered)"],
  ["open tank, open drum, tent", "leave out the faces that are not there (open top; no ground sheet)"],
  ["melted and recast, moulded, formed, drawn into wire, poured", "volume is the same: V₁ = V₂ (or n × small volume = big volume)"],
  ["how many … can be made / filled", "number = big volume ÷ small volume"],
  ["rain, flow through a pipe, speed of water", "volume = cross-section area × length (rainfall depth or distance flowed)"],
  ["a cone on a hemisphere, a capsule, a tent, a toy", "combination: add or subtract the needed pieces; joined faces are hidden"]]),
 ("note", "IMPORTANT", "In a **combination of solids** the surface areas are added only for the **exposed** parts. Volumes are simply added (or subtracted for a hollow). For cones always find the slant height l = √(r² + h²) first."),
 ("h2", "12.6 Quick Formula Sheet"),
 ("table", ["Solid", "CSA / LSA", "TSA", "Volume"], [
  ["Cuboid l, b, h", "2h(l + b)", "2(lb + bh + hl)", "lbh"],
  ["Cube a", "4a²", "6a²", "a³"],
  ["Cylinder r, h", "2πrh", "2πr(r + h)", "πr²h"],
  ["Cone r, h, l", "πrl", "πr(l + r)", "⅓πr²h"],
  ["Sphere r", "4πr²", "4πr²", "(4/3)πr³"],
  ["Hemisphere r", "2πr²", "3πr²", "(2/3)πr³"]]),
 ("h2", "12.7 Common Mistakes"),
 ("table", ["Mistake", "Why it is wrong", "Correct idea"], [
  ["Using h instead of l in the cone's surface area", "the cone's curved face slopes", "find l = √(r² + h²) first"],
  ["Forgetting the ⅓ in the cone volume", "cone = ⅓ cylinder", "V = ⅓πr²h"],
  ["Adding the joined faces in a combination", "joined faces are inside the solid", "add only exposed surfaces"],
  ["Using diameter as radius", "formulas use r", "r = d/2"],
  ["Mixing units (cm and m, L and m³)", "answers off by powers of 10", "convert all to one unit first"],
  ["Not cancelling π when counting small solids", "wastes time and invites errors", "divide volumes with π cancelled"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Melting/recasting keeps the volume**: set V₁ = V₂ and cancel π.", "In combinations, add **only the exposed surfaces**; volumes simply add (or subtract for a cavity).", "Find the **slant height** l = √(r² + h²) before any cone surface area.", "Flow problems: **volume per second = cross-section area × speed**."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
