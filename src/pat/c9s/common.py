import sys, os
sys.path.insert(0, '/home/claude/pat'); sys.path.insert(0, '/home/claude/pat/c9s')
from lib_pat import *
from figlib import *
S = lambda x: f"<sup>{x}</sup>"
B = lambda x: f"<sub>{x}</sub>"
OUT = '/home/claude/pat/out/Class9_Science'
INSTR = ["This question paper consists of 39 questions in 3 sections. Section A is Biology (Q.1–16), Section B is Chemistry (Q.17–27) and Section C is Physics (Q.28–39).",
         "All sections are compulsory. However, internal choice is provided in some questions. A student is expected to attempt only one of the options in such questions.",
         "Section A carries 32 marks, Section B 25 marks and Section C 23 marks. Marks are printed against each question.",
         "Draw neat, labelled diagrams wherever required. Use g = 10 m s<sup>−2</sup> wherever needed."]
def science_paper(n, bio, chem, phy):
    assert len(bio) == 16 and len(chem) == 11 and len(phy) == 12, (len(bio), len(chem), len(phy))
    secs = [sec("SECTION A — BIOLOGY", "Q.1–7 MCQs (1 mark each); Q.8–9 Assertion–Reason. For Assertion–Reason: (a) Both A and R are true, and R is the correct explanation of A. (b) Both A and R are true, but R is not the correct explanation of A. (c) A is true but R is false. (d) A is false but R is true.", bio),
            sec("SECTION B — CHEMISTRY", "Q.17–19 MCQs; Q.20 Assertion–Reason (options as in Section A).", chem),
            sec("SECTION C — PHYSICS", "Q.28–33 MCQs; Q.34 Assertion–Reason (options as in Section A).", phy)]
    for s, mk in zip(secs, (32, 25, 23)): assert sum(i['m'] for i in s['items']) == mk, (s['title'], sum(i['m'] for i in s['items']))
    meta = dict(cls=9, subject='Science', title='CLASS IX — SCIENCE (086) · MID-TERM / HALF-YEARLY PRACTICE PAPER', title_extra='Session 2026-27 · School Examination Pattern', set_no=n, time='3 Hours', marks=80, instr=INSTR)
    build(meta, secs, OUT, f"Class9_Science_Set_{n:02d}")

def row(*figs, labels=None):
    cells = "".join(f"<div style='text-align:center'>{f}" + (f"<div style='font-weight:700'>{labels[i]}</div>" if labels else "") + "</div>" for i, f in enumerate(figs))
    return f"<div style='display:flex;justify-content:center;gap:10px;flex-wrap:wrap'>{cells}</div>"
