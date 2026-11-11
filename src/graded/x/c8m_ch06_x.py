"""Class 8 Maths Ch 6 We Distribute, Yet Things Multiply - extras."""
from common import AR4, Q

AR = [
 AR4(r"$(x+5)^2=x^2+10x+25$.", r"$(a+b)^2=a^2+2ab+b^2$.", "a",
     r"Put $a=x$, $b=5$ in the identity: $x^2+2(x)(5)+25$."),
 AR4(r"$(a-b)^2=(b-a)^2$.", r"$(a+b)(a-b)=a^2-b^2$.", "b",
     r"$(a-b)^2=a^2-2ab+b^2=(b-a)^2$ is true. R is also true but it is a different identity and does not explain A."),
 AR4(r"$(x+3)(x-3)=x^2-9$.", r"$(a+b)^2=a^2+b^2$.", "c",
     r"A is the identity $(a+b)(a-b)=a^2-b^2$; R is false because $(a+b)^2=a^2+2ab+b^2$."),
 AR4(r"$(2x+3)(x+1)=2x^2+3$.", r"In the product of two binomials, each term of one is multiplied by each term of the other.", "d",
     r"$(2x+3)(x+1)=2x^2+2x+3x+3=2x^2+5x+3$, so A is false; R is the correct rule."),
 AR4(r"$49\times51=2499$.", r"$(a+b)(a-b)=a^2-b^2$.", "a",
     r"$49\times51=(50-1)(50+1)=50^2-1^2=2500-1=2499$."),
 AR4(r"$(3x)^2=9x^2$.", r"$(3x)^2=3x^2$.", "c",
     r"$(3x)^2=3x\times3x=9x^2$ so A is true; R is false because the coefficient is also squared."),
]

CASE = [
 Q(r"<b>Case study.</b> A rectangular vegetable plot has length $(x+5)$ m and breadth $(x+2)$ m. A square flower bed beside it has side $(x+3)$ m. "
   r"(i) Write the area of the vegetable plot as an expression. (ii) Find its area when $x=10$. (iii) Write the perimeter of the plot. (iv) By how much does the area of the plot exceed that of the flower bed? Verify for $x=10$.",
   r"(i) $(x+5)(x+2)=x^2+7x+10$ (1). (ii) $15\times12=180$ m$^2$ (1). (iii) $2(2x+7)=4x+14$ m (1). (iv) Bed area $(x+3)^2=x^2+6x+9$; difference $=x+1$ (1); for $x=10$: $180-169=11=x+1$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Meena uses identities for quick mental calculations. She wants to find $98^2$, $103\times97$ and $52^2-48^2$ without a calculator. "
   r"(i) Write 98 as a difference to use $(a-b)^2$. (ii) Find $98^2$. (iii) Find $103\times97$. (iv) Find $52^2-48^2$ and name the identity used.",
   r"(i) $98=100-2$ (1). (ii) $(100-2)^2=10000-400+4=9604$ (1). (iii) $(100+3)(100-3)=10000-9=9991$ (1). (iv) $(52+48)(52-48)=100\times4=400$ (1); identity $a^2-b^2=(a+b)(a-b)$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A stationery shop in Chandigarh sells registers at ₹$a$ each and pens at ₹$b$ each. A bulk pack has 12 registers and 18 pens, so its bill is $12a+18b$ rupees. "
   r"Rahul wants to simplify the bill by factorisation. "
   r"(i) Find the highest common factor of 12 and 18. (ii) Factorise $12a+18b$. (iii) Find the bill when $a=15$ and $b=10$. (iv) Factorise $4x^2-36$ completely and verify at $x=5$.",
   r"(i) 6 (1). (ii) $6(2a+3b)$ (1). (iii) $6(30+30)=360$; check $180+180=360$ (1). (iv) $4(x^2-9)=4(x+3)(x-3)$ (1); at $x=5$: $4\times8\times2=64$ and $4(25)-36=64$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Distributive property", [
   r"$a(b+c)=ab+ac$ and $a(b-c)=ab-ac$.",
   r"$(a+b)(c+d)=ac+ad+bc+bd$ (each term of one bracket times each term of the other).",
   r"$(x+a)(x+b)=x^2+(a+b)x+ab$."]),
 ("Standard identities", [
   r"$(a+b)^2=a^2+2ab+b^2$.",
   r"$(a-b)^2=a^2-2ab+b^2$.",
   r"$(a+b)(a-b)=a^2-b^2$.",
   r"$(a+b)^2-(a-b)^2=4ab$ and $(a+b)^2+(a-b)^2=2(a^2+b^2)$."]),
 ("Factorisation", [
   r"Take out the common factor: $ab+ac=a(b+c)$.",
   r"$a^2-b^2=(a+b)(a-b)$.",
   r"$a^2+2ab+b^2=(a+b)^2$ and $a^2-2ab+b^2=(a-b)^2$."]),
 ("Quick calculation", [
   r"$99^2=(100-1)^2$, $102^2=(100+2)^2$.",
   r"$a\times b=\left(\dfrac{a+b}2\right)^2-\left(\dfrac{a-b}2\right)^2$, e.g. $53\times47=50^2-3^2=2491$.",
   r"Like terms: same variable part (e.g. $3x^2$ and $5x^2$); only like terms can be added or subtracted."]),
]

MISTAKES = [
 r"Writing $(a+b)^2=a^2+b^2$; the middle term $2ab$ is missed.",
 r"Writing $(a-b)^2=a^2-b^2$; correct is $a^2-2ab+b^2$, while $a^2-b^2=(a+b)(a-b)$.",
 r"Multiplying only the first term of a bracket: $3(x+4)=3x+4$ instead of $3x+12$.",
 r"Sign errors when multiplying: $-2\times(-3x)=+6x$ and $(x-3)(x-2)$ has $+6$ as the constant term.",
 r"Adding unlike terms: $2x+3x^2=5x^3$; $x$ and $x^2$ are not like terms.",
 r"Squaring a product without squaring the coefficient: $(3x)^2=9x^2$, not $3x^2$.",
]
