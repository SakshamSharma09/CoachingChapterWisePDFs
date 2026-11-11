"""Graded UNIT TEST (50 m) and FULL-YEAR (80 m) papers composed from the chapter banks (no new questions).

python exam.py <class> <Subject> <unit|full> <label> <module_prefix> <ch,ch,...> [--check] [--tier Easy,Hard]
  e.g. python exam.py 8 Maths unit Unit1_Ch01-05 c8m 1,2,3,4,5
       python exam.py 8 Maths full FullYear c8m 1,2,...,14
Output: Class_NN/<Subject>/Graded_Papers/Unit_Tests/<label>/<tier folder>/  or  .../Full_Year/<tier folder>/
Each tier: 3 sets + merged key = 4 PDFs (16 per exam).  Questions are drawn round-robin across the chapters so every
chapter is covered; sets within a tier never share a question.
Blueprint: unit 50 = 15x1 + 5x2 + 5x3 (2 with OR) + 2x5 (OR);  full 80 = 20x1 + 6x2 + 6x3 (2 OR) + 6x5 (3 OR).
"""
import sys, importlib, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common
from common import interleave, shuffle_mcq, OR, lib, TIER_ORDER, TIER_FOLDER, TIER_LABEL, TIER_NICE, TIER_BLURB, NSETS, fit, to_pdf, unite, generic_paper

PLAN = {  # per section: (questions shown, items consumed per set)
    "unit": dict(A=(15, 15), B=(5, 5), C=(5, 7), D=(2, 4), marks=50, time="2 Hours", pages=3, c_or=2, d_or=2, name="UNIT TEST"),
    "full": dict(A=(20, 20), B=(6, 6), C=(6, 8), D=(6, 9), marks=80, time="3 Hours", pages=5, c_or=2, d_or=3, name="FULL-YEAR PAPER"),
    # MCQ-only test: 50 objective questions x 1 mark across the whole syllabus
    "mcq": dict(A=(50, 50), B=(0, 0), C=(0, 0), D=(0, 0), marks=50, time="1 Hour", pages=4, c_or=0, d_or=0, name="MCQ TEST"),
}

def flat(tier_bank):
    out = {}
    for k in "ABCD":
        v = tier_bank[k]
        out[k] = interleave(v) if v and isinstance(v[0], list) else list(v)
    return out

def pool(mods, tier, k):
    lists = [flat(m.TIERS[tier])[k] for m in mods]
    out = []
    for i in range(max(len(l) for l in lists)):
        for l in lists:
            if i < len(l): out.append(l[i])
    return out

def make_exam_sets(mods, tier, kind, tag):
    P = PLAN[kind]; pools = {k: pool(mods, tier, k) for k in "ABCD"}
    for k in "ABCD":
        need = P[k][1] * NSETS
        assert len(pools[k]) >= need, f"{tag}: section {k} has {len(pools[k])}, need {need}"
    ars, cases = [], []
    if tier == "Hard":
        exs = [common.load_extras(m.__name__) for m in mods]
        ars = interleave([list(getattr(e, "AR", []) or []) for e in exs if e])
        cases = interleave([list(getattr(e, "CASE", []) or []) for e in exs if e])
    nar = P["A"][0] // 5 if kind != "mcq" else 10
    ncase = {"unit": 1, "full": 2}.get(kind, 0)
    sets = []
    for s in range(NSETS):
        take = {k: pools[k][P[k][1] * s:P[k][1] * (s + 1)] for k in "ABCD"}
        rng = random.Random(f"{tag}{s}")
        A = [shuffle_mcq(i, rng) for i in take["A"]]
        if len(ars) >= nar * NSETS: A = A[:len(A) - nar] + [shuffle_mcq(i, rng) for i in ars[nar * s:nar * (s + 1)]]
        C = take["C"]; nC = P["C"][0]; orc = P["c_or"]; single = nC - orc
        Cq = C[:single] + [OR(C[single + 2 * i], C[single + 2 * i + 1]) for i in range(orc)]
        D = take["D"]; nD = P["D"][0]; ord_ = P["d_or"]; sd = nD - ord_
        Dq = D[:sd] + [OR(D[sd + 2 * i], D[sd + 2 * i + 1]) for i in range(ord_)]
        if ncase and len(cases) >= ncase * NSETS: Dq = cases[ncase * s:ncase * (s + 1)] + Dq[ncase:]
        sets.append(dict(A=A, B=take["B"], C=Cq, D=Dq))
    return sets

