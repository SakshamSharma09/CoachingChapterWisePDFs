"""Class 9 Maths Ch 7 Probability - extras."""
from common import AR4, Q

AR = [
 AR4(r"When a fair die is rolled, the probability of getting a prime number is $\dfrac12$.", r"The prime numbers on a die are 2, 3 and 5, which are 3 of the 6 equally likely outcomes.", "a",
     r"$P=\dfrac36=\dfrac12$, obtained exactly as in R."),
 AR4(r"The probability of an impossible event is 0.", r"The probability of any event lies between 0 and 1, both included.", "b",
     r"Both are true; R is a general range, so it does not explain why an impossible event gets exactly 0."),
 AR4(r"For any event $E$, $P(\text{not }E)=1-P(E)$.", r"For any event $E$, $P(E)+P(\text{not }E)=2$.", "c",
     r"A is correct; R is false because the sum is 1."),
 AR4(r"The probability of an event can be 1.5.", r"The probability of a sure event is 1.", "d",
     r"A is false because probability never exceeds 1; R is true."),
 AR4(r"When two fair coins are tossed together, the probability of getting exactly one head is $\dfrac12$.", r"The sample space is $\{HH, HT, TH, TT\}$ with 4 equally likely outcomes, of which HT and TH are favourable.", "a",
     r"$P=\dfrac24=\dfrac12$, from the sample space in R."),
 AR4(r"A coin tossed 100 times shows heads 54 times, so the experimental probability of a head is 0.54.", r"The theoretical probability of a head for a fair coin is $\dfrac12$.", "b",
     r"$\dfrac{54}{100}=0.54$; both are true, but R does not give the experimental value."),
]

CASE = [
 Q(r"<b>Case study.</b> In a Ludo game at home, Arjun rolls a fair six-faced die once. "
   r"(i) How many outcomes are there in the sample space? (ii) Find the probability of getting an even number. (iii) Find the probability of getting a number greater than 4. (iv) Find the probability of getting a multiple of 3 and hence the probability of not getting a multiple of 3.",
   r"(i) 6 outcomes: 1, 2, 3, 4, 5, 6 (1). (ii) $\dfrac36=\dfrac12$ (1). (iii) Favourable outcomes 5, 6, so $\dfrac26=\dfrac13$ (1). (iv) Multiples of 3 are 3 and 6, so $P=\dfrac13$ (1); $P(\text{not})=1-\dfrac13=\dfrac23$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A shopkeeper in Pune notes how 200 customers paid one day: 90 paid by cash, 70 by UPI and 40 by card. A customer is chosen at random from these 200. "
   r"(i) Find the experimental probability that the customer paid by cash. (ii) Find the probability that the customer paid by UPI. (iii) Find the probability that the customer paid by card. (iv) Find the probability that the customer did not pay by cash, and estimate how many of the next 500 customers will use UPI.",
   r"(i) $\dfrac{90}{200}=\dfrac9{20}$ (1). (ii) $\dfrac{70}{200}=\dfrac7{20}$ (1). (iii) $\dfrac{40}{200}=\dfrac15$ (1). (iv) $1-\dfrac9{20}=\dfrac{11}{20}$ (1); expected UPI customers $=500\times\dfrac7{20}=175$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Two fair coins are tossed together in a school game. "
   r"(i) Write the sample space. (ii) Find the probability of getting two heads. (iii) Find the probability of getting at least one head. (iv) Verify that $P(\text{at least one head})=1-P(\text{no head})$, and find how many times exactly one head is expected if the pair is tossed 80 times.",
   r"(i) $\{HH, HT, TH, TT\}$ (1). (ii) $\dfrac14$ (1). (iii) $\dfrac34$ (1). (iv) $P(\text{no head})=\dfrac14$ and $1-\dfrac14=\dfrac34$ (1); $P(\text{exactly one head})=\dfrac24=\dfrac12$, so expected $=80\times\dfrac12=40$ times (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Probability", [r"Theoretical probability: $P(E)=\dfrac{\text{number of outcomes favourable to }E}{\text{total number of equally likely outcomes}}$.",
   r"Experimental probability: $P(E)=\dfrac{\text{number of times }E\text{ occurred}}{\text{total number of trials}}$.",
   r"Always $0\le P(E)\le1$."]),
 ("Special events", [r"Sure event: $P=1$. Impossible event: $P=0$.", r"Complement: $P(\text{not }E)=1-P(E)$, i.e. $P(E)+P(\text{not }E)=1$.",
   r"The sum of the probabilities of all outcomes of an experiment is 1."]),
 ("Sample spaces", [r"One coin: $\{H, T\}$. Two coins: $\{HH, HT, TH, TT\}$ (4 outcomes). Three coins: 8 outcomes.",
   r"One die: $\{1,2,3,4,5,6\}$. Two dice: $6\times6=36$ outcomes.",
   r"Cards: 52 cards, 4 suits of 13; 26 red and 26 black."]),
 ("Estimation", [r"Expected number of times $E$ occurs in $N$ trials $\approx N\times P(E)$.",
   r"More trials make the experimental probability closer to the theoretical probability."]),
]

MISTAKES = [
 r"Giving a probability greater than 1 or a negative value, or leaving it as a count instead of a fraction.",
 r"Using the number of favourable outcomes divided by the number of <i>unfavourable</i> outcomes instead of the <i>total</i> outcomes.",
 r"Listing only HT for 'one head' when two coins are tossed; HT and TH are different outcomes.",
 r"Treating 'at least one' as 'exactly one'; use the complement $1-P(\text{none})$.",
 r"Assuming that outcomes are always equally likely, e.g. 'the sum of two dice is 7' has probability $\dfrac{6}{36}$, not $\dfrac1{11}$.",
 r"Confusing experimental and theoretical probability: experimental values come from trials and may differ from $\dfrac12$ for a coin.",
]
