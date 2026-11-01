import os, sys, subprocess, html
sys.path.insert(0, "/home/claude/rw/c6")
from lib import head, BRAND, TAIL, to_pdf
from playwright.sync_api import sync_playwright
def pages(f): return int([l for l in subprocess.run(["pdfinfo", f], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages")][0].split()[-1])
def make(ROOT, title, sub, contents, notes):
    rows = []; total = 0; keys = 0
    for dp, dn, fn in sorted(os.walk(ROOT)):
        dn.sort()
        pdfs = sorted(f for f in fn if f.endswith(".pdf") and dp != ROOT and f != "00_Index.pdf")
        if not pdfs: continue
        rows.append(f'<tr class="dir"><td colspan="2">📁 {html.escape(os.path.relpath(dp, ROOT))}</td></tr>')
        for f in pdfs:
            total += 1; keys += "Answer_Key" in f
            rows.append(f"<tr><td>{html.escape(f)}</td><td style='text-align:right'>{pages(os.path.join(dp,f))}</td></tr>")
    body = f"""{BRAND}
<div class="ttl"><div class="t">{title}</div><div class="c">{sub}</div></div>
<style>table.ix{{width:100%;border-collapse:collapse;font-size:9.5pt;margin:6px 0}} table.ix td,table.ix th{{border:.6px solid #c8cfe6;padding:3px 6px}} table.ix th{{background:#13286b;color:#fff;text-align:left}} tr.dir td{{background:#eef1fb;font-weight:700;color:#13286b}} p.n{{margin:5px 0;font-size:9.6pt}}</style>
<p class="n"><b>Contents:</b> {contents}</p>
{''.join(f'<p class="n">{n}</p>' for n in notes)}
<table class="ix"><tr><th>File</th><th style="text-align:right">Pages</th></tr>{''.join(rows)}</table>
<p class="n"><b>Total PDFs:</b> {total} ({total-keys} papers + {keys} answer keys)</p>"""
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        to_pdf(pg, head("Index") + body + TAIL, f"{ROOT}/00_Index.pdf", f"Mastermind Coaching Classes — {title}")
        b.close()
    return total, keys
