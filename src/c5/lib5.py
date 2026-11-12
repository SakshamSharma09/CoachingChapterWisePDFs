"""Class 5 model-paper builder (RSCERT PELLE pattern: 80 marks, 2.30 h, 22 questions = 7 OT x1 + 7 VSA x3 + 6 SA x6 + 2 ET x8).
Usage (from a paper module):  from lib5 import *;  build(meta, sections, outdir)   -> <outdir>/Model_Paper_NN.pdf and Model_Paper_NN_Solved.pdf
meta     = dict(subject='Maths'|'English'|'Hindi'|'EVS', set_no=1, time='2.30 Hours' (Hindi: '2.30 घण्टे'), marks=80, instr=[...])
sections = [sec(title, marks, items, note=''), ...]
item     = Q(q, marks, ans, opts=None, fig=None, parts=None, passage=None, alt=None)
   q       html question text (for items with parts it is the stem; may be '')
   opts    list of 4 option strings -> printed as (a)..(d); ans for such items must be the letter + text, e.g. '(b) 24'
   parts   [P(label, q, marks, ans, opts=None, fig=None), ...]  marks of the item = sum of parts
   passage html block (reading passage / case study text) printed before the stem and parts
   alt     another Q(...) = the OR alternative (same marks)
No ruled answer lines are printed (owner requirement: no wasted answer space); solved copy prints answers in green under each question/part."""
import html as _h, sys, os, glob
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "graded"))
import common                      # noqa: F401  (sets Windows-safe asset paths and imports lib)
from common import lib, to_pdf

def esc(t): return lib.esc(t) if isinstance(t, str) else t

def P(label, q, marks, ans, opts=None, fig=None):
    return dict(label=label, q=q, marks=marks, ans=ans, opts=opts, fig=fig)

def Q(q, marks, ans="", opts=None, fig=None, parts=None, passage=None, alt=None):
    if parts: assert sum(p["marks"] for p in parts) == marks, (q[:40], marks, [p["marks"] for p in parts])
    if alt: assert alt["marks"] == marks, "OR alternative must carry the same marks"
    if opts: assert len(opts) == 4
    return dict(q=q, marks=marks, ans=ans, opts=opts, fig=fig, parts=parts, passage=passage, alt=alt)

def sec(title, marks, items, note=""):
    assert sum(i["marks"] for i in items) == marks, (title, marks, sum(i["marks"] for i in items))
    return dict(title=title, marks=marks, items=items, note=note)

CSS5 = """
.q5{margin:3px 0 3px;break-inside:avoid;page-break-inside:avoid}
.q5 .row{display:grid;grid-template-columns:26px 1fr 34px;column-gap:4px}
.q5 .no{font-weight:700;color:#13286b}.q5 .mk5{font-weight:700;color:#c49a3c;text-align:right;font-size:8.8pt;white-space:nowrap}
.pas{border:1px solid #c9d2e6;background:#f7f9fd;border-radius:4px;padding:3px 8px;margin:2px 0 3px 26px;font-size:.96em;break-inside:auto}
.prt{margin:1px 0 1px 26px;display:grid;grid-template-columns:24px 1fr 28px;column-gap:3px;break-inside:avoid}
.prt .pm{text-align:right;color:#c49a3c;font-weight:700;font-size:8.4pt}
.o5{display:grid;grid-template-columns:repeat(4,1fr);column-gap:8px;margin-top:1px}.o5.c2{grid-template-columns:repeat(2,1fr)}.o5.c1{grid-template-columns:1fr}
.o5 span b{color:#13286b;margin-right:3px}
.ans{color:#0b6b2c;font-size:.95em;margin:1px 0 1px 26px;padding-left:6px;border-left:2px solid #7bbf8e;background:#f3fbf5}
.ans.p{margin-left:50px}
.or5{text-align:center;color:#c49a3c;font-weight:700;letter-spacing:2px;font-size:8.6pt;margin:1px 0}
.fig5{margin:2px 0 2px 26px}.fig5 svg{max-width:100%;height:auto}
.sec5n{font-weight:400;font-size:8pt;opacity:.9;margin-left:8px}
.hi{font-family:'Nirmala UI','Noto Sans Devanagari','Mangal',Arimo,sans-serif}
table.t5{border-collapse:collapse;margin:3px 0 3px 26px;font-size:.95em}table.t5 th,table.t5 td{border:1px solid #9aa7c7;padding:1px 8px;text-align:center}table.t5 th{background:#e8edf8}
"""

