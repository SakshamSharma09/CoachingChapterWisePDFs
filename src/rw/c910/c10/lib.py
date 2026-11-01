"""Shared helpers + HTML templates for Mastermind chapter tests."""
import os, html

BUILD = os.path.dirname(os.path.abspath(__file__))
KATEX = os.path.join(BUILD, "node_modules", "katex", "dist")
FONT = os.path.join(BUILD, "node_modules", "@fontsource", "arimo", "files")

# ---------- content constructors ----------
SUBJECT = ["Mathematics"]

def mcq(q, opts, ans, why, fig=None):
    return dict(kind="mcq", q=q, opts=opts, ans=ans, why=why, fig=fig)

def Q(q, ans, split="", fig=None):
    return dict(kind="q", q=q, ans=ans, split=split, fig=fig)

def OR(a, b):
    return dict(kind="or", a=a, b=b)

def table(head, rows):
    """head: list of header cells (first = row label); rows: list of lists"""
    h = "<table class='dt'>"
    h += "<tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join((f"<th>{c}</th>" if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r)) + "</tr>"
    return h + "</table>"

CHAPTERS = {
    1: "Real Numbers", 2: "Polynomials", 3: "Pair of Linear Equations in Two Variables",
    4: "Quadratic Equations", 5: "Arithmetic Progressions", 6: "Triangles",
    7: "Coordinate Geometry", 8: "Introduction to Trigonometry",
    9: "Some Applications of Trigonometry", 10: "Circles",
    11: "Areas Related to Circles", 12: "Surface Areas and Volumes",
    13: "Statistics", 14: "Probability",
}

