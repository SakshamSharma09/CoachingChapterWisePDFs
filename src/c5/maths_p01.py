from maths_common import *
import math

def cls(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight" if d == 180 else "reflex"

# Q1 area by counting squares
cells = {(c, r) for r, L in enumerate([5, 3, 3]) for c in range(L)}
area1 = len(cells); assert area1 == 11
o1, a1 = mc("11 sq cm", ["8 sq cm", "13 sq cm", "22 sq cm"], 1)
q1 = Q("Each small square of the grid is 1 cm × 1 cm. The area of the shaded figure is", 1, a1, opts=o1, fig=svg_grid(cells))

# Q2 angles
angs = [35, 90, 125]
fig2 = "".join(svg_angle(d, w=130, h=110, label=True) for d in angs)
lab = ["A", "B", "C"]
p2a = [P(f"({'abc'[i]})", f"Angle {lab[i]} = {d}°. It is a(n) ______ angle.", 1, f"<b>{cls(d)}</b>") for i, d in enumerate(angs)]
assert [cls(d) for d in angs] == ["acute", "right", "obtuse"]
hrs = [4, 9, 6]; ang = [30 * h for h in hrs]; assert ang == [120, 270, 180]
ang2 = [min(a, 360 - a) for a in ang]; assert ang2 == [120, 90, 180]
p2b = [P(f"({'abc'[i]})", f"The angle between the two hands of a clock at {h} o'clock is (smaller angle) ______ ° and it is a ______ angle.", 1, f"<b>{a}°, {cls(a)}</b>") for i, (h, a) in enumerate(zip(hrs, ang2))]
q2 = Q("Angles A, B and C are shown below (figures are drawn with the measure written on them).", 6,
       fig=fig2, parts=[P("(i)", "Name the type of each angle.", 3, "A: acute; B: right; C: obtuse", fig=None), P("(ii)", "Complete using a clock face.", 3, "")])
q2["parts"][0]["q"] = "Name the type of each angle: (a) A ______ (b) B ______ (c) C ______"
q2["parts"][0]["ans"] = "(a) acute (b) right (c) obtuse"
q2["parts"][1]["q"] = " ".join(f"({'abc'[i]}) At {h} o'clock the smaller angle between the hands is ______° and it is a(n) ______ angle." for i, h in enumerate(hrs))
q2["parts"][1]["ans"] = "; ".join(f"({'abc'[i]}) {a}°, {cls(a)}" for i, a in enumerate(ang2))

# Q3 solids
solid = {"cube": (6, 12, 8), "square pyramid": (5, 8, 5), "triangular prism": (5, 9, 6)}
for k, (f, e, v) in solid.items(): assert f + v - e == 2
q3 = Q("", 6, parts=[
    P("(i)", "Write the number asked: (a) Edges of a cube = ____ (b) Vertices of a square pyramid = ____ (c) Faces of a triangular prism = ____", 3,
      f"(a) {solid['cube'][1]} (b) {solid['square pyramid'][2]} (c) {solid['triangular prism'][0]}"),
    P("(ii)", "Name the solid shape that each object looks like: (a) a dice (b) an ice-cream cone (c) a water pipe (a long hollow tube)", 3, "(a) cube (b) cone (c) cylinder")])

# Q4 plan
rooms = [("Hall", 0, 0, 6, 4), ("Bedroom", 6, 0, 4, 4), ("Kitchen", 0, 4, 4, 3), ("Bath", 4, 4, 2, 3), ("Store", 6, 4, 4, 3)]
opens = [("D", 0, 1, 0, 2, "D1"), ("D", 6, 2.5, 6, 3.5, "D2"), ("D", 1, 4, 2, 4, "D3"), ("D", 4, 5, 4, 6, "D4"), ("D", 8, 4, 9, 4, "D5"),
         ("W", 2, 0, 4, 0, "W1"), ("W", 7, 0, 9, 0, "W2"), ("W", 1, 7, 3, 7, "W3")]
doors = sum(1 for o in opens if o[0] == "D"); wins = sum(1 for o in opens if o[0] == "W")
hall = 6 * 4; small = min(rooms, key=lambda r: r[3] * r[4]); per = 2 * (10 + 7)
assert (doors, wins, hall, small[0], small[3] * small[4], per) == (5, 3, 24, "Bath", 6, 34)
fig4 = svg_plan(rooms, opens, u=26, note="D = door (red), W = window (blue). All rooms are rectangles.")
q4 = Q("The plan of Mr. Sharma's house in Sikar is shown below. Study it and answer.", 8, fig=fig4, parts=[
    P("(a)", "Find the area of the Hall.", 2, f"6 × 4 = <b>{hall} sq m</b>"),
    P("(b)", "How many doors and how many windows does the house have?", 2, f"<b>{doors} doors, {wins} windows</b>"),
    P("(c)", "Which is the smallest room? Write its area.", 2, f"<b>Bath</b>, 2 × 3 = <b>{small[3]*small[4]} sq m</b>"),
    P("(d)", "Find the perimeter of the whole house (10 m by 7 m).", 2, f"2 × (10 + 7) = <b>{per} m</b>")])

# Q5-Q7
n5 = 47386; assert (n5 // 1000) % 10 == 7
o, a = mc("7000", ["700", "70", "70000"], 5)
q5 = Q("The place value of the digit 7 in 47,386 is", 1, a, opts=o)
digs = [3, 0, 8, 5, 2]; big = int("".join(map(str, sorted(digs, reverse=True)))); assert big == 85320
o, a = mc("85,320", ["80,325", "85,302", "23,058"], 6)
q6 = Q("The greatest 5-digit number that can be made using the digits 3, 0, 8, 5, 2 (each used once) is", 1, a, opts=o)
assert 60000 + 3000 + 40 + 7 == 63047
o, a = mc("63,047", ["60,347", "63,407", "6,347"], 7)
q7 = Q("The number 60000 + 3000 + 40 + 7 is written as", 1, a, opts=o)

# Q8
l1, l2, rate = 2.75, 1.60, 80; tot = round(l1 + l2, 2); cost = round(tot * rate, 2); assert (tot, cost) == (4.35, 348.0)
pts = {"A": 3, "B": 7, "C": 15}; vals = {k: 2 + v / 10 for k, v in pts.items()}; assert vals == {"A": 2.3, "B": 2.7, "C": 3.5}
q8 = Q("", 6, parts=[
    P("(i)", "Kamla bought 2.75 m of cloth for a kurta and 1.60 m for a dupatta. If cloth costs ₹ 80 per metre, find the total length of cloth and the total cost.", 3,
      f"Length = 2.75 + 1.60 = <b>{tot} m</b><br>Cost = 4.35 × 80 = <b>₹ {cost:.0f}</b>"),
    P("(ii)", "Read the decimal marked by A, B and C on the number line: A = ____ , B = ____ , C = ____", 3,
      f"A = {vals['A']}, B = {vals['B']}, C = {vals['C']}", fig=svg_nl(2, 2, 10, pts))])

# Q9
est = round(4893, -3) + round(3108, -3); assert est == 8000
o, a = mc("8000", ["7000", "9000", "8100"], 9)
q9 = Q("The sum 4,893 + 3,108 estimated by rounding each number to the nearest thousand is", 1, a, opts=o)

# Q10
cost10 = 3 * 28 + 2 * 15; bal = 200 - cost10; assert (cost10, bal) == (114, 86)
q10 = Q("Rahul bought 3 notebooks at ₹ 28 each and 2 pens at ₹ 15 each. He gave the shopkeeper a ₹ 200 note. How much money did the shopkeeper return to him?", 3,
        f"Notebooks = 3 × 28 = ₹ 84; Pens = 2 × 15 = ₹ 30; Total = ₹ {cost10}<br>Balance = 200 − {cost10} = <b>₹ {bal}</b>")
# Q11
qq, rr = divmod(7853, 9); assert 9 * qq + rr == 7853 and (qq, rr) == (872, 5)
q11 = Q("Divide 7,853 by 9. Write the quotient and remainder and check your answer by the division rule.", 3,
        f"Quotient = <b>{qq}</b>, Remainder = <b>{rr}</b><br>Check: Divisor × Quotient + Remainder = 9 × {qq} + {rr} = {9*qq} + {rr} = {9*qq+rr} ✓")
# Q12
inc, food, rent, fee = 24000, 8750, 6500, 3250; sp = food + rent + fee; sav = inc - sp; assert (sp, sav) == (18500, 5500)
v1, v2 = 46 * 100 - 46, 68 * 10 // 2; assert (v1, v2) == (46 * 99, 68 * 5) == (4554, 340)
q12 = Q("", 6, parts=[
    P("(i)", "A family earns ₹ 24,000 in a month. It spends ₹ 8,750 on food, ₹ 6,500 on rent and ₹ 3,250 on school fees. How much does the family save?", 3,
      f"Total spent = 8,750 + 6,500 + 3,250 = ₹ {sp:,}<br>Savings = 24,000 − {sp:,} = <b>₹ {sav:,}</b>"),
    P("(ii)", "Use the quick methods: (a) 46 × 99 = 46 × 100 − 46 = ? (b) 68 × 5 = (68 × 10) ÷ 2 = ?", 3,
      f"(a) 4600 − 46 = <b>{v1}</b> (b) 680 ÷ 2 = <b>{v2}</b>")])
# Q13
A = {i for i in range(1, 25) if i % 4 == 0}; B = {i for i in range(1, 25) if i % 6 == 0}
both = sorted(A & B); assert both == [12, 24] and len(A) == 6 and math.lcm(4, 6) == 12
fig13 = "<b>Switch A</b> (glowing bulbs shown in yellow)" + svg_bulbs(24, A) + "<b>Switch B</b>" + svg_bulbs(24, B)
f36 = [d for d in range(1, 37) if 36 % d == 0]; g = math.gcd(36, 48); pcs = 36 // g + 48 // g; assert (g, pcs) == (12, 7)
q13 = Q("", 6, parts=[
    P("(i)", "Bulbs numbered 1 to 24 are controlled by two switches. Switch A makes some bulbs glow and Switch B makes some other bulbs glow (see the figures). (a) How many bulbs glow when Switch A is pressed? (b) Write the numbers of the bulbs that glow in both cases. (c) Which is the first (smallest) bulb that glows in both cases?", 3,
      f"(a) <b>{len(A)}</b> bulbs (4, 8, 12, 16, 20, 24) (b) <b>{both[0]} and {both[1]}</b> (c) <b>{both[0]}</b> (LCM of 4 and 6)", fig=fig13),
    P("(ii)", "Two ropes of length 36 m and 48 m are cut into equal pieces of the longest possible length. (a) Write all factors of 36. (b) Find the length of each piece. (c) How many pieces are there in all?", 3,
      f"(a) {', '.join(map(str,f36))} (b) HCF of 36 and 48 = <b>{g} m</b> (c) {36//g} + {48//g} = <b>{pcs} pieces</b>")])
# Q14
G = [[4, 2, 5], [1, 7, 3], [6, 0, 8]]
acr = [int("".join(map(str, r))) for r in G]; dn = [int("".join(str(G[r][c]) for r in range(3))) for c in range(3)]
assert (acr, dn) == ([425, 173, 608], [416, 270, 538])
gridh = "<table class='t5' style='font-size:1.15em'>" + "".join("<tr>" + "".join(f"<td style='width:26px'>{x}</td>" for x in r) + "</tr>" for r in G) + "</table>"
fig14 = gridh
til = 7 * 4; perim = 2 * (7 + 4); costt = til * 60; assert (til, perim, costt) == (28, 22, 1680)
q14 = Q("", 6, parts=[
    P("(i)", "A cross-number grid is filled as shown. Numbers read from left to right in a row are ACROSS numbers; those read from top to bottom in a column are DOWN numbers. (a) Write the greatest ACROSS number. (b) Find the difference between the 1st and 2nd ACROSS numbers. (c) Find the sum of the three DOWN numbers.", 3,
      f"(a) <b>{max(acr)}</b> (b) {acr[0]} − {acr[1]} = <b>{acr[0]-acr[1]}</b> (c) {dn[0]} + {dn[1]} + {dn[2]} = <b>{sum(dn)}</b>", fig=fig14),
    P("(ii)", "A floor is covered with square tiles of side 1 m as shown. (a) How many tiles are used? (b) Find the perimeter of the floor. (c) If one tile costs ₹ 60, find the total cost of the tiles.", 3,
      f"(a) 7 × 4 = <b>{til}</b> (b) 2 × (7 + 4) = <b>{perim} m</b> (c) {til} × 60 = <b>₹ {costt:,}</b>", fig=tiles_svg(7, 4, 18, "7 tiles", "4 tiles"))])
# Q15
assert (3 * 100 + 45, 2 * 1000 + 50, 3 * 1000 + 500) == (345, 2050, 3500)
q15 = Q("Fill in the blanks: (a) 3 m 45 cm = ______ cm (b) 2 kg 50 g = ______ g (c) 3 L 500 mL = ______ mL", 3, "(a) 345 (b) 2050 (c) 3500")
q16 = Q("Write True or False: (a) 18:45 on a 24-hour clock is 6:45 p.m. (b) 1 rupee = 10 paise. (c) Water freezes at 0 °C.", 3, "(a) True (b) False (1 rupee = 100 paise) (c) True")
# Q17
s, e = 9 * 60 + 45, 12 * 60 + 20; d = e - s; assert d == 155
bus = d + 20; assert bus == 175
q17 = Q("A train leaves Jaipur at 9:45 a.m. and reaches Ajmer at 12:20 p.m. (a) How long does the journey take? (b) A bus takes 20 minutes more than the train. How long does the bus take?", 3,
        f"(a) 9:45 to 12:20 = <b>2 h 35 min</b> ({d} min) (b) {d} + 20 = {bus} min = <b>2 h 55 min</b>")
# Q18
nodes = {"Jaipur": (45, 100), "Tonk": (115, 150), "Kota": (240, 135), "Bundi": (275, 60), "Ajmer": (140, 35)}
edges = [("Jaipur", "Ajmer", 130), ("Jaipur", "Tonk", 100), ("Tonk", "Kota", 120), ("Kota", "Bundi", 38), ("Ajmer", "Bundi", 150)]
D = {frozenset((a, b)): k for a, b, k in edges}
r1 = D[frozenset(("Jaipur", "Tonk"))] + D[frozenset(("Tonk", "Kota"))]
r2 = D[frozenset(("Jaipur", "Ajmer"))] - D[frozenset(("Jaipur", "Tonk"))]
r3 = D[frozenset(("Jaipur", "Ajmer"))] + D[frozenset(("Ajmer", "Bundi"))] + D[frozenset(("Bundi", "Kota"))]
assert (r1, r2, r3, r3 - r1) == (220, 30, 318, 98)
q18 = Q("The road map shows some cities of Rajasthan and the distances between them (not to scale).", 8, fig=svg_route(nodes, edges), parts=[
    P("(a)", "What is the distance from Jaipur to Kota through Tonk?", 2, f"100 + 120 = <b>{r1} km</b>"),
    P("(b)", "How much longer is the Jaipur–Ajmer road than the Jaipur–Tonk road?", 2, f"130 − 100 = <b>{r2} km</b>"),
    P("(c)", "Which city is nearest to Kota?", 2, "<b>Bundi</b> (38 km)"),
    P("(d)", "A bus goes Jaipur → Ajmer → Bundi → Kota. How far does it travel? How much shorter is the route through Tonk?", 2, f"130 + 150 + 38 = <b>{r3} km</b>; shorter by {r3} − {r1} = <b>{r3-r1} km</b>")])
# Q19
pr = lambda n: n > 1 and all(n % k for k in range(2, int(n ** .5) + 1))
assert pr(53) and not any(pr(x) for x in (51, 57, 55))
o, a = mc("53", ["51", "55", "57"], 19)
q19 = Q("Which of the following is a prime number?", 1, a, opts=o)
tri = [sum(range(1, k + 1)) for k in (1, 2, 3, 5)]; assert tri == [1, 3, 6, 15]
o, a = mc("15", ["10", "12", "18"], 20)
q20 = Q("The staircase figures are made of small squares. How many squares will Fig. 5 have?", 1, a, opts=o, fig=svg_stairs([1, 2, 3]))
# Q21
nm = ["Aman", "Bhavna", "Chetan", "Divya", "Esha"]; vv = [6, 9, 4, 8, 5]
mx = nm[vv.index(max(vv))]; tot21 = sum(vv); dif = max(vv) - min(vv); assert (mx, tot21, dif) == ("Bhavna", 32, 5)
q21 = Q("The bar graph shows the number of story books read by five students in a month.", 3, fig=svg_bars(nm, vv, ylabel="Books"), parts=[
    P("(a)", "Who read the most books?", 1, f"<b>{mx}</b>"),
    P("(b)", "How many books did the five students read altogether?", 1, f"6 + 9 + 4 + 8 + 5 = <b>{tot21}</b>"),
    P("(c)", "How many more books did the top reader read than the lowest reader?", 1, f"9 − 4 = <b>{dif}</b>")])
# Q22
seq = [3 + 4 * i for i in range(6)]; t10 = 3 + 4 * 9; assert (seq[4], seq[5], t10) == (19, 23, 39)
q22 = Q("Look at the pattern: 3, 7, 11, 15, ___, ___, … (a) Write the rule. (b) Write the next two numbers. (c) Find the 10th number of the pattern.", 3,
        f"(a) Add 4 each time (b) <b>19, 23</b> (c) 3 + 9 × 4 = <b>{t10}</b>")

secs = [sec("UNDERSTANDING SHAPE AND SPACE", 21, [q1, q2, q3, q4]),
        sec("NUMBER SYSTEM", 9, [q5, q6, q7, q8]),
        sec("OPERATIONS", 25, [q9, q10, q11, q12, q13, q14]),
        sec("MEASUREMENT", 17, [q15, q16, q17, q18]),
        sec("DATA HANDLING AND PATTERNS", 8, [q19, q20, q21, q22])]
if __name__ == "__main__":
    run(meta(1), secs)
