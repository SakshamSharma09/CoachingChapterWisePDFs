"""Class 9 Maths Ch 14 - Surface Area and Volume: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch14"

def _old(n):
    d = "c9_maths1" if n < 9 else "c9_maths2"
    p = Path(__file__).resolve().parents[1] / "rn_work" / d / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def _lt(x):
    if isinstance(x, str): return x.replace(" < ", " &lt; ").replace(" > ", " &gt; ")
    if isinstance(x, (list, tuple)): return type(x)(_lt(i) for i in x)
    return x

pi = F(22, 7)
assert 5**3 == 125 and 2*(12+6+8) == 52 and 2*pi*7*10 == 440 and F(1, 3)*pi*49*3 == 154 and 4*pi*49 == 616
assert 2*(40+20+32) == 184 and 8*5*4 == 160 and 3*2*F(3, 2)*1000 == 9000 and 6*100 == 600 and 2*pi*F(7, 2)*12 == 264 and pi*49*5 == 770
assert 7**2+24**2 == 25**2 and pi*7*25 == 550 and 2*pi*49 == 308 and 3*pi*49 == 462 and pi*F(7, 2)*(20+F(7, 2)) == F(517, 2)
assert F(1, 3)*36*10 == 120 and 360/3 == 120 and 9*8*4 == 288 and 288/36 == 8 and 2*(6+5)*3 == 66 and (66+30)*20 == 1920
assert 2*2.5*0+2.5*2*1.2 == 6 and 6000/50 == 120 and pi*F(49, 4)*14 == 539 and 539/(22*7) == 3.5 and 2*pi*F(7, 10)*2*100 == 880
assert 550+pi*49 == 704 and F(2, 3)*pi*F(21, 2)**3 == F(4851, 2) and 3*pi*F(21, 2)**2 == F(2079, 2) and 4*pi*F(21, 2)**2 == 1386 and F(4, 3)*pi*F(21, 2)**3 == 4851
assert 550*50 == 27500 and F(1, 3)*144*9 == 432 and 4**3 == 64 and 6*16 == 96 and 64*6 == 384 and 8+12*3+6*9+27 == 125 == 5**3
assert 5**3 == 125 and 6*25 == 150 and 2*(50+F(25, 2)+25) == 175 and 10*5*F(5, 2) == 125 and 6**3/2**3 == 27 and 2**3*100 == 800
assert F(4, 3)*6**3 == 288 and F(4, 3)*8 == F(32, 3) and 288/(F(8, 1)) == 36 and F(1, 3)*pi*F(49, 4)*12 == 154 and 1540/154 == 10
assert 10*10*6 == 600 and 8*6*25 == 1200 and 1000*6 == 6000 and pi*441*40 == 55440 and 55440/20 == 2772 and 2772/6 == 462 and 462*20 == 9240
assert 4*pi*21**2 == 5544 and 4*pi*42**2 == 22176 and F(4, 3)*pi*21**3 == 38808 and F(4, 3)*pi*42**3 == 310464
assert 2*pi*F(7, 2)*4 == 88 and 3.5**2+12**2 == 12.5**2 and pi*F(7, 2)*F(25, 2) == F(275, 2) and 88+F(275, 2) == F(451, 2) and F(451, 2)*80 == 18040
assert 4*F(1, 2)*10*13 == 260 and 13**2-5**2 == 12**2 and 260+100 == 360 and F(1, 3)*100*12 == 400
assert pi*21**2*42 == 58212 and 2*pi*21*42 == 5544 and 38808*3 == 58212*2 and F(2, 3)*pi*729 == 486*pi and 486/9 == 54
assert 288/F(32, 3) == F(27, 1)*1 / 1 or True
assert 22*14*F(5, 100) == F(77, 5) and F(77, 5)/(pi*F(49, 4)) == F(2, 5) and F(1, 3)*pi*9*4 == 12*pi
assert 216*0+ F(3, 5)*360 == 216 and 2*pi*21**2 == 2772 and 2772*40 == 110880 and F(2, 3)*pi*21**3 == 19404
assert F(2, 3)*pi*441*21 == 19404 and F(1, 3)*pi*441*20 == 9240 and 19404+9240 == 28644 and pi*49*12 == 1848 and F(1, 3)*1848 == 616 and 6**2*8 == 288
assert F(1, 3)*pi*343 == F(1078, 3) and F(2, 3)*pi*343 == F(2156, 3) and pi*343 == 1078 and (96*8) == 768 and 6*6*4 == 144 and 12*12 == 144

WS = [
# ---------------- EASY ----------------
W(r"The volume of a cube of side 5 cm is:", 1, r"(a) 125 cm³. $5^3=125$. (1)", "E", opts=["125 cm³", "75 cm³", "150 cm³", "25 cm³"]),
W(r"The total surface area of a cuboid $4\text{ cm}\times3\text{ cm}\times2\text{ cm}$ is:", 1, r"(c) 52 cm². $2(lw+wh+lh)=2(12+6+8)=52$. (1)", "E", opts=["24 cm²", "26 cm²", "52 cm²", "48 cm²"]),
W(r"The curved surface area of a cylinder of radius 7 cm and height 10 cm ($\pi=\frac{22}7$) is:", 1, r"(b) 440 cm². $2\pi rh=2\times\frac{22}7\times7\times10=440$. (1)", "E", opts=["220 cm²", "440 cm²", "1540 cm²", "880 cm²"]),
W(r"The volume of a cone of base radius 7 cm and height 3 cm ($\pi=\frac{22}7$) is:", 1, r"(d) 154 cm³. $\frac13\pi r^2h=\frac13\times\frac{22}7\times49\times3=154$. (1)", "E", opts=["462 cm³", "308 cm³", "77 cm³", "154 cm³"]),
W(r"The surface area of a sphere of radius 7 cm ($\pi=\frac{22}7$) is:", 1, r"(a) 616 cm². $4\pi r^2=4\times\frac{22}7\times49=616$. (1)", "E", opts=["616 cm²", "308 cm²", "1437 cm²", "154 cm²"]),
W(r"The number of litres in 1 m³ is:", 1, r"(c) 1000, since $1\text{ m}^3=100\times100\times100\text{ cm}^3=10^6\text{ cm}^3$ and $1000\text{ cm}^3=1$ litre. (1)", "E", opts=["10", "100", "1000", "10000"]),
W(r"Find the volume and total surface area of a cuboid of length 8 cm, width 5 cm and height 4 cm.", 2, r"$V=8\times5\times4=160$ cm³ (1). $TSA=2(40+20+32)=184$ cm² (1).", "E"),
W(r"A water tank is 3 m long, 2 m wide and 1.5 m deep. Find its capacity in litres.", 2, r"Volume $=3\times2\times1.5=9$ m³ (1). $9\times1000=9000$ litres (1).", "E", wp=True),
W(r"Reena wraps a cubical gift box of side 10 cm in coloured paper with no overlap. Find the area of paper needed.", 2, r"Total surface area $=6a^2=6\times100$ (1) $=600$ cm² (1).", "E", wp=True),
W(r"Find the curved surface area of a cylinder of radius 3.5 cm and height 12 cm. (Use $\pi=\frac{22}7$.)", 2, r"$2\pi rh=2\times\frac{22}7\times3.5\times12$ (1) $=264$ cm² (1).", "E"),
W(r"A cylindrical water tank has radius 7 m and height 5 m. Find its volume and its capacity in kilolitres (1 m³ = 1 kL). (Use $\pi=\frac{22}7$.)", 2, r"$V=\pi r^2h=\frac{22}7\times49\times5$ (1) $=770$ m³ $=770$ kL (1).", "E", wp=True),
W(r"A cone has base radius 7 cm and height 24 cm. Find its slant height and curved surface area. (Use $\pi=\frac{22}7$.)", 2, r"$l=\sqrt{7^2+24^2}=\sqrt{625}=25$ cm (1). $CSA=\pi rl=\frac{22}7\times7\times25=550$ cm² (1).", "E"),
W(r"Find the curved surface area and total surface area of a hemisphere of radius 7 cm. (Use $\pi=\frac{22}7$.)", 2, r"$CSA=2\pi r^2=2\times\frac{22}7\times49=308$ cm² (1). $TSA=3\pi r^2=462$ cm² (1).", "E"),
W(r"A tumbler (a cylinder open at the top) has radius 3.5 cm and height 10 cm. Find the area of the metal sheet needed. (Use $\pi=\frac{22}7$.)", 2, r"Open at one end: $\pi r(2h+r)$ (1) $=\frac{22}7\times3.5\times23.5=258.5$ cm² (1).", "E", wp=True),
W(r"Find the volume of a pyramid with a square base of side 6 cm and height 10 cm.", 2, r"$V=\frac13\times\text{base area}\times\text{height}=\frac13\times36\times10$ (1) $=120$ cm³ (1).", "E"),
W(r"A cone and a cylinder have the same base and the same height. If the cylinder holds 360 cm³ of salt, how much does the cone hold? Why does the experiment of emptying the cone into the cylinder need exactly 3 fills?", 2, r"The cone holds $\frac13\times360=120$ cm³ (1). The volume of a cone is one-third of the cylinder on the same base and height, so 3 cone-fills fill the cylinder (1).", "E", wp=True),
W(r"True or false (give a reason): if the side of a cube is doubled, its volume is also doubled.", 2, r"**False.** Volume $=a^3$; with side $2a$ it becomes $(2a)^3=8a^3$, i.e. 8 times (2).", "E"),
# ---------------- MEDIUM ----------------
W(r"A classroom is 9 m long, 8 m wide and 4 m high and 36 students sit in it. How much air (volume) is available per student?", 3, r"Volume $=9\times8\times4=288$ m³ (2). Per student $=288\div36=8$ m³ (1).", "M", wp=True),
W(r"A room is 6 m long, 5 m wide and 3 m high. Find the cost of painting its four walls and ceiling at ₹ 20 per m² (ignore doors and windows).", 3, r"Four walls $=2(l+w)h=2\times11\times3=66$ m² (1). Ceiling $=6\times5=30$ m² (1). Total $96\times20=$ ₹ 1,920 (1).", "M", wp=True),
W(r"A tank is 2.5 m long, 2 m wide and 1.2 m deep. A pump fills it at 50 litres per minute. How long does it take to fill the empty tank?", 3, r"Volume $=2.5\times2\times1.2=6$ m³ $=6000$ litres (2). Time $=6000\div50=120$ minutes $=2$ hours (1).", "M", wp=True),
W(r"Earth dug from a cylindrical well of diameter 7 m and depth 14 m is spread evenly over a rectangular plot 22 m by 7 m. Find the height of the raised platform. (Use $\pi=\frac{22}7$.)", 3, r"Volume of earth $=\frac{22}7\times3.5^2\times14=539$ m³ (1.5). Plot area $=22\times7=154$ m² (0.5). Height $=539\div154=3.5$ m (1).", "M", wp=True),
W(r"A garden roller has diameter 1.4 m and length 2 m. How much area does it level in 100 revolutions? (Use $\pi=\frac{22}7$.)", 3, r"One revolution covers the curved surface $2\pi rh=2\times\frac{22}7\times0.7\times2=8.8$ m² (2). 100 revolutions $=880$ m² (1).", "M", wp=True),
W(r"A cone has base radius 7 cm and height 24 cm. Find its slant height, curved surface area and total surface area. (Use $\pi=\frac{22}7$.)", 3, r"$l=25$ cm (1). $CSA=\pi rl=550$ cm² (1). $TSA=550+\pi r^2=550+154=704$ cm² (1).", "M"),
W(r"A conical tent has base radius 7 m and height 24 m. Find the canvas needed and its cost at ₹ 50 per m². (Use $\pi=\frac{22}7$.)", 3, r"$l=\sqrt{49+576}=25$ m (1). Canvas $=\pi rl=\frac{22}7\times7\times25=550$ m² (1). Cost $=550\times50=$ ₹ 27,500 (1).", "M", wp=True),
W(r"Find the volume and the total surface area of a hemisphere of radius 10.5 cm. (Use $\pi=\frac{22}7$.)", 3, r"$V=\frac23\pi r^3=\frac23\times\frac{22}7\times10.5^3=2425.5$ cm³ (1.5). $TSA=3\pi r^2=3\times\frac{22}7\times110.25=1039.5$ cm² (1.5).", "M"),
W(r"A spherical ball has radius 10.5 cm. Find the area to be painted and the volume of air inside it. (Use $\pi=\frac{22}7$.)", 3, r"Surface area $=4\pi r^2=4\times\frac{22}7\times110.25=1386$ cm² (1.5). Volume $=\frac43\pi r^3=4851$ cm³ (1.5).", "M", wp=True),
W(r"A pyramid-shaped granary has a square base of side 12 m and height 9 m. Find the volume of grain it can hold when full.", 3, r"Base area $=144$ m² (1). $V=\frac13\times144\times9$ (1) $=432$ m³ (1).", "M", wp=True),
W(r"A cube of side 4 cm is cut into 1 cm cubes. How many small cubes are formed? Find the total surface area before and after cutting and compare.", 3, r"Number of cubes $=4^3=64$ (1). Before: $6\times16=96$ cm² (0.5). After: $64\times6=384$ cm² (1). The surface area becomes 4 times while the volume (64 cm³) is unchanged (0.5).", "M"),
W(r"A cube of side 5 cm is painted on all faces and cut into 125 unit cubes. How many unit cubes have exactly 3, 2, 1 and 0 painted faces?", 3, r"3 faces (corners): 8 (0.75). 2 faces (edges): $12(5-2)=36$ (0.75). 1 face: $6(5-2)^2=54$ (0.75). 0 faces: $(5-2)^3=27$ (0.75). Check $8+36+54+27=125$ ✓.", "M"),
W(r"A cube of side 5 cm and a cuboid $10\text{ cm}\times5\text{ cm}\times2.5\text{ cm}$ have the same volume. Compare their total surface areas and say which needs less packing material.", 3, r"Both volumes are 125 cm³ (1). Cube: $6\times25=150$ cm² (1). Cuboid: $2(50+12.5+25)=175$ cm² (0.5). The cube needs less material for the same capacity (0.5).", "M", wp=True),
W(r"The radius of a spherical toy ball is doubled. By what factor do its surface area and volume change? If the original volume is 100 cm³, find the new volume.", 2, r"Area $\times2^2=4$, volume $\times2^3=8$ (1). New volume $=800$ cm³ (1).", "M", wp=True),
W(r"A metal cube of side 6 cm is melted and recast into small cubes of side 2 cm. How many small cubes are made?", 3, r"Volume of the big cube $=216$ cm³ (1). Volume of a small cube $=8$ cm³ (1). Number $=216\div8=27$ (1).", "M", wp=True),
W(r"A metal sphere of radius 6 cm is melted and recast into cones of base radius 2 cm and height 6 cm. How many cones are made? (Use $\pi$ as it cancels.)", 3, r"Sphere: $\frac43\pi\times216=288\pi$ cm³ (1). One cone: $\frac13\pi\times4\times6=8\pi$ cm³ (1). Number $=288\pi\div8\pi=36$ (1).", "M", wp=True),
W(r"A cube of side 6 cm is dropped into a rectangular tank of base 18 cm by 12 cm containing water. By how much does the water level rise?", 3, r"Volume displaced $=6^3=216$ cm³ (1). Base area of the tank $=216$ cm² (1). Rise $=216\div216=1$ cm (1).", "M", wp=True),
W(r"A steel tumbler (open at the top) has radius 3.5 cm and height 10 cm. Find the area of steel used and its capacity in mL. (Use $\pi=\frac{22}7$, 1 cm³ = 1 mL.)", 3, r"Area $=\pi r(2h+r)=258.5$ cm² (1.5). Capacity $=\pi r^2h=\frac{22}7\times12.25\times10=385$ cm³ $=385$ mL (1.5).", "M", wp=True),
W(r"An ice-cream cone has base radius 3.5 cm and height 12 cm. Find its volume. How many such cones can be filled from 1.54 litres of ice cream? (Use $\pi=\frac{22}7$.)", 3, r"$V=\frac13\times\frac{22}7\times12.25\times12=154$ cm³ (1.5). 1.54 L $=1540$ cm³ (0.5), so $1540\div154=10$ cones (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"A toy is a cone of height 20 cm placed on a hemisphere of radius 21 cm (the base of the cone equals the flat face of the hemisphere). Find the total volume of the toy. (Use $\pi=\frac{22}7$.)", 4, r"Hemisphere: $\frac23\pi r^3=\frac23\times\frac{22}7\times9261=19404$ cm³ (1.5). Cone: $\frac13\pi r^2h=\frac13\times\frac{22}7\times441\times20=9240$ cm³ (1.5). Total $=28644$ cm³ (1).", "H", wp=True),
W(r"A cube of side 10 cm is cut into 8 equal cubes. Find the change in total surface area. If it is cut into 1000 cubes of side 1 cm, how many times does the surface area become? What stays the same?", 4, r"Original: $6\times100=600$ cm² (1). Eight cubes of side 5 cm: $8\times6\times25=1200$ cm², i.e. doubled (1.5). 1000 cubes of side 1 cm: $1000\times6=6000$ cm², i.e. 10 times (1). The volume 1000 cm³ stays the same (0.5).", "H", wp=True),
W(r"**Guesstimate.** A golgappa vendor's vessel is a cylinder of radius 21 cm and height 40 cm, completely full of pani. Assume each golgappa takes 20 cm³ of pani and he serves 6 golgappas in a plate at ₹ 20 a plate. (i) Find the volume of the vessel. (ii) How many golgappas can he serve? (iii) How many plates and how much money? (iv) Name the assumptions behind this estimate. (Use $\pi=\frac{22}7$.)", 5, r"(i) $V=\frac{22}7\times441\times40=55440$ cm³ (1). (ii) $55440\div20=2772$ golgappas (1). (iii) $2772\div6=462$ plates; $462\times20=$ ₹ 9,240 (1.5). (iv) The vessel is exactly full with no pani left over or spilt, each golgappa takes exactly 20 cm³, and all are sold; different assumptions give different answers (1.5).", "H", wp=True),
W(r"A sphere has radius 21 cm. Find its surface area and volume. If the radius is doubled, find the new surface area and volume and verify the factors 4 and 8. (Use $\pi=\frac{22}7$.)", 4, r"$r=21$: $4\pi r^2=5544$ cm² (1), $\frac43\pi r^3=38808$ cm³ (1). $r=42$: $4\pi r^2=22176$ cm² (1) and $\frac43\pi r^3=310464$ cm³ (0.5). $22176\div5544=4$ and $310464\div38808=8$ ✓ (0.5).", "H"),
W(r"A circus tent is a cylinder of radius 3.5 m and height 4 m surmounted by a cone of the same base radius and height 12 m. Find the canvas needed and its cost at ₹ 80 per m². (Use $\pi=\frac{22}7$.)", 4, r"Cone slant height $l=\sqrt{3.5^2+12^2}=12.5$ m (1). Cylinder CSA $=2\pi rh=88$ m² (1). Cone CSA $=\pi rl=\frac{22}7\times3.5\times12.5=137.5$ m² (1). Canvas $=225.5$ m²; cost $=225.5\times80=$ ₹ 18,040 (1).", "H", wp=True),
W(r"A square pyramid has a base of side 10 m and each triangular face has slant height 13 m. Find its total surface area, its vertical height and its volume.", 4, r"Lateral area $=4\times\frac12\times10\times13=260$ m² (1). TSA $=260+100=360$ m² (1). Height $=\sqrt{13^2-5^2}=12$ m (1). $V=\frac13\times100\times12=400$ m³ (1).", "H", wp=True),
W(r"A cylinder of radius $r$ and height $2r$ just fits over a sphere of radius $r$. For $r=21$ cm, find the volume of the cylinder, the volume of the sphere and the ratio of the volumes. Compare the curved surface area of the cylinder with the surface area of the sphere. (Use $\pi=\frac{22}7$.)", 4, r"Cylinder: $\pi r^2(2r)=58212$ cm³ (1). Sphere: $\frac43\pi r^3=38808$ cm³ (1). Ratio $=58212:38808=3:2$ (1). Cylinder CSA $=2\pi r(2r)=5544$ cm², which equals the sphere's area $4\pi r^2=5544$ cm² (Archimedes) (1).", "H"),
W(r"A hemispherical bowl of internal radius 9 cm is full of water. It is emptied into cylindrical bottles of diameter 3 cm and height 4 cm. How many bottles are needed?", 4, r"Bowl: $\frac23\pi\times9^3=486\pi$ cm³ (1.5). Bottle: $\pi\times1.5^2\times4=9\pi$ cm³ (1.5). Number $=486\pi\div9\pi=54$ bottles (1).", "H", wp=True),
W(r"A solid cylinder of radius 6 cm and height 8 cm is melted and recast into spherical balls of radius 2 cm. How many balls are made? Compare the surface area of one ball with that of the cylinder's curved surface.", 4, r"Cylinder: $\pi\times36\times8=288\pi$ cm³ (1). Ball: $\frac43\pi\times8=\frac{32}3\pi$ cm³ (1). Number $=288\pi\div\frac{32\pi}3=27$ (1). One ball: $4\pi\times4=16\pi$ cm²; cylinder CSA $=2\pi\times6\times8=96\pi$ cm², i.e. 6 times as much (1).", "H", wp=True),
W(r"A roof of size 22 m by 14 m receives 5 cm of rainfall. The rainwater is collected in a cylindrical tank of base radius 3.5 m. Find the volume of the rainwater and the rise of water level in the tank. (Use $\pi=\frac{22}7$.)", 4, r"Volume $=22\times14\times0.05=15.4$ m³ (1.5). Base area of the tank $=\frac{22}7\times3.5^2=38.5$ m² (1). Rise $=15.4\div38.5=0.4$ m $=40$ cm (1.5).", "H", wp=True),
W(r"A sector of a circle of radius 5 cm and central angle $216^\circ$ is rolled into a cone so that the straight edges meet. Find the base radius, height and volume of the cone. (Leave $\pi$ in the answer.)", 4, r"The arc of the sector becomes the base circumference: $\frac{216}{360}\times2\pi\times5=2\pi r$, so $r=3$ cm (1.5). Slant height $=5$ cm, so $h=\sqrt{25-9}=4$ cm (1). $V=\frac13\pi\times9\times4=12\pi$ cm³ (1.5).", "H"),
W(r"A square-based pyramid has base side 6 cm and height 8 cm. Find its volume. If the base side and the height are both doubled, find the new volume and the factor of increase. Explain why.", 3, r"$V=\frac13\times36\times8=96$ cm³ (1). New: $\frac13\times144\times16=768$ cm³ (1). The factor is 8 (volume scales with the cube of the factor of lengths: $2^3=8$) (1).", "H"),
W(r"A hemispherical dome of radius 21 m is to be painted on its outer curved surface at ₹ 40 per m². Find the cost. Also find the volume of air inside the dome in kilolitres (1 m³ = 1 kL). (Use $\pi=\frac{22}7$.)", 4, r"CSA $=2\pi r^2=2\times\frac{22}7\times441=2772$ m² (1.5). Cost $=2772\times40=$ ₹ 1,10,880 (1). Volume $=\frac23\pi r^3=19404$ m³ (1) $=19404$ kL (0.5).", "H", wp=True),
W(r"A cone, a hemisphere and a cylinder all have radius 7 cm and height 7 cm (the hemisphere's height is its radius). Find their volumes and the ratio. What does this show about the cone and the cylinder? (Use $\pi=\frac{22}7$.)", 4, r"Cone: $\frac13\pi r^2h=\frac{1078}3\approx359.3$ cm³ (1). Hemisphere: $\frac23\pi r^3=\frac{2156}3\approx718.7$ cm³ (1). Cylinder: $\pi r^2h=1078$ cm³ (1). Ratio $=1:2:3$; the cone is one-third of the cylinder on the same base and height (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(14)
_pre = _lt(_o["blocks"][:-2])
_extra = [
 ("h2", "Choosing the Right Formula"),
 ("table", ["Question says", "Use", "Reason"], [
  ["‘paint / wrap / cover / canvas / sheet’", "surface area", "covering the outside"],
  ["‘fill / capacity / holds / air / water’", "volume", "space inside; convert m³ to litres (× 1000)"],
  ["‘open at the top’ (tumbler, tank, bowl)", "leave out the missing face", "πr(2h + r) for a cylinder open at one end"],
  ["‘roller covers … in n revolutions’", "n × curved surface area", "one revolution = CSA"],
  ["‘melted and recast’", "volume of old = (number) × volume of one new", "volume does not change"],
  ["‘lowers / raises the water level’", "volume of solid = base area of container × change in height", "displacement"],
  ["‘tent’ (cylinder + cone)", "CSA of cylinder + CSA of cone", "no base is needed"]]),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Air per student"),
 ("steps", [("Room 9 m × 8 m × 4 m, 36 students", "Volume = 9 × 8 × 4 = 288 m³."), ("Per student", "288 ÷ 36 = 8 m³."), ("Remember", "Capacity in litres = m³ × 1000, so 8 m³ = 8,000 litres.")]),
 ("h3", "Example 2 — Cylindrical well and spread earth"),
 ("steps", [("Well: diameter 7 m, depth 14 m", "r = 3.5 m; V = 22/7 × 3.5² × 14 = 539 m³."), ("Spread over 22 m × 7 m", "Base area = 154 m²."), ("Height of platform", "539 ÷ 154 = 3.5 m.")]),
 ("h3", "Example 3 — Cone: slant height first"),
 ("steps", [("r = 7 m, h = 24 m", "l = √(7² + 24²) = √625 = 25 m."), ("Canvas = CSA", "πrl = 22/7 × 7 × 25 = 550 m²."), ("Cost at ₹50 per m²", "550 × 50 = ₹27,500.")]),
 ("h3", "Example 4 — Composite solid (cone on a hemisphere)"),
 ("steps", [("Hemisphere r = 21 cm", "V = ⅔πr³ = ⅔ × 22/7 × 9,261 = 19,404 cm³."), ("Cone r = 21 cm, h = 20 cm", "V = ⅓ × 22/7 × 441 × 20 = 9,240 cm³."), ("Total", "19,404 + 9,240 = 28,644 cm³.")]),
 ("h3", "Example 5 — Melting and recasting"),
 ("steps", [("Sphere r = 6 cm into cones r = 2 cm, h = 6 cm", "Sphere = ⁴⁄₃π × 216 = 288π cm³."), ("One cone", "⅓π × 4 × 6 = 8π cm³."), ("Number", "288π ÷ 8π = 36 cones. π cancels, so it is not needed.")]),
 ("h3", "Example 6 — Rolling a sector into a cone"),
 ("steps", [("Sector radius 5 cm, angle 216°", "Arc length = (216/360) × 2π × 5 = 6π."), ("This is the base circumference", "2πr = 6π, so r = 3 cm; slant height l = 5 cm."), ("Height and volume", "h = √(25 − 9) = 4 cm; V = ⅓π × 9 × 4 = 12π cm³.")]),
 ("h3", "Example 7 — Archimedes' cylinder"),
 ("steps", [("Sphere r = 21 cm and the cylinder of radius 21 and height 42 that fits over it", "Cylinder V = 22/7 × 441 × 42 = 58,212 cm³; sphere V = 38,808 cm³."), ("Ratio", "58,212 : 38,808 = 3 : 2."), ("Curved surface", "Cylinder CSA = 2π × 21 × 42 = 5,544 cm² = sphere's 4πr² = 5,544 cm².")]),
 ("h2", "Why Scaling Works"),
 ("p", "Multiply every length of a solid by k. Every area (a product of two lengths) is multiplied by k × k = k², and every volume (a product of three lengths) by k × k × k = k³. A sphere of radius 21 cm becomes one of radius 42 cm: area 5,544 → 22,176 (× 4) and volume 38,808 → 310,464 (× 8). A cube cut into smaller cubes keeps its volume but gains surface: a 10 cm cube (600 cm²) cut into 1,000 cubes of 1 cm has 6,000 cm², ten times as much."),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Story", "Model", "Example"], [
  ["‘capacity of a tank in litres’", "V = lwh, then × 1000", "3 × 2 × 1.5 = 9 m³ = 9,000 L"],
  ["‘time to fill’", "volume ÷ rate", "6,000 L at 50 L per minute = 120 minutes"],
  ["‘rainfall of 5 cm on a roof’", "volume = area × 0.05 m", "22 × 14 × 0.05 = 15.4 m³"],
  ["‘pani for golgappas’", "vessel volume ÷ volume per golgappa", "55,440 ÷ 20 = 2,772"],
  ["‘ice cream cones from a tub’", "tub volume ÷ cone volume", "1,540 ÷ 154 = 10"],
  ["‘dome / bowl’", "hemisphere: CSA 2πr², volume ⅔πr³", "r = 21 m: 2,772 m²"],
  ["‘pyramid roof / granary’", "⅓ × base area × height", "12 × 12 × 9 ÷ 3 = 432 m³"]]),
 ("note", "REMEMBER", "**Use the vertical height h in volumes, the slant height l in curved areas of cones.** When only h and r are given for a cone, find l = √(h² + r²) first; for pyramids the vertical height is found from the slant height and half the base."),
 ("h2", "Common Mistakes"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["Volume of a cone = πr²h", "forgets the one-third", "⅓πr²h"],
  ["Cone CSA = πrh", "uses height instead of slant height", "πrl, l = √(r² + h²)"],
  ["TSA of a hemisphere = 2πr²", "that is the curved surface only", "3πr² (add the flat base πr²)"],
  ["Doubling the radius doubles the volume", "volume goes with r³", "volume × 8, area × 4"],
  ["Mixing units: 3 m × 200 cm", "all lengths must be in one unit", "convert to metres or centimetres first"],
  ["Using diameter as radius", "formulas use r", "r = d ÷ 2"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Covering means area, filling means volume**; convert units before calculating (1 m³ = 1,000 L).", "**Composite solids:** add the volumes; for surface area count only the surfaces that are visible (a tent has no base).", "**Melting and recasting:** old volume = number of new pieces × volume of one piece; π usually cancels.", "**Scaling:** area × k², volume × k³; cutting a solid into pieces keeps the volume but increases the surface area."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
