"""Class 9 Maths Ch 12 - Quadrilaterals (angle sum, parallelogram, rectangle, rhombus, square, midpoint theorem)."""
from g9m import *

SLUG, NAME, CHNO = "Quadrilaterals", "Quadrilaterals", 12

TRIP = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (6, 8, 10)]
def deg(x): return f"${s(x)}^\\circ$"
def cm(x): return f"${s(x)}$ cm"
def sq(x): return f"${s(x)}$ cm$^2$"
def ang(q, c, why="", offs=(10, -10, 20, -20, 5, 30, 15, -5)): return nn(q, c, why, offs=offs, pos=True, fmtf=deg)
def lenm(q, c, why="", offs=(1, -1, 2, -2, 3, 4, 5, 6), pos=True): return nn(q, c, why, offs=offs, pos=pos, fmtf=cm)
def areq(q, c, why="", offs=(1, -1, 2, 4, 6, 10, 12, 24)): return nn(q, c, why, offs=offs, pos=True, fmtf=sq)
def R(rng, lo, hi, step=1): return rng.randrange(lo, hi + 1, step)

# ---- MCQ generators ----
def g_fourth(lo, hi):
    def f(r):
        a, b, c = R(r, lo, hi, 5), R(r, lo, hi, 5), R(r, lo, hi, 5)
        d = 360 - a - b - c
        if not 20 <= d < 180: return None
        return ang(f"Three angles of a quadrilateral are ${a}^\\circ$, ${b}^\\circ$ and ${c}^\\circ$. The fourth angle is:", d, "Angle sum of a quadrilateral is $360^\\circ$.")
    return f

def g_ratio():
    def f(r):
        p = [r.randint(1, 6) for _ in range(4)]
        if len(set(p)) < 3 or 360 % sum(p): return None
        u_ = 360 // sum(p)
        return ang(f"The angles of a quadrilateral are in the ratio ${':'.join(map(str, p))}$. The largest angle is:", max(p) * u_, f"One part $=360^\\circ\\div{sum(p)}={u_}^\\circ$.")
    return f

def g_par_angle(lo, hi):
    def f(r):
        a = R(r, lo, hi, 2)
        if a == 90: return None
        w = r.choice(["B", "C", "D"])
        v = {"B": 180 - a, "C": a, "D": 180 - a}[w]
        return ang(f"In a parallelogram ABCD, $\\angle A={a}^\\circ$. Then $\\angle {w}$ is:", v, "Opposite angles are equal; adjacent angles add up to $180^\\circ$.")
    return f

def g_par_x(lo, hi):
    def f(r):
        x = r.randint(lo, hi); a, b = r.randint(1, 20), r.randint(1, 20); k = r.choice([2, 3])
        # opposite angles: (k x + a) = (x + a + b)... use: (kx + a) and (x + c) equal
        c = k * x + a - x
        return nn(f"In a parallelogram, two opposite angles are $({k}x+{a})^\\circ$ and $(x+{c})^\\circ$. The value of $x$ is:", x, "Opposite angles are equal.", offs=(1, -1, 2, -2, 5, 10), pos=True)
    return f

def g_par_adj(lo, hi):
    def f(r):
        k = r.randint(2, 8); d = 180 // (k + 1)
        if 180 % (k + 1): return None
        return ang(f"Two adjacent angles of a parallelogram are in the ratio $1:{k}$. The smaller angle is:", d, "Adjacent angles add up to $180^\\circ$.")
    return f

