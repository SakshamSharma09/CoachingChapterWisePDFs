import math
from figs import svg, line, circ, text, poly, dot
from figs8 import arrow, rect
def circuit(labels=('A', 'B', 'C', 'D')):
    """Simple series circuit: cell (A), bulb (B), switch (C), connecting wires (D)."""
    b = line(60, 40, 260, 40) + line(60, 40, 60, 130) + line(260, 40, 260, 130) + line(60, 130, 140, 130) + line(180, 130, 260, 130)
    # cell at bottom-left of bottom wire (long and short plates)
    b += line(140, 118, 140, 142, '#000', 2.6) + line(150, 125, 150, 135, '#000', 4.5) + line(150, 130, 180, 130)
    b += text(145, 160, labels[0])
    # bulb at top
    b += circ(160, 40, 15, '#000', '#fff8d6', 1.6) + line(150, 50, 170, 30, '#555', 1) + line(150, 30, 170, 50, '#555', 1)
    b += text(160, 20, labels[1])
    # switch on the right wire (open)
    b += line(260, 65, 260, 80, '#fff', 3) + line(260, 80, 272, 66, '#000', 2) + circ(260, 80, 2.5, '#000', '#000', 1) + circ(260, 65, 2.5, '#000', '#000', 1)
    b += text(288, 76, labels[2])
    b += text(30, 90, labels[3], 'middle')
    return svg(310, 170, b)
def reflection(ang_i, label_i='i', label_r='r'):
    """Plane mirror with normal; incident and reflected rays at ang_i from the normal."""
    cx, cy, L = 150, 130, 100
    t = math.radians(ang_i)
    ix, iy = cx - L * math.sin(t), cy - L * math.cos(t)
    rx, ry = cx + L * math.sin(t), cy - L * math.cos(t)
    b = line(40, cy, 260, cy, '#000', 3) + "".join(line(40 + k * 12, cy, 32 + k * 12, cy + 10, '#555', 1) for k in range(19))
    b += line(cx, cy, cx, cy - 115, '#555', 1, '5,4') + text(cx + 4, cy - 118, 'N', 'start')
    b += arrow(ix, iy, cx - 4 * math.sin(t), cy - 4 * math.cos(t), '#c0392b', 1.8) + arrow(cx, cy, rx, ry, '#1f4e8c', 1.8)
    b += text(ix - 6, iy - 4, 'Incident ray', 'end', 10) + text(rx + 6, ry - 4, 'Reflected ray', 'start', 10)
    b += text(cx - 28, cy - 40, f"{ang_i}°" if label_i == 'deg' else label_i, 'middle', 11) + text(cx + 28, cy - 40, label_r, 'middle', 11)
    b += text(cx, cy + 28, 'Plane mirror', 'middle', 11) + text(cx + 2, cy + 3, 'O', 'start', 10)
    return svg(300, 170, b)
def dist_time(pts, xmax=None, ymax=None, xl='Time (h)', yl='Distance (km)', xs=1, ys=None):
    """Distance-time graph from points [(t, d), ...] with grid."""
    xmax = xmax or max(p[0] for p in pts); ymax = ymax or max(p[1] for p in pts)
    ys = ys or max(1, ymax // 6)
    W, H = 300, 190; x0, y0, gw, gh = 45, 160, 230, 140
    X = lambda t: x0 + t / xmax * gw; Y = lambda d: y0 - d / ymax * gh
    b = ""
    t = 0
    while t <= xmax: b += line(X(t), y0, X(t), y0 - gh, '#e3e3e3', .7) + text(X(t), y0 + 13, t, 'middle', 10); t += xs
    d = 0
    while d <= ymax: b += line(x0, Y(d), x0 + gw, Y(d), '#e3e3e3', .7) + text(x0 - 5, Y(d) + 3, d, 'end', 10); d += ys
    b += line(x0, y0, x0 + gw, y0, '#000', 1.4) + line(x0, y0, x0, y0 - gh, '#000', 1.4)
    b += "<polyline points='" + " ".join(f"{X(a):.1f},{Y(c):.1f}" for a, c in pts) + "' fill='none' stroke='#c0392b' stroke-width='2'/>"
    for a, c in pts: b += circ(f"{X(a):.1f}", f"{Y(c):.1f}", 2.6, '#c0392b', '#c0392b', 1)
    b += text(x0 + gw / 2, 186, xl, 'middle', 11) + f"<text x='12' y='{y0-gh/2}' font-size='11' text-anchor='middle' transform='rotate(-90 12 {y0-gh/2})'>{yl}</text>"
    return svg(W, H, b)
