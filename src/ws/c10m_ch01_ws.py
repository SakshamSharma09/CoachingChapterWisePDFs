"""Class 10 Maths Ch 1 - Real Numbers: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import gcd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch01"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def lcm(a, b): return a * b // gcd(a, b)
assert 2*2*3*13 == 156 and lcm(8, 12) == 24 and gcd(90, 144) == 18 and lcm(90, 144) == 720
assert lcm(lcm(12, 15), 21) == 420 and gcd(gcd(12, 15), 21) == 3 and 9 * 360 // 45 == 72
assert lcm(lcm(48, 72), 108) == 432 and gcd(420, 130) == 10 and gcd(60, 84) == 12 and gcd(616, 32) == 8
assert gcd(gcd(24, 40), 56) == 8 and 29 * 5 == 145 and 13 * 32 == 416
assert lcm(lcm(40, 56), 72) == 2520 and 2520 // 40 == 63 and 2520 // 56 == 45 and 2520 // 72 == 35
assert lcm(lcm(12, 16), 24) == 48 and gcd(gcd(105, 175), 245) == 35 and gcd(65, 117) == 13
assert lcm(lcm(84, 105), 126) == 1260 and gcd(gcd(84, 105), 126) == 21 and 23 * 1449 // 161 == 207 and 1449 % 161 == 0
assert lcm(lcm(9, 12), 15) == 180 and lcm(12, 28) == 84 and gcd(12, 28) == 4 and 17 * 18 == 306
assert 60 * 17 == 1020 and 7 * 6 * 5 * 4 * 3 * 2 + 5 == 5 * 1009 and 21 / 168 == 0.125 and 7 / 80 == 0.0875 and 17 / 8 == 2.125

WS = [
# ---------------- EASY ----------------
W(r"The prime factorisation of 156 is:", 1, r"(b) $2^2\times3\times13$. $156=2\times78=2\times2\times39=2^2\times3\times13$. (1)", "E", opts=[r"$2\times3\times13^2$", r"$2^2\times3\times13$", r"$2\times3^2\times13$", r"$2^3\times3\times13$"]),
W(r"If $\text{HCF}(8,12)=4$, then $\text{LCM}(8,12)$ is:", 1, r"(b) 24. $\text{LCM}=\dfrac{8\times12}{4}=24$. (1)", "E", opts=["48", "24", "96", "32"]),
W(r"Which of the following numbers is irrational?", 1, r"(c) $2+\sqrt3$. A rational plus an irrational is irrational; $\sqrt{36}/\sqrt9=2$, $0.3333\ldots=\tfrac13$ and $3.14$ are rational. (1)", "E", opts=[r"$\dfrac{\sqrt{36}}{\sqrt9}$", r"$0.3333\ldots$", r"$2+\sqrt3$", r"$3.14$"]),
W(r"The decimal expansion of which of these terminates?", 1, r"(a) $\dfrac7{40}$. In lowest terms $40=2^3\times5$ has only the primes 2 and 5. The others have the factor 3 or 7 in the denominator. (1)", "E", opts=[r"$\dfrac7{40}$", r"$\dfrac5{12}$", r"$\dfrac{11}{30}$", r"$\dfrac4{21}$"]),
W(r"For a natural number $n$, the number $6^n$ ends with the digit 0:", 1, r"(c) for no value of $n$. $6^n=2^n3^n$ has no prime factor 5, so it is never divisible by 10. (1)", "E", opts=[r"for every $n$", r"for even $n$ only", r"for no value of $n$", r"for $n=5$ only"]),
W(r"The value of $\sqrt2\times\sqrt8$ is:", 1, r"(b) 4. $\sqrt2\times\sqrt8=\sqrt{16}=4$, a rational number. (1)", "E", opts=[r"$\sqrt{10}$", "4", r"$2\sqrt2$", "16"]),
W(r"For two positive integers 15 and 20, the product $\text{HCF}\times\text{LCM}$ equals:", 1, r"(c) 300. $\text{HCF}\times\text{LCM}=15\times20=300$ (HCF 5, LCM 60). (1)", "E", opts=["35", "60", "300", "150"]),
W(r"Express 140 as a product of prime factors.", 2, r"$140=2\times70=2\times2\times35$ (1) $=2^2\times5\times7$ (1).", "E"),
W(r"Find the HCF and LCM of 24 and 36 using prime factorisation.", 2, r"$24=2^3\times3$, $36=2^2\times3^2$. HCF $=2^2\times3=12$ (1); LCM $=2^3\times3^2=72$ (1).", "E"),
W(r"Is $7\times11\times13+13$ a prime or a composite number? Give a reason.", 1, r"$7\times11\times13+13=13(77+1)=13\times78$ is a product of two numbers greater than 1, so it is **composite** (1).", "E"),
W(r"Without dividing, state whether $\dfrac{29}{200}$ has a terminating decimal expansion, and if so after how many places the decimal ends.", 2, r"$200=2^3\times5^2$, only 2 and 5, so it terminates (1). The number of decimal places is the larger of the powers 3 and 2, i.e. **3** places ($0.145$) (1).", "E"),
W(r"Ravi and Sunita jog round a circular park. Ravi takes 12 minutes for one round and Sunita takes 18 minutes. If they start together from the same point, after how many minutes will they next be together at the starting point?", 2, r"They are together again after the LCM of 12 and 18 (1). $12=2^2\times3$, $18=2\times3^2$, LCM $=2^2\times3^2=$ **36 minutes** (1).", "E", wp=True),
W(r"A bell in a temple tolls every 15 minutes and another bell tolls every 20 minutes. Both toll together at 6:00 a.m. At what time will they next toll together?", 2, r"LCM of 15 and 20 $=60$ minutes (1). They toll together next at **7:00 a.m.** (1).", "E", wp=True),
W(r"Kavita has 36 red and 48 blue marbles. She wants to put them in identical packets so that every packet has the same number of red marbles and the same number of blue marbles and none is left. What is the largest number of packets she can make?", 2, r"The number of packets must divide both 36 and 48, so the largest is the HCF (1). $\text{HCF}(36,48)=12$ **packets** (each with 3 red and 4 blue) (1).", "E", wp=True),
W(r"True or false? Give a reason. The sum of two irrational numbers is always irrational.", 1, r"**False.** $\sqrt2+(-\sqrt2)=0$, which is rational (1).", "E"),
W(r"A rectangular floor of a classroom measures 96 cm by 72 cm in a model. It is to be covered completely by square tiles of the largest possible size, without cutting. Find the side of each tile and the number of tiles.", 2, r"Side $=\text{HCF}(96,72)=24$ cm (1). Number of tiles $=\dfrac{96}{24}\times\dfrac{72}{24}=4\times3=$ **12** (1).", "E", wp=True),
W(r"Meena says, 'The decimal $0.202020\ldots$ never ends, so it is an irrational number.' Is she right? Explain.", 2, r"No. An irrational number has a decimal that is **non-terminating and non-repeating** (1). Here the block 20 repeats, so the number is rational (it equals $\tfrac{20}{99}$) (1).", "E"),
# ---------------- MEDIUM ----------------
W(r"Find the HCF and LCM of 90 and 144 by prime factorisation and verify that $\text{HCF}\times\text{LCM}$ equals the product of the numbers.", 3, r"$90=2\times3^2\times5$, $144=2^4\times3^2$ (1). HCF $=2\times3^2=18$, LCM $=2^4\times3^2\times5=720$ (1). $18\times720=12960=90\times144$ ✓ (1).", "M"),
W(r"Find the HCF and LCM of 12, 15 and 21 by prime factorisation.", 3, r"$12=2^2\times3$, $15=3\times5$, $21=3\times7$ (1). HCF $=3$ (1). LCM $=2^2\times3\times5\times7=420$ (1).", "M"),
W(r"The HCF of two numbers is 9 and their LCM is 360. If one of the numbers is 45, find the other.", 2, r"$\text{HCF}\times\text{LCM}=$ product of the two numbers (1). Other number $=\dfrac{9\times360}{45}=$ **72** (1).", "M"),
W(r"Three traffic lights at a crossing change after every 48 s, 72 s and 108 s. They change together at 7:00 a.m. At what time will they next change together?", 3, r"Required time $=\text{LCM}(48,72,108)$ (1). $48=2^4\times3$, $72=2^3\times3^2$, $108=2^2\times3^3$, so LCM $=2^4\times3^3=432$ s (1) $=7$ min 12 s. Next together at **7:07:12 a.m.** (1).", "M", wp=True),
W(r"A sweet seller has 420 kaju barfi and 130 badam barfi. He wants to stack them in trays so that each tray has the same number of pieces, with only one kind of sweet in a tray. Find the number of pieces in each tray and the minimum number of trays needed.", 3, r"Pieces per tray must divide both 420 and 130; for the **minimum** number of trays take the HCF (1). $420=2^2\times3\times5\times7$, $130=2\times5\times13$, HCF $=10$ (1). Trays $=\dfrac{420}{10}+\dfrac{130}{10}=42+13=$ **55** (1).", "M", wp=True),
W(r"In a school sports day in Kota, 60 boys and 84 girls have to be seated in rows so that every row has the same number of students and no row mixes boys and girls. Find the maximum number of students in a row and the total number of rows.", 3, r"Row size must divide 60 and 84; maximum $=\text{HCF}(60,84)=12$ (1,1). Rows $=\dfrac{60}{12}+\dfrac{84}{12}=5+7=$ **12** (1).", "M", wp=True),
W(r"Given that $\sqrt3$ is irrational, prove that $5-\sqrt3$ is irrational.", 3, r"Suppose $5-\sqrt3$ is rational, equal to $r$ (1). Then $\sqrt3=5-r$ (1). The right side is rational, but $\sqrt3$ is irrational, a contradiction. Hence $5-\sqrt3$ is **irrational** (1).", "M"),
W(r"Given that $p$ prime and $p\mid a^2\Rightarrow p\mid a$, prove that $\sqrt5$ is irrational.", 3, r"Suppose $\sqrt5=\dfrac ab$ with $a,b$ co-prime, $b\ne0$. Then $5b^2=a^2$ (1), so $5\mid a^2$, hence $5\mid a$; let $a=5c$ (1). Then $5b^2=25c^2$, so $b^2=5c^2$ and $5\mid b$. Now 5 divides both $a$ and $b$, contradicting that they are co-prime. So $\sqrt5$ is irrational (1).", "M"),
W(r"Without long division, say which of these have terminating decimal expansions: (i) $\dfrac{13}{3125}$ (ii) $\dfrac{17}{8}$ (iii) $\dfrac{64}{455}$ (iv) $\dfrac{15}{1600}$ (v) $\dfrac{29}{343}$ (vi) $\dfrac{77}{210}$", 3, r"(i) $3125=5^5$: terminates. (ii) $8=2^3$: terminates. (iii) $455=5\times7\times13$: non-terminating repeating. (iv) $\tfrac{15}{1600}=\tfrac3{320}$, $320=2^6\times5$: terminates. (v) $343=7^3$: non-terminating repeating. (vi) $\tfrac{77}{210}=\tfrac{11}{30}$, factor 3: non-terminating repeating. (Any 6 correct: 3 marks; 3-5 correct: 2 marks.) (3)", "M"),
W(r"Can $14^n$ end with the digit 0 for some natural number $n$? Give a reason.", 2, r"If it ended in 0 it would be divisible by 5 (and 2) (1). But $14^n=2^n\times7^n$ has only the primes 2 and 7, so by uniqueness of prime factorisation there is no factor 5. **No.** (1)", "M"),
W(r"Explain why $7\times6\times5\times4\times3\times2\times1+5$ and $17\times19+19$ are composite numbers.", 2, r"$7\times6\times5\times4\times3\times2\times1+5=5040+5=5(1008+1)=5\times1009$, a product of two numbers greater than 1 (1). $17\times19+19=19(17+1)=19\times18$, also a product of two such numbers (1). Both are composite.", "M"),
W(r"An army contingent of 616 members is to march behind an army band of 32 members. The two groups march in the same number of columns. What is the maximum number of columns in which they can march?", 3, r"The number of columns divides both 616 and 32; the maximum is the HCF (1). $616=2^3\times7\times11$, $32=2^5$ (1). $\text{HCF}=2^3=$ **8 columns** (1).", "M", wp=True),
W(r"Find the smallest 4-digit number that is divisible by 12, 15 and 20.", 3, r"$\text{LCM}(12,15,20)=60$ (1). The smallest 4-digit number is 1000; $1000\div60$ gives 16 full multiples and remainder 40, so the next multiple is $60\times17$ (1) $=$ **1020** (1).", "M"),
W(r"Given that $\sqrt2$ is irrational, show that $7\sqrt2$ is irrational.", 2, r"Suppose $7\sqrt2=r$, a rational number (1). Then $\sqrt2=\dfrac r7$ would be rational, a contradiction. So $7\sqrt2$ is irrational (1).", "M"),
W(r"Using the denominators only, find the number of decimal places in the expansion of $\dfrac{13}{3125}$ and then write the decimal.", 2, r"$3125=5^5$, so the decimal terminates after **5 places** (1). $\dfrac{13}{3125}=\dfrac{13\times2^5}{10^5}=\dfrac{416}{100000}=0.00416$ (1).", "M"),
W(r"Three ropes of lengths 24 m, 40 m and 56 m are to be cut into pieces of the same length with nothing left over. Find the greatest possible length of a piece and the total number of pieces.", 3, r"Greatest length $=\text{HCF}(24,40,56)=8$ m (1,1). Pieces $=3+5+7=$ **15** (1).", "M", wp=True),
W(r"Rohan finds the HCF of 18 and 30 as follows: $18=2\times3^2$, $30=2\times3\times5$, so $\text{HCF}=2\times3^2\times5=90$. Find his mistake and give the correct HCF and LCM.", 2, r"He took the **greatest** powers of **all** primes, which gives the LCM, not the HCF (1). HCF $=2\times3=6$ and LCM $=90$ (check $6\times90=540=18\times30$) (1).", "M"),
W(r"True or false? Give a reason. $(2+\sqrt3)(2-\sqrt3)$ is an irrational number.", 2, r"**False.** $(2+\sqrt3)(2-\sqrt3)=4-3=1$ (1), which is rational. The product of two irrational numbers can be rational (1).", "M"),
# ---------------- HARD ----------------
W(r"The HCF of two numbers is 23 and their LCM is 1449. If one number is 161, find the other and verify your answer.", 3, r"Other number $=\dfrac{23\times1449}{161}=\dfrac{33327}{161}=207$ (1,1). Check: $161=7\times23$, $207=9\times23$; HCF $=23$ ✓, LCM $=23\times7\times9=1449$ ✓ (1).", "H"),
W(r"Three runners practise on a circular track. They take 40 s, 56 s and 72 s for one lap and start together from the same point. After how many seconds will all three be at the starting point together? How many laps will each have run then?", 4, r"Time $=\text{LCM}(40,56,72)$ (1). $40=2^3\times5$, $56=2^3\times7$, $72=2^3\times3^2$, LCM $=2^3\times3^2\times5\times7=2520$ s $=42$ min (1). Laps: $\dfrac{2520}{40}=63$, $\dfrac{2520}{56}=45$, $\dfrac{2520}{72}=35$ (2).", "H", wp=True),
W(r"Prove that $\sqrt3$ is irrational.", 4, r"Suppose $\sqrt3=\dfrac ab$, $a,b$ co-prime integers, $b\ne0$ (1). Then $3b^2=a^2$, so $3\mid a^2$ and therefore $3\mid a$ (1). Write $a=3c$; then $3b^2=9c^2$, $b^2=3c^2$, so $3\mid b$ (1). Then 3 is a common factor of $a$ and $b$, contradicting that they are co-prime. Hence $\sqrt3$ is irrational (1).", "H"),
W(r"Find the least number which, when divided by 12, 16 and 24, leaves the remainder 5 in each case.", 3, r"The number is 5 more than a common multiple of 12, 16 and 24 (1). $\text{LCM}=48$ (1). Least number $=48+5=$ **53** (1). (Check: $53=12\times4+5=16\times3+5=24\times2+5$.)", "H", wp=True),
W(r"A farmer has 105 bags of wheat, 175 bags of bajra and 245 bags of maize. He loads trucks so that each truck carries the same number of bags of a single crop. Find (i) the largest number of bags per truck, (ii) the number of trucks, (iii) the total hire if each truck costs ₹ 2,500.", 4, r"(i) $\text{HCF}(105,175,245)=35$ bags ($105=3\times5\times7$, $175=5^2\times7$, $245=5\times7^2$) (2). (ii) Trucks $=\dfrac{105}{35}+\dfrac{175}{35}+\dfrac{245}{35}=3+5+7=15$ (1). (iii) $15\times2500=$ ₹ **37,500** (1).", "H", wp=True),
W(r"If $p=a^3b^2$ and $q=a^2b$ where $a$ and $b$ are distinct primes, find $\text{HCF}(p,q)$ and $\text{LCM}(p,q)$ and verify that $\text{HCF}\times\text{LCM}=pq$.", 3, r"Smallest powers of common primes: $\text{HCF}=a^2b$ (1). Greatest powers: $\text{LCM}=a^3b^2$ (1). $a^2b\times a^3b^2=a^5b^3=pq$ ✓ (1).", "H"),
W(r"Pooja says, '$\dfrac{21}{168}$ cannot have a terminating decimal because $168=2^3\times3\times7$ contains the primes 3 and 7.' Is she correct? Find the decimal expansion.", 3, r"No (1). The fraction must first be reduced to lowest terms: $\dfrac{21}{168}=\dfrac18$ (1), and $8=2^3$ has only the prime 2, so it terminates: $0.125$ (1).", "H"),
W(r"Can $15^n$ end with the digit 0 for any natural number $n$? What is the last digit of $15^n$? Justify.", 3, r"$15^n=3^n\times5^n$ has no prime factor 2, so it is odd and not divisible by 10; it cannot end in 0 (1). It is a multiple of 5 and odd, so its last digit is 5 (1). Check: $15,225,3375,\ldots$ all end in 5 (1).", "H"),
W(r"Three bells in a temple ring at intervals of 9, 12 and 15 minutes. They ring together at 4:00 p.m. How many times will they ring together between 4:00 p.m. and 10:00 p.m., counting the 4:00 p.m. ring and any at 10:00 p.m.?", 3, r"$\text{LCM}(9,12,15)=180$ min (1) $=3$ hours (1). They ring together at 4:00, 7:00 and 10:00 p.m., i.e. **3 times** (1).", "H", wp=True),
W(r"Find the greatest number that divides 70 and 125, leaving remainders 5 and 8 respectively.", 3, r"The number divides $70-5=65$ and $125-8=117$ exactly (1). $65=5\times13$, $117=3^2\times13$, HCF $=13$ (1). It exceeds both remainders (13 > 8), so the number is **13** (1).", "H", wp=True),
W(r"Give an example of two irrational numbers whose (i) sum is rational, (ii) product is rational, (iii) sum is irrational, (iv) quotient is rational. Verify each.", 4, r"(i) $\sqrt2$ and $-\sqrt2$: sum $0$. (ii) $\sqrt3$ and $\sqrt3$: product $3$. (iii) $\sqrt2$ and $\sqrt3$ (or $\sqrt2+\sqrt2=2\sqrt2$): sum irrational. (iv) $2\sqrt5$ and $\sqrt5$: quotient $2$. (1 mark each; other correct pairs are accepted.)", "H"),
W(r"**Case study.** On the Annual Day, a school in Jaipur has three batches of students: 84 in the dance group, 105 in the music group and 126 in the drama group. The coordinator forms teams of equal size, each team from one group only. (i) What is the largest possible team size? (ii) How many teams are formed? (iii) The principal wants a number of chairs that can be arranged exactly in rows of 84, or exactly in rows of 105, or exactly in rows of 126: find the smallest such number of chairs.", 5, r"(i) $84=2^2\times3\times7$, $105=3\times5\times7$, $126=2\times3^2\times7$; HCF $=3\times7=21$ (2). (ii) Teams $=\dfrac{84}{21}+\dfrac{105}{21}+\dfrac{126}{21}=4+5+6=15$ (1). (iii) The number must be a common multiple, the smallest is $\text{LCM}=2^2\times3^2\times5\times7=1260$ chairs (2).", "H", wp=True),
W(r"Show that $\text{HCF}(8,15)\times\text{LCM}(8,15)=8\times15$. Then, for any two consecutive natural numbers $n$ and $n+1$, write the HCF and LCM and give them for 17 and 18.", 3, r"$8=2^3$, $15=3\times5$: HCF $=1$, LCM $=120=8\times15$ ✓ (1). Consecutive numbers share no prime factor, so $\text{HCF}=1$ and $\text{LCM}=n(n+1)$ (1). For 17 and 18: HCF $=1$, LCM $=306$ (1).", "H"),
W(r"The LCM of 12 and a number $x$ is 84 and their HCF is 4. Find $x$ and verify.", 3, r"$12x=\text{HCF}\times\text{LCM}=4\times84=336$ (1), so $x=28$ (1). Check: $12=2^2\times3$, $28=2^2\times7$: HCF $=4$ ✓, LCM $=2^2\times3\times7=84$ ✓ (1).", "H"),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(1)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "1.6 More Worked Examples"),
 ("h3", "Example 1 — HCF and LCM of three numbers"),
 ("steps", [("Find the HCF and LCM of 12, 15 and 21", "12 = 2² × 3, 15 = 3 × 5, 21 = 3 × 7."), ("HCF", "The only prime common to all three is 3, with smallest power 3¹, so HCF = **3**."), ("LCM", "Take every prime with its greatest power: 2² × 3 × 5 × 7 = **420**. (Remember HCF × LCM = product works only for **two** numbers.)")]),
 ("h3", "Example 2 — Finding the missing number"),
 ("steps", [("The HCF of two numbers is 23, the LCM is 1449, one number is 161", "Use HCF × LCM = product of the two numbers."), ("Compute", "Other number = (23 × 1449) ÷ 161 = 33327 ÷ 161 = 207."), ("Verify", "161 = 7 × 23 and 207 = 9 × 23, so HCF = 23 and LCM = 23 × 7 × 9 = 1449. ✓")]),
 ("h3", "Example 3 — Proving irrationality of a combination"),
 ("steps", [("Prove that 3 + 2√5 is irrational", "Assume 3 + 2√5 = r, a rational number."), ("Isolate the root", "2√5 = r − 3, so √5 = (r − 3)/2."), ("Contradict", "(r − 3)/2 is rational but √5 is irrational. So the assumption is false and **3 + 2√5 is irrational**.")]),
 ("h3", "Example 4 — Terminating or not?"),
 ("steps", [("Is 21/168 a terminating decimal?", "First reduce to lowest terms: 21/168 = 1/8."), ("Look at the denominator", "8 = 2³ has only the prime 2, so the decimal terminates."), ("Decimal", "1/8 = **0.125**. Had we looked at 168 = 2³ × 3 × 7 without reducing, we would have wrongly said non-terminating.")]),
 ("h3", "Example 5 — Remainder problem"),
 ("steps", [("Greatest number dividing 70 and 125 leaving remainders 5 and 8", "The number divides 70 − 5 = 65 and 125 − 8 = 117 exactly."), ("HCF", "65 = 5 × 13 and 117 = 3² × 13, so HCF = 13."), ("Check", "13 is larger than both remainders (5 and 8), so it is valid. Answer: **13**.")]),
 ("h3", "Example 6 — Smallest number leaving a remainder"),
 ("steps", [("Least number leaving remainder 5 when divided by 12, 16 and 24", "The number is 5 more than a common multiple."), ("LCM", "12 = 2² × 3, 16 = 2⁴, 24 = 2³ × 3, so LCM = 2⁴ × 3 = 48."), ("Answer", "Least number = 48 + 5 = **53**.")]),
 ("h2", "1.7 Word Problems: How to Translate"),
 ("table", ["Clue in the problem", "Concept", "Example"], [
  ["‘meet again at the starting point’, ‘ring together’, ‘change together’, ‘next time’", "LCM of the times", "Bells at 15 and 20 min toll together after 60 min"],
  ["‘largest’, ‘greatest’, ‘maximum size’ of a tile, packet, row or rope piece", "HCF", "Largest square tile for 96 cm × 72 cm: HCF = 24 cm"],
  ["‘minimum number of trays / trucks / columns’", "use the HCF as the group size, then divide", "420 and 130 sweets: 10 per tray gives 42 + 13 = 55 trays"],
  ["‘smallest number divisible by …’", "LCM", "Smallest number divisible by 12, 15, 20 is 60"],
  ["‘leaves remainder r’", "subtract r first, then HCF (largest divisor) or add r to the LCM (smallest number)", "Least number leaving 5 with 12, 16, 24: 48 + 5 = 53"],
  ["one number and the HCF and LCM are given", "HCF × LCM = a × b (two numbers)", "9 × 360 ÷ 45 = 72"]]),
 ("note", "REMEMBER", "In an LCM problem the answer is a **time or quantity when things coincide**; in an HCF problem the answer is the **size of the biggest equal group or piece**. Ask: *do I need a common multiple (bigger) or a common divisor (smaller)?*"),
 ("h2", "1.8 Which Numbers Are Rational or Irrational?"),
 ("table", ["Number", "Type", "Reason"], [
  ["√2, √3, √5, √7", "irrational", "square roots of primes"],
  ["√16, √49, √(36)/√9", "rational", "perfect squares: 4, 7, 2"],
  ["2 + √3, 5 − √3, 7√2, 3 + 2√5", "irrational", "non-zero rational and irrational combined"],
  ["(2 + √3)(2 − √3) = 1", "rational", "the product of two irrationals can be rational"],
  ["√2 + (−√2) = 0", "rational", "the sum of two irrationals can be rational"],
  ["0.202020… (block repeats)", "rational", "repeating decimal"],
  ["0.1010010001… (no repeat)", "irrational", "non-terminating and non-repeating"]]),
 ("h2", "1.9 Common Mistakes"),
 ("table", ["Mistake", "Why it is wrong", "Correct idea"], [
  ["Taking greatest powers of all primes for the HCF", "that gives the LCM", "HCF: smallest powers of **common** primes only"],
  ["Using HCF × LCM = a × b × c for three numbers", "valid only for two numbers", "find HCF and LCM of three numbers by factorisation"],
  ["Saying 21/168 is non-terminating because 168 has factors 3 and 7", "the fraction was not in lowest terms", "reduce first: 1/8 = 0.125"],
  ["‘The sum of irrationals is irrational’", "√2 + (−√2) = 0", "the result can be rational or irrational"],
  ["Writing 1 as a prime", "a prime has exactly two factors; 1 has one", "1 is neither prime nor composite"],
  ["Forgetting the remainder step in ‘leaves remainder r’", "r must be taken off before finding the HCF", "use (number − remainder) and make sure the divisor > r"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["Use the **clue words** in a word problem: *together / next time* means LCM; *largest / greatest group or piece* means HCF.", "For problems with remainders, **subtract the remainder first** (HCF) or **add it at the end** (LCM).", "Always **reduce a fraction to lowest terms** before testing whether its decimal terminates."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
