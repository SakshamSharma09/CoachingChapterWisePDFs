"""Class 6 SST Ch 5 India, That Is Bharat - Hard-tier extras (assertion-reason, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("The Rig Veda calls the north-western region of India Sapta Sindhava.", "Sapta means seven and Sindhu means river, so the name means the land of seven rivers.", "a",
     "R gives the meaning of the name, which explains why the region was called Sapta Sindhava."),
 AR4("Ashoka used the name Jambudvipa in his inscriptions.", "Jambudvipa means the land of seven rivers.", "c",
     "A is true. R is false: Jambudvipa means the island (dvipa) of the jamun tree; Sapta Sindhava means land of seven rivers."),
 AR4("The word India comes from the river Ganga.", "The Greeks called the river Sindhu 'Indos'.", "d",
     "India comes from the Sindhu (Indus), not the Ganga, so A is false; R is true."),
 AR4("The Himalayas form the northern natural boundary of the Indian Subcontinent.", "The Constitution of India came into force in 1950.", "b",
     "Both statements are true, but they are unrelated."),
 AR4("The names Hind and India are both derived from the river Sindhu.", "The Persians pronounced Sindhu as Hindu or Hind, and the Greeks later changed it to Indos.", "a",
     "R describes how the name Sindhu changed in different languages, explaining A."),
 AR4("Bharatavarsha is a name for the country used in the Mahabharata and the Puranas.", "Bharatavarsha means the land of the Bharatas.", "a",
     "The meaning of the name explains why the country was called Bharatavarsha."),
]

CASE = [
 Q("<b>Case study.</b> A teacher writes three ancient names on the board. The Rig Veda uses Sapta Sindhava for the north-western region. The Mahabharata and the Puranas speak of Bharatavarsha. The Mauryan emperor Ashoka used the name Jambudvipa in his inscriptions. "
   "(i) What does Sapta Sindhava mean? (ii) Which emperor used Jambudvipa? (iii) Which name is found in the epics? (iv) Why do you think the land had many names in different texts and times?",
   "(i) The land of seven rivers (1). (ii) Ashoka (1). (iii) Bharatavarsha (1). (iv) Different texts, regions and rulers used different names over a long period (1), which shows the country has an ancient history and has been known in many ways (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Foreign visitors and neighbours knew India by names that came from the river Sindhu. The Persians called the land beyond the Sindhu Hindu or Hind. The Greeks called it Indos or Indike. Later, the Latin and English name India grew out of these words. "
   "(i) Name the river from which these names come. (ii) What did the Greeks call the land? (iii) Which languages gave us the name India? (iv) Explain how the word Sindhu became Hind and Indos.",
   "(i) The Sindhu (Indus) (1). (ii) Indos or Indike (1). (iii) Greek and Latin, and then English (1). (iv) Persians pronounced the 's' of Sindhu as 'h', giving Hindu or Hind (1); Greeks then dropped the 'h' sound, giving Indos, and from it came India (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Article 1 of the Constitution of India begins with the words 'India, that is Bharat, shall be a Union of States'. The Constitution came into force on 26 January 1950, which is celebrated every year as Republic Day. "
   "(i) Which words in Article 1 mention both names of our country? (ii) In which year did the Constitution come into force? (iii) Which day is celebrated for this? (iv) Give one reason why the Constitution uses both 'India' and 'Bharat'.",
   "(i) 'India, that is Bharat' (1). (ii) 1950 (1). (iii) Republic Day, 26 January (1). (iv) Both names are old and widely used: Bharat comes from ancient texts and India from the river Sindhu, so the Constitution honours both traditions (2).", "1+1+1+2"),
]

MISTAKES = [
 "Mixing up the meanings: <b>Sapta Sindhava</b> = land of seven rivers; <b>Jambudvipa</b> = island of the jamun tree; <b>Bharatavarsha</b> = land of the Bharatas.",
 "Saying India got its name from the Ganga. The name comes from the <b>Sindhu</b> (Indus) through Persian and Greek.",
 "Attributing the wrong source: Sapta Sindhava is in the Rig Veda, Bharatavarsha in the Mahabharata and Puranas, Jambudvipa in Ashoka's inscriptions.",
 "Confusing which people used which name: Persians (Hindu/Hind), Greeks (Indos/Indike), Chinese (Yintu/Yindu).",
 "Writing 1947 for the Constitution coming into force. It came into force on <b>26 January 1950</b>.",
 "Writing that India has only one ancient name; the land has been known by many names in different periods.",
]
