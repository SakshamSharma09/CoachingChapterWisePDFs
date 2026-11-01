import random
from lib import mcq, Q, OR
from mk9 import M4, build
def lin(a, b, v="x"):
    t = ("" if a == 1 else "-" if a == -1 else str(a)) + v
    if b > 0: return f"{t}+{b}"
    if b < 0: return f"{t}-{-b}"
    return t
def sgn(n): return f"{n}" if n >= 0 else f"({n})"
A = []; B = []; C = []; D = []
# A: degree (5)
for poly, deg in [(r"$3x^2-5x+7$", 2), (r"$y^3+2y-1$", 3), (r"$-9$", 0), (r"$4z-3$", 1), (r"$x^4-3x^3+6x^2-2x+7$", 4)]:
    nm = {0: "constant", 1: "linear", 2: "quadratic", 3: "cubic", 4: "a polynomial of degree 4"}[deg]
    A.append(M4(f"The degree of the polynomial {poly} is:", str(deg), [str(d) for d in (deg + 1, deg - 1, deg + 2, deg + 3) if d >= 0 and d != deg][:3], f"highest power of the variable is {deg}"))
# A: evaluate linear (6)
for a, b, x in [(5, -3, 2), (2, 3, -6), (3, 1, 4), (-4, 7, 3), (6, -5, -2), (-2, -1, 5)]:
    v = a * x + b
    A.append(M4(f"The value of the linear polynomial ${lin(a,b)}$ at $x={x}$ is:", str(v), [str(a*x - b), str(v + a), str(-v)], f"${a}({x})+({b})={v}$"))
# A: evaluate quadratic (4)
for a, b, c, x in [(7, -4, 6, 0), (7, -4, 6, -3), (1, 2, -3, 2), (2, -1, 1, -1)]:
    v = a*x*x + b*x + c
    ps = f"{a}x^2" + (f"+{b}x" if b > 0 else f"-{-b}x") + (f"+{c}" if c > 0 else f"-{-c}")
    A.append(M4(f"The value of ${ps}$ at $x={x}$ is:", str(v), [str(a*x*x - b*x + c), str(v + 2), str(v - 3), str(v + 5)], f"substitute $x={x}$ to get {v}"))
# A: nth term (5)
for a1, d in [(3, 4), (5, 2), (10, -3), (1, 6), (7, 5)]:
    n = lin(d, a1 - d, "n")
    wr = [lin(d, a1, "n"), lin(a1, d, "n"), lin(d, -(a1 + d), "n"), lin(d, a1 - d + 1, "n")]
    A.append(M4(f"The sequence ${a1}, {a1+d}, {a1+2*d}, {a1+3*d},\\dots$ forms a linear pattern. Its $n$th term is:", f"${n}$", [f"${w}$" for w in wr], f"common difference ${d}$, so $a_n={n}$"))
# A: slope / intercept (6)
for a, b in [(2, 5), (-3, 1), (4, -7), (1, 3), (-1, -2), (5, 0)]:
    A.append(M4(f"For the line $y={lin(a,b)}$, the slope and the $y$-intercept are respectively:", f"${a}$ and ${b}$", [f"${b}$ and ${a}$", f"${-a}$ and ${b}$", f"${a}$ and ${-b}$", f"${a+1}$ and ${b+1}$"], "compare with $y=ax+b$"))
# A: point on line (4)
for a, b, x, y, on in [(2, 1, 7, 15, True), (3, -2, 2, 5, False), (-1, 4, 3, 1, True), (4, 3, 1, 8, False)]:
    ans = "lies on the line" if on else "does not lie on the line"
    A.append(M4(f"The point $({x},\\,{y})$ ___ the line $y={lin(a,b)}$.", ans, ["lies on the line" if not on else "does not lie on the line", "is the $y$-intercept of the line", "is the origin"], f"RHS at $x={x}$ is ${a*x+b}$, {'equal to' if on else 'not equal to'} ${y}$"))
