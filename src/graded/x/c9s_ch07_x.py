"""Class 9 Science Ch 7 Work, Energy and Simple Machines - extras (g = 10 m/s^2)."""
from common import AR4, Q

AR = [
 AR4("No work is done by a person who holds a heavy suitcase while standing still.", "Work is done only when a force produces a displacement of the body in the direction of the force.", "a",
     "There is no displacement, so $W=Fs=0$."),
 AR4("The joule is the SI unit of energy.", "Power is the rate of doing work.", "b",
     "Both are true, but the definition of power does not explain the unit of energy."),
 AR4("When the speed of a body is doubled, its kinetic energy becomes four times.", "The kinetic energy of a body is directly proportional to its speed.", "c",
     "$KE=\\tfrac12mv^2$ varies as the square of the speed, so R is false."),
 AR4("A single fixed pulley has a mechanical advantage greater than 1.", "A fixed pulley changes the direction of the applied force.", "d",
     "The mechanical advantage of a fixed pulley is 1, so A is false; R is true."),
 AR4("At the highest point of a ball thrown upward, its potential energy is maximum.", "At that point its kinetic energy is zero and its mechanical energy is entirely potential (ignoring air resistance).", "a",
     "Since the velocity is zero there, all the energy is potential."),
 AR4("The total mechanical energy of a freely falling body (ignoring air resistance) remains constant.", "The work done by gravity on a falling body is positive.", "b",
     "Both are true, but the sign of the work does not by itself explain conservation of mechanical energy."),
]

CASE = [
 Q("<b>Case study.</b> Ravi, a student of mass 50 kg, climbs the stairs of his school building through a vertical height of 10 m in 20 s. Take $g=10$ m/s$^2$. "
   "(i) Find the gain in his potential energy. (ii) How much work does he do against gravity? (iii) Find his power. (iv) If he climbs the same stairs in 40 s, what is his power, and does the work done change?",
   r"(i) $PE=mgh=50\times10\times10=5000$ J (1). (ii) Work $=5000$ J (1). (iii) $P=W/t=5000/20=250$ W (1). (iv) $P=5000/40=125$ W (1); the work done is unchanged (5000 J), only the rate of doing work changes (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A 2 kg ball is dropped from the roof of a building 20 m high. Ignore air resistance and take $g=10$ m/s$^2$. "
   "(i) Find the potential energy of the ball at the top. (ii) What is its kinetic energy just before it hits the ground? (iii) Find its speed just before it hits the ground. (iv) Find the kinetic energy when it is 5 m above the ground and state what happens to the total mechanical energy.",
   r"(i) $PE=2\times10\times20=400$ J (1). (ii) $KE=400$ J, by conservation of energy (1). (iii) $\tfrac12\times2\times v^2=400$, so $v=20$ m/s (1). (iv) At 5 m: $PE=2\times10\times5=100$ J, so $KE=400-100=300$ J (1); the total mechanical energy stays 400 J (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A mechanic uses a crowbar as a lever to lift a load of 600 N. The effort arm is 1.5 m and the load arm is 0.5 m. The effort end is pushed down through 0.6 m. "
   "(i) Find the mechanical advantage of the lever. (ii) Find the effort required, assuming an ideal lever. (iii) How high does the load rise? (iv) Find the work done by the effort and the work done on the load, and say why the efficiency of a real machine is below 100 per cent.",
   r"(i) $MA=\dfrac{\text{effort arm}}{\text{load arm}}=\dfrac{1.5}{0.5}=3$ (1). (ii) $E=\dfrac{L}{MA}=\dfrac{600}{3}=200$ N (1). (iii) Load rises $0.6/3=0.2$ m (1). (iv) Work by effort $=200\times0.6=120$ J; work on the load $=600\times0.2=120$ J (1); in a real machine some work is lost against friction, so output work is less than input work (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Work", ["$W=F\\,s$ for force along displacement; SI unit joule, $1\\text{ J}=1\\text{ N m}$.",
   "Work is zero if the displacement is zero or the force is perpendicular to the displacement; negative if the force opposes the displacement (e.g. friction).",
   "Work-energy theorem: work done by the net force = change in kinetic energy."]),
 ("Energy", ["Kinetic energy $KE=\\tfrac12mv^2$; potential energy (gravitational) $PE=mgh$.",
   "Law of conservation of energy: energy can neither be created nor destroyed, only changed from one form to another.",
   "Mechanical energy $=KE+PE$ is constant for a freely moving body (no friction): $\\tfrac12mv^2+mgh=\\text{constant}$; speed after falling through $h$ from rest $v=\\sqrt{2gh}$."]),
 ("Power", ["$P=\\dfrac{W}{t}=\\dfrac{E}{t}$; SI unit watt, $1\\text{ W}=1\\text{ J/s}$; $1\\text{ kW}=1000\\text{ W}$.",
   "Commercial unit of energy: $1\\text{ kWh}=1000\\text{ W}\\times3600\\text{ s}=3.6\\times10^{6}\\text{ J}$.",
   "Energy used (kWh) $=$ power (kW) $\\times$ time (h)."]),
 ("Simple machines", ["Mechanical advantage $MA=\\dfrac{\\text{load}}{\\text{effort}}$ (no unit). Lever: $MA=\\dfrac{\\text{effort arm}}{\\text{load arm}}$; principle of moments: effort $\\times$ effort arm = load $\\times$ load arm.",
   "Fixed pulley $MA=1$ (changes direction only); movable pulley $MA=2$; inclined plane $MA=\\dfrac{\\text{length of ramp}}{\\text{height}}$.",
   "A machine allows a smaller effort to move a larger load but does not reduce the work: ideal $W_{\\text{in}}=W_{\\text{out}}$."]),
 ("Efficiency", ["Efficiency $=\\dfrac{\\text{useful work (output)}}{\\text{work put in (input)}}\\times100\\%$; always $<100\\%$ for real machines because of friction."]),
]

MISTAKES = [
 "Saying work is done by holding a load or by pushing a wall; without displacement, work is zero.",
 "Treating work done by friction or by a force perpendicular to the motion (a coolie walking with a load on his head) as positive.",
 "Writing $KE=mv^2$ or taking $KE\\propto v$; doubling the speed makes the kinetic energy four times.",
 "Not converting units: minutes to seconds in $P=W/t$, kW to W, or 20 cm of stairs to metres.",
 "Believing that a machine (lever, ramp) saves work; it only reduces the effort by increasing the distance moved by the effort.",
 "Using $1\\text{ kWh}=1000$ J instead of $3.6\\times10^{6}$ J, or calling kWh a unit of power.",
]
