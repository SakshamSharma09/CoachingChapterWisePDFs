from math import gcd
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def lcm(a, b): return a * b // gcd(a, b)
# A: divisibility by 3 / 9 (6)
for n, d in [(4725, 9), (7314, 3), (8109, 9), (5238, 9), (2461, 3), (6912, 9)]:
    ok = n % d == 0; ds = sum(map(int, str(n)))
    A.append(M4(f"Is {n} divisible by {d}?", "Yes" if ok else "No", ["No" if ok else "Yes", "Only if the last digit is even", "Only if the number is prime"], f"Digit sum {ds} {'is' if ds % d == 0 else 'is not'} divisible by {d}"))
# A: divisibility by 11 (4)
for n in [2728, 8591, 1331, 7062]:
    a = sum(map(int, str(n)[::-2])); b = sum(map(int, str(n)[-2::-2])); ok = (a - b) % 11 == 0
    A.append(M4(f"Is {n} divisible by 11?", "Yes" if ok else "No", ["No" if ok else "Yes", "Only if it is odd", "Only if it ends in 1"], "Difference of sums of alternate digits"))
# A: smallest digit to make divisible (6)
for pre, d in [("47_5", 3), ("52_8", 9), ("36_2", 9), ("81_4", 3), ("2_43", 9), ("6_17", 3)]:
    for x in range(10):
        n = int(pre.replace("_", str(x)))
        if n % d == 0 and x == min(y for y in range(10) if int(pre.replace("_", str(y))) % d == 0): ans = x; break
    wrong = [str((ans + k) % 10) for k in (1, 2, 5)]
    A.append(M4(f"The smallest digit that replaces the blank in {pre} so that the number is divisible by {d} is:", str(ans), wrong, f"Digit sum must be a multiple of {d}"))
# A: LCM/HCF (6)
for a, b in [(12, 18), (8, 20), (15, 25), (14, 21), (16, 24), (9, 12)]:
    A.append(M4(f"The LCM of {a} and {b} is:", str(lcm(a, b)), [str(a*b), str(gcd(a, b)), str(lcm(a, b)+a)], "Smallest common multiple"))
# A: concepts (18)
A += [
 M4("A number is divisible by 4 if the number formed by its last two digits is divisible by:", "4", ["2", "8", "5"], "Rule for 4"),
 M4("A number is divisible by 8 if its last three digits form a number divisible by:", "8", ["4", "2", "5"], "Rule for 8"),
 M4("The smallest number divisible by 2, 3 and 5 is:", "30", ["10", "15", "60"], "LCM"),
 M4("A number is divisible by 6 if it is divisible by:", "both 2 and 3", ["2 and 4", "3 and 9", "5 and 2"], "6 = 2 × 3 (coprime)"),
 M4("Which of these is divisible by 5?", "3475", ["3472", "3471", "3476"], "Ends in 0 or 5"),
 M4("The sum of any two odd numbers is:", "even", ["odd", "prime", "a multiple of 3"], "odd + odd = even"),
 M4("The product of an even and an odd number is:", "even", ["odd", "prime", "a square"], "Property"),
 M4("The Kaprekar constant for four-digit numbers is:", "6174", ["1729", "1089", "1234"], "Repeated rearranging and subtracting"),
 M4("Starting with 3 and subtracting the reverse of its digits repeatedly (Kaprekar), the process for 3-digit numbers ends at:", "495", ["594", "999", "100"], "Kaprekar for 3 digits"),
 M4("A palindromic number reads:", "the same forwards and backwards", ["only forwards", "differently backwards", "as a prime"], "e.g. 12321"),
 M4("The number 1 is:", "neither prime nor composite", ["prime", "composite", "even"], "By convention"),
 M4("The smallest prime number is:", "2", ["1", "3", "0"], "Only even prime"),
 M4("The HCF of 24 and 36 is:", "12", ["6", "24", "72"], "Greatest common factor"),
 M4("If a number is divisible by both 4 and 9, it is also divisible by:", "36", ["13", "18 only", "27"], "Coprime factors"),
 M4("A number ending in 00 is always divisible by:", "100", ["3", "7", "11"], "Ends in two zeros"),
 M4("The digit sum of 9999 is:", "36", ["27", "9", "18"], "9+9+9+9"),
 M4("The number 12345679 × 9 equals:", "111111111", ["123456790", "100000001", "999999999"], "A curious pattern"),
 M4("Which of the following numbers is a perfect number?", "28", ["20", "30", "36"], "28 = 1+2+4+7+14"),
]
assert len(A) == 40, len(A)
B = [
 Q("State the divisibility test for 3.", "A number is divisible by 3 if the sum of its digits is divisible by 3 (2).", "2"),
 Q("State the divisibility test for 11.", "The difference between the sums of digits at odd and even places is 0 or a multiple of 11 (2).", "2"),
 Q("Is 5148 divisible by 4? Explain.", "Last two digits 48 are divisible by 4, so yes (2).", "2"),
 Q("Check whether 7392 is divisible by 8.", "Last three digits 392 $=8\\times49$, so yes (2).", "2"),
 Q("What are co-prime numbers? Give an example.", "Numbers whose HCF is 1 (1); 8 and 15 (1).", "1+1"),
 Q("Find the HCF of 18 and 48.", "Factors: $18=2\\times3^2$, $48=2^4\\times3$ (1); HCF $=6$ (1).", "1+1"),
 Q("Find the LCM of 6, 8 and 12.", "$\\text{LCM}=24$ (2).", "2"),
 Q("What is a palindromic number? Give two examples.", "Reads the same both ways (1); 121 and 4554 (1).", "1+1"),
 Q("Write the Kaprekar process for 3-digit numbers briefly.", "Arrange digits in descending and ascending order, subtract; repeat to reach 495 (2).", "2"),
 Q("Why is 2 the only even prime?", "Every other even number has 2 as a factor besides 1 and itself (2).", "2"),
 Q("Find the digit $x$ if $46x$ is divisible by 9.", "Sum $10+x$ must be 18, so $x=8$ (2).", "2"),
 Q("Solve the cryptarithm: $A+A=10$. Find $A$.", "$A=5$ (2).", "2"),
 Q("What is the sum of the first 10 odd numbers? Which pattern does it follow?", "100 (1); the sum of first $n$ odd numbers is $n^2$ (1).", "1+1"),
 Q("State whether 1001 is divisible by 7, 11 and 13.", "$1001=7\\times11\\times13$, so yes to all (2).", "2"),
 Q("Find the remainder when 245 is divided by 9 using digit sum.", "Digit sum 11, then 2; remainder $=2$ (2).", "2"),
 Q("Is a number divisible by 12 if it is divisible by 3 and 4? Give a reason.", "Yes; 3 and 4 are co-prime and $3\\times4=12$ (2).", "2"),
]
for pre, d in [("5_72", 3), ("3_47", 9), ("8_16", 9), ("7_29", 3), ("4_51", 9), ("9_36", 3)]:
    xs = [x for x in range(10) if int(pre.replace("_", str(x))) % d == 0]
    C.append(Q(f"Find all digits that can replace the blank in {pre} to make it divisible by {d}.", f"Digit sum condition (2); digits: {', '.join(map(str, xs))} (1).", "2+1"))
