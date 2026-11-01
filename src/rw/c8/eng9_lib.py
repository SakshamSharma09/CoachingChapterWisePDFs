"""English paper template (same look as the Mastermind papers) with per-item marks,
extract-based and passage-based questions."""
import html, re
import lib
from lib import head, BRAND, TAIL, render_q

def mcq(q, opts, ans, why=""):
    return dict(kind="mcq", q=q, opts=opts, ans=ans, why=why)
def Q(q, ans, mk=None):
    return dict(kind="q", q=q, ans=ans, mk=mk)
def OR(a, b):
    return dict(kind="or", a=a, b=b)
def X(text, subs, title="Read the following extract and answer the questions that follow."):
    """extract-based: subs = [(question, answer), ...] each 1 mark"""
    return dict(kind="ext", text=text, subs=[dict(q=q, ans=a, mk=1) for q, a in subs], title=title)
def P(text, subs, title="Read the passage carefully and answer the questions that follow.", head_=""):
    """passage/data based: subs = [dict(q, ans, mk, opts=None)]"""
    return dict(kind="pas", text=text, subs=subs, title=title, head=head_)
def S(q, ans, mk=1, opts=None):
    return dict(q=q, ans=ans, mk=mk, opts=opts)

def item_marks(it, default):
    k = it["kind"]
    if k == "or": return item_marks(it["a"], default)
    if k in ("ext", "pas"): return sum(s["mk"] for s in it["subs"])
    return int(it.get("mk") or default)

EXTRA_CSS = """<style>
.ps{border:1px solid var(--line);border-left:3px solid var(--gold);background:#fcfcfe;padding:3px 8px;margin:2px 0 3px;font-size:calc(var(--fs) - .5pt);text-align:justify}
.ps p{margin:0 0 3px}
.ps .h{font-weight:700;color:var(--navy);text-align:center;margin-bottom:2px}
.ps table{border-collapse:collapse;margin:2px auto;font-size:calc(var(--fs) - 1pt)}
.ps td,.ps th{border:1px solid var(--line);padding:1px 7px;text-align:center}
.ps th{background:var(--navy);color:#fff}
.sq{display:grid;grid-template-columns:30px 1fr 18px;column-gap:3px;margin:1px 0}
.sq .l{color:var(--navy);font-weight:700}
.sq .m{color:var(--gold);font-weight:700;text-align:right;font-size:8.2pt}
.sq .o{display:grid;grid-template-columns:repeat(2,1fr);column-gap:8px}
.sq .o b{color:var(--navy);margin-right:3px}
.sq .o.c4{grid-template-columns:repeat(4,1fr)}
.qn2{font-weight:700;color:var(--navy)}
.sw{border-top:1px dashed var(--line);margin:3px 0 1px;padding-top:2px;font-size:8.2pt}
</style>"""

ROM = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv"]

def _subs_html(subs):
    h = ""
    for i, s in enumerate(subs):
        o = ""
        if s.get("opts"):
            L = max(len(x) for x in s["opts"])
            cls = "c4" if L <= 12 else ""
            o = f"<div class='o {cls}'>" + "".join(f"<span><b>({l})</b>{x}</span>" for l, x in zip("abcd", s["opts"])) + "</div>"
        h += f"<div class='sq'><div class='l'>({ROM[i]})</div><div>{s['q']}{o}</div><div class='m'>{s['mk']}</div></div>"
    return h

def render_block(n, it, default):
    k = it["kind"]
    if k in ("ext", "pas"):
        tot = item_marks(it, default)
        hd = f"<div class='h'>{it['head']}</div>" if it.get("head") else ""
        body = f"<div style='font-style:italic;font-size:8.4pt;color:#555;margin-bottom:1px'>{it['title']}</div><div class='ps'>{hd}{it['text']}</div>{_subs_html(it['subs'])}"
        return f"<div class='q' style='break-inside:auto'><div class='qn'>{n}.</div><div>{body}</div><div class='mk'>{tot}</div></div>"
    return render_q(n, it, item_marks(it, default))

def render_item(n, it, default):
    if it["kind"] == "or":
        return render_block(n, it["a"], default) + "<div class='orw'>OR</div>" + render_block("", it["b"], default)
    return render_block(n, it, default)

