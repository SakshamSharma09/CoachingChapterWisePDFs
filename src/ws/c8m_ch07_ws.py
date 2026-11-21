"""Class 8 Maths Ch 7 - Proportional Reasoning-1: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch07"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric checks of the answers used below
assert 4000 - 2400 == 1600 and 3200 - 1600 == 1600 and 5 * 800 == 4000 and 4 * 800 == 3200 and 3 * 800 == 2400 and 2 * 800 == 1600
assert 5500 / 1.1 == 5000 and 2000 * .8 * .9 == 1440 and 1500 * .88 == 1320 and 1200 / .75 == 1600 and 24000 * .15 == 3600
assert 45000 // 10 * 3 == 13500 and 45000 // 10 * 5 == 22500 and 45000 // 10 * 2 == 9000 and 100 * 1.5 * .5 == 75
assert 15 * 5 == 15 * 3 + 30 and (3*6+6) * 5 == (4*6+6) * 4 and 36 / 240 * 300 == 45 and 27 / .15 == 180 and 100 * 1.2 * .8 == 96
assert 15**2 + 20**2 == 25**2 and 24 * 3 / 5 == 14.4 and 72 / 90 * 100 == 80 and 36 / 90 * 100 == 40 and 40 * 5 / 8 == 25

WS = [
# ---------------- EASY ----------------
W("The ratio 24 : 36 in its simplest form is:", 1, "(a) 2 : 3. Divide both terms by their HCF 12. (1)", "E", opts=["2 : 3", "3 : 2", "4 : 6", "12 : 18"]),
W("If $3:5=x:20$, then $x$ is:", 1, "(b) 12. $5x=3\\times20=60$, so $x=12$. (1)", "E", opts=["10", "12", "15", "25"]),
W("25% of 80 is:", 1, "(a) 20. $\\frac{25}{100}\\times80=20$. (1)", "E", opts=["20", "25", "32", "55"]),
W("₹ 1,200 is divided between two children in the ratio $3:5$. The smaller share is:", 1, "(b) ₹ 450. Total parts $=8$, one part $=1200\\div8=150$, smaller share $=3\\times150=450$. (1)", "E", opts=["₹ 360", "₹ 450", "₹ 480", "₹ 750"]),
W("Which pair of quantities is in direct proportion?", 1, "(a) the cost of pens and the number of pens (identical pens). If one doubles the other doubles; the other pairs do not change in the same ratio. (1)", "E",
  opts=["number of identical pens bought and total cost", "age of a child and her height", "number of workers and days to finish a job", "speed of a car and time taken for a fixed distance"]),
W("A price increases from ₹ 500 to ₹ 600. The percentage increase is:", 1, "(b) 20%. Increase $=100$; $\\frac{100}{500}\\times100=20\\%$. (1)", "E", opts=["10%", "20%", "25%", "100%"]),
W("The ratio of 40 cm to 1 m in simplest form is:", 1, "(b) 2 : 5. $1\\text{ m}=100$ cm, so $40:100=2:5$. (1)", "E", opts=["40 : 1", "2 : 5", "4 : 1", "1 : 40"]),
W("Find $x$ if $5:8=x:40$.", 2, "$8x=5\\times40=200$ (1), so $x=25$ (1). Check: $\\frac58=\\frac{25}{40}$.", "E"),
W("2 cups of rice are enough for 5 persons. How many cups are needed for 15 persons?", 2, "$15\\div5=3$, so the quantity triples (1): $2\\times3=6$ cups (1).", "E", wp=True),
W("Divide 72 sweets between Ritu and Sonu in the ratio $4:5$.", 2, "Total parts $=9$, one part $=72\\div9=8$ (1). Ritu gets $32$, Sonu gets $40$ (1).", "E", wp=True),
W("Express $\\frac34$ as a percentage.", 1, "$\\frac34\\times100=75\\%$ (1).", "E"),
W("Find the ratio of 45 minutes to 2 hours in simplest form.", 2, "$2$ hours $=120$ minutes (1). $45:120=3:8$ (1).", "E", wp=True),
W("A car runs 112 km on 8 litres of petrol. How far will it run on 15 litres?", 2, "1 litre gives $112\\div8=14$ km (1). 15 litres give $15\\times14=210$ km (1).", "E", wp=True),
W("Write 35% as a fraction in lowest terms and as a decimal.", 2, "$35\\%=\\frac{35}{100}=\\frac7{20}$ (1) $=0.35$ (1).", "E"),
W("True or false (give a reason): the ratios $2:3$ and $3:2$ are equal.", 1, "**False.** $\\frac23\\ne\\frac32$; the order of the terms matters (1).", "E"),
W("5 kg of rice costs ₹ 250. Find the cost of 8 kg at the same rate.", 2, "1 kg costs $250\\div5=$ ₹ 50 (1). 8 kg cost $8\\times50=$ ₹ 400 (1).", "E", wp=True),
W("Are $6:9$ and $10:15$ in proportion? Check using the product of the extremes and means.", 2, "Extremes: $6\\times15=90$; means: $9\\times10=90$ (1). They are equal, so **yes** they are in proportion (1).", "E"),
# ---------------- MEDIUM ----------------
W("Milk and water are mixed in the ratio $3:2$ to make 20 litres of mixture. How much milk and how much water are in it?", 2, "Total parts $=5$, one part $=4$ L (1). Milk $=12$ L, water $=8$ L (1).", "M", wp=True),
W("A profit of ₹ 2,800 is shared among three partners in the ratio $3:4:7$. Find each share.", 3, "Total parts $=14$ (1). One part $=2800\\div14=200$ (1). Shares: ₹ 600, ₹ 800, ₹ 1,400 (1).", "M", wp=True),
W("Mr Sharma earns ₹ 24,000 a month and saves 15% of it. Find his savings and his expenses.", 3, "Savings $=\\frac{15}{100}\\times24000$ (1) $=$ ₹ 3,600 (1). Expenses $=24000-3600=$ ₹ 20,400 (1).", "M", wp=True),
W("The price of a book rises from ₹ 800 to ₹ 920. Find the percentage increase.", 2, "Increase $=120$ (1). $\\frac{120}{800}\\times100=15\\%$ (1).", "M", wp=True),
W("The price of a school bag falls from ₹ 500 to ₹ 400. Find the percentage decrease.", 2, "Decrease $=100$ (1). $\\frac{100}{500}\\times100=20\\%$ (1).", "M", wp=True),
W("The price of an article is ₹ 100. It first rises by 20% and then falls by 20%. Find the final price and the net percentage change.", 3, "After 20% rise: $100\\times1.2=120$ (1). After 20% fall of 120: $120\\times0.8=96$ (1). Net change: 4% **decrease** (the second percentage is on a larger base) (1).", "M", wp=True),
W("A batsman scored 36 of his 90 runs in boundaries. What percentage of his runs came from boundaries?", 2, "$\\frac{36}{90}\\times100$ (1) $=40\\%$ (1).", "M", wp=True),
W("Two numbers are in the ratio $4:5$ and their sum is 72. Find the numbers.", 2, "Total parts $=9$, one part $=8$ (1). Numbers: 32 and 40 (1).", "M"),
W("On a map, 1 cm stands for 5 km. The distance between two towns on the map is 7.5 cm. Find the actual distance.", 3, "Actual distance $=7.5\\times5$ (2) $=37.5$ km (1).", "M", wp=True),
W("A recipe for 6 persons needs 450 g of rice. How much rice is needed for 10 persons?", 2, "For 1 person $450\\div6=75$ g (1). For 10 persons $=750$ g (1).", "M", wp=True),
W("The sides of two squares are in the ratio $2:3$. Find the ratio of (i) their perimeters (ii) their areas.", 3, "Sides $2k$ and $3k$ (1). (i) Perimeters $8k:12k=2:3$ (1). (ii) Areas $4k^2:9k^2=4:9$ (1).", "M"),
W("In a class of 40 students the ratio of boys to girls is $3:5$. How many girls are there?", 2, "Total parts $=8$, one part $=5$ students (1). Girls $=5\\times5=25$ (1).", "M", wp=True),
W("A shirt is marked at ₹ 1,500 and a discount of 12% is given. Find the discount and the price paid.", 3, "Discount $=\\frac{12}{100}\\times1500=$ ₹ 180 (2). Price paid $=1500-180=$ ₹ 1,320 (1).", "M", wp=True),
W("If $x:y=3:4$ and $y:z=6:5$, find $x:y:z$.", 3, "Make $y$ equal: $3:4=9:12$ and $6:5=12:10$ (2). So $x:y:z=9:12:10$ (1).", "M"),
W("A pipe fills 120 litres of water in 8 minutes. How long will it take to fill 450 litres at the same rate?", 2, "Rate $=15$ L per minute (1). Time $=450\\div15=30$ minutes (1).", "M", wp=True),
W("Ritu is 12 years old and her mother is 36. Write the ratio of their ages now and after 4 years, in simplest form.", 3, "Now: $12:36=1:3$ (1). After 4 years: $16:40$ (1) $=2:5$ (1).", "M", wp=True),
W("Find the fourth term $x$ so that $4,\\ 9,\\ 12,\\ x$ are in proportion.", 2, "$4:9=12:x$ (1). $4x=9\\times12=108$, $x=27$ (1).", "M"),
W("A number increases from 40 to 52. Find the percentage increase.", 2, "Increase $=12$ (1). $\\frac{12}{40}\\times100=30\\%$ (1).", "M"),
W("Write the ratio $3:7$ as percentages of the total.", 2, "Total parts $=10$ (1). First $=\\frac3{10}=30\\%$, second $=70\\%$ (1).", "M"),
# ---------------- HARD ----------------
W("The incomes of two friends are in the ratio $5:4$ and their expenditures are in the ratio $3:2$. Each saves ₹ 1,600. Find their incomes and expenditures.", 5, "Incomes $5x,4x$; expenditures $3y,2y$ (1). $5x-3y=1600$ and $4x-2y=1600$ (1). From the second, $y=2x-800$; substituting, $5x-6x+2400=1600$ so $x=800$ (2). Incomes ₹ 4,000 and ₹ 3,200; expenditures ₹ 2,400 and ₹ 1,600 (1).", "H", wp=True),
W("A profit of ₹ 45,000 is shared by three partners in the ratio $3:5:2$. Find each partner's share and the percentage of the profit that the second partner gets.", 3, "One part $=45000\\div10=4500$ (1). Shares: ₹ 13,500, ₹ 22,500, ₹ 9,000 (1). Second partner gets $\\frac5{10}=50\\%$ (1).", "H", wp=True),
W("After a 10% increase the population of a village is 5,500. What was the population before the increase?", 3, "Let the original be $P$: $P\\times1.10=5500$ (1). $P=5500\\div1.1$ (1) $=5,000$ (1).", "H", wp=True),
W("A shopkeeper allows two successive discounts of 20% and 10% on an article marked ₹ 2,000. Find the price paid and the single equivalent discount percentage.", 4, "After 20%: $2000\\times0.8=1600$ (1). After 10% on 1600: $1600\\times0.9=1440$ (1). Total discount $=560$ (1). $\\frac{560}{2000}\\times100=28\\%$, not $30\\%$ (1).", "H", wp=True),
W("After a discount of 25% the price of a jacket is ₹ 1,200. Find the marked price.", 3, "Price paid is 75% of the marked price (1). $0.75\\times M=1200$ (1). $M=1600$, so the marked price is ₹ 1,600 (1).", "H", wp=True),
W("Find the mean proportional $x$ between 5 and 20, i.e. $5:x=x:20$ ($x>0$).", 3, "$x^2=5\\times20=100$ (2). $x=10$ (1). Check: $5:10=10:20$.", "H"),
W("There are 40 litres of a milk-and-water mixture in the ratio $3:2$. How much water must be added to make the ratio of milk to water $3:5$?", 4, "Milk $=24$ L, water $=16$ L (1). The milk stays 24 L; for ratio $3:5$ water must be $40$ L (2). Water to add $=40-16=24$ L (1).", "H", wp=True),
W("Raju scored 72 out of 90 in Maths and 85 out of 100 in Science. Compare his performance in the two subjects using percentages. In which subject did he do better?", 3, "Maths: $\\frac{72}{90}\\times100=80\\%$ (1). Science: $85\\%$ (1). He did better in Science (1).", "H", wp=True),
W("A car's journey is recorded: time 1 h, 2 h, 3 h, 5 h and distance 60 km, 120 km, 180 km, $?$ km. (i) Show the distance is in direct proportion to time. (ii) Find the missing distance. (iii) How long will it take to cover 270 km?", 4, "(i) Distance $\\div$ time $=60$ km/h each time, a constant ratio (1). (ii) $5\\times60=300$ km (1.5). (iii) $270\\div60=4.5$ hours (1.5).", "H", wp=True),
W("Sam says: ‘If a price goes up by 50% and then comes down by 50%, it returns to the original price.’ Is he right? Test with ₹ 100.", 3, "Not right (1). $100\\to150$ (after 50% rise) (1) $\\to75$ (50% of 150 taken off): a net 25% fall (1).", "H"),
W("**Case study.** A school kitchen uses 36 kg of rice for 240 students in one day. (i) How much rice is used per student? (ii) How much rice is needed for 300 students? (iii) How many students can be fed with 27 kg?", 4, "(i) $36\\div240=0.15$ kg $=150$ g per student (1.5). (ii) $300\\times0.15=45$ kg (1.5). (iii) $27\\div0.15=180$ students (1).", "H", wp=True),
W("The sides of a triangle are in the ratio $3:4:5$ and its perimeter is 60 cm. Find the sides and show that the triangle is right-angled.", 3, "Total parts $=12$, one part $=5$ cm (1). Sides: 15 cm, 20 cm, 25 cm (1). $15^2+20^2=225+400=625=25^2$, so it is right-angled (1).", "H", wp=True),
W("Two numbers are in the ratio $3:4$. If 6 is added to each, the ratio becomes $4:5$. Find the numbers.", 4, "Numbers $3k$ and $4k$ (1). $\\dfrac{3k+6}{4k+6}=\\dfrac45$ (1) $\\Rightarrow15k+30=16k+24\\Rightarrow k=6$ (1). Numbers 18 and 24 (check $24:30=4:5$) (1).", "H"),
W("A's salary is 25% more than B's salary. By what percentage is B's salary less than A's?", 3, "Let B's salary be 100; A's is 125 (1). B's is 25 less than A's (1). $\\frac{25}{125}\\times100=20\\%$ (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(7)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "7.6 Discount, Savings and Reverse Percentages"),
 ("ul", ["**Percentage of a quantity:** 15% of ₹24,000 = (15/100) × 24,000 = ₹3,600 saved; expenses = 24,000 − 3,600 = ₹20,400.", "**Discount:** discount = (rate/100) × marked price; price paid = marked price − discount. 12% off ₹1,500 is ₹180, so the price paid is ₹1,320. Price paid = 88% of the marked price.", "**Reverse percentage:** if the price after a 25% discount is ₹1,200, then 75% of the marked price = 1,200, so the marked price = 1,200 ÷ 0.75 = **₹1,600**. After a 10% increase the population is 5,500, so the old population = 5,500 ÷ 1.1 = **5,000**.", "**Two successive changes** multiply: 20% off then 10% off = × 0.8 × 0.9 = × 0.72, i.e. a single discount of **28%**, not 30%.", "**Ratio to percentage:** a : b means a/(a + b) × 100% and b/(a + b) × 100%; 3 : 7 means 30% and 70%."]),
 ("note", "REMEMBER", "A percentage is always taken on a **base**. After an increase the new base is larger, so a 20% rise followed by a 20% fall leaves a 4% fall overall, and a 50% rise followed by a 50% fall leaves 25% below the start."),
 ("h2", "7.7 Worked Examples"),
 ("h3", "Example 1 — Equal ratios and proportion"),
 ("steps", [("Is 6 : 9 = 10 : 15?", "Cross-multiply: 6 × 15 = 90 and 9 × 10 = 90."), ("Conclusion", "The products of extremes and means are equal, so the ratios are in **proportion**."), ("Fourth term", "For 4 : 9 = 12 : x we get 4x = 108, x = 27.")]),
 ("h3", "Example 2 — Sharing in a ratio"),
 ("steps", [("₹2,800 shared in the ratio 3 : 4 : 7", "Total parts = 3 + 4 + 7 = 14."), ("One part", "2,800 ÷ 14 = ₹200."), ("Shares", "₹600, ₹800 and ₹1,400; they add up to ₹2,800 ✓.")]),
 ("h3", "Example 3 — Two ratios joined into one"),
 ("steps", [("Given x : y = 3 : 4 and y : z = 6 : 5", "Make the common term y the same: 4 and 6 have LCM 12."), ("Scale", "x : y = 9 : 12 and y : z = 12 : 10."), ("Combine", "**x : y : z = 9 : 12 : 10**.")]),
 ("h3", "Example 4 — Finding numbers from a changed ratio"),
 ("steps", [("Ratio 3 : 4; add 6 to each to get 4 : 5", "Numbers 3k and 4k: (3k + 6) ÷ (4k + 6) = 4/5."), ("Cross-multiply", "15k + 30 = 16k + 24, so k = 6."), ("Answer", "The numbers are **18 and 24**; 24 : 30 = 4 : 5 ✓.")]),
 ("h3", "Example 5 — Two incomes, two expenses"),
 ("steps", [("Incomes 5 : 4, expenses 3 : 2, savings ₹1,600 each", "Incomes 5x and 4x; expenses 3y and 2y."), ("Equations", "5x − 3y = 1600 and 4x − 2y = 1600, so y = 2x − 800."), ("Solve", "5x − 6x + 2400 = 1600, x = 800. Incomes ₹4,000 and ₹3,200; expenses ₹2,400 and ₹1,600.")]),
 ("h3", "Example 6 — Mixture problem"),
 ("steps", [("40 L of milk and water in the ratio 3 : 2", "Milk = 24 L, water = 16 L."), ("Add water to make milk : water = 3 : 5", "Milk stays 24 L, so the water must be 5/3 × 24 = 40 L."), ("Water to be added", "40 − 16 = **24 L**.")]),
 ("h2", "7.8 Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["‘in the ratio a : b’ with a total", "parts = a + b; one part = total ÷ parts", "72 sweets in 4 : 5: 32 and 40"],
  ["map scale ‘1 cm stands for 5 km’", "multiply the map length by the scale", "7.5 cm × 5 = 37.5 km"],
  ["‘same rate’, ‘per’ (price per kg, km per litre)", "unitary method: find one unit", "112 km on 8 L: 14 km per L"],
  ["‘ratio after adding the same number to both’", "write 3k, 4k and form an equation", "(3k + 6) : (4k + 6) = 4 : 5, k = 6"],
  ["‘increase/decrease by x%’", "new = old × (1 ± x/100)", "10% increase to 5,500: old = 5,500 ÷ 1.1"],
  ["‘successive discounts’", "multiply the factors", "× 0.8 × 0.9 = × 0.72"],
  ["‘x is p% more than y’, ‘y is how much less than x’", "take the correct base each time", "A = 125, B = 100: B is 20% less than A"]]),
 ("h2", "7.9 Common Mistakes"),
 ("table", ["Wrong idea", "Why it is wrong", "Correct"], [
  ["40 cm : 1 m = 40 : 1", "ratio needs the same unit", "40 : 100 = 2 : 5"],
  ["Percentage change = change ÷ new value", "the base is the original value", "120 ÷ 800 = 15%"],
  ["20% up, 20% down gives back the start", "second percentage is on a new base", "100 → 120 → 96 (4% fall)"],
  ["Discounts of 20% and 10% make 30%", "they multiply, not add", "28% single discount"],
  ["Workers and days are in direct proportion", "more workers take fewer days (inverse proportion)", "men × days is constant"],
  ["If A is 25% more than B then B is 25% less than A", "different bases", "B is 20% less than A"]]),
 ]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Reverse percentages:** divide by (1 ± rate): after a 25% discount, marked price = paid price ÷ 0.75.", "**Successive changes multiply** (× 0.8 × 0.9 = × 0.72); a rise then a fall of the same percentage never returns to the start.", "**Ratio problems with a changed ratio** are solved by writing the numbers as ak and bk and forming an equation."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
