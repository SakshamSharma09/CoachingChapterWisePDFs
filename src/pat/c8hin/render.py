"""Class 8 Hindi (Delhi DoE pattern, 60 marks, 2.30 h) renderer.  Devanagari via Noto Sans Devanagari (fontsource)."""
import os, html
from playwright.sync_api import sync_playwright
HF = "file:///home/claude/hindi/fonts/node_modules/@fontsource"
CSS = f"""
@font-face{{font-family:NotoDev;font-weight:400;src:url('{HF}/noto-sans-devanagari/files/noto-sans-devanagari-devanagari-400-normal.woff2')}}
@font-face{{font-family:NotoDev;font-weight:600;src:url('{HF}/noto-sans-devanagari/files/noto-sans-devanagari-devanagari-600-normal.woff2')}}
@font-face{{font-family:NotoDev;font-weight:700;src:url('{HF}/noto-sans-devanagari/files/noto-sans-devanagari-devanagari-700-normal.woff2')}}
@page{{size:A4;margin:12mm 14mm 14mm 14mm}}
*{{box-sizing:border-box}}
body{{font-family:NotoDev,Arimo,'Liberation Sans',Arial,sans-serif;font-size:10.2pt;line-height:1.5;color:#111;margin:0}}
.hd{{text-align:center;border-bottom:2px solid #0f2347;padding-bottom:1.5mm;margin-bottom:1.5mm}}
.hd .b{{font-family:Arimo,Arial;font-size:14pt;font-weight:700;color:#0f2347;letter-spacing:.06em}}
.hd .s{{font-family:Arimo,Arial;font-size:8pt;color:#444}}
.tt{{text-align:center;font-weight:700;font-size:12pt}}
.meta{{display:flex;justify-content:space-between;border-top:1px solid #999;border-bottom:1px solid #999;padding:.8mm 0;margin:1mm 0 1.5mm;font-size:10pt}}
.ins{{font-size:9.6pt;margin-bottom:1mm}} .ins ul{{margin:0;padding-left:5mm}}
.khand{{text-align:center;font-weight:700;font-size:11.5pt;color:#fff;background:#0f2347;padding:.6mm 0;margin:3mm 0 1.5mm;page-break-after:avoid}}
.q{{margin:0 0 2.6mm}}
.qh{{display:flex;justify-content:space-between;gap:3mm;font-weight:600;page-break-after:avoid}}
.qh .mk{{white-space:nowrap;font-weight:600}}
.ps{{break-inside:avoid;border:1px solid #bbb;border-left:3px solid #c9a227;background:#fcfcfe;padding:1.2mm 3mm;margin:1mm 0 1.5mm;text-align:justify}}
.ps.poem{{text-align:left;line-height:1.55}}
.ps p{{margin:0 0 1mm}}
.pt{{text-align:center;font-weight:700;margin-bottom:.5mm}}
.pa{{display:flex;gap:2mm;margin:.8mm 0;page-break-inside:avoid}}
.pa .l{{width:9mm;flex:none}} .pa .b{{flex:1}} .pa .m{{width:7mm;flex:none;text-align:right;font-weight:600}}
.opts{{display:grid;grid-template-columns:1fr 1fr;column-gap:6mm}} .opts.c4{{grid-template-columns:repeat(4,1fr)}}
.orr{{text-align:center;font-weight:700;margin:1mm 0;letter-spacing:.15em}}
table.t{{border-collapse:collapse;margin:1mm 0;width:70%}} table.t td,table.t th{{border:1px solid #444;padding:.5mm 3mm}}
.sol{{background:#f3f5fa;border-left:3px solid #0f2347;padding:.8mm 2.5mm;margin:.6mm 0;font-size:9.6pt}}
.ans{{font-weight:700;color:#0f2347}}
ul.pts{{margin:0;padding-left:5mm}}
"""
LAB = ['(क)', '(ख)', '(ग)', '(घ)']; ROM = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
def P(q, m, ans='', sol='', opts=None, table=None): return dict(q=q, m=m, ans=ans, sol=sol, opts=opts, table=table)

def _opts(o):
    L = max(len(x) for x in o)
    return f"<div class='opts{' c4' if L<=7 else ''}'>" + "".join(f"<div>{LAB[i]} {x}</div>" for i, x in enumerate(o)) + "</div>"
def _table(t): return "<table class='t'>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in t) + "</table>"
def _part(p, lab, key, m=None):
    mm = p['m'] if m is None else m
    body = p['q'] + (_table(p['table']) if p.get('table') else '') + (_opts(p['opts']) if p.get('opts') else '')
    if key:
        a = p['ans']
        if p.get('opts') and isinstance(a, int): a = f"{LAB[a]} {p['opts'][a]}"
        body += f"<div class='sol'><span class='ans'>उत्तर:</span> {a}" + (f" — {p['sol']}" if p.get('sol') else '') + "</div>"
    return f"<div class='pa'><div class='l'>{lab}</div><div class='b'>{body}</div><div class='m'>{'' if key else mm}</div></div>"

def qmarks(q):
    k = q['kind']
    if k == 'plain': return sum(p['m'] for p in q['parts'])
    if k == 'any2': return 2 * q['parts'][0]['m']
    if k in ('or', 'topics'): return q['m']
def paper_marks(paper): return sum(qmarks(q) for s in paper['sections'] for q in s['qs'])

