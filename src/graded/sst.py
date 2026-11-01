"""Compact authoring helpers for hand-written Social Science graded banks (own module).
MC rows: 'question | correct | wrong1 | wrong2 | wrong3 | why'.   AR rows: 'assertion | reason | code | why'.
B2/C3/D5: question + answer points (marks are auto-split)."""
import common
from common import M4, Q, grp
from lib import mcq

# Subject string 'Social_Science' (folder name) -> display 'Social Science' without editing common.py
_orig = common.build_chapter
def _bc(pg, root, cls, subject, *a, **k):
    return _orig(pg, root, cls, subject.replace("_", " "), *a, **k)
common.build_chapter = _bc

AR_OPTS = ["Both A and R are true and R is the correct explanation of A.",
           "Both A and R are true but R is not the correct explanation of A.",
           "A is true but R is false.", "A is false but R is true."]

def MC(rows):
    out = []
    for r in rows:
        p = [x.strip() for x in r.split("|")]
        assert len(p) == 6, r
        out.append(M4(p[0], p[1], p[2:5], p[5]))
    return out

def AR(rows):
    out = []
    for r in rows:
        a, rr, code, why = [x.strip() for x in r.split("|")]
        out.append(mcq(f"Assertion (A): {a} Reason (R): {rr}", AR_OPTS[:], code, why))
    return out

def _split(total, n):
    if n == total: return [1] * n
    if total == 2 and n == 1: return [2]
    if total == 3 and n == 2: return [2, 1]
    if total == 3 and n == 1: return [3]
    if total == 5 and n == 4: return [2, 1, 1, 1]
    if total == 5 and n == 3: return [2, 2, 1]
    if total == 5 and n == 2: return [3, 2]
    raise ValueError((total, n))

def _Z(total, q, steps):
    m = _split(total, len(steps))
    return Q(q, "; ".join(f"{s} ({k})" for s, k in zip(steps, m)) + ".", "+".join(map(str, m)))

def B2(q, *s): return _Z(2, q, s)
def C3(q, *s): return _Z(3, q, s)
def D5(q, *s): return _Z(5, q, s)

def T(A, B, C, D):
    assert sum(len(g) for g in A) >= 30, sum(len(g) for g in A)
    assert len(B) == 12 and len(C) == 18 and len(D) == 12, (len(B), len(C), len(D))
    return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
