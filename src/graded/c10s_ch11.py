"""Class 10 Science Ch 11 - Electricity (hand-written graded banks)."""
from scix import tier

SLUG, NAME, CHNO = "Electricity", "Electricity", 11

# ============================ NCERT-TYPE ============================
nA = """
The SI unit of electric charge is ~~ coulomb ~~ ampere ~~ volt ~~ ohm ~~ 1 C is the charge of about 6 x 10^18 electrons.
The SI unit of electric current is ~~ ampere ~~ coulomb ~~ volt ~~ watt ~~ 1 A = 1 C/s.
Electric current is measured by an ~~ ammeter connected in series ~~ ammeter connected in parallel ~~ voltmeter connected in series ~~ voltmeter connected in parallel ~~ An ammeter has a very low resistance.
Potential difference is measured by a ~~ voltmeter connected in parallel ~~ voltmeter connected in series ~~ ammeter in parallel ~~ galvanometer in series ~~ A voltmeter has a very high resistance.
One volt is the potential difference when ~~ 1 joule of work is done to move 1 coulomb of charge ~~ 1 coulomb of charge moves in 1 s ~~ 1 watt of power is used for 1 s ~~ 1 ohm of resistance carries 1 A ~~ V = W/Q.
The relation between charge, current and time is ~~ Q = I t ~~ Q = I / t ~~ Q = t / I ~~ Q = I + t ~~ I = Q/t.
Which of the following is a good conductor of electricity? ~~ Copper ~~ Rubber ~~ Glass ~~ Wood ~~ Free electrons are present in metals.
Conventional current flows from ~~ the positive terminal to the negative terminal outside the cell ~~ the negative to the positive terminal ~~ in either direction ~~ only in the cell ~~ Opposite to the direction of electron flow.
The charge on an electron is ~~ 1.6 x 10^-19 C ~~ 1.6 x 10^19 C ~~ 6.25 x 10^18 C ~~ 9.1 x 10^-31 C ~~ Magnitude of the charge on an electron.
The device that maintains a potential difference across a conductor is ~~ a cell or battery ~~ an ammeter ~~ a resistor ~~ a switch ~~ A source of emf.

Ohm's law states that the current through a conductor is ~~ directly proportional to the potential difference, at constant temperature ~~ inversely proportional to the potential difference ~~ independent of the potential difference ~~ proportional to the square of V ~~ V = IR.
The SI unit of resistance is ~~ ohm ~~ ampere ~~ volt ~~ watt ~~ 1 ohm = 1 V/A.
The V-I graph for an ohmic conductor is ~~ a straight line through the origin ~~ a curve ~~ a parabola ~~ a horizontal line ~~ Slope = R.
The resistance of a conductor is ~~ directly proportional to its length ~~ inversely proportional to its length ~~ independent of length ~~ proportional to the square of the area ~~ R is proportional to L.
The resistance of a conductor is inversely proportional to its ~~ area of cross-section ~~ length ~~ resistivity ~~ temperature only ~~ R = rho L / A.
The SI unit of resistivity is ~~ ohm metre ~~ ohm ~~ ohm per metre ~~ siemens ~~ rho = R A / L.
Resistivity of an alloy is generally ~~ higher than that of its constituent metals ~~ lower than that of its metals ~~ zero ~~ same as that of insulators ~~ Alloys have higher resistivity.
Which material is used in the filament of an electric heater? ~~ Nichrome ~~ Copper ~~ Aluminium ~~ Silver ~~ High resistivity and does not oxidise easily.
Which of the following has the lowest resistivity? ~~ Silver ~~ Iron ~~ Nichrome ~~ Mercury ~~ Silver is the best conductor.
The resistance of a wire is R. If its length is doubled and its area is halved, the new resistance is ~~ 4R ~~ 2R ~~ R/2 ~~ R ~~ R = rho (2L)/(A/2).

For resistors in series, the equivalent resistance is ~~ R1 + R2 + R3 ~~ 1/R1 + 1/R2 ~~ greater than none ~~ less than each ~~ Rs = R1 + R2 + R3.
In a series circuit the quantity that is the same through all the resistors is ~~ current ~~ potential difference ~~ power ~~ resistance ~~ Same current.
In a parallel circuit the quantity that is the same across all the resistors is ~~ potential difference ~~ current ~~ resistance ~~ power ~~ Same voltage.
The equivalent resistance of 2 ohm and 2 ohm in parallel is ~~ 1 ohm ~~ 4 ohm ~~ 2 ohm ~~ 0.5 ohm ~~ 1/Rp = 1/2 + 1/2.
The effective resistance of three resistors of 3 ohm each in series is ~~ 9 ohm ~~ 1 ohm ~~ 3 ohm ~~ 6 ohm ~~ Add.
The equivalent resistance of parallel resistors is ~~ less than the smallest resistance ~~ more than the largest resistance ~~ equal to the average ~~ equal to the sum ~~ More paths reduce R.
Why are household appliances connected in parallel? ~~ Each gets the same voltage and works independently ~~ it reduces current ~~ it increases voltage ~~ it saves power ~~ Parallel connection.
The heat produced in a resistor is given by ~~ I^2 R t ~~ I R^2 t ~~ I R / t ~~ V I / t ~~ Joule's law.
The SI unit of electric power is ~~ watt ~~ joule ~~ volt ~~ ampere ~~ 1 W = 1 J/s.
1 kilowatt hour equals ~~ 3.6 x 10^6 J ~~ 3.6 x 10^3 J ~~ 1000 J ~~ 36 x 10^6 J ~~ 1 kW x 3600 s.
""".strip()
nB = """
Define one ampere of current. ~~ Current when 1 coulomb of charge flows through a point in 1 second|2
What is meant by the electric potential difference between two points? ~~ Work done to move a unit charge from one point to another|2
State Ohm's law. ~~ Potential difference across a conductor is proportional to the current|1 ~~ Temperature and other conditions remain constant|1
Why is an ammeter connected in series and a voltmeter in parallel? ~~ Ammeter has low resistance, so the current is not changed|1 ~~ Voltmeter has high resistance, so it draws almost no current|1
List the factors on which the resistance of a conductor depends. ~~ Length and area of cross-section|1 ~~ Nature of the material and temperature|1
Why are alloys used in heating devices? ~~ Resistivity of alloys is higher|1 ~~ They do not oxidise readily at high temperature|1
Why is copper used for connecting wires? ~~ Copper has low resistivity|1 ~~ It is a good conductor and ductile|1
What is the effect on resistance when the length of a wire is doubled? ~~ Resistance is proportional to length|1 ~~ It becomes double|1
Write the expressions for power in three forms. ~~ P = VI|1 ~~ P = I^2 R = V^2 / R|1
State Joule's law of heating. ~~ H = I^2 R t|1 ~~ Heat depends on the square of current, resistance and time|1
Why do we use a fuse in electrical circuits? ~~ It melts when the current exceeds the safe limit|1 ~~ It protects the appliance|1
What is the commercial unit of electric energy? Give its value in joules. ~~ Kilowatt hour|1 ~~ 3.6 x 10^6 J|1
""".strip()
nC = """
A current of 0.5 A flows in a conductor for 10 minutes. Find the charge that flows and the number of electrons. ~~ Q = I t = 0.5 x 600 = 300 C|1 ~~ n = Q / e|1 ~~ n = 300 / 1.6 x 10^-19 = 1.875 x 10^21|1
How much work is done in moving a charge of 2 C across two points having a potential difference of 12 V? ~~ W = V Q|1 ~~ W = 12 x 2|1 ~~ W = 24 J|1
A wire of resistance 20 ohm carries a current of 0.5 A. Find the potential difference across it. ~~ V = I R|1 ~~ V = 0.5 x 20|1 ~~ V = 10 V|1
Draw the circuit diagram in words: how would you connect a cell, a resistor, an ammeter and a voltmeter to verify Ohm's law? ~~ Cell, key, resistor and ammeter are in series|1 ~~ Voltmeter is connected in parallel with the resistor|1 ~~ Readings of V and I are noted and V/I is found to be constant|1
Explain why the resistance of a conductor increases with its length and decreases with its area. ~~ Longer path means more collisions of electrons|1 ~~ Larger area gives more paths for electrons|1 ~~ R = rho L / A|1
The resistance of a wire of length 2 m and area 0.5 mm^2 is 4 ohm. Find its resistivity. ~~ rho = R A / L|1 ~~ rho = 4 x 0.5 x 10^-6 / 2|1 ~~ rho = 1 x 10^-6 ohm m|1
Find the equivalent resistance when 2 ohm, 3 ohm and 5 ohm are connected in series, and the current from a 6 V battery. ~~ Rs = 2 + 3 + 5 = 10 ohm|1 ~~ I = V / R|1 ~~ I = 0.6 A|1
Three resistors 20 ohm, 30 ohm and 60 ohm are in parallel. Find the equivalent resistance. ~~ 1/R = 1/20 + 1/30 + 1/60|1 ~~ 1/R = 6/60 = 1/10|1 ~~ R = 10 ohm|1
State three differences between series and parallel combinations of resistors. ~~ Series: same current; parallel: same potential difference|1 ~~ Series: R increases; parallel: R decreases|1 ~~ Series: one break stops all; parallel: others still work|1
A 6 ohm and a 3 ohm resistor are in parallel and connected in series with 4 ohm. Find the total resistance. ~~ Parallel: 6 x 3 / 9 = 2 ohm|1 ~~ Total = 2 + 4|1 ~~ Total = 6 ohm|1
An electric iron of 1100 W is operated at 220 V. Find the current and the resistance. ~~ I = P / V = 1100 / 220 = 5 A|1 ~~ R = V / I|1 ~~ R = 44 ohm|1
Calculate the heat produced by a 10 ohm resistor carrying 2 A current for 30 s. ~~ H = I^2 R t|1 ~~ H = 4 x 10 x 30|1 ~~ H = 1200 J|1
Why does a bulb filament glow but the connecting wire does not? ~~ Filament has very high resistance, so heat produced is large|1 ~~ Heat H = I^2 R t|1 ~~ Connecting wires have low resistance|1
How much energy in kWh is consumed by a 2 kW heater in 3 hours? What is the cost at Rs 5 per unit? ~~ Energy = 2 x 3 = 6 kWh|1 ~~ 1 unit = 1 kWh|1 ~~ Cost = 6 x 5 = Rs 30|1
Why is tungsten used for bulb filaments? ~~ High melting point|1 ~~ High resistivity|1 ~~ It does not oxidise readily in an inert gas|1
State the factors on which the heat produced in a conductor depends and write the formula. ~~ Current, resistance and time|1 ~~ H = I^2 R t|1 ~~ Also equals V I t|1
Explain why the series arrangement is not used for household circuits. ~~ Same current flows through all appliances|1 ~~ If one fails the entire circuit breaks|1 ~~ Voltage is divided among appliances|1
What is the resistance of a bulb rated 100 W, 220 V? Find the current. ~~ R = V^2 / P = 48400 / 100|1 ~~ R = 484 ohm|1 ~~ I = P / V = 0.45 A|1
""".strip()
nD = """
State and explain Ohm's law. Describe an activity to verify it and how the V-I graph is used to find the resistance. ~~ V is proportional to I at constant temperature|1 ~~ Connect cell, ammeter, resistor and key in series and a voltmeter across the resistor|1 ~~ Take readings for different numbers of cells|1 ~~ The V-I graph is a straight line through the origin|1 ~~ The slope of the graph gives the resistance|1
Derive the formula for the equivalent resistance of three resistors connected in series. Find it for 3 ohm, 4 ohm and 5 ohm. ~~ Same current I flows through each|1 ~~ V = V1 + V2 + V3 = I (R1 + R2 + R3)|1 ~~ Rs = R1 + R2 + R3|1 ~~ Rs = 3 + 4 + 5|1 ~~ Rs = 12 ohm|1
Derive the formula for the equivalent resistance of two resistors in parallel. Find it for 12 ohm and 4 ohm. ~~ Same potential difference V across each|1 ~~ Total current I = I1 + I2|1 ~~ 1/Rp = 1/R1 + 1/R2|1 ~~ 1/Rp = 1/12 + 1/4 = 4/12|1 ~~ Rp = 3 ohm|1
A resistance of 40 ohm and one of 60 ohm are in parallel. A 12 V battery is connected. Find the total resistance and the current in each resistor. ~~ 1/R = 1/40 + 1/60 = 5/120|1 ~~ R = 24 ohm|1 ~~ I1 = 12 / 40 = 0.3 A|1 ~~ I2 = 12 / 60 = 0.2 A|1 ~~ Total current 0.5 A|1
Define resistivity. State the factors on which it depends. A wire of length 1 m and area of cross-section 1 mm^2 has resistance 1.5 ohm. Find its resistivity. ~~ Resistance of a conductor of unit length and unit area|1 ~~ Depends on material and temperature, not on size|1 ~~ rho = R A / L|1 ~~ rho = 1.5 x 10^-6 / 1|1 ~~ rho = 1.5 x 10^-6 ohm m|1
A bulb is rated 60 W at 220 V. Find the current drawn, resistance of the filament and the energy consumed in 5 hours in kWh and in joules. ~~ I = 60/220 = 0.27 A|1 ~~ R = 220^2 / 60 = 806.7 ohm|1 ~~ Energy = 0.06 x 5 = 0.3 kWh|1 ~~ 0.3 x 3.6 x 10^6|1 ~~ = 1.08 x 10^6 J|1
Establish the formula H = I^2 R t from the definitions of work and potential difference. ~~ Work done to move charge Q across V is W = V Q|1 ~~ Q = I t|1 ~~ W = V I t|1 ~~ Using V = I R, W = I^2 R t|1 ~~ This energy is dissipated as heat H|1
List five applications of the heating effect of electric current with the principle of working of a fuse. ~~ Electric heater, toaster, iron|1 ~~ Electric bulb|1 ~~ Fuse works by heating its wire|1 ~~ Fuse wire has low melting point|1 ~~ It melts when current exceeds the limit and breaks the circuit|1
Three resistors of 2 ohm, 3 ohm and 6 ohm are connected in parallel across a 6 V source. Find the total resistance, total current and the power consumed. ~~ 1/R = 1/2 + 1/3 + 1/6 = 1|1 ~~ R = 1 ohm|1 ~~ I = 6 / 1 = 6 A|1 ~~ P = V I = 36 W|1 ~~ Individual currents 3 A, 2 A, 1 A|1
Explain the factors affecting resistance with expression, and compare the resistance of copper and nichrome wires of the same size. ~~ R = rho L / A|1 ~~ Increases with length and decreases with area|1 ~~ Depends on the material and temperature|1 ~~ Nichrome has much higher resistivity than copper|1 ~~ So the nichrome wire has a greater resistance|1
An electric heater of 2 kW is used for 2 hours daily for 30 days at Rs 6 per unit. Find the energy consumed and the cost of use. ~~ Energy per day = 2 x 2 = 4 kWh|1 ~~ In 30 days = 120 kWh|1 ~~ 120 units|1 ~~ Cost = 120 x 6|1 ~~ Rs 720|1
A circuit has 4 ohm in series with a parallel combination of 6 ohm and 3 ohm across a 12 V battery. Find the total resistance, the current and the voltage across the parallel combination. ~~ Parallel part = 6 x 3 / 9 = 2 ohm|1 ~~ Total R = 4 + 2 = 6 ohm|1 ~~ I = 12 / 6 = 2 A|1 ~~ Voltage across 4 ohm = 8 V|1 ~~ Voltage across parallel part = 12 - 8 = 4 V|1
""".strip()

