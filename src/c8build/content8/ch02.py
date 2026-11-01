from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def fr(f):
    f = F(f)
    return str(f.numerator) if f.denominator == 1 else rf"\frac{{{f.numerator}}}{{{f.denominator}}}"
# A: product of powers (5)
for a, m, n in [(2, 5, 3), (3, 4, 6), (5, 2, 7), (7, 3, 3), (10, 6, 4)]:
    A.append(M4(rf"${a}^{{{m}}}\times{a}^{{{n}}}$ equals:", rf"${a}^{{{m+n}}}$", [rf"${a}^{{{m*n}}}$", rf"${a*a}^{{{m+n}}}$", rf"${a}^{{{m-n}}}$"], rf"Add the exponents: ${m}+{n}={m+n}$"))
# A: quotient (5)
for a, m, n in [(2, 9, 4), (3, 10, 6), (5, 8, 3), (7, 12, 5), (11, 7, 7)]:
    A.append(M4(rf"${a}^{{{m}}}\div{a}^{{{n}}}$ equals:", rf"${a}^{{{m-n}}}$" if m != n else "1", [rf"${a}^{{{m+n}}}$", rf"${a}^{{{m//max(n,1)}}}$", rf"${a}^{{{m*n}}}$"], "Subtract the exponents"))
# A: power of power (4)
for a, m, n in [(2, 3, 4), (5, 2, 3), (3, 4, 2), (10, 3, 5)]:
    A.append(M4(rf"$({a}^{{{m}}})^{{{n}}}$ equals:", rf"${a}^{{{m*n}}}$", [rf"${a}^{{{m+n}}}$", rf"${a}^{{{m**n}}}$", rf"${a*m}^{{{n}}}$"], "Multiply the exponents"))
# A: negative exponents (6)
for a, n in [(2, 3), (3, 2), (5, 2), (10, 3), (4, 2), (2, 5)]:
    A.append(M4(rf"The value of ${a}^{{-{n}}}$ is:", rf"$\frac{{1}}{{{a**n}}}$", [rf"$-{a**n}$", rf"$\frac{{1}}{{{a*n}}}$", rf"${a**n}$"], rf"$a^{{-n}}=\frac1{{a^n}}$"))
# A: zero exponent and misc (3)
A += [
 M4(r"The value of $(-7)^0$ is:", "1", ["0", "−7", "7"], "Any non-zero number to the power 0 is 1"),
 M4(r"$(2\times3)^4$ equals:", r"$2^4\times3^4$", [r"$2^4+3^4$", r"$6^8$", r"$2\times3^4$"], r"$(ab)^n=a^nb^n$"),
 M4(r"$\left(\frac{2}{5}\right)^3$ equals:", r"$\frac{8}{125}$", [r"$\frac{6}{15}$", r"$\frac{8}{15}$", r"$\frac{2}{125}$"], r"$\frac{2^3}{5^3}$"),
]
# A: scientific notation (7)
SN = [("4500", r"$4.5\times10^3$", [r"$45\times10^3$", r"$4.5\times10^4$", r"$0.45\times10^3$"]),
      ("72000", r"$7.2\times10^4$", [r"$72\times10^4$", r"$7.2\times10^3$", r"$0.72\times10^4$"]),
      ("0.0035", r"$3.5\times10^{-3}$", [r"$3.5\times10^{3}$", r"$35\times10^{-3}$", r"$3.5\times10^{-4}$"]),
      ("6300000", r"$6.3\times10^6$", [r"$6.3\times10^5$", r"$63\times10^5$", r"$6.3\times10^7$"]),
      ("0.00008", r"$8\times10^{-5}$", [r"$8\times10^{-4}$", r"$8\times10^{5}$", r"$0.8\times10^{-5}$"]),
      ("150000000", r"$1.5\times10^8$", [r"$1.5\times10^7$", r"$15\times10^7$", r"$1.5\times10^9$"]),
      ("0.0412", r"$4.12\times10^{-2}$", [r"$4.12\times10^{-3}$", r"$41.2\times10^{-2}$", r"$4.12\times10^{2}$"])]
for num, sci, wr in SN:
    A.append(M4(f"The number {num} in standard (scientific) form is:", sci, wr, "One non-zero digit before the decimal point"))
