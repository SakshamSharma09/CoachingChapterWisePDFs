"""Science collection builder (reuses the Maths machinery)."""
import os, sys, random, importlib
from collections import Counter
from playwright.sync_api import sync_playwright
import lib
from lib import OR, generic_paper, generic_key, to_pdf

SCI = {1: "Chemical Reactions and Equations", 2: "Acids, Bases and Salts", 3: "Metals and Non-metals",
       4: "Carbon and its Compounds", 5: "Life Processes", 6: "Control and Coordination",
       7: "How do Organisms Reproduce?", 8: "Heredity", 9: "Light – Reflection and Refraction",
       10: "The Human Eye and the Colourful World", 11: "Electricity",
       12: "Magnetic Effects of Electric Current", 13: "Our Environment"}
lib.CHAPTERS.clear(); lib.CHAPTERS.update(SCI); lib.SUBJECT[0] = "Science"

import compose as M   # maths composer: shuffle, fit, pick, unite …  (its bank is maths; we rebuild ours)
M.BANK.clear(); M.TAKEN_TXT.clear()
BANK = M.BANK
ROOT = "/home/claude/papers/Science_Class10_Paper_Generated"
SLUG = {1: "Chemical_Reactions_and_Equations", 2: "Acids_Bases_and_Salts", 3: "Metals_and_Non-metals",
        4: "Carbon_and_its_Compounds", 5: "Life_Processes", 6: "Control_and_Coordination",
        7: "How_do_Organisms_Reproduce", 8: "Heredity", 9: "Light_Reflection_and_Refraction",
        10: "Human_Eye_and_Colourful_World", 11: "Electricity", 12: "Magnetic_Effects_of_Current",
        13: "Our_Environment"}
PAIRS = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]
PAIR_NAMES = {(1, 2): "Chemical_Reactions_Acids_Bases_Salts", (3, 4): "Metals_Non-metals_and_Carbon_Compounds",
              (5, 6): "Life_Processes_Control_Coordination", (7, 8): "Reproduction_and_Heredity",
              (9, 10): "Light_and_Human_Eye", (11, 12): "Electricity_and_Magnetic_Effects"}
UNITS = [((1, 2, 3, 4), "Unit1_Ch01-04_Chemical_Substances"),
         ((5, 6, 7, 8, 13), "Unit2_Ch05-08_and_13_World_of_Living_and_Environment"),
         ((9, 10, 11, 12), "Unit3_Ch09-12_Light_Electricity_Magnetism")]

MODS = {c: importlib.import_module(f"sci.s{c:02d}") for c in range(1, 14) if os.path.exists(f"sci/s{c:02d}.py")}

def pair_sets(c1, c2):
    m1, m2 = MODS[c1].POOL, MODS[c2].POOL
    out = {}
    for k, s in enumerate("ABCD"):
        out[s] = dict(A=m1["A"][5*k:5*k+5] + m2["A"][5*k:5*k+5], B=m1["B"][2*k:2*k+2] + m2["B"][2*k:2*k+2],
                      C=[m1["C"][3*k], m2["C"][3*k], OR(m1["C"][3*k+1], m1["C"][3*k+2]), OR(m2["C"][3*k+1], m2["C"][3*k+2])],
                      D=[OR(m1["D"][2*k], m1["D"][2*k+1]), OR(m2["D"][2*k], m2["D"][2*k+1])])
    return out

def build_bank():
    for c, m in MODS.items():
        for s, d in m.SETS.items():
            for lvl in "ABCD":
                for it in d[lvl]:
                    for q in ([it["a"], it["b"]] if it["kind"] == "or" else [it]): M.add(q, c, lvl, "chapter")
        for lvl in "ABCD":
            for q in m.POOL[lvl]: M.add(q, c, lvl, "pair")
    try:
        sup = importlib.import_module("sci.supp")
        for (c, lvl), lst in sup.ITEMS.items():
            for q in lst: M.add(q, c, lvl, "supp")
    except ModuleNotFoundError:
        pass

S40 = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
       ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 10–15 words each."),
       ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 30–40 words each."),
       ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")]
NOTE = "Draw neat, labelled diagrams wherever required."

