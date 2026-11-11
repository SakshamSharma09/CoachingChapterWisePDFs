"""Class 6 Science Ch 4 Exploring Magnets - extras."""
from common import AR4, Q

AR = [
 AR4("A freely suspended bar magnet always comes to rest along the north-south direction.", "The Earth behaves like a huge magnet.", "a",
     "The Earth's magnetic field acts on the suspended magnet and aligns it, so R explains A."),
 AR4("An iron nail is attracted by a magnet.", "Cobalt and nickel are also magnetic materials.", "b",
     "Both true, but R does not explain why iron is attracted."),
 AR4("Like poles of two magnets attract each other.", "A north pole and a south pole attract each other.", "d",
     "A is false: like poles repel. R is true."),
 AR4("A wooden ruler is attracted by a magnet.", "Wood is a non-magnetic material.", "d",
     "A is false, because wood is non-magnetic; R is true."),
 AR4("The attraction of a magnet is strongest at its poles.", "Iron filings stick mostly near the ends of a bar magnet.", "a",
     "More filings stick at the poles because the attraction is strongest there."),
 AR4("A magnet always has two poles even if it is cut into two pieces.", "Magnetic poles can be separated to get a single north pole.", "c",
     "A is true: each piece gets both poles. R is false, poles cannot be isolated."),
]

CASE = [
 Q("<b>Case study.</b> Rohan found an old compass in his grandfather's trunk in Amritsar. The needle always settled pointing in one direction, however he turned the box. When he brought a bar magnet near, the needle moved away from the north. "
   "(i) What does the needle of a compass point towards when undisturbed? (ii) Name the poles of a magnet. (iii) Why did the needle move when the magnet came near? (iv) How can a compass help travellers find directions?",
   "(i) North (and south) direction (1). (ii) North pole and south pole (1). (iii) The magnet's poles attracted or repelled the needle, which is itself a small magnet (1). (iv) Its north-pointing needle shows north; then south, east and west can be found (1), so travellers can find the way even where there are no landmarks (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In a lab, Ishita brought a magnet near objects: an iron key, a copper coin, a plastic scale, a steel pin, a glass marble and a nickel piece. Only some of them stuck to the magnet. "
   "(i) Name two objects that were attracted. (ii) Name two objects that were not attracted. (iii) What are materials attracted by a magnet called? (iv) Ishita wants to separate iron nails from a heap of sand. Suggest a method and explain.",
   "(i) Iron key and steel pin (1). (ii) Any two of copper coin, plastic scale, glass marble (1). (iii) Magnetic materials (1). (iv) Move a magnet over the mixture (1); iron nails stick to it and the non-magnetic sand stays behind (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Two bar magnets were placed on a table, with the ends marked N and S. When Dev brought the N end of one magnet near the N end of the other, they pushed apart. When he turned one magnet around, they pulled together and stuck. "
   "(i) What happens when like poles are brought near each other? (ii) What happens with unlike poles? (iii) Name the ends of a magnet where attraction is strongest. (iv) A magnet is kept with its S end near a suspended magnet's S end. Predict what happens and give a reason.",
   "(i) They repel (1). (ii) They attract (1). (iii) The poles (1). (iv) They will repel each other and the suspended magnet turns away (1) because like poles repel (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Magnetic and non-magnetic", ["Magnetic: iron, nickel, cobalt (and steel).", "Non-magnetic: wood, plastic, glass, copper, paper, rubber."]),
 ("Poles of a magnet", ["Every magnet has two poles: north and south.", "Attraction is strongest at the poles.", "Poles cannot be separated: cutting a magnet gives two magnets."]),
 ("Rules of attraction", ["Like poles repel (N-N, S-S).", "Unlike poles attract (N-S).", "Repulsion is the sure test for a magnet; attraction alone is not (iron is also attracted)."]),
 ("Direction and uses", ["A freely suspended bar magnet rests in the north-south direction.", "A magnetic compass has a small magnet needle that points north-south.",
   "Uses: compass, fridge and door catches, magnetic toys, separating iron from waste.", "Shapes of magnets: bar, horseshoe, ring, cylinder."]),
]

MISTAKES = [
 "Thinking everything metallic is magnetic; copper and aluminium are metals but <b>not</b> magnetic.",
 "Using attraction alone as the test for a magnet (iron is attracted too); the sure test is <b>repulsion</b>.",
 "Writing 'like poles attract'; <b>like poles repel</b> and unlike poles attract.",
 "Thinking the centre of a bar magnet is the strongest part; it is strongest at the <b>poles</b>.",
 "Believing a magnet cut in half gives a separate north and south pole; each piece has both.",
 "Forgetting that a freely suspended magnet comes to rest in the north-south direction.",
]