# A: large-number vocab (4)
A += [
 M4("One crore is equal to:", r"$10^7$", [r"$10^5$", r"$10^6$", r"$10^8$"], "1 crore = 100 lakh = 10,000,000"),
 M4("One lakh is equal to:", r"$10^5$", [r"$10^4$", r"$10^6$", r"$10^7$"], "1 lakh = 100,000"),
 M4("One billion is:", r"$10^9$", [r"$10^6$", r"$10^{12}$", r"$10^7$"], "A thousand million"),
 M4(r"$2^{10}$ is closest to:", "1000", ["100", "10000", "2000"], "$2^{10}=1024$"),
]
A += [
 M4(r"$7.5\times10^{4}$ written in usual form is:", "75000", ["7500", "750000", "0.00075"], "Move the decimal 4 places right"),
 M4(r"$2\times10^{-3}$ written in usual form is:", "0.002", ["0.0002", "2000", "0.02"], "Move the decimal 3 places left"),
 M4(r"The value of $\left(\frac{1}{3}\right)^{-2}$ is:", "9", [r"$\frac19$", "6", r"$-\frac19$"], "Reciprocal squared"),
 M4(r"$\dfrac{5^{6}}{5^{8}}$ equals:", r"$\frac{1}{25}$", ["25", "$-25$", r"$5^{-14}$"], "$5^{6-8}=5^{-2}$"),
 M4(r"If $2^{x}=64$ then $x$ is:", "6", ["5", "7", "8"], "$64=2^6$"),
 M4(r"$(2^{3})^{0}$ equals:", "1", ["0", "8", "6"], "Anything non-zero to power 0"),
]
assert len(A) == 40, len(A)
B = [
 Q(r"Simplify $2^5\times2^{-3}$.", r"Add exponents: $2^{5-3}=2^2=4$ (2).", "2"),
 Q(r"Write $5^{-3}$ as a fraction.", r"$\frac1{5^3}=\frac1{125}$ (2).", "2"),
 Q(r"Express $0.00045$ in scientific notation.", r"$4.5\times10^{-4}$ (2).", "2"),
 Q(r"Write $6.2\times10^{5}$ in usual form.", "620000 (2).", "2"),
 Q(r"Simplify $(3^2)^4\div3^6$.", r"$3^8\div3^6=3^2=9$ (2).", "2"),
 Q(r"Evaluate $(-1)^{101}$ and $(-1)^{100}$.", "$-1$ for an odd power (1); $1$ for an even power (1).", "1+1"),
 Q(r"Find the value of $4^0+4^{-1}$.", r"$1+\frac14=\frac54$ (2).", "2"),
 Q("State the law for multiplying powers with the same base. Give an example.", r"Add exponents: $a^m\times a^n=a^{m+n}$ (1); e.g. $5^2\times5^3=5^5$ (1).", "1+1"),
 Q("Why is any number raised to the power 0 equal to 1 (for non-zero numbers)?", r"$a^n\div a^n=1$ and by the law also $a^{n-n}=a^0$ (2).", "2"),
 Q(r"Which is greater, $2^{10}$ or $10^{2}$? Why?", r"$2^{10}=1024>100=10^2$ (2).", "2"),
 Q("Write the number 3,500,000 in scientific notation.", r"$3.5\times10^6$ (2).", "2"),
 Q("What is the speed of light, 300000000 m/s, in scientific notation?", r"$3\times10^8$ m/s (2).", "2"),
 Q(r"Simplify $\dfrac{10^5\times10^{-2}}{10^2}$.", r"$10^{5-2-2}=10^1=10$ (2).", "2"),
 Q(r"Express $\dfrac{1}{64}$ as a power of 2 with a negative exponent.", r"$\frac1{2^6}=2^{-6}$ (2).", "2"),
 Q(r"Find $x$ if $5^x=625$.", r"$625=5^4$ so $x=4$ (2).", "2"),
 Q(r"Compare $3\times10^4$ and $2\times10^5$.", r"$30000<200000$, so $2\times10^5$ is larger (2).", "2"),
]
for a, b, c, d in [(2, 4, 3, 5), (3, 5, 2, 6), (5, 3, 4, 2), (7, 4, 2, 3), (10, 8, 5, 4), (2, 6, 5, 2), (3, 7, 3, 4), (5, 6, 2, 3), (4, 5, 3, 2), (6, 4, 4, 5), (2, 8, 3, 4), (3, 8, 6, 2)][:12]:
    C.append(Q(rf"Simplify: $\dfrac{{{a}^{{{b}}}\times{a}^{{{c}}}}}{{{a}^{{{d}}}}}$.", rf"Add in the numerator: ${a}^{{{b+c}}}$ (1); subtract: ${a}^{{{b+c-d}}}$ (1); value ${a**(b+c-d)}$ (1).", "1+1+1"))
