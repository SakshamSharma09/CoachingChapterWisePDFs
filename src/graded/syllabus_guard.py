"""Scan graded chapter sources (and rendered text) for topics that are NOT in the current assessed syllabus.
python syllabus_guard.py            -> prints every hit as file:line: keyword
Add keywords to EXCLUDED when the owner confirms more deleted topics. Matching is case-insensitive."""
import re, glob, sys
from pathlib import Path
here = Path(__file__).resolve().parent
EXCLUDED = {  # file-prefix -> [(regex, reason)]
    "c10m": [(r"euclid", "Euclid's division lemma/algorithm removed"), (r"division algorithm|divide .{0,30}polynomial|polynomial division|quotient is .{0,40}remainder|remainder when .{0,30}divided by \$?x|completing the square|ogive|cumulative frequency curve|frustum", "polynomial division / completing square / ogive / frustum removed"),
             (r"construct(ion|ing)\b.{0,40}(tangent|triangle|similar)|ruler and compass|compass", "Constructions chapter removed"), (r"3q\s*\+\s*1|6q\s*\+\s*1|form 3q|[489]q\s*\+\s*[1-8]|square of any (odd )?integer|odd integer is of the form", "Euclid-lemma proofs removed")],
    "c10s": [(r"periodic (table|classification)|mendeleev|dobereiner|newlands", "Periodic Classification removed"), (r"sources of energy|solar cell|biogas|nuclear (reactor|energy)", "Sources of Energy removed"),
             (r"sustainable management|forests and wildlife|water harvesting", "Sustainable Management removed")],
}
hits = 0
for f in sorted(glob.glob(str(here / "c*_ch*.py"))):
    pre = Path(f).name.split("_")[0]
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        for rx, why in EXCLUDED.get(pre, []):
            if re.search(rx, line, re.I):
                print(f"{Path(f).name}:{i}: {why}: {line.strip()[:110]}"); hits += 1
print("syllabus_guard hits:", hits)
sys.exit(1 if hits else 0)
