# Review log: Class 10 Maths worksheets, answer keys and notes (c10m_ch01..ch14)

Reviewer label: maths_c10. Method: every WS answer recomputed by hand (and cross-checked against the in-file python asserts); every old-notes block (src/rn_work/c10_maths, which the notes borrow) and every added "More Worked Examples" example recomputed; keyword scan of all notes/WS text for off-syllabus items (Euclid, division lemma/algorithm, polynomial division, constructions, ogive/cumulative-frequency graph, frustum, area of triangle by coordinates, cross-multiplication); one worksheet page and one notes page rendered and viewed (Ch13 worksheet p1, Ch10 notes p2). All 14 files re-run; PDFs regenerated and validator passes.

Result: no wrong numerical answer was found in the original 700 questions except the Ch03 k=-6 explanation slip. The problems were mainly one unsound question (Ch02), off-syllabus content (Ch13), duplicates, mark/level mismatches and small wording/notes errors.

## Ch01 Real Numbers
- Found/fixed: Medium "7!+5 and 7x11x13+13 composite" repeated the Easy question's expression -> second expression replaced by 17x19+19 (answer rewritten). Case study (iii) "seat all three groups ... using the same number of chairs" was ambiguous -> reworded (chairs arranged exactly in rows of 84, or 105, or 126; answer 1260 unchanged).
- Unresolved: Medium "prove sqrt5 irrational" and Hard "prove sqrt3 irrational" are the same proof type (kept, both are standard NCERT).

## Ch02 Polynomials
- Found/fixed: Hard "(a^2+9)x^2+13x+6a, one zero reciprocal of the other" (NCERT classic) gives 18x^2+13x+18 whose discriminant is negative, i.e. NO real zeroes, so the question is unsound in a real-number syllabus. Replaced by "(k+1)x^2-10x+(2k-2)" (k=3, 4x^2-10x+4, zeroes 1/2 and 2); in-file assert comment updated.
- Re-tag: "alpha-beta=1, find k" Hard 3 marks -> Medium (two-step). Added a stable sort so numbering stays contiguous.

## Ch03 Pair of Linear Equations
- Found/fixed: Hard "kx+3y=k-3, 12x+ky=k": explanation compared the wrong ratio for k=-6 (said 3/2 != 1/2; the ratio a1/a2 is -1/2). Corrected. Medium Meena question gave an example price pair with pencil Rs 0 -> replaced by (3,1) and (1.50,2). Hostel fixed-plus-rate problem is the same type as the Medium taxi problem -> re-tagged Medium.
- Unresolved: three fixed+rate problems (taxi, hostel, library) are near-duplicates in type with different numbers; the area-of-triangle-from-two-lines item uses base x height of a figure drawn from the given lines (not the coordinate formula), left as is.

## Ch04 Quadratic Equations
- Found/fixed: MCQ distractor "one real and one imaginary root" (imaginary numbers are not in Class 10) -> "two real roots 2 and -2". All other answers verified (including taps 25 h/15 h, train, boat, fencing).

## Ch05 Arithmetic Progressions
- Found/fixed: Hard contractor-penalty question was a direct S_n with 3 marks -> re-tagged Medium. All answers verified (S_n=3n^2+5n, 3-digit multiples of 7 = 70336, spiral 143 cm, ladder rungs 3.85 m, etc.).
- Unresolved: "Rohan's mistake" (3 marks) is rather Medium than Hard; left.

## Ch06 Triangles
- Found/fixed: notes table had a meaningless row "RHS is not needed / Pythagoras plus SSS ... / -" -> removed. Notes step title "Cross-multiply" -> "Clear the fractions" (avoid the excluded cross-multiplication wording). Ladder-pulled-2-m answer reworded (it used 8 m for both the old height and the new foot, which read as an error). Two Hard 3-mark items (equilateral 3a^2=4h^2; converse of BPT 7.2/6.4) re-tagged Medium.
- All proofs (BPT, Pythagoras, cross poles h=2) re-derived and correct.

