import sys; sys.path.insert(0,'/home/claude/pat')
from figs import *

def arrow(x, y1, y2, c='#c00', lab=''):
    d = 1 if y2 > y1 else -1
    s = line(x, y1, x, y2, c, 2.2) + f"<polygon points='{x-4},{y2-6*d} {x+4},{y2-6*d} {x},{y2}' fill='{c}'/>"
    return s + (text(x, y2+(13 if d>0 else -5), lab, sz=11, c=c) if lab else '')

def ray_mirror(u, f, h=3, s=5):
    """Concave mirror (real object distance u>f, cm). Axis y=100, mirror at x=X0. scale s px/cm. returns svg."""
    X0 = 330; Y = 105
    xo = X0 - u*s; ho = h*s
    v = u*f/(u-f); xi = X0 - v*s; hi = ho*v/u
    b = line(10, Y, X0+30, Y, '#555', 1) + f"<path d='M{X0},{Y-70} Q{X0+22},{Y} {X0},{Y+70}' stroke='#000' stroke-width='3' fill='none'/>"
    b += dot(X0-f*s, Y, '', 0, 0) + text(X0-f*s, Y+16, 'F', sz=11) + dot(X0-2*f*s, Y, '', 0, 0) + text(X0-2*f*s, Y+16, 'C', sz=11) + text(X0+8, Y+16, 'P', sz=11)
    b += arrow(xo, Y, Y-ho, '#0a5', 'O')
    tip = (xo, Y-ho)
    b += line(tip[0], tip[1], X0, tip[1], '#0f2347', 1.2) + line(X0, tip[1], xi, Y+hi, '#0f2347', 1.2)
    b += line(tip[0], tip[1], X0, Y, '#0f2347', 1.2) + line(X0, Y, xi, Y+hi, '#0f2347', 1.2)
    b += arrow(xi, Y, Y+hi, '#c00', 'I')
    return svg(360, 190, b)

def ray_lens(u, f, h=3, s=5, label_f=True):
    """Convex lens, real object u>f. lens at x=X0"""
    X0 = 190; Y = 100
    xo = X0 - u*s; ho = h*s
    v = u*f/(u-f); xi = X0 + v*s; hi = ho*v/u
    W = int(max(X0+v*s+30, 380))
    b = line(5, Y, W-5, Y, '#555', 1) + line(X0, Y-60, X0, Y+60, '#000', 2.6) + f"<polygon points='{X0-5},{Y-52} {X0+5},{Y-52} {X0},{Y-62}' fill='#000'/><polygon points='{X0-5},{Y+52} {X0+5},{Y+52} {X0},{Y+62}' fill='#000'/>"
    for k, lab in ((1, 'F'), (2, '2F')):
        b += dot(X0-k*f*s, Y, '', 0, 0) + text(X0-k*f*s, Y+16, lab+'₁', sz=10) + dot(X0+k*f*s, Y, '', 0, 0) + text(X0+k*f*s, Y+16, lab+'₂', sz=10)
    b += text(X0+8, Y+16, 'O', sz=10)
    b += arrow(xo, Y, Y-ho, '#0a5', 'AB')
    tip = (xo, Y-ho)
    b += line(tip[0], tip[1], X0, tip[1], '#0f2347', 1.2) + line(X0, tip[1], xi, Y+hi, '#0f2347', 1.2) + line(tip[0], tip[1], xi, Y+hi, '#0f2347', 1.2)
    b += arrow(xi, Y, Y+hi, '#c00', "A'B'")
    return svg(W, 200, b)

