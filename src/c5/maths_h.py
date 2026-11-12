"""Shared helpers for Class 5 Maths model papers 6-10 (figures, MCQ builder, Indian number format)."""
import sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib5 import *            # noqa
from fractions import Fraction as Fr

LET = "abcd"

def mc(q, correct, others, pos, fig=None, why=""):
    correct = str(correct); others = [str(x) for x in others]
    assert len(others) == 3 and len(set(others + [correct])) == 4, (q, correct, others)
    o = others[:]; o.insert(pos, correct)
    return Q(q, 1, f"({LET[pos]}) {correct}" + (f" &mdash; {why}" if why else ""), opts=o, fig=fig)

def ind(n):
    s = str(n)
    if len(s) <= 3: return s
    h, r, parts = s[-3:], s[:-3], []
    while len(r) > 2: parts.insert(0, r[-2:]); r = r[:-2]
    if r: parts.insert(0, r)
    return ",".join(parts + [h])

def intl(n): return f"{n:,}"
def rs(n): return f"&#8377; {ind(n)}"

def shape(rows): return {(c, r) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == "#"}

def perim(cells):
    return sum(1 for (c, r) in cells for d in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (c + d[0], r + d[1]) not in cells)

def tbl(headers, rows):
    return ("<table class='t5'><tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>" +
            "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>")

