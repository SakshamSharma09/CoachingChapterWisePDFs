"""Build, from the typed sample-paper data (src/sp10/data/<Subject>_<Paper>.json):
  1. Class_10/<Subject>/SamplePaper_Chapterwise_Worksheets/ChNN_<slug>_SP_Worksheet.pdf (+ _Answer_Key.pdf)
     every DISTINCT question of the chapter from all 11 sample papers (CBSE official + 10).
  2. Class_10/<Subject>/SamplePaper_Sectionwise_Tests/<Group>_Test_NN.pdf (+ _Answer_Key.pdf), 80 marks each.
Usage: python build.py <Subject> [ws|tests|both] [--only ChNN]      Subject: Maths Science SST English Hindi
"""
import sys, os, re, json, glob, html as H, difflib, random, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "src" / "graded")); sys.path.insert(0, str(HERE))
import common                                      # noqa
from common import lib, to_pdf                     # noqa
from chapters import CH

WORK = Path(r"C:\Users\Saksham\AppData\Local\Temp\claude\0da2d72d58043887\fc748be4-719d-4cc6-9a85-08dc202f3924\scratchpad\sp10work")
FOLDER = {"Maths": "Maths", "Science": "Science", "SST": "Social_Science", "English": "English", "Hindi": "Hindi"}
TITLE = {"Maths": "MATHEMATICS", "Science": "SCIENCE", "SST": "SOCIAL SCIENCE", "English": "ENGLISH", "Hindi": "HINDI"}
PAPERS = ["CBSE_Official"] + ["Paper_%02d" % i for i in range(1, 11)]
PTAG = {p: ("CBSE" if p == "CBSE_Official" else "SP" + p[-2:]) for p in PAPERS}
PTAG["Generated"] = "Gen"; PTAG["Mock"] = "Mock"
PAPERS_ALL = PAPERS + ["Generated"]

CSS = """
.q{display:grid;grid-template-columns:28px 1fr 46px;column-gap:4px;margin:5px 0;}
.q .no{font-weight:700;color:#13286b}.q .mk{text-align:right;font-weight:700;color:#c49a3c;font-size:8.8pt;white-space:nowrap}
.src{display:block;font-size:7pt;color:#777;margin-top:1px}
.o5{display:grid;grid-template-columns:repeat(4,1fr);column-gap:8px;margin-top:2px}.o5.c2{grid-template-columns:repeat(2,1fr)}.o5.c1{grid-template-columns:1fr}
.o5 span b{color:#13286b;margin-right:3px}
.sp{margin:3px 0 0 6px}.sp .l{display:grid;grid-template-columns:26px 1fr 34px;margin:2px 0}
.fg{margin:3px 0;text-align:left}.fg img{max-width:62%;max-height:70mm;border:1px solid #ddd;margin-right:6px;vertical-align:top}
.fg.sm img{max-height:34mm}
.stat{display:flex;justify-content:space-between;border:1px solid #13286b;background:#f2f5fb;padding:3px 9px;font-weight:700;color:#13286b;font-size:9pt;margin:5px 0}
.hi{font-family:'Nirmala UI','Noto Sans Devanagari','Mangal',Arimo,sans-serif}
.pass{white-space:pre-line}
table.mt{border-collapse:collapse;margin:3px 0;font-size:9pt}table.mt td,table.mt th{border:1px solid #999;padding:1px 6px}
.ans{margin:2px 0 6px 28px;padding:3px 7px;border-left:3px solid #c49a3c;background:#fdf8ec;font-size:9.4pt}
.nt{color:#b3261e;font-size:8.4pt;margin-top:2px}
.sec{display:flex;justify-content:space-between;background:#13286b;color:#fff;padding:3px 9px;font-weight:700;font-size:9.6pt;margin:9px 0 3px}
.sec .pill{color:#ffd966}
.ttl{border:1.5px solid #13286b;padding:5px 10px;margin:6px 0;background:#f7f9fd}.ttl .t{font-weight:700;font-size:12pt;color:#13286b}.ttl .c{font-size:9.4pt}
.end{display:flex;justify-content:space-between;border-top:1.5px solid #13286b;margin-top:8px;padding-top:3px;font-weight:700;color:#13286b;font-size:9pt}
"""
TAIL = r"""</main><script>
document.addEventListener('DOMContentLoaded',function(){renderMathInElement(document.body,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:false});
document.fonts.ready.then(function(){window.__done=true;});});
</script></body></html>"""

