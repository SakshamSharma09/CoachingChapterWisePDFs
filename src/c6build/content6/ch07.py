from fractions import Fraction as F
from math import gcd
from lib import mcq, Q, OR
from mk9 import M4, build
def fr(x):
    x = F(x)
    return f"{x.numerator}" if x.denominator == 1 else f"\\frac{{{x.numerator}}}{{{x.denominator}}}"
def mix(x):
    x = F(x); w = x.numerator // x.denominator; r = x - w
    return f"{w}\\frac{{{r.numerator}}}{{{r.denominator}}}" if r and w else fr(x)
def T(x): return f"${x}$"
A = [
 M4("In the fraction $\\frac{3}{8}$, the number 8 is called the:", "denominator", ["numerator", "quotient", "remainder"], "total equal parts"),
 M4("In the fraction $\\frac{3}{8}$, the number 3 is called the:", "numerator", ["denominator", "divisor", "sum"], "parts taken"),
 M4("A fraction whose numerator is less than its denominator is a:", "proper fraction", ["improper fraction", "mixed fraction", "whole number"], "less than 1"),
 M4("A fraction whose numerator is greater than or equal to its denominator is a:", "improper fraction", ["proper fraction", "unit fraction", "decimal"], "at least 1"),
 M4("A number made of a whole number and a proper fraction is a:", "mixed fraction", ["proper fraction", "unit fraction", "improper fraction"], "e.g. 2½"),
 M4("A fraction with numerator 1 is a:", "unit fraction", ["mixed fraction", "improper fraction", "whole number"], "e.g. 1/5"),
 M4("Fractions with the same value are:", "equivalent fractions", ["unit fractions", "proper fractions", "unlike fractions"], "e.g. 1/2 = 2/4"),
 M4("Fractions with the same denominator are called:", "like fractions", ["unlike fractions", "unit fractions", "mixed fractions"], "same denominator"),
 M4("To find an equivalent fraction we multiply or divide the numerator and denominator by:", "the same non-zero number", ["different numbers", "zero", "the sum"], "rule"),
 M4("The fraction $\\frac{4}{12}$ in its simplest form is:", "$\\frac13$", ["$\\frac14$", "$\\frac23$", "$\\frac12$"], "divide by 4"),
 M4("Which is greater?", "$\\frac34$", ["$\\frac23$", "$\\frac12$", "$\\frac13$"], "common denominator 12"),
 M4("$\\frac{5}{7}+\\frac{1}{7}$ equals:", "$\\frac67$", ["$\\frac{6}{14}$", "$\\frac47$", "$\\frac57$"], "add numerators"),
 M4("$\\frac{9}{11}-\\frac{4}{11}$ equals:", "$\\frac{5}{11}$", ["$\\frac{5}{0}$", "$\\frac{13}{11}$", "$\\frac{4}{11}$"], "subtract numerators"),
 M4("$\\frac12+\\frac13$ equals:", "$\\frac56$", ["$\\frac25$", "$\\frac{2}{6}$", "$\\frac16$"], "LCM 6"),
 M4("$\\frac34-\\frac12$ equals:", "$\\frac14$", ["$\\frac{1}{2}$", "$\\frac{1}{8}$", "$\\frac{3}{8}$"], "$\\frac34-\\frac24$"),
 M4("Which fraction is equivalent to $\\frac23$?", "$\\frac{6}{9}$", ["$\\frac{6}{12}$", "$\\frac{4}{9}$", "$\\frac{2}{9}$"], "multiply by 3"),
 M4("Which fraction is the smallest?", "$\\frac15$", ["$\\frac14$", "$\\frac13$", "$\\frac12$"], "bigger denominator, smaller part of unit fractions"),
 M4("The mixed fraction $2\\frac13$ as an improper fraction is:", "$\\frac73$", ["$\\frac{6}{3}$", "$\\frac{5}{3}$", "$\\frac{2}{3}$"], "$2\\times3+1$"),
 M4("The improper fraction $\\frac{11}{4}$ as a mixed fraction is:", "$2\\frac34$", ["$2\\frac14$", "$3\\frac14$", "$1\\frac34$"], "$11=2\\times4+3$"),
 M4("Half of a pizza is eaten and one fourth is eaten more. The fraction eaten is:", "$\\frac34$", ["$\\frac23$", "$\\frac14$", "$\\frac12$"], "$\\frac12+\\frac14$"),
 M4("The fraction of a day that is 6 hours is:", "$\\frac14$", ["$\\frac16$", "$\\frac13$", "$\\frac12$"], "6/24"),
 M4("If a ribbon of 1 m is divided into 8 equal parts, each part is:", "$\\frac18$ m", ["$\\frac14$ m", "8 m", "$\\frac12$ m"], "equal parts"),
 M4("On the number line, $\\frac12$ lies:", "midway between 0 and 1", ["at 1", "beyond 1", "at 0"], "half"),
 M4("The fraction equal to 1 is:", "$\\frac55$", ["$\\frac15$", "$\\frac{5}{10}$", "$\\frac{1}{5}$"], "same numerator and denominator"),
 M4("$\\frac{3}{4}$ of 20 is:", "15", ["12", "5", "16"], "$20\\div4\\times3$"),
 M4("$\\frac{2}{5}$ of 30 is:", "12", ["10", "15", "6"], "$30\\div5\\times2$"),
 M4("A fraction cannot have denominator:", "0", ["1", "2", "10"], "division by zero"),
 M4("The simplest form of $\\frac{18}{24}$ is:", "$\\frac34$", ["$\\frac{9}{12}$", "$\\frac23$", "$\\frac{6}{8}$"], "divide by 6"),
 M4("Equal shares of 3 chapatis among 4 children give each:", "$\\frac34$ of a chapati", ["$\\frac43$ chapati", "1 chapati", "$\\frac14$ chapati"], "sharing"),
]
A.append(M4("The fraction $\\frac{5}{8}$ means:", "5 of 8 equal parts", ["8 of 5 equal parts", "5 + 8 parts", "5 equal parts of 3"], "numerator over denominator"))
pairs = [(F(2, 3), F(3, 4)), (F(5, 6), F(7, 9)), (F(3, 5), F(5, 8)), (F(4, 7), F(5, 9)), (F(7, 10), F(2, 3))]
for a, b in pairs:
    big = max(a, b)
    A.append(M4(f"Which is greater: {T(fr(a))} or {T(fr(b))}?", T(fr(big)), [T(fr(min(a, b))), "both are equal", "cannot be compared"], "compare using common denominator"))
