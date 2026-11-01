from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def fm(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}".rstrip("0").rstrip(".")
def opts(v, u, extra=()):
    v = F(v); c = [v * 2, v / 2, v + 2, v - 2 if v > 2 else v + 4, v * 3, v + 5, v / 3]
    out = []
    for x in list(extra) + c:
        x = F(x)
        if x != v and x > 0 and fm(x) != fm(v) and fm(x) not in out: out.append(fm(x))
    return [f"{o} {u}" for o in out[:3]]
A = []
# average speed (4)
for d, t, sp in [(120, 40, 3), (300, 60, 5), (450, 90, 5), (1800, 100, 18)]:
    pass
for d, t in [(120, 40), (300, 60), (900, 50), (1500, 100)]:
    v = F(d, t)
    A.append(M4(f"A cyclist covers {d} m in {t} s along a straight road without turning back. The average speed is:", f"{fm(v)} m s⁻¹", opts(v, "m s⁻¹", [F(t, d)]), f"{d} ÷ {t}"))
# unit conversion (3)
for k in [36, 72, 108]:
    v = F(k * 5, 18)
    A.append(M4(f"A speed of {k} km h⁻¹ in SI units is:", f"{fm(v)} m s⁻¹", opts(v, "m s⁻¹", [F(k, 3), F(k * 18, 5)]), f"{k} × 5/18"))
# acceleration (4)
for u, v, t in [(0, 20, 5), (10, 30, 4), (25, 5, 10), (15, 0, 5)]:
    a = F(v - u, t); sgn = "−" if a < 0 else ""
    o = [x for x in dict.fromkeys([f"{sgn}{fm(abs(a)*2)} m s⁻²", f"{'' if a<0 else '−'}{fm(abs(a))} m s⁻²", f"{fm(abs(a)+1)} m s⁻²", f"{fm(F(v+u, t))} m s⁻²"]) if x != f"{sgn}{fm(abs(a))} m s⁻²"][:3]
    A.append(M4(f"The velocity of a car changes from {u} m s⁻¹ to {v} m s⁻¹ in {t} s in a straight line. Its average acceleration is:", f"{sgn}{fm(abs(a))} m s⁻²", o, f"({v} − {u}) ÷ {t}"))
# v = u + at (3)
for u, a, t in [(0, 3, 6), (5, 2, 8), (20, -4, 3)]:
    v = u + a * t
    A.append(M4(f"A body with initial velocity {u} m s⁻¹ moves with constant acceleration {a} m s⁻² for {t} s. Its final velocity is:", f"{v} m s⁻¹", opts(v, "m s⁻¹", [u + a, u * t + a * t])[:3] if v > 0 else [f"{x} m s⁻¹" for x in (-v, v + 10, 32)], "v = u + at"))
# s = ut + at²/2 (3)
for u, a, t in [(0, 2, 5), (10, 2, 4), (0, 4, 3)]:
    s = F(u * t) + F(a * t * t, 2)
    A.append(M4(f"A body starts with velocity {u} m s⁻¹ and accelerates uniformly at {a} m s⁻² for {t} s. The distance travelled is:", f"{fm(s)} m", opts(s, "m", [a * t * t, u * t + a * t]), "s = ut + ½at²"))
# stopping distance (3)
for u, a in [(20, 5), (30, 5), (10, 2)]:
    s = F(u * u, 2 * a)
    A.append(M4(f"A vehicle moving at {u} m s⁻¹ is brought to rest with a uniform retardation of {a} m s⁻². The stopping distance is:", f"{fm(s)} m", opts(s, "m", [F(u * u, a), F(u, a)]), "v² = u² + 2as"))
# circular distance (2)
for r, tag in [(7, 44), (14, 88)]:
    A.append(M4(f"A child on a merry-go-round of radius {r} m completes one full revolution (π = 22/7). The distance travelled and the displacement are:", f"{tag} m and 0", [f"{tag//2} m and {r} m", f"{tag} m and {2*r} m", f"0 and {tag} m"], "circumference = 2πr; returns to start"))
