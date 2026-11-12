from maths_h import *
import math

I = []
cells = shape(["#.#.#", "#####", "#####", ".###."]); A1 = len(cells); assert A1 == 16
I.append(mc("Each square in the figure has an area of 1 square cm. The area of the shaded figure is", f"{A1} sq cm", ["14 sq cm", "15 sq cm", "18 sq cm"], 3, fig=svg_grid(cells, 18)))

def kind(d): return "acute" if d < 90 else "right" if d == 90 else "obtuse" if d < 180 else "straight" if d == 180 else "reflex"
assert [kind(27), kind(143), kind(215)] == ["acute", "obtuse", "reflex"] and kind(100) == "obtuse"
I.append(Q("", 6, parts=[
    P("(i)", "Write the type of each angle: (a) &ang;X (b) &ang;Y (c) &ang;Z", 3, "(a) acute &nbsp; (b) obtuse &nbsp; (c) reflex", fig=angles([("X", 27), ("Y", 143), ("Z", 215)])),
    P("(ii)", "(a) What is the measure of each corner angle of a square? (b) Is an angle of 100&deg; acute or obtuse? (c) A window is opened until its two parts lie in one straight line. What angle do they make?", 3,
      "(a) 90&deg; (a right angle) &nbsp; (b) obtuse (it is more than 90&deg; and less than 180&deg;) &nbsp; (c) 180&deg; (a straight angle)")]))

S = {"square pyramid": (5, 8, 5), "cone": (2, 1, 1), "cube": (6, 12, 8), "triangular prism": (5, 9, 6)}
for k, (f, e, v) in S.items():
    if k != "cone": assert f + v - e == 2
I.append(Q("", 6, parts=[
    P("(i)", "Name the solid that can be folded from each net: (a) 4 triangles joined to 1 square (b) 6 rectangles (c) 2 triangles and 3 rectangles", 3,
      "(a) square pyramid &nbsp; (b) cuboid &nbsp; (c) triangular prism"),
    P("(ii)", "(a) How many edges does a square pyramid have? (b) How many vertices does a cone have? (c) How many faces does a cube have?", 3,
      f"(a) {S['square pyramid'][1]} &nbsp; (b) {S['cone'][2]} &nbsp; (c) {S['cube'][0]}")]))

top = [("Study", 3), ("Hall", 6)]; bot = [("Bath", 3), ("Kitchen", 6)]; h1, h2, gh = 4, 3, 3
R = {"Study": (3, 4), "Hall": (6, 4), "Bath": (3, 3), "Kitchen": (6, 3), "Garden": (9, 3)}; AR = {k: w * h for k, (w, h) in R.items()}
ph = 2 * sum(R["Hall"]); big = [k for k, v in AR.items() if v > 15]; kc = AR["Kitchen"] * 120
assert (ph, AR["Kitchen"], kc, sorted(big)) == (20, 18, 2160, ["Garden", "Hall", "Kitchen"])
I.append(Q("The plan of a farmhouse near Pushkar is shown below.", 8, fig=plan(9, top, bot, h1, h2, ("Garden", gh)), parts=[
    P("(a)", "Find the perimeter of the Hall.", 2, f"2 &times; (6 + 4) = <b>{ph} m</b>"),
    P("(b)", "Find the area of the Kitchen.", 2, f"6 &times; 3 = <b>{AR['Kitchen']} sq m</b>"),
    P("(c)", "The Kitchen floor is to be tiled at &#8377; 120 per sq m. What will be the cost?", 2, f"18 &times; 120 = <b>{rs(kc)}</b>"),
    P("(d)", "How many rooms (including the Garden) have an area of more than 15 sq m? Name them.", 2, f"Areas: Study {AR['Study']}, Hall {AR['Hall']}, Bath {AR['Bath']}, Kitchen {AR['Kitchen']}, Garden {AR['Garden']}. <b>{len(big)} &mdash; Hall, Kitchen and Garden</b>")]))

