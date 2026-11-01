"""Class 8 Maths Ch 9 - The Baudhayana-Pythagoras Theorem."""
from c8m_u import *

SLUG, NAME, CHNO = "Baudhayana_Pythagoras_Theorem", "The Baudhayana–Pythagoras Theorem", 9

def rt(n):
    """LaTeX for sqrt(n) simplified"""
    k = 1; m = n
    for p in range(isqrt(n), 1, -1):
        if m % (p * p) == 0: k *= p; m //= p * p; break
    while True:
        done = True
        for p in range(isqrt(m), 1, -1):
            if m % (p * p) == 0: k *= p; m //= p * p; done = False; break
        if done: break
    if m == 1: return str(k)
    return (str(k) if k > 1 else "") + r"\sqrt{%d}" % m
def srt(n): return "$" + rt(n) + "$"
def is_sq(n): return isqrt(n) ** 2 == n
def SURD(q, n, why, others):
    """MCQ whose answer is sqrt(n) (simplified, math mode) with wrong radicands given in others"""
    ws = []
    for o in others:
        s = srt(o) if o > 0 else None
        if s and s != srt(n) and s not in ws: ws.append(s)
    for o in (n + 1, n + 2, n * 2, n - 1, n + 4):
        s = srt(o)
        if o > 0 and s != srt(n) and s not in ws: ws.append(s)
    return M4(q, srt(n), ws[:3], why)

ET = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (7, 24, 25), (12, 16, 20), (15, 20, 25)]
NT = [(20, 21, 29), (9, 40, 41), (10, 24, 26), (12, 35, 37), (11, 60, 61), (16, 30, 34), (28, 45, 53), (33, 56, 65)]
MT = [(18, 24, 30), (15, 36, 39), (24, 32, 40), (21, 28, 35), (30, 40, 50), (14, 48, 50), (27, 36, 45), (40, 42, 58)]
HT = [(48, 55, 73), (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97), (60, 91, 109), (20, 99, 101), (44, 117, 125)]
for L in (ET, NT, MT, HT):
    for a, b, c in L: assert a * a + b * b == c * c, (a, b, c)

def tri3(a, b, c): return f"{a}, {b}, {c}"
def near_trip(a, b, c): return [tri3(a, b, c + 1), tri3(a, b + 1, c), tri3(a + 1, b + 1, c), tri3(a, b, c - 1)]

# ================= EASY =================
e1 = [M4(f"The legs of a right triangle are {a} cm and {b} cm. Its hypotenuse (in cm) is:", c, [a + b, c + 1, c - 1, b - a if b > a else a - b], f"${a}^2+{b}^2={a*a}+{b*b}={c*c}$, hypotenuse $={c}$") for a, b, c in ET]
e2 = [M4(f"The hypotenuse of a right triangle is {c} cm and one leg is {a} cm. The other leg (in cm) is:", b, [c - a, b + 1, b - 1, c + a], f"${c}^2-{a}^2={c*c-a*a}$, other leg $={b}$") for a, b, c in ET]
e3 = [M4("Which of the following is a Pythagorean triplet?", tri3(a, b, c), near_trip(a, b, c), f"${a}^2+{b}^2={a*a+b*b}={c}^2$") for a, b, c in ET[:6]]
e4 = [M4(f"The perimeter of a right triangle with legs {a} cm and {b} cm is (in cm):", a + b + c, [a + b, a + b + c + 1, c * 2, a + b + c - 2], f"Hypotenuse $={c}$; perimeter $={a}+{b}+{c}={a+b+c}$") for a, b, c in ET[:6]]
e5 = [M4(f"A rectangle is {a} cm long and {b} cm broad. Its diagonal (in cm) is:", c, [a + b, c + 1, c - 1, abs(a - b)], f"Diagonal$^2={a*a}+{b*b}={c*c}$") for a, b, c in ET[:6]]
e6 = [M4("The longest side of a right triangle is called the:", "hypotenuse", ["altitude", "base", "median"], "Side opposite the right angle"),
      M4("In a right triangle, the hypotenuse is opposite to the angle of:", r"$90^\circ$", [r"$30^\circ$", r"$60^\circ$", r"$45^\circ$"], "Right angle"),
      M4("In a right triangle with legs $a$, $b$ and hypotenuse $c$:", "$a^2+b^2=c^2$", ["$a+b=c$", "$a^2-b^2=c^2$", "$a^2+c^2=b^2$"], "Baudhayana–Pythagoras theorem"),
      M4("The smallest Pythagorean triplet is:", "3, 4, 5", ["1, 2, 3", "2, 3, 4", "4, 5, 6"], "$3^2+4^2=5^2$"),
      M4("The Baudhayana–Pythagoras theorem is true for:", "right-angled triangles only", ["all triangles", "isosceles triangles only", "equilateral triangles only"], "Right triangles only"),
      M4("The diagonal of a square is:", "longer than its side", ["equal to its side", "shorter than its side", "half of its side"], "Diagonal is the hypotenuse of a right triangle")]
