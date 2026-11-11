"""Class 8 Science Ch 5 Exploring Forces - extras."""
from common import AR4, Q

AR = [
 AR4("Friction is a contact force.", "Friction acts only when two surfaces are in contact and opposes their relative motion.", "a", "R states exactly why friction is a contact force."),
 AR4("The mass of an object is the same on the Earth and on the Moon.", "Mass is the amount of matter in an object, which does not change with place.", "a", "Mass is constant because the quantity of matter is the same; only weight changes."),
 AR4("Two equal and opposite forces acting on a body always make it move.", "Balanced forces have zero net force.", "d", "A is false: balanced forces cannot change the state of motion; R is true."),
 AR4("A rubbed plastic comb attracts small bits of paper.", "Gravitational force acts between the comb and the paper.", "b", "Both true, but the attraction is due to electrostatic force (charges), not gravity, so R does not explain A."),
 AR4("The weight of a body is measured in newton.", "A spring balance measures the mass of a body in kilogram.", "c", "A is true; R is false because a spring balance measures force (weight), calibrated in newton."),
 AR4("Smooth-looking surfaces still experience friction.", "Even polished surfaces have tiny irregularities that interlock with each other.", "a", "Microscopic bumps on every surface cause friction."),
]

CASE = [
 Q("<b>Case study.</b> Harpreet pulls a box of mass 20 kg across a floor with a horizontal force of 60 N. The force of friction between the box and the floor is 40 N. When he puts rollers under the box, the friction drops to 10 N. "
   "(i) Find the net force on the box in the first case. (ii) Is the box moving or at rest? (iii) State the direction of friction. (iv) Find the net force with rollers and explain why rollers help.",
   "(i) 60 - 40 = 20 N in the direction of the pull (1). (ii) Moving, since the net force is not zero (1). (iii) Opposite to the direction of motion (1). (iv) 60 - 10 = 50 N (1); rolling friction is much smaller than sliding friction, so less force is wasted (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Tara's mass is 40 kg. Taking the weight of 1 kg as about 10 N, she stands on a spring balance on the Earth. Her teacher says that on a planet where gravity is weaker the balance would show a smaller reading, but her mass would not change. "
   "(i) Find Tara's weight on the Earth. (ii) What is the SI unit of weight? (iii) Which quantity changes with the place: mass or weight? (iv) A 5 kg bag has a weight of about 50 N. Explain the difference between the mass and weight of the bag.",
   "(i) 40 x 10 = 400 N (1). (ii) Newton (1). (iii) Weight (1). (iv) Mass (5 kg) is the quantity of matter and stays the same everywhere; weight (50 N) is the gravitational pull of the Earth on the bag and depends on the place (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Rehana rubs a plastic scale on dry hair and brings it near tiny pieces of paper, which jump to it. Later, in a humid monsoon evening, the same trick fails. Her teacher says that rubbing causes charging by friction, and that moist air helps the charge to leak away. "
   "(i) Name the force that attracts the paper bits. (ii) Is it a contact or non-contact force? (iii) How does the scale get charged? (iv) Why does the experiment fail on a humid day?",
   "(i) Electrostatic force (1). (ii) Non-contact force (1). (iii) By rubbing (friction) it gains charge (1). (iv) Moist air is a conductor and carries the charge away, so the scale does not stay charged and cannot attract the paper (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Force", ["A force is a push or a pull; SI unit: newton (N).", "A force can change speed, direction of motion or shape of an object.", "Net force on two forces in the same direction $=F_1+F_2$; in opposite directions $=F_1-F_2$ (larger minus smaller).",
   "Balanced forces: net force is zero; unbalanced forces change the state of motion."]),
 ("Types of forces", ["Contact: muscular, friction. Non-contact: gravitational, magnetic, electrostatic.", "Electrostatic force: between charged bodies; like charges repel, unlike attract; charged bodies also attract neutral ones."]),
 ("Friction", ["Opposes the relative motion of surfaces in contact; acts opposite to the motion.", "Kinds: static, sliding, rolling; rolling friction $<$ sliding friction.",
   "Increased by rough surfaces and a greater push; reduced by lubricants, polishing, wheels and ball bearings.", "Fluid friction (drag): acts on objects moving through liquids and gases."]),
 ("Mass and weight", [r"Weight $W=mg$; near the Earth, about 10 N per kg is used in this chapter.", "Mass: kg (constant). Weight: N (changes with gravity).", "Weight is measured by a spring balance."]),
]

MISTAKES = [
 "Writing that friction acts in the direction of motion; it acts <b>opposite</b> to the motion (or its tendency).",
 "Using kg as the unit of weight, or saying weight is constant everywhere.",
 "Subtracting forces that act in the same direction, or adding forces that act in opposite directions.",
 "Thinking friction is always harmful; it is needed for walking, brakes and gripping.",
 "Saying magnetic and electrostatic forces need contact, or that electrostatic force only repels.",
 "Concluding that an object not moving has no force on it; balanced forces also give zero motion change.",
]