CSS = r"""
@font-face{font-family:Arimo;font-weight:400;font-style:normal;src:url('file://%(font)s/arimo-latin-400-normal.woff2')}
@font-face{font-family:Arimo;font-weight:700;font-style:normal;src:url('file://%(font)s/arimo-latin-700-normal.woff2')}
@font-face{font-family:Arimo;font-weight:400;font-style:italic;src:url('file://%(font)s/arimo-latin-400-italic.woff2')}
@font-face{font-family:Arimo;font-weight:700;font-style:italic;src:url('file://%(font)s/arimo-latin-700-italic.woff2')}
:root{--navy:#13286b;--gold:#c49a3c;--ink:#1d1d1f;--soft:#f2f5fb;--line:#c9d2e6;}
@page{size:A4;margin:11mm 12mm 13mm 12mm}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff}
main{font-size:var(--fs,10.1pt);line-height:var(--lh,1.36)}
body{font-family:Arimo,Arial,Helvetica,sans-serif;color:var(--ink);font-size:var(--fs,10.1pt);line-height:var(--lh,1.36);
 -webkit-print-color-adjust:exact;print-color-adjust:exact}
.katex{font-size:1.04em}
.wm{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-52deg);font-size:100pt;font-weight:700;
 letter-spacing:6px;color:rgba(19,40,107,.022);z-index:0;white-space:nowrap;pointer-events:none}
main{position:relative;z-index:1}
.hdr{text-align:center;margin-bottom:5px}
.hdr .n{font-size:17.5pt;font-weight:700;color:var(--navy);letter-spacing:1.6px}
.hdr .s{font-size:7.6pt;font-weight:700;color:var(--gold);letter-spacing:2.2px;margin-top:1px}
.hdr .a{font-size:7.2pt;color:#555;margin-top:1px}
.rule{border-top:2.2px solid var(--navy);border-bottom:.8px solid var(--navy);height:3.5px;margin:4px 0 6px}
.ttl{text-align:center}
.ttl .t{font-size:12pt;font-weight:700;color:var(--navy);letter-spacing:.5px}
.ttl .c{font-size:9.2pt;color:#333;margin-top:1px}
.ttl .c b{color:var(--navy)}
.setpill{display:inline-block;background:var(--gold);color:#fff;font-weight:700;border-radius:10px;padding:0 9px;font-size:8.6pt;margin-left:6px;letter-spacing:.8px;vertical-align:1px}
.tm{display:flex;justify-content:space-between;border:1px solid var(--navy);background:var(--soft);padding:3px 9px;
 font-weight:700;color:var(--navy);font-size:9.2pt;margin:5px 0 4px}
.tm .mid{font-weight:400;color:#444;font-size:8.4pt}
.gi{border:1px solid var(--navy);border-radius:4px;background:var(--soft);padding:3px 9px 4px;font-size:7.7pt;color:#333;line-height:1.32}
.gi b{color:var(--navy)}
.gi ol{margin:1px 0 0 0;padding-left:15px;columns:2;column-gap:22px}
.sec{display:flex;justify-content:space-between;align-items:center;background:var(--navy);color:#fff;font-weight:700;
 padding:3px 6px 3px 10px;font-size:9.6pt;margin:var(--sg,7px) 0 2px;break-after:avoid;page-break-after:avoid}
.pill{background:var(--gold);color:var(--navy);border-radius:10px;padding:0 9px;font-size:8.2pt}
.sub{font-style:italic;font-size:8pt;color:#555;margin:0 0 2px 3px;break-after:avoid}
.q{display:grid;grid-template-columns:24px 1fr 20px;column-gap:4px;margin:var(--qg,3px) 0 2px;break-inside:avoid;page-break-inside:avoid}
.qn{font-weight:700;color:var(--navy)}
.mk{font-weight:700;color:var(--gold);text-align:right;font-size:8.8pt}
.opts{display:grid;grid-template-columns:repeat(4,1fr);column-gap:8px;row-gap:0;margin-top:1px}
.opts.c2{grid-template-columns:repeat(2,1fr)}
.opts.c1{grid-template-columns:1fr}
.opts span b{color:var(--navy);margin-right:3px}
.orw{text-align:center;color:var(--gold);font-weight:700;letter-spacing:2px;font-size:8.6pt;margin:0;line-height:1.1}
.fig{float:right;margin:0 0 2px 10px}
.fig svg{display:block}
table.dt{border-collapse:collapse;margin:3px 0 2px;font-size:8.8pt}
table.dt th,table.dt td{border:1px solid var(--line);padding:1px 7px;text-align:center}
table.dt th{background:var(--navy);color:#fff;font-weight:700;white-space:nowrap}
table.dt tr:first-child th{background:#24418f}
.end{display:flex;justify-content:space-between;background:var(--navy);color:#fff;font-weight:700;padding:3px 6px 3px 10px;
 font-size:9.4pt;margin-top:8px;break-inside:avoid}
/* answer key */
table.ak{border-collapse:collapse;width:100%;font-size:8.6pt;margin:2px 0 3px}
table.ak th{background:var(--navy);color:#fff;text-align:left;padding:2px 6px;font-weight:700}
table.ak td{border:1px solid var(--line);padding:2px 6px;vertical-align:top}
table.ak tr:nth-child(even) td{background:#f7f9fd}
table.ak td.n{width:26px;text-align:center;font-weight:700;color:var(--navy)}
table.ak td.m{width:66px;text-align:center;color:#444}
table.ak tr{break-inside:avoid}
.keyhead{text-align:center;margin:3px 0 4px}
.keyhead span{display:inline-block;background:var(--navy);color:#fff;font-weight:700;letter-spacing:3px;border-radius:12px;padding:1px 16px;font-size:9.5pt}
.orlab{color:var(--gold);font-weight:700}
.pb{break-before:page;page-break-before:always}
.note{border-left:3px solid var(--gold);background:#fdf8ec;padding:3px 8px;font-size:8.2pt;margin:5px 0}
"""

HEAD = r"""<!doctype html><html><head><meta charset="utf-8"><title>%(title)s</title>
<link rel="stylesheet" href="file://%(katex)s/katex.min.css">
<script src="file://%(katex)s/katex.min.js"></script>
<script src="file://%(katex)s/contrib/mhchem.min.js"></script>
<script src="file://%(katex)s/contrib/auto-render.min.js"></script>
<style>%(css)s</style></head><body><div class="wm">MASTERMIND</div><main>
"""

TAIL = r"""</main><script>
document.addEventListener('DOMContentLoaded',function(){renderMathInElement(document.body,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:true});
document.fonts.ready.then(function(){window.__done=true;});});
</script></body></html>"""

def head(title):
    return HEAD % dict(title=html.escape(title), katex=KATEX, css=CSS.replace('%(font)s', FONT))

BRAND = """<div class="hdr"><div class="n">THE MASTERMIND COACHING CLASSES</div>
<div class="s">CBSE / RBSE • NURSERY – CLASS XII • JAIPUR</div>
<div class="a">Road No. 5, VKIA, Jaipur — 9887258679</div></div><div class="rule"></div>"""


def _optcols(opts):
    import re
    plain = [re.sub(r"\$[^$]*\$", "xxxxxx", o) for o in opts]
    L = max(len(p) for p in plain)
    if L <= 16: return ""
    if L <= 40: return " c2"
    return " c1"


