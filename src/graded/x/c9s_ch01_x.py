"""Class 9 Science Ch 1 Exploration: Entering the World of Chemistry - extras."""
from common import AR4, Q

AR = [
 AR4("Repeating a measurement several times and taking the mean gives a more reliable value than a single reading.", "Random errors in individual readings tend to cancel out when several readings are averaged.", "a",
     "Some readings are slightly too high and some too low, so the mean reduces the effect of random errors."),
 AR4("The least count of a metre scale marked in millimetres is 1 mm.", "The metre is the SI unit of length.", "b",
     "Both statements are true, but the SI unit does not explain why the least count is 1 mm (it is the smallest division on the scale)."),
 AR4("A model can be useful in science even though it is simplified.", "A scientific model is an exact copy of the real object or system.", "c",
     "Models keep only the features that matter for the question, so they are not exact copies; R is false."),
 AR4("A scientific model, once accepted, can never be changed.", "New evidence that disagrees with a model's predictions can lead scientists to modify or replace the model.", "d",
     "A is false because models are revised when evidence demands it; R is true."),
 AR4("A frictionless surface is used as an idealisation in many physics problems.", "Idealisations remove less important details so that the main principle can be studied more easily.", "a",
     "Ignoring friction simplifies the situation; R is the reason idealisations are used."),
 AR4("The metre, the kilogram and the second are SI base units.", "The newton is the SI unit of force.", "b",
     "Both are true; the newton is a derived unit and does not explain why the first three are base units."),
]

CASE = [
 Q("<b>Case study.</b> Kavya measures the length of a pencil with a ruler marked in millimetres. She takes five readings: 14.2 cm, 14.4 cm, 14.3 cm, 14.1 cm and 14.5 cm. Her teacher says that no single reading may be exactly right, so the readings should be combined. "
   "(i) What is the least count of her ruler in cm? (ii) Find the mean length of the pencil. (iii) Express the mean length in metres. (iv) Why is the mean more reliable than the first reading, and what is the largest deviation of any reading from the mean?",
   r"(i) 1 mm = 0.1 cm (1). (ii) $(14.2+14.4+14.3+14.1+14.5)/5=71.5/5=14.3$ cm (1). (iii) $14.3\text{ cm}=0.143$ m (1). (iv) Readings that are too high and too low cancel partly in the mean, so random errors are reduced (1); the largest deviation is $|14.5-14.3|=|14.1-14.3|=0.2$ cm (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A bus from Jaipur to Agra covers 240 km in 4 hours. A second bus on the same route travels at a steady 25 m/s. Rohit wants to compare the two speeds, but they are given in different units. "
   "(i) Find the average speed of the first bus in km/h. (ii) Convert this speed to m/s. (iii) Express 240 km in metres. (iv) Convert the speed of the second bus to km/h and state which bus is faster and by how much in km/h.",
   r"(i) $240/4=60$ km/h (1). (ii) $60\times\tfrac{5}{18}=\tfrac{50}{3}\approx16.7$ m/s (1). (iii) $240\text{ km}=240\times1000=2.4\times10^{5}$ m (1). (iv) $25\times\tfrac{18}{5}=90$ km/h (1); the second bus is faster by $90-60=30$ km/h (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In the chemistry laboratory, Ms Nair shows the class a ball-and-stick model of a water molecule, with red and white balls joined by sticks. A student points out that real atoms are not coloured balls and bonds are not sticks. The teacher explains that the model still helps in predicting properties. "
   "(i) What is a model in science? (ii) Name one limitation of the ball-and-stick model. (iii) Give one other example of a model used in science. (iv) If an experiment gives a result that disagrees with the prediction of a model, what do scientists do, and why?",
   "(i) A model is a simplified representation of an object or system that keeps the features important for the question being studied (1). (ii) Atoms are not hard coloured balls and bonds are not rigid sticks, so it cannot show the real size, motion or electron arrangement (1). (iii) Any one: the solar-system model of the atom, a map, a globe, a particle model of matter (1). (iv) They check the measurements and assumptions and then modify or replace the model (1), because a model is accepted only as long as it agrees with evidence (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Nature of science", ["Observation $\\rightarrow$ question $\\rightarrow$ hypothesis $\\rightarrow$ experiment/testing $\\rightarrow$ conclusion; results are shared and checked by other scientists.",
   "<b>Law</b>: describes a regular pattern in nature. <b>Theory</b>: well-tested explanation that makes testable predictions.",
   "<b>Model</b>: simplified representation that keeps what matters; models are revised when evidence disagrees with them.",
   "<b>Idealisation</b>: ignoring minor effects (e.g. frictionless surface, point mass) to study the main principle."]),
 ("SI units", ["Length: metre (m); mass: kilogram (kg); time: second (s); temperature: kelvin (K); amount of substance: mole.",
   "Prefixes: kilo (k) $=10^{3}$, centi (c) $=10^{-2}$, milli (m) $=10^{-3}$, micro ($\\mu$) $=10^{-6}$, nano (n) $=10^{-9}$.",
   "$1\\text{ km}=1000\\text{ m}$, $1\\text{ m}=100\\text{ cm}=1000\\text{ mm}$, $1\\text{ h}=3600\\text{ s}$."]),
 ("Unit conversion", ["$1\\text{ km/h}=\\dfrac{1000}{3600}\\text{ m/s}=\\dfrac{5}{18}\\text{ m/s}$.",
   "km/h $\\rightarrow$ m/s: multiply by $\\dfrac{5}{18}$; m/s $\\rightarrow$ km/h: multiply by $\\dfrac{18}{5}$.",
   "Multiply by a conversion factor equal to 1, e.g. $\\dfrac{1000\\text{ m}}{1\\text{ km}}$, so that the unwanted unit cancels."]),
 ("Measurement and error", ["Least count = smallest value that an instrument can measure (smallest scale division).",
   "Mean of readings $=\\dfrac{\\text{sum of readings}}{\\text{number of readings}}$.",
   "Error = measured value $-$ true value; repeating and averaging reduces random error.",
   "Precision: closeness of repeated readings to each other. Accuracy: closeness to the true value."]),
 ("Estimation and notation", ["Scientific notation: $N=a\\times10^{n}$ with $1\\le a<10$.",
   "Estimation gives an approximate value using round numbers; it is used to check whether an answer is sensible.",
   "The speed of light in vacuum is denoted by $c\\approx3\\times10^{8}$ m/s."]),
]

MISTAKES = [
 "Multiplying by $18/5$ instead of $5/18$ (or the reverse) when converting between km/h and m/s; remember that m/s values are always <i>smaller</i> numbers.",
 "Writing a measured value without its unit, or mixing units (cm with m) in one calculation.",
 "Confusing <i>law</i> with <i>theory</i>: a law describes a pattern, a theory explains it; a theory does not 'become' a law.",
 "Taking the mean of the readings as 'the true value'; it is only a more reliable estimate, and a single reading is not 'wrong' just because it differs from others.",
 "Treating a model as an exact copy of reality, or saying that a model that fails a test should be ignored instead of being improved.",
 "Mixing up accuracy and precision, and reading the least count of an instrument wrongly (use the smallest division, not the numbered one).",
]
