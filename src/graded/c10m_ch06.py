"""Class 10 Maths Ch 6 - Triangles (graded banks). Text-only geometry (no figures needed)."""
from mg import *

SLUG, NAME, CHNO = "Triangles", "Triangles", 6

TR = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (6, 8, 10), (9, 12, 15), (12, 16, 20), (15, 20, 25), (12, 35, 37), (16, 30, 34)]
DEF = "In $\\triangle ABC$, $D$ and $E$ lie on $AB$ and $AC$ with $DE\\parallel BC$."

def BPT(x, y, k):
    return Q(f"{DEF} If $AD={x}$ cm, $DB={y}$ cm and $AE={k*x}$ cm, find $EC$.", f"By the Basic Proportionality Theorem, $\\dfrac{{AD}}{{DB}}=\\dfrac{{AE}}{{EC}}$ (1); $\\dfrac{{{x}}}{{{y}}}=\\dfrac{{{k*x}}}{{EC}}$ (1); $EC={k*y}$ cm (1).", "1+1+1")
def BPT2(x, y, k):
    return Q(f"{DEF} If $AB={x+y}$ cm, $AD={x}$ cm and $AC={k*(x+y)}$ cm, find $AE$ and $EC$.", f"$\\dfrac{{AD}}{{AB}}=\\dfrac{{AE}}{{AC}}$ (1); $AE=\\dfrac{{{x}\\times{k*(x+y)}}}{{{x+y}}}={k*x}$ cm (1); $EC={k*(x+y)}-{k*x}={k*y}$ cm (1).", "1+1+1")
def PYTH(a, b, c):
    return Q(f"In a right triangle the two perpendicular sides are {a} cm and {b} cm. Find the hypotenuse and the perimeter.", f"$h^2={a}^2+{b}^2={a*a+b*b}$ (1); $h={c}$ cm (1); perimeter $={a+b+c}$ cm (1).", "1+1+1")
def LADDER(a, b, c):
    return Q(f"A ladder {c} m long reaches a window {b} m above the ground. Find the distance of the foot of the ladder from the wall.", f"Ladder is the hypotenuse of a right triangle (1); $d^2={c}^2-{b}^2={c*c-b*b}$ (1); $d={a}$ m (1).", "1+1+1")
def AREAR(s1, s2, A1):
    A2 = F(A1 * s2 * s2, s1 * s1)
    return Q(f"The areas of two similar triangles are ${t(A1)}$ cm² and ${t(A2)}$ cm². If a side of the first is {s1} cm, find the corresponding side of the second.", f"Ratio of areas $=$ (ratio of sides)$^2$ (1); $\\dfrac{{{t(A1)}}}{{{t(A2)}}}=\\dfrac{{{s1}^2}}{{x^2}}$ (1); $x={s2}$ cm (1).", "1+1+1")
def SHADOW(h, s, S):
    H = F(h * S, s)
    return Q(f"A pole {h} m high casts a shadow {s} m long. At the same time a tower casts a shadow {S} m long. Find the height of the tower.", f"The triangles formed are similar (AA) (1); $\\dfrac{{H}}{{{h}}}=\\dfrac{{{S}}}{{{s}}}$ (1); $H={t(H)}$ m (1).", "1+1+1")
def ISRT(a, b, c):
    ok = a * a + b * b == c * c
    return Q(f"The sides of a triangle are {a} cm, {b} cm and {c} cm. Is it a right triangle? If so, name the right angle.", f"Largest side {max(a,b,c)}: $({max(a,b,c)})^2={max(a,b,c)**2}$ (1); sum of squares of the others $={a*a+b*b+c*c-max(a,b,c)**2}$ (1); " + ("equal, so by the converse of Pythagoras it is right-angled at the vertex opposite the longest side (1)." if ok else "not equal, so it is not right-angled (1)."), "1+1+1")
def ALT(p, q, k):
    h = k * p
    return Q(f"In a right triangle, the altitude to the hypotenuse divides it into segments of {p} cm and {p*k*k} cm. Find the length of the altitude.", f"Altitude$^2=$ product of the segments (1); $h^2={p}\\times{p*k*k}={p*p*k*k}$ (1); $h={h}$ cm (1).", "1+1+1") if False else \
        Q(f"In a right triangle, the altitude to the hypotenuse divides it into segments of {p} cm and {q} cm. Find the altitude.", f"Altitude$^2=$ product of the segments (1); $h^2={p}\\times{q}={p*q}$ (1); $h={isqrt(p*q)}$ cm (1).", "1+1+1")
