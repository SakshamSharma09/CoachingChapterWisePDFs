"""Class 6 Science Ch 7 - Temperature and its Measurement: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch07"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch07", str(REPO / "src/rn_work/c6_sci/ch07.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Temperature is a reliable measure of the ______ of a body.", 1, "(b) hotness or coldness", "E", opts=["weight", "hotness or coldness", "size", "colour"]),
W("The normal temperature of the human body is:", 1, "(c) 37.0 °C", "E", opts=["25.0 °C", "30.0 °C", "37.0 °C", "45.0 °C"]),
W("The SI unit of temperature is:", 1, "(d) kelvin", "E", opts=["degree Celsius", "degree Fahrenheit", "metre", "kelvin"]),
W("Which thermometer is used to measure the temperature of a person with fever?", 1, "(a) clinical thermometer", "E", opts=["clinical thermometer", "laboratory thermometer", "a ruler", "a spring balance"]),
W("The range of a usual laboratory thermometer is:", 1, "(b) –10 °C to 110 °C", "E", opts=["0 °C to 37 °C", "–10 °C to 110 °C", "35 °C to 42 °C", "100 °C to 500 °C"]),
W("Old clinical thermometers are being replaced because they contain a toxic liquid metal. Which one?", 1, "(c) mercury", "E", opts=["iron", "copper", "mercury", "silver"]),
W("Write True or False: Our sense of touch always tells us correctly how hot a body is.", 1, "False. The sense of touch is not reliable; the same water can feel cool to one hand and warm to the other. (1)", "E"),
W("Fill in the blank: In a digital clinical thermometer the temperature is shown on a ______.", 1, "display (screen).", "E"),
W("Write the symbol for degree Celsius and for kelvin.", 2, "Degree Celsius: °C; kelvin: K (no degree sign). (1+1)", "E"),
W("Write the normal body temperature in degree Fahrenheit.", 1, "98.6 °F. (1)", "E"),
W("Name the Indian woman scientist known as the 'Weather Woman of India'.", 1, "Anna Mani. (1)", "E"),
W("Where is the bulb of a digital clinical thermometer placed to measure body temperature?", 1, "Under the tongue. (1)", "E"),
W("Name two kinds of thermometers.", 2, "Clinical thermometer and laboratory thermometer. (1+1)", "E"),
W("Which liquid, other than mercury, is used inside a laboratory thermometer? What is its colour?", 2, "Alcohol, coloured red. (1+1)", "E"),
W("Why can a clinical thermometer not be used to measure the temperature of boiling water?", 2, "Its range is only about 35 °C to 42 °C, much lower than 100 °C, so it cannot read such a high temperature (and may break). (2)", "E"),
W("Convert 0 °C into kelvin using K = °C + 273.15.", 1, "0 + 273.15 = 273.15 K. (1)", "E"),
W("What is the use of a wall (room) thermometer?", 1, "It shows the approximate temperature of the room (air). (1)", "E"),
W("What does a thermometer with a reading of 38.5 °C tell about a person: is the person's temperature higher or lower than normal?", 1, "Higher than normal (37.0 °C), so the person may have a fever. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Activity: the right hand is kept in warm water, the left hand in ice-cold water, and then both in tap water. Why does the tap water feel cool to one hand and warm to the other?", 2, "Each hand has got used to the earlier temperature (1). The right hand feels the tap water cooler than the warm water and the left hand feels it warmer than the cold water, so touch is unreliable (1).", "M"),
W("Priya's temperature, taken by a digital thermometer under the tongue, is 38.2 °C. Is it normal? By how much is it above normal?", 2, "It is not normal (1). 38.2 – 37.0 = 1.2 °C above normal (1).", "M", wp=True),
W("Why should the thermometer tip be washed with soap and water before and after use?", 2, "To remove germs so that the infection does not spread from one person to another. (2)", "M"),
W("A thermometer has 10 small divisions between the marks 20 °C and 30 °C. Find its least count (smallest value).", 2, "Difference of big marks = 30 – 20 = 10 °C (1). 10 ÷ 10 = 1 °C per division (1).", "M"),
W("The temperature of a cup of tea is 80 °C. Find it in kelvin.", 2, "K = °C + 273.15 (1) = 80 + 273.15 = 353.15 K (1).", "M", wp=True),
W("Aarav measures the temperature of hot water in a beaker. His thermometer touches the bottom of the beaker. What mistake did he make? What will happen to the reading?", 2, "The bulb must not touch the bottom or sides (1). The bottom is hotter than the water, so the reading will be wrong, too high (1).", "M", wp=True),
W("Give two reasons why digital thermometers are better than mercury thermometers.", 2, "Mercury is toxic and hard to dispose of if the thermometer breaks (1); digital thermometers are safe and easy to read (1).", "M"),
W("For small children the thermometer is sometimes placed in the armpit. Will the reading be higher or lower than the real body temperature? By how much?", 2, "Lower (1), by about 0.5 °C to 1 °C (1).", "M", wp=True),
W("Why should we read a laboratory thermometer while the bulb is still in the water?", 2, "As soon as the thermometer is taken out, the liquid column starts to fall, so the reading becomes wrong. (2)", "M"),
W("Fill in the table: (i) Scale named after Celsius, unit symbol ____ (ii) Scale named after Fahrenheit, unit symbol ____ (iii) SI scale, unit symbol ____", 3, "(i) °C (ii) °F (iii) K. (1 each)", "M"),
W("Write two rules for correct writing of temperature units, as given in the chapter.", 2, "Any two: symbol has no full stop; keep a space between the number and the symbol (37.0 °C); the unit kelvin has no degree sign; names of scales begin with capital letters. (1+1)", "M"),
W("A laboratory thermometer shows a reading from –10 °C to 110 °C. Find the total span of temperature it can measure.", 2, "110 – (–10) (1) = 120 °C (1).", "M"),
W("Find the mistake: \"Sana held the thermometer slanting and read the scale from the side while the bulb was in water.\"", 2, "The thermometer should be held vertical (1) and the eye must be in line with the top of the liquid column, not from the side (1).", "M", wp=True),
W("What is meant by the range of a thermometer? Give the range of a clinical thermometer.", 2, "Range is the lowest to the highest temperature that the thermometer can measure (1). The clinical thermometer reads about 35 °C to 42 °C (1).", "M"),
W("Why is the pulse rate not a reliable way to tell whether a person has fever?", 2, "Pulse rate also changes with other things such as running or fear, so it cannot say for sure that a person has fever. (2)", "M"),
W("Raju says, \"When water boils its temperature keeps rising, so the longer we heat, the hotter the water gets.\" Is he right?", 2, "No. The temperature of boiling water stays constant (about 100 °C at sea level) while it boils (2).", "M", wp=True),
W("Phiban and her classmates in Shillong measured boiling water and got 97.8, 98.0, 97.9, 98.0 and 98.1 °C. Give one reason why their readings are slightly different from one another. What is the difference between the highest and lowest reading?", 2, "Small differences arise from how each student reads the thermometer (bulb touching the beaker, slanting thermometer, eye not in line with the column) (1). Highest 98.1 – lowest 97.8 = 0.3 °C (1).", "M", wp=True),
W("Why are maximum and minimum air temperatures reported in weather forecasts?", 2, "They tell how hot and how cold the day will be, so people can dress and plan work accordingly. (2)", "M", wp=True),
W("Why should we never hold the thermometer by the bulb or tip, and why must experiments with boiling water be done only with a teacher?", 2, "Holding by the bulb changes its temperature and may break it (1). Boiling water can scald or burn, so a teacher must supervise (1).", "M"),
# ---------------- HARD ----------------
W("A laboratory thermometer has 5 small divisions between the big marks 0 °C and 10 °C. The liquid column stops 3 small divisions above 30 °C. Find (i) the least count (ii) the reading.", 3, "(i) 10 ÷ 5 = 2 °C per division (1). (ii) 3 × 2 = 6 °C above 30 °C (1), so reading = 36 °C (1).", "H", wp=True),
W("The table shows the temperature of a patient measured every 2 hours: 8 am – 38.6 °C, 10 am – 38.0 °C, 12 noon – 37.4 °C, 2 pm – 37.0 °C. (i) At what time did the temperature become normal? (ii) By how much did it fall in the 6 hours?", 3, "(i) At 2 pm (37.0 °C is normal) (1). (ii) 38.6 – 37.0 (1) = 1.6 °C (1).", "H", wp=True),
W("Anita read the temperature of cold water as 21 °C but her friend said that a clinical thermometer should have been used because it is more accurate. Explain why she is wrong and which thermometer is right.", 3, "A clinical thermometer only reads 35 °C to 42 °C and cannot read 21 °C (1). A laboratory thermometer (range –10 °C to 110 °C) is right for water (1) because 21 °C lies inside its range (1).", "H", wp=True),
W("Convert 37.0 °C into kelvin and give your answer using the correct unit symbol. Then convert 310.15 K back to °C and compare with normal body temperature.", 3, "37.0 + 273.15 = 310.15 K (1). 310.15 – 273.15 = 37.0 °C (1), which is the normal body temperature (1).", "H", wp=True),
W("Arrange the steps of using a digital clinical thermometer in correct order: (a) read the display (b) wash tip with soap and water (c) place it under the tongue (d) press reset (e) wait for the beep.", 3, "(b), (d), (c), (e), (a). (Washing again and recording the reading follow.) (3)", "H"),
W("Meera has a fever. Her father touches her forehead and says \"It is about 40 °C.\" Her mother measures it with a digital thermometer and gets 38.1 °C. Whose statement should the doctor trust, and why?", 3, "The thermometer reading (1). Touch is unreliable and only a feeling (1); a thermometer gives a correct and measurable value that can be recorded and compared (1).", "H", wp=True),
W("During the COVID-19 pandemic non-contact (infrared) thermometers were used at gates. Explain why they were useful.", 3, "They measure body temperature without touching the person (1), so germs cannot pass from one person to the next (1) and many people can be checked quickly (1).", "H", wp=True),
W("A student plots the temperature of melting ice with time and sees that the reading stays at 0 °C for a long time even though the beaker is on a warm table. Explain what this shows.", 3, "The temperature does not change while ice melts (1). Heat from the surroundings is used up in melting the ice (1) and only after all ice has melted does the temperature of the water start to rise (1).", "H"),
W("The chapter quotes Anna Mani: \"Wrong measurements are worse than no measurements at all.\" Explain with a school or home example.", 3, "A wrong reading can mislead us (1). For example, if a faulty thermometer shows 37 °C for a feverish child, the family may not give medicine in time (1), whereas with no reading they would at least be careful and consult a doctor (1).", "H", wp=True),
W("Compare the clinical and laboratory thermometers on four points: use, range, liquid or sensor, and the kink or digital feature.", 4, "Use: body temperature vs. other liquids and objects (1). Range: about 35 °C to 42 °C vs. –10 °C to 110 °C (1). Working: digital heat sensor (or mercury in old ones) vs. alcohol (red) or mercury in a glass tube (1). Display: digital screen, beep vs. a scale on the tube read by the top of the liquid column (1).", "H"),
W("The daily temperatures of a town in a week were (in °C): Mon 28, Tue 30, Wed 33, Thu 31, Fri 29, Sat 27, Sun 30. Find the maximum, the minimum and their difference. On which days was the temperature above 30 °C?", 4, "Maximum = 33 °C on Wednesday (1). Minimum = 27 °C on Saturday (1). Difference = 33 – 27 = 6 °C (1). Above 30 °C: only Wednesday (33) and Thursday (31) (1).", "H", wp=True),
W("Write the temperature of the following in kelvin: (i) –10 °C (ii) 100 °C. Why is the lowest possible temperature called absolute zero and what is its value in °C?", 4, "(i) –10 + 273.15 = 263.15 K (1). (ii) 100 + 273.15 = 373.15 K (1). The lowest possible temperature is 0 K (1), which is about –273.15 °C; nothing can be colder (1).", "H"),
W("A mercury thermometer breaks in a classroom. Why is it a problem? What should the students do?", 3, "Mercury is toxic and hard to dispose of (1). Students should not touch it, should move away and tell the teacher immediately (1), who will clear it safely; this is why digital thermometers are preferred (1).", "H", wp=True),
]

CH = _base()
CH["blocks"] += [
 ("h2", "7.5 Reading a Thermometer Scale: Least Count"),
 ("p", "A laboratory thermometer has long marks (labelled 0, 10, 20 ...) and short marks between them. Before using it, find three things: its **range**, its **least count** and the **unit**. The least count tells how small a change you can read."),
 ("note", "FORMULA", "Least count = (difference between two labelled marks) ÷ (number of small divisions between them)"),
 ("steps", [("Example 1 — Find the least count", "Between 20 °C and 30 °C there are 10 small divisions. Difference = 30 – 20 = 10 °C. Least count = 10 ÷ 10 = **1 °C**."),
  ("Example 2 — Reading with 5 divisions", "Between 0 °C and 10 °C there are 5 divisions. Least count = 10 ÷ 5 = **2 °C**. If the liquid stops 3 divisions after 30 °C, reading = 30 + 3 × 2 = **36 °C**."),
  ("Example 3 — Kelvin conversion", "Water at 25 °C in kelvin: K = 25 + 273.15 = **298.15 K**. Boiling water, 100 °C = **373.15 K**; melting ice, 0 °C = **273.15 K**."),
  ("Example 4 — How much above normal?", "A boy's temperature is 38.5 °C. Normal = 37.0 °C. Rise = 38.5 – 37.0 = **1.5 °C**, so he has a fever and should see a doctor."),
  ("Example 5 — Range of a thermometer", "A laboratory thermometer reads from –10 °C to 110 °C. Span = 110 – (–10) = **120 °C**. It can measure tap water (about 25 °C) and boiling water (100 °C) but a clinical thermometer cannot.")]),
 ("note", "IMPORTANT", "Always write temperature with a space and the correct symbol: **37.0 °C**, **310.15 K**. There is no degree sign with kelvin and no full stop after the symbol."),
 ("h2", "7.6 Clinical and Laboratory Thermometer: Comparison"),
 ("table", ["Point", "Clinical thermometer", "Laboratory thermometer"],
  [["Use", "Human body temperature", "Temperature of water, other liquids, air in experiments"],
   ["Range", "About 35 °C to 42 °C", "About –10 °C to 110 °C"],
   ["Modern form", "Digital with heat sensor, display and beep", "Glass tube with bulb, liquid (alcohol or mercury) and Celsius scale"],
   ["How it is read", "Number on the display after the beep", "Mark level with the top of the liquid column, eye in line"],
   ["Special care", "Reset, clean before and after use, do not hold by the tip", "Bulb must not touch the container, vertical, read while in the liquid"]]),
 ("h2", "7.7 Real-Life Situations"),
 ("ul", ["**School health check:** A teacher with a non-contact thermometer checks children at the gate; no touching means no spread of germs.",
  "**Fever at home:** A mother places a digital thermometer under the tongue of her child. A reading above 37.0 °C by about 1 °C or more suggests fever. For a small child the armpit may be used, but the reading is 0.5 °C to 1 °C lower than the real value.",
  "**Weather report:** The radio says maximum 36 °C and minimum 24 °C for the day in Jaipur. The maximum is the hottest temperature of the day (afternoon) and the minimum is the coolest (early morning).",
  "**Cooking and tea:** We use our fingers to judge hotness but a thermometer to measure it; never touch hot liquids to test them.",
  "**Science laboratory:** Students heat water and note temperature every minute. They find that the temperature stays constant while the water is boiling."]),
 ("h2", "7.8 Common Mistakes and Misconceptions"),
 ("table", ["Wrong idea", "Correct idea"],
  [["We can judge temperature correctly by touch.", "Touch is unreliable; a thermometer gives a measured value."],
   ["A clinical thermometer can measure the temperature of boiling water.", "Its range is only about 35–42 °C; use a laboratory thermometer."],
   ["The temperature of boiling water keeps increasing as we heat.", "It stays constant while water boils."],
   ["Kelvin is written as °K.", "Kelvin is written K with no degree sign."],
   ["Read the thermometer after taking it out of the water.", "Read it while the bulb is in the water, with the eye in line with the column."],
   ["Pulse rate is a sure sign of fever.", "Pulse rate is affected by many things and is not reliable."]]),
 ("note", "REMEMBER", "Normal body temperature is an **average** of many healthy persons. It varies a little with age, time of day and activity, so a reading of 37.1 °C is not a cause for worry."),
 ("h2", "7.9 Likely Questions: Higher Order"),
 ("qa", [("Why was it wrong to use a mercury thermometer in schools?", "Mercury is toxic. If the thermometer breaks, the spilled mercury is dangerous and difficult to remove, so digital thermometers are safer."),
  ("Why is the lowest temperature called absolute zero?", "Nothing can be colder than 0 K (about –273.15 °C), so it is the lowest possible temperature."),
  ("A student reads the thermometer with her eye above the top of the column. Will the reading be correct?", "No. The eye must be in line with the top of the liquid column to avoid a wrong reading."),
  ("Why is Anna Mani remembered?", "She designed and built weather-measurement instruments, reducing India's dependence on other countries, and studied wind and solar energy.")]),
]
CH["takeaways"] += ["**Least count** = difference between two labelled marks ÷ number of small divisions; check it before reading a thermometer.", "A mercury thermometer is replaced by digital and infrared ones because mercury is **toxic**."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
