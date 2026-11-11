"""Class 10 Maths Ch 9 - Some Applications of Trigonometry (graded banks). Angles 30/45/60 only; exact answers."""
from c10m_x import *

SLUG, NAME, CHNO = "Some_Applications_of_Trigonometry", "Some Applications of Trigonometry", 9

def um(x): return f"${stex(x)}$ m"
def deg(x): return f"${stex(x)}^\\circ$"

def generic_wrong(c):
    a, b = c
    cands = [(b, a) if (a == 0 or b == 0) else (a + b, 0), smul(c, S(2)), smul(c, S(F(1, 2))), sadd(c, S(1)), smul(c, S(0, 1)), sadd(c, S(0, 1))]
    return [w for w in cands if w != c]

def SC(stem0, ask, ans, wrongs, parts, fmt=um):
    ans = ans if isinstance(ans, list) else [ans]
    assert all(snice(a) for a in ans), (stem0, ans)
    if len(ans) == 1:
        extra = generic_wrong(ans[0])
        wrongs = [w for w in list(wrongs) + extra if w != ans[0]]
    return dict(stem0=stem0, ask=ask, ans=ans, wrongs=wrongs, parts=parts, fmt=fmt)
def MC(sc):
    assert len(sc["ans"]) == 1
    f = sc["fmt"]
    return M4(f"{sc['stem0']} The {sc['ask']} is:", f(sc["ans"][0]), [f(w) for w in sc["wrongs"]], sc["parts"][1] + "; " + sc["parts"][2])
def SQ(sc, total):
    return QS(f"{sc['stem0']} Find the {sc['ask']}.", sc["parts"], total)
def ansj(sc): return ", ".join(sc["fmt"](a) for a in sc["ans"])

# ---------- scenarios ----------
def height_dist(d, ang):
    h = smul(S(d), TAN[ang])
    return SC(f"From a point on level ground, {d} m away from the foot of a vertical tower, the angle of elevation of its top is ${ang}^\\circ$.", "height of the tower", h,
              [smul(S(d), TAN[a]) for a in (30, 45, 60) if a != ang],
              [f"Let the height be $h$; in the right triangle, $\\tan{ang}^\\circ=\\frac{{h}}{{{d}}}$", f"$h={d}\\tan{ang}^\\circ={d}\\times{stex(TAN[ang]) if ang != 45 else 1}$ (with $\\tan30^\\circ=\\frac{{1}}{{\\sqrt3}}$, $\\tan60^\\circ=\\sqrt3$)", f"Height $={stex(h)}$ m"])
def shadow(h, ang):
    x = smul(h, COT[ang])
    return SC(f"A vertical pole is ${stex(h)}$ m high. The angle of elevation of the sun is ${ang}^\\circ$ and the pole casts a shadow on level ground.", "length of the shadow", x,
              [smul(h, TAN[ang]), smul(h, COT[90 - ang if ang != 45 else 45]), smul(h, S(2))],
              [f"Let the shadow be $x$; $\\tan{ang}^\\circ=\\frac{{{stex(h)}}}{{x}}$", f"$x={stex(h)}\\cot{ang}^\\circ$", f"Shadow $={stex(x)}$ m"])
def depr(h, ang):
    x = smul(h, COT[ang])
    return SC(f"From the top of a cliff ${stex(h)}$ m high, the angle of depression of a boat on the sea is ${ang}^\\circ$.", "horizontal distance of the boat from the foot of the cliff", x,
              [smul(h, TAN[ang]), smul(h, COT[90 - ang if ang != 45 else 45])],
              [f"Angle of depression $=$ angle of elevation of the top of the cliff from the boat $={ang}^\\circ$", f"$\\tan{ang}^\\circ=\\frac{{{stex(h)}}}{{x}}$ so $x={stex(h)}\\cot{ang}^\\circ$", f"Distance $={stex(x)}$ m"])
