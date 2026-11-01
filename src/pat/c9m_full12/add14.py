"""Chapter 13 (pair of linear equations) and Chapter 14 (surface area & volume) items for the 14-chapter Class 9 Maths sets."""
from cm import *
import math
PI = F(22, 7)

# ---------------- solid figures (inline SVG) ----------------
def _el(cx, cy, rx, ry, dash=False, c='#000', fill='none', w=1.4):
    return f"<ellipse cx='{cx}' cy='{cy}' rx='{rx}' ry='{ry}' stroke='{c}' stroke-width='{w}' fill='{fill}'{' stroke-dasharray=%s' % chr(39)+'4,3'+chr(39) if dash else ''}/>"
def _path(d, c='#000', fill='none', w=1.4, dash=False):
    return f"<path d='{d}' stroke='{c}' stroke-width='{w}' fill='{fill}'{' stroke-dasharray=%s' % chr(39)+'4,3'+chr(39) if dash else ''}/>"
def _half_el_front(cx, cy, rx, ry): return _path(f"M{cx-rx},{cy} A{rx},{ry} 0 0 0 {cx+rx},{cy}")
def _half_el_back(cx, cy, rx, ry): return _path(f"M{cx-rx},{cy} A{rx},{ry} 0 0 1 {cx+rx},{cy}", dash=True)

def cylinder_fig(r='r', h='h', open_top=False, cx=100, top=30, H=90, R=45, W=200, size_lab=True, tag=''):
    ry = 12; bot = top + H
    b = _el(cx, top, R, ry, fill='#eef2fb') if not open_top else _el(cx, top, R, ry)
    b += line(cx-R, top, cx-R, bot) + line(cx+R, top, cx+R, bot) + _half_el_front(cx, bot, R, ry) + _half_el_back(cx, bot, R, ry)
    b += line(cx, bot, cx+R, bot, '#0f2347', 1.2, '3,2') + text(cx+R/2, bot-3, r, sz=11)
    b += line(cx+R+14, top, cx+R+14, bot, '#0f2347', 1.2) + text(cx+R+18, (top+bot)/2+4, h, 'start', 11)
    if tag: b += text(cx, bot+ry+16, tag, sz=10)
    return svg(W, bot+ry+22 if tag else bot+ry+8, b)

def cone_fig(r='r', h='h', l='l', cx=100, top=14, H=100, R=48, W=210, tag=''):
    ry = 12; bot = top + H
    b = line(cx, top, cx-R, bot) + line(cx, top, cx+R, bot) + _half_el_front(cx, bot, R, ry) + _half_el_back(cx, bot, R, ry)
    b += line(cx, top, cx, bot, '#0f2347', 1.2, '3,2') + dot(cx, bot, '', 0, 0)
    b += line(cx, bot, cx+R, bot, '#0f2347', 1.2, '3,2') + text(cx+R/2, bot+14, r, sz=11)
    b += text(cx-5, (top+bot)/2+4, h, 'end', 11) + text(cx+R/2+12, (top+bot)/2-6, l, 'start', 11)
    if tag: b += text(cx, bot+ry+20, tag, sz=10)
    return svg(W, bot+ry+(26 if tag else 12), b)

def hemisphere_fig(r='r', cx=100, base=95, R=60, W=200, tag=''):
    ry = 14
    b = _path(f"M{cx-R},{base} A{R},{R} 0 0 1 {cx+R},{base}", fill='#eef2fb') + _el(cx, base, R, ry) + dot(cx, base, 'O', 4, -4)
    b += line(cx, base, cx+R, base, '#0f2347', 1.2) + text(cx+R/2, base+12 if False else base-4, r, sz=11)
    if tag: b += text(cx, base+ry+18, tag, sz=10)
    return svg(W, base+ry+(24 if tag else 10), b)

