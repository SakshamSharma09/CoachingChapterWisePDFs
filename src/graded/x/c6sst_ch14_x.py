"""Class 6 SST Ch 14 Economic Activities Around Us - Hard-tier extras."""
from common import AR4, Q

AR = [
 AR4("Farming and mining belong to the primary sector.", "Primary activities depend directly on natural resources.", "a",
     "R gives the reason for placing them in the primary sector."),
 AR4("A textile factory belongs to the secondary sector.", "Secondary activities process primary products into other goods.", "a",
     "Cotton from the primary sector is processed into cloth, so R explains A."),
 AR4("Teaching and banking are tertiary activities.", "Tertiary activities directly extract raw materials from the earth.", "c",
     "A is true; R is false, tertiary activities provide services."),
 AR4("The tertiary sector supports the primary and secondary sectors.", "A truck driver who carries wheat to a mill works in the tertiary sector.", "b",
     "Both are true, but R is only one example and does not explain the support role stated in A."),
 AR4("Making bread from wheat flour is a primary activity.", "Growing wheat is a primary activity.", "d",
     "A is false, bread-making is a secondary activity; R is true."),
 AR4("Processing tea leaves into packaged tea is a secondary activity.", "Plucking tea leaves is a tertiary activity.", "c",
     "A is true; R is false, plucking leaves is a primary activity."),
]

CASE = [
 Q("<b>Case study.</b> Kishan grows sugarcane in his field in Uttar Pradesh. He sells it to a nearby mill, where it is turned into sugar. A trader buys the sugar and sells it to shops in the city, where families buy it. "
   "(i) Which sector does Kishan's work belong to? (ii) Which sector does the sugar mill belong to? (iii) Which sector does the trader belong to? (iv) Explain how the three sectors depend on one another in this example.",
   "(i) Primary sector (1). (ii) Secondary sector (1). (iii) Tertiary sector (1). (iv) The farmer supplies sugarcane, which the mill processes into sugar (1); the trader moves and sells the sugar to consumers, so each sector needs the others (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Fatima lives in a coastal village in Kerala. Her father catches fish. Her uncle runs a small unit that cleans and packs the fish, and her aunt is a bus conductor who carries the packed boxes to the market. "
   "(i) Fishing belongs to which sector? (ii) Which sector does the packing unit belong to? (iii) Which sector does the conductor's job belong to? (iv) Why is the primary sector called the base of the economy?",
   "(i) Primary sector (1). (ii) Secondary sector (1). (iii) Tertiary sector (1). (iv) It provides raw materials that other sectors use (1); without such raw produce there would be nothing to process or to sell (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A town in Gujarat has a cotton ginning mill, a cloth-weaving factory, a bank, a school and a hospital. Many people from nearby villages work in these places, while others still grow cotton in their fields. "
   "(i) Name one primary activity in the passage. (ii) Name one secondary activity. (iii) Name one tertiary service. (iv) Why do economic activities in towns often offer more kinds of jobs than in villages?",
   "(i) Growing cotton (1). (ii) Weaving cloth or ginning cotton (1). (iii) Banking, teaching or health care (1). (iv) Towns have factories and many services in addition to farming (1); these need people with different skills, so more kinds of work are available (1).", "1+1+1+2"),
]

MISTAKES = [
 "Placing a factory in the primary sector; it is <b>secondary</b> because it processes primary products.",
 "Treating the primary sector as only farming; it also includes <b>mining, fishing, forestry and animal rearing</b>.",
 "Classifying a teacher, banker or driver as secondary; all are <b>tertiary (service)</b> workers.",
 "Writing that making tea or bread is primary because of the raw materials; the <b>processing</b> step is secondary.",
 "Forgetting that construction of buildings and roads is a <b>secondary</b> activity.",
 "Not showing the link between sectors; each answer should say that one sector's <b>output is another's input</b> or service.",
]
