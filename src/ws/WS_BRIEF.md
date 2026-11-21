# Chapter worksheets (~50 graded questions) + detailed chapter notes — brief for authoring agents

Repo: D:\Coaching Chapterwise PDFs (Windows; run from any directory with `python`; Playwright/pypdf/pymupdf are installed; Chromium is found automatically).
Why this exists: the existing graded chapter papers are mostly parametric drills (for example Class 9 Maths "Linear Polynomials" has no word problems at all). The owner wants, for EVERY class / subject / chapter, a NEW kind of content:
1. a **chapter worksheet of about 50 questions** with marks and an Easy / Medium / Hard indicator on every question (plus an answer key), full of application, word, reasoning and case questions;
2. **detailed chapter-wise notes** (one PDF per chapter, much fuller than the existing multi-chapter revision notes).
Read first: `src/ws/libws.py` (docstring + `W()`), then the bank module of your chapter in `src/graded/<bank>.py` (scope, NAME, what the drills already cover — do NOT copy bank questions), then existing notes source for the chapter if any (`src/rn_work/<set>/cNN.py`, a dict `CH` — use as a starting point and EXPAND; folders: c6_maths c6_sci c6_sst c7_maths c7_sci c7_sst c8_maths1 c8_maths2 c8_sci c8_sst2 c9_maths1 c9_maths2 c9_sci_a c9_sci_b c9_sst c9_sst2 c10_maths c10_science c10_sst). NCERT chapter PDFs are in `NCERT_Books/Class_NN/<Subject>/...` (read with pymupdf when you need to verify scope/facts).

## One file per chapter: `src/ws/<bank>_ws.py`  (e.g. `c9m_ch02_ws.py`)
```python
"""Class 9 Maths Ch 2 ..."""
from libws import *          # W, run
BANK = "c9m_ch02"
WS = [ W(q, marks, ans, "E"|"M"|"H", opts=None, fig=None, wp=False), ... ]
CH = dict(num=2, title="...", tag="Maths", intro="...", big_questions=[...], blocks=[...], takeaways=[...])
if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
```
Run `python src/ws/c9m_ch02_ws.py` -> writes `Class_09/Maths/Worksheets/Ch02_<slug>_Worksheet.pdf`, `..._Worksheet_Answer_Key.pdf` and `Class_09/Maths/Chapter_Notes/Ch02_<slug>_Chapter_Notes.pdf`. Subject strings: Maths, Science, Social_Science, English, Hindi. `run` validates and raises with a clear message — fix and rerun (a transient `OSError Errno 22` just means rerun).

## Worksheet rules (WS)
- 50-52 questions: Easy 16-18, Medium 18-20, Hard 12-14 (each level at least 10). Marks: Easy 1-2 (the MCQs are Easy, 1 mark, 5-8 of them with `opts`), Medium 2-3, Hard 3-5. Put questions in ascending difficulty inside each level.
- These are NEW question types for the chapter: real-life word/application problems (Indian names, money, travel, school, sports, farming, Rajasthan contexts), multi-step reasoning, error analysis ("find the mistake"), true/false with reason, match/complete, data/table-based, case-study and HOTS questions, 'explain why', puzzles. `wp=True` flags word/application problems; the validator requires at least 12 for Maths, 8 for Science (use more), none required for SST/English/Hindi (but include source-based, map-based, timeline, 'why/how' and case items for SST; comprehension, vocabulary, grammar-in-context, extract-based and writing items for English/Hindi).
- Everything inside the chapter's CURRENT assessed syllabus (see AGENT_BRIEF.md exclusions: e.g. Class 10 Maths no Euclid's lemma/algorithm, polynomial division algorithm, constructions, ogives, frustum, area of triangle by coordinates, cross-multiplication; Class 10 Science no Periodic Classification, Sources of Energy, Sustainable Management; Class 10 SST nothing deleted).
- Maths: compute answers in code or verify twice; clean numbers; KaTeX `$...$` allowed in questions and answers (Hindi: Devanagari). Answers must show the working with marks in brackets e.g. `(1)`. No question may need drawing space; questions on graphs must give the table/figure (SVG helpers: `svg_*` in `src/c5/lib5.py` can be imported with `sys.path.insert(0,'src/c5')` if useful).
- MCQs: one correct option, three hand-written plausible distractors; answer string starts with `(a)`/`(b)`...
- No answer lines are printed (owner requirement: no wasted space).

## Detailed notes rules (CH)
Content model = `src/rnlib/notes.py` docstring (blocks: h2, h3, p, ul, ol, table, note (NOTE|IMPORTANT|FORMULA|DEFINITION|REMEMBER), steps, qa). **No `$`/LaTeX in notes**: write maths with Unicode (x², √2, ½, π, ≤, →, ×, ÷, Greek) and `<sup>`/`<sub>`; `**bold**` and `*italic*`. Requirements (validator): >= 6 `h2` sections, >= 1400 words, >= 6 takeaways. Expected: 4-8 pages. Include, as fits the subject:
- Maths: definitions, every formula/identity with a FORMULA note, proofs/derivations where the syllabus has them, 5-8 fully worked examples (use `steps` blocks titled "Example n — ..."), tables of cases/types, common mistakes (REMEMBER notes), a "Word problems: how to translate" section where relevant, 6-8 likely exam questions (qa).
- Science: concepts with explanations, definitions, laws/equations with units, activities and what they show, diagrams described in words (labelled parts in a table), differences tables, numerical examples (steps), common misconceptions, likely questions.
- Social Science: background, causes-events-effects, timeline table, key people/places/terms table, map pointers (what to locate), sources/case notes, comparison tables, likely 3/5-mark answers (qa).
- English/Hindi (lesson/poem): summary in the right order, characters/speakers, theme and values, literary devices with examples, key vocabulary with meanings, extract explanations, grammar points of the lesson, likely questions with model answers. (Hindi in correct Devanagari.)
Keep all facts accurate and in the current NCERT / reader text; if unsure of a fact leave it out.

## Quality gate
Spot-check ~10 answers per chapter; read your question list for ambiguity, wrong answers, off-syllabus items, duplicates and lazy distractors. After the first chapter, view one worksheet page and one notes page as images (pymupdf -> PNG) and fix layout problems (very long answers in the key are fine). Do NOT git commit/push/checkout/reset/stash; write only your own `src/ws/<bank>_ws.py` files and the PDFs they produce. Final report <= 8 lines: chapters done (with question counts / note pages), any doubts.