def render_q(n, item, marks):
    import re
    fig = f"<div class='fig'>{item['fig']}</div>" if item.get("fig") else ""
    txt = item["q"]
    if item["kind"] != "mcq" and "(ii)" in txt:
        txt = re.sub(r"\s\((ii|iii|iv|v)\)\s", r"<br>(\1) ", txt)
        txt = re.sub(r"\s\(i\)\s", r"<br>(i) ", txt)
    if item["kind"] != "mcq" and "(b)" in txt and "(a)" in txt:
        txt = re.sub(r"\s\(([a-e])\)\s", r"<br>(\1) ", txt)
    body = fig + txt
    if item["kind"] == "mcq":
        cls = _optcols(item["opts"])
        body += f"<div class='opts{cls}'>" + "".join(
            f"<span><b>({l})</b>{o}</span>" for l, o in zip("abcd", item["opts"])) + "</div>"
    num = f"{n}." if n != "" else ""
    return f"<div class='q'><div class='qn'>{num}</div><div>{body}</div><div class='mk'>{marks}</div></div>"


def render_item(n, item, marks):
    if item["kind"] == "or":
        a = render_q(n, item["a"], marks)
        b = render_q("", item["b"], marks)
        return a + "<div class='orw'>OR</div>" + b
    return render_q(n, item, marks)


SECTIONS = [("A", "SECTION — A (Objective Type Questions)", 1, "Choose the correct option and write it in your answer book."),
            ("B", "SECTION — B (Very Short Answer Type)", 2, "Answer in about 20–30 words each."),
            ("C", "SECTION — C (Short Answer Type)", 3, "Answer in about 40–60 words each."),
            ("D", "SECTION — D (Long Answer Type)", 5, "Answer in about 100–150 words each.")]


def paper_html(ch, setname, data, fs=10.1):
    name = CHAPTERS[ch]
    title = f"Ch {ch:02d} {name} — Set {setname}"
    h = head(title).replace("<main>", f"<main style='--fs:{fs}pt;--lh:{1.30+0.03*(fs-9.4):.3f};--qg:{2+ (fs-9.4)*3:.1f}px;--sg:{5+(fs-9.4)*4:.1f}px'>") + BRAND
    h += f"""<div class="ttl"><div class="t">CLASS 10 — MATHEMATICS CHAPTER TEST <span class="setpill">SET {setname}</span></div>
<div class="c">Chapter {ch}: <b>{name}</b> &nbsp;|&nbsp; RBSE Board Pattern &nbsp;|&nbsp; Session 2026–27</div></div>
<div class="tm"><span>Time: 1 Hour 30 Minutes</span><span class="mid">Name: ____________________ &nbsp; Roll No.: ________</span><span>Maximum Marks: 40</span></div>
<div class="gi"><b>General Instructions:</b><ol>
<li>All questions are compulsory.</li>
<li>Q. 1–10 are Objective Type (1 mark each).</li>
<li>Q. 11–14 are Very Short Answer Type (2 marks each).</li>
<li>Q. 15–18 are Short Answer Type (3 marks each).</li>
<li>Q. 19–20 are Long Answer Type (5 marks each).</li>
<li>Internal choice is given in Q. 17 to 20.</li>
<li>Write the question number before each answer.</li>
<li>{data.get('note','Draw neat figures wherever required.')}</li></ol></div>"""
    n = 1
    for key, label, mk, sub in SECTIONS:
        items = data[key]
        tot = len(items) * mk
        h += f"<div class='sec'><span>{label}</span><span class='pill'>{len(items)} × {mk} = {tot}</span></div><div class='sub'>{sub}</div>"
        for it in items:
            h += render_item(n, it, mk)
            n += 1
    h += "<div class='end'><span>END OF QUESTION PAPER</span><span class='pill'>Total: 40 Marks</span></div>"
    return h + TAIL


def _ans_row(n, item, mk, lab=""):
    split = item.get("split") or str(mk)
    return f"<tr><td class='n'>{n}</td><td>{lab}{item['ans']}</td><td class='m'>{split}</td></tr>"