def SMALLTRI(m, n):
    return Q(f"In $\\triangle ABC$, $DE\\parallel BC$ with $AD:DB={m}:{n}$. Find the ratio of the area of $\\triangle ADE$ to that of $\\triangle ABC$, and to that of trapezium $DBCE$.", f"$\\triangle ADE\\sim\\triangle ABC$, $AD:AB={m}:{m+n}$ (1); area ratio $={m*m}:{(m+n)**2}$ (2); trapezium area $={(m+n)**2-m*m}$ parts, so $\\triangle ADE:DBCE={m*m}:{(m+n)**2-m*m}$ (2).", "1+2+2")
def PERIM(r, p1, a):
    return Q(f"Two similar triangles have perimeters {p1} cm and {p1*r} cm. If a side of the smaller is {a} cm, find the corresponding side of the larger and the ratio of their areas.", f"Ratio of sides $=$ ratio of perimeters $=1:{r}$ (1); side $={a*r}$ cm (1); ratio of areas $=1:{r*r}$ (1).", "1+1+1")
def RHOM(a, b):
    s = F(a * a + b * b, 4)
    return Q(f"The diagonals of a rhombus are {2*a} cm and {2*b} cm. Find its side." , f"Diagonals bisect at right angles: half-diagonals {a} and {b} (1); $s^2={a}^2+{b}^2={a*a+b*b}$ (1); side $=\\sqrt{{{a*a+b*b}}}$ cm (1).", "1+1+1")
def POLES(a, b, d):
    return Q(f"Two poles of heights {a} m and {b} m stand on level ground {d} m apart. Find the distance between their tops.", f"Draw a horizontal line from the top of the shorter pole: right triangle with legs ${d}$ and ${abs(a-b)}$ (2); $x^2={d*d}+{(a-b)**2}$ (1); $x={t(sqrt(d*d+(a-b)**2))}$ m (2).", "2+1+2")
def SIMSIDES(a, b, c, k):
    return Q(f"$\\triangle ABC\\sim\\triangle PQR$ with $AB={a}$ cm, $BC={b}$ cm, $CA={c}$ cm and $PQ={a*k}$ cm. Find $QR$, $RP$ and the ratio of perimeters.", f"$\\dfrac{{PQ}}{{AB}}=\\dfrac{{QR}}{{BC}}=\\dfrac{{RP}}{{CA}}={k}$ (1); $QR={b*k}$ cm, $RP={c*k}$ cm (2); perimeter ratio $=1:{k}$ (1).", "1+1+1+1") if False else \
        Q(f"$\\triangle ABC\\sim\\triangle PQR$ with $AB={a}$ cm, $BC={b}$ cm, $CA={c}$ cm and $PQ={a*k}$ cm. Find $QR$ and $RP$.", f"$\\dfrac{{PQ}}{{AB}}=\\dfrac{{QR}}{{BC}}=\\dfrac{{RP}}{{CA}}={k}$ (1); $QR={b*k}$ cm (1); $RP={c*k}$ cm (1).", "1+1+1")
def MIDQ(x):
    return Q(f"In $\\triangle ABC$, $D$ and $E$ are the midpoints of $AB$ and $AC$ and $BC={2*x}$ cm. Find $DE$ and the ratio of areas of $\\triangle ADE$ and $\\triangle ABC$.", f"Midpoint theorem: $DE\\parallel BC$, $DE=\\frac12BC={x}$ cm (2); areas in ratio $(1/2)^2=1:4$ (1).", "2+1")

