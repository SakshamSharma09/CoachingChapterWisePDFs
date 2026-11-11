import os; os.environ.setdefault('CHROMIUM_PATH', os.path.expanduser('~/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe'))
import sys, re, itertools; sys.path.insert(0, 'D:/Coaching Chapterwise PDFs/src/pat/c6sst')
from lib8 import *
import figs

_ctr = [0]
_ORDER = [2, 0, 3, 1, 1, 3, 0, 2, 3, 2, 1, 0, 0, 1, 2, 3]
def _pos():
    p = _ORDER[_ctr[0] % len(_ORDER)]; _ctr[0] += 1; return p
def m(q, c, w, sol='', fig=None):
    pos = _pos(); opts = list(w); opts.insert(pos, c)
    return mcq(q, opts, 'abcd'[pos], sol, fig)
def chrono(events, sol=''):
    """events: list of (text, year) in the DISPLAYED order (shuffled). Builds 4 permutations as options."""
    assert len(events) == 4
    order = sorted(range(4), key=lambda i: events[i][1]); correct = tuple(o + 1 for o in order)
    perms = [p for p in itertools.permutations([1, 2, 3, 4]) if p != correct]
    # distractors: close permutations (swap adjacent pairs) for plausibility
    d = []
    for i in range(3):
        c = list(correct); c[i], c[i + 1] = c[i + 1], c[i]; d.append(tuple(c))
    d = [x for x in d if x != correct][:3]
    pos = _pos(); opts = [", ".join(map(str, p)) for p in d]; opts.insert(pos, ", ".join(map(str, correct)))
    lst = "".join(f"<br>&nbsp;&nbsp;{i+1}. {t}" for i, (t, _) in enumerate(events))
    q = f"Arrange the following events in chronological order and select the correct option.{lst}"
    return mcq(q, opts, 'abcd'[pos], sol or "Correct order: " + " → ".join(f"{t} ({y})" for t, y in sorted(events, key=lambda e: e[1])), None)
def ar(a, r, kind, sol=''):
    """kind: 'exp' both true & R explains A; 'noexp' both true, R not explanation; 'A' A true R false; 'R' A false R true. Options in school order."""
    opts = ["A is correct, R is incorrect", "A is incorrect, R is correct", "Both A and R are correct and R is the correct explanation of A", "Both A and R are correct but R is not the correct explanation of A"]
    ans = {'A': 'a', 'R': 'b', 'exp': 'c', 'noexp': 'd'}[kind]
    q = f"Given below are two statements – Assertion (A) and Reason (R). Read them and select the correct option.<br><b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}"
    return mcq(q, opts, ans, sol)
def st(s1, s2, t1, t2, sol=''):
    opts = ["Only I is correct", "Only II is correct", "Both are correct", "Both are incorrect"]
    a = 'a' if (t1 and not t2) else 'b' if (t2 and not t1) else 'c' if (t1 and t2) else 'd'
    return mcq(f"Read Statement I and Statement II and select the correct option.<br><b>Statement I:</b> {s1}<br><b>Statement II:</b> {s2}", opts, a, sol)
def fill(q, c, w, sol=''): return m("Fill in the blank with the appropriate option.<br>" + q, c, w, sol)
def pair(label, c, w, sol=''):
    """Identify the correct match: label e.g. 'Battle of Plassey' c='1757' w=[...]"""
    return m("Identify the correct match.", f"{label} – {c}", [f"{label} – {x}" for x in w], sol)
def pts(*p):  # marking points as list
    return "<ul style='margin:.5mm 0 .5mm 4mm;padding-left:3mm'>" + "".join(f"<li>{x}</li>" for x in p) + "</ul>"
def sol(head, *p): return f"<b>{head}</b>" + pts(*p)
def vsa(q, *p, m_=2, head="Marking points (any two, 1 mark each):"): return sa(q, m_, sol(head, *p))
def src(text, subs): return case(text, subs)
def s(q, mk, ans): return sub(q, mk, ans)

