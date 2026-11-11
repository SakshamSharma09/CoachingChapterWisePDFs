"""Class 10 Maths Ch 12 - Surface Areas and Volumes (graded banks). Combinations of two solids and conversion of solids. pi = 22/7."""
from c10m_x import *

SLUG, NAME, CHNO = "Surface_Areas_and_Volumes", "Surface Areas and Volumes", 12
PI = F(22, 7)
def Af(x): return f"{nd(x)} cm²"
def Vf(x): return f"{nd(x)} cm³"
def Lf(x): return f"{nd(x)} cm"
def Nf(x): return nd(x)
def ts(x): return t(x) if F(x).denominator == 1 else nd(x)
def sc(stem0, ask, ans, ex, parts, fmt):
    ans = ans if isinstance(ans, list) else [ans]
    if len(ans) == 1:
        c = ans[0]; w = list(ex) + [c * 2, c / 2, c * 3, c + 10, c - 10]
        return SCG(stem0, ask, ans, [x for x in w if x > 0], parts, fmt)
    return SCG(stem0, ask, ans, [], parts, fmt)
def slant(r, h):
    l2 = F(r) ** 2 + F(h) ** 2; l = F(isqrt(l2.numerator), isqrt(l2.denominator))
    assert l * l == l2, (r, h)
    return l
CONES = [(7, 24, 25), (14, 48, 50), (21, 28, 35), (21, 72, 75), (21, 20, 29), (35, 12, 37), (28, 45, 53), (42, 56, 70), (28, 96, 100), (35, 84, 91), (49, 168, 175), (63, 84, 105)]

# ---- single solids ----
def cyl_csa(r, h):
    v = 2 * PI * r * h
    return sc(f"A right circular cylinder has base radius {ts(r)} cm and height {ts(h)} cm.", "curved surface area of the cylinder", v, [PI * r * r * h, 2 * PI * r * (r + h)], ["Curved surface area $=2\\pi rh$", f"$2\\times\\frac{{22}}{{7}}\\times{ts(r)}\\times{ts(h)}$", f"CSA $={nd(v)}$ cm$^2$"], Af)
def cyl_tsa(r, h):
    v = 2 * PI * r * (r + h)
    return sc(f"A right circular cylinder has base radius {ts(r)} cm and height {ts(h)} cm.", "total surface area of the cylinder", v, [2 * PI * r * h, PI * r * r * h, 2 * PI * r * h + PI * r * r], ["Total surface area $=2\\pi r(r+h)$", f"$2\\times\\frac{{22}}{{7}}\\times{ts(r)}\\times({ts(r)}+{ts(h)})$", f"TSA $={nd(v)}$ cm$^2$"], Af)
def cyl_vol(r, h):
    v = PI * r * r * h
    return sc(f"A right circular cylinder has base radius {ts(r)} cm and height {ts(h)} cm.", "volume of the cylinder", v, [2 * PI * r * h, v / 3, 2 * PI * r * (r + h)], ["Volume $=\\pi r^2h$", f"$\\frac{{22}}{{7}}\\times{ts(r)}^2\\times{ts(h)}$", f"Volume $={nd(v)}$ cm$^3$"], Vf)
def cone_l(r, h):
    l = slant(r, h)
    return sc(f"A right circular cone has base radius {ts(r)} cm and height {ts(h)} cm.", "slant height of the cone", l, [r + h, h - 1, F(r + h, 2)], ["Slant height $l=\\sqrt{r^2+h^2}$", f"$l^2={ts(r)}^2+{ts(h)}^2={nd(F(r)**2+F(h)**2)}$", f"$l={nd(l)}$ cm"], Lf)
def cone_csa(r, h):
    l = slant(r, h); v = PI * r * l
    return sc(f"A right circular cone has base radius {ts(r)} cm and height {ts(h)} cm.", "curved surface area of the cone", v, [PI * r * h, PI * r * (r + l), PI * r * r], [f"Slant height $l=\\sqrt{{{ts(r)}^2+{ts(h)}^2}}={nd(l)}$ cm", "CSA $=\\pi rl$", f"CSA $=\\frac{{22}}{{7}}\\times{ts(r)}\\times{nd(l)}={nd(v)}$ cm$^2$"], Af)
