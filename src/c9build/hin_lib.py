"""Hindi paper template (Mastermind look, RBSE pattern) — Devanagari fonts, अ/ब/स/द options."""
import html, re, os
import lib
from lib import head as _head, BRAND, TAIL
from eng_lib import mcq, Q, OR, X, P, S, item_marks

HF = "/home/claude/hindi/fonts/node_modules/@fontsource"
HIN_CSS = f"""<style>
@font-face{{font-family:NotoDev;font-weight:400;src:url('file://{HF}/noto-sans-devanagari/files/noto-sans-devanagari-devanagari-400-normal.woff2')}}
@font-face{{font-family:NotoDev;font-weight:600;src:url('file://{HF}/noto-sans-devanagari/files/noto-sans-devanagari-devanagari-600-normal.woff2')}}
@font-face{{font-family:NotoDev;font-weight:700;src:url('file://{HF}/noto-sans-devanagari/files/noto-sans-devanagari-devanagari-700-normal.woff2')}}
body,main{{font-family:NotoDev,Arimo,Arial,sans-serif}}
.ps{{border:1px solid var(--line);border-left:3px solid var(--gold);background:#fcfcfe;padding:3px 8px;margin:2px 0 3px;font-size:calc(var(--fs) - .4pt);text-align:justify}}
.ps p{{margin:0 0 3px}}
.ps .h{{font-weight:700;color:var(--navy);text-align:center;margin-bottom:2px}}
.ps .pt{{text-align:center;line-height:1.5}}
.sq{{display:grid;grid-template-columns:22px 1fr 18px;column-gap:3px;margin:1px 0}}
.sq .l{{color:var(--navy);font-weight:700}}
.sq .m{{color:var(--gold);font-weight:700;text-align:right;font-size:8.2pt}}
.sq .o{{display:grid;grid-template-columns:repeat(2,1fr);column-gap:8px}}
.sq .o.c4{{grid-template-columns:repeat(4,1fr)}}
.sq .o b,.opts span b{{color:var(--navy);margin-right:3px}}
.orw{{text-align:center;color:var(--gold);font-weight:700;letter-spacing:1px;font-size:9pt;margin:0;line-height:1.2}}
.q p{{margin:0}}
.pts{{margin:1px 0 0 0;padding-left:14px}}
.pts li{{margin:0}}
</style>"""
L4 = ["अ", "ब", "स", "द"]
NUM = ["1", "2", "3", "4", "5", "6", "7", "8"]

def head(doc):
    return _head(doc)

def _optcols(opts):
    L = max(len(o) for o in opts)
    if L <= 14: return ""
    if L <= 36: return " c2"
    return " c1"

def hq(n, it, mk):
    txt = it["q"]
    body = txt
    if it["kind"] == "mcq":
        body += f"<div class='opts{_optcols(it['opts'])}'>" + "".join(f"<span><b>{l})</b>{o}</span>" for l, o in zip(L4, it["opts"])) + "</div>"
    num = f"{n}." if n != "" else ""
    return f"<div class='q'><div class='qn'>{num}</div><div>{body}</div><div class='mk'>{mk}</div></div>"

def _subs_html(subs):
    h = ""
    for i, s in enumerate(subs):
        o = ""
        if s.get("opts"):
            L = max(len(x) for x in s["opts"]); cls = "c4" if L <= 10 else ""
            o = f"<div class='o {cls}'>" + "".join(f"<span><b>{l})</b>{x}</span>" for l, x in zip(L4, s["opts"])) + "</div>"
        h += f"<div class='sq'><div class='l'>{NUM[i]})</div><div>{s['q']}{o}</div><div class='m'>{s['mk']}</div></div>"
    return h

def render_block(n, it, default):
    k = it["kind"]
    if k in ("ext", "pas"):
        tot = item_marks(it, default)
        hd = f"<div class='h'>{it['head']}</div>" if it.get("head") else ""
        body = f"<div style='font-size:8.6pt;color:#555;margin-bottom:1px'>{it['title']}</div><div class='ps'>{hd}{it['text']}</div>{_subs_html(it['subs'])}"
        return f"<div class='q' style='break-inside:auto'><div class='qn'>{n}.</div><div>{body}</div><div class='mk'>{tot}</div></div>"
    return hq(n, it, item_marks(it, default))

def render_item(n, it, default):
    if it["kind"] == "or":
        return render_block(n, it["a"], default) + "<div class='orw'>अथवा</div>" + render_block("", it["b"], default)
    return render_block(n, it, default)

