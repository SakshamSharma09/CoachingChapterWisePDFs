"""Class 8 Maths Ch 1 A Square and a Cube - extras."""
from common import AR4, Q

AR = [
 AR4(r"The number 1296 is a perfect square.", r"A number is a perfect square if every prime in its prime factorisation occurs an even number of times.", "a",
     r"$1296=2^4\times3^4$, every exponent is even, so it is a perfect square ($36^2$); R is the test that explains it."),
 AR4(r"The square of an even number is always even.", r"The sum of the first $n$ odd natural numbers is $n^2$.", "b",
     r"$(2k)^2=4k^2$ is even, so A is true; R is also true ($1+3+5=9=3^2$) but it does not explain A."),
 AR4(r"The cube of a negative integer is negative.", r"The cube of every integer is positive.", "c",
     r"$(-3)^3=-27$ so A is true; R is false because cubes of negative integers are negative."),
 AR4(r"The number 392 is a perfect cube.", r"A number is a perfect cube if every prime in its prime factorisation has an exponent that is a multiple of 3.", "d",
     r"$392=2^3\times7^2$; the exponent of 7 is 2, so 392 is not a perfect cube. A is false, R is true."),
 AR4(r"The number of non-square numbers between $20^2$ and $21^2$ is 40.", r"There are $2n$ non-square numbers between $n^2$ and $(n+1)^2$.", "a",
     r"Between 400 and 441 are the numbers 401 to 440, that is 40 numbers, and $2\times20=40$; R gives the rule."),
 AR4(r"The cube root of $-27$ is $-3$.", r"A negative number has no cube root.", "c",
     r"$(-3)^3=-27$, so A is true; R is false because negative numbers do have (negative) cube roots."),
]

CASE = [
 Q(r"<b>Case study.</b> Ramesh, a gardener in Jaipur, is given a square plot of area 1764 m$^2$ to plant a lawn and fence it. He wants to find its dimensions using prime factorisation. "
   r"(i) Express 1764 as a product of prime factors. (ii) Find the side of the plot. (iii) Find the cost of fencing all four sides at ₹50 per metre. (iv) The owner decides to increase the side to 45 m. Find the extra area added.",
   r"(i) $1764=2^2\times3^2\times7^2$ (1). (ii) Side $=2\times3\times7=42$ m (1). (iii) Perimeter $=4\times42=168$ m; cost $=168\times50=$ ₹8,400 (1). (iv) New area $=45^2=2025$ m$^2$; extra area $=2025-1764=261$ m$^2$ (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Mohan, a shopkeeper in Indore, packs sweets in a cubical box of volume 2744 cm$^3$. He also has 1350 cm$^3$ of clay that he wants to mould into a cube. "
   r"(i) Find the edge of the box. (ii) Find the total surface area of the box. (iii) How many cubes of edge 2 cm fit in the box? (iv) Find the smallest number by which 1350 must be multiplied so that the product is a perfect cube, and the edge of that cube.",
   r"(i) $2744=2^3\times7^3$, edge $=14$ cm (1). (ii) $6\times14^2=1176$ cm$^2$ (1). (iii) $2744\div8=343$ cubes (1). (iv) $1350=2\times3^3\times5^2$; multiply by $2^2\times5=20$ (1); product $27000=30^3$, edge 30 cm (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Meera notices that $1+3+5+7+9+11+13=49$. She wonders if odd numbers can help her decide whether a number is a perfect square. Her teacher also gives her the number 2000. "
   r"(i) How many odd numbers were added to get 49? (ii) Find the sum of the first 15 odd natural numbers. (iii) Is 2000 a perfect square? Give a reason. (iv) Find the smallest number by which 2000 must be divided to get a perfect square, and the square root of the quotient.",
   r"(i) 7 odd numbers, since the sum is $7^2$ (1). (ii) $15^2=225$ (1). (iii) No; $2000=2^4\times5^3$, the prime 5 occurs an odd number of times (1). (iv) Divide by 5 (1); quotient $400$ and $\sqrt{400}=20$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Squares and square roots", [
   r"A perfect square is $n^2$ for a natural number $n$; its units digit is 0, 1, 4, 5, 6 or 9 only.",
   r"A number is a perfect square if every prime factor occurs an even number of times.",
   r"$1+3+5+\dots+(2n-1)=n^2$ (sum of the first $n$ odd numbers).",
   r"$(n+1)^2-n^2=2n+1$; there are $2n$ non-square numbers between $n^2$ and $(n+1)^2$.",
   r"Square root by prime factorisation: pair equal primes and take one from each pair; $\sqrt{a\times b}=\sqrt a\times\sqrt b$."]),
 ("Patterns with squares", [
   r"$(2n)^2$ is even and $(2n+1)^2$ is odd; a perfect square ends in an even number of zeros.",
   r"$\sqrt{\dfrac{a}{b}}=\dfrac{\sqrt a}{\sqrt b}$; a square of a number ending in 5 ends in 25."]),
 ("Cubes and cube roots", [
   r"A perfect cube is $n^3$; every prime factor occurs a multiple of 3 times.",
   r"Cube root by prime factorisation: group equal primes in triples, take one from each triple.",
   r"$\sqrt[3]{-a}=-\sqrt[3]{a}$; the cube of a negative number is negative; $\sqrt[3]{ab}=\sqrt[3]{a}\,\sqrt[3]{b}$.",
   r"Cube of side $a$: volume $a^3$, surface area $6a^2$."]),
 ("Special numbers", [
   r"$1729=1^3+12^3=9^3+10^3$ is the smallest number expressible as the sum of two cubes in two ways (Ramanujan's taxicab number).",
   r"To make $n$ a perfect square (or cube): multiply or divide by the primes that have an odd (or non-multiple-of-3) exponent."]),
]

MISTAKES = [
 r"Concluding that a number is a perfect square from its last digit alone: a units digit of 0, 1, 4, 5, 6 or 9 is only <i>necessary</i>, not sufficient.",
 r"Pairing primes for a perfect cube: grouping them in <b>pairs</b> (square-root rule) instead of <b>triples</b>.",
 r"Writing $\sqrt{a+b}=\sqrt a+\sqrt b$ or $(a+b)^2=a^2+b^2$.",
 r"Mixing up $2^3$ with $2\times3$ or $3^2$ with $3\times2$; $4^3=64$, not 12.",
 r"Saying the cube root of $-8$ does not exist; it is $-2$ because $(-2)^3=-8$.",
 r"Multiplying or dividing by the wrong prime when making a number a perfect square or cube, instead of looking only at the primes with an incorrect exponent.",
]