# ---------- India outline map ----------
INDIA = [(68.2,23.7),(69.6,24.3),(70.2,25.6),(69.5,26.8),(70.6,28.0),(71.9,28.9),(73.2,29.9),(74.0,30.6),(74.6,31.6),(75.7,32.3),(74.6,32.8),(74.2,34.0),(73.5,35.0),(73.5,36.5),(75.0,37.0),(77.8,35.5),(77.0,35.7),(78.0,35.5),(79.0,34.4),(80.2,35.4),(79.5,33.5),(78.8,32.5),(79.0,31.2),(78.5,31.0),(79.8,30.3),(80.5,29.7),(80.1,28.8),(81.0,28.3),(82.5,27.6),(84.0,27.4),(85.5,26.8),(87.3,26.4),(88.1,26.5),(88.1,27.1),(88.8,27.3),(88.9,28.1),(89.0,26.8),(90.0,26.8),(92.0,26.9),(92.1,27.8),(93.5,28.6),(95.0,29.2),(96.1,29.4),(97.4,28.2),(96.9,27.4),(97.1,27.0),(96.0,26.4),(95.0,25.5),(94.6,24.0),(93.4,23.0),(93.2,22.6),(92.5,22.0),(92.2,23.7),(91.5,24.1),(91.2,25.2),(90.0,25.2),(89.8,26.0),(89.0,26.3),(88.4,24.5),(88.7,24.2),(88.2,23.0),(89.0,22.0),(88.5,21.7),(87.0,21.5),(86.5,20.3),(85.5,19.7),(84.0,18.4),(82.3,16.7),(81.0,15.7),(80.2,14.0),(80.3,13.0),(79.9,11.5),(79.8,10.3),(79.3,9.2),(78.2,8.9),(77.55,8.08),(76.5,9.0),(75.8,11.0),(74.8,13.0),(74.0,15.0),(73.4,16.5),(72.8,19.0),(72.7,20.5),(72.6,21.5),(72.0,21.0),(70.2,20.9),(69.0,22.3),(70.0,22.9),(70.7,22.9),(68.6,23.2)]
_X0, _Y0, _SX, _SY = 66.0, 38.5, 12.0, 13.0
def _xy(lon, lat): return (round(20 + (lon - _X0) * _SX, 1), round(10 + (_Y0 - lat) * _SY, 1))
def india_map(marks=None, nolabel=False):
    W, H = int(20 + 33 * _SX + 20), int(10 + 32 * _SY + 10)
    b = ""
    for lon in range(68, 98, 4): x = _xy(lon, 0)[0]; b += figs.line(x, 10, x, H - 10, '#e3e3e3', .6) + figs.text(x, H - 1, f"{lon}°E", sz=8, c='#777')
    for lat in range(8, 38, 4): y = _xy(0, lat)[1]; b += figs.line(20, y, W - 20, y, '#e3e3e3', .6) + figs.text(8, y + 3, f"{lat}°N", sz=8, c='#777')
    b += figs.poly([_xy(*p) for p in INDIA], '#0f2347', '#fbfbf3', 1.6)
    b += figs.text(W - 30, 24, "N ↑", sz=11)
    boxes = []
    for (L, lo, la, nm, dx, dy) in (marks or []):
        x, y = _xy(lo, la)
        txt = f"{L}. {nm}"; w = 5.3 * len(txt)
        left = lo <= 76.2 and (x - 7 - w) > 2
        dx = -7 if left else 7
        dy = -5
        for _ in range(12):
            x0 = x + dx if not left else x + dx - w
            bx = (x0, y + dy - 9, x0 + w, y + dy + 3)
            if not any(bx[0] < o[2] and bx[2] > o[0] and bx[1] < o[3] and bx[3] > o[1] for o in boxes): break
            dy += 11 if dy < 12 else -30
        boxes.append(bx)
        b += f"<circle cx='{x}' cy='{y}' r='4' fill='#c0392b'/>" + f"<text x='{x+dx}' y='{y+dy}' text-anchor='{'end' if left else 'start'}' font-size='9.5' fill='#c0392b' font-weight='bold' stroke='#fff' stroke-width='3' paint-order='stroke' stroke-linejoin='round'>{txt}</text>"
    return figs.svg(W, H, b)

