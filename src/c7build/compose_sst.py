"""Social Science collection builder (reuses the Maths/Science machinery)."""
import os, sys, random, importlib
from collections import Counter
from playwright.sync_api import sync_playwright
import lib
from lib import OR, generic_paper, generic_key, to_pdf

# id -> (subject, NCERT chapter number, name, slug)
H, G, P, E = "History", "Geography", "Political Science", "Economics"
INFO = {
 1: (H, 1, "The Rise of Nationalism in Europe", "Rise_of_Nationalism_in_Europe"),
 2: (H, 2, "Nationalism in India", "Nationalism_in_India"),
 3: (H, 3, "The Making of a Global World", "Making_of_a_Global_World"),
 4: (H, 4, "The Age of Industrialisation", "Age_of_Industrialisation"),
 5: (H, 5, "Print Culture and the Modern World", "Print_Culture_and_Modern_World"),
 6: (G, 1, "Resources and Development", "Resources_and_Development"),
 7: (G, 2, "Forest and Wildlife Resources", "Forest_and_Wildlife_Resources"),
 8: (G, 3, "Water Resources", "Water_Resources"),
 9: (G, 4, "Agriculture", "Agriculture"),
 10: (G, 5, "Minerals and Energy Resources", "Minerals_and_Energy_Resources"),
 11: (G, 6, "Manufacturing Industries", "Manufacturing_Industries"),
 12: (G, 7, "Lifelines of National Economy", "Lifelines_of_National_Economy"),
 13: (P, 1, "Power-sharing", "Power-sharing"),
 14: (P, 2, "Federalism", "Federalism"),
 15: (P, 3, "Gender, Religion and Caste", "Gender_Religion_and_Caste"),
 16: (P, 4, "Political Parties", "Political_Parties"),
 17: (P, 5, "Outcomes of Democracy", "Outcomes_of_Democracy"),
 18: (E, 1, "Development", "Development"),
 19: (E, 3, "Money and Credit", "Money_and_Credit"),
 20: (E, 4, "Globalisation and the Indian Economy", "Globalisation_and_Indian_Economy"),
 21: (E, 5, "Consumer Rights", "Consumer_Rights"),
}
SUBJ_DIR = {H: "1_History", G: "2_Geography", P: "3_Political_Science", E: "4_Economics"}
SUBJ_FILE = {H: "History", G: "Geography", P: "PolSci", E: "Economics"}
lib.CHAPTERS.clear(); lib.CHAPTERS.update({c: v[2] for c, v in INFO.items()}); lib.SUBJECT[0] = "Social Science"

def ch_label(chs):
    segs = []; cur = None
    for c in chs:
        s = INFO[c][0]
        if cur and cur[0] == s: cur[1].append(c)
        else:
            cur = [s, [c]]; segs.append(cur)
    if len(chs) == len(INFO):
        return "<b>Full Syllabus — History, Geography, Political Science &amp; Economics</b>"
    out = []
    for s, cs in segs:
        nums = [INFO[c][1] for c in cs]
        if len(cs) == 1:
            out.append(f"{s} Chapter {nums[0]}: <b>{INFO[cs[0]][2]}</b>")
        elif len(chs) <= 2:
            out.append(f"{s} Chapters {nums[0]} &amp; {nums[1]}: <b>{INFO[cs[0]][2]}, {INFO[cs[1]][2]}</b>")
        else:
            out.append(f"{s} Chapters {', '.join(map(str, nums))}: <b>{', '.join(INFO[c][2] for c in cs)}</b>")
    return " &nbsp;·&nbsp; ".join(out)
lib.ch_label = ch_label

import compose as M
M.BANK.clear(); M.TAKEN_TXT.clear()
BANK = M.BANK
_orig_shuffle = M.shuffle_mcq
def _shuffle_keep_ar(it, rng):
    if it["opts"][0].startswith("Both A and R"):   # Assertion–Reason keeps its standard option order
        import copy; return copy.deepcopy(it)
    return _orig_shuffle(it, rng)
M.shuffle_mcq = _shuffle_keep_ar
ROOT = "/home/claude/papers/SocialScience_Class10_Paper_Generated"

