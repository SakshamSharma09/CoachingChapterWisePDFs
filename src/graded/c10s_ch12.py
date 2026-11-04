"""Class 10 Science Ch 12 - Magnetic Effects of Electric Current (hand-written graded banks).
Scope: magnetic field and field lines, field due to a current-carrying straight wire and solenoid,
force on a current-carrying conductor (Fleming's left-hand rule), electromagnetic induction,
generator, AC/DC, domestic circuits. The electric motor is NOT included (not in the assessed syllabus)."""
from scix import tier

SLUG, NAME, CHNO = "Magnetic_Effects_of_Current", "Magnetic Effects of Electric Current", 12

# ============================ NCERT-TYPE ============================
nA = """
The magnetic field lines outside a bar magnet are directed ~~ from the north pole to the south pole ~~ from the south pole to the north pole ~~ along the magnet only ~~ in no definite direction ~~ By convention, outside the magnet.
Magnetic field lines inside a bar magnet go from ~~ the south pole to the north pole ~~ the north pole to the south pole ~~ one side to the other randomly ~~ do not exist ~~ They form closed loops.
Two magnetic field lines ~~ never intersect each other ~~ intersect at the poles ~~ intersect at the centre ~~ intersect often ~~ Two directions at a point are impossible.
The strength of a magnetic field is indicated by ~~ the closeness of the field lines ~~ the colour of the lines ~~ the length of the lines ~~ the number of poles ~~ Crowded lines mean a strong field.
A compass needle is deflected when placed near a current-carrying wire. This was observed by ~~ Oersted ~~ Faraday ~~ Ampere ~~ Fleming ~~ Hans Christian Oersted in 1820.
The magnetic field produced by a straight current-carrying wire has field lines in the form of ~~ concentric circles around the wire ~~ straight lines parallel to the wire ~~ radial lines ~~ ellipses ~~ Circles centred on the wire.
The direction of the magnetic field around a straight wire is given by ~~ the right-hand thumb rule ~~ Fleming's left-hand rule ~~ Fleming's right-hand rule ~~ Lenz's rule ~~ Thumb along current, fingers show the field.
The magnetic field at a point due to a straight current-carrying wire ~~ decreases as the distance from the wire increases ~~ increases as the distance increases ~~ is independent of distance ~~ is zero everywhere ~~ Field is stronger nearer.
The magnetic field produced by a current-carrying wire at a given point depends on ~~ the current and the distance from the wire ~~ the colour of the wire ~~ the length of the wire only ~~ the voltage only ~~ Increases with the current.
The magnetic field inside a long current-carrying solenoid is ~~ nearly uniform ~~ zero ~~ increasing along the axis ~~ circular ~~ Parallel straight lines inside.

The field pattern of a solenoid is similar to that of ~~ a bar magnet ~~ a straight wire ~~ a horseshoe magnet only ~~ a plane mirror ~~ One end behaves as N and the other as S.
A soft iron core inside a solenoid ~~ makes an electromagnet ~~ reduces the field ~~ stops the current ~~ has no effect ~~ The core becomes magnetised.
An electromagnet is made of ~~ soft iron wrapped with a coil carrying current ~~ steel only ~~ copper only ~~ plastic ~~ It is a temporary magnet.
The strength of an electromagnet can be increased by ~~ increasing the current or the number of turns ~~ decreasing the current ~~ removing the core ~~ using a thicker iron-free coil ~~ More turns, more current.
A current-carrying conductor placed in a magnetic field experiences ~~ a force ~~ no force ~~ only heating ~~ a decrease in current ~~ This was shown by Andre-Marie Ampere.
The force on a current-carrying conductor is maximum when the current is ~~ perpendicular to the magnetic field ~~ parallel to the field ~~ at 30 degrees ~~ zero ~~ At right angles the force is greatest.
The direction of force on a current-carrying conductor is given by ~~ Fleming's left-hand rule ~~ Fleming's right-hand rule ~~ Ohm's law ~~ Snell's law ~~ Thumb, forefinger and middle finger.
In Fleming's left-hand rule, the thumb points in the direction of ~~ the force (motion) ~~ the field ~~ the current ~~ the induced emf ~~ Forefinger: field; middle finger: current.
In Fleming's left-hand rule, the middle finger points in the direction of ~~ current ~~ force ~~ field ~~ velocity ~~ Mutually perpendicular fingers.
A positively charged particle moving perpendicular to a magnetic field experiences a force that is ~~ perpendicular to both ~~ along the field ~~ along the velocity ~~ zero ~~ By Fleming's left-hand rule.

Electromagnetic induction is the production of ~~ induced current in a coil due to a changing magnetic field ~~ a magnetic field by a steady current ~~ force on a coil ~~ heat by current ~~ It was discovered by Faraday.
The phenomenon of electromagnetic induction was discovered by ~~ Michael Faraday ~~ Oersted ~~ Ampere ~~ Newton ~~ Faraday, 1831.
An induced current is produced in a coil when ~~ a magnet is moved towards or away from it ~~ a magnet is held still near it ~~ the coil is kept in a steady field at rest ~~ a battery is disconnected ~~ Relative motion changes the flux.
The direction of the induced current is given by ~~ Fleming's right-hand rule ~~ Fleming's left-hand rule ~~ Ohm's law ~~ Joule's law ~~ Thumb: motion; forefinger: field; middle finger: current.
An electric generator converts ~~ mechanical energy into electrical energy ~~ electrical energy into mechanical energy ~~ heat into light ~~ chemical energy into electrical energy ~~ It works on electromagnetic induction.
In a generator, the armature coil rotates in ~~ a magnetic field ~~ an electric field ~~ a gravitational field only ~~ vacuum ~~ Between the poles of a magnet.
The current that changes direction periodically is ~~ alternating current ~~ direct current ~~ static current ~~ steady current ~~ AC.
The frequency of AC supplied in India is ~~ 50 Hz ~~ 60 Hz ~~ 100 Hz ~~ 25 Hz ~~ It reverses direction every 1/100 second.
In a household circuit, the wire with red insulation is the ~~ live wire ~~ neutral wire ~~ earth wire ~~ fuse wire ~~ Standard colour code.
The earth wire is connected to ~~ the metal body of the appliance ~~ the live terminal ~~ the neutral terminal ~~ the fuse ~~ For safety against electric shocks.
""".strip()
nB = """
State the rule to find the direction of the magnetic field around a straight current-carrying wire. ~~ Right-hand thumb rule: hold the wire in the right hand with the thumb along the current|1 ~~ Curled fingers show the direction of the field|1
List any two properties of magnetic field lines. ~~ They start from N and end at S outside the magnet (closed loops)|1 ~~ No two field lines cross; closeness indicates strength|1
What is an electromagnet? Give one use. ~~ A soft iron core wound with a current-carrying coil|1 ~~ Used to lift scrap iron or in electric bells|1
Why does a compass needle get deflected near a current-carrying wire? ~~ Wire produces a magnetic field|1 ~~ The field acts on the needle|1
Name the rule to find the direction of the force on a current-carrying conductor and state it. ~~ Fleming's left-hand rule|1 ~~ Forefinger: field; middle finger: current; thumb: force|1
What is electromagnetic induction? ~~ Production of current in a coil by a changing magnetic field|1 ~~ Faraday's discovery|1
State Fleming's right-hand rule. ~~ Thumb: motion of conductor; forefinger: magnetic field|1 ~~ Middle finger: induced current|1
What is the function of an earth wire? ~~ It carries leakage current to the ground|1 ~~ It prevents electric shocks|1
State two advantages of AC over DC. ~~ AC can be transmitted over long distances with less loss of energy|1 ~~ It is cheaper to generate and distribute AC on a large scale|1
What is a short circuit? ~~ Live and neutral wires touch each other|1 ~~ The current suddenly becomes very large|1
What do you mean by overloading? ~~ Too many appliances are connected to a single socket|1 ~~ The current drawn exceeds the safe limit|1
Name the two parts of a simple generator that cause the current to be taken out. ~~ Slip rings|1 ~~ Brushes|1
""".strip()
nC = """
Draw (describe) the magnetic field lines around a bar magnet and state three properties. ~~ Lines emerge from N and merge at S outside the magnet|1 ~~ They form closed loops|1 ~~ Closer lines mean a stronger field and no two lines intersect|1
Describe Oersted's experiment and state the conclusion. ~~ A compass needle is placed near a wire|1 ~~ When current flows, the needle is deflected|1 ~~ Electric current produces a magnetic field|1
How does the magnetic field due to a straight wire change when (a) the current is increased (b) the distance from the wire is increased? ~~ (a) Field increases with current|1 ~~ (b) Field decreases with distance|1 ~~ The deflection of the compass needle varies accordingly|1
What is a solenoid? State the nature of its magnetic field. ~~ A coil of many circular turns of insulated wire in the shape of a cylinder|1 ~~ Field inside is uniform and parallel to the axis|1 ~~ Outside, the pattern resembles that of a bar magnet|1
List the factors on which the strength of the magnetic field of a solenoid depends. ~~ Magnitude of the current|1 ~~ Number of turns per unit length|1 ~~ Nature of the core material (soft iron increases it)|1
A current-carrying conductor is placed perpendicular to the magnetic field. What will happen if the direction of the current is reversed? ~~ The force acts on the conductor|1 ~~ Reversing the current reverses the force|1 ~~ The conductor is displaced in the opposite direction|1
A proton enters a magnetic field perpendicular to it. State what happens and the direction of force. ~~ A force acts on it|1 ~~ The force is perpendicular to the velocity and field|1 ~~ Its path becomes curved|1
State Fleming's left-hand rule with the help of the three fingers. ~~ Stretch the thumb, forefinger and middle finger mutually perpendicular|1 ~~ Forefinger: field; middle finger: current|1 ~~ Thumb: force|1
State the difference between an electric generator and the process of electromagnetic induction. ~~ EMI is the phenomenon of induction|1 ~~ A generator is a device based on it|1 ~~ Generator converts mechanical energy to electrical energy|1
Describe an activity to show the electromagnetic induction using a coil and a magnet. ~~ Connect a coil to a galvanometer|1 ~~ Move a bar magnet towards or away from the coil|1 ~~ The galvanometer shows deflection only during the motion|1
What is the difference between AC and DC? ~~ DC flows in one direction only|1 ~~ AC reverses its direction periodically|1 ~~ Example: cell gives DC; mains supply gives AC|1
Why is AC preferred for power transmission? ~~ Much less energy is lost in the lines over long distances|1 ~~ AC is easily generated in large power stations|1 ~~ DC cannot be sent economically over such distances|1
What are the colour codes of the live, neutral and earth wires? ~~ Live: red|1 ~~ Neutral: black|1 ~~ Earth: green|1
How does a fuse protect the circuit from overloading? ~~ Fuse is connected in series with the live wire|1 ~~ Excess current melts its wire|1 ~~ The circuit breaks and appliances are saved|1
Why is the metal body of an appliance earthed? ~~ If the live wire touches the body, current flows to the earth|1 ~~ The user does not get a shock|1 ~~ The earth wire has very low resistance|1
How does a magnetic field exert a force on a current-carrying conductor? Name the physical quantities that affect the force. ~~ Field of the conductor interacts with the external field|1 ~~ Larger current gives a larger force|1 ~~ Strength of the field and the angle with it also matter|1
What is the direction of the field inside a solenoid when the current flows clockwise as seen from one end? State the rule you used. ~~ Clockwise at an end looks like the south pole|1 ~~ Field inside is directed away from that end|1 ~~ Right-hand rule for the solenoid|1
Mention two sources of overloading in a household circuit and the safety measures. ~~ Too many appliances on a single socket|1 ~~ Accidental rise in supply voltage|1 ~~ Use of a fuse or MCB to prevent damage|1
""".strip()
nD = """
Describe an activity to show that a current-carrying wire produces a magnetic field around it. State the right-hand thumb rule. ~~ Place a compass near a straight wire passing through a card|1 ~~ Switch on the current: the needle deflects|1 ~~ Reversing the current reverses the deflection|1 ~~ Iron filings form concentric circles|1 ~~ Right-hand thumb rule gives the direction|1
Describe the magnetic field due to a current-carrying solenoid with the field pattern. Explain how it is used to make an electromagnet. ~~ Field is like that of a bar magnet|1 ~~ Uniform field inside, parallel to the axis|1 ~~ Soft iron core placed inside the solenoid|1 ~~ Core becomes strongly magnetised|1 ~~ Electromagnet is temporary: it works only while the current flows|1
State the rule to find the direction of force on a current-carrying conductor. A conductor is placed in a field directed vertically downwards and the current flows from east to west. Find the direction of the force. ~~ Fleming's left-hand rule|1 ~~ Forefinger along the field (down)|1 ~~ Middle finger along the current (west)|1 ~~ Thumb gives the force|1 ~~ The force acts towards the south|1
Describe Faraday's experiments showing electromagnetic induction. State the conditions for the induced current. ~~ A coil is connected to a galvanometer|1 ~~ A magnet is moved in and out of the coil|1 ~~ Deflection occurs only during the motion|1 ~~ Faster motion gives a larger deflection|1 ~~ Induction occurs when the magnetic field through the coil changes|1
Describe the construction and working of an AC generator with the principle. ~~ Principle: electromagnetic induction|1 ~~ Armature coil rotates between the poles of a magnet|1 ~~ The coil cuts the field lines and current is induced|1 ~~ Slip rings and brushes transfer the current to the external circuit|1 ~~ Direction of current changes after every half rotation, so AC is produced|1
Differentiate between AC and DC. State the frequency of AC in India and give one advantage of AC. ~~ DC flows in one direction, AC reverses periodically|1 ~~ Frequency of AC in India is 50 Hz|1 ~~ Reverses every 1/100 s|1 ~~ AC can be transmitted over long distances with less energy loss|1 ~~ Hence mains supply is AC|1
Draw (describe) a domestic electric circuit and explain the functions of the live wire, neutral wire, earth wire and fuse. ~~ Mains supply of 220 V comes through live (red) and neutral (black)|1 ~~ Earth wire (green) is connected to the metal body|1 ~~ Fuse is placed in the live wire|1 ~~ Appliances are connected in parallel|1 ~~ Earth wire avoids shocks and fuse avoids overloading|1
What are short circuiting and overloading? State their causes and the safety devices used. ~~ Short circuit: live and neutral wires come in direct contact|1 ~~ Cause: damaged insulation or a fault|1 ~~ Overloading: too much current drawn by many appliances|1 ~~ Cause: too many appliances on one socket|1 ~~ Safety: fuse, earth wire or MCB|1
Explain why the magnetic field lines around a bar magnet never cross, and how the field strength is shown by them. Mention three properties. ~~ If they crossed, there would be two directions at one point|1 ~~ Lines are closed curves|1 ~~ They go from N to S outside the magnet|1 ~~ Closer lines mean a stronger field|1 ~~ Field is strongest near the poles|1
Describe the right-hand rule for a solenoid and explain the factors affecting the strength of the magnetic field. ~~ Grasp the solenoid with the right hand with fingers along the current|1 ~~ Thumb points to the north pole|1 ~~ More current gives a stronger field|1 ~~ More turns per unit length give a stronger field|1 ~~ A soft iron core increases the strength|1
Explain how a current-carrying wire experiences a force in a magnetic field. How can you increase the force and reverse its direction? ~~ A current-carrying conductor has its own magnetic field|1 ~~ It interacts with the external field|1 ~~ Force increases with the current and the strength of the field|1 ~~ Reversing the current reverses the force|1 ~~ Reversing the field also reverses it|1
Compare the principles and energy conversions of an electromagnet and a generator. ~~ Electromagnet: electric current produces magnetism|1 ~~ Generator: moving conductor in a field produces current|1 ~~ Electromagnet: electrical to magnetic|1 ~~ Generator: mechanical to electrical energy|1 ~~ Generator works on electromagnetic induction|1
""".strip()

