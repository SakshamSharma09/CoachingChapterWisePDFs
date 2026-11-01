import os, re, html as H, sys
sys.path.insert(0, '/home/claude/pat/c8eng')
from lib_pat import CSS as BASE_CSS
from playwright.sync_api import sync_playwright
CSS = BASE_CSS + """
.sh{margin:3mm 0 1.5mm;padding:1mm 2mm;background:#0f2347;color:#fff;font-weight:700;font-size:10pt;display:flex;justify-content:space-between;page-break-after:avoid}
.pas{border:1px solid #bbb;background:#fafafa;padding:2mm 3mm;margin:1.5mm 0 2mm;text-align:justify}.pas p{margin:0 0 1.2mm}
.qq{display:flex;gap:2mm;margin:0 0 1.8mm;page-break-inside:avoid}.qq .n{width:8mm;flex:none;font-weight:700}.qq .b{flex:1}.qq .m{width:8mm;flex:none;text-align:right;font-weight:700}
.o{display:grid;grid-template-columns:1fr 1fr;gap:.3mm 4mm;margin-top:.6mm}.o.c1{grid-template-columns:1fr}
.grp{font-weight:700;margin:2mm 0 1mm;display:flex;justify-content:space-between;page-break-after:avoid}
.stim{text-align:center;margin:1mm 0}.poem{font-style:italic;margin:1mm 0 1.5mm 8mm;line-height:1.5}
.sol{font-size:9.4pt;background:#f3f5fa;border-left:3px solid #0f2347;padding:1mm 2.5mm;margin:.8mm 0}
.note{font-size:9pt;font-style:italic;margin:.5mm 0 1.5mm}
"""
def mc(q, o, a, m=1): assert len(o) == 4 and 0 <= a < 4; return dict(t='mc', q=q, o=o, a=a, m=m)
def tf(q, a): return dict(t='tf', q=q, a=a, m=1)
def fb(q, a, o=None): return dict(t='fb', q=q, a=a, o=o, m=1)
def sa(q, a, m=1): return dict(t='sa', q=q, a=a, m=m)
def poster(title, tag, rows, c1="#0f2347", c2="#c9a227"):
    h = 70 + 46 * len(rows) + 30
    b = f"<rect x='2' y='2' width='436' height='{h-4}' rx='10' fill='#fffdf3' stroke='{c1}' stroke-width='4'/>"
    b += f"<rect x='2' y='2' width='436' height='54' rx='10' fill='{c1}'/><text x='220' y='34' text-anchor='middle' font-size='20' font-weight='bold' fill='#fff'>{title}</text>"
    b += f"<text x='220' y='72' text-anchor='middle' font-size='12' font-style='italic' fill='{c1}'>{tag}</text>"
    for i, (sym, line) in enumerate(rows):
        y = 90 + 46 * i
        b += f"<circle cx='36' cy='{y+12}' r='15' fill='{c2}'/><text x='36' y='{y+18}' text-anchor='middle' font-size='16' fill='#fff' font-weight='bold'>{sym}</text>"
        b += f"<text x='62' y='{y+17}' font-size='13' fill='#222'>{line}</text><line x1='20' y1='{y+34}' x2='420' y2='{y+34}' stroke='#ddd'/>"
    return f"<svg xmlns='http://www.w3.org/2000/svg' width='440' height='{h}' viewBox='0 0 440 {h}' font-family='Arial'>{b}</svg>"
LET = 'abcde'
def opts_html(o):
    L = max(len(re.sub('<[^>]+>', '', x)) for x in o)
    return f"<div class='o {'c1' if L > 38 else ''}'>" + "".join(f"<div>({LET[i]}) {x}</div>" for i, x in enumerate(o)) + "</div>"
def q_html(it, label, key, show_marks=True):
    t = it['t']; body = it['q']
    if t == 'mc': body += opts_html(it['o'])
    if t == 'tf': body += "<div class='note'>(State True or False.)</div>"
    if t == 'fb' and it.get('o'): body += f" <i>({' / '.join(it['o'])})</i>"
    if key:
        if t == 'mc': ans = f"({LET[it['a']]}) {it['o'][it['a']]}"
        elif t == 'tf': ans = 'True' if it['a'] else 'False'
        else: ans = it['a']
        body += f"<div class='sol'><b>Ans:</b> {ans}</div>"
    mk = '' if key or not show_marks else it['m']
    return f"<div class='qq'><div class='n'>{label}</div><div class='b'>{body}</div><div class='m'>{mk}</div></div>"
def marks(qs): return sum(x['m'] for x in qs)