def cone_tsa(r, h):
    l = slant(r, h); v = PI * r * (r + l)
    return sc(f"A right circular cone has base radius {ts(r)} cm and height {ts(h)} cm.", "total surface area of the cone", v, [PI * r * l, PI * r * (r + h), PI * r * r], [f"Slant height $l={nd(l)}$ cm", "TSA $=\\pi r(l+r)$", f"TSA $=\\frac{{22}}{{7}}\\times{ts(r)}\\times({nd(l)}+{ts(r)})={nd(v)}$ cm$^2$"], Af)
def cone_vol(r, h):
    v = PI * r * r * h / 3
    return sc(f"A right circular cone has base radius {ts(r)} cm and height {ts(h)} cm.", "volume of the cone", v, [PI * r * r * h, PI * r * r * h / 2], ["Volume $=\\frac13\\pi r^2h$", f"$\\frac13\\times\\frac{{22}}{{7}}\\times{ts(r)}^2\\times{ts(h)}$", f"Volume $={nd(v)}$ cm$^3$"], Vf)
def sph_sa(r):
    v = 4 * PI * r * r
    return sc(f"A solid sphere has radius {ts(r)} cm.", "surface area of the sphere", v, [2 * PI * r * r, 3 * PI * r * r, PI * r * r], ["Surface area $=4\\pi r^2$", f"$4\\times\\frac{{22}}{{7}}\\times{ts(r)}^2$", f"Surface area $={nd(v)}$ cm$^2$"], Af)
def sph_vol(r):
    v = F(4, 3) * PI * r ** 3
    return sc(f"A solid sphere has radius {ts(r)} cm.", "volume of the sphere", v, [4 * PI * r * r, PI * r ** 3, 2 * PI * r ** 3 / 3], ["Volume $=\\frac43\\pi r^3$", f"$\\frac43\\times\\frac{{22}}{{7}}\\times{ts(r)}^3$", f"Volume $={nd(v)}$ cm$^3$"], Vf)
def hemi_tsa(r):
    v = 3 * PI * r * r
    return sc(f"A solid hemisphere has radius {ts(r)} cm.", "total surface area of the hemisphere", v, [2 * PI * r * r, 4 * PI * r * r, PI * r * r], ["TSA $=$ curved surface $2\\pi r^2$ + flat circular face $\\pi r^2=3\\pi r^2$", f"$3\\times\\frac{{22}}{{7}}\\times{ts(r)}^2$", f"TSA $={nd(v)}$ cm$^2$"], Af)
def hemi_vol(r):
    v = F(2, 3) * PI * r ** 3
    return sc(f"A solid hemisphere has radius {ts(r)} cm.", "volume of the hemisphere", v, [F(4, 3) * PI * r ** 3, 2 * PI * r * r, PI * r ** 3], ["Volume $=\\frac23\\pi r^3$", f"$\\frac23\\times\\frac{{22}}{{7}}\\times{ts(r)}^3$", f"Volume $={nd(v)}$ cm$^3$"], Vf)
def cuboid_tsa(l, b, h):
    v = 2 * (l * b + b * h + h * l)
    return sc(f"A cuboid measures {l} cm by {b} cm by {h} cm.", "total surface area of the cuboid", v, [l * b * h, 2 * (l + b) * h, l * b + b * h + h * l], ["TSA $=2(lb+bh+hl)$", f"$2({l}\\times{b}+{b}\\times{h}+{h}\\times{l})$", f"TSA $={v}$ cm$^2$"], Af)
def cube_vol_from_tsa(a):
    return sc(f"The total surface area of a cube is {6*a*a} cm$^2$.", "volume of the cube", a ** 3, [a * a, 6 * a ** 3, a ** 2 * 6], ["TSA $=6a^2$", f"$a^2={a*a}$, so $a={a}$ cm", f"Volume $=a^3={a**3}$ cm$^3$"], Vf)

# ---- combinations ----
def toy(r, h):
    l = slant(r, h); v = 2 * PI * r * r + PI * r * l
    return sc(f"A toy is a cone of base radius {ts(r)} cm and height {ts(h)} cm mounted on a hemisphere of the same radius (the flat faces coincide).", "total surface area of the toy", v, [3 * PI * r * r + PI * r * l, 2 * PI * r * r + PI * r * h, PI * r * l], [f"Slant height of the cone $l=\\sqrt{{{ts(r)}^2+{ts(h)}^2}}={nd(l)}$ cm", "TSA $=$ CSA of cone $+$ CSA of hemisphere $=\\pi rl+2\\pi r^2$", f"TSA $=\\frac{{22}}{{7}}\\times{ts(r)}\\times{nd(l)}+2\\times\\frac{{22}}{{7}}\\times{ts(r)}^2={nd(v)}$ cm$^2$"], Af)