# A hand (10)
A += [
 M4(r"Which of the following is a linear polynomial?", r"$5x-8$", [r"$x^2+1$", r"$7$", r"$x^3-x$"], "degree 1"),
 M4(r"The coefficient of $x^2$ in $x^4-3x^3+6x^2-2x+7$ is:", "6", ["−3", "−2", "7"], "read off the term $6x^2$"),
 M4(r"The constant term of $9x^3+5x^2-8x-10$ is:", "−10", ["9", "−8", "5"], "term without the variable"),
 M4(r"A straight line $y=ax$ always passes through:", "the origin", ["the point $(1,\\,1)$ only", "the $y$-axis at $(0,\\,a)$", "no fixed point"], "$x=0\\Rightarrow y=0$"),
 M4(r"The lines $y=3x+2$ and $y=3x-5$ are:", "parallel", ["perpendicular", "coincident", "intersecting at the origin"], "equal slopes, different intercepts"),
 M4(r"A linear growth is represented by a straight line with:", "positive slope", ["negative slope", "zero intercept", "undefined slope"], "values increase with $x$"),
 M4(r"The graph of $y=-2x$ rises or falls as $x$ increases?", "falls (negative slope)", ["rises", "is horizontal", "is vertical"], "slope $-2<0$"),
 M4(r"If $y=ax+b$ passes through $(0,\,4)$ and $(1,\,7)$, then $a+b$ equals:", "7", ["3", "4", "11"], "$b=4$, $a=3$ ⇒ $a+b=7$"),
 M4(r"A student claims: “$5x^2-3$ is a linear polynomial.” The correct response is:", r"False, its degree is 2 so it is quadratic", ["True", "True only for $x>0$", "Cannot be determined"], "degree of $5x^2-3$ is 2"),
 M4(r"The perimeter of a square of side $x$ cm is a linear polynomial. For side 2.5 cm it is:", "10 cm", ["6.25 cm", "5 cm", "12.5 cm"], "$4x=10$"),
]
assert len(A) == 40, len(A)

# B (16)
for a1, d, n in [(4, 3, 10), (2, 5, 12), (100, -5, 8), (7, 4, 15)]:
    an = a1 + (n - 1) * d
    B.append(Q(f"A linear pattern begins ${a1},\\ {a1+d},\\ {a1+2*d},\\dots$ Write the expression for its $n$th term and find the {n}th term.", f"$a_n={d}n+({a1-d})$; $a_{{{n}}}={d}({n})+({a1-d})=\\mathbf{{{an}}}$", "1+1"))
for a, b, x1, x2 in [(5, -3, 0, -1), (3, 4, 2, -2), (-2, 6, 1, 4), (4, -1, 3, 0)]:
    B.append(Q(f"Find the values of the linear polynomial ${lin(a,b)}$ at $x={x1}$ and $x={x2}$.", f"At $x={x1}$: ${a}({x1})+({b})={a*x1+b}$; at $x={x2}$: ${a}({x2})+({b})={a*x2+b}$", "1+1"))
B += [
 Q(r"A chess club charges ₹200 joining fee plus ₹50 per match. Write the expression for the amount paid for $m$ matches and find $m$ if a player paid ₹750.", r"Amount $=200+50m$. $200+50m=750\Rightarrow m=11$ matches.", "1+1"),
 Q(r"Find the equation of the line through $(0,\,3)$ with slope 2. Where does it cut the $y$-axis?", r"$y=2x+3$; it cuts the $y$-axis at $(0,3)$.", "1+1"),
 Q(r"State the slope and $y$-intercept of $y=-4x+9$ and say whether it shows linear growth or decay.", r"Slope $=-4$, $y$-intercept $=9$; negative slope ⇒ linear decay.", "1+1"),
 Q(r"The height of water in a tank is $h(t)=3-0.5t$ metres after $t$ months. Find the height after 5 months and the time when the tank is empty.", r"$h(5)=3-2.5=0.5$ m. Empty when $3-0.5t=0\Rightarrow t=6$ months.", "1+1"),
 Q(r"Show that $(7,\,15)$ lies on the line $y=2x+1$ but $(3,\,8)$ does not.", r"$2(7)+1=15$ ✓. $2(3)+1=7\ne8$ ✗.", "1+1"),
 Q(r"Write the number of tiles in stage $n$ if the pattern $1,3,5,7,\dots$ is followed, and find which stage has 47 tiles.", r"$2n-1$. $2n-1=47\Rightarrow n=24$.", "1+1"),
 Q(r"An auto-rickshaw fare is ₹25 for the first 2 km and ₹15 for every further km. Find the fare for 10 km.", r"$25+15\times8=₹145$.", "1+1"),
 Q(r"The sum of two numbers is 64 and one is 10 more than the other. Form a linear equation and find the numbers.", r"$x+(x+10)=64\Rightarrow x=27$; numbers 27 and 37.", "1+1"),
]
assert len(B) == 16, len(B)

