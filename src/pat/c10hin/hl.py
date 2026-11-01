"""Class 10 Hindi-A school-pattern builder (Delhi DoE style). Devanagari."""
import os, html, re
from playwright.sync_api import sync_playwright
HF = "/home/claude/hindi/fonts/node_modules/@fontsource/noto-sans-devanagari/files"
CSS = f"""
@font-face{{font-family:ND;font-weight:400;src:url('file://{HF}/noto-sans-devanagari-devanagari-400-normal.woff2')}}
@font-face{{font-family:ND;font-weight:700;src:url('file://{HF}/noto-sans-devanagari-devanagari-700-normal.woff2')}}
@page{{size:A4;margin:12mm 14mm 15mm 14mm}}
*{{box-sizing:border-box}} body{{font-family:ND,'Noto Sans Devanagari',Arimo,Arial,sans-serif;font-size:10.2pt;line-height:1.5;color:#111;margin:0}}
.hd{{text-align:center;border-bottom:2px solid #0f2347;padding-bottom:2mm;margin-bottom:2mm}}.hd .b{{font-size:15pt;font-weight:700;color:#0f2347}}.hd .s{{font-size:8.5pt;color:#444}}
.tt{{text-align:center;font-weight:700;font-size:12.5pt}}.tt2{{text-align:center;font-size:9.5pt;color:#333;margin-bottom:1.5mm}}
.meta{{display:flex;justify-content:space-between;border-top:1px solid #999;border-bottom:1px solid #999;padding:1mm 0;margin-bottom:2mm}}
.ins{{font-size:9.6pt;margin-bottom:2mm}}.ins ul{{margin:.5mm 0 0 4mm;padding-left:3mm}}
.sec{{text-align:center;font-weight:700;margin:3.5mm 0 1.5mm;page-break-after:avoid}}.sec small{{display:block;font-weight:700}}
.q{{margin:0 0 2.6mm}}.qh{{display:flex;gap:2mm;page-break-after:avoid}}.qh .t{{flex:1;text-align:justify}}.qh .m{{width:14mm;text-align:right;flex:none;font-weight:700}}
.ps{{border:1px solid #bbb;border-left:3px solid #c9a227;background:#fcfcfe;padding:1.5mm 3mm;margin:1mm 0 1.5mm;text-align:justify}}.ps.pt{{text-align:left;line-height:1.7}}
.p{{display:flex;gap:1.5mm;margin:.6mm 0;page-break-inside:avoid}}.p .l{{width:9mm;flex:none}}.p .b{{flex:1}}.p .m{{width:8mm;flex:none;text-align:right}}
.o{{margin:.3mm 0 .3mm 5mm}}.st{{margin:.2mm 0 .2mm 4mm}}
.orr{{text-align:center;font-weight:700;margin:1mm 0}}
.key .sol{{background:#f1f4fa;border-left:3px solid #0f2347;padding:.8mm 2.5mm;margin:.6mm 0 1mm;font-size:9.6pt}}.ans{{font-weight:700;color:#0f2347}}
"""
ROM = ["I", "II", "III", "IV"]; IDX = ["(i)", "(ii)", "(iii)", "(iv)"]; HL = ["क", "ख", "ग", "घ", "ङ"]
def opts(lst): return lst
def part(q, m, o=None, ans="", sol="", stm=None):
    return dict(q=q, m=m, o=o, ans=ans, sol=sol, stm=stm)
def ST(q, stmts, true, extra=None):
    """statements-selection MCQ; true = tuple of indices that are correct. extra: decoy sets."""
    import itertools
    def name(s):
        r = [ROM[i] for i in s]
        if len(r) == 1: return f"केवल कथन {r[0]} सही है।"
        return "कथन " + (", ".join(r[:-1]) + " और " + r[-1] if len(r) > 2 else r[0] + " और " + r[1]) + " सही हैं।"
    true = tuple(sorted(true)); n = len(true)
    cands = [c for k in (2, 3, 1) for c in itertools.combinations(range(4), k) if c != true]
    dec = [tuple(sorted(c)) for c in (extra or [])]
    dec += [c for c in cands if c not in dec and len(c) in (n, 2)]
    dec = [d for d in dec if d != true][:3]
    allo = sorted([true] + dec, key=lambda c: (len(c), c))
    return dict(q=q, stm=stmts, o=[name(c) for c in allo], ans=IDX[allo.index(true)], kind="st")
