import math
from figs import svg, line, circ, text, poly, dot
def bar(data, ymax, step, ylab='', xlab='', w=300, h=170):
    L, B, T = 44, h - 34, 14; pw = w - L - 10; ph = B - T
    Y = lambda v: B - v * ph / ymax
    b = ""
    for v in range(0, ymax + 1, step):
        b += line(L, Y(v), w - 10, Y(v), '#ddd', .6) + text(L - 5, Y(v) + 3, v, 'end', 9)
    b += line(L, T, L, B, '#000', 1.4) + line(L, B, w - 10, B, '#000', 1.4)
    n = len(data); bw = pw / n * 0.55
    for i, (lab, v) in enumerate(data):
        x = L + pw / n * (i + .5)
        b += f"<rect x='{x-bw/2:.1f}' y='{Y(v):.1f}' width='{bw:.1f}' height='{B-Y(v):.1f}' fill='#8fb1e0' stroke='#0f2347'/>" + text(x, B + 12, lab, sz=9)
    b += text(L + pw / 2, h - 4, xlab, sz=10)
    if ylab: b += f"<text x='10' y='{(T+B)/2}' font-size='10' text-anchor='middle' transform='rotate(-90 10 {(T+B)/2})'>{ylab}</text>"
    return svg(w, h, b)
def rect_dim(wd, ht, lw='', lh='', sc=8, extra=''):
    W, H = wd * sc, ht * sc; b = poly([(30, 20), (30 + W, 20), (30 + W, 20 + H), (30, 20 + H)], '#000', '#eef3fb')
    b += text(30 + W / 2, 14, lw) + text(24, 20 + H / 2 + 4, lh, 'end') + extra
    return svg(int(W + 70), int(H + 40), b)
def lshape(a, b_, c, d, sc=9):
    """L shape: outer a (width) x b_ (height); notch at top-right of size c (w) x d (h). labels e,f unused."""
    P = [(0, 0), (a, 0), (a, b_ - d), (a - c, b_ - d), (a - c, b_), (0, b_)]
    pts = [(25 + x * sc, 20 + y * sc) for x, y in P]
    s = poly(pts, '#000', '#eef3fb')
    s += text(25 + a * sc / 2, 14, f"{a} m") + text(18, 20 + b_ * sc / 2 + 4, f"{b_} m", 'end')
    s += text(25 + (a - c / 2) * sc, 20 + (b_ - d) * sc - 4 if False else 20 + (b_ - d) * sc + 12, '') 
    s += text(25 + (a - c) * sc / 2, 20 + b_ * sc + 14, f"{a-c} m") + text(25 + a * sc + 6, 20 + (b_ - d) * sc / 2 + 4, f"{b_-d} m", 'start')
    s += text(25 + (a - c / 2) * sc, 20 + (b_ - d) * sc - 4, f"{c} m") if False else ''
    return svg(int(25 + a * sc + 50), int(20 + b_ * sc + 26), s)
def numline(lo, hi, marks=None, w=380):
    n = hi - lo; u = (w - 40) / n; X = lambda v: 20 + (v - lo) * u
    b = line(10, 34, w - 10, 34, '#000', 1.4)
    for v in range(lo, hi + 1):
        b += line(X(v), 29, X(v), 39, '#000', 1) + text(X(v), 53, v, sz=10)
    for k, v in (marks or {}).items(): b += circ(X(v), 34, 4, '#c0392b', '#c0392b') + text(X(v), 20, k, c='#c0392b')
    return svg(w, 62, b)
def angle(deg, lab=('O', 'A', 'B'), r=70, flip=False):
    a = math.radians(deg); ox, oy = 30, 90
    b = line(ox, oy, ox + r, oy, '#000', 1.6) + line(ox, oy, ox + r * math.cos(a), oy - r * math.sin(a), '#000', 1.6)
    b += text(ox - 6, oy + 14, lab[0]) + text(ox + r + 8, oy + 4, lab[1]) + text(ox + r * math.cos(a) + 8, oy - r * math.sin(a) - 4, lab[2])
    b += f"<path d='M {ox+22} {oy} A 22 22 0 0 0 {ox+22*math.cos(a):.1f} {oy-22*math.sin(a):.1f}' fill='none' stroke='#c0392b' stroke-width='1.4'/>"
    return svg(150, 105, b)
def clock(hh, mm, r=48):
    cx = cy = r + 8; b = circ(cx, cy, r, '#000', '#fff', 1.6)
    for i in range(12):
        a = math.radians(i * 30); b += line(cx + (r - 6) * math.sin(a), cy - (r - 6) * math.cos(a), cx + r * math.sin(a), cy - r * math.cos(a), '#000', 1.2)
        b += text(cx + (r - 14) * math.sin(a), cy - (r - 14) * math.cos(a) + 3, 12 if i == 0 else i, sz=8)
    ah = math.radians((hh % 12) * 30 + mm * .5); am = math.radians(mm * 6)
    b += line(cx, cy, cx + 24 * math.sin(ah), cy - 24 * math.cos(ah), '#000', 2.6) + line(cx, cy, cx + 36 * math.sin(am), cy - 36 * math.cos(am), '#000', 1.6) + circ(cx, cy, 2.5, '#000', '#000')
    return svg(2 * cx, 2 * cy, b)
def sym_shape(kind='arrow'):
    # a shape with a dashed axis for symmetry questions: house-like pentagon + dashed vertical axis
    b = poly([(60, 20), (110, 55), (110, 120), (10, 120), (10, 55)], '#000', '#eef3fb') + line(60, 8, 60, 132, '#c0392b', 1.3, '5,3')
    return svg(120, 140, b)
