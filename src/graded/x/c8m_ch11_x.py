"""Class 8 Maths Ch 11 Exploring Some Geometric Themes - extras."""
from common import AR4, Q

AR = [
 AR4(r"A cube satisfies Euler's formula.", r"For every convex polyhedron, $F+V-E=2$.", "a",
     r"A cube has $F=6$, $V=8$, $E=12$ and $6+8-12=2$; R is the general result."),
 AR4(r"A triangular prism has 5 faces.", r"A pyramid with an $n$-sided base has $n+1$ faces.", "b",
     r"A triangular prism has 2 triangular and 3 rectangular faces, so A is true; R is true but about pyramids, so it does not explain A."),
 AR4(r"A hexagonal prism has 18 edges.", r"A hexagonal prism has 6 vertices.", "c",
     r"Edges $=3\times6=18$ so A is true; a hexagonal prism has 12 vertices, so R is false."),
 AR4(r"A square pyramid has 6 vertices.", r"A square pyramid has 8 edges.", "d",
     r"A square pyramid has 5 vertices (4 base + 1 apex), so A is false; it has 8 edges, so R is true."),
 AR4(r"A polyhedron with 10 vertices and 15 edges has 7 faces.", r"For a polyhedron, $F=2-V+E$.", "a",
     r"$F=2-10+15=7$; R is Euler's formula rearranged."),
 AR4(r"When a $3\times3\times3$ cube painted on all faces is cut into 27 unit cubes, exactly one small cube has no painted face.", r"Eight of the 27 small cubes have exactly three painted faces.", "b",
     r"The unit cube at the centre is unpainted, so A is true; the 8 corner cubes have three painted faces so R is true; R does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Rohan makes solid models of a pentagonal prism and a pentagonal pyramid for a school exhibition and counts their faces, vertices and edges. "
   r"(i) How many faces does the pentagonal prism have? (ii) How many vertices does it have? (iii) How many edges does it have? (iv) Verify Euler's formula for the prism and for the pentagonal pyramid.",
   r"(i) $5+2=7$ (1). (ii) $2\times5=10$ (1). (iii) $3\times5=15$ (1). (iv) Prism: $F+V-E=7+10-15=2$ (1). Pyramid: $F=6$, $V=6$, $E=10$ and $6+6-10=2$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A $4\times4\times4$ wooden cube is painted red on all its faces and then cut into 64 identical small cubes. "
   r"(i) How many small cubes have exactly three painted faces? (ii) How many have exactly two painted faces? (iii) How many have exactly one painted face? (iv) How many have no painted face? Show that the four counts add up to 64.",
   r"(i) 8 corner cubes (1). (ii) $12\times(4-2)=24$ (1). (iii) $6\times(4-2)^2=24$ (1). (iv) $(4-2)^3=8$ (1); $8+24+24+8=64$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A teacher draws a Sierpinski triangle. Start with a solid triangle; at stage 1 the middle triangle is removed leaving 3 triangles. At each next stage the middle part of every remaining triangle is removed in the same way. "
   r"(i) How many triangles remain at stage 1? (ii) How many remain at stage 2? (iii) How many remain at stage 3? (iv) Write the number at stage $n$ and find it at stage 5.",
   r"(i) 3 (1). (ii) $3\times3=9$ (1). (iii) 27 (1). (iv) Each stage multiplies the count by 3, so the number is $3^n$ (1); at stage 5: $3^5=243$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Polyhedra", [
   r"A polyhedron has faces (flat polygons), edges (where two faces meet) and vertices (corners).",
   r"Euler's formula: $F+V-E=2$ for convex polyhedra.",
   r"Prism with $n$-sided base: $F=n+2$, $V=2n$, $E=3n$.",
   r"Pyramid with $n$-sided base: $F=n+1$, $V=n+1$, $E=2n$."]),
 ("Nets", [
   r"A net is a flat pattern that folds into a solid; a cube has 11 different nets of 6 squares.",
   r"Number of faces of the solid $=$ number of polygons in its net."]),
 ("Painted cube ($n\\times n\\times n$ cut into $n^3$ unit cubes, $n\\ge2$)", [
   r"3 faces painted: 8 (corners). 2 faces painted: $12(n-2)$.",
   r"1 face painted: $6(n-2)^2$. No face painted: $(n-2)^3$."]),
 ("Fractals", [
   r"A fractal is a pattern that repeats itself at smaller and smaller scales (self-similar).",
   r"Sierpinski triangle: the number of triangles multiplies by 3 at each stage, giving $3^n$ at stage $n$.",
   r"Koch snowflake: each stage replaces every side by 4 segments of one-third the length."]),
]

MISTAKES = [
 r"Counting faces, edges and vertices of a prism and pyramid with each other's formulas (a pyramid has $2n$ edges, a prism $3n$).",
 r"Forgetting the apex when counting the vertices of a pyramid (a square pyramid has 5, not 4).",
 r"In painted-cube questions, using $n-2$ for the edge cubes but forgetting to multiply by the number of edges (12) or faces (6).",
 r"Assuming that any six squares joined edge to edge fold into a cube; the net must not overlap when folded.",
 r"Using Euler's formula as $F+V+E=2$; the correct form is $F+V-E=2$.",
 r"Counting the stages of a fractal wrongly: the starting figure is stage 0, not stage 1.",
]