def sphere_fig(r='r', cx=100, cy=72, R=55, W=200, tag=''):
    b = circ(cx, cy, R) + _half_el_front(cx, cy, R, 14) + _half_el_back(cx, cy, R, 14) + dot(cx, cy, 'O', 4, -4)
    b += line(cx, cy, cx+R, cy, '#0f2347', 1.2) + text(cx+R/2, cy-4, r, sz=11)
    if tag: b += text(cx, cy+R+18, tag, sz=10)
    return svg(W, cy+R+(24 if tag else 8), b)

def cube_fig(a='a', s=70, ox=40, oy=30, d=28, W=200):
    f = [(ox, oy+d), (ox+s, oy+d), (ox+s, oy+d+s), (ox, oy+d+s)]
    bk = [(x+d, y-d) for x, y in f]
    b = poly(f, fill='#eef2fb') + poly([f[0], f[1], bk[1], bk[0]], fill='#f6f8fd') + poly([f[1], f[2], bk[2], bk[1]], fill='#dde5f5')
    b += text(ox+s/2, oy+d+s+14, a, sz=11) + text(ox+s+d+8, oy+d+s/2, a, 'start', 11)
    return svg(W, oy+d+s+22, b)

def pair_cyl_svg():
    ry = 10
    # P: radius 20, height 90 ; Q: radius 60, height 30  (ratio r:3r, h:h/3)
    def cyl(cx, R, H, top, lab_r, lab_h, name):
        bot = top + H
        s = _el(cx, top, R, ry, fill='#eef2fb') + line(cx-R, top, cx-R, bot) + line(cx+R, top, cx+R, bot) + _half_el_front(cx, bot, R, ry) + _half_el_back(cx, bot, R, ry)
        s += line(cx, bot, cx+R, bot, '#0f2347', 1.2, '3,2') + text(cx+R/2, bot-3, lab_r, sz=11) + text(cx+R+6, (top+bot)/2+4, lab_h, 'start', 11) + text(cx, bot+ry+16, name, sz=10)
        return s
    return svg(330, 150, cyl(60, 20, 90, 18, 'r', 'h', 'Cylinder P') + cyl(220, 60, 30, 78, '3r', 'h/3', 'Cylinder Q'))

def cylinder_cone_svg():
    ry = 9
    def cyl(cx, R, H, top):
        bot = top + H
        return _el(cx, top, R, ry, fill='#eef2fb') + line(cx-R, top, cx-R, bot) + line(cx+R, top, cx+R, bot) + _half_el_front(cx, bot, R, ry) + _half_el_back(cx, bot, R, ry) + line(cx, bot, cx+R, bot, '#0f2347', 1.2, '3,2') + text(cx+R/2, bot-3, '3 cm', sz=10) + text(cx+R+6, (top+bot)/2+4, '14 cm', 'start', 10)
    def con(cx, R, H, top):
        bot = top + H
        return line(cx, top, cx-R, bot) + line(cx, top, cx+R, bot) + _half_el_front(cx, bot, R, ry) + _half_el_back(cx, bot, R, ry) + line(cx, top, cx, bot, '#0f2347', 1.2, '3,2') + text(cx+R/2, bot+13, '3 cm', sz=10) + text(cx-4, (top+bot)/2+4, '14 cm', 'end', 10)
    return svg(330, 150, cyl(70, 32, 90, 22) + text(70, 138, 'Solid cylinder', sz=10) + con(230, 32, 90, 22) + text(230, 138, 'Cone (one of several)', sz=10))

def icecream_fig():
    cx = 100; R = 45; ry = 10; base = 70
    b = line(cx-R, base, cx, 160) + line(cx+R, base, cx, 160)
    b += _path(f"M{cx-R},{base} A{R},{R} 0 0 1 {cx+R},{base}", fill='#eef2fb') + _half_el_front(cx, base, R, ry) + _half_el_back(cx, base, R, ry)
    b += line(cx, base, cx+R, base, '#0f2347', 1.2, '3,2') + text(cx+R/2, base-3, '3.5 cm', sz=10) + line(cx, base, cx, 160, '#0f2347', 1.2, '3,2') + text(cx-5, 120, '12 cm', 'end', 10)
    return svg(210, 172, b)

