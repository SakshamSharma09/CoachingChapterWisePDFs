from lib import mcq, Q, OR
from mk9 import M4, build
def AM(rows):
    return [M4(q, c, w, y) for q, c, w, y in rows]
def QS(rows):
    return [Q(q, a, s) for q, a, s in rows]
def finish(rows, B, C, D):
    assert len(rows)==40 and len(B)==16 and len(C)==24 and len(D)==16, (len(rows),len(B),len(C),len(D))
    A = AM(rows)
    return A, QS(B), QS(C), QS(D)
