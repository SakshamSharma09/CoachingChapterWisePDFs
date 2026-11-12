"""Shared helpers for Class 5 Hindi model papers 1-5 (hindi_p01..p05)."""
import random
from lib5 import *

INSTR = [
    "यह प्रश्न-पत्र सीखने के स्तर (शिक्षण-क्षेत्रों) पर आधारित है।",
    "प्रश्न-पत्र पर अपना नाम और अनुक्रमांक अवश्य लिखिए।",
    "सभी प्रश्न अनिवार्य हैं।",
    "प्रश्नों के सामने उनके अंक दिए गए हैं।",
    "उत्तर साफ़-सुथरे और सुन्दर अक्षरों में लिखिए।",
]
T1 = "पढ़ना, पढ़कर समझना और समझकर लिखना (गद्य)"
T2 = "पद्य"
T3 = "व्यावहारिक व्याकरण"
T4 = "सृजनात्मक अभिव्यक्ति"
T5 = "परिवेशीय सजगता"


def meta(n):
    return dict(subject="Hindi", set_no=n, time="2.30 घण्टे", marks=80, instr=INSTR)


def mc(q, opts, idx, passage=None):
    """MCQ; opts = 4 option strings, idx = index (0-3) of the correct one."""
    assert len(opts) == 4
    return Q(q, 1, "(%s) %s" % ("abcd"[idx], opts[idx]), opts=opts, passage=passage)


def mt(pairs_left, pairs_right):
    """match-the-following table: left numbered 1.., right lettered (क)(ख)(ग).."""
    letters = ["क", "ख", "ग", "घ"]
    rows = "".join("<tr><td>%d. %s</td><td>(%s) %s</td></tr>" % (i + 1, l, letters[i], r)
                   for i, (l, r) in enumerate(zip(pairs_left, pairs_right)))
    return "<table class='t5'>%s</table>" % rows


def grid(words, seed0=1, size=5):
    """word-search of aksharas. words = list of (list_of_aksharas, clue). Returns (table_html, locations list)."""
    pool = ["क", "ग", "च", "ज", "द", "न", "प", "म", "य", "व", "स", "ह", "त", "ब", "ल", "का", "की", "ने", "ती", "से", "ला"]
    for seed in range(seed0, seed0 + 2000):
        rnd = random.Random(seed)
        g = [[None] * size for _ in range(size)]
        locs = []
        ok = True
        for ws, _ in words:
            placed = False
            for _t in range(200):
                d = rnd.choice("HV")
                r = rnd.randrange(size - (len(ws) - 1 if d == "V" else 0))
                c = rnd.randrange(size - (len(ws) - 1 if d == "H" else 0))
                cells = [(r + (i if d == "V" else 0), c + (i if d == "H" else 0)) for i in range(len(ws))]
                if all(g[a][b] is None for a, b in cells):
                    for (a, b), ch in zip(cells, ws):
                        g[a][b] = ch
                    locs.append((d, r + 1, c + 1))
                    placed = True
                    break
            if not placed:
                ok = False
                break
        if not ok:
            continue
        for a in range(size):
            for b in range(size):
                if g[a][b] is None:
                    g[a][b] = rnd.choice(pool)
        # each answer must be found exactly once in rows (->) and columns (down)
        def count(ws):
            n = 0
            L = len(ws)
            for a in range(size):
                for b in range(size - L + 1):
                    if g[a][b:b + L] == ws:
                        n += 1
            for b in range(size):
                col = [g[a][b] for a in range(size)]
                for a in range(size - L + 1):
                    if col[a:a + L] == ws:
                        n += 1
            return n
        if all(count(ws) == 1 for ws, _ in words):
            t = "<table class='t5' style='margin-left:26px;font-size:1.15em'>" + "".join(
                "<tr>" + "".join("<td style='padding:3px 10px'>%s</td>" % x for x in row) + "</tr>" for row in g) + "</table>"
            return t, locs
    raise RuntimeError("grid failed")


def q18(words, seed0=1):
    t, locs = grid(words, seed0)
    parts = []
    for i, ((ws, clue), (d, r, c)) in enumerate(zip(words, locs)):
        w = "".join(ws)
        where = ("पंक्ति %d में बाएँ से दाएँ (&rarr;)" % r) if d == "H" else ("स्तंभ %d में ऊपर से नीचे (&darr;)" % c)
        parts.append(P("(%s)" % ["i", "ii", "iii", "iv", "v", "vi"][i], clue, 1, "<b>%s</b> (%s)" % (w, where)))
    return Q("नीचे दिए अक्षर-जाल में छह शब्द छिपे हैं। इन्हें बाएँ से दाएँ (&rarr;) या ऊपर से नीचे (&darr;) पढ़ा जा सकता है। संकेत पढ़कर सही शब्द खोजिए और लिखिए :", 6, "", parts=parts, fig=t)
