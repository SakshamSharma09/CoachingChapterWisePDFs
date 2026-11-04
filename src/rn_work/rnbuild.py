"""Shared builder for the new Maths notes sets (portable paths, Linux Chromium).
Usage: python3 rnbuild.py <workdir> <class> <first>-<last> <outname> "<Title>" "<sub>" "<label>"
"""
import sys, os, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rnlib'))
os.environ.setdefault('CHROMIUM_PATH', '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')
from notes import check_chapters, build_pdf

import re
_SUP = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿᵐ", "0123456789-+nm"))
_SUB = dict(zip("₀₁₂₃₄₅₆₇₈₉₊₋ₙ", "0123456789+-n"))
_RS = re.compile("[" + "".join(_SUP) + "]+")
_RB = re.compile("[" + "".join(_SUB) + "]+")
def _fix(x):
    if isinstance(x, str):
        x = _RS.sub(lambda m: "<sup>" + "".join(_SUP[c] for c in m.group()).replace("-", "&minus;") + "</sup>", x)
        return _RB.sub(lambda m: "<sub>" + "".join(_SUB[c] for c in m.group()).replace("-", "&minus;") + "</sub>", x)
    if isinstance(x, (list, tuple)):
        return type(x)(_fix(i) for i in x)
    if isinstance(x, dict):
        return {k: _fix(v) for k, v in x.items()}
    return x

def run(work, first, last, out, title, sub, label):
    sys.path.insert(0, os.path.join(HERE, work))
    chs = [_fix(importlib.import_module(f"c{i:02d}").CH) for i in range(first, last + 1)]
    check_chapters(chs)
    build_pdf(dict(title=title, sub=sub, label=label), chs, out)
    print("built", out, [c['num'] for c in chs])
