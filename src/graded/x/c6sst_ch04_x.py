"""Class 6 SST Ch 4 Timeline and Sources of History - Hard-tier extras (assertion-reason, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("There is no year zero between 1 BCE and 1 CE.", "In the BCE/CE system 1 BCE is followed directly by 1 CE.", "a",
     "The counting goes from 1 BCE straight to 1 CE, which is why there is no year zero."),
 AR4("The 21st century CE began in the year 2001 and ends in 2100.", "A century is a period of 1,000 years.", "c",
     "A is true because century counting starts from year 1; R is false, a century is 100 years."),
 AR4("Fossils are studied by epigraphists.", "Epigraphists are scholars who study ancient inscriptions.", "d",
     "Fossils are studied by palaeontologists, so A is false; R is true."),
 AR4("Coins and pottery are archaeological sources of history.", "Folk tales told by elders are oral sources of history.", "b",
     "Both are true statements about different kinds of sources; neither explains the other."),
 AR4("In BCE dating, 300 BCE is older than 100 BCE.", "BCE years are counted backwards, so the numbers become smaller as time moves towards CE.", "a",
     "Because numbers fall towards 1 BCE, 300 BCE lies further back in time."),
 AR4("Early communities settled near rivers.", "Rivers provided water and fertile land for farming.", "a",
     "Water and fertile soil made farming possible, which explains why people settled near rivers."),
]

CASE = [
 Q("<b>Case study.</b> A museum labels three objects. An inscription is dated 250 BCE, a copper coin is dated 150 CE and a stone building is dated 1650 CE. The guide says that a student should place them in order on a timeline from oldest to newest. "
   "(i) In which century BCE is 250 BCE? (ii) In which century CE is 150 CE? (iii) In which century CE is 1650 CE? (iv) Arrange the three in order from oldest to newest and explain why 250 BCE is the oldest although 250 is smaller than 1650.",
   "(i) 3rd century BCE (300 to 201 BCE) (1). (ii) 2nd century CE (101 to 200) (1). (iii) 17th century CE (1601 to 1700) (1). (iv) 250 BCE, 150 CE, 1650 CE (1); BCE years are counted backwards from 1 BCE, so any BCE date is earlier than any CE date (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A team of archaeologists digs near an old riverbank. They find clay pots and a copper coin, and a stone slab with writing on it. The village elders narrate a folk tale about the place, and a palm-leaf manuscript in a nearby library also mentions the old town. "
   "(i) Who are the scholars who dig up the remains of the past? (ii) Which kind of source are the pots and coin? (iii) Which kind of source is the folk tale? (iv) Why do historians use many types of sources instead of only one?",
   "(i) Archaeologists (1). (ii) Archaeological sources (1). (iii) Oral source (1). (iv) One source may be incomplete or one-sided (1); using many sources lets historians compare and check facts to get a fuller, more reliable picture (1).", "1+1+1+2"),
 Q("<b>Case study.</b> At Bhimbetka in Madhya Pradesh, visitors see paintings of animals and hunters on the walls of rock shelters. These were made by early humans who lived by hunting animals and gathering plants. After the last Ice Age ended about 12,000 years ago, the climate became warmer and people began to grow grains and settle near rivers. "
   "(i) What are such paintings on rock called? (ii) How did early humans get their food? (iii) Why did people settle near rivers? (iv) How did life change after the Ice Age ended?",
   "(i) Rock art (1). (ii) By hunting animals and gathering plants (1). (iii) For water and fertile soil for farming (1). (iv) The climate became warmer, people began to grow crops (1) and settled in one place instead of moving about (1).", "1+1+1+2"),
]

MISTAKES = [
 "Forgetting that BCE years run <b>backwards</b>: 300 BCE is <i>older</i> than 100 BCE, and every BCE date is earlier than any CE date.",
 "Making a century error: the 21st century is <b>2001 to 2100</b>, and the 3rd century BCE is 300 to 201 BCE, not 200 to 101 BCE.",
 "Believing there is a year 0. The count goes from 1 BCE directly to 1 CE.",
 "Mixing up the experts: <b>archaeologists</b> dig up remains, <b>palaeontologists</b> study fossils, <b>epigraphists</b> study inscriptions, <b>anthropologists</b> study societies.",
 "Putting sources in the wrong type: coins and pottery (archaeological), Vedas and epics (literary), folk tales (oral), paintings and sculptures (artistic).",
 "Writing that early humans farmed and lived in cities. They hunted and gathered and used caves; farming began after the Ice Age.",
]
