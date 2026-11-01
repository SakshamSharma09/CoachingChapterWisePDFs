import os, sys, copy, random, importlib, subprocess, re
from playwright.sync_api import sync_playwright
import lib
from lib import CHAPTERS, OR, generic_paper, generic_key, paper_html, key_html, to_pdf
import supp

ROOT = "/home/claude/papers/Maths_Class10_Paper_Generated"

def pages(pdf):
    o = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    return int([l for l in o.splitlines() if l.startswith("Pages")][0].split()[1])

FIXED = re.compile(r"both|neither|cannot be determined|none|^correct$|all of these|all the above", re.I)
def shuffle_mcq(it, rng):
    it = copy.deepcopy(it)
    opts = it["opts"]; ans = "abcd".index(it["ans"])
    free = [i for i, o in enumerate(opts) if not FIXED.search(o)]
    perm = free[:]; rng.shuffle(perm)
    new = opts[:]; newans = ans
    for dst, src in zip(free, perm):
        new[dst] = opts[src]
        if src == ans: newans = dst
    it["opts"] = new; it["ans"] = "abcd"[newans]
    return it

def shuffle_paper(data, seed):
    rng = random.Random(seed)
    d = dict(data); d["A"] = [shuffle_mcq(i, rng) for i in data["A"]]
    return d

# ---------------- bank ----------------
BANK = []
def add(item, ch, lvl, src):
    BANK.append(dict(item=item, ch=ch, lvl=lvl, src=src, uid=len(BANK), used=0))

for ch in range(1, 15):
    m = importlib.import_module(f"content.ch{ch:02d}")
    for s, d in m.SETS.items():
        for lvl in "ABCD":
            for it in d[lvl]:
                for q in ([it["a"], it["b"]] if it["kind"] == "or" else [it]):
                    add(q, ch, lvl, "chapter")
PAIRS = {}
for p in range(1, 8):
    m = importlib.import_module(f"pairs.p{p}")
    PAIRS[p] = m
    c1, c2 = m.CHS
    for s, d in m.SETS.items():
        for i, it in enumerate(d["A"]): add(it, c1 if i < 5 else c2, "A", "pair")
        for i, it in enumerate(d["B"]): add(it, c1 if i < 2 else c2, "B", "pair")
        for i, it in enumerate(d["C"]):
            c = c1 if i % 2 == 0 else c2
            for q in ([it["a"], it["b"]] if it["kind"] == "or" else [it]): add(q, c, "C", "pair")
        for i, it in enumerate(d["D"]):
            c = c1 if i % 2 == 0 else c2
            for q in [it["a"], it["b"]]: add(q, c, "D", "pair")
for q in supp.GRAPH: add(q, 3, "G", "supp")
for q in supp.C13: add(q, 13, "C", "supp")
for lst, c in ((supp.D13, 13), (supp.D7, 7), (supp.D8, 8), (supp.D12, 12)):
    for q in lst: add(q, c, "D", "supp")

import difflib
def _norm(b):
    t = b["item"]["q"]
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).lower()
def _ans(b):
    it = b["item"]
    return (it["opts"]["abcd".index(it["ans"])] if it["kind"] == "mcq" else it["ans"]).lower()
TAKEN_TXT = {}
def pick(ch, lvl, n, prefer, taken, rng):
    if not taken:
        TAKEN_TXT.pop(id(taken), None); TAKEN_TXT.pop(("ans", id(taken)), None)
    chosen = TAKEN_TXT.setdefault(id(taken), [])
    cands = [b for b in BANK if b["ch"] == ch and b["lvl"] == lvl and b["uid"] not in taken]
    rng.shuffle(cands)
    cands.sort(key=lambda b: (b["used"], 0 if b["src"] in prefer else 1))
    out = []
    for b in cands:
        if len(out) == n: break
        t = _norm(b)
        if any(difflib.SequenceMatcher(None, t, c).ratio() > 0.62 for c in chosen): continue
        if b["lvl"] == "A" and any(_ans(b) == a for a in TAKEN_TXT.setdefault(("ans", id(taken)), [])): continue
        out.append(b); chosen.append(t); TAKEN_TXT[("ans", id(taken))].append(_ans(b))
    if len(out) < n: raise SystemExit(f"bank short: ch{ch} {lvl} need {n}")
    for b in out: b["used"] += 1; taken.add(b["uid"])
    return [b["item"] for b in out]

def orpair(ch, lvl, prefer, taken, rng):
    a, b = pick(ch, lvl, 2, prefer, taken, rng)
    return OR(a, b)

