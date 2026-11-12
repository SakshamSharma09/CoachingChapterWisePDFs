from maths_common import *
import math
from fractions import Fraction as Fr

def cls(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight"
def words_ind(n):  # for 3,45,200 style
    return n

# Q1
cells = {(c, r) for r, L in enumerate([1, 4, 4, 4]) for c in range(L)}; assert len(cells) == 13
o, a = mc("13 sq cm", ["12 sq cm", "16 sq cm", "26 sq cm"], 11)
q1 = Q("Each small square is 1 cm × 1 cm. What is the area of the shaded shape?", 1, a, opts=o, fig=svg_grid(cells))
# Q2
angs = [60, 180, 150]; assert [cls(d) for d in angs] == ["acute", "straight", "obtuse"]
fig2 = "".join(svg_angle(d, w=130, h=110) for d in angs)
q2 = Q("Three angles P, Q and R are shown with their measures.", 6, fig=fig2, parts=[
    P("(i)", "Write the type of angle: (a) P ______ (b) Q ______ (c) R ______", 3, "(a) acute (b) straight (c) obtuse"),
    P("(ii)", "Which solid is formed by folding each net? (a) a net of 6 equal squares ______ (b) a net of 2 circles and 1 rectangle ______ (c) a net of 1 circle and 1 sector of a circle ______", 3, "(a) cube (b) cylinder (c) cone")])
# Q3
cub = (8, 12, 6); tp = (4, 6, 4); assert cub[0] - cub[1] + cub[2] == 2 and tp[0] - tp[1] + tp[2] == 2
q3 = Q("", 6, parts=[
    P("(i)", "(a) How many vertices does a cuboid have? (b) How many edges does a triangular pyramid (tetrahedron) have? (c) How many flat faces does a cylinder have?", 3, f"(a) {cub[0]} (b) {tp[1]} (c) 2"),
    P("(ii)", "Name the solid that each object looks like: (a) a matchbox (b) a football (c) a joker's cap", 3, "(a) cuboid (b) sphere (c) cone")])
# Q4 school plan
rooms = [("Lab", 0, 0, 4, 5), ("Classroom", 4, 0, 6, 5), ("Office", 0, 5, 5, 3), ("Store", 5, 5, 5, 3)]
opens = [("D", 4, 3, 4, 4, "D1"), ("D", 1, 5, 2, 5, "D2"), ("D", 7, 5, 8, 5, "D3"), ("D", 5, 6, 5, 7, "D4"), ("D", 10, 1, 10, 2, "D5"),
         ("W", 1, 0, 3, 0, "W1"), ("W", 6, 0, 8, 0, "W2"), ("W", 1, 8, 3, 8, "W3")]
ar = {r[0]: r[3] * r[4] for r in rooms}; assert ar == {"Lab": 20, "Classroom": 30, "Office": 15, "Store": 15}
cost = ar["Office"] * 40; per = 2 * (10 + 8); doors = sum(o[0] == "D" for o in opens); wins = sum(o[0] == "W" for o in opens)
assert (cost, per, doors, wins) == (600, 36, 5, 3)
q4 = Q("The plan of a school block in Alwar is shown. Study it and answer.", 8,
       fig=svg_plan(rooms, opens, u=26, note="D = door (red), W = window (blue)."), parts=[
    P("(a)", "What is the area of the Classroom?", 2, f"6 × 5 = <b>{ar['Classroom']} sq m</b>"),
    P("(b)", "How much more floor area does the Classroom have than the Lab?", 2, f"30 − 20 = <b>{ar['Classroom']-ar['Lab']} sq m</b>"),
    P("(c)", "The Office floor is to be covered with carpet at ₹ 40 per sq m. Find the cost.", 2, f"15 × 40 = <b>₹ {cost}</b>"),
    P("(d)", "Find the perimeter of the whole block (10 m by 8 m). How many doors are there in all?", 2, f"2 × (10 + 8) = <b>{per} m</b>; doors = <b>{doors}</b>")])
# Q5-7
n = 345200; assert indian(n) == "3,45,200" and intl(n) == "345,200"
o, a = mc("345,200", ["3,45,200", "34,520", "3,452,000"], 15)
q5 = Q("The number 3,45,200 written in the international system is", 1, a, opts=o)
assert 99999 + 1 == 100000
o, a = mc("1,00,000", ["99,990", "10,000", "10,00,000"], 16)
q6 = Q("The successor of 99,999 is", 1, a, opts=o)
nums = [48210, 48021, 48201, 48012]; assert min(nums) == 48012
o, a = mc("48,012", ["48,021", "48,201", "48,210"], 17)
q7 = Q("Which is the smallest of these numbers: 48,210; 48,021; 48,201; 48,012?", 1, a, opts=o)
# Q8
tot = Fr(1, 2) + Fr(1, 4); rest = 1 - tot; assert (tot, rest) == (Fr(3, 4), Fr(1, 4))
pts = {"A": 3, "B": 5, "C": 7}
def mixed(f):
    w = f.numerator // f.denominator; r = f - w
    return f"{w} {fr(r.numerator, r.denominator)}" if w and r else (str(w) if w else fr(r.numerator, r.denominator))
vals = {k: Fr(v, 4) for k, v in pts.items()}
q8 = Q("", 6, parts=[
    P("(i)", "Ravi walked 1/2 km in the morning and 1/4 km in the evening. (a) How far did he walk in all? (b) How much less than 1 km is that?", 3,
      f"(a) 1/2 + 1/4 = 2/4 + 1/4 = <b>{fr(3,4)} km</b> (b) 1 − 3/4 = <b>{fr(1,4)} km</b>"),
    P("(ii)", "Write the fraction shown by A, B and C: A = ____ , B = ____ , C = ____", 3,
      "A = " + mixed(vals["A"]) + ", B = " + mixed(vals["B"]) + ", C = " + mixed(vals["C"]), fig=svg_nl(0, 2, 4, pts))])
# Q9
assert 36 * 25 == 900
o, a = mc("900", ["725", "720", "1000"], 21)
q9 = Q("36 × 25 = ?", 1, a, opts=o)
# Q10
filled = 8 * 750; left = 40 * 1000 - filled; assert (filled, left) == (6000, 34000)
q10 = Q("A dairy has 40 litres of milk. It fills 8 bottles of 750 mL each. How many litres of milk are left?", 3,
        f"Milk in bottles = 8 × 750 = {filled} mL = 6 L<br>Left = 40 − 6 = <b>{left//1000} L</b>")
q_, r_ = divmod(3458, 8); assert (q_, r_) == (432, 2) and 8 * q_ + r_ == 3458
q11 = Q("A school library has 3,458 books. They are arranged equally on 8 shelves. How many books are on each shelf and how many are left over? Verify your answer.", 3,
        f"3458 ÷ 8: Quotient = <b>{q_}</b> books per shelf, Remainder = <b>{r_}</b><br>Check: 8 × {q_} + {r_} = {8*q_} + {r_} = {8*q_+r_} ✓")
# Q12
bill = 5 * 62 + 2 * 118 + 145; ch = 1000 - bill; assert (bill, ch) == (691, 309)
est = round(6812, -2) - round(2395, -2); ex = 6812 - 2395; assert (est, ex) == (4400, 4417)
q12 = Q("", 6, parts=[
    P("(i)", "Anita bought 5 kg rice at ₹ 62 per kg, 2 kg dal at ₹ 118 per kg and 1 L oil for ₹ 145. She paid ₹ 1,000. How much change did she get?", 3,
      f"Rice = ₹ 310; Dal = ₹ 236; Oil = ₹ 145; Bill = ₹ {bill}<br>Change = 1000 − {bill} = <b>₹ {ch}</b>"),
    P("(ii)", "(a) Estimate 6,812 − 2,395 by rounding each number to the nearest hundred. (b) Find the exact difference.", 3,
      f"(a) 6,800 − 2,400 = <b>{est:,}</b> (b) 6,812 − 2,395 = <b>{ex:,}</b>")])
# Q13
P3 = {i for i in range(1, 31) if i % 3 == 0}; Q5 = {i for i in range(1, 31) if i % 5 == 0}; bo = sorted(P3 & Q5)
assert (len(P3), len(Q5), bo) == (10, 6, [15, 30])
fig13 = "<b>Switch P</b>" + svg_bulbs(30, P3, col="#7ed6a0") + "<b>Switch Q</b>" + svg_bulbs(30, Q5, col="#f08a8a")
l = math.lcm(12, 18); assert l == 36
q13 = Q("", 6, parts=[
    P("(i)", "Bulbs 1 to 30 are connected to two switches P and Q. The bulbs that glow are coloured. (a) How many bulbs glow with switch P? (b) How many glow with switch Q? (c) Which bulbs glow with both switches?", 3,
      f"(a) <b>{len(P3)}</b> (b) <b>{len(Q5)}</b> (c) <b>15 and 30</b> (common multiples of 3 and 5)", fig=fig13),
    P("(ii)", "Two school bells ring together at 8:00 a.m. One rings every 12 minutes and the other every 18 minutes. (a) After how many minutes will they ring together again? (b) At what time?", 3,
      f"(a) LCM of 12 and 18 = <b>{l} minutes</b> (b) 8:00 + 36 min = <b>8:36 a.m.</b>")])
# Q14
G = [[3, 6, 1], [8, 5, 2], [9, 4, 7]]
acr = [int("".join(map(str, r))) for r in G]; dn = [int("".join(str(G[r][c]) for r in range(3))) for c in range(3)]
assert (acr, dn) == ([361, 852, 947], [389, 654, 127]) and acr[0] + acr[1] == 1213
gridh = "<table class='t5' style='font-size:1.15em'>" + "".join("<tr>" + "".join(f"<td style='width:26px'>{x}</td>" for x in r) + "</tr>" for r in G) + "</table>"
q14 = Q("", 6, parts=[
    P("(i)", "In this filled cross-number grid, each ROW is an ACROSS number and each COLUMN is a DOWN number. (a) Write the smallest ACROSS number. (b) Add the 1st and 2nd ACROSS numbers. (c) Write the greatest DOWN number.", 3,
      f"(a) <b>{min(acr)}</b> (b) 361 + 852 = <b>{acr[0]+acr[1]}</b> (c) <b>{max(dn)}</b>", fig=gridh),
    P("(ii)", "36 square tiles of side 1 cm are arranged as a rectangle of 9 tiles in a row (figure). (a) How many rows are there? (b) Find the perimeter of the rectangle. (c) If the same tiles are put in 6 rows, how many tiles are in each row?", 3,
      f"(a) 36 ÷ 9 = <b>4 rows</b> (b) 2 × (9 + 4) = <b>26 cm</b> (c) 36 ÷ 6 = <b>6 tiles</b>", fig=tiles_svg(9, 4, 16, "9 tiles", "4 rows"))])
assert 36 // 9 == 4 and 2 * (9 + 4) == 26 and 36 // 6 == 6
# Q15-17
assert (2.5 * 1000, 4500 / 1000, 2 * 60 + 15) == (2500, 4.5, 135)
q15 = Q("Fill in the blanks: (a) 2.5 km = ______ m (b) 4500 g = ______ kg (c) 2 h 15 min = ______ min", 3, "(a) 2500 (b) 4.5 (c) 135")
q16 = Q("Write True or False: (a) 3 p.m. is 13:00 on a 24-hour clock. (b) The normal temperature of the human body is about 37 °C. (c) ₹ 3.05 = 305 paise.", 3,
        "(a) False (3 p.m. = 15:00) (b) True (c) True")
g = 2 * 48500 + 36750; assert g == 133750
q17 = Q("A trader bought 2 sacks of wheat of 48 kg 500 g each and 1 sack of bajra of 36 kg 750 g. Find the total mass of grain in kg and g.", 3,
        f"Wheat = 2 × 48 kg 500 g = 97 kg<br>Total = 97 kg + 36 kg 750 g = <b>133 kg 750 g</b>")
# Q18
nodes = {"Bikaner": (50, 40), "Jodhpur": (140, 90), "Barmer": (130, 150), "Jaisalmer": (270, 100)}
edges = [("Bikaner", "Jodhpur", 250), ("Jodhpur", "Barmer", 200), ("Barmer", "Jaisalmer", 160), ("Jodhpur", "Jaisalmer", 285), ("Bikaner", "Jaisalmer", 330)]
v1 = 200 + 160; v2 = v1 - 285; v4 = 250 + 200 + 160; v5 = v4 - 330
assert (v1, v2, v4, v5) == (360, 75, 610, 280)
q18 = Q("Distances between four cities of Rajasthan are shown on the map (not to scale).", 8, fig=svg_route(nodes, edges), parts=[
    P("(a)", "Find the distance from Jodhpur to Jaisalmer through Barmer.", 2, f"200 + 160 = <b>{v1} km</b>"),
    P("(b)", "How much shorter is the direct Jodhpur–Jaisalmer road than the route through Barmer?", 2, f"360 − 285 = <b>{v2} km</b>"),
    P("(c)", "Which city is nearest to Jodhpur?", 2, "<b>Barmer</b> (200 km)"),
    P("(d)", "A car goes Bikaner → Jodhpur → Barmer → Jaisalmer. How far does it travel? How much more is it than the direct road Bikaner–Jaisalmer?", 2, f"250 + 200 + 160 = <b>{v4} km</b>; {v4} − 330 = <b>{v5} km</b> more")])
# Q19-20
assert 11 * 11 == 121 and not any(int(x ** .5) ** 2 == x for x in (120, 122, 125))
o, a = mc("121", ["120", "122", "125"], 30)
q19 = Q("Which of these is a square number?", 1, a, opts=o)
sticks = [3 * k + 1 for k in (1, 2, 3, 6)]; assert sticks == [4, 7, 10, 19]
o, a = mc("19", ["16", "18", "21"], 31)
q20 = Q("Squares are made in a row with matchsticks. Fig. 1 needs 4 sticks. How many sticks are needed for Fig. 6?", 1, a, opts=o, fig=svg_rowsq([1, 2, 3]))
# Q21 tally
def tally(n): return ("<s>||||</s> " * (n // 5) + "|" * (n % 5)).strip()
fr_ = {"Mango": 13, "Apple": 9, "Banana": 7, "Guava": 6, "Orange": 5}; T = sum(fr_.values()); assert T == 40
fig21 = tab([[k, tally(v)] for k, v in fr_.items()], ["Fruit", "Tally marks"])
q21 = Q("Students of Class 5 were asked to choose their favourite fruit. The tally table shows the result (a group of five is shown as ||||).", 3, fig=fig21, parts=[
    P("(a)", "Which fruit was chosen by the most students? How many chose it?", 1, "<b>Mango</b>, 13 students"),
    P("(b)", "How many students were asked in all?", 1, f"13 + 9 + 7 + 6 + 5 = <b>{T}</b>"),
    P("(c)", "How many more students chose Mango than Banana?", 1, f"13 − 7 = <b>{13-7}</b>")])
# Q22
odd = [sum(range(1, 2 * k, 2)) for k in (4, 6, 10)]; assert odd == [16, 36, 100]
q22 = Q("Look at the pattern: 1 = 1 × 1; 1 + 3 = 2 × 2; 1 + 3 + 5 = 3 × 3. Find: (a) 1 + 3 + 5 + 7 (b) 1 + 3 + 5 + 7 + 9 + 11 (c) the sum of the first 10 odd numbers", 3,
        "The sum of the first n odd numbers = n × n. (a) 4 × 4 = <b>16</b> (b) 6 × 6 = <b>36</b> (c) 10 × 10 = <b>100</b>")

secs = [sec("UNDERSTANDING SHAPE AND SPACE", 21, [q1, q2, q3, q4]),
        sec("NUMBER SYSTEM", 9, [q5, q6, q7, q8]),
        sec("OPERATIONS", 25, [q9, q10, q11, q12, q13, q14]),
        sec("MEASUREMENT", 17, [q15, q16, q17, q18]),
        sec("DATA HANDLING AND PATTERNS", 8, [q19, q20, q21, q22])]
if __name__ == "__main__":
    run(meta(2), secs)
