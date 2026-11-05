"""Class 9 Science Ch 5 - Describing Motion Around Us (hand-written graded banks; numerics computed in code)."""
from sci import MC, AR, Z, T

SLUG, NAME, CHNO = "Describing_Motion", "Describing Motion Around Us", 5

def f(x):
    """Format a number without trailing zeros."""
    x = round(x, 2)
    return str(int(x)) if x == int(x) else str(x)

def num(q, ans, wrongs, why, unit=""):
    """MCQ whose correct answer is computed by the caller."""
    return (q, f(ans) + unit, *[f(w) + unit for w in wrongs], why)

# ---- computed numerical items -------------------------------------------------
# s = ut + 1/2 a t^2 ; v = u + at ; v^2 = u^2 + 2as   (g = 10 m/s^2)
v1 = 0 + 3 * 4                   # a=3, t=4 from rest
s1 = 0.5 * 2 * 10 ** 2           # a=2, t=10 from rest
a1 = (20 - 10) / 5               # 10 -> 20 in 5 s
s2 = (10 + 20) / 2 * 5           # same journey
a2 = (30 - 0) / 6                # rest to 30 in 6 s
v3 = (0 + 2 * 2 * 25) ** 0.5     # v^2 = 2as, a=2, s=25
s4 = 20 ** 2 / (2 * 5)           # brakes: v=20 -> 0 with a=-5
t4 = 20 / 5
h5 = 0.5 * 10 * 3 ** 2           # free fall 3 s
vf5 = 10 * 3
v6 = 72 * 5 / 18                 # 72 km/h in m/s
a6 = (0 - v6) / 8                # stops in 8 s
d6 = v6 * 8 / 2

# ============================ NCERT-TYPE ============================
nA = [MC([
 ("A runner completes one full lap of a 400 m circular track. Her displacement at the end is:", "0", "400 m", "200 m", "800 m", "She returns to the starting point."),
 ("The distance travelled by a body is always:", "greater than or equal to the magnitude of displacement", "less than displacement", "equal to velocity", "negative", "Path length is at least the straight-line gap."),
 ("Displacement is a:", "vector quantity", "scalar quantity", "unit", "constant", "It has magnitude and direction."),
 ("Speed is a:", "scalar quantity", "vector quantity", "unit of length", "force", "Only magnitude."),
 ("The SI unit of velocity is:", "m/s", "m", "m/s squared", "km", "Metre per second."),
 ("The SI unit of acceleration is:", "m/s squared", "m/s", "m", "kg", "Rate of change of velocity."),
 ("A boy walks 3 m east and then 4 m north. The distance covered is:", "7 m", "5 m", "1 m", "12 m", "3 + 4."),
 ("For the same boy, the magnitude of displacement is:", "5 m", "7 m", "1 m", "12 m", "Pythagoras: sqrt(9 + 16)."),
 ("A body moves with uniform velocity if it covers:", "equal displacements in equal intervals of time in the same direction", "equal distances in equal times in a circle", "unequal distances", "zero distance", "Constant magnitude and direction."),
 ("The slope of a distance-time graph gives:", "speed", "acceleration", "displacement", "force", "Distance divided by time."),
 ]), MC([
 ("The slope of a velocity-time graph gives:", "acceleration", "speed", "distance", "force", "Change in velocity per time."),
 ("The area under a velocity-time graph gives:", "displacement", "acceleration", "speed", "time", "Product of v and t."),
 ("A straight line parallel to the time axis on a distance-time graph indicates that the body is:", "at rest", "moving with uniform speed", "accelerating", "falling", "Distance does not change."),
 ("A straight line parallel to the time axis on a velocity-time graph indicates:", "uniform velocity", "rest only", "increasing acceleration", "retardation", "Velocity constant."),
 ("A straight line sloping upward on a velocity-time graph indicates:", "uniform acceleration", "uniform velocity", "rest", "retardation", "v increases uniformly."),
 ("Convert 90 km/h into m/s:", "25", "90", "9", "250", "90 x 5/18."),
 ("A car goes from 10 m/s to 20 m/s in 5 s. Its acceleration is:", f(a1) + " m/s squared", "5 m/s squared", "10 m/s squared", "0.5 m/s squared", "(20 - 10)/5."),
 ("The average speed of a car which travels 60 km in 1 hour and then 40 km in the next 1 hour is:", "50 km/h", "100 km/h", "60 km/h", "40 km/h", "100/2."),
 ("Which equation is correct for uniformly accelerated motion?", "v = u + at", "v = u - at only", "s = vt always", "v = at squared", "First equation."),
 ("Which equation is correct for uniformly accelerated motion?", "s = ut + (1/2)at squared", "s = ut - at", "s = u + at", "s = ut squared", "Second equation."),
 ]), MC([
 ("The equation v squared = u squared + 2as relates:", "velocity, acceleration and displacement", "velocity and time only", "force and mass", "work and time", "Third equation."),
 ("Acceleration due to gravity near the Earth's surface is about:", "10 m/s squared", "10 m/s", "1 m/s squared", "100 m/s squared", "g about 9.8."),
 ("A ball falls from rest for 2 s. Its velocity (g = 10 m/s squared) is:", "20 m/s", "10 m/s", "5 m/s", "40 m/s", "v = gt."),
 ("A ball is thrown vertically upward. At the highest point its velocity is:", "zero", "maximum", "10 m/s", "equal to initial", "Instantaneously at rest."),
 ("In uniform circular motion, the speed is constant but the velocity changes because:", "the direction keeps changing", "the magnitude changes", "the mass changes", "there is no force", "Direction changes."),
 ("In uniform circular motion, the velocity at any point is directed:", "along the tangent", "towards the centre", "away from the centre", "along the radius", "Tangent to the circle."),
 ("A body moving in a circle of radius r completes one revolution in time T. Its speed is:", "2 pi r / T", "pi r / T", "r / T", "2 r / T", "Circumference / time."),
 ("A car's speedometer shows 60 km/h. This reading is its:", "instantaneous speed", "average velocity", "displacement", "acceleration", "Speed at that instant."),
 ("Negative acceleration is called:", "retardation (deceleration)", "velocity", "speed", "inertia", "Velocity decreases."),
 ("An object is said to be in motion when its position:", "changes with time relative to a reference point", "does not change", "is zero", "is at origin", "Motion is relative."),
 ])]
