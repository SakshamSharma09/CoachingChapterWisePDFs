from math import gcd
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def g(x): return f"{x:g}"
# A: map scale (6)
for cm, scale, km in [(4, 25, 100), (6.5, 20, 130), (3, 150, 450), (8, 12.5, 100), (2.4, 50, 120), (5, 40, 200)]:
    A.append(M4(f"On a map, 1 cm represents {g(scale)} km. A distance of {g(cm)} cm on the map represents:", f"{g(km)} km", [f"{g(km+scale)} km", f"{g(km/2)} km", f"{g(km*2)} km"], "Multiply by the scale"))
# A: 3-term ratio sharing (6)
for tot, r in [(600, (1, 2, 3)), (1100, (2, 3, 6)), (900, (3, 4, 2)), (1500, (5, 3, 2)), (840, (2, 4, 8)), (720, (1, 3, 5))]:
    t = sum(r); u = tot // t
    A.append(M4(f"₹ {tot} is shared among A, B and C in the ratio {':'.join(map(str, r))}. B gets:", f"₹ {r[1]*u}", [f"₹ {r[0]*u}", f"₹ {r[2]*u}", f"₹ {tot//3}", f"₹ {r[1]*u+2*u}", f"₹ {r[1]*u+u}"], f"One part = ₹ {u}"))
# A: inverse proportion (6)
for w, d, w2 in [(12, 10, 8), (6, 20, 15), (8, 9, 12), (15, 14, 10), (20, 6, 8), (9, 16, 12)]:
    d2 = w * d / w2
    A.append(M4(f"{w} workers finish a job in {d} days. How many days will {w2} workers take?", g(d2), [g(d2+2), g(d2-1), g(w2*d/w)], "Workers × days is constant"))
# A: pie chart angles (5)
for part in [(25, "25%"), (10, "10%"), (40, "40%"), (15, "15%"), (30, "30%")]:
    pc = part[0]
    A.append(M4(f"In a pie chart, a sector representing {pc}% of the data has a central angle of:", f"{g(pc*3.6)}°", [f"{g(pc*3.6+10)}°", f"{g(pc*2)}°", f"{g(pc)}°"], "Angle = percent × 3.6"))
# A: concepts (17)
A += [
 M4("A map scale 1 : 100000 means 1 cm on the map is how many km on the ground?", "1 km", ["10 km", "0.1 km", "100 km"], "100000 cm = 1 km"),
 M4("If two quantities are inversely proportional, their:", "product is constant", ["sum is constant", "ratio is constant", "difference is constant"], "xy = k"),
 M4("If the speed doubles, the time taken for the same distance:", "halves", ["doubles", "remains same", "triples"], "Inverse proportion"),
 M4("A pie chart is made from a circle, whose total angle is:", "360°", ["180°", "100°", "90°"], "Full turn"),
 M4("If A : B = 2 : 3 and B : C = 3 : 5, then A : B : C is:", "2 : 3 : 5", ["2 : 5 : 3", "3 : 2 : 5", "6 : 9 : 15"], "B is already common"),
 M4("The ratio 20 : 30 : 50 in simplest form is:", "2 : 3 : 5", ["1 : 2 : 3", "4 : 6 : 10", "2 : 3 : 4"], "Divide by 10"),
 M4("A whole divided in the ratio 3 : 7 gives the smaller part as what fraction of the whole?", "3/10", ["3/7", "7/10", "3/4"], "3 of 10 parts"),
 M4("If 10 pipes fill a tank in 6 hours, 15 pipes will fill it in:", "4 hours", ["9 hours", "5 hours", "3 hours"], "Pipes × hours = 60"),
 M4("A scale drawing has scale 1 : 50. A 2 m wall is drawn with length:", "4 cm", ["40 cm", "2 cm", "10 cm"], "200 cm / 50"),
 M4("Which pair is in direct proportion?", "Cost and number of identical items", ["Speed and time", "Workers and days", "Pipes and time"], "More items, more cost"),
 M4("If the ratio of boys to girls is 3 : 2, the percentage of girls is:", "40%", ["60%", "33.3%", "50%"], "2/5"),
 M4("The sector angle for 90° of a pie chart represents what percent?", "25%", ["50%", "10%", "75%"], "90/360"),
 M4("Three partners invest ₹ 2000, ₹ 3000 and ₹ 5000. The profit ratio is:", "2 : 3 : 5", ["1 : 2 : 3", "2 : 5 : 3", "5 : 3 : 2"], "In proportion to investment"),
 M4("The map distance is 5 cm and the actual distance is 20 km. The scale is 1 cm =", "4 km", ["5 km", "100 km", "0.25 km"], "20/5"),
 M4("If x varies inversely with y and x = 6 when y = 4, then when y = 8, x =", "3", ["12", "24", "2"], "xy = 24"),
 M4("The slope of a speed–time reasoning: doubling men halves days. This is:", "inverse proportion", ["direct proportion", "no relation", "equal ratio"], "Definition"),
 M4("If a pizza is divided in the ratio 1 : 2 : 3 among three, the largest share is:", "1/2", ["1/3", "1/6", "2/3"], "3 of 6 parts"),
]
assert len(A) == 40, len(A)
B = [
 Q("What is an inverse proportion? Give an example.", "When one quantity increases the other decreases so that their product is constant (1); workers and days (1).", "1+1"),
 Q("A map has scale 1 cm = 8 km. Find the actual distance for 12.5 cm.", "100 km (2).", "2"),
 Q("Divide 360 in the ratio 1 : 2 : 3.", "60, 120, 180 (2).", "2"),
 Q("Write the ratio 2 : 3 and 3 : 5 as a single three-term ratio.", "2 : 3 : 5 (2).", "2"),
 Q("6 men build a wall in 12 days. How long will 9 men take?", "8 days (2).", "2"),
 Q("A pie chart sector is 72°. What percent of the whole is it?", "20% (2).", "2"),
 Q("Express the scale 1 : 200000 as 1 cm = ? km.", "1 cm = 2 km (2).", "2"),
 Q("If the ratio of red, white and blue balls is 2 : 3 : 5 and there are 40 balls, how many are blue?", "20 (2).", "2"),
 Q("A car takes 5 hours at 60 km/h. How long at 75 km/h?", "4 hours (2).", "2"),
 Q("Find the central angle of a sector representing 35% of the data.", "126° (2).", "2"),
 Q("The ratio of lengths on a blueprint is 1 : 40. A room 6 m long appears how long on it?", "15 cm (2).", "2"),
 Q("Find the missing term: 3 : 4 : 5 = 9 : x : y.", "$x=12$, $y=15$ (2).", "2"),
 Q("20 students eat in 12 days with a stock of food. How long does it last for 30 students?", "8 days (2).", "2"),
 Q("State the difference between direct and inverse proportion.", "Direct: ratio constant; inverse: product constant (2).", "2"),
 Q("A pie chart shows 300 students; 25% prefer cricket. How many?", "75 (2).", "2"),
 Q("A sum of ₹ 900 is shared in the ratio 4 : 5 : 6. Find the smallest share.", "₹ 240 (2).", "2"),
]
for tot, r in [(1800, (2, 3, 4)), (4400, (1, 3, 7)), (2700, (4, 5, 9)), (3600, (2, 5, 5)), (3000, (1, 2, 7)), (4800, (3, 4, 5))]:
    t = sum(r); u = tot // t
    C.append(Q(f"Divide ₹ {tot} among A, B and C in the ratio {':'.join(map(str, r))}.", f"Total parts $={t}$ (1); one part $=₹ {u}$ (1); shares {', '.join('₹ '+str(x*u) for x in r)} (1).", "1+1+1"))
