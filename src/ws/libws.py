"""Chapter worksheet (about 50 graded questions) + detailed chapter notes builder.

A chapter file  src/ws/<bank>_ws.py  (e.g. c9m_ch02_ws.py) contains
    WS = [W(...), ...]            ~50 questions (see W below)
    CH = dict(num=.., title=.., intro=.., blocks=[...], takeaways=[...])    detailed notes (rnlib/notes.py content model)
and ends with
    if __name__ == "__main__": run(__file__, "c9m_ch02", 9, "Maths", WS, CH)
run() writes, under Class_NN/<Subject>/:
    Worksheets/ChNN_<slug>_Worksheet.pdf            questions only (no answer lines)
    Worksheets/ChNN_<slug>_Worksheet_Answer_Key.pdf  answers / solutions with marks
    Chapter_Notes/ChNN_<slug>_Chapter_Notes.pdf     detailed notes
Question item:  W(q, marks, ans, level, opts=None, fig=None, wp=False)
    level 'E' | 'M' | 'H'  (easy / medium / hard);  wp=True marks a word / application problem (printed tag)
    opts  4 option strings for an MCQ (1 mark); ans for an MCQ is '(b) text'
"""
import sys, os, re, glob, html as _h
from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "src" / "graded")); sys.path.insert(0, str(REPO / "src" / "rnlib")); sys.path.insert(0, str(REPO / "src" / "rn_work"))
import common                                    # noqa: E402  (Windows-safe KaTeX asset paths)
from common import lib, to_pdf                   # noqa: E402

LEVELS = {"E": ("EASY", "#1b7f3b", "#e7f6ec"), "M": ("MEDIUM", "#b36b00", "#fff3dc"), "H": ("HARD", "#b3261e", "#fdecea")}
SUBJ_TITLE = {"Maths": "MATHEMATICS", "Science": "SCIENCE", "Social_Science": "SOCIAL SCIENCE", "English": "ENGLISH", "Hindi": "HINDI"}
MIN_WP = {"Maths": 12, "Science": 8, "Social_Science": 0, "English": 0, "Hindi": 0}

def W(q, marks, ans, level, opts=None, fig=None, wp=False):
    assert level in LEVELS, level
    if opts:
        assert len(opts) == 4 and marks == 1, "MCQ: 4 options and 1 mark"
        assert re.match(r"\([abcd]\)", ans), "MCQ answer must start with (a)/(b)/(c)/(d)"
    assert ans and q, "question and answer required"
    return dict(q=q, marks=marks, ans=ans, level=level, opts=opts, fig=fig, wp=wp)

CSSW = """
.wq{display:grid;grid-template-columns:26px 1fr 40px;column-gap:4px;margin:3px 0 3px;break-inside:avoid;page-break-inside:avoid}
.wq .no{font-weight:700;color:#13286b}.wq .mk{text-align:right;font-weight:700;color:#c49a3c;font-size:8.8pt;white-space:nowrap}
.bd{display:inline-block;font-size:7pt;font-weight:700;letter-spacing:.6px;border-radius:8px;padding:0 6px;margin-right:5px;vertical-align:1px}
.wp{display:inline-block;font-size:7pt;font-weight:700;color:#13286b;border:1px solid #13286b;border-radius:8px;padding:0 5px;margin-right:5px;vertical-align:1px}
.o5{display:grid;grid-template-columns:repeat(4,1fr);column-gap:8px;margin-top:1px}.o5.c2{grid-template-columns:repeat(2,1fr)}.o5.c1{grid-template-columns:1fr}
.o5 span b{color:#13286b;margin-right:3px}
.lg{display:flex;gap:10px;align-items:center;font-size:8.4pt;margin:3px 0 2px;color:#333}
.stat{display:flex;justify-content:space-between;border:1px solid #13286b;background:#f2f5fb;padding:3px 9px;font-weight:700;color:#13286b;font-size:9pt;margin:5px 0 4px}
.fig5{margin:2px 0}.fig5 svg{max-width:100%;height:auto}
.hi{font-family:'Nirmala UI','Noto Sans Devanagari','Mangal',Arimo,sans-serif}
table.ak td.lv{width:46px;text-align:center;font-weight:700;font-size:7.6pt}
"""

def _opts(opts):
    L = max(len(_h.unescape(re.sub(r"\$[^$]*\$", "xxxxxx", o))) for o in opts)
    cls = "" if L <= 16 else (" c2" if L <= 40 else " c1")
    return f"<div class='o5{cls}'>" + "".join(f"<span><b>({l})</b>{lib.esc(o)}</span>" for l, o in zip("abcd", opts)) + "</div>"

def _split_parts(txt):
    txt = re.sub(r"\s\((ii|iii|iv|v|vi)\)\s", r"<br>(\1) ", txt)
    return re.sub(r"\s\(i\)\s", r"<br>(i) ", txt) if "(ii)" in txt else txt