def hemispheres_fig():
    cx1 = 70; cx2 = 220; base = 80; R = 52; ry = 12
    s = _path(f"M{cx1-R},{base} A{R},{R} 0 0 1 {cx1+R},{base}", fill='#eef2fb') + _el(cx1, base, R, ry) + text(cx1, base+ry+18, 'Hemisphere', sz=10)
    s += line(cx1, base, cx1+R, base, '#0f2347', 1.2) + text(cx1+R/2, base-4, '10.5 cm', sz=10)
    s += circ(cx2, 56, R) + _half_el_front(cx2, 56, R, 12) + _half_el_back(cx2, 56, R, 12) + text(cx2, 56+R+18, 'Solid ball', sz=10)
    return svg(300, 140, s)

def graph(eq1, eq2, p1, p2, q1, q2, P, xr, yr, u=20):
    pts = {'P': P}
    return coord_plane(pts, xr=xr, yr=yr, u=u, segs=[(p1, p2), (q1, q2)])

# ---------------- verification helpers ----------------
def cone_v(r, h): return F(1, 3)*PI*r*r*h
def cyl_v(r, h): return PI*r*r*h
def cyl_csa(r, h): return 2*PI*r*h
def cone_csa(r, l): return PI*r*l
def sph_a(r): return 4*PI*r*r
def sph_v(r): return F(4, 3)*PI*r**3
def hem_csa(r): return 2*PI*r*r
def hem_v(r): return F(2, 3)*PI*r**3
def num(x):
    return str(int(x)) if x == int(x) else (f"{float(x):.2f}".rstrip('0').rstrip('.'))

def solve2(a1, b1, c1, a2, b2, c2):
    det = a1*b2 - a2*b1
    return F(c1*b2 - c2*b1, det), F(a1*c2 - a2*c1, det)

def graph_item(e1, e2, tab1, tab2, sol, xr, yr, lines_pts, marks=3, ask="Draw the graphs of the equations {e1} and {e2} on the same grid and use them to find the solution of the pair."):
    (p1, p2), (q1, q2) = lines_pts
    fig = coord_plane({'P(%s, %s)' % sol: sol}, xr=xr, yr=yr, u=21, segs=[(p1, p2), (q1, q2)])
    t1 = htable(["x"] + [a for a, b in tab1], ["y"] + [b for a, b in tab1])
    t2 = htable(["x"] + [a for a, b in tab2], ["y"] + [b for a, b in tab2])
    q = ask.format(e1=e1, e2=e2)
    s = (f"Table for {e1}:" + t1 + f"Table for {e2}:" + t2 + "(1) Draw both lines (1)" + fig + f"The lines meet at <b>({sol[0]}, {sol[1]})</b>, so x = {sol[0]}, y = {sol[1]} (1)")
    return sa(q, marks, s)

# ---------------- per-set content ----------------
def patch(n, A, B, C, E):
    S = SETS[n]
    A[2] = S['a13']; A[13] = S['a14']; B[2] = S['b']; C[2] = S['c']; E[2] = S['e']
    return A, B, C, E

SETS = {}