def _q(q, key):
    h = f"<div class='qh'><div>प्रश्न {q['n']}. {q['instr']}</div><div class='mk'>{q.get('mknote','')}</div></div>"
    out = [h]
    if q.get('passage'):
        cls = 'poem' if q.get('poem') else ''
        t = f"<div class='pt'>{q['ptitle']}</div>" if q.get('ptitle') else ''
        out.append(f"<div class='ps {cls}'>{t}{q['passage']}</div>")
    k = q['kind']
    if k in ('plain', 'any2'):
        for i, p in enumerate(q['parts']): out.append(_part(p, f"({ROM[i]})", key))
    elif k == 'or':
        out.append(f"<div class='pa'><div class='l'></div><div class='b'>{q['a']['q']}"
                   + (f"<div class='sol'><span class='ans'>उत्तर (आदर्श पत्र):</span><br>{q['a']['sol']}</div>" if key else '') + "</div></div>")
        out.append("<div class='orr'>अथवा</div>")
        out.append(f"<div class='pa'><div class='l'></div><div class='b'>{q['b']['q']}"
                   + (f"<div class='sol'><span class='ans'>उत्तर (आदर्श पत्र):</span><br>{q['b']['sol']}</div>" if key else '') + "</div></div>")
    elif k == 'topics':
        for i, (title, hints, sol) in enumerate(q['topics']):
            out.append(f"<div class='pa'><div class='l'>({['क','ख','ग'][i]})</div><div class='b'><b>{title}</b><ul class='pts'>" + "".join(f"<li>{h}</li>" for h in hints) + "</ul>"
                       + (f"<div class='sol'><span class='ans'>आदर्श अनुच्छेद:</span> {sol}</div>" if key and sol else '') + "</div></div>")
        if key: out.append("<div class='sol'>अंक-विभाजन (किसी भी विषय के लिए): तीनों संकेत-बिंदुओं का समावेश एवं विषय-वस्तु 3, भाषा-शुद्धता 2, क्रमबद्धता/प्रस्तुति 1।</div>")
    return f"<div class='q'>{''.join(out)}</div>"

INSTR = ["इस प्रश्न पत्र में कुल चार खंड हैं- ‘क’, ‘ख’, ‘ग’ और ‘घ’।", "इस प्रश्न पत्र में कुल 11 प्रश्न हैं, सभी प्रश्न अनिवार्य हैं।",
         "इस प्रश्न पत्र में आंतरिक विकल्प दिए गए हैं।", "प्रश्नों के उत्तर दिए गए निर्देशों का पालन करते हुए लिखिए।",
         "यथासंभव प्रत्येक खंड के प्रश्नों के उत्तर क्रमशः लिखिए।"]

def html_doc(paper, key=False):
    assert paper_marks(paper) == 60, paper_marks(paper)
    n = paper['set_no']
    if key:
        head = (f"<div class='tt'>उत्तर-कुंजी एवं अंक-योजना — कक्षा 8 · हिंदी · सेट {n:02d}</div>"
                f"<div class='meta'><span>अधिकतम अंक: 60</span><span>समय: 2.30 घंटे</span><span>अन्य उचित उत्तरों को भी पूर्ण अंक दिए जाएँ।</span></div>")
    else:
        head = (f"<div class='tt'>मध्यावधि अभ्यास प्रश्न पत्र (2026-27) · कक्षा-8 · विषय : हिंदी · सेट {n:02d}</div>"
                f"<div class='meta'><span>निर्धारित समय : 2.30 घंटे</span><span>अधिकतम अंक : 60</span></div>"
                f"<div class='ins'><b>सामान्य निर्देश :</b> निम्नलिखित निर्देशों को पढ़कर उनका पालन कीजिए :<ul>{''.join(f'<li>{i}</li>' for i in INSTR)}</ul></div>")
    body = []
    for s in paper['sections']:
        body.append(f"<div class='khand'>{s['title']}</div>")
        for q in s['qs']: body.append(_q(q, key))
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='hd'><div class='b'>THE MASTERMIND COACHING CLASSES</div><div class='s'>CBSE / RBSE · Nursery – Class XII · Road No. 5, VKIA, Jaipur · 9887258679</div></div>{head}{''.join(body)}</body></html>"

def build(paper, outdir):
    os.makedirs(outdir, exist_ok=True); n = paper['set_no']
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for key, fn in ((False, f"Set_{n:02d}.pdf"), (True, f"Set_{n:02d}_Answer_Key.pdf")):
            hp = f"/tmp/c8h/_{fn}.html"; open(hp, 'w').write(html_doc(paper, key)); pg.goto('file://' + hp); pg.wait_for_timeout(400)
            foot = f"<div style='width:100%;font-size:7.5pt;color:#666;text-align:center;font-family:Arial'>Mastermind Coaching Classes · Class 8 Hindi · Set {n:02d} {'· Answer Key ' if key else ''}| Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>"
            pg.pdf(path=f"{outdir}/{fn}", format='A4', print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=foot, margin=dict(top='12mm', bottom='15mm', left='14mm', right='14mm'))
        br.close()

def Q(n, instr, kind, parts=None, passage=None, mknote='', poem=False, ptitle=None, **kw):
    return dict(n=n, instr=instr, kind=kind, parts=parts, passage=passage, mknote=mknote, poem=poem, ptitle=ptitle, **kw)
