"""Class 9 Science Ch 1 - Exploration: Entering the World of Secondary Science: worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import re as _re
BANK = "c9s_ch01"

# computed values used in answers
_gimli_need_l = 22300 / 0.8                  # 27875 L
_gimli_used_l = 22300 / 1.77                 # 12598.9 L
_gimli_short = _gimli_need_l - _gimli_used_l # about 15276 L
_heart = 72 * 60 * 24 * 365 * 70             # beats in 70 years

WS = [
# ------------------------------------------------------------------ EASY (17)
W("In science, a model is:", 1, "(b) a simplified representation of a system that keeps only what matters for the question being studied.", "E",
  opts=["an exact copy of the real object", "a simplified representation that keeps what matters", "a law that can never change", "a guess made without any evidence"]),
W("The SI unit of mass is the:", 1, "(c) kilogram (kg).", "E",
  opts=["gram", "tonne", "kilogram", "quintal"]),
W("The speed of light is written as c, which comes from the Latin word celeritas meaning:", 1, "(a) speed.", "E",
  opts=["speed", "light", "constant", "distance"]),
W("A statement that describes a regular pattern seen in nature, in words or as a mathematical relation, is called a:", 1, "(d) law.", "E",
  opts=["model", "hypothesis", "estimate", "law"]),
W("Meghnad Saha studied starlight by treating the matter in a star as:", 1, "(b) a hot gas, so that he could focus on temperature, pressure and the formation of ions.", "E",
  opts=["a hot solid", "a hot gas", "a cold liquid", "a collection of rocks"]),
W("In the chapter, the magnifying glass symbol on the page numbers stands for:", 1, "(c) careful observation. The compass stands for direction and purpose.", "E",
  opts=["direction and purpose", "measurement of length", "careful observation", "a scientific law"]),
W("Define a scientific model. Why do scientists deliberately leave out some details while building one?", 2,
  "A model is a simplified way of representing a real object or system that keeps only the features that matter for the question being asked (1). Leaving details out is intentional: it keeps the problem simple enough to study and answer (1).", "E"),
W("Name one model used in each of (i) physics (ii) chemistry (iii) biology.", 2,
  "(i) A moving car treated as a single point (ii) atoms drawn as spheres joined by sticks (iii) a labelled diagram of a cell showing only key parts. (3 correct = 2 marks, 2 correct = 1 mark; any valid example accepted)", "E"),
W("Differentiate between a scientific law and a scientific theory with one example of each.", 2,
  "A law describes a regular pattern in nature, e.g. Newton's laws describe the jerk felt when a bus stops suddenly (1). A theory explains why the pattern occurs on the basis of evidence, e.g. atomic theory explains how molecules form (1).", "E"),
W("True or false, with a reason: A scientific theory is just a guess.", 2,
  "False (1). A theory is an explanation built on evidence collected over a long time and on careful testing; it can change when new evidence appears (1).", "E"),
W("Why do scientists all over the world use SI units?", 2,
  "SI units are internationally agreed standards (1), so measurements can be compared and shared without confusion and mistakes caused by mixing units are avoided (1).", "E"),
W("Ritu's school is 4500 m from her home. Express this distance in kilometres.", 1,
  "4500 m = 4500 &divide; 1000 = 4.5 km. (1)", "E", wp=True),
W("A water tank in Bikaner holds 1500 litres. Express its volume in cubic metres (1 m<sup>3</sup> = 1000 L).", 2,
  "1500 L = 1500 &divide; 1000 (1) = 1.5 m<sup>3</sup> (1).", "E", wp=True),
W("A bus travels at 36 km/h. Convert this speed to m/s.", 2,
  "36 km/h = 36 &times; 5/18 (1) = 10 m/s (1).", "E", wp=True),
W("Match the term with its meaning: (a) law (b) theory (c) principle (d) model, with (1) explains why a pattern occurs (2) simplified view of a system (3) broad guiding idea (4) describes a pattern.", 2,
  "(a)&ndash;(4), (b)&ndash;(1), (c)&ndash;(3), (d)&ndash;(2). (4 correct = 2 marks, 2-3 correct = 1 mark)", "E"),
W("A student says: 'Everyday words like force and work mean the same in science as in daily life.' Is this correct? Give one example.", 2,
  "Not correct (1). In science words such as force, work or reaction have specific, precise meanings; e.g. in daily life 'work' means any effort, but in science it means force applied through a distance (1).", "E"),
W("Soham claims that the flow of a river can be studied without worrying about the colour of the water. Is he right? Explain using the idea of a model.", 2,
  "Yes (1). A model keeps only the features that matter for the question (speed, depth, width); colour does not affect the flow, so it can be ignored (1).", "E", wp=True),

# ------------------------------------------------------------------ MEDIUM (19)
W("In the model of a cricket six, which of these would you (i) keep (ii) ignore: mass of the ball, speed of the hit, brand of the bat, colour of the ball, direction of the hit, air resistance (small effect)?", 3,
  "Keep: mass of the ball, speed of the hit, direction of the hit (1). Ignore completely: brand of the bat, colour of the ball (1). Air resistance has a small effect and can be ignored in a simple model but included for a more accurate one (1).", "M", wp=True),
W("Aarav wants to find the time his cycle takes to reach home from school. List two quantities he should keep and two details he can ignore in a simple model.", 2,
  "Keep: the distance to be covered and the average speed (stops at traffic lights if they are long) (1). Ignore: colour of the cycle, the weather on one day, small changes in speed (1).", "M", wp=True),
W("Aarav's school is 3 km from his home and he cycles at an average speed of 12 km/h. Estimate the time he takes, in minutes.", 2,
  "Time = distance &divide; speed = 3 &divide; 12 (1) = 0.25 h = 15 minutes (1).", "M", wp=True),
W("The speed of a coach is 90 km/h and that of a train is 25 m/s. Convert both to the same unit and say which is faster.", 3,
  "Coach: 90 &times; 5/18 = 25 m/s (1). Train: 25 m/s = 25 &times; 18/5 = 90 km/h (1). Both have the same speed; neither is faster (1).", "M", wp=True),
W("Error analysis: Nisha converts 54 km/h into m/s by multiplying by 18/5 and writes 194.4 m/s. Find the mistake, correct it and say why her answer should have looked wrong.", 3,
  "She used the wrong factor (1). To change km/h into m/s multiply by 5/18: 54 &times; 5/18 = 15 m/s (1). 194.4 m/s is about 700 km/h, far too fast for a vehicle, so an estimate would have shown the error (1).", "M"),
W("Three students timed 20 oscillations of the same pendulum and got 36.2 s, 36.8 s, 36.5 s. (i) Find the mean time for 20 oscillations. (ii) Find the time period of one oscillation.", 3,
  "(i) Mean = (36.2 + 36.8 + 36.5) &divide; 3 = 109.5 &divide; 3 = 36.5 s (1.5). (ii) Time period = 36.5 &divide; 20 = 1.825 s (1.5).", "M", wp=True),
W("Why is the mean of repeated readings more reliable than a single reading?", 2,
  "Random errors make some readings slightly high and others slightly low (1); on taking the mean these errors partly cancel, so the result is closer to the true value (1).", "M"),
W("A medicine dose is 250 mg. Express it in (i) grams (ii) kilograms. Why do doctors need an exact value here but an approximate value is enough for estimating travel time?", 3,
  "(i) 250 mg = 0.25 g (1). (ii) 0.25 g = 0.00025 kg = 2.5 &times; 10<sup>&minus;4</sup> kg (1). A wrong dose can harm the patient, so medicine needs exact values; a rough travel time does not cause harm (1).", "M", wp=True),
W("An aircraft needs 22 300 kg of fuel. Briefly explain how a mix-up between pounds per litre and kilograms per litre can leave the aircraft short of fuel, and state the lesson.", 3,
  "The crew used the fuel density in lb/L where kg/L was needed (1). The mass converted to litres was therefore wrong and the plane loaded roughly 15 000 litres too little (1). Lesson: use SI units consistently and check units at each step (1).", "M"),
W("Classify as law, theory or principle: (i) Newton's laws of motion (ii) the atomic theory of matter (iii) conservation of energy applied while climbing stairs.", 3,
  "(i) Law: describes the pattern behind a jerk when a bus stops (1). (ii) Theory: explains how molecules are formed (1). (iii) Principle: a broad idea used to make sense of a situation (1).", "M"),
W("Error analysis: Pooja writes, 'A theory becomes a law when it has been proved enough times.' Point out the mistake.", 2,
  "A theory never turns into a law (1). A law describes a pattern; a theory explains why it occurs; they are different kinds of statements, both based on evidence, and both open to revision (1).", "M"),
W("A WhatsApp message says that food becomes harmful if cooked during an eclipse. Write two scientific questions to test the claim.", 3,
  "Any two of: What physical change does an eclipse cause to the food? (1) Is there any chemical or biological mechanism by which a shadow can harm food? (1) Has food prepared during an eclipse been tested against food prepared at other times? (1) (2 questions with clear scientific reasoning = 3 marks including a conclusion that an eclipse is only a play of shadows)", "M"),
W("Priya says: 'It will rain today because the clouds are dark.' What better questions would make this a scientific prediction?", 3,
  "Ask for measurable data and past patterns (1): What was the humidity (above 80 per cent?) when it last rained? (1) What are today's wind speed and direction and is the temperature dropping as before the last rains? (1)", "M"),
W("Why are weather forecasts reliable for a few hours or days but less certain for the distant future?", 2,
  "Weather depends on temperature, pressure, humidity and wind (1). Very small differences in these grow with time and change the outcome, so long-range forecasts become uncertain (1).", "M"),
W("A school in Jaipur has 600 students and each drinks about 1.5 litres of water per school day. Estimate the water drunk in a month of 25 school days.", 3,
  "Per day = 600 &times; 1.5 = 900 L (1). In 25 days = 900 &times; 25 = 22 500 L (1). This is an estimate because 1.5 L is an assumed average (1).", "M", wp=True),
W("An adult breathes about 15 times a minute and each breath moves about 0.5 litre of air. Estimate the volume of air breathed (i) in one hour (ii) in one day.", 3,
  "(i) 15 &times; 60 = 900 breaths in an hour; 900 &times; 0.5 = 450 L (1.5). (ii) 450 &times; 24 = 10 800 L, about 10 000 litres per day (1.5).", "M", wp=True),
W("A cheetah runs at 28 m/s and a car on a highway at 100 km/h. Which is faster and by how much, in m/s? Round to one decimal place.", 3,
  "Car speed = 100 &times; 5/18 = 27.8 m/s (1.5). Cheetah 28 m/s is faster (0.5) by 28 &minus; 27.8 = 0.2 m/s (1).", "M", wp=True),
W("Explain with an example how a failed prediction can be useful to science.", 2,
  "If the observation disagrees with the prediction, scientists re-examine their assumptions, models or measurements (1). This leads to a better model, e.g. including air resistance when a falling feather does not match a prediction made without it (1).", "M"),
W("Name two ways in which different branches of science help explain how a face mask works.", 2,
  "Physics: motion of particles and electrostatic attraction in the fibres; Chemistry: the polymer fibres of the cloth; Biology: size and behaviour of viruses; Mathematics: airflow and filtration. (any two = 2 marks)", "M", wp=True),

# ------------------------------------------------------------------ HARD (14)
W(f"A flight needs 22 300 kg of jet fuel of density 0.8 kg/L. The crew mistakenly used the density as 1.77 (a value in pounds per litre) as if it were kg/L. (i) How many litres were actually needed? (ii) How many litres did the crew load? (iii) By how much was the plane short? (iv) What does this teach about units?", 4,
  f"(i) Litres needed = 22 300 &divide; 0.8 = {_gimli_need_l:,.0f} L (1). (ii) Litres loaded = 22 300 &divide; 1.77 &asymp; {_gimli_used_l:,.0f} L (1). (iii) Shortfall = {_gimli_need_l:,.0f} &minus; {_gimli_used_l:,.0f} &asymp; {_gimli_short:,.0f} L, about 15 000 litres (1). (iv) Units must be consistent (SI); a unit mix-up can cause serious accidents (1).", "H", wp=True),
W("Estimate the number of times your heart beats in 70 years if it beats about 72 times a minute. Show each step and write the answer in the form a &times; 10<sup>n</sup>.", 3,
  f"Minutes in a year = 60 &times; 24 &times; 365 = 5 25 600 (1). In 70 years = 5 25 600 &times; 70 = 3.68 &times; 10<sup>7</sup> minutes (1). Beats = 72 &times; 3.68 &times; 10<sup>7</sup> &asymp; {_heart/1e9:.1f} &times; 10<sup>9</sup>, i.e. about 2.6 billion (1).", "H", wp=True),
W("Estimate how much cooked rice, in kg, four people need in 30 days if each needs 2000 kcal a day and 100 g of cooked rice gives about 130 kcal. Assume all energy comes from rice. Is your answer sensible?", 4,
  "Total energy = 4 &times; 2000 &times; 30 = 2 40 000 kcal (1). Energy per kg of cooked rice = 130 &times; 10 = 1300 kcal (1). Rice = 2 40 000 &divide; 1300 &asymp; 185 kg (1). It is sensible: about 6 kg per day for four people is a large but possible quantity of cooked rice; 100 g or several tonnes would have been unreasonable (1).", "H", wp=True),
W("A student estimates that a person breathes 10 lakh (1 000 000) litres of air each day. Using a classroom 8 m &times; 6 m &times; 3 m, show by estimation that this answer cannot be right.", 3,
  "Volume of classroom = 8 &times; 6 &times; 3 = 144 m<sup>3</sup> = 144 000 L (1). 10 lakh litres &divide; 1.44 lakh litres &asymp; 7 classrooms full of air in one day (1). A person breathes about 10 000 litres a day, so the answer is about 100 times too big (1).", "H", wp=True),
W("A farmer in Sikar has a rectangular field 120 m &times; 80 m. The fertiliser dose is 5 kg per 100 m<sup>2</sup>. (i) How much fertiliser is needed? (ii) If he mistakenly used the field area in square centimetres in the same formula, by what factor would his answer be wrong?", 4,
  "(i) Area = 120 &times; 80 = 9600 m<sup>2</sup> (1). Fertiliser = 9600 &divide; 100 &times; 5 = 480 kg (1). (ii) 1 m<sup>2</sup> = 10<sup>4</sup> cm<sup>2</sup> (1), so the answer would be 10 000 times too large (4 800 000 kg), absurd for one field, which shows why units must be checked (1).", "H", wp=True),
W("A model predicts that a ball hit by a batter will land 40 m away; the observed distance is 34 m. (i) Find the percentage difference. (ii) Suggest two reasons for the difference. (iii) What should scientists do next?", 4,
  "(i) (40 &minus; 34) &divide; 40 &times; 100 = 15 per cent (1). (ii) Air resistance was ignored; spin or wind, or error in the measured speed or angle of hit (any two) (2). (iii) Re-examine assumptions, add the neglected effects to the model or repeat the measurements, then test again (1).", "H"),
W("Saha treated the matter in stars as a hot gas. Explain (i) why this simplification was useful and (ii) what conclusion about the colour of stars it helped him explain.", 3,
  "(i) He needed only temperature, pressure and how atoms form ions, so he did not have to model every atom or reaction (1.5). (ii) It explained why the colour of a star is linked to its temperature (1.5).", "H"),
W("Adding more detail to a model makes it more accurate but also more complex. Using the example of a falling stone, explain when you would and would not ignore air resistance.", 3,
  "For a heavy compact stone falling a short distance, air resistance is small, so ignore it to see the basic effect of gravity (1). For a feather, a parachute or a very long fall, air resistance matters and must be added (1). Choose the level of detail that matches the question and the accuracy needed (1).", "H"),
W("Using the idea of exact versus approximate answers, decide for each whether an estimate is enough: (i) time for a bus journey (ii) dose of a medicine (iii) fuel loaded on an aircraft (iv) number of people at a fair. Give a reason for each.", 4,
  "(i) Estimate enough: delay of a few minutes does no harm (1). (ii) Exact: a wrong dose can harm (1). (iii) Exact: too little fuel risks the aircraft (1). (iv) Estimate enough: planning needs only a rough count (1).", "H"),
W("'Failure of a prediction is science's greatest strength.' Explain this statement with a suitable example.", 3,
  "Science accepts or rejects ideas on evidence, never on opinion or belief (1). If a prediction fails, the idea is tested again and improved or replaced, so errors get corrected (1). Example: a weather forecast that fails leads to better models using more data on temperature, pressure, humidity and wind (1).", "H"),
W("Seema argues: 'Since no theory is final, we should not trust science.' Write a reasoned reply of three points.", 3,
  "Theories are based on careful testing and many observations, so they are reliable within the conditions tested (1). They change only when new evidence appears, which is a sign of honest correction, not weakness (1). The alternative, belief without evidence, cannot be tested or corrected (1).", "H"),
W("Case study: Physics treats a moving car as a point, chemistry draws atoms as balls, biology draws a heart as a pump and earth science treats the Earth as a smooth sphere of layers. (i) What is common to these? (ii) Why do real problems such as climate change need several branches of science together? (iii) Name one human-made boundary in science.", 4,
  "(i) Each is a model that simplifies reality by ignoring details not needed for the question (1). (ii) Climate change involves physics (energy), chemistry (gases), biology (living things) and earth science, plus mathematics; no single branch explains all of it (2). (iii) The division into physics, chemistry, biology and earth science is human-made; nature has no such boundaries (1).", "H"),
]

_ns = {}
exec(open(REPO / "src" / "rn_work" / "c9_sci_a" / "c01.py", encoding="utf-8").read(), _ns)
CH = _ns["CH"]
_strip = lambda t: _re.sub(r"^\d+(\.\d+)*\s+", "", t)
_base = [(b[0], _strip(b[1])) + tuple(b[2:]) if b[0] in ("h2", "h3") else b for b in CH["blocks"]]
_extra = [
("h2", "Units and Conversions: a Practical Toolkit"),
("p", "Every measured quantity is a **number multiplied by a unit**. Writing the unit at every step is the easiest way to avoid errors. The SI system gives one standard unit for each quantity; other units are connected to it by fixed factors."),
("table", ["Quantity", "SI unit (symbol)", "Useful conversions"], [
 ["Length", "metre (m)", "1 km = 1000 m; 1 m = 100 cm; 1 cm = 10 mm"],
 ["Mass", "kilogram (kg)", "1 kg = 1000 g; 1 g = 1000 mg; 1 quintal = 100 kg"],
 ["Time", "second (s)", "1 min = 60 s; 1 h = 3600 s; 1 day = 86 400 s"],
 ["Speed", "metre per second (m/s)", "1 m/s = 3.6 km/h; 1 km/h = 5/18 m/s"],
 ["Volume", "cubic metre (m³)", "1 m³ = 1000 L; 1 L = 1000 mL = 1000 cm³"]]),
("note", "FORMULA", "To change **km/h → m/s** multiply by **5/18**. To change **m/s → km/h** multiply by **18/5**. Quick check: 36 km/h = 10 m/s; 72 km/h = 20 m/s."),
("steps", [("Example 1 — A bus and a train", "A bus runs at 90 km/h; a train at 25 m/s. **Step 1:** bring both to m/s: 90 × 5/18 = 25 m/s. **Step 2:** compare: 25 m/s = 25 m/s. **Answer:** both have the same speed."),
 ("Example 2 — Time to reach school", "Distance 3 km, average speed 12 km/h. **Step 1:** write the relation: time = distance ÷ speed. **Step 2:** substitute with units: 3 km ÷ 12 km/h = 0.25 h. **Step 3:** convert: 0.25 × 60 = **15 minutes**."),
 ("Example 3 — Mean of repeated readings", "Pendulum time for 20 oscillations: 36.2 s, 36.8 s, 36.5 s. **Step 1:** mean = (36.2 + 36.8 + 36.5) ÷ 3 = 36.5 s. **Step 2:** time period = 36.5 ÷ 20 = **1.825 s**. Taking a mean reduces the effect of random errors.")]),
("note", "REMEMBER", "**Do not mix units.** The aircraft fuel incident happened because pounds per litre were used where kilograms per litre were needed. Convert everything to SI units **before** you substitute."),

("h2", "Estimation Step by Step"),
("p", "An estimate is a **reasoned approximate answer**. It is not careless: you choose sensible numbers, state your assumptions and check that the result is the right size. Scientists also use estimates to catch calculation errors before they matter."),
("steps", [("Example 4 — Heartbeats in a lifetime", "Assume 72 beats a minute. **Step 1:** minutes in a year = 60 × 24 × 365 = 5 25 600. **Step 2:** minutes in 70 years ≈ 3.7 × 10⁷. **Step 3:** beats ≈ 72 × 3.7 × 10⁷ ≈ **2.6 × 10⁹**, about 2.6 billion."),
 ("Example 5 — Is 10 lakh litres of air a day possible?", "Classroom volume = 8 × 6 × 3 = 144 m³ = 1 44 000 L. A claim of 10 lakh litres is about 7 classrooms full of air breathed by one person in a day. This is far above the estimate of about 10 000 litres, so the claim is **unreasonable**."),
 ("Example 6 — Water for a school", "600 students × 1.5 L a day × 25 school days = **22 500 L** a month. The number 1.5 L is an assumed average, so the answer is an estimate.")]),
("table", ["When an estimate is enough", "When an exact value is needed"], [
 ["Travel time of a journey", "Dose of a medicine"], ["Crowd at a fair", "Fuel loaded on an aircraft"], ["Water used by a school", "Amount of a chemical in a reaction in the laboratory"]]),

("h2", "Models, Predictions and Testing: Worked Reasoning"),
("p", "A model gives a prediction; an experiment gives an observation. Science advances through the **match or mismatch** between the two."),
("table", ["Stage", "What is done", "Example"], [
 ["1. Build a model", "Choose what to keep and what to ignore", "A cricket ball treated with mass, speed and direction only"],
 ["2. Predict", "Use the model to expect a result", "The ball will land 40 m away"],
 ["3. Observe", "Measure the real outcome", "The ball landed 34 m away"],
 ["4. Compare", "Find the difference: (40 − 34) ÷ 40 × 100 = 15 per cent", "The model is only fairly good"],
 ["5. Revise", "Re-check measurements and add ignored effects", "Include air resistance and spin"]]),
("note", "IMPORTANT", "A mismatch does **not** mean science has failed. It shows exactly where the model or the assumptions need improvement."),
("h3", "Aircraft fuel: the numbers"),
("p", "A flight needed 22 300 kg of fuel of density 0.8 kg/L, i.e. 22 300 ÷ 0.8 = **27 875 L**. The crew divided by 1.77 (the density in pounds per litre) and loaded about 12 600 L. The shortfall was about **15 000 L**. One wrong unit changed the answer by more than half."),

("h2", "Common Mistakes and Misconceptions"),
("note", "REMEMBER", "**A theory is not a guess.** It is a well-tested explanation. A **law does not outrank a theory**: they do different jobs (pattern versus explanation)."),
("note", "REMEMBER", "**A model is not a lie.** It is deliberately simple. Judge it by whether it helps answer the question, not by whether it looks real."),
("ul", ["Do not write a bare number. Always write the **unit**; marks are lost without it.",
 "Do not multiply by 18/5 when converting km/h to m/s. Use **5/18**, and check that the answer is smaller than the km/h value.",
 "Estimating is not guessing. State your **assumptions** and check the size of your answer.",
 "Scientific words (force, work, reaction) have **precise** meanings that differ from everyday use.",
 "A failed prediction does not prove the whole theory wrong; first re-check the measurements, assumptions and model."]),
]
CH["blocks"] = _base[:-2] + _extra + _base[-2:]

if __name__ == "__main__": run(__file__, BANK, 9, "Science", WS, CH)