def _opts(opts):
    plain = max(len(_h.unescape(o)) for o in opts)
    cls = "" if plain <= 14 else (" c2" if plain <= 40 else " c1")
    return f"<div class='o5{cls}'>" + "".join(f"<span><b>({l})</b>{esc(o)}</span>" for l, o in zip("abcd", opts)) + "</div>"

def _fig(f): return f"<div class='fig5'>{f}</div>" if f else ""

def _item(n, it, solved, hi=False):
    h = ""
    def one(num, x, solved, lead=True):
        o = f"<div class='q5'><div class='row'><div class='no'>{num}</div><div>"
        if x.get("passage"): o += ""
        o += esc(x["q"]) if x["q"] else ""
        if x.get("opts"): o += _opts(x["opts"])
        o += "</div>" + (f"<div class='mk5'>[{x['marks']}]</div>" if lead else "<div></div>") + "</div>"
        if x.get("passage"): o += f"<div class='pas'>{x['passage']}</div>"
        o += _fig(x.get("fig"))
        if x.get("parts"):
            for p in x["parts"]:
                o += f"<div class='prt'><div><b>{esc(p['label'])}</b></div><div>{esc(p['q'])}" + (_opts(p['opts']) if p.get('opts') else "") + f"{_fig(p.get('fig'))}</div><div class='pm'>{p['marks']}</div></div>"
                if solved and p["ans"]: o += f"<div class='ans p'><b>Ans.</b> {p['ans']}</div>"
        if solved and x.get("ans"): o += f"<div class='ans'><b>Ans.</b> {x['ans']}</div>"
        return o + "</div>"
    h += one(f"{n}.", it, solved)
    if it.get("alt"):
        h += "<div class='or5'>— OR —</div>" + one("", it["alt"], solved, lead=False)
    return h

def page_html(meta, sections, solved):
    hi = meta["subject"] == "Hindi"
    h = lib.head(f"Class 5 {meta['subject']} Model Paper {meta['set_no']}").replace("<style>", "<style>" + CSS5, 1)
    h = h.replace("<main>", "<main class='hi'>" if hi else "<main>", 1) + lib.BRAND
    name = {"Maths": "MATHEMATICS", "English": "ENGLISH", "Hindi": "HINDI", "EVS": "ENVIRONMENTAL STUDIES"}[meta["subject"]]
    tag = "SOLVED" if solved else "UNSOLVED"
    h += (f"<div class='ttl'><div class='t'>CLASS V — {name} · MODEL PAPER {meta['set_no']:02d} <span class='setpill'>{tag}</span></div>"
          f"<div class='c'>Learning-Level Evaluation Pattern (RSCERT) &nbsp;|&nbsp; Session 2026–27</div></div>")
    h += (f"<div class='tm'><span>Time: {meta['time']}</span><span class='mid'>Name: ____________________ &nbsp; Roll No.: ________</span>"
          f"<span>Maximum Marks: {meta['marks']}</span></div>")
    h += "<div class='gi'><b>General Instructions:</b><ol>" + "".join(f"<li>{i}</li>" for i in meta["instr"]) + "</ol></div>"
    n = 1
    for s in sections:
        h += f"<div class='sec'><span>{s['title']}<span class='sec5n'>{s['note']}</span></span><span class='pill'>Marks {s['marks']}</span></div>"
        for it in s["items"]:
            h += _item(n, it, solved, hi); n += 1
    h += f"<div class='end'><span>END OF QUESTION PAPER</span><span class='pill'>Total: {meta['marks']} Marks</span></div>"
    return h + lib.TAIL

import re as _re
def _plain(t, n=90):
    t = _re.sub(r"<[^>]+>", " ", t or ""); t = _h.unescape(_re.sub(r"\s+", " ", t)).strip()
    return (t[:n] + "…") if len(t) > n else t