# ------------------------------------------------------------------ data
def norm(s):
    return re.sub(r"[^0-9a-z\u0900-\u097f]+", "", (s or "").lower())

def figs(it, paper, sub):
    """figure files (absolute) for a question dict"""
    names = []
    for k in ("figure", "figure2", "figure_extra"):
        if it.get(k): names.append(it[k])
    for k in ("figures", "option_figures"):
        v = it.get(k)
        if isinstance(v, list): names += [x for x in v if isinstance(x, str)]
    out = []
    for n in names:
        p = WORK / sub / paper / n
        if p.exists() and str(p) not in out: out.append(str(p))
    return out

def mk_item(q, paper, sub, alt=False):
    paper = q.get("paper") or paper
    sps = []
    for sp in q.get("subparts") or []:
        d = dict(text=sp.get("text") or "", marks=sp.get("marks") or 0, options=sp.get("options"), answer=sp.get("answer"),
                 figs=figs(sp, paper, sub), chapter=sp.get("chapter"))
        if sp.get("or"):
            o = sp["or"]; d["or"] = dict(text=o.get("text") or "", options=o.get("options"), answer=o.get("answer"), figs=figs(o, paper, sub))
        sps.append(d)
    chap = q.get("chapter")
    if chap == "OTHER":
        m = re.search(r"SKILL_\w+", q.get("note") or "")
        if m: chap = m.group(0)
    return dict(sub=sub, paper=paper, no=q["no"], alt=alt, section=q.get("section"), marks=q.get("marks") or 0, type=q.get("type"),
                chapter=chap, text=q.get("text") or "", options=q.get("options"), figs=(figs(q, paper, sub) or ([str(WORK / "SST" / "Paper_05" / "fig_p03_0.png")] if (sub == "SST" and q.get("type") == "map" and paper in ("Generated", "Mock")) else [])),
                afigs=[str(WORK / sub / paper / q["answer_figure"])] if q.get("answer_figure") and (WORK / sub / paper / q["answer_figure"]).exists() else [],
                answer=q.get("answer"), subparts=sps, note=q.get("note"), srcs=[(paper, q["no"], alt)], origin=q.get("origin"), basis=q.get("basis"))

def load(sub):
    items = []
    for p in PAPERS:
        f = HERE / "data" / f"{sub}_{p}.json"
        if not f.exists(): print("missing", f.name); continue
        for q in json.load(open(f, encoding="utf-8"))["questions"]:
            items += split_lit(mk_item(q, p, sub))
            o = q.get("or")
            if o:
                oo = dict(q); oo.update({k: o.get(k) for k in ("text", "options", "figure", "answer", "subparts", "note", "chapter") if k in o})
                oo["chapter"] = o.get("chapter") or q["chapter"]
                oo["figure"] = o.get("figure"); oo["subparts"] = o.get("subparts"); oo["answer"] = o.get("answer")
                items += split_lit(mk_item(oo, p, sub, alt=True))
    for f in sorted((HERE / "data").glob(f"Gen_{sub}_*.json")):
        for i, q in enumerate(json.load(open(f, encoding="utf-8"))["questions"], 1):
            q = dict(q); q["no"] = q.get("no") or i
            items += split_lit(mk_item(q, "Generated", sub))
    return items

