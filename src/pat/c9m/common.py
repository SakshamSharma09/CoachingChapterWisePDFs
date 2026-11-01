import sys, random, math
sys.path.insert(0, '/home/claude/pat'); sys.path.insert(0, '/home/claude/pat/c9m')
from lib_pat import *
from fg import *
from fractions import Fraction as F
def mc(q, correct, wrong, sol='', fig=None):
    assert len(wrong) == 3 and correct not in wrong and len(set(wrong)) == 3
    opts = [correct] + list(wrong); r = random.Random(hash(q) % 100000 + len(q)); idx = list(range(4)); r.shuffle(idx)
    new = [opts[i] for i in idx]; ans = 'abcd'[new.index(correct)]
    return mcq(q, new, ans, sol, fig)
def mcl(q, opts, ans, sol='', fig=None): return mcq(q, opts, ans, sol, fig)   # fixed order (e.g. numeric ascending / statement lists)
def steps(*s): return "<br>".join(s)
INSTR = [
 "This question paper contains 38 questions and is divided into 5 sections — A, B, C, D and E.",
 "In Section A, Q. 1–18 are multiple-choice questions and Q. 19–20 are Assertion–Reason based questions of 1 mark each.",
 "In Section B, Q. 21–25 are very short answer (VSA) type questions carrying 2 marks each.",
 "In Section C, Q. 26–31 are short answer (SA) type questions carrying 3 marks each.",
 "In Section D, Q. 32–35 are long answer (LA) type questions carrying 5 marks each.",
 "In Section E, Q. 36–38 are case-study based questions carrying 4 marks each with sub-parts of 1, 1 and 2 marks respectively.",
 "All questions are compulsory. However, an internal choice is provided in 1 question of Section B, 2 questions of Section C and 2 questions of Section D. An internal choice is provided in all the 2-mark sub-parts of Section E.",
 "Draw neat and clean figures wherever required. Take π = 22/7 wherever required, if not stated. Use of calculators is not allowed.",
 "Write the serial number of each question before attempting it."]
def meta(n): return dict(cls=9, subject='Maths', title='CLASS IX — MATHEMATICS · FULL SYLLABUS EXAMINATION', title_extra='Session 2026-27 | CBSE / RBSE Pattern', set_no=n, time='3 Hours', marks=80, instr=INSTR)
SECA = "Q1–Q18 are multiple-choice questions (1 mark each). Q19–Q20 are Assertion (A) and Reason (R) questions: select the correct option from (a), (b), (c), (d) given below each."
def sections(A, B, C, D, E):
    assert len(A) == 20 and len(B) == 5 and len(C) == 6 and len(D) == 4 and len(E) == 3
    return [sec("SECTION A — Objective Type", SECA, A), sec("SECTION B — Very Short Answer (2 marks each)", "Internal choice is provided in one question.", B),
            sec("SECTION C — Short Answer (3 marks each)", "Internal choice is provided in two questions.", C),
            sec("SECTION D — Long Answer (5 marks each)", "Internal choice is provided in two questions.", D),
            sec("SECTION E — Case-Study Based Questions (4 marks each)", "Read each case carefully and answer the questions that follow. Internal choice is provided in every 2-mark sub-part.", E)]
def fr(a, b): return frac(a, b)
