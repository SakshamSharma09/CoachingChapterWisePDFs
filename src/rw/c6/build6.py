import os, sys, importlib
sys.path.insert(0, "/home/claude/rw/c6")
from playwright.sync_api import sync_playwright
import compose_core as M
from lib import to_pdf
from eng6_lib import eng_paper, eng_key
import compose_eng9_shared as C

def load_sets(names):
    out = {}
    for n in names:
        m = importlib.import_module(f"en6.{n}")
        out.update(m.SETS)
    return out
READ = load_sets(["r6a", "r6b"]); WRIT = load_sets(["w6a", "w6b"])
assert len(READ) == 10 and len(WRIT) == 10
ROOT = "/home/claude/rw/out/Class6/Class6_English_Reading_Writing"

def main():
    d = ROOT; os.makedirs(f"{d}/Reading_Papers/Answer_Keys", exist_ok=True); os.makedirs(f"{d}/Writing_and_Grammar_Papers/Answer_Keys", exist_ok=True)
    log = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for i in range(1, 11):
            s = f"{i:02d}"
            data = C.shuffle_data(dict(A=[READ[i]["P1"]], B=[READ[i]["P2"]]), f"engread6_{i}")
            secs = [("A", "SECTION — A (Reading Comprehension: Factual Passage)", 10, "Read the passage and answer the questions."),
                    ("B", "SECTION — B (Reading Comprehension: Story / Poem)", 10, "Read the text and answer the questions.")]
            meta = dict(doc=f"Class 6 English Reading Paper Set {s}", title="CLASS 6 ENGLISH — READING SKILL PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                        instr=C.instr_list(["Section A has one factual passage with 10 questions (1 mark each).", "Section B has one story or poem with 10 questions (1 mark each).", "Read the passages carefully before attempting the questions."]), label="<b>Reading Comprehension</b>")
            rd = f"{d}/Reading_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{rd}/Class6_English_Reading_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 6 English · Reading Paper · Set {s}", 3)
            to_pdf(pg, eng_key(meta, data), f"{rd}/Answer_Keys/Class6_English_Reading_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 6 English Reading Paper · Set {s}")
            log.append((f"Reading_{s}", n, fs))
            W = WRIT[i]
            data = dict(A=W["W"], B=W["G"])
            secs = [("A", "SECTION — A (Writing Skills)", 4, "Attempt all the questions; internal choice is given in each."), ("B", "SECTION — B (Grammar)", 1, "Attempt all the questions.")]
            meta = dict(doc=f"Class 6 English Writing and Grammar Paper Set {s}", title="CLASS 6 ENGLISH — WRITING &amp; GRAMMAR PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                        instr=C.instr_list(["Section A: Q. 1 Notice or Message (3 marks), Q. 2 Letter or E-mail (5 marks), Q. 3 Paragraph, Diary Entry or Story (4 marks).", "Section B: Q. 4–11 Grammar (1 mark each).", "Keep to the word limit given in each question."], "Internal choice is given in Q. 1, 2 and 3."), label="<b>Writing Skills &amp; Grammar</b>")
            wd = f"{d}/Writing_and_Grammar_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{wd}/Class6_English_Writing_Grammar_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 6 English · Writing & Grammar · Set {s}", 2)
            to_pdf(pg, eng_key(meta, data), f"{wd}/Answer_Keys/Class6_English_Writing_Grammar_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · Class 6 English Writing & Grammar · Set {s}")
            log.append((f"WritingGrammar_{s}", n, fs))
        br.close()
    for l in log: print(*l)
main()