nB = [
 Z("Differentiate between distance and displacement.", "Distance: total path length, scalar|1", "Displacement: shortest straight-line gap with direction, vector|1"),
 Z("Differentiate between speed and velocity.", "Speed: distance/time, scalar|1", "Velocity: displacement/time, vector|1"),
 Z("Can the magnitude of displacement be greater than the distance travelled? Give a reason.", "No|1", "Straight-line gap cannot exceed the path length|1"),
 Z("Convert 72 km/h into m/s.", "72 x 1000/3600|1", "= 20 m/s|1"),
 Z("Define acceleration. Give its SI unit.", "Rate of change of velocity|1", "m/s squared|1"),
 Z("What does the slope of a velocity-time graph represent?", "Acceleration|1", "Rise in velocity divided by time|1"),
 Z("What does the area under a velocity-time graph represent? How is it found for constant velocity?", "Displacement|1", "Area of a rectangle = v x t|1"),
 Z("A car increases its speed from 10 m/s to 20 m/s in 5 s. Find its acceleration.", "a = (20 - 10)/5|1", f"= {f(a1)} m/s squared|1"),
 Z("Why is uniform circular motion accelerated even though the speed is constant?", "Direction of velocity changes continuously|1", "Change in velocity means acceleration|1"),
 Z("Write the three equations of motion for uniform acceleration.", "v = u + at|1", "s = ut + (1/2)at squared and v squared = u squared + 2as|1"),
 Z("What is meant by a uniform and non-uniform motion? Give one example each.", "Uniform: equal distances in equal times|1", "Non-uniform: unequal, e.g. a car in traffic|1"),
 Z("What is average speed? A man runs 100 m in 20 s. Find his speed.", "Total distance / total time|1", "5 m/s|1"),
]
nC = [
 Z("A boy walks 3 m east and then 4 m north. Find the distance and the magnitude of displacement.", "Distance = 3 + 4 = 7 m|1", "Displacement = sqrt(3 squared + 4 squared)|1", "= 5 m|1"),
 Z("A car starts from rest with an acceleration of 3 m/s squared. Find its velocity after 4 s and the distance covered.", f"v = at = {f(v1)} m/s|1", "s = (1/2)at squared = 0.5 x 3 x 16|1", "= 24 m|1"),
 Z("A car moving at 20 m/s is brought to rest with a retardation of 5 m/s squared. Find the time taken and the distance covered.", f"t = 20/5 = {f(t4)} s|1", f"s = v squared / 2a = 400/10|1", f"= {f(s4)} m|1"),
 Z("A man drives 200 km north in 3 h and then 200 km south in 2 h. Find the average speed and the average velocity.", "Average speed = 400/5 = 80 km/h|1", "Net displacement = 0|1", "Average velocity = 0|1"),
 Z("A ball is dropped from a height and takes 3 s to reach the ground. Find the height and the velocity just before hitting the ground (g = 10 m/s squared).", f"h = 0.5 x 10 x 9 = {f(h5)} m|1", f"v = gt = {f(vf5)} m/s|1", "Starts from rest|1"),
 Z("Draw in words the distance-time graph of a body moving with uniform speed and show how to find the speed.", "A straight line sloping upward through the origin|1", "Take two points and find rise/run|1", "Slope = speed|1"),
 Z("From a velocity-time graph of a body moving at 6 m/s for 10 s find the distance covered.", "Graph is a horizontal line|1", "Area = 6 x 10|1", "= 60 m|1"),
 Z("A train accelerates from 10 m/s to 30 m/s in 10 s. Find the acceleration and the distance travelled.", "a = 20/10 = 2 m/s squared|1", "s = (10 + 30)/2 x 10|1", "= 200 m|1"),
 Z("A bicycle slows from 8 m/s to 4 m/s in 2 s. Find the acceleration and the stopping time from 4 m/s at the same rate.", "a = (4 - 8)/2 = -2 m/s squared|1", "Time to stop = 4/2|1", "= 2 s|1"),
 Z("Explain uniform circular motion with examples. Why is it an accelerated motion?", "Motion along a circle with constant speed|1", "Examples: tip of a fan blade, Earth around the Sun|1", "Velocity direction keeps changing|1"),
 Z("A body travels 20 m in the first 2 s and 30 m in the next 3 s. Find the average speed.", "Total distance 50 m|1", "Total time 5 s|1", "Average speed 10 m/s|1"),
 Z("Derive v = u + at from the definition of acceleration.", "a = (v - u)/t|1", "at = v - u|1", "v = u + at|1"),
 Z("The odometer of a car reads 2000 km at the start and 2050 km after 1 hour. Find the average speed and say what the speedometer shows.", "Distance = 50 km in 1 h|1", "Average speed 50 km/h|1", "Speedometer shows instantaneous speed|1"),
 Z("A body is thrown upwards with a velocity of 20 m/s. Find the maximum height and the time to reach it (g = 10 m/s squared).", "v = u - gt gives 0 = 20 - 10t, t = 2 s|1", "h = u squared / 2g = 400/20|1", "= 20 m|1"),
 Z("State three differences between scalar and vector quantities with examples.", "Scalar has magnitude only; vector has magnitude and direction|1", "Scalars: distance, speed, time|1", "Vectors: displacement, velocity, acceleration|1"),
 Z("An object moves 5 m east, then 12 m north. Find the displacement and its direction relative to east.", "Magnitude = sqrt(25 + 144) = 13 m|1", "tan(theta) = 12/5|1", "About 67 degrees north of east|1"),
 Z("Explain what a position-time graph that is a curve bending upward tells us about the motion.", "Slope increases with time|1", "Velocity is increasing|1", "The body is accelerating|1"),
 Z("Name three types of motion with examples of each.", "Linear: a car on a straight road|1", "Circular: a merry-go-round|1", "Oscillatory: a pendulum|1"),
]
nD = [
 Z("Derive the three equations of motion for a body moving with uniform acceleration using the velocity-time graph or algebra.", "v = u + at from slope|1", "s = area of trapezium = ut + (1/2)at squared|1", "v squared = u squared + 2as by eliminating t|1", "Meaning of symbols|1", "Conditions: uniform acceleration|1"),
 Z("A car starting from rest acquires a speed of 30 m/s in 6 s and then moves with this speed for 10 s, after which it brakes uniformly to rest in 5 s. Find the acceleration in each stage and the total distance.", f"Stage 1: a = {f(a2)} m/s squared|1", "Stage 2: a = 0|1", "Stage 3: a = -6 m/s squared|1", "Distance: 90 + 300 + 75|1", "= 465 m|1"),
 Z("Explain distance, displacement, speed, velocity and acceleration with a suitable example of a runner on a circular track.", "Distance along the path|1", "Displacement from the start|1", "Speed = distance/time|1", "Velocity = displacement/time|1", "Acceleration due to changing direction|1"),
 Z("A body is thrown vertically upward with a speed of 40 m/s (g = 10 m/s squared). Find the maximum height, the time to reach it and the total time of flight.", "t up = 4 s|1", "h = 1600/20 = 80 m|1", "Total time 8 s|1", "Velocity on return 40 m/s downward|1", "Symmetry of motion|1"),
 Z("Describe the distance-time and velocity-time graphs for (a) rest (b) uniform velocity (c) uniform acceleration (d) uniform retardation.", "Rest: horizontal s-t line|1", "Uniform velocity: straight s-t line, horizontal v-t line|1", "Uniform acceleration: straight rising v-t line|1", "Retardation: falling v-t line|1", "Slopes and areas|1"),
 Z("A cyclist rides with a speed of 18 km/h, accelerates uniformly at 0.5 m/s squared for 10 s and then applies brakes to stop in 20 s. Find the final speed after acceleration, the retardation and the total distance.", "u = 5 m/s|1", "v = 5 + 5 = 10 m/s|1", "s1 = 75 m|1", "Retardation = 0.5 m/s squared; s2 = 100 m|1", "Total = 175 m|1"),
 Z("Explain uniform circular motion with the tangent velocity direction, the relation v = 2 pi r/T, and calculate the speed of a body at the tip of a 0.5 m radius wheel with period 2 s (pi = 3.14).", "Velocity along the tangent|1", "Direction changes: accelerated|1", "v = 2 x 3.14 x 0.5/2|1", "= 1.57 m/s|1", "Speed constant|1"),
 Z("Two trains A and B of speeds 72 km/h and 54 km/h are moving on parallel tracks in the same direction. Find the speed of A relative to B and the time A takes to overtake B if A is 100 m behind and 150 m long and B is 150 m long.", "72 km/h = 20 m/s; 54 km/h = 15 m/s|1", "Relative speed 5 m/s|1", "Distance to cover = 100 + 150 + 150|1", "= 400 m|1", "Time = 80 s|1"),
 Z("Describe an activity to find the average speed of a student between two points using a stopwatch and measuring tape; discuss sources of error.", "Measure the distance|1", "Time the student walking|1", "Average speed = distance/time|1", "Errors: reaction time|1", "Repeat and average|1"),
 Z("A stone is dropped from the top of a tower and takes 4 s to reach the ground. Find the height of the tower, the velocity on reaching the ground and the distance in the last second (g = 10 m/s squared).", "h = 0.5 x 10 x 16 = 80 m|1", "v = 40 m/s|1", "Distance in 3 s = 45 m|1", "Last second = 35 m|1", "Using s = (1/2)gt squared|1"),
 Z("Explain the importance of the frame of reference with examples: passengers in a moving train and a person on the platform.", "Motion is relative|1", "A passenger is at rest relative to the train|1", "Moves relative to the platform|1", "Trees seem to move backward|1", "Describing motion needs a reference|1"),
 Z("A motorist travels 120 km at 60 km/h and returns at 40 km/h. Find the average speed for the whole trip and explain why it is not 50 km/h.", "Time going = 2 h; returning = 3 h|1", "Total distance = 240 km|1", "Total time 5 h|1", "Average speed 48 km/h|1", "Average speed is total distance over total time|1"),
]

