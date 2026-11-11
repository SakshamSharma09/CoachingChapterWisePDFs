"""Class 9 Maths Ch 8 Sequences and Progressions - extras."""
from common import AR4, Q

AR = [
 AR4(r"The sequence $2, 5, 8, 11, \ldots$ is an arithmetic progression.", r"The difference between consecutive terms is the constant 3.", "a",
     r"$5-2=8-5=11-8=3$; a constant common difference is the definition of an AP."),
 AR4(r"The sequence $2, 4, 8, 16, \ldots$ is a geometric progression.", r"The sequence $1, 3, 5, 7, \ldots$ is an arithmetic progression.", "b",
     r"The ratio of consecutive terms of the first is 2 and the difference of consecutive terms of the second is 2; both are true, but they are unrelated statements."),
 AR4(r"The sum of the first 10 natural numbers is 55.", r"The sum of the first $n$ natural numbers is $n(n+1)$.", "c",
     r"$\dfrac{10\times11}{2}=55$, so A is true; R is false because the sum is $\dfrac{n(n+1)}{2}$."),
 AR4(r"The sequence $3, 6, 12, 18, \ldots$ is a geometric progression.", r"In a geometric progression the ratio of consecutive terms is constant.", "d",
     r"$\frac63=2,\ \frac{12}6=2,\ \frac{18}{12}=1.5$; the ratio is not constant, so A is false and R is true."),
 AR4(r"The 10th term of the AP $3, 7, 11, \ldots$ is 39.", r"The nth term of an AP is $t_n=a+(n-1)d$.", "a",
     r"$3+9\times4=39$, using R."),
 AR4(r"In an AP with first term 7 and common difference $-2$, the 5th term is $-1$.", r"The common difference of an AP can be negative.", "b",
     r"$7+4\times(-2)=-1$, so A is true; R is true but only says a negative difference is allowed, it does not give the value."),
]

CASE = [
 Q(r"<b>Case study.</b> Meera starts a recurring savings plan in a bank. She deposits Rs 100 in month 1, Rs 150 in month 2, Rs 200 in month 3, and so on, increasing the deposit by the same amount every month. "
   r"(i) Write the first term and the common difference. (ii) Find the deposit in month 12. (iii) Find the total amount deposited in 12 months. (iv) In which month is the deposit Rs 1000?",
   r"(i) $a=100,\ d=50$ (1). (ii) $t_{12}=100+11\times50=650$ (1). (iii) $S_{12}=\dfrac{12}{2}(100+650)=6\times750=4500$ (1). (iv) $100+(n-1)50=1000\Rightarrow n-1=18\Rightarrow n=19$ (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> An auditorium has 15 rows of seats. The first row has 20 seats and each next row has 2 seats more than the row in front of it. "
   r"(i) Find the common difference. (ii) Find the number of seats in the 15th row. (iii) Find the total number of seats in the auditorium. (iv) Find the number of seats in the last 5 rows (11th to 15th rows).",
   r"(i) $d=2$ (1). (ii) $t_{15}=20+14\times2=48$ (1). (iii) $S_{15}=\dfrac{15}{2}(20+48)=510$ (1). (iv) $S_{10}=\dfrac{10}{2}(40+18)=290$ (1); last 5 rows $=510-290=220$ seats (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A school launches a news bulletin. In stage 1, one student knows the news; in each later stage every student who knows it tells 3 new students, so the number of new students informed in successive stages is $1, 3, 9, 27, \ldots$ "
   r"(i) Find the common ratio. (ii) Find the number of new students informed in stage 5. (iii) Write the nth term. (iv) In which stage does the number first exceed 500?",
   r"(i) $r=3$ (1). (ii) $t_5=3^4=81$ (1). (iii) $t_n=3^{n-1}$ (1). (iv) $3^5=243<500$ and $3^6=729>500$, so $n-1=6$, i.e. stage 7 (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Sequences", [r"A sequence is an ordered list of numbers $t_1, t_2, t_3, \ldots$; $t_n$ is the nth term.",
   r"A rule such as $t_n=3n+2$ gives every term by putting $n=1, 2, 3, \ldots$"]),
 ("Arithmetic progression (AP)", [r"Common difference $d=t_{n+1}-t_n$ is constant.", r"nth term: $t_n=a+(n-1)d$.",
   r"Sum of first $n$ terms: $S_n=\dfrac n2\left[2a+(n-1)d\right]=\dfrac n2(a+l)$, where $l$ is the last term.",
   r"$t_n=S_n-S_{n-1}$ for $n\ge2$.", r"Sum of first $n$ natural numbers: $\dfrac{n(n+1)}{2}$.",
   r"Three numbers $a-d,\ a,\ a+d$ are in AP; the middle term is the average of its neighbours."]),
 ("Geometric progression (GP)", [r"Common ratio $r=\dfrac{t_{n+1}}{t_n}$ is constant (and non-zero).", r"nth term: $t_n=ar^{n-1}$.",
   r"Terms are multiplied by $r$ each step; $|r|<1$ makes the terms shrink, $r<0$ makes the signs alternate."]),
 ("Telling them apart", [r"AP: add the same number each time (constant difference). GP: multiply by the same number each time (constant ratio).",
   r"Example: $2, 5, 8, \ldots$ is an AP; $2, 6, 18, \ldots$ is a GP; $1, 4, 9, 16, \ldots$ is neither."]),
]

MISTAKES = [
 r"Writing $t_n=a+nd$ instead of $a+(n-1)d$, which makes the first term wrong.",
 r"Forgetting the factor $\dfrac n2$ in $S_n$, or using $n(n+1)$ for the sum of the first $n$ natural numbers (it is $\dfrac{n(n+1)}{2}$).",
 r"Using $t_n=ar^n$ for a GP instead of $ar^{n-1}$.",
 r"Calling a sequence an AP after checking only the first two terms; the difference must be the same for all consecutive terms.",
 r"Taking $S_n$ of an AP to be the nth term, or finding the nth term as $S_n$ instead of $S_n-S_{n-1}$.",
 r"Sign errors with a negative common difference or ratio, e.g. $t_5=7+4\times(-2)=-1$, not $7+4\times2$.",
]
