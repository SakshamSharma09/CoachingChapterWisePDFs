from maths_h import *
import math

I = []
cells = shape(["###.##", "######", ".#####", "..###."]); A1 = len(cells); assert A1 == 19
I.append(mc("Each square of the figure is of area 1 square cm. The area of the shaded figure is", f"{A1} sq cm", ["17 sq cm", "18 sq cm", "21 sq cm"], 2, fig=svg_grid(cells, 18)))

def kind(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight" if d == 180 else "reflex"
assert [kind(62), kind(91), kind(330)] == ["acute", "obtuse", "reflex"]
I.append(Q("", 6, parts=[
    P("(i)", "Name the type of each angle: (a) &ang;K (b) &ang;L (c) &ang;M", 3, "(a) acute &nbsp; (b) obtuse (91&deg; is a little more than a right angle) &nbsp; (c) reflex", fig=angles([("K", 62), ("L", 91), ("M", 330)])),
    P("(ii)", "(a) Through how many degrees does the minute hand turn from 12 to 9? (b) What type of angle is that? (c) How many right angles make a half turn?", 3,
      f"(a) 9 &times; 30 = <b>{9*30}&deg;</b> &nbsp; (b) <b>{kind(270)}</b> angle (more than 180&deg;) &nbsp; (c) 180 &divide; 90 = <b>{180//90}</b>")]))

I.append(Q("", 6, parts=[
    P("(i)", "Name the flat shape of the face: (a) a face of a cube (b) the base of a cone (c) a face of a triangular pyramid", 3, "(a) square &nbsp; (b) circle &nbsp; (c) triangle"),
    P("(ii)", "Name the solid: (a) it has 2 flat circular faces and 1 curved face (b) it has 6 rectangular faces (c) it has one vertex and a circular base", 3, "(a) cylinder &nbsp; (b) cuboid &nbsp; (c) cone")]))

top = [("Hall", 8), ("Study", 4)]; bot = [("Dining", 8), ("Store", 4)]; h1, h2 = 6, 3
R = {"Hall": (8, 6), "Study": (4, 6), "Dining": (8, 3), "Store": (4, 3)}; A = {k: w * h for k, (w, h) in R.items()}
ps = 2 * sum(R["Study"]); tot = 12 * 9; assert (A["Hall"], A["Store"], ps, tot, sum(A.values())) == (48, 12, 20, 108, 108)
I.append(Q("The plan of a house in Bikaner is shown. The north direction is marked.", 8, fig=plan(12, top, bot, h1, h2), parts=[
    P("(a)", "Find the area of the Hall.", 2, f"8 &times; 6 = <b>{A['Hall']} sq m</b>"),
    P("(b)", "Which room is to the south of the Study? What is its area?", 2, f"The <b>Store</b>; area = 4 &times; 3 = <b>{A['Store']} sq m</b>"),
    P("(c)", "Find the perimeter of the Study.", 2, f"2 &times; (4 + 6) = <b>{ps} m</b>"),
    P("(d)", "Find the area of the whole house.", 2, f"Length 12 m, breadth 6 + 3 = 9 m; area = 12 &times; 9 = <b>{tot} sq m</b>")]))

assert str(724983)[0] == "7"
I.append(mc("In 7,24,983, the digit in the lakhs place is", 7, [2, 4, 9], 1))
rd = round(348562, -3); assert rd == 349000
I.append(mc("3,48,562 rounded off to the nearest thousand is", ind(rd), [ind(348000), ind(350000), ind(348500)], 0))
pre = 500000 - 1; assert ind(pre) == "4,99,999"
I.append(mc("The number that comes just before 5,00,000 is", ind(pre), [ind(499000), ind(400000), ind(499990)], 2))

wk = Fr(3, 8) + Fr(1, 4); rem = 1 - wk; m = rem * 1000; assert (wk, rem, m) == (Fr(5, 8), Fr(3, 8), 375)
fig8 = nl(Fr(3, 10), Fr(4, 10), 10, {"A": Fr(32, 100), "B": Fr(35, 100), "C": Fr(39, 100)}, {0: "0.3", 10: "0.4"})
I.append(Q("", 6, parts=[
    P("(i)", "Rakesh lives 1 km from the bus stand. He walked 3/8 km and then took a rickshaw for 1/4 km. (a) What distance has he covered in all? (b) What part of the km is left? (c) How many metres is that?", 3,
      f"(a) 3/8 + 1/4 = 3/8 + 2/8 = <b>5/8 km</b> &nbsp; (b) 1 &minus; 5/8 = <b>3/8 km</b> &nbsp; (c) 3/8 of 1000 = <b>{m} m</b>"),
    P("(ii)", "The line from 0.3 to 0.4 is divided into 10 equal parts. Write the decimal number shown by A, B and C.", 3, "A = 0.32 &nbsp; B = 0.35 &nbsp; C = 0.39", fig=fig8)]))

x9 = 10000 - 4567; assert x9 == 5433
I.append(mc("What should be added to 4,567 to get 10,000?", ind(x9), [ind(5443), ind(6433), ind(5533)], 1))

tank, per, fam = 3600, 12, 150; day = per * fam; days = tank // day; assert (day, days) == (1800, 2) and tank % day == 0
I.append(Q("A water tanker brings 3,600 litres of water to a village in Jaisalmer. Each of 150 families gets 12 litres of water every day. For how many days will the water last?", 3,
           f"Water needed in one day = 150 &times; 12 = {day} L<br>Days = 3,600 &divide; {day} = <b>{days} days</b>"))
q, r = divmod(7305, 8); assert (q, r) == (913, 1) and 8 * q + r == 7305
I.append(Q("Divide 7,305 by 8. Find the quotient and the remainder. Verify the result.", 3,
           f"Quotient = <b>{q}</b>, remainder = <b>{r}</b>.<br>Verification: 8 &times; {q} + {r} = {8*q} + {r} = {8*q+r}. &#10003;"))

dy, sw, cr = 12 * 35, 3 * 240, 365; tt = dy + sw + cr; ch = 2000 - tt; assert (dy, sw, tt, ch) == (420, 720, 1505, 495)
v1, v2, v3 = 36 * 11, 4 * 17 * 25, 125 * 16; assert (v1, v2, v3) == (396, 1700, 2000)
I.append(Q("", 6, parts=[
    P("(i)", "Before Diwali, Mohan bought 12 packets of diyas at &#8377; 35 per packet, 3 boxes of sweets at &#8377; 240 per box and crackers worth &#8377; 365. (a) Find the total bill. (b) How much change did he get from &#8377; 2,000?", 3,
      f"(a) diyas {rs(dy)} + sweets {rs(sw)} + crackers {rs(cr)} = <b>{rs(tt)}</b> &nbsp; (b) 2,000 &minus; {tt} = <b>{rs(ch)}</b>"),
    P("(ii)", "Find by a quick method: (a) 36 &times; 11 (b) 4 &times; 17 &times; 25 (c) 125 &times; 16", 3,
      f"(a) 36 &times; 10 + 36 = 360 + 36 = <b>{v1}</b> &nbsp; (b) (4 &times; 25) &times; 17 = 100 &times; 17 = <b>{ind(v2)}</b> &nbsp; (c) 125 &times; 8 = 1000, so 125 &times; 16 = <b>{ind(v3)}</b>")]))

def col(i): return "#9be3a8" if i % 40 == 0 else "#ffe27a" if i % 8 == 0 else "#9fd3ff" if i % 10 == 0 else "#ffffff"
la = [i for i in range(1, 41) if i % 8 == 0]; lb = [i for i in range(1, 41) if i % 10 == 0]; bo = [i for i in la if i in lb]
l3 = math.lcm(10, 15, 20); h3 = math.gcd(16, 40); assert (la, lb, bo, l3, h3) == ([8, 16, 24, 32, 40], [10, 20, 30, 40], [40], 60, 8)
I.append(Q("Bulbs numbered 1 to 40 are fixed in a row. Switch A lights every 8th bulb and Switch B lights every 10th bulb. Yellow = A only, blue = B only, green = both.", 6,
           fig=bulbs(40, col, per=20, r=10), parts=[
    P("(i)", "(a) Write the numbers of the bulbs lit by Switch A. (b) Write the numbers of the bulbs lit by Switch B. (c) Which bulb is lit by both? Which number (LCM) does it match?", 3,
      f"(a) <b>{', '.join(map(str, la))}</b> &nbsp; (b) <b>{', '.join(map(str, lb))}</b> &nbsp; (c) bulb <b>40</b>, the LCM of 8 and 10"),
    P("(ii)", "(a) Find the LCM of 10 and 15. (b) Three bells ring every 10, 15 and 20 minutes. They ring together at 6:00 pm. At what time will they ring together again? (c) Find the HCF of 16 and 40.", 3,
      f"(a) <b>{math.lcm(10,15)}</b> &nbsp; (b) LCM of 10, 15, 20 = {l3} min, so at <b>7:00 pm</b> &nbsp; (c) <b>{h3}</b>")]))

G = [[7, 2, 9], [4, 6, 8], [5, 3, 1]]
fl = [x for r in G for x in r]; m3 = [x for x in fl if x % 3 == 0]; r2 = sum(G[1]); df = max(fl) - min(fl); assert (m3, r2, df) == ([9, 6, 3], 18, 8)
gt = "<table class='t5' style='font-size:1.1em'>" + "".join("<tr>" + "".join(f"<td style='width:30px'>{c}</td>" for c in r) + "</tr>" for r in G) + "</table>"
pairs = [(w, 36 // w) for w in range(1, 37) if 36 % w == 0 and w <= 36 // w]; assert len(pairs) == 5 and (6, 6) in pairs and 2 * (4 + 9) == 26
I.append(Q("", 6, parts=[
    P("(i)", "Look at the number grid. (a) Write the numbers that are multiples of 3. (b) Find the sum of the numbers in the middle row. (c) Find the difference between the biggest and the smallest number in the grid.", 3,
      f"(a) <b>{', '.join(map(str, m3))}</b> &nbsp; (b) 4 + 6 + 8 = <b>{r2}</b> &nbsp; (c) 9 &minus; 1 = <b>{df}</b>", fig=gt),
    P("(ii)", "36 square tiles are arranged in a rectangle using all the tiles. One such arrangement (4 rows and 9 columns) is shown. (a) In how many different ways can the 36 tiles be arranged? (b) Which arrangement makes a square? (c) Find the perimeter of the arrangement shown (each tile has a side of 1 m).", 3,
      f"Pairs: 1&times;36, 2&times;18, 3&times;12, 4&times;9, 6&times;6. (a) <b>{len(pairs)}</b> &nbsp; (b) <b>6 &times; 6</b> &nbsp; (c) 2 &times; (9 + 4) = <b>26 m</b>", fig=svg_grid(rect(4, 9), 16))]))

y1, y2, y3 = 6 * 1000 + 5, 2500, 5 * 60 + 20; assert (y1, y2, y3) == (6005, 2500, 320)
I.append(Q("Fill in the blanks: (a) 6 km 5 m = ______ m &nbsp; (b) 2 kg 500 g = ______ g &nbsp; (c) 5 hours 20 minutes = ______ minutes", 3, f"(a) {y1} &nbsp; (b) {y2} &nbsp; (c) {y3}"))
assert 7 + 12 == 19
I.append(Q("Write True or False: (a) 7:05 pm is written as 19:05 in the 24-hour clock. (b) &#8377; 6.50 is the same as 65 paise. (c) A temperature of 45&deg;C is a cold winter day in Jaipur.", 3,
           "(a) True &nbsp; (b) False (&#8377; 6.50 = 650 paise) &nbsp; (c) False (45&deg;C is very hot)"))
sold = 2750 + 3480; lf = 10000 - sold; assert (sold, lf) == (6230, 3770)
I.append(Q("A shopkeeper in Jaisalmer had 10 kg of dates. He sold 2 kg 750 g in the morning and 3 kg 480 g in the evening. How much is left?", 3,
           f"Sold = 2750 g + 3480 g = {sold} g = 6 kg 230 g<br>Left = 10,000 &minus; {sold} = {lf} g = <b>3 kg 770 g</b>"))

nodes = {"Bikaner": (40, 40, "a"), "Nagaur": (170, 28, "a"), "Jodhpur": (270, 85, "a"), "Jaisalmer": (40, 160, "b"), "Barmer": (200, 160, "b")}
edges = [("Bikaner", "Nagaur", 110), ("Nagaur", "Jodhpur", 135), ("Bikaner", "Jodhpur", 250), ("Jodhpur", "Jaisalmer", 285), ("Jaisalmer", "Barmer", 160), ("Jodhpur", "Barmer", 215), ("Bikaner", "Jaisalmer", 330)]
D_ = {(a, b): k for a, b, k in edges}
via = 110 + 135; v2 = 160 + 215; assert (via, 250 - via, v2, v2 - 285, 2 * 330) == (245, 5, 375, 90, 660)
I.append(Q("The road map shows some cities of western Rajasthan with the distances in km.", 8, fig=route(nodes, edges), parts=[
    P("(a)", "Which is shorter for going from Bikaner to Jodhpur: the direct road or the road through Nagaur? By how much?", 2, f"Through Nagaur: 110 + 135 = {via} km; direct = 250 km. Through <b>Nagaur</b> is shorter by <b>{250-via} km</b>."),
    P("(b)", "How many km more is it to go from Jaisalmer to Jodhpur through Barmer than by the direct road?", 2, f"160 + 215 = {v2} km; {v2} &minus; 285 = <b>{v2-285} km</b>"),
    P("(c)", "Which city is the nearest to Jodhpur on this map? Write the distance.", 2, "<b>Nagaur</b>, 135 km (Barmer is 215 km)"),
    P("(d)", "A bus goes from Bikaner to Jaisalmer and comes back by the same road. How many km does it travel?", 2, f"2 &times; 330 = <b>{2*330} km</b>")]))

assert 36 % 2 == 0 and math.isqrt(36) ** 2 == 36 and all(x % 2 and math.isqrt(x) ** 2 == x for x in (25, 49, 81))
I.append(mc("Which of these numbers is both an even number and a square number?", 36, [25, 49, 81], 3))
ls = [ell(n) for n in (1, 2, 3, 4)]; assert [len(s) for s in ls] == [1, 3, 5, 7] and len(ell(8)) == 15
I.append(mc("Squares are arranged in L-shapes as shown. How many squares are needed for Fig. 8?", 15, [13, 16, 17], 0, fig=pats(ls), why="1, 3, 5, 7, &hellip; (add 2 each time); Fig. 8 = 2 &times; 8 &minus; 1"))
bk = [("Mon", 18), ("Tue", 24), ("Wed", 12), ("Thu", 30), ("Fri", 21)]
assert max(bk, key=lambda x: x[1])[0] == "Thu" and sum(v for _, v in bk) == 105 and 24 - 12 == 12
I.append(Q("The bar graph shows the number of books issued from a school library on 5 days.", 3, fig=bars([a for a, _ in bk], [b for _, b in bk], 6, 30, ylab="Books issued", xlab="Days"), parts=[
    P("(a)", "On which day were the most books issued?", 1, "Thursday (30 books)"),
    P("(b)", "How many more books were issued on Tuesday than on Wednesday?", 1, "24 &minus; 12 = 12"),
    P("(c)", "How many books were issued in the 5 days together?", 1, "18 + 24 + 12 + 30 + 21 = 105")]))
fb = [1, 1]
while len(fb) < 10: fb.append(fb[-1] + fb[-2])
assert fb[:8] == [1, 1, 2, 3, 5, 8, 13, 21] and fb[9] == 55
I.append(Q("Look at the pattern: 1, 1, 2, 3, 5, 8, ___, ___. (a) What is the rule of the pattern? (b) Write the next two numbers. (c) What is the 10th number?", 3,
           f"(a) each number is the sum of the two numbers before it &nbsp; (b) 5 + 8 = {fb[6]}, 8 + 13 = {fb[7]} &nbsp; (c) 13 + 21 = 34, 21 + 34 = 55 &rarr; <b>{fb[9]}</b>"))

finish(10, I)