# ---------------- EASY ----------------
eA = [[MN(f"In a right triangle with legs {a} and {b}, the hypotenuse is:", c, why=f"$\\sqrt{{{a}^2+{b}^2}}={c}$") for a, b, c in TR[:5]],
      [MS("If $\\triangle ABC\\sim\\triangle DEF$, then $\\dfrac{AB}{DE}=$", "$\\dfrac{BC}{EF}$", ["$\\dfrac{BC}{DF}$", "$\\dfrac{AC}{EF}$", "$\\dfrac{AB}{EF}$"], "Corresponding sides are proportional") for _ in range(5)] if False else
      [MN(f"The ratio of corresponding sides of two similar triangles is {a}:{b}. Their perimeters are in the ratio {a}:", b, why="Perimeter ratio = side ratio") for a, b in [(1, 3), (2, 5), (3, 4), (4, 7), (5, 6)]],
      [MN(f"In $\\triangle ABC$, $DE\\parallel BC$, $AD={x}$, $DB={y}$, $AE={k*x}$. Then $EC=$", k * y, why="$\\frac{AD}{DB}=\\frac{AE}{EC}$") for x, y, k in [(2, 3, 2), (3, 4, 2), (1, 5, 3), (4, 3, 2), (2, 7, 2)]],
      [MN(f"The areas of two similar triangles are in the ratio {a*a}:{b*b}. The ratio of their corresponding sides is {a}:", b, why="Side ratio is the square root of the area ratio") for a, b in [(2, 3), (3, 5), (1, 4), (4, 5), (2, 7)]],
      [MN(f"The diagonal of a rectangle with sides {a} and {b} is:", c, why="Pythagoras") for a, b, c in TR[:5]],
      [MS("Two triangles are similar if their corresponding angles are:", "equal", ["supplementary", "complementary", "in ratio 1:2"], "AAA similarity") for _ in range(1)] + [MS(f"A triangle has sides {a}, {b}, {c}. It is right-angled if:", f"${a}^2+{b}^2={c}^2$", [f"${a}+{b}={c}$", f"${a}^2={b}^2+{c}^2$", f"${a}\\times{b}={c}$"], "Converse of Pythagoras") for a, b, c in TR[:4]]]
eB = ([Q(f"Find the hypotenuse of a right triangle with legs {a} cm and {b} cm.", f"$h^2={a*a}+{b*b}={c*c}$ (1); $h={c}$ cm (1).", "1+1") for a, b, c in TR[6:10]]
      + [Q(f"The sides of two similar triangles are in the ratio {a}:{b}. Find the ratio of their areas.", f"Area ratio $=({a}/{b})^2$ (1) $={a*a}:{b*b}$ (1).", "1+1") for a, b in [(2, 3), (3, 4), (5, 2), (4, 7)]]
      + [Q(f"In $\\triangle ABC$, $DE\\parallel BC$, $AD={x}$ cm, $DB={y}$ cm, $AE={x*2}$ cm. Find $EC$.", f"$\\frac{{AD}}{{DB}}=\\frac{{AE}}{{EC}}$ (1); $EC={2*y}$ cm (1).", "1+1") for x, y in [(3, 4), (2, 5), (4, 3), (5, 6)]])
eC = ([PYTH(a, b, c) for a, b, c in TR[:6]] + [BPT(x, y, k) for x, y, k in [(2, 3, 2), (3, 5, 2), (4, 5, 3), (1, 4, 4), (5, 2, 2), (3, 7, 3)]]
      + [ISRT(*p) for p in [(6, 8, 10), (5, 7, 9), (9, 40, 41), (10, 24, 26), (4, 6, 8), (12, 35, 37)]])
eD = ([LADDER(a, b, c) for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (9, 12, 15), (12, 16, 20)]]
      + [SHADOW(h, s, S) for h, s, S in [(6, 4, 30), (5, 3, 21), (8, 5, 35), (4, 3, 27), (7, 2, 18), (3, 2, 20)]])

