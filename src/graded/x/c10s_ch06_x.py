"""Class 10 Science Ch 6 Control and Coordination - extras."""
from common import AR4, Q

AR = [
 AR4(r"A reflex action is a quick, automatic response.", r"In a reflex action the signal passes through the spinal cord and not through the brain.", "a",
     r"The short reflex arc through the spinal cord saves time, which makes the response quick."),
 AR4(r"Auxin is synthesised at the shoot tip.", r"Gibberellins help in the growth of the stem.", "b",
     r"Both true; they are different hormones, so R does not explain A."),
 AR4(r"Insulin is secreted by the pancreas.", r"Insulin raises the blood sugar level.", "c",
     r"Insulin lowers the blood sugar level; R is false."),
 AR4(r"Adrenaline is secreted by the pituitary gland.", r"Adrenaline prepares the body to face an emergency situation.", "d",
     r"Adrenaline is secreted by the adrenal glands, so A is false; R is true."),
 AR4(r"Shoots of a plant bend towards light.", r"Auxin accumulates on the shaded side of the shoot and makes the cells there grow longer.", "a",
     r"Faster elongation on the shaded side bends the shoot towards the light (phototropism)."),
 AR4(r"The pituitary gland is called the master gland.", r"The pituitary secretes growth hormone, which regulates growth and development of the body.", "b",
     r"Both true; the pituitary is called master gland because it controls other endocrine glands, which R does not state."),
]

CASE = [
 Q(r"<b>Case study.</b> While helping in the kitchen, Ramesh accidentally touched a hot tava and immediately pulled his hand away, even before he realised that it was hot. "
   r"(i) Name this type of response. (ii) Name the neuron that carries the impulse from the spinal cord to the muscle of the hand. (iii) Which part of the nervous system acts as the main centre for this action? (iv) State two differences between this action and writing a letter.",
   r"(i) Reflex action (1). (ii) Motor neuron (1). (iii) Spinal cord (1). (iv) A reflex is quick, involuntary and does not need thinking (1); writing is voluntary, controlled by the cerebrum and slower (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Mr Gupta's blood test shows a high sugar level. His doctor says that a hormone is not being secreted in sufficient quantity by a gland that lies below the stomach. Mr Gupta's cousin, who lives in a hilly village and does not use iodised salt, has a swollen neck. "
   r"(i) Name the hormone lacking in Mr Gupta. (ii) Name the gland that secretes it. (iii) Name the disease of the cousin's neck. (iv) Name the hormone whose synthesis is affected in the cousin and state one function of that hormone.",
   r"(i) Insulin (1). (ii) Pancreas (1). (iii) Goitre (1). (iv) Thyroxine, as iodine is required to make it (1); it regulates the metabolism of carbohydrates, proteins and fats for proper growth (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Sunita kept a potted seedling near a window. After a few days she found the shoot bent towards the window. She also noticed that the tendrils of her pea plant coiled round a support, and the roots of the seedling grew downwards. "
   r"(i) Name the movement of the shoot towards light. (ii) Name the plant hormone responsible for this bending. (iii) On which side of the shoot does this hormone accumulate? (iv) Name the movement shown by the tendril and explain how it occurs.",
   r"(i) Phototropism (1). (ii) Auxin (1). (iii) On the side away from light (shaded side) (1). (iv) Thigmotropism (response to touch) (1); the part of the tendril in contact with the support grows slowly while the part away from it grows faster, so it coils (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Nervous system", [r"Pathway: receptor $\rightarrow$ sensory neuron $\rightarrow$ CNS (spinal cord/brain) $\rightarrow$ motor neuron $\rightarrow$ effector (muscle/gland).",
   r"Neuron: dendrite $\rightarrow$ cell body $\rightarrow$ axon $\rightarrow$ axon end $\rightarrow$ synapse (chemical transmission) $\rightarrow$ next neuron.",
   r"Reflex arc: receptor $\rightarrow$ sensory neuron $\rightarrow$ spinal cord $\rightarrow$ motor neuron $\rightarrow$ effector (quick, involuntary).",
   r"Receptors: eyes (light), ears (sound, balance), nose (smell), tongue (taste), skin (touch, temperature)."]),
 ("Human brain", [r"Forebrain: cerebrum (thinking, memory, voluntary actions, senses), hunger centre. Midbrain.",
   r"Hindbrain: medulla (involuntary actions: blood pressure, salivation, vomiting), pons, cerebellum (posture, balance, precision of voluntary actions).",
   r"Protection: skull (brain), vertebral column (spinal cord), cerebrospinal fluid."]),
 ("Plant movements and hormones", [r"Tropism: directional growth in response to a stimulus. Phototropism (light), geotropism (gravity), hydrotropism (water), chemotropism (chemicals), thigmotropism (touch).",
   r"Auxin: promotes cell elongation (shoot tip). Gibberellin: stem growth. Cytokinin: cell division (fruits, seeds). Abscisic acid: inhibits growth, causes wilting.",
   r"Sensitive plant (Mimosa): non-directional response due to change in cell turgor."]),
 ("Hormones in animals", [r"Thyroxine (thyroid): metabolism; needs iodine; deficiency causes goitre. Growth hormone (pituitary): growth; deficiency dwarfism, excess gigantism.",
   r"Insulin (pancreas): lowers blood sugar; deficiency causes diabetes. Adrenaline (adrenal): fight-or-flight, raises heart rate and breathing.",
   r"Testosterone (testes) and oestrogen (ovary): changes at puberty. Feedback mechanism regulates hormone release."]),
]

MISTAKES = [
 r"Saying that a reflex action is controlled by the brain; the reflex arc passes through the spinal cord (the brain is informed later).",
 r"Writing that auxin accumulates on the <i>lighted</i> side of the shoot; it accumulates on the shaded side.",
 r"Confusing gland and hormone pairs: adrenaline is from the adrenal gland (not the pituitary), insulin from the pancreas, thyroxine from the thyroid.",
 r"Mixing up the functions of brain parts: cerebellum maintains posture and balance; medulla controls involuntary actions such as blood pressure and vomiting.",
 r"Saying that tropic movements and the movement of Mimosa leaves are the same; tropism is a directional growth, whereas Mimosa's response is a non-directional change in turgor.",
 r"Reading the direction of an impulse wrongly in a neuron; it moves from the dendrite to the cell body, along the axon, and then across the synapse.",
]