def ladder(L, ang, what="height"):
    if what == "height": v, nm, fn = smul(S(L), SIN[ang]), "height reached on the wall", "\\sin"
    else: v, nm, fn = smul(S(L), COS[ang]), "distance of the foot of the ladder from the wall", "\\cos"
    other = smul(S(L), COS[ang] if what == "height" else SIN[ang])
    return SC(f"A ladder {L} m long leans against a vertical wall and makes an angle of ${ang}^\\circ$ with the level ground.", nm, v, [other, smul(S(L), TAN[ang])],
              [f"The ladder is the hypotenuse, length ${L}$ m", f"{'Height' if what == 'height' else 'Base'} $={L}{fn}{ang}^\\circ={L}\\times{stex(SIN[ang] if what == 'height' else COS[ang]) if (SIN[ang] if what == 'height' else COS[ang])[0] == 0 else t((SIN[ang] if what == 'height' else COS[ang])[0])}$".replace("\\times\\frac", "\\times\\frac"), f"{nm.capitalize()} $={stex(v)}$ m"])
def ladder2(L, ang):
    h, b = smul(S(L), SIN[ang]), smul(S(L), COS[ang])
    return SC(f"A ladder {L} m long leans against a vertical wall and makes an angle of ${ang}^\\circ$ with the level ground.", "height reached on the wall and the distance of the foot of the ladder from the wall (in this order)", [h, b], [],
              [f"Ladder is the hypotenuse; height $={L}\\sin{ang}^\\circ$, base $={L}\\cos{ang}^\\circ$", f"$\\sin{ang}^\\circ={stex(SIN[ang])}$, $\\cos{ang}^\\circ={stex(COS[ang])}$", f"Height $={stex(h)}$ m, distance $={stex(b)}$ m"])
def kite(L, ang):
    h = smul(S(L), SIN[ang])
    return SC(f"The string of a kite is {L} m long. It is taut and makes an angle of ${ang}^\\circ$ with the level ground.", "height of the kite above the ground", h,
              [smul(S(L), COS[ang]), smul(S(L), TAN[ang])],
              ["Kite string is the hypotenuse of the right triangle", f"$h={L}\\sin{ang}^\\circ={L}\\times{stex(SIN[ang])}$", f"Height $={stex(h)}$ m"])
def move(x, a1, a2, story="walk"):
    h = sdiv(S(x), ssub(COT[a1], COT[a2])); d1 = smul(h, COT[a1]); d2 = smul(h, COT[a2])
    if story == "walk":
        st = f"The angle of elevation of the top of a vertical tower from a point on level ground is ${a1}^\\circ$. After walking {x} m towards the foot of the tower along a straight line, the angle of elevation becomes ${a2}^\\circ$."
    else:
        st = f"The shadow of a vertical tower on level ground is {x} m longer when the sun's elevation is ${a1}^\\circ$ than when it is ${a2}^\\circ$."
    return SC(st, "height of the tower", h, [smul(S(x), TAN[a2]), smul(S(x), TAN[a1]), sdiv(S(x), ssub(TAN[a2], TAN[a1]))],
              [f"Let height $=h$; the distances from the foot are $h\\cot{a1}^\\circ$ and $h\\cot{a2}^\\circ$, which differ by ${x}$ m", f"$h(\\cot{a1}^\\circ-\\cot{a2}^\\circ)={x}$ gives $h={x}\\div({stex(ssub(COT[a1], COT[a2]))})$", f"Height $={stex(h)}$ m (distances ${stex(d1)}$ m and ${stex(d2)}$ m)"])
def move2(x, a1, a2):
    sc = move(x, a1, a2)
    h = sc["ans"][0]; d1 = smul(h, COT[a1])
    sc["ask"] = "height of the tower and the initial distance of the point from its foot (in this order)"
    sc["ans"] = [h, d1]; sc["wrongs"] = []
    return sc