# ---------------- NCERT ----------------
nA = [[MN(f"In $\\triangle ABC$, $DE\\parallel BC$, $AD={x}$ cm, $DB={y}$ cm, $AE={k*x}$ cm. Then $EC$ (in cm) $=$", k * y, why="BPT") for x, y, k in [(1, 1.5 if False else 3, 2), (3, 6, 2), (5, 4, 3), (2, 9, 4), (6, 5, 2)]],
      [MN(f"$\\triangle ABC\\sim\\triangle DEF$ with areas {a*a*k} cm² and {b*b*k} cm². If $AB={a*3}$ cm, then $DE$ (cm) $=$", b * 3, why="Sides in ratio $\\sqrt{\\text{areas}}$") for a, b, k in [(2, 3, 4), (3, 4, 2), (1, 2, 9), (2, 5, 3), (3, 5, 1)]],
      [MN(f"The length of the diagonal of a square of side {s} cm, squared, is:", 2 * s * s, why="$d^2=s^2+s^2$") for s in [3, 5, 6, 8, 9]],
      [MN(f"A man goes {a} m due east and then {b} m due north. His distance from the start (m) is:", c, why="Pythagoras") for a, b, c in [(15, 20, 25), (24, 32, 40), (9, 12, 15), (30, 40, 50), (21, 28, 35)]],
      [MS(f"In $\\triangle ABC$, $AB={a}$, $BC={b}$, $AC={c}$. The triangle is:", "right-angled" if a * a + b * b == c * c else "not right-angled", ["not right-angled" if a * a + b * b == c * c else "right-angled", "equilateral", "isosceles right"], f"Check ${a}^2+{b}^2$ against ${c}^2$") for a, b, c in [(9, 12, 15), (7, 8, 10), (8, 15, 17), (10, 11, 15), (20, 48, 52)]],
      [MN(f"In $\\triangle ABC$, $DE\\parallel BC$ and $AD:DB={m}:{n}$. Then $AE:AC$ is {m}:", m + n, why="$\\frac{AE}{AC}=\\frac{AD}{AB}$") for m, n in [(2, 3), (3, 5), (1, 4), (4, 3), (5, 2)]]]
nB = ([Q(f"A ladder {c} m long reaches a window {b} m high. Find how far the foot of the ladder is from the wall.", f"$d^2={c*c}-{b*b}={a*a}$ (1); $d={a}$ m (1).", "1+1") for a, b, c in TR[2:6]]
      + [Q(f"Sides of a triangle are {a} cm, {b} cm, {c} cm. State with reason whether it is right-angled.", f"${max(a,b,c)}^2={max(a,b,c)**2}$; sum of squares of others $={a*a+b*b+c*c-max(a,b,c)**2}$ (1); " + ("equal, so right-angled (1)." if a * a + b * b == c * c else "not equal, so not right-angled (1)."), "1+1") for a, b, c in [(7, 24, 25), (6, 7, 10), (13, 84, 85), (9, 10, 14)]]
      + [Q(f"The perimeters of two similar triangles are {p} cm and {p*r} cm. Find the ratio of their corresponding sides and their areas.", f"Side ratio $=1:{r}$ (1); area ratio $=1:{r*r}$ (1).", "1+1") for p, r in [(20, 2), (24, 3), (15, 4), (18, 5)]])
nC = ([BPT(x, y, k) for x, y, k in [(4, 6, 3), (5, 3, 2), (2, 7, 5), (6, 4, 2), (3, 8, 3), (7, 2, 2)]] + [AREAR(*p) for p in [(4, 6, 16), (3, 9, 18), (5, 8, 25), (6, 10, 24), (2, 7, 12), (9, 12, 54)]]
      + [SMALLTRI(m, n) for m, n in [(1, 2), (2, 3), (1, 3), (3, 4), (2, 5), (3, 2)]])
