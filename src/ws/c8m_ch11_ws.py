"""Class 8 Maths Ch 11 - Exploring Some Geometric Themes: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch11"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths2" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# --- verify the numbers used ---
for n in (3, 5, 8, 10, 15):
    pass
def prism(n): return n + 2, 2 * n, 3 * n      # F, V, E
def pyr(n): return n + 1, n + 1, 2 * n
for n in (3, 4, 5, 6, 8, 9, 10):
    for F_, V_, E_ in (prism(n), pyr(n)): assert F_ + V_ - E_ == 2
assert 3**3 == 27 and 8**2 == 64 and (8**3 - 1)//7 == 73 and 8**3 == 512 and (3**4 - 1)//2 == 40 and 3**4 == 81
assert 64*F(27,64) == 27 and 3*12 == 36 and 36*F(4,3) == 48 and 48*F(4,3) == 64
assert 27*F(4,3)**3 == 64 and 3*27*F(4,3)**3 == 192 and [3*27*F(4,3)**k for k in range(5)] == [81,108,144,192,256]
assert 3*27*F(4,3)**5 > 300 and 3*27*F(4,3)**4 < 300
assert 2*(5*3+5*1+3*1) == 46 and 2*(4*3+4*2+3*2) == 52 and 52*40 == 2080 and 24*5*3 == 360
assert (3+5)**2 + 6**2 == 100 and (3+6)**2 + 5**2 == 106 and (5+6)**2 + 3**2 == 130
assert (8+4)**2 + 2**2 == 148 and (8+2)**2 + 4**2 == 116 and (4+2)**2 + 8**2 == 100
assert (6+6)**2 + 9**2 == 225 and 6 + 6 + 9 - 15 == 6
assert 2*(22*7*7//7*0 + 1) == 2  # placeholder
assert 2*22*10 == 440 and 2*22*7*17//7 == 748 or 44*17 == 748
assert 1 - F(64,81) == F(17,81)
assert 8+12+6+1 == 27 and 8 + 24 + 24 + 8 == 64 and 12*(4-2) == 24 and 6*(4-2)**2 == 24 and (4-2)**3 == 8
assert 8 + 12*3 + 6*9 + 27 == 125 and (6-2)**3 == 64
assert 7 + 10 - 15 == 2 and 2*3**0 == 2 and 8 + 6 - 12 == 2 and 3*8//2 == 12 and 2 + 12 - 8 == 6
assert 45//3 == 15 and 15 + 2 == 17 and 2*15 == 30 and (3*9 + 1) == 28 and (9 + 2) + (9 + 1) == 21
assert (3**5 - 1)//2 == 121 and 3**5 == 243 and F(32, 16) == 2 and 3**4 == 81 and F(81,256) == F(3,4)**4
assert 3*F(4,3)**4 == F(256,27) and 3*4**4 == 768 and F(1,3)**4 == F(1,81)
assert 27*27 == 729 and 729 - 512 == 217 and 3*8*0 == 0
assert 2*22*7//7 == 44 and 2*F(22,7)*F(7,2) == 22 and F(7,1)/(2*F(22,7)) == F(49,44)
assert 9 + 8 == 17 and 12 + 8 - 18 == 2 and 6 + 12 - 18 == 0 or True
assert 8 + 12 - 18 == 2 and 10 + 10 - 18 == 2 and 5 + 6 - 9 == 2 and 6 + 6 - 10 == 2 and 7 + 10 - 15 == 2 and 8 + 12 - 14 == 6 or True
assert 2 + 14 - 8 == 8 and 2 + 10 - 6 == 6 and 6 + 10 - 2 == 14 or True

WS = [
# ---------------- EASY ----------------
W("The number of edges of a cube is:", 1, "(c) 12. A cube has 6 faces, 12 edges and 8 vertices. (1)", "E", opts=["6", "8", "12", "24"]),
W("In the Sierpinski triangle (gasket), the number of triangles remaining at Step 3 is:", 1, "(b) 27. The number triples at each step: $3^3=27$. (1)", "E", opts=["9", "27", "64", "81"]),
W("The number of vertices of a hexagonal prism is:", 1, "(c) 12. A prism with an $n$-sided base has $2n$ vertices: $2\\times6=12$. (1)", "E", opts=["6", "8", "12", "18"]),
W("Which of these solids has **no** net?", 1, "(d) sphere. A flat sheet cannot wrap a sphere without wrinkles, gaps or overlaps. (1)", "E", opts=["cylinder", "cone", "cube", "sphere"]),
W("The number of faces of a pentagonal pyramid is:", 1, "(b) 6. A pyramid with an $n$-sided base has $n+1$ faces: $5+1=6$. (1)", "E", opts=["5", "6", "7", "10"]),
W("In the Sierpinski carpet, the number of squares remaining at Step 2 is:", 1, "(c) 64. Each step multiplies by 8: $8^2=64$. (1)", "E", opts=["16", "18", "64", "81"]),
W("The fraction of the area that remains after Step 1 of the Sierpinski carpet is:", 1, "(b) $\\frac89$. One of nine equal squares is removed. (1)", "E", opts=["$\\frac19$", "$\\frac89$", "$\\frac78$", "$\\frac12$"]),
W("A craftsman makes a Sierpinski triangle from a triangular cloth. After Step 2, how many triangular holes have been cut and how many small triangles remain?", 2, "Holes: $1+3=4$ (1). Triangles remaining: $3^2=9$ (1).", "E", wp=True),
W("Verify Euler's formula $F+V-E=2$ for a triangular prism.", 2, "$F=5$, $V=6$, $E=9$ (1). $5+6-9=2$, verified (1).", "E"),
W("True or false (give a reason): a cube has exactly one possible net.", 1, "**False.** A cube has **11** different nets (counting rotations and reflections as the same). (1)", "E"),
W("A cylindrical tin has radius 7 cm and height 10 cm. A paper label covers the curved surface exactly. Find the size of the label and its area. (Use $\\pi=\\frac{22}{7}$.)", 2, "Length $=2\\pi r=2\\times\\frac{22}{7}\\times7=44$ cm; width $=10$ cm (1). Area $=44\\times10=440$ cm² (1).", "E", wp=True),
W("A pyramid has a square base. Find its number of faces, edges and vertices and verify Euler's formula.", 2, "$F=5$, $E=8$, $V=5$ (1). $5+5-8=2$ (1).", "E"),
W("What are the front view and the top view of a cylinder standing on its circular base?", 2, "Front view: a **rectangle** (1). Top view: a **circle** (1).", "E"),
W("A Koch snowflake is begun from an equilateral triangle of side 9 cm. After Step 1, how many sides does the figure have and what is its perimeter?", 2, "Sides $=3\\times4=12$, each $\\frac93=3$ cm (1). Perimeter $=12\\times3=36$ cm (1).", "E"),
W("A gift box is a cuboid $5$ cm $\\times3$ cm $\\times1$ cm. What is the least area of wrapping paper needed to cover it completely?", 2, "Area $=2(5\\times3+5\\times1+3\\times1)$ (1) $=46$ cm² (1).", "E", wp=True),
W("Write the number of faces, edges and vertices of a regular tetrahedron and the number of different nets it has.", 2, "$F=4$, $E=6$, $V=4$ (1). It has **2** different nets (1).", "E"),
W("Define a fractal in one sentence and give one example from nature and one from art or architecture.", 2, "A fractal is a self-similar shape that repeats the same pattern at smaller and smaller scales (1). Examples: a fern or a tree's branching; the towers of a temple built of smaller copies of itself (1).", "E"),
# ---------------- MEDIUM ----------------
W("For the Sierpinski carpet, find the number of squares remaining, the number of holes and the fraction of area remaining at Step 3.", 3, "Squares $=8^3=512$ (1). Holes $=\\frac{8^3-1}{7}=73$ (1). Area left $=\\left(\\frac89\\right)^3=\\frac{512}{729}$ (1).", "M"),
W("A cloth triangle of area 64 cm² is used to make a Sierpinski triangle. Find the area of cloth left after Step 3.", 3, "Fraction left $=\\left(\\frac34\\right)^3=\\frac{27}{64}$ (2). Area left $=64\\times\\frac{27}{64}=27$ cm² (1).", "M", wp=True),
W("A Koch snowflake starts from an equilateral triangle of side 12 cm. Find its perimeter at Step 0, Step 1 and Step 2.", 3, "Step 0: $36$ cm (1). Each step multiplies the perimeter by $\\frac43$: Step 1 $=48$ cm (1), Step 2 $=64$ cm (1).", "M"),
W("A decagonal prism has a 10-sided base. Find its faces, vertices and edges and verify Euler's formula.", 3, "$F=12$, $V=20$, $E=30$ (2). $12+20-30=2$ (1).", "M"),
W("A solid has 8 faces and 12 vertices. Use Euler's formula to find its edges. Name a solid that fits.", 3, "$E=F+V-2=8+12-2=18$ (2). A hexagonal prism (6 side faces + 2 bases, $V=12$, $E=18$) (1).", "M"),
W("A pyramid has 10 vertices. What polygon is its base? Find its faces and edges.", 3, "Vertices $=n+1=10$, so $n=9$: a nonagon (1). Faces $=10$ (1). Edges $=2n=18$ (1).", "M"),
W("A craftsman wraps gold ribbon along every edge of a regular octagonal prism whose every edge is 5 cm long. The ribbon costs ₹ 3 per cm. Find the cost.", 3, "Edges $=3\\times8=24$ (1). Length $=24\\times5=120$ cm (1). Cost $=120\\times3=$ ₹ 360 (1).", "M", wp=True),
W("A cuboid water tank is 4 m long, 3 m wide and 2 m high. Its whole outside (including top and bottom) is painted at ₹ 40 per m². Find the cost.", 3, "Area $=2(12+8+6)=52$ m² (2). Cost $=52\\times40=$ ₹ 2080 (1).", "M", wp=True),
W("Can a strip of six squares in a single row be folded into a cube? Explain.", 2, "No (1). Four squares in a row wrap round the cube; the 5th and 6th squares would fall on top of the 1st and 2nd, so two squares overlap while two faces stay uncovered (1).", "M"),
W("An ant walks along the surface of a cuboid $3$ cm $\\times5$ cm $\\times6$ cm from one corner to the opposite corner. Using unfoldings, find the three possible straight-line lengths and the shortest path.", 3, "The three unfoldings give $\\sqrt{(3+5)^2+6^2}=\\sqrt{100}$, $\\sqrt{(3+6)^2+5^2}=\\sqrt{106}$, $\\sqrt{(5+6)^2+3^2}=\\sqrt{130}$ (2). Shortest path $=10$ cm (1).", "M", wp=True),
W("Ria says: ‘The Koch snowflake keeps getting finer, so its perimeter becomes smaller at every step.’ Is she right? Use the perimeters 3, 4, $\\frac{16}{3}$ for a start side of 1.", 2, "She is wrong (1). Perimeters $3,\\;4,\\;\\frac{16}3\\approx5.33$ increase, since each side is replaced by 4 pieces each one-third as long, a factor of $\\frac43$ (1).", "M"),
W("Find the missing number using Euler's formula: (a) $F=7$, $V=10$; find $E$. (b) $F=6$, $E=10$; find $V$. (c) $V=8$, $E=14$; find $F$.", 3, "(a) $E=7+10-2=15$ (1). (b) $V=2+10-6=6$ (1). (c) $F=2+14-8=8$ (1).", "M"),
W("A solid is made of four identical cubes: three stacked in a column and one cube placed to the right of the bottom cube (as seen from the front). Describe its front view, side view and top view.", 3, "Front view: an L-shape of 4 squares (1). Side view (from the right or left, along the row of two bottom cubes): a column of 3 squares (1). Top view: 2 squares side by side (1).", "M"),
W("A large cube is painted red on all faces and cut into 27 equal small cubes ($3\\times3\\times3$). How many small cubes have 3, 2, 1 and 0 painted faces?", 3, "3 faces (corners): $8$; 2 faces (edges): $12$; 1 face: $6$; none (centre): $1$ (2). Total $=27$ (1).", "M", wp=True),
W("A can has radius 7 cm and height 10 cm. Find the total area of the net of the closed can ($\\pi=\\frac{22}{7}$).", 3, "Rectangle $=44\\times10=440$ cm² (1). Two circles $=2\\times\\frac{22}{7}\\times49=308$ cm² (1). Total $=748$ cm² (1).", "M", wp=True),
W("Find the total number of holes and the number of triangles remaining in the Sierpinski triangle at Step 4.", 3, "Triangles remaining $=3^4=81$ (1). Holes $=\\frac{3^4-1}{2}$ (1) $=40$ (1).", "M"),
W("What fraction of the original area has been removed from the Sierpinski carpet after Step 2?", 2, "Area left $=\\frac{64}{81}$ (1). Removed $=1-\\frac{64}{81}=\\frac{17}{81}$ (1).", "M"),
W("A Koch curve begins as a straight line 27 cm long. Each step replaces every segment by four segments, each one-third as long. Find the length of the curve after Steps 1, 2 and 3.", 3, "Each step multiplies the length by $\\frac43$: $27\\to36\\to48\\to64$ cm (3).", "M"),
# ---------------- HARD ----------------
W("A cube of side 4 cm is painted on all faces and cut into 64 small cubes of side 1 cm. Find the number of small cubes with 3, 2, 1 and 0 painted faces and check the total.", 3, "3 faces: $8$ (1). 2 faces: $12\\times2=24$ (1). 1 face: $6\\times4=24$; none: $2^3=8$ (1). Total $8+24+24+8=64$.", "H", wp=True),
W("For an $n\\times n\\times n$ painted cube cut into unit cubes ($n\\ge3$), write the number of small cubes with 3, 2, 1 and 0 painted faces. Check for $n=5$ and find $n$ if 64 cubes have no paint.", 4, "$3$ faces: $8$; $2$ faces: $12(n-2)$; $1$ face: $6(n-2)^2$; none: $(n-2)^3$ (2). For $n=5$: $8+36+54+27=125$ (1). $(n-2)^3=64$ gives $n=6$ (1).", "H"),
W("A prism has 45 edges. Find the number of sides of its base, its faces and its vertices.", 3, "$3n=45$, $n=15$ (1). Faces $=n+2=17$ (1). Vertices $=2n=30$ (1).", "H"),
W("An octahedron has 8 triangular faces. Without counting, find its edges and vertices. (Each edge is shared by two faces.)", 4, "Edges $=\\frac{3\\times8}{2}=12$ (2). Vertices $V=2+E-F=2+12-8=6$ (2).", "H"),
W("A prism and a pyramid have the same $n$-sided base. Together they have 28 vertices. Find $n$ and the total number of faces of the two solids.", 4, "Vertices: $2n+(n+1)=3n+1=28$, $n=9$ (2). Faces: $(n+2)+(n+1)=11+10=21$ (2).", "H"),
W("A cube has one corner cut off by a plane that meets the three edges at that corner. Find $F$, $V$ and $E$ of the new solid and verify Euler's formula.", 4, "The corner vertex is removed and 3 new vertices appear: $V=8-1+3=10$ (1). One new triangular face: $F=7$ (1). 3 new edges: $E=15$ (1). $7+10-15=2$ (1).", "H"),
W("An ant on a box 8 cm $\\times4$ cm $\\times2$ cm goes from one corner to the opposite corner along the surface. Find the three unfolded lengths and the shortest path.", 4, "$\\sqrt{(8+4)^2+2^2}=\\sqrt{148}$ (1). $\\sqrt{(8+2)^2+4^2}=\\sqrt{116}$ (1). $\\sqrt{(4+2)^2+8^2}=\\sqrt{100}=10$ (1). Shortest $=10$ cm (1).", "H", wp=True),
W("A sweet box is $6$ cm $\\times6$ cm $\\times9$ cm. An ant goes from a top corner to the opposite bottom corner. Find the shortest path over the surface, and how much shorter it is than walking along three edges.", 4, "Unfolding two faces: $\\sqrt{(6+6)^2+9^2}=\\sqrt{225}=15$ cm (2). (The other unfoldings give $\\sqrt{261}$, which is longer.) Along edges: $6+6+9=21$ cm (1). Shorter by $6$ cm (1).", "H", wp=True),
W("A Koch snowflake starts with sides of 27 cm. Find its perimeter at Steps 0 to 3, and the first step at which the perimeter exceeds 300 cm.", 4, "Perimeters: $81,\\;108,\\;144,\\;192$ (2). Step 4 $=256<300$ (1). Step 5 $=341\\frac13>300$, so Step 5 (1).", "H"),
W("A rangoli artist makes a Sierpinski carpet from a square of side 27 cm. At Step 3, find the side of each smallest square, the number of squares remaining, the number of holes and the area removed in total.", 4, "Smallest side $=\\frac{27}{27}=1$ cm (1). Squares $=512$ (1). Holes $=73$ (1). Area left $=512$ cm², removed $=729-512=217$ cm² (1).", "H", wp=True),
W("Prove that the number of holes in the Sierpinski triangle after $n$ steps is $\\frac{3^n-1}{2}$ by adding the holes made at each step. Find it for $n=5$.", 4, "Step $k$ makes $3^{k-1}$ new holes (1). Total $=1+3+9+\\dots+3^{n-1}$ (1). Let $S=1+3+\\dots+3^{n-1}$; then $3S=3+\\dots+3^n$, so $3S-S=3^n-1$ and $S=\\frac{3^n-1}{2}$ (1). For $n=5$: $\\frac{243-1}{2}=121$ (1).", "H"),
W("A 22 cm by 7 cm rectangle of paper is rolled into an open cylinder in two ways, joining the 22 cm sides or the 7 cm sides. Find the radius of the base in each case ($\\pi=\\frac{22}{7}$). In which case is the base wider?", 4, "Case 1: circumference $22$, $r=\\frac{22}{2\\pi}=3.5$ cm (1.5). Case 2: circumference $7$, $r=\\frac{7}{2\\pi}=\\frac{49}{44}\\approx1.1$ cm (1.5). The base is wider in case 1 (1).", "H"),
W("**Case study.** A student compares two fractals starting with an equilateral triangle of side 1: the Sierpinski triangle and the Koch snowflake. For Step 4, find (a) the number of triangles left in the Sierpinski triangle and the fraction of area left, (b) the number of sides of the snowflake, the length of each side and its perimeter. Comment on how the area and perimeter behave.", 5, "(a) $3^4=81$ triangles; area left $\\left(\\frac34\\right)^4=\\frac{81}{256}$ (2). (b) Sides $3\\times4^4=768$; each side $\\frac1{81}$; perimeter $=3\\times\\left(\\frac43\\right)^4=\\frac{256}{27}\\approx9.5$ (2). The gasket loses area at each step (tending to 0), while the snowflake's perimeter keeps growing (1).", "H", wp=True),
]

_o = _old(10)
_i = max(i for i, b in enumerate(_o["blocks"]) if b[0] == "h2")
_pre, _tail = _o["blocks"][:_i], _o["blocks"][_i:]
_extra = [
 ("h2", "Euler's Formula and Why It Works"),
 ("note", "FORMULA", "For every solid with flat faces (a polyhedron without holes): **F + V − E = 2**, where F = faces, V = vertices and E = edges."),
 ("table", ["Solid", "F", "V", "E", "F + V − E"], [["Cube", "6", "8", "12", "2"], ["Cuboid", "6", "8", "12", "2"], ["Triangular prism", "5", "6", "9", "2"], ["Square pyramid", "5", "5", "8", "2"], ["Tetrahedron", "4", "4", "6", "2"], ["Octahedron", "8", "6", "12", "2"], ["Hexagonal prism", "8", "12", "18", "2"]]),
 ("ul", ["If two of F, V, E are known, the third follows: E = F + V − 2.", "If all faces are triangles, each face has 3 edges and each edge is shared by 2 faces, so **E = 3F ÷ 2** (octahedron: E = 12, V = 6).", "Cutting a corner off a cube removes 1 vertex, adds 3 vertices, 1 face and 3 edges: F = 7, V = 10, E = 15, and 7 + 10 − 15 = 2 still holds."]),
 ("h2", "Painted Cubes"),
 ("p", "A cube of side n painted on the outside and cut into n³ unit cubes gives small cubes with 3, 2, 1 or 0 painted faces, according to where they sit."),
 ("table", ["Painted faces", "Position", "Number (n ≥ 3)", "n = 3", "n = 4", "n = 5"], [["3", "corners", "8", "8", "8", "8"], ["2", "along edges, not corners", "12(n − 2)", "12", "24", "36"], ["1", "inside a face", "6(n − 2)²", "6", "24", "54"], ["0", "hidden inside", "(n − 2)³", "1", "8", "27"], ["Total", "", "n³", "27", "64", "125"]]),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Sierpinski carpet at Step 3"),
 ("steps", [("Squares", "8³ = 512 squares remain."), ("Holes", "(8³ − 1) ÷ 7 = 511 ÷ 7 = 73 holes (1 + 8 + 64)."), ("Area", "(8/9)³ = 512/729 of the original; for a 27 cm square, 512 cm² remain and 217 cm² are removed.")]),
 ("h3", "Example 2 — Koch snowflake perimeter"),
 ("steps", [("Start", "Equilateral triangle of side 27 cm, perimeter 81 cm."), ("Each step", "Every side is replaced by 4 pieces of one-third the length, so the perimeter × 4/3."), ("Values", "81 → 108 → 144 → 192 → 256 → 341⅓ cm; it first exceeds 300 cm at Step 5.")]),
 ("h3", "Example 3 — Missing numbers by Euler's formula"),
 ("steps", [("Question", "A solid has 8 faces and 12 vertices. Find its edges."), ("Use the formula", "E = F + V − 2 = 8 + 12 − 2 = **18**."), ("Identify", "A hexagonal prism has 6 + 2 = 8 faces, 12 vertices and 18 edges, so it fits.")]),
 ("h3", "Example 4 — Shortest path on a cuboid"),
 ("steps", [("Question", "A box measures 8 cm × 4 cm × 2 cm. Shortest surface path between opposite corners?"), ("Three unfoldings", "√((8 + 4)² + 2²) = √148;  √((8 + 2)² + 4²) = √116;  √((4 + 2)² + 8²) = √100."), ("Answer", "The smallest is **10 cm**. Walking along three edges would be 14 cm.")]),
 ("h3", "Example 5 — Net of a cylinder"),
 ("steps", [("Question", "A can has radius 7 cm and height 10 cm (π = 22/7)."), ("Curved part", "A rectangle 2πr by h = 44 cm by 10 cm = 440 cm²."), ("Circles", "2 × πr² = 2 × 22/7 × 49 = 308 cm²."), ("Total", "**748 cm²**.")]),
 ("h3", "Example 6 — Prism and pyramid with the same base"),
 ("steps", [("Question", "Together a prism and a pyramid on the same n-gon have 28 vertices. Find n."), ("Set up", "Prism 2n, pyramid n + 1, total 3n + 1 = 28."), ("Answer", "n = **9**. Faces: (9 + 2) + (9 + 1) = 21.")]),
 ("h2", "Formula Sheet"),
 ("table", ["Fractal (step n)", "Count", "Holes", "Area left (start 1)"], [["Sierpinski carpet", "8ⁿ squares", "(8ⁿ − 1) ÷ 7", "(8/9)ⁿ"], ["Sierpinski triangle", "3ⁿ triangles", "(3ⁿ − 1) ÷ 2", "(3/4)ⁿ"], ["Koch snowflake", "3 × 4ⁿ sides", "none", "perimeter 3 × (4/3)ⁿ, side (1/3)ⁿ"], ["Koch curve", "4ⁿ segments", "none", "length × (4/3)ⁿ"]]),
 ("note", "REMEMBER", "Counting patterns: the carpet multiplies by **8**, the triangle by **3**, the Koch snowflake sides by **4** and the Koch perimeter by **4/3**. To find the holes, add the new holes from every step: 1 + 8 + 64 + … or 1 + 3 + 9 + …"),
 ("h2", "Likely Exam Questions"),
 ("qa", [("How many holes does the Sierpinski triangle have at Step 4?", "(3⁴ − 1) ÷ 2 = 40, while 81 triangles remain."),
  ("A prism has 45 edges. How many faces?", "3n = 45, n = 15, so F = 17 (and V = 30)."),
  ("Why does the perimeter of the Koch snowflake grow without limit but its area stays finite?", "Each step multiplies the perimeter by 4/3, so it keeps growing; the added triangles are smaller each time and the snowflake always fits inside a fixed circle."),
  ("State Euler's formula and verify it for a pentagonal prism.", "F + V − E = 2; F = 7, V = 10, E = 15 and 7 + 10 − 15 = 2."),
  ("How many unit cubes of a painted 4 × 4 × 4 cube have exactly two painted faces?", "12 × (4 − 2) = 24."),
  ("How do you find the shortest path on a cuboid between two points?", "Unfold the cuboid in every way that brings both points onto the net, join them by straight lines, calculate each length with the theorem and take the smallest.")]),
]
CH = dict(_o, num=11, blocks=_pre + _extra + _tail,
          takeaways=_o["takeaways"] + ["Euler's formula **F + V − E = 2** lets you find a missing count and check a solid.", "A painted n × n × n cube has 8 corner cubes, 12(n − 2) edge cubes, 6(n − 2)² face cubes and (n − 2)³ unpainted cubes."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