# ---- SET 1 ----
assert 2*2+0 and 5*2 + 2*5 == 20 and cone_v(6, 7) == 264
assert 22*(2*15+7)//1 == 814 and PI*7*(2*15+7) == 814
sol1 = solve2(1, 1, 6, 1, -1, 2); assert sol1 == (4, 2)
R1, H1 = 21, 21
assert hem_csa(R1) == 2772 and hem_v(R1) == 19404 and 2772*5 == 13860 and cyl_v(R1, H1) == 29106 and F(hem_v(R1), cyl_v(R1, H1)) == F(2, 3)
SETS[1] = dict(
 a13=mc("Which of the following is a solution of the linear equation 5x + 2y = 20?", "(2, 5)", ["(5, 2)", "(4, 1)", "(3, 2)"], "5(2) + 2(5) = 10 + 10 = 20. The others give 29, 22 and 19."),
 a14=mc("The volume of a cone of base radius 6 cm and height 7 cm (take π = 22/7) is:", "264 cm³", ["792 cm³", "528 cm³", "132 cm³"], "V = ⅓πr²h = ⅓ × 22/7 × 36 × 7 = 264 cm³ (792 would be πr²h)."),
 b=sa("A cylindrical tin of radius 7 cm and height 15 cm is open at the top. Find the area of tin sheet needed to make it (π = 22/7).", 2, "Open cylinder: area = 2πrh + πr² = πr(2h + r) (1)<br>= 22/7 × 7 × (30 + 7) = 22 × 37 = <b>814 cm²</b> (1)", fig=cylinder_fig('7 cm', '15 cm', open_top=True)),
 c=graph_item("x + y = 6", "x − y = 2", [(0, 6), (6, 0)], [(0, -2), (2, 0)], (4, 2), (-1, 8), (-3, 8), [((0, 6), (6, 0)), ((0, -2), (6, 4))]),
 e=case("The dome of a planetarium is a hemisphere of radius 21 m (take π = 22/7).",
        [sub("Find the curved surface area of the dome.", 1, "CSA = 2πr² = 2 × 22/7 × 441 = <b>2772 m²</b>"),
         sub("Find the volume of air inside the dome.", 1, "V = ⅔πr³ = ⅔ × 22/7 × 9261 = <b>19404 m³</b>"),
         OR(sub("The outside of the dome is painted at ₹5 per m². Find the cost.", 2, "Cost = 2772 × 5 (1) = <b>₹13860</b> (1)"),
            sub("A cylinder has the same radius and height 21 m. Show that volume of dome : volume of cylinder = 2 : 3.", 2, "Cylinder volume = πr²h = 22/7 × 441 × 21 = 29106 m³ (1); 19404 : 29106 = <b>2 : 3</b> (1)"))], fig=hemisphere_fig('21 m', tag='Dome')),
)

# ---- SET 2 ----
assert 3*4 + 4*2 == 20 and cyl_v(7, 10) == 1540
assert cone_csa(7, 25) == 550 and math.isqrt(25**2-7**2) == 24
sol2 = solve2(2, 1, 8, 1, -1, 1); assert sol2 == (3, 2)
assert cone_v(7, 24) == 1232 and cone_csa(7, 25) == 550 and F(1232) / (PI*49) == 8
SETS[2] = dict(
 a13=mc("If (k, 2) is a solution of the equation 3x + 4y = 20, then the value of k is:", "4", ["2", "5", "8"], "3k + 8 = 20 ⇒ 3k = 12 ⇒ k = 4."),
 a14=mc("A cylindrical drum has radius 7 cm and height 10 cm. Its volume (π = 22/7) is:", "1540 cm³", ["440 cm³", "770 cm³", "3080 cm³"], "V = πr²h = 22/7 × 49 × 10 = 1540 cm³ (440 cm² would be the curved surface area)."),
 b=sa("A conical tent has base radius 7 m and slant height 25 m. Find its curved surface area and its height (π = 22/7).", 2, "CSA = πrl = 22/7 × 7 × 25 = <b>550 m²</b> (1)<br>h = √(25² − 7²) = √576 = <b>24 m</b> (1)", fig=cone_fig('7 m', 'h', '25 m')),
 c=graph_item("2x + y = 8", "x − y = 1", [(0, 8), (4, 0)], [(0, -1), (1, 0)], (3, 2), (-2, 6), (-2, 9), [((0, 8), (4, 0)), ((0, -1), (6, 5))]),
 e=case("A grain merchant stores grain in a conical heap of base radius 7 m and height 24 m (π = 22/7).",
        [sub("Find the slant height of the heap.", 1, "l = √(24² + 7²) = <b>25 m</b>"),
         sub("Find the volume of grain in the heap.", 1, "V = ⅓πr²h = ⅓ × 22/7 × 49 × 24 = <b>1232 m³</b>"),
         OR(sub("Find the area of canvas needed to cover the heap.", 2, "CSA = πrl = 22/7 × 7 × 25 (1) = <b>550 m²</b> (1)"),
            sub("The grain is poured into a cylindrical bin of the same base radius. Find the height of grain in the bin.", 2, "πr²h = 1232 ⇒ 154h = 1232 (1) ⇒ <b>h = 8 m</b> (1)"))], fig=cone_fig('7 m', '24 m', '25 m')),
)

