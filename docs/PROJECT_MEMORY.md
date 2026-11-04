# Project Memory — Mastermind Coaching Classes, Jaipur
Practice papers, revision notes and answer keys for Classes 5–10 (NCERT based). Written 2026-11-01 as a hand-over for any future session (Claude Code, claude.ai, or a person).

---
## 1. Standing rules (from the owner)
- **Original content only.** Never copy textbook text/examples verbatim; extracts for English/Hindi are paraphrased originals. Every paper has an **answer key** (step marking for maths).
- Source = the NCERT book PDFs the owner supplies per class (OCR when text is legacy-font/scanned; Hindi needs page images because pdftotext garbles Devanagari).
- **Same method for every class/subject** ("Class 10 method"):
  1. Chapter tests, Sets A–B (40 marks; English/Hindi prose 20, poems 10).
  2. Two-chapter tests, Sets A–D (40 marks).
  3. Unit tests (50 marks, Sets A–C; English/Hindi 30 marks).
  4. Full-syllabus papers, 80 marks, 10 per subject, RBSE blueprint (session 2026–27), each with key.
  5. Skill papers for English (Reading, Writing, Grammar) and Hindi.
  6. `00_Index.pdf` per collection + zips.
- **Revision Notes** (Science, Social Science; later Maths for second books): descriptive yet brief, covering the crux of the whole chapter, fully usable by students, modelled on the supplied Class 8 notes; tables, key terms, FORMULA/DEFINITION boxes, worked examples, Q&A, takeaways.
- **School-pattern papers** (added after the owner found our papers differed from real school papers): modelled on real Delhi DoE/CBSE 2026-27 papers — scenario/competency questions, case/source studies, assertion–reason, figures, map item. Built with `pat/lib_pat.py`.
- **Second books (Part 2 / Book 2):** whenever supplied, build the same full set for them *plus* full-year papers combining Part 1 + Part 2, and revision notes (including Maths, not only SST).
- Flag assumptions in the final message; deliver via zips + index. Use per-class/per-chapter agents, staggered (too many agents at once hit rate limits).
- Avoid broad filesystem scans on the owner's machine; owner's files live in `D:\Coaching Chapterwise PDFs` and GitHub repo `SakshamSharma09/CoachingChapterWisePDFs` (branch `master`).

## 2. Patterns learned from the real school papers
- **Class 9/10 Maths (80 m):** 38 questions — A 20×1 (18 MCQ + 2 A-R), B 5×2, C 6×3, D 4×5, E 3 case studies ×4 (1+1+2).
- **Class 9/10 Science:** 39 questions in three subject sections (Biology/Chemistry/Physics), case studies, A-R.
- **Class 9 SST (80 m):** 37 questions — A 20 MCQ, B 4×2, C 5×3, D 4×5, E 3 source-based ×4, F map 5.
- **Class 10 SST:** 38 questions, four 20-mark sections (History, Geography, Political Science, Economics); map 5.
- **Class 10 English:** Reading 20, Grammar 10, Writing 10, Literature 40. **Class 10 Hindi-A:** sections क/ख/ग/घ, 15 questions.
- **Class 8 (60 m, 2.5 h):** Maths 16 q; Science A Q1 I–XII, B Q2–5×2, C Q6–8×3, D Q9–11×5, E Q12–15 case ×4; SST 15 MCQ + 4×2 + 2×3 + 2×5 + 4 source ×4 + map 5; English Reading 14/Grammar 14/Writing 12/Literature 20; Hindi 11 q.
- Full details: `docs/School_Pattern_BLUEPRINT.md`, `docs/Pattern_Analysis_and_Blueprints.md`.

