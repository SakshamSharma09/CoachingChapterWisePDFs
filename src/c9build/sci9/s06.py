from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def fm(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}".rstrip("0").rstrip(".")
def opts(v, u, extra=()):
    v = F(v); c = [v * 2, v / 2, v + 2, v + 5, v * 3, v / 3, v + 10]
    out = []
    for x in list(extra) + c:
        x = F(x)
        if x != v and x > 0 and fm(x) != fm(v) and fm(x) not in out: out.append(fm(x))
    return [f"{o} {u}" for o in out[:3]]
A = []
# F = ma (force) (4)
for m, a in [(5, 4), (10, 3), (2, 6), (50, 2)]:
    f = m * a
    A.append(M4(f"The net force needed to give a body of mass {m} kg an acceleration of {a} m s⁻² is:", f"{f} N", opts(f, "N", [m + a, F(m, a)]), "F = ma"))
# a = F/m (4)
for f, m in [(20, 4), (30, 6), (100, 25), (12, 8)]:
    a = F(f, m)
    A.append(M4(f"A net force of {f} N acts on a body of mass {m} kg. Its acceleration is:", f"{fm(a)} m s⁻²", opts(a, "m s⁻²", [F(m, f), f * m]), "a = F/m"))
# weight (3)
for m in [5, 20, 60]:
    w = m * 10
    A.append(M4(f"The weight of a {m} kg body is (g = 10 m s⁻²):", f"{w} N", opts(w, "N", [m]), "W = mg"))
# net force (4): two forces
for f1, f2, kind in [(10, 6, "opposite"), (8, 8, "opposite"), (12, 5, "same"), (15, 9, "opposite")]:
    n = f1 + f2 if kind == "same" else abs(f1 - f2)
    w = [x for x in dict.fromkeys([f1 + f2 if kind != "same" else abs(f1 - f2), f1 * f2, f1, f2, n + 2]) if x != n][:3]
    A.append(M4(f"Two forces of {f1} N and {f2} N act on a block along the same straight line in {'the same direction' if kind == 'same' else 'opposite directions'}. The magnitude of the net force is:", f"{n} N", [f"{x} N" for x in w], "add if same direction; subtract if opposite"))
# F = ma then a: mass from F,a (2)
for f, a in [(60, 3), (45, 9)]:
    m = f // a
    A.append(M4(f"A force of {f} N produces an acceleration of {a} m s⁻² in a body. Its mass is:", f"{m} kg", opts(m, "kg", [f * a, a]), "m = F/a"))
# velocity after force (2)
for m, f, t in [(2, 6, 4), (5, 10, 3)]:
    v = F(f, m) * t
    A.append(M4(f"A body of mass {m} kg initially at rest is pushed by a net force of {f} N for {t} s. Its final velocity is:", f"{fm(v)} m s⁻¹", opts(v, "m s⁻¹", [f * t, F(f * t, m * 2)]), "a = F/m, v = at"))
