"""Class 9 Science Ch 10 Tissues in Action - extras."""
from common import AR4, Q

AR = [
 AR4("Meristematic tissue is responsible for the growth of plants.", "Its cells are actively dividing.", "a",
     "Growth requires new cells, which are produced by dividing meristematic cells."),
 AR4("Phloem transports food from the leaves to other parts of the plant.", "Xylem is composed mainly of dead cells.", "b",
     "Both are true; the nature of xylem does not explain the function of phloem."),
 AR4("Cardiac muscle fibres are striated and involuntary.", "Cardiac muscle cells are unbranched and have many nuclei.", "c",
     "Cardiac muscle cells are branched and usually have a single nucleus, so R is false."),
 AR4("Blood is a type of epithelial tissue.", "Blood is a fluid connective tissue.", "d",
     "Blood belongs to connective tissue, not epithelial tissue, so A is false; R is true."),
 AR4("Guard cells regulate the opening and closing of stomata.", "Guard cells change their shape when water enters or leaves them.", "a",
     "When guard cells swell the pore opens, and when they lose water it closes."),
 AR4("Ligaments connect bone to bone.", "Tendons connect muscle to bone.", "b",
     "Both statements are true, but they describe different structures."),
]

CASE = [
 Q("<b>Case study.</b> A gardener in Mysuru mows a lawn every week and the grass keeps growing back quickly. He also notices that the trunk of an old neem tree has become thicker over the years, while the tip of a branch has grown longer. "
   "(i) Which meristem is responsible for the regrowth of the cut grass? (ii) Which meristem causes the increase in the girth of the tree? (iii) Which meristem increases the length of the branch tip? (iv) Why can grass regrow after mowing while a branch cut at its tip may not regrow the same way?",
   "(i) Intercalary meristem (1). (ii) Lateral meristem (cambium) (1). (iii) Apical meristem (1). (iv) The intercalary meristem is at the base of the leaves or internodes, below the cut, so it is not removed (1), whereas the apical meristem at the tip is removed when the tip is cut (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In a school activity, Rahul places a freshly cut balsam stem in water mixed with red ink and keeps it in sunlight. After some hours he cuts a thin section and sees red-stained vessels near the centre of the stem. "
   "(i) Which tissue has been stained red? (ii) Name the two conducting elements of this tissue. (iii) In which direction does this tissue conduct? (iv) Why is the phloem not stained, and what does it transport?",
   "(i) Xylem (1). (ii) Tracheids and vessels (1). (iii) Upward, from roots to leaves (1). (iv) Phloem carries food prepared in the leaves, not water from the soil, so it takes up no ink (1); it transports food from leaves to other parts through sieve tubes assisted by companion cells (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A doctor in Lucknow explains to students three kinds of muscle: the one in the wall of the heart, the one in the arm that lifts a book, and the one in the wall of the intestine that pushes food. "
   "(i) Name the muscle tissue of the heart. (ii) Which muscle is attached to bones and is under voluntary control? (iii) Name the muscle found in the intestine wall. (iv) The heart muscle contracts and relaxes rhythmically for a lifetime without fatigue. Why is it involuntary and how does its structure fit its function?",
   "(i) Cardiac muscle (1). (ii) Skeletal (striated) muscle (1). (iii) Smooth (unstriated) muscle (1). (iv) It works without conscious control, so it is involuntary (1); its cells are striated, branched and joined at intercalated discs so that the heart contracts together rhythmically (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Plant tissues", ["Meristematic: apical (tips of root/shoot, length), lateral (cambium, girth), intercalary (base of leaves/internodes, regrowth).",
   "Simple permanent: parenchyma (storage, photosynthesis as chlorenchyma, floating as aerenchyma), collenchyma (flexibility, support), sclerenchyma (dead, lignified, strength; husk of coconut).",
   "Protective: epidermis (stomata, root hairs, waxy cuticle) and cork (dead cells with suberin) in the bark."]),
 ("Complex permanent tissues", ["Xylem: tracheids, vessels, xylem parenchyma, fibres; conducts water and minerals upward; dead cells.",
   "Phloem: sieve tubes, companion cells, phloem parenchyma, fibres; conducts food (both directions); living cells (except fibres)."]),
 ("Animal tissues", ["Epithelial: squamous (flat, lining of mouth, skin), cuboidal (kidney tubules), columnar (intestine), ciliated; stratified for protection.",
   "Connective: blood and lymph (fluid), bone (rigid, skeleton), cartilage (smooth, ear, nose, joints), areolar, adipose (fat storage), tendon (muscle to bone), ligament (bone to bone)."]),
 ("Muscular and nervous tissues", ["Skeletal: striated, voluntary, long, multinucleate. Smooth: unstriated, involuntary, spindle-shaped, single nucleus. Cardiac: striated, involuntary, branched, single nucleus.",
   "Nervous tissue: neurons with cell body, dendrites and axon; carries impulses; the brain, spinal cord and nerves."]),
 ("Organisation", ["Cells $\\rightarrow$ tissue $\\rightarrow$ organ $\\rightarrow$ organ system $\\rightarrow$ organism.",
   "Stomata: pores in the epidermis of leaves bordered by two bean-shaped guard cells; they exchange gases and lose water vapour (transpiration)."]),
]

MISTAKES = [
 "Saying that xylem conducts food and phloem conducts water; xylem: water and minerals, phloem: food.",
 "Calling xylem vessels and sieve tubes both living; xylem conducting elements are dead, sieve tubes are living but without a nucleus and depend on companion cells.",
 "Mixing up tendons and ligaments (tendon: muscle to bone; ligament: bone to bone).",
 "Saying cardiac muscle is voluntary or unbranched; it is involuntary, striated and branched.",
 "Confusing apical meristem (length), lateral meristem (girth) and intercalary meristem (regrowth at base); also writing that meristem cells have large vacuoles (they have dense cytoplasm and small or no vacuoles).",
 "Listing blood as an epithelial tissue; it is a connective tissue with a fluid matrix (plasma).",
]
