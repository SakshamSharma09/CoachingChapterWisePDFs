"""Reviewer helper: tidy sign/unit artefacts in generated text of a TIERS dict
('1x' -> 'x', '-1(' -> '-(', '+-' -> '-', '--' -> '+')."""
import re
_UNIT = re.compile(r"(?<![\w.^{}\\])1(?=[xyz](?![a-z]))")
_NEG = re.compile(r"(?<=[-+])1(?=\()")
def _fx(s):
    if not isinstance(s, str): return s
    s = _UNIT.sub("", s)
    s = _NEG.sub("", s)
    s = s.replace("--", "+").replace("+-", "-")
    return s
def tidy(tiers):
    def walk(x):
        if isinstance(x, dict):
            for k, v in list(x.items()):
                if k in ("q", "ans", "why"): x[k] = _fx(v)
                elif k == "opts": x[k] = [_fx(o) for o in v]
                elif k == "steps": x[k] = [(_fx(t), m) if isinstance(t, str) else (t, m) for t, m in v]
                else: walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    walk(tiers)
    return tiers