nD = ([Q("Prove that if a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.", "Given $\\triangle ABC$, $DE\\parallel BC$; join $BE$, $CD$ and draw $EM\\perp AB$, $DN\\perp AC$ (1); $\\frac{ar(ADE)}{ar(BDE)}=\\frac{\\frac12AD\\cdot EM}{\\frac12DB\\cdot EM}=\\frac{AD}{DB}$ and $\\frac{ar(ADE)}{ar(CDE)}=\\frac{AE}{EC}$ (2); $ar(BDE)=ar(CDE)$ (same base $DE$, same parallels) (1); hence $\\frac{AD}{DB}=\\frac{AE}{EC}$ (1).", "1+2+1+1"),
       Q("State and prove the converse of the Basic Proportionality Theorem.", "If $\\frac{AD}{DB}=\\frac{AE}{EC}$, then $DE\\parallel BC$ (1). Suppose not; draw $DE'\\parallel BC$ meeting $AC$ at $E'$ (1); by BPT $\\frac{AD}{DB}=\\frac{AE'}{E'C}$ (1); so $\\frac{AE}{EC}=\\frac{AE'}{E'C}$, hence $E=E'$ (1); thus $DE\\parallel BC$ (1).", "1+1+1+1+1"),
       Q("Prove that the ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding sides.", "Let $\\triangle ABC\\sim\\triangle PQR$; draw altitudes $AM$ and $PN$ (1); $\\frac{ar(ABC)}{ar(PQR)}=\\frac{BC\\cdot AM}{QR\\cdot PN}$ (1); $\\triangle ABM\\sim\\triangle PQN$ gives $\\frac{AM}{PN}=\\frac{AB}{PQ}$ (1); with $\\frac{AB}{PQ}=\\frac{BC}{QR}$ get $\\left(\\frac{AB}{PQ}\\right)^2$, and equal to $\\left(\\frac{BC}{QR}\\right)^2=\\left(\\frac{CA}{RP}\\right)^2$ (2).", "1+1+1+2"),
       Q("Prove that in a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides.", "Let $\\angle B=90^\\circ$; draw $BD\\perp AC$ (1); $\\triangle ADB\\sim\\triangle ABC$ gives $AB^2=AD\\cdot AC$ (1); $\\triangle BDC\\sim\\triangle ABC$ gives $BC^2=CD\\cdot AC$ (1); adding, $AB^2+BC^2=AC(AD+DC)=AC^2$ (2).", "1+1+1+2"),
       Q("Prove that if the square of one side of a triangle equals the sum of the squares of the other two sides, the angle opposite the first side is a right angle.", "Given $AC^2=AB^2+BC^2$ (1); construct $\\triangle PQR$ with $\\angle Q=90^\\circ$, $PQ=AB$, $QR=BC$ (1); $PR^2=PQ^2+QR^2=AB^2+BC^2=AC^2$, so $PR=AC$ (1); $\\triangle ABC\\cong\\triangle PQR$ (SSS), hence $\\angle B=\\angle Q=90^\\circ$ (2).", "1+1+1+2"),
       Q("Prove that the line joining the midpoints of two sides of a triangle is parallel to the third side.", "$D,E$ midpoints of $AB,AC$ (1); $\\frac{AD}{DB}=1=\\frac{AE}{EC}$ (2); by the converse of BPT, $DE\\parallel BC$ (2).", "1+2+2")]
      + [PERIM(r, p, a) for r, p, a in [(2, 18, 5), (3, 20, 6), (4, 15, 4), (5, 12, 3), (2, 30, 8), (3, 24, 7)]])

# ---------------- MEDIUM ----------------
mA = [[MN(f"If $DE\\parallel BC$ in $\\triangle ABC$, $AB={x+y}$ cm, $AD={x}$ cm, $AC={k*(x+y)}$ cm, then $EC$ (cm) is:", k * y, why="$AE=k\\times AD$") for x, y, k in [(3, 2, 2), (4, 3, 3), (2, 6, 2), (5, 4, 2), (3, 9, 3)]],
      [MN(f"The areas of two similar triangles are {a*a*k} cm² and {b*b*k} cm². The ratio of their perimeters is {a}:", b, why="Perimeter ratio = side ratio") for a, b, k in [(3, 5, 4), (2, 7, 9), (4, 9, 1), (5, 6, 2), (1, 8, 3)]],
      [MN(f"The altitude to the hypotenuse of a right triangle divides it into {p} cm and {q} cm. The altitude (cm) is:", isqrt(p * q), why="$h^2=pq$") for p, q in [(4, 9), (3, 12), (2, 18), (5, 20), (8, 18)]],
      [MN(f"A pole {h} m high casts a shadow {s} m long. A tower casting a shadow {S} m has height (m):", F(h * S, s), why="Similar triangles") for h, s, S in [(6, 4, 24), (8, 5, 40), (10, 6, 54), (3, 2, 30), (12, 7, 35)]],
      [MN(f"The diagonals of a rhombus are {2*a} and {2*b}. Its side squared is:", a * a + b * b, why="Half-diagonals are legs") for a, b in [(6, 8), (5, 12), (9, 12), (8, 15), (7, 24)]],
      [MN(f"Two poles of heights {a} m and {b} m are {d} m apart. The distance between their tops (m) is:", c, why="Right triangle with legs $d$ and $a-b$") for a, b, d, c in [(13, 8, 12, 13), (20, 14, 8, 10), (30, 6, 7, 25), (17, 9, 15, 17), (25, 5, 21, 29)]]]
mB = ([BPT2(x, y, k) for x, y, k in [(3, 2, 2), (4, 6, 2), (2, 3, 3), (5, 5, 2)]] + [PERIM(r, p, a) for r, p, a in [(2, 21, 4), (3, 16, 5), (4, 10, 3), (5, 14, 2)]]
      + [MIDQ(x) for x in [4, 6, 9, 11]])
