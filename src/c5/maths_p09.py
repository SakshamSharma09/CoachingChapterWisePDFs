from maths_h import *
import math

I = []
cells = shape(["#...", "####", "####", ".##."]); p = perim(cells)
adj = sum(1 for (c, r) in cells for d in ((1, 0), (0, 1)) if (c + d[0], r + d[1]) in cells); assert p == 4 * len(cells) - 2 * adj == 16
I.append(mc("The side of each square is 1 cm. The perimeter of the shaded figure is", f"{p} cm", ["18 cm", "14 cm", "22 cm"], 1, fig=svg_grid(cells, 20)))

def kind(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight" if d == 180 else "reflex"
assert [kind(15), kind(175), kind(270)] == ["acute", "obtuse", "reflex"]
I.append(Q("", 6, parts=[
    P("(i)", "Write the type of each angle shown: (a) &ang;P (b) &ang;Q (c) &ang;R", 3, "(a) acute (less than 90&deg;) &nbsp; (b) obtuse (just less than 180&deg;) &nbsp; (c) reflex (more than 180&deg;)", fig=angles([("P", 15), ("Q", 175), ("R", 270)])),
    P("(ii)", "(a) Through how many degrees does the hour hand turn from 12 to 5? (b) What type of angle is made by the hands of a clock at 3 o&rsquo;clock? (c) How many straight angles make a complete turn?", 3,
      f"(a) 5 &times; 30 = <b>{5*30}&deg;</b> &nbsp; (b) right angle &nbsp; (c) 360 &divide; 180 = <b>{360//180}</b>")]))

T = {"Cube": (6, 12, 8), "Triangular pyramid": (4, 6, 4), "Square pyramid": (5, 8, 5), "Triangular prism": (5, 9, 6)}
for f, e, v in T.values(): assert f + v - e == 2
same = [k for k, (f, e, v) in T.items() if f == v]; mv = max(T, key=lambda k: T[k][2]); se = T["Cube"][1] + T["Triangular prism"][1]
assert same == ["Triangular pyramid", "Square pyramid"] and mv == "Cube" and se == 21
tt = tbl(["Solid", "Faces", "Edges", "Vertices"], [[k, *v] for k, v in T.items()])
I.append(Q("", 6, parts=[
    P("(i)", "Name the solid that looks like: (a) a brick (b) a funnel (c) the Great Pyramid of Egypt", 3, "(a) cuboid &nbsp; (b) cone &nbsp; (c) square pyramid"),
    P("(ii)", "Use the table. (a) Which two solids have the same number of faces and vertices? (b) Which solid has the most vertices? (c) What is the total number of edges of a cube and a triangular prism together?", 3,
      f"(a) <b>Triangular pyramid</b> (4, 4) and <b>square pyramid</b> (5, 5) &nbsp; (b) <b>Cube</b> (8) &nbsp; (c) 12 + 9 = <b>{se}</b>", fig=tt)]))

top = [("Living Room", 7), ("Store", 3)]; bot = [("Bedroom", 7), ("Toilet", 3)]; h1, h2 = 4, 3
pl = 2 * (7 + 4); sa = 3 * 4; carp = 7 * 3 * 85; assert (pl, sa, carp) == (22, 12, 1785)
I.append(Q("The plan of Hari&rsquo;s house in Kota is given.", 8, fig=plan(10, top, bot, h1, h2), parts=[
    P("(a)", "Find the perimeter of the Living Room.", 2, f"2 &times; (7 + 4) = <b>{pl} m</b>"),
    P("(b)", "Find the area of the Store.", 2, f"3 &times; 4 = <b>{sa} sq m</b>"),
    P("(c)", "In which direction (with respect to the Living Room) is the Store?", 2, "<b>East</b> (it is on the right side; north is at the top)"),
    P("(d)", "A carpet costing &#8377; 85 per sq m is laid in the Bedroom. Find the cost.", 2, f"Area = 7 &times; 3 = 21 sq m; cost = 21 &times; 85 = <b>{rs(carp)}</b>")]))

n = 608347; assert str(n)[1] == "0"
I.append(mc("In the number 6,08,347 the digit in the ten-thousands place is", 0, [6, 8, 3], 2))
dg = [7, 0, 4, 2, 9, 6]; s6 = sorted(dg); s6[0], s6[1] = s6[1], s6[0]; sm = int("".join(map(str, s6))); assert sm == 204679
I.append(mc("The smallest 6-digit number that can be made from the digits 7, 0, 4, 2, 9, 6 (each used once) is", ind(sm), [ind(24679), ind(204769), ind(246790)], 0))
I.append(mc("705009 is read as", "seven lakh five thousand nine", ["seven lakh fifty thousand nine", "seventy lakh five thousand nine", "seven lakh five thousand ninety"], 3, why="7,05,009"))

tot = Fr(5, 4) + 0  # placeholder to keep Fr imported
from decimal import Decimal as D
w = [D("1.25"), D("2.5"), D("0.75")]; sw = sum(w); df = max(w) - min(w); assert (sw, df) == (D("4.5"), D("1.75")) and D("3.5") - sw == -1
fig8 = nl(0, 2, 8, {"A": Fr(3, 4), "B": Fr(5, 4), "C": Fr(7, 4)}, {0: "0", 4: "1", 8: "2"})
I.append(Q("", 6, parts=[
    P("(i)", "A potter of Kota made three pots weighing 1.25 kg, 2.5 kg and 0.75 kg. (a) What is the total weight? (b) How much heavier is the heaviest pot than the lightest? (c) Is the total more or less than 5 kg?", 3,
      f"(a) 1.25 + 2.50 + 0.75 = <b>{sw} kg</b> &nbsp; (b) 2.50 &minus; 0.75 = <b>{df} kg</b> &nbsp; (c) less (4.5 kg &lt; 5 kg)"),
    P("(ii)", "The line from 0 to 2 is divided into 8 equal parts. Write the fraction shown by A, B and C (write B and C as mixed numbers).", 3, "A = 3/4 &nbsp; B = 5/4 = 1 1/4 &nbsp; C = 7/4 = 1 3/4", fig=fig8)]))

dv9 = 4923; assert dv9 % 9 == 0 and all(x % 9 for x in (4921, 4925, 4927))
I.append(mc("Which of these numbers is divisible by 9?", ind(dv9), [ind(4921), ind(4925), ind(4927)], 2, why="4 + 9 + 2 + 3 = 18, a multiple of 9"))

b, pr, disc = 28, 650, 1200; cost = b * pr - disc; assert (b * pr, cost) == (18200, 17000)
I.append(Q("A school in Jodhpur buys 28 benches at &#8377; 650 each. The shopkeeper gives a discount of &#8377; 1,200 on the whole bill. How much money does the school pay?", 3,
           f"Cost of benches = 28 &times; 650 = {rs(b*pr)}<br>After discount = {b*pr} &minus; {disc} = <b>{rs(cost)}</b>"))
q, r = divmod(9876, 13); assert (q, r) == (759, 9) and 13 * q + r == 9876
I.append(Q("Divide 9,876 by 13. Write the quotient and the remainder, and check the answer by multiplication.", 3,
           f"Quotient = <b>{q}</b>, remainder = <b>{r}</b>.<br>Check: 13 &times; {q} = {13*q}; {13*q} + {r} = {13*q+r}. &#10003;"))

dly = 35 * 52; mo = dly * 30; left = mo - 18000; assert (dly, mo, left) == (1820, 54600, 36600)
a1, a2, a3 = 52 * 98, 36 * 25, 4000 - 1997; assert (5200 - 104, 36 * 100 // 4, 2003) == (a1, a2, a3)
I.append(Q("", 6, parts=[
    P("(i)", "Ramlal sells 35 litres of milk every day at &#8377; 52 per litre. (a) How much does he earn in a day? (b) How much does he earn in 30 days? (c) His monthly cost of cattle feed is &#8377; 18,000. How much is left?", 3,
      f"(a) 35 &times; 52 = <b>{rs(dly)}</b> &nbsp; (b) 1,820 &times; 30 = <b>{rs(mo)}</b> &nbsp; (c) 54,600 &minus; 18,000 = <b>{rs(left)}</b>"),
    P("(ii)", "Find using an easy method: (a) 52 &times; 98 (b) 36 &times; 25 (c) 4,000 &minus; 1,997", 3,
      f"(a) 52 &times; 100 &minus; 52 &times; 2 = 5200 &minus; 104 = <b>{ind(a1)}</b> &nbsp; (b) 36 &times; 100 &divide; 4 = 3600 &divide; 4 = <b>{a2}</b> &nbsp; (c) 4,000 &minus; 2,000 + 3 = <b>{ind(a3)}</b>")]))

f = lambda n: [s for s in range(1, 21) if n % s == 0]
pm = [k for k in range(2, 21) if len(f(k)) == 2]
assert f(12) == [1, 2, 3, 4, 6, 12] and len(f(16)) == 5 and f(9) == [1, 3, 9] and pm == [2, 3, 5, 7, 11, 13, 17, 19] and [k for k in range(1, 21) if k % 6 == 0] == [6, 12, 18]
I.append(Q("There are 20 lockers numbered 1 to 20. Student 1 touches every locker, Student 2 touches every 2nd locker (2, 4, 6, &hellip;), Student 3 touches every 3rd locker, and so on up to Student 20. (A student touches a locker if its number is a multiple of the student&rsquo;s number.)", 6,
           fig=bulbs(20, lambda i: "#ffffff", per=10), parts=[
    P("(i)", "(a) Which students touch locker 12? (b) How many students touch locker 16? (c) Which students touch locker 9?", 3,
      f"(a) <b>1, 2, 3, 4, 6, 12</b> (the factors of 12) &nbsp; (b) factors of 16 are 1, 2, 4, 8, 16, so <b>5</b> students &nbsp; (c) <b>1, 3, 9</b>"),
    P("(ii)", "(a) Which lockers are touched by exactly 2 students? (b) Which lockers does Student 6 touch? (c) Name the locker (up to 20) touched by both Student 4 and Student 6.", 3,
      f"(a) <b>{', '.join(map(str, pm))}</b> (prime numbers) &nbsp; (b) <b>6, 12, 18</b> &nbsp; (c) <b>12</b> (LCM of 4 and 6)")]))

assert math.isqrt(48) ** 2 != 48
I.append(Q("", 6, parts=[
    P("(i)", "Solve the riddles: (a) I am a multiple of both 6 and 8, and I am between 40 and 60. (b) I am a 2-digit number less than 40. The sum of my digits is 9 and their product is 18. (c) I am a square number between 50 and 80.", 3,
      "(a) <b>48</b> &nbsp; (b) <b>36</b> (3 + 6 = 9, 3 &times; 6 = 18; 63 is more than 40) &nbsp; (c) <b>64</b> (8 &times; 8)"),
    P("(ii)", "The floor of a room is covered by square tiles in 4 rows and 7 columns, as shown. (a) How many tiles are there? (b) Each tile has a side of 50 cm. Find the length and breadth of the floor in metres. (c) Find the area of the floor in sq m.", 3,
      "(a) 4 &times; 7 = <b>28</b> &nbsp; (b) length = 7 &times; 50 = 350 cm = <b>3.5 m</b>; breadth = 4 &times; 50 = 200 cm = <b>2 m</b> &nbsp; (c) 3.5 &times; 2 = <b>7 sq m</b>", fig=svg_grid(rect(4, 7), 20))]))
assert [k for k in range(40, 60) if k % 6 == 0 and k % 8 == 0] == [48] and [x for x in range(10, 40) if sum(map(int, str(x))) == 9 and (x // 10) * (x % 10) == 18] == [36] and [x for x in range(50, 80) if math.isqrt(x) ** 2 == x] == [64]
assert 7 * 50 == 350 and 4 * 50 == 200 and 3.5 * 2 == 7

I.append(Q("Fill in the blanks: (a) 7 km 250 m = ______ m &nbsp; (b) 2 days = ______ hours &nbsp; (c) 3 L 50 mL = ______ mL", 3, f"(a) {7*1000+250} &nbsp; (b) {2*24} &nbsp; (c) {3*1000+50}"))
I.append(Q("Write True or False: (a) 00:00 hours is midnight in the 24-hour clock. (b) 1 quintal is 10 kg. (c) The boiling point of water is 100&deg;C.", 3,
           "(a) True &nbsp; (b) False (1 quintal = 100 kg) &nbsp; (c) True"))
st = 6 * 60 + 50; en = st + 7 * 60 + 25; assert (en // 60, en % 60) == (14, 15)
I.append(Q("Ramesh started his work at 6:50 am and worked for 7 hours 25 minutes. At what time did he finish? Write the time in the 12-hour clock.", 3,
           "6:50 am + 7 h = 1:50 pm; 1:50 pm + 25 min = 2:15 pm.<br>He finished at <b>2:15 pm</b> (14:15)."))

names = ["Jaipur", "Ajmer", "Kota", "Bharatpur", "Alwar"]
dd = {("Jaipur", "Ajmer"): 130, ("Jaipur", "Kota"): 250, ("Jaipur", "Bharatpur"): 180, ("Jaipur", "Alwar"): 150, ("Ajmer", "Kota"): 200,
      ("Ajmer", "Bharatpur"): 310, ("Ajmer", "Alwar"): 280, ("Kota", "Bharatpur"): 330, ("Kota", "Alwar"): 400, ("Bharatpur", "Alwar"): 110}
def g(a, b): return dd[(a, b)] if (a, b) in dd else dd[(b, a)]
nl_ = min((x for x in names if x != "Alwar"), key=lambda x: g("Alwar", x)); fk = max((x for x in names if x != "Kota"), key=lambda x: g("Kota", x))
via = g("Alwar", "Bharatpur") + g("Bharatpur", "Jaipur"); assert (nl_, fk, via, via - g("Alwar", "Jaipur")) == ("Bharatpur", "Alwar", 290, 140)
I.append(Q("The table shows the road distance (in km) between some cities.", 8, fig=dist_table(names, dd), parts=[
    P("(a)", "A taxi goes from Jaipur to Ajmer and comes back to Jaipur. How many km does it run?", 2, f"2 &times; 130 = <b>{2*g('Jaipur','Ajmer')} km</b>"),
    P("(b)", "Which city is nearest to Alwar?", 2, f"<b>Bharatpur</b> ({g('Alwar','Bharatpur')} km)"),
    P("(c)", "Which city is farthest from Kota?", 2, f"<b>Alwar</b> ({g('Kota','Alwar')} km)"),
    P("(d)", "Going from Alwar to Jaipur through Bharatpur is how many km longer than the direct road?", 2, f"110 + 180 = {via} km; {via} &minus; 150 = <b>{via-150} km</b>")]))

I.append(mc("The product of two odd numbers is always", "an odd number", ["an even number", "a multiple of 4", "zero"], 0, why="e.g. 3 &times; 5 = 15, 7 &times; 9 = 63"))
rs_ = [rect(n, n + 1) for n in (1, 2, 3, 4)]; assert [len(s) for s in rs_] == [2, 6, 12, 20] and len(rect(6, 7)) == 42
I.append(mc("Tiles are arranged in rectangles as shown. How many tiles will be needed for Fig. 6?", 42, [30, 36, 49], 3, fig=pats(rs_), why="1&times;2, 2&times;3, 3&times;4, &hellip; &rarr; 6 &times; 7 = 42"))
vg = [("Mon", 4), ("Tue", 6), ("Wed", 3), ("Thu", 5)]
pic = tbl(["Day", "Vegetables sold (&#9679; = 10 kg)"], [[d, "&#9679; " * k] for d, k in vg])
assert 5 * 10 == 50 and 6 * 10 - 3 * 10 == 30
I.append(Q("A pictograph shows the vegetables sold in a shop. Each dot (&#9679;) stands for 10 kg.", 3, fig=pic, parts=[
    P("(a)", "How many kg of vegetables were sold on Thursday?", 1, "5 &times; 10 = 50 kg"),
    P("(b)", "On which day was the least sold?", 1, "Wednesday (3 baskets = 30 kg)"),
    P("(c)", "How many more kg were sold on Tuesday than on Wednesday?", 1, "60 &minus; 30 = 30 kg")]))
sq = [3]
for i in range(1, 6): sq.append(sq[-1] + i)
assert sq == [3, 4, 6, 9, 13, 18]; nx1 = sq[-1] + 6; nx2 = nx1 + 7; assert (nx1, nx2) == (24, 31)
I.append(Q("Look at the pattern: 3, 4, 6, 9, 13, 18, ___, ___. (a) Write the number added at each step. (b) Write the next two numbers. (c) Which number is added to get the 9th number from the 8th?", 3,
           f"(a) +1, +2, +3, +4, +5, &hellip; (the added number goes up by 1 each time) &nbsp; (b) 18 + 6 = {nx1}, 24 + 7 = {nx2} &nbsp; (c) the 8th number is 31, the 9th is 31 + 8 = 39, so <b>8</b> is added"))
assert nx2 + 8 == 39

finish(9, I)