def split_lit(it):
    """literature question whose sub-questions come from different lessons -> one item per sub-question"""
    if it["sub"] not in ("English", "Hindi") or it["type"] != "literature" or not it["subparts"]: return [it]
    chs = {sp["chapter"] or it["chapter"] for sp in it["subparts"]}
    if len(chs) < 2: return [it]
    stem = it["text"].strip().split(chr(10))[0]
    stem = stem if len(stem) < 150 else ""
    out = []
    for sp in it["subparts"]:
        n = dict(it); n["stem"] = stem; n["chapter"] = sp["chapter"] or it["chapter"]
        n["text"] = sp["text"]; n["options"] = sp["options"]; n["marks"] = sp["marks"]; n["figs"] = sp["figs"]; n["answer"] = sp["answer"]; n["subparts"] = []
        n["afigs"] = []; n["note"] = None; n["srcs"] = list(it["srcs"])
        if sp.get("or"):
            n["text"] += chr(10) + "OR" + chr(10) + sp["or"]["text"]; n["answer"] = (sp["answer"] or "") + chr(10) + "OR: " + (sp["or"].get("answer") or "")
        out.append(n)
    return out

def sig(it):
    return norm(it["text"] + " " + " ".join(it["options"] or []) + " " + " ".join(s["text"] for s in it["subparts"]))

def dedupe(items):
    """keep first occurrence (official paper first); merge sources of near-duplicates within the same chapter"""
    kept = []; by = collections.defaultdict(list)
    for it in items:
        s = sig(it)[:1500]; hit = None
        if len(s) < 8: kept.append(it); by[it["chapter"]].append((s, it)); continue
        for s2, k in by[it["chapter"]]:
            if s2 == s or difflib.SequenceMatcher(None, s, s2, autojunk=False).ratio() >= (0.985 if it["srcs"][0][0] == "Generated" or k["srcs"][0][0] == "Generated" else 0.9):
                hit = k; break
        if hit: hit["srcs"] += it["srcs"]
        else: kept.append(it); by[it["chapter"]].append((s, it))
    return kept

# ------------------------------------------------------------------ rendering
def rich(t):
    """question / answer text -> html (keeps $...$ for KaTeX); markdown tables and newlines handled"""
    if not t: return ""
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S).replace("**", "")
    lines = t.split("\n"); out = []; i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            hdr = [c.strip() for c in lines[i].strip().strip("|").split("|")]; i += 2; rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            out.append("<table class='mt'><tr>" + "".join(f"<th>{H.escape(c)}</th>" for c in hdr) + "</tr>" +
                       "".join("<tr>" + "".join(f"<td>{H.escape(c)}</td>" for c in r) + "</tr>" for r in rows) + "</table>")
            continue
        out.append(lines[i]); i += 1
    # escape everything except our tags: do escaping on non-table, non-<b> parts
    res = []
    for seg in out:
        if seg.startswith("<table"): res.append(seg); continue
        e = H.escape(seg, quote=False).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")
        res.append(e)
    html = "<br>".join(r if r.startswith("<table") else r for r in res)
    return re.sub(r"<br>(<table)", r"\1", html)

_OPT = re.compile(r"^\(?(?:[A-Da-d]|[क-घ])[.)]\s*(?=\S)")
def _so(o):
    return _OPT.sub("", o, count=1)

def opts_html(opts):
    if not opts: return ""
    L = max(len(re.sub(r"\$[^$]*\$", "xxxxxx", o)) for o in opts)
    cls = "" if L <= 16 else (" c2" if L <= 44 else " c1")
    return f"<div class='o5{cls}'>" + "".join(f"<span><b>({l})</b>{rich(_so(o))}</span>" for l, o in zip("abcd", opts)) + "</div>"

def figs_html(fs, small=False):
    if not fs: return ""
    return f"<div class='fg{' sm' if small else ''}'>" + "".join(f"<img src='{Path(f).as_uri()}'>" for f in fs) + "</div>"

def src_tag(it, with_ch=False):
    if it.get("srctxt"):
        return f"<span class='src'>{it['srctxt']}" + (f" · {it['chapter']}" if with_ch else "") + "</span>"
    if it["srcs"] and it["srcs"][0][0] == "Generated":
        o = {"ncert": "NCERT-style", "variant": "changed-values version", "related": "related question"}.get(it.get("origin"), "generated")
        return f"<span class='src'>Generated ({o}" + (f"; based on {it['basis']}" if it.get("basis") else "") + ")" + (f" · {it['chapter']}" if with_ch else "") + "</span>"
    s = ", ".join(sorted({f"{PTAG[p]} Q{n}{'(OR)' if a else ''}" for p, n, a in it["srcs"]}, key=lambda x: (x[:4] != "CBSE", x)))
    return f"<span class='src'>Source: {s}" + (f" · {it['chapter']}" if with_ch else "") + "</span>"