# ============================ EASY ============================
eA = [MC([
 ("Distance is a:", "scalar", "vector", "force", "unit", "Magnitude only."),
 ("Displacement is a:", "vector", "scalar", "unit", "speed", "Magnitude and direction."),
 ("Speed = ", "distance/time", "time/distance", "distance x time", "mass/volume", "Formula."),
 ("Velocity = ", "displacement/time", "distance x time", "time/displacement", "mass x time", "Formula."),
 ("Acceleration = ", "change in velocity/time", "velocity x time", "distance/time", "force/time", "Formula."),
 ("SI unit of speed:", "m/s", "m", "kg", "s", "Metre per second."),
 ("SI unit of acceleration:", "m/s squared", "m/s", "m", "s", "Unit."),
 ("A body at rest has speed:", "zero", "10 m/s", "1 m/s", "100 m/s", "No motion."),
 ("A car moving at constant speed on a straight road has acceleration:", "zero", "positive", "negative", "infinite", "No change in velocity."),
 ("The slope of an s-t graph gives:", "speed", "acceleration", "force", "mass", "Slope."),
 ]), MC([
 ("The area under a v-t graph gives:", "displacement", "speed", "acceleration", "force", "Area."),
 ("The slope of a v-t graph gives:", "acceleration", "speed", "distance", "force", "Slope."),
 ("A runner completes one lap of a circular track. The displacement is:", "zero", "equal to distance", "double", "half", "Back at start."),
 ("1 km/h in m/s is:", "5/18 m/s", "18/5 m/s", "1 m/s", "10 m/s", "1000/3600."),
 ("36 km/h in m/s:", "10", "36", "3.6", "100", "36 x 5/18."),
 ("18 km/h in m/s:", "5", "18", "1.8", "50", "18 x 5/18."),
 ("Acceleration due to gravity is about:", "10 m/s squared", "100 m/s squared", "1 m/s squared", "0 m/s squared", "g."),
 ("A freely falling body starts with velocity:", "zero", "10 m/s", "equal to g", "infinite", "Dropped."),
 ("A body thrown upward has velocity zero at:", "the highest point", "the start", "the ground", "never", "Turning point."),
 ("In circular motion at uniform speed, velocity is:", "changing", "constant", "zero", "same direction", "Direction changes."),
 ]), MC([
 ("A car travels 100 km in 2 hours. Its average speed is:", "50 km/h", "200 km/h", "100 km/h", "2 km/h", "100/2."),
 ("A man walks 10 m in 5 s. His speed is:", "2 m/s", "50 m/s", "5 m/s", "0.5 m/s", "10/5."),
 ("Velocity changes from 0 to 10 m/s in 2 s. Acceleration:", "5 m/s squared", "20 m/s squared", "10 m/s squared", "2 m/s squared", "10/2."),
 ("Velocity of 20 m/s for 5 s. Distance:", "100 m", "4 m", "25 m", "20 m", "20 x 5."),
 ("A ball falls for 1 s (g = 10). Velocity:", "10 m/s", "1 m/s", "5 m/s", "20 m/s", "gt."),
 ("A ball falls for 2 s (g = 10). Distance:", "20 m", "10 m", "40 m", "5 m", "0.5 x 10 x 4."),
 ("The equation v = u + at gives v when u = 0, a = 2 and t = 3:", "6 m/s", "5 m/s", "3 m/s", "2 m/s", "2 x 3."),
 ("The retardation is:", "negative acceleration", "positive acceleration", "speed", "distance", "Slowing."),
 ("If velocity is constant, the v-t graph is:", "a horizontal line", "a sloping line", "a curve", "a vertical line", "No change."),
 ("If a body is at rest, the s-t graph is:", "a horizontal line", "a sloping line", "a curve", "a vertical line", "No change."),
 ])]
