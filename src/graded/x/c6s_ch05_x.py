"""Class 6 Science Ch 5 Measurement of Length and Motion - extras."""
from common import AR4, Q

AR = [
 AR4("The SI unit of length is the metre.", "1 metre is equal to 100 centimetres.", "b",
     "Both true; the conversion does not explain why metre is the SI unit."),
 AR4("Standard units are needed to measure length.", "Handspan and footstep differ from person to person.", "a",
     "Non-standard units give different values for different people, so a common standard unit is needed."),
 AR4("The motion of a swing is periodic.", "A swing repeats its motion after equal intervals of time.", "a",
     "Repeating after equal time intervals is the meaning of periodic motion."),
 AR4("To measure the length of a curved line, a thread can be used.", "A thread is a rigid straight scale.", "c",
     "A is true: lay the thread along the curve and measure it on a scale. R is false, a thread is flexible."),
 AR4("A car moving along a straight road shows circular motion.", "Circular motion means moving along a circle.", "d",
     "A is false: it is linear motion. R is true."),
 AR4("To read a scale correctly, the eye must be placed directly above the mark being read.", "Reading from a slant gives an error called parallax.", "a",
     "Reading from the side makes the mark appear shifted; looking straight above avoids it."),
]

CASE = [
 Q("<b>Case study.</b> Sunita measured the length of her classroom using her footsteps and got 12 steps. Her friend Priya measured the same room and got 15 steps. They were confused, so their teacher in Bhopal asked them to use a measuring tape. The tape gave 9 m for both girls. "
   "(i) Name the non-standard unit used by the girls. (ii) Why did they get different values? (iii) What is the SI unit of length? (iv) Express 9 m in centimetres and explain why a measuring tape is better.",
   "(i) Footstep (1). (ii) Their steps are of different sizes (1). (iii) Metre (1). (iv) 9 m = 900 cm (1); a tape gives the same value for everyone because it uses a standard unit (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Karan wants to find the length of a curved road shown on a map and the circumference of a round plate. He has a ruler and a piece of thread. He puts the thread along the curve, marks the ends and then straightens the thread against the ruler. The thread measures 24 cm. "
   "(i) Which tool is used to measure straight short lengths? (ii) How many millimetres are in 24 cm? (iii) Name the unit used for large road distances. (iv) Why did Karan use a thread instead of a ruler directly? Why must the thread not be stretched?",
   "(i) Ruler (1). (ii) 240 mm (1). (iii) Kilometre (1). (iv) A ruler is straight and cannot bend along a curve (1); stretching changes the length of the thread and gives a wrong value (1).", "1+1+1+2"),
 Q("<b>Case study.</b> At a fair in Mysuru, Neha saw a toy train moving along a straight track, a giant wheel turning round and round, and a swing moving to and fro. A butterfly was flying here and there around the stalls. "
   "(i) What kind of motion does the toy train show? (ii) Which of these is a periodic motion? (iii) Which one shows random motion? (iv) The giant wheel completes one turn in 2 minutes. Is its motion periodic? Explain.",
   "(i) Linear motion (1). (ii) The swing (or the giant wheel) (1). (iii) The butterfly (1). (iv) Yes, it repeats the same turn after every 2 minutes (1), equal time intervals mean periodic motion (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Units of length", ["SI unit: metre (m).", "1 m = 100 cm.   1 cm = 10 mm.", "1 km = 1000 m.", "Non-standard units (cubit, handspan, footstep) differ from person to person."]),
 ("Measuring length", ["Short lengths: ruler. Body and cloth: measuring tape.", "Curved line: use a thread, then measure the thread on a ruler.", "Place the zero mark at the start; keep the eye directly above the mark.", "Avoid using a broken end of the scale."]),
 ("Types of motion", ["Linear: straight line (a car on a straight road).", "Circular: along a circle (a stone whirled on a string).", "Rotational: spinning about its own axis (a top, a fan).", "Periodic: repeats after equal times (a pendulum, a swing).", "Random: no fixed pattern (a flying butterfly)."]),
 ("Remember", ["Motion = change of position with time.", "Rest: no change of position.", "Oscillation: to and fro motion about a mean position."]),
]

MISTAKES = [
 "Mixing up conversions: 1 m = 100 cm (not 10 cm), 1 cm = 10 mm, 1 km = 1000 m.",
 "Reading the scale from the side, which gives a wrong value; keep the eye straight above the mark.",
 "Starting the measurement from the 1 cm mark without subtracting; either start at zero or subtract the first reading.",
 "Stretching or loosening the thread while measuring a curved line.",
 "Calling a spinning top <b>circular</b> motion; spinning about its own axis is rotational.",
 "Saying all repeating motion is periodic; it must repeat after <b>equal</b> intervals of time.",
]