def body_html(it, key=False, chtag=False):
    pre = f"<div style='font-size:8.6pt;color:#555'><i>{rich(it['stem'])}</i></div>" if it.get('stem') else ''
    h = f"<div class='pass'>{rich(it['text'])}</div>" if it["type"] in ("reading", "case") and len(it["text"]) > 220 else rich(it["text"])
    h = pre + h
    h += figs_html(it["figs"])
    if it["options"]: h += opts_html(it["options"])
    if it["subparts"]:
        h += "<div class='sp'>"
        for k, sp in enumerate(it["subparts"], 1):
            lab = "(" + ("i ii iii iv v vi vii viii ix x xi xii xiii xiv xv xvi".split() + [str(x) for x in range(17, 40)])[k - 1] + ")"
            h += f"<div class='l'><span>{lab}</span><div>{rich(sp['text'])}{figs_html(sp['figs'], True)}{opts_html(sp['options'])}"
            if sp.get("or"): h += f"<div><b>OR</b> {rich(sp['or']['text'])}{opts_html(sp['or']['options'])}</div>"
            if key and sp.get("answer"): h += f"<div class='ans' style='margin-left:0'>{rich(sp['answer'])}</div>"
            if key and sp.get("or") and sp["or"].get("answer"): h += f"<div class='ans' style='margin-left:0'><b>OR:</b> {rich(sp['or']['answer'])}</div>"
            h += f"</div><span style='text-align:right;color:#c49a3c;font-weight:700;font-size:8.4pt'>[{sp['marks']}]</span></div>"
        h += "</div>"
    if key:
        if it["answer"]: h += f"<div class='ans'>{rich(it['answer'])}{figs_html(it['afigs'], True)}</div>"
        elif it["afigs"]: h += f"<div class='ans'>{figs_html(it['afigs'], True)}</div>"
        if it.get("note"):
            nt = re.sub(r"SKILL_\w+[;:]?\s*", "", it["note"]).strip()
            if nt: h += f"<div class='nt'>Note: {rich(nt)}</div>"
    return h + ('' if it.get('nosrc') else src_tag(it, chtag))

def page(sub, title, sub_title, stats, qhtml):
    hi = sub == "Hindi"
    h = lib.head(title).replace("<style>", "<style>" + CSS, 1)
    h = h.replace("<main>", "<main class='hi'>" if hi else "<main>", 1) + lib.BRAND
    h += f"<div class='ttl'><div class='t'>{title}</div><div class='c'>{sub_title}</div></div>"
    h += f"<div class='stat'>{''.join(f'<span>{s}</span>' for s in stats)}</div>"
    return h + qhtml + TAIL

def to_pdf_retry(pg, html, out, foot):
    for k in range(4):
        try:
            to_pdf(pg, html, out, foot); return
        except OSError as e:
            print("retry", e)
    raise

def qblock(num, it, key, chtag=False):
    return f"<div class='q'><div class='no'>{num}.</div><div>{body_html(it, key, chtag)}</div><div class='mk'>[{it['marks']}]</div></div>"

GROUP = {"mcq": "A. Multiple choice questions (1 mark)", "ar": "B. Assertion–Reason questions (1 mark)", "vsa": "C. Very short answer questions (2 marks)",
         "sa": "D. Short answer questions (3 marks)", "la": "E. Long answer questions (5 marks)", "case": "F. Case / source-based questions (4 marks)",
         "map": "G. Map-based questions", "reading": "Reading comprehension", "grammar": "Grammar", "writing": "Writing", "literature": "Literature",
         "other": "Other"}
ORDER = list(GROUP)

def chapter_title(ch):
    m = re.match(r"(?:Ch(\d+)_|SKILL_)(.*)", ch)
    return (int(m.group(1)) if m.group(1) else 0, m.group(2).replace("_", " ")) if m else (0, ch)

