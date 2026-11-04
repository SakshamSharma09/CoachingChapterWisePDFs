"""Class 10 Maths Ch 11 - Areas Related to Circles (graded banks). pi = 22/7; segments only for 60/90/120 degrees; sqrt3 = 1.73 where needed."""
from c10m_x import *

SLUG, NAME, CHNO = "Areas_Related_to_Circles", "Areas Related to Circles", 11
PI = F(22, 7)
R3 = F(173, 100)

def Af(u): return lambda x: f"{nd(x)} {u}²"
def Lf(u): return lambda x: f"{nd(x)} {u}"
def A2(u): return lambda x: f"{rnd2(x)} {u}²"
def Df(x): return f"${nd(x)}^\\circ$"
def Nf(x): return nd(x)
def sc(stem0, ask, ans, ex, parts, fmt):
    ans = ans if isinstance(ans, list) else [ans]
    w = nums_near(ans[0], ex) if len(ans) == 1 else []
    return SCG(stem0, ask, ans, w, parts, fmt)
def ts(x): return t(x) if F(x).denominator == 1 else nd(x)   # plain number inside tex

def c_area(r, u="cm"):
    v = PI * r * r
    return sc(f"The radius of a circle is {nd(r)} {u}.", "area of the circle", v, [PI * r, 2 * PI * r, PI * r * r * 2], ["Area of a circle $=\\pi r^2$", f"$\\frac{{22}}{{7}}\\times{ts(r)}\\times{ts(r)}$", f"Area $={nd(v)}$ {u}$^2$"], Af(u))
def c_circ(r, u="cm"):
    v = 2 * PI * r
    return sc(f"The radius of a circle is {nd(r)} {u}.", "circumference of the circle", v, [PI * r, PI * r * r, 4 * PI * r], ["Circumference $=2\\pi r$", f"$2\\times\\frac{{22}}{{7}}\\times{ts(r)}$", f"Circumference $={nd(v)}$ {u}"], Lf(u))
def r_circ(C, u="cm"):
    r = F(C) / (2 * PI)
    return sc(f"The circumference of a circle is {nd(C)} {u}.", "radius of the circle", r, [C / PI, F(C) / (4 * PI), r * 2], ["Circumference $=2\\pi r$", f"$r=\\frac{{{nd(C)}\\times7}}{{2\\times22}}$", f"$r={nd(r)}$ {u}"], Lf(u))
def r_area(A, u="cm"):
    r2 = F(A) / PI; r = F(isqrt(r2.numerator), isqrt(r2.denominator)); assert r * r == r2, A
    return sc(f"The area of a circle is {nd(A)} {u}$^2$.", "radius of the circle", r, [r2, r * 2, F(A) / (2 * PI)], ["Area $=\\pi r^2$", f"$r^2=\\frac{{{nd(A)}\\times7}}{{22}}={nd(r2)}$", f"$r={nd(r)}$ {u}"], Lf(u))
def arc(r, th, u="cm"):
    v = F(th, 360) * 2 * PI * r
    return sc(f"A sector of a circle of radius {nd(r)} {u} has central angle ${th}^\\circ$.", "length of its arc", v, [F(th, 360) * PI * r * r, F(th, 180) * 2 * PI * r, v + 2 * r], ["Arc length $=\\frac{\\theta}{360}\\times2\\pi r$", f"$\\frac{{{th}}}{{360}}\\times2\\times\\frac{{22}}{{7}}\\times{ts(r)}$", f"Arc $={nd(v)}$ {u}"], Lf(u))
def sec_area(r, th, u="cm"):
    v = F(th, 360) * PI * r * r
    return sc(f"A sector of a circle of radius {nd(r)} {u} has central angle ${th}^\\circ$.", "area of the sector", v, [F(th, 360) * 2 * PI * r, PI * r * r, v * 2], ["Area of sector $=\\frac{\\theta}{360}\\times\\pi r^2$", f"$\\frac{{{th}}}{{360}}\\times\\frac{{22}}{{7}}\\times{ts(r)}^2$", f"Area $={nd(v)}$ {u}$^2$"], Af(u))
def sec_perim(r, th, u="cm"):
    v = F(th, 360) * 2 * PI * r + 2 * r
    return sc(f"A sector of a circle of radius {nd(r)} {u} has central angle ${th}^\\circ$.", "perimeter of the sector", v, [F(th, 360) * 2 * PI * r, v + r, F(th, 360) * 2 * PI * r + r], ["Perimeter $=$ arc $+\\,2r$", f"Arc $=\\frac{{{th}}}{{360}}\\times2\\pi\\times{ts(r)}={nd(F(th,360)*2*PI*r)}$ {u}", f"Perimeter $={nd(F(th,360)*2*PI*r)}+{ts(2*r)}={nd(v)}$ {u}"], Lf(u))