sums = [(F(1, 2), F(1, 3)), (F(2, 5), F(1, 4)), (F(3, 8), F(1, 4)), (F(5, 6), F(1, 3)), (F(1, 6), F(1, 4))]
for a, b in sums:
    s = a + b
    A.append(M4(f"{T(fr(a))} + {T(fr(b))} equals:", T(fr(s)), [T(fr(s + F(1, 12))), T(fr(s - F(1, 20))), T(f"\\frac{{{a.numerator + b.numerator}}}{{{a.denominator + b.denominator}}}")], "use the LCM of denominators"))
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Define a proper fraction and an improper fraction with one example each.", "Numerator < denominator, e.g. $\\frac35$; numerator ≥ denominator, e.g. $\\frac75$.", "1+1"),
 Q("Convert $3\\frac25$ to an improper fraction.", "$\\frac{17}{5}$.", "1+1"),
 Q("Convert $\\frac{19}{6}$ to a mixed fraction.", "$3\\frac16$.", "1+1"),
 Q("Write three fractions equivalent to $\\frac{2}{5}$.", "$\\frac{4}{10},\\frac{6}{15},\\frac{8}{20}$.", "1+1"),
 Q("Simplify $\\frac{24}{36}$.", "$\\frac23$ (divide by 12).", "1+1"),
 Q("Add $\\frac{3}{10}+\\frac{4}{10}$.", "$\\frac{7}{10}$.", "1+1"),
 Q("Subtract $\\frac{7}{9}-\\frac{2}{9}$.", "$\\frac59$.", "1+1"),
 Q("Which is greater, $\\frac{5}{6}$ or $\\frac{3}{4}$?", "$\\frac{5}{6}=\\frac{10}{12}$, $\\frac34=\\frac{9}{12}$; $\\frac56$ is greater.", "1+1"),
 Q("What is a unit fraction? Give two examples.", "A fraction with numerator 1; $\\frac12$, $\\frac17$.", "1+1"),
 Q("Find $\\frac{3}{5}$ of 40.", "$40\\div5\\times3=24$.", "1+1"),
 Q("What fraction of an hour is 15 minutes?", "$\\frac{15}{60}=\\frac14$.", "1+1"),
 Q("Write the like fractions among $\\frac{2}{7},\\frac{3}{5},\\frac{5}{7},\\frac{1}{7}$.", "$\\frac27,\\frac57,\\frac17$.", "1+1"),
 Q("Add $\\frac12+\\frac14$.", "$\\frac34$.", "1+1"),
 Q("Locate $\\frac34$ on the number line.", "It lies three quarters of the way from 0 to 1.", "1+1"),
 Q("What does the fraction $\\frac{2}{3}$ mean when a rope is divided?", "Two out of three equal parts of the rope.", "1+1"),
 Q("Arrange in ascending order: $\\frac13,\\frac12,\\frac16$.", "$\\frac16<\\frac13<\\frac12$.", "1+1"),
]
C = [
 Q("Add $\\frac{2}{3}+\\frac{3}{4}$ and write the answer as a mixed fraction.", "LCM 12: $\\frac{8}{12}+\\frac{9}{12}=\\frac{17}{12}$ (2); $1\\frac{5}{12}$ (1).", "2+1"),
 Q("Subtract $\\frac{5}{6}-\\frac{1}{4}$.", "LCM 12: $\\frac{10}{12}-\\frac{3}{12}=\\frac{7}{12}$ (3).", "1+2"),
 Q("Arrange $\\frac{2}{3},\\frac{3}{5},\\frac{7}{10}$ in descending order.", "$\\frac{20}{30},\\frac{18}{30},\\frac{21}{30}$ (2); $\\frac{7}{10}>\\frac23>\\frac35$ (1).", "2+1"),
 Q("Find three equivalent fractions of $\\frac{3}{7}$ and explain how you get them.", "Multiply numerator and denominator by 2, 3, 4: $\\frac{6}{14},\\frac{9}{21},\\frac{12}{28}$ (3).", "1+2"),
 Q("Convert $5\\frac{3}{8}$ to an improper fraction and $\\frac{37}{5}$ to a mixed fraction.", "$\\frac{43}{8}$ (1.5); $7\\frac25$ (1.5).", "1½+1½"),
 Q("A rope 3 m long is cut into pieces of $\\frac{3}{4}$ m. How many pieces?", "$3\\div\\frac34=4$ pieces (3).", "1+2"),
 Q("Ravi ate $\\frac{2}{5}$ of a cake and Rita ate $\\frac{1}{3}$. How much did they eat together? How much is left?", "$\\frac{11}{15}$ eaten (1.5); $\\frac{4}{15}$ left (1.5).", "1½+1½"),
 Q("Show that $\\frac{4}{6}$ and $\\frac{10}{15}$ are equivalent.", "Both simplify to $\\frac23$ (3).", "1+2"),
 Q("Share 5 equal chapatis among 4 children. What does each get? Write as a mixed fraction.", "$\\frac54=1\\frac14$ chapati (3).", "1+2"),
 Q("A tank is $\\frac{3}{4}$ full. After using $\\frac{1}{8}$ of the tank, how much remains?", "$\\frac68-\\frac18=\\frac58$ (3).", "1+2"),
 Q("Compare $\\frac{5}{8}$ and $\\frac{7}{12}$ using a common denominator.", "$\\frac{15}{24}>\\frac{14}{24}$, so $\\frac58$ is greater (3).", "1+2"),
 Q("Explain with a picture why $\\frac{1}{2}=\\frac{3}{6}$.", "A circle or strip halved equals 3 of 6 equal parts (3).", "1+2"),
 Q("What fraction of a metre is 35 cm? Simplify.", "$\\frac{35}{100}=\\frac{7}{20}$ (3).", "1+2"),
 Q("Find $\\frac{2}{3}$ of ₹ 150 and $\\frac{3}{5}$ of 250 g.", "₹100 (1.5); 150 g (1.5).", "1½+1½"),
 Q("Write the fraction of the shaded part if 3 of 8 equal squares are shaded and 1 more is shaded.", "$\\frac48=\\frac12$ (3).", "1+2"),
 Q("Convert $\\frac{7}{4}$ to a mixed fraction and place it on a number line between whole numbers.", "$1\\frac34$ between 1 and 2 (3).", "1+2"),
 Q("A bag has 24 balls, $\\frac{3}{8}$ of them are red. How many are red and how many are not?", "9 red (1.5); 15 not red (1.5).", "1½+1½"),
 Q("Add $2\\frac12+1\\frac13$.", "$3+\\frac56=3\\frac56$ (3).", "1+2"),
 Q("Subtract $3\\frac14-1\\frac12$.", "$\\frac{13}{4}-\\frac{6}{4}=\\frac74=1\\frac34$ (3).", "1+2"),
 Q("Find the missing number: $\\frac{3}{5}=\\frac{?}{35}$.", "21 (3).", "1+2"),
 Q("A cloth of $\\frac{7}{2}$ m is cut into two parts, one of $\\frac{5}{4}$ m. Find the other.", "$\\frac{14}{4}-\\frac54=\\frac94=2\\frac14$ m (3).", "1+2"),
 Q("Why is $\\frac{1}{4}$ greater than $\\frac{1}{5}$?", "When a whole is divided into fewer parts each part is larger (3).", "1+2"),
 Q("Find the sum $\\frac{1}{2}+\\frac{1}{4}+\\frac{1}{8}$.", "$\\frac{4+2+1}{8}=\\frac78$ (3).", "1+2"),
 Q("Put $\\frac{7}{3}$ and $2\\frac13$ on the number line. What do you notice?", "They are the same point (3).", "1+2"),
]
D = [
 Q("(i) Define proper, improper and mixed fractions. (ii) Write $\\frac{29}{6}$ as a mixed fraction. (iii) Write $4\\frac{2}{7}$ as an improper fraction.", "(i) Definitions with examples (2). (ii) $4\\frac56$ (1.5). (iii) $\\frac{30}{7}$ (1.5).", "2+1½+1½"),
 Q("(i) What are equivalent fractions? (ii) Find four fractions equal to $\\frac{3}{4}$. (iii) Simplify $\\frac{45}{60}$.", "(i) Fractions with the same value (1). (ii) $\\frac68,\\frac9{12},\\frac{12}{16},\\frac{15}{20}$ (2). (iii) $\\frac34$ (2).", "1+2+2"),
 Q("(i) Compare $\\frac{5}{6},\\frac{3}{4}$ and $\\frac{7}{9}$. (ii) Arrange in ascending order.", "(i) Denominator 36: $\\frac{30}{36},\\frac{27}{36},\\frac{28}{36}$ (3). (ii) $\\frac34<\\frac79<\\frac56$ (2).", "3+2"),
 Q("<b>Case study:</b> A recipe needs $\\frac{3}{4}$ cup of flour and $\\frac{1}{2}$ cup of sugar. (i) How much dry material in total? (ii) How much more flour than sugar? (iii) If the recipe is doubled, how much flour? (iv) Write the answer to (i) as a mixed fraction.", "(i) $\\frac54$ cup (1). (ii) $\\frac14$ cup (1). (iii) $1\\frac12$ cups (1). (iv) $1\\frac14$ (2).", "1+1+1+2"),
 Q("(i) Add $\\frac{3}{4}+\\frac{5}{6}$. (ii) Subtract $\\frac{7}{8}-\\frac{1}{3}$. (iii) Express both results as mixed fractions where needed.", "(i) $\\frac{19}{12}$ (2). (ii) $\\frac{13}{24}$ (2). (iii) $1\\frac{7}{12}$ (1).", "2+2+1"),
 Q("(i) Explain how to add unlike fractions. (ii) Add $\\frac{2}{5}+\\frac{7}{10}$. (iii) Add $1\\frac{1}{4}+2\\frac{2}{3}$.", "(i) Make denominators equal using LCM (1). (ii) $\\frac{11}{10}=1\\frac1{10}$ (2). (iii) $3\\frac{11}{12}$ (2).", "1+2+2"),
 Q("<b>Case study:</b> A water tank is $\\frac{5}{8}$ full. Rahul adds $\\frac{1}{4}$ of the tank. Then $\\frac{1}{8}$ is used. (i) Fraction after adding? (ii) Fraction after using? (iii) Is the tank full at any time? (iv) How much more is needed to fill?", "(i) $\\frac78$ (1). (ii) $\\frac68=\\frac34$ (1). (iii) No (1). (iv) $\\frac14$ (2).", "1+1+1+2"),
 Q("(i) Show $\\frac{3}{5}$ and $\\frac{6}{10}$ on a number line. (ii) Show they are equal. (iii) Find $\\frac{3}{5}$ of 75.", "(i) Correct number line (2). (ii) Same point (1). (iii) 45 (2).", "2+1+2"),
 Q("(i) Divide 7 equal cakes among 3 friends. (ii) Write each share as a mixed fraction. (iii) Explain with a picture.", "(i) $\\frac73$ each (2). (ii) $2\\frac13$ (1.5). (iii) 2 whole and one-third (1.5).", "2+1½+1½"),
 Q("<b>Case study:</b> A tailor has 5 m of cloth. A shirt uses $1\\frac{3}{4}$ m. (i) How much for two shirts? (ii) How much cloth is left? (iii) Can he make a third shirt? (iv) How much more is needed or left?", "(i) $3\\frac12$ m (1). (ii) $1\\frac12$ m (1). (iii) No (1). (iv) Needs $\\frac14$ m more (2).", "1+1+1+2"),
 Q("(i) State why the denominator cannot be zero. (ii) Write the smallest unit fraction with denominator ≤ 10. (iii) Order $\\frac12,\\frac13,\\frac14,\\frac1{10}$.", "(i) Cannot divide into zero parts (2). (ii) $\\frac1{10}$ (1). (iii) $\\frac1{10}<\\frac14<\\frac13<\\frac12$ (2).", "2+1+2"),
 Q("(i) Compare $\\frac{7}{3}$ and $2\\frac12$. (ii) Add them. (iii) Write the sum as a mixed fraction.", "(i) $\\frac{14}{6}<\\frac{15}{6}$ (2). (ii) $\\frac{29}{6}$ (2). (iii) $4\\frac56$ (1).", "2+2+1"),
 Q("<b>Case study:</b> A class of 40: $\\frac{3}{8}$ walk, $\\frac{1}{4}$ cycle, rest use a bus. (i) How many walk? (ii) How many cycle? (iii) Fraction using a bus? (iv) How many use the bus?", "(i) 15 (1). (ii) 10 (1). (iii) $\\frac38$ (1). (iv) 15 (2).", "1+1+1+2"),
 Q("(i) Why are $\\frac{2}{4}$ and $\\frac{1}{2}$ equal? (ii) Show with folding paper. (iii) Find the fraction equal to $\\frac{1}{2}$ with denominator 18.", "(i) Same part of whole (1). (ii) Fold and shade (2). (iii) $\\frac{9}{18}$ (2).", "1+2+2"),
 Q("(i) Mention one historical fact about fractions in India. (ii) Write 3/4 in Indian number words. (iii) Why were fractions needed?", "(i) Fractions like ½, ¼ used in ancient Indian measures / Brahmagupta and Bakhshali (2). (ii) Three-fourths / Pa·un (1). (iii) For sharing and trade measures (2).", "2+1+2"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 15, (len(B), len(C), len(D))
D.append(Q("(i) Write $\\frac{3}{4}$ of a day in hours. (ii) Write $\\frac{2}{3}$ of an hour in minutes. (iii) What is $\\frac{5}{8}$ of 1 kg in grams?", "(i) 18 hours (1.5). (ii) 40 minutes (1.5). (iii) 625 g (2).", "1½+1½+2"))
SETS, POOL = build(A, B, C, D)
