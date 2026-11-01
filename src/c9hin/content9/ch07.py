from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def fr(f):
    f = F(f)
    return f"{f.numerator}" if f.denominator == 1 else f"\\frac{{{f.numerator}}}{{{f.denominator}}}"
def wrongs(p, extra=()):
    n, k = p.denominator, p.numerator
    out = []
    for a, b in [(n-k, n), (k, n+1), (k+1, n), (k-1, n), (k, n-1), (1, n), (k, 2*n), (k+1, n+1), (2*k, n+2), (n-k, n+1)]:
        if b <= 0 or a <= 0: continue
        v = F(a, b)
        if v != p and 0 < v < 1 and v not in out: out.append(v)
    return out
def pm(stem, p, why):
    p = F(p)
    w = wrongs(p)
    assert len(w) >= 3, (stem, p, w)
    return M4(stem, f"${fr(p)}$", [f"${fr(x)}$" for x in w[:3]], why)
A = []; B = []; C = []; D = []
# die (8)
for stem, k, why in [("a prime number", 3, "2, 3, 5"), ("a number greater than 4", 2, "5, 6"), ("an even number", 3, "2, 4, 6"), ("a multiple of 3", 2, "3, 6"),
                     ("a number less than 3", 2, "1, 2"), ("a number other than 6", 5, "1,2,3,4,5"), ("a factor of 12", 5, "1, 2, 3, 4, 6"), ("an odd prime number", 2, "3, 5")]:
    A.append(pm(f"A fair die is rolled once. The probability of getting {stem} is:", F(k, 6), f"favourable outcomes: {why} ⇒ {k} out of 6"))
# bag (8)
for (r, b, g), col, k in [((5, 3, 2), "blue", 3), ((4, 6, 2), "red", 4), ((7, 5, 8), "green", 8), ((3, 9, 3), "blue", 9), ((6, 4, 5), "red", 6), ((2, 8, 5), "green", 5), ((10, 6, 4), "blue", 6), ((9, 3, 3), "red", 9)]:
    n = r+b+g
    A.append(pm(f"A bag contains {r} red, {b} blue and {g} green balls. One ball is drawn at random. The probability that it is {col} is:", F(k, n), f"{k} favourable out of {n} equally likely balls"))
# letters (5)
for word, what, k in [("PROBABILITY", "the letter B", 2), ("PROBABILITY", "a vowel", 4), ("MATHEMATICS", "the letter M", 2), ("MATHEMATICS", "the letter A", 2), ("MATHEMATICS", "a vowel", 4)]:
    n = len(word)
    A.append(pm(f"A letter is picked at random from the word ‘{word}’. The probability of picking {what} is:", F(k, n), f"{k} favourable out of {n} letters"))
# relative frequency (5)
for n, k in [(50, 8), (200, 46), (40, 6), (25, 10), (80, 28)]:
    v = F(k, n); s = f"{float(v):g}"
    w = [x for x in dict.fromkeys([f"{float(F(n, k)):.2f}".rstrip('0').rstrip('.'), f"{float(v)+0.1:g}", f"{float(v)/2:g}", f"{float(1-v):g}"]) if x != s]
    A.append(M4(f"An event occurred {k} times in {n} trials. Its experimental probability (relative frequency) is:", s, w[:3], f"${k}/{n}={s}$"))