# ============================ EASY ============================
eA = """
The region around a magnet in which its force can be felt is the ~~ magnetic field ~~ electric field ~~ gravitational field ~~ light field ~~ Definition.
The SI unit for the strength of the magnetic field is the ~~ tesla ~~ ampere ~~ weber only ~~ henry ~~ T.
Like poles of magnets ~~ repel each other ~~ attract each other ~~ do not interact ~~ merge ~~ N-N repel.
Unlike poles of magnets ~~ attract each other ~~ repel each other ~~ do not interact ~~ melt ~~ N-S attract.
A freely suspended bar magnet points ~~ north-south ~~ east-west ~~ up-down ~~ in any direction ~~ Because of the earth's field.
The instrument used to find the direction of a magnetic field is a ~~ compass ~~ voltmeter ~~ thermometer ~~ hygrometer ~~ A small magnet.
Iron filings arrange themselves along ~~ magnetic field lines ~~ electric lines ~~ random directions ~~ straight lines only ~~ They get magnetised.
Which of these is a magnetic substance? ~~ Iron ~~ Wood ~~ Plastic ~~ Glass ~~ Ferromagnetic.
A magnet attracts ~~ iron nails ~~ plastic spoons ~~ wooden rods ~~ glass beads ~~ They contain iron.
Outside a magnet, field lines emerge from the ~~ north pole ~~ south pole ~~ middle ~~ both poles ~~ N to S.

A current-carrying wire produces ~~ a magnetic field ~~ no field ~~ only light ~~ only sound ~~ Oersted's discovery.
Oersted observed that a compass needle moves near a wire carrying ~~ an electric current ~~ no current ~~ light ~~ sound ~~ Current deflects the needle.
When the current in a wire is reversed, the compass needle deflects ~~ in the opposite direction ~~ in the same direction ~~ not at all ~~ randomly ~~ The field direction reverses.
The field lines around a straight wire are ~~ concentric circles ~~ parallel lines ~~ radial lines ~~ spirals only ~~ Circular.
The rule to find the direction of the field due to a wire is ~~ right-hand thumb rule ~~ left-hand rule ~~ Ohm's law ~~ Joule's law ~~ Thumb along the current.
A coil of many turns of insulated wire is called ~~ a solenoid ~~ a resistor ~~ a fuse ~~ a cell ~~ Cylindrical coil.
The field inside a solenoid is ~~ uniform ~~ zero ~~ random ~~ weak at the centre ~~ Parallel lines.
An electromagnet uses a core of ~~ soft iron ~~ copper ~~ aluminium ~~ plastic ~~ Easily magnetised and demagnetised.
An electromagnet is a ~~ temporary magnet ~~ permanent magnet ~~ weak natural magnet ~~ insulator ~~ Works only with current.
Electromagnets are used in ~~ electric bells ~~ torches only ~~ glass ~~ mirrors ~~ Common use.

The force on a current-carrying conductor is shown by ~~ Fleming's left-hand rule ~~ Fleming's right-hand rule ~~ Joule's law ~~ Snell's law ~~ Force direction.
In Fleming's left-hand rule, the forefinger indicates ~~ the field ~~ the force ~~ the current ~~ the voltage ~~ Forefinger: field.
In Fleming's left-hand rule, the thumb indicates ~~ force or motion ~~ field ~~ current ~~ resistance ~~ Thumb: motion.
Electromagnetic induction was discovered by ~~ Faraday ~~ Oersted ~~ Newton ~~ Ohm ~~ Michael Faraday.
Which device works on electromagnetic induction? ~~ Generator ~~ Bulb ~~ Heater ~~ Cell ~~ Converts motion to electricity.
The current produced by electromagnetic induction is called ~~ induced current ~~ direct current only ~~ static current ~~ leakage current ~~ Induced by a changing field.
AC means ~~ alternating current ~~ always current ~~ amplified current ~~ ampere current ~~ Direction changes.
DC means ~~ direct current ~~ double current ~~ dynamic current ~~ driving current ~~ One direction.
Electric current from a battery is ~~ DC ~~ AC ~~ both ~~ none ~~ Steady direction.
The household supply in India is ~~ 220 V, 50 Hz AC ~~ 110 V, 60 Hz AC ~~ 220 V DC ~~ 12 V DC ~~ Standard mains.
""".strip()
eB = """
What is a magnetic field? ~~ The region around a magnet where its force is felt|2
Name the poles of a magnet. ~~ North pole|1 ~~ South pole|1
State the direction of field lines outside a magnet. ~~ From the north pole to the south pole|2
Who discovered that current produces a magnetic field? ~~ Hans Christian Oersted|1 ~~ In 1820|1
State the right-hand thumb rule. ~~ Thumb along the current|1 ~~ Fingers curl in the direction of the field|1
What is a solenoid? ~~ A coil of many turns of insulated wire|1 ~~ Of a cylindrical shape|1
What is an electromagnet? ~~ A magnet formed by a current in a coil around a soft iron core|2
Name the rule that gives the direction of force on a current-carrying conductor. ~~ Fleming's left-hand rule|2
Who discovered electromagnetic induction? ~~ Michael Faraday|2
What is a generator used for? ~~ To convert mechanical energy into electrical energy|2
Define alternating current. ~~ Current that changes its direction periodically|2
What is the use of the earth wire? ~~ Safety against electric shocks|1 ~~ Leakage current goes to earth|1
""".strip()
eC = """
Draw (describe) the field lines of a bar magnet and mention the direction. ~~ Closed curves|1 ~~ Outside: N to S|1 ~~ Inside: S to N|1
State any three properties of magnetic field lines. ~~ They are closed curves|1 ~~ They do not cross|1 ~~ Closer lines mean a stronger field|1
How can you show the magnetic field around a bar magnet using iron filings? ~~ Place the magnet below a sheet of paper|1 ~~ Sprinkle iron filings|1 ~~ Tap the paper; filings align along field lines|1
Describe Oersted's experiment briefly. ~~ A wire is placed near a compass|1 ~~ The current is passed|1 ~~ The needle is deflected|1
List three differences between a permanent magnet and an electromagnet. ~~ Permanent magnet cannot be switched off|1 ~~ Electromagnet is temporary|1 ~~ Electromagnet strength can be changed|1
State the factors affecting the strength of an electromagnet. ~~ Current|1 ~~ Number of turns|1 ~~ Material of the core|1
State Fleming's left-hand rule. ~~ Forefinger: field|1 ~~ Middle finger: current|1 ~~ Thumb: force|1
State Fleming's right-hand rule. ~~ Thumb: direction of motion|1 ~~ Forefinger: field|1 ~~ Middle finger: induced current|1
What is the principle of an electric generator? ~~ Electromagnetic induction|1 ~~ A coil rotating in a field|1 ~~ Induces a current|1
Distinguish between AC and DC. ~~ AC changes direction|1 ~~ DC flows in one direction|1 ~~ AC from mains and DC from cells|1
State the frequency of AC in India and explain what it means. ~~ 50 Hz|1 ~~ 50 complete cycles per second|1 ~~ Direction changes 100 times per second|1
List two advantages of AC. ~~ Easy to transmit over long distances|1 ~~ Less power is wasted in the lines|1 ~~ Generated easily in power stations|1
Name the three wires in a domestic circuit with their colours. ~~ Live: red|1 ~~ Neutral: black|1 ~~ Earth: green|1
Why is a fuse connected in the live wire? ~~ It protects the appliance from excess current|1 ~~ It melts when the current is large|1 ~~ Prevents fire hazards|1
What is the voltage of the household supply in India? Why are appliances connected in parallel? ~~ 220 V|1 ~~ Each gets the same voltage|1 ~~ Each works independently|1
Name two safety devices used in a domestic circuit. ~~ Fuse|1 ~~ Earth wire|1 ~~ MCB (miniature circuit breaker)|1
What is the use of slip rings and brushes in a generator? ~~ Slip rings rotate with the coil|1 ~~ Brushes press on the rings|1 ~~ They carry the current to the external circuit|1
What do you understand by the term 'induced current'? ~~ Current produced due to a changing magnetic field|1 ~~ Seen in a closed coil|1 ~~ Detected by a galvanometer|1
""".strip()
eD = """
Describe the properties of magnetic field lines. ~~ They emerge from the north pole and end at the south pole|1 ~~ They form closed curves|1 ~~ The tangent gives the direction of the field|1 ~~ Closeness shows strength|1 ~~ No two lines intersect|1
Describe Oersted's experiment with a diagram description. State its conclusion. ~~ A straight wire is connected to a battery and a key|1 ~~ A compass is placed near the wire|1 ~~ On passing the current the needle is deflected|1 ~~ Reverse the current: deflection reverses|1 ~~ Current produces a magnetic field|1
Explain the magnetic field due to a current-carrying straight conductor. ~~ Concentric circles around the wire|1 ~~ Direction by the right-hand thumb rule|1 ~~ Field increases with current|1 ~~ Field decreases as the distance increases|1 ~~ The field is stronger near the wire|1
What is a solenoid? Describe the field pattern and state how an electromagnet is made. ~~ Solenoid is a coil of many circular turns|1 ~~ Field inside is uniform|1 ~~ Outside it is like a bar magnet|1 ~~ Soft iron rod is placed inside|1 ~~ It becomes an electromagnet when current flows|1
Explain Fleming's left-hand rule and state the factors on which the force on a conductor depends. ~~ Forefinger: field|1 ~~ Middle finger: current|1 ~~ Thumb: force|1 ~~ Fingers are mutually perpendicular|1 ~~ Force depends on current, field strength and angle|1
Describe Faraday's experiment of electromagnetic induction using a coil, magnet and galvanometer. ~~ A coil is connected to a galvanometer|1 ~~ A magnet is moved into the coil|1 ~~ The galvanometer deflects|1 ~~ On withdrawal it deflects the other way|1 ~~ There is no deflection when the magnet is at rest|1
Describe the principle, construction and working of an AC generator. ~~ Principle: electromagnetic induction|1 ~~ Armature coil, magnets, slip rings, brushes|1 ~~ Coil rotates in the field|1 ~~ Current is induced and changes direction every half turn|1 ~~ Output is alternating current|1
Distinguish between AC and DC giving the sources of each. State one advantage of AC. ~~ DC has a fixed direction, AC reverses|1 ~~ DC source: cell|1 ~~ AC source: generator, mains|1 ~~ AC can be transmitted over long distances|1 ~~ With less loss of energy|1
Describe a domestic electric circuit. Name the wires and the safety devices. ~~ Mains supply of 220 V enters through the main fuse|1 ~~ Live (red) and neutral (black) wires|1 ~~ Earth (green) wire connected to the appliance body|1 ~~ Appliances in parallel|1 ~~ Fuse in live wire|1
What are short circuit and overloading? How are they avoided? ~~ Short circuit: live and neutral wires touch|1 ~~ Very large current flows|1 ~~ Overloading: too many appliances in one socket|1 ~~ Use fuse or MCB|1 ~~ Do not overload sockets|1
Why is earthing needed? Explain with the help of a metal body appliance. ~~ Metal body may become live due to a fault|1 ~~ A person touching it gets a shock|1 ~~ Earth wire gives a low-resistance path|1 ~~ The current goes to the ground|1 ~~ The shock is avoided|1
Compare a generator and an electromagnet in terms of principle and energy change. ~~ Generator: electromagnetic induction|1 ~~ Electromagnet: magnetic effect of current|1 ~~ Generator: mechanical to electrical|1 ~~ Electromagnet: electrical to magnetic|1 ~~ Both use coils|1
""".strip()

