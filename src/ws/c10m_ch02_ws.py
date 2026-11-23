"""Class 10 Maths Ch 2 - Polynomials: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch02"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

from fractions import Fraction as F
p = lambda c, x: sum(ci * x ** i for i, ci in enumerate(c))      # coeffs low->high
assert p([4, -3, 1], 2) == 2 and p([2, 3, 1], -1) == 0 and p([12, -7, 1], 3) == 0 == p([12, -7, 1], 4)
assert p([10, -7, 1], 2) == 0 == p([10, -7, 1], 5) and (6 + 3 - 10 + 0) == -1 and 36 + 18 - 10 == 44
assert p([-3, -7, 6], F(3, 2)) == 0 and p([-3, -7, 6], F(-1, 3)) == 0 and F(3, 2) + F(-1, 3) == F(7, 6)
assert 25 - 12 == 13 and F(5, 6) == F(5) / 6 and p([-2, 3, 2], F(1, 2)) == 0 and p([-2, 3, 2], -2) == 0
assert p([6, -5, 1], 2) == 0 and p([20, -9, 1], 4) == 0 == p([20, -9, 1], 5)
assert p([0, 20, -5], 0) == 0 and p([0, 20, -5], 4) == 0
assert [p([-3, -2, 1], x) for x in range(-2, 5)] == [5, 0, -3, -4, -3, 0, 5]
assert p([48, -14, 1], 6) == 0 == p([48, -14, 1], 8) and p([96, -20, 1], 8) == 0 == p([96, -20, 1], 12)
assert p([15, 10, -5], 3) == 0 and p([15, 10, -5], -1) == 0 and p([6, -4 , -2], 1) == 0 and p([0, 6, -1], 6) == 0 and p([0, 6, -1], 1) == 5 and p([0, 6, -1], 3) == 9
assert p([-3, 5, 2], F(1, 2)) == 0 and p([-3, 5, 2], -3) == 0 and p([-2, -5, 3], 2) == 0 and p([-2, -5, 3], F(-1, 3)) == 0
assert p([36, -13, 1], 4) == 0 == p([36, -13, 1], 9) and p([6, -5, 1], 3) == 0 and 9 - 6 * 3 + 9 == 0
assert p([480, -52, 1], 40) == 0 == p([480, -52, 1], 12) and 40 + 16 == 2 * (12 + 16)
assert p([6, 1, 1][::1], 0) == 6 and p([-6, 1, 1], 2) == 0 == p([-6, 1, 1], -3) and (-3) ** 3 + 2 ** 3 == -19
assert p([23, -10, 1], 5 + 2) != 0 and 7 + 2 * 6 + 4 == 23
# (k+1)x^2-10x+(2k-2) with k=3 is 4x^2-10x+4 = 2(2x-1)(x-2): zeroes 1/2 and 2 (reciprocals, real)
assert p([4, -10, 4], 2) == 0 == p([4, -10, 4], F(1, 2)) and 2 * 3 - 2 == 3 + 1

WS = [
# ---------------- EASY ----------------
W(r"The degree of the polynomial $5x^3-7x^7+2x$ is:", 1, r"(b) 7. The degree is the highest power of $x$, which is 7. (1)", "E", opts=["3", "7", "1", "5"]),
W(r"The zero of the linear polynomial $p(x)=2x-7$ is:", 1, r"(a) $\dfrac72$. $2x-7=0\Rightarrow x=\dfrac72$. (1)", "E", opts=[r"$\dfrac72$", r"$-\dfrac72$", r"$\dfrac27$", "7"]),
W(r"The graph of a quadratic polynomial lies completely above the $x$-axis. The number of zeroes of the polynomial is:", 1, r"(a) 0. Zeroes are the $x$-coordinates of points where the graph meets the $x$-axis; here it never does. (1)", "E", opts=["0", "1", "2", "3"]),
W(r"The sum of the zeroes of $x^2-5x+6$ is:", 1, r"(b) 5. Sum $=-\dfrac ba=-\dfrac{-5}{1}=5$ (zeroes 2 and 3). (1)", "E", opts=["-5", "5", "6", "-6"]),
W(r"The product of the zeroes of $2x^2-8x+3$ is:", 1, r"(a) $\dfrac32$. Product $=\dfrac ca=\dfrac32$. (1)", "E", opts=[r"$\dfrac32$", r"$-\dfrac32$", "4", "3"]),
W(r"A quadratic polynomial whose zeroes have sum 3 and product $-2$ is:", 1, r"(b) $x^2-3x-2$. The polynomial is $x^2-(\text{sum})x+\text{product}=x^2-3x+(-2)$. (1)", "E", opts=[r"$x^2+3x-2$", r"$x^2-3x-2$", r"$x^2-3x+2$", r"$x^2+3x+2$"]),
W(r"A cubic polynomial can have at most how many zeroes?", 1, r"(c) 3. A polynomial of degree $n$ has at most $n$ zeroes. (1)", "E", opts=["1", "2", "3", "4"]),
W(r"Find the zero of the polynomial $3x+5$.", 2, r"$3x+5=0$ (1) $\Rightarrow x=-\dfrac53$ (1).", "E"),
W(r"Is $x=-1$ a zero of $p(x)=x^2+3x+2$? Show your working.", 2, r"$p(-1)=(-1)^2+3(-1)+2=1-3+2$ (1) $=0$, so $-1$ **is** a zero (1).", "E"),
W(r"A tailor's charge (in hundreds of rupees) for stitching $x$ shirts is $C(x)=x^2-3x+4$. Find the charge for 2 shirts.", 2, r"$C(2)=4-6+4$ (1) $=2$, i.e. ₹ **200** (1).", "E", wp=True),
W(r"Find the zeroes of $x^2-7x+12$ by factorising.", 2, r"$x^2-7x+12=(x-3)(x-4)$ (1). Zeroes: **3 and 4** (1).", "E"),
W(r"True or false? Give a reason. A linear polynomial $ax+b$ $(a\ne0)$ has exactly one zero.", 1, r"**True.** $ax+b=0$ gives the single value $x=-\dfrac ba$ (1).", "E"),
W(r"The profit (in thousand rupees) of a small shop after $x$ months is $P(x)=x^2-7x+10$. In which months does the shop break even, i.e. $P(x)=0$?", 2, r"$x^2-7x+10=(x-2)(x-5)$ (1). Break-even in the **2nd and 5th month** (1).", "E", wp=True),
W(r"A rectangular garden has length $(x+5)$ m and breadth $(x-2)$ m. Write its area as a polynomial in standard form, state its degree and find the area when $x=6$.", 2, r"Area $=(x+5)(x-2)=x^2+3x-10$, degree 2 (1). At $x=6$: $36+18-10=$ **44 m²** (1).", "E", wp=True),
W(r"Rohit says that $x^2+4$ has zeroes 2 and $-2$. Is he right? Explain.", 2, r"No. $p(2)=4+4=8\ne0$ and $p(-2)=8\ne0$ (1). $x^2+4\ge4$ for every $x$, so its graph never meets the $x$-axis and it has **no real zero** (1).", "E"),
W(r"A fruit seller's profit (in ₹) on selling $x$ dozen oranges is $30x-120$. How many dozen must he sell to neither gain nor lose?", 2, r"No gain, no loss means $30x-120=0$ (1), so $x=4$: **4 dozen** (1).", "E", wp=True),
W(r"Without finding the zeroes, write the sum and the product of the zeroes of $x^2+7x+10$.", 2, r"Sum $=-\dfrac ba=-7$ (1). Product $=\dfrac ca=10$ (1).", "E"),
# ---------------- MEDIUM ----------------
W(r"Find the zeroes of $6x^2-3-7x$ and verify the relation between the zeroes and the coefficients.", 3, r"$6x^2-7x-3=(3x+1)(2x-3)$ (1), zeroes $-\dfrac13$ and $\dfrac32$. Sum $=\dfrac76=-\dfrac{-7}{6}$ ✓ (1). Product $=-\dfrac12=\dfrac{-3}{6}$ ✓ (1).", "M"),
W(r"Find the zeroes of $4u^2+8u$ and verify the relation between zeroes and coefficients.", 3, r"$4u(u+2)=0$ (1), so $u=0$ or $u=-2$. Sum $=-2=-\dfrac84$ ✓ (1). Product $=0=\dfrac04$ ✓ (1).", "M"),
W(r"Form a quadratic polynomial whose zeroes have sum $-3$ and product 2, and find its zeroes.", 2, r"$x^2-(-3)x+2=x^2+3x+2$ (1) $=(x+1)(x+2)$, zeroes $-1,-2$ (1).", "M"),
W(r"Find a quadratic polynomial whose zeroes are $2+\sqrt3$ and $2-\sqrt3$.", 2, r"Sum $=4$, product $=(2)^2-(\sqrt3)^2=1$ (1). Polynomial: $x^2-4x+1$ (1).", "M"),
W(r"If $\alpha,\beta$ are the zeroes of $x^2-5x+6$, find (i) $\alpha^2+\beta^2$ (ii) $\dfrac1\alpha+\dfrac1\beta$.", 3, r"$\alpha+\beta=5$, $\alpha\beta=6$ (1). (i) $\alpha^2+\beta^2=25-12=13$ (1). (ii) $\dfrac{\alpha+\beta}{\alpha\beta}=\dfrac56$ (1).", "M"),
W(r"Find $k$ if the sum of the zeroes of $kx^2+2x+3k$ equals their product.", 3, r"Sum $=-\dfrac2k$, product $=\dfrac{3k}k=3$ (1). $-\dfrac2k=3$ (1) $\Rightarrow k=-\dfrac23$ (1).", "M"),
W(r"If $-2$ is a zero of $2x^2+3x+k$, find $k$ and the other zero.", 3, r"$2(4)+3(-2)+k=0\Rightarrow k=-2$ (1). Product of zeroes $=\dfrac{-2}{2}=-1$ (1), so other zero $=\dfrac{-1}{-2}=\dfrac12$ (1). (Check: $2x^2+3x-2=(2x-1)(x+2)$.)", "M"),
W(r"The area of a rectangular plot is $(x^2-x-12)$ m² and its length is $(x+3)$ m. Find the breadth by factorising the area.", 2, r"$x^2-x-12=(x-4)(x+3)$ (1). Breadth $=$ **$(x-4)$ m** (1).", "M", wp=True),
W(r"The profit (in lakh ₹) of a company in year $t$ is $P(t)=t^2-9t+20$. (i) In which years is the profit zero? (ii) Verify that the sum and product of those years agree with the coefficients.", 3, r"(i) $t^2-9t+20=(t-4)(t-5)$, so profit is zero in years **4 and 5** (1). (ii) Sum $=9=-\dfrac{-9}{1}$ ✓ (1); product $=20=\dfrac{20}{1}$ ✓ (1).", "M", wp=True),
W(r"A stone is thrown vertically upward and its height (in m) after $t$ seconds is $h(t)=20t-5t^2$. (i) After how many seconds is it back on the ground? (ii) Write the sum and product of the zeroes.", 3, r"(i) $20t-5t^2=5t(4-t)=0\Rightarrow t=0$ (throw) or $t=4$ (1,1): it lands after **4 s**. (ii) $-5t^2+20t$: sum $=-\dfrac{20}{-5}=4$, product $=0$ (1).", "M", wp=True),
W(r"The graph of $y=p(x)$ of a quadratic polynomial is a parabola opening upwards that **touches** the $x$-axis at $(3,0)$ and nowhere else. How many zeroes does $p(x)$ have? Write one possible $p(x)$.", 2, r"It meets the axis at one point only, so $p(x)$ has **one (repeated) zero**, $x=3$ (1). One possible polynomial is $(x-3)^2=x^2-6x+9$ (1).", "M"),
W(r"The table gives some values of a quadratic polynomial $p(x)$:  $x=-2,-1,0,1,2,3,4$ and $p(x)=5,0,-3,-4,-3,0,5$. (i) Read off the zeroes. (ii) Find the sum and product of the zeroes. (iii) Hence write $p(x)$.", 3, r"(i) $p(x)=0$ at $x=-1$ and $x=3$ (1). (ii) Sum $=2$, product $=-3$ (1). (iii) $p(x)=k(x^2-2x-3)$; $p(0)=-3$ gives $k=1$, so $p(x)=x^2-2x-3$ (1). (Check $p(4)=16-8-3=5$ ✓.)", "M"),
W(r"A student writes: sum of zeroes of $2x^2+5x-3$ is $\dfrac52$ and product is $\dfrac32$. Find the mistakes and give the correct values.", 2, r"She ignored the signs: sum $=-\dfrac ba=-\dfrac52$ (1) and product $=\dfrac ca=\dfrac{-3}{2}=-\dfrac32$ (1).", "M"),
W(r"True or false? Give a reason. Every quadratic polynomial has two real zeroes.", 2, r"**False** (1). $x^2+1$ is quadratic but its graph lies above the $x$-axis, so it has no real zero; a quadratic has at most two (1).", "M"),
W(r"Find a quadratic polynomial, the sum and product of whose zeroes are $-\dfrac14$ and $\dfrac14$ respectively.", 2, r"$k\left(x^2+\dfrac14x+\dfrac14\right)$ (1). With $k=4$: **$4x^2+x+1$** (1).", "M"),
W(r"If $\alpha,\beta$ are the zeroes of $2x^2-7x+3$, find $\alpha+\beta$, $\alpha\beta$ and $|\alpha-\beta|$. Verify by finding the zeroes.", 3, r"$\alpha+\beta=\dfrac72$, $\alpha\beta=\dfrac32$ (1). $(\alpha-\beta)^2=\dfrac{49}{4}-6=\dfrac{25}{4}$, so $|\alpha-\beta|=\dfrac52$ (1). Zeroes: $(2x-1)(x-3)$ gives $\dfrac12$ and 3, difference $\dfrac52$ ✓ (1).", "M"),
W(r"The sum of the length and breadth of a rectangular park is 14 m and its area is 48 m². Form a quadratic polynomial whose zeroes are the length and the breadth, and find the dimensions.", 3, r"Sum $=14$, product $=48$ (1), so the polynomial is $x^2-14x+48$ (1) $=(x-6)(x-8)$. The park is **8 m by 6 m** (1).", "M", wp=True),
W(r"Two numbers have sum 20 and product 96. Form a quadratic polynomial whose zeroes are these numbers and find them.", 2, r"$x^2-20x+96$ (1) $=(x-8)(x-12)$, so the numbers are **8 and 12** (1).", "M", wp=True),
W(r"Find the zeroes of $x^2-3$ and verify the relation between the zeroes and the coefficients.", 3, r"$x^2-3=(x-\sqrt3)(x+\sqrt3)$, zeroes $\sqrt3,-\sqrt3$ (1). Sum $=0=-\dfrac01$ ✓ (1). Product $=-3=\dfrac{-3}{1}$ ✓ (1).", "M"),
# ---------------- HARD ----------------
W(r"A diver jumps from a platform. Her height (in m) above the water $t$ seconds after the jump is $h(t)=-5t^2+10t+15$. (i) After how many seconds does she hit the water? (ii) Why is one zero of $h$ rejected? (iii) Verify that the sum and product of both zeroes agree with the coefficients.", 4, r"(i) $-5(t^2-2t-3)=-5(t-3)(t+1)=0$ gives $t=3$ or $t=-1$ (1). She hits the water after **3 s** (1). (ii) $t=-1$ is before the jump, so time cannot be negative (1). (iii) Sum $=2=-\dfrac{10}{-5}$ ✓, product $=-3=\dfrac{15}{-5}$ ✓ (1).", "H", wp=True),
W(r"If $\alpha,\beta$ are the zeroes of $x^2-5x+k$ and $\alpha-\beta=1$, find $k$.", 3, r"$\alpha+\beta=5$ and $\alpha-\beta=1$ (1) give $\alpha=3,\beta=2$ (1). $k=\alpha\beta=6$ (1).", "M"),
W(r"If $\alpha,\beta$ are the zeroes of $3x^2-5x-2$, form a quadratic polynomial whose zeroes are $\dfrac1\alpha$ and $\dfrac1\beta$. Verify by finding the actual zeroes.", 4, r"$\alpha+\beta=\dfrac53$, $\alpha\beta=-\dfrac23$ (1). New sum $=\dfrac{\alpha+\beta}{\alpha\beta}=-\dfrac52$, new product $=\dfrac1{\alpha\beta}=-\dfrac32$ (1). Polynomial $x^2+\dfrac52x-\dfrac32$, i.e. $2x^2+5x-3$ (1). Check: zeroes of $3x^2-5x-2=(3x+1)(x-2)$ are $-\dfrac13,2$; reciprocals $-3,\dfrac12$ are the zeroes of $(2x-1)(x+3)$ ✓ (1).", "H"),
W(r"If $\alpha,\beta$ are the zeroes of $x^2-5x+6$, form a quadratic polynomial whose zeroes are $\alpha^2$ and $\beta^2$.", 4, r"$\alpha+\beta=5$, $\alpha\beta=6$ (1). New sum $=\alpha^2+\beta^2=25-12=13$ (1). New product $=(\alpha\beta)^2=36$ (1). Polynomial $x^2-13x+36$ (zeroes 4, 9 ✓) (1).", "H"),
W(r"If one zero of $(k+1)x^2-10x+(2k-2)$ is the reciprocal of the other, find $k$ and both zeroes.", 4, r"Zeroes $\alpha$ and $\dfrac1\alpha$, so their product is 1 (1). Product $=\dfrac{2k-2}{k+1}=1$ (1) $\Rightarrow 2k-2=k+1$, $k=3$ (1). The polynomial is $4x^2-10x+4=2(2x-1)(x-2)$, zeroes $\dfrac12$ and $2$ (1).", "H"),
W(r"If one zero of $3x^2-8x+2k+1$ is seven times the other, find the zeroes and the value of $k$.", 4, r"Let the zeroes be $\alpha$ and $7\alpha$. Sum: $8\alpha=\dfrac83\Rightarrow\alpha=\dfrac13$ (1). Zeroes $\dfrac13$ and $\dfrac73$ (1). Product: $\dfrac79=\dfrac{2k+1}{3}$ (1) $\Rightarrow 2k+1=\dfrac73$, $k=\dfrac23$ (1).", "H"),
W(r"A fountain jet leaves the nozzle at ground level at the point $(0,0)$ and lands again on the ground at $(6,0)$, where $x$ is the horizontal distance and $y$ the height in metres. At $x=1$ the water is 5 m high. (i) Find the quadratic polynomial $y=p(x)$. (ii) Verify the sum and product of its zeroes. (iii) Find the height at $x=3$.", 4, r"(i) Zeroes 0 and 6, so $p(x)=kx(x-6)$ (1). $p(1)=-5k=5\Rightarrow k=-1$, so $p(x)=-x^2+6x$ (1). (ii) Sum $=6=-\dfrac6{-1}$ ✓, product $=0=\dfrac0{-1}$ ✓ (1). (iii) $p(3)=-9+18=9$ m (1).", "H", wp=True),
W(r"Find $k$ such that the graph of $y=x^2-4x+k$ touches the $x$-axis at exactly one point, and find that point.", 3, r"A single (repeated) zero means $\alpha=\beta$ (1). Sum $=2\alpha=4\Rightarrow\alpha=2$ (1). Product $=\alpha^2=k=4$; the polynomial is $(x-2)^2$ and the point is $(2,0)$ (1).", "H"),
W(r"**Case study.** Ravi sells lassi at the Pushkar fair. His profit (in hundreds of rupees) from selling $x$ hundred glasses is $P(x)=-x^2+8x-12$. (i) For what values of $x$ is the profit zero? (ii) Verify the sum and product of these values from the coefficients. (iii) Find his profit when he sells 400 glasses. (iv) For $x=1$ find $P(1)$ and say what the sign means.", 5, r"(i) $-(x^2-8x+12)=-(x-2)(x-6)$, zero profit at $x=2$ and $x=6$, i.e. **200 and 600 glasses** (1,1). (ii) Sum $=8=-\dfrac8{-1}$, product $=12=\dfrac{-12}{-1}$ ✓ (1). (iii) $P(4)=-16+32-12=4$, profit ₹ **400** (1). (iv) $P(1)=-1+8-12=-5$, a **loss** of ₹ 500, since he has not yet covered his costs (1).", "H", wp=True),
W(r"The sum of the zeroes of a quadratic polynomial is 5 and the sum of the squares of the zeroes is 13. Find the polynomial and its zeroes.", 4, r"$\alpha+\beta=5$ and $\alpha^2+\beta^2=13$ (1). $2\alpha\beta=25-13=12$, so $\alpha\beta=6$ (1). Polynomial $x^2-5x+6$ (1), zeroes 2 and 3 (1).", "H"),
W(r"Isha wants a polynomial with zeroes 3 and $-2$. She writes $x^2+(3-2)x+3(-2)=x^2+x-6$. Find her mistake, give the correct polynomial and check it.", 3, r"The middle term must be $-(\text{sum of zeroes})x$, but she used $+(\text{sum})x$ (1). Correct polynomial: $x^2-x-6$ (1). Check: $(x-3)(x+2)=x^2-x-6$ ✓. (Her polynomial has zeroes 2 and $-3$.) (1)", "H"),
W(r"The present ages (in years) of a father and his son are the zeroes of $x^2-52x+480$. (i) Find their ages. (ii) After how many years will the father be exactly twice as old as the son?", 4, r"(i) $x^2-52x+480=(x-12)(x-40)$: son 12 years, father 40 years (2). (ii) $40+t=2(12+t)$ (1) $\Rightarrow t=16$ years (1).", "H", wp=True),
W(r"If $\alpha,\beta$ are the zeroes of $x^2-6x+7$, find a quadratic polynomial whose zeroes are $\alpha+2$ and $\beta+2$.", 3, r"$\alpha+\beta=6$, $\alpha\beta=7$ (1). New sum $=6+4=10$ (1). New product $=\alpha\beta+2(\alpha+\beta)+4=7+12+4=23$ (1). Polynomial: $x^2-10x+23$.", "H"),
W(r"If $\alpha,\beta$ are the zeroes of $x^2+x-6$, find $\alpha^3+\beta^3$ using the sum and product, and check by finding the zeroes.", 4, r"$\alpha+\beta=-1$, $\alpha\beta=-6$ (1). $\alpha^3+\beta^3=(\alpha+\beta)^3-3\alpha\beta(\alpha+\beta)$ (1) $=-1-3(-6)(-1)=-1-18=-19$ (1). Check: zeroes $2$ and $-3$: $8-27=-19$ ✓ (1).", "H"),
]
WS.sort(key=lambda w: "EMH".index(w["level"]))   # keep the parts contiguous after a re-tag
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(2)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "2.5 More Worked Examples"),
 ("h3", "Example 1 — Zeroes of a quadratic and verification"),
 ("steps", [("Find the zeroes of 6x² − 7x − 3", "Split the middle term: 6x² − 9x + 2x − 3 = 3x(2x − 3) + 1(2x − 3) = (2x − 3)(3x + 1)."), ("Zeroes", "x = 3/2 and x = −1/3."), ("Verify", "Sum = 3/2 − 1/3 = 7/6 = −(−7)/6 and product = −1/2 = −3/6. Both agree with −b/a and c/a.")]),
 ("h3", "Example 2 — Polynomial from the sum and product"),
 ("steps", [("Find a quadratic whose zeroes are 2 + √3 and 2 − √3", "Sum = 4. Product = 2² − (√3)² = 4 − 3 = 1."), ("Write the polynomial", "x² − (sum)x + product = x² − 4x + 1."), ("Any multiple works", "k(x² − 4x + 1) has the same zeroes for every non-zero k.")]),
 ("h3", "Example 3 — Finding k from a condition"),
 ("steps", [("Sum of zeroes of kx² + 2x + 3k equals their product. Find k", "Sum = −2/k and product = 3k/k = 3."), ("Equate", "−2/k = 3, so k = −2/3."), ("Check", "With k = −2/3 the sum is 3 and the product is 3.")]),
 ("h3", "Example 4 — Zero given, find the other zero and k"),
 ("steps", [("−2 is a zero of 2x² + 3x + k", "Substitute: 2(4) + 3(−2) + k = 0, so k = −2."), ("Other zero", "Product of zeroes = k/a = −2/2 = −1, so the other zero is −1 ÷ (−2) = 1/2."), ("Check", "2x² + 3x − 2 = (2x − 1)(x + 2), zeroes 1/2 and −2.")]),
 ("h3", "Example 5 — New polynomial from old zeroes"),
 ("steps", [("α, β are zeroes of 3x² − 5x − 2. Form the polynomial with zeroes 1/α and 1/β", "α + β = 5/3 and αβ = −2/3."), ("New sum and product", "1/α + 1/β = (α + β)/αβ = −5/2 and (1/α)(1/β) = 1/αβ = −3/2."), ("Polynomial", "x² + (5/2)x − 3/2, or **2x² + 5x − 3**.")]),
 ("h3", "Example 6 — A condition on the zeroes"),
 ("steps", [("One zero of 3x² − 8x + 2k + 1 is seven times the other", "Call the zeroes α and 7α."), ("Use the sum", "8α = 8/3, so α = 1/3 and the zeroes are 1/3 and 7/3."), ("Use the product", "7/9 = (2k + 1)/3, so 2k + 1 = 7/3 and **k = 2/3**.")]),
 ("h2", "2.6 Identities in α and β (quadratic only)"),
 ("table", ["Expression", "In terms of sum S = α + β and product P = αβ", "Example: S = 5, P = 6"], [
  ["α² + β²", "S² − 2P", "25 − 12 = 13"],
  ["(α − β)²", "S² − 4P", "25 − 24 = 1"],
  ["1/α + 1/β", "S/P", "5/6"],
  ["α/β + β/α", "(S² − 2P)/P", "13/6"],
  ["α³ + β³", "S³ − 3PS", "125 − 90 = 35"],
  ["α + β + αβ", "S + P", "11"]]),
 ("note", "REMEMBER", "To build a new polynomial from the zeroes of an old one, never solve the old equation if you do not have to. Find the **new sum** and **new product** in terms of S and P and write x² − (new sum)x + (new product)."),
 ("h2", "2.7 Reading Zeroes from a Graph or a Table"),
 ("table", ["What you see", "What it means", "Example"], [
  ["parabola cuts the x-axis at two points", "two distinct zeroes", "zeroes −1 and 3, polynomial k(x² − 2x − 3)"],
  ["parabola just touches the x-axis", "one repeated zero (α = β)", "(x − 3)² = x² − 6x + 9"],
  ["parabola lies entirely above or below the axis", "no real zero", "x² + 4, x² + 1"],
  ["table of values where p(x) changes sign or becomes 0", "zero at (or between) those x-values", "p(−1) = 0 and p(3) = 0"],
  ["parabola opens upward / downward", "a > 0 / a < 0", "−5t² + 20t opens downward"],
  ["graph cuts the y-axis at (0, c)", "p(0) = c, the constant term", "gives k when the zeroes are known"]]),
 ("p", "To find k in p(x) = k(x − α)(x − β) use one extra point, such as where the graph cuts the y-axis or any other value from a table."),
 ("h2", "2.8 Word Problems: How to Translate"),
 ("table", ["Situation", "Polynomial", "Meaning of a zero"], [
  ["profit or loss P(x) after x months/units", "quadratic or linear P(x)", "**break-even** point (no gain, no loss)"],
  ["height of a stone, ball, diver or fountain jet h(t)", "quadratic in t", "time or distance at which it is at ground or water level"],
  ["area of a rectangle given as a polynomial", "(length)(breadth)", "factorise to get the missing side"],
  ["two numbers (or ages, or length and breadth) with given sum and product", "x² − (sum)x + product", "the two numbers themselves"],
  ["cost as a polynomial of the number of articles", "evaluate p(x)", "substitute, do not solve"]]),
 ("note", "IMPORTANT", "In a real situation reject a zero that is **not meaningful**: a negative time, a negative length or age. Say why in the answer."),
 ("h2", "2.9 Common Mistakes"),
 ("table", ["Mistake", "Correct idea"], [
  ["Writing sum of zeroes = b/a", "sum = **−b/a**; product = c/a"],
  ["Forming the polynomial as x² + (sum)x + product", "x² − (sum)x + product"],
  ["Saying every quadratic has two zeroes", "it has 0, 1 or 2 real zeroes; x² + 1 has none"],
  ["Calling a polynomial with a negative or fractional power of x a polynomial", "powers of x must be whole numbers, so √x + 2 and 1/x are not polynomials"],
  ["Forgetting the constant k", "x² − 4x + 1 and 3x² − 12x + 3 have the same zeroes; use one extra condition to fix k"],
  ["Using the relations when the polynomial is not in standard form", "write 6x² − 3 − 7x as 6x² − 7x − 3 first: b = −7, c = −3"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["For **word problems** the zeroes of a profit, height or area polynomial are the **break-even, landing or boundary values**; reject meaningless ones.", "Use **S = α + β and P = αβ** to find α² + β², 1/α + 1/β and new polynomials without solving.", "A parabola that **touches** the x-axis has one repeated zero; one that stays above or below has **no real zero**."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
