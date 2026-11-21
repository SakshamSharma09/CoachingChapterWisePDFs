"""Class 9 Maths Ch 10 - How Quantities Combine (Understanding Data): worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch10"

def _old(n):
    d = "c9_maths1" if n < 9 else "c9_maths2"
    p = Path(__file__).resolve().parents[1] / "rn_work" / d / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def close(x, y): return abs(x - y) < 1e-9
def wm(*pairs): return sum(v * w for v, w in pairs) / sum(w for v, w in pairs)
assert close(wm((60, 10), (80, 10)), 70) and close(wm((50, 20), (60, 30)), 56) and close(wm((70, 30), (80, 20)), 74) and close(wm((300, 2), (400, 3)), 360)
assert close(wm((70, 40), (80, 60)), 76) and close(wm((40, 4), (50, 6)), 46) and close(wm((10, 200), (20, 200)), 15) and close(wm((60, 2), (80, 3)), 72)
assert close(12*25+38, 338) and close(338/13, 26) and close(54+36+30, 120) and close(54/120, .45) and close(36/120, .3)
assert close(wm((64, 25), (72, 15)), 67) and close(40*62-25*56, 1080) and close(1080/15, 72) and close(wm((8, 300), (18, 200)), 12)
assert close(0.3*150+0.1*150, 0.2*300) and close(15+0.3*150, 0.2*(150+150)) and close(20*0.15, 3) and close(3/0.10, 30)
assert close(10*42-9*40, 60) and close((12*45+71)/13, 47) and close(wm((72, 2), (65, 3), (80, 5)), 73.9) and abs((72+65+80)/3-72.33) < .01
assert close(wm((40, 30), (60, 10)), 45) and close(wm((75, 8), (50, 12)), 60) and close((1.8+2.2+2.6+3.4)/4, 2.5) and close(2.5*12, 30)
assert close(wm((5, 3), (4, 2), (1, 1)), 4) and close(wm((60, 30), (65, 40), (70, 30)), 65) and close(wm((48, 20), (58, 30)), 54)
assert abs(wm((60, 30), (65, 20), (70, 50)) - 66.5) < 1 and close((6600-1800-3500)/20, 65)
assert close(0.4*300+0.1*600, 0.2*900) and close(0.2*30, 6) and close(6/0.12, 50) and close(1.8/0.12, 15) and close(120+120, 0.75*(200+120))
assert close(0.2*90+0.3*70+0.5*82, 80) and close(wm((60, 40), (80, 10)), 64) and close(wm((55, 10), (75, 40)), 71) and wm((60, 40), (55, 10))
assert close(0.4*80000, 32000) and close(0.35*80000, 28000) and close(0.25*80000, 20000) and close(0.4*200000, 80000) and close(0.3*200000, 60000)
assert close(wm((2, 10), (3, 6), (5, 4)), 2.9) and close(2.9*20, 58) and close(58*150, 8700)
assert close((8*35-16-24)/6, 40) and close((240+45+55)/8, 42.5) and close(40*2 + 60*3, 52*5)
assert close(100*.1+200*.25+200*.2, 100) and close(100/500, .2) and close(100/.16, 625) and close(625-500, 125)
assert close(500*.2, 100) and close(200*.1, 20) and close(500*.8, 400) and close(200*.9, 180) and close(20000*.45, 9000) and close(50000*.3, 15000)
assert close((10*10+30*10), 400) and close((5*72), 360) and close(450-360, 90) and close((360-90)+2*90, 450) and close(450/6, 75)

WS = [
# ---------------- EASY ----------------
W(r"10 students have an average of 60 marks and another 10 students have an average of 80 marks. The average of all 20 students is:", 1, r"(b) 70. The groups are of equal size, so $\frac{60+80}{2}=70$ (or $\frac{600+800}{20}=70$). (1)", "E", opts=["65", "70", "75", "140"]),
W(r"20 boys have an average of 50 marks and 30 girls have an average of 60 marks. The average of all 50 students is:", 1, r"(c) 56. Total $=20\times50+30\times60=1000+1800=2800$; $2800\div50=56$. (1)", "E", opts=["55", "58", "56", "110"]),
W(r"200 mL of a 10% sugar solution is mixed with 200 mL of a 20% sugar solution. The concentration of the mixture is:", 1, r"(a) 15%. Equal quantities, so the concentration is midway between 10% and 20%. (1)", "E", opts=["15%", "30%", "10%", "20%"]),
W(r"In a 100% stacked bar chart, you can:", 1, r"(c) compare the shares of the parts within a bar. Every bar has the same length, so actual amounts across bars cannot be compared. (1)", "E",
  opts=["read the actual totals of every bar", "compare actual amounts of one part across bars", "compare the shares of the parts within a bar", "find the average of the bars"]),
W(r"The average of 5 numbers is 12. Their sum is:", 1, r"(d) 60. Sum $=$ average $\times$ number of values $=12\times5=60$. (1)", "E", opts=["17", "7", "2.4", "60"]),
W(r"Mixing a 10% solution with a 30% solution can give a concentration of:", 1, r"(b) 18%. The mixture's concentration lies between 10% and 30%; 35% and 8% lie outside, and 18% is inside the range. (1)", "E", opts=["35%", "18%", "8%", "40%"]),
W(r"The average of 12 numbers is 25. A 13th number, 38, is added. Find the new average.", 2, r"Old sum $=12\times25=300$ (1). New sum $=338$, new average $=338\div13=26$ (1).", "E"),
W(r"Class A has 30 students with average 70 marks and class B has 20 students with average 80 marks. Find the average of all 50 students.", 2, r"Total $=30\times70+20\times80=2100+1600=3700$ (1). Average $=3700\div50=74$ (1).", "E", wp=True),
W(r"A shopkeeper mixes 2 kg of tea at ₹ 300 per kg with 3 kg of tea at ₹ 400 per kg. Find the cost of 1 kg of the mixture.", 2, r"Cost of the mixture $=2\times300+3\times400=600+1200=$ ₹ 1,800 (1). Per kg $=1800\div5=$ ₹ 360 (1).", "E", wp=True),
W(r"In a school, the class test carries weight 40% and the annual exam weight 60%. Anita scores 70 in the test and 80 in the exam. Find her weighted score.", 2, r"$\frac{40\times70+60\times80}{100}=\frac{2800+4800}{100}$ (1) $=76$ (1).", "E", wp=True),
W(r"A batsman's average in 4 matches is 40 runs and in the next 6 matches is 50 runs. Find his average over all 10 matches.", 2, r"Total runs $=4\times40+6\times50=160+300=460$ (1). Average $=460\div10=46$ (1).", "E", wp=True),
W(r"True or false (give a reason or working): if a group of 10 students has average 20 and a group of 30 students has average 40, the combined average is 30.", 2, r"**False.** The groups are not equal, so the average of the averages is wrong. Combined $=\frac{10\times20+30\times40}{40}=\frac{1400}{40}=35$ (2).", "E"),
W(r"A jar holds 200 mL of 10% juice and another holds 200 mL of 20% juice. They are poured together. What is the percentage of juice in the mixture, and why is it midway?", 2, r"Juice $=20+40=60$ mL in 400 mL, i.e. 15% (1). The quantities are equal, so the two concentrations carry the same weight and the result is midway (1).", "E", wp=True),
W(r"A 50 mL mixture contains 10 mL of acid. Find the concentration of acid. How much acid is in 200 mL of the same mixture?", 2, r"Concentration $=\frac{10}{50}=20\%$ (1). In 200 mL: $0.2\times200=40$ mL (1).", "E", wp=True),
W(r"A student scores 60 in internals (weight 2) and 80 in the final exam (weight 3). Find the weighted average.", 2, r"$\frac{2\times60+3\times80}{2+3}=\frac{120+240}{5}$ (1) $=72$ (1).", "E"),
W(r"**Stacked bar data.** A bakery's monthly sales (in ₹ thousands) are: bread 54, cake 36, biscuits 30. Find the total length of its stacked bar and the percentage share of each item.", 2, r"Total $=54+36+30=120$ (thousand) (0.5). Shares: bread $\frac{54}{120}=45\%$, cake $30\%$, biscuits $25\%$ (1.5).", "E", wp=True),
W(r"True or false (give a reason): in a 100% stacked bar chart, a longer segment always means a larger amount.", 2, r"**False.** The segment shows a share of its own bar's total. A longer segment in a bar with a small total may be a smaller amount than a shorter segment in a bar with a big total (2).", "E"),
# ---------------- MEDIUM ----------------
W(r"25 students have an average of 64 and 15 students have an average of 72. Find the average of all 40.", 2, r"$\frac{25\times64+15\times72}{40}=\frac{1600+1080}{40}$ (1) $=\frac{2680}{40}=67$ (1).", "M"),
W(r"The average marks of 40 students are 62. The average of 25 of them is 56. Find the average of the other 15 students.", 3, r"Total of 40 $=40\times62=2480$ (1). Total of 25 $=25\times56=1400$ (1). Others' total $=1080$, average $=1080\div15=72$ (1).", "M", wp=True),
W(r"300 mL of an 8% salt solution is mixed with 200 mL of an 18% salt solution. Find the concentration of the mixture.", 3, r"Salt $=0.08\times300+0.18\times200=24+36=60$ mL (2). Concentration $=\frac{60}{500}=12\%$ (1).", "M"),
W(r"How much 30% syrup must be added to 150 mL of 10% syrup to get a 20% syrup?", 3, r"Let $y$ mL of 30% be added: $\frac{15+0.3y}{150+y}=0.2$ (1). $15+0.3y=30+0.2y$ (1). $0.1y=15$, $y=150$ mL (1). Check: equal amounts give the midpoint 20%.", "M", wp=True),
W(r"A chemist has 20 L of a 15% acid solution. How much water must be added to make it a 10% solution?", 3, r"Acid $=0.15\times20=3$ L, which stays the same (1). New volume $=3\div0.10=30$ L (1). Water to be added $=30-20=10$ L (1).", "M", wp=True),
W(r"The average of 9 numbers is 40. When a 10th number is added, the average becomes 42. Find the 10th number.", 3, r"Sum of 9 $=360$ (1). Sum of 10 $=420$ (1). 10th number $=420-360=60$ (1).", "M"),
W(r"After 12 innings a batsman's average is 45 runs. In his 13th innings he scores 71. Find his new average.", 3, r"Runs in 12 innings $=12\times45=540$ (1). After 13 innings $=540+71=611$ (1). New average $=611\div13=47$ (1).", "M", wp=True),
W(r"Zoya's marks and weights are: unit tests 72 (weight 2), half-yearly 65 (weight 3), annual 80 (weight 5). Find the weighted average and compare it with the simple average of the three marks.", 3, r"Weighted $=\frac{144+195+400}{10}=\frac{739}{10}=73.9$ (2). Simple average $=\frac{72+65+80}{3}\approx72.3$; it is lower because the highest mark carries the greatest weight (1).", "M", wp=True),
W(r"Sonu says: 'A class has 30 boys with average 40 marks and 10 girls with average 60 marks, so the class average is $\frac{40+60}{2}=50$.' Find his mistake and the correct average.", 2, r"He ignored that the groups are of different sizes (1). Correct: $\frac{30\times40+10\times60}{40}=\frac{1800}{40}=45$ (1).", "M"),
W(r"A jeweller melts an 8 g ring that is 75% gold with a 12 g ring that is 50% gold. What percentage of the new piece is gold?", 3, r"Gold $=0.75\times8+0.5\times12=6+6=12$ g (2). Total mass 20 g, so $\frac{12}{20}=60\%$ (1).", "M", wp=True),
W(r"To find the mean depth of an irregular pit, the depths measured at four places are 1.8 m, 2.2 m, 2.6 m and 3.4 m. Find the mean depth. If the pit's surface area is 12 m², estimate its volume.", 3, r"Mean depth $=\frac{1.8+2.2+2.6+3.4}{4}=\frac{10}{4}=2.5$ m (2). Volume $\approx12\times2.5=30$ m³ (1).", "M", wp=True),
W(r"A restaurant is rated: food 5 (weight 3), service 4 (weight 2), ambience 1 (weight 1). Find the weighted rating.", 3, r"$\frac{3\times5+2\times4+1\times1}{3+2+1}$ (2) $=\frac{24}{6}=4$ (1).", "M"),
W(r"The number of boys and girls in three sections of Class 9: 9A (18, 22), 9B (24, 16), 9C (20, 20). (i) Find each section's total. (ii) Find the share of girls in each section. (iii) Which section has the highest share of girls?", 3, r"(i) 40, 40, 40 (1). (ii) 9A: $\frac{22}{40}=55\%$; 9B: $40\%$; 9C: $50\%$ (1.5). (iii) 9A (0.5).", "M", wp=True),
W(r"In a 100% stacked bar, bread is 45% of Bakery A's sales and 30% of Bakery B's sales. A's total sales are ₹ 20,000 and B's are ₹ 50,000. Which bakery sold more bread, in rupees?", 3, r"A: $0.45\times20000=$ ₹ 9,000 (1). B: $0.30\times50000=$ ₹ 15,000 (1). B sold more bread, though its percentage is smaller; the 100% chart hides totals (1).", "M", wp=True),
W(r"Can mixing a 10% solution and a 20% solution give a 25% solution? Explain. What is the concentration if 300 mL of the 10% solution is mixed with 100 mL of the 20% solution?", 3, r"No: the mixture's concentration lies between the two concentrations, 10% and 20% (1). Mixture: $\frac{30+20}{400}=\frac{50}{400}=12.5\%$ (2), closer to 10% because there is more of it.", "M"),
W(r"A school has three sections: 30 students with average 60, 40 students with average 65 and 30 students with average 70. Find the average of the whole class of 100.", 3, r"Total $=1800+2600+2100=6500$ (2). Average $=6500\div100=65$ (1).", "M", wp=True),
W(r"A dairy mixes 20 L of milk costing ₹ 48 per litre with 30 L costing ₹ 58 per litre. Find the cost of 1 litre of the mixture.", 3, r"Cost $=20\times48+30\times58=960+1740=$ ₹ 2,700 (2). Per litre $=2700\div50=$ ₹ 54 (1).", "M", wp=True),
W(r"A factory owner compares three factories of very different sizes using a 100% stacked bar of the share of cotton in the cloth they produce. Why is the 100% stacked bar a better choice than an ordinary stacked bar for comparing the cotton share? What can it not tell you?", 3, r"All bars have the same length, so the cotton shares can be compared directly even though the totals differ (1.5). It cannot tell the actual quantities of cotton or the sizes of the factories (1.5).", "M", wp=True),
W(r"The average mark of 10 students is 52. A student who scored 70 leaves the group. Find the average of the remaining 9 students.", 3, r"Total of 10 $=520$ (1). Remaining total $=520-70=450$ (1). Average $=450\div9=50$ (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"Classes A, B and C have 30, 20 and 50 students. The averages of A and C are 60 and 70, and the average of all 100 students is 66. Find the average of class B.", 4, r"Total $=100\times66=6600$ (1). A $=1800$, C $=3500$ (1). B's total $=6600-1800-3500=1300$ (1). B's average $=1300\div20=65$ (1).", "H", wp=True),
W(r"How many mL of a 40% acid solution must be added to 600 mL of a 10% acid solution to get a 20% solution?", 4, r"Let $y$ mL be added: $\frac{60+0.4y}{600+y}=0.2$ (1). $60+0.4y=120+0.2y$ (1). $0.2y=60$ (1). $y=300$ mL; check: $\frac{60+120}{900}=20\%$ (1).", "H", wp=True),
W(r"A tank has 30 L of a 20% solution. (i) How much water must be added to make it a 12% solution? (ii) How much of this 12% solution contains 1.8 L of solute?", 4, r"(i) Solute $=6$ L, unchanged (0.5). New volume $=6\div0.12=50$ L (1), water $=20$ L (0.5). (ii) $\frac{1.8}{0.12}=15$ L (2).", "H", wp=True),
W(r"A jeweller has 200 g of an alloy that is 60% gold. How much pure gold must be added to make the alloy 75% gold? What karat is a 75% gold alloy (24 karat is pure gold)?", 5, r"Gold present $=120$ g. Add $y$ g of pure gold: $\frac{120+y}{200+y}=0.75$ (2). $120+y=150+0.75y$ (1). $0.25y=30$, $y=120$ g (1). Karat $=0.75\times24=18$ karat (1).", "H", wp=True),
W(r"A final grade is 20% assignment, 30% mid-term and 50% final exam. Neeraj scored 90 in the assignment and 70 in the mid-term. What must he score in the final exam to get an overall 80?", 4, r"$0.2\times90+0.3\times70+0.5x=80$ (1). $18+21+0.5x=80$ (1). $0.5x=41$ (1). $x=82$ (1).", "H", wp=True),
W(r"**Averages can mislead.** School X has 40 boys (average 60) and 10 girls (average 80). School Y has 10 boys (average 55) and 40 girls (average 75). (i) Find each school's overall average. (ii) Compare the boys' averages and the girls' averages. (iii) Explain why School Y has the higher overall average although X is better in each group.", 4, r"(i) X: $\frac{2400+800}{50}=64$; Y: $\frac{550+3000}{50}=71$ (1.5). (ii) Boys: X 60 against Y 55; girls: X 80 against Y 75; X is higher in both groups (1). (iii) Y has 40 of its 50 students from the higher-scoring group (girls), i.e. the weights differ, which raises its overall average (1.5).", "H", wp=True),
W(r"The 100% stacked bars of two shops' sales show: Shop P (total ₹ 80,000): fruit 40%, vegetables 35%, dairy 25%. Shop Q (total ₹ 2,00,000): fruit 30%, vegetables 30%, dairy 40%. (i) Find each shop's sales in rupees by item. (ii) Which shop sold more dairy and by how much? (iii) Why could the chart alone not show this?", 4, r"(i) P: fruit 32,000, vegetables 28,000, dairy 20,000; Q: fruit 60,000, vegetables 60,000, dairy 80,000 (2). (ii) Q sold more dairy: $80000-20000=$ ₹ 60,000 more (1). (iii) A 100% bar shows only shares; the totals (₹ 80,000 and ₹ 2,00,000) are needed (1).", "H", wp=True),
W(r"**Case study (Brahmagupta's pit).** A pit has three zones: Zone 1 of area 10 m² and depth 2 m, Zone 2 of area 6 m² and depth 3 m, Zone 3 of area 4 m² and depth 5 m. (i) Find the mean depth, using the areas as weights. (ii) Find the volume of earth removed. (iii) Find the cost of filling the pit at ₹ 150 per m³.", 5, r"(i) Mean depth $=\frac{10\times2+6\times3+4\times5}{10+6+4}=\frac{58}{20}=2.9$ m (2). (ii) Volume $=20\times2.9=58$ m³ (the sum of area times depth for each zone) (1.5). (iii) Cost $=58\times150=$ ₹ 8,700 (1.5).", "H", wp=True),
W(r"The average of 8 numbers is 35. Two of the numbers, 16 and 24, are removed. (i) Find the average of the remaining six. (ii) Two new numbers, 45 and 55, are then added. Find the average of the eight numbers now.", 4, r"(i) Sum of 8 $=280$; remaining sum $=280-40=240$; average $=240\div6=40$ (2). (ii) New sum $=240+100=340$; average $=340\div8=42.5$ (2).", "H"),
W(r"Two varieties of rice cost ₹ 40 per kg and ₹ 60 per kg. In what ratio should they be mixed so that the mixture can be sold at ₹ 52 per kg without profit or loss? Check with 5 kg of the mixture.", 4, r"Let $x$ kg of ₹ 40 and $y$ kg of ₹ 60: $40x+60y=52(x+y)$ (1). $8y=12x$, so $x:y=2:3$ (2). Check: 2 kg and 3 kg: $80+180=260=52\times5$ ✓ (1).", "H", wp=True),
W(r"Three solutions are mixed: 100 mL of 10%, 200 mL of 25% and 200 mL of 20%. (i) Find the concentration of the mixture. (ii) How much water must be added to dilute it to 16%?", 4, r"(i) Solute $=10+50+40=100$ mL in 500 mL, so 20% (2). (ii) New volume $=100\div0.16=625$ mL; water $=625-500=125$ mL (2).", "H", wp=True),
W(r"School A (500 students) shows 80% pass and 20% fail on a 100% stacked bar; School B (200 students) shows 90% pass and 10% fail. (i) Find the number of students who passed and failed in each school. (ii) A student says 'B has more passes because 90% is bigger than 80%.' Is he right? Explain.", 4, r"(i) A: 400 pass, 100 fail; B: 180 pass, 20 fail (2). (ii) No: A has 400 passes against 180 (1). A percentage compares shares, not numbers; the totals differ (1).", "H", wp=True),
W(r"Two groups have $n$ and $m$ values with averages $a$ and $b$, where $a<b$. Show that the combined average is greater than $a$ and less than $b$. Test it with $n=3$, $a=10$, $m=2$, $b=20$.", 3, r"Combined $=\frac{an+bm}{n+m}$. Then $\frac{an+bm}{n+m}-a=\frac{m(b-a)}{n+m}>0$ and $b-\frac{an+bm}{n+m}=\frac{n(b-a)}{n+m}>0$ (2). Test: $\frac{30+40}{5}=14$, and $10<14<20$ (1).", "H"),
W(r"A student has 5 test scores with average 72. When the last test counts double, the weighted average is 75. Find the last score and the sum of the first four scores.", 4, r"Total of 5 $=360$ (1). Let the last score be $x$ and the first four sum to $S$: $S+x=360$ and $\frac{S+2x}{6}=75$ so $S+2x=450$ (2). Subtract: $x=90$ and $S=270$ (1).", "H", wp=True),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(10)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "10.6 Working Rules and Derivations"),
 ("h3", "Why the combined average is (an + bm) ÷ (n + m)"),
 ("p", "Average = total ÷ number of values, so total = average × number. Group 1 total = an, group 2 total = bm. All values together: total an + bm, count n + m. Hence the combined average is (an + bm) ÷ (n + m)."),
 ("h3", "The combined average lies between a and b"),
 ("p", "Take a &lt; b. Then (an + bm)/(n + m) − a = m(b − a)/(n + m) &gt; 0 and b − (an + bm)/(n + m) = n(b − a)/(n + m) &gt; 0. So a &lt; combined average &lt; b. It is nearer the average of the **larger** group, because larger weights pull harder."),
 ("table", ["Question type", "Method", "Example"], [
  ["Combine two groups", "(an + bm) ÷ (n + m)", "30 × 70 + 20 × 80 over 50 = 74"],
  ["One group's average missing", "total of all − total of known group, then divide", "40 × 62 − 25 × 56 = 1,080; ÷ 15 = 72"],
  ["Add one value x", "new average = (n × a + x) ÷ (n + 1)", "12 innings avg 45, then 71: 611 ÷ 13 = 47"],
  ["Remove a value", "(n × a − x) ÷ (n − 1)", "10 students avg 52, one with 70 leaves: 450 ÷ 9 = 50"],
  ["Mixtures", "solute = Σ (quantity × concentration), divide by total quantity", "300 mL of 8% + 200 mL of 18% = 12%"],
  ["Dilution", "solute is unchanged; new volume = solute ÷ new concentration", "3 L solute: 3 ÷ 0.10 = 30 L, add 10 L water"]]),
 ("h2", "10.7 Worked Examples"),
 ("h3", "Example 1 — Combining unequal groups"),
 ("steps", [("Class A: 30 students, average 70. Class B: 20 students, average 80", "Totals: 30 × 70 = 2,100 and 20 × 80 = 1,600."), ("Add", "3,700 marks for 50 students."), ("Average", "3,700 ÷ 50 = 74. The simple average 75 is wrong because A is larger.")]),
 ("h3", "Example 2 — Finding a missing group average"),
 ("steps", [("40 students average 62; 25 of them average 56", "Total of 40 = 2,480; total of 25 = 1,400."), ("The other 15", "2,480 − 1,400 = 1,080."), ("Their average", "1,080 ÷ 15 = 72.")]),
 ("h3", "Example 3 — Mixture with an unknown quantity"),
 ("steps", [("How much 40% acid to add to 600 mL of 10% to get 20%?", "(60 + 0.4y) ÷ (600 + y) = 0.2."), ("Solve", "60 + 0.4y = 120 + 0.2y, so 0.2y = 60 and y = 300 mL."), ("Check", "Acid = 60 + 120 = 180 mL in 900 mL = 20%.")]),
 ("h3", "Example 4 — Alloy with pure gold added"),
 ("steps", [("200 g of 60% gold alloy has 120 g gold", "Add y g of pure gold: (120 + y) ÷ (200 + y) = 0.75."), ("Solve", "120 + y = 150 + 0.75y, so y = 120 g."), ("Karat", "75% of 24 = 18 karat; 16 varṇa = 100% pure gold.")]),
 ("h3", "Example 5 — Weighted marks and the mark needed"),
 ("steps", [("Weights 20%, 30%, 50%; scores 90, 70 and x; target 80", "0.2 × 90 + 0.3 × 70 + 0.5x = 80."), ("Simplify", "18 + 21 + 0.5x = 80, so 0.5x = 41."), ("Answer", "x = 82.")]),
 ("h3", "Example 6 — Brahmagupta's pit"),
 ("steps", [("Zones: 10 m² at 2 m, 6 m² at 3 m, 4 m² at 5 m", "Use the areas as weights."), ("Mean depth", "(20 + 18 + 20) ÷ 20 = 2.9 m."), ("Volume", "20 × 2.9 = 58 m³; cost at ₹150 per m³ = ₹8,700.")]),
 ("h3", "Example 7 — Reading a 100% stacked bar"),
 ("steps", [("Bread is 45% of Bakery A (total ₹20,000) and 30% of Bakery B (total ₹50,000)", "A: 0.45 × 20,000 = ₹9,000. B: 0.30 × 50,000 = ₹15,000."), ("Which sold more bread?", "B, even though its share is smaller."), ("Lesson", "A 100% bar compares shares, not amounts; get the totals before comparing amounts.")]),
 ("h2", "10.8 Averages that Mislead"),
 ("p", "An overall average depends on both the group averages and the **group sizes**. A school can have higher averages in every group yet a lower overall average when its groups have different proportions."),
 ("table", ["", "Boys (number, average)", "Girls (number, average)", "Overall"], [["School X", "40 boys, 60", "10 girls, 80", "(2,400 + 800) ÷ 50 = 64"], ["School Y", "10 boys, 55", "40 girls, 75", "(550 + 3,000) ÷ 50 = 71"]]),
 ("note", "IMPORTANT", "School X beats School Y among boys (60 &gt; 55) and among girls (80 &gt; 75), yet Y's overall average is higher, because most of Y's students are girls, the higher-scoring group. Always **split the data** into groups before drawing conclusions from one overall number."),
 ("h2", "10.9 Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["‘average of the whole class’", "total ÷ number of students", "(Σ group average × group size) ÷ total size"],
  ["‘percent weight / counts double’", "weights 20 : 30 : 50 or 1 : 1 : 2", "last test counts twice: weights 1, 1, 1, 1, 2"],
  ["‘mixed together’", "weighted mean with quantities as weights", "300 mL of 8% + 200 mL of 18%"],
  ["‘water is added’", "solute fixed, volume increases", "20 L of 15% becomes 30 L of 10%"],
  ["‘pure gold added’", "the added part has concentration 100%", "(120 + y) ÷ (200 + y) = 0.75"],
  ["‘ratio in which to mix’", "set up weighted-mean equation, solve for the ratio", "₹40 and ₹60 rice to sell at ₹52: ratio 2 : 3"],
  ["‘share on a 100% bar’", "percentage × that bar's total gives amount", "45% of ₹20,000 = ₹9,000"]]),
 ("h2", "10.10 Common Mistakes"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["Average of 70 and 80 for groups of 30 and 20 = 75", "groups are unequal", "(2,100 + 1,600) ÷ 50 = 74"],
  ["Mixing 10% and 20% in unequal amounts gives 15%", "15% is midway only for equal quantities", "use weights: 300 mL and 100 mL give 12.5%"],
  ["After adding water the solute becomes less", "only the solution volume changes", "solute stays the same"],
  ["Concentration of the mixture can be 25% from 10% and 20%", "result lies between the two", "must be between 10% and 20%"],
  ["Longer segment in a 100% bar means more", "it is a share of its own total", "need the total to find the amount"],
  ["Not converting marks to one scale before weighting", "different maxima distort the average", "convert to percentages first"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Total = average × number**; use it to find missing totals, to add a value and to remove a value.", "The combined average always lies **between** the two group averages and is **nearer the larger group**.", "In dilution the **solute stays fixed**: new volume = solute ÷ new concentration.", "An overall average can **mislead** (as with School X and School Y); split data into groups to compare fairly."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
