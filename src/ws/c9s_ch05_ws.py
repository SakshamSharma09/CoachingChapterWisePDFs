"""Class 9 Science Ch 5 Describing Motion Around Us: worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import re as _re
BANK = "c9s_ch05"

# computed values (g = 10 m s^-2 wherever free fall is used)
_a1, _t1 = 1.5, 8
_v1, _s1 = _a1 * _t1, 0.5 * _a1 * _t1 ** 2                       # 12 m/s, 48 m
_a2 = (0 - 12 ** 2) / (2 * 24); _t2 = 12 / abs(_a2)               # -3, 4
_sA, _sB = 10 ** 2 / (2 * 5), 20 ** 2 / (2 * 5)                   # 10 m, 40 m
_T4 = (2 * 80 / 10) ** 0.5; _V4 = 10 * _T4                        # 4 s, 40 m/s
_h5 = 20 ** 2 / (2 * 10)                                          # 20 m
_avg8 = 130 / (65 / 50 + 65 / 65)                                 # 56.5 km/h
_s17 = (0 - 20 ** 2) / (2 * (-0.5))                               # 400 m
assert (_v1, _s1, _a2, _t2, _sA, _sB, _T4, _V4, _h5) == (12, 48, -3, 4, 10, 40, 4, 40, 20) and round(_avg8, 1) == 56.5 and _s17 == 400

WS = [
# ------------------------------------------------------------------ EASY (17)
W("The SI unit of acceleration is:", 1, "(c) m s<sup>&minus;2</sup>.", "E",
  opts=["m s<sup>&minus;1</sup>", "m<sup>2</sup> s<sup>&minus;1</sup>", "m s<sup>&minus;2</sup>", "km h<sup>&minus;1</sup>"]),
W("A speed of 72 km h<sup>&minus;1</sup> is equal to:", 1, "(b) 20 m s<sup>&minus;1</sup> (72 &times; 5/18).", "E",
  opts=["10 m s<sup>&minus;1</sup>", "20 m s<sup>&minus;1</sup>", "72 m s<sup>&minus;1</sup>", "259 m s<sup>&minus;1</sup>"]),
W("The slope of a position-time graph gives:", 1, "(a) velocity.", "E",
  opts=["velocity", "acceleration", "distance", "displacement"]),
W("A child on a circular track of radius 7 m runs half a revolution. Taking &pi; = 22/7, the distance and the magnitude of displacement are:", 1,
  "(d) 22 m and 14 m. Distance = &pi;R = 22 m; displacement = diameter = 14 m.", "E",
  opts=["14 m and 22 m", "44 m and 0", "22 m and 22 m", "22 m and 14 m"]),
W("The area under a velocity-time graph gives:", 1, "(b) displacement.", "E",
  opts=["acceleration", "displacement", "average speed", "time"]),
W("In uniform circular motion the velocity of the body at any point is directed:", 1, "(c) along the tangent to the circle at that point, in the direction of motion.", "E",
  opts=["towards the centre", "away from the centre", "along the tangent", "along the radius outward"]),
W("Rahul walks 80 m east from his home to a shop, then 30 m back towards home. Find the distance travelled and the displacement.", 2,
  "Distance = 80 + 30 = 110 m (1). Displacement = 80 &minus; 30 = 50 m towards the east (1).", "E", wp=True),
W("A bus covers 150 km in 3 hours. Find its average speed in km h<sup>&minus;1</sup> and in m s<sup>&minus;1</sup>.", 2,
  "Average speed = 150 &divide; 3 = 50 km h<sup>&minus;1</sup> (1). In m s<sup>&minus;1</sup>: 50 &times; 5/18 = 13.9 m s<sup>&minus;1</sup> (1).", "E", wp=True),
W("A car starts from rest and reaches 20 m s<sup>&minus;1</sup> in 5 s. Find its acceleration.", 2,
  "a = (v &minus; u)/t = (20 &minus; 0)/5 (1) = 4 m s<sup>&minus;2</sup> (1).", "E", wp=True),
W("Ria is cycling at 10 m s<sup>&minus;1</sup> and brakes to a stop in 5 s. Find the acceleration and state what the sign means.", 2,
  "a = (0 &minus; 10)/5 = &minus;2 m s<sup>&minus;2</sup> (1). The negative sign shows the acceleration is opposite to the velocity, i.e. retardation (1).", "E", wp=True),
W("True or false, with a reason: A bus moving at a steady 100 km h<sup>&minus;1</sup> along a straight road has a large acceleration.", 2,
  "False (1). Acceleration depends on how quickly velocity changes, not on how large it is; constant velocity means zero acceleration (1).", "E"),
W("Define (i) uniform motion (ii) non-uniform motion.", 2,
  "(i) Uniform motion: equal distances are covered in equal intervals of time (constant speed) (1). (ii) Non-uniform motion: unequal distances are covered in equal intervals of time (1).", "E"),
W("A train moves at a constant velocity of 20 m s<sup>&minus;1</sup> for 6 s. Draw (in words) its velocity-time graph and find the displacement from the graph.", 2,
  "The graph is a horizontal straight line at 20 m s<sup>&minus;1</sup> (1). Displacement = area of the rectangle = 20 &times; 6 = 120 m (1).", "E", wp=True),
W("What does a straight line parallel to the time axis mean in (i) a position-time graph (ii) a velocity-time graph?", 2,
  "(i) The object is at rest, its position does not change (1). (ii) The object moves with constant velocity and its acceleration is zero (1).", "E"),
W("Classify as scalar or vector: distance, displacement, speed, velocity, acceleration, time.", 2,
  "Scalars: distance, speed, time. Vectors: displacement, velocity, acceleration. (6 correct = 2 marks, 4-5 correct = 1 mark)", "E"),
W("Convert (i) 54 km h<sup>&minus;1</sup> to m s<sup>&minus;1</sup> (ii) 5 m s<sup>&minus;1</sup> to km h<sup>&minus;1</sup>.", 2,
  "(i) 54 &times; 5/18 = 15 m s<sup>&minus;1</sup> (1). (ii) 5 &times; 18/5 = 18 km h<sup>&minus;1</sup> (1).", "E"),
W("Sarang swims to the far end of a 25 m pool and back in 50 s. Find his average speed and average velocity.", 2,
  "Distance = 50 m, so average speed = 50/50 = 1 m s<sup>&minus;1</sup> (1). Displacement = 0, so average velocity = 0 (1).", "E", wp=True),

# ------------------------------------------------------------------ MEDIUM (19)
W(f"A scooter starts from rest and moves with a constant acceleration of {_a1} m s<sup>&minus;2</sup> for {_t1} s. Find (i) its final velocity (ii) the distance covered.", 3,
  f"(i) v = u + at = 0 + {_a1} &times; {_t1} = {_v1:g} m s<sup>&minus;1</sup> (1.5). (ii) s = ut + &frac12;at<sup>2</sup> = &frac12; &times; {_a1} &times; {_t1}<sup>2</sup> = {_s1:g} m (1.5).", "M", wp=True),
W("A car moving at 12 m s<sup>&minus;1</sup> is brought to rest in 24 m on a village road. Find the (uniform) retardation and the time taken to stop.", 3,
  f"v<sup>2</sup> = u<sup>2</sup> + 2as gives 0 = 144 + 2a(24), so a = &minus;3 m s<sup>&minus;2</sup> (1.5). Time t = (v &minus; u)/a = (0 &minus; 12)/(&minus;3) = 4 s (1.5).", "M", wp=True),
W("A vehicle can brake with a retardation of 5 m s<sup>&minus;2</sup>. Find its braking distance from (i) 36 km h<sup>&minus;1</sup> (ii) 72 km h<sup>&minus;1</sup>. What do you notice?", 3,
  f"(i) u = 10 m s<sup>&minus;1</sup>: s = u<sup>2</sup>/2a = 100/10 = {_sA:g} m (1). (ii) u = 20 m s<sup>&minus;1</sup>: s = 400/10 = {_sB:g} m (1). Doubling the speed makes the braking distance four times (1).", "M", wp=True),
W("A stone is dropped from the top of an 80 m tower. Taking g = 10 m s<sup>&minus;2</sup>, find the time taken to reach the ground and the speed with which it hits.", 3,
  f"s = &frac12;gt<sup>2</sup>: 80 = 5t<sup>2</sup>, so t = {_T4:g} s (1.5). v = gt = 10 &times; {_T4:g} = {_V4:g} m s<sup>&minus;1</sup> (1.5).", "M", wp=True),
W("A cricketer throws a ball vertically upwards at 20 m s<sup>&minus;1</sup>. Taking g = 10 m s<sup>&minus;2</sup>, find the time to reach the highest point and the maximum height.", 3,
  f"At the top v = 0: t = (v &minus; u)/a = (0 &minus; 20)/(&minus;10) = 2 s (1.5). Height = u<sup>2</sup>/2g = 400/20 = {_h5:g} m (1.5).", "M", wp=True),
W("The position of an object is noted every 2 s: t = 0, 2, 4, 6, 8 s; x = 0, 10, 20, 20, 20 m. Find the velocity in (i) 0 to 4 s (ii) 4 s to 8 s and describe the motion.", 3,
  "(i) v = (20 &minus; 0)/4 = 5 m s<sup>&minus;1</sup> (1). (ii) v = 0 (1). The object moves with constant velocity 5 m s<sup>&minus;1</sup> for 4 s and then stays at rest at x = 20 m (1).", "M"),
W("On a position-time graph of a scooter, the points (2 s, 30 m) and (6 s, 90 m) lie on a straight line. Find its velocity from the slope.", 2,
  "Slope = (90 &minus; 30)/(6 &minus; 2) = 60/4 (1) = 15 m s<sup>&minus;1</sup> (1).", "M", wp=True),
W(f"A bus goes from Jaipur to Ajmer, 130 km apart. It covers the first 65 km at 50 km h<sup>&minus;1</sup> and the next 65 km at 65 km h<sup>&minus;1</sup>. Find the average speed for the whole journey. Is it equal to the mean of 50 and 65?", 3,
  f"Time = 65/50 + 65/65 = 1.3 + 1 = 2.3 h (1). Average speed = 130/2.3 &asymp; {_avg8:.1f} km h<sup>&minus;1</sup> (1). The mean of 50 and 65 is 57.5, which is not the same, because the times for the two halves are unequal (1).", "M", wp=True),
W("Error analysis: Farhan says, 'At the top of its path a ball thrown upwards has zero velocity, so its acceleration there is also zero.' Is he correct?", 2,
  "No (1). The acceleration is g = 10 m s<sup>&minus;2</sup> downward throughout the motion, including at the top, where the velocity is only instantaneously zero (1).", "M"),
W("A runner completes one lap of a circular track of radius 35 m in 55 s. Taking &pi; = 22/7, find the distance covered, the displacement, the average speed and the average velocity for one lap.", 3,
  "Distance = 2&pi;R = 2 &times; 22/7 &times; 35 = 220 m (1). Displacement = 0 (0.5). Average speed = 220/55 = 4 m s<sup>&minus;1</sup> (1). Average velocity = 0 (0.5).", "M", wp=True),
W("Why is uniform circular motion an accelerated motion although the speed is constant?", 3,
  "Velocity has both magnitude and direction (1). In circular motion the direction of the velocity changes continuously (1), and a change in velocity, whether in magnitude or direction, means acceleration (1).", "M"),
W("In an activity a marble rolls along the inside of a ring on a table. When the ring is lifted, in what direction does the marble leave and why?", 2,
  "It moves in a straight line along the tangent to the circle at the point of release (1), because the velocity at any point on a circle is along the tangent, and with no ring to turn it, it keeps that direction (1).", "M"),
W("A scooter speeds up from 18 km h<sup>&minus;1</sup> to 72 km h<sup>&minus;1</sup> in 15 s. Find its acceleration in m s<sup>&minus;2</sup>.", 2,
  "u = 5 m s<sup>&minus;1</sup>, v = 20 m s<sup>&minus;1</sup> (1). a = (20 &minus; 5)/15 = 1 m s<sup>&minus;2</sup> (1).", "M", wp=True),
W("Using the first two kinematic equations derive v<sup>2</sup> = u<sup>2</sup> + 2as.", 3,
  "From v = u + at, t = (v &minus; u)/a (1). Substitute in s = ut + &frac12;at<sup>2</sup>: s = u(v &minus; u)/a + (v &minus; u)<sup>2</sup>/2a (1). Simplify: 2as = 2u(v &minus; u) + (v &minus; u)<sup>2</sup> = v<sup>2</sup> &minus; u<sup>2</sup>, so v<sup>2</sup> = u<sup>2</sup> + 2as (1).", "M"),
W("A freely falling object has velocities 10, 20 and 30 m s<sup>&minus;1</sup> at 1 s, 2 s and 3 s after release. Find its acceleration and name the quantity.", 2,
  "Velocity changes by 10 m s<sup>&minus;1</sup> every second, so a = 10 m s<sup>&minus;2</sup> (1). This is the acceleration due to gravity g, directed downwards (1).", "M"),
W("Describe the motion shown by (i) a straight line rising in a v-t graph (ii) a straight line falling in a v-t graph (iii) a curve getting steeper in an x-t graph.", 3,
  "(i) Velocity increases uniformly, constant positive acceleration (1). (ii) Velocity decreases uniformly, constant negative acceleration (retardation) (1). (iii) Velocity is increasing, i.e. the body is accelerating (1).", "M"),
W(f"A train running at 72 km h<sup>&minus;1</sup> applies brakes and stops uniformly in 40 s. Find the retardation and the distance travelled while stopping.", 3,
  f"u = 20 m s<sup>&minus;1</sup>, v = 0, t = 40 s: a = (0 &minus; 20)/40 = &minus;0.5 m s<sup>&minus;2</sup> (1.5). s = ut + &frac12;at<sup>2</sup> = 800 &minus; 400 = {_s17:g} m (1.5).", "M", wp=True),
W("A cycle slows from 36 km h<sup>&minus;1</sup> to rest in 4 s; a car slows from 72 km h<sup>&minus;1</sup> to rest in 10 s. Which one has the larger retardation?", 3,
  "Cycle: a = (0 &minus; 10)/4 = &minus;2.5 m s<sup>&minus;2</sup> (1). Car: a = (0 &minus; 20)/10 = &minus;2 m s<sup>&minus;2</sup> (1). The cycle has the larger retardation although its speed is less (1).", "M", wp=True),

# ------------------------------------------------------------------ HARD (14)
W("The velocity-time data of a cyclist: t = 0 s, v = 0; t = 4 s, v = 8 m s<sup>&minus;1</sup>; t = 10 s, v = 8 m s<sup>&minus;1</sup>; t = 14 s, v = 0, with straight lines between the points. Find (i) the acceleration in each phase (ii) the total distance covered.", 4,
  "(i) 0-4 s: (8 &minus; 0)/4 = 2 m s<sup>&minus;2</sup>; 4-10 s: 0; 10-14 s: (0 &minus; 8)/4 = &minus;2 m s<sup>&minus;2</sup> (1.5). (ii) Areas: &frac12; &times; 4 &times; 8 = 16 m; 6 &times; 8 = 48 m; &frac12; &times; 4 &times; 8 = 16 m (1.5). Total = 80 m (1).", "H", wp=True),
W("A truck driver sees an obstacle 50 m ahead while moving at 72 km h<sup>&minus;1</sup>. His reaction time is 0.6 s and the brakes give a retardation of 5 m s<sup>&minus;2</sup>. Will the truck stop before the obstacle? Find the total stopping distance.", 4,
  "u = 20 m s<sup>&minus;1</sup>. Distance in reaction time = 20 &times; 0.6 = 12 m (1). Braking distance = u<sup>2</sup>/2a = 400/10 = 40 m (1.5). Total = 52 m, which is more than 50 m (1), so the truck hits the obstacle (0.5).", "H", wp=True),
W("A car goes from A to B at 40 km h<sup>&minus;1</sup> and returns along the same road at 60 km h<sup>&minus;1</sup>. Find the average speed and the average velocity for the round trip. Why is the average speed not 50 km h<sup>&minus;1</sup>?", 3,
  "Let AB = d: time = d/40 + d/60 = d/24; total distance 2d, so average speed = 2d &divide; (d/24) = 48 km h<sup>&minus;1</sup> (1.5). Displacement = 0, so average velocity = 0 (0.5). The car spends more time at the lower speed, so the average is not the simple mean (1).", "H"),
W("A car accelerates uniformly from rest to 15 m s<sup>&minus;1</sup> in 5 s, then moves at 15 m s<sup>&minus;1</sup> for 12 s, and then stops uniformly in 5 s. Find the total distance and the average speed for the whole journey.", 4,
  "Phase areas: &frac12; &times; 5 &times; 15 = 37.5 m; 15 &times; 12 = 180 m; &frac12; &times; 5 &times; 15 = 37.5 m (2). Total distance = 255 m (1). Total time = 22 s, so average speed = 255/22 = 11.6 m s<sup>&minus;1</sup> (1).", "H", wp=True),
W("Two cars, 120 m apart on a straight road, move towards each other at constant speeds of 15 m s<sup>&minus;1</sup> and 10 m s<sup>&minus;1</sup>. After how many seconds do they meet and how far from the first car's starting point?", 3,
  "Relative speed = 15 + 10 = 25 m s<sup>&minus;1</sup> (1). Time = 120/25 = 4.8 s (1). Distance from the first car = 15 &times; 4.8 = 72 m (1).", "H", wp=True),
W("A thief on a motorcycle is 64 m ahead of a police jeep and moves at a constant 12 m s<sup>&minus;1</sup>. The jeep starts from rest at the same instant with a constant acceleration of 2 m s<sup>&minus;2</sup>. Find the time taken to catch the thief, the distance covered by the jeep and its speed at that instant.", 5,
  "Jeep: s = &frac12; &times; 2 &times; t<sup>2</sup> = t<sup>2</sup> (1). Thief: s = 64 + 12t (1). Equate: t<sup>2</sup> &minus; 12t &minus; 64 = 0, so (t &minus; 16)(t + 4) = 0, t = 16 s (1.5). Jeep distance = 16<sup>2</sup> = 256 m (1). Speed = at = 2 &times; 16 = 32 m s<sup>&minus;1</sup> (0.5).", "H", wp=True),
W("A ball is thrown vertically downwards at 10 m s<sup>&minus;1</sup> from a roof 75 m above the ground. Taking g = 10 m s<sup>&minus;2</sup>, find the time to reach the ground and the speed on reaching it.", 4,
  "75 = 10t + 5t<sup>2</sup>, so t<sup>2</sup> + 2t &minus; 15 = 0, (t + 5)(t &minus; 3) = 0 (1.5); t = 3 s (0.5). v = u + gt = 10 + 30 = 40 m s<sup>&minus;1</sup> (1). Check: v<sup>2</sup> = 100 + 2 &times; 10 &times; 75 = 1600 (1).", "H", wp=True),
W("A ball is thrown vertically upwards at 30 m s<sup>&minus;1</sup> (g = 10 m s<sup>&minus;2</sup>). Find (i) the time to reach the top (ii) the maximum height (iii) the total time to return to the thrower's hand (iv) the total distance and displacement for the whole flight.", 4,
  "(i) t = 30/10 = 3 s (1). (ii) H = 900/20 = 45 m (1). (iii) 2 &times; 3 = 6 s (1). (iv) Distance = 45 + 45 = 90 m; displacement = 0 (1).", "H", wp=True),
W("The tip of the 14 cm long second hand of a wall clock moves from 12 to 6 in 30 s. Taking &pi; = 22/7, find the distance covered, the magnitude of the displacement, the average speed and the magnitude of the average velocity.", 4,
  "Half revolution: distance = &pi;R = 22/7 &times; 14 = 44 cm (1). Displacement = diameter = 28 cm (1). Speed = 44/30 = 1.47 cm s<sup>&minus;1</sup> (1). Velocity = 28/30 = 0.93 cm s<sup>&minus;1</sup> (1).", "H", wp=True),
W("A merry-go-round at a fair in Pushkar has a radius of 3.5 m and makes 10 complete revolutions in one minute. Take &pi; = 22/7. Find the speed of a child sitting at its rim and the child's displacement after one minute. Is the child's motion uniform circular motion? Explain.", 3,
  "Circumference = 2 &times; 22/7 &times; 3.5 = 22 m; in 10 revolutions distance = 220 m, so speed = 220/60 = 3.67 m s<sup>&minus;1</sup> (1.5). After 10 full revolutions the child is back at the start: displacement = 0 (0.5). Yes, the speed is constant but the direction of velocity keeps changing, so it is uniform circular motion (1).", "H", wp=True),
W("Two cyclists A and B start along a straight road. A starts from the origin at t = 0 and moves at 10 m s<sup>&minus;1</sup>. B is 30 m ahead of the origin at t = 0 and moves at 5 m s<sup>&minus;1</sup> in the same direction. (i) Write the position-time equation of each. (ii) Find when and where A overtakes B. (iii) Describe the two x-t lines.", 4,
  "(i) x<sub>A</sub> = 10t; x<sub>B</sub> = 30 + 5t (1). (ii) 10t = 30 + 5t gives t = 6 s; x = 60 m (1.5). (iii) Both are straight lines; A's line starts at the origin and is steeper, B's starts at 30 m with a smaller slope, and they cross at (6 s, 60 m) (1.5).", "H", wp=True),
W("Can a body have zero velocity and non-zero acceleration at the same instant? Can a body have constant speed and non-zero acceleration? Give one example of each.", 3,
  "Yes to both (1). Zero velocity with acceleration: a ball thrown upwards at its highest point (v = 0, a = g downward) (1). Constant speed with acceleration: a body in uniform circular motion, since its direction changes (1).", "H"),
W("Assertion (A): The stopping distance of a vehicle at 100 km h<sup>&minus;1</sup> is about four times that at 50 km h<sup>&minus;1</sup>. Reason (R): For the same retardation, stopping distance is proportional to the square of the initial speed. Are A and R true and does R explain A? Support with a short calculation using a = 4 m s<sup>&minus;2</sup>.", 3,
  "A and R are both true and R explains A (1). Using s = u<sup>2</sup>/2a: at 50 km h<sup>&minus;1</sup> = 13.9 m s<sup>&minus;1</sup>, s = 193/8 &asymp; 24 m; at 100 km h<sup>&minus;1</sup> = 27.8 m s<sup>&minus;1</sup>, s = 772/8 &asymp; 96 m (1.5), which is four times (0.5).", "H"),
W("Using a velocity-time graph for a body moving with uniform acceleration from velocity u to v in time t, derive s = ut + &frac12;at<sup>2</sup>.", 3,
  "The graph is a straight line from (0, u) to (t, v) (0.5). Displacement = area under the graph = rectangle (u &times; t) + triangle (&frac12; &times; t &times; (v &minus; u)) (1.5). Since v &minus; u = at, s = ut + &frac12;at<sup>2</sup> (1).", "H"),
]

_ns = {}
exec(open(REPO / "src" / "rn_work" / "c9_sci_a" / "c05.py", encoding="utf-8").read(), _ns)
CH = _ns["CH"]
_strip = lambda t: _re.sub(r"^\d+(\.\d+)*\s+", "", t)
_base = [(b[0], _strip(b[1])) + tuple(b[2:]) if b[0] in ("h2", "h3") else b for b in CH["blocks"]]
_extra = [
("h2", "Problem-Solving Method for Motion Numericals"),
("p", "Use the same five steps every time. They prevent the most common errors: wrong units, wrong sign and wrong equation."),
("steps", [("Step 1 — Draw and choose", "Sketch the situation. Choose the origin and the positive direction and keep them for the whole problem."),
 ("Step 2 — List the data with signs and SI units", "Write u, v, a, s, t. Convert km h⁻¹ to m s⁻¹ (× 5/18). Retardation is **negative**. 'Starts from rest' means u = 0; 'stops' means v = 0; at the top of a throw v = 0."),
 ("Step 3 — Pick the equation that has the three known quantities and the unknown", "No s given → v = u + at. No v → s = ut + ½at². No t → v² = u² + 2as."),
 ("Step 4 — Substitute with units and solve", "Write every number with its unit and check the unit of the answer."),
 ("Step 5 — Check", "Is the size sensible? Is the sign sensible? Does the answer agree with a quick v–t area?")]),
("table", ["Situation", "Data to use", "Equation"], [
 ["Starts from rest, uniform a, time t", "u = 0", "v = at; s = ½at²"],
 ["Brakes to a stop in distance s", "v = 0, a negative", "0 = u² + 2as → s = u²/2|a|"],
 ["Free fall from rest", "u = 0, a = g = 10 m s⁻² down", "v = gt; h = ½gt²"],
 ["Thrown up", "v = 0 at top, a = −g", "t = u/g; H = u²/2g"],
 ["Round trip or full lap", "displacement = 0", "average velocity = 0; speed = distance ÷ time"]]),

("h2", "Worked Examples"),
("steps", [("Example 1 — Scooter from rest", "a = 1.5 m s⁻², t = 8 s. **v** = 0 + 1.5 × 8 = **12 m s⁻¹**. **s** = ½ × 1.5 × 8² = **48 m**."),
 ("Example 2 — Braking in a short distance", "u = 12 m s⁻¹, v = 0, s = 24 m. 0 = 144 + 2a(24) → a = **−3 m s⁻²**. t = (0 − 12) ÷ (−3) = **4 s**."),
 ("Example 3 — Why a gap matters", "Braking distances for a = −5 m s⁻²: at 10 m s⁻¹, s = 100 ÷ 10 = 10 m; at 20 m s⁻¹, s = 400 ÷ 10 = 40 m. **Double speed → four times the braking distance.**"),
 ("Example 4 — Reaction time", "Truck at 20 m s⁻¹, reaction time 0.6 s, a = −5 m s⁻². Reaction distance = 20 × 0.6 = 12 m. Braking = 40 m. Total **52 m**. An obstacle at 50 m is hit."),
 ("Example 5 — Area under a v–t graph", "0 → 8 m s⁻¹ in 4 s, 8 m s⁻¹ for 6 s, 8 → 0 in 4 s. Areas = 16 + 48 + 16 = **80 m**. Accelerations: +2, 0, −2 m s⁻²."),
 ("Example 6 — Catching up", "Thief 64 m ahead at 12 m s⁻¹; jeep from rest, a = 2 m s⁻². Jeep: t². Thief: 64 + 12t. t² − 12t − 64 = 0 → t = **16 s**; jeep covers 256 m, speed 32 m s⁻¹."),
 ("Example 7 — Average speed of a two-part journey", "65 km at 50 km h⁻¹ takes 1.3 h; 65 km at 65 km h⁻¹ takes 1 h. Average speed = 130 ÷ 2.3 = **56.5 km h⁻¹**, not the mean 57.5 km h⁻¹.")]),
("note", "IMPORTANT", "**Average speed is total distance divided by total time.** It is the simple mean of two speeds only when the two parts of the journey take equal **time**. For equal **distances** at speeds v₁ and v₂ the average speed is 2v₁v₂ ÷ (v₁ + v₂) (40 and 60 km h⁻¹ → 48 km h⁻¹)."),

("h2", "Reading Graphs Quickly"),
("table", ["Feature on graph", "Position–time (x–t)", "Velocity–time (v–t)"], [
 ["Horizontal line", "At rest", "Constant velocity, a = 0"],
 ["Straight rising line", "Constant velocity (slope = v)", "Constant acceleration (slope = a)"],
 ["Steeper line", "Larger velocity", "Larger acceleration"],
 ["Curve", "Velocity changing", "Acceleration changing (not covered)"],
 ["Line falling", "Moving back toward the origin (negative velocity)", "Retardation if v is positive"],
 ["Two lines crossing", "The two bodies are at the same place at that time", "The two bodies have the same velocity at that time (not the same place)"],
 ["Area under line", "—", "Displacement"]]),
("note", "REMEMBER", "On a v–t graph, a line crossing the time axis means the body **reverses direction**. **Areas below the axis are negative displacement.**"),

("h2", "Common Mistakes and Misconceptions"),
("ul", ["**Using km h⁻¹ with m s⁻² in the same equation.** Convert everything to SI first.",
 "**Forgetting the sign of retardation.** In v = u + at with v < u the value of a comes out negative; do not drop the sign.",
 "**Thinking zero velocity means zero acceleration.** A ball at the top of its path has v = 0 but a = g.",
 "**Using the kinematic equations when acceleration is not constant** (they are valid only for constant a).",
 "**Taking the simple mean for average speed.** Always use total distance ÷ total time.",
 "**Confusing the graph with the path.** An x–t or v–t graph is not a picture of the route.",
 "**Believing uniform circular motion has no acceleration.** Its speed is constant, but the direction of velocity changes continuously, so there is acceleration.",
 "**Mixing up slope and area.** Slope of x–t = velocity; slope of v–t = acceleration; area under v–t = displacement."]),
]
CH["blocks"] = _base[:-1] + _extra + _base[-1:]

if __name__ == "__main__": run(__file__, BANK, 9, "Science", WS, CH)