EASY_A = [e1, e2, e3, e4, e5, e6]
EASY_B = ([Q(f"The legs of a right triangle are {a} cm and {b} cm. Find its hypotenuse.", f"$h^2={a}^2+{b}^2={a*a}+{b*b}={c*c}$ (1); $h={c}$ cm (1).", "1+1") for a, b, c in ET[:4]]
          + [Q(f"In a right triangle the hypotenuse is {c} cm and one leg is {a} cm. Find the other leg.", f"$x^2={c}^2-{a}^2={c*c}-{a*a}={b*b}$ (1); $x={b}$ cm (1).", "1+1") for a, b, c in ET[4:]]
          + [Q(f"Is a triangle with sides {x}, {y}, {z} cm right-angled?", (f"${x}^2+{y}^2={x*x+y*y}={z}^2$ (1), so it is right-angled (1)." if x * x + y * y == z * z else f"${x}^2+{y}^2={x*x+y*y}\\ne{z}^2={z*z}$ (1), so it is not right-angled (1)."), "1+1") for x, y, z in [(6, 8, 10), (4, 5, 6), (9, 12, 15), (5, 7, 9)]])
EASY_C = ([Q(f"A ladder {c} m long leans against a wall. Its foot is {a} m from the wall. How high on the wall does it reach?", f"Height$^2={c}^2-{a}^2={c*c}-{a*a}={b*b}$ (2); height $={b}$ m (1).", "2+1") for a, b, c in ET[:6]]
          + [Q(f"Find the perimeter of a right triangle whose legs are {a} cm and {b} cm.", f"Hypotenuse$^2={a*a}+{b*b}={c*c}$, hypotenuse $={c}$ cm (2); perimeter $={a}+{b}+{c}={a+b+c}$ cm (1).", "2+1") for a, b, c in ET[2:8]]
          + [Q(f"Rohan walks {a} km east and then {b} km north. How far is he from his starting point?", f"Distance$^2={a}^2+{b}^2={c*c}$ (2); distance $={c}$ km (1).", "2+1") for a, b, c in ET[1:7]])
EASY_D = ([Q(f"A rectangular field is {a} m long and {b} m broad. Find the length of its diagonal. A man walks along the diagonal instead of the two sides; how much distance does he save?", f"Diagonal$^2={a*a}+{b*b}={c*c}$, diagonal $={c}$ m (3); distance along two sides $={a+b}$ m, saved $={a+b-c}$ m (2).", "3+2") for a, b, c in ET[:6]]
          + [Q(f"Using $(2m,\\,m^2-1,\\,m^2+1)$ with $m={m}$, write a Pythagorean triplet and verify it.", f"Triplet: ${2*m},\\,{m*m-1},\\,{m*m+1}$ (2); ${(2*m)**2}+{(m*m-1)**2}={(2*m)**2+(m*m-1)**2}$ (2); ${m*m+1}^2={(m*m+1)**2}$ so verified (1).", "2+2+1") for m in [2, 3, 4, 5, 6, 7]])

