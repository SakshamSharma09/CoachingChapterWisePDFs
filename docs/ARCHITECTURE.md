# Architecture — what contains what, and how it is built

Mastermind Coaching Classes, Jaipur. Repo: github.com/SakshamSharma09/CoachingChapterWisePDFs (public, branch `master`).
About 10,000 PDFs (excluding the git-ignored scratch folders) are generated from about 1,000 small Python files.
Nothing is hand-typed into a PDF: every PDF is produced from a Python source file, so a fix means editing a source file and re-running it.

## 1. The big picture

```
 NCERT chapter PDFs (NCERT_Books/)  ──read by authors/reviewers (scope + facts)
            │
            ▼
 SOURCE (src/)   question banks + notes content, one Python file per chapter
            │   run a generator script
            ▼
 HTML  ──Playwright / Chromium──►  PDF   (A4, header/footer, KaTeX for maths)
            │
            ▼
 OUTPUT (Class_NN/<Subject>/<Product>/…)  committed and pushed to GitHub
```

Rules that hold everywhere: all questions are original (never copied from textbooks); every paper has a separate answer key; no blank answer lines are printed (owner requirement); content stays inside the current assessed syllabus (exclusions in `src/graded/AGENT_BRIEF.md`).

## 2. Top-level folders

| Folder | Contents |
|---|---|
| `Class_05` … `Class_10` | All published output PDFs, per class → subject → product (section 3). |
| `NCERT_Books/` | The owner-supplied NCERT chapter PDFs for Classes 6–10, renamed `ChNN_Title.pdf`, grouped `Class_NN/<Subject>/<Book>/`. Source material and reference; its own README lists them. |
| `English_Grammar_Workbooks/` | Part 1 (Classes 5–8) and Part 2 (Classes 9–10) grammar workbooks. |
| `docs/` | This file, STATUS.md (auto-generated, see note), PROJECT_MEMORY.md (owner rules and hand-over), blueprints, WORKSHEETS_AND_NOTES.md, `review_logs/` (17 reviewer logs listing every fix and every item a teacher should check). |
| `src/` | All generator source (section 5); `src/sp10/` is the Class 10 sample-paper pipeline (section 9). |
| `_incoming/`, `_old_unorganized/` | Git-ignored scratch: raw photo zips (Gulmohar, Ruskin Bond) and pre-organisation copies. Safe to delete locally. |
| `1_organise.ps1`, `2_push_to_github.ps1` | Early helper scripts for organising and pushing. |

## 3. Output products (inside `Class_NN/<Subject>/`)

Subjects: Maths, Science, Social_Science, English, Hindi (Class 5: Maths, English, Hindi, EVS). Class 8 English also has `English_Gulmohar/` and `English_Ruskin_Bond/` (separate readers, own README).

| Folder | What it holds | Where applicable |
|---|---|---|
| `Practice_Papers/` | Original paper family: chapter tests (40 m), two-chapter tests, unit tests (50 m), full-syllabus papers (80 m), each with key, plus `00_Index.pdf`. | Classes 6–10 |
| `Part2_Papers/`, `FullYear_Part1+2_Papers/` | Second-book papers and 80-mark papers over Part 1 + 2. | Class 8 SST; Class 9 SST and Maths |
| `School_Pattern_Papers/`, `School_Pattern_FullYear_Part1+2/` | Papers modelled on real Delhi DoE/CBSE school papers (case, source, assertion-reason, map). | Classes 6–10 (varies, see README) |
| `Graded_Papers/` | Graded system (section 4). Per chapter `ChNN_<slug>/{1_NCERT_Type,2_Easy_Level,3_Medium_Level,4_Hard_Level}/` = 3 sets + 1 answer key per tier; plus `Unit_Tests/`, `Full_Year/`, `MCQ_Tests/` (each with the four tiers). The Hard tier carries assertion-reason and case-based items; every answer key has a "mistakes to avoid" box. Gulmohar/Ruskin folders have only NCERT-Type and Hard tiers. | Classes 6–10 all subjects, plus the two Class 8 readers |
| `Formula_Sheets/` | One-page formula sheets per chapter. | Maths, Science |
| `Worksheets/` | One ~50-question worksheet per chapter (Easy/Medium/Hard tag and marks on every question, many word/application problems) and a separate `_Worksheet_Answer_Key.pdf`. 257 chapters. | Classes 6–10 |
| `Chapter_Notes/` | One detailed notes PDF per chapter (4–9 pages). 257 chapters. | Classes 6–10 |
| `Revision_Notes/` | Older multi-chapter revision-note books. | Science, SST, some Maths |
| `Reading_Writing/` | English reading and writing papers. | Classes 5–10 English |
| `Model_Papers/` | 10 papers per subject in the RSCERT PELLE pattern (80 m, 2.30 h, 22 questions): `Model_Paper_NN.pdf` (unsolved), `_Answer_Key.pdf`, `_Solved.pdf`. 120 PDFs. | Class 5 only |

