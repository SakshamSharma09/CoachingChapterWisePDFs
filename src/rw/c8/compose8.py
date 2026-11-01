"""Class 8 English: Reading and Writing+Grammar skill papers."""
import os, sys, copy, random, importlib
from playwright.sync_api import sync_playwright
import compose_core as M
from lib import to_pdf
from eng9_lib import eng_paper, eng_key

ROOT = "/home/claude/rw/out/Class8/Class8_English_Reading_Writing"
def load(names):
    out = {}
    for n in names:
        out.update(importlib.import_module(f"en8.{n}").SETS)
    return out
READ = load(["r8a", "r8b", "r8c"]); WRIT = load(["w8a", "w8b"])
assert len(READ) == 10 and len(WRIT) == 10

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
            if it["kind"] == "pas":
                it = copy.deepcopy(it); it["subs"] = [shuf_sub(s, rng) for s in it["subs"]]
            new.append(it)
        out[k] = new
    return out
def instr_list(parts, choice=None):
    base = ["All questions are compulsory."] + parts
    if choice: base.append(choice)
    return base + ["Write the question number before each answer."]

def main():
    d = ROOT
    rd = f"{d}/Reading_Papers"; wd = f"{d}/Writing_and_Grammar_Papers"
    os.makedirs(f"{rd}/Answer_Keys", exist_ok=True); os.makedirs(f"{wd}/Answer_Keys", exist_ok=True)
    log = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for i in range(1, 11):
            s = f"{i:02d}"
            data = shuffle_data(dict(A=[READ[i]["P1"]], B=[READ[i]["P2"]]), f"c8read{i}")
            secs = [("A", "SECTION — A (Reading Comprehension: Factual / Discursive Passage)", 10, "Read the passage and answer the questions."),
                    ("B", "SECTION — B (Reading Comprehension: Literary Passage — Poem / Story)", 10, "Read the text and answer the questions.")]
            meta = dict(doc=f"Class 8 English Reading Paper Set {s}", title="CLASS 8 ENGLISH — READING SKILL PAPER", set=s, time="40 Minutes", marks=20, secs=secs,
                        instr=instr_list(["Section A has one factual passage with 10 questions (1 mark each).", "Section B has one literary passage (poem or story) with 10 questions (1 mark each)."]), label="<b>Reading Comprehension</b>")
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{rd}/Class8_English_Reading_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 8 English · Reading Paper · Set {s}", 3)
            to_pdf(pg, eng_key(meta, data), f"{rd}/Answer_Keys/Class8_English_Reading_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 8 English Reading Paper · Set {s}")
            log.append((f"Reading_{s}", n, fs))
            W = WRIT[i]
            data = dict(A=W["W"], B=W["G"])
            secs = [("A", "SECTION — A (Writing Skills)", 4, "Attempt all the questions; internal choice is given in each."), ("B", "SECTION — B (Grammar)", 1, "Attempt all the questions.")]
            meta = dict(doc=f"Class 8 English Writing and Grammar Paper Set {s}", title="CLASS 8 ENGLISH — WRITING &amp; GRAMMAR PAPER", set=s, time="40 Minutes", marks=20, secs=secs,
                        instr=instr_list(["Section A: Q. 1 Notice / Message / Diary / E-mail (3 marks), Q. 2 Letter / Application (5 marks), Q. 3 Paragraph / Article / Story / Speech (4 marks).", "Section B: Q. 4–11 Grammar (1 mark each)."], "Internal choice is given in Q. 1, 2 and 3."), label="<b>Writing Skills &amp; Grammar</b>")
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{wd}/Class8_English_Writing_Grammar_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 8 English · Writing & Grammar · Set {s}", 2)
            to_pdf(pg, eng_key(meta, data), f"{wd}/Answer_Keys/Class8_English_Writing_Grammar_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 8 English Writing & Grammar · Set {s}")
            log.append((f"WritingGrammar_{s}", n, fs))
        br.close()
    for l in log: print(*l)
if __name__ == "__main__": main()
