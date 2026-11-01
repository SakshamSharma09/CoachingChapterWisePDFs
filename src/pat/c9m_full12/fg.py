import sys, math
sys.path.insert(0, '/home/claude/pat')
from figs import *
def pt(cx, cy, r, ang): a = math.radians(ang); return cx + r*math.cos(a), cy - r*math.sin(a)
def circle_fig(pts, chords=(), center='O', radii=(), arcs_extra='', size=210, extra='', rr=80, lab=14, tangent=()):
    """pts: {label: angle_deg}. chords: [('A','B'),...] drawn as lines; radii: labels joined to centre."""
    cx = cy = size/2; b = circ(cx, cy, rr)
    P = {k: pt(cx, cy, rr, a) for k, a in pts.items()}
    for a, c in chords: b += line(*P[a], *P[c])
    for a in radii: b += line(cx, cy, *P[a])
    if center: b += dot(cx, cy, center, 5, -4)
    for k, (x, y) in P.items():
        ang = pts[k]; lx, ly = pt(cx, cy, rr+lab, ang); b += dot(x, y) + text(lx, ly+4, k)
    return svg(size, size, b + extra), P
def fig_sector(r_label='7 cm', ang=60, size=190, shade=True, rr=75):
    cx = cy = size/2
    x1, y1 = pt(cx, cy, rr, 0); x2, y2 = pt(cx, cy, rr, ang)
    large = 1 if ang > 180 else 0
    path = f"<path d='M{cx},{cy} L{x1},{y1} A{rr},{rr} 0 {large} 0 {x2},{y2} Z' fill='{'#cfd8ee' if shade else 'none'}' stroke='#000' stroke-width='1.4'/>"
    return svg(size, size, circ(cx, cy, rr, '#999', 'none', 1) + path + dot(cx, cy, 'O', -12, 4) + text(cx+rr/2, cy+14, r_label) + text(cx+22, cy-6, f"{ang}°", 'start', 11))
def tri_fig(P, labels, sides=None, w=230, h=170, extra=''):
    """P: three (x,y) in svg px; labels: 'ABC'; sides: dict {'AB':'5 cm',...}"""
    b = poly(P)
    for (x, y), l in zip(P, labels):
        dx = -12 if x < w/2 else 8; dy = 14 if y > h/2 else -6
        b += text(x+dx, y+dy, l)
    if sides:
        idx = {labels[0]+labels[1]: (0, 1), labels[1]+labels[2]: (1, 2), labels[0]+labels[2]: (0, 2)}
        for k, v in sides.items():
            i, j = idx[k]; mx = (P[i][0]+P[j][0])/2; my = (P[i][1]+P[j][1])/2
            b += text(mx + (0 if True else 0), my+(14 if my > h/2 else -6), v, sz=11)
    return svg(w, h, b + extra)
def numline(lo, hi, marks=(), u=40, labels=None):
    W = (hi-lo)*u+50; b = line(15, 30, W-15, 30) + f"<path d='M{W-15},30 l-6,-4 v8 z'/>"
    for i in range(lo, hi+1):
        x = 25+(i-lo)*u; b += line(x, 25, x, 35) + text(x, 50, i, sz=11)
    for v, l in marks:
        x = 25+(v-lo)*u; b += dot(x, 30, '') + text(x, 16, l)
    return svg(W, 62, b)
def table(headers, rows, first_bold=True):
    h = "<table class='t'><tr>" + "".join(f"<th>{x}</th>" for x in headers) + "</tr>"
    for r in rows: h += "<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>"
    return h + "</table>"
def htable(top, bottom):  # two-row horizontal table
    return "<table class='t'><tr>" + "".join(f"<th>{x}</th>" for x in top) + "</tr><tr>" + "".join(f"<td>{x}</td>" for x in bottom) + "</tr></table>"