def circuit(kind, labels, battery='6 V'):
    """kind: 'series' (R1,R2,R3 in series), 'par2' (R1||R2 in series with R3), 'par3' (three parallel), 'mix' (R1 in series with (R2||R3))."""
    b = ""; W, H = 320, 150
    def res(x, y, lab, vert=False):
        if vert: return f"<rect x='{x-6}' y='{y-16}' width='12' height='32' fill='#fff' stroke='#000' stroke-width='1.6'/>" + text(x+16, y+4, lab, 'start', 11)
        return f"<rect x='{x-16}' y='{y-6}' width='32' height='12' fill='#fff' stroke='#000' stroke-width='1.6'/>" + text(x, y-10, lab, sz=11)
    b += line(30, 30, 290, 30) + line(30, 120, 290, 120) + line(30, 30, 30, 120) + line(290, 30, 290, 120)
    b += f"<rect x='24' y='64' width='12' height='24' fill='#fff'/>" + line(22, 70, 38, 70, '#000', 3) + line(26, 80, 34, 80, '#000', 1.6) + text(44, 62, battery, 'start', 11)
    if kind == 'series':
        for x, l in zip((90, 160, 230), labels): b += f"<rect x='{x-30}' y='20' width='60' height='20' fill='#fff'/>" + res(x, 30, l)
    elif kind == 'par3':
        b += line(150, 30, 150, 120) + line(250, 30, 250, 120)
        for yy, l in zip((50, 75, 100), labels): b += line(150, yy, 250, yy) + res(200, yy, l)
        b = b.replace(line(150, 30, 150, 120), line(150, 30, 150, 120))
    elif kind == 'mix':
        b += f"<rect x='60' y='20' width='60' height='20' fill='#fff'/>" + res(90, 30, labels[0])
        b += line(190, 30, 190, 120) + line(260, 30, 260, 120)
        for yy, l in zip((60, 95), labels[1:]): b += line(190, yy, 260, yy) + res(225, yy, l)
    elif kind == 'par2':
        b += f"<rect x='200' y='20' width='60' height='20' fill='#fff'/>" + res(230, 30, labels[2])
        b += line(80, 30, 80, 120) + line(150, 30, 150, 120)
        for yy, l in zip((60, 95), labels[:2]): b += line(80, yy, 150, yy) + res(115, yy, l)
    return svg(W, H, b)

def tissue_box(): return ""

def table_html(rows, head=None):
    h = "<table class='t'>" + (("<tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr>") if head else "")
    return h + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"

def bar_pyramid(levels):
    """levels bottom->top list of (label, value)"""
    b = ""; n = len(levels)
    for i, (lab, val) in enumerate(levels):
        w = 220 - i*(180/max(n-1, 1)); y = 20 + (n-1-i)*30
        b += f"<rect x='{140-w/2}' y='{y}' width='{w}' height='26' fill='#cfe3c7' stroke='#333'/>" + text(140, y+17, f"{lab}: {val}", sz=11)
    return svg(280, 30*n+30, b)

def solenoid():
    b = line(40, 70, 70, 70) + line(230, 70, 260, 70)
    for x in range(70, 231, 20): b += f"<ellipse cx='{x+10}' cy='70' rx='7' ry='26' fill='none' stroke='#000' stroke-width='1.6'/>"
    b += line(40, 70, 40, 125) + line(260, 70, 260, 125) + line(40, 125, 260, 125) + text(150, 118, 'Battery', sz=11) + text(150, 25, 'Solenoid', sz=11)
    return svg(300, 140, b)

def straight_wire_compass(): 
    b = circ(150, 80, 8, '#000', '#fff') + "<circle cx='150' cy='80' r='2' fill='#000'/>" + text(150, 20, 'Current coming out of the page (towards you)', sz=11)
    for r in (35, 60): b += circ(150, 80, r, '#888', 'none', 1)
    return svg(300, 150, b + text(150, 142, 'Concentric circles show the field lines', sz=10))

def heart():
    b = "<path d='M150 40 C110 10 60 40 80 90 C95 130 140 150 150 165 C160 150 205 130 220 90 C240 40 190 10 150 40Z' fill='#f6d5d5' stroke='#900' stroke-width='2'/>" + line(150, 45, 150, 160, '#900', 1.4) + line(85, 85, 215, 85, '#900', 1.4)
    for x, y, t in ((115, 62, 'P'), (185, 62, 'Q'), (115, 118, 'R'), (185, 118, 'S')): b += text(x, y, t, sz=15)
    return svg(300, 180, b)

def neuron():
    b = "<circle cx='60' cy='70' r='18' fill='#fde7a8' stroke='#333' stroke-width='1.6'/>" + text(60, 74, 'P', sz=13)
    for a in (-35, 0, 35): b += line(46, 62, 12, 70+a*0.6, '#333', 1.6)
    b += text(18, 40, 'Q', sz=13) + line(78, 70, 250, 70, '#333', 3) + text(150, 60, 'R', sz=13)
    b += f"<rect x='110' y='64' width='24' height='12' fill='#fff' stroke='#333'/><rect x='150' y='64' width='24' height='12' fill='#fff' stroke='#333'/>"
    for a in (-28, 0, 28): b += line(250, 70, 285, 70+a, '#333', 1.6)
    b += text(285, 50, 'S', sz=13)
    return svg(310, 120, b)

