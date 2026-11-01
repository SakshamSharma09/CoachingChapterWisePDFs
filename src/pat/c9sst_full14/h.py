import sys; sys.path.insert(0, '/home/claude/pat')
from lib_pat import *
import figs

# ---------- helpers ----------
_ctr = [0]
_ORDER = [1, 3, 0, 2, 2, 0, 3, 1, 1, 2, 0, 3, 3, 1, 2, 0]
def m(q, c, w, sol='', fig=None):
    """mcq with correct option c and 3 wrong options w; position cycles for variety."""
    pos = _ORDER[_ctr[0] % len(_ORDER)]; _ctr[0] += 1
    opts = list(w); opts.insert(pos, c)
    return mcq(q, opts, 'abcd'[pos], sol, fig)
def st(s1, s2, t1, t2, sol=''):
    """Statement 1 / Statement 2 type."""
    opts = ["Both statements are correct", "Statement 1 is correct, Statement 2 is incorrect", "Statement 1 is incorrect, Statement 2 is correct", "Both statements are incorrect"]
    a = 'a' if (t1 and t2) else 'b' if t1 else 'c' if t2 else 'd'
    return mcq(f"Read the statements and choose the correct option.<br><b>Statement 1:</b> {s1}<br><b>Statement 2:</b> {s2}", opts, a, sol)
def match(rows, right, opts, ans, sol=''):
    """rows: list of left items (a,b,c), right: list of right items (1,2,3) ; opts list of 4 strings"""
    t = "<table class='t'><tr><th>Column I</th><th>Column II</th></tr>" + "".join(f"<tr><td>({'abcd'[i]}) {l}</td><td>{i+1}. {r}</td></tr>" for i, (l, r) in enumerate(zip(rows, right))) + "</table>"
    return mcq("Match Column I with Column II and choose the correct option." + t, opts, ans, sol)
def src(text, subs): return case(f"<i>Read the passage carefully and answer the questions that follow.</i><br>“{text}”", subs)

# ---------- India outline map ----------
INDIA = [(68.2,23.7),(69.6,24.3),(70.2,25.6),(69.5,26.8),(70.6,28.0),(71.9,28.9),(73.2,29.9),(74.0,30.6),(74.6,31.6),(75.7,32.3),(74.6,32.8),(74.2,34.0),(73.5,35.0),(73.5,36.5),(75.0,37.0),(77.8,35.5),(77.0,35.7),(78.0,35.5),(79.0,34.4),(80.2,35.4),(79.5,33.5),(78.8,32.5),(79.0,31.2),(78.5,31.0),(79.8,30.3),(80.5,29.7),(80.1,28.8),(81.0,28.3),(82.5,27.6),(84.0,27.4),(85.5,26.8),(87.3,26.4),(88.1,26.5),(88.1,27.1),(88.8,27.3),(88.9,28.1),(89.0,26.8),(90.0,26.8),(92.0,26.9),(92.1,27.8),(93.5,28.6),(95.0,29.2),(96.1,29.4),(97.4,28.2),(96.9,27.4),(97.1,27.0),(96.0,26.4),(95.0,25.5),(94.6,24.0),(93.4,23.0),(93.2,22.6),(92.5,22.0),(92.2,23.7),(91.5,24.1),(91.2,25.2),(90.0,25.2),(89.8,26.0),(89.0,26.3),(88.4,24.5),(88.7,24.2),(88.2,23.0),(89.0,22.0),(88.5,21.7),(87.0,21.5),(86.5,20.3),(85.5,19.7),(84.0,18.4),(82.3,16.7),(81.0,15.7),(80.2,14.0),(80.3,13.0),(79.9,11.5),(79.8,10.3),(79.3,9.2),(78.2,8.9),(77.55,8.08),(76.5,9.0),(75.8,11.0),(74.8,13.0),(74.0,15.0),(73.4,16.5),(72.8,19.0),(72.7,20.5),(72.6,21.5),(72.0,21.0),(70.2,20.9),(69.0,22.3),(70.0,22.9),(70.7,22.9),(68.6,23.2)]
_X0, _Y0, _SX, _SY = 66.0, 38.5, 12.0, 13.0
def _xy(lon, lat): return (round(20 + (lon - _X0) * _SX, 1), round(10 + (_Y0 - lat) * _SY, 1))
def india_map(marks=None):
    """marks: list of (letter, lon, lat, name). Blank map when None."""
    W, H = int(20 + 33 * _SX + 20), int(10 + 32 * _SY + 10)
    b = ""
    for lon in range(68, 98, 4): x = _xy(lon, 0)[0]; b += figs.line(x, 10, x, H - 10, '#e3e3e3', .6) + figs.text(x, H - 1, f"{lon}°E", sz=8, c='#777')
    for lat in range(8, 38, 4): y = _xy(0, lat)[1]; b += figs.line(20, y, W - 20, y, '#e3e3e3', .6) + figs.text(8, y + 3, f"{lat}°N", sz=8, c='#777')
    b += figs.poly([_xy(*p) for p in INDIA], '#0f2347', '#fbfbf3', 1.6)
    b += figs.text(W - 30, 24, "N ↑", sz=11)
    for (L, lo, la, nm) in (marks or []):
        x, y = _xy(lo, la)
        b += f"<circle cx='{x}' cy='{y}' r='4' fill='#c0392b'/>" + figs.text(x + 7, y - 5, f"{L}. {nm}", 'start', 10, '#c0392b')
    return figs.svg(W, H, b)