def hin_paper(meta, data, fs=10.4):
    lh = 1.52 + 0.02 * (fs - 10)
    h = head(meta["doc"]).replace("<main>", f"<main style='--fs:{fs}pt;--lh:{lh:.3f};--qg:{2+(fs-9.4)*3:.1f}px;--sg:{5+(fs-9.4)*4:.1f}px'>") + HIN_CSS + BRAND
    h += f"""<div class="ttl"><div class="t">{meta['title']} <span class="setpill">सेट {meta['set']}</span></div>
<div class="c">{meta['label']} &nbsp;|&nbsp; RBSE पैटर्न &nbsp;|&nbsp; सत्र 2026–27</div></div>
<div class="tm"><span>समय : {meta['time']}</span><span class="mid">नाम : ____________________ &nbsp; अनुक्रमांक : ________</span><span>पूर्णांक : {meta['marks']}</span></div>
<div class="gi"><b>परीक्षार्थियों के लिए सामान्य निर्देश :</b><ol>""" + "".join(f"<li>{i}</li>" for i in meta["instr"]) + "</ol></div>"
    n = 1; total = 0
    for key, label, mk, sub in meta["secs"]:
        items = data[key]
        tot = sum(item_marks(i, mk) for i in items); total += tot
        h += f"<div class='sec'><span>{label}</span><span class='pill'>{tot} अंक</span></div><div class='sub'>{sub}</div>"
        for it in items:
            h += render_item(n, it, mk); n += 1
    assert total == meta["marks"], (meta["doc"], total, meta["marks"])
    h += f"<div class='end'><span>प्रश्न-पत्र समाप्त</span><span class='pill'>कुल : {meta['marks']} अंक</span></div>"
    return h + TAIL

def _ans_html(a):
    return a if isinstance(a, str) else "<br>".join(a)

def _rows(n, it, default, prefix=""):
    k = it["kind"]
    if k == "mcq":
        idx = "abcd".index(it["ans"])
        return f"<tr><td class='n'>{n}</td><td>{prefix}<b>({L4[idx]})</b> {it['opts'][idx]}" + (f" — <i>{it['why']}</i>" if it.get("why") else "") + f"</td><td class='m'>1</td></tr>"
    if k in ("ext", "pas"):
        rows = ""
        for i, s in enumerate(it["subs"]):
            a = s["ans"]
            if s.get("opts") and len(a) == 1 and a in "abcd":
                a = f"<b>({L4['abcd'.index(a)]})</b> {s['opts']['abcd'.index(a)]}"
            rows += f"<tr><td class='n'>{n if i == 0 else ''}</td><td>{prefix if i == 0 else ''}<b>{NUM[i]})</b> {a}</td><td class='m'>{s['mk']}</td></tr>"
        return rows
    return f"<tr><td class='n'>{n}</td><td>{prefix}{_ans_html(it['ans'])}</td><td class='m'>{item_marks(it, default)}</td></tr>"

def hin_key(meta, data):
    h = head(meta["doc"] + " — उत्तर-कुंजी") + HIN_CSS + BRAND
    h += f"""<div class="ttl"><div class="t">उत्तर-कुंजी एवं अंकन-योजना <span class="setpill">सेट {meta['set']}</span></div>
<div class="c">{meta['label']} &nbsp;|&nbsp; कक्षा 9 हिन्दी &nbsp;|&nbsp; पूर्णांक : {meta['marks']}</div></div>"""
    n = 1
    for key, label, mk, _ in meta["secs"]:
        items = data[key]
        tot = sum(item_marks(i, mk) for i in items)
        h += f"<div class='sec'><span>{re.sub(r'[(][^)]*[)]', '', label).strip()} — उत्तर</span><span class='pill'>{tot} अंक</span></div>"
        h += "<table class='ak'><tr><th style='width:26px'>प्र.</th><th>अपेक्षित उत्तर / मूल्यांकन-बिंदु</th><th style='width:50px;text-align:center'>अंक</th></tr>"
        for it in items:
            if it["kind"] == "or":
                h += _rows(n, it["a"], mk) + _rows("", it["b"], mk, "<span class='orlab'>अथवा:</span> ")
            else:
                h += _rows(n, it, mk)
            n += 1
        h += "</table>"
    h += "<div class='note'><b>मूल्यांकनकर्ता हेतु :</b> दिए गए उत्तर आदर्श उत्तर / मूल्यांकन-बिंदु हैं; परीक्षार्थी द्वारा अपने शब्दों में लिखे गए सही एवं प्रासंगिक उत्तर को भी पूर्ण अंक दें। लेखन-कार्य में अंक प्रारूप, विषय-वस्तु, क्रमबद्धता एवं भाषा की शुद्धता के लिए हैं। आंतरिक विकल्प वाले प्रश्नों में केवल हल किए गए विकल्प का मूल्यांकन करें।</div>"
    return h + TAIL