# ------------------------------------------------------------------ worksheets
def build_worksheets(sub, items, pg, only=None):
    out = REPO / "Class_10" / FOLDER[sub] / "SamplePaper_Chapterwise_Worksheets"; out.mkdir(parents=True, exist_ok=True)
    bych = collections.defaultdict(list)
    for it in items: bych[it["chapter"]].append(it)
    report = []
    for ch in sorted(bych):
        if only and only not in ch: continue
        its = sorted(bych[ch], key=lambda x: (ORDER.index(x["type"]) if x["type"] in ORDER else 99, x["marks"]))
        raw = len(its); its = dedupe(its)
        no, name = chapter_title(ch)
        tot = sum(i["marks"] for i in its)
        stem = f"{ch}_SP_Worksheet"
        for key in (False, True):
            qh = ""; n = 0; last = None
            for it in its:
                g = it["type"] if it["type"] in GROUP else "other"
                if g != last:
                    cnt = [x for x in its if (x["type"] if x["type"] in GROUP else "other") == g]
                    qh += f"<div class='sec'><span>{GROUP[g]}</span><span class='pill'>{len(cnt)} questions · {sum(x['marks'] for x in cnt)} marks</span></div>"; last = g
                n += 1; qh += qblock(n, it, key)
            qh += f"<div class='end'><span>{'END OF ANSWER KEY' if key else 'END OF WORKSHEET'}</span><span>Total: {tot} marks</span></div>"
            ttl = f"CLASS 10 — {TITLE[sub]} · {'CH ' + str(no) + ' ' if no else ''}{name.upper()} · {'ANSWER KEY' if key else 'SAMPLE-PAPER QUESTION WORKSHEET'}"
            html = page(sub, ttl, f"All distinct questions on this chapter from the 11 sample papers of 2026–27 (CBSE official + 10) &nbsp;|&nbsp; Source tags: CBSE = official paper, SPnn = sample paper nn",
                        [f"Questions: {len(its)}", f"Total marks: {tot}", f"Found in sample papers: {raw} (duplicates merged)"], qh)
            to_pdf_retry(pg, html, out / (stem + ("_Answer_Key" if key else "") + ".pdf"), f"Mastermind Coaching Classes — Class 10 {sub} · {name} · Sample-paper worksheet")
        report.append((ch, raw, len(its), tot)); print(ch, raw, "->", len(its), "questions", tot, "marks", flush=True)
    return report

# ------------------------------------------------------------------ tests
def group_of(sub, it):
    t, m, ch = it["type"], it["marks"], it["chapter"]
    no, _ = chapter_title(ch)
    if sub == "Maths":
        return {1: "SecA_1mark_MCQ_and_AR", 2: "SecB_2mark", 3: "SecC_3mark", 5: "SecD_5mark", 4: "SecE_Case_Based_4mark"}.get(m, None) if not (t == "case" and m != 4) else "SecE_Case_Based_4mark"
    if sub == "Science":
        if t == "case": return "Case_Based"
        return "SecA_Biology" if ch in CH["Science"][4:8] + CH["Science"][12:13] else "SecB_Chemistry" if ch in CH["Science"][:4] else "SecC_Physics"
    if sub == "SST":
        if no == 0: return None
        return "SecA_History" if no <= 5 else "SecB_Geography" if no <= 12 else "SecC_Political_Science" if no <= 17 else "SecD_Economics"
    if sub == "English":
        return {"reading": "SecA_Reading", "writing": "SecB_Writing", "grammar": "SecC_Grammar", "literature": "SecD_Literature"}.get(t)
    if sub == "Hindi":
        return {"reading": "SecA_Reading_Apathit", "grammar": "SecB_Grammar_Vyakaran", "literature": "SecC_Textbook", "writing": "SecD_Writing"}.get(t)

