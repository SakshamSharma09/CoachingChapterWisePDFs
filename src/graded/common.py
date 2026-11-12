"""Graded-paper composer: NCERT-type / Easy / Medium / Hard x 3 sets per chapter (40-mark papers + answer keys).

Reuses the layout engine in ../c8build/lib.py. Each chapter module exposes
    TIERS = {"NCERT": dict(A=[...], B=[...], C=[...], D=[...]), "Easy": ..., "Medium": ..., "Hard": ...}
with at least A>=30 MCQ, B>=12, C>=18, D>=12 items per tier (built with lib.mcq / lib.Q).
"""
import os, sys, random, copy, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = HERE.parent / "c8build"
sys.path.insert(0, str(BUILD))
import lib
from lib import OR, generic_paper, generic_key, to_pdf as _unused
from lib import Q, mcq  # noqa: F401

def M4(q, c, w, why=""):
    """MCQ with correct option first; distractors de-duplicated and, for numeric answers, padded automatically."""
    c = str(c); seen = []
    for x in w:
        x = str(x)
        if x != c and x not in seen: seen.append(x)
    try:
        v = int(c)
        for d in (1, -1, 2, 3, -2, 4, 5, 10):
            x = str(v + d)
            if len(seen) >= 3: break
            if x != c and x not in seen and v + d >= 0: seen.append(x)
    except ValueError:
        pass
    assert len(seen) >= 3, (q, c, w)
    return mcq(q, [c] + seen[:3], "a", why)

AR_OPTS = ["Both A and R are true and R is the correct explanation of A.",
           "Both A and R are true but R is not the correct explanation of A.",
           "A is true but R is false.", "A is false but R is true."]
def AR4(assertion, reason, key, why=""):
    """CBSE assertion-reason MCQ. key: 'a' both true & R explains A; 'b' both true, R does not explain A; 'c' A true R false; 'd' A false R true."""
    assert key in "abcd"
    return dict(kind="mcq", q=f"<b>Assertion (A):</b> {assertion}<br><b>Reason (R):</b> {reason}<br>Choose the correct option:",
                opts=list(AR_OPTS), ans=key, why=why, fig=None)

def load_extras(modname):
    import importlib
    try: return importlib.import_module(f"x.{modname}_x")
    except ModuleNotFoundError as e:
        if e.name and e.name.startswith("x"): return None
        raise

def mistakes_box(items):
    if not items: return ""
    lis = "".join(f"<li>{i}</li>" for i in items)
    return ("<div style='border-left:3px solid #b3261e;background:#fdf1f0;padding:3px 8px;font-size:8.2pt;margin:6px 0'>"
            f"<b>Mistakes to avoid:</b><ul style='margin:2px 0 0 14px;padding:0'>{lis}</ul></div>")

# --- Windows-safe asset paths (lib builds file:// + path) ---
def _uri_path(p):
    p = str(p).replace("\\", "/")
    return p if p.startswith("/") else "/" + p
lib.KATEX = _uri_path(lib.KATEX)
lib.FONT = _uri_path(lib.FONT)

TIER_ORDER = ["NCERT", "Easy", "Medium", "Hard"]
TIER_FOLDER = {"NCERT": "1_NCERT_Type", "Easy": "2_Easy_Level", "Medium": "3_Medium_Level", "Hard": "4_Hard_Level"}
TIER_LABEL = {"NCERT": "NCERT-TYPE", "Easy": "EASY LEVEL", "Medium": "MEDIUM LEVEL", "Hard": "HARD LEVEL"}
TIER_NICE = {"NCERT": "NCERT-Type", "Easy": "Easy Level", "Medium": "Medium Level", "Hard": "Hard Level"}
TIER_BLURB = {"NCERT": "NCERT-type: questions in the style of the textbook examples and exercises",
              "Easy": "Easy level: direct, single-step questions", "Medium": "Medium level: multi-step questions",
              "Hard": "Hard level: application and higher-order questions"}
NSETS = 3

FIXED = re.compile(r"both|neither|cannot be determined|none|^correct$|all of these|all the above|^A is (true|false)|^R is (true|false)", re.I)
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

