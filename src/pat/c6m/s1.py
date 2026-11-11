from h6 import *
# ---------- Set 1 : emphasis Number Play, Prime Time, Fractions, Integers ----------
F4 = [Fr(3, 4), Fr(5, 8), Fr(7, 10), Fr(2, 3)]
g = max(F4)
q1 = mcqgroup([
 mm("The 8th triangular number (1, 3, 6, 10, ...) is:", tri(8), [28, 45, 64], "Sum 1 + 2 + ... + 8 = 36."),
 mm("At 4 o'clock, the angle between the hour hand and the minute hand is:", "120°", ["90°", "60°", "150°"], "Each hour gap is 30°; 4 × 30° = 120°."),
 mm("The greatest 4-digit number that can be formed using the digits 7, 0, 5, 9 (each once) is:", 9750, [9570, 9705, 7059], "Arrange digits in descending order: 9, 7, 5, 0."),
 mm("In a pictograph, one symbol stands for 20 books. A row has 3 full symbols and 1 half symbol. The number of books shown is:", 20 * 3 + 10, [60, 80, 35], "3 × 20 + 10 = 70."),
 mm("Which of the following is a prime number?", 97, [91, 87, 51], "91 = 7 × 13, 87 = 3 × 29, 51 = 3 × 17 are composite; 97 has no factor other than 1 and 97."),
 mm("Two temple bells ring every 12 minutes and every 18 minutes. They ring together at 6:00 a.m. They will next ring together at:", "6:36 a.m.", ["6:06 a.m.", "6:30 a.m.", "7:12 a.m."], "LCM(12, 18) = 36 minutes."),
 mm("The perimeter of a square plot is 36 m. Its area is:", 81, [36, 144, 1296], "Side = 36 ÷ 4 = 9 m; area = 9 × 9 = 81 m²."),
 m("Which of these fractions is the greatest?", imp(g), [imp(x) for x in F4 if x != g], "Common denominator 120: 90, 75, 84, 80 — greatest is 90/120 = 3/4."),
 m("The value of " + fr(Fr(7, 2)) + " + " + fr(Fr(11, 4)) + " is:", fr(Fr(7, 2) + Fr(11, 4)), [fr(Fr(7,2)+Fr(11,4)-Fr(1,2)), fr(Fr(61, 8)), fr(Fr(6))], "7/2 = 14/4; 14/4 + 11/4 = 25/4 = 6 1/4."),
 m("While drawing the perpendicular bisector of a 6 cm line segment using a compass, the arcs from both ends must have a radius:", "more than 3 cm", ["exactly 3 cm", "less than 3 cm", "exactly 6 cm"], "Arcs must cross each other, so the radius must exceed half of 6 cm."),
 mm("The number of lines of symmetry of a regular hexagon is:", 6, [3, 4, 2], "A regular polygon of n sides has n lines of symmetry."),
 mm("In Shimla the night temperature was −4 °C. By afternoon it rose by 9 °C. The afternoon temperature was:", "5 °C", ["−5 °C", "13 °C", "−13 °C"], "−4 + 9 = 5."),
])
b = [
 sa("For the sequence 1, 3, 6, 10, 15, ...: (i) write the next two terms; (ii) name the sequence.", 2, f"(i) {tri(6)}, {tri(7)} (1 mark)<br>(ii) Triangular numbers (1 mark)"),
 sa("Classify each angle as acute, right, obtuse or reflex: (i) 35° (ii) 90° (iii) 150° (iv) 200°.", 2, "(i) acute (ii) right (iii) obtuse (iv) reflex (any 2 correct = 1 mark; all 4 = 2 marks)"),
 OR(sa("Write the Collatz sequence that starts with 6. (Even number: halve it; odd number: multiply by 3 and add 1.)", 2, "Sequence: " + ", ".join(map(str, collatz(6))) + " (2 marks; 1 mark if one slip)"),
    sa("Do one round of Kaprekar's routine on 3524: arrange digits to make the largest and the smallest number, and subtract.", 2, f"Largest {kap(3524)[0]}, smallest {kap(3524)[1]:04d} (1 mark); difference = {kap(3524)[2]} (1 mark)")),
 sa("Find the HCF of 36 and 48 using prime factorisation.", 2, f"36 = {pfs(36)}, 48 = {pfs(48)} (1 mark)<br>HCF = 2² × 3 = {gcd(36,48)} (1 mark)"),
 sa("Add: " + fr(Fr(3, 8)) + " + " + fr(Fr(5, 12)) + ".", 2, f"LCM of 8 and 12 = 24: 9/24 + 10/24 (1 mark) = {imp(Fr(3,8)+Fr(5,12))} (1 mark)"),
 sa("Write the order of rotational symmetry of (i) a square (ii) an equilateral triangle.", 2, "(i) 4 (1 mark) (ii) 3 (1 mark)"),
]
c = [
 OR(sa("Three signal lights flash every 8, 12 and 20 seconds. They flash together at the start. (i) After how many seconds do they flash together again? (ii) How many times do they flash together in the next 10 minutes?", 3,
       f"(i) LCM(8, 12, 20) = {lcm(lcm(8,12),20)} s (2 marks)<br>(ii) 600 ÷ {lcm(lcm(8,12),20)} = {600//lcm(lcm(8,12),20)} times (1 mark)"),
    sa("(i) List all prime numbers between 60 and 90. (ii) Write one pair of twin primes from your list.", 3, f"(i) {', '.join(map(str, primes(61, 89)))} (2 marks)<br>(ii) 71 and 73 (1 mark)")),
 sa("A garden is shaped like the L in the figure. (i) Find its perimeter. (ii) Find its area. (iii) Find the cost of fencing it all around at ₹50 per metre.", 3,
    f"(i) Perimeter = 2(12 + 9) = {2*21} m (1 mark)<br>(ii) Area = 12 × 9 − 5 × 4 = 108 − 20 = {108-20} m² (1 mark)<br>(iii) Cost = 42 × 50 = ₹{42*50} (1 mark)", fig=G.lshape(12, 9, 5, 4)),
 sa("The bar graph shows how many students visited the school library on five days. (i) On which day did most students visit? (ii) Find the total number of visitors in the week. (iii) How many more students came on Wednesday than on Thursday?", 3,
    f"(i) Wednesday (1 mark)<br>(ii) 24 + 18 + 30 + 12 + 21 = {24+18+30+12+21} (1 mark)<br>(iii) 30 − 12 = 18 (1 mark)", fig=G.bar([("Mon", 24), ("Tue", 18), ("Wed", 30), ("Thu", 12), ("Fri", 21)], 30, 6, 'Students', 'Day')),
]
gr, sm = 8630, 3068
d = [
 OR(sa("Use the digits 3, 0, 8, 6 once each. (i) Form the greatest and the smallest 4-digit numbers. (ii) Find their difference. (iii) Estimate 4812 + 3197 by rounding each number to the nearest hundred.", 5,
       f"(i) Greatest {gr}, smallest {sm} (2 marks; 0 cannot be in the thousands place)<br>(ii) {gr} − {sm} = {gr-sm} (1 mark)<br>(iii) 4800 + 3200 = 8000 (2 marks)"),
    sa("Apply Kaprekar's routine to 8531. Show each step until you reach 6174 and write the number of steps taken.", 5,
       "<br>".join(f"{a} − {b:04d} = {r}" for a, b, r in kap_chain(8531)) + f"<br>6174 is reached in {len(kap_chain(8531))} steps. (1 mark per correct step up to 4, 1 mark for the count)")),
 OR(sa("Draw a line segment AB = 7 cm. Construct its perpendicular bisector with a compass and ruler. Let it meet AB at M and measure AM.", 5,
       "Steps: draw AB = 7 cm (1); with A as centre and radius more than 3.5 cm draw arcs on both sides (1); with the same radius and B as centre draw arcs cutting the first arcs at P and Q (1); join PQ meeting AB at M (1). AM = 3.5 cm = MB (1)."),
    sa("Draw ∠PQR = 70° using a protractor and bisect it using a compass. Write the measure of each half.", 5,
       "Steps: draw ray QR; place protractor at Q and mark 70°; draw QP (2 marks). With Q as centre draw an arc cutting both arms at X and Y (1). With X and Y as centres and the same radius draw arcs cutting at Z; join QZ (1). Each half = 35° (1).")),
 sa("The temperature at Mount Abu at 6 a.m. was −3 °C. It rose by 8 °C by noon and then fell by 5 °C by evening. (i) Find the temperature at noon. (ii) Find the temperature in the evening. (iii) By how many degrees is the evening temperature higher than the 6 a.m. temperature? (iv) Show the three temperatures on a number line from −5 to 6.", 5,
    f"(i) −3 + 8 = {-3+8} °C (1)<br>(ii) 5 − 5 = {5-5} °C (1)<br>(iii) 0 − (−3) = 3 °C (1)<br>(iv) Marks at −3, 5 and 0 on a correctly scaled number line (2)", fig=None),
]
case1 = case("On the occasion of Diwali, Nisha's mother prepares suji halwa. She uses 3/4 kg of suji and 1/2 kg of sugar for one batch.",
 [sub("What is the total weight of suji and sugar in one batch?", 1, f"3/4 + 1/2 = 3/4 + 2/4 = {fr(Fr(3,4)+Fr(1,2))} kg"),
  sub("How much more suji than sugar is used in one batch?", 1, f"3/4 − 1/2 = {imp(Fr(3,4)-Fr(1,2))} kg"),
  OR(sub("How much suji is needed for 6 such batches?", 2, f"6 × 3/4 (1 mark) = 18/4 = {fr(6*Fr(3,4))} kg (1 mark)"),
     sub("The suji and sugar of one batch (together) are shared equally among 5 children. How much (by weight) does each child get?", 2, f"Total = 5/4 kg (1 mark); each child: 5/4 ÷ 5 = {imp(Fr(5,4)/5)} kg (1 mark)"))])