def opposite(h, a1, a2):
    d = smul(h, sadd(COT[a1], COT[a2]))
    return SC(f"Two points on level ground lie on opposite sides of a tower of height ${stex(h)}$ m, in line with its foot. The angles of elevation of the top of the tower from the two points are ${a1}^\\circ$ and ${a2}^\\circ$.", "distance between the two points", d,
              [smul(h, ssub(COT[a1], COT[a2])), smul(h, sadd(TAN[a1], TAN[a2]))],
              [f"Distances of the points from the foot: $h\\cot{a1}^\\circ={stex(smul(h, COT[a1]))}$ m and $h\\cot{a2}^\\circ={stex(smul(h, COT[a2]))}$ m", "The points are on opposite sides, so the distances add", f"Distance $={stex(d)}$ m"])
def twodepr(h, a1, a2):
    d = smul(h, ssub(COT[a1], COT[a2]))
    return SC(f"From the top of a tower ${stex(h)}$ m high, the angles of depression of two objects on level ground, on the same side of the tower and in line with its foot, are ${a1}^\\circ$ and ${a2}^\\circ$.", "distance between the two objects", d,
              [smul(h, sadd(COT[a1], COT[a2])), smul(h, ssub(TAN[a2], TAN[a1]))],
              [f"Distances from the foot: $h\\cot{a1}^\\circ={stex(smul(h, COT[a1]))}$ m (farther) and $h\\cot{a2}^\\circ={stex(smul(h, COT[a2]))}$ m (nearer)", "Both objects are on the same side, so the distances are subtracted", f"Distance $={stex(d)}$ m"])
def bldg_tower(b, a_top, a_bot):
    dd = sdiv(S(b) if not isinstance(b, tuple) else b, ssub(TAN[a_bot], TAN[a_top])); H = smul(dd, TAN[a_bot])
    return SC(f"A building is ${stex(b if isinstance(b, tuple) else S(b))}$ m high. From the top of the building the angle of elevation of the top of a tower is ${a_top}^\\circ$ and from the foot of the building it is ${a_bot}^\\circ$.", "height of the tower and its distance from the building (in this order)", [H, dd], [],
              [f"Let the tower be $H$ and the distance $d$: $H=d\\tan{a_bot}^\\circ$ and $H-{stex(b if isinstance(b, tuple) else S(b))}=d\\tan{a_top}^\\circ$", f"Subtract: $d(\\tan{a_bot}^\\circ-\\tan{a_top}^\\circ)={stex(b if isinstance(b, tuple) else S(b))}$, so $d={stex(dd)}$", f"$H=d\\tan{a_bot}^\\circ={stex(H)}$; tower ${stex(H)}$ m, distance ${stex(dd)}$ m"])
def flag(bh, a1, a2):
    d = smul(S(bh), COT[a1]); L = ssub(smul(d, TAN[a2]), S(bh))
    return SC(f"A flagstaff stands on the top of a building {bh} m high. From a point on level ground the angles of elevation of the bottom and the top of the flagstaff are ${a1}^\\circ$ and ${a2}^\\circ$ respectively.", "length of the flagstaff", L,
              [smul(d, TAN[a2]), sadd(smul(d, TAN[a2]), S(bh))],
              [f"Distance of the point from the building: $d={bh}\\cot{a1}^\\circ={stex(d)}$ m", f"Height of the top of the flagstaff $=d\\tan{a2}^\\circ={stex(smul(d, TAN[a2]))}$ m", f"Length $={stex(smul(d, TAN[a2]))}-{bh}={stex(L)}$ m"])
