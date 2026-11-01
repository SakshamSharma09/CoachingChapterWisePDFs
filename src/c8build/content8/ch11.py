from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
# A: counts in Sierpinski triangle (6)
for n, tri in [(1, 3), (2, 9), (3, 27), (4, 81), (5, 243), (6, 729)]:
    A.append(M4(f"In the Sierpinski triangle, the number of small shaded triangles after stage {n} is:", str(tri), [str(tri+3), str(tri-1), str(tri*2), str(tri+6), str(tri+1)], f"Each stage multiplies the count by 3: $3^{n}={tri}$"))
# A: faces/edges/vertices of solids (12)
solids = [("cube", 6, 12, 8), ("cuboid", 6, 12, 8), ("triangular prism", 5, 9, 6), ("square pyramid", 5, 8, 5), ("triangular pyramid (tetrahedron)", 4, 6, 4), ("pentagonal prism", 7, 15, 10)]
for nm, f, e, v in solids:
    A.append(M4(f"The number of faces of a {nm} is:", str(f), [str(f+1), str(f-1), str(f+2)], "Count the faces"))
    A.append(M4(f"The number of edges of a {nm} is:", str(e), [str(e+1), str(e-1), str(e+3)], "Count the edges"))
# A: Euler (4)
for nm, f, e, v in [("cube", 6, 12, 8), ("triangular prism", 5, 9, 6), ("square pyramid", 5, 8, 5), ("hexagonal prism", 8, 18, 12)]:
    A.append(M4(f"A solid has {f} faces and {v} vertices. Using $F+V-E=2$, the number of edges is:", str(e), [str(e+2), str(e-2), str(f+v), str(e+4), str(e-3)], "Euler's relation"))
# A: concepts (18)
A += [
 M4("A figure which has the same shape at every scale, repeating itself, is called a:", "fractal", ["polygon", "prism", "net"], "Self-similarity"),
 M4("The Koch snowflake is built by repeatedly adding triangles to:", "the middle third of each side", ["the vertices", "the interior", "the base only"], "Fractal construction"),
 M4("Each side of a Koch curve is replaced at each stage by how many segments?", "4", ["2", "3", "5"], "Four segments of one-third length"),
 M4("A two-dimensional pattern that can be folded to make a solid is its:", "net", ["shadow", "section", "projection"], "Net of a solid"),
 M4("The number of squares in the net of a cube is:", "6", ["4", "8", "12"], "6 faces"),
 M4("Which solid has a circular face and one vertex?", "cone", ["cylinder", "cuboid", "sphere"], "Cone"),
 M4("A cylinder has how many curved surfaces?", "1", ["2", "0", "3"], "Plus two circular faces"),
 M4("The faces of a prism that are not bases are called:", "lateral faces", ["edges", "vertices", "nets"], "Rectangles for a right prism"),
 M4("A pyramid with a square base has triangular faces numbering:", "4", ["2", "3", "5"], "One per base edge"),
 M4("If a cube is cut by a plane parallel to a face, the cross section is a:", "square", ["triangle", "circle", "hexagon"], "Same as a face"),
 M4("The top view of a cylinder standing on its base is a:", "circle", ["rectangle", "triangle", "square"], "Looking from above"),
 M4("Which is not a polyhedron?", "cylinder", ["cube", "prism", "pyramid"], "Has a curved surface"),
 M4("The side view of a cone is a:", "triangle", ["circle", "square", "rectangle"], "Looking from the side"),
 M4("The Sierpinski triangle is obtained by repeatedly removing:", "the central inverted triangle", ["one corner", "a vertex", "the base"], "Fractal"),
 M4("The number of vertices of a cuboid is:", "8", ["6", "12", "4"], "Corners"),
 M4("Which solid has all faces as congruent equilateral triangles?", "regular tetrahedron", ["cube", "square pyramid", "prism"], "Four faces"),
 M4("The relation between faces, vertices and edges of a polyhedron is:", "$F+V-E=2$", ["$F+V+E=2$", "$F-V+E=2$", "$F+E-V=0$"], "Euler's formula"),
 M4("A solid with two parallel congruent polygonal bases joined by rectangles is a:", "prism", ["pyramid", "cone", "sphere"], "Definition"),
]
assert len(A) == 40, len(A)
B = [
 Q("What is a fractal? Give an example.", "A pattern that repeats itself at smaller scales (1); Sierpinski triangle or Koch snowflake (1).", "1+1"),
 Q("How many triangles are shaded in stage 3 of the Sierpinski triangle?", "$3^3=27$ (2).", "2"),
 Q("What is a net of a solid? Draw the net of a cube in words.", "A flat pattern that folds into the solid (1); six squares joined (1).", "1+1"),
 Q("State the number of faces, edges and vertices of a cuboid.", "6, 12 and 8 (2).", "2"),
 Q("Verify Euler's formula for a triangular prism.", "$F=5,V=6,E=9$; $5+6-9=2$ (2).", "2"),
 Q("What is the top view of a cone placed on its base?", "A circle with a dot (centre) (2).", "2"),
 Q("Name the solid whose net has two circles and one rectangle.", "A cylinder (2).", "2"),
 Q("How many faces does a square pyramid have? Name their shapes.", "5: one square and four triangles (2).", "2"),
 Q("What is self-similarity?", "A part of the figure looks like the whole figure (2).", "2"),
 Q("In the Koch curve, how does the length of each stage change?", "It becomes $\\frac43$ times the previous length (2).", "2"),
 Q("Name the cross-section when a cylinder is cut parallel to its base.", "A circle (2).", "2"),
 Q("A cube has edge 4 cm. Find the total length of all its edges.", "$12\\times4=48$ cm (2).", "2"),
 Q("How many edges does a pentagonal pyramid have?", "10 (2).", "2"),
 Q("State two real-life examples of fractals found in nature.", "Fern leaf, broccoli, river networks, snowflakes (1+1).", "1+1"),
 Q("Which solid has no vertex and no edge?", "Sphere (2).", "2"),
 Q("Name the front view of a cube.", "A square (2).", "2"),
]
for n in range(1, 7):
    C.append(Q(f"A Sierpinski triangle starts with one shaded triangle of side 1 unit. After stage {n}, find the number of shaded triangles and the side of each.", f"Number $=3^{n}={3**n}$ (2); side $=\\dfrac1{{2^{n}}}$ unit (1).", "2+1"))