def ang_arc(r, L, u="cm"):
    th = F(L) * 360 / (2 * PI * r); assert th.denominator == 1
    return sc(f"An arc of length {nd(L)} {u} subtends an angle at the centre of a circle of radius {nd(r)} {u}.", "angle subtended by the arc at the centre", th, [th * 2, th / 2 if th % 2 == 0 else th + 10, 180 - th], ["Arc $=\\frac{\\theta}{360}\\times2\\pi r$", f"$\\theta=\\frac{{{nd(L)}\\times360}}{{2\\times\\frac{{22}}{{7}}\\times{ts(r)}}}$", f"$\\theta={nd(th)}^\\circ$"], Df)
def ang_area(r, A, u="cm"):
    th = F(A) * 360 / (PI * r * r); assert th.denominator == 1
    return sc(f"The area of a sector of a circle of radius {nd(r)} {u} is {nd(A)} {u}$^2$.", "central angle of the sector", th, [th * 2, th + 30, 180 - th], ["Sector area $=\\frac{\\theta}{360}\\times\\pi r^2$", f"$\\theta=\\frac{{{nd(A)}\\times360}}{{\\frac{{22}}{{7}}\\times{ts(r)}^2}}$", f"$\\theta={nd(th)}^\\circ$"], Df)
def seg90(r, u="cm"):
    sec = PI * r * r / 4; tri = F(r * r, 2); v = sec - tri
    return sc(f"A chord of a circle of radius {nd(r)} {u} subtends a right angle at the centre.", "area of the minor segment", v, [sec, tri, v + tri / 2], ["Segment $=$ sector $-$ triangle", f"Sector $={nd(sec)}$ {u}$^2$, triangle $=\\frac12\\times{ts(r)}\\times{ts(r)}={nd(tri)}$ {u}$^2$", f"Segment $={nd(sec)}-{nd(tri)}={nd(v)}$ {u}$^2$"], Af(u))
def seg(r, th, u="cm"):
    assert th in (60, 120)
    sec = F(th, 360) * PI * r * r; tri = R3 * r * r / 4 if th == 60 else R3 * r * r / 4
    v = sec - tri
    return sc(f"A chord of a circle of radius {nd(r)} {u} subtends an angle of ${th}^\\circ$ at the centre. (Use $\\pi=\\frac{{22}}{{7}}$ and $\\sqrt3=1.73$; answer to two decimal places.)", "area of the minor segment", v, [sec, tri, sec + tri], ["Segment $=$ sector $-$ triangle", f"Sector $={rnd2(sec)}$ {u}$^2$; triangle $=\\frac{{\\sqrt3}}{{4}}r^2={rnd2(tri)}$ {u}$^2$" if th == 60 else f"Sector $={rnd2(sec)}$ {u}$^2$; triangle with sides $r$, $r$ and angle ${th}^\\circ$ has area $\\frac12r^2\\sin{th}^\\circ=\\frac{{\\sqrt3}}{{4}}r^2={rnd2(tri)}$ {u}$^2$", f"Segment $={rnd2(sec)}-{rnd2(tri)}={rnd2(v)}$ {u}$^2$"], A2(u))
def semi_perim(r, u="cm"):
    v = PI * r + 2 * r
    return sc(f"A semicircular protractor-shaped plate has radius {nd(r)} {u}.", "perimeter of the plate", v, [PI * r, 2 * PI * r + 2 * r, PI * r + r], ["Perimeter $=$ semicircular arc $+$ diameter", f"Arc $=\\pi r={nd(PI*r)}$ {u}; diameter $={nd(2*r)}$ {u}", f"Perimeter $={nd(v)}$ {u}"], Lf(u))
def quad_perim(r, u="cm"):
    v = PI * r / 2 + 2 * r
    return sc(f"A quadrant of a circle has radius {nd(r)} {u}.", "perimeter of the quadrant", v, [PI * r / 2, PI * r + 2 * r, PI * r / 2 + r], ["Perimeter $=$ quarter arc $+\\,2r$", f"Quarter arc $=\\frac{{\\pi r}}{{2}}={nd(PI*r/2)}$ {u}; $2r={nd(2*r)}$ {u}", f"Perimeter $={nd(v)}$ {u}"], Lf(u))
