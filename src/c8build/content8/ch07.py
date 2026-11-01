from math import gcd
from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
# A: simplest form (6)
for a, b in [(18, 24), (45, 60), (28, 35), (36, 90), (54, 72), (25, 100)]:
    g = gcd(a, b)
    A.append(M4(f"The ratio {a} : {b} in its simplest form is:", f"{a//g} : {b//g}", [f"{a//g+1} : {b//g}", f"{a//g} : {b//g+1}", f"{b//g} : {a//g}"], f"Divide both by HCF {g}"))
# A: missing term in proportion (5)
for a, b, c in [(3, 5, 12), (4, 9, 20), (2, 7, 10), (5, 6, 15), (7, 8, 21)]:
    d = b * c // a
    A.append(M4(f"If {a} : {b} = {c} : x, then x equals:", str(d), [str(d+1), str(d-1), str(d+3)], f"Product of extremes = product of means: ${a}x={b*c}$") if (b*c) % a == 0 else None)
A = [x for x in A if x]
# A: sharing in ratio (5)
for tot, r1, r2 in [(500, 2, 3), (720, 5, 4), (900, 7, 3), (840, 3, 4), (660, 5, 6)]:
    s = tot // (r1 + r2)
    A.append(M4(f"₹ {tot} is divided between A and B in the ratio {r1} : {r2}. A's share is:", f"₹ {r1*s}", [f"₹ {r2*s}", f"₹ {r1*s+s}", f"₹ {tot//2}", f"₹ {r1*s+2*s}"], f"A gets {r1}/{r1+r2} of {tot}"))
# A: unit conversions (6)
for q, ans, wr in [("2.5 km in metres is:", "2500 m", ["250 m", "25 m", "25000 m"]),
                   ("3 hours in minutes is:", "180 minutes", ["30 minutes", "360 minutes", "300 minutes"]),
                   ("750 g in kg is:", "0.75 kg", ["7.5 kg", "75 kg", "0.075 kg"]),
                   ("4.2 litres in mL is:", "4200 mL", ["420 mL", "42 mL", "42000 mL"]),
                   ("15 cm in metres is:", "0.15 m", ["1.5 m", "15 m", "0.015 m"]),
                   ("90 minutes in hours is:", "1.5 hours", ["9 hours", "0.9 hours", "15 hours"])]:
    A.append(M4(q, ans, wr, "Unit conversion"))
