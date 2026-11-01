"""Hindi (Class 10, RBSE) collection builder."""
import os, sys, copy, random, re, importlib
from collections import Counter
from playwright.sync_api import sync_playwright
import compose as M
from lib import to_pdf
from hin_lib import hin_paper, hin_key, OR, Q, item_marks
import hin.gram as GR

M.FIXED = re.compile(M.FIXED.pattern + "|उपर्युक्त|इनमें से|दोनों|सभी|कोई नहीं", re.I)
ROOT = "/home/claude/papers/Hindi_Class10_Paper_Generated"
H = [f"h{i:02d}" for i in range(1, 16)]
KP = H[0:6]; KR = H[6:9]; PO = H[9:15]; PROSE = KP + KR
MOD = {n: importlib.import_module(f"hin.{n}") for n in H}
slug = lambda s: re.sub(r"[^\w]+", "_", s, flags=re.U).strip("_")
def load(names):
    out = {}
    for n in names: out.update(importlib.import_module(f"hin.{n}").SETS)
    return out
READ = load(["reading_a", "reading_b", "reading_c"]); WRIT = load(["writing_a", "writing_b"]); GRAM = GR.SETS
assert len(READ) == len(WRIT) == len(GRAM) == 10

def shuf_sub(s, rng):
    s = copy.deepcopy(s)
    if s.get("opts") and not any(M.FIXED.search(o) for o in s["opts"]):
        c = s["opts"]["abcd".index(s["ans"])]; rng.shuffle(s["opts"]); s["ans"] = "abcd"[s["opts"].index(c)]
    return s
def shuffle_data(data, seed):
    rng = random.Random(seed); out = {}
    for k, items in data.items():
        new = []
        for it in items:
            if it["kind"] == "mcq": new.append(M.shuffle_mcq(it, rng))
            elif it["kind"] == "pas":
                it = copy.deepcopy(it); it["subs"] = [shuf_sub(s, rng) for s in it["subs"]]; new.append(it)
            else: new.append(it)
        out[k] = new
    return out

USE = Counter()
def nxt(name, kind):
    pool = getattr(MOD[name], kind); r = copy.deepcopy(pool[USE[(name, kind)] % len(pool)]); USE[(name, kind)] += 1; return r
def rot(lst, n, off): return [lst[(off + j) % len(lst)] for j in range(n)]
def auth(name):
    m = MOD[name]; au = m.SRC.split("—")[-1].strip()
    return Q(f"<b>{au}</b> का जीवन-परिचय देते हुए उनकी प्रमुख रचनाओं का उल्लेख कीजिए।", m.AUTH, "3")

def run(pg, meta, data, outdir, base, foot, target, fmin=9.4):
    path = f"{outdir}/{base}.pdf"
    n, fs = M.fit(pg, lambda f: hin_paper(meta, data, f), path, foot, target, fmin=fmin)
    kf = f"{outdir}/_k{meta['set']}.pdf"
    to_pdf(pg, hin_key(meta, data), kf, "उत्तर-कुंजी · " + foot.split("·", 1)[-1].strip())
    return n, fs, kf

S_A = ("A", "खण्ड — अ (वस्तुनिष्ठ प्रश्न)", 1, "सही विकल्प चुनकर उत्तर-पुस्तिका में लिखिए।")
S_B = ("B", "खण्ड — ब (अति लघूत्तरात्मक प्रश्न)", 2, "लगभग 25–30 शब्दों में उत्तर दीजिए।")
S_C = ("C", "खण्ड — स (लघूत्तरात्मक प्रश्न)", 3, "लगभग 60 शब्दों में उत्तर दीजिए।")
S_D = ("D", "खण्ड — द (दीर्घ उत्तरीय प्रश्न)", 4, "लगभग 100 शब्दों में उत्तर दीजिए।")
def instr(parts, choice=None):
    b = ["सभी प्रश्न अनिवार्य हैं।"] + parts
    if choice: b.append(choice)
    return b + ["प्रश्न का क्रमांक उत्तर के साथ अवश्य लिखिए।", "उत्तर-पुस्तिका में उत्तर प्रश्नों के क्रम में ही लिखिए।"]