# ============================ MEDIUM ============================
mA = """
A compass needle placed below a wire carrying current from south to north is deflected. If the current is reversed, the deflection ~~ is reversed ~~ stays the same ~~ becomes zero ~~ doubles ~~ The field direction reverses.
The magnetic field produced by a straight wire at a distance 4 cm is B. At 2 cm from the wire (same current), the field is ~~ larger than B ~~ smaller than B ~~ equal to B ~~ zero ~~ Nearer, stronger.
Looking at a circular coil, the current is anticlockwise. The face seen behaves as ~~ a north pole ~~ a south pole ~~ neutral ~~ both poles ~~ Anticlockwise looks like north.
When current in a solenoid is doubled (other factors same), the field inside ~~ increases ~~ decreases ~~ remains the same ~~ becomes zero ~~ Proportional to the current.
A solenoid is wound over a soft iron rod. This arrangement is ~~ an electromagnet ~~ a permanent magnet ~~ a fuse ~~ a resistor ~~ It becomes magnetised.
Which core is used for the electromagnet in an electric bell? ~~ Soft iron ~~ Steel ~~ Copper ~~ Brass ~~ It demagnetises quickly.
Steel is not used for making an electromagnet because ~~ it retains magnetism after the current stops ~~ it is a nonmetal ~~ it is expensive ~~ it melts easily ~~ It would become a permanent magnet.
A magnetic field line at a point is a curve whose tangent gives ~~ the direction of the field ~~ the direction of the current ~~ the speed of the charge ~~ the voltage ~~ Definition of a field line.
A magnetic field line at a point is a curve such that its tangent shows ~~ the direction of the field ~~ the direction of the current ~~ the direction of force on a charge always ~~ the force on iron ~~ Definition.
The magnetic field is strongest where ~~ field lines are closest ~~ field lines are far ~~ lines cross ~~ lines are straight ~~ Density of lines.

A straight conductor carrying current from east to west is placed in a magnetic field pointing down. The force is directed ~~ to the south ~~ to the north ~~ upward ~~ downward ~~ By Fleming's left-hand rule: thumb points to the south.
An alpha particle moving north is deflected towards the east in a magnetic field. The force is ~~ perpendicular to the velocity ~~ along the velocity ~~ against the velocity ~~ zero ~~ Force is always perpendicular to velocity.
A conductor of length L carrying current I is placed parallel to the field. The force is ~~ zero ~~ maximum ~~ half of maximum ~~ equal to the weight ~~ No force parallel to the field.
Which of the following reverses the force on a current-carrying conductor in a field? ~~ Reversing the current ~~ Increasing the current ~~ Reducing the length ~~ Heating it ~~ Direction changes.
When both the current and the field are reversed, the force ~~ remains the same direction ~~ is reversed ~~ becomes zero ~~ doubles ~~ Two reversals cancel.
A positively charged particle moves into a magnetic field directed into the page, moving to the right. The force is ~~ upward (on the page) ~~ downward ~~ to the left ~~ into the page ~~ By Fleming's left-hand rule.
A moving charge in a magnetic field, moving perpendicular to the field, follows a path that is ~~ circular ~~ straight ~~ parabolic ~~ zigzag ~~ The force acts as a centripetal force.
The force on a conductor in a magnetic field increases when ~~ the current is increased ~~ the field is reduced ~~ the conductor is shortened to zero ~~ the conductor is made parallel ~~ Greater current gives a greater force.
Force on a current-carrying wire is an example of ~~ the interaction of two magnetic fields ~~ chemical effect ~~ heating effect ~~ gravitational effect ~~ Wire field and external field.
The SI unit of magnetic field is ~~ tesla ~~ weber per ampere ~~ newton ~~ ampere metre ~~ T = N / (A m).

If a magnet is moved faster into a coil, the induced current ~~ increases ~~ decreases ~~ remains the same ~~ becomes zero ~~ Faster change gives a larger emf.
The induced current in a coil is zero when ~~ the magnet is at rest relative to the coil ~~ the magnet is moved ~~ the coil is moved ~~ the field changes ~~ No change in the field.
A coil with 100 turns instead of 50 turns, other things same, gives ~~ a larger induced emf ~~ a smaller induced emf ~~ the same induced emf ~~ no emf ~~ More turns, more emf.
Direction of the induced current is obtained from ~~ Fleming's right-hand rule ~~ Fleming's left-hand rule ~~ Joule's law ~~ Ohm's law ~~ Right-hand rule for generators.
In a generator the current changes direction after every ~~ half rotation ~~ full rotation ~~ two rotations ~~ four rotations ~~ Each half turn.
The frequency of AC is 50 Hz. The time period of AC is ~~ 0.02 s ~~ 50 s ~~ 0.2 s ~~ 5 s ~~ T = 1 / f.
In 1 second, the direction of a 50 Hz AC reverses ~~ 100 times ~~ 50 times ~~ 25 times ~~ 200 times ~~ Twice per cycle.
The direction of the current in the mains supply in India reverses every ~~ 1/100 s ~~ 1 s ~~ 1/50 s ~~ 100 s ~~ Frequency is 50 Hz, so reversal occurs 100 times per second.
The device used to safely carry the leakage current to the earth is the ~~ earth wire ~~ live wire ~~ neutral wire ~~ fuse ~~ Earthing.
For a 15 A circuit, the typical appliance used is ~~ an air conditioner or geyser ~~ a bulb ~~ a tube light ~~ a phone charger ~~ High power.
""".strip()
mB = """
State why two field lines cannot intersect each other. ~~ At the point of intersection there would be two directions of the field|1 ~~ The field has only one direction at a point|1
A coil carries current clockwise as seen from the left. Which pole is at the left face? ~~ Clockwise appears as a south pole|1 ~~ So the left face is the south pole|1
Why is the compass needle deflected more when kept nearer to a wire? ~~ The field is stronger near the wire|1 ~~ Greater field produces more deflection|1
Give the reason why soft iron and not steel is used in an electromagnet. ~~ Soft iron gets magnetised and demagnetised quickly|1 ~~ Steel remains a permanent magnet|1
A current-carrying wire is parallel to a uniform magnetic field. State the force and give the reason. ~~ Force is zero|1 ~~ Force is maximum only when the wire is perpendicular to the field|1
Why does the galvanometer connected to a coil show no deflection when the magnet is held at rest inside the coil? ~~ There is no change of the field through the coil|1 ~~ No induced current is produced|1
Why does a generator's output become AC? ~~ The coil's sides interchange positions every half rotation|1 ~~ The direction of the induced current reverses|1
Calculate the time period of an AC with frequency 50 Hz. ~~ T = 1 / f|1 ~~ T = 1 / 50 = 0.02 s|1
How many times does the current of frequency 50 Hz change direction in 1 minute? ~~ 100 times per second|1 ~~ 6000 times per minute|1
Why is the wire of a fuse made of a material having a low melting point? ~~ It melts quickly when excess current flows|1 ~~ This breaks the circuit|1
What is the difference between the potential of the live wire and that of the neutral wire? ~~ Live wire is at 220 V relative to the earth|1 ~~ Neutral wire is at nearly zero potential|1
Why must the switch be on the live wire of an appliance? ~~ Switching off disconnects the live wire|1 ~~ The appliance is then safe to touch|1
""".strip()
mC = """
A bar magnet is moved towards a coil connected to a galvanometer and then away. Describe the observations and give the reason. ~~ Galvanometer deflects when the magnet moves in|1 ~~ It deflects in the opposite direction when withdrawn|1 ~~ The magnetic field through the coil changes, inducing a current|1
How does the magnetic field due to a solenoid vary (a) with the current (b) with the number of turns per unit length (c) with a soft iron core? ~~ (a) Increases with current|1 ~~ (b) Increases with turns per unit length|1 ~~ (c) Increases with a soft iron core|1
Explain why a current-carrying coil kept near a compass needle deflects it, and what happens when the current is reversed. ~~ Coil produces a magnetic field like a bar magnet|1 ~~ The needle aligns with the field and deflects|1 ~~ Reversing the current reverses the poles and the deflection|1
A student winds 100 turns of insulated copper wire on an iron nail and connects it to a battery. What will happen to iron pins brought near? How can she make it stronger? ~~ The nail becomes an electromagnet|1 ~~ It attracts the iron pins|1 ~~ Increase the current or the number of turns|1
An electron enters a region of magnetic field directed into the page, moving to the right. What is the direction of the force on it? Give the reasoning. ~~ Conventional current direction is opposite to the electron's motion|1 ~~ Apply Fleming's left-hand rule with current to the left|1 ~~ Force is downward (on the page)|1
Explain the working of an electric bell using an electromagnet in brief. ~~ Current passes through the coil, the iron core becomes a magnet|1 ~~ It attracts the iron armature, the hammer strikes the gong|1 ~~ The circuit breaks and the cycle repeats|1
State differences between a DC generator and an AC generator. ~~ AC generator has two slip rings|1 ~~ DC generator has a split-ring commutator|1 ~~ AC reverses direction; DC output is in one direction|1
Why does the induced current in a generator last only during rotation? ~~ Emf is produced only when the coil cuts the field lines|1 ~~ A stationary coil has no change in flux|1 ~~ So the current stops when the rotation stops|1
What are the conditions for the induced current in a closed coil? ~~ There must be a change in the magnetic field linked with the coil|1 ~~ The circuit should be closed|1 ~~ Motion of the magnet or coil produces the change|1
Describe the colour coding of wires and the voltage between live and neutral wires in India. ~~ Red for live, black for neutral, green for earth|1 ~~ Potential difference of 220 V|1 ~~ The frequency is 50 Hz|1
Why does a person get a shock on touching the metal body of a faulty iron without earthing? ~~ The live wire may touch the body|1 ~~ The body gets the high potential|1 ~~ Current passes through the person|1
How would you identify the poles of a bar magnet using a compass? ~~ Bring the compass close|1 ~~ Pointing end of the needle indicates the opposite pole|1 ~~ The N pole of the needle is attracted to the S pole of the magnet|1
What is the difference between the magnetic field due to a straight wire and that due to a solenoid? ~~ Straight wire: concentric circles|1 ~~ Solenoid: field like a bar magnet|1 ~~ Solenoid's field is uniform inside|1
Why are the house wiring and appliances connected in parallel but a fuse in series? ~~ Parallel gives each appliance the full voltage|1 ~~ The fuse must carry the total current|1 ~~ Series fuse cuts off the circuit|1
State the energy conversions taking place in a generator and electromagnet. ~~ Generator: mechanical to electrical|1 ~~ Electromagnet: electrical to magnetic|1 ~~ Both are useful devices|1
If the speed of rotation of the coil of a generator is increased, what happens to the output? Explain. ~~ The induced emf increases|1 ~~ The rate of change of the field increases|1 ~~ The frequency of AC also increases|1
Why should a 2 kW heater be used with a 15 A socket, not a 5 A socket? ~~ Current drawn = 2000 / 220 = 9.1 A|1 ~~ A 5 A socket would be overloaded|1 ~~ 15 A circuit is suited for high-power appliances|1
What is the effect on the magnetic field of a solenoid when an iron rod is inserted? Explain. ~~ The field increases|1 ~~ Iron gets magnetised by the field|1 ~~ Its own magnetism adds to the field|1
""".strip()
mD = """
Explain the magnetic field pattern around a current-carrying straight wire and how it changes when the current is doubled and when the distance from the wire is doubled. Describe how to show the direction of the field using the right-hand thumb rule. ~~ Concentric circles around the wire|1 ~~ Doubling the current increases the field|1 ~~ Doubling the distance weakens the field|1 ~~ Right-hand thumb rule: thumb along current|1 ~~ Fingers curl in the direction of the field|1
A student wants to make a strong electromagnet. Describe how it is made, state the factors on which its strength depends and state why it is called a temporary magnet. ~~ Wind many turns of insulated copper wire over a soft iron rod|1 ~~ Connect to a battery|1 ~~ Strength increases with current and with number of turns|1 ~~ Soft iron core increases it|1 ~~ Loses magnetism when current stops, so temporary|1
A straight conductor carrying current of 5 A is placed in a magnetic field. Explain the force on it with Fleming's left-hand rule. If the current flows north to south and the field is vertically upward, find the direction of force. ~~ Force arises from interaction of the wire's field and the external field|1 ~~ Forefinger: field (up)|1 ~~ Middle finger: current (south)|1 ~~ Thumb gives the force|1 ~~ Force is directed towards the west|1
Describe an experiment to demonstrate the force on a current-carrying rod placed in the field of a horseshoe magnet. State two ways to change its direction. ~~ A rod is suspended between poles of a magnet|1 ~~ Current is passed through the rod|1 ~~ The rod is displaced|1 ~~ Reversing the current reverses the force|1 ~~ Reversing the field reverses the force|1
A coil of insulated wire connected to a galvanometer is kept near a bar magnet. Describe four different ways in which a current can be induced. Which factors increase the current? ~~ Moving the magnet towards the coil|1 ~~ Moving the magnet away|1 ~~ Moving the coil towards or away from the magnet|1 ~~ Changing the current in a nearby coil|1 ~~ More speed, more turns and a stronger magnet increase the current|1
Describe the working of an AC generator with the help of the position of the coil during one rotation and the direction of the current. ~~ Coil rotates between N and S poles|1 ~~ First half rotation: current flows in one direction|1 ~~ Second half rotation: direction reverses|1 ~~ Slip rings and brushes convey the current outside|1 ~~ AC output with a frequency of 50 Hz at the power stations in India|1
A household circuit has a 5 A circuit for lights and fans and a 15 A circuit for power appliances. Describe its layout, state why a geyser of 2 kW needs the 15 A circuit and why a fuse is used. ~~ Mains: live, neutral and earth wires|1 ~~ Appliances are connected in parallel|1 ~~ Geyser current = 2000 / 220 = 9.1 A|1 ~~ More than 5 A, so needs the 15 A line|1 ~~ Fuse in the live wire melts for excess current|1
Explain what is meant by short circuit and overloading in household wiring. Give two causes of each and mention three precautions. ~~ Short circuit: live and neutral touch|1 ~~ Causes: damaged insulation, faulty appliance|1 ~~ Overloading: too many appliances on one socket|1 ~~ Cause: faulty appliance drawing excess current or accidental rise in voltage|1 ~~ Precautions: fuse, earth wire, MCB, good insulation|1
Distinguish between direct current and alternating current. State the frequency in India, the period, and the number of reversals per second. ~~ DC: one direction|1 ~~ AC: periodic reversal|1 ~~ Frequency: 50 Hz|1 ~~ Period: 0.02 s|1 ~~ 100 reversals per second|1
Explain with a labelled description of the solenoid how we can find the polarity of its ends using the right-hand rule. How does a solenoid act as a bar magnet? ~~ Solenoid carries current in many circular turns|1 ~~ Grasp with the right hand, fingers along the current|1 ~~ Thumb points towards the north pole|1 ~~ One end acts as north and the other as south|1 ~~ Field pattern outside is like that of a bar magnet|1
Using the idea of electromagnetic induction, explain how mechanical energy is converted to electrical energy in a power station, and the role of the coil, magnet and turbine. ~~ A turbine rotates the armature coil|1 ~~ The coil rotates in the magnetic field|1 ~~ The change of the field through the coil induces a current|1 ~~ The turbine is driven by steam or water|1 ~~ Mechanical energy is converted into electrical energy|1
Compare Oersted's experiment and Faraday's experiment in terms of the observation, the conclusion and the type of effect. ~~ Oersted: current deflects a compass needle|1 ~~ Conclusion: current produces a magnetic field|1 ~~ Faraday: moving magnet induces current in a coil|1 ~~ Conclusion: changing magnetic field produces current|1 ~~ They are opposite effects|1
""".strip()

