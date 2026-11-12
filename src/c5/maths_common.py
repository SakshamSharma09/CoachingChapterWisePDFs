"""Shared helpers for the Class 5 Maths model papers (figures + MCQ option shuffler)."""
import random, math
from lib5 import *

INSTR = ["This question paper is based on the learning areas of Class 5 Mathematics (Shape and Space, Number System, Operations, Measurement, Data Handling and Patterns).",
         "Write your Name and Roll No. clearly on the question paper / answer sheet.",
         "All questions are compulsory.",
         "The marks allotted to each question are given against it.",
         "Write your answers neatly and show the steps of working wherever required."]

def meta(n):
    return dict(subject="Maths", set_no=n, time="2.30 Hours", marks=80, instr=INSTR)

def fr(n, d):
    return f"<sup>{n}</sup>&frasl;<sub>{d}</sub>"

def mc(ans, wrong, seed):
    """returns (opts, answer-string) ; ans/wrong are strings; correct option placed pseudo-randomly."""
    wrong = list(wrong)
    assert len(wrong) == 3 and ans not in wrong and len(set(wrong)) == 3, (ans, wrong)
    pos = random.Random(seed).randrange(4)
    opts = wrong[:]; opts.insert(pos, ans)
    return opts, f"({'abcd'[pos]}) {ans}"

def indian(n):
    s = str(n)
    if len(s) <= 3: return s
    h = s[-3:]; r = s[:-3]; parts = []
    while len(r) > 2: parts.insert(0, r[-2:]); r = r[:-2]
    if r: parts.insert(0, r)
    return ",".join(parts + [h])

def intl(n): return f"{n:,}"

# ---------- floor plan ----------
def svg_plan(rooms, openings=(), u=22, W=None, H=None, note=""):
    """rooms [(name,x,y,w,h)] metres; openings [(kind,'D'|'W',x1,y1,x2,y2,label)]"""
    X = max(r[1] + r[3] for r in rooms); Y = max(r[2] + r[4] for r in rooms)
    pw, ph = X * u + 40, Y * u + 24
    s = f"<svg width='{pw}' height='{ph}' viewBox='0 0 {pw} {ph}' xmlns='http://www.w3.org/2000/svg' font-family='Arial'>"
    for nm, x, y, w, h in rooms:
        s += f"<rect x='{x*u+10}' y='{y*u+14}' width='{w*u}' height='{h*u}' fill='#fbfaf2' stroke='#222' stroke-width='2.2'/>"
        s += f"<text x='{x*u+10+w*u/2}' y='{y*u+14+h*u/2-1}' font-size='9.5' font-weight='700' text-anchor='middle'>{nm}</text>"
        s += f"<text x='{x*u+10+w*u/2}' y='{y*u+14+h*u/2+10}' font-size='8.5' text-anchor='middle' fill='#444'>{w} m × {h} m</text>"
    for kind, x1, y1, x2, y2, lab in openings:
        col = '#c0392b' if kind == 'D' else '#2e86c1'
        s += f"<line x1='{x1*u+10}' y1='{y1*u+14}' x2='{x2*u+10}' y2='{y2*u+14}' stroke='{col}' stroke-width='5'/>"
        s += f"<text x='{(x1+x2)*u/2+10+(0 if y1==y2 else 6)}' y='{(y1+y2)*u/2+14+(-4 if y1==y2 else 3)}' font-size='8' font-weight='700' fill='{col}' text-anchor='{'middle' if y1==y2 else 'start'}'>{lab}</text>"
    s += f"<text x='{pw-14}' y='11' font-size='9' font-weight='700' text-anchor='middle'>N↑</text>"
    s += "</svg>"
    return s + (f"<div style='font-size:8.5pt'>{note}</div>" if note else "")

# ---------- route map ----------
def svg_route(nodes, edges, w=330, h=170):
    s = f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' font-family='Arial'>"
    for a, b, km in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        s += f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='#7a8bb5' stroke-width='2'/>"
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        s += f"<rect x='{mx-17}' y='{my-8}' width='34' height='14' fill='#fff8e0' stroke='#c49a3c' rx='3'/><text x='{mx}' y='{my+3}' font-size='9' text-anchor='middle'>{km} km</text>"
    for nm, (x, y) in nodes.items():
        s += f"<circle cx='{x}' cy='{y}' r='5' fill='#13286b'/><text x='{x}' y='{y-9}' font-size='10' font-weight='700' text-anchor='middle'>{nm}</text>"
    return s + "</svg>"