# sample space (3)
for stem, n in [("two coins are tossed together", 4), ("a coin is tossed and a die is rolled", 12), ("two dice are rolled together", 36)]:
    A.append(M4(f"The number of outcomes in the sample space when {stem} is:", str(n), [str(x) for x in (n//2, n+2, n*2) if x != n][:3], "multiply the number of outcomes of each experiment"))
# population estimate (3)
for p, N, ans in [(F(2, 5), 1500, 600), (F(3, 10), 2000, 600), (F(3, 20), 800, 120)]:
    A.append(M4(f"A sample shows a probability of ${fr(p)}$ that a student likes cricket. In a school of {N} students the expected number who like cricket is:", str(ans), [str(ans+100), str(ans//2), str(ans+N//10)], "expected number $=P\\times$ population"))
A += [
 M4("The probability of any event always lies between:", "0 and 1 (both included)", ["−1 and 1", "0 and 100", "1 and 2"], "probability scale 0 to 1"),
 M4("The probability of an impossible event is:", "0", ["1", "0.5", "−1"], "can never happen"),
 M4("The probability of a certain event is:", "1", ["0", "0.5", "100"], "always happens"),
 M4(r"If $P(E)=0.35$, then the probability that $E$ does not happen is:", "0.65", ["0.35", "0.55", "1.35"], "$1-0.35$"),
 M4("A fair coin has landed heads six times in a row. The probability of tails on the next toss is:", r"$\frac12$", [r"$\frac13$", r"$\frac{1}{64}$", r"$\frac34$"], "tosses are independent — the coin has no memory"),
 M4("Believing that tails is ‘due’ after many heads is called:", "the Gambler's Fallacy", ["the Law of Large Numbers", "relative frequency", "sampling"], "past outcomes do not affect the next fair toss"),
 M4("As the number of trials increases, the experimental probability tends to get closer to the:", "theoretical probability", ["number of trials", "sample space size", "value 1"], "Law of Large Numbers"),
 M4("The game of Snakes and Ladders originated in ancient India from a game called:", "Jñān-Chaupaḍ", ["Pachisi only", "Shatranj", "Mancala"], "as given in the chapter"),
]
assert len(A) == 8+8+5+5+3+3+8 == 40, len(A)
# B (16)
B += [
 Q(r"Write the sample space when two coins are tossed together and find the probability of exactly one head.", r"Sample space $\{HH,HT,TH,TT\}$; favourable: $HT,TH$ ⇒ $P=\frac24=\frac12$.", "1+1"),
 Q(r"A fair die is rolled. Find the probability of getting a prime number.", r"Primes: 2, 3, 5 ⇒ $\frac36=\frac12$.", "1+1"),
 Q(r"A bag has 4 red and 6 blue balls. A ball is drawn at random. What is the probability that it is not red?", r"Not red = blue: $\frac6{10}=\frac35$.", "1+1"),
 Q(r"A die is rolled 50 times and shows a 4 eight times. Find the experimental probability of a 4 and compare it with the theoretical probability.", r"Experimental $=\frac8{50}=0.16$; theoretical $=\frac16\approx0.167$. They are close.", "1+1"),
 Q(r"In a survey of 50 students, 10 like bananas. Find the probability that a randomly chosen student likes bananas, and the expected number among 1500 students.", r"$P=\frac{10}{50}=0.2$ (1). Expected $=0.2\times1500=300$ (1).", "1+1"),
 Q(r"A letter is picked at random from ‘PROBABILITY’. Find the probability of (i) the letter B (ii) a vowel.", r"11 letters. (i) B occurs twice ⇒ $\frac2{11}$. (ii) Vowels O, A, I, I ⇒ $\frac4{11}$.", "1+1"),
 Q(r"A fair coin shows heads six times in a row. A friend says tails is sure on the next toss. Is she right? Why?", r"No. Each toss is independent; the coin has no memory, so $P(\text{tails})$ is still $\frac12$. This mistaken belief is the Gambler's Fallacy.", "1+1"),
 Q(r"Label as impossible, less likely, even chance, more likely or certain: (i) Monday follows Sunday. (ii) It snows in Mumbai in July.", r"(i) Certain (probability 1). (ii) Impossible (probability 0, or essentially so).", "1+1"),
 Q(r"If the probability that a team wins is $0.35$, what is the probability that it does not win? Why?", r"$1-0.35=0.65$, since the win and not-win events together are certain (probability 1).", "1+1"),
 Q(r"A card is drawn from a well-shuffled pack of 52 cards. Find the probability that it is (i) a king (ii) a red king.", r"(i) $\frac4{52}=\frac1{13}$. (ii) $\frac2{52}=\frac1{26}$.", "1+1"),
 Q(r"A box has 20 bulbs of which 3 are defective. One bulb is picked at random. Find the probability that it is (i) defective (ii) not defective.", r"(i) $\frac3{20}$. (ii) $\frac{17}{20}$.", "1+1"),
 Q(r"Two dice are rolled together. Find the probability that the sum is 7.", r"36 equally likely outcomes; sum 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) ⇒ $\frac6{36}=\frac16$.", "1+1"),
 Q(r"A spinner has 8 equal sectors numbered 1 to 8. Find the probability that it stops on a multiple of 3.", r"Multiples of 3: 3, 6 ⇒ $\frac28=\frac14$.", "1+1"),
 Q(r"Why is tossing a coin considered a fair way to decide which team bats first?", r"Both outcomes are equally likely ($\frac12$ each) and no one can predict the result beforehand, so neither team has an advantage.", "2"),
 Q(r"A coin is tossed 200 times and shows heads 112 times. Find the relative frequency of heads and compare it with $\frac12$.", r"$\frac{112}{200}=0.56$. The theoretical value is $0.5$; with more tosses the experimental value tends to get closer.", "1+1"),
 Q(r"One month of the year is chosen at random. What is the probability that it has 31 days?", r"7 months (Jan, Mar, May, Jul, Aug, Oct, Dec) out of 12: $\frac7{12}$.", "1+1"),
]
assert len(B) == 16, len(B)
# C (24)
C += [
 Q(r"Three coins are tossed together. Write the sample space and find the probability of at least two heads.", r"$\{HHH,HHT,HTH,THH,HTT,THT,TTH,TTT\}$ (1). At least two heads: HHH, HHT, HTH, THH — 4 outcomes (1). $P=\frac48=\frac12$ (1).", "1+1+1"),
 Q(r"Two dice are rolled. Find the probability that (i) the sum is 8 (ii) the sum is at least 10.", r"36 outcomes (1). (i) (2,6),(3,5),(4,4),(5,3),(6,2) ⇒ $\frac5{36}$ (1). (ii) (4,6),(5,5),(5,6),(6,4),(6,5),(6,6) ⇒ $\frac6{36}=\frac16$ (1).", "1+1+1"),
 Q(r"A card is drawn from a pack of 52. Find the probability of (i) an ace (ii) a heart (iii) a face card (J, Q, K).", r"(i) $\frac4{52}=\frac1{13}$ (ii) $\frac{13}{52}=\frac14$ (iii) $\frac{12}{52}=\frac3{13}$.", "1+1+1"),
 Q(r"A bag contains 5 red, 3 blue and 2 green balls. Find the probability of drawing (i) a red ball (ii) a ball that is not green (iii) a yellow ball.", r"10 balls. (i) $\frac5{10}=\frac12$ (ii) $\frac8{10}=\frac45$ (iii) $0$ — impossible event.", "1+1+1"),
 Q(r"The probability that a randomly chosen bulb from a batch is defective is $0.04$. How many defective bulbs are expected in 1500 bulbs?", r"$0.04\times1500=60$ bulbs (the estimate becomes better with a larger sample).", "2+1"),
 Q(r"A die was rolled 120 times: 1→18, 2→22, 3→19, 4→21, 5→24, 6→16. Find the experimental probability of (i) getting 5 (ii) getting an even number, and compare (i) with $\frac16$.", r"(i) $\frac{24}{120}=0.2$ (1). (ii) $\frac{22+21+16}{120}=\frac{59}{120}\approx0.49$ (1). Theoretical for 5 is $\frac16\approx0.167$; close but not equal (1).", "1+1+1"),
 Q(r"In a sample of 100 students, 35 like cricket. Estimate how many of 1200 students like cricket, and explain why a larger, more varied sample gives a better estimate.", r"$P=0.35$; expected $=0.35\times1200=420$ (2). A larger sample drawn from different classes represents the whole population better (1).", "2+1"),
 Q(r"In Snakes and Ladders a player has rolled three 6s in a row and says a 6 cannot come again. Find the probability of a 6 on the next roll and comment.", r"$\frac16$ (1). Rolls are independent, so earlier results do not change it; the belief is the Gambler's Fallacy (2).", "1+2"),
 Q(r"If $P(E)=\frac5{12}$, find $P(\text{not }E)$ and show that $P(E)+P(\text{not }E)=1$.", r"$P(\text{not }E)=1-\frac5{12}=\frac7{12}$ (2). Sum $=\frac5{12}+\frac7{12}=1$ ✓ (1).", "2+1"),
 Q(r"A letter is chosen at random from ‘MATHEMATICS’. Find the probability of (i) M (ii) T (iii) a vowel.", r"11 letters. (i) $\frac2{11}$ (ii) $\frac2{11}$ (iii) vowels A, E, A, I ⇒ $\frac4{11}$.", "1+1+1"),
 Q(r"In a raffle 500 tickets are sold. Riya buys 5 tickets and one ticket wins the prize. What is the probability that Riya wins?", r"$\frac5{500}=\frac1{100}=0.01$.", "2+1"),
 Q(r"Two dice are rolled. Find the probability that (i) both show the same number (ii) the sum is a prime number.", r"(i) 6 doubles ⇒ $\frac6{36}=\frac16$ (1). (ii) Primes 2,3,5,7,11 occur in $1+2+4+6+2=15$ ways ⇒ $\frac{15}{36}=\frac5{12}$ (2).", "1+2"),
 Q(r"A bag of 12 balls has red ones with $P(\text{red})=\frac13$. (i) How many red balls? (ii) If 2 more red balls are added, find the new $P(\text{red})$.", r"(i) $\frac13\times12=4$ (1). (ii) $\frac{6}{14}=\frac37$ (2).", "1+2"),
 Q(r"Distinguish between subjective and objective (experimental/theoretical) probability using the example ‘it will rain today’.", r"Subjective: a person's own opinion from what they see (‘sunny, so unlikely’), differing between people (1). Objective: based on evidence such as past rainfall data (relative frequency) or on equally likely outcomes (theoretical) (2).", "1+2"),
 Q(r"A spinner has 8 equal sectors numbered 1 to 8. Find the probability that it stops on (i) a prime (ii) a number greater than 5.", r"(i) 2, 3, 5, 7 ⇒ $\frac48=\frac12$ (ii) 6, 7, 8 ⇒ $\frac38$.", "1+1+1"),
 Q(r"A number is chosen at random from 1 to 25. Find the probability that it is (i) a multiple of 5 (ii) a prime number.", r"(i) 5, 10, 15, 20, 25 ⇒ $\frac5{25}=\frac15$ (ii) 2,3,5,7,11,13,17,19,23 ⇒ $\frac9{25}$.", "1+2"),
 Q(r"A basketball player scored 18 times in 30 attempts. Find the experimental probability of scoring and estimate the number of scores in 50 attempts.", r"$\frac{18}{30}=0.6$ (1+1). Expected $=0.6\times50=30$ (1).", "2+1"),
 Q(r"Explain what happens to experimental probability as the number of trials increases, using the Law of Large Numbers.", r"For few trials the relative frequency can differ much from the theoretical value, but as the number of trials grows it tends to get closer to the theoretical probability (e.g. tosses of a fair coin approach 0.5).", "3"),
 Q(r"A card is drawn from a pack of 52. Find the probability of (i) a black queen (ii) the ace of spades (iii) a number card from 2 to 10.", r"(i) $\frac2{52}=\frac1{26}$ (ii) $\frac1{52}$ (iii) $\frac{36}{52}=\frac9{13}$.", "1+1+1"),
 Q(r"A class of 40 has 24 girls. One student is chosen at random. Find the probability that the student is (i) a girl (ii) a boy.", r"(i) $\frac{24}{40}=\frac35$ (ii) $\frac{16}{40}=\frac25$ (and $\frac35+\frac25=1$).", "1+1+1"),
 Q(r"A die is rolled once. Find the probability that the number is both even and prime, and the probability that it is neither.", r"Only 2 is both even and prime ⇒ $\frac16$ (1). The numbers that are even or prime are 2, 3, 4, 5, 6, so only 1 is neither ⇒ $\frac16$ (2).", "1+2"),
 Q(r"A day of the week is chosen at random. What is the probability that it is a weekend day? Is a random pick of ‘a day starting with T’ more or less likely?", r"Weekend (Sat, Sun) ⇒ $\frac27$ (1). Days beginning with T: Tuesday, Thursday ⇒ $\frac27$ — equally likely (2).", "1+2"),
 Q(r"A coin was tossed 1000 times with 520 heads. Find the relative frequency of heads and the difference from the theoretical probability.", r"$\frac{520}{1000}=0.52$ (1+1). Difference from $0.5$ is $0.02$ (1) — small because the number of trials is large.", "2+1"),
 Q(r"One month is chosen at random. Find the probability that it has exactly 30 days.", r"April, June, September, November ⇒ $\frac4{12}=\frac13$ (3).", "3"),
]
assert len(C) == 24, len(C)
# D (16)
D += [
 Q(r"<b>Case study:</b> A survey of 50 students about favourite fruit gives: mango 20, apple 15, banana 10, grapes 5. (i) Find the probability that a randomly chosen student likes mango. (ii) Find the probability for each of the other fruits and check that all four add to 1. (iii) For a school of 1500 students, estimate the number of mangoes and bananas needed. (iv) How would a better estimate be obtained?", r"(i) $\frac{20}{50}=0.4$ (1). (ii) apple $0.3$, banana $0.2$, grapes $0.1$; sum $=0.4+0.3+0.2+0.1=1$ ✓ (2). (iii) mango $0.4\times1500=600$; banana $0.2\times1500=300$ (1). (iv) Use a larger sample from different classes and grades (1).", "1+2+1+1"),
 Q(r"<b>Case study:</b> Two dice are rolled together. (i) Write how many outcomes the sample space has. (ii) Find the probability of a sum of 7. (iii) Find the probability of a double. (iv) Find the probability that the sum is less than 5.", r"(i) $6\times6=36$ (1). (ii) $\frac6{36}=\frac16$ (1). (iii) $\frac6{36}=\frac16$ (1). (iv) (1,1),(1,2),(2,1),(1,3),(3,1),(2,2) ⇒ $\frac6{36}=\frac16$ (2).", "1+1+1+2"),
 Q(r"<b>Case study:</b> A well-shuffled pack of 52 cards is used. Find the probability of drawing (i) a king (ii) a red card (iii) a face card (iv) neither a heart nor a diamond (v) the queen of hearts.", r"(i) $\frac1{13}$ (ii) $\frac12$ (iii) $\frac3{13}$ (iv) $\frac{26}{52}=\frac12$ (v) $\frac1{52}$ (1 mark each).", "1+1+1+1+1"),
 Q(r"<b>Case study:</b> A bag has 5 red, 3 blue and 2 green marbles. (i) Find $P(\text{red})$, $P(\text{blue})$, $P(\text{green})$ and show they add to 1. (ii) Find the probability that the marble is not blue. (iii) 5 more green marbles are added; find the new $P(\text{green})$.", r"(i) $\frac5{10},\frac3{10},\frac2{10}$; sum $=1$ (2). (ii) $1-\frac3{10}=\frac7{10}$ (1). (iii) 15 marbles, 7 green ⇒ $\frac7{15}$ (2).", "2+1+2"),
 Q(r"<b>Case study:</b> A die was rolled 120 times: 1→18, 2→22, 3→19, 4→21, 5→24, 6→16. (i) Find the experimental probability of each face. (ii) Find the probability of an odd number. (iii) Compare with the theoretical value $\frac16$ for each face. (iv) What would you expect if the die were rolled 6000 times?", r"(i) 0.15, 0.183, 0.158, 0.175, 0.2, 0.133 (2). (ii) $\frac{18+19+24}{120}=\frac{61}{120}\approx0.51$ (1). (iii) All lie near 0.167 but differ (1). (iv) Each face would be near $\frac16$, so about 1000 times (1).", "2+1+1+1"),
 Q(r"(i) What is the Gambler's Fallacy? (ii) A coin shows heads 6 times in a row. What is $P(\text{tails})$ on the 7th toss? (iii) In Snakes and Ladders a player rolls three 6s in a row. What is $P(6)$ next? (iv) Explain why the answers are not affected by earlier results.", r"(i) The mistaken belief that past random outcomes change the chances of the next one (1). (ii) $\frac12$ (1). (iii) $\frac16$ (1). (iv) Each toss or roll is an independent event; the coin and die have no memory (2).", "1+1+1+2"),
 Q(r"Rank the following on the probability scale 0 to 1 and label each: (i) The next Monday comes after Sunday. (ii) It snows in Mumbai in July. (iii) You roll a 3 on a fair die. (iv) A fair coin shows heads. (v) A bag has only red sweets and you draw a red one.", r"(i) Certain (1). (ii) Impossible (0). (iii) Less likely ($\frac16$). (iv) Even chance ($\frac12$). (v) Certain (1). (1 mark each)", "1+1+1+1+1"),
 Q(r"<b>Case study:</b> A letter is picked at random from ‘PROBABILITY’. (i) How many letters are there? (ii) Find $P(\text{B})$. (iii) Find $P(\text{I})$. (iv) Find the probability of a vowel and of a consonant, and show they add to 1.", r"(i) 11 (1). (ii) $\frac2{11}$ (1). (iii) $\frac2{11}$ (1). (iv) Vowels O, A, I, I ⇒ $\frac4{11}$; consonants $\frac7{11}$; sum $=1$ (2).", "1+1+1+2"),
 Q(r"Three coins are tossed together. (i) List the sample space. (ii) Find the probability of exactly two heads. (iii) Find the probability of at least one head. (iv) Find the probability that all three coins show the same face.", r"(i) HHH, HHT, HTH, THH, HTT, THT, TTH, TTT (2). (ii) 3 outcomes ⇒ $\frac38$ (1). (iii) $1-\frac18=\frac78$ (1). (iv) HHH, TTT ⇒ $\frac28=\frac14$ (1).", "2+1+1+1"),
 Q(r"<b>Case study:</b> In a factory, 8 of a sample of 200 bulbs are defective. (i) Find the probability that a bulb is defective. (ii) Estimate the number of defective bulbs in a batch of 5000. (iii) Find the probability that a bulb is good. (iv) Why would a bigger sample give a more reliable estimate?", r"(i) $\frac8{200}=0.04$ (1). (ii) $0.04\times5000=200$ (1). (iii) $0.96$ (1). (iv) A bigger, representative sample varies less from the true proportion (2).", "1+1+1+2"),
 Q(r"(i) Explain subjective probability with an example. (ii) Explain how an objective estimate of the chance of rain can be made from data. (iii) Why is rain called a random event?", r"(i) A personal judgement, e.g. ‘it is sunny so I think rain is unlikely’; different people may differ (2). (ii) Count the days with rain in past years and compute the relative frequency (2). (iii) Rain depends on many sensitive atmospheric factors, so the outcome cannot be predicted with certainty (1).", "2+2+1"),
 Q(r"<b>Case study:</b> Two players A and B play with a spinner of 8 equal sectors numbered 1–8. A wins if the number is prime; B wins if the number is a composite number. (i) Find $P(A\text{ wins})$. (ii) Find $P(B\text{ wins})$. (iii) Is the game fair? (iv) Which number(s) make neither win?", r"(i) Primes 2,3,5,7 ⇒ $\frac48=\frac12$ (1). (ii) Composites 4,6,8 ⇒ $\frac38$ (1). (iii) Not fair, $\frac12\ne\frac38$ (1). (iv) 1 (neither prime nor composite), probability $\frac18$ (2).", "1+1+1+2"),
 Q(r"<b>Case study:</b> A school raffle sells 1000 tickets and awards 5 prizes. Anil buys 10 tickets. (i) Find the probability that one particular ticket wins a prize. (ii) Find the probability that Anil's ticket set contains a winning ticket (assume at most one of his tickets can win). (iii) Find the probability that a ticket does not win. (iv) How many winning tickets are expected among 200 tickets bought?", r"(i) $\frac5{1000}=0.005$ (1). (ii) $\frac{10\times5}{1000}=0.05$ (2). (iii) $0.995$ (1). (iv) $0.005\times200=1$ (1).", "1+2+1+1"),
 Q(r"<b>Case study:</b> A cricket team played 20 matches: it won 12, drew 3 and lost 5. (i) Find the experimental probability of winning, drawing and losing. (ii) Check that they add to 1. (iii) Estimate the number of wins in 30 matches. (iv) Does this prove the team will win its next match?", r"(i) win $0.6$, draw $0.15$, lose $0.25$ (2). (ii) $0.6+0.15+0.25=1$ ✓ (1). (iii) $0.6\times30=18$ (1). (iv) No. It is only an estimate from past data; probability tells what happens in the long run, not what will happen next (1).", "2+1+1+1"),
 Q(r"A card is drawn from a pack of 52. Let $E$ be the event ‘the card is a spade’. (i) Find $P(E)$. (ii) Find $P(\text{not }E)$ and show it equals $1-P(E)$. (iii) Find the probability of ‘a spade or a heart’. (iv) Find the probability of ‘an ace or a king’.", r"(i) $\frac{13}{52}=\frac14$ (1). (ii) $\frac{39}{52}=\frac34=1-\frac14$ (2). (iii) $\frac{26}{52}=\frac12$ (1). (iv) 8 cards ⇒ $\frac8{52}=\frac2{13}$ (1).", "1+2+1+1"),
 Q(r"<b>Case study:</b> A class of 50 students gives its mode of travel to school: bus 18, bicycle 10, walking 12, car 10. (i) Find the probability that a randomly chosen student cycles. (ii) Find the probability for each mode and check that they add to 1. (iii) Among 1200 students in the school, estimate the number who walk. (iv) Which mode is most likely and by how much more than the least likely?", r"(i) $\frac{10}{50}=0.2$ (1). (ii) bus $0.36$, bicycle $0.2$, walking $0.24$, car $0.2$; sum $=1$ (2). (iii) $0.24\times1200=288$ (1). (iv) Bus is most likely (0.36); least likely: bicycle/car (0.2), difference $0.16$ (1).", "1+2+1+1"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
