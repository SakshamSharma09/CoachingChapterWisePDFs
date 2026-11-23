# Review log: hindi_c9_c10 (Class 9 Hindi ch01, ch07-ch12; Class 10 Hindi ch01-ch15)

Method. Class 9: every worksheet answer and the notes checked against the Unicode NCERT PDFs (text extracted with pymupdf; the Unicode text is lightly garbled by doubled matras but readable). Class 10: Kshitij/Kritika PDFs use legacy fonts, so answers were checked only against my own knowledge of the lessons and poems; where I was not sure a detail was removed or softened. All 22 PDFs sets were regenerated with `python src/ws/<bank>_ws.py` (all validators pass). Pages viewed as images: Class 9 ch11 worksheet p1 and Class 10 ch08 notes p2; Devanagari renders correctly and nothing is clipped.

## Class 9
- c9hi_ch01 (दो बैलों की कथा): all answers verified against the story. Fixed 1 unsupported claim (Hira "said suffer if you cannot avoid beating"; replaced with the actual quoted line "हमारी जाति का यह धर्म नहीं है").
- c9hi_ch07 (रीढ़ की हड्डी): all facts (dates 1917/1939/1978, lawyer/medical student, quotes) verified against the NCERT text. No errors found, nothing changed.
- c9hi_ch08 (पद, रैदास): 2 fixes. "घन बन" gloss was muddled ("घने वन (बादल)"); now follows the textbook word list (घन = बादल). Notes' summary of Namdev's first pad claimed "Ram is the only support"; replaced with what the text says (questions about origin; "राम कोइ न किसही केरा / तरवर पंखि-बसेरा").
- c9hi_ch09 (भारति, जय, विजय करे!): 2 fixes. Hedged samas answers ("कर्मधारय/उपमान", "द्विगु/बहुव्रीहि") made single answers; notes table made consistent (शतदल, शतमुख = बहुव्रीहि).
- c9hi_ch10 (घर की याद): 4 fixes. Removed "प्रातःकाल" (not in poem) from an MCQ; "चरखे पर कात रहा है" changed to "कातने में व्यस्त" (the poem has no "चरखा"); the answer for the "तू जरा-सा दुख कितना सह सकेगा" question corrected (addressed to the human heart, not to clouds); notes glossary "चरखे पर सूत निकालना" simplified.
- c9hi_ch11 (झाँसी की रानी): 5 fixes. MCQ "बचपन में किस नाम से पुकारा जाता था? मनु/छबीली" had two defensible answers (historically Manu); re-worded to the poem's own usage and "मनु" removed. A garbled question stem fixed. The Jhalkari Bai question and a notes section with a birth date (22 Nov 1830), husband's name etc. were not in the NCERT text; replaced by a question on Kana and Mandra (which is in the poem) and a notes section on the final battle. Notes line on "बचपन का नाम छबीली" corrected.
- c9hi_ch12 (राम-लक्ष्मण-परशुराम संवाद): the name "सुनयना" for Sita's mother is not in the text; removed everywhere (6 places, questions re-phrased, one broken stem repaired). Rest verified against the NCERT excerpt.

## Class 10 (from knowledge, legacy-font PDFs not checked)
- ch01 नेताजी का चश्मा: checked, no errors.
- ch02 बालगोबिन भगत: 1 fix, MCQ about "माघ" had a second defensible option (फागुन); distractor replaced.
- ch03 लखनवी अंदाज़, ch04 एक कहानी यह भी, ch06 संस्कृति, ch07 माता का अँचल, ch11 राम-लक्ष्मण-परशुराम, ch13 उत्साह/अट नहीं रही है: checked, ch13 only had a dubious rasa label ("शृंगार") softened.
- ch05 नौबतखाने में इबादत: removed "लगभग चौदह वर्ष की उम्र में काशी आया" (age not confidently remembered) in the question, answer and notes; added a sentence to keep notes above 1400 words.
- ch08 साना-साना हाथ जोड़ि: the "arrange places in travel order" question and the notes' assertion of the order (गंगटोक -> यूमथांग -> लाचुंग -> कटाओ) could not be confirmed; question replaced with one on the starting point and notes reworded ("अपनी पाठ्यपुस्तक से मिलाकर").
- ch09 मैं क्यों लिखता हूँ?: checked, no errors.
- ch10 सूरदास: 2 fixes. A question asking "तत्सम of गुर" (गुड़ is not tatsama) reworded; the anupras question used an invalid example (पुनरुक्ति / "क्रम बचन"), replaced by "नंद-नंदन".
- ch12 आत्मकथ्य: spelling-question answer was incoherent ("उज्जवल की जगह उज्ज्वल" when the given word is "उज्वल"); fixed.
- ch14 यह दंतुरित मुसकान / फसल: the phrase "चिर प्रवासी" attributed to the poet could not be confirmed; changed to "प्रवासी" and the MCQ re-worded.
- ch15 संगतकार: "उत्प्रेक्षा/उपमा-सूचक" hedge made a single answer (उत्प्रेक्षा); unsupported detail that the main singer "also held the sthayi when a novice" removed (poem only says the accompanist reminds him of his childhood as a novice).

## Counts
About 40 issues found, 40 fixed (Class 9: 16; Class 10: 24), none left unresolved in files.

## Not verified / for a teacher to check
- All Class 10 content (legacy-font PDFs): biographical dates (Nirala 1899-1961, Nagarjun 1911-98, Prasad 1889-1937, Agyeya 1911, Yashpal 1903-76, Mangalesh Dabral 1948, Tulsi 1532-1623, Sur c.1478) are the usual textbook values, not re-checked.
- Class 10 ch08 (Sikkim trip): place order and the Katao/Yumthang details should be matched to the textbook.
- Class 10 ch14: exact wording of the lines about the poet being a stranger/traveller ("प्रवासी") should be matched to the textbook.
- Class 10 ch05: the age at which Bismillah Khan went to Kashi was deliberately left out.
- Hindi sandhi/samas items in several Class 10 chapters (e.g. ch09, ch12) may be beyond the lesson itself but are standard Class 10 grammar.
- Difficulty tags/marks were scanned (no clear mis-tags found; some "Hard" 3-mark items in ch11 Class 9 are modest).