PAIRS = [(1, 2), (3, 4), (6, 7), (8, 9), (10, 11), (13, 14), (15, 16), (18, 19), (20, 21)]
PAIR_NAMES = {(1, 2): "Nationalism_in_Europe_and_India", (3, 4): "Global_World_and_Industrialisation",
              (6, 7): "Resources_and_Forest_Wildlife", (8, 9): "Water_Resources_and_Agriculture",
              (10, 11): "Minerals_Energy_and_Manufacturing", (13, 14): "Power-sharing_and_Federalism",
              (15, 16): "Gender_Religion_Caste_and_Political_Parties", (18, 19): "Development_and_Money_Credit",
              (20, 21): "Globalisation_and_Consumer_Rights"}
UNITS = [((1, 2, 3, 4, 5), "History_Unit_Ch1-5_India_and_the_Contemporary_World"),
         ((6, 7, 8, 9), "Geography_Unit_A_Ch1-4_Resources_Water_Agriculture"),
         ((10, 11, 12), "Geography_Unit_B_Ch5-7_Minerals_Industries_Lifelines"),
         ((13, 14, 15, 16, 17), "PolSci_Unit_Ch1-5_Democratic_Politics"),
         ((18, 19, 20, 21), "Economics_Unit_Ch1_3_4_5_Understanding_Economic_Development")]
UNIT_TITLE = {0: "HISTORY", 1: "GEOGRAPHY", 2: "GEOGRAPHY", 3: "POLITICAL SCIENCE", 4: "ECONOMICS"}

MODS = {c: importlib.import_module(f"sst.c{c:02d}") for c in INFO}

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

S40 = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
       ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 10–15 words each."),
       ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 30–40 words each."),
       ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")]
NOTE = "Answers must be written in the answer book in the order of the questions."

def lab(c): return f"{INFO[c][0]} Ch {INFO[c][1]}: {INFO[c][2]}"

def rot(lst, n, off):
    return [lst[(off + j) % len(lst)] for j in range(n)]

