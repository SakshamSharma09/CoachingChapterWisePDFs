import os, sys, copy, random, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from playwright.sync_api import sync_playwright
import compose_core as M
from lib import to_pdf
from eng9_lib import eng_paper, eng_key, OR, item_marks
import compose_eng9 as C   # reuse shuffle_data, instr_list
from en9 import r9a, r9b, r9c, x9_ext, x9_p2, w9n_a, w9n_b
ROOT = "/home/claude/rw/out/Class9/English_Class9_Reading_Writing"
READ = {}
for m in (r9a, r9b, r9c): READ.update(m.SETS)
for k in READ:
    p1 = copy.deepcopy(READ[k]["P1"])
    parts = p1["text"].split("</p>")
    ins = x9_ext.EXT[k].split("</p>")[0] + "</p>" + x9_ext.EXT[k].split("</p>")[1] + "</p>"

    body = [x for x in p1["text"].split("</p>") if x.strip()]
    orig = [x for x in READ[k]["P1"]["text"].split("</p>") if x.strip()]
    ext = [x for x in (x9_ext.EXT[k] + x9_ext.EXB[k]).split("</p>") if x.strip()]
    paras = orig[:2] + ext + orig[2:]
    p1["text"] = "".join(x.strip() + "</p>" for x in paras)
    p1["subs"] = p1["subs"] + x9_ext.XS[k]
    READ[k] = dict(P1=p1, P2=x9_p2.P2[k])
WRIT = {}
for m in (w9n_a, w9n_b): WRIT.update(m.SETS)
def fixbr(o):
    if isinstance(o, dict):
        for kk, v in list(o.items()):
            if isinstance(v, str): o[kk] = v.replace("\\n", "<br>").replace("\n", "<br>") if kk in ("ans",) else v
            else: fixbr(v)
    elif isinstance(o, list):
        for x in o: fixbr(x)
fixbr(WRIT)
for k in READ:
    assert sum(s["mk"] for s in READ[k]["P1"]["subs"]) == 12 and sum(s["mk"] for s in READ[k]["P2"]["subs"]) == 8, k
for k in WRIT:
    assert sum(item_marks(i, 4) for i in WRIT[k]["W"]) == 20 and sum(item_marks(i, 1) for i in WRIT[k]["G"]) == 10, k

def main():
    d = ROOT
    os.makedirs(f"{d}/Reading_Papers/Answer_Keys", exist_ok=True); os.makedirs(f"{d}/Writing_and_Grammar_Papers/Answer_Keys", exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for i in range(1, 11):
            s = f"{i:02d}"
            data = C.shuffle_data(dict(A=[READ[i]["P1"]], B=[READ[i]["P2"]]), f"engread{i}")
            secs = [("A", "SECTION — A (Reading Comprehension: Factual / Discursive Passage, 400–450 words)", 12, "Read the passage and answer the questions."),
                    ("B", "SECTION — B (Reading Comprehension: Case-based Passage, 200–250 words)", 8, "Read the text and answer the questions.")]
            meta = dict(doc=f"English Reading Paper Set {s}", title="CLASS 9 ENGLISH — READING SKILL PAPER", set=s, time="45 Minutes", marks=20, secs=secs,
                        instr=C.instr_list(["Section A has one passage with 12 questions (1 mark each).", "Section B has one case-based passage with 8 questions (1 mark each).", "Questions include MCQs and short answers of 30–40 words."]), label="<b>Reading Comprehension</b>")
            rd = f"{d}/Reading_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{rd}/English_Reading_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 9 English · Reading Paper · Set {s}", 3)
            to_pdf(pg, eng_key(meta, data), f"{rd}/Answer_Keys/English_Reading_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · English Reading Paper · Set {s}")
            print("R", s, n, fs, flush=True)
            W = WRIT[i]
            data = dict(A=W["W"], B=W["G"])
            secs = [("A", "SECTION — A (Writing Skills: 20 Marks)", 4, "Attempt all the questions; internal choice is given in each."),
                    ("B", "SECTION — B (Grammar: 10 Marks)", 1, "Attempt all the questions.")]
            meta = dict(doc=f"English Writing and Grammar Paper Set {s}", title="CLASS 9 ENGLISH — WRITING &amp; GRAMMAR PAPER", set=s, time="1 Hour 15 Minutes", marks=30, secs=secs,
                        instr=C.instr_list(["Section A (Writing, 20 marks): Q. 1 Notice/Poster (4 marks, up to 50 words), Q. 2 Formal letter/email (5 marks, 120–150 words), Q. 3 Speech/Article (5 marks, 120–150 words), Q. 4 Narrative essay/story (6 marks, 150–180 words).", "Section B (Grammar, 10 marks): Q. 5 Paragraph completion (4 marks), Q. 6–8 Sentence rearrangement (1 mark each), Q. 9–11 Sentence transformation (1 mark each)."], "Internal choice is given in Q. 1, 2, 3 and 4."), label="<b>Writing Skills &amp; Grammar</b>")
            wd = f"{d}/Writing_and_Grammar_Papers"
            n, fs = M.fit(pg, lambda f: eng_paper(meta, data, f), f"{wd}/English_Writing_Grammar_Paper_Set_{s}.pdf", f"Mastermind Coaching Classes — Class 9 English · Writing & Grammar · Set {s}", 4)
            to_pdf(pg, eng_key(meta, data), f"{wd}/Answer_Keys/English_Writing_Grammar_Paper_Set_{s}_Answer_Key.pdf", f"Answer Key · English Writing & Grammar · Set {s}")
            print("W", s, n, fs, flush=True)
        br.close()
    import index9
    print(index9.make(d, "CLASS 9 ENGLISH — READING &amp; WRITING SKILL PAPERS", "CBSE / RBSE Pattern | Session 2026–27 | Revised",
        "10 Reading papers (20 marks: factual/discursive passage 400–450 words = 12 marks; case-based passage 200–250 words = 8 marks) · 10 Writing and Grammar papers (30 marks: Notice/Poster 4, Formal letter/email 5, Speech/Article 5, Narrative essay 6; Grammar 10). Every paper has a separate answer key.",
        ["<b>Sets are original.</b> All passages, tasks and model answers are written for this collection.", "<b>Answers are model answers;</b> accept any relevant answer in the candidate's own words."]))
if __name__ == "__main__": main()