def toy_vol(r, h):
    v = F(2, 3) * PI * r ** 3 + PI * r * r * h / 3
    return sc(f"A toy is a cone of base radius {ts(r)} cm and height {ts(h)} cm mounted on a hemisphere of the same radius.", "volume of the toy", v, [F(2, 3) * PI * r ** 3, PI * r * r * h / 3, F(4, 3) * PI * r ** 3 + PI * r * r * h / 3], ["Volume $=$ hemisphere $+$ cone", f"Hemisphere $=\\frac23\\pi r^3={nd(F(2,3)*PI*r**3)}$ cm$^3$; cone $=\\frac13\\pi r^2h={nd(PI*r*r*h/3)}$ cm$^3$", f"Volume $={nd(v)}$ cm$^3$"], Vf)
def capsule_sa(r, h):
    v = 2 * PI * r * h + 4 * PI * r * r
    return sc(f"A capsule is a cylinder of radius {ts(r)} cm and length {ts(h)} cm (straight part) with a hemisphere of the same radius fixed at each end.", "total surface area of the capsule", v, [2 * PI * r * h + 2 * PI * r * r, 2 * PI * r * (h + r), 2 * PI * r * h + 6 * PI * r * r], ["Surface $=$ CSA of cylinder $+$ two hemispherical surfaces", f"$2\\pi rh+2(2\\pi r^2)=2\\times\\frac{{22}}{{7}}\\times{ts(r)}\\times{ts(h)}+4\\times\\frac{{22}}{{7}}\\times{ts(r)}^2$", f"TSA $={nd(v)}$ cm$^2$"], Af)
def capsule_vol(r, h):
    v = PI * r * r * h + F(4, 3) * PI * r ** 3
    return sc(f"A capsule is a cylinder of radius {ts(r)} cm and length {ts(h)} cm (straight part) with a hemisphere of the same radius fixed at each end.", "volume of the capsule", v, [PI * r * r * h, PI * r * r * h + F(2, 3) * PI * r ** 3, PI * r * r * h + 2 * PI * r ** 3], ["Volume $=$ cylinder $+$ two hemispheres $=\\pi r^2h+\\frac43\\pi r^3$", f"Cylinder $={nd(PI*r*r*h)}$ cm$^3$; two hemispheres $={nd(F(4,3)*PI*r**3)}$ cm$^3$", f"Volume $={nd(v)}$ cm$^3$"], Vf)
def cube_hemi(a):
    r = F(a, 2); v = 6 * a * a + PI * r * r
    return sc(f"A solid is a cube of edge {a} cm surmounted by a hemisphere of diameter {a} cm (the hemisphere rests on a face of the cube).", "total surface area of the solid", v, [6 * a * a + 2 * PI * r * r, 6 * a * a, 6 * a * a - PI * r * r], ["TSA $=$ surface of cube $-$ circle covered $+$ curved surface of hemisphere", f"$6a^2-\\pi r^2+2\\pi r^2=6a^2+\\pi r^2$ with $r={ts(r)}$ cm", f"TSA $={nd(6*a*a)}+{nd(PI*r*r)}={nd(v)}$ cm$^2$"], Af)
def cube_dep(a):
    r = F(a, 2); v = a ** 3 - F(2, 3) * PI * r ** 3
    return sc(f"A hemispherical depression of diameter {a} cm, the largest possible, is scooped out of the top face of a cubical block of edge {a} cm.", "volume of the remaining block", v, [a ** 3, F(2, 3) * PI * r ** 3, a ** 3 - F(4, 3) * PI * r ** 3], ["Remaining volume $=$ cube $-$ hemisphere", f"Cube $={a**3}$ cm$^3$; hemisphere of radius ${ts(r)}$ cm $=\\frac23\\pi r^3={nd(F(2,3)*PI*r**3)}$ cm$^3$", f"Volume $={nd(v)}$ cm$^3$"], Vf)
def wood(r, h):
    v = 2 * PI * r * h + 4 * PI * r * r
    return sc(f"A wooden article is made by scooping out a hemisphere of radius {ts(r)} cm from each end of a solid cylinder of height {ts(h)} cm and base radius {ts(r)} cm.", "total surface area of the article", v, [2 * PI * r * h + 2 * PI * r * r, 2 * PI * r * h, 2 * PI * r * h + 6 * PI * r * r], ["Surface $=$ CSA of cylinder $+$ two hemispherical hollows (the flat ends are removed)", f"$2\\pi rh+2(2\\pi r^2)$ with $r={ts(r)}$, $h={ts(h)}$", f"TSA $={nd(2*PI*r*h)}+{nd(4*PI*r*r)}={nd(v)}$ cm$^2$"], Af)
