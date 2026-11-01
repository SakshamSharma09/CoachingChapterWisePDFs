import os, sys, copy, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from playwright.sync_api import sync_playwright
import compose_core as M
from lib import to_pdf
from eng_lib import eng_paper, eng_key, OR, item_marks
from eng import reading, reading_b, reading_c, writing_a, writing_b, x10_ext as X, w10n_a, w10n_b
ROOT = "/home/claude/rw/out/Class10/English_Class10_Reading_Writing"
def shuf_sub(s, rng):
    s = copy.deepcopy(s)
    if s.get("opts") and not any(M.FIXED.search(o) for o in s["opts"]):
        correct = s["opts"]["abcd".index(s["ans"])]; rng.shuffle(s["opts"]); s["ans"] = "abcd"[s["opts"].index(correct)]
    return s
def shuffle_data(data, seed):
    rng = random.Random(seed); out = {}
    for k, items in data.items():
        new = []
        for it in items:
            it = copy.deepcopy(it); it["subs"] = [shuf_sub(s, rng) for s in it["subs"]]; new.append(it)
        out[k] = new
    return out
def instr_list(parts, choice=None):
    base = ["All questions are compulsory."] + parts
    if choice: base.append(choice)
    return base + ["Write the question number before each answer."]
READ = {}
for m in (reading, reading_b, reading_c): READ.update(m.SETS)
for k in READ:
    p1 = copy.deepcopy(READ[k]["P1"]); p2 = copy.deepcopy(READ[k]["P2"])
    paras = [x.strip() + "</p>" for x in p1["text"].split("</p>") if x.strip()]
    ext = [x.strip() + "</p>" for x in X.P1X[k].split("</p>") if x.strip()]
    p1["text"] = "".join(paras[:2] + ext + paras[2:])
    p2["text"] = X.P2PRE[k] + p2["text"] + X.P2POST[k]
    for s in p2["subs"]: s["q"] = s["q"].replace("in the first sentence", "in the passage")
    READ[k] = dict(P1=p1, P2=p2)
WRIT = {}
for m in (writing_a, writing_b): WRIT.update(m.SETS)
NEWB = {**w10n_a.NEWB, **w10n_b.NEWB}; ANA = {**w10n_a.ANA, **w10n_b.ANA}; GN = {**w10n_a.G_NEW, **w10n_b.G_NEW}
def fixbr(o):
    if isinstance(o, dict):
        for kk, v in list(o.items()):
            if isinstance(v, str) and kk == "ans": o[kk] = v.replace("\n", "<br>")
            elif not isinstance(v, str): fixbr(v)
    elif isinstance(o, list):
        for x in o: fixbr(x)
W2 = {}
for i in range(1, 11):
    W2[i] = dict(W=[OR(WRIT[i]["W"][1]["a"], NEWB[i]), OR(*ANA[i])], G=list(WRIT[i]["G"]) + GN[i])
    assert sum(item_marks(x, 5) for x in W2[i]["W"]) == 10 and sum(item_marks(x, 1) for x in W2[i]["G"]) == 10, i
for k in READ:
    assert sum(s["mk"] for s in READ[k]["P1"]["subs"]) == 10 and sum(s["mk"] for s in READ[k]["P2"]["subs"]) == 10
def main():
    d = ROOT
    os.makedirs(f"{d}/Reading_Papers/Answer_Keys", exist_ok=True); os.makedirs(f"{d}/Writing_and_Grammar_Papers/Answer_Keys", exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for i in range(1, 11):
            s = f"{i:02d}"
            data = shuffle_data(dict(A=[READ[i]["P1"]], B=[READ[i]["P2"]]), f"engread{i}")
            secs = [("A", "SECTION — A (Reading Comprehension: Discursive Passage, 400–450 words)", 10, "Read the passage and answer the questions."),
                    ("B", "SECTION — B (Reading Comprehension: Case-based Passage with data/visual input, 200–250 words)", 10, "Read the text and answer the questions.")]
            meta = dict(doc=f"English Reading Paper Set {s}", title="CLASS 10 ENGLISH — READING SKILL PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                        instr=instr_list(["Section A has one discursive passage with 10 questions (1 mark each).", "Section B has one case-based passage with 10 questions (1 mark each).", "Questions include MCQs and short answers of 30–40 words."]), label="<b>Reading Comprehension</b>")
            rd = f"{d}/Reading_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{rd}/English_Reading_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 10 English · Reading Paper · Set {s}", 3)
            to_pdf(pg, eng_key(meta, data), f"{rd}/Answer_Keys/English_Reading_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · English Reading Paper · Set {s}")
            print("R", s, n, fs, flush=True)
            W = copy.deepcopy(W2[i]); fixbr(W)
            data = dict(A=W["W"], B=W["G"])
            secs = [("A", "SECTION — A (Writing Skills: 10 Marks)", 5, "Attempt all the questions; internal choice is given in each."), ("B", "SECTION — B (Grammar: 10 Marks)", 1, "Attempt all the questions.")]
            meta = dict(doc=f"English Writing and Grammar Paper Set {s}", title="CLASS 10 ENGLISH — WRITING &amp; GRAMMAR PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                        instr=instr_list(["Section A (Writing, 10 marks): Q. 1 Formal letter (5 marks, 100–120 words), Q. 2 Analytical paragraph based on data (5 marks, 100–120 words).", "Section B (Grammar, 10 marks): Q. 3–12 gap-filling, editing and transformation items (1 mark each). Topics: determiners, tenses, modals, subject-verb agreement, reported speech, voice and clauses."], "Internal choice is given in Q. 1 and Q. 2."), label="<b>Writing Skills &amp; Grammar</b>")
            wd = f"{d}/Writing_and_Grammar_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{wd}/English_Writing_Grammar_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 10 English · Writing & Grammar · Set {s}", 2)
            to_pdf(pg, eng_key(meta, data), f"{wd}/Answer_Keys/English_Writing_Grammar_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · English Writing & Grammar · Set {s}")
            print("W", s, n, fs, flush=True)
        br.close()
    import index9
    print(index9.make(d, "CLASS 10 ENGLISH — READING &amp; WRITING SKILL PAPERS", "CBSE / RBSE Pattern | Session 2026–27 | Revised",
        "10 Reading papers (20 marks: discursive passage 400–450 words = 10 marks; case-based passage with data 200–250 words = 10 marks) · 10 Writing and Grammar papers (20 marks: formal letter 5, analytical paragraph 5, grammar 10). Every paper has a separate answer key.",
        ["<b>Sets are original.</b> All passages, tasks and model answers are written for this collection.", "<b>Answers are model answers;</b> accept any relevant answer in the candidate's own words."]))
if __name__ == "__main__": main()
