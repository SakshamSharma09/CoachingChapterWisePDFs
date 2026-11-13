# Class 8 English reader with 'Ruskin Speaks' features (Ruskin Bond-linked; exact title not yet known) — chapter bank brief

Repo: D:\Coaching Chapterwise PDFs. Read first: `src/graded/AGENT_BRIEF.md` (bank structure, quality gate, anti-lazy-distractor rule), `src/graded/engh.py` and the finished template `src/graded/c9e_ch01.py` (English bank style: `m(question, "right|wrong1|wrong2|wrong3", why)` MCQs, tier(A,B,C,D), 4 tiers NCERT/Easy/Medium/Hard).

## Book
A Class 8 English reader (NOT NCERT; exact book title not given by the owner yet; features: "Let's Read", "About the Poet/Author", "Ruskin Speaks" boxes, Comprehension (A match the columns, B reference to the context, C answer the questions), Literary Device, Vocabulary, Listening, Writing). More chapters will be supplied later, so keep every file chapter-specific. Source pages are photographs under `_incoming/ruskin_bond/chNN_<name>/pageK.jpeg` (git-ignored; view with the Read tool; some are slightly angled and have handwritten pencil notes by a student: ignore the notes and use only the printed text; a finger may hide a few words).
Units: 11 "The Child's Story" (Charles Dickens; pages 90-98: the story, glossary words rumbling/scimitars/reckon/solitary/summoned/serene/forbearing, Comprehension, Vocabulary (onomatopoeia, homophones), Listening, Writing) and 12 "Stopping by Woods on a Snowy Evening" (Robert Frost; pages 99-101: the poem, About the Poet, annotated devices, Ruskin Speaks, Comprehension: reference to the context, answer the questions, Literary Device).

## Your job: ONE module `src/graded/c8rb_chNN.py` for your unit
Module header: `SLUG, NAME, CHNO` (CHNO = the unit number you were given, SLUG like "The_Boy_Who_Broke_the_Bank"), then `TIERS = {"NCERT":..., "Easy":..., "Medium":..., "Hard":...}` exactly as `c9e_ch01.py` ends (>= 30 MCQ, 12 two-mark, 18 three-mark, 12 five-mark items per tier; B/C/D in topic groups as the template does).
Define ONLY TWO tiers in TIERS: "NCERT" and "Hard" (framework supports modules with only some tiers). NCERT = like the book's own Comprehension/Literary Device/Vocabulary questions (para-based, character, theme, vocabulary-in-context); Easy = direct recall/one-step; Medium = inference, cause/effect, character traits, vocabulary & grammar from the unit; Hard = analysis, HOTS, extract-based questions, tone/irony/suspense, value-based/long-answer writing.
Content rules:
1. Read EVERY photo of your unit carefully first; note the author, the plot in order, character names, key quotes (use them only as short extracts, max ~20 words; never reproduce long passages), the glossary words the book teaches, and the grammar point of the unit. Questions must be answerable from the unit as printed in this book (abridged versions differ from the full original story, so follow the book's text, not memory).
2. Original wording; no copying the book's exercise questions verbatim (rephrase). Never claim a fact you cannot see on the pages; for author/background use only what the "Before You Read" box and page headers show plus well-established facts.
3. Mix question types: comprehension, vocabulary in context, grammar (the unit's grammar topic: you may add original practice sentences), extract-based, character, theme/values, creative/opinion answers (with marking points: "(1) ... (1) ..."), short notes. Written answers = brief marking outlines with marks like the other English banks.
4. Every MCQ needs 3 hand-written plausible distractors and exactly one correct answer; no 'none/all of these' filler; no two correct options. Question text unique within a tier.
5. A short unit (poem) must still reach the counts: vary angle (meaning, imagery, devices, tone, word study, extract completion, Helen Keller's life as stated in the unit, comparison of stanzas, value-based writing) without repeating the same question.
## Check and render
```
cd "D:\Coaching Chapterwise PDFs\src\graded"
python run_graded.py c8rb_chNN 8 English_Ruskin_Bond --check
python -W ignore run_graded.py c8rb_chNN 8 English_Ruskin_Bond          # renders 16 PDFs to Class_08/English_Ruskin_Bond/Graded_Papers/ChNN_<slug>/ ; every paper must be 2 pages (retry if you see a transient OSError Errno 22)
python mcq_scan.py ; python syllabus_guard.py
```
Look at one paper page and one key page (pymupdf -> PNG) and spot-check ~15 answers against the photographed text. DO NOT git commit/push. Write only your own module and the rendered folder. Final report <= 8 lines: counts, any page you could not read, doubts.
