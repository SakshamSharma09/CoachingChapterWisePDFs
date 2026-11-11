"""Class 10 Maths Ch 1 Real Numbers - Hard-tier extras (assertion-reason, case-based), formula sheet, mistakes box."""
from common import AR4, Q

AR = [
 AR4("The HCF of 12 and 18 is 6 and their LCM is 36.", "For two positive integers a and b, HCF(a, b) x LCM(a, b) = a x b.", "a",
     "HCF x LCM = 6 x 36 = 216 = 12 x 18, and R is the general result used to find the LCM."),
 AR4("The number $5 - 2\\sqrt{3}$ is irrational.", "The sum of a rational number and an irrational number is irrational.", "a",
     "5 is rational and $2\\sqrt3$ is irrational, so the difference is irrational; R explains it."),
 AR4("$\\sqrt{2}\\times\\sqrt{8}$ is a rational number.", "The product of two irrational numbers is always irrational.", "c",
     "$\\sqrt2\\times\\sqrt8=\\sqrt{16}=4$ is rational, so A is true; R is false (this is a counter-example)."),
 AR4("The decimal expansion of $\\dfrac{7}{80}$ is terminating.", "The denominator 80 = $2^4\\times5$ has no prime factor other than 2 and 5.", "a",
     "A rational number whose denominator (in lowest terms) is of the form $2^m5^n$ has a terminating decimal expansion."),
 AR4("If two numbers are co-prime, their LCM equals their product.", "The HCF of two co-prime numbers is 1.", "a",
     "LCM = (product)/HCF = product when HCF = 1."),
 AR4("The number $6^n$ can end with the digit 0 for some natural number n.", "A number ends with 0 only if it is divisible by both 2 and 5.", "d",
     "$6^n=2^n3^n$ has no factor 5, so it never ends in 0; A is false, R is true."),
]

CASE = [
 Q("<b>Case study.</b> A school is arranging chairs for the annual day. There are 144 chairs in the front block and 180 chairs in the back block. The teacher wants to arrange each block in rows so that every row has the same number of chairs, and every row in both blocks has equal length. "
   "(i) Express 144 and 180 as products of prime factors. (ii) Find the greatest possible number of chairs in each row. (iii) How many rows will there be in all? (iv) The coordinator proposes one more block of 216 chairs with the same rule. Find the greatest row length that works for all three blocks and the total number of rows.",
   "(i) $144=2^4\\times3^2$, $180=2^2\\times3^2\\times5$ (1). (ii) HCF = $2^2\\times3^2=36$ chairs per row (1). (iii) Rows: $144/36+180/36=4+5=9$ (1). (iv) $216=2^3\\times3^3$; HCF(144, 180, 216) = $2^2\\times3^2=36$ (1); rows $=4+5+6=15$ (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Two runners start together from the same point of a circular track. Aman takes 36 seconds and Bhavna takes 48 seconds to complete one round, and both keep a constant pace. "
   "(i) Write 36 and 48 in prime factorised form. (ii) After how many seconds will they meet again at the starting point? (iii) How many rounds will each have completed by then? (iv) A third runner, Chetan, takes 60 seconds per round. After how many seconds will all three meet again at the starting point, and how many rounds will Chetan have run?",
   "(i) $36=2^2\\times3^2$, $48=2^4\\times3$ (1). (ii) LCM = $2^4\\times3^2=144$ s (1). (iii) Aman: $144/36=4$ rounds; Bhavna: $144/48=3$ rounds (1). (iv) $60=2^2\\times3\\times5$; LCM(36, 48, 60) = $2^4\\times3^2\\times5=720$ s (1); Chetan: $720/60=12$ rounds (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A teacher gives the class the numbers $\\dfrac{13}{125}$, $\\dfrac{17}{18}$ and $\\dfrac{29}{343}$ and asks students to decide the nature of their decimal expansions without dividing. "
   "(i) Write the denominator of $\\dfrac{13}{125}$ in prime factors. (ii) State the condition on the denominator for a rational number to have a terminating decimal expansion. (iii) Which of the three numbers have terminating expansions? (iv) Find the decimal expansion of $\\dfrac{13}{125}$ and state, with reason, whether $\\dfrac{17}{18}$ terminates.",
   "(i) $125=5^3$ (1). (ii) In lowest terms the denominator must be of the form $2^m5^n$ (1). (iii) Only $\\dfrac{13}{125}$ terminates; $18=2\\times3^2$ and $343=7^3$ contain primes other than 2 and 5 (1). (iv) $\\dfrac{13}{125}=\\dfrac{13\\times8}{1000}=0.104$ (1); $\\dfrac{17}{18}$ does not terminate because its denominator has the prime factor 3 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Fundamental Theorem of Arithmetic", ["Every composite number can be expressed as a product of primes, and this factorisation is unique apart from the order of the primes.",
   "Example: $360=2^3\\times3^2\\times5$."]),
 ("HCF and LCM by prime factorisation", ["HCF = product of the smallest power of each common prime factor.",
   "LCM = product of the greatest power of each prime factor present in the numbers.",
   "For two positive integers: $\\text{HCF}(a,b)\\times\\text{LCM}(a,b)=a\\times b$ (does not hold for three numbers).",
   "Co-prime numbers: HCF = 1 and LCM = product."]),
 ("Irrational numbers", ["$\\sqrt2,\\ \\sqrt3,\\ \\sqrt5$ and, in general, $\\sqrt p$ for a prime p are irrational.",
   "Rational $\\pm$ irrational = irrational; non-zero rational $\\times$ irrational = irrational.",
   "Sum, difference, product or quotient of two irrationals may be rational or irrational (e.g. $\\sqrt2\\times\\sqrt2=2$)."]),
 ("Decimal expansions of rational numbers", ["$\\dfrac pq$ in lowest terms terminates if $q=2^m5^n$ ($m,n\\ge0$).",
   "Otherwise the decimal expansion is non-terminating and repeating.",
   "Irrational numbers have non-terminating, non-repeating expansions."]),
 ("Method to prove $\\sqrt p$ irrational", ["Assume $\\sqrt p=\\dfrac ab$ with a, b co-prime; then $a^2=pb^2$, so p divides a; write $a=pc$ and show p divides b; contradiction with co-primality."]),
]

MISTAKES = [
 "Using HCF $\\times$ LCM = product for <b>three</b> numbers; the result holds only for two numbers.",
 "Taking the <i>greatest</i> power for HCF or the <i>smallest</i> power for LCM; HCF uses smallest common powers, LCM uses greatest powers.",
 "Checking the denominator before reducing the fraction to lowest terms when testing for a terminating decimal.",
 "Assuming the product (or sum) of two irrational numbers is always irrational: $\\sqrt2\\times\\sqrt2=2$.",
 "In irrationality proofs, forgetting to state that a and b are co-prime at the start, which is what gives the contradiction.",
]
