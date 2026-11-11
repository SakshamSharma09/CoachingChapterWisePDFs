"""Class 9 SST Ch 4 Atmosphere and Climate - Hard-tier extras (AR, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("Aeroplanes prefer to fly in the lower stratosphere.", "The stratosphere is calm and free from clouds.", "a",
     "Almost all weather occurs in the troposphere, so the stratosphere gives smooth, cloud-free flying."),
 AR4("Temperature falls with altitude in the troposphere.", "The stratosphere is heated by the ozone layer absorbing ultraviolet radiation.", "b",
     "Both are true but R explains why temperature rises in the stratosphere, not why it falls in the troposphere."),
 AR4("During the day a sea breeze blows from the sea towards the land.", "In the daytime the sea heats up faster than the land.", "c",
     "Land heats faster than the sea, creating low pressure over land; so R is false."),
 AR4("Greenhouse gases cool the Earth.", "Greenhouse gases such as carbon dioxide and methane trap heat in the atmosphere.", "d",
     "Trapping heat warms the Earth, so A is false; R is true."),
 AR4("The north-east monsoon brings rain to the Tamil Nadu coast.", "The winds pick up moisture over the Bay of Bengal before reaching the coast.", "a",
     "Moisture gathered over the Bay of Bengal is dropped on the coast of Tamil Nadu."),
 AR4("Nitrogen is the most abundant gas in the atmosphere.", "Oxygen forms about 21 per cent of the atmosphere.", "b",
     "Nitrogen (about 78 per cent) is the most abundant; the share of oxygen is a true fact but does not explain it."),
]

CASE = [
 Q("<b>Case study.</b> A teacher says: 'Weather happens in the lowest layer, which has an average height of about 12 km. Above it lies a layer containing ozone that is calm and cloud-free. Most meteors burn up in a higher layer. In the layer at about 700 km, radio waves are reflected back and auroras appear.' "
   "(i) Name the lowest layer of the atmosphere. (ii) Which layer contains the ozone layer? (iii) In which layer do most meteors burn up? (iv) Name the layer where radio waves are reflected and auroras occur, and state why jet aircraft prefer the lower stratosphere.",
   "(i) Troposphere (1). (ii) Stratosphere (1). (iii) Mesosphere (1). (iv) Thermosphere (ionosphere) (1); because the lower stratosphere is calm and cloud-free, with little weather turbulence (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Kavya's class discusses the monsoon. The word 'mausim' means season. The south-west monsoon brings most of India's rain from June to September. Later, the north-east monsoon winds pick up moisture over the Bay of Bengal and bring rain to the Tamil Nadu coast. "
   "(i) What does the word 'mausim' mean? (ii) During which months does the south-west monsoon bring rain? (iii) Which coast gets rain from the north-east monsoon? (iv) Why is the monsoon described as a seasonal reversal of winds, and why does a weak monsoon matter for India?",
   "(i) Season (1). (ii) June to September (1). (iii) The Tamil Nadu coast (1). (iv) The wind direction reverses with the season, blowing from sea to land in summer and from land to sea in winter (1); a weak monsoon can cause drought and affect farming (1).", "1+1+1+2"),
 Q("<b>Case study.</b> During the monsoon of 2025, the rivers Satluj, Beas and Ravi swelled and flooded large parts of Punjab. Weak embankments and construction near rivers worsened the damage. Scientists link rising carbon dioxide and methane in the air with global warming, and advise planting trees, cycling and using solar energy. "
   "(i) Name two rivers that flooded Punjab in 2025. (ii) In which season did these floods occur? (iii) Name one greenhouse gas. (iv) Give one human factor that worsened the floods and one action that reduces our carbon footprint.",
   "(i) Any two of Satluj, Beas, Ravi (1). (ii) Monsoon (1). (iii) Carbon dioxide (or methane) (1). (iv) Weak embankments or building near rivers (1); planting trees, cycling or using solar energy (1).", "1+1+1+2"),
]

MISTAKES = [
 "<b>Weather</b> is the day-to-day state of the atmosphere; <b>climate</b> is the average weather over 30 years or more. A single rainy day is not climate.",
 "Sea breeze blows from sea to land in the <b>day</b> (land is warmer, low pressure on land); land breeze blows from land to sea at <b>night</b> and is weaker. Do not reverse them.",
 "Order of layers from the surface: troposphere, stratosphere, mesosphere, thermosphere, exosphere. Ozone is in the <b>stratosphere</b>; weather and most water vapour in the troposphere.",
 "Temperature <b>falls</b> with height in the troposphere but <b>rises</b> in the stratosphere (ozone absorbs UV); wind blows from high pressure to low pressure.",
 "Nitrogen is about 78 per cent and oxygen about 21 per cent; do not swap them. Carbon dioxide is only about 0.04 per cent.",
 "South-west monsoon: June to September, most of India's rain; the north-east monsoon rains the Tamil Nadu coast. Greenhouse gases <b>warm</b> the Earth by trapping heat.",
]