A += [
 M4("Displacement is:", "the shortest straight-line change in position with a direction", ["the total path length covered", "always equal to distance", "always positive"], "vector quantity"),
 M4("A runner completes one full lap of a 400 m track. Her displacement is:", "zero", ["400 m", "200 m", "800 m"], "returns to start"),
 M4("The SI unit of acceleration is:", "m s⁻²", ["m s⁻¹", "km h⁻¹", "m s²"], "change in velocity per second"),
 M4("Average speed and the magnitude of average velocity are equal when an object:", "moves in a straight line in one direction", ["moves in a circle", "returns to start", "is at rest"], "distance = |displacement|"),
 M4("The slope of a position–time graph gives:", "velocity", ["acceleration", "displacement", "distance only"], "rate of change of position"),
 M4("The slope of a velocity–time graph gives:", "acceleration", ["velocity", "displacement", "speed"], "rate of change of velocity"),
 M4("The area under a velocity–time graph gives:", "displacement", ["acceleration", "velocity", "force"], "v × t"),
 M4("A straight line parallel to the time axis on a position–time graph shows that the object is:", "at rest", ["moving with constant velocity", "accelerating", "moving in a circle"], "position does not change"),
 M4("A horizontal line on a velocity–time graph shows:", "constant velocity, zero acceleration", ["rest", "constant acceleration", "decreasing velocity"], "slope is zero"),
 M4("Which equation is NOT a kinematic equation for constant acceleration?", "v = s/t²", ["v = u + at", "s = ut + ½at²", "v² = u² + 2as"], "not valid in general"),
 M4("In uniform circular motion, the object has:", "constant speed but changing velocity", ["constant velocity", "zero acceleration", "changing speed"], "direction keeps changing"),
 M4("In uniform circular motion the velocity at any point is directed:", "along the tangent", ["towards the centre", "away from the centre", "along the radius"], "tangent to circle"),
 M4("A body thrown vertically upward and falling back to the thrower's hand has displacement:", "zero", ["twice the height", "the maximum height", "equal to the distance"], "returns to start"),
 M4("The acceleration of a freely falling body near Earth's surface is about:", "9.8 m s⁻²", ["98 m s⁻²", "0.98 m s⁻²", "1.6 m s⁻²"], "g"),
 M4("A negative sign for acceleration in straight-line motion means:", "acceleration is opposite to the chosen positive direction", ["the body is at rest", "the speed is zero", "the distance is negative"], "sign gives direction"),
 M4("A car goes from rest to 20 m s⁻¹ in 10 s. The distance covered, assuming uniform acceleration, is:", "100 m", ["200 m", "50 m", "20 m"], "average velocity 10 m/s × 10 s"),
 M4("Which graph shows a body moving with uniform acceleration?", "a straight inclined line on a velocity–time graph", ["a horizontal line on a velocity–time graph", "a horizontal line on a position–time graph", "a vertical line on a position–time graph"], "constant slope of v–t"),
 M4("A body in uniform circular motion of radius r completes one revolution in time T. Its average speed is:", "2πr/T", ["zero", "r/T", "πr/T"], "circumference ÷ time"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Distinguish between distance and displacement.", "Distance is the total path length (scalar, only magnitude); displacement is the net change in position with direction (1+1).", "1+1"),
 Q("Can the magnitude of displacement be greater than the distance travelled? Give reason.", "No; the straight-line change in position cannot exceed the actual path length (2).", "2"),
 Q("Define average velocity. State its SI unit.", "Displacement divided by the time interval (1); m s⁻¹ (1).", "1+1"),
 Q("A boy walks 3 m east and then 4 m north. Find the distance and the magnitude of displacement.", "Distance = 3 + 4 = 7 m (1); displacement = √(3² + 4²) = 5 m (1).", "1+1"),
 Q("An athlete completes one round of a circular track of radius 7 m in 40 s. Find the average speed (π = 22/7).", "Distance = 2 × 22/7 × 7 = 44 m (1); speed = 44/40 = 1.1 m s⁻¹ (1).", "1+1"),
 Q("Convert 90 km h⁻¹ into m s⁻¹.", "90 × 5/18 = 25 m s⁻¹ (2).", "2"),
 Q("Define acceleration. What does a negative value indicate?", "Rate of change of velocity (1); acceleration opposite to velocity, i.e. retardation if it is slowing down (1).", "1+1"),
 Q("A car increases its speed from 10 m s⁻¹ to 20 m s⁻¹ in 5 s. Find its acceleration.", "a = (20 − 10)/5 (1) = 2 m s⁻² (1).", "1+1"),
 Q("What does the slope of a position–time graph represent?", "Velocity (rate of change of position) (2).", "2"),
 Q("What does the area under a velocity–time graph represent? How is it found for constant velocity?", "Displacement (1); rectangle: velocity × time (1).", "1+1"),
 Q("Write the three kinematic equations for uniformly accelerated motion.", "v = u + at (½); s = ut + ½at² (1); v² = u² + 2as (½).", "2"),
 Q("A car starting from rest has acceleration 3 m s⁻². Find its velocity after 4 s.", "v = 0 + 3 × 4 = 12 m s⁻¹ (2).", "2"),
 Q("Why is circular motion at constant speed accelerated?", "The direction of velocity changes continuously, so velocity changes (2).", "2"),
 Q("What is the direction of velocity in uniform circular motion?", "Tangent to the circle at the point (2).", "2"),
 Q("Give one example each of uniform and non-uniform motion in a straight line.", "Uniform: a train at constant speed on a straight track; non-uniform: a car speeding up from a traffic signal (1+1).", "1+1"),
 Q("A ball falls from rest for 2 s. Find its velocity (g = 10 m s⁻²).", "v = gt = 10 × 2 = 20 m s⁻¹ (2).", "2"),
]
C = [
 Q("Explain with an example why distance travelled and displacement can be different.", "A girl runs 100 m east and returns 40 m (1); distance = 140 m (1); displacement = 60 m east (1).", "1+1+1"),
 Q("A student goes to the 4th floor of a building (3 m per floor) and then comes down to the 2nd floor. Find the vertical distance and displacement.", "Distance = 12 + 6 = 18 m (2); displacement = 6 m upward (1).", "2+1"),
 Q("A man drives 200 km north in 3 h and then 200 km south in 2 h. Find the average speed and average velocity.", "Average speed = 400/5 = 80 km h⁻¹ (2); average velocity = 0 (1).", "2+1"),
 Q("Explain how a body can have zero average velocity but non-zero average speed.", "When it returns to the starting point, displacement is zero but distance is not (3).", "3"),
 Q("A bus speeds up from 36 km h⁻¹ to 54 km h⁻¹ in 10 s. Find the acceleration.", "36 km/h = 10 m/s, 54 km/h = 15 m/s (1); a = (15 − 10)/10 (1) = 0.5 m s⁻² (1).", "1+1+1"),
 Q("A bus moving at 54 km h⁻¹ is stopped in 5 s by braking. Find the acceleration and the stopping distance.", "u = 15 m/s; a = −15/5 = −3 m s⁻² (1.5); s = 15 × 5/2 = 37.5 m (1.5).", "1½+1½"),
 Q("State the characteristics of a position–time graph for (i) an object at rest and (ii) uniform motion.", "(i) Straight line parallel to the time axis (1.5); (ii) straight inclined line whose slope gives constant velocity (1.5).", "1½+1½"),
 Q("Distinguish between the position–time graphs of uniform and non-uniform motion.", "Uniform: straight line (1.5); non-uniform: curve, since displacements in equal intervals are unequal (1.5).", "1½+1½"),
 Q("Draw a velocity–time graph for a body with constant acceleration and describe how acceleration is obtained.", "Straight line inclined to the time axis (1); take two points, acceleration = (v₂ − v₁)/(t₂ − t₁) = slope (2).", "1+2"),
 Q("A velocity–time graph is a horizontal line at 20 m s⁻¹ from 0 to 6 s. Find the acceleration and displacement.", "Slope zero, so acceleration = 0 (1); displacement = area = 20 × 6 = 120 m (2).", "1+2"),
 Q("A car moves with velocity rising uniformly from 5 m s⁻¹ to 15 m s⁻¹ in 10 s. Find the displacement using the graph.", "Area of trapezium = ½ × (5 + 15) × 10 = 100 m (3).", "3"),
 Q("Derive v = u + at using the definition of acceleration.", "a = (v − u)/t (2); hence v = u + at (1).", "2+1"),
 Q("Derive s = ut + ½at² from a velocity–time graph.", "Area = rectangle ut + triangle ½ × t × (v − u) (1.5); (v − u) = at, so s = ut + ½at² (1.5).", "1½+1½"),
 Q("A train starting from rest reaches 20 m s⁻¹ in 50 s. Find the acceleration and distance.", "a = 20/50 = 0.4 m s⁻² (1.5); s = ½ × 0.4 × 50² = 500 m (1.5).", "1½+1½"),
 Q("A car moving at 20 m s⁻¹ brakes with retardation 5 m s⁻². Find the stopping distance and time.", "0 = 400 − 10s ⇒ s = 40 m (2); t = 20/5 = 4 s (1).", "2+1"),
 Q("Why is it important to keep a safe distance from the vehicle ahead? Relate to stopping distance.", "Stopping distance ∝ u² (v² = u² + 2as); doubling speed makes it four times (3).", "3"),
 Q("Explain uniform circular motion with an example. Is the motion accelerated?", "Motion in a circle at constant speed, e.g. a fan blade tip (1); direction of velocity keeps changing (1), so it is accelerated (1).", "1+1+1"),
 Q("A body moves round a circle of radius 14 m in 22 s. Find the distance, displacement after one round and speed (π = 22/7).", "Distance = 88 m (1); displacement = 0 (1); speed = 88/22 = 4 m s⁻¹ (1).", "1+1+1"),
 Q("A stone is dropped from a tower and takes 3 s to hit the ground. Find the height and final velocity (g = 10 m s⁻²).", "h = ½ × 10 × 9 = 45 m (2); v = 30 m s⁻¹ (1).", "2+1"),
 Q("Two cars A and B have position–time lines of slopes 10 and 20 m s⁻¹. Which is faster? Find the distance each covers in 5 s.", "B is faster (steeper) (1); A = 50 m, B = 100 m (2).", "1+2"),
 Q("Is a scooter with a constant speedometer reading always unaccelerated? Explain.", "No; if it turns a bend, the direction of velocity changes and so it accelerates (3).", "3"),
 Q("Using the Ganitakaumudi example, two postmen start 210 yojanas apart and walk towards each other at 9 and 5 yojanas per day. When do they meet?", "Combined speed = 14 yojanas/day (1.5); time = 210/14 = 15 days (1.5).", "1½+1½"),
 Q("A body travels 20 m in the first 2 s and 40 m in the next 2 s in a straight line. Is the motion uniform? Find average speeds.", "20/2 = 10 m s⁻¹, 40/2 = 20 m s⁻¹ (2); unequal distances in equal times, so non-uniform (1).", "2+1"),
 Q("A motorbike with u = 28 m s⁻¹ stops after 98 m. Find the acceleration and time.", "0 = 784 + 2a(98) ⇒ a = −4 m s⁻² (2); t = 28/4 = 7 s (1).", "2+1"),
]
D = [
 Q("(i) Define displacement and average velocity. (ii) An athlete runs from O to A (100 m), turns back to B (60 m from A). Find the distance and displacement. (iii) Compare average speed and average velocity.", "(i) Net change in position; displacement/time (2). (ii) Distance 160 m; displacement 40 m (2). (iii) Speed = distance/time (scalar); velocity = displacement/time (vector) (1).", "2+2+1"),
 Q("(i) Define acceleration with SI unit. (ii) A car moves from 36 km h⁻¹ to 72 km h⁻¹ in 5 s. Find the acceleration. (iii) Explain what the sign of acceleration means.", "(i) Rate of change of velocity; m s⁻² (1). (ii) 10 → 20 m/s; a = 2 m s⁻² (2). (iii) Positive: along velocity (speeding up), negative: opposite (slowing) (2).", "1+2+2"),
 Q("<b>Case study:</b> A bus at 36 km h⁻¹ accelerates for 10 s to 54 km h⁻¹, moves uniformly for a while, then brakes to rest in 5 s. (i) Convert the speeds. (ii) Find acceleration during acceleration. (iii) Find acceleration while braking. (iv) Find the braking distance.", "(i) 10 and 15 m/s (1). (ii) 0.5 m s⁻² (1). (iii) −3 m s⁻² (1). (iv) 15 × 5/2 = 37.5 m (2).", "1+1+1+2"),
 Q("(i) How do you plot a position–time graph? (ii) What does its slope represent? (iii) Compare graphs for uniform and non-uniform motion.", "(i) Time on x-axis, position on y-axis, scale, plot points and join (2). (ii) Velocity (1). (iii) Straight line vs curve (2).", "2+1+2"),
 Q("(i) What does a velocity–time graph show for constant velocity and constant acceleration? (ii) How is acceleration obtained from it? (iii) Find the displacement for 5 m s⁻¹ rising uniformly to 15 m s⁻¹ in 10 s.", "(i) Horizontal line; inclined line (2). (ii) Slope (1). (iii) ½ × (5 + 15) × 10 = 100 m (2).", "2+1+2"),
 Q("<b>Case study:</b> Table: t = 0, 5, 10, 15, 20 s with v = 0, 2.5, 5, 7.5, 10 m s⁻¹. (i) Describe the motion. (ii) Find the acceleration. (iii) Find the displacement in 20 s. (iv) Describe the shape of the v–t graph.", "(i) Velocity increases by equal amounts in equal times — uniform acceleration (1). (ii) 10/20 = 0.5 m s⁻² (1). (iii) ½ × 20 × 10 = 100 m (2). (iv) Straight line through origin (1).", "1+1+2+1"),
 Q("(i) Derive v = u + at. (ii) Derive s = ut + ½at² using the v–t graph. (iii) Derive v² = u² + 2as.", "(i) From a = (v − u)/t (1). (ii) Area of trapezium/rectangle plus triangle (2). (iii) Eliminate t: t = (v − u)/a; s = (v + u)(v − u)/2a (2).", "1+2+2"),
 Q("A car starting from rest accelerates uniformly at 2 m s⁻² for 10 s. (i) Find its final velocity. (ii) Find the distance in 10 s. (iii) It then brakes to rest at 5 m s⁻²; find the braking distance. (iv) Find the total distance.", "(i) 20 m/s (1). (ii) 100 m (1). (iii) 400/10 = 40 m (2). (iv) 140 m (1).", "1+1+2+1"),
 Q("<b>Case study:</b> A driver at 20 m s⁻¹ sees an obstacle 50 m ahead and brakes at 5 m s⁻². (i) Find the stopping distance. (ii) Will the vehicle hit the obstacle? (iii) If speed were 30 m s⁻¹, find the stopping distance. (iv) What do you infer about speed limits?", "(i) 40 m (1). (ii) No, 10 m short (1). (iii) 90 m (2). (iv) Stopping distance rises as the square of speed, so speed limits matter (1).", "1+1+2+1"),
 Q("(i) Define uniform circular motion. (ii) Why is it accelerated? (iii) Show with a marble in a ring that velocity is along the tangent. (iv) State why it is an idealised model.", "(i) Motion along a circle at constant speed (1). (ii) Direction of velocity changes (1). (iii) On removing the ring, the marble moves along a straight tangent (2). (iv) Real motions seldom have exactly constant speed and a perfect circle (1).", "1+1+2+1"),
 Q("A child on a merry-go-round of radius 7 m completes 5 revolutions in 110 s (π = 22/7). (i) Find the distance. (ii) Find the displacement. (iii) Find the average speed. (iv) Find the average velocity.", "(i) 5 × 44 = 220 m (1). (ii) 0 (1). (iii) 220/110 = 2 m s⁻¹ (2). (iv) 0 (1).", "1+1+2+1"),
 Q("<b>Case study:</b> A ball is dropped from a height; its velocity at successive seconds is 9.8, 19.6, 29.4 m s⁻¹. (i) Find the acceleration in each second. (ii) Is it constant? (iii) Name this acceleration. (iv) Find the distance fallen in 3 s.", "(i) 9.8 m s⁻² each (1). (ii) Yes (1). (iii) Acceleration due to gravity (g) (1). (iv) ½ × 9.8 × 9 = 44.1 m (2).", "1+1+1+2"),
 Q("(i) Distinguish scalar and vector with two examples each from this chapter. (ii) List four differences between distance and displacement.", "(i) Scalar: distance, speed; vector: displacement, velocity (acceleration) (2). (ii) Path length vs shortest change in position; scalar vs vector; never zero for moving vs can be zero; ≥ displacement (3).", "2+3"),
 Q("A train of speed 90 km h⁻¹ is brought to rest in 50 s. (i) Convert the speed. (ii) Find retardation. (iii) Find the stopping distance. (iv) What fraction of the distance is covered in the first 25 s?", "(i) 25 m s⁻¹ (1). (ii) 25/50 = 0.5 m s⁻² (1). (iii) s = 25 × 50/2 = 625 m (2). (iv) First 25 s: 25 × 25 − ½ × 0.5 × 25² = 468.75 m, i.e. 3/4 of the total (1).", "1+1+2+1"),
 Q("<b>Case study:</b> Two cars A and B start together; on a position–time graph A is a line of slope 10 m s⁻¹ and B of slope 20 m s⁻¹. (i) Which is faster? (ii) Find the position of each after 6 s. (iii) After how many seconds is B 100 m ahead of A? (iv) What would a horizontal line mean?", "(i) B (1). (ii) A 60 m, B 120 m (2). (iii) Gap grows 10 m per second, so 10 s (1). (iv) The car is at rest (1).", "1+2+1+1"),
 Q("(i) State the conditions under which the kinematic equations are valid. (ii) A motorbike with u = 28 m s⁻¹ stops after 98 m. Find the acceleration. (iii) Find the time taken. (iv) Why is the sign of a negative?", "(i) Straight-line motion with constant acceleration (1). (ii) 0 = 784 + 2a(98), a = −4 m s⁻² (2). (iii) t = 28/4 = 7 s (1). (iv) It acts opposite to the velocity (1).", "1+2+1+1"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
