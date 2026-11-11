"""School-pattern paper builder (CBSE-style 80-mark papers with case studies, A-R, figures).
Item kinds (python dicts):
  mcq(q, opts, ans, sol='', fig=None)            1 mark, ans in 'abcd'
  ar(a, r, ans, sol='')                           1 mark Assertion-Reason (std 4 options)
  sa(q, marks, sol, fig=None)                     2/3/5 marks; sol = marking scheme text (HTML allowed)
  OR(x, y)                                        internal choice between two sa/case-sub items
  case(text, subs, fig=None)                      4 marks; subs=[sub(q, marks, sol, fig=None), ...]; a sub may be OR(sub, sub)
Sections: sec(title, note, items). paper meta: dict(cls, subject, title_extra, set_no, time, marks, instr=[...]).
HTML helpers: frac(a,b), sqrt(x), sub/sup via <sub>/<sup>.  Figures: SVG strings (see figs.py).
"""
import os, html
from playwright.sync_api import sync_playwright

def frac(a, b): return f"<span class='fr'><span class='n'>{a}</span><span class='d'>{b}</span></span>"
def sqrt(x): return f"√<span class='ov'>{x}</span>"

def mcq(q, opts, ans, sol='', fig=None): assert len(opts) == 4 and ans in 'abcd'; return dict(k='mcq', q=q, opts=opts, ans=ans, sol=sol, fig=fig, m=1)
AR_OPTS = ["Both A and R are true, and R is the correct explanation of A.", "Both A and R are true, but R is not the correct explanation of A.", "A is true but R is false.", "A is false but R is true."]
def ar(a, r, ans, sol=''): assert ans in 'abcd'; return dict(k='ar', a=a, r=r, ans=ans, sol=sol, m=1)
def sa(q, marks, sol, fig=None): return dict(k='sa', q=q, m=marks, sol=sol, fig=fig)
def sub(q, marks, sol, fig=None): return dict(k='sub', q=q, m=marks, sol=sol, fig=fig)
def OR(x, y): return dict(k='or', a=x, b=y, m=x['m'])
def case(text, subs, fig=None, lab='roman'): return dict(k='case', text=text, subs=subs, fig=fig, lab=lab, m=sum(s['m'] for s in subs))
def sec(title, note, items): return dict(title=title, note=note, items=items)

CSS = """
@page{size:A4;margin:12mm 13mm 14mm 13mm}
*{box-sizing:border-box} body{font-family:'Arimo','Liberation Sans',Arial,sans-serif;font-size:10.2pt;line-height:1.38;color:#111;margin:0}
.hd{text-align:center;border-bottom:2px solid #0f2347;padding-bottom:2mm;margin-bottom:2mm}
.hd .b{font-size:15pt;font-weight:700;color:#0f2347;letter-spacing:.06em}.hd .s{font-size:8.5pt;color:#444}
.tt{text-align:center;font-weight:700;font-size:12.5pt;margin:2mm 0 0}.tt2{text-align:center;font-size:9pt;color:#444;margin-bottom:2mm}
.meta{display:flex;justify-content:space-between;font-size:9.6pt;border-top:1px solid #999;border-bottom:1px solid #999;padding:1.2mm 0;margin-bottom:2mm}
.ins{font-size:9pt;margin-bottom:2mm}.ins ol{margin:.5mm 0 0 4mm;padding-left:3mm}.ins li{margin:0}
.sec{margin:3mm 0 1.5mm;padding:1mm 2mm;background:#0f2347;color:#fff;font-weight:700;font-size:10pt;display:flex;justify-content:space-between;page-break-after:avoid}
.snote{font-size:9pt;font-style:italic;margin:0 0 1.5mm;page-break-after:avoid}
.q{display:flex;gap:2mm;margin:0 0 2.4mm;page-break-inside:avoid}.qn{width:7mm;flex:none;font-weight:700}.qb{flex:1}.qm{width:9mm;flex:none;text-align:right;font-weight:700}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:.4mm 4mm;margin-top:.8mm}.opts.c4{grid-template-columns:repeat(4,1fr)}.opts.c1{grid-template-columns:1fr}
.orr{text-align:center;font-weight:700;margin:1mm 0;letter-spacing:.2em}
.fig{margin:1.2mm 0;text-align:center}.fig svg{max-width:100%;height:auto}
.sub{display:flex;gap:2mm;margin:1mm 0}.sub .sl{width:7mm;flex:none}.sub .sm{width:9mm;flex:none;text-align:right}.sub>div:nth-child(2){flex:1}
.case{border-left:3px solid #c9a227;padding-left:3mm;margin-bottom:1mm}
table.t{border-collapse:collapse;margin:1mm 0}table.t td,table.t th{border:1px solid #444;padding:.6mm 2.4mm;text-align:center}
.fr{display:inline-block;vertical-align:middle;text-align:center;line-height:1.05}.fr .n{display:block;border-bottom:1px solid #000;padding:0 .6mm}.fr .d{display:block}
.ov{border-top:1px solid #000;padding:0 .4mm}
.qc{page-break-inside:auto}.sub{page-break-inside:avoid}.key .q{page-break-inside:auto}.sol{font-size:9.4pt;color:#222;background:#f3f5fa;border-left:3px solid #0f2347;padding:1mm 2.5mm;margin:.8mm 0}.ans{font-weight:700;color:#0f2347}
.foot{font-size:8pt;color:#666;text-align:center}
"""

