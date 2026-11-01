import sys; sys.path.insert(0,'/home/claude/pat/c8m')
import lib_pat as L
from lib_pat import *
import figs as F
ROM=['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii']
def mcqgroup(items): assert len(items)==12; return dict(k='mg', items=items, m=12)
_orig = L._item_html
def _item_html(it, n, key):
    if it['k']=='mg':
        out=[f"<div class='q'><div class='qn'>{n}.</div><div class='qb'><b>Question {n} consists of multiple-choice questions (i–xii) of 1 mark each. Choose the correct option.</b></div><div class='qm'></div></div>"]
        for j,s in enumerate(it['items']):
            x=_orig(s,'',key)
            x=x.replace("<div class='qn'></div>",f"<div class='qn'>({ROM[j]})</div>",1)
            out.append(x)
        return "".join(out)
    return _orig(it,n,key)
L._item_html=_item_html
# helpers for figures
def quad(pts, labels, extra='', w=220, h=150, fill='none'):
    b=F.poly(pts,'#000',fill)+extra
    cx=sum(p[0] for p in pts)/len(pts); cy=sum(p[1] for p in pts)/len(pts)
    for (x,y),t in zip(pts,labels):
        dx=12 if x>cx else -12; dy=14 if y>cy else -6
        b+=F.text(x+dx,y+dy,t)
    return F.svg(w,h,b)

import random, hashlib
def m(q, correct, wrong, sol='', fig=None, pos=None):
    """mcq with correct option placed pseudo-randomly (or at pos 0-3)."""
    opts = list(wrong)[:3]; assert len(opts)==3 and correct not in opts, (q, correct, opts)
    p = pos if pos is not None else int(hashlib.md5(q.encode()).hexdigest(),16) % 4
    opts.insert(p, correct)
    return L.mcq(q, opts, 'abcd'[p], sol, fig)
def instr(n_q, extra=''):
    return [f"This question paper contains {n_q} questions. All questions are compulsory.",
      "Question paper is divided into FIVE sections – Section ‘A’, ‘B’, ‘C’, ‘D’ and ‘E’.",
      "In Section ‘A’ question number 1 has 12 multiple choice sub-parts carrying 1 mark each.",
      "In Section ‘B’ question numbers 2 to 7 are very short answer type questions carrying 2 marks each.",
      "In Section ‘C’ question numbers 8 to 10 are short answer (SA) type questions carrying 3 marks each.",
      "In Section ‘D’ question numbers 11 to 13 are long answer (LA) type questions carrying 5 marks each.",
      "In Section ‘E’ question numbers 14 to 16 are case-based questions whose sub-parts are of 1, 1 and 2 marks respectively.",
      "There is no overall choice. However, internal choice has been provided in 1 question of Section B, 1 question of Section C, 2 questions of Section D, and in the 2-mark sub-part of every case-based question in Section E. Attempt only one of the alternatives in all such questions.",
      "Draw neat figures wherever required. Use of calculators is NOT allowed. Write the serial number of the question before attempting it."]
def meta(n):
    return dict(cls=8, subject='Mathematics', title='CLASS VIII — MATHEMATICS · MID-TERM PRACTICE PAPER', title_extra='Session 2026-27 | CBSE / RBSE Pattern', set_no=n, time='2 Hours 30 Minutes', marks=60, instr=instr(16))
def secs(q1, b, c, d, e):
    return [sec("SECTION A — Multiple Choice Questions (12 × 1 = 12)", "", [q1]),
            sec("SECTION B — Very Short Answer (6 × 2 = 12)", "Questions 2 to 7 carry 2 marks each.", b),
            sec("SECTION C — Short Answer (3 × 3 = 9)", "Questions 8 to 10 carry 3 marks each.", c),
            sec("SECTION D — Long Answer (3 × 5 = 15)", "Questions 11 to 13 carry 5 marks each.", d),
            sec("SECTION E — Case-Based Questions (3 × 4 = 12)", "Questions 14 to 16 carry 4 marks each (1 + 1 + 2).", e)]
