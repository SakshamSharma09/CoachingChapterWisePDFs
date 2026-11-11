"""Class 6 Science Ch 6 Materials Around Us - extras."""
from common import AR4, Q

AR = [
 AR4("Clear glass is a transparent material.", "Light passes through transparent materials almost completely.", "a",
     "We can see clearly through glass because light passes through it; R explains A."),
 AR4("Wood is an opaque material.", "Frosted glass is a translucent material.", "b",
     "Both true, but they are about different materials; R does not explain A."),
 AR4("Sand dissolves in water.", "Salt dissolves in water.", "d",
     "A is false: sand is insoluble. R is true."),
 AR4("Metals generally show lustre (shine).", "All metals are very soft and can be cut with a knife.", "c",
     "A is true; R is false because most metals are hard (sodium is an exception)."),
 AR4("A steel spoon placed in hot tea soon becomes hot.", "Metals are good conductors of heat.", "a",
     "Because metals conduct heat well, the spoon takes heat from the tea and passes it along."),
 AR4("A cooking pan has a plastic or wooden handle.", "Plastic and wood are poor conductors of heat.", "a",
     "Poor conduction keeps the handle from becoming too hot, so R explains A."),
]

CASE = [
 Q("<b>Case study.</b> Mansi's mother in Nagpur has a steel kadhai with a wooden handle, a glass bowl, a cloth bag and a plastic bucket. She showed that the glass bowl lets light through clearly, tracing paper lets some light through, and a wooden board lets none. "
   "(i) Name the material of the kadhai. (ii) Which material from the story is transparent? (iii) Which is opaque? (iv) Why is the handle of a kadhai made of wood and the kadhai of steel?",
   "(i) Steel (a metal) (1). (ii) Glass (1). (iii) Wood (1). (iv) Metal conducts heat well, so it heats the food (1); wood is a poor conductor so the handle stays cool to hold (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Arjun stirred a spoonful of each of the following in separate glasses of water: salt, sugar, sand, chalk powder and a few drops of oil. Salt and sugar vanished. Sand and chalk settled at the bottom. The oil floated on top. "
   "(i) Which two substances are soluble in water? (ii) Name one insoluble substance that settled. (iii) Which substance floated on the water? (iv) Why does oil float on water? Name one material that dissolves in water but is not seen again.",
   "(i) Salt and sugar (1). (ii) Sand (or chalk) (1). (iii) Oil (1). (iv) Oil does not mix with water and is lighter than it (1); salt (or sugar) dissolves completely (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A teacher in Surat sorted objects into two groups. Group A: iron nail, copper wire, aluminium foil, all hard and shiny. Group B: wooden stick, plastic comb, rubber band, none shiny. Group A objects also conducted electricity in a simple circuit while Group B did not. "
   "(i) What is the property of shine in metals called? (ii) Which group contains metals? (iii) Name a natural material from the story. (iv) Why are electric wires made of copper but covered with plastic?",
   "(i) Lustre (1). (ii) Group A (1). (iii) Wood (1). (iv) Copper is a good conductor of electricity so current flows easily (1); plastic is an insulator, so it protects us from shock (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Materials", ["Material: the substance an object is made of.", "Natural: cotton, wood, wool. Man-made: plastic, nylon.", "Group materials by properties like hardness, lustre, solubility and transparency."]),
 ("Transparency of light", ["Transparent: light passes fully (clear glass, air, water).", "Translucent: light passes partly (tracing paper, frosted glass).", "Opaque: no light passes (wood, metal, brick)."]),
 ("Solubility", ["Soluble: dissolves in water (salt, sugar).", "Insoluble: does not dissolve (sand, chalk, oil).", "Oil and water do not mix; oil floats as a layer."]),
 ("Metals and non-metals", ["Metals: lustre, hard, good conductors of heat and electricity.", "Non-metals: wood, plastic and rubber are poor conductors.", "Good conductor: copper. Insulator: plastic, rubber, wood."]),
]

MISTAKES = [
 "Calling frosted glass or tracing paper transparent; they are <b>translucent</b>.",
 "Saying that insoluble means the substance cannot mix with anything; it means it does not dissolve in <b>water</b>.",
 "Writing that all metals are hard; sodium is soft, and only most metals are hard.",
 "Confusing <b>opaque</b> with translucent: opaque blocks all light.",
 "Thinking oil is soluble because it spreads on water; it floats as a separate layer.",
 "Assuming all shiny objects are metals; lustre alone is not proof, check conduction too.",
]
