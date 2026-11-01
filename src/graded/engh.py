"""English helper (own module): compact builders for graded English chapters."""
from common import M4, grp, Q

def m(stem, opts, why=""):
    """m("stem", "right|wrong|wrong|wrong", "why")"""
    o = [x.strip() for x in opts.split("|")]
    return M4(stem, o[0], o[1:], why)

def b(q, a): return Q(q, a if "(" in a else a + " (1+1)", "1+1")
def c(q, a): return Q(q, a, "1+1+1")
def d(q, a, split="2+2+1"): return Q(q, a, split)

def tier(A, B, C, D):
    """A: flat list (chunked in 10s so every set mixes topics)."""
    assert len(A) >= 30 and len(B) >= 12 and len(C) >= 18 and len(D) >= 12, (len(A), len(B), len(C), len(D))
    return dict(A=grp(A, 10), B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
