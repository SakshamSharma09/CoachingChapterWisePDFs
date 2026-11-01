"""English (Class 9) collection builder — reuses the Mastermind template (eng_lib) and fit/unite helpers."""
import os, sys, copy, random, importlib
from collections import Counter
from playwright.sync_api import sync_playwright
import compose_core as M
from lib import to_pdf
from eng9_lib import eng_paper, eng_key, OR

ROOT = "/home/claude/out9/English_Class9_Paper_Generated"
EN = [f"e{i:02d}" for i in range(1, 9)]
MOD = {n: importlib.import_module(f"en9.{n}") for n in EN}
slug = lambda s: "".join(ch if ch.isalnum() else "_" for ch in s.replace("'", "").replace("!", "")).strip("_").replace("__", "_")

def load_sets(prefix, names):
    out = {}
    for n in names:
        m = importlib.import_module(f"en9.{n}")
        for k, v in m.SETS.items(): out[k] = v
    return out
READ = load_sets("reading", ["r9a", "r9b", "r9c"])
WRIT = load_sets("writing", ["w9a", "w9b"])
assert len(READ) == 10 and len(WRIT) == 10

# ───────── shuffling ─────────
def shuf_sub(s, rng):
    s = copy.deepcopy(s)
    if s.get("opts") and not any(M.FIXED.search(o) for o in s["opts"]):
        correct = s["opts"]["abcd".index(s["ans"])]
        rng.shuffle(s["opts"]); s["ans"] = "abcd"[s["opts"].index(correct)]
    return s

def shuffle_data(data, seed):
    rng = random.Random(seed); out = {}
    for k, items in data.items():
        new = []
        for it in items:
            if it["kind"] == "mcq": new.append(M.shuffle_mcq(it, rng))
            elif it["kind"] == "pas":
                it = copy.deepcopy(it); it["subs"] = [shuf_sub(s, rng) for s in it["subs"]]; new.append(it)
            else: new.append(it)
        out[k] = new
    return out

# ───────── pickers ─────────
USE = Counter()
def nxt(name, kind, n=1):
    pool = getattr(MOD[name], kind); res = []
    for _ in range(n):
        res.append(copy.deepcopy(pool[USE[(name, kind)] % len(pool)])); USE[(name, kind)] += 1
    return res
def one(name, kind): return nxt(name, kind)[0]
def rot(lst, n, off): return [lst[(off + j) % len(lst)] for j in range(n)]

# ───────── section templates ─────────
def sections_lit(total_lbl=True):
    return [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
            ("B", "SECTION — B (Extract-based Questions)", 4, "Read the extract / situation and answer all the questions that follow."),
            ("C", "SECTION — C (Short Answer Type)", 2, "Answer in about 30–40 words each."),
            ("D", "SECTION — D (Long Answer Type)", 3, "Answer in about 80–100 words each.")]
def instr_list(parts, choice=None):
    base = ["All questions are compulsory."] + parts
    if choice: base.append(choice)
    return base + ["Write the question number before each answer.", "Answers must be written in the answer book in the order of the questions."]

def run(pg, meta, data, outdir, base, foot, target, fmin=9.4):
    path = f"{outdir}/{base}.pdf"
    n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), path, foot, target, fmin=fmin)
    kf = f"{outdir}/_k{meta['set']}.pdf"
    to_pdf(pg, eng_key(meta, data), kf, "Answer Key · " + foot.split("—", 1)[-1].strip())
    return n, fs, kf

def lit_data(mc, ext, sa, la_pairs, la_single=()):
    return dict(A=mc, B=ext, C=sa, D=list(la_single) + [OR(a, b) for a, b in la_pairs])

