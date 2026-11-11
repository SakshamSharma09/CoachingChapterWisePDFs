"""Class 6 Science Ch 7 Temperature and its Measurement - extras."""
from common import AR4, Q

AR = [
 AR4("The sense of touch is not a reliable way to judge temperature.", "Our skin can be misled by what we touched before, so the same water may feel hot or cold.", "a",
     "After holding a hand in cold water, lukewarm water feels warm; this shows touch can mislead, which R explains."),
 AR4("A clinical thermometer is used to measure the temperature of a human body.", "A laboratory thermometer is used to measure the temperature of boiling water.", "b",
     "Both are true, but the two uses are separate and R does not explain A."),
 AR4("A clinical thermometer can be used to measure the temperature of boiling water.", "A clinical thermometer has a range of about 35 degrees C to 42 degrees C.", "d",
     "A is false: the range is too small and it would break. R is true."),
 AR4("Heat flows from a hot object to a cold object.", "A hot cup of tea left on a table becomes cold because it loses heat to the surroundings.", "a",
     "The tea is hotter than the air, so heat passes from tea to the surroundings."),
 AR4("The normal temperature of a healthy human body is about 37 degrees C.", "The normal body temperature of every person is exactly 40 degrees C.", "c",
     "A is true; R is false, the normal value is about 37 degrees C."),
 AR4("A clinical thermometer should be shaken before use.", "The mercury thread in a clinical thermometer does not fall by itself when the thermometer is taken out of the mouth.", "a",
     "A kink stops the mercury going back, so the thread must be shaken down first."),
]

CASE = [
 Q("<b>Case study.</b> Ananya in Hyderabad felt hot and weak. Her father took a clinical thermometer, shook it so that the mercury level came below 35 degrees C, and placed it under her tongue for about a minute. The reading was 38.5 degrees C. "
   "(i) Why was the thermometer shaken first? (ii) What is the normal body temperature? (iii) In which unit is the temperature read here? (iv) Does Ananya have a fever? Explain why the thermometer should not be held in hot water.",
   "(i) To bring the mercury thread down so that the old reading does not mislead (1). (ii) About 37 degrees C (1). (iii) Degrees Celsius (1). (iv) Yes, 38.5 degrees C is higher than 37 degrees C (1); a hot-water temperature is beyond its range and the thermometer would break (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In a lab, Vikram put a laboratory thermometer into a beaker of hot water. He made sure the bulb was fully in the water but not touching the bottom or the sides, and read the thermometer with his eyes level with the mercury thread. The reading was 70 degrees C. "
   "(i) Name the thermometer used. (ii) Why should the bulb not touch the beaker? (iii) How should the eye be placed while reading? (iv) After a few minutes the reading falls to 55 degrees C. What does this show about the flow of heat?",
   "(i) Laboratory thermometer (1). (ii) The beaker wall may be hotter or colder than the water and give a wrong reading (1). (iii) Level with the mercury thread (1). (iv) Heat has flowed from the hot water to the cooler surroundings (1), so the water got cooler (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Sana placed three bowls in a row: the left one with hot water, the middle one with lukewarm water and the right one with cold water. She put her left hand in the hot water and her right hand in cold water for a minute, then put both in the middle bowl. The left hand felt the middle water cold and the right hand felt it warm. "
   "(i) What do we call how hot or cold something is? (ii) Which instrument gives a reliable reading? (iii) Which sense did Sana use here? (iv) Why did the same water feel different to the two hands?",
   "(i) Temperature (1). (ii) Thermometer (1). (iii) The sense of touch (1). (iv) Each hand had got used to a different temperature (1), so touch gave misleading feelings and cannot be trusted to measure temperature (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Temperature", ["Temperature tells how hot or cold an object is.", "It is measured with a thermometer.", "Unit used in daily life: degree Celsius (degrees C).", "Touch is not reliable for judging temperature."]),
 ("Fixed values", ["Water freezes (ice melts) at 0 degrees C.", "Water boils at 100 degrees C.", "Normal human body temperature: about 37 degrees C."]),
 ("Thermometers", ["Clinical thermometer: body temperature; range about 35 to 42 degrees C; has a kink; shake it down before use.",
   "Laboratory thermometer: range about -10 to 110 degrees C; for liquids and other things.", "Mercury or alcohol inside a thin glass tube expands when heated."]),
 ("Heat flow and materials", ["Heat flows from a hotter object to a colder one.", "Conductors let heat pass easily (iron, copper).", "Insulators do not (wood, plastic).", "Keep the bulb in the liquid, not touching the walls; read at eye level."]),
]

MISTAKES = [
 "Using a clinical thermometer for hot water or for a room; it is only for the <b>human body</b>.",
 "Not shaking the clinical thermometer before use, so an old reading is mistaken for the new one.",
 "Letting the bulb of the laboratory thermometer touch the beaker, or reading it from a slant.",
 "Believing that our hands can measure temperature accurately; touch can be <b>misleading</b>.",
 "Writing that cold flows from ice to a hand; <b>heat</b> flows from the hotter to the colder object.",
 "Writing the wrong units or values: body temperature is about 37 degrees C, not 100 degrees C.",
]