eB = [
 Z("Define distance.", "Total length of the path travelled|2"),
 Z("Define displacement.", "Shortest distance between initial and final positions with direction|2"),
 Z("Define speed.", "Distance travelled per unit time|2"),
 Z("Define velocity.", "Displacement per unit time|2"),
 Z("Define acceleration.", "Rate of change of velocity|2"),
 Z("What is uniform motion?", "Equal distances in equal intervals of time|2"),
 Z("Convert 54 km/h into m/s.", "54 x 5/18|1", "= 15 m/s|1"),
 Z("Write the first equation of motion.", "v = u + at|1", "Meaning of symbols|1"),
 Z("Write the second equation of motion.", "s = ut + (1/2)at squared|1", "Meaning of symbols|1"),
 Z("Write the third equation of motion.", "v squared = u squared + 2as|1", "Meaning of symbols|1"),
 Z("What is g? State its value.", "Acceleration due to gravity|1", "About 10 m/s squared|1"),
 Z("What is the displacement after one full circle?", "Zero|1", "Initial and final points coincide|1"),
]
eC = [
 Z("List three differences between distance and displacement.", "Scalar and vector|1", "Distance is always positive|1", "Displacement may be zero|1"),
 Z("List three differences between speed and velocity.", "Scalar vs vector|1", "Distance vs displacement|1", "Speed is never negative|1"),
 Z("A car covers 150 km in 3 h. Find the speed.", "Speed = distance/time|1", "150/3|1", "50 km/h|1"),
 Z("A body goes from 0 to 20 m/s in 5 s. Find the acceleration.", "a = (v - u)/t|1", "20/5|1", "4 m/s squared|1"),
 Z("A car at 10 m/s accelerates at 2 m/s squared for 5 s. Find the final velocity.", "v = u + at|1", "10 + 10|1", "20 m/s|1"),
 Z("A body starts from rest with an acceleration of 2 m/s squared. Find the distance in 5 s.", "s = (1/2)at squared|1", "0.5 x 2 x 25|1", "25 m|1"),
 Z("Convert 108 km/h to m/s.", "108 x 5/18|1", "= 30|1", "m/s|1"),
 Z("Convert 20 m/s to km/h.", "20 x 18/5|1", "= 72|1", "km/h|1"),
 Z("A ball dropped from rest hits the ground in 2 s. Find the speed (g = 10).", "v = gt|1", "= 20|1", "m/s|1"),
 Z("State the nature of the s-t graph for (a) rest (b) uniform speed (c) increasing speed.", "(a) Horizontal line|1", "(b) Straight sloping line|1", "(c) Curve bending upward|1"),
 Z("State the nature of the v-t graph for (a) uniform velocity (b) uniform acceleration (c) retardation.", "(a) Horizontal line|1", "(b) Rising straight line|1", "(c) Falling straight line|1"),
 Z("Give three examples of uniform circular motion.", "Fan blades|1", "Earth around the Sun|1", "Second hand of a clock|1"),
 Z("Name three scalars and three vectors.", "Scalars: distance, speed, time|1", "Vectors: displacement, velocity, acceleration|1", "Direction is the difference|1"),
 Z("A man walks 4 m east and 3 m north. Find the displacement.", "Pythagoras|1", "sqrt(16 + 9)|1", "5 m|1"),
 Z("State three examples of non-uniform motion.", "Car in traffic|1", "Falling ball|1", "Train starting|1"),
 Z("What does the speedometer and the odometer measure?", "Speedometer: instantaneous speed|1", "Odometer: distance covered|1", "Units km/h and km|1"),
 Z("A train of 100 m crosses a pole in 5 s. Find its speed.", "Distance = 100 m|1", "100/5|1", "20 m/s|1"),
 Z("Write the SI units of distance, speed, acceleration.", "m|1", "m/s|1", "m/s squared|1"),
]
eD = [
 Z("Explain distance, displacement, speed, velocity and acceleration.", "Distance|1", "Displacement|1", "Speed|1", "Velocity|1", "Acceleration|1"),
 Z("Derive v = u + at.", "a = (v - u)/t|1", "at = v - u|1", "v = u + at|1", "Symbols|1", "Conditions|1"),
 Z("A car starts from rest and reaches 20 m/s in 10 s. Find acceleration and distance.", "a = 2 m/s squared|1", "s = 0.5 x 2 x 100|1", "= 100 m|1", "Formulas used|1", "Units|1"),
 Z("A ball is dropped from a 45 m height. Find the time of fall and the final velocity (g = 10).", "45 = 5 t squared|1", "t = 3 s|1", "v = 30 m/s|1", "Starts from rest|1", "Formulas|1"),
 Z("Explain the graphs for rest, uniform velocity and acceleration.", "s-t graphs|1", "v-t graphs|1", "Slope meaning|1", "Area meaning|1", "Examples|1"),
 Z("Explain uniform circular motion.", "Definition|1", "Constant speed|1", "Direction changes|1", "Accelerated|1", "Examples|1"),
 Z("Find the average speed: 60 km in 2 h and 40 km in 1 h.", "Total distance 100 km|1", "Total time 3 h|1", "33.3 km/h|1", "Formula|1", "Units|1"),
 Z("A car at 20 m/s brakes with retardation of 4 m/s squared. Find the time and distance to stop.", "t = 5 s|1", "s = 400/8 = 50 m|1", "v = 0|1", "Formula|1", "Units|1"),
 Z("Explain the relative nature of motion with an example.", "Reference point|1", "Passenger in train|1", "Platform observer|1", "Trees seem to move|1", "Motion is relative|1"),
 Z("Explain how to find the speed of a body from a distance-time graph and acceleration from a velocity-time graph.", "Slope of s-t|1", "Take two points|1", "Slope of v-t|1", "Rise by run|1", "Units|1"),
 Z("A boy runs 400 m around a circular track of radius 63.7 m in 100 s. Find the speed and the displacement after one round.", "Speed = 4 m/s|1", "Displacement = 0|1", "Distance 400 m|1", "Velocity zero|1", "Reason|1"),
 Z("State five differences between scalars and vectors with examples.", "Magnitude|1", "Direction|1", "Examples|1", "Addition|1", "Units|1"),
]

# ============================ MEDIUM ============================
mA = [MC([
 num("A car starting from rest has acceleration 3 m/s squared. Its velocity after 4 s is (m/s):", v1, [6, 7, 1], "v = at.", " m/s"),
 num("A body starts from rest with acceleration 2 m/s squared. The distance covered in 10 s is:", s1, [20, 200, 10], "s = (1/2)at squared.", " m"),
 num("A car brakes from 20 m/s to rest with retardation 5 m/s squared. The distance covered is:", s4, [4, 100, 10], "v squared = 2as.", " m"),
 num("A car moving at 72 km/h stops in 8 s. The retardation is:", -a6, [4, 9, 0.9], "72 km/h = 20 m/s; a = 20/8.", " m/s squared"),
 num("A body starting from rest with a = 2 m/s squared covers 25 m. Its final velocity is:", v3, [5, 20, 50], "v squared = 2as = 100.", " m/s"),
 num("A stone is dropped; after 3 s it has fallen (g = 10):", h5, [30, 15, 90], "0.5 x 10 x 9.", " m"),
 num("The velocity of a stone dropped for 3 s is (g = 10):", vf5, [15, 10, 90], "gt.", " m/s"),
 num("A car travels at 90 km/h. Its speed in m/s is:", 90 * 5 / 18, [9, 90, 324], "90 x 5/18.", " m/s"),
 ("A body travels 40 m in 4 s and then 60 m in 6 s. Its average speed is:", "10 m/s", "5 m/s", "20 m/s", "100 m/s", "100/10."),
 ("A particle moves 3 m east and 3 m west in 6 s. Its average velocity is:", "zero", "1 m/s", "0.5 m/s", "6 m/s", "Net displacement zero."),
 ]), MC([
 ("A body moves along a straight line with speed 4 m/s for 10 s and 6 m/s for the next 10 s. The average speed is:", "5 m/s", "10 m/s", "4 m/s", "6 m/s", "100/20."),
 ("A car travels half the distance at 40 km/h and the other half at 60 km/h. The average speed is:", "48 km/h", "50 km/h", "45 km/h", "52 km/h", "Harmonic mean 2 x 40 x 60/100."),
 ("A graph of velocity against time is a straight line passing through the origin. The body has:", "uniform acceleration from rest", "uniform velocity", "zero acceleration", "retardation", "v proportional to t."),
 ("In a v-t graph, a line sloping downward from 20 m/s to 0 in 4 s shows retardation of:", "5 m/s squared", "20 m/s squared", "80 m/s squared", "4 m/s squared", "20/4."),
 ("The area under the v-t graph for the above is:", "40 m", "80 m", "20 m", "5 m", "Triangle: 0.5 x 4 x 20."),
 ("A car moves with uniform acceleration. The distance covered in the nth second is proportional to:", "(2n - 1)", "n squared", "n", "1/n", "Ratio 1 : 3 : 5."),
 ("The distances covered in successive seconds by a freely falling body from rest are in the ratio:", "1 : 3 : 5", "1 : 2 : 3", "1 : 4 : 9", "1 : 1 : 1", "Odd numbers."),
 ("The total distances covered in 1 s, 2 s, 3 s by a body falling from rest are in the ratio:", "1 : 4 : 9", "1 : 3 : 5", "1 : 2 : 3", "1 : 8 : 27", "Proportional to t squared."),
 ("A ball is thrown upward at 30 m/s. The time to reach the highest point (g = 10) is:", "3 s", "30 s", "6 s", "1.5 s", "u/g."),
 ("For the above, the maximum height is:", "45 m", "90 m", "30 m", "15 m", "u squared/2g."),
 ]), MC([
 ("A stone thrown vertically up returns to the thrower's hand after 6 s. The velocity of throw is (g = 10):", "30 m/s", "60 m/s", "15 m/s", "10 m/s", "t up = 3 s; u = gt."),
 ("A body in circular motion of radius 2 m makes 1 revolution in 4 s. Speed is (pi = 3.14):", "3.14 m/s", "6.28 m/s", "1.57 m/s", "12.56 m/s", "2 pi r/T = 12.56/4."),
 ("The displacement of a body after half a circle of radius r is:", "2r", "pi r", "r", "zero", "Diameter."),
 ("The distance covered by a body after half a circle of radius r is:", "pi r", "2r", "zero", "2 pi r", "Half the circumference."),
 ("A car with a speed of 54 km/h is 150 m from a signal. If it keeps the speed, the time to reach the signal is:", "10 s", "15 s", "2.8 s", "5 s", "15 m/s; 150/15."),
 ("A train 200 m long passing a pole in 10 s has speed:", "20 m/s", "2 m/s", "200 m/s", "10 m/s", "200/10."),
 ("A body covers 5 m in the first second and 15 m in the next second. This indicates:", "uniform acceleration", "uniform velocity", "retardation", "rest", "Speed increases."),
 ("A cyclist stops pedalling and rolls to rest in 10 s from 5 m/s. The average retardation is:", "0.5 m/s squared", "2 m/s squared", "50 m/s squared", "5 m/s squared", "5/10."),
 ("A jet starts from rest and reaches 100 m/s in 20 s. Its acceleration is:", "5 m/s squared", "2000 m/s squared", "0.2 m/s squared", "80 m/s squared", "100/20."),
 ("Which statement is correct about a body moving in a straight line with uniform acceleration?", "its velocity changes by equal amounts in equal times", "its speed is constant", "its displacement is constant", "it is at rest", "Definition."),
 ])]
