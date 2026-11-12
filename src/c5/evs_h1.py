"""Shared helpers for Class 5 EVS model papers 1-5."""
import math
from lib5 import *

INSTR = [
    "This question paper is based on the learning areas of Class V Environmental Studies (EVS).",
    "Write your Name and Roll No. in the space given on the top of the question paper.",
    "All questions are compulsory.",
    "The marks for each question are given against it.",
    "Write your answers neatly and legibly.",
]
ROM = "i ii iii iv v".split()

def mcq(q, opts, k, fig=None, passage=None):
    return Q(q, 1, f"({'abcd'[k]}) {opts[k]}", opts=opts, fig=fig, passage=passage)

def parts(stem, marks, items, fig=None, passage=None):
    """items = [(question, marks, answer[, opts])]; labels (i), (ii)..."""
    ps = []
    for n, it in enumerate(items):
        ps.append(P(f"({ROM[n]})", it[0], it[1], it[2], opts=it[3] if len(it) > 3 else None))
    return Q(stem, marks, parts=ps, fig=fig, passage=passage)

def table(rows, head=None):
    h = "<table class='t5' style='margin-left:0'>"
    if head: h += "<tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr>"
    for r in rows: h += "<tr>" + "".join(f"<td style='text-align:left'>{c}</td>" for c in r) + "</tr>"
    return h + "</table>"

def emoji(txt, size=26):
    return f"<div style='font-size:{size}px;line-height:1.3'>{txt}</div>"

# ---- schematic locator map (positions from real latitude/longitude; NOT a boundary outline) ----
LL = {  # district headquarters (lat, lon)
    "Jaipur": (26.92, 75.79), "Bikaner": (28.02, 73.31), "Jodhpur": (26.24, 73.02), "Jaisalmer": (26.92, 70.91),
    "Udaipur": (24.58, 73.71), "Kota": (25.18, 75.83), "Ajmer": (26.45, 74.64), "Bharatpur": (27.22, 77.49),
    "Alwar": (27.55, 76.61), "Chittorgarh": (24.88, 74.62), "Sri Ganganagar": (29.92, 73.88), "Barmer": (25.75, 71.42),
    "Banswara": (23.55, 74.44), "Sawai Madhopur": (26.02, 76.35), "Churu": (28.30, 74.97), "Sikar": (27.61, 75.14),
    "Bundi": (25.44, 75.64), "Sirohi": (24.89, 72.86), "Nagaur": (27.20, 73.74), "Jhunjhunu": (28.13, 75.40),
    "Dholpur": (26.70, 77.89), "Hanumangarh": (29.58, 74.32), "Jhalawar": (24.60, 76.16), "Pali": (25.77, 73.33),
    "Dungarpur": (23.84, 73.71), "Bhilwara": (25.35, 74.63),
}

def direction(frm, to):
    (la1, lo1), (la2, lo2) = LL[frm], LL[to]
    dx = (lo2 - lo1) * math.cos(math.radians((la1 + la2) / 2)); dy = la2 - la1
    ang = (math.degrees(math.atan2(dx, dy)) + 360) % 360
    names = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]
    return names[int((ang + 22.5) // 45) % 8], ang

def svg_locator(targets, extra=(), w=330, h=300):
    """Dots A, B, C.. for `targets` (district names); Jaipur shown as a star; extra = other labelled reference towns."""
    lo0, lo1, la0, la1 = 70.0, 78.4, 23.2, 30.2
    k = math.cos(math.radians(26.5))
    sx = (w - 20) / ((lo1 - lo0) * k); sy = (h - 24) / (la1 - la0); s_ = min(sx, sy)
    X = lambda lo: 10 + (lo - lo0) * k * s_
    Y = lambda la: h - 12 - (la - la0) * s_
    o = f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'>"
    o += f"<rect x='1' y='1' width='{w-2}' height='{h-2}' fill='#fbfaf3' stroke='#9aa7c7' stroke-dasharray='4 3'/>"
    o += f"<text x='{w/2}' y='14' font-size='10' text-anchor='middle' fill='#555'>Schematic location map of Rajasthan (not to scale)</text>"
    jx, jy = X(LL['Jaipur'][1]), Y(LL['Jaipur'][0])
    o += f"<text x='{jx:.1f}' y='{jy+4:.1f}' font-size='17' text-anchor='middle' fill='#c49a3c'>&#9733;</text><text x='{jx+11:.1f}' y='{jy+3:.1f}' font-size='9' fill='#13286b'>Jaipur (capital)</text>"
    for nm in extra:
        x, y = X(LL[nm][1]), Y(LL[nm][0])
        o += f"<circle cx='{x:.1f}' cy='{y:.1f}' r='3' fill='#555'/><text x='{x+6:.1f}' y='{y+3:.1f}' font-size='9' fill='#333'>{nm}</text>"
    for i, nm in enumerate(targets):
        x, y = X(LL[nm][1]), Y(LL[nm][0])
        o += f"<circle cx='{x:.1f}' cy='{y:.1f}' r='7.5' fill='#d94b3d'/><text x='{x:.1f}' y='{y+3.6:.1f}' font-size='10' font-weight='700' fill='#fff' text-anchor='middle'>{'ABCD'[i]}</text>"
    # compass
    o += f"<g transform='translate({w-30},{h-58})'><line x1='0' y1='28' x2='0' y2='0' stroke='#13286b' stroke-width='2'/><polygon points='0,-4 -5,6 5,6' fill='#13286b'/><text x='0' y='-8' font-size='11' font-weight='700' text-anchor='middle' fill='#13286b'>N</text></g>"
    return o + "</svg>"

def run(no, items):
    """items = list of 22 Q objects."""
    assert len(items) == 22, len(items)
    g = lambda a, b: items[a - 1:b]
    secs = [
        sec("OUR ENVIRONMENT AND CULTURE", 11, g(1, 4)),
        sec("PLANTS, ANIMALS AND OUR RESPONSIBILITY", 12, g(5, 7)),
        sec("FOOD, WATER AND HOUSES", 14, g(8, 13)),
        sec("OUR PRIDE, PROFESSIONS AND ANALYSIS", 26, g(14, 17)),
        sec("TRANSPORT, COMMUNICATION AND LIFE SKILLS", 17, g(18, 22)),
    ]
    meta = dict(subject="EVS", set_no=no, time="2.30 Hours", marks=80, instr=INSTR)
    print(build(meta, secs))