## 3. What has been delivered (till 2026-11-01)
| Class | Maths | Science | Social Science | English | Hindi |
|---|---|---|---|---|---|
| 5 | – | – | – | Reading & Writing | – |
| 6 | Papers | Papers + Notes (Part 1, 2) | Papers + Notes | Reading & Writing | – |
| 7 | Papers | Papers + Notes | Papers + Notes | Reading & Writing | – |
| 8 | Papers; school-pattern; **Book 2 notes (ch 8–14)** | Papers; school-pattern; notes P1 (supplied) + P2 | Papers (Part 1); **Part 2 papers (ch 8–15)**; **full-year P1+P2 (10 papers)**; school-pattern (5) + **school-pattern full-year (5)**; notes P1 (supplied) + **P2** | school-pattern; Reading & Writing | school-pattern |
| 9 | Papers (ch 1–8); **Part 2 (ch 9–14) papers + notes**; **full-year P1+P2**; school-pattern + **school-pattern full-year (ch 1–14)** | Papers; school-pattern; notes P1 + P2 | Papers (ch 1–8); **Part 2 (ch 9–14)**; **full-year**; school-pattern + **full-year school-pattern**; notes P1 + **P2** | Papers; Reading & Writing (rebuilt) | Papers |
| 10 | Papers; school-pattern | Papers; school-pattern | Papers; school-pattern | Papers; school-pattern; Reading & Writing (rebuilt) | Papers; school-pattern |
Also: **English Grammar Workbooks** v2 — Part 1 (Classes 5–8, 139 p.) and Part 2 (Classes 9–10, advanced topics only, 127 p.; chapters open with "Foundation (revise from Part 1, Chapter N)").

### Chapter maps (our numbering)
- **Class 9 SST:** Part 1 = 1 Problem of Choice, 2 Price Puzzle (Eco); 3 Shaping Earth's Surface, 4 Atmosphere & Climate (Geo); 5 Early Humans & Civilisation, 6 State & Society to 1000 CE (Hist); 7 Democracy, 8 Elections (Polity). **Part 2** = 9 Oceans and Life, 10 Life on Earth (Geo); 11 Resistance and Resilience 1000–1700 (Hist); 12 Governance and Public Policy (Pol); 13 Managing Your Personal Finances, 14 From Ideas to Startups (Eco).
- **Class 9 Maths (Ganita Manjari):** Part 1 = 1 Coordinates, 2 Linear Polynomials, 3 World of Numbers, 4 Algebraic Identities, 5 Circles, 6 Perimeter & Area, 7 Probability, 8 Sequences & Progressions. **Part 2** = 9 Propositions and their Converses, 10 How Quantities Combine (Understanding Data), 11 World of Algorithms, 12 Quadrilaterals, 13 Two Variables One Line, 14 Surface Area and Volume. *(The first set of files the owner labelled "Part 2" was identical to Part 1 — caught by text comparison.)*
- **Class 8 SST:** Part 1 = 1 Natural Resources, 2 Reshaping India's Political Map, 3 Rise of the Marathas, 4 Colonial Era, 5 Universal Franchise, 6 Parliamentary System, 7 Factors of Production. **Part 2** = 8 World Geography, 9 India's Long Road to Independence, 10 Indian Architecture, 11 Role of the Judiciary, 12 Citizenship, 13 Dynamics of Population, 14 India's Urban Landscape, 15 Cultural Currents 13th–17th c.
- **Class 8 Maths Book 2 (Ganita Prakash 2):** 8 Algebra Play, 9 Area, 10 Exploring Geometric Themes, 11 Fractions in Disguise, 12 Proportional Reasoning-2, 13 Tales by Dots and Lines, 14 Baudhāyana-Pythagoras theorem.
- Class 9 Science notes: Part 1 ch 1–7, Part 2 ch 8–13 (Biology ×5, Chemistry ×4, Physics ×4 books).