mC = ([BPT2(x, y, k) for x, y, k in [(4, 5, 2), (2, 7, 3), (6, 3, 2), (5, 8, 2), (3, 10, 3), (7, 4, 2)]] + [SIMSIDES(a, b, c, k) for a, b, c, k in [(3, 4, 5, 2), (5, 6, 7, 3), (4, 7, 8, 2), (6, 8, 10, 4), (5, 9, 12, 3), (7, 10, 11, 2)]]
      + [ALT(p, q, 0) for p, q in [(4, 9), (2, 8), (3, 27), (5, 20), (8, 18), (9, 16)]])
mD = ([POLES(a, b, d) for a, b, d in [(14, 2, 9), (20, 8, 16), (18, 6, 5), (25, 9, 12), (16, 4, 35), (11, 3, 15)]] + [RHOM(a, b) for a, b in [(6, 8), (5, 12), (9, 12), (8, 15), (12, 16), (7, 24)]])

# ---------------- HARD ----------------
hA = [[MN(f"In $\\triangle ABC$, $DE\\parallel BC$ and $AD:DB={m}:{n}$. The ratio of areas of $\\triangle ADE$ to trapezium $DBCE$ is {m*m}:", (m + n) ** 2 - m * m, why="$(m+n)^2-m^2$") for m, n in [(1, 2), (2, 3), (3, 4), (1, 4), (2, 5)]],
      [MN(f"In a right triangle with hypotenuse $c={c}$ and one leg $a={a}$, the area (sq. units) is:", F(a * b, 2), why="Find $b$ by Pythagoras") for a, b, c in TR[:5]],
      [MN(f"The sides of a triangle are {a}, {b}, {c} (all in cm); the length of the altitude to the longest side (cm) of a right triangle is:" if False else f"The altitude on the hypotenuse of the right triangle with legs {a} and {b} is of length (cm):", F(a * b, c), why="$\\frac12ab=\\frac12ch$") for a, b, c in TR[:5]],
      [MN(f"If $\\triangle ABC\\sim\\triangle PQR$, $ar(ABC)={a*a*k}$ and $ar(PQR)={b*b*k}$ and $AB={a*2}$, then $PQ=$", b * 2, why="Sides in ratio $a:b$") for a, b, k in [(3, 7, 2), (4, 9, 3), (2, 11, 5), (5, 8, 4), (3, 10, 6)]],
      [MN(f"In $\\triangle ABC$ right-angled at $B$, $AB={a}$, $BC={b}$. If $BD\\perp AC$, then $AD$ (cm, correct to the exact value) is:", F(a * a, c), why="$AB^2=AD\\cdot AC$") for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (9, 12, 15)]],
      [MN(f"A square has diagonal ${s}\\sqrt2$ cm. Its area (cm²) is:", s * s, why="Side $=s$") for s in [5, 7, 9, 11, 13]]]
def BPTK(x, y, k):
    return Q(f"In $\\triangle ABC$, $DE\\parallel BC$, $AD=x$, $DB=x{sg(y-x)}$... " if False else f"In $\\triangle ABC$, $DE\\parallel BC$, $AD={x}$ cm, $AB={x+y}$ cm and $BC={k*(x+y)}$ cm. Find $DE$.", f"$\\triangle ADE\\sim\\triangle ABC$ (1); $\\dfrac{{DE}}{{BC}}=\\dfrac{{AD}}{{AB}}=\\dfrac{{{x}}}{{{x+y}}}$ (1); $DE={k*x}$ cm (1).", "1+1+1")
hB = ([BPTK(x, y, k) for x, y, k in [(3, 4, 2), (2, 5, 3), (4, 5, 2), (5, 3, 4)]] + [SMALLTRI(m, n) if False else AREAR(s1, s2, A1) for s1, s2, A1 in [(3, 5, 27), (4, 9, 32), (2, 7, 20), (5, 6, 50)]]
      + [Q(f"Find the altitude on the hypotenuse of the right triangle with legs {a} cm and {b} cm.", f"Hypotenuse ${c}$ cm (1); $\\frac12ab=\\frac12ch$ so $h={t(F(a*b,c))}$ cm (1).", "1+1") for a, b, c in TR[:4]])