def _stats(ws):
    n = {k: sum(1 for w in ws if w["level"] == k) for k in LEVELS}
    m = {k: sum(w["marks"] for w in ws if w["level"] == k) for k in LEVELS}
    return n, m, sum(m.values()), sum(1 for w in ws if w["wp"])

def check_ws(ws, subject):
    n, m, tot, wp = _stats(ws)
    assert 48 <= len(ws) <= 56, f"{len(ws)} questions (need about 50)"
    for k in LEVELS: assert n[k] >= 10, f"level {k} has only {n[k]} questions"
    assert wp >= MIN_WP[subject], f"{wp} word/application problems; need >= {MIN_WP[subject]} for {subject}"
    for w in ws:
        if w["level"] == "E": assert w["marks"] in (1, 2), ("easy marks", w["q"][:40])
        if w["level"] == "M": assert w["marks"] in (1, 2, 3), ("medium marks", w["q"][:40])
        if w["level"] == "H": assert w["marks"] in (2, 3, 4, 5), ("hard marks", w["q"][:40])
    seen = set()
    for w in ws:
        key = re.sub(r"\W+", "", w["q"] + "|".join(w["opts"] or []))
        assert key not in seen, ("duplicate question", w["q"][:50]); seen.add(key)
    return n, m, tot, wp

def worksheet_html(meta, ws, key=False):
    hi = meta["subject"] == "Hindi"
    h = lib.head(f"{meta['name']} worksheet").replace("<style>", "<style>" + CSSW, 1)
    h = h.replace("<main>", "<main class='hi'>" if hi else "<main>", 1) + lib.BRAND
    n, m, tot, wp = _stats(ws)
    title = f"CLASS {meta['cls']} — {SUBJ_TITLE[meta['subject']]} · CHAPTER {meta['chno']} {'ANSWER KEY' if key else 'WORKSHEET'}"
    h += (f"<div class='ttl'><div class='t'>{title}</div><div class='c'>Chapter {meta['chno']}: <b>{lib.esc(meta['name'])}</b> &nbsp;|&nbsp; Session 2026–27</div></div>")
    h += (f"<div class='stat'><span>Questions: {len(ws)}</span><span>Total marks: {tot}</span>"
          f"<span>Easy {n['E']} ({m['E']}m) · Medium {n['M']} ({m['M']}m) · Hard {n['H']} ({m['H']}m)</span><span>Word / application problems: {wp}</span></div>")
    if not key:
        h += ("<div class='lg'><b>Level:</b>" + "".join(f"<span class='bd' style='background:{LEVELS[k][2]};color:{LEVELS[k][1]};border:1px solid {LEVELS[k][1]}'>{LEVELS[k][0]}</span>" for k in "EMH") +
              "<span>Marks are shown at the right of every question. Attempt the parts in order; show your working.</span></div>")
    num = 0
    for k in "EMH":
        part = [(i, w) for i, w in enumerate(ws, 1) if w["level"] == k]
        label, col, bg = LEVELS[k]
        h += f"<div class='sec'><span>PART {'ABC'['EMH'.index(k)]} — {label} LEVEL</span><span class='pill'>{len(part)} questions · {sum(w['marks'] for _, w in part)} marks</span></div>"
        if key:
            h += "<table class='ak'><tr><th style='width:30px'>Q.</th><th style='width:46px'>Level</th><th style='width:34px'>Marks</th><th>Answer / solution</th></tr>"
            for i, w in part:
                h += f"<tr><td class='n'>{i}</td><td class='lv' style='color:{col};background:{bg}'>{label}</td><td class='m'>{w['marks']}</td><td>{w['ans']}</td></tr>"
            h += "</table>"
        else:
            for i, w in part:
                tags = f"<span class='bd' style='background:{bg};color:{col};border:1px solid {col}'>{label}</span>" + ("<span class='wp'>WORD PROBLEM</span>" if w["wp"] else "")
                body = tags + _split_parts(lib.esc(w["q"]))
                if w["opts"]: body += _opts(w["opts"])
                if w["fig"]: body += f"<div class='fig5'>{w['fig']}</div>"
                h += f"<div class='wq'><div class='no'>{i}.</div><div>{body}</div><div class='mk'>[{w['marks']}]</div></div>"
    h += f"<div class='end'><span>{'END OF ANSWER KEY' if key else 'END OF WORKSHEET'}</span><span class='pill'>Total: {tot} marks</span></div>"
    return h + lib.TAIL

