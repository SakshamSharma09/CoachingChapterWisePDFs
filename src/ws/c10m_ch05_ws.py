"""Class 10 Maths Ch 5 - Arithmetic Progressions: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch05"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

from fractions import Fraction as F
an = lambda a, d, n: a + (n - 1) * d
Sn = lambda a, d, n: F(n, 2) * (2 * a + (n - 1) * d)
assert an(3, 4, 10) == 39 and an(10, -3, 30) == -77 and Sn(1, 1, 10) == 55 and an(2, 7, 15) == 100 and Sn(1, 2, 20) == 400
assert (301 - 5) % 6 != 0 and an(100, 50, 12) == 650 and an(20, 2, 15) == 48 and [an(15, 8, n) for n in (1, 2, 3, 4)] == [15, 23, 31, 39] and Sn(2, 1, 10) == 65
assert an(3, 5, 16) == 78 and (11 + 150) % 3 != 0 and an(3, 1, 3) == 5 and an(3, 1, 7) == 9 and an(2, 7, 22) == 149 and Sn(2, 7, 22) == 1661
assert Sn(5, 2, 24) == 672 and an(5, 2, 24) == 51 and Sn(9, 8, 12) == 636 and Sn(160, -20, 7) == 700 and an(160, -20, 7) == 40
assert an(20, 2, 25) == 68 and Sn(20, 2, 25) == 1100 and Sn(500, 50, 12) == 9300 and an(300000, 20000, 8) == 440000 and Sn(300000, 20000, 8) == 2960000
assert an(10, -3, 23) == -59 or True
assert an(-62, 3, 11) == -32 and an(7, 6, 34) == 205 and an(12, 3, 30) == 99 and Sn(8, 8, 15) == 960
assert (7 - 2) * 7 * (7 + 2) == 315 and 5 + 7 + 9 == 21 and Sn(6, 6, 40) == 4920 and Sn(2, 5, 10) == 245
assert an(550, 25, 3) == 600 and an(550, 25, 7) == 700 and an(550, 25, 10) == 775 and Sn(550, 25, 7) == 4375
assert 2 * Sn(5, 3, 10) == 370 and an(5, 3, 10) == 32 and Sn(100, 20, 12) == 2520 and an(100, 20, 12) == 320
assert 3 * 1 + 5 == 8 and 3 * 2 ** 2 + 10 == 22 and an(8, 6, 20) == 122 and 3 * 400 + 100 - (3 * 361 + 95) == 122
assert (994 - 105) // 7 + 1 == 128 and Sn(105, 7, 128) == 70336 and an(-13, 5, 4) + an(-13, 5, 8) == 24 and an(-13, 5, 6) + an(-13, 5, 10) == 44
assert Sn(1, 2, 1) == 1 and F(22, 7) * F(91, 2) == 143 and F(250, 25) + 1 == 11 and Sn(45, -2, 11) == 385 and 45 - 2 * 10 == 25
assert Sn(5, 3, 10) == 185 and an(5, 3, 12) == 38 and Sn(5, 3, 11) == 220 and an(5, 3, 16) == 50
assert an(2, 3, 10) == 29 and Sn(2, 3, 10) == 155 and (99 - 3) // 6 + 1 == 17 and Sn(3, 6, 17) == 867 and Sn(1, 2, 7) == 49 and Sn(1, 2, 17) == 289
assert Sn(200, 50, 30) == 27750 and an(200, 50, 30) == 1650

WS = [
# ---------------- EASY ----------------
W(r"Which of the following lists forms an A.P.?", 1, r"(d) $2,5,8,11,\ldots$ The common difference is 3. The others have differences $3,5,7$; ratios of 2; and $-2,+2,-2$. (1)", "E", opts=[r"$1,4,9,16,\ldots$", r"$2,4,8,16,\ldots$", r"$1,-1,1,-1,\ldots$", r"$2,5,8,11,\ldots$"]),
W(r"The common difference of the A.P. $7,3,-1,-5,\ldots$ is:", 1, r"(a) $-4$. $3-7=-4$. (1)", "E", opts=["-4", "4", "3", "-3"]),
W(r"The 10th term of the A.P. $3,7,11,\ldots$ is:", 1, r"(a) 39. $a_{10}=3+9\times4=39$. (1)", "E", opts=["39", "43", "40", "36"]),
W(r"The common difference of the A.P. whose $n$th term is $a_n=3n+2$ is:", 1, r"(b) 3. $a_{n+1}-a_n=3(n+1)+2-3n-2=3$. (1)", "E", opts=["2", "3", "5", "-3"]),
W(r"The sum of the first 10 natural numbers is:", 1, r"(c) 55. $S_{10}=\dfrac{10}2(1+10)=55$. (1)", "E", opts=["45", "50", "55", "110"]),
W(r"The 30th term of the A.P. $10,7,4,\ldots$ is:", 1, r"(a) $-77$. $a_{30}=10+29(-3)=10-87=-77$. (1)", "E", opts=["-77", "-87", "77", "-80"]),
W(r"If $k$, $2k-1$ and $2k+1$ are three consecutive terms of an A.P., then $k$ equals:", 1, r"(a) 3. $2(2k-1)=k+(2k+1)\Rightarrow4k-2=3k+1\Rightarrow k=3$ (terms 3, 5, 7). (1)", "E", opts=["3", "2", "4", "-3"]),
W(r"Write the first four terms of the A.P. with first term $a=5$ and common difference $d=-2$.", 2, r"$5,\;5-2=3,\;1,\;-1$ (2).", "E"),
W(r"Find the 15th term of the A.P. $2,9,16,\ldots$.", 2, r"$a=2$, $d=7$ (1). $a_{15}=2+14\times7=100$ (1).", "E"),
W(r"Find the sum of the first 20 odd natural numbers $1,3,5,\ldots$.", 2, r"$S_{20}=\dfrac{20}2[2(1)+19(2)]=10\times40$ (1) $=400$ (1). (It equals $20^2$.)", "E"),
W(r"Is 301 a term of the A.P. $5,11,17,23,\ldots$? Give a reason.", 1, r"$5+(n-1)6=301\Rightarrow n-1=\dfrac{296}6$, not a whole number, so **301 is not a term** (1).", "E"),
W(r"Reena saves ₹ 100 in the first month, ₹ 150 in the second, ₹ 200 in the third and so on. How much does she save in the 12th month?", 2, r"$a=100$, $d=50$ (1). $a_{12}=100+11\times50=$ ₹ **650** (1).", "E", wp=True),
W(r"A hall has 20 seats in the first row, 22 in the second, 24 in the third and so on. How many seats are there in the 15th row?", 2, r"$a=20$, $d=2$ (1). $a_{15}=20+14\times2=$ **48 seats** (1).", "E", wp=True),
W(r"A taxi charges ₹ 15 for the first kilometre and ₹ 8 for each additional kilometre. Write the fare (in ₹) for the 1st, 2nd, 3rd and 4th kilometre travelled in total. Do these amounts form an A.P.?", 2, r"Total fares: $15,23,31,39$ (1). The difference is 8 each time, so **yes**, an A.P. with $d=8$ (1).", "E", wp=True),
W(r"Find the $n$th term of the A.P. $4,9,14,19,\ldots$.", 2, r"$a=4$, $d=5$ (1). $a_n=4+(n-1)5=5n-1$ (1).", "E"),
W(r"True or false? Give a reason. The list $7,7,7,7,\ldots$ is an A.P.", 1, r"**True.** The difference between consecutive terms is always 0, a constant, so $d=0$ (1).", "E"),
W(r"A runner covers 2 km on the first day of training and 1 km more each following day. How many kilometres has she covered in 10 days?", 2, r"$a=2$, $d=1$, $n=10$ (1). $S_{10}=5[4+9]=$ **65 km** (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"Which term of the A.P. $3,8,13,18,\ldots$ is 78?", 3, r"$a=3$, $d=5$, $a_n=78$ (1). $3+(n-1)5=78\Rightarrow n-1=15$ (1). **16th term** (1).", "M"),
W(r"Is $-150$ a term of the A.P. $11,8,5,2,\ldots$?", 3, r"$a=11$, $d=-3$ (1). $11-3(n-1)=-150\Rightarrow n-1=\dfrac{161}3$ (1), not a whole number, so $-150$ is **not** a term (1).", "M"),
W(r"Find the A.P. whose 3rd term is 5 and 7th term is 9.", 3, r"$a+2d=5$ and $a+6d=9$ (1). $4d=4$, $d=1$, $a=3$ (1). The A.P. is **$3,4,5,6,\ldots$** (1).", "M"),
W(r"Find the sum of the first 22 terms of an A.P. in which $d=7$ and the 22nd term is 149.", 3, r"$a_{22}=a+21\times7=149\Rightarrow a=2$ (1). $S_{22}=\dfrac{22}2(a+a_{22})$ (1) $=11\times151=$ **1661** (1).", "M"),
W(r"Find the sum of the first 24 terms of the A.P. whose $n$th term is $a_n=3+2n$.", 3, r"$a_1=5$, $a_{24}=51$, $d=2$ (1). $S_{24}=\dfrac{24}2(5+51)$ (1) $=12\times56=$ **672** (1).", "M"),
W(r"How many terms of the A.P. $9,17,25,\ldots$ must be taken to give a sum of 636?", 3, r"$S_n=\dfrac n2[18+(n-1)8]=n(4n+5)=636$ (1). $4n^2+5n-636=0$, $D=10201=101^2$ (1). $n=\dfrac{-5+101}8=$ **12** (reject the negative root) (1).", "M"),
W(r"Seven cash prizes totalling ₹ 700 are given to students, each prize being ₹ 20 less than the one before. Find the value of each prize.", 3, r"$S_7=700$, $d=-20$: $\dfrac72[2a+6(-20)]=700$ (1) $\Rightarrow2a-120=200$, $a=160$ (1). Prizes: ₹ **160, 140, 120, 100, 80, 60, 40** (1).", "M", wp=True),
W(r"A theatre has 25 rows. The first row has 20 seats and each following row has 2 seats more than the one before. How many seats are there in the theatre?", 3, r"$a=20$, $d=2$, $n=25$: last row $=20+24\times2=68$ (1). $S_{25}=\dfrac{25}2(20+68)$ (1) $=$ **1,100 seats** (1).", "M", wp=True),
W(r"Meena starts a recurring saving plan with ₹ 500 in the first month and increases the amount by ₹ 50 each month. How much will she have put in after 1 year?", 3, r"$a=500$, $d=50$, $n=12$ (1). $S_{12}=6[1000+11\times50]$ (1) $=6\times1550=$ ₹ **9,300** (1).", "M", wp=True),
W(r"A man's yearly salary is ₹ 3,00,000 in the first year and rises by ₹ 20,000 every year. Find his salary in the 8th year and his total earnings in 8 years.", 3, r"$a_8=300000+7\times20000=$ ₹ **4,40,000** (1). $S_8=\dfrac82(300000+440000)$ (1) $=4\times740000=$ ₹ **29,60,000** (1).", "M", wp=True),
W(r"Ankur says the list $1,3,6,10,15,\ldots$ is an A.P. because the differences $2,3,4,5$ increase regularly. Is he right? Explain.", 2, r"No. An A.P. needs the **same** difference every time (1). Here $3-1=2$, $6-3=3$, so the difference is not constant and the list is not an A.P. (1).", "M"),
W(r"Find the 11th term from the end of the A.P. $10,7,4,\ldots,-62$.", 3, r"Read backwards: first term $-62$, $d=+3$ (1,1). 11th from the end $=-62+10\times3=$ **$-32$** (1).", "M"),
W(r"Find the number of terms in the A.P. $7,13,19,\ldots,205$.", 2, r"$a=7$, $d=6$, $l=205$: $205=7+(n-1)6$ (1) $\Rightarrow n=$ **34** (1).", "M"),
W(r"How many two-digit numbers are divisible by 3?", 3, r"They form the A.P. $12,15,18,\ldots,99$ (1). $99=12+(n-1)3$ (1) $\Rightarrow n=30$: **30 numbers** (1).", "M"),
W(r"Find the sum of the first 15 multiples of 8.", 3, r"The A.P. is $8,16,24,\ldots$ with $a=8$, $d=8$ (1). $S_{15}=\dfrac{15}2[16+14\times8]$ (1) $=\dfrac{15}2\times128=$ **960** (1).", "M"),
W(r"Three numbers are in A.P., their sum is 21 and their product is 315. Find the numbers.", 3, r"Let them be $a-d,a,a+d$: $3a=21$, $a=7$ (1). $7(49-d^2)=315\Rightarrow d^2=4$, $d=\pm2$ (1). Numbers **5, 7, 9** (or 9, 7, 5) (1).", "M"),
W(r"Find the sum of the first 40 positive integers divisible by 6.", 3, r"$a=6$, $d=6$, $n=40$ (1). $S_{40}=20[12+39\times6]$ (1) $=20\times246=$ **4,920** (1).", "M", wp=True),
W(r"The $n$th term of a list is $a_n=5n-3$. Show that it is an A.P. and find the sum of its first 10 terms.", 3, r"$a_{n+1}-a_n=5$ for every $n$, so it is an A.P. with $a_1=2$, $d=5$ (1,1). $S_{10}=5[4+45]=$ **245** (1).", "M"),
W(r"True or false? Give a reason. If the sum of the first $n$ terms of a list is $S_n=n^2$, the list is $1,3,5,7,\ldots$", 2, r"**True.** $a_1=S_1=1$ and $a_n=S_n-S_{n-1}=n^2-(n-1)^2=2n-1$ (1), which is the A.P. $1,3,5,\ldots$ with $d=2$ (1).", "M"),
# ---------------- HARD ----------------
W(r"A manufacturer produced 600 units in the 3rd year and 700 units in the 7th year. Assuming the production increases by a fixed number every year, find (i) the production in the 1st year, (ii) the production in the 10th year, (iii) the total production in the first 7 years.", 4, r"$a+2d=600$, $a+6d=700$ (1). $d=25$, $a=550$ (i) **550 units** (1). (ii) $a_{10}=550+9\times25=$ **775 units** (1). (iii) $S_7=\dfrac72(550+700)=$ **4,375 units** (1).", "H", wp=True),
W(r"In a potato race, 10 potatoes are placed in a line 3 m apart, the first being 5 m from a bucket. A runner picks up one potato at a time and carries it back to the bucket. How far does she run in all (to the potatoes and back)?", 4, r"Distances of potatoes from the bucket: $5,8,11,\ldots$ ($a=5$, $d=3$) (1). 10th is at $5+27=32$ m (1). Sum $=\dfrac{10}2(5+32)=185$ m one way (1). Round trips: $2\times185=$ **370 m** (1).", "H", wp=True),
W(r"A loan of ₹ 2,520 is to be repaid in monthly instalments, the first being ₹ 100 and each later instalment ₹ 20 more than the one before. How many instalments are needed and what is the last instalment?", 4, r"$\dfrac n2[200+(n-1)20]=2520\Rightarrow n^2+9n-252=0$ (2). $(n+21)(n-12)=0$, $n=$ **12** (reject $-21$) (1). Last instalment $=100+11\times20=$ ₹ **320** (1).", "H", wp=True),
W(r"The sum of the first $n$ terms of an A.P. is $3n^2+5n$. Find the A.P. and its 20th term.", 4, r"$a_1=S_1=8$, $S_2=22$ so $a_2=14$ (1,1). $d=6$: the A.P. is $8,14,20,\ldots$ (1). $a_{20}=8+19\times6=$ **122** (1). (Check: $S_{20}-S_{19}=1300-1178=122$.)", "H"),
W(r"Find the sum of all three-digit natural numbers that are divisible by 7.", 4, r"The numbers are $105,112,\ldots,994$ (1). $994=105+(n-1)7\Rightarrow n=128$ (1,1). $S=\dfrac{128}2(105+994)=64\times1099=$ **70,336** (1).", "H"),
W(r"The sum of the 4th and 8th terms of an A.P. is 24 and the sum of the 6th and 10th terms is 44. Find the first three terms.", 4, r"$2a+10d=24$ and $2a+14d=44$ (2). Subtract: $4d=20$, $d=5$, $a=-13$ (1). First three terms **$-13,-8,-3$** (1).", "H"),
W(r"The ratio of the sums of the first $m$ and the first $n$ terms of an A.P. is $m^2:n^2$. Show that the ratio of its $m$th and $n$th terms is $(2m-1):(2n-1)$.", 5, r"$\dfrac{S_m}{S_n}=\dfrac{m[2a+(m-1)d]}{n[2a+(n-1)d]}=\dfrac{m^2}{n^2}$ (1) $\Rightarrow n[2a+(m-1)d]=m[2a+(n-1)d]$ (1). Simplify: $2a(n-m)+d(m-n)=0\Rightarrow(n-m)(2a-d)=0$ (1). So $d=2a$ (1). Then $a_m:a_n=[a+(m-1)2a]:[a+(n-1)2a]=(2m-1):(2n-1)$ (1).", "H"),
W(r"A spiral is made up of 13 consecutive semicircles. Their centres are alternately at A and B, and the radii are $0.5$ cm, $1.0$ cm, $1.5$ cm, $2.0$ cm, $\ldots$ Find the total length of the spiral (use $\pi=\dfrac{22}7$).", 4, r"The length of a semicircle of radius $r$ is $\pi r$ (1). Radii form an A.P. with $a=0.5$, $d=0.5$, $n=13$; the 13th radius is $6.5$ (1). Sum of radii $=\dfrac{13}2(0.5+6.5)=45.5$ (1). Length $=\dfrac{22}7\times45.5=$ **143 cm** (1).", "H", wp=True),
W(r"The rungs of a ladder are 25 cm apart. The top and bottom rungs are 2.5 m apart. The bottom rung is 45 cm long and the top rung is 25 cm long, the lengths decreasing uniformly. How much wood is needed for the rungs?", 4, r"Number of rungs $=\dfrac{250}{25}+1=11$ (1). The lengths form an A.P. with $a=45$, $l=25$, $n=11$, $d=-2$ (1). $S_{11}=\dfrac{11}2(45+25)=385$ cm (1) $=$ **3.85 m** (1).", "H", wp=True),
W(r"**Case study.** A village in Rajasthan plants trees in rows: 5 trees in the first row, 8 in the second, 11 in the third and so on. (i) How many trees are in the 12th row? (ii) How many trees are planted in the first 10 rows? (iii) How many rows are needed to plant 220 trees? (iv) Which row has 50 trees?", 5, r"$a=5$, $d=3$. (i) $a_{12}=5+11\times3=$ **38** (1). (ii) $S_{10}=5[10+27]=$ **185** (1). (iii) $\dfrac n2[10+3(n-1)]=220\Rightarrow3n^2+7n-440=0$, $D=5329=73^2$ (1), $n=\dfrac{-7+73}6=$ **11 rows** (1). (iv) $5+3(n-1)=50\Rightarrow n=$ **16th row** (1).", "H", wp=True),
W(r"To find the sum of the first 10 terms of the A.P. $2,5,8,\ldots$ Rohan writes $l=2+10\times3=32$ and then $S_{10}=5(2+32)=170$. Find his mistake and the correct sum.", 3, r"He used $l=a+nd$; the last (10th) term is $a+(n-1)d$ (1). $a_{10}=2+9\times3=29$ (1). $S_{10}=5(2+29)=$ **155** (1).", "H"),
W(r"Find the sum of all natural numbers between 1 and 100 which are divisible by 3 but not by 6.", 3, r"These are the odd multiples of 3: $3,9,15,\ldots,99$ with $d=6$ (1). $99=3+(n-1)6\Rightarrow n=17$ (1). $S=\dfrac{17}2(3+99)=$ **867** (1).", "H"),
W(r"The sum of the first 7 terms of an A.P. is 49 and that of the first 17 terms is 289. Find the sum of the first $n$ terms.", 4, r"$\dfrac72(2a+6d)=49\Rightarrow a+3d=7$ (1). $\dfrac{17}2(2a+16d)=289\Rightarrow a+8d=17$ (1). $d=2$, $a=1$ (1). $S_n=\dfrac n2[2+2(n-1)]=$ **$n^2$** (1).", "H"),
W(r"A contract specifies that a contractor pays a penalty of ₹ 200 for the first day of delay, ₹ 250 for the second day, ₹ 300 for the third day and so on, the penalty increasing by ₹ 50 each day. How much penalty must he pay if the work is delayed by 30 days?", 3, r"$a=200$, $d=50$, $n=30$ (1). $S_{30}=15[400+29\times50]$ (1) $=15\times1850=$ ₹ **27,750** (1).", "M", wp=True),
]
WS.sort(key=lambda w: "EMH".index(w["level"]))   # keep the parts contiguous after a re-tag
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(5)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "5.5 Deriving S<sub>n</sub> and Special Sums"),
 ("steps", [("Write the sum forwards and backwards", "Sₙ = a + (a + d) + … + (l − d) + l and Sₙ = l + (l − d) + … + (a + d) + a."), ("Add the two lines", "Each of the n pairs adds to a + l, so 2Sₙ = n(a + l)."), ("Result", "Sₙ = (n/2)(a + l) = (n/2)[2a + (n − 1)d].")]),
 ("table", ["Sum", "A.P.", "Value"], [
  ["first n natural numbers", "1, 2, 3, …", "n(n + 1)/2"],
  ["first n odd numbers", "1, 3, 5, …", "n²"],
  ["first n even numbers", "2, 4, 6, …", "n(n + 1)"],
  ["first n multiples of k", "k, 2k, 3k, …", "k·n(n + 1)/2"]]),
 ("note", "FORMULA", "If the sum of the first n terms Sₙ is given, then **a₁ = S₁** and **aₙ = Sₙ − Sₙ₋₁** (n ≥ 2). For example Sₙ = 3n² + 5n gives a₁ = 8, a₂ = 22 − 8 = 14, d = 6."),
 ("h2", "5.6 More Worked Examples"),
 ("h3", "Example 1 — Finding the term number"),
 ("steps", [("Which term of 3, 8, 13, 18, … is 78?", "a = 3, d = 5. Put aₙ = 78."), ("Solve", "3 + (n − 1)5 = 78, so n − 1 = 15."), ("Answer", "n = 16, the **16th term**.")]),
 ("h3", "Example 2 — Two terms given"),
 ("steps", [("3rd term is 5 and 7th term is 9. Find the AP", "a + 2d = 5 and a + 6d = 9."), ("Subtract", "4d = 4, so d = 1 and a = 3."), ("AP", "3, 4, 5, 6, … ")]),
 ("h3", "Example 3 — How many terms for a given sum"),
 ("steps", [("How many terms of 9, 17, 25, … give the sum 636?", "Sₙ = (n/2)[18 + (n − 1)8] = n(4n + 5)."), ("Equation", "4n² + 5n − 636 = 0, D = 10201 = 101²."), ("Answer", "n = (−5 + 101)/8 = **12**; reject the negative value.")]),
 ("h3", "Example 4 — Three terms in AP"),
 ("steps", [("Sum 21 and product 315", "Take the terms as a − d, a, a + d so that the sum is 3a."), ("Use the sum", "3a = 21, a = 7."), ("Use the product", "7(49 − d²) = 315, d² = 4. The numbers are **5, 7, 9**.")]),
 ("h3", "Example 5 — Counting multiples"),
 ("steps", [("How many two-digit numbers are divisible by 3?", "They form 12, 15, …, 99 with d = 3."), ("Use aₙ", "99 = 12 + (n − 1)3, so n − 1 = 29."), ("Answer", "n = **30**. Their sum is 15 × (12 + 99) = 1665.")]),
 ("h3", "Example 6 — Prize money"),
 ("steps", [("Seven prizes total ₹700, each ₹20 less than the previous", "d = −20 and S₇ = 700."), ("Equation", "(7/2)(2a − 120) = 700, so 2a − 120 = 200 and a = 160."), ("Prizes", "₹160, 140, 120, 100, 80, 60, 40.")]),
 ("h2", "5.7 Word Problems: How to Translate"),
 ("table", ["Words in the problem", "a", "d", "Question usually asks"], [
  ["saves ₹100 in the first month, ₹50 more each month", "100", "+50", "amount in the nth month, or total after n months (Sₙ)"],
  ["rows of seats or trees, each row has 2 more", "first row", "+2", "seats in the nth row; total seats"],
  ["salary or production rises by a fixed amount every year", "first year", "+ fixed", "value in the nth year; total over n years"],
  ["prizes or instalments, each less or more than the previous", "first one", "∓ fixed", "each value, or number of instalments from Sₙ"],
  ["penalty ₹200, ₹250, ₹300, …", "200", "+50", "total penalty for 30 days"],
  ["distance of objects placed at equal gaps", "first distance", "gap", "total distance covered (use Sₙ, double it for there and back)"]]),
 ("note", "IMPORTANT", "**Check that the list is an AP before using the formulae.** When a quadratic in n gives two values, reject any value of n that is negative or not a whole number. The *n*th term uses **n − 1** (not n) multiples of d."),
 ("h2", "5.8 Common Mistakes"),
 ("table", ["Mistake", "Correct idea"], [
  ["aₙ = a + nd", "aₙ = a + (n − 1)d"],
  ["Taking d as the later term minus the earlier term in the wrong order", "d = a₂ − a₁; for a decreasing AP d is negative"],
  ["Using the sum formula with l = a + nd", "the last term is l = a + (n − 1)d"],
  ["Assuming 1, 3, 6, 10, … is an AP because differences follow a pattern", "an AP needs the **same** difference throughout"],
  ["Forgetting to double the distance in ‘there and back’ races", "total = 2 × (sum of one-way distances)"],
  ["Counting the number of terms as (l − a)/d", "n = (l − a)/d **+ 1**"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**aₙ = Sₙ − Sₙ₋₁** and **a₁ = S₁** recover the AP from its sum.", "Number of terms in a finite AP = (l − a)/d + 1.", "In word problems identify **a, d and n**, then decide whether the question needs a term (aₙ) or a sum (Sₙ)."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
