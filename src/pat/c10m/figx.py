import sys, math
import figs
sys.path.insert(0, '/home/claude/pat')
from figs import *

def _lab(pts, name, c, d=13):
    x, y = pts[name]; dx, dy = x-c[0], y-c[1]; n = math.hypot(dx, dy) or 1
    return text(x+dx/n*d, y+dy/n*d+4, name)

def shape(pts, edges, extra='', w=240, h=170, labs=None, dashed=()):
    """pts: name->(x,y) svg px. edges: list of (a,b). Labels pushed away from centroid."""
    c = (sum(p[0] for p in pts.values())/len(pts), sum(p[1] for p in pts.values())/len(pts))
    b = ''
    for a, bb in edges:
        b += line(*pts[a], *pts[bb], dash=('4,3' if (a, bb) in dashed else None))
    b += extra
    for k in (labs if labs is not None else pts): b += _lab(pts, k, c)
    return svg(w, h, b)

def midlab(p, q, t, dx=0, dy=-4):
    return text((p[0]+q[0])/2+dx, (p[1]+q[1])/2+dy, t, sz=11)

def tri_parallel(DE_frac=0.5, labels=('A', 'B', 'C', 'D', 'E'), notes=None, w=240, h=185):
    A = (115, 26); B = (20, 158); C = (215, 158)
    D = (A[0]+(B[0]-A[0])*DE_frac, A[1]+(B[1]-A[1])*DE_frac); E = (A[0]+(C[0]-A[0])*DE_frac, A[1]+(C[1]-A[1])*DE_frac)
    pts = dict(zip(labels, (A, B, C, D, E)))
    ex = line(*D, *E)
    body = ''
    cen = (115, 110)
    for e in [(labels[0], labels[1]), (labels[1], labels[2]), (labels[2], labels[0])]: body += line(*pts[e[0]], *pts[e[1]])
    body += ex
    for k in pts: body += _lab(pts, k, cen)
    if notes:
        for (a, b2, t, dx, dy) in notes: body += midlab(pts[a], pts[b2], t, dx, dy)
    return svg(w, h, body)

def circle_tangents(ang_note='', w=250, h=190):
    O = (95, 95); r = 55; Ae = (225, 95)
    d = Ae[0]-O[0]; a = math.acos(r/d)
    P = (O[0]+r*math.cos(a), O[1]-r*math.sin(a)); Q = (O[0]+r*math.cos(a), O[1]+r*math.sin(a))
    b = circ(*O, r) + line(*Ae, *P) + line(*Ae, *Q) + line(*O, *P) + line(*O, *Q) + line(*O, *Ae, dash='4,3')
    b += dot(*O, 'O', -14, 4) + text(P[0], P[1]-8, 'P') + text(Q[0], Q[1]+16, 'Q') + text(Ae[0]+10, Ae[1]+4, 'A')
    b += ang_note
    return svg(w, h, b)

def cyclic_quad(labels='ABCD', extra_text=(), w=220, h=200):
    O = (110, 100); r = 78
    ang = [200, 330, 40, 130]  # degrees (svg y down => use -sin)
    pts = {}
    for l, a in zip(labels, ang): pts[l] = (O[0]+r*math.cos(math.radians(a)), O[1]-r*math.sin(math.radians(a)))
    b = circ(*O, r)
    for i in range(4): b += line(*pts[labels[i]], *pts[labels[(i+1) % 4]])
    for k in pts: b += _lab(pts, k, O, 12)
    for (x, y, t) in extra_text: b += text(x, y, t, sz=11)
    return svg(w, h, b), pts

def solid_tent(r_px=60, hc=70, hk=60, labels=True, w=220, h=230):
    cx = 110; base = 200; top_cyl = base-hc; apex = top_cyl-hk
    b = line(cx-r_px, base, cx-r_px, top_cyl) + line(cx+r_px, base, cx+r_px, top_cyl) + line(cx-r_px, top_cyl, cx, apex) + line(cx+r_px, top_cyl, cx, apex)
    b += f"<ellipse cx='{cx}' cy='{base}' rx='{r_px}' ry='14' stroke='#000' fill='none' stroke-width='1.4'/>"
    b += f"<ellipse cx='{cx}' cy='{top_cyl}' rx='{r_px}' ry='14' stroke='#000' fill='none' stroke-width='1' stroke-dasharray='4,3'/>"
    b += line(cx+r_px+14, base, cx+r_px+14, top_cyl, '#0f2347', 1) + line(cx+r_px+14, top_cyl, cx+r_px+14, apex, '#0f2347', 1)
    return b, (cx, base, top_cyl, apex, r_px)