def _letters(): return 'abcd'
def _opts_html(opts):
    L = max(len(html.unescape(__import__('re').sub('<[^>]+>', '', o))) for o in opts)
    cls = 'c4' if L <= 14 else ('' if L <= 40 else 'c1')
    return f"<div class='opts {cls}'>" + "".join(f"<div>({_letters()[i]}) {o}</div>" for i, o in enumerate(opts)) + "</div>"
def _fig(f): return f"<div class='fig'>{f}</div>" if f else ""

def _item_html(it, n, key):
    k = it['k']
    sol = lambda s: (f"<div class='sol'>{s}</div>" if (key and s) else "")
    if k == 'mcq':
        body = f"{it['q']}{_fig(it['fig'])}{_opts_html(it['opts'])}"
        if key: body += f"<div class='sol'><span class='ans'>Ans: ({it['ans']})</span> {it['sol']}</div>"
        return f"<div class='q'><div class='qn'>{n}{'.' if n!='' else ''}</div><div class='qb'>{body}</div><div class='qm'>{'' if key else 1}</div></div>"
    if k == 'ar':
        body = f"<b>Assertion (A):</b> {it['a']}<br><b>Reason (R):</b> {it['r']}" + ('' if key else _opts_html(AR_OPTS).replace("class='opts '", "class='opts c1'"))
        if key: body += f"<div class='sol'><span class='ans'>Ans: ({it['ans']})</span> {it['sol']}</div>"
        return f"<div class='q'><div class='qn'>{n}{'.' if n!='' else ''}</div><div class='qb'>{body}</div><div class='qm'>{'' if key else 1}</div></div>"
    if k == 'sa':
        return f"<div class='q'><div class='qn'>{n}{'.' if n!='' else ''}</div><div class='qb'>{it['q']}{'' if (key and it.get('nofig')) else _fig(it['fig'])}{sol(it['sol'])}</div><div class='qm'>{'' if key else it['m']}</div></div>"
    if k == 'or':
        a, b = it['a'], it['b']
        if a['k'] == 'case': raise ValueError
        return (_item_html(a, n, key) + "<div class='orr'>OR</div>" + _item_html(b, '', key).replace("<div class='qm'>" + ('' if key else str(b['m'])) + "</div>", "<div class='qm'></div>"))
    if k == 'case':
        parts = ["<div class='case'>" + it['text'] + _fig(it['fig']) + "</div>"]
        letters = 'iiiivvvi'
        roman = ['a', 'b', 'c', 'd', 'e'] if it.get('lab') == 'alpha' else ['i', 'ii', 'iii', 'iv', 'v']
        for j, s in enumerate(it['subs']):
            def one(sb, lab, mk):
                return f"<div class='sub'><div class='sl'>({lab})</div><div>{sb['q']}{_fig(sb.get('fig'))}{sol(sb['sol'])}</div><div class='sm'>{'' if key else mk}</div></div>"
            if s['k'] == 'or':
                parts.append(one(s['a'], roman[j], s['a']['m']) + "<div class='orr'>OR</div>" + one(s['b'], roman[j], ''))
            else: parts.append(one(s, roman[j], s['m']))
        return f"<div class='q qc'><div class='qn'>{n}.</div><div class='qb'>{''.join(parts)}</div><div class='qm'></div></div>"
    raise ValueError(k)

