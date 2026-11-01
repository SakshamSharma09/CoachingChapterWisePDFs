import sys; sys.path.insert(0,'/home/claude/pat'); sys.path.insert(0,'/home/claude/pat/c10s')
from lib10 import *
from f10 import *
INSTR = [
 "This question paper consists of 39 questions in 3 sections. Section A is Biology, Section B is Chemistry and Section C is Physics.",
 "All sections are compulsory. However, internal choice is provided in some questions. A student is expected to attempt only one of these questions.",
 "Draw neat, labelled diagrams wherever required. Use of calculator is not allowed.",
]
def meta(n): return dict(cls=10, subject='Science', title='CLASS X — SCIENCE (086) · FULL SYLLABUS PRACTICE PAPER', title_extra='Session 2026–27 | CBSE / RBSE Pattern | Section A Biology · Section B Chemistry · Section C Physics', set_no=n, time='3 Hours', marks=80, instr=INSTR)
def unwrap(x): return x['a'] if x['k'] == 'or' else x
SPEC = dict(Bio=dict(mcq=7, ar=2, s2=3, s3=2, case=1, d=1), Chem=dict(mcq=5, ar=1, s2=2, s3=2, case=1, d=1), Phy=dict(mcq=4, ar=1, s2=1, s3=3, case=1, d=1))
def block(name, d):
    sp = SPEC[name]
    for k, v in sp.items(): assert len(d[k]) == v, (name, k, len(d[k]), v)
    return d['mcq'] + d['ar'] + d['s2'] + d['s3'] + d['case'] + d['d']
def go(n, bio, chem, phy):
    secs = []
    notes = dict(Bio="Q1–Q7 MCQs. Q8–Q9: Assertion (A) / Reason (R) – choose A, B, C or D.", Chem="Q17–Q21 MCQs. Q22: Assertion (A) / Reason (R) – choose A, B, C or D.", Phy="Q29–Q32 MCQs. Q33: Assertion (A) / Reason (R) – choose A, B, C or D.")
    for nm, d, t in (('Bio', bio, 'SECTION A — BIOLOGY'), ('Chem', chem, 'SECTION B — CHEMISTRY'), ('Phy', phy, 'SECTION C — PHYSICS')):
        secs.append(sec(t, notes[nm], block(nm, d)))
    build(meta(n), secs, '/home/claude/pat/out/Class10_Science/Set_%02d' % n, 'Class10_Science_SchoolPattern_Set_%02d' % n)