def inside(lon, lat):
    x, y = lon, lat; ins = False; P = INDIA
    for i in range(len(P)):
        x1, y1 = P[i]; x2, y2 = P[(i + 1) % len(P)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: ins = not ins
    return ins

ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI']
def _shrink(svg, f=0.72):
    m_ = re.search(r"width='(\d+)' height='(\d+)'", svg)
    w, h = int(m_.group(1)), int(m_.group(2))
    return svg.replace(m_.group(0), f"width='{int(w*f)}' height='{int(h*f)}'", 1)
def mapq(items):
    """items: 6 tuples (name, lon, lat, state[, dx, dy]); returns sa question, 5 marks."""
    assert len(items) == 6
    lines = "".join(f"<div>({ROMAN[i]}) &nbsp;{it[0]}</div>" for i, it in enumerate(items))
    vi = "".join(f"<div><span>({ROMAN[i]}) &nbsp;In which present-day Indian state/UT is {re.sub(r' *[(].*?[)]', '', it[0])} located?</span><span>1</span></div>" for i, it in enumerate(items))
    q = (f"On the Political outline Map of India provided, locate and label any <b>five</b> of the following places using appropriate symbols/signs: <span style='float:right'>(5×1=5)</span><div class='mp'>{lines}</div>"
         f"<div class='vi'><b>The following questions are for Visually Impaired students only, in lieu of Question No. 14. Answer any five questions:</b>{vi}</div>")
    marks = [(ROMAN[i], it[1], it[2], it[0], 7, -5) for i, it in enumerate(items)]
    ans = "".join(f"<li>({ROMAN[i]}) {it[0]} — <b>{it[3]}</b></li>" for i, it in enumerate(items))
    soln = ("1 mark for each correctly located and labelled place (any five); a position within about 150 km of the true location is acceptable. "
            "For Visually Impaired candidates: 1 mark for each correct state/UT (any five).<ul style='columns:2;margin:.5mm 0 .5mm 4mm;padding-left:3mm'>" + ans + "</ul>" + _shrink(india_map(marks), 0.62))
    r = sa(q, 5, soln, fig=_shrink(india_map())); r['nofig'] = True
    for it in items: assert inside(it[1], it[2]), f"{it[0]} outside outline"
    return r

def meta(n, tag):
    return dict(cls=6, subject='Social Science', title='CLASS VI — SOCIAL SCIENCE · FULL-YEAR PRACTICE PAPER', title_extra=f'Annual Examination Pattern · Session 2026–27 · {tag}', set_no=n, time='2 Hours 30 Minutes', marks=60,
        instr=["All questions are compulsory.",
               "The question paper is divided into six sections – A, B, C, D, E and F.",
               "Section A contains Question No. 1 with 15 sub-parts, all Multiple Choice Questions. Each sub-part carries 1 mark. Choose the correct option.",
               "Section B contains Question Nos. 2 to 5, which are very short answer questions carrying 2 marks each. Answer each question in at least 20 words.",
               "Section C contains Question Nos. 6 and 7, which are short answer questions carrying 3 marks each. Answer each question in about 40–60 words.",
               "Section D contains Question Nos. 8 and 9, which are long answer questions carrying 5 marks each. Answer each question in about 80–100 words.",
               "Section E contains Question Nos. 10 to 13, which are source/case-based questions carrying 4 marks each (1+1+2). Read the given source carefully and answer the questions that follow.",
               "Section F contains Question No. 14, a map-based question carrying 5 marks. Mark the given locations on the map using appropriate symbols/signs.",
               "No overall choice has been provided in the question paper; however, internal choices are given in some questions. Attempt only one option in such questions.",
               "For Visually Impaired students, a separate question has been provided in place of Question No. 14. It is to be attempted only by Visually Impaired students.",
               "Maintain neatness and clarity while writing answers."])

def assemble(A, B, C, D, E, F):
    assert len(A) == 15 and len(B) == 4 and len(C) == 2 and len(D) == 2 and len(E) == 4
    return [dict(title="SECTION A — Multiple Choice Questions (1×15=15)", note="Question 1 · Choose the correct option for each sub-part.", items=A, mcqs=True),
            dict(title="SECTION B — Very Short Answer Questions (4×2=8)", note="Question Nos. 2 to 5 · each carries 2 marks · at least 20 words.", items=B),
            dict(title="SECTION C — Short Answer Questions (2×3=6)", note="Question Nos. 6 and 7 · each carries 3 marks · about 40–60 words.", items=C),
            dict(title="SECTION D — Long Answer Questions (2×5=10)", note="Question Nos. 8 and 9 · each carries 5 marks · about 80–100 words.", items=D),
            dict(title="SECTION E — Case / Source Based Questions (4×4=16)", note="Question Nos. 10 to 13 · each carries 4 marks (1+1+2).", items=E),
            dict(title="SECTION F — Map Based Question (1×5=5)", note="Question No. 14 · 5 marks.", items=[F])]
