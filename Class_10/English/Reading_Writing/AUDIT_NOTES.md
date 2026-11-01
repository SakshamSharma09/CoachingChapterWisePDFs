# Class 9 / Class 10 Reading & Writing — Audit Notes

## Pattern checked (WebSearch/WebFetch, 2026-27 syllabus summaries from third-party publishers; confirm against the official CBSE circular)
**Class 10** — Reading 20: discursive passage 400–450 words (10) + case-based passage 200–250 words with data/visual (10); MCQ and 30–40-word answers. Writing 10: formal letter 100–120 words (5) + analytical paragraph from chart/map/cue 100–120 words (5). Grammar 10 (attempt 10 of 12): determiners, tenses, modals, subject-verb concord, reported speech; gap-filling, editing, transformation.
**Class 9** — Reading 20: factual/literary passage 400–450 words (12) + case-based passage 200–250 words (8). Writing 20: notice/poster ≤50 words (4), letter to editor/formal email 120–150 (5), speech/magazine article 120–150 (5), narrative essay 150–180 (6). Grammar 10: paragraph completion (4), sentence rearrangement (3), sentence transformation (3). Source page also showed an older version (R1: notice or informal invitation, 200–250-word essay); R2 above is treated as the 2026-27 pattern.

## Audit findings (original sets)
| Item | Class 9 original | Class 10 original |
|---|---|---|
| Passage 1 length | 168–216 words (needed 400–450) | 246–321 words (needed 400–450) |
| Passage 2 (case-based) | 30–102 words (notices/small tables; needed 200–250) | 33–90 words (needed 200–250) |
| Reading marks split | 10 + 10 (pattern 12 + 8) | 10 + 10 (correct) |
| Writing tasks | notice 3, letter 5 (half informal), paragraph 4 — no speech/article/narrative | notice 3, letter 5 (half informal), plain paragraph 4 — no data-based analytical paragraph |
| Writing marks | 12 | 12 |
| Grammar | 8 one-mark items | 8 one-mark items, none on paragraph completion/editing mix |
| Answer keys | correct and consistent | correct and consistent |
| Distinctness | all 10 sets distinct | all 10 sets distinct |

## Changes made (in the rebuilt collections; originals untouched)
**Class 9** (`c9/en9/x9_ext.py`, `x9_p2.py`, `w9n_a.py`, `w9n_b.py`, `c9/build9.py`)
- Passage 1 extended with 3 new paragraphs per set to 400–450 words; 2 new sub-questions added (12 marks).
- 10 new case-based passages (200–250 words: school/town notices, surveys, tables, advertisements), 8 questions each (8 marks).
- Writing & Grammar paper rebuilt as 30 marks: notice/poster, formal letter/email (replaced the informal letters), speech/article, narrative essay/story (all with internal choice and model answers); grammar: paragraph completion (4 MCQ), 3 rearrangements, 3 transformations.
**Class 10** (`c10/eng/x10_ext.py`, `w10n_a.py`, `w10n_b.py`, `c10/build10.py`)
- Passage 1 extended by 1–2 paragraphs to 400–450 words (questions unchanged and still valid).
- Case-based passages given a context paragraph before and after the data (200–250 words); all data and questions unchanged ("first sentence" wording changed to "passage").
- Writing rebuilt: formal letter OR formal letter (informal letters removed; letters of request, complaint, enquiry, order, application, editor); data-based analytical paragraph OR (20 new tables with model analyses); the old notice and generic paragraph dropped.
- Grammar raised from 8 to 10 items (added an editing item and a gap-fill item per set).

## Limitations / flags
- Pattern details come from publisher summaries of the 2026-27 syllabus, not the CBSE document; one Class 9 source showed two versions (the newer R2 used).
- Class 9 reading time of 45 minutes and Writing & Grammar time of 1 h 15 min are our estimates.
- Class 10 grammar gives 10 compulsory items instead of "attempt 10 of 12".
- Old Class 9/10 full-syllabus (80-mark) papers still use the old reading/writing sets; they were not rebuilt in this task.
