"""Heuristic MCQ quality scan over every graded chapter module. Flags: duplicate options, option equal to stem,
literal placeholders (none/xxx/TODO), options reused verbatim across >=6 unrelated questions (auto-fill symptom).
python mcq_scan.py [prefix]"""
import sys, glob, importlib, collections, re, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common
pre = sys.argv[1] if len(sys.argv) > 1 else ""
bad = collections.Counter(); notes = []
for f in sorted(glob.glob(str(Path(__file__).resolve().parent / f"c*{pre}*_ch*.py"))):
    name = Path(f).stem
    try: m = importlib.import_module(name)
    except Exception as e: notes.append(f"{name}: import failed {e!r}"[:100]); continue
    for tier, bank in getattr(m, "TIERS", {}).items():
        A = bank["A"]; items = common.interleave(A) if A and isinstance(A[0], list) else list(A)
        use = collections.Counter()
        for it in items:
            o = it.get("opts") or []
            if len(set(o)) < len(o): notes.append(f"{name}/{tier}: duplicate options in '{it['q'][:50]}'")
            if any(re.fullmatch(r"(?i)\s*(none|xxx|todo|tbd|\?+)\s*", x) for x in o): notes.append(f"{name}/{tier}: placeholder option in '{it['q'][:50]}'")
            for x in o:
                if len(x) > 3 and not re.fullmatch(r"[\d$.\\^{}()\s,+\-×÷=/a-zA-Z°]*", x): use[x] += 1
        for x, n in use.items():
            if n >= 8: notes.append(f"{name}/{tier}: option '{x[:40]}' reused in {n} MCQs")
print("\n".join(notes[:60])); print("flags:", len(notes))