# ---- SET 3 ----
assert math.isclose(0 + 6/2, 3) and sph_a(7) == 616
sol3 = solve2(1, 2, 6, 2, -1, 2); assert sol3 == (2, 2)
assert cyl_csa(F(7, 2), 8) == 176 and cyl_v(F(7, 2), 8) == 308 and 308*1000 == 308000 and 176*40 == 7040
SETS[3] = dict(
 a13=mc("The graph of the equation x + 2y = 6 cuts the y-axis at the point:", "(0, 3)", ["(6, 0)", "(3, 0)", "(0, 6)"], "Put x = 0: 2y = 6 ⇒ y = 3."),
 a14=mc("The surface area of a sphere of radius 7 cm (π = 22/7) is:", "616 cm²", ["154 cm²", "308 cm²", "1437 cm²"], "4πr² = 4 × 22/7 × 49 = 616 cm²."),
 b=sa("The radius of cylinder Q is three times the radius of cylinder P and its height is one-third of the height of P. Find the ratio of (i) their curved surface areas, (ii) their volumes (P : Q).", 2, "Let P have r, h; Q has 3r, h/3. (i) CSA: 2πrh : 2π(3r)(h/3) = <b>1 : 1</b> (1)<br>(ii) Volume: πr²h : π(9r²)(h/3) = πr²h : 3πr²h = <b>1 : 3</b> (1)", fig=pair_cyl_svg()),
 c=graph_item("x + 2y = 6", "2x − y = 2", [(0, 3), (6, 0)], [(0, -2), (1, 0)], (2, 2), (-2, 7), (-3, 5), [((0, 3), (6, 0)), ((0, -2), (3, 4))]),
 e=case("A school has an open cylindrical water tank of radius 3.5 m and height 8 m (π = 22/7).",
        [sub("Find the curved surface area of the tank.", 1, "CSA = 2πrh = 2 × 22/7 × 3.5 × 8 = <b>176 m²</b>"),
         sub("Find the volume of water the tank can hold.", 1, "V = πr²h = 22/7 × 12.25 × 8 = <b>308 m³</b>"),
         OR(sub("Express the capacity of the tank in litres (1 m³ = 1000 litres).", 2, "308 × 1000 (1) = <b>308000 litres</b> (1)"),
            sub("The outer curved surface is painted at ₹40 per m². Find the cost.", 2, "Cost = 176 × 40 (1) = <b>₹7040</b> (1)"))], fig=cylinder_fig('3.5 m', '8 m', open_top=True, tag='Water tank')),
)