# ================= NCERT =================
n1 = [SURD(f"The legs of a right triangle are {a} cm and {b} cm. Its hypotenuse (in cm) is:", a * a + b * b, f"$h^2={a}^2+{b}^2={a*a+b*b}$", [a + b, (a + b) ** 2]) for a, b in [(5, 7), (2, 6), (3, 5), (4, 6), (1, 7), (6, 7)]]
n2 = [M4(f"The legs of a right triangle are {a} cm and {b} cm. The area of the square drawn on its hypotenuse (in cm²) is:", a * a + b * b, [a * b, a + b, a * a + b * b + 2 * a * b], f"Square on hypotenuse $=a^2+b^2={a*a+b*b}$") for a, b in [(7, 9), (11, 13), (5, 14), (8, 17), (12, 19)]]
n3 = [M4(f"Taking $m={m}$ in $(2m,\\,m^2-1,\\,m^2+1)$, the Pythagorean triplet is:", tri3(2 * m, m * m - 1, m * m + 1), [tri3(2 * m, m * m - 1, m * m + 2), tri3(m, m * m - 1, m * m + 1), tri3(2 * m, m * m, m * m + 1)], f"$2m={2*m}$, $m^2-1={m*m-1}$, $m^2+1={m*m+1}$") for m in [8, 9, 10, 11, 12, 13]]
n4 = [M4(f"A triangle has sides {x} cm, {y} cm and {z} cm. It is:", "right-angled" if x * x + y * y == z * z else "not right-angled", ["right-angled" if x * x + y * y != z * z else "not right-angled", "equilateral", "cannot be said"], f"${x}^2+{y}^2={x*x+y*y}$ and ${z}^2={z*z}$") for x, y, z in [(14, 48, 50), (11, 25, 30), (24, 45, 51), (13, 16, 22), (36, 77, 85), (20, 48, 54)]]
n5 = [SURD(f"The diagonal of a square of side {s} cm (in cm) is:", 2 * s * s, f"$d^2=s^2+s^2={2*s*s}$", [s * s, 4 * s * s]) for s in [3, 5, 6, 7, 9]]
n6 = [M4(f"The hypotenuse of a right triangle is {c} cm and one leg is {a} cm. Its area (in cm²) is:", Fr(a * b, 2), [a * b, Fr(a * c, 2), Fr(a * b, 2) + a], f"Other leg $={b}$ cm; area $=\\frac12\\times{a}\\times{b}$") for a, b, c in NT[:6]]
n7 = [M4("The Baudhayana–Pythagoras theorem states that in a right triangle:", "the square of the hypotenuse equals the sum of the squares of the other two sides", ["the sum of the two legs equals the hypotenuse", "the square of a leg equals the sum of the other two sides", "the hypotenuse is the shortest side"], "Statement of the theorem"),
      M4("If the sum of the squares of two sides of a triangle equals the square of the third side, then the triangle is:", "right-angled", ["acute-angled", "obtuse-angled", "equilateral"], "Converse of the theorem"),
      M4("The diagonal of a rectangle divides it into two:", "congruent right triangles", ["equilateral triangles", "isosceles triangles with no right angle", "similar squares"], "Rectangle has four right angles")]
NCERT_A = [n1, n2, n3, n4, n5, n6, n7]
NCERT_B = ([Q(f"Find the Pythagorean triplet with the smallest member ${2*m}$.", f"Take $2m={2*m}$, so $m={m}$ (1); triplet $({2*m},\\,{m*m-1},\\,{m*m+1})$ (1).", "1+1") for m in [14, 15, 16, 18]]
           + [Q(f"The sides of a triangle are {x} cm, {y} cm, {z} cm. Is it a right triangle? Which angle is the right angle?", f"${x}^2+{y}^2={x*x+y*y}$ (1); ${z}^2={z*z}$ so the triangle is right-angled, the right angle is opposite the side {z} cm (1)." if x * x + y * y == z * z else f"${x}^2+{y}^2={x*x+y*y}\\neq{z}^2={z*z}$ (1) so it is not a right triangle (1).", "1+1") for x, y, z in [(16, 63, 65), (18, 24, 32), (45, 108, 117), (19, 21, 29)]]
           + [Q(f"Find the length of the diagonal of a square of side {s} cm.", rf"$d^2={s}^2+{s}^2={2*s*s}$ (1); $d={rt(2*s*s)}$ cm (1).", "1+1") for s in [4, 8, 10, 12]])
