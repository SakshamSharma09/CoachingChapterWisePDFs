"""Class 7 Maths Ch 8 Working with Fractions - extras."""
from common import AR4, Q

AR = [
 AR4(r"$\frac23\times\frac34=\frac12$.", "The product of two fractions is (product of numerators) / (product of denominators).", "a",
     "6/12 = 1/2."),
 AR4(r"$\frac34\div\frac12=\frac32$.", r"$\frac12$ of $\frac34$ is $\frac38$.", "b",
     "(3/4) x 2 = 3/2 and (1/2)(3/4) = 3/8. Both true but separate facts."),
 AR4(r"Dividing by $\frac23$ is the same as multiplying by $\frac32$.", "Dividing by a fraction is the same as multiplying by the fraction itself.", "c",
     "A is true. Dividing by a fraction means multiplying by its reciprocal, so R is false."),
 AR4("Multiplying a positive number by a proper fraction always gives a larger number.", r"$\frac12$ of 8 is 4.", "d",
     "The result is smaller (4 < 8), so A is false. R is true."),
 AR4(r"$1\frac12\times\frac23=1$.", r"$1\frac12=\frac32$ and $\frac32\times\frac23=1$.", "a",
     "R shows the working that gives A."),
 AR4("The reciprocal of 0 is not defined.", "The reciprocal of 1 is 1.", "b",
     "No number multiplied by 0 gives 1, so A is true. R is true but unrelated."),
]

CASE = [
 Q(r"<b>Case study.</b> A cake needs $\frac34$ kg of flour. Rani wants to make only $\frac23$ of the recipe. (i) How much flour does she need? (ii) How much flour is needed for 4 whole cakes? (iii) How much flour is needed for $1\frac12$ cakes? (iv) She has 5 kg of flour. How many full cakes can she make and how much flour is left?",
   r"(i) $\frac34\times\frac23=\frac12$ kg (1). (ii) $4\times\frac34=3$ kg (1). (iii) $\frac34\times\frac32=\frac98=1\frac18$ kg (1). (iv) $5\div\frac34=\frac{20}{3}=6\frac23$, so 6 full cakes (1); flour used $=6\times\frac34=4\frac12$ kg, so $\frac12$ kg is left (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A table top is $\frac34$ m long and $\frac25$ m wide. (i) Find its area. (ii) Find its perimeter. (iii) $\frac13$ of the area is painted red. Find the red area. (iv) A second table top is $1\frac12$ m long and $\frac23$ m wide. Find its area and how much larger it is than the first.",
   r"(i) $\frac34\times\frac25=\frac{3}{10}$ m$^2$ (1). (ii) $2\left(\frac34+\frac25\right)=2\times\frac{23}{20}=\frac{23}{10}=2\frac{3}{10}$ m (1). (iii) $\frac13\times\frac{3}{10}=\frac{1}{10}$ m$^2$ (1). (iv) $\frac32\times\frac23=1$ m$^2$ (1); it is larger by $1-\frac{3}{10}=\frac{7}{10}$ m$^2$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A ribbon is $3\frac12$ m long. Kiran cuts it into equal pieces. (i) Write $3\frac12$ as an improper fraction. (ii) Write the reciprocal of $\frac78$. (iii) How many pieces of $\frac78$ m can be cut? (iv) If each piece is $\frac34$ m instead, how many full pieces are cut and what length is left over?",
   r"(i) $\frac72$ (1). (ii) $\frac87$ (1). (iii) $\frac72\div\frac78=\frac72\times\frac87=4$ pieces (1). (iv) $\frac72\div\frac34=\frac{14}{3}=4\frac23$, so 4 full pieces (1); length used $=4\times\frac34=3$ m, so $\frac12$ m is left (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Multiplying fractions", [r"$\dfrac ab\times\dfrac cd=\dfrac{a\times c}{b\times d}$ (cancel common factors first to save work).",
   r"'of' means multiply: $\dfrac12$ of $\dfrac34=\dfrac12\times\dfrac34=\dfrac38$.",
   r"Mixed numbers: convert to improper fractions before multiplying: $1\dfrac12\times\dfrac23=\dfrac32\times\dfrac23=1$.",
   r"Multiplying by a proper fraction makes a number smaller; by an improper fraction (greater than 1) makes it larger."]),
 ("Reciprocal", [r"Reciprocal of $\dfrac ab$ is $\dfrac ba$ and $\dfrac ab\times\dfrac ba=1$.",
   r"Reciprocal of a whole number $n$ is $\dfrac1n$. Reciprocal of 1 is 1. Zero has no reciprocal."]),
 ("Dividing fractions", [r"$\dfrac ab\div\dfrac cd=\dfrac ab\times\dfrac dc$ (multiply by the reciprocal of the divisor).",
   r"Whole number $\div$ fraction: $4\div\dfrac12=4\times2=8$.   Fraction $\div$ whole number: $\dfrac34\div3=\dfrac34\times\dfrac13=\dfrac14$.",
   r"Number of pieces $=$ total length $\div$ length of one piece."]),
 ("Area and word problems", [r"Area of a rectangle $=l\times b$ with fraction sides, e.g. $\dfrac34\times\dfrac25=\dfrac3{10}$ m$^2$.",
   r"Remaining part $=1-$ (fraction used); leftover $=$ total $-$ (pieces $\times$ size)."]),
]

MISTAKES = [
 r"Multiplying mixed numbers by multiplying the whole parts and the fractions separately; convert to improper fractions first.",
 r"Inverting the wrong fraction when dividing: only the <i>divisor</i> is inverted, not the dividend.",
 r"Dividing numerators and denominators directly without inverting, or inverting and forgetting to change $\div$ to $\times$.",
 r"Believing multiplication always makes a number bigger; multiplying by a proper fraction makes it smaller.",
 r"Forgetting to cancel common factors, or cancelling across a $+$ sign.",
]