def sq_circ(s, u="cm"):
    v = F(s) ** 2 - PI * F(s) ** 2 / 4
    return sc(f"The largest possible circle is cut from a square sheet of side {nd(s)} {u}.", "area of the sheet left over", v, [PI * F(s) ** 2 / 4, F(s) ** 2, F(s) ** 2 - PI * F(s) ** 2 / 2], ["The largest circle has diameter equal to the side, so $r=\\frac{s}{2}$", f"Circle area $=\\frac{{22}}{{7}}\\times{ts(F(s)/2)}^2={nd(PI*F(s)**2/4)}$ {u}$^2$; square $={nd(F(s)**2)}$ {u}$^2$", f"Left over $={nd(v)}$ {u}$^2$"], Af(u))
def circ_sq(r, u="cm"):
    v = PI * r * r - 2 * r * r
    return sc(f"A square is inscribed in a circle of radius {nd(r)} {u}.", "area of the circle outside the square", v, [PI * r * r, 2 * r * r, PI * r * r - 4 * r * r], ["The diagonal of the square is the diameter $2r$, so its area is $\\frac{(2r)^2}{2}=2r^2$", f"Circle $={nd(PI*r*r)}$ {u}$^2$; square $={nd(2*r*r)}$ {u}$^2$", f"Difference $={nd(v)}$ {u}$^2$"], Af(u))
def path(r, w, u="m"):
    R = r + w; v = PI * (R * R - r * r)
    return sc(f"A circular park of radius {nd(r)} {u} is surrounded by a path {nd(w)} {u} wide.", "area of the path", v, [PI * w * 2 * r, v * 2, v / 2], [f"Outer radius $={nd(R)}$ {u}", f"Area $=\\pi(R^2-r^2)=\\frac{{22}}{{7}}({nd(R)}^2-{nd(r)}^2)$", f"Area of path $={nd(v)}$ {u}$^2$"], Af(u))
def sec_diff(R, r, th):
    v = F(th, 360) * PI * (R * R - r * r)
    return sc(f"Two concentric circles have radii {R} cm and {r} cm. A sector of angle ${th}^\\circ$ is marked in both.", "area of the region between the two arcs within the sector", v, [PI * (R * R - r * r), v * 2, v / 2], ["Required area $=\\frac{\\theta}{360}\\times\\pi(R^2-r^2)$", f"$\\frac{{{th}}}{{360}}\\times\\frac{{22}}{{7}}\\times({R}^2-{r}^2)$", f"Area $={nd(v)}$ cm$^2$"], Af("cm"))
def clock_area(r, tm):
    v = F(tm, 60) * PI * r * r
    return sc(f"The minute hand of a clock is {nd(r)} cm long.", f"area swept by the minute hand in {tm} minutes", v, [F(tm, 60) * 2 * PI * r, PI * r * r, F(tm, 30) * PI * r * r], [f"In {tm} minutes the hand turns through $6^\\circ\\times{tm}={6*tm}^\\circ$", f"Area $=\\frac{{{6*tm}}}{{360}}\\times\\frac{{22}}{{7}}\\times{ts(r)}^2$", f"Area $={nd(v)}$ cm$^2$"], Af("cm"))
def clock_tip(r, tm):
    v = F(tm, 60) * 2 * PI * r
    return sc(f"The minute hand of a clock is {nd(r)} cm long.", f"distance moved by its tip in {tm} minutes", v, [F(tm, 60) * PI * r * r, 2 * PI * r, F(tm, 30) * 2 * PI * r], [f"Angle turned in {tm} minutes $={6*tm}^\\circ$", f"Arc $=\\frac{{{6*tm}}}{{360}}\\times2\\times\\frac{{22}}{{7}}\\times{ts(r)}$", f"Distance $={nd(v)}$ cm"], Lf("cm"))
def cow(r, th=90):
    v = F(th, 360) * PI * r * r
    where = "at a corner of" if th == 90 else "at the midpoint of one side of"
    return sc(f"A horse is tied {where} a large square field with a rope {nd(r)} m long.", "area of the field it can graze", v, [PI * r * r, v * 2, F(th, 360) * 2 * PI * r], [f"The horse can graze a sector of angle ${th}^\\circ$ and radius {nd(r)} m", f"Area $=\\frac{{{th}}}{{360}}\\times\\frac{{22}}{{7}}\\times{ts(r)}^2$", f"Area $={nd(v)}$ m$^2$"], Af("m"))