# ============================ EASY ============================
eA = """
Electric current is the rate of flow of ~~ charge ~~ mass ~~ energy ~~ heat ~~ I = Q/t.
Which of these is an insulator? ~~ Rubber ~~ Copper ~~ Iron ~~ Aluminium ~~ No free electrons.
The instrument used to measure current is the ~~ ammeter ~~ voltmeter ~~ galvanometer only ~~ thermometer ~~ A for ampere.
The instrument used to measure potential difference is the ~~ voltmeter ~~ ammeter ~~ ohmmeter only ~~ barometer ~~ V for volt.
A voltmeter is connected ~~ in parallel ~~ in series ~~ at any place ~~ in a short circuit ~~ Across the component.
An ammeter is connected ~~ in series ~~ in parallel ~~ across the cell ~~ across the bulb ~~ In the path of current.
The unit of potential difference is ~~ volt ~~ ampere ~~ ohm ~~ coulomb ~~ V.
The relation between V, I and R is ~~ V = I R ~~ V = I / R ~~ V = R / I ~~ V = I + R ~~ Ohm's law.
The symbol of a resistor is ~~ a zig-zag line ~~ two parallel lines ~~ a circle with a cross ~~ a plain line ~~ Standard symbol.
A closed circuit is one in which ~~ current flows ~~ no current flows ~~ the cell is removed ~~ the key is open ~~ The path is complete.

The resistance of a wire depends on ~~ its length ~~ the current only ~~ the voltage only ~~ the time ~~ R is proportional to length.
Thicker wires have ~~ less resistance ~~ more resistance ~~ the same resistance ~~ infinite resistance ~~ Greater area.
A longer wire of the same material and thickness has ~~ more resistance ~~ less resistance ~~ the same resistance ~~ no resistance ~~ Proportional to length.
Resistance of a metal wire ~~ increases with temperature ~~ decreases with temperature ~~ is the same at all temperatures ~~ becomes zero on heating ~~ Metals.
The unit of resistivity is ~~ ohm metre ~~ ohm ~~ metre ~~ siemens ~~ Ohm m.
Which is the best conductor? ~~ Silver ~~ Nichrome ~~ Glass ~~ Rubber ~~ Lowest resistivity.
The resistivity of an insulator is ~~ very high ~~ very low ~~ zero ~~ same as copper ~~ 10^12 to 10^17 ohm m.
Nichrome is an alloy of ~~ nickel, chromium and iron ~~ copper and zinc ~~ lead and tin ~~ iron and carbon only ~~ Used in heaters.
Resistance of 1 m of a wire is 2 ohm. For 3 m of the same wire, the resistance is ~~ 6 ohm ~~ 2 ohm ~~ 1/3 ohm ~~ 3 ohm ~~ Proportional.
Resistance is measured in ~~ ohm ~~ volt ~~ watt ~~ joule ~~ Omega.

Two resistors of 5 ohm each in series have a total of ~~ 10 ohm ~~ 2.5 ohm ~~ 5 ohm ~~ 25 ohm ~~ Add.
Two resistors of 4 ohm each in parallel have a total of ~~ 2 ohm ~~ 8 ohm ~~ 4 ohm ~~ 16 ohm ~~ Half.
In series, if one bulb fuses, the others ~~ stop glowing ~~ glow brighter ~~ glow dimmer ~~ are unaffected ~~ The circuit is broken.
In parallel, if one bulb fuses, the others ~~ continue to glow ~~ stop ~~ explode ~~ glow dimmer ~~ Separate paths.
Electric power is the ~~ rate of consumption of energy ~~ total energy ~~ charge ~~ resistance ~~ P = W/t.
The unit of power is ~~ watt ~~ joule ~~ coulomb ~~ ohm ~~ W.
The unit of electrical energy used commercially is ~~ kilowatt hour ~~ watt ~~ joule per second ~~ volt ~~ kWh.
The fuse wire is made of a material of ~~ low melting point ~~ high melting point ~~ high resistivity only ~~ zero resistance ~~ It melts quickly.
The formula for power is ~~ P = V I ~~ P = V / I ~~ P = I / V ~~ P = R / I ~~ Power = V x I.
Heating effect of current is used in ~~ an electric heater ~~ a magnet ~~ a battery ~~ a compass ~~ Heater works on I^2 R t.
""".strip()
eB = """
Define electric current. ~~ Rate of flow of electric charge|2
What is the SI unit of charge? Give its value in terms of electrons. ~~ Coulomb|1 ~~ About 6.25 x 10^18 electrons|1
What is a potential difference? ~~ Work done per unit charge in moving between two points|2
Write Ohm's law in the form of an equation. ~~ V = I R|1 ~~ Where R is constant at constant temperature|1
Define the resistance of a conductor. ~~ Opposition offered to the flow of current|1 ~~ R = V / I|1
Define 1 ohm. ~~ Resistance when 1 A flows at a potential difference of 1 V|2
Write the unit of resistivity. ~~ Ohm metre|2
Name two materials used in making heating elements. ~~ Nichrome|1 ~~ Constantan or manganin|1
What is the formula for the equivalent resistance in series? ~~ Rs = R1 + R2 + R3|2
What is the formula for equivalent resistance in parallel? ~~ 1/Rp = 1/R1 + 1/R2 + 1/R3|2
Define electric power and give its unit. ~~ Rate of doing electrical work|1 ~~ Watt|1
What is a fuse? ~~ A safety device with a low-melting wire|1 ~~ Breaks the circuit on overloading|1
""".strip()
eC = """
Find the charge flowing in 5 s through a wire carrying a current of 2 A. ~~ Q = I t|1 ~~ Q = 2 x 5|1 ~~ Q = 10 C|1
A current of 0.2 A flows through a resistor of 10 ohm. Find the potential difference. ~~ V = I R|1 ~~ V = 0.2 x 10|1 ~~ V = 2 V|1
A potential difference of 12 V is applied across a 4 ohm resistor. Find the current. ~~ I = V / R|1 ~~ I = 12 / 4|1 ~~ I = 3 A|1
A current of 3 A flows through a conductor having 6 V across it. Find the resistance. ~~ R = V / I|1 ~~ R = 6 / 3|1 ~~ R = 2 ohm|1
Find the work done in moving 5 C of charge through a potential difference of 6 V. ~~ W = Q V|1 ~~ W = 5 x 6|1 ~~ W = 30 J|1
Write the symbols used in a circuit for a cell, a bulb, a switch (key closed) and a resistor. ~~ Cell: long and short parallel lines|1 ~~ Bulb: a circle with a cross|1 ~~ Resistor: a zig-zag line or rectangle|1
List three factors on which the resistance of a wire depends. ~~ Length|1 ~~ Area of cross-section|1 ~~ Nature of the material|1
Find the resistance of a series connection of 3 ohm, 4 ohm and 5 ohm. ~~ Rs = R1 + R2 + R3|1 ~~ 3 + 4 + 5|1 ~~ 12 ohm|1
Find the equivalent resistance of 6 ohm and 3 ohm in parallel. ~~ 1/R = 1/6 + 1/3|1 ~~ 1/R = 1/2|1 ~~ R = 2 ohm|1
A 40 W bulb works for 5 h daily. Find the energy used per day in kWh. ~~ Energy = P x t|1 ~~ 0.04 kW x 5 h|1 ~~ 0.2 kWh|1
An electric heater of 1000 W is used for 2 hours. Find the energy consumed in kWh. ~~ P = 1 kW|1 ~~ E = 1 x 2|1 ~~ E = 2 kWh|1
Calculate the power of a device with 220 V and 2 A. ~~ P = V I|1 ~~ P = 220 x 2|1 ~~ P = 440 W|1
Convert 1 kWh into joules. ~~ 1 kW = 1000 W|1 ~~ 1 h = 3600 s|1 ~~ 1 kWh = 3.6 x 10^6 J|1
State three advantages of parallel connection in homes. ~~ Each appliance gets full voltage|1 ~~ Each can be switched on or off independently|1 ~~ Failure of one does not affect others|1
Why is the resistance of the ammeter kept low? ~~ It is connected in series|1 ~~ It should not change the current|1 ~~ So that it does not reduce the current in the circuit|1
Why is tungsten used for the filament of an electric bulb? ~~ High melting point|1 ~~ High resistivity|1 ~~ Does not oxidise at the working temperature in inert gas|1
How is a fuse connected in a circuit? Why? ~~ In series with the appliance|1 ~~ Excess current melts it|1 ~~ Breaks the circuit and saves the appliance|1
Calculate the heat produced in 10 s by a 5 ohm resistor carrying 2 A. ~~ H = I^2 R t|1 ~~ 4 x 5 x 10|1 ~~ H = 200 J|1
""".strip()
eD = """
State Ohm's law. Draw (describe) the V-I graph and explain what its slope represents. ~~ Current is proportional to the potential difference at constant temperature|1 ~~ V = I R|1 ~~ Graph is a straight line through the origin|1 ~~ Slope = V / I|1 ~~ Slope gives the resistance|1
Explain the factors on which the resistance of a conductor depends. ~~ Length: R increases with length|1 ~~ Area: R decreases with area|1 ~~ Nature of the material|1 ~~ Temperature|1 ~~ R = rho L / A|1
Three resistors of 2 ohm, 4 ohm and 6 ohm are connected in series to a 12 V battery. Find the total resistance, current and voltage across each. ~~ R = 2 + 4 + 6 = 12 ohm|1 ~~ I = 12 / 12 = 1 A|1 ~~ V1 = 2 V|1 ~~ V2 = 4 V|1 ~~ V3 = 6 V|1
Two resistors of 10 ohm and 15 ohm are connected in parallel to a 6 V battery. Find the total resistance and the current in each. ~~ 1/R = 1/10 + 1/15 = 5/30|1 ~~ R = 6 ohm|1 ~~ I1 = 6 / 10 = 0.6 A|1 ~~ I2 = 6 / 15 = 0.4 A|1 ~~ Total current 1 A|1
Distinguish between series and parallel arrangements of resistors with respect to current, voltage, equivalent resistance, failure of one and use. ~~ Current: same vs divided|1 ~~ Voltage: divided vs same|1 ~~ Rs greater than each; Rp less than each|1 ~~ Failure: breaks all vs others work|1 ~~ Use: parallel in homes|1
Explain the heating effect of electric current. Give the formula and two uses. ~~ Electrical energy is converted to heat|1 ~~ Electrons collide with atoms|1 ~~ H = I^2 R t|1 ~~ Use: heater|1 ~~ Use: electric iron or bulb|1
A bulb rated 100 W at 220 V is used for 10 hours. Find the energy consumed in kWh and the current drawn. ~~ E = P t = 0.1 kW x 10 h|1 ~~ E = 1 kWh|1 ~~ I = P / V|1 ~~ I = 100 / 220|1 ~~ I = 0.45 A|1
Define electric power. Derive P = V I = I^2 R = V^2 / R. ~~ Power is work done per unit time|1 ~~ W = V Q = V I t|1 ~~ P = V I|1 ~~ Substituting V = I R: P = I^2 R|1 ~~ Substituting I = V / R: P = V^2 / R|1
An electric geyser of 2 kW is used for 3 hours daily. Find the energy used in 30 days and the cost at Rs 5 per kWh. ~~ Daily energy = 2 x 3 = 6 kWh|1 ~~ 30 days: 180 kWh|1 ~~ Cost = 180 x 5|1 ~~ Rs 900|1 ~~ 180 units are used|1
A wire of resistance 8 ohm is cut into two equal parts. Find the resistance of each part and the equivalent resistance when they are joined in parallel. ~~ Each part is half the length|1 ~~ Each part has 4 ohm|1 ~~ 1/R = 1/4 + 1/4|1 ~~ R = 2 ohm|1 ~~ Parallel resistance is less than each part|1
Explain why wires of copper are used in house wiring and nichrome in heaters. ~~ Copper has low resistivity|1 ~~ Less heat is produced in wires|1 ~~ Nichrome has high resistivity|1 ~~ It can withstand high temperatures|1 ~~ It does not oxidise readily|1
Explain with a labelled description how to connect an ammeter and a voltmeter to measure the current through and the voltage across a resistor. ~~ Cell, key, resistor and ammeter in series|1 ~~ Voltmeter is connected across the resistor|1 ~~ Positive terminals to the higher potential side|1 ~~ Ammeter has low resistance|1 ~~ Voltmeter has high resistance|1
""".strip()

