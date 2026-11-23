# Review log: maths_c8 (Class 8 Maths, c8m_ch01..c8m_ch14)

Method: every answer in all 14 WS lists was recomputed by hand/in code (marks-vs-working totals were also checked by script); notes (CH) were read line by line and checked against the NCERT Ganita Prakash Part 1/Part 2 PDFs (pymupdf text). PDFs for all edited chapters were regenerated (validator OK). Layout was checked on Ch05 worksheet page 1, Ch05 answer key page 1 and Ch09 notes page 4 (no clipping/garbling).

Result of the numerical pass: about 700 questions recomputed; only 2 answer-level defects found (Ch05 Q4 two correct options, Ch09 Q40 marks), no wrong numeric answers.

## Ch01 A Square and a Cube
- Found: none in answers/notes. Q37 (show 4,104 is a sum of two cubes in two ways) is tagged Hard/3 but is a two-line check (really Medium).
- Fixed: nothing. Unresolved: Q37 tag left (changing level counts risks validator minimums; teacher may retag).

## Ch02 Power Play
- Found: Q30 said "radius of an atom 1x10^-10 m ... each taking up one radius" (physically inconsistent; notes table says diameter).
- Fixed: Q30 now says diameter / one diameter (answer unchanged, 10^7).

## Ch03 A Story of Numbers
- Found: notes said Ishango bone "about 20,000 years old"; NCERT says 20,000 to 35,000 years.
- Fixed: notes wording corrected. Base-5/8 conversions confirmed in NCERT (Section 3.3). Binary mentions (Q5, Q13, Q14, Q28, Q32, Q41, Q42) are extensions of "idea of a base"; NCERT text has no "binary" word but the base idea is in the chapter. Left as is.

## Ch04 Quadrilaterals
- Found: notes table and WS Q5 said a trapezium has "exactly/only one pair" of parallel sides; NCERT defines it as at least one pair (so parallelograms are trapezia).
- Fixed: notes table, relationship bullet and takeaway now follow NCERT; Q5 explanation corrected (answer (c) still the only correct option).

## Ch05 Number Play
- Found: Q4 (palindrome MCQ) had two correct options, 12,321 and 21,312. Kaprekar's constant (Q7, Q28, Q41, notes 5.5 and takeaway) and Collatz (Q31, notes) are not in the NCERT Class 8 chapter (chapter = parity of sums, remainders, divisibility shortcuts, cryptarithms, LCM property).
- Fixed: Q4 option changed to 21,213. Replaced Q7 (even-expression MCQ), Q28 (remainders of sum/difference, NCERT-style), Q31 (remainder 0/2 on division by 4), Q41 (LCM vs product of divisors); notes 5.5 rewritten to parity/remainder/divisibility properties (all taken from the NCERT chapter summary); takeaway updated. Test-code assertions for Kaprekar remain harmless in the file.
- Unresolved: palindrome items (Q4, Q15, Q30, Q48 and notes) are Class 6/7 style content, not in this NCERT chapter; kept as light enrichment (Q48 is a genuine algebra proof). Cryptarithms (an NCERT section 5.3) are not tested at all; teacher may want to add.

## Ch06 We Distribute, Yet Things Multiply
- Found: factorisation (Q17 x^2-16, Q31 x^2+11x+18, Q45 trinomials, and notes paragraph "Factorising") is not in the Class 8 Ganita Prakash chapter (NCERT has identities 1, 1A, 1B, 1C, Sridharacharya's a^2=(a+b)(a-b)+b^2, patterns 1 and 2, mind-the-mistake).
- Fixed: Q17 -> 45x55 by (a+b)(a-b); Q31 -> Sridharacharya's rule for 59^2; Q45 -> proof of 2(a^2+b^2)=(a+b)^2+(a-b)^2 (NCERT Pattern 1) and use; factorising paragraph removed from notes.
- Unresolved: Q38 ($x+1/x$) and notes 6.5 use an algebraic fraction; valid but beyond NCERT; kept as a HOTS item.

## Ch07 Proportional Reasoning - 1
- Found: no wrong answers. Structural overlap: NCERT Ch7 (Part 1) has no percentages at all; about 20 questions (Q3, Q6, Q11, Q14, Q20-24, Q30, Q35, Q36, Q39-41, Q44, Q46, Q50) and notes 7.5-7.6 are really Part 2 Ch1 (Fractions in Disguise) content. Q40 (successive discounts) duplicated Ch08 Q39.
- Fixed: duplication removed on the Ch08 side (see Ch08). Not restructured (instructed not to).
- Unresolved: the percentage block belongs to Ch08; teacher may prefer to swap those items for ratio/unit-conversion/similarity questions.

## Ch08 Fractions in Disguise
- Found: Q39 duplicated Ch07 Q40 (20% and 10% discounts); notes common-mistakes row about "165% of" was garbled.
- Fixed: Q39 now 25% and 20% (price 1,500; single discount 40%, not 45%); notes row reworded. All CI/SI/GST/profit-loss numerics recomputed OK; Kautilya claim confirmed in NCERT text.

## Ch09 Baudhayana-Pythagoras Theorem
- Found: Q40 awarded 4 marks but the key's marking points summed to 5; notes attributed a lotus problem with 2 units/6 units/depth 8 to Lilavati, whereas NCERT's version is 1 unit, 3 units, depth 4.
- Fixed: Q40 marking points now sum to 4; notes lotus problem replaced by the NCERT numbers (9 = 2x+1, x = 4). Fermat/Wiles and Euclid claims confirmed in NCERT.

## Ch10 Proportional Reasoning - 2
- Found: Q1 (24:36) and Q8 (45 min : 2 h) were identical to Ch07 Q1 and Q12.
- Fixed: Q1 now 36:48 (3:4); Q8 now 40 min : 2 h (1:3). Pipes/work, pie chart, maps and inverse proportion verified against NCERT sections 3.2-3.6.

## Ch11 Exploring Some Geometric Themes
- Found: Q30 (four cubes, "front view looking along the direction of the single side cube") was ambiguous and contradicted its own key (looking along that direction hides the side cube).
- Fixed: Q30 reworded (side cube to the right of the bottom cube as seen from the front); key clarified. Nets counts (11, 2, 11, 43,380), Kandariya/Fulani/Escher facts confirmed in NCERT.

## Ch12 Tales by Dots and Lines
- Found: none (all means/medians/frequencies/spreadsheet answers recomputed; 52 bars, 48-box time strip, sleep data story confirmed in NCERT).

## Ch13 Algebra Play
- Found: none (date trick, pyramids, calendar, genie, largest-product, 37/111 results recomputed).

## Ch14 Area
- Found: none (all areas, conversions, path areas recomputed).

## Could not verify / for teacher
- Ch01 Q37 difficulty tag; Ch05 palindrome items and absence of cryptarithms; Ch07 percentage overlap with Ch08; Ch06 Q38 rational expression.
- Ch09 notes Section "Facts about SQRT2" (terminating-decimal argument) is a paraphrase, not checked word-for-word against NCERT.
- Cross-chapter near-duplicates remain: Ch07 Q23 vs Ch08 Q26 (20% up then down); Ch11 Q27 vs Q42 (cuboid shortest path, different numbers, same type).
