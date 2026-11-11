"""Class 8 Science Ch 6 Pressure, Winds, Storms and Cyclones - extras."""
from common import AR4, Q

AR = [
 AR4("A sharp knife cuts better than a blunt one.", "For the same force, a smaller area of contact gives a larger pressure.", "a", "The sharp edge has a smaller area, so the pressure is greater."),
 AR4("The walls of a dam are made thicker at the bottom.", "Pressure of water increases with depth.", "a", "Greater pressure at the bottom needs a stronger and thicker wall."),
 AR4("Liquids exert pressure only on the base of the container.", "Liquids exert pressure in all directions.", "d", "A is false and R is true: liquids press on the walls as well as the base."),
 AR4("Air exerts pressure on everything in it.", "Atmospheric pressure decreases as we go to greater heights.", "b", "Both true, but the fall of pressure with height does not explain why air exerts pressure."),
 AR4("A cyclone weakens after it reaches the land.", "Land supplies more warm moist air to a cyclone than the ocean does.", "c", "A is true; R is false: the ocean supplies the energy, and the supply is cut off over land."),
 AR4("Winds blow from a region of high pressure to a region of low pressure.", "Air moves so as to reduce the difference in pressure.", "a", "Movement of air from high to low pressure evens out the difference."),
]

CASE = [
 Q("<b>Case study.</b> Mohan weighs 600 N. When he stands on both feet, each foot has an area of 0.01 square metre in contact with the ground. When he lifts one foot, he stands on one foot only. "
   "(i) State the formula for pressure. (ii) Find the pressure when he stands on both feet. (iii) Find the pressure when he stands on one foot. (iv) A camel's wide feet do not sink in the desert sand, but a person's narrow heels do. Explain.",
   "(i) Pressure = force / area (1). (ii) Area = 0.02 square metre, P = 600 / 0.02 = 30000 Pa (1). (iii) P = 600 / 0.01 = 60000 Pa (1). (iv) A camel's wide feet spread its weight over a large area, so the pressure on the sand is small; a heel has a small area, so the pressure is large (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A cyclone formed over the Bay of Bengal and moved towards the Odisha coast. Meteorologists reported very low pressure at the centre, a calm region called the eye, and strong winds in the surrounding wall. Authorities moved people from the coast and a storm surge flooded low villages. After landfall the cyclone weakened within a day. "
   "(i) Where do tropical cyclones form? (ii) Name the calm centre of a cyclone. (iii) Why do winds rush towards the centre? (iv) Give two reasons why the cyclone weakened over land.",
   "(i) Over warm oceans (1). (ii) The eye (1). (iii) The centre is a region of very low pressure and air moves from high to low pressure (1). (iv) It no longer receives warm moist air/water vapour from the sea, and friction with land slows the winds (any two) (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A water tank at the top of a building has a tap at the bottom floor and another at the third floor. Water comes out with a strong flow from the bottom tap and only a weak flow from the upper tap. "
   "(i) Which tap has higher water pressure? (ii) Name the factor on which liquid pressure depends. (iii) Does water press only downwards on the tank? (iv) Explain the strong flow from the bottom tap.",
   "(i) The bottom-floor tap (1). (ii) Depth of the liquid (height of the liquid column above the point) (1). (iii) No, it presses on the base and walls in all directions (1). (iv) The bottom tap is deeper below the water surface in the tank, so the water pressure there is greater and pushes the water out more strongly (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Pressure", [r"$P=\dfrac{F}{A}$ ; force acts perpendicular to the surface.", r"SI unit: pascal (Pa); $1\ \text{Pa}=1\ \text{N/m}^2$.", "Same force: smaller area gives larger pressure (knife, nail); larger area gives smaller pressure (broad straps, tractor tyres)."]),
 ("Liquids and gases", ["Liquids exert pressure on the base and walls, in all directions.", "Liquid pressure increases with depth.", "Air has weight and exerts atmospheric pressure; it decreases with height.",
   "Gases also exert pressure in all directions on the walls of a container."]),
 ("Winds", ["Air moves from high pressure to low pressure; this moving air is wind.", "Uneven heating of land and sea (sea breeze, land breeze) causes pressure differences.",
   "Warm air rises, leaving a low-pressure region."]),
 ("Storms and cyclones", ["Thunderstorm, tornado and tropical cyclone: very low-pressure systems with strong winds.", "Cyclones form over warm oceans; the eye is the calm centre.",
   "Names: hurricane (Atlantic), typhoon (Pacific), cyclone (Indian Ocean).", "Safety: early warning, shelters, evacuation, mangroves/trees as barriers; storm surge causes coastal flooding."]),
]

MISTAKES = [
 "Writing P = A / F or forgetting that the area must be in square metres (convert cm squared first).",
 "Dividing the weight by the area of one foot when the person stands on both feet.",
 "Saying liquid pressure depends on the shape or width of the container; it depends on depth.",
 "Saying wind blows from low to high pressure, or that the eye of a cyclone is the stormiest part.",
 "Writing that atmospheric pressure increases with height.",
 "Confusing pressure (N/m squared, pascal) with force (N, newton).",
]