pv = 30000; assert str(530462)[1] == "3"
I.append(mc("In 5,30,462, the place value of the digit 3 is", ind(pv), [ind(3000), ind(300000), ind(300)], 0))
nm = 806040; I.append(mc("Eight lakh six thousand forty is written as", ind(nm), [ind(860040), ind(80640), ind(806400)], 2))
nums = [58204, 85402, 52840, 82504]; ds = sorted(nums, reverse=True); asc = sorted(nums); assert ds == [85402, 82504, 58204, 52840]
fmt = lambda l: ", ".join(ind(x) for x in l)
I.append(mc("Which line shows the numbers in descending order?", fmt(ds), [fmt(asc), fmt([85402, 58204, 82504, 52840]), fmt([82504, 85402, 52840, 58204])], 1))

g, v = Fr(1, 2), Fr(1, 3); used = g + v; rest = 1 - used; grass = rest * 120; assert (used, rest, grass) == (Fr(5, 6), Fr(1, 6), 20)
fig8 = nl(1, 2, 4, {"A": Fr(5, 4), "B": Fr(3, 2), "C": Fr(7, 4)}, {0: "1", 4: "2"})
I.append(Q("", 6, parts=[
    P("(i)", "In a garden of 120 sq m, 1/2 of the area has flowering plants and 1/3 of the area has vegetables. The rest is grass. (a) What fraction of the garden has plants (flowers and vegetables together)? (b) What fraction is grass? (c) How many sq m is the grass?", 3,
      f"(a) 1/2 + 1/3 = 3/6 + 2/6 = <b>5/6</b> &nbsp; (b) 1 &minus; 5/6 = <b>1/6</b> &nbsp; (c) 120 &divide; 6 = <b>{grass} sq m</b>"),
    P("(ii)", "The line from 1 to 2 is divided into 4 equal parts. Write the mixed number shown by A, B and C.", 3, "A = 1 1/4 &nbsp; B = 1 2/4 = 1 1/2 &nbsp; C = 1 3/4", fig=fig8)]))

q9 = 3600 // 12; assert q9 == 300
I.append(mc("3,600 &divide; 12 =", q9, [30, 3000, 330], 3))

ad, ch = 185, 90; tt = 2 * ad + 3 * ch; chg = 1000 - tt; assert (tt, chg) == (640, 360)
I.append(Q("A bus ticket from Jaipur to Kota costs &#8377; 185 for an adult and &#8377; 90 for a child. A family of 2 adults and 3 children buys tickets and pays with a &#8377; 1,000 note. How much money is returned?", 3,
           f"Adults: 2 &times; 185 = {rs(2*ad)}; children: 3 &times; 90 = {rs(3*ch)}<br>Total = {rs(tt)}<br>Money returned = 1,000 &minus; {tt} = <b>{rs(chg)}</b>"))

q, r = divmod(6359, 40); assert (q, r) == (158, 39) and 40 * q + r == 6359
I.append(Q("A farmer in Nagaur has 6,359 kg of wheat. He fills sacks of 40 kg each. How many full sacks are made and how many kg are left? Verify your answer.", 3,
           f"6359 &divide; 40: quotient <b>{q}</b>, remainder <b>{r}</b>. So <b>{q} full sacks</b> and <b>{r} kg</b> are left.<br>Check: 40 &times; {q} + {r} = {40*q} + {r} = {40*q+r}. &#10003;"))

items = [349, 475, 628, 584]; s = sum(items); bal = 2500 - s; assert (s, bal) == (2036, 464)
w1, w2, w3 = 64 * 11, 18 * 50, 97 + 3 + 88; assert (w1, w2, w3) == (704, 900, 188)
I.append(Q("", 6, parts=[
    P("(i)", "For Class 5, Meena&rsquo;s father bought a bag for &#8377; 349, shoes for &#8377; 475, books for &#8377; 628 and a uniform for &#8377; 584. (a) What is the total bill? (b) He paid &#8377; 2,500. How much is returned? (c) Would &#8377; 2,000 have been enough?", 3,
      f"(a) 349 + 475 + 628 + 584 = <b>{rs(s)}</b> &nbsp; (b) 2,500 &minus; 2,036 = <b>{rs(bal)}</b> &nbsp; (c) <b>No</b>, as 2,036 is more than 2,000."),
    P("(ii)", "Find by an easy method: (a) 64 &times; 11 (b) 18 &times; 50 (c) 97 + 88 + 3", 3,
      f"(a) 64 &times; 10 + 64 = 640 + 64 = <b>{w1}</b> &nbsp; (b) 18 &times; 100 &divide; 2 = 1800 &divide; 2 = <b>{w2}</b> &nbsp; (c) 97 + 3 + 88 = 100 + 88 = <b>{w3}</b>")]))

