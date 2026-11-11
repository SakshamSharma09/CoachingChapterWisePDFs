"""Class 9 Maths Ch 4 Algebraic Identities - extras."""
from common import AR4, Q

AR = [
 AR4(r"$103^2=10609$.", r"$(a+b)^2=a^2+2ab+b^2$.", "a",
     r"$103^2=(100+3)^2=10000+600+9=10609$, using R."),
 AR4(r"$x^2-9=(x-3)(x+3)$.", r"$(a+b)^2=a^2+2ab+b^2$.", "b",
     r"A follows from $a^2-b^2=(a-b)(a+b)$; R is true but is a different identity and does not explain A."),
 AR4(r"$(x-y)^2=x^2-2xy+y^2$.", r"$(x-y)^2=x^2-y^2$.", "c",
     r"A is the correct identity; R is false because the middle term $-2xy$ is missing."),
 AR4(r"$(a+b)^3=a^3+b^3$ for all real numbers $a$ and $b$.", r"$(a+b)^3=a^3+3a^2b+3ab^2+b^3$.", "d",
     r"A is false (take $a=b=1$: $8\ne2$); R is the correct identity."),
 AR4(r"If $x+y=7$ and $xy=10$, then $x^2+y^2=29$.", r"$x^2+y^2=(x+y)^2-2xy$.", "a",
     r"$49-20=29$, obtained by using R."),
 AR4(r"$(2x-3)^3=8x^3-36x^2+54x-27$.", r"$(a+b)(a-b)=a^2-b^2$.", "b",
     r"A follows from $(a-b)^3=a^3-3a^2b+3ab^2-b^3$ with $a=2x,\ b=3$; R is true but is not used to prove A."),
]

CASE = [
 Q(r"<b>Case study.</b> Sunita, a Class 9 student in Lucknow, calculates squares and products quickly using algebraic identities instead of long multiplication. "
   r"(i) Find $103^2$. (ii) Find $98^2$. (iii) Find $102\times98$. (iv) Find $997\times1003$ using an identity and name the identity.",
   r"(i) $(100+3)^2=10000+600+9=10609$ (1). (ii) $(100-2)^2=10000-400+4=9604$ (1). (iii) $(100+2)(100-2)=10000-4=9996$ (1). (iv) $(1000-3)(1000+3)=1000^2-3^2=999991$ (1) using $(a-b)(a+b)=a^2-b^2$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A square lawn of side $x$ metres is surrounded by a path 2 m wide on all four sides, so that the outer boundary is also a square. "
   r"(i) Write the side of the outer square. (ii) Expand the area of the outer square. (iii) Find the area of the path in terms of $x$. (iv) If $x=12$, find the area of the path and the cost of paving it at Rs 50 per m$^2$.",
   r"(i) $x+4$ m (1). (ii) $(x+4)^2=x^2+8x+16$ m$^2$ (1). (iii) $(x+4)^2-x^2=8x+16$ m$^2$ (1). (iv) $8(12)+16=112$ m$^2$ (1); cost $=112\times50=$ Rs 5600 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A toy maker in Channapatna makes wooden cubes. One cube has edge $(2x+1)$ cm and another has edge $(3x-2)$ cm. "
   r"(i) Expand the volume of the first cube. (ii) Find the volume of the first cube when $x=2$. (iii) Use $(10+1)^3$ to find $11^3$. (iv) Expand the volume of the second cube and verify the result at $x=1$.",
   r"(i) $(2x+1)^3=8x^3+12x^2+6x+1$ (1). (ii) Edge $=5$ cm, so volume $=125$ cm$^3$ (check: $64+48+12+1=125$) (1). (iii) $1000+300+30+1=1331$ (1). (iv) $(3x-2)^3=27x^3-54x^2+36x-8$ (1); at $x=1$: $27-54+36-8=1=1^3$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Square identities", [r"$(a+b)^2=a^2+2ab+b^2$", r"$(a-b)^2=a^2-2ab+b^2$", r"$a^2-b^2=(a+b)(a-b)$",
   r"$(x+a)(x+b)=x^2+(a+b)x+ab$"]),
 ("Cube identities", [r"$(a+b)^3=a^3+3a^2b+3ab^2+b^3$", r"$(a-b)^3=a^3-3a^2b+3ab^2-b^3$",
   r"Sign pattern in $(a-b)^3$: the signs alternate $+,-,+,-$."]),
 ("Useful consequences", [r"$a^2+b^2=(a+b)^2-2ab=(a-b)^2+2ab$", r"$(a+b)^2-(a-b)^2=4ab$ and $(a+b)^2+(a-b)^2=2(a^2+b^2)$",
   r"Numerical use: $103^2=(100+3)^2$, $98^2=(100-2)^2$, $102\times98=100^2-2^2$, $11^3=(10+1)^3$."]),
 ("Factorisation", [r"Take out the common factor first, then look for an identity.",
   r"$x^2+(a+b)x+ab=(x+a)(x+b)$: find two numbers with sum $=a+b$ and product $=ab$.",
   r"$4x^2+12x+9=(2x+3)^2$ (perfect square: first and last terms are squares, middle term is twice their product).",
   r"A difference of two squares factorises as $(a+b)(a-b)$; a sum of two squares does not factorise over real numbers."]),
]

MISTAKES = [
 r"Writing $(a+b)^2=a^2+b^2$ and leaving out the middle term $2ab$.",
 r"Using $(a-b)^2=a^2-b^2$; this confuses a square of a difference with a difference of squares.",
 r"Sign errors in $(a-b)^3$: the terms alternate in sign, giving $a^3-3a^2b+3ab^2-b^3$.",
 r"Not squaring the whole term: $(2x+3)^2=4x^2+12x+9$, not $2x^2+12x+9$.",
 r"Factorising $x^2+5x+6$ with numbers whose sum or product is wrong; always check that the sum is 5 and the product is 6.",
 r"Not taking out a common factor before applying an identity, e.g. $2x^2-18=2(x-3)(x+3)$.",
]