# C (24): 3 marks
C += [
 Q(r"The present age of Salil's mother is three times his age. After 5 years their ages will add up to 70. Find their present ages.", r"Let Salil's age $=x$, mother $=3x$. $(x+5)+(3x+5)=70\Rightarrow4x=60\Rightarrow x=15$. Salil 15 years, mother 45 years.", "1+1+1"),
 Q(r"The difference between two positive integers is 63 and their ratio is 2 : 5. Find the integers.", r"Let the numbers be $2k$ and $5k$: $5k-2k=63\Rightarrow k=21$. Numbers: 42 and 105.", "1+1+1"),
 Q(r"Ruby has 3 times as many ₹2 coins as ₹5 coins. If she has ₹88 in all, how many coins of each type does she have?", r"₹5 coins $=x$, ₹2 coins $=3x$. $5x+6x=88\Rightarrow x=8$. So 8 five-rupee coins and 24 two-rupee coins.", "1+1+1"),
 Q(r"A farmer cuts a 300 ft fence into two pieces; the longer is four times the shorter. Find the lengths.", r"$x+4x=300\Rightarrow x=60$. Pieces: 60 ft and 240 ft.", "1+1+1"),
 Q(r"The length of a rectangle is 3 more than twice its width and its perimeter is 24 cm. Find its dimensions.", r"Width $=w$, length $=2w+3$. $2(3w+3)=24\Rightarrow w=3$. Width 3 cm, length 9 cm.", "1+1+1"),
 Q(r"A rally starts with 120 members and 9 drop out every hour. Find a linear expression for the number remaining at the end of the $n$th hour and the number after 7 hours.", r"$120-9n$; after 7 hours: $120-63=57$.", "2+1"),
 Q(r"A learning platform charges a fixed monthly fee plus a cost per module. For 10 modules the bill is ₹400 and for 14 modules ₹500. Find $a$ and $b$ in $y=ax+b$.", r"$400=10a+b$, $500=14a+b$. Subtract: $4a=100\Rightarrow a=25$; $b=400-250=150$. $y=25x+150$.", "1+1+1"),
 Q(r"A gym charges a fixed fee plus a rate per hour of court use: 10 h costs ₹800 and 15 h costs ₹1100. Find the relation $y=ax+b$ and the bill for 20 h.", r"$800=10a+b$, $1100=15a+b\Rightarrow a=60,\ b=200$. $y=60x+200$; for $x=20$: ₹1400.", "2+1"),
 Q(r"Find $a$ and $b$ in °C $=a\,$°F$+b$, given that ice melts at 0 °C (32 °F) and water boils at 100 °C (212 °F). Then convert 98.6 °F to °C.", r"$0=32a+b$, $100=212a+b\Rightarrow180a=100$, $a=\frac59$, $b=-\frac{160}9$. °C $=\frac59(°F-32)$. At 98.6 °F: $\frac59\times66.6=37$ °C.", "1+1+1"),
 Q(r"The cost of a journey is $C(d)=100+60d$. Find the cost of 15 km and the distance for a cost of ₹700. Is it linear growth or decay?", r"$C(15)=100+900=₹1000$. $100+60d=700\Rightarrow d=10$ km. Positive slope 60 ⇒ linear growth.", "1+1+1"),
 Q(r"A plant 1.75 ft tall grows 0.5 ft every month. Write $h$ in terms of $t$ (months), find the height after 7 months and explain why this is linear growth.", r"$h=1.75+0.5t$; $h(7)=5.25$ ft. The height rises by the same 0.5 ft each month (constant positive slope).", "1+1+1"),
 Q(r"A phone bought for ₹10,000 loses ₹800 every year. Find its value after 3 years, write $v$ in terms of $t$ and after how many years it becomes ₹4,000.", r"$v=10000-800t$; $v(3)=7600$. $10000-800t=4000\Rightarrow t=7.5$ years.", "1+1+1"),
 Q(r"The balance of a prepaid plan is ₹600 and it reduces by ₹15 daily. Write $b(x)$ and find after how many days it runs out.", r"$b(x)=600-15x$; zero when $x=40$ days. Negative slope ⇒ linear decay.", "2+1"),
 Q(r"Without plotting, state the $y$-intercept and say which of the lines $y=2x-1$, $y=2x+1$ and $y=2x+5$ are parallel. Give a reason.", r"Intercepts $-1$, $1$, $5$. All three have slope 2, so they are parallel (equal slopes, different intercepts).", "1+1+1"),
 Q(r"Draw (describe the points for) the graphs of $y=\frac12x$, $y=x$ and $y=2x$ using suitable points. What does the value of $a$ in $y=ax$ tell about the line?", r"Points: $(0,0),(4,2)$; $(0,0),(2,2)$; $(0,0),(2,4)$. All pass through the origin; larger $a$ ⇒ steeper line; $a=1$ makes equal angles with both axes.", "2+1"),
 Q(r"Write the coordinates of three points on the line $y=3x-2$ and state where it cuts the $y$-axis.", r"For $x=0,1,2$: $(0,-2)$, $(1,1)$, $(2,4)$. It cuts the $y$-axis at $(0,-2)$.", "2+1"),
 Q(r"The points $(-3,6)$, $(-2,4)$, $(0,0)$, $(1,-2)$ lie on a line. Find its equation and its slope. What does the slope tell?", r"$y=-2x$ (each $y$ is $-2$ times $x$). Slope $-2$ ⇒ the line falls; $y$ decreases by 2 for each unit increase in $x$ (linear decay).", "1+1+1"),
 Q(r"The area of a rectangle of length 13 cm and breadth $b$ cm is a linear polynomial in $b$. Find it for $b=12,10,8$ and write the pattern.", r"$A=13b$: $156,\ 130,\ 104$ cm$^2$. The area changes by $13\times$ (change in $b$); a linear pattern with constant difference 26 for a decrease of 2 cm in $b$.", "2+1"),
 Q(r"The volume of a box of length 7 cm and breadth 11 cm is a linear polynomial in the height $h$. Find the volume for $h=5,9,13$.", r"$V=77h$: $385,\ 693,\ 1001$ cm$^3$. Consecutive differences are equal (308) — a linear pattern.", "2+1"),
 Q(r"Sarita has a 500-page book and reads 20 pages a day. Write the pages left after $d$ days and find the days needed to finish.", r"$500-20d$; zero when $d=25$ days. After 15 days, 200 pages remain.", "2+1"),
 Q(r"A student has ₹500 in her account and receives ₹150 every month. Write a linear expression for the amount in the $n$th month (from the second month onwards) and find in which month she will have ₹1,850.", r"First month ₹500; second ₹650… $a_n=500+150(n-1)=350+150n$. $350+150n=1850\Rightarrow n=10$.", "1+1+1"),
 Q(r"The wire of length 20 cm is bent into a rectangle of length $x$ cm. Write the area in terms of $x$ and find it for $x=6$.", r"Width $=10-x$; area $=x(10-x)=10x-x^2$ (a quadratic polynomial). At $x=6$: $60-36=24$ cm$^2$.", "2+1"),
 Q(r"Given $y=2x+1$, complete the table: $x=1,2,5,7,9,12,20$ and check which of the points lies on the line: $(4,9)$ or $(6,14)$.", r"$y=3,5,11,15,19,25,41$. $(4,9)$: $2(4)+1=9$ ✓ lies on the line; $(6,14)$: $2(6)+1=13\ne14$ ✗.", "2+1"),
 Q(r"Solve the linear equation $3x-4=11$ and verify the solution. Also write a word problem that leads to $2x+10=64$.", r"$3x=15\Rightarrow x=5$; check $3(5)-4=11$ ✓. Example: the sum of two numbers is 64 and one is 10 more than the other: $x+(x+10)=64\Rightarrow2x+10=64$.", "1+1+1"),
]
assert len(C) == 24, len(C)