def main(levels):
    os.makedirs(ROOT, exist_ok=True); log = []
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page()
        if "1" in levels:
            for gdir, names, gname in [("1_क्षितिज_गद्य", KP, "क्षितिज (गद्य)"), ("2_कृतिका", KR, "कृतिका"), ("3_क्षितिज_काव्य", PO, "क्षितिज (काव्य)")]:
                for i, nm in enumerate(names, 1):
                    m = MOD[nm]; poem = nm in PO
                    sl = f"{i:02d}_{slug(m.NAME)}"; d = f"{ROOT}/1_Chapter_Tests/{gdir}/{sl}"; os.makedirs(d, exist_ok=True); keys = []
                    for s, S_ in enumerate("AB"):
                        if poem:
                            data = dict(A=m.MCQ[5*s:5*s+5], B=[m.VSA[s]], C=[m.VYA[s]]); marks = 10; tm = "25 मिनट"
                            secs = [S_A, S_B, S_C]; ins = instr(["प्र. 1–5 वस्तुनिष्ठ (प्रत्येक 1 अंक)।", "प्र. 6 अति लघूत्तरात्मक (2 अंक)।", "प्र. 7 व्याख्या/लघूत्तरात्मक (3 अंक)।"])
                        else:
                            data = dict(A=m.MCQ[6*s:6*s+6], B=m.VSA[2*s:2*s+2], C=[m.VYA[s], m.SA[s]], D=[m.LA[s]]); marks = 20; tm = "45 मिनट"
                            secs = [S_A, S_B, S_C, S_D]; ins = instr(["प्र. 1–6 वस्तुनिष्ठ (प्रत्येक 1 अंक)।", "प्र. 7–8 अति लघूत्तरात्मक (प्रत्येक 2 अंक)।", "प्र. 9–10 लघूत्तरात्मक (प्रत्येक 3 अंक)।", "प्र. 11 दीर्घ उत्तरीय (4 अंक)।"])
                        data = shuffle_data(data, f"hch{nm}{S_}")
                        meta = dict(doc=f"{sl} Set {S_}", title=f"कक्षा 10 हिन्दी — {gname} अध्याय-परीक्षण", set=S_, time=tm, marks=marks, secs=secs, instr=ins, label=f"पाठ {i} : <b>{m.NAME}</b>")
                        n, fs, kf = run(pg, meta, data, d, f"{sl}_Set_{S_}", f"Mastermind Coaching Classes — कक्षा 10 हिन्दी · {m.NAME} · सेट {S_}", 1 if poem else 2)
                        log.append((f"{sl}_{S_}", n, fs)); keys.append(kf)
                    M.unite(keys, f"{d}/{sl}_Answer_Key.pdf")
        if "2" in levels:
            units = [(KP, "Unit_1_Kshitij_Gadya_Lessons_1_to_6", "क्षितिज (गद्य)", "क्षितिज (गद्य) — सभी 6 पाठ", False),
                     (KR, "Unit_2_Kritika_Lessons_1_to_3", "कृतिका", "कृतिका — सभी 3 पाठ", False),
                     (PO, "Unit_3_Kshitij_Kavya_All_Poems", "क्षितिज (काव्य)", "क्षितिज (काव्य) — सभी काव्य-पाठ", True)]
            for ui, (names, sl, ttl, lbl, poem) in enumerate(units):
                d = f"{ROOT}/2_Unit_Tests_30_Marks/{sl}"; os.makedirs(d, exist_ok=True); keys = []; n_ = len(names)
                for k, S_ in enumerate("ABC"):
                    A_ = [nxt(names[(j + 2 * k) % n_], "MCQ") for j in range(8)]
                    B_ = [nxt(names[(k + 2 * j + 1) % n_], "VSA") for j in range(4)]
                    C_ = [nxt(names[(k + 1) % n_], "VYA"), nxt(names[(k + 3) % n_], "SA" if not poem else "VYA")]
                    D_ = [OR(nxt(names[(k + 2) % n_], "LA"), nxt(names[(k + 4) % n_], "LA")), OR(nxt(names[(k + 5) % n_], "LA"), nxt(names[(k + 6) % n_], "LA"))]
                    data = shuffle_data(dict(A=A_, B=B_, C=C_, D=D_), f"hunit{ui}{S_}")
                    ins = instr(["प्र. 1–8 वस्तुनिष्ठ (प्रत्येक 1 अंक)।", "प्र. 9–12 अति लघूत्तरात्मक (प्रत्येक 2 अंक)।", "प्र. 13–14 लघूत्तरात्मक (प्रत्येक 3 अंक)।", "प्र. 15–16 दीर्घ उत्तरीय (प्रत्येक 4 अंक)।"], "प्र. 15 एवं 16 में आंतरिक विकल्प हैं।")
                    meta = dict(doc=f"{sl} Set {S_}", title=f"कक्षा 10 हिन्दी — {ttl} इकाई-परीक्षण", set=S_, time="1 घण्टा 15 मिनट", marks=30, secs=[S_A, S_B, S_C, S_D], instr=ins, label=f"<b>{lbl}</b>")
                    n, fs, kf = run(pg, meta, data, d, f"{sl}_Set_{S_}", f"Mastermind Coaching Classes — कक्षा 10 हिन्दी · {lbl} · सेट {S_}", 2)
                    log.append((f"{sl}_{S_}", n, fs)); keys.append(kf)
                M.unite(keys, f"{d}/{sl}_Answer_Key.pdf")
        if "3" in levels:
            d = f"{ROOT}/3_Skill_Papers"; 
            for sub in ("Reading_Papers_12_Marks", "Writing_and_CaseStudy_Papers_24_Marks", "Grammar_Papers_10_Marks"): os.makedirs(f"{d}/{sub}/Answer_Keys", exist_ok=True)
            for i in range(1, 11):
                s = f"{i:02d}"
                def one_(sub, title, label, secs, ins, data, marks, time, tgt, fname):
                    meta = dict(doc=f"Hindi {fname} Set {s}", title=title, set=s, time=time, marks=marks, secs=secs, instr=ins, label=label)
                    pth = f"{d}/{sub}/{fname}_Set_{s}.pdf"
                    ft = f"Mastermind Coaching Classes — कक्षा 10 हिन्दी · {label.replace('<b>','').replace('</b>','')} · सेट {s}"
                    n, fs = M.fit(pg, lambda f: hin_paper(meta, data, f), pth, ft, tgt)
                    to_pdf(pg, hin_key(meta, data), f"{d}/{sub}/Answer_Keys/{fname}_Set_{s}_Answer_Key.pdf", "उत्तर-कुंजी · " + ft.split("·", 1)[-1].strip())
                    log.append((f"{fname}_{s}", n, fs))
                one_("Reading_Papers_12_Marks", "कक्षा 10 हिन्दी — अपठित बोध (पठन-कौशल) परीक्षण", "<b>अपठित गद्यांश एवं पद्यांश</b>",
                     [("R", "खण्ड — स (अपठित गद्यांश व पद्यांश)", 3, "अपठित गद्यांश/पद्यांश पढ़कर प्रश्नों के उत्तर दीजिए।")], instr(["प्र. 1–2 अपठित गद्यांश (प्रत्येक 3 अंक, 3 उप-प्रश्न 1-1 अंक के)।", "प्र. 3–4 अपठित पद्यांश (प्रत्येक 3 अंक)।"]),
                     dict(R=READ[i]["R"]), 12, "30 मिनट", 2, "Hindi_Reading_Paper")
                W = WRIT[i]
                one_("Writing_and_CaseStudy_Papers_24_Marks", "कक्षा 10 हिन्दी — लेखन-कौशल एवं प्रकरण-अध्ययन परीक्षण", "<b>लेखन-कौशल एवं प्रकरण-अध्ययन</b>",
                     [("W", "खण्ड — द (लेखन-कौशल एवं प्रकरण-अध्ययन)", 4, "सभी प्रश्न अनिवार्य हैं; आंतरिक विकल्प दिए गए हैं।")],
                     instr(["प्र. 1 प्रकरण-अध्ययन (4 अंक), प्र. 2 सारांश/भाव-पल्लवन (4 अंक), प्र. 3 पत्र-लेखन (4 अंक), प्र. 4 निबंध (6 अंक), प्र. 5 प्रकरण-अध्ययन (6 अंक)।"], "प्र. 1, 2, 3 एवं 5 में आंतरिक विकल्प हैं; प्र. 4 में तीन विषयों में से एक चुनें।"),
                     dict(W=W["W"]), 24, "1 घण्टा 15 मिनट", 3, "Hindi_Writing_CaseStudy_Paper")
                G = copy.deepcopy(GRAM[i]); G = shuffle_data(dict(G=G["G"]), f"hgram{i}")["G"] + GRAM[i]["M"]
                one_("Grammar_Papers_10_Marks", "कक्षा 10 हिन्दी — व्याकरण परीक्षण", "<b>व्याकरण</b>",
                     [("G", "खण्ड — अ (व्याकरण)", 1, "सही विकल्प चुनिए / प्रश्न का उत्तर दीजिए।")], instr(["प्र. 1–8 वस्तुनिष्ठ (प्रत्येक 1 अंक)।", "प्र. 9 मुहावरा (2 अंक)।"]),
                     dict(G=G), 10, "25 मिनट", 1, "Hindi_Grammar_Paper")
        if "4" in levels:
            d = f"{ROOT}/4_Full_Syllabus_Papers_80_Marks"; kd = f"{d}/Answer_Keys"; os.makedirs(kd, exist_ok=True)
            for i in range(1, 11):
                s = f"{i:02d}"; W = WRIT[(i + 3) % 10 + 1]
                lm = [nxt(n, "MCQ") for n in rot(PROSE, 5, i)] + [nxt(n, "MCQ") for n in rot(PO, 3, i)]
                gm = [GR.item(c, i + c) for c in (0, 3)]
                gf = [GR.fill(c, i + c + 2) for c in (1, 2, 4, 5, 6, 7)]
                vs = [nxt(n, "VSA") for n in rot(PROSE, 3, i + 1)] + [nxt(n, "VSA") for n in rot(PO, 2, i + 2)] + [GR.muh(i - 1)]
                reading = READ[i]["R"]
                va = [OR(nxt(rot(PROSE, 1, i)[0], "VYA"), nxt(rot(PROSE, 1, i + 4)[0], "VYA")), OR(nxt(rot(PO, 1, i)[0], "VYA"), nxt(rot(PO, 1, i + 3)[0], "VYA")),
                      OR(auth(rot(PROSE, 1, i + 2)[0]), auth(rot(PO, 1, i + 1)[0])), nxt(rot(PROSE, 1, i + 6)[0], "SA")]
                la = [OR(nxt(rot(PROSE, 1, i + 3)[0], "LA"), nxt(rot(PO, 1, i + 2)[0], "LA"))]
                data = shuffle_data(dict(A=lm + gm + gf, B=vs, C=reading + va, D=la + W["W"]), f"hfull{i}")
                secs = [("A", "खण्ड — अ (वस्तुनिष्ठ प्रश्न : 16 अंक)", 1, "सही विकल्प चुनिए / रिक्त स्थान की पूर्ति कीजिए।"),
                        ("B", "खण्ड — ब (अति लघूत्तरात्मक प्रश्न : 12 अंक)", 2, "लगभग 25–30 शब्दों में उत्तर दीजिए।"),
                        ("C", "खण्ड — स (अपठित, व्याख्या एवं लघूत्तरात्मक : 24 अंक)", 3, "निर्देशानुसार उत्तर दीजिए।"),
                        ("D", "खण्ड — द (दीर्घ उत्तरीय एवं लेखन-कौशल : 28 अंक)", 4, "निर्देशानुसार उत्तर दीजिए।")]
                ins = ["सभी प्रश्न अनिवार्य हैं।", "खण्ड अ : प्र. 1–10 बहुविकल्पीय, प्र. 11–16 रिक्त स्थान (प्रत्येक 1 अंक) — कुल 16 अंक।", "खण्ड ब : प्र. 17–22 (प्रत्येक 2 अंक) — कुल 12 अंक; प्र. 22 मुहावरे पर आधारित है।",
                       "खण्ड स : प्र. 23–26 अपठित गद्यांश/पद्यांश (प्रत्येक 3 अंक); प्र. 27–30 (प्रत्येक 3 अंक) — कुल 24 अंक।", "खण्ड द : प्र. 31–34 (प्रत्येक 4 अंक), प्र. 35 निबंध (6 अंक), प्र. 36 प्रकरण-अध्ययन (6 अंक) — कुल 28 अंक।",
                       "आंतरिक विकल्प : प्र. 27, 28, 29, 31, 32, 33, 34 एवं 36 में।", "प्रश्न का क्रमांक उत्तर के साथ अवश्य लिखिए।"]
                meta = dict(doc=f"Hindi Full Syllabus Set {s}", title="कक्षा 10 — हिन्दी पूर्ण पाठ्यक्रम प्रश्न-पत्र", set=s, time="3 घण्टा 15 मिनट", marks=80, secs=secs, instr=ins,
                            label="<b>क्षितिज · कृतिका · अपठित · व्याकरण · रचना</b>")
                ft = f"Mastermind Coaching Classes — कक्षा 10 हिन्दी · पूर्ण पाठ्यक्रम प्रश्न-पत्र · सेट {s}"
                n, fs = M.fit(pg, lambda f: hin_paper(meta, data, f), f"{d}/Hindi_Full_Syllabus_Set_{s}.pdf", ft, 5, fmin=9.8)
                to_pdf(pg, hin_key(meta, data), f"{kd}/Hindi_Full_Syllabus_Set_{s}_Answer_Key.pdf", f"उत्तर-कुंजी · हिन्दी पूर्ण पाठ्यक्रम · सेट {s}")
                log.append((f"Hindi_Full_{s}", n, fs))
        br.close()
    for l in log: print(*l)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1234")