Approximate PDF counts: Graded 5,750; Practice 1,970; Worksheets 514 (257 sheets + 257 keys); Chapter notes 257; Reading/Writing 246; School-pattern ~200; Part 2 / full-year ~200; Formula sheets 122; Model papers 120; NCERT 254.

## 4. The graded system in detail (`Graded_Papers`)

- **Tiers:** NCERT-Type (textbook-style), Easy, Medium, Hard. Three sets per tier (40 marks; prose 20 / poems 10 for English and Hindi) plus one key.
- **Unit tests** (50 marks; English/Hindi 30) group chapters into units (`UnitK_ChAA-BB`); **full-year papers** are 80 marks; **MCQ tests** are 50 × 1 mark. All exist per tier.
- **Extras** per chapter live in `src/graded/x/<bank>_x.py`: assertion-reason (AR), case-based items (CASE), formulas (FORMULAS), mistakes (MISTAKES). They are injected into Hard-tier sets and keys.
- Class 10 SST/English/Hindi and Class 9 English/Hindi have extra unit definitions (`EXTRA_UNITS` in `run_exams.py`).

## 5. Source tree (`src/`)

| Path | Role |
|---|---|
| `graded/` | **Core of the graded system.** `c<class><m|s|sst|e|h>_chNN.py` = chapter bank (TIERS dict NCERT/Easy/Medium/Hard). `common.py` (layout, AR4, extras loading, fit-to-page), `run_graded.py` (chapter papers), `exam.py` + `run_exams.py` (unit / full-year / MCQ; `--with-full --with-mcq --rebuild-hard --workers`), `formula_sheets.py`, `render_extras.py`, `status.py` (STATUS.md generator), `syllabus_guard.py`, `x/` (258 extras files), briefs: `AGENT_BRIEF.md`, `EXTRAS_BRIEF.md`, `GULMOHAR_BRIEF.md`, `RUSKIN_BOOK_BRIEF.md`. |
| `ws/` | **Worksheets + chapter notes.** `libws.py` (the renderer and validators), `<bank>_ws.py` per chapter (260 files; `WS` list of questions via `W(q, marks, ans, level, opts, fig, wp)`, `CH` notes dict), `WS_BRIEF.md`, `REVIEW_BRIEF.md`. Validators: 48–56 questions, each level ≥ 10, word-problem minimums (Maths 12, Science 8), no duplicates; notes ≥ 6 sections, ≥ 1,400 words, ≥ 6 takeaways, no `$` in notes. Run one file with `python src/ws/c9m_ch02_ws.py`; it writes the worksheet, key and notes PDFs. |
| `rnlib/`, `rn_work/` | Notes renderer (`notes.py`, block types h2/h3/p/ul/ol/table/note/steps/qa) and the older revision-note sources by book. The worksheet notes reuse the renderer. |
| `c5/` | Class 5 model papers: `lib5.py` (layout, marks blueprint per subject, SVG helpers), `<subject>_pNN.py`, `CLASS5_BRIEF.md`. |
| `c6build`, `c7build`, `c8build`, `c9build`, `c9hin`, `c8p2` | Original practice-paper generators and question banks per class (`compose*.py`, `content9/`, `sst9/`, `sci9/`, `en9/`, `hin9/`, `lib.py` KaTeX layout, `chk.py` validator, `index9.py`). |
| `sp10/` | Class 10 sample-paper pipeline: `prep.py`, `BRIEF.md`, `data/<Subject>_<Paper>.json` (55 typed papers), `validate.py`, `chapters.py`, `build.py`. See section 9. |
| `pat/` | School-pattern papers: `lib_pat.py`, `figs.py` (maps/figures), per-class-subject folders, `BLUEPRINT.md`. |
| `rw/` | Reading and writing papers. `gw/` grammar workbooks. `tools/` misc helpers. |

## 6. How to do common tasks

