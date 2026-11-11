"""Class 8 Science Ch 1 Exploring the Investigative World of Science - extras."""
from common import AR4, Q

AR = [
 AR4("In a fair test on how oil temperature affects the puffing of a puri, the thickness of the dough must be kept the same.", "Only one variable should be changed at a time while all other factors are kept constant.", "a", "Equal thickness is a controlled variable; R is the rule of a fair test."),
 AR4("A hypothesis can be tested by an experiment or observation.", "A hypothesis is a tentative, testable explanation or prediction.", "a", "R is the definition that explains why A holds."),
 AR4("A single measurement is enough to be sure of a result.", "Repeating a measurement and taking the average reduces the effect of random errors.", "d", "A is false because repeating readings improves reliability; R is true."),
 AR4("Reading a scale with the eye placed to the side of the pointer gives an incorrect value.", "This error can be removed by using a thicker scale.", "c", "A is true (parallax error); R is false: the eye must be placed directly in line with the mark."),
 AR4("A graph of the collected data can show how two variables are related.", "A table lists data in rows and columns.", "b", "Both are true, but a table's layout does not explain why a graph shows a relationship."),
 AR4("The variable that a scientist deliberately changes in an experiment is the dependent variable.", "The quantity that is measured as the outcome is the dependent variable.", "d", "The deliberately changed quantity is the independent variable, so A is false; R is true."),
]

CASE = [
 Q("<b>Case study.</b> Meera wants to know whether the amount of water in the dough changes how well a puri puffs. She makes four puris using 20 mL, 30 mL, 40 mL and 50 mL of water for the same quantity of flour, rolls them to equal thickness and fries them in oil at 180 degrees C. She measures the time each takes to puff. "
   "(i) Name the independent variable. (ii) Name the dependent variable. (iii) Name one variable that Meera has kept constant. (iv) Write a testable hypothesis for this study and explain why she should repeat the trial.",
   "(i) Amount of water in the dough (1). (ii) Time taken to puff (or degree of puffing) (1). (iii) Quantity of flour / thickness of puri / oil temperature (any one) (1). (iv) Hypothesis: puris made with more water puff in less time (or puff better) (1). Repeating trials checks for chance errors and makes the result reliable (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A student records the temperature of hot tea every 2 minutes: 0 min - 90 degrees C, 2 min - 78 degrees C, 4 min - 69 degrees C, 6 min - 62 degrees C. "
   "(i) How much did the temperature fall in the first 2 minutes? (ii) How much did it fall between 4 and 6 minutes? (iii) Which instrument measures the temperature? (iv) Does the tea cool at the same rate throughout? Justify using the data.",
   "(i) 90 - 78 = 12 degrees C (1). (ii) 69 - 62 = 7 degrees C (1). (iii) A thermometer (1). (iv) No: the fall is 12, 9 and 7 degrees C in successive 2-minute intervals, so cooling slows down as the tea gets closer to room temperature (2).", "1+1+1+2"),
 Q("<b>Case study.</b> Ravi tested whether the mass of the bob affects the time period of a simple pendulum. He used bobs of 20 g, 40 g and 60 g on a thread of the same length, and timed 20 oscillations in each case with a stopwatch. For the 20 g bob, 20 oscillations took 40 s. "
   "(i) Why was the thread kept the same length? (ii) Find the time period for the 20 g bob. (iii) Why did he time 20 oscillations instead of one? (iv) Name the independent and dependent variables.",
   "(i) Length is a controlled variable; changing it would also change the period, so the test would not be fair (1). (ii) 40 / 20 = 2 s (1). (iii) A larger time interval reduces the percentage error due to reaction time (1). (iv) Independent: mass of the bob; dependent: time period (1+1).", "1+1+1+2"),
]

FORMULAS = [
 ("Scientific method", ["Steps: observation, question, hypothesis, experiment, analysis of data, conclusion.",
   "Hypothesis: a tentative, testable explanation.", "Conclusions must be supported by data and open to revision."]),
 ("Variables and fair test", ["Independent variable: the quantity the investigator deliberately changes.",
   "Dependent variable: the quantity measured as the result.", "Controlled variables: all other factors kept constant.",
   "A fair test changes only ONE variable at a time."]),
 ("Measurement and units", ["SI unit of length: metre (m); mass: kilogram (kg); time: second (s); temperature: kelvin (K), commonly degree Celsius.",
   r"Time period $T=\dfrac{\text{total time}}{\text{number of oscillations}}$.", r"Average $=\dfrac{\text{sum of readings}}{\text{number of readings}}$.",
   "Instruments: scale, stopwatch, thermometer, measuring cylinder, spring balance."]),
 ("Errors and reliability", ["Parallax error: wrong reading because the eye is not directly in line with the mark.",
   "Repeat readings and take the mean to reduce random error.", "Record data in tables; plot graphs to see how two variables are related."]),
]

MISTAKES = [
 "Mixing up the <b>independent</b> variable (changed by you) with the <b>dependent</b> variable (measured).",
 "Changing more than one factor at a time and still calling the test fair.",
 "Writing a hypothesis as a question or an opinion instead of a testable statement.",
 "Taking a single reading and skipping repeats; forgetting to average readings.",
 "Reading a scale or thermometer from the side (parallax) and omitting units in the answer.",
 "Drawing a conclusion that the data do not support, or generalising from one trial.",
]
