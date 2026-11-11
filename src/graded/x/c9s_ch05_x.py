"""Class 9 Science Ch 5 Describing Motion Around Us - extras (g = 10 m/s^2)."""
from common import AR4, Q

AR = [
 AR4("The displacement of a body can be zero even though the distance travelled is not zero.", "Displacement is the shortest straight-line distance from the initial position to the final position, in a given direction.", "a",
     "If a body returns to its starting point, the shortest distance between start and finish is zero, although it has travelled a path."),
 AR4("The slope of a position-time graph gives the velocity of the body.", "The area under a velocity-time graph gives the displacement of the body.", "b",
     "Both are true statements about graphs, but the second does not explain the first."),
 AR4("Acceleration is the rate of change of velocity with time.", "The acceleration of a body is always in the direction of its motion.", "c",
     "A is the definition. R is false: for a slowing body (retardation) the acceleration is opposite to the motion."),
 AR4("The speedometer of a car measures its velocity.", "Velocity has both magnitude and direction.", "d",
     "A speedometer gives only the magnitude (speed), so A is false; R is true."),
 AR4("At the highest point of a ball thrown vertically upward, its velocity is zero but its acceleration is not zero.", "The acceleration due to gravity acts on the ball throughout its flight.", "a",
     "Gravity gives a constant downward acceleration of about 10 m/s$^2$ even when the velocity momentarily becomes zero."),
 AR4("The SI unit of acceleration is m/s$^2$.", "The distance-time graph of a body moving with uniform speed is a straight line.", "b",
     "Both are true but unrelated."),
]

CASE = [
 Q("<b>Case study.</b> A metro train in Delhi starts from rest at a station and accelerates uniformly at 0.5 m/s$^2$ for 40 s. It then moves at constant velocity for the next 60 s. "
   "(i) Find the velocity of the train after 40 s. (ii) Find the distance covered in the first 40 s. (iii) Find the distance covered in the next 60 s. (iv) Find the total distance covered in the 100 s and the average speed over this time.",
   r"(i) $v=u+at=0+0.5\times40=20$ m/s (1). (ii) $s=\tfrac12at^2=\tfrac12\times0.5\times1600=400$ m (1). (iii) $s=vt=20\times60=1200$ m (1). (iv) Total $=400+1200=1600$ m (1); average speed $=1600/100=16$ m/s (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A car on a highway near Nagpur is moving at 72 km/h. The driver sees a barrier ahead and applies the brakes, producing a uniform retardation of 5 m/s$^2$. "
   "(i) Convert the initial speed to m/s. (ii) Find the time taken to stop. (iii) Find the distance covered before the car stops. (iv) If the barrier is only 30 m from where the brakes are applied, find the speed with which the car hits it.",
   r"(i) $72\times\tfrac{5}{18}=20$ m/s (1). (ii) $t=\dfrac{v-u}{a}=\dfrac{0-20}{-5}=4$ s (1). (iii) $s=\dfrac{v^2-u^2}{2a}=\dfrac{0-400}{-10}=40$ m (1). (iv) $v^2=u^2+2as=400-2\times5\times30=100$ (1), so $v=10$ m/s (the car hits the barrier) (1).", "1+1+1+2"),
 Q("<b>Case study.</b> The velocity-time graph of a cyclist is described as follows: the velocity rises uniformly from 0 to 8 m/s in the first 4 s, stays at 8 m/s from 4 s to 10 s, and then falls uniformly to zero from 10 s to 12 s. "
   "(i) Find the acceleration during the first 4 s. (ii) What is the nature of the motion between 4 s and 10 s? (iii) Find the retardation during the last 2 s. (iv) Find the total distance travelled using the area under the graph.",
   r"(i) $a=\dfrac{8-0}{4}=2$ m/s$^2$ (1). (ii) Uniform velocity, with zero acceleration (1). (iii) $\dfrac{8-0}{2}=4$ m/s$^2$ (1). (iv) Area $=\tfrac12\times4\times8+6\times8+\tfrac12\times2\times8=16+48+8=72$ m (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Distance, displacement, speed, velocity", ["Distance: total path length (scalar, SI unit m). Displacement: shortest straight-line distance from initial to final position with direction (vector, m).",
   "Average speed $=\\dfrac{\\text{total distance}}{\\text{total time}}$ (m/s). Average velocity $=\\dfrac{\\text{displacement}}{\\text{time}}$.",
   "Displacement $\\le$ distance; for a full round trip displacement and average velocity are zero.",
   "$1\\text{ km/h}=\\dfrac{5}{18}\\text{ m/s}$."]),
 ("Acceleration", ["$a=\\dfrac{v-u}{t}$ (SI unit m/s$^2$); positive when the speed increases, negative (retardation) when it decreases.",
   "Uniform motion: equal distances in equal times (zero acceleration). Non-uniform: unequal distances in equal times."]),
 ("Equations of motion (uniform acceleration)", ["$v=u+at$",
   "$s=ut+\\tfrac12at^2$",
   "$v^2=u^2+2as$",
   "$u$ = initial velocity, $v$ = final velocity, $a$ = acceleration, $t$ = time, $s$ = displacement."]),
 ("Graphs", ["Position-time graph: slope = velocity; straight line = uniform velocity; curve = changing velocity; horizontal line = at rest.",
   "Velocity-time graph: slope = acceleration; area under the graph = displacement; horizontal line = uniform velocity; straight sloping line = uniform acceleration.",
   "Distance-time graph: slope = speed (never negative)."]),
 ("Motion under gravity (free fall)", ["Acceleration $g\\approx10\\text{ m/s}^2$ (9.8 m/s$^2$) directed downward for all bodies in the absence of air resistance.",
   "Thrown upward with speed $u$: maximum height $H=\\dfrac{u^2}{2g}$, time of ascent $=\\dfrac ug$; at the highest point $v=0$ but $a=g$.",
   "Dropped from rest: $v=gt$, $s=\\tfrac12gt^2$."]),
]

MISTAKES = [
 "Using distance instead of displacement (or speed instead of velocity); for a round trip the displacement and average velocity are zero.",
 "Not converting km/h to m/s before using the equations of motion, or mixing km with seconds.",
 "Putting a positive sign for retardation in $v=u+at$ or $v^2=u^2+2as$; for a slowing body $a$ is negative.",
 "Reading the slope of an x-t graph as acceleration and the slope of a v-t graph as velocity; slope of x-t is velocity, slope of v-t is acceleration.",
 "Calculating the distance from a v-t graph by adding signed areas or by taking only one segment; add the areas of all segments (triangles and rectangles) and take area below the axis as positive for distance.",
 "Thinking that acceleration is zero at the top of a vertical throw; only the velocity is zero, acceleration is still $g$.",
]