def key_html(ch, sets):
    name = CHAPTERS[ch]
    h = head(f"Ch {ch:02d} {name} — Answer Key") + BRAND
    first = True
    for setname, data in sets.items():
        if not first:
            h += "<div class='pb'></div>" + BRAND
        first = False
        h += f"""<div class="ttl"><div class="t">ANSWER KEY &amp; MARKING SCHEME <span class="setpill">SET {setname}</span></div>
<div class="c">Chapter {ch}: <b>{name}</b> &nbsp;|&nbsp; Class 10 Mathematics &nbsp;|&nbsp; Maximum Marks: 40</div></div>"""
        h += "<div class='sec'><span>SECTION — A (Objective Type)</span><span class='pill'>10 × 1 = 10</span></div>"
        h += "<table class='ak'><tr><th style='width:26px'>Q.</th><th style='width:38%'>Correct Option</th><th>Brief Reasoning</th></tr>"
        for i, it in enumerate(data["A"], 1):
            idx = "abcd".index(it["ans"])
            h += f"<tr><td class='n'>{i}</td><td><b>({it['ans']})</b> {it['opts'][idx]}</td><td>{it['why']}</td></tr>"
        h += "</table>"
        n = 11
        for key, label, mk, _ in SECTIONS[1:]:
            items = data[key]
            h += f"<div class='sec'><span>{label.replace(' Type','')} — Answers</span><span class='pill'>{len(items)} × {mk} = {len(items)*mk}</span></div>"
            h += "<table class='ak'><tr><th style='width:26px'>Q.</th><th>Expected Answer / Value Points</th><th style='width:66px;text-align:center'>Marks</th></tr>"
            for it in items:
                if it["kind"] == "or":
                    h += _ans_row(n, it["a"], mk)
                    h += _ans_row("", it["b"], mk, "<span class='orlab'>OR:</span> ")
                else:
                    h += _ans_row(n, it, mk)
                n += 1
            h += "</table>"
        h += "<div class='note'><b>Evaluator's note:</b> Award step marks as shown; accept any correct alternative method. In internal-choice questions, evaluate only the option attempted. Deduct up to ½ mark for missing units or figures where required.</div>"
    return h + TAIL


def to_pdf(page, html_str, out_pdf, footer_left):
    tmp = out_pdf[:-4] + ".html"
    with open(tmp, "w") as f:
        f.write(html_str)
    page.goto("file://" + tmp)
    page.wait_for_function("window.__done === true", timeout=20000)
    page.pdf(path=out_pdf, format="A4", print_background=True, display_header_footer=True,
             header_template="<span></span>",
             footer_template=f"""<div style="width:100%;font-family:Arial;font-size:7px;margin:0 12mm;display:flex;justify-content:space-between;border-top:.7px solid #13286b;padding-top:2px;color:#13286b">
<span>{html.escape(footer_left)}</span><span style="color:#c49a3c;font-weight:bold">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>""",
             margin=dict(top="11mm", bottom="13mm", left="12mm", right="12mm"))
    os.remove(tmp)


def plot_svg(f, x0, x1, y0, y1, w=190, h=150, xt=None, label="y = p(x)", dots=()):
    """Small graph: axes, unit ticks, curve f, optional highlighted points."""
    sx = lambda x: (x - x0) / (x1 - x0) * w
    sy = lambda y: h - (y - y0) / (y1 - y0) * h
    pts = []
    N = 240
    for i in range(N + 1):
        x = x0 + (x1 - x0) * i / N
        y = max(min(f(x), y1), y0)
        pts.append(f"{sx(x):.1f},{sy(y):.1f}")
    s = f"<svg width='{w}' height='{h}' viewBox='-4 -4 {w+8} {h+8}' xmlns='http://www.w3.org/2000/svg' font-family='Arial' font-size='9'>"
    s += f"<rect x='-4' y='-4' width='{w+8}' height='{h+8}' fill='#f7f9fd' stroke='#c9d2e6'/>"
    s += f"<line x1='0' y1='{sy(0):.1f}' x2='{w}' y2='{sy(0):.1f}' stroke='#333' stroke-width='.9'/>"
    s += f"<line x1='{sx(0):.1f}' y1='0' x2='{sx(0):.1f}' y2='{h}' stroke='#333' stroke-width='.9'/>"
    for t in (xt or range(int(x0), int(x1) + 1)):
        if t == 0: continue
        s += f"<line x1='{sx(t):.1f}' y1='{sy(0)-2:.1f}' x2='{sx(t):.1f}' y2='{sy(0)+2:.1f}' stroke='#333'/>"
        s += f"<text x='{sx(t):.1f}' y='{sy(0)+11:.1f}' text-anchor='middle'>{t}</text>"
    s += f"<text x='{w-6}' y='{sy(0)-4:.1f}' font-style='italic'>X</text><text x='{sx(0)+4:.1f}' y='8' font-style='italic'>Y</text>"
    s += f"<text x='{sx(0)-8:.1f}' y='{sy(0)+11:.1f}'>O</text>"
    s += f"<polyline points='{' '.join(pts)}' fill='none' stroke='#13286b' stroke-width='1.8'/>"
    for (x, y) in dots:
        s += f"<circle cx='{sx(x):.1f}' cy='{sy(y):.1f}' r='2.6' fill='#c49a3c'/>"
    s += f"<text x='{w*0.62:.0f}' y='12' fill='#13286b' font-style='italic'>{label}</text>"
    return s + "</svg>"