def cyl_cone_cavity(r, h):
    l = slant(r, h); v = 2 * PI * r * h + PI * r * r + PI * r * l
    return sc(f"From a solid cylinder of height {ts(h)} cm and base radius {ts(r)} cm, a conical cavity of the same height and the same base radius is hollowed out.", "total surface area of the remaining solid", v, [2 * PI * r * h + 2 * PI * r * r, 2 * PI * r * h + PI * r * l, 2 * PI * r * (r + h) + PI * r * l], [f"Slant height of the cone $l=\\sqrt{{{ts(r)}^2+{ts(h)}^2}}={nd(l)}$ cm", "TSA $=$ CSA cylinder $+$ one flat base $+$ CSA of cone", f"$={nd(2*PI*r*h)}+{nd(PI*r*r)}+{nd(PI*r*l)}={nd(v)}$ cm$^2$"], Af)
def cyl_cone_cavity_vol(r, h):
    v = PI * r * r * h * F(2, 3)
    return sc(f"From a solid cylinder of height {ts(h)} cm and base radius {ts(r)} cm, a conical cavity of the same height and base radius is hollowed out.", "volume of the remaining solid", v, [PI * r * r * h, PI * r * r * h / 3, PI * r * r * h * F(5, 3)], ["Volume left $=$ cylinder $-$ cone", f"Cylinder $={nd(PI*r*r*h)}$ cm$^3$; cone $={nd(PI*r*r*h/3)}$ cm$^3$", f"Volume left $={nd(v)}$ cm$^3$"], Vf)
def tent(r, hc, hn):
    l = slant(r, hn); v = 2 * PI * r * hc + PI * r * l
    return sc(f"A tent is a cylinder of radius {ts(r)} m and height {ts(hc)} m surmounted by a cone of the same radius and height {ts(hn)} m.", "area of canvas (in m$^2$) needed to make the tent", v, [2 * PI * r * hc, PI * r * l, 2 * PI * r * hc + PI * r * hn], [f"Slant height of the cone $l=\\sqrt{{{ts(r)}^2+{ts(hn)}^2}}={nd(l)}$ m", "Canvas $=$ CSA of cylinder $+$ CSA of cone", f"$={nd(2*PI*r*hc)}+{nd(PI*r*l)}={nd(v)}$ m$^2$"], lambda x: f"{nd(x)} m²")
def hollow_hemi(R, r):
    v = F(2, 3) * PI * (F(R) ** 3 - F(r) ** 3)
    return sc(f"A hemispherical bowl has outer radius {ts(R)} cm and inner radius {ts(r)} cm.", "volume of material used to make the bowl", v, [F(2, 3) * PI * R ** 3, F(2, 3) * PI * (R - r) ** 3, F(4, 3) * PI * (F(R) ** 3 - F(r) ** 3)], ["Volume of material $=$ outer hemisphere $-$ inner hemisphere", f"$\\frac23\\pi(R^3-r^3)=\\frac23\\times\\frac{{22}}{{7}}({ts(R)}^3-{ts(r)}^3)$", f"Volume $={nd(v)}$ cm$^3$"], Vf)

# ---- conversion of solids ----
def n_spheres(R, r):
    n = F(R) ** 3 / F(r) ** 3; assert n.denominator == 1
    return sc(f"A solid metallic sphere of radius {ts(R)} cm is melted and recast into small solid spheres of radius {ts(r)} cm.", "number of small spheres obtained", n, [n * 2, n - 1, F(R, r)], ["Volume of big sphere $=n\\times$ volume of a small sphere", f"$n=\\frac{{\\frac43\\pi({ts(R)})^3}}{{\\frac43\\pi({ts(r)})^3}}=\\left(\\frac{{{ts(R)}}}{{{ts(r)}}}\\right)^3$", f"$n={nd(n)}$"], Nf)
def cyl_to_spheres(r, h, rho):
    n = F(3) * r * r * h / (4 * F(rho) ** 3); assert n.denominator == 1
    return sc(f"A solid metallic cylinder of base radius {ts(r)} cm and height {ts(h)} cm is melted and recast into solid spheres of radius {ts(rho)} cm.", "number of spheres obtained", n, [n * 2, n + 6, n - 2], [f"Volume of cylinder $=\\pi\\times{ts(r)}^2\\times{ts(h)}$", f"Volume of a sphere $=\\frac43\\pi({ts(rho)})^3$; $n=\\frac{{3r^2h}}{{4\\rho^3}}$", f"$n={nd(n)}$"], Nf)
