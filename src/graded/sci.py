"""Compact authoring helpers for hand-written Science graded banks.
Shorthand inside text: [[H2O]] -> $\\ce{H2O}$ ; <<x^2>> -> $x^2$."""
import re
from common import M4, Q, grp
from lib import mcq

def tx(s):
    s = re.sub(r"\[\[(.+?)\]\]", lambda m: "$\\ce{" + m.group(1) + "}$", s)
    s = re.sub(r"<<(.+?)>>", lambda m: "$" + m.group(1) + "$", s)
    return s

def MC(rows):
    return [M4(tx(q), tx(c), [tx(a), tx(b), tx(d)], tx(w)) for q, c, a, b, d, w in rows]

AR_OPTS = ["Both A and R are true and R is the correct explanation of A.",
           "Both A and R are true but R is not the correct explanation of A.",
           "A is true but R is false.", "A is false but R is true."]
def AR(a, r, code, why):
    """Assertion-Reason MCQ. code in 'abcd' = the correct standard option."""
    return mcq(tx(f"Assertion (A): {a} Reason (R): {r}"), AR_OPTS[:], code, tx(why))

def Z(q, *steps):
    """Question with marking steps, each 'text|marks'."""
    st = []
    for s in steps:
        t, m = s.rsplit("|", 1); st.append((tx(t.strip()), int(m)))
    return Q(tx(q), "; ".join(f"{t} ({m})" for t, m in st) + ".", "+".join(str(m) for _, m in st))

def T(A, B, C, D):
    """A: list of groups; B: 12 Z items; C: 18; D: 12."""
    assert len(B) == 12 and len(C) == 18 and len(D) == 12, (len(B), len(C), len(D))
    assert sum(len(g) for g in A) >= 30, sum(len(g) for g in A)
    for L, m in ((B, 2), (C, 3), (D, 5)):
        for x in L:
            assert sum(int(p) for p in x["split"].split("+")) == m, (m, x["q"][:60], x["split"])
    return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
