"""Class 8 Maths Ch 2 Power Play - extras."""
from common import AR4, Q

AR = [
 AR4(r"$2^{-3}=\dfrac18$.", r"For a non-zero number $a$, $a^{-n}=\dfrac{1}{a^n}$.", "a",
     r"$2^{-3}=\dfrac1{2^3}=\dfrac18$; R is exactly the rule used."),
 AR4(r"$(-1)^{101}=-1$.", r"Any non-zero number raised to the power 0 equals 1.", "b",
     r"An odd power of $-1$ is $-1$, so A is true; R is also true but is unrelated to the value of $(-1)^{101}$."),
 AR4(r"$3^0+2^0=2$.", r"$a^0=0$ for every non-zero number $a$.", "c",
     r"$3^0+2^0=1+1=2$ so A is true; R is false because $a^0=1$."),
 AR4(r"$2^3\times3^3=5^3$.", r"$a^m\times b^m=(ab)^m$.", "d",
     r"$2^3\times3^3=6^3=216$, not $5^3=125$; A is false, R is a true law."),
 AR4(r"$0.00045=4.5\times10^{-4}$.", r"In standard form a number is written as $m\times10^n$ with $1\le m<10$ and $n$ an integer.", "a",
     r"Moving the decimal point 4 places to the right gives $4.5$, so the number is $4.5\times10^{-4}$, which is R applied."),
 AR4(r"$(2^3)^2=2^6$.", r"$a^m\times a^n=a^{m+n}$.", "b",
     r"A follows from $(a^m)^n=a^{mn}$; R is a different true law, so it does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> The distance of the Earth from the Sun is about $150\,000\,000$ km and light travels at about $3\times10^{5}$ km per second. Students of a science club use these to answer questions on standard form. "
   r"(i) Write $150\,000\,000$ in standard form. (ii) Find the time light takes to reach the Earth from the Sun. (iii) Write that time in standard form. (iv) Light takes about 1.3 s to reach the Earth from the Moon. Find the Moon's distance in standard form.",
   r"(i) $1.5\times10^{8}$ km (1). (ii) Time $=\dfrac{1.5\times10^8}{3\times10^5}=0.5\times10^3=500$ s (1). (iii) $5\times10^{2}$ s (1). (iv) Distance $=3\times10^5\times1.3=3.9\times10^5$ km (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A biology student in Pune starts a culture of 5 bacteria that double in number every hour. She records the number after $n$ hours as $5\times2^{n}$. "
   r"(i) How many bacteria are there after 1 hour? (ii) How many are there after 6 hours? (iii) After how many whole hours does the count first exceed 1000? (iv) Using laws of exponents, find the ratio of the count after 8 hours to the count after 4 hours.",
   r"(i) $5\times2=10$ (1). (ii) $5\times2^6=5\times64=320$ (1). (iii) After 7 h: $5\times128=640$; after 8 h: $5\times256=1280>1000$, so 8 hours (1). (iv) $\dfrac{5\times2^8}{5\times2^4}=2^{8-4}=2^4=16$ (1+1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Kabir is revising laws of exponents and writes four expressions in his notebook. "
   r"(i) Find the value of $2^{-4}$. (ii) Find the value of $\left(\dfrac32\right)^{-2}$. (iii) Find the value of $7^5\div7^3$. (iv) Simplify $\dfrac{2^3\times2^{-5}}{2^{-2}}$ and state the law used.",
   r"(i) $\dfrac1{2^4}=\dfrac1{16}$ (1). (ii) $\left(\dfrac23\right)^2=\dfrac49$ (1). (iii) $7^{5-3}=7^2=49$ (1). (iv) $2^{3-5-(-2)}=2^{0}=1$ (1); laws $a^m\times a^n=a^{m+n}$ and $\dfrac{a^m}{a^n}=a^{m-n}$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Laws of exponents ($a,b\\neq0$; $m,n$ integers)", [
   r"$a^m\times a^n=a^{m+n}$ and $\dfrac{a^m}{a^n}=a^{m-n}$.",
   r"$(a^m)^n=a^{mn}$.",
   r"$a^m\times b^m=(ab)^m$ and $\dfrac{a^m}{b^m}=\left(\dfrac ab\right)^m$."]),
 ("Zero and negative exponents", [
   r"$a^0=1$ for $a\neq0$.",
   r"$a^{-n}=\dfrac1{a^n}$ and $\dfrac1{a^{-n}}=a^n$.",
   r"$\left(\dfrac ab\right)^{-n}=\left(\dfrac ba\right)^n$."]),
 ("Standard (scientific) form", [
   r"A number is written as $m\times10^n$ with $1\le m<10$ and $n$ an integer.",
   r"Large numbers: positive $n$ (e.g. $3\,50\,000=3.5\times10^5$). Small numbers: negative $n$ (e.g. $0.0072=7.2\times10^{-3}$).",
   r"To multiply or divide: operate on the $m$ parts, then add or subtract the exponents of 10; re-adjust to $1\le m<10$."]),
 ("Useful facts", [
   r"$(-1)^n=1$ if $n$ is even and $-1$ if $n$ is odd.",
   r"Powers help compare very large or small quantities: compare the exponents of 10 first, then $m$."]),
]

MISTAKES = [
 r"Writing $2^{-3}=-8$ or $-\dfrac18$; a negative exponent means the <b>reciprocal</b>, so $2^{-3}=\dfrac18$.",
 r"Adding the bases: $2^3\times2^4=4^7$ instead of $2^{3+4}=2^7$.",
 r"Saying $a^0=0$; for $a\neq0$ it is 1.",
 r"Multiplying exponents when multiplying powers of the same base ($a^m\times a^n=a^{mn}$) or adding them in $(a^m)^n$.",
 r"Leaving the answer as $25\times10^{4}$ or $0.25\times10^6$; in standard form the number part must satisfy $1\le m<10$.",
 r"Getting the sign of the exponent wrong for small numbers: $0.0003=3\times10^{-4}$, not $3\times10^{4}$.",
]
