"""Class 7 Science Ch 7 Measurement of Time and Motion - extras."""
from common import AR4, Q

AR = [
 AR4("The SI unit of time is the second.", "One minute is equal to 60 seconds.", "b",
     "Both are true, but the relation between minute and second does not explain why the second is the SI unit."),
 AR4("The time period of a simple pendulum increases when its length is increased.", "A longer pendulum takes more time to complete one oscillation.", "a",
     "R restates the effect of length on the time period and explains A."),
 AR4("A car that travels 90 km in 2 hours has a speed of 45 km/h.", "Speed is equal to distance multiplied by time.", "c",
     "$90/2=45$ km/h so A is true; speed = distance / time, so R is false."),
 AR4("A speed of 36 km/h is the same as 36 m/s.", "1 km/h is equal to $\\dfrac{5}{18}$ m/s.", "d",
     "$36\\times\\dfrac{5}{18}=10$ m/s, so A is false; R is true."),
 AR4("A straight line sloping upward through the origin in a distance-time graph shows uniform speed.", "Equal distances are covered in equal intervals of time.", "a",
     "A straight line means the distance grows equally in equal times, which is uniform speed."),
 AR4("An odometer measures the distance travelled by a vehicle.", "A speedometer measures the speed of a vehicle.", "b",
     "Both are true, but they are different instruments and neither explains the other."),
]

CASE = [
 Q("<b>Case study.</b> Kavya makes a simple pendulum using a stone tied to a 1 m thread. She counts 30 complete oscillations in 60 seconds. Later, she makes a longer pendulum and finds it takes 50 seconds for 20 oscillations. "
   "(i) Find the time period of the first pendulum. (ii) Does the time period depend on the mass of the bob? (iii) Find the time period of the longer pendulum. (iv) Which pendulum is longer, and how do you know?",
   "(i) $60/30=2$ s (1). (ii) No, it does not (1). (iii) $50/20=2.5$ s (1). (iv) The second pendulum is longer (1), because a longer pendulum has a larger time period (2.5 s is greater than 2 s) (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A train from Nagpur travels 144 km in 2 hours at a steady speed. A student, Imran, is asked some questions about its motion. "
   "(i) Find the speed of the train in km/h. (ii) Convert this speed into m/s. (iii) How far will it go in 3.5 hours at the same speed? (iv) How much time will it take to cover 360 km at the same speed? State the assumption you make.",
   "(i) $144/2=72$ km/h (1). (ii) $72\\times\\dfrac{5}{18}=20$ m/s (1). (iii) $72\\times3.5=252$ km (1). (iv) $360/72=5$ hours (1); the train is assumed to move with the same (uniform) speed throughout (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Rohan cycles to the market. He covers 4 km in the first 20 minutes, stops at a shop for 10 minutes, and then covers the remaining 6 km in the next 20 minutes. His sister draws a distance-time graph of his journey. "
   "(i) Find his speed in the first 20 minutes in km/h. (ii) What will the graph look like during the 10-minute halt? (iii) Find his speed in the last 20 minutes in km/h. (iv) Find his average speed for the whole journey.",
   "(i) $4\\text{ km}/\\dfrac{1}{3}\\text{ h}=12$ km/h (1). (ii) A horizontal line, as the distance does not change (1). (iii) $6\\text{ km}/\\dfrac{1}{3}\\text{ h}=18$ km/h (1). (iv) Total distance 10 km, total time 50 min $=\\dfrac{5}{6}$ h (1); average speed $=10\\div\\dfrac56=12$ km/h (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Units of time", [
   "SI unit of time: second (s). 1 minute = 60 s; 1 hour = 60 minutes = 3600 s; 1 day = 24 hours.",
   "Old time-measuring devices: sundial (shadow), water clock, sand clock; modern: quartz clocks and watches."]),
 ("Oscillation and time period of a pendulum", [
   "Oscillation: one complete to-and-fro motion of the bob back to its starting position.",
   "Time period $=\\dfrac{\\text{total time}}{\\text{number of oscillations}}$.",
   "Time period of a simple pendulum depends on its length (longer pendulum, larger period); it does not depend on the mass of the bob."]),
 ("Speed", [
   "Speed $=\\dfrac{\\text{distance}}{\\text{time}}$; distance = speed $\\times$ time; time = distance $\\div$ speed.",
   "SI unit: metre per second (m/s); also km/h. 1 km/h $=\\dfrac{5}{18}$ m/s; 1 m/s $=3.6$ km/h.",
   "Average speed $=\\dfrac{\\text{total distance}}{\\text{total time}}$."]),
 ("Types of motion and graphs", [
   "Uniform motion: equal distances in equal times; non-uniform: unequal distances in equal times.",
   "Periodic motion repeats at regular intervals (pendulum, swing, Earth's rotation).",
   "Distance-time graph: straight slanting line = uniform speed; horizontal line = at rest; steeper line = greater speed.",
   "Odometer measures distance travelled; speedometer shows speed of a vehicle."]),
]

MISTAKES = [
 "Dividing time by the number of oscillations the wrong way; time period $=$ <b>total time $\\div$ number of oscillations</b>.",
 "Writing that a heavier bob has a larger time period; the period depends on <b>length</b>, not on mass.",
 "Forgetting to convert units before calculating (minutes to hours, km/h to m/s).",
 "Using $\\times\\dfrac{18}{5}$ instead of $\\times\\dfrac{5}{18}$ when converting km/h to m/s.",
 "Calculating average speed as the average of two speeds instead of <i>total distance divided by total time</i>.",
 "Reading a horizontal line on a distance-time graph as 'moving fast'; it means the object is <b>at rest</b>.",
]
