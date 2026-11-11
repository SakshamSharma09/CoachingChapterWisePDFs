"""Re-render every chapter that has an extras module. python render_extras.py [--prefix c8m,c9m] [--workers 4]
Validates AR(6)/CASE(3)/MISTAKES counts first, retries transient PDF write errors."""
import sys, glob, re, subprocess, importlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
here = Path(__file__).resolve().parent; sys.path.insert(0, str(here))
SUBJ = {"m": "Maths", "s": "Science", "sst": "Social_Science", "e": "English", "h": "Hindi", "hi": "Hindi"}
want = sys.argv[sys.argv.index("--prefix") + 1].split(",") if "--prefix" in sys.argv else None
workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
jobs = []
for f in sorted(glob.glob(str(here / "x" / "c*_ch*_x.py"))):
    mod = Path(f).stem[:-2]; m = re.fullmatch(r"c(\d+)(m|sst|s|e|hi|h)_ch(\d+)", mod)
    if not m or (want and f"c{m.group(1)}{m.group(2)}" not in want): continue
    x = importlib.import_module(f"x.{mod}_x")
    ok = len(getattr(x, "MISTAKES", [])) >= 4
    if m.group(2) in ("m", "s", "sst"): ok = ok and len(getattr(x, "AR", [])) == 6 and len(getattr(x, "CASE", [])) == 3
    if m.group(2) in ("m", "s"): ok = ok and bool(getattr(x, "FORMULAS", None))
    if not ok: print("INCOMPLETE", mod); continue
    jobs.append((mod, int(m.group(1)), SUBJ[m.group(2)]))
def run(j):
    mod, cls, subj = j
    for _ in range(5):
        r = subprocess.run([sys.executable, "-W", "ignore", str(here / "run_graded.py"), mod, str(cls), subj], capture_output=True, text=True, cwd=here)
        if r.returncode == 0 and r.stdout.count("pages @") == 12 and all(" 2 pages" in l for l in r.stdout.splitlines() if "pages @" in l): return mod, True, ""
    return mod, False, (r.stderr or r.stdout)[-300:]
with ThreadPoolExecutor(workers) as ex:
    for mod, ok, msg in ex.map(run, jobs): print(mod, "ok" if ok else "FAIL " + msg, flush=True)
for cls in sorted({j[1] for j in jobs}):
    for subj in sorted({j[2] for j in jobs if j[1] == cls}):
        if subj in ("Maths", "Science"):
            subprocess.run([sys.executable, "-W", "ignore", str(here / "formula_sheets.py"), str(cls), subj], cwd=here)