| Task | Command / action |
|---|---|
| Rebuild one worksheet + key + notes | `python src/ws/<bank>_ws.py` |
| Rebuild graded chapter papers | `python src/graded/run_graded.py` (see script for class/subject filters) |
| Rebuild unit/full-year/MCQ exams | `python src/graded/run_exams.py --with-full --with-mcq` (`--rebuild-hard` after extras change) |
| Rebuild formula sheets / extras | `src/graded/formula_sheets.py`, `render_extras.py` |
| Add a chapter to a reader (Gulmohar/Ruskin) | Write `c8gl_chNN.py` / `c8rb_chNN.py` per the brief, run run_graded, then run_exams for units |
| Regenerate STATUS.md | `python src/graded/status.py` |

## 7. Environment and gotchas

- Windows, Python 3.11 (no 3.12-only f-string syntax), Playwright with the existing Chromium (`chromium-1248`; the code finds it automatically, or set `CHROMIUM_PATH`).
- PDF writes sometimes fail with `OSError Errno 22`: rerun.
- Use `&lt;` / `&gt;` for raw `<` `>` in notes text; no `$`/LaTeX in notes (Unicode maths instead).
- Repo is large (about 1.6+ GB): push in batches.

## 8. Quality and known open items

Every worksheet/key/notes set was independently reviewed (about 450 fixes; logs in `docs/review_logs/`). Open items for a teacher: Class 10 Hindi and English-poem content verified from memory (source PDFs garbled or absent); Class 10 English Ch 14 ending; generous Hard tags; older Class 9 English graded papers vs NCERT "Kaveri"; `c10sst_ch07` graded bank still tests IUCN categories; unit/full-year/MCQ exams were not rebuilt after later bank edits; Gulmohar units 1–8 and 13–17 not checked against the printed book; Ruskin reader's real title unknown (only chapters 11–12 so far); old 4-tier Gulmohar unit folders 9–12 can be deleted.

## 9. Class 10 sample-paper products (added 2026-11-24)

Source: the 2026-27 Class 10 sample papers supplied by the owner (zip: 11 papers per subject = the CBSE official paper + 10 further papers, each with solutions). Nothing is invented: questions and official answers were typed into data files and de-duplicated.

| Folder (`Class_10/<Subject>/`) | Contents |
|---|---|
| `Sample_Papers_2026-27/` | The 11 original PDFs, renamed `CBSE_Official_...` and `Paper_01...Paper_10_...` (question paper + marking scheme). |
| `SamplePaper_Chapterwise_Worksheets/` | One worksheet per chapter holding every distinct question on that chapter from all 11 papers (duplicates merged, source tag on each question, e.g. `SP03 Q12`), grouped by question type, with marks, figures/maps copied as images, plus a separate `_Answer_Key.pdf`. English also has `SKILL_Reading / Grammar / Writing` worksheets; Hindi has the same for unseen reading, grammar and writing. |
| `SamplePaper_Sectionwise_Tests/` | 80-mark tests built from one section only: Maths = Sec A (1-mark MCQ/AR), B (2), C (3), D (5), E (4-mark case); Science = Biology / Chemistry / Physics / Case-based; Social Science = History / Geography / Political Science / Economics; English = Reading / Writing / Grammar / Literature; Hindi = Reading / Grammar / Textbook / Writing. Each test has an answer key. Questions are not repeated across tests of a group. |

Pipeline (`src/sp10/`): `prep.py` (copies PDFs, page PNGs, embedded figures with positions) -> agents type each paper into `data/<Subject>_<Paper>.json` following `BRIEF.md` (schema: section, marks, type, chapter, text, options, figure, answer, `or`, subparts) -> `validate.py` -> `build.py <Subject> [ws|tests|both]` (de-duplicates with difflib, renders worksheets and tests with the shared KaTeX layout). `chapters.py` lists the chapter ids. Intermediate page images live outside the repo (scratchpad `sp10work`); figure images used in PDFs are embedded in the PDFs.

Known limits: the official marking schemes contain errors (wrong options, arithmetic slips); the transcribers kept the official answer and added a `Note:` line in the key where they believe it is wrong. Questions that mix chapters are filed under the main chapter (English/Hindi literature questions are split per sub-question when the sub-questions come from different lessons). Tests may mix a few questions from a neighbouring group to reach exactly 80 marks. These papers are third-party/CBSE copyrighted material: keep this folder out of any public repository unless you are sure you may publish it.
