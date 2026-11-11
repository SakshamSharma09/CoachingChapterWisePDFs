"""Class 10 Science Ch 11 Electricity - extras."""
from common import AR4, Q

AR = [
 AR4(r"An ammeter is connected in series in a circuit.", r"An ammeter has a very low resistance.", "a",
     r"A low-resistance meter in series does not change the current it is measuring."),
 AR4(r"The resistance of a conductor is directly proportional to its length.", r"The resistivity of a material depends on its temperature.", "b",
     r"Both true ($R=\rho l/A$ and $\rho$ changes with temperature), but R does not explain A."),
 AR4(r"In a series combination of resistors, the current is the same through every resistor.", r"In a series combination the potential difference across each resistor is the same.", "c",
     r"In series the current is the same but the potential difference divides; R is false."),
 AR4(r"A fuse wire is made of a material of high melting point.", r"A fuse protects a circuit by melting when an excessive current flows through it.", "d",
     r"A fuse wire has a low melting point so that it melts easily; A is false and R is true."),
 AR4(r"Household appliances are connected in parallel.", r"In parallel each appliance gets the same potential difference and can be operated independently.", "a",
     r"R states why parallel connection is preferred."),
 AR4(r"Tungsten is used for the filaments of electric bulbs.", r"Alloys have higher resistivity than the metals of which they are made.", "b",
     r"Both true; tungsten is chosen for its very high melting point, which R does not mention."),
]

CASE = [
 Q(r"<b>Case study.</b> In an experiment, a student connects a nichrome wire to a variable battery and notes the readings: when the potential difference is 2 V the current is 0.4 A; at 4 V it is 0.8 A and at 6 V it is 1.2 A. "
   r"(i) Find the resistance of the wire. (ii) What is the shape of the V-I graph? (iii) State Ohm's law. (iv) The wire is cut into two equal halves and the two halves are joined in parallel. Find the resistance of the combination.",
   r"(i) $R=V/I=2/0.4=5\ \Omega$ (1). (ii) A straight line passing through the origin (1). (iii) At constant temperature the current through a conductor is directly proportional to the potential difference across its ends (1). (iv) Each half has resistance $2.5\ \Omega$ (1); in parallel $R=2.5/2=1.25\ \Omega$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Priya has three resistors of $2\ \Omega$, $3\ \Omega$ and $6\ \Omega$ and a 6 V battery. She first joins the three resistors in series and then in parallel. "
   r"(i) Find the equivalent resistance in the series combination. (ii) Find the equivalent resistance in the parallel combination. (iii) Find the total current drawn from the battery in the parallel combination. (iv) Find the current through each resistor in the parallel combination and verify that they add up to the total current.",
   r"(i) $2+3+6=11\ \Omega$ (1). (ii) $\dfrac1R=\dfrac12+\dfrac13+\dfrac16=1$, so $R=1\ \Omega$ (1). (iii) $I=V/R=6/1=6$ A (1). (iv) $6/2=3$ A, $6/3=2$ A, $6/6=1$ A (1); $3+2+1=6$ A which equals the total current (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Mr Sharma's home in Jaipur has a 1500 W geyser used for 2 hours daily and four 100 W bulbs used for 5 hours daily. The electricity company charges Rs 6 per unit (1 unit = 1 kWh). Assume a 30-day month. "
   r"(i) Calculate the energy consumed by the geyser in one day in kWh. (ii) Calculate the energy consumed by the four bulbs in one day. (iii) How many joules are there in 1 kWh? (iv) Calculate the electricity bill for 30 days.",
   r"(i) $1.5\times2=3$ kWh (1). (ii) $4\times0.1\times5=2$ kWh (1). (iii) $3.6\times10^{6}$ J (1). (iv) Total per day $=5$ kWh (1); for 30 days $=150$ units, bill $=150\times6=$ Rs 900 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Charge, current, potential difference", [r"Current $I=\dfrac Qt$ (unit ampere, A = C/s); charge of an electron $=1.6\times10^{-19}$ C; 1 C $\approx6\times10^{18}$ electrons.",
   r"Potential difference $V=\dfrac WQ$ (unit volt, V = J/C). Conventional current flows from the positive to the negative terminal.",
   r"Ammeter: in series, low resistance. Voltmeter: in parallel, high resistance."]),
 ("Ohm's law and resistance", [r"$V=IR$ (at constant temperature); $R$ in ohm ($\Omega$).",
   r"$R=\rho\dfrac lA$; $\rho$ is resistivity (unit $\Omega$ m), depends on material and temperature, not on size. Resistance $\propto l$, $\propto\dfrac1A$.",
   r"Metals: low $\rho$; alloys: higher $\rho$, do not oxidise readily (nichrome in heaters); tungsten filament for bulbs (high melting point)."]),
 ("Combinations", [r"Series: $R_s=R_1+R_2+R_3$; same current, voltage divides, $V=V_1+V_2+V_3$.",
   r"Parallel: $\dfrac1{R_p}=\dfrac1{R_1}+\dfrac1{R_2}+\dfrac1{R_3}$; same voltage, current divides, $I=I_1+I_2+I_3$; $R_p$ is less than the smallest resistor.",
   r"Two equal resistors $R$: series $2R$, parallel $\dfrac R2$."]),
 ("Heating effect, power and energy", [r"$H=I^2Rt$ (joule's law of heating, $H$ in J, $t$ in s).",
   r"Power $P=VI=I^2R=\dfrac{V^2}{R}$ (unit watt, W). Energy $E=Pt$.",
   r"1 kWh $=3.6\times10^{6}$ J (one unit of electrical energy). Uses: electric heater, bulb filament, fuse (low melting point)."]),
]

MISTAKES = [
 r"Adding the reciprocals incorrectly: for resistors in parallel $\frac1{R_p}=\sum\frac1R$ and the final answer is $R_p$, not the sum of reciprocals.",
 r"Connecting an ammeter in parallel or a voltmeter in series; the ammeter goes in series and the voltmeter in parallel.",
 r"Thinking that resistance is directly proportional to cross-sectional area; $R\propto\frac1A$ and $R\propto l$.",
 r"Using $H=I^2Rt$ with $t$ in minutes or hours; time must be in seconds (and energy in kWh needs power in kW and time in hours).",
 r"Writing that in a series circuit the voltage across each resistor is the same; the <b>current</b> is the same in series and the <b>voltage</b> is the same in parallel.",
 r"Forgetting that 1 kWh equals $3.6\times10^6$ J; and confusing the unit of resistivity ($\Omega$ m) with that of resistance ($\Omega$).",
]
