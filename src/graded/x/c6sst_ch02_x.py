"""Class 6 SST Ch 2 Oceans and Continents - Hard-tier extras (assertion-reason, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("The Earth is called the blue planet.", "About 71 per cent of the Earth's surface is covered with water.", "a",
     "Water covers most of the surface, so the Earth looks blue from space; R explains A."),
 AR4("The Pacific Ocean is the largest ocean in the world.", "There are only three oceans on the Earth.", "c",
     "A is true. R is false because there are five oceans: Pacific, Atlantic, Indian, Southern and Arctic."),
 AR4("The Southern Ocean lies around the North Pole.", "The Arctic Ocean is the smallest of the oceans.", "d",
     "The Southern Ocean surrounds Antarctica near the South Pole, so A is false; the Arctic Ocean is indeed the smallest, so R is true."),
 AR4("Asia is the largest continent in the world.", "Antarctica is the coldest continent.", "b",
     "Both statements are true, but the coldness of Antarctica does not explain the size of Asia."),
 AR4("The boundaries between the oceans shown on maps are conventions made by people.", "The waters of all the oceans are connected with one another.", "a",
     "Because ocean water is continuous, the dividing lines are only drawn for convenience."),
 AR4("A tsunami can be caused by an undersea earthquake.", "An undersea earthquake suddenly moves the sea floor and pushes a huge volume of water.", "a",
     "The sudden movement of the sea floor displaces water and forms giant waves, which explains A."),
]

CASE = [
 Q("<b>Case study.</b> A class makes a model of the Earth. They paint 71 parts out of every 100 parts of the surface blue and the remaining 29 parts brown. Most of the brown area is seen in the upper half of the model, which shows the Northern Hemisphere. "
   "(i) What does the blue colour show? (ii) What share of the Earth's surface is land? (iii) In which hemisphere is there more land? (iv) If a pin is dropped at random on the model, is it more likely to fall on land or water? Give a reason.",
   "(i) Water, i.e. the oceans and other water bodies (1). (ii) About 29 per cent (1). (iii) The Northern Hemisphere (1). (iv) On water, because water covers about 71 per cent, i.e. more than twice the area of land (1) so the chance of hitting it is greater (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Ananya is given clues to five oceans. Ocean A is the largest ocean. Ocean B lies between the Americas on one side and Europe and Africa on the other. Ocean C is south of India. Ocean D surrounds the North Pole and is the smallest. Ocean E surrounds Antarctica. "
   "(i) Name Ocean A. (ii) Name Ocean B. (iii) Name Ocean D. (iv) Name Oceans C and E, and state why Ocean C is important for India.",
   "(i) Pacific Ocean (1). (ii) Atlantic Ocean (1). (iii) Arctic Ocean (1). (iv) C is the Indian Ocean and E is the Southern Ocean (1). The Indian Ocean is important because India lies on its shores, with the Arabian Sea on the west and the Bay of Bengal on the east, and it carries trade routes (1).", "1+1+1+2"),
 Q("<b>Case study.</b> On 26 December 2004 a huge sea wave struck the coasts of Tamil Nadu and many other countries around the Indian Ocean, causing great loss of life. The wave was set off by an earthquake under the sea. Afterwards, an early-warning system was set up for the Indian Ocean. "
   "(i) What is this wave called? (ii) What caused it? (iii) What is the purpose of the early-warning system? (iv) Give two precautions that coastal people can take when a warning is issued.",
   "(i) A tsunami (1). (ii) An undersea earthquake (1). (iii) To warn countries and people in time so that they can move to safety (1). (iv) Any two: move quickly to higher ground, follow official instructions and evacuation routes, stay away from the beach until the all-clear (1+1 = 2).", "1+1+1+2"),
]

MISTAKES = [
 "Writing that land covers about three-fourths of the Earth. <b>Water</b> covers about 71 per cent and land about 29 per cent.",
 "Naming only three or four oceans. The five oceans are the Pacific, Atlantic, Indian, Southern and Arctic; the Pacific is the largest and the Arctic the smallest.",
 "Confusing <b>ocean</b>, <b>sea</b> and <b>continent</b>: the Arabian Sea and Bay of Bengal are parts of the Indian Ocean, not separate oceans.",
 "Treating Australia as a country only. It is also the smallest continent; Asia is the largest and Antarctica the coldest.",
 "Mixing up <b>flora</b> (plants) and <b>fauna</b> (animals), and a <b>tsunami</b> (sea wave from an undersea earthquake) with a <b>cyclone</b> (storm with strong winds and rain).",
 "Believing the lines between oceans are natural walls. Ocean water is continuous; the boundaries are only conventions drawn on maps.",
]