def col(i): return "#9be3a8" if i % 12 == 0 else "#ffe27a" if i % 4 == 0 else "#9fd3ff" if i % 6 == 0 else "#ffffff"
cm = [i for i in range(1, 37) if i % 4 == 0 and i % 6 == 0]; lc = math.lcm(8, 12); hc = math.gcd(24, 36)
assert cm == [12, 24, 36] and lc == 24 and hc == 12 and 18 % 4 != 0
I.append(Q("Two frogs jump along the numbers 1 to 36. Frog A lands on 4, 8, 12, &hellip; (every 4th number) and Frog B lands on 6, 12, 18, &hellip; (every 6th number). Yellow = only A lands, blue = only B lands, green = both land.", 6,
           fig=bulbs(36, col, per=12), parts=[
    P("(i)", "(a) On which numbers do both frogs land? (b) The first common landing number is the LCM of which two numbers? (c) Does Frog A land on 18? Why?", 3,
      f"(a) <b>{', '.join(map(str, cm))}</b> &nbsp; (b) LCM of 4 and 6 = 12 &nbsp; (c) No, 18 is not a multiple of 4 (18 &divide; 4 leaves remainder 2)"),
    P("(ii)", "(a) Find the LCM of 8 and 12. (b) Find the HCF of 24 and 36. (c) A tape of 24 m and a tape of 36 m are cut into equal pieces of the longest possible length. What is the length of each piece?", 3,
      f"(a) <b>{lc}</b> &nbsp; (b) <b>{hc}</b> &nbsp; (c) HCF of 24 and 36 = <b>{hc} m</b>")]))

assert 344 + 365 == 709 and 27 * 3 == 81
ring = len(hollow(6)); assert ring == 20 == 4 * 6 - 4 and (6 - 2) ** 2 == 16
I.append(Q("", 6, parts=[
    P("(i)", "Find the digits A, B and C that make the sums correct: &nbsp; 3 A 4 + B 6 5 = 7 0 9 &nbsp; and &nbsp; 2 C &times; 3 = 8 1", 3,
      "Tens: A + 6 must end in 0, so A = 4 (carry 1). Hundreds: 3 + B + 1 = 7, so B = 3. Check: 344 + 365 = 709. &nbsp; 81 &divide; 3 = 27, so C = 7. &nbsp; <b>A = 4, B = 3, C = 7</b>"),
    P("(ii)", "A square garden of side 6 m has a path made of square tiles (1 m &times; 1 m) only along its border, as shaded. (a) How many tiles are on one side of the border? (b) How many tiles are used in all? (c) How many sq m of the garden are inside the border (not tiled)?", 3,
      f"(a) 6 &nbsp; (b) 4 &times; 6 &minus; 4 (corner tiles counted twice) = <b>{ring}</b> &nbsp; (c) inside is 4 m &times; 4 m = <b>16 sq m</b> (36 &minus; 20)", fig=pats([hollow(6)], cw=14))]))

x1, x2, x3 = 3 * 100 + 8, 4 * 1000 + 75, 1000 + 250; assert (x1, x2, x3) == (308, 4075, 1250)
I.append(Q("Fill in the blanks: (a) 3 m 8 cm = ______ cm &nbsp; (b) 4 kg 75 g = ______ g &nbsp; (c) 1 litre 250 mL = ______ mL", 3, f"(a) {x1} &nbsp; (b) {x2} &nbsp; (c) {x3}"))
I.append(Q("Write True or False: (a) &#8377; 2.75 is the same as 275 paise. (b) 1 kilometre is 100 metres. (c) 15:40 in the 24-hour clock is 3:40 pm.", 3,
           "(a) True &nbsp; (b) False (1 km = 1000 m) &nbsp; (c) True (15 &minus; 12 = 3)"))