# ---------- number line with lettered points ----------
def svg_nl(start, units, per, pts, w=330, fmt=None):
    """start int, units = number of whole units, per = parts per unit, pts {letter: parts from start}."""
    n = units * per; x0, x1 = 14, w - 14; dx = (x1 - x0) / n
    s = f"<svg width='{w}' height='56' viewBox='0 0 {w} 56' xmlns='http://www.w3.org/2000/svg' font-family='Arial'><line x1='{x0-8}' y1='28' x2='{x1+8}' y2='28' stroke='#222' stroke-width='1.5'/>"
    for i in range(n + 1):
        x = x0 + i * dx; big = i % per == 0
        s += f"<line x1='{x:.1f}' y1='{22 if big else 24}' x2='{x:.1f}' y2='{34 if big else 32}' stroke='#222'/>"
        if big:
            v = start + i // per
            s += f"<text x='{x:.1f}' y='48' font-size='10' text-anchor='middle'>{fmt(v) if fmt else v}</text>"
    for L, p in pts.items():
        x = x0 + p * dx
        s += f"<circle cx='{x:.1f}' cy='28' r='3.6' fill='#c0392b'/><text x='{x:.1f}' y='15' font-size='11' font-weight='700' fill='#c0392b' text-anchor='middle'>{L}</text>"
    return s + "</svg>"

# ---------- bulbs ----------
def svg_bulbs(n, lit, per_row=10, col="#f6c344"):
    """numbered bulbs 1..n ; lit = set of numbers that glow."""
    rows = (n + per_row - 1) // per_row; w = per_row * 32 + 6
    s = f"<div><svg width='{w}' height='{rows*34+4}' viewBox='0 0 {w} {rows*34+4}' xmlns='http://www.w3.org/2000/svg' font-family='Arial'>"
    for i in range(1, n + 1):
        r, c = divmod(i - 1, per_row); cx, cy = 18 + c * 32, 17 + r * 34
        s += f"<circle cx='{cx}' cy='{cy}' r='13' fill='{col if i in lit else '#e9ecf2'}' stroke='#555'/><text x='{cx}' y='{cy+4}' font-size='10' font-weight='700' text-anchor='middle'>{i}</text>"
    return s + "</svg></div>"

# ---------- shape patterns ----------
def svg_stairs(ks, cw=13):
    """staircase figures with k steps each (squares)."""
    W = sum(k * cw + 22 for k in ks); H = max(ks) * cw + 22
    s = f"<svg width='{W}' height='{H+12}' xmlns='http://www.w3.org/2000/svg' font-family='Arial'>"; x = 6
    for i, k in enumerate(ks):
        for c in range(k):
            for r in range(c + 1):
                s += f"<rect x='{x+c*cw}' y='{4+(k-1-r)*cw}' width='{cw}' height='{cw}' fill='#9db6ea' stroke='#13286b'/>"
        s += f"<text x='{x}' y='{H+10}' font-size='9'>Fig. {i+1}</text>"; x += k * cw + 22
    return s + "</svg>"

def svg_rowsq(ks, cw=14):
    """squares in a row made of matchsticks: fig with k squares."""
    W = sum(k * cw + 30 for k in ks); H = cw + 28
    s = f"<svg width='{W}' height='{H}' xmlns='http://www.w3.org/2000/svg' font-family='Arial'>"; x = 6
    for i, k in enumerate(ks):
        s += f"<rect x='{x}' y='4' width='{k*cw}' height='{cw}' fill='none' stroke='#c0392b' stroke-width='2'/>"
        for c in range(1, k): s += f"<line x1='{x+c*cw}' y1='4' x2='{x+c*cw}' y2='{4+cw}' stroke='#c0392b' stroke-width='2'/>"
        s += f"<text x='{x}' y='{cw+20}' font-size='9'>Fig. {i+1}</text>"; x += k * cw + 30
    return s + "</svg>"

def svg_tritri(ks, cw=12):
    """pyramid of small triangles: fig k has k rows (k*k triangles) drawn as stacked dots"""
    W = sum(k * cw + 26 for k in ks); H = max(ks) * cw + 24
    s = f"<svg width='{W}' height='{H}' xmlns='http://www.w3.org/2000/svg' font-family='Arial'>"; x = 6
    for i, k in enumerate(ks):
        for r in range(k):
            for c in range(r + 1):
                cx = x + k * cw / 2 + (c - r / 2) * cw; cy = 8 + r * cw
                s += f"<circle cx='{cx:.1f}' cy='{cy}' r='4' fill='#4a6fc4'/>"
        s += f"<text x='{x}' y='{H-2}' font-size='9'>Fig. {i+1}</text>"; x += k * cw + 26
    return s + "</svg>"

def svg_clockface_free(): return ""

def tab(rows, head=None):
    h = "<table class='t5'>"
    if head: h += "<tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr>"
    for r in rows: h += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</table>"

def tiles_svg(cols, rows, cw=18, label_w="", label_h=""):
    W, H = cols * cw + 40, rows * cw + 30
    s = f"<svg width='{W}' height='{H}' xmlns='http://www.w3.org/2000/svg' font-family='Arial'>"
    for r in range(rows):
        for c in range(cols):
            s += f"<rect x='{20+c*cw}' y='{4+r*cw}' width='{cw}' height='{cw}' fill='#f1d9a8' stroke='#8a6a2b'/>"
    s += f"<text x='{20+cols*cw/2}' y='{H-4}' font-size='9' text-anchor='middle'>{label_w}</text>"
    s += f"<text x='6' y='{4+rows*cw/2}' font-size='9' text-anchor='middle' transform='rotate(-90 6 {4+rows*cw/2})'>{label_h}</text>"
    return s + "</svg>"

def run(m, secs):
    r = build(m, secs)
    print(r)