def flower_ls():
    b = "<path d='M150 170 L150 120' stroke='#2a7' stroke-width='5'/><ellipse cx='150' cy='105' rx='22' ry='18' fill='#ffe9a0' stroke='#333' stroke-width='1.4'/>"
    b += "<path d='M150 95 L150 40' stroke='#c47' stroke-width='3'/><circle cx='150' cy='38' r='6' fill='#c47'/>" + text(172, 40, 'P', 'start', 13)
    b += "<path d='M138 100 L110 60' stroke='#666' stroke-width='2'/><rect x='100' y='48' width='14' height='16' fill='#e9c46a' stroke='#333'/>" + text(94, 56, 'Q', 'end', 13)
    b += text(176, 110, 'R', 'start', 13) + "<circle cx='146' cy='106' r='3' fill='#8a5'/><circle cx='155' cy='106' r='3' fill='#8a5'/>" + text(150, 188, 'Longitudinal section of a flower (simplified)', sz=10)
    return svg(300, 195, b)

def eye(defect='myopia'):
    b = "<ellipse cx='150' cy='80' rx='70' ry='50' fill='#fff' stroke='#333' stroke-width='1.8'/><ellipse cx='95' cy='80' rx='9' ry='22' fill='#cde' stroke='#333'/>" + line(30, 60, 86, 74, '#0f2347') + line(30, 100, 86, 86, '#0f2347')
    if defect == 'myopia': b += line(86, 74, 130, 80, '#0f2347') + line(86, 86, 130, 80, '#0f2347') + dot(130, 80, 'X', 4, -6) + text(150, 150, 'Parallel rays focus at X, in front of the retina', sz=10)
    else: b += line(86, 74, 215, 80, '#0f2347') + line(86, 86, 215, 80, '#0f2347') + dot(215, 80, 'X', 4, -6) + text(150, 150, 'Parallel rays would meet at X, behind the retina', sz=10)
    b += line(205, 50, 205, 110, '#c00', 2.6) + text(205, 126, 'Retina', sz=10)
    return svg(300, 160, b)

def prism():
    b = poly([(110, 110), (190, 110), (150, 40)], '#333', '#e8f1ff') + line(20, 90, 128, 82, '#555', 2)
    cols = ['#e00', '#f80', '#fd0', '#2a2', '#26f', '#52c', '#a2c']
    for i, c in enumerate(cols): b += line(172, 78, 280, 70+i*6, c, 2)
    b += text(210, 30, 'White light →', sz=10) + text(24, 80, 'White light', 'start', 10)
    return svg(300, 130, b)

def electrolysis():
    b = f"<rect x='90' y='60' width='120' height='70' fill='#cfe8ff' stroke='#000' stroke-width='2'/>"
    for x, t in ((125, 'P'), (175, 'Q')):
        b += f"<rect x='{x-18}' y='20' width='36' height='90' fill='#f6f6f6' stroke='#000'/>" + line(x, 20, x, 110, '#555', 3) + text(x, 15, t, sz=13)
    b += text(125, 50, 'gas', sz=10) + text(175, 70, 'gas', sz=10) + line(100, 130, 100, 150, '#000') + line(200, 130, 200, 150, '#000') + line(100, 150, 200, 150, '#000') + text(150, 168, 'Battery', sz=11)
    return svg(300, 180, b)

def test_tube_setup(top='Iron nail', liq='CuSO₄ solution'):
    b = f"<path d='M120 20 L120 130 Q150 160 180 130 L180 20' fill='none' stroke='#000' stroke-width='2'/><path d='M121 70 L121 130 Q150 158 179 130 L179 70Z' fill='#bfe0ff'/><rect x='146' y='30' width='8' height='95' fill='#888' stroke='#333'/>" + text(150, 178, f'{top} in {liq}', sz=11)
    return svg(300, 190, b)

def punnett(rows, cols, cells):
    return table_html([[rows[i]] + cells[i] for i in range(len(rows))], head=['×'] + cols)

def refraction_glass():
    b = f"<rect x='90' y='40' width='120' height='90' fill='#dbeaff' stroke='#333' stroke-width='1.6'/>" + line(30, 20, 130, 40, '#0f2347') + line(130, 40, 150, 130, '#0f2347') + line(150, 130, 250, 150, '#0f2347') + line(130, 40, 130, 20, '#888', 1, '4') + text(30, 14, 'Incident ray', 'start', 10) + text(250, 168, 'Emergent ray', 'end', 10)
    return svg(300, 180, b)