def key_html(meta, sections):
    """Stand-alone answer key: question number, marks, short question stem, model answer."""
    hi = meta["subject"] == "Hindi"
    h = lib.head(f"Class 5 {meta['subject']} Model Paper {meta['set_no']} Answer Key").replace("<style>", "<style>" + CSS5, 1)
    h = h.replace("<main>", "<main class='hi'>" if hi else "<main>", 1) + lib.BRAND
    name = {"Maths": "MATHEMATICS", "English": "ENGLISH", "Hindi": "HINDI", "EVS": "ENVIRONMENTAL STUDIES"}[meta["subject"]]
    h += (f"<div class='ttl'><div class='t'>CLASS V — {name} · MODEL PAPER {meta['set_no']:02d} <span class='setpill'>ANSWER KEY</span></div>"
          f"<div class='c'>Answers and marking points &nbsp;|&nbsp; Maximum Marks: {meta['marks']}</div></div>")
    rows = lambda it, n, ans_only=False: ""
    n = 1
    for s in sections:
        h += f"<div class='sec'><span>{s['title']}</span><span class='pill'>Marks {s['marks']}</span></div>"
        h += "<table class='ak'><tr><th style='width:30px'>Q.</th><th style='width:34px'>Marks</th><th>Answer / marking points</th></tr>"
        for it in s["items"]:
            def block(x, num, tag=""):
                out = f"<tr><td class='n'>{num}</td><td class='m'>{x['marks']}</td><td>{tag}<span style='color:#777;font-size:.9em'>{esc(_plain(x['q']))}</span>"
                if x.get("opts") and x.get("ans"): out += f"<div><b>{x['ans']}</b></div>"
                elif x.get("ans") and not x.get("parts"): out += f"<div>{x['ans']}</div>"
                for p in x.get("parts") or []:
                    out += f"<div style='margin-top:2px'><b>{esc(p['label'])}</b> <span style='color:#777;font-size:.9em'>{esc(_plain(p['q'], 60))}</span> <span style='color:#c49a3c'>[{p['marks']}]</span><div style='color:#0b6b2c'>{p['ans']}</div></div>"
                if x.get("parts") and x.get("ans"): out += f"<div style='color:#0b6b2c'>{x['ans']}</div>"
                return out + "</td></tr>"
            h += block(it, n)
            if it.get("alt"): h += block(it["alt"], "OR", "<span class='orlab'>OR </span>")
            n += 1
        h += "</table>"
    h += f"<div class='end'><span>END OF ANSWER KEY</span><span class='pill'>Total: {meta['marks']} Marks</span></div>"
    return h + lib.TAIL

SEQ = {  # marks of Q1..Q22 per subject (RSCERT PELLE blueprint read from the supplied sample papers)
    "Maths":   [1, 6, 6, 8, 1, 1, 1, 6, 1, 3, 3, 6, 6, 6, 3, 3, 3, 8, 1, 1, 3, 3],
    "English": [1] * 7 + [2, 2, 3, 5, 8, 5, 2] + [5] * 6 + [8, 8],
    "Hindi":   [1, 1, 1, 1, 1, 3, 3, 3, 8, 1, 3, 6, 3, 1, 3, 3, 6, 6, 6, 6, 6, 8],
    "EVS":     [1, 1, 3, 6, 1, 3, 8, 1, 1, 3, 3, 3, 3, 6, 8, 6, 6, 1, 3, 6, 1, 6],
}
def check(meta, sections):
    items = [i for s in sections for i in s["items"]]
    got = [i["marks"] for i in items]
    assert sum(got) == meta["marks"] == 80, f"total marks {sum(got)}"
    assert got == SEQ[meta["subject"]], f"marks per question {got} != blueprint {SEQ[meta['subject']]}"
    for i in items:
        if i.get("opts"): assert i["ans"], "MCQ needs an answer"
    return True

def _chrome():
    c = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"
    if os.path.exists(c): return c
    if os.environ.get("CHROMIUM_PATH"): return os.environ["CHROMIUM_PATH"]
    g = sorted(glob.glob(os.path.expanduser("~/AppData/Local/ms-playwright/chromium-*/chrome-win*/chrome.exe")))
    return g[-1] if g else None

def build(meta, sections, outdir=None):
    check(meta, sections)
    repo = HERE.parents[1]
    out = Path(outdir) if outdir else repo / "Class_05" / meta["subject"] / "Model_Papers"
    out.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright
    last = None
    for attempt in range(5):
        try:
            with sync_playwright() as p:
                br = p.chromium.launch(executable_path=_chrome()); pg = br.new_page()
                for solved in (False, True):
                    stem = f"Model_Paper_{meta['set_no']:02d}" + ("_Solved" if solved else "")
                    to_pdf(pg, page_html(meta, sections, solved), out / f"{stem}.pdf",
                           f"Mastermind Coaching Classes — Class 5 {meta['subject']} · Model Paper {meta['set_no']:02d} · {'Solved' if solved else 'Unsolved'}")
                to_pdf(pg, key_html(meta, sections), out / f"Model_Paper_{meta['set_no']:02d}_Answer_Key.pdf",
                       f"Mastermind Coaching Classes — Class 5 {meta['subject']} · Model Paper {meta['set_no']:02d} · Answer Key")
                br.close()
            break
        except OSError as e:
            last = e
    else:
        raise last
    from pypdf import PdfReader
    return {s: len(PdfReader(str(out / f"Model_Paper_{meta['set_no']:02d}{s}.pdf")).pages) for s in ("", "_Solved", "_Answer_Key")}