def _count(sections): return sum(1 for s in sections for _ in s['items'])

def paper_html(meta, sections, key=False):
    total = 0; n = 0; body = []
    for s in sections:
        sm = sum(i['m'] for i in s['items']); total += sm
        body.append(f"<div class='sec'><span>{s['title']}</span><span>{len(s['items'])} questions · {sm} marks</span></div>")
        if s.get('note'): body.append(f"<div class='snote'>{s['note']}</div>")
        for it in s['items']:
            n += 1; body.append(_item_html(it, n, key))
    assert total == meta['marks'], f"marks {total} != {meta['marks']}"
    if key:
        head = f"<div class='tt'>ANSWER KEY & MARKING SCHEME — {meta['subject'].upper()} · CLASS {meta['cls']} · SET {meta['set_no']:02d}</div><div class='tt2'>Max. Marks: {meta['marks']} · The Mastermind Coaching Classes, Jaipur · Alternate correct methods to be given full credit</div>"
    else:
        ins = "".join(f"<li>{i}</li>" for i in meta['instr'])
        head = (f"<div class='tt'>{meta['title']}</div><div class='tt2'>{meta.get('title_extra','')}</div>"
                f"<div class='meta'><span>Class: {meta['cls']}</span><span>Subject: {meta['subject']}</span><span>Set {meta['set_no']:02d}</span><span>Time: {meta['time']}</span><span>Max. Marks: {meta['marks']}</span></div>"
                f"<div class='ins'><b>General Instructions:</b><ol>{ins}</ol></div>")
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body class='{'key' if key else ''}'><div class='hd'><div class='b'>THE MASTERMIND COACHING CLASSES</div><div class='s'>CBSE / RBSE · Nursery – Class XII · Road No. 5, VKIA, Jaipur · 9887258679</div></div>{head}{''.join(body)}</body></html>"

def build(meta, sections, outdir, name):
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH') or None); pg = br.new_page()
        for key, fn in ((False, f"{name}.pdf"), (True, f"{name}_Answer_Key.pdf")):
            pg.set_content(paper_html(meta, sections, key), wait_until='load')
            foot = f"<div style='width:100%;font-size:7.5pt;color:#666;text-align:center;font-family:Arial'>Mastermind Coaching Classes · Class {meta['cls']} {meta['subject']} · Set {meta['set_no']:02d} {'· Answer Key ' if key else ''}| Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>"
            pg.pdf(path=f"{outdir}/{fn}", format='A4', print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=foot, margin=dict(top='12mm', bottom='15mm', left='13mm', right='13mm'))
        br.close()


# =====================================================================
# CLASS 8 SST — Delhi-DoE school-pattern renderer (overrides, numbering:
#   Q1.(i)-(xv), 2.(A)/2.(B) OR, case sub-labels 10.1/10.2/10.3)
# =====================================================================
CSS += """
.qn8{width:13mm;flex:none;font-weight:700}.qm8{width:11mm;flex:none;text-align:right;font-weight:700}
.q8{display:flex;gap:2mm;margin:0 0 2.3mm;page-break-inside:avoid}.qb8{flex:1}
.cs{border-left:3px solid #c9a227;padding-left:3mm;margin:.5mm 0 1.2mm;text-align:justify}
.cq{display:flex;gap:2mm;margin:.8mm 0 .8mm 6mm;page-break-inside:avoid}.cq .l{width:12mm;flex:none}.cq .b{flex:1}.cq .mk{width:9mm;flex:none;text-align:right}
.hdg{font-weight:700;margin:0 0 1mm}
.vi{font-size:9pt;border-top:1px dotted #888;margin-top:1.5mm;padding-top:1mm}
.vi div{display:flex;justify-content:space-between}
.mp{display:grid;grid-template-columns:1fr 1fr;gap:0 6mm;margin:.5mm 0 1mm 0}
"""
ROM = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv']
def _o8(opts):
    import re
    L = max(len(html.unescape(re.sub('<[^>]+>', '', o))) for o in opts)
    cls = 'c4' if L <= 15 else ('' if L <= 42 else 'c1')
    return f"<div class='opts {cls}'>" + "".join(f"<div>({'ABCD'[i]}) {o}</div>" for i, o in enumerate(opts)) + "</div>"