def tally(n):
    return "<span style='letter-spacing:1px;font-weight:700'>" + ("<s>||||</s> " * (n // 5)) + "|" * (n % 5) + "</span>"

def meta(n):
    return dict(subject="Maths", set_no=n, time="2.30 Hours", marks=80, instr=[
        "This question paper is based on the learning areas of Class 5 Mathematics (Shape and Space, Number System, Operations, Measurement, Data Handling and Patterns).",
        "Write your name and roll number in the space given on the question paper.",
        "All questions are compulsory.",
        "The marks for each question are shown against it.",
        "Write your answers neatly and show your working wherever it is needed."])

def finish(n, items):
    assert len(items) == 22
    secs = [sec("UNDERSTANDING SHAPE AND SPACE", 21, items[0:4]), sec("NUMBER SYSTEM", 9, items[4:8]),
            sec("OPERATIONS", 25, items[8:14]), sec("MEASUREMENT", 17, items[14:18]),
            sec("DATA HANDLING AND PATTERNS", 8, items[18:22])]
    print(build(meta(n), secs))

# ---------------- figures ----------------
def ang(deg, name, show=True):
    ox, oy, r = 26, 56, 48; t = math.radians(deg)
    x2, y2 = ox + r * math.cos(t), oy - r * math.sin(t)
    ex, ey = ox + 14 * math.cos(t), oy - 14 * math.sin(t)
    large = 1 if deg > 180 else 0
    cap = f"&ang;{name} = {deg}&deg;" if show else f"&ang;{name}"
    return (f"<svg width='110' height='116' viewBox='0 0 110 116' xmlns='http://www.w3.org/2000/svg'>"
            f"<line x1='{ox}' y1='{oy}' x2='{ox+r}' y2='{oy}' stroke='#222' stroke-width='1.6'/>"
            f"<line x1='{ox}' y1='{oy}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='#222' stroke-width='1.6'/>"
            f"<path d='M {ox+14} {oy} A 14 14 0 {large} 0 {ex:.1f} {ey:.1f}' fill='none' stroke='#c49a3c' stroke-width='1.6'/>"
            f"<text x='55' y='112' font-size='11' text-anchor='middle'>{cap}</text></svg>")

def angles(lst): return "<div style='display:flex;gap:6px'>" + "".join(ang(d, n) for n, d in lst) + "</div>"

def nl(a, b, n, pts, labels, w=340):
    x0, x1 = 22, w - 22
    s = f"<svg width='{w}' height='62' viewBox='0 0 {w} 62' xmlns='http://www.w3.org/2000/svg'><line x1='{x0-10}' y1='36' x2='{x1+10}' y2='36' stroke='#222' stroke-width='1.4'/>"
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        s += f"<line x1='{x:.1f}' y1='31' x2='{x:.1f}' y2='41' stroke='#222'/>"
        if i in labels: s += f"<text x='{x:.1f}' y='55' font-size='11' text-anchor='middle'>{labels[i]}</text>"
    for L, v in pts.items():
        t = (Fr(v) - Fr(a)) / (Fr(b) - Fr(a)); assert 0 <= t <= 1
        x = x0 + (x1 - x0) * float(t)
        s += f"<polygon points='{x-4:.1f},20 {x+4:.1f},20 {x:.1f},31' fill='#c49a3c'/><text x='{x:.1f}' y='15' font-size='12' font-weight='700' text-anchor='middle' fill='#13286b'>{L}</text>"
    return s + "</svg>"

def bars(labels, values, step, top, w=310, h=178, ylab="", xlab="", fill="#4a6fc4"):
    L, B, T = 40, h - 36, 16; n = len(values); bw = (w - L - 10) / n * 0.55
    s = f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'><line x1='{L}' y1='{T}' x2='{L}' y2='{B}' stroke='#222'/><line x1='{L}' y1='{B}' x2='{w-5}' y2='{B}' stroke='#222'/>"
    for k in range(0, top + 1, step):
        y = B - (B - T) * k / top
        s += f"<line x1='{L-3}' y1='{y:.1f}' x2='{L}' y2='{y:.1f}' stroke='#222'/><text x='{L-6}' y='{y+3:.1f}' font-size='9' text-anchor='end'>{k}</text>"
        if k: s += f"<line x1='{L}' y1='{y:.1f}' x2='{w-5}' y2='{y:.1f}' stroke='#e3e8f3'/>"
    for i, (lb, v) in enumerate(zip(labels, values)):
        cx = L + (w - L - 10) * (i + 0.5) / n; y = B - (B - T) * v / top
        s += f"<rect x='{cx-bw/2:.1f}' y='{y:.1f}' width='{bw:.1f}' height='{B-y:.1f}' fill='{fill}'/><text x='{cx:.1f}' y='{B+12}' font-size='9' text-anchor='middle'>{lb}</text>"
    if ylab: s += f"<text x='4' y='10' font-size='9'>{ylab}</text>"
    if xlab: s += f"<text x='{(L+w)/2:.0f}' y='{h-4}' font-size='9' text-anchor='middle'>{xlab}</text>"
    return s + "</svg>"

def plan(W, top, bot, h1, h2, ver=None, sc=22):
    assert sum(w for _, w in top) == W == sum(w for _, w in bot)
    H = h1 + h2 + (ver[1] if ver else 0); ox, oy = 6, 18
    s = f"<svg width='{W*sc+14}' height='{H*sc+26}' viewBox='0 0 {W*sc+14} {H*sc+26}' xmlns='http://www.w3.org/2000/svg'><text x='{ox}' y='12' font-size='10' font-weight='700' fill='#13286b'>N &uarr;</text>"
    def room(nm, x, y, w, h):
        cx, cy = ox + (x + w / 2) * sc, oy + (y + h / 2) * sc
        return (f"<rect x='{ox+x*sc}' y='{oy+y*sc}' width='{w*sc}' height='{h*sc}' fill='#f7f9fd' stroke='#13286b' stroke-width='1.8'/>"
                f"<text x='{cx:.0f}' y='{cy-1:.0f}' font-size='10' font-weight='700' text-anchor='middle'>{nm}</text>"
                f"<text x='{cx:.0f}' y='{cy+11:.0f}' font-size='9' text-anchor='middle'>{w} m &times; {h} m</text>")
    x = 0
    for nm, w in top: s += room(nm, x, 0, w, h1); x += w
    x = 0
    for nm, w in bot: s += room(nm, x, h1, w, h2); x += w
    if ver: s += room(ver[0], 0, h1 + h2, W, ver[1])
    return s + "</svg>"

def route(nodes, edges, w=340, h=190):
    s = f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'>"
    for a, b, km in edges:
        (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]
        s += f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='#7a8bb5' stroke-width='2'/>"
    for a, b, km in edges:
        (x1, y1, _), (x2, y2, _) = nodes[a], nodes[b]; mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        s += f"<rect x='{mx-17:.0f}' y='{my-8:.0f}' width='34' height='15' fill='#fff' stroke='#c9d2e6'/><text x='{mx:.0f}' y='{my+4:.0f}' font-size='10' font-weight='700' text-anchor='middle' fill='#8a5a00'>{km} km</text>"
    for nm, (x, y, pos) in nodes.items():
        tx, ty, an = {"a": (x, y - 9, "middle"), "b": (x, y + 18, "middle"), "l": (x - 9, y + 4, "end"), "r": (x + 9, y + 4, "start")}[pos]
        s += f"<circle cx='{x}' cy='{y}' r='5' fill='#13286b'/><text x='{tx}' y='{ty}' font-size='11' font-weight='700' text-anchor='{an}'>{nm}</text>"
    return s + "</svg>"

def dist_table(names, d):
    def g(a, b): return d[(a, b)] if (a, b) in d else d[(b, a)]
    rows = [[a] + ["&mdash;" if a == b else g(a, b) for b in names] for a in names]
    return tbl(["km"] + names, rows)

def bulbs(n, colfn, per=12, r=11):
    rows = (n + per - 1) // per; w = per * (2 * r + 6) + 6
    s = f"<svg width='{w}' height='{rows*(2*r+8)+4}' xmlns='http://www.w3.org/2000/svg'>"
    for i in range(1, n + 1):
        c, rr = (i - 1) % per, (i - 1) // per; cx, cy = 3 + r + 3 + c * (2 * r + 6), 3 + r + rr * (2 * r + 8)
        s += f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{colfn(i)}' stroke='#13286b'/><text x='{cx}' y='{cy+4}' font-size='10' text-anchor='middle'>{i}</text>"
    return s + "</svg>"

def pats(sets, cw=11, fill="#9db6ea"):
    H = max(max(r for c, r in s) + 1 for s in sets) * cw
    x = 14; o = ""
    for i, st in enumerate(sets):
        W = max(c for c, r in st) + 1; hh = max(r for c, r in st) + 1
        for c, r in st: o += f"<rect x='{x+c*cw}' y='{4+H-hh*cw+r*cw}' width='{cw}' height='{cw}' fill='{fill}' stroke='#13286b'/>"
        o += f"<text x='{x+W*cw/2}' y='{H+18}' font-size='10' text-anchor='middle'>Fig. {i+1}</text>"
        x += W * cw + 20
    return f"<svg width='{x}' height='{H+24}' xmlns='http://www.w3.org/2000/svg'>{o}</svg>"

# pattern generators (sets of (col,row))
def stairs(n): return {(c, r) for r in range(n) for c in range(r + 1)}
def cross(n): return {(n, r) for r in range(2 * n + 1)} | {(c, n) for c in range(2 * n + 1)}
def hollow(k): return {(c, r) for c in range(k) for r in range(k) if c in (0, k - 1) or r in (0, k - 1)}
def ell(n): return {(0, r) for r in range(n)} | {(c, n - 1) for c in range(n)}
def rect(n, m): return {(c, r) for c in range(m) for r in range(n)}
def tri_rows(n): return {(c, r) for r in range(n) for c in range(2 * r + 1)}   # rows of 1,3,5,..