sacks = 2 * 50 * 1000; sold = 37500; rem = sacks - sold; assert (rem // 1000, rem % 1000) == (62, 500)
I.append(Q("A grocer had 2 sacks of rice of 50 kg each. He sold 37 kg 500 g of it. How much rice is left?", 3,
           f"Total = 2 &times; 50 = 100 kg = {sacks} g<br>Sold = 37 kg 500 g = {sold} g<br>Left = {sacks} &minus; {sold} = {rem} g = <b>62 kg 500 g</b>"))

nodes = {"Udaipur": (40, 150, "b"), "Chittorgarh": (75, 50, "a"), "Bhilwara": (190, 40, "a"), "Ajmer": (265, 95, "a"), "Pushkar": (290, 165, "b")}
edges = [("Udaipur", "Chittorgarh", 115), ("Chittorgarh", "Bhilwara", 85), ("Bhilwara", "Ajmer", 130), ("Ajmer", "Pushkar", 15), ("Udaipur", "Ajmer", 270)]
d = {(a, b): k for a, b, k in edges}
long = 115 + 85 + 130; assert long == 330 and long - 270 == 60 and 2 * 15 == 30 and (85 + 130) * 2 == 430
I.append(Q("The map shows some roads of Rajasthan with their lengths in km.", 8, fig=route(nodes, edges), parts=[
    P("(a)", "How long is the road from Udaipur to Ajmer going through Chittorgarh and Bhilwara?", 2, f"115 + 85 + 130 = <b>{long} km</b>"),
    P("(b)", "How much shorter is the direct road from Udaipur to Ajmer than the route in part (a)?", 2, f"{long} &minus; 270 = <b>60 km</b>"),
    P("(c)", "A person goes from Ajmer to Pushkar and comes back the same day. How many km does he travel?", 2, "2 &times; 15 = <b>30 km</b>"),
    P("(d)", "A bus charges &#8377; 2 per km. What is the fare from Chittorgarh to Ajmer through Bhilwara?", 2, f"Distance = 85 + 130 = 215 km; fare = 215 &times; 2 = <b>{rs(430)}</b>")]))

tri = [1, 3, 6, 10, 15, 21, 28]; assert 28 in tri and not {27, 30, 26} & set(tri)
I.append(mc("Which of the following is a triangular number?", 28, [27, 30, 26], 0, why="1, 3, 6, 10, 15, 21, 28"))
hs = [hollow(k) for k in (2, 3, 4)]; assert [len(s) for s in hs] == [4, 8, 12] and len(hollow(7)) == 24
I.append(mc("Small squares are used to make hollow squares as shown. How many small squares are needed for Fig. 6?", 24, [20, 28, 36], 1, fig=pats(hs), why="4, 8, 12, &hellip; &rarr; 6 &times; 4 = 24"))
dv = [("Day 1", 15), ("Day 2", 25), ("Day 3", 40), ("Day 4", 50), ("Day 5", 30)]
I.append(Q("The bar graph shows the number of visitors (in hundreds) at a village fair on 5 days.", 3, fig=bars([a for a, _ in dv], [b for _, b in dv], 10, 50, ylab="Visitors (in hundreds)", xlab="Days"), parts=[
    P("(a)", "On which day were there the most visitors?", 1, "Day 4"),
    P("(b)", "How many visitors came on Day 2?", 1, "25 hundreds = 2,500"),
    P("(c)", "How many visitors came on Day 1 and Day 5 together?", 1, "(15 + 30) hundreds = 45 hundreds = 4,500")]))
sqn = [k * k for k in range(1, 11)]
I.append(Q("Look at the pattern: 1, 4, 9, 16, 25, ___, ___. (a) Write the next two numbers. (b) What kind of numbers are these? (c) What is the 10th number of the pattern?", 3,
           f"(a) {sqn[5]}, {sqn[6]} &nbsp; (b) square numbers (1&times;1, 2&times;2, 3&times;3, &hellip;) &nbsp; (c) 10 &times; 10 = {sqn[9]}"))

finish(8, I)
