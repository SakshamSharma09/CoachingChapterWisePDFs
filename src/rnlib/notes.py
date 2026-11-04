"""Mastermind Revision Notes renderer (style of the Class 8 reference notes).

Content model (plain Python data, one dict per chapter):
  dict(num=1, title="...", tag="Geography & Economics" (optional), intro="...",
       big_questions=[...] (optional), blocks=[...], takeaways=[...])
Blocks (tuples):
  ("h2", "1.1 Section title")      main section heading (gold bar)
  ("h3", "Sub-heading")            small gold-arrow sub heading
  ("p", "paragraph text")
  ("ul", ["bullet", ...])          bullets
  ("ol", ["step", ...])            numbered list
  ("table", ["Col1", "Col2"], [["a", "b"], ...])
  ("note", "NOTE" | "IMPORTANT" | "FORMULA" | "DEFINITION" | "REMEMBER", "text")
  ("steps", [("Step 1 — title", "text"), ...])
  ("qa", [("question", "answer"), ...])        quick Q&A table (likely exam questions)
Inline markup in any text: **bold**, *italic*, and plain HTML like <sub>2</sub>, <sup>2</sup>, &rarr; are allowed.
Write a literal < or & as &lt; / &amp;.
"""
import re, html, os
from playwright.sync_api import sync_playwright

NAVY, GOLD = "#0f2347", "#c9a227"

CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm; }
*{box-sizing:border-box}
body{font-family:'Arimo','Liberation Sans',Arial,sans-serif;font-size:10.4pt;line-height:1.42;color:#1d2433;margin:0}
b{color:#0f2347}
.cover{page-break-after:always;padding-top:26mm}
.cover .brand{letter-spacing:.14em;font-weight:700;color:#0f2347;font-size:13pt;border-bottom:3px solid #c9a227;display:inline-block;padding-bottom:4px}
.cover h1{font-size:34pt;margin:22mm 0 2mm;color:#0f2347}
.cover h2{font-size:17pt;margin:0 0 3mm;color:#0f2347;font-weight:600}
.cover .sub{font-size:12pt;color:#444;margin-bottom:10mm}
.how{border-left:4px solid #c9a227;background:#f6f3e6;padding:3mm 5mm;margin:8mm 0;font-size:10pt}
.how .t{letter-spacing:.1em;font-weight:700;color:#7a6200;font-size:9pt;margin-bottom:1mm}
table{border-collapse:collapse;width:100%;margin:2.5mm 0 3.5mm;font-size:9.6pt;page-break-inside:auto}
tr{page-break-inside:avoid}
th{background:#0f2347;color:#fff;text-align:left;padding:1.6mm 2.4mm;font-weight:700}
td{border:1px solid #ccd2de;padding:1.5mm 2.4mm;vertical-align:top}
tbody tr:nth-child(even) td{background:#f3f5fa}
td:first-child{color:#0f2347;font-weight:600}
.toc td:first-child{width:14mm;text-align:center}
.chap{page-break-before:always}
.chap:first-of-type{page-break-before:avoid}
.chh{background:#0f2347;border-left:5px solid #c9a227;color:#fff;padding:3.2mm 5mm;margin-bottom:3.5mm;border-radius:2px;page-break-after:avoid}
.chh .k{color:#c9a227;letter-spacing:.2em;font-size:8.6pt;font-weight:700}
.chh .tt{font-size:17pt;font-weight:700;margin-top:1mm;line-height:1.2}
.intro{font-style:italic;border:1px solid #c9a227;border-width:1px 0;background:#f6f7fb;padding:2.4mm 3.4mm;margin:0 0 3.4mm}
h2{font-size:13.4pt;color:#0f2347;border-left:4px solid #c9a227;padding-left:2.6mm;margin:5.5mm 0 2mm;page-break-after:avoid}
h3{font-size:11pt;color:#0f2347;margin:3.6mm 0 1.2mm;page-break-after:avoid}
h3:before{content:'▸ ';color:#c9a227}
p{margin:0 0 2.1mm;text-align:justify}
ul,ol{margin:0 0 2.6mm 5mm;padding-left:4mm}
li{margin:0 0 1.1mm}
ul li::marker{color:#c9a227}
.box{border-left:4px solid #0f2347;background:#eef1f8;padding:2.2mm 3.4mm;margin:2.8mm 0;page-break-inside:avoid}
.box .l{font-size:8pt;letter-spacing:.14em;font-weight:700;color:#7a6200;margin-bottom:.8mm}
.box.formula{background:#fff8dc;border-left-color:#c9a227}
.box.important{background:#fdf3e4;border-left-color:#c9a227}
.step{border-left:3px solid #c9a227;padding-left:3mm;margin:2mm 0;page-break-inside:avoid}
.step .s{font-weight:700;color:#0f2347}
.tk{background:#0f2347;color:#fff;border-radius:2px;padding:3.4mm 5mm;margin-top:5mm;page-break-inside:avoid}
.tk .t{color:#c9a227;font-weight:700;letter-spacing:.12em;margin-bottom:1.5mm}
.tk ul{margin-bottom:0}
.tk li::marker{color:#c9a227}
.tk b{color:#ffd966}
.bq{background:#f6f7fb;padding:2.4mm 4mm;margin:0 0 3mm}
"""

def fmt(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s, flags=re.S)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s, flags=re.S)
    return s

def render_block(b):
    k = b[0]
    if k == "h2": return f"<h2>{fmt(b[1])}</h2>"
    if k == "h3": return f"<h3>{fmt(b[1])}</h3>"
    if k == "p": return f"<p>{fmt(b[1])}</p>"
    if k == "ul": return "<ul>" + "".join(f"<li>{fmt(x)}</li>" for x in b[1]) + "</ul>"
    if k == "ol": return "<ol>" + "".join(f"<li>{fmt(x)}</li>" for x in b[1]) + "</ol>"
    if k == "table":
        hd = "".join(f"<th>{fmt(x)}</th>" for x in b[1])
        rows = "".join("<tr>" + "".join(f"<td>{fmt(c)}</td>" for c in r) + "</tr>" for r in b[2])
        return f"<table><thead><tr>{hd}</tr></thead><tbody>{rows}</tbody></table>"
    if k == "note":
        cls = {"FORMULA": "formula", "IMPORTANT": "important"}.get(b[1].upper(), "")
        return f"<div class='box {cls}'><div class='l'>{b[1].upper()}</div>{fmt(b[2])}</div>"
    if k == "steps":
        return "".join(f"<div class='step'><div class='s'>{fmt(t)}</div>{fmt(x)}</div>" for t, x in b[1])
    if k == "qa":
        rows = "".join(f"<tr><td>{fmt(q)}</td><td>{fmt(a)}</td></tr>" for q, a in b[1])
        return f"<table><thead><tr><th style='width:42%'>Likely question</th><th>Model answer</th></tr></thead><tbody>{rows}</tbody></table>"
    raise ValueError(k)

def chapter_html(ch, label):
    tag = ch.get("tag")
    k = f"CHAPTER {ch['num']:02d}" + (f" · {tag.upper()}" if tag else "")
    h = f"<section class='chap'><div class='chh'><div class='k'>{k}</div><div class='tt'>{fmt(ch['title'])}</div></div>"
    if ch.get("intro"): h += f"<div class='intro'>{fmt(ch['intro'])}</div>"
    if ch.get("big_questions"):
        h += "<h2>Big Questions</h2><ul>" + "".join(f"<li>{fmt(x)}</li>" for x in ch["big_questions"]) + "</ul>"
    for b in ch["blocks"]: h += render_block(b)
    if ch.get("takeaways"):
        h += "<div class='tk'><div class='t'>★ KEY TAKEAWAYS</div><ul>" + "".join(f"<li>{fmt(x)}</li>" for x in ch["takeaways"]) + "</ul></div>"
    return h + "</section>"

def book_html(meta, chapters):
    toc = "".join(f"<tr><td>{c['num']}</td><td>{fmt(c['title'])}</td><td>{fmt(c.get('theme',''))}</td></tr>" for c in chapters)
    cover = f"""<div class='cover'><div class='brand'>THE MASTERMIND COACHING CLASSES</div>
<h1>Revision Notes</h1><h2>{meta['title']}</h2><div class='sub'>{meta['sub']}</div>
<div class='how'><div class='t'>HOW TO USE THESE NOTES</div>{meta.get('how','Each chapter follows the textbook\'s own order of sections, so you can read straight through. Bold words are keywords you must be able to define. Tables compare and classify; shaded boxes hold definitions, formulas and key facts. The navy Key Takeaways box at the end of every chapter is your last-two-minutes revision.')}</div>
<table class='toc'><thead><tr><th>CH.</th><th>CHAPTER TITLE</th><th>CORE THEME</th></tr></thead><tbody>{toc}</tbody></table>
<p style='margin-top:10mm;font-size:9pt;color:#555'>The Mastermind Coaching Classes — Road No. 5, VKIA, Jaipur — 9887258679</p></div>"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{cover}" + "".join(chapter_html(c, meta['label']) for c in chapters) + "</body></html>"

def build_pdf(meta, chapters, out):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    h = book_html(meta, chapters)
    with sync_playwright() as p:
        br = p.chromium.launch(**({'executable_path': os.environ['CHROMIUM_PATH']} if os.environ.get('CHROMIUM_PATH') else {})); pg = br.new_page()
        pg.set_content(h, wait_until="load")
        foot = f"<div style='width:100%;font-size:7.5pt;color:#666;text-align:center;font-family:Arial'>Mastermind Coaching Classes · {meta['label']} &nbsp;|&nbsp; Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>"
        pg.pdf(path=out, format="A4", print_background=True, display_header_footer=True, header_template="<div></div>", footer_template=foot,
               margin=dict(top="16mm", bottom="17mm", left="15mm", right="15mm"))
        br.close()
    return out

def check_chapters(chapters):
    """Structural sanity check; raises on problems."""
    bad = []
    for c in chapters:
        for key in ("num", "title", "intro", "blocks", "takeaways"):
            if key not in c: bad.append((c.get("num"), "missing " + key))
        nh = sum(1 for b in c["blocks"] if b[0] == "h2")
        if nh < 3: bad.append((c["num"], "too few sections"))
        txt = " ".join(str(b) for b in c["blocks"])
        if "$" in txt or "\\(" in txt: bad.append((c["num"], "LaTeX/$ found"))
        for b in c["blocks"]:
            if b[0] not in ("h2", "h3", "p", "ul", "ol", "table", "note", "steps", "qa"): bad.append((c["num"], "bad block " + b[0]))
            if b[0] == "table":
                w = len(b[1])
                for r in b[2]:
                    if len(r) != w: bad.append((c["num"], "table width mismatch: " + str(r)[:40]))
    if bad: raise AssertionError(bad)
