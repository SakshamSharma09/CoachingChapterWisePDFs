from lib import mcq, Q, OR
from mk9 import M4, build
AR_OPTS = ["Both A and R are true and R is the correct explanation of A",
           "Both A and R are true but R is not the correct explanation of A",
           "A is true but R is false",
           "A is false but R is true"]
def AR(a, r, ans, why):
    return mcq(f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}", list(AR_OPTS), ans, why)
def finish(rows, ars, B, C, D):
    A = [M4(q, c, w, y) for q, c, w, y in rows] + [AR(*x) for x in ars]
    assert len(A) == 40 and len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
    return A, [Q(*x) for x in B], [Q(*x) for x in C], [Q(*x) for x in D]