def main(levels):
    os.makedirs(ROOT, exist_ok=True)
    build_bank()
    log = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        if "1" in levels:
            for c, m in MODS.items():
                sj, no, nm, sl = INFO[c]
                slug = f"{SUBJ_FILE[sj]}_Ch{no:02d}_{sl}"; d = f"{ROOT}/1_Chapter_Tests_40_Marks/{SUBJ_DIR[sj]}/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for s, data in m.SETS.items():
                    data = M.shuffle_paper(data, f"sst{c}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title=f"CLASS 10 SOCIAL SCIENCE — {sj.upper()} CHAPTER TEST", set=s, chs=(c,),
                                time="1 Hour 30 Minutes", marks=40, secs=S40, instr=M.instr((10, 4, 4, 2), 17, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 10 Social Science · {lab(c)} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    k = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), k, f"Answer Key · {lab(c)} · Set {s}"); keys.append(k)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "2" in levels:
            for (c1, c2) in PAIRS:
                sj = INFO[c1][0]
                slug = f"{SUBJ_FILE[sj]}_Ch{INFO[c1][1]:02d}-{INFO[c2][1]:02d}_{PAIR_NAMES[(c1, c2)]}"
                d = f"{ROOT}/2_Two_Chapter_Tests_40_Marks/{SUBJ_DIR[sj]}/{slug}"; os.makedirs(d, exist_ok=True)
                keys = []
                for s, data in pair_sets(c1, c2).items():
                    data = M.shuffle_paper(data, f"sstpair{c1}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title=f"CLASS 10 SOCIAL SCIENCE — {sj.upper()} TWO-CHAPTER TEST", set=s, chs=(c1, c2),
                                time="1 Hour 30 Minutes", marks=40, secs=S40, instr=M.instr((10, 4, 4, 2), 17, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 10 Social Science · {sj} Chapters {INFO[c1][1]} & {INFO[c2][1]} · Set {s}", 2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    k = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), k, f"Answer Key · {sj} Chapters {INFO[c1][1]} & {INFO[c2][1]} · Set {s}"); keys.append(k)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "3" in levels:
            for ui, (chs, slug) in enumerate(UNITS):
                sj = INFO[chs[0]][0]
                d = f"{ROOT}/3_Unit_Tests_50_Marks/{slug}"; os.makedirs(d, exist_ok=True); keys = []
                for si, s in enumerate("ABC"):
                    rng = random.Random(f"sstunit{ui}{s}"); taken = set(); pref = ("chapter", "supp")
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
                    data = M.shuffle_paper(dict(A=A, B=B, C=C, D=D), f"sstunit{ui}{s}")
                    meta = dict(doc=f"{slug} Set {s}", title=f"CLASS 10 SOCIAL SCIENCE — {UNIT_TITLE[ui]} UNIT TEST", set=s, chs=chs,
                                time="2 Hours", marks=50, secs=S40, instr=M.instr((12, 5, 6, 2), 22, NOTE))
                    n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), f"{d}/{slug}_Set_{s}.pdf",
                                  f"Mastermind Coaching Classes — Class 10 Social Science · {sj} Unit Test · Set {s}", 2, fmin=10.2)
                    log.append((f"{slug}_Set_{s}", n, fs))
                    kf = f"{d}/_k{s}.pdf"; to_pdf(pg, generic_key(meta, data), kf, f"Answer Key · {sj} Unit Test · Set {s}"); keys.append(kf)
                M.unite(keys, f"{d}/{slug}_Answer_Key.pdf")
        if "4" in levels:
            d = f"{ROOT}/4_Full_Syllabus_Papers_80_Marks"; kd = f"{d}/Answer_Keys"; os.makedirs(kd, exist_ok=True)
            Hs, Gs, Ps, Es = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17], [18, 19, 20, 21]
            for i in range(1, 11):
                rng = random.Random(f"sstfull{i}"); taken = set(); pref = ("pair", "supp")
                A = []
                # 20 MCQ: History 5, Geography 6, Political Science 5, Economics 4
                gA = rot(Gs, 6, i % 7)
                for c in Hs + gA + Ps + Es: A += M.pick(c, "A", 1, pref, taken, rng)
                # 8 very short answers (2 each): 2 from every subject
                Bc = rot(Hs, 2, i) + rot(Gs, 2, 2 * i) + rot(Ps, 2, i + 1) + rot(Es, 2, i)
                B = [M.pick(c, "B", 1, pref, taken, rng)[0] for c in Bc]
                # 6 short answers + 2 with choice (3 each)
                Cc = [rot(Hs, 1, i + 2)[0], rot(Gs, 1, 3 * i)[0], rot(Gs, 1, 3 * i + 3)[0], rot(Ps, 1, i + 3)[0], rot(Ps, 1, i)[0], rot(Es, 1, i + 1)[0]]
                C = [M.pick(c, "C", 1, pref, taken, rng)[0] for c in Cc]
                C += [M.orpair(rot(Hs, 1, i + 4)[0], "C", pref, taken, rng), M.orpair(rot(Es, 1, i + 3)[0], "C", pref, taken, rng)]
                # 4 long answers with choice (5 each): one per subject
                Dc = [rot(Hs, 1, i + 1)[0], rot(Gs, 1, i + 4)[0], rot(Ps, 1, i + 2)[0], rot(Es, 1, i + 2)[0]]
                D = [M.orpair(c, "D", pref, taken, rng) for c in Dc]
                data = M.shuffle_paper(dict(A=A, B=B, C=C, D=D), f"sstfull{i}")
                s = f"{i:02d}"
                meta = dict(doc=f"Social Science Full Syllabus Set {s}", title="CLASS 10 — SOCIAL SCIENCE FULL SYLLABUS PAPER", set=s, chs=tuple(INFO),
                            time="3 Hours 15 Minutes", marks=80, secs=S40, instr=M.instr((20, 8, 8, 4), 35, NOTE))
                outp = f"{d}/SocialScience_Full_Syllabus_Set_{s}.pdf"; ft = f"Mastermind Coaching Classes — Class 10 Social Science · Full Syllabus Paper · Set {s}"
                n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), outp, ft, 3, fmin=10.8)
                if n > 3: n, fs = M.fit(pg, lambda f: generic_paper(meta, data, f), outp, ft, 4)
                log.append((f"SocialScience_Full_Syllabus_Set_{s}", n, fs))
                to_pdf(pg, generic_key(meta, data), f"{kd}/SocialScience_Full_Syllabus_Set_{s}_Answer_Key.pdf", f"Answer Key · Social Science Full Syllabus · Set {s}")
        br.close()
    for l in log: print(*l)
    u = Counter(b["used"] for b in BANK); print("bank:", len(BANK), dict(sorted(u.items())))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1234")
