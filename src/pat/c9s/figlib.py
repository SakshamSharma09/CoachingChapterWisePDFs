import sys, math
sys.path.insert(0, '/home/claude/pat')
from figs import *

def table(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"<table class='t'><tr>{h}</tr>{r}</table>"

def arrow(x1, y1, x2, y2, c='#c0392b', w=2):
    a = math.atan2(y2-y1, x2-x1); L = 9
    p1 = (x2-L*math.cos(a-.4), y2-L*math.sin(a-.4)); p2 = (x2-L*math.cos(a+.4), y2-L*math.sin(a+.4))
    return line(x1, y1, x2, y2, c, w) + poly([(x2, y2), p1, p2], c, c, 1)

def force_fig(name='P', left=None, right=None, ground=True, W=300):
    """left=(label, length_px) arrow pointing right-to-left on left side? left: force acting towards left from the right side."""
    b = f"<rect x='110' y='40' width='80' height='46' fill='#e8ecf5' stroke='#000' stroke-width='1.6'/>" + text(150, 69, name, sz=14)
    if ground: b += line(60, 86, 240, 86, '#000', 1.5) + "".join(line(x, 86, x-8, 95, '#555', 1) for x in range(70, 240, 14))
    if right: b += arrow(190, 63, 190+right[1], 63) + text(190+right[1]/2, 55, right[0], sz=12)
    if left: b += arrow(110, 63, 110-left[1], 63) + text(110-left[1]/2, 55, left[0], sz=12)
    return svg(W, 105, b)

def bohr(shells, nlabel='', r0=26, step=22, W=None):
    n = len(shells); R = r0+step*(n-1); size = 2*R+30; c = size/2
    b = ""
    for i, e in enumerate(shells):
        r = r0+step*i; b += circ(c, c, r, '#555', 'none', 1.2)
        for k in range(e):
            a = 2*math.pi*k/e - math.pi/2; b += f"<circle cx='{c+r*math.cos(a):.1f}' cy='{c+r*math.sin(a):.1f}' r='3.6' fill='#2c5aa0'/>"
    b += circ(c, c, 13, '#c0392b', '#f5b7b1', 1.4) + text(c, c+4, nlabel, sz=10)
    return svg(size, size, b)

def graph(pts, xmax, ymax, xl, yl, xs=1, ys=1, W=300, H=190, extra="", color='#0f2347'):
    ox, oy, pw, ph = 42, H-34, W-62, H-56
    X = lambda x: ox+x/xmax*pw; Y = lambda y: oy-y/ymax*ph
    b = ""
    i = 0
    while i <= xmax+1e-9: b += line(X(i), oy, X(i), 14, '#e3e3e3', .7) + text(X(i), oy+14, f"{i:g}", sz=10); i += xs
    j = 0
    while j <= ymax+1e-9: b += line(ox, Y(j), W-16, Y(j), '#e3e3e3', .7) + text(ox-6, Y(j)+3, f"{j:g}", 'end', 10); j += ys
    b += line(ox, oy, W-14, oy, '#000', 1.4) + line(ox, oy, ox, 12, '#000', 1.4)
    b += "".join(line(X(a), Y(b2), X(c), Y(d), color, 2) for (a, b2), (c, d) in zip(pts, pts[1:]))
    b += "".join(f"<circle cx='{X(a):.1f}' cy='{Y(b2):.1f}' r='2.4' fill='{color}'/>" for a, b2 in pts)
    b += text(ox+pw/2, H-6, xl, sz=11) + f"<text x='11' y='{oy-ph/2}' font-size='11' text-anchor='middle' transform='rotate(-90 11 {oy-ph/2})'>{yl}</text>" + extra
    return svg(W, H, b)

def cell_fig(labels, kind='animal'):
    """labels: dict key->letter among nucleus, mito, vacuole, chloro, wall, membrane, er, golgi, lyso"""
    b = ""
    if kind == 'plant':
        b += f"<rect x='25' y='15' width='230' height='150' rx='12' fill='#f4fbf0' stroke='#2e7d32' stroke-width='3'/><rect x='31' y='21' width='218' height='138' rx='9' fill='#fff' stroke='#555' stroke-width='1.2'/>"
        b += f"<rect x='80' y='45' width='100' height='80' rx='20' fill='#eaf4ff' stroke='#555'/>"
        for (x, y) in [(52, 40), (210, 50), (50, 135), (205, 135)]: b += f"<ellipse cx='{x}' cy='{y}' rx='14' ry='8' fill='#7cb342' stroke='#33691e'/>"
    else:
        b += f"<ellipse cx='140' cy='90' rx='120' ry='75' fill='#fff8ec' stroke='#555' stroke-width='2'/>"
        b += f"<ellipse cx='235' cy='55' rx='11' ry='6' fill='#ffd54f' stroke='#8d6e00'/>"
    b += circ(140, 85, 22, '#6a1b9a', '#e1bee7', 1.6) + circ(140, 85, 7, '#6a1b9a', '#6a1b9a')
    b += f"<ellipse cx='95' cy='135' rx='16' ry='8' fill='#ffcc80' stroke='#e65100'/><ellipse cx='190' cy='140' rx='16' ry='8' fill='#ffcc80' stroke='#e65100'/>"
    b += poly([(185, 55), (205, 52), (212, 70), (190, 75)], '#00695c', '#b2dfdb', 1.2)
    pos = dict(nucleus=(140, 85), mito=(95, 135), vacuole=(120, 65) if kind == 'plant' else (150, 140), chloro=(52, 40), wall=(25, 90), membrane=(31, 90), golgi=(197, 63), lyso=(235, 55))
    for k, L in labels.items():
        x, y = pos[k]; b += line(x, y, 270 if x > 140 else 5, y-14 if y < 90 else y+14, '#222', .9) + text(268 if x > 140 else 8, (y-16 if y < 90 else y+24), L, 'end' if x > 140 else 'start', 14)
    return svg(285, 180, b)

def muscle_fig(kind):
    b = ""
    if kind == 'striated':
        for r in range(3):
            y = 18+r*38; b += f"<rect x='15' y='{y}' width='230' height='28' fill='#f6d5d5' stroke='#7b1f1f'/>"
            for x in range(25, 240, 10): b += line(x, y, x, y+28, '#b23a3a', 1.2)
            for x in (70, 150, 210): b += f"<ellipse cx='{x}' cy='{y+4}' rx='6' ry='3' fill='#4a148c'/>"
    elif kind == 'smooth':
        for r, x0 in enumerate((20, 55, 90, 125, 160)):
            b += f"<ellipse cx='{x0+40}' cy='{70+(r%2)*14}' rx='45' ry='9' fill='#f6d5d5' stroke='#7b1f1f' transform='rotate(-18 {x0+40} {70+(r%2)*14})'/><ellipse cx='{x0+40}' cy='{70+(r%2)*14}' rx='6' ry='3' fill='#4a148c' transform='rotate(-18 {x0+40} {70+(r%2)*14})'/>"
    else:
        for r in range(3):
            y = 18+r*38; b += f"<rect x='15' y='{y}' width='150' height='24' fill='#f6d5d5' stroke='#7b1f1f'/>" + line(165, y+12, 205, y+30 if r < 2 else y-10, '#7b1f1f', 5)
            for x in range(25, 160, 12): b += line(x, y, x, y+24, '#b23a3a', 1.1)
            b += f"<ellipse cx='85' cy='{y+12}' rx='6' ry='3.5' fill='#4a148c'/>" + line(160, y, 160, y+24, '#000', 2.4)
    return svg(260, 140, b)

def lever_fig(L_load, L_eff, load='Load', eff='Effort'):
    tot = L_load+L_eff; k = 220/tot; fx = 30+L_load*k
    b = line(30, 70, 250, 70, '#000', 5) + poly([(fx, 72), (fx-14, 100), (fx+14, 100)], '#000', '#888') + text(fx, 114, 'F', sz=12)
    b += arrow(30, 25, 30, 64, '#2c5aa0') + text(30, 18, load, sz=11) + arrow(250, 112, 250, 76, '#c0392b') + text(250, 126, eff, sz=11)
    b += line(30, 124, fx, 124, '#555', 1) + text((30+fx)/2, 138, f"{L_load} m", sz=11) + line(fx, 140, 250, 140, '#555', 1) + text((fx+250)/2, 154, f"{L_eff} m", sz=11)
    return svg(280, 162, b)

def wave_fig(label_lambda=True, A=None):
    pts = " ".join(f"{20+x*2.2:.1f},{70-30*math.sin(x/20*2*math.pi):.1f}" for x in range(0, 101))
    b = f"<polyline points='{pts}' fill='none' stroke='#0f2347' stroke-width='2'/>" + line(20, 70, 250, 70, '#999', 1, '4,3')
    b += text(20+5*2.2, 28, 'P', sz=13) + text(20+15*2.2, 118, 'Q', sz=13) + text(20+25*2.2, 28, 'R', sz=13)
    return svg(270, 130, b)

def incline_fig(L, h):
    b = poly([(30, 120), (230, 120), (230, 120-h*8)], '#000', '#eef2fa', 1.6) + text(115, 85-h*2, f"{L} m", sz=12) + line(236, 120, 236, 120-h*8, '#555', 1) + text(255, 124-h*4, f"{h} m", sz=12)
    return svg(285, 140, b)

def circle_track(r, rounds=''):
    b = circ(130, 90, 62, '#0f2347', '#eef2fa', 2) + dot(130, 28, 'Start', 6, -4) + line(130, 90, 192, 90, '#c0392b', 1.4) + text(162, 84, f"r = {r} m", sz=11) + dot(130, 90)
    return svg(260, 170, b)

def flower_fig(labels):
    L = labels; b = ""
    b += f"<ellipse cx='130' cy='150' rx='34' ry='16' fill='#c5e1a5' stroke='#33691e'/>"
    b += f"<rect x='124' y='55' width='12' height='60' fill='#fff9c4' stroke='#827717'/>" + f"<ellipse cx='130' cy='120' rx='22' ry='28' fill='#ffe0b2' stroke='#e65100' stroke-width='1.6'/>"
    for dx in (-8, 8): b += circ(130+dx, 122, 5, '#e65100', '#ffb74d', 1)
    b += f"<ellipse cx='130' cy='50' rx='13' ry='7' fill='#ce93d8' stroke='#6a1b9a'/>"
    for sx in (-52, 52): b += line(130+sx, 125, 130+sx*.9, 70, '#827717', 3) + f"<ellipse cx='{130+sx*.9}' cy='64' rx='9' ry='12' fill='#ffd54f' stroke='#8d6e00'/>"
    for sx in (-1, 1): b += f"<ellipse cx='{130+sx*60}' cy='128' rx='20' ry='42' fill='#f8bbd0' stroke='#ad1457' transform='rotate({sx*-20} {130+sx*60} 128)'/>"
    pos = dict(stigma=(130, 50, 215, 30), style=(130, 85, 215, 70), ovary=(130, 125, 215, 125), ovule=(138, 122, 215, 150), anther=(130+52*.9, 64, 215, 55), filament=(130+52*.9, 100, 215, 100), petal=(190, 128, 215, 138), sepal=(130, 150, 215, 165))
    for k, Lb in L.items():
        x, y, tx, ty = pos[k]; b += line(x, y, tx, ty, '#222', .9) + text(tx+6, ty+4, Lb, 'start', 14)
    return svg(250, 180, b)

def pyramid_fig(levels):
    n = len(levels); b = ""
    for i, (name, val) in enumerate(levels):
        w0 = 220-i*(180/n); w1 = 220-(i+1)*(180/n); y = 20+ (n-1-i)*0  # bottom first
    # draw bottom to top
    h = 30; W = 260
    for i, (name, val) in enumerate(levels):
        yb = 20+(n-i)*h; yt = yb-h; wb = 220*(1-i/n); wt = 220*(1-(i+1)/n); cx = 130
        b += poly([(cx-wb/2, yb), (cx+wb/2, yb), (cx+wt/2, yt), (cx-wt/2, yt)], '#0f2347', ['#c8e6c9', '#fff9c4', '#ffe0b2', '#f8bbd0'][i % 4], 1.2) + text(cx, yb-11, f"{name}: {val}", sz=11)
    return svg(W, 40+n*h, b)

def cycle_fig(nodes, W=260, H=190):
    n = len(nodes); cx, cy, R = W/2, H/2, 70; b = ""; pts = []
    for i, t in enumerate(nodes):
        a = 2*math.pi*i/n - math.pi/2; pts.append((cx+R*1.15*math.cos(a), cy+R*math.sin(a)))
    for i in range(n):
        x1, y1 = pts[i]; x2, y2 = pts[(i+1) % n]; b += arrow(x1+(x2-x1)*.35, y1+(y2-y1)*.35, x1+(x2-x1)*.65, y1+(y2-y1)*.65, '#555', 1.6)
    for (x, y), t in zip(pts, nodes): b += f"<rect x='{x-34}' y='{y-11}' width='68' height='22' rx='5' fill='#eaf4ff' stroke='#2c5aa0'/>" + text(x, y+4, t, sz=10)
    return svg(W, H, b)

def chromatogram(spots, front=100, W=210):
    """spots: dict label -> distance(mm) from baseline; strip height fixed."""
    b = f"<rect x='60' y='10' width='60' height='150' fill='#fffdf2' stroke='#555'/>" + line(60, 150, 120, 150, '#999', 1, '3,3') + line(60, 150-front*.9, 120, 150-front*.9, '#c0392b', 1, '3,3') + text(160, 150-front*.9+4, 'Solvent front', 'middle', 10) + text(160, 154, 'Baseline', 'middle', 10)
    for i, (k, d) in enumerate(spots.items()): x = 75+i*15; b += circ(x, 150-d*.9, 4, '#4527a0', '#b39ddb', 1) + text(x, 168, k, sz=10)
    return svg(W, 180, b)

def tyndall():
    b = "".join(f"<rect x='{60+i*70}' y='30' width='44' height='80' rx='6' fill='#e8f4fd' stroke='#555'/>" for i in range(2)) + "".join(arrow(8, 70, 58+i*70, 70, '#f9a825', 1.6) for i in range(2))
    b += line(104, 70, 134, 70, '#f9a825', 1.6) + line(8, 70, 58, 70, '#f9a825', 1.6) + text(82, 128, 'X', sz=13) + text(152, 128, 'Y', sz=13)
    b += "".join(f"<circle cx='{82+dx}' cy='{70+dy}' r='1.4' fill='#444'/>" for dx, dy in [(-8, -10), (4, 14), (10, -20), (-12, 20), (6, 2)])
    return svg(220, 140, b)

def neuron_fig(labels):
    L = labels; b = ""
    for (x, y) in [(40, 30), (30, 60), (45, 95), (70, 110)]: b += line(x, y, 85, 70, '#4a148c', 2)
    b += circ(95, 70, 22, '#6a1b9a', '#e1bee7', 1.6) + circ(95, 70, 8, '#6a1b9a', '#6a1b9a')
    b += line(117, 70, 215, 70, '#4a148c', 4) + "".join(line(x, 66, x, 74, '#fff', 3) for x in (140, 165, 190))
    for (x, y) in [(235, 45), (240, 70), (235, 95)]: b += line(215, 70, x, y, '#4a148c', 2) + circ(x+4, y, 4, '#4a148c', '#b39ddb', 1)
    pos = dict(dendrite=(55, 40, 40, 14), body=(95, 55, 95, 14), axon=(160, 70, 160, 120), sheath=(140, 70, 130, 120), ending=(244, 70, 244, 120))
    for k, Lb in L.items(): x, y, tx, ty = pos[k]; b += line(x, y, tx, ty, '#222', .9) + text(tx, ty+(-3 if ty < 50 else 14), Lb, sz=14)
    return svg(270, 135, b)

def plasmo_fig():
    b = ""
    for i, (w, h, t) in enumerate([(70, 70, 'X'), (56, 56, 'Y'), (36, 36, 'Z')]):
        cx = 50+i*95; b += f"<rect x='{cx-37}' y='20' width='74' height='74' rx='6' fill='none' stroke='#2e7d32' stroke-width='3'/><rect x='{cx-w/2}' y='{57-h/2}' width='{w}' height='{h}' rx='10' fill='#e3f2fd' stroke='#555'/>" + text(cx, 112, t, sz=14)
    return svg(290, 125, b)