def instr(kind, tier):
    if kind == "mcq":
        return ["All questions are compulsory.", "Q. 1–50 are Multiple Choice Questions (1 mark each); there is no negative marking.",
                "Choose the correct option and write its letter (a, b, c or d) against the question number.",
                "Questions cover the whole syllabus of the class.", TIER_BLURB[tier] + "."]
    P = PLAN[kind]; a, b, c, d = P["A"][0], P["B"][0], P["C"][0], P["D"][0]
    n1 = a; n2 = n1 + b; n3 = n2 + c; n4 = n3 + d
    return ["All questions are compulsory.", f"Q. 1–{n1} are Objective Type (1 mark each).",
            f"Q. {n1+1}–{n2} are Very Short Answer Type (2 marks each).", f"Q. {n2+1}–{n3} are Short Answer Type (3 marks each).",
            f"Q. {n3+1}–{n4} are Long Answer Type (5 marks each).",
            f"Internal choice is given in Q. {n3-P['c_or']+1}–{n3} and Q. {n4-P['d_or']+1}–{n4}.",
            "Write the question number before each answer.", TIER_BLURB[tier] + "."]

def _chrome():
    import os, glob
    c = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"
    if Path(c).exists(): return c
    if os.environ.get("CHROMIUM_PATH"): return os.environ["CHROMIUM_PATH"]
    g = sorted(glob.glob(os.path.expanduser("~/AppData/Local/ms-playwright/chromium-*/chrome-win*/chrome.exe")))
    return g[-1] if g else None

if __name__ == "__main__":
    cls = int(sys.argv[1]); subject = sys.argv[2]; kind = sys.argv[3]; label = sys.argv[4]; prefix = sys.argv[5]
    chs = [int(x) for x in sys.argv[6].split(",")]
    check = "--check" in sys.argv
    only = sys.argv[sys.argv.index("--tier") + 1].split(",") if "--tier" in sys.argv else None
    mods = [importlib.import_module(f"{prefix}_ch{c:02d}") for c in chs]
    P = PLAN[kind]
    for t in TIER_ORDER:
        make_exam_sets(mods, t, kind, f"{subject}{label}{t}")
    print("bank OK: sets can be composed for", len(mods), "chapters")
    if check: sys.exit(0)
    from playwright.sync_api import sync_playwright
    repo = Path(__file__).resolve().parents[2]
    base = repo / f"Class_{cls:02d}" / subject.replace(" ", "_") / "Graded_Papers" / {"unit": "Unit_Tests", "full": "Full_Year", "mcq": "MCQ_Tests"}[kind]
    if kind == "unit": base = base / label
    lib.CHAPTERS.clear(); lib.CHAPTERS.update({c: m.NAME for c, m in zip(chs, mods)}); lib.SUBJECT[0] = subject
    if kind == "unit":
        def _lab(c):
            names = ", ".join(lib.CHAPTERS[x] for x in c)
            return f"Chapters {c[0]}–{c[-1]}: <b>{names}</b>"
        lib.ch_label = _lab
    _gk = lib.generic_key
    gk = lambda meta, data: _gk(meta, data).replace("Class 8 ", f"Class {cls} ", 1)
    secs = [("A", "SECTION — A (Objective Type Questions)" if kind != "mcq" else "MULTIPLE CHOICE QUESTIONS", 1, "Choose the correct option and write it in your answer book."),
            ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 20–30 words each."),
            ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 40–60 words each."),
            ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")]
    if kind == "mcq": secs = secs[:1]
    chosen = tuple(chs) if (len(chs) <= 6 or kind != "unit") else (chs[0], chs[-1])
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=_chrome())
        pg = br.new_page()
        for tier in TIER_ORDER:
            if only and tier not in only: continue
            d = base / TIER_FOLDER[tier]; d.mkdir(parents=True, exist_ok=True)
            sets = make_exam_sets(mods, tier, kind, f"{subject}{label}{tier}")
            keys = []
            for s, data in enumerate(sets, 1):
                stem = f"{label}_{tier}_Set_{s}"
                meta = dict(doc=stem, title=f"CLASS {cls} — {subject.replace('_', ' ').upper()} · {TIER_LABEL[tier]} {P['name']}", set=str(s), chs=chosen,
                            time=P["time"], marks=P["marks"], secs=secs, instr=instr(kind, tier))
                n, fs = fit(pg, lambda f: generic_paper(meta, data, f), d / f"{stem}.pdf",
                            f"Mastermind Coaching Classes — Class {cls} {subject} · {label} · {TIER_NICE[tier]} · Set {s}", target=P["pages"])
                print(f"{stem}: {n} pages @ {fs}pt")
                k = d / f"_k{s}.pdf"; to_pdf(pg, gk(meta, data), k, f"Answer Key · {subject} {label} · {TIER_NICE[tier]} · Set {s}"); keys.append(k)
            unite(keys, d / f"{label}_{tier}_Answer_Key.pdf")
        br.close()
