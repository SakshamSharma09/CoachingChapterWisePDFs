from math import isqrt
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def cube_root(n): return round(n ** (1/3))
# A: perfect squares / non-squares (4)
for ns, pick in [([144, 150, 200, 99], 144), ([225, 230, 250, 300], 225), ([400, 410, 450, 500], 400), ([81, 82, 90, 120], 81)]:
    A.append(M4("Which of the following is a perfect square?", str(pick), [str(x) for x in ns if x != pick], f"${isqrt(pick)}^2={pick}$"))
# A: squares (4)
for n in [13, 17, 25, 36]:
    A.append(M4(f"The value of ${n}^2$ is:", str(n*n), [str(n*2), str(n*n+n), str(n*n-n)], f"${n}\\times{n}={n*n}$"))
# A: square roots (6)
for n in [196, 324, 529, 676, 1089, 1764]:
    r = isqrt(n)
    A.append(M4(rf"$\sqrt{{{n}}}$ is equal to:", str(r), [str(r+1), str(r-1), str(r+2)], f"${r}\\times{r}={n}$"))
# A: odd numbers sum (4)
for n in [8, 12, 15, 20]:
    A.append(M4(f"The sum of the first {n} odd natural numbers is:", str(n*n), [str(n*(n+1)), str(n*n-1), str(2*n)], f"Sum of first $n$ odd numbers $=n^2={n*n}$"))
# A: number of non-squares between consecutive squares (3)
for n in [7, 11, 14]:
    A.append(M4(rf"How many non-square numbers lie between ${n}^2$ and ${n+1}^2$?", str(2*n), [str(2*n+1), str(2*n-1), str(n)], f"There are $2n={2*n}$ numbers between $n^2$ and $(n+1)^2$"))
# A: cubes (4)
for n in [6, 9, 11, 15]:
    A.append(M4(f"The value of ${n}^3$ is:", str(n**3), [str(n*n*3), str(n**3+n), str(n**3-n)], f"${n}\\times{n}\\times{n}={n**3}$"))
# A: cube roots (5)
for n in [343, 729, 1728, 3375, 9261]:
    r = cube_root(n)
    A.append(M4(rf"$\sqrt[3]{{{n}}}$ is:", str(r), [str(r+1), str(r-1), str(r+2)], f"${r}^3={n}$"))
# A: perfect cube identification (3)
for ns, pick in [([125, 130, 150, 200], 125), ([512, 500, 600, 700], 512), ([1000, 900, 800, 1200], 1000)]:
    A.append(M4("Which of the following is a perfect cube?", str(pick), [str(x) for x in ns if x != pick], f"${cube_root(pick)}^3={pick}$"))
# A: concepts (7)
A += [
 M4("The ones digit of a perfect square can never be:", "7", ["1", "4", "9"], "Squares end only in 0, 1, 4, 5, 6 or 9"),
 M4("The number 1729 is famous as the:", "smallest number expressible as the sum of two cubes in two ways", ["largest perfect cube", "smallest perfect square", "sum of first 10 odd numbers"], "$1729=1^3+12^3=9^3+10^3$"),
 M4("The square of an even number is always:", "even", ["odd", "prime", "a multiple of 3"], "even × even = even"),
 M4("The ones digit of $27^2$ is:", "9", ["7", "4", "1"], "$7^2=49$ ends in 9"),
 M4("The cube of a negative number is:", "negative", ["positive", "zero", "always even"], "negative × negative × negative = negative"),
 M4("The smallest number by which 72 must be multiplied to get a perfect square is:", "2", ["3", "6", "4"], "$72=2^3\\times3^2$; one more 2 is needed"),
 M4("The smallest number by which 54 must be multiplied to get a perfect cube is:", "4", ["2", "3", "6"], "$54=2\\times3^3$; $2\\times2$ more"),
]
assert len(A) == 40, len(A)

# B (16)
for n in [24, 35, 48]:
    B.append(Q(rf"Is {n*n} a perfect square? Give its square root.", rf"Yes, ${n*n}={n}\times{n}$, so $\sqrt{{{n*n}}}={n}$.", "1+1"))
