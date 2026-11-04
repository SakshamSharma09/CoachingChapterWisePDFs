"""Compact line-based authoring helper for Class 6/7 Science banks (wraps sci.py).
MCQ line : question ## correct ## wrong1 ## wrong2 ## wrong3 ## why
Z line   : question ## step ## step ...   (each step = 1 mark unless it ends with |n)
Shorthand: [[H2O]] -> chemistry ; <<x^2>> -> maths."""
import re
from sci import MC, Z as _Z, T as _T

def _lines(s):
    return [l.strip() for l in s.strip().split("\n") if l.strip()]

def mc(block):
    rows = []
    for l in _lines(block):
        p = [x.strip() for x in l.split(" ## ")]
        if len(p) == 5: p.append("")
        assert len(p) == 6, l
        rows.append(tuple(p))
    return MC(rows)

def zs(block):
    out = []
    for l in _lines(block):
        p = [x.strip() for x in l.split(" ## ")]
        q, steps = p[0], p[1:]
        steps = [s if re.search(r"\|\d$", s) else s + "|1" for s in steps]
        out.append(_Z(q, *steps))
    return out

def tier(A, B, C, D):
    return _T(A, zs(B), zs(C), zs(D))
