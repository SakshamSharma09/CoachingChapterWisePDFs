"""Build every graded Unit Test / Full-Year paper whose chapters are all complete.
python run_exams.py [--dry] [--with-full] [--class 8] [--subject Maths]
Units come from Class_NN/<Subject>/Practice_Papers/3_Unit_Tests_*/UnitK_ChAA-BB_*; full-year uses every chapter folder in 1_Chapter_Tests_*.
Skips anything already complete (16 PDFs) or whose chapter modules/folders are not finished."""
import re, subprocess, sys, glob, os
from pathlib import Path
repo = Path(__file__).resolve().parents[2]; here = Path(__file__).resolve().parent
PFX = {"Maths": "m", "Science": "s", "Social_Science": "sst"}
dry = "--dry" in sys.argv
with_full = "--with-full" in sys.argv   # full-year only once ALL chapters of a subject are final
fc = int(sys.argv[sys.argv.index("--class") + 1]) if "--class" in sys.argv else None
fs = sys.argv[sys.argv.index("--subject") + 1] if "--subject" in sys.argv else None

def complete(p): return len(glob.glob(str(p / "*" / "*.pdf"))) == 16
def chap_ok(cls, subj, ch):
    g = glob.glob(str(repo / f"Class_{cls:02d}" / subj / "Graded_Papers" / f"Ch{ch:02d}_*"))
    return bool(g) and complete(Path(g[0])) and (here / f"c{cls}{PFX[subj]}_ch{ch:02d}.py").exists()
jobs = []
for cls in range(6, 11):
    if fc and cls != fc: continue
    for subj in PFX:
        if fs and subj != fs: continue
        root = repo / f"Class_{cls:02d}" / subj
        if not root.exists(): continue
        ct = sorted(glob.glob(str(root / "Practice_Papers" / "1_Chapter_Tests*" / "Ch*")))
        allch = sorted({int(re.match(r"Ch(\d+)", os.path.basename(c)).group(1)) for c in ct})
        gp = root / "Graded_Papers"
        for u in sorted(glob.glob(str(root / "Practice_Papers" / "3_Unit_Tests*" / "Unit*"))):
            m = re.match(r"(Unit\d+)_Ch(\d+)-(\d+)", os.path.basename(u))
            if not m: continue
            a, b = int(m.group(2)), int(m.group(3)); chs = list(range(a, b + 1))
            label = f"{m.group(1)}_Ch{a:02d}-{b:02d}"
            jobs.append((cls, subj, "unit", label, chs, gp / "Unit_Tests" / label))
        mods = {int(re.search(r"_ch(\d+)\.py", f).group(1)) for f in glob.glob(str(here / f"c{cls}{PFX[subj]}_ch*.py"))}
        allch = sorted(set(allch) | mods)
        if allch: jobs.append((cls, subj, "full", "FullYear", allch, gp / "Full_Year"))
built = 0
for cls, subj, kind, label, chs, out in jobs:
    ok = all(chap_ok(cls, subj, c) for c in chs)
    state = "DONE" if complete(out) else ("READY" if ok else "waiting")
    print(f"Class {cls} {subj:15s} {kind:4s} {label:22s} chapters {chs[0]}-{chs[-1]}: {state}")
    if kind == "full" and not with_full: continue
    if state == "READY" and not dry:
        r = subprocess.run([sys.executable, "-W", "ignore", str(here / "exam.py"), str(cls), subj, kind, label, f"c{cls}{PFX[subj]}", ",".join(map(str, chs))], capture_output=True, text=True)
        print("   ", "built" if r.returncode == 0 else "FAILED: " + (r.stderr or r.stdout)[-300:]); built += (r.returncode == 0)
print("built:", built)
