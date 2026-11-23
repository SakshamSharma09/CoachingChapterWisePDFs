"""Class 6 Maths Ch 5 - Prime Time: worksheet + detailed notes."""
from math import gcd
from libws import *          # W, run
BANK = "c6m_ch05"

def lcm(a, b): return a * b // gcd(a, b)
def lcmm(*xs):
    r = 1
    for x in xs: r = lcm(r, x)
    return r
def gcdm(*xs):
    r = 0
    for x in xs: r = gcd(r, x)
    return r
def fac(n): return [d for d in range(1, n + 1) if n % d == 0]
def isp(n): return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))

# ---- self-checks -------------------------------------------------------------
assert fac(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36] and fac(24) == [1, 2, 3, 4, 6, 8, 12, 24]
assert [p for p in range(20, 41) if isp(p)] == [23, 29, 31, 37] and 91 == 7 * 13 and 51 == 3 * 17
assert gcd(12, 18) == 6 and lcm(4, 6) == 12 and gcd(8, 12) == 4 and lcm(8, 12) == 24
assert lcmm(12, 15) == 60 and gcd(48, 36) == 12 and 48 // 12 + 36 // 12 == 7
assert 84 == 2**2 * 3 * 7 and 126 == 2 * 3**2 * 7 and gcd(84, 126) == 42 and lcm(84, 126) == 252
assert 3102 % 2 == 0 and 3102 % 3 == 0 and 3102 % 4 != 0 and 3102 % 6 == 0 and 3102 % 9 != 0
assert 2728 % 11 == 0 and 8712 % 11 == 0 and 5463 % 11 != 0 and lcmm(2, 3, 4, 5) == 60 and lcmm(2, 3, 4) + 1 == 13
assert gcd(15, 25) == 5 and 3 + 17 == 20 == 7 + 13 and max(p for p in range(10, 100) if isp(p)) == 97 and min(p for p in range(100, 1000) if isp(p)) == 101
assert [p for p in range(50, 71) if isp(p)] == [53, 59, 61, 67] and sum(isp(p) for p in range(1, 31)) == 10
assert lcmm(12, 16, 24) == 48 and gcd(240, 180) == 60 and (240 // 60) * (180 // 60) == 12
assert [(a, b) for a, b in [(14, 15), (18, 24), (35, 64), (21, 28)] if gcd(a, b) == 1] == [(14, 15), (35, 64)]
assert 210 == 2 * 3 * 5 * 7 and 91 % 7 == 0 and gcdm(36, 48, 60) == 12 and len([1 for a in fac(30) if a * a <= 30]) == 4
assert 8172 % 9 == 0 and 8172 % 11 != 0 and 8172 % 4 == 0 and lcmm(40, 60, 90) == 360 and 360 // 60 == 6
assert gcdm(120, 180, 240) == 60 and 120 // 60 + 180 // 60 + 240 // 60 == 9 and lcmm(6, 8, 12) + 5 == 29
assert lcmm(12, 15, 20) == 60 and 17 * 60 == 1020 and 16 * 60 < 1000 and 24 * 30 // 6 == 120 and gcd(24, 30) == 6 and 1001 == 7 * 11 * 13
assert 2794 % 11 == 0 and [x for x in range(100, 201) if x % 24 == 0] == [120, 144, 168, 192]
assert 360 == 2**3 * 3**2 * 5 and 540 == 2**2 * 3**3 * 5 and gcd(360, 540) == 180 and lcm(360, 540) == 1080
assert 221 == 13 * 17 and gcd(36, 48) == 12 and 36 // 12 == 3 and 48 // 12 == 4 and lcm(18, 24) == 72 and 72 // 18 == 4 and 72 // 24 == 3
assert 12 % 2 == 0 and 12 % 4 == 0 and 12 % 8 != 0 and 12 % 4 == 0 and 12 % 6 == 0 and 12 % 24 != 0

WS = [
# ------------------------------------------------------------------ EASY
W("The smallest prime number is", 1, "(c) 2. It has exactly two factors, 1 and 2. (0 and 1 are not prime; 3 is bigger.) (1)", "E", opts=["0", "1", "2", "3"]),
W("Which of these numbers is composite?", 1, "(c) 51. $51=3\\times17$ has more than two factors. 29, 31 and 37 are prime. (1)", "E", opts=["29", "31", "51", "37"]),
W("Which pair of numbers is co-prime?", 1, "(b) 8 and 15. Their only common factor is 1. (4, 6 share 2; 9, 12 share 3; 14, 21 share 7.) (1)", "E", opts=["4 and 6", "8 and 15", "9 and 12", "14 and 21"]),
W("The HCF of 12 and 18 is", 1, "(a) 6. Factors of 12: 1, 2, 3, 4, 6, 12; of 18: 1, 2, 3, 6, 9, 18; the greatest common one is 6. (1)", "E", opts=["6", "3", "36", "9"]),
W("The LCM of 4 and 6 is", 1, "(b) 12. Multiples of 4: 4, 8, 12; of 6: 6, 12; the smallest common multiple is 12. (1)", "E", opts=["24", "12", "10", "2"]),
W("The prime factorisation of 60 is", 1, "(c) $2\\times2\\times3\\times5$, that is $2^2\\times3\\times5$. (1)", "E", opts=["$2\\times3\\times10$", "$4\\times15$", "$2^2\\times3\\times5$", "$2\\times3^2\\times5$"]),
W("List all the factors of 36. How many are there?", 2, "1, 2, 3, 4, 6, 9, 12, 18, 36. There are 9 factors. (2)", "E"),
W("Write the first five multiples of 7.", 1, "7, 14, 21, 28, 35. (1)", "E"),
W("A teacher wants to seat 24 students in equal rows with nobody left out. Write all the possible numbers of rows.", 2, "The number of rows must be a factor of 24: 1, 2, 3, 4, 6, 8, 12, 24. (2)", "E", wp=True),
W("List the prime numbers between 20 and 40.", 2, "23, 29, 31, 37. (2)", "E"),
W("True or False? Give a reason. “1 is a prime number.”", 2, "False. A prime number has exactly two factors, but 1 has only one factor (itself). So 1 is neither prime nor composite. (2)", "E"),
W("Twin primes are primes that differ by 2, like 11 and 13. Write all the pairs of twin primes below 20.", 2, "(3, 5), (5, 7), (11, 13), (17, 19). (2)", "E"),
W("Meena says 91 is a prime number. Check by finding a factor other than 1 and 91.", 2, "$91=7\\times13$, so it has factors 7 and 13 as well. 91 is composite. (2)", "E"),
W("Use divisibility tests to say which of 2, 3, 4, 5, 9, 10 divide 2,340 exactly.", 2, "Ends in 0, so divisible by 2, 5 and 10. Digit sum $2+3+4+0=9$, so divisible by 3 and 9. Last two digits 40 is divisible by 4. So all six divide it. (2)", "E"),
W("A farmer wants to plant 36 saplings in equal rows. Can he make 5 equal rows? Why or why not? What numbers of equal rows are possible with 36 saplings?", 2, "No, 36 is not divisible by 5 (it does not end in 0 or 5). The number of rows must be a factor of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36. (2)", "E", wp=True),
W("Write the prime factorisation of 28.", 1, "$28=2\\times2\\times7=2^2\\times7$. (1)", "E"),
W("Find the HCF and the LCM of 8 and 12 by writing their factors and multiples.", 2, "Factors of 8: 1, 2, 4, 8; of 12: 1, 2, 3, 4, 6, 12. HCF $=4$. Multiples of 8: 8, 16, 24; of 12: 12, 24. LCM $=24$. (1+1)", "E"),

# ------------------------------------------------------------------ MEDIUM
W("Two bells ring together at 9:00 a.m. After that one bell rings every 12 minutes and the other every 15 minutes. At what time will they next ring together?", 3,
  "They ring together after the LCM of 12 and 15. $12=2^2\\times3$, $15=3\\times5$, LCM $=2^2\\times3\\times5=60$ minutes. So at 10:00 a.m. (3)", "M", wp=True),
W("Two ropes are 48 m and 36 m long. Both are cut into pieces of equal length, as long as possible, with nothing left over. Find the length of each piece and the total number of pieces.", 3,
  "Length $=$ HCF of 48 and 36 $=12$ m. Pieces: $48\\div12=4$ and $36\\div12=3$, total 7 pieces. (3)", "M", wp=True),
W("Find the prime factorisation of 84 and 126. Hence find their HCF and LCM.", 3,
  "$84=2^2\\times3\\times7$, $126=2\\times3^2\\times7$. HCF $=2\\times3\\times7=42$ (common primes, smallest powers). LCM $=2^2\\times3^2\\times7=252$ (all primes, greatest powers). (3)", "M"),
W("Test 3,102 for divisibility by 2, 3, 4, 6 and 9.", 3, "2: last digit 2, yes. 3: digit sum 6, yes. 4: last two digits 02, not divisible. 6: divisible by 2 and 3, yes. 9: digit sum 6, no. (3)", "M"),
W("Using the divisibility rule for 11, test 2,728, 8,712 and 5,463.", 3,
  "2,728: $(2+2)-(7+8)=4-15=-11$, a multiple of 11, so divisible. 8,712: $(8+1)-(7+2)=0$, divisible. 5,463: $(5+6)-(4+3)=4$, not divisible. (3)", "M"),
W("A shopkeeper wants to pack mangoes so that the total can be packed in boxes of 2, or 3, or 4, or 5 with none left over. What is the smallest number of mangoes he needs?", 2,
  "Smallest number divisible by 2, 3, 4 and 5 is their LCM. $2$, $3$, $2^2$, $5$ give $2^2\\times3\\times5=60$ mangoes. (2)", "M", wp=True),
W("Find the smallest number greater than 4 which leaves a remainder 1 when divided by 2, 3 and 4.", 3, "LCM of 2, 3, 4 is 12. A number that leaves remainder 1 is $12+1=13$. Check: $13=2\\times6+1=3\\times4+1=4\\times3+1$. (3)", "M"),
W("Anil says 15 and 25 are co-prime because neither is a prime number. Is he right? Explain.", 2, "No. Co-prime means the only common factor is 1. 15 and 25 have the common factor 5 (HCF is 5), so they are not co-prime. Co-prime numbers need not be prime, but they must have HCF 1. (2)", "M"),
W("Express 20 as the sum of two prime numbers in two different ways.", 2, "$3+17=20$ and $7+13=20$. (2)", "M"),
W("Write the largest 2-digit prime number and the smallest 3-digit prime number.", 2, "Largest 2-digit prime is 97 (98, 99 are composite). Smallest 3-digit prime is 101 (100 is even). (1+1)", "M"),
W("How many prime numbers are there from 1 to 30? List the primes between 50 and 70.", 3, "From 1 to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, which are 10 primes. (1.5) Between 50 and 70: 53, 59, 61, 67. (1.5)", "M"),
W("Three runners start together at the starting line of a circular track. They take 12 s, 16 s and 24 s to complete one round. After how many seconds will all three be at the start together again?", 3,
  "LCM of 12, 16 and 24: $12=2^2\\times3$, $16=2^4$, $24=2^3\\times3$. LCM $=2^4\\times3=48$ seconds. (3)", "M", wp=True),
W("A floor 240 cm long and 180 cm wide is to be covered with square tiles of the biggest possible size, with no cutting. Find the side of the tile and the number of tiles.", 3,
  "Side $=$ HCF of 240 and 180 $=60$ cm. Tiles along the length $=240\\div60=4$; along the width $=180\\div60=3$. Number of tiles $=4\\times3=12$. (3)", "M", wp=True),
W("Which of these pairs are co-prime: (14, 15), (18, 24), (35, 64), (21, 28)?", 2, "(14, 15): HCF 1, co-prime. (18, 24): HCF 6. (35, 64): HCF 1, co-prime. (21, 28): HCF 7. So (14, 15) and (35, 64) are co-prime. (2)", "M"),
W("Find the prime factors of 210. How many different prime factors does it have?", 2, "$210=2\\times3\\times5\\times7$. It has 4 different prime factors. (2)", "M"),
W("Can 91 chocolates be shared equally among 7 friends without breaking any? Among 5 friends? Explain.", 2, "Among 7: $91=7\\times13$, so yes, 13 each. Among 5: 91 does not end in 0 or 5, so it is not divisible by 5, so no. (2)", "M", wp=True),
W("Find the HCF of 36, 48 and 60 using prime factorisation.", 3, "$36=2^2\\times3^2$, $48=2^4\\times3$, $60=2^2\\times3\\times5$. Common primes: 2 and 3, smallest powers $2^2$ and $3$. HCF $=4\\times3=12$. (3)", "M"),
W("Reena has 30 chocolates and arranges all of them in a rectangle of rows and columns, with no gaps. How many different rectangles are possible if a rectangle with 5 rows and 6 columns is treated as the same as 6 rows and 5 columns?", 2,
  "Factor pairs of 30: $1\\times30$, $2\\times15$, $3\\times10$, $5\\times6$. So 4 different rectangles. (2)", "M", wp=True),
W("Is 8,172 divisible by 9? By 11? By 4? Show the tests.", 3, "9: digit sum $8+1+7+2=18$, yes. 11: $(8+7)-(1+2)=12$, not a multiple of 11, so no. 4: last two digits 72, and $72=4\\times18$, so yes. (3)", "M"),

# ------------------------------------------------------------------ HARD
W("Three traffic lights at a crossing change after every 40 seconds, 60 seconds and 90 seconds. They change together at 8:00:00 a.m. At what time will they next change together?", 4,
  "LCM of 40, 60, 90: $40=2^3\\times5$, $60=2^2\\times3\\times5$, $90=2\\times3^2\\times5$. LCM $=2^3\\times3^2\\times5=360$ seconds $=6$ minutes. So at 8:06:00 a.m. (4)", "H", wp=True),
W("A merchant has 120 L, 180 L and 240 L of three kinds of oil. He wants to fill them in tins of the same capacity, as big as possible, with no oil left over. Find the capacity of a tin and the total number of tins.", 4,
  "Capacity $=$ HCF of 120, 180, 240 $=60$ L. Tins: $120\\div60=2$, $180\\div60=3$, $240\\div60=4$. Total $=2+3+4=9$ tins. (4)", "H", wp=True),
W("Find the smallest number greater than 12 which leaves a remainder 5 when divided by 6, by 8 and by 12.", 3, "LCM of 6, 8, 12 is 24 ($2^3\\times3$). Required number $=24+5=29$. Check: $29=6\\times4+5=8\\times3+5=12\\times2+5$. (3)", "H"),
W("Find the smallest 4-digit number that is divisible by 12, 15 and 20.", 4,
  "LCM of 12, 15, 20 $=2^2\\times3\\times5=60$. $1000\\div60$ gives 16 remainder 40, so $16\\times60=960$ has 3 digits and the next multiple $17\\times60=1020$ is the smallest 4-digit multiple. (4)", "H"),
W("The HCF of 24 and 30 is 6. Use the rule HCF × LCM = product of the two numbers to find their LCM. Check the rule for 12 and 18.", 3,
  "LCM $=\\frac{24\\times30}{6}=\\frac{720}{6}=120$. For 12 and 18: HCF $=6$, LCM $=36$ and $6\\times36=216=12\\times18$. (3)", "H"),
W("To find all primes up to 100 by the Sieve of Eratosthenes we cross out multiples of 2, 3, 5 and 7 only. Why is it not necessary to cross out multiples of 11 and bigger primes?", 3,
  "Any composite number up to 100 is a product of two factors and the smaller factor is at most 10 (since $11\\times11=121>100$). So it has a prime factor 2, 3, 5 or 7 and has been crossed out already. (3)", "H"),
W("Find the digit that can replace the blank so that the number 27_4 is divisible by 11. Verify.", 3,
  "Digits at odd places: $2$ and $\\_$; at even places: $7$ and $4$. Even sum $=11$. Odd sum $=2+\\_$. The difference must be 0 or 11, so $2+\\_=11$, blank $=9$. Check: $2794=11\\times254$. (3)", "H"),
W("List all the numbers between 100 and 200 that are divisible by both 6 and 8.", 3, "A number divisible by both 6 and 8 is a multiple of their LCM 24. Multiples of 24 between 100 and 200: $24\\times5=120$, $144$, $168$, $192$. (3)", "H"),
W("Find the prime factorisation of 360 and 540. Use it to find their HCF and LCM and check that HCF × LCM equals the product.", 4,
  "$360=2^3\\times3^2\\times5$, $540=2^2\\times3^3\\times5$. HCF $=2^2\\times3^2\\times5=180$. LCM $=2^3\\times3^3\\times5=1080$. Check: $180\\times1080=194400=360\\times540$. (4)", "H"),
W("Two numbers have HCF 1 and LCM 221. What does HCF 1 tell you about them? Find the two numbers if both are prime.", 3,
  "HCF 1 means they are co-prime. For co-prime numbers the LCM is their product. $221=13\\times17$, so the primes are 13 and 17. (3)", "H"),
W("Is 1,001 a prime number? Test it with the divisibility rules for 7 and 11 and write its prime factorisation.", 3,
  "11: $(1+0)-(0+1)=0$, so 11 divides 1,001. 7: $1001=7\\times143$. Then $143=11\\times13$. So $1001=7\\times11\\times13$, which is composite. (3)", "H"),
W("A class has 36 boys and 48 girls. The teacher forms the largest possible number of groups so that each group has the same number of boys and the same number of girls. How many groups are there and how many boys and girls does each group have?", 4,
  "Number of groups $=$ HCF of 36 and 48 $=12$. Each group has $36\\div12=3$ boys and $48\\div12=4$ girls. (4)", "H", wp=True),
W("Show by an example that a number divisible by both 2 and 4 need not be divisible by 8, and that a number divisible by both 4 and 6 need not be divisible by 24. Which rule for testing a composite number does this teach us?", 3,
  "12 is divisible by 2 and 4 but $12\\div8$ is not a whole number. 12 is divisible by 4 and 6 but not by 24. The rule: to test divisibility by a composite number, test its **co-prime** factors (e.g. 3 and 4 for 12, 8 and 9 for 72), not factors that share a common factor. (3)", "H"),
W("Asha and Bhavna run on a circular track. Asha takes 18 minutes for one round and Bhavna 24 minutes. They start together. After how many minutes will they again be at the start together? How many rounds will each have completed?", 4,
  "LCM of 18 and 24: $18=2\\times3^2$, $24=2^3\\times3$, LCM $=2^3\\times3^2=72$ minutes. Asha: $72\\div18=4$ rounds. Bhavna: $72\\div24=3$ rounds. (4)", "H", wp=True),
]

CH = dict(num=5, title="Prime Time", tag="Maths (Part 1)",
 intro="Primes are the building blocks of all counting numbers, just as atoms are the building blocks of matter. In this chapter you will learn about factors and multiples, primes and composites, how to break any number into primes, quick divisibility tests and how HCF and LCM solve everyday problems such as cutting ropes, tiling floors and finding when bells ring together.",
 big_questions=["What are factors and multiples, and what makes a number prime?", "How do we write a number as a product of primes?", "How do HCF and LCM help us solve real problems?"],
 blocks=[
 ("h2", "5.1 Factors and Multiples"),
 ("note", "DEFINITION", "A **factor** of a number divides it exactly (with no remainder). A **multiple** of a number is obtained by multiplying it by 1, 2, 3, 4, … Every number is a factor and a multiple of itself, and 1 is a factor of every number."),
 ("ul", ["Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36 (nine factors). Factors come in pairs: 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6.", "Multiples of 7: 7, 14, 21, 28, 35, … and so on without end.", "The number of factors is **finite**; multiples are **infinite**. Every factor is ≤ the number; every multiple is ≥ the number.", "Equal-rows situations use factors: 24 students can be seated in equal rows with nobody left out only if the number of rows is a factor of 24: 1, 2, 3, 4, 6, 8, 12 or 24."]),
 ("h2", "5.2 Primes, Composites and Co-primes"),
 ("table", ["Kind", "Meaning", "Examples"], [
  ["**Prime**", "exactly two factors: 1 and itself", "2, 3, 5, 7, 11, 13, 17, 19, 23, 29"],
  ["**Composite**", "more than two factors", "4, 6, 9, 15, 51 (= 3 × 17), 91 (= 7 × 13)"],
  ["Neither", "1 has only one factor", "1"],
  ["**Co-primes**", "two numbers whose only common factor is 1 (HCF = 1)", "8 and 15; 35 and 64; 14 and 15 (they need not be prime)"],
  ["**Twin primes**", "primes that differ by 2", "(3, 5), (5, 7), (11, 13), (17, 19)"]]),
 ("note", "IMPORTANT", "**2 is the only even prime** (every other even number also has 2 as a factor). **1 is neither prime nor composite.** There are **10 primes below 30** (2, 3, 5, 7, 11, 13, 17, 19, 23, 29), **4 between 20 and 40** (23, 29, 31, 37) and **25 below 100**. The largest 2-digit prime is 97 and the smallest 3-digit prime is 101."),
 ("p", "**Goldbach's idea.** Many even numbers can be written as a sum of two primes: 20 = 3 + 17 = 7 + 13. Nobody has found an even number greater than 2 for which it fails, but nobody has proved that it always works."),
 ("h3", "The Sieve of Eratosthenes (finding primes up to 100)"),
 ("steps", [("Step 1", "Write the numbers 1 to 100 in a grid and cross out 1 (it is not prime)."), ("Step 2", "Circle 2 and cross out all its other multiples (4, 6, 8, …)."), ("Step 3", "Circle the next number not crossed out (3) and cross out its multiples; repeat with 5 and 7."), ("Step 4", "Stop. Any composite number up to 100 has a factor ≤ 10 (since 11 × 11 = 121 is more than 100), so it has already been crossed out. The 25 numbers left are the primes.")]),
 ("h2", "5.3 Prime Factorisation"),
 ("note", "DEFINITION", "Writing a number as a **product of primes** is called its **prime factorisation**. It is **unique** apart from the order in which the primes are written."),
 ("p", "Use a **factor tree**: split the number into two factors, keep splitting any composite factor, and stop when all the leaves are primes. 84 = 2 × 42 = 2 × 2 × 21 = 2 × 2 × 3 × 7 = **2² × 3 × 7**. In the same way 126 = 2 × 63 = 2 × 3 × 21 = **2 × 3² × 7** and 360 = **2³ × 3² × 5**."),
 ("table", ["Number", "Prime factorisation", "Different primes"], [["28", "2² × 7", "2, 7"], ["60", "2² × 3 × 5", "2, 3, 5"], ["84", "2² × 3 × 7", "2, 3, 7"], ["210", "2 × 3 × 5 × 7", "2, 3, 5, 7"], ["360", "2³ × 3² × 5", "2, 3, 5"], ["1,001", "7 × 11 × 13", "7, 11, 13"]]),
 ("h2", "5.4 Divisibility Rules"),
 ("table", ["By", "Rule", "Example"], [
  ["2, 5, 10", "last digit even / 0 or 5 / 0", "2,340"],
  ["3", "sum of digits divisible by 3", "3,102: 3 + 1 + 0 + 2 = 6 ✓"],
  ["9", "sum of digits divisible by 9", "8,172: 18 ✓"],
  ["4", "last two digits divisible by 4", "5,316: 16 ✓"],
  ["8", "last three digits divisible by 8", "7,392: 392 = 8 × 49 ✓"],
  ["6", "divisible by both 2 and 3", "3,102 ✓"],
  ["11", "difference between the sum of the digits at odd places and the sum at even places is 0 or a multiple of 11", "2,728: (2 + 2) − (7 + 8) = −11 ✓; 8,712: 9 − 9 = 0 ✓"]]),
 ("note", "REMEMBER", "To test divisibility by a composite number such as 12 (or 24, 72), test it for **co-prime factors**: 3 and 4 for 12; 3 and 8 for 24. Testing 2 and 6 is not enough for 12 because 2 and 6 share a factor. For example 12 is divisible by 2 and 4 but not by 8, and by 4 and 6 but not by 24."),
 ("h2", "5.5 Common Factors, HCF; Common Multiples, LCM"),
 ("note", "DEFINITION", "**HCF** (highest common factor) of given numbers is the greatest number that divides all of them. **LCM** (lowest common multiple) is the smallest number that is a multiple of all of them."),
 ("table", ["Method", "HCF", "LCM"], [["Listing", "list the factors, pick the greatest common one", "list the multiples, pick the smallest common one"], ["Prime factorisation", "multiply the **common** primes with the **smallest** powers", "multiply **all** primes with the **greatest** powers"]]),
 ("note", "FORMULA", "For two numbers **HCF × LCM = product of the numbers**. So LCM = (a × b) ÷ HCF. Example: HCF of 24 and 30 is 6, so LCM = 720 ÷ 6 = 120. This rule is for **two** numbers only. For co-prime numbers the LCM is just their product (13 and 17 give 221)."),
 ("p", "**Example.** 12 = 2² × 3 and 18 = 2 × 3². HCF = 2 × 3 = **6**; LCM = 2² × 3² = **36**. HCF of 36, 48 and 60 is 2² × 3 = **12**; LCM of 12, 16 and 24 is 2⁴ × 3 = **48**."),
 ("h2", "5.6 Which One to Use in a Word Problem: HCF or LCM?"),
 ("table", ["Clue in the problem", "Use", "Why"], [
  ["‘Cut into equal pieces, as long as possible’, ‘largest tile’, ‘greatest capacity’, ‘largest number of groups’", "**HCF**", "we are splitting into equal parts, and want the biggest part that divides all quantities"],
  ["‘Ring together again’, ‘meet at the start again’, ‘change together’, ‘smallest number divisible by …’", "**LCM**", "we are looking for the first time that repeating events coincide (a common multiple)"],
  ["‘Leaves remainder r’", "**LCM + r**", "the number is a common multiple plus the remainder"]]),
 ("h2", "5.7 Worked Examples"),
 ("steps", [
  ("Example 1 — Bells (LCM)", "Bells ring every 12 and 15 minutes from 9:00 a.m. LCM = 60 minutes, so they ring together at 10:00 a.m."),
  ("Example 2 — Ropes (HCF)", "Ropes of 48 m and 36 m cut into the longest equal pieces: HCF = 12 m. Pieces: 4 + 3 = 7."),
  ("Example 3 — Tiles (HCF)", "A floor 240 cm × 180 cm needs square tiles of side HCF = 60 cm; number = (240 ÷ 60) × (180 ÷ 60) = 4 × 3 = 12."),
  ("Example 4 — Traffic lights (LCM)", "Lights change every 40, 60, 90 seconds. LCM = 360 s = 6 minutes."),
  ("Example 5 — Remainder", "Smallest number greater than 12 that leaves remainder 5 when divided by 6, 8, 12: LCM = 24, so 24 + 5 = **29**."),
  ("Example 6 — Smallest 4-digit multiple", "Divisible by 12, 15, 20: LCM = 60; 1000 ÷ 60 gives 16 remainder 40, so the smallest 4-digit multiple is 17 × 60 = **1020**."),
  ("Example 7 — Missing digit (rule of 11)", "2 7 _ 4: odd places 2 + _, even places 7 + 4 = 11. For the difference to be 0 we need 2 + _ = 11, so the digit is **9**; 2794 = 11 × 254."),
  ("Example 8 — Groups", "36 boys and 48 girls into the largest number of equal groups: HCF = 12 groups, each with 3 boys and 4 girls.")]),
 ("note", "REMEMBER", "Common mistakes: (1) calling 1 a prime; (2) thinking all odd numbers are prime (9, 15, 91 are not); (3) believing co-prime numbers must be prime (8 and 15 are co-prime); (4) taking the greatest powers for the HCF instead of the smallest; (5) mixing up HCF and LCM in word problems; (6) testing divisibility by 12 with 2 and 6, or by 24 with 4 and 6."),
 ("h2", "Quick Revision: Likely Exam Questions"),
 ("qa", [
  ("Define a prime number and give three examples.", "A number with exactly two factors, 1 and itself: 2, 3, 5."),
  ("Is 91 prime?", "No. 91 = 7 × 13."),
  ("What are twin primes? Give a pair.", "Primes that differ by 2, e.g. (5, 7) or (11, 13)."),
  ("List the primes between 20 and 40.", "23, 29, 31, 37."),
  ("Find the prime factorisation of 84.", "2 × 2 × 3 × 7 = 2² × 3 × 7."),
  ("Find the HCF and LCM of 12 and 18.", "HCF = 6, LCM = 36."),
  ("State the divisibility rule of 11.", "The difference of the sum of the digits at odd places and the sum of the digits at even places is 0 or a multiple of 11."),
  ("Why is every even number greater than 2 composite?", "It has 2 as a factor besides 1 and itself."),
  ("Are 35 and 64 co-prime?", "Yes. Their only common factor is 1."),
  ("Express 20 as a sum of two primes in two ways.", "3 + 17 and 7 + 13."),
  ("Which method do you use to cut ropes into equal pieces of greatest length?", "HCF of the rope lengths."),
  ("Two bells ring every 12 and 15 minutes. After how long do they ring together?", "LCM = 60 minutes."),
 ]),
 ],
 takeaways=["A **factor** divides exactly; a **multiple** is got by multiplying. Factors are finite, multiples are infinite.",
  "**Prime:** exactly two factors; **composite:** more than two; **1** is neither; **2** is the only even prime; there are 25 primes below 100 (found with the **sieve**).",
  "**Co-primes** have HCF 1 (they need not be prime); **twin primes** differ by 2.",
  "Every number has a **unique prime factorisation** (use a factor tree), e.g. 84 = 2² × 3 × 7.",
  "Test divisibility by a composite number through **co-prime factors**; rule of 11 uses the difference of alternate digit sums.",
  "**HCF** = common primes with smallest powers; **LCM** = all primes with greatest powers; for two numbers HCF × LCM = their product.",
  "Use **HCF** for cutting, tiling, grouping into equal parts (largest size); use **LCM** for events that repeat and meet again (smallest time), and LCM + remainder for ‘leaves remainder’ problems."])

if __name__ == "__main__": run(__file__, BANK, 6, "Maths", WS, CH)