def g_par_diff(lo, hi):
    def f(r):
        d = R(r, lo, hi, 10)
        return ang(f"One angle of a parallelogram exceeds another adjacent angle by ${d}^\\circ$. The smaller angle is:", (180 - d) // 2, "Let angles be $x$ and $x+d$; they add to $180^\\circ$.", offs=(d // 2, -5, 10, 15, 20, 5)) if (180 - d) % 2 == 0 else None
    return f

def g_diag_bis(lo, hi):
    def f(r):
        x = r.randint(lo, hi); p, q = r.randint(2, 5), r.randint(1, 9)
        if p * x + q <= 0: return None
        v = 2 * (p * x + q)
        return lenm(f"The diagonals of a parallelogram intersect at O. If $OA=({p}x+{q})$ cm and $x={x}$, then the diagonal AC is:", v, "Diagonals bisect each other, so $AC=2\\times OA$.", offs=(p * x + q, 2, 4, -2, 6, 10))
    return f

def g_rect_diag(trs):
    def f(r):
        a, b, c = r.choice(trs); k = r.randint(1, 4)
        w = r.choice(["diag", "side"])
        if w == "diag":
            return lenm(f"The sides of a rectangle are ${a*k}$ cm and ${b*k}$ cm. Its diagonal is:", c * k, f"$\\sqrt{{{a*k}^2+{b*k}^2}}={c*k}$.")
        return lenm(f"A rectangle has one side ${a*k}$ cm and diagonal ${c*k}$ cm. The other side is:", b * k, f"$\\sqrt{{{c*k}^2-{a*k}^2}}={b*k}$.")
    return f

def g_rect_area(trs):
    def f(r):
        a, b, c = r.choice(trs); k = r.randint(1, 3)
        return areq(f"The diagonal of a rectangle is ${c*k}$ cm and one side is ${a*k}$ cm. Its area is:", a * b * k * k, f"Other side $={b*k}$ cm; area $={a*k}\\times{b*k}$.", offs=(a * k, b * k, 10, -10, 20, 4))
    return f

def g_rhomb_side(trs):
    def f(r):
        a, b, c = r.choice(trs); k = r.randint(1, 3)
        return lenm(f"The diagonals of a rhombus are ${2*a*k}$ cm and ${2*b*k}$ cm. Its side is:", c * k, f"Half-diagonals ${a*k}$ and ${b*k}$ meet at right angles: side $=\\sqrt{{{a*k}^2+{b*k}^2}}$.")
    return f

def g_rhomb_per(trs):
    def f(r):
        a, b, c = r.choice(trs); k = r.randint(1, 3)
        return lenm(f"The diagonals of a rhombus are ${2*a*k}$ cm and ${2*b*k}$ cm. Its perimeter is:", 4 * c * k, f"Side $={c*k}$ cm, perimeter $=4\\times{c*k}$.", offs=(c * k, 2 * c * k, 4, -4, 8, 10))
    return f

def g_rhomb_area(trs):
    def f(r):
        a, b, c = r.choice(trs); k = r.randint(1, 3); d1, d2 = 2 * a * k, 2 * b * k
        return areq(f"The diagonals of a rhombus are ${d1}$ cm and ${d2}$ cm. Its area is:", d1 * d2 // 2, "Area $=\\frac12d_1d_2$.", offs=(d1, d2, 10, -10, d1 * d2 // 4, 20))
    return f

def g_rhomb_ang(lo, hi):
    def f(r):
        a = R(r, lo, hi, 2)
        if a % 2 or a == 90: return None
        return ang(f"In a rhombus ABCD, $\\angle A={a}^\\circ$. The angle between the diagonal AC and the side AB is:", a // 2, "A diagonal of a rhombus bisects the angle at the vertex.", offs=(a, 90 - a // 2, 10, -10, 5, 15))
    return f

def g_square_diag(lo, hi):
    def f(r):
        s_ = r.randint(lo, hi)
        return M4(f"The diagonal of a square of side ${s_}$ cm is:", f"${s_}\\sqrt2$ cm", [f"${2*s_}$ cm", f"${s_}\\sqrt3$ cm", f"${s_*s_}$ cm"], f"$\\sqrt{{{s_}^2+{s_}^2}}={s_}\\sqrt2$.")
    return f

def g_square_area(lo, hi):
    def f(r):
        d = r.randint(lo, hi) * 2
        return areq(f"The diagonal of a square is ${d}$ cm. Its area is:", d * d // 2, "Area $=\\frac12d^2$.", offs=(d, d * 2, 4, -4, 10, d // 2))
    return f

def g_mid(lo, hi):
    def f(r):
        bc = R(r, lo, hi, 2); w = r.choice(["DE", "BC"])
        if w == "DE":
            return lenm(f"In $\\triangle ABC$, D and E are the midpoints of AB and AC and $BC={bc}$ cm. Then DE is:", bc // 2, "Midpoint theorem: $DE=\\frac12BC$.", offs=(bc, 2, 4, -2, bc // 2 + 3))
        return lenm(f"In $\\triangle ABC$, D and E are the midpoints of AB and AC and $DE={bc//2}$ cm. Then BC is:", bc, "Midpoint theorem: $BC=2DE$.", offs=(bc // 2, 2, 4, -2, bc // 4))
    return f

def g_mid_per(lo, hi):
    def f(r):
        a, b, c = r.randint(lo, hi) * 2, r.randint(lo, hi) * 2, r.randint(lo, hi) * 2
        if a + b <= c or a + c <= b or b + c <= a: return None
        return lenm(f"The sides of a triangle are ${a}$ cm, ${b}$ cm and ${c}$ cm. The perimeter of the triangle formed by joining the midpoints of its sides is:", (a + b + c) // 2, "Each new side is half of a side of the original triangle.", offs=(a + b + c, (a + b + c) // 4, 2, 4, -2, 6))
    return f

def g_varignon(lo, hi):
    def f(r):
        d1, d2 = r.randint(lo, hi), r.randint(lo, hi)
        return lenm(f"The diagonals of a quadrilateral are ${d1}$ cm and ${d2}$ cm. The perimeter of the parallelogram formed by joining the midpoints of its sides is:", d1 + d2, "Each side of the new figure is half a diagonal; there are two of each.", offs=(d1 + d2 + 2, (d1 + d2) // 2, 2 * (d1 + d2), 4, -2, 6))
    return f

def g_par_perim(lo, hi):
    def f(r):
        a, b = r.randint(lo, hi), r.randint(lo, hi)
        if a == b: return None
        return lenm(f"In a parallelogram ABCD, $AB={a}$ cm and $BC={b}$ cm. Its perimeter is:", 2 * (a + b), "Opposite sides are equal.", offs=(a + b, a * b, 4, -4, 2, 10))
    return f

CONCEPT = [tx(q, c, w, why) for q, c, w, why in [
    ("A quadrilateral in which both pairs of opposite sides are parallel is a:", "parallelogram", ["trapezium", "kite", "triangle"], "Definition."),
    ("The diagonals of a rhombus:", "bisect each other at right angles", ["are equal", "do not intersect", "are parallel"], "Property of a rhombus."),
    ("A parallelogram with all four angles equal is a:", "rectangle", ["rhombus", "kite", "trapezium"], "Each angle is $90^\\circ$."),
    ("A quadrilateral whose diagonals are equal and bisect each other at right angles is a:", "square", ["rhombus that is not a square", "rectangle that is not a square", "kite"], "Both properties hold only for a square."),
    ("If one pair of opposite sides of a quadrilateral is equal and parallel, then it is a:", "parallelogram", ["trapezium only", "kite", "rhombus always"], "A test for a parallelogram."),
    ("The line segment joining the midpoints of two sides of a triangle is:", "parallel to the third side and half of it", ["equal to the third side", "perpendicular to the third side", "twice the third side"], "Midpoint theorem."),
    ("The diagonals of a rectangle:", "are equal and bisect each other", ["are perpendicular", "are unequal", "do not bisect each other"], "Property of a rectangle."),
    ("The sum of the interior angles of any quadrilateral is:", "$360^\\circ$", ["$180^\\circ$", "$270^\\circ$", "$540^\\circ$"], "Split into two triangles.")]]
CON2 = [tx(q, c, w, why) for q, c, w, why in [
    ("Which quadrilateral always has all four sides equal?", "rhombus", ["rectangle", "parallelogram", "kite"], "Definition of a rhombus."),
    ("The opposite angles of a parallelogram are:", "equal", ["supplementary always", "complementary", "unequal"], "Property."),
    ("Which of these has diagonals that are always perpendicular?", "rhombus", ["rectangle", "parallelogram", "trapezium"], "Property of rhombus."),
    ("Every square is a:", "rhombus and a rectangle", ["kite only", "trapezium only", "triangle"], "It has all properties of both.")]]

# =============================== EASY ===============================
EASY_A = [draw(100, 4, g_fourth(60, 120)), draw(101, 4, g_par_angle(50, 80)), draw(102, 4, g_par_perim(5, 15)), CON2, draw(103, 4, g_rect_diag([TRIP[0], TRIP[6]])), draw(104, 4, g_mid(8, 30)), CONCEPT[:4], draw(105, 4, g_square_diag(3, 12))]

def q_fourth(lo, hi):
    def f(r):
        a, b, c = R(r, lo, hi, 5), R(r, lo, hi, 5), R(r, lo, hi, 5); d = 360 - a - b - c
        if not 30 <= d < 180: return None
        return QQ(f"Three angles of a quadrilateral are {a}°, {b}° and {c}°. Find the fourth angle.", "Angle sum $=360^\\circ$", f"Sum of the three given angles $={a+b+c}^\\circ$", f"Fourth angle $=360^\\circ-{a+b+c}^\\circ={d}^\\circ$")
    return f
def q_para(lo, hi):
    def f(r):
        a = R(r, lo, hi, 2)
        if a == 90: return None
        return QQ(f"In a parallelogram ABCD, $\\angle A={a}^\\circ$. Find $\\angle B$, $\\angle C$ and $\\angle D$.", f"$\\angle C=\\angle A={a}^\\circ$ (opposite angles)", f"$\\angle B=180^\\circ-{a}^\\circ={180-a}^\\circ$ (adjacent angles)", f"$\\angle D=\\angle B={180-a}^\\circ$")
    return f
def q_ppar(lo, hi):
    def f(r):
        a, b = r.randint(lo, hi), r.randint(lo, hi)
        if a == b: return None
        return QQ(f"The adjacent sides of a parallelogram are {a} cm and {b} cm. Find the lengths of the other two sides and the perimeter.", f"Opposite sides are equal: other sides ${a}$ cm and ${b}$ cm", f"Perimeter $=2({a}+{b})={2*(a+b)}$ cm")
    return f
def q_rect(trs, ks):
    def f(r):
        a, b, c = r.choice(trs); k = r.choice(ks)
        return QQ(f"The sides of a rectangle are {a*k} cm and {b*k} cm. Find the length of its diagonal and its perimeter.", f"Diagonal $=\\sqrt{{{a*k}^2+{b*k}^2}}$", f"$=\\sqrt{{{(a*k)**2+(b*k)**2}}}={c*k}$ cm", f"Perimeter $=2({a*k}+{b*k})={2*(a+b)*k}$ cm")
    return f
def q_midp(lo, hi):
    def f(r):
        a, b, c = r.randint(lo, hi) * 2, r.randint(lo, hi) * 2, r.randint(lo, hi) * 2
        if a + b <= c or a + c <= b or b + c <= a: return None
        return QQ(f"In $\\triangle ABC$, $AB={a}$ cm, $BC={b}$ cm and $CA={c}$ cm. D, E, F are the midpoints of AB, BC and CA. Find the sides of $\\triangle DEF$ and its perimeter.", f"$EF={a//2}$ cm, $FD={b//2}$ cm, $DE={c//2}$ cm (midpoint theorem: each side is half the parallel side)", f"Perimeter $={a//2}+{b//2}+{c//2}={(a+b+c)//2}$ cm")
    return f
EASY_B = draw(110, 4, q_fourth(60, 120)) + draw(111, 4, q_para(40, 80)) + draw(112, 4, q_ppar(5, 15))
EASY_C = draw(113, 6, q_rect([TRIP[0], TRIP[6]], (1, 2, 3, 4))) + draw(114, 6, q_midp(5, 15)) + draw(115, 6, q_fourth(40, 130))
def q_rat():
    def f(r):
        p = [r.randint(1, 6) for _ in range(4)]
        if len(set(p)) < 3 or 360 % sum(p): return None
        u_ = 360 // sum(p)
        return QQ(f"The angles of a quadrilateral are in the ratio {':'.join(map(str, p))}. Find all four angles.", f"Sum of ratio terms $={sum(p)}$", f"One part $=360^\\circ\\div{sum(p)}={u_}^\\circ$", "Angles: " + ", ".join(f"${x*u_}^\\circ$" for x in p))
    return f
def q_rhomb(trs, ks):
    def f(r):
        a, b, c = r.choice(trs); k = r.choice(ks)
        return QQ(f"The diagonals of a rhombus are {2*a*k} cm and {2*b*k} cm. Find its side, perimeter and area.", "Diagonals bisect each other at right angles", f"Side $=\\sqrt{{{a*k}^2+{b*k}^2}}={c*k}$ cm", f"Perimeter $=4\\times{c*k}={4*c*k}$ cm", f"Area $=\\frac12\\times{2*a*k}\\times{2*b*k}={2*a*b*k*k}$ cm$^2$")
    return f
EASY_D = draw(116, 6, q_rat()) + draw(117, 6, q_rhomb([TRIP[0], TRIP[6]], (1, 2, 3, 4)))

# =============================== NCERT ===============================
NCERT_A = [draw(200, 4, g_ratio()), draw(201, 4, g_par_x(5, 30)), draw(202, 4, g_par_adj(2, 8)), draw(203, 4, g_diag_bis(2, 9)), CONCEPT[4:],
           draw(204, 4, g_rhomb_ang(40, 140)), draw(205, 4, g_mid_per(4, 20)), draw(206, 4, g_square_area(4, 15))]
def q_px(lo, hi):
    def f(r):
        x = r.randint(lo, hi); a = r.randint(2, 15); k = r.choice([2, 3, 4]); c = (k - 1) * x + a
        A = k * x + a
        if not 20 < A < 160 or A == 90: return None
        return QQ(f"The opposite angles of a parallelogram are $({k}x+{a})^\\circ$ and $(x+{c})^\\circ$. Find $x$ and all four angles.", "Opposite angles are equal", f"${k}x+{a}=x+{c}$ gives $x={x}$", f"Angles $A=C={A}^\\circ$", f"$B=D=180^\\circ-{A}^\\circ={180-A}^\\circ$")
    return f
def q_adjk(ks):
    def f(r):
        k = r.choice(ks)
        if 180 % (k + 1): return None
        d = 180 // (k + 1)
        return QQ(f"Two adjacent angles of a parallelogram are in the ratio 1 : {k}. Find all four angles.", f"Adjacent angles add up to $180^\\circ$: $x+{k}x=180^\\circ$", f"$x={d}^\\circ$ and the other is ${k*d}^\\circ$", f"Opposite angles are equal: the four angles are ${d}^\\circ, {k*d}^\\circ, {d}^\\circ, {k*d}^\\circ$")
    return f
NCERT_B = draw(210, 4, q_para(40, 130)) + draw(211, 4, q_rect([TRIP[1], TRIP[2]], (1, 2))) + draw(212, 4, q_midp(8, 25))
def q_diag(lo, hi):
    def f(r):
        x = r.randint(lo, hi); p, q = r.randint(2, 5), r.randint(1, 9)
        oa = p * x + q
        a2 = r.randint(1, 4); b2 = oa - a2 * x
        if b2 <= 0 or b2 == q: return None
        return QQ(f"The diagonals of a parallelogram ABCD meet at O. $OA=({p}x+{q})$ cm and $OC=({a2}x+{b2})$ cm. Find $x$ and the length of AC.", "Diagonals bisect each other, so $OA=OC$", f"${p}x+{q}={a2}x+{b2}$ gives $x={x}$", f"$OA={oa}$ cm", f"$AC=2\\times{oa}={2*oa}$ cm")
    return f
NCERT_C = draw(213, 6, q_px(4, 25)) + draw(214, 6, q_adjk((2, 3, 4, 5, 8, 9))) + draw(215, 6, q_diag(2, 9))
def q_mid_conv(r):
    bc = r.randint(6, 20) * 2; de = bc // 2; ab = r.randint(8, 24) * 2
    return QQ(f"In $\\triangle ABC$, D is the midpoint of AB and the line through D parallel to BC meets AC at E. $BC={bc}$ cm and $AB={ab}$ cm. Find $DE$, $AD$ and show that E is the midpoint of AC.", f"$AD={ab//2}$ cm (D is the midpoint)", f"By the converse of the midpoint theorem, E is the midpoint of AC", f"$DE=\\frac12BC={de}$ cm", "Hence $AE=EC$")
def q_var(r):
    d1, d2 = r.randint(8, 30), r.randint(8, 30)
    return QQ(f"The diagonals of a quadrilateral ABCD are AC = {d1} cm and BD = {d2} cm. P, Q, R, S are the midpoints of AB, BC, CD, DA. Show that PQRS is a parallelogram and find its perimeter.", "In $\\triangle ABC$, $PQ\\parallel AC$ and $PQ=\\frac12AC$; in $\\triangle ADC$, $SR\\parallel AC$ and $SR=\\frac12AC$", "So $PQ\\parallel SR$ and $PQ=SR$: a pair of opposite sides equal and parallel, so PQRS is a parallelogram", f"$PQ=SR={d1/2:g}$ cm and $QR=PS={d2/2:g}$ cm", f"Perimeter $={d1}+{d2}={d1+d2}$ cm")
NCERT_D = draw(216, 6, q_mid_conv) + draw(217, 6, q_var)

# =============================== MEDIUM ===============================
MED_A = [draw(300, 4, g_ratio()), draw(301, 4, g_par_diff(10, 80)), draw(302, 4, g_rect_area([TRIP[1], TRIP[2]])), draw(303, 4, g_rhomb_per([TRIP[1], TRIP[2], TRIP[3]])),
         draw(304, 4, g_rhomb_area([TRIP[1], TRIP[2], TRIP[3]])), draw(305, 4, g_varignon(10, 40)), draw(306, 4, g_par_x(31, 60)), draw(307, 4, g_mid(20, 60))]
def q_diffk(lo, hi):
    def f(r):
        d = R(r, lo, hi, 10)
        return QQ(f"One angle of a parallelogram is {d}° more than its adjacent angle. Find all the angles.", f"Let the angles be $x$ and $x+{d}$; adjacent angles sum to $180^\\circ$", f"$2x+{d}=180$ gives $x={(180-d)//2}$", f"Angles: ${(180-d)//2}^\\circ, {(180+d)//2}^\\circ, {(180-d)//2}^\\circ, {(180+d)//2}^\\circ$") if (180 - d) % 2 == 0 else None
    return f
def q_rectarea(trs, ks):
    def f(r):
        a, b, c = r.choice(trs); k = r.choice(ks)
        return QQ(f"A rectangle has a diagonal of {c*k} cm and one side {a*k} cm. Find its other side, area and perimeter.", f"Other side $=\\sqrt{{{c*k}^2-{a*k}^2}}={b*k}$ cm", f"Area $={a*k}\\times{b*k}={a*b*k*k}$ cm$^2$", f"Perimeter $=2({a*k}+{b*k})={2*(a+b)*k}$ cm")
    return f
def q_rhomb_ang(lo, hi):
    def f(r):
        a = R(r, lo, hi, 2)
        if a == 90: return None
        return QQ(f"In rhombus ABCD, $\\angle A={a}^\\circ$. Find $\\angle B$, and the angles $\\angle OAB$ and $\\angle OBA$ where O is the point of intersection of the diagonals.", f"$\\angle B=180^\\circ-{a}^\\circ={180-a}^\\circ$", f"Diagonal AC bisects $\\angle A$: $\\angle OAB={a/2:g}^\\circ$", f"$\\angle OBA=\\frac12\\angle B={(180-a)/2:g}^\\circ$", f"In $\\triangle AOB$: $\\angle AOB=180^\\circ-{a/2:g}^\\circ-{(180-a)/2:g}^\\circ=90^\\circ$ (diagonals are perpendicular)")
    return f
MED_B = draw(310, 4, q_diffk(10, 80)) + draw(311, 4, q_rectarea([TRIP[1], TRIP[2], TRIP[3]], (1, 2))) + draw(312, 4, q_rhomb([TRIP[1], TRIP[2], TRIP[3]], (1, 2)))
def q_sqd(lo, hi):
    def f(r):
        d = r.randint(lo, hi) * 2
        return QQ(f"The diagonal of a square is {d} cm. Find its area and its side in terms of $\\sqrt2$.", f"Area $=\\frac12d^2=\\frac12\\times{d}^2={d*d//2}$ cm$^2$", f"Side$^2={d*d//2}$", f"Side $={d//2}\\sqrt2$ cm")
    return f
def q_triang_mid(lo, hi):
    def f(r):
        a, b, c = r.randint(lo, hi) * 2, r.randint(lo, hi) * 2, r.randint(lo, hi) * 2
        if a + b <= c or a + c <= b or b + c <= a: return None
        return QQ(f"The perimeter of $\\triangle ABC$ is {a+b+c} cm. D, E, F are the midpoints of its sides. Find the perimeter of $\\triangle DEF$ and the length of each of its sides in terms of the sides of $\\triangle ABC$.", "Midpoint theorem on each pair of sides", f"$DE=\\frac12AC$, $EF=\\frac12AB$, $FD=\\frac12BC$", f"Perimeter of $\\triangle DEF=\\frac12({a+b+c})={(a+b+c)//2}$ cm")
    return f
def q_par_exp(lo, hi):
    def f(r):
        x = r.randint(lo, hi); a, b = r.randint(1, 9), r.randint(1, 9); k = r.choice([2, 3])
        c = (k - 1) * x + a
        AB, CD, BC = k * x + a, x + c, x + b
        return QQ(f"In parallelogram ABCD, $AB=({k}x+{a})$ cm, $CD=(x+{c})$ cm and $BC=(x+{b})$ cm. Find $x$, the sides and the perimeter.", "Opposite sides are equal: $AB=CD$", f"${k}x+{a}=x+{c}$ gives $x={x}$", f"$AB=CD={AB}$ cm and $BC=AD={x+b}$ cm", f"Perimeter $=2({AB}+{x+b})={2*(AB+x+b)}$ cm")
    return f
MED_C = draw(313, 6, q_sqd(4, 20)) + draw(314, 6, q_rhomb_ang(40, 140)) + draw(315, 6, q_par_exp(2, 12))
def q_rectangle_proof(r):
    a, b = r.randint(6, 15), r.randint(6, 15)
    if a == b: return None
    d2 = a * a + b * b
    return QQ(f"ABCD is a parallelogram with $AB={a}$ cm, $AD={b}$ cm and diagonal $AC$ with $AC^2={d2}$ cm$^2$. Show that ABCD is a rectangle.", f"In $\\triangle ABC$, $AB^2+BC^2={a*a}+{b*b}={d2}$ (as $BC=AD={b}$)", f"This equals $AC^2$, so $\\angle B=90^\\circ$ (converse of the Baudhāyana–Pythagoras theorem)", "A parallelogram with one right angle has all angles $90^\\circ$", "Hence ABCD is a rectangle")
MED_D = draw(316, 6, q_rectangle_proof) + draw(317, 6, q_triang_mid(5, 20))

# =============================== HARD ===============================
def g_ap_ang(ds):
    def f(r):
        d = r.choice(ds); a = (360 - 6 * d) // 4
        if (360 - 6 * d) % 4 or a <= 0: return None
        return ang(f"The four angles of a quadrilateral are in AP with common difference ${d}^\\circ$. The smallest angle is:", a, "Angles $a, a+d, a+2d, a+3d$ add up to $360^\\circ$.", offs=(d, -d, 10, 20, -10, 15))
    return f
def g_rect_ratio(ks):
    def f(r):
        k = r.choice(ks)
        return lenm(f"The sides of a rectangle are in the ratio $3:4$ and its diagonal is ${5*k}$ cm. Its perimeter is:", 14 * k, f"Sides ${3*k}$ cm and ${4*k}$ cm.", offs=(7 * k, k, 5 * k, 2, -2, 10))
    return f
def g_sq_per(ks):
    def f(r):
        k = r.choice(ks)
        return lenm(f"The diagonal of a square is ${k}\\sqrt2$ cm. Its perimeter is:", 4 * k, f"Side $={k}$ cm.", offs=(2 * k, k, 8, -4, 2 * k + 4, 10))
    return f
def g_rh_other(trs):
    def f(r):
        a, b, c = r.choice(trs); k = r.randint(1, 3)
        return lenm(f"A rhombus has side ${c*k}$ cm and one diagonal ${2*a*k}$ cm. The other diagonal is:", 2 * b * k, f"Half-diagonals and the side form a right triangle: half of the other diagonal $=\\sqrt{{{c*k}^2-{a*k}^2}}={b*k}$.", offs=(b * k, 2, -2, 4, 6, a * k))
    return f
HARD_A = [draw(400, 4, g_ap_ang((10, 20, 30, 40, 50, 14, 16, 22, 26))), draw(401, 4, g_rect_ratio((2, 3, 4, 5, 6, 7, 8))), draw(402, 4, g_sq_per((6, 7, 9, 11, 12, 13, 15, 18))), draw(403, 4, g_rh_other([TRIP[1], TRIP[2], TRIP[3], TRIP[5]])),
          draw(404, 4, g_rhomb_area([TRIP[3], TRIP[4], TRIP[5]])), draw(405, 4, g_rect_area([TRIP[3], TRIP[4], TRIP[5]])), draw(406, 4, g_par_x(61, 120)), draw(407, 4, g_varignon(41, 120))]
def q_rh_other(trs, ks):
    def f(r):
        a, b, c = r.choice(trs); k = r.choice(ks)
        return QQ(f"A rhombus has side {c*k} cm and one diagonal {2*a*k} cm. Find the other diagonal, its area and the distance between a pair of opposite sides (height), correct to two decimal places.", f"Half of the given diagonal $={a*k}$ cm", f"Half of the other diagonal $=\\sqrt{{{c*k}^2-{a*k}^2}}={b*k}$ cm, so the diagonal is ${2*b*k}$ cm", f"Area $=\\frac12\\times{2*a*k}\\times{2*b*k}={2*a*b*k*k}$ cm$^2$", f"Height $=\\dfrac{{\\text{{area}}}}{{\\text{{side}}}}=\\dfrac{{{2*a*b*k*k}}}{{{c*k}}}={2*a*b*k*k/(c*k):.2f}$ cm")
    return f
def q_rect_mid(trs, ks):
    def f(r):
        a, b, c = r.choice(trs); k = r.choice(ks)
        return QQ(f"The midpoints of the sides of a rectangle {2*a*k} cm by {2*b*k} cm are joined in order. Show that the figure formed is a rhombus and find its perimeter and area.", "Each side of the new figure is half a diagonal of the rectangle (midpoint theorem), and the diagonals of a rectangle are equal, so all four sides are equal", f"Diagonal of the rectangle $=\\sqrt{{{(2*a*k)**2}+{(2*b*k)**2}}}={2*c*k}$ cm, so each side $={c*k}$ cm", f"Perimeter $=4\\times{c*k}={4*c*k}$ cm", f"Its diagonals are the sides of the rectangle, so area $=\\frac12\\times{2*a*k}\\times{2*b*k}={2*a*b*k*k}$ cm$^2$")
    return f
def q_rh_proof(trs, ks):
    def f(r):
        a, b, c = r.choice(trs); k = r.choice(ks)
        return QQ(f"In a parallelogram ABCD the diagonals meet at O with $OA={a*k}$ cm, $OB={b*k}$ cm and $AB={c*k}$ cm. Show that ABCD is a rhombus and find its perimeter.", "Diagonals of a parallelogram bisect each other, so $OA=OC$ and $OB=OD$", f"$OA^2+OB^2={(a*k)**2}+{(b*k)**2}={(c*k)**2}=AB^2$", "By the converse of the Baudhāyana–Pythagoras theorem, $\\angle AOB=90^\\circ$, so the diagonals are perpendicular", "A parallelogram with perpendicular diagonals is a rhombus, so all sides equal", f"Perimeter $=4\\times{c*k}={4*c*k}$ cm")
    return f
def q_apang(ds):
    def f(r):
        d = r.choice(ds); a = (360 - 6 * d) // 4
        if (360 - 6 * d) % 4 or a <= 0: return None
        return QQ(f"The angles of a quadrilateral are in AP with common difference {d}°. Find all four angles and say whether a pair of them is supplementary.", f"Let the angles be $a, a+{d}, a+{2*d}, a+{3*d}$", f"$4a+{6*d}=360$ gives $a={a}$", f"Angles: ${a}^\\circ, {a+d}^\\circ, {a+2*d}^\\circ, {a+3*d}^\\circ$", f"${a}^\\circ+{a+3*d}^\\circ={2*a+3*d}^\\circ$ (and ${a+d}^\\circ+{a+2*d}^\\circ$ also ${2*a+3*d}^\\circ$), so they are supplementary")
    return f
HARD_B = draw(410, 4, q_rh_other([TRIP[1], TRIP[2], TRIP[3], TRIP[5]], (1, 2, 3))) + draw(411, 4, q_apang((10, 20, 30, 40, 50, 14, 16, 22, 26))) + draw(412, 4, q_par_exp(13, 40))
HARD_C = draw(413, 6, q_diag(10, 40)) + draw(414, 6, q_rhomb_ang(34, 146)) + draw(415, 6, q_mid_conv)
HARD_D = draw(416, 6, q_rect_mid([TRIP[1], TRIP[2], TRIP[3], TRIP[4]], (1, 2, 3))) + draw(417, 6, q_rh_proof([TRIP[0], TRIP[1], TRIP[2], TRIP[3], TRIP[4], TRIP[5]], (1, 2, 3)))

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
