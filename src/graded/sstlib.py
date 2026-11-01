"""Helpers for Social Science graded banks (Class 9/10). Hand-written content; this file only removes boilerplate."""
from common import M4, Q, grp
import common, lib

# --- display subject as 'Social Science' (runner is called with Social_Science so folders match) ---
if not getattr(common, "_sst_patched", False):
    _orig = common.build_chapter
    def _bc(pg, root, cls, subject, *a, **k):
        return _orig(pg, root, cls, subject.replace("_", " "), *a, **k)
    common.build_chapter = _bc
    common._sst_patched = True

def mc(rows):
    """rows: (question, right, wrong1, wrong2, wrong3, why)"""
    return [M4(r[0], r[1], list(r[2:5]), r[5] if len(r) > 5 else "") for r in rows]

AR_TXT = ["Both A and R are true and R is the correct explanation of A.",
          "Both A and R are true but R is not the correct explanation of A.",
          "A is true but R is false.", "A is false but R is true."]
def ar(a, r, k, why=""):
    """k = 1..4 index of the correct option (1 = both true & R explains A)."""
    q = f"<b>Assertion (A):</b> {a}<br><b>Reason (R):</b> {r}"
    return lib.mcq(q, AR_TXT[:], "abcd"[k - 1], why)

def W(q, *pts):
    """Written answer; one mark per point."""
    n = len(pts)
    return Q(q, "; ".join(f"{p} (1)" if not p.rstrip().endswith(")") else p for p in pts), "+".join("1" * 1 for _ in range(n)))

def W2(q, pts, split):
    """pts with explicit marks as list of (text, marks)."""
    return Q(q, "; ".join(f"{t} ({m})" for t, m in pts), "+".join(str(m) for _, m in pts))

def tier(A, B, C, D):
    for lst, mk in ((B, 2), (C, 3), (D, 5)):
        for it in lst:
            assert sum(int(x) for x in it["split"].split("+")) == mk, (mk, it["q"][:60], it["split"])
    return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