case2 = case("A rectangular park in Jaipur is 30 m long and 20 m wide (see figure). The municipality wants to put a fence around it and grow grass inside.",
 [sub("Find the perimeter of the park.", 1, f"2 × (30 + 20) = {2*50} m"),
  sub("Find the area of the park.", 1, f"30 × 20 = {600} m²"),
  OR(sub("Fencing costs ₹40 per metre. Find the total cost of fencing.", 2, f"100 × 40 (1 mark) = ₹{100*40} (1 mark)"),
     sub("One packet of grass seed covers 50 m². How many packets are needed for the whole park?", 2, f"600 ÷ 50 (1 mark) = {600//50} packets (1 mark)"))], fig=G.rect_dim(30, 20, "30 m", "20 m", 4.5))
case3 = case("Aman looks at the wall clock in his classroom. It shows exactly 2 o'clock (see figure). He knows that the angle between two consecutive numbers on a clock is 30°.",
 [sub("What is the angle between the hour hand and minute hand at 2 o'clock?", 1, "2 × 30° = 60°"),
  sub("Name the type of this angle.", 1, "Acute angle (less than 90°)"),
  OR(sub("At 3 o'clock the hands make which kind of angle? Give its measure and explain.", 2, "Right angle (1 mark): 3 × 30° = 90° (1 mark)"),
     sub("Through how many degrees does the minute hand turn in 20 minutes? (It turns 360° in 60 minutes.)", 2, "20 ÷ 60 × 360° (1 mark) = 120° (1 mark)"))], fig=G.clock(2, 0))
META = meta(1); SECTIONS = secs(q1, b, c, d, [case1, case2, case3])
