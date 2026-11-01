"""Helpers for Hindi graded banks (Class 8/9/10). Devanagari font stack + Hindi section labels; grammar pools."""
import common
from common import M4, Q, grp
import lib

# --- Devanagari font fallback (Arimo has Latin only; Chromium falls back to Nirmala UI / Mangal on Windows) ---
lib.CSS = lib.CSS + """
body,main,.q,.opts,table.ak,.sec,.sub,.gi,.ttl,.note{font-family:Arimo,'Nirmala UI','Mangal','Noto Sans Devanagari',Arial,sans-serif}
"""

common.SECS = [("A", "खंड — A (वस्तुनिष्ठ प्रश्न)", 1, "सही विकल्प चुनकर उत्तर-पुस्तिका में लिखिए।"),
               ("B", "खंड — B (अति लघूत्तरात्मक प्रश्न)", 2, "प्रत्येक का उत्तर लगभग 20–30 शब्दों में दीजिए।"),
               ("C", "खंड — C (लघूत्तरात्मक प्रश्न)", 3, "प्रत्येक का उत्तर लगभग 40–60 शब्दों में दीजिए।"),
               ("D", "खंड — D (दीर्घ उत्तरीय प्रश्न)", 5, "प्रत्येक का उत्तर लगभग 100–150 शब्दों में दीजिए।")]
_BL = {"NCERT": "पाठ्यपुस्तक-शैली के प्रश्न (अभ्यास व पाठ-आधारित)", "Easy": "सरल स्तर: प्रत्यक्ष, स्मरण-आधारित प्रश्न",
       "Medium": "मध्यम स्तर: व्याख्या व भाव-बोध पर आधारित प्रश्न", "Hard": "कठिन स्तर: विश्लेषण, सराहना व उच्च चिंतन के प्रश्न"}
def _instr(tier):
    return ["सभी प्रश्न अनिवार्य हैं।", "प्रश्न 1–10 वस्तुनिष्ठ प्रश्न हैं (प्रत्येक 1 अंक)।",
            "प्रश्न 11–14 अति लघूत्तरात्मक प्रश्न हैं (प्रत्येक 2 अंक)।", "प्रश्न 15–18 लघूत्तरात्मक प्रश्न हैं (प्रत्येक 3 अंक)।",
            "प्रश्न 19–20 दीर्घ उत्तरीय प्रश्न हैं (प्रत्येक 5 अंक)।", "प्रश्न 17 से 20 में आंतरिक विकल्प दिया गया है।",
            "प्रत्येक उत्तर से पहले प्रश्न-संख्या अवश्य लिखिए।", _BL[tier] + "।"]
common.instr = _instr

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))

from hgram import gram_mcq, gram_B, gram_C
def m(q, c, w, why=""): return M4(q, c, w.split("|"), why)
def q2(q, a, s="1+1"): return Q(q, a, s)
def q3(q, a, s="1+1+1"): return Q(q, a, s)
def q5(q, a, s="2+2+1"): return Q(q, a, s)

def build(ch, NC, EA, ME, HA):
    """Each argument: dict(A=[18 MCQ], B=[8], C=[12], D=[12]). Grammar groups are appended automatically."""
    out = {}
    for t, (name, d) in enumerate([("NCERT", NC), ("Easy", EA), ("Medium", ME), ("Hard", HA)]):
        assert len(d["A"]) >= 18 and len(d["B"]) >= 8 and len(d["C"]) >= 12 and len(d["D"]) >= 12, (name, len(d["A"]), len(d["B"]), len(d["C"]), len(d["D"]))
        d = dict(A=d["A"][:18], B=d["B"][:8], C=d["C"][:12], D=d["D"][:12])
        A = [d["A"][:9], d["A"][9:], gram_mcq(t, ch)]
        out[name] = dict(A=A, B=grp(d["B"] + gram_B(t, ch), 4), C=grp(d["C"] + gram_C(t, ch), 6), D=grp(d["D"], 6))
    return out
