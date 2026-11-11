"""Class 10 Science Ch 12 Magnetic Effects of Electric Current - extras."""
from common import AR4, Q

AR = [
 AR4(r"Two magnetic field lines never intersect each other.", r"At any point in a magnetic field, the field has only one direction.", "a",
     r"If two lines crossed, there would be two directions of the field at the point of intersection."),
 AR4(r"A solenoid carrying current behaves like a bar magnet.", r"The magnetic field inside a long solenoid is uniform.", "b",
     r"Both true; the field pattern outside is like that of a bar magnet, which is not explained by the uniform field inside."),
 AR4(r"Alternating current changes its direction periodically.", r"The frequency of AC supplied in India is 100 Hz.", "c",
     r"India's AC has frequency 50 Hz (reverses direction every $\tfrac1{100}$ s); R is false."),
 AR4(r"A fuse is connected in the neutral wire of a domestic circuit.", r"A fuse protects the appliances by melting when the current is excessive.", "d",
     r"The fuse is connected in the live wire; A is false, R is true."),
 AR4(r"The metallic body of an electrical appliance is connected to the earth wire.", r"The earth wire provides a low-resistance path for leakage current and prevents electric shocks.", "a",
     r"The leakage current flows to the earth instead of through the user's body."),
 AR4(r"A current-carrying conductor placed perpendicular to a magnetic field experiences a force.", r"The direction of the force reverses when the direction of the current is reversed.", "b",
     r"Both true; R is a further fact about the direction of the force, not a reason for A."),
]

CASE = [
 Q(r"<b>Case study.</b> Rohit placed a compass needle near a straight copper wire connected to a battery through a switch. When the switch was closed, the needle was deflected, and when he reversed the battery connections, the needle was deflected in the opposite direction. "
   r"(i) Name the scientist who first observed this effect. (ii) What does this experiment show? (iii) Name the rule used to find the direction of the magnetic field around a straight current-carrying wire. (iv) If the current in a vertical wire flows upwards, what is the direction of the field lines when seen from above, and how does the field strength change as one moves away from the wire?",
   r"(i) Hans Christian Oersted (1). (ii) An electric current produces a magnetic field around the wire (1). (iii) Right-hand thumb rule (1). (iv) Anticlockwise (concentric circles) as seen from above (1); the field strength decreases as the distance from the wire increases (and increases with current) (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In a laboratory, Sneha connects the ends of a coil of insulated copper wire to a galvanometer. When she pushes a bar magnet rapidly into the coil, the needle of the galvanometer deflects momentarily. The needle returns to zero when the magnet is held at rest inside the coil. "
   r"(i) Name the phenomenon. (ii) Who discovered it? (iii) Why does the needle show no deflection when the magnet is stationary? (iv) State two ways of increasing the induced current.",
   r"(i) Electromagnetic induction (1). (ii) Michael Faraday (1). (iii) Current is induced only when the magnetic field through the coil changes, which does not happen when the magnet is at rest (1). (iv) Move the magnet faster, use a stronger magnet, or increase the number of turns of the coil (any two) (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Mr Gupta is installing a 2 kW geyser at his house in Lucknow, where the supply is 220 V. The electrician connects the geyser through a separate 15 A circuit with a fuse and an earth wire. "
   r"(i) What is the colour of the live wire and the earth wire as per the convention? (ii) Calculate the current drawn by the geyser. (iii) Why is the geyser not connected to the 5 A lighting circuit? (iv) State the function of the fuse and of the earth wire.",
   r"(i) Live wire is red and earth wire is green (1). (ii) $I=P/V=2000/220\approx9.1$ A (1). (iii) The geyser draws about 9 A, more than the 5 A rating of the lighting circuit, which would overheat or blow the fuse (1). (iv) The fuse melts and breaks the circuit when the current is excessive (short circuit or overloading) (1); the earth wire carries leakage current from the metal body to the ground, avoiding shocks (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Magnetic field and field lines", [r"Field lines: closed curves, from N to S outside the magnet and S to N inside; closer lines mean a stronger field; they never intersect; the tangent gives the field direction.",
   r"Oersted: current in a wire deflects a compass needle (current produces a magnetic field). Field around a straight wire: concentric circles; strength increases with current and decreases with distance.",
   r"Right-hand thumb rule: thumb along the current, curled fingers give the field direction. A circular loop: field at the centre is strongest, increases with the number of turns."]),
 ("Solenoid and force", [r"Solenoid: a coil of many circular turns; field lines like those of a bar magnet; field inside is uniform; an iron core makes an electromagnet.",
   r"Force on a conductor: maximum when the current is perpendicular to the field. Fleming's left-hand rule: forefinger = field, middle finger = current, thumb = force (mutually perpendicular).",
   r"Reversing the current or the field reverses the force. Unit of field strength: tesla (T)."]),
 ("Electromagnetic induction", [r"A changing magnetic field through a coil (or a conductor moving in a field) induces an emf and a current.",
   r"Fleming's right-hand rule: thumb = motion, forefinger = field, middle finger = induced current. Faster change or more turns gives greater induced current.",
   r"Generator: converts mechanical energy into electrical energy (rotating coil in a magnetic field). AC reverses direction periodically (India: 50 Hz, i.e. reversal every $\tfrac1{100}$ s); DC flows in one direction."]),
 ("Domestic electric circuits", [r"Supply 220 V in India: live wire (red), neutral (black), earth (green).",
   r"Fuse: low melting point wire in the live wire; melts on overloading or short circuit. Earthing prevents shocks from the metal body. Appliances in parallel.",
   r"Overloading: too many appliances on one circuit. Short circuit: live and neutral wires touch, resistance falls and current rises. $I=\dfrac PV$."]),
]

MISTAKES = [
 r"Mixing up Fleming's left-hand rule (force on a current-carrying conductor) and right-hand rule (induced current in a moving conductor).",
 r"Saying that the field lines inside a magnet go from N to S; outside they go N to S, but inside they go from S to N (closed loops).",
 r"Believing that a stationary magnet inside a coil induces a current; induction requires a <b>change</b> of magnetic field.",
 r"Writing the frequency of Indian AC as 60 Hz or 100 Hz; it is 50 Hz, and the direction reverses every $\tfrac1{100}$ s.",
 r"Connecting the fuse in the neutral or earth wire; the fuse is placed in the live wire.",
 r"Confusing the colours: live is red, neutral is black, and earth wire is green; confusing short circuit with overloading.",
]
