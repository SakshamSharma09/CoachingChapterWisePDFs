"""Ultra-compact authoring layer for SST graded banks (own module; builds on sst.py).
A rows : 'question | right | w1 | w2 | w3 | why'   or   'AR: assertion | reason | k(1-4) | why'
B/C/D  : 'question @ point @ point ...'  (2/3/5 marks; points are auto-split)"""
from sst import *
import sst, lib

def _a(rows):
    out = []
    for r in rows:
        if r.startswith("AR:"):
            a, rr, k, why = [x.strip() for x in r[3:].split("|")]
            out.append(mcq(f"Assertion (A): {a} Reason (R): {rr}", AR_OPTS[:], "abcd"[int(k) - 1], why))
        else:
            out += MC([r])
    return out

def _w(total, rows):
    out = []
    for r in rows:
        p = [x.strip() for x in r.split(" @ ")]
        out.append(sst._Z(total, p[0], p[1:]))
    return out

import random
def _mix(x, tag):
    x = list(x); random.Random(tag).shuffle(x); return x

def tier(A, B, C, D):
    A = _mix(_a(A), A[0][:20])   # deterministic shuffle so every set mixes topics / AR items
    return T([A[i:i + 10] for i in range(0, len(A), 10)], _mix(_w(2, B), B[0][:9]), _mix(_w(3, C), C[0][:9]), _mix(_w(5, D), D[0][:9]))
