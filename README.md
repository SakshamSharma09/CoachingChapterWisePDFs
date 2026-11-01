# Coaching Chapterwise PDFs — Mastermind Coaching Classes, Jaipur

Original practice papers, revision notes and answer keys for Classes 5–10, generated from the NCERT books
(Class 9/10 papers follow RBSE/CBSE patterns). Every paper has a separate answer key. All questions are original.

## Folder layout
```
Class_NN/<Subject>/
    Practice_Papers/               chapter tests (40 m), two-chapter tests, unit tests, full-syllabus papers (+ answer keys, 00_Index.pdf)
    Part2_Papers/                  Part 2 book only (Class 8 SST, Class 9 SST & Maths)
    FullYear_Part1+2_Papers/       80-mark papers covering Part 1 + Part 2
    School_Pattern_Papers/         5 sets per subject in the Delhi DoE/CBSE school-paper pattern (Classes 8-10)
    School_Pattern_FullYear_Part1+2/   same pattern, whole-year (Class 8 SST; Class 9 SST & Maths)
    Revision_Notes/                descriptive revision notes (Science, SST, Maths where done)
    Reading_Writing/               English reading + writing papers (Classes 5-10)
English_Grammar_Workbooks/         Part 1 (Classes 5-8), Part 2 (Classes 9-10)
docs/                              pattern analysis and blueprint
src/                               generator source (Python): question banks, composers, notes renderer
```

## Status (as of 2026-11-01)
| Class | Maths | Science | Social Science | English | Hindi |
|---|---|---|---|---|---|
| 5 | – | – | – | Reading/Writing | – |
| 6 | Papers | Papers + Notes | Papers + Notes | Reading/Writing | – |
| 7 | Papers | Papers + Notes | Papers + Notes | Reading/Writing | – |
| 8 | Papers, School-pattern, Notes (Book 2) | Papers, School-pattern, Notes | Papers, Part 2, Full year, School-pattern, Notes | School-pattern, Reading/Writing | School-pattern |
| 9 | Papers, Part 2 (ch 9-14), Full year, School-pattern, Notes (Part 2) | Papers, School-pattern, Notes | Papers, Part 2 (ch 9-14), Full year, School-pattern, Notes | Papers, Reading/Writing | Papers |
| 10 | Papers, School-pattern | Papers, School-pattern | Papers, School-pattern | Papers, School-pattern, Reading/Writing | Papers, School-pattern |

## Known gaps / to do
- Class 9 Science Part 2 book not yet received; Class 9 Maths Part 2 may have more chapters than 9-14.
- Maths revision notes: only Class 8 Book 2 and Class 9 Part 2 done; Classes 6-7 Maths and Class 8-9 Maths Book 1 pending.
- Class 6-7 and Class 9 English/Hindi not rebuilt in the school pattern.
- Class 10 revision notes not generated.
- India outline map in the school-pattern papers is approximate.

## Regenerating
Question banks live in `src/c9build/content9`, `sst9`, `sci9` (and `c8build/sst8`, etc.). Papers are composed with
`compose9.py` (HTML → PDF via Playwright/Chromium). Revision notes use `src/rnlib/notes.py`; school-pattern papers use `src/pat/lib_pat.py`.
