from maths_common import *
import math
from fractions import Fraction as Fr

def cls(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight"

# Q1 : T shaped figure
rows = [(0, 6), (1, 5), (2, 4)]
cells = {(c, r) for r, (s, e) in enumerate(rows) for c in range(s, e)}
cells = {(c, r) for (c, r) in cells}
area = len(cells); assert area == 12
# grid helper needs min col 0 : shift not needed (svg_grid uses absolute col)
o, a = mc("12 sq cm", ["10 sq cm", "14 sq cm", "9 sq cm"], 71)
q1 = Q("Each small square is 1 cm × 1 cm. Count the squares and find the area of the shaded figure.", 1, a, opts=o, fig=svg_grid(cells))
# Q2
angs = [70, 110]; assert sum(angs) == 180
fig2 = "".join(svg_angle(d, w=150, h=110) for d in angs)
dirs = ["North", "East", "South", "West"]
def turn(start, quarters_cw): return dirs[(dirs.index(start) + quarters_cw) % 4]
t1 = turn("North", 1); t2 = turn("East", 2); t3 = turn("North", -3)
assert (t1, t2, t3) == ("East", "West", "East")
q2 = Q("Two angles P and Q are shown below.", 6, fig=fig2, parts=[
    P("(i)", "(a) Name the type of angle P. (b) Name the type of angle Q. (c) What is the sum of the two angles? What kind of angle do they make together?", 3,
      f"(a) <b>acute</b> (b) <b>obtuse</b> (c) 70° + 110° = <b>180°</b>, a <b>straight angle</b>"),
    P("(ii)", "Neha faces North. In which direction will she face after (a) a clockwise turn of one right angle? (b) a clockwise turn of two right angles from East? (c) an anticlockwise turn of three right angles from North?", 3,
      f"(a) <b>{t1}</b> (b) <b>{t2}</b> (c) <b>{t3}</b>")])
# Q3
q3 = Q("", 6, parts=[
    P("(i)", "Fill in: (a) A cube has ____ faces. (b) A cone has ____ vertex. (c) A triangular pyramid has ____ faces.", 3, "(a) 6 (b) 1 (c) 4"),
    P("(ii)", "Which solid can be made from each net? (a) 2 triangles and 3 rectangles (b) 4 triangles (c) 6 rectangles", 3, "(a) triangular prism (b) triangular pyramid (tetrahedron) (c) cuboid")])
# Q4
rooms = [("Shop", 0, 0, 8, 5), ("Godown", 8, 0, 4, 5), ("Office", 0, 5, 4, 3), ("Wash", 4, 5, 2, 3), ("Parking", 6, 5, 6, 3)]
opens = [("D", 3, 0, 5, 0, "D1"), ("D", 8, 2, 8, 3, "D2"), ("D", 1, 5, 2, 5, "D3"), ("D", 4, 6, 4, 7, "D4"), ("D", 12, 6, 12, 7.5, "D5"),
         ("W", 10, 0, 11, 0, "W1"), ("W", 0, 6, 0, 7, "W2")]
ar = {r[0]: r[3] * r[4] for r in rooms}; assert sum(ar.values()) == 96 and ar["Shop"] == 40 and ar["Godown"] == 20 and ar["Parking"] == 18
fl = ar["Godown"] * 120; pr = 2 * (12 + 8); assert (fl, pr) == (2400, 40)
q4 = Q("The ground-floor plan of a shop in Pushkar is shown. Answer the questions.", 8, fig=svg_plan(rooms, opens, u=26, note="D = door (red), W = window (blue)."), parts=[
    P("(a)", "Find the area of the Shop.", 2, f"8 × 5 = <b>{ar['Shop']} sq m</b>"),
    P("(b)", "How many sq m more is the Shop than the Godown?", 2, f"{ar['Shop']} − {ar['Godown']} = <b>{ar['Shop']-ar['Godown']} sq m</b>"),
    P("(c)", "The Godown floor is to be laid at ₹ 120 per sq m. Find the cost.", 2, f"20 × 120 = <b>₹ {fl:,}</b>"),
    P("(d)", "Find the perimeter of the whole building (12 m by 8 m).", 2, f"2 × (12 + 8) = <b>{pr} m</b>")])
# Q5-7
assert indian(407050) == "4,07,050"
o, a = mc("Four lakh seven thousand fifty", ["Four lakh seventy thousand fifty", "Forty lakh seven thousand fifty", "Four lakh seven thousand five hundred"], 75)
q5 = Q("4,07,050 is read as", 1, a, opts=o)
assert str(738215)[1] == "3"
o, a = mc("3", ["7", "8", "1"], 76)
q6 = Q("In 7,38,215 the digit in the ten-thousands place is", 1, a, opts=o)
cand = [348920, 384092, 348290, 384029]; assert max(cand) == 384092
o, a = mc("3,84,092", ["3,48,920", "3,48,290", "3,84,029"], 77)
q7 = Q("The greatest number among 3,48,920; 3,84,092; 3,48,290 and 3,84,029 is", 1, a, opts=o)
# Q8
dec = Fr(3, 5) * 250; und = 250 - dec; assert (dec, und) == (150, 100)
pts = {"A": 3, "B": 5, "C": 9}
q8 = Q("", 6, parts=[
    P("(i)", "At the Pushkar fair, 3/5 of the 250 camels were decorated. (a) How many camels were decorated? (b) How many were not decorated?", 3,
      f"(a) 250 ÷ 5 × 3 = 50 × 3 = <b>{int(dec)}</b> (b) 250 − 150 = <b>{int(und)}</b>"),
    P("(ii)", "Write the decimal shown by each letter: A = ____ , B = ____ , C = ____", 3, "A = 0.3 (3/10), B = 0.5 (1/2), C = 0.9 (9/10)", fig=svg_nl(0, 1, 10, pts))])
# Q9
assert 305 * 12 == 3660
o, a = mc("3660", ["3060", "3560", "3650"], 79)
q9 = Q("305 × 12 = ?", 1, a, opts=o)
# Q10
qb, rb = divmod(500, 8); assert (qb, rb) == (62, 4)
q10 = Q("A tank holds 500 litres. It is filled with a bucket of 8 litres. How many full buckets are needed to fill it as much as possible and how many litres are still needed to fill it completely?", 3,
        f"500 ÷ 8 = {qb} remainder {rb}<br><b>{qb} full buckets</b> give {qb*8} L, so <b>{rb} L</b> more are needed.")
q_, r_ = divmod(6274, 7); assert (q_, r_) == (896, 2) and 7 * q_ + r_ == 6274
q11 = Q("Divide 6,274 by 7 and verify your answer.", 3, f"Quotient = <b>{q_}</b>, Remainder = <b>{r_}</b><br>Verify: 7 × {q_} + {r_} = {7*q_} + {r_} = {7*q_+r_} ✓")
# Q12
sal = 32500; ex = [1850, 9650, 4200, 3300]; lf = sal - sum(ex); assert (sum(ex), lf) == (19000, 13500)
e = 490 * 30; xx = 487 * 31; assert (e, xx) == (14700, 15097)
q12 = Q("", 6, parts=[
    P("(i)", "Mr. Meena earns ₹ 32,500 a month. He spends ₹ 1,850 on electricity, ₹ 9,650 on groceries, ₹ 4,200 on school fees and ₹ 3,300 on other things. How much does he save?", 3,
      f"Spent = 1,850 + 9,650 + 4,200 + 3,300 = ₹ {sum(ex):,}<br>Saved = 32,500 − {sum(ex):,} = <b>₹ {lf:,}</b>"),
    P("(ii)", "(a) Estimate 487 × 31 by rounding to the nearest ten. (b) Find the exact product.", 3, f"(a) 490 × 30 = <b>{e:,}</b> (b) 487 × 31 = <b>{xx:,}</b>")])
# Q13
A = {i for i in range(1, 37) if i % 6 == 0}; B = {i for i in range(1, 37) if i % 9 == 0}; bo = sorted(A & B)
assert (len(A), len(B), bo, math.lcm(6, 9)) == (6, 4, [18, 36], 18)
fig13 = "<b>Switch A</b>" + svg_bulbs(36, A, per_row=12, col="#a6e3a1") + "<b>Switch B</b>" + svg_bulbs(36, B, per_row=12, col="#f9c784")
g = math.gcd(24, 36); assert (g, 24 // g, 36 // g) == (12, 2, 3)
q13 = Q("", 6, parts=[
    P("(i)", "Bulbs 1 to 36 are connected to two switches. Glowing bulbs are coloured. (a) How many bulbs glow with Switch A? (b) How many glow with Switch B? (c) Which bulbs glow with both?", 3,
      f"(a) <b>{len(A)}</b> (b) <b>{len(B)}</b> (c) <b>18 and 36</b>", fig=fig13),
    P("(ii)", "24 laddoos and 36 barfis are to be put on plates so that every plate has the same number of laddoos and the same number of barfis, with none left. (a) What is the greatest number of plates? (b) How many laddoos and how many barfis are on each plate?", 3,
      f"(a) HCF of 24 and 36 = <b>{g} plates</b> (b) <b>{24//g} laddoos</b> and <b>{36//g} barfis</b>")])
# Q14
M = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
assert all(sum(r) == 15 for r in M) and all(sum(M[r][c] for r in range(3)) == 15 for c in range(3)) and sum(M[i][i] for i in range(3)) == 15
mag = "<table class='t5' style='font-size:1.2em'>" + "".join("<tr>" + "".join(f"<td style='width:28px'>{x}</td>" for x in r) + "</tr>" for r in M) + "</table>"
fl2 = 24 * 4; w_, l_ = 6 * 2, 4 * 2; assert (w_ * l_, 2 * (w_ + l_)) == (96, 40)
q14 = Q("", 6, parts=[
    P("(i)", "A 'magic square' is shown. (a) Find the sum of the numbers in the first row. (b) Find the sum of the numbers in the second column. (c) Find the sum of the numbers on the diagonal 8, 5, 2. What do you notice?", 3,
      "(a) 8 + 1 + 6 = <b>15</b> (b) 1 + 5 + 9 = <b>15</b> (c) 8 + 5 + 2 = <b>15</b>. Every row, column and diagonal has the same sum, 15.", fig=mag),
    P("(ii)", "A floor is covered by 6 tiles in a row and 4 such rows (figure). Each tile is a square of side 2 m. (a) How many tiles are used? (b) What are the length and breadth of the floor? (c) Find the area of the floor.", 3,
      f"(a) 6 × 4 = <b>24</b> (b) <b>{w_} m</b> by <b>{l_} m</b> (c) {w_} × {l_} = <b>{w_*l_} sq m</b>", fig=tiles_svg(6, 4, 20, "6 tiles", "4 tiles"))])
# Q15-17
assert (5 * 100 + 8, 6 * 1000 + 40, 3 * 60 + 30) == (508, 6040, 210)
q15 = Q("Fill in the blanks: (a) 5 m 8 cm = ______ cm (b) 6 kg 40 g = ______ g (c) 3 h 30 min = ______ min", 3, "(a) 508 (b) 6040 (c) 210")
q16 = Q("Write True or False: (a) 10 mL is more than 1 L. (b) Water boils at 100 °C. (c) A quarter of ₹ 100 is ₹ 25.", 3, "(a) False (1 L = 1000 mL) (b) True (c) True")
ppk = 1100 // 25; assert ppk * 25 == 1100 and ppk * 7 == 308
q17 = Q("A 25 kg bag of rice costs ₹ 1,100. (a) What is the cost of 1 kg of rice? (b) What is the cost of 7 kg of rice?", 3, f"(a) 1100 ÷ 25 = <b>₹ {ppk}</b> (b) 44 × 7 = <b>₹ {ppk*7}</b>")
# Q18
nodes = {"Ajmer": (150, 85), "Pushkar": (60, 35), "Kishangarh": (270, 40), "Beawar": (80, 150), "Nasirabad": (270, 140)}
edges = [("Ajmer", "Pushkar", 15), ("Ajmer", "Kishangarh", 27), ("Ajmer", "Beawar", 55), ("Ajmer", "Nasirabad", 22), ("Pushkar", "Beawar", 60)]
v1 = 22 + 15; v2 = 55 - 15; v3 = 15 + 55 - 60; v4 = 27 + 27 + 22
assert (v1, v2, v3, v4) == (37, 40, 10, 76)
q18 = Q("The map shows the roads around Ajmer in Rajasthan with distances (not to scale).", 8, fig=svg_route(nodes, edges), parts=[
    P("(a)", "How far is Nasirabad from Pushkar if one goes through Ajmer?", 2, f"22 + 15 = <b>{v1} km</b>"),
    P("(b)", "How much farther from Ajmer is Beawar than Pushkar?", 2, f"55 − 15 = <b>{v2} km</b>"),
    P("(c)", "How many km are saved by going directly from Pushkar to Beawar instead of through Ajmer?", 2, f"15 + 55 = 70 km; 70 − 60 = <b>{v3} km</b>"),
    P("(d)", "A cyclist rides Ajmer → Kishangarh → Ajmer → Nasirabad. How far does he ride?", 2, f"27 + 27 + 22 = <b>{v4} km</b>")])
# Q19-20
mm = [x for x in (25, 35, 40, 45) if x % 3 == 0 and x % 5 == 0]; assert mm == [45]
o, a = mc("45", ["25", "35", "40"], 91)
q19 = Q("Which of these numbers is a multiple of both 3 and 5?", 1, a, opts=o)
s7 = 7 * 8 // 2; assert s7 == 28
o, a = mc("28", ["21", "35", "14"], 92)
q20 = Q("Staircases are made of squares as shown (Fig. 1 has 1 square, Fig. 2 has 3, Fig. 3 has 6). How many squares will Fig. 7 have?", 1, a, opts=o, fig=svg_stairs([1, 2, 3]))
# Q21 pictograph
items = {"Lassi": 6, "Kulfi": 8, "Kachori": 5, "Jalebi": 9}; unit = 10
fig21 = tab([[k, "🥤" * v] for k, v in items.items()], ["Item", f"Sold (each symbol = {unit} plates / glasses)"])
lo = min(items, key=items.get); tt = sum(items.values()) * unit; dd = (items["Kulfi"] - items["Lassi"]) * unit
assert (lo, tt, dd) == ("Kachori", 280, 20)
q21 = Q("The pictograph shows how many items a stall sold at a fair.", 3, fig=fig21, parts=[
    P("(a)", "Which item sold the least? How many were sold?", 1, "<b>Kachori</b>, 5 × 10 = 50"),
    P("(b)", "Find the total number of items sold.", 1, f"(6 + 8 + 5 + 9) × 10 = <b>{tt}</b>"),
    P("(c)", "How many more Kulfi than Lassi were sold?", 1, f"(8 − 6) × 10 = <b>{dd}</b>")])
v = [int("1" * k) for k in (5, 6, 7)]
assert 1234 * 9 + 5 == 11111 and 12345 * 9 + 6 == 111111 and 123456 * 9 + 7 == 1111111
q22 = Q("Look at the pattern: 1 × 9 + 2 = 11; 12 × 9 + 3 = 111; 123 × 9 + 4 = 1111. Using the pattern, write the answers: (a) 1234 × 9 + 5 (b) 12345 × 9 + 6 (c) 123456 × 9 + 7", 3,
        f"Each answer is a number of all 1s. (a) <b>11111</b> (b) <b>111111</b> (c) <b>1111111</b>")
secs = [sec("UNDERSTANDING SHAPE AND SPACE", 21, [q1, q2, q3, q4]),
        sec("NUMBER SYSTEM", 9, [q5, q6, q7, q8]),
        sec("OPERATIONS", 25, [q9, q10, q11, q12, q13, q14]),
        sec("MEASUREMENT", 17, [q15, q16, q17, q18]),
        sec("DATA HANDLING AND PATTERNS", 8, [q19, q20, q21, q22])]
if __name__ == "__main__":
    run(meta(4), secs)