mB = [
 Z("A car moves with uniform velocity of 15 m/s for 20 s. Find the distance and draw the nature of the v-t graph.", "s = 15 x 20 = 300 m|1", "Horizontal line; area gives distance|1"),
 Z("A scooter changes its velocity from 6 m/s to 12 m/s in 3 s. Find the acceleration and the distance moved.", "a = 2 m/s squared|1", "s = 9 x 3 = 27 m|1"),
 Z("A body of velocity 10 m/s accelerates at 2 m/s squared for 5 s. Find the final velocity and the distance covered.", "v = 20 m/s|1", "s = 75 m|1"),
 Z("A body moves 6 m east and 8 m north. Find the displacement and the distance.", "Distance 14 m|1", "Displacement 10 m|1"),
 Z("An object is dropped from 20 m. Find the time to hit the ground and the speed on impact (g = 10).", "t = 2 s|1", "v = 20 m/s|1"),
 Z("State why the slope of an s-t graph gives speed and show with numbers: 20 m at 2 s and 60 m at 6 s.", "Slope = (60 - 20)/(6 - 2)|1", "= 10 m/s|1"),
 Z("State the average velocity in a round trip and explain why.", "Zero|1", "Net displacement is zero|1"),
 Z("A car stops in 5 s from 15 m/s. Find the retardation and the stopping distance.", "a = -3 m/s squared|1", "s = 37.5 m|1"),
 Z("Why is the free fall of a feather and a stone in a vacuum identical?", "No air resistance|1", "Acceleration due to gravity is the same for all|1"),
 Z("An athlete runs 100 m in 10 s. Find the average speed in m/s and km/h.", "10 m/s|1", "36 km/h|1"),
 Z("Draw in words the s-t graph of a body that moves 10 m in 10 s, rests for 10 s and returns in 10 s.", "Rising line|1", "Horizontal line then falling line to the origin|1"),
 Z("Two cars A and B start from the same point; A moves at 10 m/s and B at 15 m/s in the same direction. Find the distance between them after 10 s.", "Relative speed 5 m/s|1", "Distance = 50 m|1"),
]
mC = [
 Z("A bus moving at 20 m/s speeds up uniformly to 30 m/s in 5 s. Find the acceleration, the distance and the average velocity.", "a = 2 m/s squared|1", "s = 25 x 5 = 125 m|1", "Average velocity 25 m/s|1"),
 Z("A ball is thrown upward with 25 m/s. Find the time to rise, the maximum height, and the velocity at 1 s (g = 10).", "Time = 2.5 s|1", "H = 625/20 = 31.25 m|1", "v at 1 s = 15 m/s|1"),
 Z("The speed of a car increases from 36 km/h to 72 km/h in 10 s. Find the acceleration in m/s squared and the distance travelled.", "u = 10, v = 20 m/s|1", "a = 1 m/s squared|1", "s = 150 m|1"),
 Z("A body starts from rest and moves with a = 4 m/s squared. Find the distance in the 3rd second.", "s3 - s2 = 0.5 x 4 x (9 - 4)|1", "= 10 m|1", "Using the nth second formula|1"),
 Z("A train at 90 km/h brakes with retardation 1.25 m/s squared. Find the distance and time to stop.", "u = 25 m/s|1", "t = 20 s|1", "s = 250 m|1"),
 Z("A person walks 40 m east, 30 m north and 40 m west in 50 s. Find the distance, displacement and average speed.", "Distance 110 m|1", "Displacement 30 m north|1", "Average speed 2.2 m/s|1"),
 Z("A car A starts from rest with a = 2 m/s squared and car B moves at uniform 20 m/s. When will A overtake B if both start together from the same point?", "s_A = t squared; s_B = 20t|1", "Equal when t = 20 s|1", "Distance 400 m|1"),
 Z("The speed-time data of a car are: t(s) 0, 2, 4, 6 and v(m/s) 0, 6, 12, 18. Find the acceleration and the distance in 6 s.", "a = 3 m/s squared|1", "Area of triangle = 0.5 x 6 x 18|1", "= 54 m|1"),
 Z("Explain the meaning of a v-t graph with equal horizontal segments at 5 m/s, then a rising line, then horizontal at 10 m/s.", "Uniform velocity 5 m/s|1", "Uniform acceleration while rising|1", "Then uniform velocity 10 m/s|1"),
 Z("A car travels with speeds of 20 m/s for 10 s, 30 m/s for 10 s and 40 m/s for 10 s. Find the average speed.", "Distance = 200 + 300 + 400 = 900 m|1", "Time = 30 s|1", "Average speed 30 m/s|1"),
 Z("A stone dropped from a bridge takes 2.5 s to hit the water. Find the height of the bridge and the impact speed (g = 10).", "h = 0.5 x 10 x 6.25 = 31.25 m|1", "v = 25 m/s|1", "Starts from rest|1"),
 Z("A body completes a circle of circumference 20 m in 5 s. Find the speed, the average velocity after half a revolution (displacement = diameter, taking pi = 3.14).", "Speed = 4 m/s|1", "Diameter = 20/3.14 = 6.37 m|1", "Average velocity = 6.37/2.5 = 2.55 m/s|1"),
 Z("An object has a uniform velocity of 8 m/s for 5 s, rests for 5 s and then moves with 4 m/s for 10 s. Find the total distance and the average speed.", "40 + 0 + 40 = 80 m|1", "Time 20 s|1", "Average speed 4 m/s|1"),
 Z("Show that for uniform acceleration the average velocity equals (u + v)/2 and use it to derive s = (u + v)t/2.", "Velocity changes uniformly|1", "Average v = (u + v)/2|1", "s = average velocity x t|1"),
 Z("A car moves 30 km in the first hour and 50 km in the second hour in the same direction. Find the average speed and say if the motion is uniform.", "80/2 = 40 km/h|1", "Distances in equal times unequal|1", "Non-uniform|1"),
 Z("A ball rolls down an incline from rest with an acceleration of 0.5 m/s squared. Find the velocity after 6 s and the distance covered.", "v = 3 m/s|1", "s = 9 m|1", "Formulas used|1"),
 Z("A body moving with uniform acceleration has velocity 5 m/s at t = 0 and 25 m/s at t = 10 s. Find the acceleration and the displacement.", "a = 2 m/s squared|1", "s = 15 x 10 = 150 m|1", "Average velocity 15 m/s|1"),
 Z("Explain why a body moving on a circle at a constant speed has a changing velocity and acceleration directed to the centre.", "Velocity direction changes|1", "Change in velocity points to the centre|1", "Hence centripetal acceleration|1"),
]
mD = [
 Z("A car accelerates from rest at 2 m/s squared for 10 s, moves at constant velocity for 20 s and then retards uniformly to rest in 5 s. Find the maximum velocity, the retardation and the total distance. Draw the v-t graph in words.", "Maximum velocity 20 m/s|1", "Retardation 4 m/s squared|1", "Distances 100, 400 and 50 m|1", "Total 550 m|1", "Trapezium graph|1"),
 Z("A ball is thrown vertically upward from the ground with 30 m/s. Find (a) the time to reach the top (b) the maximum height (c) the total time of flight (d) the velocity on returning (g = 10).", "(a) 3 s|1", "(b) 45 m|1", "(c) 6 s|1", "(d) 30 m/s downward|1", "Symmetry|1"),
 Z("Explain how to find the displacement, the acceleration and the average velocity from a v-t graph given as: 0 to 4 s rising from 0 to 8 m/s; 4 to 8 s constant at 8 m/s; 8 to 10 s falling to 0.", "Acceleration first part 2 m/s squared|1", "Distance first part 16 m|1", "Second part 32 m|1", "Third part 8 m (retardation 4)|1", "Total 56 m; average velocity 5.6 m/s|1"),
 Z("Two stations A and B are 120 km apart. A train leaves A at 60 km/h towards B and another leaves B at 40 km/h towards A at the same time. After how long and where do they meet?", "Relative speed = 100 km/h|1", "Time = 120/100 = 1.2 h|1", "From A: 72 km|1", "From B: 48 km|1", "Total 120 km|1"),
 Z("A stone is dropped from the top of a tower of height 80 m and at the same time another stone is thrown up from the base at 40 m/s. When and where do they meet (g = 10)?", "Relative speed constant at 40 m/s|1", "Time = 80/40 = 2 s|1", "First stone falls 20 m|1", "They meet 60 m above the ground|1", "Check second: 80 - 20 = 60|1"),
 Z("Derive the formula for the distance covered in the nth second and calculate it for a = 4 m/s squared, u = 2 m/s, n = 5.", "s_n = u + a(2n - 1)/2|1", "Substitute|1", "= 2 + 4 x 9/2|1", "= 20 m|1", "Check with s5 - s4|1"),
 Z("A driver at 72 km/h sees an obstacle 50 m ahead and brakes with a retardation of 5 m/s squared after a reaction time of 0.5 s. Will he stop in time?", "Speed 20 m/s|1", "Reaction distance 10 m|1", "Braking distance 40 m|1", "Total 50 m|1", "Just stops at the obstacle|1"),
 Z("Explain uniform circular motion of the Moon around the Earth: the orbital period 27 days, orbital radius 3.84 x 10^5 km, find the orbital speed in km/s (pi = 3.14).", "Circumference = 2 x 3.14 x 3.84 x 10^5 = 2.41 x 10^6 km|1", "Period = 27 x 86400 = 2.33 x 10^6 s|1", "Speed = 1.03 km/s|1", "Direction changes: acceleration|1", "Speed constant|1"),
 Z("The table gives t(s): 0, 1, 2, 3, 4 and s(m): 0, 5, 20, 45, 80 for a body. Analyse the motion, find the acceleration and the velocity at t = 4 s.", "s proportional to t squared|1", "Starts from rest|1", "s = 5t squared, so a = 10 m/s squared|1", "v = at = 40 m/s at 4 s|1", "Free fall|1"),
 Z("Explain, using the relative speed idea, why a passenger in a train moving at 80 km/h sees an oncoming train of speed 70 km/h passing at 150 km/h. Find the time taken to cross a 300 m train.", "Relative speed = 150 km/h|1", "= 41.7 m/s|1", "Time = 300/41.7|1", "= 7.2 s|1", "Opposite directions: speeds add|1"),
 Z("A race: A runs 100 m in 12.5 s, B in 12 s. Find the speeds in m/s and km/h, and the distance by which B wins.", "A: 8 m/s = 28.8 km/h|1", "B: 8.33 m/s = 30 km/h|1", "When B finishes, A has run 96 m|1", "B wins by 4 m|1", "Calculation of A's distance 8 x 12|1"),
 Z("Explain the graphical derivation of the equation of motion s = ut + (1/2)at squared from the v-t graph and verify numerically with u = 4, a = 2, t = 5.", "Area under graph = rectangle + triangle|1", "ut + (1/2)at squared|1", "= 20 + 25|1", "= 45 m|1", "Verify using average velocity 9 x 5 = 45|1"),
]

