"""Class 7 Science Ch 6 Heat Transfer in Nature - extras."""
from common import AR4, Q

AR = [
 AR4("Heat always flows from a hotter body to a colder body.", "Heat flows until the two bodies reach the same temperature.", "a",
     "R describes the result of the flow from hot to cold, supporting A."),
 AR4("The heat of the Sun reaches the Earth by radiation.", "Conduction and convection need a material medium, which is almost absent between the Sun and the Earth.", "a",
     "Only radiation can travel through empty space, so R explains A."),
 AR4("Convection takes place in liquids and gases.", "Conduction takes place in solids.", "b",
     "Both are true, but one does not explain the other."),
 AR4("A sea breeze blows from the sea to the land during the day.", "During the day, the sea water gets hotter than the land.", "c",
     "Land heats faster, warm air rises over land and cool air comes in from the sea, so A is true; R is false because land, not sea, becomes hotter."),
 AR4("Dark-coloured clothes are preferred in summer.", "Dark-coloured surfaces absorb more heat radiation than light-coloured surfaces.", "d",
     "Light-coloured clothes reflect more radiation and are preferred in summer, so A is false; R is true."),
 AR4("A thermos flask keeps hot liquids hot for a long time.", "The vacuum between its double walls prevents heat transfer by conduction and convection.", "a",
     "Without a medium, conduction and convection stop, which keeps the liquid hot."),
]

CASE = [
 Q("<b>Case study.</b> Sunita is cooking dal on a gas stove. She leaves a steel spoon in the pan and, after some time, the spoon's handle becomes too hot to hold. She uses a wooden spoon to stir. She also sees the dal circulating inside the pan as it boils. "
   "(i) By which mode does the handle of the steel spoon get hot? (ii) Why is the wooden spoon preferred? (iii) By which mode does the dal circulate? (iv) Explain how the water in a pan gets heated from the bottom to the top.",
   "(i) Conduction (1). (ii) Wood is a poor conductor (insulator) of heat (1). (iii) Convection (1). (iv) Water at the bottom gets heated, becomes lighter and rises (1); cooler, heavier water from the top moves down and a convection current heats all the water (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Meera lives in Chennai near the sea. On a hot afternoon she feels a cool breeze coming from the sea to the land. At night, the breeze flows in the opposite direction. "
   "(i) Which heats faster during the day, land or sea? (ii) What is the afternoon breeze called? (iii) What is the night-time breeze called? (iv) Explain why the breeze blows from the land to the sea at night.",
   "(i) Land (1). (ii) Sea breeze (1). (iii) Land breeze (1). (iv) At night land cools faster than water (1), so the warm air over the sea rises and the cooler air from the land moves in to take its place (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Mohan carries hot tea in a thermos flask during a trip to Shimla. The flask has double walls with a vacuum in between and shiny inner surfaces. On the same day, he wears a white shirt to stay cool in the sun. "
   "(i) By which mode does heat reach Mohan from the Sun? (ii) Why is a white shirt better in summer? (iii) Which two modes of heat transfer does the vacuum stop? (iv) Why are the walls of the flask made shiny?",
   "(i) Radiation (1). (ii) White colour reflects more heat radiation (1). (iii) Conduction and convection (1). (iv) Shiny surfaces reflect heat radiation back (1), so that the tea does not lose heat by radiation and stays hot (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Heat and temperature", [
   "Heat is energy that flows from a hotter body to a colder body; it stops when temperatures become equal.",
   "Temperature tells how hot or cold a body is; the SI unit of temperature is the kelvin, and we commonly use degree Celsius ($^\\circ$C)."]),
 ("Modes of heat transfer", [
   "Conduction: through solids from particle to particle; the particles do not move from their places.",
   "Convection: through liquids and gases by movement of the hot, lighter fluid upward and cold fluid downward.",
   "Radiation: through space without any medium (Sun to Earth); dark surfaces absorb more, light and shiny surfaces reflect more."]),
 ("Conductors and insulators of heat", [
   "Good conductors: metals such as copper, aluminium, iron (used for pans and radiators).",
   "Poor conductors (insulators): wood, plastic, air, wool, rubber (used for handles, clothes).",
   "Woollen clothes keep us warm as they trap air, a poor conductor."]),
 ("Convection in nature", [
   "Sea breeze: day time; land is hotter, warm air over land rises, cool air from the sea blows to land.",
   "Land breeze: night time; sea is warmer, so air blows from land to sea.",
   "Thermos flask: vacuum stops conduction and convection; silvered walls reflect radiation."]),
]

MISTAKES = [
 "Saying that heat flows from a cold body to a hot body; heat always flows from <b>hot to cold</b>.",
 "Writing that conduction needs the movement of particles from place to place; in conduction the particles only pass on the heat and <b>stay in position</b>.",
 "Mixing up sea and land breezes: the <i>sea breeze</i> blows by day (sea to land), the <i>land breeze</i> blows at night (land to sea).",
 "Thinking that heat from the Sun reaches us by conduction or convection; it is <b>radiation</b>, which needs no medium.",
 "Writing that dark colours are better in summer; <b>light</b> colours reflect more radiation.",
 "Confusing heat with temperature; temperature is a measure of hotness, heat is energy in transfer.",
]
