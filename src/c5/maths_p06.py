from maths_h import *
import math

I = []
# ---- Q1 area by counting squares
cells = shape(["##....", "####..", "######", ".#####"]); A = len(cells); assert A == 17
I.append(mc("Each small square of the figure is 1 square cm. What is the area of the shaded figure?", f"{A} sq cm", ["15 sq cm", "18 sq cm", "20 sq cm"], 2,
            fig=svg_grid(cells, 18)))

# ---- Q2 angles
fig2 = angles([("P", 52), ("Q", 180), ("R", 250)])
def kind(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight" if d == 180 else "reflex"
assert [kind(52), kind(180), kind(250)] == ["acute", "straight", "reflex"]
hr = 3 * 30; assert hr == 90
I.append(Q("", 6, parts=[
    P("(i)", "Look at the three angles drawn. Write the type of each angle (acute / right / obtuse / straight / reflex): (a) &ang;P (b) &ang;Q (c) &ang;R", 3,
      f"(a) {kind(52)} (less than 90&deg;) &nbsp; (b) {kind(180)} angle &nbsp; (c) {kind(250)} (more than 180&deg;)", fig=fig2),
    P("(ii)", "(a) The minute hand of a clock moves from 12 to 3. Through how many degrees does it turn? (b) What is the angle between the hands of a clock at 6 o&rsquo;clock? Name its type. (c) How many right angles make one complete turn?", 3,
      f"(a) {hr}&deg; (a right angle) &nbsp; (b) 180&deg;, a straight angle &nbsp; (c) 360 &divide; 90 = {360//90}")]))

# ---- Q3 solids
S = {"cuboid": (6, 12, 8), "triangular prism": (5, 9, 6), "square pyramid": (5, 8, 5)}
for k, (f, e, v) in S.items(): assert f + v - e == 2
I.append(Q("", 6, parts=[
    P("(i)", "Write the number asked: (a) edges of a cuboid (b) faces of a triangular prism (c) vertices (corners) of a square pyramid", 3,
      f"(a) {S['cuboid'][1]} &nbsp; (b) {S['triangular prism'][0]} &nbsp; (c) {S['square pyramid'][2]}"),
    P("(ii)", "Name the solid that each net folds into: (a) a net made of 6 equal squares (b) a net made of one circle and one sector (a slice of a circle) (c) a net made of two circles and one rectangle", 3,
      "(a) cube &nbsp; (b) cone &nbsp; (c) cylinder")]))

# ---- Q4 floor plan
top = [("Hall", 6), ("Kitchen", 4)]; bot = [("Bedroom", 6), ("Store", 4)]; h1, h2, vh = 5, 3, 2
rooms = {"Hall": (6, 5), "Kitchen": (4, 5), "Bedroom": (6, 3), "Store": (4, 3), "Verandah": (10, 2)}
ar = {k: w * h for k, (w, h) in rooms.items()}
small = min((k for k in rooms if k != "Verandah"), key=lambda k: ar[k]); assert small == "Store" and ar[small] == 12
pbed = 2 * sum(rooms["Bedroom"]); assert pbed == 18
cost = ar["Verandah"] * 150; assert cost == 3000
I.append(Q("The plan of a house in Sikar is given below (not to scale; the north direction is shown).", 8, fig=plan(10, top, bot, h1, h2, ("Verandah", vh)), parts=[
    P("(a)", "What is the area of the Hall?", 2, f"6 &times; 5 = {ar['Hall']} sq m"),
    P("(b)", "Which room has the smallest area? Write its area.", 2, f"Store: 4 &times; 3 = {ar['Store']} sq m (Kitchen {ar['Kitchen']}, Bedroom {ar['Bedroom']}, Hall {ar['Hall']})"),
    P("(c)", "Find the perimeter of the Bedroom.", 2, f"2 &times; (6 + 3) = {pbed} m"),
    P("(d)", "The Verandah is to be tiled at &#8377; 150 per sq m. Find the cost.", 2, f"Area = 10 &times; 2 = {ar['Verandah']} sq m; cost = 20 &times; 150 = {rs(cost)}")]))

# ---- Q5-Q7
n5 = 407285; pv = int(str(n5)[-4]) * 1000; assert pv == 7000
I.append(mc("In the number 4,07,285 the value of the digit 7 is", 7000, [70, 700, 70000], 1))
dg = [3, 0, 8, 5, 1, 9]; big = int("".join(map(str, sorted(dg, reverse=True)))); assert big == 985310
I.append(mc("The greatest 6-digit number that can be made from the digits 3, 0, 8, 5, 1, 9 (each used once) is", ind(big), [ind(980531), ind(985130), ind(983510)], 0))
x7 = 300000 + 40000 + 500 + 6; assert x7 == 340506
I.append(mc("300000 + 40000 + 500 + 6 is the expanded form of", ind(x7), [ind(34506), ind(304506), ind(340056)], 3))

# ---- Q8
a, b = Fr(3, 10), Fr(2, 5); done = a + b; left = 1 - done; assert (done, left) == (Fr(7, 10), Fr(3, 10)); lit = left * 1000; assert lit == 300
fig8 = nl(0, 1, 8, {"A": Fr(1, 8), "B": Fr(1, 2), "C": Fr(7, 8)}, {0: "0", 8: "1"})
I.append(Q("", 6, parts=[
    P("(i)", "A water tank holds 1000 litres. On Monday 3/10 of it was filled and on Tuesday 2/5 of it was filled. (a) What fraction of the tank is filled in two days? (b) What fraction is still empty? (c) How many litres is that?", 3,
      f"(a) 3/10 + 2/5 = 3/10 + 4/10 = <b>7/10</b> &nbsp; (b) 1 &minus; 7/10 = <b>3/10</b> &nbsp; (c) 3/10 of 1000 = <b>{lit} litres</b>"),
    P("(ii)", "The number line from 0 to 1 is divided into 8 equal parts. Write the fraction shown by A, B and C.", 3,
      "A = 1/8 &nbsp; B = 4/8 = 1/2 &nbsp; C = 7/8", fig=fig8)]))

# ---- Q9
p9 = 405 * 12; assert p9 == 4860
I.append(mc("The product of 405 and 12 is", ind(p9), [ind(4050), ind(4560), ind(5860)], 2))

# ---- Q10
cans, cap, sold = 24, 15, 280; tot = cans * cap; rem = tot - sold; pk = rem // 2; assert (tot, rem, pk) == (360, 80, 40) and rem % 2 == 0
I.append(Q(f"A dairy in Jaipur filled {cans} cans with {cap} litres of milk in each can. In the morning {sold} litres were sold. The remaining milk was packed in 2-litre packets. How many packets were made?", 3,
           f"Total milk = {cans} &times; {cap} = {tot} L<br>Remaining = {tot} &minus; {sold} = {rem} L<br>Packets = {rem} &divide; 2 = <b>{pk}</b>"))

# ---- Q11
q, r = divmod(5843, 7); assert (q, r) == (834, 5) and 7 * q + r == 5843
I.append(Q("Divide 5,843 by 7. Write the quotient and the remainder and check your answer.", 3,
           f"Quotient = <b>{q}</b>, remainder = <b>{r}</b>.<br>Check: divisor &times; quotient + remainder = 7 &times; {q} + {r} = {7*q} + {r} = {7*q+r}, which is the dividend. &#10003;"))

# ---- Q12
wk = 450 + 280 + 620 + 350; mo = wk * 4; inc = 9500; sav = inc - mo; assert (wk, mo, sav) == (1700, 6800, 2700)
v1 = 73 * 99; v2 = 46 * 25; v3 = 8 * 125; assert (v1, v2, v3) == (7227, 1150, 1000)
I.append(Q("", 6, parts=[
    P("(i)", "The Sharma family spends in one week: vegetables &#8377; 450, milk &#8377; 280, grains &#8377; 620 and other things &#8377; 350. (a) What is the weekly expense? (b) What is the expense in 4 weeks? (c) If the monthly income is &#8377; 9,500, how much is saved?", 3,
      f"(a) 450 + 280 + 620 + 350 = {rs(wk)} &nbsp; (b) 1,700 &times; 4 = {rs(mo)} &nbsp; (c) 9,500 &minus; 6,800 = {rs(sav)}"),
    P("(ii)", "Use a short method: (a) 73 &times; 99 (b) 46 &times; 25 (c) 8 &times; 125", 3,
      f"(a) 73 &times; 100 &minus; 73 = 7300 &minus; 73 = <b>{v1}</b> &nbsp; (b) 46 &times; 100 &divide; 4 = 4600 &divide; 4 = <b>{v2}</b> &nbsp; (c) 8 &times; 125: 8 &times; 100 = 800 and 8 &times; 25 = 200, so 800 + 200 = <b>{v3}</b>")]))

# ---- Q13 bulbs
def col(i): return "#9be3a8" if i % 12 == 0 else "#ffe27a" if i % 3 == 0 else "#9fd3ff" if i % 4 == 0 else "#ffffff"
both = [i for i in range(1, 25) if i % 3 == 0 and i % 4 == 0]; nb = len([i for i in range(1, 25) if i % 4 == 0]); lc = math.lcm(6, 8); hc = math.gcd(12, 18)
assert both == [12, 24] and nb == 6 and lc == 24 and hc == 6 and 120 // lc == 5
I.append(Q("Bulbs numbered 1 to 24 are fixed on a board. Switch A lights every 3rd bulb (3, 6, 9, &hellip;) and Switch B lights every 4th bulb (4, 8, 12, &hellip;). Yellow = lit by A only, blue = lit by B only, green = lit by both.", 6,
           fig=bulbs(24, col), parts=[
    P("(i)", "(a) Which bulbs are lit by both the switches? (b) How many bulbs are lit by Switch B? (c) The first bulb lit by both is the LCM of which two numbers?", 3,
      f"(a) <b>{both[0]} and {both[1]}</b> (green) &nbsp; (b) 4, 8, 12, 16, 20, 24 = <b>{nb}</b> bulbs &nbsp; (c) LCM of 3 and 4 = 12"),
    P("(ii)", "(a) Find the LCM of 6 and 8. (b) Find the HCF of 12 and 18. (c) Two lights flash every 6 seconds and every 8 seconds. They flash together at 8:00 pm. How many more times do they flash together in the next 2 minutes?", 3,
      f"(a) <b>{lc}</b> &nbsp; (b) factors of 12: 1,2,3,4,6,12; of 18: 1,2,3,6,9,18; HCF = <b>{hc}</b> &nbsp; (c) together every {lc} s; 120 &divide; {lc} = <b>{120//lc}</b> times")]))

# ---- Q14 magic square + tiles
M = [[12, 5, 10], [7, 9, 11], [8, 13, 6]]
ms = sum(M[0]); assert all(sum(r) == ms for r in M) and all(sum(M[i][j] for i in range(3)) == ms for j in range(3))
d1 = M[0][0] + M[1][1] + M[2][2]; d2 = M[0][2] + M[1][1] + M[2][0]; assert d1 == d2 == ms == 27 and ms // 3 == M[1][1]
fm = "<table class='t5' style='font-size:1.1em'>" + "".join("<tr>" + "".join(f"<td style='width:34px'>{c}</td>" for c in r) + "</tr>" for r in M) + "</table>"
pairs = [(w, 48 // w) for w in range(1, 49) if 48 % w == 0 and w <= 48 // w]; best = min(pairs, key=lambda p: 2 * sum(p)); assert len(pairs) == 5 and best == (6, 8) and 2 * sum(best) == 28
I.append(Q("", 6, parts=[
    P("(i)", "The square on the right is a magic square. (a) What is the sum of each row? (b) Find the sum of the diagonal 12, 9, 6. (c) Which number in the square is exactly one-third of the magic sum?", 3,
      f"(a) 12 + 5 + 10 = <b>{ms}</b> &nbsp; (b) 12 + 9 + 6 = <b>{d1}</b> &nbsp; (c) 27 &divide; 3 = <b>9</b> (the middle number)", fig=fm),
    P("(ii)", "48 square tiles, each of side 1 m, are arranged to make a rectangle (using all the tiles). (a) In how many different ways (rectangles) can this be done? (b) Write the length and breadth of the rectangle having the smallest perimeter. (c) Write that perimeter.", 3,
      f"Factor pairs of 48: 1&times;48, 2&times;24, 3&times;16, 4&times;12, 6&times;8. (a) <b>{len(pairs)}</b> ways &nbsp; (b) <b>8 m by 6 m</b> &nbsp; (c) 2 &times; (8 + 6) = <b>{2*sum(best)} m</b>")]))

# ---- Q15-17
b1 = 5 * 1000 + 40; b2 = 3 * 1000 + 250; b3 = 3 * 60 + 15; assert (b1, b2, b3) == (5040, 3250, 195)
I.append(Q("Fill in the blanks: (a) 5 km 40 m = ______ m &nbsp; (b) 3 kg 250 g = ______ g &nbsp; (c) 3 hours 15 minutes = ______ minutes", 3, f"(a) {b1} &nbsp; (b) {b2} &nbsp; (c) {b3}"))
I.append(Q("Write True or False: (a) 6:30 pm is written as 18:30 in the 24-hour clock. (b) 450 g is more than half a kilogram. (c) The normal temperature of the human body is about 25&deg;C.", 3,
           "(a) True (6 + 12 = 18) &nbsp; (b) False (half kg = 500 g) &nbsp; (c) False (about 37&deg;C)"))
s, e = 9 * 60 + 45, 14 * 60 + 20; dur = e - s; assert (dur // 60, dur % 60) == (4, 35)
I.append(Q("A train leaves Jaipur at 9:45 am and reaches Kota at 2:20 pm the same day. How long does the journey take?", 3,
           f"2:20 pm = 14:20. From 9:45 to 14:20: 9:45 &rarr; 12:00 = 2 h 15 min; 12:00 &rarr; 14:20 = 2 h 20 min.<br>Total = <b>{dur//60} hours {dur%60} minutes</b>"))

# ---- Q18 route
nodes = {"Alwar": (45, 40, "a"), "Jaipur": (150, 78, "b"), "Ajmer": (240, 40, "a"), "Chittorgarh": (262, 135, "b"), "Kota": (160, 160, "b")}
edges = [("Alwar", "Jaipur", 150), ("Jaipur", "Ajmer", 130), ("Ajmer", "Chittorgarh", 190), ("Jaipur", "Kota", 250), ("Kota", "Chittorgarh", 170)]
d = {(a, b): k for a, b, k in edges}
r1 = d[("Alwar", "Jaipur")] + d[("Jaipur", "Ajmer")]; via_aj = d[("Jaipur", "Ajmer")] + d[("Ajmer", "Chittorgarh")]; via_k = d[("Jaipur", "Kota")] + d[("Kota", "Chittorgarh")]
r3 = d[("Alwar", "Jaipur")] + d[("Jaipur", "Kota")]; assert (r1, via_aj, via_k, r3, r3 // 5) == (280, 320, 420, 400, 80)
I.append(Q("The road map of some cities of Rajasthan is shown (distances are given in km).", 8, fig=route(nodes, edges), parts=[
    P("(a)", "A bus goes from Alwar to Ajmer through Jaipur. How far does it travel?", 2, f"150 + 130 = <b>{r1} km</b>"),
    P("(b)", "Which route from Jaipur to Chittorgarh is shorter &mdash; through Ajmer or through Kota? By how many km?", 2, f"Through Ajmer: {via_aj} km; through Kota: {via_k} km. Through <b>Ajmer</b> is shorter by {via_k-via_aj} km."),
    P("(c)", "A car runs 5 km on 1 litre of petrol. How many litres are needed from Alwar to Kota via Jaipur?", 2, f"Distance = 150 + 250 = {r3} km; petrol = {r3} &divide; 5 = <b>{r3//5} litres</b>"),
    P("(d)", "Which city is nearest to Jaipur? Write the distance.", 2, "<b>Ajmer</b>, 130 km (Alwar 150, Kota 250)")]))

# ---- Q19-22
sq = 144; assert math.isqrt(sq) ** 2 == sq and all(math.isqrt(x) ** 2 != x for x in (150, 200, 96))
I.append(mc("Which of the following is a square number?", sq, [150, 200, 96], 1))
st = [stairs(i) for i in (1, 2, 3, 4)]; assert [len(s) for s in st] == [1, 3, 6, 10] and len(stairs(6)) == 21
I.append(mc("Squares are arranged in steps as shown. How many squares will be there in Fig. 6?", 21, [15, 18, 24], 0, fig=pats(st), why="1, 3, 6, 10, 15, 21"))
lab = ["Cricket", "Kabaddi", "Kho-kho", "Hockey", "Football"]; val = [24, 18, 12, 6, 15]
I.append(Q("The bar graph shows the favourite game of the students of Class 5.", 3, fig=bars(lab, val, 6, 24, ylab="Number of students", xlab="Games"), parts=[
    P("(a)", "Which game is liked by the most students?", 1, "Cricket (24)"),
    P("(b)", "How many more students like Cricket than Hockey?", 1, f"{val[0]} &minus; {val[3]} = {val[0]-val[3]}"),
    P("(c)", "How many students are there in all?", 1, f"24 + 18 + 12 + 6 + 15 = {sum(val)}")]))
assert sum(val) == 75
t = [5 + 4 * i for i in range(10)]; assert t[:6] == [5, 9, 13, 17, 21, 25] and t[9] == 41
I.append(Q("Look at the pattern: 5, 9, 13, 17, ___, ___. (a) Write the rule. (b) Write the next two numbers. (c) What will be the 10th number?", 3,
           f"(a) add 4 each time &nbsp; (b) {t[4]}, {t[5]} &nbsp; (c) 5 + 9 &times; 4 = {t[9]}"))

finish(6, I)
