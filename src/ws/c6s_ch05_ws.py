"""Class 6 Science Ch 5 - Measurement of Length and Motion: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch05"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch05", str(REPO / "src/rn_work/c6_sci/ch05.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The SI unit of length is the:", 1, "(b) metre", "E", opts=["centimetre", "metre", "kilometre", "inch"]),
W("1 kilometre is equal to:", 1, "(c) 1000 m", "E", opts=["100 m", "10 m", "1000 m", "10000 m"]),
W("While reading a scale, the eye should be:", 1, "(a) directly above the mark being read", "E", opts=["directly above the mark being read", "far to the left of the mark", "at a slant from the right", "closed"]),
W("A swing moves in a ______ motion.", 1, "(d) oscillatory", "E", opts=["linear", "circular", "random", "oscillatory"]),
W("A fixed point used to describe the position of an object is called a:", 1, "(b) reference point", "E", opts=["starting stone", "reference point", "ruler", "unit"]),
W("Which of these is an example of circular motion?", 1, "(c) the rim of a merry-go-round", "E", opts=["a falling apple", "a swing", "the rim of a merry-go-round", "a car on a straight road"]),
W("Fill in the blank: A measurement has two parts, a number and a ______.", 1, "unit.", "E"),
W("Fill in the blank: 1 m = ______ cm.", 1, "100.", "E"),
W("Fill in the blank: 1 cm = ______ mm.", 1, "10.", "E"),
W("Write True or False: A handspan is a standard unit of length.", 1, "False. Handspans differ from person to person, so it is not a standard unit. (1)", "E"),
W("Name the old Indian unit of length based on the width of a finger.", 1, "Angula. (1)", "E"),
W("Write the symbol of kilometre, metre, centimetre and millimetre.", 2, "km, m, cm, mm. (0.5 each)", "E"),
W("Name two instruments that can be used to measure the length of a curved line.", 2, "A flexible measuring tape (tailor's tape), or a thread with a scale. (1+1)", "E"),
W("Name two examples of linear motion.", 2, "Any two: a falling orange, a pushed box, a march-past, a car on a straight road. (1+1)", "E"),
W("What is periodic motion?", 1, "Motion that repeats itself after a fixed interval of time. (1)", "E"),
W("Express 3 km in metres.", 1, "3 x 1000 = 3000 m. (1)", "E"),
W("Which is the smallest division on a common 15 cm scale?", 1, "1 mm (0.1 cm). (1)", "E"),
# ---------------- MEDIUM ----------------
W("Convert: (i) 250 cm into m (ii) 4.5 m into cm (iii) 3 cm into mm.", 3, "(i) 250 / 100 = 2.5 m (1). (ii) 4.5 x 100 = 450 cm (1). (iii) 3 x 10 = 30 mm (1).", "M"),
W("Five friends measure the same table in handspans and get different numbers. Explain why and suggest a solution.", 3, "Their handspans are of different sizes (1), so the number of handspans differs (1). They should use a standard unit such as the metre or centimetre with a scale (1).", "M", wp=True),
W("A tailor needs 2.5 m of cloth for one kurta. How many centimetres is that? How many kurtas can he make from 15 m?", 3, "2.5 m = 250 cm (1). Number of kurtas = 15 / 2.5 (1) = 6 kurtas (1).", "M", wp=True),
W("The zero mark of Imran's scale is worn out. The pencil's one end is at 1.0 cm and the other at 10.4 cm. Find its length.", 2, "Length = 10.4 - 1.0 (1) = 9.4 cm (1).", "M", wp=True),
W("Why is it wrong to read a scale with the eye placed at a slant? Draw a conclusion about the correct position.", 2, "A slanted view makes the reading look higher or lower than the actual mark, giving a wrong value (1). The eye should be directly above the mark (1).", "M"),
W("Radha says that the distance from her house to school is 2 km and 500 m. Write it in km and in m.", 2, "2 km 500 m = 2.5 km (1) = 2500 m (1).", "M", wp=True),
W("Name the correct scale for measuring (i) the length of a pencil (ii) the height of a room (iii) the girth of a tree trunk.", 3, "(i) A 15 cm scale. (ii) A metre scale or measuring tape. (iii) A flexible tape. (1 each)", "M", wp=True),
W("How will you measure the length of a curved path on a map of a village using a thread? Write the steps.", 3, "Lay the thread carefully along the curved path (1). Mark both ends of the thread (1). Straighten the thread and measure it with a scale (1).", "M", wp=True),
W("Padma sees a kilometre stone 'Delhi 70 km' and later 'Delhi 60 km'. Which is the reference point? Is she nearer or farther from Delhi?", 2, "Delhi is the reference point (1). She is nearer to Delhi by 10 km (1).", "M", wp=True),
W("Passengers sit in a moving bus. Are they in motion or at rest? Explain by reference points.", 3, "Passengers are at rest with respect to the bus or a seatmate (1.5). They are in motion with respect to buildings outside the bus (1.5).", "M", wp=True),
W("Classify the motion: (i) a ball falling straight (ii) a swing (iii) the second hand of a clock (iv) a vibrating guitar string.", 3, "(i) Linear (ii) Oscillatory (iii) Circular (iv) Oscillatory. (Any four correct 3, three correct 2, two correct 1)", "M"),
W("Write the correct way to write: 7 kgs, 12 Cm., 50 m., 5 M.", 2, "7 kg, 12 cm, 50 m (no full stop except at end of a sentence), 5 m. Symbols are in lowercase and have no plural 's'. (2)", "M"),
W("Why do the friends in the chapter get different answers when asked which is nearer, the garden or school? How is it solved?", 2, "Each friend measured from their own house (1). With a common point like the bus stand, everyone agrees (1).", "M", wp=True),
W("Define motion and rest.", 2, "An object is in motion if its position changes with respect to a reference point with time (1). If the position does not change, it is at rest (1).", "M"),
W("Give one example each of circular and oscillatory motion.", 2, "Circular: an eraser whirled on a thread. Oscillatory: a swing or hanging eraser (pendulum). (1+1)", "M"),
W("Find the mistake: \"A tailor measured the cloth with the 15 cm scale placed apart from the cloth and slanting.\"", 2, "The scale should touch the cloth along its length (1) and should lie straight, not slanting (1).", "M", wp=True),
W("What is 1 inch in cm? Why do we use common standard units such as the metre instead of handspans?", 2, "1 inch = 2.54 cm (1). A standard unit is the same for everybody, so measurements agree when people trade or travel (1).", "M"),
W("Name two situations where a km is better to use than a cm.", 2, "Distance between cities, length of a railway track. (1+1)", "M"),
W("How do visually challenged students measure length?", 1, "They use scales with raised markings. (1)", "M"),
# ---------------- HARD ----------------
W("A farmer's field is 120 m long and 80 m wide. He wants to put a fence around it. How long should the fence be in metres and in km?", 3, "Perimeter = 2 x (120 + 80) (1) = 400 m (1) = 0.4 km (1).", "H", wp=True),
W("Anish walks 400 m to the bus stand every day. How many metres does he walk in a week (6 school days, to and fro)? Write the answer in km.", 3, "One day = 400 x 2 = 800 m (1). 6 days = 4800 m (1) = 4.8 km (1).", "H", wp=True),
W("Meena measured her notebook as 21.5 cm long. Write it in mm. Another notebook is 0.18 m long. Which is longer and by how much?", 4, "21.5 cm = 215 mm (1). 0.18 m = 18 cm (1). The first is longer (1) by 21.5 - 18 = 3.5 cm (1).", "H", wp=True),
W("A bus goes from Jaipur to Ajmer. The kilometre stones show Ajmer 100 km, then Ajmer 40 km. How far has the bus moved? Why do stones show decreasing numbers?", 3, "Distance covered = 100 - 40 = 60 km (1.5). The reference point is Ajmer and the bus is getting nearer to it, so the numbers decrease (1.5).", "H", wp=True),
W("On a moving ship on calm sea with no windows you cannot say if it is moving. Explain this using the idea of a reference point.", 3, "Motion needs a reference point outside the ship (1). Inside, everything is moving with the ship, so nothing changes position with respect to us (1). So we cannot tell without looking outside (1).", "H"),
W("A rollercoaster ball goes straight down, then round a loop, then straight again. Name the motion on each part.", 3, "Straight parts: linear motion (1). Loop: circular motion (1). The ball passes along the whole track only once and does not keep repeating its path after fixed intervals, so the whole motion is not periodic (1).", "H", wp=True),
W("Why are circular and oscillatory motions both periodic but linear motion of a falling stone is not?", 3, "Circular and oscillatory motions repeat their path after fixed times (1.5). A falling stone moves only once down along a straight path and does not repeat (1.5).", "H"),
W("A cloth seller measures a cloth using her arm length and a customer using his arm length gets a different value. Write two problems this causes in trade and how SI units solve them.", 4, "Arms are different, so the same length gets different values (1). The buyer or seller may feel cheated (1). With the metre scale, everyone gets the same value (1) so trade is fair and clear (1).", "H", wp=True),
W("A student measured a leaf using a scale having a gap between scale edge and the zero mark. His reading is from 0.5 cm to 8.7 cm. Find its length and explain what he should do if the zero mark is not at the end.", 3, "Length = 8.7 - 0.5 (1) = 8.2 cm (1). Start from another clear mark and subtract the first reading from the last reading (1).", "H", wp=True),
W("Write a conversion table from km to mm to show 1 km in each unit, and find how many mm in 2.5 m.", 4, "1 km = 1000 m = 100000 cm = 1000000 mm (3). 2.5 m = 2500 mm (1).", "H"),
W("A boy standing on a bridge looks at a boat moving in the river and a bird sitting on the boat. Describe the motion of the bird with respect to the boy and to the boat.", 3, "With respect to the boy, the bird is in motion because its position changes (1.5). With respect to the boat, the bird is at rest (1.5).", "H", wp=True),
W("Plan an activity to prove that a hanging eraser shows oscillatory motion. State what you will observe and measure.", 3, "Hang the eraser by a thread, pull it to one side and release (1). It moves to and fro about the fixed position (1). Count the number of swings in a given time (e.g. 20 s) to show repetition (1).", "H", wp=True),
W("Why should we write the unit with the number, and why is '25' alone not a complete measurement?", 3, "A measurement has two parts: a number and a unit (1). '25' does not say whether it is 25 cm, 25 m or 25 km (1) and could cause confusion or mistakes (1).", "H"),
]

CH = _base()
def _fix(x, old, new):
    if isinstance(x, str): return x.replace(old, new)
    if isinstance(x, list): return [_fix(i, old, new) for i in x]
    if isinstance(x, tuple): return tuple(_fix(i, old, new) for i in x)
    return x
CH["blocks"] = _fix(CH["blocks"], 'They were body-based and rod-based units used when no common standard existed; angula is still used by carpenters and tailors.', 'They are units (angula is a finger width) mentioned in ancient Indian literature and used in measuring artefacts, architecture and town planning; angula is still used by carpenters and tailors.')
CH["blocks"] += [
 ("h2", "5.9 Worked Examples: Units and Readings"),
 ("steps", [("Example 1 — Changing units", "Convert 3.2 km to m: 1 km = 1000 m, so 3.2 x 1000 = 3200 m. Convert 450 cm to m: divide by 100, 450 / 100 = 4.5 m. Convert 6.5 cm to mm: multiply by 10, 6.5 x 10 = 65 mm."),
  ("Example 2 — Using a broken scale", "The left end of a pencil is at the 1.0 cm mark and the right end at the 10.4 cm mark. Length = 10.4 cm - 1.0 cm = **9.4 cm**."),
  ("Example 3 — Reference point", "A kilometre stone says 'Delhi 70 km' and the next, 10 minutes later, says 'Delhi 60 km'. With Delhi as reference point the position has changed with time, so the bus is in motion and is getting closer to Delhi."),
  ("Example 4 — Measuring a curve", "To measure a curved line on a map, lay a thread exactly along the curve, mark its two ends, straighten the thread and measure it with a scale.")]),
 ("note", "FORMULA", "1 km = 1000 m;  1 m = 100 cm;  1 cm = 10 mm;  so 1 m = 1000 mm and 1 km = 100000 cm.  To go to a smaller unit multiply; to go to a bigger unit divide."),
 ("h2", "5.10 Types of Motion at a Glance"),
 ("table", ["Type", "Path", "Periodic?", "Everyday examples"],
  [["Linear", "Straight line", "No (single pass)", "Falling stone, car on a straight road, marching soldiers"],
   ["Circular", "Circle", "Yes", "Merry-go-round, eraser whirled on a thread, tip of a fan blade"],
   ["Oscillatory", "To and fro about a fixed position", "Yes", "Swing, pendulum, vibrating strip or guitar string"]]),
 ("h2", "5.11 Common Mistakes"),
 ("ul", ["Do **not** use handspans or footsteps as final answers; use standard units.",
  "Do not put the eye at a slant; look from **directly above** the mark.",
  "Write units as **cm**, **km**, not 'Cm', 'kms' or 'cm.'",
  "Always carry a **unit** with every number in the answer.",
  "While converting, check whether to multiply or divide; metres to centimetres means multiply by 100.",
  "An object can be at rest with respect to one thing and in motion with respect to another."]),
 ("h2", "5.12 Measuring Well: Tips"),
 ("ul", ["Use a scale suited to the object; a short scale for a pencil, a tape for a room.",
  "Keep the scale in contact with the object, along its length.",
  "Take the measurement two or three times and compare; small differences come from eye position and scale limits.",
  "Record the number with unit and put a space between them: 9.4 cm.",
  "For round or curved things, use a flexible tape or thread."]),
 ("h2", "5.13 Higher Order Questions"),
 ("qa", [("Why did ancient India use angula and dhanusa?", "They were body-based and rod-based units used when no common standard existed; angula is still used by carpenters and tailors."),
  ("Can an object have a different type of motion in different parts of its path?", "Yes, e.g. a ball on a rollercoaster moves linearly on straight parts and circularly in a loop."),
  ("Why are Harappan scales important?", "Ruled scales excavated from Harappan sites show that ancient people used standard-like measurement."),
  ("Why is a thread better than a ruler for a curved line?", "A thread bends along the curve; a straight ruler cannot.")]),
]
CH["takeaways"] += ["**Convert**: bigger unit to smaller means multiply; smaller to bigger means divide.", "Always state the **reference point** when you say an object is at rest or in motion."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