for nm, f, e, v in [("hexagonal prism", 8, 18, 12), ("octagonal pyramid", 9, 16, 9), ("hexagonal pyramid", 7, 12, 7), ("pentagonal prism", 7, 15, 10), ("triangular pyramid", 4, 6, 4), ("octagonal prism", 10, 24, 16)]:
    C.append(Q(f"Find the faces, edges and vertices of a {nm} and verify Euler's formula.", f"$F={f}$, $E={e}$, $V={v}$ (2); $F+V-E={f+v-e}=2$ (1).", "2+1"))
for s in [2, 3, 5, 6]:
    C.append(Q(f"A cube has edge {s} cm. Find its surface area and the number of such cubes needed to make a cuboid of dimensions ${2*s}\\times{s}\\times{s}$.", f"Surface area $=6\\times{s}^2={6*s*s}$ cm² (2); 2 cubes (1).", "2+1"))
C += [
 Q("Draw the nets of a cube and a cuboid. Mention one difference.", "Cube net has six equal squares; cuboid net has rectangles of three pairs (3).", "3"),
 Q("Describe the Koch snowflake construction in three steps.", "Start with an equilateral triangle (1); divide each side into three equal parts and add a small triangle on the middle part (1); repeat on every new side (1).", "1+1+1"),
]
C += [
 Q("How many edges are there in a Koch curve after stage 3 if stage 0 is one segment?", "Segments multiply by 4 each stage (1); $4^3=64$ segments (2).", "1+2"),
 Q("A cube of edge 3 cm is painted and cut into 27 unit cubes. How many cubes have exactly two faces painted?", "12 edge cubes (3).", "3"),
 Q("A cuboid has dimensions 8 cm × 5 cm × 3 cm. Find its total surface area.", "$2(40+24+15)=158$ cm² (3).", "3"),
 Q("Why can a regular pyramid with base 7 sides have 8 faces?", "One base and seven triangles (3).", "3"),
 Q("Match each solid with its top view: cube, cylinder, cone, square pyramid.", "Square, circle, circle with centre, square with diagonals (3).", "3"),
 Q("State two uses of nets in everyday life.", "Packaging boxes, paper models and gift boxes (1.5); designing 3D objects from flat sheets (1.5).", "1½+1½"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Explain how to construct the Sierpinski triangle. (ii) Count the shaded triangles in the first four stages. (iii) What pattern do you see?", "(i) Remove the central inverted triangle from each triangle repeatedly (2). (ii) 1, 3, 9, 27 (1.5). (iii) Multiplied by 3 each stage (1.5).", "2+1½+1½"),
 Q("(i) Define a polyhedron. (ii) Verify Euler's formula for a cube and a square pyramid.", "(i) A solid bounded by plane polygonal faces (2). (ii) $6+8-12=2$; $5+5-8=2$ (3).", "2+3"),
 Q("<b>Case study:</b> A box maker needs a net for a cuboid box 10 cm × 6 cm × 4 cm. (i) List the sizes of the six rectangles. (ii) Find the total area of cardboard. (iii) Why will flaps need extra?", "(i) 10×6 (2), 10×4 (2), 6×4 (2) (2). (ii) $2(60+40+24)=248$ cm² (2). (iii) For gluing (1).", "2+2+1"),
 Q("(i) State the steps to draw the Koch snowflake. (ii) If the original side is 9 cm, find the side length and number of sides after stage 2.", "(i) Replace the middle third of each side by two segments forming a triangle (3). (ii) Side 1 cm, sides $3\\times4\\times4=48$ (2).", "3+2"),
 Q("(i) Draw the top, front and side views of a cylinder lying on its curved surface. (ii) Name each view.", "(i) Top: rectangle; front: rectangle; side: circle (3). (ii) Identification (2).", "3+2"),
 Q("<b>Case study:</b> A cone-shaped party hat is made from a sector of a circle. (i) Name the solid. (ii) Number of faces and edges. (iii) What is the net?", "(i) Cone (1). (ii) 2 faces (one curved, one flat), 1 edge (2). (iii) A sector and a circle (2).", "1+2+2"),
 Q("(i) How many cubes of edge 1 cm fit in a cuboid of 5 × 4 × 3 cm? (ii) Count the number of cubes on the surface.", "(i) 60 (2). (ii) Inside cubes $3\\times2\\times1=6$; surface $=54$ (3).", "2+3"),
 Q("(i) What is the cross section of a cube cut diagonally through two opposite edges? (ii) Of a cone cut parallel to the base?", "(i) A rectangle (3). (ii) A circle (2).", "3+2"),
 Q("<b>Case study:</b> A school logo uses Sierpinski triangles with side 16 cm. (i) After stage 3, what is the side of the smallest white triangle? (ii) Count the shaded ones. (iii) Total shaded area fraction.", "(i) 2 cm (2). (ii) 27 (1). (iii) $(3/4)^3=27/64$ (2).", "2+1+2"),
 Q("(i) A prism has 12 vertices. Name it and find its faces and edges. (ii) Verify Euler's formula.", "(i) Hexagonal prism, 8 faces, 18 edges (3). (ii) $8+12-18=2$ (2).", "3+2"),
 Q("(i) Why do prisms and pyramids differ in nets? (ii) Draw the net of a triangular pyramid in words.", "(i) Prisms have two bases and rectangles; pyramids one base and triangles (3). (ii) Four triangles, one central (2).", "3+2"),
 Q("<b>Case study:</b> Packaging for a chocolate is a triangular prism with equilateral triangle base of side 4 cm and length 20 cm. (i) Number of faces, edges, vertices. (ii) Sum of lengths of all edges. (iii) Shape of the front view.", "(i) 5, 9, 6 (2). (ii) $6\\times4+3\\times20=84$ cm (2). (iii) Triangle (1).", "2+2+1"),
 Q("(i) Find the number of small cubes in a $4\\times4\\times4$ cube painted outside. (ii) How many have 3 faces painted?", "(i) 64 (2). (ii) 8 corner cubes (3).", "2+3"),
 Q("(i) A polyhedron has 6 faces and 12 edges. Find its vertices using Euler's formula. (ii) Name two such solids.", "(i) $V=2-F+E=8$ (3). (ii) Cube and cuboid (2).", "3+2"),
 Q("(i) How do fractals appear in nature and art? (ii) Give two examples.", "(i) Repeating patterns at all scales (3). (ii) Fern leaf, Romanesco broccoli, kolam designs (2).", "3+2"),
 Q("<b>Case study:</b> An architect draws a plan of a pyramid-shaped monument. (i) Name its faces. (ii) The base is a square of side 40 m, height 30 m; find the slant height. (iii) Find the area of one triangular face.", "(i) 4 triangles and 1 square (1). (ii) $\\sqrt{20^2+30^2}=\\sqrt{1300}\\approx36$ m (2). (iii) $\\tfrac12\\times40\\times36\\approx720$ m² (2).", "1+2+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
