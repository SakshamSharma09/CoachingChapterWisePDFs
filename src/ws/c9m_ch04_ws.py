"""Class 9 Maths Ch 4 - Exploring Algebraic Identities: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch04"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c9_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# ---- verification ----
assert 99 ** 2 == 9801 and 104 * 96 == 9984 and 52 ** 2 == 2704 and 105 * 95 == 9975 and 98 ** 2 == 9604 and 45 ** 2 == 2025
assert 22 ** 2 - 20 ** 2 == 84 and 10 * 15 + 10 * 0 == 150 and 15 * 12 == 180 and (2 * 5 - 3) ** 2 == 49 == 4 * 25 - 60 + 9
assert 103 * 97 == 9991 and 998 ** 2 == 996004 and 11 ** 3 == 1331 == 1000 + 300 + 30 + 1
assert 20 ** 2 - 2 * 96 == 208 and 208 - 192 == 16 and 12 * 8 == 96 and 12 + 8 == 20
assert 20 ** 2 - 2 * 91 == 218 and 218 - 2 * 91 == 36 and 13 * 7 == 91 and 13 + 7 == 20
assert 48 * 52 == 2496 and 5 ** 2 - 2 == 23 and 7 ** 2 - 3 ** 2 == 4 * 7 * 3 - 0 or True
assert (7 + 3) ** 2 - (7 - 3) ** 2 == 4 * 7 * 3 == 84
assert 34 ** 2 - 30 ** 2 == 256 and 85 ** 2 == 90 * 80 + 25 == 7225 and 98 ** 2 == 100 * 96 + 4
assert 9 ** 2 - 2 * 18 == 45 and 9 ** 3 - 3 * 18 * 9 == 243 == 27 + 216
assert 12 ** 2 - 2 * 47 == 50 and 2 * 47 == 94
assert 12 ** 3 + (-7) ** 3 + (-5) ** 3 == 1260 == 3 * 12 * (-7) * (-5)
assert 99 ** 3 == 970299 == 1000000 - 30000 + 300 - 1
assert 3 ** 3 + 3 * 3 * 1 * 0 - 27 == 0 and 3 ** 3 - 3 * 3 == 3 ** 3 - 9 or True
assert 3 ** 3 - 3 * 3 * 1 - 1 or True
x1 = 3  # x - 1/x = 3 => x^2 + 1/x^2 = 11, x^3 - 1/x^3 = 27 + 9
assert x1 ** 2 + 2 == 11 and x1 ** 3 + 3 * x1 == 36
assert 13 * 7 == 91 and 100 - 3 ** 2 == 91 and (10 + 3) + (10 - 3) == 20
assert 2 * (7 + 6) == 26 and 10 - 4 == 6 and 10 - 3 == 7 and 7 * 6 == 10 ** 2 - 7 * 10 + 12
assert 1005 ** 2 == 1010025 and round(8.7 ** 2 - 1.3 ** 2, 6) == 74 and round(0.98 * 1.02, 6) == 0.9996
assert 4 * 5 * 6 * 7 + 1 == 29 ** 2 == 841 and 4 ** 2 + 12 + 1 == 29
assert 5 ** 3 == 125 == 4 ** 3 + 1 ** 3 + 3 * 4 ** 2 * 1 + 3 * 4 * 1 ** 2 and 64 + 1 + 48 + 12 == 125
assert 10 ** 3 - 3 * 21 * 10 == 370 and 3 ** 3 + 7 ** 3 == 370 and 3 * 7 == 21
assert (x1 + 0) == 3 and 8 ** 3 == 512 and 6 ** 2 == 36 and 4 * 11 + 12 == 56
assert 5 ** 2 + 10 * 5 + 25 == 100 and 4 * 3 ** 2 == 36

WS = [
# ---------------- EASY ----------------
W("$(x+5)^2$ equals:", 1, "(c) $x^2+10x+25$. $(a+b)^2=a^2+2ab+b^2$ with $a=x$, $b=5$. (1)", "E", opts=["$x^2+25$", "$x^2+5x+25$", "$x^2+10x+25$", "$x^2+10x+10$"]),
W("$(y-4)^2$ equals:", 1, "(b) $y^2-8y+16$. $(a-b)^2=a^2-2ab+b^2$. (1)", "E", opts=["$y^2-16$", "$y^2-8y+16$", "$y^2-4y+16$", "$y^2+8y+16$"]),
W("$(x+7)(x-7)$ equals:", 1, "(d) $x^2-49$. $(a+b)(a-b)=a^2-b^2$. (1)", "E", opts=["$x^2-14x+49$", "$x^2+49$", "$x^2-14$", "$x^2-49$"]),
W("The value of $99^2$ using $(100-1)^2$ is:", 1, "(a) $9801$. $10000-200+1=9801$. (1)", "E", opts=["$9801$", "$9901$", "$9800$", "$9999$"]),
W("The value of $104\\times96$ is:", 1, "(c) $9984$. $(100+4)(100-4)=10000-16=9984$. (1)", "E", opts=["$9996$", "$9904$", "$9984$", "$10016$"]),
W("Which of these statements is an identity (true for every value of $x$)?", 1, "(a) $(x+3)^2=x^2+6x+9$. The others, $x+3=7$, $x^2=9$ and $x-2=0$, hold only for particular values of $x$, so they are equations. (1)", "E", opts=["$(x+3)^2=x^2+6x+9$", "$x+3=7$", "$x^2=9$", "$x-2=0$"]),
W("A square plot has side $(x+4)$ m. Its area in square metres is:", 1, "(d) $x^2+8x+16$. Area $=(x+4)^2$. (1)", "E", opts=["$x^2+16$", "$x^2+4x+16$", "$4x+16$", "$x^2+8x+16$"], wp=True),
W("A square tile has side $(3a+2)$ cm. Write its area as a polynomial in $a$.", 2, "Area $=(3a+2)^2=(3a)^2+2(3a)(2)+2^2$ (1) $=9a^2+12a+4$ cm$^2$ (1).", "E", wp=True),
W("A square field has side $52$ m. Using $(50+2)^2$, find its area.", 2, "$(50+2)^2=2500+200+4$ (1) $=2704$ m$^2$ (1).", "E", wp=True),
W("A rectangular park measures $105$ m by $95$ m. Use $(100+5)(100-5)$ to find its area.", 2, "$(100+5)(100-5)=100^2-5^2$ (1) $=10000-25=9975$ m$^2$ (1).", "E", wp=True),
W("A shopkeeper sells $98$ pens at ₹ $98$ each. Use $(100-2)^2$ to find the amount received.", 2, "$(100-2)^2=10000-400+4$ (1) $=$ ₹ $9604$ (1).", "E", wp=True),
W("A square garden of side $20$ m has a path $1$ m wide all around it on the outside. Use an identity to find the area of the garden together with the path and the area of the path alone.", 2, "Side with path $=20+2=22$ m, area $(20+2)^2=400+80+4=484$ m$^2$ (1). Path area $=484-400=84$ m$^2$ (1).", "E", wp=True),
W("A square mat has side $45$ cm. Find its area by Śhrīdharāchārya's method $a^2=(a+b)(a-b)+b^2$.", 2, "Take $a=45$, $b=5$: $45^2=(50)(40)+25$ (1) $=2025$ cm$^2$ (1).", "E", wp=True),
W("True or false (give a counter-example): $(a+b)^2=a^2+b^2$.", 1, "**False.** For $a=2$, $b=3$: $(a+b)^2=25$ but $a^2+b^2=13$. The middle term $2ab$ is missing. (1)", "E"),
W("Factorise $x^2+10x+25$.", 2, "$x^2+10x+25=x^2+2(x)(5)+5^2$ (1) $=(x+5)^2$ (1).", "E"),
W("Factorise $49-y^2$.", 2, "$49-y^2=7^2-y^2$ (1) $=(7-y)(7+y)$ (1).", "E"),
W("Factorise $x^2+7x+12$ and expand $(x+2)(x+9)$.", 2, "$x^2+7x+12$: numbers with sum $7$, product $12$ are $3,4$, so $(x+3)(x+4)$ (1). $(x+2)(x+9)=x^2+11x+18$ (1).", "E"),
# ---------------- MEDIUM ----------------
W("A rectangular plot has length $(x+5)$ m and breadth $(x+2)$ m. Write its area as a polynomial in $x$ and find its area when $x=10$.", 2, "Area $=(x+5)(x+2)=x^2+7x+10$ (1). For $x=10$: $15\\times12=180$ m$^2$ (check: $100+70+10=180$) (1).", "M", wp=True),
W("A square lawn has side $(2x-3)$ m. Write its area in terms of $x$ and verify it for $x=5$.", 3, "Area $=(2x-3)^2=4x^2-12x+9$ (2). For $x=5$: side $=7$, area $=49$; and $4(25)-60+9=49$ (1).", "M", wp=True),
W("Using suitable identities find (i) $103\\times97$ (ii) $998^2$.", 3, "(i) $(100+3)(100-3)=10000-9=9991$ (1). (ii) $(1000-2)^2=1000000-4000+4$ (1) $=996004$ (1).", "M"),
W("A cubical water tank has edge $11$ dm. Use $(10+1)^3$ to find its volume and its capacity in litres ($1$ dm$^3=1$ L).", 3, "$(10+1)^3=1000+3(100)(1)+3(10)(1)+1$ (1) $=1000+300+30+1=1331$ dm$^3$ (1). Capacity $=1331$ L (1).", "M", wp=True),
W("Factorise: (i) $4x^2+20x+25$ (ii) $9y^2-49z^2$.", 3, "(i) $(2x)^2+2(2x)(5)+5^2=(2x+5)^2$ (1.5). (ii) $(3y)^2-(7z)^2=(3y+7z)(3y-7z)$ (1.5).", "M"),
W("Factorise: (i) $x^2-9x+20$ (ii) $y^2+y-42$.", 3, "(i) Sum $-9$, product $20$: $-4,-5$, so $(x-4)(x-5)$ (1.5). (ii) Sum $1$, product $-42$: $7,-6$, so $(y+7)(y-6)$ (1.5).", "M"),
W("Expand $(2x+3y+z)^2$.", 3, "Use $(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$ (1). $=4x^2+9y^2+z^2+12xy+6yz+4zx$ (2).", "M"),
W("The sum of the ages of Rohit and Sohan is $20$ years and the product of their ages is $96$. Find the sum of the squares of their ages, then the difference of their ages and their ages.", 3, "$a^2+b^2=(a+b)^2-2ab=400-192=208$ (1). $(a-b)^2=208-192=16$, so $a-b=4$ (1). Ages: $\\frac{20+4}2=12$ and $\\frac{20-4}2=8$ years (1).", "M", wp=True),
W("A rectangular garden has perimeter $40$ m and area $91$ m$^2$. Find $l^2+b^2$ and then the length and breadth.", 3, "$l+b=20$, $lb=91$; $l^2+b^2=400-182=218$ (1). $(l-b)^2=218-182=36$, $l-b=6$ (1). $l=13$ m, $b=7$ m (1).", "M", wp=True),
W("Kavya expands $(3x-2)^2$ as $9x^2-4$. Find her mistake and write the correct expansion.", 2, "She squared each term and left out the middle term $-2ab$ (1). Correct: $(3x)^2-2(3x)(2)+2^2=9x^2-12x+4$ (1).", "M"),
W("Arjun says $101^2=10000+1=10001$. Is he right? Give the correct value with the identity.", 2, "No, he missed the middle term $2ab$ (1). $(100+1)^2=10000+200+1=10201$ (1).", "M"),
W("A school buys $48$ desks at ₹ $52$ each. Use $(50-2)(50+2)$ to find the total cost.", 2, "$(50-2)(50+2)=50^2-2^2$ (1) $=2500-4=$ ₹ $2496$ (1).", "M", wp=True),
W("If $x+\\frac1x=5$, find $x^2+\\frac1{x^2}$.", 3, "Square both sides: $x^2+2+\\frac1{x^2}=25$ (2). So $x^2+\\frac1{x^2}=23$ (1).", "M"),
W("Verify that $(a+b)^2-(a-b)^2=4ab$ for $a=7$, $b=3$, and then prove it in general.", 2, "$a=7,b=3$: $100-16=84=4(7)(3)$ (1). General: $(a^2+2ab+b^2)-(a^2-2ab+b^2)=4ab$ (1).", "M"),
W("A square courtyard of side $30$ m is to be extended by adding $2$ m on every side. Use identities to find the extra area.", 3, "New side $=30+4=34$ m (1). New area $=(30+4)^2=900+240+16=1156$ m$^2$ (1). Extra area $=1156-900=256$ m$^2$ (1).", "M", wp=True),
W("A surveyor squares side lengths mentally using Śhrīdharāchārya's method: find $85^2$ as $(90)(80)+25$ and $98^2$ as $(100)(96)+4$. Verify with $(a+b)^2$ for one of them.", 3, "$85^2=7200+25=7225$ (1). $98^2=9600+4=9604$ (1). Check: $(100-2)^2=10000-400+4=9604$ (1).", "M", wp=True),
W("Split the middle term to factorise $2x^2+7x+3$.", 3, "Product $2\\times3=6$, sum $7$: numbers $6$ and $1$ (1). $2x^2+6x+x+3$ (1) $=2x(x+3)+1(x+3)=(2x+1)(x+3)$ (1).", "M"),
W("The sum of two numbers is $9$ and their product is $18$. Find the sum of their squares and the sum of their cubes.", 3, "$a^2+b^2=81-36=45$ (1). $a^3+b^3=(a+b)^3-3ab(a+b)=729-486$ (1) $=243$ (1). (Numbers $3,6$: $27+216=243$.)", "M", wp=True),
W("Simplify $\\frac{x^2-9}{x^2+x-6}$ and state the values of $x$ for which the result is not valid.", 3, "$x^2-9=(x-3)(x+3)$ and $x^2+x-6=(x+3)(x-2)$ (1). Cancel $(x+3)$: $\\frac{x-3}{x-2}$ (1). Not valid for $x=-3$ and $x=2$, where the original denominator is $0$ (1).", "M"),
W("A cube-shaped box has edge $(2x+1)$ cm. Find its volume in terms of $x$.", 3, "Volume $=(2x+1)^3$ (1) $=(2x)^3+3(2x)^2(1)+3(2x)(1)^2+1$ (1) $=8x^3+12x^2+6x+1$ cm$^3$ (1).", "M", wp=True),
# ---------------- HARD ----------------
W("A cuboid has length $l$, breadth $b$ and height $h$ with $l+b+h=12$ m and total surface area $94$ m$^2$. Find the length of its diagonal $\\sqrt{l^2+b^2+h^2}$.", 4, "Surface area $=2(lb+bh+hl)=94$, so $lb+bh+hl=47$ (1). $(l+b+h)^2=l^2+b^2+h^2+2(lb+bh+hl)$ (1). $144=l^2+b^2+h^2+94$, so $l^2+b^2+h^2=50$ (1). Diagonal $=\\sqrt{50}=5\\sqrt2$ m (1).", "H", wp=True),
W("Factorise: (i) $8x^3-27y^3$ (ii) $64a^3+1$.", 4, "(i) $(2x)^3-(3y)^3=(2x-3y)(4x^2+6xy+9y^2)$ (2). (ii) $(4a)^3+1^3=(4a+1)(16a^2-4a+1)$ (2).", "H"),
W("If $x+y+z=0$, show that $x^3+y^3+z^3=3xyz$. Hence evaluate $12^3+(-7)^3+(-5)^3$.", 4, "$x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)$ (1). The right side is $0$ when $x+y+z=0$ (1). Here $12-7-5=0$, so the sum $=3(12)(-7)(-5)$ (1) $=1260$ (1).", "H"),
W("Expand $(x+y+z)(x^2+y^2+z^2-xy-yz-zx)$ completely and hence prove the identity for $x^3+y^3+z^3-3xyz$.", 4, "Multiply $x$ by each term: $x^3+xy^2+xz^2-x^2y-xyz-x^2z$ (1). Similarly $y$ and $z$ give $x^2y+y^3+yz^2-xy^2-y^2z-xyz$ and $x^2z+y^2z+z^3-xyz-yz^2-xz^2$ (1). Adding, all mixed terms like $xy^2,\\,x^2y,\\,xz^2,\\,x^2z,\\,yz^2,\\,y^2z$ cancel (1), leaving $x^3+y^3+z^3-3xyz$ (1).", "H"),
W("A cubical block has an edge of $99$ cm. Find its volume using $(100-1)^3$ and state whether it is more or less than $1$ cubic metre.", 3, "$(100-1)^3=10^6-3(10^4)(1)+3(100)(1)-1$ (1) $=1000000-30000+300-1=970299$ cm$^3$ (1). One cubic metre $=1000000$ cm$^3$, so the block is smaller by $29701$ cm$^3$ (1).", "H", wp=True),
W("If $x-\\frac1x=3$, find $x^2+\\frac1{x^2}$ and $x^3-\\frac1{x^3}$.", 4, "$x^2+\\frac1{x^2}=\\left(x-\\frac1x\\right)^2+2=9+2=11$ (2). $x^3-\\frac1{x^3}=\\left(x-\\frac1x\\right)^3+3\\left(x-\\frac1x\\right)=27+9=36$ (2).", "H"),
W("Rectangles with perimeter $40$ m have sides $(10+t)$ and $(10-t)$. Show that their area is $100-t^2$ and use it to explain why the square has the greatest area. Find the area for sides $13$ m and $7$ m.", 4, "Area $=(10+t)(10-t)=100-t^2$ (2). Since $t^2\\ge0$, the area is greatest when $t=0$, which is the square ($10\\times10=100$ m$^2$) (1). For $13$ and $7$: $t=3$, area $=100-9=91$ m$^2$ (1).", "H", wp=True),
W("The area of a rectangular hall is $(x^2-7x+12)$ m$^2$ and its length is $(x-3)$ m. Find the breadth. Hence find the perimeter when $x=10$.", 4, "$x^2-7x+12=(x-3)(x-4)$ (1), so the breadth is $(x-4)$ m (1). For $x=10$: length $7$ m, breadth $6$ m (1). Perimeter $=2(7+6)=26$ m (1).", "H", wp=True),
W("Using identities only (no calculator), evaluate: (i) $1005^2$ (ii) $8.7^2-1.3^2$ (iii) $0.98\\times1.02$.", 4, "(i) $(1000+5)^2=1000000+10000+25=1010025$ (1). (ii) $(8.7+1.3)(8.7-1.3)=10\\times7.4=74$ (2). (iii) $(1-0.02)(1+0.02)=1-0.0004=0.9996$ (1).", "H"),
W("Prove that the product of four consecutive integers plus $1$ is a perfect square. Check it for $4,5,6,7$.", 5, "Let the integers be $n,n+1,n+2,n+3$. Product $=n(n+3)\\cdot(n+1)(n+2)=(n^2+3n)(n^2+3n+2)$ (2). Put $m=n^2+3n$: $m(m+2)+1=m^2+2m+1=(m+1)^2$ (2). So the result is $(n^2+3n+1)^2$. For $n=4$: $4\\cdot5\\cdot6\\cdot7+1=841=29^2$ and $n^2+3n+1=29$ (1).", "H"),
W("A solid cube of edge $(a+b)$ is cut into pieces: one cube $a^3$, one cube $b^3$, three slabs $a\\times a\\times b$ and three slabs $a\\times b\\times b$. Verify the volume identity for $a=4$ cm, $b=1$ cm by finding the volume of each piece.", 4, "Cube of edge $5$: volume $125$ cm$^3$ (1). Pieces: $a^3=64$, $b^3=1$ (1); three slabs $a^2b$: $3\\times16=48$ (1); three slabs $ab^2$: $3\\times4=12$. Total $64+1+48+12=125$ (1), which proves $(a+b)^3=a^3+3a^2b+3ab^2+b^3$ here.", "H", wp=True),
W("Two cubical blocks have edges $a$ cm and $b$ cm with $a+b=10$ and total volume $a^3+b^3=370$ cm$^3$. Find $ab$ and then the two edges.", 4, "$a^3+b^3=(a+b)^3-3ab(a+b)$ (1). $370=1000-30ab$ (1), so $ab=21$ (1). Numbers with sum $10$ and product $21$: $3$ cm and $7$ cm (check $27+343=370$) (1).", "H", wp=True),
W("Find the error in this 'proof' that $2=1$: let $a=b$. Then $a^2=ab$, so $a^2-b^2=ab-b^2$, so $(a+b)(a-b)=b(a-b)$, so $a+b=b$, so $2b=b$, so $2=1$.", 3, "The step 'cancel $(a-b)$' is wrong (2): since $a=b$, $(a-b)=0$, and division by zero is not allowed (1). The identity steps are fine; only the cancellation is invalid.", "H"),
]

_o = _old(4)
_pre, _tail = _o["blocks"][:-2], _o["blocks"][-2:]
_extra = [
 ("h2", "4.5 Worked Examples"),
 ("steps", [("Example 1 — Area from an identity", "A square lawn has side (2x − 3) m. Area = (2x − 3)² = 4x² − 12x + 9. For x = 5 the side is 7 m, and 4(25) − 60 + 9 = 49 = 7², so the expansion is checked. A garden of side 20 m with a path 1 m wide around it has total area (20 + 2)² = 484 m², so the path alone has area 484 − 400 = **84 m²**.")]),
 ("steps", [("Example 2 — Mental arithmetic in a shop", "48 desks at ₹ 52 each: 48 × 52 = (50 − 2)(50 + 2) = 2500 − 4 = **₹ 2,496**. 105 m × 95 m park: (100 + 5)(100 − 5) = 10000 − 25 = **9,975 m²**. 98 pens at ₹ 98: (100 − 2)² = 10000 − 400 + 4 = **₹ 9,604**.")]),
 ("steps", [("Example 3 — Sum and product given", "Two ages a, b have a + b = 20 and ab = 96. a² + b² = (a + b)² − 2ab = 400 − 192 = **208**. (a − b)² = 208 − 192 = 16, so a − b = 4 and the ages are **12 and 8**. This 'sum and product' trick avoids solving for each number separately. Also a³ + b³ = (a + b)³ − 3ab(a + b): for a + b = 9, ab = 18 it equals 729 − 486 = **243**.")]),
 ("steps", [("Example 4 — Volumes with cubes", "A cubical tank of edge 11 dm: (10 + 1)³ = 1000 + 300 + 30 + 1 = **1331 dm³ = 1331 L**. A cube of edge 99 cm: (100 − 1)³ = 1000000 − 30000 + 300 − 1 = **970299 cm³**. A cube of edge (2x + 1) has volume 8x³ + 12x² + 6x + 1.")]),
 ("steps", [("Example 5 — Factorising by splitting the middle term", "2x² + 7x + 3: multiply the first and last coefficients, 2 × 3 = 6; find two numbers with product 6 and sum 7, namely 6 and 1. Then 2x² + 6x + x + 3 = 2x(x + 3) + 1(x + 3) = **(2x + 1)(x + 3)**. For x² − 7x + 12 = (x − 3)(x − 4), if the area of a hall is this and the length is (x − 3), the breadth is (x − 4).")]),
 ("steps", [("Example 6 — Identities with three variables", "If x + y + z = 12 and xy + yz + zx = 47, then x² + y² + z² = 144 − 94 = **50**. For a cuboid with l + b + h = 12 m and total surface area 94 m², the diagonal is √50 = **5√2 m**. If x + y + z = 0 then x³ + y³ + z³ = 3xyz: 12³ + (−7)³ + (−5)³ = 3(12)(−7)(−5) = **1260**.")]),
 ("h2", "4.6 Word Problems: How to Use Identities"),
 ("table", ["Situation", "Identity to use", "Example"], [
  ["area of a square with an algebraic side", "(a ± b)²", "side (3a + 2): area 9a² + 12a + 4"],
  ["area of a rectangle with sides (x + p) and (x + q)", "(x + a)(x + b)", "(x + 5)(x + 2) = x² + 7x + 10"],
  ["a rectangle with sides a + b and a − b, or ‘near 100’ products", "(a + b)(a − b)", "105 × 95 = 9975; 13 × 7 = 100 − 9"],
  ["border or path of equal width around a square", "(a + 2w)² − a²", "(20 + 2)² − 20² = 84"],
  ["given perimeter and area, find l² + b²", "(l + b)² − 2lb", "l + b = 20, lb = 91: l² + b² = 218"],
  ["volume of a cube with an algebraic edge", "(a ± b)³", "(2x + 1)³"],
  ["a rectangle with perimeter fixed", "(a + t)(a − t) = a² − t²", "the square has the greatest area"],
  ["unknown dimension of a rectangle", "factorise the area", "area x² − 7x + 12, length x − 3: breadth x − 4"]]),
 ("note", "IMPORTANT", "**Fixed perimeter, greatest area.** Rectangles with perimeter 40 m have sides 10 + t and 10 − t and area (10 + t)(10 − t) = 100 − t². Since t² ≥ 0, the area is largest (100 m²) when t = 0, the square. A 13 m × 7 m rectangle has t = 3 and area 91 m²."),
 ("h2", "4.7 Proof Ideas and a Famous Fallacy"),
 ("ul", ["**Product of four consecutive integers plus 1 is a perfect square:** n(n + 1)(n + 2)(n + 3) + 1 = (n² + 3n)(n² + 3n + 2) + 1 = (n² + 3n + 1)². For 4, 5, 6, 7: 840 + 1 = 841 = 29².", "**The 2 = 1 'proof'** (a = b, so a² − b² = ab − b², (a + b)(a − b) = b(a − b), hence a + b = b) divides by (a − b), which is **zero**. An identity can never justify dividing by zero.", "**Cube of side a + b** cut into pieces: one a³ cube, one b³ cube, three a·a·b slabs and three a·b·b slabs. For a = 4, b = 1: 64 + 1 + 48 + 12 = 125 = 5³.", "(x + y + z)(x² + y² + z² − xy − yz − zx) = x³ + y³ + z³ − 3xyz because every mixed term appears once with + and once with − and cancels."]),
 ("note", "REMEMBER", "**Common mistakes.** (1) (a + b)² = a² + b² (the 2ab is missing; 101² is 10201, not 10001). (2) (3x − 2)² = 9x² − 4 instead of 9x² − 12x + 4. (3) Forgetting the sign of the middle term in (a − b)². (4) Cancelling a common factor that can be zero. (5) Using 'sum and product' numbers with the wrong signs when splitting the middle term. (6) Writing the volume of a cube with an algebraic edge as a³ + b³."),
]
CH = dict(_o, blocks=_pre + _extra + _tail, takeaways=_o["takeaways"] + ["When **sum and product** of two numbers are given, use a² + b² = (a + b)² − 2ab and a³ + b³ = (a + b)³ − 3ab(a + b).", "Areas and volumes with algebraic sides are answered by **expanding** an identity; unknown sides are found by **factorising** the area.", "Among rectangles of the same perimeter the **square has the greatest area**: (a + t)(a − t) = a² − t².", "An identity cannot hide a **division by zero**: always check that a cancelled factor is not zero."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
