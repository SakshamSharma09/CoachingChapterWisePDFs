"""Class 8 Science Ch 4 Electricity: Magnetic and Heating Effects - extras."""
from common import AR4, Q

AR = [
 AR4("A compass needle placed near a wire deflects when current flows through the wire.", "An electric current produces a magnetic field around the wire.", "a", "Oersted's observation is explained by the magnetic field of the current."),
 AR4("A soft iron core placed inside a current-carrying coil makes a much stronger electromagnet.", "Soft iron loses its magnetism easily when the current is switched off.", "b", "Both are true, but the loss of magnetism on switching off does not explain why the magnet is stronger."),
 AR4("A fuse wire is made of a material with a high melting point.", "A fuse protects a circuit by melting and breaking it when the current becomes too large.", "d", "A fuse wire has a low melting point, so A is false; R is true."),
 AR4("The filament of an electric bulb glows when current passes through it.", "A bulb filament is strongly cooled by its surroundings so it never gets hot.", "c", "A is true (heating effect); R is false, the filament becomes very hot."),
 AR4("Increasing the number of turns of a coil (with the same current) makes an electromagnet stronger.", "A coil of insulated copper wire is used to make an electromagnet.", "b", "Both are true, but R only describes the material, not why more turns strengthen the magnet."),
 AR4("An electric heater coil is made of nichrome.", "Nichrome is an alloy with high resistance and a high melting point, so it can get red hot without melting.", "a", "These properties make it suitable for heating elements."),
]

CASE = [
 Q("<b>Case study.</b> Dev makes an electromagnet by winding insulated copper wire around an iron nail and connecting the ends to a cell. With 50 turns it lifts 8 small iron pins; with 100 turns on the same nail and with the same cell it lifts 17 pins. When he disconnects the cell, nearly all the pins drop. "
   "(i) Why is the copper wire insulated? (ii) How does the number of turns affect the strength? (iii) What happens to the nail's magnetism when the cell is disconnected? (iv) Give two ways, other than changing the turns, to make this electromagnet stronger.",
   "(i) So that current flows through the turns and not directly between neighbouring turns/nail (1). (ii) More turns give a stronger electromagnet (8 to 17 pins) (1). (iii) It loses its magnetism (soft iron is a temporary magnet) (1). (iv) Use more cells (more current) / use a larger soft iron core (any two sensible) (2).", "1+1+1+2"),
 Q("<b>Case study.</b> In a house wiring, the normal current drawn by all appliances on a circuit is 8 A. The electrician has fuse wires rated 5 A, 10 A and 30 A. During a short circuit the current rises suddenly and the lights go out, though the wiring is undamaged. "
   "(i) What is a fuse? (ii) Which fuse should be used for this circuit? (iii) Which effect of current makes a fuse work? (iv) Why should a 30 A fuse not be used here?",
   "(i) A safety device with a thin low-melting wire that breaks the circuit when current is too high (1). (ii) 10 A (1). (iii) Heating effect of current (1). (iv) A 30 A fuse would not melt at a current well above 8 A, so wires could overheat and cause a fire before the circuit breaks (2). A 5 A fuse would blow in normal use.", "1+1+1+2"),
 Q("<b>Case study.</b> Sana places a compass needle below a straight wire running north to south, with the needle parallel to the wire. When she connects the wire to a battery through a switch, the needle swings. She then reverses the battery connections and the needle swings the other way. "
   "(i) Who first observed this effect? (ii) Name the effect of current shown. (iii) What happens when the switch is kept open? (iv) What conclusion can be drawn from the reversal of the needle's deflection?",
   "(i) Hans Christian Oersted (1). (ii) Magnetic effect of electric current (1). (iii) No current, so no deflection, the needle stays pointing north (1). (iv) The direction of the magnetic field depends on the direction of the current: reversing the current reverses the deflection (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Electric circuit", ["A circuit has a source (cell/battery), conducting wires, a switch and the device (bulb, heater).", "Current flows only in a closed circuit; conventional current goes from + to - outside the cell.",
   "Conductors (metals, graphite) allow current; insulators (plastic, rubber, dry wood) do not.", "Unit of electric current: ampere (A)."]),
 ("Magnetic effect of current", ["Oersted: a current-carrying wire deflects a magnetic compass needle.", "Reversing the current reverses the deflection.",
   "Electromagnet: insulated wire coiled on a soft iron core; it is magnetic only while current flows."]),
 ("Strength of an electromagnet", ["Increases with: more turns, more current (more cells), a soft iron core.", "Uses: lifting scrap iron, electric bell, relays, cranes."]),
 ("Heating effect of current", ["A current-carrying conductor becomes hot; heat increases with current, resistance and time.", "Heating elements (heater, iron, toaster): nichrome, high resistance and high melting point.",
   "Bulb filament: tungsten, very high melting point.", "Fuse: thin low-melting wire; rating just above the normal current; MCB trips and can be reset."]),
]

MISTAKES = [
 "Saying the current direction does not matter for the compass needle; reversing it reverses the deflection.",
 "Using steel or plastic as the core of an electromagnet; soft iron is used for a temporary magnet.",
 "Choosing a fuse of very large rating or writing that a fuse wire has a <i>high</i> melting point.",
 "Forgetting that a circuit must be closed (switch ON) for current, and for the compass to react.",
 "Not insulating the coil wire, or forgetting to say that the magnetism ends when the current stops.",
 "Confusing the heating effect (bulb, heater, fuse) with the magnetic effect (electromagnet, compass).",
]