def grp(lst, n):
    """Split a flat list into topic groups of n (so sets mix topics)."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def interleave(groups):
    """Round-robin across topic groups so every set mixes topics."""
    out = []; i = 0
    while any(i < len(g) for g in groups):
        for g in groups:
            if i < len(g): out.append(g[i])
        i += 1
    return out

def make_sets(tier, tag, ex=None):
    """tier: dict(A=[groups..] or flat, B, C, D). Returns [set dicts]."""
    flat = {}
    for k in "ABCD":
        v = tier[k]
        flat[k] = interleave(v) if v and isinstance(v[0], list) else list(v)
    need = dict(A=10 * NSETS, B=4 * NSETS, C=6 * NSETS, D=4 * NSETS)
    for k, n in need.items():
        assert len(flat[k]) >= n, f"{tag}: section {k} has {len(flat[k])}, need {n}"
        qs = [x["q"] + "|".join(x.get("opts") or []) for x in flat[k]]
        assert len(set(qs)) == len(qs), f"{tag}: duplicate question text in {k}"
    sets = []
    for s in range(NSETS):
        A = flat["A"][10 * s:10 * s + 10]; B = flat["B"][4 * s:4 * s + 4]
        C = flat["C"][6 * s:6 * s + 6]; D = flat["D"][4 * s:4 * s + 4]
        rng = random.Random(f"{tag}{s}")
        A = [shuffle_mcq(i, rng) for i in A]
        Dq = [OR(D[0], D[1]), OR(D[2], D[3])]
        ar = list(getattr(ex, "AR", []) or []); cs = list(getattr(ex, "CASE", []) or [])
        if ex is not None and len(ar) >= 2 * NSETS:
            A = A[:8] + [shuffle_mcq(i, rng) for i in ar[2 * s:2 * s + 2]]
        if ex is not None and len(cs) >= NSETS:
            Dq = [cs[s], OR(D[2], D[3])]
        sets.append(dict(A=A, B=B, C=[C[0], C[1], OR(C[2], C[3]), OR(C[4], C[5])], D=Dq))
    return sets

# ---- rendering ----
def to_pdf(page, html_str, out_pdf, footer_left):
    import html as _h
    tmp = Path(out_pdf).with_suffix(".html")
    tmp.write_text(html_str, encoding="utf-8")
    page.goto(tmp.as_uri())
    page.wait_for_function("window.__done === true", timeout=30000)
    page.pdf(path=str(out_pdf), format="A4", print_background=True, display_header_footer=True,
             header_template="<span></span>",
             footer_template=f"""<div style="width:100%;font-family:Arial;font-size:7px;margin:0 12mm;display:flex;justify-content:space-between;border-top:.7px solid #13286b;padding-top:2px;color:#13286b">
<span>{_h.escape(footer_left)}</span><span style="color:#c49a3c;font-weight:bold">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>""",
             margin=dict(top="11mm", bottom="13mm", left="12mm", right="12mm"))
    tmp.unlink()

def npages(pdf):
    from pypdf import PdfReader
    return len(PdfReader(str(pdf)).pages)

def fit(pg, html_fn, out, foot, target=2, fmin=8.8):
    fs = 11.8
    while True:
        to_pdf(pg, html_fn(fs), out, foot)
        n = npages(out)
        if n <= target or fs <= fmin: return n, fs
        fs = round(fs - 0.2, 1)

def unite(files, out):
    from pypdf import PdfWriter
    w = PdfWriter()
    for f in files: w.append(str(f))
    with open(out, "wb") as fh: w.write(fh)
    w.close()
    for f in files: os.remove(f)

SECS = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
        ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 20–30 words each."),
        ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 40–60 words each."),
        ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")]

def instr(tier):
    return ["All questions are compulsory.", "Q. 1–10 are Objective Type (1 mark each).",
            "Q. 11–14 are Very Short Answer Type (2 marks each).", "Q. 15–18 are Short Answer Type (3 marks each).",
            "Q. 19–20 are Long Answer Type (5 marks each).", "Internal choice is given in Q. 17 to 20.",
            "Write the question number before each answer.", TIER_BLURB[tier] + "."]

def build_chapter(pg, root, cls, subject, chno, slug, name, tiers, only=None, extras=None):
    """root = repo path of .../Graded_Papers"""
    lib.CHAPTERS.clear(); lib.CHAPTERS[chno] = name; lib.SUBJECT[0] = subject
    log = []
    _gk = lib.generic_key
    mb = mistakes_box(getattr(extras, "MISTAKES", None))
    def gk(meta, data):
        h = _gk(meta, data).replace("Class 8 ", f"Class {cls} ", 1)
        return h.replace("<div class='note'>", mb + "<div class='note'>", 1) if mb else h
    for tier in TIER_ORDER:
        if only and tier not in only: continue
        if tier not in tiers: continue
        d = Path(root) / f"Ch{chno:02d}_{slug}" / TIER_FOLDER[tier]; d.mkdir(parents=True, exist_ok=True)
        sets = make_sets(tiers[tier], f"{subject}{chno}{tier}", extras if tier == "Hard" else None)
        keys = []
        for s, data in enumerate(sets, 1):
            base = f"Ch{chno:02d}_{slug}_{tier}_Set_{s}"
            meta = dict(doc=f"{base}", title=f"CLASS {cls} — {subject.replace('_', ' ').upper()} · {TIER_LABEL[tier]} CHAPTER TEST", set=str(s), chs=(chno,),
                        time="1 Hour 30 Minutes", marks=40, secs=SECS, instr=instr(tier))
            n, fs = fit(pg, lambda f: generic_paper(meta, data, f), d / f"{base}.pdf",
                        f"Mastermind Coaching Classes — Class {cls} {subject} · Ch {chno}: {name} · {TIER_NICE[tier]} · Set {s}")
            log.append((base, n, fs))
            k = d / f"_k{s}.pdf"; to_pdf(pg, gk(meta, data), k, f"Answer Key · {subject} Ch {chno} · {TIER_NICE[tier]} · Set {s}"); keys.append(k)
        unite(keys, d / f"Ch{chno:02d}_{slug}_{tier}_Answer_Key.pdf")
    return log
