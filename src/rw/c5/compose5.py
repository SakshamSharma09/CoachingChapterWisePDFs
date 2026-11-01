import os, sys, copy, importlib
from playwright.sync_api import sync_playwright
import compose_core as M
from lib import to_pdf
from eng9_lib import eng_paper, eng_key
import random
class C9:
    @staticmethod
    def shuffle_data(data, seed):
        rng = random.Random(seed); out = {}
        for k, items in data.items():
            new = []
            for it in items:
                if it["kind"] == "pas":
                    it = copy.deepcopy(it)
                    for s in it["subs"]:
                        if s.get("opts") and not any(M.FIXED.search(o) for o in s["opts"]):
                            c = s["opts"]["abcd".index(s["ans"])]; rng.shuffle(s["opts"]); s["ans"] = "abcd"[s["opts"].index(c)]
                new.append(it)
            out[k] = new
        return out
ROOT = "/home/claude/rw/out/Class5"
def load(names):
    out = {}
    for n in names: out.update(importlib.import_module(f"en5.{n}").SETS)
    return out
READ = load(["r5a", "r5b"]); WRIT = load(["w5a", "w5b"])
assert len(READ) == 10 and len(WRIT) == 10
def main():
    d = f"{ROOT}/Class5_English_Reading_Writing"; log = []
    for sub in ("Reading_Papers/Answer_Keys", "Writing_and_Grammar_Papers/Answer_Keys"): os.makedirs(f"{d}/{sub}", exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for i in range(1, 11):
            s = f"{i:02d}"
            data = C9.shuffle_data(dict(A=[READ[i]["P1"]], B=[READ[i]["P2"]]), f"c5read{i}")
            secs = [("A", "SECTION — A (Reading: Information Passage / Notice / Table)", 10, "Read the passage and answer the questions."),
                    ("B", "SECTION — B (Reading: Story / Poem)", 10, "Read the text and answer the questions.")]
            meta = dict(doc=f"Class 5 English Reading Paper Set {s}", title="CLASS 5 ENGLISH — READING PAPER", set=s, time="40 Minutes", marks=20, secs=secs,
                        instr=["All questions are compulsory.", "Section A has one passage with 10 questions (1 mark each).", "Section B has one story or poem with 10 questions (1 mark each).", "Read the passage twice before you answer. Write neatly."],
                        label="<b>Reading Comprehension</b>")
            rd = f"{d}/Reading_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{rd}/English_Reading_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 5 English · Reading Paper · Set {s}", 3)
            to_pdf(pg, eng_key(meta, data), f"{rd}/Answer_Keys/English_Reading_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 5 English Reading · Set {s}")
            log.append((f"Reading_{s}", n, fs))
            W = WRIT[i]; data = dict(A=W["W"], B=W["G"])
            secs = [("A", "SECTION — A (Writing Skills)", 4, "Attempt all the questions; a choice is given in each."), ("B", "SECTION — B (Grammar)", 1, "Attempt all the questions.")]
            meta = dict(doc=f"Class 5 English Writing and Grammar Paper Set {s}", title="CLASS 5 ENGLISH — WRITING &amp; GRAMMAR PAPER", set=s, time="40 Minutes", marks=20, secs=secs,
                        instr=["All questions are compulsory.", "Section A: Q. 1 Message or Notice (3 marks), Q. 2 Letter (5 marks), Q. 3 Paragraph (4 marks).", "Section B: Q. 4–11 Grammar (1 mark each).", "Choice is given in Q. 1, 2 and 3. Write in neat handwriting."],
                        label="<b>Writing Skills &amp; Grammar</b>")
            wd = f"{d}/Writing_and_Grammar_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{wd}/English_Writing_Grammar_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 5 English · Writing & Grammar · Set {s}", 2)
            to_pdf(pg, eng_key(meta, data), f"{wd}/Answer_Keys/English_Writing_Grammar_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 5 English Writing & Grammar · Set {s}")
            log.append((f"WG_{s}", n, fs))
        br.close()
    for l in log: print(*l)
main()