def TRAPQ(a, b, c, d):
    return Q(f"In trapezium $ABCD$, $AB\\parallel DC$ and the diagonals meet at $O$. If $AB={a*d}$ cm and $DC={b*d}$ cm, find $AO:OC$ and the ratio $ar(AOB):ar(COD)$.", f"$\\triangle AOB\\sim\\triangle COD$ (AA) (1); $\\dfrac{{AO}}{{OC}}=\\dfrac{{AB}}{{DC}}={a}:{b}$ (1); area ratio $={a*a}:{b*b}$ (1).", "1+1+1")
hC = ([TRAPQ(a, b, 0, d) for a, b, d in [(2, 3, 4), (3, 5, 2), (1, 4, 5), (2, 7, 3), (3, 4, 6), (4, 9, 2)]]
      + [Q(f"In an equilateral triangle of side {2*s} cm, find the length of the altitude and the area." if False else f"Find the altitude of an equilateral triangle of side {2*s} cm, in terms of $\\sqrt3$.", f"Altitude bisects the base: $h^2=({2*s})^2-{s}^2={3*s*s}$ (1+1); $h={s}\\sqrt3$ cm (1).", "1+1+1") for s in [3, 4, 5, 6, 7, 9]]
      + [Q(f"In $\\triangle ABC$, $\\angle B=90^\\circ$ and $BD\\perp AC$. If $AD={F(a*a,c)}$ cm and $DC={F(b*b,c)}$ cm, find $BD$ and $AB$." if False else f"$\\triangle ABC$ is right-angled at $B$ with $AB={a}$ cm and $BC={b}$ cm; $BD\\perp AC$. Find $AD$, $DC$ and $BD$.", f"$AC={c}$ cm (1); $AD=\\frac{{AB^2}}{{AC}}={t(F(a*a,c))}$ cm, $DC=\\frac{{BC^2}}{{AC}}={t(F(b*b,c))}$ cm (1); $BD=\\frac{{AB\\cdot BC}}{{AC}}={t(F(a*b,c))}$ cm (1).", "1+1+1") for a, b, c in TR[:6]])
def AB4(a, b, k):
    return Q(f"In $\\triangle ABC$, $AD\\perp BC$ and $BD={a*a}$... " if False else f"Two ships leave a port at the same time; one sails {a*k} km due north and the other {b*k} km due west. Find the distance between them and the ratio of this to the distance if both travelled half as far.", f"Right triangle with legs ${a*k}$ and ${b*k}$ (1); distance $=k\\sqrt{{a^2+b^2}}$; here $={t(k*isqrt(a*a+b*b))}$ km (2); half-distance case gives similar triangle, ratio $2:1$ (2).", "1+2+2")
hD = ([AB4(a, b, k) for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)] for k in [10] for b in [b]] if False else
      [Q(f"Two ships leave a port at the same time; one sails {a*k} km due north and the other {b*k} km due west. Find the distance between them and the ratio of this distance to the one if both had sailed only half as far.", f"Right triangle with legs ${a*k}$ and ${b*k}$ (1); distance $=\\sqrt{{{(a*k)**2}+{(b*k)**2}}}={c*k}$ km (2); half-distance triangle is similar with ratio $1:2$, so the distances are in ratio $2:1$ (2).", "1+2+2") for a, b, c, k in [(3, 4, 5, 20), (5, 12, 13, 10), (8, 15, 17, 6), (6, 8, 10, 15)]]
      + [POLES(a, b, d) for a, b, d in [(22, 6, 12), (19, 7, 9), (30, 12, 24), (45, 9, 27)]]
      + [Q(f"A girl {h} m tall walks away from a lamp post {H} m high at {v} m/s. Find the length of her shadow after {tt} seconds.", f"Distance walked $={v*tt}$ m; let shadow $=x$ m (1); similar triangles: $\\dfrac{{x}}{{x+{v*tt}}}=\\dfrac{{{h}}}{{{H}}}$ (2); $x={t(F(h*v*tt,H-h))}$ m (2).", "1+2+2") for h, H, v, tt in [(F(3, 2), F(9, 2), 2, 6) if False else (2, 6, 1, 8), (3, 9, 2, 6), (1, 5, 2, 10), (2, 8, 3, 4)] ])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
