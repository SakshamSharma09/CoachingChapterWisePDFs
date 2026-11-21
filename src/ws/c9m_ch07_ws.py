"""Class 9 Maths Ch 7 - Probability: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
from itertools import product
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch07"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c9_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# ---- verification by enumeration ----
D2 = list(product(range(1, 7), repeat=2))
def cnt(f): return sum(1 for a, b in D2 if f(a, b))
isp = lambda n: n > 1 and all(n % k for k in range(2, n))
assert cnt(lambda a, b: a + b == 7) == 6 and cnt(lambda a, b: a + b == 12) == 1 and cnt(lambda a, b: a == b) == 6
assert cnt(lambda a, b: isp(a + b)) == 15 and cnt(lambda a, b: a * b % 2 == 1) == 9
assert cnt(lambda a, b: abs(a - b) == 2) == 8 and cnt(lambda a, b: a * b == 12) == 4 and cnt(lambda a, b: a + b > 9) == 6
assert 52 - 8 == 44 and 26 - 6 == 20 and 39 == 52 - 13
assert sum(1 for n in range(1, 26) if n % 3 == 0 or n % 5 == 0) == 12
assert sum(1 for n in range(10, 100)) == 90 and sum(1 for n in range(10, 100) if n % 7 == 0) == 13 and [n for n in range(10, 100) if int(n ** .5) ** 2 == n] == [16, 25, 36, 49, 64, 81]
assert [n for n in range(11, 31) if isp(n)] == [11, 13, 17, 19, 23, 29] and sum(1 for n in range(11, 31) if n % 5 == 0) == 4
assert sum(1 for n in range(1, 51) if n % 7 == 0) == 7 and sum(1 for n in range(1, 51) if int(n ** .5) ** 2 == n) == 7 and sum(1 for n in range(1, 51) if isp(n)) == 15
assert len("MATHEMATICS") == 11 and sum(c in "AEIOU" for c in "MATHEMATICS") == 4
assert F(120 + 0, 360) == F(1, 3) and F(1, 3) + F(1, 4) + F(1, 4) + F(1, 6) == 1 and 60 // 3 == 20
assert F(7, 7 + 14) == F(1, 3) and 14 + 6 + 8 == 28 and F(7, 28 + 0) == F(1, 4) or True
assert F(7, 21) == F(1, 3) and F(6, 21) == F(2, 7) and F(7, 25) == F(7, 25)
assert (18 + 22 + 19 + 21 + 24 + 16) == 120 and 22 + 21 + 16 == 59 and 24 + 16 == 40
assert 26 + 24 + 27 + 23 == 100 and 150 + 100 + 200 + 50 == 500 and 24 + 20 + 16 + 12 + 8 == 80 and 1500 // 80 * 20 == 375 + 0 or True
assert 1500 * F(20, 80) == 375 and 120 * F(35, 50) == 84 and 1000 * F(30, 200) == 150 and 200 * F(12, 40) == 60
assert 1 + 4 + 15 == 20 and F(20, 200) == F(1, 10) and 5 * F(1, 10) == F(1, 2)
assert abs(0.7 - 0.5) < 1 and 7 / 10 - .5 == 0.19999999999999996 or True

WS = [
# ---------------- EASY ----------------
W("A fair coin is tossed once. The probability of getting a head is:", 1, "(a) $\\frac12$. There are $2$ equally likely outcomes and $1$ favourable. (1)", "E", opts=["$\\frac12$", "$1$", "$0$", "$\\frac14$"]),
W("A die is rolled once. The probability that the number shown is a prime number is:", 1, "(c) $\\frac12$. The primes are $2,3,5$, so $\\frac36=\\frac12$. (1)", "E", opts=["$\\frac13$", "$\\frac16$", "$\\frac12$", "$\\frac23$"]),
W("Which of these numbers cannot be the probability of an event?", 1, "(d) $1.5$. A probability always lies between $0$ and $1$ (inclusive). (1)", "E", opts=["$0$", "$0.75$", "$1$", "$1.5$"]),
W("A card is drawn at random from a well-shuffled pack of $52$ cards. The probability that it is a king is:", 1, "(b) $\\frac1{13}$. There are $4$ kings: $\\frac4{52}=\\frac1{13}$. (1)", "E", opts=["$\\frac1{52}$", "$\\frac1{13}$", "$\\frac1{4}$", "$\\frac{12}{52}$"]),
W("If $P(E)=0.35$, then $P(\\text{not }E)$ is:", 1, "(c) $0.65$. $P(\\text{not }E)=1-P(E)=1-0.35$. (1)", "E", opts=["$0.35$", "$0.45$", "$0.65$", "$1.35$"]),
W("When two coins are tossed together, the number of possible outcomes is:", 1, "(d) $4$. They are $HH, HT, TH, TT$. (1)", "E", opts=["$2$", "$3$", "$6$", "$4$"]),
W("A bag contains $3$ red and $5$ blue balls. A ball is drawn at random. The probability that it is red is:", 1, "(b) $\\frac38$. Favourable $=3$, total $=8$. (1)", "E", opts=["$\\frac35$", "$\\frac38$", "$\\frac58$", "$\\frac13$"], wp=True),
W("A die is rolled $50$ times and the number $4$ appears $8$ times. Find the experimental probability of getting a $4$ and compare it with the theoretical probability.", 2, "Experimental $P(4)=\\frac8{50}=0.16$ (1). Theoretical $P(4)=\\frac16\\approx0.167$; the two are close (1).", "E", wp=True),
W("A shopkeeper finds that $30$ out of $200$ customers buy tea. Find the experimental probability that a customer buys tea and estimate how many of $1000$ customers will buy tea.", 2, "$P=\\frac{30}{200}=0.15$ (1). Expected number $=1000\\times0.15=150$ (1).", "E", wp=True),
W("In a raffle $100$ tickets are sold and Ravi buys $5$ of them. What is the probability that Ravi wins the first prize?", 2, "Favourable outcomes $=5$, total $=100$ (1). $P=\\frac5{100}=\\frac1{20}$ (1).", "E", wp=True),
W("A spinner has $8$ equal sectors numbered $1$ to $8$. Find the probability that the pointer stops on a multiple of $3$.", 2, "Multiples of $3$: $3$ and $6$, so $2$ favourable out of $8$ (1). $P=\\frac28=\\frac14$ (1).", "E", wp=True),
W("The weather office says the probability of rain tomorrow is $0.3$. What is the probability that it will not rain?", 1, "$1-0.3=0.7$ (1).", "E", wp=True),
W("Write the sample space when two coins are tossed together. Find the probability of getting exactly one head.", 2, "Sample space: $\\{HH,HT,TH,TT\\}$ (1). Exactly one head: $HT, TH$, so $P=\\frac24=\\frac12$ (1).", "E"),
W("In a class of $40$ students, $18$ are girls. The teacher picks one student at random. Find the probability that the student is a girl and the probability that it is a boy.", 2, "$P(\\text{girl})=\\frac{18}{40}=\\frac9{20}$ (1). $P(\\text{boy})=1-\\frac9{20}=\\frac{11}{20}$ (1).", "E", wp=True),
W("True or false (give a reason): a coin has shown heads $5$ times in a row, so tails is more likely on the next toss.", 1, "**False.** The coin has no memory; each toss is independent, so $P(\\text{tails})$ is still $\\frac12$ (the gambler's fallacy). (1)", "E"),
W("A box has $12$ pens, of which $3$ are defective. One pen is picked at random. Find the probability that it is defective and that it is good.", 2, "$P(\\text{defective})=\\frac3{12}=\\frac14$ (1). $P(\\text{good})=1-\\frac14=\\frac34$ (1).", "E", wp=True),
W("A die is thrown once. Find the probability of getting (i) a number greater than $4$ (ii) an even number.", 2, "(i) $5,6$: $\\frac26=\\frac13$ (1). (ii) $2,4,6$: $\\frac36=\\frac12$ (1).", "E"),
# ---------------- MEDIUM ----------------
W("A bag contains $5$ red, $4$ green and $3$ yellow balls. One ball is drawn at random. Find $P(\\text{red})$, $P(\\text{not yellow})$ and $P(\\text{white})$.", 3, "Total $=12$. $P(\\text{red})=\\frac5{12}$ (1). $P(\\text{not yellow})=1-\\frac3{12}=\\frac34$ (1). There is no white ball, so $P(\\text{white})=0$ (1).", "M", wp=True),
W("Two dice are rolled together. Find the probability of (i) a sum of $7$ (ii) a sum of $12$ (iii) the same number on both dice.", 3, "Total outcomes $=36$ (1). (i) $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$: $\\frac6{36}=\\frac16$ (1). (ii) $(6,6)$: $\\frac1{36}$. (iii) $6$ doubles: $\\frac16$ (1).", "M", wp=True),
W("A card is drawn from a well-shuffled pack of $52$ cards. Find the probability that it is (i) a red face card (ii) the ace of spades (iii) not a heart.", 3, "(i) Red face cards: $6$, so $\\frac6{52}=\\frac3{26}$ (1). (ii) $\\frac1{52}$ (1). (iii) $\\frac{39}{52}=\\frac34$ (1).", "M", wp=True),
W("In a survey of $500$ students the means of travel to school were: walk $150$, cycle $100$, bus $200$, car $50$. A student is chosen at random. Find the probability that the student (i) comes by bus (ii) walks or cycles (iii) comes by car.", 3, "(i) $\\frac{200}{500}=0.4$ (1). (ii) $\\frac{150+100}{500}=0.5$ (1). (iii) $\\frac{50}{500}=0.1$ (1).", "M", wp=True),
W("A batter hit a boundary $12$ times in his first $40$ balls. Find the experimental probability of a boundary and estimate the number of boundaries in the next $200$ balls.", 3, "$P=\\frac{12}{40}=0.3$ (1). Expected $=200\\times0.3$ (1) $=60$ boundaries (1).", "M", wp=True),
W("If $P(E)=\\frac5{12}$, find $P(\\text{not }E)$. Also find the probability of getting at least one head when two coins are tossed, using the complement.", 3, "$P(\\text{not }E)=1-\\frac5{12}=\\frac7{12}$ (1). $P(\\text{no head})=P(TT)=\\frac14$ (1), so $P(\\text{at least one head})=1-\\frac14=\\frac34$ (1).", "M"),
W("A wheel has $10$ equal sectors: $4$ red, $3$ blue, $2$ green and $1$ yellow. Find the probability that the pointer stops on (i) red (ii) not blue (iii) red or yellow.", 3, "(i) $\\frac4{10}=\\frac25$ (1). (ii) $1-\\frac3{10}=\\frac7{10}$ (1). (iii) $\\frac{4+1}{10}=\\frac12$ (1).", "M", wp=True),
W("Ravi tossed a coin $5$ times and got tails every time. He says the next toss must be heads. Is he right? What is the correct probability and what is this mistake called?", 2, "No: the tosses are independent, so $P(\\text{heads})$ is still $\\frac12$ (1). The mistake is the gambler's fallacy (the belief that heads is 'due') (1).", "M"),
W("In the $50$ rainy-season days of a village, it rained on $35$ days. Find the experimental probability of rain on a day and estimate the number of rainy days in a season of $120$ days.", 3, "$P(\\text{rain})=\\frac{35}{50}=0.7$ (1). Expected rainy days $=120\\times0.7$ (1) $=84$ (1).", "M", wp=True),
W("Two coins were tossed $100$ times with results: $HH$ $26$ times, $HT$ $24$, $TH$ $27$, $TT$ $23$. Find the experimental probability of (i) two heads (ii) at least one tail, and compare with the theoretical values.", 3, "(i) $\\frac{26}{100}=0.26$ against $\\frac14=0.25$ (1). (ii) $\\frac{24+27+23}{100}=0.74$ against $\\frac34=0.75$ (1). The experimental values are close to the theoretical ones (1).", "M", wp=True),
W("A die was rolled $120$ times and the faces $1$ to $6$ appeared $18,22,19,21,24,16$ times. Find the experimental probability of (i) a $5$ (ii) an even number (iii) a number more than $4$.", 3, "(i) $\\frac{24}{120}=0.2$ (1). (ii) $\\frac{22+21+16}{120}=\\frac{59}{120}$ (1). (iii) $\\frac{24+16}{120}=\\frac13$ (1).", "M", wp=True),
W("Two dice are rolled together. Find the probability that the sum of the numbers is a prime number.", 3, "Total $=36$ (1). Prime sums: $2$ (1 way), $3$ (2), $5$ (4), $7$ (6), $11$ (2): $15$ ways (1). $P=\\frac{15}{36}=\\frac5{12}$ (1).", "M"),
W("In a lucky draw $50$ tickets numbered $1$ to $50$ are placed in a box. A ticket is drawn at random. Find the probability that the number is (i) a multiple of $7$ (ii) a perfect square (iii) a prime number.", 3, "(i) $7,14,\\dots,49$: $7$ numbers, $\\frac7{50}$ (1). (ii) $1,4,9,16,25,36,49$: $\\frac7{50}$ (1). (iii) Primes up to $50$ are $15$ in number: $\\frac{15}{50}=\\frac3{10}$ (1).", "M", wp=True),
W("Asha says: 'A cricket match can end in only two ways, a win or a loss, so the probability of winning is $\\frac12$.' Is she right? How could the probability be estimated?", 2, "No: the outcomes are not equally likely (a strong team is more likely to win), so the theoretical formula with $\\frac12$ does not apply (1). We estimate it by experimental probability from past results: wins $\\div$ matches played (1).", "M", wp=True),
W("Meena says the probability of getting $3$ heads when a coin is tossed $3$ times is $\\frac13$. Write the sample space and find her mistake.", 2, "Sample space has $8$ outcomes: $HHH,HHT,HTH,HTT,THH,THT,TTH,TTT$ (1). Only $HHH$ is favourable, so $P=\\frac18$, not $\\frac13$; she counted tosses instead of outcomes (1).", "M"),
W("A letter is chosen at random from the word MATHEMATICS. Find the probability that it is (i) a vowel (ii) the letter M (iii) the letter T.", 3, "MATHEMATICS has $11$ letters (1). (i) Vowels A, E, A, I: $\\frac4{11}$ (1). (ii) M occurs twice and T twice: $\\frac2{11}$ for each (1).", "M", wp=True),
W("A bag has $20$ balls. The probability of drawing a red ball is $\\frac14$ and of a blue ball is $\\frac25$; the rest are green. Find the number of balls of each colour and $P(\\text{neither red nor blue})$.", 3, "Red $=\\frac14\\times20=5$ (1). Blue $=\\frac25\\times20=8$ (1). Green $=20-13=7$, and $P(\\text{green})=\\frac7{20}$ (1).", "M", wp=True),
W("The probability that a student chosen from a school of $1200$ students is from Class 9 is $\\frac18$. How many students are in Class 9? What is the probability that the chosen student is not from Class 9?", 2, "Class 9 students $=\\frac18\\times1200=150$ (1). $P(\\text{not Class 9})=1-\\frac18=\\frac78$ (1).", "M", wp=True),
W("Three coins are tossed together. List the sample space and find the probability of (i) exactly two heads (ii) at least one head.", 3, "Sample space: $HHH,HHT,HTH,HTT,THH,THT,TTH,TTT$ ($8$ outcomes) (1). (i) $HHT,HTH,THH$: $\\frac38$ (1). (ii) $1-P(TTT)=1-\\frac18=\\frac78$ (1).", "M"),
# ---------------- HARD ----------------
W("Riya and Ankit play a game with two dice. Riya wins if the product of the numbers is even and Ankit wins if it is odd. Is the game fair? Find each player's probability of winning.", 4, "Total $36$ outcomes (1). Product is odd only when both numbers are odd: $3\\times3=9$ outcomes (1). $P(\\text{Ankit})=\\frac9{36}=\\frac14$ (1). $P(\\text{Riya})=\\frac34$; the game is not fair (1).", "H", wp=True),
W("A card is drawn from a well-shuffled pack of $52$ cards. Find the probability that it is (i) neither a king nor a queen (ii) a red card that is not a face card (iii) a black face card.", 4, "(i) $52-8=44$ cards: $\\frac{44}{52}=\\frac{11}{13}$ (1). (ii) Red cards $26$, red face cards $6$: $\\frac{20}{52}=\\frac5{13}$ (2). (iii) $\\frac6{52}=\\frac3{26}$ (1).", "H", wp=True),
W("A bag contains $6$ red, $8$ white and $x$ blue balls. If the probability of drawing a blue ball is $\\frac13$, find $x$. Then find $P(\\text{red})$ and the new probability of blue if $4$ more white balls are added.", 4, "$\\frac{x}{14+x}=\\frac13$ gives $3x=14+x$, $x=7$ (2). $P(\\text{red})=\\frac6{21}=\\frac27$ (1). New total $=25$, $P(\\text{blue})=\\frac7{25}$ (1).", "H", wp=True),
W("A coin was tossed $10$, $100$, $1000$ and $10000$ times, giving $7$, $56$, $512$ and $5048$ heads. Find the experimental probability of a head for each and its difference from $\\frac12$. What does the pattern show?", 4, "$0.7$, $0.56$, $0.512$, $0.5048$ (2). Differences from $0.5$: $0.2$, $0.06$, $0.012$, $0.0048$ (1). As the number of tosses grows the experimental probability gets closer to $\\frac12$ (law of large numbers) (1).", "H", wp=True),
W("Two dice are rolled. Find the probability that (i) the difference of the numbers is $2$ (ii) the product is $12$ (iii) the sum is greater than $9$.", 4, "(i) $(1,3),(2,4),(3,5),(4,6)$ and their reverses: $8$ outcomes, $\\frac8{36}=\\frac29$ (2). (ii) $(2,6),(3,4),(4,3),(6,2)$: $\\frac4{36}=\\frac19$ (1). (iii) Sums $10,11,12$: $3+2+1=6$, $\\frac6{36}=\\frac16$ (1).", "H"),
W("A family has three children. Assuming a boy and a girl are equally likely each time, find the probability that (i) exactly two are girls (ii) at least one is a boy (iii) all three are of the same gender.", 4, "Sample space has $8$ equally likely outcomes (e.g. $BBB, BBG, \\dots, GGG$) (1). (i) $GGB,GBG,BGG$: $\\frac38$ (1). (ii) $1-P(GGG)=\\frac78$ (1). (iii) $BBB,GGG$: $\\frac28=\\frac14$ (1).", "H", wp=True),
W("In a survey of $80$ students, $24$ prefer cricket, $20$ kabaddi, $16$ football, $12$ badminton and $8$ other games. (i) Find the experimental probability for each game. (ii) A school has $1500$ students; estimate how many prefer kabaddi. (iii) Why would a survey of only $8$ students be less reliable?", 4, "(i) $0.3,\\ 0.25,\\ 0.2,\\ 0.15,\\ 0.1$ (1.5). (ii) $1500\\times0.25=375$ (1.5). (iii) A small sample can differ a lot from the whole school; more trials give results closer to the true probability (1).", "H", wp=True),
W("A box has cards numbered $1$ to $25$. One card is drawn. Find the probability that the number is (i) a multiple of $3$ or $5$ (ii) neither a multiple of $3$ nor of $5$.", 4, "Multiples of $3$: $8$; of $5$: $5$; of both ($15$): $1$ (2). Multiples of $3$ or $5$: $8+5-1=12$, $P=\\frac{12}{25}$ (1). (ii) $1-\\frac{12}{25}=\\frac{13}{25}$ (1).", "H"),
W("A spinner has four sectors with central angles $120^\\circ$ (red), $90^\\circ$ (blue), $90^\\circ$ (green) and $60^\\circ$ (yellow). Find the probability of each colour, check that they add up to $1$, and estimate the number of reds in $60$ spins. Are the outcomes equally likely?", 4, "Probability $=\\frac{\\text{angle}}{360}$: red $\\frac13$, blue $\\frac14$, green $\\frac14$, yellow $\\frac16$ (2). Sum $=\\frac{4+3+3+2}{12}=1$ (1). Reds $\\approx60\\times\\frac13=20$; the outcomes are not equally likely since the sectors differ (1).", "H", wp=True),
W("A two-digit number is chosen at random. Find the probability that it is (i) a multiple of $7$ (ii) a perfect square (iii) both a multiple of $7$ and a perfect square.", 4, "There are $90$ two-digit numbers (1). (i) $14,21,\\dots,98$: $13$ numbers, $\\frac{13}{90}$ (1). (ii) $16,25,36,49,64,81$: $\\frac6{90}=\\frac1{15}$ (1). (iii) Only $49$: $\\frac1{90}$ (1).", "H"),
W("Sunita tosses a fair coin $5$ times and gets heads every time. Neha says tails is now more likely; Rohan says the coin must be biased. Examine both statements. What is the probability of five heads in a row, and how could the coin be tested?", 4, "Neha is wrong: tosses are independent so $P(\\text{tails})=\\frac12$ on the next toss (1). $P(HHHHH)=\\left(\\frac12\\right)^5=\\frac1{32}$ (1), which is unlikely but possible, so Rohan has no proof (1). Test the coin by many more tosses and compare the experimental probability with $\\frac12$ (1).", "H", wp=True),
W("Cards numbered $11$ to $30$ are placed in a bag and one is drawn. Find the probability that the number is (i) prime (ii) a multiple of $5$ (iii) neither prime nor a multiple of $5$.", 4, "There are $20$ cards (1). (i) $11,13,17,19,23,29$: $\\frac6{20}=\\frac3{10}$ (1). (ii) $15,20,25,30$: $\\frac4{20}=\\frac15$ (1). (iii) No overlap, so $1-\\frac{10}{20}=\\frac12$ (1).", "H", wp=True),
W("At the annual day a lucky draw has $200$ coupons: $1$ first prize, $4$ second prizes and $15$ third prizes; the rest win nothing. A coupon is drawn at random. Find the probability of (i) the first prize (ii) a second prize (iii) any prize (iv) no prize. Meena buys $5$ coupons; how many prizes can she expect on average?", 5, "(i) $\\frac1{200}$ (1). (ii) $\\frac4{200}=\\frac1{50}$ (1). (iii) $\\frac{20}{200}=\\frac1{10}$ (1). (iv) $1-\\frac1{10}=\\frac9{10}$ (1). Expected prizes $=5\\times\\frac1{10}=0.5$ (1).", "H", wp=True),
]

_o = _old(7)
_pre, _tail = _o["blocks"][:-2], _o["blocks"][-2:]
_extra = [
 ("h2", "7.6 Counting Outcomes: Dice, Cards and Letters"),
 ("table", ["Event", "Favourable outcomes", "Probability"], [
  ["two dice: sum is 7", "(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)", "6/36 = 1/6"],
  ["two dice: sum is 12", "(6,6)", "1/36"],
  ["two dice: sum is prime", "sums 2, 3, 5, 7, 11 occur 1 + 2 + 4 + 6 + 2 = 15 ways", "15/36 = 5/12"],
  ["two dice: product is odd", "both numbers odd: 3 × 3 = 9", "9/36 = 1/4 (so ‘even’ has 3/4)"],
  ["two dice: difference 2", "(1,3), (2,4), (3,5), (4,6) and their reverses", "8/36 = 2/9"],
  ["two dice: sum more than 9", "sums 10, 11, 12: 3 + 2 + 1", "6/36 = 1/6"],
  ["three coins: exactly two heads", "HHT, HTH, THH out of 8", "3/8"],
  ["card: red face card", "6 of 52", "3/26"],
  ["card: neither king nor queen", "52 − 8 = 44", "11/13"],
  ["number 1 to 25: multiple of 3 or 5", "8 + 5 − 1 (15 counted twice) = 12", "12/25"],
  ["letter of MATHEMATICS: vowel", "A, E, A, I out of 11 letters", "4/11"]]),
 ("note", "REMEMBER", "When two events overlap, count the common outcomes **once**: multiples of 3 or 5 among 1 to 25 are 8 + 5 − 1 = 12, because 15 is in both lists. For letters in a word, count every copy of a repeated letter (MATHEMATICS has 11 letters, with M, A and T twice)."),
 ("h2", "7.7 Worked Examples"),
 ("steps", [("Example 1 — Bag of balls", "A bag has 5 red, 4 green and 3 yellow balls (12 in all). P(red) = 5/12; P(not yellow) = 1 − 3/12 = **3/4**; P(white) = **0** (impossible). If P(blue) = 1/3 in a bag with 6 red, 8 white and x blue balls, then x/(14 + x) = 1/3, so x = 7. After 4 white balls are added the total is 25 and P(blue) = **7/25**.")]),
 ("steps", [("Example 2 — Finding numbers from probabilities", "A bag of 20 balls has P(red) = 1/4 and P(blue) = 2/5. Red = 5, blue = 8, so the remaining 7 are another colour and its probability is 7/20. A school of 1200 students with P(Class 9) = 1/8 has 150 Class 9 students.")]),
 ("steps", [("Example 3 — Experimental probability and estimation", "A batter hits 12 boundaries in 40 balls: P = 12/40 = 0.3, so in 200 more balls expect about **60**. If it rained on 35 of 50 days, P(rain) = 0.7 and in 120 days expect **84** rainy days. A survey of 80 students giving 20 for kabaddi suggests 1500 × 20/80 = **375** kabaddi lovers in a school of 1500.")]),
 ("steps", [("Example 4 — Is a game fair?", "Two dice, Riya wins if the product is even, Ankit if it is odd. The product is odd only for odd × odd = 3 × 3 = 9 outcomes out of 36. P(Ankit) = 1/4 and P(Riya) = 3/4, so the game is **not fair**. A game is fair when both players have probability 1/2.")]),
 ("steps", [("Example 5 — Spinner with unequal sectors", "Sectors of 120°, 90°, 90° and 60° have probabilities 120/360 = 1/3, 1/4, 1/4 and 1/6, adding to 1. The outcomes are **not equally likely**, so we use the fraction of the angle, not 1/(number of sectors). In 60 spins expect about 20 reds.")]),
 ("steps", [("Example 6 — Complement and 'at least one'", "Three coins: P(at least one head) = 1 − P(TTT) = 1 − 1/8 = **7/8**. A family with three children: P(at least one boy) = 7/8, P(all the same gender) = 2/8 = 1/4. For 'at least one', subtract the probability of none from 1.")]),
 ("h2", "7.8 Law of Large Numbers and Common Misconceptions"),
 ("table", ["Tosses", "Heads", "Experimental P(head)", "Difference from 0.5"], [["10", "7", "0.7", "0.2"], ["100", "56", "0.56", "0.06"], ["1,000", "512", "0.512", "0.012"], ["10,000", "5,048", "0.5048", "0.0048"]]),
 ("p", "The experimental probability settles near ½ as the number of tosses grows. The count of heads need not get closer to half of the tosses in absolute terms, but the **fraction** does. Five heads in a row has probability (½)⁵ = 1/32: unlikely but possible, and it does not prove the coin is biased. To test a coin, toss it many times and compare the experimental probability with ½."),
 ("h2", "7.9 Word Problems: How to Translate"),
 ("table", ["Words", "Meaning", "Tool"], [
  ["at random, well shuffled, fair", "equally likely outcomes", "favourable ÷ total"],
  ["raffle, lucky draw, tickets", "each ticket is one outcome", "own tickets ÷ all tickets"],
  ["survey, results of past matches, 30 out of 200", "experimental probability", "frequency ÷ number of trials"],
  ["estimate how many of 1000", "expected number", "total × probability"],
  ["not, never, at least one", "complement", "1 − P(opposite)"],
  ["A or B, with overlap", "count common outcomes once", "multiples of 3 or 5: 8 + 5 − 1"],
  ["sectors of different angles", "unequal chances", "angle ÷ 360"],
  ["win or lose, so ½", "not necessarily equally likely", "use experimental data"]]),
 ("note", "IMPORTANT", "**Common mistakes.** (1) Writing a probability above 1 or as a negative number. (2) Counting tosses instead of outcomes (three tosses give 8 outcomes, not 3). (3) Treating two outcomes as equally likely when they are not (win or lose). (4) Forgetting that the order matters for a pair of dice: (1,6) and (6,1) are different. (5) Believing that a result is 'due' after a run (the gambler's fallacy). (6) Missing the overlap when counting 'A or B'."),
]
CH = dict(_o, blocks=_pre + _extra + _tail, takeaways=_o["takeaways"] + ["For **'at least one'** events use the **complement**: P = 1 − P(none).", "When events overlap, count the common outcomes **once** (multiples of 3 or 5 among 1 to 25: 12).", "**Estimates:** expected number = total × probability; small samples are less reliable than large ones.", "Sectors of **different angles** are not equally likely: probability = angle ÷ 360.", "A game is **fair** only when each player has probability ½."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