def cow_inc(r1, r2):
    v = PI * (r2 * r2 - r1 * r1) / 4
    return sc(f"A horse is tied at a corner of a large square field. The rope is first {r1} m long and then lengthened to {r2} m.", "increase in the area it can graze", v, [PI * r2 * r2 / 4, PI * (r2 - r1) ** 2 / 4, PI * (r2 * r2 - r1 * r1)], ["Grazed area is a quadrant: $\\frac14\\pi r^2$", f"Increase $=\\frac14\\times\\frac{{22}}{{7}}({r2}^2-{r1}^2)$", f"Increase $={nd(v)}$ m$^2$"], Af("m"))
def wheel(r, D):
    C = 2 * PI * r; n = F(D * 100) / C; assert n.denominator == 1
    return sc(f"A wheel has radius {nd(r)} cm.", f"number of complete revolutions it makes to cover {D} m", n, [n * 2, n + 10, F(D * 100) / (PI * r)], [f"Circumference $=2\\times\\frac{{22}}{{7}}\\times{ts(r)}={nd(C)}$ cm", f"Distance ${D}$ m $={D*100}$ cm; revolutions $=\\frac{{{D*100}}}{{{nd(C)}}}$", f"Revolutions $={nd(n)}$"], Nf)
def fence(r, rate):
    C = 2 * PI * r; v = C * rate
    return sc(f"A circular field has radius {nd(r)} m. Fencing costs ₹ {rate} per metre.", "cost (in ₹) of fencing the field once", v, [C, PI * r * r * rate, C * rate / 2], [f"Circumference $=2\\pi r=2\\times\\frac{{22}}{{7}}\\times{ts(r)}={nd(C)}$ m", f"Cost $={nd(C)}\\times{rate}$", f"Cost $=$ ₹ {nd(v)}"], lambda x: f"₹ {nd(x)}")
def wire_sq(r):
    side = 2 * PI * r / 4; v = side * side
    return sc(f"A wire in the form of a circle of radius {nd(r)} cm is bent into a square.", "area of the square", v, [side, 4 * v, PI * r * r], [f"Perimeter of the square $=$ circumference $=2\\pi r={nd(2*PI*r)}$ cm", f"Side $={nd(2*PI*r)}\\div4={nd(side)}$ cm", f"Area $={nd(side)}^2={nd(v)}$ cm$^2$"], Af("cm"))
def sum_r(r1, r2):
    r = r1 + r2
    return sc(f"The radii of two circles are {r1} cm and {r2} cm.", "radius of the circle whose circumference equals the sum of their circumferences", r, [isqrt(r1 * r1 + r2 * r2) if isqrt(r1 * r1 + r2 * r2) ** 2 == r1 * r1 + r2 * r2 else r + 2, r2 - r1, 2 * r], ["Let the new radius be $R$; $2\\pi R=2\\pi r_1+2\\pi r_2$", f"$R=r_1+r_2={r1}+{r2}$", f"$R={r}$ cm"], Lf("cm"))
def sum_a(r1, r2):
    r = isqrt(r1 * r1 + r2 * r2); assert r * r == r1 * r1 + r2 * r2
    return sc(f"The radii of two circles are {r1} cm and {r2} cm.", "radius of the circle whose area equals the sum of their areas", r, [r1 + r2, r2 - r1, r + 2], ["Let the new radius be $R$; $\\pi R^2=\\pi r_1^2+\\pi r_2^2$", f"$R^2={r1}^2+{r2}^2={r1*r1+r2*r2}$", f"$R={r}$ cm"], Lf("cm"))
def umbrella(r, n):
    v = PI * r * r / n
    return sc(f"An umbrella has {n} ribs which are equally spaced and the umbrella, when opened flat, is a circle of radius {nd(r)} cm.", "area between two consecutive ribs", v, [PI * r * r, PI * r * r / (n - 1), 2 * PI * r / n], [f"The {n} ribs divide the circle into {n} equal sectors", f"Area of the circle $=\\frac{{22}}{{7}}\\times{ts(r)}^2={nd(PI*r*r)}$ cm$^2$", f"Area between ribs $={nd(PI*r*r)}\\div{n}={nd(v)}$ cm$^2$"], Af("cm"))
