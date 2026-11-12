"""Shared helpers for Class 5 EVS model papers 6-10 (schematic Rajasthan city map, MCQ/table/match builders)."""
import sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib5 import *

def mcq(q, opts, k, fig=None):
    return Q(q, 1, f"({'abcd'[k]}) {opts[k]}", opts=opts, fig=fig)

def tbl(head, rows):
    return ("<table class='t5'><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" +
            "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>")

def match(a, b, ha="Column A", hb="Column B"):
    r = "".join(f"<tr><td>{i+1}. {x}</td><td>{'abcde'[i]}. {y}</td></tr>" for i, (x, y) in enumerate(zip(a, b)))
    return f"<table class='t5'><tr><th>{ha}</th><th>{hb}</th></tr>{r}</table>"

def pic(s, size=30):
    return f"<div style='font-size:{size}px;line-height:1.2'>{s}</div>"

# (lon, lat) approximate positions -> schematic only (not to scale, no outline)
CITY = {"Ganganagar": (73.88, 29.92), "Bikaner": (73.31, 28.02), "Jaisalmer": (70.9, 26.9), "Jodhpur": (73.02, 26.29),
        "Ajmer": (74.64, 26.45), "Jaipur": (75.79, 26.91), "Alwar": (76.6, 27.55), "Bharatpur": (77.49, 27.22),
        "Kota": (75.84, 25.18), "Udaipur": (73.71, 24.58), "Mount Abu": (72.71, 24.59), "Banswara": (74.44, 23.55)}

def direction(a, b):
    """compass direction of city b as seen from city a (8-point)."""
    dx = CITY[b][0] - CITY[a][0]; dy = CITY[b][1] - CITY[a][1]
    ang = (math.degrees(math.atan2(dx, dy)) + 360) % 360   # 0 = north, clockwise
    return ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"][int((ang + 22.5) // 45) % 8]

def svg_cities():
    W, H = 372, 286
    X = lambda lon: (lon - 70.5) * 40 + 15
    Y = lambda lat: (30.2 - lat) * 38 + 10
    s = f"<svg width='{W}' height='{H}' viewBox='0 0 {W} {H}' xmlns='http://www.w3.org/2000/svg'><rect x='1' y='1' width='{W-2}' height='{H-2}' fill='#fbfcff' stroke='#9aa7c7'/>"
    s += "<g stroke='#13286b' stroke-width='1.4' fill='#13286b'><line x1='345' y1='62' x2='345' y2='26'/><polygon points='345,20 340,30 350,30'/></g><text x='345' y='17' font-size='11' text-anchor='middle' font-weight='bold'>N</text>"
    for n, (lo, la) in CITY.items():
        left = n == "Mount Abu"
        s += f"<circle cx='{X(lo):.0f}' cy='{Y(la):.0f}' r='3.5' fill='#c0392b'/>"
        anc = 'text-anchor="end"' if left else ''
        tx = X(lo) - 6 if left else X(lo) + 6
        s += f"<text x='{tx:.0f}' y='{Y(la)+3:.0f}' font-size='10' {anc}>{n}</text>"
    s += f"<text x='8' y='{H-6}' font-size='8' fill='#555'>Schematic positions of cities (not to scale; state boundary not shown)</text></svg>"
    return s

def cities_q(parts):
    """Q4: schematic of Rajasthan cities. parts = list of P(...)."""
    return Q("The figure below shows the approximate positions of some cities of Rajasthan (schematic, not to scale). Look at it and answer the following.",
             6, "", fig=svg_cities(), parts=parts)

def dq(label, a, b, marks, exp):
    """direction question with asserted answer."""
    assert direction(a, b) == exp, (a, b, direction(a, b), exp)
    return P(label, f"In which direction does <b>{b}</b> lie from <b>{a}</b>?", marks, exp.capitalize() + ".")

INSTR = ["This question paper is based on the learning areas of Environmental Studies (EVS).",
         "Write your Name and Roll No. in the space given at the top of the question paper.",
         "All questions are compulsory.",
         "The marks for each question are given against it.",
         "Write your answers neatly and legibly."]

TITLES = [("OBSERVATION · IDENTIFICATION · DISCUSSION", 11, 0, 4),
          ("INTER-RELATIONSHIP OF SOCIAL AND NATURAL ENVIRONMENT", 12, 4, 7),
          ("REASONING · CLASSIFICATION · QUESTIONING", 11, 7, 12),
          ("CREATION OF NEW PRODUCTS · LOCAL MATERIALS · DECISION MAKING", 17, 12, 15),
          ("ANALYSIS AND APPLYING", 12, 15, 17),
          ("SENSITIVITY TO JUSTICE, EQUITY AND NATURAL RESOURCES", 10, 17, 20),
          ("SOCIAL-EMOTIONAL AND LIFE SKILLS", 7, 20, 22)]

def run(set_no, items):
    assert len(items) == 22
    meta = dict(subject="EVS", set_no=set_no, time="2.30 Hours", marks=80, instr=INSTR)
    secs = [sec(t, m, items[a:b]) for t, m, a, b in TITLES]
    print(build(meta, secs))