# ============================ HARD ============================
hA = [[
 AR("A body can have zero displacement but non-zero distance.", "Distance is the length of the path and displacement is the net change in position.", "a", "R explains A."),
 AR("A body moving in a circle with constant speed is accelerated.", "The direction of its velocity changes continuously.", "a", "R explains A."),
 AR("The average velocity of a body in a round trip is zero.", "The net displacement is zero.", "a", "R explains A."),
 AR("A ball thrown vertically up has zero acceleration at the highest point.", "Its velocity is zero at the highest point.", "d", "A is false: acceleration is g throughout; R is true."),
 AR("A feather and a coin fall together in a vacuum.", "In the absence of air resistance, all bodies fall with the same acceleration.", "a", "R explains A."),
 AR("The area under a velocity-time graph gives the displacement.", "Displacement is the product of average velocity and time.", "a", "R explains A."),
 AR("The slope of a position-time graph at an instant gives the instantaneous velocity.", "Velocity is the rate of change of position.", "a", "R explains A."),
 AR("A straight line on a v-t graph inclined to the time axis shows uniform acceleration.", "The slope of the line is constant.", "a", "R explains A."),
 AR("A car's speedometer measures its average velocity.", "The speedometer shows the instantaneous speed.", "d", "A is false and R is true."),
 AR("A body can have a velocity directed east and acceleration directed west.", "The acceleration is opposite to the velocity when the body slows down.", "a", "R explains A."),
 ], MC([
 ("A body is thrown upward with velocity u. The velocity at half the maximum height is:", "u / sqrt(2)", "u / 2", "u", "u / 4", "v squared = u squared - 2g(h/2) with h = u squared/2g."),
 ("A car goes from rest with acceleration a for time t, then retards uniformly with 2a till it stops. The total time is:", "1.5 t", "2 t", "t", "3 t", "v = at; retard time = at/2a = t/2."),
 ("A stone dropped from a height h takes time t. If dropped from 4h, the time taken will be:", "2t", "4t", "t", "t/2", "t proportional to sqrt(h)."),
 ("The ratio of distances covered in the 1st, 2nd and 3rd seconds from rest with uniform acceleration is:", "1 : 3 : 5", "1 : 2 : 3", "1 : 4 : 9", "1 : 1 : 1", "Odd numbers."),
 ("A body covers 30 m in the 3rd second from rest with uniform acceleration. Its acceleration is:", "12 m/s squared", "10 m/s squared", "6 m/s squared", "30 m/s squared", "s3 = a/2 x 5 = 30."),
 ("A train 100 m long moving at 36 km/h crosses a bridge in 20 s. The length of the bridge is:", "100 m", "200 m", "300 m", "20 m", "10 x 20 = 200 total; minus 100."),
 ("Two bodies are thrown up with speeds u and 2u. The ratio of their maximum heights is:", "1 : 4", "1 : 2", "2 : 1", "1 : 8", "h proportional to u squared."),
 ("A particle moving with uniform acceleration covers 20 m in the first 2 s and 60 m in the next 2 s. Its acceleration is:", "10 m/s squared", "5 m/s squared", "20 m/s squared", "2.5 m/s squared", "60 - 20 = a x t squared = 4a, so a = 10."),
 ("The displacement of a body is given by s = 5t + 2t squared (SI). Its acceleration is:", "4 m/s squared", "2 m/s squared", "5 m/s squared", "9 m/s squared", "Compare with ut + (1/2)at squared."),
 ("In the above case the initial velocity is:", "5 m/s", "2 m/s", "4 m/s", "0", "Coefficient of t."),
 ]), MC([
 ("A boat goes 12 km downstream in 1 hour and returns upstream in 2 hours. The average speed for the round trip is:", "8 km/h", "9 km/h", "6 km/h", "12 km/h", "24 km/ 3 h."),
 ("A man walks to a market at 4 km/h and returns at 6 km/h. The average speed is:", "4.8 km/h", "5 km/h", "4.5 km/h", "5.5 km/h", "Harmonic mean."),
 ("A body covers the first half of its journey at 20 m/s and the second half at 30 m/s. The average speed is:", "24 m/s", "25 m/s", "26 m/s", "50 m/s", "2 x 20 x 30/50."),
 ("A body is projected upward and takes 5 s to return. The maximum height reached (g = 10) is:", "31.25 m", "62.5 m", "125 m", "25 m", "t up = 2.5; h = 0.5 x 10 x 6.25."),
 ("A car decelerates uniformly from 30 m/s to 10 m/s in 5 s. The distance in this time is:", "100 m", "150 m", "200 m", "50 m", "Average 20 x 5."),
 ("A particle with a velocity of 10 m/s due east gets a velocity of 10 m/s due north after 5 s. The magnitude of its average acceleration is about:", "2.8 m/s squared", "4 m/s squared", "2 m/s squared", "0", "Change = 14.1 m/s over 5 s."),
 ("The ratio of the speeds of two bodies of the same mass dropped from different heights 2 m and 8 m just before impact is:", "1 : 2", "1 : 4", "2 : 1", "1 : 1", "v proportional to sqrt(h)."),
 ("The v-t graph of a body is a triangle with base 10 s and height 20 m/s. The distance covered is:", "100 m", "200 m", "50 m", "10 m", "0.5 x 10 x 20."),
 ("A car starting from rest reaches 25 m/s in 10 s with uniform acceleration and then moves at that speed for 20 s. The total distance is:", "625 m", "125 m", "500 m", "750 m", "125 + 500."),
 ("A lift going up moves with an acceleration a for t1, uniform speed for t2 and retards for t3. The v-t graph is a:", "trapezium", "triangle", "rectangle", "circle", "Shape of motion."),
 ])]