def mapq(items, vi_items, marks_note="Attempt any five. Each item carries 1 mark."):
    """items: list of (name, lon, lat); returns sa question 5 marks."""
    L = "ABCDEF"
    lines = "".join(f"<br>{L[i]}. {n}" for i, (n, _, _) in enumerate(items))
    import re
    vi = "".join(f"<br>{i+1}. Name the State/UT in which {re.sub(r' *[(].*?[)]', '', n)} is located." for i, (n, _, _) in enumerate(items))
    q = (f"On the outline map of India provided, locate and label any <b>five</b> of the following (use the given letter/number for each): <i>{marks_note}</i>{lines}"
         f"<div style='font-size:8.6pt;border-top:1px dotted #888;margin-top:1.5mm;padding-top:1mm'><b>Note — in lieu of Q.37, for visually impaired candidates only (answer any five):</b>{vi}</div>")
    marks = [(L[i], lo, la, n) for i, (n, lo, la) in enumerate(items)]
    sol = "1 mark for each correctly located and labelled item (any five). Correct positions are shown below; answers marked within a tolerance of about 150 km are acceptable.<br>" + india_map(marks)
    r = sa(q, 5, sol, fig=india_map()); r['nofig'] = True; return r

def meta(n, tag):
    return dict(cls=9, subject='Social Science', title='CLASS IX — SOCIAL SCIENCE · FULL SYLLABUS PRACTICE PAPER', title_extra=f'Session 2026-27 · CBSE / RBSE Pattern · {tag}', set_no=n, time='3 Hours', marks=80,
        instr=["This question paper contains 37 questions. All questions are compulsory.", "The paper is divided into SIX sections — A, B, C, D, E and F.",
               "Section A — Q.1–20 are multiple-choice questions of 1 mark each.", "Section B — Q.21–24 are Very Short Answer (VSA) questions of 2 marks each (about 40 words); there is internal choice in 1 question.",
               "Section C — Q.25–29 are Short Answer (SA) questions of 3 marks each (about 60 words); there is internal choice in 1 question.", "Section D — Q.30–33 are Long Answer (LA) questions of 5 marks each (about 120 words); internal choice is given in all four questions.",
               "Section E — Q.34–36 are case/source-based questions of 4 marks each with sub-parts of 1, 1 and 2 marks.", "Section F — Q.37 is a map-skill question of 5 marks.",
               "A separate set of questions in lieu of the map question is given for visually impaired candidates only.", "Write the question number before each answer."])

def assemble(A, B, C, D, E, F):
    assert len(A) == 20 and len(B) == 4 and len(C) == 5 and len(D) == 4 and len(E) == 3
    return [sec("SECTION A — Multiple Choice Questions", "Select the most appropriate option. (20 × 1 = 20)", A),
            sec("SECTION B — Very Short Answer Type", "Each question carries 2 marks. Answer in about 40 words. (4 × 2 = 8)", B),
            sec("SECTION C — Short Answer Type", "Each question carries 3 marks. Answer in about 60 words. (5 × 3 = 15)", C),
            sec("SECTION D — Long Answer Type", "Each question carries 5 marks. Answer in about 120 words. (4 × 5 = 20)", D),
            sec("SECTION E — Source-based / Case-based Questions", "Each question carries 4 marks (1 + 1 + 2). (3 × 4 = 12)", E),
            sec("SECTION F — Map-based Question", "(1 × 5 = 5)", [F])]