# ============================ MEDIUM ============================
mA = """
The number of electrons passing per second through a conductor carrying 3.2 A is ~~ 2 x 10^19 ~~ 5 x 10^18 ~~ 2 x 10^18 ~~ 3.2 x 10^19 ~~ n = 3.2 / 1.6 x 10^-19.
A charge of 600 C flows in 5 minutes. The current is ~~ 2 A ~~ 3 A ~~ 120 A ~~ 0.5 A ~~ I = 600 / 300.
The work done in moving 4 C of charge across a potential difference of 9 V is ~~ 36 J ~~ 13 J ~~ 2.25 J ~~ 5 J ~~ W = V Q.
The V-I graph of a conductor has a slope of 5 ohm. If the current is 2 A, the voltage is ~~ 10 V ~~ 2.5 V ~~ 7 V ~~ 0.4 V ~~ V = I R.
If the potential difference across a fixed resistor is doubled, the current becomes ~~ twice ~~ half ~~ four times ~~ unchanged ~~ Ohm's law.
For a graph between V (y-axis) and I (x-axis), the quantity represented by the slope is ~~ resistance ~~ power ~~ conductance ~~ charge ~~ V / I = R.
The resistance of a wire is 10 ohm. If its length is tripled by stretching with the same volume, the resistance is nearly ~~ 90 ohm ~~ 30 ohm ~~ 3.3 ohm ~~ 10 ohm ~~ When the length is tripled the area becomes one third: R x 9.
A wire of radius r has resistance R. A wire of the same material and length but radius 2r has a resistance ~~ R/4 ~~ R/2 ~~ 4R ~~ 2R ~~ Area is four times.
A wire has resistance 12 ohm. It is cut into three equal pieces. The resistance of each piece is ~~ 4 ohm ~~ 12 ohm ~~ 36 ohm ~~ 1/4 ohm ~~ R is proportional to L.
The resistivity of a material depends on ~~ its nature and temperature ~~ its length ~~ its area ~~ the current through it ~~ Property of the material.

Three resistors of 6 ohm each are connected in parallel. The equivalent resistance is ~~ 2 ohm ~~ 18 ohm ~~ 6 ohm ~~ 3 ohm ~~ R / n.
A 10 ohm and a 40 ohm resistor are in parallel. The equivalent resistance is ~~ 8 ohm ~~ 50 ohm ~~ 25 ohm ~~ 5 ohm ~~ 400 / 50.
Resistors of 2 ohm, 3 ohm and 6 ohm are connected in parallel. The equivalent resistance is ~~ 1 ohm ~~ 11 ohm ~~ 3 ohm ~~ 2 ohm ~~ 1/2 + 1/3 + 1/6 = 1.
Two resistors of 4 ohm and 12 ohm in series are connected to a 16 V battery. The current is ~~ 1 A ~~ 4 A ~~ 0.25 A ~~ 16 A ~~ I = 16 / 16.
A circuit has 5 ohm in series with the parallel combination of 6 ohm and 3 ohm. The total resistance is ~~ 7 ohm ~~ 14 ohm ~~ 3.5 ohm ~~ 9 ohm ~~ 5 + 2.
A 6 V battery is connected to two resistors of 3 ohm and 6 ohm in series. The potential difference across the 3 ohm resistor is ~~ 2 V ~~ 4 V ~~ 6 V ~~ 3 V ~~ I = 6/9; V = 2 A/3 x 3.
Two identical bulbs are connected in series to a battery. Compared to a single bulb, each bulb is ~~ dimmer ~~ brighter ~~ equally bright ~~ off ~~ Voltage is shared.
Two identical bulbs connected in parallel to a battery, compared to the series connection, are ~~ brighter ~~ dimmer ~~ equally bright ~~ off ~~ Each gets full voltage.
The current through the 4 ohm resistor when 4 ohm and 12 ohm are in parallel across 12 V is ~~ 3 A ~~ 1 A ~~ 4 A ~~ 12 A ~~ I = 12 / 4.
The total current drawn from a 12 V battery by a 4 ohm and a 12 ohm resistor in parallel is ~~ 4 A ~~ 3 A ~~ 1 A ~~ 0.75 A ~~ 3 + 1.

The power of an electric device that draws 5 A at 220 V is ~~ 1100 W ~~ 44 W ~~ 225 W ~~ 1.1 W ~~ P = V I.
A 100 W bulb has a resistance at 220 V of ~~ 484 ohm ~~ 2.2 ohm ~~ 22 ohm ~~ 100 ohm ~~ V^2 / P.
A 2 kW heater runs for 30 minutes. Energy consumed is ~~ 1 kWh ~~ 2 kWh ~~ 60 kWh ~~ 4 kWh ~~ 2 x 0.5.
Heat produced by 3 A passing through 4 ohm for 10 s is ~~ 360 J ~~ 120 J ~~ 12 J ~~ 90 J ~~ 9 x 4 x 10.
If the current through a resistor is doubled, the heat produced in a given time becomes ~~ four times ~~ twice ~~ half ~~ unchanged ~~ H is proportional to I^2.
A fuse rated 5 A can safely run appliances up to a total power at 220 V of ~~ 1100 W ~~ 44 W ~~ 5500 W ~~ 220 W ~~ P = V I.
The cost of running a 1.5 kW heater for 4 hours at Rs 6 per unit is ~~ Rs 36 ~~ Rs 24 ~~ Rs 9 ~~ Rs 60 ~~ 6 kWh x 6.
Which of the following lamps has the highest resistance (all rated for 220 V)? ~~ 25 W ~~ 40 W ~~ 60 W ~~ 100 W ~~ R = V^2 / P is highest for the least power.
A 60 W bulb is used for 10 hours. The energy consumed in joules is ~~ 2.16 x 10^6 J ~~ 600 J ~~ 3.6 x 10^6 J ~~ 6 x 10^4 J ~~ 0.6 kWh x 3.6 x 10^6.
Which of these energy conversions occurs in an electric heater? ~~ Electrical to heat ~~ Heat to electrical ~~ Chemical to electrical ~~ Light to heat ~~ Joule heating.
""".strip()
mB = """
How many electrons flow per second through a conductor carrying a current of 0.8 A? ~~ n = I / e = 0.8 / 1.6 x 10^-19|1 ~~ n = 5 x 10^18|1
A 10 ohm resistor and a 15 ohm resistor are connected in series to a 5 V cell. Find the current. ~~ Rs = 25 ohm|1 ~~ I = 5 / 25 = 0.2 A|1
Calculate the resistance of 100 m of copper wire of area 1 mm^2 if rho = 1.7 x 10^-8 ohm m. ~~ R = rho L / A = 1.7 x 10^-8 x 100 / 10^-6|1 ~~ R = 1.7 ohm|1
How will the resistance of a wire change if its diameter is halved? ~~ Area becomes one-fourth|1 ~~ Resistance becomes four times|1
A 20 ohm resistor is connected in parallel with a 5 ohm resistor. Find the equivalent resistance. ~~ 1/R = 1/20 + 1/5 = 5/20|1 ~~ R = 4 ohm|1
Find the power of a heater that draws 4 A from a 220 V supply. ~~ P = V I|1 ~~ P = 220 x 4 = 880 W|1
The heat produced in a resistor is 400 J in 10 s when the current is 2 A. Find the resistance. ~~ H = I^2 R t|1 ~~ R = 400 / (4 x 10) = 10 ohm|1
Why does a heater coil get hot while the wires connecting it remain cool? ~~ Same current flows through both|1 ~~ Coil has high resistance so more I^2 R heat|1
Why is the series arrangement not used for home appliances? ~~ Voltage gets divided among the appliances|1 ~~ If one fails the others also stop|1
Find the cost of using a 60 W bulb for 5 hours daily for 30 days at Rs 6 per unit. ~~ Energy = 0.06 x 5 x 30 = 9 kWh|1 ~~ Cost = 9 x 6 = Rs 54|1
A bulb is marked 220 V, 55 W. Find the current. ~~ I = P / V|1 ~~ I = 55 / 220 = 0.25 A|1
A potential difference of 20 V is applied across a 5 ohm and a 15 ohm resistor in series. Find the voltage across the 15 ohm resistor. ~~ I = 20 / 20 = 1 A|1 ~~ V = 1 x 15 = 15 V|1
""".strip()
mC = """
A battery of 9 V is connected to 3 ohm, 4 ohm and 2 ohm in series. Find the current and the voltage across the 4 ohm resistor. ~~ R = 3 + 4 + 2 = 9 ohm|1 ~~ I = 9 / 9 = 1 A|1 ~~ V = I R = 4 V|1
Find the equivalent resistance of 3 resistors of 4 ohm, 6 ohm and 12 ohm connected in parallel and the current drawn from 6 V. ~~ 1/R = 1/4 + 1/6 + 1/12 = 6/12|1 ~~ R = 2 ohm|1 ~~ I = 6 / 2 = 3 A|1
A wire has a resistance of 16 ohm. It is cut into four equal parts and the parts are joined in parallel. Find the equivalent resistance. ~~ Each part = 4 ohm|1 ~~ 1/R = 4 x 1/4 = 1|1 ~~ R = 1 ohm|1
In a series circuit of 5 ohm and 10 ohm with a 6 V source, find the potential difference across each and the power dissipated in the circuit. ~~ I = 6 / 15 = 0.4 A|1 ~~ V1 = 2 V, V2 = 4 V|1 ~~ P = V I = 6 x 0.4 = 2.4 W|1
A conductor of resistance 5 ohm has current 3 A for 2 minutes. Find the heat produced. ~~ H = I^2 R t|1 ~~ 9 x 5 x 120|1 ~~ H = 5400 J|1
A bulb is rated 40 W at 220 V. Find the resistance and the current. If it is used at 110 V, find the power consumed approximately. ~~ R = 220^2 / 40 = 1210 ohm|1 ~~ I = 40 / 220 = 0.18 A|1 ~~ At 110 V, P = 110^2 / 1210 = 10 W|1
Explain with the help of a formula why a thick wire is used for heavy current. ~~ R = rho L / A|1 ~~ Greater area gives lower resistance|1 ~~ Less heat I^2 R t, so the wire does not overheat|1
Why do two bulbs of 60 W and 100 W, both rated 220 V, have different resistances? Which has more? ~~ R = V^2 / P|1 ~~ 60 W bulb: R = 806.7 ohm|1 ~~ 100 W bulb: 484 ohm, so 60 W has more resistance|1
Compare the resistivity of copper (1.6 x 10^-8) and nichrome (1.1 x 10^-6) ohm m. For wires of the same size, find the ratio of resistances. ~~ R is proportional to rho|1 ~~ Ratio = 1.1 x 10^-6 / 1.6 x 10^-8|1 ~~ About 69 times larger for nichrome|1
A 2 ohm resistor is connected in series with a parallel combination of 3 ohm and 6 ohm and a 6 V battery. Find the current from the battery. ~~ Parallel part = 18 / 9 = 2 ohm|1 ~~ Total R = 4 ohm|1 ~~ I = 6 / 4 = 1.5 A|1
The current in a conductor is 2 A at 8 V. What current flows at 20 V if the temperature does not change? ~~ R = 8 / 2 = 4 ohm|1 ~~ I = 20 / 4|1 ~~ I = 5 A|1
A student plots V versus I for two resistors and finds the slopes are 2 ohm and 6 ohm. Which resistor is thicker if they are the same length and material? ~~ Slope gives resistance|1 ~~ R is inversely proportional to area|1 ~~ 2 ohm resistor is thicker|1
How many 220 ohm resistors must be connected in parallel to draw a total current of 5 A from a 220 V line? ~~ Required equivalent R = 220 / 5 = 44 ohm|1 ~~ n resistors in parallel give 220 / n|1 ~~ n = 5|1
Find the energy consumed by three bulbs of 60 W, each used for 4 h daily for 30 days. ~~ Daily = 3 x 0.06 x 4 = 0.72 kWh|1 ~~ In 30 days = 21.6 kWh|1 ~~ 21.6 units|1
Why is a fuse wire of a lower melting point and a smaller rating than the wire of the appliance? ~~ It must melt before the appliance wire gets hot|1 ~~ Excess current heats and melts it|1 ~~ Circuit breaks and protects the appliance|1
How much charge passes through a bulb of 100 W at 220 V in 10 minutes? ~~ I = 100 / 220 = 0.4545 A|1 ~~ t = 600 s|1 ~~ Q = I t = 272.7 C|1
An electric kettle draws 5 A at 220 V. How long does it take to produce 3.3 x 10^5 J of heat? ~~ P = 1100 W|1 ~~ t = H / P|1 ~~ t = 300 s|1
A resistor of 12 ohm is connected to a battery of unknown voltage and carries 2 A. Find the voltage and the power. ~~ V = I R = 24 V|1 ~~ P = V I|1 ~~ P = 48 W|1
""".strip()
mD = """
A circuit has three resistors: 6 ohm and 3 ohm in parallel, in series with 4 ohm, connected to a 12 V battery. Find (a) the total resistance (b) the current from the battery (c) the voltage across the parallel combination (d) the current through each parallel resistor. ~~ (a) Parallel = 2 ohm; total = 6 ohm|1 ~~ (b) I = 12 / 6 = 2 A|1 ~~ (c) V = 2 x 2 = 4 V|1 ~~ (d) I in 6 ohm = 4/6 = 0.67 A|1 ~~ I in 3 ohm = 4/3 = 1.33 A|1
Three resistors of 10 ohm, 20 ohm and 30 ohm are in series. (a) Find the equivalent resistance. (b) What is the current if a 12 V battery is used? (c) Find the power dissipated in each. ~~ (a) R = 60 ohm|1 ~~ (b) I = 12 / 60 = 0.2 A|1 ~~ (c) P1 = I^2 R = 0.4 W|1 ~~ P2 = 0.8 W|1 ~~ P3 = 1.2 W|1
A wire of length 2 m, area 0.4 mm^2 and resistivity 1.6 x 10^-8 ohm m is connected to a 4 V battery. Find its resistance, the current and the power dissipated. ~~ R = rho L / A = 1.6 x 10^-8 x 2 / 0.4 x 10^-6|1 ~~ R = 0.08 ohm|1 ~~ I = 4 / 0.08 = 50 A|1 ~~ P = V I = 200 W|1 ~~ Large current means heavy heating|1
Derive the formula for the equivalent resistance of two resistors in parallel and find the equivalent of 8 ohm and 24 ohm and the current from 12 V. ~~ I = I1 + I2 and V is the same|1 ~~ 1/Rp = 1/R1 + 1/R2|1 ~~ 1/Rp = 1/8 + 1/24 = 4/24|1 ~~ Rp = 6 ohm|1 ~~ I = 12 / 6 = 2 A|1
A 1.5 kW geyser and a 100 W fan, a 60 W bulb are used for 4 hours, 8 hours and 6 hours respectively every day. Calculate the monthly (30 days) bill at Rs 7 per unit. ~~ Geyser: 1.5 x 4 = 6 kWh|1 ~~ Fan: 0.1 x 8 = 0.8 kWh|1 ~~ Bulb: 0.06 x 6 = 0.36 kWh|1 ~~ Daily = 7.16 kWh; 30 days = 214.8 kWh|1 ~~ Bill = 214.8 x 7 = Rs 1503.6|1
Two lamps, one rated 100 W at 220 V and the other 25 W at 220 V, are connected in series across 220 V. Which glows brighter? Find the current. ~~ R1 = 484 ohm; R2 = 1936 ohm|1 ~~ Total R = 2420 ohm|1 ~~ I = 220 / 2420 = 0.0909 A|1 ~~ Same current, P = I^2 R is larger for larger R|1 ~~ The 25 W lamp glows brighter|1
Explain Joule's law of heating. Find the heat produced when a current of 2 A flows through a 50 ohm resistor for 10 minutes. State the heat in calories (1 cal = 4.2 J). ~~ H = I^2 R t|1 ~~ H = 4 x 50 x 600|1 ~~ H = 1.2 x 10^5 J|1 ~~ In calories: 1.2 x 10^5 / 4.2|1 ~~ = 28571 cal|1
How can you use four (or fewer) resistors of 2 ohm each to get (a) 8 ohm (b) 0.5 ohm (c) 2 ohm (d) 3 ohm? ~~ (a) All four in series: 8 ohm|1 ~~ (b) All four in parallel: 2/4 = 0.5 ohm|1 ~~ (c) Two series pairs (4 ohm each) joined in parallel: 2 ohm|1 ~~ (d) Two in parallel (1 ohm) in series with one more 2 ohm: 3 ohm|1 ~~ Series raises and parallel lowers the resistance|1
A battery of 12 V and a bulb of 6 V, 3 W is to be used with a resistor so that the bulb glows normally. Find the series resistor. ~~ Current of the bulb = 3 / 6 = 0.5 A|1 ~~ Voltage across the resistor = 12 - 6 = 6 V|1 ~~ R = 6 / 0.5|1 ~~ R = 12 ohm|1 ~~ Power dissipated in resistor = 3 W|1
Explain why the resistance of a wire changes when it is stretched to double its length. Find the new resistance if the original is 5 ohm. ~~ Volume is constant, so the area becomes half|1 ~~ Length is doubled|1 ~~ R = rho (2L) / (A/2)|1 ~~ New R = 4 x 5|1 ~~ R = 20 ohm|1
In a circuit, two bulbs of 40 W and 60 W (each rated 220 V) are connected (a) in series (b) in parallel across 220 V. Which glows brighter in each case? Explain. ~~ R40 = 1210 ohm, R60 = 806.7 ohm|1 ~~ Series: same current|1 ~~ P = I^2 R so 40 W bulb glows brighter|1 ~~ Parallel: same voltage, P = V^2 / R|1 ~~ The 60 W bulb glows brighter|1
An electric iron of 1 kW is used on 220 V for 2 hours daily. (a) Find the current drawn (b) the resistance of its element (c) the energy used in a month of 30 days in kWh and in joules. ~~ (a) I = 1000 / 220 = 4.55 A|1 ~~ (b) R = 220^2 / 1000 = 48.4 ohm|1 ~~ (c) Daily energy = 1 x 2 = 2 kWh|1 ~~ Monthly = 60 kWh|1 ~~ In joules: 60 x 3.6 x 10^6 = 2.16 x 10^8 J|1
""".strip()

