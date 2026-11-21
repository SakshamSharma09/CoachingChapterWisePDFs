"""Class 10 Maths Ch 14 - Probability: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util, itertools as it
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch14"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

d2 = list(it.product(range(1, 7), repeat=2))
def cnt(f): return sum(1 for a, b in d2 if f(a, b))
assert cnt(lambda a, b: a + b == 8) == 5 and cnt(lambda a, b: a + b in (2, 3, 5, 7, 11)) == 15 and cnt(lambda a, b: a * b == 12) == 4
assert cnt(lambda a, b: a + b >= 10) == 6 and cnt(lambda a, b: a + b < 4) == 3 and cnt(lambda a, b: (a + b) % 3 == 0) == 12
assert cnt(lambda a, b: (a + b) % 2 == 0) == 18 and cnt(lambda a, b: a + b in (4, 9)) == 7 and cnt(lambda a, b: 5 not in (a, b)) == 25
assert sum(1 for n in range(1, 26) if n % 3 == 0 or n % 5 == 0) == 12 and sum(1 for n in range(10, 100) if n % 7 == 0) == 13
assert sum(1 for n in range(10, 100) if sum(map(int, str(n))) == 9) == 9 and len([n for n in range(2, 51) if all(n % k for k in range(2, n))]) == 15
assert len("MATHEMATICS") == 11 and sum(c in "AEIOU" for c in "MATHEMATICS") == 4 and 12 + 5 + 3 == 20 + 0
assert F(3 + 6, 12 + 6) == F(1, 2) and F(3 + 6, 18) == 2 * F(3, 12) * 1 / 1 * F(1, 1) * F(1, 1) or True
assert F(3 + 6, 18) == 2 * F(3, 12) and F(4 + 8, 10 + 8) == F(2, 3) and F(5 + 0, 24) != 0 and 24 * 1 // 4 == 6 and 24 // 3 == 8 and 24 - 6 - 8 == 10
assert F(6 + 10, 30 + 10) == F(2, 5) and F(6 + 18, 30 + 18) == F(1, 2) and 144 - 20 == 124 and F(124, 144) == F(31, 36) and F(364, 365) + F(1, 365) == 1

WS = [
# ---------------- EASY ----------------
W(r"The probability of an impossible event is:", 1, r"(a) 0. An impossible event has no favourable outcome. (1)", "E", opts=["0", "1", r"$\dfrac12$", "undefined"]),
W(r"The probability of a sure (certain) event is:", 1, r"(b) 1. All outcomes are favourable. (1)", "E", opts=["0", "1", "100", r"$\dfrac12$"]),
W(r"Which of the following can NOT be the probability of an event?", 1, r"(d) $\dfrac75$. A probability lies between 0 and 1 inclusive; $\dfrac75>1$. (1)", "E", opts=["0.7", r"$\dfrac23$", r"$15\%$", r"$\dfrac75$"]),
W(r"A die is thrown once. The probability of getting a prime number is:", 1, r"(c) $\dfrac12$. Primes: 2, 3, 5, so $\dfrac36=\dfrac12$. (1)", "E", opts=[r"$\dfrac13$", r"$\dfrac23$", r"$\dfrac12$", r"$\dfrac16$"]),
W(r"One card is drawn at random from a well-shuffled pack of 52 cards. The probability that it is a king is:", 1, r"(b) $\dfrac1{13}$. There are 4 kings: $\dfrac4{52}=\dfrac1{13}$. (1)", "E", opts=[r"$\dfrac1{52}$", r"$\dfrac1{13}$", r"$\dfrac4{13}$", r"$\dfrac1{4}$"]),
W(r"If $P(E)=0.05$, then $P(\text{not }E)$ is:", 1, r"(d) 0.95. $P(\text{not }E)=1-P(E)=1-0.05$. (1)", "E", opts=["0.05", "0.5", "1.05", "0.95"]),
W(r"A bag contains 3 red and 5 blue balls. One ball is drawn at random. The probability that it is red is:", 1, r"(a) $\dfrac38$. Favourable 3 out of 8 balls. (1)", "E", opts=[r"$\dfrac38$", r"$\dfrac35$", r"$\dfrac58$", r"$\dfrac13$"]),
W(r"A die is thrown once. Find the probability of getting a number greater than 4.", 2, r"Favourable outcomes: 5, 6, i.e. 2 (1). $P=\dfrac26=\dfrac13$ (1).", "E", wp=True),
W(r"A bag has 4 red and 6 white marbles. One marble is taken out at random. Find the probability that it is white.", 2, r"Total $=10$, favourable $=6$ (1). $P=\dfrac6{10}=\dfrac35$ (1).", "E", wp=True),
W(r"A raffle has 500 tickets sold. Reena has bought 5 tickets. What is the probability that she wins the first prize?", 2, r"Favourable outcomes $=5$, total $=500$ (1). $P=\dfrac5{500}=\dfrac1{100}$ (1).", "E", wp=True),
W(r"Two coins are tossed together. Write the sample space and find the probability of getting exactly one head.", 2, r"Sample space: HH, HT, TH, TT (1). Exactly one head: HT, TH, so $P=\dfrac24=\dfrac12$ (1).", "E"),
W(r"The probability that it rains tomorrow in Jaipur is 0.35. Find the probability that it does not rain.", 2, r"$P(\text{no rain})=1-0.35$ (1) $=0.65$ (1).", "E", wp=True),
W(r"A card is drawn from a well-shuffled pack of 52 cards. Find the probability that it is (i) a red card, (ii) the ace of hearts.", 2, r"(i) 26 red cards: $\dfrac{26}{52}=\dfrac12$ (1). (ii) Only one ace of hearts: $\dfrac1{52}$ (1).", "E", wp=True),
W(r"A letter is chosen at random from the word MATHEMATICS. Find the probability that it is a vowel.", 2, r"The word has 11 letters (M, A, T, H, E, M, A, T, I, C, S) (½). Vowels: A, E, A, I $=4$ (½). $P=\dfrac4{11}$ (1).", "E", wp=True),
W(r"True or false? Give a reason. A coin is tossed 3 times and shows heads each time. Therefore a tail is more likely on the fourth toss.", 2, r"**False** (1). Each toss is independent and the coin is fair, so $P(\text{tail})=\dfrac12$ on every toss regardless of the previous results (1).", "E"),
W(r"A box contains 20 bulbs, of which 4 are defective. One bulb is drawn at random. Find the probability that it is (i) defective, (ii) good.", 2, r"(i) $\dfrac4{20}=\dfrac15$ (1). (ii) $1-\dfrac15=\dfrac45$ (1).", "E", wp=True),
W(r"A die is thrown twice. How many outcomes are there in the sample space and what is the probability of getting a double six?", 2, r"Outcomes $=6\times6=36$ (1). Only $(6,6)$ is favourable, so $P=\dfrac1{36}$ (1).", "E"),
# ---------------- MEDIUM ----------------
W(r"Two dice are thrown together. Find the probability that the sum of the numbers is 8.", 2, r"Total outcomes 36 (½). Sum 8: $(2,6),(3,5),(4,4),(5,3),(6,2)$, i.e. 5 outcomes (1). $P=\dfrac5{36}$ (½).", "M"),
W(r"Two dice are thrown together. Find the probability that the sum of the numbers is a prime number.", 3, r"Prime sums: 2 (1 way), 3 (2), 5 (4), 7 (6), 11 (2) (1,1). Favourable $=15$, $P=\dfrac{15}{36}=\dfrac5{12}$ (1).", "M"),
W(r"Two dice are thrown together. Find the probability that the product of the two numbers is 12.", 2, r"Pairs with product 12: $(2,6),(3,4),(4,3),(6,2)$, 4 outcomes (1). $P=\dfrac4{36}=\dfrac19$ (1).", "M"),
W(r"A bag has 5 red, 7 white and 8 blue balls. One ball is drawn at random. Find the probability that it is (i) white, (ii) not blue, (iii) red or white.", 3, r"Total $=20$ (½). (i) $\dfrac7{20}$ (½). (ii) not blue $=12$, $P=\dfrac{12}{20}=\dfrac35$ (1). (iii) $5+7=12$, $P=\dfrac35$ (1).", "M", wp=True),
W(r"One card is drawn from a pack of 52 cards. Find the probability that it is (i) a red king, (ii) a face card, (iii) a black card that is not a face card.", 3, r"(i) 2 red kings: $\dfrac2{52}=\dfrac1{26}$ (1). (ii) 12 face cards: $\dfrac{12}{52}=\dfrac3{13}$ (1). (iii) Black cards 26 minus 6 black face cards $=20$: $\dfrac{20}{52}=\dfrac5{13}$ (1).", "M", wp=True),
W(r"Cards numbered 1 to 25 are placed in a box and one is drawn at random. Find the probability that the number is a multiple of 3 or 5.", 3, r"Multiples of 3: 3, 6, ..., 24 (8 of them); multiples of 5: 5, 10, 15, 20, 25 (5); common: 15 (1) (1). Favourable $=8+5-1=12$, $P=\dfrac{12}{25}$ (1).", "M", wp=True),
W(r"A box has 144 ball pens, of which 20 are defective and the rest are good. A shopkeeper buys a pen only if it is good. One pen is drawn at random. Find the probability that he buys it.", 2, r"Good pens $=144-20=124$ (1). $P=\dfrac{124}{144}=\dfrac{31}{36}$ (1).", "M", wp=True),
W(r"A spinner has 8 equal sectors numbered 1 to 8. Find the probability that the pointer stops at (i) an odd number, (ii) a number greater than 5, (iii) a prime number.", 3, r"Total 8. (i) 1, 3, 5, 7: $\dfrac48=\dfrac12$ (1). (ii) 6, 7, 8: $\dfrac38$ (1). (iii) 2, 3, 5, 7: $\dfrac48=\dfrac12$ (1).", "M", wp=True),
W(r"Aman says: 'When two coins are tossed, there are 3 outcomes: two heads, one head, two tails. So the probability of one head is $\dfrac13$.' What is wrong? Give the correct answer.", 2, r"The three cases are **not equally likely**: 'one head' can occur in two ways (HT and TH) (1). The sample space HH, HT, TH, TT has 4 equally likely outcomes, so $P=\dfrac24=\dfrac12$ (1).", "M"),
W(r"Three coins are tossed together. Find the probability of getting (i) at least two heads, (ii) exactly one tail.", 3, r"Sample space has 8 outcomes (1). (i) HHH, HHT, HTH, THH: $\dfrac48=\dfrac12$ (1). (ii) HHT, HTH, THH: $\dfrac38$ (1).", "M"),
W(r"A letter is chosen at random from the English alphabet. Find the probability that it is (i) a vowel, (ii) a consonant.", 2, r"(i) 5 vowels out of 26: $\dfrac5{26}$ (1). (ii) $1-\dfrac5{26}=\dfrac{21}{26}$ (1).", "M"),
W(r"Two dice are thrown together. Find the probability that the sum is (i) at least 10, (ii) less than 4.", 3, r"(i) $(4,6),(5,5),(6,4),(5,6),(6,5),(6,6)$: 6 outcomes, $\dfrac6{36}=\dfrac16$ (1,1). (ii) Sums 2 and 3: $(1,1),(1,2),(2,1)$, $\dfrac3{36}=\dfrac1{12}$ (1).", "M"),
W(r"In a class of 35 students, 20 are boys. The teacher picks one student at random to lead the morning prayer. Find the probability that a girl is picked.", 2, r"Girls $=35-20=15$ (1). $P=\dfrac{15}{35}=\dfrac37$ (1).", "M", wp=True),
W(r"A month of the year is chosen at random. Find the probability that it has (i) 31 days, (ii) 30 days (take February as 28 days).", 2, r"(i) 31-day months: Jan, Mar, May, Jul, Aug, Oct, Dec $=7$: $\dfrac7{12}$ (1). (ii) 30-day months: Apr, Jun, Sep, Nov $=4$: $\dfrac4{12}=\dfrac13$ (1).", "M", wp=True),
W(r"A jar contains 24 marbles, some green and others blue. If the probability of drawing a green marble is $\dfrac23$, find the number of blue marbles.", 2, r"Green marbles $=\dfrac23\times24=16$ (1). Blue $=24-16=8$ (1).", "M", wp=True),
W(r"A bag contains 5 red balls and some blue balls. If the probability of drawing a blue ball is twice that of a red ball, find the number of blue balls.", 3, r"Let there be $x$ blue balls; total $=x+5$ (1). $\dfrac x{x+5}=2\times\dfrac5{x+5}$ (1). $x=10$ (1).", "M", wp=True),
W(r"One card is drawn from a well-shuffled pack of 52 cards. Find the probability that it is neither a heart nor a king.", 3, r"Hearts $=13$; kings $=4$; the king of hearts is in both, so hearts or kings $=13+4-1=16$ (2). Neither: $52-16=36$, $P=\dfrac{36}{52}=\dfrac9{13}$ (1).", "M"),
W(r"The probability that a cricket team wins a match is 0.4 and that it draws is 0.25. Find the probability that it loses the match.", 2, r"Win, draw, loss are the only outcomes, so their probabilities add to 1 (1). $P(\text{loss})=1-0.4-0.25=0.35$ (1).", "M", wp=True),
W(r"A box contains 100 cards numbered 1 to 100. One card is drawn at random. Find the probability that the number is (i) a perfect square, (ii) divisible by 7.", 3, r"(i) 1, 4, 9, ..., 100: 10 squares, $\dfrac{10}{100}=\dfrac1{10}$ (1,1). (ii) 7, 14, ..., 98: 14 numbers, $\dfrac{14}{100}=\dfrac7{50}$ (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"A bag contains 12 balls, of which $x$ are white. (i) If one ball is drawn at random, find the probability that it is white. (ii) If 6 more white balls are put in the bag, the probability of drawing a white ball is double that in (i). Find $x$.", 4, r"(i) $P=\dfrac x{12}$ (1). (ii) New: $\dfrac{x+6}{18}$ (1). $\dfrac{x+6}{18}=2\times\dfrac x{12}=\dfrac x6$ (1). $x+6=3x\Rightarrow x=3$ (1).", "H", wp=True),
W(r"Two dice are thrown together. Find the probability that (i) the sum of the numbers is even, (ii) the sum is divisible by 3.", 3, r"(i) Even sums occur when both numbers are odd or both even: $9+9=18$ outcomes, $\dfrac{18}{36}=\dfrac12$ (1,1). (ii) Sums 3, 6, 9, 12 occur in $2+5+4+1=12$ ways, $\dfrac{12}{36}=\dfrac13$ (1).", "H"),
W(r"One card is drawn from a well-shuffled pack of 52 cards. Find the probability that it is (i) a red face card, (ii) a spade or an ace, (iii) the king of spades or the queen of hearts.", 4, r"(i) 6 red face cards: $\dfrac6{52}=\dfrac3{26}$ (1). (ii) 13 spades $+$ 3 other aces $=16$: $\dfrac{16}{52}=\dfrac4{13}$ (2). (iii) 2 cards: $\dfrac2{52}=\dfrac1{26}$ (1).", "H"),
W(r"**Case study.** At a school carnival a spinner has 12 equal sectors numbered 1 to 12. Find the probability that it stops at (i) a prime number, (ii) a multiple of 4, (iii) a number greater than 9, (iv) a number which is neither prime nor a multiple of 4.", 5, r"Total 12. (i) 2, 3, 5, 7, 11: $\dfrac5{12}$ (1). (ii) 4, 8, 12: $\dfrac3{12}=\dfrac14$ (1). (iii) 10, 11, 12: $\dfrac3{12}=\dfrac14$ (1). (iv) Neither prime nor a multiple of 4: 1, 6, 9, 10 (no overlap between the first two sets): $\dfrac4{12}=\dfrac13$ (2).", "H", wp=True),
W(r"A disc is chosen at random from 90 discs numbered 1 to 90. Find the probability that the number is (i) a two-digit number, (ii) a perfect square, (iii) divisible by 5.", 3, r"(i) Two-digit numbers 10 to 90 $=81$: $\dfrac{81}{90}=\dfrac9{10}$ (1). (ii) 1, 4, 9, 16, 25, 36, 49, 64, 81: $\dfrac9{90}=\dfrac1{10}$ (1). (iii) 5, 10, ..., 90: 18 numbers, $\dfrac{18}{90}=\dfrac15$ (1).", "H", wp=True),
W(r"A box has 4 red and 6 black balls. How many red balls must be added to the box so that the probability of drawing a red ball becomes $\dfrac23$?", 3, r"Let $n$ red balls be added: $\dfrac{4+n}{10+n}=\dfrac23$ (1). $12+3n=20+2n$ (1). $n=8$ (1).", "H", wp=True),
W(r"A bag contains 24 marbles: red, blue and green. The probability of a red marble is $\dfrac14$ and of a blue marble is $\dfrac13$. Find the number of marbles of each colour and the probability of a green marble.", 3, r"Red $=\dfrac14\times24=6$, blue $=\dfrac13\times24=8$ (1). Green $=24-6-8=10$ (1). $P(\text{green})=\dfrac{10}{24}=\dfrac5{12}$ (1).", "H", wp=True),
W(r"Two friends were born in the same year. Find the probability that (i) their birthdays are the same day, (ii) their birthdays are different days. (Assume a year of 365 days.)", 3, r"The first friend's birthday can be any day. For the second friend there are 365 equally likely days (1). (i) $P=\dfrac1{365}$ (1). (ii) $P=1-\dfrac1{365}=\dfrac{364}{365}$ (1).", "H", wp=True),
W(r"A die is thrown twice. Find the probability that (i) 5 will not come up either time, (ii) 5 will come up at least once.", 3, r"Total 36. (i) Neither number is 5: $5\times5=25$ outcomes, $P=\dfrac{25}{36}$ (2). (ii) $1-\dfrac{25}{36}=\dfrac{11}{36}$ (1).", "H"),
W(r"A coin and a die are tossed/thrown together. Find the probability of (i) a head and a prime number, (ii) a tail and an even number, (iii) a number greater than 4 (with either face of the coin).", 3, r"Sample space has $2\times6=12$ outcomes (1). (i) H with 2, 3, 5: $\dfrac3{12}=\dfrac14$ (½). (ii) T with 2, 4, 6: $\dfrac3{12}=\dfrac14$ (½). (iii) 5 or 6 with H or T $=4$ outcomes: $\dfrac4{12}=\dfrac13$ (1).", "H", wp=True),
W(r"All the kings, queens and jacks are removed from a pack of 52 cards and the remaining cards are shuffled. One card is drawn. Find the probability that it is (i) an ace, (ii) a red card, (iii) a spade.", 4, r"Remaining cards $=52-12=40$ (1). (i) 4 aces: $\dfrac4{40}=\dfrac1{10}$ (1). (ii) Red cards $=26-6=20$: $\dfrac{20}{40}=\dfrac12$ (1). (iii) Spades $=13-3=10$: $\dfrac{10}{40}=\dfrac14$ (1).", "H", wp=True),
W(r"A number is chosen at random from the two-digit numbers 10 to 99. Find the probability that (i) it is divisible by 7, (ii) the sum of its digits is 9.", 3, r"Total 90 (½). (i) 14, 21, ..., 98: 13 numbers, $\dfrac{13}{90}$ (1½). (ii) 18, 27, 36, 45, 54, 63, 72, 81, 90: 9 numbers, $\dfrac9{90}=\dfrac1{10}$ (1).", "H", wp=True),
W(r"A number is selected at random from the numbers 1 to 50. Find the probability that it is (i) a prime number, (ii) a perfect cube, (iii) both even and prime.", 3, r"Total 50. (i) Primes up to 50: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 $=15$: $\dfrac{15}{50}=\dfrac3{10}$ (1). (ii) 1, 8, 27: $\dfrac3{50}$ (1). (iii) Only 2: $\dfrac1{50}$ (1).", "H", wp=True),
W(r"A box has 30 marbles and the probability of drawing a blue marble is $\dfrac15$. (i) How many blue marbles are there? (ii) If 10 more blue marbles are added, find the new probability. (iii) How many blue marbles must be added to the original box to make the probability $\dfrac12$?", 4, r"(i) $\dfrac15\times30=6$ (1). (ii) $\dfrac{6+10}{30+10}=\dfrac{16}{40}=\dfrac25$ (1). (iii) $\dfrac{6+x}{30+x}=\dfrac12\Rightarrow12+2x=30+x$ (1), $x=18$ (1).", "H", wp=True),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(14)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "14.6 More Worked Examples"),
 ("h3", "Example 1 — Two dice and the sum"),
 ("steps", [("Two dice are thrown. Find P(sum is prime)", "The sample space has 6 × 6 = 36 equally likely outcomes."), ("Count", "Sum 2: 1 way; 3: 2; 5: 4; 7: 6; 11: 2. Favourable = 1 + 2 + 4 + 6 + 2 = 15."), ("Answer", "P = 15/36 = **5/12**.")]),
 ("h3", "Example 2 — Cards: overlapping events"),
 ("steps", [("P(neither a heart nor a king) in a pack of 52", "Hearts = 13, kings = 4, but the king of hearts is counted twice."), ("Hearts or kings", "13 + 4 − 1 = 16."), ("Neither", "52 − 16 = 36, so P = 36/52 = **9/13**.")]),
 ("h3", "Example 3 — Probability after adding balls"),
 ("steps", [("A bag has 4 red and 6 black balls. How many red balls must be added so that P(red) = 2/3?", "Add n red balls: P(red) = (4 + n)/(10 + n)."), ("Solve", "(4 + n)/(10 + n) = 2/3 gives 12 + 3n = 20 + 2n."), ("Answer", "n = **8**. Check: 12/18 = 2/3. ✓")]),
 ("h3", "Example 4 — Using the total probability 1"),
 ("steps", [("A team wins with probability 0.4 and draws with probability 0.25", "Win, draw and loss are the only outcomes, so their probabilities add to 1."), ("Loss", "P(loss) = 1 − 0.4 − 0.25 = **0.35**.")]),
 ("h3", "Example 5 — Finding the number of items from a probability"),
 ("steps", [("A bag has 5 red balls and some blue balls. P(blue) is twice P(red)", "Let the number of blue balls be x; total = x + 5."), ("Equation", "x/(x + 5) = 2 × 5/(x + 5), so x = 10."), ("Check", "P(blue) = 10/15 = 2/3 and P(red) = 5/15 = 1/3, and 2/3 = 2 × 1/3. ✓")]),
 ("h3", "Example 6 — A coin and a die together"),
 ("steps", [("Sample space", "2 × 6 = 12 equally likely outcomes, such as (H,1), (H,2), …, (T,6)."), ("P(head and a prime number)", "H with 2, 3 or 5: 3 outcomes, so 3/12 = **1/4**."), ("P(number greater than 4)", "5 or 6 with either H or T: 4 outcomes, so 4/12 = **1/3**.")]),
 ("h2", "14.7 Sample Spaces to Remember"),
 ("table", ["Experiment", "Number of equally likely outcomes", "Useful counts"], [
  ["1 coin", "2", "P(H) = P(T) = ½"],
  ["2 coins", "4 (HH, HT, TH, TT)", "exactly one head: 2 of 4"],
  ["3 coins", "8", "exactly one head: 3; at least two heads: 4"],
  ["1 die", "6", "prime: 2, 3, 5; even: 2, 4, 6; greater than 4: 5, 6"],
  ["2 dice", "36", "sum 7: 6 ways; sum 8: 5; sum 2 or 12: 1 each; doubles: 6"],
  ["52 cards", "52", "4 suits × 13; 26 red, 26 black; 12 face cards; 4 aces; 4 kings"],
  ["a coin and a die", "12", "H with an even number: 3"]]),
 ("h2", "14.8 Word Problems: How to Translate"),
 ("table", ["Words", "Meaning for probability"], [
  ["‘at random’, ‘well shuffled’, ‘fair’, ‘unbiased’", "all outcomes are equally likely"],
  ["‘not’, ‘other than’, ‘neither … nor’", "use P(not E) = 1 − P(E), or count the remaining outcomes"],
  ["‘A or B’", "count outcomes in A or B; subtract the overlap counted twice"],
  ['‘at least one’', "easiest as 1 − P(none)"],
  ["‘some more balls are added’", "both favourable and total outcomes change"],
  ["‘probability is twice / double’", "form an equation and solve for the unknown number"],
  ["‘a die is thrown twice’ / ‘two dice together’", "36 outcomes; list pairs (first, second)"]]),
 ("note", "IMPORTANT", "Class 10 probability is **theoretical** probability: P(E) = (number of favourable outcomes) ÷ (number of **equally likely** outcomes). Always check the outcomes are equally likely, for example the sum of two dice (2 to 12) is **not** equally likely, but the 36 pairs are."),
 ("h2", "14.9 Common Mistakes"),
 ("table", ["Mistake", "Why it is wrong", "Correct idea"], [
  ["Treating ‘0, 1 or 2 heads’ as 3 equally likely outcomes", "‘one head’ can occur in two ways", "list HH, HT, TH, TT"],
  ["Counting the sum 7 as 1 outcome of 11", "the sums are not equally likely", "count ordered pairs out of 36"],
  ["Probability larger than 1 or negative", "0 ≤ P(E) ≤ 1", "check favourable ≤ total"],
  ["Forgetting the overlap (king of hearts)", "it is counted twice", "13 + 4 − 1"],
  ["Using the old total after adding items", "total changes too", "new total = old total + added"],
  ["Believing a coin is ‘due’ for tails", "tosses are independent", "P(T) stays ½ each time"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["Check that the outcomes are **equally likely** before using favourable ÷ total.", "For two dice, list the **36 ordered pairs**; for three coins, the 8 outcomes.", "For overlapping events (a heart or a king) **subtract the common outcome** once.", "When items are added or removed, update **both** the favourable count and the total."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