# D (16): 5 marks
D += [
 Q(r"<b>Case study:</b> A taxi company charges ₹100 as a fixed fee and ₹60 per km. The cost for $d$ km is $C(d)=100+60d$. (i) Find the cost for 5 km and 15 km. (ii) For how many km is the cost ₹700? (iii) Is this linear growth or decay? Write the slope and $y$-intercept and what each means.", r"(i) $C(5)=400$, $C(15)=1000$. (ii) $100+60d=700\Rightarrow d=10$ km. (iii) Linear growth; slope 60 = cost per km, intercept 100 = fixed charge.", "2+1+2"),
 Q(r"(i) Plot the graphs of $y=2x-1$, $y=2x+1$ and $y=2x+5$ on the same axes by choosing points. (ii) What do you observe about the lines? (iii) Where does $y=2x+5$ cut the $y$-axis?", r"(i) e.g. $y=2x-1$: $(0,-1),(1,1)$; $y=2x+1$: $(0,1),(1,3)$; $y=2x+5$: $(0,5),(1,7)$. (ii) All parallel (same slope 2); they shift up/down as $b$ changes. (iii) $(0,5)$.", "3+1+1"),
 Q(r"<b>Case study:</b> A growing pattern of tiles has 1, 3, 5, 7, … tiles in stages 1, 2, 3, 4. (i) Find the expression for the number of tiles in stage $n$. (ii) How many tiles are there in stages 15 and 26? (iii) Which stage has 21 tiles? Which has 47? (iv) What is the slope of the line $y=2x-1$ and what does it represent?", r"(i) $2n-1$. (ii) $29$ and $51$. (iii) $2n-1=21\Rightarrow n=11$; $n=24$ for 47. (iv) Slope 2 = constant difference between consecutive terms.", "1+1+2+1"),
 Q(r"A telecom company charges a fixed fee and a rate per GB. When 10 GB are used the bill is ₹350; for 20 GB it is ₹550. (i) Find $a$ and $b$ in $y=ax+b$. (ii) Write the relation and find the bill for 35 GB. (iii) What do $a$ and $b$ represent?", r"(i) $350=10a+b$, $550=20a+b$ ⇒ $a=20$, $b=150$. (ii) $y=20x+150$; $x=35$: ₹850. (iii) ₹20 per GB and ₹150 fixed monthly fee.", "2+2+1"),
 Q(r"(i) Solve: the sum of two numbers is 64 and one is 10 more than the other. (ii) The ages of a mother and son are in the ratio 3 : 1 and after 5 years their ages sum to 70. Find their present ages.", r"(i) $x+(x+10)=64\Rightarrow x=27$; numbers 27, 37. (ii) $3x+5+x+5=70\Rightarrow x=15$; son 15, mother 45.", "2+3"),
 Q(r"<b>Case study:</b> A water tank has height $h(t)=3-0.5t$ m of water after $t$ months of summer. (i) Make a table for $t=0$ to 6. (ii) Is it growth or decay? Why? (iii) When does the tank become empty? (iv) Draw (describe) the graph and state its slope and intercept.", r"(i) $t$: 0,1,2,3,4,5,6 → $h$: 3, 2.5, 2, 1.5, 1, 0.5, 0. (ii) Linear decay — constant decrease of 0.5 m per month. (iii) At $t=6$ months. (iv) Straight line through $(0,3)$ and $(6,0)$; slope $-0.5$, $h$-intercept 3.", "1+1+1+2"),
 Q(r"Find $a$ and $b$ in $°C=a\,°F+b$ given ice melts at 0 °C = 32 °F and water boils at 100 °C = 212 °F. Hence convert (i) 77 °F to °C and (ii) 25 °C to °F.", r"$a=\frac59$, $b=-\frac{160}9$. (i) $\frac59(77-32)=25$ °C. (ii) $25=\frac59(F-32)\Rightarrow F=77$ °F.", "3+1+1"),
 Q(r"A mobile phone costs ₹10,000 and loses ₹800 in value every year. (i) Find its value after 3 years. (ii) Make a table for $t=0$ to 8 years. (iii) Write $v$ in terms of $t$ and explain why this is linear decay. (iv) After how many years will its value be ₹2,000?", r"(i) ₹7,600. (ii) 10000, 9200, 8400, 7600, 6800, 6000, 5200, 4400, 3600. (iii) $v=10000-800t$; constant decrease ₹800 per year. (iv) $10000-800t=2000\Rightarrow t=10$ years.", "1+1+2+1"),
]
D += [
 Q(r"<b>Case study:</b> A farmer cuts a 300-ft fence into two pieces; the longer is four times the shorter. A rectangular plot has length 3 more than twice its width and perimeter 24 m. (i) Find the two pieces. (ii) Find the dimensions of the plot. (iii) Find the area of the plot.", r"(i) $x+4x=300\Rightarrow$ 60 ft and 240 ft. (ii) $2(3w+3)=24\Rightarrow w=3$ m, $l=9$ m. (iii) $27$ m$^2$.", "2+2+1"),
 Q(r"Draw the graphs of $y=3x$ and $y=-3x$ using suitable points. (i) Where do they meet? (ii) Compare their slopes. (iii) State what the sign of the slope tells about growth and decay.", r"Points: $(0,0),(1,3)$ and $(0,0),(1,-3)$. (i) At the origin. (ii) Slopes $3$ and $-3$; same steepness, opposite directions. (iii) Positive slope ⇒ growth; negative slope ⇒ decay.", "2+1+2"),
 Q(r"The points $(0,\,5)$ and $(4,\,13)$ lie on a line $y=ax+b$. (i) Find $a$ and $b$. (ii) Write the equation. (iii) Is $(10,25)$ on the line? (iv) Find the point where the line cuts the $x$-axis.", r"(i) $b=5$; $13=4a+5\Rightarrow a=2$. (ii) $y=2x+5$. (iii) $2(10)+5=25$ ✓ yes. (iv) $y=0\Rightarrow x=-2.5$: $(-2.5,0)$.", "2+1+1+1"),
 Q(r"<b>Case study:</b> Reiaan's school sells notebooks at ₹x each. The cost for $n$ notebooks including a one-time ₹20 bag fee is $20+x\,n$. For 5 notebooks the bill is ₹70. (i) Find $x$. (ii) Write the cost function. (iii) Find the cost of 12 notebooks. (iv) How many notebooks can be bought for ₹170?", r"(i) $20+5x=70\Rightarrow x=10$. (ii) $C(n)=20+10n$. (iii) ₹140. (iv) $20+10n=170\Rightarrow n=15$.", "1+1+1+2"),
 Q(r"(i) Find the value of $5x^2-3x+7$ at $x=1$ and $x=-2$. (ii) Write a cubic polynomial in $x$ whose $x^2$ coefficient is $-7$. (iii) State the degree of $4z^3+5z^2-11$ and the coefficient of $z$.", r"(i) $x=1$: $9$; $x=-2$: $20+6+7=33$. (ii) e.g. $x^3-7x^2+2x+1$. (iii) Degree 3; coefficient of $z$ is 0 (no $z$ term).", "2+2+1"),
 Q(r"<b>Case study:</b> A student has ₹500 in her savings account and gets ₹150 every month. (i) Write a linear expression for the amount after $n$ months. (ii) Find the amount after 6 months. (iii) After how many months will she have ₹2,000? (iv) Plot (describe) the graph and identify the slope.", r"(i) $A=500+150n$. (ii) ₹1,400. (iii) $500+150n=2000\Rightarrow n=10$. (iv) A straight line through $(0,500)$ and $(10,2000)$; slope 150 = monthly addition.", "1+1+1+2"),
 Q(r"Find the equation of the line passing through $(1,\,3)$ and $(3,\,7)$. Also (i) check whether $(5,\,11)$ lies on it, (ii) find its $y$-intercept, (iii) write the equation of a parallel line through $(0,\,-1)$.", r"$3=a+b$, $7=3a+b\Rightarrow a=2$, $b=1$: $y=2x+1$. (i) $2(5)+1=11$ ✓. (ii) $1$. (iii) $y=2x-1$.", "2+1+1+1"),
 Q(r"A rectangular garden has length $l$ m and width $w$ m. Wire fencing costs ₹100/m along the length (both sides), wooden fencing ₹80/m along the width (both sides) and seeding ₹50/m$^2$. (i) Write the expression for the total cost. (ii) Find it for $l=20$, $w=10$. (iii) Name the terms, variables and coefficients.", r"(i) $200l+160w+50lw$. (ii) $4000+1600+10000=₹15,600$. (iii) Terms: $200l$, $160w$, $50lw$; variables $l$, $w$; coefficients 200, 160, 50.", "2+2+1"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