# ============================ HARD ============================
hA = """
AR ~~ A voltmeter is connected in parallel with a resistor. ~~ A voltmeter has a very high resistance. ~~ a ~~ High resistance draws almost no current.
AR ~~ Copper wires are used for transmission of electricity. ~~ Copper has high resistivity. ~~ c ~~ A is true; R is false: copper has low resistivity.
AR ~~ The resistance of a conductor increases with temperature. ~~ At a high temperature, the electrons collide more often with the atoms. ~~ a ~~ Greater collisions give more resistance.
AR ~~ Parallel combination of resistors is used in houses. ~~ Each appliance gets the same voltage and works independently. ~~ a ~~ Parallel arrangement features.
AR ~~ The fuse wire is made of a metal of low melting point. ~~ It must melt when the current exceeds the safe limit. ~~ a ~~ The fuse protects appliances.
AR ~~ The equivalent resistance of two resistors in parallel is more than that of each. ~~ More paths are available for the flow of current. ~~ d ~~ A is false; R is true: parallel resistance is less than each.
AR ~~ Nichrome is used in heating elements. ~~ Nichrome has low melting point and low resistivity. ~~ c ~~ A is true; R is false: nichrome has high resistivity and high melting point.
AR ~~ Electric current is a scalar quantity. ~~ Currents add arithmetically at a junction and do not follow the rules of vector addition. ~~ a ~~ Currents are added algebraically (Kirchhoff's rule is not required), so current is a scalar.
AR ~~ The bulb in a flashlight glows immediately on closing the switch even though electrons drift slowly. ~~ The electric field is set up in the conductor almost instantly. ~~ a ~~ The field moves with a high speed along the wire.
AR ~~ A 60 W bulb has a higher resistance than a 100 W bulb for the same voltage rating. ~~ Resistance is given by V squared divided by power for a rated bulb. ~~ a ~~ R = V^2 / P.

The resistance of a wire of length L and area A is 12 ohm. A second wire of the same material has length 2L and radius double that of the first. Its resistance is ~~ 6 ohm ~~ 12 ohm ~~ 24 ohm ~~ 3 ohm ~~ R2 = rho 2L / 4A = R / 2.
A wire is stretched to three times its length with its volume unchanged. The new resistance is ~~ 9 R ~~ 3 R ~~ R / 3 ~~ R / 9 ~~ L is tripled, A is one third.
A cylindrical wire of resistance R is cut into n equal parts which are joined in parallel. The equivalent resistance is ~~ R / n^2 ~~ R / n ~~ n R ~~ n^2 R ~~ Each part R/n; parallel gives R/n^2.
A cell of emf 6 V is connected across 2 ohm and 4 ohm in parallel. The total power delivered is ~~ 27 W ~~ 18 W ~~ 9 W ~~ 6 W ~~ P = V^2 (1/2 + 1/4) = 36 x 0.75.
When two resistors are connected in series the equivalent is 9 ohm and in parallel it is 2 ohm. The resistors are ~~ 3 ohm and 6 ohm ~~ 4 ohm and 5 ohm ~~ 2 ohm and 7 ohm ~~ 1 ohm and 8 ohm ~~ 3 + 6 = 9 and 18 / 9 = 2.
Two bulbs of 60 W and 100 W (both rated 220 V) are connected in series across 220 V. The bulb that glows brighter is ~~ 60 W ~~ 100 W ~~ both equally ~~ neither ~~ Same current, larger R dissipates more power.
Two bulbs of 40 W and 100 W, both rated 220 V, are in parallel across 220 V. The current drawn is ~~ 0.64 A ~~ 0.18 A ~~ 0.45 A ~~ 1.4 A ~~ (140 W) / 220.
An electric kettle rated 1.1 kW at 220 V is connected to a 110 V supply. The power drawn is nearly ~~ 275 W ~~ 550 W ~~ 1100 W ~~ 2200 W ~~ P is proportional to V^2.
The ratio of resistances of 60 W and 100 W bulbs of the same voltage rating is ~~ 5 : 3 ~~ 3 : 5 ~~ 6 : 10 ~~ 1 : 1 ~~ R is proportional to 1/P.
The current in a resistor R is doubled by changing the voltage. The power dissipated becomes ~~ four times ~~ twice ~~ the same ~~ half ~~ P = I^2 R.

Which graph is a straight line through the origin for a metallic conductor at constant temperature? ~~ V against I ~~ V against t ~~ I against R ~~ P against I ~~ Ohm's law.
In the circuit, ammeter reads 2 A and voltmeter across the resistor reads 10 V. The resistance is ~~ 5 ohm ~~ 20 ohm ~~ 12 ohm ~~ 0.2 ohm ~~ R = V / I.
For the given resistors of 3 ohm, 6 ohm connected in parallel and then in series with 2 ohm and a 6 V cell, the current is ~~ 1.5 A ~~ 3 A ~~ 1 A ~~ 0.75 A ~~ R = 2 + 2 = 4 ohm.
The effective resistance between two ends when four 4 ohm resistors are in a parallel-series arrangement of two in series in each of two parallel branches is ~~ 4 ohm ~~ 8 ohm ~~ 2 ohm ~~ 16 ohm ~~ Each branch 8 ohm; two in parallel gives 4 ohm.
A heater coil has resistance R and gives out heat Q in a time t. If it is cut to half its length and used on the same supply, the heat in the same time is ~~ 2 Q ~~ Q / 2 ~~ Q ~~ 4 Q ~~ R halves; H = V^2 t / R doubles.
A battery supplies 36 W to two identical resistors connected in series. If they are connected in parallel to the same battery, the power would be ~~ 144 W ~~ 72 W ~~ 18 W ~~ 36 W ~~ Series: V^2/(2R) = 36; parallel: V^2 (2/R) = 4 times.
A metal wire carries 2 A. Heat produced in 10 s is 400 J. If the current is raised to 4 A for 5 s, the heat produced is ~~ 800 J ~~ 400 J ~~ 1600 J ~~ 200 J ~~ H = I^2 R t; 16 / 4 x 1 / 2 x 400.
The kilowatt hour used by a 250 W lamp for 4 hours is ~~ 1 kWh ~~ 250 kWh ~~ 0.25 kWh ~~ 4 kWh ~~ 0.25 x 4.
Which of these changes will NOT increase the resistance of a copper wire? ~~ Reducing the temperature ~~ Doubling the length ~~ Halving the area ~~ Replacing with nichrome ~~ Lower temperature decreases R.
A fuse of rating 3 A is used in a circuit with appliances of 220 V. The total power which can be used is ~~ 660 W ~~ 220 W ~~ 73 W ~~ 1100 W ~~ 220 x 3.
""".strip()
hB = """
Calculate the number of electrons flowing per second in a wire carrying 4.8 mA. ~~ I = 4.8 x 10^-3 A|1 ~~ n = 4.8 x 10^-3 / 1.6 x 10^-19 = 3 x 10^16|1
A wire of resistance 4 ohm is bent to form a circle. Find its resistance between two diametrically opposite points. ~~ Two halves of 2 ohm each in parallel|1 ~~ R = 1 ohm|1
A 12 ohm resistor and a 4 ohm resistor are in parallel with a total current of 4 A. Find the current in the 4 ohm resistor. ~~ Current divides inversely to resistance|1 ~~ I = 4 x 12 / 16 = 3 A|1
Two resistors, when connected in series, have a total of 25 ohm and in parallel 4 ohm. Find the resistors. ~~ R1 + R2 = 25 and R1 R2 = 100|1 ~~ R1 = 5 ohm and R2 = 20 ohm|1
A heater of 800 W is connected to a 220 V source. Find the resistance and the heat produced in 5 minutes. ~~ R = 220^2 / 800 = 60.5 ohm|1 ~~ H = P t = 800 x 300 = 2.4 x 10^5 J|1
A resistor dissipates 100 W when connected to 100 V. What power will it dissipate at 50 V? ~~ P is proportional to V^2|1 ~~ P = 100 x (1/4) = 25 W|1
Why does the filament of a bulb break more easily when switched on? ~~ Cold filament has low resistance so a large current flows|1 ~~ Sudden heating weakens it|1
A bulb rated 60 W, 220 V is connected to 110 V. Find the current drawn. ~~ R = 806.7 ohm|1 ~~ I = 110 / 806.7 = 0.136 A|1
How does the resistance of a 100 W bulb compare with a 25 W bulb of the same voltage rating? ~~ R = V^2 / P|1 ~~ Ratio R100 : R25 = 1 : 4|1
An electric heater draws 10 A at 220 V. Find the energy used in 2 hours in kWh and the cost at Rs 6 per unit. ~~ P = 2.2 kW|1 ~~ E = 4.4 kWh, cost = Rs 26.4|1
Why is the power rating of a fuse specified as a current rating? ~~ Heat produced depends on I^2 R t|1 ~~ The fuse melts when the current exceeds the limit|1
What is the effect on the heat produced in a wire if both the current and the resistance are doubled for the same time? ~~ H = I^2 R t|1 ~~ H becomes 8 times|1
""".strip()
hC = """
The resistance of a copper wire is 2.5 ohm at 20 degrees Celsius. Why does its resistance rise at high temperature, and what is the effect on the current if the voltage is constant? ~~ Atoms vibrate more, increasing collisions with electrons|1 ~~ Resistance increases|1 ~~ Current decreases (I = V / R)|1
Two wires of the same material and length have radii in the ratio 1 : 2. Find the ratio of their resistances and of the currents when they are connected in parallel across a battery. ~~ Area ratio = 1 : 4|1 ~~ R1 : R2 = 4 : 1|1 ~~ Parallel: I1 : I2 = 1 : 4|1
Resistors of 1 ohm, 2 ohm and 3 ohm are connected in series to a 12 V source. Find the power dissipated in each and the total. ~~ I = 12 / 6 = 2 A|1 ~~ P1 = 4 W, P2 = 8 W, P3 = 12 W|1 ~~ Total = 24 W = V I|1
A wire of resistance R is stretched to double its length and then folded into two equal parts connected in parallel. Find the resulting resistance. ~~ Stretched resistance = 4R|1 ~~ Each half = 2R|1 ~~ Parallel: R|1
A cell sends 0.5 A through a 4 ohm resistor and 0.25 A through an 8 ohm resistor. Find the emf and the internal resistance. ~~ 0.5 (4 + r) = 0.25 (8 + r)|1 ~~ 2 + 0.5 r = 2 + 0.25 r|1 ~~ r = 0, emf = 2 V|1
A hot plate with a resistance of 55 ohm works on 220 V. Find the current, the power and the cost of using it for 5 hours at Rs 5 per unit. ~~ I = 220 / 55 = 4 A|1 ~~ P = 880 W|1 ~~ E = 0.88 x 5 = 4.4 kWh, cost Rs 22|1
Three bulbs of 100 W each rated 220 V are connected in parallel with a 220 V source. Find the total current and the equivalent resistance. ~~ P = 300 W|1 ~~ I = 300 / 220 = 1.36 A|1 ~~ R = 220 / 1.36 = 161.3 ohm|1
A student connects a voltmeter in series with the resistor by mistake. What will happen and why? ~~ Voltmeter has a very high resistance|1 ~~ Total resistance becomes very high|1 ~~ Almost no current flows and the bulb will not glow|1
Why do we use the kWh instead of the joule for household energy bills? ~~ Joule is a very small unit|1 ~~ 1 kWh = 3.6 x 10^6 J|1 ~~ kWh is convenient|1
Why does a heater coil shorten if a part of it breaks and is rejoined, and what happens to its power? ~~ Resistance decreases as length falls|1 ~~ P = V^2 / R increases|1 ~~ The coil gets hotter|1
The resistance between points A and B of a 12 ohm wire bent into a square is calculated between adjacent corners. Find it. ~~ Each side 3 ohm|1 ~~ One side 3 ohm in parallel with the other three sides 9 ohm|1 ~~ R = 27 / 12 = 2.25 ohm|1
How will the brightness of a bulb change if one more identical bulb is connected in series with it? Explain. ~~ Total resistance doubles|1 ~~ Current halves|1 ~~ Each bulb glows dimmer|1
Why are ammeters of low resistance and voltmeters of high resistance? ~~ Ammeter in series should not add to the resistance|1 ~~ Voltmeter in parallel should not draw current|1 ~~ Else the readings are altered|1
For a given resistor, the current is 0.2 A for 4 V. If the voltage is increased to 10 V, find the new current and power. ~~ R = 4 / 0.2 = 20 ohm|1 ~~ I = 10 / 20 = 0.5 A|1 ~~ P = 5 W|1
Why is the electric power transmitted at a very high voltage over long distances? ~~ Current is lower for the same power|1 ~~ Heat I^2 R t in the lines is reduced|1 ~~ Less power is wasted|1
In a circuit, two resistors of 6 ohm and 12 ohm are in parallel and the current in the 6 ohm resistor is 2 A. Find the total current and the voltage. ~~ V = 2 x 6 = 12 V|1 ~~ I in 12 ohm = 1 A|1 ~~ Total = 3 A|1
A nichrome wire and a copper wire of the same dimensions are connected in series. Which gets hotter and why? ~~ Same current flows|1 ~~ Nichrome has higher resistance|1 ~~ H = I^2 R t is greater for nichrome|1
The current of 2 A flows through the resistor of 10 ohm. How much charge flows and how much energy is dissipated in 30 s? ~~ Q = 2 x 30 = 60 C|1 ~~ V = 20 V|1 ~~ E = V Q = 1200 J|1
""".strip()
hD = """
A cell of 12 V and negligible internal resistance is connected to a 6 ohm resistor in series with a parallel pair of 12 ohm and 4 ohm. Find (a) the equivalent resistance (b) the main current (c) the current through each resistor in parallel (d) the power consumed in the circuit. ~~ (a) Parallel part = 48 / 16 = 3 ohm; total = 9 ohm|1 ~~ (b) I = 12 / 9 = 1.33 A|1 ~~ (c) Voltage across parallel = 1.33 x 3 = 4 V|1 ~~ Currents: 4/12 = 0.33 A and 4/4 = 1 A|1 ~~ (d) P = 12 x 1.33 = 16 W|1
A wire of resistance 10 ohm is stretched uniformly to three times its length. Find the new resistance. The stretched wire is then folded into three equal parts and joined in parallel. Find the final resistance. ~~ New R = 9 x 10 = 90 ohm|1 ~~ Each third = 30 ohm|1 ~~ 1/R = 3 / 30|1 ~~ R = 10 ohm|1 ~~ Resistance comes back to the original|1
An electric motor of 2 kW is run for 3 hours every day, an iron of 750 W for 1 hour, and 5 bulbs of 60 W for 6 hours daily. If one unit costs Rs 6.50, find the monthly (30 days) bill. ~~ Motor: 6 kWh|1 ~~ Iron: 0.75 kWh|1 ~~ Bulbs: 5 x 0.06 x 6 = 1.8 kWh|1 ~~ Daily 8.55 kWh; month 256.5 kWh|1 ~~ Bill = 256.5 x 6.5 = Rs 1667.25|1
Explain how the V-I characteristics are used to find the resistance when two readings are given: at 2 V the current is 0.4 A and at 6 V the current is 1.2 A. Is the conductor ohmic? Find the power at 6 V. ~~ R1 = 2 / 0.4 = 5 ohm|1 ~~ R2 = 6 / 1.2 = 5 ohm|1 ~~ R is the same, so ohmic|1 ~~ P = V I = 6 x 1.2|1 ~~ P = 7.2 W|1
Establish the relation between the heat produced, the current, the resistance and the time. A nichrome coil produces 8.4 x 10^5 J in 10 minutes from a 220 V supply. Find its resistance and the current. ~~ H = V Q = V I t = I^2 R t|1 ~~ P = H / t = 8.4 x 10^5 / 600 = 1400 W|1 ~~ I = P / V = 6.36 A|1 ~~ R = V / I|1 ~~ R = 34.6 ohm|1
A student has resistors of 3 ohm, 6 ohm and 9 ohm. Show how she can obtain (a) the highest possible resistance (b) the lowest possible resistance (c) 11 ohm. Verify with calculations. ~~ (a) All in series: 3 + 6 + 9 = 18 ohm|1 ~~ (b) All in parallel: 1/R = 1/3 + 1/6 + 1/9 = 11/18|1 ~~ R = 1.64 ohm|1 ~~ (c) 3 ohm and 6 ohm in parallel give 2 ohm|1 ~~ Adding 9 ohm in series gives 9 + 2 = 11 ohm|1
An electric heater has two coils of 20 ohm and 30 ohm that can be used singly, in series or in parallel on a 120 V supply. Find the power in each of the four modes and identify the highest-power mode. ~~ 20 ohm: P = 14400 / 20 = 720 W|1 ~~ 30 ohm: P = 480 W|1 ~~ Series 50 ohm: 288 W|1 ~~ Parallel 12 ohm: 1200 W|1 ~~ Parallel gives the highest power|1
Two bulbs rated 60 W and 40 W at 220 V are connected in series and the supply is 220 V. Find the current, the voltage across each and the power consumed by each. ~~ R60 = 806.7 ohm; R40 = 1210 ohm|1 ~~ Total = 2016.7 ohm; I = 0.109 A|1 ~~ V60 = 88 V; V40 = 132 V|1 ~~ P60 = 9.6 W|1 ~~ P40 = 14.4 W|1
Explain the working of an electric fuse and how a fuse rating is chosen for a 2.2 kW geyser used at 220 V. Why is a 5 A fuse unsuitable? ~~ Fuse wire melts when the current exceeds a limit|1 ~~ It is connected in series|1 ~~ Current of the geyser = 2200 / 220 = 10 A|1 ~~ A fuse of rating a little above 10 A (e.g. 15 A) is chosen|1 ~~ A 5 A fuse would melt|1
The following readings are taken for a resistor: V = 1 V, I = 0.1 A; V = 2 V, I = 0.2 A; V = 3 V, I = 0.3 A. Find the resistance from the graph, the power at 3 V and verify Ohm's law. If the same resistor is a wire of area 1 mm^2 and length 5 m, find the resistivity. ~~ V / I = 10 ohm each time|1 ~~ So Ohm's law holds|1 ~~ P = 3 x 0.3 = 0.9 W|1 ~~ rho = R A / L = 10 x 10^-6 / 5|1 ~~ rho = 2 x 10^-6 ohm m|1
Compare the series and parallel arrangements of two identical bulbs on a battery with reference to the brightness, the total power and the effect of the failure of one bulb. Support with a numerical example for two 10 ohm bulbs on 20 V. ~~ Series: R = 20 ohm, I = 1 A|1 ~~ Series total power = 20 W|1 ~~ Parallel: R = 5 ohm, I = 4 A|1 ~~ Parallel total power = 80 W; each bulb 40 W|1 ~~ Series: failure of one stops both; parallel: the other continues|1
A power station delivers 22 kW to a village through a line of total resistance 2 ohm. Compare the power lost in the line if the power is sent at 220 V and at 2200 V. ~~ At 220 V: I = 22000 / 220 = 100 A|1 ~~ Loss = I^2 R = 10000 x 2 = 20000 W|1 ~~ At 2200 V: I = 10 A|1 ~~ Loss = 100 x 2 = 200 W|1 ~~ High-voltage transmission reduces the loss 100 times|1
""".strip()

TIERS = {"NCERT": tier(nA, nB, nC, nD), "Easy": tier(eA, eB, eC, eD), "Medium": tier(mA, mB, mC, mD), "Hard": tier(hA, hB, hC, hD)}
