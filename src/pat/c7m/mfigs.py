import math
from figs import svg, line, circ, text, poly, dot
def transversal(top_lbl, bot_lbl, ang=70, names=('A','B','C','D','P','Q'), bot_below=False):
    """AB (top) || CD (bottom), transversal through P (on AB) and Q (on CD). top_lbl at angle BPQ (right, below AB); bot_lbl at angle DQP (right, above CD)."""
    A, B, C, D, Pn, Qn = names
    y1, y2 = 50, 130; t = math.radians(ang); dx = (y2 - y1) / math.tan(t)
    px = 120; qx = px + dx
    ext = 30; ex = ext / math.sin(t) * math.cos(t)
    b = line(30, y1, 260, y1) + line(30, y2, 260, y2)
    b += line(px - ex, y1 - ext, qx + ex, y2 + ext)
    b += text(22, y1 + 4, A, 'end') + text(268, y1 + 4, B, 'start') + text(22, y2 + 4, C, 'end') + text(268, y2 + 4, D, 'start')
    b += text(px - 8, y1 - 8, Pn, 'end') + text(qx + 6, y2 + 14, Qn, 'start')
    b += text(px + 52, y1 + 24, top_lbl, 'middle', 11) + (text(qx + 52, y2 + 24, bot_lbl, 'middle', 11) if bot_below else text(qx + 52, y2 - 12, bot_lbl, 'middle', 11))
    return svg(290, 180, b)
def _pts(angB, angC, L, bx=30, by=145):
    a = math.radians(angB); c = math.radians(angC); A = math.radians(180 - angB - angC)
    ab = L * math.sin(c) / math.sin(A)
    return (bx, by), (bx + L, by), (bx + ab * math.cos(a), by - ab * math.sin(a))
def tri_ext(la, lb, lext, angB=65, angC=30, names=('A','B','C','D')):
    """Triangle ABC drawn to scale (angles at B and C given), BC extended to D. la at A (inside), lb at B, lext = exterior angle at C."""
    A, B, C, D = names
    pb, pc, pa = _pts(angB, angC, 190)
    pd = (pc[0] + 60, pc[1])
    b = poly([pa, pb, pc]) + line(pc[0], pc[1], pd[0], pd[1])
    b += text(pa[0], pa[1] - 7, A) + text(pb[0] - 6, pb[1] + 14, B, 'end') + text(pc[0] - 2, pc[1] + 15, C) + text(pd[0] + 4, pd[1] + 5, D, 'start')
    b += text(pa[0] + 4, pa[1] + 30, la, 'middle', 10) + text(pb[0] + 50, pb[1] - 7, lb, 'middle', 10) + text(pc[0] + 38, pc[1] - 12, lext, 'middle', 10)
    return svg(300, 175, b)
def tri(la, lb, lc, angA, angB, angC, names=('A','B','C')):
    """Triangle drawn to scale; labels placed outside near each vertex."""
    A, B, C = names
    pb, pc, pa = _pts(angB, angC, 90, 100, 150)
    b = poly([pa, pb, pc])
    b += text(pa[0], pa[1] - 20, la, 'middle', 11) + text(pa[0], pa[1] - 7, A)
    b += text(pb[0] - 6, pb[1] + 13, B, 'end') + text(pb[0] - 6, pb[1] + 27, lb, 'end', 11)
    b += text(pc[0] + 6, pc[1] + 13, C, 'start') + text(pc[0] + 6, pc[1] + 27, lc, 'start', 11)
    return svg(300, 185, b)
