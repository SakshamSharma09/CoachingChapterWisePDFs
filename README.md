# Coaching Chapterwise PDFs — Mastermind Coaching Classes, Jaipur

Original practice papers, worksheets, notes and answer keys for Classes 5–10 (NCERT based; Class 9/10 follow RBSE/CBSE patterns). Every paper has a separate answer key. All questions are original. About 9,700 PDFs, all generated from Python sources in `src/`.

**Full architecture (what contains what, and how it is built): [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).**

## Layout
```
Class_NN/<Subject>/
    Graded_Papers/        NCERT-Type / Easy / Medium / Hard x 3 sets + key per chapter; Unit_Tests, Full_Year, MCQ_Tests
    Worksheets/           ~50-question worksheet per chapter (Easy/Medium/Hard + marks) and its answer key
    Chapter_Notes/        detailed notes, one PDF per chapter
    Formula_Sheets/       one-page formula sheets (Maths, Science)
    Practice_Papers/      chapter, two-chapter, unit and full-syllabus papers (+ keys, 00_Index.pdf)
    Part2_Papers/ FullYear_Part1+2_Papers/    second-book and whole-year papers (Class 8 SST; Class 9 SST, Maths)
    School_Pattern_Papers/ School_Pattern_FullYear_Part1+2/    real-school-pattern papers
    Revision_Notes/       older multi-chapter revision notes
    Reading_Writing/      English reading and writing papers
    Model_Papers/         Class 5 only: 10 per subject (unsolved, answer key, solved)
Class_10/<Subject>/Sample_Papers_2026-27/ SamplePaper_Chapterwise_Worksheets/ SamplePaper_Sectionwise_Tests/ Mock_Papers_2026-27/   Class 10 2026-27 sample papers, chapter-wise question worksheets, 80-mark section tests, 5 mock papers per subject (see docs/ARCHITECTURE.md sections 9 and 9b)
Class_08/English_Gulmohar/      Gulmohar reader (17 units; NCERT-Type + Hard; unit tests)
Class_08/English_Ruskin_Bond/   Ruskin Bond-linked reader (chapters 11-12 so far)
NCERT_Books/                    NCERT chapter PDFs, Classes 6-10 (ChNN_Title.pdf)
English_Grammar_Workbooks/      Part 1 (Classes 5-8), Part 2 (Classes 9-10)
docs/                           ARCHITECTURE, STATUS, PROJECT_MEMORY, blueprints, review_logs/
src/                            generator source (Python)
```

## What exists (as of 2026-11)
| Class | Maths | Science | Social Science | English | Hindi |
|---|---|---|---|---|---|
| 5 | Model papers | – | – (EVS model papers) | Model papers, Reading/Writing | Model papers |
| 6–7 | Graded, worksheets, notes, formula sheets, practice, school-pattern | same | same | Reading/Writing | – |
| 8 | all products | all products | all products incl. Part 2 | school-pattern, Reading/Writing, Gulmohar, Ruskin reader | school-pattern |
| 9 | all products incl. Part 2 | all products | all products incl. Part 2 | graded, worksheets, notes, practice | graded, worksheets, notes, practice |
| 10 | all products + 2026-27 sample-paper set | all products + sample-paper set | all products + sample-paper set | all products + sample-paper set | all products + sample-paper set |

Class 10 also has, per subject, the 11 original 2026-27 sample papers (CBSE official + 10), chapter-wise worksheets of every distinct sample-paper question (with answer keys) and 80-mark section-wise tests, and 5 mock papers per subject with answer keys (35% real sample questions, 40% changed-values versions, 25% NCERT-style; generated questions are labelled). See docs/ARCHITECTURE.md sections 9 and 9b.

Worksheets, answer keys and chapter notes exist for all 257 chapters in Classes 6–10 (Maths 60, Science 62, SST 77, English 36, Hindi 22).

## Known gaps / for a teacher to check
See section 8 of docs/ARCHITECTURE.md and the logs in `docs/review_logs/`. Main items: Class 10 Hindi and English-poem facts rely on reviewer knowledge (source PDFs garbled or absent); older Class 9 English graded papers vs NCERT "Kaveri"; unit/full-year/MCQ exams not rebuilt after later bank edits; Gulmohar units 1–8 and 13–17 unchecked against the printed book; Class 6–8 English/Hindi graded papers and Class 5 graded papers not built.

## Regenerating
- One chapter worksheet + key + notes: `python src/ws/<bank>_ws.py`
- Graded chapter papers: `src/graded/run_graded.py`; unit / full-year / MCQ: `src/graded/run_exams.py`
- Older families: see `docs/ARCHITECTURE.md` section 5 and `docs/PROJECT_MEMORY.md`.
Requirements: Windows, Python 3.11, Playwright with Chromium.
