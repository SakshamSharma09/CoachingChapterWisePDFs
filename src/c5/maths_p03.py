from maths_common import *
import math
from fractions import Fraction as Fr

def cls(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight"
def mixed(f):
    w = f.numerator // f.denominator; r = f - w
    return f"{w} {fr(r.numerator, r.denominator)}" if w and r else (str(w) if w else fr(r.numerator, r.denominator))

# Q1 perimeter basics
L, W = 18, 12; pm = 2 * (L + W); assert pm == 60
o, a = mc("60 m", ["30 m", "216 m", "36 m"], 41)
q1 = Q("A rectangular garden is 18 m long and 12 m wide. The length of the fence needed to go all around it is", 1, a, opts=o)
# Q2
angs = [40, 90, 135]; assert [cls(d) for d in angs] == ["acute", "right", "obtuse"]
fig2 = "".join(svg_angle(d, w=130, h=110) for d in angs)
q2 = Q("Angles A, B and C are shown with their measures.", 6, fig=fig2, parts=[
    P("(i)", "(a) Which angle is a right angle? (b) Which angle is obtuse? (c) By how many degrees is angle C greater than angle A?", 3, f"(a) <b>B</b> (b) <b>C</b> (c) 135° − 40° = <b>{135-40}°</b>"),
    P("(ii)", "Name the solid: (a) 6 faces, 12 edges, 8 vertices, all faces equal squares (b) 1 flat face, 1 curved face, 1 vertex (c) 5 faces, 8 edges, 5 vertices, base is a square", 3, "(a) cube (b) cone (c) square pyramid")])
# Q3
prism = (5, 9, 6); assert prism[0] - prism[1] + prism[2] == 2
q3 = Q("", 6, parts=[
    P("(i)", "(a) How many faces does a cuboid have? (b) How many edges does a square pyramid have? (c) How many curved faces does a cylinder have?", 3, "(a) 6 (b) 8 (c) 1"),
    P("(ii)", "Which solid does each object look like? (a) a tin of ghee (b) a Toblerone chocolate box (c) an Egyptian pyramid", 3, "(a) cylinder (b) triangular prism (c) square pyramid")])
# Q4 house plan
rooms = [("Room A", 0, 0, 5, 4), ("Room B", 5, 0, 3, 4), ("Room C", 8, 0, 4, 4), ("Verandah", 0, 4, 12, 2)]
opens = [("D", 2, 4, 3, 4, "D1"), ("D", 6, 4, 7, 4, "D2"), ("D", 9, 4, 10, 4, "D3"), ("D", 12, 4.5, 12, 5.5, "D4"),
         ("W", 1, 0, 3, 0, "W1"), ("W", 9, 0, 11, 0, "W2")]
ar = {r[0]: r[3] * r[4] for r in rooms}; assert ar == {"Room A": 20, "Room B": 12, "Room C": 16, "Verandah": 24}
big = max(ar, key=lambda k: ar[k] if k != "Verandah" else 0); tilec = ar["Verandah"] * 55; tot = 12 * 6; assert (big, tilec, tot) == ("Room A", 1320, 72)
q4 = Q("Study the plan of a farm house near Bharatpur and answer.", 8, fig=svg_plan(rooms, opens, u=26, note="D = door (red), W = window (blue)."), parts=[
    P("(a)", "What is the area of Room C?", 2, f"4 × 4 = <b>{ar['Room C']} sq m</b>"),
    P("(b)", "Which of the three rooms (A, B, C) is the largest? Write its area.", 2, f"<b>Room A</b>, 5 × 4 = <b>20 sq m</b>"),
    P("(c)", "The Verandah floor is to be tiled at ₹ 55 per sq m. Find the cost.", 2, f"Area = 12 × 2 = 24 sq m; Cost = 24 × 55 = <b>₹ {tilec:,}</b>"),
    P("(d)", "Find the total floor area of the whole house (12 m by 6 m).", 2, f"12 × 6 = <b>{tot} sq m</b> (= 20 + 12 + 16 + 24)")])
assert sum(ar.values()) == tot
# Q5-7
assert (605432 // 100000) == 6
o, a = mc("6,00,000", ["60,000", "6,000", "6,00,00,000"], 45)
q5 = Q("In the number 6,05,432, the place value of 6 is", 1, a, opts=o)
r_ = round(38527, -2); assert r_ == 38500
o, a = mc("38,500", ["38,000", "39,000", "38,600"], 46)
q6 = Q("38,527 rounded off to the nearest hundred is", 1, a, opts=o)
assert 99999 - 10000 == 89999
o, a = mc("89,999", ["90,000", "89,000", "99,990"], 47)
q7 = Q("The difference between the greatest and the smallest 5-digit numbers is", 1, a, opts=o)
# Q8
left = Fr(55, 10) - Fr(275, 100); assert left == Fr(11, 4)
extra = 2.75 + 1.5; assert abs(extra - 4.25) < 1e-9
pts = {"A": 2, "B": 5, "C": 8}; vals = {k: 1 + Fr(v, 5) for k, v in pts.items()}
assert [str(v) for v in vals.values()] == ["7/5", "2", "13/5"]
q8 = Q("", 6, parts=[
    P("(i)", "A water tank has 5.5 litres of water. 2.75 litres are used for plants. (a) How much water is left? (b) If 1.5 litres more are poured in later, how much water will the tank have?", 3,
      f"(a) 5.50 − 2.75 = <b>2.75 L</b> (b) 2.75 + 1.50 = <b>4.25 L</b>"),
    P("(ii)", "Write the number shown by A, B and C: A = ____ , B = ____ , C = ____", 3, "A = " + mixed(vals["A"]) + ", B = 2, C = " + mixed(vals["C"]), fig=svg_nl(1, 2, 5, pts))])
# Q9
assert 125 * 8 == 1000
o, a = mc("1000", ["800", "1200", "100"], 49)
q9 = Q("125 × 8 = ?", 1, a, opts=o)
# Q10
cost = 5 * 240; prof = 1450 - cost; assert (cost, prof) == (1200, 250)
q10 = Q("A shopkeeper bought 5 boxes of sweets at ₹ 240 per box and sold all the sweets for ₹ 1,450. Find his profit.", 3, f"Cost price = 5 × 240 = ₹ {cost:,}<br>Profit = 1,450 − {cost:,} = <b>₹ {prof}</b>")
q_, r2 = divmod(5000, 12); assert (q_, r2) == (416, 8) and 12 * q_ + r2 == 5000
q11 = Q("5,000 laddoos are packed in boxes of 12 each. How many full boxes are made and how many laddoos are left? Check your answer.", 3,
        f"5000 ÷ 12: <b>{q_} boxes</b>, remainder <b>{r2} laddoos</b><br>Check: 12 × {q_} + {r2} = {12*q_} + {r2} = 5000 ✓")
# Q12
fare = 4 * 135; entry = 4 * 60; food = 480; tt = fare + entry + food; rem = 1500 - tt; assert (fare, entry, tt, rem) == (540, 240, 1260, 240)
a1 = 15 * 100 - 15; a2 = 24 * 100 // 4; assert (a1, a2) == (15 * 99, 24 * 25) == (1485, 600)
q12 = Q("", 6, parts=[
    P("(i)", "Four friends visited Amer Fort. Bus fare is ₹ 135 per person, entry ticket is ₹ 60 per person and they spent ₹ 480 on food. They had ₹ 1,500 in all. How much money was left?", 3,
      f"Fare = ₹ {fare}; Tickets = ₹ {entry}; Food = ₹ {food}; Total = ₹ {tt:,}<br>Left = 1,500 − {tt:,} = <b>₹ {rem}</b>"),
    P("(ii)", "Use quick methods: (a) 15 × 99 = 15 × 100 − 15 (b) 24 × 25 = (24 × 100) ÷ 4", 3, f"(a) 1500 − 15 = <b>{a1}</b> (b) 2400 ÷ 4 = <b>{a2}</b>")])
# Q13
X = {i for i in range(1, 21) if i % 2 == 0}; Y = {i for i in range(1, 21) if i % 5 == 0}
only = sorted(Y - X); b = sorted(X & Y); assert (len(X), only, b) == (10, [5, 15], [10, 20])
fig13 = "<b>Switch X</b>" + svg_bulbs(20, X, col="#8fc5f2") + "<b>Switch Y</b>" + svg_bulbs(20, Y, col="#f2a08f")
l = math.lcm(6, 8); n = 120 // l; assert (l, n) == (24, 5)
q13 = Q("", 6, parts=[
    P("(i)", "Bulbs 1 to 20 glow as shown for two switches X and Y. (a) How many bulbs glow with X? (b) Which bulbs glow with Y but not with X? (c) What is the smallest number of a bulb that glows with both?", 3,
      f"(a) <b>{len(X)}</b> (b) <b>{only[0]} and {only[1]}</b> (c) <b>{b[0]}</b> (LCM of 2 and 5)", fig=fig13),
    P("(ii)", "A red light blinks every 6 seconds and a green light every 8 seconds. They blink together at the start. (a) After how many seconds will they blink together again? (b) How many times in all will they blink together in the next 2 minutes (counting the blink at 120 s)?", 3,
      f"(a) LCM of 6 and 8 = <b>{l} s</b> (b) 2 min = 120 s; 120 ÷ 24 = <b>{n} times</b> (at 24, 48, 72, 96 and 120 s)")])
# Q14
G = [[5, 1, 8], [2, 7, 4], [9, 3, 6]]
acr = [int("".join(map(str, r))) for r in G]; dn = [int("".join(str(G[r][c]) for r in range(3))) for c in range(3)]
assert (acr, dn) == ([518, 274, 936], [529, 173, 846]) and sum(acr) == 1728 and max(dn) - min(dn) == 673
gridh = "<table class='t5' style='font-size:1.15em'>" + "".join("<tr>" + "".join(f"<td style='width:26px'>{x}</td>" for x in r) + "</tr>" for r in G) + "</table>"
border = 2 * (8 + 5) - 4; inner = (8 - 2) * (5 - 2); assert 40 - inner == border == 22
q14 = Q("", 6, parts=[
    P("(i)", "In the filled grid, rows are ACROSS numbers and columns are DOWN numbers. (a) Write the greatest ACROSS number. (b) Find the sum of all three ACROSS numbers. (c) Find the difference between the greatest and the smallest DOWN numbers.", 3,
      f"(a) <b>936</b> (b) 518 + 274 + 936 = <b>{sum(acr):,}</b> (c) 846 − 173 = <b>{max(dn)-min(dn)}</b>", fig=gridh),
    P("(ii)", "A floor 8 m by 5 m is covered by square tiles of side 1 m (figure). (a) How many tiles are there in all? (b) How many tiles touch the walls (the border tiles)?", 3,
      f"(a) 8 × 5 = <b>40</b> (b) Inner tiles = 6 × 3 = 18, so border tiles = 40 − 18 = <b>{border}</b>", fig=tiles_svg(8, 5, 18, "8 tiles", "5 tiles"))])
# Q15-17
assert (7 * 10 + 5, 3 * 1000 + 250, 2500 / 1000) == (75, 3250, 2.5)
q15 = Q("Fill in the blanks: (a) 7 cm 5 mm = ______ mm (b) 3 kg 250 g = ______ g (c) 2500 mL = ______ L", 3, "(a) 75 (b) 3250 (c) 2.5")
q16 = Q("Write True or False: (a) 5:00 a.m. is written as 05:00 hours on a 24-hour clock. (b) ₹ 50 = 5000 paise. (c) A kilometre is shorter than a metre.", 3, "(a) True (b) True (c) False (1 km = 1000 m)")
end = 17 * 60 + 30 + 2 * 60 + 40; h, m = divmod(end, 60); assert (h, m) == (20, 10)
q17 = Q("A folk-music programme starts at 5:30 p.m. and lasts for 2 hours 40 minutes. (a) At what time does it end (in p.m.)? (b) Write the ending time on a 24-hour clock.", 3,
        "(a) 5:30 + 2 h 40 min = <b>8:10 p.m.</b> (b) <b>20:10</b> hours")
# Q18 distance table
cit = ["Jaipur", "Udaipur", "Kota", "Bharatpur"]
Dm = {("Jaipur", "Udaipur"): 400, ("Jaipur", "Kota"): 250, ("Jaipur", "Bharatpur"): 185, ("Udaipur", "Kota"): 270, ("Udaipur", "Bharatpur"): 580, ("Kota", "Bharatpur"): 330}
def d(a, b): return 0 if a == b else Dm.get((a, b)) or Dm[(b, a)]
tbl = tab([[a] + [("—" if a == b else d(a, b)) for b in cit] for a in cit], ["km"] + cit)
c1 = d("Kota", "Udaipur"); c2 = d("Jaipur", "Bharatpur") + d("Bharatpur", "Kota") - d("Jaipur", "Kota"); c4 = 2 * d("Jaipur", "Kota")
near = min(cit[1:], key=lambda c: d("Jaipur", c)); far = max(cit[1:], key=lambda c: d("Jaipur", c))
assert (c1, c2, near, far, c4) == (270, 265, "Bharatpur", "Udaipur", 500)
q18 = Q("The table gives the road distance (in km) between four cities of Rajasthan (approximate, for practice).", 8, fig=tbl, parts=[
    P("(a)", "What is the distance between Udaipur and Kota?", 2, f"<b>{c1} km</b>"),
    P("(b)", "How much longer is the journey Jaipur → Bharatpur → Kota than the direct road from Jaipur to Kota?", 2, f"185 + 330 = 515 km; 515 − 250 = <b>{c2} km</b>"),
    P("(c)", "Which city is nearest to Jaipur and which is farthest from Jaipur?", 2, f"Nearest: <b>{near}</b> (185 km); farthest: <b>{far}</b> (400 km)"),
    P("(d)", "How far is a return trip Jaipur → Kota → Jaipur?", 2, f"250 + 250 = <b>{c4} km</b>")])
# Q19-20
o, a = mc("even", ["odd", "prime", "can be odd or even"], 61)
q19 = Q("The sum of two odd numbers is always", 1, a, opts=o)
assert 7 + 9 == 16 and 3 + 5 == 8
t6 = sum(range(1, 7)); assert t6 == 21
o, a = mc("21", ["18", "24", "36"], 62)
q20 = Q("Dots are arranged in triangles. Fig. 1, 2 and 3 have 1, 3 and 6 dots. How many dots will Fig. 6 have?", 1, a, opts=o, fig=svg_tritri([1, 2, 3]))
# Q21
nm = ["Mon", "Tue", "Wed", "Thu", "Fri"]; vv = [7, 5, 9, 6, 8]; assert sum(vv) == 35
q21 = Q("The bar graph shows the number of students who visited the school library on five days.", 3, fig=svg_bars(nm, vv, ylabel="Students"), parts=[
    P("(a)", "On which day did the most students visit?", 1, "<b>Wednesday</b> (9 students)"),
    P("(b)", "How many students visited the library in the five days?", 1, "7 + 5 + 9 + 6 + 8 = <b>35</b>"),
    P("(c)", "How many more students came on Wednesday than on Tuesday?", 1, "9 − 5 = <b>4</b>")])
seq = [5 * 2 ** i for i in range(8)]; assert seq[:5] == [5, 10, 20, 40, 80] and seq[5] == 160 and seq[7] == 640
q22 = Q("Look at the pattern: 5, 10, 20, 40, ___, ___, … (a) Write the rule. (b) Write the next two numbers. (c) Find the 8th number.", 3,
        "(a) Multiply the previous number by 2 (b) <b>80, 160</b> (c) 160 → 320 → 640: <b>640</b>")
q22["q"] = "Look at the pattern: 5, 10, 20, 40, ___, ___, … (a) Write the rule. (b) Write the next two numbers. (c) Find the 8th number."
q22["ans"] = "(a) Multiply the previous number by 2 (b) <b>80, 160</b> (c) 6th = 160, 7th = 320, 8th = <b>640</b>"
secs = [sec("UNDERSTANDING SHAPE AND SPACE", 21, [q1, q2, q3, q4]),
        sec("NUMBER SYSTEM", 9, [q5, q6, q7, q8]),
        sec("OPERATIONS", 25, [q9, q10, q11, q12, q13, q14]),
        sec("MEASUREMENT", 17, [q15, q16, q17, q18]),
        sec("DATA HANDLING AND PATTERNS", 8, [q19, q20, q21, q22])]
if __name__ == "__main__":
    run(meta(3), secs)
