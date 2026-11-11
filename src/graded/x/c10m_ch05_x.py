"""Class 10 Maths Ch 5 Arithmetic Progressions - extras (nth term and sum of first n terms)."""
from common import AR4, Q

AR = [
 AR4(r"The list $3,7,11,15,\dots$ forms an AP.", r"In an AP the difference between any two consecutive terms is the same constant.", "a",
     r"$7-3=11-7=15-11=4$; R is the defining property of an AP."),
 AR4(r"The 10th term of the AP $2,5,8,\dots$ is 29.", r"The nth term of an AP with first term a and common difference d is $a_n=a+nd$.", "c",
     r"$a_{10}=2+9\times3=29$, so A is true; the correct formula is $a+(n-1)d$, so R is false."),
 AR4(r"The sequence $1,4,9,16,\dots$ is an AP.", r"In an AP, the difference between consecutive terms is constant.", "d",
     r"Differences are $3,5,7,\dots$, which are not constant: A false; R is true."),
 AR4(r"The sum of the first 10 natural numbers is 55.", r"The nth term of an AP is $a_n=a+(n-1)d$.", "b",
     r"$S_{10}=\tfrac{10}{2}(1+10)=55$ is true and R is a true formula, but R is not what gives the sum."),
 AR4(r"The sequence whose nth term is $a_n=4n-1$ is an AP.", r"For this sequence $a_{n+1}-a_n=4$ for every n.", "a",
     r"$a_{n+1}-a_n=(4n+3)-(4n-1)=4$, a constant, which is why it is an AP."),
 AR4(r"The sum of the first 15 odd natural numbers is 225.", r"The sum of first n terms of an AP is $S_n=\dfrac n2\,[a+(n-1)d]$.", "c",
     r"$S_{15}=\tfrac{15}{2}(2\times1+14\times2)=225=15^2$, so A is true; the correct formula has $2a$, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> Mohan starts a monthly savings plan. He saves ₹ 100 in the first month and increases his saving by ₹ 20 every month. "
   r"(i) Write the first term and the common difference of the AP formed by his monthly savings. (ii) How much does he save in the 10th month? (iii) Find his total savings in the first 12 months. (iv) In which month will he save ₹ 400, and what will his total savings be up to that month?",
   r"(i) $a=100$, $d=20$ (1). (ii) $a_{10}=100+9\times20=₹\,280$ (1). (iii) $S_{12}=\tfrac{12}{2}[2(100)+11(20)]=6\times420=₹\,2520$ (1). (iv) $100+(n-1)20=400\Rightarrow n=16$ (1); $S_{16}=\tfrac{16}{2}(100+400)=₹\,4000$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> The school auditorium has 15 rows of seats. The first row has 20 seats and each next row has 2 more seats than the row before it. "
   r"(i) Write the number of seats in the first three rows. (ii) How many seats are there in the last (15th) row? (iii) Find the total number of seats in the auditorium. (iv) Find the number of seats in the 8th row and the total collection if every seat is sold at ₹ 150.",
   r"(i) 20, 22, 24 (1). (ii) $a_{15}=20+14\times2=48$ (1). (iii) $S_{15}=\tfrac{15}{2}(20+48)=510$ (1). (iv) $a_8=20+7\times2=34$ seats (1); collection $=510\times150=₹\,76{,}500$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Kavya has a 360-page storybook. She reads 10 pages on the first day and every day she reads 2 pages more than the day before. "
   r"(i) How many pages does she read on the 2nd and 3rd days? (ii) How many pages does she read on the 10th day? (iii) How many pages does she read in the first 5 days? (iv) In how many days does she finish the book, and how many pages does she read on the last day?",
   r"(i) 12 and 14 pages (1). (ii) $a_{10}=10+9\times2=28$ (1). (iii) $S_5=\tfrac52(20+8)=70$ (1). (iv) $\tfrac n2[20+2(n-1)]=360\Rightarrow n^2+9n-360=0\Rightarrow(n+24)(n-15)=0$, so $n=15$ days (1); last day $=10+14\times2=38$ pages (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Arithmetic progression", [r"A list $a,\ a+d,\ a+2d,\dots$ with first term a and common difference $d=a_{k+1}-a_k$ (constant).",
   r"d can be positive, negative or zero."]),
 ("nth term", [r"$a_n=a+(n-1)d$.",
   r"nth term from the end of a finite AP with last term l: $l-(n-1)d$.",
   r"Check for AP: $a_{k+1}-a_k$ is the same for all k."]),
 ("Sum of first n terms", [r"$S_n=\dfrac n2\,[2a+(n-1)d]$.",
   r"$S_n=\dfrac n2\,(a+l)$ when the last term l is known.",
   r"$a_n=S_n-S_{n-1}$.",
   r"Sum of first n natural numbers $=\dfrac{n(n+1)}{2}$; first n odd numbers $=n^2$."]),
 ("Useful results", [r"Three consecutive terms: $a-d,\ a,\ a+d$. Four terms: $a-3d,\ a-d,\ a+d,\ a+3d$.",
   r"If a, b, c are in AP then $2b=a+c$.",
   r"Number of terms of $a,\dots,l$: $n=\dfrac{l-a}{d}+1$."]),
 ("Word problems", [r"Decide the first term, d and what is asked (a term or a sum); reject non-integer or negative n."]),
]

MISTAKES = [
 r"Using $a_n=a+nd$ instead of $a+(n-1)d$.",
 r"Writing $S_n=\dfrac n2[a+(n-1)d]$; the bracket needs $2a$.",
 r"Taking d as $a_1-a_2$; it is $a_2-a_1$ (a decreasing AP has negative d).",
 r"Using $S_n$ when only $a_n$ is asked (or the other way round) in word problems.",
 r"Not rejecting a negative or fractional value of n obtained from a quadratic in n.",
 r"Calling a list an AP after checking only the first two differences.",
]