C += [
 Q(r"Express $0.0000327$ in scientific notation and write the number of zeros after the decimal point before the first digit.", r"$3.27\times10^{-5}$ (2); four zeros (1).", "2+1"),
 Q("The distance of the Sun from the Earth is about 150000000 km. Write it in scientific notation and in terms of lakh/crore.", r"$1.5\times10^8$ km (2); 15 crore km (1).", "2+1"),
 Q(r"Simplify $\left(\frac{3}{4}\right)^{-2}$.", r"$\left(\frac43\right)^2$ (1.5); $\frac{16}{9}$ (1.5).", "1½+1½"),
 Q(r"Simplify $2^{-3}+3^{-2}$ as a single fraction.", r"$\frac18+\frac19$ (1.5); $\frac{17}{72}$ (1.5).", "1½+1½"),
 Q(r"Find the value of $\left(2^{3}\right)^{2}\times2^{-4}\div2^{0}$.", r"$2^{6}\times2^{-4}=2^2=4$ (3).", "3"),
 Q(r"The mass of the Earth is $5.97\times10^{24}$ kg and of the Moon is $7.35\times10^{22}$ kg. Which is greater and about how many times?", r"Earth is greater (1); ratio $\approx81$ (2).", "1+2"),
 Q("A bacterium doubles every hour. Starting with one bacterium, how many are there after 10 hours? Write as a power.", r"$2^{10}=1024$ (3).", "3"),
 Q(r"Show that $(a\times b)^{-1}=a^{-1}\times b^{-1}$ for $a=2,\ b=5$.", r"LHS $=\frac1{10}$; RHS $=\frac12\times\frac15=\frac1{10}$ (3).", "3"),
 Q(r"Write $\dfrac{4.2\times10^5}{2.1\times10^2}$ in scientific notation.", r"$2\times10^3$ (3).", "3"),
 Q(r"If $3^{x+1}=81$, find $x$ and verify.", r"$81=3^4$ so $x+1=4$, $x=3$ (2); $3^4=81$ (1).", "2+1"),
 Q(r"Arrange in ascending order: $3\times10^{-3}$, $2\times10^{-2}$, $5\times10^{-4}$.", r"$5\times10^{-4}<3\times10^{-3}<2\times10^{-2}$ (3).", "3"),
 Q(r"A sheet of paper is 0.1 mm thick. Find the height of a stack of $10^4$ sheets in metres.", r"$0.1\times10^4=1000$ mm $=1$ m (3).", "3"),
]
C = C[:24]
assert len(C) == 24, len(C)
D = [
 Q(r"(i) State the laws of exponents for $a^m\times a^n$, $a^m\div a^n$ and $(a^m)^n$. (ii) Simplify $\dfrac{2^{7}\times 5^{4}}{10^{3}}$.", r"(i) $a^{m+n}$, $a^{m-n}$, $a^{mn}$ (3). (ii) $=2^7\times5^4/(2^3\times5^3)=2^4\times5=80$ (2).", "3+2"),
 Q(r"(i) Write $4.7\times10^{-4}$ in decimal form. (ii) Write $0.00000092$ in standard form. (iii) Add $3\times10^4+5\times10^3$ and express in standard form.", r"(i) $0.00047$ (1). (ii) $9.2\times10^{-7}$ (2). (iii) $35000=3.5\times10^4$ (2).", "1+2+2"),
 Q(r"(i) Find the value of $\left(\frac{2}{3}\right)^{-3}\times\left(\frac{2}{3}\right)^{2}$. (ii) Simplify $\dfrac{(25)^{3}\times 5^{2}}{5^{10}}$.", r"(i) $\left(\frac23\right)^{-1}=\frac32$ (2). (ii) $5^6\times5^2/5^{10}=5^{-2}=\frac1{25}$ (3).", "2+3"),
 Q("<b>Case study:</b> A laboratory sample has $2\\times10^{9}$ bacteria. The population triples every hour. (i) How many bacteria are there after 3 hours? (ii) Express the answer in standard form. (iii) After how many hours will it first exceed $10^{11}$?", r"(i) $2\times10^9\times3^3=5.4\times10^{10}$ (2). (ii) $5.4\times10^{10}$ (1). (iii) after 4 hours: $1.62\times10^{11}$ (2).", "2+1+2"),
 Q(r"(i) Explain why $2^{-3}=\frac18$. (ii) Simplify $\dfrac{2^{-3}\times3^{2}}{6^{-1}}$.", r"(i) $2^{0}\div2^{3}=2^{-3}=\frac18$ (2). (ii) $\frac{9}{8}\times6=\frac{27}{4}$ (3).", "2+3"),
 Q("(i) The Milky Way is about $10^{5}$ light-years wide and one light-year is about $9.46\\times10^{12}$ km. Estimate its width in km. (ii) Express in standard form.", r"(i) $9.46\times10^{12}\times10^5=9.46\times10^{17}$ km (3). (ii) Already in standard form (2).", "3+2"),
 Q(r"(i) Evaluate $(5^{0}+4^{-1})\times2^{2}$. (ii) Find $x$ if $\left(\frac{3}{5}\right)^{x}\times\left(\frac{3}{5}\right)^{-4}=\left(\frac35\right)^{5}$.", r"(i) $(1+\frac14)\times4=5$ (2). (ii) $x-4=5$, $x=9$ (3).", "2+3"),
 Q("<b>Case study:</b> The population of India is about 140 crore and area is about 32.9 lakh km². (i) Write both in standard form. (ii) Find the approximate population density. (iii) Compare with a city having density 11000 per km².", r"(i) $1.4\times10^9$ and $3.29\times10^6$ (2). (ii) $\approx426$ per km² (2). (iii) City is about 26 times denser (1).", "2+2+1"),
 Q(r"(i) Prove $a^m\times a^{-m}=1$. (ii) Verify for $a=3,\ m=2$.", r"(i) $a^{m-m}=a^0=1$ (3). (ii) $9\times\frac19=1$ (2).", "3+2"),
 Q(r"(i) Write $\left(\frac{1}{2}\right)^{-5}$ without a negative exponent. (ii) Simplify $\dfrac{(-2)^{3}\times(-2)^{-5}}{(-2)^{-1}}$.", r"(i) $2^5=32$ (2). (ii) $(-2)^{3-5+1}=(-2)^{-1}=-\frac12$ (3).", "2+3"),
 Q(r"(i) The diameter of a hydrogen atom is about $10^{-10}$ m and of a pollen grain about $10^{-5}$ m. How many times larger is the pollen grain? (ii) Express a red blood cell of $7\times10^{-6}$ m in mm.", r"(i) $10^{-5}/10^{-10}=10^5$ times (3). (ii) $7\times10^{-3}$ mm (2).", "3+2"),
 Q("(i) Explain how to compare two numbers written in scientific notation. (ii) Compare $4.5\\times10^{7}$ and $9.1\\times10^{6}$.", r"(i) Compare the powers of 10 first, then the decimal parts (3). (ii) $4.5\times10^7=45\times10^6>9.1\times10^6$ (2).", "3+2"),
 Q(r"(i) Simplify $\dfrac{16^{2}\times 2^{3}}{4^{3}}$. (ii) Express the result as a power of 2.", r"(i) $\frac{2^8\times2^3}{2^6}=2^5=32$ (3). (ii) $2^5$ (2).", "3+2"),
 Q("<b>Case study:</b> A dealer's annual turnover is ₹ 4.8 crore. (i) Write it in standard form. (ii) If it grows by $10^{6}$ every year, find the turnover after 5 years. (iii) Write the answer in standard form.", r"(i) $4.8\times10^7$ (1). (ii) $4.8\times10^7+5\times10^6=5.3\times10^7$ (2). (iii) $5.3\times10^7$ (2).", "1+2+2"),
 Q(r"(i) Show that $(ab)^n=a^nb^n$ for $a=2,\ b=3,\ n=3$. (ii) Hence find $12^3\div 6^3$.", r"(i) $6^3=216=8\times27$ (2). (ii) $(12/6)^3=8$ (3).", "2+3"),
 Q("(i) Why do scientists prefer scientific notation? (ii) Write the mass of an electron, 0.00000000000000000000000000000091 kg, in scientific notation.", r"(i) Compact, easy to compare and calculate (2). (ii) $9.1\times10^{-31}$ kg (3).", "2+3"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