def _row8(num, body, mk):
    return f"<div class='q8'><div class='qn8'>{num}</div><div class='qb8'>{body}</div><div class='qm8'>{mk}</div></div>"

def _sa8(it, num, key):
    sol = f"<div class='sol'>{it['sol']}</div>" if key and it.get('sol') else ''
    fig = '' if (key and it.get('nofig')) else _fig(it.get('fig'))
    return _row8(num, f"{it['q']}{fig}{sol}", '' if key else f"({it['m']})")

def _mc8(it, num, key):
    body = f"{it['q']}{_fig(it.get('fig'))}{_o8(it['opts'])}"
    if key: body += f"<div class='sol'><span class='ans'>Ans: ({it['ans'].upper()})</span> {it['sol']}</div>"
    return _row8(num, body, '' if key else '(1)')

def _case8(it, n, key):
    parts = f"<div class='hdg'>Read the paragraph given below and answer the questions that follow: ({'+'.join(str(s['m']) for s in it['subs'])}={it['m']})</div><div class='cs'>{it['text']}</div>"
    if not key: parts += "<div><b>Questions:</b></div>"
    for j, s in enumerate(it['subs'], 1):
        sol = f"<div class='sol'>{s['sol']}</div>" if key else ''
        parts += f"<div class='cq'><div class='l'>({n}.{j})</div><div class='b'>{s['q']}{sol}</div><div class='mk'>{'' if key else '('+str(s['m'])+')'}</div></div>"
    return f"<div style='page-break-inside:avoid;margin-bottom:2.5mm'><div style='display:flex;gap:2mm'><div class='qn8'>{n}.</div><div style='flex:1'>{parts}</div></div></div>"

def paper_html(meta, sections, key=False):
    total = 0; n = 0; body = []
    for s in sections:
        sm = sum(i['m'] for i in s['items']); total += sm
        body.append(f"<div class='sec'><span>{s['title']}</span><span>{sm} marks</span></div>")
        if s.get('note'): body.append(f"<div class='snote'>{s['note']}</div>")
        if s.get('mcqs'):
            n += 1
            assert len(s['items']) == 15
            for j, it in enumerate(s['items']):
                body.append(_mc8(it, (f"{n}.({ROM[j]})" if j == 0 else f"({ROM[j]})"), key))
            continue
        for it in s['items']:
            n += 1
            if it['k'] == 'or':
                body.append(f"<div style='page-break-inside:{'auto' if key else 'avoid'}'>" + _sa8(it['a'], f"{n}.(A)", key) + "<div class='orr'>OR</div>" + _sa8(it['b'], f"{n}.(B)", key) + "</div>")
            elif it['k'] == 'case': body.append(_case8(it, n, key))
            else: body.append(_sa8(it, f"{n}.", key))
    assert total == meta['marks'], f"marks {total} != {meta['marks']}"
    assert n == 14, f"question count {n}"
    if key:
        head = f"<div class='tt'>ANSWER KEY & MARKING SCHEME — {meta['subject'].upper()} · CLASS {meta['cls']} · SET {meta['set_no']:02d}</div><div class='tt2'>Max. Marks: {meta['marks']} · The Mastermind Coaching Classes, Jaipur · Alternate correct points / examples to be given full credit</div>"
    else:
        ins = "".join(f"<li>{i}</li>" for i in meta['instr'])
        head = (f"<div class='tt'>{meta['title']}</div><div class='tt2'>{meta.get('title_extra','')}</div>"
                f"<div class='meta'><span>Class: {meta['cls']}</span><span>Subject: {meta['subject']}</span><span>Set {meta['set_no']:02d}</span><span>Time Allowed: {meta['time']}</span><span>Max. Marks: {meta['marks']}</span></div>"
                f"<div class='ins'><b>GENERAL INSTRUCTIONS</b><ol>{ins}</ol></div>")
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body class='{'key' if key else ''}'><div class='hd'><div class='b'>THE MASTERMIND COACHING CLASSES</div><div class='s'>CBSE / RBSE · Nursery – Class XII · Road No. 5, VKIA, Jaipur · 9887258679</div></div>{head}{''.join(body)}</body></html>"