def pedestal(L, a1, a2):
    p = sdiv(S(L), ssub(TAN[a2], S(1))) if a1 == 45 else None
    return SC(f"A statue {L} m tall stands on a pedestal. From a point on the ground, the angle of elevation of the top of the statue is ${a2}^\\circ$ and that of the top of the pedestal is ${a1}^\\circ$.", "height of the pedestal", p, [smul(S(L), TAN[a2]), sdiv(S(L), TAN[a2])],
              [f"Let pedestal $=p$; distance from the point $=p\\cot{a1}^\\circ=p$", f"$p+{L}=p\\tan{a2}^\\circ$ gives $p(\\sqrt3-1)={L}$", f"$p=\\frac{{{L}}}{{\\sqrt3-1}}={stex(p)}$ m"])
def tree(h, th, what):
    if th == 30: top = smul(S(h), S(2)); dist = smul(S(h), COT[30])
    else: top = smul(S(h), S(0, F(2, 3))); dist = smul(S(h), COT[60])
    if what == "total": v, nm = sadd(S(h), top), "original height of the tree"
    else: v, nm = dist, "distance from the foot of the tree to the point where its top touches the ground"
    return SC(f"A storm breaks a tree at a height of {h} m above the ground. The broken part bends over, its top touches the ground and the broken part makes an angle of ${th}^\\circ$ with the ground.", nm, v, [top, smul(S(h), TAN[th]) if what != "total" else smul(S(h), S(2))],
              [f"Broken part (hypotenuse) $=\\frac{{{h}}}{{\\sin{th}^\\circ}}={stex(top)}$ m", f"Distance from the foot $={h}\\cot{th}^\\circ={stex(dist)}$ m", f"{nm.capitalize()} $={stex(v)}$ m" + (f" (that is ${h}+{stex(top)}$)" if what == "total" and th == 30 else "")])
def poles(w):
    h = sdiv(S(w), sadd(COT[30], COT[60])); d1 = smul(h, COT[60]); d2 = smul(h, COT[30])
    return SC(f"Two vertical poles of equal height stand on opposite sides of a road {w} m wide. From a point on the road between them, the angles of elevation of the tops of the poles are ${60}^\\circ$ and ${30}^\\circ$.", "common height of the poles and the distances of the point from the poles (nearer pole first)", [h, d1, d2], [],
              [f"Let height $=h$; distances $h\\cot60^\\circ$ and $h\\cot30^\\circ$ add up to ${w}$", f"$h\\left(\\frac{{1}}{{\\sqrt3}}+\\sqrt3\\right)={w}$ gives $h={stex(h)}$", f"Height ${stex(h)}$ m; distances ${stex(d1)}$ m and ${stex(d2)}$ m"])
def eye(e, d, ang):
    v = sadd(S(e), smul(S(d), TAN[ang]))
    return SC(f"A boy whose eyes are {e} m above the ground stands {d} m away from a vertical building. The angle of elevation of the top of the building from his eyes is ${ang}^\\circ$.", "height of the building", v, [smul(S(d), TAN[ang]), sadd(S(e + 1), smul(S(d), TAN[ang]))],
              [f"Height of the top above the level of his eyes $={d}\\tan{ang}^\\circ={stex(smul(S(d), TAN[ang]))}$ m", f"Add the height of the eyes: ${e}+{stex(smul(S(d), TAN[ang]))}$", f"Height of building $={stex(v)}$ m"])
def car(t_, a1, a2):
    v = S(F(t_, 2))
    return SC(f"A car moves at a uniform speed towards the foot of a vertical tower. The angle of elevation of the top of the tower changes from ${a1}^\\circ$ to ${a2}^\\circ$ in {t_} minutes.", "further time the car takes to reach the foot of the tower", v, [S(t_), S(2 * t_), S(F(t_, 3))],
              [f"Let height $=h$: distances $h\\cot30^\\circ=h\\sqrt3$ and $h\\cot60^\\circ=\\frac{{h}}{{\\sqrt3}}$", f"Distance covered in {t_} min $=h\\sqrt3-\\frac{{h}}{{\\sqrt3}}=\\frac{{2h}}{{\\sqrt3}}$; distance left $=\\frac{{h}}{{\\sqrt3}}$, which is half of it", f"Time left $={t_}\\div2={stex(v)}$ minutes"], fmt=lambda x: f"${stex(x)}$ minutes")