# A: concepts (fill to 40)
A += [
 M4("A ratio compares two quantities of the same kind by:", "division", ["addition", "subtraction", "multiplication"], "Ratio $a:b=a/b$"),
 M4("The ratio of 1 m to 40 cm is:", "5 : 2", ["1 : 40", "2 : 5", "25 : 1"], "100 cm : 40 cm"),
 M4("If 4 : 7 = x : 21, then x is:", "12", ["9", "15", "28"], "Multiply both by 3"),
 M4("Two ratios are equal if they:", "have the same value when simplified", ["have the same first term", "have the same sum", "have equal differences"], "Proportion"),
 M4("The ratio 3 : 4 is equivalent to:", "9 : 12", ["6 : 9", "4 : 3", "7 : 8"], "Multiply both by 3"),
 M4("If the cost of 6 pens is ₹ 90, the cost of 10 pens is:", "₹ 150", ["₹ 100", "₹ 120", "₹ 180"], "₹ 15 per pen"),
 M4("A car covers 240 km in 4 hours. In 7 hours at the same speed it covers:", "420 km", ["360 km", "480 km", "280 km"], "60 km/h"),
 M4("A mixture has milk and water in the ratio 3 : 2. In 20 L of mixture, milk is:", "12 L", ["8 L", "10 L", "15 L"], "3/5 of 20"),
 M4("The ratio of 15 minutes to 2 hours is:", "1 : 8", ["15 : 2", "1 : 4", "1 : 6"], "15 : 120"),
 M4("If A : B = 2 : 3 and B : C = 4 : 5, then A : B : C is:", "8 : 12 : 15", ["2 : 3 : 5", "2 : 4 : 5", "6 : 8 : 10"], "Make B equal"),
 M4("Rohan is 12 years old and his father is 42. The ratio of their ages is:", "2 : 7", ["7 : 2", "1 : 3", "3 : 7"], "12 : 42"),
 M4("If the ratio of boys to girls is 5 : 4 and there are 36 girls, the number of boys is:", "45", ["40", "36", "54"], "9 units"),
]
A += [
 M4("If 5 notebooks cost ₹ 120, then 8 notebooks cost:", "₹ 192", ["₹ 160", "₹ 200", "₹ 240"], "₹ 24 each"),
 M4("The ratio of 250 g to 2 kg is:", "1 : 8", ["1 : 4", "5 : 4", "1 : 80"], "250 g : 2000 g"),
 M4("A map scale 1 cm = 5 km. A distance of 3.5 cm on the map represents:", "17.5 km", ["1.75 km", "15 km", "35 km"], "3.5 × 5"),
 M4("The ratios 2 : 5 and 6 : x are equal if x is:", "15", ["12", "18", "30"], "Multiply by 3"),
 M4("If x and y are inversely proportional and x doubles, y:", "becomes half", ["doubles", "stays same", "becomes zero"], "Product constant"),
 M4("The cost of 12 eggs is ₹ 90. The cost of 18 eggs is:", "₹ 135", ["₹ 120", "₹ 150", "₹ 108"], "₹ 7.5 each"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("What is a ratio? Write the ratio of 24 to 36 in simplest form.", "Comparison of two quantities by division (1); $2:3$ (1).", "1+1"),
 Q("Write the ratio of 75 paise to ₹ 3 in simplest form.", "$75:300=1:4$ (2).", "2"),
 Q("Are 4 : 9 and 12 : 27 in proportion? Why?", "Yes, $4\\times27=108=9\\times12$ (2).", "2"),
 Q("Divide ₹ 1200 between two friends in the ratio 3 : 5.", "Shares ₹ 450 and ₹ 750 (2).", "2"),
 Q("Convert 3.6 km to metres and 450 mL to litres.", "3600 m (1); 0.45 L (1).", "1+1"),
 Q("If 8 workers finish a job in 15 days, how many days will 12 workers take?", "Inverse relation: $8\\times15/12=10$ days (2).", "2"),
 Q("Find $x$ if $5:8=x:40$.", "$x=25$ (2).", "2"),
 Q("The ratio of cats to dogs in a shelter is 4 : 5. If there are 20 cats, how many dogs?", "25 dogs (2).", "2"),
 Q("What does a map scale 1 : 50000 mean?", "1 unit on the map is 50000 of the same units on the ground (2).", "2"),
 Q("A recipe uses 2 cups of rice for 5 persons. How many cups for 15 persons?", "6 cups (2).", "2"),
 Q("State two ways to check that two ratios are equal.", "Reduce to simplest form (1); cross-multiply (1).", "1+1"),
 Q("Write the ratio of 2 hours to 40 minutes.", "$120:40=3:1$ (2).", "2"),
 Q("Find the ratio of the perimeter of a square of side 6 cm to the side.", "$24:6=4:1$ (2).", "2"),
 Q("If the ratio of ages of two sisters is 3 : 4 and the elder is 20, find the younger.", "15 years (2).", "2"),
 Q("Write the ratio 45 minutes : 1 day in simplest form.", "$45:1440=1:32$ (2).", "2"),
 Q("What is direct proportion? Give an example.", "When one quantity increases, the other increases in the same ratio (1); cost and quantity (1).", "1+1"),
]
for tot, r in [(1500, (2, 3)), (2400, (3, 5)), (4200, (4, 3)), (1800, (1, 2, 3)), (3300, (2, 3, 6)), (2800, (3, 4, 7))]:
    t = sum(r); u = tot // t
    C.append(Q(f"Divide ₹ {tot} in the ratio {':'.join(map(str, r))}.", f"Total parts $={t}$ (1); one part $=₹ {u}$ (1); shares {', '.join('₹ '+str(x*u) for x in r)} (1).", "1+1+1"))
for ratio, t in [((3, 2), 40), ((5, 3), 64), ((4, 5), 72), ((7, 3), 50), ((2, 7), 90), ((3, 8), 66)]:
    a, b = ratio; tu = t // (a + b)
    C.append(Q(f"Two numbers are in the ratio {a} : {b} and their sum is {t}. Find the numbers.", f"Let numbers be ${a}x$, ${b}x$; ${a+b}x={t}$ (1); $x={t/(a+b):g}$ (1); numbers {a*t/(a+b):g} and {b*t/(a+b):g} (1).", "1+1+1"))
C += [
 Q("A map has scale 1 : 200000. Two towns are 6 cm apart on the map. Find the actual distance in km.", "$6\\times200000=12$ lakh cm (1); $=12$ km (2).", "1+2"),
 Q("The ratio of copper to zinc in brass is 13 : 7. How much zinc is in 5 kg brass?", "$7/20\\times5=1.75$ kg (3).", "3"),
 Q("A car uses 8 L of petrol for 112 km. How far will it go with 15 L?", "14 km per L (1); 210 km (2).", "1+2"),
 Q("The ratio of boys to girls in a class is 7 : 5. If total is 36, find the number of each.", "21 and 15 (3).", "3"),
 Q("A rope 36 m long is cut into three pieces in the ratio 2 : 3 : 4. Find the pieces.", "8 m, 12 m, 16 m (3).", "3"),
 Q("The speeds of two trains are in the ratio 4 : 5. If the second travels 300 km in a given time, how far does the first go?", "240 km (3).", "3"),
]
C += [
 Q("Find the ratio of 3 m 20 cm to 1 m 60 cm and simplify.", "$320:160=2:1$ (3).", "3"),
 Q("The ages of Rita and Sita are in the ratio 5 : 7 and the sum of their ages is 60. Find their ages after 5 years.", "Ages 25 and 35 (2); after 5 years 30 and 40 (1).", "2+1"),
 Q("If 15 men can reap a field in 12 days, in how many days can 20 men reap it?", "Total work 180 man-days (1.5); $180/20=9$ days (1.5).", "1½+1½"),
 Q("A train travels 150 km in 2.5 hours. At the same speed, find the time to cover 270 km.", "Speed 60 km/h (1.5); 4.5 hours (1.5).", "1½+1½"),
 Q("A mixture of 40 L contains milk and water in the ratio 7 : 1. How much water must be added to make the ratio 7 : 3?", "Milk 35 L, water 5 L (1); new water $=15$ L (1); add 10 L (1).", "1+1+1"),
 Q("The perimeters of two squares are in the ratio 2 : 3. Find the ratio of their sides and areas.", "Sides 2 : 3 (1.5); areas 4 : 9 (1.5).", "1½+1½"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Define ratio and proportion. (ii) Find $x$ if $x:12=15:20$. (iii) Check if 6, 9, 10, 15 are in proportion.", "(i) Ratio is a comparison by division; proportion is equality of two ratios (2). (ii) $x=9$ (1.5). (iii) $6\\times15=90=9\\times10$, yes (1.5).", "2+1½+1½"),
 Q("(i) Divide ₹ 7500 among A, B, C in the ratio 2 : 3 : 5. (ii) If C gives ₹ 500 to A, find the new ratio.", "(i) ₹ 1500, ₹ 2250, ₹ 3750 (3). (ii) A 2000 : B 2250 : C 3250 = 8 : 9 : 13 (2).", "3+2"),
 Q("<b>Case study:</b> A recipe for 6 people uses 450 g flour, 300 g sugar and 150 g butter. (i) Write the ratio of flour : sugar : butter. (ii) Find quantities for 10 people. (iii) How many people can be served with 1.5 kg flour?", "(i) 3 : 2 : 1 (1). (ii) 750 g, 500 g, 250 g (2). (iii) 20 people (2).", "1+2+2"),
 Q("(i) A map scale is 1 cm = 25 km. Find the actual distance for 7.4 cm. (ii) Express the scale as a ratio.", "(i) 185 km (2). (ii) $1:2500000$ (3).", "2+3"),
 Q("(i) 12 men can build a wall in 20 days. How many days will 15 men take? (ii) How many men are needed to finish in 8 days?", "(i) 16 days (2.5). (ii) 30 men (2.5).", "2½+2½"),
 Q("<b>Case study:</b> A school's 480 students are in the ratio 5 : 3 for Primary and Secondary sections. (i) How many in each? (ii) If 20 Primary students shift to Secondary, find the new ratio. (iii) Comment.", "(i) 300 and 180 (2). (ii) 280 : 200 = 7 : 5 (2). (iii) Ratio changes as numbers shift (1).", "2+2+1"),
 Q("(i) If $A:B=3:4$ and $B:C=6:7$, find $A:B:C$. (ii) If the sum is 175, find each.", "(i) $9:12:14$ (2). (ii) Total parts 35, so 45, 60 and 70 (3).", "2+3"),
 Q("(i) Convert 36 km/h to m/s. (ii) A cyclist travels 15 km in 50 minutes; find speed in km/h.", "(i) $36\\times1000/3600=10$ m/s (2). (ii) 18 km/h (3).", "2+3"),
 Q("(i) 6 pipes fill a tank in 2 hours. Find the time for 4 pipes. (ii) Name the type of variation.", "(i) 3 hours (3). (ii) Inverse proportion (2).", "3+2"),
 Q("<b>Case study:</b> Mix a paint using blue and white in ratio 3 : 7. (i) How much white for 9 L blue? (ii) Total paint? (iii) Percentage of blue?", "(i) 21 L (2). (ii) 30 L (1). (iii) 30% (2).", "2+1+2"),
 Q("(i) Divide 156 into parts proportional to $\\tfrac12,\\tfrac13,\\tfrac14$. (ii) Which part is greatest?", "(i) Ratio $6:4:3$; parts 72, 48 and 36 (3). (ii) The first (2).", "3+2"),
 Q("(i) Express ratio 0.75 : 1.5 and 2/3 : 5/6 in simplest form. (ii) Which is greater?", "(i) $1:2$ and $4:5$ (3). (ii) $4:5$ is greater since $0.8>0.5$ (2).", "3+2"),
 Q("<b>Case study:</b> A shop sells 3 pens for ₹ 45. (i) Cost of 1 pen. (ii) Cost of 14 pens. (iii) How many pens for ₹ 375?", "(i) ₹ 15 (1). (ii) ₹ 210 (2). (iii) 25 pens (2).", "1+2+2"),
 Q("(i) State unit conversions between km, m, cm, mm. (ii) Convert 4 km 250 m to metres and 0.045 km to cm.", "(i) 1 km = 1000 m, 1 m = 100 cm, 1 cm = 10 mm (2). (ii) 4250 m and 4500 cm (3).", "2+3"),
 Q("(i) The ratio of incomes of two persons is 5 : 4 and expenses 4 : 3. If each saves ₹ 1000, find incomes. (ii) Verify.", "(i) Incomes $5x$, $4x$, expenses $4y$, $3y$; $5x-4y=1000$, $4x-3y=1000$ give $x=y=1000$, incomes ₹ 5000 and ₹ 4000 (3). (ii) Expenses ₹ 4000 and ₹ 3000, savings ₹ 1000 each (2).", "3+2"),
]
D.append(Q("(i) Find the ratio of the areas of two squares with sides 7 cm and 14 cm. (ii) Compare with the ratio of the sides.", "(i) $49:196=1:4$ (3). (ii) Sides $1:2$, so area ratio is the square of the side ratio (2).", "3+2"))
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
