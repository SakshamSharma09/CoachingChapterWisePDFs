from math import gcd
from lib import mcq, Q, OR
from mk9 import M4, build
def lcm(a, b): return a * b // gcd(a, b)
def factors(n): return [d for d in range(1, n + 1) if n % d == 0]
def pf(n):
    out = []; d = 2
    while n > 1:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out
def fmt(l): return " × ".join(map(str, l))
A = [
 M4("A number having exactly two factors, 1 and itself, is:", "a prime number", ["a composite number", "an even number", "a co-prime"], "definition"),
 M4("The number 1 is:", "neither prime nor composite", ["prime", "composite", "even"], "only one factor"),
 M4("The only even prime number is:", "2", ["4", "1", "0"], "two factors"),
 M4("Which of these is a prime number?", "29", ["27", "33", "39"], "no other factors"),
 M4("Which of these is a composite number?", "51", ["47", "53", "59"], "51 = 3 × 17"),
 M4("Two numbers whose only common factor is 1 are:", "co-prime", ["twin primes", "composite", "equal"], "e.g. 8 and 15"),
 M4("Which pair is co-prime?", "14 and 15", ["14 and 21", "12 and 18", "10 and 25"], "HCF is 1"),
 M4("The process of writing a number as a product of primes is:", "prime factorisation", ["division", "estimation", "rounding"], "definition"),
 M4("The method used to find all primes up to 100 by crossing out multiples is the:", "Sieve of Eratosthenes", ["Collatz routine", "Kaprekar routine", "Pascal's method"], "ancient method"),
 M4("A number is divisible by 2 if its last digit is:", "0, 2, 4, 6 or 8", ["1, 3, 5, 7, 9", "0 or 5 only", "any digit"], "even"),
 M4("A number is divisible by 3 if:", "the sum of its digits is divisible by 3", ["its last digit is 3", "it is even", "its last two digits are 33"], "digit sum rule"),
 M4("A number is divisible by 9 if:", "the sum of its digits is divisible by 9", ["it ends in 9", "it is odd", "it has two 9s"], "digit sum rule"),
 M4("A number is divisible by 5 if its last digit is:", "0 or 5", ["1 or 5", "2 or 5", "5 or 7"], "rule"),
 M4("A number is divisible by 10 if its last digit is:", "0", ["5", "1", "any"], "rule"),
 M4("A number is divisible by 4 if its last two digits form a number divisible by:", "4", ["2", "3", "5"], "rule"),
 M4("A number is divisible by 6 if it is divisible by:", "both 2 and 3", ["2 or 3", "both 4 and 3", "5 and 2"], "6 = 2 × 3"),
 M4("The smallest prime number is:", "2", ["1", "3", "0"], "first prime"),
 M4("The number of primes between 1 and 20 is:", "8", ["7", "9", "10"], "2,3,5,7,11,13,17,19"),
 M4("Twin primes are primes that differ by:", "2", ["1", "3", "4"], "e.g. 11 and 13"),
 M4("Which pair is a twin prime pair?", "17 and 19", ["13 and 17", "19 and 23", "23 and 27"], "differ by 2"),
 M4("Every number is a multiple of:", "1 and itself", ["2", "10", "its square"], "basic fact"),
 M4("The HCF is the:", "highest common factor", ["highest common fraction", "half of the common factor", "highest common multiple"], "definition"),
 M4("The LCM is the:", "least common multiple", ["last common multiple", "largest common multiple", "least common factor"], "definition"),
 M4("The prime factorisation of 12 is:", "2 × 2 × 3", ["2 × 6", "3 × 4", "2 × 3 × 3"], "all primes"),
 M4("Prime factors of 30 are:", "2, 3, 5", ["2, 3, 6", "1, 2, 15", "3, 10"], "30 = 2×3×5"),
 M4("The smallest 2-digit prime is:", "11", ["10", "13", "17"], "first prime ≥ 10"),
 M4("The largest 2-digit prime is:", "97", ["99", "98", "91"], "99, 98 and 91 are not prime"),
 M4("The smallest composite number is:", "4", ["2", "3", "6"], "2 × 2"),
 M4("The factors of a number are always:", "less than or equal to the number", ["greater than the number", "odd only", "primes only"], "property"),
]
for a, b in [(12, 18), (8, 20), (15, 25), (14, 21), (16, 24), (18, 30), (9, 12), (10, 35)]:
    g = gcd(a, b)
    A.append(M4(f"The HCF of {a} and {b} is:", str(g), [str(g * 2), str(g + 1), str(max(g - 1, 1))] if g > 1 else ["2", "3", "4"], f"common factors of {a} and {b}"))