def angle_of(rise, run):
    q = sdiv(rise, run); a = [k for k in (30, 45, 60) if TAN[k] == q][0]
    return SC(f"A person looks at the top of a vertical pole from a point on the ground. The top of the pole is ${stex(rise)}$ m above the level of the person's eyes and the eyes are ${stex(run)}$ m horizontally from the pole.", "angle of elevation of the top of the pole", S(a), [S(k) for k in (30, 45, 60) if k != a] + [S(90 - a if a != 45 else 15)],
              [f"$\\tan\\theta=\\frac{{\\text{{rise}}}}{{\\text{{run}}}}=\\frac{{{stex(rise)}}}{{{stex(run)}}}$", f"$\\tan\\theta={stex(q)}$ which is $\\tan{a}^\\circ$", f"$\\theta={a}^\\circ$"], fmt=deg)
def bldg_depr(b, ae, ad):
    dd = smul(S(b), COT[ad]); H = sadd(S(b), smul(dd, TAN[ae]))
    return SC(f"From the top of a building {b} m high, the angle of elevation of the top of a tower is ${ae}^\\circ$ and the angle of depression of its foot is ${ad}^\\circ$.", "height of the tower", H, [smul(dd, TAN[ae]), smul(S(b), TAN[ae])],
              [f"Horizontal distance $d={b}\\cot{ad}^\\circ={stex(dd)}$ m (from the depression of the foot)", f"Part of the tower above the top of the building $=d\\tan{ae}^\\circ={stex(smul(dd, TAN[ae]))}$ m", f"Tower $={stex(H)}$ m"])

CONCEPT_E = [M4("The line drawn from the eye of an observer to the point of the object being viewed is called the:", "line of sight", ["horizontal line", "normal", "tangent"], "Definition"),
    M4("The angle of elevation of an object is measured from:", "the horizontal line upwards to the line of sight", ["the vertical line to the line of sight", "the line of sight to the ground", "the ground downwards to the horizontal"], "Definition"),
    M4("The angle of depression of an object from an observer is $30^\\circ$. The angle of elevation of the observer as seen from the object is:", "$30^\\circ$", ["$60^\\circ$", "$90^\\circ$", "$0^\\circ$"], "Alternate angles are equal"),
    M4("As the sun rises higher in the sky, the shadow of a vertical pole:", "becomes shorter", ["becomes longer", "stays the same", "becomes zero at once"], "Larger elevation gives smaller $\\cot$"),
    M4("A pole casts a shadow equal to its own height. The angle of elevation of the sun is:", "$45^\\circ$", ["$30^\\circ$", "$60^\\circ$", "$90^\\circ$"], "$\\tan\\theta=1$"),
    M4("The angle of elevation of the top of a tower, seen from a point on level ground, becomes smaller when the observer:", "walks away from the foot of the tower", ["walks towards the foot of the tower", "climbs up the tower", "stays where he is while the tower grows taller"], "The height is fixed, so a larger horizontal distance gives a smaller angle")]
