import os, sys, copy, random, importlib, subprocess, re
from playwright.sync_api import sync_playwright
import lib
from lib import CHAPTERS, OR, generic_paper, generic_key, paper_html, key_html, to_pdf


def pages(pdf):
    o = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    return int([l for l in o.splitlines() if l.startswith("Pages")][0].split()[1])

FIXED = re.compile(r"both|neither|cannot be determined|none|^correct$|all of these|all the above|उपर्युक्त|इनमें से|दोनों|सभी|कोई नहीं", re.I)
def shuffle_mcq(it, rng):
    it = copy.deepcopy(it)
    opts = it["opts"]; ans = "abcd".index(it["ans"])
    free = [i for i, o in enumerate(opts) if not FIXED.search(o)]
    perm = free[:]; rng.shuffle(perm)
    new = opts[:]; newans = ans
    for dst, src in zip(free, perm):
        new[dst] = opts[src]
        if src == ans: newans = dst
    it["opts"] = new; it["ans"] = "abcd"[newans]
    return it

def shuffle_paper(data, seed):
    rng = random.Random(seed)
    d = dict(data); d["A"] = [shuffle_mcq(i, rng) for i in data["A"]]
    return d

# ---------------- bank ----------------
BANK = []
def add(item, ch, lvl, src):
    BANK.append(dict(item=item, ch=ch, lvl=lvl, src=src, uid=len(BANK), used=0))

import difflib
def _norm(b):
    t = b["item"]["q"]
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).lower()
def _ans(b):
    it = b["item"]
    return (it["opts"]["abcd".index(it["ans"])] if it["kind"] == "mcq" else it["ans"]).lower()
TAKEN_TXT = {}
def pick(ch, lvl, n, prefer, taken, rng):
    if not taken:
        TAKEN_TXT.pop(id(taken), None); TAKEN_TXT.pop(("ans", id(taken)), None)
    chosen = TAKEN_TXT.setdefault(id(taken), [])
    cands = [b for b in BANK if b["ch"] == ch and b["lvl"] == lvl and b["uid"] not in taken]
    rng.shuffle(cands)
    cands.sort(key=lambda b: (b["used"], 0 if b["src"] in prefer else 1))
    out = []
    for b in cands:
        if len(out) == n: break
        t = _norm(b)
        if any(difflib.SequenceMatcher(None, t, c).ratio() > 0.62 for c in chosen): continue
        if b["lvl"] == "A" and any(_ans(b) == a for a in TAKEN_TXT.setdefault(("ans", id(taken)), [])): continue
        out.append(b); chosen.append(t); TAKEN_TXT[("ans", id(taken))].append(_ans(b))
    if len(out) < n: raise SystemExit(f"bank short: ch{ch} {lvl} need {n}")
    for b in out: b["used"] += 1; taken.add(b["uid"])
    return [b["item"] for b in out]

def orpair(ch, lvl, prefer, taken, rng):
    a, b = pick(ch, lvl, 2, prefer, taken, rng)
    return OR(a, b)

# ---------------- builders ----------------
def fit(pg, html_fn, out, foot, target, fmin=9.4):
    fs = 11.8
    while True:
        to_pdf(pg, html_fn(fs), out, foot)
        n = pages(out)
        if n <= target or fs <= fmin: break
        fs = round(fs - 0.2, 1)
    if n > target:  # allow one more page at a comfortable size
        fs = 11.0
        while True:
            to_pdf(pg, html_fn(fs), out, foot)
            if pages(out) <= target + 1 or fs <= fmin: break
            fs = round(fs - 0.2, 1)
    return pages(out), fs

def unite(files, out):
    subprocess.run(["pdfunite", *files, out], check=True)
    for f in files: os.remove(f)

S40 = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
       ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 20–30 words each."),
       ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 40–60 words each."),
       ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")]

def instr(counts, choice_from, extra):
    a, b, c, d = counts
    q1 = a; q2 = a + b; q3 = a + b + c; q4 = a + b + c + d
    return ["All questions are compulsory.",
            f"Q. 1–{q1} are Objective Type (1 mark each).",
            f"Q. {q1+1}–{q2} are Very Short Answer Type (2 marks each).",
            f"Q. {q2+1}–{q3} are Short Answer Type (3 marks each).",
            f"Q. {q3+1}–{q4} are Long Answer Type (5 marks each).",
            f"Internal choice is given in Q. {choice_from} to {q4}.",
            "Write the question number before each answer.", extra]

