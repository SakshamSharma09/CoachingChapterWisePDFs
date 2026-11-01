import sys, random, math
sys.path.insert(0, '/home/claude/pat'); sys.path.insert(0, '/home/claude/pat/c10m')
from lib_pat import *
import figs, figx
from fractions import Fraction as Fr

def tbl(head, rows):
    return "<table class='t'><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
def htbl(*rows):  # horizontal table: first col is header
    return "<table class='t'>" + "".join("<tr>" + "".join((f"<th>{c}</th>" if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r)) + "</tr>" for r in rows) + "</table>"

class Mk:
    """Option placer: correct answer letter cycles through a seeded shuffle for an even spread."""
    def __init__(self, seed):
        rnd = random.Random(seed); self.seq = []
        for _ in range(6): b = list('abcd'); rnd.shuffle(b); self.seq += b
        self.i = 0
    def mc(self, q, correct, wrongs, sol='', fig=None):
        pos = 'abcd'.index(self.seq[self.i]); self.i += 1
        opts = list(wrongs); opts.insert(pos, correct)
        return mcq(q, opts, 'abcd'[pos], sol, fig)

INSTR = ["This Question Paper has 5 Sections 'A', 'B', 'C', 'D' and 'E'.",
 "Section A has 20 MCQs carrying 1 mark each (Q19–20 are Assertion–Reason questions).",
 "Section B has 5 questions carrying 02 marks each.",
 "Section C has 6 questions carrying 03 marks each.",
 "Section D has 4 questions carrying 05 marks each.",
 "Section E has 3 case based questions (04 marks each) with sub-parts of the values of 1, 1 and 2 marks respectively.",
 "All questions are compulsory. However, an internal choice in 2 questions of 5 marks, 2 questions of 3 marks and 2 questions of 2 marks has been provided. An internal choice has been provided in the 2-mark questions of Section E. You have to attempt only one option out of the given options.",
 "Draw neat figures wherever required. Take π = 22/7 wherever required, if not stated.",
 "There is no provision of negative marking. Use of calculator is not permitted.",
 "Please write down the serial number of the question before attempting it."]

def assemble(n, A, B, C, D, E, kind='MID-TERM PRACTICE PAPER'):
    assert len(A) == 20 and len(B) == 5 and len(C) == 6 and len(D) == 4 and len(E) == 3
    assert A[18]['k'] == 'ar' and A[19]['k'] == 'ar' and all(a['k'] == 'mcq' for a in A[:18])
    for e in E: assert any(x['k']=='or' for x in e['subs']), 'E needs OR in 2-mark part'
    assert sum(1 for x in B if x['k'] == 'or') == 2 and sum(1 for x in C if x['k'] == 'or') == 2 and sum(1 for x in D if x['k'] == 'or') == 2
    secs = [sec("SECTION – A  (Multiple Choice Questions · 20 × 1 = 20)", "Q1–Q18 are multiple-choice questions. Q19–Q20: a statement of Assertion (A) is followed by a statement of Reason (R). Choose the correct option.", A),
            sec("SECTION – B  (Very Short Answer Questions · 5 × 2 = 10)", "", B),
            sec("SECTION – C  (Short Answer Questions · 6 × 3 = 18)", "", C),
            sec("SECTION – D  (Long Answer Questions · 4 × 5 = 20)", "", D),
            sec("SECTION – E  (Case Study Based Questions · 3 × 4 = 12)", "", E)]
    meta = dict(cls=10, subject='Mathematics', title='CLASS X — MATHEMATICS (Standard) · ' + kind,
                title_extra='Session 2026-27 · CBSE / Directorate of Education pattern · Sub code 041', set_no=n, time='3 Hours', marks=80, instr=INSTR)
    return meta, secs

def S(*a, **k): return sa(*a, **k)
