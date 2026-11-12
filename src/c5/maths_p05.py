from maths_common import *
import math
from fractions import Fraction as Fr

def cls(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight"
def mixed(f):
    w = f.numerator // f.denominator; r = f - w
    return f"{w} {fr(r.numerator, r.denominator)}" if w and r else (str(w) if w else fr(r.numerator, r.denominator))

# Q1
rows = [(0, 2), (0, 5), (0, 5), (3, 5)]
cells = {(c, r) for r, (s, e) in enumerate(rows) for c in range(s, e)}; assert len(cells) == 14
o, a = mc("14 sq cm", ["12 sq cm", "15 sq cm", "28 sq cm"], 101)
q1 = Q("Each small square is 1 cm × 1 cm. The area of the shaded figure is", 1, a, opts=o, fig=svg_grid(cells))
# Q2
angs = [55, 100, 150]; assert [cls(d) for d in angs] == ["acute", "obtuse", "obtuse"]
fig2 = "".join(svg_angle(d, w=130, h=110) for d in angs)
cb = 3 * 6 - 2 * 2; assert cb == 14
q2 = Q("Angles A, B and C are shown below.", 6, fig=fig2, parts=[
    P("(i)", "(a) Which angle is acute? (b) Which angle is the greatest? (c) How many degrees must be added to angle A to make a right angle?", 3,
      f"(a) <b>A</b> (b) <b>C</b> (c) 90° − 55° = <b>{90-55}°</b>"),
    P("(ii)", "Three cubes of side 1 cm are placed in a row to form a cuboid 3 cm long. (a) How many faces does the cuboid have? (b) How many edges? (c) How many small 1 cm × 1 cm squares are there on its outer surface?", 3,
      f"(a) <b>6</b> (b) <b>12</b> (c) 3 × 6 = 18, minus 4 hidden squares (2 joints × 2) = <b>{cb}</b>")])
# Q3
q3 = Q("", 6, parts=[
    P("(i)", "Name the solid: (a) it has no vertex and no edge, only one curved surface (b) it has 2 flat circular faces and 1 curved surface (c) it has 8 vertices and 6 rectangular faces", 3, "(a) sphere (b) cylinder (c) cuboid"),
    P("(ii)", "Which solid does each object look like? (a) a brick (b) a road roller (c) a laddoo", 3, "(a) cuboid (b) cylinder (c) sphere")])
# Q4
rooms = [("Reading Room", 0, 0, 7, 5), ("Office", 7, 0, 3, 5), ("Store", 0, 5, 3, 3), ("Computers", 3, 5, 4, 3), ("Court", 7, 5, 3, 3)]
opens = [("D", 3, 5, 4, 5, "D1"), ("D", 7, 1.5, 7, 2.5, "D2"), ("D", 1, 5, 2, 5, "D3"), ("D", 5, 8, 6, 8, "D4"),
         ("W", 2, 0, 5, 0, "W1"), ("W", 8, 0, 9, 0, "W2"), ("W", 3.5, 5, 3.5, 5, "")]
opens = opens[:-1]
ar = {r[0]: r[3] * r[4] for r in rooms}; assert ar == {"Reading Room": 35, "Office": 15, "Store": 9, "Computers": 12, "Court": 9}
sc = ar["Store"] + ar["Computers"]; cp = ar["Reading Room"] * 30; same = [k for k in ar if list(ar.values()).count(ar[k]) > 1]
assert (sc, cp, same) == (21, 1050, ["Store", "Court"])
q4 = Q("The plan of a village library is shown. Study it and answer.", 8, fig=svg_plan(rooms, opens, u=26, note="D = door (red), W = window (blue)."), parts=[
    P("(a)", "Find the area of the Reading Room.", 2, f"7 × 5 = <b>{ar['Reading Room']} sq m</b>"),
    P("(b)", "What is the total area of the Store and the Computer room?", 2, f"9 + 12 = <b>{sc} sq m</b>"),
    P("(c)", "Which two rooms have the same area? What is it?", 2, "<b>Store and Court</b>, each 3 × 3 = <b>9 sq m</b>"),
    P("(d)", "A carpet costing ₹ 30 per sq m is laid in the Reading Room. Find the cost.", 2, f"35 × 30 = <b>₹ {cp:,}</b>")])
# Q5-7
v = 800000 + 40000 + 600 + 3; assert v == 840603
o, a = mc("8,40,603", ["8,04,603", "8,40,063", "84,603"], 105)
q5 = Q("800000 + 40000 + 600 + 3 = ", 1, a, opts=o)
assert round(56498, -3) == 56000
o, a = mc("56,000", ["57,000", "56,500", "55,000"], 106)
q6 = Q("56,498 rounded off to the nearest thousand is", 1, a, opts=o)
assert 102345 == int("".join(map(str, [1, 0, 2, 3, 4, 5])))
o, a = mc("1,02,345", ["1,00,000", "1,00,234", "1,23,450"], 107)
q7 = Q("The smallest 6-digit number having all different digits is", 1, a, opts=o)
# Q8
e = Fr(2, 9) + Fr(4, 9); lf = 1 - e; assert (e, lf) == (Fr(2, 3), Fr(1, 3))
pts = {"A": 1, "B": 5, "C": 7}; vals = {k: Fr(v, 3) for k, v in pts.items()}
q8 = Q("", 6, parts=[
    P("(i)", "Sunita ate 2/9 of a cake and her sister Tara ate 4/9 of it. (a) What fraction of the cake did they eat together? (b) What fraction is left?", 3,
      f"(a) 2/9 + 4/9 = 6/9 = <b>{fr(2,3)}</b> (b) 1 − 2/3 = <b>{fr(1,3)}</b>"),
    P("(ii)", "Write the fraction or mixed number shown by A, B and C: A = ____ , B = ____ , C = ____", 3,
      "A = " + mixed(vals["A"]) + ", B = " + mixed(vals["B"]) + ", C = " + mixed(vals["C"]), fig=svg_nl(0, 3, 3, pts))])
# Q9
assert 1000 // 25 == 40
o, a = mc("40", ["4", "25", "400"], 109)
q9 = Q("1000 ÷ 25 = ?", 1, a, opts=o)
# Q10
tot = 650 + 3 * 85 - 100; assert tot == 805
q10 = Q("Raju bought a cricket bat for ₹ 650 and 3 balls at ₹ 85 each. The shopkeeper gave him a discount of ₹ 100 on the whole bill. How much did Raju pay?", 3,
        f"Balls = 3 × 85 = ₹ 255; Bill = 650 + 255 = ₹ 905<br>Pays = 905 − 100 = <b>₹ {tot}</b>")
q_, r_ = divmod(2547, 6); assert (q_, r_) == (424, 3) and 6 * q_ + r_ == 2547
q11 = Q("Divide 2,547 by 6. Write the quotient and the remainder and check your answer.", 3, f"Quotient = <b>{q_}</b>, Remainder = <b>{r_}</b><br>Check: 6 × {q_} + {r_} = {6*q_} + {r_} = {6*q_+r_} ✓")
# Q12
dw = 4 * 320 + 850 + 12 * 45; left = 3000 - dw; assert (4 * 320, 12 * 45, dw, left) == (1280, 540, 2670, 330)
est = round(7486, -3) + round(5318, -3); ex = 7486 + 5318; assert (est, ex) == (12000, 12804)
q12 = Q("", 6, parts=[
    P("(i)", "For Diwali, a family bought 4 kg sweets at ₹ 320 per kg, crackers worth ₹ 850 and 12 packets of diyas at ₹ 45 per packet. They had ₹ 3,000. How much money was left?", 3,
      f"Sweets = ₹ 1,280; Diyas = 12 × 45 = ₹ 540; Total = 1,280 + 850 + 540 = ₹ {dw:,}<br>Left = 3,000 − {dw:,} = <b>₹ {left}</b>"),
    P("(ii)", "(a) Estimate 7,486 + 5,318 by rounding each to the nearest thousand. (b) Find the exact sum.", 3, f"(a) 7,000 + 5,000 = <b>{est:,}</b> (b) <b>{ex:,}</b>")])
# Q13
A = {i for i in range(1, 29) if i % 7 == 0}; B = {i for i in range(1, 29) if i % 4 == 0}; bo = sorted(A & B)
assert (len(A), len(B), bo) == (4, 7, [28])
fig13 = "<b>Switch A</b>" + svg_bulbs(28, A, per_row=14, col="#c3a6f0") + "<b>Switch B</b>" + svg_bulbs(28, B, per_row=14, col="#f0d36f")
f28 = [d for d in range(1, 29) if 28 % d == 0]; f42 = [d for d in range(1, 43) if 42 % d == 0]; cf = [d for d in f28 if d in f42]; assert (cf, max(cf)) == ([1, 2, 7, 14], 14)
q13 = Q("", 6, parts=[
    P("(i)", "Bulbs 1 to 28 are connected to switches A and B. Glowing bulbs are coloured. (a) How many bulbs glow with Switch A? (b) How many with Switch B? (c) Which bulb glows with both switches?", 3,
      f"(a) <b>{len(A)}</b> (b) <b>{len(B)}</b> (c) <b>28</b> (LCM of 7 and 4)", fig=fig13),
    P("(ii)", "(a) Write all factors of 28. (b) Write the common factors of 28 and 42. (c) Write the HCF of 28 and 42.", 3,
      f"(a) {', '.join(map(str,f28))} (b) {', '.join(map(str,cf))} (c) <b>{max(cf)}</b>")])
# Q14
base = [3, 5, 2, 6]; lv = [base]
while len(lv[-1]) > 1: lv.append([lv[-1][i] + lv[-1][i + 1] for i in range(len(lv[-1]) - 1)])
assert lv == [[3, 5, 2, 6], [8, 7, 8], [15, 15], [30]]
pyr = "<table class='t5'>" + "".join("<tr><td colspan='1' style='border:none'></td>" if False else "<tr>" + f"<td style='border:none;width:{(4-len(r))*14}px'></td>" + "".join(f"<td style='width:30px'>{x}</td>" for x in r) + "</tr>" for r in reversed(lv)) + "</table>"
pyr = "<table class='t5' style='font-size:1.1em'>" + "".join("<tr><td style='border:none'></td>" * 0 + "".join(f"<td colspan='2' style='min-width:34px'>{x}</td>" for x in r).join([f"<td colspan='{4-len(r)}' style='border:none'></td>", f"<td colspan='{4-len(r)}' style='border:none'></td>"]) + "</tr>" for r in reversed(lv)) + "</table>"
pyr = "<table class='t5' style='font-size:1.1em'>" + "".join(
    "<tr>" + f"<td colspan='{4-len(r)}' style='border:none'></td>" + "".join(f"<td colspan='2' style='min-width:34px'>{x}</td>" for x in r) + f"<td colspan='{4-len(r)}' style='border:none'></td></tr>" for r in reversed(lv)) + "</table>"
sb = sum(base); assert (sb, lv[-1][0] - sb) == (16, 14)
til = 10 * 3; per = 2 * (10 + 3); cost = til * 25; assert (til, per, cost) == (30, 26, 750)
q14 = Q("", 6, parts=[
    P("(i)", "In this number pyramid every number is the sum of the two numbers just below it. (a) Which two numbers add up to 15 in the 2nd row from the top? (b) Which number is at the top? (c) Find the sum of the four numbers in the bottom row. By how much is the top number greater than this sum?", 3,
      f"(a) <b>8 and 7</b> (b) <b>{lv[-1][0]}</b> (c) 3 + 5 + 2 + 6 = <b>{sb}</b>; 30 − 16 = <b>{lv[-1][0]-sb}</b>", fig=pyr),
    P("(ii)", "A verandah floor is covered with square tiles of side 1 m as shown. (a) How many tiles are used? (b) Find the perimeter of the floor. (c) One tile costs ₹ 25. Find the cost of all tiles.", 3,
      f"(a) 10 × 3 = <b>{til}</b> (b) 2 × (10 + 3) = <b>{per} m</b> (c) {til} × 25 = <b>₹ {cost}</b>", fig=tiles_svg(10, 3, 18, "10 tiles", "3 tiles"))])
# Q15-17
assert (8 * 1000 + 50, 3.5 * 1000, 2 * 24) == (8050, 3500, 48)
q15 = Q("Fill in the blanks: (a) 8 km 50 m = ______ m (b) 3.5 kg = ______ g (c) 2 days = ______ hours", 3, "(a) 8050 (b) 3500 (c) 48")
q16 = Q("Write True or False: (a) 22:30 hours is 10:30 p.m. (b) A 500 g packet is heavier than a 1 kg packet. (c) ₹ 7.25 means 7 rupees and 25 paise.", 3, "(a) True (b) False (500 g is half a kg) (c) True")
dep = 6 * 60 + 50; arr = 11 * 60 + 15; dur = arr - dep; late = arr + 95; assert dur == 265 and divmod(late, 60) == (12, 50)
q17 = Q("A train leaves Jaipur at 6:50 a.m. and is to reach Delhi at 11:15 a.m. (a) How long is the scheduled journey? (b) One day the train ran 1 hour 35 minutes late. At what time did it reach Delhi?", 3,
        "(a) 6:50 a.m. to 11:15 a.m. = <b>4 h 25 min</b> (b) 11:15 + 1 h 35 min = <b>12:50 p.m.</b>")
# Q18
nodes = {"Jaipur": (45, 140), "Sikar": (125, 85), "Jhunjhunu": (250, 40), "Churu": (260, 130), "Alwar": (130, 20)}
edges = [("Jaipur", "Sikar", 114), ("Sikar", "Jhunjhunu", 55), ("Sikar", "Churu", 70), ("Jhunjhunu", "Churu", 80), ("Jaipur", "Alwar", 150)]
w1 = 114 + 55; w3 = 2 * (114 + 70); w4 = 55 + 80 - 70
assert (w1, w3, w4) == (169, 368, 65)
q18 = Q("The map shows some roads of northern Rajasthan with distances (not to scale).", 8, fig=svg_route(nodes, edges), parts=[
    P("(a)", "How far is Jhunjhunu from Jaipur if one goes through Sikar?", 2, f"114 + 55 = <b>{w1} km</b>"),
    P("(b)", "Which city is nearest to Sikar? How far is it?", 2, "<b>Jhunjhunu</b>, 55 km (Churu is 70 km, Jaipur 114 km)"),
    P("(c)", "A bus goes from Jaipur to Churu through Sikar and comes back the same way. How far does it run in all?", 2, f"(114 + 70) × 2 = <b>{w3} km</b>"),
    P("(d)", "How much longer is the route Sikar → Jhunjhunu → Churu than the direct road Sikar → Churu?", 2, f"55 + 80 = 135 km; 135 − 70 = <b>{w4} km</b>")])
# Q19-20
tri = [n * (n + 1) // 2 for n in range(1, 8)]; assert 6 in tri and not any(x in tri for x in (8, 9, 12))
o, a = mc("6", ["8", "9", "12"], 121)
q19 = Q("Which of these is a triangular number (1, 3, 6, 10, 15, …)?", 1, a, opts=o)
st = 3 * 10 + 1; assert st == 31
o, a = mc("31", ["30", "33", "40"], 122)
q20 = Q("Squares are made with matchsticks (Fig. 1 needs 4 sticks, Fig. 2 needs 7, Fig. 3 needs 10). How many sticks are needed to make 10 squares in a row?", 1, a, opts=o, fig=svg_rowsq([1, 2, 3]))
# Q21 tally with blanks
def tally(n): return ("<s>||||</s> " * (n // 5) + "|" * (n % 5)).strip()
sp = {"Cricket": 14, "Kabaddi": 9, "Football": 6, "Kho-kho": 11}; T = sum(sp.values()); assert T == 40
fig21 = tab([[k, tally(v)] for k, v in sp.items()], ["Game", "Tally marks"])
q21 = Q("Students of Class 5 voted for their favourite game. The tally table is shown (a group of five is ||||).", 3, fig=fig21, parts=[
    P("(a)", "Write the number of votes for Cricket, Kabaddi, Football and Kho-kho.", 1, "Cricket 14, Kabaddi 9, Football 6, Kho-kho 11"),
    P("(b)", "Which game got the fewest votes? Which got the most?", 1, "Fewest: <b>Football</b> (6); most: <b>Cricket</b> (14)"),
    P("(c)", "How many students voted in all?", 1, f"14 + 9 + 6 + 11 = <b>{T}</b>")])
# Q22
s = [1];
for k in range(1, 9): s.append(s[-1] + k)
assert s[:6] == [1, 2, 4, 7, 11, 16] and s[6:8] == [22, 29] and s[8] == 37
q22 = Q("Look at the pattern: 1, 2, 4, 7, 11, 16, ___, ___, … (a) What is added each time? (b) Write the next two numbers. (c) Find the 9th number.", 3,
        "(a) The number added goes up by 1 each time: +1, +2, +3, +4, +5, … (b) <b>22, 29</b> (c) 29 + 8 = <b>37</b>")
secs = [sec("UNDERSTANDING SHAPE AND SPACE", 21, [q1, q2, q3, q4]),
        sec("NUMBER SYSTEM", 9, [q5, q6, q7, q8]),
        sec("OPERATIONS", 25, [q9, q10, q11, q12, q13, q14]),
        sec("MEASUREMENT", 17, [q15, q16, q17, q18]),
        sec("DATA HANDLING AND PATTERNS", 8, [q19, q20, q21, q22])]
if __name__ == "__main__":
    run(meta(5), secs)