def sphere_to_wire(R, r):
    L = F(4) * R ** 3 / (3 * F(r) ** 2); 
    return sc(f"A solid metallic sphere of radius {ts(R)} cm is melted and drawn into a wire of circular cross-section of radius {ts(r)} cm.", "length of the wire", L, [L * 2, L / 2, F(4) * R ** 3 / (3 * F(r))], ["Volume of sphere $=$ volume of wire (cylinder) $=\\pi r^2L$", f"$\\frac43\\pi({ts(R)})^3=\\pi({ts(r)})^2L$", f"$L={nd(L)}$ cm"], Lf)
def cone_to_sphere(r, h):
    R3 = F(r) ** 2 * h / 4; R = F(round(float(R3) ** (1 / 3))); assert R ** 3 == R3, (r, h)
    return sc(f"A solid metallic cone of base radius {ts(r)} cm and height {ts(h)} cm is melted and recast into a solid sphere.", "radius of the sphere", R, [R + 1, R * 2, R - 1], ["Volume of sphere $=$ volume of cone", f"$\\frac43\\pi R^3=\\frac13\\pi({ts(r)})^2({ts(h)})$ gives $R^3={nd(R3)}$", f"$R={nd(R)}$ cm"], Lf)
def cyl_to_cuboid(r, h, l, b):
    v = PI * r * r * h; x = v / (l * b); assert dec(x)
    return sc(f"Water from a full cylindrical tank of radius {ts(r)} cm and height {ts(h)} cm is poured into an empty rectangular tank of base {l} cm by {b} cm.", "height of water in the rectangular tank", x, [x * 2, x / 2, v / (l + b)], ["Volume of water is the same in both tanks", f"$\\pi r^2h={nd(v)}$ cm$^3$ and base area of cuboid $={l*b}$ cm$^2$", f"Height $={nd(v)}\\div{l*b}={nd(x)}$ cm"], Lf)
def sphere_drop(R, r):
    x = F(4) * R ** 3 / (3 * F(r) ** 2)
    return sc(f"A solid sphere of radius {ts(R)} cm is completely dropped into water in a cylindrical vessel of base radius {ts(r)} cm, and no water spills.", "rise in the water level", x, [x * 2, x / 2, F(R, r)], ["Volume of water displaced $=$ volume of sphere $=$ rise $\\times$ base area", f"$\\frac43\\pi({ts(R)})^3=\\pi({ts(r)})^2x$", f"$x={nd(x)}$ cm"], Lf)
def cone_to_cyl(r, h, R):
    x = F(r) ** 2 * h / (3 * F(R) ** 2); assert dec(x)
    return sc(f"A conical vessel of radius {ts(r)} cm and height {ts(h)} cm is full of water. The water is poured into a cylindrical vessel of base radius {ts(R)} cm.", "height of the water in the cylindrical vessel", x, [x * 3, x / 2, x * 2], ["Volume of water in the cone $=\\frac13\\pi r^2h$", f"$\\frac13\\pi({ts(r)})^2({ts(h)})=\\pi({ts(R)})^2x$", f"$x={nd(x)}$ cm"], Lf)
def cuboid_cubes(l, b, h, a):
    n = F(l * b * h, a ** 3); assert n.denominator == 1
    return sc(f"A solid metal cuboid {l} cm by {b} cm by {h} cm is melted and recast into cubes of edge {a} cm.", "number of cubes obtained", n, [n * 2, n - 1, F(l * b * h, a * a)], ["Volume of cuboid $=n\\times$ volume of a cube", f"$n=\\frac{{{l}\\times{b}\\times{h}}}{{{a}^3}}$", f"$n={nd(n)}$"], Nf)

# ---- extra (harder) scenarios ----
def sphere_in_cube(a):
    v = a ** 3 - F(4, 3) * PI * F(a, 2) ** 3
    return sc(f"The largest possible solid sphere is carved out of a cube of edge {a} cm.", "volume of the material wasted", v, [F(4, 3) * PI * F(a, 2) ** 3, a ** 3, a ** 3 - F(2, 3) * PI * F(a, 2) ** 3], ["The sphere has diameter equal to the edge, so $r=\\frac{a}{2}$", f"Sphere $=\\frac43\\pi\\left(\\frac{{{a}}}{{2}}\\right)^3={nd(F(4,3)*PI*F(a,2)**3)}$ cm$^3$; cube $={a**3}$ cm$^3$", f"Wasted $={nd(v)}$ cm$^3$"], Vf)
