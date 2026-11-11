"""Class 6 Maths Ch 5 Prime Time - extras."""
from common import AR4, Q

AR = [
 AR4("The number 1 is neither prime nor composite.", "The number 1 has only one factor, namely itself.", "a",
     "A prime has exactly two factors and a composite has more than two; 1 has just one factor."),
 AR4("2 is the only even prime number.", "Every even number greater than 2 has 2 as a factor other than 1 and itself.", "a",
     "So every even number above 2 has at least three factors and is composite."),
 AR4("91 is a composite number.", "Every number that is not divisible by 2, 3 or 5 is a prime number.", "c",
     "91 = 7 x 13 so A is true. 91 is not divisible by 2, 3 or 5 but is composite, so R is false."),
 AR4("51 is a prime number.", "A prime number has exactly two factors.", "d",
     "51 = 3 x 17, so A is false. R is true."),
 AR4("15 and 28 are co-prime numbers.", "28 is a composite number.", "b",
     "HCF(15, 28) = 1, so A is true. R is true but does not explain why they are co-prime."),
 AR4("If a number is divisible by 9, it is divisible by 3.", "3 is a factor of 9.", "a",
     "Any multiple of 9 is a multiple of a multiple of 3, so it is divisible by 3."),
]

CASE = [
 Q(r"<b>Case study.</b> Two temple bells ring together at 9:00 am. One bell rings every 12 minutes and the other every 18 minutes. (i) Write 12 and 18 as products of prime factors. (ii) Find the LCM of 12 and 18. (iii) At what time will they ring together next? (iv) How many more times will they ring together before 11:00 am? Give the times.",
   r"(i) $12=2^2\times3$, $18=2\times3^2$ (1). (ii) LCM $=2^2\times3^2=36$ (1). (iii) 9:36 am (1). (iv) 11:00 am is 120 minutes after 9:00; $120\div36$ gives 3 more times, at 9:36, 10:12 and 10:48 am (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A hall floor is 120 cm by 84 cm and is to be covered with square tiles of the largest possible size, with no tile cut. (i) Write 120 and 84 as products of prime factors. (ii) Find the side of the largest square tile. (iii) How many tiles fit along the length and along the breadth? (iv) Find the total number of tiles and check it by using areas.",
   r"(i) $120=2^3\times3\times5$, $84=2^2\times3\times7$ (1). (ii) HCF $=2^2\times3=12$ cm (1). (iii) $120\div12=10$ along the length and $84\div12=7$ along the breadth (1). (iv) $10\times7=70$ tiles (1); check: $\dfrac{120\times84}{12\times12}=\dfrac{10080}{144}=70$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Sana is using the Sieve of Eratosthenes on the numbers from 1 to 30. She crosses out 1 and all multiples of 2, 3 and 5 except the numbers 2, 3 and 5 themselves. (i) How many prime numbers are there from 1 to 30? (ii) Write the primes between 20 and 30. (iii) Is 27 a prime? Give a reason. (iv) Use the divisibility test for 3 to show that 57 is not a prime.",
   r"(i) 10 primes (2, 3, 5, 7, 11, 13, 17, 19, 23, 29) (1). (ii) 23 and 29 (1). (iii) No, $27=3\times9$ has more than two factors (1). (iv) The digit sum of 57 is $5+7=12$, which is divisible by 3, so 57 is divisible by 3 (1); $57=3\times19$, so it is composite (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Factors and multiples", [r"A factor of $n$ divides $n$ exactly; the smallest factor is 1 and the largest is $n$.",
   r"A multiple of $n$ is $n\times1, n\times2, n\times3,\dots$ Every number is a factor and a multiple of itself.",
   r"Prime: exactly two factors (1 and itself), e.g. 2, 3, 5, 7, 11. Composite: more than two factors. 1 is neither."]),
 ("Divisibility tests", [r"By 2: last digit 0, 2, 4, 6, 8.  By 5: last digit 0 or 5.  By 10: last digit 0.",
   r"By 3: digit sum divisible by 3.  By 9: digit sum divisible by 9.",
   r"By 4: last two digits divisible by 4.  By 8: last three digits divisible by 8.",
   r"By 11: (sum of digits at odd places) $-$ (sum at even places) is 0 or a multiple of 11."]),
 ("Prime factorisation, HCF and LCM", [r"Every number $>1$ is a product of primes, e.g. $60=2^2\times3\times5$.",
   r"HCF: product of the common prime factors with the smallest powers.",
   r"LCM: product of all prime factors with the greatest powers.",
   r"For two numbers: $\text{HCF}\times\text{LCM}=$ product of the two numbers.",
   r"Co-prime numbers: HCF $=1$ (e.g. 15 and 28)."]),
 ("Sieve of Eratosthenes", [r"Cross out 1, then multiples of 2, 3, 5, 7, ... (keep the prime itself). Primes up to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29."]),
 ("Problem types", [r"Meet again together $\Rightarrow$ LCM. Largest equal pieces or tiles $\Rightarrow$ HCF."]),
]

MISTAKES = [
 r"Calling 1 a prime number; 1 is neither prime nor composite.",
 r"Thinking all odd numbers are prime (9, 15, 21, 91 are composite) or that 2 is not prime.",
 r"Taking the greatest powers for HCF or the smallest powers for LCM; it is the other way round.",
 r"Using LCM when the question asks for the largest equal size (HCF), and the reverse for 'meet again'.",
 r"Applying the divisibility test for 4 or 8 to the digit sum instead of the last two or three digits.",
]
