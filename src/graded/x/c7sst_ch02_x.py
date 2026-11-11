"""Class 7 SST Ch 2 Understanding the Weather - Hard-tier extras."""
from common import AR4, Q

AR = [
 AR4("Wind blows from high-pressure areas to low-pressure areas.", "Air tends to move to balance a difference in pressure.", "a",
     "R gives the reason for the direction of wind in A."),
 AR4("Mean daily temperature is calculated as (maximum + minimum) / 2.", "Rainfall is measured with a rain gauge.", "b",
     "Both are true, but R is unrelated to the calculation of temperature."),
 AR4("Normal atmospheric pressure at sea level is about 1013 millibars.", "A barometer is used to measure rainfall.", "c",
     "A is true; R is false, a barometer measures pressure and a rain gauge measures rainfall."),
 AR4("Wet clothes dry faster when humidity is high.", "High humidity means the air already holds a large amount of water vapour.", "d",
     "A is false, clothes dry faster when humidity is low; R is true."),
 AR4("Humidity is the amount of water vapour in the air.", "Air with low humidity can take in more water vapour.", "a",
     "R follows from the definition of humidity in A and explains drying."),
 AR4("A wind vane shows the speed of the wind.", "A wind vane points in the direction from which the wind blows.", "d",
     "A is false, a wind vane shows direction, not speed; R is true."),
]

CASE = [
 Q("<b>Case study.</b> A school weather club in Jaipur records the temperature each day. On one day the maximum temperature was 38 degrees C and the minimum was 24 degrees C. The students also fix a rain gauge in the playground, which collected 16 mm of rain after a storm. "
   "(i) Calculate the mean daily temperature. (ii) What does the rain gauge measure? (iii) Name the instrument used to measure temperature. (iv) Why do weather stations keep records of the maximum and minimum temperature?",
   "(i) (38 + 24) / 2 = 31 degrees C (1). (ii) The amount (depth) of rainfall (1). (iii) A thermometer (1). (iv) The mean is worked out from the two extremes (1); long records help to understand patterns and make forecasts (1).", "1+1+1+2"),
 Q("<b>Case study.</b> On a sunny afternoon, the air over land near the Gujarat coast becomes warmer, and its pressure falls. The air over the cooler sea has higher pressure. Winds start to blow from the sea towards the land. A wind sock at the nearby airstrip points inland. "
   "(i) From which area does the wind blow here? (ii) Where is the pressure lower? (iii) Which instrument at the airstrip shows wind direction? (iv) Explain why wind blows from the sea to the land.",
   "(i) From the sea (high pressure) (1). (ii) Over the land (1). (iii) A wind sock (1). (iv) Wind moves from high-pressure to low-pressure areas (1); the warm land has low pressure, so cooler air from the sea moves in to fill it (1).", "1+1+1+2"),
 Q("<b>Case study.</b> During the monsoon, Kavya notices that her washed clothes take two days to dry, though they dry within hours in summer. The newspaper reports that humidity is 90 per cent. In the dry month of May, the humidity is much lower. "
   "(i) What is humidity? (ii) When do clothes dry faster, in high or low humidity? (iii) Which department issues weather forecasts in India? (iv) Why do clothes dry slowly when humidity is high?",
   "(i) The amount of water vapour in the air (1). (ii) In low humidity (1). (iii) The India Meteorological Department (1). (iv) Air that is nearly full of vapour can take little more (1); so water from the clothes evaporates slowly (1).", "1+1+1+2"),
]

MISTAKES = [
 "Mixing up the instruments: <b>thermometer</b> - temperature, <b>rain gauge</b> - rainfall, <b>barometer</b> - pressure, <b>wind vane</b> - direction.",
 "Using the wrong formula for mean daily temperature; it is <b>(maximum + minimum) / 2</b>, not the difference.",
 "Writing that wind blows from low to high pressure; it blows from <b>high to low pressure</b>.",
 "Confusing weather with climate; weather is the <b>day-to-day</b> state of the atmosphere, climate is the long-term pattern.",
 "Forgetting the units: rainfall in <b>mm</b>, temperature in <b>degrees C</b>, pressure in <b>millibars</b>.",
 "Stating that clothes dry faster in high humidity; they dry faster when humidity is <b>low</b>.",
]
