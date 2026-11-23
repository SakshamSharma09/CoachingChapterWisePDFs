"""Class 8 Maths Ch 10 - Proportional Reasoning-2: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch10"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths2" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# --- verify the numbers used ---
assert 800*5//8 == 500 and 6*48 == 6*48 and 48*9//6 == 72 and 4*20 == 80 and 4*12//6 == 8 and 90/360 == 0.25
assert F(45,120) == F(3,8) and 60*F(5,2) == 150 and 96*5//12 == 40 and 96*7//12 == 56 and 180*5//3 == 300
assert 360*30//100 == 108 and 7.5*2 == 15 and 60*2//5 == 24 and 60*3//5 == 36 and 8*15//10 == 12
assert [360*p//100 for p in (30,25,20,15,10)] == [108,90,72,54,36] and 24000*25//100 == 6000
assert 40*3//8 == 15 and 40*5//8 == 25 and 18*8//3 == 48 and 36000*2//9 == 8000 and 36000*4//9 == 16000
assert (2*4, 3*4, 3*5) == (8,12,15) and 70//35*8 == 16 and 18/5 == 3.6 and 6*5 == 30
assert 60*24//40 == 36 and F(1,6)+F(1,12) == F(1,4) and 12*10 == 120
assert F(3,4) > F(5,7) and 4*10 == 40 and 300*10//4 == 750 and 1200*4//300 == 16
assert 120*144//360 == 48 and 120*72//360 == 24 and 120*90//360 == 30 and 120*54//360 == 18 and 48+24+30+18 == 120
assert 4*60//80 == 3 and 40*3//5 == 24 and 40*2//5 == 16 and 1260*3//6 == 630 and 1260*2//6 == 420 and 1260//6 == 210
assert 18//(7-4) == 6 and 6*7 == 42 and 6*4 == 24 and 5*18 == 90 and 90//6 == 15
assert F(1,8)-F(1,12) == F(1,24) and 12*15 == 180 and 180//18 == 10 and 5+10 == 15
assert 4*50 == 200 and 3*50 == 150 and 200*150 == 30000 and 30000//10000 == 3
assert 30*5//6 == 25 and 25*2//5 == 10 and 10-5 == 5 and 9300//31 == 300 and 300*9 == 2700 and 300*12 == 3600 and 300*10 == 3000
assert 90*1 == 90 and 36*360//90//1 == 144 and 54*360//144 == 135
assert 45*100//100 == 45 and 8000*45//100 == 3600 and 8000*25//100 == 2000 and 8000*20//100 == 1600 and 8000*10//100 == 800
assert [360*p//100 for p in (45,25,20,10)] == [162,90,72,36] and 1600*5//4 == 2000
assert F(1,20)+F(1,30)-F(1,60) == F(1,15) and 15*3 == 45 and F(45,15)+F(45,10) == F(15,2) and F(90,15) == 6 and F(90,F(15,2)) == 12
assert 350*6//7 == 300 and 300-250 == 50 and (2*3+4)*11 == 10*11 and (2*3+4*1) == 10 and (3+2*4) == 11
assert 36*32 == 1152 and 1152*3//4 == 864 and 864//16 == 54 and 54-36 == 18
assert 20*60 == 1200 and 2.4*100/60 == 4

WS = [
# ---------------- EASY ----------------
W("The ratio $36:48$ in its simplest form is:", 1, "(b) $3:4$. Divide both terms by the HCF 12. (1)", "E", opts=["$4:3$", "$3:4$", "$6:8$", "$12:16$"]),
W("If $3:5=12:x$, then $x$ is:", 1, "(c) 20. The multiplier is $12\\div3=4$, so $x=5\\times4=20$. (1)", "E", opts=["15", "17", "20", "36"]),
W("₹ 800 is divided between two friends in the ratio $3:5$. The larger share is:", 1, "(b) ₹ 500. One part $=800\\div8=100$; larger share $=5\\times100$. (1)", "E", opts=["₹ 300", "₹ 500", "₹ 600", "₹ 160"], wp=True),
W("If 6 pens cost ₹ 48, then 9 pens cost:", 1, "(c) ₹ 72. Cost per pen $=48\\div6=8$; $9\\times8=72$. (1)", "E", opts=["₹ 54", "₹ 64", "₹ 72", "₹ 96"], wp=True),
W("On a map, 1 cm represents 5 km. A distance of 4 cm on the map is actually:", 1, "(b) 20 km. $4\\times5=20$. (1)", "E", opts=["9 km", "20 km", "1.25 km", "45 km"], wp=True),
W("4 workers finish a job in 12 days. At the same rate, 6 workers will finish it in:", 1, "(a) 8 days. Total work $=4\\times12=48$ worker-days; $48\\div6=8$. (1)", "E", opts=["8 days", "18 days", "10 days", "16 days"], wp=True),
W("In a pie chart a sector has angle $90^\\circ$. It represents:", 1, "(b) $25\\%$ of the data. $\\frac{90}{360}=\\frac14$. (1)", "E", opts=["$10\\%$", "$25\\%$", "$50\\%$", "$90\\%$"]),
W("Find the ratio of 40 minutes to 2 hours in simplest form.", 2, "Convert: 2 hours $=120$ minutes (1). $40:120=1:3$ (1).", "E", wp=True),
W("Rice costs ₹ 60 per kg. Find the cost of 2.5 kg.", 2, "Cost is directly proportional to weight (1). $60\\times2.5=$ ₹ 150 (1).", "E", wp=True),
W("Two numbers are in the ratio $5:7$ and their sum is 96. Find the numbers.", 2, "One part $=96\\div12=8$ (1). Numbers $40$ and $56$ (1).", "E"),
W("True or false (give a reason): if two quantities are in inverse proportion, their product stays constant.", 1, "**True.** In inverse proportion, when one quantity is multiplied by $k$ the other is divided by $k$, so $x\\times y$ is unchanged (1).", "E"),
W("A car travels 180 km in 3 hours. At the same speed, how far will it go in 5 hours?", 2, "Speed $=60$ km/h (1). Distance $=60\\times5=300$ km (1).", "E", wp=True),
W("If $a:b=2:3$ and $b:c=3:4$, write $a:b:c$.", 2, "$b$ is already 3 in both ratios (1). $a:b:c=2:3:4$ (1).", "E"),
W("In a pie chart, a category is $30\\%$ of the data. What angle does its sector make at the centre?", 2, "$\\frac{30}{100}\\times360^\\circ$ (1) $=108^\\circ$ (1).", "E"),
W("On a map 1 cm stands for 2 km. Two towns are 7.5 cm apart on the map. Find the actual distance.", 2, "$7.5\\times2$ (1) $=15$ km (1).", "E", wp=True),
W("Asha and Bina share 60 sweets in the ratio $2:3$. How many does each get?", 2, "One part $=60\\div5=12$ (1). Asha $24$, Bina $36$ (1).", "E", wp=True),
W("8 men dig a trench in 15 days. How long will 10 men take, working at the same rate?", 2, "Work $=8\\times15=120$ man-days (1). Time $=120\\div10=12$ days (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("Two numbers are in the ratio $7:4$ and their difference is 18. Find the numbers.", 2, "Difference of parts $=3$, so one part $=18\\div3=6$ (1). Numbers $42$ and $24$ (1).", "M"),
W("Which ratio is greater, $3:4$ or $5:7$? Show how you decide.", 2, "Compare as fractions with a common denominator: $\\frac34=\\frac{21}{28}$ and $\\frac57=\\frac{20}{28}$ (1). So $3:4$ is greater (1).", "M"),
W("A 40 kg brass alloy has copper and zinc in the ratio $3:2$. Find the mass of each metal.", 2, "One part $=40\\div5=8$ kg (1). Copper $24$ kg, zinc $16$ kg (1).", "M", wp=True),
W("A tractor uses 18 litres of diesel to plough 3 acres. How much diesel is needed for 8 acres?", 2, "Diesel per acre $=6$ litres (1). $8\\times6=48$ litres (1).", "M", wp=True),
W("5 painters can paint a wall in 18 days. How long will 6 painters take?", 2, "Work $=5\\times18=90$ painter-days (1). $90\\div6=15$ days (1).", "M", wp=True),
W("A bus takes 4 hours at 60 km/h for a journey. How long will it take at 80 km/h?", 2, "Distance $=240$ km (1). Time $=240\\div80=3$ hours (1).", "M", wp=True),
W("Ravi says: ‘6 men finish a job in 10 days, so 12 men will take 20 days.’ What is wrong? Find the correct time.", 2, "More men means fewer days (inverse proportion), not more (1). Work $=60$ man-days; $60\\div12=5$ days (1).", "M"),
W("A class of 40 students has boys and girls in the ratio $3:5$. Find the number of boys and girls and how many more girls than boys.", 3, "One part $=40\\div8=5$ (1). Boys $15$, girls $25$ (1). Girls are $10$ more (1).", "M", wp=True),
W("Divide ₹ 36,000, the profit of a business, among three partners in the ratio $2:3:4$.", 3, "Total parts $=9$, one part $=36000\\div9=4000$ (1). Shares $8000$, $12000$ (1), $16000$ (1).", "M", wp=True),
W("If $a:b=2:3$ and $b:c=4:5$, find $a:b:c$. If $a+b+c=70$, find $a$, $b$ and $c$.", 3, "Make $b$ common: $a:b=8:12$, $b:c=12:15$, so $a:b:c=8:12:15$ (1). Parts $=35$, one part $=2$ (1). $16,\\;24,\\;30$ (1).", "M"),
W("A map has scale 1 cm : 5 km. A road is 18 km long. What is its length on the map? What actual distance does 6 cm on the map show?", 3, "Map length $=18\\div5=3.6$ cm (2). $6\\times5=30$ km (1).", "M", wp=True),
W("A hostel has food for 60 students for 24 days. How long will the same food last if there are only 40 students?", 3, "Food $=60\\times24=1440$ student-days (1). $1440\\div40$ (1) $=36$ days (1).", "M", wp=True),
W("One pipe fills a tank in 6 hours and another in 12 hours. How long will they take together?", 3, "In 1 hour they fill $\\frac16+\\frac1{12}=\\frac14$ of the tank (2). Time $=4$ hours (1).", "M", wp=True),
W("A father is 40 years old and his son is 10. Find the ratio of their ages now and after 10 years.", 3, "Now: $40:10=4:1$ (1). After 10 years: $50:20=5:2$ (1). The ratio changes because the same number is added to both ages, not multiplied (1).", "M", wp=True),
W("Decide whether $y$ is directly proportional, inversely proportional, or neither, to $x$: (i) $x=2,4,6,8$; $y=10,20,30,40$. (ii) $x=1,2,4,8$; $y=48,24,12,6$. (iii) $x=1,2,3,4$; $y=5,9,13,17$.", 3, "(i) $y\\div x=5$ always: direct (1). (ii) $xy=48$ always: inverse (1). (iii) neither $y\\div x$ nor $xy$ is constant: neither (1).", "M"),
W("A recipe for 4 persons needs 300 g flour. How much flour is needed for 10 persons? How many persons can be served with 1.2 kg?", 3, "Per person $=75$ g; 10 persons $=750$ g (1.5). $1200\\div75=16$ persons (1.5).", "M", wp=True),
W("In a pie chart of 120 students' favourite sports, the angles are Cricket $144^\\circ$, Football $72^\\circ$, Kabaddi $90^\\circ$ and Others $54^\\circ$. Find the number of students for each sport.", 3, "Number $=\\frac{\\text{angle}}{360}\\times120$ (1). Cricket $48$, Football $24$ (1), Kabaddi $30$, Others $18$ (1). Total $=120$.", "M", wp=True),
W("Monthly expenses of ₹ 24,000: food $30\\%$, rent $25\\%$, education $20\\%$, savings $15\\%$, other $10\\%$. Find the angle of each sector in a pie chart and the rent in rupees.", 3, "Angles: food $108^\\circ$, rent $90^\\circ$, education $72^\\circ$, savings $54^\\circ$, other $36^\\circ$ (2). Rent $=25\\%$ of $24000=$ ₹ 6000 (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Aman says: ‘5 pens cost ₹ 40 and 10 pens cost ₹ 80, so pens and cost are in inverse proportion because both change.’ Is he right? Explain using a constant.", 3, "He is wrong (1). Cost $\\div$ pens $=8$ in both cases, a constant, so the cost is **directly** proportional to the number of pens (1). In inverse proportion one quantity would fall as the other rises (1).", "H"),
W("If $x:y=3:4$, find the ratio $(2x+y):(x+2y)$.", 3, "Let $x=3k$, $y=4k$ (1). $2x+y=10k$ and $x+2y=11k$ (1). Ratio $=10:11$ (1).", "H"),
W("A tap fills a tank in 8 hours and a leak at the bottom empties the full tank in 12 hours. If both are open, how long does the tank take to fill?", 3, "Net rate $=\\frac18-\\frac1{12}=\\frac1{24}$ of the tank per hour (2). Time $=24$ hours (1).", "H", wp=True),
W("In a pie chart the sector for Maths has angle $90^\\circ$ and stands for 36 students. Find the total number of students and the angle for English if 54 students chose it.", 3, "$90^\\circ$ is $\\frac14$ of the circle, so total $=4\\times36=144$ (1). English angle $=\\frac{54}{144}\\times360^\\circ$ (1) $=135^\\circ$ (1).", "H", wp=True),
W("A model bus is 20 cm long and its scale is $1:60$. Find the real length of the bus in metres. If the real width is 2.4 m, find the width of the model.", 3, "Real length $=20\\times60=1200$ cm $=12$ m (2). Model width $=240\\div60=4$ cm (1).", "H", wp=True),
W("A cyclist covers a distance in 3 hours at 15 km/h. For the return journey he rides at 10 km/h. Find the time for the return and the average speed for the whole journey. Is it 12.5 km/h?", 4, "Distance $=45$ km (1). Return time $=4.5$ hours (1). Total distance $90$ km in $7.5$ hours, average $=12$ km/h (1). It is not 12.5 km/h, because more time is spent at the lower speed (1).", "H", wp=True),
W("A mixture of 30 litres has milk and water in the ratio $5:1$. How much water must be added to make the ratio $5:2$?", 4, "Milk $=25$ L, water $=5$ L (1). Milk stays 25 L; for $5:2$ water must be $10$ L (2). Add $5$ L (1).", "H", wp=True),
W("A school had 600 students with boys and girls in the ratio $7:5$. After some girls joined, the ratio became $7:6$. How many girls joined?", 4, "Boys $=350$, girls $=250$ (1). Boys unchanged, so new girls $=350\\times\\frac67=300$ (2). $300-250=50$ girls joined (1).", "H", wp=True),
W("Three friends share ₹ 9300 so that $A:B=3:4$ and $B:C=6:5$. Find the ratio $A:B:C$ and each share.", 4, "Make $B$ equal: $A:B=9:12$, $B:C=12:10$, so $A:B:C=9:12:10$ (1). Total parts $=31$, one part $=9300\\div31=300$ (1). Shares $2700,\\;3600,\\;3000$ (2).", "H", wp=True),
W("12 men can finish a job in 20 days. After 5 days, 6 more men join them. In how many days in all is the job completed?", 4, "Total work $=12\\times20=240$ man-days (1). After 5 days, done $=60$, left $=180$ (1). With 18 men: $180\\div18=10$ days (1). Total $=5+10=15$ days (1).", "H", wp=True),
W("A rectangular field appears as 4 cm by 3 cm on a map where 1 cm stands for 50 m. Find the real length, breadth, area in hectares (1 hectare = 10,000 m²) and the real length of the diagonal.", 4, "Real sides $200$ m and $150$ m (1). Area $=30000$ m² $=3$ hectares (1). Diagonal on map $=5$ cm (1), real diagonal $=250$ m (1).", "H", wp=True),
W("Pipe A fills a tank in 20 minutes, pipe B fills it in 30 minutes and an outlet C empties it in 60 minutes. If all three are open together, in how many minutes is the empty tank filled?", 4, "Net rate $=\\frac1{20}+\\frac1{30}-\\frac1{60}$ (1) $=\\frac{3+2-1}{60}=\\frac1{15}$ (2). Time $=15$ minutes (1).", "H", wp=True),
W("**Case study (road work).** A contractor puts 36 labourers on a road to be built in 24 days. After 8 days only $\\frac14$ of the road is done. How many more labourers must be added to finish on time?", 5, "Whole job $=36\\times32=1152$ labourer-days (since $\\frac14$ took $36\\times8=288$) (2). Left $=\\frac34$ of the job $=864$ labourer-days in 16 days (1). Labourers needed $=864\\div16=54$ (1). Add $54-36=18$ labourers (1).", "H", wp=True),
W("**Case study (tourists).** In a year 8000 tourists visited four places in the proportions Jaipur $45\\%$, Udaipur $25\\%$, Jaisalmer $20\\%$, others $10\\%$. Find the number of tourists at each place and the sector angle for each in a pie chart. If Jaisalmer's visitors increase by $25\\%$ next year, how many visit it?", 5, "Numbers: $3600,\\;2000,\\;1600,\\;800$ (2). Angles: $162^\\circ,\\;90^\\circ,\\;72^\\circ,\\;36^\\circ$ (2). Jaisalmer next year $=1600\\times1.25=2000$ (1).", "H", wp=True),
]

_o = _old(12)
_i = max(i for i, b in enumerate(_o["blocks"]) if b[0] == "h2")
_pre, _tail = _o["blocks"][:_i], _o["blocks"][_i:]
_extra = [
 ("h2", "Key Ideas and Formulae"),
 ("note", "FORMULA", "Ratio a : b = a ÷ b.  Equal ratios: a : b = c : d means ad = bc.  Dividing a total T in the ratio p : q: first share = T × p ÷ (p + q), second share = T × q ÷ (p + q).  Map scale: actual distance = map distance × scale."),
 ("note", "FORMULA", "Direct proportion: y ÷ x is constant (y₁ ÷ x₁ = y₂ ÷ x₂).  Inverse proportion: x × y is constant (x₁y₁ = x₂y₂).  Pie chart: sector angle = (value ÷ total) × 360° = per cent × 3.6°."),
 ("table", ["Feature", "Direct proportion", "Inverse proportion"], [["If one doubles", "the other doubles", "the other halves"], ["Constant quantity", "ratio y ÷ x", "product x × y"], ["Typical examples", "cost and quantity, distance and time at fixed speed", "workers and days, speed and time for a fixed distance"], ["Method", "unit rate: find the value of one", "total work: find workers × days, then divide"], ["Check", "table values y ÷ x all equal", "table values x × y all equal"]]),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Joining two ratios"),
 ("steps", [("Question", "a : b = 2 : 3 and b : c = 4 : 5. Find a : b : c, and the three numbers if their sum is 70."), ("Make b equal", "Multiply the first ratio by 4 and the second by 3: a : b = 8 : 12, b : c = 12 : 15."), ("Combine", "a : b : c = 8 : 12 : 15."), ("Share", "8 + 12 + 15 = 35 parts, one part = 2, so the numbers are **16, 24, 30**.")]),
 ("h3", "Example 2 — Reading a map"),
 ("steps", [("Question", "A map shows 1 cm for 5 km. A road is 18 km long. Its length on the map?"), ("Method", "Map length = actual ÷ scale = 18 ÷ 5."), ("Answer", "**3.6 cm**. Conversely 6 cm on the map is 6 × 5 = 30 km.")]),
 ("h3", "Example 3 — Inverse proportion (days and workers)"),
 ("steps", [("Question", "A hostel has food for 60 students for 24 days. How long will it last for 40 students?"), ("Total food", "60 × 24 = 1440 student-days."), ("Answer", "1440 ÷ 40 = **36 days**.")]),
 ("h3", "Example 4 — Working together"),
 ("steps", [("Question", "A tap fills a tank in 8 hours; a leak empties it in 12 hours. Both are open."), ("Rates", "Tap fills 1/8 per hour, leak removes 1/12 per hour."), ("Net rate", "1/8 − 1/12 = 3/24 − 2/24 = 1/24 per hour."), ("Answer", "The tank fills in **24 hours**.")]),
 ("h3", "Example 5 — Pie chart angles"),
 ("steps", [("Data", "Monthly expenses ₹ 24,000: food 30%, rent 25%, education 20%, savings 15%, other 10%."), ("Angles", "Per cent × 3.6°: 108°, 90°, 72°, 54°, 36°."), ("Check", "108 + 90 + 72 + 54 + 36 = 360°, so the angles are consistent. Rent = 25% of 24,000 = **₹ 6000**.")]),
 ("h3", "Example 6 — Ratio that changes"),
 ("steps", [("Question", "A school of 600 has boys : girls = 7 : 5. After some girls join the ratio becomes 7 : 6. How many joined?"), ("Now", "Boys = 350, girls = 250."), ("Later", "Boys stay 350, so girls = 350 × 6 ÷ 7 = 300."), ("Answer", "300 − 250 = **50 girls**.")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["‘in the ratio p : q’", "total parts = p + q; one part = total ÷ (p + q)", "₹ 36,000 in 2 : 3 : 4, one part = ₹ 4000"],
  ["‘scale 1 cm : 5 km’", "map × 5 = actual; actual ÷ 5 = map", "4 cm on the map = 20 km"],
  ["‘more men, fewer days’", "inverse: men × days = constant", "5 painters × 18 days = 6 painters × 15 days"],
  ["‘same rate’, ‘price per kg’", "direct: find the unit rate first", "₹ 60 per kg, 2.5 kg = ₹ 150"],
  ["‘fills in … hours’, ‘empties in … hours’", "rate = 1 ÷ time; add filling rates, subtract emptying rates", "1/20 + 1/30 − 1/60 = 1/15 per minute"],
  ["‘after … the ratio becomes’", "the part that does not change gives the new part", "boys stay 350 while girls change"],
  ["average speed for a to-and-fro journey", "total distance ÷ total time, never the mean of the two speeds", "15 km/h and 10 km/h give 12 km/h, not 12.5"]]),
 ("note", "REMEMBER", "First decide **direct or inverse**: ask ‘if one quantity doubles, what happens to the other?’ Then choose the unit-rate method (direct) or the total-work method (inverse)."),
 ("h2", "Likely Exam Questions"),
 ("qa", [("Divide ₹ 9300 among A, B and C if A : B = 3 : 4 and B : C = 6 : 5.", "A : B : C = 9 : 12 : 10, 31 parts of ₹ 300: ₹ 2700, ₹ 3600, ₹ 3000."),
  ("12 men finish a job in 20 days. After 5 days 6 more men join. When does it finish?", "Left = 12 × 15 = 180 man-days; 18 men take 10 days; total 15 days."),
  ("How is a pie chart sector angle found?", "Angle = (value ÷ total) × 360°; the angles of all sectors add up to 360°."),
  ("Two pipes fill a tank in 20 and 30 minutes and an outlet empties it in 60. Time with all open?", "Net rate 1/20 + 1/30 − 1/60 = 1/15, so 15 minutes."),
  ("How do you tell direct from inverse proportion from a table?", "Check y ÷ x (direct) or x × y (inverse) for every pair; the constant one decides."),
  ("A model of length 20 cm has scale 1 : 60. Real length?", "20 × 60 = 1200 cm = 12 m.")]),
]
CH = dict(_o, num=10, blocks=_pre + _extra + _tail,
          takeaways=_o["takeaways"] + ["For ratios that change (after people join or leave), find the part that stays the same and work from it.", "Pipes and workers: convert each time to a **rate** (1 ÷ time), add the helpers, subtract the hinderers.", "The average speed of a return journey is **total distance ÷ total time**, not the mean of the two speeds."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