A += [
 M4("The SI unit of force is:", "newton", ["joule", "pascal", "watt"], "kg m s⁻²"),
 M4("1 N is the force that gives an acceleration of 1 m s⁻² to a mass of:", "1 kg", ["1 g", "10 kg", "9.8 kg"], "definition"),
 M4("Newton's first law is also called the law of:", "inertia", ["action", "gravitation", "momentum change"], "tendency to resist change"),
 M4("A passenger standing in a bus falls backwards when the bus suddenly starts because of:", "inertia of rest", ["inertia of motion", "friction on the bus", "weight"], "the body tries to remain at rest"),
 M4("Friction acting on a moving object is directed:", "opposite to its motion", ["along its motion", "perpendicular to the surface only", "downwards"], "opposes relative motion"),
 M4("A body moving at constant velocity has net force:", "zero", ["equal to its weight", "equal to mv", "increasing"], "Newton's first law"),
 M4("Which of these is a pair of action–reaction forces?", "Paddle pushes water backwards; water pushes paddle forwards", ["Weight of a book and the normal force on it", "Two tug-of-war teams' pulls on a rope", "Gravity and friction on a car"], "act on two different bodies"),
 M4("Action and reaction forces do not cancel because they:", "act on different objects", ["are unequal", "act in the same direction", "act at different times"], "third law"),
 M4("A gun recoils when a bullet is fired. This is explained by:", "Newton's third law", ["Newton's first law", "law of gravitation", "Hooke's law"], "equal and opposite force"),
 M4("A fielder pulls his hands back while catching a fast ball to:", "increase the time of stopping and reduce the force", ["increase the force", "increase the ball's mass", "decrease the ball's momentum to zero faster"], "smaller acceleration"),
 M4("Airbags in cars protect passengers by:", "increasing the time over which the passenger stops", ["reducing the car's mass", "increasing friction", "making the car stop faster"], "reduces force"),
 M4("Grooves on shoe soles and tyre treads are made to:", "increase friction", ["reduce friction", "reduce weight", "increase speed"], "grip"),
 M4("We can walk because the ground exerts a ______ on our feet in the forward direction.", "force of friction", ["tension", "buoyant force", "magnetic force"], "reaction to backward push"),
 M4("A rocket lifts off because the exhaust gases pushed downwards exert an equal and opposite force which is:", "upward on the rocket and greater than its weight", ["downward on the rocket", "upward but less than its weight", "zero"], "third law"),
 M4("The value of g near the Earth's surface is approximately:", "9.8 m s⁻²", ["6.67 m s⁻²", "98 m s⁻²", "1.6 m s⁻²"], "acceleration due to gravitational force"),
 M4("For the same force, a body with larger mass has:", "smaller acceleration", ["larger acceleration", "the same acceleration", "zero acceleration"], "a ∝ 1/m"),
 M4("Galileo's thought experiment on a smooth horizontal plane suggested that a body:", "keeps moving indefinitely if no friction acts", ["stops immediately", "always needs a force to move", "moves in a circle"], "basis of the first law"),
 M4("Two teams in a tug of war pull with 500 N each and the rope does not move. The forces on the rope are:", "balanced", ["unbalanced", "action–reaction on the rope", "zero on each team"], "net force is zero"),
 M4("An astronaut in free space throws a tool away from her. She will:", "move in the opposite direction", ["move in the same direction", "stay at rest", "spin without moving"], "third law"),
 M4("A body of mass 2 kg is acted on by two forces, 8 N east and 3 N west. Its acceleration is:", "2.5 m s⁻² east", ["5.5 m s⁻² east", "2.5 m s⁻² west", "1.5 m s⁻² east"], "(8 − 3)/2"),
 M4("The momentum of a 2 kg ball moving at 5 m s⁻¹ is:", "10 kg m s⁻¹", ["7 kg m s⁻¹", "2.5 kg m s⁻¹", "25 kg m s⁻¹"], "p = mv"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("State Newton's first law of motion.", "An object at rest remains at rest and an object in motion continues with constant velocity unless a net force acts on it (2).", "2"),
 Q("What is inertia? On what does it depend?", "The tendency of a body to resist a change in its state of rest or uniform motion (1); it depends on mass (1).", "1+1"),
 Q("Why does a passenger lurch forward when a moving bus stops suddenly?", "Inertia of motion: the body tends to continue its motion while the bus stops (2).", "2"),
 Q("State Newton's second law and write its mathematical form.", "Acceleration is proportional to the net force and inversely proportional to mass, in the direction of the force (1); F = ma (1).", "1+1"),
 Q("Define one newton.", "The force that produces an acceleration of 1 m s⁻² in a body of mass 1 kg (2).", "2"),
 Q("Find the force required to accelerate a 1500 kg car at 2 m s⁻².", "F = ma = 1500 × 2 (1) = 3000 N (1).", "1+1"),
 Q("State Newton's third law of motion.", "Whenever one object exerts a force on a second, the second exerts an equal and opposite force on the first (2).", "2"),
 Q("Why do action and reaction not cancel each other?", "They act on two different objects (2).", "2"),
 Q("Why is it difficult to walk on a wet polished floor?", "Friction is very small, so the foot cannot push the ground backwards and the ground cannot push forward enough (2).", "2"),
 Q("A box is pushed with a force equal to the friction acting on it. Will it move with constant velocity? Why?", "Net force is zero, so by the first law it continues at constant velocity if already moving (2).", "2"),
 Q("Find the net force when 10 N and 6 N act on a block in opposite directions.", "Net force = 10 − 6 = 4 N in the direction of the larger force (2).", "2"),
 Q("Why does a fielder draw his hands back while catching a fast ball?", "It increases the time to stop the ball, so the acceleration and force are smaller (2).", "2"),
 Q("Calculate the weight of a 30 kg body (g = 10 m s⁻²).", "W = mg = 30 × 10 = 300 N (2).", "2"),
 Q("What are balanced forces? Give an example.", "Forces which are equal and opposite on the same object so the net force is zero (1); a book at rest on a table (1).", "1+1"),
 Q("How does a rocket move upward?", "The exhaust gases pushed down exert an equal upward force on the rocket, larger than its weight (2).", "2"),
 Q("A bullet of mass 20 g is fired from a gun. Why is the recoil of the gun much smaller in velocity than the bullet's velocity?", "Forces are equal and opposite but the gun is much heavier, so its acceleration is much less (a = F/m) (2).", "2"),
]
C = [
 Q("Describe an activity to show that friction depends on the nature of surfaces.", "Push a stack of coins with a stretched rubber band on different surfaces (1); the distance travelled differs: larger on smoother surfaces (1); so friction is smaller on smooth surfaces (1).", "1+1+1"),
 Q("Explain Galileo's thought experiment that led to the first law.", "A body on a smooth surface travels farther as friction decreases (1.5); in the limit of zero friction it would move forever with constant velocity, so no force is needed to maintain motion (1.5).", "1½+1½"),
 Q("Does a body moving with constant velocity have a net force on it? Explain with the example of a box pushed on a floor.", "No (1); the applied force balances friction, so net force is zero (2).", "1+2"),
 Q("Draw the position–time and velocity–time graphs for a body with no net force and explain.", "At rest: horizontal line at one position, zero velocity (1.5); constant velocity: straight inclined line for position and horizontal line for velocity (1.5).", "1½+1½"),
 Q("A body of mass 10 kg is acted upon by a force of 50 N. Find the acceleration and the distance covered in 4 s from rest.", "a = 50/10 = 5 m s⁻² (1.5); s = ½ × 5 × 16 = 40 m (1.5).", "1½+1½"),
 Q("A car of mass 1000 kg moving at 20 m s⁻¹ is stopped in 5 s. Find the force applied by brakes.", "a = −20/5 = −4 m s⁻² (2); F = 1000 × (−4) = −4000 N, i.e. 4000 N opposite to motion (1).", "2+1"),
 Q("A 25 kg block is pushed with 55 N against a maximum friction of 50 N. Find the acceleration and displacement in 2 s.", "Net force = 5 N, a = 5/25 = 0.2 m s⁻² (2); s = ½ × 0.2 × 4 = 0.4 m (1).", "2+1"),
 Q("Two children of different masses sit on identical swings. For which child will a bigger force be needed for the same acceleration? Why?", "The heavier child; F = ma, so for equal acceleration force is larger for larger mass (3).", "3"),
 Q("Explain with two examples how Newton's second law helps in protecting from injury.", "Airbags and seat belts increase stopping time, reducing acceleration and force (1.5); a fielder pulling hands back while catching a cricket ball (1.5).", "1½+1½"),
 Q("A weightlifter holds a 30 kg barbell steady. Find the force she applies (g = 9.8 m s⁻²).", "Weight = 30 × 9.8 = 294 N (2); she applies an equal upward force of 294 N (1).", "2+1"),
 Q("Explain with a sketch-based example how a canoe moves forward.", "The paddle pushes water backwards (1); water pushes the paddle forwards with an equal force (1); the forces act on different objects, so the canoe moves forward (1).", "1+1+1"),
 Q("Using Newton's third law, explain how we are able to walk.", "The foot pushes the ground backwards (1); friction from the ground acts forward on the foot (1); without friction we would slip (1).", "1+1+1"),
 Q("A 0.1 kg bullet is fired from a 5 kg gun with a force of 2 N. Find the initial accelerations of the bullet and gun.", "Bullet: 2/0.1 = 20 m s⁻² (1.5); gun: 2/5 = 0.4 m s⁻² in the opposite direction (1.5).", "1½+1½"),
 Q("Why does the Earth not appear to move towards a falling fruit although the forces are equal?", "The Earth's mass is huge, so its acceleration a = F/m is negligibly small (3).", "3"),
 Q("Explain the working of a balloon rocket.", "The stretched balloon pushes the air out backwards (1.5); the air exerts an equal force on the balloon forward, so it moves (1.5).", "1½+1½"),
 Q("How can a spacecraft in space with negligible gravity slow down?", "Fire its engine in the direction of motion; exhaust exerts an opposite force on the craft (3).", "3"),
 Q("Two blocks of masses 2 kg and 3 kg joined by a string are pulled on a smooth floor by a 10 N force. Find the acceleration and the tension in the string.", "Total mass 5 kg, a = 10/5 = 2 m s⁻² (1.5); T = 2 × 2 = 4 N (1.5).", "1½+1½"),
 Q("Differentiate between mass and weight.", "Mass: amount of matter, constant, kg, scalar (1.5); weight: gravitational force on the body, depends on g, N, vector (1.5).", "1½+1½"),
 Q("Find the force on a 1500 kg sports car accelerating from rest to 10 m s⁻¹ in 5 s. What force acts when it later comes to rest in 5 s?", "a = 2 m s⁻², F = 3000 N forward (2); on stopping, F = −3000 N (1).", "2+1"),
 Q("Out of 100 oarsmen in a boat, 95 row backwards and 5 row forwards, each applying 200 N. Find the net force on the boat.", "Net = (95 − 5) × 200 = 18 000 N (3).", "3"),
 Q("Why is it said that forces always occur in pairs? Give two examples.", "Every force is an interaction between two objects, giving equal and opposite forces on each (1); hammer–nail and Earth–apple (2).", "1+2"),
 Q("A body of mass 4 kg changes its velocity from 6 m s⁻¹ to 14 m s⁻¹ in 4 s. Find the force.", "a = 8/4 = 2 m s⁻² (1.5); F = 4 × 2 = 8 N (1.5).", "1½+1½"),
 Q("Why do vehicles' tyres have treads and why is driving on a wet road risky?", "Treads increase friction/grip (1.5); water reduces friction so tyres slip and stopping distance rises (1.5).", "1½+1½"),
 Q("Explain what happens if the force of friction disappears from the world.", "Moving objects would never stop, we could not walk, knots and nails would not hold, vehicles could not grip (3).", "3"),
]
D = [
 Q("(i) State Newton's first law. (ii) Describe Galileo's reasoning. (iii) Give two everyday examples of inertia.", "(i) A body continues in rest or uniform motion unless a net force acts (1). (ii) With less friction a body goes farther; with none it would move forever (2). (iii) Passenger lurching when the bus stops; dust shaken off a carpet (2).", "1+2+2"),
 Q("(i) Describe Activity 6.3 to show that acceleration depends on force. (ii) How does mass affect acceleration? (iii) Write the law in the mathematical form.", "(i) A cart pulled by a thread over a pulley with cup masses: doubling the load in the cup increases acceleration (2). (ii) Heavier cart, smaller acceleration (1). (iii) a = F/m or F = ma (2).", "2+1+2"),
 Q("<b>Case study:</b> A student pushes a 25 kg block; maximum friction is 50 N. (i) What happens with a 50 N push? (ii) What is the net force with 55 N? (iii) Find the acceleration. (iv) Find its displacement in 2 s.", "(i) Net force is zero, the block stays at rest (1). (ii) 5 N (1). (iii) 0.2 m s⁻² (1). (iv) ½ × 0.2 × 4 = 0.4 m (2).", "1+1+1+2"),
 Q("(i) State Newton's third law. (ii) Explain with the example of a canoe. (iii) Why do the forces not cancel?", "(i) Every action has an equal and opposite reaction on the other body (1). (ii) Paddle pushes water back, water pushes paddle forward (2). (iii) They act on different objects (2).", "1+2+2"),
 Q("<b>Case study:</b> A sports car of mass 1500 kg moves east: 0 to 10 m s⁻¹ in 5 s, then constant for 5 s, then to rest in 5 s. (i) Find the force in the first 5 s. (ii) Find the net force in the middle interval. (iii) Find the force during braking. (iv) Find the total distance.", "(i) a = 2, F = 3000 N east (1). (ii) 0 (1). (iii) a = −2, F = −3000 N (westwards) (1). (iv) 25 + 50 + 25 = 100 m (2).", "1+1+1+2"),
 Q("(i) Why do airbags and cricket fielders reduce force on impact? (ii) A 0.15 kg ball at 30 m s⁻¹ is stopped in 0.1 s; find the force. (iii) Find the force if stopped in 0.01 s.", "(i) Longer stopping time gives smaller acceleration (1). (ii) a = 300 m s⁻², F = 45 N (2). (iii) a = 3000, F = 450 N (2).", "1+2+2"),
 Q("(i) How does a rocket lift off? (ii) How is the same principle used by the Chandrayaan-3 lander? (iii) Explain with the balloon activity.", "(i) Exhaust gases pushed down; the upward reaction exceeds weight (2). (ii) Engines fire against the direction of motion, slowing it (1). (iii) Air rushes out, balloon moves opposite (2).", "2+1+2"),
 Q("<b>Case study:</b> A 0.1 kg bullet leaves a 5 kg gun with a force of 2 N. (i) What is the recoil force on the gun? (ii) Find the bullet's acceleration. (iii) Find the gun's acceleration. (iv) Explain the difference.", "(i) 2 N (1). (ii) 20 m s⁻² (1). (iii) 0.4 m s⁻² (1). (iv) Same force but different masses (2).", "1+1+1+2"),
 Q("(i) What is friction? (ii) Describe the experiment to compare friction on different surfaces. (iii) How does friction help us to walk?", "(i) Force opposing relative motion between surfaces in contact (1). (ii) Pull a block with a spring balance on surfaces; reading when it just moves is the friction (2). (iii) Foot pushes back, friction pushes forward (2).", "1+2+2"),
 Q("<b>Case study:</b> A car of 800 kg moving at 25 m s⁻¹ stops in 10 s. (i) Find the retardation. (ii) Find the braking force. (iii) Find the stopping distance. (iv) If the speed were doubled for the same force, find the new stopping distance.", "(i) 2.5 m s⁻² (1). (ii) 2000 N (1). (iii) 125 m (2). (iv) 500 m (1).", "1+1+2+1"),
 Q("(i) Explain the system approach for two boxes of m₁ and m₂ pulled by force F. (ii) Find the acceleration for m₁ = 2 kg, m₂ = 3 kg, F = 10 N. (iii) Find the tension.", "(i) Treat both and the string as one object; internal tension is ignored, a = F/(m₁ + m₂) (2). (ii) 2 m s⁻² (1.5). (iii) T = m₂ a = 6 N when box 1 is pulled (1.5).", "2+1½+1½"),
 Q("(i) Distinguish balanced and unbalanced forces. (ii) Two teams pull a rope with 400 N and 300 N. Find the net force and direction. (iii) Which team wins and why?", "(i) Balanced: net force zero; unbalanced: non-zero (2). (ii) 100 N towards the first team (2). (iii) First team, as net force is in its direction (1).", "2+2+1"),
 Q("<b>Case study:</b> A weightlifter holds a barbell of total mass 30 kg (g = 9.8 m s⁻²). (i) What forces act on it? (ii) Find the weight. (iii) Find the force she applies. (iv) What would be the net force?", "(i) Weight downwards, her upward force (1). (ii) 294 N (1). (iii) 294 N upwards (1). (iv) Zero (2).", "1+1+1+2"),
 Q("(i) Differentiate mass and weight. (ii) What is the weight of a 60 kg person on the Earth (g = 10)? (iii) On the Moon where g = 1.6?", "(i) Mass is fixed, weight depends on g (2). (ii) 600 N (1.5). (iii) 96 N (1.5).", "2+1½+1½"),
 Q("(i) State Newton's second law in terms of momentum. (ii) Define momentum. (iii) A 2 kg ball moving at 5 m s⁻¹ is stopped in 0.5 s; find the force.", "(i) Rate of change of momentum is proportional to net force (1). (ii) Product of mass and velocity (1). (iii) Δp = 10, F = 10/0.5 = 20 N (3).", "1+1+3"),
 Q("(i) State the three laws with an example each. (ii) Which law explains why seat belts are essential?", "(i) First: lurch in a bus; second: F = ma for a car; third: rocket launch (3). (ii) First law (inertia) – the body continues moving forward (2).", "3+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