for n in [5, 9, 12]:
    B.append(Q(f"Write the sum of the first {n} odd natural numbers without adding.", rf"The sum of the first $n$ odd numbers is $n^2$ (1); so the sum is ${n}^2={n*n}$ (1).", "1+1"))
B += [
 Q("What is a perfect square? Give two examples.", "A number that is the square of a natural number (1); e.g. 16 and 49 (1).", "1+1"),
 Q("What is a perfect cube? Give two examples.", "A number that is the cube of a natural number (1); e.g. 27 and 125 (1).", "1+1"),
 Q("Without calculating, say why 2468 cannot be a perfect square.", "A perfect square cannot end in 2, 3, 7 or 8 (1); 2468 ends in 8 (1).", "1+1"),
 Q("Find the cube root of 2744 by prime factorisation.", r"$2744=2^3\times7^3$ (1); cube root $=2\times7=14$ (1).", "1+1"),
 Q("What is a Pythagorean triplet? Write the triplet that contains 8.", "Three natural numbers $a,b,c$ with $a^2+b^2=c^2$ (1); for example $6,8,10$ (1).", "1+1"),
 Q("Why is 1729 called the Hardy–Ramanujan number?", r"It is the smallest number that is the sum of two cubes in two ways: $1^3+12^3=9^3+10^3$ (2).", "2"),
 Q("How many numbers lie between $15^2$ and $16^2$?", r"$2\times15=30$ numbers lie between them (2).", "2"),
 Q(r"Find $\sqrt{1521}$ by prime factorisation.", r"$1521=3^2\times13^2$ (1); so $\sqrt{1521}=3\times13=39$ (1).", "1+1"),
 Q("State the rule for the number of non-square numbers between $n^2$ and $(n+1)^2$.", r"There are $2n$ such numbers (2).", "2"),
 Q("Write the square of 105 using the pattern for numbers ending in 5.", r"$105^2=(10\times11)\,|\,25=11025$ (2).", "2"),
]
assert len(B) == 16, len(B)

# C (24)
for n in [3375, 5832, 10648, 17576]:
    r = cube_root(n)
    fs = {3375: r"3^3\times5^3", 5832: r"2^3\times3^6", 10648: r"2^3\times11^3", 17576: r"2^3\times13^3"}[n]
    C.append(Q(rf"Find the cube root of {n} by prime factorisation.", rf"${n}={fs}$ (2); cube root $={r}$ (1).", "2+1"))
for n in [2025, 3136, 4624, 7396]:
    r = isqrt(n)
    C.append(Q(rf"Find $\sqrt{{{n}}}$ using prime factorisation.", rf"Factorise {n} into prime pairs (2); the square root is ${r}$ (1).", "2+1"))