for a, b in [(4, 6), (6, 8), (3, 5), (10, 15)]:
    l = lcm(a, b)
    A.append(M4(f"The LCM of {a} and {b} is:", str(l), [str(l + a), str(a * b * 2), str(l - b)], f"smallest common multiple of {a} and {b}"))
for n in (36, 60):
    pass
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Define a prime number. Give three examples.", "A number with exactly two factors, 1 and itself; 2, 3, 5.", "1+1"),
 Q("List the factors of 24.", "1, 2, 3, 4, 6, 8, 12, 24.", "1+1"),
 Q("Write the first five multiples of 7.", "7, 14, 21, 28, 35.", "1+1"),
 Q("Find the HCF of 18 and 24.", "6.", "1+1"),
 Q("Find the LCM of 4 and 10.", "20.", "1+1"),
 Q("What are co-prime numbers? Give an example.", "Numbers with common factor only 1; 9 and 10.", "1+1"),
 Q("Is 91 prime? Give reason.", "No; 91 = 7 × 13.", "1+1"),
 Q("Write the prime factorisation of 36.", "$2\\times2\\times3\\times3$.", "1+1"),
 Q("State the divisibility rule of 11.", "The difference between the sum of alternate digits is 0 or a multiple of 11.", "1+1"),
 Q("Is 2,134 divisible by 3? Give reason.", "Digit sum 10 is not divisible by 3, so no.", "1+1"),
 Q("What are twin primes? Give a pair.", "Two primes with a difference of 2; 5 and 7.", "1+1"),
 Q("Why is 1 neither prime nor composite?", "It has only one factor.", "1+1"),
 Q("List the prime numbers between 20 and 40.", "23, 29, 31, 37.", "1+1"),
 Q("Is 128 divisible by 4? Show by the rule.", "Yes; last two digits 28 are divisible by 4.", "1+1"),
 Q("Write all the factors of 17.", "1 and 17.", "1+1"),
 Q("Find the smallest number divisible by both 6 and 8.", "24.", "1+1"),
]
C = [
 Q("Find the prime factorisation of 84 and 126 and their HCF.", "84 = 2×2×3×7; 126 = 2×3×3×7 (2); HCF = 42 (1).", "2+1"),
 Q("Explain the Sieve of Eratosthenes in steps.", "Write numbers 1 to 100 (1); cross out 1 and multiples of 2, 3, 5, 7 keeping the prime (1); remaining numbers are primes (1).", "1+1+1"),
 Q("Find the LCM of 12 and 18 using prime factorisation.", "12 = 2²×3; 18 = 2×3² (1.5); LCM = 2²×3² = 36 (1.5).", "1½+1½"),
 Q("Using divisibility tests, check whether 3,456 is divisible by 2, 3, 4, 6 and 9.", "Divisible by 2, 3 (digit sum 18), 4 (last two digits 56), 6 and 9 (3).", "1+2"),
 Q("Write all primes less than 30 and state how many there are.", "2, 3, 5, 7, 11, 13, 17, 19, 23, 29 (2); 10 primes (1).", "2+1"),
 Q("Explain with an example why two consecutive numbers are always co-prime.", "Any common factor of n and n+1 divides their difference 1 (1.5); e.g. 8 and 9 are co-prime (1.5).", "1½+1½"),
 Q("A rope of 48 m and another of 36 m are cut into equal pieces of the longest possible length. Find the length.", "HCF of 48 and 36 = 12 (1); the pieces are 12 m (2).", "1+2"),
 Q("Three bells ring every 6, 8 and 12 minutes. After how many minutes will they ring together?", "LCM of 6, 8, 12 = 24 minutes (3).", "1+2"),
 Q("Find the factors of 36 and state how many there are.", "1, 2, 3, 4, 6, 9, 12, 18, 36 (2); 9 factors (1).", "2+1"),
 Q("Express 90 as a product of primes. How many prime factors does it have?", "2 × 3 × 3 × 5 (2); four prime factors (1).", "2+1"),
 Q("Are 35 and 64 co-prime? Find their HCF.", "HCF is 1 (2); so co-prime (1).", "2+1"),
 Q("State and test the divisibility rule of 9 on 7,128.", "Digit sum divisible by 9 (1); 7+1+2+8 = 18, so divisible (2).", "1+2"),
 Q("Write the first 8 multiples of 9. What do you notice about their digit sums?", "9, 18, 27, 36, 45, 54, 63, 72 (2); digit sums are 9 (1).", "2+1"),
 Q("Show that 143 is composite by finding its factors.", "143 = 11 × 13 (3).", "1+2"),
 Q("What is the smallest number that leaves remainder 1 when divided by 2, 3 and 4?", "LCM 12 + 1 = 13 (3).", "1+2"),
 Q("Find the smallest 3-digit number divisible by 9.", "108 (digit sum 9) (3).", "1+2"),
 Q("Explain: every even number greater than 2 is composite.", "It has 2 as a factor besides 1 and itself (3).", "1+2"),
 Q("Write the prime factorisation of 100 using a factor tree.", "100 → 10 × 10 → 2×5×2×5 = 2²×5² (3).", "1+2"),
 Q("Find the HCF of 36, 48 and 60.", "12 (3).", "1+2"),
 Q("Which of 221, 223, 225 are prime? Give reasons.", "223 is prime; 221 = 13 × 17; 225 = 15 × 15 (3).", "1+2"),
 Q("Express 20 as the sum of two primes in two different ways.", "3 + 17 and 7 + 13 (3).", "1+2"),
 Q("A number is divisible by both 4 and 6. Is it divisible by 24? Explain with an example.", "Not always; 12 is divisible by 4 and 6 but not 24 (3).", "1+2"),
 Q("Why is the divisibility rule of 3 true for 123? Verify.", "Digit sum 6 is divisible by 3; 123 = 3 × 41 (3).", "1+2"),
 Q("What are the different kinds of numbers: prime, composite, co-prime, twin primes? Give an example each.", "Prime 7; composite 12; co-prime 8, 9; twin primes 11, 13 (3).", "1+2"),
]
D = [
 Q("(i) Find the prime factorisation of 180. (ii) Find its number of factors. (iii) List all its factors.", "(i) 2²×3²×5 (2). (ii) 18 (1.5). (iii) 1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 30, 36, 45, 60, 90, 180 (1.5).", "2+1½+1½"),
 Q("(i) Find the HCF and LCM of 24 and 36 by prime factorisation. (ii) Verify HCF × LCM = product.", "(i) 24 = 2³×3, 36 = 2²×3²; HCF = 12, LCM = 72 (3). (ii) 12 × 72 = 864 = 24 × 36 (2).", "3+2"),
 Q("(i) State the divisibility tests for 2, 3, 4, 5, 6, 9, 10. (ii) Test 5,940.", "(i) Rules (3). (ii) Divisible by 2, 3, 4, 5, 6, 9, 10 (2).", "3+2"),
 Q("<b>Case study:</b> A teacher has 36 pencils and 48 erasers to pack equally into the largest number of kits without leftovers. (i) How many kits? (ii) Pencils in each? (iii) Erasers in each? (iv) Which concept is used?", "(i) HCF = 12 kits (1). (ii) 3 (1). (iii) 4 (1). (iv) HCF (2).", "1+1+1+2"),
 Q("(i) List the prime numbers from 1 to 50. (ii) How many are there? (iii) Find the twin primes among them.", "(i) 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 (2). (ii) 15 (1). (iii) (3,5), (5,7), (11,13), (17,19), (29,31), (41,43) (2).", "2+1+2"),
 Q("(i) Explain co-prime numbers. (ii) Which pairs are co-prime: (21, 22), (18, 27), (35, 36), (14, 49)? (iii) Give a real-life use.", "(i) HCF 1 (1). (ii) (21,22) and (35,36) (2). (iii) Gear teeth / safe locks (2).", "1+2+2"),
 Q("<b>Case study:</b> Two traffic lights turn green every 40 s and 60 s starting together. (i) After how many seconds do they turn green together again? (ii) How many times in 10 minutes? (iii) Which concept is used? (iv) If the periods were 7 s and 9 s?", "(i) LCM = 120 s (1). (ii) 5 times after the start (1). (iii) LCM (1). (iv) 63 s (2).", "1+1+1+2"),
 Q("(i) Explain the Sieve of Eratosthenes. (ii) List primes up to 30 obtained.", "(i) Process (3). (ii) 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 (2).", "3+2"),
 Q("(i) Find the LCM of 15, 20 and 25. (ii) The smallest number divisible by all three. (iii) Test 300 for divisibility by 15, 20, 25.", "(i) 300 (2). (ii) 300 (1). (iii) Divisible by all (2).", "2+1+2"),
 Q("<b>Case study:</b> A gardener plants saplings in rows. He has 84 saplings. (i) In how many ways can he arrange them in equal rows? (ii) List the possible rows. (iii) Why can't 83 saplings be arranged in rows other than one row or 83 rows? (iv) Which type of number is 83?", "(i) 12 ways (6 pairs) (1). (ii) 1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84 (1). (iii) 83 has only two factors (1). (iv) Prime (2).", "1+1+1+2"),
 Q("(i) Why is 2 the only even prime? (ii) Is the sum of two primes always even? (iii) Give an example.", "(i) All other evens have 2 as a factor (2). (ii) No (1). (iii) 2 + 3 = 5 (2).", "2+1+2"),
 Q("(i) Find the smallest number that when divided by 8, 12, 15 leaves no remainder. (ii) Find the smallest number that leaves remainder 5 each time.", "(i) LCM = 120 (2.5). (ii) 125 (2.5).", "2½+2½"),
 Q("(i) What is a composite number? (ii) Write the composite numbers between 20 and 30. (iii) Factorise each.", "(i) More than two factors (1). (ii) 20, 21, 22, 24, 25, 26, 27, 28 (2). (iii) Correct factorisations (2).", "1+2+2"),
 Q("(i) Use divisibility rules to check 1,331 for 11. (ii) Check 4,367. (iii) Explain the rule.", "(i) Divisible by 11 (alternate digit sums 1+3 and 3+1 equal) (2). (ii) Not divisible (2). (iii) Alternate digit sum difference (1).", "2+2+1"),
 Q("(i) Why do we use prime factorisation? (ii) Express 252 and 420 as prime products. (iii) Find their HCF.", "(i) Helps HCF, LCM (1). (ii) 252 = 2²×3²×7; 420 = 2²×3×5×7 (2). (iii) 84 (2).", "1+2+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 15, (len(B), len(C), len(D))
D.append(Q("(i) Show that 13 is prime. (ii) Check 91 and 87 for primality. (iii) Which numbers up to 100 can be quickly ruled out?", "(i) No divisor other than 1 and 13 (1). (ii) 91 = 7×13; 87 = 3×29 (2). (iii) Even numbers and multiples of 3, 5, 7 (2).", "1+2+2"))
SETS, POOL = build(A, B, C, D)
