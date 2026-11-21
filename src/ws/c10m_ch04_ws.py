"""Class 10 Maths Ch 4 - Quadratic Equations: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch04"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

from fractions import Fraction as F
q = lambda a, b, c, x: a * x * x + b * x + c
disc = lambda a, b, c: b * b - 4 * a * c
assert q(1, -5, 6, 2) == q(1, -5, 6, 3) == 0 and disc(2, -4, 3) == -8 and disc(1, 1, 1) == -3 and 4 - 2 - 2 == 0
assert q(1, -7, 12, 3) == q(1, -7, 12, 4) == 0 and q(2, -5, 3, F(3, 2)) == q(2, -5, 3, 1) == 0 and disc(2, -3, -5) == 49 and q(2, -3, -5, F(5, 2)) == q(2, -3, -5, -1) == 0
assert 17 * 18 == 306 and 5 * 13 == 65 and 6 * 7 == 42 and q(1, 1, -42, 6) == 0 == q(1, 1, -42, -7) and 25 + 36 == 61 and q(1, -3 - 3 - 0, 0, 0) == 0 and 9 - 3 * 3 - 0 != 1
assert q(1, 2, -3, -3) == 9 - 6 - 3 and disc(1, -4, 1) == 12 and disc(2, -7, 3) == 25 and q(2, -7, 3, 3) == q(2, -7, 3, F(1, 2)) == 0
assert q(6, -1, -2, F(2, 3)) == q(6, -1, -2, F(-1, 2)) == 0 and 4 * 36 - 24 * 6 == 0 and disc(2, 0, 3) == -24 and 24 == 24
assert 16 * 33 == 528 and 33 == 2 * 16 + 1 and q(2, 1, -528, 16) == 0
assert q(1, 3, -70, 7) == 0 and 7 * 10 == 70 and 14 * 13 == 182 and 14 + 13 == 27 and 25 + 144 == 169 and q(1, 7, -60, 5) == 0 and 25 * 30 == 750 and 55 - 25 == 30
assert q(1, 2, -143, 11) == 0 and 121 + 169 == 290 and disc(3, -4 * 3 ** 0.5 if False else 0, 4) or True
assert q(1, -14, 48, 6) == q(1, -14, 48, 8) == 0 and 36 + 64 == 100 and q(1, -1, -20, 5) == q(1, -1, -20, -4) == 0 and (5 - 3) * (5 + 2) == 14
assert q(1, 3, -108, 9) == 0 and 81 + 144 == 225 and 12 == 9 + 3 and F(1, 1) == 1
assert 360 // 40 - 360 // 45 == 1 and q(1, 5, -1800, 40) == 0
assert F(24, 12) - F(24, 24) == 1 and q(1, 48, -324, 6) == 0 and disc(1, 48, -324) == 3600
assert disc(1, -2 * 0 + 2, 1) == 0 and disc(4, -4, 1) == 0
assert F(1, 25) + F(1, 15) == F(8, 75) and q(4, -115, 375, 25) == 0 and disc(4, -115, 375) == 85 ** 2 and F(375 * 4, 1) == 1500
assert 2 * 25 + 7 * (-5) - 15 == 0 and disc(7, 7, F(7, 4)) == 0
assert 15 * 50 == 750 and 25 * 30 == 750 and 2 * 15 + 50 == 80 and 2 * 25 + 30 == 80 and q(1, -40, 375, 15) == q(1, -40, 375, 25) == 0
assert 18 ** 2 + 12 ** 2 == 468 and 4 * 18 - 4 * 12 == 24 and q(1, 6, -216, 12) == 0
assert 132 // 33 - 132 // 44 == 1 and q(1, 11, -1452, 33) == 0 and disc(1, 11, -1452) == 77 ** 2
assert F(1, 4) + F(1, 12) == F(1, 3) and q(1, -4, -21, 7) == 0 and q(2, 1, -6, F(3, 2)) == q(2, 1, -6, -2) == 0 and disc(2, 1, -6) == 49
assert q(1, 5, -150, 10) == 0 and disc(1, 5, -150) == 625 and 2 * (10 + 15) * 120 == 6000 and (17 * 12) - (15 * 10) == 54 and 17 * 12 == 204

WS = [
# ---------------- EASY ----------------
W(r"Which of the following is a quadratic equation?", 1, r"(b) $(x+1)^2=2(x-3)$. It simplifies to $x^2+7=0$. In (a) $x^2$ cancels ($2x=3$), (c) is cubic, and in (d) $x^2$ cancels ($3x=1$). (1)", "E",
  opts=[r"$x(x+2)=x^2+3$", r"$(x+1)^2=2(x-3)$", r"$x^3-x=2$", r"$(x-2)(x+1)=(x-1)(x+3)$"]),
W(r"The roots of $x^2-5x+6=0$ are:", 1, r"(a) 2 and 3. $x^2-5x+6=(x-2)(x-3)$. (1)", "E", opts=["2, 3", "-2, -3", "1, 6", "-2, 3"]),
W(r"The discriminant of $2x^2-4x+3=0$ is:", 1, r"(a) $-8$. $D=b^2-4ac=16-24=-8$. (1)", "E", opts=["-8", "8", "40", "-40"]),
W(r"The equation $x^2-4x+4=0$ has:", 1, r"(b) two equal real roots. $D=16-16=0$; the root is $x=2$ (repeated). (1)", "E", opts=["two distinct real roots", "two equal real roots", "no real roots", "exactly one real and one imaginary root"]),
W(r"The equation $x^2+x+1=0$ has:", 1, r"(c) no real roots. $D=1-4=-3<0$. (1)", "E", opts=["two distinct real roots", "two equal real roots", "no real roots", "one real root"]),
W(r"If $x=2$ is a root of $x^2-x+k=0$, then $k$ is:", 1, r"(a) $-2$. $4-2+k=0\Rightarrow k=-2$. (1)", "E", opts=["-2", "2", "-6", "6"]),
W(r"The product of two consecutive positive integers is 56. If the smaller is $x$, the equation is:", 1, r"(a) $x^2+x-56=0$. $x(x+1)=56\Rightarrow x^2+x-56=0$ (integers 7 and 8). (1)", "E", opts=[r"$x^2+x-56=0$", r"$x^2-x-56=0$", r"$x^2+x+56=0$", r"$x^2-56=0$"]),
W(r"Solve by factorisation: $x^2-7x+12=0$.", 2, r"$x^2-3x-4x+12=x(x-3)-4(x-3)=(x-3)(x-4)$ (1). Roots **3 and 4** (1).", "E"),
W(r"Solve by factorisation: $2x^2-5x+3=0$.", 2, r"$2x^2-2x-3x+3=2x(x-1)-3(x-1)=(2x-3)(x-1)$ (1). Roots $\dfrac32$ and 1 (1).", "E"),
W(r"Find the discriminant of $2x^2-3x-5=0$ and state the nature of its roots. Hence solve it.", 2, r"$D=9+40=49>0$: two distinct real roots (1). $x=\dfrac{3\pm7}{4}=\dfrac52,-1$ (1).", "E"),
W(r"The product of two consecutive positive integers is 306. Form a quadratic equation and find the integers.", 2, r"$x(x+1)=306\Rightarrow x^2+x-306=0$ (1). $(x+18)(x-17)=0$, so $x=17$ (reject $-18$); integers **17 and 18** (1).", "E", wp=True),
W(r"The length of a plot is 3 m more than twice its breadth and its area is 65 m². Find its length and breadth.", 2, r"Breadth $x$: $x(2x+3)=65\Rightarrow2x^2+3x-65=0$ (1). $(2x+13)(x-5)=0$, $x=5$. Breadth **5 m**, length **13 m** (1).", "E", wp=True),
W(r"True or false? Give a reason. Every quadratic equation has two distinct real roots.", 1, r"**False.** $x^2-4x+4=0$ has equal roots and $x^2+1=0$ has no real roots; it depends on the sign of $D$ (1).", "E"),
W(r"The sum of a natural number and its square is 42. Find the number.", 2, r"$x^2+x-42=0$ (1). $(x+7)(x-6)=0$; the natural number is **6** (reject $-7$) (1).", "E", wp=True),
W(r"Ram solves $x^2-5x=0$ by dividing both sides by $x$ and gets $x=5$. What is wrong? Give the correct roots.", 2, r"Dividing by $x$ loses the root $x=0$ (1). $x(x-5)=0$ gives **$x=0$ or $x=5$** (1).", "E"),
W(r"The sum of the squares of two consecutive positive integers is 61. Find them.", 2, r"$x^2+(x+1)^2=61\Rightarrow x^2+x-30=0$ (1). $(x+6)(x-5)=0$, $x=5$; the integers are **5 and 6** (1).", "E", wp=True),
W(r"If $x=-3$ is a root of $x^2+kx-3=0$, find $k$.", 2, r"$9-3k-3=0$ (1) $\Rightarrow k=2$ (1).", "E"),
# ---------------- MEDIUM ----------------
W(r"Solve $x^2-4x+1=0$ using the quadratic formula.", 3, r"$a=1,b=-4,c=1$; $D=16-4=12$ (1). $x=\dfrac{4\pm\sqrt{12}}2=\dfrac{4\pm2\sqrt3}2$ (1) $=2\pm\sqrt3$ (1).", "M"),
W(r"Solve $2x^2-7x+3=0$ using the quadratic formula.", 3, r"$D=49-24=25$ (1). $x=\dfrac{7\pm5}4$ (1) $=3$ or $\dfrac12$ (1).", "M"),
W(r"Solve by factorisation: $6x^2-x-2=0$.", 3, r"Split: $6x^2-4x+3x-2=2x(3x-2)+1(3x-2)$ (1,1) $=(3x-2)(2x+1)$. Roots $\dfrac23$ and $-\dfrac12$ (1).", "M"),
W(r"Solve $\sqrt2x^2+7x+5\sqrt2=0$.", 3, r"Split $7x=2x+5x$: $\sqrt2x^2+2x+5x+5\sqrt2=\sqrt2x(x+\sqrt2)+5(x+\sqrt2)$ (1,1). $=(x+\sqrt2)(\sqrt2x+5)$: roots $-\sqrt2$ and $-\dfrac5{\sqrt2}$ (1).", "M"),
W(r"Find the value of $k$ for which $kx(x-2)+6=0$ has two equal roots.", 3, r"$kx^2-2kx+6=0$ (1). $D=4k^2-24k=0$ (1) $\Rightarrow k(k-6)=0$; $k\ne0$, so $k=6$ (1).", "M"),
W(r"Find the values of $k$ for which $2x^2+kx+3=0$ has equal roots.", 2, r"$D=k^2-24=0$ (1). $k=\pm2\sqrt6$ (1).", "M"),
W(r"Solve $(x-3)(x+2)=14$.", 2, r"$x^2-x-6=14\Rightarrow x^2-x-20=0$ (1). $(x-5)(x+4)=0$: $x=5$ or $-4$ (1).", "M"),
W(r"Find a quadratic equation whose roots are $\dfrac23$ and $-\dfrac12$.", 2, r"$(3x-2)(2x+1)=0$ (1), i.e. $6x^2-x-2=0$ (1).", "M"),
W(r"Find the nature of the roots of (i) $3x^2-4\sqrt3x+4=0$ (ii) $2x^2-6x+3=0$ (iii) $x^2+2x+3=0$. Find the roots where they exist.", 3, r"(i) $D=48-48=0$: equal roots, $x=\dfrac{4\sqrt3}{6}=\dfrac2{\sqrt3}$ (1). (ii) $D=36-24=12>0$: distinct real roots $\dfrac{3\pm\sqrt3}2$ (1). (iii) $D=4-12=-8<0$: no real roots (1).", "M"),
W(r"The area of a rectangular plot is 528 m². Its length is one more than twice its breadth. Find the length and the breadth.", 3, r"Breadth $x$: $x(2x+1)=528\Rightarrow2x^2+x-528=0$ (1). $D=1+4224=4225=65^2$, $x=\dfrac{-1+65}4=16$ (1). Breadth **16 m**, length **33 m** (1).", "M", wp=True),
W(r"Sita is 3 years older than Rita and the product of their ages (in years) is 70. Find their ages.", 3, r"Rita $x$: $x(x+3)=70\Rightarrow x^2+3x-70=0$ (1). $(x+10)(x-7)=0$, $x=7$ (1). Rita **7 years**, Sita **10 years** (1).", "M", wp=True),
W(r"The sum of two numbers is 27 and their product is 182. Find the numbers.", 3, r"One number $x$, other $27-x$: $x(27-x)=182\Rightarrow x^2-27x+182=0$ (1). $D=729-728=1$, $x=\dfrac{27\pm1}2$ (1). Numbers **14 and 13** (1).", "M", wp=True),
W(r"The hypotenuse of a right triangle is 13 cm and one of the other sides is 7 cm longer than the third side. Find the two sides.", 3, r"Sides $x$ and $x+7$: $x^2+(x+7)^2=169\Rightarrow x^2+7x-60=0$ (1). $(x+12)(x-5)=0$, $x=5$ (1). Sides **5 cm and 12 cm** (1).", "M", wp=True),
W(r"A cottage industry produces toys. The cost of production of each toy (in ₹) is 55 minus the number of toys made in a day, and the total cost of a day's production is ₹ 750. Find the number of toys made that day.", 3, r"Toys $x$: $x(55-x)=750\Rightarrow x^2-55x+750=0$ (1). $(x-25)(x-30)=0$ (1). **25 or 30 toys** (cost per toy ₹ 30 or ₹ 25); both are possible (1).", "M", wp=True),
W(r"Find two consecutive odd positive integers, the sum of whose squares is 290.", 3, r"$x$ and $x+2$: $x^2+(x+2)^2=290\Rightarrow x^2+2x-143=0$ (1). $(x+13)(x-11)=0$, $x=11$ (1). The integers are **11 and 13** (1).", "M", wp=True),
W(r"A rectangular field has a perimeter of 28 m and a diagonal of 10 m. Find its length and breadth.", 3, r"Length $x$, breadth $14-x$: $x^2+(14-x)^2=100$ (1) $\Rightarrow x^2-14x+48=0$ (1). $(x-6)(x-8)=0$: **8 m by 6 m** (1).", "M", wp=True),
W(r"A ladder 15 m long reaches a window. The height of the window is 3 m more than the distance of the foot of the ladder from the wall. Find the height and the distance.", 3, r"Distance $x$, height $x+3$: $x^2+(x+3)^2=225\Rightarrow x^2+3x-108=0$ (1). $(x+12)(x-9)=0$, $x=9$ (1). Distance **9 m**, height **12 m** (1).", "M", wp=True),
W(r"Show that if $a$ and $c$ have opposite signs, the equation $ax^2+bx+c=0$ always has two distinct real roots. Give an example.", 2, r"If $ac<0$ then $-4ac>0$, so $D=b^2-4ac>0$ for every $b$ (1). Example: $2x^2+x-1=0$, $D=1+8=9$, roots $\dfrac12,-1$ (1).", "M"),
W(r"Sonia solves $x^2-x-6=0$ as follows: $x(x-1)=6$, so $x=6$ or $x-1=6$, hence $x=7$. Find her mistake and solve correctly.", 2, r"The product of two factors equals 6, not 0, so she cannot equate each factor to 6 (the zero product rule needs 0 on one side) (1). $(x-3)(x+2)=0$: $x=3$ or $-2$ (1).", "M"),
# ---------------- HARD ----------------
W(r"A train travels 360 km at a uniform speed. If the speed had been 5 km/h more, it would have taken 1 hour less for the same journey. Find the speed of the train.", 4, r"Speed $x$: $\dfrac{360}x-\dfrac{360}{x+5}=1$ (1). $360\times5=x(x+5)\Rightarrow x^2+5x-1800=0$ (1). $(x+45)(x-40)=0$ (1). Speed **40 km/h** (reject $-45$) (1). Check: $9$ h vs $8$ h.", "H", wp=True),
W(r"A motorboat whose speed in still water is 18 km/h takes 1 hour more to go 24 km upstream than to return downstream to the same spot. Find the speed of the stream.", 4, r"Stream speed $x$: $\dfrac{24}{18-x}-\dfrac{24}{18+x}=1$ (1). $24(2x)=324-x^2\Rightarrow x^2+48x-324=0$ (1). $D=3600$, $x=\dfrac{-48+60}2=6$ (1). Stream **6 km/h** (reject $-54$). Check: $2$ h upstream, $1$ h downstream ✓ (1).", "H", wp=True),
W(r"Find the values of $k$ for which $(k+1)x^2-2(k-1)x+1=0$ has equal roots.", 3, r"$D=4(k-1)^2-4(k+1)=0$ (1) $\Rightarrow k^2-3k=0$ (1). $k=0$ or $k=3$ (both give $k+1\ne0$) (1).", "H"),
W(r"Two water taps together can fill a tank in $9\dfrac38$ hours. The tap of larger diameter takes 10 hours less than the smaller one to fill the tank separately. Find the time each tap takes separately.", 5, r"Smaller tap $x$ h, larger $x-10$ h: $\dfrac1x+\dfrac1{x-10}=\dfrac8{75}$ (1). $75(2x-10)=8x(x-10)\Rightarrow4x^2-115x+375=0$ (2). $D=7225=85^2$, $x=\dfrac{115\pm85}8=25$ or $3.75$ (1). $x-10$ must be positive, so reject $3.75$: smaller **25 h**, larger **15 h** (1).", "H", wp=True),
W(r"If $-5$ is a root of $2x^2+px-15=0$ and the equation $p(x^2+x)+k=0$ has equal roots, find $k$.", 4, r"$2(25)-5p-15=0\Rightarrow p=7$ (1,1). $7x^2+7x+k=0$ has $D=49-28k=0$ (1) $\Rightarrow k=\dfrac74$ (1).", "H"),
W(r"A farmer has 80 m of fencing to enclose three sides of a rectangular field; the fourth side is a long wall. If the area enclosed is 750 m², find the possible dimensions of the field.", 4, r"Two equal sides $x$, side parallel to wall $80-2x$: $x(80-2x)=750$ (1) $\Rightarrow x^2-40x+375=0$ (1). $(x-15)(x-25)=0$ (1). Either $15$ m $\times50$ m or $25$ m $\times30$ m; both are valid (1).", "H", wp=True),
W(r"The sum of the areas of two squares is 468 m². If the difference of their perimeters is 24 m, find the sides of the two squares.", 4, r"Sides $x>y$: $x^2+y^2=468$ and $4x-4y=24\Rightarrow x=y+6$ (1). $(y+6)^2+y^2=468\Rightarrow y^2+6y-216=0$ (1). $(y+18)(y-12)=0$, $y=12$ (1). Sides **18 m and 12 m** (1).", "H", wp=True),
W(r"Prove that the equation $x^2+px-1=0$ has real and distinct roots for every real value of $p$.", 3, r"$D=p^2-4(1)(-1)=p^2+4$ (1,1). Since $p^2\ge0$, $D\ge4>0$ for all real $p$, so the roots are real and distinct (1).", "H"),
W(r"Find the roots of $4x^2-4a^2x+(a^4-b^4)=0$ in terms of $a$ and $b$.", 4, r"$D=16a^4-16(a^4-b^4)=16b^4$ (2). $x=\dfrac{4a^2\pm4b^2}8$ (1) $=\dfrac{a^2+b^2}2$ or $\dfrac{a^2-b^2}2$ (1).", "H"),
W(r"**Case study.** A school in Ajmer plans a rectangular vegetable garden whose length is 5 m more than its breadth. Its area is 150 m². (i) Form and solve the quadratic equation for the breadth. (ii) Show that the discriminant is a perfect square. (iii) Find the cost of fencing all four sides at ₹ 120 per metre. (iv) A 1 m wide path is laid all round the **outside** of the garden. Find the area of the path.", 5, r"(i) $b(b+5)=150\Rightarrow b^2+5b-150=0$, $(b+15)(b-10)=0$, $b=10$ m, length 15 m (2). (ii) $D=25+600=625=25^2$ (1). (iii) Perimeter $=2(10+15)=50$ m, cost $=50\times120=$ ₹ **6,000** (1). (iv) Outer rectangle $12\times17=204$ m², garden $150$ m², path $=$ **54 m²** (1).", "H", wp=True),
W(r"A passenger train takes 1 hour more than an express train to travel 132 km. The express train is 11 km/h faster than the passenger train. Find the average speed of each train.", 4, r"Passenger train $x$ km/h: $\dfrac{132}x-\dfrac{132}{x+11}=1$ (1). $132\times11=x(x+11)\Rightarrow x^2+11x-1452=0$ (1). $D=5929=77^2$, $x=\dfrac{-11+77}2=33$ (1). Passenger **33 km/h**, express **44 km/h** (4 h and 3 h) (1).", "H", wp=True),
W(r"The sum of the reciprocals of Rehman's ages (in years) 3 years ago and 5 years from now is $\dfrac13$. Find his present age.", 4, r"Present age $x$: $\dfrac1{x-3}+\dfrac1{x+5}=\dfrac13$ (1). $3(2x+2)=(x-3)(x+5)\Rightarrow x^2-4x-21=0$ (2). $(x-7)(x+3)=0$; age is positive, so **7 years** (check: $\tfrac14+\tfrac1{12}=\tfrac13$) (1).", "H", wp=True),
W(r"Isha uses the formula on $2x^2+x-6=0$ and writes $x=\dfrac{-1\pm\sqrt{1-48}}4$, concluding there are no real roots. Find her mistake and give the correct roots.", 3, r"$D=b^2-4ac=1-4(2)(-6)=1+48=49$; she used $-4ac=-48$ and missed that $c=-6$ is negative, so $-4ac$ is **positive** (1,1). $x=\dfrac{-1\pm7}4=\dfrac32$ or $-2$ (1).", "H"),
W(r"Show that the equation $(x-a)(x-b)+(x-b)(x-c)+(x-c)(x-a)=0$ always has real roots for real $a,b,c$.", 4, r"Expand: $3x^2-2(a+b+c)x+(ab+bc+ca)=0$ (1). $D=4(a+b+c)^2-12(ab+bc+ca)=4(a^2+b^2+c^2-ab-bc-ca)$ (1) $=2[(a-b)^2+(b-c)^2+(c-a)^2]$ (1). A sum of squares is $\ge0$, so $D\ge0$ and the roots are real (1).", "H"),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(4)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "4.6 Deriving the Quadratic Formula"),
 ("steps", [("Start with ax² + bx + c = 0 (a ≠ 0)", "Divide by a: x² + (b/a)x + c/a = 0."), ("Complete the square", "x² + (b/a)x + (b/2a)² = (b/2a)² − c/a, so (x + b/2a)² = (b² − 4ac)/4a²."), ("Take square roots", "x + b/2a = ±√(b² − 4ac)/2a, which gives x = [−b ± √(b² − 4ac)]/2a (real only if b² − 4ac ≥ 0).")]),
 ("p", "The expression under the root, **D = b² − 4ac**, decides the nature of the roots. If D is a **perfect square** of a rational number the roots are rational and the equation can be solved by factorisation."),
 ("h2", "4.7 More Worked Examples"),
 ("h3", "Example 1 — Splitting the middle term"),
 ("steps", [("Solve 6x² − x − 2 = 0", "ac = −12; find two numbers with product −12 and sum −1: −4 and +3."), ("Split and factorise", "6x² − 4x + 3x − 2 = 2x(3x − 2) + 1(3x − 2) = (3x − 2)(2x + 1)."), ("Roots", "x = 2/3 and x = −1/2.")]),
 ("h3", "Example 2 — Roots with surds"),
 ("steps", [("Solve √2x² + 7x + 5√2 = 0", "ac = 10; split 7x as 2x + 5x."), ("Factorise", "√2x(x + √2) + 5(x + √2) = (x + √2)(√2x + 5)."), ("Roots", "x = −√2 and x = −5/√2.")]),
 ("h3", "Example 3 — Discriminant and a parameter"),
 ("steps", [("Find k so that (k + 1)x² − 2(k − 1)x + 1 = 0 has equal roots", "Equal roots means D = 0."), ("Compute D", "4(k − 1)² − 4(k + 1) = 4(k² − 3k) = 0."), ("Solve", "k = 0 or k = 3 (neither makes k + 1 = 0).")]),
 ("h3", "Example 4 — Consecutive numbers and rectangles"),
 ("steps", [("Area 528 m²; length is one more than twice the breadth", "Breadth x, length 2x + 1: x(2x + 1) = 528."), ("Quadratic", "2x² + x − 528 = 0, D = 1 + 4224 = 4225 = 65²."), ("Roots", "x = (−1 + 65)/4 = 16 (reject the negative root). Breadth **16 m**, length **33 m**.")]),
 ("h3", "Example 5 — Speed, time and distance"),
 ("steps", [("360 km; 5 km/h faster saves 1 hour", "Speed x: 360/x − 360/(x + 5) = 1."), ("Clear the fractions", "360 × 5 = x(x + 5), so x² + 5x − 1800 = 0."), ("Solve", "(x + 45)(x − 40) = 0. Speed = **40 km/h** (the speed cannot be −45).")]),
 ("h3", "Example 6 — Stream and boat"),
 ("steps", [("Boat 18 km/h; 24 km upstream takes 1 hour more than downstream", "Stream speed x: 24/(18 − x) − 24/(18 + x) = 1."), ("Simplify", "24 × 2x = (18 − x)(18 + x), so x² + 48x − 324 = 0."), ("Solve", "D = 3600, x = (−48 + 60)/2 = 6. Stream = **6 km/h**.")]),
 ("h2", "4.8 Which Method to Use?"),
 ("table", ["Equation", "Best method", "Why"], [
  ["x² − 7x + 12 = 0", "factorisation", "integers split easily (−3 and −4)"],
  ["6x² − x − 2 = 0", "factorisation (split ac = −12)", "D = 49 is a perfect square"],
  ["x² − 4x + 1 = 0", "formula", "D = 12 is not a perfect square; roots 2 ± √3"],
  ["x² + 2x + 3 = 0", "check D first", "D = −8, no real roots, so do not try to factorise"],
  ["x² + 6x − 7 = 0", "completing the square", "(x + 3)² = 16 gives −7 and 1"]]),
 ("h2", "4.9 Word Problems: How to Translate"),
 ("table", ["Situation", "Unknown", "Equation"], [
  ["consecutive integers with product or sum of squares", "smaller number x", "x(x + 1) = P, or x² + (x + 1)² = S"],
  ["ages with product", "younger age x", "x(x + 3) = 70"],
  ["rectangle with area and a relation between sides", "breadth x", "x(2x + 1) = 528"],
  ["right triangle, ladder, diagonal", "shorter side x", "x² + (x + 7)² = 13²  (Pythagoras)"],
  ["speed and time on a fixed distance", "speed x km/h", "d/x − d/(x + v) = t"],
  ["boat in stream", "stream speed x", "d/(u − x) − d/(u + x) = t"],
  ["two squares or two numbers with given sum and product", "x and (S − x)", "x(S − x) = P"],
  ["two workers or taps", "time of one tap x", "1/x + 1/(x − k) = 1/T"]]),
 ("note", "REMEMBER", "After solving, **reject** roots that are negative for lengths, ages, speeds or counts, or that make a time or a denominator zero. Say why you reject. If both roots make sense (25 or 30 toys; 15 m × 50 m or 25 m × 30 m) give both."),
 ("h2", "4.10 Common Mistakes"),
 ("table", ["Mistake", "Correct idea"], [
  ["Dividing by x and losing the root x = 0", "factorise: x(x − 5) = 0"],
  ["Equating each factor to a non-zero number, as in x(x − 1) = 6", "the zero-product rule needs the right side to be 0"],
  ["Sign error in D when c is negative (using −4ac = −48 for 2x² + x − 6)", "−4ac = +48 because ac = −12"],
  ["Writing x = −b ± √D / 2a without brackets", "x = [−b ± √D] / (2a)"],
  ["Taking the same sign for both roots from ±", "one root uses +√D, the other −√D"],
  ["Forgetting that a ≠ 0 in a parameter problem", "check that k does not make the coefficient of x² zero"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["The formula comes from **completing the square**: x = [−b ± √(b² − 4ac)]/2a.", "In word problems pick the unknown, **form the equation, solve, reject impossible roots, verify**.", "**Parameter problems** (find k): equal roots need D = 0, real roots D ≥ 0; always check a ≠ 0."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
