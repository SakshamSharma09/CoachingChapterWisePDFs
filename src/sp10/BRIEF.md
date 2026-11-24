# Brief — transcribe one Class 10 (2026-27) sample paper into structured data

Owner wants, from the CBSE sample papers, (a) chapter-wise worksheets of all DISTINCT questions and (b) section-wise 80-mark tests. To build them we need every question and its solution as clean TEXT (typed by you), with diagrams copied as images only.

## Inputs (per paper) in `WORK/<Subject>/<Paper>/`
(WORK = `C:\Users\Saksham\AppData\Local\Temp\claude\0da2d72d58043887\fc748be4-719d-4cc6-9a85-08dc202f3924\scratchpad\sp10work`)
- `pageNN.png` — every PDF page (read these with the Read tool; the paper comes first, then the solutions/marking scheme).
- `figs.json` + `fig_pNN_k.png` — embedded figures with their page and bbox (PDF points). Reference a figure by its file name.
- The original PDF: `Class_10/<Subject>/Sample_Papers_2026-27/<Paper>_Class10_<Subject>_Sample_Paper_with_Solutions.pdf` (use pymupdf `page.get_text()` for exact text when it is clean — SST/English/Hindi/Science are mostly clean; maths formulas are fragmented, so read the page images).
- If a diagram is vector/not in figs.json, crop it: `python src/sp10/figclip.py <pdf> <page(1-based)> x0 y0 x1 y1 <out.png>`.

## Output: ONE JSON file `src/sp10/data/<Subject>_<Paper>.json`
```json
{"subject":"Maths","paper":"Paper_03","questions":[
 {"no":1,"section":"A","marks":1,"type":"mcq",
  "chapter":"Ch01_Real_Numbers",
  "text":"The HCF of 12 and 18 is",
  "options":["3","6","9","12"],
  "figure":null,
  "answer":"(b) 6 — 12 = 2²·3, 18 = 2·3², HCF = 2·3 = 6.",
  "or":null,
  "subparts":null}
]}
```
- `type`: mcq | ar (assertion-reason; put both statements in `text` and the four standard options in `options`) | vsa | sa | la | case (case/source based: `text` = the passage, `subparts` = list of `{ "text":..., "marks":n, "options":[...]|null, "answer":"..." }`) | map | reading | grammar | writing | literature | other.
- `section`: the paper's own section letter. `marks`: total marks of the question (sum of subparts for case).
- `chapter`: EXACTLY one of the folder ids listed below (the textbook chapter the question tests). For a question that mixes two chapters use the main one. English reading/grammar/writing → `SKILL_Reading`, `SKILL_Grammar`, `SKILL_Writing`; English/Hindi extract questions from a lesson/poem → that lesson's id. Anything that fits nothing → `OTHER` and say why in `"note"`.
- `or`: if the paper gives an internal-choice alternative, the full alternative as the same object shape (text/options/figure/answer), else null. The chapter of the alternative may differ: add `"chapter"` inside `or` too.
- `figure`: file name from figs.json (e.g. `fig_p05_0.png`) when the question needs a diagram/map/table image; for a subpart figure put `"figure"` inside the subpart. Tables should be typed as text (`| a | b |` markdown rows), not copied as images.
- `answer`: the official solution/marking-scheme answer, typed, with the working. Keep marking-scheme step marks only if short. If the PDF has no answer for something, write `"(answer not given in the paper)"` — do not invent.
- Text rules: maths in KaTeX `$...$` (e.g. `$x^2-5x+6=0$`, `\frac{a}{b}`, `\sqrt{3}`, `\angle`, `\triangle`, `\pi`, `^\circ`); chemistry/physics with Unicode or `$\mathrm{H_2O}$`; Devanagari exact for Hindi. Reproduce wording exactly (these are the questions we are compiling); fix only OCR/formatting glitches. No `**`.
- Check: every question number of the paper is present (Maths 38, Science 39, SST 38, English 11 main questions with all sub-questions, Hindi 15 main questions with sub-questions), marks add up to 80, every MCQ has 4 options and an answer.
- Validate with `python src/sp10/validate.py src/sp10/data/<file>.json` and fix what it reports.

## Chapter ids
Use the lists in `src/sp10/chapters.py` (CH[subject]).

## Rules
Only write your own `src/sp10/data/*.json` files (and tiny temp files in the scratchpad). Do not run git commands. Final report ≤ 6 lines: papers done, questions count, anything doubtful.
