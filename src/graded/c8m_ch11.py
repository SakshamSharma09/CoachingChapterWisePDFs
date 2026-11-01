"""Class 8 Maths Ch 11 - Exploring Some Geometric Themes (fractals, polyhedra, Euler's formula, nets, painted cubes)."""
from c8m_u import *

SLUG, NAME, CHNO = "Geometric_Themes", "Exploring Some Geometric Themes", 11

PN = {3: "triangular", 4: "square", 5: "pentagonal", 6: "hexagonal", 7: "heptagonal", 8: "octagonal", 9: "nonagonal", 10: "decagonal", 12: "dodecagonal"}
def prism(n): return n + 2, 2 * n, 3 * n       # F, V, E
def pyr(n): return n + 1, n + 1, 2 * n
def I(x):
    x = Fr(x); assert x.denominator == 1, x; return int(x)
def euler(F, V, E): return F + V - E == 2
def sier(n): return 3 ** n
def koch_len(L, n): return Fr(L) * Fr(4, 3) ** n

# ================= EASY =================
e1 = [M4(f"In the Sierpinski triangle construction, the number of small shaded triangles at stage {n} (stage 0 has one) is:", 3 ** n, [2 ** n * 3, 3 * n, 3 ** n - 1, 3 ** n + 3], f"Each stage triples the count: $3^{n}={3**n}$") for n in [1, 2, 3, 4, 5, 6]]
e2 = [M4(f"The number of faces of a {PN[n]} prism is:", prism(n)[0], [n, n + 1, 2 * n, 3 * n], f"$n+2={n+2}$ (two bases and $n$ rectangles)") for n in [3, 5, 6, 7, 8, 9]]
e3 = [M4(f"The number of vertices of a {PN[n]} pyramid is:", pyr(n)[1], [n, 2 * n, n + 2, n - 1], f"$n$ base vertices + 1 apex $={n+1}$") for n in [3, 5, 6, 7, 8, 10]]
e4 = [M4(f"The number of edges of a {PN[n]} prism is:", prism(n)[2], [2 * n, n + 2, 2 * n + 2, 4 * n], f"$3n={3*n}$") for n in [3, 5, 6, 8, 9, 10]]
e5 = [M4(f"A polyhedron has {F} faces and {V} vertices. By Euler's formula, its number of edges is:", F + V - 2, [F + V, F + V - 1, F * V // 2 if F * V // 2 != F + V - 2 else F + V + 3, F + V - 4], f"$F+V-E=2$ gives $E={F}+{V}-2={F+V-2}$") for F, V in [(6, 8), (5, 5), (5, 6), (8, 6), (7, 10), (4, 4)]]
e6 = [M4(f"The sum of the lengths of all the edges of a cube of side {s} cm is (in cm):", 12 * s, [6 * s, 8 * s, 4 * s, 12 * s + s], f"A cube has 12 edges: $12\\times{s}={12*s}$") for s in [3, 5, 6, 7, 9, 10]]
e7 = [M4("Euler's formula for a polyhedron with $F$ faces, $V$ vertices and $E$ edges is:", "$F+V-E=2$", ["$F+V+E=2$", "$F-V+E=2$", "$F+V=E$"], "Euler's formula"),
      M4("The number of faces of a cube is:", "6", ["4", "8", "12"], "Six square faces"),
      M4("The number of vertices of a cuboid is:", "8", ["6", "12", "4"], "Eight corners"),
      M4("A solid with a polygon as base and triangular faces meeting at a point is a:", "pyramid", ["prism", "cylinder", "cuboid"], "Definition of a pyramid"),
      M4("The faces of a prism other than the bases are:", "rectangles (parallelograms)", ["triangles", "circles", "pentagons only"], "Lateral faces"),
      M4("A figure in which the same pattern repeats at smaller scales is called a:", "fractal", ["polygon", "net", "prism"], "Self-similarity")]
EASY_A = [e1, e2, e3, e4, e5, e6, e7]
EASY_B = ([Q(f"Write the number of faces, vertices and edges of a {PN[n]} prism.", f"Faces $=n+2={prism(n)[0]}$ (1); vertices $=2n={prism(n)[1]}$, edges $=3n={prism(n)[2]}$ (1).", "1+1") for n in [3, 5, 6, 8]]
          + [Q(f"A solid has {F} faces, {V} vertices and {E} edges. Verify Euler's formula.", f"$F+V-E={F}+{V}-{E}$ (1) $={F+V-E}$, so Euler's formula is verified (1).", "1+1") for F, V, E in [(6, 8, 12), (5, 5, 8), (4, 4, 6), (8, 12, 18)]]
          + [Q(f"Find the total length of all edges of a cube of side {s} cm.", f"A cube has 12 equal edges (1); total $=12\\times{s}={12*s}$ cm (1).", "1+1") for s in [4, 8, 11, 15]])
EASY_C = ([Q(f"State the number of faces, vertices and edges of a {PN[n]} pyramid and verify Euler's formula.", f"Faces $={n+1}$, vertices $={n+1}$, edges $={2*n}$ (2); $F+V-E={n+1}+{n+1}-{2*n}=2$ (1).", "2+1") for n in [3, 4, 5, 6, 7, 8]]
          + [Q(f"In the Sierpinski triangle, how many shaded triangles are there at stage {n}? How many more are there at stage {n+1}?", f"Stage {n}: $3^{n}={3**n}$ (1); stage {n+1}: $3^{n+1}={3**(n+1)}$ (1); more $={3**(n+1)-3**n}$ (1).", "1+1+1") for n in [2, 3, 4, 5, 6, 7]]
          + [Q(f"A cuboid measures {l} cm by {b} cm by {h} cm. Find the total length of its edges and state its number of faces and vertices.", f"A cuboid has 4 edges of each length (1); total $=4({l}+{b}+{h})={4*(l+b+h)}$ cm (1); faces 6, vertices 8 (1).", "1+1+1") for l, b, h in [(5, 3, 2), (8, 4, 3), (10, 6, 4), (12, 5, 3), (9, 7, 2), (6, 6, 5)]])
EASY_D = ([Q(f"A Koch curve begins with a straight line of length {L} cm (stage 0). At each stage every segment is replaced by 4 segments each one-third as long. Find the number of segments, the length of each segment and the total length at stage 2.", f"Stage 1: 4 segments of {g(Fr(L,3))} cm (1); stage 2: $4\\times4=16$ segments (1); each of length $={g(Fr(L,9))}$ cm (1); total $=16\\times{g(Fr(L,9))}={g(Fr(16*L,9))}$ cm (2).", "1+1+1+2") for L in [9, 18, 27, 36, 45, 54]]
          + [Q(f"In the Sierpinski triangle, stage 0 has 1 shaded triangle. Fill in the number of shaded triangles at stages {n}, {n+1} and {n+2}. By what factor does the count grow at each stage?", f"Stage {n}: ${3**n}$ (1); stage {n+1}: ${3**(n+1)}$ (1); stage {n+2}: ${3**(n+2)}$ (1); each stage multiplies the number by 3 (2).", "1+1+1+2") for n in [1, 2, 3, 4, 5, 6]])

# ================= NCERT =================
n1 = [M4(f"A polyhedron has {V} vertices and {E} edges. The number of faces is:", 2 + E - V, [E - V, E + V - 2, 2 + E + V, 2 + E - V + 2], f"$F=2+E-V={2+E-V}$") for V, E in [(12, 18), (10, 15), (6, 9), (7, 12), (24, 36), (60, 90)]]
n2 = [M4(f"A Koch curve starts with one segment. The number of segments at stage {n} is:", 4 ** n, [3 ** n, 4 * n, 4 ** n - 1, 2 ** (n + 1)], f"Each segment becomes 4: $4^{n}={4**n}$") for n in [1, 2, 3, 4, 5]]
n3 = [M4(f"In the Sierpinski triangle (area of the original triangle taken as 1), the fraction of area still shaded after stage {n} is:", f"${fr(3**n, 4**n)}$", [f"${fr(1, 4**n)}$", f"${fr(3*n, 4*n)}$", f"${fr(3**n - 1, 4**n)}$"], f"Each stage keeps $\\frac34$: $(3/4)^{n}$") for n in [2, 3, 4, 5]]
n4 = [M4(f"A cube of side {n} cm is painted on all faces and cut into 1 cm cubes. The number of small cubes with exactly one face painted is:", 6 * (n - 2) ** 2, [12 * (n - 2), 8, (n - 2) ** 3, 6 * n * n], f"$6(n-2)^2=6\\times{(n-2)**2}$") for n in [3, 4, 5, 6, 7]]
n5 = [M4("The net of a cylinder consists of:", "two circles and one rectangle", ["two circles and one triangle", "one circle and one sector", "two rectangles and one circle"], "Unrolling the curved surface gives a rectangle"),
      M4("The net of a cone consists of:", "one circle and one sector", ["two circles and a rectangle", "one circle and one triangle", "one square and four triangles"], "Curved surface opens into a sector"),
      M4("The net of a triangular prism consists of:", "two triangles and three rectangles", ["three triangles and two rectangles", "five rectangles", "four triangles and one rectangle"], "Two bases and three lateral faces"),
      M4("The net of a square pyramid consists of:", "one square and four triangles", ["two squares and four triangles", "five squares", "one square and four rectangles"], "Base and four slant faces"),
      M4("The net of a regular tetrahedron consists of:", "four equilateral triangles", ["three equilateral triangles", "four squares", "two triangles and two squares"], "Four triangular faces"),
      M4("The net of a hexagonal prism consists of:", "two hexagons and six rectangles", ["two hexagons and eight rectangles", "one hexagon and six triangles", "six hexagons and two rectangles"], "Two bases and $n=6$ lateral faces")]
n6 = [M4("The top view of a cone standing on its base is a:", "circle (with a dot at the centre)", ["triangle", "square", "rectangle"], "Looking down, the base circle with the apex at centre"),
      M4("The front view of a cylinder standing on its base is a:", "rectangle", ["circle", "triangle", "square always"], "Side view of upright cylinder"),
      M4("The front view of a cone standing on its base is a:", "triangle", ["circle", "rectangle", "pentagon"], "Isosceles triangle"),
      M4("The top view of a cube is a:", "square", ["circle", "triangle", "hexagon"], "Looking down at the top face"),
      M4("The cross-section of a cube cut by a plane parallel to one of its faces is a:", "square", ["triangle", "circle", "hexagon"], "Same as the face"),
      M4("The cross-section of a cylinder cut by a plane parallel to its base is a:", "circle", ["rectangle", "ellipse only", "triangle"], "Congruent to the base")]
NCERT_A = [n1, n2, n3, n4, n5, n6]
NCERT_B = ([Q(f"A prism has {3*n} edges. Find the number of sides of its base and the number of faces.", f"Edges $=3n={3*n}$ so $n={n}$ (1); faces $=n+2={n+2}$ (1).", "1+1") for n in [7, 9, 11, 14]]
           + [Q(f"Verify Euler's formula for a {PN[n]} pyramid.", f"$F={n+1}$, $V={n+1}$, $E={2*n}$ (1); $F+V-E={n+1}+{n+1}-{2*n}=2$ (1).", "1+1") for n in [9, 10, 12, 14]]
           + [Q(f"A solid has {F} faces and {E} edges. Use Euler's formula to find its number of vertices.", f"$V=2+E-F$ (1) $={2+E-F}$ (1).", "1+1") for F, E in [(9, 21), (10, 24), (12, 30), (14, 36)]])
NCERT_C = ([Q(f"A cube of side {n} cm is painted on all faces and cut into 1 cm cubes. Find the number of small cubes with (i) exactly two faces painted (ii) exactly one face painted.", f"(i) $12(n-2)=12\\times{n-2}={12*(n-2)}$ (1+1); (ii) $6(n-2)^2=6\\times{(n-2)**2}={6*(n-2)**2}$ (1).", "2+1") for n in [3, 4, 5, 6, 7, 8]]
           + [Q(f"A Koch curve starts with a straight line of length {L} cm. How many segments are there at stage {n}, how long is each, and what is the total length?", f"Segments $=4^{n}={4**n}$ (1); each $=L/3^{n}={g(Fr(L,3**n))}$ cm (1); total $={g(koch_len(L,n))}$ cm (1).", "1+1+1") for L, n in [(27, 3), (81, 4), (9, 2), (18, 2), (54, 3), (162, 4)]]
           + [Q(f"A Sierpinski triangle starts with a triangle of area {A} cm². Find the shaded area after stage {n} and the area removed.", f"Shaded area $={A}\\times(3/4)^{n}={g(Fr(A*3**n,4**n))}$ cm² (2); removed $={g(A-Fr(A*3**n,4**n))}$ cm² (1).", "2+1") for A, n in [(64, 2), (256, 2), (256, 3), (512, 3), (1024, 3), (1024, 4)]])
NCERT_D = ([Q(f"Find the number of faces, vertices and edges of (i) a {PN[n]} prism and (ii) a {PN[n]} pyramid, and verify Euler's formula for both.", f"Prism: $F={n+2}$, $V={2*n}$, $E={3*n}$ (2); $F+V-E={n+2}+{2*n}-{3*n}=2$ (1); pyramid: $F={n+1}$, $V={n+1}$, $E={2*n}$ (1); $F+V-E={n+1}+{n+1}-{2*n}=2$ (1).", "2+1+1+1") for n in [3, 4, 5, 6, 7, 8]]
           + [Q(f"A cube of side {n} cm is painted and cut into 1 cm cubes. Find the number of cubes with three, two, one and no painted faces. Verify that these add up to {n**3}.", f"Three faces: 8 (1); two faces: $12({n}-2)={12*(n-2)}$ (1); one face: $6({n}-2)^2={6*(n-2)**2}$ (1); none: $({n}-2)^3={(n-2)**3}$ (1); total $=8+{12*(n-2)}+{6*(n-2)**2}+{(n-2)**3}={n**3}$ (1).", "1+1+1+1+1") for n in [9, 10, 12, 15, 20, 25]])

# ================= MEDIUM =================
m1 = [M4(f"A prism has {E} edges. The number of its faces is:", E // 3 + 2, [E // 3, E // 3 + 1, E // 3 + 3, E // 2], f"$n={E//3}$, faces $=n+2$") for E in [18, 24, 27, 30, 36]]
m2 = [M4(f"A pyramid has {V} vertices. The number of its edges is:", 2 * (V - 1), [V - 1, 2 * V, V + 1, 3 * (V - 1)], f"Base has $n={V-1}$ sides; edges $=2n$") for V in [7, 9, 11, 13, 16]]
m3 = [M4(f"All {F} faces of a polyhedron are triangles. The number of its edges is:", 3 * F // 2, [3 * F, F, 2 * F, 3 * F // 2 + 2], f"Each edge is shared by 2 faces: $E=3F/2$") for F in [8, 12, 14, 16, 20, 24]]
m4_ = [M4(f"A polyhedron has {F} faces and {E} edges. Its number of vertices is:", 2 + E - F, [E - F, F + E - 2, 2 + E + F], f"$V=2+E-F$") for F, E in [(12, 30), (32, 90), (14, 36), (20, 30), (26, 48)]]
m5 = [M4(f"A cube of side {n} cm is painted all over and cut into 1 cm cubes. The number of cubes with no face painted is:", (n - 2) ** 3, [(n - 2) ** 2, 6 * (n - 2) ** 2, n ** 3 - 8, (n - 1) ** 3], f"Inner cube of side ${n-2}$") for n in [4, 6, 8, 9, 11]]
m6 = [M4(f"A Koch curve starts with a line of length {L} cm. The total length after stage {n} (in cm) is:", g(koch_len(L, n)), [g(L * n), g(Fr(L * 4 * n, 3)), g(Fr(L * (3 ** n), 4 ** n))], f"Length multiplies by $\\frac43$ each stage: ${L}\\times(4/3)^{n}$") for L, n in [(27, 2), (81, 3), (189, 3), (36, 2), (162, 3)]]
m7 = [M4(f"The total number of triangles removed from the Sierpinski triangle up to stage {n} is:", (3 ** n - 1) // 2, [3 ** n - 1, 3 ** (n - 1), 3 ** n, (3 ** n - 1) // 2 + 3], f"$1+3+\\dots+3^{n-1}=(3^{n}-1)/2$") for n in [3, 4, 5, 6]]
MED_A = [m1, m2, m3, m4_, m5, m6, m7]
MED_B = ([Q(f"A cuboid is {l} cm long, {b} cm wide and {h} cm high. Find the sum of lengths of all its edges and the number of edges.", f"12 edges (1); sum $=4({l}+{b}+{h})={4*(l+b+h)}$ cm (1).", "1+1") for l, b, h in [(15, 9, 6), (14, 8, 5), (18, 11, 7), (20, 12, 9)]]
         + [Q(f"A prism has {3*n} edges. Find its number of faces and vertices.", f"$n={n}$ (1); faces ${n+2}$, vertices ${2*n}$ (1).", "1+1") for n in [12, 13, 15, 16]]
         + [Q(f"A Koch curve starts with a line of length {L} cm. Find the number of segments and the total length at stage 2.", f"Segments $=16$ (1); total $={g(koch_len(L,2))}$ cm (1).", "1+1") for L in [63, 72, 81, 90]])
MED_C = ([Q(f"A cube of side {n} cm is painted all over and cut into 1 cm cubes. Find the number of cubes with (i) exactly three painted faces (ii) no painted face (iii) at least one painted face.", f"(i) 8 (1); (ii) $({n}-2)^3={(n-2)**3}$ (1); (iii) ${n**3}-{(n-2)**3}={n**3-(n-2)**3}$ (1).", "1+1+1") for n in [4, 5, 6, 7, 9, 10]]
         + [Q(f"All {F} faces of a polyhedron are triangles. Find the number of edges and vertices.", f"$E=3F/2={3*F//2}$ (1); $V=2+E-F={2+3*F//2-F}$ (2).", "1+2") for F in [10, 18, 22, 26, 28, 30]]
         + [Q(f"A Sierpinski triangle starts with a triangle of area {A} cm². Find the shaded area and the number of shaded triangles at stage {n}.", f"Number $=3^{n}={3**n}$ (1); shaded area $={A}\\times(3/4)^{n}={g(Fr(A*3**n,4**n))}$ cm² (2).", "1+2") for A, n in [(128, 3), (320, 2), (1280, 4), (576, 2), (2048, 5), (4096, 3)] if (A * 3 ** n) % 4 ** n == 0])
MED_D = ([Q(f"A prism and a pyramid both have a {PN[n]} base. Find the difference between the number of (i) faces (ii) vertices (iii) edges of the prism and the pyramid.", f"Prism: ${n+2}$, ${2*n}$, ${3*n}$; pyramid: ${n+1}$, ${n+1}$, ${2*n}$ (2); differences: faces ${1}$ (1), vertices ${n-1}$ (1), edges ${n}$ (1).", "2+1+1+1") for n in [5, 6, 7, 8, 9, 10]]
          + [Q(f"A Koch snowflake is built from an equilateral triangle of side {s} cm. Find its perimeter at stage 0, stage 1 and stage 2.", f"Stage 0: $3\\times{s}={3*s}$ cm (1); stage 1: ${3*s}\\times\\frac43={g(Fr(12*s,3))}$ cm (2); stage 2: ${g(Fr(3*s*16,9))}$ cm (2).", "1+2+2") for s in [9, 18, 27, 36, 45, 54]])

# ================= HARD =================
h1 = [M4(f"All the {F} faces of a polyhedron are pentagons. Its number of vertices is:", 2 + 5 * F // 2 - F, [5 * F // 2, 5 * F // 2 - F, 2 + 5 * F // 2 + F, 2 + 5 * F // 2 - F + 2], f"$E=5F/2={5*F//2}$; $V=2+E-F$") for F in [12, 16, 20, 24]]
h2 = [M4(f"A polyhedron has {E} edges and exactly {k} edges meet at every vertex. Its number of faces is:", 2 + E - 2 * E // k, [E - 2 * E // k, 2 * E // k, 2 + E, 2 + E - 2 * E // k + 2], f"$V=2E/{k}={2*E//k}$; $F=2+E-V$") for E, k in [(18, 3), (30, 3), (24, 4), (12, 4), (36, 3), (60, 3)]]
h3 = [M4("If every corner of a cube is sliced off (without removing the whole edges), the number of vertices of the resulting solid is:", "24", ["8", "12", "16"], "Each corner is replaced by 3 new vertices: $8\\times3=24$"),
      M4("If every corner of a cube is sliced off, the number of faces of the resulting solid is:", "14", ["6", "8", "12"], "6 original faces + 8 new triangular faces"),
      M4("If every corner of a cube is sliced off, the number of edges of the resulting solid is:", "36", ["12", "24", "48"], "$F+V-2=14+24-2$"),
      M4("If one corner of a cube is sliced off, the number of vertices of the new solid is:", "10", ["8", "9", "11"], "Remove 1 vertex and add 3 new ones")]
h4 = [M4(f"A cube is painted all over and cut into unit cubes. If exactly {6*(n-2)**2} of the unit cubes have exactly one face painted, the side of the big cube is:", n, [n - 1, n + 1, n + 2], f"$6(n-2)^2={6*(n-2)**2}$ gives $n={n}$") for n in [4, 5, 7, 8]]
h5 = [M4(f"A Koch curve starts with a {L} cm line. The length of the curve at stage {n} (in cm) is:", I(koch_len(L, n)), [L * n, I(koch_len(L, n)) - 3 ** (n - 1), I(koch_len(L, n)) + L, I(koch_len(L, n - 1))], f"${L}\\times(4/3)^{n}$") for L, n in [(81, 4), (27, 3), (243, 5), (9, 2)]]
h6 = [M4(f"A Sierpinski triangle starts with a triangle of side {s} cm. At stage {n} the side of each small shaded triangle is (in cm):", g(Fr(s, 2 ** n)), [g(Fr(s, 3 ** n)), g(Fr(s, 2 * n)), g(Fr(s, 2 ** n) * 2)], f"Side halves every stage: ${s}/2^{n}$") for s, n in [(64, 4), (96, 3), (80, 4), (120, 3)]]
def poly_faces(a, b): return a + b, Fr(3 * a + 4 * b, 2)
h7 = [M4(f"A polyhedron has {a} triangular faces and {b} quadrilateral faces and no other faces. Its number of vertices is:", I(2 + poly_faces(a, b)[1] - (a + b)), [I(poly_faces(a, b)[1]), I(2 + poly_faces(a, b)[1] + a + b), a + b], f"$E=(3\\times{a}+4\\times{b})/2={I(poly_faces(a,b)[1])}$; $V=2+E-F$") for a, b in [(8, 2), (4, 2), (6, 3), (2, 3)] if (3 * a + 4 * b) % 2 == 0]
HARD_A = [h1, h2, h3, h4, h5, h6, h7]
HARD_B = ([Q(f"A cube is painted all over and cut into unit cubes. If {12*(n-2)} unit cubes have exactly two painted faces, find the side of the cube and the total number of unit cubes.", f"$12(n-2)={12*(n-2)}$ gives $n={n}$ (1); total $={n}^3={n**3}$ (1).", "1+1") for n in [6, 9, 10, 12]]
         + [Q(f"A polyhedron has {a} triangular faces and {b} square faces only. Find its number of edges.", f"Each edge is shared by two faces: $E=(3\\times{a}+4\\times{b})/2$ (1) $={I(poly_faces(a,b)[1])}$ (1).", "1+1") for a, b in [(8, 6), (20, 0), (12, 6), (6, 8)]]
         + [Q(f"A Sierpinski triangle starts with a triangle of side {s} cm. Find the number of shaded triangles and the side of each at stage {n}.", f"Number $=3^{n}={3**n}$ (1); side $={s}/2^{n}={g(Fr(s,2**n))}$ cm (1).", "1+1") for s, n in [(128, 5), (96, 5), (160, 4), (144, 4)]])
def first_stage(N):
    n = 0
    while 3 ** n <= N: n += 1
    return n
HARD_C = ([Q(f"Every face of a polyhedron is a triangle and it has {F} faces. Find the number of edges and vertices and verify Euler's formula.", f"$E=3F/2={3*F//2}$ (1); $V=2+E-F={2+3*F//2-F}$ (1); $F+V-E={F}+{2+3*F//2-F}-{3*F//2}=2$ (1).", "1+1+1") for F in [32, 40, 36, 44, 48, 52]]
         + [Q(f"A cube is painted all over and cut into unit cubes. For which side is the number of unit cubes with exactly two painted faces equal to {12*(n-2)}? Hence find the number with exactly one painted face.", f"$12(n-2)={12*(n-2)}$ gives $n={n}$ (1); one face: $6(n-2)^2=6\\times{(n-2)**2}={6*(n-2)**2}$ (2).", "1+2") for n in [14, 16, 18, 21, 24, 30]]
         + [Q(f"In the Sierpinski triangle construction, find the first stage at which the number of shaded triangles exceeds {N}. How many shaded triangles are there at that stage?", f"$3^{first_stage(N)-1}={3**(first_stage(N)-1)}\\le{N}$ but $3^{first_stage(N)}={3**first_stage(N)}>{N}$ (2); so stage {first_stage(N)} with ${3**first_stage(N)}$ triangles (1).", "2+1") for N in [500, 1000, 5000, 10000, 20000, 100000]])
HARD_D = ([Q(f"A polyhedron has {a} triangular faces and {b} quadrilateral faces and no other faces. Find the number of edges and vertices, and verify Euler's formula.", f"$F={a+b}$; $E=(3\\times{a}+4\\times{b})/2={I(poly_faces(a,b)[1])}$ (2); $V=2+E-F={I(2+poly_faces(a,b)[1]-a-b)}$ (2); $F+V-E=2$ (1).", "2+2+1") for a, b in [(10, 5), (12, 4), (14, 6), (16, 8), (18, 3), (6, 12)] if (3 * a + 4 * b) % 2 == 0]
          + [Q(f"A Koch snowflake is built from an equilateral triangle of side {s} cm. Find its perimeter at stage {n}, and by how much the perimeter has increased from stage 0.", f"Stage 0 perimeter $={3*s}$ cm (1); each stage multiplies the perimeter by $\\frac43$ (1); stage {n}: $3\\times{s}\\times(4/3)^{n}={g(3*koch_len(s,n))}$ cm (2); increase $={g(3*koch_len(s,n)-3*s)}$ cm (1).", "1+1+2+1") for s, n in [(27, 3), (9, 2), (81, 4), (18, 2), (54, 3), (36, 2)]])

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}
