# Review log: science_c9 (Class 9 Science, c9s_ch01..c9s_ch13)

Method: every numerical answer recomputed by hand/python (g = 10 m/s2 as stated); factual items and notes checked against the NCERT PDFs (text extracted with pymupdf). Layout checked by rendering Ch3 worksheet page 1 and Ch7 notes page 3 (no clipping).

## Ch01 Exploration
- Found: Hard-tagged cheetah vs car speed conversion is a one-step conversion (Hard mis-tag).
- Fixed: retagged to Medium and moved into the Medium block.
- Verified: fuel-incident figures (27 875 L, 12 599 L, ~15 000 L short), heartbeat 2.6e9, rice 185 kg, all unit conversions; Saha, celeritas, magnifier/compass facts match NCERT.
- Unresolved: Medium and Hard aircraft-fuel questions are near-duplicates (kept: different depth).

## Ch02 Mixtures
- All concentration/solubility numericals recomputed OK (KNO3, KCl, NaCl values match NCERT Table 5.4); 25 C boiling-point rule, paperfuge, emulsions, alloys match NCERT.
- No changes needed.

## Ch03 Atomic foundations
- Found: Hard question used a "giant covalent solid like sand" (substance A) - not in NCERT; three Hard questions (lime, haematite) were simple percent-composition items.
- Fixed: removed substance A (question now three substances, 3 marks); retagged lime and haematite questions to Medium.
- All mass-ratio, formula-mass, per cent calculations recomputed OK; NaCl six-neighbour lattice, N2O5 name from NCERT.

## Ch04 Journey inside the atom
- Found: two Hard items (Z=14/9/12 table, U-235/238) were routine; the first had 4 marks.
- Fixed: retagged both to Medium (table question marks reduced to 3, key split 1+1+1).
- Verified: isotope averages (B 10.8, Mg 24.32, Cl 75:25), scale calculations, D2O 11.1 %; cobalt-60, I-131, C-14, cricket-ground analogy, Chadwick 1932 match NCERT.

## Ch05 Motion
- All kinematics answers recomputed (thief/jeep t = 16 s, truck stopping 52 m, areas under v-t, etc.): all correct. No changes.

## Ch06 Forces
- All numericals recomputed OK. Fixed: 2 kg block (friction 4 N) and football kick were one-step Hard items; retagged to Medium.

## Ch07 Work, energy, simple machines
- Lever-class table (Class I/II/III) is NOT outside NCERT: Table 7.2 "Classes of Levers" in the chapter has exactly these three classes; kept. (NCERT lists tongs under both Class I and III; the notes table omits tongs from Class I; harmless.) 1 hp = 746 W also in NCERT.
- All numericals recomputed OK (roller coaster 17.3 m/s, ball 0.95 N, ramp MA 4 and 450 J wasted, lunar height 43.2 m, etc.). No changes.

## Ch08 Sound
- All numericals recomputed OK (echo/sonar/rail 2.796 s, 1.72 km cannon, etc.); 0.1 s echo, 0.05 s reverberation, 344 m/s at 22 C, octave, hearing aid, sonic boom match NCERT. No changes.

## Ch09 Cell
- Found: "A typical blood cell is 50 um" is factually wrong (RBC about 7 um).
- Fixed: reworded to "A cell is 50 um across".
- Verified: magnification, 200 um onion cell, potato percent changes, interpolation 12 %, 2^n growth, RBC replacement 2.1e11/day; 120-day RBC, contact inhibition, PCD, Venter, mitosis/meiosis in NCERT.

## Ch10 Tissues
- Found: term "aerenchyma" is not used in NCERT (concept is).
- Fixed: answer now says "specialised parenchyma with large air spaces (called aerenchyma)".
- Verified: root-growth data, ring-width question, Steward totipotency, bone marrow (leukaemia, thalassaemia), 12 pairs of ribs all in NCERT.

## Ch11 Diversity and classification
- Found: lichen Hard question asked which "kingdom" the alga belongs to - ambiguous (NCERT does not classify the alga into a kingdom there).
- Fixed: question now asks the mode of nutrition of each partner; key corrected.
- Verified against NCERT: Pakke 300/1300 = 23 %, hotspots, stromatolites 2.5 bn yr, mangroves 1999, Kyasanur, mushroom cycle 30-45 days, biogas from ruminant gut bacteria.

## Ch12 Reproduction
- Found: the pollen-per-seed data (maize 7.5 lakh/125 seeds; sunflower 30 000/900) and the Hard range figures are not from NCERT and look like real measurements.
- Fixed: both questions now state the figures are illustrative (made-up) values.
- Verified: 2^7 = 128, 1 % of 20 000 = 200, 16 Mar / 31 Mar dates, IVF (Kanupriya/Subhash Mukhopadhyay 1978), menstrual cycle days, trimesters, hygiene (4-6 h), prenatal sex determination ban.

## Ch13 Earth system
- All calculations recomputed OK (solar energy 7.2e6 J, 12 kWh, Rs 100.8, 96 000 houses, 33.3 % CO2 rise vs NCERT's rounded "about 35 %", lapse rate 6.5 C/km, albedo 0.85/0.27 within NCERT ranges). Gyre, North Atlantic Drift, Haber-Bosch, 71 % carbon in oceans, CFC/Montreal from NCERT. No changes.

## Totals
Issues found: 12 (7 mis-tagged difficulty items in Ch1/3/4/6, 1 off-syllabus (Ch3), 1 factual (Ch9), 1 non-NCERT term (Ch10), 1 ambiguous question (Ch11), 2 unsupported data (Ch12)). Fixed: all 12. All chapters regenerated with `python src/ws/c9s_chNN_ws.py` (validator passed).

## Not verified / for a teacher
- Base notes text (from src/rn_work/c9_sci_a and c9_sci_b) was spot-checked against NCERT, not read line by line.
- Answer-key marks splits are accepted as written; only totals were checked for the questions edited.
- Several Hard 3-mark items remain fairly short (e.g. ch06 two-skater, ch05 two-cars); difficulty is a judgement call.
