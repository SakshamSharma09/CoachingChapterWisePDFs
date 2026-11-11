# Extras brief — Hard-tier assertion-reason + case-based items, formula sheets, "mistakes to avoid" boxes

Repo: D:\Coaching Chapterwise PDFs (Windows; run commands with PowerShell/Git Bash from `src/graded`; `python` is on PATH with playwright/pypdf/pymupdf installed; Chromium is auto-found).
Read first: `src/graded/AGENT_BRIEF.md` (esp. the *Assessed-syllabus rule* and *Quality gate*), `src/graded/common.py` (AR4, make_sets, mistakes_box), and the finished example `src/graded/x/c10m_ch01_x.py`.

## What to write — ONE new file per chapter: `src/graded/x/<module>_x.py`
`<module>` is the chapter-bank module name (e.g. `c9s_ch04` -> `x/c9s_ch04_x.py`). Do NOT edit the chapter bank itself, `common.py`, `exam.py`, `run_graded.py`, or any other agent's files. Contents:

```python
from common import AR4, Q          # AR4(assertion, reason, key, why) ; Q(question_html, answer_html, "1+1+1+2")
AR = [AR4("...", "...", "a|b|c|d", "why")] * 6   # exactly 6 items, hand-written
CASE = [Q("<b>Case study.</b> passage ... (i) ... (ii) ... (iii) ... (iv) ...", "(i) ... (1). (ii) ... (1). (iii) ... (1). (iv) ... (2).", "1+1+1+2")] * 3   # exactly 3 items
FORMULAS = [("Heading", ["line with $KaTeX$", ...]), ...]    # Maths and Science ONLY; must fit ONE A4 page (about 25-35 lines in 4-6 headings)
MISTAKES = ["5 to 6 short bullets: the typical student errors in this chapter (KaTeX/<b>/<i> allowed)"]
```
Subject scope: **Maths, Science**: AR + CASE + FORMULAS + MISTAKES. **Social Science**: AR + CASE (source-based passage/data/map-description case studies) + MISTAKES (no FORMULAS). **English, Hindi**: MISTAKES only (5-6 bullets of typical errors for that lesson: theme/character confusions, grammar/spelling slips, answer-writing errors); no AR/CASE/FORMULAS.

### AR (assertion–reason) rules
- `key`: 'a' both true and R explains A; 'b' both true, R does not explain A; 'c' A true, R false; 'd' A false, R true. Use a MIX of keys over the 6 items (at least one each of a, b, c, d across the chapter's 6).
- Each assertion and reason must be a clear factual/mathematical statement that is definitely true or false (no opinion), strictly inside the chapter and the CURRENT assessed syllabus.
- Maths: verify numerically in your head or with a quick Python check before writing. `why` states the reasoning briefly.

### CASE rules (CBSE case-based, 5 marks here: four parts, split "1+1+1+2")
- 40–90 word realistic scenario with Indian names/places/objects, then parts (i)–(iv); parts (i)-(iii) are 1 mark each, (iv) is 2 marks and needs reasoning. Part labels must be written inline as "(i) ... (ii) ... (iii) ... (iv) ..." in ONE string (the renderer splits them).
- Answer string gives each part's answer with the marks in brackets, e.g. "(i) ... (1). (ii) ... (1). ...".
- No figures are needed (describe data in words or with `lib.table` if essential). Numbers must be clean and answers computed/verified by you.
- Three cases per chapter must be on different sub-topics.

### MISTAKES/FORMULAS rules
- Specific to THIS chapter (not generic exam advice). Facts must be correct. Formula sheet: definitions/laws/units/identities a student needs for the chapter's assessed content only.

## Check and render (per chapter, before moving on)
```
cd "D:\Coaching Chapterwise PDFs\src\graded"
python -W ignore run_graded.py <module> <class> <Subject>          # prints "extras: {AR:6, CASE:3, ...}" then re-renders ALL 16 PDFs of the chapter (the Hard tier gets AR+case items, every answer key gets the Mistakes box)
python -W ignore formula_sheets.py <class> <Subject>               # Maths/Science only: renders Class_NN/<Subject>/Formula_Sheets/ChNN_<slug>_Formula_Sheet.pdf (must be 1 page; it renders every chapter that has FORMULAS — fine to re-run)
python syllabus_guard.py                                            # 0 hits
```
Subject is one of Maths, Science, Social_Science, English, Hindi. Every paper must stay at 2 pages. Look at one Hard paper page 2 and one Hard answer key last page (pymupdf -> PNG) for your first chapter and fix layout issues. Spot-check every answer you wrote.
DO NOT run git commit/push/checkout/reset/stash. Final report: chapters completed, anything doubtful (<= 12 lines).