NCERT_C = ([Q(f"The hypotenuse of an isosceles right triangle is ${k}\\sqrt2$ cm. Find the length of each equal side and the area of the triangle.", rf"$2x^2=({k}\sqrt2)^2={2*k*k}$ (1); $x={k}$ cm (1); area $=\frac12\times{k}\times{k}={g(Fr(k*k,2))}$ cm² (1).", "1+1+1") for k in [4, 6, 7, 9, 10, 12]]
           + [Q(f"A ladder {c} m long reaches a window {b} m above the ground. Find the distance of the foot of the ladder from the wall.", f"$d^2={c}^2-{b}^2={c*c}-{b*b}={a*a}$ (2); $d={a}$ m (1).", "2+1") for a, b, c in NT[:6]]
           + [Q(f"The diagonals of a rhombus are {2*a} cm and {2*b} cm. Find its side.", f"Diagonals bisect at right angles: half-diagonals {a} cm and {b} cm (1); side$^2={a*a}+{b*b}={c*c}$ (1); side $={c}$ cm (1).", "1+1+1") for a, b, c in NT[2:8]])
NCERT_D = ([Q(f"The diagonals of a rhombus are {2*a} cm and {2*b} cm. Find its side, perimeter and area.", f"Half-diagonals {a} cm, {b} cm (1); side$^2={a*a}+{b*b}={c*c}$, side $={c}$ cm (2); perimeter $=4\\times{c}={4*c}$ cm (1); area $=\\frac12\\times{2*a}\\times{2*b}={2*a*b}$ cm² (1).", "1+2+1+1") for a, b, c in NT[:6]]
           + [Q(f"Two poles of heights {h1} m and {h2} m stand on level ground {d} m apart. Find the distance between their tops.", f"Difference in heights $={h1}-{h2}={h1-h2}$ m (1); distance$^2={h1-h2}^2+{d}^2={(h1-h2)**2+d*d}$ (2); distance $={isqrt((h1-h2)**2+d*d)}$ m (2).", "1+2+2")
              for h1, h2, d in [(20, 12, 15), (30, 6, 10), (17, 5, 16), (45, 5, 42), (35, 11, 32), (28, 4, 7)]])

