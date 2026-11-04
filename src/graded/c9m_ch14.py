"""Class 9 Maths Ch 14 - Surface Area and Volume (cuboid, cube, cylinder, cone, sphere, hemisphere, pyramid; recasting)."""
from g9m import *

SLUG, NAME, CHNO = "Surface_Area_and_Volume", "Surface Area and Volume", 14

PI = Fr(22, 7)
TRIP = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (6, 8, 10), (9, 12, 15), (12, 16, 20)]
RS = [Fr(7, 2), 7, Fr(21, 2), 14, 21, 28, 35]          # radii that keep pi*r^2 neat
def dv(x):
    """Decimal text of a Fraction (terminating, max 2 dp) else rounded to 2 dp."""
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    t = f"{float(x):.2f}".rstrip("0").rstrip(".")
    return t
def cm(x): return f"${dv(x)}$ cm"
def c2(x): return f"${dv(x)}$ cm$^2$"
def c3(x): return f"${dv(x)}$ cm$^3$"
def okd(x):
    x = Fr(x); d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    return d == 1 and abs(x * 100 - round(x * 100)) == 0
def m_(q, c, why, f, offs=(1, -1, 2, -2, 5, 10, 20, -10), pos=True):
    return nn(q, c, why, offs=tuple(Fr(o) for o in offs), pos=pos, fmtf=lambda x: f(x))