C += [
 Q("Find the smallest number by which 180 must be multiplied to make it a perfect square. Also find the square root of the product.", r"$180=2^2\times3^2\times5$ (1); multiply by 5 (1); $900$, $\sqrt{900}=30$ (1).", "1+1+1"),
 Q("Find the smallest number by which 500 must be divided to make it a perfect cube.", r"$500=2^2\times5^3$ (1); divide by $4$ (1); quotient $125=5^3$ (1).", "1+1+1"),
 Q("Express 64 as the sum of consecutive odd numbers starting with 1.", r"$64=8^2$ (1); so the sum of the first 8 odd numbers (1): $1+3+5+7+9+11+13+15$ (1).", "1+1+1"),
 Q("Find a Pythagorean triplet whose smallest member is 9.", r"For odd $m$, triplet $(m,\tfrac{m^2-1}2,\tfrac{m^2+1}2)$ (1); $m=9$ gives $40$ and $41$ (1); $9^2+40^2=41^2$ (1).", "1+1+1"),
 Q("A square garden has area 1296 m². Find its side. How much fencing is needed for the boundary?", r"Side $=\sqrt{1296}=36$ m (2); perimeter $=4\times36=144$ m (1).", "2+1"),
 Q("A cubical tank holds 13824 litres (1 m³ = 1000 L). Find the length of its edge.", r"Volume $=13.824$ m³ (1); edge $=\sqrt[3]{13.824}=2.4$ m (2).", "1+2"),
 Q("Show that the sum of two consecutive triangular numbers is a perfect square. Verify for 10 and 15.", r"$T_n+T_{n+1}=(n+1)^2$ (1); $10+15=25=5^2$ (1); also $6+10=16$ (1).", "1+1+1"),
 Q("Observe the pattern: $1^2=1$, $11^2=121$, $111^2=12321$. Predict $1111^2$ and $11111^2$.", "The digits rise to the number of ones, then fall back (1); $1111^2=1234321$ (1); $11111^2=123454321$ (1).", "1+1+1"),
 Q("Find the square of 78 using $(a+b)^2$ with $a=80,\\,b=-2$.", r"$(80-2)^2=6400-320+4$ (2); $=6084$ (1).", "2+1"),
 Q("Is 1372 a perfect cube? If not, by which smallest number should it be multiplied to make it one?", r"$1372=2^2\times7^3$ (1); not a cube since $2^2$ is not a triple (1); multiply by 2 (1).", "1+1+1"),
 Q("Find the least square number divisible by each of 6, 8 and 12.", r"LCM $=24=2^3\times3$ (1); need $2^4\times3^2$ (1); least square $=144$ (1).", "1+1+1"),
 Q("Is 1620 a perfect square? Use prime factorisation to decide.", r"$1620=2^2\times3^4\times5$ (2); 5 has no pair, so it is not a perfect square (1).", "2+1"),
 Q("Write the cubes of the first five natural numbers and state which are odd.", "1, 8, 27, 64, 125 (2); odd cubes are 1, 27, 125 (1).", "2+1"),
 Q("Compare the growth of squares and cubes: which is larger for 12, $12^2$ or $12^3$? By how much?", r"$12^2=144$, $12^3=1728$ (2); difference $1584$ (1).", "2+1"),
 Q("Why does a perfect square have an odd number of factors? Illustrate with 36.", "Factors pair up except the square root (1.5); 36 has 9 factors: 1, 2, 3, 4, 6, 9, 12, 18, 36 (1.5).", "1½+1½"),
]
C.append(Q("Find the smallest square number divisible by 10, 15 and 20.", r"LCM $=60=2^2\times3\times5$ (1); need $2^2\times3^2\times5^2$ (1); square $=900$ (1).", "1+1+1"))
C = C[:24]
assert len(C) == 24, len(C)

# D (16)
for lo, hi in [(10, 12), (20, 21)]:
    pass
