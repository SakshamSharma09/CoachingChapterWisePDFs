"""Class 8 Maths Ch 8 - Fractions in Disguise: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run
from fractions import Fraction as F

BANK = "c8m_ch08"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths2" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# --- verify the numbers used ---
assert 800*F(75,100) == 600 and 8000*F(110,100) == 8800 and 2000*5*3/100 == 300 and 36*100//40 == 90
assert 640 + 160 == 800 and F(160,640) == F(1,4) and F(1700,85)*100 == 2000
assert 1200*F(80,100)*F(105,100) == 1008 and 12000*F(105,100)**2 == 13230
assert 10000*F(11,10)**2 - 10000 == 2100
assert F(944*100,118) == 800
assert 2500*F(8,10)*F(9,10) == 1800 and 1-F(1800,2500) == F(28,100)
assert 5000*(F(11,10)**2-1) - 5000*F(2,10) == 50
assert 1000+1500 == 2500 and F(100,2500) == F(4,100)
assert 50000*F(11,10)*F(9,10) == 49500 and F(12,10)*F(9,10) == F(108,100)
assert 4840*F(10,100) == 484 and 5324-4840 == 484 and F(4840*100,121) == 4000
assert 40*F(15,100) == 6 and F(6*100,10) == 60 and 60-40 == 20
assert 20*50*F(9,10)*F(105,100) == 945 and 10*80*F(75,100)*F(118,100) == 708 and 945+708 == 1653
assert 100000*F(8,10)**3 == 51200 and 100000*F(8,10)**4 == 40960
assert 2000*F(11,10)**2 == 2420 and F(14,10)*F(75,100) == F(105,100) and 800*F(14,10) == 1120 and 1120*F(75,100) == 840
assert 70 + 65 - 55 == 80
assert 5*F(40,100) == 2 and 5*F(30,100) == F(3,2) and 2*40*2400 == 192000
assert F(78,120) == F(65,100) and F(72,90) == F(8,10) and 3200*F(10,100) == 320
assert 8000*5*3/100 == 1200 and F(9200-8000,8000*3)*100 == 5 and 1500*F(20,100) == 300
assert 40*F(55,100) == 22 and 50*F(60,100) == 30 and 12 + 5 == 17

WS = [
# ---------------- EASY ----------------
W("The fraction $\\frac38$ written as a percentage is:", 1, "(a) $37.5\\%$. $\\frac38\\times100=37.5$. (1)", "E", opts=["$37.5\\%$", "$38\\%$", "$35\\%$", "$83\\%$"]),
W("$35\\%$ of 240 is:", 1, "(b) 84. $\\frac{35}{100}\\times240=84$. (1)", "E", opts=["72", "84", "96", "70"]),
W("A bag marked ₹ 800 is sold at a $25\\%$ discount. Its selling price is:", 1, "(b) ₹ 600. Discount $=25\\%$ of $800=200$, so SP $=800-200=600$. (1)", "E", opts=["₹ 200", "₹ 600", "₹ 625", "₹ 1000"], wp=True),
W("$125\\%$ written as a fraction in lowest terms is:", 1, "(c) $\\frac54$. $\\frac{125}{100}=\\frac54$. (1)", "E", opts=["$\\frac45$", "$\\frac{125}{10}$", "$\\frac54$", "$\\frac1{25}$"]),
W("A chair bought for ₹ 500 is sold for ₹ 450. The loss per cent is:", 1, "(b) $10\\%$. Loss $=50$; $\\frac{50}{500}\\times100=10\\%$. (1)", "E", opts=["$5\\%$", "$10\\%$", "$11\\%$", "$50\\%$"], wp=True),
W("The simple interest on ₹ 2000 at $5\\%$ per annum for 3 years is:", 1, "(b) ₹ 300. $SI=\\frac{2000\\times5\\times3}{100}=300$. (1)", "E", opts=["₹ 100", "₹ 300", "₹ 330", "₹ 600"], wp=True),
W("The population of a village is 8000. It rises by $10\\%$ in a year. The new population is:", 1, "(c) 8800. Increase $=800$; $8000+800=8800$. (1)", "E", opts=["8010", "8100", "8800", "9600"], wp=True),
W("Rohan scored 36 out of 40 in a test. Express his score as a percentage.", 2, "$\\frac{36}{40}\\times100$ (1) $=90\\%$ (1).", "E", wp=True),
W("In a class of 60 students, 18 are absent. What per cent of the class is absent and what per cent is present?", 2, "Absent $=\\frac{18}{60}\\times100=30\\%$ (1). Present $=100\\%-30\\%=70\\%$ (1).", "E", wp=True),
W("Write $0.35$ as a percentage and as a fraction in lowest terms.", 2, "$0.35=35\\%$ (1) $=\\frac{35}{100}=\\frac7{20}$ (1).", "E"),
W("The price of petrol rose from ₹ 100 to ₹ 108 per litre. Find the per cent increase.", 2, "Increase $=108-100=8$ (1). $\\frac{8}{100}\\times100=8\\%$ (1).", "E", wp=True),
W("A farmer harvests 250 kg of wheat and $12\\%$ of it is wasted. How much wheat is wasted and how much is left?", 2, "Wasted $=\\frac{12}{100}\\times250=30$ kg (1). Left $=250-30=220$ kg (1).", "E", wp=True),
W("True or false (give a reason): $150\\%$ of a number is greater than the number itself.", 1, "**True.** $150\\%=\\frac{150}{100}=1.5$, so $150\\%$ of a number is $1.5$ times the number (1).", "E"),
W("Which is greater, $\\frac35$ or $62\\%$?", 2, "$\\frac35=60\\%$ (1). Since $62\\%>60\\%$, $62\\%$ is greater (1).", "E"),
W("A cycle costing ₹ 3200 is offered at $10\\%$ discount. Find the discount and the price to be paid.", 2, "Discount $=\\frac{10}{100}\\times3200=$ ₹ 320 (1). Price $=3200-320=$ ₹ 2880 (1).", "E", wp=True),
W("A restaurant bill is ₹ 600 before tax and $18\\%$ GST is added. Find the GST and the total bill.", 2, "GST $=\\frac{18}{100}\\times600=$ ₹ 108 (1). Total $=600+108=$ ₹ 708 (1).", "E", wp=True),
W("Sunita borrows ₹ 5000 at $6\\%$ per annum simple interest for 2 years. Find the interest and the amount to be returned.", 2, "$SI=\\frac{5000\\times6\\times2}{100}=$ ₹ 600 (1). Amount $=5000+600=$ ₹ 5600 (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("A number increased by $25\\%$ becomes 150. Find the number.", 2, "Let the number be $x$. $1.25x=150$ (1), so $x=120$ (1).", "M"),
W("Express $0.04$ and $1.2$ as percentages and $15\\%$ as a decimal.", 2, "$0.04=4\\%$, $1.2=120\\%$ (1). $15\\%=0.15$ (1).", "M"),
W("A shopkeeper buys a table for ₹ 640 and sells it for ₹ 800. Find the profit per cent.", 2, "Profit $=800-640=160$ (1). Profit $\\%=\\frac{160}{640}\\times100=25\\%$ (1).", "M", wp=True),
W("A fan is sold at a loss of $15\\%$ for ₹ 1700. Find its cost price.", 2, "SP $=85\\%$ of CP (1). CP $=\\frac{1700}{0.85}=$ ₹ 2000 (1).", "M", wp=True),
W("The price of a dozen bananas fell from ₹ 80 to ₹ 68. Find the per cent decrease.", 2, "Decrease $=12$ (1). $\\frac{12}{80}\\times100=15\\%$ (1).", "M", wp=True),
W("A tank is $40\\%$ full and holds 120 litres of water. Find its capacity and the water needed to fill it.", 2, "$0.4\\times C=120$, $C=300$ litres (1). Needed $=300-120=180$ litres (1).", "M", wp=True),
W("Ratio and per cent: the boys and girls of a school of 500 students are in the ratio $3:2$. Find the per cent of girls and the number of girls.", 2, "Girls $=\\frac25$ of the school $=40\\%$ (1). Number $=\\frac25\\times500=200$ (1).", "M", wp=True),
W("Ravi scored 78 out of 120 in Maths and 72 out of 90 in Science. In which subject did he do better? Give the per cents.", 3, "Maths: $\\frac{78}{120}\\times100=65\\%$ (1). Science: $\\frac{72}{90}\\times100=80\\%$ (1). He did better in **Science** (1).", "M", wp=True),
W("Price rises by $20\\%$ and then falls by $20\\%$. Neha says the price returns to the original. Find the mistake. Take the original price as ₹ 100.", 2, "After rise: $100\\times1.2=120$ (1). After fall of $20\\%$ of 120 $=24$: $96$. The price is $4\\%$ lower, because the second per cent is taken on a different base (1).", "M"),
W("A shop marks a pair of shoes at ₹ 1500. Offer A is $20\\%$ off; offer B is a flat ₹ 280 off. Which is better and by how much?", 2, "Offer A discount $=0.2\\times1500=300$ (1). $300>280$, so A is better by ₹ 20 (1).", "M", wp=True),
W("The population of a village is 12,000. It grows by $5\\%$ every year. Find the population after 2 years.", 3, "After year 1: $12000\\times1.05=12600$ (1). After year 2: $12600\\times1.05$ (1) $=13230$ (1).", "M", wp=True),
W("A scooter costing ₹ 50,000 loses $10\\%$ of its value each year. Find its value after 2 years.", 3, "After year 1: $50000\\times0.9=45000$ (1). After year 2: $45000\\times0.9$ (1) $=$ ₹ 40,500 (1).", "M", wp=True),
W("Principal ₹ 8000 amounts to ₹ 9200 in 3 years at simple interest. Find the rate per annum.", 3, "Interest $=9200-8000=1200$ (1). $1200=\\frac{8000\\times R\\times3}{100}$ (1), so $R=5\\%$ per annum (1).", "M", wp=True),
W("A price including $18\\%$ GST is ₹ 944. Find the price before GST and the GST paid.", 3, "Price with GST $=118\\%$ of the original (1). Original $=\\frac{944}{1.18}=$ ₹ 800 (1). GST $=944-800=$ ₹ 144 (1).", "M", wp=True),
W("A jacket marked ₹ 1200 is sold at $20\\%$ discount and then $5\\%$ GST is charged on the discounted price. Find the final price.", 3, "Discount $=240$, price $=960$ (1). GST $=5\\%$ of $960=48$ (1). Final price $=960+48=$ ₹ 1008 (1).", "M", wp=True),
W("Find the compound interest on ₹ 10,000 at $10\\%$ per annum for 2 years. By how much is it more than the simple interest?", 3, "Amount $=10000\\times1.1\\times1.1=12100$ so $CI=$ ₹ 2100 (1). $SI=\\frac{10000\\times10\\times2}{100}=2000$ (1). CI is ₹ 100 more (1).", "M", wp=True),
W("A trader marks a toy $25\\%$ above its cost of ₹ 800 and then allows a $10\\%$ discount. Find the selling price, the profit and the profit per cent.", 3, "Marked price $=800\\times1.25=1000$ (1). SP $=1000-100=900$ (1). Profit $=100$, profit $\\%=\\frac{100}{800}\\times100=12.5\\%$ (1).", "M", wp=True),
W("In a class of 50 students, $60\\%$ are girls. $40\\%$ of the girls and $25\\%$ of the boys play cricket. What per cent of the class plays cricket?", 3, "Girls $=30$, boys $=20$ (1). Cricket players $=0.4\\times30+0.25\\times20=12+5=17$ (1). $\\frac{17}{50}\\times100=34\\%$ (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Anil calculated the compound interest on ₹ 2000 at $10\\%$ for 2 years as $2000\\times\\frac{20}{100}=$ ₹ 400. Find and correct his mistake.", 3, "He added the interest of the two years without compounding, which is simple interest (1). Correct amount $=2000\\times1.1\\times1.1=2420$ (1). $CI=$ ₹ 420 (1).", "H"),
W("Show with an example and in general that $x\\%$ of $y$ equals $y\\%$ of $x$. Use it to find $8\\%$ of 50 quickly.", 3, "Example: $10\\%$ of $50=5$ and $50\\%$ of $10=5$ (1). In general $\\frac{x}{100}\\times y=\\frac{xy}{100}=\\frac{y}{100}\\times x$ (1). $8\\%$ of $50=50\\%$ of $8=4$ (1).", "H"),
W("The length of a rectangle is increased by $20\\%$ and its breadth is decreased by $10\\%$. Find the per cent change in its area.", 3, "New area $=1.2l\\times0.9b=1.08\\,lb$ (2). Area increases by $8\\%$ (1).", "H"),
W("A shopkeeper gives two successive discounts of $25\\%$ and $20\\%$ on a TV marked ₹ 2500. Find the price paid and the single equal discount per cent.", 3, "After $25\\%$: $2500\\times0.75=1875$ (1). After $20\\%$: $1875\\times0.8=1500$ (1). Single discount $=\\frac{1000}{2500}\\times100=40\\%$, not $45\\%$ (1).", "H", wp=True),
W("A sum amounts to ₹ 4840 in 2 years and ₹ 5324 in 3 years at compound interest. Find the rate per cent and the sum.", 4, "Interest for the third year $=5324-4840=484$ on ₹ 4840 (1). Rate $=\\frac{484}{4840}\\times100=10\\%$ (1). Sum $=\\frac{4840}{1.1^2}$ (1) $=$ ₹ 4000 (1).", "H", wp=True),
W("The difference between the compound interest and the simple interest on a sum for 2 years at $10\\%$ per annum is ₹ 50. Find the sum.", 4, "On ₹ $P$: $CI=0.21P$, $SI=0.20P$ (2). Difference $=0.01P=50$ (1). $P=$ ₹ 5000 (1).", "H", wp=True),
W("A population of 50,000 increases by $10\\%$ in the first year and decreases by $10\\%$ in the second. Find the population after 2 years and the net per cent change.", 4, "After year 1: $55000$ (1). After year 2: $55000\\times0.9=49500$ (1). Net change $=-500$ (1), i.e. $1\\%$ decrease (1).", "H", wp=True),
W("A shopkeeper sells two fans at ₹ 1200 each. On one he gains $20\\%$ and on the other he loses $20\\%$. Find his overall gain or loss per cent.", 4, "CP of first $=\\frac{1200}{1.2}=1000$ (1). CP of second $=\\frac{1200}{0.8}=1500$ (1). Total CP $=2500$, total SP $=2400$, loss $=100$ (1). Loss $\\%=\\frac{100}{2500}\\times100=4\\%$ (1).", "H", wp=True),
W("A machine worth ₹ 1,00,000 loses $20\\%$ of its value every year. After how many whole years is its value below ₹ 50,000? Show the value each year.", 4, "Year 1: 80,000 (1). Year 2: 64,000 (1). Year 3: 51,200 (1). Year 4: 40,960, which is below 50,000, so **4 years** (1).", "H", wp=True),
W("A shopkeeper marks goods $40\\%$ above the cost and gives a $25\\%$ discount. Find the profit per cent. If the cost is ₹ 800, find the marked price, the selling price and the profit.", 4, "SP $=1.4\\times0.75=1.05$ times CP, so profit $=5\\%$ (1). MP $=800\\times1.4=$ ₹ 1120 (1). SP $=1120\\times0.75=$ ₹ 840 (1). Profit $=$ ₹ 40 (1).", "H", wp=True),
W("A solution of 40 litres contains $15\\%$ acid. How much water must be added to make it a $10\\%$ acid solution?", 4, "Acid $=0.15\\times40=6$ litres (1). Acid stays 6 litres; $10\\%$ of the new total $=6$ (1), so total $=60$ litres (1). Water added $=20$ litres (1).", "H", wp=True),
W("In an examination $70\\%$ of the candidates passed Maths, $65\\%$ passed Science and $55\\%$ passed both. What per cent passed at least one subject and what per cent failed both?", 4, "Passed at least one $=70+65-55=80\\%$ (2). Failed both $=100-80=20\\%$ (2).", "H", wp=True),
W("**Case study.** A school buys 20 notebooks at ₹ 50 each with $10\\%$ discount, then $5\\%$ GST on the discounted amount; and 10 compass boxes at ₹ 80 each with $25\\%$ discount, then $18\\%$ GST on the discounted amount. Find (a) the amount paid for notebooks, (b) the amount paid for compass boxes, (c) the total bill.", 5, "(a) $20\\times50=1000$; after $10\\%$ off $900$; GST $45$; pay ₹ 945 (2). (b) $10\\times80=800$; after $25\\%$ off $600$; GST $108$; pay ₹ 708 (2). (c) Total $=945+708=$ ₹ 1653 (1).", "H", wp=True),
W("**Case study (Rajasthan farm).** A farmer has 5 hectares. $40\\%$ is sown with wheat and $30\\%$ with mustard. The remaining land is divided between barley and fallow in the ratio $2:1$. Find the area under each and the per cent under barley. If wheat gives 40 quintal per hectare at ₹ 2400 per quintal, find the income from wheat.", 5, "Wheat $=2$ ha, mustard $=1.5$ ha (1). Remaining $=1.5$ ha; barley $=1$ ha, fallow $=0.5$ ha (2). Barley $=\\frac15=20\\%$ (1). Wheat income $=2\\times40\\times2400=$ ₹ 1,92,000 (1).", "H", wp=True),
]

_o = _old(11)
_i = max(i for i, b in enumerate(_o["blocks"]) if b[0] == "h2")
_pre, _tail = _o["blocks"][:_i], _o["blocks"][_i:]
_extra = [
 ("h2", "Key Formulae at a Glance"),
 ("note", "FORMULA", "Per cent of a quantity = (p ÷ 100) × quantity.  Per cent change = (change ÷ original) × 100.  Profit = SP − CP;  Loss = CP − SP;  Profit % = (profit ÷ CP) × 100;  Loss % = (loss ÷ CP) × 100."),
 ("note", "FORMULA", "Discount = marked price − selling price;  Discount % = (discount ÷ marked price) × 100.  Price with GST = price × (100 + GST%) ÷ 100.  Simple interest SI = P × R × T ÷ 100;  Amount = P + SI.  Compound interest: A = P (1 + R/100)<sup>n</sup>;  CI = A − P.  Depreciation: V = P (1 − R/100)<sup>n</sup>."),
 ("table", ["Situation", "Multiplier on the original", "Example"], [["Increase by 20%", "1.20", "₹ 500 → ₹ 600"], ["Decrease by 20%", "0.80", "₹ 500 → ₹ 400"], ["Profit 25%", "1.25 × CP", "CP ₹ 800 → SP ₹ 1000"], ["Loss 15%", "0.85 × CP", "SP ₹ 1700 → CP ₹ 2000"], ["GST 18%", "1.18", "₹ 800 → ₹ 944"], ["10% growth for 2 years", "1.10 × 1.10 = 1.21", "₹ 10,000 → ₹ 12,100"], ["10% decline for 2 years", "0.90 × 0.90 = 0.81", "₹ 50,000 → ₹ 40,500"]]),
 ("h2", "More Worked Examples"),
 ("h3", "Example 1 — Finding the original after a per cent change"),
 ("steps", [("Question", "After a 25% rise a number becomes 150. Find the number."), ("Set up", "New value = 125% of original = 1.25 × x."), ("Solve", "1.25x = 150, so x = 150 ÷ 1.25 = **120**. Check: 25% of 120 = 30 and 120 + 30 = 150.")]),
 ("h3", "Example 2 — Cost price from a loss"),
 ("steps", [("Question", "A fan is sold at a 15% loss for ₹ 1700. Find the cost price."), ("Set up", "SP = 100% − 15% = 85% of CP."), ("Solve", "CP = 1700 ÷ 0.85 = **₹ 2000**.")]),
 ("h3", "Example 3 — Marked price, discount and GST"),
 ("steps", [("Question", "A jacket marked ₹ 1200 has a 20% discount, then 5% GST on the discounted price."), ("Discount", "20% of 1200 = 240, so price = ₹ 960."), ("GST", "5% of 960 = 48."), ("Final price", "960 + 48 = **₹ 1008**.")]),
 ("h3", "Example 4 — Compound interest"),
 ("steps", [("Question", "Find the CI on ₹ 10,000 at 10% per annum for 2 years."), ("Year 1", "Interest 1000, amount 11,000."), ("Year 2", "Interest 10% of 11,000 = 1100, amount 12,100."), ("Answer", "CI = 12,100 − 10,000 = **₹ 2100**; SI would be only ₹ 2000. The extra ₹ 100 is interest on the first year's interest.")]),
 ("h3", "Example 5 — Successive per cent changes"),
 ("steps", [("Question", "A price rises 20% then falls 20%. What is the net change?"), ("Take 100", "100 → 120 → 120 − 24 = 96."), ("Answer", "Net **4% decrease**, not zero, because the second 20% is taken on 120, not on 100.")]),
 ("h3", "Example 6 — Two articles, one gain and one loss"),
 ("steps", [("Question", "Two fans are each sold for ₹ 1200, one at 20% gain and the other at 20% loss."), ("Cost prices", "First: 1200 ÷ 1.2 = 1000. Second: 1200 ÷ 0.8 = 1500."), ("Total", "CP = 2500, SP = 2400, so loss = ₹ 100."), ("Loss %", "100 ÷ 2500 × 100 = **4%**. (Equal per cent gain and loss on equal selling prices is always a loss.)")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Words in the problem", "What to do", "Example"], [
  ["‘of’ with a per cent", "multiply: p% of Q = p ÷ 100 × Q", "35% of 240 = 84"],
  ["‘increased by p%’, ‘rose’, ‘grew’", "multiply by (100 + p) ÷ 100", "8000 up 10% = 8800"],
  ["‘decreased by p%’, ‘discount’, ‘fell’", "multiply by (100 − p) ÷ 100", "₹ 800 with 25% off = ₹ 600"],
  ["‘becomes … after’ a change", "original × multiplier = new value, so divide to find the original", "1.25x = 150 gives x = 120"],
  ["‘including GST’", "the given amount is (100 + GST)% of the base price", "944 ÷ 1.18 = 800"],
  ["‘each year’, ‘after n years’", "apply the multiplier n times (compound) or add the same interest n times (simple)", "12,000 at 5% for 2 years = 13,230"],
  ["‘ratio’ then ‘per cent’", "convert the ratio to a fraction of the total, then multiply by 100", "boys : girls = 3 : 2 gives girls 2/5 = 40%"]]),
 ("note", "REMEMBER", "Always ask: **per cent of what?** Profit and loss use the **cost price**, discount uses the **marked price**, per cent change uses the **original value**."),
 ("h2", "Likely Exam Questions"),
 ("qa", [("A bill is ₹ 600 and 18% GST is added. What is the total?", "GST = 18% of 600 = ₹ 108, total = ₹ 708."),
  ("Why is a 20% rise followed by a 20% fall not a return to the start?", "The 20% fall is taken on the larger, increased value, so 100 → 120 → 96, a net 4% fall."),
  ("A sum becomes ₹ 4840 in 2 years and ₹ 5324 in 3 years at compound interest. Find the rate.", "Third-year interest = 484 on 4840, so the rate is 484 ÷ 4840 × 100 = 10%."),
  ("Difference between CI and SI for 2 years at 10% is ₹ 50. Find the sum.", "Difference = 1% of P = 50, so P = ₹ 5000."),
  ("Cost ₹ 800, marked 40% above cost, 25% discount: profit per cent?", "SP = 1.4 × 0.75 × CP = 1.05 CP, so a 5% profit."),
  ("Explain why x% of y equals y% of x.", "Both equal xy ÷ 100, because multiplication can be done in any order.")]),
]
CH = dict(_o, num=8, blocks=_pre + _extra + _tail,
          takeaways=_o["takeaways"] + ["A **multiplier** (1.25 for +25%, 0.85 for −15%) turns every per cent problem into one multiplication or division.", "To find the **original** value from a changed value, **divide** by the multiplier; do not subtract the per cent.", "Compound interest and depreciation repeat the multiplier once per year: A = P(1 ± R/100)<sup>n</sup>."])


def _sub(x, P):
    """review fix: exact text replacements inside the notes blocks"""
    if isinstance(x, str):
        for a, b in P: x = x.replace(a, b)
        return x
    if isinstance(x, list): return [_sub(i, P) for i in x]
    if isinstance(x, tuple): return tuple(_sub(i, P) for i in x)
    if isinstance(x, dict): return {k: _sub(v, P) for k, v in x.items()}
    return x
_P = [("Reading ‘165% of’ as ‘65% more’ differently", "Treating ‘165% of the old value’ and ‘65% more than the old value’ as different amounts")]
CH = _sub(CH, _P)

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
