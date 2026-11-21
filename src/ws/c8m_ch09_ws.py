"""Class 8 Maths Ch 9 - The Baudhayana-Pythagoras Theorem: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
from math import isqrt
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch09"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths2" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def tri(a, b, c): assert a*a + b*b == c*c, (a, b, c)
for t in [(6,8,10),(5,12,13),(9,12,15),(7,24,25),(21,28,35),(24,32,40),(10,24,26),(12,5,13),(8,15,17),(20,21,29),(40,30,50),(9,40,41),(16,30,34),(20,48,52),(11,60,61),(12,16,20),(15,20,25),(5,12,13),(300,400,500),(30,40,50),(12,35,37),(8,15,17),(15,8,17),(15,36,39),(7,24,25),(2*4,4*4-1,4*4+1)]:
    tri(*t)
assert 17**2-15**2 == 8**2 and 17**2-8**2 == 15**2 and 13**2-5**2 == 12**2 and 13**2-12**2 == 5**2 and 5+12 == 17
assert 12**2 + 16**2 == 20**2 and 144 + 256 == 400 and 32-12 == 20
assert 6*29 == 174 and 174*35 == 6090 and 210*40 == 8400 and 150*60 == 9000
assert 25**2-7**2 == 24**2 and 14**2//2 == 98 and 41**2-9**2 == 40**2 and 40*9//2 == 180
assert 1.41**2 < 2 < 1.42**2 and 9*9 - 8*8 == 17 and 6*6*2 == 72 and 8*8 < 72 < 9*9
assert 13**2-5**2 == 144 and 10*24//2 == 120 and 9**2+12**2 == 15**2 and 10**2+24**2 == 26**2
assert 14 - 9 == 5 and 5**2 + 12**2 == 13**2 and 25**2 - 24**2 == 7**2 and 25**2-20**2 == 15**2
assert 7**2+9**2 != 12**2 and 11**2+60**2 != 62**2 and 100/4 == 25 and 25**2-24**2 == 49
assert 24*24 + 24*0 + 49 == 625 and sum(range(1, 48, 2)) == 24**2 and 2*24 - 1 == 47 and 2*25 - 1 == 49
assert 4*4 + 3*3 == 25 and 8*8*2 == 128 and 128//4 == 32 and 4**2 + 4**2 == 32
assert 12**2 + 5**2 == 13**2 and (2*3.75 - 3.75*2 == 0) and 4 + 3.75**2 == 4 + 14.0625 and (3.75 + 0.5)**2 == 18.0625

WS = [
# ---------------- EASY ----------------
W("The legs of a right triangle are 6 cm and 8 cm. Its hypotenuse is:", 1, "(b) 10 cm. $6^2+8^2=36+64=100$, so the hypotenuse is $\\sqrt{100}=10$ cm. (1)", "E", opts=["7 cm", "10 cm", "14 cm", "48 cm"]),
W("The hypotenuse of a right triangle is 13 cm and one leg is 5 cm. The other leg is:", 1, "(b) 12 cm. $13^2-5^2=169-25=144$, so the leg is 12 cm. (1)", "E", opts=["8 cm", "12 cm", "18 cm", "144 cm"]),
W("Which of these sets is a Baudhāyana (Pythagorean) triple?", 1, "(b) $(9,12,15)$. $9^2+12^2=81+144=225=15^2$; the others fail, e.g. $10^2+24^2=676\\ne27^2$. (1)", "E", opts=["$(7,8,9)$", "$(9,12,15)$", "$(10,24,27)$", "$(6,8,11)$"]),
W("A square has side 5 cm. The area of the square drawn on its diagonal is:", 1, "(b) 50 cm². The square on the diagonal has double the area: $2\\times25=50$. (1)", "E", opts=["25 cm²", "50 cm²", "100 cm²", "10 cm²"]),
W("If the side of a square is doubled, its area becomes:", 1, "(c) 4 times. $(2a)^2=4a^2$. (1)", "E", opts=["2 times", "3 times", "4 times", "8 times"]),
W("Which of these triples is **not** primitive (has a common factor greater than 1)?", 1, "(c) $(6,8,10)$, which is $2\\times(3,4,5)$. (1)", "E", opts=["$(3,4,5)$", "$(5,12,13)$", "$(6,8,10)$", "$(8,15,17)$"]),
W("The longest side of a right-angled triangle is the:", 1, "(a) hypotenuse. It is opposite the right angle. (1)", "E", opts=["hypotenuse", "base", "altitude", "median"]),
W("A 10 m ladder leans against a wall with its foot 6 m from the wall. How high up the wall does it reach?", 2, "Height $=\\sqrt{10^2-6^2}$ (1) $=\\sqrt{64}=8$ m (1).", "E", wp=True),
W("A rectangular park is 12 m long and 5 m wide. Rakesh walks along two sides from one corner to the opposite corner; Sonal walks along the diagonal. How much shorter is Sonal's walk?", 2, "Diagonal $=\\sqrt{144+25}=13$ m (1). Rakesh walks $17$ m, so Sonal's path is $4$ m shorter (1).", "E", wp=True),
W("Find the hypotenuse and the perimeter of a right triangle whose legs are 9 cm and 12 cm.", 2, "Hypotenuse $=\\sqrt{81+144}=\\sqrt{225}=15$ cm (1). Perimeter $=9+12+15=36$ cm (1).", "E"),
W("True or false (give a reason): in a right-angled triangle the hypotenuse can be shorter than one of the other sides.", 1, "**False.** The hypotenuse satisfies $c^2=a^2+b^2$, so $c^2>a^2$ and $c^2>b^2$: it is the longest side (1).", "E"),
W("Check whether $(7,24,25)$ is a Baudhāyana triple.", 2, "$7^2+24^2=49+576$ (1) $=625=25^2$, so it is a triple (1).", "E"),
W("Use the scaling rule on $(3,4,5)$ with $k=7$ to get a new triple and verify it.", 2, "$(21,28,35)$ (1). $21^2+28^2=441+784=1225=35^2$ (1).", "E"),
W("A right triangle has two equal sides of 6 cm. Find the square of its hypotenuse and say between which two whole numbers the hypotenuse lies.", 2, "$c^2=36+36=72$ (1). $8^2=64<72<81=9^2$, so $8<c<9$ (1).", "E"),
W("A flagpole 15 m high is held by a wire running from its top to a point on the ground 8 m from its foot. Find the length of the wire.", 2, "Length $=\\sqrt{15^2+8^2}$ (1) $=\\sqrt{289}=17$ m (1).", "E", wp=True),
W("Mohan walks 8 km east and then 15 km north. How far is he in a straight line from his starting point?", 2, "Distance $=\\sqrt{8^2+15^2}$ (1) $=\\sqrt{289}=17$ km (1).", "E", wp=True),
W("A mason checks a corner of a wall with a rope knotted into 12 equal parts, forming a loop with sides of 3, 4 and 5 parts. Explain why this shows a right angle.", 2, "$3^2+4^2=9+16=25=5^2$ (1), and a triangle whose sides satisfy $a^2+b^2=c^2$ has a right angle opposite the longest side (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("A television has a screen with diagonal 40 inch and width 32 inch. Find its height.", 2, "Height $=\\sqrt{40^2-32^2}=\\sqrt{1600-1024}$ (1) $=\\sqrt{576}=24$ inch (1).", "M", wp=True),
W("Show that $\\sqrt2$ lies between $1.41$ and $1.42$.", 2, "$1.41^2=1.9881<2$ (1) and $1.42^2=2.0164>2$ (1), so $1.41<\\sqrt2<1.42$.", "M"),
W("Pooja finds the hypotenuse of a right triangle with legs 5 cm and 12 cm as $5+12=17$ cm. Find her mistake and the correct answer.", 2, "She added the legs; the theorem says add the **squares** (1). $c^2=25+144=169$, so $c=13$ cm (1).", "M"),
W("Using the rule $\\left(n,\\frac{n^2-1}{2},\\frac{n^2+1}{2}\\right)$ for odd $n$, find the triple with smallest member 11 and verify it.", 2, "$\\frac{121-1}{2}=60$, $\\frac{121+1}{2}=61$, so $(11,60,61)$ (1). $121+3600=3721=61^2$ (1).", "M"),
W("The diagonal of a square is 14 cm. Find its area.", 2, "Square on the diagonal has area $14^2=196$ cm² (1). That is double the original square, so area $=98$ cm² (1).", "M"),
W("A right triangle has hypotenuse 41 cm and one leg 9 cm. Find the other leg and the area.", 2, "Other leg $=\\sqrt{1681-81}=\\sqrt{1600}=40$ cm (1). Area $=\\frac12\\times9\\times40=180$ cm² (1).", "M"),
W("A kite is flying at a height of 60 m with its string fully out, 100 m long, held at ground level. How far horizontally is the holder from the point below the kite?", 2, "Distance $=\\sqrt{100^2-60^2}=\\sqrt{6400}=80$ m (2).", "M", wp=True),
W("Find the height and the area of an isosceles triangle with equal sides 13 cm and base 10 cm.", 3, "The height bisects the base, so $h=\\sqrt{13^2-5^2}$ (1) $=12$ cm (1). Area $=\\frac12\\times10\\times12=60$ cm² (1).", "M"),
W("Find the height and area of an equilateral triangle of side 8 cm. Leave $\\sqrt3$ in the answer.", 3, "The height bisects the base: $h^2=64-16=48$ (1), $h=4\\sqrt3$ cm (1). Area $=\\frac12\\times8\\times4\\sqrt3=16\\sqrt3$ cm² (1).", "M"),
W("A rhombus-shaped field has side 13 m and one diagonal 10 m. Find the other diagonal and the area.", 3, "Diagonals bisect at right angles: half-diagonal $=\\sqrt{13^2-5^2}=12$ (1). Other diagonal $=24$ m (1). Area $=\\frac12\\times10\\times24=120$ m² (1).", "M", wp=True),
W("Two poles of height 9 m and 14 m stand 12 m apart on level ground. Find the distance between their tops.", 3, "Difference in heights $=5$ m (1). Distance $=\\sqrt{12^2+5^2}$ (1) $=13$ m (1).", "M", wp=True),
W("The diagonal of a rectangular playground is 17 m and one side is 8 m. Find the other side, the perimeter and the area.", 3, "Other side $=\\sqrt{289-64}=15$ m (1). Perimeter $=2(8+15)=46$ m (1). Area $=120$ m² (1).", "M", wp=True),
W("A ladder 25 m long reaches a window 24 m above the ground. How far is its foot from the wall? If the foot is pulled 8 m further away, how high will it now reach?", 3, "Foot at $\\sqrt{625-576}=7$ m (1). New distance $=15$ m (1). Height $=\\sqrt{625-225}=20$ m (1).", "M", wp=True),
W("Two friends leave school together. Kamal walks east at 30 m per minute and Vimal walks north at 40 m per minute. How far apart are they after 10 minutes?", 3, "Kamal $300$ m, Vimal $400$ m (1). Distance $=\\sqrt{300^2+400^2}$ (1) $=500$ m (1).", "M", wp=True),
W("A bamboo 32 cubits high is broken by the wind so that its top touches the ground 16 cubits from its foot. At what height from the ground was it broken?", 3, "Let the break be at height $x$; the broken part is $32-x$ (1). $x^2+16^2=(32-x)^2$ gives $256=1024-64x$ (1), so $x=12$ cubits (1).", "M", wp=True),
W("Is a triangle with sides 20 cm, 48 cm and 52 cm right-angled? Which angle is the right angle?", 3, "Longest side 52: $52^2=2704$ (1). $20^2+48^2=400+2304=2704$ (1). Yes, right angle opposite the 52 cm side (1).", "M"),
W("The legs of a right triangle are in the ratio $5:12$ and the hypotenuse is 52 cm. Find the legs and the perimeter.", 3, "Legs $5k,12k$: $25k^2+144k^2=52^2$, so $13k=52$, $k=4$ (1). Legs $20$ cm and $48$ cm (1). Perimeter $=20+48+52=120$ cm (1).", "M"),
W("Using the sum of odd numbers, explain why $24^2+7^2=25^2$. (The sum of the first $n$ odd numbers is $n^2$.)", 3, "The first 24 odd numbers add up to $24^2=576$ (1). The 25th odd number is $2\\times25-1=49=7^2$ (1). So $24^2+7^2=576+49=625=25^2$ (1).", "M"),
# ---------------- HARD ----------------
W("A rectangular field is 40 m by 30 m. A path is to be paved along its diagonal at ₹ 150 per metre. Find the cost and the distance saved by walking along the diagonal instead of the two sides.", 3, "Diagonal $=\\sqrt{1600+900}=50$ m (1). Cost $=50\\times150=$ ₹ 7500 (1). Sides give $70$ m, so $20$ m is saved (1).", "H", wp=True),
W("Which of these triangles are right-angled? (i) 9, 40, 41 (ii) 11, 60, 62 (iii) 16, 30, 34. Show the check for each.", 3, "(i) $81+1600=1681=41^2$: yes (1). (ii) $121+3600=3721\\ne62^2=3844$: no (1). (iii) $256+900=1156=34^2$: yes (1).", "H"),
W("Use the theorem to prove that if the diagonal of a square is $d$, its area is $\\frac{d^2}{2}$. Hence find the area of a square with diagonal $12\\sqrt2$ cm.", 3, "Side $a$: $d^2=a^2+a^2=2a^2$ (1), so area $a^2=\\frac{d^2}{2}$ (1). With $d=12\\sqrt2$, area $=\\frac{288}{2}=144$ cm² (1).", "H"),
W("Find the height and area of an isosceles triangle of sides 17 cm, 17 cm and 16 cm. Show your steps.", 3, "Height bisects the base (8 cm each side) (1). $h=\\sqrt{17^2-8^2}=\\sqrt{225}=15$ cm (1). Area $=\\frac12\\times16\\times15=120$ cm² (1).", "H"),
W("The perimeter of a rhombus is 100 cm and one diagonal is 48 cm. Find the other diagonal and the area.", 4, "Side $=25$ cm; half-diagonal $=24$ cm (1). Other half-diagonal $=\\sqrt{625-576}=7$ (2). Other diagonal $=14$ cm (1). Area $=\\frac12\\times48\\times14=336$ cm² (1).", "H"),
W("Prove that $(2m,\\;m^2-1,\\;m^2+1)$ is a Baudhāyana triple for every counting number $m>1$. Write the triple for $m=4$.", 4, "$(2m)^2+(m^2-1)^2=4m^2+m^4-2m^2+1$ (1) $=m^4+2m^2+1=(m^2+1)^2$ (2). For $m=4$: $(8,15,17)$ (1).", "H"),
W("A 17 m ladder rests against a wall with its top 15 m above the ground. Its top slides down 7 m along the wall. How far does the foot of the ladder move?", 4, "Initial foot distance $=\\sqrt{289-225}=8$ m (1). New height $=15-7=8$ m (1). New foot distance $=\\sqrt{289-64}=15$ m (1). The foot moves $15-8=7$ m (1).", "H", wp=True),
W("Complete the Baudhāyana triples: (i) $(8,15,\\;?)$ (ii) $(?,\\;24,25)$ (iii) $(12,35,\\;?)$ (iv) $(9,\\;?,\\;41)$.", 4, "(i) $17$ (1). (ii) $7$ (1). (iii) $37$ (1). (iv) $40$ (1).", "H"),
W("A drone takes off vertically to 30 m and then flies 40 m horizontally. (a) How far is it from the launch point in a straight line? (b) How much shorter is flying straight back than going back the way it came?", 3, "(a) $\\sqrt{30^2+40^2}=50$ m (2). (b) The way it came is $70$ m, so $20$ m shorter (1).", "H", wp=True),
W("A ladder of 13 m rests against one wall of a street, its top 12 m high. Without moving the foot, it is turned over to the opposite wall and reaches 5 m high. Find the width of the street.", 4, "Foot to first wall $=\\sqrt{169-144}=5$ m (1). Foot to second wall $=\\sqrt{169-25}=12$ m (2). Width $=5+12=17$ m (1).", "H", wp=True),
W("A lotus stalk rises $\\frac12$ cubit above the water. When pulled aside it just touches the water 2 cubits from where it stood. Find the depth of the water.", 4, "Depth $x$, stalk length $x+\\frac12$ (1). $x^2+2^2=\\left(x+\\frac12\\right)^2$ (1) gives $4=x+\\frac14$ (1). $x=3.75$ cubits (1).", "H", wp=True),
W("Starting with a square of side 8 cm, a square of half its area is made by joining the midpoints of its sides. Find the area and the side of the new square and show that the side is $4\\sqrt2$ cm.", 4, "Area of original $=64$, so new area $=32$ cm² (1). Each side of the new square is the hypotenuse of a right triangle with legs 4 and 4 (1): $\\sqrt{16+16}=\\sqrt{32}$ (1) $=4\\sqrt2$ cm (1).", "H"),
W("**Case study.** A tent is held up by a vertical pole 20 m high. Six ropes run from the top of the pole to pegs on the ground, each peg 21 m from the foot of the pole. Find the length of one rope, the total rope needed, and the cost at ₹ 35 per metre.", 4, "One rope $=\\sqrt{20^2+21^2}=\\sqrt{841}=29$ m (1). Total $=6\\times29=174$ m (1). Cost $=174\\times35=$ ₹ 6090 (2).", "H", wp=True),
W("**Case study.** A tubewell is at one corner A of a rectangular field 120 m by 90 m and the water tank is at the opposite corner C. A pipe along two sides costs ₹ 40 per metre; a pipe along the diagonal costs ₹ 60 per metre because of digging through rock. Find the cost of each plan and say which is cheaper and by how much.", 5, "Diagonal $=\\sqrt{120^2+90^2}=150$ m (1). Along the sides: $210$ m (1), cost $210\\times40=$ ₹ 8400 (1). Diagonal: $150\\times60=$ ₹ 9000 (1). The sides plan is cheaper by ₹ 600 (1).", "H", wp=True),
]

_o = _old(14)
_i = max(i for i, b in enumerate(_o["blocks"]) if b[0] == "h2")
_pre, _tail = _o["blocks"][:_i], _o["blocks"][_i:]
_extra = [
 ("h2", "The Theorem and Its Proof by Rearrangement"),
 ("p", "Take four copies of a right triangle with perpendicular sides **a**, **b** and hypotenuse **c**. Place them inside a big square of side **a + b**, with their hypotenuses forming a tilted inner four-sided figure. This inner figure has four equal sides **c** and all its angles are right angles, so it is a square of area c²."),
 ("table", ["Step", "Argument"], [["Area of the big square", "(a + b)² = a² + 2ab + b²"], ["Four triangles", "4 × ½ab = 2ab"], ["Inner square (what is left)", "(a² + 2ab + b²) − 2ab = a² + b²"], ["But the inner square has side c", "so c² = a² + b²"]]),
 ("note", "IMPORTANT", "Baudhāyana stated this result in the Śulba-Sūtra long before Pythagoras, using it to build altars from rope. In this chapter the same rule is called the **Baudhāyana–Pythagoras theorem**."),
 ("h2", "Converse: Is a Triangle Right-Angled?"),
 ("p", "If the sides of a triangle satisfy **a² + b² = c²** where c is the **longest** side, the angle opposite c is a right angle. Builders used this: a rope with 12 equal parts folded into sides of 3, 4 and 5 parts always gives a perfect right angle."),
 ("table", ["Sides", "Check with the longest side", "Right-angled?"], [["3, 4, 5", "9 + 16 = 25 = 5²", "Yes"], ["20, 48, 52", "400 + 2304 = 2704 = 52²", "Yes"], ["9, 40, 41", "81 + 1600 = 1681 = 41²", "Yes"], ["7, 9, 12", "49 + 81 = 130 but 12² = 144", "No"], ["11, 60, 62", "121 + 3600 = 3721 but 62² = 3844", "No"]]),
 ("h2", "Formulae and Quick Facts"),
 ("note", "FORMULA", "Hypotenuse: c = √(a² + b²).   Missing leg: b = √(c² − a²).   Diagonal of a rectangle l × w: d = √(l² + w²).   Diagonal of a square of side a: d = a√2, so area = d² ÷ 2."),
 ("note", "FORMULA", "Equilateral triangle of side s: height h = (√3 ÷ 2) × s, area = (√3 ÷ 4) × s².   Isosceles triangle with equal sides l and base b: height = √(l² − (b ÷ 2)²).   Rhombus with diagonals d₁, d₂: side = √((d₁ ÷ 2)² + (d₂ ÷ 2)²)."),
 ("table", ["Primitive triple", "Check", "Some multiples"], [["(3, 4, 5)", "9 + 16 = 25", "(6, 8, 10), (9, 12, 15), (12, 16, 20), (21, 28, 35)"], ["(5, 12, 13)", "25 + 144 = 169", "(10, 24, 26), (15, 36, 39)"], ["(8, 15, 17)", "64 + 225 = 289", "(16, 30, 34)"], ["(7, 24, 25)", "49 + 576 = 625", "(14, 48, 50)"], ["(20, 21, 29)", "400 + 441 = 841", "(40, 42, 58)"], ["(9, 40, 41)", "81 + 1600 = 1681", "(18, 80, 82)"]]),
 ("p", "A general recipe: for any counting number **m > 1**, **(2m, m² − 1, m² + 1)** is a triple, because (2m)² + (m² − 1)² = m⁴ + 2m² + 1 = (m² + 1)². With m = 2, 3, 4, 5 this gives (4, 3, 5), (6, 8, 10), (8, 15, 17) and (10, 24, 26). For an odd number n, **(n, (n² − 1) ÷ 2, (n² + 1) ÷ 2)** is a triple, for example n = 11 gives (11, 60, 61)."),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Ladder against a wall"),
 ("steps", [("Question", "A 25 m ladder reaches a window 24 m high. How far is its foot from the wall? How high does it reach if the foot is pulled 8 m further out?"), ("Foot distance", "√(25² − 24²) = √49 = 7 m."), ("New distance", "7 + 8 = 15 m, so height = √(625 − 225) = √400 = **20 m**.")]),
 ("h3", "Example 2 — A broken bamboo"),
 ("steps", [("Question", "A bamboo 32 cubits high breaks so that its top touches the ground 16 cubits from the foot. Find the height of the break."), ("Set up", "Let the break be at height x. The fallen part is 32 − x and forms the hypotenuse."), ("Equation", "x² + 16² = (32 − x)², so 256 = 1024 − 64x, giving x = **12 cubits**. Check: 12² + 16² = 144 + 256 = 400 = 20²."),]),
 ("h3", "Example 3 — Height of an isosceles triangle"),
 ("steps", [("Question", "Find the height and area of a triangle with sides 17, 17 and 16 cm."), ("Use symmetry", "The height from the apex bisects the base, so each half is 8 cm."), ("Height", "√(17² − 8²) = √225 = 15 cm."), ("Area", "½ × 16 × 15 = **120 cm²**.")]),
 ("h3", "Example 4 — Rhombus"),
 ("steps", [("Question", "A rhombus has perimeter 100 cm and one diagonal 48 cm. Find the other diagonal and the area."), ("Side", "100 ÷ 4 = 25 cm. Half of the given diagonal = 24 cm."), ("Other half", "√(25² − 24²) = 7 cm, so the other diagonal is 14 cm."), ("Area", "½ × 48 × 14 = **336 cm²**.")]),
 ("h3", "Example 5 — Two poles"),
 ("steps", [("Question", "Poles 9 m and 14 m high stand 12 m apart. Distance between their tops?"), ("Right triangle", "Horizontal side 12 m; vertical side = 14 − 9 = 5 m."), ("Distance", "√(144 + 25) = **13 m**.")]),
 ("h3", "Example 6 — Lotus in a pond"),
 ("steps", [("Question", "A lotus stands ½ cubit above the water and, pulled aside, touches the water 2 cubits away. Find the depth."), ("Equation", "x² + 2² = (x + ½)², so 4 = x + ¼."), ("Answer", "x = **3.75 cubits**.")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Situation", "Draw", "Right triangle sides"], [
  ["Ladder against a wall", "wall, ground, ladder", "legs: height and foot distance; hypotenuse: ladder"],
  ["Wire or rope to a pole or tent", "vertical pole and slanting rope", "legs: pole height and peg distance; hypotenuse: rope"],
  ["Walking east then north", "an L-shaped path", "legs: the two walks; hypotenuse: straight distance"],
  ["Diagonal of a field, screen or door", "rectangle with its diagonal", "legs: length and width"],
  ["Two poles or buildings of different heights", "poles with a horizontal line joining the lower top", "legs: gap between poles and height difference"],
  ["Broken tree or bamboo", "standing part, fallen part, ground", "hypotenuse is the fallen part (32 − x)"]]),
 ("note", "REMEMBER", "Always draw the right triangle first, name the hypotenuse (opposite the right angle), and decide whether you need **a² + b²** (find the longest side) or **c² − a²** (find a shorter side)."),
]
CH = dict(_o, num=9, blocks=_pre + _extra + _tail,
          takeaways=_o["takeaways"] + ["The converse also holds: if a² + b² = c² for the longest side c, the triangle is right-angled.", "Most word problems (ladders, poles, ropes, fields, screens) hide a right triangle; draw it before calculating.", "Triples can be generated: (2m, m² − 1, m² + 1) for every m > 1, and scaled by any k."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