def make_tests(sub, items, total=80):
    groups = collections.defaultdict(list)
    for it in items:
        g = group_of(sub, it)
        if g: groups[g].append(it)
    tests = {}
    rnd = random.Random(2026)
    for g, pool in sorted(groups.items()):
        pool = dedupe(sorted(pool, key=lambda x: (PAPERS_ALL.index(x["paper"]), x["no"])))
        # also drop duplicates across chapters
        seen = []; uniq = []
        for it in pool:
            s = sig(it)[:800]
            gen = it["srcs"][0][0] == "Generated"
            if any(difflib.SequenceMatcher(None, s, s2, autojunk=False).ratio() >= (0.985 if (gen or g2) else 0.9) for s2, g2 in seen): continue
            seen.append((s, gen)); uniq.append(it)
        pool = uniq
        bych = collections.defaultdict(list)
        for it in pool: bych[it["chapter"]].append(it)
        for l in bych.values(): rnd.shuffle(l)
        used = []; tno = 0
        while True:
            chs = sorted(bych); order = []
            for k in range(max([len(l) for l in bych.values()] or [0])):
                for ch in chs:
                    if k < len(bych[ch]): order.append(bych[ch][k])
            reach = {0: []}
            for it in order:
                for v in sorted(list(reach), reverse=True):
                    nv = v + it["marks"]
                    if nv <= total and nv not in reach: reach[nv] = reach[v] + [it]
            chosen = None; s = 0
            if total in reach: chosen = reach[total]; s = total
            else:
                cand = [it for it in items if group_of(sub, it) != g and not any(id(it) == id(u) for u in used)]
                for best in sorted(reach, reverse=True):
                    rest = total - best
                    if rest > 40: break
                    r2 = {0: []}
                    for it in cand:
                        for v in sorted(list(r2), reverse=True):
                            nv = v + it["marks"]
                            if nv <= rest and nv not in r2 and len(r2[v]) < 8: r2[nv] = r2[v] + [it]
                    if rest in r2:
                        chosen = reach[best] + r2[rest]; used += r2[rest]; s = total; break
            if chosen is None: break
            for it in chosen:
                if it in bych[it["chapter"]]: bych[it["chapter"]].remove(it)
            tno += 1
            chosen.sort(key=lambda x: (chapter_title(x["chapter"])[0], x["no"]))
            tests[(g, tno)] = chosen
        if tno == 0:
            print("pool too small for an 80-mark test:", g, sum(i["marks"] for i in pool))
    return tests

def build_tests(sub, items, pg):
    out = REPO / "Class_10" / FOLDER[sub] / "SamplePaper_Sectionwise_Tests"; out.mkdir(parents=True, exist_ok=True)
    tests = make_tests(sub, items)
    for (g, n), its in sorted(tests.items()):
        for key in (False, True):
            qh = ""; tot = sum(i["marks"] for i in its)
            for k, it in enumerate(its, 1): qh += qblock(k, it, key, chtag=key)
            qh += f"<div class='end'><span>{'END OF ANSWER KEY' if key else 'END OF TEST'}</span><span>Total: {tot} marks</span></div>"
            gname = re.sub(r"^Sec([A-E])_", "Section " + chr(92) + "1 — ", g).replace("_", " ")
            instr = "<div class='ttl'><div class='c'><b>Time allowed:</b> 3 hours &nbsp; <b>Maximum marks:</b> 80. All questions are compulsory; read each question carefully; marks are shown at the right.</div></div>" if not key else ""
            html = page(sub, f"CLASS 10 — {TITLE[sub]} · {gname.upper()} TEST {n} · {'ANSWER KEY' if key else '80 MARKS'}",
                        "Section-wise test built from distinct questions of the 2026–27 sample papers &nbsp;|&nbsp; Source tags: CBSE = official paper, SPnn = sample paper nn",
                        [f"Questions: {len(its)}", f"Total marks: {tot}", "Time: 3 hours"], instr + qh)
            to_pdf_retry(pg, html, out / f"{g}_Test_{n:02d}{'_Answer_Key' if key else ''}.pdf", f"Mastermind Coaching Classes — Class 10 {sub} · {gname} test {n}")
        print("test", g, n, len(its), "questions", flush=True)

# ------------------------------------------------------------------ mock papers
SEC_NAME = {"Maths": {"A": "Section A — Multiple choice and assertion–reason (1 mark each)", "B": "Section B — Very short answer (2 marks each)", "C": "Section C — Short answer (3 marks each)", "D": "Section D — Long answer (5 marks each)", "E": "Section E — Case-based questions (4 marks each)"}}
ORIGIN = {"real": "real sample-paper question", "variant": "changed-values version", "ncert": "NCERT-style question"}

