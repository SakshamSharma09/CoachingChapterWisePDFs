import os, sys, copy, random, importlib
sys.path.insert(0, "/home/claude/rw/c7")
from playwright.sync_api import sync_playwright
import compose_core as M
from lib import to_pdf
from eng9_lib import eng_paper, eng_key

ROOT = "/home/claude/rw/out/Class7/Class7_Reading_Writing_Papers"
def load(names):
    out = {}
    for n in names: out.update(importlib.import_module(f"en7.{n}").SETS)
    return out
READ = load(["r7a", "r7b"]); WRIT = load(["w7a", "w7b"])
assert len(READ) == 10 and len(WRIT) == 10

def shuf_sub(s, rng):
    s = copy.deepcopy(s)
    if s.get("opts") and len(s["opts"]) > 2 and not any(M.FIXED.search(o) for o in s["opts"]):
        c = s["opts"]["abcd".index(s["ans"])]; rng.shuffle(s["opts"]); s["ans"] = "abcd"[s["opts"].index(c)]
    return s
def shuffle_data(data, seed):
    rng = random.Random(seed); out = {}
    for k, items in data.items():
        new = []
        for it in items:
            if it["kind"] == "pas":
                it = copy.deepcopy(it); it["subs"] = [shuf_sub(s, rng) for s in it["subs"]]
            new.append(it)
        out[k] = new
    return out
def instr(parts): return ["All questions are compulsory."] + parts + ["Write the question number before each answer."]

def main():
    d = ROOT; rd = f"{d}/Reading_Papers"; wd = f"{d}/Writing_and_Grammar_Papers"
    for p in (f"{rd}/Answer_Keys", f"{wd}/Answer_Keys"): os.makedirs(p, exist_ok=True)
    with sync_playwright() as p:
        pg = p.chromium.launch().new_page()
        for i in range(1, 11):
            s = f"{i:02d}"
            data = shuffle_data(dict(A=[READ[i]["P1"]], B=[READ[i]["P2"]]), f"c7read{i}")
            secs = [("A", "SECTION — A (Reading Comprehension: Factual Passage)", 10, "Read the passage and answer the questions."),
                    ("B", "SECTION — B (Reading Comprehension: Story / Poem)", 10, "Read the text and answer the questions.")]
            meta = dict(doc=f"English Reading Paper Set {s}", title="CLASS 7 ENGLISH — READING SKILL PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                        instr=instr(["Section A has one factual passage with 10 questions (1 mark each).", "Section B has one story or poem with 10 questions (1 mark each)."]), label="<b>Reading Comprehension</b>")
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{rd}/English_Reading_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 7 English · Reading Paper · Set {s}", 3)
            to_pdf(pg, eng_key(meta, data), f"{rd}/Answer_Keys/English_Reading_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 7 English Reading Paper · Set {s}")
            print("R", s, n, fs)
            W = WRIT[i]; data = dict(A=W["W"], B=W["G"])
            secs = [("A", "SECTION — A (Writing Skills)", 4, "Attempt all the questions; internal choice is given in each."), ("B", "SECTION — B (Grammar)", 1, "Attempt all the questions.")]
            meta = dict(doc=f"English Writing and Grammar Paper Set {s}", title="CLASS 7 ENGLISH — WRITING &amp; GRAMMAR PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                        instr=instr(["Section A: Q. 1 Notice / Message / E-mail (3 marks), Q. 2 Letter (5 marks), Q. 3 Paragraph / Diary / Story (4 marks).", "Section B: Q. 4–11 Grammar (1 mark each).", "Internal choice is given in Q. 1, 2 and 3."]), label="<b>Writing Skills &amp; Grammar</b>")
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{wd}/English_Writing_Grammar_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 7 English · Writing & Grammar · Set {s}", 2)
            to_pdf(pg, eng_key(meta, data), f"{wd}/Answer_Keys/English_Writing_Grammar_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 7 English Writing & Grammar · Set {s}")
            print("W", s, n, fs)
main()
import index9
print(index9.make(ROOT, "CLASS 7 ENGLISH — READING &amp; WRITING PAPER COLLECTION INDEX",
 "RBSE Board Pattern | Session 2026–27 | Class 7 level (NCERT Honeysuckle / An Alien Hand pattern)",
 "10 Reading skill papers (20 marks) and 10 Writing &amp; Grammar papers (20 marks), each with a separate answer key.",
 ["<b>Reading papers:</b> Section A is a factual passage (about 200–250 words); Section B is a story or a poem. Each has 10 questions: MCQ, True/False, short answers, vocabulary, reference and inference.",
  "<b>Writing &amp; Grammar papers:</b> Q1 notice / message / e-mail (3), Q2 informal or formal letter (5), Q3 paragraph / diary entry / short story (4), plus 8 grammar items (tenses, articles, prepositions, conjunctions, voice, reported speech, word formation).",
  "<b>Note:</b> All passages, poems and model answers are original."]))
