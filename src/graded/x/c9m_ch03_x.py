"""Class 9 Maths Ch 3 World of Numbers - extras."""
from common import AR4, Q

AR = [
 AR4(r"The number $0.375$ is a rational number.", r"Every terminating decimal can be written in the form $\dfrac pq$ with integers $p, q$ and $q\ne0$.", "a",
     r"$0.375=\dfrac{375}{1000}=\dfrac38$; R is the general reason."),
 AR4(r"The number $\sqrt2$ is irrational.", r"The decimal expansion of an irrational number is non-terminating and non-repeating.", "b",
     r"Both statements are true, but R is a property of irrational numbers and does not prove that $\sqrt2$ is irrational."),
 AR4(r"$(\sqrt3+\sqrt2)(\sqrt3-\sqrt2)=1$ is a rational number.", r"The product of two irrational numbers is always irrational.", "c",
     r"$(\sqrt3)^2-(\sqrt2)^2=3-2=1$, so A is true; R is false because this product is rational."),
 AR4(r"The decimal expansion of $\dfrac17$ is terminating.", r"$\dfrac17=0.\overline{142857}$, a non-terminating repeating decimal.", "d",
     r"A is false because 7 has a prime factor other than 2 and 5; R is true."),
 AR4(r"The number $\dfrac38$ has a terminating decimal expansion.", r"$\dfrac38$ is a rational number.", "b",
     r"$\dfrac38=0.375$ terminates, so A is true; R is true, but not every rational number terminates, so R does not explain A."),
 AR4(r"The number $3+\sqrt5$ is irrational.", r"The sum of a rational number and an irrational number is irrational.", "a",
     r"3 is rational and $\sqrt5$ is irrational, so R applies directly."),
]

CASE = [
 Q(r"<b>Case study.</b> Mrs Gupta writes the fractions $\dfrac{7}{16}$, $\dfrac{5}{12}$ and $\dfrac{11}{25}$ on the board and asks the class to find their decimal expansions. "
   r"(i) Write $\dfrac{7}{16}$ as a decimal. (ii) Write $\dfrac{11}{25}$ as a decimal. (iii) Express the denominator 12 in prime factors. (iv) Which of the three fractions have terminating decimal expansions? Give the reason.",
   r"(i) $\dfrac{7}{16}=0.4375$ (1). (ii) $\dfrac{11}{25}=0.44$ (1). (iii) $12=2^2\times3$ (1). (iv) $\dfrac7{16}$ and $\dfrac{11}{25}$ terminate (1) because $16=2^4$ and $25=5^2$ have only the prime factors 2 and 5; $\dfrac5{12}=0.41\overline6$ does not terminate because $12$ has the factor 3 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Ritu is tiling her courtyard. One square tile has area $2$ m$^2$ and another square tile has area $8$ m$^2$. "
   r"(i) Write the side of the first tile. (ii) Write the side of the second tile in the form $a\sqrt2$. (iii) Find the product of the two sides. (iv) Classify $5+\sqrt2$ as rational or irrational with reason, and find $(\sqrt2+1)(\sqrt2-1)$.",
   r"(i) $\sqrt2$ m (1). (ii) $\sqrt8=2\sqrt2$ m (1). (iii) $\sqrt2\times2\sqrt2=4$ (1). (iv) $5+\sqrt2$ is irrational because it is the sum of a rational and an irrational number (1); $(\sqrt2+1)(\sqrt2-1)=2-1=1$, so the product of two irrational numbers can be rational (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Govind, a merchant, keeps accounts using Brahmagupta's idea that a fortune is positive and a debt is negative. He has 4 debts of Rs 6 each to be recorded. "
   r"(i) Find the total, using the product of a fortune 4 and a debt $-6$. (ii) Find $-7-0$. (iii) Find the product of the two debts $-3$ and $-8$. (iv) Find $(-5)\times(-4)+(-3)\times6$ and say whether the result is a fortune or a debt.",
   r"(i) $4\times(-6)=-24$, a debt of Rs 24 (1). (ii) $-7-0=-7$ (1). (iii) $(-3)\times(-8)=24$, a fortune (1). (iv) $20+(-18)=2$ (1), which is a fortune of 2 (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Rational and irrational numbers", [r"Rational number: $\dfrac pq$ with $p, q$ integers and $q\ne0$. Irrational number: cannot be written in this form (e.g. $\sqrt2,\ \sqrt3,\ \pi$).",
   r"Rational numbers have terminating or non-terminating repeating decimals; irrational numbers have non-terminating, non-repeating decimals.",
   r"$\sqrt p$ is irrational for a prime $p$."]),
 ("Decimal expansions", [r"$\dfrac pq$ in lowest terms terminates if $q=2^m5^n$ ($m,n\ge0$); the number of decimal places is the larger of $m$ and $n$.",
   r"Otherwise the expansion is non-terminating repeating, e.g. $\dfrac13=0.\overline3$.",
   r"Recurring decimal to fraction: for $x=0.\overline{ab}$, $100x-x=ab$, so $x=\dfrac{ab}{99}$; for $x=0.\overline a$, $x=\dfrac a9$."]),
 ("Operations on irrationals", [r"Rational $\pm$ irrational = irrational; non-zero rational $\times$ irrational = irrational.",
   r"Two irrationals can give a rational result: $\sqrt2\times\sqrt8=4$, $\sqrt3\times\sqrt3=3$.",
   r"$\sqrt a\times\sqrt b=\sqrt{ab}$, and $(\sqrt a+\sqrt b)(\sqrt a-\sqrt b)=a-b$ for $a,b>0$."]),
 ("Brahmagupta's rules (fortune $+$, debt $-$)", [r"Fortune $\times$ fortune = fortune; debt $\times$ debt = fortune; fortune $\times$ debt = debt.",
   r"$a-0=a$, $a\times0=0$; zero minus zero is zero."]),
]

MISTAKES = [
 r"Testing the denominator of $\dfrac pq$ for factors 2 and 5 before reducing the fraction to lowest terms.",
 r"Believing the product (or sum) of two irrational numbers is always irrational: $\sqrt2\times\sqrt8=4$.",
 r"Treating $\dfrac{22}{7}$ or $3.14$ as the exact value of $\pi$; both are rational approximations, $\pi$ itself is irrational.",
 r"Saying a decimal is irrational because it is long or non-terminating; a repeating decimal such as $0.\overline{142857}$ is rational.",
 r"Using $0.\overline{ab}=\dfrac{ab}{100}$ instead of $\dfrac{ab}{99}$ when converting a recurring decimal.",
 r"Getting the sign wrong for debt $\times$ debt: the product of two negatives is a fortune (positive).",
]