def brooch(d, n):
    r = F(d, 2); v = 2 * PI * r + n * d
    return sc(f"A brooch is a circular piece of silver wire of diameter {d} mm. The wire is also used for {n} equal diameters that divide the brooch into {2*n} sectors.", "total length of wire required (in mm)", v, [2 * PI * r, PI * r * r, 2 * PI * r + n * r], ["Wire $=$ circumference $+$ the diameters", f"Circumference $=\\pi d={nd(PI*d)}$ mm; diameters $={n}\\times{d}={n*d}$ mm", f"Total $={nd(v)}$ mm"], Lf("mm"))
def lens_sq(s):
    v = F(s) ** 2 - PI * F(s) ** 2 / 4
    return sc(f"A quadrant of a circle of radius {s} cm is cut from a square of side {s} cm, with the centre of the quadrant at one corner of the square.", "area of the remaining part of the square", v, [PI * F(s) ** 2 / 4, F(s) ** 2, F(s) ** 2 - PI * F(s) ** 2 / 2], ["The quadrant has radius $s$, so its area is $\\frac14\\pi s^2$", f"Quadrant $={nd(PI*F(s)**2/4)}$ cm$^2$; square $={nd(F(s)**2)}$ cm$^2$", f"Remaining $={nd(v)}$ cm$^2$"], Af("cm"))
def semi_area(r, u="cm"):
    v = PI * r * r / 2
    return sc(f"A semicircle has radius {nd(r)} {u}.", "area of the semicircle", v, [PI * r * r, PI * r, PI * r * r / 4], ["Area of semicircle $=\\frac12\\pi r^2$", f"$\\frac12\\times\\frac{{22}}{{7}}\\times{ts(r)}^2$", f"Area $={nd(v)}$ {u}$^2$"], Af(u))

# ================= EASY =================
eA = [[MC(c_area(r)) for r in (7, 14, 21, 28, 35)],
      [MC(c_circ(r)) for r in (7, 14, 21, 35, 42)],
      [MC(r_circ(C)) for C in (44, 88, 132, 176, 22)],
      [MC(r_area(A)) for A in (154, 616, 1386, 2464, 3850)],
      [MC(sec_area(21, th)) for th in (60, 90, 120, 180, 30)],
      [MC(arc(21, th)) for th in (60, 90, 120, 180, 30)],
      [MC(semi_perim(r)) for r in (7, 14, 21, 35, 28)],
      [MC(quad_perim(r)) for r in (7, 14, 21, 35, 28)]]
eB = ([SQ(c_area(r, "m"), 2) for r in (F(7, 2), F(21, 2), F(35, 2), F(49, 2))] + [SQ(c_circ(r, "m"), 2) for r in (F(7, 2), F(21, 2), F(35, 2), F(49, 2))]
      + [SQ(sec_area(21, th), 2) for th in (45, 72, 150, 40)])
eC = ([SQ(arc(21, th), 3) for th in (45, 72, 150, 108, 36, 24)] + [SQ(sec_perim(21, th), 3) for th in (60, 90, 120, 30, 180, 150)] + [SQ(semi_area(r), 3) for r in (7, 14, 21, 28, 35, 42)])
eD = [SQ(path(r, w), 5) for r, w in ((14, 7), (21, 7), (28, 7), (35, 7), (14, 14), (7, 7))] + [SQ(sq_circ(s), 5) for s in (14, 28, 42, 21, 35, 7)]

# ================= NCERT =================
nA = [[MC(fence(r, rate)) for r, rate in ((14, 10), (21, 5), (35, 4), (28, 15), (42, 8))],
      [MC(wheel(r, D)) for r, D in ((21, 66), (35, 110), (14, 44), (28, 88), (21, 132))],
      [MC(sum_r(r1, r2)) for r1, r2 in ((19, 9), (8, 6), (12, 5), (15, 7), (10, 4))],
      [MC(sum_a(r1, r2)) for r1, r2 in ((6, 8), (5, 12), (9, 12), (7, 24), (20, 21))],
      [MC(clock_area(21, tm)) for tm in (5, 10, 15, 20, 25)],
      [MC(cow(r)) for r in (7, 14, 21, 28, 35)],
      [MC(ang_area(21, A)) for A in (F(231), F(693, 2), F(231, 2), F(462), F(693))]]