def sphere_in_cyl(r):
    v = 2 * PI * r ** 3 - F(4, 3) * PI * r ** 3
    return sc(f"A solid sphere of radius {ts(r)} cm fits exactly inside a cylinder (it touches the curved surface and both bases).", "volume of the space in the cylinder not occupied by the sphere", v, [F(4, 3) * PI * r ** 3, 2 * PI * r ** 3, 2 * PI * r ** 3 + F(4, 3) * PI * r ** 3], ["The cylinder has radius $r$ and height $2r$", f"Cylinder $=\\pi r^2(2r)={nd(2*PI*r**3)}$ cm$^3$; sphere $=\\frac43\\pi r^3={nd(F(4,3)*PI*r**3)}$ cm$^3$", f"Unoccupied $={nd(v)}$ cm$^3$"], Vf)
def cyl_to_cone_h(r, h):
    return sc(f"A solid cylinder of radius {r} cm and height {h} cm is melted and recast into a cone of the same base radius.", "height of the cone", 3 * h, [h, 2 * h, F(h, 3)], ["Volume is conserved: $\\pi r^2h=\\frac13\\pi r^2H$", f"$H=3h=3\\times{h}$", f"$H={3*h}$ cm"], Lf)
def cone_hemi_eq(r):
    return sc(f"A solid cone and a solid hemisphere have equal base radii {ts(r)} cm and equal volumes.", "height of the cone", 2 * r, [r, 3 * r, F(3 * r, 2)], ["$\\frac13\\pi r^2h=\\frac23\\pi r^3$", "Cancel $\\frac13\\pi r^2$: $h=2r$", f"$h={nd(2*r)}$ cm"], Lf)