# ---------------- small SVG helpers (Class 5) ----------------
def svg_numberline(a, b, step=1, marks=None, w=320, label_every=1, circles=()):
    """number line from a to b; marks = {value: label} extra labels; circles = values to circle (blank boxes)."""
    n = int(round((b - a) / step)); x0, x1 = 15, w - 15; dx = (x1 - x0) / n
    s = f"<svg width='{w}' height='46' viewBox='0 0 {w} 46' xmlns='http://www.w3.org/2000/svg'><line x1='{x0-8}' y1='20' x2='{x1+8}' y2='20' stroke='#222' stroke-width='1.4'/>"
    for i in range(n + 1):
        v = a + i * step; x = x0 + i * dx
        s += f"<line x1='{x:.1f}' y1='15' x2='{x:.1f}' y2='25' stroke='#222'/>"
        if i % label_every == 0 and v not in circles: s += f"<text x='{x:.1f}' y='38' font-size='10' text-anchor='middle'>{v}</text>"
        if v in circles: s += f"<circle cx='{x:.1f}' cy='8' r='6' fill='none' stroke='#13286b'/>"
    return s + "</svg>"

def svg_bars(labels, values, w=300, h=150, ylabel="", maxv=None):
    maxv = maxv or max(values); n = len(values); L, B, T = 34, h - 24, 10; bw = (w - L - 10) / n * 0.55
    s = f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'><line x1='{L}' y1='{T}' x2='{L}' y2='{B}' stroke='#222'/><line x1='{L}' y1='{B}' x2='{w-5}' y2='{B}' stroke='#222'/>"
    for k in range(0, maxv + 1):
        y = B - (B - T) * k / maxv; s += f"<line x1='{L-3}' y1='{y:.1f}' x2='{L}' y2='{y:.1f}' stroke='#222'/><text x='{L-6}' y='{y+3:.1f}' font-size='8' text-anchor='end'>{k}</text>"
        if k: s += f"<line x1='{L}' y1='{y:.1f}' x2='{w-5}' y2='{y:.1f}' stroke='#e3e8f3'/>"
    for i, (lb, v) in enumerate(zip(labels, values)):
        cx = L + (w - L - 10) * (i + 0.5) / n; y = B - (B - T) * v / maxv
        s += f"<rect x='{cx-bw/2:.1f}' y='{y:.1f}' width='{bw:.1f}' height='{B-y:.1f}' fill='#4a6fc4'/><text x='{cx:.1f}' y='{B+12}' font-size='9' text-anchor='middle'>{lb}</text>"
    if ylabel: s += f"<text x='8' y='{T+4}' font-size='8'>{ylabel}</text>"
    return s + "</svg>"

def svg_angle(deg, w=170, h=110, label=True):
    import math
    ox, oy, r = 20, h - 18, 90; t = math.radians(deg)
    x2, y2 = ox + r * math.cos(t), oy - r * math.sin(t)
    s = f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'><line x1='{ox}' y1='{oy}' x2='{ox+r}' y2='{oy}' stroke='#222' stroke-width='1.6'/><line x1='{ox}' y1='{oy}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='#222' stroke-width='1.6'/>"
    s += f"<path d='M {ox+22} {oy} A 22 22 0 0 0 {ox+22*math.cos(t):.1f} {oy-22*math.sin(t):.1f}' fill='none' stroke='#c49a3c' stroke-width='1.4'/>"
    if label: s += f"<text x='{ox+26}' y='{oy-8}' font-size='10'>{deg}°</text>"
    return s + "</svg>"

def svg_grid(cells, cw=16, w=None, h=None, shade="#9db6ea"):
    """cells = set of (col,row) shaded squares on a grid (row 0 at top)."""
    W = max(c for c, r in cells) + 1; H = max(r for c, r in cells) + 1
    s = f"<svg width='{W*cw+4}' height='{H*cw+4}' xmlns='http://www.w3.org/2000/svg'>"
    for c, r in cells: s += f"<rect x='{c*cw+2}' y='{r*cw+2}' width='{cw}' height='{cw}' fill='{shade}' stroke='#13286b'/>"
    return s + "</svg>"