def main(levels):
    os.makedirs(ROOT, exist_ok=True)
    build_bank()
    log = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        if "1" in levels:
            for c, m in MODS.items():
                slug = f"Ch{c:02d}_{SLUG[c]}"; d = f"{ROOT}/1_Chapter_Tests_40_Marks/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for s, data in m.SETS.items():
                    data = M.shuffle_paper(data, f"sci{c}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title="CLASS 10 — SCIENCE CHAPTER TEST", set=s, chs=(c,),
                                time="1 Hour 30 Minutes", marks=40, secs=S40, instr=M.instr((10, 4, 4, 2), 17, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 10 Science · Ch {c}: {SCI[c]} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    k = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), k, f"Answer Key · Science Ch {c} · Set {s}"); keys.append(k)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "2" in levels:
            for (c1, c2) in PAIRS:
                if c1 not in MODS or c2 not in MODS: continue
                slug = f"Ch{c1:02d}-{c2:02d}_{PAIR_NAMES[(c1, c2)]}"; d = f"{ROOT}/2_Two_Chapter_Tests_40_Marks/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for s, data in pair_sets(c1, c2).items():
                    data = M.shuffle_paper(data, f"scipair{c1}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title="CLASS 10 — SCIENCE TWO-CHAPTER TEST", set=s, chs=(c1, c2),
                                time="1 Hour 30 Minutes", marks=40, secs=S40, instr=M.instr((10, 4, 4, 2), 17, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 10 Science · Chapters {c1} & {c2} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    k = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), k, f"Answer Key · Science Chapters {c1} & {c2} · Set {s}"); keys.append(k)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "3" in levels:
            for ui, (chs, slug) in enumerate(UNITS):
                d = f"{ROOT}/3_Unit_Tests_50_Marks/{slug}"; os.makedirs(d, exist_ok=True); keys = []
                for si, s in enumerate("ABC"):
                    rng = random.Random(f"sciunit{ui}{s}"); taken = set(); pref = ("chapter", "supp")
                    k = len(chs); order = list(chs[si % k:] + chs[:si % k])
                    cnt = lambda n, off: Counter(order[(i + off) % k] for i in range(n))
                    A = []; B = []; C = []
                    for c in chs: A += M.pick(c, "A", cnt(12, 0)[c], pref, taken, rng)
                    for c in chs:
                        if cnt(5, 1)[c]: B += M.pick(c, "B", cnt(5, 1)[c], pref, taken, rng)
                    for c in chs:
                        if cnt(4, 2)[c]: C += M.pick(c, "C", cnt(4, 2)[c], pref, taken, rng)
                    C += [M.orpair(order[(3 + j) % k], "C", pref, taken, rng) for j in range(2)]
                    D = [M.orpair(c, "D", pref, taken, rng) for c in sorted({order[1 % k], order[(k - 1) % k]})]
                    data = M.shuffle_paper(dict(A=A, B=B, C=C, D=D), f"sciunit{ui}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title="CLASS 10 — SCIENCE UNIT TEST", set=s, chs=chs,
                                time="2 Hours", marks=50, secs=S40, instr=M.instr((12, 5, 6, 2), 22, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 10 Science · Unit Test · Set {s}", 2, fmin=10.2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    kf = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), kf, f"Answer Key · Science Unit Test · Set {s}"); keys.append(kf)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "4" in levels:
            d = f"{ROOT}/4_Full_Syllabus_Papers_80_Marks"; kd = f"{d}/Answer_Keys"; os.makedirs(kd, exist_ok=True)
            MCQ = {1: 1, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1, 7: 2, 8: 2, 9: 1, 10: 1, 11: 2, 12: 1, 13: 2}
            BQ = [1, 2, 5, 6, 7, 8, 9, 12]
            CPLAIN = [1, 3, 6, 7, 10, 12]
            DQ = [9, 4, 11, 5]
            for i in range(1, 11):
                rng = random.Random(f"scifull{i}"); taken = set(); pref = ("pair", "supp")
                A = []
                for c, n in MCQ.items(): A += M.pick(c, "A", n, pref, taken, rng)
                B = [M.pick(c, "B", 1, pref, taken, rng)[0] for c in BQ]
                C = [M.pick(c, "C", 1, pref, taken, rng)[0] for c in CPLAIN] + [M.orpair(2, "C", pref, taken, rng), M.orpair(13, "C", pref, taken, rng)]
                D = [M.orpair(c, "D", pref, taken, rng) for c in DQ]
                data = M.shuffle_paper(dict(A=A, B=B, C=C, D=D), f"scifull{i}")
                s = f"{i:02d}"
                meta = dict(doc=f"Science Full Syllabus Set {s}", title="CLASS 10 — SCIENCE FULL SYLLABUS PAPER", set=s, chs=tuple(range(1, 14)),
                            time="3 Hours 15 Minutes", marks=80, secs=S40, instr=M.instr((20, 8, 8, 4), 35, NOTE))
                n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/Science_Full_Syllabus_Set_{s}.pdf",
                              f"Mastermind Coaching Classes — Class 10 Science · Full Syllabus Paper · Set {s}", 4)
                log.append((f"Science_Full_Syllabus_Set_{s}", n, fs))
                to_pdf(pg, generic_key(meta, data), f"{kd}/Science_Full_Syllabus_Set_{s}_Answer_Key.pdf", f"Answer Key · Science Full Syllabus · Set {s}")
        br.close()
    for l in log: print(*l)
    u = Counter(b["used"] for b in BANK); print("bank:", len(BANK), dict(sorted(u.items())))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1234")
