"""Class 6 SST Ch 1 Locating Places on the Earth - Hard-tier extras (assertion-reason, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("The Equator is the longest of all the parallels of latitude.", "Parallels of latitude become smaller in size as we move from the Equator towards the poles.", "a",
     "The Equator (0&deg;) is the largest circle; the other parallels shrink towards the poles, which explains A."),
 AR4("All the lines of longitude (meridians) are equal in length.", "All the lines of latitude (parallels) are equal in length.", "c",
     "Every meridian is a half circle from pole to pole, so A is true; parallels shrink towards the poles, so R is false."),
 AR4("The Prime Meridian passes through Delhi.", "The Prime Meridian is the line of 0&deg; longitude.", "d",
     "The Prime Meridian passes through Greenwich near London, so A is false; R is true."),
 AR4("The Equator divides the Earth into the Northern and Southern Hemispheres.", "The Prime Meridian is at 0&deg; longitude.", "b",
     "Both are true, but the reason about the Prime Meridian does not explain how the Equator divides the Earth."),
 AR4("A place at 60&deg;E longitude is ahead of Greenwich time.", "The Earth rotates from west to east.", "a",
     "Places to the east see the Sun first, so their time is ahead; this follows from the west-to-east rotation."),
 AR4("A globe shows the shape of the Earth more truly than a flat map.", "A globe is a spherical model of the Earth.", "a",
     "Because a globe is spherical like the Earth, it avoids the distortions that come from flattening the surface."),
]

CASE = [
 Q("<b>Case study.</b> Riya draws a sketch map of her district. Her map scale is 1 cm = 5 km. The distance from her school to the market is 4 cm on the map, and from the market to the river is 3 cm. She marks the school at the centre and the river towards the east of the market, using the arrow N for north. "
   "(i) What does the scale 1 cm = 5 km tell us? (ii) Find the real distance from the school to the market. (iii) Which three things must every map have? (iv) Riya's actual distance from the market to the river is 20 km. How many cm should she draw on the map?",
   "(i) 1 cm on the map stands for 5 km on the ground (1). (ii) $4\\times5=20$ km (1). (iii) Distance (scale), direction and symbols (1). (iv) $20\\div5=4$ cm; she should draw it 4 cm long (1) because 3 cm would stand for only 15 km (1).", "1+1+1+2"),
 Q("<b>Case study.</b> City X lies on the Prime Meridian. City Y lies at 60&deg;E on the same latitude, and City Z lies at 30&deg;W. Students are asked to compare the local times of these three places when it is 12 noon at City X. "
   "(i) What is the longitude of City X? (ii) How many hours does the Earth take to rotate through 15&deg;? (iii) Is City Y ahead of or behind City X in time? (iv) Find the local time at City Y and at City Z when it is noon at City X.",
   "(i) 0&deg; (1). (ii) 1 hour, since $360&deg;\\div24=15&deg;$ (1). (iii) Ahead, because it lies to the east and the Sun reaches it first (1). (iv) Y: $60\\div15=4$ hours ahead, so 4 p.m. (1); Z: $30\\div15=2$ hours behind, so 10 a.m. (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A teacher gives the coordinates of two places: Place P is at 20&deg;N, 30&deg;E and Place Q is at 20&deg;S, 30&deg;E. She asks the class to locate them on a globe. "
   "(i) In which hemispheres (north-south and east-west) does P lie? (ii) In which north-south hemisphere does Q lie? (iii) Do P and Q lie on the same meridian? (iv) Are P and Q on the same parallel of latitude? Explain how far apart they are in degrees of latitude.",
   "(i) Northern and Eastern Hemispheres (1). (ii) Southern Hemisphere (1). (iii) Yes, both are at 30&deg;E (1). (iv) No, they lie on different parallels (20&deg;N and 20&deg;S) on opposite sides of the Equator (1); they are $20+20=40&deg;$ apart in latitude (1).", "1+1+1+2"),
]

MISTAKES = [
 "Mixing up <b>latitude</b> and <b>longitude</b>: latitudes are east-west parallels measured north or south of the Equator; longitudes are north-south meridians measured east or west of the Prime Meridian.",
 "Saying meridians are parallel to each other. Only <b>parallels of latitude</b> are parallel; meridians meet at the poles.",
 "Writing a scale answer without converting: for 1 cm = 5 km, a 4 cm line is <i>4 x 5 = 20 km</i> (multiply), and real distance to map distance needs <i>division</i>.",
 "Getting the time difference backwards: places to the <b>east</b> are <i>ahead</i> in time and places to the west are behind; each 15&deg; is 1 hour.",
 "Forgetting the direction letters (N, S, E, W) with degrees, e.g. writing 20&deg; instead of 20&deg;N, or calling the Prime Meridian a latitude.",
 "Confusing a <b>map</b>, an <b>atlas</b> and a <b>globe</b>: a map is flat, an atlas is a collection of maps, a globe is a spherical model of the Earth.",
]
