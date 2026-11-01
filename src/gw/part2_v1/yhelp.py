import re, random
KEY = {'A': [], 'B': [], 'C': []}
COUNT = {'A': 0, 'B': 0, 'C': 0}

def _pairs_table(rows):
    """rows: list of (label, text) -> two pairs per table row"""
    out = []
    for i in range(0, len(rows), 2):
        a = rows[i]; b = rows[i+1] if i+1 < len(rows) else ("", "")
        out.append([str(a[0]), a[1], str(b[0]), b[1]])
    return ("table", ["No.", "Answer", "No.", "Answer"], out)

def _key(part, sid, title, rows):
    KEY[part].append(("h3", f"{sid} · {title}"))
    KEY[part].append(_pairs_table(rows))

def items(part, sid, title, instr, pairs):
    """pairs: (q, a) or (q, a, why)"""
    COUNT[part] += len(pairs)
    blocks = [("h3", f"{sid} · {title}"), ("p", instr), ("ol", [p[0] for p in pairs])]
    rows = [(i+1, p[1] + (f" — *{p[2]}*" if len(p) > 2 else "")) for i, p in enumerate(pairs)]
    _key(part, sid, title, rows)
    return blocks

def gap(part, sid, title, instr, text, blanks):
    """text has [1]..[n]; blanks: list of (4 options, correct index 0-3)"""
    n = len(blanks); COUNT[part] += n
    t = re.sub(r"\[(\d+)\]", lambda m: f"**({m.group(1)})** ______", text)
    t = t.replace("\n", "<br>")
    L = "abcd"
    tb = ("table", ["Blank", "(a)", "(b)", "(c)", "(d)"],
          [[str(i+1)] + list(o) for i, (o, _) in enumerate(blanks)])
    rows = [(i+1, f"({L[a]}) {o[a]}") for i, (o, a) in enumerate(blanks)]
    _key(part, sid, title, rows)
    return [("h3", f"{sid} · {title}"), ("p", instr), ("p", t), tb]

def edit(part, sid, title, instr, lines, head=None):
    """lines contain {wrong|right}; one per line"""
    COUNT[part] += len(lines)
    rows_d, rows_k = [], []
    for i, ln in enumerate(lines):
        m = re.search(r"\{([^|}]*)\|([^}]*)\}", ln)
        assert m, ln
        shown = re.sub(r"\{([^|}]*)\|([^}]*)\}", lambda mm: mm.group(1), ln)
        c = "abcdefghij"[i]
        rows_d.append([f"({c})", shown, "", ""])
        rows_k.append((f"({c})", f"**{m.group(1)}** → **{m.group(2)}**"))
    _key(part, sid, title, rows_k)
    return [("h3", f"{sid} · {title}"), ("p", instr),
            ("table", ["", "Passage line", "Incorrect word", "Correction"], rows_d)]

def omit(part, sid, title, instr, lines):
    """lines contain [missing]; one per line"""
    COUNT[part] += len(lines)
    rows_d, rows_k = [], []
    for i, ln in enumerate(lines):
        m = re.search(r"\[([^\]]+)\]", ln)
        assert m, ln
        shown = re.sub(r"\s*\[[^\]]+\]\s*", " ", ln).strip()
        c = "abcdefghij"[i]
        rows_d.append([f"({c})", shown, ""])
        rows_k.append((f"({c})", f"**{m.group(1)}** — {ln.replace('[', '**').replace(']', '**')}"))
    _key(part, sid, title, rows_k)
    return [("h3", f"{sid} · {title}"), ("p", instr),
            ("table", ["", "Passage line (put a slash where a word is missing)", "Missing word"], rows_d)]

def reorder(part, sid, title, instr, sents, seed=7):
    """sents: 'seg / seg / seg / seg.' correct order; displayed shuffled"""
    COUNT[part] += len(sents)
    rnd = random.Random(seed + len(sid) * 13 + sum(map(ord, sid)))
    qs, rows = [], []
    for i, s in enumerate(sents):
        segs = [x.strip() for x in s.split("/")]
        assert len(segs) >= 3, s
        full = " ".join(segs)
        order = list(range(len(segs)))
        for _ in range(20):
            rnd.shuffle(order)
            if order != sorted(order): break
        disp = []
        for j in order:
            x = segs[j].rstrip(".?!")
            if not (x.startswith("I ") or x.startswith("I'") or x.startswith("^")) and x[:1].isupper() and not re.match(r"[A-Z][a-z]*\s", x) is None and j == 0:
                pass
            if x.startswith("^"): x = x[1:]
            elif not (x == "I" or x.startswith("I ") or x.startswith("I’")):
                # lower the first letter only for the sentence-initial segment
                if j == 0: x = x[:1].lower() + x[1:]
            disp.append(x)
        qs.append(" / ".join(disp))
        rows.append((i+1, full.replace("^", "")))
    _key(part, sid, title, rows)
    return [("h3", f"{sid} · {title}"), ("p", instr), ("ol", qs)]

def passage(part, sid, title, instr, pre, text, answers):
    """pre: list of dialogue/instruction lines (strings); text has (a)__ blanks marked {a}..; answers list"""
    COUNT[part] += len(answers)
    t = re.sub(r"\{([a-j])\}", lambda m: f"**({m.group(1)})** ____________", text)
    blocks = [("h3", f"{sid} · {title}"), ("p", instr)]
    if pre: blocks.append(("ul", pre))
    blocks.append(("p", t))
    _key(part, sid, title, [(f"({'abcdefghij'[i]})", a) for i, a in enumerate(answers)])
    return blocks
