"""One-page formula sheets (Maths / Science chapters that have FORMULAS in their extras module).
python formula_sheets.py <class> <Subject>       -> Class_NN/<Subject>/Formula_Sheets/ChNN_<slug>_Formula_Sheet.pdf
FORMULAS = [("Heading", ["line (KaTeX $...$ allowed)", ...]), ...]"""
import sys, glob, re, importlib, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common
from common import lib, to_pdf, npages
PFX = {"Maths": "m", "Science": "s"}
cls = int(sys.argv[1]); subject = sys.argv[2]
repo = Path(__file__).resolve().parents[2]
out = repo / f"Class_{cls:02d}" / subject / "Formula_Sheets"; out.mkdir(parents=True, exist_ok=True)
def _chrome():
    c = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"
    if os.path.exists(c): return c
    if os.environ.get("CHROMIUM_PATH"): return os.environ["CHROMIUM_PATH"]
    g = sorted(glob.glob(os.path.expanduser("~/AppData/Local/ms-playwright/chromium-*/chrome-win*/chrome.exe")))
    return g[-1] if g else None
def html_sheet(mod, ex, fs):
    h = lib.head(f"Formula Sheet Ch {mod.CHNO}").replace("<main>", f"<main style='--fs:{fs}pt;--lh:1.32'>") + lib.BRAND
    h += (f"<div class='ttl'><div class='t'>CLASS {cls} — {subject.upper()} · FORMULA SHEET</div>"
          f"<div class='c'>Chapter {mod.CHNO}: <b>{mod.NAME}</b> &nbsp;|&nbsp; Quick revision, one page</div></div>")
    for head, lines in ex.FORMULAS:
        h += f"<div class='sec'><span>{head}</span></div><ul style='margin:3px 0 6px 16px;padding:0'>" + "".join(f"<li style='margin:2px 0'>{lib.esc(l)}</li>" for l in lines) + "</ul>"
    return h + lib.TAIL
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    br = p.chromium.launch(executable_path=_chrome()); pg = br.new_page()
    for f in sorted(glob.glob(str(Path(__file__).parent / f"c{cls}{PFX[subject]}_ch*.py"))):
        name = Path(f).stem
        if not re.fullmatch(rf"c{cls}{PFX[subject]}_ch\d+", name): continue
        ex = common.load_extras(name)
        if not ex or not getattr(ex, "FORMULAS", None): continue
        mod = importlib.import_module(name)
        dst = out / f"Ch{mod.CHNO:02d}_{mod.SLUG}_Formula_Sheet.pdf"
        fs = 11.2
        while True:
            to_pdf(pg, html_sheet(mod, ex, fs), dst, f"Mastermind Coaching Classes — Class {cls} {subject} · Ch {mod.CHNO} · Formula Sheet")
            if npages(dst) <= 1 or fs <= 8.6: break
            fs = round(fs - 0.3, 1)
        print(dst.name, npages(dst), "page(s) @", fs)
    br.close()
