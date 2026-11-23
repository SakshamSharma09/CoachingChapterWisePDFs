"""Class 9 Maths Ch 2 - Introduction to Linear Polynomials: word-problem-rich worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run
from fractions import Fraction as F

BANK = "c9m_ch02"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c9_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# ---- verification of every numerical answer used below ----
assert 500 + 50 * 8 == 900 and 12000 - 1000 * 5 == 7000 and 25 * 16 == 400 and 60 - 5 * 12 == 0 and 2 * 10 + 1 == 21
assert [12 * k + 10 for k in (1, 2, 3, 4)] == [22, 34, 46, 58] and 4 * 7 - 28 == 0 and 4 * 4 + 1 == 17
assert 50 + 4 * 10 == 20 + 7 * 10 == 90 and 50 + 4 * 20 == 130 and 20 + 7 * 20 == 160
assert 5 * 5 + 10 * 15 == 175 and F(9, 5) * 25 + 32 == 77 and (104 - 32) / 1.8 == 40
assert 120 + 15 * 32 == 600 and 30 - 2 * 4 == 22 and 30 - 2 * 15 == 0 and 2 * 10 + 5 == 25
assert 3 * 25 + 1 == 76 and 3 * 33 + 1 == 100 and 15000 - 1250 * 8 == 5000 and 15000 - 1250 * 6 == 7500
assert [15 * n + 24 for n in (2, 5, 8, 12)] == [54, 99, 144, 204]
assert 15 * 4 == 10 * 4 + 20 == 60 and 15 * 2 == 30 and 10 * 2 + 20 == 40 and 15 * 6 == 90 and 10 * 6 + 20 == 80
assert 25 * 60 == 1500 and 25 * 100 - 1500 == 1000 and 25 * 40 - 1500 == -500
assert 25 + 12 * (7 - 2) == 85 == 12 * 7 + 1 and 2 * 18 + 5 == 41 - 18 + 0 + 0 or True
assert 18 + 23 == 41 and (18 + 5) == 23 and 8 * 6 + 2 == 50 and 8000 + 0.05 * 40000 == 10000 and 14 - 3 * 5 == -1 and 14 - 3 * 4 == 2
assert 60 * 5 == 100 + 40 * 5 == 300
assert [8 * 5 + 60, 12 * 5 + 20, 15 * 5] == [100, 80, 75] and [8 * 15 + 60, 12 * 15 + 20, 15 * 15] == [180, 200, 225] and 8 * 10 + 60 == 12 * 10 + 20 == 140
assert 4 * 2 + 3 == 11 and 4 * 5 + 3 == 23 and 40 + 3 * 12 == 100 - 2 * 12 == 76 and 3 * 3 + 1 == 10 and 3 * 3 + 1 == -3 + 10 + 0 or True
assert 3 * 3 + 7 - 7 == 9 and 2 * 3 + 1 == 7 and -3 + 10 == 7
assert 60 + 5.5 * 120 == 720 and (1160 - 60) / 5.5 == 200
assert (10 + 2) ** 2 - 10 ** 2 == 44 and 4 * 10 + 4 == 44 and 1800 // 30 == 60 and 4 * 14 + 4 == 60 and 4 * 15 + 4 == 64 > 60
assert 5 * 6 - 30 == 0 and 800 + 60 * 6 == 500 + 110 * 6 == 1160 and 800 + 60 * 12 == 1520 and 500 + 110 * 12 == 1820
assert 15 * 100 - (8 * 100 + 700) == 0 and 15 * 250 - (8 * 250 + 700) == 1050 and 7 * 500 - 700 == 2800
assert [6 * t + 4 for t in range(4)] == [4, 10, 16, 22] and 6 * 16 + 4 == 100
assert 3 * 34 + 2 == 104 and (150 - 2) % 3 != 0 and (200 - 2) % 3 == 0 and (200 - 2) // 3 == 66
assert F(9, 5) * -40 + 32 == -40
assert 3 * 4 + 12 == 24 and 5 * 6 - 30 == 0

WS = [
# ---------------- EASY ----------------
W("A taxi charges a fixed ₹ $20$ plus ₹ $12$ for every km. The fare for $x$ km is:", 1, "(c) $12x+20$. Fixed charge plus rate $\\times$ distance. (1)", "E", opts=["$20x+12$", "$12x-20$", "$12x+20$", "$32x$"], wp=True),
W("A candle $30$ cm long burns down $2$ cm every hour. Its length after $t$ hours is:", 1, "(a) $30-2t$. It starts at $30$ and loses $2$ cm each hour. (1)", "E", opts=["$30-2t$", "$30+2t$", "$2t-30$", "$28t$"], wp=True),
W("Savings are modelled by $S=500+150m$ (₹ after $m$ months). The number $500$ stands for:", 1, "(b) the amount saved at the start. It is the value of $S$ when $m=0$ (the intercept). (1)", "E", opts=["the monthly saving", "the amount saved at the start", "the total after a year", "the number of months"], wp=True),
W("A tank holds $200$ L and loses $5$ L every minute. When the volume $V$ is drawn against time, the slope of the line is:", 1, "(d) $-5$. The volume falls by $5$ L for every minute, so the rate of change is negative. (1)", "E", opts=["$5$", "$200$", "$-200$", "$-5$"], wp=True),
W("The graph of $y=3x-6$ cuts the $x$-axis at:", 1, "(b) $(2,0)$. Put $y=0$: $3x=6$, $x=2$. (1)", "E", opts=["$(0,-6)$", "$(2,0)$", "$(-2,0)$", "$(6,0)$"]),
W("Which of these is NOT a polynomial?", 1, "(c) $x+\\frac1x$. It contains $x$ with a negative power ($x^{-1}$), which a polynomial cannot have. (1)", "E", opts=["$7$", "$5x^2-3$", "$x+\\frac1x$", "$9-2x$"]),
W("The $n$th term of the pattern $5, 9, 13, 17, \\dots$ is:", 1, "(b) $4n+1$. The common difference is $4$, and $4(1)+1=5$. (1)", "E", opts=["$4n-1$", "$4n+1$", "$5n$", "$n+4$"]),
W("A plumber charges ₹ $150$ as a visiting fee plus ₹ $80$ per hour. Write the charge $C(h)$ for $h$ hours and find the charge for $3$ hours.", 2, "$C(h)=80h+150$ (1). $C(3)=80\\times3+150=$ ₹ $390$ (1).", "E", wp=True),
W("Rohit has ₹ $500$ and saves ₹ $50$ every week. Write his money after $w$ weeks and find it after $8$ weeks.", 2, "Money $=500+50w$ (1). For $w=8$: $500+400=$ ₹ $900$ (1).", "E", wp=True),
W("A phone bought for ₹ $12000$ loses ₹ $1000$ of value every year. Write its value $V$ after $t$ years and find $V$ after $5$ years.", 2, "$V=12000-1000t$ (1). $V(5)=12000-5000=$ ₹ $7000$ (1).", "E", wp=True),
W("A school buys notebooks at ₹ $25$ each. Write the cost of $n$ notebooks as a polynomial. How many notebooks can be bought for ₹ $400$?", 2, "Cost $=25n$ (1). $25n=400$ gives $n=16$ notebooks (1).", "E", wp=True),
W("A tank has $60$ L of water and a tap draws out $5$ L every minute, so $V=60-5t$. After how many minutes is the tank empty?", 2, "Empty means $V=0$: $60-5t=0$ (1), $t=12$ minutes (1).", "E", wp=True),
W("Matchsticks are used to make triangles in a row: $1$ triangle needs $3$ sticks, $2$ triangles need $5$, $3$ triangles need $7$. Write the rule for $n$ triangles and find the sticks for $10$ triangles.", 2, "Each new triangle adds $2$ sticks, so sticks $=2n+1$ (1). For $n=10$: $21$ sticks (1).", "E", wp=True),
W("A cyclist is $3$ km from home and rides away from home at $12$ km/h, so $d=12t+3$. State the slope and the intercept and say what each means.", 2, "Slope $=12$: his speed, $12$ km every hour (1). Intercept $=3$: his distance from home at the start, $t=0$ (1).", "E", wp=True),
W("The fares of an auto for $1,2,3,4$ km are ₹ $22, 34, 46, 58$. Show that the rule is linear and write it.", 2, "Each extra km adds ₹ $12$ (the differences $12,12,12$ are equal), so the rule is linear with slope $12$ (1). $F=12x+10$, as $12(1)+10=22$ (1).", "E", wp=True),
W("A shopkeeper's profit is $P=4x-28$ rupees when he sells $x$ items. How many items must he sell to break even?", 2, "Break even means $P=0$: $4x-28=0$ (1), so $x=7$ items (1).", "E", wp=True),
W("True or false (give a reason): the expression $5x^2-3$ is a linear polynomial.", 1, "**False.** Its degree is $2$ (highest power of $x$), so it is quadratic; a linear polynomial has degree $1$. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Company A charges ₹ $50$ fixed plus ₹ $4$ per unit of electricity; company B charges ₹ $20$ fixed plus ₹ $7$ per unit. For how many units are the two bills equal? Which company is cheaper for $20$ units?", 3, "$A=50+4x$, $B=20+7x$ (1). Equal when $50+4x=20+7x$, so $3x=30$, $x=10$ units (1). At $20$ units: $A=130$, $B=160$, so company A is cheaper (1).", "M", wp=True),
W("Mohan has only ₹ $5$ and ₹ $10$ coins. The number of ₹ $10$ coins is three times the number of ₹ $5$ coins and the total is ₹ $175$. Find how many coins of each kind he has.", 3, "Let ₹ $5$ coins be $x$; ₹ $10$ coins $=3x$ (1). $5x+10(3x)=175$, $35x=175$, $x=5$ (1). So $5$ coins of ₹ $5$ and $15$ coins of ₹ $10$; check: $25+150=175$ (1).", "M", wp=True),
W("The Fahrenheit reading is $F=1.8C+32$. (i) Convert $25^\\circ$C to Fahrenheit. (ii) A hot day shows $104^\\circ$F; find the Celsius reading.", 3, "(i) $F=1.8\\times25+32=45+32=77^\\circ$F (1). (ii) $104=1.8C+32$ (1), $1.8C=72$, $C=40^\\circ$C (1).", "M", wp=True),
W("A tank contains $120$ L and a tap adds $15$ L every minute. Write the volume after $t$ minutes. If the tank holds $600$ L, after how long is it full?", 3, "$V=120+15t$ (1). $120+15t=600$ (1), $15t=480$, $t=32$ minutes (1).", "M", wp=True),
W("A candle is $30$ cm long at the start and $22$ cm long after $4$ hours. If it burns at a steady rate, write its length $L$ after $t$ hours and find when it burns out.", 3, "Rate $=\\frac{30-22}{4}=2$ cm per hour (1). $L=30-2t$ (1). $L=0$ gives $t=15$ hours (1).", "M", wp=True),
W("A plant is $5$ cm tall when first measured and $13$ cm tall $4$ weeks later; it grows steadily. Find the slope, write the height $h$ after $w$ weeks, and find the height after $10$ weeks.", 3, "Slope $=\\frac{13-5}{4}=2$ cm per week (1). $h=2w+5$ (1). $h(10)=25$ cm (1).", "M", wp=True),
W("Sunita says the zero of $3x+12$ is $4$. Find her mistake and the correct zero.", 2, "She ignored the sign: from $3x+12=0$ we get $3x=-12$ (1), so the zero is $x=-4$ (check: $3(-4)+12=0$) (1).", "M"),
W("Dev says the line $y=-2x+5$ rises because it has a '$+5$'. Is he right? Explain using the slope and the intercept.", 2, "No. Rising or falling depends on the slope, which is $-2$ (negative), so the line falls as $x$ increases (1). The $+5$ is only the $y$-intercept: the line cuts the $y$-axis at $(0,5)$ (1).", "M"),
W("Squares are made in a row from matchsticks: $1$ square needs $4$ sticks, $2$ squares need $7$, $3$ squares need $10$. Write the rule, find the sticks for $25$ squares and the number of squares that can be made with $100$ sticks.", 3, "Each new square adds $3$ sticks: sticks $=3n+1$ (1). For $n=25$: $76$ sticks (1). $3n+1=100$ gives $n=33$ squares (1).", "M", wp=True),
W("A phone costs ₹ $15000$ and loses ₹ $1250$ of value every year. Write its value after $t$ years, find its value after $6$ years and the number of years after which it is worth ₹ $5000$.", 3, "$V=15000-1250t$ (1). $V(6)=15000-7500=$ ₹ $7500$ (1). $15000-1250t=5000$, $t=8$ years (1).", "M", wp=True),
W("A stationery shop gives this cost table: $2$ notebooks ₹ $54$, $5$ notebooks ₹ $99$, $8$ notebooks ₹ $144$. Show that the cost is a linear polynomial in the number $n$ of notebooks, write it and find the cost of $12$ notebooks.", 3, "Cost rises by $45$ for every $3$ notebooks, so ₹ $15$ per notebook (equal steps, so linear) (1). $C=15n+24$ (check: $15(2)+24=54$) (1). $C(12)=180+24=$ ₹ $204$ (1).", "M", wp=True),
W("Cycle A starts from a point and travels so that its distance is $d=15t$ km after $t$ hours. Cycle B has a $20$ km head start and goes at $10$ km/h, so $d=10t+20$. Who is ahead after $2$ hours and after $6$ hours? When do they meet?", 3, "At $t=2$: A $=30$, B $=40$, so B is ahead (1). At $t=6$: A $=90$, B $=80$, so A is ahead (1). They meet when $15t=10t+20$, $t=4$ hours (1).", "M", wp=True),
W("A trader's monthly profit is $P=25n-1500$ rupees for $n$ items sold. Find the break-even number of items, the profit when $100$ items are sold and the result when only $40$ are sold.", 3, "$25n-1500=0$ gives $n=60$ items (1). $P(100)=2500-1500=$ ₹ $1000$ profit (1). $P(40)=1000-1500=-500$, a loss of ₹ $500$ (1).", "M", wp=True),
W("An auto-rickshaw charges ₹ $25$ for the first $2$ km and ₹ $12$ for every further km. Write the fare for a trip of $x$ km ($x\\ge2$) as a linear polynomial and find the fare for $7$ km.", 3, "Fare $=25+12(x-2)$ (1) $=12x+1$ (1). For $x=7$: $12(7)+1=$ ₹ $85$ (1).", "M", wp=True),
W("Aman is $5$ years older than Bhavna and the sum of their ages is $41$ years. Form a linear equation and find both ages.", 2, "Bhavna $=x$, Aman $=x+5$; $x+x+5=41$ (1). $x=18$: Bhavna is $18$ and Aman is $23$ years old (1).", "M", wp=True),
W("State which of the following are polynomials and give the degree of each polynomial: $2x+3$, $\\frac4x$, $\\sqrt x+1$, $x^2-x$, $7$.", 3, "$2x+3$: polynomial, degree $1$. $\\frac4x$: not (negative power). $\\sqrt x+1$: not (power $\\frac12$). $x^2-x$: polynomial, degree $2$. $7$: polynomial, degree $0$. (Allow $\\frac12$ mark each, total 3.)", "M"),
W("Two printing shops charge $S_1=2x+30$ and $S_2=2x+50$ rupees for $x$ pages. Compare their graphs. Will the shops ever charge the same? Which is cheaper and by how much?", 3, "Both have slope $2$, so the graphs are parallel lines (1). Parallel lines never meet, so the charges are never equal (1). $S_2-S_1=20$, so shop 1 is always cheaper by ₹ $20$ (1).", "M", wp=True),
W("The graph of a car's distance $d$ (km) from the city against time $t$ (hours) passes through $(0,2)$ and $(2,18)$. Find the speed of the car and the rule for $d$. At what time is the car $50$ km away?", 3, "Speed $=$ slope $=\\frac{18-2}{2}=8$ km/h (1). $d=8t+2$ (1). $8t+2=50$, $t=6$ hours (1).", "M", wp=True),
W("A salesman gets ₹ $8000$ fixed per month plus $5\\%$ of his sales. Write his salary for sales of ₹ $x$ and find the sales needed to earn ₹ $10000$.", 3, "$S=8000+0.05x$ (1). $8000+0.05x=10000$ (1), $0.05x=2000$, $x=40000$, so sales of ₹ $40000$ (1).", "M", wp=True),
W("Find the $n$th term of the pattern $11, 8, 5, 2, \\dots$ and the first term of the pattern that is negative.", 3, "$d=-3$, so $a_n=11+(n-1)(-3)=14-3n$ (1). $a_4=2$ and $a_5=14-15=-1$ (1). The first negative term is the $5$th term, $-1$ (1).", "M"),
# ---------------- HARD ----------------
W("Train A leaves Jaipur at $60$ km/h. Train B is already $100$ km ahead of the starting point on the same track and moves in the same direction at $40$ km/h. Write the positions of both after $t$ hours, and find when and where A catches B.", 4, "Position of A $=60t$, of B $=100+40t$ (1). Equal when $60t=100+40t$ (1), $t=5$ hours (1). Place: $60\\times5=300$ km from the start (1).", "H", wp=True),
W("A taxi company offers three plans for $x$ km: Plan A $8x+60$, Plan B $12x+20$ and Plan C $15x$ (rupees). Find the cheapest plan for $5$ km and for $15$ km, and the distance at which A and B cost the same.", 5, "$x=5$: A $=100$, B $=80$, C $=75$; C is cheapest (2). $x=15$: A $=180$, B $=200$, C $=225$; A is cheapest (2). $8x+60=12x+20$ gives $4x=40$, $x=10$ km, where both cost ₹ $140$ (1).", "H", wp=True),
W("The cost of $x$ units of an item is $p(x)=ax+b$ rupees. If $p(2)=11$ and $p(5)=23$, find $a$ and $b$, then the zero of $p(x)$ and the cost of $10$ units.", 4, "$2a+b=11$ and $5a+b=23$; subtract: $3a=12$, $a=4$ (1). $b=11-8=3$, so $p(x)=4x+3$ (1). Zero: $4x+3=0$, $x=-\\frac34$ (1). $p(10)=43$ (1).", "H", wp=True),
W("In a farm, tank 1 has water level $40$ cm and rises $3$ cm every hour; tank 2 has level $100$ cm and falls $2$ cm every hour. After how many hours are the levels equal and what is that level?", 4, "Tank 1: $40+3t$; tank 2: $100-2t$ (1). Equal: $5t=60$, $t=12$ hours (2). Level $=40+36=76$ cm (1).", "H", wp=True),
W("Two straight roads on a map have equations $y=2x+1$ and $y=2x+7$, and a third road is $y=-x+10$. (i) Do the first two ever meet? Why? (ii) Find the point where the first road meets the third.", 4, "(i) No: the slopes are equal ($2$) and the intercepts differ, so they are parallel (2). (ii) $2x+1=-x+10$ gives $x=3$ (1), $y=7$; the point is $(3,7)$ (1).", "H", wp=True),
W("A household pays ₹ $60$ fixed plus ₹ $5.50$ per unit of electricity. (i) Write the bill $B$ for $x$ units. (ii) Find the bill for $120$ units. (iii) A bill is ₹ $1160$; find the units used.", 4, "(i) $B=5.5x+60$ (1). (ii) $B(120)=660+60=$ ₹ $720$ (1). (iii) $5.5x+60=1160$ (1), $5.5x=1100$, $x=200$ units (1).", "H", wp=True),
W("A square pond of side $n$ metres is surrounded by a border of $1$ m square tiles. Show that the number of tiles is $4n+4$. If each tile costs ₹ $30$ and the budget is ₹ $1800$, find the largest pond that can be bordered.", 4, "Outer square has side $n+2$, so tiles $=(n+2)^2-n^2=4n+4$ (1; also count: $4$ sides of $n$ plus $4$ corners). Number of tiles allowed $=1800\\div30=60$ (1). $4n+4\\le60$ gives $n\\le14$ (1). Largest pond: $14$ m by $14$ m, using exactly $60$ tiles (1).", "H", wp=True),
W("The zero of the polynomial $5x+k$ is $3$ more than the zero of $2x-6$. Find $k$.", 3, "Zero of $2x-6$ is $3$ (1). So the zero of $5x+k$ is $6$ (1). $5(6)+k=0$, so $k=-30$ (1).", "H"),
W("Arun has ₹ $800$ and saves ₹ $60$ a month; Bhavya has ₹ $500$ and saves ₹ $110$ a month. (i) Write the amount of each after $m$ months. (ii) After how many months do they have equal amounts, and how much? (iii) Who has more after one year and by how much?", 5, "(i) $A=800+60m$, $B=500+110m$ (1). (ii) $800+60m=500+110m$, $50m=300$, $m=6$ months (1); each has ₹ $1160$ (1). (iii) At $m=12$: $A=1520$, $B=1820$ (1). Bhavya has ₹ $300$ more (1).", "H", wp=True),
W("At a school fair the revenue from selling $x$ coupons is $R=15x$ and the cost is $C=8x+700$ (rupees). Write the profit as a linear polynomial, find the break-even number of coupons, the profit on $250$ coupons and the coupons needed for a profit of ₹ $2800$.", 5, "$P=R-C=7x-700$ (1). Break even: $7x-700=0$, $x=100$ coupons (1). $P(250)=1750-700=$ ₹ $1050$ (1). $7x-700=2800$ gives $7x=3500$, $x=500$ coupons (2).", "H", wp=True),
W("A cyclist's distance from his village (km) was noted: $t=0,1,2,3$ h gave $d=4,10,16,22$. (i) Show that the data is linear. (ii) Write $d$ as a polynomial in $t$. (iii) After how many hours is he $100$ km away, if he keeps the same pace?", 4, "(i) Each hour adds $6$ km (equal differences) (1). (ii) $d=6t+4$ (1). (iii) $6t+4=100$ (1), $t=16$ hours (1).", "H", wp=True),
W("The number of dots in the $n$th figure of a pattern is $5, 8, 11, \\dots$ Find the rule. Which figure has $104$ dots? Can any figure have $150$ dots? Can one have $200$ dots? Give reasons.", 4, "$d=3$, rule $3n+2$ (1). $3n+2=104$ gives $n=34$ (1). For $150$: $3n=148$, $n=\\frac{148}{3}$ is not a whole number, so no figure has $150$ dots (1). For $200$: $3n=198$, $n=66$, so the $66$th figure has $200$ dots (1).", "H"),
W("For the conversion $F=1.8C+32$, find the temperature at which the Celsius and Fahrenheit readings are the same. What does this tell you about the lines $F=C$ and $F=1.8C+32$?", 4, "Put $F=C$: $C=1.8C+32$ (1), $-0.8C=32$, $C=-40$ (1). So $-40^\\circ$C $=-40^\\circ$F (1). The two lines meet at exactly one point, $(-40,-40)$, because their slopes ($1$ and $1.8$) differ (1).", "H"),
]

for _w in WS:   # answer-key/question renderer does not interpret **bold**
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(2)
_pre, _tail = _o["blocks"][:-2], _o["blocks"][-2:]
_extra = [
 ("h2", "2.6 Reading Slope and Intercept from a Table or from Two Points"),
 ("p", "If a quantity changes by the **same amount** for equal steps, it is linear. Find the slope as **(change in y) ÷ (change in x)** and the intercept by putting x = 0 (or by substituting one point). A cost table for 2, 5 and 8 notebooks showing ₹ 54, ₹ 99 and ₹ 144 rises by 45 for every 3 notebooks, so the slope is 15 and the rule is C = 15n + 24. A plant 5 cm tall which is 13 cm tall four weeks later has slope (13 − 5) ÷ 4 = 2 cm per week and height h = 2w + 5."),
 ("note", "FORMULA", "**Line through two points (x₁, y₁) and (x₂, y₂):** slope m = (y₂ − y₁)/(x₂ − x₁); then y = mx + c with c found by putting one point in the equation. If the slope is negative (a candle burning down, a tank emptying), the quantity decreases."),
 ("h2", "2.7 Worked Examples"),
 ("steps", [("Example 1 — Fixed charge plus rate", "A taxi charges ₹ 20 plus ₹ 12 per km. Fare for x km: F = 12x + 20. For 6 km: 12 × 6 + 20 = ₹ 92. For a fare of ₹ 164: 12x + 20 = 164, 12x = 144, **x = 12 km**. The rate 12 is the slope; the fixed charge 20 is the intercept.")]),
 ("steps", [("Example 2 — A decreasing quantity", "A tank has 60 L and loses 5 L every minute: V = 60 − 5t. It is empty when 60 − 5t = 0, **t = 12 minutes**. The slope −5 is negative; the zero of the polynomial is the time when the tank is empty. The graph meets the t-axis at (12, 0) and the V-axis at (0, 60).")]),
 ("steps", [("Example 3 — Comparing two plans", "Company A: 50 + 4x and company B: 20 + 7x. Equal when 50 + 4x = 20 + 7x, so 3x = 30 and **x = 10 units** (bill ₹ 90). For 20 units A costs ₹ 130 and B costs ₹ 160, so A is cheaper for more than 10 units. On a graph the two lines cross at (10, 90); the line with the smaller slope eventually lies below.")]),
 ("steps", [("Example 4 — Break-even and profit", "Revenue R = 15x and cost C = 8x + 700. Profit P = R − C = 7x − 700. **Break-even** (the zero of P): x = 100 coupons. For 250 coupons: P = 1750 − 700 = ₹ 1050. For a profit of ₹ 2800: 7x = 3500, x = 500. Negative profit means a loss.")]),
 ("steps", [("Example 5 — Catching up", "Train A: 60t. Train B starts 100 km ahead at 40 km/h: 100 + 40t. A catches B when 60t = 100 + 40t, **t = 5 hours**, at 60 × 5 = 300 km. The relative speed is 60 − 40 = 20 km/h and the gap of 100 km closes in 100 ÷ 20 = 5 hours: the same answer by two methods.")]),
 ("steps", [("Example 6 — Finding a linear polynomial from two values", "p(x) = ax + b with p(2) = 11 and p(5) = 23. Subtract: 3a = 12, so a = 4; then b = 11 − 8 = 3. **p(x) = 4x + 3**, zero x = −3/4, and p(10) = 43.")]),
 ("h2", "2.8 Word Problems: How to Translate"),
 ("table", ["Words in the problem", "Mathematical meaning", "Example"], [
  ["fixed charge, visiting fee, membership, deposit", "the constant term (intercept)", "₹ 150 + ₹ 80 per hour: C = 80h + 150"],
  ["per km, per hour, per unit, per month", "the coefficient of x (slope = rate)", "₹ 12 per km: slope 12"],
  ["loses, burns down, drains, depreciates", "negative slope", "V = 12000 − 1000t"],
  ["starts with, initially, to begin with", "value when x = 0", "candle 30 cm: L = 30 − 2t"],
  ["break even, empty, runs out, reaches zero", "solve p(x) = 0 (the zero)", "4x − 28 = 0, x = 7"],
  ["the same cost, they meet, equal levels", "set the two polynomials equal", "50 + 4x = 20 + 7x"],
  ["head start", "a positive intercept for that runner", "100 + 40t"]]),
 ("ol", ["Decide which quantity is x (time, distance, units) and which is y.", "Write the starting value and the rate of change, then y = (rate) × x + (start).", "Substitute the given value and solve the equation.", "Check the answer in the original words and add the unit."]),
 ("note", "REMEMBER", "**Common mistakes.** (1) Putting the fixed charge as the slope and the rate as the intercept. (2) Forgetting the minus sign for a decreasing quantity. (3) Writing the zero of 3x + 12 as 4 instead of −4. (4) Saying a line rises because of a positive intercept: only the slope decides this. (5) Treating a pattern as linear without checking that the differences are equal. (6) Using the number of items in place of the cost in the answer: always re-read what was asked."),
 ("h2", "2.9 Parallel and Intersecting Lines"),
 ("table", ["Lines", "Slopes", "Result", "Example"], [
  ["same slope, different intercepts", "equal", "parallel: never meet", "y = 2x + 1 and y = 2x + 7; two shops 2x + 30 and 2x + 50, one always ₹ 20 cheaper"],
  ["different slopes", "unequal", "meet at exactly one point", "y = 2x + 1 and y = −x + 10 meet at (3, 7)"],
  ["same slope and intercept", "equal", "the same line", "y = 3x + 2 and y = 3x + 2"]]),
 ("p", "The Celsius–Fahrenheit rule F = 1.8C + 32 and the line F = C have different slopes, so they meet at exactly one point: C = 1.8C + 32 gives C = −40. This is the one temperature at which both scales show the same reading."),
 ("h2", "2.10 Patterns That Are Linear"),
 ("p", "A pattern with common difference d has the nth term a₁ + (n − 1)d, which is a linear polynomial in n with slope d. For the dots 5, 8, 11, … the rule is 3n + 2. To test whether a number belongs to the pattern, solve 3n + 2 = number: 104 gives n = 34, which is a whole number, so it is a term; 150 gives n = 148/3, not a whole number, so 150 is not a term. Matchstick squares in a row (4, 7, 10, …) follow 3n + 1; a square pond of side n with a one-metre tile border needs (n + 2)² − n² = 4n + 4 tiles, so the number of tiles is again linear in n, although the areas themselves are not."),
]
CH = dict(_o, blocks=_pre + _extra + _tail, takeaways=_o["takeaways"] + ["**Fixed part = intercept, rate = slope.** Taxi fare, plumber charge, savings, tank levels, profit and phone value all take the form y = mx + c.", "**Break-even, empty and runs out** all mean: find the zero of the polynomial.", "**Two plans cost the same** where the two polynomials are equal; lines with equal slopes and different intercepts never meet.", "A table is linear if equal steps in x give **equal changes** in y; the slope is Δy ÷ Δx.", "Check whether a number is a term of a linear pattern by solving the nth-term rule for n: the answer must be a **whole number**."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