def cyl_to_cones(r, h, rc, hc):
    n = F(3 * r * r * h, rc * rc * hc); assert n.denominator == 1
    return sc(f"A solid cylinder of base radius {r} cm and height {h} cm is melted and recast into identical solid cones, each of base radius {rc} cm and height {hc} cm.", "number of cones obtained", n, [n * 2, n // 3, n + 4], ["Volume of cylinder $=n\\times$ volume of one cone", f"$\\pi({r})^2({h})=n\\times\\frac13\\pi({rc})^2({hc})$", f"$n={nd(n)}$"], Nf)
def rat(a, b, kind):
    k = 2 if kind == "sa" else 3
    def red(x, y): g = gcd(x, y); return (x // g, y // g)
    ans = red(a ** k, b ** k); other = 3 if kind == "sa" else 2
    nm = "surface areas" if kind == "sa" else "volumes"
    return SCG(f"The radii of two solid spheres are in the ratio {a} : {b}.", f"ratio of their {nm}", [ans], [red(a, b), red(a ** other, b ** other), red(a ** k * 2, b ** k)],
               [f"{'Surface area $=4\\pi r^2$' if kind == 'sa' else 'Volume $=\\frac43\\pi r^3$'}, so the ratio is the ratio of the {'squares' if kind == 'sa' else 'cubes'} of the radii", f"${a}^{k}:{b}^{k}={a**k}:{b**k}$", f"Ratio $={ans[0]}:{ans[1]}$"], lambda x: f"{x[0]} : {x[1]}")

h2 = lambda n: F(n, 2)
# ================= EASY =================
eA = [[MC(cyl_csa(r, h)) for r, h in ((7, 5), (14, 10), (21, 8), (7, 12), (35, 4))],
      [MC(cyl_vol(r, h)) for r, h in ((7, 10), (14, 5), (21, 2), (7, 3), (14, 3))],
      [MC(cone_l(r, h)) for r, h, _ in (CONES[0], CONES[1], CONES[2], CONES[4], CONES[5])],
      [MC(cone_csa(r, h)) for r, h, _ in (CONES[0], CONES[1], CONES[2], CONES[4], CONES[5])],
      [MC(sph_sa(r)) for r in (7, 14, 21, 28, 35)],
      [MC(sph_vol(r)) for r in (21, 42, h2(21), h2(63), h2(105))],
      [MC(hemi_tsa(r)) for r in (7, 14, 21, 28, 35)]]
eB = ([SQ(cyl_tsa(r, h), 2) for r, h in ((7, 10), (14, 6), (21, 4), (35, 2))] + [SQ(hemi_vol(r), 2) for r in (h2(21), 21, h2(63), 42)]
      + [SQ(cuboid_tsa(*p), 2) for p in ((8, 5, 3), (12, 7, 4), (15, 10, 6), (20, 9, 5))])
eC = ([SQ(cone_vol(r, h), 3) for r, h, _ in CONES[:6]] + [SQ(cone_tsa(r, h), 3) for r, h, _ in CONES[:6]] + [SQ(cube_vol_from_tsa(a), 3) for a in (3, 4, 5, 6, 7, 8)])
eD = [SQ(cuboid_cubes(*p), 5) for p in ((24, 12, 6, 3), (24, 12, 12, 6), (24, 18, 9, 3), (24, 18, 18, 6), (24, 24, 6, 3), (24, 24, 18, 6))] + [SQ(n_spheres(R, r), 5) for R, r in ((6, 2), (9, 3), (12, 4), (10, 2), (8, 2), (15, 5))]

# ================= NCERT =================
nA = [[MC(toy(r, h)) for r, h, _ in (CONES[0], CONES[2], CONES[5], CONES[1], CONES[6])],
      [MC(capsule_sa(r, h)) for r, h in ((h2(7), 10), (7, 14), (7, 20), (14, 28), (h2(21), 12))],
      [MC(cube_hemi(a)) for a in (14, 28, 7, 21, 42)],
      [MC(cyl_cone_cavity(r, h)) for r, h, _ in (CONES[0], CONES[1], CONES[2], CONES[3], CONES[5])],
      [MC(wood(r, h)) for r, h in ((h2(7), 10), (7, 15), (7, 20), (h2(21), 12), (14, 20))],
      [MC(cyl_to_spheres(*p)) for p in ((6, 32, 3), (6, 24, 2), (3, 32, 2), (9, 24, 3), (12, 16, 4))],
      [MC(cone_to_sphere(r, h)) for r, h in ((6, 24), (3, 12), (12, 6), (4, 54), (9, 36))]]
nB = ([SQ(sphere_to_wire(R, r), 2) for R, r in ((6, 2), (6, 3), (3, 1), (9, 3))] + [SQ(cuboid_cubes(*p), 2) for p in ((24, 12, 9, 6), (24, 12, 15, 3), (24, 18, 12, 6), (24, 24, 9, 3))]
      + [SQ(sphere_drop(R, r), 2) for R, r in ((3, 3), (6, 4), (6, 6), (9, 9))])
nC = ([SQ(toy_vol(r, h), 3) for r, h in ((21, 10), (21, 20), (h2(21), 14), (h2(21), 28), (21, 35), (h2(21), 21))] + [SQ(capsule_vol(r, h), 3) for r, h in ((h2(21), 10), (h2(21), 20), (21, 15), (21, 30), (h2(21), 15), (21, 10))]
      + [SQ(cyl_cone_cavity_vol(r, h), 3) for r, h in ((7, 12), (7, 24), (7, 15), (14, 9), (14, 6), (21, 12))])
nD = [SQ(cyl_to_cuboid(*p), 5) for p in ((7, 10, 11, 7), (7, 12, 22, 14), (7, 15, 21, 11), (7, 24, 33, 14), (14, 6, 22, 14), (7, 28, 22, 14))] + [SQ(cone_to_cyl(*p), 5) for p in ((6, 8, 4), (6, 12, 3), (6, 15, 5), (6, 10, 5), (6, 24, 4), (6, 30, 6))]

# ================= MEDIUM =================
mA = [[MC(tent(r, hc, hn)) for r, hc, hn in ((h2(7), 4, 12), (h2(7), 10, 12), (7, 8, 24), (7, 12, 24), (h2(21), 9, 14))],
      [MC(hollow_hemi(R, r)) for R, r in ((6, 3), (8, 2), (12, 6), (12, 3), (11, 2))],
      [MC(cube_dep(a)) for a in (21, 42, 63, 84, 105)],
      [MC(sphere_to_wire(R, r)) for R, r in ((12, 3), (9, 2), (6, 4), (12, 4), (3, 2))],
      [MC(sphere_drop(R, r)) for R, r in ((3, 6), (6, 12), (9, 6), (12, 12), (9, 18))],
      [MC(capsule_sa(r, h)) for r, h in ((7, 10), (14, 10), (21, 14), (h2(7), 20), (h2(21), 20))],
      [MC(toy(r, h)) for r, h, _ in CONES[7:12]],
      [MC(cuboid_cubes(*p)) for p in ((24, 12, 18, 3), (24, 18, 15, 3), (24, 24, 12, 3), (24, 18, 6, 6), (24, 12, 6, 6))]]
mB = ([SQ(cone_to_sphere(r, h), 2) for r, h in ((6, 3), (3, 96), (12, 48), (18, 9))] + [SQ(cyl_to_spheres(*p), 2) for p in ((6, 48, 3), (6, 72, 2), (9, 32, 3), (12, 24, 3))] + [SQ(cube_hemi(a), 2) for a in (35, 49, 56, 63)])
mC = ([SQ(capsule_vol(r, h), 3) for r, h in ((h2(21), 12), (h2(21), 18), (21, 12), (21, 24), (h2(21), 25), (21, 8))] + [SQ(toy_vol(r, h), 3) for r, h in ((21, 14), (21, 42), (h2(21), 7), (h2(21), 35), (21, 21), (h2(21), 42))]
      + [SQ(wood(r, h), 3) for r, h in ((h2(7), 15), (7, 10), (7, 12), (14, 15), (h2(21), 20), (14, 25))])
mD = [SQ(cone_to_cyl(*p), 5) for p in ((6, 20, 4), (6, 16, 4), (6, 12, 6), (6, 18, 6), (9, 8, 3), (9, 16, 6))] + [SQ(cyl_to_cuboid(*p), 5) for p in ((7, 20, 22, 14), (7, 30, 21, 11), (7, 12, 42, 11), (14, 10, 22, 14), (7, 30, 30, 22), (7, 15, 44, 21))]

# ================= HARD =================
hA = [[MC(sphere_in_cube(a)) for a in (21, 42, 63, 84, 105)],
      [MC(sphere_in_cyl(r)) for r in (h2(21), 21, h2(63), 42, h2(105))],
      [MC(cyl_to_cone_h(r, h)) for r, h in ((6, 5), (7, 8), (4, 9), (10, 3), (12, 7))],
      [MC(cone_hemi_eq(r)) for r in (7, 10, 12, 21, 9)],
      [MC(rat(a, b, "sa")) for a, b in ((2, 3), (3, 5), (4, 7), (5, 6), (6, 9))],
      [MC(rat(a, b, "vol")) for a, b in ((2, 3), (3, 4), (1, 5), (5, 7), (4, 6))],
      [MC(cyl_to_cones(*p)) for p in ((6, 10, 3, 4), (7, 12, 7, 6), (6, 8, 2, 12), (9, 4, 3, 6), (10, 9, 5, 6))],
      [MC(hollow_hemi(R, r)) for R, r in ((9, h2(15)), (15, 9), (10, h2(5)), (13, 10), (12, h2(3)))]]
hB = ([SQ(sphere_drop(R, r), 2) for R, r in ((6, 8), (9, 12), (12, 8), (15, 10))] + [SQ(hollow_hemi(R, r), 2) for R, r in ((h2(15), h2(9)), (14, h2(7)), (h2(27), 6), (h2(19), 5))]
      + [SQ(sphere_to_wire(R, r), 2) for R, r in ((12, 2), (9, 1), (12, 1), (6, 1))])
hC = ([SQ(cyl_to_spheres(*p), 3) for p in ((9, 32, 6), (6, 72, 6), (12, 24, 6), (12, 16, 6), (9, 48, 3), (6, 54, 3))] + [SQ(cone_to_sphere(r, h), 3) for r, h in ((10, 5), (8, 4), (5, 20), (10, 40), (20, 10), (2, 8))]
      + [SQ(cyl_to_cones(*p), 3) for p in ((6, 20, 3, 8), (12, 14, 6, 21), (8, 9, 4, 6), (5, 24, 5, 8), (14, 6, 7, 18), (9, 20, 3, 15))])
hD = [SQ(toy(r, h), 5) for r, h, _ in CONES[10:12]] + [SQ(capsule_vol(r, h), 5) for r, h in ((h2(21), 40), (21, 45))] + [SQ(tent(r, hc, hn), 5) for r, hc, hn in ((h2(21), 12, 14), (21, 15, 28))] \
     + [SQ(sphere_in_cyl(r), 5) for r in (h2(63), 42)] + [SQ(cube_dep(a), 5) for a in (126, 147)] + [SQ(sphere_in_cube(a), 5) for a in (126, 147)]

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