## Ch07 Coordinate Geometry
- Found/fixed: the answer of "point on x-axis equidistant from (-2,5),(2,-3)" was garbled in the source ("8x+29=-8x+13+\ldots") and patched at run time by a loop; source answer now correct and the patch loop removed. Hard "collinear A,B,C find k" is a mid-point one-liner with 4 marks -> 3 marks and Medium. Notes common-mistakes row mentioned negative k = external division (not required) -> reworded.
- No area-of-triangle formula, collinearity by area, or external division in any question. All 49 answers verified.

## Ch08 Introduction to Trigonometry
- Found/fixed: Easy "sin A, cos A, tan A for AB=3, BC=4" showed mark split "(1/2+1/2+1/2+1/2)" for 5 items -> "(1/2 each)". All identities/numerical answers verified (including (43-24sqrt3)/11, the p^2-1/p^2+1 and cos^2A=(m^2-1)/(n^2-1) proofs).

## Ch09 Some Applications of Trigonometry
- Found/fixed: near-duplicates replaced: "car depression 30 deg, 60 m building" (clone of the 75 m lighthouse item) -> two cars at 45 and 30 deg (43.8 m); "6 m pole shadows at 30/60 and difference" (clone of the 15 m pole item) -> 15 m building, ground distance and line of sight at 30 deg. All values recomputed with sqrt3=1.73.

## Ch10 Circles
- Found/fixed: Easy coin question (25 cm / 24 cm / r=7) duplicated the Medium "Q 25 cm" question -> 26 cm / 24 cm, r=10. Notes (borrowed block) said "A circle can have any number of parallel tangents" - false; reworded (infinitely many tangents, only two parallel to a given direction), patched in the ws file (rn_work not touched). All proofs checked.

## Ch11 Areas Related to Circles
- Found/fixed: notes sector table had "6 pi = 18.86" next to "2 pi = 6.28" (pi mixed); corrected to 18.85. All 49 answers verified (including segments 13.08, 271.27, petals 112, lens 57).
- Unresolved: Medium "circle inscribed in a square" is Easy level; left.

## Ch13 Statistics
- Found/fixed (syllabus): two questions built on "less than" / "more than" cumulative frequency tables (the ogive topic, excluded) replaced: Medium -> median of batter's 30 innings (55 runs); Hard -> error-analysis "mean 24.75 with class mark 20 used instead of 25; correct mean 26". Two Hard items asked students to say whether data is "skewed left/right" (not in NCERT) -> now only ask for the order of mean/median/mode and the empirical-relation check.
- Unresolved: Hard missing-frequency mean problems (f1=28,f2=24 and f1=8,f2=12) are NCERT exercise problems almost verbatim (kept as NCERT-type, answers correct); two missing-frequency means are of the same type.

## Ch12 Surface Areas and Volumes
- Found/fixed: Hard "difference of CSAs of cylinder and cone" (3-mark one-liner) -> Medium. No frustum anywhere; all combinations are of two solids (capsule uses two hemispheres, as NCERT). All answers verified.
- Unresolved: Hard "three spheres melted (6,8,10 -> 12)" is Medium difficulty; left (re-tagging would push Medium to 21).

## Ch14 Probability
- No errors found; all 49 answers and the notes (dice tables, cards, birthdays 1/365, leap-year 2/7) verified.
- Unresolved: several Hard items are easy counting problems (90 discs, 1-50 primes/cubes, 10-99 divisible by 7) - tags are generous; left as the Hard group would otherwise fall below the minimum.

## Notes (all chapters)
Old borrowed notes and added worked examples recomputed; no other numerical or factual error found. Not verified: nothing was checked against the NCERT PDFs themselves (scope/syllabus judged from the brief's exclusion list and knowledge of the rationalised book).
