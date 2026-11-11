import math
from figs import svg, line, circ, text, poly, dot
def rect(x, y, w, h, fill='none', c='#000', sw=1.5): return f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='{fill}' stroke='{c}' stroke-width='{sw}'/>"
def ruler(lo, hi, a, b, label='Pencil'):
    """scale from lo to hi cm (broken ruler starts at lo); pencil spans a..b cm."""
    u = 28; X = lambda v: 20 + (v - lo) * u; W = int(X(hi) + 20)
    s = rect(X(lo) - 10, 54, (hi - lo) * u + 10, 34, '#fbf1c7', '#8a6d00', 1.2)
    for i in range(int((hi - lo) * 10) + 1):
        v = lo + i / 10; L = 14 if i % 10 == 0 else (9 if i % 5 == 0 else 5)
        s += line(X(v), 54, X(v), 54 + L, '#000', .8)
        if i % 10 == 0: s += text(X(v), 80, int(v), sz=10)
    s += rect(X(a), 28, (b - a) * u - 12, 16, '#e9b44c', '#7a4e00', 1.2) + poly([(X(b) - 12, 28), (X(b), 36), (X(b) - 12, 44)], '#7a4e00', '#f2d6a2', 1.2)
    s += text((X(a) + X(b)) / 2, 22, label, sz=10) + line(X(a), 44, X(a), 54, '#c0392b', .8) + line(X(b), 36, X(b), 54, '#c0392b', .8)
    return svg(W, 98, s)
def thermo(val, lo=-10, hi=110, step=10, w=120, h=190):
    top, bot = 20, h - 40; Y = lambda t: bot - (t - lo) * (bot - top) / (hi - lo)
    s = rect(55, top - 6, 12, bot - top + 12, '#fff', '#444', 1.5) + circ(61, bot + 14, 14, '#444', '#c0392b', 1.5)
    s += f"<rect x='58' y='{Y(val):.1f}' width='6' height='{bot-Y(val)+8:.1f}' fill='#c0392b'/>"
    for t in range(lo, hi + 1, step):
        s += line(67, Y(t), 74, Y(t), '#000', 1) + text(80, Y(t) + 3, t, 'start', 9)
    return svg(w, h, s)
def bar_magnets(a=('N', 'S'), b=('N', 'S'), gap=40):
    s = ""
    def mag(x, p):
        return rect(x, 30, 50, 24, '#d9534f', '#222', 1.5) + rect(x + 50, 30, 50, 24, '#4a7ab5', '#222', 1.5) + text(x + 25, 47, p[0], sz=13) + text(x + 75, 47, p[1], sz=13)
    s += mag(20, a) + mag(20 + 100 + gap, b)
    s += text(20 + 50, 24, 'Magnet P', sz=10) + text(20 + 100 + gap + 50, 24, 'Magnet Q', sz=10)
    return svg(300 + gap, 80, s)
def funnel():
    s = poly([(70, 40), (170, 40), (130, 110), (110, 110)], '#444', '#f4f4f4', 1.5) + line(120, 110, 120, 140, '#444', 3)
    s += rect(80, 150, 80, 60, '#e8f1fb', '#444', 1.5) + f"<path d='M 85 60 L 155 60 L 125 105 L 115 105 Z' fill='#d9c9a3'/>"
    s += text(210, 55, 'Filter paper', 'start', 10) + text(210, 100, 'Funnel', 'start', 10) + text(170, 185, 'Beaker', 'start', 10)
    s += line(208, 52, 150, 70, '#555', .8) + line(208, 97, 140, 90, '#555', .8)
    return svg(290, 220, s)
def plant_types():
    s = ""
    # climber with tendril, tree, herb as simple shapes
    s += line(40, 150, 40, 60, '#2c7a3f', 2) + circ(40, 50, 14, '#2c7a3f', '#9ccf9c', 1.2) + text(40, 175, 'P', sz=13)
    s += rect(100, 100, 10, 60, '#8b5a2b', '#5c3a14', 1) + circ(105, 80, 32, '#2c7a3f', '#7fbf7f', 1.2) + text(105, 175, 'Q', sz=13)
    s += line(170, 160, 170, 130, '#2c7a3f', 2) + circ(170, 122, 10, '#2c7a3f', '#b6e0a8', 1.2) + text(170, 175, 'R', sz=13)
    return svg(220, 185, s)