def eng_paper(meta, data, fs=10.1):
    h = head(meta["doc"]).replace("<main>", f"<main style='--fs:{fs}pt;--lh:{1.30+0.03*(fs-9.4):.3f};--qg:{2+(fs-9.4)*3:.1f}px;--sg:{5+(fs-9.4)*4:.1f}px'>") + EXTRA_CSS + BRAND
    h += f"""<div class="ttl"><div class="t">{meta['title']} <span class="setpill">SET {meta['set']}</span></div>
<div class="c">{meta['label']} &nbsp;|&nbsp; RBSE Board Pattern &nbsp;|&nbsp; Session 2026–27</div></div>
<div class="tm"><span>Time: {meta['time']}</span><span class="mid">Name: ____________________ &nbsp; Roll No.: ________</span><span>Maximum Marks: {meta['marks']}</span></div>
<div class="gi"><b>General Instructions:</b><ol>""" + "".join(f"<li>{i}</li>" for i in meta["instr"]) + "</ol></div>"
    n = 1; total = 0
    for key, label, mk, sub in meta["secs"]:
        items = data[key]
        tot = sum(item_marks(i, mk) for i in items); total += tot
        h += f"<div class='sec'><span>{label}</span><span class='pill'>{tot} Marks</span></div><div class='sub'>{sub}</div>"
        for it in items:
            h += render_item(n, it, mk); n += 1
    assert total == meta["marks"], (meta["doc"], total, meta["marks"])
    h += f"<div class='end'><span>END OF QUESTION PAPER</span><span class='pill'>Total: {meta['marks']} Marks</span></div>"
    return h + TAIL

def _ans_html(a):
    return a if isinstance(a, str) else "<br>".join(a)

def _rows(n, it, default, prefix=""):
    k = it["kind"]; out = ""
    if k == "mcq":
        idx = "abcd".index(it["ans"])
        return f"<tr><td class='n'>{n}</td><td>{prefix}<b>({it['ans']})</b> {it['opts'][idx]}" + (f" — <i>{it['why']}</i>" if it.get("why") else "") + f"</td><td class='m'>1</td></tr>"
    if k in ("ext", "pas"):
        rows = ""
        for i, s in enumerate(it["subs"]):
            a = s["ans"]
            if s.get("opts") and len(a) == 1 and a in "abcd":
                a = f"<b>({a})</b> {s['opts']['abcd'.index(a)]}"
            rows += f"<tr><td class='n'>{n if i == 0 else ''}</td><td>{prefix if i == 0 else ''}<b>({ROM[i]})</b> {a}</td><td class='m'>{s['mk']}</td></tr>"
        return rows
    return f"<tr><td class='n'>{n}</td><td>{prefix}{_ans_html(it['ans'])}</td><td class='m'>{item_marks(it, default)}</td></tr>"

def eng_key(meta, data):
    h = head(meta["doc"] + " — Answer Key") + EXTRA_CSS + BRAND
    h += f"""<div class="ttl"><div class="t">ANSWER KEY &amp; MARKING SCHEME <span class="setpill">SET {meta['set']}</span></div>
<div class="c">{meta['label']} &nbsp;|&nbsp; Class 8 English &nbsp;|&nbsp; Maximum Marks: {meta['marks']}</div></div>"""
    n = 1
    for key, label, mk, _ in meta["secs"]:
        items = data[key]
        tot = sum(item_marks(i, mk) for i in items)
        h += f"<div class='sec'><span>{re.sub(r'[(][^)]*[)]', '', label).strip()} — Answers</span><span class='pill'>{tot} Marks</span></div>"
        h += "<table class='ak'><tr><th style='width:26px'>Q.</th><th>Expected Answer / Value Points</th><th style='width:50px;text-align:center'>Marks</th></tr>"
        for it in items:
            if it["kind"] == "or":
                h += _rows(n, it["a"], mk) + _rows("", it["b"], mk, "<span class='orlab'>OR:</span> ")
            else:
                h += _rows(n, it, mk)
            n += 1
        h += "</table>"
    h += "<div class='note'><b>Evaluator's note:</b> Answers given are model answers / value points; accept any other relevant and correct response in the candidate's own words. For writing tasks, marks are for format, content, organisation and accuracy of language. In internal-choice questions, evaluate only the option attempted.</div>"
    return h + TAIL