# ---- notes -----------------------------------------------------------------
_SUP = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿᵐ", "0123456789-+nm")); _SUB = dict(zip("₀₁₂₃₄₅₆₇₈₉₊₋ₙ", "0123456789+-n"))
_RS = re.compile("[" + "".join(_SUP) + "]+"); _RB = re.compile("[" + "".join(_SUB) + "]+")
def _fix(x):
    if isinstance(x, str):
        x = _RS.sub(lambda m: "<sup>" + "".join(_SUP[c] for c in m.group()).replace("-", "&minus;") + "</sup>", x)
        return _RB.sub(lambda m: "<sub>" + "".join(_SUB[c] for c in m.group()).replace("-", "&minus;") + "</sub>", x)
    if isinstance(x, (list, tuple)): return type(x)(_fix(i) for i in x)
    if isinstance(x, dict): return {k: _fix(v) for k, v in x.items()}
    return x

def check_notes(ch):
    import notes
    notes.check_chapters([ch])
    words = len(re.sub(r"<[^>]+>", " ", " ".join(str(b) for b in ch["blocks"])).split())
    nh = sum(1 for b in ch["blocks"] if b[0] == "h2")
    assert nh >= 6, f"only {nh} sections; detailed notes need >= 6"
    assert words >= 1400, f"only ~{words} words; detailed notes need >= 1400"
    assert len(ch["takeaways"]) >= 6, "need >= 6 key takeaways"
    return words, nh

def notes_pdf(ch, meta, out, pg):
    import notes
    ch = _fix(ch)
    body = notes.chapter_html(ch, meta["label"])
    css = notes.CSS + ".hd2{font-size:8.6pt;color:#555;border-bottom:1.5px solid #c9a227;padding-bottom:1mm;margin-bottom:3mm;letter-spacing:.06em}"
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>"
            f"<div class='hd2'><b>THE MASTERMIND COACHING CLASSES</b> &nbsp;·&nbsp; {meta['label']} &nbsp;·&nbsp; Detailed chapter notes</div>{body}</body></html>")
    pg.set_content(html, wait_until="load")
    foot = (f"<div style='width:100%;font-size:7.5pt;color:#666;text-align:center;font-family:Arial'>Mastermind Coaching Classes · {meta['label']} &nbsp;|&nbsp; Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>")
    pg.pdf(path=str(out), format="A4", print_background=True, display_header_footer=True, header_template="<div></div>", footer_template=foot,
           margin=dict(top="16mm", bottom="17mm", left="15mm", right="15mm"))

def _chrome():
    c = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"
    if os.path.exists(c): return c
    if os.environ.get("CHROMIUM_PATH"): return os.environ["CHROMIUM_PATH"]
    g = sorted(glob.glob(os.path.expanduser("~/AppData/Local/ms-playwright/chromium-*/chrome-win*/chrome.exe")))
    return g[-1] if g else None

def run(file, bank, cls, subject, WS=None, CH=None, only=None):
    """Build worksheet + key + notes for one chapter. WS / CH may be None to skip that part."""
    import importlib
    mod = importlib.import_module(bank)
    slug, name, chno = mod.SLUG, mod.NAME, mod.CHNO
    meta = dict(cls=cls, subject=subject, chno=chno, name=name, label=f"Class {cls} {subject.replace('_', ' ')} · Ch {chno}: {name}")
    base = REPO / f"Class_{cls:02d}" / subject
    stem = f"Ch{chno:02d}_{slug}"
    info = {}
    if WS is not None: info["ws"] = check_ws(WS, subject)
    if CH is not None: info["notes"] = check_notes(_fix(CH))
    from playwright.sync_api import sync_playwright
    last = None
    for attempt in range(5):
        try:
            with sync_playwright() as p:
                br = p.chromium.launch(executable_path=_chrome()); pg = br.new_page()
                if WS is not None and only in (None, "ws"):
                    d = base / "Worksheets"; d.mkdir(parents=True, exist_ok=True)
                    to_pdf(pg, worksheet_html(meta, WS), d / f"{stem}_Worksheet.pdf", f"Mastermind Coaching Classes — {meta['label']} · Worksheet")
                    to_pdf(pg, worksheet_html(meta, WS, key=True), d / f"{stem}_Worksheet_Answer_Key.pdf", f"Mastermind Coaching Classes — {meta['label']} · Worksheet answer key")
                if CH is not None and only in (None, "notes"):
                    d = base / "Chapter_Notes"; d.mkdir(parents=True, exist_ok=True)
                    notes_pdf(CH, meta, d / f"{stem}_Chapter_Notes.pdf", pg)
                br.close()
            break
        except OSError as e:
            last = e
    else:
        raise last
    from pypdf import PdfReader
    out = {}
    for sub, nm in (("Worksheets", f"{stem}_Worksheet.pdf"), ("Worksheets", f"{stem}_Worksheet_Answer_Key.pdf"), ("Chapter_Notes", f"{stem}_Chapter_Notes.pdf")):
        f = base / sub / nm
        if f.exists(): out[nm.replace(stem + "_", "")] = len(PdfReader(str(f)).pages)
    print(bank, "OK", {k: v for k, v in info.items()}, out)
    return out
