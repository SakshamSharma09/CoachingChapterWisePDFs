# Class 8 English "Gulmohar" (reader, not NCERT) — chapter bank brief

Repo: D:\Coaching Chapterwise PDFs. Read first: `src/graded/AGENT_BRIEF.md` (bank structure, quality gate, anti-lazy-distractor rule), `src/graded/engh.py` and the finished template `src/graded/c9e_ch01.py` (English bank style: `m(question, "right|wrong1|wrong2|wrong3", why)` MCQs, tier(A,B,C,D), 4 tiers NCERT/Easy/Medium/Hard).

## Book
"Gulmohar" is a Class 8 English reader (NOT an NCERT book); it must stay separate from NCERT/Honeydew material. Source pages are photographs under `_incoming/gulmohar/unitNN_<name>/imgK.jpeg` (git-ignored; view with the Read tool; some pages are photographed twice; a finger or page edge may hide a few words). Reference list of units: https://edurev.in/courses/122917_Gul-Mohar-Class-8-Book-Solutions-Summaries-Worksheets (units in order: 9 The Boy Who Broke the Bank, 10 The Visitor, 11 Helen Keller, 12 The Stolen Bacillus).
The book's structure on each prose page: Before You Read, glossed text with numbered paragraphs, margin-vocabulary boxes, thinking questions, Activities, "Understanding the Text" (A, B questions), "Appreciating the Text", Grammar and Usage. Poem units have Understanding / Appreciating the Poem.

## Your job: ONE module `src/graded/c8gl_chNN.py` for your unit
Module header: `SLUG, NAME, CHNO` (CHNO = the unit number you were given, SLUG like "The_Boy_Who_Broke_the_Bank"), then `TIERS = {"NCERT":..., "Easy":..., "Medium":..., "Hard":...}` exactly as `c9e_ch01.py` ends (>= 30 MCQ, 12 two-mark, 18 three-mark, 12 five-mark items per tier; B/C/D in topic groups as the template does).
Tier meaning: NCERT = like the book's own Understanding/Appreciating questions (para-based, character, theme, vocabulary-in-context); Easy = direct recall/one-step; Medium = inference, cause/effect, character traits, vocabulary & grammar from the unit; Hard = analysis, HOTS, extract-based questions, tone/irony/suspense, value-based/long-answer writing.
Content rules:
1. Read EVERY photo of your unit carefully first; note the author, the plot in order, character names, key quotes (use them only as short extracts, max ~20 words; never reproduce long passages), the glossary words the book teaches, and the grammar point of the unit. Questions must be answerable from the unit as printed in this book (abridged versions differ from the full original story, so follow the book's text, not memory).
2. Original wording; no copying the book's exercise questions verbatim (rephrase). Never claim a fact you cannot see on the pages; for author/background use only what the "Before You Read" box and page headers show plus well-established facts.
3. Mix question types: comprehension, vocabulary in context, grammar (the unit's grammar topic: you may add original practice sentences), extract-based, character, theme/values, creative/opinion answers (with marking points: "(1) ... (1) ..."), short notes. Written answers = brief marking outlines with marks like the other English banks.
4. Every MCQ needs 3 hand-written plausible distractors and exactly one correct answer; no 'none/all of these' filler; no two correct options. Question text unique within a tier.
5. A short unit (poem) must still reach the counts: vary angle (meaning, imagery, devices, tone, word study, extract completion, Helen Keller's life as stated in the unit, comparison of stanzas, value-based writing) without repeating the same question.
## Check and render
```
cd "D:\Coaching Chapterwise PDFs\src\graded"
python run_graded.py c8gl_chNN 8 English_Gulmohar --check
python -W ignore run_graded.py c8gl_chNN 8 English_Gulmohar          # renders 16 PDFs to Class_08/English_Gulmohar/Graded_Papers/ChNN_<slug>/ ; every paper must be 2 pages (retry if you see a transient OSError Errno 22)
python mcq_scan.py ; python syllabus_guard.py
```
Look at one paper page and one key page (pymupdf -> PNG) and spot-check ~15 answers against the photographed text. DO NOT git commit/push. Write only your own module and the rendered folder. Final report <= 8 lines: counts, any page you could not read, doubts.