def main(levels):
    os.makedirs(ROOT, exist_ok=True); log = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        # ── 1. chapter tests ──
        if "1" in levels:
            groups = [("1_Unit_Wise_Chapter_Tests_20_Marks", "UNIT-WISE", EN, "Unit", "EN")]
            for gdir, gname, names, gfile, code in groups:
                for i, nm in enumerate(names, 1):
                    m = MOD[nm]; poem = False
                    sl = f"{gfile}_{i:02d}_{slug(m.NAME)}"
                    d = f"{ROOT}/{gdir}/{sl}"; os.makedirs(d, exist_ok=True); keys = []
                    for s, S_ in enumerate("AB"):
                        if poem:
                            data = dict(A=m.MCQ[4*s:4*s+4], B=[m.EXT[s]], C=[m.SA[s]]); marks = 10; tm = "25 Minutes"
                            secs = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
                                    ("B", "SECTION — B (Extract-based Question)", 4, "Read the extract and answer all the questions that follow."),
                                    ("C", "SECTION — C (Short Answer Type)", 2, "Answer in about 30–40 words.")]
                            ins = instr_list(["Q. 1–4 are Objective Type (1 mark each).", "Q. 5 is an Extract-based question (4 marks).", "Q. 6 is a Short Answer Type question (2 marks)."])
                            target = 1
                        else:
                            data = lit_data(m.MCQ[6*s-2*s:6*s-2*s+4] + m.MCQ[12+2*s:14+2*s], [m.EXT[0 if s == 0 else 2]], m.SA[2*s:2*s+2], [(m.LA[4*s], m.LA[4*s+1]), (m.LA[4*s+2], m.LA[4*s+3])])
                            marks = 20; tm = "45 Minutes"; secs = sections_lit()
                            ins = instr_list(["Q. 1–6 are Objective Type (1 mark each).", "Q. 7 is an Extract-based question (4 marks).", "Q. 8–9 are Short Answer Type (2 marks each).", "Q. 10–11 are Long Answer Type (3 marks each)."], "Internal choice is given in Q. 10 and 11.")
                            target = 2
                        data = shuffle_data(data, f"engch{nm}{S_}")
                        if not poem: pass
                        meta = dict(doc=f"{sl} Set {S_}", title=f"CLASS 9 ENGLISH — {gname} CHAPTER TEST", set=S_, time=tm, marks=marks, secs=secs, instr=ins,
                                    label=f"Unit {i}: <b>{m.NAME}</b> &nbsp;(Kaveri — Prose and Poetry)")
                        n, fs, kf = run(pg, meta, data, d, f"{sl}_Set_{S_}", f"Mastermind Coaching Classes — Class 9 English · {m.NAME} · Set {S_}", target)
                        log.append((f"{sl}_Set_{S_}", n, fs)); keys.append(kf)
                    M.unite(keys, f"{d}/{sl}_Answer_Key.pdf")
        # ── 2. unit tests ──
        if "2" in levels:
            units = [(EN[:4], "Unit_1_Ch01-04", "UNITS 1–4", "Kaveri — Units 1 to 4"),
                     (EN[4:], "Unit_2_Ch05-08", "UNITS 5–8", "Kaveri — Units 5 to 8")]
            for ui, (names, sl, ttl, lbl) in enumerate(units):
                d = f"{ROOT}/2_Unit_Tests_30_Marks/{sl}"; os.makedirs(d, exist_ok=True); keys = []; n_ = len(names)
                for k, S_ in enumerate("ABC"):
                    A_ = [];
                    for j in range(8): A_.append(one(names[(j + 3 * k) % n_], "MCQ"))
                    B_ = [one(names[(2 * k + 1) % n_], "EXT")]
                    C_ = [one(names[(k + 4 + 2 * j) % n_], "SA") for j in range(3)]
                    D_ = [one(names[(k + 1) % n_], "LA"), one(names[(k + 5) % n_], "LA")]
                    pairs = [(one(names[(k + 2) % n_], "LA"), one(names[(k + 7) % n_], "LA")), (one(names[(k + 3) % n_], "LA"), one(names[(k + 8) % n_], "LA"))]
                    data = shuffle_data(lit_data(A_, B_, C_, pairs, D_), f"engunit{ui}{S_}")
                    secs = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option."), ("B", "SECTION — B (Extract-based Question)", 4, "Read the extract and answer all the questions that follow."),
                            ("C", "SECTION — C (Short Answer Type)", 2, "Answer in about 30–40 words each."), ("D", "SECTION — D (Long Answer Type)", 3, "Answer in about 80–100 words each.")]
                    ins = instr_list(["Q. 1–8 are Objective Type (1 mark each).", "Q. 9 is an Extract-based question (4 marks).", "Q. 10–12 are Short Answer Type (2 marks each).", "Q. 13–16 are Long Answer Type (3 marks each)."], "Internal choice is given in Q. 15 and 16.")
                    meta = dict(doc=f"{sl} Set {S_}", title=f"CLASS 9 ENGLISH — {ttl} UNIT TEST", set=S_, time="1 Hour 15 Minutes", marks=30, secs=secs, instr=ins, label=f"<b>{lbl}</b>")
                    n, fs, kf = run(pg, meta, data, d, f"{sl}_Set_{S_}", f"Mastermind Coaching Classes — Class 9 English · {lbl} · Set {S_}", 2)
                    log.append((f"{sl}_Set_{S_}", n, fs)); keys.append(kf)
                M.unite(keys, f"{d}/{sl}_Answer_Key.pdf")
        # ── 3. skill papers ──
        if "3" in levels:
            d = f"{ROOT}/3_Skill_Papers_20_Marks"; os.makedirs(f"{d}/Reading_Papers/Answer_Keys", exist_ok=True); os.makedirs(f"{d}/Writing_and_Grammar_Papers/Answer_Keys", exist_ok=True)
            for i in range(1, 11):
                s = f"{i:02d}"
                data = shuffle_data(dict(A=[READ[i]["P1"]], B=[READ[i]["P2"]]), f"engread{i}")
                secs = [("A", "SECTION — A (Reading Comprehension: Discursive Passage)", 10, "Read the passage and answer the questions."), ("B", "SECTION — B (Reading Comprehension: Case-based / Data Passage)", 10, "Read the text and answer the questions.")]
                meta = dict(doc=f"English Reading Paper Set {s}", title="CLASS 9 ENGLISH — READING SKILL PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                            instr=instr_list(["Section A has one passage with 10 questions (1 mark each).", "Section B has one case-based passage with 10 questions (1 mark each)."]), label="<b>Reading Comprehension</b>")
                rd = f"{d}/Reading_Papers"; path = f"{rd}/English_Reading_Paper_Set_{s}.pdf"
                n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), path, f"Mastermind Coaching Classes — Class 9 English · Reading Paper · Set {s}", 3)
                to_pdf(pg, eng_key(meta, data), f"{rd}/Answer_Keys/English_Reading_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · English Reading Paper · Set {s}")
                log.append((f"Reading_{s}", n, fs))
                W = WRIT[i]
                data = dict(A=W["W"], B=W["G"])
                secs = [("A", "SECTION — A (Writing Skills)", 4, "Attempt all the questions; internal choice is given in each."), ("B", "SECTION — B (Grammar)", 1, "Attempt all the questions.")]
                meta = dict(doc=f"English Writing and Grammar Paper Set {s}", title="CLASS 9 ENGLISH — WRITING &amp; GRAMMAR PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                            instr=instr_list(["Section A: Q. 1 Notice (3 marks), Q. 2 Letter (5 marks), Q. 3 Paragraph (4 marks).", "Section B: Q. 4–11 Grammar (1 mark each)."], "Internal choice is given in Q. 1, 2 and 3."), label="<b>Writing Skills &amp; Grammar</b>")
                wd = f"{d}/Writing_and_Grammar_Papers"
                n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{wd}/English_Writing_Grammar_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 9 English · Writing & Grammar · Set {s}", 2)
                to_pdf(pg, eng_key(meta, data), f"{wd}/Answer_Keys/English_Writing_Grammar_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · English Writing & Grammar · Set {s}")
                log.append((f"WritingGrammar_{s}", n, fs))
        # ── 4. full papers ──
        if "4" in levels:
            d = f"{ROOT}/4_Full_Syllabus_Papers_80_Marks"; kd = f"{d}/Answer_Keys"; os.makedirs(kd, exist_ok=True)
            for i in range(1, 11):
                s = f"{i:02d}"; W = WRIT[(i + 3) % 10 + 1]
                A_ = [READ[i]["P1"], READ[i]["P2"]]
                lm = [one(n, "MCQ") for n in rot(EN, 8, i)]
                le = [one(rot(EN, 1, i + 2)[0], "EXT"), one(rot(EN, 1, i + 5)[0], "EXT"), one(rot(EN, 1, i + 7)[0], "EXT")]
                ls = [one(rot(EN, 1, i + 1)[0], "SA"), one(rot(EN, 1, i + 3)[0], "SA"), one(rot(EN, 1, i + 4)[0], "SA"), one(rot(EN, 1, i + 6)[0], "SA")]
                ll = [OR(one(rot(EN, 1, i + j)[0], "LA"), one(rot(EN, 1, i + j + 4)[0], "LA")) for j in range(4)]
                data = shuffle_data(dict(R=A_, W=W["W"], G=W["G"], L1=lm, L2=le, L3=ls, L4=ll), f"engfull{i}")
                secs = [("R", "SECTION — A (Reading: 20 Marks)", 10, "Read the passages and answer the questions that follow."),
                        ("W", "SECTION — B (Writing Skills: 12 Marks)", 4, "Internal choice is given in each question."),
                        ("G", "SECTION — C (Grammar: 8 Marks)", 1, "Attempt all the questions."),
                        ("L1", "SECTION — D (Literature: Objective Type)", 1, "Choose the correct option and write it in your answer book."),
                        ("L2", "SECTION — E (Literature: Extract-based Questions)", 4, "Read the extracts and answer the questions that follow."),
                        ("L3", "SECTION — F (Literature: Short Answer Type)", 2, "Answer in about 30–40 words each."),
                        ("L4", "SECTION — G (Literature: Long Answer Type)", 3, "Answer in about 80–100 words each.")]
                ins = ["All questions are compulsory.", "Section A (Reading, 20 marks): Q. 1–2, passages with 10 sub-questions each (1 mark each).", "Section B (Writing, 12 marks): Q. 3 Notice (3), Q. 4 Letter (5), Q. 5 Paragraph (4).",
                       "Section C (Grammar, 8 marks): Q. 6–13 (1 mark each).", "Section D–G (Literature, 40 marks): Q. 14–21 objective (1 mark each), Q. 22–24 extract-based (4 marks each), Q. 25–28 short answer (2 marks each), Q. 29–32 long answer (3 marks each).",
                       "Internal choice is given in Q. 3, 4, 5 and Q. 29 to 32.", "Write the question number before each answer."]
                meta = dict(doc=f"English Full Syllabus Set {s}", title="CLASS 9 — ENGLISH FULL SYLLABUS PAPER", set=s, time="3 Hours 15 Minutes", marks=80, secs=secs, instr=ins,
                            label="<b>Reading · Writing &amp; Grammar · Literature (Kaveri: Prose and Poetry)</b>")
                outp = f"{d}/English_Full_Syllabus_Set_{s}.pdf"; ft = f"Mastermind Coaching Classes — Class 9 English · Full Syllabus Paper · Set {s}"
                n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), outp, ft, 4, fmin=9.8)
                to_pdf(pg, eng_key(meta, data), f"{kd}/English_Full_Syllabus_Set_{s}_Answer_Key.pdf", f"Answer Key · English Full Syllabus · Set {s}")
                log.append((f"English_Full_{s}", n, fs))
        br.close()
    for l in log: print(*l)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1234")