D += [
 Q(r"(i) Show that $1+3+5+7+9+11=6^2$. (ii) Find the sum of the first 25 odd numbers. (iii) Which number's square is the sum of the first 40 odd numbers?", r"(i) $1+3+5+7+9+11=36$ (2). (ii) $25^2=625$ (1.5). (iii) $40^2=1600$ so 40 (1.5).", "2+1½+1½"),
 Q(r"(i) Find $\sqrt{7569}$ by prime factorisation. (ii) Find the least number to multiply 7569 to get a perfect cube.", r"(i) $7569=3^2\times29^2$, root $87$ (2.5). (ii) $3^2\times29^2$ needs $3\times29$ for a cube, i.e. $87$ (2.5).", "2½+2½"),
 Q(r"(i) Find the cube root of 12167. (ii) Find the smallest number to divide 3240 to make it a perfect cube.", r"(i) $12167=23^3$, root $23$ (2). (ii) $3240=2^3\times3^4\times5$; divide by $3\times5=15$ to get $216$ (3).", "2+3"),
 Q("<b>Case study:</b> A school hall is a square with side 24 m and is to be tiled with square tiles of side 0.5 m. (i) Find the area of the hall. (ii) How many tiles are needed? (iii) If a cube-shaped water tank has edge 1.5 m, find its volume in litres.", r"(i) $24^2=576$ m² (1). (ii) tile area $0.25$; $576/0.25=2304$ tiles (2). (iii) $1.5^3=3.375$ m³ $=3375$ litres (2).", "1+2+2"),
 Q(r"(i) Write the Pythagorean triplets obtained from $m=5$, $7$ and $9$ using $(m,\tfrac{m^2-1}2,\tfrac{m^2+1}2)$. (ii) Verify one of them.", r"(i) $(5,12,13)$, $(7,24,25)$, $(9,40,41)$ (3). (ii) $5^2+12^2=25+144=169=13^2$ (2).", "3+2"),
 Q(r"(i) Prove that $n^3$ can be written as the sum of $n$ consecutive odd numbers; show it for $n=4$. (ii) Write $5^3$ in this way.", r"(i) $4^3=64=13+15+17+19$ (3). (ii) $125=21+23+25+27+29$ (2).", "3+2"),
 Q("<b>Case study:</b> Hardy visited Ramanujan in hospital and mentioned that his taxi number was 1729. Ramanujan said it is a very interesting number. (i) Why is 1729 interesting? (ii) Express it as a sum of two cubes in both ways. (iii) Verify each sum.", r"(i) Smallest number that is the sum of two cubes in two different ways (1). (ii) $1^3+12^3$ and $9^3+10^3$ (2). (iii) $1+1728=1729$; $729+1000=1729$ (2).", "1+2+2"),
 Q(r"(i) Find the square root of $\dfrac{441}{784}$. (ii) Find $\sqrt[3]{\dfrac{343}{1728}}$.", r"(i) $\frac{21}{28}=\frac34$ (2.5). (ii) $\frac{7}{12}$ (2.5).", "2½+2½"),
 Q(r"(i) Find the square of 995 using $(1000-5)^2$. (ii) Find $97^2$ using $(100-3)^2$.", r"(i) $10^6-10000+25=990025$ (2.5). (ii) $10000-600+9=9409$ (2.5).", "2½+2½"),
 Q("(i) State three properties of square numbers. (ii) Verify each with an example.", "(i) Ones digit restrictions; square of even is even and of odd is odd; $n^2-(n-1)^2=2n-1$ (3). (ii) Examples such as $12^2=144$, $13^2=169$, $9^2-8^2=17$ (2).", "3+2"),
 Q(r"A rectangular field of area $1176$ m² has length and breadth in the ratio $3:2$. Find its sides and the cost of fencing at ₹20 per metre.", r"Let sides $3x,2x$: $6x^2=1176$ (2); $x^2=196$, $x=14$ (2); sides $42$ m and $28$ m (1). Perimeter $140$ m, so fencing costs ₹2800.", "2+2+1"),
 Q(r"(i) Show that $\sqrt{a}\times\sqrt{b}=\sqrt{ab}$ using $a=36$, $b=49$. (ii) Find $\sqrt{2916}$ by factorisation.", r"(i) $6\times7=42=\sqrt{1764}$ (2). (ii) $2916=2^2\times3^6$, root $=2\times27=54$ (3).", "2+3"),
 Q("<b>Case study:</b> A dance troupe forms a square arrangement with the same number of rows and columns. There are 1225 dancers. (i) How many rows? (ii) If 71 more join, can a new square be formed? Explain. (iii) How many must be added to form the next square?", r"(i) $\sqrt{1225}=35$ (1). (ii) 1296 is $36^2$, so yes with $36$ rows (2). (iii) $36^2-35^2=71$ (2).", "1+2+2"),
 Q(r"(i) Estimate $\sqrt{200}$ between consecutive integers. (ii) Find $\sqrt{200}$ to one decimal place using the nearest squares.", r"(i) $14^2=196$, $15^2=225$, so between 14 and 15 (2). (ii) $14.1^2=198.81$; $14.2^2=201.64$; so about $14.1$ (3).", "2+3"),
 Q(r"(i) Find the cube root of $-1728$. (ii) Find $\sqrt[3]{0.027}$ and $\sqrt[3]{\dfrac{27}{125}}$.", r"(i) $-12$ (1.5). (ii) $0.3$ and $\frac35$ (3.5).", "1½+3½"),
 Q(r"(i) State and verify the identity $(a+b)^2-(a-b)^2=4ab$ using $a=9,\ b=4$. (ii) Hence find $13^2-5^2$ using $(a+b)(a-b)$.", r"(i) $169-25=144=4\times36$ (3). (ii) $(13+5)(13-5)=144$ (2).", "3+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