def render(meta, S, key):
    out = []; tot = 0
    def head(t, m): out.append(f"<div class='sh'><span>{t}</span><span>{m} marks</span></div>")
    # Section A
    head("SECTION A — READING (14 Marks)", 14)
    r1, r2 = S['R1'], S['R2']
    assert marks(r1['qs']) == 7 and marks(r2['qs']) == 7, (marks(r1['qs']), marks(r2['qs']))
    out.append(f"<div class='grp'><span>Q1. Read the passage carefully and answer the questions that follow:</span><span>7</span></div><div class='pas'>{r1['passage']}</div>")
    for i, it in enumerate(r1['qs'], 1): out.append(q_html(it, f"{i}.", key))
    out.append(f"<div class='grp'><span>Q2. Study the poster carefully and answer the questions that follow:</span><span>7</span></div><div class='stim'>{r2['poster']}</div><div class='pas'>{r2['passage']}</div>")
    for i, it in enumerate(r2['qs'], 1): out.append(q_html(it, f"{i})", key))
    # Section B
    head("SECTION B — GRAMMAR (14 Marks)", 14)
    out.append("<div class='grp'><span>Q3. Do as directed.</span></div>")
    n = 0; gm = 0
    for gi, g in enumerate(S['G']):
        rom = ['I', 'II', 'III', 'IV'][gi]
        out.append(f"<div class='grp'><span>{rom}. Attempt any {g['k']} from the following questions {g['ins']}</span><span>({g['k']}x1={g['k']})</span></div>")
        gm += g['k']
        for it in g['items']:
            n += 1; out.append(q_html(it, f"{n})", key, False))
    assert gm == 14, gm
    # Section C
    head("SECTION C — WRITING (12 Marks)", 12)
    for qn, pair in (("Q4", S['W'][0]), ("Q5", S['W'][1])):
        out.append(f"<div class='grp'><span>{qn}. Answer any one from A and B.</span><span>(1x6=6)</span></div>")
        for lab, w in zip("AB", pair):
            if lab == 'B': out.append("<div class='orr'>OR</div>")
            out.append(f"<div class='qq'><div class='n'>({lab})</div><div class='b'>{w['q']}" + (f"<div class='sol'><b>Sample answer ({w['words']}):</b><br>{w['a']}<br><i>Marking: {w['mk']}</i></div>" if key else '') + "</div></div>")
    # Section D
    head("SECTION D — LITERATURE (20 Marks)", 20)
    L = S['L']
    out.append(f"<div class='grp'><span>Q6. Read the following passage and answer any four out of the five questions that follow:</span><span>(4x1=4)</span></div><div class='pas'>{L['q6']['passage']}</div>")
    for i, it in enumerate(L['q6']['qs']): out.append(q_html(it, f"{LET[i]})", key, False))
    out.append(f"<div class='grp'><span>Q7. Read the following extract and answer any two out of the three questions that follow:</span><span>(2x2=4)</span></div><div class='poem'>{L['q7']['poem']}</div>")
    for i, it in enumerate(L['q7']['qs']): out.append(q_html(it, f"{LET[i]})", key, False))
    out.append("<div class='grp'><span>Q8. Answer any four out of the five questions given below.</span><span>(4x3=12)</span></div>")
    for i, it in enumerate(L['q8']): out.append(q_html(it, f"{LET[i]})", key, False))
    if key:
        head_t = f"<div class='tt'>ANSWER KEY & MARKING SCHEME — ENGLISH · CLASS 8 · SET {meta['set_no']:02d}</div><div class='tt2'>Max. Marks 60 · The Mastermind Coaching Classes, Jaipur · Any other correct answer in the student's own words to be accepted</div>"
    else:
        head_t = (f"<div class='tt'>CLASS VIII — ENGLISH · MID-TERM PRACTICE PAPER</div><div class='tt2'>Session 2026–27 · Set {meta['set_no']:02d}</div>"
                  f"<div class='meta'><span>Class: VIII</span><span>Subject: English</span><span>Time: 2½ Hours</span><span>Max. Marks: 60</span></div>"
                  "<div class='ins'><b>General Instructions:</b><ol><li>The Question Paper is divided into FOUR sections. Section A: Reading 14 marks; Section B: Grammar 14 marks; Section C: Writing 12 marks; Section D: Literature 20 marks.</li><li>Attempt questions based on specific instructions for each part.</li><li>Marks are indicated against each question.</li><li>Read the questions carefully before answering.</li></ol></div>")
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body class='{'key' if key else ''}'><div class='hd'><div class='b'>THE MASTERMIND COACHING CLASSES</div><div class='s'>CBSE / RBSE · Nursery – Class XII · Road No. 5, VKIA, Jaipur · 9887258679</div></div>{head_t}{''.join(out)}</body></html>"

def build(meta, S, outdir, name):
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for key, fn in ((False, f"{name}.pdf"), (True, f"{name}_Answer_Key.pdf")):
            pg.set_content(render(meta, S, key), wait_until='load')
            foot = f"<div style='width:100%;font-size:7.5pt;color:#666;text-align:center;font-family:Arial'>Mastermind Coaching Classes · Class 8 English · Set {meta['set_no']:02d} {'· Answer Key ' if key else ''}| Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>"
            pg.pdf(path=f"{outdir}/{fn}", format='A4', print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=foot, margin=dict(top='12mm', bottom='15mm', left='13mm', right='13mm'))
        br.close()
