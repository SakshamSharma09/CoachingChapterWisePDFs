"""Class 9 Science Ch 6 How Forces Affect Motion - extras (g = 10 m/s^2)."""
from common import AR4, Q

AR = [
 AR4("Passengers in a bus jerk forward when the bus stops suddenly.", "The lower part of the body stops with the bus, while the upper part tends to remain in motion because of inertia.", "a",
     "This is inertia of motion, which is the reason for the forward jerk."),
 AR4("The SI unit of force is the newton.", "Momentum is the product of the mass and the velocity of a body.", "b",
     "Both are true, but they are unrelated statements."),
 AR4("The mass of a body is the same everywhere, whereas its weight changes from place to place.", "The weight of a body is independent of the acceleration due to gravity.", "c",
     "$W=mg$, so weight depends on $g$; R is false."),
 AR4("Action and reaction forces cancel each other because they are equal and opposite.", "Action and reaction forces act on different bodies.", "d",
     "Forces can cancel only if they act on the same body, so A is false; R is true."),
 AR4("A gun recoils backward when a bullet is fired from it.", "The total momentum of the gun and bullet is zero before firing and remains zero afterwards, so the gun gets momentum opposite to that of the bullet.", "a",
     "Conservation of momentum explains the recoil."),
 AR4("Rolling friction is less than sliding friction.", "Friction always opposes the relative motion between surfaces in contact.", "b",
     "Both are true; R does not explain why rolling friction is smaller."),
]

CASE = [
 Q("<b>Case study.</b> A porter at a railway station pushes a loaded trolley of mass 20 kg on a level platform with a horizontal force of 50 N. The platform exerts a friction force of 10 N opposing the motion. Take $g=10$ m/s$^2$. "
   "(i) Find the weight of the trolley. (ii) Find the net force on it. (iii) Find its acceleration. (iv) If the trolley starts from rest, find its velocity and the distance travelled after 5 s.",
   r"(i) $W=mg=20\times10=200$ N (1). (ii) $50-10=40$ N (1). (iii) $a=F/m=40/20=2$ m/s$^2$ (1). (iv) $v=at=2\times5=10$ m/s (1); $s=\tfrac12at^2=\tfrac12\times2\times25=25$ m (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A cricket ball of mass 0.15 kg moving at 30 m/s is caught by a fielder in Chennai. If he stops the ball in 0.05 s with stiff hands, the hands sting. A coach advises him to pull his hands back while catching, which makes the stopping time 0.15 s. "
   "(i) Find the momentum of the ball before it is caught. (ii) Find the average force on the hands if the ball is stopped in 0.05 s. (iii) Find the force if the stopping time is 0.15 s. (iv) Name the law used and explain why pulling the hands back reduces the force.",
   r"(i) $p=mv=0.15\times30=4.5$ kg m/s (1). (ii) $F=\dfrac{4.5-0}{0.05}=90$ N (1). (iii) $F=\dfrac{4.5}{0.15}=30$ N (1). (iv) Newton's second law, $F=\Delta p/\Delta t$ (1); the change of momentum is the same, but a longer time gives a smaller rate of change, hence a smaller force (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A rifle of mass 4 kg fires a bullet of mass 20 g at a speed of 200 m/s. The shooter feels the rifle push back against the shoulder. "
   "(i) What is the total momentum of the rifle and bullet before firing? (ii) Find the momentum of the bullet. (iii) Find the recoil velocity of the rifle. (iv) Explain why the speed of the rifle is much smaller than that of the bullet, and state its direction.",
   r"(i) Zero (both at rest) (1). (ii) $0.02\times200=4$ kg m/s (1). (iii) By conservation of momentum, $4\times v+4=0$, so $v=-1$ m/s, i.e. 1 m/s (1). (iv) The momenta are equal in size and the rifle has a much larger mass, so $v=p/m$ is small (1); the rifle moves opposite to the bullet (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Newton's laws", ["First law (law of inertia): a body remains at rest or in uniform motion in a straight line unless an external unbalanced force acts on it. Inertia depends on mass.",
   "Second law: the rate of change of momentum is proportional to the applied force, in the direction of the force: $F=\\dfrac{\\Delta p}{\\Delta t}=ma$.",
   "Third law: to every action there is an equal and opposite reaction; the two forces act on <i>different</i> bodies."]),
 ("Force, momentum and weight", ["SI unit of force: newton, $1\\text{ N}=1\\text{ kg m/s}^2$.",
   "Momentum $p=mv$ (kg m/s), a vector in the direction of velocity.",
   "Weight $W=mg$ (in N); $g\\approx10\\text{ m/s}^2$ on Earth, about one-sixth of this on the Moon; mass is constant, weight varies with $g$."]),
 ("Conservation of momentum", ["In an isolated system, total momentum before = total momentum after: $m_1u_1+m_2u_2=m_1v_1+m_2v_2$.",
   "Recoil of a gun (both initially at rest): $0=mv+MV$, so $V=-\\dfrac{mv}{M}$.",
   "Rocket: hot gases ejected backward give the rocket momentum forward."]),
 ("Friction", ["Friction opposes the relative motion (or tendency of motion) between surfaces in contact; it depends on the nature of surfaces and the normal force.",
   "Rolling friction $<$ sliding friction; static friction $\\ge$ sliding friction.",
   "Reduced by lubricants, polishing, ball bearings, wheels. Useful for walking, gripping, braking."]),
 ("Applications of $F=ma$", ["Net force $F_{\\text{net}}=F_{\\text{applied}}-f$ when friction $f$ opposes the motion.",
   "Impulse $=F\\Delta t=\\Delta p$; increasing the time of impact reduces the force (cricket catch, air bags)."]),
]

MISTAKES = [
 "Using mass in kg as weight in N (a 5 kg body weighs 50 N when $g=10$), or saying that the mass of a body changes on the Moon.",
 "Using the applied force instead of the <i>net</i> force in $F=ma$ when friction acts.",
 "Saying that action and reaction cancel; they are equal and opposite but act on two different bodies.",
 "Forgetting to convert grams to kilograms (a 20 g bullet is 0.02 kg) in momentum and recoil problems.",
 "Dropping the negative sign (direction) of recoil velocity, or believing that a heavier gun recoils faster; recoil speed is inversely proportional to the gun's mass.",
 "Confusing inertia of rest with inertia of motion, or thinking that inertia depends on speed; it depends only on mass.",
]