AR_O = ["कथन सही है लेकिन कारण कथन की सही व्याख्या नहीं है।", "कथन गलत है, किंतु कारण सही है।", "कथन सही है और कारण, कथन की सही व्याख्या है।", "कथन और कारण दोनों गलत हैं।"]
def AR(kathan, karan, ans):
    """ans: 0..3 index into AR_O."""
    return dict(q=f"कथन : {kathan}<br>कारण : {karan}", stm=None, o=AR_O, ans=IDX[ans], kind="ar")
def M(q, o, ans):  # plain MCQ, ans index
    return dict(q=q, stm=None, o=o, ans=IDX[ans], kind="m")
def sub(item, m=1, sol=""):
    d = dict(item); d.setdefault("kind", "m"); d["m"] = m
    d["sol"] = sol or (d.get("sol") or ""); return d
def READ(n, intro, text, parts, poem=False): return dict(t="read", n=n, intro=intro, text=text, parts=parts, poem=poem)
def ANY(n, intro, take, each, items): return dict(t="any", n=n, intro=intro, take=take, each=each, items=items)   # items [(q,ans)]
def WRITE(n, intro, marks, opts_, label="अथवा"): return dict(t="write", n=n, intro=intro, marks=marks, opts=opts_)  # opts_ [(prompt, sample)]
def TOPICS(n, intro, marks, topics): return dict(t="topics", n=n, intro=intro, marks=marks, topics=topics)  # topics [(title,[bullets],sample)]

def qmarks(b):
    t = b["t"]
    if t == "read": return sum(p["m"] for p in b["parts"])
    if t == "any": return b["take"] * b["each"]
    return b["marks"]

def _p_html(p, i, key, lab=None):
    lab = lab or f"({HL[i]})"
    h = f"<div class='b'>{p['q']}"
    if p.get("stm"): h += "".join(f"<div class='st'>{ROM[j]}. {s}</div>" for j, s in enumerate(p["stm"]))
    if p.get("o"):
        if p.get("kind") in ("st",) or p.get("stm") or p.get("kind") == "ar": h += "".join(f"<div class='o'>{IDX[j]} &nbsp;{o}</div>" for j, o in enumerate(p["o"]))
        else:
            h += "".join(f"<div class='o'>{IDX[j]} &nbsp;{o}</div>" for j, o in enumerate(p["o"]))
    if key: h += f"<div class='sol'><span class='ans'>उत्तर : {p['ans']}</span> {p.get('sol','')}</div>"
    h += "</div>"
    return f"<div class='p'><div class='l'>{lab}</div>{h}<div class='m'>{'' if key else '('+str(p['m'])+')'}</div></div>"

def block_html(b, key):
    t = b["t"]; n = b["n"]; tot = qmarks(b)
    head = f"<div class='qh'><div class='t'><b>प्रश्न {n}.</b> {b['intro']}</div><div class='m'>{'' if key else ('('+str(tot)+')')}</div></div>"
    if t == "read":
        box = f"<div class='ps{' pt' if b['poem'] else ''}'>{b['text']}</div>"
        if key: return f"<div class='q'><div class='qh'><div class='t'><b>प्रश्न {n}.</b> (अंक {tot})</div></div>" + "".join(_p_html(p, i, True) for i, p in enumerate(b["parts"])) + "</div>"
        return f"<div class='q'>{head}{box}" + "".join(_p_html(p, i, False) for i, p in enumerate(b["parts"])) + "</div>"
    if t == "any":
        if key:
            body = "".join(f"<div class='p'><div class='l'>({HL[i]})</div><div class='b'>{q}<div class='sol'>{a}</div></div></div>" for i, (q, a) in enumerate(b["items"]))
            return f"<div class='q'><div class='qh'><div class='t'><b>प्रश्न {n}.</b> ({b['take']}×{b['each']}={tot} अंक)</div></div>{body}</div>"
        body = "".join(f"<div class='p'><div class='l'>({HL[i]})</div><div class='b'>{q}</div></div>" for i, (q, a) in enumerate(b["items"]))
        return f"<div class='q'>{head}{body}</div>"
    if t == "write":
        parts = []
        for i, (pr, sm) in enumerate(b["opts"]):
            if i: parts.append("<div class='orr'>अथवा</div>")
            parts.append(f"<div class='p'><div class='l'>({HL[i]})</div><div class='b'>{pr}" + (f"<div class='sol'>{sm}</div>" if key else "") + "</div></div>")
        return f"<div class='q'>{head if not key else '<div class=qh><div class=t><b>प्रश्न '+str(n)+'.</b> (अंक '+str(tot)+')</div></div>'}{''.join(parts)}</div>"
    if t == "topics":
        parts = []
        for i, (ti, bl, sm) in enumerate(b["topics"]):
            parts.append(f"<div class='p'><div class='l'>({HL[i]})</div><div class='b'><b>{ti}</b>" + "".join(f"<div class='o'>• {x}</div>" for x in bl) + (f"<div class='sol'>{sm}</div>" if key else "") + "</div></div>")
        return f"<div class='q'>{head if not key else '<div class=qh><div class=t><b>प्रश्न '+str(n)+'.</b> (अंक '+str(tot)+')</div></div>'}{''.join(parts)}</div>"