nB = ([SQ(clock_tip(14, tm), 2) for tm in (15, 30, 45, 9)] + [SQ(wire_sq(r), 2) for r in (14, 28, 35, 42)] + [SQ(cow_inc(r1, r2), 2) for r1, r2 in ((7, 14), (14, 21), (7, 21), (14, 28))])
nC = ([SQ(seg90(r), 3) for r in (7, 14, 21, 28, 35, 42)] + [SQ(sec_perim(14, th), 3) for th in (90, 180, 45, 270, 135, 225)] + [SQ(umbrella(r, n), 3) for r, n in ((28, 8), (21, 6), (35, 10), (42, 12), (14, 4), (56, 16))])
nD = [SQ(seg(r, th), 5) for r, th in ((14, 60), (21, 60), (28, 60), (14, 120), (21, 120), (28, 120))] + [SQ(brooch(d, n), 5) for d, n in ((35, 5), (28, 4), (42, 6))] + [SQ(circ_sq(r), 5) for r in (7, 14, 21)]

# ================= MEDIUM =================
h2 = lambda n: F(n, 2)
mA = [[MC(circ_sq(r)) for r in (7, 14, 21, 28, h2(21))],
      [MC(sq_circ(s)) for s in (56, 70, 49, 63, 84)],
      [MC(path(r, w)) for r, w in ((20, 7), (15, 7), (30, 7), (40, 7), (25, h2(7)))],
      [MC(sec_diff(14, 7, th)) for th in (60, 120, 90, 30, 180)],
      [MC(ang_arc(14, L)) for L in (22, 11, 44, 33, 55)],
      [MC(seg90(r)) for r in (49, 56, 63, 70, 77)],
      [MC(wire_sq(r)) for r in (21, 35, 49, 56, 63)],
      [MC(lens_sq(s)) for s in (14, 28, 35, 42, 56)]]
mB = ([SQ(clock_area(28, tm), 2) for tm in (15, 30, 45, 9)] + [SQ(cow(r, 180), 2) for r in (14, 21, 28, 7)] + [SQ(wheel(r, D), 2) for r, D in ((35, 55), (14, 88), (7, 22), (28, 88))])
mC = ([SQ(fence(r, rate), 3) for r, rate in ((14, 12), (21, 9), (35, 6), (28, 11), (42, 7), (49, 5))] + [SQ(sum_r(r1, r2), 3) for r1, r2 in ((14, 7), (18, 11), (25, 13), (30, 12), (21, 16), (9, 4))]
      + [SQ(sum_a(r1, r2), 3) for r1, r2 in ((3, 4), (8, 15), (12, 16), (15, 20), (10, 24), (18, 24))])
mD = [SQ(sec_diff(14, 7, th), 5) for th in (45, 72, 150, 108, 36, 24)] + [SQ(umbrella(r, n), 5) for r, n in ((42, 8), (35, 14), (21, 9))] + [SQ(cow_inc(r1, r2), 5) for r1, r2 in ((7, 28), (14, 35), (21, 42))]

# ================= HARD =================
hA = [[MC(seg(r, th)) for r, th in ((7, 60), (h2(21), 120), (h2(35), 60), (35, 120), (42, 60))],
      [MC(brooch(d, n)) for d, n in ((21, 4), (49, 7), (14, 3), (56, 8), (70, 5))],
      [MC(cow(r, 180)) for r in (35, 42, 49, 56, 63)],
      [MC(sec_perim(42, th)) for th in (45, 75, 135, 105, 210)],
      [MC(ang_arc(42, L)) for L in (22, 44, 66, 88, 33)],
      [MC(circ_sq(r)) for r in (35, 42, 49, 56, 63)],
      [MC(cow_inc(r1, r2)) for r1, r2 in ((7, 35), (21, 35), (14, 42), (28, 42), (35, 49))]]
hB = ([SQ(umbrella(r, n), 2) for r, n in ((49, 14), (63, 18), (70, 20), (84, 24))] + [SQ(wheel(r, D), 2) for r, D in ((35, 110), (49, 154), (56, 176), (42, 198))] + [SQ(path(r, w), 2) for r, w in ((35, h2(7)), (45, 7), (60, 7), (28, h2(7)))])
hC = ([SQ(sec_area(42, th), 3) for th in (50, 80, 110, 140, 170, 200)] + [SQ(lens_sq(s), 3) for s in (63, 70, 77, 84, 91, 98)] + [SQ(clock_area(42, tm), 3) for tm in (5, 10, 20, 25, 35, 40)])
hD = [SQ(seg(r, th), 5) for r, th in ((35, 60), (42, 120), (49, 60), (56, 120), (63, 60), (70, 120))] + [SQ(sec_diff(21, 14, th), 5) for th in (36, 72, 90, 108, 144, 180)]

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