for cm, scale in [(7.5, 40), (9, 15), (12.4, 25), (3.2, 150), (6.8, 50), (11, 30)]:
    C.append(Q(f"On a map, 1 cm stands for {g(scale)} km. Two cities are {g(cm)} cm apart. Find the actual distance. How long does a train at 60 km/h take?", f"Distance $={g(cm*scale)}$ km (1.5); time $={g(cm*scale/60)}$ h (1.5).", "1½+1½"))
for w, d, w2 in [(15, 20, 25), (24, 18, 36), (10, 30, 12), (8, 45, 18)]:
    C.append(Q(f"{w} workers can complete a task in {d} days. How many days will {w2} workers take, and how many extra days if {w} had worked?", f"Total work $={w*d}$ worker-days (1); days $={g(w*d/w2)}$ (1); difference ${g(abs(d-w*d/w2))}$ days (1).", "1+1+1"))
C += [
 Q("In a survey of 240 people, the pie chart angles for tea, coffee and juice are 150°, 120° and 90°. Find the number for each.", "Tea 100, coffee 80, juice 60 (3).", "3"),
 Q("A and B invest ₹ 12000 and ₹ 18000. They share a profit of ₹ 7500. Find each share.", "Ratio 2 : 3 (1); ₹ 3000 and ₹ 4500 (2).", "1+2"),
 Q("A map scale shows 5 cm = 20 km. What is 1 cm in km, and what is the representative ratio?", "1 cm = 4 km (1); $1:400000$ (2).", "1+2"),
 Q("A farmer has fodder for 30 cows for 24 days. How long for 36 cows?", "20 days (3).", "3"),
]
C += [
 Q("A pie chart of 360 students shows: Maths 25%, Science 35%, Arts 40%. Find the angles and the number of students for each.", "90°, 126°, 144° (1.5); 90, 126, 144 students (1.5).", "1½+1½"),
 Q("A and B can do a job in 12 days and 15 days respectively. Who is faster and what is the ratio of their daily work?", "A is faster (1); daily work ratio $\\frac1{12}:\\frac1{15}=5:4$ (2).", "1+2"),
 Q("The ratio of the angles of a triangle is 2 : 3 : 4. Find each angle.", "Sum 180° (1); 40°, 60°, 80° (2).", "1+2"),
 Q("The ratio of a father's age to son's is 7 : 2. If the difference is 35 years, find their ages.", "5 parts = 35, one part 7 (1.5); 49 and 14 (1.5).", "1½+1½"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Explain inverse proportion with an example. (ii) 8 men can dig a trench in 15 days. In how many days can 12 men dig it? (iii) How many men are needed to finish in 6 days?", "(i) Explanation (2). (ii) 10 days (1.5). (iii) 20 men (1.5).", "2+1½+1½"),
 Q("<b>Case study:</b> A road map uses a scale of 1 : 500000. (i) Express in cm to km. (ii) Two cities are 18 cm apart; find the actual distance. (iii) A bus at 50 km/h takes how long?", "(i) 1 cm = 5 km (2). (ii) 90 km (1). (iii) 1.8 hours (2).", "2+1+2"),
 Q("(i) Divide ₹ 12000 among A, B and C so that A : B = 2 : 3 and B : C = 4 : 5. (ii) Who gets the largest share?", "(i) A : B : C = 8 : 12 : 15; shares ₹ 2742.86? use ₹ 14000 instead: ₹ 3200, ₹ 4800, ₹ 6000 (3). (ii) C (2).", "3+2"),
 Q("(i) How is a pie chart drawn? (ii) Draw a pie chart for expenses of ₹ 2400: food 1200, rent 600, travel 400, savings 200 and give angles.", "(i) Angle = fraction × 360° (2). (ii) 180°, 90°, 60°, 30° (3).", "2+3"),
 Q("<b>Case study:</b> A pie chart shows the time spent by a student in a 24-hour day: sleep 8 h, school 6 h, study 4 h, play 3 h, other 3 h. (i) Find each angle. (ii) Which sector is the largest? (iii) By how many degrees does study exceed play?", "(i) 120°, 90°, 60°, 45°, 45° (3). (ii) Sleep (1). (iii) 15° (1).", "3+1+1"),
 Q("(i) A hostel has food for 80 students for 30 days. After 10 days 20 students leave. For how many more days will the food last? (ii) Explain.", "(i) Remaining 20 days of food for 80; for 60 students: $80\\times20/60=26\\tfrac23$ days (3). (ii) Inverse proportion (2).", "3+2"),
 Q("(i) Three friends invested ₹ 8000, ₹ 12000 and ₹ 20000. Profit is ₹ 10000. Find each share. (ii) What if the first invests for 12 months, others for 6 months?", "(i) 2000, 3000, 5000 (2). (ii) Ratio 96:72:120 = 4:3:5, shares 3333.33, 2500, 4166.67 (3).", "2+3"),
 Q("<b>Case study:</b> A model of a building is made at a scale of 1 : 150. (i) A 45 m tall building is how tall on the model? (ii) The model's door is 1.6 cm; find the real door. (iii) Floor area ratio between model and real.", "(i) 30 cm (2). (ii) 2.4 m (1). (iii) 1 : 22500 (2).", "2+1+2"),
 Q("(i) A train 300 m long crosses a pole in 15 s. Find its speed. (ii) At the same speed, time to cross a 450 m bridge?", "(i) 20 m/s (2). (ii) $750/20=37.5$ s (3).", "2+3"),
 Q("(i) Mix paints A and B in ratio 3 : 5. How much A is needed for 24 L total? (ii) If extra 10 L B is added, find the new ratio.", "(i) 9 L (2). (ii) 9 : 25 (3).", "2+3"),
 Q("(i) A recipe for 4 uses 300 g flour. How much for 10? (ii) Which type of proportion?", "(i) 750 g (3). (ii) Direct (2).", "3+2"),
 Q("<b>Case study:</b> The population of a town is in the ratio 3 : 2 : 5 among children, adults and seniors; total 20000. (i) Find each. (ii) Draw the pie chart angles. (iii) What percent are seniors?", "(i) 6000, 4000, 10000 (2). (ii) 108°, 72°, 180° (2). (iii) 50% (1).", "2+2+1"),
 Q("(i) A cyclist covers 36 km in 2 hours. How long for 90 km? (ii) What if the speed becomes 12 km/h?", "(i) 5 hours (2). (ii) 7.5 hours (3).", "2+3"),
 Q("(i) If 15 men take 6 days, find the work in man-days. (ii) How many men finish half the job in 3 days?", "(i) 90 man-days (2). (ii) Half is 45, so 15 men (3).", "2+3"),
 Q("(i) Show that if A : B = 3 : 4 and B : C = 5 : 6, then A : B : C = 15 : 20 : 24. (ii) Find each if sum is 118.", "(i) Make B = 20 (2). (ii) 30, 40, 48 (3).", "2+3"),
 Q("<b>Case study:</b> A scale on a floor plan is 1 cm : 2 m. A room is drawn 5 cm × 3.5 cm. (i) Find the actual dimensions. (ii) Area. (iii) Cost of flooring at ₹ 450 per m².", "(i) 10 m × 7 m (2). (ii) 70 m² (1). (iii) ₹ 31500 (2).", "2+1+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
