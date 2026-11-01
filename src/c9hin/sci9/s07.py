from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def fm(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}".rstrip("0").rstrip(".")
def opts(v, u, extra=()):
    v = F(v); c = [v * 2, v / 2, v + 10, v * 4, v / 4, v + 5, v * 3]
    out = []
    for x in list(extra) + c:
        x = F(x)
        if x != v and x > 0 and fm(x) != fm(v) and fm(x) not in out: out.append(fm(x))
    return [f"{o} {u}" for o in out[:3]]
A = []
for f, s in [(20, 5), (50, 3), (120, 4), (8, 25)]:
    A.append(M4(f"A constant force of {f} N displaces a body by {s} m in the direction of the force. The work done is:", f"{f*s} J", opts(f * s, "J", [f + s, F(f, s)]), "W = F × s"))
for m, v in [(2, 4), (10, 6), (0.5 and 4, 5), (1000, 10)]:
    k = F(m * v * v, 2)
    A.append(M4(f"The kinetic energy of a body of mass {m} kg moving at {v} m s⁻¹ is:", f"{fm(k)} J", opts(k, "J", [m * v, m * v * v]), "½mv²"))
for m, h in [(2, 5), (5, 10), (10, 3), (0.2 and 4, 20)]:
    u = m * 10 * h
    A.append(M4(f"The potential energy of a {m} kg body at a height of {h} m (g = 10 m s⁻²) is:", f"{u} J", opts(u, "J", [m * h, F(u, 2)]), "mgh"))
for w, t in [(600, 10), (1500, 30), (2000, 8), (900, 3)]:
    p = F(w, t)
    A.append(M4(f"A machine does {w} J of work in {t} s. Its power is:", f"{fm(p)} W", opts(p, "W", [w * t, F(t, w)]), "P = W/t"))
for load, eff in [(300, 100), (500, 125)]:
    ma = F(load, eff)
    A.append(M4(f"A machine lifts a load of {load} N by applying an effort of {eff} N. Its mechanical advantage is:", fm(ma), [fm(x) for x in dict.fromkeys([F(1, ma), ma + 1, ma * 2, ma - 1]) if x != ma][:3], "load ÷ effort"))
for h, L in [(2, 10), (3, 12)]:
    ma = F(L, h)
    A.append(M4(f"A ramp of length {L} m raises a load to a height of {h} m (ignore friction). Its mechanical advantage is:", fm(ma), [fm(x) for x in dict.fromkeys([F(1, ma), ma + 1, ma * 2, L + h]) if x != ma][:3], "L ÷ h"))
for ld, la, ea in [(60, 20, 40), (80, 10, 40)]:
    e = F(ld * la, ea)
    A.append(M4(f"On a lever the load is {ld} N at {la} cm from the fulcrum. To balance it with the effort arm {ea} cm, the effort needed is:", f"{fm(e)} N", opts(e, "N", [ld, ld + la]), "effort × effort arm = load × load arm"))
