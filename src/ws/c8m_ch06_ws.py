"""Class 8 Maths Ch 6 - We Distribute, Yet Things Multiply: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch06"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric spot checks of every identity used
for v in range(2, 9):
    assert (3*v+2)*(2*v-5) == 6*v*v-11*v-10 and (v-3)*(v+3)*(v*v+9) == v**4-81 and (v+4)**2-(v-4)**2 == 16*v
    assert (v*v+v+1)*(v-1) == v**3-1 and (2*v-3)*(v+4) == 2*v*v+5*v-12 and (2*v+3)**2 == 4*v*v+12*v+9
    assert (v+7)*(v+2) == v*v+9*v+14 and (v+4)**2-v*v == 8*v+16 and v*(v+1)*(v+2)*(v+3)+1 == (v*v+3*v+1)**2
assert 998**2 == 996004 and 103*97 == 9991 and 97**2-9 == 9400 and 305**2 == 93025 and 63**2-37**2 == 2600 and 47**2-33**2 == 1120
assert 13*7 == 91 and 13+7 == 20 and 15*9 == 135 and 96*45 == 4320 and 12*9 == 108 and 7*105 == 735 and 6*98 == 588 and 75**2 == 5625

WS = [
# ---------------- EASY ----------------
W("Expand $3(x+4)$.", 1, "(a) $3x+12$. Multiply both terms of the bracket by 3. (1)", "E", opts=["$3x+12$", "$3x+4$", "$x+12$", "$3x+7$"]),
W("$(x+3)^2$ is equal to:", 1, "(c) $x^2+6x+9$. $(a+b)^2=a^2+2ab+b^2$ with $a=x$, $b=3$. (1)", "E", opts=["$x^2+9$", "$x^2+3x+9$", "$x^2+6x+9$", "$x^2+6x+6$"]),
W("$(a+b)(a-b)$ is equal to:", 1, "(c) $a^2-b^2$ (difference of two squares). (1)", "E", opts=["$a^2+b^2$", "$a^2-2ab+b^2$", "$a^2-b^2$", "$a^2+2ab+b^2$"]),
W("The value of $102\\times98$ is:", 1, "(c) 9,996. $102\\times98=(100+2)(100-2)=10000-4=9996$. (1)", "E", opts=["9,994", "9,986", "9,996", "10,004"]),
W("$(x+2)(x+5)$ is equal to:", 1, "(b) $x^2+7x+10$. $(x+a)(x+b)=x^2+(a+b)x+ab$ with $a=2$, $b=5$. (1)", "E", opts=["$x^2+10$", "$x^2+7x+10$", "$x^2+7x+7$", "$x^2+3x+10$"]),
W("The value of $19^2$ using $(20-1)^2$ is:", 1, "(a) 361. $400-40+1=361$. (1)", "E", opts=["361", "359", "381", "399"]),
W("Which of these is **not** correct for all values of $a$ and $b$?", 1, "(c) $(a-b)^2=a^2-b^2$ is wrong; the correct identity is $(a-b)^2=a^2-2ab+b^2$. (1)", "E",
  opts=["$(a+b)^2=a^2+2ab+b^2$", "$(a-b)^2=a^2-2ab+b^2$", "$(a-b)^2=a^2-b^2$", "$(a+b)(a-b)=a^2-b^2$"]),
W("Expand $5(2x-3)$.", 2, "$5\\times2x-5\\times3$ (1) $=10x-15$ (1).", "E"),
W("Use the distributive property to find $7\\times105$.", 2, "$7\\times105=7\\times(100+5)$ (1) $=700+35=735$ (1).", "E"),
W("A garden is $(x+5)$ metres long and 3 metres wide. Write its area as an expression in $x$, and find the area when $x=10$.", 2, "Area $=3(x+5)=3x+15$ (1). For $x=10$: $30+15=45$ m² (1).", "E", wp=True),
W("Expand $(2a-3)^2$.", 2, "$(2a)^2-2(2a)(3)+3^2$ (1) $=4a^2-12a+9$ (1).", "E"),
W("Find the cost of 6 packets of biscuits at ₹ 98 each, using $98=100-2$.", 2, "$6\\times(100-2)=600-12$ (1) $=$ ₹ 588 (1).", "E", wp=True),
W("Multiply $(x+1)(x+4)$.", 2, "$x\\cdot x+x\\cdot4+1\\cdot x+1\\cdot4$ (1) $=x^2+5x+4$ (1).", "E"),
W("Simplify $4(x+2)+3(x-1)$.", 2, "$4x+8+3x-3$ (1) $=7x+5$ (1).", "E"),
W("True or false (give a reason): $(x+5)^2=x^2+25$.", 1, "**False.** The middle term $2\\times x\\times5=10x$ is missing; $(x+5)^2=x^2+10x+25$ (1).", "E"),
W("A shopkeeper buys 25 notebooks at ₹ 48 each. Use $48=50-2$ to find the total cost.", 2, "$25\\times(50-2)=1250-50$ (1) $=$ ₹ 1,200 (1).", "E", wp=True),
W("Factorise $x^2-16$.", 1, "$x^2-4^2=(x-4)(x+4)$ (1).", "E"),
# ---------------- MEDIUM ----------------
W("Multiply $(3x+2)(2x-5)$.", 2, "$6x^2-15x+4x-10$ (1) $=6x^2-11x-10$ (1).", "M"),
W("Use an identity to find $998^2$.", 2, "$998^2=(1000-2)^2=1000000-2\\times1000\\times2+4$ (1) $=996004$ (1).", "M"),
W("Find $103\\times97$ without direct multiplication.", 2, "$(100+3)(100-3)=100^2-3^2$ (1) $=10000-9=9991$ (1).", "M"),
W("Evaluate $97^2-3^2$ using an identity.", 2, "$a^2-b^2=(a+b)(a-b)$: $(97+3)(97-3)$ (1) $=100\\times94=9400$ (1).", "M"),
W("A square field has side $(2x+3)$ metres. Write its area as an expression in $x$ and find the area when $x=5$.", 3, "Area $=(2x+3)^2=4x^2+12x+9$ (2). For $x=5$: $100+60+9=169$ m² (1). Check: side $=13$ m, $13^2=169$.", "M", wp=True),
W("A rectangular hall is $(x+7)$ m long and $(x+2)$ m wide. Find its area as an expression in $x$ and its value when $x=8$.", 3, "Area $=(x+7)(x+2)=x^2+9x+14$ (2). For $x=8$: $64+72+14=150$ m² (1). Check: $15\\times10=150$.", "M", wp=True),
W("If $a+b=10$ and $ab=21$, find $a^2+b^2$.", 3, "$(a+b)^2=a^2+2ab+b^2$ (1). $100=a^2+b^2+42$ (1). $a^2+b^2=58$ (1).", "M"),
W("Find the product $(x-3)(x+3)(x^2+9)$.", 3, "$(x-3)(x+3)=x^2-9$ (1). $(x^2-9)(x^2+9)=(x^2)^2-9^2$ (1) $=x^4-81$ (1).", "M"),
W("Reena writes $(x+5)^2=x^2+25$. Find her mistake, give the correct expansion and verify it for $x=1$.", 2, "She left out the middle term $2\\times x\\times5=10x$ (1). Correct: $x^2+10x+25$; for $x=1$: $(1+5)^2=36$ and $1+10+25=36$ ✓ (1).", "M"),
W("A square tile has side 1.02 m. Find its area using $(1+0.02)^2$.", 2, "$1+2(0.02)+0.02^2$ (1) $=1+0.04+0.0004=1.0404$ m² (1).", "M", wp=True),
W("Find $75^2$ using $(70+5)^2$ and check it with the rule for numbers ending in 5.", 2, "$4900+700+25=5625$ (1). Rule: $7\\times8=56$ followed by 25 gives $5625$ ✓ (1).", "M"),
W("Simplify $(x+4)^2-(x-4)^2$.", 3, "$(x^2+8x+16)-(x^2-8x+16)$ (2) $=16x$ (1).", "M"),
W("Bhavna buys $(a+3)$ pens at ₹ $(a-3)$ each. Show that the total cost is ₹ $(a^2-9)$ and find it for $a=12$.", 3, "Cost $=(a+3)(a-3)=a^2-9$ (2). For $a=12$: $144-9=$ ₹ 135 (1). Check: 15 pens at ₹ 9 $=135$.", "M", wp=True),
W("Factorise $x^2+11x+18$.", 2, "Find two numbers with sum 11 and product 18: 2 and 9 (1). $x^2+11x+18=(x+2)(x+9)$ (1).", "M"),
W("Expand $(2x+3y)^2$.", 2, "$(2x)^2+2(2x)(3y)+(3y)^2$ (1) $=4x^2+12xy+9y^2$ (1).", "M"),
W("Find $305^2$ using $(300+5)^2$.", 2, "$300^2+2\\times300\\times5+5^2$ (1) $=90000+3000+25=93025$ (1).", "M"),
W("Evaluate $63^2-37^2$ using $a^2-b^2=(a+b)(a-b)$.", 2, "$(63+37)(63-37)$ (1) $=100\\times26=2600$ (1).", "M"),
W("A rectangular mat measures 23 cm by 17 cm. Write 23 as $20+3$ and 17 as $10+7$ and find the four partial areas of the picture ‘$(20+3)\\times(10+7)$’. Add them to find the area of the mat.", 3, "Areas: $20\\times10=200$, $20\\times7=140$, $3\\times10=30$, $3\\times7=21$ (2). Total $=391$ cm² (1).", "M", wp=True),
W("Simplify $(x+2)(x-2)+4$.", 2, "$(x+2)(x-2)=x^2-4$ (1). $x^2-4+4=x^2$ (1).", "M"),
# ---------------- HARD ----------------
W("If $a+b=7$ and $ab=12$, find $a^2+b^2$ and $(a-b)^2$.", 3, "$a^2+b^2=(a+b)^2-2ab=49-24=25$ (2). $(a-b)^2=a^2+b^2-2ab=25-24=1$ (1).", "H"),
W("If $x+\\dfrac1x=5$, find $x^2+\\dfrac1{x^2}$ and then $x^4+\\dfrac1{x^4}$.", 4, "$\\left(x+\\frac1x\\right)^2=x^2+2+\\frac1{x^2}$ (1), so $x^2+\\frac1{x^2}=25-2=23$ (1). Squaring again: $\\left(x^2+\\frac1{x^2}\\right)^2=x^4+2+\\frac1{x^4}$ (1), so $x^4+\\frac1{x^4}=529-2=527$ (1).", "H"),
W("A square flower bed of side 10 m has a path 2 m wide all round it (outside). (i) Write the area of the path for a bed of side $a$ m and 2 m path. (ii) Find the area for $a=10$ and the cost of paving at ₹ 45 per m².", 4, "(i) Outer square has side $a+4$: path area $=(a+4)^2-a^2$ (1) $=8a+16$ (1). (ii) For $a=10$: $96$ m² (1). Cost $=96\\times45=$ ₹ 4,320 (1).", "H", wp=True),
W("Multiply $(x^2+x+1)(x-1)$ and simplify.", 3, "$x^3+x^2+x-x^2-x-1$ (2) $=x^3-1$ (1).", "H"),
W("Evaluate $(9.9)^2-(0.1)^2$ using an identity.", 3, "$a^2-b^2=(a+b)(a-b)$ (1). $(9.9+0.1)(9.9-0.1)=10\\times9.8$ (1) $=98$ (1).", "H"),
W("The perimeter of a rectangle is 40 cm and its area is 91 cm². Find the length and breadth. (Hint: find $l-b$.)", 4, "$l+b=20$, $lb=91$ (1). $(l-b)^2=(l+b)^2-4lb=400-364=36$ (2). $l-b=6$, so $l=13$ cm and $b=7$ cm (1).", "H", wp=True),
W("Prove that $(a+b)^2-(a-b)^2=4ab$. Use it to find $47^2-33^2$ (take $a+b=47$, $a-b=33$).", 4, "LHS $=(a^2+2ab+b^2)-(a^2-2ab+b^2)=4ab$ (2). From $a+b=47$ and $a-b=33$: $a=40$, $b=7$ (1). $47^2-33^2=4\\times40\\times7=1120$ (1).", "H"),
W("A student multiplies $(2x-3)(x+4)$ as $2x^2-12$ (first terms and last terms only). Find the mistake, give the correct product and check it for $x=2$.", 3, "Every term of the first bracket must multiply every term of the second (1). $(2x-3)(x+4)=2x^2+8x-3x-12=2x^2+5x-12$ (1). For $x=2$: $1\\times6=6$ and $8+10-12=6$ ✓ (1).", "H"),
W("Factorise (i) $4a^2-12a+9$ (ii) $x^2-7x+12$.", 3, "(i) $4a^2-12a+9=(2a)^2-2(2a)(3)+3^2=(2a-3)^2$ (1.5). (ii) two numbers with sum $-7$ and product 12 are $-3$ and $-4$: $(x-3)(x-4)$ (1.5).", "H"),
W("**Case study.** A square of side $(a+b)$ is divided into four parts: a square of side $a$, a square of side $b$ and two rectangles $a\\times b$. Take $a=6$ and $b=4$. (i) Find the areas of the four parts. (ii) Add them and compare with $(a+b)^2$. (iii) Which identity does this picture show?", 4, "(i) $36$, $16$, $24$, $24$ (1.5). (ii) Sum $=100=10^2=(a+b)^2$ (1.5). (iii) $(a+b)^2=a^2+2ab+b^2$ (1).", "H", wp=True),
W("Show that the product of four consecutive natural numbers plus 1 is a perfect square. Verify for $1\\times2\\times3\\times4+1$ and prove it in general.", 5, "$1\\times2\\times3\\times4+1=25=5^2$ (1). Let the numbers be $n,n+1,n+2,n+3$: $n(n+3)=n^2+3n=m$ and $(n+1)(n+2)=m+2$ (2). Product $+1=m(m+2)+1=m^2+2m+1=(m+1)^2=(n^2+3n+1)^2$, a perfect square (2).", "H"),
W("The difference of two numbers is 3 and the difference of their squares is 63. Find the numbers.", 4, "$a^2-b^2=(a+b)(a-b)=63$ (1). With $a-b=3$: $a+b=21$ (1). Adding: $2a=24$, $a=12$ (1); $b=9$ (1). Check: $144-81=63$.", "H", wp=True),
W("Evaluate $(7.3)^2-(2.7)^2$ using an identity.", 3, "$(7.3+2.7)(7.3-2.7)$ (1) $=10\\times4.6$ (1) $=46$ (1).", "H"),
W("If $(x+a)(x+b)=x^2+10x+21$, find $a$, $b$ and the value of $(a-b)^2$.", 3, "$a+b=10$ and $ab=21$ (1), so $a,b=3,7$ (1). $(a-b)^2=(7-3)^2=16$ (check: $100-4\\times21=16$) (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(6)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "6.5 More on Identities"),
 ("table", ["Result", "How it comes", "Use"], [
  ["(a + b)² − (a − b)² = 4ab", "subtract identity II from identity I", "47² − 33² = 4 × 40 × 7 = 1120"],
  ["(a + b)² + (a − b)² = 2(a² + b²)", "add identity I and II", "if a + b = 10 and a − b = 2: sum of squares = 52"],
  ["a² + b² = (a + b)² − 2ab", "rearrange identity I", "a + b = 10, ab = 21 gives a² + b² = 58"],
  ["(a − b)² = (a + b)² − 4ab", "combine the above", "l + b = 20, lb = 91 gives (l − b)² = 36, l − b = 6"],
  ["x² + 1/x² = (x + 1/x)² − 2", "square x + 1/x", "x + 1/x = 5 gives 23; then x⁴ + 1/x⁴ = 23² − 2 = 527"],
  ["(x + a)(x + b) = x² + (a + b)x + ab", "identity IV", "if the product is x² + 10x + 21, then a + b = 10, ab = 21: a, b = 3, 7"]]),
 ("h2", "6.6 Worked Examples"),
 ("h3", "Example 1 — Expanding with two terms in each bracket"),
 ("steps", [("Multiply (3x + 2)(2x − 5)", "3x × 2x = 6x²; 3x × (−5) = −15x; 2 × 2x = 4x; 2 × (−5) = −10."), ("Collect like terms", "6x² − 15x + 4x − 10 = 6x² − 11x − 10."), ("Check with x = 1", "5 × (−3) = −15 and 6 − 11 − 10 = −15 ✓.")]),
 ("h3", "Example 2 — Area expression for a field"),
 ("steps", [("Square field of side (2x + 3) m", "Area = (2x + 3)²."), ("Use identity I", "(2x)² + 2 × 2x × 3 + 3² = 4x² + 12x + 9."), ("When x = 5", "100 + 60 + 9 = 169 m², which equals 13² for side 13 m.")]),
 ("h3", "Example 3 — Area of a path"),
 ("steps", [("Square bed of side a with a path 2 m wide all round", "Outer square has side a + 4."), ("Path area", "(a + 4)² − a² = a² + 8a + 16 − a² = 8a + 16."), ("For a = 10 and cost ₹45 per m²", "Area 96 m²; cost 96 × 45 = ₹4,320.")]),
 ("h3", "Example 4 — Finding two numbers from the sum and the product"),
 ("steps", [("Perimeter 40 cm, area 91 cm²", "l + b = 20 and lb = 91."), ("Use the identity", "(l − b)² = (l + b)² − 4lb = 400 − 364 = 36, so l − b = 6."), ("Solve", "l = 13 cm, b = 7 cm (check 13 × 7 = 91).")]),
 ("h3", "Example 5 — Quick arithmetic"),
 ("steps", [("Find 998²", "(1000 − 2)² = 1,000,000 − 4,000 + 4."), ("Find 103 × 97", "(100 + 3)(100 − 3) = 10,000 − 9 = 9,991."), ("Find 7.3² − 2.7²", "(7.3 + 2.7)(7.3 − 2.7) = 10 × 4.6 = 46.")]),
 ("h3", "Example 6 — A neat proof"),
 ("steps", [("Product of 4 consecutive numbers + 1", "Take n(n + 3) = n² + 3n = m; then (n + 1)(n + 2) = m + 2."), ("Combine", "m(m + 2) + 1 = m² + 2m + 1 = (m + 1)²."), ("Conclusion", "It is the square of n² + 3n + 1, e.g. 1 × 2 × 3 × 4 + 1 = 25 = 5².")]),
 ("h2", "6.7 Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["area of a rectangle with algebraic sides", "(length) × (breadth), expand", "(x + 7)(x + 2) = x² + 9x + 14"],
  ["area of a square with side an expression", "(side)² by identity I or II", "(2x + 3)² = 4x² + 12x + 9"],
  ["a path all round a square of side a, width w", "(a + 2w)² − a²", "w = 2: 8a + 16"],
  ["‘n items at ₹ price each’ with both given as expressions", "multiply the brackets", "(a + 3)(a − 3) = a² − 9"],
  ["‘difference of two numbers and of their squares’", "a² − b² = (a + b)(a − b)", "a − b = 3 and a² − b² = 63 give a + b = 21"],
  ["‘perimeter and area of a rectangle given’", "l + b and lb, then (l − b)² = (l + b)² − 4lb", "l = 13, b = 7"]]),
 ("h2", "6.8 Common Mistakes (More)"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["(2x − 3)(x + 4) = 2x² − 12", "only first and last terms were multiplied", "2x² + 5x − 12"],
  ["(x − 3)² = x² − 9", "middle term missing", "x² − 6x + 9"],
  ["(a + b)(a − b) = a² + b²", "the cross terms cancel but b² keeps its minus sign", "a² − b²"],
  ["−2(x − 3) = −2x − 6", "the sign of the second term must also change", "−2x + 6"],
  ["99² = 99 × 2 = 198", "squaring is not doubling", "(100 − 1)² = 9,801"],
  ["(3x)² = 3x²", "the coefficient is also squared", "9x²"]]),
 ]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Useful forms:** a² + b² = (a + b)² − 2ab and (a − b)² = (a + b)² − 4ab; they solve ‘sum and product’ word problems.", "**Area expressions:** area of a path round a square of side a and width w is (a + 2w)² − a² = 4aw + 4w²."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