## 4. Where things are
**Repository layout** (`D:\Coaching Chapterwise PDFs`, also in GitHub when pushed):
```
Class_NN/<Subject>/Practice_Papers | Part2_Papers | FullYear_Part1+2_Papers | School_Pattern_Papers | School_Pattern_FullYear_Part1+2 | Revision_Notes | Reading_Writing
English_Grammar_Workbooks/   docs/   src/   README.md
_old_unorganized/ and _incoming/ (git-ignored; safe to delete after checking)
```
**Source code (`src/`):**
- `c6build, c7build, c8build, c9build` — question banks and composers per class (`content9/chNN.py` Maths ch banks; `sst9/sNN.py`, `sst8/sNN.py`; `sci9`, `en9`), `compose9.py` (generic composer; chapter/pair/unit/full levels; `rot` mode = random spread across Part 1+2), `run_*` scripts, `chk.py` bank validator, `index9.py` index builder, `lib.py` HTML/PDF layout.
- `rnlib/notes.py` + `notes_compact.py` — revision-notes renderer (navy #0f2347 / gold #c9a227). `rn_work/<class_subject>/cNN.py` — chapter notes dicts; `build.py` per set.
- `pat/` — school-pattern engine `lib_pat.py` (`mcq, ar, sa, sub, OR, case, sec, build`), `figs.py` (SVG helpers), `BLUEPRINT.md`, per-class folders (`c9m, c9sst, c10m, c8sst_full15, c9sst_full14, c9m_full12 …`).
- `gw/` grammar workbooks, `rw/` Reading & Writing, `tools/mkrepo.py` (rebuilds this folder tree).

**Chapter-bank format:** lists A (40 MCQ incl. A-R), B (16 two-mark), C (24 three-mark), D (16 five-mark with `split` marks); `SETS, POOL = build(A,B,C,D)`; validate with `python3 chk.py content9.ch13`.
**Pipeline:** Python builds HTML → Playwright Chromium → PDF; `fit()` shrinks font to hit page targets.

## 5. Known gaps / caveats (be honest with the owner)
- **Not built yet:** Class 9 Science Part 2 book (never supplied); Maths Part 2 may have chapters beyond 14; Maths revision notes for Classes 6–7 and Class 8–9 Book 1; Class 10 revision notes; Class 6–7 and Class 9 English/Hindi in the school pattern; Class 8 English/Hindi practice sets; visually-impaired alternative questions for Science.
- India outline map in school-pattern papers is approximate (answers marked within ~150 km); no world-ocean map item.
- SST facts were not web-verified; Part 1 facts in the combined papers come from the banks/general knowledge and were not rechecked against the Part 1 books. Class 10 SST school-pattern Sets 3–5 are plainer.
- Class 8 Maths school-pattern covers chapters 1–7 only. English/Hindi literature extracts are paraphrases.
- Layout of generated PDFs was spot-checked on a few pages only; maths numerics were computed in code by the building agents, but answer keys have not had a full independent check.
- Full-year 80-mark papers (our format) reuse some Part 1 bank questions; Part 2 pack unit test replaced the earlier ch 9–12 unit test.
- Environment note: the cloud container cannot push to the owner's GitHub repo (no credential); pushing is done from the owner's PC with `2_push_to_github.ps1`. `device_bash` on the PC was unavailable (isolated Linux failed to start); file transfer limit is 30 MB/file, 100 MB/call.

## 6. Timeline (condensed)
1. Class 10 collections built for all five subjects (method fixed). 2. Classes 6–9 generated per class with agents; Class 9 delivered as one combined zip. 3. Revision notes regenerated to the descriptive standard (Classes 6–9 Science/SST). 4. Reading & Writing for Classes 5–10 (rebuilt for 9, 10); two grammar workbooks (v2, shortened, Part 2 advanced-only). 5. 25–26 Oct: owner supplied real school papers → school-pattern sets for Classes 8, 9, 10. 6. 26–29 Oct: Part 2 books → Class 9 SST ch 9–14, Class 8 SST ch 8–15, Class 9 Maths ch 9–14, Class 8 Maths Book 2 notes, plus full-year and school-pattern full-year papers. 7. 1 Nov: everything organised into the folder tree above, copied to `D:\Coaching Chapterwise PDFs`; push to GitHub pending.

## 7. Next steps when work resumes
1. Confirm the GitHub push; open the folder in Claude Code so it can read/edit files and run git.
2. Ask for / receive: Class 9 Science Part 2, remaining Maths Part 2 chapters, any other second books.
3. Fill gaps in §5 in priority order: Maths notes (6–7, 8–9 Book 1), Class 10 notes, school-pattern for Classes 6–7 and Class 9 English/Hindi.
4. Run an independent answer-key audit (maths first) and a visual QA of all PDFs.
