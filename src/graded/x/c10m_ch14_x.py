"""Class 10 Maths Ch 14 Probability - extras (classical probability of single events; no cards, no empirical probability)."""
from common import AR4, Q

AR = [
 AR4(r"The probability of getting a number greater than 6 when a die is thrown once is 0.", r"The probability of an impossible event is 0.", "a",
     r"No face of a die shows more than 6, so the event is impossible and its probability is 0."),
 AR4(r"The probability of getting a prime number when a die is thrown once is $\dfrac12$.", r"The probability of an event can be greater than 1.", "c",
     r"Primes are 2, 3, 5, so $P=\tfrac36=\tfrac12$: A true; probability lies between 0 and 1, so R is false."),
 AR4(r"The probability of an event can be 1.5.", r"For any event E, $0\le P(E)\le1$.", "d",
     r"A is false since $P(E)\le1$; R states exactly that and is true."),
 AR4(r"When two coins are tossed together, the probability of getting at least one head is $\dfrac34$.", r"The sum of the probabilities of all the elementary events of an experiment is 1.", "b",
     r"Outcomes HH, HT, TH, TT: three have at least one head, so $P=\tfrac34$. R is true but it is not the reason for the value."),
 AR4(r"If $P(E)=0.35$, then $P(\text{not }E)=0.65$.", r"For any event E, $P(E)+P(\text{not }E)=1$.", "a",
     r"$P(\text{not }E)=1-0.35=0.65$ using R."),
 AR4(r"A bag has 3 red and 5 blue balls. The probability of drawing a red ball is $\dfrac38$.", r"The probability of an event is the number of unfavourable outcomes divided by the total number of outcomes.", "c",
     r"Favourable outcomes 3 out of 8 gives $\tfrac38$: A true; probability uses <i>favourable</i> outcomes, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> A bag contains 4 red, 5 blue and 6 green balls. One ball is drawn at random. "
   r"(i) How many equally likely outcomes are there? (ii) Find the probability that the ball is red. (iii) Find the probability that the ball is not green. (iv) Find the probability that the ball is blue or green. If 5 more red balls are added to the bag, what is the new probability of drawing a red ball?",
   r"(i) $4+5+6=15$ (1). (ii) $P(\text{red})=\tfrac4{15}$ (1). (iii) $P(\text{not green})=\tfrac{9}{15}=\tfrac35$ (1). (iv) $P(\text{blue or green})=\tfrac{11}{15}$ (1); new total $=20$, red $=9$, $P=\tfrac9{20}$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Two fair dice are thrown together in a board game. "
   r"(i) How many outcomes are possible in all? (ii) Find the probability that the sum of the numbers is 8. (iii) Find the probability of getting a doublet. (iv) Find the probability that the sum is a prime number, showing the count of favourable outcomes.",
   r"(i) $6\times6=36$ (1). (ii) Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2), so $P=\tfrac5{36}$ (1). (iii) Doublets: 6, so $P=\tfrac6{36}=\tfrac16$ (1). (iv) Sum 2: 1 way, 3: 2, 5: 4, 7: 6, 11: 2; total 15 favourable (1); $P=\tfrac{15}{36}=\tfrac5{12}$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A raffle has 25 tickets numbered 1 to 25 placed in a box. One ticket is drawn at random. "
   r"(i) How many equally likely outcomes are there? (ii) Find the probability that the number is a prime number. (iii) Find the probability that the number is a multiple of 5. (iv) Find the probability that the number is neither prime nor a multiple of 5.",
   r"(i) 25 (1). (ii) Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23 (9 numbers), $P=\tfrac9{25}$ (1). (iii) Multiples of 5: 5, 10, 15, 20, 25 (5 numbers), $P=\tfrac5{25}=\tfrac15$ (1). (iv) 5 is counted in both lists, so prime or multiple of 5 $=9+5-1=13$ numbers (1); $P(\text{neither})=\tfrac{25-13}{25}=\tfrac{12}{25}$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Classical (theoretical) probability", [r"$P(E)=\dfrac{\text{number of outcomes favourable to }E}{\text{total number of equally likely outcomes}}$.",
   r"$0\le P(E)\le1$. Impossible event: $P=0$. Sure (certain) event: $P=1$."]),
 ("Complementary events", [r"$P(E)+P(\overline E)=1$, so $P(\overline E)=1-P(E)$ ($\overline E$ = 'not E').",
   r"Sum of the probabilities of all elementary events of an experiment $=1$."]),
 ("Sample spaces", [r"One coin: H, T (2). Two coins: HH, HT, TH, TT (4). Three coins: 8 outcomes.",
   r"One die: 1 to 6 (6). Two dice: $6\times6=36$ outcomes."]),
 ("Two dice: useful counts", [r"Sum 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1 (total 36).",
   r"Doublets: 6. Prime sums 2, 3, 5, 7, 11: 15 outcomes."]),
 ("Counting tips", [r"Primes up to 20: 2, 3, 5, 7, 11, 13, 17, 19. Composite numbers have more than two factors; 1 is neither prime nor composite.",
   r"'A or B' when A and B overlap: $n(A\cup B)=n(A)+n(B)-n(A\cap B)$.",
   r"Adding objects to a bag changes both the favourable and the total counts."]),
]

MISTAKES = [
 r"Writing a probability greater than 1 or negative; a probability always lies between 0 and 1.",
 r"Using outcomes that are not equally likely (e.g. treating 'sum 7' and 'sum 12' as equally likely).",
 r"Counting 1 as a prime number, or leaving out 2, the only even prime.",
 r"Counting the overlap twice in 'A or B' questions.",
 r"For two dice, using only 12 or 6 outcomes instead of 36, or counting (2,6) and (6,2) as the same outcome.",
 r"Not changing the total number of outcomes when balls are removed or added, and not simplifying the fraction.",
]
