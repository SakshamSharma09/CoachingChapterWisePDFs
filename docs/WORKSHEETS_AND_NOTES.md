# Chapter worksheets, answer keys and detailed notes (Classes 6-10)

For every chapter (Maths 60, Science 62, Social Science 77, English 36 lessons/poems, Hindi 22) there are three PDFs:
- `Class_NN/<Subject>/Worksheets/ChNN_<name>_Worksheet.pdf`: about 50 graded questions (Easy / Medium / Hard tag and marks on every question; word / application problems flagged); no answer lines.
- `..._Worksheet_Answer_Key.pdf`: answers and working with marks.
- `Class_NN/<Subject>/Chapter_Notes/ChNN_<name>_Chapter_Notes.pdf`: detailed notes (4-9 pages: concepts, worked examples, tables, common mistakes, likely questions, key takeaways).

Sources: `src/ws/<bank>_ws.py` (one per chapter; run it to regenerate the three PDFs), builder `src/ws/libws.py`, rules `src/ws/WS_BRIEF.md`, reviewer rules `src/ws/REVIEW_BRIEF.md`.

## Review pass
An independent reviewer pass covered every chapter (recomputing numerical answers, checking facts against the NCERT PDFs, checking that every MCQ has one correct option, tags and marks). Logs with every issue found / fixed / left for a teacher: `docs/review_logs/*.md` (Maths c6-7, c8, c9, c10; Science c6-7, c8, c9, c10; Social Science c6, c7, c8, c9, c10a, c10b; English c9+c10 prose, c10 poems; Hindi c9+c10).
Limits of the review: Maths and Science numbers were recomputed in full; facts were checked against the NCERT PDFs where they are readable. The Class 10 Hindi Kshitij/Kritika PDFs are garbled, the Class 10 English poems are not in the repository, and some base notes inherited from `src/rn_work` were only screened, so those parts rest on the reviewers' knowledge: a subject teacher should skim them. Many 'Hard' tags are generous (several Hard items are Medium effort).

## Known follow-ups
- The older graded Class 9 English banks (`src/graded/c9e_chNN.py`) describe a different book from the NCERT 'Kaveri' textbook in `NCERT_Books/Class_09/English`; the new worksheets follow Kaveri.
- The 'mistakes to avoid' bullets inside the older Class 10 English graded answer keys were corrected for three poems/lessons; the rest of those bullets were not re-verified.
