"""Class 9 Maths Ch 8 - Sequences and Progressions: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch08"

def _old(n):
    d = "c9_maths1" if n < 9 else "c9_maths2"
    p = Path(__file__).resolve().parents[1] / "rn_work" / d / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric checks
def ap(a, d, n): return a + (n - 1) * d
def aps(a, d, n): return n * (2 * a + (n - 1) * d) // 2
assert 4*6-3 == 21 and ap(2, 3, 20) == 59 and ap(50, 10, 8) == 120 and ap(20, 2, 10) == 38 and ap(30, 12, 10) == 138
assert 5*2**6 == 320 and ap(7, 6, 25) == 151 and aps(3, 4, 20) == 820 and aps(14, 2, 18) == 558
assert ap(20000, 1500, 9) == 32000 and aps(20000, 1500, 9) == 234000 and aps(5, 5, 30) == 2325 and ap(5, 5, 30) == 150
assert ap(5, 4, 25) == 101 and aps(5, 4, 25) == 1325 and 2*3**7 == 4374 and 3*3**5 == 729 and 3*3**6 == 2187 and 3*3**7 == 6561
assert ap(4, 5, 20) == 99 and ap(4, 5, 21) == 104 and ap(3, 2, 15) == 31 and 2*25+1 == 51 and aps(500, 50, 12) == 9300 and ap(500, 50, 12) == 1050
assert ap(2, 4, 4) == 14 and ap(2, 4, 9) == 34 and ap(2, 4, 20) == 78 and aps(2, 4, 20) == 800
assert 12*(8*12+10)//2 == 636 and aps(9, 8, 12) == 636
assert 8*(64-9) == 440 and 5*8*11 == 440 and aps(24000, 1000, 24) == 852000 and aps(20000, 1500, 24) == 894000
assert 20000+1500*8 == 24000+1000*8 == 32000 and 20000+1500*9 > 24000+1000*9
assert ap(50, -2, 20) == 12 and aps(50, -2, 20) == 620
assert all(sum(ap(40, -2, i) for i in range(1, n+1)) == (400 if n in (16, 25) else None) or True for n in (16,))
assert aps(40, -2, 16) == 400 and aps(40, -2, 25) == 400 and ap(40, -2, 25) == -8 and ap(40, -2, 16) == 10
assert 3*2**2 == 12 and 3*2**5 == 96 and 3*2**7 == 384
assert 81*(2/3)**4 == 16 or abs(81*(2/3)**4 - 16) < 1e-9
assert 81*(2/3)**6 > 5 > 81*(2/3)**7
a, b = 1, 2; v = [a, b]
for _ in range(6): v.append(v[-1] + v[-2])
assert v[7] == 34 and v[6] == 21 and v[5] == 13
u = [1]
for _ in range(5): u.append(2*u[-1] + 1)
assert u == [1, 3, 7, 15, 31, 63]
assert sum(range(105, 400, 7)) == 10836 and len(range(105, 400, 7)) == 43
assert (3/4)**2 > .5 > (3/4)**3 and 2**9 == 512 and 2**10 > 1000 > 2**9
t = [2]
for _ in range(4): t.append(3*t[-1] - 1)
assert t == [2, 5, 14, 41, 122]
w = [1, 2]
for _ in range(5): w.append(w[-1] + w[-2])
assert w == [1, 2, 3, 5, 8, 13, 21]

WS = [
# ---------------- EASY ----------------
W(r"For the sequence $t_n=4n-3$, the value of $t_6$ is:", 1, r"(a) 21. $t_6=4\times6-3=21$. (1)", "E", opts=["21", "24", "27", "19"]),
W(r"The common difference of the AP $17, 13, 9, 5,\ldots$ is:", 1, r"(c) $-4$. Each term is 4 less than the one before: $13-17=-4$. (1)", "E", opts=["4", "$-3$", "$-4$", "$-5$"]),
W(r"The next term of the GP $5, 10, 20, 40,\ldots$ is:", 1, r"(b) 80. The common ratio is 2, so the next term is $40\times2=80$. (1)", "E", opts=["60", "80", "70", "160"]),
W(r"The sum of the first 20 natural numbers is:", 1, r"(d) 210. $S=\frac{20\times21}{2}=210$. (1)", "E", opts=["200", "190", "420", "210"]),
W(r"Which of the following sequences is a GP?", 1, r"(c) $3, 6, 12, 24,\ldots$ has the constant ratio 2. (1)", "E", opts=[r"$2, 4, 6, 8,\ldots$", r"$1, 4, 9, 16,\ldots$", r"$3, 6, 12, 24,\ldots$", r"$10, 7, 4, 1,\ldots$"]),
W(r"In the Virahānka sequence $1, 2, 3, 5, 8, 13,\ldots$ (each term is the sum of the two before it), the next term is:".replace(r"ā", "ā"), 1, r"(a) 21, since $8+13=21$. (1)", "E", opts=["21", "20", "26", "18"]),
W(r"A sequence has $t_1=5$ and $t_{n+1}=t_n+4$. Write its first five terms and an explicit rule for $t_n$.", 2, r"Terms: $5, 9, 13, 17, 21$ (1). Constant difference 4 gives $t_n=5+(n-1)4=4n+1$ (1).", "E"),
W(r"Ravi saves ₹ 50 in the first week and ₹ 10 more every week than in the week before. How much does he save in the 8th week?", 2, r"Savings form an AP with $a=50$, $d=10$ (1). $t_8=50+7\times10=$ ₹ 120 (1).", "E", wp=True),
W(r"The first row of a school hall has 20 seats and every next row has 2 seats more. How many seats are there in the 10th row?", 2, r"AP with $a=20$, $d=2$ (1). $t_{10}=20+9\times2=38$ seats (1).", "E", wp=True),
W(r"A culture has 5 bacteria and the number doubles every hour. How many bacteria are there after 6 hours?", 2, r"GP with first term 5 and ratio 2; after 6 hours it is the 7th term (1). $5\times2^6=320$ (1).", "E", wp=True),
W(r"A taxi charges ₹ 30 for the first kilometre and ₹ 12 for each additional kilometre. Find the fare for a 10 km journey.", 2, r"Fares for 1 km, 2 km, 3 km,... form an AP with $a=30$, $d=12$ (1). Fare for 10 km $=30+9\times12=$ ₹ 138 (1).", "E", wp=True),
W(r"Show that $2, 5, 8, 11,\ldots$ is an AP and find its 20th term.", 2, r"Differences $5-2=8-5=11-8=3$, constant, so it is an AP with $a=2$, $d=3$ (1). $t_{20}=2+19\times3=59$ (1).", "E"),
W(r"Logs are stacked with 1 log in the top row, 2 in the next row, 3 in the next, and so on, up to 15 rows. How many logs are there in all?", 2, r"Total $=1+2+\cdots+15=\frac{15\times16}{2}$ (1) $=120$ logs (1).", "E", wp=True),
W(r"True or false (give a reason): the sequence $1, 4, 9, 16,\ldots$ is an AP.", 2, r"**False.** The differences are $3, 5, 7,\ldots$, which are not equal, so there is no common difference (2).", "E"),
W(r"Write an explicit rule for the sequence $4, 7, 10, 13,\ldots$ and use it to find $t_{20}$.", 2, r"Common difference 3, first term 4: $t_n=3n+1$ (1). $t_{20}=3\times20+1=61$ (1).", "E"),
W(r"In the Sierpiński triangle, the number of black triangles at Stage $n$ is $3^n$. Find the number of black triangles at Stage 3 and at Stage 6.".replace(r"ń", "ń"), 2, r"Stage 3: $3^3=27$ (1). Stage 6: $3^6=729$ (1).", "E", wp=True),
W(r"Rohit says that $2, 4, 8, 16,\ldots$ is an AP with common difference 2. Is he right? Explain.", 2, r"No. The differences are $2, 4, 8,\ldots$, not equal (1). The ratios $4/2=8/4=16/8=2$ are equal, so it is a GP with ratio 2 (1).", "E"),
# ---------------- MEDIUM ----------------
W(r"Which term of the AP $7, 13, 19,\ldots$ is 151?", 2, r"$a=7$, $d=6$: $7+(n-1)6=151$ (1). $(n-1)=24$, so $n=25$: it is the 25th term (1).", "M"),
W(r"Find the sum of the first 20 terms of the AP $3, 7, 11,\ldots$.", 2, r"$a=3$, $d=4$. $S_{20}=\frac{20}{2}[2\times3+19\times4]$ (1) $=10\times82=820$ (1).", "M"),
W(r"An auditorium has 18 rows. The first row has 14 seats and each next row has 2 more seats than the one before. Find the seats in the last row and the total number of seats.", 3, r"AP with $a=14$, $d=2$, $n=18$. Last row $=14+17\times2=48$ (1). Total $=\frac{18}{2}(14+48)$ (1) $=9\times62=558$ seats (1).", "M", wp=True),
W(r"Sahil's salary is ₹ 20,000 in the first year and rises by ₹ 1,500 every year. Find his salary in the 9th year and his total earnings in 9 years.", 3, r"AP: $a=20000$, $d=1500$. $t_9=20000+8\times1500=$ ₹ 32,000 (1). $S_9=\frac92(20000+32000)$ (1) $=9\times26000=$ ₹ 2,34,000 (1).", "M", wp=True),
W(r"Meena saves ₹ 5 on day 1, ₹ 10 on day 2, ₹ 15 on day 3, and so on. How much does she save on day 30 and in all in 30 days?", 3, r"AP: $a=5$, $d=5$. Day 30: $5+29\times5=$ ₹ 150 (1). Total $=\frac{30}{2}(5+150)$ (1) $=15\times155=$ ₹ 2,325 (1).", "M", wp=True),
W(r"Find the number of terms in the AP $5, 9, 13,\ldots, 101$ and their sum.", 3, r"$a=5$, $d=4$: $5+(n-1)4=101$ gives $n=25$ (1). $S=\frac{25}{2}(5+101)$ (1) $=25\times53=1325$ (1).", "M"),
W(r"Show that $2, 6, 18, 54,\ldots$ is a GP, write its $n$th term and find the 8th term.", 2, r"Ratios $6/2=18/6=54/18=3$, so it is a GP with $a=2$, $r=3$; $t_n=2\times3^{n-1}$ (1). $t_8=2\times3^7=4374$ (1).", "M"),
W(r"A colony has 3 bacteria initially and the number triples every hour. How many are there after 5 hours? After how many whole hours does the colony first exceed 5000?", 3, r"After $h$ hours the number is $3\times3^h$ (1). After 5 hours: $3\times243=729$ (1). After 6 hours $2187$ (not above 5000); after 7 hours $6561>5000$, so 7 hours (1).", "M", wp=True),
W(r"A ball dropped from a height of 64 m rises, after every bounce, to half of the height it fell from. Show that the rebound heights form a GP and find the height after the 5th bounce.", 3, r"Rebounds $32, 16, 8,\ldots$ with constant ratio $\frac12$, so a GP (1). The $n$th rebound is $64\times(\frac12)^n$ (1). 5th: $64/32=2$ m (1).", "M", wp=True),
W(r"A sheet of paper 0.1 mm thick is folded in half again and again, doubling the thickness at each fold. Find the thickness after 10 folds.", 2, r"After $k$ folds thickness $=0.1\times2^k$ mm (1). For $k=10$: $0.1\times1024=102.4$ mm (about 10 cm) (1).", "M", wp=True),
W(r"A sequence is defined by $u_1=2$ and $u_n=3u_{n-1}-1$. Write the first five terms. Is 41 a term? Is 100 a term?", 3, r"$2,\ 5,\ 14,\ 41,\ 122$ (2). 41 is the 4th term, so yes; terms increase from 41 to 122, so 100 is not a term (1).", "M"),
W(r"Priya says the explicit rule for $2, 5, 8, 11,\ldots$ is $t_n=3n+2$. Find her mistake and give the correct rule.", 2, r"Check: $t_1=3+2=5\neq2$, so the rule fails (1). The AP has $a=2$, $d=3$: $t_n=2+3(n-1)=3n-1$ ($t_1=2$, $t_2=5$ ✓) (1).", "M"),
W(r"In a quiz, a team's points in successive rounds are $4, 9, 14,\ldots$. In which round does the team's score in that round first exceed 100? Does the score exactly 100 ever occur?", 3, r"$t_n=4+5(n-1)=5n-1$ (1). $5n-1>100$ gives $n>20.2$; $t_{20}=99$ and $t_{21}=104$, so the 21st round (1). $5n-1=100$ gives $n=20.2$, not a whole number, so 100 never occurs (1).", "M", wp=True),
W(r"Verify that the sum of the first 6 odd numbers equals $6^2$. Use the rule 'sum of the first $n$ odd numbers $=n^2$' to find $1+3+5+\cdots+49$.", 3, r"$1+3+5+7+9+11=36=6^2$ (1). The odd numbers up to 49 are the first 25 odd numbers ($2n-1=49$, $n=25$) (1). Sum $=25^2=625$ (1).", "M"),
W(r"A staircase has $n$ steps and you climb 1 or 2 steps at a time. Let $V_n$ be the number of ways: $V_1=1$, $V_2=2$, $V_3=3$, and $V_n=V_{n-1}+V_{n-2}$. Find the number of ways to climb 7 steps.", 3, r"$V_4=3+2=5$ (1), $V_5=8$, $V_6=13$ (1), $V_7=13+8=21$ ways (1).", "M", wp=True),
W(r"In the Sierpiński triangle the black area at Stage $n$ is $(\frac34)^n$ of the original. If the original triangle has area 256 cm², find the black area at Stage 4 and the number of black triangles then.".replace(r"ń", "ń"), 3, r"Black area $=256\times\frac{81}{256}$ (1) $=81$ cm² (1). Number of black triangles $=3^4=81$ (1).", "M", wp=True),
W(r"The differences of consecutive square numbers $1, 4, 9, 16, 25,\ldots$ are $3, 5, 7, 9,\ldots$. Use this pattern to write $t_{12}-t_{11}$ and then find $12^2$ from $11^2=121$.", 2, r"The difference between $n^2$ and $(n-1)^2$ is $2n-1$; for $n=12$ it is 23 (1). $12^2=121+23=144$ (1).", "M"),
W(r"Matchsticks are used to make a row of triangles: 1 triangle needs 3 sticks, 2 triangles need 5 sticks, 3 triangles need 7 sticks, and so on. Find the number of sticks for 15 triangles and the number of triangles that can be made with 51 sticks.", 3, r"AP: $a=3$, $d=2$, $t_n=2n+1$ (1). For 15 triangles: $31$ sticks (1). $2n+1=51$ gives $n=25$ triangles (1).", "M", wp=True),
W(r"Ritu repays a loan in 12 monthly instalments: ₹ 500 in the first month, and each instalment is ₹ 50 more than the one before. Find the last instalment and the total repaid.", 3, r"AP: $a=500$, $d=50$. Last $=500+11\times50=$ ₹ 1,050 (1). Total $=\frac{12}{2}(500+1050)$ (1) $=6\times1550=$ ₹ 9,300 (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"The 4th term of an AP is 14 and its 9th term is 34. Find the first term, the common difference, the 20th term and the sum of the first 20 terms.", 4, r"$a+3d=14$ and $a+8d=34$ (1). Subtract: $5d=20$, $d=4$, $a=2$ (1). $t_{20}=2+19\times4=78$ (1). $S_{20}=10(2+78)=800$ (1).", "H"),
W(r"Three numbers in AP have sum 24 and product 440. Find them.", 4, r"Take $a-d,\ a,\ a+d$. Sum $=3a=24$, $a=8$ (1). Product $=8(64-d^2)=440$ (1), so $d^2=9$, $d=\pm3$ (1). The numbers are $5, 8, 11$ (1).", "H"),
W(r"How many terms of the AP $9, 17, 25,\ldots$ must be taken so that the sum is 636?", 4, r"$a=9$, $d=8$. $S_n=\frac n2[18+8(n-1)]=n(4n+5)$ (1). $4n^2+5n-636=0$ (1). $(n-12)(4n+53)=0$ (1). $n=12$; the negative root is rejected (1).", "H"),
W(r"Two companies offer a job. Company A: ₹ 24,000 in the first month with a rise of ₹ 1,000 every month. Company B: ₹ 20,000 in the first month with a rise of ₹ 1,500 every month. (i) Find the total pay from each in 24 months. (ii) From which month is B's monthly pay higher than A's?", 5, r"(i) A: $S_{24}=12[48000+23\times1000]=12\times71000=$ ₹ 8,52,000 (1.5). B: $S_{24}=12[40000+23\times1500]=12\times74500=$ ₹ 8,94,000 (1.5). (ii) Monthly pay: A $=24000+1000(n-1)$, B $=20000+1500(n-1)$. Equal when $500(n-1)=4000$, $n=9$ (both ₹ 32,000) (1). So B pays more from the 10th month (1).", "H", wp=True),
W(r"A pile of 400 pipes is stacked in rows. The bottom row has 40 pipes and each row above has 2 pipes fewer than the row below. How many rows are there? Why are there two mathematical answers and which one is acceptable?", 4, r"$a=40$, $d=-2$: $S_n=\frac n2[80-2(n-1)]=n(41-n)=400$ (1). $n^2-41n+400=0$, $(n-16)(n-25)=0$ (1). $n=25$ gives a top row of $40-48=-8$ pipes, impossible (1). So $n=16$ rows, top row $40-30=10$ pipes (1).", "H", wp=True),
W(r"The 3rd term of a GP is 12 and the 6th term is 96. Find the first term, the common ratio and the 8th term.", 4, r"$ar^2=12$, $ar^5=96$ (1). Dividing: $r^3=8$, $r=2$ (1). $a=12/4=3$ (1). $t_8=3\times2^7=384$ (1).", "H"),
W(r"A ball is dropped from 81 m. After every bounce it rises to $\frac23$ of the height it fell from. Find the height after the 4th bounce and the first bounce after which the height is below 5 m.", 4, r"Rebounds form a GP with first term 54 and ratio $\frac23$; $n$th rebound $=81(\frac23)^n$ (1). 4th: $81\times\frac{16}{81}=16$ m (1). 6th: $81\times\frac{64}{729}\approx7.1$ m; 7th: $81\times\frac{128}{2187}\approx4.7$ m $<5$ (1). So after the 7th bounce (1).", "H", wp=True),
W(r"Show that $t_n=5n+2$ gives an AP and find $d$. Show that $t_n=n^2+1$ does not give an AP.", 3, r"$t_{n+1}-t_n=5(n+1)+2-5n-2=5$, constant, so an AP with $d=5$ (1.5). For $n^2+1$: $2, 5, 10,\ldots$; $5-2=3\neq10-5=5$, so not an AP (1.5).", "H"),
W(r"**Case study (Virahānka rhythms).** A rhythm of $n$ beats is built from short syllables (1 beat) and long syllables (2 beats). Let $V_n$ be the number of different rhythms: $V_1=1$ (S), $V_2=2$ (SS, L), $V_3=3$ (SSS, SL, LS). (i) List all rhythms of 4 beats. (ii) Explain why $V_n=V_{n-1}+V_{n-2}$. (iii) Find $V_8$.".replace(r"ā", "ā"), 5, r"(i) SSSS, SSL, SLS, LSS, LL: $V_4=5$ (1.5). (ii) A rhythm of $n$ beats ends either in S (before it a rhythm of $n-1$ beats) or in L (before it a rhythm of $n-2$ beats), so $V_n=V_{n-1}+V_{n-2}$ (2). (iii) $V_5=8$, $V_6=13$, $V_7=21$, $V_8=34$ (1.5).", "H", wp=True),
W(r"A sequence has $a_1=1$ and $a_n=2a_{n-1}+1$. Write the first five terms, guess an explicit rule, and check it for $a_6$.", 3, r"$1, 3, 7, 15, 31$ (1). Each term is one less than a power of 2: $a_n=2^n-1$ (1). $a_6=2\times31+1=63=2^6-1$ ✓ (1).", "H"),
W(r"Find the sum of all multiples of 7 lying between 100 and 400.", 4, r"The multiples are $105, 112,\ldots, 399$: $a=105$, $d=7$ (1). $105+7(n-1)=399$ gives $n=43$ (1). $S=\frac{43}{2}(105+399)$ (1) $=43\times252=10836$ (1).", "H"),
W(r"At which stage of the Sierpiński triangle does the black area first fall below half the original area? Give the number of black triangles at that stage.".replace(r"ń", "ń"), 4, r"Black area at Stage $n$ is $(\frac34)^n$ (1). Stage 2: $\frac9{16}=0.5625>0.5$ (1). Stage 3: $\frac{27}{64}\approx0.42<0.5$ (1). So Stage 3, with $3^3=27$ black triangles (1).", "H"),
W(r"Prove that if a sequence of non-zero numbers is both an AP and a GP, then all its terms are equal. (Use three consecutive terms $a, a+d, a+2d$.)", 4, r"For a GP, $\frac{a+d}{a}=\frac{a+2d}{a+d}$ (1). Cross-multiplying: $(a+d)^2=a(a+2d)$ (1). $a^2+2ad+d^2=a^2+2ad$, so $d^2=0$ and $d=0$ (1). Hence all terms equal $a$ (1).", "H"),
W(r"A sage asks for 1 grain of rice on the first square of a chessboard, 2 on the second, 4 on the third, doubling each time. How many grains are on the 10th square? On which square does the number first exceed 1000? Is the sequence an AP or a GP, and why?", 3, r"GP with $a=1$, $r=2$; the number doubles each time, so constant ratio (1). 10th square: $2^9=512$ (1). $2^{10}=1024>1000$, so the 11th square (1).", "H", wp=True),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(8)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "8.5 Proofs and Derivations"),
 ("h3", "Why the nth term of an AP is a + (n − 1)d"),
 ("p", "The first term is a. To reach the second term we add d once, to reach the third we add d twice, and so on. To reach the nth term we have added d exactly (n − 1) times. Hence tₙ = a + (n − 1)d. For example the 12th term of 7, 10, 13, … is 7 + 11 × 3 = 40."),
 ("h3", "Why Sₙ = (n/2)[2a + (n − 1)d] (Gauss's pairing)"),
 ("steps", [("Write the sum forwards and backwards", "S = a + (a + d) + … + (l − d) + l and S = l + (l − d) + … + (a + d) + a, where l = a + (n − 1)d is the last term."), ("Add the two lines term by term", "Every pair adds to (a + l), and there are n pairs, so 2S = n(a + l)."), ("Divide by 2", "S = (n/2)(a + l) = (n/2)[2a + (n − 1)d]. For 1 + 2 + … + 100: 50 × 101 = 5,050.")]),
 ("note", "FORMULA", "Use **Sₙ = (n/2)(a + l)** when the last term l is known, and **Sₙ = (n/2)[2a + (n − 1)d]** when d and n are known. Sum of the first n natural numbers = n(n + 1)/2; sum of the first n odd numbers = n²."),
 ("h3", "Why the sum of the first n odd numbers is n²"),
 ("p", "The odd numbers 1, 3, 5, …, (2n − 1) form an AP with a = 1, d = 2. So S = (n/2)[2 + 2(n − 1)] = (n/2)(2n) = n². Picture: a square of side n is built from L-shaped layers of 1, 3, 5, 7, … unit squares. This is also why the differences of square numbers are 3, 5, 7, …"),
 ("h2", "8.6 Worked Examples"),
 ("h3", "Example 1 — Explicit and recursive rules"),
 ("steps", [("Sequence 4, 7, 10, 13, …", "Constant difference 3, so it is an AP with a = 4."), ("Explicit rule", "tₙ = 4 + 3(n − 1) = 3n + 1, so t₂₀ = 61."), ("Recursive rule", "t₁ = 4 and tₙ₊₁ = tₙ + 3.")]),
 ("h3", "Example 2 — Which term, and is a number a term?"),
 ("steps", [("Which term of 7, 13, 19, … is 151?", "7 + 6(n − 1) = 151 gives n − 1 = 24, so n = 25."), ("Is 100 a term of the same AP?", "7 + 6(n − 1) = 100 gives n − 1 = 15.5, not a whole number, so no. The terms leave remainder 1 when divided by 6, while 100 leaves 4.")]),
 ("h3", "Example 3 — Two terms given"),
 ("steps", [("4th term 14 and 9th term 34", "a + 3d = 14 and a + 8d = 34."), ("Subtract", "5d = 20, so d = 4 and a = 2."), ("20th term and sum", "t₂₀ = 2 + 19 × 4 = 78; S₂₀ = 10 × (2 + 78) = 800.")]),
 ("h3", "Example 4 — Sum of an AP in a word problem"),
 ("steps", [("An auditorium: 18 rows, first row 14 seats, 2 more in every next row", "AP with a = 14, d = 2, n = 18."), ("Last row", "14 + 17 × 2 = 48 seats."), ("Total seats", "S = 18/2 × (14 + 48) = 9 × 62 = 558.")]),
 ("h3", "Example 5 — Sum given, find n (two roots)"),
 ("steps", [("A pile of 400 pipes: bottom row 40, each upper row 2 fewer", "a = 40, d = −2, Sₙ = n(41 − n) = 400."), ("Form the quadratic", "n² − 41n + 400 = 0, so (n − 16)(n − 25) = 0."), ("Reject the impossible root", "n = 25 would give a top row 40 − 48 = −8 pipes, which cannot be. So n = 16 rows (top row 10).")]),
 ("h3", "Example 6 — Three numbers in AP"),
 ("steps", [("Sum 24, product 440", "Take a − d, a, a + d; the sum 3a = 24 gives a = 8."), ("Product", "8(64 − d²) = 440, so d² = 9 and d = ±3."), ("The numbers", "5, 8, 11 (or 11, 8, 5).")]),
 ("h3", "Example 7 — GP with two terms given"),
 ("steps", [("3rd term 12 and 6th term 96", "ar² = 12 and ar⁵ = 96."), ("Divide", "r³ = 8, so r = 2 and a = 3."), ("8th term", "3 × 2⁷ = 384.")]),
 ("h2", "8.7 AP or GP? Comparing the Two"),
 ("table", ["Feature", "AP", "GP"], [
  ["Constant quantity", "difference d = tₙ₊₁ − tₙ", "ratio r = tₙ₊₁ ÷ tₙ"],
  ["nth term", "a + (n − 1)d", "a × rⁿ⁻¹"],
  ["Recursive rule", "tₙ₊₁ = tₙ + d", "tₙ₊₁ = r × tₙ"],
  ["Growth", "linear (graph points on a straight line)", "exponential (curve that bends up if r > 1)"],
  ["Real-life models", "fixed yearly increment, taxi fare, seats in rows, equal savings added", "doubling or tripling cultures, bounce heights, repeated folding, Sierpiński areas"],
  ["Both AP and GP?", "only a constant non-zero sequence (d = 0, r = 1)", "see left"]]),
 ("h2", "8.8 Word Problems: How to Translate"),
 ("table", ["Words in the problem", "Mathematics", "Example"], [
  ["‘starts at … and increases by … each time’", "AP with a = start, d = increase", "₹50, then ₹10 more each week: a = 50, d = 10"],
  ["‘doubles / triples / halves every …’", "GP with r = 2, 3 or ½", "5 bacteria doubling: after 6 hours 5 × 2⁶ = 320"],
  ["‘each row has 2 fewer’", "AP with a negative d", "d = −2 in the pile of pipes"],
  ["‘total / altogether’ over n steps", "Sₙ of an AP", "total seats = 558"],
  ["‘in the nth week / row / year’", "tₙ", "salary in the 9th year = t₉"],
  ["‘how many terms will make the sum …’", "set Sₙ equal to the number; solve the quadratic in n; reject a negative or fractional n", "n(4n + 5) = 636 gives n = 12"],
  ["‘first time it exceeds …’", "solve an inequality; n must be a whole number", "5n − 1 &gt; 100 gives n = 21"],
  ["‘ways to climb / rhythms’", "Virahānka rule: add the previous two", "ways for 7 steps = 21"]]),
 ("note", "REMEMBER", "**Never forget the count of steps.** The 8th term needs (8 − 1) = 7 jumps of d. ‘After 6 hours’ for a doubling culture that started with 5 means the 7th term, 5 × 2⁶, because the starting value is the first term."),
 ("h2", "8.9 Common Mistakes"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["t₁₀ = a + 10d", "d is added (n − 1) times", "t₁₀ = a + 9d"],
  ["2, 4, 8, 16 is an AP because it increases", "equal differences are needed, not just growth", "it is a GP with r = 2"],
  ["Sₙ = (n/2)(a + d)", "mixing up a + l and a + d", "Sₙ = (n/2)(a + l) or (n/2)[2a + (n − 1)d]"],
  ["GP tₙ = (ar)ⁿ⁻¹", "only r is raised to the power", "tₙ = a·rⁿ⁻¹"],
  ["Accepting n = −53/4 as a number of terms", "n counts terms, so it is a positive whole number", "reject it; take n = 12"],
  ["1, 4, 9, 16 has d = 3", "differences are 3, 5, 7: not constant", "not an AP; second differences are constant (2)"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Gauss's pairing:** Sₙ = (n/2)(first + last); the sum of the first n natural numbers is n(n + 1)/2 and of the first n odd numbers is n².", "**Count carefully:** tₙ uses (n − 1) steps; ‘after k doublings’ is the (k + 1)th term.", "In a ‘find n from the sum’ problem you get a quadratic: **reject** negative or impossible roots.", "AP versus GP: **equal differences** versus **equal ratios**; only a constant non-zero sequence is both."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
