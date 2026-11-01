"""Class 10 English school-pattern paper renderer (Delhi DoE style, 80 marks)."""
import os, re, html
from playwright.sync_api import sync_playwright
ROM = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
CSS = """
@page{size:A4;margin:12mm 13mm 14mm 13mm}
*{box-sizing:border-box} body{font-family:'Arimo','Liberation Sans',Arial,sans-serif;font-size:10.2pt;line-height:1.38;color:#111;margin:0}
.hd{text-align:center;border-bottom:2px solid #0f2347;padding-bottom:2mm;margin-bottom:2mm}
.hd .b{font-size:15pt;font-weight:700;color:#0f2347;letter-spacing:.06em}.hd .s{font-size:8.5pt;color:#444}
.tt{text-align:center;font-weight:700;font-size:12pt;margin:1.5mm 0 0}.tt2{text-align:center;font-size:9pt;color:#444;margin-bottom:2mm}
.meta{display:flex;justify-content:space-between;font-size:9.6pt;border-top:1px solid #999;border-bottom:1px solid #999;padding:1.2mm 0;margin-bottom:2mm}
.ins{font-size:9pt;margin-bottom:2mm}.ins ol{margin:.5mm 0 0 4mm;padding-left:3mm}.ins li{margin:0}
.sec{margin:3.5mm 0 1.5mm;padding:1mm 2mm;background:#0f2347;color:#fff;font-weight:700;font-size:10pt;display:flex;justify-content:space-between;page-break-after:avoid}
.sub{font-weight:700;margin:2mm 0 1mm;display:flex;justify-content:space-between;page-break-after:avoid}
.ps p{margin:0 0 1.4mm;text-align:justify}.pw{font-size:8.5pt;color:#555;text-align:right;margin-bottom:1.5mm}
.pt{font-weight:700;text-align:center;margin:1mm 0}
.p{display:flex;gap:2mm;margin:0 0 1.8mm;page-break-inside:avoid}.pn{width:9mm;flex:none}.pb{flex:1}.pm{width:8mm;flex:none;text-align:right;font-weight:700}
.opts{margin:.6mm 0 0 0}.opts div{margin:0}
.orr{text-align:center;font-weight:700;margin:1.2mm 0;letter-spacing:.2em}
.ext{border-left:3px solid #c9a227;padding:.6mm 3mm;margin:1mm 0 1.6mm;font-style:italic;background:#faf8ee}.src{text-align:right;font-style:normal;font-size:9pt}
table.t{border-collapse:collapse;margin:1mm 0}table.t td,table.t th{border:1px solid #444;padding:.7mm 2.6mm;text-align:center}
.q{margin:0 0 2mm;display:flex;gap:2mm;page-break-inside:avoid}.qn{width:7mm;flex:none;font-weight:700}.qb{flex:1}
.key .sol{font-size:9.4pt;background:#f3f5fa;border-left:3px solid #0f2347;padding:1mm 2.5mm;margin:.8mm 0}.ans{font-weight:700;color:#0f2347}
.key .p{page-break-inside:auto}.mk{font-size:9pt;color:#555}
"""
def wc(paras): return sum(len(re.sub(r'<[^>]+>', ' ', p).split()) for p in paras)
def P(q, m, sol, opts=None, ans=None, extra=''): 
    if opts: assert ans in 'abcd' and len(opts) in (2, 3, 4), q
    return dict(q=q, m=m, sol=sol, opts=opts, ans=ans, extra=extra)
