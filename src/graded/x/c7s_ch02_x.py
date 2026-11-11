"""Class 7 Science Ch 2 Electricity: Circuits and their Components - extras."""
from common import AR4, Q

AR = [
 AR4("A bulb glows when the switch in its circuit is closed.", "A closed switch completes the circuit so that current can flow.", "a",
     "Current flows only in a complete (closed) circuit, so R explains why the bulb glows."),
 AR4("A fuse is connected in series with an electrical appliance.", "Fuse wire has a very high melting point, so it never melts.", "c",
     "A fuse is in series, so A is true; but fuse wire has a LOW melting point and melts when current is too large, so R is false."),
 AR4("Electric wires are covered with plastic or rubber.", "Copper is a good conductor of electricity.", "b",
     "Both are true, but the plastic covering is used because it is an insulator, which R does not explain."),
 AR4("A bulb glows even when there is a gap in the circuit.", "Current flows only in a closed circuit.", "d",
     "A gap makes an open circuit with no current, so A is false; R is true."),
 AR4("In a series connection of bulbs, if one bulb is removed the other bulbs go off.", "In a series connection there is only one path for the current.", "a",
     "Removing a bulb breaks the only path, so no current flows anywhere in the circuit."),
 AR4("An MCB switches off the circuit when the current becomes too large.", "An MCB can be switched on again and reused, unlike a fuse wire.", "b",
     "Both are true, but reusability does not explain why it switches off."),
]

CASE = [
 Q("<b>Case study.</b> Ananya's torch has two cells of 1.5 V each placed one after another, a small bulb and a push switch. One day, even after pressing the switch, the bulb does not glow, though the cells are new. "
   "(i) What is the total voltage of the two cells joined in series? (ii) Name the component that opens or closes the circuit. (iii) Name the thin wire inside the bulb that glows. (iv) Give one possible reason for the bulb not glowing and explain it.",
   "(i) $1.5+1.5=3$ V (1). (ii) The switch (1). (iii) The filament (1). (iv) The filament may be broken (fused) or there may be a loose connection (1); in both cases the circuit is not complete, so no current flows through the filament (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In Mrs Verma's house in Jaipur, many heavy appliances were switched on together on one socket. The wire became hot and, suddenly, the electricity in that room went off. The electrician found that a fuse had blown. "
   "(i) Name the safety device that stopped the current. (ii) What property of fuse wire makes it suitable? (iii) Name the effect of current that made the wire hot. (iv) Why should an ordinary copper wire not be used in place of the fuse wire?",
   "(i) The fuse (1). (ii) It has a low melting point (1). (iii) The heating effect of electric current (1). (iv) Copper has a much higher melting point, so it would not melt when the current is too large (1); the wires would stay overheated and could cause a fire (1).", "1+1+1+2"),
 Q("<b>Case study.</b> For Diwali, Ravi buys a string of 20 small bulbs joined one after another. When one bulb fuses, the entire string goes off. The shopkeeper says that in house wiring the bulbs and fans are connected in parallel. "
   "(i) What type of connection is used in Ravi's string? (ii) Why do all the bulbs go off when one fuses? (iii) What would happen to the other bulbs if they were in parallel and one fused? (iv) Give two reasons why appliances in a house are connected in parallel.",
   "(i) Series connection (1). (ii) There is only one path for the current, and a fused bulb breaks it (1). (iii) The other bulbs would keep glowing (1). (iv) Each appliance can be switched on or off independently (1), and each gets the full voltage of the supply (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Components of a circuit", [
   "Electric cell: converts chemical energy to electrical energy; long cap is positive (+), flat base is negative ($-$).",
   "Battery: two or more cells connected together; cells in series add their voltages (e.g. 1.5 V + 1.5 V = 3 V).",
   "Switch opens or closes the circuit; filament is the thin wire in a bulb that heats and glows.",
   "Electric circuit: a continuous path for current; closed circuit: current flows; open circuit: no current."]),
 ("Conductors and insulators", [
   "Conductors (copper, aluminium, iron, graphite, salt water) allow current to pass.",
   "Insulators (plastic, rubber, wood, glass, dry cloth) do not allow current to pass.",
   "Wires have plastic covering for safety; switch handles are made of insulators."]),
 ("Series and parallel connection", [
   "Series: components joined one after another; one path; if one fails all stop.",
   "Parallel: components joined across the same two points; many paths; others work if one fails.",
   "House wiring uses parallel connection."]),
 ("Heating effect and safety", [
   "Heating effect: a current passing through a wire heats it (electric heater, geyser, iron, toaster).",
   "Fuse: a wire with low melting point in series; melts when current is too large and breaks the circuit.",
   "MCB: automatic switch that trips on overloading or short circuit and can be reset.",
   "Short circuit: current takes a very low-resistance path and becomes very large; overloading: too many appliances on one line."]),
]

MISTAKES = [
 "Connecting a cell with the wrong polarity or leaving a gap in the circuit and still expecting the bulb to glow; it needs a <b>closed</b> circuit.",
 "Saying that a fuse wire has a high melting point; it has a <b>low</b> melting point so that it melts first.",
 "Confusing series and parallel: in series there is <i>one</i> path, in parallel there are <i>many</i> paths.",
 "Thinking all materials with a plastic covering are conductors; the covering is an <b>insulator</b>, the wire inside is the conductor.",
 "Writing that the fuse is connected in parallel with the appliance; it is connected in <b>series</b>.",
 "Mixing up the heating effect (heat from current) with the cause of the glow of a bulb; the filament glows because it becomes very hot.",
]
