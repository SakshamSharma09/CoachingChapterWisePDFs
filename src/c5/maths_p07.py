from maths_h import *
import math
from decimal import Decimal as D

I = []
# Q1 perimeter on grid
cells = shape(["###.", "####", ".###"]); P1 = perim(cells); assert P1 == 14
I.append(mc("The side of each small square is 1 cm. The perimeter of the shaded figure is", f"{P1} cm", ["12 cm", "16 cm", "11 cm"], 0, fig=svg_grid(cells, 20)))

# Q2
def kind(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight" if d == 180 else "reflex"
assert [kind(90), kind(118), kind(305)] == ["right", "obtuse", "reflex"]
I.append(Q("", 6, parts=[
    P("(i)", "Name the type of each angle shown: (a) &ang;A (b) &ang;B (c) &ang;C", 3, "(a) right angle &nbsp; (b) obtuse angle (between 90&deg; and 180&deg;) &nbsp; (c) reflex angle (more than 180&deg;)", fig=angles([("A", 90), ("B", 118), ("C", 305)])),
    P("(ii)", "(a) The hour hand moves from 12 to 4. Through how many degrees does it turn? (b) What type of angle do the hands of a clock make at 9 o&rsquo;clock? (c) A half turn is how many degrees?", 3,
      f"(a) 4 &times; 30 = <b>{4*30}&deg;</b> &nbsp; (b) a right angle (90&deg;) &nbsp; (c) 180&deg;")]))

# Q3
S = {"cube": (6, 12, 8), "triangular pyramid": (4, 6, 4), "triangular prism": (5, 9, 6)}
for f, e, v in S.values(): assert f + v - e == 2
I.append(Q("", 6, parts=[
    P("(i)", "Name the solid shape: (a) a die used in Ludo (b) an ice-cream cone (c) a round tin of ghee", 3, "(a) cube &nbsp; (b) cone &nbsp; (c) cylinder"),
    P("(ii)", "(a) How many vertices does a cube have? (b) How many edges does a triangular pyramid have? (c) How many flat faces does a cylinder have?", 3,
      f"(a) {S['cube'][2]} &nbsp; (b) {S['triangular pyramid'][1]} &nbsp; (c) 2 (two circular faces; the third face is curved)")]))

# Q4 plan
top = [("Bedroom", 5), ("Drawing Room", 7)]; bot = [("Kitchen", 5), ("Dining", 7)]; h1, h2 = 4, 3
R = {"Bedroom": (5, 4), "Drawing Room": (7, 4), "Kitchen": (5, 3), "Dining": (7, 3)}; A = {k: w * h for k, (w, h) in R.items()}
assert sum(A.values()) == 12 * 7 == 84 and A["Drawing Room"] - A["Dining"] == 7
I.append(Q("Look at the plan of Raju&rsquo;s house in Bharatpur.", 8, fig=plan(12, top, bot, h1, h2), parts=[
    P("(a)", "Find the area of the Drawing Room.", 2, f"7 &times; 4 = {A['Drawing Room']} sq m"),
    P("(b)", "Which room is to the south of the Bedroom?", 2, "The Kitchen (the north arrow shows the top is north, so the room below is south)"),
    P("(c)", "How much larger is the Drawing Room than the Dining room?", 2, f"Dining = 7 &times; 3 = {A['Dining']} sq m; {A['Drawing Room']} &minus; {A['Dining']} = <b>7 sq m</b>"),
    P("(d)", "Find the total floor area of the house.", 2, f"Length 12 m, breadth 4 + 3 = 7 m; 12 &times; 7 = <b>{12*7} sq m</b> (check: 20 + 28 + 15 + 21 = {sum(A.values())})")]))

# Q5-7
n = 456300; assert intl(n) == "456,300" and ind(n) == "4,56,300"
I.append(mc("The number 4,56,300 written in the international system is", "456,300", ["4,56,300", "4,563,00", "45,63,00"], 1))
c = [209876, 290678, 209867, 298076]; sm = min(c); assert sm == 209867
I.append(mc("Which is the smallest number?", ind(sm), [ind(209876), ind(290678), ind(298076)], 2))
rd = round(76482 / 100) * 100; assert rd == 76500
I.append(mc("76,482 rounded off to the nearest hundred is", ind(rd), [ind(76000), ind(76400), ind(77000)], 3))

# Q8
a, b = D("2.35"), D("1.8"); tot = a + b; dif = a - b; cost = tot * 40; assert (tot, dif, cost) == (D("4.15"), D("0.55"), D("166.00"))
fig8 = nl(2, 3, 10, {"A": Fr(21, 10), "B": Fr(5, 2), "C": Fr(29, 10)}, {0: "2", 10: "3"})
I.append(Q("", 6, parts=[
    P("(i)", "Anita bought 2.35 m of red cloth and 1.8 m of green cloth. (a) How much cloth did she buy in all? (b) How much more red cloth than green? (c) If the cloth costs &#8377; 40 per metre, what is the total cost?", 3,
      f"(a) 2.35 + 1.80 = <b>{tot} m</b> &nbsp; (b) 2.35 &minus; 1.80 = <b>{dif} m</b> &nbsp; (c) 4.15 &times; 40 = <b>&#8377; {cost:.0f}</b>"),
    P("(ii)", "The line from 2 to 3 is divided into 10 equal parts. Write the decimal number shown by A, B and C.", 3, "A = 2.1 &nbsp; B = 2.5 &nbsp; C = 2.9", fig=fig8)]))

# Q9
est = round(4986, -3) + round(3012, -3); assert est == 8000
I.append(mc("The estimated sum of 4,986 and 3,012 (rounding each number to the nearest thousand) is", ind(est), [ind(7000), ind(9000), ind(8100)], 0))

# Q10
sug, dal = 3 * 44, 2 * 126; pay = 500; ch = pay - sug - dal; assert (sug, dal, ch) == (132, 252, 116)
I.append(Q(f"Kailash bought 3 kg sugar at &#8377; 44 per kg and 2 kg dal at &#8377; 126 per kg. He gave a &#8377; 500 note to the shopkeeper. How much money did he get back?", 3,
           f"Sugar = 3 &times; 44 = {rs(sug)}; dal = 2 &times; 126 = {rs(dal)}<br>Total = {sug} + {dal} = {rs(sug+dal)}<br>Balance = 500 &minus; {sug+dal} = <b>{rs(ch)}</b>"))

# Q11
q, r = divmod(8205, 9); assert (q, r) == (911, 6) and 9 * q + r == 8205
I.append(Q("Divide 8,205 by 9. Write the quotient and the remainder. Then verify your answer.", 3,
           f"Quotient = <b>{q}</b>, remainder = <b>{r}</b>.<br>Verification: 9 &times; {q} + {r} = {9*q} + {r} = {9*q+r} = dividend. &#10003;"))

# Q12
fund = 38 * 125 + 3 * 200; exp = 4500; left = fund - exp; assert (38 * 125, fund, left) == (4750, 5350, 850)
e1, e2, e3 = round(4872, -3) + round(2139, -3), round(9096, -3) - round(3985, -3), 60 * 40
assert (e1, e2, e3) == (7000, 5000, 2400) and (4872 + 2139, 9096 - 3985, 59 * 41) == (7011, 5111, 2419)
I.append(Q("", 6, parts=[
    P("(i)", "For a school picnic, 38 students paid &#8377; 125 each and 3 teachers paid &#8377; 200 each. (a) How much money was collected? (b) The bus and meals cost &#8377; 4,500. How much money is left?", 3,
      f"(a) 38 &times; 125 = {rs(38*125)}; 3 &times; 200 = {rs(600)}; total = <b>{rs(fund)}</b> &nbsp; (b) {fund} &minus; {exp} = <b>{rs(left)}</b>"),
    P("(ii)", "Estimate by rounding (thousands for (a), (b); tens for (c)): (a) 4,872 + 2,139 (b) 9,096 &minus; 3,985 (c) 59 &times; 41", 3,
      f"(a) 5,000 + 2,000 = <b>{ind(e1)}</b> (exact 7,011) &nbsp; (b) 9,000 &minus; 4,000 = <b>{ind(e2)}</b> (exact 5,111) &nbsp; (c) 60 &times; 40 = <b>{ind(e3)}</b> (exact 2,419)")]))

# Q13 bulbs 1-30
def col(i): return "#9be3a8" if i % 10 == 0 else "#ffe27a" if i % 5 == 0 else "#ffffff"
la = [i for i in range(1, 31) if i % 5 == 0]; lb = [i for i in range(1, 31) if i % 10 == 0]; fa = [i for i in range(1, 31) if 30 % i == 0]
cf = [i for i in range(1, 31) if 20 % i == 0 and 30 % i == 0]; assert (len(la), len(lb), fa, cf, math.gcd(20, 30)) == (6, 3, [1, 2, 3, 5, 6, 10, 15, 30], [1, 2, 5, 10], 10)
I.append(Q("Bulbs numbered 1 to 30 are fixed in a hall. Switch A lights every 5th bulb (5, 10, 15, &hellip;) and Switch B lights every 10th bulb (10, 20, 30). Yellow = lit by A only, green = lit by A and B both.", 6,
           fig=bulbs(30, col, per=15, r=10), parts=[
    P("(i)", "(a) How many bulbs does Switch A light? (b) How many bulbs does Switch B light? (c) Every bulb lit by B is also lit by A. Why?", 3,
      f"(a) <b>{len(la)}</b> (5, 10, 15, 20, 25, 30) &nbsp; (b) <b>{len(lb)}</b> (10, 20, 30) &nbsp; (c) every multiple of 10 is also a multiple of 5"),
    P("(ii)", "(a) Write all the factors of 30. (b) Write the common factors of 20 and 30. (c) Find the HCF of 20 and 30.", 3,
      f"(a) {', '.join(map(str, fa))} &nbsp; (b) {', '.join(map(str, cf))} &nbsp; (c) <b>10</b>")]))

# Q14 number pyramid
rows = [[6, 9, 5, 8]]
while len(rows[-1]) > 1: rows.append([x + y for x, y in zip(rows[-1], rows[-1][1:])])
assert rows == [[6, 9, 5, 8], [15, 14, 13], [29, 27], [56]]
def brick(x, lab=None): return f"<span style='display:inline-block;width:36px;border:1px solid #13286b;background:#f7f9fd;margin:1px;text-align:center'>{lab or x}</span>"
shown = [[brick(0, "56")], [brick(29), brick(27)], [brick(15), brick(0, "<b>A</b>"), brick(13)], [brick(6), brick(0, "<b>B</b>"), brick(5), brick(0, "<b>C</b>")]]
pyr = "<div style='text-align:center;width:200px'>" + "".join(f"<div>{''.join(r)}</div>" for r in shown) + "</div>"
A_, B_, C_ = 29 - 15, 15 - 6, 13 - 5; assert (A_, B_, C_) == (14, 9, 8) == (rows[1][1], rows[0][1], rows[0][3])
I.append(Q("", 6, parts=[
    P("(i)", "In the number pyramid each brick is the sum of the two bricks just below it. Find the numbers A, B and C.", 3,
      f"B: 6 + B = 15, so B = <b>{B_}</b>. A: 15 + A = 29, so A = <b>{A_}</b>. C: 5 + C = 13, so C = <b>{C_}</b>.", fig=pyr),
    P("(ii)", "A floor 8 m long and 6 m wide is covered with square tiles of side 2 m. (a) How many tiles are in one row? (b) How many rows are there? (c) How many tiles are used in all?", 3,
      f"(a) 8 &divide; 2 = <b>{8//2}</b> &nbsp; (b) 6 &divide; 2 = <b>{6//2}</b> &nbsp; (c) 4 &times; 3 = <b>{(8//2)*(6//2)}</b> (check: area 48 &divide; 4 = 12)")]))

# Q15-17
a1, a2, a3 = 4 * 100 + 35, int(2.5 * 1000), (2 * 60 + 15); assert (a1, a2, a3) == (435, 2500, 135)
I.append(Q("Fill in the blanks: (a) 4 m 35 cm = ______ cm &nbsp; (b) 2.5 litres = ______ mL &nbsp; (c) 135 minutes = ______ hours ______ minutes", 3, f"(a) {a1} &nbsp; (b) {a2} &nbsp; (c) 2 hours 15 minutes"))
assert 10 + 12 == 22 and 8 + 12 == 20
I.append(Q("Write True or False: (a) 10:15 pm is written as 22:15 in the 24-hour clock. (b) 8:30 am is written as 20:30 in the 24-hour clock. (c) Water freezes at 0&deg;C.", 3,
           "(a) True &nbsp; (b) False (8:30 am = 08:30) &nbsp; (c) True"))
o, c_ = 8 * 60 + 30, 19 * 60 + 15; du = c_ - o; assert (du // 60, du % 60) == (10, 45)
I.append(Q("A shop in Alwar opens at 8:30 am and closes at 7:15 pm. For how many hours and minutes is the shop open?", 3,
           f"7:15 pm = 19:15. 19:15 &minus; 8:30 = {du//60} h {du%60} min. (8:30 to 18:30 is 10 h, and 18:30 to 19:15 is 45 min.)<br>Answer: <b>10 hours 45 minutes</b>"))

# Q18 distance table
names = ["Jaipur", "Bikaner", "Jodhpur", "Udaipur", "Kota"]
dd = {("Jaipur", "Bikaner"): 330, ("Jaipur", "Jodhpur"): 340, ("Jaipur", "Udaipur"): 400, ("Jaipur", "Kota"): 250, ("Bikaner", "Jodhpur"): 250,
      ("Bikaner", "Udaipur"): 600, ("Bikaner", "Kota"): 560, ("Jodhpur", "Udaipur"): 250, ("Jodhpur", "Kota"): 480, ("Udaipur", "Kota"): 270}
def g(a, b): return dd[(a, b)] if (a, b) in dd else dd[(b, a)]
nb = min((x for x in names if x != "Bikaner"), key=lambda x: g("Bikaner", x)); assert nb == "Jodhpur"
via = g("Jaipur", "Udaipur") + g("Udaipur", "Jodhpur"); assert via == 650 and via - g("Jaipur", "Jodhpur") == 310 and 2 * g("Kota", "Udaipur") == 540
I.append(Q("The table gives the distance (in km) by road between some cities of Rajasthan.", 8, fig=dist_table(names, dd), parts=[
    P("(a)", "What is the distance between Jaipur and Jodhpur?", 2, f"<b>{g('Jaipur','Jodhpur')} km</b>"),
    P("(b)", "Which city is nearest to Bikaner among the cities given?", 2, f"<b>Jodhpur</b> ({g('Bikaner','Jodhpur')} km; Jaipur is {g('Bikaner','Jaipur')} km)"),
    P("(c)", "Sonu goes from Jaipur to Jodhpur through Udaipur. How many km more is this than the direct road?", 2, f"400 + 250 = {via} km; {via} &minus; 340 = <b>{via-340} km</b> more"),
    P("(d)", "A taxi goes from Kota to Udaipur and returns to Kota. How far does it travel?", 2, f"2 &times; 270 = <b>{2*g('Kota','Udaipur')} km</b>")]))

# Q19-22
pr = 47
isp = lambda n: n > 1 and all(n % k for k in range(2, math.isqrt(n) + 1)); assert isp(47) and not any(isp(x) for x in (51, 57, 91))
I.append(mc("Which of these is a prime number?", pr, [51, 57, 91], 2))
cr = [cross(i) for i in (0, 1, 2)]; assert [len(s) for s in cr] == [1, 5, 9] and len(cross(5)) == 21
I.append(mc("A plus-shaped design is made with squares as shown. How many squares will be needed for Fig. 6?", 21, [17, 24, 25], 3, fig=pats(cr), why="1, 5, 9, 13, 17, 21 (add 4 each time)"))
fr = [("Mango", 17), ("Apple", 13), ("Banana", 9), ("Orange", 11)]
tb = tbl(["Fruit", "Tally marks"], [[f, tally(v)] for f, v in fr])
assert sum(v for _, v in fr) == 50 and 17 - 9 == 8
I.append(Q("Students of Class 5 were asked to choose their favourite fruit. The tally marks are shown (each crossed group stands for 5).", 3, fig=tb, parts=[
    P("(a)", "How many students chose Apple?", 1, "13"),
    P("(b)", "Which fruit is the least liked? How many students chose it?", 1, "Banana, 9"),
    P("(c)", "How many students were asked in all?", 1, "17 + 13 + 9 + 11 = 50")]))
ls = [(1, 2), (12, 3), (123, 4), (1234, 5), (12345, 6)]
res = [a * 9 + b for a, b in ls]; assert res == [11, 111, 1111, 11111, 111111]
I.append(Q("Observe the pattern: &nbsp; 1 &times; 9 + 2 = 11 &nbsp;|&nbsp; 12 &times; 9 + 3 = 111 &nbsp;|&nbsp; 123 &times; 9 + 4 = 1111. &nbsp; (a) Write the next line of the pattern. (b) What is its answer? (c) Write the line that gives 111111.", 3,
           f"(a) 1234 &times; 9 + 5 &nbsp; (b) {res[3]} &nbsp; (c) 12345 &times; 9 + 6 = {res[4]}"))

finish(7, I)
