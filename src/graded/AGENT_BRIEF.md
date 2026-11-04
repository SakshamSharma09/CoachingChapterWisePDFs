# Graded papers — shared brief for authoring agents

Repo: D:\Coaching Chapterwise PDFs (Mastermind Coaching Classes, Jaipur; NCERT-based practice papers).
Goal: for every chapter of your assigned class/subject produce 4 types — **NCERT-type** (style of NCERT examples/exercises, original wording), **Easy** (direct, single step/recall), **Medium** (multi-step), **Hard** (application, HOTS, word/case problems) — each with **3 sets** of 40-mark papers plus a merged answer key (12 papers + 4 keys per chapter).

## Framework (DONE — do not edit `common.py`, `run_graded.py`, or `src/c8build/lib.py`)
Read first: `src/graded/common.py`, `src/graded/run_graded.py`, and the finished template `src/graded/c8m_ch01.py`.
A chapter module defines `SLUG, NAME, CHNO, TIERS` where `TIERS = {"NCERT":T(A,B,C,D), "Easy":..., "Medium":..., "Hard":...}`:
- `A`: list of topic groups, each a list of MCQs built with `M4(question, correct, [wrong, ...], why)`; >= 30 items in total per tier (they are interleaved, 10 per set).
- `B`: 12 items `Q(q, ans, "1+1")` (2 marks) — 3 topic groups of 4.
- `C`: 18 items (3 marks) — 3 groups of 6.   `D`: 12 items (5 marks) — 2 groups of 6.  (`T()` wraps with `grp(B,4), grp(C,6), grp(D,6)`.)
- Answers carry the working with marking points like "(1)" and a split string ("1+1+1", "2+2+1").
- Maths in KaTeX `$...$`; chemistry via `$\ce{H2O}$`. Figures: `fig=` SVG argument (helpers: `src/c8build/lib.py plot_svg`, `src/pat/figs.py`) or phrase the question so none is needed.
- Question text must be unique within a tier (stem+options); the checker asserts counts/duplicates.

## Rules
1. Original questions only; stay strictly inside the chapter's NCERT syllabus. Existing banks (src/c6build…c9build, content*/sci*/sst*) are for SCOPE only — do not copy from them.
2. Maths: compute answers IN CODE (parametric generators) so keys are right. Other subjects: write answers by hand and double-check facts.
3. Tiers must be genuinely different in difficulty and use disjoint parameters/topics.
4. Write ONLY your own files `src/graded/<prefix>_chNN.py` (and one optional helper module of your own). Never git commit/push (the owner's lead session does that).
5. Sizes: each paper must render in <= 2 pages (the runner prints pages).

## Run (PowerShell)
```
$env:PYTHONPATH="C:\Users\Saksham\AppData\Local\Temp\claude\C--Users-Saksham--claude-spares-spare-MGgmm5\d8405be3-342e-4ac3-9ee2-45b3cefd8089\scratchpad\libs"
cd "D:\Coaching Chapterwise PDFs\src\graded"
python run_graded.py <module> <class> <subject> --check     # validate counts/duplicates
python run_graded.py <module> <class> <subject>             # render PDFs into Class_NN/<Subject>/Graded_Papers/ChNN_<slug>/
```
Folder/slug names: reuse the existing `ChNN_<slug>` names from `Class_NN/<Subject>/Practice_Papers/1_Chapter_Tests_*`.
Check visually: render one paper page + one key page per chapter with `python -W ignore -c "import pymupdf; ..."` to PNG and view it; spot-check ~10 answers per chapter. Fix and re-render. Finish a chapter fully before starting the next; the rendered chapter folders are your deliverable.
Final report (short): chapters completed, PDF counts, weaknesses.

## Assessed-syllabus rule (owner requirement — IMPORTANT)
Only test content that is in the CURRENT assessed syllabus, not merely printed in the NCERT book. Topics that appear in the book but are deleted/not assessed must NOT appear in any question or answer.
Known exclusions (add more as you learn them; if you are unsure whether a topic is assessed, leave it out and mention it in your report):
- Class 10 Maths: Euclid's division lemma/algorithm (and the "form 3q, 3q+1 / 6q+1" proofs built on it); division algorithm for polynomials; the Constructions chapter.
- Class 10 Science: Periodic Classification of Elements, Sources of Energy, Sustainable Management of Natural Resources chapters (already excluded from our chapter lists).
- Old NCERT books under `_old_unorganized/*/Old NCERT Books` are pre-rationalisation: use them for nothing except scope hints.