def pick(r, xs): return r.choice(xs)
def near(c): return (Fr(c) // 10 + 1, -(Fr(c) // 10) - 1, Fr(c) // 5 + 2, Fr(c) // 7 + 1, -(Fr(c) // 7) - 3, Fr(c) // 4 + 5)

# ============ value functions ============
def cyl_v(r, h): return PI * r * r * h
def cyl_c(r, h): return 2 * PI * r * h
def cyl_t(r, h): return 2 * PI * r * (r + h)
def cone_v(r, h): return PI * r * r * h / 3
def cone_c(r, l): return PI * r * l
def cone_t(r, l): return PI * r * (l + r)
def sph_a(r): return 4 * PI * r * r
def sph_v(r): return Fr(4, 3) * PI * r ** 3
def hem_c(r): return 2 * PI * r * r
def hem_t(r): return 3 * PI * r * r
def hem_v(r): return Fr(2, 3) * PI * r ** 3
def Rtxt(r): return dv(r)

# ============ MCQ generators ============
def g_cuboid(lo, hi, w):
    def f(r):
        l, b, h = r.randint(lo, hi), r.randint(lo, hi), r.randint(lo, hi)
        if len({l, b, h}) < 3: return None
        if w == "v": return m_(f"The volume of a cuboid of length ${l}$ cm, breadth ${b}$ cm and height ${h}$ cm is:", l * b * h, f"$lbh={l}\\times{b}\\times{h}$.", c3, offs=near(l * b * h))
        if w == "t": return m_(f"The total surface area of a cuboid ${l}$ cm $\\times$ ${b}$ cm $\\times$ ${h}$ cm is:", 2 * (l * b + b * h + h * l), "$2(lb+bh+hl)$.", c2, offs=near(2 * (l * b + b * h + h * l)))
        return m_(f"The lateral surface area of a cuboid ${l}$ cm $\\times$ ${b}$ cm $\\times$ ${h}$ cm (height ${h}$ cm) is:", 2 * h * (l + b), "$2h(l+b)$.", c2, offs=near(2 * h * (l + b)))
    return f
def g_cube(lo, hi, w):
    def f(r):
        a = r.randint(lo, hi)
        if w == "v": return m_(f"The volume of a cube of edge ${a}$ cm is:", a ** 3, f"${a}^3$.", c3, offs=near(a ** 3))
        if w == "t": return m_(f"The total surface area of a cube of edge ${a}$ cm is:", 6 * a * a, "$6a^2$.", c2, offs=near(6 * a * a))
        return m_(f"The volume of a cube is ${a**3}$ cm$^3$. Its edge is:", a, f"$\\sqrt[3]{{{a**3}}}={a}$.", cm, offs=(1, -1, 2, -2, 3, 5))
    return f
def g_cyl(w, hs=range(5, 31), rs=RS):
    def f(r):
        rr, h = pick(r, rs), r.choice(list(hs))
        v = {"v": cyl_v, "c": cyl_c, "t": cyl_t}[w](rr, h)
        if not okd(v): return None
        nm_ = {"v": "volume", "c": "curved surface area", "t": "total surface area"}[w]
        fm = c3 if w == "v" else c2
        ex = {"v": "$\\pi r^2h$", "c": "$2\\pi rh$", "t": "$2\\pi r(r+h)$"}[w]
        return m_(f"Take $\\pi=\\frac{{22}}7$. The {nm_} of a cylinder of radius ${dv(rr)}$ cm and height ${h}$ cm is:", v, f"{ex} with $r={dv(rr)}$, $h={h}$.", fm, offs=near(v))
    return f
def g_slant(trs):
    def f(r):
        a, b, c = pick(r, trs); k = r.randint(1, 3)
        if r.random() < .5: return m_(f"A cone has radius ${a*k}$ cm and height ${b*k}$ cm. Its slant height is:", c * k, f"$l=\\sqrt{{{a*k}^2+{b*k}^2}}$.", cm, offs=(1, -1, 2, -2, 5, 3))
        return m_(f"A cone has height ${b*k}$ cm and slant height ${c*k}$ cm. Its radius is:", a * k, f"$r=\\sqrt{{{c*k}^2-{b*k}^2}}$.", cm, offs=(1, -1, 2, -2, 5, 3))
    return f
def g_cone(w, trs):
    def f(r):
        a, b, c = pick(r, trs); fct = pick(r, [Fr(7, 2), 7, 14]) if a % 7 else pick(r, [1, 2])
        rr, hh, ll = a * fct, b * fct, c * fct
        if rr > 42 or hh > 56: return None
        if w == "c": v = cone_c(rr, ll); nm_ = "curved surface area"; ex = "$\\pi rl$"; fm = c2
        elif w == "t": v = cone_t(rr, ll); nm_ = "total surface area"; ex = "$\\pi r(l+r)$"; fm = c2
        else: v = cone_v(rr, hh); nm_ = "volume"; ex = "$\\frac13\\pi r^2h$"; fm = c3
        if not okd(v): return None
        given = f"radius ${dv(rr)}$ cm and slant height ${dv(ll)}$ cm" if w != "v" else f"radius ${dv(rr)}$ cm and height ${dv(hh)}$ cm"
        return m_(f"Take $\\pi=\\frac{{22}}7$. The {nm_} of a cone of {given} is:", v, f"{ex} with the given values.", fm, offs=near(v))
    return f
def g_sph(w, rs):
    def f(r):
        rr = pick(r, rs)
        v = {"a": sph_a, "v": sph_v, "hc": hem_c, "ht": hem_t, "hv": hem_v}[w](rr)
        if not okd(v): return None
        nm_ = {"a": "surface area of a sphere", "v": "volume of a sphere", "hc": "curved surface area of a hemisphere", "ht": "total surface area of a solid hemisphere", "hv": "volume of a hemisphere"}[w]
        ex = {"a": "$4\\pi r^2$", "v": "$\\frac43\\pi r^3$", "hc": "$2\\pi r^2$", "ht": "$3\\pi r^2$", "hv": "$\\frac23\\pi r^3$"}[w]
        return m_(f"Take $\\pi=\\frac{{22}}7$. The {nm_} of radius ${dv(rr)}$ cm is:", v, f"{ex} with $r={dv(rr)}$.", c3 if w in ("v", "hv") else c2, offs=near(v))
    return f
def g_scale(kind):
    def f(r):
        k = r.randint(2, 6)
        if kind == "sa": return M4(f"The radius of a sphere is multiplied by ${k}$. Its surface area becomes ___ times:", str(k * k), [str(k), str(k ** 3), str(2 * k)], f"Surface area $\\propto r^2$, so ${k}^2={k*k}$.")
        if kind == "vol": return M4(f"The edge of a cube is multiplied by ${k}$. Its volume becomes ___ times:", str(k ** 3), [str(k), str(k * k), str(3 * k)], f"Volume $\\propto a^3$, so ${k}^3={k**3}$.")
        return M4(f"The radii of two spheres are in the ratio $1:{k}$. The ratio of their volumes is:", f"$1:{k**3}$", [f"$1:{k}$", f"$1:{k*k}$", f"$1:{k**3-k}$"], f"Ratio of volumes $=r_1^3:r_2^3=1:{k**3}$.")
    return f
def g_litre(lo, hi):
    def f(r):
        l, b, h = r.randint(lo, hi), r.randint(lo, hi), r.randint(lo, hi)
        if len({l, b, h}) < 3: return None
        return nn(f"A tank measures ${l}$ m $\\times$ ${b}$ m $\\times$ ${h}$ m. Its capacity in litres ($1\\text{{ m}}^3=1000$ L) is:", l * b * h * 1000, f"$V={l*b*h}$ m$^3$.", offs=(1000, -1000, 100, 10000, -100, 2000), pos=True)
    return f
def g_cubes(lo, hi):
    def f(r):
        a = r.randint(lo, hi); n1, n2, n3 = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
        if len({n1, n2, n3}) < 3: return None
        return nn(f"The number of cubes of edge ${a}$ cm that can be cut from a cuboid ${n1*a}$ cm $\\times$ ${n2*a}$ cm $\\times$ ${n3*a}$ cm is:", n1 * n2 * n3, f"$\\dfrac{{{n1*a}}}{{{a}}}\\times\\dfrac{{{n2*a}}}{{{a}}}\\times\\dfrac{{{n3*a}}}{{{a}}}$.", offs=(1, -1, n1, 2, -2, 6), pos=True)
    return f
def g_pyr(lo, hi):
    def f(r):
        a, h = r.randint(lo, hi), r.randint(lo, hi) * 3
        return m_(f"A pyramid has a square base of side ${a}$ cm and height ${h}$ cm. Its volume is:", Fr(a * a * h, 3), "$\\frac13\\times\\text{base area}\\times\\text{height}$.", c3, offs=near(a * a * h // 3))
    return f
CONCEPT = [tx(q, c, w, why) for q, c, w, why in [
    ("The volume of a cone is ___ the volume of a cylinder of the same base and height:", "one-third of", ["half of", "twice", "equal to"], "$\\frac13\\pi r^2h$ versus $\\pi r^2h$."),
    ("The formula for the surface area of a sphere of radius $r$ is:", "$4\\pi r^2$", ["$2\\pi r^2$", "$\\frac43\\pi r^3$", "$\\pi r^2$"], "Standard formula."),
    ("The curved surface area of a hemisphere of radius $r$ is:", "$2\\pi r^2$", ["$3\\pi r^2$", "$4\\pi r^2$", "$\\pi r^2$"], "Half of a sphere's surface."),
    ("In a cone, the relation between radius $r$, height $h$ and slant height $l$ is:", "$l^2=r^2+h^2$", ["$l=r+h$", "$h^2=r^2+l^2$", "$r^2=l^2+h^2$"], "Right triangle."),
    ("The volume of a pyramid with base area $B$ and height $h$ is:", "$\\frac13Bh$", ["$Bh$", "$\\frac12Bh$", "$\\frac23Bh$"], "One third of the prism."),
    ("The total surface area of a closed cylinder of radius $r$ and height $h$ is:", "$2\\pi r(r+h)$", ["$2\\pi rh$", "$\\pi r^2h$", "$\\pi r(r+h)$"], "Curved surface plus two circular ends."),
    ("The unit of volume is:", "cubic units", ["square units", "units", "degrees"], "Three dimensions."),
    ("When a solid is melted and recast into another shape, which quantity stays the same?", "volume", ["surface area", "height", "radius"], "Material is conserved.")]]

# =============================== EASY ===============================
EASY_A = [draw(100, 4, g_cuboid(2, 9, "v")), draw(101, 4, g_cube(2, 9, "v")), draw(102, 4, g_cube(2, 9, "t")), draw(103, 4, g_cuboid(2, 9, "l")), CONCEPT[:4], draw(104, 4, g_cube(2, 9, "e")), draw(105, 4, g_cyl("v", range(2, 11), [Fr(7, 2), 7])), draw(106, 4, g_sph("a", [Fr(7, 2), 7, 14, 21]))]

def q_cuboid(lo, hi):
    def f(r):
        l, b, h = r.randint(lo, hi), r.randint(lo, hi), r.randint(lo, hi)
        if len({l, b, h}) < 3: return None
        return QQ(f"Find the volume, total surface area and lateral surface area of a cuboid of length {l} cm, breadth {b} cm and height {h} cm.", f"Volume $=lbh={l}\\times{b}\\times{h}={l*b*h}$ cm$^3$", f"TSA $=2(lb+bh+hl)=2({l*b}+{b*h}+{h*l})={2*(l*b+b*h+h*l)}$ cm$^2$", f"LSA $=2h(l+b)={2*h*(l+b)}$ cm$^2$")
    return f
def q_cube(lo, hi):
    def f(r):
        a = r.randint(lo, hi)
        return QQ(f"Find the volume and total surface area of a cube of edge {a} cm. Also find the edge of a cube whose volume is {(a+1)**3} cm³.", f"Volume $={a}^3={a**3}$ cm$^3$", f"TSA $=6\\times{a}^2={6*a*a}$ cm$^2$", f"Edge for volume ${(a+1)**3}$: $\\sqrt[3]{{{(a+1)**3}}}={a+1}$ cm")
    return f
def q_cyl(w, hs, rs):
    def f(r):
        rr, h = pick(r, rs), r.choice(list(hs))
        v, c, t = cyl_v(rr, h), cyl_c(rr, h), cyl_t(rr, h)
        if not (okd(v) and okd(c) and okd(t)): return None
        return QQ(f"Take $\\pi=\\frac{{22}}7$. Find the curved surface area, total surface area and volume of a cylinder of radius {dv(rr)} cm and height {h} cm.", f"CSA $=2\\pi rh=2\\times\\frac{{22}}7\\times{dv(rr)}\\times{h}={dv(c)}$ cm$^2$", f"TSA $=2\\pi r(r+h)={dv(t)}$ cm$^2$", f"Volume $=\\pi r^2h={dv(v)}$ cm$^3$")
    return f
def q_litre(lo, hi):
    def f(r):
        l, b, h = r.randint(lo, hi), r.randint(lo, hi), r.randint(lo, hi)
        if len({l, b, h}) < 3: return None
        return QQ(f"A water tank is {l} m long, {b} m wide and {h} m deep. How many litres of water does it hold when full? (1 m³ = 1000 litres)", f"Volume $={l}\\times{b}\\times{h}={l*b*h}$ m$^3$", f"Capacity $={l*b*h}\\times1000$ litres", f"$={l*b*h*1000}$ litres")
    return f
def q_sph(rs):
    def f(r):
        rr = pick(r, rs); a, v = sph_a(rr), sph_v(rr)
        if not (okd(a) and okd(v)): return None
        return QQ(f"Take $\\pi=\\frac{{22}}7$. Find the surface area and volume of a sphere of radius {dv(rr)} cm.", f"Surface area $=4\\pi r^2=4\\times\\frac{{22}}7\\times{dv(rr)}^2={dv(a)}$ cm$^2$", f"Volume $=\\frac43\\pi r^3={dv(v)}$ cm$^3$")
    return f
EASY_B = draw(110, 4, q_cuboid(2, 9)) + draw(111, 4, q_cube(2, 12)) + draw(112, 4, q_litre(2, 9))
EASY_C = draw(113, 6, q_cuboid(5, 15)) + draw(114, 6, q_cyl("v", range(2, 12), [Fr(7, 2), 7, 14])) + draw(115, 6, q_cube(13, 20))
def q_cubes(lo, hi):
    def f(r):
        a = r.randint(lo, hi); n1, n2, n3 = r.randint(2, 6), r.randint(2, 6), r.randint(2, 6)
        if len({n1, n2, n3}) < 3: return None
        return QQ(f"How many cubes of edge {a} cm can be cut from a cuboid measuring {n1*a} cm × {n2*a} cm × {n3*a} cm? Find the leftover volume if each cube is cut and the cuboid is fully used.", f"Volume of cuboid $={n1*a}\\times{n2*a}\\times{n3*a}={n1*n2*n3*a**3}$ cm$^3$", f"Volume of one cube $={a}^3={a**3}$ cm$^3$", f"Number of cubes $=\\dfrac{{{n1*n2*n3*a**3}}}{{{a**3}}}={n1*n2*n3}$", "Leftover volume $=0$ (the cuboid divides exactly)")
    return f
EASY_D = draw(116, 6, q_cyl("t", range(5, 20), [7, 14, 21, Fr(21, 2)])) + draw(117, 6, q_cubes(2, 5))

# ---------- more generators ----------
def g_diag(r):
    a, b, c, d = pick(r, [(2, 3, 6, 7), (1, 2, 2, 3), (2, 6, 9, 11), (4, 4, 7, 9), (4, 8, 8, 12), (6, 6, 7, 11), (3, 4, 12, 13), (2, 10, 11, 15)]); k = r.randint(1, 3)
    return m_(f"The diagonal of a cuboid measuring ${a*k}$ cm $\\times$ ${b*k}$ cm $\\times$ ${c*k}$ cm is:", d * k, f"$\\sqrt{{l^2+b^2+h^2}}=\\sqrt{{{(a*k)**2}+{(b*k)**2}+{(c*k)**2}}}$.", cm, offs=(1, -1, 2, -2, 5, 3))
def g_comp(r):
    rr = pick(r, [Fr(7, 2), 7, 14, 21]); h = r.randint(2, 6) * 3
    v = hem_v(rr) + cone_v(rr, h)
    if not okd(v): return None
    return m_(f"Take $\\pi=\\frac{{22}}7$. A toy is a cone of height ${h}$ cm placed on a hemisphere, both of radius ${dv(rr)}$ cm. Its total volume is:", v, "Volume of hemisphere + volume of cone.", c3, offs=near(v))
def g_rec_sph(r):
    k = r.randint(2, 6); rr = r.randint(1, 4)
    return nn(f"A solid sphere of radius ${k*rr}$ cm is melted and recast into small solid spheres of radius ${rr}$ cm. The number of small spheres is:", k ** 3, f"$\\dfrac{{({k*rr})^3}}{{{rr}^3}}={k}^3$.", offs=(k, -k, k * k, 2 * k ** 3, 10, -5), pos=True)
def g_rec_cube(r):
    a = r.randint(2, 5); n1, n2, n3 = r.randint(2, 8), r.randint(2, 8), r.randint(2, 8)
    return nn(f"A cuboid ${n1*a*a}$ cm $\\times$ ${n2*a}$ cm $\\times$ ${n3*a}$ cm is melted and recast into cubes of edge ${a}$ cm. The number of cubes is:", n1 * a * n2 * n3, f"$\\dfrac{{{n1*a*a}\\times{n2*a}\\times{n3*a}}}{{{a**3}}}$.", offs=(n1, n2, 2, -2, 10, 6), pos=True)
def g_rec_cone(r):
    rr = pick(r, [7, 14, Fr(7, 2)]); h = r.randint(2, 8) * 3; H = r.choice([d for d in (1, 2, 3, 6, 9) if (3 * h) % d == 0 and d != h])
    return nn(f"A cylinder of radius ${dv(rr)}$ cm and height ${h}$ cm is melted and recast into cones of the same radius and height ${H}$ cm. The number of cones is:", Fr(3 * h, H), "Cylinder volume $\\div$ cone volume $=\\frac{3h}{H}$.", offs=(1, -1, h, 2, 3, 6), pos=True) if (3 * h) % H == 0 else None
def g_bowl(r):
    rr = pick(r, [Fr(21, 2), 21]); v = hem_v(rr)
    return m_(f"Take $\\pi=\\frac{{22}}7$. The capacity of a hemispherical bowl of inner radius ${dv(rr)}$ cm is:", v, "$\\frac23\\pi r^3$.", c3, offs=near(v))
def g_rec_cyl(r):
    R = r.choice([3, 6, 9, 12]); rr = r.choice([2, 3, 4, 6]); 
    if (4 * R ** 3) % (3 * rr * rr): return None
    h = Fr(4 * R ** 3, 3 * rr * rr)
    return m_(f"A solid sphere of radius ${R}$ cm is melted and recast into a solid cylinder of radius ${rr}$ cm. The height of the cylinder is:", h, "Equal volumes: $\\frac43\\pi R^3=\\pi r^2h$.", cm, offs=(1, -1, 2, 4, -2, 6))

# =============================== NCERT ===============================
NCERT_A = [draw(200, 4, g_cyl("c")), draw(201, 4, g_cyl("t")), draw(202, 4, g_cone("c", TRIP[:5])), draw(203, 4, g_cone("v", TRIP[:5])), draw(204, 4, g_sph("a", [Fr(21, 2), 21, 28, 35])), draw(205, 4, g_sph("v", [Fr(21, 2), 21, 42, Fr(63, 2)])),
           draw(206, 4, g_sph("hc", [Fr(7, 2), 7, 14, 21, 28])), CONCEPT[4:]]
def q_cone(trs):
    def f(r):
        a, b, c = pick(r, trs); fct = pick(r, [Fr(7, 2), 7, 14]) if a % 7 else pick(r, [1, 2])
        rr, hh, ll = a * fct, b * fct, c * fct
        if rr > 42 or hh > 56: return None
        cc, tt, vv = cone_c(rr, ll), cone_t(rr, ll), cone_v(rr, hh)
        if not (okd(cc) and okd(tt) and okd(vv)): return None
        return QQ(f"Take $\\pi=\\frac{{22}}7$. A cone has radius {dv(rr)} cm and height {dv(hh)} cm. Find its slant height, curved surface area and volume.", f"$l=\\sqrt{{r^2+h^2}}={dv(ll)}$ cm", f"CSA $=\\pi rl={dv(cc)}$ cm$^2$", f"Volume $=\\frac13\\pi r^2h={dv(vv)}$ cm$^3$")
    return f
def q_hem(rs, full=True):
    def f(r):
        rr = pick(r, rs); c, t_, v = hem_c(rr), hem_t(rr), hem_v(rr)
        if not (okd(c) and okd(t_) and (okd(v) or not full)): return None
        steps = [f"CSA $=2\\pi r^2=2\\times\\frac{{22}}7\\times{dv(rr)}^2={dv(c)}$ cm$^2$", f"TSA $=3\\pi r^2={dv(t_)}$ cm$^2$"]
        if full: steps.append(f"Volume $=\\frac23\\pi r^3={dv(v)}$ cm$^3$")
        return QQ(f"Take $\\pi=\\frac{{22}}7$. Find the curved surface area, total surface area" + (" and volume" if full else "") + f" of a solid hemisphere of radius {dv(rr)} cm.", *steps)
    return f
def q_pyr(lo, hi):
    def f(r):
        a, h = r.randint(lo, hi), r.randint(lo, hi) * 3
        return QQ(f"A pyramid has a square base of side {a} cm and height {h} cm. Find its volume.", f"Base area $={a}^2={a*a}$ cm$^2$", f"Volume $=\\frac13\\times{a*a}\\times{h}$", f"$={a*a*h//3}$ cm$^3$")
    return f
NCERT_B = draw(210, 4, q_cone(TRIP[:5])) + draw(211, 4, q_hem([Fr(7, 2), 7, 14, 21, 28], False)) + draw(212, 4, q_pyr(3, 12))
def q_sheet(r):
    k = r.randint(1, 3); h = r.randint(5, 25)
    rr = 7 * k; L = 44 * k
    return QQ(f"A rectangular sheet {L} cm long and {h} cm wide is rolled so that its length forms the circumference of the base of a cylinder of height {h} cm. Find the radius, the curved surface area and the volume (Take $\\pi=\\frac{{22}}7$).", f"$2\\pi r={L}$, so $r=\\dfrac{{{L}\\times7}}{{2\\times22}}={rr}$ cm", f"CSA $=$ area of the sheet $={L}\\times{h}={L*h}$ cm$^2$", f"Volume $=\\pi r^2h=\\frac{{22}}7\\times{rr}^2\\times{h}={cyl_v(rr, h)}$ cm$^3$")
def q_paint(r):
    rr = pick(r, [7, 14, 21]); h = r.randint(2, 9) * 5; rate = r.randint(2, 8) * 5
    c = cyl_c(rr, h)
    return QQ(f"Take $\\pi=\\frac{{22}}7$. A cylindrical pillar has radius {rr} cm and height {h} cm. Find the cost of painting its curved surface at ₹{rate} per 1000 cm$^2$.", f"CSA $=2\\pi rh=2\\times\\frac{{22}}7\\times{rr}\\times{h}={dv(c)}$ cm$^2$", f"Number of units of 1000 cm$^2$ $=\\dfrac{{{dv(c)}}}{{1000}}={dv(c/1000)}$", f"Cost $={dv(c/1000)}\\times{rate}=$ ₹{dv(c*rate/1000)}")
NCERT_C = draw(213, 6, q_cone(TRIP)) + draw(214, 6, q_hem([Fr(21, 2), 21, Fr(63, 2), 42, Fr(105, 2), 63])) + draw(215, 6, q_paint)
def q_rec_sph(r):
    k = r.randint(2, 6); rr = r.randint(1, 5)
    return QQ(f"A solid metal sphere of radius {k*rr} cm is melted and recast into small solid spheres of radius {rr} cm. Find the number of small spheres and compare the total surface area of the small spheres with the surface area of the big sphere.", "Volume is conserved: $n\\times\\frac43\\pi r^3=\\frac43\\pi R^3$", f"$n=\\left(\\dfrac{{{k*rr}}}{{{rr}}}\\right)^3={k**3}$", f"Total area of small spheres $={k**3}\\times4\\pi({rr})^2$, area of big sphere $=4\\pi({k*rr})^2$", f"Ratio $=\\dfrac{{{k**3}\\times{rr}^2}}{{{k*rr}^2}}={k}$: the small spheres have {k} times the surface area")
def q_rec_cone(r):
    rr = pick(r, [7, 14, Fr(7, 2)]); h = r.randint(2, 8) * 3; H = r.choice([1, 2, 3, 6, 9])
    if (3 * h) % H or H == h: return None
    n = 3 * h // H
    return QQ(f"A cylindrical metal block of radius {dv(rr)} cm and height {h} cm is melted and recast into cones of the same radius and height {H} cm. How many cones are made?", f"Volume of cylinder $=\\pi r^2\\times{h}$", f"Volume of one cone $=\\frac13\\pi r^2\\times{H}$", f"$n=\\dfrac{{\\pi r^2\\times{h}}}{{\\frac13\\pi r^2\\times{H}}}=\\dfrac{{3\\times{h}}}{{{H}}}={n}$")
NCERT_D = draw(216, 6, q_sheet) + draw(217, 6, q_rec_sph)

# =============================== MEDIUM ===============================
MED_A = [draw(300, 4, g_scale("sa")), draw(301, 4, g_scale("vol")), draw(302, 4, g_scale("ratio")), draw(303, 4, g_cone("t", TRIP)), draw(304, 4, g_slant(TRIP[1:6])),
         draw(305, 4, g_litre(3, 12)), draw(306, 4, g_cubes(2, 5)), draw(307, 4, g_pyr(4, 12))]
def q_findr(r):
    rr = pick(r, [7, 14, 21, Fr(7, 2), Fr(21, 2)]); h = r.randint(2, 12) * 2
    v = cyl_v(rr, h)
    return QQ(f"Take $\\pi=\\frac{{22}}7$. A cylinder of height {h} cm has volume {dv(v)} cm$^3$. Find its radius and its curved surface area.", f"$\\pi r^2h={dv(v)}$ gives $r^2=\\dfrac{{{dv(v)}\\times7}}{{22\\times{h}}}={dv(rr*rr)}$", f"$r={dv(rr)}$ cm", f"CSA $=2\\pi rh=2\\times\\frac{{22}}7\\times{dv(rr)}\\times{h}={dv(cyl_c(rr, h))}$ cm$^2$")
def q_cubeedge(r):
    a = r.randint(3, 15)
    return QQ(f"The total surface area of a cube is {6*a*a} cm$^2$. Find its edge, its volume and the length of its face diagonal in terms of $\\sqrt2$.", f"$6a^2={6*a*a}$ gives $a^2={a*a}$, so $a={a}$ cm", f"Volume $={a}^3={a**3}$ cm$^3$", f"Face diagonal $=\\sqrt{{{a}^2+{a}^2}}={a}\\sqrt2$ cm")
MED_B = draw(310, 4, q_findr) + draw(311, 4, q_cubeedge) + draw(312, 4, q_cubes(3, 9))
def q_scale(r):
    k = r.randint(2, 5); a = r.randint(2, 9)
    return QQ(f"The edge of a cube is {a} cm. If every edge is multiplied by {k}, find the new surface area and volume and the factors by which they change.", f"Old TSA $=6\\times{a}^2={6*a*a}$, new TSA $=6\\times{a*k}^2={6*(a*k)**2}$ cm$^2$", f"Old volume $={a**3}$, new volume $={(a*k)**3}$ cm$^3$", f"Surface area becomes ${k}^2={k*k}$ times, volume ${k}^3={k**3}$ times")
MED_C = draw(313, 6, q_cone(TRIP)) + draw(314, 6, q_scale) + draw(315, 6, q_hem([Fr(7, 2), 7, 14, 21, 28, 35, Fr(21, 2)], False))
def q_rec_cube(r):
    a = r.randint(2, 5); n1, n2, n3 = r.randint(2, 8), r.randint(2, 8), r.randint(2, 8)
    return QQ(f"A solid cuboid {n1*a*a} cm × {n2*a} cm × {n3*a} cm is melted and recast into cubes of edge {a} cm. Find the number of cubes and the total surface area of all the cubes.", f"Volume of cuboid $={n1*a*a*n2*a*n3*a}$ cm$^3$; volume of a cube $={a**3}$", f"Number of cubes $={n1*a*n2*n3}$", f"TSA of one cube $=6\\times{a}^2={6*a*a}$", f"Total surface area $={n1*a*n2*n3}\\times{6*a*a}={n1*a*n2*n3*6*a*a}$ cm$^2$")
MED_D = draw(316, 6, q_rec_cone) + draw(317, 6, q_rec_cube)

# =============================== HARD ===============================
HARD_A = [draw(400, 4, g_diag), draw(401, 4, g_comp), draw(402, 4, g_rec_sph), draw(403, 4, g_rec_cube), draw(404, 4, g_rec_cone), draw(405, 2, g_bowl) + draw(406, 2, g_rec_cyl), draw(407, 4, g_cone("v", TRIP)), draw(408, 4, g_cyl("v", range(30, 61), [14, 21, 28, 35]))]
def q_diag(r):
    a, b, c, d = pick(r, [(2, 3, 6, 7), (1, 2, 2, 3), (2, 6, 9, 11), (4, 4, 7, 9), (4, 8, 8, 12), (6, 6, 7, 11), (3, 4, 12, 13), (2, 10, 11, 15)]); k = r.randint(1, 3)
    l, b_, h = a * k, b * k, c * k
    return QQ(f"A cuboid measures {l} cm × {b_} cm × {h} cm. Find the length of its diagonal, its total surface area and its volume.", f"Diagonal $=\\sqrt{{{l}^2+{b_}^2+{h}^2}}=\\sqrt{{{l*l+b_*b_+h*h}}}={d*k}$ cm", f"TSA $=2({l*b_}+{b_*h}+{h*l})={2*(l*b_+b_*h+h*l)}$ cm$^2$", f"Volume $={l}\\times{b_}\\times{h}={l*b_*h}$ cm$^3$")
def q_comp(r):
    a, b, c = pick(r, TRIP); f_ = pick(r, [Fr(7, 2), 7, 14, Fr(21, 2)]) if a % 7 else pick(r, [1, 2])
    rr, hh, ll = a * f_, b * f_, c * f_
    if rr > 42 or hh > 56: return None
    v = hem_v(rr) + cone_v(rr, hh); sa = hem_c(rr) + cone_c(rr, ll)
    if not (okd(v) and okd(sa)): return None
    return QQ(f"Take $\\pi=\\frac{{22}}7$. A toy is a cone of radius {dv(rr)} cm and height {dv(hh)} cm resting on a hemisphere of the same radius. Find its total volume and its total surface area (curved parts only).", f"Slant height of the cone $=\\sqrt{{r^2+h^2}}={dv(ll)}$ cm", f"Volume $=\\frac23\\pi r^3+\\frac13\\pi r^2h={dv(v)}$ cm$^3$", f"Surface area $=2\\pi r^2+\\pi rl={dv(sa)}$ cm$^2$")
HARD_B = draw(410, 4, q_diag) + draw(411, 4, q_comp) + draw(412, 4, q_findr)
def q_rec_cyl(r):
    R = r.choice([3, 6, 9, 12]); rr = r.choice([2, 3, 4, 6])
    if (4 * R ** 3) % (3 * rr * rr): return None
    h = Fr(4 * R ** 3, 3 * rr * rr)
    return QQ(f"A solid sphere of radius {R} cm is melted and recast into a solid cylinder of radius {rr} cm. Find the height of the cylinder and its curved surface area (Take $\\pi=\\frac{{22}}7$).", f"$\\frac43\\pi{R}^3=\\pi({rr})^2h$", f"$h=\\dfrac{{4\\times{R**3}}}{{3\\times{rr*rr}}}={dv(h)}$ cm", f"CSA $=2\\pi rh=2\\times\\frac{{22}}7\\times{rr}\\times{dv(h)}={dv(cyl_c(rr, h))}$ cm$^2$")
def q_water(r):
    rr = pick(r, [7, 14, 21]); h = r.randint(2, 6) * 5; l, b = r.choice([(22, 14), (44, 21), (11, 7), (22, 21), (33, 14)])
    v = cyl_v(rr, h); rise = v / (l * b)
    if not okd(rise): return None
    return QQ(f"Take $\\pi=\\frac{{22}}7$. Water from a full cylindrical tank of radius {rr} cm and height {h} cm is poured into an empty rectangular tank with a base {l} cm × {b} cm. Find the height of water in the rectangular tank.", f"Volume of water $=\\pi r^2h=\\frac{{22}}7\\times{rr}^2\\times{h}={dv(v)}$ cm$^3$", f"Base area $={l}\\times{b}={l*b}$ cm$^2$", f"Height $=\\dfrac{{{dv(v)}}}{{{l*b}}}={dv(rise)}$ cm")
def q_bowl(r):
    rr = pick(r, [Fr(21, 2), 21]); v = hem_v(rr); n = r.randint(2, 6)
    return QQ(f"Take $\\pi=\\frac{{22}}7$. A hemispherical bowl has inner radius {dv(rr)} cm. Find its capacity, and the number of such bowls that can be filled from a vessel holding {dv(v*n)} cm$^3$ of soup.", f"Capacity $=\\frac23\\pi r^3=\\frac23\\times\\frac{{22}}7\\times{dv(rr)}^3={dv(v)}$ cm$^3$", f"Number of bowls $=\\dfrac{{{dv(v*n)}}}{{{dv(v)}}}={n}$")
HARD_C = draw(413, 6, q_rec_cyl) + draw(414, 6, q_water) + draw(415, 6, q_bowl)
def q_icecream(r):
    a, b, c = pick(r, TRIP); f_ = pick(r, [Fr(7, 2), 7, 14, Fr(21, 2)]) if a % 7 else pick(r, [1, 2])
    rr, hh = a * f_, b * f_; n = r.randint(10, 40)
    if rr > 42 or hh > 56: return None
    v = hem_v(rr) + cone_v(rr, hh)
    if not okd(v): return None
    return QQ(f"Take $\\pi=\\frac{{22}}7$. An ice-cream cone of radius {dv(rr)} cm and height {dv(hh)} cm is completely filled and topped with a hemisphere of ice-cream of the same radius. Find the total volume of ice-cream and the volume needed for {n} such cones.", f"Volume of the cone $=\\frac13\\pi r^2h={dv(cone_v(rr, hh))}$ cm$^3$", f"Volume of the hemisphere $=\\frac23\\pi r^3={dv(hem_v(rr))}$ cm$^3$", f"Volume per cone $={dv(v)}$ cm$^3$", f"For {n} cones: ${n}\\times{dv(v)}={dv(n*v)}$ cm$^3$")
def q_rec_mix(r):
    R = r.choice([6, 9, 12]); rr = r.choice([1, 2, 3]); k = Fr(R, rr)
    n = r.randint(2, 5) 
    return QQ(f"A solid sphere of radius {R} cm is melted and {n} identical solid cylinders of radius {rr} cm are made from the metal. Find the height of each cylinder.", f"Volume of sphere $=\\frac43\\pi{R}^3$", f"Each cylinder has volume $\\frac{{4\\pi{R**3}}}{{3\\times{n}}}=\\pi({rr})^2h$", f"$h=\\dfrac{{4\\times{R**3}}}{{3\\times{n}\\times{rr*rr}}}={dv(Fr(4*R**3, 3*n*rr*rr))}$ cm")
HARD_D = draw(416, 6, q_icecream) + draw(417, 6, q_rec_mix)

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
