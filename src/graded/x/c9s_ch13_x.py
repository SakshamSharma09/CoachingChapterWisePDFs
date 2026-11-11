"""Class 9 Science Ch 13 Earth as a System: Energy, Matter and Life - extras."""
from common import AR4, Q

AR = [
 AR4("The albedo of fresh snow is high.", "Snow reflects most of the incoming solar radiation back into space.", "a",
     "Albedo is the fraction of sunlight reflected; snow reflects a large fraction, so its albedo is high."),
 AR4("Carbon dioxide is called a greenhouse gas.", "Nitrogen makes up about 78 per cent of the atmosphere.", "b",
     "Both are true but the composition of the atmosphere does not explain why $\\ce{CO2}$ is a greenhouse gas."),
 AR4("The ozone layer protects living organisms from harmful ultraviolet radiation.", "The ozone layer lies in the troposphere, close to the ground.", "c",
     "A is true; the ozone layer is in the stratosphere, so R is false."),
 AR4("Plants release carbon dioxide to the atmosphere during photosynthesis.", "Photosynthesis uses carbon dioxide and water to make glucose and oxygen.", "d",
     "Plants absorb carbon dioxide in photosynthesis, so A is false; R is true: $\\ce{6CO2 + 6H2O -> C6H12O6 + 6O2}$."),
 AR4("Most of the weather occurs in the troposphere.", "The troposphere is the lowest layer of the atmosphere and contains most of the water vapour and clouds.", "a",
     "Clouds, rain and winds form where the water vapour is, in the troposphere."),
 AR4("Bacteria in the root nodules of legumes increase the fertility of soil.", "Lightning also converts atmospheric nitrogen into nitrogen compounds.", "b",
     "Both are true, but they are two different ways of nitrogen fixation."),
]