hB = [
 Z("A car travels the first half of the distance at 30 km/h and the next half at 60 km/h. Find the average speed.", "Harmonic mean 2 x 30 x 60/90|1", "= 40 km/h|1"),
 Z("A ball is thrown vertically upward and returns to the thrower in 4 s. Find the speed of throw and the maximum height (g = 10).", "u = g x 2 = 20 m/s|1", "H = 20 m|1"),
 Z("A body has displacement given by s = 2t + 3t squared. Find the velocity at t = 2 s.", "Initial velocity 2 m/s, a = 6 m/s squared|1", "v = 2 + 12 = 14 m/s|1"),
 Z("Why is the distance covered in successive seconds by a freely falling body increasing?", "Velocity increases with time|1", "Equal times, increasing average velocity|1"),
 Z("A body is dropped from rest and also another thrown down with 10 m/s from the same height. Compare the time of fall if h = 20 m (g = 10).", "Dropped: 2 s|1", "Thrown down: 20 = 10t + 5t squared gives t = 1.24 s|1"),
 Z("A cyclist is moving at 6 m/s and increases his speed to 11 m/s while covering 34 m. Find the acceleration and time.", "a = (121 - 36)/68 = 1.25 m/s squared|1", "t = 4 s|1"),
 Z("Why is the average velocity of a body moving at constant speed around a circle for half a revolution not equal to its speed?", "Displacement (diameter) is less than the arc length|1", "Velocity is displacement/time|1"),
 Z("Two balls A and B are dropped from heights 5 m and 20 m. Find the ratio of the times and the ratio of the final speeds.", "t proportional to sqrt(h): 1 : 2|1", "v proportional to sqrt(h): 1 : 2|1"),
 Z("A bus moving at 15 m/s sees a red light 60 m ahead. Find the minimum retardation needed to stop it just before the light.", "a = v squared / 2s|1", "= 225/120 = 1.875 m/s squared|1"),
 Z("If the velocity of a body is changing but its speed is constant, what type of motion is it? Give an example.", "Uniform circular motion|1", "Satellite or a car taking a circular turn|1"),
 Z("A stone is thrown vertically up at 15 m/s from a 20 m-high cliff. Find the velocity when it hits the ground (g = 10).", "v squared = 225 + 400|1", "v = 25 m/s|1"),
 Z("Show that the distance covered in the last second is the same for the upward and the downward trips for a stone thrown upward in the 1st and last seconds.", "Symmetry of motion|1", "The first second up equals the last second down|1"),
]
hC = [
 Z("A particle starts from rest with a = 4 m/s squared for 5 s, then moves uniformly for 10 s and then decelerates at 2 m/s squared until it stops. Find the total distance.", "v = 20 m/s; s1 = 50 m|1", "s2 = 200 m|1", "t3 = 10 s; s3 = 100 m; total = 350 m|1"),
 Z("A car A at 90 km/h overtakes car B moving at 72 km/h. If A is 50 m behind B, find the time taken to be 50 m ahead of B.", "Relative speed = 18 km/h = 5 m/s|1", "Relative distance = 100 m|1", "Time = 20 s|1"),
 Z("A ball thrown up with 20 m/s reaches the roof of a building in 1 s. Find the height of the roof and the velocity at that point (g = 10).", "h = 20 x 1 - 5 = 15 m|1", "v = 20 - 10 = 10 m/s upward|1", "Ball is still rising|1"),
 Z("A train starting from rest has acceleration 0.5 m/s squared for 1 minute. Find the speed in km/h and the distance covered.", "v = 30 m/s = 108 km/h|1", "s = 900 m|1", "Using time of 60 s|1"),
 Z("The velocity of a body increases from 2 m/s to 14 m/s in 6 s. Find a, s and the velocity at the midpoint of the time.", "a = 2 m/s squared|1", "s = 8 x 6 = 48 m|1", "v at 3 s = 8 m/s|1"),
 Z("Compare the motion of two bodies whose s-t graphs are straight lines through the origin with slopes 2 and 5. Find the speeds and the distance between them after 10 s.", "Speeds 2 m/s and 5 m/s|1", "Distances 20 m and 50 m|1", "Separation 30 m (same direction)|1"),
 Z("A ball rolls down an incline from rest and covers 2 m in the 1st second. Find the acceleration and the distance in 4 s.", "s1 = a/2 = 2, so a = 4 m/s squared|1", "s4 = 0.5 x 4 x 16|1", "= 32 m|1"),
 Z("A man jumps from a height of 5 m. Find the time of fall and the speed on landing, and the retardation if he stops in 0.1 s (g = 10).", "t = 1 s, v = 10 m/s|1", "a = 10/0.1 = 100 m/s squared|1", "Bending knees increases the stopping time|1"),
 Z("The equation of motion s = 10t - 2t squared is given. Find the initial velocity, acceleration and when the body momentarily stops.", "u = 10 m/s|1", "a = -4 m/s squared|1", "Stops at t = 2.5 s|1"),
 Z("Calculate the average speed of the tip of a minute hand of length 10 cm (pi = 3.14) in cm/min and the displacement of the tip in 30 minutes.", "Circumference = 62.8 cm|1", "Speed = 62.8 cm/min|1", "Displacement = 20 cm|1"),
 Z("Explain why the time taken to fall from the second half of a height is shorter than for the first half using h = 100 m.", "Total time 4.47 s|1", "First 50 m takes 3.16 s|1", "Second 50 m takes 1.31 s as speed has increased|1"),
 Z("A bike accelerates from 0 to 54 km/h in 5 s. Find the acceleration and the distance. If the acceleration is then halved, find the time to reach 72 km/h.", "a = 3 m/s squared|1", "s = 37.5 m|1", "Time = 5/1.5 = 3.33 s|1"),
 Z("A lift moves upward with acceleration 2 m/s squared for 4 s, then uniformly for 6 s and decelerates at 4 m/s squared. Find the height travelled.", "v = 8 m/s; s1 = 16 m|1", "s2 = 48 m|1", "t3 = 2 s; s3 = 8 m; total 72 m|1"),
 Z("A car travelling at 25 m/s is overtaking another at 15 m/s on a road. A truck coming from the opposite direction at 20 m/s is 400 m ahead. Will the overtaking car pass safely if it needs 6 s?", "Closing speed with truck 45 m/s|1", "In 6 s: 270 m covered|1", "270 < 400, so safe|1"),
 Z("Find the displacement of a body given by its v-t graph: +4 m/s for 5 s then -4 m/s for 5 s.", "First 20 m forward|1", "Next 20 m backward|1", "Displacement 0; distance 40 m|1"),
 Z("Explain how the third equation of motion can be derived from the first two.", "t = (v - u)/a|1", "Substitute into s = ut + 0.5 a t squared|1", "v squared = u squared + 2as|1"),
 Z("Explain why the speed at the lowest point is the same as the speed at the start if a ball is thrown up and returns to the same level, ignoring air resistance.", "Energy or motion is symmetric|1", "Upward and downward trips are mirror images|1", "Speed equals initial speed|1"),
 Z("A car is moving at 20 m/s. The driver sees a child 40 m away and brakes with 5 m/s squared after 0.4 s of reaction time. Find the distance and judge if the child is in danger.", "Reaction distance 8 m|1", "Braking distance 40 m|1", "Total 48 m which exceeds 40 m: danger|1"),
]
hD = [
 Z("A train starts from rest at station A and stops at station B 3 km away. It accelerates at 0.5 m/s squared for the first part and retards at 1 m/s squared for the last part with no uniform stretch. Find the maximum speed, the total time and the distances in the two parts.", "Distances inversely proportional to a: 2 km and 1 km|1", "v squared = 2 x 0.5 x 2000, v = 44.7 m/s|1", "t1 = 89.4 s|1", "t2 = 44.7 s; total 134 s|1", "Check s2 = 44.7 squared/2 = 1000 m|1"),
 Z("A stone is dropped from a balloon rising upwards with 10 m/s when it is at 75 m. Find the time taken by the stone to reach the ground and its velocity then (g = 10).", "Initial velocity 10 m/s upward|1", "-75 = 10t - 5t squared|1", "t squared - 2t - 15 = 0, t = 5 s|1", "v = 10 - 50 = -40 m/s|1", "Speed 40 m/s downward|1"),
 Z("Plot and analyse the data for a car: t = 0, 5, 10, 15, 20, 25 s; v = 0, 10, 20, 20, 10, 0 m/s. Find the acceleration in each stage, the total distance and the average speed.", "a = 2 m/s squared for 10 s|1", "a = 0 for 5 s|1", "a = -2 for 10 s|1", "Distance 100 + 100 + 100 = 300 m|1", "Average speed 12 m/s|1"),
 Z("Two stones are thrown vertically upward from the same point with the same speed 20 m/s but 2 s apart. When and where do they meet (g = 10)?", "Stone 1: h = 20t - 5t squared|1", "Stone 2: h = 20(t - 2) - 5(t - 2) squared|1", "Equate: t = 3 s|1", "h = 15 m|1", "Velocities 10 up and -10 down|1"),
 Z("The motion of a particle is given by x = 3t squared - 2t + 1 (SI). Find its displacement in the first 3 s, the velocity at t = 3 s, and the average velocity and acceleration.", "x(0) = 1, x(3) = 22, displacement 21 m|1", "v = 6t - 2 = 16 m/s|1", "Average velocity = 7 m/s|1", "a = 6 m/s squared|1", "Initial velocity -2 m/s|1"),
 Z("A cricket ball hit vertically upward reaches a maximum height of 45 m. Find the speed of the hit, the time of flight and the velocity 2 s after the hit (g = 10).", "u = sqrt(2 x 10 x 45) = 30 m/s|1", "Time up 3 s, time of flight 6 s|1", "v at 2 s = 30 - 20 = 10 m/s upward|1", "At 4 s: 10 m/s downward|1", "Symmetry of the upward and downward motion|1"),
 Z("Explain the motion of a ball moving in a vertical circle of radius 1 m with speed 4 m/s, the period, the speed vs velocity, and the average velocity over half a period (pi = 3.14).", "T = 2 x 3.14/4 = 1.57 s|1", "Speed constant 4 m/s|1", "Velocity changes direction|1", "Displacement in half period 2 m|1", "Average velocity = 2/0.785 = 2.55 m/s|1"),
 Z("A police car at rest starts moving with 2 m/s squared acceleration when a speeding car moving at 20 m/s passes it. Find where and when the police car catches it and the speed of the police car then.", "Equal distances: t squared = 20t|1", "t = 20 s|1", "Distance 400 m|1", "Police speed 40 m/s|1", "Relative speeds before and after|1"),
 Z("Analyse the free fall of a stone from a 125 m high cliff: time of fall, speed, distances in the first, second and last seconds (g = 10).", "t = 5 s|1", "v = 50 m/s|1", "1st second 5 m, 2nd 15 m|1", "Last second 45 m (125 - 80)|1", "Ratio 1 : 3 : 5 : 7 : 9|1"),
 Z("A body moves in a straight line with the v-t graph: 0 to 2 s: 0 to 6 m/s; 2 to 5 s: 6 m/s; 5 to 7 s: 6 to -2 m/s. Find the displacement, the distance and the average acceleration over 7 s.", "Area 0-2: 6 m|1", "Area 2-5: 18 m|1", "5 to 6.5 s: +4.5 m, 6.5 to 7: -0.5 m|1", "Displacement 28 m, distance 29 m|1", "Average acceleration = (-2 - 0)/7 = -0.29 m/s squared|1"),
 Z("A body is thrown vertically upward from the top of a 40 m high tower with a speed of 20 m/s. Find the maximum height above the ground, the time to reach the ground and the speed with which it hits the ground (g = 10).", "Rise = 400/20 = 20 m, so maximum height 60 m|1", "Time up = 2 s|1", "Fall of 60 m takes sqrt(12) = 3.46 s, total 5.46 s|1", "v = sqrt(2 x 10 x 60) = 34.6 m/s|1", "Check with v squared = u squared + 2gh over 40 m: 400 + 800 = 1200|1"),
 Z("Discuss the role of reaction time and braking distance in road safety with the equation d = vt + v squared/2a, calculating the total stopping distance at 20 m/s and 30 m/s with t = 0.5 s and a = 5 m/s squared.", "At 20 m/s: 10 + 40 = 50 m|1", "At 30 m/s: 15 + 90 = 105 m|1", "Doubling speed more than doubles stopping distance|1", "Reaction time matters|1", "Speed limits are for safety|1"),
]

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
