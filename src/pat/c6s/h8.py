import os; os.environ.setdefault('CHROMIUM_PATH', os.path.expanduser('~/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe'))
import random, sys
sys.path.insert(0, 'D:/Coaching Chapterwise PDFs/src/pat/c6s')
from lib_pat import *
import figs8 as F
def mc(q, c, w, why='', fig=None):
    r = random.Random(q); o = [c] + list(w); r.shuffle(o)
    return mcq(q, o, 'abcd'[o.index(c)], why or f"Correct option: {c}", fig=fig)
def c4(text, a, b, c, d, fig=None):
    """a,b: (q, ans) 1 mark each; c,d: (q, ans) 2 marks each (internal choice)."""
    return case(text, [sub(a[0], 1, a[1]), sub(b[0], 1, b[1]), OR(sub(c[0], 2, c[1]), sub(d[0], 2, d[1]))], fig=fig, lab='alpha')
def match(left, right, ans, title="Match the Columns"):
    rows = "".join(f"<tr><td>{('('+chr(97+i)+') '+l) if l else ''}</td><td>({'i ii iii iv v vi'.split()[i]}) {r}</td></tr>" for i, (l, r) in enumerate(zip(left + [''] * 9, right)) if l or r)
    q = f"{title}<table class='t' style='margin:1mm 0'><tr><th>Column I</th><th>Column II</th></tr>{rows}</table>"
    return sa(q, 5, "<b>Answer:</b> " + ", ".join(ans) + ". (1 mark for each correct match)")
def fill(words, sents, ans):
    q = f"Complete the given sentences (choose from the words in the box): <b>({', '.join(words)})</b><br>" + "".join(f"{['i','ii','iii','iv','v'][i]}. {s}<br>" for i, s in enumerate(sents))
    return sa(q, 5, "<b>Answers:</b> " + "; ".join(f"{['i','ii','iii','iv','v'][i]}. {a}" for i, a in enumerate(ans)) + " (1 mark each)")
INSTR = ["All questions are compulsory.",
 "This question paper has five sections A, B, C, D and E. Marks are indicated against each question.",
 "Section A (Q. 1, parts I–XII) consists of multiple choice questions of 1 mark each.",
 "Section B (Q. 2–5) consists of very short answer questions of 2 marks each.",
 "Section C (Q. 6–8) consists of short answer questions of 3 marks each.",
 "Section D (Q. 9–11) consists of long answer questions of 5 marks each.",
 "Section E (Q. 12–15) consists of four case-based / source-based questions of 4 marks each (1 + 1 + 2).",
 "There is no overall choice. However, internal choice is given in some questions. Only one of the choices in such questions is to be attempted.",
 "Draw neat and labelled diagrams wherever required."]
OUT = "D:/Coaching Chapterwise PDFs/Class_06/Science/School_Pattern_Papers"
def make(n, term, A, B, C, D, E, name):
    meta = dict(cls=6, subject='Science', title='CLASS VI — SCIENCE · FULL-YEAR PRACTICE PAPER', title_extra=f"Annual Examination Pattern · Session 2026-27 · {term}", set_no=n, time='2 Hours 30 Minutes', marks=60, instr=INSTR)
    secs = [sec("SECTION A — Multiple Choice Questions", "Question 1 has twelve parts (I–XII). Each carries 1 mark.", [mcqset(A)]),
            sec("SECTION B — Very Short Answer Questions", "2 marks each (about 30–40 words).", B),
            sec("SECTION C — Short Answer Questions", "3 marks each (about 60 words).", C),
            sec("SECTION D — Long Answer Questions", "5 marks each.", D),
            sec("SECTION E — Case-based / Source-based Questions", "Read the cases carefully and answer. Each question carries 4 marks.", E)]
    assert len(A) == 12 and len(B) == 4 and len(C) == 3 and len(D) == 3 and len(E) == 4
    build(meta, secs, OUT, name)
