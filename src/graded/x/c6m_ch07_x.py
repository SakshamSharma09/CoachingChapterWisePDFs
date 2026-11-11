"""Class 6 Maths Ch 7 Fractions - extras."""
from common import AR4, Q

AR = [
 AR4(r"$\frac34$ and $\frac68$ are equivalent fractions.", "Multiplying the numerator and denominator by the same non-zero number gives an equivalent fraction.", "a",
     "Multiplying 3 and 4 by 2 gives 6 and 8."),
 AR4(r"The fraction $\frac74$ is an improper fraction.", r"$\frac74=1\frac34$.", "b",
     "Both are true. R is just another way of writing the number and does not explain why it is improper."),
 AR4(r"$\frac25+\frac15=\frac35$.", "To add fractions with the same denominator, add the numerators and also add the denominators.", "c",
     "A is true; the denominator stays the same, so R is false."),
 AR4(r"$\frac38$ is greater than $\frac12$.", "Among fractions with the same numerator, the one with the smaller denominator is greater.", "d",
     r"$\frac38=0.375<0.5=\frac12$, so A is false. R is true."),
 AR4(r"$\frac12+\frac13=\frac56$.", "Unlike fractions are first changed into equivalent fractions with a common denominator.", "a",
     r"$\frac36+\frac26=\frac56$ using the common denominator 6."),
 AR4(r"$\frac23$ of 12 is 8.", "Every proper fraction is less than 1.", "b",
     "12 / 3 = 4 and 4 x 2 = 8. Both true, but R does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> A pizza is cut into 8 equal slices. Kavita eats $\frac38$ of the pizza and her brother Rohan eats $\frac28$ of it. (i) What fraction of the pizza did they eat together? (ii) What fraction is left? (iii) Who ate more? (iv) How many slices are left, and what is the fraction left written with denominator 16?",
   r"(i) $\frac38+\frac28=\frac58$ (1). (ii) $1-\frac58=\frac38$ (1). (iii) Kavita (3 slices against 2) (1). (iv) 3 slices are left (1); $\frac38=\frac{6}{16}$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A milkman has $2\frac12$ litres of milk in the morning and $1\frac34$ litres in the evening. (i) Write $2\frac12$ as an improper fraction. (ii) Find the total milk he has. (iii) In which part of the day did he have more milk? (iv) He sells $3\frac12$ litres. How much is left?",
   r"(i) $\frac52$ (1). (ii) $2\frac12+1\frac34=\frac{10}{4}+\frac74=\frac{17}{4}=4\frac14$ litres (1). (iii) Morning, as $2\frac12>1\frac34$ (1). (iv) $4\frac14-3\frac12=\frac{17}{4}-\frac{14}{4}=\frac34$ litre (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> There are 40 students in a class. $\frac35$ of them like cricket, $\frac14$ of them like football, and the rest like other games. (i) How many students like cricket? (ii) How many like football? (iii) How many like other games? (iv) What fraction of the class likes other games? Show it in simplest form.",
   r"(i) $\frac35\times40=24$ (1). (ii) $\frac14\times40=10$ (1). (iii) $40-24-10=6$ (1). (iv) $\frac{6}{40}=\frac{3}{20}$ (the check: $1-\frac35-\frac14=\frac{3}{20}$) (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Kinds of fractions", [r"Fraction $\dfrac ab$: numerator $a$ (parts taken), denominator $b$ (equal parts in the whole).",
   r"Proper: $a<b$ (less than 1). Improper: $a\ge b$ (1 or more). Mixed number: whole part plus fraction.",
   r"Mixed to improper: $c\dfrac ab=\dfrac{c\times b+a}{b}$.   Improper to mixed: divide the numerator by the denominator."]),
 ("Equivalent fractions", [r"$\dfrac ab=\dfrac{a\times k}{b\times k}=\dfrac{a\div k}{b\div k}$ for any non-zero $k$.",
   r"Simplest form: divide numerator and denominator by their HCF."]),
 ("Comparing", [r"Same denominator: the larger numerator is greater. Same numerator: the smaller denominator is greater.",
   r"Unlike fractions: change to a common denominator (LCM of denominators), then compare."]),
 ("Addition and subtraction", [r"Like fractions: $\dfrac ac+\dfrac bc=\dfrac{a+b}{c}$ and $\dfrac ac-\dfrac bc=\dfrac{a-b}{c}$ (denominator unchanged).",
   r"Unlike fractions: make denominators equal first. Mixed numbers: add or subtract the whole parts and the fractions, or convert to improper fractions."]),
 ("Fraction of a quantity", [r"$\dfrac ab$ of $N=\dfrac Nb\times a$ (divide into $b$ equal parts, take $a$).",
   r"Remaining part $=1-$ fraction used."]),
]

MISTAKES = [
 r"Adding the denominators as well: $\frac15+\frac25=\frac37$ is wrong; the answer is $\frac35$.",
 r"Adding numerators and denominators of unlike fractions directly, e.g. $\frac12+\frac13=\frac25$.",
 r"Changing only the numerator or only the denominator when making an equivalent fraction.",
 r"Converting $2\frac12$ to $\frac{3}{2}$ instead of $\frac{2\times2+1}{2}=\frac52$.",
 r"Comparing fractions by denominators only: a bigger denominator with the same numerator makes the fraction <i>smaller</i>.",
]