for a, b, c in [(12, 18, 30), (8, 12, 20), (15, 20, 25), (6, 9, 15), (14, 21, 35), (10, 16, 24)]:
    l = lcm(lcm(a, b), c)
    C.append(Q(f"Find the smallest number divisible by {a}, {b} and {c}.", f"Prime factorise each (1); take the highest powers (1); LCM $={l}$ (1).", "1+1+1"))
C += [
 Q("Explain the test for divisibility by 6 using 2 and 3. Test 4728.", "Even and digit sum 21 is divisible by 3 (2); so divisible by 6 (1).", "2+1"),
 Q("Apply Kaprekar's routine to 3524 until it reaches 6174.", "5432−2345=3087 (1); 8730−0378=8352 (1); 8532−2358=6174 (1).", "1+1+1"),
 Q("Find the missing digit: $3\\,\\square\\,5\\,2$ is divisible by 11.", "Alternate sums: $3+5$ and $\\square+2$ must differ by 0 or 11, so $\\square=6$ (3).", "3"),
 Q("A bell rings every 12 minutes and another every 18 minutes. If both ring together at 8 a.m., when will they next ring together?", "LCM $=36$ (2); at 8:36 a.m. (1).", "2+1"),
 Q("Show that the number formed by writing any digit three times, such as 777, is divisible by 3 and 37.", "$777=3\\times259=3\\times7\\times37$ (3).", "3"),
 Q("The sum of the digits of a two-digit number is 9. Show that the number formed by reversing the digits differs by a multiple of 9.", "Number $10a+b$, reverse $10b+a$, difference $9(a-b)$ (3).", "3"),
]
C += [
 Q("Check the divisibility of 245718 by 2, 3, 4 and 9.", "Even, so divisible by 2 (1); digit sum 27, so divisible by 3 and 9 (1); last two digits 18 are not divisible by 4 (1).", "1+1+1"),
 Q("Find the LCM of 24, 36 and 40 and the HCF of 24 and 36.", "LCM 360 (1.5); HCF 12 (1.5).", "1½+1½"),
 Q("A number leaves remainder 3 when divided by 5, 6 and 8. Find the smallest such number greater than 3.", "LCM $=120$ (2); $123$ (1).", "2+1"),
 Q("Is 20000001 divisible by 11? Show the working.", "Sum of digits at odd places (from the right) $=1$, at even places $=2$ (2); difference 1 is not a multiple of 11, so no (1).", "2+1"),
 Q("Show that a number and the sum of its digits leave the same remainder on division by 9. Verify for 4729.", "Digit sum 22 leaves remainder 4 (1.5); $4729=9\\times525+4$ (1.5).", "1½+1½"),
 Q("Write the first five multiples of 14 and say which are divisible by 4.", "14, 28, 42, 56, 70 (2); 28 and 56 (1).", "2+1"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) State the divisibility tests for 2, 4, 5 and 8. (ii) Test 3,15,000 and 59,32,816 for these.", "(i) Last digit; last two digits; last digit 0/5; last three digits (3). (ii) Appropriate checks (2).", "3+2"),
 Q("(i) Find the HCF and LCM of 84 and 126 by prime factorisation. (ii) Verify HCF × LCM = product.", "(i) $84=2^2\\times3\\times7$, $126=2\\times3^2\\times7$; HCF 42, LCM 252 (3). (ii) $42\\times252=10584=84\\times126$ (2).", "3+2"),
 Q("<b>Case study:</b> Three traffic lights change every 40 s, 60 s and 90 s respectively and all turn green together at 9:00 a.m. (i) After how many seconds will they next change together? (ii) At what time? (iii) How many times will they change together between 9:00 and 10:00, counting both 9:00 and 10:00?", "(i) LCM $=360$ s (2). (ii) 9:06 a.m. (1). (iii) 11 times (2).", "2+1+2"),
 Q("(i) Solve the cryptarithm $AB+BA=121$ for digits $A,B$. (ii) Show that the sum of a two-digit number and its reverse is always a multiple of 11.", "(i) $11(A+B)=121$, $A+B=11$, e.g. 29 and 92 (2). (ii) $11(a+b)$ (3).", "2+3"),
 Q("(i) Apply Kaprekar's routine to 954. (ii) What does the sequence show? (iii) Try 100 and say what happens.", "(i) 954−459=495 (2). (ii) Reaches the constant 495 (1). (iii) 100−001=099; 990−099=891; 981−189=792; 972−279=693; 963−369=594; 954−459=495 (2).", "2+1+2"),
 Q("(i) Find the smallest 4-digit number divisible by 9 and 11. (ii) Find the largest 4-digit number divisible by both.", "(i) LCM 99; $1000\\div99$ gives 1089 (2.5). (ii) $9999=99\\times101$ (2.5).", "2½+2½"),
 Q("<b>Case study:</b> A teacher wants to arrange 144 red and 180 blue flags in equal rows so that each row has flags of one colour only and rows have equal flags. (i) What is the largest number of flags per row? (ii) How many rows of each colour? (iii) Why HCF?", "(i) HCF $=36$ (2). (ii) 4 red and 5 blue rows (2). (iii) Largest equal group (1).", "2+2+1"),
 Q("(i) Show that a number is divisible by 9 iff its digit sum is divisible by 9. (ii) Test 70524.", "(i) $10^k\\equiv1\\pmod9$ so number $\\equiv$ digit sum (3). (ii) Digit sum 18, divisible by 9 (2).", "3+2"),
 Q("(i) Prove that the product of three consecutive integers is divisible by 6. (ii) Verify for 7×8×9.", "(i) One is even and one is a multiple of 3 (3). (ii) $504=6\\times84$ (2).", "3+2"),
 Q("(i) A number has digits 4, 7 and 1 in some order. Form the largest and smallest numbers and subtract. (ii) Repeat the process and reach 495.", "(i) 741−147=594 (2). (ii) 954−459=495 (3).", "2+3"),
 Q("<b>Case study:</b> A museum numbers tickets from 1001 to 1100. (i) How many ticket numbers are divisible by 7? (ii) Which are divisible by 11? (iii) Which ticket is divisible by both?", "(i) 1001, 1008, …, 1099 gives 15 (2). (ii) 1001, 1012, …, 1100 gives 10 (2). (iii) 1001 and 1078 (1).", "2+2+1"),
 Q("(i) Take 854, subtract its reverse, then add the reverse of the difference. (ii) Repeat with 732 and state what you notice.", "(i) 854−458=396; 396+693=1089 (3). (ii) 732−237=495; 495+594=1089, so always 1089 (2).", "3+2"),
 Q("(i) Find the missing digits in $5\\,\\square\\,3\\,\\triangle$ so the number is divisible by 9 and by 5. (ii) Give all such numbers.", "(i) Last digit $\\triangle$ is 0 or 5 (2). (ii) Digit sum $8+\\square+\\triangle$ is a multiple of 9, giving 5130 and 5535 (3).", "2+3"),
 Q("(i) State what a perfect number is. (ii) Show that 6 and 28 are perfect.", "(i) Sum of its proper divisors equals the number (2). (ii) $1+2+3=6$; $1+2+4+7+14=28$ (3).", "2+3"),
 Q("(i) What are twin primes? List the pairs below 50. (ii) Is 91 prime?", "(i) Primes differing by 2: (3,5), (5,7), (11,13), (17,19), (29,31), (41,43) (3). (ii) $91=7\\times13$, not prime (2).", "3+2"),
 Q("<b>Case study:</b> A school bell rings 4 times during an hour at equal gaps of 15 minutes starting at 8:00. (i) What are the ring times? (ii) What is the LCM-based interpretation if another system rings every 20 minutes? (iii) When do they ring together?", "(i) 8:00, 8:15, 8:30, 8:45 (1). (ii) LCM of 15 and 20 is 60 minutes (2). (iii) At 8:00 and 9:00 (2).", "1+2+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
