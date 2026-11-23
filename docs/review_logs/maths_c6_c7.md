# Review log: maths_c6_c7 (Class 6 Maths ch01-10, Class 7 Maths ch01-08)

Method: every numeric answer in all 18 WS lists recomputed (python for counts, routines, sums, fractions, decimals; by hand for the rest); every MCQ checked for a single correct option; figure-based questions (c6m_ch04) checked against the rendered figure data; notes read in full and worked examples re-checked; NCERT Ganita Prakash chapter text searched with pymupdf for scope (Class 6 ch1, 3, 5). Layout viewed for c6m_ch04 (worksheet p1, key p1, notes p2) and c7m_ch01 (worksheet p1): no clipping. All 18 files re-run and validate (PDFs regenerated).

Result: no wrong numerical answers were found in the 18 answer keys. Issues found were formatting bugs, ambiguity and notes errors (12 in all, all fixed).

## c6m_ch01 Patterns in Mathematics
- Q42 (1+...+100 by pairing) near-duplicate of Q19 (1+...+20). Fixed: now 51+...+100 = 3775 with pairing and a check.

## c6m_ch02 Lines and Angles
- No errors. Q37/Q38 use clock angles with the hour hand at 0.5 deg/min (beyond NCERT text but stated in question and notes). Left.

## c6m_ch03 Number Play
- Q44 (odometer palindrome) answer wording was confusing. Fixed (lists 15051 ... 15951, next is 16061, 110 km).
- Unresolved: the 1089 trick (Q17, Q21, Q38 and notes) is not in the NCERT Class 6 chapter (Kaprekar 6174, Collatz, palindromes, estimation, game 21 are). Mathematically correct; teacher may treat as enrichment.

## c6m_ch04 Data Handling
- Q38 and Q50 answers contained `\times`, `\frac` in non-raw strings, so \t and \f became control characters and the key printed "3 imes50", "3rac12". Fixed with raw strings. (Scanned all 18 files' WS and CH for control characters: none others.)
- Figure data in all 11 figure questions matches the answers.

## c6m_ch05 Prime Time
- Q24 and Q39 ("smallest number leaving remainder r"): 1 and 5 trivially satisfy the condition, so two valid answers. Fixed by adding "greater than 4" / "greater than 12"; notes Example 5 updated likewise.
- Unresolved: NCERT Class 6 Ch5 does not use the terms HCF/LCM (it uses common factors/multiples) and does not teach divisibility by 8 and 11 as notes/Q22/Q43 do. Maths is correct; teacher decides whether to keep as enrichment.

## c6m_ch06 Perimeter and Area
- No errors. Q49 tagged H5 is a listing task (easy-medium work); left.

## c6m_ch07 Fractions
- Q15 wording garbled ("Into how many equal parts and which mark ..."). Rewritten.
- Notes 7.1: garbled sentence on halves/fourths fixed; the "half-century and quarter-final" fraction example removed (not a fraction use). One sentence added to stay above the 1400-word minimum.

## c6m_ch08 Playing with Constructions
- No errors found (circles, diagonals, perpendicular bisector, all answers recomputed).

## c6m_ch09 Symmetry
- Q11, Q18, Q37 and notes: "parallelogram (not a rectangle)" has 0 lines of symmetry is false for a rhombus (2 lines). Changed to "not a rectangle or rhombus" / "neither a rectangle nor a rhombus" everywhere.
- Notes: Hawa Mahal claim (line symmetry) unverified; removed, Taj Mahal kept.

## c6m_ch10 The Other Side of Zero
- No errors. Q40 (a+b=-5, a-b=7 "by trial") is a little advanced for Class 6 but solvable by trial; left.

## c7m_ch01 Large Numbers Around Us
- Notes table: 1 lakh crore (10^12) was written 1,00,00,00,00,000 (that is 10^11). Corrected to 10,00,00,00,00,000 (agrees with Q48 key).

## c7m_ch02 Arithmetic Expressions
- Q37 grammar ("a 18 km"), Example 5 labelled "Taxi fare" for an auto-rickshaw: fixed.

## c7m_ch03 A Peek Beyond the Point
- No errors (all decimal arithmetic recomputed).

## c7m_ch04 Expressions Using Letter-Numbers
- No errors. Q46 (three true/false statements) is tagged Hard but is Easy-Medium work; not retagged (would need reordering).

## c7m_ch05 Parallel and Intersecting Lines
- Q47 ("three angles on a straight line in ratio 2:3:4", angle between bisectors of smallest and largest) depends on their order; added "side by side, in this order".

## c7m_ch06 Number Play
- No errors (Kaprekar, Collatz, reverse-and-add, consecutive-sum counts and 7A3B all verified by program).

## c7m_ch07 A Tale of Three Intersecting Lines
- No errors (triangle-counting questions Q23/Q42/Q48 verified by enumeration).

## c7m_ch08 Working with Fractions
- No errors.

## Could not verify / for a teacher
- NCERT scope of the Class 7 chapters was not text-searched (only spot-checked by topic); Class 6 ch1/3/5 were.
- Class 6 Ch2 Q37-38 and Class 7 Ch5 Q42 use the hour hand at 0.5 deg per minute, which is outside the NCERT chapters (given in the question).
- Several H-tagged items are only moderately hard (c6m_ch07 Q38/Q44/Q47, c7m_ch04 Q46, c7m_ch07 Q49); tags left as is.
