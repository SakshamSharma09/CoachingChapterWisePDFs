"""Build every graded Unit Test (50 m), Full-Year paper (80 m) and MCQ-only test (50 MCQ) whose chapters are all complete.
python run_exams.py [--dry] [--with-full] [--with-mcq] [--class 8] [--subject Maths] [--workers 4]
Units come from Class_NN/<Subject>/Practice_Papers/3_Unit_Tests_*/UnitK_ChAA-BB_* when they exist, otherwise from EXTRA_UNITS below
(Class 10 SST / English / Hindi, Class 9 English / Hindi, whose practice-paper folders are nested differently).
Full-year and MCQ tests use every chapter that has a chapter bank. Skips anything already complete (16 PDFs) or whose chapters are unfinished."""
import re, subprocess, sys, glob, os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
repo = Path(__file__).resolve().parents[2]; here = Path(__file__).resolve().parent
PFX = {"Maths": "m", "Science": "s", "Social_Science": "sst", "English": "e", "Hindi": "h", "English_Gulmohar": "gl", "English_Ruskin_Bond": "rb"}
def prefix(cls, subj): return f"c{cls}hi" if (cls == 9 and subj == "Hindi") else f"c{cls}{PFX[subj]}"
# subjects whose chapter list is incomplete: no full-year / MCQ-whole-syllabus test yet
INCOMPLETE = {(9, "Hindi"), (8, "English_Gulmohar"), (8, "English_Ruskin_Bond")}   # Gulmohar: only some units supplied, so no full-year / whole-book MCQ test
EXTRA_UNITS = {
    (10, "Social_Science"): [("Unit1_Ch01-05", 1, 5), ("Unit2_Ch06-09", 6, 9), ("Unit3_Ch10-12", 10, 12), ("Unit4_Ch13-17", 13, 17), ("Unit5_Ch18-22", 18, 22)],
    (10, "English"): [("Unit1_Ch01-09", 1, 9), ("Unit2_Ch10-18", 10, 18), ("Unit3_Ch19-28", 19, 28)],
    (10, "Hindi"): [("Unit1_Ch01-05", 1, 5), ("Unit2_Ch06-10", 6, 10), ("Unit3_Ch11-15", 11, 15)],
    (9, "English"): [("Unit1_Ch01-04", 1, 4), ("Unit2_Ch05-08", 5, 8)],
    (9, "Hindi"): [("Unit2_Ch07-12", 7, 12)],
    (8, "English_Gulmohar"): [("UnitA_Ch01-04", 1, 4), ("UnitB_Ch05-08", 5, 8), ("UnitC_Ch09-12", 9, 12), ("UnitD_Ch13-17", 13, 17)],
}
dry = "--dry" in sys.argv
with_full = "--with-full" in sys.argv
with_mcq = "--with-mcq" in sys.argv
rebuild_hard = "--rebuild-hard" in sys.argv   # re-render only the Hard tier (after AR/case extras changed) for Maths/Science/SST
workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
fc = int(sys.argv[sys.argv.index("--class") + 1]) if "--class" in sys.argv else None
fs = sys.argv[sys.argv.index("--subject") + 1] if "--subject" in sys.argv else None

def complete(p):
    n = len(glob.glob(str(p / "*" / "*.pdf"))); d = len(glob.glob(str(p / "*")))
    return n == 4 * d and d in (2, 4)   # 4 PDFs (3 sets + key) per tier folder; 4 tiers, or 2 for Gulmohar
def chap_ok(cls, subj, ch):
    g = glob.glob(str(repo / f"Class_{cls:02d}" / subj / "Graded_Papers" / f"Ch{ch:02d}_*"))
    return bool(g) and complete(Path(g[0])) and (here / f"{prefix(cls, subj)}_ch{ch:02d}.py").exists()
jobs = []
for cls in range(6, 11):
    if fc and cls != fc: continue
    for subj in PFX:
        if fs and subj != fs: continue
        root = repo / f"Class_{cls:02d}" / subj
        if not root.exists(): continue
        gp = root / "Graded_Papers"
        units = []
        for u in sorted(glob.glob(str(root / "Practice_Papers" / "3_Unit_Tests*" / "Unit*"))):
            m = re.match(r"(Unit\d+)_Ch(\d+)-(\d+)", os.path.basename(u))
            if m: units.append((f"{m.group(1)}_Ch{int(m.group(2)):02d}-{int(m.group(3)):02d}", int(m.group(2)), int(m.group(3))))
        if (cls, subj) in EXTRA_UNITS and not units: units = EXTRA_UNITS[(cls, subj)]
        for label, a, b in units:
            jobs.append((cls, subj, "unit", label, list(range(a, b + 1)), gp / "Unit_Tests" / label))
        mods = sorted(int(re.search(r"_ch(\d+)\.py", f).group(1)) for f in glob.glob(str(here / f"{prefix(cls, subj)}_ch*.py")))
        if mods and (cls, subj) not in INCOMPLETE:
            jobs.append((cls, subj, "full", "FullYear", mods, gp / "Full_Year"))
            jobs.append((cls, subj, "mcq", "MCQ_Test", mods, gp / "MCQ_Tests"))

def run(job):
    cls, subj, kind, label, chs, out = job
    r = subprocess.run([sys.executable, "-W", "ignore", str(here / "exam.py"), str(cls), subj, kind, label, prefix(cls, subj), ",".join(map(str, chs))] + (["--tier", "Hard"] if rebuild_hard else []),
                       capture_output=True, text=True)
    ok = r.returncode == 0 and complete(out)
    return job, ok, "" if ok else (r.stderr or r.stdout)[-400:]

todo = []
for job in jobs:
    cls, subj, kind, label, chs, out = job
    ok = all(chap_ok(cls, subj, c) for c in chs)
    state = "DONE" if complete(out) else ("READY" if ok else "waiting")
    print(f"Class {cls} {subj:15s} {kind:4s} {label:22s} chapters {chs[0]}-{chs[-1]}: {state}", flush=True)
    if kind == "full" and not with_full: continue
    if kind == "mcq" and not with_mcq: continue
    if rebuild_hard:
        if subj in ("Maths", "Science", "Social_Science") and state in ("DONE", "READY") and not dry: todo.append(job)
        continue
    if state == "READY" and not dry: todo.append(job)
built = 0
with ThreadPoolExecutor(max_workers=workers) as ex:
    for job, ok, msg in ex.map(run, todo):
        print(f"   Class {job[0]} {job[1]} {job[2]} {job[3]}:", "built" if ok else "FAILED " + msg, flush=True); built += ok
print("built:", built)