def paper_html(meta, sections, key=False):
    total = 0; body = []
    for title, sub_, blocks in sections:
        body.append(f"<div class='sec'>{title}<small>({sub_})</small></div>")
        for b in blocks:
            total += qmarks(b); body.append(block_html(b, key))
    assert total == 80, f"marks {total}"
    if key:
        head = f"<div class='tt'>उत्तर-कुंजी एवं अंकन-योजना — हिंदी-अ (कोड 002) · कक्षा-दसवीं · सेट {meta['set']:02d}</div><div class='tt2'>अधिकतम अंक : 80 · द मास्टरमाइंड कोचिंग क्लासेस, जयपुर · अन्य उपयुक्त उत्तर/बिंदुओं को भी अंक दिए जाएँ</div>"
    else:
        ins = "".join(f"<li>{x}</li>" for x in meta["instr"])
        head = (f"<div class='tt'>मध्यावधि/पूर्ण पाठ्यक्रम अभ्यास प्रश्न-पत्र (सत्र : 2026-2027)</div><div class='tt2'>कक्षा-दसवीं · हिंदी-अ (कोड 002) · सेट {meta['set']:02d}</div>"
                f"<div class='meta'><span>निर्धारित समय : 3 घंटे</span><span>नाम : ____________ अनुक्रमांक : _____</span><span>अधिकतम अंक : 80</span></div>"
                f"<div class='ins'><b>सामान्य निर्देश :</b><ul>{ins}</ul></div>")
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body class='{'key' if key else ''}'><div class='hd'><div class='b'>द मास्टरमाइंड कोचिंग क्लासेस</div><div class='s'>CBSE / RBSE · नर्सरी – कक्षा XII · रोड नं. 5, VKIA, जयपुर · 9887258679</div></div>{head}{''.join(body)}</body></html>"

INSTR = ["इस प्रश्न पत्र में कुल चार खंड हैं- क, ख, ग और घ।", "इस प्रश्न पत्र में कुल 15 प्रश्न हैं। सभी प्रश्न अनिवार्य हैं।", "प्रश्नों में आंतरिक विकल्प दिए गए हैं।", "प्रश्नों के उत्तर दिए गए निर्देशों का पालन करते हुए लिखिए।"]

def build(set_no, sections, outdir):
    os.makedirs(outdir, exist_ok=True)
    meta = dict(set=set_no, instr=INSTR)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        for key, fn in ((False, f"Hindi_A_Set_{set_no:02d}.pdf"), (True, f"Hindi_A_Set_{set_no:02d}_Answer_Key.pdf")):
            f = f"/tmp/hin_{set_no}_{int(key)}.html"
            open(f, "w").write(paper_html(meta, sections, key)); pg.goto("file://" + f); pg.wait_for_timeout(400)
            foot = f"<div style='width:100%;font-size:7.5pt;color:#666;text-align:center;font-family:Arial'>Mastermind Coaching Classes · Class 10 Hindi-A · Set {set_no:02d} {'· Answer Key ' if key else ''}| Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>"
            pg.pdf(path=f"{outdir}/{fn}", format="A4", print_background=True, display_header_footer=True, header_template="<div></div>", footer_template=foot, margin=dict(top="12mm", bottom="15mm", left="14mm", right="14mm"))
        br.close()