# ---- SET 4 ----
assert 3+2 == 5 and 3-2 == 1 and math.isqrt(13**2-5**2) == 12
assert 6*5*5 == 150 and 5**3 == 125
sol4 = solve2(3, 1, 9, 1, 1, 5); assert sol4 == (2, 3)
rr = F(7, 2); assert cone_v(rr, 12) == 154 and hem_csa(rr) == 77 and math.isclose(math.sqrt(144+12.25), 12.5) and cone_csa(rr, F(25, 2)) == F(275, 2) and F(275, 2)+77 == F(429, 2)
SETS[4] = dict(
 a13=mc("The solution of the pair of equations x + y = 5 and x − y = 1 is:", "x = 3, y = 2", ["x = 2, y = 3", "x = 4, y = 1", "x = 5, y = 0"], "Adding: 2x = 6 ⇒ x = 3; then y = 2."),
 a14=mc("A cone has base radius 5 cm and slant height 13 cm. Its height is:", "12 cm", ["8 cm", "18 cm", "√194 cm"], "h² = l² − r² = 169 − 25 = 144 ⇒ h = 12 cm."),
 b=sa("The total surface area of a cube is 150 cm². Find the length of its edge and its volume.", 2, "6a² = 150 ⇒ a² = 25 ⇒ <b>a = 5 cm</b> (1)<br>Volume = a³ = <b>125 cm³</b> (1)", fig=cube_fig('a')),
 c=graph_item("3x + y = 9", "x + y = 5", [(0, 9), (3, 0)], [(0, 5), (5, 0)], (2, 3), (-1, 6), (-1, 10), [((0, 9), (3, 0)), ((0, 5), (5, 0))]),
 e=case("An ice-cream seller serves ice cream in a cone of base radius 3.5 cm and height 12 cm, with a hemispherical scoop of the same radius on top (π = 22/7).",
        [sub("Find the volume of ice cream inside the cone.", 1, "V = ⅓πr²h = ⅓ × 22/7 × 12.25 × 12 = <b>154 cm³</b>"),
         sub("Find the curved surface area of the hemispherical top.", 1, "CSA = 2πr² = 2 × 22/7 × 12.25 = <b>77 cm²</b>"),
         OR(sub("Find the slant height of the cone and its curved surface area.", 2, "l = √(12² + 3.5²) = √156.25 = <b>12.5 cm</b> (1); CSA = πrl = 22/7 × 3.5 × 12.5 = <b>137.5 cm²</b> (1)"),
            sub("Find the total outer surface area of the cone and the hemisphere together (excluding the base).", 2, "Cone CSA = 137.5 cm² (1); total = 137.5 + 77 = <b>214.5 cm²</b> (1)"))], fig=icecream_fig()),
)

# ---- SET 5 ----
sol5 = solve2(2, -1, 1, 1, 1, 5); assert sol5 == (2, 3)
assert F(cyl_v(3, 14), cone_v(3, 14)) == 3
assert sph_a(F(21, 2)) == 1386 and sph_v(F(21, 2)) == 4851 and 3*PI*F(21, 2)**2 == F(2079, 2) and F(4851, 2) == F(9702, 4)
SETS[5] = dict(
 a13=mc("The slope of the line y = 2x + 3 is:", "2", ["3", "−2", "1/2"], "In the slope-intercept form y = mx + c the slope is m = 2."),
 a14=mc("A cylinder and a cone have the same base radius and the same height. The ratio of the volume of the cylinder to that of the cone is:", "3 : 1", ["1 : 3", "2 : 1", "3 : 2"], "πr²h : ⅓πr²h = 3 : 1."),
 b=sa("A solid metal cylinder of radius 3 cm and height 14 cm is melted and recast into cones, each of radius 3 cm and height 14 cm. How many cones are made? Give a reason.", 2, "Volume of cylinder = πr²h; volume of each cone = ⅓πr²h (1)<br>Number of cones = πr²h ÷ ⅓πr²h = <b>3</b> (melting keeps the volume the same) (1)", fig=cylinder_cone_svg()),
 c=graph_item("y = 2x − 1", "x + y = 5", [(0, -1), (2, 3)], [(0, 5), (5, 0)], (2, 3), (-1, 6), (-2, 6), [((0, -1), (3, 5)), ((0, 5), (5, 0))], ask="Draw the graphs of y = 2x − 1 and x + y = 5 on the same grid. Where do the lines meet? Write the solution of the pair."),
 e=case("A solid iron ball has radius 10.5 cm (π = 22/7). It is cut along a plane through its centre into two equal hemispheres.",
        [sub("Find the surface area of the ball.", 1, "4πr² = 4 × 22/7 × 110.25 = <b>1386 cm²</b>"),
         sub("Find the volume of the ball.", 1, "V = 4/3 πr³ = 4/3 × 22/7 × 1157.625 = <b>4851 cm³</b>"),
         OR(sub("Find the volume of each hemisphere.", 2, "Each hemisphere has half the volume (1): 4851 ÷ 2 = <b>2425.5 cm³</b> (1)"),
            sub("Find the total surface area of each hemisphere.", 2, "TSA = CSA + base = 2πr² + πr² = 3πr² (1) = 3 × 22/7 × 110.25 = <b>1039.5 cm²</b> (1)"))], fig=hemispheres_fig()),
)