# ---------------- builders ----------------
def fit(pg, html_fn, out, foot, target, fmin=9.4):
    fs = 11.8
    while True:
        to_pdf(pg, html_fn(fs), out, foot)
        n = pages(out)
        if n <= target or fs <= fmin: break
        fs = round(fs - 0.2, 1)
    if n > target:  # allow one more page at a comfortable size
        fs = 11.0
        while True:
            to_pdf(pg, html_fn(fs), out, foot)
            if pages(out) <= target + 1 or fs <= fmin: break
            fs = round(fs - 0.2, 1)
    return pages(out), fs

def unite(files, out):
    subprocess.run(["pdfunite", *files, out], check=True)
    for f in files: os.remove(f)

S40 = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
       ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 20–30 words each."),
       ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 40–60 words each."),
       ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")]

def instr(counts, choice_from, extra):
    a, b, c, d = counts
    q1 = a; q2 = a + b; q3 = a + b + c; q4 = a + b + c + d
    return ["All questions are compulsory.",
            f"Q. 1–{q1} are Objective Type (1 mark each).",
            f"Q. {q1+1}–{q2} are Very Short Answer Type (2 marks each).",
            f"Q. {q2+1}–{q3} are Short Answer Type (3 marks each).",
            f"Q. {q3+1}–{q4} are Long Answer Type (5 marks each).",
            f"Internal choice is given in Q. {choice_from} to {q4}.",
            "Write the question number before each answer.", extra]

PAIR_NAMES = {1: "Real_Numbers_and_Polynomials", 2: "Linear_and_Quadratic_Equations", 3: "AP_and_Coordinate_Geometry",
              4: "Triangles_and_Circles", 5: "Trigonometry_and_its_Applications", 6: "Areas_and_Volumes",
              7: "Statistics_and_Probability"}
UNITS = [((1, 2, 3, 4), "Unit1_Ch01-04_Number_Systems_and_Algebra"),
         ((5, 6, 7), "Unit2_Ch05-07_AP_Triangles_Coordinate_Geometry"),
         ((8, 9, 10, 11), "Unit3_Ch08-11_Trigonometry_and_Circles"),
         ((12, 13, 14), "Unit4_Ch12-14_Mensuration_Statistics_Probability")]

