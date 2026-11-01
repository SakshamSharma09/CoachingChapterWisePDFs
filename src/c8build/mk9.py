"""Helpers: build chapter SETS/POOL from flat lists; mcq helper with correct option first."""
from lib import mcq, Q, OR
def M4(q, c, w, why=""):
    w = [x for x in w if x != c]
    seen = []; 
    for x in w:
        if x not in seen: seen.append(x)
    assert len(seen) >= 3, (q, c, w)
    return mcq(q, [c] + seen[:3], "a", why)
def build(A, B, C, D):
    A = [A[i] for i in sorted(range(40), key=lambda i: (i % 4, i // 4))]
    assert len(A) == 40 and len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
    SETS = {
      "A": dict(A=A[0:10], B=B[0:4], C=[C[0], C[1], OR(C[2], C[3]), OR(C[4], C[5])], D=[OR(D[0], D[1]), OR(D[2], D[3])]),
      "B": dict(A=A[10:20], B=B[4:8], C=[C[6], C[7], OR(C[8], C[9]), OR(C[10], C[11])], D=[OR(D[4], D[5]), OR(D[6], D[7])]),
    }
    POOL = dict(A=A[20:40], B=B[8:16], C=C[12:24], D=D[8:16])
    return SETS, POOL