def height_dist(angle_deg, label_h='h', label_d='', ground=190, w=260, h=190, obs_ang=True):
    # tower at right, observer at left, angle of elevation
    tx = 210; d = 150; ox = tx-d; hh = d*math.tan(math.radians(angle_deg))
    top = ground-min(hh, 150)
    b = line(10, ground, 250, ground, w=1.2) + line(tx, ground, tx, top, w=3) + line(ox, ground, tx, top, '#0f2347', 1.2)
    b += text(ox-8, ground+14, 'P') + text(tx+10, ground+14, 'B') + text(tx+10, top-2, 'A')
    b += f"<path d='M {ox+34} {ground} A 34 34 0 0 0 {ox+34*math.cos(math.radians(angle_deg))} {ground-34*math.sin(math.radians(angle_deg))}' fill='none' stroke='#c00' stroke-width='1.2'/>"
    b += text(ox+48, ground-6, f"{angle_deg}°", sz=11, c='#c00')
    return svg(w, h, b)

def right_tri(leg_h, leg_v, hyp, w=240, h=170, alpha_at='B', hide=None):
    """Right angle at C (bottom-left). Horizontal leg BC, vertical leg AC, hypotenuse AB. Labels show given sides (strings); angle α (or θ) at B."""
    C = (30, 140); B = (210, 140); A = (30, 25)
    b = line(*C, *B) + line(*C, *A) + line(*A, *B)
    b += f"<path d='M 30 128 L 42 128 L 42 140' fill='none' stroke='#000' stroke-width='1'/>"
    b += text(120, 156, leg_h) + text(14, 85, leg_v, 'end') + text(130, 78, hyp, 'start')
    b += text(20, 152, 'C') + text(218, 150, 'B') + text(26, 18, 'A')
    b += text(172, 134, 'α', sz=14, c='#c00')
    return svg(w, h, b)

def zoxy(t=0.7, w=300, h=190):
    A = (120, 20); B = (50, 150); C = (240, 150)
    Z = (B[0]+t*(C[0]-B[0]), 150)
    X = (C[0]+(1-t)*(A[0]-C[0]), C[1]+(1-t)*(A[1]-C[1]))
    Y = (B[0]+t*(A[0]-B[0]), B[1]+t*(A[1]-B[1]))
    # line XY meets y=150
    dx, dy = Y[0]-X[0], Y[1]-X[1]; k = (150-X[1])/dy; O = (X[0]+k*dx, 150)
    b = line(*A, *B) + line(*B, *C) + line(*C, *A) + line(*X, *Z) + line(*Y, *Z) + line(*Y, *X) + line(*O, *Y, dash='4,3') + line(*O, *B if O[0] < B[0] else C, dash='4,3')
    for n_, p, dxl, dyl in [('A', A, 0, -6), ('B', B, 0, 15), ('C', C, 8, 14), ('Z', Z, 0, 15), ('X', X, 12, 0), ('Y', Y, -10, 0), ('O', O, 0, 15)]:
        b += text(p[0]+dxl, p[1]+dyl, n_)
    return svg(w, h, b)

def coord_grid(pts, xr=(0, 16), yr=(0, 18), u=14, segs=()):
    return figs.coord_plane(pts, xr, yr, u, segs)

def shadow_fig(w=300, h=150):
    b = line(10, 130, 290, 130, w=1.2) + line(60, 130, 60, 60, w=3) + line(60, 60, 130, 130, '#0f2347') + line(170, 130, 170, 25, w=3) + line(170, 25, 280, 130, '#0f2347')
    b += text(48, 98, 'pole', 'end', 11) + text(158, 78, 'tower', 'end', 11) + text(95, 144, 'shadow', 'middle', 11) + text(225, 144, 'shadow', 'middle', 11)
    return svg(w, h, b)

def tower_building(a_h=30, b_h=60, w=300, h=200):
    # tower (tall, left) and building (short, right); sightlines from foot of each to top of other
    gx1, gx2, g = 60, 230, 180
    th = 150; bh = 50
    b = line(10, g, 290, g, w=1.2) + line(gx1, g, gx1, g-th, w=4) + line(gx2, g, gx2, g-bh, w=4)
    b += line(gx1, g, gx2, g-bh, '#0f2347', 1.2) + line(gx2, g, gx1, g-th, '#0f2347', 1.2)
    b += text(gx1, g+14, 'Q') + text(gx2, g+14, 'P') + text(gx1-8, g-th-4, 'T', 'end') + text(gx2+8, g-bh-4, 'B', 'start')
    b += text(gx1+46, g-8, '30°', 'middle', 11, '#c00') + text(gx2-60, g-8, '60°', 'middle', 11, '#c00')
    return svg(w, h, b)