# ---------------- generic multi-level papers ----------------
def ch_label(chs):
    if len(chs) == 1:
        return f"Chapter {chs[0]}: <b>{CHAPTERS[chs[0]]}</b>"
    if len(chs) == len(CHAPTERS):
        return f"<b>Full Syllabus (Chapters 1–{len(CHAPTERS)})</b>"
    nums = " &amp; ".join(str(c) for c in chs) if len(chs) == 2 else f"{chs[0]}–{chs[-1]}"
    names = ", ".join(CHAPTERS[c] for c in chs)
    return f"Chapters {nums}: <b>{names}</b>"


def generic_paper(meta, data, fs=10.1):
    """meta: title, chs, time, marks, secs=[(key,label,mk,sub)], instr=[...]"""
    h = head(meta["doc"]).replace("<main>", f"<main style='--fs:{fs}pt;--lh:{1.30+0.03*(fs-9.4):.3f};--qg:{2+(fs-9.4)*3:.1f}px;--sg:{5+(fs-9.4)*4:.1f}px'>") + BRAND
    h += f"""<div class="ttl"><div class="t">{meta['title']} <span class="setpill">SET {meta['set']}</span></div>
<div class="c">{ch_label(meta['chs'])} &nbsp;|&nbsp; RBSE Board Pattern &nbsp;|&nbsp; Session 2026–27</div></div>
<div class="tm"><span>Time: {meta['time']}</span><span class="mid">Name: ____________________ &nbsp; Roll No.: ________</span><span>Maximum Marks: {meta['marks']}</span></div>
<div class="gi"><b>General Instructions:</b><ol>""" + "".join(f"<li>{i}</li>" for i in meta["instr"]) + "</ol></div>"
    n = 1
    for key, label, mk, sub in meta["secs"]:
        items = data[key]
        h += f"<div class='sec'><span>{label}</span><span class='pill'>{len(items)} × {mk} = {len(items)*mk}</span></div><div class='sub'>{sub}</div>"
        for it in items:
            h += render_item(n, it, mk)
            n += 1
    h += f"<div class='end'><span>END OF QUESTION PAPER</span><span class='pill'>Total: {meta['marks']} Marks</span></div>"
    return h + TAIL


def generic_key(meta, data):
    h = head(meta["doc"] + " — Answer Key") + BRAND
    h += f"""<div class="ttl"><div class="t">ANSWER KEY &amp; MARKING SCHEME <span class="setpill">SET {meta['set']}</span></div>
<div class="c">{ch_label(meta['chs'])} &nbsp;|&nbsp; Class 10 {SUBJECT[0]} &nbsp;|&nbsp; Maximum Marks: {meta['marks']}</div></div>"""
    n = 1
    for key, label, mk, _ in meta["secs"]:
        items = data[key]
        if key == "A":
            h += f"<div class='sec'><span>{label.replace(' Questions','')} — Answers</span><span class='pill'>{len(items)} × 1 = {len(items)}</span></div>"
            h += "<table class='ak'><tr><th style='width:26px'>Q.</th><th style='width:38%'>Correct Option</th><th>Brief Reasoning</th></tr>"
            for it in items:
                idx = "abcd".index(it["ans"])
                h += f"<tr><td class='n'>{n}</td><td><b>({it['ans']})</b> {it['opts'][idx]}</td><td>{it['why']}</td></tr>"
                n += 1
            h += "</table>"
            continue
        h += f"<div class='sec'><span>{label.replace(' Type','')} — Answers</span><span class='pill'>{len(items)} × {mk} = {len(items)*mk}</span></div>"
        h += "<table class='ak'><tr><th style='width:26px'>Q.</th><th>Expected Answer / Value Points</th><th style='width:66px;text-align:center'>Marks</th></tr>"
        for it in items:
            if it["kind"] == "or":
                h += _ans_row(n, it["a"], mk)
                h += _ans_row("", it["b"], mk, "<span class='orlab'>OR:</span> ")
            else:
                h += _ans_row(n, it, mk)
            n += 1
        h += "</table>"
    h += "<div class='note'><b>Evaluator's note:</b> Award step marks as shown; accept any correct alternative method. In internal-choice questions, evaluate only the option attempted. Deduct up to ½ mark for missing units or figures where required.</div>"
    return h + TAIL
