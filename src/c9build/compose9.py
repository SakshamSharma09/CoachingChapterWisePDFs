"""Generic Class 9 builder for chapter-wise subjects (Maths, Science, ...)."""
import os, sys, random, importlib
from collections import Counter
from playwright.sync_api import sync_playwright
import lib
from lib import OR, generic_paper, generic_key, to_pdf
import compose_core as M

def secs(bw, cw, dw, extra_c=""):
    return [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
            ("B", "SECTION — B (Very Short Answer Type)", 2, f"Answer in about {bw} words each."),
            ("C", "SECTION — C (Short Answer Type)", 3, f"Answer in about {cw} words each.{extra_c}"),
            ("D", "SECTION — D (Long Answer Type)", 5, f"Answer in about {dw} words each.")]

def pair_sets(MODS, c1, c2):
    m1, m2 = MODS[c1].POOL, MODS[c2].POOL
    out = {}
    for k, s in enumerate("ABCD"):
        out[s] = dict(A=m1["A"][5*k:5*k+5] + m2["A"][5*k:5*k+5], B=m1["B"][2*k:2*k+2] + m2["B"][2*k:2*k+2],
                      C=[m1["C"][3*k], m2["C"][3*k], OR(m1["C"][3*k+1], m1["C"][3*k+2]), OR(m2["C"][3*k+1], m2["C"][3*k+2])],
                      D=[OR(m1["D"][2*k], m1["D"][2*k+1]), OR(m2["D"][2*k], m2["D"][2*k+1])])
    return out