# ================= MEDIUM =================
m1 = [M4(f"An isosceles triangle has equal sides {c} cm and base {2*a} cm. Its height (in cm) is:", b, [c - a, b + 1, b - 1, c + a], f"Height splits the base: $h^2={c}^2-{a}^2={b*b}$") for a, b, c in MT]
m2 = [M4(f"A rectangle has a diagonal of {c} cm and one side {a} cm. Its perimeter (in cm) is:", 2 * (a + b), [a + b, 2 * (a + c), 2 * (a + b) + 2], f"Other side $={b}$; perimeter $=2({a}+{b})$") for a, b, c in MT[:6]]
m3 = [M4(f"The side of a rhombus is {c} cm and one diagonal is {2*a} cm. The other diagonal (in cm) is:", 2 * b, [b, 2 * c - 2 * a, 2 * b + 2], f"Half of other diagonal $=\\sqrt{{{c}^2-{a}^2}}={b}$") for a, b, c in MT[:6]]
m4 = [M4(f"Two vertical poles of heights {h} m and {h-a} m stand {b} m apart on level ground. The distance between their tops (in m) is:", c, [a + b, c + 1, c - 2], f"Height difference ${a}$ m; $\sqrt{{{a}^2+{b}^2}}={c}$") for (a, b, c), h in zip(MT[:6], [40, 35, 38, 45, 50, 42])]
m5 = [M4(f"The area of a right triangle with hypotenuse {c} cm and one leg {a} cm (in cm²) is:", a * b // 2, [a * b, a * c // 2, a * b // 2 + a], f"Other leg $={b}$; area $=\\frac12ab$") for a, b, c in MT[:6]]
m6 = [M4("Which set of numbers is a Pythagorean triplet?", tri3(*[k * x for x in t]), [tri3(k * t[0], k * t[1], k * t[2] + 1), tri3(k * t[0] + 1, k * t[1], k * t[2]), tri3(k * t[0], k * t[1] + 2, k * t[2])], f"Multiples of ${t}$ by ${k}$ stay a triplet") for t, k in [((3, 4, 5), 11), ((5, 12, 13), 7), ((8, 15, 17), 5), ((7, 24, 25), 3), ((3, 4, 5), 13)]]
MED_A = [m1, m2, m3, m4, m5, m6]
MED_B = ([Q(f"An isosceles triangle has equal sides of {c} cm and base {2*a} cm. Find its height.", f"Height bisects the base, $h^2={c}^2-{a}^2$ (1); $h={b}$ cm (1).", "1+1") for a, b, c in MT[:4]]
         + [Q(f"The diagonal of a rectangle is {c} cm and one side is {a} cm. Find the other side and the area.", f"Other side $={b}$ cm (1); area $={a*b}$ cm² (1).", "1+1") for a, b, c in MT[2:6]]
         + [Q(f"The side of a rhombus is {c} cm and one diagonal is {2*a} cm. Find the other diagonal.", f"Half of other diagonal$^2={c}^2-{a}^2={b*b}$ (1); other diagonal $={2*b}$ cm (1).", "1+1") for a, b, c in MT[4:8]])
MED_C = ([Q(f"A ladder {L} m long reaches a point {h1} m up a wall. The foot is then pulled away so that it is {d2} m from the wall. How far down does the top of the ladder slip?", f"Initial foot distance $=\\sqrt{{{L}^2-{h1}^2}}={d1}$ m (1); new height $=\\sqrt{{{L}^2-{d2}^2}}={h2}$ m (1); slip $={h1}-{h2}={h1-h2}$ m (1).", "1+1+1")
           for L, d1, h1, d2, h2 in [(25, 7, 24, 15, 20), (25, 15, 20, 20, 15), (13, 5, 12, 12, 5), (17, 8, 15, 15, 8), (26, 10, 24, 24, 10), (39, 15, 36, 36, 15)] if h1 != h2][:6]
         + [Q(f"Show that the triangle with sides {x} cm, {y} cm and {z} cm is right-angled and find its area.", f"${x}^2+{y}^2={x*x+y*y}={z}^2$ (1); right-angled with legs {x}, {y} (1); area $=\\frac12\\times{x}\\times{y}={g(Fr(x*y,2))}$ cm² (1).", "1+1+1") for x, y, z in MT[:6]]
         + [Q(f"The altitude drawn to the hypotenuse of a right triangle with legs {a} cm and {b} cm: find the hypotenuse and the length of this altitude.", f"Hypotenuse $={c}$ cm (1); area $=\\frac12\\times{a}\\times{b}={a*b//2}$ (1); $\\frac12\\times{c}\\times h={a*b//2}$ gives $h={g(Fr(a*b,c))}$ cm (1).", "1+1+1") for a, b, c in MT[:6]])
MED_D = ([Q(f"A man walks {a} m east and then {b} m north. Find (i) the straight-line distance of his final position from the start, (ii) the distance saved by going straight, (iii) the total distance if he returns to the start by the straight path.", f"(i) $\sqrt{{{a}^2+{b}^2}}={c}$ m (2); (ii) saved $={a}+{b}-{c}={a+b-c}$ m (1); (iii) total $={a}+{b}+{c}={a+b+c}$ m (2).", "2+1+2") for a, b, c in MT[:6]]
          + [Q(f"An isosceles triangle has equal sides of {c} cm and base {2*a} cm. Find its height, area and perimeter.", f"Height$^2={c}^2-{a}^2={b*b}$, height $={b}$ cm (2); area $=\\frac12\\times{2*a}\\times{b}={a*b}$ cm² (2); perimeter $=2\\times{c}+{2*a}={2*c+2*a}$ cm (1).", "2+2+1") for a, b, c in MT[2:8]])

# ================= HARD =================
def fac(k, t): return tuple(k * x for x in t)
h1 = [M4(f"The legs of a right triangle are in the ratio ${p}:{q}$ and its hypotenuse is {k*c} cm. Its perimeter (in cm) is:", k * (p + q + c), [k * (p + q), k * c * 2, k * (p + q + c) + k], f"Legs ${k*p}$ and ${k*q}$ since ${p}^2+{q}^2={c}^2$") for (p, q, c), k in [((5, 12, 13), 4), ((8, 15, 17), 3), ((7, 24, 25), 2), ((9, 40, 41), 2)]]
h2 = [M4(f"The sides of a rectangle are in the ratio ${p}:{q}$ and its diagonal is {k*c} cm. The area of the rectangle (in cm²) is:", k * k * p * q, [k * k * p * q + k * k, k * (p + q) * 2, k * k * c], f"Sides ${k*p}$ and ${k*q}$; area $={k*p}\\times{k*q}$") for (p, q, c), k in [((3, 4, 5), 9), ((5, 12, 13), 3), ((8, 15, 17), 2), ((20, 21, 29), 1)]]
h3 = [M4(f"A Pythagorean triplet whose smallest member is {n} is:", tri3(*t), [tri3(n, n + 1, n + 2), tri3(n, t[1] + 1, t[2] + 1), tri3(n, t[1] - 1, t[2] - 1)], "Use $(n,\\frac{n^2-1}{2},\\frac{n^2+1}{2})$ for odd $n$ and $(n,\\frac{n^2}{4}-1,\\frac{n^2}{4}+1)$ for even $n$")
      for n, t in [(n, (n, (n * n - 1) // 2, (n * n + 1) // 2) if n % 2 else (n, n * n // 4 - 1, n * n // 4 + 1)) for n in [15, 17, 22, 26, 31, 40]]]
h4 = [M4(f"A rhombus has perimeter {4*c} cm and one diagonal {2*a} cm. Its area (in cm²) is:", 2 * a * b, [a * b, 2 * a * c, 2 * a * b + a], f"Side ${c}$; half other diagonal ${b}$; area $=\\frac12 d_1d_2={2*a*b}$") for a, b, c in HT[:5]]
h5 = [M4(f"A ladder {L} m long, standing in a street, rests against a house on one side when its top reaches {h1} m. Without moving its foot it is turned to rest against the opposite house, reaching {h2} m. The width of the street (in m) is:", isqrt(L * L - h1 * h1) + isqrt(L * L - h2 * h2), [h1 + h2, L, isqrt(L * L - h1 * h1) + isqrt(L * L - h2 * h2) + 2], f"Foot distances $\\sqrt{{{L}^2-{h1}^2}}={isqrt(L*L-h1*h1)}$ and $\\sqrt{{{L}^2-{h2}^2}}={isqrt(L*L-h2*h2)}$ add up to the width") for L, h1, h2 in [(13, 12, 5), (17, 15, 8), (25, 24, 20), (41, 40, 9), (29, 21, 20)]]
h6 = [M4(f"In a rectangle ABCD, P is a point inside with PA = {x}, PB = {y}, PC = {z}. Then PD$^2$ equals:", x * x + z * z - y * y, [x * x + y * y + z * z, x * x - y * y + z, y * y + z * z - x * x], "Rectangle property $PA^2+PC^2=PB^2+PD^2$") for x, y, z in [(6, 5, 9), (7, 8, 11), (9, 7, 10), (4, 6, 12)]]
h7 = [M4(f"The longest rod that fits in a room {l} m by {b} m by {hh} m has length (in m):", d, [l + b + hh, d - 1, d + 1], f"$\\sqrt{{{l}^2+{b}^2+{hh}^2}}={d}$") for l, b, hh, d in [(2, 3, 6, 7), (4, 4, 7, 9), (2, 6, 9, 11), (6, 6, 7, 11)]]
HARD_A = [h1, h2, h3, h4, h5, h6, h7]
HARD_B = ([Q(f"The legs of a right triangle are in the ratio ${p}:{q}$ and the hypotenuse is {k*c} cm. Find the legs.", f"Let legs be ${p}x$, ${q}x$; hypotenuse $={c}x={k*c}$ (1); $x={k}$, legs ${k*p}$ cm and ${k*q}$ cm (1).", "1+1") for (p, q, c), k in [((3, 4, 5), 7), ((5, 12, 13), 5), ((8, 15, 17), 4), ((7, 24, 25), 3)]]
         + [Q(f"Find a Pythagorean triplet in which one member is {n}.", f"Triplet $({t[0]},\\,{t[1]},\\,{t[2]})$ (1); check ${t[0]}^2+{t[1]}^2={t[0]**2+t[1]**2}={t[2]}^2$ (1).", "1+1") for n, t in [(n, (n, (n * n - 1) // 2, (n * n + 1) // 2) if n % 2 else (n, n * n // 4 - 1, n * n // 4 + 1)) for n in [19, 24, 33, 36]]]
         + [Q(f"In a rectangle ABCD, P is a point inside with PA = {x} cm, PB = {y} cm, PC = {z} cm. Find PD$^2$.", f"$PA^2+PC^2=PB^2+PD^2$ (1); $PD^2={x*x}+{z*z}-{y*y}={x*x+z*z-y*y}$ (1).", "1+1") for x, y, z in [(8, 6, 10), (9, 7, 12), (5, 11, 13), (10, 9, 14)]])
HARD_C = ([Q(f"A ladder {L} m long, with its foot in a street, reaches a window {h1} m high on one side. Without moving its foot it is turned to reach a window {h2} m high on the opposite side. Find the width of the street.", f"Foot to first wall $=\\sqrt{{{L}^2-{h1}^2}}={isqrt(L*L-h1*h1)}$ m (1); foot to second wall $=\\sqrt{{{L}^2-{h2}^2}}={isqrt(L*L-h2*h2)}$ m (1); width $={isqrt(L*L-h1*h1)+isqrt(L*L-h2*h2)}$ m (1).", "1+1+1") for L, h1, h2 in [(37, 35, 12), (53, 45, 28), (65, 63, 33), (61, 60, 11), (85, 84, 40), (73, 55, 48)]]
         + [Q(f"A rhombus has perimeter {4*c} cm and one diagonal {2*a} cm. Find the other diagonal and the area.", f"Side $={c}$ cm; half-diagonal $={a}$ cm (1); other half $=\\sqrt{{{c}^2-{a}^2}}={b}$ cm, other diagonal ${2*b}$ cm (1); area $=\\frac12\\times{2*a}\\times{2*b}={2*a*b}$ cm² (1).", "1+1+1") for a, b, c in HT[:6]]
         + [Q(f"Two ships leave a port, one sailing east at {u} km/h and the other south at {v} km/h. How far apart are they after {t} hours?", f"East distance $={u*t}$ km, south distance $={v*t}$ km (1); distance$^2={(u*t)**2}+{(v*t)**2}={(u*t)**2+(v*t)**2}$ (1); distance $={c*t}$ km (1).", "1+1+1") for (u, v, c), t in zip([(8, 15, 17), (12, 35, 37), (20, 21, 29), (9, 40, 41), (16, 30, 34), (24, 7, 25)], [3, 2, 4, 2, 5, 3])])
QUAD = [((9, 12, 15), (15, 20, 25)), ((5, 12, 13), (13, 84, 85)), ((8, 6, 10), (10, 24, 26)), ((12, 16, 20), (20, 21, 29)), ((15, 8, 17), (17, 144, 145)), ((7, 24, 25), (25, 60, 65))]
for (a, b, e), (e2_, f, hh) in QUAD: assert a * a + b * b == e * e and e2_ == e and e * e + f * f == hh * hh, (a, b, e, f, hh)
CUB = [(1, 2, 2, 3), (2, 3, 6, 7), (4, 4, 7, 9), (2, 6, 9, 11), (6, 6, 7, 11), (3, 4, 12, 13)]
for l, b, hh, d in CUB: assert l * l + b * b + hh * hh == d * d
HARD_D = ([Q(f"In quadrilateral ABCD, $\\angle B=90^\\circ$, AB = {a} cm, BC = {b} cm, CD = {f} cm and DA = {hh} cm. Prove that $\\angle ACD=90^\\circ$ and find the area of ABCD.", f"$AC^2={a}^2+{b}^2={e*e}$, $AC={e}$ cm (1); $AC^2+CD^2={e*e}+{f*f}={hh*hh}=DA^2$ so $\\angle ACD=90^\\circ$ (2); area $=\\frac12\\times{a}\\times{b}+\\frac12\\times{e}\\times{f}={g(Fr(a*b,2)+Fr(e*f,2))}$ cm² (2).", "1+2+2") for (a, b, e), (_, f, hh) in QUAD]
          + [Q(f"A room is {l} m long, {b} m wide and {hh} m high. Find the length of the longest rod that can be placed in it. Also find the diagonal of its floor.", f"Floor diagonal$^2={l}^2+{b}^2={l*l+b*b}$ (1), floor diagonal $=\\sqrt{{{l*l+b*b}}}$ m (1); rod$^2={l*l+b*b}+{hh}^2={d*d}$ (2); rod $={d}$ m (1).", "1+1+2+1") for l, b, hh, d in CUB])

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}
