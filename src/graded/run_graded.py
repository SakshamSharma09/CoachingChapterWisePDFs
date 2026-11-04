"""Usage: python run_graded.py <module> <class> <subject> [--check] [--tier Easy,Hard]
Writes <repo>/Class_NN/<Subject>/Graded_Papers/ChNN_<slug>/<tier folder>/..."""
import sys, importlib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common, os
def _chrome():
    c='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
    return c if os.path.exists(c) else None
mod = importlib.import_module(sys.argv[1]); cls = int(sys.argv[2]); subject = sys.argv[3]
check = "--check" in sys.argv
only = None
if "--tier" in sys.argv: only = sys.argv[sys.argv.index("--tier") + 1].split(",")
for t in common.TIER_ORDER:
    common.make_sets(mod.TIERS[t], f"{subject}{mod.CHNO}{t}")
print("bank OK:", {t: {k: sum(len(g) if g and isinstance(g[0], list) else 1 for g in ([mod.TIERS[t][k]] if not isinstance(mod.TIERS[t][k][0], list) else mod.TIERS[t][k])) for k in "ABCD"} for t in common.TIER_ORDER} if False else "counts and duplicates passed")
if check: sys.exit(0)
from playwright.sync_api import sync_playwright
repo = Path(__file__).resolve().parents[2]
root = repo / f"Class_{cls:02d}" / subject.replace(" ", "_") / "Graded_Papers"
with sync_playwright() as p:
    br = p.chromium.launch(executable_path=_chrome()); pg = br.new_page()
    log = common.build_chapter(pg, root, cls, subject, mod.CHNO, mod.SLUG, mod.NAME, mod.TIERS, only)
    br.close()
for n, pgs, fs in log: print(f"{n}: {pgs} pages @ {fs}pt")