def run(cfg, levels):
    S = cfg["subject"]; SC = S.upper(); CH = cfg["chapters"]
    lib.CHAPTERS.clear(); lib.CHAPTERS.update(CH); lib.SUBJECT[0] = S
    M.BANK.clear(); M.TAKEN_TXT.clear()
    MODS = {c: importlib.import_module(cfg["modfmt"] % c) for c in CH}
    for c, m in MODS.items():
        for s, d in m.SETS.items():
            for lvl in "ABCD":
                for it in d[lvl]:
                    for q in ([it["a"], it["b"]] if it["kind"] == "or" else [it]): M.add(q, c, lvl, "chapter")
        for lvl in "ABCD":
            for q in m.POOL[lvl]: M.add(q, c, lvl, "pair")
    if cfg.get("supp"):
        sup = importlib.import_module(cfg["supp"])
        for (c, lvl), lst in sup.ITEMS.items():
            for q in lst: M.add(q, c, lvl, "supp")
    ROOT = cfg["root"]; os.makedirs(ROOT, exist_ok=True)
    S40 = secs(*cfg["words"]); NOTE = cfg["note"]
    log = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        if "1" in levels:
            for c, m in MODS.items():
                slug = f"Ch{c:02d}_{cfg['slug'][c]}"; d = f"{ROOT}/1_Chapter_Tests_40_Marks/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for s, data in m.SETS.items():
                    data = M.shuffle_paper(data, f"{S}{c}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title=f"CLASS 9 — {SC} CHAPTER TEST", set=s, chs=(c,),
                                time="1 Hour 30 Minutes", marks=40, secs=S40, instr=M.instr((10, 4, 4, 2), 17, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 9 {S} · Ch {c}: {CH[c]} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    k = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), k, f"Answer Key · {S} Ch {c} · Set {s}"); keys.append(k)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "2" in levels:
            for (c1, c2) in cfg["pairs"]:
                slug = f"Ch{c1:02d}-{c2:02d}_{cfg['pair_names'][(c1, c2)]}"; d = f"{ROOT}/2_Two_Chapter_Tests_40_Marks/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for s, data in pair_sets(MODS, c1, c2).items():
                    data = M.shuffle_paper(data, f"{S}pair{c1}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title=f"CLASS 9 — {SC} TWO-CHAPTER TEST", set=s, chs=(c1, c2),
                                time="1 Hour 30 Minutes", marks=40, secs=S40, instr=M.instr((10, 4, 4, 2), 17, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 9 {S} · Chapters {c1} & {c2} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    k = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), k, f"Answer Key · {S} Chapters {c1} & {c2} · Set {s}"); keys.append(k)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "3" in levels:
            for ui, (chs, slug) in enumerate(cfg["units"]):
                d = f"{ROOT}/3_Unit_Tests_50_Marks/{slug}"; os.makedirs(d, exist_ok=True); keys = []
                for si, s in enumerate("ABC"):
                    rng = random.Random(f"{S}unit{ui}{s}"); taken = set(); pref = ("chapter", "supp")
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
                    data = M.shuffle_paper(dict(A=A, B=B, C=C, D=D), f"{S}unit{ui}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title=f"CLASS 9 — {SC} UNIT TEST", set=s, chs=chs,
                                time="2 Hours", marks=50, secs=S40, instr=M.instr((12, 5, 6, 2), 22, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 9 {S} · Unit Test · Set {s}", 2, fmin=10.2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    kf = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), kf, f"Answer Key · {S} Unit Test · Set {s}"); keys.append(kf)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "4" in levels:
            d = f"{ROOT}/4_Full_Syllabus_Papers_80_Marks"; kd = f"{d}/Answer_Keys"; os.makedirs(kd, exist_ok=True)
            F = cfg["full"]
            for i in range(1, 11):
                rng = random.Random(f"{S}full{i}"); taken = set(); pref = ("pair", "supp")
                if F.get("rot"):
                    chs_ = sorted(CH); P2 = [c for c in chs_ if c >= F["rot"]]
                    mc = {c: 1 for c in chs_}
                    ex = 20 - len(chs_); e2 = min(4, ex)
                    for c in rng.sample(P2, e2) + rng.sample(chs_, ex - e2): mc[c] += 1
                    F2 = dict(MCQ=mc, BQ=sorted(rng.sample(P2, 4) + rng.sample([c for c in chs_ if c < F["rot"]], 4)))
                    rest = [c for c in chs_]; rng.shuffle(rest)
                    cs = rest[:8]; F2["CPLAIN"] = cs[:6]; F2["CORS"] = cs[6:]
                    F2["DQ"] = rng.sample(P2, 2) + rng.sample([c for c in chs_ if c < F["rot"]], 2)
                else: F2 = F
                A = []
                for c, n in F2["MCQ"].items(): A += M.pick(c, "A", n, pref, taken, rng)
                B = [M.pick(c, "B", 1, pref, taken, rng)[0] for c in F2["BQ"]]
                C = [M.pick(c, "C", 1, pref, taken, rng)[0] for c in F2["CPLAIN"]] + [M.orpair(c, "C", pref, taken, rng) for c in F2["CORS"]]
                D = [M.orpair(c, "D", pref, taken, rng) for c in F2["DQ"]]
                assert (len(A), len(B), len(C), len(D)) == (20, 8, 8, 4), (len(A), len(B), len(C), len(D))
                data = M.shuffle_paper(dict(A=A, B=B, C=C, D=D), f"{S}full{i}")
                s = f"{i:02d}"
                meta = dict(doc=f"{S} Full Syllabus Set {s}", title=f"CLASS 9 — {SC} FULL SYLLABUS PAPER", set=s, chs=tuple(CH),
                            time="3 Hours 15 Minutes", marks=80, secs=S40, instr=M.instr((20, 8, 8, 4), 35, NOTE))
                n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{S}_Full_Syllabus_Set_{s}.pdf",
                              f"Mastermind Coaching Classes — Class 9 {S} · Full Syllabus Paper · Set {s}", 4)
                log.append((f"{S}_Full_Syllabus_Set_{s}", n, fs))
                to_pdf(pg, generic_key(meta, data), f"{kd}/{S}_Full_Syllabus_Set_{s}_Answer_Key.pdf", f"Answer Key · {S} Full Syllabus · Set {s}")
        br.close()
    for l in log: print(*l)
    u = Counter(b["used"] for b in M.BANK); print("bank:", len(M.BANK), dict(sorted(u.items())))