# ============================ HARD ============================
hA = """
AR ~~ Magnetic field lines never intersect. ~~ The field at a point has only one direction. ~~ a ~~ At a crossing there would be two directions of the field.
AR ~~ A straight current-carrying wire produces a magnetic field around it. ~~ A compass needle placed near the wire gets deflected when the current flows. ~~ b ~~ Both true; the deflection is evidence of the field, not its explanation.
AR ~~ Soft iron is used as the core of an electromagnet. ~~ Soft iron is easily magnetised and demagnetised. ~~ a ~~ Needed for a temporary magnet.
AR ~~ A current-carrying conductor in a field always experiences a force. ~~ The magnetic field acts on the moving charges in the conductor. ~~ c ~~ A is false: the force is zero when the conductor is parallel to the field; R is true.
AR ~~ A conductor moving parallel to the magnetic field induces no current. ~~ There is no change in the magnetic field lines linked with the conductor. ~~ a ~~ Nothing is cut.
AR ~~ AC is preferred for the transmission of power over long distances. ~~ Much less energy is lost when AC is sent over long distances. ~~ a ~~ Lower loss explains the preference.
AR ~~ The earth wire is connected to the metal body of a geyser. ~~ It safeguards the user by taking leakage current to the earth. ~~ a ~~ Prevents shock.
AR ~~ The fuse is connected in the live wire. ~~ It disconnects the appliance from the supply when excess current flows. ~~ a ~~ Breaking the live wire isolates the appliance.
AR ~~ The direction of the force on a charge moving in a magnetic field is perpendicular to the velocity. ~~ The force cannot change the speed of the charged particle. ~~ a ~~ Force perpendicular to motion does no work.
AR ~~ DC generators have a commutator. ~~ A commutator reverses the connection to the circuit every half rotation to give a unidirectional current. ~~ a ~~ The split ring acts as a commutator.

A straight wire with current is placed between the poles of a magnet. The force on the wire is greatest when the wire makes an angle with the field of ~~ 90 degrees ~~ 0 degrees ~~ 45 degrees ~~ 30 degrees ~~ Perpendicular is the maximum.
A coil moves along the field lines of a uniform field in a direction parallel to the field. The induced current is ~~ zero ~~ maximum ~~ half ~~ alternating ~~ No change of linked field.
A bar magnet is brought towards a closed coil of wire. The coil ~~ develops an induced current while the magnet moves ~~ develops a current even if the magnet is at rest ~~ never develops a current ~~ becomes a permanent magnet ~~ A changing field links the coil only during the motion.
A circular coil carrying current has a south pole facing the viewer. The current as seen is ~~ clockwise ~~ anticlockwise ~~ zero ~~ alternating ~~ Clockwise appears as a south pole.
The right-hand thumb rule applied to a vertical wire carrying current upward gives the field direction ~~ anticlockwise when seen from above ~~ clockwise when seen from above ~~ upward ~~ downward ~~ Fingers curl anticlockwise from above.
A positively charged particle moves along the direction of the magnetic field. The force on it is ~~ zero ~~ maximum ~~ perpendicular to the field ~~ along the field ~~ No force when the motion is parallel to the field.
A uniform magnetic field exists in a region. A charged particle enters along the field lines. The particle ~~ moves in a straight line ~~ moves in a circle ~~ stops ~~ moves in a parabola ~~ No force along the field.
Which of the following does not produce a magnetic field? ~~ A stationary charge ~~ A current-carrying wire ~~ A moving charge ~~ A bar magnet ~~ Only moving charges and magnets.
An iron nail is placed in a solenoid carrying current and then the current is switched off. The nail ~~ loses most of the magnetism if it is soft iron ~~ remains strongly magnetised always ~~ attracts everything ~~ becomes non-metal ~~ Soft iron.
In a solenoid, the field at the centre is uniform. If the solenoid is stretched to double its length (same turns, same current), the field ~~ decreases ~~ increases ~~ stays the same ~~ becomes zero ~~ Turns per unit length are halved.

A generator coil of frequency 50 Hz is rotated at double the speed. The frequency becomes ~~ 100 Hz ~~ 25 Hz ~~ 50 Hz ~~ 200 Hz ~~ Proportional to speed.
A magnet is brought toward a coil at a speed v and the induced emf is E. If the speed is tripled, the emf becomes ~~ 3 E ~~ E / 3 ~~ E ~~ 9 E ~~ Proportional to rate of change.
The average value of a pure alternating current over one complete cycle is ~~ zero ~~ maximum ~~ half of maximum ~~ equal to peak ~~ Positive and negative halves cancel.
The number of reversals of AC in a minute of 50 Hz supply is ~~ 6000 ~~ 3000 ~~ 600 ~~ 100 ~~ 100 per s x 60.
A fuse of 5 A is connected in a circuit with a 1.5 kW heater at 220 V. The fuse ~~ blows because I = 6.8 A ~~ does not blow ~~ blows because I = 1.5 A ~~ gives no protection ~~ I = 1500 / 220 = 6.8 A > 5 A.
Appliances A (1 kW) and B (0.5 kW) use the same 220 V line protected by a 5 A fuse. Which combination will blow the fuse? ~~ Both A and B on together ~~ A alone ~~ B alone ~~ None ~~ 1.5 kW draws 6.8 A.
Which of the following correctly describes the live wire? ~~ At high potential with respect to earth ~~ At zero potential ~~ Has green insulation ~~ Connected to the metal body ~~ 220 V.
A person touches a metal body of an appliance whose live wire is loose and touching the body. If the body is earthed ~~ the fuse blows and the person is safe ~~ the person is electrocuted ~~ the appliance runs better ~~ there is no change ~~ Large current passes to earth.
If the iron core is removed from an electromagnet, the strength ~~ decreases ~~ increases ~~ is unchanged ~~ is infinite ~~ Core enhances the field.
A coil rotating in a magnetic field produces a maximum emf when the coil ~~ cuts the lines of force at the greatest rate ~~ is parallel to the field lines ~~ lies along the field lines but does not move ~~ is at rest ~~ Greatest rate of change of flux.
""".strip()
hB = """
A charged particle enters a magnetic field and its speed remains unchanged. Explain why. ~~ Force is perpendicular to the velocity|1 ~~ No work is done, so the speed is constant|1
The frequency of AC changes from 50 Hz to 60 Hz. Find the new period and compare the number of reversals per second. ~~ T = 1 / 60 = 0.0167 s|1 ~~ Reversals = 120 per second (vs 100)|1
How would you test whether a wire in a circuit is carrying current without touching it, using a compass? ~~ Bring a compass near the wire|1 ~~ Deflection of the needle shows a current|1
Why does a current-carrying coil suspended freely in the earth's field rest along the north-south direction? ~~ It acts like a bar magnet|1 ~~ It aligns with the earth's field|1
Calculate the current drawn by a 2.2 kW geyser at 220 V and say whether a 5 A or a 15 A circuit is suitable. ~~ I = 2200 / 220 = 10 A|1 ~~ The 15 A circuit is suitable|1
What happens to the induced current if the same magnet is pushed into a coil with a larger number of turns? ~~ Induced emf is larger|1 ~~ More turns link more of the changing field|1
Why does a magnet attract an iron nail but not a copper wire? ~~ Iron is a magnetic material|1 ~~ Copper is not magnetised by an external magnet|1
Explain why the iron filings near the poles of a bar magnet are crowded. ~~ Field is strongest near the poles|1 ~~ Field lines are closer there|1
Why is a switch always connected to the live wire? ~~ It disconnects the appliance from the high potential|1 ~~ The appliance stays safe when switched off|1
Name the device that converts AC into DC and the device which changes direction in a DC generator. ~~ Rectifier|1 ~~ Split-ring commutator|1
Two solenoids A and B have the same current and length, but A has 200 turns and B has 400 turns. Compare the fields. ~~ Field is proportional to the number of turns per unit length|1 ~~ B has double the field|1
If a bar magnet is cut into two pieces along its length, what are the poles of each piece? ~~ Each piece has its own north and south poles|1 ~~ Isolated poles are not possible|1
""".strip()
hC = """
Explain why the force on a current-carrying conductor depends on the angle between the conductor and the field. ~~ Force arises from the component of the field perpendicular to the wire|1 ~~ It is maximum when the wire is perpendicular|1 ~~ It is zero when the wire is parallel|1
A wire carrying current is bent in the form of a circular loop. How are the field lines inside the loop and outside it different? ~~ Inside: field lines are nearly parallel and in one direction|1 ~~ Outside: lines go back in the opposite direction|1 ~~ Each element of the wire adds to the field|1
A heater of 2 kW and a toaster of 1 kW are used at a time on a 5 A fuse circuit at 220 V. Will the fuse blow? Show by calculation. ~~ Total power = 3 kW|1 ~~ I = 3000 / 220 = 13.6 A|1 ~~ More than 5 A, so the fuse blows|1
Explain how a magnet, a coil and a galvanometer can be used to show that the induced current depends on the speed of the magnet. ~~ Move the magnet slowly: small deflection|1 ~~ Move it quickly: larger deflection|1 ~~ The rate of change of the field decides the emf|1
In a generator the armature rotates at 50 revolutions per second. State the frequency of the AC produced and its period. ~~ One cycle for one rotation|1 ~~ Frequency = 50 Hz|1 ~~ Period = 0.02 s|1
What is meant by earthing? Explain with an example why it is necessary for a refrigerator. ~~ Metal body connected to the earth through the earth wire|1 ~~ If the live wire touches the body, current passes to earth|1 ~~ Prevents shocks and fires|1
Why should an electrical appliance such as a toaster have a metal casing connected to the earth wire? ~~ Metal case can become live due to a fault|1 ~~ The earth wire is a low-resistance path|1 ~~ The fuse blows and the user is safe|1
Explain the difference between the nature of the magnetic field of a straight wire and a bar magnet. ~~ Straight wire: concentric closed circles around the wire|1 ~~ Bar magnet: lines emerge from N and enter S|1 ~~ Both have closed loop fields|1
How can you determine the polarity of an electromagnet using a compass needle? ~~ Bring the needle near an end|1 ~~ If the north pole of the needle is attracted, the end is a south pole|1 ~~ Reversing the current reverses the polarity|1
Under what circumstances is the force on a moving charge in a magnetic field maximum? ~~ Charge moves perpendicular to the field|1 ~~ Force is zero when it moves along the field|1 ~~ Maximum at 90 degrees|1
In a closed circuit with a galvanometer and a coil, a magnet falls through the coil. Describe the sign of the galvanometer deflection when it enters and leaves. ~~ Deflection occurs in one direction while entering|1 ~~ In the opposite direction when leaving|1 ~~ The field through the coil first increases and then decreases|1
Give reasons: (a) why the metal body is earthed (b) why the fuse is in the live wire (c) why a thick wire is used in the 15 A circuit. ~~ (a) To take leakage current to earth|1 ~~ (b) The live wire carries the full current, and cutting it isolates the appliance|1 ~~ (c) Thick wire has low resistance and less heating|1
Why do we say that electricity and magnetism are related? Give two examples. ~~ Current produces a magnetic field (Oersted)|1 ~~ Changing magnetic field produces current (Faraday)|1 ~~ Force on a conductor in a field links the two|1
How would you make a stronger electromagnet using the same wire and battery? ~~ Increase the number of turns|1 ~~ Use a soft iron core|1 ~~ Use a thicker core or a larger current|1
Explain why an alternating current is produced by the coil of a generator when it rotates continuously in the same direction. ~~ The two sides of the coil exchange positions every half rotation|1 ~~ The direction of the induced current reverses each half rotation|1 ~~ Hence the output is alternating|1
How does the output of an AC generator change if the number of turns in the coil is doubled? ~~ The induced emf doubles|1 ~~ The frequency is unchanged|1 ~~ More turns link more field lines|1
If the earth had no magnetic field, why would a compass needle be of no use? ~~ The needle aligns with the magnetic field|1 ~~ Without a field it points in no fixed direction|1 ~~ It is used to find direction by the earth's field|1
What would happen to an appliance if the neutral wire in a 220 V circuit is broken? ~~ The appliance is cut off from the circuit|1 ~~ The wire may still be live, so it is dangerous|1 ~~ Switch and fuse give protection|1
""".strip()
hD = """
A straight wire carries current from west to east in a field pointing north. Find the direction of the force and describe how it changes (a) when the current is reversed (b) when both are reversed. State the rule used. ~~ Fleming's left-hand rule|1 ~~ Forefinger north, middle finger east|1 ~~ Thumb points upward|1 ~~ (a) Force becomes downward|1 ~~ (b) Both reversed: force upward as before|1
Describe the construction and working of a simple DC generator and mention the role of the split ring commutator. Why is the current from it not steady? ~~ Armature coil rotates between magnet poles|1 ~~ EMI induces a current|1 ~~ Split rings reverse the connection every half rotation|1 ~~ Output is in one direction|1 ~~ Value varies between zero and maximum, so it is not steady|1
Explain with the principle and steps how a magnetic field is produced by a current in a solenoid and how it can be made 10 times stronger. ~~ Each turn produces a magnetic field|1 ~~ Fields of all turns add inside|1 ~~ Field is stronger with more turns per unit length|1 ~~ Increasing the current raises the field|1 ~~ A soft iron core increases it considerably|1
A student has a solenoid, a bar magnet, a galvanometer and a battery. Design activities to show (a) the magnetic effect of current (b) electromagnetic induction. State the observations and the conclusions. ~~ (a) Place a compass near the solenoid; switch on the current|1 ~~ Needle deflects, so current produces a magnetic field|1 ~~ (b) Connect the solenoid to the galvanometer|1 ~~ Move the magnet in and out|1 ~~ Deflection shows induced current from a changing field|1
Describe the domestic circuit used in a house. Why are the fuse, the earth wire and the MCB used? A home has 5 bulbs of 60 W, 2 fans of 80 W and a 1.5 kW heater, all on 220 V. Find the total current when all are used. ~~ Live, neutral and earth wires; appliances in parallel|1 ~~ Fuse and MCB protect from overload|1 ~~ Earth wire gives safety|1 ~~ Total power = 300 + 160 + 1500 = 1960 W|1 ~~ I = 1960 / 220 = 8.9 A|1
Explain the factors on which the force on a current-carrying conductor in a field depends and how the direction can be reversed. A rod carries current across a uniform field. State the direction of the force with the left-hand rule if the field points upward along the page and the current flows to the right along the page. ~~ Depends on current|1 ~~ On the strength of the field|1 ~~ On the angle between wire and field|1 ~~ Reverse the current or field to reverse the force|1 ~~ Field up and current right (both along the page): force is out of the page, towards the observer|1
Compare the magnetic field of a bar magnet and of a current-carrying solenoid. Explain how a solenoid can be used to lift iron scrap. ~~ Both have similar field patterns|1 ~~ Lines go from N to S outside|1 ~~ The solenoid's field can be switched on or off|1 ~~ A soft iron core makes it a strong electromagnet|1 ~~ Scrap is lifted while the current flows and dropped when switched off|1
In an experiment a bar magnet is pushed into a coil with 3 different speeds, and the deflections of the galvanometer are 2, 4 and 6 divisions. What do you conclude? Also predict the deflection if the coil had double the turns. ~~ Deflection increases with speed|1 ~~ It is proportional to the speed here (2 : 4 : 6 = 1 : 2 : 3)|1 ~~ The induced emf depends on the rate of change of the field|1 ~~ With double the turns the emf doubles|1 ~~ Deflections would be about 4, 8 and 12 divisions|1
State the frequency, the period and the typical voltage of the household supply in India. A device draws 5 A at 220 V; find its power and the energy used in 3 hours in kWh. ~~ Frequency 50 Hz, period 0.02 s|1 ~~ Voltage 220 V|1 ~~ P = V I = 1100 W|1 ~~ E = 1.1 kW x 3 h|1 ~~ E = 3.3 kWh|1
Describe the effect on the heating and safety of an appliance if (a) the earth wire is not connected (b) the fuse is placed in the neutral wire (c) the switch is placed in the neutral wire. ~~ (a) Metal body may stay live, causing a shock|1 ~~ (b) Live wire remains connected when the fuse melts|1 ~~ (b) The appliance remains at high potential|1 ~~ (c) Appliance stays live even when switched off|1 ~~ Hence the fuse and switch must be in the live wire|1
Explain Oersted's discovery and Faraday's discovery, and say how they led to inventions such as the electromagnet and the generator. ~~ Oersted: current produces a magnetic field|1 ~~ Led to the electromagnet|1 ~~ Faraday: a changing field induces a current|1 ~~ Led to the generator|1 ~~ Both show the link between electricity and magnetism|1
A coil is connected to a galvanometer. A magnet is pushed into it, held for a few seconds and then pulled out. Describe the galvanometer readings in the three stages and explain. ~~ While pushing in: the needle deflects one way|1 ~~ While held at rest: no deflection|1 ~~ While pulling out: deflection in the opposite direction|1 ~~ Induced current appears only when the field linked with the coil changes|1 ~~ Faster motion gives a larger deflection|1
""".strip()

TIERS = {"NCERT": tier(nA, nB, nC, nD), "Easy": tier(eA, eB, eC, eD), "Medium": tier(mA, mB, mC, mD), "Hard": tier(hA, hB, hC, hD)}