A += [
 M4("The SI unit of work is:", "joule", ["watt", "newton", "pascal"], "N m"),
 M4("The SI unit of power is:", "watt", ["joule", "newton", "kilowatt-hour"], "1 W = 1 J s⁻¹"),
 M4("A girl carrying a box walks horizontally. The work done by the force holding the box is:", "zero", ["positive", "negative", "mgh"], "force ⟂ displacement"),
 M4("Work done by a goalkeeper in stopping a ball is:", "negative", ["positive", "zero", "infinite"], "force opposes displacement"),
 M4("If the velocity of a vehicle doubles, its kinetic energy becomes:", "four times", ["two times", "half", "same"], "KE ∝ v²"),
 M4("A stretched rubber band stores:", "potential energy", ["kinetic energy", "light energy", "no energy"], "deformed shape"),
 M4("As a body falls freely, its mechanical energy:", "remains constant", ["increases", "decreases", "becomes zero"], "PE converted to KE"),
 M4("A fixed pulley is used to:", "change the direction of the effort", ["reduce the load", "reduce the effort", "increase the work done"], "MA = 1"),
 M4("The mechanical advantage of a fixed pulley is:", "1", ["2", "greater than 2", "less than 1"], "effort = load"),
 M4("A crowbar is a lever of the class in which:", "the fulcrum is between effort and load", ["the load is between fulcrum and effort", "the effort is between fulcrum and load", "there is no fulcrum"], "first class"),
 M4("A wheelbarrow is a lever with the:", "load between fulcrum and effort", ["fulcrum between load and effort", "effort between load and fulcrum", "no load"], "second class"),
 M4("The work-energy theorem states that the work done on a body equals the change in its:", "energy", ["mass", "momentum only", "force"], "W = ΔE"),
 M4("Machines make work easier by changing:", "the magnitude or direction of the force", ["the total work needed", "the energy created", "the law of conservation"], "no energy is created"),
 M4("Which has the same value as 1 J?", "1 kg m² s⁻²", ["1 kg m s⁻²", "1 kg m s⁻¹", "1 kg m⁻¹ s⁻²"], "N × m"),
 M4("Two bodies A and B of masses m and 4m have the same kinetic energy. The ratio of their speeds vA : vB is:", "2 : 1", ["1 : 2", "4 : 1", "1 : 1"], "½mv² = ½(4m)v²"),
 M4("The speed of a child reaching the bottom of a smooth slide of height h depends on:", "h only (and g)", ["the mass of the child", "the shape of the slide", "the time taken"], "v = √(2gh)"),
 M4("Which of the following is an example of a body possessing only potential energy?", "a stretched bow before release", ["a rolling ball", "a flowing river", "a moving car"], "deformation stores energy"),
 M4("1 kilowatt equals:", "1000 W", ["100 W", "10 W", "10 000 W"], "kilo = 10³"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Define work in the scientific sense. Give its SI unit.", "Work = force × displacement in the direction of the force (1); joule (1).", "1+1"),
 Q("Define 1 joule of work.", "Work done when a force of 1 N displaces a body by 1 m in the direction of the force (2).", "2"),
 Q("Under what conditions is the work done by a force zero?", "When force is zero, displacement is zero, or force is perpendicular to displacement (2).", "2"),
 Q("A force of 40 N moves a trolley by 5 m in the direction of the force. Find the work done.", "W = 40 × 5 = 200 J (2).", "2"),
 Q("When is the work done negative? Give an example.", "When force acts opposite to displacement (1); goalkeeper stopping a ball (1).", "1+1"),
 Q("State the work-energy theorem.", "Work done on an object equals the change in its energy (2).", "2"),
 Q("Write the expressions for kinetic and gravitational potential energies.", "KE = ½mv² (1); PE = mgh (1).", "1+1"),
 Q("Calculate the kinetic energy of a 0.2 kg ball moving at 10 m s⁻¹.", "½ × 0.2 × 100 = 10 J (2).", "2"),
 Q("Find the potential energy of a 5 kg body at a height of 4 m (g = 10 m s⁻²).", "mgh = 5 × 10 × 4 = 200 J (2).", "2"),
 Q("State the law of conservation of mechanical energy for a freely falling body.", "In the absence of other forces, the sum of KE and PE stays constant (2).", "2"),
 Q("Define power. Give the SI unit.", "Rate of doing work (1); watt (1).", "1+1"),
 Q("A weightlifter lifts 75 kg through 2 m in 5 s. Find the power (g = 10).", "W = 75 × 10 × 2 = 1500 J (1); P = 1500/5 = 300 W (1).", "1+1"),
 Q("Define mechanical advantage.", "The ratio of load to effort (2).", "2"),
 Q("What is the use of a fixed pulley?", "It changes the direction of effort, making pulling down convenient; MA = 1 (2).", "2"),
 Q("What are the three parts of a lever?", "Fulcrum, load, effort (2).", "2"),
 Q("State the principle of the lever.", "Effort × effort arm = load × load arm (2).", "2"),
]
C = [
 Q("A girl lifts a dumbbell up and then lowers it. When is positive work done and when negative?", "Lifting: force and displacement are upward, so positive (1.5); lowering: force upward, displacement downward, so negative (1.5).", "1½+1½"),
 Q("Explain why no work is done when you push hard against a wall.", "Displacement is zero (1.5); the tiredness is due to the use of internal body energy (1.5).", "1½+1½"),
 Q("A goalkeeper stops a ball with a force of 200 N, her hands moving back 15 cm. Find the work done on the ball.", "Force opposes displacement (1); W = 200 × (−0.15) (1) = −30 J (1).", "1+1+1"),
 Q("Derive the expression for kinetic energy.", "W = Fs = ma·s with v² = u² + 2as gives W = ½m(v² − u²) (2); from rest, KE = ½mv² (1).", "2+1"),
 Q("The velocity of a vehicle is doubled. How does its kinetic energy change? Explain.", "KE = ½mv²; with 2v it becomes 4 × ½mv² (3).", "3"),
 Q("A 0.2 kg cricket ball is bowled at 43 m s⁻¹. Find its kinetic energy.", "½ × 0.2 × 43² (2) = 184.9 J (1).", "2+1"),
 Q("Derive the expression for gravitational potential energy.", "Force to lift slowly = mg (1); work = mg × h (1); stored as PE = mgh (1).", "1+1+1"),
 Q("A fielder throws a 200 g ball 10 m high. Find its PE at the highest point and its speed on returning to the ground (g = 10).", "PE = 0.2 × 10 × 10 = 20 J (1.5); ½mv² = 20 ⇒ v = √200 ≈ 14.1 m s⁻¹ (1.5).", "1½+1½"),
 Q("Show that the mechanical energy is conserved for a freely falling body at the initial and final points.", "At height h: PE = mgh, KE = 0 (1); just before ground: PE = 0, KE = ½mv² = mgh since v² = 2gh (2).", "1+2"),
 Q("Explain the energy changes in a swinging pendulum.", "At extreme positions PE is maximum and KE zero (1); at the lowest point KE is maximum and PE minimum (1); the total is nearly constant, losses are due to friction and air (1).", "1+1+1"),
 Q("A child slides down a smooth slide of height 2.5 m. Find the speed at the bottom (g = 10).", "mgh = ½mv² (1); v² = 2 × 10 × 2.5 = 50 (1); v ≈ 7.07 m s⁻¹ (1).", "1+1+1"),
 Q("Name the energy transformation in: (i) a glowing bulb (ii) a ringing bell (iii) photosynthesis.", "(i) electrical → light and heat (1); (ii) mechanical → sound (1); (iii) light → chemical (1).", "1+1+1"),
 Q("Two bodies of masses m and 4m have the same KE. Find the ratio of their speeds.", "½mv₁² = ½(4m)v₂² ⇒ v₁² = 4v₂² (2); v₁ : v₂ = 2 : 1 (1).", "2+1"),
 Q("A crane lifts a mass to the 10th floor in time t, then to the 20th floor in 2t. Compare the work and power.", "Work doubles (1.5); power is the same (W/t = 2W/2t) (1.5).", "1½+1½"),
 Q("A car of mass 1000 kg reaches 72 km h⁻¹ from rest in 10 s. Find the power.", "v = 20 m s⁻¹, KE = 200 000 J (2); P = 20 000 W (1).", "2+1"),
 Q("Differentiate between potential and kinetic energy with an example each.", "KE is due to motion, e.g. a rolling ball (1.5); PE is due to position or shape, e.g. a stretched spring (1.5).", "1½+1½"),
 Q("A person raises a 30 cm step with a 40 cm wide ramp. Find the length of the ramp and the mechanical advantage.", "L = √(30² + 40²) = 50 cm (1.5); MA = 50/30 = 1.67 (1.5).", "1½+1½"),
 Q("Why is climbing an inclined plank easier than lifting a load vertically? Does it save work?", "Effort is smaller because it is applied over a longer distance (2); work done (ignoring friction) is the same (1).", "2+1"),
 Q("Why are roads on hills made to wind around?", "A longer path means a smaller slope, hence a larger MA and less effort (3).", "3"),
 Q("Classify the levers: scissors, wheelbarrow and tweezers.", "Scissors: fulcrum between (1); wheelbarrow: load between (1); tweezers: effort between (1).", "1+1+1"),
 Q("On a seesaw a 15 kg child sits 2 m from the fulcrum. Where must a 30 kg child sit to balance it?", "15 × 2 = 30 × d (2); d = 1 m (1).", "2+1"),
 Q("State two kinds of energy transfer other than doing work.", "Heat transfer from hot to cold bodies (1.5); radiation, e.g. the Sun's energy (1.5).", "1½+1½"),
 Q("A truck of mass 10 000 kg moving at 20 m s⁻¹ enters a sand ramp. Find its initial kinetic energy and explain how it stops.", "KE = ½ × 10 000 × 400 = 2 × 10⁶ J (2); the sand does negative work and the truck gains PE (1).", "2+1"),
 Q("Why can a perpetual-motion machine not exist?", "Real machines lose energy to friction and air resistance as heat and sound, so they slow down; energy cannot be created (3).", "3"),
]
D = [
 Q("(i) Define work and joule. (ii) When is work zero, positive or negative? (iii) A force of 25 N moves a body 6 m; find the work.", "(i) W = F s; 1 J = 1 N × 1 m (2). (ii) Zero: F = 0, s = 0 or F ⟂ s; positive: along; negative: opposite (2). (iii) 150 J (1).", "2+2+1"),
 Q("<b>Case study:</b> A girl lifts a 5 kg bag to 1 m, then three bags together to 1 m, and a single bag to 3 m. (i) Compare the work in the three cases. (ii) Find the work for one bag (g = 10). (iii) Explain the relation between work, force and distance.", "(i) 1 : 3 : 3 (2). (ii) 50 J (1). (iii) Work increases in proportion to force and to displacement (2).", "2+1+2"),
 Q("(i) State the work-energy theorem. (ii) Derive the expression for kinetic energy. (iii) Find the speed of a 15 000 kg aircraft stopped within 100 m by a force of 367 500 N.", "(i) Work = change in energy (1). (ii) W = ½m(v² − u²), KE = ½mv² (2). (iii) ½·15000·v² = 367500·100 ⇒ v = 70 m s⁻¹ (2).", "1+2+2"),
 Q("(i) Derive PE = mgh. (ii) Describe the sand-bed activity to show that PE depends on height. (iii) What is meant by conservation of mechanical energy?", "(i) Work to lift = mg × h (1.5). (ii) Dropping a ball from larger heights makes deeper depressions (2). (iii) KE + PE is constant when no external force acts (1.5).", "1½+2+1½"),
 Q("<b>Case study:</b> A ball of mass 0.5 kg is dropped from 20 m (g = 10). (i) Find its initial PE. (ii) Find its speed on reaching the ground. (iii) Find its KE at 10 m above the ground. (iv) State the principle used.", "(i) 100 J (1). (ii) v = √(2 × 10 × 20) = 20 m s⁻¹ (2). (iii) PE = 50 J, so KE = 50 J (1). (iv) Conservation of mechanical energy (1).", "1+2+1+1"),
 Q("(i) Describe the pendulum activity for conservation of energy. (ii) Why does a real pendulum stop? (iii) Name the energy at the extreme and mean positions.", "(i) A bob released from a point rises to nearly the same height on the other side (2). (ii) Friction at the support and air resistance convert energy to heat (2). (iii) Extreme: PE; mean: KE (1).", "2+2+1"),
 Q("(i) Define power and write its SI unit. (ii) Differentiate work and power. (iii) A motor lifts 120 kg through 15 m in 20 s. Find its power (g = 10).", "(i) P = W/t, watt (1). (ii) Work is the energy transferred; power is its rate (2). (iii) W = 18 000 J; P = 900 W (2).", "1+2+2"),
 Q("<b>Case study:</b> A student of mass 40 kg is lifted by a lift to the top of a 72.5 m building, then later climbs the stairs. (i) Find the gain in PE in the lift (g = 10). (ii) Find the gain by stairs. (iii) What do you conclude? (iv) If the stair climb takes 100 s, find the power.", "(i) 40 × 10 × 72.5 = 29 000 J (1). (ii) 29 000 J (1). (iii) PE depends only on the height, not the path (1). (iv) 290 W (2).", "1+1+1+2"),
 Q("(i) What are simple machines? (ii) Define mechanical advantage. (iii) Describe the fixed and movable pulleys.", "(i) Devices that make work easier by changing the magnitude or direction of a force (1). (ii) Load/effort (1). (iii) Fixed: only changes the direction, MA = 1; movable: MA > 1, lifts heavy loads with less effort (3).", "1+1+3"),
 Q("(i) Describe how an inclined plane makes work easier. (ii) Derive its mechanical advantage. (iii) A load of 500 N is raised 2 m using a 10 m long smooth ramp. Find the effort.", "(i) A longer path means a smaller force, but the same work (1). (ii) F′L = mgh ⇒ MA = mg/F′ = L/h (2). (iii) MA = 5, effort = 100 N (2).", "1+2+2"),
 Q("<b>Case study:</b> On a seesaw a child of 20 kg sits 3 m from the fulcrum. (i) Find the moment of the child's weight (g = 10). (ii) At what distance should a 30 kg child sit? (iii) Which class of lever is a seesaw? (iv) What happens if the 30 kg child sits at 3 m?", "(i) 200 × 3 = 600 N m (1). (ii) 300 × d = 600 ⇒ d = 2 m (2). (iii) First class (1). (iv) The heavier child's side goes down (1).", "1+2+1+1"),
 Q("(i) State the principle of the lever. (ii) Describe the beam balance activity. (iii) Classify levers with examples.", "(i) Effort × effort arm = load × load arm (1). (ii) Coins in the pans; the heavier pan moved closer to balance (2). (iii) I: scissors; II: wheelbarrow; III: tweezers (2).", "1+2+2"),
 Q("<b>Case study:</b> A truck of 10 000 kg moving at 72 km h⁻¹ enters an escape ramp inclined at 30°, with sand exerting 50 000 N. (i) Find its speed in m s⁻¹. (ii) Find its initial KE. (iii) Find the length of the ramp it needs. (iv) Why are escape ramps made of sand?", "(i) 20 m s⁻¹ (1). (ii) 2 × 10⁶ J (1). (iii) 2 × 10⁶ = 50 000 d + 10 000 × 10 × d/2 ⇒ d = 20 m (2). (iv) Sand gives a large opposing force and dissipates energy (1).", "1+1+2+1"),
 Q("(i) List the different forms of energy with one example each. (ii) Explain energy conversion in a hydroelectric plant. (iii) What is the gharat or panchakki?", "(i) Mechanical, heat, light, sound, electrical, chemical, nuclear (3). (ii) Water's PE → KE → turbine → electrical (1). (iii) A water-driven mill that uses falling water to turn a grinding stone (1).", "3+1+1"),
 Q("(i) Explain why the total work cannot be reduced by a machine. (ii) A man pushes a 100 kg load up a 5 m long ramp 1 m high (g = 10); find the effort without friction. (iii) What is the work done?", "(i) Energy is conserved; machines only change force/direction (1). (ii) F × 5 = 1000 × 1, F = 200 N (2). (iii) 1000 J (2).", "1+2+2"),
 Q("(i) Distinguish negative from positive work with two examples. (ii) A scooter of mass 160 kg reaches speed v in the same time with and without a 40 kg passenger; find the ratio of fuel used.", "(i) Positive: pushing a wheelchair; negative: friction on a sliding coin (2). (ii) Energy ∝ mass: 160 : 200 = 4 : 5 (3).", "2+3"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
