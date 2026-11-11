import math, random
from figs import svg, line, circ, text, poly, dot
def arrow(x1, y1, x2, y2, c='#c0392b', w=2):
    a = math.atan2(y2-y1, x2-x1); h = 8
    p = [(x2, y2), (x2-h*math.cos(a-.4), y2-h*math.sin(a-.4)), (x2-h*math.cos(a+.4), y2-h*math.sin(a+.4))]
    return line(x1, y1, x2, y2, c, w) + poly(p, c, c, 1)
def rect(x, y, w, h, fill='none', c='#000', sw=1.5): return f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='{fill}' stroke='{c}' stroke-width='{sw}'/>"
def block_forces(left, right, label='Block'):
    b = rect(130, 50, 80, 50, '#e8eef8') + text(170, 80, label)
    b += line(60, 100, 280, 100, '#000', 2)
    if left: b += arrow(130, 75, 130-left[0]*10, 75) + text(130-left[0]*10-14, 70, left[1], 'end')
    if right: b += arrow(210, 75, 210+right[0]*10, 75) + text(210+right[0]*10+6, 70, right[1], 'start')
    return svg(340, 120, b)
def particles(state, w=170, h=110):
    b = rect(2, 2, w, h, '#fafafa', '#555', 1.2); r = random.Random({'solid': 1, 'liquid': 2, 'gas': 3}[state])
    if state == 'solid':
        for i in range(6):
            for j in range(4): b += circ(22+i*25, 20+j*25, 8, '#1f4e8c', '#9db9e3', 1)
    elif state == 'liquid':
        pts = []
        for j in range(4):
            for i in range(6): pts.append((18+i*26+r.randint(-4, 4)+(j%2)*8, 70+(j-1)*0+j*9-27+r.randint(-3, 3)))
        for x, y in pts[:18]: b += circ(x, 40+ (y-40), 8, '#1f4e8c', '#9db9e3', 1)
    else:
        for _ in range(9): b += circ(r.randint(14, w-14), r.randint(14, h-14), 8, '#1f4e8c', '#9db9e3', 1)
    return svg(w+4, h+4, b)
def three_states():
    return "<table class='t' style='margin:auto'><tr>" + "".join(f"<td>{particles(s)}<br><b>{n}</b></td>" for s, n in (('solid', 'P'), ('liquid', 'Q'), ('gas', 'R'))) + "</tr></table>"
def electromagnet():
    b = rect(100, 60, 120, 30, '#cfd6e0', '#444')
    for i in range(8): b += line(108+i*14, 52, 114+i*14, 98, '#b36b00', 2.2)
    b += line(108, 52, 60, 52, '#000') + line(60, 52, 60, 160, '#000') + line(60, 160, 140, 160, '#000')
    b += rect(140, 150, 20, 20, '#fff') + rect(160, 145, 14, 30, '#222', '#222') + line(174, 160, 250, 160, '#000') + line(250, 160, 250, 98, '#000') + line(250, 98, 214, 98, '#000')
    b += text(120, 190, 'Cell') + text(160, 30, 'Iron nail with insulated copper coil') + text(285, 125, 'Switch', 'middle')
    for i in range(4): b += circ(105+i*10, 112, 3, '#555', '#aaa', 1)
    b += text(125, 132, 'Iron pins', 'middle')
    return svg(330, 200, b)
def compass_wire():
    b = line(30, 70, 300, 70, '#b36b00', 4) + circ(165, 120, 26, '#444', '#fff', 1.5) + arrow(165, 120, 175, 98, '#c0392b', 2) + line(165, 120, 155, 142, '#1f4e8c', 3)
    b += text(60, 60, 'Current-carrying wire', 'start') + text(205, 125, 'Compass needle', 'start') + text(165, 175, 'Magnetic compass', 'middle')
    return svg(330, 190, b)
def pressure_tank():
    b = rect(90, 20, 120, 160, '#e8f1fb', '#444', 2)
    for y in (60, 100, 140): b += line(210, y, 250, y, '#1f4e8c', 2) + arrow(210, y, 215+ (y-20)*0.35, y, '#1f4e8c', 2)
    b += text(60, 65, 'A', 'end') + text(60, 105, 'B', 'end') + text(60, 145, 'C', 'end')
    for y in (60, 100, 140): b += circ(90, y, 3, '#000', '#000', 1)
    b += text(150, 195, 'Water-filled container with holes A, B, C')
    return svg(300, 205, b)
def concave_mirror():
    b = line(20, 100, 340, 100, '#444', 1.2)
    b += f"<path d='M 300 20 Q 330 100 300 180' fill='none' stroke='#000' stroke-width='3'/>"
    b += dot(250, 100, 'F', -4, 16) + dot(200, 100, 'C', -4, 16) + dot(300, 100, 'P', 6, 16)
    b += arrow(130, 100, 130, 60, '#1f4e8c', 3) + text(130, 118, 'Object', 'middle')
    b += line(130, 60, 300, 60, '#c0392b') + line(300, 60, 190, 100, '#c0392b', 1.4) + line(130, 60, 300, 108, '#2c7a3f')
    return svg(350, 200, b)
def earth_layers():
    b = circ(130, 110, 100, '#222', '#e8d7b0') + circ(130, 110, 72, '#222', '#d4a373') + circ(130, 110, 46, '#222', '#e76f51') + circ(130, 110, 20, '#222', '#f4a261')
    b += text(130, 114, 'D', 'middle', 11) + text(130, 66, 'C', 'middle', 11) + text(130, 36, 'B', 'middle', 11) + text(130, 20, 'A', 'middle', 11)
    return svg(270, 220, b)
def food_web():
    b = ""
    nodes = {'Grass': (60, 120), 'Grasshopper': (160, 60), 'Frog': (260, 60), 'Snake': (350, 90), 'Mouse': (160, 170), 'Hawk': (440, 120)}
    for k, (x, y) in nodes.items(): b += rect(x-34, y-13, 68, 26, '#eef5ee', '#2c7a3f', 1.2) + text(x, y+4, k, 'middle', 11)
    for a, c in (('Grass', 'Grasshopper'), ('Grasshopper', 'Frog'), ('Frog', 'Snake'), ('Snake', 'Hawk'), ('Grass', 'Mouse'), ('Mouse', 'Snake')):
        (x1, y1), (x2, y2) = nodes[a], nodes[c]; dx, dy = x2-x1, y2-y1; d = math.hypot(dx, dy); u = (dx/d, dy/d)
        b += arrow(x1+u[0]*36, y1+u[1]*17, x2-u[0]*38, y2-u[1]*19, '#555', 1.6)
    return svg(500, 200, b)
def moon_phase_row():
    b = ""
    for i, ph in enumerate((0.0, 0.25, 0.5, 0.75)):
        cx = 50+i*100; b += circ(cx, 50, 28, '#333', '#222')
        if ph == 0.5: b += circ(cx, 50, 28, '#333', '#f5f0c8')
        elif ph == 0.25: b += f"<path d='M {cx} 22 A 28 28 0 0 1 {cx} 78 A 14 28 0 0 0 {cx} 22' fill='#f5f0c8'/>"
        elif ph == 0.75: b += f"<path d='M {cx} 22 A 28 28 0 0 1 {cx} 78 A 14 28 0 0 1 {cx} 22' fill='#f5f0c8'/>"
        b += text(cx, 100, 'PQRS'[i], 'middle', 13)
    return svg(400, 110, b)