CONCEPT_M = [M4("If the angle of elevation of the top of a tower is $30^\\circ$ at a point $P$ and it is $60^\\circ$ at a point nearer to the tower, then the point nearer to the tower is at:", "one-third of the distance of $P$ from the foot", ["half the distance of $P$ from the foot", "twice the distance of $P$ from the foot", "the same distance as $P$"], "$\\cot60^\\circ:\\cot30^\\circ=1:3$"),
    M4("The angle of elevation of the top of a tower increases as an observer walks towards the tower because:", "the horizontal distance decreases while the height is fixed", ["the height of the tower decreases", "the line of sight becomes horizontal", "the observer moves away from the foot"], "$\\tan\\theta=h/d$"),
    M4("The height of a tower is $h$ and the angle of elevation of its top is $45^\\circ$. The distance of the observer from the foot of the tower is:", "$h$", ["$\\sqrt2\\,h$", "$\\dfrac{h}{2}$", "$2h$"], "$\\tan45^\\circ=1$"),
    M4("If the length of the shadow of a tower is $\\sqrt3$ times its height, the angle of elevation of the sun is:", "$30^\\circ$", ["$60^\\circ$", "$45^\\circ$", "$90^\\circ$"], "$\\cot\\theta=\\sqrt3$"),
    M4("From the top of a tower the angle of depression of a car is $\\theta$. The angle of elevation of the top of the tower from the car is:", "$\\theta$", ["$90^\\circ-\\theta$", "$2\\theta$", "$180^\\circ-\\theta$"], "Alternate interior angles")]

# ================= EASY =================
eA = [[MC(height_dist(d, 45)) for d in (7, 12, 15, 20, 25, 30)],
      [MC(height_dist(d, 60)) for d in (5, 8, 11, 14, 25)],
      [MC(height_dist(d, 30)) for d in (9, 12, 18, 24, 30)],
      [MC(shadow(S(h), a)) for h, a in ((9, 45), (15, 45), (8, 30), (10, 30), (6, 30))],
      [MC(depr(S(h), a)) for h, a in ((12, 45), (20, 45), (7, 30), (15, 30), (9, 45))],
      [MC(ladder(L, a)) for L, a in ((8, 60), (10, 60), (14, 30), (18, 30), (20, 60))],
      CONCEPT_E]
eB = ([SQ(height_dist(d, a), 2) for d, a in ((10, 45), (16, 45), (4, 60), (13, 60))]
      + [SQ(shadow(S(h), a), 2) for h, a in ((14, 45), (11, 30), (7, 45), (12, 30))]
      + [SQ(kite(L, a), 2) for L, a in ((20, 30), (36, 30), (24, 60), (30, 60))])
eC = ([SQ(ladder2(L, a), 3) for L, a in ((12, 60), (16, 60), (22, 30), (26, 30), (30, 60), (40, 30))]
      + [SQ(depr(S(0, k), a), 3) for k, a in ((10, 60), (15, 60), (4, 30), (6, 60), (20, 30), (9, 30))]
      + [SQ(shadow(S(0, k), a), 3) for k, a in ((12, 60), (9, 60), (5, 30), (14, 60), (8, 30), (11, 60))])
eD = ([SQ(opposite(S(0, k), 30, 60), 5) for k in (6, 9, 12, 15, 18, 21)]
      + [SQ(move2(x, 30, 60), 5) for x in (6, 10, 14, 16, 18, 22)])

# ================= NCERT =================
nA = [[MC(height_dist(d, a)) for d, a in ((15, 60), (21, 30), (40, 45), (6, 30), (35, 60))],
      [MC(ladder(L, 60)) for L in (6, 16, 24, 30, 18)],
      [MC(eye(e, d, a)) for e, d, a in ((2, 10, 45), (3, 15, 45), (2, 12, 60), (1, 20, 45), (4, 9, 60))],
      [MC(move(x, 30, 60)) for x in (20, 30, 40, 60, 100)],
      [MC(tree(h, 30, "total")) for h in (4, 5, 8, 9, 12)],
      [MC(bldg_depr(b, 60, 45)) for b in (7, 10, 14, 12, 21)],
      [MC(angle_of(S(r), S(r))) for r in (10, 15, 20, 25, 30)]]
nB = ([SQ(tree(h, 30, "dist"), 2) for h in (6, 8, 10, 15)] + [SQ(ladder(L, 60, "base"), 2) for L in (14, 22, 28, 36)]
      + [SQ(angle_of(S(0, r), S(r)), 2) for r in (10, 12, 14, 16)])