def main(levels):
    os.makedirs(ROOT, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        log = []
        # ---- level 1: chapter tests (already authored) ----
        if "1" in levels:
            for ch in range(1, 15):
                m = importlib.import_module(f"content.ch{ch:02d}")
                nm = CHAPTERS[ch]; slug = f"Ch{ch:02d}_{nm.replace(' ', '_')}"
                d = f"{ROOT}/1_Chapter_Tests_40_Marks/{slug}"; os.makedirs(d, exist_ok=True)
                for s, data in m.SETS.items():
                    n, fs = fit(pg, lambda f: paper_html(ch, s, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                f"Mastermind Coaching Classes — Class 10 Maths · Ch {ch}: {nm} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                to_pdf(pg, key_html(ch, m.SETS), f"{d}/{slug}_Answer_Key.pdf", f"Mastermind Coaching Classes — Answer Key · Ch {ch}: {nm}")
        # ---- level 2: two-chapter tests ----
        if "2" in levels:
            for pn, m in PAIRS.items():
                c1, c2 = m.CHS
                slug = f"Ch{c1:02d}-{c2:02d}_{PAIR_NAMES[pn]}"
                d = f"{ROOT}/2_Two_Chapter_Tests_40_Marks/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for s, data in m.SETS.items():
                    data = shuffle_paper(data, f"pair{pn}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title="CLASS 10 — MATHEMATICS TWO-CHAPTER TEST", set=s, chs=m.CHS,
                                time="1 Hour 30 Minutes", marks=40, secs=S40,
                                instr=instr((10, 4, 4, 2), 17, data.get("note", "Draw neat figures wherever required.")))
                    n, fs = fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                f"Mastermind Coaching Classes — Class 10 Maths · Chapters {c1} & {c2} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    k = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), k, f"Answer Key · Chapters {c1} & {c2} · Set {s}"); keys.append(k)
                unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        # ---- level 3: unit tests (50 marks) ----
        if "3" in levels:
            S50 = S40
            for ui, (chs, slug) in enumerate(UNITS):
                d = f"{ROOT}/3_Unit_Tests_50_Marks/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for si, s in enumerate("ABC"):
                    rng = random.Random(f"unit{ui}{s}"); taken = set(); pref = ("chapter", "supp")
                    k = len(chs)
                    A, B, C, D = [], [], [], []
                    mcq_n = [3] * 4 if k == 4 else [4] * 3
                    b_n = ([2, 1, 1, 1] if k == 4 else [2, 2, 1]); b_n = b_n[si % k:] + b_n[:si % k]
                    c_plain = [1, 1, 1, 1] if k == 4 else [2, 1, 1]; c_plain = c_plain[si % k:] + c_plain[:si % k]
                    or_c = [chs[(si) % k], chs[(si + 2) % k]] if k == 4 else [chs[si % k], chs[(si + 1) % k]]
                    or_d = [chs[(si + 1) % k], chs[(si + 3) % k]] if k == 4 else [chs[(si + 2) % k], chs[(si + 1 + 2) % k]]
                    if or_d[0] == or_d[1]: or_d[1] = chs[(chs.index(or_d[0]) + 1) % k]
                    for c, n in zip(chs, mcq_n): A += pick(c, "A", n, pref, taken, rng)
                    for c, n in zip(chs, b_n): B += pick(c, "B", n, pref, taken, rng)
                    for c, n in zip(chs, c_plain): C += pick(c, "C", n, pref, taken, rng)
                    C += [orpair(c, "C", pref, taken, rng) for c in or_c]
                    D += [orpair(c, "D", pref, taken, rng) for c in sorted(or_d)]
                    data = shuffle_paper(dict(A=A, B=B, C=C, D=D), f"unit{ui}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title="CLASS 10 — MATHEMATICS UNIT TEST", set=s, chs=chs,
                                time="2 Hours", marks=50, secs=S50,
                                instr=instr((12, 5, 6, 2), 22, "Draw neat figures; use graph paper where a graph is asked."))
                    n, fs = fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                f"Mastermind Coaching Classes — Class 10 Maths · Unit Test (Ch {chs[0]}–{chs[-1]}) · Set {s}", 2, fmin=10.2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    kf = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), kf, f"Answer Key · Unit Test Ch {chs[0]}–{chs[-1]} · Set {s}"); keys.append(kf)
                unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        # ---- level 4: full syllabus (80 marks, RBSE blueprint) ----
        if "4" in levels:
            d = f"{ROOT}/4_Full_Syllabus_Papers_80_Marks"; kd = f"{d}/Answer_Keys"; os.makedirs(kd, exist_ok=True)
            MCQ = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 10, 11, 11, 12, 13, 13, 14]
            BQ = [1, 2, 4, 6, 7, 8, 9, 10]
            CPLAIN = [13, 5, 10, 11, 14]
            for i in range(1, 11):
                rng = random.Random(f"full{i}"); taken = set(); pref = ("pair", "supp")
                A = []
                for c in sorted(set(MCQ)): A += pick(c, "A", MCQ.count(c), pref, taken, rng)
                B = [pick(c, "B", 1, pref, taken, rng)[0] for c in BQ]
                C = pick(3, "G", 1, pref, taken, rng) + [pick(c, "C", 1, pref, taken, rng)[0] for c in CPLAIN]
                C += [orpair(9, "C", pref, taken, rng), orpair(13, "C", pref, taken, rng)]
                D = [orpair(c, "D", pref, taken, rng) for c in (7, 8, 12, 13)]
                data = shuffle_paper(dict(A=A, B=B, C=C, D=D), f"full{i}")
                s = f"{i:02d}"
                meta = dict(doc=f"Full Syllabus Set {s}", title="CLASS 10 — MATHEMATICS FULL SYLLABUS PAPER", set=s, chs=tuple(range(1, 15)),
                            time="3 Hours 15 Minutes", marks=80,
                            secs=[("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
                                  ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 20–30 words each."),
                                  ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 40–60 words each. Solve Q. 29 on graph paper."),
                                  ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")],
                            instr=instr((20, 8, 8, 4), 35, "Solve Q. 29 on graph paper. Draw neat figures."))
                n, fs = fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/Full_Syllabus_Set_{s}.pdf",
                            f"Mastermind Coaching Classes — Class 10 Maths · Full Syllabus Paper · Set {s}", 4)
                log.append((f"Full_Syllabus_Set_{s}", n, fs))
                to_pdf(pg, generic_key(meta, data), f"{kd}/Full_Syllabus_Set_{s}_Answer_Key.pdf", f"Answer Key · Full Syllabus Paper · Set {s}")
        br.close()
    for l in log: print(*l)
    from collections import Counter
    u = Counter(b["used"] for b in BANK)
    print("bank usage histogram:", dict(sorted(u.items())), "bank size", len(BANK))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1234")
