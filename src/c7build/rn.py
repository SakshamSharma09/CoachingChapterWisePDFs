import re, html, sys, importlib
def clean(a):
    a = re.sub(r"\s*\((?:\d+(?:\.\d+)?)\)", "", a)
    return a.strip()
def qa(modname, n=8):
    m = importlib.import_module(modname)
    rows = []
    for q in m.B[:n]:
        qq = re.sub(r"<[^>]+>", "", q["q"])
        rows.append([qq, clean(q["ans"])])
    return rows
sys.path.insert(0, "/home/claude/c7build")
from playwright.sync_api import sync_playwright
from lib import to_pdf
CSS = """
@page{size:A4}
body{font-family:'Noto Sans','DejaVu Sans',Arial,sans-serif;font-size:10pt;line-height:1.42;color:#1d2433;margin:0}
.hdr{text-align:center}.hdr .n{font-size:15pt;font-weight:800;color:#13286b;letter-spacing:.5px}.hdr .s{font-size:7.5pt;color:#c49a3c;letter-spacing:1.5px;font-weight:700}.hdr .a{font-size:8pt;color:#555}
.rule{border-top:2px solid #13286b;margin:5px 0 8px}
.cover{height:250mm;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;page-break-after:always}
.cover h1{font-size:30pt;color:#13286b;margin:6px 0}.cover .g{font-size:13pt;letter-spacing:3px;color:#c49a3c;font-weight:700}
.cover .d{max-width:130mm;font-size:11pt;color:#444;margin:14px 0}
.cover ul{text-align:left;font-size:10pt;max-width:140mm}
.cover .f{margin-top:30px;font-size:9pt;color:#13286b}
.toc{page-break-after:always}.toc h2{color:#13286b;border-bottom:2px solid #c49a3c;padding-bottom:3px}.toc table{width:100%;border-collapse:collapse}.toc td{padding:4px 6px;border-bottom:.5px solid #dde}
.ch{page-break-before:always}.ch:first-of-type{page-break-before:auto}
.cn{font-size:8.5pt;font-weight:800;letter-spacing:2px;color:#c49a3c}.ct{font-size:19pt;font-weight:800;color:#13286b;margin:0 0 6px;border-bottom:2px solid #13286b;padding-bottom:4px}
.intro{font-style:italic;color:#444;margin:4px 0 8px}
h3{font-size:12pt;color:#13286b;margin:11px 0 4px;border-left:4px solid #c49a3c;padding-left:7px;break-after:avoid}
ul{margin:3px 0 4px 17px;padding:0}li{margin:2px 0}
table.t{width:100%;border-collapse:collapse;margin:6px 0;font-size:9.2pt;break-inside:avoid}table.t th{background:#13286b;color:#fff;text-align:left;padding:4px 6px}table.t td{border:.6px solid #c8cfe6;padding:3px 6px;vertical-align:top}table.t tr:nth-child(even) td{background:#f4f6fd}
.note{border-left:4px solid #1f5fbf;background:#eaf2ff;padding:5px 9px;margin:7px 0;font-size:9.5pt;break-inside:avoid}.note b.l{color:#1f5fbf;letter-spacing:1px}
.key{border:1px solid #e0c36a;background:#fff8e1;border-radius:4px;padding:6px 10px;margin:10px 0 2px;break-inside:avoid}.key .k{font-weight:800;color:#8a6a10;border-bottom:1px solid #e0c36a;margin-bottom:3px}
"""
def md(s):
    s = html.escape(s)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
def chapter(c, grade_sub):
    o = [f'<section class="ch"><div class="cn">CHAPTER {c["no"]:02d} · {grade_sub}</div><div class="ct">{md(c["title"])}</div><div class="intro">{md(c["intro"])}</div>']
    for s in c["secs"]:
        o.append(f'<h3>{md(s["h"])}</h3>')
        if s.get("pts"): o.append("<ul>" + "".join(f"<li>{md(p)}</li>" for p in s["pts"]) + "</ul>")
        if s.get("table"):
            hd, rows = s["table"]
            o.append('<table class="t"><tr>' + "".join(f"<th>{md(h)}</th>" for h in hd) + "</tr>" + "".join("<tr>" + "".join(f"<td>{md(x)}</td>" for x in r) + "</tr>" for r in rows) + "</table>")
        if s.get("note"): o.append(f'<div class="note"><b class="l">NOTE</b> &nbsp;{md(s["note"])}</div>')
    o.append('<div class="key"><div class="k">★ KEY TAKEAWAYS</div><ul>' + "".join(f"<li>{md(k)}</li>" for k in c["key"]) + "</ul></div></section>")
    return "".join(o)
def build(chs, out, title, grade_sub, scope, how):
    toc = "".join(f'<tr><td><b>Chapter {c["no"]:02d}</b></td><td>{md(c["title"])}</td></tr>' for c in chs)
    cover = f"""<div class="cover"><div class="hdr"><div class="n">THE MASTERMIND COACHING CLASSES</div><div class="s">CBSE / RBSE • NURSERY – CLASS XII • JAIPUR</div></div>
<div class="g" style="margin-top:30px">REVISION NOTES</div><h1>{title}</h1><div class="g">{grade_sub}</div>
<div class="d">{scope}</div><ul>{''.join(f'<li>{md(h)}</li>' for h in how)}</ul>
<div class="f">The Mastermind Coaching Classes — Road No. 5, VKIA, Jaipur — 9887258679</div></div>
<div class="toc"><h2>Contents</h2><table>{toc}</table></div>"""
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{cover}{''.join(chapter(c, grade_sub) for c in chs)}
<script>document.fonts.ready.then(function(){{window.__done=true;}});</script></body></html>"""
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        to_pdf(pg, doc, out, f"Mastermind Coaching Classes · {grade_sub} · {title}")
        b.close()
