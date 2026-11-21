"""Class 6 Science Ch 4 - Exploring Magnets: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch04"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch04", str(REPO / "src/rn_work/c6_sci/ch04.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Which of these is attracted by a magnet?", 1, "(c) an iron nail", "E", opts=["a wooden ruler", "a plastic comb", "an iron nail", "a glass marble"]),
W("The ends of a magnet, where the attraction is strongest, are called its:", 1, "(a) poles", "E", opts=["poles", "filings", "lodestones", "needles"]),
W("A freely suspended bar magnet comes to rest along the:", 1, "(b) north-south direction", "E", opts=["east-west direction", "north-south direction", "up-down direction", "any random direction"]),
W("When the North pole of a magnet is brought near the North pole of another magnet, they:", 1, "(d) repel each other", "E", opts=["attract each other", "do not react", "stick together", "repel each other"]),
W("Which is a non-magnetic material?", 1, "(b) rubber", "E", opts=["nickel", "rubber", "cobalt", "iron"]),
W("The sure test for a magnet is:", 1, "(c) repulsion", "E", opts=["attraction", "shining surface", "repulsion", "heaviness"]),
W("Naturally occurring magnets used by sailors in olden days are called ______.", 1, "lodestones.", "E"),
W("Name the three magnetic metals mentioned in the chapter.", 2, "Iron, nickel and cobalt. (2)", "E"),
W("Name three common shapes of magnets.", 2, "Any three: bar, U-shaped (horseshoe), ring, disc, cylindrical. (Any 2 shapes: 1, three: 2)", "E"),
W("Write True or False: A magnet can have only one pole.", 1, "False. Poles always occur in pairs, North and South. (1)", "E"),
W("Write True or False: A magnet attracts all metals.", 1, "False. It attracts only magnetic materials such as iron, nickel and cobalt. (1)", "E"),
W("Name the instrument that sailors use to find directions at sea.", 1, "Magnetic compass. (1)", "E"),
W("What is the colour usually painted on the north-pointing end of a compass needle?", 1, "Red. (1)", "E"),
W("State the law of attraction and repulsion of magnets.", 2, "Like poles repel; unlike poles attract. (2)", "E"),
W("What do we get if we break a bar magnet into two pieces?", 1, "Two smaller magnets, each with a North and a South pole. (1)", "E"),
W("What did Indian sailors use as a navigation instrument in the old times (a floating fish-shaped iron piece in oil)?", 1, "Matsya-yantra (machchh-yantra). (1)", "E"),
W("Give two examples of non-magnetic materials.", 2, "Any two: wood, plastic, glass, paper, cloth, rubber. (1+1)", "E"),
# ---------------- MEDIUM ----------------
W("Sort into magnetic and non-magnetic: iron key, eraser, steel spoon, plastic scale, nickel coin, glass.", 3, "Magnetic: iron key, steel spoon, nickel coin. Non-magnetic: eraser, plastic scale, glass. (1.5 for each correct group)", "M", wp=True),
W("Why do most iron filings stick near the ends of a bar magnet and not in the middle?", 2, "Attraction is strongest at the poles, which are at the ends. (2)", "M"),
W("Ravi has two identical-looking iron bars. One is a magnet. How can he find out which one, using only a thread?", 3, "Suspend each bar freely by a thread at its middle (1). A magnet comes to rest along the north-south line every time (1) while the plain iron bar rests in any direction (1).", "M", wp=True),
W("Why does the Earth make a freely hanging magnet point north-south?", 2, "The Earth itself behaves like a giant magnet, so a freely suspended magnet lines up with it. (2)", "M"),
W("Describe a magnetic compass in two or three sentences.", 3, "It is a small box with a transparent cover (1) containing a magnetised needle balanced on a pin so it can rotate freely (1) over a dial with directions marked; the north end of the needle is usually red (1).", "M"),
W("Seema wants to know directions in a new place. Explain how she uses a compass.", 3, "Place the compass flat and wait for the needle to settle (1). Turn the box until N and S marks on the dial line up with the needle (1). Now the other directions are as marked on the dial (1).", "M", wp=True),
W("Why is repulsion considered a surer test of a magnet than attraction?", 2, "Iron is also attracted to both poles of a magnet, but only another magnet can repel it. (2)", "M"),
W("A compass needle's N pole moves away when you bring a bar magnet's pole near. Which pole of the bar magnet was it? Give reason.", 2, "The North pole of the bar magnet, because like poles repel. (2)", "M", wp=True),
W("Two toy cars each carry a magnet. When their ends are brought together, one moves away from the other. What can you say about the poles facing each other?", 2, "They are like poles (N-N or S-S), because like poles repel. (2)", "M", wp=True),
W("Does a magnet work through a wooden table? How can you test this using a paper clip?", 3, "Yes, magnetic effect acts through non-magnetic materials (1). Place a paper clip on the table and move a magnet under it (1); the paper clip moves with the magnet (1).", "M", wp=True),
W("Write the steps of making a magnetic compass at home.", 3, "Stroke an iron needle along its length with one pole of a bar magnet in the same direction (1), repeat 30-40 times (1), pass it through a cork and float it in water; it will point north-south (1).", "M"),
W("In a maze toy, steel balls are stuck. How can a magnet help to take them out without touching them?", 2, "Moving a magnet under the cardboard tray makes the steel balls move along; they can be guided out. (2)", "M", wp=True),
W("How should two bar magnets be stored together? Give two rules.", 2, "Place them in pairs with unlike poles on the same side, a wooden piece between them and soft iron pieces across the ends. (2)", "M"),
W("Why should magnets not be kept near mobile phones or remote controls?", 2, "They can disturb or damage these devices. (2)", "M"),
W("Find the mistake: \"A magnet with a broken piece will have a North pole in one piece and a South pole in the other, and the pieces will not be magnets.\"", 2, "Each piece has both N and S poles and is a magnet. Poles always occur in pairs. (2)", "M"),
W("Why do we use a steel paper clip to demonstrate a magnet, instead of an aluminium foil?", 2, "Steel is a magnetic material (contains iron) while aluminium is non-magnetic. (2)", "M"),
W("What happens if a freely suspended iron bar (not a magnet) is rotated and released? Compare it with a magnet.", 2, "The iron bar stays in any direction; a magnet always returns to the north-south line. (2)", "M"),
W("Reshma writes a story about a spice ship in a storm with no stars. How can its sailors find direction?", 2, "They can use a magnetic compass or a freely hanging magnet which always points north-south. (2)", "M", wp=True),
W("Why should magnets be protected from heat, dropping and hammering?", 2, "These make the magnet weak or lose its magnetism. (2)", "M"),
# ---------------- HARD ----------------
W("A mechanic's steel screws keep falling when he tries to place them in a narrow hole. Suggest a way using a magnet and give the reason it works.", 3, "Magnetise the screwdriver by stroking it with a magnet (1). The screws made of steel are attracted and stick to its tip (1) because steel is a magnetic material (1).", "H", wp=True),
W("A steel paper clip has fallen into a bowl of water. Without wetting your hand, how can you take it out?", 3, "Hold a magnet outside the bowl (1) and move it along the side to bring the clip up near the magnet (1) since magnetic force acts through water and the glass or container (1).", "H", wp=True),
W("Two bars A and B attract each other at both ends. Bar A repels a magnet's N pole at one end. What can you say about A and B?", 3, "A is a magnet (it repelled) (1). B attracts at both ends, so B may be plain iron (1) and not a magnet, since only a magnet could repel (1).", "H", wp=True),
W("Magnet X attracts magnet Y at one end but the other end of Y repels X. Explain with the poles.", 3, "Each end of Y has a different pole (1). The end that attracts X's pole is an unlike pole (1) and the other end is a like pole, which repels (1).", "H"),
W("A student breaks a bar magnet into 4 pieces and says, \"Now I have 4 North poles and no South pole.\" Correct this statement.", 3, "Every piece is a complete magnet (1). Each has one North and one South pole (1), so we have 4 North poles and 4 South poles in all (1).", "H", wp=True),
W("Anita keeps a bar magnet near a compass. The needle's red end turns towards the magnet. What does this tell about the pole near the compass? Explain.", 3, "The red (north-seeking) end is attracted, so the pole near it is a South pole (2); unlike poles attract (1).", "H", wp=True),
W("Explain why a ship's compass is placed away from heavy iron objects and magnets.", 3, "A compass needle is a magnet (1). Iron objects and magnets attract or repel it (1) and give wrong readings, so the compass is placed away (1).", "H", wp=True),
W("A child says magnetism does not work when a cardboard is placed between a magnet and a pin. Design a test to check this claim.", 4, "Place a pin on a table and cardboard over it (1). Move a magnet above the cardboard (1). If the pin moves, the claim is wrong (1). Repeat with wood, plastic or glass sheets for more evidence (1).", "H", wp=True),
W("If you cut a long piece of magnet at its middle, would the middle become a pole? Explain using the idea of poles.", 3, "No. Each piece gets its own N and S poles (1) and each cut end becomes a pole of the new magnet (1) because poles always occur in pairs and a magnet cannot have a single pole (1).", "H"),
W("The chapter says Earth behaves like a giant magnet. Give two pieces of evidence from activities.", 3, "A freely hanging magnet always rests along the north-south line (1.5). A compass needle also settles in the north-south direction in any place (1.5).", "H"),
W("Plan an activity to find which of five rods (iron, steel, wooden, plastic, aluminium) are magnetic. State the result you expect.", 4, "Bring each rod near iron filings or pins (1). Rods that attract them are magnetic (1). Expected: iron and steel are attracted (1); wood, plastic and aluminium are not (1).", "H", wp=True),
W("Two magnets are pushed together and they move apart on pencil rollers. What will happen if one is turned around? Explain.", 3, "They will now come together (1). Turning one magnet changes the poles facing each other from like to unlike (1), and unlike poles attract (1).", "H", wp=True),
W("A fridge door magnet holds a paper on a steel door. Which two properties of magnets does this use?", 3, "A magnet attracts steel (magnetic material) (1.5) and acts through paper, a non-magnetic material (1.5).", "H", wp=True),
]

CH = _base()
CH["blocks"] += [
 ("h2", "4.7 Worked Examples and Activity Results"),
 ("steps", [("Example 1 — Which bar is the magnet?", "Two similar iron-looking bars P and Q. **Test 1:** suspend both freely: P settles north-south each time; Q stays in any direction. **Conclusion:** P is a magnet, Q is plain iron. **Test 2:** bring the N pole of a known magnet near each end of P: one end repels. Only a magnet can repel, so P is a magnet."),
  ("Example 2 — Reading a compass", "The needle's red end points to the top of the dial and does not match 'N'. Turn the box until the red end lies on N of the dial. Now E, S, W are in the right places and the direction of a landmark can be read."),
  ("Example 3 — Magnet through materials", "Place a paper clip on a table, cover it with a wooden board and move a magnet below the board. The paper clip moves along. **Conclusion:** magnetic force acts through wood, a non-magnetic material.")]),
 ("h2", "4.8 Magnet Behaviour: Summary Table"),
 ("table", ["Situation", "What happens", "Reason"],
  [["N pole near S pole", "Attract", "Unlike poles attract"],
   ["N near N, or S near S", "Repel", "Like poles repel"],
   ["Iron bar near a magnet (either pole)", "Attracted at both ends", "Iron is magnetic"],
   ["Freely hung magnet", "Rests north-south", "Earth acts as a giant magnet"],
   ["Freely hung plain iron bar", "Rests in any direction", "Not a magnet"],
   ["Wood or plastic between magnet and clip", "Clip still attracted", "Magnetic force acts through non-magnetic materials"],
   ["Magnet broken in two", "Two magnets, each with N and S", "Poles occur in pairs"]]),
 ("h2", "4.9 Common Mistakes"),
 ("ul", ["Attraction alone does **not** prove a magnet (iron is attracted too); **repulsion** does.",
  "Do not say that a magnet attracts all metals; **aluminium, copper and gold** are not attracted.",
  "A magnet cannot be cut into a single North or single South pole.",
  "The north-pointing end of a magnet is called its **North (north-seeking) pole**.",
  "Do not heat, drop or hammer magnets; do not place them near phones.",
  "A magnet is strongest at its **ends** (poles) and weakest in the middle."]),
 ("h2", "4.10 Uses and Safety"),
 ("ul", ["Compasses for travellers, sailors and pilots.",
  "Fridge door seals, pencil box catches, toys, stickers.",
  "Magnetised screwdrivers hold steel screws.",
  "Magnetic picks remove steel pins and needles from a floor or sand.",
  "Keep magnets away from mobile phones, watches and remote controls.",
  "Store magnets in pairs with soft iron keepers and wooden pieces."]),
 ("h2", "4.11 Higher Order Questions"),
 ("qa", [("Can we make a magnet from a piece of iron?", "Yes. Stroke an iron piece many times in one direction with a magnet; it will attract pins and point north-south when suspended."),
  ("Why does a bar magnet of any shape attract more near its ends?", "The poles are at the ends, where the attraction is strongest."),
  ("What is the use of soft iron pieces across magnet ends during storage?", "They keep the magnets from weakening."),
  ("What would a compass needle do near a strong magnet?", "It will turn towards the magnet's poles and not point north.")]),
]
CH["takeaways"] += ["**Repulsion** is the only sure test of a magnet.", "A compass needle is a small magnet; keep it away from other magnets and iron."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
