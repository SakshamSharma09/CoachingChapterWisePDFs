"""Class 9 Maths Ch 11 - World of Algorithms: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import gcd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch11"

def _old(n):
    d = "c9_maths1" if n < 9 else "c9_maths2"
    p = Path(__file__).resolve().parents[1] / "rn_work" / d / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def divs(n): return [d for d in range(1, n + 1) if n % d == 0]
def sub_steps(m, n):
    c = 0
    while n:
        if m < n: m, n = n, m
        m, n = n, m - n; c += 1
    return m, c
def div_steps(m, n):
    c = 0
    while n: m, n = n, m % n; c += 1
    return m, c
assert 17 % 5 == 2 and gcd(24, 36) == 12 and len(divs(18)) == 6 and divs(13) == [1, 13] and 3478+2589 == 6067 and 4865+7358 == 12223
assert divs(20) == [1, 2, 4, 5, 10, 20] and len(divs(24)) == 8 and 47 % 6 == 5 and 100 % 7 == 2 and (9+50) % 12 == 11
assert [d for d in divs(18) if 24 % d == 0] == [1, 2, 3, 6] and gcd(120, 150) == 30 and sub_steps(35, 14) == (7, 4) and divs(51) == [1, 3, 17, 51]
assert 5947+3865 == 9812 and gcd(375, 825) == 75 and 375//75+825//75 == 16 and gcd(60, 16) == 4 and gcd(252, 105) == 21 and sub_steps(48, 18) == (6, 5)
assert sum(j for j in range(1, 11) if j % 2 == 0) == 30 and gcd(36, 48) == 12 and 36//12+48//12 == 7 and divs(91) == [1, 7, 13, 91]
assert all(97 % p for p in (2, 3, 5, 7)) and gcd(1071, 462) == 21 and 3347+2729 == 6076 and 6076//60 == 101
assert sum(map(int, "4729")) == 22 and 100 % 12 == 4 and 100//12 == 8 and sub_steps(825, 375) == (75, 7) and div_steps(825, 375) == (75, 2)
assert [j for j in range(1, 31) if j % 3 == 0 and j % 2 == 1] == [3, 9, 15, 21, 27] and sum([3, 9, 15, 21, 27]) == 75
assert gcd(gcd(84, 126), 210) == 42 and 84//42+126//42+210//42 == 10 and div_steps(91, 35) == (7, 4) and sub_steps(91, 35)[0] == 7
assert div_steps(252, 198) == (18, 4) and div_steps(1071, 462) == (21, 3) and gcd(180, 150) == 30 and sum(divs(28)) == 56
assert [k for k in range(2, 37) if 36 % k == 0 and 48 % k == 0] == [2, 3, 4, 6, 12] and 462//21*1071//21 == 22*51 == 1122 and 1071//21 == 51 and 462//21 == 22
assert 365 % 7 == 1 and 1000 % 7 == 6 and 1000 % 6 == 4 and 1000//6 == 166 and gcd(1000, 6) == 2 and gcd(101, 100) == 1 and gcd(8, 15) == 1
assert sum(map(int, "52718")) == 23 and div_steps(89, 55) == (1, 9) and 999+999 == 1998 and 9999+1 == 10000 and 825 - 2*375 == 75 and gcd(2*500+1, 2) == 1
assert sub_steps(1001, 2)[1] in range(495, 510)

WS = [
# ---------------- EASY ----------------
W(r"The value of $17 \bmod 5$ (the remainder when 17 is divided by 5) is:", 1, r"(b) 2, since $17=5\times3+2$. (1)", "E", opts=["3", "2", "12", "1"]),
W(r"The gcd of 24 and 36 is:", 1, r"(c) 12. Common divisors of 24 and 36: $1,2,3,4,6,12$; the largest is 12. (1)", "E", opts=["6", "4", "12", "72"]),
W(r"The list divisors(18) has how many entries?", 1, r"(d) 6. divisors(18) $=[1,2,3,6,9,18]$. (1)", "E", opts=["4", "5", "9", "6"]),
W(r"When two digits and a carry are added in a column, the new carry can be at most:", 1, r"(a) 1. The largest column total is $9+9+1=19$, which is one ten and 9 units. (1)", "E", opts=["1", "2", "9", "10"]),
W(r"In Euclid's algorithm the value of $\gcd(25, 0)$ is:", 1, r"(c) 25. The rule is $\gcd(m,0)=m$ (every number divides 0). (1)", "E", opts=["0", "1", "25", "5"]),
W(r"The list divisors(13) is:", 1, r"(b) $[1, 13]$. 13 is prime, so it has exactly two divisors. (1)", "E", opts=["$[13]$", "$[1, 13]$", "$[1, 3, 13]$", "$[1, 2, 13]$"]),
W(r"Add $3478+2589$ column by column. Write the digit and the carry for each column.", 2, r"Units: $8+9=17$, write 7, carry 1. Tens: $7+8+1=16$, write 6, carry 1. Hundreds: $4+5+1=10$, write 0, carry 1. Thousands: $3+2+1=6$ (1). Answer $6067$ (1).", "E"),
W(r"A shopkeeper adds two bills, ₹ 4,865 and ₹ 7,358, by the column method. Write the carry in each column and the final answer.", 2, r"Units $5+8=13$ (3, carry 1); tens $6+5+1=12$ (2, carry 1); hundreds $8+3+1=12$ (2, carry 1); thousands $4+7+1=12$ (2, carry 1); final carry 1 is written to the left (1). Total ₹ 12,223 (1).", "E", wp=True),
W(r"Write the list divisors(20) using the algorithm 'for each $j$ from 1 to 20, if $j$ divides 20 add $j$ to the list'.", 2, r"$j=1,2,4,5,10,20$ divide 20 (1). List $=[1,2,4,5,10,20]$, in increasing order (1).", "E"),
W(r"24 chocolates are to be shared equally among some children with none left over. List all possible numbers of children.", 2, r"The number of children must divide 24, so divisors(24) (1) $=[1,2,3,4,6,8,12,24]$: 8 possibilities (1).", "E", wp=True),
W(r"Find (i) $47 \bmod 6$ (ii) $100 \bmod 7$.", 2, r"(i) $47=6\times7+5$, so 5 (1). (ii) $100=7\times14+2$, so 2 (1).", "E"),
W(r"A clock shows 9 o'clock. What time will it show after 50 hours? (Use $\bmod 12$.)", 2, r"$9+50=59$ (1). $59 \bmod 12=11$ (as $59=12\times4+11$), so it shows 11 o'clock (1).", "E", wp=True),
W(r"Find $\gcd(18, 24)$ by listing the divisors of both numbers and picking the rightmost common divisor.", 2, r"divisors(18) $=[1,2,3,6,9,18]$ and divisors(24) $=[1,2,3,4,6,8,12,24]$ (1). Common $=[1,2,3,6]$; the rightmost entry is the gcd, 6 (1).", "E"),
W(r"A floor 120 cm by 150 cm is to be covered fully by square tiles with no cutting. What is the side of the largest possible tile?", 2, r"The side must divide both 120 and 150, so it is $\gcd(120,150)$ (1). $150=120\times1+30$, $120=30\times4+0$, so the gcd is 30 cm (1).", "E", wp=True),
W(r"Use $\gcd(m,n)=\gcd(n,m-n)$ repeatedly to find $\gcd(35,14)$. Write the chain of pairs.", 2, r"$(35,14)\to(14,21)\to(21,14)\to(14,7)\to(7,7)\to(7,0)$ (1.5). The gcd is 7 (0.5).", "E"),
W(r"Is 29 prime? Is 51 prime? Use the lists divisors(29) and divisors(51).", 2, r"divisors(29) $=[1,29]$, exactly two entries, so 29 is prime (1). divisors(51) $=[1,3,17,51]$, four entries, so 51 is not prime (1).", "E"),
W(r"True or false (give a reason): while adding two numbers column by column the carry can sometimes be 2.", 2, r"**False.** The largest column total is $9+9+1=19$, so the carry is 0 or 1 (2).", "E"),
# ---------------- MEDIUM ----------------
W(r"Add $5947+3865$ by the column algorithm and show the carry after each column.", 2, r"Units $7+5=12$ (2, c1); tens $4+6+1=11$ (1, c1); hundreds $9+8+1=18$ (8, c1); thousands $5+3+1=9$ (c0) (1). Answer $9812$ (1).", "M"),
W(r"Two ropes of lengths 375 cm and 825 cm are to be cut into equal pieces of the greatest possible length with no waste. Find the length of each piece and the total number of pieces.", 3, r"Length $=\gcd(375,825)$; $825=375\times2+75$ and $375=75\times5+0$, so 75 cm (2). Pieces $=\frac{375}{75}+\frac{825}{75}=5+11=16$ (1).", "M", wp=True),
W(r"Use Euclid's division method $\gcd(m,n)=\gcd(n,m \bmod n)$ to find $\gcd(60,16)$. Write each division.", 3, r"$60=16\times3+12$ (1). $16=12\times1+4$ (1). $12=4\times3+0$, so the gcd is 4 (1).", "M"),
W(r"Find $\gcd(252,105)$ using repeated division. Write each step.", 3, r"$252=105\times2+42$ (1). $105=42\times2+21$ (1). $42=21\times2+0$, so the gcd is 21 (1).", "M"),
W(r"Use the subtraction rule ($\gcd(m,n)=\gcd(n,m-n)$, reversing the pair when $m<n$) to find $\gcd(48,18)$. Write the chain and say how many times the subtraction step was used.", 3, r"$(48,18)\to(18,30)\to(30,18)\to(18,12)\to(12,6)\to(6,6)\to(6,0)$ (1.5). The gcd is 6 (0.5). The subtraction step was used 5 times (1).", "M"),
W(r"To find $\gcd(99,2)$ the subtraction method reduces 99 by 2 again and again. Roughly how many reductions are needed? How many does the division method need? What does this show?", 2, r"Subtraction: $99\to97\to95\to\cdots\to1$, about 50 reductions (1). Division: $(99,2)\to(2,1)\to(1,0)$, only 2 (0.5). The subtraction effort depends on the value of the numbers; division on the number of digits (0.5).", "M"),
W(r"Today is Monday. Using remainders on division by 7, find the day of the week 100 days from today.", 2, r"$100 \bmod 7=2$ (as $100=7\times14+2$) (1). Two days after Monday is Wednesday (1).", "M", wp=True),
W(r"Trace this algorithm and give its output: 'Set sum = 0. For each $j$ from 1 to 10: if $j$ is even, add $j$ to sum. Report sum.'", 3, r"The even $j$ are $2,4,6,8,10$ (1). sum goes $2, 6, 12, 20, 30$ (1). Output: 30 (1).", "M"),
W(r"In the 'most-recent-common-divisor' algorithm (start with 1; for $k=2$ to $\min(m,n)$, if $k$ divides both, set it to $k$), run $m=12$, $n=18$ and write the successive values.", 3, r"$k=2$: divides both, value 2. $k=3$: value 3. $k=4$, 5: no. $k=6$: value 6. $k=7$ to 12: no (1.5). Values: $1\to2\to3\to6$ (1). gcd $=6$ (0.5).", "M"),
W(r"A shelf-maker has 36 history books and 48 science books. Each shelf must hold the same number of books of only one subject. What is the greatest number of books per shelf, and how many shelves are needed?", 3, r"Books per shelf must divide both 36 and 48, so it is $\gcd(36,48)=12$ ($48=36\times1+12$, $36=12\times3$) (2). Shelves $=3+4=7$ (1).", "M", wp=True),
W(r"Decide whether 91 and 97 are prime. For 91 give divisors(91). For 97 explain which numbers you tested.", 3, r"divisors(91) $=[1,7,13,91]$ (7 × 13), so 91 is not prime (1.5). 97 is not divisible by 2, 3, 5 or 7 ($7\times13=91$, $7\times14=98$) and no larger divisor is possible up to its square root, so it is prime (1.5).", "M"),
W(r"Find $\gcd(1071,462)$ by Euclid's division method, writing each division.", 3, r"$1071=462\times2+147$ (1). $462=147\times3+21$ (1). $147=21\times7+0$; gcd $=21$ (1).", "M"),
W(r"Counting dots one by one at 1 second per dot, how long would $3347+2729$ take? The column method takes 15 seconds per column. How long does it take? Compare.", 3, r"Dots $=3347+2729=6076$, i.e. 6076 s $\approx$ 1 h 41 min (1.5). Column method: 4 columns $\times$ 15 s $=60$ s (1). Counting grows with the value, the column method with the number of digits (0.5).", "M", wp=True),
W(r"Trace: 'Set total = 0 and $n=4729$. While $n>0$: let $d=n \bmod 10$; add $d$ to total; replace $n$ by $(n-d)/10$.' Write the values of $d$ and the final total.", 3, r"$n=4729$: $d=9$; $n=472$: $d=2$; $n=47$: $d=7$; $n=4$: $d=4$; then $n=0$ stops (2). Total $=9+2+7+4=22$ (1).", "M"),
W(r"A caterer packs 100 laddoos into boxes of 12. How many boxes are filled and how many laddoos are left? Which operation gives the leftover?", 3, r"$100=12\times8+4$ (1.5). 8 boxes are filled and 4 laddoos are left (1). The leftover is $100 \bmod 12=4$ (0.5).", "M", wp=True),
W(r"Check that $\gcd(m,n)$ and $\gcd(n,m-n)$ have the same common divisors for $m=84$, $n=36$.", 3, r"Common divisors of 84 and 36: $1,2,3,4,6,12$ (1). $m-n=48$; common divisors of 36 and 48: $1,2,3,4,6,12$ (1). The lists are equal, so both gcds are 12 (1).", "M"),
W(r"Apply the subtraction method to $\gcd(825,375)$ and count how many times the subtraction step is used. How many divisions does Euclid's division method need for the same pair?", 3, r"$(825,375)\to(375,450)\to(450,375)\to(375,75)\to(75,300)\to(300,75)\to(75,225)\to(225,75)\to(75,150)\to(150,75)\to(75,75)\to(75,0)$: the step is used 7 times (2). Division: $825=375\times2+75$, $375=75\times5+0$: 2 divisions (1).", "M"),
W(r"Anil checks common divisors of 12 and 100 for every $k$ from 1 to 100. Why is it enough to check up to 12? How many values of $k$ does he save?", 2, r"A common divisor cannot be larger than the smaller number, 12 (1). He saves $100-12=88$ checks (1).", "M"),
W(r"A student's algorithm: 'For each $j$ from 1 to 30: if $j$ is a multiple of 3 and $j$ is odd, add $j$ to a list. Report the list and the sum.' Trace it.", 3, r"Odd multiples of 3 up to 30: $3,9,15,21,27$ (2). Sum $=75$ (1).", "M"),
# ---------------- HARD ----------------
W(r"Three ribbons of lengths 84 cm, 126 cm and 210 cm are cut into the longest equal pieces with no waste. Find the piece length using the division method on pairs, and the total number of pieces.", 4, r"$\gcd(84,126)$: $126=84\times1+42$, $84=42\times2+0$, so 42 (1.5). $\gcd(42,210)$: $210=42\times5$, so 42 cm (1). Pieces $=2+3+5=10$ (1.5).", "H", wp=True),
W(r"Show that if $d$ divides $m$ and $n$ ($m\geq n$), then $d$ divides $m-n$, and that if $d$ divides $n$ and $m-n$, then $d$ divides $m$. Hence explain $\gcd(m,n)=\gcd(n,m-n)$.", 4, r"Let $m=ad$, $n=bd$; then $m-n=(a-b)d$, divisible by $d$ (1.5). Let $n=xd$, $m-n=yd$; then $m=n+(m-n)=(x+y)d$ (1.5). So both pairs have identical common divisors, hence the same greatest one (1).", "H"),
W(r"**Trace the algorithm.** Input $m,n$. Step 1: $r=m \bmod n$. Step 2: if $r=0$, report $n$ and stop. Step 3: replace $m$ by $n$ and $n$ by $r$ and go to Step 1. Trace it for $(m,n)=(1071,462)$ and $(252,198)$, writing every remainder, and report the outputs.", 5, r"(1071, 462): $r=147$; $(462,147)$: $r=21$; $(147,21)$: $r=0$ so output 21 (2). (252, 198): $r=54$; $(198,54)$: $r=36$; $(54,36)$: $r=18$; $(36,18)$: $r=0$ so output 18 (2). The algorithm is Euclid's division method (1).", "H"),
W(r"Estimate the number of reductions the subtraction method needs for $\gcd(1001,2)$ and compare with the division method. Why is the division method called faster?", 4, r"Subtraction: $1001\to999\to997\to\cdots\to3\to1$, about 500 reductions (1.5). Division: $1001=2\times500+1$, then $2=1\times2+0$: 2 divisions (1.5). One division removes all the repeated subtractions at once, so the work depends on the number of digits, not the value (1).", "H", wp=True),
W(r"The prime factorisations are stored as lists of (prime, power) pairs: $180=[(2,2),(3,2),(5,1)]$ and $150=[(2,1),(3,1),(5,2)]$. Find the gcd by taking each common prime to the smaller power, and verify it by Euclid's division method.", 4, r"Smaller powers: $2^1,3^1,5^1$ (1.5). gcd $=2\times3\times5=30$ (0.5). Division: $180=150\times1+30$, $150=30\times5+0$; the gcd is 30 ✓ (2).", "H"),
W(r"Describe an algorithm for 'the sum of all divisors of $n$' (use a list and a conditional step). Trace it for $n=28$ and say what you notice about the sum.", 4, r"Algorithm: sum $=0$; for each $j$ from 1 to $n$, if $j$ divides $n$ add $j$ to sum; report sum (2). For 28: $1+2+4+7+14+28=56$ (1). The sum is $2\times28$, so 28 is a 'perfect number' (the proper divisors add to 28) (1).", "H"),
W(r"Run the 'most-recent-common-divisor' algorithm for $m=36$, $n=48$ and list the values taken. How many values of $k$ does it check, and how many divisions does Euclid's division method need for the same pair?", 4, r"$k$ runs from 2 to 36 (35 values) (1). Common divisors found: $k=2,3,4,6,12$, so the values are $1\to2\to3\to4\to6\to12$ (1.5). gcd $=12$. Division: $48=36\times1+12$, $36=12\times3+0$: 2 divisions (1.5).", "H"),
W(r"**Case study.** A rectangular field 462 m long and 1,071 m wide is divided into equal square plots with no land left. (i) Find the side of the largest such plot. (ii) Find the number of plots. (iii) Show your gcd working in Euclid's division form.", 5, r"(i) Side $=\gcd(462,1071)$ (1). $1071=462\times2+147$, $462=147\times3+21$, $147=21\times7+0$ (2). Side 21 m (0.5). (ii) $\frac{462}{21}\times\frac{1071}{21}=22\times51=1122$ plots (1.5).", "H", wp=True),
W(r"Trace the column algorithm for $9999+1$ and for $999+999$. Show the carries. Why does the sum $9999+1$ have 5 digits, and what is the largest carry produced in either sum?", 4, r"$9999+1$: units $9+1=10$ (0, c1); tens $9+0+1=10$ (0, c1); hundreds (0, c1); thousands (0, c1); final carry 1 gives $10000$ (1.5). $999+999$: units 18 (8, c1); tens $9+9+1=19$ (9, c1); hundreds 19 (9, c1); final carry 1: $1998$ (1.5). The final carry adds a new digit; the largest carry is 1 (1).", "H"),
W(r"Today is Thursday. Find the day of the week (i) 365 days from now and (ii) 1000 days from now, by using remainders on division by 7. Explain how this is a 'mod' calculation.", 4, r"(i) $365=7\times52+1$, so $365 \bmod 7=1$: Friday (1.5). (ii) $1000=7\times142+6$, so $1000 \bmod 7=6$: six days after Thursday is Wednesday (1.5). The weekday repeats every 7 days, so only the remainder matters (1).", "H", wp=True),
W(r"Show that repeated subtraction of $n$ from $m$ ends with $m \bmod n$. For $\gcd(1000,6)$, how many subtractions of 6 does this take, and what are the next pairs after reaching the remainder?", 4, r"Subtracting $n$ as often as possible leaves a number less than $n$, which is the remainder (1). $1000=6\times166+4$: 166 subtractions, leaving 4 (1.5). Pairs: $(6,4)\to(4,2)\to(2,0)$, so $\gcd=2$ (1.5).", "H"),
W(r"Give two numbers that are not prime and have gcd 1 (co-prime), and verify using Euclid's division method. Then find $\gcd(101,100)$ and explain why $\gcd(k+1,k)=1$ for every $k$.", 3, r"8 and 15: $15=8\times1+7$, $8=7\times1+1$, $7=1\times7+0$, gcd 1 (1). $101=100\times1+1$, $100=1\times100+0$, gcd 1 (1). Any common divisor of $k+1$ and $k$ divides their difference 1 (1).", "H"),
W(r"A digit-sum algorithm is run on $n=52718$ ($d=n \bmod 10$, add $d$ to total, replace $n$ by $(n-d)/10$, repeat until $n=0$). Write the digits taken and the total. Use the total to decide whether 52718 is divisible by 3.", 4, r"Digits taken: $8,1,7,2,5$ (1.5). Total $=23$ (1). 23 is not a multiple of 3, so 52718 is not divisible by 3 (1). Check: $52718=3\times17572+2$ (0.5).", "H", wp=True),
W(r"Apply Euclid's division method to the consecutive Virahānka–Fibonacci numbers $\gcd(89,55)$ and count the divisions. What do you notice about the quotients?", 4, r"$89=55\times1+34$; $55=34\times1+21$; $34=21\times1+13$; $21=13\times1+8$; $13=8\times1+5$; $8=5\times1+3$; $5=3\times1+2$; $3=2\times1+1$; $2=1\times2+0$ (2.5). gcd $=1$ after 9 divisions (0.5). All quotients are 1 until the last; consecutive terms of this sequence need the most steps for their size (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(11)
def _lt(x):
    if isinstance(x, str): return x.replace(" < ", " &lt; ").replace(" > ", " &gt; ")
    if isinstance(x, (list, tuple)): return type(x)(_lt(i) for i in x)
    return x
_pre = _lt(_o["blocks"][:-2])
_extra = [
 ("h2", "Tracing Algorithms: Method and Examples"),
 ("p", "To **trace** (or execute) an algorithm, write a table with one column for every named value and one row for every pass through the repeated step. Update only what the step says, and record the new value of each name every time."),
 ("table", ["Pass", "n", "d = n mod 10", "total"], [["start", "52,718", "–", "0"], ["1", "5,271", "8", "8"], ["2", "527", "1", "9"], ["3", "52", "7", "16"], ["4", "5", "2", "18"], ["5", "0", "5", "23"]]),
 ("p", "The table traces the digit-sum algorithm (d = n mod 10; add d to total; replace n by (n − d)/10; stop when n = 0). It reports 23; since 23 is not a multiple of 3, 52,718 is not divisible by 3."),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Column addition with carries"),
 ("steps", [("Add 4,865 + 7,358", "Units: 5 + 8 = 13, write 3, carry 1. Tens: 6 + 5 + 1 = 12, write 2, carry 1."), ("Next columns", "Hundreds: 8 + 3 + 1 = 12, write 2, carry 1. Thousands: 4 + 7 + 1 = 12, write 2, carry 1."), ("Final carry", "Write the last 1 to the left: 12,223.")]),
 ("h3", "Example 2 — gcd by Euclid's division method"),
 ("steps", [("gcd(1071, 462)", "1071 = 462 × 2 + 147."), ("Next", "462 = 147 × 3 + 21, then 147 = 21 × 7 + 0."), ("Answer", "The last non-zero remainder is 21, so gcd = 21 (three divisions).")]),
 ("h3", "Example 3 — gcd by Euclid's subtraction method"),
 ("steps", [("gcd(48, 18)", "(48, 18) → (18, 30): m &lt; n, so reverse to (30, 18)."), ("Continue", "(30, 18) → (18, 12) → (12, 6) → (6, 6) → (6, 0)."), ("Answer", "gcd = 6. The subtraction step was used 5 times.")]),
 ("h3", "Example 4 — Cutting into equal pieces"),
 ("steps", [("Ropes of 375 cm and 825 cm, longest equal pieces", "Piece length = gcd(375, 825)."), ("Division", "825 = 375 × 2 + 75; 375 = 75 × 5 + 0, so 75 cm."), ("Number of pieces", "375 ÷ 75 + 825 ÷ 75 = 5 + 11 = 16.")]),
 ("h3", "Example 5 — Using remainders: days of the week"),
 ("steps", [("Today is Thursday; what day in 1,000 days?", "The week repeats every 7 days, so only 1,000 mod 7 matters."), ("Divide", "1,000 = 7 × 142 + 6, remainder 6."), ("Count on", "Six days after Thursday is Wednesday.")]),
 ("h3", "Example 6 — Checking the most-recent-common-divisor algorithm"),
 ("steps", [("m = 36, n = 48", "Start with value 1; test k = 2, 3, …, 36."), ("Updates", "k = 2, 3, 4, 6, 12 divide both, so the value goes 1 → 2 → 3 → 4 → 6 → 12."), ("Efficiency", "This checks 35 values; Euclid's division method needs only two divisions (48 = 36 × 1 + 12, 36 = 12 × 3 + 0).")]),
 ("h3", "Example 7 — Slowest case: consecutive Virahānka–Fibonacci numbers"),
 ("steps", [("gcd(89, 55)", "89 = 55 × 1 + 34, 55 = 34 × 1 + 21, 34 = 21 × 1 + 13, 21 = 13 × 1 + 8."), ("Continue", "13 = 8 × 1 + 5, 8 = 5 × 1 + 3, 5 = 3 × 1 + 2, 3 = 2 × 1 + 1, 2 = 1 × 2 + 0."), ("Observation", "gcd = 1 after 9 divisions, every quotient being 1 except the last: consecutive terms of this sequence need the most steps for their size.")]),
 ("h2", "Why the Algorithms Work: Justification"),
 ("p", "An algorithm is only useful if we can **prove it is correct** and **count its steps**. Here are the two main justifications of the chapter."),
 ("h3", "Column addition"),
 ("p", "Write each number by place value: 3,478 = 3 × 1,000 + 4 × 100 + 7 × 10 + 8. Adding two numbers means adding the units together, the tens together, and so on. If a column total is 10 or more, a group of ten units is exchanged for **one** ten of the next place; that is the carry. The carry is at most 1 because 9 + 9 + 1 = 19 = 10 + 9. Finally, a carry left after the leftmost column becomes a new leading digit (9,999 + 1 = 10,000)."),
 ("h3", "Euclid's division step: gcd(m, n) = gcd(n, m mod n)"),
 ("steps", [("Write the division", "m = q × n + r, where r = m mod n and 0 ≤ r &lt; n."), ("Common divisors are shared", "If d divides m and n, it divides r = m − qn. If d divides n and r, it divides m = qn + r."), ("So the gcds agree", "Pairs (m, n) and (n, r) have the same common divisors. The second pair has a smaller number, so we repeat until r = 0, when gcd(n, 0) = n.")]),
 ("note", "IMPORTANT", "The remainder strictly decreases at every division (r &lt; n), so the algorithm **must stop**. This is how we justify that a repeating algorithm does not run forever."),
 ("h2", "Designing and Checking an Algorithm"),
 ("ol", ["**State the problem** clearly: what is the input and what must be reported?", "**Name the values** you will keep track of (for example total, carry, most-recent-common-divisor).", "Choose **basic steps** you can already do (add digits, divide, compare).", "Decide the **repeated step** (for each j from 1 to n) and any **condition** (if j divides n).", "**Trace** it on a small input, writing a table of values for each pass.", "**Justify** that it gives the right answer and **count** how many passes it needs; look for a faster version."]),
 ("h3", "Example 8 — Designing: the sum of all divisors"),
 ("steps", [("Algorithm", "Set sum = 0. For each j from 1 to n: if j divides n, add j to sum. Report sum."), ("Trace for n = 28", "j = 1, 2, 4, 7, 14, 28 divide 28; sum = 1 + 2 + 4 + 7 + 14 + 28 = 56."), ("Observation", "56 = 2 × 28, so the divisors other than 28 add up to 28 itself; such a number is called a perfect number (the next one is 496).")]),
 ("h3", "Example 9 — Is it prime? Using divisors(n)"),
 ("steps", [("Is 91 prime?", "divisors(91) = [1, 7, 13, 91]: four entries, so 91 = 7 × 13 is not prime."), ("Is 97 prime?", "97 is not divisible by 2, 3, 5 or 7 (7 × 13 = 91 and 7 × 14 = 98). Any larger divisor would pair with a smaller one, so 97 has only the divisors 1 and 97: it is prime."), ("Rule", "n is prime exactly when the list divisors(n) has two entries.")]),
 ("h2", "Counting Steps: Comparing Algorithms"),
 ("table", ["Task", "Method", "Steps depend on", "Example"], [
  ["Adding", "counting dots", "the value", "3,347 + 2,729 = 6,076 dots, about 1 h 41 min at 1 s per dot"],
  ["Adding", "column algorithm", "number of digits", "4 columns × 15 s = 60 s"],
  ["gcd", "list divisors of both", "values m + n", "scans 1 to m and 1 to n"],
  ["gcd", "most-recent-common-divisor", "min(m, n)", "gcd(36, 48): checks k = 2 … 36"],
  ["gcd", "Euclid subtraction", "the value (can be large)", "gcd(1001, 2) needs about 500 reductions"],
  ["gcd", "Euclid division (Āryabhaṭa)", "number of digits", "gcd(1001, 2): 2 divisions"]]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Words", "Algorithmic idea", "Example"], [
  ["‘shared equally with none left over’", "divisors of the total", "24 chocolates: 1, 2, 3, 4, 6, 8, 12 or 24 children"],
  ["‘cut into equal pieces, longest possible, no waste’", "gcd of the lengths", "ropes 375 cm and 825 cm: 75 cm"],
  ["‘largest square tile / plot’", "gcd of length and breadth", "120 cm × 150 cm: 30 cm"],
  ["‘how many are left over’", "m mod n", "100 laddoos in boxes of 12: 100 mod 12 = 4"],
  ["‘after so many days / hours’", "reduce mod 7 or mod 12", "50 hours after 9 o'clock: 59 mod 12 = 11"],
  ["‘each shelf only one kind’", "gcd, then divide each total", "36 and 48 books: 12 per shelf, 3 + 4 = 7 shelves"],
  ["‘how many steps / how long’", "count passes of the repeated step", "subtraction 7 times, division 2 times"]]),
 ("note", "REMEMBER", "**Always state the answer in the units of the problem** (cm, plots, shelves). gcd(375, 825) = 75 is a length in cm for the ropes, but the number of pieces is 16."),
 ("h2", "Common Mistakes"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["Forgetting the final carry: 95 + 17 = 12", "a carry is left after the last column", "112"],
  ["gcd(m, n) = gcd(n, m + n)", "the rule subtracts (or takes the remainder)", "gcd(n, m − n) or gcd(n, m mod n)"],
  ["Stopping Euclid's division when the remainder is 1", "stop only when the remainder is 0", "the last non-zero remainder (or divisor) is the gcd"],
  ["Reporting 0 as the gcd of (m, 0)", "gcd(m, 0) = m", "report m"],
  ["Using the list [1, 2, 3, 6, 9, 18] and calling 9 the gcd with 24", "9 does not divide 24", "common divisors only: [1, 2, 3, 6], gcd = 6"],
  ["Counting steps by the digits for the subtraction method", "subtraction effort grows with the value", "gcd(2k + 1, 2) needs about k reductions"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**To trace an algorithm** keep a table of every named value and update it exactly as each step says.", "**m mod n** is the remainder on dividing m by n; it repeats in cycles, which is why it solves day-of-week and clock problems.", "Euclid's division method stops when the **remainder is 0**; the last non-zero divisor is the gcd.", "Word problems about equal pieces, tiles and shelves are **gcd problems**; ‘left over’ problems are **mod problems**."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
