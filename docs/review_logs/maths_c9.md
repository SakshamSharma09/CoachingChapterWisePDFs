# Review log: maths_c9 (Class 9 Maths, c9m_ch01 to c9m_ch14)

Scope: 14 banks (bank numbering follows the repo; c9m_ch05 = Circles, c9m_ch07 = Probability, c9m_ch08 = Sequences). About 700 questions: every numerical answer was recomputed by hand against the stated working (and the existing in-file asserts in each .py), every MCQ checked for exactly one correct option, the old notes (src/rn_work/c9_maths1, c9_maths2) and the added notes were re-derived, and historical/factual claims were checked against the extracted Ganita Manjari text. All 14 scripts were re-run; PDFs regenerated and validator passes for every chapter.

## Result in one line
No wrong numerical answer and no two-valid-answer MCQ was found in any of the 14 chapters. 6 presentation/content issues found and fixed; a few minor tagging points are left for a teacher (below).

## Linear Polynomials (c9m_ch02) check
Confirmed: 39 of 50 questions are flagged word/application problems (validator minimum 12). All 39 recomputed (fares, savings, tanks, candle, depreciation, break-even, plan comparison, matchsticks, trains, tanks, gym/electricity bills, tile border, temperature conversion). All answers correct; the chapter notes' examples also recomputed correctly.

## Issues found and fixed
1. c9m_ch05 Q16 (Easy): asked for angle AOB but O was never defined as the centre. Added "with centre O".
2. c9m_ch02 Q6 (MCQ): the question printed a literal `**not**` (Markdown not rendered). Changed to "NOT".
3. c9m_ch01 to c9m_ch07: the answer-key PDFs printed literal `**False.**`, `**Side**` etc. (banks ch08 to ch14 already strip it). Added the same `**`-stripping loop on WS q/ans to ch01 to ch07. Checked all 42 Class 9 Maths PDFs afterwards: no `**`, `&lt;` or `&gt;` left.
4. c9m_ch08: chessboard-grains question (3 marks, one-step GP) was tagged Hard; moved to the end of Medium (level M). Counts now E17 M20 H13.
5. c9m_ch12: "Prove diagonals of a rectangle are equal" (3 marks, one congruence) was tagged Hard; moved to the end of Medium. Counts now E17 M20 H13.
6. c9m_ch14 notes: the guesstimate table listed "Water on the Earth as a thin layer" as an "Example from the chapter"; it is not in the NCERT chapter. Replaced (via a text fix applied to the inherited notes block in the ws file; rn_work was not touched) by the chapter's own end-of-chapter brick-count exercise.

## Verified correct (no change needed), notable items
- Ch01: distance/midpoint/section answers, kite, rhombus (area 20), parallelogram (-1,-1),(5,1),(7,5),(1,3), Jaipur grid, taxi vs straight-line (48 extra).
- Ch03: all decimal/fraction conversions, 100th digit of 1/7 = 8, 50th digit of 5/7 = 1, 1/13 rotations, square-root spiral (hypotenuses root2, root3, 2, root5), Brahmagupta/Aryabhata facts match NCERT (628 CE, 499 CE, 3927/1250, Bakhshali).
- Ch04: all expansions/factorisations, sum-product problems (12 and 8; 13 and 7), x+y+z identity, 4 consecutive integers + 1 = 841, a+b=10, a^3+b^3=370 gives 3 and 7.
- Ch05: all chord/angle numbers (13-5-12, 8-15-17, 6-8-10 triples), parallel chords (23/7 cm, 14/2 cm), cyclic kite 10-24-26 (area 240), three villages A(0,0) B(8,0) C(0,6) gives well (4,3).
- Ch06: circumference/area (pi=22/7), Heron (84, 204, 108, 180), Brahmagupta 25-39-52-60 gives 1764 (also = 750 + 1014 by splitting), belt puzzle 2 pi, rangoli outline 352/3, segment 56.
- Ch07: dice/cards/coins counts (15/36, 8/36, 12/25, 13/90 etc.).
- Ch08: AP/GP terms and sums (820, 558, 2325, 1325, 636 = 12 terms, 10836, 852000 vs 894000), pipes n=16 (n=25 rejected), Virahanka V7 = 21, V8 = 34.
- Ch09: counterexamples (2047 = 23 x 89, 41^2, Euler 641 x 6700417 re-multiplied), lockers 1/4/9/16, Pythagorean triples.
- Ch10: weighted means, dilution, alloy (120 g gold, 18 karat), School X/Y paradox (64 vs 71), Brahmagupta pit (2.9 m, 58 m^3).
- Ch11: all Euclid chains (including subtraction step counts 4, 5, 7 and division counts), traces (digit sums 22 and 23), days of week.
- Ch12: all angle/midpoint/centroid/Varignon numbers; tiling angles.
- Ch13: all simultaneous equations (re-solved), ratio-test items, a=5,b=1; k=10 item; area 13.5.
- Ch14: all volumes/areas (pi = 22/7): 539, 550, 704, 28644, 55440/2772/462/9240, 5544/22176/38808/310464, 58212, tent 18040, sector-cone 12 pi, dome 110880.
- Notes in every chapter: formulas, worked examples and tables recomputed; historical claims (Brahmagupta 628, Aryabhata 499, Madhava, Virahanka/Gopala/Hemachandra, Shridharacharya c.750, Al-Khwarizmi c.820, Shivling Peak, calculus remark) match the NCERT text.
- Layout: viewed Ch02 worksheet p1, Ch12 answer key p1, Ch08/Ch12/Ch14 notes pages; nothing clipped or garbled.

## Left as is (minor, teacher may wish to adjust)
- c9m_ch03: Medium "prove 2+root3 irrational" and Hard "show 3+2root5 irrational" are the same technique (the Hard one is light for Hard).
- c9m_ch08: Hard "show 5n+2 is an AP, n^2+1 is not" (3 marks) is easier than the other Hard items. Not moved because Medium would then reach 21 questions.
- c9m_ch09: Hard "factors of 36 and why odd count" (4 marks) is closer to Medium; marks (4) prevent re-tagging without editing the mark scheme. Hard "a divides bc" item mentions that the statement holds for prime a (a fact of Euclid's-lemma type, stated without proof; it is a counter-example question so left).
- c9m_ch07: Medium (Ravi 5 tails), Medium (Meena 3 coins) and Hard (Sunita 5 heads) overlap in idea with other items but are different questions (validator duplicate check passes).
- c9m_ch06/ch14: answers use pi = 22/7 where radii are multiples of 7, as stated in each question; the Class 9 notes say to follow the question's instruction.
- Not independently verified: the exact wording of every NCERT example (only scope and facts were checked); the "scope" call that Brahmagupta's quadrilateral formula, sector/segment items (ch06) and section formula (ch01) are in the assessed syllabus rests on their presence in the Ganita Manjari chapters, not on a separate CBSE deletion list.