nC = ([SQ(move(x, 30, 60, "walk"), 3) for x in (20, 34, 50)] + [SQ(move(x, 30, 60, "shadow"), 3) for x in (40, 24, 60)] + [SQ(bldg_depr(b, 60, 45), 3) for b in (5, 8, 9, 15, 16, 20)]
      + [SQ(twodepr(S(h), 30, 45), 3) for h in (75, 60, 90, 45, 100, 30)])
nD = ([SQ(poles(w), 5) for w in (80, 120, 160, 40, 200, 240)] + [SQ(pedestal(L, 45, 60), 5) for L in (2, 4, 6, 8, 10, 12)])

# ================= MEDIUM =================
mA = [[MC(eye(e, d, a)) for e, d, a in ((2, 18, 45), (5, 8, 60), (3, 27, 45), (4, 30, 45), (1, 6, 60))],
      [MC(move(x, 30, 60)) for x in (8, 12, 16, 24, 36)],
      [MC(opposite(S(0, k), 30, 60)) for k in (6, 12, 24, 30, 45)],
      [MC(tree(h, 30, "dist")) for h in (3, 7, 11, 14, 20)],
      [MC(tree(h, 60, "total")) for h in (3, 6, 9, 12, 15)],
      [MC(kite(L, 60)) for L in (10, 34, 46, 52, 58)],
      [MC(pedestal(L, 45, 60)) for L in (14, 16, 18, 20, 22)],
      CONCEPT_M]
mB = ([SQ(bldg_depr(b, 30, 60), 2) for b in (6, 12, 18, 24)] + [SQ(eye(e, d, a), 2) for e, d, a in ((2, 24, 60), (3, 14, 45), (5, 30, 45), (1, 21, 60))]
      + [SQ(twodepr(S(h), 45, 60), 2) for h in (9, 12, 18, 30)])
mC = ([SQ(move(x, 45, 60), 3) for x in (4, 8, 10, 14, 18, 20)] + [SQ(bldg_tower(S(0, k), 30, 60), 3) for k in (6, 8, 10, 12, 14, 16)]
      + [SQ(flag(b, 45, 60), 3) for b in (6, 8, 10, 12, 15, 20)])
mD = ([SQ(poles(w), 5) for w in (60, 100, 140, 180, 220, 260)] + [SQ(move2(x, 30, 45), 5) for x in (2, 4, 6, 8, 10, 12)])

# ================= HARD =================
hA = [[MC(move(x, 30, 45)) for x in (4, 6, 10, 14, 20)],
      [MC(flag(b, 30, 60)) for b in (10, 12, 18, 24, 30)],
      [MC(car(t_, 30, 60)) for t_ in (4, 8, 12, 16, 20)],
      [MC(twodepr(S(0, k), 30, 60)) for k in (6, 9, 12, 15, 24)],
      [MC(bldg_depr(b, 30, 60)) for b in (3, 9, 15, 21, 27)],
      [MC(opposite(S(h), 45, 60)) for h in (9, 15, 21, 27, 33)],
      [MC(angle_of(S(0, r), S(r * 3))) for r in (4, 5, 6, 7, 8)]]
hB = ([SQ(move(x, 45, 60), 2) for x in (6, 12, 16, 22)] + [SQ(flag(b, 45, 30), 2) for b in (9, 15, 21, 27)] + [SQ(car(t_, 30, 60), 2) for t_ in (6, 10, 14, 22)])
hC = ([SQ(bldg_tower(S(0, k), 30, 60), 3) for k in (18, 20, 22, 24, 26, 28)] + [SQ(flag(b, 45, 60), 3) for b in (14, 16, 18, 22, 24, 30)]
      + [SQ(opposite(S(h), 45, 60), 3) for h in (6, 12, 18, 24, 36, 42)])
hD = ([SQ(bldg_tower(S(b), 45, 60), 5) for b in (4, 6, 8, 10, 12, 14)] + [SQ(poles(w), 5) for w in (48, 72, 96, 144, 168, 192)])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