CASE = [
 Q("<b>Case study.</b> The Earth is a system of four interacting spheres: the geosphere, hydrosphere, atmosphere and biosphere. When rain falls on a forest hill in Meghalaya, water flows into streams, soaks into the soil, is absorbed by roots and is released as water vapour from the leaves. "
   "(i) Name the sphere that contains all the water on the Earth. (ii) Name the sphere that contains the gases around the Earth. (iii) Which sphere includes all living organisms? (iv) Explain with this example how two spheres interact.",
   "(i) Hydrosphere (1). (ii) Atmosphere (1). (iii) Biosphere (1). (iv) Rain from the atmosphere (water vapour condenses) falls on the geosphere and flows into the hydrosphere (1); plants of the biosphere absorb water from the soil and return water vapour to the atmosphere (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A rooftop of area 100 m$^2$ in Chennai receives 0.8 m of rain in a year. The residents plan rainwater harvesting and also read that burning of fossil fuels is increasing the concentration of carbon dioxide in the atmosphere, leading to global warming. "
   "(i) Find the volume of rainwater falling on the roof in a year. (ii) Express this volume in litres ($1\\text{ m}^3=1000$ L). (iii) Name one greenhouse gas other than carbon dioxide. (iv) Explain how an increase in greenhouse gases leads to a rise in the temperature of the Earth.",
   r"(i) $100\times0.8=80$ m$^3$ (1). (ii) $80\times1000=80\,000$ L (1). (iii) Methane, nitrous oxide or water vapour (any one) (1). (iv) Greenhouse gases trap heat radiated from the Earth's surface (1), so less heat escapes to space and the average temperature of the atmosphere rises (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A school in Nagpur studies the carbon cycle. Green plants absorb carbon dioxide and make glucose. Animals eat plants and release carbon dioxide by respiration. When plants and animals die, decomposers break them down. Burning of coal and petrol adds carbon dioxide to the atmosphere. "
   "(i) Write the word equation for photosynthesis. (ii) Name the process by which animals return carbon dioxide to the air. (iii) Name one human activity that adds carbon dioxide. (iv) Why is planting more trees helpful in reducing the amount of carbon dioxide in the air?",
   r"(i) Carbon dioxide + water $\xrightarrow{\text{sunlight, chlorophyll}}$ glucose + oxygen, i.e. $\ce{6CO2 + 6H2O -> C6H12O6 + 6O2}$ (1). (ii) Respiration (1). (iii) Burning of fossil fuels, deforestation or burning of crop residue (any one) (1). (iv) Trees absorb carbon dioxide during photosynthesis and store the carbon in their bodies (1), so the carbon dioxide in the atmosphere reduces (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Spheres of the Earth", ["Geosphere: rocks, soil and interior. Hydrosphere: all water (oceans, rivers, ice, groundwater, vapour). Atmosphere: envelope of gases. Biosphere: all living organisms with their environment.",
   "Atmosphere layers from the ground: troposphere (weather), stratosphere (ozone layer), mesosphere, thermosphere. Composition of dry air: about 78% $\\ce{N2}$, 21% $\\ce{O2}$, 0.04% $\\ce{CO2}$."]),
 ("Energy balance and albedo", ["Sun is the main source of energy. Albedo $=\\dfrac{\\text{solar radiation reflected}}{\\text{solar radiation received}}$ (fraction between 0 and 1).",
   "High albedo: snow, ice, clouds. Low albedo: oceans, forests, dark soil. Lower albedo $\\rightarrow$ more heat absorbed $\\rightarrow$ warmer surface.",
   "Poles are colder than the equator because sunlight strikes them at a slant and spreads over a larger area."]),
 ("Greenhouse effect and ozone", ["Greenhouse gases ($\\ce{CO2}$, $\\ce{CH4}$, $\\ce{N2O}$, water vapour) trap heat; natural greenhouse effect keeps the Earth warm; enhanced effect causes global warming.",
   "Effects of global warming: melting of ice and glaciers, sea-level rise, extreme weather, changes in rainfall and crops.",
   "Ozone layer absorbs harmful ultraviolet rays; depleted by CFCs (chlorofluorocarbons) from refrigerators, aerosols and so on."]),
 ("Cycles of matter", ["Water cycle: evaporation $\\rightarrow$ condensation (clouds) $\\rightarrow$ precipitation $\\rightarrow$ run-off and infiltration. Carbon cycle: $\\ce{6CO2 + 6H2O ->[light] C6H12O6 + 6O2}$ (photosynthesis); respiration, combustion and decay return $\\ce{CO2}$.",
   "Nitrogen cycle: nitrogen fixation by lightning and by bacteria (<i>Rhizobium</i>) in legume root nodules; nitrates absorbed by plants; denitrifying bacteria return $\\ce{N2}$."]),
 ("Human impact and rainwater", ["Rainwater collected $=$ roof area $\\times$ rainfall depth; $1\\text{ m}^3=1000$ L.",
   "Afforestation, reducing fossil-fuel use, recycling and avoiding plastic reduce human impact; burning crop residue causes air pollution and releases $\\ce{CO2}$."]),
]

MISTAKES = [
 "Placing the ozone layer in the troposphere; it is in the stratosphere, and the weather happens in the troposphere.",
 "Mixing up the greenhouse effect with ozone depletion; greenhouse gases cause warming, CFCs cause ozone depletion.",
 "Saying that high albedo means a surface absorbs more heat; high albedo means more sunlight is reflected and less absorbed.",
 "Writing that plants release carbon dioxide in photosynthesis; photosynthesis absorbs $\\ce{CO2}$ and releases $\\ce{O2}$ (plants release $\\ce{CO2}$ only in respiration).",
 "Not converting units in rainwater problems: $\\text{area}\\times\\text{depth}$ gives m$^3$, which must be multiplied by 1000 to get litres.",
 "Thinking that the Earth's spheres work separately; they interact (for example evaporation links the hydrosphere to the atmosphere).",
]
