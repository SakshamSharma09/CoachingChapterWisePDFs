import re, html, os
from playwright.sync_api import sync_playwright
import lib

CSS = """
@page{size:A4}
body{font-family:Arial,Helvetica,sans-serif;font-size:9.4pt;line-height:1.38;color:#1b1b1b;margin:0}
.wm{display:none}
.cover{text-align:center;padding-top:50mm}
.cover .org{color:#13286b;font-weight:700;letter-spacing:2px;font-size:11pt}
.cover h1{color:#13286b;font-size:26pt;margin:10px 0 4px}
.cover .sub{color:#c49a3c;font-weight:700;font-size:13pt}
.cover .how{text-align:left;margin:22mm 14mm 0;border:1px solid #c9d2e6;background:#f7f9fd;padding:8px 12px;font-size:9pt}
table.toc{width:100%;border-collapse:collapse;margin-top:16px;font-size:9pt}
table.toc th{background:#13286b;color:#fff;text-align:left;padding:4px 6px}
table.toc td{border-bottom:1px solid #dde3f0;padding:4px 6px}
.ch{break-before:page;page-break-before:always}
.chh{background:#13286b;color:#fff;padding:8px 12px;border-radius:3px;margin-bottom:8px}
.chh .c{color:#c49a3c;font-size:8pt;font-weight:700;letter-spacing:1px}
.chh h2{margin:2px 0 0;font-size:15pt}
.probe{background:#1d3a8a;color:#fff;padding:6px 12px;margin-bottom:8px;border-radius:3px;font-size:8.6pt}
.probe b{color:#e6c673;letter-spacing:1px;font-size:8pt}
.probe ul{margin:3px 0 0 14px;padding:0}
h3{color:#13286b;font-size:10.8pt;margin:10px 0 3px;border-bottom:1px solid #dde3f0;padding-bottom:1px;break-after:avoid}
ul{margin:3px 0 4px 16px;padding:0}li{margin:1.5px 0}
li::marker{color:#c49a3c}
b{color:#0e2160}
.def{border-left:3px solid #c49a3c;background:#fdf8ec;padding:4px 9px;margin:6px 0;font-size:9pt;break-inside:avoid}
.def .l{color:#c49a3c;font-weight:700;font-size:7.6pt;letter-spacing:1px}
table.t{width:100%;border-collapse:collapse;margin:5px 0;font-size:8.8pt;break-inside:avoid}
table.t th{background:#13286b;color:#fff;text-align:left;padding:3px 6px}
table.t td{border:1px solid #d3daea;padding:3px 6px;vertical-align:top}
table.t tr:nth-child(even) td{background:#f5f7fc}
.key{background:#13286b;color:#fff;padding:7px 12px;margin-top:10px;border-radius:3px;break-inside:avoid}
.key .l{color:#e6c673;font-weight:700;letter-spacing:1px;font-size:8.6pt}
.key b{color:#e6c673}
.key ul{margin:3px 0 0 14px}
.intro{margin:4px 0 6px}
"""
def md(s):
    s = html.escape(s, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)

def chapter(n, d, label):
    h = f'<div class="ch"><div class="chh"><div class="c">CHAPTER {n:02d}</div><h2>{md(d["title"])}</h2></div>'
    h += '<div class="probe"><b>PROBE &amp; PONDER</b><ul>' + "".join(f"<li>{md(x)}</li>" for x in d["probe"]) + "</ul></div>"
    h += f'<p class="intro">{md(d["intro"])}</p>'
    for i, sec in enumerate(d["sections"], 1):
        h += f"<h3>{n}.{i} {md(sec['h'])}</h3>"
        if sec.get("bul"): h += "<ul>" + "".join(f"<li>{md(x)}</li>" for x in sec["bul"]) + "</ul>"
        if sec.get("defn"): h += f'<div class="def"><div class="l">DEFINITION</div>{md(sec["defn"])}</div>'
        if sec.get("tab"):
            hd, rows = sec["tab"]
            h += '<table class="t"><tr>' + "".join(f"<th>{md(x)}</th>" for x in hd) + "</tr>" + "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
        if sec.get("bul2"): h += "<ul>" + "".join(f"<li>{md(x)}</li>" for x in sec["bul2"]) + "</ul>"
    h += '<div class="key"><div class="l">KEY TAKEAWAYS</div><ul>' + "".join(f"<li>{md(x)}</li>" for x in d["key"]) + "</ul></div></div>"
    return h

def build(chs, subject, book, out, outdir):
    os.makedirs(outdir, exist_ok=True)
    body = f'<div class="cover"><div class="org">THE MASTERMIND COACHING CLASSES</div><h1>Revision Notes</h1><div class="sub">CLASS 6 · {subject.upper()}</div><div style="margin-top:8px">{md(book)}</div>'
    body += '<div class="how"><b>HOW TO USE THESE NOTES</b><br>Each chapter opens with a few thinking questions and then follows the order of the textbook. Bold words are keywords you should be able to define. Gold boxes hold definitions; tables compare and classify. The navy Key Takeaways box at the end of each chapter is your last-two-minutes revision. These notes are our own summary, not a copy of the textbook.</div>'
    body += '<table class="toc"><tr><th>Ch.</th><th>Chapter</th></tr>' + "".join(f"<tr><td>{n}</td><td>{md(d['title'])}</td></tr>" for n, d in chs.items()) + "</table></div>"
    body += "".join(chapter(n, d, subject) for n, d in chs.items())
    page_html = lib.head(f"Class 6 {subject} Revision Notes").replace("</style>", CSS + "</style>") + body + lib.TAIL
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        lib.to_pdf(pg, page_html, os.path.join(outdir, out), f"The Mastermind Coaching Classes — Road No. 5, VKIA, Jaipur — 9887258679 | Class 6 {subject} Revision Notes")
        br.close()
