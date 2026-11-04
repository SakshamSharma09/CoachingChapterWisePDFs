"""Line-based authoring shortcut on top of sci.py.
MCQ line : question ~~ correct ~~ w1 ~~ w2 ~~ w3 ~~ why      (blank line starts a new topic group)
AR line  : AR ~~ assertion ~~ reason ~~ code(a-d) ~~ why
Z line   : question ~~ step|marks ~~ step|marks ...          (B/C/D sections, one per line)"""
from sci import MC, AR, Z, T

def mcs(text):
    groups = []
    for blk in text.strip().split("\n\n"):
        rows, ars = [], []
        for ln in blk.strip().splitlines():
            f = [x.strip() for x in ln.split("~~")]
            if f[0] == "AR":
                assert len(f) == 5, ln
                ars.append(AR(f[1], f[2], f[3], f[4]))
            else:
                assert len(f) == 6, ln
                rows.append(tuple(f))
        groups.append((MC(rows) if rows else []) + ars)
    return groups

def zs(text):
    out = []
    for ln in text.strip().splitlines():
        f = [x.strip() for x in ln.split("~~")]
        out.append(Z(f[0], *f[1:]))
    return out

def tier(a, b, c, d):
    return T(mcs(a), zs(b), zs(c), zs(d))