def mock_item(q, sub, n, key=True):
    it = mk_item(q, "Mock", sub); it["nosrc"] = not key
    o = q.get("origin"); b = q.get("basis")
    txt = {"real": f"Real sample question ({b})", "variant": f"Variant of {b}", "ncert": "NCERT-style question (original)"}.get(o, "")
    it["srctxt"] = f"Mock paper source: {txt}"
    return it

def build_mocks(sub, pg):
    out = REPO / "Class_10" / FOLDER[sub] / "Mock_Papers_2026-27"; out.mkdir(parents=True, exist_ok=True)
    for f in sorted((HERE / "data").glob(f"Mock_{sub}_*.json")):
        j = json.load(open(f, encoding="utf-8")); n = int(f.stem[-2:])
        if any(q.get("text") is None and not q.get("subparts") for q in j["questions"]): print("incomplete", f.name); continue
        qs = j["questions"]; tot = sum(q["marks"] for q in qs)
        for key in (False, True):
            qh = ""; last = None
            for q in qs:
                it = mock_item(q, sub, n, key); sec = q.get("section")
                if sec != last:
                    cnt = [x for x in qs if x.get("section") == sec]
                    qh += f"<div class='sec'><span>Section {sec}</span><span class='pill'>{len(cnt)} questions · {sum(x['marks'] for x in cnt)} marks</span></div>"; last = sec
                it_or = None
                if q.get("or"):
                    oo = dict(q); o = q["or"]
                    oo.update({k: o.get(k) for k in ("text", "options", "figure", "answer", "subparts", "note") if k in o}); oo["or"] = None
                    it_or = mock_item(oo, sub, n, key)
                body = body_html(it, key, key)
                if it_or: body += "<div style='text-align:center;font-weight:700;margin:4px 0'>OR</div>" + body_html(it_or, key, key)
                qh += f"<div class='q'><div class='no'>{q['no']}.</div><div>{body}</div><div class='mk'>[{q['marks']}]</div></div>"
            qh += f"<div class='end'><span>{'END OF ANSWER KEY' if key else 'END OF PAPER'}</span><span>Total: {tot} marks</span></div>"
            instr = "" if key else ("<div class='ttl'><div class='c'><b>Time allowed:</b> 3 hours &nbsp; <b>Maximum marks:</b> 80. All questions are compulsory; internal choice is given in some questions. Marks are shown at the right of each question.</div></div>")
            html = page(sub, f"CLASS 10 — {TITLE[sub]} · MOCK PAPER {n} (2026–27 PATTERN) · {'ANSWER KEY' if key else '80 MARKS'}",
                        "Pattern follows the 2026–27 CBSE sample paper; about 35% real sample questions, 40% changed-value versions, 25% NCERT-style questions" if not key else "Each key line names the source of the question (real sample paper / changed-values version / NCERT-style)",
                        [f"Questions: {len(qs)}", f"Total marks: {tot}", "Time: 3 hours"], instr + qh)
            to_pdf_retry(pg, html, out / f"Mock_Paper_{n:02d}{'_Answer_Key' if key else ''}.pdf", f"Mastermind Coaching Classes — Class 10 {sub} · Mock paper {n}")
        print("mock", sub, n, tot, flush=True)

if __name__ == "__main__":
    sub = sys.argv[1]; what = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "both"
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    from playwright.sync_api import sync_playwright
    items = load(sub)
    print(sub, "items", len(items), flush=True)
    import glob as _g
    _c = sorted(_g.glob(os.path.expanduser("~/AppData/Local/ms-playwright/chromium-*/chrome-win*/chrome.exe")))
    with sync_playwright() as p:
        br = p.chromium.launch(**({'executable_path': os.environ.get('CHROMIUM_PATH') or _c[-1]} if (os.environ.get('CHROMIUM_PATH') or _c) else {})); pg = br.new_page()
        if what in ("ws", "both"): build_worksheets(sub, items, pg, only)
        if what in ("tests", "both"): build_tests(sub, items, pg)
        if what in ("mock",): build_mocks(sub, pg)
        br.close()