def table(head, rows): return "<table class='t'><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
def errtab(): return table(["ERROR", "CORRECTION"], [["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]])
def _part(p, lab, key, mark=True):
    o = ""
    if p['opts']: o = "<div class='opts'>" + "".join(f"<div>({'ABCD'[i]}) {t}</div>" for i, t in enumerate(p['opts'])) + "</div>"
    body = f"{p['q']}{p['extra']}{o}"
    if key:
        a = f"<span class='ans'>Ans: ({p['ans'].upper()})</span> " if p['ans'] else ""
        body += f"<div class='sol'>{a}{p['sol']}</div>"
    return f"<div class='p'><div class='pn'>{lab}</div><div class='pb'>{body}</div><div class='pm'>{p['m'] if mark else ''}</div></div>"
def _parts(parts, key, start=0, mark=True): return "".join(_part(p, ROM[start+i] + ".", key, mark) for i, p in enumerate(parts))
def sm(parts): return sum(p['m'] for p in parts)

def paper_html(S, key=False):
    n = S['set_no']; B = []
    tot = 0
    def sec(t, m): B.append(f"<div class='sec'><span>{t}</span><span>{m}</span></div>")
    sec("SECTION A — READING SKILLS", "20 marks")
    for qi, ps in enumerate(S['passages']):
        m = sm(ps['parts']); assert m == 10, (n, qi, m); tot += m
        w = wc(ps['paras'])
        B.append(f"<div class='sub'><span>{qi+1}. Read the following passage.</span><span>{m}</span></div><div class='ps'>" + "".join(f"<p><b>{i+1}.</b> {t}</p>" for i, t in enumerate(ps['paras'])) + f"</div><div class='pw'>Created for academic usage / {w} words</div><div class='sub'><span>Answer the following questions, based on the passage above.</span></div>" + _parts(ps['parts'], key))
    sec("SECTION B — GRAMMAR AND WRITING SKILLS", "20 marks")
    g = S['grammar']; assert len(g) == 12 and all(p['m'] == 1 for p in g), n; tot += 10
    B.append("<div class='sub'><span>GRAMMAR — 10</span></div><div class='sub'><span>3. Complete any ten of the twelve of the following tasks, as directed.</span><span>(10 × 1 = 10)</span></div>" + _parts(g, key))
    for qn, nm in ((4, 'q4'), (5, 'q5')):
        A, Bq = S[nm]; tot += 5
        B.append(f"<div class='sub'><span>{qn}. Attempt ANY ONE from A and B.</span><span>1 × 5 = 5</span></div>")
        for lab, it in (("A", A), ("B", Bq)):
            if lab == "B": B.append("<div class='orr'>OR</div>")
            B.append(f"<div class='p'><div class='pn'>{lab}.</div><div class='pb'>{it['q']}" + (f"<div class='sol'>{it['sol']}</div>" if key else "") + "</div></div>")
    sec("SECTION C — LITERATURE TEXTBOOK", "40 marks")
    for qn, nm in ((6, 'q6'), (7, 'q7')):
        B.append(f"<div class='sub'><span>{qn}. Read the following extracts and answer the questions for any one of the given two, (a) or (b).</span><span>5</span></div>")
        for lab, it in zip("ab", S[nm]):
            m = sm(it['parts']); assert m == 5, (n, qn, lab, m); tot += 0
            if lab == "b": B.append("<div class='orr'>OR</div>")
            B.append(f"<div class='sub'><span>({lab})</span></div><div class='ext'>{it['extract']}<div class='src'>({it['src']})</div></div>" + _parts(it['parts'], key))
        tot += 5
    for qn, nm, need, mk in ((8, 'q8', 4, 3), (9, 'q9', 2, 3)):
        items = S[nm]; assert len(items) == need + 1 if nm == 'q8' else len(items) == 3, (n, nm)
        B.append(f"<div class='sub'><span>{qn}. Answer any {'four of the following five' if nm=='q8' else 'two of the following three'} questions in 40–50 words each.</span><span>({need} × 3 = {need*3})</span></div>")
        for i, (q, sol) in enumerate(items): B.append(f"<div class='p'><div class='pn'>{ROM[i]}.</div><div class='pb'>{q}" + (f"<div class='sol'>{sol}</div>" if key else "") + "</div></div>")
        tot += need * 3
    for qn, nm in ((10, 'q10'), (11, 'q11')):
        A, Bq = S[nm]; tot += 6
        B.append(f"<div class='sub'><span>{qn}. Answer ANY ONE of the following two questions, in about 100–120 words.</span><span>(1 × 6)</span></div>")
        for lab, (q, sol) in (("A", A), ("B", Bq)):
            if lab == "B": B.append("<div class='orr'>OR</div>")
            B.append(f"<div class='p'><div class='pn'>({lab})</div><div class='pb'>{q}" + (f"<div class='sol'>{sol}</div>" if key else "") + "</div></div>")
    assert tot == 80, (n, tot)
    if key:
        head = f"<div class='tt'>ANSWER KEY & MARKING SCHEME — ENGLISH LANGUAGE AND LITERATURE · CLASS X · SET {n:02d}</div><div class='tt2'>Max. Marks: 80 · Alternative correct answers / expressions to be given due credit · Writing: Format 1 + Content 2 + Fluency & accuracy 2</div>"
    else:
        head = (f"<div class='tt'>CLASS X — ENGLISH LANGUAGE AND LITERATURE (184) · PRACTICE PAPER · SET {n:02d}</div><div class='tt2'>Session 2026-27 · Mid-Term Pattern</div>"
                "<div class='meta'><span>Class: X</span><span>Subject: English Language and Literature</span><span>Time: 3 Hours</span><span>Max. Marks: 80</span></div>"
                "<div class='ins'><b>General Instructions:</b><ol><li>This question paper comprises 11 questions. All questions are compulsory.</li><li>The question paper contains THREE sections — Section A: Reading Skills; Section B: Grammar and Writing Skills; Section C: Literature Textbook.</li><li>Attempt questions based on the specific instructions given for each part.</li></ol></div>")
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body class='{'key' if key else ''}'><div class='hd'><div class='b'>THE MASTERMIND COACHING CLASSES</div><div class='s'>CBSE / RBSE · Nursery – Class XII · Road No. 5, VKIA, Jaipur · 9887258679</div></div>{head}{''.join(B)}</body></html>"

def build(S, outdir):
    os.makedirs(outdir, exist_ok=True); n = S['set_no']
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for key, fn in ((False, f"English_Class10_Set_{n:02d}.pdf"), (True, f"English_Class10_Set_{n:02d}_Answer_Key.pdf")):
            pg.set_content(paper_html(S, key), wait_until='load')
            foot = f"<div style='width:100%;font-size:7.5pt;color:#666;text-align:center;font-family:Arial'>Mastermind Coaching Classes · Class 10 English · Set {n:02d} {'· Answer Key ' if key else ''}| Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>"
            pg.pdf(path=f"{outdir}/{fn}", format='A4', print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=foot, margin=dict(top='12mm', bottom='15mm', left='13mm', right='13mm'))
        br.close()
